#!/usr/bin/env python3
"""critic 5: balance inversions (stem printed softer but > 3 dB louder than a stem printed louder in the same bar,
levels while sounding, as tools/stems.py counts them) broken down by the offending (too loud) stem.
Usage: inv_by_stem.py stem_bars.csv [label]"""
import sys, csv
from collections import defaultdict, Counter
O = ['ppp', 'pp', 'p', 'mp', 'mf', 'f', 'ff', 'fff']
L = defaultdict(dict)
for r in csv.DictReader(open(sys.argv[1])):
    if r['loud_LUFS'] not in ('', 'nan') and r['dyn'] in O and r['stem'] != 'drums':
        L[int(r['bar'])][r['stem']] = (float(r['loud_LUFS']), O.index(r['dyn']))
c = Counter(); tot = 0
for b, d in L.items():
    for s, (l, k) in d.items():
        for s2, (l2, k2) in d.items():
            if k < k2 and l > l2 + 3:
                c[s] += 1; tot += 1
print(f"{sys.argv[2] if len(sys.argv) > 2 else ''} inversions {tot}; by offending stem: " + ', '.join(f'{k} {v}' for k, v in c.most_common(10)))
