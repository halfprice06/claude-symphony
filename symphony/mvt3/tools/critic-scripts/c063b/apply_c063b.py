import re, sys
W=sys.argv[1]
# --- recS.ily: viola weave 171-186, harp rests 187-198
p=W+'/sections/recS.ily'; s=open(p).read()
m=re.search(r'^recSVla = \{ (.*) \}$',s,re.M)
bars=[b.strip() for b in m.group(1).split('|') if b.strip()]
new=[]
for i,b in enumerate(bars[:16]):
    dy=re.findall(r'<([a-g][a-z]*[,\']*) ([a-g][a-z]*[,\']*)>4',b)
    halves=[f"{x}8( {y} {x} {y})" for (x,y) in dy]
    if len(dy)==1: halves.append("r2")
    bar=' '.join(halves)
    if i==0: bar=bar.replace("8(","8(\\pp^\\markup \\italic \"arco, sul tasto\"",1)
    new.append(bar)
rest=bars[16:]
assert '"arco, unis., espress."' in rest[0]
rest[0]=rest[0].replace('"arco, unis., espress."','"ord., espress."')
s=s.replace(m.group(0),'recSVla = { '+' | '.join(new+rest)+' | }')
s=s.replace("recSVla = {","""% c063 (form; Adler II PDF 288, Haydn: on a repeat the scoring changes, "devices like these add great variety"; PDF 269-270, Sibelius VC and Bartok PC 3: a soft,
% rhythmically independent weaving background under the solo; PDF 259-260): 171-186 were 51-66 transposed in every accompanying part. The violas now weave arco sul tasto pp
% eighths on the same dyads (E flat3-A flat3, an octave and more below the cor anglais and muted trumpet), so the recapitulated second theme keeps the movement's eighth-note
% motion and is not a copy of 51; 187 'ord.' (they are already arco and unis.).
recSVla = {""",1)
for v in ['recSHarpR','recSHarpL']:
    mm=re.search(r'^'+v+r' = \{.*\}$',s,re.M)
    s=s.replace(mm.group(0), v+' = { R1*16 | R1*12 | }')
s=s.replace("recSHarpR =","""% c063 (form; Adler II PDF 263-264, 267: a colour kept back stays fresh, Mozart keeps the orchestral horns and flutes silent while a soloist of that kind plays;
% PDF 261-262: roles exchanged): the harp's only texture in the movement is broken-chord eighths under a major-mode cantabile (67, 123, 187, 235); 187-198 were 67-78 again,
% harp included. The harp rests at 187-198, so its fourth use, under the owed C-major second-theme head at 235, comes after 104 bars of silence; the eighth-note motion
% moves to the minor half (violas 171-186).
recSHarpR =""",1)
open(p,'w').write(s)
# --- dev.ily: Vln I answers at 117 and 122
p=W+'/sections/dev.ily'; s=open(p).read()
old="f'''2-> r2 | fis''1\\p\\> | R1*8\\! | R1*5 | r2 r4 a''4(\\mf\\< |"
assert s.count(old)==1, 'vln1'
s=s.replace(old,"f'''2-> r2 | fis''1\\p\\> | R1*2\\! | r4 f'''8(\\p^\\markup \\italic \"dolce\" es''' d''' c''' bes'' aes'' | g''4) r4 r2 | R1*3 | r4 d'''8( c''' b'' a'' g'' fis'' | g''4) r4 r2 | R1*4 | r2 r4 a''4(\\mf\\< |")
s=s.replace("devVlnOne =","""% c063 (form; Adler II PDF 257-258: dialogue, a phrase answered at once in another colour "aids in a clearer exposition of the form"; PDF 274, Beethoven VC iii: the
% bassoon's line set against a contrasting activity, the answer kept two octaves above the woodwind solo): 117 and 122 Vln I, arco p against Vln II's pizz., answers the bassoon's
% held notes with the development's scale figure (winds at 101, 105), so the call of 99-106 carries into the lyrical centre; 117 descends F6-A flat5 to G5 at 118 (sixths and fourths over the solo's G4-F4-E flat4, no fifths); 122 descends D6-F sharp5 with B natural and lands on
% G5 at 123 with the turn to G major. Vln I then rests until its hand-over entry at 128.
devVlnOne =""",1)
open(p,'w').write(s)
print('ok')
