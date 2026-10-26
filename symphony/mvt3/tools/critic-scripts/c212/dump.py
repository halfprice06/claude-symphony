import mido, sys
mf=mido.MidiFile(sys.argv[1]); tpb=mf.ticks_per_beat
a,b=int(sys.argv[2]),int(sys.argv[3])
names='C C# D Eb E F F# G Ab A Bb B'.split()
def nn(n): return names[n%12]+str(n//12-1)
notes=[]
for i,t in enumerate(mf.tracks):
    nm=''.join(m.name for m in t if m.type=='track_name')
    if 'Timp' in nm or i==49 or 'Harp' in nm: continue
    if len(sys.argv)>4 and sys.argv[4]=='noharp' and 'Harp' in nm: continue
    tm=0; on={}
    for m in t:
        tm+=m.time
        if m.type=='note_on' and m.velocity>0: on.setdefault(m.note,[]).append(tm)
        elif m.type in('note_off','note_on') and m.note in on and on[m.note]:
            s=on[m.note].pop(0); notes.append((s,tm,m.note,nm.split(':')[0][:6]))
bar=4*tpb
for B in range(a,b+1):
    row=[]
    for q in range(8):
        t=(B-1)*bar+q*tpb//2
        ps=sorted({n for s,e,n,_ in notes if s<=t<e})
        if not ps: row.append('-'); continue
        pcs=[]
        for p in ps:
            if names[p%12] not in pcs: pcs.append(names[p%12])
        row.append(f"{nn(ps[0])}/{nn(ps[-1])}[{' '.join(pcs)}]")
    print(B,' | '.join(row))
