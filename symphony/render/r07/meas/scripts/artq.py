#!/usr/bin/env python3
"""r07: quick articulation metrics of single stem WAVs (tools/stems.py note_metrics, same definitions as stemcmp):
detached / staccato / accent audible ratio, slurred and detached boundary dips.
Usage: artq.py NOTES.csv STEM_NAME WAV [WAV ...]"""
import sys, os, csv, re
import numpy as np
R = "/mnt/project-files/symphony/render"
sys.path.insert(0, R + "/tools")
import stems, rtk
nf, name = sys.argv[1], sys.argv[2]
rows = list(csv.DictReader(open(nf)))
for r in rows:
    for k in ("t_on_s", "notated_s"):
        r[k] = float(r[k])
    r["t_off_s"] = float(r["t_off_s"]) if r["t_off_s"] else None
    r["bar"] = int(r["bar"]); r["midi_vel"] = int(r["midi_vel"]) if r["midi_vel"] else ""
rs = [r for r in rows if (stems.key(r["midi_track"]) if r["midi_track"] else r["staff"]) == name]
for w in sys.argv[3:]:
    x = rtk.decode(w)
    te, ee = rtk.env_db(x, rtk.SR, 0.02, 0.01)
    nm, dips = stems.note_metrics(te, ee, rs)
    out = []
    for c in ("detached", "staccato", "accent", "legato"):
        v = [d["audible_ratio"] for d in nm if d["cls"] == c and "audible_ratio" in d]
        if v:
            out.append(f"{c} {np.median(v):.2f} (n {len(v)})")
    for s in (True, False):
        v = [d["dip_dB"] for d in dips if d["slurred"] == s]
        if v:
            out.append(f"{'slur' if s else 'det'} dip {np.median(v):+.1f}")
    print(os.path.basename(w), "|", " ; ".join(out))
