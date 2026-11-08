import sys, collections, statistics as st, bisect
L=open(sys.argv[1],errors='replace').read().replace('\r','').split('\n')
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
def parse(ev):
    notes=[];on={};cc1=[]
    for t,s,a,b in ev:
        ty=s&0xF0
        if ty==0x90 and b>0: on.setdefault(a,[]).append((t,b))
        elif ty==0x80 or (ty==0x90 and b==0):
            if on.get(a): t0,v=on[a].pop(0); notes.append((t0,t,a,v))
        elif ty==0xB0 and a==1: cc1.append((t,b))
    notes.sort(); cc1.sort()
    return [n for n in notes if n[2]>=24], cc1
def ccat(cc,t):
    k=bisect.bisect_right([c[0] for c in cc],t)-1
    return cc[k][1] if k>=0 else None
offs=[-400,-200,-100,-50,0,50,100,200,400,800]
agg={'phrase_start':collections.defaultdict(list),'legato_cont':collections.defaultdict(list)}
ends=collections.defaultdict(list)
longs=[]; shortcorr=[]
for name,ev in items:
    notes,cc=parse(ev)
    if len(cc)<50 or not notes: 
        continue
    times=[c[0] for c in cc]
    for k,n in enumerate(notes):
        prev_end=max([m[1] for m in notes[:k]],default=-10**9)
        gap=(n[0]-prev_end)*MSPT
        kind='phrase_start' if gap>150 else 'legato_cont'
        base=ccat(cc,n[0])
        if base is None: continue
        for o in offs:
            v=ccat(cc,n[0]+o/MSPT)
            if v is not None: agg[kind][o].append(v-base)
        agg[kind]['abs'].append(base)
        # phrase end: next onset gap > 150ms after this note's end
        nxt=notes[k+1][0] if k+1<len(notes) else 10**9
        if (nxt-n[1])*MSPT>150:
            e=ccat(cc,n[1])
            for o in (-1000,-500,-250,0,250):
                v=ccat(cc,n[1]+o/MSPT)
                if v is not None and e is not None: ends[o].append(v-e)
            ends['abs'].append(e)
        dur=(n[1]-n[0])*MSPT
        if dur>1200:
            seg=[c for c in cc if n[0]<=c[0]<=n[1]]
            if len(seg)>=3:
                vals=[c[1] for c in seg]; s0=ccat(cc,n[0]); 
                pk=max(range(len(seg)),key=lambda j:seg[j][1]); tr=min(range(len(seg)),key=lambda j:seg[j][1])
                longs.append((name[:28],round(dur),s0,max(vals),vals[-1],round((seg[pk][0]-n[0])/(n[1]-n[0]),2),min(vals)))
        # velocity vs cc1
        shortcorr.append((n[3],base,name))
print("CC1 change relative to the value at note onset (median, IQR) -- tracks with dense CC1")
for kind in agg:
    print(f"\n{kind}: n={len(agg[kind]['abs'])}, CC1 at onset median {st.median(agg[kind]['abs'])}")
    for o in offs:
        v=sorted(agg[kind][o]); 
        if len(v)>4: print(f"  {o:+5d} ms: med {st.median(v):+.0f}  IQR {v[len(v)//4]:+d}..{v[3*len(v)//4]:+d}")
print(f"\nphrase ends (relative to CC1 at note-off), n={len(ends['abs'])}, CC1 at note-off median {st.median(ends['abs'])}")
for o in (-1000,-500,-250,0,250):
    v=sorted(ends[o]); print(f"  {o:+5d} ms: med {st.median(v):+.0f} IQR {v[len(v)//4]:+d}..{v[3*len(v)//4]:+d}")
print("\nlong notes (>1.2 s): track, dur ms, CC1 start, peak, end, peak position (0-1), min")
for x in longs: print('  ',x)
# velocity vs cc1 correlation
import math
def corr(a,b):
    ma,mb=st.mean(a),st.mean(b); sa=math.sqrt(sum((x-ma)**2 for x in a)); sb=math.sqrt(sum((y-mb)**2 for y in b))
    return sum((x-ma)*(y-mb) for x,y in zip(a,b))/(sa*sb) if sa and sb else float('nan')
print("\nvelocity vs CC1-at-onset correlation, all dense-CC1 notes:", round(corr([s[0] for s in shortcorr],[s[1] for s in shortcorr]),2))
