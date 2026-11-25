"""mvt1 c01 (critic A #2): fit build/rebow_fills.json for every automatic or listed re-bow, from a rendered cycle.

Usage: fit_rebows.py PREV_CYCLE PARTS_JSON [--write] [--tracks "Violoncellos,Violins II"] [--skip "Track:qn" ...]
  [--stems DIR] (mvt2 c29: measure simulated stems from tools/stem_fix.py --out DIR where present)
  PREV_CYCLE: the cycle whose stems are measured (cycles/cNN/render).
  PARTS_JSON: the parts.json that produced that render (its tempo map and each track's "rebows" list: [qn, end of the
  split note, pitch], written by score_to_parts.py).

Method (the movement II c26 fit, kit LEARNINGS 6, made robust for many short re-bows): stereo-power level of the stem,
50 ms RMS every 20 ms, smoothed over 0.12 s (L). For a re-bow at time r whose piece runs to e (the next re-bow of the
same note, or the note's end):
  pre   = mean L over [r - 0.45, r - 0.10] s, minus the plan's own level change (P) at that time;
  P(t)  = the planned level relative to r: parts.json vol_db + PLAN_DB_PER_CC x CC11 + 20 log10(CC7 / 127) (mvt2 c42;
          a printed hairpin or a CC7 fade across a re-bow is kept, not flattened);
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
mvt2 c34 (critic A #2): --window "Track:S" fits that track's pieces over S s (default WINDOW_S 1.5): the basses' pedal
pieces swelled +4 dB and fell -6 dB at +1.2..+2.4 s, outside the 1.5 s window, and the hold averaged that away.
--hold-max-after QN:DB caps the hold of every re-bow at or after score qn QN at DB (the final ppp chord: the holds of
+3..+5 dB made the morendo swell 3 dB in its last 3 s).
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
WINDOW_BY = {}   # mvt2 c34 (critic A #2): --window "Track:S" fits that track's pieces over S s instead of WINDOW_S
for i, a in enumerate(args):
    if a == "--window":
        tn, w_ = args[i + 1].rsplit(":", 1)
        WINDOW_BY[tn.strip()] = float(w_)
    if a == "--tracks":
        ONLY = set(x.strip() for x in args[i + 1].split(","))
    if a == "--skip":
        tn, q = args[i + 1].rsplit(":", 1)
        SKIP.add((tn, round(float(q), 3)))
    if a == "--hold-max-after":
        HOLD_MAX = tuple(float(x) for x in args[i + 1].split(":"))
# mvt2 c29: --stems DIR measures the stems in DIR (a stem_fix.py simulation of the cycle's render, e.g. with stale loop
# profiles taken out) where DIR has the track's stem, else the cycle's own render
STEMS = args[args.index("--stems") + 1] if "--stems" in args else None
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


def level(name):
    f = glob.glob(f"{STEMS}/[0-9][0-9]_{name}.wav") if STEMS else []
    f = f or glob.glob(f"{ROOT}/cycles/c{int(cyc):02d}/render/[0-9][0-9]_{name}.wav")
    x, sr = sf.read(f[0], dtype="float32")
    p = (x.astype(np.float64) ** 2).mean(1) if x.ndim > 1 else x.astype(np.float64) ** 2
    h, w = int(HOP * sr), int(WIN * sr)
    c = np.cumsum(np.concatenate([np.zeros(w // 2 + 1), p, np.zeros(w)]))
    idx = np.arange(0, len(p), h)
    L = 10 * np.log10((c[idx + w] - c[idx]) / w + 1e-12)
    k = max(1, int(round(SMOOTH_S / HOP)))
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
for t in D["tracks"]:
    nm = t["name"]
    rb = t.get("rebows") or []
    if not rb or (ONLY and nm not in ONLY):
        continue
    L = level(nm)
    at = lambda s: float(np.interp(s / HOP, np.arange(len(L)), L))
    vol, cc11 = t.get("vol_db", []), t.get("cc11", [])
    # mvt2 c42 (critics A #1, C #1): the CC7 lane is part of the plan (pre-hall linear amplitude, 20 log10(cc7/127)):
    # without it the fit read the bar 66 niente's CC7 fade as a hole and filled it back in (holds +4..+8 dB)
    cc7 = t.get("cc7", [])
    plan = lambda q: (step_at(vol, q) + PLAN_DB_PER_CC * step_at(cc11, q, 64)
                      + 20 * np.log10(max(1.0, step_at(cc7, q, 127)) / 127.0))
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

        def plan_s(s):   # the plan at absolute time s (seconds), without the old re-bow shapes
            return plan(float(np.interp(s, QS, QG))) - fmeas(s)

        def samp(s):     # the stem level without the old re-bow shapes
            return at(s) - fmeas(s)
        p0 = plan_s(r - 0.25)
        pw = np.arange(r - PRE_WIN[0], r - PRE_WIN[1], HOP)
        pre = np.mean([samp(s) - (plan_s(s) - p0) for s in pw]) + prev_hold
        W = min(WINDOW_BY.get(nm, WINDOW_S), piece - 0.3)
        pf = min(PRE_FILL_S, max(0.04, (r - q2s(prev_p)) - 0.5)) if prev_p is not None else PRE_FILL_S
        ts = np.arange(-pf, W + 1e-9, STEP_S)
        raw = np.array([pre + (plan_s(r + x) - p0) - samp(r + x) for x in ts])
        h1 = min(r + max(HOLD_MAX_S, W + 0.3), ps - 0.3)
        hs = np.arange(r + max(0.0, W - 0.3), max(h1, r + W - 0.29), HOP)
        post = np.mean([samp(s) - (plan_s(s) - p0) for s in hs])
        hold = float(np.clip(pre - post, *CLAMP))
        if HOLD_MAX is not None and p >= HOLD_MAX[0] - 1e-6:
            hold = min(hold, HOLD_MAX[1])
        sm = smooth(raw, FILL_SMOOTH_S)
        f = np.where(ts < EARLY_S, np.clip(sm, *CLAMP_EARLY), np.clip(sm, *CLAMP))
        bl = np.clip((ts - (W - BLEND_S)) / BLEND_S, 0, 1)
        f = f * (1 - bl) + hold * bl
        pts = [[round(float(-pf - 0.04), 3), round(prev_hold, 2)]] + [[round(float(x), 3), round(float(y), 2)] for x, y in zip(ts, f)]
        if last_of_note:
            pts += [[round(piece - 0.1, 3), round(hold, 2)], [round(piece + 0.02, 3), 0.0]]
            prev_hold = 0.0
        else:
            prev_hold = hold
        prev_p = p
        fills[f"{p:.4f}".rstrip("0").rstrip(".")] = pts
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
    new.update(out)
    json.dump(new, open(RF_PATH, "w"), indent=0)
    print("wrote", RF_PATH)
