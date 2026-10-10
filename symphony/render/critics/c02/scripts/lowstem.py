#!/usr/bin/env python3
"""Energy below 100 Hz and in 40-80 Hz per stem (dB re the full mix's total energy), to find where the low end of a mix
comes from. Usage: lowstem.py stems_dir [stems_dir2 ...]"""
import sys, glob, os, numpy as np, soundfile as sf
for d in sys.argv[1:]:
    E = {}
    for p in sorted(glob.glob(os.path.join(d, "*.wav"))):
        if p.endswith("_dry.wav"): continue
        x, sr = sf.read(p, dtype="float32", always_2d=True); m = x.mean(1).astype(np.float64)
        n = 1 << 16; k = len(m) // n
        P = np.zeros(n // 2 + 1)
        for i in range(k): P += np.abs(np.fft.rfft(m[i * n:(i + 1) * n] * np.hanning(n))) ** 2
        f = np.fft.rfftfreq(n, 1 / sr)
        E[os.path.basename(p)[:-4]] = (P.sum(), P[f < 100].sum(), P[(f >= 40) & (f < 80)].sum(), P[(f>=100)&(f<250)].sum())
    tot = sum(v[0] for v in E.values())
    print(d, "mix <100 Hz share %.1f dB" % (10*np.log10(sum(v[1] for v in E.values())/tot)))
    for s, v in sorted(E.items(), key=lambda z: -z[1][1])[:8]:
        print("  %-15s <100 Hz %.1f dB, 40-80 Hz %.1f dB, 100-250 %.1f dB (re mix total); stem share of its own energy <100 Hz %.1f dB" % (s, 10*np.log10(v[1]/tot), 10*np.log10(v[2]/tot), 10*np.log10(v[3]/tot), 10*np.log10(v[1]/v[0])))
