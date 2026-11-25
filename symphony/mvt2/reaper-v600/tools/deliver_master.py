"""Delivery master for headphone listening: slow look-ahead gain ride on the quiet passages, constant gain to
-19 LUFS, true-peak limiter at -1.5 dBTP, mp3. The climax is left alone.

Usage: python deliver_master.py <master.wav> <out.mp3>
Method and targets: loop/DYNAMICS-RESEARCH.md (LRA 14-16 LU, BBC classical guideline 15 LU; no inversions of
crescendos/diminuendos; limiter at most about 3 dB). Prints the measurements of the result.
"""
import os, re, subprocess, sys, tempfile
import numpy as np
import soundfile as sf

SRC, OUT = sys.argv[1], sys.argv[2]
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
# mvt2 c50 (critic C #5): 2.5 -> 2.0: the top ride took 3.1 dB more from the climax (bar 61) than from the ff cadence
# (bar 79). On the c50 master: span 18.1 -> 18.5 dB, limiter 1.7 -> 1.5 dB, LRA 14.6 -> 14.9 (limits: span 18.7, limiter 3)
TOP_ABOVE, TOP_RATIO = -3.0, 2.0
FAST_CAP_ABOVE = 4.0   # mvt1 c10 (critic C #1); None = off
# mvt1 c22 (critic C #3): a cap read from momentary loudness (400 ms, the max over +-0.5 s): no momentary peak is lifted
# above knee + MOM_CAP_ABOVE. The slow lift and FAST_CAP_ABOVE read short-term loudness (3 s), which a 0.3 s ff stab
# barely moves, so a stab between soft bars took their lift (bar 33 the 4th-loudest moment of the c21 mp3, bar 41 over
# the ff arrival at 117). None = off
# mvt2 c34 (critic C #4): 6 -> 3: the lift looked ahead into a pp and raised a brass ff accent before it to the
# loudest moment outside the climax (Trombone 1 218: -11.5 -> -13.9 LUFS momentary; LRA, span, limiter unchanged)
MOM_CAP_ABOVE, MOM_CAP_SMOOTH_S = 3.0, 0.5
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
RATIO, KNEE_BELOW = 2.2, 6.0
# mvt2 c44 (EW template mix, re-fit): 2.2 gave span 19.1 dB on the dry + returns master; 2.4: LRA 15.2, span 18.8, limiter 1.9
RATIO = 2.4
LIFT_SMOOTH_S = 5.0
# mvt2 c52 (critic C #2; the finale's c13 technique 35): RISE_DELAY_S. The gain at time t is the lower of its value at t
# and at t - RISE_DELAY_S, so gain rises wait that long (the ride no longer lifts a printed diminuendo while it is
# still falling) and gain falls are not delayed. 0 = off; mix.json "deliver": {"rise_delay_s": ...} sets it for a score;
# environment override DELIVER_RISE_DELAY_S
RISE_DELAY_S = 0.0
_MIXJ0 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "build", "mix.json")
if os.path.exists(_MIXJ0):
    import json as _jd0
    RISE_DELAY_S = float((_jd0.load(open(_MIXJ0)).get("deliver") or {}).get("rise_delay_s", RISE_DELAY_S))
RISE_DELAY_S = float(os.environ.get("DELIVER_RISE_DELAY_S", RISE_DELAY_S))
RATIO = float(os.environ.get("DELIVER_RATIO", RATIO))
KNEE_BELOW = float(os.environ.get("DELIVER_KNEE_BELOW", KNEE_BELOW))
LIFT_SMOOTH_S = float(os.environ["DELIVER_LIFT_SMOOTH_S"]) if os.environ.get("DELIVER_LIFT_SMOOTH_S") else LIFT_SMOOTH_S
# mvt2 c57 (Dan, 16 Nov: "overall the tracks are too soft", pp detail inaudible on AirPods): target, true-peak ceiling and
# the lift cap can be set per score in mix.json "deliver" {"target_i", "tp_db", "cap_db", "ratio", "knee_below"} or by
# the environment (DELIVER_TARGET_I, DELIVER_TP_DB, DELIVER_CAP_DB, DELIVER_RATIO, DELIVER_KNEE_BELOW). Defaults are the
# old settings (-19.5 LUFS, -1.5 dBTP, cap 10 dB), so a delivery at the old level needs only DELIVER_OLD=1 (ignores
# the mix.json values)
TP_DB = -1.5
if os.path.exists(_MIXJ0) and not os.environ.get("DELIVER_OLD"):
    _dv = _jd0.load(open(_MIXJ0)).get("deliver") or {}
    TARGET_I = float(_dv.get("target_i", TARGET_I)); TP_DB = float(_dv.get("tp_db", TP_DB)); CAP_DB = float(_dv.get("cap_db", CAP_DB))
    RATIO = float(_dv.get("ratio", RATIO)); KNEE_BELOW = float(_dv.get("knee_below", KNEE_BELOW))
    TOP_ABOVE = float(_dv.get("top_above", TOP_ABOVE)); TOP_RATIO = float(_dv.get("top_ratio", TOP_RATIO))
    MOM_CAP_ABOVE = float(_dv.get("mom_cap_above", MOM_CAP_ABOVE))
