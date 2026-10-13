\version "2.24.0"
% SECOND THEME IN MAJOR, bars 67-82, E flat major: theme F2 in the violins in octaves (Vln I at B flat 6 at most, 78, c011; movement III's
% C7 is kept for the C-major arrival at 219), the cellos' counter-melody (the bass counterline movement I lacked), harp broken chords,
% violas off the beat. Flute 1 and oboe 1 join the tune from 77 for its climax. 81-82 animando into the closing group.

% c032 (harmony): 79 Cl 2 and Hn 2 C4 (were A flat3: B flat-A flat under the tune's F-E flat, parallel 5ths).
% c095: the violins' crescendo to f at 78 starts on the downbeat of 77 (was on the last quarter of 76, which ends a system: the hairpin printed as a 2 mm stub after the last note, then restarted on the next system).
sTwoVlnOne = { bes''2.(\mf^\markup \italic "arco, cantabile" g''4) | f''4( es''4 g''4 bes''4) | f'''2( es'''4 d'''4) | c'''2( bes''2) | aes''2.( c'''4) | bes''4( aes''4 g''4 f''4) | g''2( es''2) | f''1 | bes''2.( g''4) | f''4( es''4 g''4 bes''4) | es'''2.\< f'''4\upbow | bes'''4(\f\downbow aes'''4 g'''4 f'''4) | es'''2.( d'''4) | c'''4( bes''4 aes''4 g''4)\> | f''2( d''2) | es''1\mf | }
sTwoVlnTwo = { bes'2.(\mf^\markup \italic "arco" g'4) | f'4( es'4 g'4 bes'4) | f''2( es''4 d''4) | c''2( bes'2) | aes'2.( c''4) | bes'4( aes'4 g'4 f'4) | g'2( es'2) | f'1 | bes'2.( g'4) | f'4( es'4 g'4 bes'4) | es''2.\< f''4\upbow | bes''4(\f\downbow aes''4 g''4 f''4) | es''2.( d''4) | c''4( bes'4 aes'4 g'4)\> | f'2( d'2^\markup \italic "sul G") | es'1\mf^\markup \italic "ord." | }
sTwoFluteOne = { R1*10 | es'''2.(\p\< f'''4 | bes'''4\f aes'''4 g'''4 f'''4) | es'''2.( d'''4 | c'''4 bes''4 aes''4 g''4\> | f''2 d''2 | es''1)\mf | }
sTwoOboeOne = { R1*10 | es''2.(\p\< f''4 | bes''4\f aes''4 g''4 f''4) | es''2.( d''4 | c''4 bes'4 aes'4 g'4\> | f'2 d'2 | es'1)\mf | }
% c027 (texture; Adler II PDF 259-260): 69-70 the violas' and cellos' counter-melody no longer moves in octaves with the tune (was c'-es'-d' | c'-bes against f-es-d | c-bes); it now moves against the tune's rhythm, A flat-B flat-C | C-D-E flat.
% c051 (melody; Sebesky ch. 6, PDF 208, Ex. 273: the counter-line changes from half notes to quarters to push into the next phrase): 74 Vc/Vla A flat-G-F-A flat under the tune's held F (the 7th resolves to G at 75).
% c094 (Rimsky-Korsakov PDF 51: in soft passages one string section = one wind; the counter-melody in unison (Vla + Vc) outweighs the tune spread in octaves): 67 Vla and Vc mp, crescendo 76 to mf at 77 with the tune's crescendo.
% c097 (texture; Adler ch. 11, PDF 44, 48-49: 'the wonderful independence' of a counter-line against the theme): 70-73 the violas' and cellos' counter-melody no longer lands on the tune's pitch (octaves C-C at 70, A flat-A flat at 71, G-G at 73 on the downbeat); it now moves E flat-F-G | E flat-C-E flat | ... | B flat-C-B flat, in sixths and tenths under the tune; 75-82 unchanged. Same change at 190-193 (recS).
sTwoVc = { g2(\mp^\markup \italic "arco, espress." aes4 bes4) | aes2( g2) | aes4( bes4 c'2) | es'4( f'4 g'2) | es'2( c'4 es'4) | d'2( aes2) | bes2( c'4 bes4) | aes4( g4 f4 aes4) | g2( aes4 bes4) | aes2(\< g2) | bes2(\mf c'4 f'4) | es'2( d'2) | c'2( aes4 c'4) | es'2( d'2) | aes2( f2) | g1 | }
sTwoVla = { g2(\mp^\markup \italic "arco, unis., espress." aes4 bes4) | aes2( g2) | aes4( bes4 c'2) | es'4( f'4 g'2) | es'2( c'4 es'4) | d'2( aes2) | bes2( c'4 bes4) | aes4( g4 f4 aes4) | g2( aes4 bes4) | aes2(\< g2) | bes2(\mf c'4 f'4) | es'2( d'2) | c'2( aes4 c'4) | es'2( d'2) | aes2( f2) | g1 | }
% c098 (expression; balance after c094): 67 the basses mp with the violas and cellos (were mf, a level above the counter-melody c094 lowered to mp), crescendo 76 to mf at 77 with them.
sTwoCb = { es,1\mp^\markup \italic "arco" | d,2 es,2 | c,1 | aes,,2 g,,2 | f,,1 | bes,,1 | es,2 c,2 | bes,,1 | g,,2 es,2 | d,2\< es,2 | g,,2\mf aes,,2 | c,1 | aes,,1 | aes,,2 bes,,2 | bes,,1 | es,1 \ottava #0 | }
sTwoBsnTwo = { es1\p | d2 es2 | c1 | aes,2 g,2 | f,1 | bes,1 | es2 c2 | bes,2. r4 | g,2 es2 | d2 es2 | g,2 aes,2 | c1 | aes,1 | aes,2 bes,2 | bes,1 | es1 | }
sTwoHarpR = { \stemUp es'8 g'8 bes'8 es''8 es'8 g'8 bes'8 es''8 | f'8 aes'8 bes'8 d''8 es'8 g'8 bes'8 es''8 | es'8 aes'8 c''8 es''8 es'8 aes'8 c''8 es''8 | es'8 aes'8 c''8 es''8 es'8 g'8 bes'8 es''8 | es'8 f'8 aes'8 c''8 es'8 f'8 aes'8 c''8 | f'8 bes'8 d''8 f''8 f'8 aes'8 bes'8 d''8 | es'8 g'8 bes'8 es''8 es'8 g'8 c''8 es''8 | f'8 bes'8 d''8 f''8 f'8 aes'8 bes'8 d''8 | es'8 g'8 bes'8 es''8 es'8 g'8 bes'8 es''8 | f'8 aes'8 bes'8 d''8 es'8 g'8 bes'8 es''8 | es'8 g'8 bes'8 es''8 es'8 f'8 aes'8 c''8 | es'8 g'8 c''8 es''8 f'8 bes'8 d''8 f''8 | es'8 aes'8 c''8 es''8 es'8 aes'8 c''8 es''8 | es'8 aes'8 c''8 es''8 f'8 bes'8 d''8 f''8 | f'8 aes'8 bes'8 d''8 f'8 aes'8 bes'8 d''8 | es'8 g'8 bes'8 es''8 es'8 g'8 bes'8 es''8 \stemNeutral | }
% c039 (Gould PDF 45: across extensive rests the notes take separate octave signs): the 8 bassa line closes at 82; it ran on over rests to 186.
% c075 (MOLA PDF 5): pedal diagram score-only (tag 'score)
sTwoHarpL = { \ottava #-1 \set Staff.ottavation = #"8" es,1\mf-\tag #'score ^\markup \small \line { \harp-pedal #"--^|^--^" \italic "(low D string: D♮)" } | d,2 es,2 | c,1 | aes,,2 g,,2 | f,,1 | bes,,1 | es,2 c,2 | bes,,1 | g,,2 es,2 | d,2 es,2 | g,,2 aes,,2 | c,1 | aes,,1 | aes,,2 bes,,2 | bes,,1 | es,1 \ottava #0 | }
% c047 (texture; Rimsky-Korsakov PDF 108: clarinets should rarely be set inside the horns; two horns and two bassoons give the soft four-part chord): Cl 1-2 rest 75-82, where Hn 1-2 enter; the pad passes from clarinets to horns
sTwoClOne = { R1*16 | }
sTwoClTwo = { R1*16 | }
sTwoBsnOne = { es1\p | d2 es2 | c1 | c2 es4 r4 | c1 | d1 | es2 c2 | d1 | es1 | d2 es2 | es2 c2 | c2 d4 r4 | c1 | c2 d2 | d1 | es1 | }
sTwoHnOne = { R1*8 | es'1\p | d'2 es'2 | es'2 c'2 | c'2 d'2 | c'1 | c'2 d'2 | d'1 | es'1 | }
sTwoHnTwo = { R1*8 | g1\p | aes2 g2 | g2 aes2 | g2 bes2 | c'1 | aes2 bes2 | aes1 | g1 | }
