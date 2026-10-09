import mido, numpy as np, sys
from collections import defaultdict
sys.path.insert(0,'/mnt/project-files/symphony/render/r01')
from articulate import TempoMap, key
mid=mido.MidiFile('/mnt/project-files/symphony/render/r01/r01.midi'); tm=TempoMap(mid)
cc=defaultdict(list); notes=defaultdict(list)
for tr in mid.tracks[1:]:
    t=0; act={}
    st=key(tr.name)
    for m in tr:
        t+=m.time
        if m.type=='control_change' and m.control==11 and m.channel==0: cc[st].append((tm.t2s(t),m.value))
        if m.type=='note_on' and m.velocity>0: act[(m.channel,m.note)]=tm.t2s(t)
        elif m.type in('note_off','note_on') and (m.channel,m.note) in act:
            notes[st].append((act.pop((m.channel,m.note)),tm.t2s(t)))
tot=0
for st in cc:
    c=cc[st]; ns=np.array(notes[st]) if notes[st] else np.zeros((0,2))
    jumps=[]
    for (t0,v0),(t1,v1) in zip(c,c[1:]):
        d=40*np.log10(v1/v0)
        if abs(d)>=3:
            held=((ns[:,0]<t1-0.1)&(ns[:,1]>t1+0.05)).sum() if len(ns) else 0
            if held: jumps.append((round(t1,2),round(d,1)))
    tot+=len(jumps)
    if jumps: print(f"{st:15s} {len(jumps):4d} steps >=3 dB in one 20 ms step while a note is held; down {sum(1 for j in jumps if j[1]<0)}, largest {min(j[1] for j in jumps)}/{max(j[1] for j in jumps)}; e.g. {jumps[:4]}")
print('total',tot)
