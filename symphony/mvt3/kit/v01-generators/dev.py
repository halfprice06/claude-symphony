from g import *
import re
# DEVELOPMENT, bars 99-134 (36 bars)
# 99-106: call and response: strings play F1's head (F minor 99-100, B flat minor 103-104), woodwinds answer with motive x (101-102, 105-106)
# 107-110: lament bass F-E-E flat-D-D flat-C (i - V6 - v6 - IV6 - iv6 - V) with 7-6 suspensions in the violins (A&S Unit 31)
# 111-114: cadence in F minor (root V-i allowed outside C), then F rises to F sharp: D7, V of G
# 115-122: G minor, bassoon 1 solo on theme F2 over pizzicato strings; 123-130: G major, theme F2 in the harp alone (its first melodic line)
# 131-134: cadence in G (D7-G, f), the development's own cadence in one held key (cyclic-notes: G, never a key in movement I)
O={}
headF="f2->( c4. des8 | es4-.) des8( c8 bes,4-.) aes,4-. |"
headBb="bes2->( f4. ges8 | aes4-.) ges8( f8 es4-.) des4-. |"
xF="r4 c'''8( bes'' aes'' g'' f'' e'' | f''8 g'' aes'' bes'' c'''4->) c''4-> |"
xBb="r4 f'''8( es''' des''' c''' bes'' a'' | bes''8 c''' des''' es''' f'''4->) f''4-> |"
# strings: Vc/Cb/Vla head; brass punctuations on F minor / B flat minor chords
O['VcA']=shift(headF,0).replace("->(","->(\\f",1)+" <f c'>4-. r4 r2 | R1 | "+headBb+" <bes f'>4-. r4 r2 | R1 |"
O['CbA']=shift(headF,-1).replace("->(","->(\\f",1)+" f,4-. r4 r2 | R1 | "+shift(headBb,-1)+" bes,,4-. r4 r2 | R1 |"
O['VlaA']=shift(headF,1).replace("->(","->(\\f",1)+" <aes c'>4-. r4 r2 | R1 | "+shift(headBb,1)+" <des' f'>4-. r4 r2 | R1 |"
O['BsnTwoA']=O['VcA'].replace("<f c'>","f").replace("<bes f'>","bes,")
O['HnThreeA']="c'4->\\f r4 r2 | R1*3 | f'4-> r4 r2 | R1*3 |"
O['HnFourA']="aes4->\\f r4 r2 | R1*3 | des'4-> r4 r2 | R1*3 |"
O['TbnOneA']="c'4->\\f r4 r2 | R1*3 | des'4-> r4 r2 | R1*3 |"
O['TbnTwoA']="aes4->\\f r4 r2 | R1*3 | bes4-> r4 r2 | R1*3 |"
O['BassTbnA']="f,4->\\f r4 r2 | R1*3 | bes,,4-> r4 r2 | R1*3 |"
O['TimpA']="c4->\\f r4 r2 | R1*7 |"
# woodwind answers (motive x), in octaves Fl 1 / Ob 1 / Cl 1
O['FluteOneA']="R1*2 | "+xF.replace("8(","8(\\mf",1)+" R1*2 | "+xBb+""
O['OboeOneA']="R1*2 | "+shift(xF,-1).replace("8(","8(\\mf",1)+" R1*2 | "+shift(xBb,-1)+""
O['ClOneA']="R1*2 | "+shift(xF,-1).replace("8(","8(\\mf",1)+" R1*2 | "+shift(xBb,-1)+""
O['BsnOneA']="R1*2 | e1\\mf | e2 e2 | R1*2 | a1 | a2 a2 |"
O['ClTwoA']="R1*2 | e'1\\mf | f'2 e'2 | R1*2 | a'1 | bes'2 a'2 |"
O['HnOneA']="R1*2 | g'1\\mp | aes'2 g'2 | R1*2 | c''1 | des''2 c''2 |"
O['HnTwoA']="R1*2 | e'1\\mp | f'2 e'2 | R1*2 | a'1 | bes'2 a'2 |"
# 107-110 lament bass with 7-6 suspensions; 111-114 cadence and turn to D7
O['VcB']="f2\\p\\< e2 | es2 d2 | des2 c2 | c1\\f | f2 des2 | bes,2 c2 | f2-> r2 | d1\\> |"
O['CbB']="f,2\\p\\< e,2 | es,2 d,2 | des,2 c,2 | c,1\\f | f,2 des,2 | bes,,2 c,2 | f,2-> r2 | d,1\\> |"
O['BsnTwoB']="f2\\p\\< e2 | es2 d2 | des2 c2 | c1\\f | f2 des2 | bes,2 c2 | f2-> r2 | d1\\> |"
O['CbsnB']="f,2\\p\\< e,2 | es,2 d,2 | des,2 c,2 | c,1\\f | f,2 des,2 | bes,,2 c,2 | f,2-> r2 | R1 |"
O['VlnOneB']="c'''1~\\p\\< | c'''2 c'''4( bes''4)~ | bes''2 bes''4( g''4) | g''1\\f | aes''2( f''2 | f''2 e''2) | f''2-> r2 | fis''1\\> |"
O['VlnTwoB']="aes''1~\\p\\< | aes''2 g''2~ | g''2 f''4( e''4) | e''1\\f | c''2( des''2 | des''2 c''2) | c''2-> r2 | c''1\\> |"
O['VlaB']="c'2\\p\\< c'2 | c'2 bes2 | bes2 bes2 | g1\\f | aes2( aes2 | g2 g2) | aes2-> r2 | a1\\> |"
O['HnOneB']="R1*3 | g'1\\f | aes'2 aes'2 | bes'2 g'2 | aes'2-> r2 | R1 |"
O['HnTwoB']="R1*3 | e'1\\f | f'2 f'2 | f'2 e'2 | f'2-> r2 | R1 |"
O['TbnOneB']="R1*3 | c'1\\f | c'2 des'2 | des'2 c'2 | c'2-> r2 | R1 |"
O['TbnTwoB']="R1*3 | g1\\f | aes2 aes2 | f2 g2 | aes2-> r2 | R1 |"
O['BassTbnB']="R1*3 | c1\\f | f,2 des2 | bes,,2 c2 | f,2-> r2 | R1 |"
O['TimpB']="R1*3 | c4\\f r4 c4 r4 | R1 | R1 | c4-> r4 r2 | R1 |"
O['FluteOneB']="R1*3 | g''1\\f | aes''2 f''2 | f''2 e''2 | f''2-> r2 | R1 |"
O['OboeOneB']="R1*3 | e''1\\f | f''2 des''2 | des''2 c''2 | c''2-> r2 | R1 |"
O['ClOneB']="R1*3 | c''1\\f | c''2 aes'2 | bes'2 g'2 | aes'2-> r2 | R1 |"
O['BsnOneB']="R1*3 | e1\\f | c2 f2 | f2 e2 | c2-> r2 | R1 |"
# 115-122 G minor, bassoon 1 solo (theme F2 transposed from E flat minor up a major third)
f2g="d'2.(\\p^\\markup \\italic \"solo, espress.\" bes4 | a4 g4 bes4 d'4 | g'2. f'4 | es'2 d'2) | c'2.( es'4 | d'4 c'4 bes4 a4 | bes2 g2 | a1) |"
O['BsnOneC']=f2g
H1=[('g,',['g','bes','d']),('fis,',['d','fis','a','c']),('es,',['es','g','bes']),('c,',['c','es','g']),('a,',['a','c','es']),('d,',['d','fis','a']),('g,',['g','bes','d']),('d,',['d','fis','a','c'])]
def pzr(lo,hi,dyn=""):
    r=[]
    for k,(b,ch) in enumerate(H1):
        ps=place(ch,lo,hi)[:2]; r.append(f"r4 {chord(ps)}4{dyn if k==0 else ''} r4 {chord(ps)}4")
    return " | ".join(r)+" |"
