"""mvt1 c47 (critic B #1, critic A #1, coordinator): per-note check of render-to-render state changes on unchanged data.

Usage: state_check.py OLD_RENDER OLD_BUILD NEW_RENDER NEW_BUILD [--tracks "Trumpet 1" ...] [--db 3.0] [--ms 30]
                      [--no-pcx] [--no-eq] [--old-src build_reaper.py] [--out FILE] [--json FILE]
  OLD_RENDER / NEW_RENDER  render folders (stems NN_<track>.wav; the delivered set or render_first/)
  OLD_BUILD / NEW_BUILD    folders with the parts.json and mix.json each render was made from (cycles/cNN/rendered_build,
                           or cycles/cNN/before for the data of the cycle before)
  --db / --ms              flag a note whose level moved more than this many dB (after the envelope change is removed),
                           or whose perceived attack (pcX) moved more than this many ms
  --no-pcx                 level only (faster)
  --no-eq                  keep the EQ change in the level (c50, from mvt1 c52: by default the change predicted from each
                           build's family EQ, "eq" and side-only "side_shelf" bands, applied to the old note's mid / side
                           spectrum, is removed with the envelope change; column "eq" in the flagged lines). Track width
                           changes are not modelled.
  --old-src                the build_reaper.py OLD_BUILD was written with, when vol_points() changed since

Why: Opus instances can render identical data differently. The Solo Trumpet KS Master's Leg Slur MAX targets rendered
4-15 dB louder and about 65 ms earlier than the render before in c42, c43 and c46 (three of five renders), with the same
notes, keyswitches, CC lanes and envelope; the attack probe looks at spreads and did not catch it. This compares every
note whose data did not change, and the note before it, between two renders.

A note counts as unchanged when a note of the old build has the same score onset and pitch with the same moved onset,
length and velocity, the same keyswitch row, the same CC1 / CC11 values on a 0.05 qn grid from 1 qn before the note to
its end (at most 1 qn), and the note sounding into it (or ending within 0.5 qn before it) is unchanged in the same way.
Level: stereo power over [moved onset, + min(length, 0.6 s)], minus the mean new-minus-old envelope change over that
window (build_reaper's vol_points on each build). Notes whose envelope change varies by more than 1 dB inside the window
are skipped. pcX: tools/pcx.py attack_pcx (the previous pitch excluded for a monophonic note).
Output: one line per track (notes compared, flagged), then every flagged note, then "RUN" lines: 3 or more notes within
4 qn of each other whose level moved over --db (a state change, e.g. one legato phrase), and "timing run" lines (4 or
more notes flagged on pcX only; string pcX varies by about 50 ms robust SD between renders, so these are informational).
Tested on c45 -> c46: the 16 Trumpet 1 notes in two runs and Horn 3 164, as critics A and B found by hand.

mvt2 c49 (critic A #1): "take swap" lines. A row with two alternating takes (--swap-arts, default Detache) can change
its take order between renders on unchanged data (Violas bars 48-51, c47 -> c48: the two Detache takes peak about
270 ms apart, so fitted entry leads landed on the wrong take). For the compared notes of such a row, chained while
they are within 4 qn of each other, a line is printed when two notes of one pitch moved by more than --ms in opposite
directions. Unlike a timing run this is not informational: swap or re-fit the leads in the same cycle, or reset the
round robin before the passage (RR_RESET_AT in tools/score_to_parts.py).
"""
import bisect, glob, json, os, sys
import numpy as np
import soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pcx   # noqa: E402
import eqresp   # noqa: E402  (c50, from mvt1 c52)

args = sys.argv[1:]


def opt(name, default=None, cast=str):
    if name in args:
        return cast(args[args.index(name) + 1])
    return default


OLD_R, OLD_B, NEW_R, NEW_B = args[:4]
DB = opt("--db", 3.0, float)
MS = opt("--ms", 30.0, float)
NO_PCX = "--no-pcx" in args
NO_EQ = "--no-eq" in args   # c50 (mvt1 c52, critic B #5): do not remove the EQ change
OUT = opt("--out")
JSON_OUT = opt("--json")
SWAP_ARTS = tuple(x for x in opt("--swap-arts", "Detache").split(",") if x)
TRACKS = []
if "--tracks" in args:
    i = args.index("--tracks") + 1
    while i < len(args) and not args[i].startswith("--"):
        TRACKS.append(args[i])
        i += 1

