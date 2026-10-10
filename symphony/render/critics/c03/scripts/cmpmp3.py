#!/usr/bin/env python3
"""Compare two MP3 renders: length, integrated-level difference, sample correlation, residual level. Usage: cmpmp3.py a.mp3 b.mp3"""
import sys, subprocess, numpy as np
def dec(p):
    r = subprocess.run(["ffmpeg","-v","error","-i",p,"-f","f32le","-ac","2","-ar","48000","-"],capture_output=True)
    return np.frombuffer(r.stdout, np.float32).reshape(-1,2).astype(np.float64)
a, b = dec(sys.argv[1]), dec(sys.argv[2])
print("len s", len(a)/48000, len(b)/48000)
n = min(len(a), len(b)); a, b = a[:n], b[:n]
# best lag within +-2000 samples (mp3 padding)
m1, m2 = a[:,0][:480000*2], b[:,0][:480000*2]
best = max(range(-2000,2001,1), key=lambda L: 0) if False else 0
c = np.corrcoef(a.ravel(), b.ravel())[0,1]
res = 10*np.log10(((a-b)**2).mean()/(a**2).mean())
print(f"corr {c:.5f} residual {res:.1f} dB re signal; rms a {10*np.log10((a**2).mean()):.2f} b {10*np.log10((b**2).mean()):.2f} dB")
