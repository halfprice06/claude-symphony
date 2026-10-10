import csv, numpy as np, soundfile as sf, sys
from collections import defaultdict
rows=defaultdict(list)
for r in csv.DictReader(open('/tmp/rcritic-02/notes.csv')):
    rows[r['staff']].append((float(r['t_on_s']), float(r['t_on_s'])+float(r['notated_s'])))
for arg in sys.argv[1:]:
    staff,wav=arg.split('=')
    x,sr=sf.read(wav,dtype='float32'); m=x.mean(1); h=int(0.005*sr); k=len(m)//h
    E=10*np.log10((m[:k*h].reshape(k,h)**2).mean(1)+1e-14)
    ev=sorted(rows[staff]); ons=np.array([a for a,b in ev])
    t20=[];t40=[];short=[]
    for a,b in ev:
        nxt=ons[ons>b-1e-3]
        if len(nxt) and nxt.min()<b+1.2: continue
        if any((a2<b and b2>b) for a2,b2 in ev if a2!=a): continue
        i=int(b/0.005); lvl=E[i-6:i-1].mean()
        if lvl<E.max()-50: continue
        after=E[i:i+int(1.2/0.005)]
        j20=np.nonzero(after<lvl-20)[0]; j40=np.nonzero(after<lvl-40)[0]
        if len(j20): t20.append(j20[0]*0.005)
        if len(j40): t40.append(j40[0]*0.005)
    c=float(np.dot(x[:,0],x[:,1])/np.sqrt(np.dot(x[:,0],x[:,0])*np.dot(x[:,1],x[:,1])))
    print('%-14s %-40s n %3d  after last note-off: -20 dB in %.2f s, -40 dB in %s s; L/R corr %.2f'%(staff,wav.split('/')[-2]+'/'+wav.split('/')[-1],len(t20),np.median(t20) if t20 else np.nan,('%.2f'%np.median(t40)) if t40 else ' >1.2',c))
