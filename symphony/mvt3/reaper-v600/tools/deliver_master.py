"""Delivery master for headphone listening: slow look-ahead gain ride on the quiet passages, constant gain to
-16 LUFS (mvt3 c20), true-peak limiter at -1.0 dBTP, mp3. The climax is left alone.

Usage: python deliver_master.py <master.wav> <out.mp3> [<parts.json> [--fit-flat A B]]
  mvt1 c40 (critic C #3): with parts.json, its "ride_trims" (score_to_parts.py RIDE_TRIMS: rows of (score qn, dB)) are
  added to the ride's gain, converted to file seconds on its tempo map (the render is cut at score qn 0).
  --fit-flat A B prints, without writing the mp3, a RIDE_TRIMS row for score qn A..B that holds the ride at that
  span's own steady lift ((knee - its mean short-term loudness) x (1 - 1/RATIO)) instead of the slow interpolation
  between its neighbours (trims every 2 qn, ramped in and out over 0.05 qn); the listed trims are left out of the fit.
Method and targets: loop/DYNAMICS-RESEARCH.md (LRA 14-16 LU, BBC classical guideline 15 LU; no inversions of
crescendos/diminuendos; limiter at most about 3 dB). Prints the measurements of the result.
"""
import os, re, shutil, subprocess, sys, tempfile
import numpy as np
import soundfile as sf

SRC, OUT = sys.argv[1], sys.argv[2]
PARTS = sys.argv[3] if len(sys.argv) > 3 and not sys.argv[3].startswith("--") else None
FIT = [float(v) for v in sys.argv[sys.argv.index("--fit-flat") + 1:sys.argv.index("--fit-flat") + 3]] \
    if "--fit-flat" in sys.argv else None