SRC = open(os.path.join(HERE, "build_reaper.py")).read()
SRC = SRC[:SRC.index("ENV_LUA = ")]
OLD_SRC = SRC
if opt("--old-src"):
    OLD_SRC = open(opt("--old-src")).read()
    OLD_SRC = OLD_SRC[:OLD_SRC.index("ENV_LUA = ")]


def load(build_dir, src):
    ns = {"__name__": "build_reaper_partial"}
    argv = sys.argv
    sys.argv = ["build_reaper.py", os.path.join(build_dir, "parts.json"), "/private/tmp/claude-501/mockup-loop/mvt2-statecheck-jobs"]
    try:
        exec(compile(src, "build_reaper.py", "exec"), ns)
    finally:
        sys.argv = argv
    return ns


A, B = load(OLD_B, OLD_SRC), load(NEW_B, SRC)
PRE = B["PRE"]
TA = {t["name"]: t for t in A["d"]["tracks"]}
TB = {t["name"]: t for t in B["d"]["tracks"]}
tm_a, tm_b = pcx.TM(A["d"]["tempo"]), pcx.TM(B["d"]["tempo"])
SR = pcx.SR


def stem(render_dir, name):
    c = sorted(glob.glob(os.path.join(render_dir, f"[0-9][0-9]_{glob.escape(name)}.wav")))
    return c[0] if c else None


def art_at(tr, q):
    a = tr.get("first_art")
    for k in sorted(tr.get("ks", []), key=lambda k: k["qn"]):
        if k["qn"] <= q + 1e-6:
            a = k["art"]
        else:
            break
    return a


_LANES = {}


def lane_at(pts, q):
    """the step value of a CC lane [[qn, value], ...] at qn q (None before its first point)"""
    k = id(pts)
    if k not in _LANES:
        sp = sorted((float(a), b) for a, b in pts)
        _LANES[k] = ([a for a, _ in sp], [b for _, b in sp], pts)
    qs, vs, _ = _LANES[k]
    i = bisect.bisect_right(qs, q + 1e-6) - 1
    return vs[i] if i >= 0 else None


def prev_note(ns, n):
    c = [m for m in ns if m is not n and m["qn"] < n["qn"] - 1e-4 and m["qn"] + m["dur"] > n["qn"] - 0.5]
    return max(c, key=lambda m: m["qn"]) if c else None


def match(ns_old, n):
    return next((m for m in ns_old if abs(m["sq"] - n["sq"]) < 1e-4 and m["pitch"] == n["pitch"]), None)


def same_note(ta, tb, mo, n):
    if mo is None or abs(mo["qn"] - n["qn"]) > 1e-4 or abs(mo["dur"] - n["dur"]) > 1e-4 or mo.get("vel") != n.get("vel"):
        return False
    if art_at(ta, mo["qn"]) != art_at(tb, n["qn"]):
        return False
    q0, q1 = n["qn"] - 1.0, n["qn"] + min(n["dur"], 1.0)
    for ln in ("cc1", "cc11"):
        for q in np.arange(q0, q1 + 1e-9, 0.05):
            if lane_at(ta.get(ln, []), q) != lane_at(tb.get(ln, []), q):
                return False
    return True


def env_curve(ns_, tr):
    pts = ns_["vol_points"](tr)
    s = np.array([ns_["q2s"](p["qn"] - PRE) for p in pts])
    v = np.array([p["db"] for p in pts])
    return s, v


def level_db(x, t0, t1):
    i0, i1 = max(0, int(t0 * SR)), min(len(x), int(t1 * SR))
    if i1 - i0 < 64:
        return None
    return float(10 * np.log10(np.mean(x[i0:i1] ** 2) * 2 + 1e-20))


NFFT = 8192
FQ = np.fft.rfftfreq(NFFT, 1 / SR)


