#!/usr/bin/env python3
"""r04: level of the recorded timpani roll per MIDI pitch (VPO timpani-roll.sfz through sfzplay, same channel env as
config), K-weighted, 1.0-3.0 s into a 4 s roll at velocity 100. Prints a JSON table {pitch: trim dB} (median = 0)
for config articulation.timp_roll_pitch_trim_dB, so rolls on different drums start at the same level for the same
printed dynamic (the samples differ by several dB from drum to drum).
Usage: calib_timp_roll.py [config.json] [lo hi]"""
import sys, os, json, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "lib"))
import sfzplay, rtk
from stem import env_for
cfg = json.load(open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "config.json")))
lo, hi = (int(sys.argv[2]), int(sys.argv[3])) if len(sys.argv) > 3 else (36, 62)
spec = cfg["stems"]["Timpani"]["sfz"]["channels"]["1"]
inst = sfzplay.Sfz(os.path.normpath(os.path.join(HERE, spec["file"])))
sr = cfg["sample_rate"]; lev = {}
for p in range(lo, hi + 1):
    if not inst.select(p, 100):
        continue
    inst.rr = {}
    y = sfzplay.render(inst, [(0.0, 4.0, p, 100, env_for(spec.get("env"), 4.0))], sr, 5.0, seed=7)
    k = rtk.k_weight(y.astype(np.float64), sr)
    lev[p] = 10 * np.log10((k[int(1.0 * sr):int(3.0 * sr)] ** 2).sum(1).mean() + 1e-20)
med = float(np.median(list(lev.values())))
print(json.dumps({str(p): round(med - v, 1) for p, v in lev.items()}))