# c10: TARGET_I -19.0 -> -19.5 (critics B #3 / C #2 fallback, inside the research range -18..-20): the limiter did 4.5 dB
# mvt1 c02 (critic C #5): RATIO 2.0 -> 2.5 (simulated on c01: span 20.5 -> 19.7 dB, LRA 15.6 -> 14.9 LU, no inversions;
# 3.0 gave 6 inversions)
TARGET_I, KNEE_BELOW, RATIO, CAP_DB, SMOOTH_S = -19.5, 6.0, 2.5, 10.0, 3.0
# mvt1 c08 (critic C #3): a slow top ride over the loudest frames (above the 95th percentile + TOP_ABOVE, TOP_RATIO:1,
# same smoothing): the delivered p75->max was 10.6 dB against 4.8-7.6 in five recordings and the p10 span 20.0 dB
# (target 16-19); it acts on the top 5-8% of frames only. TOP_RATIO 1.0 = off. 1.6 rather than the critic's 2.0: on a
# simulation of the c08 changes 2.0 left bar 160 only 0.35 LU over bar 122 (1.6: 0.49, span 18.6 dB, limiter 1.3 dB)
# mvt1 c30 (critic C #2): 1.6 -> 2.5 with the coda's _coda26 -2 -> -3.5 dB (simulated on c29: limiter 2.1 -> 1.3 dB,
# pp bars 0.8 -> 2.2 dB under p, max-p75 9.4 -> 8.6 dB, bar 160 still 1.0 dB over bar 122 on S max)
TOP_ABOVE, TOP_RATIO = -3.0, 2.5
# mvt3 c20 (Dan 2026-11-17: "i have to turn the volume on my airpods to almost max ... overall the tracks are too soft";
# shared delivery target for all movements, mockup-kit/README.md; ported from symphony/mvt1/reaper-v621/tools/
# deliver_master.py): delivered -16 LUFS, -1.0 dBTP, LRA 12-13 LU, p10 short-term -25 or higher. Top ride from 10 dB
# under the 95th percentile at 3:1; the quiet-lift ratio stays this score's mix.json "deliver" 2.0 (critic B c20:
# 3.0 gives LRA 11.3 on the c19 master, 2.0 gives -16.4 LUFS, LRA 12.4, p10 -24.8)
TOP_ABOVE, TOP_RATIO = -10.0, 3.0
# mvt3 c21 (coordinator, Movement II c57: 3:1 gave LRA 10.6 there): top ride 3:1 -> 2:1. Simulated on the c20 master
# with the c21 rides, ratio 1.8 and the loudness loop: LRA 11.5 -> 12.4, p10 -22.3 -> -22.9, limiter 5.8 -> 6.0 dB on the
# final chord, 263 over the loudest ff bar 0.9 -> 1.7 dB (cycles/c21/logs/deliv_c20_top2.log)
TOP_RATIO = 2.0
TOP_RATIO = float(os.environ.get("DELIVER_TOP_RATIO", TOP_RATIO))   # mvt3 c21: A/B override
FAST_CAP_ABOVE = 4.0   # mvt1 c10 (critic C #1); None = off
# mvt1 c22 (critic C #3): a cap read from momentary loudness (400 ms, the max over +-0.5 s): no momentary peak is lifted
# above knee + MOM_CAP_ABOVE. The slow lift and FAST_CAP_ABOVE read short-term loudness (3 s), which a 0.3 s ff stab
# barely moves, so a stab between soft bars took their lift (bar 33 the 4th-loudest moment of the c21 mp3, bar 41 over
# the ff arrival at 117). None = off
MOM_CAP_ABOVE, MOM_CAP_SMOOTH_S = 6.0, 0.5
TAIL_DB, TAIL_S, FADE_S = -65.0, 1.0, 0.5
# mvt1 c36 (critic C #6): the quiet-passage lift's own smoothing (both passes), separate from the top ride's SMOOTH_S.
# None = SMOOTH_S. Environment overrides for A/B deliveries of one master: DELIVER_RATIO, DELIVER_KNEE_BELOW,
# DELIVER_LIFT_SMOOTH_S
# mvt1 c36 (critic C #6, simulated on the c35 master with the c36 level changes): RATIO 2.5 -> 3.0, KNEE_BELOW 6 -> 5,
# LIFT_SMOOTH_S 5.0: the 3 s lift passed phrase-length swells into the gain, so soft passages kept a median 77% of
# their 5 s moves (19 under 50%); now 82% (3 under 50%), p50-p10 6.1 -> 7.0 dB, max-p75 8.5 -> 7.3 dB, LRA 14.7 -> 14.8,
# span 19.0, limiter 1.1 -> 0.9 dB, 0 inversions, bar 160 over bar 122 unchanged (0.8 LU)
RATIO, KNEE_BELOW = 3.0, 5.0
LIFT_SMOOTH_S = 5.0
TARGET_I, KNEE_BELOW = -16.0, 7.0   # mvt3 c20, see TOP_ABOVE
TARGET_I = -14.0   # mvt3 c20, Dan 2026-11-17: "-14 goal please" (shared target -16 -> -14 LUFS)
TARGET_I = float(os.environ.get("DELIVER_TARGET_I", TARGET_I))
# mvt3 c07: mix.json (next to parts.json) "deliver": {"ratio": ...} sets the quiet-passage ride ratio for this score
# (the c07 phrase shapes widened the master LRA 20.5 -> 23.5 LU and the delivered LRA fell to 13.5 at 3.0)
if PARTS and os.path.exists(os.path.join(os.path.dirname(os.path.abspath(PARTS)), "mix.json")):
    import json as _jd
    RATIO = float((_jd.load(open(os.path.join(os.path.dirname(os.path.abspath(PARTS)), "mix.json"))).get("deliver") or {}).get("ratio", RATIO))
