import mido, sys, itertools, collections
mf=mido.MidiFile(sys.argv[1]); tpb=mf.ticks_per_beat
names=['fluteOne','fluteTwo','oboeOne','oboeTwo','corAnglais','clOne','clTwo','bassCl','bsnOne','bsnTwo','cbsn','hnOne','hnTwo','hnThree','hnFour','tptOne','tptTwo','tptThree','tbnOne','tbnTwo','bassTbn','tuba','timp','harpR','harpL','vlnOne','vlnTwo','vla','vc','cb']
tracks=[t for t in mf.tracks if any(m.type=='note_on' for m in t)]
# map by order of staves (lilypond writes one track per staff in order); verify count
notes={}
ti=0
for t in mf.tracks[1:]:
    tm=0; on={}; ns=[]
    for m in t:
        tm+=m.time
        if m.type=='note_on' and m.velocity>0: on.setdefault(m.note,[]).append(tm)
        elif m.type in('note_off','note_on'):
            if m.note in on and on[m.note]:
                s=on[m.note].pop(0); ns.append((s/tpb,tm/tpb,m.note))
    if ti<len(names): notes[names[ti]]=sorted(ns)
    ti+=1
print('tracks',ti,file=sys.stderr)
skip={'timp','harpR','harpL'}
# build voices: top and bottom
voices={}
for n,ns in notes.items():
    if n in skip: continue
    by=collections.defaultdict(list)
    for s,e,p in ns: by[s].append((s,e,p))
    top=[];bot=[]
    for s in sorted(by):
        g=by[s]; top.append(max(g,key=lambda x:x[2])); bot.append(min(g,key=lambda x:x[2]))
    voices[n]=top
    if any(len(g)>1 for g in by.values()): voices[n+'.lo']=bot
def at(v,t):
    # pitch sounding at time t, with onset flag
    for s,e,p in v:
        if s<=t<e-1e-6: return p,abs(s-t)<1e-6
    return None,False
# global bass line: lowest sounding (excl timp/harp)
allv=[(n,v) for n,v in voices.items()]
times=sorted({s for v in voices.values() for s,e,p in v})
def bar(t): return int(t//4)+1, t%4+1
# precompute sounding pitch per voice per time
snd={}
for n,v in voices.items():
    d={}; i=0
    vs=sorted(v)
    for t in times:
        p=None;on=False
        for s,e,pp in vs:
            if s<=t+1e-6 and t<e-1e-6: p=pp; on=abs(s-t)<1e-6
            if s>t: break
        d[t]=(p,on)
    snd[n]=d
bass={t:min([snd[n][t][0] for n in voices if snd[n][t][0] is not None],default=None) for t in times}
snd['BASS']={t:(bass[t], True) for t in times}
names2=list(voices)+['BASS']
out=[]
def check(a,b):
    A=snd[a];B=snd[b]
    seq=[]
    prev=None
    for t in times:
        pa,oa=A[t];pb,ob=B[t]
        if pa is None or pb is None: prev=None; seq.append(None); continue
        seq.append((t,pa,pb))
    pts=[x for x in seq]
    # collapse repeated identical states
    st=[]
    for x in pts:
        if x is None: st.append(None); continue
        if st and st[-1] is not None and st[-1][1]==x[1] and st[-1][2]==x[2]: continue
        st.append(x)
    for i in range(1,len(st)):
        x,y=st[i-1],st[i]
        if x is None or y is None: continue
        da=y[1]-x[1]; db=y[2]-x[2]
        if da==0 or db==0 or (da>0)!=(db>0): continue
        i1=abs(x[1]-x[2]); i2=abs(y[1]-y[2])
        for cls,lab in ((7,'P5'),(0,'P8')):
            if i1%12==cls and i2%12==cls and i1>0 or (cls==0 and i1%12==0 and i2%12==0):
                # doubling filter: neighbours same class
                nb=[st[j] for j in (i-2,i+1) if 0<=j<len(st) and st[j] is not None]
                same=sum(1 for z in nb if abs(z[1]-z[2])%12==cls)
                if cls==0 and (not nb or same>0): continue
                if cls==7 and nb and same==len(nb): continue
                out.append((y[0],lab,a,b,x[1],y[1],x[2],y[2]))
for a,b in itertools.combinations(names2,2):
    if a.split('.')[0]==b.split('.')[0]: continue
    check(a,b)
nm=lambda p: ['C','Db','D','Eb','E','F','F#','G','Ab','A','Bb','B'][p%12]+str(p//12-1)
out.sort()
for t,lab,a,b,a1,a2,b1,b2 in out:
    br,bt=bar(t)
    print(f"bar {br} beat {bt:.2f} {lab} {a}:{nm(a1)}->{nm(a2)} {b}:{nm(b1)}->{nm(b2)}")
