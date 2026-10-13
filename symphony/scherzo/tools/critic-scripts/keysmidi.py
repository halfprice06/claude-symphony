import mido, music21 as m21, collections
mf=mido.MidiFile('build/all.midi'); tpb=mf.ticks_per_beat
notes=[]
for i,t in enumerate(mf.tracks[1:]):
    if i in (22,): continue  # timp
    tm=0; on={}
    for m in t:
        tm+=m.time
        if m.type=='note_on' and m.velocity>0: on.setdefault(m.note,[]).append(tm)
        elif m.type in('note_off','note_on') and on.get(m.note):
            s=on[m.note].pop(0); notes.append((s/tpb/4+1,(tm-s)/tpb,m.note))
kk=m21.analysis.discrete.KrumhanslSchmuckler()
for st in range(1,181,4):
    w=[0]*12
    for b,d,p in notes:
        if st<=b<st+4: w[p%12]+=d
    sol=kk.getSolution(m21.stream.Stream([m21.note.Note(m21.pitch.Pitch(midi=60+i),quarterLength=max(w[i],0.0001)) for i in range(12) if w[i]>0]))
    print(st,st+3,sol)