# mvt3 c13 (critic C #1): RISE_DELAY_S. After a tutti stop the short-term loudness falls and the ride's gain rises while
# the hall tail is still sounding, which lengthens the stop on the delivered file (c12: bar 2 reached -20 dB after 0.44 s
# on the master and 0.49-0.50 s on the mp3; 11.6 dB at 0.3 s against 13.1). With a delay the gain at time t is the lower
# of its value at t and at t - RISE_DELAY_S: gain rises wait that long, gain falls are not delayed. 0 = off (default);
# mix.json "deliver": {"rise_delay_s": ...} sets it for a score; environment override DELIVER_RISE_DELAY_S
RISE_DELAY_S = 0.0
if PARTS and os.path.exists(os.path.join(os.path.dirname(os.path.abspath(PARTS)), "mix.json")):
    RISE_DELAY_S = float((_jd.load(open(os.path.join(os.path.dirname(os.path.abspath(PARTS)), "mix.json"))).get("deliver") or {}).get("rise_delay_s", RISE_DELAY_S))
RISE_DELAY_S = float(os.environ.get("DELIVER_RISE_DELAY_S", RISE_DELAY_S))
RATIO = float(os.environ.get("DELIVER_RATIO", RATIO))
# mvt3 c24 (critic C c24 #2): mix.json "deliver": {"top_above": ...} sets where the top ride starts (dB re the 95th
# percentile of short-term loudness) for a score; environment override DELIVER_TOP_ABOVE. -10 started the 2:1 ride about
# 7 dB under the ff level and took 2.5-3.5 dB off every f-ff passage (f -> ff on the c23 mp3 1.4 dB against 5.0 on the
# master); -6 with the quiet-lift ratio 2.1: f -> ff 2.2 dB, LRA 12.0, limiter 5.8 dB (simulated on the c23 master)
if PARTS and os.path.exists(os.path.join(os.path.dirname(os.path.abspath(PARTS)), "mix.json")):
    TOP_ABOVE = float((_jd.load(open(os.path.join(os.path.dirname(os.path.abspath(PARTS)), "mix.json"))).get("deliver") or {}).get("top_above", TOP_ABOVE))
TOP_ABOVE = float(os.environ.get("DELIVER_TOP_ABOVE", TOP_ABOVE))
KNEE_BELOW = float(os.environ.get("DELIVER_KNEE_BELOW", KNEE_BELOW))
LIFT_SMOOTH_S = float(os.environ["DELIVER_LIFT_SMOOTH_S"]) if os.environ.get("DELIVER_LIFT_SMOOTH_S") else LIFT_SMOOTH_S
# mvt3 c20: limit 0.841 -> 0.87 for the -1.0 dBTP ceiling (critic B c20: 0.891 leaves TP -0.9 after the mp3 encode;
# 0.87 measured -1.0)
CEIL, TP_MAX = 0.87, -1.0
LOUD_PASSES = int(os.environ.get("DELIVER_LOUD_PASSES", 3))   # mvt3 c21: see the loudness loop
LOUD_TOL = 0.1
LIMIT_FMT = "aresample=192000,alimiter=limit={:.4f}:attack=5:release=80:level=0:asc=1,aresample=48000"


def short_term(path):
    """EBU short-term loudness (3 s window) at 10 Hz."""
    out = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af",
                          "ebur128=metadata=1,ametadata=print:key=lavfi.r128.S:file=-", "-f", "null", "-"],
                         capture_output=True, text=True).stdout
    return np.array([float(v) for v in re.findall(r"lavfi\.r128\.S=(-?[\d.]+|-inf|nan)", out.replace("-inf", "-70"))])


def momentary(path):
    """EBU momentary loudness (400 ms window) at 10 Hz."""
    out = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af",
                          "ebur128=metadata=1,ametadata=print:key=lavfi.r128.M:file=-", "-f", "null", "-"],
                         capture_output=True, text=True).stdout
    return np.array([float(v) for v in re.findall(r"lavfi\.r128\.M=(-?[\d.]+|-inf|nan)", out.replace("-inf", "-70"))])


