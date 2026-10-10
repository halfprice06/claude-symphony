#!/usr/bin/env python3
"""r05: balance inversions (tools/stems.py rule: a stem printed softer is > 3 dB louder, while sounding, than a stem
printed louder in the same bar), counted (a) as tools/stems.py does and (b) leaving out pairs where either stem has a
printed hairpin in that bar (stem_bars' 'dyn' is the printed dynamic at the bar's notes; a crescendo rendered as one
legitimately rises above it). Usage: inv_nohp.py stem_bars.csv notes.csv label"""
import sys, csv, re
from collections import defaultdict
sb, nf, lab = sys.argv[1:4]
D = ["ppp", "pp", "p", "mp", "mf", "f", "ff", "fff"]
def key(n): return re.sub(r"[^A-Za-z0-9 ]", "", n.split(":")[0]).strip() or "drums"
hp = set()
for r in csv.DictReader(open(nf, encoding="utf-8")):
    if r["hairpin"]: hp.add((key(r["midi_track"] or r["staff"]), int(r["bar"])))
pb = defaultdict(list)
for r in csv.DictReader(open(sb)):
    if r["loud_LUFS"] not in ("", "nan"): pb[int(r["bar"])].append(r)
a = b = 0
for bar, l in pb.items():
    for A in l:
        for B in l:
            if A["dyn"] in D and B["dyn"] in D and D.index(A["dyn"]) < D.index(B["dyn"]) and float(A["loud_LUFS"]) > float(B["loud_LUFS"]) + 3:
                a += 1
                if (A["stem"], bar) not in hp and (B["stem"], bar) not in hp: b += 1
print(f"{lab}: inversions {a}; without pairs in printed hairpins {b}")
