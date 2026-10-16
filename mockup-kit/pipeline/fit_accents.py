"""mvt1 c07 (ONE_TIME, Dan's item 8): fit per-accent swell levels so every accent sits about TARGET dB over the
unaccented notes around it at the same printed level.

Usage: fit_accents.py PREV RENDERED_PARTS [--family brass] [--lo 2.0] [--hi 4.0] [--target 3.0] [--iters 4] [--write]
  PREV            cycle number of the render to measure (cycles/cNN/render stems)
  RENDERED_PARTS  the parts.json that render was made from (its vol_db is what the stems carry)
The build directory's current config is rebuilt with score_to_parts.py into a scratch parts.json on every iteration;
build/accent_fits.json is only written with --write.

Per accent (score onset with a printed accent on a GENTLE_ACCENT family track):
  level  = power mean of the stem over onset + 0.05 .. min(onset + 0.35, note end - 0.02) s
  nbrs   = up to two unaccented onsets each side, within --near (2.5) qn, CC11 within 6 of the accent's, same window
  over   = level - power mean of the neighbours' levels
  resid  = over - (accent's mean volume-envelope dB - neighbours' mean), from RENDERED_PARTS: what the samples, rows
           and CC11 give, which a level-only change does not move
The prediction for a new build is resid + its envelope difference. Accents whose articulation (or a neighbour's)
differs between the rendered and the new build cannot be predicted and are left at the family's default swell. An
accent predicted outside [lo, hi] gets a fitted swell (the family's swell shape, at most 5 dB) and, when even no swell
leaves it over hi, a negative step trim on the whole note; accents inside [lo, hi] are left alone.
Also prints 2-5 kHz energy over the first 80 ms minus the body (+0.15 .. +0.5 s) per accent.
"""
import json, os, sys, bisect, collections, subprocess, argparse
import numpy as np, soundfile as sf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = f"{ROOT}/build"
PY = sys.executable
ap = argparse.ArgumentParser()
ap.add_argument("prev", type=int)
ap.add_argument("rendered_parts")
ap.add_argument("--family", default="brass")
ap.add_argument("--lo", type=float, default=2.0)
ap.add_argument("--hi", type=float, default=4.0)
ap.add_argument("--target", type=float, default=3.0)
ap.add_argument("--iters", type=int, default=4)
ap.add_argument("--near", type=float, default=2.5)   # neighbours within this many qn
ap.add_argument("--max-swell", type=float, default=5.0)
ap.add_argument("--min-trim", type=float, default=-6.0)
ap.add_argument("--max-trim", type=float, default=3.0)
# c08 (actor): no negative step trim on an accent whose note is longer than this many qn, or that a printed crescendo
# arrives on (the c08 render: a -6 dB step on Violins I's whole-bar ff arrival at qn 100 took the section 4.7 dB down
# in bar 26); 0 = off
ap.add_argument("--keep-long-qn", type=float, default=1.5)
# c08 (critic A #2): a note of this many qn or less that starts a slur is not a neighbour (0 = off)
ap.add_argument("--pickup-qn", type=float, default=0.5)
ap.add_argument("--scratch", default=os.environ.get("TMPDIR", "/tmp"))
ap.add_argument("--write", action="store_true")
A = ap.parse_args()
sys.path.insert(0, f"{ROOT}/tools")
from rendermap import shift_for   # noqa: E402
if shift_for(A.prev):
    sys.exit("renders made with the shifted c00-c02 tempo map are not supported")

EV = collections.defaultdict(list)
for l in open(f"{BUILD}/mockup-events.tsv"):
    f = l.rstrip("\n").split("\t")
    if len(f) >= 5:
        EV[f[0]].append((float(f[1]), f[3], f[4:]))


def q2s_of(P):
    tempo = sorted(P["tempo"])
    tq, ts = [0.0], [0.0]
    for (q0, b0), (q1, b1) in zip(tempo, tempo[1:]):
        ts.append(ts[-1] + (q1 - q0) * 60 / b0); tq.append(q1)

    def q2s(q):
        i = max(0, bisect.bisect_right(tq, q) - 1)
        return ts[i] + (q - tq[i]) * 60 / tempo[i][1]
    return q2s, tempo


def lane(pts, q):
    xs = [p[0] for p in pts]
    i = bisect.bisect_right(xs, q + 1e-9) - 1
    return pts[max(i, 0)][1]


def arts_of(t):
    ks = sorted(t["ks"], key=lambda k: k["qn"]); kq = [k["qn"] for k in ks]

    def art(n):
        i = bisect.bisect_right(kq, n["qn"] + 1e-6) - 1
        return ks[i]["art"] if i >= 0 else t.get("first_art")
    return art


