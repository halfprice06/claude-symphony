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
# mvt1 c13 (critic A #2): an accent whose previous note on the track is a short pickup (--pickup-max-qn or less,
# unaccented) ending at the accent must also stand --pickup-over dB over that pickup (level of the pickup from its onset
# + 0.03 s to the accent's onset); the fitted swell is raised until both the neighbour target and this hold (0 = off)
ap.add_argument("--pickup-over", type=float, default=0.0)
ap.add_argument("--pickup-max-qn", type=float, default=0.5)
# the pickup term never raises an accent more than this many dB over its same-dynamic neighbours (trim the pickup instead)
ap.add_argument("--pickup-cap-over", type=float, default=5.0)
# mvt1 c17 (critic A #2): a note written this many qn or longer is measured as its loudest 200 ms inside [score onset
# - 0.05 s, min(score onset + 0.5 s, end - 0.02 s)] (accents and neighbours alike): string accents peak at +0.30 s (p75
# +0.43), after the moved-onset + 0.05..0.35 s window of a led legato target ends, so the fit asked 2-2.5 dB too much
# (0 = off: every note on the old window)
ap.add_argument("--peak-long-qn", type=float, default=1.0)
# mvt1 c17 (critic A #2): cap on swell + step trim per accent, by family (29 of 126 string fits totalled 6 dB or more)
ap.add_argument("--max-total", type=float, default=None)
# mvt1 c17 (critic B #1): accents to leave as they are, "Track:q" (repeatable)
ap.add_argument("--skip", action="append", default=[])
ap.add_argument("--scratch", default=os.environ.get("TMPDIR", "/tmp"))
ap.add_argument("--write", action="store_true")
A = ap.parse_args()
if A.max_total is None:
    A.max_total = {"string": 4.5, "wind": 6.0, "brass": 6.0}.get(A.family, 6.0)
SKIP = {(x.rsplit(":", 1)[0], round(float(x.rsplit(":", 1)[1]), 3)) for x in A.skip}
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
        # written length: the longest note event at this onset on the track's staves, or the played length when a tie
        # merged notes into one (mockup-events.tsv lists tied notes separately)
        wlen = max([float(v[1]) for s_ in t["staves"] for q_, k_, v in EV[s_] if k_ == "note" and abs(q_ - n["sq"]) < 1e-3]
                   + [n["qn"] + n["dur"] - n["sq"]])
        # mvt1 c17 (critic A #2): long notes are measured as a 200 ms peak from the score onset (see --peak-long-qn)
        peak = A.peak_long_qn > 0 and wlen >= A.peak_long_qn - 1e-6
        if peak:
            ss = q2s(n["sq"])
            a, b = ss - 0.05, min(ss + 0.5, te - 0.02)
        out[k] = dict(qn=n["qn"], a=a, b=b, qa=n["qn"] + 0.05 * bpm / 60, qb=n["qn"] + (b - ts) * bpm / 60, peak=peak,
                      art=art(n), cc=lane(t["cc11"], n["qn"] + 0.02), acc=k in acc, ts=ts, te=te, ok=b - a >= 0.08,
                      # c08 (critic A #2): a slur's short first note plays the legato row's slow first-note layer
                      pickup=k in slur0 and n["qn"] + n["dur"] - n["sq"] <= A.pickup_qn + 0.1,
                      slen=n["qn"] + n["dur"] - n["sq"], sq=n["sq"], qend=n["qn"] + n["dur"],
                      arrival=any(h[2] == "cresc" and abs(h[1] - n["sq"]) < 0.3 for h in t.get("hairpins", [])),
                      # mvt1 c15 (critic A #5): a legato target moved more than 0.05 s early: its window starts on the
                      # transition peak, which the fit read as the accent (Violas 120: a -6 dB step, 9.7 dB under the pickup)
                      legearly="Leg" in (art(n) or "") and q2s(n["sq"]) - ts > 0.05)
    return out


