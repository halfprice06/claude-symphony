#!/usr/bin/env python3
"""r05 (critic 4, plan 5): bus EQ tuning against the mean third-octave LTAS of the four Brahms references (1 and 4,
movements I and II). Usage: eqtune4.py 'OLD_EQ_JSON' 'NEW_EQ_JSON' premaster.wav [...]
The premasters already carry OLD_EQ; NEW_EQ's response divided by OLD_EQ's is applied to show the result."""
import sys, os, json, numpy as np, soundfile as sf
R = "/mnt/project-files/symphony/render"
sys.path.insert(0, R + "/r05/lib"); sys.path.insert(0, R + "/tools")
import rtk, busq
refs = [R + "/critics/c00/ref_brahms1_i_musopen", R + "/critics/c00/ref_brahms4_i_musopen",
        R + "/critics/c04/ref_brahms1_ii_musopen", R + "/critics/c04/ref_brahms4_ii_musopen"]
F = None; acc = []; shares = []
for d in refs:
    m = json.load(open(d + "/metrics.json"))["spectrum"]
    F = m["third_octave_Hz"]; acc.append(m["third_octave_dB_rel_total"]); shares.append(m["band_shares_dB"])
ref = np.mean(acc, 0)
print("refs band shares <100 / 2-6k:", [(round(s["20-100Hz"], 1), round(s["2000-6000Hz"], 1)) for s in shares])
old, new = json.loads(sys.argv[1]), json.loads(sys.argv[2])
sel = [62.5, 78.7, 99.2, 250, 315, 630, 793.7, 2519.8, 3174.8, 4000, 6349.6, 8000, 10079.4]
for w in sys.argv[3:]:
    x, sr = sf.read(w, always_2d=True); m = x.mean(1)
    f, P = rtk.psd(m, sr); ff = np.maximum(f, 1e-3)
    for lab, PP in (("old", P), ("new", P * busq.power_response(new, sr, ff) / busq.power_response(old, sr, ff))):
        b = rtk.third_octave(f, PP); bs = rtk.band_shares(f, PP)
        d = {fc: b[i] - ref[i] for i, fc in enumerate(F) if i < len(b)}
        print(w.split("/")[-2], lab, "<100 %.1f 2-6k %.1f |" % (bs["20-100Hz"], bs["2000-6000Hz"]),
              " ".join("%d:%+.1f" % (fc, d[min(d, key=lambda z: abs(z - fc))]) for fc in sel))
