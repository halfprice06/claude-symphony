#!/usr/bin/env python3
"""Bar loudness (measure.py bars.csv, loud_rel_I) against the loudest PRINTED dynamic in the bar (notes.csv with correct
bars, see fixbars.py). Prints median per dynamic, steps, Spearman rho (bar loudness vs printed dynamic index), and
bars printed <= mf that are louder than the median f bar.  Usage: bardyn.py label bars.csv notes.csv [label bars notes ...]"""
import csv, sys, numpy as np
from collections import defaultdict
from scipy.stats import spearmanr
DY = ['ppp', 'pp', 'p', 'mp', 'mf', 'f', 'ff', 'fff']
a = sys.argv[1:]
for i in range(0, len(a), 3):
    lab, bf, nf = a[i:i + 3]
    mx = {}
    for r in csv.DictReader(open(nf, encoding='utf-8')):
        if r['dyn'] in DY:
            b = int(r['bar']); mx[b] = max(mx.get(b, 0), DY.index(r['dyn']))
    b = {int(x['bar']): float(x['loud_rel_I']) for x in csv.DictReader(open(bf)) if x['loud_rel_I'] not in ('', 'nan')}
    ks = [k for k in b if k in mx]
    rho = spearmanr([mx[k] for k in ks], [b[k] for k in ks])[0]
    by = defaultdict(list)
    for k in ks: by[mx[k]].append(b[k])
    med = {DY[d]: round(float(np.median(v)), 1) for d, v in sorted(by.items())}
    n = {DY[d]: len(v) for d, v in sorted(by.items())}
    ds = sorted(by); steps = {f"{DY[x]}->{DY[y]}": round(float(np.median(by[y]) - np.median(by[x])), 1) for x, y in zip(ds, ds[1:])}
    print(f"{lab}: Spearman rho bar loudness vs printed dyn = {rho:.2f} (n={len(ks)})")
    print(f"  median rel I by loudest printed dyn: {med}  n={n}")
    print(f"  steps: {steps}")
    if 5 in by:
        fmed = np.median(by[5]); bad = [(k, DY[mx[k]], round(b[k], 1)) for k in sorted(ks) if mx[k] <= 4 and b[k] > fmed]
        print(f"  bars printed <= mf louder than the median f bar ({fmed:.1f}): {len(bad)} {bad[:12]}")