def env_mean(t, w):
    qs = np.linspace(w["qa"], max(w["qb"], w["qa"] + 0.001), 12)
    if w.get("pqa") is not None:   # mvt1 c17: a peak-measured note: the envelope over its loudest 200 ms
        qs = np.linspace(w["pqa"], w["pqb"], 12)
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
        t1 = T1.get(t0["name"])
        f = [x for x in os.listdir(d) if x[:2] != "00" and x.endswith(".wav") and x[3:-4] == t0["name"]]
        if t1 is None or not f:   # mvt1 c13: a track new in this build (or not rendered) has nothing to measure
            continue
        f = f[0]
        x, sr = sf.read(f"{d}/{f}", dtype="float32")
        p = (x.astype(np.float64) ** 2).mean(1)
        W0, W1 = windows(P0, t0), windows(P1, t1)
        on = sorted(W0)
        q2s0, tempo0 = q2s_of(P0)

        def s2q(s_):   # inverse of q2s0 (bisection; the tempo map is the same in both builds)
            lo, hi = -10.0, 1e4
            for _ in range(50):
                m_ = (lo + hi) / 2
                lo, hi = (m_, hi) if q2s0(m_) < s_ else (lo, m_)
            return (lo + hi) / 2

        def level(W, q):
            """power mean over the window, or (peak windows) the loudest 200 ms inside it; sets the envelope window"""
            w_ = W[q]
            if not w_["peak"]:
                return pm(p[int(w_["a"] * sr):int(w_["b"] * sr)])
            a_, b_ = int(w_["a"] * sr), int(w_["b"] * sr)
            seg = p[max(a_, 0):b_]
            n_ = int(0.2 * sr); h_ = int(0.01 * sr)
            if len(seg) <= n_:
                c_ = (a_ + b_) / 2 / sr; v_ = pm(seg)
            else:
                cs = np.concatenate([[0.0], np.cumsum(seg)])
                st_ = np.arange(0, len(seg) - n_ + 1, h_)
                mv = (cs[st_ + n_] - cs[st_]) / n_
                i_ = int(np.argmax(mv)); v_ = 10 * np.log10(mv[i_] + 1e-15); c_ = (max(a_, 0) + st_[i_] + n_ / 2) / sr
            w_["pqa"], w_["pqb"] = s2q(c_ - 0.1), s2q(c_ + 0.1)
            if q in W1 and W1[q]["peak"]:
                W1[q]["pqa"], W1[q]["pqb"] = w_["pqa"], w_["pqb"]
            return v_

        for j, k in enumerate(on):
            w = W0[k]
            if not w["acc"] or not w["ok"] or k not in W1:
                continue
            L = level(W0, k)
            nb = [q for q in on[max(0, j - 2):j] + on[j + 1:j + 3]
                  if not W0[q]["acc"] and abs(q - k) <= A.near and W0[q]["ok"] and abs(W0[q]["cc"] - w["cc"]) <= 6 and q in W1
                  and not (A.pickup_qn > 0 and W0[q]["pickup"])]
            hf = None
            if w["te"] - w["ts"] > 0.3:
                hf = band(x, sr, w["ts"], w["ts"] + 0.08) - band(x, sr, w["ts"] + 0.15, min(w["ts"] + 0.5, w["te"] - 0.02))
            r = dict(track=t0["name"], q=k, art0=w["art"], art1=W1[k]["art"], hf=None if hf is None else round(hf, 1), nb=nb,
                     keep=(A.keep_long_qn > 0 and (W1[k]["slen"] >= A.keep_long_qn - 1e-6 or W1[k]["arrival"]))
                     or W1[k]["legearly"])   # mvt1 c15 (A #5): no negative step on an early legato target
            if nb:
                Ln = [level(W0, q) for q in nb]
                over = L - pm([10 ** (v / 10) for v in Ln])
                e0 = env_mean(t0, w) - np.mean([env_mean(t0, W0[q]) for q in nb])
                e1 = env_mean(t1, W1[k]) - np.mean([env_mean(t1, W1[q]) for q in nb])
                valid = w["art"] == W1[k]["art"] and all(W0[q]["art"] == W1[q]["art"] for q in nb)
                r.update(over=round(over, 2), resid=round(over - e0, 2), env1=round(e1, 2),
                         pred=round(over - e0 + e1, 2), valid=valid)
            # mvt1 c13 (critic A #2): the pickup term
            pk_ = on[j - 1] if j > 0 else None
            if A.pickup_over > 0 and pk_ is not None and not W0[pk_]["acc"] and pk_ in W1 \
                    and k - pk_ <= A.pickup_max_qn + 0.01 and W0[pk_]["qend"] >= w["qn"] - 0.1:
                pw0, pw1 = W0[pk_], W1[pk_]
                pa, pb = pw0["ts"] + 0.03, w["ts"]
                if pb - pa >= 0.05:
                    Lp = pm(p[int(pa * sr):int(pb * sr)])

                    def penv(t_, pw_, w_):
                        qs_ = np.linspace(pw_["qn"] + 0.03 * lane(t_["tempo_"], pw_["qn"]) / 60, max(w_["qn"], pw_["qn"] + 0.01), 12)
                        return 10 * np.log10(np.mean(10 ** (np.array([lane(t_["vol_db"], q_) for q_ in qs_]) / 10)))
                    t0["tempo_"] = t1["tempo_"] = P0["tempo"]
                    over_p = L - Lp
                    e0p = env_mean(t0, w) - penv(t0, pw0, w)
                    e1p = env_mean(t1, W1[k]) - penv(t1, pw1, W1[k])
                    r.update(pick=pk_, over_pick=round(over_p, 2), ppred=round(over_p - e0p + e1p, 2),
                             pvalid=w["art"] == W1[k]["art"] and pw0["art"] == pw1["art"])
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


def cap_total(sw, tr):
    """mvt1 c17 (critic A #2): swell + step at most A.max_total (the step goes first)"""
    ex = sw + tr - A.max_total
    if ex > 0:
        u = min(ex, max(tr, 0.0)); tr -= u; ex -= u
        sw = max(0.0, sw - ex)
    return sw, tr


