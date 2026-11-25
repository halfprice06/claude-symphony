"""Delivery master for headphone listening: slow look-ahead gain ride on the quiet passages, constant gain to
-16 LUFS (scherzo c18; was -19.5), true-peak limiter at -1.0 dBTP (was -1.5), mp3. The climax is left alone.

Usage: python deliver_master.py <master.wav> <out.mp3> [<parts.json> [--fit-flat A B]]
  mvt1 c40 (critic C #3): with parts.json, its "ride_trims" (score_to_parts.py RIDE_TRIMS: rows of (score qn, dB)) are
  added to the ride's gain, converted to file seconds on its tempo map (the render is cut at score qn 0).
  --fit-flat A B prints, without writing the mp3, a RIDE_TRIMS row for score qn A..B that holds the ride at that
  span's own steady lift ((knee - its mean short-term loudness) x (1 - 1/RATIO)) instead of the slow interpolation
  between its neighbours (trims every 2 qn, ramped in and out over 0.05 qn); the listed trims are left out of the fit.
  mvt1 c50: with "master_eq" in the mix.json next to parts.json, the master is equalised first (see MASTER_EQ).
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
FAST_CAP_ABOVE = 4.0   # mvt1 c10 (critic C #1); None = off
# mvt1 c22 (critic C #3): a cap read from momentary loudness (400 ms, the max over +-0.5 s): no momentary peak is lifted
# above knee + MOM_CAP_ABOVE. The slow lift and FAST_CAP_ABOVE read short-term loudness (3 s), which a 0.3 s ff stab
# barely moves, so a stab between soft bars took their lift (bar 33 the 4th-loudest moment of the c21 mp3, bar 41 over
# the ff arrival at 117). None = off
# mvt2 c34 (critic C #4): 6 -> 3: the lift looked ahead into a pp and raised a brass ff accent before it to the
# loudest moment outside the climax (Trombone 1 218: -11.5 -> -13.9 LUFS momentary; LRA, span, limiter unchanged)
# scherzo c30 (critic C #1): 3 -> 0: the lift raised exposed p / pp solos' momentary peaks to knee + 3 dB, the f level
# (horn call bars 4-5 -10.3 LUFS momentary against bar 101's f hemiola -11.3; the pp violin solo over the trio's f);
# with 0 and four ride rows C simulated the horn call -13.3, the violin solo -13.7, every spec item passing
MOM_CAP_ABOVE, MOM_CAP_SMOOTH_S = 0.0, 0.5
TAIL_DB, TAIL_S, FADE_S = -65.0, 1.0, 0.5
# mvt1 c36 (critic C #6): the quiet-passage lift's own smoothing (both passes), separate from the top ride's SMOOTH_S.
# None = SMOOTH_S. Environment overrides for A/B deliveries of one master: DELIVER_RATIO, DELIVER_KNEE_BELOW,
# DELIVER_LIFT_SMOOTH_S
# mvt1 c36 (critic C #6, simulated on the c35 master with the c36 level changes): RATIO 2.5 -> 3.0, KNEE_BELOW 6 -> 5,
# LIFT_SMOOTH_S 5.0: the 3 s lift passed phrase-length swells into the gain, so soft passages kept a median 77% of
# their 5 s moves (19 under 50%); now 82% (3 under 50%), p50-p10 6.1 -> 7.0 dB, max-p75 8.5 -> 7.3 dB, LRA 14.7 -> 14.8,
# span 19.0, limiter 1.1 -> 0.9 dB, 0 inversions, bar 160 over bar 122 unchanged (0.8 LU)
RATIO, KNEE_BELOW = 3.0, 5.0
# mvt2 c30 (critic C #1): movement II's slow crescendos (bars 52-61, 71-78) kept only 41-52% of their rise with 3.0 / 5;
# on the c30 master 2.2 / 6 gave LRA 15.6 LU (3.0/5: 14.3), span 17.8 dB (16.5), limiter 1.3 dB (0.4); 2.0 / 6 went to
# LRA 16.3, over the 14-16 target
# scherzo c00 (port): movement II's 2.2 / 6 is for its slow crescendos; the scherzo (an Allegro, like movement I) keeps
# movement I's 3.0 / 5 above. DELIVER_RATIO / DELIVER_KNEE_BELOW still override for A/B deliveries
# RATIO, KNEE_BELOW = 2.2, 6.0
# scherzo c06 (EastWest template mix: Spaces II returns at the template's levels, full IRs): the wetter master compresses
# the soft-loud range (master LRA 23.1 -> 22.0 LU) and 3.0 / 5 delivered LRA 12.7 LU, span 17.9 dB. Refit on the c06
# master (cycles/c06/CHANGES.md): 2.5 / 6 LRA 13.8, span 18.8; 2.2 / 6 LRA 14.3, span 19.3; 2.2 / 5.5 LRA 14.0, span 19.0,
# limiter 3.4 dB (the fff summit's peak), true peak -1.6 dBTP
RATIO, KNEE_BELOW = 2.2, 5.5
LIFT_SMOOTH_S = 5.0
RATIO = float(os.environ.get("DELIVER_RATIO", RATIO))
KNEE_BELOW = float(os.environ.get("DELIVER_KNEE_BELOW", KNEE_BELOW))
LIFT_SMOOTH_S = float(os.environ["DELIVER_LIFT_SMOOTH_S"]) if os.environ.get("DELIVER_LIFT_SMOOTH_S") else LIFT_SMOOTH_S
# scherzo c18 (Dan 2026-11-17: "overall the tracks are too soft", listening on AirPods; the coordinator's provisional
# shared target until the mockup-kit guide has one): integrated -16 LUFS, LRA 10-12 LU, true peak -1.0 dBTP, the quiet
# passages lifted most, limiter at most 3 dB. TP_DB is the limiter ceiling; the old values are -19.5 / -1.5.
# Environment overrides for A/B deliveries: DELIVER_TARGET_I, DELIVER_TP_DB, DELIVER_CAP_DB
# (2026-11-17, mockup-kit/README.md "Shared delivery loudness target", Movement I's deliver_master.py): -16 LUFS within
# 0.5, -1.0 dBTP, LRA 12-13 LU, p10 short-term -25 LUFS or higher; quiet-lift knee 7 dB under p95, slow top ride from
# 10 dB under p95 at 3:1
# (Dan 2026-11-17 03:27Z: "-14 goal please"; limiter ceiling 0.87 (-1.21 dBFS): 0.891 missed -1.0 dBTP by 0.1 dB on
# the finale)
TARGET_I, TP_DB = -14.0, 20 * np.log10(0.87)
# (c18 render: ceiling 0.87 gave -0.9 dBTP after the mp3 encode: 0.85; the limiter takes about 0.6 LU of loudness at
# -14, so the pre-limiter level aims that much higher)
TP_DB, LIM_TAKES_DB = 20 * np.log10(0.85), 0.6
LIM_TAKES_DB = float(os.environ.get("DELIVER_LIM_TAKES_DB", LIM_TAKES_DB))
# scherzo: lift ratio 1.8 (simulated on the c17 master with the peak compressor below: 2.2 gave LRA 11.6, 2.0 12.0 /
# 11.8, 1.8 12.3 LU, p10 short-term -24.1, limiter 3.3 dB)
# (at -14 LUFS: 1.8 gave LRA 11.7, 1.6 12.3 LU on the c17 master; limiter 4.9 dB on the summit's peaks)
# (c18 render: top ride 3:1 gave LRA 11.7, 2.5:1 12.0 LU with the summit still 0.7 LU over the next loudest bar)
KNEE_BELOW, TOP_ABOVE, TOP_RATIO, RATIO = 7.0, -10.0, 2.5, 1.6
KNEE_BELOW = float(os.environ.get("DELIVER_KNEE_BELOW", KNEE_BELOW)); RATIO = float(os.environ.get("DELIVER_RATIO", RATIO))
TARGET_I = float(os.environ.get("DELIVER_TARGET_I", TARGET_I))
TP_DB = float(os.environ.get("DELIVER_TP_DB", TP_DB))
TP_MAX, LOUD_TOL = -1.0, 0.1
LOUD_PASSES = int(os.environ.get("DELIVER_LOUD_PASSES", 3))
CAP_DB = float(os.environ.get("DELIVER_CAP_DB", CAP_DB))
# scherzo c19 (finale c21, Movement I c61: 2:1 kept the printed order): top ride 2.5:1 -> 2:1 (c19 master: LRA 11.8 ->
# 12.3, limiter and climax order unchanged)
TOP_RATIO = 2.0
# scherzo c22 (critic C #1; shared delivery spec 2026-11-17, "climax margin before loudness range"): top ride from 6 dB
# under p95 (10 put every f, ff and fff over its threshold and halved the steps between them) and quiet lift 2.1 (C's
# simulation on the c21 master with the peak compressor below: summit lead 0.44 -> 0.72 LU, f -> ff 1.7 -> 2.2 LU, limiter
# at the summit 5.7 -> 3.0 dB, LRA 12.1 -> 10.6 with the c22 ride rows)
TOP_ABOVE, RATIO = -6.0, 2.1
# scherzo c29 (critic B #3; shared spec item 3, f -> ff 2 LU): top ride from 3 dB under p95 (B's simulation on the c28
# master with the deeper coda ride row and Violins I theme A +1.5 dB: f -> ff 1.88 -> 2.29 LU, summit lead 0.67 -> 0.76, LRA
# 10.9 -> 11.5, p10 -20.6 -> -21.0, limiter 3.7 -> 3.8)
TOP_ABOVE = -3.0
RATIO = float(os.environ.get("DELIVER_RATIO", RATIO))
TOP_ABOVE = float(os.environ.get("DELIVER_TOP_ABOVE", TOP_ABOVE)); TOP_RATIO = float(os.environ.get("DELIVER_TOP_RATIO", TOP_RATIO))
LIMIT_REPORT_BARS = [("summit 336-339", 336, 339), ("tutti 105-120", 105, 120), ("tutti 305-320", 305, 320), ("bar 72", 72, 72),
                     ("bar 300", 300, 300), ("final chord 375-376", 375, 376)]   # scherzo c18 (score bars)
# scherzo c18: a fast peak compressor before the limiter (the limiter's 4.6-5 dB at -16 LUFS came from short crests:
# accents and timpani strokes); "" = off. Environment override DELIVER_PEAK_COMP
# (without it the limiter did 4.0-4.4 dB at -16 LUFS on the c17 master; with it 3.3 dB, LRA -0.2 LU)
# scherzo c22 (critic C #1): -9 dB 3:1 (was -6 dB 2:1): the summit's pre-limiter crests (+2.4..+4.3 dBFS from the summed
# strings and hall) took 5.7 dB of limiting; with -9 / 3:1 3.0 dB
PEAK_COMP = os.environ.get("DELIVER_PEAK_COMP", "acompressor=threshold=-9dB:ratio=3:attack=2:release=60:knee=4:makeup=1")
LIMIT = f"aresample=192000,alimiter=limit={10 ** (TP_DB / 20):.4f}:attack=5:release=80:level=0:asc=1,aresample=48000"


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


# scherzo c23 (shared delivery spec, Dan approved 2026-11-18; mockup-kit README "Room-noise bed in the delivery"): a
# synthetic hall-air bed at ROOM_BED_LUFS integrated, added after the limiter and before the mp3 encode, so rests and
# fades end in room hiss, not digital silence: pink, an extra first-order fall above 2.5 kHz, a fourth-order low cut at
# 84 Hz, partly correlated stereo (L = 0.8 a + 0.6 c, R = 0.8 b + 0.6 c), fixed seed. env DELIVER_ROOM_BED_LUFS (default
# -60; "off" disables it)
_rb = os.environ.get("DELIVER_ROOM_BED_LUFS", "-60")
ROOM_BED_LUFS = None if _rb.lower() == "off" else float(_rb)
# scherzo c24 (coordinator, Movement I c62): the bed now matches Movement I's tools/deliver_master.py exactly (one bed
# for all movements): seeds 6201 / 6202 / 6203 (c23: one generator, seed 20261118), low cut (f/84)^4 / (1 + (f/84)^4)
# (c23: a Butterworth magnitude), peak-normalised before the loudness scaling (c23: RMS, with 50 ms ramps), added to
# the whole limited file before the trim and fade-out (c23: after them, so the fade did not take the bed)
ROOM_BED_LP_HZ, ROOM_BED_HP_HZ, ROOM_BED_SEEDS = 2500.0, 84.0, (6201, 6202, 6203)


def room_bed(n, sr, lufs, tmpdir):
    """(n, 2) float32 bed at lufs integrated (Movement I c62's room_bed)"""
    f = np.fft.rfftfreq(n, 1.0 / sr)
    f[0] = 1.0
    g = 1 / np.sqrt(f) * 1 / np.sqrt(1 + (f / ROOM_BED_LP_HZ) ** 2) * (f / ROOM_BED_HP_HZ) ** 4 / (1 + (f / ROOM_BED_HP_HZ) ** 4)
    g[0] = 0.0
    a, b, c = (np.fft.irfft(np.fft.rfft(np.random.default_rng(sd).standard_normal(n)) * g, n) for sd in ROOM_BED_SEEDS)
    z = np.stack([0.8 * a + 0.6 * c, 0.8 * b + 0.6 * c], axis=1)
    z /= np.abs(z).max()
    p_ = os.path.join(tmpdir, "bed_raw.wav")
    sf.write(p_, (0.1 * z).astype(np.float32), sr, subtype="FLOAT")
    k_ = 0.1 * 10 ** ((lufs - integrated(p_)["I"]) / 20)
    os.remove(p_)
    print(f"room bed: {lufs} LUFS integrated (pink, first-order fall above {ROOM_BED_LP_HZ:.0f} Hz, fourth-order low cut {ROOM_BED_HP_HZ:.0f} Hz, seeds {ROOM_BED_SEEDS})")
    return (k_ * z).astype(np.float32)


def smooth(v, sec, rate=10):  # zero-phase Gaussian
    n = max(1, int(sec * rate)); k = np.exp(-0.5 * (np.arange(-3 * n, 3 * n + 1) / n) ** 2); k /= k.sum()
    return np.convolve(np.pad(v, (3 * n, 3 * n), mode="edge"), k, "valid")


# mvt1 c50 (TEMPLATE-PLAN section 3, the template's master ReaEQ): mix.json "master_eq" (next to parts.json), a band list
# as "family_eqs" ({"band": highpass|lowpass|bell|lowshelf|highshelf, "hz", "db", "bw_oct"}), applied to the master
# before everything else here (ffmpeg biquads: RBJ filters with the bandwidth in octaves, as ReaEQ), so the ride, the
# -19.5 LUFS gain and the limiter all act on the equalised master. render/00_Master.wav itself is not changed. Absent =
# no EQ (as before).
MASTER_EQ = []
if PARTS and os.path.exists(os.path.join(os.path.dirname(os.path.abspath(PARTS)), "mix.json")):
    import json as _json_m
    MASTER_EQ = _json_m.load(open(os.path.join(os.path.dirname(os.path.abspath(PARTS)), "mix.json"))).get("master_eq") or []


def eq_filter(bands):
    """ffmpeg filter chain for a master_eq band list"""
    out = []
    for b in bands:
        kind, hz, bw = b["band"], float(b["hz"]), float(b.get("bw_oct", 2.0 if b["band"] in ("highpass", "lowpass") else 1.39))
        if kind in ("highpass", "lowpass"):
            out.append(f"{kind}=f={hz}:poles=2:width_type=o:width={bw}")
        elif kind == "bell":
            out.append(f"equalizer=f={hz}:width_type=o:width={bw}:gain={float(b.get('db', 0.0))}")
        elif kind in ("lowshelf", "highshelf"):
            out.append(f"{kind}=f={hz}:width_type=o:width={bw}:gain={float(b.get('db', 0.0))}")
        else:
            sys.exit(f"master_eq: band type {kind!r} (use highpass, lowpass, bell, lowshelf, highshelf)")
    return ",".join(out)


if MASTER_EQ:
    _eq_dir = tempfile.mkdtemp(prefix="deliver-eq-")
    _eq_src = os.path.join(_eq_dir, "master_eq.wav")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", SRC, "-af", eq_filter(MASTER_EQ), "-c:a", "pcm_f32le",
                    _eq_src], check=True)
    print("master EQ (mix.json master_eq): " + "; ".join(
        f"{b['band']} {b['hz']} Hz" + (f" {b['db']:+} dB" if "db" in b else "") + (f" bw {b['bw_oct']}" if "bw_oct" in b else "")
        for b in MASTER_EQ))
    SRC = _eq_src
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
with tempfile.TemporaryDirectory() as td:
    rode = os.path.join(td, "ride.wav"); sf.write(rode, y, sr, subtype="FLOAT")
    lift = TARGET_I - integrated(rode)["I"]
    # scherzo c19 (shared spec, loudness loop adopted for all movements; ported from the finale c21 / Movement I): after the
    # limiter and the mp3 encode the mp3's integrated loudness is measured; if it is more than LOUD_TOL under TARGET_I the
    # pre-limiter gain is raised by the shortfall + 0.05 dB and the limiter runs again (LOUD_PASSES passes at most; env
    # DELIVER_LOUD_PASSES=1 turns it off). The true peak is measured after the encode; if it is over TP_MAX the ceiling is
    # lowered by the excess + 0.05 dB and the limiter and encode run again (at most twice)
    ceil_db_ = TP_DB
    for _loud_pass in range(LOUD_PASSES):
        for _tp_pass in range(3):
            LIMIT = f"aresample=192000,alimiter=limit={10 ** (ceil_db_ / 20):.4f}:attack=5:release=80:level=0:asc=1,aresample=48000"
            before_lim = os.path.join(td, "pre.wav")
            for _it in range((3 if PEAK_COMP else 1) if _loud_pass == 0 and _tp_pass == 0 else 1):   # scherzo c18: the compressor lowers the level; correct the gain and redo
                subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", rode, "-af", f"volume={lift:.2f}dB" + (("," + PEAK_COMP) if PEAK_COMP else ""), "-c:a", "pcm_f32le", before_lim], check=True)
                if PEAK_COMP and _loud_pass == 0 and _tp_pass == 0:
                    _d = TARGET_I + LIM_TAKES_DB - integrated(before_lim)["I"]   # (what the limiter takes)
                    if abs(_d) < 0.1:
                        break
                    lift += _d
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
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", before_lim, "-af", LIMIT, "-c:a", "pcm_f32le", lim], check=True)
            # scherzo c18 (shared spec 2026-11-17): the limiter's gain reduction per passage (max over 50 ms windows of the
            # pre-limiter peak over the limited peak, the output moved back by the limiter's 5 ms look-ahead), bars in score bars of 3 qn (LIMIT_REPORT_BARS; needs parts.json)
            if q2s is not None and LIMIT_REPORT_BARS:
                _z = sf.read(lim, dtype="float32", always_2d=True)[0][int(0.005 * sr):]; _n = min(len(_z), len(pre_x)) // w_ * w_
                _a = np.abs(pre_x[:_n]).max(axis=1).reshape(-1, w_).max(axis=1); _b = np.abs(_z[:_n]).max(axis=1).reshape(-1, w_).max(axis=1)
                _gr = np.where(_b > 1e-3, 20 * np.log10((_a + 1e-9) / (_b + 1e-9)), 0.0)
                print("limiter per passage (max dB): " + "; ".join(
                    f"{nm_} {_gr[int(q2s(3 * b0_ - 3) / 0.05):max(int(q2s(3 * b1_) / 0.05), int(q2s(3 * b0_ - 3) / 0.05) + 1)].max():.1f}"
                    for nm_, b0_, b1_ in LIMIT_REPORT_BARS) + f"; whole file {_gr.max():.1f}")
            # mvt1 c07 (critic C #6): the render runs 8 s past the last release for measurement; the delivered file ends TAIL_S
            # after the last 50 ms window above TAIL_DB dBFS, with a fade over its last FADE_S (an "attacca" into the next
            # movement is not a 7 s pause)
            z, zsr = sf.read(lim, dtype="float32", always_2d=True)
            w = int(0.05 * zsr)
            lv = 20 * np.log10(np.sqrt((z[: len(z) // w * w] ** 2).mean(axis=1).reshape(-1, w).mean(axis=1)) + 1e-12)
            last = (np.nonzero(lv > TAIL_DB)[0].max() + 1) * 0.05 if (lv > TAIL_DB).any() else len(z) / zsr
            end = min(len(z) / zsr, last + TAIL_S)
            _af = f"atrim=end={end:.3f},afade=t=out:st={max(0.0, end - FADE_S):.3f}:d={FADE_S}"
            if ROOM_BED_LUFS is None:
                subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", lim, "-af", _af, "-b:a", "192k", OUT], check=True)
            else:   # scherzo c23 (shared spec, mockup-kit README "Room-noise bed in the delivery"): after the limiter
                _bedf = lim[:-4] + "_bed.wav"
                if z.shape[1] == 1:
                    z = np.repeat(z, 2, axis=1)
                if "_bed" not in globals() or len(_bed) != len(z):
                    _bed = room_bed(len(z), zsr, ROOM_BED_LUFS, os.path.dirname(lim))
                sf.write(_bedf, z + _bed, zsr, subtype="FLOAT")
                subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", _bedf, "-af", _af, "-b:a", "192k", OUT], check=True)
            tp_ = integrated(OUT)["TP"]
            if tp_ <= TP_MAX or _tp_pass == 2:
                break
            ceil_db_ += TP_MAX - tp_ - 0.05
            print(f"true peak {tp_} dBTP over {TP_MAX}: limiter ceiling lowered to {ceil_db_:.2f} dBFS")
        i_now = integrated(OUT)["I"]
        short_ = TARGET_I - i_now
        print(f"loudness pass {_loud_pass + 1}: I {i_now} LUFS (gain {lift:+.2f} dB), shortfall {short_:+.2f} LU")
        if short_ <= LOUD_TOL or _loud_pass == LOUD_PASSES - 1:
            break
        lift += short_ + 0.05
m = integrated(OUT)
St = short_term(OUT); St = St[St > -59]
_p10 = np.percentile(St, 10)
print(f"short-term p10 {_p10:.1f} LUFS, max {St.max():.1f}")
print(f"delivered: I {m['I']} LUFS, LRA {m['LRA']} LU, TP {m['TP']} dBTP; ride max +{gdb.max():.1f} dB, min {gdb.min():.1f} dB; "
      f"limiter about {max(0.0, 20*np.log10(peak_pre) - ceil_db_):.1f} dB on the loudest sample peak; "
      f"p10-to-max short-term span {St.max() - np.percentile(St, 10):.1f} dB; "
      f"length {end:.2f} s (tail {end - last:.2f} s after the last window above {TAIL_DB:.0f} dBFS)")
if MASTER_EQ:   # mvt1 c50
    shutil.rmtree(_eq_dir, ignore_errors=True)
