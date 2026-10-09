# For notes >= 1 s under a printed hairpin: compare the realised CC11 change over the note (dB, 40log10)
# with the change of the velocity-equivalent curve (start velocity vs velocity of the next note in the staff)
import mido, csv, re, numpy as np, sys
from collections import defaultdict
sys.path.insert(0,'/mnt/project-files/symphony/render/r01')
from articulate import TempoMap, key
mid=mido.MidiFile('/mnt/project-files/symphony/render/r01/r01.midi'); tm=TempoMap(mid)
cc=defaultdict(list)
for tr in mid.tracks[1:]:
    t=0
    for m in tr:
        t+=m.time
        if m.type=='control_change' and m.control==11 and m.channel==0: cc[key(tr.name)].append((tm.t2s(t),m.value))
rows=list(csv.DictReader(open('/tmp/rcritic-01/notes_r01.csv')))
bystaff=defaultdict(list)
for r in rows: bystaff[key(r['midi_track']) if r['midi_track'] else r['staff']].append(r)
res=[]
for st,rs in bystaff.items():
    if st not in cc: continue
    ct=np.array([c[0] for c in cc[st]]); cv=np.array([c[1] for c in cc[st]])
    def ccat(s):
        i=np.searchsorted(ct,s,side='right')-1; return cv[max(i,0)]
    ons=sorted(set(float(r['t_on_s']) for r in rs))
    for r in rs:
        if not r['hairpin'] or float(r['notated_s'])<1.0 or 'tremolo' in r['arts'] or r['staff']=='Timpani': continue
        t0=float(r['t_on_s']); t1=t0+float(r['notated_s'])
        # velocities at the next onset of this staff at/after t1 (printed curve target)
        nxt=[x for x in rs if abs(float(x['t_on_s'])-t1)<0.03 and x['midi_vel'] and not x['arts']]
        if not nxt: continue
        v0=int(r['midi_vel']); v1=np.median([int(x['midi_vel']) for x in nxt])
        want=40*np.log10(v1/v0)
        # realised: cc11 just before t1 minus cc11 just after onset (+0.3s, after accent dips)
        a=ccat(t0+0.05); b=ccat(t1-0.03)
        got=40*np.log10(b/a)
        capped=b==127 and want>got+1
        # max cc over note
        res.append((st,r['bar'],r['hairpin'],round(t1-t0,2),v0,v1,round(want,1),round(got,1),a,b,capped))
cr=[x for x in res if x[2]=='cresc']; de=[x for x in res if x[2]=='decresc']
for name,L in (('cresc',cr),('decresc',de)):
    w=np.array([x[6] for x in L]); g=np.array([x[7] for x in L])
    print(name,'n',len(L),'printed change median %.1f dB, realised median %.1f dB; realised/printed ratio median %.2f; capped at CC11=127: %d'%(np.median(w),np.median(g),np.median(g[np.abs(w)>1]/w[np.abs(w)>1]),sum(x[10] for x in L)))
print('examples cresc with largest shortfall:')
for x in sorted(cr,key=lambda x:x[7]-x[6])[:12]: print(x)