# mvt1 c17: existing fits over the cap are brought under it before the iteration
for tn_, fd_ in fits.items():
    if not any(t_["name"] == tn_ and t_["family"] == A.family for t_ in json.load(open(A.rendered_parts))["tracks"]):
        continue
    for q_, v_ in list(fd_.items()):
        if (tn_, round(float(q_), 3)) in SKIP:
            continue
        sw_, tr_ = (v_ if isinstance(v_, list) else [v_, 0.0])
        sw2, tr2 = cap_total(sw_, tr_)
        if (sw2, tr2) != (sw_, tr_):
            fd_[q_] = [round(sw2, 2), round(tr2, 2)] if abs(tr2) > 0.05 else round(sw2, 2)

for it in range(A.iters):
    P1 = build(fits)
    rows = plan(P0, P1)
    moved = 0
    for r in rows:
        if (r["track"], round(r["q"], 3)) in SKIP:
            continue
        has_pk = A.pickup_over > 0 and "ppred" in r and r["pvalid"]
        if ("pred" not in r or not r["valid"]) and not has_pk:
            continue
        cur = fits.get(r["track"], {}).get(f"{r['q']:g}")
        need_pk = (A.pickup_over - r["ppred"]) if has_pk else -99.0
        if need_pk > 0.25:   # mvt1 c13: under its pickup; raise to the pickup target (the neighbour target may give more)
            dl0 = need_pk if not ("pred" in r and r["valid"]) else max(min(need_pk, A.pickup_cap_over - r["pred"]),
                                                                        A.target - r["pred"])
            if dl0 <= 0.25 and cur is not None:
                continue
            sw, tr = (cur if isinstance(cur, list) else [cur, 0.0]) if cur is not None else [default_swell(r["track"]), 0.0]
            if tr < 0:
                u = min(dl0, -tr); tr += u; dl0 -= u
            sw_new = sw + dl0 / 0.85
            if sw_new > A.max_swell:
                tr = min(A.max_trim, tr + (sw_new - A.max_swell) * 0.85); sw_new = A.max_swell
            sw_new, tr = cap_total(sw_new, tr)
            fits.setdefault(r["track"], {})[f"{r['q']:g}"] = [round(float(sw_new), 2), round(float(tr), 2)] \
                if abs(tr) > 0.05 else round(float(sw_new), 2)
            moved += 1
            continue
        if "pred" not in r or not r["valid"]:
            continue
        if r.get("keep") and isinstance(cur, list) and cur[1] < 0:   # c08: drop an old negative trim, refit next pass
            fits[r["track"]][f"{r['q']:g}"] = cur[0]
            moved += 1
            continue
        inside = A.lo <= r["pred"] <= A.hi
        tgt_ = A.target
        if has_pk and r["pred"] > A.target:
            # mvt1 c13: lower toward the target only as far as the pickup target allows
            tgt_ = max(A.target, r["pred"] - max(0.0, r["ppred"] - A.pickup_over))
        if cur is None and inside:
            continue
        if cur is not None and abs(r["pred"] - tgt_) < 0.25:
            continue
        sw, tr = (cur if isinstance(cur, list) else [cur, 0.0]) if cur is not None else [default_swell(r["track"]), 0.0]
        dlt = tgt_ - r["pred"]
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
        sw_new, tr = cap_total(sw_new, tr)
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
          f"{'' if 'ppred' not in r else '  pick ' + format(r['over_pick'], '+.1f') + ' -> ' + format(r['ppred'], '+.1f')}"
          f"{'' if r.get('valid', True) else '  (articulation changed: not predicted)'}")
pv = [r["pred"] for r in rows if "pred" in r and r["valid"]]
pp_ = [r["ppred"] for r in rows if "ppred" in r and r["pvalid"]]
if pp_:
    print(f"pickup: {sum(v >= A.pickup_over - 0.5 for v in pp_)}/{len(pp_)} predicted >= {A.pickup_over - 0.5:+.1f} dB over "
          f"their pickup, median {np.median(pp_):+.2f}, min {min(pp_):+.1f}; under 0: "
          f"{[(r['track'], r['q'], r['ppred']) for r in rows if 'ppred' in r and r['pvalid'] and r['ppred'] < 0]}")
print(f"predicted: {sum(A.lo <= v <= A.hi for v in pv)}/{len(pv)} in [{A.lo}, {A.hi}], median {np.median(pv):+.2f}, "
      f"min {min(pv):+.1f}, max {max(pv):+.1f}; hf > 3 dB: {sum(1 for r in rows if r['hf'] is not None and r['hf'] > 3)}")
if A.write:
    out = {"_doc": orig.get("_doc", "Per-accent fitted swells {track: {score qn: swell dB or [swell dB, step trim dB]}} "
                                     "written by tools/fit_accents.py (score_to_parts.py ACCENT_FITS).")}
    out.update({k: dict(sorted(v.items(), key=lambda kv: float(kv[0]))) for k, v in sorted(fits.items())})
    json.dump(out, open(fits_path, "w"), indent=1)
    print("wrote", fits_path)
