\version "2.24.0"
% RETRANSITION, bars 135-150. 135-138: a descending chain of diminished sevenths over the chromatic bass D - D flat - C - B,
% arriving on movement I's stop chord B-D-F-A flat at 138 (not resolved to C: that resolution belongs to the C-major arrival at 219).
% 139-146: a held G area with B natural in the bass (cyclic-notes, A&S PDF 449, 452-454): theme F1's head on G in imitation,
% horns 139, oboe and clarinet 141, violins 143, everyone 145. 147-150: V6/5 ff, allargando; the reprise comes from the inverted V.
% c026: 143-145 timpani: the scherzo's motive x (crotchet, two quavers, crotchet) on the dominant, quoted from the scherzo's own retransition
% (scherzo v04 bars 241, 243, 249, 251, 253-255; scherzo v24 241 and 249: b,4 b,8 b,8 b,4 on its dominant B), transposed down a major third to G (the C - A flat - E cycle
% run back). It is also the rhythm of F1's second bar (f'4 es'8 d'8 c'4), which Vln II (143) and Vln I (144) play in rhythmic unison with it.
% 145: two overlapping statements; 146 eighths; 147 roll (a written-out acceleration of the drum strokes).
% c073 (form; A&S PDF 112: a chord expanded over a whole section needs its root position; PDF 95, Ex. 6-4: the expanded V shapes the form; PDF 122: the bass of V6/5
% may leave the leading tone inside an expansion of V7): 147-150 the bass (Cb, Cbn, tuba, B.cl, Bn 2, Vc lower note) moves from B to the root G, so the ff dominant
% before the reprise stands on G for 147-153 (the i6/4 at 151 is a neighbour chord over it, PDF 129-130); B stays in the bass 138-146 (stop chord, stretto). The tonic root still comes only at 155 (V6/5 - i).

