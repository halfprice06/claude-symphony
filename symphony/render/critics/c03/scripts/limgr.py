#!/usr/bin/env python3
"""Limiter gain reduction: compare premaster x gain with the master (50 ms blocks, RMS). Usage: limgr.py mix_prem.wav master.wav gain_dB"""
import sys, numpy as np, soundfile as sf
a, sr = sf.read(sys.argv[1], dtype='float64', always_2d=True); b, _ = sf.read(sys.argv[2], dtype='float64', always_2d=True)
a *= 10 ** (float(sys.argv[3]) / 20); n = min(len(a), len(b)); w = int(0.05 * sr); k = n // w
ra = np.sqrt((a[:k*w]**2).reshape(k, w, 2).mean((1, 2))) + 1e-12; rb = np.sqrt((b[:k*w]**2).reshape(k, w, 2).mean((1, 2))) + 1e-12
gr = 20 * np.log10(rb / ra); gr = gr[ra > 1e-4]
print(f"blocks with GR > 0.5 dB: {(gr < -0.5).sum()} ({(gr < -0.5).mean()*100:.2f} %), > 1 dB: {(gr < -1).sum()}, > 2 dB: {(gr < -2).sum()}; max GR {-gr.min():.1f} dB")