def eq_ratio(name):
    """c50 (mvt1 c52, critic B #5): (|H_new / H_old|^2 on both channels, the same for the side-only bands), or None when
    the track's EQ did not change between the two builds"""
    try:
        bo, so = eqresp.track_bands(A["MIX"], A["mix_for"](name))
        bn, sn = eqresp.track_bands(B["MIX"], B["mix_for"](name))
    except KeyError:
        return None
    if bo == bn and so == sn:
        return None
    with np.errstate(divide="ignore", invalid="ignore"):   # a high-pass is 0 at 0 Hz in both builds
        rb_ = np.nan_to_num(eqresp.resp2(bn, FQ) / eqresp.resp2(bo, FQ), nan=1.0, posinf=1.0)
        rs_ = np.nan_to_num(eqresp.resp2(sn, FQ) / eqresp.resp2(so, FQ), nan=1.0, posinf=1.0)
    return rb_, rs_


def eq_pred_db(x, t0, t1, ratio):
    """the level change (dB) the EQ change gives the old stem's segment [t0, t1] (mid / side power spectra)"""
    i0, i1 = max(0, int(t0 * SR)), min(len(x), int(t1 * SR))
    seg = x[i0:i1].astype(np.float64)
    if len(seg) < 64:
        return 0.0
    w = np.hanning(NFFT)
    pm = np.zeros(len(FQ)); ps = np.zeros(len(FQ))
    for s0 in range(0, max(1, len(seg) - NFFT + 1), 2048):
        fr = seg[s0:s0 + NFFT]
        if len(fr) < NFFT:
            fr = np.pad(fr, ((0, NFFT - len(fr)), (0, 0)))
        pm += np.abs(np.fft.rfft((fr[:, 0] + fr[:, 1]) * 0.5 * w)) ** 2
        ps += np.abs(np.fft.rfft((fr[:, 0] - fr[:, 1]) * 0.5 * w)) ** 2
    hb, hs = ratio
    tot = float(np.sum(pm + ps))
    if tot <= 0:
        return 0.0
    return float(10 * np.log10(np.sum(pm * hb + ps * hb * hs) / tot))


