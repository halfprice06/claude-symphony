import music21 as m21, sys, pickle, os
f=sys.argv[1]; a,b=int(sys.argv[2]),int(sys.argv[3]); step=float(sys.argv[4]) if len(sys.argv)>4 else 2.0
pk='/tmp/critic-002/'+os.path.basename(f)+'.pkl'
if False: pass
else:
    s=m21.converter.parse(f)
ex=s.measures(a,b)
ch=ex.chordify()
for m in ch.getElementsByClass('Measure'):
    out=[]
    ts=m.barDuration.quarterLength
    t=0
    while t<ts:
        ps=set()
        for c in m.notes:
            if c.offset<=t<c.offset+c.quarterLength or (c.offset>=t and c.offset<t+step):
                for p in c.pitches: ps.add(p)
        if ps:
            lo=min(ps,key=lambda p:p.ps)
            pcs=sorted({p.name for p in ps})
            try: rn=m21.chord.Chord(list(ps)).commonName
            except: rn=''
            out.append(f"{lo.nameWithOctave}|{' '.join(pcs)}")
        t+=step
    print(m.number, ' ;; '.join(out))
