import mido, sys, collections
f=sys.argv[1]
mf=mido.MidiFile(f); tpb=mf.ticks_per_beat
tracks={}
for i,t in enumerate(mf.tracks):
    tm=0; on={}; name=str(i); ns=[]
    for m in t:
        tm+=m.time
        if m.type=='track_name': name=m.name
        if m.type=='note_on' and m.velocity>0: on.setdefault((m.channel,m.note),[]).append(tm)
        elif m.type in('note_off','note_on') and on.get((m.channel,m.note)):
            s=on[(m.channel,m.note)].pop(0); ns.append((s/tpb,tm/tpb,m.note))
    if ns and not any(x in name for x in ('imp','drum','Cym','Harp')):
        tracks.setdefault(name.split(':')[0],[]).extend(ns)
def line(ns,which):
    by=collections.defaultdict(list)
    for s,e,p in ns: by[s].append((e,p))
    out=[]
    for s in sorted(by):
        ps=[p for e,p in by[s]]
        out.append((s,max(by[s])[0] if False else max(e for e,p in by[s]),max(ps) if which=='^' else min(ps)))
    return out
L={}
for k,ns in tracks.items():
    L[k+'^']=line(ns,'^'); L[k+'_']=line(ns,'_')
def at(l,t):
    # pitch sounding at time t (latest onset <= t still sounding)
    r=None
    for s,e,p in l:
        if s<=t+1e-6 and e>t+1e-6: r=(s,p)
        if s>t: break
    return r
NM='C Db D Eb E F F# G Ab A Bb B'.split()
nm=lambda p:NM[p%12]+str(p//12-1)
keys=sorted(L); res=[]
for i,a in enumerate(keys):
    for b in keys[i+1:]:
        if a[:-1]==b[:-1]: continue
        ts=sorted({s for s,e,p in L[a]}|{s for s,e,p in L[b]})
        prev=None; prevprev=None
        for t in ts:
            x=at(L[a],t); y=at(L[b],t)
            cur=(x[1],y[1]) if x and y else None
            if cur and prev and cur[0]!=prev[0] and cur[1]!=prev[1]:
                i1=abs(prev[0]-prev[1]); i2=abs(cur[0]-cur[1])
                same=(cur[0]-prev[0])*(cur[1]-prev[1])>0
                if same and i1%12==7 and i2%12==7:
                    res.append((t,'P5',a,b,nm(prev[0])+'-'+nm(prev[1]),nm(cur[0])+'-'+nm(cur[1])))
                if same and i1%12==0 and i2%12==0 and i1>0 and prevprev and abs(prevprev[0]-prevprev[1])%12!=0:
                    res.append((t,'P8',a,b,nm(prev[0])+'-'+nm(prev[1]),nm(cur[0])+'-'+nm(cur[1])))
            prevprev=prev; prev=cur if cur else None
res.sort()
for t,k,a,b,p,c in res:
    bar=int(t//4)+1; beat=t%4+1
    print(f"{bar}:{beat:.1f} {k} {a} / {b}  {p} -> {c}")