O['VlnTwoC']=pzr(62,70,"\\pp^\\markup \\italic \"pizz.\"")
O['VlaC']=pzr(55,64,"\\pp^\\markup \\italic \"pizz.\"")
O['VcC']=" | ".join(f"{b.replace(',','')}4{'\\pp^\\markup \\italic \"pizz.\"' if k==0 else ''} r4 r2" for k,(b,ch) in enumerate(H1))+" |"
O['CbC']=" | ".join(f"{b}4{'\\pp^\\markup \\italic \"pizz.\"' if k==0 else ''} r4 r2" for k,(b,ch) in enumerate(H1))+" |"
O['ClOneC']="bes1\\pp | a1 | bes1 | g1 | a1 | a1 | bes1 | fis1 |"
O['ClTwoC']="g1\\pp | fis1 | g1 | es1 | es1 | fis1 | g1 | c'1 |"
# 123-130 G major, harp melody (F2 in G major), soft strings and horn
f2G="d''2.( b'4 | a'4 g'4 b'4 d''4 | g''2. fis''4 | e''2 d''2) | c''2.( e''4 | d''4 c''4 b'4 a'4 | b'2 g'2 | a'1) |"
H2=[['g','b','d'],['d','fis','a','c'],['e','g','b'],['c','e','g'],['a','c','e'],['d','fis','a'],['g','b','d'],['d','fis','a','c']]
O['HarpRC']="R1*8 | "+re.sub(r"(\d)",lambda m:m.group(1),f2G.replace("2.(","2.(^\\markup \\italic \"solo, cantabile\"",1).replace("(","").replace(")",""),count=0)
lh=[]
for ch in H2:
    ps=place(ch,43,60)[:4]
    lh.append(" ".join(f"{p}8" for p in ps)+" "+" ".join(f"{p}8" for p in ps))
