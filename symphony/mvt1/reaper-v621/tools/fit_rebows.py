"""mvt1 c01 (critic A #2): fit build/rebow_fills.json for every automatic or listed re-bow, from a rendered cycle.

Usage: fit_rebows.py PREV_CYCLE PARTS_JSON [--write] [--tracks "Violoncellos,Violins II"] [--skip "Track:qn" ...]
  PREV_CYCLE: the cycle whose stems are measured (cycles/cNN/render).
  PARTS_JSON: the parts.json that produced that render (its tempo map and each track's "rebows" list: [qn, end of the
  split note, pitch], written by score_to_parts.py).

Method (the movement II c26 fit, kit LEARNINGS 6, made robust for many short re-bows): stereo-power level of the stem,
50 ms RMS every 20 ms, smoothed over 0.12 s (L). For a re-bow at time r whose piece runs to e (the next re-bow of the
same note, or the note's end):
  pre   = mean L over [r - 0.45, r - 0.10] s, minus the plan's own level change (P) at that time;
  P(t)  = the planned level relative to r: parts.json vol_db + PLAN_DB_PER_CC x CC11 (a printed hairpin across a re-bow
          is kept, not flattened);
  fill  = over [0, W] (W = min(1.5 s, piece length - 0.3 s)): pre + P(r + t) - L(r + t), smoothed over 0.1 s, clamped
          to CLAMP, blended over the last 0.3 s of the window into
  hold  = pre - mean(L - P) over [W - 0.3, piece end - 0.3] (at most 2.8 s after r), held to the next re-bow.
After the last re-bow of a note the hold returns to 0 over the note's last 0.1 s. Points are [s after the re-bow, dB],
the first one [-0.04, previous hold]. score_to_parts.py applies each list from its re-bow to the next list.

Re-bows whose fitted values would have to move by more than CLAMP are clamped; re-bows listed with --skip and those
whose pieces were shorter than MIN_PIECE_S are left out. Without --write it prints a summary only.

mvt1 c02 (critic A #6, C #4): a refit on a render that already carries fitted shapes. The old shapes (build/rebow_fills.json
as it is when this runs, rebuilt as score_to_parts.py applies them) are taken out of both the plan and the stem level,
and each piece's target is the level before the note's first re-bow: pre of re-bow i = its measured pre without the old
shape plus the new hold of re-bow i-1 (the c01 fit chained each piece to the previous piece's unfilled level). The fill
starts PRE_FILL_S before the re-bow (the bar-10 celli hole started 0.16 s early), and its first EARLY_S may reach
CLAMP_EARLY (that shape sat at its +9 cap). A 0.04 s smoothing (A #6) was tried and rejected: these stems swing +-6 dB
at about 3 Hz inside a held note (vibrato and bow), and the 0.04 s fit followed the swing (+12 / -5 / +9 dB in 0.8 s).
--hold-max-after QN:DB caps the hold of every re-bow at or after score qn QN at DB (the final ppp chord: the holds of
+3..+5 dB made the morendo swell 3 dB in its last 3 s).

mvt1 c53 (critic A #1): --only "Track:qn" (repeatable) refits the listed re-bows alone. Every other list of the track is
kept as it is in build/rebow_fills.json, and so is the chain of holds: an unlisted re-bow hands its existing hold on,
and a listed re-bow that is not the last of its note keeps its existing hold (its fill is refitted from the existing
previous hold into the existing hold), so the next list still starts from the value it was fitted on. The hold of a
listed re-bow that is the last of its note is refitted. With --write only the listed keys are replaced.
--render-dir DIR reads the stems from DIR (a range render) and --render-t0 QN gives the score qn at which those files
start (0 when left out). --fine adds a second stage to the listed re-bows: the 0.12 s level smoothing of the first
stage is wider than a bow change (a 0.1-0.25 s hole centred 0.05-0.15 s after the re-bow was left 4-9 dB deep under a
fill that looked right at 0.12 s). The stem level with the old shapes out and the new fill in is measured again at
30 ms RMS every 10 ms; what is still under the target line (pre + the plan) inside FINE_WIN, smoothed over
FINE_SMOOTH_S, is added to the fill on a 0.02 s grid: dips only (0..FINE_MAX dB, tapered at the window's edges), the
total limited to FINE_CLAMP_MAX. It follows the vibrato swing of these stems only inside FINE_WIN. --dump FILE writes, per fitted re-bow, the times, the raw (unsmoothed, unclamped) fill, the
written fill and the old fill, for a before/after simulation.
"""
import glob, json, os, sys
import numpy as np
import soundfile as sf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOP, WIN, SMOOTH_S, FILL_SMOOTH_S = 0.02, 0.05, 0.12, 0.10
PRE_FILL_S, PRE_WIN = 0.12, (0.45, 0.10)   # mvt1 c02: the fill starts PRE_FILL_S before the re-bow
CLAMP_EARLY, EARLY_S = (-6.0, 10.0), 0.4
WINDOW_S, BLEND_S, HOLD_MAX_S, MIN_PIECE_S = 1.5, 0.3, 2.8, 1.0
CLAMP = (-6.0, 9.0)
PLAN_DB_PER_CC = 0.25
STEP_S = 0.04

