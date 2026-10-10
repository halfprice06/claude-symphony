#!/usr/bin/env python3
"""For given times, which stem carries the high-frequency transient: HF (>6 kHz) energy in 2 ms around t relative to the
median of the 80 ms around it, per stem. Usage: clickstem.py stems_dir t1 t2 ..."""
import sys, glob, os, numpy as np, soundfile as sf
from scipy.signal import butter, sosfiltfilt
d = sys.argv[1]; T = [float(t) for t in sys.argv[2:]]
res = {}
for p in sorted(glob.glob(os.path.join(d, "*.wav"))):
    if p.endswith("_dry.wav"): continue
    x, sr = sf.read(p, dtype="float64", always_2d=True); m = x.mean(1)
    sos = butter(4, 6000, "highpass", fs=sr, output="sos")
    out = []
    for t in T:
        a = int((t - 0.06) * sr); seg = sosfiltfilt(sos, m[max(a, 0):a + int(0.12 * sr)]); w = int(0.002 * sr)
        e = (seg[:len(seg) // w * w].reshape(-1, w) ** 2).mean(1) + 1e-20
        out.append((10 * np.log10(e.max() / np.median(e)), 10 * np.log10(e.max())))
    res[os.path.basename(p)[:-4]] = out
for i, t in enumerate(T):
    best = sorted(res.items(), key=lambda z: -z[1][i][0])[:3]
    print(t, "; ".join(f"{s} jump {v[i][0]:.0f} dB at {v[i][1]:.0f} dB" for s, v in best))
