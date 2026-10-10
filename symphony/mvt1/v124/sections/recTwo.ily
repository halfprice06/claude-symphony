% RECAPITULATION, second theme in C major, bars 147–166 (20 bars; exposition 47–68 has 22). A = 147–155 (horn + violas + cellos, CA answers).
% Cycle 80: the violins' literal restatement of the head (old 156–159, = 47–50 / 56–59 in the exposition) is cut and withheld for movement III.
% The violins enter at 156 with the head's rhythm a step lower on ♭VII (pickup f''–d''' = the rising sixth), whose descent falls on the motto's
% own pitches D–D♭–C (spelled D♭: passing tone over B♭ → F minor); climax head at K (158), ♭VI fff at 160.

% Withheld in the recapitulation since cycle 80 (the violins' C-major head, unused here): reserved for movement III.
% recTwoMelodyA below is the withheld violin statement without its pickup (the slur opens in the pickup). The complete passage, with pickup, the chromatic counter (Cl1/Hn2) and bass, is in v99/sections/recTwo.ily (bars 156–159 of v99), kept for movement III.
recTwoMelodyA = { e''2.~ e''8 d''8 | c''4 a''2-- g''4) | f''4.(\< e''8 d''4 f''8 a''8 | c'''2 b''2) | }
recTwoMelodyB = {
  d'''2.~\< d'''8 des'''8 | c'''2 bes''4 aes''8 g''8) | g''4\ff\downbow e'''2.~ | e'''4\< f'''4 g'''2 |
  c'''4\fff\downbow aes'''2~ aes'''8 g'''8 | f'''2 d'''4( b''8 c'''8) | a''2.~(\ff a''8 gis''8) | a''4.\>( g''8 f''4 a''8 c'''8) |
  d'''2\mp( c'''2\> | b''4 a''8 g''8 f''4 d''4) | c''2\p~ c''2\< |
}
recTwoCounter = {
  f'2\mp\< r8 f'8( g'8 a'8 | aes'2) f'2 | g'2\ff c''2 | b'2\< f'2 |
  es'4\fff c''4 r8 c''8( bes'8 aes'8 | aes'2) f'2 | e'2\ff\> r8 e'8( f'8 g'8 | f'2) c''2 |
  f'4\mp aes'8( b'8) d''2~ | d''2( b'4 f'4) | e'2 es'2\< |
}
recTwoMelody = { \recTwoMelodyB }
recTwoSync = {
  r8 d'8(\mp\< f'8 bes'8 d''4) r4 | r8 c'8( f'8 aes'8 c''4) r4 | g4\ff e'2.~ | e'4\< f'4 g'2 |
  c'4\fff aes'2~ aes'8 g'8 | f'2 d'4( b8 c'8) | r4 e'4~\ff\> e'8 d'8( c'8 b8) |
  r4 c'4~ c'8 a8( c'8 f'8) | r4 f'4~\mp f'8 e'8( d'8 g8) | r4 g4~ g8 b8( d'8 b8) | <e' g'>2\mp <es' g'>2\< |
}
recTwoArp = {
  bes,8(\mp\< d bes4.) a8( aes8 g8) | f,8( c f aes c'2) | \clef tenor g4\ff e'2.~ | e'4\< f'4 g'2 |
  c'4\fff aes'2~ aes'8 g'8 | f'2 d'4( b8 c'8) | \clef bass a,8(\ff\> e a c' e'2) | f,8( c f a c'2) |
  d,8(\mp aes, d f) g,2 | g,8(\> d f b f2) | c,8(\p g, c e es2\<) |
}

recTwoFluteOne = {
  R1*11 |
  \partCombineUnisono g''4\ff( e'''2.~ | e'''4\< f'''4 g'''2) | c'''4(\fff aes'''2~ aes'''8 g'''8 |
  f'''2 d'''4 b''8 c'''8) | \partCombineAutomatic a''2.~(\ff a''8 gis''8) | a''4.\>( g''8 f''2)\! | R1*3 |
}
recTwoFluteTwo = {
  R1*11 |
  g''4\ff( e'''2.~ | e'''4\< f'''4 g'''2) |
  c'''4(\fff aes'''2~ aes'''8 g'''8 | f'''2 d'''4 b''8 c'''8) | R1*5 |
}
recTwoOboeOne = {
  R1*11 | g'4\ff( e''2.~ |
  e''4\< f''4 g''2) | c''4(\fff aes''2~ aes''8 g''8 | f''2 d''4 b'8 c''8) | R1*5 |
}
recTwoOboeTwo = { R1*11 | g'2\ff c''2 | b'2\< f'2 | es'4\fff c''4 r8 c''8( bes'8 aes'8 | aes'2) f'2 | R1*5 | }
recTwoCorAnglais = {
  r2 r8 g'8(\p a'8 b'8 | c''2) r2 | r2 r8 a'8( b'8 c''8 | d''2) r2 |
  r2 r8 bes'8( a'8 g'8 | a'2) r2 | c''1 | g'2 f'2 | e'2 r2 |
  R1*11 |
}
% c104: Cl 1 takes the counterline an octave higher at 158–162 (Ob 2 and Hn 3 keep it at pitch), so the octave under the
% tune's top doubling holds a chord tone at the climax (it was empty on every beat of 158–161).
recTwoClOne = { R1*5 | r2. f''4~(\mp | f''4 e''8 d''8 c''4 a'4) | R1*2 |
  f'2\mp\< r8 f'8( g'8 a'8 | aes'2) f'2 |
  g''2\ff c'''2 | b''2\< f''2 |
  es''4\fff c'''4 r8 c'''8( bes''8 aes''8 | aes''2) f''2 |
  e''2\ff\> r8 e'8( f'8 g'8 | f'2) c''2 |
  f'4\mp aes'8( b'8) d''2~ | d''2( b'4 f'4) | e'2 es'2\< |
}
recTwoClTwo = { R1*11 | e'1\ff | d'1\< | c'1\fff | d'1 | R1*5 | }
recTwoBsnOne = {
  R1*9 |
  f,1\mf\< | \partCombineUnisono f,1 | g,1\ff | g,1\< | aes,1\fff | \partCombineAutomatic d2 g,4 r4 | e,1\ff\> | \partCombineUnisono f,1 | \partCombineAutomatic d,2\mp \partCombineUnisono g,2~ | g,1\> | \partCombineAutomatic c,2.\p r4 |
}
recTwoBsnTwo = {
  c1\pp | f1 | d1 | g,1 |
  e1 | f1 | d1 | g1 |
  c2 r2 |
  bes,1\mf\< | f,1 | g,1\ff |
  g,1\< | aes,1\fff | d2 g,2 | a,2.\ff\> r4 |
  f,1 | d2\mp g,2~ | g,1\> | c2.\p r4 |
}
recTwoCbsn = { R1*11 | g,,1\ff | g,,1\< | aes,,1\fff | d,2 g,,2 | R1*5 | }
recTwoHnOne = {
  e'2.~\< e'8 d'8\> | c'4\! a'2--\< g'4\!) | f'4.( e'8 d'4 f'8\< a'8 | c''2\> b'2\!) |
  g4( e'2--\< d'4\!) | c'4.(\> b8 a2\!) | R1 | c''4(\> b'4 d''4 f'4) |
  e'2\p d'2 | f'1\mf\< | f'2. r4 |
  g4\ff e'2.~ | e'4\< f'4 g'2 | c'4\fff aes'2~ aes'8 g'8 | f'2 d'4( b8 c'8) |
  e'1\ff\> | R1 | f'1\p | f'1 |
  e'2\mp es'2\< |
}
recTwoHnTwo = {
  R1*9 | d'2.~\mf\< d'8 des'8 | c'2. r4 | g4\ff e'2.~ |
  e'4\< f'4 g'2 | c'4\fff aes'2~ aes'8 g'8 | f'2 d'4( b8 c'8) | c'1\ff\> |
  c'1 | c'2\p r2 | R1 | c'2\mp~ c'2\< |
}
recTwoHnThree = {
  R1*9 | bes1\mf\< | aes1 | g'2\ff c''2 | % c087: Hn 3 holds 157 (entered at 156; breathes at 160), so one horn bridges into K
  b'2\< f'2 | es'4\fff c''4 r8 c''8( bes'8 aes'8 | aes'2) f'2 | \clef bass a1\ff\> |
  R1 | aes2\p a2 | b1 | g1\mp |
}
recTwoHnFour = { R1*9 | f1\mf\< | f2. r4 | g1\ff | g1\< | aes1\fff | f2 g2 | e1\ff\> | f1 | d2\p g2 | R1 | c1\mp | }
recTwoTptOne = {
  R1*11 | g'4\ff e''2.~ | e''4\< f''4 g''2 | c''4\fff aes''2~ aes''8 g''8 |
  f''2 d''4( b'8 c''8) | c''2\ff\>~ c''2\mp | R1*4 |
}
recTwoTptTwo = {
  R1*11 | g'1\ff | g'1\< | aes'1\fff |
  f'2 f'2 | e'2\ff\>~ e'2\mp | R1*4 |
}
recTwoTptThree = {
  R1*11 | c'1\ff | b1\< | c'1\fff |
  b1 | c'2\ff\>~ c'2\mp | R1*4 |
}
recTwoTbnOne = {
  R1*11 | c'1\ff | b1\< | c'1\fff |
  b1 | c'2\ff\>~ c'2\mp | R1*4 |
}
recTwoTbnTwo = {
  R1*11 | g1\ff | g1\< | es1\fff |
  f2 f2 | e2\ff\>~ e2\mp | R1*4 |
}
recTwoBassTbn = {
  R1*11 | g,1\ff | g,1\< | aes,1\fff |
  d2 g,2 | a,2\ff\>~ a,2\mp | R1*4 |
}
recTwoTuba = {
  R1*11 | g,,1\ff | g,,1\< | aes,,1\fff |
  d,2 g,,2 | a,,2\ff\>~ a,,2\mp | R1*4 |
}
recTwoTimp = { R1*11 | g,1:32\ff | g,1:32\< | aes,1:32\fff | g,2:32\> r2\! | R1*4 | r2 c2:32\p\< | }
recTwoPerc = \drummode { R1*12 | cymr1:32\pp\<\laissezVibrer^\markup { "2: Susp. cym." \italic "soft sticks, l.v." } | cymc1\fff\laissezVibrer^\markup { "1: Crash cym." \italic "l.v." } | R1*6 | }
recTwoHarpR = {
  % 156–166: one rolled chord per harmony on beat 1 in the upper register (the exposition had broken eighths);
  % beats 3–4 are left to the viola fills. No chord on beat 3 of 168 (4–3 suspension in the tune).
  R1*9 | <f'' bes'' f'''>2\arpeggio r2 | <aes'' c''' f'''>2\arpeggio r2 | R1*4 |
  <a'' c''' e'''>2\arpeggio r2 | <a'' c''' f'''>2\arpeggio r2^\markup \small \italic "étouffez" | <aes'' d''' f'''>2\arpeggio r2^\markup \small \italic "étouffez (m.d.)" | <g'' b'' f'''>2\arpeggio r2 |
  <c'' g'' c'''>4\arpeggio r4 r2 |
}
recTwoHarpL = {
  R1*8 | R1_\pedBflatAflat |
  <bes,, bes,>2\mf r2 | <f,, f,>2\f r2 | R1_\markup \small "B♮ A♮" | R1*3 |
  <a,, a,>2\f r2 | <f,, f,>2 r2_\markup \small "A♭" | <d, d>2 <g,, g,>2 | <g,, g,>2 r2 |
  <c, c>4\p r4 r2 |
}
recTwoVlnOne = {
  g''1:32\pp^"sul tasto" | a''1:32 | a''1:32 | f''1:32 |
  bes''1:32 | a''1:32 | a''1:32 | e''4:32 d''2.:32 |
  e''2:32 r4 f''4(\mf^"ord." | \recTwoMelody |
}
% cycle 82: 148 IV–IV+ (C–C#–D in Vln II) into ii at 149; 155 beats 3–4 E→D in Vla/Vc/Hn1 under the violins' f pickup.
recTwoVlnTwo = {
  e''1:32\pp^"sul tasto" | c''2:32 cis''2:32 | d''1:32 | d''1:32 | g''1:32 | f''1:32 | f''1:32 | c''4:32 b'2.:32 |
  c''2:32 r4 f'4(\mf^"ord." |
  d''2.~\< d''8 des''8 | c''2 bes'4 aes'8 g'8) | g''4\ff\downbow e'''2.~ | e'''4\< f'''4 g'''2 |
  c'''4\fff\downbow aes'''2~ aes'''8 g'''8 | f'''2 d'''4( b''8 c'''8) | a'2.~(\ff a'8 gis'8) | a'4.\>( g'8 f'4 a'8 c''8) |
  d''2\mp( c''2\> | b'4 a'8 g'8 f'4 d'4) | c'2\p~ c'2\< |
}
recTwoVla = {
  e'2.~\< e'8 d'8\> | c'4\! a'2--\< g'4\!) | f'4.( e'8 d'4 f'8\< a'8 | c''2\> b'2\!) |
  g'4( e''2--\< d''4\!) | c''4.(\> b'8 a'8\! b'32 c''32 d''32 e''32 f''4~ | f''4 e''8 d''8 c''4 a'4) | c''4(\> b'4 d''4 f'4) |
  e'2\p d'2 | \recTwoSync |
}
recTwoVc = {
  \clef tenor e2.~\< e8 d8\> | c4\! a2--\< g4\!) | f4.( e8 d4 f8\< a8 | c'2\> b2\!) |
  g4( e'2--\< d'4\!) | c'4.(\> b8 a8\! b32 c'32 d'32 e'32 f'4~ | f'4 e'8 d'8 c'4 a4) | c'4(\> b4 d'4 f4) |
  e2\p d2 | \clef bass \recTwoArp |
}
recTwoCb = {
  c,4\pp^"pizz." r4 r2 | f,4 r4 r2 | d,4 r4 r2 | g,,4 r4 g,,4 r4 |
  e,4 r4 r2 | f,4 r4 r2 | d,4 r4 r2 | g,4 r4 g,4 r4 |
  c,4 r4 r2 | bes,,1\mp\<^"arco" | f,,1 | g,,1\ff |
  g,,1\< | aes,,1\fff | d,2 g,,2 | a,,1\ff\> |
  f,,1 | d,2\mp g,2~ | g,1\> | c,2\p~ c,2\< |
}
