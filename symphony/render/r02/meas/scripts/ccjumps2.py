"""critic 1's ccjumps.py, per channel: CC11 steps >= 3 dB within one control step while a note of the SAME
channel is held (r02 writes one CC11 curve per voice channel). Usage: ccjumps2.py MIDI"""
import mido, numpy as np, sys
from collections import defaultdict
sys.path.insert(0,'/mnt/project-files/symphony/render/r02')
from articulate import TempoMap, key
mid=mido.MidiFile(sys.argv[1]); tm=TempoMap(mid)
cc=defaultdict(list); notes=defaultdict(list)
for tr in mid.tracks[1:]:
    t=0; act={}; st=key(tr.name)
    for m in tr:
        t+=m.time
        if m.type=='control_change' and m.control==11: cc[(st,m.channel)].append((tm.t2s(t),m.value))
        if m.type=='note_on' and m.velocity>0: act[(m.channel,m.note)]=tm.t2s(t)
        elif m.type in('note_off','note_on') and (m.channel,m.note) in act:
            notes[(st,m.channel)].append((act.pop((m.channel,m.note)),tm.t2s(t)))
tot=0; per=defaultdict(int)
for k in cc:
    c=sorted(cc[k]); ns=np.array(notes[k]) if notes[k] else np.zeros((0,2))
    for (t0,v0),(t1,v1) in zip(c,c[1:]):
        d=40*np.log10(v1/v0)
        if abs(d)>=3 and len(ns) and ((ns[:,0]<t1-0.1)&(ns[:,1]>t1+0.05)).sum():
            tot+=1; per[k[0]]+=1
print(dict(per)); print('total',tot)
