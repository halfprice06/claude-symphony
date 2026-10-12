from g import *
import re
def W(name,d,comment):
    lines=["\\version \"2.24.0\""]+comment+[""]+[f"{name}{k} = {{ {v} }}" for k,v in d.items()]
    open(f'/tmp/m3/v01/sections/{name}.ily','w').write("\n".join(lines)+"\n")
rep=lambda p,n=8: " ".join([f"{p}8"]*n)
# ---------- codaOne 199-210 ----------
P_hi="r8 g''8( es'''4.->) d'''8( des'''8 c'''8 | c'''4) b''8( c'''8) aes''4.-> g''8 | r8 g''8( f'''4.->) es'''8( d'''8 c'''8) | bes''8-. c'''-. des'''-. bes''-. g'''4.-> f'''8 | aes'''4.-> g'''8 f'''4 d'''4 | c'''4-> b''4-> r2 |"
P_mid=shift(P_hi,-1); P_lo=shift(P_hi,-2)
dyn=lambda s,d: s.replace("8(","8("+d,1) if s.startswith("r8") else re.sub(r"(\d)",lambda m:m.group(1)+d,s,count=1)
headAb="aes'2->( es'4. f'8 | ges'4-.) f'8( es'8 des'4-.) c'4-. |"
run="aes'8( bes' c'' des'' es'' f'' ges'' aes'' | bes''8 c''' des''' es''' f'''4->) r4 |"
C1={}
C1['FluteOne']=dyn(P_hi,"\\ff")+" R1*2 | "+shift(headAb,1).replace("->(","->(\\ff",1)+" ges'''1\\< | ges'''2. r4\\! |"
C1['FluteTwo']="g''1\\ff | aes''1 | aes''1 | bes''1 | c'''2 f''2 | g''4-> g''4-> r2 | R1*2 | es''1\\ff | es''1 | es'''1\\< | es'''2. r4\\! |"
C1['OboeOne']=dyn(P_mid,"\\ff")+" R1*2 | "+headAb.replace("->(","->(\\ff",1)+" c'''1\\< | c'''2. r4\\! |"
C1['OboeTwo']="g'1\\ff | f'1 | aes'1 | g'1 | aes'2 f'2 | f'4-> f'4-> r2 | R1*2 | c''1\\ff | c''1 | aes''1\\< | aes''2. r4\\! |"
C1['ClOne']=dyn(P_mid,"\\ff")+" R1*2 | "+headAb.replace("->(","->(\\ff",1)+" ges''1\\< | ges''2. r4\\! |"
C1['ClTwo']="es'1\\ff | d'1 | c'1 | des'1 | c'2 d'2 | d'4-> d'4-> r2 | R1*2 | aes'1\\ff | aes'1 | es''1\\< | es''2. r4\\! |"
C1['BsnOne']="c'2\\ff es'2 | d'2 f'2 | es'2 c'2 | e'2 bes2 | aes2 f2 | g4-> g,4-> r2 | c'1\\ff | c'1 | es'1 | es'1 | ges1\\< | ges2. r4\\! |"
C1['BsnTwo']="c1\\ff | d1 | es1 | e1 | f2 d2 | g,4-> g,4-> r2 | aes,1\\ff | aes,1 | aes,1 | aes,1 | aes,1\\< | aes,2. r4\\! |"
C1['Cbsn']="c,4\\ff c,4 c,4 c,4 | d,4 d,4 d,4 d,4 | es,4 es,4 es,4 es,4 | e,4 e,4 e,4 e,4 | f,4 f,4 d,4 d,4 | g,,4-> g,,4-> r2 | aes,,1\\ff | aes,,1 | aes,,1 | aes,,1 | aes,,1\\< | aes,,2. r4\\! |"
C1['HnOne']="g'1\\ff | f'1 | aes'1 | g'1 | aes'2 aes'2 | g'4-> g'4-> r2 | "+headAb.replace("->(","->(\\ff",1)+" es''1 | es''1 | es''1\\< | es''2. r4\\! |"
C1['HnTwo']="es'1\\ff | f'1 | f'1 | e'1 | f'2 f'2 | f'4-> f'4-> r2 | "+headAb.replace("->(","->(\\ff",1)+" c''1 | c''1 | c''1\\< | c''2. r4\\! |"
C1['HnThree']="c'1\\f~ | c'4 b2. | c'1 | des'1 | c'2 c'2 | c'4-> b4-> r2 | "+headAb.replace("->(","->(\\ff",1)+" ges'1 | ges'1 | ges'1\\< | ges'2. r4\\! |"
C1['HnFour']="g1\\f | g2 r2 | aes1 | bes1 | aes2 aes2 | g4-> g4-> r2 | "+headAb.replace("->(","->(\\ff",1)+" es'1 | es'1 | es'1\\< | es'2. r4\\! |"
C1['TptOne']="c''4\\f r8 c''8 c''4 r8 c''8 | g'4 r4 b'4 r4 | c''1 | des''4 r8 des''8 des''4 r8 des''8 | c''2 aes'2 | g'4->\\ff g'4-> r2 | R1*6 |"
C1['TptTwo']="g'4\\f r8 g'8 g'4 r8 g'8 | f'4 r4 f'4 r4 | aes'1 | g'4 r8 g'8 g'4 r8 g'8 | aes'2 f'2 | f'4->\\ff f'4-> r2 | R1*6 |"
C1['TptThree']="es'4\\f r8 es'8 es'4 r8 es'8 | d'4 r4 d'4 r4 | es'1 | e'4 r8 e'8 e'4 r8 e'8 | f'2 d'2 | d'4-> d'4-> r2 | R1*6 |"
C1['TbnOne']="c'1\\f~ | c'4 b2. | c'1 | des'1 | c'2 c'2 | c'4-> b4-> r2 | "+shift(headAb,-1).replace("->(","->(\\ff",1)+" c'1 | c'1 | c'1\\< | c'2. r4\\! |"
C1['TbnTwo']="g1\\f | f1 | aes1 | g1 | aes2 aes2 | g4-> g4-> r2 | es1\\ff | es1 | ges1 | ges1 | ges1\\< | ges2. r4\\! |"
C1['BassTbn']="c1\\f | d1 | es1 | e1 | f2 d2 | g,4-> g,4-> r2 | aes,1\\ff | aes,1 | aes,1 | aes,1 | aes,1\\< | aes,2. r4\\! |"
C1['Tuba']="c,1\\f | d,1 | es,1 | e,1 | f,2 d,2 | g,,4-> g,,4-> r2 | aes,,1\\ff | aes,,1 | aes,,1 | aes,,1 | aes,,1\\< | aes,,2. r4\\! |"
C1['Timp']="c4\\ff r8 c8 c4 r8 c8 | g,4 r4 g,4 r4 | R1 | c4 r8 c8 c4 r8 c8 | R1 | g,4-> g,4-> r2 | aes,4->\\ff r4 r2 | R1 | aes,4-> r4 r2 | R1 | aes,1:32\\f\\< | aes,2.:32 r4\\ff |"
C1['Perc']="R1*10 | R1 | r2 r4 \\drummode { cymc4->\\ff } |"
C1['VlnOne']=dyn(P_hi,"\\ff")+" "+run.replace("8(","8(\\ff",1)+" "+shift(headAb,1)+" "+shift(run,0)
C1['VlnTwo']=dyn(P_mid,"\\ff")+" "+shift(run,-1).replace("8(","8(\\ff",1)+" "+headAb+" "+shift(run,-1)
C1['Vla']=dyn(P_lo,"\\ff").replace("c'4-> b4-> r2 |","<d' f'>4-> <d' f'>4-> r2 |")+" "+" | ".join(["<es' aes'>4 r8 <es' aes'>8 <es' aes'>4 r8 <es' aes'>8"]*4)+" | <es' ges'>1\\< | <es' ges'>2. r4\\! |"
C1['Vc']="c'2\\ff es'2 | d'2 f'2 | es'2 c'2 | e'2 bes2 | aes2 f2 | g4-> g,4-> r2 | aes,1\\ff | aes,1 | aes,1 | aes,1 | aes,1\\< | aes,2. r4\\! |"
C1['Cb']=" | ".join([rep("c,"),rep("d,"),rep("es,"),rep("e,"),rep("f,",4)+" "+rep("d,",4),"g,,4-> g,,4-> r2"])+" | "+" | ".join([rep("aes,,")]*6)+" |"
C1['Cb']=C1['Cb'].replace("c,8","c,8\\ff",1)
# drummode wrapper for Perc: write whole variable in drummode
C1['Perc']="R1*11 | r2 r4 cymc4->\\ff |"
W('codaOne',C1,["% CODA, bars 199-210. 199-204: the last C-minor tutti, in movement I's hammered layout exactly as at its bars 27-32 (movement I's first-theme",
"% head in four octaves, double basses in repeated eighths on the chromatic bass C-D-E flat-E-F, bassoon 1 and cellos on the tenor line,",
"% horns and trombones held, trumpets and timpani in the c4 r8 c8 rhythm; cyclic-notes 'Owed' item 7). Movement I's head is used only as a link.",
"% 205-210: over the A flat pedal (V of D flat) theme F1's head in the horns, then in the high winds and violins; A flat 7 crescendo into D flat."])
