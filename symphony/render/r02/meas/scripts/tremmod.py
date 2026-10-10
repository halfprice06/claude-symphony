"""Envelope modulation of tremolo notes (critic 1, section 7): energy of the amplitude envelope in 8-24 Hz minus
1-6 Hz (dB), median over :32 tremolo notes >= 0.5 s, against unmarked sustained notes >= 0.5 s of the same stem.
usage: tremmod.py notes.csv STEMDIR"""
import csv, sys, re, os, numpy as np, soundfile as sf
from collections import defaultdict
rows=list(csv.DictReader(open(sys.argv[1])))
def key(n): return re.sub(r"[^A-Za-z0-9 ]","",n.split(":")[0]).strip()
def mod(m,sr,t0,t1):
    a=int((t0+0.1)*sr); b=int(t1*sr); seg=m[a:b]; h=int(0.002*sr); k=len(seg)//h
    if k<100: return None
    e=np.sqrt((seg[:k*h].reshape(k,h)**2).mean(1)); e=e-e.mean(); E=np.abs(np.fft.rfft(e*np.hanning(k)))**2; f=np.fft.rfftfreq(k,0.002)
    return 10*np.log10(E[(f>=8)&(f<=24)].sum()/(E[(f>=1)&(f<=6)].sum()+1e-30))
by=defaultdict(list)
for r in rows: by[key(r['staff'])].append(r)
for st in ["Violins I","Violins II","Violas"]:
    p=os.path.join(sys.argv[2],re.sub(r"\W+","_",st)+".wav"); x,sr=sf.read(p,dtype='float32'); m=x.mean(1)
    tr=[mod(m,sr,float(r['t_on_s']),float(r['t_on_s'])+float(r['notated_s'])) for r in by[st] if 'tremolo32' in r['arts'] and float(r['notated_s'])>=0.5]
    su=[mod(m,sr,float(r['t_on_s']),float(r['t_on_s'])+float(r['notated_s'])) for r in by[st] if r['arts']=='' and r['slur']=='' and float(r['notated_s'])>=0.5]
    tr=[v for v in tr if v is not None]; su=[v for v in su if v is not None]
    print(f"{st:12s} tremolo 8-24 vs 1-6 Hz {np.median(tr):+.1f} dB (n={len(tr)}); sustained {np.median(su):+.1f} dB (n={len(su)})")