def integrated(path):
    err = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    g = lambda k: float(re.findall(k + r":\s+(-?[\d.]+)", err)[-1])
    return {"I": g("I"), "LRA": g("LRA"), "TP": g("Peak")}


def smooth(v, sec, rate=10):  # zero-phase Gaussian
    n = max(1, int(sec * rate)); k = np.exp(-0.5 * (np.arange(-3 * n, 3 * n + 1) / n) ** 2); k /= k.sum()
    return np.convolve(np.pad(v, (3 * n, 3 * n), mode="edge"), k, "valid")


def biquad_h(b, f, sr):
    """complex response at f (Hz) of one RBJ biquad for a ReaEQ-style band {type hp|lp|bell|hshelf|lshelf, hz, db, bw}"""
    w0 = 2 * np.pi * float(b["hz"]) / sr
    cw, sw = np.cos(w0), np.sin(w0)
    al = sw * np.sinh(np.log(2) / 2 * float(b.get("bw", 2.0)) * w0 / sw)
    A = 10 ** (float(b.get("db", 0.0)) / 40)
    t = b["type"]
    if t == "hp":
        num, den = [(1 + cw) / 2, -(1 + cw), (1 + cw) / 2], [1 + al, -2 * cw, 1 - al]
    elif t == "lp":
        num, den = [(1 - cw) / 2, 1 - cw, (1 - cw) / 2], [1 + al, -2 * cw, 1 - al]
    elif t == "bell":
        num, den = [1 + al * A, -2 * cw, 1 - al * A], [1 + al / A, -2 * cw, 1 - al / A]
    elif t == "hshelf":
        sa = 2 * np.sqrt(A) * al
        num = [A * ((A + 1) + (A - 1) * cw + sa), -2 * A * ((A - 1) + (A + 1) * cw), A * ((A + 1) + (A - 1) * cw - sa)]
        den = [(A + 1) - (A - 1) * cw + sa, 2 * ((A - 1) - (A + 1) * cw), (A + 1) - (A - 1) * cw - sa]
    elif t == "lshelf":
        sa = 2 * np.sqrt(A) * al
        num = [A * ((A + 1) - (A - 1) * cw + sa), 2 * A * ((A - 1) - (A + 1) * cw), A * ((A + 1) - (A - 1) * cw - sa)]
        den = [(A + 1) + (A - 1) * cw + sa, -2 * ((A - 1) + (A + 1) * cw), (A + 1) + (A - 1) * cw - sa]
    else:
        raise SystemExit(f"master_eq: unknown band type {t!r}")
    z = np.exp(-1j * 2 * np.pi * f / sr)
    return (num[0] + num[1] * z + num[2] * z * z) / (den[0] + den[1] * z + den[2] * z * z)


# mvt3 c06 (EW template, plan item 3): mix.json "master_eq" (next to parts.json; the template's master ReaEQ) is applied
# here, before the ride, so 00_Master.wav stays the plain sum of the stems (dry + return stems). The biquads are
# applied as their exact complex response on one zero-padded FFT per channel (equal to the IIR up to the 2 s pad)
_EQ_TMP = None
if PARTS and os.path.exists(os.path.join(os.path.dirname(os.path.abspath(PARTS)), "mix.json")):
    import json as _j0
    _meq = [b_ for b_ in _j0.load(open(os.path.join(os.path.dirname(os.path.abspath(PARTS)), "mix.json"))).get("master_eq", [])
            if isinstance(b_, dict)]
    if _meq:
        x0, sr0 = sf.read(SRC, dtype="float64", always_2d=True)
        n_ = len(x0) + 2 * sr0
        f_ = np.fft.rfftfreq(n_, 1 / sr0)
        H_ = np.ones(len(f_), complex)
        for b_ in _meq:
            H_ *= biquad_h(b_, f_, sr0)
        y0 = np.stack([np.fft.irfft(np.fft.rfft(x0[:, c_], n_) * H_, n_)[:len(x0)] for c_ in range(x0.shape[1])], axis=1)
        _EQ_TMP = tempfile.NamedTemporaryFile(suffix=".wav", delete=False).name
        sf.write(_EQ_TMP, y0.astype(np.float32), sr0, subtype="FLOAT")
        SRC = _EQ_TMP
        print("master EQ: " + ", ".join(f"{b_['type']} {b_['hz']:g} Hz {b_.get('db', 0):+g} dB" for b_ in _meq))
        del x0, y0