O['HarpLC']="R1*8 | "+lh[0].replace("8","8\\p",1)+" | "+" | ".join(lh[1:])+" |"
O['VlnTwoD']="b'1\\pp^\\markup \\italic \"arco\" | c''1 | b'1 | c''1 | c''1 | c''1 | b'1 | c''1 |"
O['VlaD']="g'1\\pp^\\markup \\italic \"arco\" | fis'1 | g'1 | g'1 | e'1 | fis'1 | g'1 | fis'1 |"
O['VcD']="g1\\pp^\\markup \\italic \"arco\" | d1 | e1 | c1 | a,1 | d1 | g1 | d1 |"
O['CbD']="g,1\\pp^\\markup \\italic \"arco\" | d,1 | e,1 | c,1 | a,,1 | d,1 | g,1 | d,1 |"
O['HnOneD']="R1*4 | e'1\\pp | fis'2( a'2) | g'1 | fis'1 |"
# 131-134 cadence in G, f; then G held, diminuendo, G7 at 134
O['VlnOneE']="r4 a''8(\\f b'' c''' d''' e''' fis''' | g'''4->) d'''4-> b''4-> g''4-> | g''1\\>~ | g''2. r4\\p |"
O['VlnTwoE']="r4 fis'8(\\f g' a' b' c'' d'' | d''4->) b'4-> g'4-> d'4-> | d''1\\>~ | d''2. r4\\p |"
O['VlaE']="<d' a'>2\\f <c' a'>2 | <d' b'>4-> r4 r2 | b1\\>~ | b2. r4\\p |"
O['VcE']="d2\\f d2 | g,4-> r4 r2 | g1\\>~ | g2. r4\\p |"
O['CbE']="d,2\\f d,2 | g,,4-> r4 r2 | g,1\\>~ | g,2. r4\\p |"
O['FluteOneE']="a''1\\f | g''4-> r4 r2 | R1*2 |"
O['OboeOneE']="fis''2\\f c''2 | b'4-> r4 r2 | R1*2 |"
O['ClOneE']="d''2\\f fis'2 | g'4-> r4 r2 | R1*2 |"
O['BsnOneE']="c'2\\f a2 | b4-> r4 r2 | R1*2 |"
O['BsnTwoE']="d2\\f d2 | g,4-> r4 r2 | R1*2 |"
O['HnOneE']="a'1\\f | g'4-> r4 r2 | R1*2 |"
O['HnTwoE']="fis'2\\f fis'2 | g'4-> r4 r2 | R1*2 |"
O['HnThreeE']="d'1\\f | d'4-> r4 r2 | d'1\\>~ | d'2. r4\\p |"
O['HnFourE']="c'1\\f | b4-> r4 r2 | b1\\>~ | b2. r4\\p |"
O['VlnOneC']="R1*8\\! |"; O['BsnTwoC']="R1*8\\! |"
O['TimpE']="R1 | g,4->\\f r4 r2 | R1*2 |"
O['HarpRE']="R1*4 |"; O['HarpLE']="R1*4 |"
def cat(inst,parts,lens):
    s=[]
    for p,n in zip(parts,lens):
        k=inst+p
        s.append(O[k] if k in O else f"R1*{n} |")
    return " ".join(s)
parts=['A','B','C','D','E']; lens=[8,8,8,12,4]
# D is 8 bars of material for some, but the section is 12 (123-130 = 8 bars + ...). fix: C=115-122 (8), D=123-130 (8), E=131-134 (4); total 36 = 8+8+8+8+4
lens=[8,8,8,8,4]
insts=['FluteOne','FluteTwo','OboeOne','OboeTwo','CorAnglais','ClOne','ClTwo','BassCl','BsnOne','BsnTwo','Cbsn','HnOne','HnTwo','HnThree','HnFour','TptOne','TptTwo','TptThree','TbnOne','TbnTwo','BassTbn','Tuba','Timp','HarpR','HarpL','VlnOne','VlnTwo','Vla','Vc','Cb']
# harp RH/LH: section C has its material placed as 'R1*8 | ...' -> it is meant for D; move
O['HarpRD']=O.pop('HarpRC').replace("R1*8 | ",""); O['HarpLD']=O.pop('HarpLC').replace("R1*8 | ","")
out=["% DEVELOPMENT, bars 99-134.",
"% 99-106: call and response between strings (theme F1's head, F minor 99, B flat minor 103) and woodwinds (motive x, 101, 105).",
"% 107-110: lament bass F-E-E flat-D-D flat-C (i - V6 - v6 - IV6 - iv6 - V) with 7-6 suspensions in the violins (A&S Unit 31, PDF 551-583).",
"% 111-114: cadence in F minor; the bass rises F - F sharp (D7, V of G). 115-122: G minor, bassoon 1 solo on theme F2 over pizzicato strings",
"% (movement I gives the bassoon only short solos, cyclic-notes critic 54). 123-130: G major, theme F2 in the harp alone (its first melodic",
"% line in the symphony, cyclic-notes 'Still unused'). 131-134: cadence in G (D7-G, f): the development holds one key with its own cadence.",""]
for i in insts:
    body=cat(i,parts,lens)
    if all(f"{i}{p}" not in O for p in parts): continue
    out.append(f"dev{i} = {{ {body} }}")
open('/tmp/m3/v01/sections/dev.ily','w').write("\\version \"2.24.0\"\n"+"\n".join(out)+"\n")
