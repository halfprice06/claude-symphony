% A' SECTION, bars 71-82 (3/4).
% 71-78: the theme in Vln I (upper octave) and Vln II; cellos and horns 1-2 play the counter-melody of bar 23.
%        The cadence at 78 is deceptive (F minor).
% 79-82: the cadential bars again, ff, peak F6 at 79, full close at 82.
% v03's closing 83-90 (clarinet theme head, horn motto tail over a tonic pedal) is cut (critic 003).

aTwoVlnOne = {
  aes''4. c'''8) es'''4~ | es'''4 d'''4( des'''4) | c'''4.( bes''8 aes''4 | g''2) es''8( f''8 |
  aes''4.\mp\< c'''8) f'''4~ | f'''4 bes'''4( aes'''4) | g'''4( es'''8 des'''8 c'''8 bes''8 | aes''2)\f \afterGrace c'''4 { f'''16( g''' aes''' } |
  bes'''2.)~\ff | bes'''4 aes'''2 | g'''4(\> es'''8 des'''8 c'''8 bes''8) | aes''2.\p |
}
aTwoVlnTwo = {
  aes'4. c''8) es''4~ | es''4 d''4( des''4) | c''4.( bes'8 aes'4 | g'2) es'8( f'8 |
  aes'4.\mp\< c''8) f''4~ | f''4 bes''4( aes''4) | g''4( es''8 des''8 c''8 bes'8 | aes'2)\f \afterGrace c''4 { f''16( g'' aes'' } |
  bes''2.)~\ff | bes''4 aes''2 | g''4(\> es''8 des''8 c''8 bes'8) | aes'2.\p |
}
aTwoFluteOne = {
  R2.*4 |
  aes''4.(\mp\< c'''8 f'''4~ | f'''4 bes'''4 aes'''4 | g'''4 es'''8 des'''8 c'''8 bes''8 | aes''2)\f c'''4( |
  bes'''2.~\ff | bes'''4 aes'''2) \breathe | g'''4(\> es'''8 des'''8 c'''8 bes''8 | aes''2.)\p |
}
aTwoOboeOne = {
  R2.*8 |
  bes''2.~(\ff | bes''4 aes''2) | g''4(\> es''8 des''8 c''8 bes'8 | aes'2.)\p |
}
aTwoVla = {
  c'8(\pp^\markup \italic "unis., espr." es' aes') es'( c' aes) | c'( aes' bes) aes'( bes g') | c'( es' aes') c'( es' aes) | bes( es' g') es'( bes es') |
  c'(\p\< es' aes') es'( aes f') | f'( aes' f') bes( es' bes) | g( bes es') g'( es' des') | c'(\f f' aes') f'( c' aes) |
  <f' aes'>2.:32\ff^\markup \italic "div." | <f' aes'>4:32 <f' aes'>4:32 <es' aes'>4:32 | <es' g'>2.:32\> | <es' aes'>2.\p |
}
aTwoVc = {
  es2\p^\markup \italic "cantabile" aes8( g8 | f2) g4( | aes2 c'4) | bes2. |
  es2(\mp\< f4) | aes2( c'4) | bes2( des'4) | c'2\f c'4 |
  des'4\ff c'4 bes4 | aes4( bes4 c'4) | bes2\> des'4 | c'2.\p |
}
aTwoHnOne = {
  R2.*7 | r2 c'4(\f |
  \partCombineUnisono des'4\ff c'4 bes4 | aes4 bes4 c'4) \breathe | bes2(\> des'4 | c'2.)\p \partCombineAutomatic |
}
% c006: the 71-78 counter-melody moves to horn 2, so horn 1 rests after its solo at 67-70.
aTwoHnTwo = {
  es2\p^\markup \bold "2." aes8( g8 | f2 g4 | aes2 c'4 | bes2.) |
  es2(\mp\< f4 | aes2 c'4 | bes2 des'4 | c'2)\f c'4( |
  des'4\ff c'4 bes4 | aes4 bes4 c'4) \breathe | bes2(\> des'4 | c'2.)\p |
}
aTwoHnThree = { R2.*8 | \clef bass aes2.\ff | aes4 aes4 aes4 | g2.\> | aes2.\p | }
aTwoHnFour = { R2.*8 | \clef bass des2.\ff | des4 des4 c4 | bes,2.\> | c2.\p | }
aTwoClOne = {
  c''2.\pp | c''4 bes'4 bes'4 | c''2. | bes'2. |
  c''2.\p\< | des''4 des''4 c''4 | bes'2. | f'2\f f'4 |
  des''2.\ff | des''4 des''4 c''4 | bes'2.\> | c''2.\p |
}
aTwoClTwo = {
  aes'2.\pp | aes'4 f'4 g'4 | aes'2. | g'2. |
  aes'2.\p\< | aes'4 aes'4 aes'4 | g'2. | aes'2\f aes'4 |
  aes'2.\ff | aes'4 aes'4 aes'4 | g'2.\> | aes'2.\p |
}
% c011: bassoon 1 joins the cello and horn counter-melody at the ff return (Rimsky-Korsakov PDF 54, 56: relief by doubling; Antar [63] cellos doubled by bassoons).
aTwoBsnOne = { R2.*7 | r2 c'4( | des'4\ff c'4 bes4 | aes4 bes4 c'4) \breathe | bes2(\> des'4 | c'2.)\p | }
aTwoBsnTwo = {
  aes,2.\pp | f4 bes,4 es4 | aes,2 c4 | es2. |
  aes,4\p\< c4 des4 | des2 es4 | es2. | f2.\f |
  des2.\ff | des2 es4 | es2.\> | aes,2.\p |
}
aTwoBassCl = { R2.*8 | des2.\ff | des2 es4 | es,2.\> | aes,2.\p | }
aTwoCb = {
  aes,,2.\pp | f,4 bes,,4 es,4 | aes,,2 c,4 | es,2. |
  aes,,4\p\< c,4 des,4 | des,2 es,4 | es,2. | f,2.\f |
  des,2.\ff | des,2 es,4 | es,2.\> | aes,,2.\p |
}
aTwoTimp = { R2.*8 | des2.:32\f | des2:32 es4 | es2.:32\> | aes,2.\p | }
aTwoHarpR = {
  r4 <aes c' es'>2\arpeggio | R2. | r4 <aes c' es'>2\arpeggio | r4 <g bes es'>2\arpeggio |
  r4 <aes c' es'>2\arpeggio | <aes des' f'>4\arpeggio r2 | r4 <g bes des'>2\arpeggio | r4 <aes c' f'>2\arpeggio |
  r4 <aes des' f'>2\arpeggio | <aes des' f'>4\arpeggio r2 | r4 <g bes des'>2\arpeggio | r4 <aes c' es'>2\arpeggio |
}
aTwoHarpL = {
  <aes,, es,>2.\pp\arpeggio | <f,, c,>4\arpeggio <bes,, f,>4\arpeggio <es,, bes,,>4\arpeggio | <aes,, es,>2\arpeggio c,4 | <es,, es,>2.\arpeggio |
  <aes,, es,>4\p\arpeggio c,4 des,4 | <des, aes,>2\arpeggio es,4 | <es,, bes,,>2.\arpeggio | <f,, c,>2.\arpeggio |
  <des, aes,>2.\f\arpeggio | <des, aes,>2\arpeggio es,4 | <es,, bes,,>2.\arpeggio | <aes,, es,>2.\arpeggio |
}
