"""rtk: render toolkit library (measurement helpers shared by the scripts in this folder).

Functions here are imported by measure.py, compare.py, stems.py and sfcal.py.
Only numpy, scipy, mido and ffmpeg are needed (matplotlib for plots).
"""
import json, re, subprocess
import numpy as np
from scipy import signal

SR = 44100  # analysis sample rate; every file is resampled to this on decode


# ---------------------------------------------------------------- audio I/O
def decode(path, sr=SR, start=None, dur=None):
    """Decode any audio file with ffmpeg to float32 stereo array (n, 2) at sr."""
    cmd = ["ffmpeg", "-v", "error"]
    if start is not None:
        cmd += ["-ss", str(start)]
    if dur is not None:
        cmd += ["-t", str(dur)]
    cmd += ["-i", str(path), "-map", "0:a:0", "-f", "f32le", "-ac", "2", "-ar", str(sr), "-"]
    raw = subprocess.run(cmd, stdout=subprocess.PIPE, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).reshape(-1, 2).copy()


def ffmpeg_ebur128(path, start=None, dur=None):
    """Official numbers from ffmpeg's ebur128 filter: I (LUFS), LRA (LU), LRA low/high, true peak (dBTP)."""
    cmd = ["ffmpeg", "-nostats", "-hide_banner"]
    if start is not None:
        cmd += ["-ss", str(start)]
    if dur is not None:
        cmd += ["-t", str(dur)]
    cmd += ["-i", str(path), "-map", "0:a:0", "-af", "ebur128=peak=true", "-f", "null", "-"]
    err = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.DEVNULL).stderr.decode()
    s = err[err.rfind("Summary:"):]
    def g(pat):
        m = re.search(pat, s)
        return float(m.group(1)) if m and m.group(1) not in ("-inf", "inf") else None
    return {"I_LUFS": g(r"I:\s+(-?[\d.]+|-inf) LUFS"), "LRA_LU": g(r"LRA:\s+(-?[\d.]+) LU"),
            "LRA_low_LUFS": g(r"LRA low:\s+(-?[\d.]+|-inf) LUFS"), "LRA_high_LUFS": g(r"LRA high:\s+(-?[\d.]+|-inf) LUFS"),
            "true_peak_dBTP": g(r"Peak:\s+(-?[\d.]+|-inf) dBFS")}


# ---------------------------------------------------------------- loudness (ITU-R BS.1770 / EBU R128)
def k_weight(x, sr=SR):
    """K-weighting filter (BS.1770-4), coefficients derived for any sample rate (as in pyloudnorm)."""
    # stage 1: high shelf
    G, Q, fc = 3.999843853973347, 0.7071752369554196, 1681.974450955533
    A = 10 ** (G / 40); K = np.tan(np.pi * fc / sr); Vh = 10 ** (G / 20); Vb = Vh ** 0.4996667741545416
    a0 = 1 + K / Q + K * K
    b1 = [(Vh + Vb * K / Q + K * K) / a0, 2 * (K * K - Vh) / a0, (Vh - Vb * K / Q + K * K) / a0]
    a1 = [1, 2 * (K * K - 1) / a0, (1 - K / Q + K * K) / a0]
    # stage 2: high pass
    Q, fc = 0.5003270373238773, 38.13547087602444
    K = np.tan(np.pi * fc / sr)
    a2 = [1, 2 * (K * K - 1) / (1 + K / Q + K * K), (1 - K / Q + K * K) / (1 + K / Q + K * K)]
    b2 = [1, -2, 1]
    y = signal.lfilter(b1, a1, x, axis=0)
    return signal.lfilter(b2, a2, y, axis=0)


def loudness_series(x, sr=SR, win=0.4, hop=0.1):
    """Ungated loudness (LUFS) of sliding windows: win=0.4 -> momentary, win=3.0 -> short-term.
    Returns (times of window centres, LUFS array)."""
    y = k_weight(x, sr)
    p = (y ** 2).sum(axis=1)  # channel weights 1.0 for L and R
    c = np.concatenate([[0.0], np.cumsum(p)])
    w = int(win * sr); h = int(hop * sr)
    starts = np.arange(0, max(1, len(p) - w + 1), h)
    ms = (c[starts + w] - c[starts]) / w
    t = (starts + w / 2) / sr
    return t, -0.691 + 10 * np.log10(ms + 1e-12)


