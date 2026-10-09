% DEVELOPMENT, bars 77–130.
% D1 77–84 (8): motto-head dialogue, a new colour on every entry.
% D2 85–96 (12): fugato.  D3 97–102 (6): second theme in B minor (fugato ends in B♭ minor; shifted up a semitone at 97).
% D3a 103–110 (8, cycle 70): the two themes combined. 103–106 (f): first-theme head on top (Ob 2 + Cl 2; strings rest, cycles 74/76) over the second-theme head in the
%   tenor (Hn 1, Bsn 1), D minor → V of E minor; 107–110 (p): inverted, second-theme head on top (Fl 1 low + Va) over the first-theme
%   head in the bass (Vc, Bsn 2), E minor → B♭ minor → cadential 6/4 and V of F minor (the exposition's own pitches 49–50, D♭–C–B♭–D♭–F | A♭–G).
% D3b 111–116 (6): the wedge.  D4 117–130 (14): dominant pedal, trombone motto augmented, climax, collapse, retransition.

devFluteOne = {
  R1*4 | \partCombineSoloI r2 r8 g''8\f^\markup \bold "1." es'''4-> |
  \partCombineAutomatic r8 g''8\ff es'''4.-> d'''8 des'''8 c'''8 | aes''4-> r4 aes''4-> r4 | R1*10 | r8 f''8\f des'''4.-> c'''8-. ces'''8-. bes''8-. |
  bes''4\< a''8( bes''8) ges''4.-> f''8-. | r8 f''8 des'''4.-> c'''8-. ces'''8-. bes''8-. | \transpose c cis { r2. f''4(\ff | \ottava #1 des'''2.~ des'''8 c'''8 |
  bes''4 ges'''2-- f'''4) | es'''4.( des'''8 c'''4 \ottava #0 es''8 ges''8 | bes''2 a''2) | f''4( des'''2-- c'''8 g''8) } |
  % cycle 74: 107–110 Fl 1 in its low register doubles the violas on the second-theme head
  R1*4 | g'2.~(\mp^\markup \italic "espr." g'8 fis'8 | e'4 c''2-- b'4) | des''4.( c''8 bes'4 des''8 f''8 | aes''2\< g''4 c''4\!) |
  R1*4 |
  des'''4\f c'''4 es'''4 des'''4 | d'''1\< | \partCombineApart r8\ff b'8 aes''4.-> g''8 f''8 d''8 | r8 es''8 c'''4.-> b''8 c'''8 g''8 |
  r8 d''8 b''4-> r8 f''8 d'''4-> | r8 f''8 des'''4-> r8 bes''8 f'''4-> | es'''4.\< f'''8 g'''2 | \partCombineAutomatic aes'''1\fff |
  g'''1 | g''2.~\>( g''8 f''8)\! | R1*6 |
}
devFluteTwo = {
  R1*5 | r8 g'8\ff es''4.-> d''8 des''8 c''8 | f''4-> r4 f''4-> r4 | R1*27 |
  R1*4 |
  des''4\f c''4 es''4 des''4 | d''1\< | f''1\ff | g''1 |
  f''2. r4 | f''1 | g''1\< | d'''1\fff |
  d'''1 | R1*7 |
}
devOboeOne = {
  R1*2 | r8 b'8\mf( g''4.->) fis''8( f''8 e''8) | r2 r8 g'8\f es''4-> | R1 |
  \partCombineApart r8\ff g'8 es''4.-> d''8 des''8 c''8 | \partCombineAutomatic d''4-> r4 d''4-> r4 | R1*13 | \transpose c cis { r2. f'4(\ff | des''2.~ des''8 c''8 |
  bes'4 ges''2-- f''4) | es''4.( des''8 c''4 es''8 ges''8 | bes''2 a''2) | f''4( des'''2-- c'''8 g''8) } |
  % 103–110 (inserted, cycle 70): first-theme head over the second-theme head (lower octave of the violins)
  % cycle 76: Ob 1 rests 103-110 (it played 97-102 ff); Ob 2 takes the first-theme head
  R1*4 | R1*4 |
  R1*4 |
  des''4\f c''4 es''4 des''4 | d''1\< | r8\ff b8 aes'4.-> g'8 f'8 d'8 | r8 es'8 c''4.-> b'8 c''8 g'8 |
  r8 d'8 b'4-> r8 f'8 d''4-> | r8 f'8 des''4-> r8 bes'8 f''4-> | es''4.\< f''8 g''2 | aes''1\fff |
  g''1 | g''2.~\>( g''8 f''8 | es''4. d''8 c''2) | d''1\p |
  R1*4 |
}
devOboeTwo = {
  R1*5 | c''1\ff | b'4-> r4 b'4-> r4 | R1*19 |
  \partCombineSoloII r8 a'8(\f f''4.->) e''8( es''8 d''8 | d''4) cis''8( d''8) g''4.-> f''8 | r8 d''8( bes''4.->) a''8( aes''8 g''8 | b''4) ais''8( b''8) g''4.->\> fis''8 | R1\! | R1*3 |
  \partCombineSoloII aes'1\mp\cresc | bes'1 | c''1 | c''2 b'2 |
  \partCombineAutomatic aes'1\f | aes'2\< a'2 | R1\! | R1*4 | f'1\fff |
  f'1 | R1*7 |
}
devCorAnglais = {
  % c096: part-only cue (82 bars rest before an off-beat fugato entry); removed from the full score by \removeWithTag #'part in score.ly
  R1*12 | \tag #'score R1*2 \tag #'part \cueDuring #"cueVla" #DOWN { s4*0^\markup \fontsize #-3 "Vla." R1*2 } | r8 c'8\f aes'4.-> g'8-. ges'8-. f'8-. | f'4 e'8( f'8) des'4.-> c'8-. | f'4-. g'4-. aes'4-. a'4-. |
  R1*4 | \transpose c cis { des'2.~\ff( des'8 c'8 | bes4 ges'2-- f'4) | es'4.( des'8 c'4 es'8 ges'8 | bes'2 a'2) | f'4( des''2-- c''8 g'8) } |
  R1*28 |
}
devClOne = {
  r2 r8 es''8\mp( ces'''4->~ | ces'''8) bes''8( beses''8 aes''8 aes''2) | R1 | r2 r8 g'8\f es''4-> |
  R1 | \partCombineApart r8 g'8\ff es''4.-> d''8 des''8 c''8 \partCombineAutomatic | aes'4-> r4 aes'4-> r4 | R1*10 |
  bes4.\f c'8 des'8( es'8) f'4 | des'4\< c'8( bes8) es'4. des'8 | r8 des''8 bes''4.-> a''8-. aes''4 | \transpose c cis { des'8\f f' bes' f' des' f' bes' f' |
  des' f' bes' f' des' f' bes' f' | es' ges' bes' ges' es' ges' bes' ges' | c' es' ges' es' c' es' ges' es' | c' es' bes' es' c' es' a' es' |
  des' f' bes' f' c' es' a' r } |
  % critic 84: Cl 1 joins Cl 2 and Ob 2 on the first-theme head 103-106 (balance against Hn 1 + Bsn 1 after the ff tutti)
  r8^\markup \bold "a2" a'8(\f f''4.->) e''8( es''8 d''8 | d''4) cis''8( d''8) g''4.-> f''8 | r8 d''8( bes''4.->) a''8( aes''8 g''8 | b''4) ais''8( b''8) g''4.^>\> fis''8 | R1\! | R1*3 |
  aes'1\mp\cresc | bes'1 | c''1 |
  c''2 b'2 | aes'1 | aes'2\ff a'4 r4 | \tuplet 3/2 { b8 d' f' } \repeat unfold 3 { \tuplet 3/2 { b8 d' f' } } |
  \omit Staff.TupletNumber \repeat unfold 4 { \tuplet 3/2 { c'8 es' g' } } | \repeat unfold 4 { \tuplet 3/2 { b8 d' f' } } | \repeat unfold 3 { \tuplet 3/2 { bes8 des' f' } } r4 | \repeat unfold 4 { \tuplet 3/2 { c'8 es' g' } } | \undo \omit Staff.TupletNumber
  f''1\fff | d''1 | f''2.\> r4 | es'1 |
  d'1-\tweak X-offset #-2 \p | r8 g8\pp\<( es'4.->) d'8( des'8 c'8 | c'4) b8( c'8) aes4.-> g8 | g4\mf( es'2 d'4 |
  des'4 c'2.) |
}
devClTwo = {
  R1*5 | r8 es'8\ff r8 es'8 r8 es'8 r8 es'8 | f'4-> r4 f'4-> r4 | R1*13 |
  \transpose c cis { des'8\f f' bes' f' des' f' bes' f' | des' f' bes' f' des' f' bes' f' | es' ges' bes' ges' es' ges' bes' ges' | c' es' ges' es' c' es' ges' es' |
  c' es' bes' es' c' es' a' es' | des' f' bes' f' c' es' a' r } |
  % cycle 74: Cl 2 doubles Ob 1 on the first-theme head 103–106 (strings rest)
  r8 a'8(\f f''4.->) e''8( es''8 d''8 | d''4) cis''8( d''8) g''4.-> f''8 | r8 d''8( bes''4.->) a''8( aes''8 g''8 | b''4) ais''8( b''8) g''4.^>\> fis''8 | R1*4\! | f'1\mp\cresc | g'2. r4 |
  g'1~( | g'4 f'2.) | f'1 | fis'2.\ff r4 |
  \tuplet 3/2 { b8 d' f' } \repeat unfold 3 { \tuplet 3/2 { b8 d' f' } } | \omit Staff.TupletNumber \repeat unfold 4 { \tuplet 3/2 { c'8 es' g' } } | \repeat unfold 4 { \tuplet 3/2 { b8 d' f' } } | \repeat unfold 4 { \tuplet 3/2 { bes8 des' f' } } |
  \repeat unfold 4 { \tuplet 3/2 { c'8 es' g' } } \undo \omit Staff.TupletNumber | b'1\fff | b'2. r4 | d'1\> |
  c'1 | c'4-\tweak X-offset #-2 \p( b2.) | R1*4 |
}
devBassCl = {
  R1*14 | f,1\f | bes,2^\markup \small "(low C instr.)" c,2 | des,2 c,2 |
  bes,1 | es,2\< f,2 | bes,4 r4 bes,4 r4 | \transpose c cis { bes,1\ff |
  bes,1 | es1 | c2. r4 | f,1 |
  f,1 } |
  d,1\f | d,4 g,2 a,4 | bes,,2 c,2 | b,,2.\> r4\! |
  % c094: B.cl alone on the first-theme head in the bass 107–109 (was Bsn 2 + Vc in unison; same notes and octave), its only line of its own in the movement
  r8\p b,8(^\markup \italic "espr." g4.->) fis8( f8 e8 | e4) g8( fis8) b,2 | r8 f,8( des4.->) c8( ces8 bes,8 | c1\<) | f1\mp\cresc | e1 | es2. r4 |
  d1 | des1 | c1 | g,1\ff~ |
  g,1~ | g,1~ | g,2. r4 | g,1\<~ |
  g,1\fff~ | g,2. r4 | g,1\>~ | g,1~ |
  g,1\pp | R1*4 |
}
devBsnOne = {
  \set Staff.soloText = "1. Solo" r8 es8\mf_\markup \italic "espr."( ces'4.->) bes8( beses8 aes8 | \set Staff.soloText = "1." aes2) r2 | R1 | \partCombineApart r8\f g,8 es4-> r2 |
  r8 g8 es'4-> r2 | \partCombineAutomatic c'2\ff c'2 | b4-> r4 b4-> r4 | R1*4 |
  r8 g8\mf es'4.-> d'8-. des'8-. c'8-. | c'4 b8( c'8) aes4.-> g8-. | c'4-. d'4-. es'4-. e'4-. | f4.\f g8 aes8( bes8) c'4 |
  aes4 g8( f8) bes4. aes8 | f2 g2 | bes2 bes2~ | bes2\< des2 |
  r4. f8 des'4.-> c'8 | \transpose c cis { ces'8\ff bes8 r4 r2 | bes2 r8 f8 des'8 c'8 | bes2 r8 es8 ges8 bes8 |
  c'2 r8 ges8 es'8 des'8 | c'2 a2 | bes2 r8 f8 a8 c'8 } |
  f2.~(\f f8 e8 | d4 bes2-- a4) | g4.( f8 e4 g8 b8 | e'2\> dis'2) |
  R1\! | R1*2 | c2\p\< g2 |
  f1\mp\cresc |
  g1 | g1~( | g4 f2.) | f1 |
  fis2. r4 | g1\ff | es'1~ | es'2. \partCombineApart d'4 |
  \partCombineAutomatic des'2. c'4~ | c'1\< | aes1\fff | g1 |
  g2.\> r4 | g1 | g1\p | R1*3 |
  \partCombineSoloI g,4(\f\<^\markup \bold "1." es2 d4) |
}
devBsnTwo = {
  R1*3 | c1\f | c1 | aes,8\ff aes,8 aes,8 aes,8 aes,8 aes,8 aes,8 aes,8 |
  g,4-> r4 g,4-> r4 | R1*7 | f,1\f | bes,,2 c,2 |
  des,2 c,2 | bes,,1 | es,2\< f,2 | bes,,4 r4 bes,,4 r4 |
  \transpose c cis { bes,1\ff | bes,1 | es1 | c2. r4 |
  f,1 | f,1 } |
  d,1\f | d,4 g,2 a,4 | bes,,2 c,2 | b,,1\> |
  R1\! | R1*2 | c,1\p\< |
  f,1\mp\cresc | e,1 |
  es,2. r4 | d,1 | des,1 | c,1 |
  g,1\ff~ | g,1~ | g,2. r4 | g,1~ |
  g,1\<~ | g,1\fff~ | g,1~ | g,2. r4\> |
  g,1~ | g,1\p | R1*4 |
}
devCbsn = {
  R1*5 | aes,,1\ff | g,,4-> r4 g,,4-> r4 | R1*12 |
  bes,,4\f r4 bes,,4 r4 | \transpose c cis { bes,,1\ff | bes,,1 | es,1 |
  c,1 | f,,1 | f,,2. r4 } |
  R1*8 | f,1\mp\cresc |
  e,1 | es,1 | d,1 | des,1 |
  c,1 | g,,1\ff~ | g,,2. r4 | g,,1~ |
  g,,1~ | g,,2. r4 | g,,1\fff~ | g,,1~ |
  g,,2. r4\> | g,,1~ | g,,1\pp | R1*4 |
}
devHnOne = {
  R1 | r2 r8 b8\mf( g'4->~ | g'8) fis'8( f'8 e'8 e'2) | R1*2 |
  aes'1\ff | aes'4-> r4 aes'4-> r4 | R1*12 | r4. f8\f des'4.-> c'8 |
  \transpose c cis { ces'8\ff bes8 r4 r2 | bes2 r8 f8 des'8 c'8 | bes2 r8 es8 ges8 bes8 | c'2 r8 ges8 es'8 des'8 |
  c'2 a2 | bes2 r2 } |
  f'2.~(\mf f'8 e'8 | d'4 bes'2-- a'4) | g'4.( f'8 e'4 g'8 b'8 | e''2\> dis''2) | R1*4\! |
  aes'1\p\cresc | bes'1 |
  c''1 | c''2 b'2 | aes'1 | aes'2 a'4 r4 |
  \partCombineUnisono g1\ff | es'1~ | es'2. d'4 | des'2. c'4~ |
  c'1 | \partCombineAutomatic aes'1\fff | g'1 | R1*7 |
}
devHnTwo = {
  R1 | r2 r8 b8\mf(^\markup \bold "a2" g'4->~ | g'8) fis'8( f'8 e'8 e'2) | R1*2 |
  es'1\ff | f'4-> r4 f'4-> r4 | R1*12 | r4. f8\f des'4.-> c'8 |
  \transpose c cis { ces'8\ff bes8 r4 r2 | bes2 r8 f8 des'8 c'8 | bes2 r8 es8 ges8 bes8 | c'2 r8 ges8 es'8 des'8 |
  c'2 a2 | bes2 r8 f8 a8 c'8 } |
  R1*8 | f'1\p\cresc | g'1 |
  g'1~( | g'4 f'2.) | f'1 | fis'2. r4 |
  g1\ff | es'1~ | es'2. d'4 | des'2. c'4~ |
  c'1 | f'1\fff | f'1 | R1*7 |
}
devHnThree = {
  R1*3 | r8 g8\f es'4-> r2 | r8 g8 es'4-> r2 | c'1\ff |
  d'4-> r4 d'4-> r4 | R1*2 | R1*11 | \transpose c cis { des'1\f |
  des'2. r4 | ges'1 | ges'1 | es'1 |
  des'2 c'4 r4 } |
  \clef bass d'1\mp | d'4 d'2 cis'4 | d'2 e'2 | fis'2\> b2 | R1*3\! | \clef treble \partCombineSoloI c'1\pp\< | \partCombineAutomatic
  c'1\p\cresc | c'1 | es'1 |
  d'1 | des'1 | d'2. r4 | g'1\ff |
  g'1 | g'1 | g'2. r4 | g'1 |
  d'1\fff | d'1 | b1\> | c'1 |
  c'4\p( b2.) | R1*4 |
}
devHnFour = {
  R1*3 | r8 g8\f es'4-> r2 | r8 g8 es'4-> r2 | aes1\ff |
  b4-> r4 b4-> r4 | R1*2 | R1*11 | \transpose c cis { bes1\f |
  bes1 | bes1 | bes1 | bes2 a2 |
  bes2 a4 r4 } |
  a1\mp | f4 g2 e4 | d2 c2 | b,1\> | R1*3\! | R1 |
  f1\p\cresc | g2. r4 | g1~( |
  g4 f2.) | f2. r4 | fis1 | g1\ff |
  g1 | g2. r4 | g1 | g1 |
  g1\fff | g2. r4 | g1\> | g1 |
  g2.\p r4 | g1\pp\<~ | g1~ | g1\mf~ |
  g1\f\< |
}
devTptOne = {
  R1*5 | \partCombineApart r8\ff g'8 es''4.-> d''8 des''8 c''8 | \partCombineAutomatic d''4-> r4 d''4-> r4 | R1*27 |
  aes'2.~(\p\cresc aes'8 g'8) | bes'2.~( bes'8 a'8) | c''2.~( c''8 b'8) | c''4.( b'8 f'4 aes'8 c''8) |
  des''4 c''4 es''4 des''4 | d''1\ff | R1*5 | aes'1\fff |
  g'1 | R1*7 |
}
devTptTwo = {
  R1*5 | aes'1\ff | aes'4-> r4 aes'4-> r4 | R1*27 |
  f'1\p\cresc | g'1 | g'1~( | g'4 f'2.) |
  f'1 | fis'1\ff | R1*5 | d'1\fff |
  d'1 | R1*7 |
}
devTptThree = {
  R1*5 | es'1\ff | b4-> r4 b4-> r4 | R1*27 |
  c'1\p\cresc | c'1 | es'1 | d'1 |
  des'1 | d'1\ff | R1*5 | b1\fff |
  b1 | R1*7 |
}
devTbnOne = {
  R1*3 | r8 g,8\f es4-> r2 | r8 g8 es'4-> r2 | c'1\ff |
  aes4-> r4 aes4-> r4 | R1*12 | r4. f8\f des'4.-> c'8 | \transpose c cis { ces'8\ff bes8 r4 r2 |
  bes2 r8 f8 des'8 c'8 | bes2 r8 es8 ges8 bes8 | c'2 r8 ges8 es'8 des'8 | c'2 a2 |
  bes2 r8 f8 a8 c'8 } | R1*10 | g1~(\mp\cresc |
  g4 f2.) | f1 | fis2. r4 | \partCombineUnisono g1\ff |
  es'1~ | es'2. d'4 | des'2. c'4~ | c'2.. r8 | % c087: eighth breath at 121 (Tchaikovsky 6/i 134 tuba)
  \partCombineAutomatic aes1\fff | g1 | g1\> | R1\! |
  R1*5 |
}
devTbnTwo = {
  R1*3 | r8 g,8\f es4-> r2 | r8 g8 es'4-> r2 | aes1\ff |
  f4-> r4 f4-> r4 | R1*27 | R1*2 |
  % c087: Tbn 2 breathes at 115 beat 4 and holds A2 through 116, so the low brass do not all breathe on beat 4 of 116
  c1\mp\cresc | c2 b,2 | aes,2. r4 | aes,2 a,2 |
  g1\ff | es'1~ | es'2. d'4 | des'2. c'4~ |
  c'2.. r8 | f1\fff | f1 | g1\> |
  R1\! | R1*5 |
}
devBassTbn = {
  R1*5 | aes,1\ff | g,4-> r4 g,4-> r4 | R1*12 |
  bes,4\f r4 bes,4 r4 | \transpose c cis { bes,1\ff | bes,1 | es1 |
  c1 | f,1 | f,1 } | R1*8 | R1 |
  R1*2 | d,1\mp\cresc | des,1 |
  c,2. r4 | g,1\ff | es1~ | es2. d4 |
  des2. c4~ | c2.. r8 | b,1\fff | b,1 |
  g,1\> | R1\! | R1*5 |
}
devTuba = {
  R1*5 | aes,,1\ff | g,,4-> r4 g,,4-> r4 | R1*27 |
  % c087: tuba breathes at 114 beat 4 (B.tbn holds the same D2) and holds C2 through 116
  f,1\p\cresc | e,1 | es,1 | d,2. r4 |
  des,1 | c,1 | g,,1\ff~ | g,,1~ |
  g,,2. r4 | g,,1~ | g,,1\<~ | g,,2.\fff r4 |
  g,,1\>~ | g,,1~ | g,,2. r4 | g,,1\pp |
  R1*4 |
}
devTimp = {
  R1*3 | c1:32\f\< | c1:32 | aes,8\ff aes,8 aes,8 aes,8 aes,8 aes,8 aes,8 aes,8 |
  g,4-> r4 g,4-> r4 | R1^\markup \small "muta C in B♮" | R1*12 |
  \transpose c cis { bes,4\ff r4 r2 | R1*4 | R1 } | R1*8 | R1^\markup \small "muta B♮ in C" |
  R1*3 | aes,1:32\mf\< | R1\! | g,1:32\ff~ |
  g,1:32~ | g,1:32~ | g,1:32~ | g,1:32\< |
  g,1:32\fff~ | g,1:32~ | g,1:32\>~ | g,1:32~ |
  g,1:32\pp~ | g,1:32\<~ | g,1:32~ | g,1:32\mf~ |
  g,1:32\f\< |
}
devPerc = \drummode { R1*45 | tt1\fff\laissezVibrer^\markup { "1: Tam-tam" \italic "hard beater, l.v." } | R1*8 | }
devVlnOne = {
  R1*2 | r8 b'8\mf( g''4.->) fis''8( f''8 e''8) | r2 r8 g'8\f es''4-> | r2 r8 g''8 es'''4-> |
  r8 g''8\ff es'''4.-> d'''8 des'''8 c'''8 | <b' aes''>4-> r4 <b' aes''>4-> r4 | R1*10 | r8 f''8\f des'''4.-> c'''8-. ces'''8-. bes''8-. |
  bes''4\< a''8( bes''8) ges''4.-> f''8-. | r8 f''8 des'''4.-> c'''8-. ces'''8-. bes''8-. | \transpose c cis { r2. f'4(\ff | des''2.~ des''8 c''8) |
  bes'4( ges''2-- f''4) | es''4.( des''8 c''4 es''8 ges''8) | bes''2( a''2) | f''4( des'''2-- c'''8 g''8) } |
  % 103–110 (inserted, cycle 70): the two theme heads combined; 103–106 P head over S head in the tenor (D minor → V of E minor), 107–110 inverted (S head on top, P head in the bass), into F minor at 111
  % cycle 74: Vln I rest 103–110 (103–106 winds and horns alone; 107–110 violas and low flute), re-entering with Tpt 1 at 111
  R1*8 |
  aes''2.~(\mp\cresc aes''8 g''8) | bes''2.~( bes''8 a''8) | c'''2.~( c'''8 b''8) | c'''4.( b''8 f''4 aes''8 c'''8) |
  des'''4 c'''4 es'''4 des'''4 | d'''1 | r8 b'8\ff aes''4.-> g''8 f''8 d''8 | r8 es''8 c'''4.-> b''8 c'''8 g''8 |
  r8 d''8 b''4-> r8 f''8 d'''4-> | r8 f''8 des'''4-> r8 bes''8 f'''4-> | \ottava #1 es'''4.\< f'''8 g'''2 | aes'''1:32\fff |
  g'''1:32 \ottava #0 | g''2.~\>( g''8 f''8 | es''4. d''8 c''2) | d''1\p |
  R1*4 |
}
devVlnTwo = {
  es'1:32\p | es'2:32 e'2:32 | e'1:32 | es'1:32\< |
  es'1:32 | r8 g'8\ff es''4.-> d''8 des''8 c''8 | <d'' f''>4-> r4 <d'' f''>4-> r4 | R1*7 |
  r8 c''8\f aes''4.-> g''8-. ges''8-. f''8-. | f''4 e''8( f''8) des''4.-> c''8-. | f''4-. g''4-. aes''4-. a''4-. | bes'4. c''8 des''8( es''8) f''4 |
  des''4\< c''8( bes'8) es''4. des''8 | r8 des''8 bes''4.-> a''8-. aes''4 | \transpose c cis { r1\! | des'2.~(\ff des'8 c'8) |
  bes4( ges'2-- f'4) | es'4.( des'8 c'4 es'8 ges'8) | bes'2( a'2) | f'4( des''2-- c''8 g'8) } |
  R1*4 |
  << { e'1\pp^"div." | e'2( dis'2) | f'1( | f'2\< e'2) } \\ { b1\pp | g4( a2.) | bes2( des'2 | c'1\<) } >> |
  <c' f'>1:32\mp\cresc | <g' bes'>1:32 | <g' c''>1:32 | <g' c''>4:32 <f' c''>4:32 <f' b'>2:32 |
  <f' aes'>1:32 | <fis' aes'>2:32 <fis' a'>2:32 | r8^"unis." b8\ff aes'4.-> g'8 f'8 d'8 | r8 es'8 c''4.-> b'8 c''8 g'8 |
  r8 d'8 b'4-> r8 f'8 d''4-> | r8 f'8 des''4-> r8 bes'8 f''4-> | es''4.\< f''8 g''2 | <d'' aes''>1:32\fff |
  <d'' g''>1:32 | <d' f'>1\> | es'1 | d'1\p |
  R1*3 | g'4(\f\< es''2 d''4) |
}
devVla = {
  ces'1:32\p | ces'2:32 b2:32 | b1:32 | c'1:32\< |
  c'1:32 | r8 g8\ff es'4.-> d'8 des'8 c'8 | <b f'>4-> r4 <b f'>4-> r4 | R1*4 |
  r8 g8\mf es'4.-> d'8-. des'8-. c'8-. | c'4 b8( c'8) aes4.-> g8-. | c'4-. d'4-. es'4-. e'4-. | f'4.\f g'8 aes'8( bes'8) c''4 |
  aes'4 g'8( f'8) bes'4. aes'8 | f'2 e'2 | f'1~( | f'4\< ges'4) bes2 |
  r8 des'8 bes'4.-> a'8-. aes'4 | \transpose c cis { bes'8\f f' des' f' bes' f' des' f' | f' des' bes des' f' des' bes des' | bes' ges' es' ges' bes' ges' es' ges' |
  ges' es' c' es' ges' es' c' es' | bes' es' c' es' a' es' c' es' | bes' f' des' f' a' es' c' es' } |
  R1*4 |
  g'2.~(\p^\markup \italic "espr." g'8 fis'8 | e'4 c''2-- b'4) | \clef treble des''4.( c''8 bes'4 des''8 f''8 | aes''2\< g''4 c''4) | \clef alto
  c'8\mp\cresc c'8 b8( c'8) c'8 c'8 b8( c'8) |
  c'8 c'8 bes8( c'8) c'8 c'8 bes8( c'8) | c'8 c'8 b8( c'8) c'8 c'8 b8( c'8) | c'8 c'8 b8( c'8) aes8 aes8 g8( aes8) | aes8 aes8 bes8( aes8) aes8 aes8 bes8( aes8) |
  c'8 c'8 b8( c'8) c'8 c'8 b8( c'8) | \tuplet 3/2 { b8\ff d' f' } \repeat unfold 3 { \tuplet 3/2 { b8 d' f' } } | \omit TupletNumber \repeat unfold 4 { \tuplet 3/2 { c'8 es' g' } } | \repeat unfold 4 { \tuplet 3/2 { b8 d' f' } } |
  \repeat unfold 4 { \tuplet 3/2 { bes8 des' f' } } | \repeat unfold 4 { \tuplet 3/2 { c'8 es' g' } } \undo \omit TupletNumber | <b d'>1:32\fff | <b d'>1:32 |
  b1\> | c'1 | c'4\p( b2.)~ | b2. r4 | R1 |
  r2 g4(\mf\< es'4~ | es'4 d'4 des'4 c'4) |
}
devVc = {
  R1 | r2 r8 b,8\mf( g4->~ | g8) fis8( f8 e8 e2) | r8 g,8\f es4-> r2 |
  r8 g8 es'4-> r2 | aes,2\ff aes,2 | g4-> r4 g4-> r4 | g,1\subP |
  r8 d8\mf bes4.-> a8-. aes8-. g8-. | g4 fis8( g8) es4.-> d8-. | g4-. a4-. bes4-. b4-. | c'4. d'8 es'8( f'8) g'4 |
  es'4 d'8( c'8) f'4. es'8 | aes2 g2 | c'2. es'4~( | es'4 des'4) c'2~( |
  c'4 bes4) g2 | bes2\f bes2~ | bes2\< des2 | r4. f8 des'4.-> c'8 |
  \transpose c cis { bes,1\ff | bes,1 | es1 | c1 |
  f,1 | f,1 } |
  R1*4 |
  R1*3 | c2\p\< g2 |
  f1\mp\cresc | g1 |
  g1~ | g4 f2. | f1 | fis1 |
  g,1:16\ff | g,1:16 | g,1:16 | g,1:16 |
  g,1:16 | aes1\fff | g1 | <g b>1\>^"div." |
  <g c'>1 | <g c'>4\p( <g b>2.) | g,4\pp\<^"unis." g,4 g,4 g,4 | g,8 g,8 g,8 g,8 g,8 g,8 g,8 g,8 |
  \tuplet 3/2 { g,8\mf g,8 g,8 } \repeat unfold 3 { \tuplet 3/2 { g,8 g,8 g,8 } } | g,16\f\< g,16 g,16 g,16 \repeat unfold 12 { g,16 } |
}
devCb = {
  aes,,1\p | aes,,2 e,2 | e,1 | c,1\< |
  c,1 | aes,,8\ff aes,,8 aes,,8 aes,,8 aes,,8 aes,,8 aes,,8 aes,,8 | g,,2-> g,,2-> | g,,1\subP |
  d,4\mf^"pizz." r4 r2 | g,4 r4 es,4 r4 | g,4 r4 bes,4 r4 | R1*2 |
  aes,2\mf^"arco"\< g,2 | f,1\f | bes,,2 c,2 | des,2 c,2 |
  bes,,1 | es,2\< f,2 | bes,,4 r4 bes,,4 r4 | \transpose c cis { bes,,1\ff |
  bes,,1 | es,1 | c,1 | f,,1 |
  f,,1 } |
  R1*4 |
  e,4\p^"pizz." r4 r2 | e,4 r4 b,,4 r4 | bes,,4 r4 r2 | c,1\p\<^"arco" |
  f,1\mp\cresc | e,1 | es,1 |
  d,1 | des,1 | c,1 | g,,1\ff~ |
  g,,1~ | g,,1~ | g,,1~ | g,,1\<~ |
  g,,1\fff~ | g,,1~ | g,,1\>~ | g,,1~ |
  g,,1\pp~ | g,,1\<~ | g,,1~ | g,,1\mf~ |
  g,,1\f\< |
}
