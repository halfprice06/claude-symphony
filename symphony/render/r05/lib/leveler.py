"""r04: slow top-only leveler for the master (critic 3: movement II short-term max +10 LU and p95 +7 LU over the
integrated level, references +5 to +8 and +3.4 to +3.9). Riding the master fader down on climaxes only: where the 3 s
short-term loudness exceeds integrated + threshold_LU, the gain falls by (excess) * (1 - 1/ratio); the gain curve is
smoothed over smooth_s so it moves like a hand on a fader. Everything below the threshold is untouched (no upward
compression, no change to soft passages). EBU R128 short-term loudness: https://tech.ebu.ch/publications/tech3342"""
import numpy as np
import rtk


def gain_curve(x, sr, I, threshold_LU=6.0, ratio=2.0, smooth_s=3.0, max_cut_dB=3.0):
    tS, S = rtk.loudness_series(x, sr, 3.0, 0.1)
    ex = np.maximum(0.0, S - (I + threshold_LU))
    g = -np.minimum(ex * (1 - 1 / ratio), max_cut_dB)
    k = max(1, int(smooth_s / 0.1))
    # minimum filter first (so the cut is in place before the peak), then a moving average
    from scipy.ndimage import minimum_filter1d
    g = minimum_filter1d(g, k)
    g = np.convolve(np.pad(g, (k // 2, k - k // 2 - 1), mode="edge"), np.ones(k) / k, mode="valid")
    return tS, g


def apply(x, sr, I, **kw):
    tS, g = gain_curve(x, sr, I, **kw)
    t = np.arange(len(x)) / sr
    gl = 10 ** (np.interp(t, tS, g) / 20)
    return x * gl[:, None], float(g.min())
