import mido, sys
m = mido.MidiFile(sys.argv[1]); tpb=m.ticks_per_beat
notes=[]
for t in m.tracks:
    now=0; on={}
    for msg in t:
        now+=msg.time
        if msg.type=='note_on' and msg.velocity>0: on.setdefault(msg.note,[]).append(now)
        elif msg.type in('note_off','note_on') and on.get(msg.note): notes.append((on[msg.note].pop(0),now,msg.note))
end=max(n[1] for n in notes); res={}
for tk in range(0,end,tpb//4):
    pcs={n[2]%12 for n in notes if n[0]<=tk<n[1]}
    if {0,4,7}<=pcs: res.setdefault(tk//(3*tpb)+1,set()).update(pcs)
for b,p in sorted(res.items()): print(b, sorted(p))
