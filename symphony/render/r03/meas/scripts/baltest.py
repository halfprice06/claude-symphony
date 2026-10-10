# offline balance test: place stems from _syn without gains (cached levels), run balance.compute, predict melody metric
import sys, os, json, csv, subprocess, re
sys.path.insert(0,'/mnt/project-files/symphony/render/r03/lib'); sys.path.insert(0,'/mnt/project-files/symphony/render/r03')
import numpy as np, soundfile as sf, marks, balance, rtk, importlib
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
W=sys.argv[1]; cache=os.path.join(W,'levels_cache.json')
cfg=json.load(open('/mnt/project-files/symphony/render/r03/config.json'))
mi=rtk.midi_info(W+'/score.midi'); bars=[(b['bar'],b['t_start'],b['t_end']) for b in mi['per_bar']]
rows=list(csv.DictReader(open(W+'/notes.csv')))
def key(n): return balance.key(n)
by=defaultdict(list)
for r in rows: by[key(r['midi_track']) if r['midi_track'] else key(r['staff'])].append(r)
st=W+'/stems'
if not os.path.exists(cache):
    mids=[f for f in os.listdir(st) if f.endswith('.mid')]
    def one(f):
        p=os.path.join(st,f); w=p[:-4]+'_nb.wav'
        subprocess.run([sys.executable,'/mnt/project-files/symphony/render/r03/stem.py',p,w,'--from-synth',p[:-4]+'_syn.wav'],check=True)
        import stem, mido
        g=stem.staff_of(mido.MidiFile(p),cfg)
        x,_=sf.read(w,dtype='float64',always_2d=True); os.remove(w)
        a,b=balance.bar_levels(x,48000,by.get(g,[]),bars)
        return g,(a,b)
    with ThreadPoolExecutor(4) as ex: L=dict(ex.map(one,mids))
    json.dump({g:[{str(k):v for k,v in a.items()},{str(k):v for k,v in b.items()}] for g,(a,b) in L.items()},open(cache,'w'))
J=json.load(open(cache))
levels={g:{int(k):v for k,v in a[0].items()} for g,a in J.items()}; whole={g:{int(k):v for k,v in a[1].items()} for g,a in J.items()}
mel=marks.melodies(W+'/ly_scratch/events.tsv',rows,mi['bar_s'],tpb=mi['tpb']); rl=marks.rolls(rows,mi['bar_s'])
B=cfg['balance']
for kv in sys.argv[2:]:
    k,v=kv.split('='); B[k]=float(v)
gains,rep=balance.compute(levels,bars,mel,rl,B,whole=whole)
# predicted melody metric (melody2 logic)
res=[]
for s,bs,_,_,txt in mel:
    dm=[];ds=[]
    for b in bs:
        if b not in levels.get(s,{}): continue
        m=levels[s][b]+gains[s].get(b,0)
        o={k:levels[k][b]+gains[k].get(b,0) for k in levels if k!=s and b in levels[k] and not k.startswith('Harp') and k!='drums'}
        if not o: continue
        dm.append(m-max(o.values())); ds.append(m-10*np.log10(sum(10**(v/10) for v in o.values())))
    if dm: res.append((s,bs[0],np.median(dm),np.median(ds)))
for r in res: print(f'  {r[0]:15s} {r[1]:4d} {r[2]:+.1f} {r[3]:+.1f}')
print('>=0:',sum(r[2]>=0 for r in res),'of',len(res),' >=-6 sum:',sum(r[3]>=-6 for r in res),' median',round(float(np.median([r[2] for r in res])),1))
print(rep['rolls'])
# timpani loudest (whole bar) predicted
n=t=0
for r in rl:
    for b in r[2]:
        if b in whole.get('Timpani',{}):
            tm=whole['Timpani'][b]+gains['Timpani'].get(b,0); o=max(whole[k][b]+gains[k].get(b,0) for k in whole if k not in('Timpani','drums') and b in whole[k])
            t+=1; n+= tm>o
print('timp loudest',n,'of',t)