def integrated(m_lufs):
    """Gated integrated loudness from momentary (400 ms, 75 % overlap ideally) values."""
    z = 10 ** ((m_lufs + 0.691) / 10)
    g = m_lufs > -70
    if not g.any():
        return -70.0
    rel = -0.691 + 10 * np.log10(z[g].mean()) - 10
    g2 = g & (m_lufs > rel)
    return float(-0.691 + 10 * np.log10(z[g2].mean()))


def lra(s_lufs):
    """Loudness range (EBU Tech 3342) from short-term (3 s) values."""
    g = s_lufs > -70
    z = 10 ** ((s_lufs[g] + 0.691) / 10)
    rel = -0.691 + 10 * np.log10(z.mean()) - 20
    v = s_lufs[g][s_lufs[g] > rel]
    return float(np.percentile(v, 95) - np.percentile(v, 10)), float(np.percentile(v, 10)), float(np.percentile(v, 95))


def power_mean_lufs(vals):
    v = np.asarray(vals)
    v = v[np.isfinite(v)]
    if len(v) == 0:
        return float("nan")
    return float(-0.691 + 10 * np.log10(np.mean(10 ** ((v + 0.691) / 10))))


# ---------------------------------------------------------------- spectrum
THIRD_OCT = 1000 * 2 ** (np.arange(-16, 14) / 3)  # 25 Hz .. 20 kHz centre frequencies


