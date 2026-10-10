#!/usr/bin/env python3
"""Blend per stem (wet stems): share of energy > 6 kHz and in the 10-16 kHz band (dB re stem total), spectral centroid,
L/R correlation, and reverberant share: energy in the 0.15-0.6 s after each sharp stem offset relative to the 0.1 s before
(median over offsets, a direct-to-reverberant proxy). Usage: blendstem.py stems_dir"""
import sys, glob, os, numpy as np, soundfile as sf
from scipy.signal import welch
for p in sorted(glob.glob(os.path.join(sys.argv[1], '*.wav'))):
    if p.endswith('_syn.wav'): continue
    x, sr = sf.read(p, dtype='float64', always_2d=True)
    m = x.mean(1)
    if np.abs(m).max() < 1e-5: continue
    f, P = welch(m, fs=sr, nperseg=8192)
    tot = P.sum(); hf = P[f > 6000].sum(); b = P[(f > 10000) & (f < 16000)].sum()
    cen = (f * P).sum() / tot
    corr = np.corrcoef(x[:, 0], x[:, 1])[0, 1]
    # offsets: 50 ms rms envelope drops > 15 dB within 150 ms
    w = int(0.05 * sr); n = len(m) // w; e = 10 * np.log10((m[:n*w].reshape(n, w)**2).mean(1) + 1e-20)
    rv = []
    for i in range(2, n - 13):
        if e[i] > e.max() - 40 and e[i] - e[i + 3] > 15 and e[i - 1] - e[i] < 3:
            rv.append(10 * np.log10((10 ** (e[i + 3:i + 12] / 10)).mean() / (10 ** (e[i - 2:i + 1] / 10)).mean()))
    print(f"{os.path.basename(p)[:-4]:16s} >6k {10*np.log10(hf/tot):6.1f} dB | 10-16k {10*np.log10(b/tot):6.1f} dB | centroid {cen:6.0f} Hz | L/R corr {corr:.2f} | tail after offsets {np.median(rv) if rv else float('nan'):6.1f} dB (n {len(rv)})")
