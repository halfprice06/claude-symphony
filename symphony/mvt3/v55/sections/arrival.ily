\version "2.24.0"
% THE C-MAJOR ARRIVAL AND CHORALE, bars 223-234 (c020: bar numbers updated from v01), Maestoso (cyclic-notes 'Owed' items 2-4). 223: trumpet 1's B rises to C, coupled with
% the timpani; the stop chord of 222 resolves; the first sustained forte major chord in full brass; string tremolo and the violins' C7 here
% and only here; crash cymbals, no tam-tam. 224-228: the brass chorale, the motto in major G-E-D-C-D flat-C, trombone colour with horns
% and trumpets, independent bass C-C-B-A-F (cyclic-notes, mvt I critic 160); c002: 227 A minor - augmented triad A-D flat-F - F (no 5ths E-F over A-B flat, A&S PDF 83). 226-230: the violins (with flutes, oboes, clarinets)
% in canon two bars after the brass. 229-230: movement I's timpani pulse c4 r8 g,8 c4 r4 between the phrases. 231-234: plagal close over
% the C pedal with mixture (IV - I - iv - I); no root-position V-I in C before the last cadence (262-263).

% c028: 224 the timpani's release stroke is f with the chorale (it inherited fff); 234 the diminuendo's mf sits on the last chord, not on the rest after it
% c029 (Rimsky-Korsakov PDF 82, 100): 224 Hn 3-4 C4 (were G3, E3): the brass chord in close order with no gap between G3 and E4, the third no longer doubled below the alto
% c036 (Adler PDF 230: give the contrabassoon periodic rests; PDF 198/175 double reeds): Bn 1-2 and Cbn rest 231-234 (they had played every bar since 211); the C pedal stays in tuba, bass trombone, cellos, basses. 223 B.cl C3 (PDF 216: low C is risky).
% c042 (harmony; A&S PDF 377, 394): 226 Fl 2 and Ob 2 G (were E: an unprepared, unresolved second against the chorale's D in Tpt 1, Hn 2-3, Tbn 1, Cl 2); 227 second half Fl 2/Ob 2 A and Cl 2 F
% (were C and E held against the brass's D flat and F: C sounded with the motto's chromatic D flat in the same octave). The canon line itself (Vln, Fl 1, Ob 1, Cl 1) is unchanged.
arrivalTptOne = { c''1\fff | g'1\f | e''1 | d''1 | c''2 des''2 | c''1 | R1 | c''1\f | a'1 | g'1 | aes'1\> | g'2.\mf r4 | }
arrivalTptTwo = { g'1\fff | e'1\f | c''1 | g'1 | a'1 | a'1 | R1 | g'1\f | f'1 | e'1 | f'1\> | e'2.\mf r4 | }
arrivalTptThree = { e'1\fff | R1*11 | }
arrivalHnOne = { c''1\fff | g'1\f | g'1 | g'1 | e'2 f'2 | f'1 | R1 | e'1\f | f'1 | e'1 | f'1\> | e'2.\mf r4 | }
arrivalHnTwo = { g'1\fff | e'1\f | e'1 | d'1 | c'2 des'2 | c'1 | R1 | c'1\f | c'1 | c'1 | c'1\> | c'2.\mf r4 | }
arrivalHnThree = { e'1\fff | c'1\f | c'1 | d'1 | a1 | a1 | R1 | g1\f | a1 | g1 | aes1\> | g2.\mf r4 | }
arrivalHnFour = { c'1\fff | c'1\f | g1 | g1 | e2 f2 | f1 | R1 | e1\f | f1 | e1 | f1\> | e2.\mf r4 | }
arrivalTbnOne = { g1\fff | g1\f | e'1 | d'1 | c'2 des'2 | c'1 | R1 | c'1\f | c'1 | c'1 | c'1\> | c'2.\mf r4 | }
arrivalTbnTwo = { e1\fff | e1\f | c'1 | g1 | e2 f2 | f1 | R1 | g1\f | f1 | g1 | f1\> | e2.\mf r4 | }
arrivalBassTbn = { c1\fff | c1\f | c1 | b,1 | a,1 | f,1 | R1 | c1\f | c1 | c1 | c1\> | c2.\mf r4 | }
arrivalTuba = { c,1\fff | c,1\f | c,1 | b,,1 | a,,1 | f,,1 | R1 | c,1\f | c,1 | c,1 | c,1\> | c,2.\mf r4 | }
% c045 (Adler part 2 PDF 80, Ex. XII-48: a longer roll is written as tied notes; an untied roll restarts at each barline): rolls on one pitch tied across the barlines
arrivalTimp = { c1:32\fff | c4\f r4 r2 | R1*4 | c4\f r8 g,8 c4 r4 | c4 r8 g,8 c4 r4 | c1:32\f~ | c1:32~ | c1:32\>~ | c2.:32\mf r4 | }
arrivalPerc = \drummode { <\tweak style #'xcircle cymc bd>1\fff | R1*11 | }
arrivalFluteOne = { c''''1\fff | R1*2 | g''1\ff | e'''1 | d'''1 | c'''2 des'''2 | c'''1 | a''1\f | g''1 | aes''1\> | g''2.\mf r4 | }
arrivalFluteTwo = { g'''1\fff | R1*2 | g''1\ff | c'''2 a''2 | a''1 | a''2 bes''2 | a''1 | f''1\f | e''1 | f''1\> | e''2.\mf r4 | }
arrivalOboeOne = { c'''1\fff | R1*2 | g''1\ff | e'''1 | d'''1 | c'''2 des'''2 | c'''1 | c''1\f | c''1 | c''1\> | c''2.\mf r4 | }
% c044 (orchestration; Adler ch. 15, PDF 169: two ideas separate when scored in opposing timbres and designs; PDF 159 no. 2, register for the dynamic; PDF 165): 226-228 Ob 2 and Cl 2 an octave higher, under the wood-wind/string canon instead of at pitch inside the brass chorale (Ob 2 G4 = Tpt 2/Hn 1, Cl 2 D4-F4 = Hn 1-3/Tbn 1). Pitch classes unchanged; 229 both return to their octave when the brass rest (Cl 2 F5-E5 over Ob 2 B flat4-A4 would be fifths at 229-230).
arrivalOboeTwo = { g''1\fff | R1*2 | g''1\ff | c'''2 a''2 | a''1 | a'2 bes'2 | a'1 | a'1\f | g'1 | aes'1\> | g'2.\mf r4 | }
arrivalClOne = { e'''1\fff | R1*2 | g''1\ff | e'''1 | d'''1 | c'''2 des'''2 | c'''1 | f''1\f | e''1 | f''1\> | e''2.\mf r4 | }
arrivalClTwo = { c'''1\fff | R1*2 | d''1\ff | e''2 f''2 | a''1 | g'2 f'2 | e'1 | c''1\f | c''1 | c''1\> | c''2.\mf r4 | }
arrivalBassCl = { c1\fff | R1*11 | }
arrivalBsnOne = { c1\fff | c1\f | c1 | b,1 | a,1 | f1 | e2 bes,2 | c1 | R1*4 | }
arrivalBsnTwo = { c,1\fff | c,1\f | c,1 | b,,1 | a,1 | f,1 | e,2 bes,,2 | c,1 | R1*4 | }
arrivalCbsn = { c,,1\fff | c,,1\f | c,,1 | b,,,1 | a,,1 | f,,1 | e,,2 bes,,2 | c,,1 | R1*4 | }
% c027 (texture; Adler II PDF 273-274, 283): 226-230 the canon's lower octave (Ob 1, Cl 1, Vln II) is moved up to the canon's upper octave, so it no longer crosses above the chorale's top line (Tpt 1 C-D flat-C, 227-228).
arrivalVlnOne = { c''''1:32\fff | R1*2 | g''1\ff\cbaw | e'''1 | d'''1 | c'''2 des'''2 | c'''1 | a''1\f | g''1 | aes''1\> | g''2.\mf g'4 | }
arrivalVlnTwo = { <e'' c'''>1:32\fff | R1 | R1 | g''1\ff\cbawU | e'''1 | d'''1 | c'''2 des'''2 | c'''1 | f''1\f | e''1 | f''1\> | e''2.\mf g'4 | }
arrivalVla = { <g' e''>1:32\fff | e'4--(\f^\markup \italic "unis." e'4-- e'4-- e'4--) | c'4--( c'4-- c'4-- c'4--) | g4--( g4-- g4-- g4--) | e4--( e4-- f4-- f4--) | a4--( a4-- a4-- a4--) | g2\f\cbaw bes2 | g1 | a1 | g1 | aes1\> | g2.\mf r4 | }
arrivalVc = { <c g>1:32\fff | c1\f\cbaw | c1 | b,1 | a,1 | f1 | e2 bes,2 | c1 | c1 | c1 | c1\> | c2.\mf r4 | }
arrivalCb = { c,1:32\fff | c,1\f\cbaw | c,1 | b,,1 | a,,1 | f,1 | e,2 bes,,2 | c,1 | c,1 | c,1 | c,1\> | c,2.\mf r4 | }
