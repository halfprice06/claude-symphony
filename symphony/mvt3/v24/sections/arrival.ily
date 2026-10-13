\version "2.24.0"
% THE C-MAJOR ARRIVAL AND CHORALE, bars 223-234 (c020: bar numbers updated from v01), Maestoso (cyclic-notes 'Owed' items 2-4). 223: trumpet 1's B rises to C, coupled with
% the timpani; the stop chord of 222 resolves; the first sustained forte major chord in full brass; string tremolo and the violins' C7 here
% and only here; crash cymbals, no tam-tam. 224-228: the brass chorale, the motto in major G-E-D-C-D flat-C, trombone colour with horns
% and trumpets, independent bass C-C-B-A-F (cyclic-notes, mvt I critic 160); c002: 227 A minor - augmented triad A-D flat-F - F (no 5ths E-F over A-B flat, A&S PDF 83). 226-230: the violins (with flutes, oboes, clarinets)
% in canon two bars after the brass. 229-230: movement I's timpani pulse c4 r8 g,8 c4 r4 between the phrases. 231-234: plagal close over
% the C pedal with mixture (IV - I - iv - I); no root-position V-I in C before the last cadence (262-263).

arrivalTptOne = { c''1\fff | g'1\f | e''1 | d''1 | c''2 des''2 | c''1 | R1 | c''1\f | a'1 | g'1 | aes'1\> | g'2. r4\mf | }
arrivalTptTwo = { g'1\fff | e'1\f | c''1 | g'1 | a'1 | a'1 | R1 | g'1\f | f'1 | e'1 | f'1\> | e'2. r4\mf | }
arrivalTptThree = { e'1\fff | R1*11 | }
arrivalHnOne = { c''1\fff | g'1\f | g'1 | g'1 | e'2 f'2 | f'1 | R1 | e'1\f | f'1 | e'1 | f'1\> | e'2. r4\mf | }
arrivalHnTwo = { g'1\fff | e'1\f | e'1 | d'1 | c'2 des'2 | c'1 | R1 | c'1\f | c'1 | c'1 | c'1\> | c'2. r4\mf | }
arrivalHnThree = { e'1\fff | g1\f | c'1 | d'1 | a1 | a1 | R1 | g1\f | a1 | g1 | aes1\> | g2. r4\mf | }
arrivalHnFour = { c'1\fff | e1\f | g1 | g1 | e2 f2 | f1 | R1 | e1\f | f1 | e1 | f1\> | e2. r4\mf | }
arrivalTbnOne = { g1\fff | g1\f | e'1 | d'1 | c'2 des'2 | c'1 | R1 | c'1\f | c'1 | c'1 | c'1\> | c'2. r4\mf | }
arrivalTbnTwo = { e1\fff | e1\f | c'1 | g1 | e2 f2 | f1 | R1 | g1\f | f1 | g1 | f1\> | e2. r4\mf | }
arrivalBassTbn = { c1\fff | c1\f | c1 | b,1 | a,1 | f,1 | R1 | c1\f | c1 | c1 | c1\> | c2. r4\mf | }
arrivalTuba = { c,1\fff | c,1\f | c,1 | b,,1 | a,,1 | f,,1 | R1 | c,1\f | c,1 | c,1 | c,1\> | c,2. r4\mf | }
arrivalTimp = { c1:32\fff | c4 r4 r2 | R1*4 | c4\f r8 g,8 c4 r4 | c4 r8 g,8 c4 r4 | c1:32\f | c1:32 | c1:32\> | c2.:32 r4\mf | }
arrivalPerc = \drummode { <\tweak style #'xcircle cymc bd>1\fff | R1*11 | }
arrivalFluteOne = { c''''1\fff | R1*2 | g''1\ff | e'''1 | d'''1 | c'''2 des'''2 | c'''1 | a''1\f | g''1 | aes''1\> | g''2. r4\mf | }
arrivalFluteTwo = { g'''1\fff | R1*2 | e''1\ff | c'''1 | a''1 | a''2 bes''2 | a''1 | f''1\f | e''1 | f''1\> | e''2. r4\mf | }
arrivalOboeOne = { c'''1\fff | R1*2 | g'1\ff | e''1 | d''1 | c''2 des''2 | c''1 | c''1\f | c''1 | c''1\> | c''2. r4\mf | }
arrivalOboeTwo = { g''1\fff | R1*2 | e'1\ff | c''1 | a'1 | a'2 bes'2 | a'1 | a'1\f | g'1 | aes'1\> | g'2. r4\mf | }
arrivalClOne = { e'''1\fff | R1*2 | g'1\ff | e''1 | d''1 | c''2 des''2 | c''1 | f''1\f | e''1 | f''1\> | e''2. r4\mf | }
arrivalClTwo = { c'''1\fff | R1*2 | d'1\ff | e'1 | a'1 | g'2 f'2 | e'1 | c''1\f | c''1 | c''1\> | c''2. r4\mf | }
arrivalBassCl = { c,1\fff | R1*11 | }
arrivalBsnOne = { c1\fff | c1\f | c1 | b,1 | a,1 | f1 | e2 bes,2 | c1 | c1 | c1 | c1\> | c2. r4\mf | }
arrivalBsnTwo = { c,1\fff | c,1\f | c,1 | b,,1 | a,1 | f,1 | e,2 bes,,2 | c,1 | c,1 | c,1 | c,1\> | c,2. r4\mf | }
arrivalCbsn = { c,,1\fff | c,,1\f | c,,1 | b,,,1 | a,,1 | f,,1 | e,,2 bes,,2 | c,,1 | c,,1 | c,,1 | c,,1\> | c,,2. r4\mf | }
arrivalVlnOne = { c''''1:32\fff | R1*2 | g''1\ff^\markup \italic "change bow at will" | e'''1 | d'''1 | c'''2 des'''2 | c'''1 | a''1\f | g''1 | aes''1\> | g''2.\mf g'4 | }
arrivalVlnTwo = { <e'' c'''>1:32\fff | R1 | R1 | g'1\ff^\markup \italic "unis., change bow at will" | e''1 | d''1 | c''2 des''2 | c''1 | f''1\f | e''1 | f''1\> | e''2.\mf g'4 | }
arrivalVla = { <g' e''>1:32\fff | e'4--(\f^\markup \italic "unis." e'4-- e'4-- e'4--) | c'4--( c'4-- c'4-- c'4--) | g4--( g4-- g4-- g4--) | e4--( e4-- f4-- f4--) | a4--( a4-- a4-- a4--) | g2\f^\markup \italic "change bow at will" bes2 | g1 | a1 | g1 | aes1\> | g2. r4\mf | }
arrivalVc = { <c g>1:32\fff | c1\f^\markup \italic "change bow at will" | c1 | b,1 | a,1 | f1 | e2 bes,2 | c1 | c1 | c1 | c1\> | c2. r4\mf | }
arrivalCb = { c,1:32\fff | c,1\f^\markup \italic "change bow at will" | c,1 | b,,1 | a,,1 | f,1 | e,2 bes,,2 | c,1 | c,1 | c,1 | c,1\> | c,2. r4\mf | }
