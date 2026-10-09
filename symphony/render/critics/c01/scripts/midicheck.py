import mido, sys, re
from collections import defaultdict, Counter
def key(n):
    k=re.sub(r"[^A-Za-z0-9 ]","",n.split(":")[0]).strip(); return k or "drums"
def notes(tr):
    t=0; act={}; out=[]; dangling=0
    for m in tr:
        t+=m.time
        if m.type=="note_on" and m.velocity>0:
            if (m.channel,m.note) in act: dangling+=1
            act.setdefault((m.channel,m.note),[]).append(t)
        elif m.type in("note_on","note_off"):
            l=act.get((m.channel,m.note))
            if l: out.append((l.pop(0),t,m.note,m.channel))
    stuck=sum(len(v) for v in act.values())
    return out,stuck,dangling
a=mido.MidiFile(sys.argv[1]); b=mido.MidiFile(sys.argv[2])
tpb=a.ticks_per_beat
print("tpb",tpb,b.ticks_per_beat,"tracks",len(a.tracks),len(b.tracks))
for ta,tb in zip(a.tracks[1:],b.tracks[1:]):
    na,sa,da=notes(ta); nb,sb,db=notes(tb)
    progs=sorted(set((m.channel,m.program) for m in tb if m.type=="program_change"))
    cc=Counter(m.control for m in tb if m.type=="control_change")
    cc11=[m.value for m in tb if m.type=="control_change" and m.control==11]
    longa=max([(o-s) for s,o,_,_ in na] or [0])/tpb; longb=max([(o-s) for s,o,_,_ in nb] or [0])/tpb
    onsA=Counter(s for s,_,_,_ in na); onsB=Counter(s for s,_,_,_ in nb)
    print(f"{ta.name[:28]:28s} notes {len(na):4d}->{len(nb):4d} stuck {sa}/{sb} reon {da}/{db} maxlen(beats) {longa:.1f}->{longb:.1f} progs {progs} cc11[{min(cc11) if cc11 else '-'}..{max(cc11) if cc11 else '-'}] n={len(cc11)} ccs {dict(cc)}")
