% B SECTION, bars 37-64 (Poco più mosso, 4/4), D flat major.
% 37-44 B1: new theme in flute 1 with clarinet 1 an octave lower, over viola triplets and pizzicato bass.
%          It opens with a rising fourth; bar 42 is the motto's tail at the D flat level (A flat-G-G flat-F),
%          harmonised as in bar 8 (vi7 - V7/V - V7 - I).
% 45-52 B2: the theme's head in B flat minor (violins), D flat 7 = C sharp 7, then F sharp minor (= G flat minor):
%          oboe 1 quotes the movement I second-theme head in minor with its pickup (cyclic-notes §3), once.
%          G sharp 7 respelled A flat 7 leads back to D flat.
% 53-60 B3: the theme in both violin sections (an octave apart), horn 1 counter-melody from the A theme's head;
%          woodwinds and horns join for the crescendo.
% 61-64 B4: climax on D flat (61), G flat to F flat (= E major) (62), then A minor: trombone 1 quotes the
%          movement I first-theme head once, ff, in a foreign key (cyclic-notes: Dvořák 9/ii 96-98 model).

bSecFluteOne = {
  f''4.(\p ges''8 f''4 es''4 | des''4 c''8 des''8 es''2) | ges''4.( f''8 es''4 des''4 | c''2 bes'2) |
  aes'4( des''4 f''4. ges''8 | aes''4 g''4 ges''4 f''4 | es''4. f''8 des''4 bes'4 | c''2.) r4 |
  R1*8 |
  R1*4 |
  aes''4(\mf\< des'''4 f'''4. ges'''8 | aes'''4 g'''4 ges'''4 f'''4 | es'''4.\f f'''8 des'''4 bes''4 | c'''1)\< |
  aes''2(\ff des'''2 | f'''2 fes'''2) | R1*2 |
}
bSecFluteTwo = {
  R1*8 | R1*8 | R1*8 |
  f''1\ff | des'''2 fes'''2 | R1*2 |
}
bSecOboeOne = {
  R1*8 |
  R1*2 | r2 r4 cis'4(\p | a'2.~ a'8 gis'8 | fis'4 d''2 cis''4) | cis''2( b'4 a'4) |
  aes'2(\> ges'2 | f'2. ges'4)\pp |
  f'2 r2 | R1*3 |
  aes'4(\mf\< des''4 f''4. ges''8 | aes''4 g''4 ges''4 f''4 | es''4.\f f''8 des''4 bes'4 | c''1)\< |
  aes'2(\ff des''2 | f''2 fes''2) | R1*2 |
}
bSecOboeTwo = {
  R1*8 | R1*8 | R1*8 |
  f'1\ff | ges'2 aes'2 | R1*2 |
}
bSecClOne = {
  f'4.(\p ges'8 f'4 es'4 | des'4 c'8 des'8 es'2) | ges'4.( f'8 es'4 des'4 | c'2 bes2) |
  aes4( des'4 f'4. ges'8 | aes'4 g'4 ges'4 f'4 | es'4. f'8 des'4 bes4 | c'2.) r4 |
  R1*8 |
  R1*4 |
  f'2\mp\< des'2 | des'4 des'4 c'4 des'4 | es'2\f es'2 | es'1\< |
  des''1\ff | des''2 fes''2 | R1*2 |
}
bSecClTwo = {
  R1*8 | R1*8 |
  R1*4 |
  des'2\mp\< des'2 | aes4 bes4 aes4 aes4 | bes2\f des'2 | c'1\< |
  aes'1\ff | bes'2 aes'2 | R1*2 |
}
bSecBassCl = {
  des'2)\! r2 | R1*7 |
  R1*8 | R1*8 |
  des1\ff | ges,2 fes,2 | R1*2 |
}
bSecBsnOne = {
  f2\pp r2 | R1*7 |
  R1*8 |
  R1*4 |
  f2\mp\< bes2 | f4 es4 es4 f4 | ges2\f es2 | es1\< |
  f1\ff | ges2 aes2 | R1*2 |
}
bSecBsnTwo = {
  R1*8 | R1*8 |
  des2\p des2 | bes,2 aes,2 | es2 des2 | a,2 bes,2 |
  f2\mp\< ges2 | bes,4 es4 aes,4 des4 | ges2\f g2 | aes,1\< |
  des1\ff | ges,2 fes,2 | R1*2 |
}
bSecCbsn = {
  R1*24 |
  des,1\ff | ges,,2 fes,,2 | R1*2 |
}
bSecHnOne = {
  R1*8 | R1*8 |
  r2 r4 aes8(\mp^\markup \italic "espr." bes8 | des'4. f'8 aes'2 | ges'2 f'2 | es'2 des'2) |
  aes'2\mf\< ges'2 | f'4 es'4 es'4 f'4 | ges'2\f es'2 | es'1\< |
  aes'1\ff | bes'2 ces''2 | R1*2 |
}
bSecHnTwo = {
  R1*8 | R1*8 | R1*4 |
  f'2\mf\< des'2 | des'4 des'4 c'4 des'4 | es'2\f des'2 | c'1\< |
  f'1\ff | ges'2 aes'2 | R1*2 |
}
bSecHnThree = {
  R1*24 |
  des'1\ff | des'2 fes'2 | R1*2 |
}
bSecHnFour = {
  R1*24 |
  aes1\ff | bes2 ces'2 | R1*2 |
}
bSecTptOne = { R1*24 | aes'2\ff des''2 | f''2 fes''2 | R1*2 | }
bSecTptTwo = { R1*24 | f'1\ff | ges'2 aes'2 | R1*2 | }
bSecTptThree = { R1*24 | des'1\ff | des'2 fes'2 | R1*2 | }
bSecTbnOne = {
  R1*24 |
  aes1\ff | bes2 ces'2 |
  r8 e8->\ff^\markup \italic "marcato" c'4.-> b8 bes8 a8 | a4 gis8 a8 f4.-> e8 |
}
bSecTbnTwo = { R1*24 | f1\ff | ges2 aes2 | R1*2 | }
bSecBassTbn = { R1*24 | des1\ff | ges,2 fes,2 | a,1\f | a,2 d,4 e,4 | }
bSecTuba = { R1*24 | des,1\ff | ges,,2 fes,,2 | R1*2 | }
bSecTimp = {
  R1*15 | aes,1:32\pp\< |
  aes,4\p r4 r2 | R1*5 |
  R1 | aes,2.:32\p\< r4\! |
  des1:32\ff | des2:32 aes,2:32 | R1*2 |
}

bSecVlnOne = {
  R1*8 |
  des''4.(\p es''8 des''4 c''4 | bes'4 aes'8 bes'8 des''2) | cis''1\> | R1\! | R1*4 |
  f''4.(\p\< ges''8 f''4 es''4 | des''4 c''8 des''8 es''2)\mp | ges''4.(\< f''8 es''4 des''4 | c''2\mf bes'2) |
  aes''4(\< des'''4 f'''4. ges'''8 | aes'''4 g'''4 ges'''4 f'''4 | es'''4.\f f'''8 des'''4 bes''4 | c'''1)\< |
  des'''1(\ff | f'''2 fes'''2) | e'''1:32\f\> | e'''2:32 r2\! |
}
bSecVlnTwo = {
  R1*8 |
  des'1\pp | des'2 des'2 | eis'1 | fis'1 | fis'4 fis'2 eis'4 | fis'2 fis'2 | es'1 | es'1\< |
  f''4.(\p\< ges''8 f''4 es''4 | des''4 c''8 des''8 es''2)\mp | ges''4.(\< f''8 es''4 des''4 | c''2\mf bes'2) |
  aes'4(\< des''4 f''4. ges''8 | aes''4 g''4 ges''4 f''4 | es''4.\f f''8 des''4 bes'4 | c''1)\< |
  aes'2(\ff des''2 | f''2 fes''2) | <e'' c'''>1:32\f\> | <e'' c'''>2:32 r2\! |
}

bSecVla = {
  \tuplet 3/2 4 { aes8(\pp des' f' des' aes des') } \tuplet 3/2 4 { aes8( des' f' des' aes des') } |
  \tuplet 3/2 4 { bes8( des' ges' des' bes des') } \tuplet 3/2 4 { c'8( es' ges' es' c' es') } |
  \tuplet 3/2 4 { bes8( des' ges' des' bes des') } \tuplet 3/2 4 { bes8( des' f' des' bes des') } |
  \tuplet 3/2 4 { a8( c' es' c' a c') } \tuplet 3/2 4 { bes8( des' f' des' bes des') } |
  \tuplet 3/2 4 { aes8( des' f' des' aes des') } \tuplet 3/2 4 { bes8( des' ges' des' bes des') } |
  \tuplet 3/2 4 { aes8( des' f') } \tuplet 3/2 4 { bes8( des' es') } \tuplet 3/2 4 { ges8( c' es') } \tuplet 3/2 4 { aes8( des' f') } |
  \tuplet 3/2 4 { ges8( bes es' bes ges bes) } \tuplet 3/2 4 { aes8( des' es' des' aes des') } |
  \tuplet 3/2 4 { ges8( c' es' c' ges c') } \tuplet 3/2 4 { ges8( c' es' c' ges c') } |
  f1\pp | f2 ges2 | b1 | cis'1 | a4 b2 gis4 | a2 d'2 | c'1 | c'1\< |
  \tuplet 3/2 4 { aes8(\p\< des' f' des' aes des') } \tuplet 3/2 4 { aes8( des' f' des' aes des') } |
  \tuplet 3/2 4 { bes8( des' ges' des' bes des') } \tuplet 3/2 4 { c'8( es' ges' es' c' es') } |
  \tuplet 3/2 4 { bes8(\mp\< des' ges' des' bes des') } \tuplet 3/2 4 { bes8( des' f' des' bes des') } |
  \tuplet 3/2 4 { a8( c' es' c' a c') } \tuplet 3/2 4 { bes8( des' f' des' bes des') } |
  \tuplet 3/2 4 { aes8(\mf\< des' f' des' aes des') } \tuplet 3/2 4 { bes8( des' ges' des' bes des') } |
  \tuplet 3/2 4 { aes8( des' f') } \tuplet 3/2 4 { bes8( des' es') } \tuplet 3/2 4 { ges8( c' es') } \tuplet 3/2 4 { aes8( des' f') } |
  \tuplet 3/2 4 { ges8(\f bes es' bes ges bes) } \tuplet 3/2 4 { bes8( des' es' des' bes des') } |
  \tuplet 3/2 4 { ges8(\< c' es' c' ges c') } \tuplet 3/2 4 { ges8( c' es' c' ges c') } |
  <des' f'>1:32\ff | <bes des'>2:32 <ces' fes'>2:32 | <e' a'>1:32\f\> | <e' a'>2:32 r2\! |
}

bSecVc = {
  des4\p^"pizz." r4 des4 r4 | bes,4 r4 aes,4 r4 | es4 r4 des4 r4 | a,2 bes,2 |
  f4 r4 ges4 r4 | bes,4 es4 aes,4 des4 | ges4 r4 aes4 r4 | aes,4 r4 r2 |
  bes,1\pp^"arco" | bes,2 bes,2 | gis,1 | a,1 | fis4 b,2 cis4 | fis2 b,2 | ges1 | ges1\< |
  des2\p\< des2 | bes,2 aes,2\mp | es2\< des2 | a,2 bes,2\mf |
  f2\< ges2 | bes,4 es4 aes,4 des4 | ges2\f g2 | aes1\< |
  aes2(\ff des'2 | f'2 fes'2) | a1:32\f\> | a2:32 r2\! |
}
bSecCb = {
  des,4\p^"pizz." r4 des,4 r4 | bes,,4 r4 aes,,4 r4 | es,4 r4 des,4 r4 | a,,2 bes,,2 |
  f,4 r4 ges,4 r4 | bes,,4 es,4 aes,,4 des,4 | ges,4 r4 aes,4 r4 | aes,,4 r4 r2 |
  bes,,1\pp^"arco" | bes,,2 ges,,2 | cis,1 | fis,1 | fis,4 b,,2 cis,4 | fis,2 b,,2 | aes,,1 | aes,,1\< |
  des,2\p\< des,2 | bes,,2 aes,,2\mp | es,2\< des,2 | a,,2 bes,,2\mf |
  f,2\< ges,2 | bes,,4 es,4 aes,,4 des,4 | ges,2\f g,2 | aes,,1\< |
  des,1\ff | ges,,2 fes,,2 | a,,1\f\> | a,,2 d,4 e,4\! |
}
