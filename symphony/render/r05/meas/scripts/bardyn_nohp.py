#!/usr/bin/env python3
"""r05: critic 2's bardyn Spearman (bar loudness vs loudest printed dynamic), over all bars and over the bars where no
more than 30 % of the notes are under a printed hairpin (in a crescendo bar the loudest printed dynamic is the start
of the ramp, not what is played). Usage: bardyn_nohp.py label bars.csv notes.csv"""
import csv, sys, numpy as np
from collections import defaultdict
from scipy.stats import spearmanr
DY = ['ppp', 'pp', 'p', 'mp', 'mf', 'f', 'ff', 'fff']
lab, bf, nf = sys.argv[1:4]
mx = {}; nh = defaultdict(int); nn = defaultdict(int)
for r in csv.DictReader(open(nf, encoding='utf-8')):
    b = int(r['bar']); nn[b] += 1; nh[b] += bool(r['hairpin'])
    if r['dyn'] in DY: mx[b] = max(mx.get(b, 0), DY.index(r['dyn']))
L = {int(x['bar']): float(x['loud_rel_I']) for x in csv.DictReader(open(bf)) if x['loud_rel_I'] not in ('', 'nan')}
ks = [k for k in L if k in mx]; k2 = [k for k in ks if nh[k] <= 0.3 * nn[k]]
r1 = spearmanr([mx[k] for k in ks], [L[k] for k in ks])[0]; r2 = spearmanr([mx[k] for k in k2], [L[k] for k in k2])[0]
print(f"{lab}: Spearman all bars {r1:.2f} (n={len(ks)}); bars without hairpins {r2:.2f} (n={len(k2)})")
