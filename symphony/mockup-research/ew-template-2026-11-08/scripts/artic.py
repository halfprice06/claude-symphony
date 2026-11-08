import sys, json, collections, statistics as st, bisect
L=open(sys.argv[1],errors='replace').read().replace('\r','').split('\n')
OP=json.load(open(sys.argv[2]))
PPQ=480; MSPT=60000/130/PPQ
items=[]; tname=None; i=0
while i<len(L):
    l=L[i]
    if l.startswith('  <TRACK'): tname=None
    elif l.startswith('    NAME ') and tname is None: tname=l[9:].strip('"')
    elif l.strip()=='<SOURCE MIDI':
        t=0; ev=[]; i+=1
        while L[i].strip()!='>':
            p=L[i].split()
            if p and p[0] in('E','e'): t+=int(p[1]); ev.append((t,int(p[2],16),int(p[3],16),int(p[4],16)))
            elif p and p[0] in('X','x'): t+=int(p[1])
            elif p and p[0] in('<X','<x'):
                t+=int(p[1]); i+=1
                while L[i].strip()!='>': i+=1
            i+=1
        items.append((tname,ev))
    i+=1
def q(v):
    v=sorted(v); return f"med {st.median(v):.0f} (IQR {v[len(v)//4]:.0f}..{v[3*len(v)//4]:.0f}, n={len(v)})" if v else '-'
for name,ev in items:
    if name not in OP: continue
    ins=[z['instrument'] for z in OP[name]['zones'] if z.get('instrument')]
    if len(ins)!=1: continue
    ins=ins[0]
    arts=ins.get('articulations',{}).get('trigger',[])
    keymap={a['key']:a['name'] for a in arts if a.get('useKey')}
    if not keymap: continue
    notes=[];on={};cc1=[]
    for t,s,a,b in ev:
        ty=s&0xF0
        if ty==0x90 and b>0: on.setdefault(a,[]).append((t,b))
        elif ty==0x80 or (ty==0x90 and b==0):
            if on.get(a): t0,v=on[a].pop(0); notes.append((t0,t,a,v))
        elif ty==0xB0 and a==1: cc1.append((t,b))
    notes.sort(); cct=[c[0] for c in cc1]
    ks=[n for n in notes if n[2] in keymap]; real=[n for n in notes if n[2] not in keymap]
    kst=[k[0] for k in ks]
    by=collections.defaultdict(list)
    for n in real:
        j=bisect.bisect_right(kst,n[0])-1
        art=keymap[ks[j][2]] if j>=0 else ins['articulations'].get('currentKeySwitch')
        by[art].append(n)
    # KS lead time: KS note before the note it affects
    leads=[]
    for k in ks:
        nx=[n for n in real if n[0]>=k[0]]
        if nx: leads.append((nx[0][0]-k[0])*MSPT)
    print(f"\n### {name}  (keyswitch notes {len(ks)}, KS lead before next note: {q(leads)} ms)")
    for art,ns in by.items():
        vel=[n[3] for n in ns]; dur=[(n[1]-n[0])*MSPT for n in ns]
        c=[cc1[bisect.bisect_right(cct,n[0])-1][1] for n in ns if bisect.bisect_right(cct,n[0])>0]
        rep=[(b[0]-a[1])*MSPT for a,b in zip(ns,ns[1:]) if a[2]==b[2] and 0<=(b[0]-a[1])*MSPT<300]
        ovl=[(a[1]-b[0])*MSPT for a,b in zip(ns,ns[1:]) if b[0]>a[0] and a[1]>b[0]]
        offg=[]
        for n in ns:
            g=PPQ//4; dd=n[0]%g; dd=dd if dd<=g/2 else dd-g; offg.append(dd*MSPT)
        early=sum(1 for o in offg if o<-1)/len(offg)*100; late=sum(1 for o in offg if o>1)/len(offg)*100
        print(f"  {art:24} notes {len(ns):3} | vel {q(vel)} | dur ms {q(dur)} | CC1 at onset {q(c)} | rep-gap ms {q(rep)} | overlap ms {q(ovl)} | off-grid early {early:.0f}% late {late:.0f}%")
