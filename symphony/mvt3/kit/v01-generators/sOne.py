from g import *
import re
mel=("bes'2.(\\p^\\markup \\italic \"dolce cantabile\" ges'4 | f'4 es'4 ges'4 bes'4 | es''2. des''4 | ces''2 bes'2) | aes'2.( ces''4 | bes'4 aes'4 ges'4 f'4 | ges'2 es'2 | f'1) | "
     "bes'2.( ges'4 | f'4 es'4 ges'4 bes'4\\< | es''2. f''4 | ges''2\\mf f''2)\\> | es''2.(\\p des''4 | ces''4 bes'4 aes'4 ges'4 | f'2 d'2 | es'1) |")
# half-bar harmony: (bass, chord)
H=[('es',['es','ges','bes']),('es',['es','ges','bes']),
   ('d',['bes','d','f','aes']),('es',['es','ges','bes']),
   ('ces',['aes','ces','es']),('ces',['aes','ces','es']),
   ('aes,',['aes','ces','es']),('ges,',['es','ges','bes']),
   ('f,',['f','aes','ces','es']),('f,',['f','aes','ces','es']),
   ('bes,',['bes','d','f']),('bes,',['bes','d','f','aes']),
   ('es',['es','ges','bes']),('aes,',['aes','ces','es']),
   ('bes,',['bes','d','f']),('bes,',['bes','d','f','aes']),
   ('ges,',['es','ges','bes']),('ges,',['es','ges','bes']),
   ('d',['bes','d','f','aes']),('es',['es','ges','bes']),
   ('ges,',['es','ges','bes']),('aes,',['f','aes','ces','es']),
   ('aes,',['aes','ces','es','ges']),('bes,',['bes','d','f']),
   ('ces',['ces','es','ges']),('ces',['ces','es','ges']),
   ('aes,',['aes','ces','es']),('bes,',['bes','d','f','aes']),
   ('bes,',['bes','d','f']),('bes,',['bes','d','f','aes']),
   ('es',['es','ges','bes']),('es',['es','ges','bes'])]
bars=[H[i:i+2] for i in range(0,32,2)]
def pz(lo,hi,idx):
    r=[]
    for b in bars:
        seg=[]
        for bass,ch in b:
            ps=place(ch,lo,hi)
            seg.append(f"r4 {chord(ps[:2])}4")
        r.append(" ".join(seg))
    return r
v2=pz(62,72,0); va=pz(53,63,0)
v2[0]=v2[0].replace("4","4\\pp^\\markup \\italic \"pizz.\"",2).replace("4\\pp^\\markup \\italic \"pizz.\"","4",1)
v2[0]=re.sub(r"^r4","r4",v2[0])
def first(x,txt): return x.replace("4 ","4"+txt+" ",1) if False else x
def basspz(oct):
    r=[]
    for b in bars:
        (b1,c1),(b2,c2)=b
        p1=b1; p2=b2
        if oct: p1=shift(p1,-1); p2=shift(p2,-1)
        r.append(f"{p1}4 r4 {p2}4 r4" if b1!=b2 else f"{p1}4 r4 r2")
    return r
vc=basspz(False); cb=basspz(True)
# sustained winds: Cl 1, Cl 2, Bsn 1 hold chords per half (tied when equal)
def held(lo,hi,pick):
    r=[]
    for b in bars:
        n=[]
        for bass,ch in b:
            ps=place(ch,lo,hi); n.append(ps[pick] if pick<len(ps) else ps[-1])
        r.append(f"{n[0]}1" if n[0]==n[1] else f"{n[0]}2 {n[1]}2")
    return r
out=["% SECOND THEME (theme F2), bars 51-66, E flat minor, Poco meno mosso: the trumpet's soft melody owed since movement I",
"% (cyclic-notes 'Owed' item 1): trumpet 1 alone, undoubled, no timpani and no other brass in its register (Adler PDF 264, 267);",
"% the octave doubling (flute 1) is saved for its climax at 61-62 (Adler PDF 279-281). E flat (III) is a key neither earlier movement uses.",
"% Accompaniment: upper strings pizz. off the beat, cellos and basses pizz. on the beat, clarinets and bassoons sustained pp.",
"% The theme is heard first in minor and then in major (67), the reverse of movement I's second theme (cyclic-notes).",""]
out.append("sOneTptOne = { "+mel.replace("\\p^","\\p^\\markup \\italic \"solo\" ^",0)+" }")
out.append("sOneFluteOne = { R1*10 | r2 r4 f'''4(\\mp | ges'''2 f'''2)\\> | es'''2.(\\p\\! des'''4) | R1*3 | }")
out.append("sOneVlnTwo = { "+" | ".join(v2)+" | }")
va[0]=va[0].replace("4 ","4\\pp^\\markup \\italic \"pizz.\" ",1).replace("r4\\pp^\\markup \\italic \"pizz.\" ","r4 ",1); out.append("sOneVla = { "+" | ".join(va)+" | }")
vc[0]=vc[0].replace("4","4\\pp^\\markup \\italic \"pizz.\"",1); cb[0]=cb[0].replace("4","4\\pp^\\markup \\italic \"pizz.\"",1); out.append("sOneVc = { "+" | ".join(vc)+" | }")
out.append("sOneCb = { "+" | ".join(cb)+" | }")
c1=held(58,67,1); c2=held(54,63,0); b1=held(46,57,1)
for L in (c1,c2,b1): L[0]=re.sub(r"(\d)",lambda m:m.group(1)+"\\pp",L[0],count=1)
out.append("sOneClOne = { "+" | ".join(c1)+" | }")
out.append("sOneClTwo = { "+" | ".join(c2)+" | }")
out.append("sOneBsnOne = { "+" | ".join(b1)+" | }")
s="\\version \"2.24.0\"\n"+"\n".join(out)+"\n"
# pizz/arco markups
s=s.replace("sOneVlnTwo = { r4","sOneVlnTwo = { r4",1)
open('/tmp/m3/v01/sections/sOne.ily','w').write(s)
s=open('/tmp/m3/v01/sections/sOne.ily').read()
s=s.replace('sOneVla = { r4 <ges bes>4 r4','sOneVla = { r4 <ges bes>4\\pp^\\markup \\italic "pizz." r4',1)
open('/tmp/m3/v01/sections/sOne.ily','w').write(s)
