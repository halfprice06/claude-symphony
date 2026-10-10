import mido, collections, sys
mf=mido.MidiFile('build/all.midi'); tpb=mf.ticks_per_beat
names=['fluteOne','fluteTwo','oboeOne','oboeTwo','corAnglais','clOne','clTwo','bassCl','bsnOne','bsnTwo','cbsn','hnOne','hnTwo','hnThree','hnFour','tptOne','tptTwo','tptThree','tbnOne','tbnTwo','bassTbn','tuba','timp','harpR','harpL','vlnOne','vlnTwo','vla','vc','cb']
N=[]
for i,t in enumerate(mf.tracks[1:]):
    tm=0; on={}
    for m in t:
        tm+=m.time
        if m.type=='note_on' and m.velocity>0: on.setdefault(m.note,[]).append(tm)
        elif m.type in('note_off','note_on') and on.get(m.note):
            s=on[m.note].pop(0); N.append((s/tpb,tm/tpb,m.note,names[i]))
nm=lambda p: ['C','Db','D','Eb','E','F','F#','G','Ab','A','Bb','B'][p%12]+str(p//12-1)
res=collections.defaultdict(set)
T=max(e for s,e,p,n in N)
t=0
while t<T:
    held=[(p,n,s,e) for s,e,p,n in N if s<=t and e>=t+1 and n not in('timp','harpR','harpL')]
    for i in range(len(held)):
        for j in range(len(held)):
            a,b=held[i],held[j]
            if a[0]<b[0] and (b[0]-a[0]) in (1,11,13,23) :
                res[int(t//4)+1].add(f"{a[1]}{nm(a[0])}/{b[1]}{nm(b[0])}@{t%4+1:.0f}")
    t+=1
for b in sorted(res): print(b, ' '.join(sorted(res[b])))
