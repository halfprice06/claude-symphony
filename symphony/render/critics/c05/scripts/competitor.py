#!/usr/bin/env python3
"""critic 5: for a melody stem over bars a-b, the loudest other stem per bar (stems.py stem_bars.csv: loud_LUFS while
sounding, printed dyn). Usage: competitor.py stem_bars.csv 'Stem' a b"""
import sys, csv
from collections import defaultdict
L = defaultdict(dict)
for r in csv.DictReader(open(sys.argv[1])):
    if r['loud_LUFS'] not in ('', 'nan'):
        L[int(r['bar'])][r['stem']] = (float(r['loud_LUFS']), r['dyn'])
st, a, b = sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
out = []
for bar in range(a, b + 1):
    d = L[bar]
    if st not in d: continue
    o = max((v[0], k, v[1]) for k, v in d.items() if k != st and k != 'drums')
    out.append(f"{bar} {d[st][1]} {d[st][0]-o[0]:+.1f} vs {o[1]} ({o[2]})")
print(f'{st} {a}-{b}: ' + '; '.join(out))
