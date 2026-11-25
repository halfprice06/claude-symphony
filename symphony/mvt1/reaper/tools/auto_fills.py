"""c16 (critic C #2): early fills as a measured pass instead of hand edits.

Usage: auto_fills.py PREV_CYCLE PARTS_JSON [--write] [--exclude "Track:onset" ...]
  PREV_CYCLE: the cycle whose render is measured (cycles/cNN/render stems).
  PARTS_JSON: the parts.json that produced that render (its tempo map, moved onsets and keyswitches).

For every legato join (the previous note sounds into the target, a new pitch, target on a "Leg" articulation, target
0.45 s or longer) on the lead lines below, the 30 ms envelope (5 ms hop) of the track's stem is measured around the
target: reference = the lower of the previous note's body (0.35 s up to 0.05 s before the moved onset) and the target's
body (+0.4..+0.7 s after the score onset); dip = reference - the minimum between the moved onset - 0.05 s and the score
onset + 0.4 s; t_min = time of that minimum relative to the score onset.

  - a join with no entry in build/early_fills.json that dips 5 dB or more gets
      {"db": min(6, dip - 3), "pre_s": max(0, -t_min), "hold_s": clamp(t_min + 0.05, 0.10, 0.35)}
  - mvt1 c15: an existing entry whose hole minimum comes before the fill is full is retimed (pre_s, hold_s, db at
    least dip - 3, cap 8) on every measured track; mvt1 c16: for a target led RETIME_LEAD_MIN_S or more the fill is
    full from RETIME_AFTER_MOVED_S after the moved onset (or 0.05 s before the measured minimum, if earlier) and held
    to RETIME_HOLD_S
  - an existing entry (wind and horn lines only) that still dips 5 dB or more gets db + min(3, dip - 4), capped at 8,
    and hold_s moved to clamp(t_min + 0.05, 0.10, 0.35) (held only to the sag minimum: the samples swell by
    themselves after about +0.3 s, LEARNINGS c11)

c17 (critic A #2):
  (a) Flute 1, Oboe 1 and Cor anglais are measured on a 200 ms window (one vibrato cycle; their high notes carry 10 dB of
      vibrato amplitude modulation that a 30 ms window reads as holes), with a 4 dB threshold.
  (b) Overshoot rule, every track: over = peak of the 200 ms envelope in [moved onset - 0.1 s, score onset + 0.4 s] minus
      the louder of the two bodies (200 ms). An existing entry with over > 2 dB is lowered by (over - 1) dB, or deleted
      when that reaches 0; it is never raised in the same pass.
  (c) Lowered and deleted entries are listed in "_auto" as "lowered"/"removed".
All windows are centred on their frame time.

mvt1 c12 (critic C #1): decrescendo guard. A target whose score onset lies inside or at the end of a printed decrescendo
of its own track (parts.json `hairpins`, start < onset <= end + 0.05 qn) may be filled at most to DECRESC_UNDER_DB under
the previous note's body: a new or raised fill is capped at prev_body - DECRESC_UNDER_DB - the hole's level (floored at
0); an existing fill whose 200 ms front peak stands over prev_body - DECRESC_UNDER_DB is reported, and lowered by the
excess ("guarded") only with --guard-existing (on the c11 render that would have removed or cut 25 hand and auto fills,
several of them fitted in c10/c11, so it is not a default). The fills at 188/588 had cancelled the decrescendo (the quarter 4 dB over the eighth before it).

Written entries are listed in the track's "_auto" key ({onset: "new"/"raised"}), so they can be regenerated.
Without --write it prints the plan only.
"""
import glob, json, os, sys
import numpy as np
import soundfile as sf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRACKS = ["Flute 1", "Oboe 1", "Cor anglais", "Clarinet 1", "Bass clarinet", "Horn 1", "Violin I solo", "Violoncellos"]
RAISE_TRACKS = ["Flute 1", "Oboe 1", "Cor anglais", "Clarinet 1", "Bass clarinet", "Horn 1"]
# the lead-line tracks are score-specific: build/auto_fills.json {"tracks": [...], "raise": [...]} replaces the lists above
if os.path.exists(f"{ROOT}/build/auto_fills.json"):
    _af = json.load(open(f"{ROOT}/build/auto_fills.json"))
    TRACKS, RAISE_TRACKS = _af.get("tracks", TRACKS), _af.get("raise", RAISE_TRACKS)
