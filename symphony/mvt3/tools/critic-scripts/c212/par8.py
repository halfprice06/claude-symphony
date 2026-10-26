import mido, sys, collections
mf=mido.MidiFile(sys.argv[1]); tpb=mf.ticks_per_beat; bar=4*tpb
a,b=int(sys.argv[2]),int(sys.argv[3])
tr={}
for i,t in enumerate(mf.tracks):
    nm=''.join(m.name for m in t if m.type=='track_name')
    if 'Timp' in nm or 'Harp' in nm or i==49 or i==0: continue
    tm=0; on={}; ns=[]
    for m in t:
        tm+=m.time
        if m.type=='note_on' and m.velocity>0: on.setdefault(m.note,[]).append(tm)
        elif m.type in('note_off','note_on') and m.note in on and on[m.note]:
            s=on[m.note].pop(0); ns.append((s,tm,m.note))
    if ns: tr[nm]=ns
allns=[n for v in tr.values() for n in v]
def sounding(ns,t): return [n for s,e,n in ns if s<=t<e]
# sample on quarter grid
pts=[(B-1)*bar+q*tpb for B in range(a,b+1) for q in range(4)]
def bass(t):
    s=sounding(allns,t); return min(s) if s else None
names='C C# D Eb E F F# G Ab A Bb B'.split()
prev=None
for t in pts:
    bs=bass(t)
    if prev is not None and bs is not None and prev[1] is not None and bs!=prev[1]:
        t0,b0=prev
        for nm,ns in tr.items():
            for f in (max,min):
                s0=sounding(ns,t0); s1=sounding(ns,t)
                if not s0 or not s1: continue
                v0,v1=f(s0),f(s1)
                if v0==v1: continue
                for iv,lab in ((0,'8ve'),(7,'5th')):
                    if (v0-b0)%12==iv and (v1-bs)%12==iv and v0!=b0 and v1!=bs and (v1-v0)*(bs-b0)>0:
                        B=t//bar+1; q=(t%bar)//tpb+1
                        print(f"{B}.{q} {lab} {nm.split(':')[0][:14]}:{nm.split(':')[-1][:6]} {'hi' if f is max else 'lo'} {names[v0%12]}{v0//12-1}->{names[v1%12]}{v1//12-1} bass {names[b0%12]}{b0//12-1}->{names[bs%12]}{bs//12-1}")
                        break
    prev=(t,bs)
