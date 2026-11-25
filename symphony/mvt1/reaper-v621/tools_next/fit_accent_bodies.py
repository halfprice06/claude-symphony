"""mvt1 c18 (critic A #1): fit body cuts on long accented notes so that the accent's weight is at its start.

Usage: fit_accent_bodies.py PREV RENDERED_PARTS [--family string] [--front-min 2.0] [--max-cut 4.0] [--min-qn 1.0]
                            [--min-s 0.75] [--skip Track:q ...] [--write]
  PREV            cycle number of the render to measure (cycles/cNN/render stems)
  RENDERED_PARTS  the parts.json that render was made from (its vol_db is what the stems carry)

Per accented onset on a track of the family (written 1 qn or longer, at least --min-s seconds long (to its written end or the next score onset);
not on or inside a printed crescendo or at its arrival, not on an sf/sfz/fp):
  front = stem power mean over score onset .. + 0.15 s
  body  = stem power mean over + 0.45 .. min(+ 0.75, the note's end - 0.05) s
  fb    = front - body, with the rendered volume envelope's own front - body taken out (resid) and the current build's
          put in (pred; the build's existing body cut included)
  cut   = clip(pred without any cut - front_min, -max_cut, 0) dB
build/accent_bodies.json ({track: {score qn: dB}}, read by score_to_parts.py ACCENT_BODIES; the cut ramps in over
ACCENT_BODY_S = 0.25 .. 0.45 s and holds to the next moved onset) is written only with --write. Level only, so
tools/stem_fix.py can apply a refit to a render.
"""
import json, os, sys, bisect, collections, subprocess, argparse
import numpy as np, soundfile as sf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = f"{ROOT}/build"
ap = argparse.ArgumentParser()
ap.add_argument("prev", type=int)
ap.add_argument("rendered_parts")
ap.add_argument("--family", default="string")
ap.add_argument("--front-min", type=float, default=2.0)
ap.add_argument("--max-cut", type=float, default=4.0)
ap.add_argument("--min-qn", type=float, default=1.0)
ap.add_argument("--min-s", type=float, default=0.75)
# mvt1 c23 (critic A #1): notes shorter than this many seconds use the short body window (0 = off)
ap.add_argument("--short-s", type=float, default=0.8)
ap.add_argument("--skip", action="append", default=[])
ap.add_argument("--scratch", default=os.environ.get("TMPDIR", "/tmp"))
ap.add_argument("--write", action="store_true")
A = ap.parse_args()
SKIP = {(x.rsplit(":", 1)[0], round(float(x.rsplit(":", 1)[1]), 3)) for x in A.skip}
PATH = f"{BUILD}/accent_bodies.json"

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

    def s2q(s):
        i = max(0, bisect.bisect_right(ts, s) - 1)
        return tq[i] + (s - ts[i]) * tempo[i][1] / 60
    return q2s, s2q


def env_db(t, qa, qb):
    """power mean of the vol_db lane (linear between points, as REAPER plays it) over [qa, qb]"""
    pts = t["vol_db"]
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    qs = np.linspace(qa, qb, 24)
    v = np.interp(qs, xs, ys)
    return 10 * np.log10(np.mean(10 ** (v / 10)))


def lvl(p, sr, a, b):
    return 10 * np.log10(np.mean(p[max(0, int(a * sr)):max(int(a * sr) + 1, int(b * sr))]) + 1e-15)


