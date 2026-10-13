import mido, sys, collections
def load(fn):
    m=mido.MidiFile(fn); tpb=m.ticks_per_beat; tracks={}
    for i,t in enumerate(m.tracks):
        name=str(i); abs_=0; on={}; notes=[]
        for msg in t:
            abs_+=msg.time
            if msg.type=='track_name': name=msg.name+f"#{i}"
            if msg.type=='note_on' and msg.velocity>0: on[(msg.channel,msg.note)]=abs_
            elif msg.type in('note_off','note_on'):
                k=(msg.channel,msg.note)
                if k in on: notes.append((on.pop(k),abs_,msg.note))
        if notes: tracks[name]=notes
    return tracks,tpb
def line(notes,step):
    # sample highest and lowest note at each grid point
    end=max(n[1] for n in notes); res={}
    for t in range(0,end,step):
        s=[n[2] for n in notes if n[0]<=t<n[1]]
        if s: res[t]=(max(s),min(s))
    return res
tr,tpb=load(sys.argv[1]); step=tpb//2
lines={}
for k,v in tr.items():
    L=line(v,step); lines[k+'^']={t:a for t,(a,b) in L.items()}; lines[k+'_']={t:b for t,(a,b) in L.items()}
keys=sorted(lines); out=set()
for i,a in enumerate(keys):
    for b in keys[i+1:]:
        if a[:-1]==b[:-1]: continue
        A=lines[a];B=lines[b]; ts=sorted(set(A)&set(B)); prev=None
        for t in ts:
            cur=(A[t],B[t])
            if prev and prev[0]!=cur[0] and prev[1]!=cur[1] and pt==t-step:
                i1=(prev[0]-prev[1])%12; i2=(cur[0]-cur[1])%12
                same=(cur[0]-prev[0])*(cur[1]-prev[1])>0
                if same and i1==i2 and i1 in (0,7) and abs(prev[0]-prev[1])>0 and abs(cur[0]-cur[1])>0:
                    out.add((round(t/tpb,1),a,b,'P8' if i1==0 else 'P5'))
            prev=cur; pt=t
for o in sorted(out): print(*o)
