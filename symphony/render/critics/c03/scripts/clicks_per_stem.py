#!/usr/bin/env python3
"""critic 1's clicks.py criterion (HF >8 kHz 50 ms block peak > 12x the median of 11 neighbouring blocks' HF rms, peak > 1e-3)
applied to each wet stem, plus the mix of all stems; prints candidate counts and times per stem. Usage: clicks_per_stem.py stems_dir"""
import sys, glob, os, numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt
from scipy.ndimage import median_filter
sos = butter(4, 8000, 'highpass', fs=48000, output='sos')
def cands(x):
    h = sosfilt(sos, x); w = 2400; n = len(h) // w
    hb = h[:n*w].reshape(n, w); rms = np.sqrt((hb**2).mean(1)) + 1e-9; pk = np.abs(hb).max(1)
    ref = median_filter(rms, 11) + 1e-9
    return np.where((pk / ref > 12) & (pk > 1e-3))[0] * 0.05
for p in sorted(glob.glob(os.path.join(sys.argv[1], '*.wav'))):
    if p.endswith('_syn.wav'): continue
    x, sr = sf.read(p, dtype='float64', always_2d=True)
    c = cands(x.mean(1))
    if len(c): print(os.path.basename(p), len(c), [round(t, 2) for t in c[:12]])
