from g import *
import re
def load(fn,pre):
    d={}
    for line in open(fn):
        m=re.match(pre+r"([A-Za-z]+) = \{ (.*) \}\s*$",line)
        if m: d[m.group(1)]=m.group(2)
    return d
A=load('/tmp/m3/v01/sections/sOne.ily','sOne'); B=load('/tmp/m3/v01/sections/sTwo.ily','sTwo')
T=lambda x: transpose(x,-2,-3)
bars=lambda x:[b.strip() for b in x.split("|") if b.strip()]
O={}
# part 1: 171-186, C minor: muted trumpet 1 doubling the cor anglais
mel=T(A['TptOne']).replace('^\\markup \\italic "dolce cantabile"','^\\markup \\italic "con sord., dolce cantabile"')
O['TptOne']=bars(mel)
O['CorAnglais']=bars(T(A['TptOne']))
fl=bars(T(A['FluteOne'])); O['OboeOne']=[shift(b,-1) if b.startswith(('r','R')) is False else b for b in fl]
O['OboeOne']=bars(shift(T(A['FluteOne']),-1))
for k in ['VlnTwo','Vla','Vc','Cb','ClOne','ClTwo','BsnOne']:
    O[k]=bars(T(A[k]))
# deceptive cadence at 186: bass A flat under the melody's C
O['Vc'][15]="aes,4 r4 r2"; O['Cb'][15]="aes,,4 r4 r2"; O['BsnOne'][15]=O['BsnOne'][15]
O['Vla'][15]="r4 <aes c'>4 r4 <aes c'>4"; O['VlnTwo'][15]="r4 <c' es'>4 r4 <c' es'>4"
O['ClTwo'][15]="es1"; O['BsnOne'][15]="aes,1"
# part 2: 187-198, C major, first 8 bars of the E flat major statement transposed, then 4 bars that turn to the flat sixth
P2={}
for k in ['VlnOne','VlnTwo','Vc','Vla','Cb','BsnTwo','HarpR','HarpL','ClOne','ClTwo','BsnOne']:
    P2[k]=bars(T(B[k]))[:8]
P2['VlnOne']+= ["g''2.( e''4","d''4 c''4 e''4 g''4\\<","c'''2. d'''4","es'''1)\\f"]
P2['VlnTwo']+= ["g'2.( e'4","d'4 c'4 e'4 g'4\\<","c''2. d''4","es''1)\\f"]
P2['Vc']+=     ["e2( f4 g4","f2 e2)","g2( c'4 d'4","c'1)"]
P2['Cb']+=     ["e,1","b,,2 c,2","e,2 f,2","aes,,1"]
P2['BsnTwo']+= ["e1","b,2 c2","e2 f2","aes,1"]
P2['Vla']+=    ["r4 <g c'>4 r4 <g c'>4","r4 <f g>4 r4 <g c'>4","r4 <g c'>4 r4 <a c'>4","r4 <aes c'>4 r4 <aes es'>4"]
P2['HarpR']+=  ["c'8 e' g' c'' c' e' g' c''","d'8 f' g' b' c' e' g' c''","c'8 e' g' c'' c'8 f' a' d''","c'8 es' aes' c'' c'8 es' aes' es''"]
P2['HarpL']+=  ["e,1","b,,2 c,2","e,2 f,2","aes,,1"]
P2['ClOne']+=  ["c'1","b2 c'2","c'2 c'2","c'1"]
P2['ClTwo']+=  ["g1","g2 g2","g2 a2","aes1"]
P2['BsnOne']+= ["c1","d2 c2","c2 c2","es1"]
P2['HnOne']=["R1*8","c'1\\p","d'2 c'2","e'2 f'2","es'1"]
P2['HnTwo']=["R1*8","g1\\p","g2 g2","c'2 a2","aes1"]
P2['FluteOne']=["R1*10","c'''2.(\\mp d'''4","es'''1)\\f"]
P2['OboeOne']=["R1*10","c''2.(\\mp d''4","es''1)\\f"]
insts=['FluteOne','OboeOne','CorAnglais','ClOne','ClTwo','BsnOne','BsnTwo','HnOne','HnTwo','TptOne','HarpR','HarpL','VlnOne','VlnTwo','Vla','Vc','Cb']
out=["% SECOND THEME IN THE RECAPITULATION, bars 171-198. 171-186: theme F2 in C minor, muted trumpet 1 in unison with the cor anglais",
"% (cyclic-notes 'Owed' item 1: on a repeat, a muted trumpet doubling the cor anglais); oboe 1 doubles the climax at the octave (181-183).",
"% Accompaniment as at 51. Deceptive cadence at 186 (V - VI): the C-major statement starts from A flat.",
"% 187-198: theme F2 in C major in the violins with the cellos' counter-melody (as at 67, a minor third lower); its consequent turns",
"% to E flat over A flat (mixture, 198), and the coda's C-minor tutti follows. Movement I's withheld sounds stay for the coda.",""]
for i in insts:
    p1=O.get(i,["R1*16"]); p2=P2.get(i,["R1*12"])
    body=" | ".join(p1)+" | "+" | ".join(p2)+" |"
    if i=="Cb": body=raise_below(body,28)
    out.append(f"recS{i} = {{ {body} }}")
open('/tmp/m3/v01/sections/recS.ily','w').write("\\version \"2.24.0\"\n"+"\n".join(out)+"\n")
