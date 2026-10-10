#!/usr/bin/env python3
"""Third-octave LTAS of measured renders (tools/measure.py metrics.json) against mean(Brahms 1, Brahms 4) from
critics/c03/ltas_vs_refs.txt. Usage: ltas.py label=meas_dir [label=meas_dir ...]"""
import sys, json
ref = {}
for l in open("/mnt/project-files/symphony/render/critics/c03/ltas_vs_refs.txt").read().splitlines()[2:]:
    p = l.split(); ref[round(float(p[0]))] = (float(p[5]) + float(p[6])) / 2
cols = [a.split("=", 1) for a in sys.argv[1:]]
data = {}
for lab, d in cols:
    m = json.load(open(d + "/mix/metrics.json"))["spectrum"]
    data[lab] = {round(f): v for f, v in zip(m["third_octave_Hz"], m["third_octave_dB_rel_total"])}
print("Hz      " + "  ".join(f"{lab:>10s}" for lab, _ in cols) + "   (render minus mean Brahms 1/4, dB)")
for f in sorted(ref):
    if f < 39 or f > 10100: continue
    print(f"{f:6d}  " + "  ".join(f"{data[lab].get(f, float('nan')) - ref[f]:+10.1f}" for lab, _ in cols))
