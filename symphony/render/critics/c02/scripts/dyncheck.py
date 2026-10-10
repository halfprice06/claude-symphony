import csv, numpy as np, sys
from collections import defaultdict
DY=['ppp','pp','p','mp','mf','f','ff','fff']
mx=defaultdict(int)
for r in csv.DictReader(open('/tmp/rcritic-02/notes.csv')):
    if r['dyn'] in DY: mx[int(r['bar'])]=max(mx[int(r['bar'])],DY.index(r['dyn']))
for lab,f in [('r02','/tmp/rcritic-02/r02/bars.csv'),('r01','/mnt/project-files/symphony/render/critics/c01/r01/bars.csv')]:
    b={int(x['bar']):float(x['loud_rel_I']) for x in csv.DictReader(open(f)) if x['loud_rel_I'] not in ('','nan')}
    by=defaultdict(list)
    for k,v in b.items(): by[mx[k]].append(v)
    med={DY[d]:round(float(np.median(v)),1) for d,v in sorted(by.items())}
    n={DY[d]:len(v) for d,v in sorted(by.items())}
    print(lab,'median bar loudness rel I by loudest printed (LilyPond) dynamic',med,n)
    fmed=np.median(by[5])
    bad=[(k,DY[mx[k]],round(v,1)) for k,v in sorted(b.items()) if mx[k]<=4 and v>fmed]
    print('  bars printed <=mf louder than median f bar (%.1f):'%fmed,len(bad),bad)
