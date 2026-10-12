from g import *
import re
def W(name,d,comment):
    lines=["\\version \"2.24.0\""]+comment+[""]
    for k,v in d.items():
        lines.append(f"{name}{k} = "+("\\drummode " if k=='Perc' else "")+f"{{ {v} }}")
    open(f'/tmp/m3/v01/sections/{name}.ily','w').write("\n".join(lines)+"\n")
rep=lambda p,n=8: " ".join([f"{p}8"]*n)
F={}
# 243-250 P head (movement I) in C major on top, S head in the brass, hammered basses
Ph="r8 g''8( e'''4.->) d'''8( des'''8 c'''8 | c'''4) b''8( c'''8) a''4.-> g''8 | r8 g''8( f'''4.->) e'''8( d'''8 c'''8) | b''8-. c'''-. d'''-. b''-. g'''4.-> f'''8 | r8 g''8( e'''4.->) d'''8( c'''8 b''8 | c'''4) e'''8( d'''8) a'''4.-> g'''8 | f'''4.-> e'''8 d'''4 g'''4 | g'''2.-> r4 |"
Sh="e''2.~(\\ff e''8 d''8 | c''4 a''2-- g''4 | f''4. e''8 d''4 f''8 a''8 | c'''2 b''2) | e''2.~( e''8 d''8 | c''4 a''2-- g''4 | f''4. e''8 d''4 c''4 | b'2 c''2) |"
Sh2="c''2.~(\\ff c''8 b'8 | a'4 f''2-- e''4 | d''4. c''8 b'4 d''8 f''8 | e''2 d''2) | c''2.~( c''8 b'8 | a'4 f''2-- e''4 | d''4. c''8 b'4 a'4 | g'2 a'2) |"
# 251-255 chorale, last statement, Don Giovanni approach: I6 - vi - iiø6/5 - bVI - V7 - I (the symphony's first root-position V7-I in C since movement I bar 135)
ch1="g'1 | e''1 | d''1 | c''2 b'2 | c''1 |"
# 256-262 tonic close
cl_v1="r8 g''8(\\ff e'''4.->) d'''8( c'''8 b''8 | c'''4->) r4 r2 | r8 g''8( e'''4.->) d'''8( c'''8 b''8 | c'''4->) r4 r2 | <e'' c'''>4-> r8 <f'' c'''>8 <e'' c'''>4-> r4 | <c''' e''' g'''>1->~ | <c''' e''' g'''>4-> r4 r2\\fermata |"
F['VlnOne']=Ph.replace("8(","8(\\ff",1)+" "+shift(ch1,1).replace("1","1\\ff",1)+" "+cl_v1
F['VlnTwo']=shift(Ph,-1).replace("8(","8(\\ff",1)+" e''1\\ff | c'''1 | aes''1 | aes''2 g''2 | g''1 | "+shift(cl_v1,-1).replace("<c'' e'' g''>","<c'' e'' g''>")
F['Vla']=shift(Ph,-2).replace("8(","8(\\ff",1)+" c''1\\ff | a'1 | f'1 | es'2 d'2 | e'1 | r8 g'8( e''4.->) d''8( c''8 b'8 | c''4->) r4 r2 | r8 g'8( e''4.->) d''8( c''8 b'8 | c''4->) r4 r2 | <g e'>4-> r8 <a f'>8 <g e'>4-> r4 | <g e' c''>1->~ | <g e' c''>4-> r4 r2\\fermata |"
F['FluteOne']=Ph.replace("8(","8(\\ff",1)+" "+shift(ch1,1).replace("1","1\\ff",1)+" "+cl_v1.replace("<c''' e''' g'''>","g'''").replace("<e'' c'''>","c'''").replace("<f'' c'''>","c'''")
F['FluteTwo']="R1*8 | e''1\\ff | c'''1 | aes''1 | aes''2 g''2 | g''1 | R1*4 | e'''1->~\\ff | e'''4-> r4 r2\\fermata |"
F['OboeOne']=shift(Ph,-1).replace("8(","8(\\ff",1)+" "+ch1.replace("1","1\\ff",1)+" R1*4 | c'''1->~\\ff | c'''4-> r4 r2\\fermata |"
F['OboeTwo']="R1*8 | e'1\\ff | c''1 | aes'1 | aes'2 g'2 | g'1 | R1*4 | g''1->~\\ff | g''4-> r4 r2\\fermata |"
F['ClOne']=shift(Ph,-1).replace("8(","8(\\ff",1)+" "+ch1.replace("1","1\\ff",1)+" R1*4 | e''1->~\\ff | e''4-> r4 r2\\fermata |"
F['ClTwo']="R1*8 | c'1\\ff | a'1 | f'1 | es'2 d'2 | e'1 | R1*4 | c''1->~\\ff | c''4-> r4 r2\\fermata |"
F['BassCl']="R1*8 | e1\\ff | a,1 | f,1 | aes,2 g,2 | c1 | R1*4 | c,1->~\\ff | c,4-> r4 r2\\fermata |"
ten="c'2\\ff e'2 | d'2 f'2 | c'2 a2 | b2 d'2 | c'2 g2 | a2 c'2 | a2 f2 | b2 g2 |"
F['BsnOne']=ten+" g1\\ff | e'1 | d'1 | c'2 b2 | c'1 | R1*4 | c'1->~\\ff | c'4-> r4 r2\\fermata |"
F['BsnTwo']="c1\\ff | d1 | f,1 | g,1 | e1 | f,1 | d1 | g,1 | e1\\ff | a,1 | f,1 | aes,2 g,2 | c1 | c4-> r4 r2 | c4-> r4 r2 | c4-> r8 f,8 c4-> r4 | c1->~ | c4-> r4 r2\\fermata |"
F['Cbsn']="c,1\\ff | d,1 | f,,1 | g,,1 | e,1 | f,,1 | d,1 | g,,1 | e,1\\ff | a,,1 | f,,1 | aes,,2 g,,2 | c,1 | R1*4 | c,1->~\\ff | c,4-> r4 r2\\fermata |"
F['Vc']=ten+" e1\\ff | a,1 | f,1 | aes,2 g,2 | c1 | c4-> r4 r2 | c4-> r4 r2 | c4-> r8 f8 c4-> r4 | <c g>1->~ | <c g>4-> r4 r2\\fermata |"
F['Cb']=" | ".join([rep("c,"),rep("d,"),rep("f,"),rep("g,,"),rep("e,"),rep("f,"),rep("d,"),rep("g,,")]).replace("c,8","c,8\\ff",1)+" | e,1\\ff | a,,1 | f,,1 | aes,,2 g,,2 | c,1 | "+" | ".join([rep("c,")]*4)+" | c,1->~ | c,4-> r4 r2\\fermata |"
F['TptOne']=Sh+" "+ch1.replace("1","1\\ff",1)+" c''4->\\ff r8 c''8 c''4-> r4 | c''4-> r8 c''8 c''4-> r4 | c''4-> r8 c''8 c''4-> r4 | c''4-> r8 c''8 c''4-> r4 | c''1->~ | c''4-> r4 r2\\fermata |"
F['TptTwo']=Sh2+" e'1\\ff | c''1 | c''1 | c''2 d''2 | e''1 | g'4->\\ff r8 g'8 g'4-> r4 | a'4-> r8 a'8 g'4-> r4 | g'4-> r8 a'8 g'4-> r4 | g'4-> r8 g'8 g'4-> r4 | e''1->~ | e''4-> r4 r2\\fermata |"
F['TptThree']="g'4\\ff r8 g'8 g'4 r8 g'8 | a'4 r8 a'8 a'4 r8 a'8 | a'4 r8 a'8 a'4 r8 a'8 | g'4 r8 g'8 g'4 r8 g'8 | g'4 r8 g'8 g'4 r8 g'8 | a'4 r8 a'8 a'4 r8 a'8 | a'4 r8 a'8 a'4 r8 a'8 | g'4 r8 g'8 g'4 r8 g'8 | c'1\\ff | a'1 | f'1 | es'2 f'2 | g'1 | e'4->\\ff r8 e'8 e'4-> r4 | f'4-> r8 f'8 e'4-> r4 | e'4-> r8 f'8 e'4-> r4 | e'4-> r8 e'8 e'4-> r4 | g'1->~ | g'4-> r4 r2\\fermata |"
F['HnOne']=shift(Sh,-1)+" "+shift(ch1,-1).replace("1","1\\ff",1)+" R1*4 | c''1->~\\ff | c''4-> r4 r2\\fermata |"
F['HnTwo']=shift(Sh,-1)+" "+shift(ch1,-1).replace("1","1\\ff",1)+" R1*4 | g'1->~\\ff | g'4-> r4 r2\\fermata |"
F['HnThree']="g'1\\ff | f'1 | f'1 | f'1 | g'1 | f'1 | f'1 | f'1 | e'1\\ff | e'1 | f'1 | es'2 d'2 | e'1 | R1*4 | e'1->~\\ff | e'4-> r4 r2\\fermata |"
F['HnFour']="e'1\\ff | d'1 | c'1 | d'1 | e'1 | c'1 | d'1 | d'1 | c'1\\ff | a1 | aes1 | aes2 g2 | g1 | R1*4 | c'1->~\\ff | c'4-> r4 r2\\fermata |"
F['TbnOne']="g1\\ff | a1 | a1 | g1 | g1 | a1 | a1 | g1 | "+shift(ch1,-1).replace("1","1\\ff",1)+" R1*4 | c'1->~\\ff | c'4-> r4 r2\\fermata |"
F['TbnTwo']="e1\\ff | f1 | f1 | f1 | e1 | f1 | f1 | f1 | c1\\ff | c1 | aes1 | es2 f2 | e1 | R1*4 | g1->~\\ff | g4-> r4 r2\\fermata |"
F['BassTbn']="c1\\ff | d1 | f,1 | g,1 | e1 | f,1 | d1 | g,1 | e1\\ff | a,1 | f,1 | aes,2 g,2 | c1 | R1*4 | c1->~\\ff | c4-> r4 r2\\fermata |"
F['Tuba']="c,1\\ff | d,1 | f,,1 | g,,1 | e,1 | f,,1 | d,1 | g,,1 | e,1\\ff | a,,1 | f,,1 | aes,,2 g,,2 | c,1 | c,4-> r4 r2 | c,4-> r4 r2 | c,4-> r8 f,,8 c,4-> r4 | c,1->~ | c,4-> r4 r2\\fermata |"
F['Timp']="c4\\ff r8 c8 c4 r8 c8 | R1 | c4 r8 c8 c4 r8 c8 | g,4 r8 g,8 g,4 r8 g,8 | c4 r8 c8 c4 r8 c8 | R1 | R1 | g,4 r8 g,8 g,4 r8 g,8 | R1*3 | aes,2\\ff g,2 | c1:32 | c4->\\ff r8 g,8 c4 r4 | c4-> r8 g,8 c4 r4 | c4-> r8 g,8 c4 r4 | c4-> r8 g,8 c4 r4 | c1:32~ | c4-> r4 r2\\fermata |"
F['Perc']="cymc4->\\ff r4 r2 | R1*3 | cymc4-> r4 r2 | R1*7 | cymc1-> | cymc4-> r4 r2 | R1 | cymc4-> r4 r2 | R1 | cymc1->~ | cymc4-> r4 r2\\fermata |"
W('finale',F,["% ALLEGRO MOLTO, bars 243-262 (cyclic-notes 'Owed' items 6, 7, 3). 243-250: movement I's first-theme head in C major on top (flute 1 and",
"% violins I, oboe 1/clarinet 1/violins II, violas, in octaves) combined with movement I's second-theme head in the brass (trumpets, horns),",
"% fast, ff, over the hammered double-bass eighths: movement I's tutti layout turned to C major. 251-255: Maestoso, the chorale's last",
"% statement in full brass, ending C-B-C, over I6 - vi - iiø6/5 (borrowed) - bVI - V7 - I: the symphony's first root-position V7-I in C since",
"% movement I bar 135; trumpet 1 takes B to C, trumpet 2 has the E natural (the Don Giovanni arrival of cyclic-notes). 256-262: tonic close,",
"% movement I's timpani pulse, last chord ff."])
