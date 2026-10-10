import csv, numpy as np, soundfile as sf, sys
from collections import defaultdict
stem, wav = sys.argv[1], sys.argv[2]
rows=[r for r in csv.DictReader(open('/tmp/rcritic-02/notes.csv')) if r['staff']==stem]
on=np.array(sorted(float(r['t_on_s']) for r in rows))
x,sr=sf.read(wav,dtype='float32'); m=x.mean(1); h=int(0.01*sr); k=len(m)//h
E=10*np.log10((m[:k*h].reshape(k,h)**2).mean(1)+1e-14)
def cls(r):
    a=r['arts']
    if 'staccato' in a: return 'staccato'
    if 'accent' in a or 'marcato' in a: return 'accent'
    if 'tremolo' in a: return 'tremolo'
    if r['tech']=='pizz': return 'pizz'
    if r['slur'] in ('start','in'): return 'slurred'
    return 'detached'
res=defaultdict(list)
for r in rows:
    t0=float(r['t_on_s']); L=float(r['notated_s'])
    if L<0.45 or L>1.2: continue
    later=on[(on>t0+0.02)&(on<t0+L-0.02)]
    if len(later): continue
    i0=int(t0/0.01); seg=E[i0:i0+int(L/0.01)+1]
    pk=seg[:max(3,int(0.3/0.01))].max()
    res[cls(r)].append((seg[int(0.5*L/0.01)]-pk, seg[min(len(seg)-1,int(0.75*L/0.01))]-pk, L))
for c,v in res.items():
    v=np.array(v); print(stem, c, 'n',len(v),'median L %.2f'%np.median(v[:,2]),'level at 50%% %.1f, at 75%% %.1f dB re peak'%(np.median(v[:,0]),np.median(v[:,1])))
