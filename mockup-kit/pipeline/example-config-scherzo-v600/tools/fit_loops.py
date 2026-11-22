"""mvt1 c02 (critic A #4, C #4): fit periodic inverse loop profiles (build/loop_profiles.json) on long held notes from a
rendered cycle: the kit method (mockup-kit LEARNINGS 6 and 10, movement II c17/c26), as a tool.

Usage: fit_loops.py PREV_CYCLE PARTS_JSON "Track:score_onset[:period_s]" ... [--clamp 3] [--write]
  PREV_CYCLE: the cycle whose stems are measured; PARTS_JSON: the parts.json that produced that render.
  Each listed note (matched by its score onset "sq", within 0.02 qn): stereo-power level of the stem (50 ms RMS every
  20 ms), minus the planned envelope (parts.json vol_db), from the moved start + LP_START_S (0.8 s) to the note end -
  LP_END_S (0.3 s), detrended by a centred moving average one period long. The period is the given one, or the lag of
  the highest autocorrelation between 2.5 and 5.0 s. The detrended level is folded at the period in 20 ms phase bins;
  corr_db = -(mean of each bin), clamped to +-clamp dB, smoothed over 3 bins (circular). score_to_parts.py adds corr_db
  at the phase (t - t0) mod period from t0 + 0.8 s to the end - 0.3 s, faded over 0.3 s (LP_* there).
  The planned envelope must not already hold a profile for the note (the fit measures the sample, not the residual):
  a note that has one in build/loop_profiles.json is refit as old + new residual.
Prints, per note: period, autocorrelation at it, folded swing (p95 - p5) before and the swing predicted after.
"""
import glob, json, os, sys
import numpy as np
import soundfile as sf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOP, WIN, BIN = 0.02, 0.05, 0.02
LP_START_S, LP_END_S = 0.8, 0.3
cyc, pj = sys.argv[1], sys.argv[2]
args = sys.argv[3:]
WRITE = "--write" in args
CLAMP = float(args[args.index("--clamp") + 1]) if "--clamp" in args else 3.0
specs = [a for i, a in enumerate(args) if ":" in a and (i == 0 or args[i - 1] != "--clamp")]
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
    f = glob.glob(f"{ROOT}/cycles/c{int(cyc):02d}/render/[0-9][0-9]_{name}.wav")
    x, sr = sf.read(f[0], dtype="float32")
    p = (x.astype(np.float64) ** 2).mean(1) if x.ndim > 1 else x.astype(np.float64) ** 2
    h, w = int(HOP * sr), int(WIN * sr)
    c = np.cumsum(np.concatenate([np.zeros(w // 2 + 1), p, np.zeros(w)]))
    idx = np.arange(0, len(p), h)
    return 10 * np.log10((c[idx + w] - c[idx]) / w + 1e-12)


def acf(y, lag_s):
    k = int(round(lag_s / HOP))
    if k >= len(y) - 5:
        return np.nan
    a, b = y[:-k], y[k:]
    return float(np.corrcoef(a, b)[0, 1])


LP_PATH = f"{ROOT}/build/loop_profiles.json"
LP = json.load(open(LP_PATH)) if os.path.exists(LP_PATH) else {}
tracks = {t["name"]: t for t in D["tracks"]}
qg = np.arange(0.0, D["end_qn"] + 8.0, 0.01)
sg = np.array([q2s(q) for q in qg])
for sp in specs:
    parts = sp.split(":")
    nm, sq = parts[0], float(parts[1])
    per = float(parts[2]) if len(parts) > 2 else None
    t = tracks[nm]
    n = min(t["notes"], key=lambda n: abs(n.get("sq", n["qn"]) - sq))
    if abs(n.get("sq", n["qn"]) - sq) > 0.02:
        print(f"{nm} {sq}: no note"); continue
    L = level(nm)
    t0 = max(0.0, q2s(n["qn"]))
    ta, tb = t0 + LP_START_S, q2s(n["qn"] + n["dur"]) - LP_END_S
    ts = np.arange(ta, tb, HOP)
    vol = t.get("vol_db", [])
    plan = np.array([step_at(vol, float(np.interp(s, sg, qg))) for s in ts])
    y = np.interp(ts / HOP, np.arange(len(L)), L) - plan
    if per is None and (tb - ta) < 2 * 2.5 + 0.1:
        print(f"{nm} {sq}: {tb - ta:.1f} s is under two periods; give the period"); continue
    if per is None:
        lags = np.arange(2.5, min(5.0, (tb - ta) / 2), 0.02)
        a_ = [acf(y - np.convolve(np.pad(y, (100, 100), mode="edge"), np.ones(200) / 200, "same")[100:-100], l) for l in lags]
        per = float(lags[int(np.nanargmax(a_))])
    k = max(1, int(round(per / HOP)))
    yd = y - np.convolve(np.pad(y, (k, k), mode="edge"), np.ones(k) / k, "same")[k:-k]
    nb = int(round(per / BIN))
    ph = (((ts - t0) % per) / BIN).astype(int) % nb
    fold = np.array([yd[ph == b].mean() if (ph == b).any() else 0.0 for b in range(nb)])
    fold = np.convolve(np.concatenate([fold[-1:], fold, fold[:1]]), np.ones(3) / 3, "valid")
    old = (LP.get(nm, {}) or {}).get(f"{sq}", (LP.get(nm, {}) or {}).get(str(round(sq, 3))))
    oldc = np.array(old["corr_db"]) if old and abs(old["period_s"] - per) < 0.01 and len(old["corr_db"]) == nb else np.zeros(nb)
    corr = np.clip(oldc - fold, -CLAMP, CLAMP)
    after = yd + (corr - oldc)[ph]
    sw0 = np.percentile(fold, 95) - np.percentile(fold, 5)
    sw1 = np.percentile(fold + (corr - oldc), 95) - np.percentile(fold + (corr - oldc), 5)
    print(f"{nm:12s} {sq:7.2f} ({tb - ta:5.1f} s): period {per:.2f} s, acf {acf(yd, per):+.2f}; folded swing {sw0:.1f} dB"
          f" -> {sw1:.1f} predicted; detrended p95-p5 {np.percentile(yd, 95) - np.percentile(yd, 5):.1f} -> "
          f"{np.percentile(after, 95) - np.percentile(after, 5):.1f}")
    LP.setdefault(nm, {})[f"{sq}"] = {"period_s": round(per, 3), "corr_db": [round(float(v), 2) for v in corr]}
if WRITE:
    LP["_doc"] = ("Periodic inverse loop profiles {track: {score onset: {period_s, corr_db (20 ms phase bins)}}}, applied by "
                  "score_to_parts.py from the moved start + 0.8 s to the end - 0.3 s. mvt1 c02: fitted by tools/fit_loops.py.")
    json.dump(LP, open(LP_PATH, "w"), indent=0)
    print("wrote", LP_PATH)