TARGET_I = float(os.environ.get("DELIVER_TARGET_I", TARGET_I)); TP_DB = float(os.environ.get("DELIVER_TP_DB", TP_DB))
CAP_DB = float(os.environ.get("DELIVER_CAP_DB", CAP_DB))
RATIO = float(os.environ.get("DELIVER_RATIO", RATIO)); KNEE_BELOW = float(os.environ.get("DELIVER_KNEE_BELOW", KNEE_BELOW))
TOP_ABOVE = float(os.environ.get("DELIVER_TOP_ABOVE", TOP_ABOVE)); TOP_RATIO = float(os.environ.get("DELIVER_TOP_RATIO", TOP_RATIO))
MOM_CAP_ABOVE = float(os.environ.get("DELIVER_MOM_CAP_ABOVE", MOM_CAP_ABOVE))
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


# mvt3 c06 (EW template, plan item 3; ported mvt2 c44): mix.json "master_eq" (build/mix.json of this work folder; the
# template's master ReaEQ) is applied here, before the ride, so 00_Master.wav stays the plain sum of the stems (dry +
# return stems). The biquads are applied as their exact complex response on one zero-padded FFT per channel
_EQ_TMP = None
_MIXJ = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "build", "mix.json")
if os.path.exists(_MIXJ):
    import json as _j0
    _meq = [b_ for b_ in _j0.load(open(_MIXJ)).get("master_eq", []) if isinstance(b_, dict)]
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
if RISE_DELAY_S > 0:   # mvt2 c52: see RISE_DELAY_S (the gain is computed at 10 frames per second)
    _d = max(1, int(round(RISE_DELAY_S * 10)))
    gdb = np.minimum(gdb, np.concatenate([np.full(_d, gdb[0]), gdb[:-_d]]))
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
    if os.environ.get("DELIVER_LOAD_OUT"):   # mvt2 c57: per-50 ms limiter load (dB over the ceiling) for a passage report
        np.save(os.environ["DELIVER_LOAD_OUT"], 20 * np.log10(pk_ + 1e-12) - TP_DB)
    _ov = 20 * np.log10(pk_ + 1e-12) - TP_DB   # mvt2 c57: how much of the file the limiter works on (50 ms windows)
    print(f"limiter load: windows over the ceiling by 1 / 3 dB: {(_ov > 1).sum()} / {(_ov > 3).sum()} of {len(_ov)} "
          f"({(_ov > 1).sum() * 0.05:.1f} / {(_ov > 3).sum() * 0.05:.1f} s); last 20 s max {_ov[-400:].max():+.1f} dB")
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
      f"limiter about {max(0.0, 20*np.log10(peak_pre) - TP_DB):.1f} dB on the loudest sample peak; "
      f"p10-to-max short-term span {St.max() - np.percentile(St, 10):.1f} dB; "
      f"length {end:.2f} s (tail {end - last:.2f} s after the last window above {TAIL_DB:.0f} dBFS)")
Mt = momentary(OUT); Mt = Mt[Mt > -59]
print(f"settings: target {TARGET_I} LUFS, ceiling {TP_DB} dBTP, ratio {RATIO}, knee {KNEE_BELOW} dB below p95, cap {CAP_DB} dB, "
      f"top ride {TOP_ABOVE} dB from p95 at {TOP_RATIO}:1, momentary cap {MOM_CAP_ABOVE}; short-term p10 {np.percentile(St, 10):.1f} LUFS; "
      f"momentary p10 {np.percentile(Mt, 10):.1f} LUFS (quietest 10 % mean {Mt[Mt <= np.percentile(Mt, 10)].mean():.1f}), max {Mt.max():.1f}")
if _EQ_TMP:
    os.remove(_EQ_TMP)
