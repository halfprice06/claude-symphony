#!/usr/bin/env python3
"""Which stem sounds after the final note-off? Usage: tailstem.py stems_dir t0_s
Prints each stem's level (dB re mix level at t0-0.5..t0) in windows after t0."""
import sys, glob, os, numpy as np, soundfile as sf
d, t0 = sys.argv[1], float(sys.argv[2])
W = [(-0.5, 0), (0.3, 0.6), (0.8, 1.3), (1.5, 2.5), (2.5, 4.0)]
res = {}; mix = None
for p in sorted(glob.glob(os.path.join(d, "*.wav"))):
    if p.endswith("_syn.wav"): continue
    x, sr = sf.read(p, dtype="float64", always_2d=True)
    def lv(a, b):
        i, j = int((t0 + a) * sr), int((t0 + b) * sr); s = x[i:j]
        return 10 * np.log10((s ** 2).mean() + 1e-20) if len(s) else -200
    res[os.path.basename(p)[:-4]] = [lv(a, b) for a, b in W]
ref = 10 * np.log10(sum(10 ** (v[0] / 10) for v in res.values()))
print("stem | " + " | ".join(f"{a:+.1f}..{b:+.1f}s" for a, b in W) + "  (dB re all stems in -0.5..0 s)")
for k, v in sorted(res.items(), key=lambda z: -z[1][3]):
    if max(v) - ref > -60: print(k, "|", " | ".join(f"{x - ref:6.1f}" for x in v))