cyc, pj = sys.argv[1], sys.argv[2]
args = sys.argv[3:]
WRITE = "--write" in args
ONLY, SKIP = None, set()
HOLD_MAX = None
ONLY_KEYS, RDIR, RT0_QN, DUMP = None, None, 0.0, None   # mvt1 c53 (see the docstring)
FINE = "--fine" in args
FINE_WIN, FINE_STEP, FINE_SMOOTH_S, FINE_MAX, FINE_CLAMP_MAX, FINE_TAPER = (0.24, 0.40), 0.02, 0.03, 5.0, 15.0, (0.06, 0.08)
for i, a in enumerate(args):
    if a == "--only":
        tn, q = args[i + 1].rsplit(":", 1)
        ONLY_KEYS = (ONLY_KEYS or set()) | {(tn, round(float(q), 3))}
    if a == "--render-dir":
        RDIR = args[i + 1]
    if a == "--render-t0":
        RT0_QN = float(args[i + 1])
    if a == "--dump":
        DUMP = args[i + 1]
    if a == "--tracks":
        ONLY = set(x.strip() for x in args[i + 1].split(","))
    if a == "--skip":
        tn, q = args[i + 1].rsplit(":", 1)
        SKIP.add((tn, round(float(q), 3)))
    if a == "--hold-max-after":
        HOLD_MAX = tuple(float(x) for x in args[i + 1].split(":"))
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


def step_at(lane, q, first=0.0):
    v = first
    for x, y in lane:
        if x <= q + 1e-9:
            v = y
        else:
            break
    return v