x, sr = sf.read(SRC)
S = np.nan_to_num(np.maximum(short_term(SRC), -70), nan=-70.0)
S = np.concatenate([S[15:], np.full(15, S[-1])])  # centre the 3 s window
loud = np.percentile(S[S > -59], 95)
knee = loud - KNEE_BELOW
Ss = smooth(S, SMOOTH_S)
LS_ = LIFT_SMOOTH_S or SMOOTH_S
Sl = smooth(S, LS_)
lift = smooth(np.clip((knee - Sl) * (1 - 1 / RATIO), 0, CAP_DB), LS_)
top = smooth(np.clip((Ss - (loud + TOP_ABOVE)) * (1 - 1 / TOP_RATIO), 0, None), SMOOTH_S)
if FAST_CAP_ABOVE is not None:
    # mvt1 c10 (critic C #1): the slow lift is capped by a lift computed from each frame's own loudness (S smoothed over
    # 1 s, knee + FAST_CAP_ABOVE), so short loud passages next to soft ones no longer inherit their neighbours' lift
    # (c09 delivered: bar 160 only 0.2 dB over bar 170 and 0.8 over bar 82 on momentary max; master 3.3 / 4.2 dB)
    fastcap = np.clip((knee + FAST_CAP_ABOVE - smooth(S, 1.0)) * (1 - 1 / RATIO), 0, CAP_DB)
    lift = smooth(np.minimum(lift, fastcap), 0.5)
if MOM_CAP_ABOVE is not None:
    Mo = np.nan_to_num(np.maximum(momentary(SRC), -70), nan=-70.0)
    Mo = np.concatenate([Mo[2:], np.full(2, Mo[-1])])   # centre the 0.4 s window
    Mo = np.concatenate([Mo, np.full(max(0, len(S) - len(Mo)), Mo[-1])])[:len(S)]
    Mmax = np.lib.stride_tricks.sliding_window_view(np.pad(Mo, (5, 5), mode="edge"), 11).max(axis=1)   # +-0.5 s
    mcap = np.clip(knee + MOM_CAP_ABOVE - Mmax, 0, CAP_DB)
    lift = np.minimum(lift, smooth(np.minimum(lift, mcap), MOM_CAP_SMOOTH_S))
gdb = lift - top
if RISE_DELAY_S > 0:   # mvt3 c13: see RISE_DELAY_S (the gain is computed at 10 frames per second)
    _d = max(1, int(round(RISE_DELAY_S * 10)))
    gdb = np.minimum(gdb, np.concatenate([np.full(_d, gdb[0]), gdb[:-_d]]))
# mvt1 c40 (critic C #3): score-timed ride trims from parts.json (see the usage)
TRIMS, q2s = [], None
if PARTS:
    import json as _json
    _pj = _json.load(open(PARTS))
    _tempo = sorted(_pj["tempo"])

    def q2s(q):
        t, lq, lb = 0.0, 0.0, _tempo[0][1]
        for tq, bpm in _tempo[1:]:
            if tq >= q:
                break
            t += (tq - lq) * 60 / lb; lq, lb = tq, bpm
        return t + (q - lq) * 60 / lb
    TRIMS = _pj.get("ride_trims", [])
