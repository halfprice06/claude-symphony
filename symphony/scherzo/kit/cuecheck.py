import mido, json, sys
W=sys.argv[1]
vars="fluteOne fluteTwo oboeOne oboeTwo corAnglais clOne clTwo bassCl bsnOne bsnTwo cbsn hnOne hnTwo hnThree hnFour tptOne tptTwo tbnOne tbnTwo bassTbn tuba timp harpR harpL vlnOne vlnTwo vla vc cb".split()
m=mido.MidiFile(sys.argv[2]); tpq=m.ticks_per_beat
tr=[t for t in m.tracks if any(x.type=='note_on' for x in t)]
names=[]
for t in m.tracks:
    n=[x.name for x in t if x.type=='track_name']
    if any(x.type=='note_on' for x in t): names.append(n[0] if n else '?')
bars={}
for name,t in zip(names,tr):
    a=0; s=set()
    for x in t:
        a+=x.time
        if x.type=='note_on' and x.velocity>0: s.add(a//(3*tpq)+1)
    bars[name]=s
print(names[:3], len(names))
key={v:v for v in vars}
partvar={"01":"fluteOne","02":"fluteTwo","03":"oboeOne","04":"oboeTwo","05":"corAnglais","06":"clOne","07":"clTwo","08":"bassCl","09":"bsnOne","10":"bsnTwo","11":"cbsn","12":"hnOne","13":"hnTwo","14":"hnThree","15":"hnFour","16":"tptOne","17":"tptTwo","19":"tbnOne","20":"tbnTwo","21":"bassTbn","22":"tuba","23":"timp","25":"harpR","26":"vlnOne","27":"vlnTwo","28":"vla","29":"vc","30":"cb"}
qv={"cueVlnOne":"vlnOne","cueVlnTwo":"vlnTwo","cueVla":"vla","cueVc":"vc","cueFlOne":"fluteOne","cueObOne":"oboeOne","cueClOne":"clOne","cueBsnOne":"bsnOne","cueHnOne":"hnOne","cueTimp":"timp","cueCA":"corAnglais","cueVlnOneLow":"vlnOne","cueClOneLow":"clOne","cueVcHigh":"vc"}
def get(v):
    for k in bars:
        if k.startswith(v) or v in k: return bars[k]
    return None
cues=json.load(open(W+"/parts-cues.json"))
for p,cl in sorted(cues.items()):
    own=get(partvar[p]) if p!="25" else (get("harpR")|get("harpL"))
    for c in cl:
        q,lab,d,b,n=c[:5]
        src=get(qv[q]); rng=range(b,b+n)
        sounding=[x for x in rng if x in src]
        ownin=[x for x in rng if x in own]
        nxt=min([x for x in own if x>=b+n] or [0])
        prev=max([x for x in own if x<b] or [0])
        print(f"{p} {partvar[p]:10s} {lab:14s} {b}-{b+n-1}: source sounds in {sounding}; part plays in cue bars {ownin}; prev own {prev}, next entry {nxt} (gap {nxt-(b+n)})")
