% SECOND THEME, bars 47–68 (A♭ major). A = 47–55 (cellos + horn), A' = 56–68 (violins).
% c102: Vla 52 <aes f'> (was <aes des'>: parallel fifths with the Hn 1/Vc melody B♭–A♭ over E♭–D♭).

tTwoOboeOne = {
  R1*22 |
}
tTwoFluteOne = {
  % c149: Fl 1 no longer doubles the violins' soft D-flat6 peak at 62-63 (sub. p <); it enters on the forte answer at 64. A soft culminating point is better
  % left unsupported (Rimsky-Korsakov PDF 142, Ex. 282 PDF 450); doubling is for a few special phrases only (PDF 140-141)
  R1*17 |
  \partCombineSoloI aes''2.~(\f^\markup \bold "1." aes''8 g''8 | f''4.\> es''8 des''2) | \partCombineAutomatic R1\! | R1 |
  % c137: flutes a2 join the top half of the Vln I run into the codetta (Adler PDF 213: Bizet's run dovetails into the woodwinds), so they arrive at 69 already moving
  r2. f''16(\p\< g''16 aes''16 bes''16) |
}
tTwoFluteTwo = {
  R1*21 | r2. f''16(\p\< g''16 aes''16 bes''16) |
}
tTwoClOne = {
  R1*5 | r2. f''4~(\mp | f''4 es''8 des''8 c''4. bes'8) | aes'4(\> g'4 bes'4 des'4)\! |
  R1 | es'2\p^\markup \italic "espr." r8 e'8( f'8 g'8 | f'2 aes'4 bes'4) | f'2 r8 f'8( es'8 des'8 |
  des'2) es'2 | f'2\< r8 f'8( es'8 des'8 | fes'2) ces'2 | c'4\subP es'8( f'8 g'4 aes'4~ |
  aes'4\< g'8 f'8) g'2 | c'2\mf r8 c'8( d'8 es'8 | des'2) aes'2 | des'4\> aes'8( g'8 bes'2~ |
  bes'2 g'4 des'4) | \after 2 \< c'1\p |
}
tTwoBsnTwo = {
  R1*9 | aes,1\pp^\markup \bold "2." | aes,1 | bes,2 des2 |
  es1 | ges2 es2 | fes1 | es2. r4 |
  es2 e2 | f1 | des1 | bes,2 es2~ |
  es1 | f2. r4 |
}
tTwoHnOne = {
  c'2.~\<^\markup { \bold "1." \italic "dolce" } c'8 bes8\> | aes4\! f'2--\< es'4\!) | des'4.( c'8 bes4 des'8\< f'8 | aes'2\> g'2\!) |
  es'4( c''2--\< bes'4\!) | aes'4.(\> g'8 f'2\!) | R1*2 | c'2.\p r4 | % c159: releases on beat 4 with Vc and Vla so the violins' E-flat4 pickup is heard alone (Adler PDF 245, Strauss Fledermaus m. 83; Beethoven 7/ii m. 50)
  R1*13 |
}
tTwoHnTwo = {
  R1*9 |
  es'2\p^\markup \italic "espr."  r8 e'8( f'8 g'8 | f'2 aes'4 bes'4) | f'2 r8 f'8( es'8 des'8 |
  des'2) es'2 | f'2\< r8 f'8( es'8 des'8 | fes'2) ces'2 | c'4\subP es'8( f'8 g'4 aes'4~ |
  aes'4\< g'8 f'8) g'2 | c'2\mp r8 c'8( d'8 es'8 | des'2) aes'2 | des'4\> aes'8( g'8 bes'2~ |
  bes'2 g'4 des'4) | \after 2 \< c'1\p |
}
tTwoHnThree = {
  R1*9 | c'1\pp | aes1 | des'1 |
  des'1 | des'2.\< r4 | aes1 | c'1\subP |
  des'1\< | c'1\mp \breathe | f'1 | des'1\> | % c156: Hn 3's pad 61-68 had no gap (about 17 s); breath before the new chord at 65 (Adler PDF 292)
  des'1 | c'2.\p r4 |
}
% c114: Hn 4 F3 at 57 (was A♭3, unison with Hn 3) and Hn 3 F4 at 65 (was D♭4, open fourth over Hn 4 A♭3); the horn pad between the violins' tune and the bass keeps thirds and sixths (Rimsky-Korsakov PDF 97, remark 4)
% c119: Hn 4 B-flat3 at 63 beats 3-4 and at 67 (was G3: a diminished fifth under Hn 3's D-flat4); the pair keeps thirds, D-flat-B-flat to C-A-flat (Rimsky-Korsakov PDF 90 rule 4, PDF 97 remark 4)
tTwoHnFour = {
  R1*9 | aes1\pp | f1 | bes1 |
  bes1 | bes1\< | fes1 | aes2.\subP r4 |
  bes1\< | aes1\mp | aes1 | r1 |
  bes1 | aes2.\p r4 |
}
tTwoTimp = {
  R1*15 | es1:32\pp\< | es2:32\> r2\! | R1\! |
  R1*4 |
}
tTwoHarpR = {
  % c125: flatter beams for the wide broken chords 47-63 (Gould, Behind Bars PDF 33-34: a short group crosses at most one stave-space)
  \override Beam.damping = #3
  \transpose c c' {
  aes8( es' aes' c'' es''2) | des8( aes des' f' aes'2) | bes,8( f bes des' aes'2) | es8( bes des' g' bes'2) |
  c8( ges aes c' es'2) | des8( aes des' f' aes'2) | bes,8( f bes des' f'2) | es8( bes des' g' bes'2) |
  aes,8( es aes c' es'2) |
}
  % 56–68: LH bass octave on beat 1, RH broken chord on beats 3–4 (interlocks with the cello's beats 1–2);
  % rolled chords in two-chord bars; at 62–63 (cello pizz.) one rising line passes from LH to RH.
  % c157: 56-59 RH broken chords an octave higher (C6-D-flat7), above the violins' tune (C5-A-flat5) instead of inside it, as 47-55 lie above the cello's tune (Sebesky PDF 13: focus)
  r2 \ottava #1 c'''8( fes''' aes''' c'''') | r2 des'''8( f''' aes''' des'''') | r2 des'''8( f''' bes''' des'''') | r2 bes''8( es''' bes''' des'''') \ottava #0 |
  <bes' des'' ges''>2\arpeggio <bes' es'' ges''>2\arpeggio | <aes' des'' fes''>2\arpeggio <fes' aes' des''>2\arpeggio |
  r2^\markup \small \italic "étouffez" aes8( c' es' aes') | r2 bes8( des' g' bes') | \revert Beam.damping
  <aes' c'' f''>2\arpeggio <f' aes' c''>2\arpeggio | r2 aes'8( des'' f'' aes'') | <bes' des'' f''>2\arpeggio r2 | r2 es''8( g'' bes'' des''') |
  r2 <f' aes' c''>2\arpeggio |
}
tTwoHarpL = {
  aes,,1\p_\pedAflat | des,1 | bes,,1 | << es,,1 { s2. s4_\markup \small "G♭" } >> |
  c,1 | des,1 | << bes,,1 { s2 s2_\markup \small "G♮" } >> | es,1 |
  aes,,1 | <aes,, aes,>2\p_\markup \small "F♭" r2 | <aes,, aes,>2 r2_\markup \small "F♮" | <bes,, bes,>2 r2 |
  <es, es>2\< << r2 { s4 s4_\markup \small "G♭" } >> | <ges,, ges,>2 <es, es>2_\markup \small "F♭" | <fes, fes>2 <fes, fes>2 | es,8(\subP aes, c es) r2 |
  es,8(_\markup \small "G♮" bes, des g) r2_\markup \small "F♮" | <f,, f,>2\mf r2 | <des, des>2 r2 | <bes,, bes,>2\> <es, es>2 |
  <es, es>2 r2 | <f,, f,>2\p r2 |
}
% c141: 57.2-59 sul A in Vln I and II (unison): the p cantabile restatement of the cello's theme keeps F5-A-flat5 on the A string
% instead of crossing to the E string (Adler PDF 75, Ex. III-7, Brahms 3/iii: violins restate the cello theme sul A, p espress.); E string from the mf at 60.
tTwoVlnOne = {
  R1*8 | r2. \once \override TextScript.self-alignment-X = #RIGHT es'4(\p^\markup \italic "molto cantabile" | c''2.~ c''8 bes'8 | aes'4 \once \override TextSpanner.bound-details.left.text = \markup \italic \small "sul A" f''2--^\startTextSpan es''4) |
  des''4.\<( c''8 bes'4 des''8 f''8 | aes''2 g''2)\stopTextSpan | bes''2.~(\mf\< bes''8 beses''8 | aes''2 ges''4 fes''8 es''8) |
  es''4\subP( c'''2.~ | c'''4)\< des'''4( bes''2) | aes''2.~(\f aes''8 g''8) | f''4.( es''8 des''4 f''8 aes''8) |
  bes''2( aes''2\> | g''4 f''8 es''8 des''4 bes'4) | aes'2\p aes'16(\< c'' des'' es'' f'' g'' aes'' bes'') |
}
% c114: Vln II 47-54 metà: one undivided note against the violas' divided pair makes A♭4 twice as strong as C4 and E♭4 (Rimsky-Korsakov PDF 88: ease the undivided part by reducing players)
tTwoVlnTwo = {
  aes'1\pp^\markup \italic "metà" | aes'1 | aes'1 | bes'1 |
  ges'1 | f'1 | f'1 | es'2 des'2 |
  <es' aes'>2^\markup \italic "tutti, div." r4 \once \override TextScript.self-alignment-X = #RIGHT es'4(\p^\markup \right-column { \italic "molto cantabile" "unis." } | c''2.~ c''8 bes'8 | aes'4 \once \override TextSpanner.bound-details.left.text = \markup \italic \small "sul A" f''2--^\startTextSpan es''4) | des''4.\<( c''8 bes'4 des''8 f''8 |
  aes''2 g''2)\stopTextSpan | bes'2.~(\mf\< bes'8 beses'8 | aes'2 ges'4 fes'8 es'8) | es'4\subP( c''2.~ |
  c''4)\< des''4( bes'2) | aes'2.~(\f aes'8 g'8) | f'4.( es'8 des'4 f'8 aes'8) | bes'2( aes'2\> |
  g'4 f'8 es'8 des'4 bes4) | \after 2 \< aes1\p |
}
tTwoVla = {
  <c' es'>1\pp^"div." | <des' f'>1 | <bes des'>1 | <bes des'>1 |
  <c' es'>1 | <aes f'>1 | <bes des'>1 | <bes es'>4 <g bes>2. |
  c'2.^"unis." r4 | r4 <c' es'>4\pp^"div." <c' e'>2 | r4 <des' f'>2 <des' f'>4 | r4 <des' f'>2 <des' f'>4 |
  r4 <bes des'>2 <des' g'>4 | r8 des'8(\<^"unis." ges'8 bes'8 des''4) r4 | r8 des'8( fes'8 aes'8 des''4) r4\! | r4 <c' es'>2\subP^"div." <c' es'>4 |
  r4 <des' g'>2\< <des' g'>4 | r4 <c' f'>2\mf <c' f'>4 | r4 <des' f'>2 <des' f'>4 | r4 <des' f'>2\> <des' f'>4 |
  r4 <des' g'>2 <des' g'>4 | \after 2 \< <c' f'>1\p |
}
tTwoVc = {
  \clef tenor c'2.~\<^\markup \italic "dolce" c'8 bes8\> | aes4\! f'2--\< es'4\!) | des'4.( c'8 bes4 des'8\< f'8 | aes'2\> g'2\!) |
  \clef treble es'4( c''2--\< bes'4\!) | aes'4.(\> g'8 f'4\! f''4~ | f''4 es''8 des''8 c''4. bes'8) | aes'4(\> g'4 bes'4 des'4) |
  c'2.\p r4 | \clef bass aes,8\p( es aes c' e'2) | aes,8( des f aes des'2) | bes,8(\< f des'4.\>) c'8( ces'8 bes8\!) |
  es,8( bes, des g bes2) | ges,8( des ges bes) es,8( bes, es ges) | fes,8( des fes aes) fes,8(\upbow aes, des fes) | es,4\subP^"pizz." r4 es4 r4 |
  es,4 r4 e,4 r4 | f,8(\mf^"arco" c f aes) d,8( aes, c f) | des,8( aes, des f aes2) | bes,8( f bes des') es2\> |
  es,8( bes, des g des'2) | f,8(\p c f aes c'2\<) |
}
tTwoCb = {
  aes,4\pp^"pizz." r4 r2 | des,4 r4 r2 | bes,,4 r4 r2 | es,4 r4 es,4 r4 |
  c,4 r4 r2 | des,4 r4 r2 | bes,,4 r4 r2 | es,4 r4 es,4 r4 |
  aes,,4 r4 r2 | aes,,1\p^"arco" | aes,,1 | bes,,2 des,2 |
  es,1 | ges,2\< es,2 | fes,1 | es,1\subP |
  es,2\< e,2 | f,2\mf d,2 | des,1 | bes,,2 es,2~\> |
  es,1 | \after 2 \< f,1\p |
}
% c131: Tpt 1 no longer doubles the Cl 1 counterline at 60-63 (chromatic, enharmonic F-flat/C-flat line at p); Hn 2 keeps it 56-68
% (Rimsky-Korsakov PDF 72-73: chromatic or enharmonic melodies are much less suited to brass, which lacks geniality; the horn's tone in piano passages gives greater scope)
tTwoTptOne = { R1*22 | }
