#!/usr/bin/env python3
# guard.py OLD_DIR NEW_DIR : compare score.midi per track (note count, last note end in ticks) and analysis.txt track table.
# Added after c439 found the violas two bars short in v436-v439 (a part that ends early in the last section gives no bar-check warning).
import sys, mido
def info(d):
    m=mido.MidiFile(f'{d}/score.midi'); r={}
    for i,t in enumerate(m.tracks):
        tick=0; n=0; last=0; name=str(i)
        for e in t:
            tick+=e.time
            if e.type=='track_name': name=e.name
            if e.type=='note_on' and e.velocity>0: n+=1
            if e.type in('note_off','note_on'): last=tick
        if n: r[f'{i}:{name}']=(n,last)
    return r
a,b=info(sys.argv[1]),info(sys.argv[2]); bad=0
for k in sorted(set(a)|set(b)):
    if a.get(k)!=b.get(k):
        print('GUARD', k, a.get(k), '->', b.get(k)); bad+= (a.get(k) is None or b.get(k) is None or a[k][1]!=b[k][1])
print('guard: %d track(s) changed end time or vanished' % bad if bad else 'guard: track end times unchanged')
