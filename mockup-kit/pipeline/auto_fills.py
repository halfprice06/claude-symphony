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

Written entries are listed in the track's "_auto" key ({onset: "new"/"raised"}), so they can be regenerated.
Without --write it prints the plan only.
"""
import glob, json, os, sys
import numpy as np
import soundfile as sf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRACKS = ["Flute 1", "Oboe 1", "Cor anglais", "Clarinet 1", "Bass clarinet", "Horn 1", "Violin I solo", "Violoncellos"]
RAISE_TRACKS = ["Flute 1", "Oboe 1", "Cor anglais", "Clarinet 1", "Bass clarinet", "Horn 1"]
HOP, WIN = 0.005, 0.030
MIN_DIP = 5.0
WIN_TRACK = {"Flute 1": 0.200, "Oboe 1": 0.200, "Cor anglais": 0.200}   # c17 (A #2a)
MIN_DIP_TRACK = {"Flute 1": 4.0, "Oboe 1": 4.0, "Cor anglais": 4.0}
OVER_WIN, OVER_MAX = 0.200, 2.0   # c17 (A #2b)

cyc, pj = sys.argv[1], sys.argv[2]
WRITE = "--write" in sys.argv[3:]
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
        if key is None:
            new = {"db": round(min(6.0, dip - 3), 1), "pre_s": round(max(0.0, -t_min), 2), "hold_s": hold}
            plan.append((nm, sq, dip, t_min, None, new, "new"))
        elif nm in RAISE_TRACKS:
            old = EF[nm][key]
            db0 = old["db"] if isinstance(old, dict) else float(old)
            pre = old.get("pre_s", 0.0) if isinstance(old, dict) else round(max(0.0, -t_min), 2)
            new = {"db": round(min(8.0, db0 + min(3.0, dip - 4)), 1), "pre_s": pre, "hold_s": hold}
            plan.append((nm, sq, dip, t_min, old, new, "raised"))

for nm, sq, dip, tm, old, new, kind in plan:   # for "lowered"/"removed", dip holds the overshoot
    print(f"{nm:14s} {sq:7.2f} dip {dip:5.1f} at {tm:+.3f} s  {kind:6s} {json.dumps(old) if old is not None else '-':40s} -> {json.dumps(new)}")
print(f"{len(plan)} entries ({sum(1 for p in plan if p[6] == 'new')} new, {sum(1 for p in plan if p[6] == 'raised')} raised)")
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
        what = f"over {dip:.1f} dB" if kind == "lowered" else f"dip {dip:.1f} dB at {tm:+.2f} s"
        tr.setdefault("_auto", {})[key] = f"c{int(cyc) + 1:02d} {kind} ({what})"
    json.dump(EF, open(EF_PATH, "w"), indent=1, ensure_ascii=False)
    print("written", EF_PATH)