def level(name, hop=HOP, win=WIN, smooth_s=SMOOTH_S):
    f = glob.glob(f"{RDIR or f'{ROOT}/cycles/c{int(cyc):02d}/render'}/[0-9][0-9]_{name}.wav")
    x, sr = sf.read(f[0], dtype="float32")
    p = (x.astype(np.float64) ** 2).mean(1) if x.ndim > 1 else x.astype(np.float64) ** 2
    h, w = int(hop * sr), int(win * sr)
    c = np.cumsum(np.concatenate([np.zeros(w // 2 + 1), p, np.zeros(w)]))
    idx = np.arange(0, len(p), h)
    L = 10 * np.log10((c[idx + w] - c[idx]) / w + 1e-12)
    k = max(1, int(round(smooth_s / hop)))
    if k <= 1:
        return L
    return np.convolve(np.pad(L, (k, k), mode="edge"), np.ones(k) / k, "same")[k:-k]


def smooth(v, sec):
    k = max(1, int(round(sec / STEP_S)))
    if len(v) <= k:
        return v
    return np.convolve(np.pad(v, (k, k), mode="edge"), np.ones(k) / k, "same")[k:-k]


QG = np.arange(0.0, D["end_qn"] + 8.0, 0.01)
QS = np.array([q2s(q) for q in QG])
RF_PATH = f"{ROOT}/build/rebow_fills.json"
RF = json.load(open(RF_PATH)) if os.path.exists(RF_PATH) else {}
out, report = {}, []
RT0_S = q2s(RT0_QN) if RDIR else 0.0
dump = {}


def old_list(nm, p):   # mvt1 c53: the existing list of a re-bow (None when it has none)
    for k_, v_ in RF.get(nm, {}).items():
        if not k_.startswith("_") and abs(float(k_) - p) < 1e-3:
            return v_
    return None


for t in D["tracks"]:
    nm = t["name"]
    rb = t.get("rebows") or []
    if not rb or (ONLY and nm not in ONLY) or (ONLY_KEYS is not None and not any(tn_ == nm for tn_, _ in ONLY_KEYS)):
        continue
    L = level(nm)
    at = lambda s: float(np.interp((s - RT0_S) / HOP, np.arange(len(L)), L))
    if FINE:
        Lf = level(nm, 0.01, 0.03, 0.0)
        atf = lambda s: float(np.interp((s - RT0_S) / 0.01, np.arange(len(Lf)), Lf))
    vol, cc11 = t.get("vol_db", []), t.get("cc11", [])
    plan = lambda q: step_at(vol, q) + PLAN_DB_PER_CC * step_at(cc11, q, 64)
    # mvt1 c02: the re-bow shapes that the measured render carried (build/rebow_fills.json as it is when this runs),
    # rebuilt as score_to_parts.py applies them, in seconds: each list from its first point to the next list's first
    # point, its last value held. plan_nf = the plan without them; the target of every piece is the level before the
    # note's first re-bow (pre of re-bow i = the measured pre minus the old fill there plus the new hold of re-bow i-1)
    olds = sorted((float(k), v) for k, v in RF.get(nm, {}).items() if not k.startswith("_"))
    seg_ = []
    for j_, (oq_, opts_) in enumerate(olds):
        r_ = q2s(oq_)
        xs_ = [r_ + a_ for a_, _ in opts_]; ys_ = [b_ for _, b_ in opts_]
        end_ = (q2s(olds[j_ + 1][0]) + olds[j_ + 1][1][0][0]) if j_ + 1 < len(olds) else q2s(D["end_qn"] + 0.5)
        if end_ > xs_[-1] + 1e-4:
            xs_.append(end_); ys_.append(ys_[-1])
        seg_.append((xs_[0], xs_[-1], np.array(xs_), np.array(ys_)))

    def fmeas(s):
        for a_, b_, xs_, ys_ in seg_:
            if a_ <= s < b_:
                return float(np.interp(s, xs_, ys_))
        return 0.0
    rb = sorted(rb, key=lambda r: tuple(r[:3]))
    fills = {}
    prev_hold, prev_end, prev_p = 0.0, None, None
    for i, (p, e, pitch, *_) in enumerate(rb):
        nxt = rb[i + 1][0] if i + 1 < len(rb) and rb[i + 1][0] < e - 1e-6 else None
        last_of_note = nxt is None
        pe = nxt if nxt is not None else e
        if prev_end is None or abs(prev_end - e) > 1e-3:   # first re-bow of a new note
            prev_hold, prev_p = 0.0, None
        prev_end = e
        r, ps = q2s(p), q2s(pe)
        piece = ps - r
        if (nm, round(p, 3)) in SKIP or piece < MIN_PIECE_S:
            if last_of_note:
                prev_hold = 0.0
            continue
        ol_ = old_list(nm, p) if ONLY_KEYS is not None else None
        if ONLY_KEYS is not None and (nm, round(p, 3)) not in ONLY_KEYS:
            # an unlisted re-bow: its existing list stays and hands its hold on (0 after the last re-bow of a note)
            if ol_ is None or last_of_note:
                prev_hold = 0.0
            else:
                prev_hold = float(ol_[-1][1])
            if ol_ is not None:
                prev_p = p
            continue

        def plan_s(s):   # the plan at absolute time s (seconds), without the old re-bow shapes
            return plan(float(np.interp(s, QS, QG))) - fmeas(s)

        def samp(s):     # the stem level without the old re-bow shapes
            return at(s) - fmeas(s)
        p0 = plan_s(r - 0.25)
        pw = np.arange(r - PRE_WIN[0], r - PRE_WIN[1], HOP)
        pre = np.mean([samp(s) - (plan_s(s) - p0) for s in pw]) + prev_hold
        W = min(WINDOW_S, piece - 0.3)
        pf = min(PRE_FILL_S, max(0.04, (r - q2s(prev_p)) - 0.5)) if prev_p is not None else PRE_FILL_S
        ts = np.arange(-pf, W + 1e-9, STEP_S)
        raw = np.array([pre + (plan_s(r + x) - p0) - samp(r + x) for x in ts])
        h1 = min(r + HOLD_MAX_S, ps - 0.3)
        hs = np.arange(r + max(0.0, W - 0.3), max(h1, r + W - 0.29), HOP)
        post = np.mean([samp(s) - (plan_s(s) - p0) for s in hs])
        hold = float(np.clip(pre - post, *CLAMP))
        if HOLD_MAX is not None and p >= HOLD_MAX[0] - 1e-6:
            hold = min(hold, HOLD_MAX[1])
        if ONLY_KEYS is not None and ol_ is not None and not last_of_note:
            hold = float(ol_[-1][1])   # the next list was fitted on this value
        sm = smooth(raw, FILL_SMOOTH_S)
        f = np.where(ts < EARLY_S, np.clip(sm, *CLAMP_EARLY), np.clip(sm, *CLAMP))
        bl = np.clip((ts - (W - BLEND_S)) / BLEND_S, 0, 1)
        f = f * (1 - bl) + hold * bl
        pts = [[round(float(-pf - 0.04), 3), round(prev_hold, 2)]] + [[round(float(x), 3), round(float(y), 2)] for x, y in zip(ts, f)]
        fine_add = None
        if FINE and ONLY_KEYS is not None:
            # mvt1 c53: second stage (see the docstring): the residual dip of the 30 ms level under the target line
            cx_, cy_ = [p_[0] for p_ in pts], [p_[1] for p_ in pts]
            tf = np.arange(-FINE_WIN[0], min(FINE_WIN[1], W - BLEND_S) + 1e-9, FINE_STEP)
            tf = tf[r + tf > (q2s(prev_p) + 0.3 if prev_p is not None else -1e9)]
            co_ = np.interp(tf, cx_, cy_)
            res_ = np.array([pre + (plan_s(r + x) - p0) - (atf(r + x) - fmeas(r + x) + c_) for x, c_ in zip(tf, co_)])
            k_ = max(1, int(round(FINE_SMOOTH_S / FINE_STEP)))
            sm_ = np.convolve(np.pad(res_, (k_, k_), mode="edge"), np.ones(k_) / k_, "same")[k_:-k_] if k_ > 1 else res_
            tp_ = np.clip((tf - tf[0]) / FINE_TAPER[0], 0, 1) * np.clip((tf[-1] - tf) / FINE_TAPER[1], 0, 1)
            fine_add = np.clip(sm_, 0.0, FINE_MAX) * tp_
            tot_ = np.minimum(co_ + fine_add, np.maximum(co_, FINE_CLAMP_MAX))
            fine_add = tot_ - co_
            if fine_add.max() >= 0.5:
                head_ = [[round(float(min(cx_[0], tf[0] - 0.04)), 3), round(prev_hold, 2)]]
                mid_ = [[round(float(x), 3), round(float(y), 2)] for x, y in zip(tf, tot_)]
                tail_ = [p_ for p_ in pts[1:] if p_[0] > tf[-1] + 1e-6]
                pts = head_ + mid_ + tail_
        if last_of_note:
            pts += [[round(piece - 0.1, 3), round(hold, 2)], [round(piece + 0.02, 3), 0.0]]
            prev_hold = 0.0
        else:
            prev_hold = hold
        prev_p = p
        fills[f"{p:.4f}".rstrip("0").rstrip(".")] = pts
        if DUMP:
            dump[f"{nm}:{p:.4f}".rstrip("0").rstrip(".")] = {
                "r_s": r, "ts": [float(x) for x in ts], "raw": [float(x) for x in raw], "new": [float(x) for x in f],
                "old": [fmeas(r + float(x)) for x in ts], "level": [at(r + float(x)) for x in ts], "pre": float(pre),
                "hold": float(hold), "piece_s": float(piece),
                "fine_t": [] if fine_add is None else [float(x) for x in tf],
                "fine_add": [] if fine_add is None else [float(x) for x in fine_add]}
        dip = float(raw[(ts >= 0) & (ts < 1.0)].max())
        report.append((nm, p, round(dip, 1), round(hold, 1), round(piece, 2)))
    out[nm] = fills

for nm in sorted(set(r[0] for r in report)):
    rs = [r for r in report if r[0] == nm]
    d = np.array([r[2] for r in rs]); h = np.array([r[3] for r in rs])
    print(f"{nm:15s} {len(rs):3d} re-bows: max fill in the first 1 s median {np.median(d):+.1f} dB (p90 {np.percentile(d, 90):+.1f}),"
          f" hold median {np.median(h):+.1f} (|hold| >= 3 dB: {(np.abs(h) >= 3).sum()})")
if WRITE:
    doc = RF.get("_doc", "")
    new = {"_doc": (doc + " " if doc else "") + f"fitted by tools/fit_rebows.py on cycle {cyc} (see its docstring)."}
    for k, v in RF.items():
        if k != "_doc" and k not in out:
            new[k] = v
    if ONLY_KEYS is not None:   # mvt1 c53: the listed keys replace the track's existing ones, the other lists stay
        for nm_, fl_ in out.items():
            keep_ = {k_: v_ for k_, v_ in RF.get(nm_, {}).items()
                     if k_.startswith("_") or not any(abs(float(k_) - float(nk_)) < 1e-3 for nk_ in fl_)}
            keep_.update(fl_)
            out[nm_] = dict(sorted(keep_.items(), key=lambda kv: (0, 0.0) if kv[0].startswith("_") else (1, float(kv[0]))))
    new.update(out)
    json.dump(new, open(RF_PATH, "w"), indent=0)
    print("wrote", RF_PATH)
if DUMP:
    json.dump(dump, open(DUMP, "w"))