def windows(P, t):
    """per score onset: (moved qn, window start/end in s, art, cc, accented)"""
    q2s, tempo = q2s_of(P)
    acc = {round(q, 3) for s in t["staves"] for q, k, v in EV[s] if k == "script" and v and v[0] == "accent"}
    slur0 = {round(q, 3) for s in t["staves"] for q, k, v in EV[s] if k == "slur" and v and v[0] == "-1"}
    art = arts_of(t)
    out = {}
    for n in sorted(t["notes"], key=lambda n: n["sq"]):
        k = round(n["sq"], 3)
        if k in out:
            continue
        ts = q2s(n["qn"]); te = q2s(n["qn"] + n["dur"])
        a, b = ts + 0.05, min(ts + 0.35, te - 0.02)
        bpm = lane(tempo, n["qn"])
        out[k] = dict(qn=n["qn"], a=a, b=b, qa=n["qn"] + 0.05 * bpm / 60, qb=n["qn"] + (b - ts) * bpm / 60,
                      art=art(n), cc=lane(t["cc11"], n["qn"] + 0.02), acc=k in acc, ts=ts, te=te, ok=b - a >= 0.08,
                      # c08 (critic A #2): a slur's short first note plays the legato row's slow first-note layer
                      pickup=k in slur0 and n["qn"] + n["dur"] - n["sq"] <= A.pickup_qn + 0.1,
                      slen=n["qn"] + n["dur"] - n["sq"],
                      arrival=any(h[2] == "cresc" and abs(h[1] - n["sq"]) < 0.3 for h in t.get("hairpins", [])))
    return out


def env_mean(t, w):
    qs = np.linspace(w["qa"], max(w["qb"], w["qa"] + 0.001), 12)
    return 10 * np.log10(np.mean(10 ** (np.array([lane(t["vol_db"], q) for q in qs]) / 10)))


def pm(v):
    return 10 * np.log10(np.mean(np.asarray(v, dtype=np.float64)) + 1e-15)


def band(x, sr, t0, t1, f0=2000, f1=5000):
    a, b = int(t0 * sr), int(t1 * sr)
    seg = x[a:b].astype(np.float64)
    tot = 0.0
    for ch in range(seg.shape[1]):
        s = seg[:, ch] * np.hanning(len(seg)); F = np.fft.rfft(s); f = np.fft.rfftfreq(len(s), 1 / sr)
        tot += np.sum(np.abs(F[(f >= f0) & (f < f1)]) ** 2)
    return 10 * np.log10(tot / seg.shape[1] / max(1, b - a) + 1e-20)


def plan(P0, P1):
    """per accent: dict with resid, env_over (new), predicted, hf, valid"""
    rows = []
    d = f"{ROOT}/cycles/c{A.prev:02d}/render"
    T1 = {t["name"]: t for t in P1["tracks"]}
    for t0 in P0["tracks"]:
        if t0["family"] != A.family:
            continue
        t1 = T1[t0["name"]]
        f = [x for x in os.listdir(d) if x[:2] != "00" and x.endswith(".wav") and x[3:-4] == t0["name"]][0]
        x, sr = sf.read(f"{d}/{f}", dtype="float32")
        p = (x.astype(np.float64) ** 2).mean(1)
        W0, W1 = windows(P0, t0), windows(P1, t1)
        on = sorted(W0)

        for j, k in enumerate(on):
            w = W0[k]
            if not w["acc"] or not w["ok"] or k not in W1:
                continue
            L = pm(p[int(w["a"] * sr):int(w["b"] * sr)])
            nb = [q for q in on[max(0, j - 2):j] + on[j + 1:j + 3]
                  if not W0[q]["acc"] and abs(q - k) <= A.near and W0[q]["ok"] and abs(W0[q]["cc"] - w["cc"]) <= 6 and q in W1
                  and not (A.pickup_qn > 0 and W0[q]["pickup"])]
            hf = None
            if w["te"] - w["ts"] > 0.3:
                hf = band(x, sr, w["ts"], w["ts"] + 0.08) - band(x, sr, w["ts"] + 0.15, min(w["ts"] + 0.5, w["te"] - 0.02))
            r = dict(track=t0["name"], q=k, art0=w["art"], art1=W1[k]["art"], hf=None if hf is None else round(hf, 1), nb=nb,
                     keep=A.keep_long_qn > 0 and (W1[k]["slen"] >= A.keep_long_qn - 1e-6 or W1[k]["arrival"]))
            if nb:
                Ln = [pm(p[int(W0[q]["a"] * sr):int(W0[q]["b"] * sr)]) for q in nb]
                over = L - pm([10 ** (v / 10) for v in Ln])
                e0 = env_mean(t0, w) - np.mean([env_mean(t0, W0[q]) for q in nb])
                e1 = env_mean(t1, W1[k]) - np.mean([env_mean(t1, W1[q]) for q in nb])
                valid = w["art"] == W1[k]["art"] and all(W0[q]["art"] == W1[q]["art"] for q in nb)
                r.update(over=round(over, 2), resid=round(over - e0, 2), env1=round(e1, 2),
                         pred=round(over - e0 + e1, 2), valid=valid)
            rows.append(r)
    return rows