def rows_for(P0, P1):
    q2s, s2q = q2s_of(P0)
    T1 = {t["name"]: t for t in P1["tracks"]}
    d = f"{ROOT}/cycles/c{A.prev:02d}/render"
    out = []
    for t0 in P0["tracks"]:
        if t0["family"] != A.family or t0["name"] not in T1:
            continue
        f = [x for x in os.listdir(d) if x[:2] != "00" and x.endswith(".wav") and x[3:-4] == t0["name"]]
        if not f:
            continue
        x, sr = sf.read(f"{d}/{f[0]}", dtype="float32")
        p = (x.astype(np.float64) ** 2).mean(1)
        st = t0["staves"]
        acc = sorted({round(q, 3) for s in st for q, k, v in EV[s] if k == "script" and v and v[0] == "accent"})
        sfq = {round(q, 3) for s in st for q, k, v in EV[s] if k == "dynamic" and v and v[0] in ("sf", "sfz", "fp")}
        ons = sorted({round(n["sq"], 3) for n in t0["notes"]})
        hps = t0.get("hairpins", [])
        for q in acc:
            if q not in ons or q in sfq or (t0["name"], q) in SKIP:
                continue
            # written length, or the played length when a tie merged notes (mockup-events.tsv lists tied notes apart)
            wlen = max([float(v[1]) for s in st for q_, k_, v in EV[s] if k_ == "note" and abs(q_ - q) < 1e-3]
                       + [n["qn"] + n["dur"] - n["sq"] for n in t0["notes"] if abs(n["sq"] - q) < 1e-3] + [0.0])
            nx = [o for o in ons if o > q + 0.01]
            if wlen < A.min_qn - 1e-6 or not nx:
                continue
            s0, e = q2s(q), min(q2s(nx[0]), q2s(q + wlen))   # the note's sounding end (score time)
            if e - s0 < A.min_s:
                continue
            if any(h[2] == "cresc" and (h[0] - 0.01 <= q <= h[1] + 0.01 or abs(h[1] - q) < 0.3) for h in hps):
                continue
            fa, fb_, ba, bb = s0, s0 + 0.15, s0 + 0.45, min(s0 + 0.75, e - 0.05)
            if A.short_s > 0 and e - s0 < A.short_s:
                # mvt1 c23 (critic A #1): a short accented note (a 126 bpm quarter is 0.476 s) has its body at
                # +0.28 s .. its played end - 0.03 s (score_to_parts ACCENT_BODY_S_SHORT ramps the cut in over 0.18-0.28 s)
                pe = q2s(max(n["qn"] + n["dur"] for n in t0["notes"] if abs(n["sq"] - q) < 1e-3))
                ba, bb = s0 + 0.28, min(e, pe) - 0.03
                if bb - ba < 0.08:
                    continue
            fb = lvl(p, sr, fa, fb_) - lvl(p, sr, ba, bb)
            e0 = env_db(t0, s2q(fa), s2q(fb_)) - env_db(t0, s2q(ba), s2q(bb))
            e1 = env_db(T1[t0["name"]], s2q(fa), s2q(fb_)) - env_db(T1[t0["name"]], s2q(ba), s2q(bb))
            out.append(dict(track=t0["name"], q=q, fb=fb, resid=fb - e0, pred=fb - e0 + e1, wlen=wlen))
    return out


def build(bodies):
    keep = open(PATH).read() if os.path.exists(PATH) else None
    sp = os.path.join(A.scratch, "fit_accent_bodies_parts.json")
    try:
        json.dump(bodies, open(PATH, "w"), indent=1)
        r = subprocess.run([sys.executable, f"{ROOT}/tools/score_to_parts.py", ".",
                            os.path.expanduser("~/.rpr-bridge/libs/ew_ho/ks_maps.json"), sp], cwd=BUILD,
                           capture_output=True, text=True)
        if r.returncode:
            sys.exit(r.stderr[-2000:])
    finally:
        if keep is None:
            os.remove(PATH)
        else:
            open(PATH, "w").write(keep)
    return json.load(open(sp))


P0 = json.load(open(A.rendered_parts))
orig = json.load(open(PATH)) if os.path.exists(PATH) else {}
cur = {k: {kk: vv for kk, vv in v.items()} for k, v in orig.items() if not k.startswith("_")}
# predictions with no cut at all
nocut = {k: {} for k in cur}
P1 = build({**{k: v for k, v in orig.items() if k.startswith("_")}, **nocut})
rows = rows_for(P0, P1)
new = {k: dict(v) for k, v in cur.items() if not any(t["name"] == k and t["family"] == A.family for t in P0["tracks"])}
for r in rows:
    c = float(np.clip(r["pred"] - A.front_min, -A.max_cut, 0.0))
    r["cut"] = round(c, 1)
    if c < -0.25:
        new.setdefault(r["track"], {})[f"{r['q']:g}"] = r["cut"]
for (tn, q) in SKIP:   # skipped accents keep what they had
    v = cur.get(tn, {}).get(f"{q:g}")
    if v is not None:
        new.setdefault(tn, {})[f"{q:g}"] = v
doc = orig.get("_doc", "mvt1 c18: body cuts on long accented notes {track: {score qn: dB}} written by "
                       "tools/fit_accent_bodies.py (score_to_parts.py ACCENT_BODIES)")
P2 = build({"_doc": doc, **new})
after = {(r["track"], r["q"]): r["pred"] for r in rows_for(P0, P2)}
print("track          q        wlen  front-body  resid  pred(no cut)  cut   pred(after)")
for r in sorted(rows, key=lambda r: (r["track"], r["q"])):
    print(f"{r['track'][:14]:14s} {r['q']:7.2f} {r['wlen']:5.2f}  {r['fb']:+6.1f}  {r['resid']:+6.1f}  {r['pred']:+6.1f}"
          f"   {r['cut']:+5.1f}  {after.get((r['track'], r['q']), float('nan')):+6.1f}")
pv = [after[(r["track"], r["q"])] for r in rows if (r["track"], r["q"]) in after]
if pv:
    print(f"{len(pv)} accents: front-body median {np.median([r['pred'] for r in rows]):+.2f} -> {np.median(pv):+.2f}, "
          f"under 0: {sum(r['pred'] < 0 for r in rows)} -> {sum(v < 0 for v in pv)}; "
          f"cut on {sum(1 for r in rows if r['cut'] < -0.25)}")
if A.write:
    json.dump({"_doc": doc, **{k: dict(sorted(v.items(), key=lambda kv: float(kv[0]))) for k, v in sorted(new.items()) if v}},
              open(PATH, "w"), indent=1)
    print("wrote", PATH)
