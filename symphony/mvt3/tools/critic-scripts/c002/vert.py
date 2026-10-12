import mido, sys, collections
f=sys.argv[1]; a,b=int(sys.argv[2]),int(sys.argv[3]); step=float(sys.argv[4]) if len(sys.argv)>4 else 1.0
mf=mido.MidiFile(f); tpb=mf.ticks_per_beat
N=[]
for i,t in enumerate(mf.tracks):
    tm=0; on={}; name=str(i)
    for m in t:
        tm+=m.time
        if m.type=='track_name': name=m.name
        if m.type=='note_on' and m.velocity>0: on.setdefault((m.channel,m.note),[]).append(tm)
        elif m.type in('note_off','note_on') and on.get((m.channel,m.note)):
            s=on[(m.channel,m.note)].pop(0); N.append((s/tpb,tm/tpb,m.note,name))
NM='C Db D Eb E F F# G Ab A Bb B'.split()
nm=lambda p:NM[p%12]+str(p//12-1)
for bar in range(a,b+1):
    out=[]
    t=(bar-1)*4.0
    while t<bar*4-1e-6:
        s=[(p,n) for st,e,p,n in N if st<=t+1e-6<e and 'imp' not in n and 'drum' not in n.lower() and 'Cym' not in n]
        if s:
            lo=min(p for p,n in s); hi=max(p for p,n in s)
            pcs=sorted({p%12 for p,n in s}, key=lambda x:(x-lo)%12)
            out.append(f"{nm(lo)}[{' '.join(NM[x] for x in pcs)}]^{nm(hi)}")
        else: out.append('-')
        t+=step
    print(bar,' | '.join(out))
