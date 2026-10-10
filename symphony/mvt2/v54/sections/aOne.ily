% A SECTION, bars 7-30 (Adagio, 3/4).
% 7-14  a : the theme in horn 1, accompanied only by clarinets, bassoon 2, bass clarinet and harp (no strings).
%          Theme: a rising A flat arpeggio to a held E flat, then the motto's tail E flat-D-D flat-C
%          read in A flat (5-#4-4-3), harmonised vi7 - V7/V(6) - V7 - I.
% 15-22 b : oboe 1 and the first violins answer each other; to F minor and back to a half cadence.
% 23-30 a': the theme in both violin sections, with a cello counter-melody; full close in A flat.

aOneHnOne = {
  \set Staff.soloText = "1."
  aes4. c'8 es'4~\< | es'4 d'4\> des'4 | c'4.\! bes8 aes4 | g2) es8( f8 |
  aes4. c'8 f'4~\< | f'4 bes'4\mp\> aes'4 | g'4 es'8 des'8 c'8 bes8 | aes2.)\p |
  R2.*16 |
}

% Clarinets tacet 7-14 (critic 004): the accompaniment now lies under the horn (2 bassoons + bass clarinet).
aOneBassCl = {
  aes,2.\pp | f,4 bes,,4 es,4 | aes,2 des,4 | es,2 r4 |  % c036: breath at 10 b3 with bassoon 1; bassoon 2 holds the B flat
  aes,4 c4 des4 | des2 bes,4 | es,2. | aes,2. |
  R2.*16 |
}
% 7-14 (critic 004): close four-part harmony under the horn, Rimsky-Korsakov's "2 Fag. over Cl. basso":
% horn on top, bassoons 1-2 in the middle (thirds and sixths where the progression allows), bass clarinet bass.
aOneBsnOne = {
  es2.\pp | aes4 aes4 g4 | aes2. | es2 r4 |  % c036: breath at 10 b3 under the horn's pickup (Adler part 1 PDF 175, 188)
  es4 aes4 aes4 | aes2 des'4 | bes2 g4 | aes2. |
  R2.*16 |
}
aOneBsnTwo = {
  c2.\pp | c4 bes,4 bes,4 | c2 f4 | bes,2. |
  c4 es4 f4 | f2 r4 | es2. | c2. |  % c036: bassoon 2 breathes at 12 b3 (repeated F dropped), staggered from bars 10
  R2.*16 |
}

% c019: chords voiced so that no harp note sounds above the horn at its attack (Rimsky-Korsakov PDF 90 rule 2, PDF 97 no. 4; Dvorak 7/ii bars 1-8)
aOneHarpR = {
  \clef bass r4 <c es aes>2\arpeggio | R2. | r4 <es aes c'>4\arpeggio <f aes>4\arpeggio | r4 <bes, es g>2\arpeggio |
  r4 <c es aes>2\arpeggio | <aes des' f'>4\arpeggio r2 | r4 <g bes des'>2\arpeggio | \clef treble r4 <aes c' es'>2\arpeggio |
  R2.*16 |
}
% Harp LH doubles the bass an octave lower and changes with it (critic 004), so it never sounds a different bass.
aOneHarpL = {
  \set Staff.ottavationMarkups = #ottavation-numbers \ottava #-1 % c025: 8 bassa for the whole phrase; written pitches were 3-5 ledger lines below (Gould PDF 46-47)
  <aes,, es,>2.\pp\arpeggio^\markup \small \column { \harp-pedal #"^-^|^--^" \italic "(lowest D string tuned to D♭)" }  % c026: the two lowest strings have no pedal; D flat 1 at bar 10 (Adler part 1 PDF 111 footnote)
  | <f,, c,>4\arpeggio <bes,, f,>4\arpeggio <es,, bes,,>4\arpeggio | <aes,, aes,>2\arpeggio des,,4 | <es,, es,>2.\arpeggio |  % c049: 9 A flat octave, not A flat-E flat: E flat2-D flat1 under the horn's passing B flat3-A flat3 made compound fifths with the melody (Rimsky-Korsakov PDF 132-133: the harmonic basis reduced to fundamental notes)
  <aes,, es,>4\arpeggio c,4 des,4 | <des, aes,>2\arpeggio bes,,4 | <es,, bes,,>2.\arpeggio | <aes,, es,>2.\arpeggio \ottava #0 |
  R2.*16 |
}

aOneOboeOne = {
  R2.*8 |
  c''4.(\p\< des''8 es''4 | f''2\> es''4)\! | R2.*2 |
  c''4(\< des''8 c''8 bes'4 | aes'2\> g'4)\! | R2.*2 |
  R2.*8 |
}

% c039: strings con sord. 15-30 (Rimsky-Korsakov Ex. 222: solo violin senza sord. over muted strings; Ex. 228, 256; Dvorak 9/ii Largo and
% Tchaikovsky Op. 35/ii: muted strings in the A section). Mutes on during the rests 4-14, off during 31-36 (all strings rest); senza sord. at 37/45.
aOneVlnOne = {
  R2.*8 |
  R2.*2 | aes''8(\p\<^\markup \italic "solo, senza sord." bes''8 g''4 f''4 | es''2\> des''4)\! |
  R2.*2 | f''8(\< g''8 es''4 d''4\! | es''2) es'8(\mp^\markup \italic "tutti (gli altri con sord.), espr., sul D" f'8 |
  aes'4. c''8) es''4~\< | es''4 d''4(\> des''4) | c''4.(\! bes'8 aes'4 | g'2) es'8( f'8 |
  aes'4.\<^\markup \italic "ord." c''8) f''4~ | f''4 bes''4(\mf\> aes''4) | g''4( es''8 des''8 c''8 bes'8) | aes'2.\p |
}
aOneVlnTwo = {
  R2.*8 |
  aes'2--(\pp^\markup \italic "con sord." aes'4--) | aes'2--( g'4--) | aes'2--( aes'4--) | aes'2--( f'4--) |
  aes'2--( g'4--) | aes'2--( e'4--) | f'2--( f'4--) | bes2 es'8(\mp^\markup \italic "sul D" f'8 |
  aes'4. c''8) es''4~\< | es''4 d''4(\> des''4) | c''4.(\! bes'8 aes'4 | g'2) es'8( f'8 |
  aes'4.\<^\markup \italic "ord." c''8) f''4~ | f''4 bes''4(\mf\> aes''4) | g''4( es''8 des''8 c''8 bes'8) | aes'2.\p |
}
aOneVla = {
  R2.*8 |
  % c017: in each bar where the oboe or Vln I holds, the violas answer in the rhythm of the bar just heard,
  % so the dialogue overlaps and the texture has a middleground (Adler PDF 179, 181; Meistersinger PDF 177-178).
  es'2.\pp^\markup \italic "con sord." | des'4.( c'8 bes4) | f'2 f'4 | c'8( es'8 c'4 des'4) |
  f'2 e'4 | c'4( des'8 c'8 bes4) | aes2 aes4 | g8( aes8 g4 bes4) |
  <c' es'>2.\p^\markup \italic "div." | <c' aes'>4 <bes aes'>4 <bes g'>4 | <c' es'>2. | <bes es'>2. |
  <c' es'>2\< <aes des'>4 | <des' f'>4 <des' f'>4\mf\> <des' f'>4 | <es' g'>2. | <es' aes'>2.\p |
}
aOneVc = {
  R2.*8 |
  c2.\pp^\markup \italic "con sord." | des2 es4 | f2 des4 | c2 bes,4 |
  f2 g4 | f2 c4 | des2 bes,4 | es2. |
  es2\p^\markup \italic "cantabile" aes8( g8 | f2) g4( | aes2 c'4) | bes2( g4) |  % c032: G3 on beat 3 breaks the B flat-E flat / E flat-A flat fifths with the bass into 27 (A&S PDF 266, 271)
 
  es2(\< f4) | \after 4 \mf \after 4 \> aes2( des'4) | bes2( des'4) | c'2.\p |
}
aOneCb = {
  R2.*8 |
  c,2.\pp^\markup \italic "con sord." | des,2 es,4 | f,2 des,4 | c,2 bes,,4 |
  f,2 g,4 | f,2 c,4 | des,2 bes,,4 | es,2. |
  aes,,2.\p | f,4 bes,,4 es,4 | aes,,2. | es,2. |  % c052: 25 bass holds A flat; the cellos' A flat3-C4 no longer moves in octaves with it
  aes,,4\< c,4 des,4 | \after 4 \mf \after 4 \> des,2 bes,,4 | es,2. | aes,,2.\p |
}
aOneHnThree = { R2.*22 | g2.\pp | es2. | }  % c052: G3 -> E flat3 (inner voice), so the leading tone doubled with the violas' G4 does not resolve in octaves (A&S PDF 425 Ex. 25-14, PDF 439)
aOneHnFour = { R2.*22 | es2.\pp | c2. | }