HOP, WIN = 0.005, 0.030
MIN_DIP = 5.0
WIN_TRACK = {"Flute 1": 0.200, "Oboe 1": 0.200, "Cor anglais": 0.200}   # c17 (A #2a)
MIN_DIP_TRACK = {"Flute 1": 4.0, "Oboe 1": 4.0, "Cor anglais": 4.0}
OVER_WIN, OVER_MAX = 0.200, 2.0   # c17 (A #2b)
DECRESC_UNDER_DB = 1.5   # mvt1 c12 (C #1)
RETIME_LEAD_MIN_S, RETIME_AFTER_MOVED_S, RETIME_HOLD_S = 0.10, 0.08, 0.35   # mvt1 c16 (critic A #4)

cyc, pj = sys.argv[1], sys.argv[2]
WRITE = "--write" in sys.argv[3:]
GUARD_EXISTING = "--guard-existing" in sys.argv[3:]   # mvt1 c12: lower existing fills too (default: report only)
EXCL = set()
args = sys.argv[3:]
for i, a in enumerate(args):
    if a == "--exclude":
        tn, q = args[i + 1].rsplit(":", 1)
        EXCL.add((tn, float(q)))
D = json.load(open(pj))
T = D["tempo"]


def q2s(q):
    t, lq, lb = 0.0, 0.0, T[0][1]
    for tq, b in T:
        if tq >= q:
            break
        t += (tq - lq) * 60 / lb; lq, lb = tq, b
    return t + (q - lq) * 60 / lb


# mvt1 c03: renders c00-c02 sound 1/6 qn early on the parts.json map (tools/rendermap.py, build/render_shift.json)
import rendermap
q2s = rendermap.wrap(q2s, cyc)


_AUDIO = {}


