"""Staccato peak against unmarked notes (critic 1, section 2 item 1): for each staccato note, the peak of the
10 ms RMS envelope in the first 150 ms of the note, minus the median peak of unmarked notes (no articulation)
of the same staff and printed dynamic within +-2 bars. Also sounding/notated length from the MIDI.
usage: staccpeak.py notes.csv STEMDIR (wavs named like render.py: Violins_I.wav)"""
import csv, sys, re, os, numpy as np, soundfile as sf
from collections import defaultdict
rows=list(csv.DictReader(open(sys.argv[1]))); W=sys.argv[2]
def key(n): return re.sub(r"[^A-Za-z0-9 ]","",n.split(":")[0]).strip()
by=defaultdict(list)
for r in rows: by[key(r['staff'])].append(r)
for st,rs in sorted(by.items()):
    sts=[r for r in rs if 'staccato' in r['arts'].split('|')]
    if not sts: continue
    p=os.path.join(W,re.sub(r"\W+","_",st)+".wav")
    if not os.path.exists(p): continue
    x,sr=sf.read(p,dtype='float32'); m=x.mean(1)
    def pk(t):
        a=int(t*sr); seg=m[a:a+int(0.15*sr)]; h=int(0.01*sr); k=len(seg)//h
        return 10*np.log10((seg[:k*h].reshape(k,h)**2).mean(1).max()+1e-20) if k else -200
    un=[r for r in rs if r['arts']=='' and r['tech']=='']
    d=[]; ratio=[]
    for r in sts:
        b=int(r['bar']); ref=[pk(float(u['t_on_s'])) for u in un if u['dyn']==r['dyn'] and abs(int(u['bar'])-b)<=2]
        if len(ref)>=2: d.append(pk(float(r['t_on_s']))-np.median(ref))
        if r['midi_len'] and r['notated_ticks']: ratio.append(int(r['midi_len'])/int(r['notated_ticks']))
    print(f"{st:14s} staccato n={len(sts)} peak minus unmarked median {np.median(d) if d else float('nan'):+.1f} dB (n={len(d)}); sounding/notated {np.median(ratio):.2f}")
