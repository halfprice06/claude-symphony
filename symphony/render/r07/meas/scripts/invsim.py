import csv, sys, re
from collections import defaultdict
O=['ppp','pp','p','mp','mf','f','ff','fff']
def load(p, notes):
    hp=defaultdict(set)
    for r in csv.DictReader(open(notes)):
        if r['hairpin']: hp[int(r['bar'])].add(re.sub(r"[^A-Za-z0-9 ]","",r['staff'].split(':')[0]).strip())
    L=defaultdict(dict)
    for r in csv.DictReader(open(p)):
        if r['loud_LUFS'] not in ('','nan') and r['dyn'] in O and r['stem']!='drums':
            L[int(r['bar'])][r['stem']]=(float(r['loud_LUFS']),O.index(r['dyn']))
    return L,hp
def count(L,hp,off):
    n=nh=0
    for b,d in L.items():
        dd={s:(l+off.get((s,O[k]),0)+off.get((s,'*'),0),k) for s,(l,k) in d.items()}
        for a,(la,da) in dd.items():
            for v,(lv,dv) in dd.items():
                if da<dv and la>lv+3:
                    n+=1
                    if a not in hp[b] and v not in hp[b]: nh+=1
    return n,nh
