import csv, json, numpy as np, sys
from collections import defaultdict
bars_csv=sys.argv[1]; cfg=json.load(open('/mnt/project-files/symphony/render/r02/config.json'))
rows=list(csv.DictReader(open(bars_csv)))
L=defaultdict(dict); D=defaultdict(dict)
for r in rows:
    if r['loud_LUFS'] in ('','nan'): continue
    L[int(r['bar'])][r['stem']]=float(r['loud_LUFS']); D[int(r['bar'])][r['stem']]=r['dyn']
# melody-lift bars per staff (8 bars max from start)
lift=defaultdict(set)
for st,b0,_,db in cfg['melodies']['list']:
    for b in range(b0,b0+8): lift[st].add(b)
exclude_all=set()
for st,s in lift.items(): exclude_all|=s
strings=['Violins I','Violins II','Violas','Violoncellos']
DY=['pp','p','mp','mf','f','ff']
res=defaultdict(lambda: defaultdict(list))
for b in L:
    if b in exclude_all: continue
    for st,v in L[b].items():
        d=D[b][st]
        if d not in DY: continue
        refs=[L[b][s] for s in strings if s in L[b] and s!=st and D[b].get(s)==d]
        if not refs: continue
        res[st][d].append(v-np.median(refs))
print('stem | level minus median of other string stems at the same printed dynamic (bars without any melody lift) pp p mp mf f ff | spread | n')
sp=[]
for st in sorted(res):
    med=[np.median(res[st][d]) if len(res[st][d])>=2 else np.nan for d in DY]
    n=[len(res[st][d]) for d in DY]
    v=[x for x in med if not np.isnan(x)]
    s=max(v)-min(v) if len(v)>=2 else np.nan
    if not np.isnan(s): sp.append(s)
    print('%-14s'%st,' '.join('%+5.1f'%x for x in med),'| %.1f |'%s, n)
print('median spread %.1f'%np.median(sp))
