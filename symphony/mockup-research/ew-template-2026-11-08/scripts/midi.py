import sys, re, collections, statistics as st
L=open(sys.argv[1],errors='replace').read().replace('\r','').split('\n')
PPQ=480; MSPT=60000/130/PPQ
tracks=[]; cur=None; i=0
while i<len(L):
    l=L[i]
    if l.startswith('  <TRACK'): cur={'name':None,'ev':[]}; tracks.append(cur)
    elif l.startswith('    NAME ') and cur and cur['name'] is None: cur['name']=l[9:].strip('"')
    elif l.strip()=='<SOURCE MIDI':
        t=0; i+=1
        while L[i].strip()!='>':
            p=L[i].split()
            if p and p[0] in('E','e'):
                t+=int(p[1]); cur['ev'].append((t,int(p[2],16),int(p[3],16),int(p[4],16)))
            elif p and p[0] in ('X','x'):
                t+=int(p[1])
            elif p and p[0] in ('<X','<x'):
                t+=int(p[1]); i+=1
                while L[i].strip()!='>': i+=1
            i+=1
    i+=1
out=[]
for tr in tracks:
    ev=tr['ev']
    if not ev: continue
    notes=[];on={}
    cc=collections.defaultdict(list)
    for t,s,a,b in ev:
        typ=s&0xF0
        if typ==0x90 and b>0: on.setdefault(a,[]).append((t,b))
        elif typ==0x80 or (typ==0x90 and b==0):
            if on.get(a): t0,v=on[a].pop(0); notes.append((t0,t,a,v))
        elif typ==0xB0: cc[a].append((t,b))
        elif typ==0xE0: cc['PB'].append((t,b))
    notes.sort()
    if not notes and not cc: continue
    print(f"\n### {tr['name']}: {len(notes)} notes")
    # keyswitch notes (below C0=24?) heuristically pitch<24
    ks=[n for n in notes if n[2]<24]; real=[n for n in notes if n[2]>=24]
    if ks: print(f"  keyswitch-range notes (<C0): {len(ks)} pitches {sorted(set(n[2] for n in ks))}")
    if real:
        vel=[n[3] for n in real]
        print(f"  velocity: min {min(vel)} med {st.median(vel)} max {max(vel)} distinct {len(set(vel))}")
        # onset offset from 16th grid
        off=[]
        for n in real:
            g=PPQ//4; d=n[0]%g; d=d if d<=g/2 else d-g; off.append(d*MSPT)
        on_grid=sum(1 for o in off if abs(o)<1)/len(off)
        print(f"  onset vs 16th grid: {on_grid*100:.0f}% exactly on grid; offset ms med {st.median(off):+.1f}, mean {st.mean(off):+.1f}, range {min(off):+.0f}..{max(off):+.0f}")
        # overlaps / gaps between successive notes (monophonic-ish lines)
        ov=[]; gaps=[]
        for a,b in zip(real,real[1:]):
            if b[0]>a[0]:
                d=(a[1]-b[0])*MSPT
                if d>0: ov.append(d)
                else: gaps.append(-d)
        if ov: print(f"  overlaps into next note: {len(ov)} med {st.median(ov):.0f} ms")
        if gaps: print(f"  gaps before next note: {len(gaps)} med {st.median(gaps):.0f} ms, min {min(gaps):.0f}")
        # repeated same pitch notes
        rep=[(b[0]-a[1])*MSPT for a,b in zip(real,real[1:]) if a[2]==b[2] and b[0]>=a[0]]
        if rep: print(f"  repeated-pitch pairs: {len(rep)} gap med {st.median(rep):.0f} ms min {min(rep):.0f} max {max(rep):.0f}")
        durs=[(n[1]-n[0])*MSPT for n in real]
        print(f"  durations ms med {st.median(durs):.0f} min {min(durs):.0f} max {max(durs):.0f}")
    for k,v in sorted(cc.items(),key=lambda x:str(x[0])):
        vals=[x[1] for x in v]; span=(v[-1][0]-v[0][0])*MSPT/1000 if len(v)>1 else 0
        print(f"  CC{k}: {len(v)} events, range {min(vals)}..{max(vals)}, med {st.median(vals)}, density {len(v)/span if span else 0:.1f}/s")
