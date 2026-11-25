"""Delivery master for headphone listening: slow look-ahead gain ride on the quiet passages, constant gain to
-19 LUFS, true-peak limiter at -1.5 dBTP, mp3. The climax is left alone.

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
RATIO = float(os.environ.get("DELIVER_RATIO", RATIO))
KNEE_BELOW = float(os.environ.get("DELIVER_KNEE_BELOW", KNEE_BELOW))
LIFT_SMOOTH_S = float(os.environ["DELIVER_LIFT_SMOOTH_S"]) if os.environ.get("DELIVER_LIFT_SMOOTH_S") else LIFT_SMOOTH_S
LIMIT = "aresample=192000,alimiter=limit=0.841:attack=5:release=80:level=0:asc=1,aresample=48000"


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
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", before_lim, "-af", LIMIT, "-c:a", "pcm_f32le", lim], check=True)
    # mvt1 c07 (critic C #6): the render runs 8 s past the last release for measurement; the delivered file ends TAIL_S
    # after the last 50 ms window above TAIL_DB dBFS, with a fade over its last FADE_S (an "attacca" into the next
    # movement is not a 7 s pause)
    z, zsr = sf.read(lim, dtype="float32", always_2d=True)
    w = int(0.05 * zsr)
    lv = 20 * np.log10(np.sqrt((z[: len(z) // w * w] ** 2).mean(axis=1).reshape(-1, w).mean(axis=1)) + 1e-12)
    last = (np.nonzero(lv > TAIL_DB)[0].max() + 1) * 0.05 if (lv > TAIL_DB).any() else len(z) / zsr
    end = min(len(z) / zsr, last + TAIL_S)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", lim, "-af",
                    f"atrim=end={end:.3f},afade=t=out:st={max(0.0, end - FADE_S):.3f}:d={FADE_S}", "-b:a", "192k", OUT],
                   check=True)
m = integrated(OUT)
St = short_term(OUT); St = St[St > -59]
print(f"delivered: I {m['I']} LUFS, LRA {m['LRA']} LU, TP {m['TP']} dBTP; ride max +{gdb.max():.1f} dB, min {gdb.min():.1f} dB; "
      f"limiter about {max(0.0, 20*np.log10(peak_pre) + 1.5):.1f} dB on the loudest sample peak; "
      f"p10-to-max short-term span {St.max() - np.percentile(St, 10):.1f} dB; "
      f"length {end:.2f} s (tail {end - last:.2f} s after the last window above {TAIL_DB:.0f} dBFS)")
if MASTER_EQ:   # mvt1 c50
    shutil.rmtree(_eq_dir, ignore_errors=True)