if FIT:
    a_, b_ = FIT
    ia_, ib_ = int(round(q2s(a_) * 10)), int(round(q2s(b_) * 10))
    target = float(np.clip((knee - S[ia_:ib_].mean()) * (1 - 1 / RATIO), 0, CAP_DB)) - float(top[ia_:ib_].mean())
    qs_ = [a_] + [q for q in np.arange(np.ceil(a_ / 2) * 2, b_, 2.0) if q > a_ + 0.5] + [b_ - 0.1]
    row = [(round(a_ - 0.05, 3), 0.0)] + [(round(float(q), 3), round(target - float(np.interp(q2s(q) * 10, np.arange(len(gdb)), gdb)), 2))
                                          for q in qs_] + [(round(b_, 3), 0.0)]
    print(f"span {a_}-{b_}: mean S {S[ia_:ib_].mean():.1f}, knee {knee:.1f}, steady lift {target:.2f} dB; ride now "
          f"{gdb[ia_]:.2f} -> {gdb[ib_]:.2f} dB")
    print("RIDE_TRIMS row:", row)
    sys.exit(0)
for row in TRIMS:
    ts_ = np.array([q2s(q) for q, _ in row]); ds_ = np.array([d for _, d in row])
    tt_ = np.arange(len(gdb)) / 10
    inside = (tt_ >= ts_[0]) & (tt_ <= ts_[-1])
    gdb = gdb + np.where(inside, np.interp(tt_, ts_, ds_), 0.0)
    print(f"ride trims {row[0][0]}-{row[-1][0]} qn: {ds_.min():+.2f}..{ds_.max():+.2f} dB")
gain = 10 ** (np.interp(np.arange(len(x)) / sr, np.arange(len(gdb)) / 10, gdb) / 20)
y = x * (gain[:, None] if x.ndim > 1 else gain)
# mvt3 c23 (critic C #5, ruling 7): env DELIVER_HEAD = a wav of the sound before score qn 0 (render_cycle.py writes the
# stems' last 0.30 s of pre-roll: the strings' led attacks of the opening chord), put before the file at the first
# frame's ride gain with a 10 ms fade-in at its first sample. The delivered file then starts HEAD seconds before qn 0.
HEAD_S_ = 0.0
if os.environ.get("DELIVER_HEAD") and os.path.exists(os.environ["DELIVER_HEAD"]):
    h_, hsr_ = sf.read(os.environ["DELIVER_HEAD"], dtype="float64", always_2d=True)
    if hsr_ == sr and h_.shape[1] == (y.shape[1] if y.ndim > 1 else 1):
        nf_ = min(len(h_), int(0.01 * sr))
        h_[:nf_] *= np.linspace(0.0, 1.0, nf_)[:, None]
        h_ = h_ * 10 ** (gdb[0] / 20)
        y = np.concatenate([h_ if y.ndim > 1 else h_[:, 0], y])
        HEAD_S_ = len(h_) / sr
        print(f"head: {HEAD_S_:.3f} s before qn 0 put before the file (peak {20 * np.log10(np.abs(h_).max() + 1e-12):+.1f} dBFS)")
# mvt3 c26 (shared delivery item, Dan 2026-11-18; mockup-kit/README.md "Room-noise bed in the delivery"): a synthetic
# hall-air bed at ROOM_BED_LUFS integrated, added after the limiter and before the mp3 encode (so the quiet-passage lift
# does not raise it): pink noise, an extra first-order fall above 2.5 kHz, a fourth-order low cut at 84 Hz, partly
# correlated stereo (L = 0.8 a + 0.6 c, R = 0.8 b + 0.6 c), fixed seed. Env DELIVER_ROOM_BED_LUFS (default -60, "off")
_rb = os.environ.get("DELIVER_ROOM_BED_LUFS", "-60")
ROOM_BED_LUFS = None if _rb.strip().lower() == "off" else float(_rb)
_BED_CACHE = {}


