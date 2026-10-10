% A' SECTION, bars 71-90 (3/4).
% 71-78: the theme in Vln I (upper octave) and Vln II; cellos and horns 1-2 play the counter-melody of bar 23.
%        The cadence at 78 is deceptive (F minor).
% 79-82: the cadential bars again, ff, peak F6 at 79, full close at 82.
% 83-90: a quiet closing statement over a tonic pedal: clarinet 1 (theme head), then horn 1 (motto tail E flat-D-D flat-C).

aTwoVlnOne = {
  aes''4. c'''8 es'''4~ | es'''4 d'''4 des'''4 | c'''4. bes''8 aes''4 | g''2) es''8( f''8 |
  aes''4.\< c'''8 f'''4~ | f'''4 bes'''4 aes'''4 | g'''4 es'''8 des'''8 c'''8 bes''8 | aes''2)\f c'''4( |
  bes'''2.~\ff | bes'''4 aes'''2 | g'''4\> es'''8 des'''8 c'''8 bes''8 | aes''2.)\p |
  R2.*8 |
}
aTwoVlnTwo = {
  aes'4. c''8 es''4~ | es''4 d''4 des''4 | c''4. bes'8 aes'4 | g'2) es'8( f'8 |
  aes'4.\< c''8 f''4~ | f''4 bes''4 aes''4 | g''4 es''8 des''8 c''8 bes'8 | aes'2)\f c''4( |
  bes''2.~\ff | bes''4 aes''2 | g''4\> es''8 des''8 c''8 bes'8 | aes'2.)\p |
  R2.*8 |
}
aTwoFluteOne = {
  R2.*4 |
  aes''4.\mf\< c'''8 f'''4~ | f'''4 bes'''4 aes'''4 | g'''4 es'''8 des'''8 c'''8 bes''8 | aes''2\f c'''4( |
  bes'''2.~\ff | bes'''4 aes'''2 | g'''4\> es'''8 des'''8 c'''8 bes''8 | aes''2.)\p |
  R2.*8 |
}
aTwoOboeOne = {
  R2.*8 |
  bes''2.~\ff | bes''4 aes''2 | g''4\> es''8 des''8 c''8 bes'8 | aes'2.\p |
  R2.*8 |
}
aTwoVla = {
  <c' es'>2.\mf | <c' aes'>4 <bes aes'>4 <bes g'>4 | <c' es'>2. | <bes es'>2. |
  <c' es'>2\< <des' f'>4 | <f' aes'>4 <f' aes'>4 <es' aes'>4 | <es' g'>2. | <f' aes'>2\f <f' aes'>4 |
  <f' aes'>2.:32\ff | <f' aes'>4:32 <f' aes'>4:32 <es' aes'>4:32 | <es' g'>2.:32\> | <es' aes'>2.\p |
  <c' es'>2.\pp | <c' aes'>4 <bes aes'>4 <bes g'>4 | <c' es'>2. | <des' f'>2. |
  <aes c'>2. | <aes f'>4 <aes fes'>4 <aes es'>4 | <aes es'>2.~ | <aes es'>2. |
}
aTwoVc = {
  es2\mf^\markup \italic "cantabile" aes8( g8 | f2 g4 | aes2 c'4 | bes2.) |
  es2(\< f4 | aes4 bes4 c'4 | bes2 des'4 | c'2)\f c'4( |
  des'4\ff c'4 bes4 | aes4 bes4 c'4 | bes2\> des'4 | c'2.)\p |
  aes,2.~\pp | aes,2.~ | aes,2.~ | aes,2.~ | aes,2.~ | aes,2.~ | aes,2.~ | aes,2. |
}
aTwoHnOne = {
  es2\mf aes8( g8 | f2 g4 | aes2 c'4 | bes2.) |
  es2(\< f4 | aes4 bes4 c'4 | bes2 des'4 | c'2)\f c'4( |
  des'4\ff c'4 bes4 | aes4 bes4 c'4 | bes2\> des'4 | c'2.)\p |
  R2.*4 | es'2.(\p^\markup \italic "solo" | d'4 des'4 c'4~ | c'2.~\> | c'2.)\pp |
}
aTwoHnTwo = {
  es2\mf aes8( g8 | f2 g4 | aes2 c'4 | bes2.) |
  es2(\< f4 | aes4 bes4 c'4 | bes2 des'4 | c'2)\f c'4( |
  des'4\ff c'4 bes4 | aes4 bes4 c'4 | bes2\> des'4 | c'2.)\p |
  R2.*8 |
}
aTwoHnThree = { R2.*8 | aes2.\ff | aes4 aes4 aes4 | g2.\> | aes2.\p | R2.*8 | }
aTwoHnFour = { R2.*8 | des2.\ff | des4 des4 c4 | bes,2.\> | c2.\p | R2.*8 | }
aTwoClOne = {
  c''2.\p | c''4 bes'4 bes'4 | c''2. | bes'2. |
  c''2\< des''4 | des''4 des''4 c''4 | bes'2. | c''2\f c''4 |
  des''2.\ff | des''4 des''4 c''4 | bes'2.\> | c''2.\p |
  aes'4.(\p c''8 es''4~ | es''4 d''4 des''4 | c''2.) | R2.*5 |
}
aTwoClTwo = {
  aes'2.\p | aes'4 f'4 g'4 | aes'2. | g'2. |
  aes'2.\< | aes'4 aes'4 aes'4 | g'2. | aes'2\f aes'4 |
  aes'2.\ff | aes'4 aes'4 aes'4 | g'2.\> | aes'2.\p |
  R2.*8 |
}
aTwoBsnTwo = {
  aes,2.\mf | f4 d4 es4 | aes,2 c4 | es2. |
  aes,4\< c4 des4 | des2 es4 | es2. | f2.\f |
  des2.\ff | des2 es4 | es2.\> | aes,2.\p |
  R2.*8 |
}
aTwoBassCl = { R2.*8 | des2.\ff | des2 es4 | es,2.\> | aes,2.\p | R2.*8 | }
aTwoCb = {
  aes,,2.\mf | f,4 d,4 es,4 | aes,,2 c,4 | es,2. |
  aes,,4\< c,4 des,4 | des,2 es,4 | es,2. | f,2.\f |
  des,2.\ff | des,2 es,4 | es,2.\> | aes,,2.\p |
  aes,,2.~\pp | aes,,2.~ | aes,,2.~ | aes,,2.~ | aes,,2.~ | aes,,2.~ | aes,,2.~ | aes,,2. |
}
aTwoTimp = { R2.*8 | des2.:32\f | des2:32 es4 | es2.:32\> | aes,2.\p | R2.*8 | }
aTwoHarpR = {
  r4 <aes c' es'>2\arpeggio | R2. | r4 <aes c' es'>2\arpeggio | r4 <g bes es'>2\arpeggio |
  r4 <aes c' es'>2\arpeggio | <aes des' f'>4\arpeggio r2 | r4 <g bes des'>2\arpeggio | r4 <aes c' f'>2\arpeggio |
  r4 <aes des' f'>2\arpeggio | <aes des' f'>4\arpeggio r2 | r4 <g bes des'>2\arpeggio | r4 <aes c' es'>2\arpeggio |
  R2.*8 |
}
aTwoHarpL = {
  <aes,, es,>2.\mf\arpeggio | <f,, c,>2.\arpeggio | <aes,, es,>2.\arpeggio | <es,, bes,,>2.\arpeggio |
  <aes,, es,>2.\arpeggio | <des, aes,>2.\arpeggio | <es,, bes,,>2.\arpeggio | <f,, c,>2.\arpeggio |
  <des, aes,>2.\f\arpeggio | <des, aes,>2.\arpeggio | <es,, bes,,>2.\arpeggio | <aes,, es,>2.\arpeggio |
  R2.*8 |
}
