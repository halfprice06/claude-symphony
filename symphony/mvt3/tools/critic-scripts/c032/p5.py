import mido, sys
fn=sys.argv[1]
m=mido.MidiFile(fn); tpb=m.ticks_per_beat
tracks={}
for i,t in enumerate(m.tracks):
    name=str(i); ab=0; on={}; ns=[]
    for msg in t:
        ab+=msg.time
        if msg.type=='track_name': name=msg.name.replace('Â·','.')+f'#{i}'
        if msg.type=='note_on' and msg.velocity>0: on[(msg.channel,msg.note)]=ab
        elif msg.type in('note_off','note_on'):
            k=(msg.channel,msg.note)
            if k in on: ns.append((on.pop(k),ab,msg.note))
    if ns and not any(x in name for x in ('Timp','Perc','Cymb','Drum','Harp')): tracks[name]=ns
step=tpb//2
N=['C','C#','D','Eb','E','F','F#','G','Ab','A','Bb','B']
def nm(p): return N[p%12]+str(p//12-1)
lines={}
for k,v in tracks.items():
    end=max(n[1] for n in v)
    hi={};lo={}
    for t in range(0,end,step):
        s=[n[2] for n in v if n[0]<=t<n[1]]
        if s: hi[t]=max(s); lo[t]=min(s)
    lines[k+'^']=hi; lines[k+'_']=lo
keys=sorted(lines); out={}
for i,a in enumerate(keys):
    for b in keys[i+1:]:
        if a[:-1]==b[:-1]: continue
        A=lines[a];B=lines[b]
        for t in sorted(set(A)&set(B)):
            tp=t-step
            if tp in A and tp in B:
                a0,b0,a1,b1=A[tp],B[tp],A[t],B[t]
                if a0==a1 or b0==b1: continue
                if (a1-a0)*(b1-b0)<=0: continue
                h0,l0=max(a0,b0),min(a0,b0); h1,l1=max(a1,b1),min(a1,b1)
                if (h0-l0)%12==7 and (h1-l1)%12==7 and (a0>b0)==(a1>b1):
                    bar=t//tpb//4+1; beat=(t/tpb)%4+1
                    out.setdefault((bar,beat),[]).append(f"{a[:-1].split('#')[0]} {nm(a0)}->{nm(a1)} / {b[:-1].split('#')[0]} {nm(b0)}->{nm(b1)}")
for k in sorted(out):
    print(k, len(out[k])); 
    for x in sorted(set(out[k]))[:6]: print('   ',x)
