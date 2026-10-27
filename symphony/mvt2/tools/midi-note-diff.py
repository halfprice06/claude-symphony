import sys, mido, collections
def barmap():
    secs=[l.split() for l in open('/home/user/claude_composes/symphony/mvt2/v340/sections.txt') if l.strip()]
    b=[]; q=0
    for n,bars,qp in secs:
        for i in range(int(bars)): b.append(q); q+=int(qp)
    return b
B=barmap()
def pos(qn):
    import bisect
    i=bisect.bisect_right(B,qn+1e-6)-1
    return i+1, round(qn-B[i]+1,3)
N='C C# D Eb E F F# G Ab A Bb B'.split()
def pn(n): return f"{N[n%12]}{n//12-1}"
def load(p):
    m=mido.MidiFile(p); tpb=m.ticks_per_beat; out=set()
    for tr in m.tracks:
        name='';t=0;on={}
        for msg in tr:
            t+=msg.time
            if msg.type=='track_name': name=msg.name
            if msg.type=='note_on' and msg.velocity>0: on.setdefault((msg.channel,msg.note),[]).append(t)
            elif msg.type in('note_off','note_on'):
                k=(msg.channel,msg.note)
                if on.get(k):
                    s=on[k].pop(0); out.add((name,s/tpb,msg.note,round((t-s)/tpb,3)))
    return out
a=load(sys.argv[1]); b=load(sys.argv[2])
rows=[]
for x in a-b: rows.append((x[1],'-',x))
for x in b-a: rows.append((x[1],'+',x))
rows.sort()
for q,s,(nm,st,p,d) in rows:
    bar,bt=pos(st); print(f"{bar:3d} b{bt:<6} {s} {nm:20s} {pn(p):4s} dur {d}")
