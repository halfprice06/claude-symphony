#!/usr/bin/env python3
"""critic 7: the same two waveform tests as clickinspect.py, on raw sample files (per-note WAVs or source AIFFs):
the clicks2 'isolated HF spike' count, and for each spike the dry second-difference outlier ratio and HF-envelope
period. If the raw recording shows the same spikes at the note's fundamental period, the premaster detections are the
instrument's own pulse waveform, not a render splice.
Usage: samplepulse.py FILE [FILE ...]"""
import sys
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt
from scipy.ndimage import median_filter
for p in sys.argv[1:]:
    x, sr = sf.read(p, dtype='float32', always_2d=True); m = x.mean(1).astype(np.float64)
    h = sosfilt(butter(4, 6000, 'highpass', fs=sr, output='sos'), m)
    w = int(0.001 * sr); n = len(h) // w
    e = (h[:n * w].reshape(n, w) ** 2).mean(1) + 1e-16; ref = median_filter(e, 41)
    full = (m[:n * w].reshape(n, w) ** 2).mean(1); fullref = np.convolve(full, np.ones(41) / 41, 'same') + 1e-16
    jump = 10 * np.log10(e / ref)
    cand = np.nonzero((jump > 15) & (10 * np.log10(e) > -95) & (10 * np.log10(fullref) > -80))[0]
    iso = [c for c in cand if c + 4 < n and jump[c + 4] < 6]
    ev = []
    for c in iso:
        if not ev or c - ev[-1] > 20:
            ev.append(c)
    ratios = []
    for c in ev[:40]:
        i = c * w; a, z = max(0, i - int(0.02 * sr)), min(len(m), i + int(0.02 * sr))
        d2 = np.abs(np.diff(m[a:z], 2))
        k0, k1 = max(0, i - a - int(0.003 * sr)), i - a + int(0.004 * sr)
        ratios.append(d2[k0:k1].max() / (np.median(d2) + 1e-12))
    # whole-file second-difference outlier ratio on the loudest 1 s (a reference for 'normal' for this sound)
    cs = np.concatenate([[0], np.cumsum(m ** 2)]); j = int(np.argmax(cs[sr:] - cs[:-sr])) + sr // 2
    seg = m[max(0, j - sr // 2):j + sr // 2]
    d2s = np.abs(np.diff(seg, 2)); blk = int(0.04 * sr)
    rs = [d2s[q:q + blk].max() / (np.median(d2s[q:q + blk]) + 1e-12) for q in range(0, len(d2s) - blk, blk)]
    print(f"{p.split('/')[-1]}: dur {len(m)/sr:.1f}s spikes {len(ev)}; spike 2nd-diff ratio median "
          f"{np.median(ratios) if ratios else float('nan'):.0f}x; loudest-second 40 ms blocks max/median ratio median {np.median(rs):.0f}x")