def psd(mono, sr=SR, nfft=8192):
    f, P = signal.welch(mono, sr, nperseg=nfft, noverlap=nfft // 2, window="hann", scaling="density")
    return f, P


def third_octave(f, P):
    """Band powers (dB, relative to the total over 25 Hz-20 kHz) on THIRD_OCT centres."""
    out = []
    for fc in THIRD_OCT:
        lo, hi = fc / 2 ** (1 / 6), fc * 2 ** (1 / 6)
        m = (f >= lo) & (f < hi)
        out.append(P[m].sum() if m.any() else 1e-20)
    out = np.array(out)
    return 10 * np.log10(out / out.sum() + 1e-20)


def band_shares(f, P, edges=(20, 100, 250, 500, 2000, 6000, 20000)):
    tot = P[(f >= edges[0]) & (f < edges[-1])].sum()
    res = {}
    for lo, hi in zip(edges[:-1], edges[1:]):
        res[f"{lo}-{hi}Hz"] = round(float(10 * np.log10(P[(f >= lo) & (f < hi)].sum() / tot + 1e-20)), 2)
    return res


def spectral_slope(f, P, lo=100, hi=10000):
    """Least-squares slope of the 1/3-octave LTAS in dB per octave between lo and hi."""
    bands = third_octave(f, P)
    m = (THIRD_OCT >= lo) & (THIRD_OCT <= hi)
    return float(np.polyfit(np.log2(THIRD_OCT[m]), bands[m], 1)[0])


def centroid_series(mono, sr=SR, nfft=4096, hop=2048):
    f, t, Z = signal.stft(mono, sr, nperseg=nfft, noverlap=nfft - hop)
    S = np.abs(Z) ** 2
    c = (f[:, None] * S).sum(0) / (S.sum(0) + 1e-20)
    return t, c, f, S


# ---------------------------------------------------------------- envelopes and decay
def env_db(x, sr=SR, win=0.03, hop=0.01):
    p = (x.astype(np.float64) ** 2).mean(axis=1) if x.ndim == 2 else x.astype(np.float64) ** 2
    c = np.concatenate([[0.0], np.cumsum(p)])
    w = int(win * sr); h = int(hop * sr)
    st = np.arange(0, max(1, len(p) - w), h)
    e = (c[st + w] - c[st]) / w
    return (st + w / 2) / sr, 10 * np.log10(e + 1e-14)


def decay_fit(t, e, t0, floor_db=None, max_len=8.0):
    """Decay after time t0 on envelope e (dB). Returns level at t0, the time to fall 10/20/30 dB,
    the T20-based RT60 estimate (fit between -5 and -25 dB) and the noise floor used."""
    m = (t >= t0) & (t < t0 + max_len)
    tt, ee = t[m] - t0, e[m]
    if len(ee) < 10:
        return None
    L0 = float(np.max(ee[:5]))
    if floor_db is None:
        floor_db = float(np.percentile(ee[-max(5, len(ee) // 10):], 50))
    res = {"t0_s": round(float(t0), 2), "level_at_t0_dB": round(L0, 1), "floor_dB": round(floor_db, 1)}
    for d in (10, 20, 30, 40):
        k = np.where(ee <= L0 - d)[0]
        res[f"t_minus{d}dB_s"] = round(float(tt[k[0]]), 3) if len(k) else None
    a = np.where(ee <= L0 - 5)[0]; b = np.where(ee <= L0 - 25)[0]
    if len(a) and len(b) and b[0] > a[0] + 3 and L0 - 25 > floor_db + 5:
        sl = np.polyfit(tt[a[0]:b[0]], ee[a[0]:b[0]], 1)[0]
        res["RT60_from_T20_s"] = round(float(-60 / sl), 2) if sl < 0 else None
    else:
        res["RT60_from_T20_s"] = None
    a = np.where(ee <= L0 - 1)[0]; b = np.where(ee <= L0 - 10)[0]
    if len(a) and len(b) and b[0] > a[0] + 2:
        sl = np.polyfit(tt[a[0]:b[0]], ee[a[0]:b[0]], 1)[0]
        res["EDT_s"] = round(float(-60 / sl), 2) if sl < 0 else None
    else:
        res["EDT_s"] = None
    return res


# ---------------------------------------------------------------- stereo
def stereo_stats(x, sr=SR):
    L, R = x[:, 0].astype(np.float64), x[:, 1].astype(np.float64)
    def corr(a, b):
        d = np.sqrt((a * a).sum() * (b * b).sum())
        return float((a * b).sum() / d) if d > 0 else float("nan")
    M, S = (L + R) / 2, (L - R) / 2
    out = {"corr_LR": round(corr(L, R), 3),
           "side_to_mid_dB": round(float(10 * np.log10((S * S).sum() / ((M * M).sum() + 1e-20) + 1e-20)), 1),
           "balance_R_minus_L_dB": round(float(10 * np.log10((R * R).sum() / ((L * L).sum() + 1e-20) + 1e-20)), 2)}
    for name, (lo, hi) in {"low<250": (20, 250), "mid250-4k": (250, 4000), "high>4k": (4000, 18000)}.items():
        sos = signal.butter(4, [lo, hi], btype="band", fs=sr, output="sos")
        l, r = signal.sosfilt(sos, L), signal.sosfilt(sos, R)
        out[f"corr_{name}"] = round(corr(l, r), 3)
    # energy-weighted spread of the pan position of time-frequency bins (0 = all centre, 1 = hard L/R)
    f, t, ZL = signal.stft(L, sr, nperseg=2048); _, _, ZR = signal.stft(R, sr, nperseg=2048)
    aL, aR = np.abs(ZL), np.abs(ZR)
    pan = (aR - aL) / (aR + aL + 1e-12)
    w = aL ** 2 + aR ** 2
    out["pan_spread_std"] = round(float(np.sqrt((w * pan ** 2).sum() / w.sum())), 3)
    hist, edges = np.histogram(pan, bins=10, range=(-1, 1), weights=w)
    out["pan_energy_hist_L_to_R"] = [round(float(v), 3) for v in hist / hist.sum()]
    return out


# ---------------------------------------------------------------- MIDI
def midi_info(path):
    """Tempo map, bar start times (s), per-bar note statistics, note list, silences (all notes off)."""
    import mido
    mid = mido.MidiFile(path)
    tpb = mid.ticks_per_beat
    tempos, tsigs, markers = [(0, 500000)], [(0, 4, 4)], []
    notes = []  # (on_tick, off_tick, track, channel, pitch, vel)
    for ti, tr in enumerate(mid.tracks):
        tick = 0; open_ = {}
        name = next((m.name for m in tr if m.type == "track_name"), f"track{ti}")
        for m in tr:
            tick += m.time
            if m.type == "set_tempo":
                tempos.append((tick, m.tempo))
            elif m.type == "time_signature":
                tsigs.append((tick, m.numerator, m.denominator))
            elif m.type == "marker":
                markers.append((tick, m.text))
            elif m.type == "note_on" and m.velocity > 0:
                open_.setdefault((m.channel, m.note), []).append((tick, m.velocity))
            elif m.type in ("note_off", "note_on"):
                k = (m.channel, m.note)
                if open_.get(k):
                    on, v = open_[k].pop(0)
                    notes.append((on, tick, ti, m.channel, m.note, v, name))
    tempos = sorted(dict(tempos).items())
    tsigs = sorted({t: (n, d) for t, n, d in tsigs}.items())
    # tick -> seconds
    tt = np.array([t for t, _ in tempos], dtype=float); tv = np.array([v for _, v in tempos], dtype=float)
    secs = np.concatenate([[0.0], np.cumsum(np.diff(tt) * tv[:-1] / 1e6 / tpb)])
    def t2s(tick):
        tick = np.asarray(tick, dtype=float)
        i = np.searchsorted(tt, tick, side="right") - 1
        return secs[i] + (tick - tt[i]) * tv[i] / 1e6 / tpb
    end_tick = max(n[1] for n in notes)
    bars = []; tick = 0; k = 0
    while tick < end_tick:
        while k + 1 < len(tsigs) and tsigs[k + 1][0] <= tick:
            k += 1
        num, den = tsigs[k][1]
        bars.append(tick); tick += int(num * tpb * 4 / den)
    bars.append(tick)
    bar_s = t2s(bars)
    N = np.array([(n[0], n[1], n[4], n[5]) for n in notes], dtype=float)
    on_s, off_s = t2s(N[:, 0]), t2s(N[:, 1])
    # silences: spans where no note sounds, >= 0.25 s
    order = np.argsort(on_s); cur_end = 0.0; gaps = []
    for i in order:
        if on_s[i] - cur_end >= 0.25 and cur_end > 0:
            gaps.append((float(cur_end), float(on_s[i])))
        cur_end = max(cur_end, off_s[i])
    per_bar = []
    for b in range(len(bars) - 1):
        m = (N[:, 0] >= bars[b]) & (N[:, 0] < bars[b + 1])
        v = N[m, 3]
        # sounding notes in bar (overlapping)
        s = (N[:, 0] < bars[b + 1]) & (N[:, 1] > bars[b])
        per_bar.append({"bar": b + 1, "t_start": round(float(bar_s[b]), 3), "t_end": round(float(bar_s[b + 1]), 3),
                        "onsets": int(m.sum()), "sounding": int(s.sum()),
                        "vel_median": float(np.median(v)) if len(v) else None,
                        "vel_max": float(v.max()) if len(v) else None,
                        "vel_sounding_max": float(N[s, 3].max()) if s.any() else None})
    return {"tpb": tpb, "bar_ticks": bars, "bar_s": [float(x) for x in bar_s], "per_bar": per_bar,
            "markers": [(float(t2s(t)), txt, 1 + bars.index(t) if t in bars else None) for t, txt in markers],
            "last_note_off_s": float(off_s.max()), "first_note_on_s": float(on_s.min()),
            "gaps": gaps, "note_on_s": on_s, "note_off_s": off_s, "notes": notes, "t2s": t2s}


def vel_to_dyn(v):
    """Map a LilyPond velocity to the printed dynamic (v120 dynamicAbsoluteVolumeFunction x 127)."""
    if v is None:
        return None
    for lim, d in ((37, "ppp"), (47, "pp"), (58, "p"), (68, "mp"), (78, "mf"), (87, "f"), (100, "ff")):
        if v <= lim:
            return d
    return "fff/acc"


def save_json(obj, path):
    def conv(o):
        if isinstance(o, (np.floating,)):
            return float(o)
        if isinstance(o, (np.integer,)):
            return int(o)
        if isinstance(o, np.ndarray):
            return o.tolist()
        raise TypeError(type(o))
    with open(path, "w") as f:
        json.dump(obj, f, indent=1, default=conv)


def cutoff_decays(t, e, min_drop=15.0):
    """Find sharp ensemble cut-offs (sustained level for 0.4 s, then a fall of >= min_drop dB within 0.4 s)
    and fit the decay slope between -5 and -20 dB below the pre-cut-off level (RT60 = -60/slope).
    Works without a score, so renders and recordings are measured the same way. Returns a list of dicts."""
    dt = t[1] - t[0]
    n4 = int(0.4 / dt); out = []; i = n4; last = -10
    while i < len(e) - 3 * n4:
        pre = e[i - n4:i + 1]
        L0 = e[i]
        if L0 >= pre.max() - 1 and pre.min() >= L0 - 6 and e[i + n4] <= L0 - min_drop and t[i] - last > 1.0:
            seg = e[i:i + 3 * n4 * 2]
            a = np.where(seg <= L0 - 5)[0]; b = np.where(seg <= L0 - 20)[0]
            if len(a) and len(b) and b[0] > a[0] + 2 and b[0] * dt <= 1.5:
                sl = np.polyfit(np.arange(a[0], b[0]) * dt, seg[a[0]:b[0]], 1)[0]
                if not (-60 / 8.0 > sl):  # keep 0 < RT60 <= 8 s
                    i += 1; continue
                out.append({"t_s": round(float(t[i]), 2), "level_dB": round(float(L0), 1),
                            "t_to_minus20dB_s": round(float(b[0] * dt), 3), "RT60_est_s": round(float(-60 / sl), 2)})
                last = t[i]; i += 3 * n4; continue
        i += 1
    return out
