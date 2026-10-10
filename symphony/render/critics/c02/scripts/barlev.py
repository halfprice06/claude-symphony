#!/usr/bin/env python3
"""K-weighted level of every stem WAV over each whole bar (not only while sounding). Usage: barlev.py stems_dir bars.csv out.csv"""
import csv, glob, os, sys, numpy as np, soundfile as sf
sys.path.insert(0, "/mnt/project-files/symphony/render/tools"); import rtk
d, bf, out = sys.argv[1:4]
bars = [(int(b["bar"]), float(b["t_start"]), float(b["t_end"])) for b in csv.DictReader(open(bf))]
w = csv.writer(open(out, "w", newline="")); w.writerow(["stem", "bar", "LUFS"])
for p in sorted(glob.glob(os.path.join(d, "*.wav"))):
    st = os.path.basename(p)[:-4].replace("_", " ")
    if st.endswith(" dry"): continue
    x, sr = sf.read(p, dtype="float64", always_2d=True); e = (rtk.k_weight(x, sr) ** 2).sum(1)
    for b, a, z in bars:
        seg = e[int(a * sr):int(z * sr)]
        w.writerow([st, b, round(10 * np.log10(seg.mean() + 1e-20) - 0.691, 2) if len(seg) else ""])
