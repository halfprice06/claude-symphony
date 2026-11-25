import sys, collections
B='/Users/gooby/sandbox/claude_composes/symphony/mvt3/reaper-v600/build/mockup-events.tsv'
ORDER=['Fl1','Fl2','Ob1','Ob2','CA','Cl1','Cl2','BCl','Bn1','Bn2','Cbn','Hn1','Hn2','Hn3','Hn4','Tpt1','Tpt2','Tpt3','Tbn1','Tbn2','BTbn','Tuba','Timp','HarpR','HarpL','VlnI','VlnII','Vla','Vc','Cb']
PROG={'Fl':73,'Ob':68,'CA':69,'Cl':71,'BCl':71,'Bn':70,'Cbn':70,'Hn':60,'Tpt':56,'Tbn':57,'BTbn':57,'Tuba':58,'Timp':47,'Harp':46,'Vln':48,'Vla':48,'Vc':48,'Cb':48}
PAN={'Fl':-0.1,'Ob':0.1,'CA':0.15,'Cl':-0.15,'BCl':-0.2,'Bn':0.15,'Cbn':0.2,'Hn':-0.3,'Tpt':0.2,'Tbn':0.3,'BTbn':0.35,'Tuba':0.35,'Timp':0.0,'Harp':-0.5,'VlnI':-0.5,'VlnII':-0.2,'Vla':0.2,'Vc':0.4,'Cb':0.5}
def key(st,table):
    for k in sorted(table,key=len,reverse=True):
        if st.startswith(k): return table[k]
VEL={'ppp':30,'pp':40,'p':52,'mp':64,'mf':76,'f':92,'ff':108,'fff':120,'sf':104,'sfz':108,'fp':92,'sfp':100,'fz':104}
b0,b1,variant,out=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3],sys.argv[4]
only=sys.argv[5].split(',') if len(sys.argv)>5 else None
QPM=168.0
notes=collections.defaultdict(list); dyn=collections.defaultdict(list); acc=set(); ties=set(); trem=set()
for l in open(B):
    f=l.rstrip('\n').split('\t')
    if len(f)<4: continue
    st,q,typ=f[0],float(f[1]),f[3]
    if typ=='note': notes[st].append([q,float(f[5]),int(f[4])])
    elif typ=='dynamic' and f[4] in VEL: dyn[st].append((q,f[4]))
    elif typ=='script' and f[4]=='accent': acc.add((st,q))
    elif typ=='tie': ties.add((st,q))
    elif typ=='tremolo': trem.add((st,q))
q0,q1=(b0-1)*4.0,b1*4.0
ev=[]; hdr=[]
for i,st in enumerate(ORDER):
    hdr.append(f"inst {i} {key(st,PROG)} {key(st,PAN)} {st}")
    if only and st not in only: continue
    ns=sorted(notes[st]); ds=sorted(dyn[st])
    # variant B: the five brass staves' beat-2 chord in bar 166 moves to beat 1 and lasts the half note
    if variant=='B' and st in ('Hn3','Hn4','Tpt1','Tpt2','Tpt3'):
        for n in ns:
            if n[0]==165*4+1.0: n[0]=165*4.0; n[1]=2.0
    # merge ties
    merged=[]
    for q,d,p in ns:
        m=next((x for x in merged if x[2]==p and abs(x[0]+x[1]-q)<1e-6 and x[3]),None)
        if m: m[1]+=d; m[3]=(st,q) in ties
        else: merged.append([q,d,p,(st,q) in ties,(st,q) in trem])
    if variant=='C' and st in ('Hn3','Hn4','Tpt1','Tpt2','Tpt3'):
        merged=[m for m in merged if m[0]!=165*4+1.0]
    for q,d,p,_,tr in merged:
        if q<q0 or q>=q1: continue
        lv=[x[1] for x in ds if x[0]<=q]
        v=VEL[lv[-1]] if lv else 76
        if (st,q) in acc: v=min(127,v+12)
        if st=='Timp' and tr:
            k=0.0
            while k<d-1e-6:
                ev.append(((q+k-q0)*60/QPM,i,'on',p,max(30,v-14 if k else v)))
                ev.append(((q+k+0.24-q0)*60/QPM,i,'off',p,0)); k+=0.25
        else:
            ev.append(((q-q0)*60/QPM,i,'on',p,v))
            ev.append(((q+d*0.93-q0)*60/QPM,i,'off',p,0))
ev.sort(key=lambda e:(e[0],0 if e[2]=='off' else 1))
with open(out,'w') as f:
    f.write('\n'.join(hdr)+'\n')
    f.write(f"len {(q1-q0)*60/QPM+2.0}\n")
    for t,i,k,p,v in ev: f.write(f"ev {t:.5f} {i} {k} {p} {v}\n")
print(out,len(ev)//2,'notes')
