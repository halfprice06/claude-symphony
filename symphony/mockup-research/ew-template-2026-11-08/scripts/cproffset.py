import sys, os, bisect
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cprlib import read, part_abs
P = read(sys.argv[1])['parts']
ref = [p for p in P if p['start'] == 0 and p['off'] == 0 and len(p['notes']) > 40]
refon = sorted(n[0] for p in ref for n in p['notes'])
print('reference parts', [p['name'] for p in ref])
for p in P:
    if p in ref or not p['notes']: continue
    res = []
    for mode in ('minus', 'plus', 'none'):
        on = [part_abs(p, n[0], mode) for n in p['notes']]
        hit = 0
        for x in on:
            k = bisect.bisect_left(refon, x - 15)
            if k < len(refon) and refon[k] <= x + 15: hit += 1
        res.append(f'{mode} {hit/len(on)*100:3.0f}%')
    print(f"{p['name'][:26]:26s} start {p['start']:7.1f} off {p['off']:7.1f} | " + '  '.join(res))