P0 = json.load(open(A.rendered_parts))
fits_path = f"{BUILD}/accent_fits.json"
orig = json.load(open(fits_path)) if os.path.exists(fits_path) else {}
fits = {k: dict(v) for k, v in orig.items() if not k.startswith("_")}
scratch_parts = os.path.join(A.scratch, "fit_accents_parts.json")
scratch_fits = os.path.join(A.scratch, "fit_accents_fits.json")
ks_maps = os.path.expanduser("~/.rpr-bridge/libs/ew_ho/ks_maps.json")


def build(fits_):
    """rebuild parts.json with these fits (build/accent_fits.json swapped in for the run, then restored)"""
    keep = open(fits_path).read() if os.path.exists(fits_path) else None
    try:
        json.dump(fits_, open(fits_path, "w"), indent=1)
        r = subprocess.run([PY, f"{ROOT}/tools/score_to_parts.py", ".", ks_maps, scratch_parts], cwd=BUILD,
                           capture_output=True, text=True)
        if r.returncode:
            sys.exit(r.stderr[-2000:])
    finally:
        if keep is None:
            os.remove(fits_path)
        else:
            open(fits_path, "w").write(keep)
    return json.load(open(scratch_parts))


def default_swell(track):
    # GENTLE_ACCENT db in movement I (brass 2.5 since c06, wind 3.5, string 3.0); only the starting point of the iteration
    return {"brass": 2.5, "wind": 3.5, "string": 3.0}.get(A.family, 2.5)


for it in range(A.iters):
    P1 = build(fits)
    rows = plan(P0, P1)
    moved = 0
    for r in rows:
        if "pred" not in r or not r["valid"]:
            continue
        cur = fits.get(r["track"], {}).get(f"{r['q']:g}")
        if r.get("keep") and isinstance(cur, list) and cur[1] < 0:   # c08: drop an old negative trim, refit next pass
            fits[r["track"]][f"{r['q']:g}"] = cur[0]
            moved += 1
            continue
        inside = A.lo <= r["pred"] <= A.hi
        if cur is None and inside:
            continue
        if cur is not None and abs(r["pred"] - A.target) < 0.25:
            continue
        sw, tr = (cur if isinstance(cur, list) else [cur, 0.0]) if cur is not None else [default_swell(r["track"]), 0.0]
        dlt = A.target - r["pred"]
        # the swell covers about 0.85 of the 0.05-0.35 s window; a trim covers all of it
        if tr < 0 and dlt > 0:
            u = min(dlt, -tr); tr += u; dlt -= u
        if tr > 0 and dlt < 0:
            u = min(-dlt, tr); tr -= u; dlt += u
        sw_new = sw + dlt / 0.85
        if sw_new < 0:
            tr += sw_new * 0.85; sw_new = 0.0
        if sw_new > A.max_swell:   # an accent under its neighbours even with the largest swell: a positive step
            tr = min(A.max_trim, tr + (sw_new - A.max_swell) * 0.85); sw_new = A.max_swell
        tr = max(tr, A.min_trim)
        if r.get("keep") and tr < 0:   # c08: a long or arrival accent keeps its body level (the swell only goes down)
            tr = 0.0
        fits.setdefault(r["track"], {})[f"{r['q']:g}"] = [round(float(sw_new), 2), round(float(tr), 2)] \
            if abs(tr) > 0.05 else round(float(sw_new), 2)
        moved += 1
    print(f"iteration {it + 1}: {moved} fits changed", file=sys.stderr)
    if not moved:
        break

P1 = build(fits)
rows = plan(P0, P1)
print("track          q        art (rendered -> new)        over  resid  pred   hf   fit")
for r in rows:
    print(f"{r['track'][:14]:14s} {r['q']:7.2f}  {r['art0'][:14]:14s} -> {r['art1'][:14]:14s} "
          f"{r.get('over', float('nan')):5.1f} {r.get('resid', float('nan')):5.1f} {r.get('pred', float('nan')):5.1f} "
          f"{'' if r['hf'] is None else r['hf']:>5}  {fits.get(r['track'], {}).get(format(r['q'], 'g'), '')}"
          f"{'' if r.get('valid', True) else '  (articulation changed: not predicted)'}")
pv = [r["pred"] for r in rows if "pred" in r and r["valid"]]
print(f"predicted: {sum(A.lo <= v <= A.hi for v in pv)}/{len(pv)} in [{A.lo}, {A.hi}], median {np.median(pv):+.2f}, "
      f"min {min(pv):+.1f}, max {max(pv):+.1f}; hf > 3 dB: {sum(1 for r in rows if r['hf'] is not None and r['hf'] > 3)}")
if A.write:
    out = {"_doc": orig.get("_doc", "Per-accent fitted swells {track: {score qn: swell dB or [swell dB, step trim dB]}} "
                                     "written by tools/fit_accents.py (score_to_parts.py ACCENT_FITS).")}
    out.update({k: dict(sorted(v.items(), key=lambda kv: float(kv[0]))) for k, v in sorted(fits.items())})
    json.dump(out, open(fits_path, "w"), indent=1)
    print("wrote", fits_path)
