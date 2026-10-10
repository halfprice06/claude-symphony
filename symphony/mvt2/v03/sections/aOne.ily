% A SECTION, bars 7-30 (Adagio, 3/4).
% 7-14  a : the theme in horn 1, accompanied only by clarinets, bassoon 2, bass clarinet and harp (no strings).
%          Theme: a rising A flat arpeggio to a held E flat, then the motto's tail E flat-D-D flat-C
%          read in A flat (5-#4-4-3), harmonised vi7 - V7/V(6) - V7 - I.
% 15-22 b : oboe 1 and the first violins answer each other; to F minor and back to a half cadence.
% 23-30 a': the theme in both violin sections, with a cello counter-melody; full close in A flat.

aOneHnOne = {
  aes4. c'8 es'4~\< | es'4 d'4\> des'4 | c'4.\! bes8 aes4 | g2) es8( f8 |
  aes4. c'8 f'4~\< | f'4 bes'4\> aes'4 | g'4 es'8 des'8 c'8 bes8 | aes2.)\! |
  R2.*16 |
}

aOneClOne = {
  c''2.\pp | c''4 bes'4 bes'4 | c''2. | bes'2. |
  c''2. | des''4 des''4 c''4 | bes'2. | c''2. |
  R2.*16 |
}
aOneClTwo = {
  aes'2.\pp | aes'4 f'4 g'4 | aes'2. | g'2. |
  aes'2. | aes'4 aes'4 aes'4 | g'2. | aes'2. |
  R2.*16 |
}
aOneBassCl = {
  aes,2.\pp | f,4 bes,,4 es,4 | aes,2 c4 | es,2. |
  aes,4 c4 des4 | des2 es4 | es,2. | aes,2. |
  R2.*16 |
}
aOneBsnTwo = {
  es2.\pp | c4 bes,4 bes,4 | es2. | bes,2. |
  es2 f4 | aes4 f4 aes4 | bes,2. | es2. |
  R2.*16 |
}

aOneHarpR = {
  r4 <aes c' es'>2\arpeggio | R2. | r4 <aes c' es'>2\arpeggio | r4 <g bes es'>2\arpeggio |
  r4 <aes c' es'>2\arpeggio | <aes des' f'>4\arpeggio r2 | r4 <g bes des'>2\arpeggio | r4 <aes c' es'>2\arpeggio |
  R2.*8 |
  r4 <aes c' es'>2\arpeggio | R2. | r4 <aes c' es'>2\arpeggio | r4 <g bes es'>2\arpeggio |
  r4 <aes c' es'>2\arpeggio | <aes des' f'>4\arpeggio r2 | r4 <g bes des'>2\arpeggio | r4 <aes c' es'>2\arpeggio |
}
aOneHarpL = {
  <aes,, es,>2.\pp\arpeggio^\markup \small \harp-pedal #"^-^|^--^" | <f,, c,>2.\arpeggio | <aes,, es,>2.\arpeggio | <es,, bes,,>2.\arpeggio |
  <aes,, es,>2.\arpeggio | <des, aes,>2.\arpeggio | <es,, bes,,>2.\arpeggio | <aes,, es,>2.\arpeggio |
  R2.*8 |
  <aes,, es,>2.\pp\arpeggio | <f,, c,>2.\arpeggio | <aes,, es,>2.\arpeggio | <es,, bes,,>2.\arpeggio |
  <aes,, es,>2.\arpeggio | <des, aes,>2.\arpeggio | <es,, bes,,>2.\arpeggio | <aes,, es,>2.\arpeggio |
}

aOneOboeOne = {
  R2.*8 |
  c''4.(\p des''8 es''4 | f''2 es''4) | R2.*2 |
  c''4( des''8 c''8 bes'4 | aes'2 g'4) | R2.*2 |
  R2.*8 |
}

aOneVlnOne = {
  R2.*8 |
  R2.*2 | aes''8(\p bes''8 g''4 f''4 | es''2 des''4) |
  R2.*2 | f''8( g''8 es''4 d''4 | es''2) es'8(\mp^\markup \italic "espr." f'8 |
  aes'4. c''8 es''4~ | es''4 d''4 des''4 | c''4. bes'8 aes'4 | g'2) es'8( f'8 |
  aes'4.\< c''8 f''4~ | f''4\mf\> bes''4 aes''4 | g''4 es''8 des''8 c''8 bes'8 | aes'2.)\p |
}
aOneVlnTwo = {
  R2.*8 |
  aes'2\pp aes'4 | aes'2 g'4 | c''2 aes'4 | g'2 f'4 |
  aes'2 g'4 | c'2 bes4 | aes2 aes4 | g2 es'8(\mp f'8 |
  aes'4. c''8 es''4~ | es''4 d''4 des''4 | c''4. bes'8 aes'4 | g'2) es'8( f'8 |
  aes'4.\< c''8 f''4~ | f''4\mf\> bes''4 aes''4 | g''4 es''8 des''8 c''8 bes'8 | aes'2.)\p |
}
aOneVla = {
  R2.*8 |
  es'2\pp f'4 | des'2 bes4 | f'2 f'4 | c'2 des'4 |
  f'2 e'4 | f'2 e'4 | f'2 f'4 | bes2. |
  <c' es'>2.\p | <c' aes'>4 <bes aes'>4 <bes g'>4 | <c' es'>2. | <bes es'>2. |
  <c' es'>2\< <aes f'>4 | <f' aes'>4\mf\> <f' aes'>4 <es' aes'>4 | <es' g'>2. | <es' aes'>2.\p |
}
aOneVc = {
  R2.*8 |
  c2\pp des4 | des2 es4 | f2 des4 | c2 bes,4 |
  f2 g4 | f2 c4 | des2 bes,4 | es2. |
  es2\p^\markup \italic "cantabile" aes8( g8 | f2 g4 | aes2 c'4 | bes2.) |
  es2(\< f4 | aes4\mf\> bes4 c'4 | bes2 des'4 | c'2.)\p |
}
aOneCb = {
  R2.*8 |
  c,2\pp des,4 | des,2 es,4 | f,2 des,4 | c,2 bes,,4 |
  f,2 g,4 | f,2 c,4 | des,2 bes,,4 | es,2. |
  aes,,2.\p | f,4 bes,,4 es,4 | aes,,2 c,4 | es,2. |
  aes,,4\< c,4 des,4 | des,2\mf\> es,4 | es,2. | aes,,2.\p |
}
aOneHnThree = { R2.*22 | g2.\pp | aes2. | }
aOneHnFour = { R2.*22 | es2.\pp | es2. | }