def env(name, win=WIN):
    if name not in _AUDIO:
        f = glob.glob(f"{ROOT}/cycles/c{int(cyc):02d}/render/[0-9][0-9]_{name}.wav")
        x, sr = sf.read(f[0], dtype="float32")
        _AUDIO[name] = (x.mean(1) if x.ndim > 1 else x, sr)
    x, sr = _AUDIO[name]
    h, w = int(HOP * sr), int(win * sr)
    # centred window: frame i covers [i*HOP - win/2, i*HOP + win/2]
    c = np.cumsum(np.concatenate([np.zeros(w // 2 + 1), x.astype(np.float64) ** 2, np.zeros(w)]))
    idx = np.arange(0, len(x), h)
    return 10 * np.log10((c[idx + w] - c[idx]) / w + 1e-12)


def arts(t):
    ks = sorted(t["ks"], key=lambda k: k["qn"])
    out = []
    for n in t["notes"]:
        a = t["first_art"]
        for k in ks:
            if k["qn"] <= n["qn"] + 1e-6:
                a = k["art"]
        out.append(a)
    return out


EF_PATH = f"{ROOT}/build/early_fills.json"
EF = json.load(open(EF_PATH))
plan = []
for t in D["tracks"]:
    nm = t["name"]
    if nm not in TRACKS:
        continue
    E = env(nm, WIN_TRACK.get(nm, WIN))
    E2 = env(nm, OVER_WIN)
    mind = MIN_DIP_TRACK.get(nm, MIN_DIP)
    fr = lambda s: int(round(s / HOP))
    ns = sorted(t["notes"], key=lambda n: n["qn"])
    A = dict(zip([id(n) for n in t["notes"]], arts(t)))
    have = {float(k): k for k in EF.get(nm, {}) if not k.startswith("_")}
    for a, b in zip(ns, ns[1:]):
        art = A[id(b)] or ""
        if "Leg" not in art or b["pitch"] == a["pitch"] or a["qn"] + a["dur"] < b["qn"] - 0.01:
            continue
        sq = b.get("sq", b["qn"])
        s_mv, s_sq, s_end = q2s(b["qn"]), q2s(sq), q2s(b["qn"] + b["dur"])
        if s_end - s_sq < 0.45 or (nm, sq) in EXCL:
            continue
        p0, p1 = max(q2s(a["qn"]) + 0.1, s_mv - 0.35), s_mv - 0.05
        b0, b1 = s_sq + 0.4, min(s_sq + 0.7, s_end - 0.05)
        if b1 - b0 < 0.025:
            b0, b1 = s_sq + 0.3, s_end
        if p1 - p0 < 0.025 or b1 - b0 < 0.025:
            continue
        ref = min(np.median(E[fr(p0):fr(p1)]), np.median(E[fr(b0):fr(b1)]))
        if ref < -62:
            continue
        w0, w1 = fr(s_mv - 0.05), fr(s_sq + 0.4)
        seg = E[w0:w1]
        k = int(np.argmin(seg))
        dip, t_min = float(ref - seg[k]), (w0 + k) * HOP - s_sq
        key = next((v for q, v in have.items() if abs(q - sq) < 0.02), None)
        # mvt1 c12 (C #1): inside or at the end of a printed decrescendo the target stays under the note before
        in_dec = any(h[2] == "decresc" and h[0] < sq - 1e-6 and sq <= h[1] + 0.05 for h in t.get("hairpins", []))
        cap = None
        if in_dec:
            prev_body = float(np.median(E2[fr(p0):fr(p1)]))
            cap = max(0.0, prev_body - DECRESC_UNDER_DB - float(seg[k]))
            if key is not None:
                old = EF[nm][key]
                pre0 = old.get("pre_s", 0.0) if isinstance(old, dict) else 0.0
                front = float(np.max(E2[fr(max(s_mv - 0.1, s_sq - pre0 - 0.05)):fr(s_sq + 0.4)]))
                exc = front - (prev_body - DECRESC_UNDER_DB)
                if exc > 0.3 and GUARD_EXISTING:
                    db0 = old["db"] if isinstance(old, dict) else float(old)
                    ndb = round(db0 - exc, 1)
                    if ndb <= 0:
                        plan.append((nm, sq, exc, t_min, old, None, "removed"))
                    else:
                        plan.append((nm, sq, exc, t_min, old, dict(old, db=ndb) if isinstance(old, dict) else ndb,
                                     "guarded"))
                    continue
                if exc > 0.3:
                    print(f"  guard (not applied; --guard-existing): {nm} {sq:.2f} existing fill front {exc:+.1f} dB over prev body - {DECRESC_UNDER_DB}")
        if key is not None:   # c17 (A #2b): overshoot of an existing fill, on the 200 ms envelope
            body2 = max(np.median(E2[fr(p0):fr(p1)]), np.median(E2[fr(b0):fr(b1)]))
            old = EF[nm][key]
            pre0 = old.get("pre_s", 0.0) if isinstance(old, dict) else 0.0
            # the window starts no earlier than the fill itself (a transition peak before the fill is not its overshoot)
            over = float(np.max(E2[fr(max(s_mv - 0.1, s_sq - pre0 - 0.05)):fr(s_sq + 0.4)]) - body2)
            if over > OVER_MAX:
                db0 = old["db"] if isinstance(old, dict) else float(old)
                ndb = round(db0 - (over - 1), 1)
                if ndb <= 0:
                    plan.append((nm, sq, over, t_min, old, None, "removed"))
                elif isinstance(old, dict):
                    plan.append((nm, sq, over, t_min, old, dict(old, db=ndb), "lowered"))
                else:
                    plan.append((nm, sq, over, t_min, old, ndb, "lowered"))
                continue
        if dip < mind:
            continue
        hold = round(min(0.35, max(0.10, t_min + 0.05)), 2)
        if key is not None and isinstance(EF[nm][key], dict) and t_min < -EF[nm][key].get("pre_s", 0.0) + 0.02:
            # mvt1 c15 (critic A #1): the hole's minimum comes before the fill is full (entries carrying c03's negative
            # pre_s, while the legato targets now start 0.11-0.22 s early): retime it on every measured track
            old = EF[nm][key]
            db0 = old["db"]
            ndb = min(8.0, max(db0, dip - 3))
            if cap is not None:
                ndb = min(ndb, max(db0, cap))
            pre_ = max(0.0, -t_min)
            lead_ = s_sq - s_mv
            if lead_ >= RETIME_LEAD_MIN_S:
                # mvt1 c16 (critic A #4): a led legato target's hole moves 0.05-0.1 s between renders (c15: retimed fills
                # were full exactly at one render's minimum and the next render's hole came before it): full from
                # RETIME_AFTER_MOVED_S after the moved onset, or 0.05 s before this render's minimum if earlier
                pre_ = max(-t_min + 0.05, lead_ - RETIME_AFTER_MOVED_S)
                hold = RETIME_HOLD_S
            new = {"db": round(ndb, 1), "pre_s": round(pre_, 2), "hold_s": hold}
            plan.append((nm, sq, dip, t_min, old, new, "retimed"))
            continue
        if key is None:
            ndb = round(min(6.0, dip - 3, cap if cap is not None else 99.0), 1)
            if ndb < 0.5:
                continue
            new = {"db": ndb, "pre_s": round(max(0.0, -t_min), 2), "hold_s": hold}
            plan.append((nm, sq, dip, t_min, None, new, "new"))
        elif nm in RAISE_TRACKS:
            old = EF[nm][key]
            db0 = old["db"] if isinstance(old, dict) else float(old)
            pre = old.get("pre_s", 0.0) if isinstance(old, dict) else round(max(0.0, -t_min), 2)
            add = min(3.0, dip - 4, cap if cap is not None else 99.0)
            if add < 0.3:
                continue
            new = {"db": round(min(8.0, db0 + add), 1), "pre_s": pre, "hold_s": hold}
            plan.append((nm, sq, dip, t_min, old, new, "raised"))

for nm, sq, dip, tm, old, new, kind in plan:   # for "lowered"/"removed", dip holds the overshoot
    print(f"{nm:14s} {sq:7.2f} dip {dip:5.1f} at {tm:+.3f} s  {kind:6s} {json.dumps(old) if old is not None else '-':40s} -> {json.dumps(new)}")
print(f"{len(plan)} entries ({sum(1 for p in plan if p[6] == 'new')} new, {sum(1 for p in plan if p[6] == 'raised')} raised, {sum(1 for p in plan if p[6] == 'retimed')} retimed)")
if WRITE:
    for nm, sq, dip, tm, old, new, kind in plan:
        tr = EF.setdefault(nm, {})
        key = next((k for k in tr if not k.startswith("_") and abs(float(k) - sq) < 0.02), None)
        if key is None:
            key = f"{sq:g}"
        if kind == "removed":
            del tr[key]
            tr.setdefault("_auto", {})[key] = f"c{int(cyc) + 1:02d} removed (over {dip:.1f} dB)"
            continue
        tr[key] = new
        what = f"over {dip:.1f} dB" if kind in ("lowered", "guarded") else f"dip {dip:.1f} dB at {tm:+.2f} s"
        tr.setdefault("_auto", {})[key] = f"c{int(cyc) + 1:02d} {kind} ({what})"
    json.dump(EF, open(EF_PATH, "w"), indent=1, ensure_ascii=False)
    print("written", EF_PATH)