def room_bed(n, sr_, td_):
    """(n, 2) float32 bed at ROOM_BED_LUFS integrated. mvt3 c27 (coordinator): Movement I c62's implementation, so every
    movement uses the same bed (seeds 6201-6203; low cut (f/84)^4 / (1 + (f/84)^4), first-order fall above 2.5 kHz,
    L = 0.8 a + 0.6 c, R = 0.8 b + 0.6 c, peak-normalised before the loudness scaling). The c26 bed differed in the low
    cut (Butterworth -3 dB at 84 Hz, theirs -6 dB there) and the seed; same level"""
    if n in _BED_CACHE:
        return _BED_CACHE[n]
    f = np.fft.rfftfreq(n, 1.0 / sr_)
    f[0] = 1.0
    g = 1 / np.sqrt(f) * 1 / np.sqrt(1 + (f / 2500.0) ** 2) * (f / 84.0) ** 4 / (1 + (f / 84.0) ** 4)
    g[0] = 0.0
    a, b, c = (np.fft.irfft(np.fft.rfft(np.random.default_rng(sd).standard_normal(n)) * g, n) for sd in (6201, 6202, 6203))
    z = np.stack([0.8 * a + 0.6 * c, 0.8 * b + 0.6 * c], axis=1)
    z /= np.abs(z).max()
    p_ = os.path.join(td_, "bed_raw.wav")
    sf.write(p_, (0.1 * z).astype(np.float32), sr_, subtype="FLOAT")
    bed = (0.1 * 10 ** ((ROOM_BED_LUFS - integrated(p_)["I"]) / 20) * z).astype(np.float32)
    sf.write(p_, bed, sr_, subtype="FLOAT")
    print(f"room bed: {integrated(p_)['I']} LUFS integrated, sample peak {20 * np.log10(np.abs(bed).max()):+.1f} dBFS")
    _BED_CACHE[n] = bed
    return bed


