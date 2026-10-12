from g import *
O={}
# 135-138: descending chain of diminished sevenths over a chromatic bass D - D flat - C - B (A&S Unit 31, PDF 570-575), pp crescendo
dims=[['d','f','aes','b'],['des','e','g','bes'],['c','es','ges','a'],['b','d','f','aes']]
def held(lo,hi,pick):
    r=[]
    for ch in dims:
        ps=place(ch,lo,hi); r.append(ps[min(pick,len(ps)-1)]+"1")
    return r
def line(lo,hi,pick,dyn):
    r=held(lo,hi,pick); r[0]=r[0]+dyn; return " | ".join(r)+" |"
A={}
A['VlnOne']="aes''1\\pp\\< | g''1 | ges''1 | f''1\\mf |"
A['VlnTwo']="d''1\\pp\\< | des''1 | c''1 | b'1\\mf |"
A['Vla']="<f' b'>1\\pp\\< | <e' bes'>1 | <es' a'>1 | <d' aes'>1\\mf |"
A['Vc']="d1\\pp\\< | des1 | c1 | b,1\\mf |"
A['Cb']="d,1\\pp\\< | des,1 | c,1 | b,,1\\mf |"
A['ClOne']="b'1\\pp\\< | bes'1 | a'1 | aes'1\\mf |"
A['ClTwo']="f'1\\pp\\< | e'1 | es'1 | d'1\\mf |"
A['BsnOne']="aes1\\pp\\< | g1 | ges1 | f1\\mf |"
A['BsnTwo']="d1\\pp\\< | des1 | c1 | b,1\\mf |"
A['HnThree']="f'1\\pp\\< | e'1 | es'1 | d'1\\mf |"
A['HnFour']="b1\\pp\\< | bes1 | a1 | aes1\\mf |"
# 139-146: B natural in the bass under V (G/B), F1's head on G in imitation: horns 139, oboe/clarinet 141, violins 143, stretto 145
hd="g'2->( d'4. es'8 | f'4-.) es'8( d'8 c'4-.) b4-. |"
B={}
B['HnOne']=hd.replace("->(","->(\\mf",1)+" d''1 | d''1 | "+shift(hd,0)+" g'1\\f | f'1 |"
B['HnTwo']=hd.replace("->(","->(\\mf",1)+" b'1 | b'1 | "+shift(hd,0)+" d'1\\f | d'1 |"
B['OboeOne']="R1*2 | "+shift(hd,1).replace("->(","->(\\mf",1)+" f''1 | f''1 | "+shift(hd,1).replace("->(","->(\\f",1)
B['ClOne']="R1*2 | "+shift(hd,1).replace("->(","->(\\mf",1)+" d''1 | d''1 | "+shift(hd,0).replace("->(","->(\\f",1)
B['FluteOne']="R1*4 | g''1\\mf | aes''1 | "+shift(hd,2).replace("->(","->(\\f",1)
B['VlnOne']="R1*4 | "+shift(hd,1).replace("->(","->(\\f",1)+" "+shift(hd,2)
B['VlnTwo']="R1*4 | "+shift(hd,0).replace("->(","->(\\f",1)+" "+shift(hd,1)
B['Vla']="d'1\\mf | d'1 | f'1 | f'1 | d'1 | d'1 | "+shift(hd,0)
B['Vc']="b,1\\mf~ | b,1~ | b,1~ | b,1~ | b,1~ | b,1~ | b,1\\f~ | b,1 |"
B['Cb']="b,,1\\mf~ | b,,1~ | b,,1~ | b,,1~ | b,,1~ | b,,1~ | b,,1\\f~ | b,,1 |"
B['Cbsn']="R1*4 | b,,1\\mf~ | b,,1~ | b,,1\\f~ | b,,1 |"
B['BsnOne']="f1\\mf | f1 | d'1 | d'1 | f1 | f1 | "+shift(hd,-1).replace("->(","->(\\f",1)
B['BsnTwo']="b,1\\mf | b,1 | b,1 | b,1 | b,1 | b,1 | b,1\\f | b,1 |"
B['HnThree']="d'1\\mf | d'1 | d'1 | d'1 | f'1 | f'1 | f'1\\f | f'1 |"
B['HnFour']="b1\\mf | b1 | b1 | b1 | b1 | b1 | b1\\f | b1 |"
B['TbnOne']="R1*4 | d'1\\mf | d'1 | f'1\\f | f'1 |"
B['TbnTwo']="R1*4 | b1\\mf | b1 | d'1\\f | d'1 |"
B['BassTbn']="R1*4 | g,1\\mf | g,1 | g,1\\f | g,1 |"
B['Timp']="R1*4 | g,4\\mf r4 g,4 r4 | g,4 r4 g,4 r4 | g,4\\f g,4 g,4 g,4 | g,8 g,8 g,8 g,8 g,8 g,8 g,8 g,8 |"
# 147-150: V6/5 ff (B bass), allargando, held; the reprise follows from the inverted V (no root-position V-i in C)
C={}
full={'FluteOne':"f'''1->\\ff | d'''1 | f'''1~ | f'''2. r4 |",'FluteTwo':"d'''1->\\ff | b''1 | d'''1~ | d'''2. r4 |",
'OboeOne':"b''1->\\ff | g''1 | b''1~ | b''2. r4 |",'OboeTwo':"f''1->\\ff | d''1 | f''1~ | f''2. r4 |",'CorAnglais':"d''1->\\ff | b'1 | d''1~ | d''2. r4 |",
'ClOne':"g''1->\\ff | f''1 | g''1~ | g''2. r4 |",'ClTwo':"d''1->\\ff | b'1 | d''1~ | d''2. r4 |",'BassCl':"b,1->\\ff | b,1 | b,1~ | b,2. r4 |",
'BsnOne':"f1->\\ff | g1 | f1~ | f2. r4 |",'BsnTwo':"b,1->\\ff | b,1 | b,1~ | b,2. r4 |",'Cbsn':"b,,1->\\ff | b,,1 | b,,1~ | b,,2. r4 |",
'HnOne':"d''1->\\ff | d''1 | d''1~ | d''2. r4 |",'HnTwo':"b'1->\\ff | b'1 | b'1~ | b'2. r4 |",'HnThree':"g'1->\\ff | g'1 | g'1~ | g'2. r4 |",'HnFour':"f'1->\\ff | f'1 | f'1~ | f'2. r4 |",
'TptOne':"d''1->\\ff | f''1 | d''1~ | d''2. r4 |",'TptTwo':"b'1->\\ff | d''1 | b'1~ | b'2. r4 |",'TptThree':"g'1->\\ff | g'1 | g'1~ | g'2. r4 |",
'TbnOne':"f'1->\\ff | f'1 | f'1~ | f'2. r4 |",'TbnTwo':"d'1->\\ff | d'1 | d'1~ | d'2. r4 |",'BassTbn':"g,1->\\ff | g,1 | g,1~ | g,2. r4 |",'Tuba':"b,,1->\\ff | b,,1 | b,,1~ | b,,2. r4 |",
'Timp':"g,1:32\\ff | g,1:32 | g,1:32~ | g,2.:32 r4 |",
'VlnOne':"<f'' d'''>1->\\ff | <d'' b''>1 | <f'' d'''>1~ | <f'' d'''>2. r4 |",'VlnTwo':"<b' g''>1->\\ff | <g' f''>1 | <b' g''>1~ | <b' g''>2. r4 |",
'Vla':"<d' b'>1->\\ff | <d' g'>1 | <d' b'>1~ | <d' b'>2. r4 |",'Vc':"<b, f>1->\\ff | <b, g>1 | <b, f>1~ | <b, f>2. r4 |",'Cb':"b,,1->\\ff | b,,1 | b,,1~ | b,,2. r4 |"}
insts=['FluteOne','FluteTwo','OboeOne','OboeTwo','CorAnglais','ClOne','ClTwo','BassCl','BsnOne','BsnTwo','Cbsn','HnOne','HnTwo','HnThree','HnFour','TptOne','TptTwo','TptThree','TbnOne','TbnTwo','BassTbn','Tuba','Timp','VlnOne','VlnTwo','Vla','Vc','Cb']
out=["% RETRANSITION, bars 135-150. 135-138: a descending chain of diminished sevenths over the chromatic bass D - D flat - C - B,",
"% arriving on movement I's stop chord B-D-F-A flat at 138 (not resolved to C: that resolution belongs to the C-major arrival at 219).",
"% 139-146: a held G area with B natural in the bass (cyclic-notes, A&S PDF 449, 452-454): theme F1's head on G in imitation,",
"% horns 139, oboe and clarinet 141, violins 143, everyone 145. 147-150: V6/5 ff, allargando; the reprise comes from the inverted V.",""]
for i in insts:
    a=A.get(i,"R1*4 |"); b=B.get(i,"R1*8 |"); c=full.get(i,"R1*4 |")
    out.append(f"retr{i} = {{ {a} {b} {c} }}")
open('/tmp/m3/v01/sections/retr.ily','w').write("\\version \"2.24.0\"\n"+"\n".join(out)+"\n")
