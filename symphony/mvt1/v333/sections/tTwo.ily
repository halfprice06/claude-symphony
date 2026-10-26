% SECOND THEME, bars 47–68 (A♭ major). A = 47–55 (cellos + horn), A' = 56–68 (violins).
% c102: Vla 52 <aes f'> (was <aes des'>: parallel fifths with the Hn 1/Vc melody B♭–A♭ over E♭–D♭).

tTwoOboeOne = {
  R1*22 |
}
tTwoFluteOne = {
  % c149: Fl 1 no longer doubles the violins' soft D-flat6 peak at 62-63 (sub. p <); it enters on the forte answer at 64. A soft culminating point is better
  % left unsupported (Rimsky-Korsakov PDF 142, Ex. 282 PDF 450); doubling is for a few special phrases only (PDF 140-141)
  R1*17 |
  \partCombineSoloI \soloStemsOn aes''2.~(\mf^\markup \bold "1." aes''8 g''8 | % c167: mf under the violins' f (Sebesky PDF 164: a flute on the lead violin line is marked a level lower)
  f''4.\> es''8 des''2) | \partCombineAutomatic \soloStemsOff R1\! | R1 |
  % c137: flutes a2 join the top half of the Vln I run into the codetta (Adler PDF 213: Bizet's run dovetails into the woodwinds), so they arrive at 69 already moving
  r2. f''16(\p\< g''16 aes''16 bes''16) |
}
tTwoFluteTwo = {
  R1*21 | r2. f''16(\p\< g''16 aes''16 bes''16) |
}
tTwoClOne = {
  R1*5 | r2. f''4~(\mp | f''4 es''8 des''8 c''4. bes'8) | aes'4(\> g'4 bes'4 des'4)\! |
  R1 | es'2\p^\markup \italic "espr." r8 e'8( f'8 g'8 | f'2 aes'4 bes'4) | f'2 r8 f'8( es'8 des'8 |
  des'2--) es'2 | f'2\< r8 f'8( es'8 des'8 | fes'2) ces'2 | c'4\subP es'8( f'8 g'4 aes'4~ |
  aes'4\< g'8 f'8) g'2 | c'2\mf r8 c'8( d'8 es'8 | des'2) aes'2 | des'4\> aes'8( g'8 bes'2~ |
  bes'2 g'4 des'4) | \after 2 \< c'1\p |
}
tTwoBsnTwo = {
  % c167: Bsn 2 rests 56-59 (it doubled the Cb's arco roots, with the harp LH octaves and the cello arpeggio's first note, under the p violin tune);
  % it enters at 60 where the violins go to mf in octaves (Sebesky PDF 140 rule 7, PDF 145-146 Ex. 195: roots doubled only for richness, not to reinforce the bass; c149 F4)
  R1*13 | % c168: Bsn 2 doubles the Cb roots 60-68; it now follows their dynamics (p<, sub. p, <, mp, >, p) instead of holding pp under the mf climax
  % (MOLA Guidelines PDF 7-8: one wind player per part, horizontal proofreading; Tchaikovsky 6/i 90-101: Fagotti, Corni and Basso carry identical swells)
  ges1\p\<^\markup \bold "2." | fes1 | es2.\subP r4 |
  es2\< e2 | f1\mp | des1 | bes,2 es2~\> |
  es1 | f2.\p r4 |
}
tTwoHnOne = {
  c'2.~\<^\markup { \bold "1." \italic "dolce" } c'8 bes8\> | aes4\! f'2--\< es'4\!) | des'4.( c'8 bes4 des'8\< f'8 | aes'2\> g'2\!) |
  es'4( c''2--\< bes'4\!) | aes'4.(\> g'8 f'2\!) | R1*2 | c'2.\p r4 | % c159: releases on beat 4 with Vc and Vla so the violins' E-flat4 pickup is heard alone (Adler PDF 245, Strauss Fledermaus m. 83; Beethoven 7/ii m. 50)
  R1*13 |
}
tTwoHnTwo = {
  R1*9 |
  es'2\p^\markup \italic "espr."  r8 e'8( f'8 g'8 | f'2 aes'4 bes'4) | f'2 r8 f'8( es'8 des'8 |
  des'2--) es'2 | f'2\< r8 f'8( es'8 des'8 | fes'2) ces'2 | c'4\subP es'8( f'8 g'4 aes'4~ |
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
  % c168: part-only dynamic for the re-entry at 67 (MOLA PDF 10 Ex. 3: an entry after rests carries its level); the score shows Hn 3's hairpin
  bes1-\tag #'part \mp-\tag #'part \> | aes2.\p r4 |
}
tTwoTimp = {
  R1*15 | es1:32\pp\< | es4:32\>~ es4\! r2 | R1\! |
  R1*4 |
}
tTwoHarpR = {
  % c125: flatter beams for the wide broken chords 47-63 (Gould, Behind Bars PDF 33-34: a short group crosses at most one stave-space)
  \override Beam.damping = #3
  \transpose c c' {
  aes8( es' aes' c'' es''2) | des8( aes des' f' aes'2) | bes,8( f bes des' aes'2) | es8( bes des' aes' bes'2) | % c171: 50 A-flat5 (was G5): the G sounded on beat 2.5 while Vc/Hn 1 still held the A-flat4 of the 4-3, and rang under the G-flat pedal change at beat 4
  % (Aldwell & Schachter PDF 352, Ex. 21-12: do not sound the tone of resolution before the suspension resolves; c136 F1 at 59-60: no pedal change on a ringing string)
  c8( ges aes c' es'2) | des8( aes des' f' aes'2) | des8( f bes des' f'2) | es8( bes des' g' bes'2) |
  aes,8( es aes c' es'2) |
}
  % 56–68: LH bass octave on beat 1, RH broken chord on beats 3–4 (interlocks with the cello's beats 1–2);
  % rolled chords in two-chord bars; at 62–63 (cello pizz.) one rising line passes from LH to RH.
  % c157: 56-59 RH broken chords an octave higher (C6-D-flat7), above the violins' tune (C5-A-flat5) instead of inside it, as 47-55 lie above the cello's tune (Sebesky PDF 13: focus)
  r2 \ottava #1 c'''8( fes''' aes''' c'''') | r2 des'''8( f''' aes''' des'''') | r2 des'''8( f''' bes''' des'''') | r2 bes''8( es''' bes''' des'''') \ottava #0 |
  <bes' des'' ges''>2\arpeggio <ges' bes' es''>2\arpeggio | <aes' des'' fes''>2\arpeggio <fes' aes' des''>2\arpeggio |
  r2^\markup \small \italic "étouffez" aes8( c' es' aes') | r2 bes8( des' g' bes') | \revert Beam.damping
  <aes' c'' f''>2\arpeggio <f' aes' c''>2\arpeggio | r2 aes'8( des'' f'' aes'') | <bes' des'' f''>2\arpeggio r2 | r2 es''8( g'' bes'' des''') |
  r2^\markup \small \italic "étouffez" <f' aes' c''>2\arpeggio |  % c246: damp the V7 arpeggio of 67 at the deceptive cadence, as at 62 and 163 (Adler adler1 PDF 113-114, 117)
}
tTwoHarpL = {
  aes,,1\p_\pedAflat | des,1 | bes,,1 | es,,1 |  % c246: G-flat now in the 47 diagram (no change at 50)
  c,1 | des,1 | << des,1 { s2 s2_\markup \small "G♮" } >> | es,1 |
  aes,,1 | <aes,, aes,>2\p_\markup \small "F♭" r2 | <aes,, aes,>2 r2_\markup \small "F♮" | <bes,, bes,>2 r2 |
  <es, es>2\< << r2 { s4 s4_\markup \small "G♭" } >> | <ges,, ges,>2 r2_\markup \small "F♭" | <fes, fes>2 <fes, fes>2 | es,8(\subP aes, c es) r2 |
  es,8(_\markup \small "G♮" bes, des g) r2_\markup \small "F♮" | <f,, f,>2\mf r2 | <des, des>2 r2 | <bes,, bes,>2\> <es, es>2 |
  <es, es>2 r2 | <f,, f,>2\p r2 |
}
% c321: 55.4-57.1 sul D in Vln I and II: the pickup E-flat4 and the S head's rising sixth to C5 and its turn on one string, then sul A from 57.2
% (Rimsky-Korsakov rimsky-principles PDF 57, Ex. 12, Sheherazade III, PDF 186: cantabile for Vln I and II in unison on the D string, then on the A; PDF 56/60-61; as the cellos' sul G motto at 1 and Vln I's sul D motto at 177)
% c141: 57.2-59 sul A in Vln I and II (unison): the p cantabile restatement of the cello's theme keeps F5-A-flat5 on the A string
% instead of crossing to the E string (Adler PDF 75, Ex. III-7, Brahms 3/iii: violins restate the cello theme sul A, p espress.); E string from the mf at 60.
tTwoVlnOne = {
  % c329: 55.4 "molto cantabile" left-aligned at the pickup so it stacks above the c321 "sul D" spanner instead of running into it ("molto cantabile sul D" / "unis.sul D" read as one marking; Vln II's text sat over the beat-1 "tutti, div." chord)
  R1*8 | r2. \once \override TextScript.self-alignment-X = #LEFT \once \override TextSpanner.bound-details.left.text = \markup \italic \small "sul D" es'4(\p^\markup \italic "molto cantabile"^\startTextSpan | c''2.~\< c''16\> des''16 c''16 bes'16 | aes'4\!\stopTextSpan \once \override TextSpanner.bound-details.left.text = \markup \italic \small "sul A" f''2--\<^\startTextSpan es''4\!) |
  des''4.\<( c''8 bes'4 des''8 f''8 | aes''2-- g''2)\stopTextSpan | bes''2.~(\mf\< bes''8 beses''8 | aes''2 ges''4 fes''8 es''8) |
  es''4\subP( c'''2.--~ | c'''4)\< des'''4( bes''2) | aes''2.~(\f aes''8 g''8) | f''4.( es''8 des''4 f''8 aes''8) |
  bes''2( aes''2~\> | aes''8 g''8 f''8 es''8 des''4 bes'4) | aes'2\p aes'16(\< c'' des'' es'' f'' g'' aes'' bes'') |
}
% c114: Vln II 47-54 metà: one undivided note against the violas' divided pair makes A♭4 twice as strong as C4 and E♭4 (Rimsky-Korsakov PDF 88: ease the undivided part by reducing players)
tTwoVlnTwo = {
  aes'1\pp^\markup \italic "metà" | aes'1 | aes'1 | bes'1 |
  % c312: 54 E-flat4 held (was E-flat4-D-flat4): the D-flat doubled the tune's chord seventh on beat 4 and then rose to the A-flat chord; the seventh is now single and falls D-flat-C in the tune (Aldwell & Schachter PDF 76, 89)
  ges'1 | f'1 | f'1 | es'1 |
  <es' aes'>2^\markup \italic "tutti, div." r4 \once \override TextScript.self-alignment-X = #LEFT \once \override TextSpanner.bound-details.left.text = \markup \italic \small "sul D" es'4(\p^\markup \left-column { \italic "molto cantabile" "unis." }^\startTextSpan | c''2.~\< c''16\> des''16 c''16 bes'16 | aes'4\!\stopTextSpan \once \override TextSpanner.bound-details.left.text = \markup \italic \small "sul A" f''2--\<^\startTextSpan es''4\!) | des''4.\<( c''8 bes'4 des''8 f''8 |
  aes''2-- g''2)\stopTextSpan | bes'2.~(\mf\< bes'8 beses'8 | aes'2 ges'4 fes'8 es'8) | es'4\subP( c''2.--~ |
  c''4)\< des''4( bes'2) | aes'2.~(\f aes'8 g'8) | f'4.( es'8 des'4 f'8 aes'8) | bes'2( aes'2~\> |
  aes'8 g'8 f'8 es'8 des'4 bes4) | \after 2 \< aes1\p |
}
tTwoVla = {
  <c' es'>1\pp^"div." | <des' f'>1 | <bes des'>1 | <bes des'>1 |
  <aes es'>1 | <aes f'>1 | <bes f'>1 | <bes es'>4 <g bes>2. |
  % c312: 55 A-flat3/C4 div. (was C4 unis.): the leading tone G3 of 54 rises to A-flat and B-flat3 steps to C, as Vln II B4-C5 does at 154-155 (Aldwell & Schachter PDF 76, 80)
  <aes c'>2. r4 |
  % c277: 56-59 rest (were off-beat dyads C4/E-flat4/E4, D-flat4/F4, B-flat3/D-flat4/G4, pp): they sounded in unison with the Cl 1/Hn 2 counterline
  % (E4 at 56, F4 at 57-58, D-flat4 at 58-59), with Hn 3-4's pad (C4 at 56, D-flat4 at 58-59) and with the top of the cello arpeggio (E4 at 56, D-flat4 at 57-58),
  % under the p violin tune. Sebesky PDF 12-13, Ex. 1: a line in the lower-middle register that adds nothing is cut, so the moving parts are heard and the lead dominates.
  % The violas enter at 60 with their own figure, together with Bsn 2 (c167), so the restatement grows by addition (Sebesky PDF 11).
  R1*4 | r8 des'8(\p\<^"unis." ges'8 bes'8 des''4) r4 | r8 des'8( fes'8 aes'8 des''4) r4\! | r4 <c' es'>2\subP^"div." <c' es'>4 |
  r4 <des' g'>2\< <des' g'>4 | r4 <c' f'>2\mf <c' f'>4 | r4 <des' f'>2 <des' f'>4 | r4 <des' f'>2\> <des' f'>4 |
  r4 <des' g'>2 <des' g'>4 | \after 2 \< <c' f'>1\p |
}
tTwoVc = {
  \clef tenor c'2.~\<^\markup \italic "dolce" c'8 bes8\> | aes4\! f'2--\< es'4\!) | des'4.( c'8 bes4 des'8\< f'8 | aes'2\> g'2\!) |
  \clef treble es'4( c''2--\< bes'4\!) | aes'4.(\> g'8 f'4\! f''4~ | f''4 es''8 des''8 c''4. bes'8) | aes'4(\> g'4 bes'4 des'4) |
  c'2.\p r4 | \clef bass aes,8\p( es aes c' e'2) | aes,8( des f aes des'2) | bes,8(\< f des'4.\>) c'8( ces'8 bes8\!) |
  es,8( bes, des g bes2) | ges,8( des ges bes) ges,8( bes, ges es) | fes,8( des fes aes) fes,8(\upbow aes, des fes) | es,4\subP^"pizz." r4 es4 r4 |
  es,4 r4 r2 | % c226: no pizz. E2 on beat 3 (doubled by Cb arco and Bsn 2): two beats more to take the bow for the arco at 64 (Adler adler1 PDF 54)
  f,8(\mf^"arco" c f aes) d,8( aes, c f) | des,8( aes, des f aes2) | bes,8( f bes des') es2\> |
  es,8( bes, des g des'2) | f,8(\p c f aes c'2\<) |
}
tTwoCb = {
% c163: 53 bass D-flat (ii6, 5-6 over the IV of 52; was B-flat ii7): the answering phrase 51-55 rises C-D-flat-E-flat-A-flat to its cadence (Aldwell & Schachter PDF 291-292, Ex. 18-3: I6 ... cadential II6-V7-I; PDF 302 Ex. 18-19d, l). Harp LH/RH and Cb follow; Vla takes F4 so it does not move D-flat-E-flat in octaves with the bass.
  aes,4\pp^"pizz." r4 r2 | des,4 r4 r2 | bes,,4 r4 r2 | es,4 r4 es,4 r4 |
  c,4 r4 r2 | des,4 r4 r2 | des,4 r4 r2 | es,4 r4 es,4 r4 |
  aes,,4 r4 r2 | aes,,1\p^"arco" | aes,,1 | bes,,2 des,2 |
  es,1 | ges,1\< | fes,1 | es,1\subP |
  es,2\< e,2 | f,2\mf d,2 | des,1 | bes,,2 es,2~\> |
  es,1 | \after 2 \< f,1\p |
}
% c131: Tpt 1 no longer doubles the Cl 1 counterline at 60-63 (chromatic, enharmonic F-flat/C-flat line at p); Hn 2 keeps it 56-68
% (Rimsky-Korsakov PDF 72-73: chromatic or enharmonic melodies are much less suited to brass, which lacks geniality; the horn's tone in piano passages gives greater scope)
tTwoTptOne = { R1*22 | }