rows, lines = [], []
names = TRACKS or [n for n in TB if n in TA]
for name in names:
    fa, fb = stem(OLD_R, name), stem(NEW_R, name)
    if not fa or not fb or name not in TA or name not in TB:
        continue
    ta, tb = TA[name], TB[name]
    if ta.get("family") in ("perc", "harp", "harm") or not tb["notes"]:
        continue
    xa, _ = sf.read(fa, dtype="float32", always_2d=True)
    xb, _ = sf.read(fb, dtype="float32", always_2d=True)
    sa, va = env_curve(A, ta)
    sb, vb = env_curve(B, tb)
    eqr = None if NO_EQ else eq_ratio(name)
    ns_a = sorted(ta["notes"], key=lambda m: m["qn"])
    ns_b = sorted(tb["notes"], key=lambda m: m["qn"])
    n_cmp, flagged = 0, []
    for n in ns_b:
        mo = match(ns_a, n)
        if not same_note(ta, tb, mo, n):
            continue
        pb = prev_note(ns_b, n)
        if pb is not None and not same_note(ta, tb, match(ns_a, pb), pb):
            continue
        tm, ts = tm_b.sec(n["qn"]), tm_b.sec(n["sq"])
        ln = min(tm_b.sec(n["qn"] + n["dur"]) - tm, 0.6)
        if ln < 0.05:
            continue
        tt = np.linspace(tm, tm + ln, 16)
        g = np.interp(tt, sb, vb) - np.interp(tt, sa, va)
        if g.max() - g.min() > 1.0:
            continue
        la, lb = level_db(xa, tm, tm + ln), level_db(xb, tm, tm + ln)
        if la is None or lb is None or la < -90 or lb < -90:
            continue
        de = eq_pred_db(xa, tm, tm + ln, eqr) if eqr is not None else 0.0
        dl = lb - la - float(g.mean()) - de
        dp = None
        if not NO_PCX:
            chord = any(m is not n and abs(m["qn"] - n["qn"]) < 0.02 for m in ns_b)
            pp = None if (chord or pb is None) else pb["pitch"]
            try:
                ra = pcx.attack_pcx(xa, tm, ts, ln, n["pitch"], pp) or {}
                rb = pcx.attack_pcx(xb, tm, ts, ln, n["pitch"], pp) or {}
            except ValueError:   # a window outside the stem (a note at the very start)
                ra = rb = {}
            if ra.get("pc") is not None and rb.get("pc") is not None:
                dp = (rb["pc"] - ra["pc"]) * 1000
        n_cmp += 1
        row = {"track": name, "sq": n["sq"], "pitch": n["pitch"], "art": art_at(tb, n["qn"]), "d_db": round(dl, 2),
               "eq_db": round(de, 2),
               "d_pcx_ms": None if dp is None else round(dp, 1)}
        rows.append(row)
        if abs(dl) > DB or (dp is not None and abs(dp) > MS):
            flagged.append(row)
    def runs_of(rows_):
        out_, cur_ = [], []
        for r in rows_:
            if cur_ and r["sq"] - cur_[-1]["sq"] > 4.0:
                if len(cur_) >= 3:
                    out_.append(cur_)
                cur_ = []
            cur_.append(r)
        if len(cur_) >= 3:
            out_.append(cur_)
        return out_
    # a "state" run: 3 or more notes within 4 qn of each other whose level moved over DB (the c42 / c43 / c46 Solo
    # Trumpet flips); timing-only runs are listed separately (string pcX varies by about 50 ms robust SD between
    # renders from round robins, so 3-note timing runs are common and are not states by themselves)
    runs = runs_of([r for r in flagged if abs(r["d_db"]) > DB])
    truns = [r_ for r_ in runs_of([r for r in flagged if abs(r["d_db"]) <= DB]) if len(r_) >= 4]
    lines.append(f"{name:18s} compared {n_cmp:4d}  flagged {len(flagged):3d}  state runs {len(runs)}  timing runs {len(truns)}")
    for r in flagged:
        lines.append(f"    {r['sq']:8.3f} p{r['pitch']:3d} {str(r['art'])[:22]:22s} level {r['d_db']:+6.2f} dB  eq {r['eq_db']:+5.2f}  "
                     f"pcX {'   n/a' if r['d_pcx_ms'] is None else format(r['d_pcx_ms'], '+6.0f')} ms")
    for tag, rr_ in (("RUN", runs), ("timing run", truns)):
        for run in rr_:
            dls = [r["d_db"] for r in run]
            dps = [r["d_pcx_ms"] for r in run if r["d_pcx_ms"] is not None]
            lines.append(f"  {tag} {name}: qn {run[0]['sq']:.2f}-{run[-1]['sq']:.2f}, {len(run)} notes, level median "
                         f"{np.median(dls):+.1f} dB, pcX median {np.median(dps) if dps else float('nan'):+.0f} ms")
    # c49: take swaps on two-take rows (see the header)
    sw = [r for r in rows if r["track"] == name and r["d_pcx_ms"] is not None and any(a_ in str(r["art"]) for a_ in SWAP_ARTS)]
    grp = []
    for r in sw + [None]:
        if r is not None and (not grp or r["sq"] - grp[-1]["sq"] <= 4.0):
            grp.append(r)
            continue
        for pch in sorted({g_["pitch"] for g_ in grp}):
            up = [g_ for g_ in grp if g_["pitch"] == pch and g_["d_pcx_ms"] > MS]
            dn = [g_ for g_ in grp if g_["pitch"] == pch and g_["d_pcx_ms"] < -MS]
            if up and dn:
                lines.append(f"  take swap {name}: qn {grp[0]['sq']:.2f}-{grp[-1]['sq']:.2f}, pitch {pch}: "
                             + ", ".join(f"{g_['sq']:.2f} {g_['d_pcx_ms']:+.0f} ms" for g_ in sorted(up + dn, key=lambda g_: g_["sq"]))
                             + " (two takes changed order: swap or re-fit the leads, or reset the round robin before the run)")
        grp = [r] if r is not None else []
text = "\n".join([f"state_check: {OLD_R} ({OLD_B}) -> {NEW_R} ({NEW_B}); flag |level| > {DB} dB or |pcX| > {MS} ms "
                  "on notes whose data did not change"] + lines)
print(text)
if OUT:
    open(OUT, "w").write(text + "\n")
if JSON_OUT:
    json.dump(rows, open(JSON_OUT, "w"), indent=0)