with tempfile.TemporaryDirectory() as td:
    rode = os.path.join(td, "ride.wav"); sf.write(rode, y, sr, subtype="FLOAT")
    lift = TARGET_I - integrated(rode)["I"]
    # mvt3 c21 (critic B c21 #1, coordinator ruling 1): the limiter's loss on the fff moments left the mp3 0.8 LU under
    # the target (-14.8 for -14.0). Loudness loop: after the limiter, encode and true-peak passes the mp3's integrated
    # loudness is measured; if it is more than LOUD_TOL under TARGET_I the pre-limiter gain is raised by the shortfall
    # (+0.05 dB) and the limiter runs again (LOUD_PASSES passes at most). Env DELIVER_LOUD_PASSES=1 turns it off
    for _loud_pass in range(LOUD_PASSES):
        before_lim = os.path.join(td, "pre.wav")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", rode, "-af", f"volume={lift:.2f}dB", "-c:a", "pcm_f32le", before_lim], check=True)
        pre_x = sf.read(before_lim, dtype="float32", always_2d=True)[0]
        peak_pre = float(np.abs(pre_x).max())
        # mvt1 c36 (critic C #5): the five highest pre-limiter peaks (sample peak per 50 ms window, at least 0.5 s apart),
        # in seconds of the file: the limiter's figure is often one phase crest, and a notch has to find it
        w_ = int(0.05 * sr)
        pk_ = np.abs(pre_x[: len(pre_x) // w_ * w_]).max(axis=1).reshape(-1, w_).max(axis=1)
        top5 = []
        for i_ in np.argsort(pk_)[::-1]:
            if all(abs(i_ - j_) * 0.05 >= 0.5 for j_ in top5):
                top5.append(int(i_))
            if len(top5) == 5:
                break
        print("pre-limiter peaks (s, dBFS): " + ", ".join(f"{(i_ + 0.5) * 0.05:.2f} {20 * np.log10(pk_[i_] + 1e-12):+.2f}"
                                                          for i_ in top5))
        lim = os.path.join(td, "lim.wav")
        # mvt3 c20: with 6-8 dB of limiting at -14 LUFS the mp3 encode made inter-sample overs (TP -0.8 dBTP at a 0.87
        # sample ceiling on a simulation of c20): after the encode the true peak is measured, and if it is over TP_MAX the
        # ceiling is lowered by the excess (+0.05 dB) and the limiter and encode run again (at most twice)
        ceil_ = CEIL
        for _tp_pass in range(3):
            LIMIT = LIMIT_FMT.format(ceil_)
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", before_lim, "-af", LIMIT, "-c:a", "pcm_f32le", lim], check=True)
            # mvt3 c20: DELIVER_KEEP_DIR=<dir> keeps the pre-limiter and limited wavs (pre.wav, lim.wav) for measuring the
            # limiter's gain reduction per bar
            if os.environ.get("DELIVER_KEEP_DIR"):
                os.makedirs(os.environ["DELIVER_KEEP_DIR"], exist_ok=True)
                shutil.copy(before_lim, os.path.join(os.environ["DELIVER_KEEP_DIR"], "pre.wav"))
                shutil.copy(lim, os.path.join(os.environ["DELIVER_KEEP_DIR"], "lim.wav"))
            # mvt1 c07 (critic C #6): the render runs 8 s past the last release for measurement; the delivered file ends TAIL_S
            # after the last 50 ms window above TAIL_DB dBFS, with a fade over its last FADE_S (an "attacca" into the next
            # movement is not a 7 s pause)
            z, zsr = sf.read(lim, dtype="float32", always_2d=True)
            w = int(0.05 * zsr)
            lv = 20 * np.log10(np.sqrt((z[: len(z) // w * w] ** 2).mean(axis=1).reshape(-1, w).mean(axis=1)) + 1e-12)
            last = (np.nonzero(lv > TAIL_DB)[0].max() + 1) * 0.05 if (lv > TAIL_DB).any() else len(z) / zsr
            end = min(len(z) / zsr, last + TAIL_S)
            enc_in = lim
            if ROOM_BED_LUFS is not None:   # mvt3 c26: the room bed after the limiter, before the encode
                zb = z + room_bed(len(z), zsr, td)[:, :z.shape[1]] if z.shape[1] <= 2 else z
                enc_in = os.path.join(td, "lim_bed.wav")
                sf.write(enc_in, zb.astype(np.float32), zsr, subtype="FLOAT")
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", enc_in, "-af",
                            f"atrim=end={end:.3f},afade=t=out:st={max(0.0, end - FADE_S):.3f}:d={FADE_S}", "-b:a", "192k", OUT],
                           check=True)
            tp_ = integrated(OUT)["TP"]
            if tp_ <= TP_MAX or _tp_pass == 2:
                break
            ceil_ *= 10 ** ((TP_MAX - tp_ - 0.05) / 20)
            print(f"true peak {tp_} dBTP over {TP_MAX}: limiter ceiling lowered to {ceil_:.3f}")
        i_now = integrated(OUT)["I"]
        short_ = TARGET_I - i_now
        print(f"loudness pass {_loud_pass + 1}: I {i_now} LUFS (lift {lift:+.2f} dB), shortfall {short_:+.2f} LU")
        if short_ <= LOUD_TOL or _loud_pass == LOUD_PASSES - 1:
            break
        lift += short_ + 0.05
m = integrated(OUT)
St = short_term(OUT); St = St[St > -59]
print(f"delivered: I {m['I']} LUFS, LRA {m['LRA']} LU, TP {m['TP']} dBTP; ride max +{gdb.max():.1f} dB, min {gdb.min():.1f} dB; "
      f"limiter about {max(0.0, 20*np.log10(peak_pre / ceil_)):.1f} dB on the loudest sample peak (ceiling {ceil_:.3f}); "
      f"p10-to-max short-term span {St.max() - np.percentile(St, 10):.1f} dB; "
      f"length {end:.2f} s (tail {end - last:.2f} s after the last window above {TAIL_DB:.0f} dBFS)")
if _EQ_TMP:
    os.remove(_EQ_TMP)
