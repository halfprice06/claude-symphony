% SECOND THEME, bars 47–68 (A♭ major). A = 47–55 (cellos + horn), A' = 56–68 (violins).

tTwoOboeOne = {
  R1*22 |
}
tTwoFluteOne = {
  R1*15 |
  \partCombineSoloI es''4\p(^\markup \bold "1." c'''2.~ | c'''4\< des'''4 bes''2) |
  aes''2.~(\f aes''8 g''8 | f''4.\> es''8 des''2) | \partCombineAutomatic R1*3\! |
}
tTwoClOne = {
  R1*5 | r2. f''4~(\mp | f''4 es''8 des''8 c''4. bes'8) | aes'4(\> g'4 bes'4 des'4)\! |
  R1 | es'2\p^\markup \italic "espr." r8 e'8( f'8 g'8 | f'2 aes'4 bes'4) | f'2 r8 f'8( es'8 des'8 |
  des'2) es'2 | f'2\< r8 f'8( es'8 des'8 | fes'2) ces'2 | c'4\subP es'8( f'8 g'4 aes'4~ |
  aes'4\< g'8 f'8) g'2 | c'2\mf r8 c'8( d'8 es'8 | des'2) aes'2 | des'4\> f'8( g'8 bes'2~ |
  bes'2 g'4 des'4) | \after 2 \< c'1\p |
}
tTwoBsnTwo = {
  R1*9 | aes,1\pp^\markup \bold "2." | aes,1 | bes,2 des2 |
  es1 | ges2 es2 | des2 fes2 | es2. r4 |
  es2 e2 | f1 | des1 | bes,2 es2~ |
  es1 | f2. r4 |
}
tTwoHnOne = {
  c'2.~\<^\markup { \bold "1." \italic "dolce" } c'8 bes8\> | aes4\! f'2--\< es'4\!) | des'4.( c'8 bes4 des'8\< f'8 | aes'2\> g'2\!) |
  es'4( c''2--\< bes'4\!) | aes'4.(\> g'8 f'2\!) | R1*2 | c'1\p |
  R1*13 |
}
tTwoHnTwo = {
  R1*9 |
  es'2\p^\markup \italic "espr."  r8 e'8( f'8 g'8 | f'2 aes'4 bes'4) | f'2 r8 f'8( es'8 des'8 |
  des'2) es'2 | R1*4 | c'2\mp^\markup \bold "2." r8 c'8( d'8 es'8 | des'2) aes'2 | des'4\> f'8( g'8 bes'2~ |
  bes'2 g'4 des'4) | \after 2 \< c'1\p |
}
tTwoHnThree = {
  R1*9 | c'1\p | aes1 | des'1 |
  des'1 | des'2.\< r4 | aes1 | c'1\subP |
  des'1\< | c'1\mp | des'1 | des'1\> |
  des'1 | c'2.\p r4 |
}
tTwoHnFour = {
  R1*9 | aes1\p | aes1 | bes1 |
  bes1 | bes1\< | fes1 | aes2.\subP r4 |
  bes2\< g2 | aes1\mp | aes1 | r1 |
  g1 | aes2.\p r4 |
}
tTwoTimp = {
  R1*15 | es1:32\pp\< | es2:32\> r2\! | R1\! |
  R1*4 |
}
tTwoHarpR = {
  \transpose c c' {
  aes8( es' aes' c'' es''2) | des8( aes des' f' aes'2) | bes,8( f bes des' aes'2) | es8( bes des' g' bes'2) |
  c8( ges aes c' es'2) | des8( aes des' f' aes'2) | bes,8( f bes des' f'2) | es8( g bes des' g'2) |
  aes,8( es aes c' es'2) |
}
  % 56–68: LH bass octave on beat 1, RH broken chord on beats 3–4 (interlocks with the cello's beats 1–2);
  % rolled chords in two-chord bars; at 62–63 (cello pizz.) one rising line passes from LH to RH.
  r2 c''8( fes'' aes'' c''') | r2 des''8( f'' aes'' des''') | r2 des''8( f'' bes'' des''') | r2 es''8( g'' bes'' des''') |
  <bes' des'' ges''>2\arpeggio <bes' es'' ges''>2\arpeggio | <aes' des'' fes''>2\arpeggio <fes' aes' des''>2\arpeggio |
  r2 aes8( c' es' aes') | r2 bes8( des' g' bes') |
  <aes' c'' f''>2\arpeggio <f' aes' c''>2\arpeggio | r2 aes'8( des'' f'' aes'') | <bes' des'' f''>2\arpeggio r2 | r2 es''8( g'' bes'' des''') |
  r2 <f' aes' c''>2\arpeggio |
}
tTwoHarpL = {
  aes,,1\p_\pedAflat | des,1 | bes,,1 | << es,,1 { s2. s4_\markup \small "G♭" } >> |
  c,1 | des,1_\markup \small "G♮" | bes,,1 | es,1 |
  aes,,1 | <aes,, aes,>2\p_\markup \small "F♭" r2 | <aes,, aes,>2_\markup \small "F♮" r2 | <bes,, bes,>2 r2 |
  <es, es>2\< << r2 { s4 s4_\markup \small "G♭" } >> | <ges,, ges,>2 <es, es>2_\markup \small "F♭" | <des, des>2 <fes, fes>2 | es,8(\subP aes, c es) r2 |
  es,8(_\markup \small "G♮" bes, des g) r2_\markup \small "F♮" | <f,, f,>2\mf r2 | <des, des>2 r2 | <bes,, bes,>2\> <es, es>2 |
  <es, es>2 r2 | <f,, f,>2\p r2 |
}
tTwoVlnOne = {
  R1*8 | r2. es'4(\p^\markup \italic "molto cantabile" | c''2.~ c''8 bes'8 | aes'4 f''2-- es''4) |
  des''4.\<( c''8 bes'4 des''8 f''8 | aes''2 g''2) | bes''2.~( bes''8 a''8 | aes''2 ges''4 fes''8 es''8) |
  es''4\subP( c'''2.~ | c'''4)\< des'''4( bes''2) | aes''2.~(\f aes''8 g''8) | f''4.( es''8 des''4 f''8 aes''8) |
  bes''2\>( aes''2 | g''4 f''8 es''8 des''4 bes'4) | aes'2\p aes'16(\< c'' des'' es'' f'' g'' aes'' bes'') |
}
tTwoVlnTwo = {
  aes'1\pp | aes'1 | aes'1 | bes'1 |
  ges'1 | f'1 | f'1 | es'2 des'2 |
  <es' aes'>2 r4 es'4(\p^\markup \italic "molto cantabile" | c''2.~ c''8 bes'8 | aes'4 f''2-- es''4) | des''4.\<( c''8 bes'4 des''8 f''8 |
  aes''2 g''2) | bes'2.~( bes'8 a'8 | aes'2 ges'4 fes'8 es'8) | es'4\subP( c''2.~ |
  c''4)\< des''4( bes'2) | aes'2.~(\f aes'8 g'8) | f'4.( es'8 des'4 f'8 aes'8) | bes'2\>( aes'2 |
  g'4 f'8 es'8 des'4 bes4) | \after 2 \< aes1\p |
}
tTwoVla = {
  <c' es'>1\pp^"div." | <des' f'>1 | <bes des'>1 | <bes des'>1 |
  <c' es'>1 | <aes des'>1 | <bes des'>1 | <g bes>1 |
  c'1^"unis." | r4 <c' es'>4\p <c' e'>2 | r4 <des' f'>2 <des' f'>4 | r4 <des' f'>2 <des' f'>4 |
  r4 <bes des'>2 <des' g'>4 | r8 des'8(\< ges'8 bes'8 des''4) r4 | r8 des'8( fes'8 aes'8 des''4) r4\! | r4 <c' es'>2\subP <c' es'>4 |
  r4 <des' g'>2\< <des' g'>4 | r4 <c' f'>2\mf <c' f'>4 | r4 <des' f'>2 <des' f'>4 | r4 <des' f'>2\> <des' f'>4 |
  r4 <des' g'>2 <des' g'>4 | \after 2 \< <c' f'>1\p |
}
tTwoVc = {
  \clef tenor c'2.~\<^\markup \italic "dolce" c'8 bes8\> | aes4\! f'2--\< es'4\!) | des'4.( c'8 bes4 des'8\< f'8 | aes'2\> g'2\!) |
  \clef treble es'4( c''2--\< bes'4\!) | aes'4.(\> g'8 f'4\! f''4~ | f''4 es''8 des''8 c''4. bes'8) | aes'4(\> g'4 bes'4 des'4) |
  c'1\p | \clef bass aes,8\p( es aes c' e'2) | aes,8( des f aes des'2) | bes,8(\< f des'4.\>) c'8( ces'8 bes8\!) |
  es,8( bes, des g bes2) | ges,8( des ges bes) es,8( bes, es ges) | des,8( aes, des fes) fes,8( aes, des fes) | es,4\subP^"pizz." r4 es4 r4 |
  es,4 r4 e,4 r4 | f,8(\mf^"arco" c f aes) d,8( aes, c f) | des,8( aes, des f aes2) | bes,8(\> f bes des') es2 |
  es,8( bes, des g des'2) | f,8(\p c f aes c'2\<) |
}
tTwoCb = {
  aes,4\pp^"pizz." r4 r2 | des,4 r4 r2 | bes,,4 r4 r2 | es,4 r4 es,4 r4 |
  c,4 r4 r2 | des,4 r4 r2 | bes,,4 r4 r2 | es,4 r4 es,4 r4 |
  aes,,4 r4 r2 | aes,,1\p^"arco" | aes,,1 | bes,,2 des,2 |
  es,1 | ges,2\< es,2 | des,2 fes,2 | es,1\subP |
  es,2\< e,2 | f,2\mf d,2 | des,1 | bes,,2\> es,2~ |
  es,1 | \after 2 \< f,1\p |
}
tTwoTptOne = {
  R1*13 | \partCombineSoloI f'2\p\< r8 f'8( es'8 des'8 | fes'2) ces'2 | c'4\subP es'8( f'8 g'4 aes'4~ |
  aes'4 g'8 f'8) g'2 | \partCombineAutomatic R1*5 |
}
