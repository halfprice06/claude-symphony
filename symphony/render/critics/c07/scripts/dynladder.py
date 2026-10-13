#!/usr/bin/env python3
"""critic 7: per-stem level by printed dynamic (stems.py stems_summary.json, LUFS while sounding, median per dynamic)
side by side for several renders, plus each stem's step mf->f and f->ff (dB), and its level minus the string median at
the same printed dynamic. Usage: dynladder.py LABEL=stems_summary.json [...]"""
import sys, json
import numpy as np
D = ["pp", "p", "mp", "mf", "f", "ff"]
STR = ["Violins I", "Violins II", "Violas", "Violoncellos", "Double basses"]
runs = []
for a in sys.argv[1:]:
    lab, p = a.split("=", 1)
    st = {s["stem"]: s for s in json.load(open(p))["stems"]}
    runs.append((lab, st))
names = sorted(set().union(*[set(r[1]) for r in runs]))
print("stem | " + " | ".join(f"{lab}: {' '.join(D)} (vs string median)  mf>f f>ff" for lab, _ in runs))
for s in names:
    if s == "drums":
        continue
    cells = []
    for lab, st in runs:
        if s not in st:
            cells.append("-"); continue
        lv = st[s].get("level_by_dynamic_LUFS", {})
        vals, rel = [], []
        for d in D:
            v = lv.get(d, {}).get("median") if lv.get(d, {}).get("n", 0) >= 2 else None
            sm = [st[q]["level_by_dynamic_LUFS"].get(d, {}).get("median") for q in STR if q in st and st[q]["level_by_dynamic_LUFS"].get(d, {}).get("n", 0) >= 2]
            sm = [z for z in sm if z is not None]
            vals.append(f"{v:.1f}" if v is not None else ".")
            rel.append(f"{v - np.median(sm):+.1f}" if v is not None and sm else ".")
        g = lambda d: lv.get(d, {}).get("median") if lv.get(d, {}).get("n", 0) >= 2 else None
        s1 = f"{g('f') - g('mf'):+.1f}" if g('f') is not None and g('mf') is not None else "."
        s2 = f"{g('ff') - g('f'):+.1f}" if g('ff') is not None and g('f') is not None else "."
        cells.append(f"{' '.join(vals)} ({' '.join(rel)})  {s1} {s2}")
    print(f"{s} | " + " | ".join(cells))
