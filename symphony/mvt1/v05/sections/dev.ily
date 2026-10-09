% DEVELOPMENT, bars 77–122.
% D1 77–84 (8): motto-head dialogue, a new colour on every entry.
% D2 85–96 (12): fugato.  D3 97–108 (12): second theme in B♭ minor, then the wedge.
% D4 109–122 (14): dominant pedal, trombone motto augmented, climax, collapse, retransition.

devFluteOne = {
  R1 | r8 es''8\mp ces'''4.-> bes''8 beses''8 aes''8 | R1*4 |
  r8 g''8\ff es'''4.-> d'''8 des'''8 c'''8 | aes''4-> r4 aes''4-> r4 |
  R1*9 | r8 f''8\f des'''4.-> c'''8 ces'''8 bes''8 | bes''4 a''8( bes''8) ges''4.-> f''8 | r8 f''8 des'''4.-> c'''8 ces'''8 bes''8 |
  r2. f''4(\ff | des'''2.~ des'''8 c'''8 | c'''2 bes''4 a''8 bes''8 | ges'''2.~ ges'''8 f'''8 | f'''2 es'''4 des'''8 es'''8 | bes'''2.~ bes'''8 a'''8) |
  aes''2.~\< aes''8 g''8 | bes''2.~ bes''8 a''8 | c'''2.~ c'''8 b''8 | des'''2.~ des'''8 c'''8 | d'''2.~ d'''8 cis'''8 | d'''1 |
  d'''1\ff | es'''1 | f'''1 | f'''1 | es'''1 | aes''1\fff | g''1 | g''2\> f''2\! | R1*6 |
}
devFluteTwo = {
  R1*6 | r8 g'8\ff es''4.-> d''8 des''8 c''8 | f''4-> r4 f''4-> r4 |
  R1*12 |
  R1 | des''2.~\ff des''8 c''8 | c''2 bes'4 a'8 bes'8 | ges''2.~ ges''8 f''8 | f''2 es''4 des''8 es''8 | bes''2.~ bes''8 a''8 |
  aes'2.~\< aes'8 g'8 | bes'2.~ bes'8 a'8 | c''2.~ c''8 b'8 | des''2.~ des''8 c''8 | d''2.~ d''8 cis''8 | d''1 |
  d''1\ff | es''1 | f''1 | f''1 | es''1 | es''1\fff | d''1 | R1*7 |
}
devOboeOne = {
  R1*3 | r8 b'8\mf g''4.-> fis''8 f''8 e''8 | R1 | r8 g'8\f es''4.-> d''8 des''8 c''8 |
  r8 g'8\ff es''4.-> d''8 des''8 c''8 | d''4-> r4 d''4-> r4 |
  R1*9 | r8 f'8\f des''4.-> c''8 ces''8 bes'8 | bes'4 a'8( bes'8) ges'4.-> f'8 | r8 f'8 des''4.-> c''8 ces''8 bes'8 |
  r2. f'4(\ff | des''2.~ des''8 c''8 | c''2 bes'4 a'8 bes'8 | ges''2.~ ges''8 f''8 | f''2 es''4 des''8 es''8 | bes''2.~ bes''8 a''8) |
  aes'2.~\< aes'8 g'8 | bes'2.~ bes'8 a'8 | c''2.~ c''8 b'8 | des''2.~ des''8 c''8 | d''2.~ d''8 cis''8 | d''1 |
  d''1\ff | es''1 | f''1 | f''1 | es''1 | c''1\fff | b'1 | g''2\> f''2 | es''2 d''2 | d''1\p | R1*4 |
}
devOboeTwo = {
  R1*6 | c''1\ff | b'4-> r4 b'4-> r4 |
  R1*12 |
  R1*6 | f'1\ff | f'1 | g'1 | aes'1 | aes'1 | a'1 |
  R1*5 | aes'1\fff | f'1 | R1*7 |
}
devCorAnglais = {
  R1*14 | r8 c'8\f aes'4.-> g'8 ges'8 f'8 | f'4 e'8( f'8) des'4.-> c'8 | f'4 g'4 aes'4 a'4 |
  R1*29 |
}
devClOne = {
  R1 | r8 es''8\mp ces'''4.-> bes''8 beses''8 aes''8 | R1*3 | r8 g'8\f es''4.-> d''8 des''8 c''8 |
  r8 g'8\ff es''4.-> d''8 des''8 c''8 | aes'4-> r4 aes'4-> r4 |
  R1*6 | r8 c'8\f aes'4.-> g'8 ges'8 f'8 | f'4 e'8( f'8) des'4.-> c'8 | f'4 g'4 aes'4 a'4 |
  bes4. c'8 des'8( es'8) f'4 | des'4 c'8( bes8) es'4. des'8 | r8 bes'8 ges''4.-> f''8 fes''8 es''8 |
  des'8\f f' bes' f' des' f' bes' f' | des' f' bes' f' des' f' bes' f' | c' es' a' es' c' es' a' es' |
  des' ges' bes' ges' des' ges' bes' ges' | des' f' bes' f' c' es' a' es' | des' ges' bes' ges' des' ges' bes' ges' |
  aes'1\< | bes'1 | c''1 | des''1 | b'1 | c''1\ff |
  \tuplet 3/2 { b8 d' f' } \repeat unfold 3 { \tuplet 3/2 { b8 d' f' } } | \repeat unfold 4 { \tuplet 3/2 { c'8 es' g' } } |
  \repeat unfold 4 { \tuplet 3/2 { b8 d' f' } } | \repeat unfold 4 { \tuplet 3/2 { bes8 des' f' } } | \repeat unfold 4 { \tuplet 3/2 { c'8 es' g' } } |
  es''1\fff | d''1 | f'1\> | es'1 | d'1\p |
  r8 g8\pp es'4.-> d'8 des'8 c'8 | c'4 b8( c'8) aes4.-> g8 | R1 | b8\< c'8 d'8 es'8 f'8 g'8 aes'8 b'8 |
}
devClTwo = {
  R1*6 | r8\ff es'8 r8 es'8 r8 es'8 r8 es'8 | f'4-> r4 f'4-> r4 |
  R1*12 |
  des'8\f f' bes' f' des' f' bes' f' | des' f' bes' f' des' f' bes' f' | c' es' a' es' c' es' a' es' |
  des' ges' bes' ges' des' ges' bes' ges' | des' f' bes' f' c' es' a' es' | des' ges' bes' ges' des' ges' bes' ges' |
  f'1\< | f'1 | g'1 | aes'1 | aes'1 | a'1\ff |
  \tuplet 3/2 { b8 d' f' } \repeat unfold 3 { \tuplet 3/2 { b8 d' f' } } | \repeat unfold 4 { \tuplet 3/2 { c'8 es' g' } } |
  \repeat unfold 4 { \tuplet 3/2 { b8 d' f' } } | \repeat unfold 4 { \tuplet 3/2 { bes8 des' f' } } | \repeat unfold 4 { \tuplet 3/2 { c'8 es' g' } } |
  c''1\fff | b'1 | d'1\> | c'1 | b1\p | R1*3 | b8\< c'8 d'8 es'8 f'8 g'8 aes'8 b'8 |
}
devBassCl = {
  R1*8 |
  r8 d,8\f bes,4.-> a,8 aes,8 g,8 | g,4 fis,8( g,8) es,4.-> d,8 | g,4 a,4 bes,4 b,4 |
  c4. d8 es8( f8) g4 | es4 d8( c8) f4. es8 | aes,2 g,2 |
  f,1 | bes,,2 c,2 | des,2 c,2 | bes,,1 | es,2 f,2 | bes,,4 r4 bes,,4 r4 |
  bes,1\ff | bes,1 | a,1 | ges,1 | f,1 | ges,1 | f1\< | des1 | c1 | bes,1 | aes,1 | a,1 |
  g,1\ff~ | g,1~ | g,1~ | g,1~ | g,1~ | g,1\fff~ | g,1~ | g,1\>~ | g,1~ | g,1\pp | R1*4 |
}
devBsnOne = {
  r8 es8\mp ces'4.-> bes8 beses8 aes8 | aes1 | R1*2 | r8 g,8\f es4.-> d8 des8 c8 | c1 | c'2\ff c'2 | b4-> r4 b4-> r4 |
  R1*3 | r8 g8\f es'4.-> d'8 des'8 c'8 | c'4 b8( c'8) aes4.-> g8 | c'4 d'4 es'4 e'4 |
  f4. g8 aes8( bes8) c'4 | aes4 g8( f8) bes4. aes8 | des'2 c'2 | bes2 bes2 | es2 des2 | r4. f8 des'4.-> c'8 |
  ces'8\ff bes8 r2. | bes2 r8 f8 des'8 c'8 | c'2 r8 f8 c'8 bes8 | ges2 r8 ges8 des'8 c'8 | bes2 a2 | ges2 r8 ges8 bes8 des'8 |
  f1\< | f1 | g1 | f1 | f1 | fis1 |
  g1\ff | es'1~ | es'2. d'4 | des'2. c'4~ | c'1 | aes1\fff | g1 | g1\> | g1 | g1\p |
  R1*2 | r8 g8\pp\< es'4.-> d'8 des'8 c'8 | b8 c'8 d'8 es'8 f'8 g'8 aes'8 b'8 |
}
devBsnTwo = {
  R1*4 | c1\f | c1 | c8\ff c8 c8 c8 c8 c8 c8 c8 | g,4-> r4 g,4-> r4 |
  r8 d,8\f bes,4.-> a,8 aes,8 g,8 | g,4 fis,8( g,8) es,4.-> d,8 | g,4 a,4 bes,4 b,4 |
  c4. d8 es8( f8) g4 | es4 d8( c8) f4. es8 | aes,2 g,2 |
  f,1 | bes,,2 c,2 | des,2 c,2 | bes,,1 | es,2 f,2 | bes,,4 r4 bes,,4 r4 |
  bes,1\ff | bes,1 | a,1 | ges,1 | f,1 | ges,1 | f,1\< | des,1 | c,1 | bes,,1 | aes,1 | a,1 |
  g,1\ff~ | g,1~ | g,1~ | g,1~ | g,1~ | g,1\fff~ | g,1~ | g,1\>~ | g,1~ | g,1\pp | R1*4 |
}
devCbsn = {
  R1*6 | c,1\ff | g,,4-> r4 g,,4-> r4 |
  R1*11 | bes,,4\f r4 bes,,4 r4 |
  bes,,1\ff | bes,,1 | a,,1 | ges,,1 | f,,1 | ges,,1 | f,,1\< | des,1 | c,1 | bes,,1 | aes,,1 | a,,1 |
  g,,1\ff~ | g,,1~ | g,,1~ | g,,1~ | g,,1~ | g,,1\fff~ | g,,1~ | g,,1\>~ | g,,1~ | g,,1\pp | R1*4 |
}
devHnOne = {
  R1*2 | r8 b8\mf g'4.-> fis'8 f'8 e'8 | e'1 | R1*2 | g'1\ff | aes'4-> r4 aes'4-> r4 |
  R1*11 | r4. f8\f des'4.-> c'8 |
  ces'8\ff bes8 r2. | bes2 r8 f8 des'8 c'8 | c'2 r8 f8 c'8 bes8 | ges2 r8 ges8 des'8 c'8 | bes2 a2 | ges2 r8 ges8 bes8 des'8 |
  aes'1\< | bes'1 | c''1 | des''1 | b'1 | c''1 |
  g1\ff | es'1~ | es'2. d'4 | des'2. c'4~ | c'1 | c'1\fff | b1 | R1*7 |
}
devHnTwo = {
  R1*2 | r8 b8\mf g'4.-> fis'8 f'8 e'8 | e'1 | R1*2 | es'1\ff | f'4-> r4 f'4-> r4 |
  R1*11 | r4. f8\f des'4.-> c'8 |
  ces'8\ff bes8 r2. | bes2 r8 f8 des'8 c'8 | c'2 r8 f8 c'8 bes8 | ges2 r8 ges8 des'8 c'8 | bes2 a2 | ges2 r8 ges8 bes8 des'8 |
  f'1\< | f'1 | g'1 | aes'1 | aes'1 | a'1 |
  g1\ff | es'1~ | es'2. d'4 | des'2. c'4~ | c'1 | aes1\fff | g1 | R1*7 |
}
devHnThree = {
  R1*4 | r8 g8\f es'4.-> d'8 des'8 c'8 | c'1 | c'1\ff | d'4-> r4 d'4-> r4 |
  R1*12 |
  des'1\f | des'1 | c'1 | des'1 | des'2 c'2 | des'1 | c'1\< | des'1 | es'1 | f'1 | f'1 | fis'1 |
  g'1\ff | g'1 | g'1 | g'1 | g'1 | es'1\fff | d'1 | b1\> | c'1 | b1\p | R1*4 |
}
devHnFour = {
  R1*4 | r8 g8\f es'4.-> d'8 des'8 c'8 | c'1 | g1\ff | b4-> r4 b4-> r4 |
  R1*12 |
  bes1\f | bes1 | a1 | bes1 | bes2 a2 | bes1 | f1\< | f1 | g1 | f1 | f1 | fis1 |
  g1\ff | g1 | g1 | g1 | g1 | g1\fff | g1 | g1\> | g1 | g1\p | g1\pp~ | g1~ | g1~ | g1\< |
}
devTptOne = {
  R1*6 | r8 g'8\ff es''4.-> d''8 des''8 c''8 | f''4-> r4 f''4-> r4 |
  R1*12 |
  R1*6 | aes'2.~\f\< aes'8 g'8 | bes'2.~ bes'8 a'8 | c''2.~ c''8 b'8 | des''2.~ des''8 c''8 | d''2.~ d''8 cis''8 | d''1\ff |
  R1*5 | aes'1\fff | g'1 | R1*7 |
}
devTptTwo = {
  R1*6 | r8\ff es'8 r8 es'8 r8 es'8 r8 es'8 | d'4-> r4 d'4-> r4 |
  R1*12 |
  R1*6 | f'1\f\< | f'1 | g'1 | aes'1 | aes'1 | a'1\ff |
  R1*5 | es'1\fff | d'1 | R1*7 |
}
devTptThree = {
  R1*6 | r8\ff c'8 r8 c'8 r8 c'8 r8 c'8 | b4-> r4 b4-> r4 |
  R1*12 |
  R1*6 | c'1\f\< | des'1 | es'1 | f'1 | f'1 | fis'1\ff |
  R1*5 | c'1\fff | b1 | R1*7 |
}
devTbnOne = {
  R1*4 | r8 g,8\f es4.-> d8 des8 c8 | c1 | c'1\ff | aes4-> r4 aes4-> r4 |
  R1*11 | r4. f8\f des'4.-> c'8 |
  ces'8\ff bes8 r2. | bes2 r8 f8 des'8 c'8 | c'2 r8 f8 c'8 bes8 | ges2 r8 ges8 des'8 c'8 | bes2 a2 | ges2 r8 ges8 bes8 des'8 |
  f1\< | f1 | g1 | f1 | f1 | fis1 |
  g1\ff | es'1~ | es'2. d'4 | des'2. c'4~ | c'1 | aes1\fff | g1 | g1\> | R1*6 |
}
devTbnTwo = {
  R1*4 | r8 g,8\f es4.-> d8 des8 c8 | c1 | g1\ff | f4-> r4 f4-> r4 |
  R1*12 |
  R1*6 | c1\f\< | des1 | c1 | bes,1 | aes,1 | a,1 |
  g1\ff | es'1~ | es'2. d'4 | des'2. c'4~ | c'1 | aes1\fff | g1 | g1\> | R1*6 |
}
devBassTbn = {
  R1*6 | c1\ff | g,4-> r4 g,4-> r4 |
  R1*11 | bes,4\f r4 bes,4 r4 |
  bes,1\ff | bes,1 | a,1 | ges,1 | f,1 | ges,1 | f,1\< | des,1 | c,1 | bes,,1 | aes,,1 | a,,1 |
  g,1\ff | es1~ | es2. d4 | des2. c4~ | c1 | g,1\fff | g,1 | g,1\> | R1*6 |
}
devTuba = {
  R1*6 | c,1\ff | g,,4-> r4 g,,4-> r4 |
  R1*12 |
  R1*6 | f,1\f\< | des,1 | c,1 | bes,,1 | aes,,1 | a,,1 |
  g,,1\ff~ | g,,1~ | g,,1~ | g,,1~ | g,,1~ | g,,1\fff~ | g,,1~ | g,,1\>~ | g,,1~ | g,,1\pp | R1*4 |
}
devTimp = {
  R1*4 | c1:32\f\< | c1:32 | c8\ff c8 c8 c8 c8 c8 c8 c8 | g,4-> r4 g,4-> r4 |
  R1*11 | f1:32\f\< |
  bes,4\ff r2. | R1*9 | aes,1:32\< | d1:32 |
  g,1:32\ff~ | g,1:32~ | g,1:32~ | g,1:32~ | g,1:32 | g,1:32\fff~ | g,1:32~ | g,1:32\>~ | g,1:32~ | g,1:32\pp~ |
  g,1:32~ | g,1:32~ | g,1:32~ | g,1:32\< |
}
devPerc = \drummode { R1*37 | <cymc tt>1\fff | R1*8 | }
devVlnOne = {
  R1*3 | r8 b'8\mf g''4.-> fis''8 f''8 e''8 | R1 | r8 g'8\f es''4.-> d''8 des''8 c''8 |
  r8 g''8\ff es'''4.-> d'''8 des'''8 c'''8 | <b' aes''>4-> r4 <b' aes''>4-> r4 |
  R1*9 | r8 f''8\f des'''4.-> c'''8 ces'''8 bes''8 | bes''4 a''8( bes''8) ges''4.-> f''8 | r8 f''8 des'''4.-> c'''8 ces'''8 bes''8 |
  r2. f'4(\ff | des''2.~ des''8 c''8 | c''2 bes'4 a'8 bes'8 | ges''2.~ ges''8 f''8 | f''2 es''4 des''8 es''8 | bes''2.~ bes''8 a''8) |
  aes''2.~\< aes''8 g''8 | bes''2.~ bes''8 a''8 | c'''2.~ c'''8 b''8 | des'''2.~ des'''8 c'''8 | d'''2.~ d'''8 cis'''8 | d'''1 |
  d'''1:32\ff | es'''1:32 | f'''1:32 | f'''1:32 | es'''1:32 | aes''1:32\fff | g''1:32 | g''2\> f''2 | es''2 d''2 | d''1\p | R1*4 |
}
devVlnTwo = {
  es'1:32\p | es'1:32 | b'1:32 | b'1:32 | g'1:32\< | g'1:32 | r8\ff c''8 r8 c''8 r8 c''8 r8 c''8 | <d'' f''>4-> r4 <d'' f''>4-> r4 |
  R1*6 | r8 c'8\f aes'4.-> g'8 ges'8 f'8 | f'4 e'8( f'8) des'4.-> c'8 | f'4 g'4 aes'4 a'4 |
  bes4. c'8 des'8( es'8) f'4 | des'4 c'8( bes8) es'4. des'8 | r8 bes'8 ges''4.-> f''8 fes''8 es''8 |
  r2. f'4(\ff | des''2.~ des''8 c''8 | c''2 bes'4 a'8 bes'8 | ges''2.~ ges''8 f''8 | f''2 es''4 des''8 es''8 | bes''2.~ bes''8 a''8) |
  <f' aes'>1:32\< | <f' bes'>1:32 | <g' c''>1:32 | <aes' des''>1:32 | <aes' b'>1:32 | <a' c''>1:32 |
  d''1:32\ff | es''1:32 | f''1:32 | f''1:32 | es''1:32 | <es'' aes''>1:32\fff | <d'' g''>1:32 | <d' f'>1\> | es'1 | d'1\p |
  R1*3 | b8\< c'8 d'8 es'8 f'8 g'8 aes'8 b'8 |
}
devVla = {
  ces'1:32\p | ces'1:32 | g'1:32 | g'1:32 | es'1:32\< | es'1:32 |
  r8\ff <es' g'>8 r8 <es' g'>8 r8 <es' g'>8 r8 <es' g'>8 | <b d'>4-> r4 <b d'>4-> r4 |
  R1*6 | r8 c'8\f aes'4.-> g'8 ges'8 f'8 | f'4 e'8( f'8) des'4.-> c'8 | f'4 g'4 aes'4 a'4 |
  bes4. c'8 des'8( es'8) f'4 | des'4 c'8( bes8) es'4. des'8 | r8 bes'8 ges''4.-> f''8 fes''8 es''8 |
  des'8\f f' bes' f' des' f' bes' f' | des' f' bes' f' des' f' bes' f' | c' es' a' es' c' es' a' es' |
  des' ges' bes' ges' des' ges' bes' ges' | des' f' bes' f' c' es' a' es' | des' ges' bes' ges' des' ges' bes' ges' |
  c'1:32\< | des'1:32 | es'1:32 | f'1:32 | f'1:32 | fis'1:32 |
  \tuplet 3/2 { b8\ff d' f' } \repeat unfold 3 { \tuplet 3/2 { b8 d' f' } } | \repeat unfold 4 { \tuplet 3/2 { c'8 es' g' } } |
  \repeat unfold 4 { \tuplet 3/2 { b8 d' f' } } | \repeat unfold 4 { \tuplet 3/2 { bes8 des' f' } } | \repeat unfold 4 { \tuplet 3/2 { c'8 es' g' } } |
  <c' es'>1:32\fff | <b d'>1:32 | b1\> | c'1 | b1\p |
  R1*2 | r8 g8\pp\< es'4.-> d'8 des'8 c'8 | b8 c'8 d'8 es'8 f'8 g'8 aes'8 b'8 |
}
devVc = {
  r8 es8\mp ces'4.-> bes8 beses8 aes8 | aes1 | r8 b,8\mf g4.-> fis8 f8 e8 | e1 |
  r8 g,8\f es4.-> d8 des8 c8 | c1 | c2\ff c2 | g4-> r4 g4-> r4 |
  r8 d,8\f bes,4.-> a,8 aes,8 g,8 | g,4 fis,8( g,8) es,4.-> d,8 | g,4 a,4 bes,4 b,4 |
  r8 g8 es'4.-> d'8 des'8 c'8 | c'4 b8( c'8) aes4.-> g8 | c'4 d'4 es'4 e'4 |
  f4. g8 aes8( bes8) c'4 | aes4 g8( f8) bes4. aes8 | des'2 c'2 | bes2 bes2 | es2 des2 | r4. f8 des'4.-> c'8 |
  bes,1\ff | bes,1 | a,1 | ges,1 | f,1 | ges,1 | f1\< | f1 | g1 | f1 | f1 | fis1 |
  g,1:32\ff | g,1:32 | g,1:32 | g,1:32 | g,1:32 | aes1\fff | g1 | <g b>1\> | <g c'>1 | <g b>1\p |
  g,1\pp~ | g,1~ | g,1~ | g,1\< |
}
devCb = {
  aes,,1\p | aes,,1 | e,1 | e,1 | c,1\< | c,1 | c,8\ff c,8 c,8 c,8 c,8 c,8 c,8 c,8 | g,,4-> r4 g,,4-> r4 |
  r8 d,8\f bes,4.-> a,8 aes,8 g,8 | g,4 fis,8( g,8) es,4.-> d,8 | g,4 a,4 bes,4 b,4 |
  c4. d8 es8( f8) g4 | es4 d8( c8) f4. es8 | aes,2 g,2 |
  f,1 | bes,,2 c,2 | des,2 c,2 | bes,,1 | es,2 f,2 | bes,,4 r4 bes,,4 r4 |
  bes,,1\ff | bes,,1 | a,,1 | ges,,1 | f,,1 | ges,,1 | f,1\< | des,1 | c,1 | bes,,1 | aes,,1 | a,,1 |
  g,,1\ff~ | g,,1~ | g,,1~ | g,,1~ | g,,1~ | g,,1\fff~ | g,,1~ | g,,1\>~ | g,,1~ | g,,1\pp~ |
  g,,1~ | g,,1~ | g,,1~ | g,,1\< |
}