retrFluteOne = { R1*4 | R1*4 | g''1\mf | aes''1 | g'''2->(\f d'''4. es'''8 | f'''4-.) es'''8( d'''8 c'''4-.) b''4-. | f'''1->\ff | d'''1 | f'''1~ | f'''2. r4 | }
retrFluteTwo = { R1*4 | R1*8 | d'''1->\ff | b''1 | d'''1~ | d'''2. r4 | }
% c028: 138 the sf of the stop chord decays (sf >) in the strings and oboe 1, so the winds' sub. p chord is heard under it (Adler II PDF 190, Ex. XV-35: held strings sf > pp; forte subito piano needs the loud chord to give way)
retrOboeOne = { R1*3 | b''1\sf\> | R1*2\! | g''2->(\mf d''4. es''8 | f''4-.) es''8( d''8 c''4-.) b'4-. | f''1 | f''1 | g''2->(\f d''4. es''8 | f''4-.) es''8( d''8 c''4-.) b'4-. | b''1->\ff | g''1 | b''1~ | b''2. r4 | }
% c010: 138 Ob 1 B5 sf on top of the stop chord, as movement I puts B5 on top (26, 138); the B resolves only at 218-219 (A&S PDF 597-598).
retrOboeTwo = { R1*4 | R1*8 | f''1->\ff | d''1 | f''1~ | f''2. r4 | }
retrCorAnglais = { R1*4 | R1*8 | d''1->\ff | b'1 | d''1~ | d''2. r4 | }
retrClOne = { b'1\pp\< | bes'1 | a'1 | aes'1\subP | R1*2 | g''2->(\mf d''4. es''8 | f''4-.) es''8( d''8 c''4-.) b'4-. | d''1 | d''1 | g'2->(\f d'4. es'8 | f'4-.) es'8( d'8 c'4-.) b4-. | g''1->\ff | f''1 | g''1~ | g''2. r4 | }
retrClTwo = { f'1\pp\< | e'1 | es'1 | d'1\subP | R1*8 | d''1->\ff | b'1 | d''1~ | d''2. r4 | }
% c075 (MOLA PDF 5: logical cues in long rests, audible and obvious, in the reading key; Example 4, PDF 10): part-only cue, tag 'part (score.ly removes it from the score); the F1 head in Bn 1 at 145-146 before the bass clarinet's first entry at 147, after 140 bars
retrBassCl = { R1*4 | R1*6 | \tag #'score { R1*2 } \tag #'part { \cueDuring "bsnOne" #UP { R1*2^\markup \tiny "Bn. 1" } } | g,1->\ff | g,1 | g,1~ | g,2. d4 | }
retrBsnOne = { aes1\pp\< | g1 | ges1 | f1\subP | f1 | f1 | d'1\< | d'1 | f1 | f1 | g2->(\f d4. es8 | f4-.) es8( d8 c4-.) b,4-. | f1->\ff | g1 | f1~ | f2. r4 | }
retrBsnTwo = { d1\pp\< | des1 | c1 | b,1\subP | b,1 | b,1 | b,1\< | b,1 | b,1 | b,1 | b,1\f | b,1 | g,1->\ff | g,1 | g,1~ | g,2. d4 | }
retrCbsn = { R1*4 | R1*4 | b,,1\pp\<~ | b,,1~ | b,,1\f~ | b,,1 \breathe | g,,1->\ff | g,,1 | g,,1~ | g,,2. d,4 | }
retrHnOne = { R1*4 | g'2->(\p d'4. es'8 | f'4-.) es'8( d'8 c'4-.) b4-. | d''1 | d''1 | g'2->( d'4. es'8 | f'4-.) es'8( d'8 c'4-.) b4-. | g'1\f | f'1 | d''1->\ff | d''1 | d''1~ | d''2. r4 | }
% c052 (harmony; A&S Unit 25, PDF 423, 439: the leading tone is not doubled): 147-150 Hn 2 and the violas take G instead of B above the bass B.
retrHnTwo = { R1*4 | R1*2 | b'1\p | b'1 | g'2->( d'4. es'8 | f'4-.) es'8( d'8 c'4-.) b4-. | d'1\f | d'1 | g'1->\ff | g'1 | g'1~ | g'2. r4 | }
% c088 (expression; Adler ch. 10, PDF 308: stopped horn is used for single notes and is effective 'when one wishes to have the horn play sf>p', marked + and then o for open): 138 Hn 3-4 take the stop chord's D and A flat stopped sf> with the strings' and oboe's sf>, open p at 139 (were sub. p under the strings' sf).
retrHnThree = { f'1\pp\< | e'1 | es'1 | d'1\sf\>-\stopped | d'1\p-\open | d'1 | d'1\< | d'1 | f'1 | f'1 | f'1\f | f'1 | g'1->\ff | g'1 | g'1~ | g'2. r4 | }
retrHnFour = { b1\pp\< | bes1 | a1 | aes1\sf\>-\stopped | b1\p-\open | b1 | b1\< | b1 | b1 | b1 | b1\f | b1 | f'1->\ff | f'1 | f'1~ | f'2. r4 | }
retrTptOne = { R1*4 | R1*8 | d''1->\ff | f''1 | d''1~ | d''2. r4 | }
retrTptTwo = { R1*4 | R1*8 | b'1->\ff | d''1 | b'1~ | b'2. r4 | }
retrTptThree = { R1*4 | R1*8 | g'1->\ff | g'1 | g'1~ | g'2. r4 | }
retrTbnOne = { R1*4 | R1*4 | d'1\pp\< | d'1 | f'1\f | f'1 | f'1->\ff | f'1 | f'1~ | f'2. r4 | }
retrTbnTwo = { R1*4 | R1*4 | b1\pp\< | b1 | d'1\f | d'1 | d'1->\ff | d'1 | d'1~ | d'2. r4 | }
retrBassTbn = { R1*4 | R1*4 | g,1\pp\< | g,1 | g,1\f | g,1 | g,1->\ff | g,1 | g,1~ | g,2. r4 | }
retrTuba = { R1*4 | R1*8 | g,,1->\ff | g,,1 | g,,1~ | g,,2. d,4 | }
% c045 (Adler part 2 PDF 80, Ex. XII-48: a longer roll is written as tied notes; an untied roll restarts at each barline): rolls on one pitch tied across the barlines
% c060 (cyclic lens; Sebesky ch. 1, PDF 13-14: focus): 143 the scherzo's motive x starts mf (was pp) so it is heard against Vln I's f F1 head; crescendo to f at 145 unchanged
retrTimp = { R1*4 | R1*4 | g,4\mf\< g,8 g,8 g,4 r4 | g,4 g,8 g,8 g,4 r4 | g,4\f g,8 g,8 g,4 g,8 g,8 | g,8 g,8 g,8 g,8 g,8 g,8 g,8 g,8 | g,1:32\ff~ | g,1:32~ | g,1:32~ | g,2.:32 r4 | }
retrVlnOne = { aes''1\pp\< | g''1 | ges''1 | f''1\sf\> | R1*4\! | g''2->(\f d''4. es''8 | f''4-.) es''8( d''8 c''4-.) r4 | g'''2->( d'''4. es'''8 | f'''4-.) es'''8( d'''8 c'''4-.) b''4-. | <f'' d'''>1->\ff | <d'' b''>1 | <f'' d'''>1~ | <f'' d'''>2. r4 | }
retrVlnTwo = { d''1\pp\< | des''1 | c''1 | b'1\sf\> | R1\! | R1 | R1 | g'2->(\mf d'4. es'8 | f'4-.) es'8( d'8 c'4-.) b4-. | b'1\f | g''2->( d''4. es''8 | f''4-.) es''8( d''8 c''4-.) b'4-. | <b' g''>1->\ff | <g' f''>1 | <b' g''>1~ | <b' g''>2. r4 | }
retrVla = { <f' b'>1\pp\<^\markup \italic "div." | <e' bes'>1 | <es' a'>1 | <d' aes'>1\sf\> | d'1\p^\markup \italic "unis." | d'1 | f'1\< | f'1 | d'1 | d'1 | g'2->( d'4. es'8 | f'4-.) es'8( d'8 c'4-.) b4-. | <d' g'>1->\ff | <d' g'>1 | <d' g'>1~ | <d' g'>2. r4 | }
retrVc = { d1\pp\< | des1 | c1 | b,1\sf\> | b,1\p | g2->( d4. es8 | f4-.) es8( d8 c4-.) b,4-. | b,1\<~\cbaw | b,1~ | b,1~ | b,1\f~ | b,1 | <g, f>1->\ff | <g, g>1 | <g, f>1~ | <g, f>2. <d f>4 | }
retrCb = { d,1\pp\< | des,1 | c,1 | b,,1\sf\> | b,,1\p~\cbaw | b,,1~ | b,,1\<~ | b,,1~ | b,,1~ | b,,1~ | b,,1\f~ | b,,1 | g,,1->\ff | g,,1 | g,,1~ | g,,2. d,4 | }
