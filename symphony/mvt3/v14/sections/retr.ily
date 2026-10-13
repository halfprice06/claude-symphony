\version "2.24.0"
% RETRANSITION, bars 135-150. 135-138: a descending chain of diminished sevenths over the chromatic bass D - D flat - C - B,
% arriving on movement I's stop chord B-D-F-A flat at 138 (not resolved to C: that resolution belongs to the C-major arrival at 219).
% 139-146: a held G area with B natural in the bass (cyclic-notes, A&S PDF 449, 452-454): theme F1's head on G in imitation,
% horns 139, oboe and clarinet 141, violins 143, everyone 145. 147-150: V6/5 ff, allargando; the reprise comes from the inverted V.

retrFluteOne = { R1*4 | R1*4 | g''1\mf | aes''1 | g'''2->(\f d'''4. es'''8 | f'''4-.) es'''8( d'''8 c'''4-.) b''4-. | f'''1->\ff | d'''1 | f'''1~ | f'''2. r4 | }
retrFluteTwo = { R1*4 | R1*8 | d'''1->\ff | b''1 | d'''1~ | d'''2. r4 | }
retrOboeOne = { R1*3 | b''1\sf | R1*2 | g''2->(\mf d''4. es''8 | f''4-.) es''8( d''8 c''4-.) b'4-. | f''1 | f''1 | g''2->(\f d''4. es''8 | f''4-.) es''8( d''8 c''4-.) b'4-. | b''1->\ff | g''1 | b''1~ | b''2. r4 | }
% c010: 138 Ob 1 B5 sf on top of the stop chord, as movement I puts B5 on top (26, 138); the B resolves only at 218-219 (A&S PDF 597-598).
retrOboeTwo = { R1*4 | R1*8 | f''1->\ff | d''1 | f''1~ | f''2. r4 | }
retrCorAnglais = { R1*4 | R1*8 | d''1->\ff | b'1 | d''1~ | d''2. r4 | }
retrClOne = { b'1\pp\< | bes'1 | a'1 | aes'1\subP | R1*2 | g''2->(\mf d''4. es''8 | f''4-.) es''8( d''8 c''4-.) b'4-. | d''1 | d''1 | g'2->(\f d'4. es'8 | f'4-.) es'8( d'8 c'4-.) b4-. | g''1->\ff | f''1 | g''1~ | g''2. r4 | }
retrClTwo = { f'1\pp\< | e'1 | es'1 | d'1\subP | R1*8 | d''1->\ff | b'1 | d''1~ | d''2. r4 | }
retrBassCl = { R1*4 | R1*8 | b,1->\ff | b,1 | b,1~ | b,2. d4 | }
retrBsnOne = { aes1\pp\< | g1 | ges1 | f1\subP | f1\p | f1 | d'1\< | d'1 | f1 | f1 | g2->(\f d4. es8 | f4-.) es8( d8 c4-.) b,4-. | f1->\ff | g1 | f1~ | f2. r4 | }
retrBsnTwo = { d1\pp\< | des1 | c1 | b,1\subP | b,1\p | b,1 | b,1\< | b,1 | b,1 | b,1 | b,1\f | b,1 | b,1->\ff | b,1 | b,1~ | b,2. d4 | }
retrCbsn = { R1*4 | R1*4 | b,,1\pp\<~ | b,,1~ | b,,1\f~ | b,,1 | b,,1->\ff | b,,1 | b,,1~ | b,,2. d,4 | }
retrHnOne = { R1*4 | g'2->(\p d'4. es'8 | f'4-.) es'8( d'8 c'4-.) b4-. | d''1 | d''1 | g'2->( d'4. es'8 | f'4-.) es'8( d'8 c'4-.) b4-. | g'1\f | f'1 | d''1->\ff | d''1 | d''1~ | d''2. r4 | }
retrHnTwo = { R1*4 | R1*2 | b'1\p | b'1 | g'2->( d'4. es'8 | f'4-.) es'8( d'8 c'4-.) b4-. | d'1\f | d'1 | b'1->\ff | b'1 | b'1~ | b'2. r4 | }
retrHnThree = { f'1\pp\< | e'1 | es'1 | d'1\subP | d'1\p | d'1 | d'1\< | d'1 | f'1 | f'1 | f'1\f | f'1 | g'1->\ff | g'1 | g'1~ | g'2. r4 | }
retrHnFour = { b1\pp\< | bes1 | a1 | aes1\subP | b1\p | b1 | b1\< | b1 | b1 | b1 | b1\f | b1 | f'1->\ff | f'1 | f'1~ | f'2. r4 | }
retrTptOne = { R1*4 | R1*8 | d''1->\ff | f''1 | d''1~ | d''2. r4 | }
retrTptTwo = { R1*4 | R1*8 | b'1->\ff | d''1 | b'1~ | b'2. r4 | }
retrTptThree = { R1*4 | R1*8 | g'1->\ff | g'1 | g'1~ | g'2. r4 | }
retrTbnOne = { R1*4 | R1*4 | d'1\pp\< | d'1 | f'1\f | f'1 | f'1->\ff | f'1 | f'1~ | f'2. r4 | }
retrTbnTwo = { R1*4 | R1*4 | b1\pp\< | b1 | d'1\f | d'1 | d'1->\ff | d'1 | d'1~ | d'2. r4 | }
retrBassTbn = { R1*4 | R1*4 | g,1\pp\< | g,1 | g,1\f | g,1 | g,1->\ff | g,1 | g,1~ | g,2. r4 | }
retrTuba = { R1*4 | R1*8 | b,,1->\ff | b,,1 | b,,1~ | b,,2. d,4 | }
retrTimp = { R1*4 | R1*4 | g,4\pp\< r4 g,4 r4 | g,4 r4 g,4 r4 | g,4\f g,4 g,4 g,4 | g,8 g,8 g,8 g,8 g,8 g,8 g,8 g,8 | g,1:32\ff | g,1:32 | g,1:32~ | g,2.:32 r4 | }
retrVlnOne = { aes''1\pp\< | g''1 | ges''1 | f''1\sf | R1*4 | g''2->(\f d''4. es''8 | f''4-.) es''8( d''8 c''4-.) b'4-. | g'''2->( d'''4. es'''8 | f'''4-.) es'''8( d'''8 c'''4-.) b''4-. | <f'' d'''>1->\ff | <d'' b''>1 | <f'' d'''>1~ | <f'' d'''>2. r4 | }
retrVlnTwo = { d''1\pp\< | des''1 | c''1 | b'1\sf | R1 | R1 | R1 | g'2->(\mf d'4. es'8 | f'4-.) es'8( d'8 c'4-.) b4-. | b'1\f | g''2->( d''4. es''8 | f''4-.) es''8( d''8 c''4-.) b'4-. | <b' g''>1->\ff | <g' f''>1 | <b' g''>1~ | <b' g''>2. r4 | }
retrVla = { <f' b'>1\pp\< | <e' bes'>1 | <es' a'>1 | <d' aes'>1\sf | d'1\p | d'1 | f'1\< | f'1 | d'1 | d'1 | g'2->( d'4. es'8 | f'4-.) es'8( d'8 c'4-.) b4-. | <d' b'>1->\ff | <d' g'>1 | <d' b'>1~ | <d' b'>2. r4 | }
retrVc = { d1\pp\< | des1 | c1 | b,1\sf | b,1\p | g2->( d4. es8 | f4-.) es8( d8 c4-.) b,4-. | b,1\<~ | b,1~ | b,1~ | b,1\f~ | b,1 | <b, f>1->\ff | <b, g>1 | <b, f>1~ | <b, f>2. <d f>4 | }
retrCb = { d,1\pp\< | des,1 | c,1 | b,,1\sf | b,,1\p~ | b,,1~ | b,,1\<~ | b,,1~ | b,,1~ | b,,1~ | b,,1\f~ | b,,1 | b,,1->\ff | b,,1 | b,,1~ | b,,2. d,4 | }
