#!/usr/bin/env python3
"""critic 6: per bar, the loudest printed dynamic (notes.csv) and each render's bar loudness rel. I (measure.py bars.csv);
residual = bar loudness minus the median of bars with the same printed dynamic in that render. Lists the bars whose
residual differs most between two renders. Usage: bardiff.py notes.csv A_bars.csv B_bars.csv [n]"""
import sys, csv, numpy as np
from collections import defaultdict
DO = ["ppp", "pp", "p", "mp", "mf", "f", "ff", "fff"]
notes, A, B = sys.argv[1:4]; N = int(sys.argv[4]) if len(sys.argv) > 4 else 15
pd = defaultdict(lambda: -1); hp = defaultdict(bool)
for r in csv.DictReader(open(notes)):
    if r['dyn'] in DO:
        b = int(r['bar']); pd[b] = max(pd[b], DO.index(r['dyn'])); hp[b] |= bool(r['hairpin'])
def load(p):
    return {int(r['bar']): float(r['loud_rel_I']) for r in csv.DictReader(open(p)) if r['loud_rel_I'] not in ('', 'nan')}
a, b = load(A), load(B)
def resid(d):
    cls = defaultdict(list)
    for k, v in d.items():
        if pd[k] >= 0: cls[pd[k]].append(v)
    med = {c: np.median(v) for c, v in cls.items()}
    return {k: v - med[pd[k]] for k, v in d.items() if pd[k] >= 0}, med
ra, ma = resid(a); rb, mb = resid(b)
print('median rel I per printed dyn  A:', {DO[c]: round(v, 1) for c, v in sorted(ma.items())})
print('                              B:', {DO[c]: round(v, 1) for c, v in sorted(mb.items())})
ks = sorted(set(ra) & set(rb), key=lambda k: -abs(rb[k] - ra[k]))
print('bar | printed | hairpin | A rel I / resid | B rel I / resid | B-A resid')
for k in ks[:N]:
    print(f'{k} | {DO[pd[k]]} | {"y" if hp[k] else ""} | {a[k]:+.1f} / {ra[k]:+.1f} | {b[k]:+.1f} / {rb[k]:+.1f} | {rb[k]-ra[k]:+.1f}')
