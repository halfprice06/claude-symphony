% RECAPITULATION, second theme in C major, bars 139–162. A = 139–147 (horn + violas), A' = 148–162 (violins, brass at the ♭VI climax).
% 152–153: the tune's chromatic descent (exposition 60–61) falls on the motto's own pitches D–D♭–C; spelled D♭ (passing tone over B♭ → F minor).

recTwoMelodyA = { e''2.~ e''8 d''8 | c''4 a''2-- g''4) | f''4.(\< e''8 d''4 f''8 a''8 | c'''2 b''2) | }
recTwoMelodyB = {
  d'''2.~( d'''8 des'''8 | c'''2 bes''4 aes''8 g''8) | g''4\ff\downbow e'''2.~ | e'''4\< f'''4 g'''2 |
  c'''4\fff\downbow aes'''2~ aes'''8 g'''8 | f'''2 d'''4( b''8 c'''8) | a''2.~(\ff a''8 gis''8) | a''4.\>( g''8 f''4 a''8 c'''8) |
  d'''2\mp( c'''2\> | b''4 a''8 g''8 f''4 d''4) | c''2\p~ c''2\< |
}
recTwoCounter = {
  r4 c''4(\mp b'4 bes'4 | a'2) c''2~( | c''4 bes'4 a'2 | g'2 f'2) |
  f'2\< r8 f'8( g'8 a'8 | aes'2) f'2 | g'2\ff c''2 | b'2\< f'2 |
  es'4\fff c''4 r8 c''8( bes'8 aes'8 | aes'2) f'2 | e'2\ff\> r8 e'8( f'8 g'8 | f'2) c''2 |
  f'4\mp aes'8( b'8) d''2~ | d''2( b'4 f'4) | e'2 es'2\< |
}
recTwoMelody = { \recTwoMelodyA \recTwoMelodyB }
recTwoSync = {
  r4 g'4~\mp g'8 f'8( e'8 c'8) | r4 a'4~ a'8 g'8( f'8 c'8) | r4 d'4~ d'8 c'8( b8 a8) | r4 g4~ g8 b8( d'8 f'8) |
  r8 d'8(\< f'8 bes'8 d''4) r4 | r8 c'8( f'8 aes'8 c''4) r4 | g4\ff e'2.~ | e'4\< f'4 g'2 |
  c'4\fff aes'2~ aes'8 g'8 | f'2 d'4( b8 c'8) | r4 e'4~\ff\> e'8 d'8( c'8 b8) |
  r4 c'4~ c'8 a8( c'8 f'8) | r4 f'4~\mp f'8 e'8( d'8 g8) | r4 g4~ g8 b8( d'8 b8) | <e' g'>2\mp <es' g'>2\< |
}
recTwoArp = {
  c8\p( g c' e' g'2) | a'8( f' c' a f2) | a'8( f' d' a f2) | g,8( d f b d'2) |
  bes,8(\< d bes4.) a8( aes8 g8) | f,8( c f aes c'2) | \clef tenor g4\ff e'2.~ | e'4\< f'4 g'2 |
  c'4\fff aes'2~ aes'8 g'8 | f'2 d'4( b8 c'8) | \clef bass a,8(\ff\> e a c' e'2) | f,8( c f a c'2) |
  d,8(\mp aes, d f) g,2 | g,8(\> d f b f2) | c,8(\p g, c e es2\<) |
}

recTwoFluteOne = {
  R1*15 |
  \partCombineUnisono g''4\ff( e'''2.~ | e'''4\< f'''4 g'''2) | c'''4(\fff aes'''2~ aes'''8 g'''8 |
  f'''2 d'''4 b''8 c'''8) | \partCombineAutomatic a''2.~(\ff a''8 gis''8) | a''4.\>( g''8 f''2)\! | R1*3 |
}
recTwoFluteTwo = {
  R1*15 |
  g''4\ff( e'''2.~ | e'''4\< f'''4 g'''2) |
  c'''4(\fff aes'''2~ aes'''8 g'''8 | f'''2 d'''4 b''8 c'''8) | R1*5 |
}
recTwoOboeOne = {
  R1*15 | g'4\ff( e''2.~ |
  e''4\< f''4 g''2) | c''4(\fff aes''2~ aes''8 g''8 | f''2 d''4 b'8 c''8) | R1*5 |
}
recTwoOboeTwo = { R1*15 | g'2\ff c''2 | b'2\< f'2 | es'4\fff c''4 r8 c''8( bes'8 aes'8 | aes'2) f'2 | R1*5 | }
recTwoCorAnglais = {
  r2 r8 g'8(\p a'8 b'8 | c''2) r2 | r2 r8 a'8( b'8 c''8 | d''2) r2 |
  r2 r8 bes'8( a'8 g'8 | a'2) r2 | c''1 | g'2 f'2 | e'2 r2 |
  R1*15 |
}
recTwoClOne = { R1*5 | r2. f''4~(\mp | f''4 e''8 d''8 c''4 a'4) | R1*2 | \recTwoCounter }
recTwoClTwo = { R1*15 | e'1\ff | d'1\< | c'1\fff | d'1 | R1*5 | }
recTwoBsnOne = {
  R1*9 | c1\mp | c1 | d2 f,2 | g,2. r4 |
  f,1\mf\< | \partCombineUnisono f,1 | g,1\ff | g,1\< | aes,1\fff | \partCombineAutomatic d2 g,4 r4 | e,1\ff\> | \partCombineUnisono f,1 | \partCombineAutomatic d,2\mp \partCombineUnisono g,2~ | g,1\> | \partCombineAutomatic c,2.\p r4 |
}
recTwoBsnTwo = {
  c1\pp | f1 | d1 | g,1 |
  e1 | f1 | d1 | g1 |
  c2 r2 | R1*3 |
  R1 | bes,1\mf\< | f,1 | g,1\ff |
  g,1\< | aes,1\fff | d2 g,2 | a,2.\ff\> r4 |
  f,1 | d2\mp g,2~ | g,1\> | c2.\p r4 |
}
recTwoCbsn = { R1*15 | g,,1\ff | g,,1\< | aes,,1\fff | d,2 g,,2 | R1*5 | }
recTwoHnOne = {
  e'2.~\< e'8 d'8\> | c'4\! a'2--\< g'4\!) | f'4.( e'8 d'4 f'8\< a'8 | c''2\> b'2\!) |
  g4( e'2--\< d'4\!) | c'4.(\> b8 a2\!) | R1 | c''4(\> b'4 d''4 f'4) |
  e'1\p | R1*4 | f'1\mf\< | f'1 |
  g4\ff e'2.~ | e'4\< f'4 g'2 | c'4\fff aes'2~ aes'8 g'8 | f'2 d'4( b8 c'8) |
  e'1\ff\> | R1 | f'1\p | f'1 |
  e'2\mp es'2\< |
}
recTwoHnTwo = {
  R1*9 | r4 c''4(\mp^\markup \italic "espr." b'4 bes'4 | a'2) c''2~( | c''4 bes'4 a'2 | g'2 f'2) | d'1\mf\< | c'2. r4 | g4\ff e'2.~ |
  e'4\< f'4 g'2 | c'4\fff aes'2~ aes'8 g'8 | f'2 d'4( b8 c'8) | c'1\ff\> |
  c'1 | c'2\p r2 | R1 | c'2\mp~ c'2\< |
}
recTwoHnThree = {
  R1*13 | bes1\mf\< | aes1 | g'2\ff c''2 |
  b'2\< f'2 | es'4\fff c''4 r8 c''8( bes'8 aes'8 | aes'2) f'2 | \clef bass a1\ff\> |
  R1 | aes2\p a2 | b1 | g1\mp |
}
recTwoHnFour = { R1*13 | f1\mf\< | f1 | g1\ff | g1\< | aes1\fff | f2 g2 | e1\ff\> | f1 | d2\p g2 | R1 | c1\mp | }
recTwoTptOne = {
  R1*15 | g'4\ff e''2.~ | e''4\< f''4 g''2 | c''4\fff aes''2~ aes''8 g''8 |
  f''2 d''4( b'8 c''8) | c''2\ff\>~ c''2\mp | R1*4 |
}
recTwoTptTwo = {
  R1*15 | g'1\ff | g'1\< | aes'1\fff |
  f'2 f'2 | e'2\ff\>~ e'2\mp | R1*4 |
}
recTwoTptThree = {
  R1*15 | c'1\ff | b1\< | c'1\fff |
  b1 | c'2\ff\>~ c'2\mp | R1*4 |
}
recTwoTbnOne = {
  R1*15 | c'1\ff | b1\< | c'1\fff |
  b1 | c'2\ff\>~ c'2\mp | R1*4 |
}
recTwoTbnTwo = {
  R1*15 | g1\ff | g1\< | es1\fff |
  f2 f2 | e2\ff\>~ e2\mp | R1*4 |
}
recTwoBassTbn = {
  R1*15 | g,1\ff | g,1\< | aes,1\fff |
  d2 g,2 | a,2\ff\>~ a,2\mp | R1*4 |
}
recTwoTuba = {
  R1*15 | g,,1\ff | g,,1\< | aes,,1\fff |
  d,2 g,,2 | a,,2\ff\>~ a,,2\mp | R1*4 |
}
recTwoTimp = { R1*15 | g,1:32\ff | g,1:32\< | aes,1:32\fff | g,2:32\> r2\! | R1*4 | r2 c2:32\p\< | }
recTwoPerc = \drummode { R1*16 | cymr1:32\pp\<\laissezVibrer^\markup { "2: Susp. cym." \italic "soft sticks, l.v." } | cymc1\fff\laissezVibrer^\markup { "1: Crash cym." \italic "l.v." } | R1*6 | }
recTwoHarpR = {
  % 148–162: one rolled chord per harmony on beat 1 in the upper register (the exposition had broken eighths);
  % beats 3–4 are left to the viola fills. No chord on beat 3 of 160 (4–3 suspension in the tune).
  R1*9 | <g'' c''' e'''>2\arpeggio r2 | <a'' c''' f'''>2\arpeggio r2 | <a'' d''' f'''>2\arpeggio r2 |
  <g'' d''' f'''>2\arpeggio r2 | <f'' bes'' f'''>2\arpeggio r2 | <aes'' c''' f'''>2\arpeggio r2 | R1*4 |
  <a'' c''' e'''>2\arpeggio r2 | <a'' c''' f'''>2\arpeggio r2^\markup \small \italic "étouffez" | <aes'' d''' f'''>2\arpeggio r2^\markup \small \italic "étouffez (m.d.)" | <g'' b'' f'''>2\arpeggio r2 |
  <c'' g'' c'''>4\arpeggio r4 r2 |
}
recTwoHarpL = {
  R1*9 | <c, c>2\mf_\pedNat r2 | <c, c>2 r2 | <d, d>2 r2 |
  <g,, g,>2 r2_\markup \small "B♭ A♭" | <bes,, bes,>2\< r2 | <f,, f,>2\f r2 | R1_\markup \small "B♮ A♮" | R1*3 |
  <a,, a,>2\f r2 | <f,, f,>2 r2_\markup \small "A♭" | <d, d>2 <g,, g,>2 | <g,, g,>2 r2 |
  <c, c>4\p r4 r2 |
}
recTwoVlnOne = {
  g''1:32\pp^"sul tasto" | a''1:32 | a''1:32 | f''1:32 |
  bes''1:32 | a''1:32 | a''1:32 | e''4:32 d''2.:32 |
  e''2:32 r4 g'4(\mf^"ord." | \recTwoMelody |
}
recTwoVlnTwo = {
  e''1:32\pp^"sul tasto" | f''1:32 | f''1:32 | d''1:32 | g''1:32 | f''1:32 | f''1:32 | c''4:32 b'2.:32 |
  c''2:32 r4 g'4(\mf^"ord." | \recTwoMelodyA
  d''2.~( d''8 des''8 | c''2 bes'4 aes'8 g'8) | g''4\ff\downbow e'''2.~ | e'''4\< f'''4 g'''2 |
  c'''4\fff\downbow aes'''2~ aes'''8 g'''8 | f'''2 d'''4( b''8 c'''8) | a'2.~(\ff a'8 gis'8) | a'4.\>( g'8 f'4 a'8 c''8) |
  d''2\mp( c''2\> | b'4 a'8 g'8 f'4 d'4) | c'2\p~ c'2\< |
}
recTwoVla = {
  e'2.~\< e'8 d'8\> | c'4\! a'2--\< g'4\!) | f'4.( e'8 d'4 f'8\< a'8 | c''2\> b'2\!) |
  g'4( e''2--\< d''4\!) | c''4.(\> b'8 a'8\! b'32 c''32 d''32 e''32 f''4~ | f''4 e''8 d''8 c''4 a'4) | c''4(\> b'4 d''4 f'4) |
  e'1\p | \recTwoSync |
}
recTwoVc = {
  \clef tenor e2.~\< e8 d8\> | c4\! a2--\< g4\!) | f4.( e8 d4 f8\< a8 | c'2\> b2\!) |
  g4( e'2--\< d'4\!) | c'4.(\> b8 a8\! b32 c'32 d'32 e'32 f'4~ | f'4 e'8 d'8 c'4 a4) | c'4(\> b4 d'4 f4) |
  e1\p | \clef bass \recTwoArp |
}
recTwoCb = {
  c,4\pp^"pizz." r4 r2 | f,4 r4 r2 | d,4 r4 r2 | g,,4 r4 g,,4 r4 |
  e,4 r4 r2 | f,4 r4 r2 | d,4 r4 r2 | g,4 r4 g,4 r4 |
  c,4 r4 r2 | c,1\mp^"arco" | c,1 | d,2 f,,2 |
  g,,1 | bes,,1\< | f,,1 | g,,1\ff |
  g,,1\< | aes,,1\fff | d,2 g,,2 | a,,1\ff\> |
  f,,1 | d,2\mp g,2~ | g,1\> | c,2\p~ c,2\< |
}
