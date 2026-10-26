% INTRODUCTION, bars 1–14 (Lento). Concert pitch; Cb and Cbsn at sounding pitch.

introFluteOne = {
  R1*10 | r2 b'4(\mf\< aes''4~ | aes''2.)\f g''4~ | << g''2 { s4\> s4\p } >> r2 | % c258: the top line reaches p on beat 2, where Hn 1's call enters mp (Casanelles PDF 152, 290)
  R1 |
}
introOboeOne = { R1*11 | c''2.\f c''4 | R1*2 | }
introOboeTwo = {
  R1*11 | fis'1\f | g'2\p r2 | R1 |
}
introClOne = { R1*10 | f'1\p\< | es'2.\f es'4 | R1*2 | }
introClTwo = { R1*10 | d'1\p\< | c'2.\f c'4 | R1*2 | }
introBassCl = {
  r2. g,4(\pp | es2.~\< es8\> d8) | c2(\< des4\> c4~ | c1\!) |
  R1*10 |
}
introBsnOne = { R1*8 | g1\pp\< | aes1 \breathe | aes1 | c'2.\f c'4 | R1*2 | }
introBsnTwo = { R1*8 | c1\pp\< | f1 \breathe | d1 | aes,2.\f r4 | g,1\p~\> | g,2.\pp r4 | }
introHnOne = { R1*10 | f'1\p\< | es'2.\f es'4 | r4 es4(\mp c'2~ | c'4\> b2)\p r4 | }
introHnTwo = { R1*10 | d'1\p\< | c'2.\f c'4 | R1*2 | }
introHnThree = {
  % c190: 13 G3 a quarter (was a half): Hn 3 has cleared before Hn 1's call enters on beat 2 below it (Adler adler2 PDF 264: Mozart keeps the orchestral horns silent while the solo horn plays)
  R1*10 | \clef bass aes1\p\< | fis1\f | g4\p r4 r2 |
  R1 \clef treble | % c115: return to treble at the end of the system, after the rests (Gould PDF 23)
}
introHnFour = { R1*10 | d1\p\< | aes,1\f | R1*2 | }
introTbnOne = {
  R1*11 | c'2.\mf c'4 | R1*2 |
}
introTbnTwo = {
  R1*11 | es2.\mf es4 | R1*2 |
}
introBassTbn = {
  R1*11 | aes,1\mf | R1*2 |
}
introTimp = {
  c1:32\ppp~^\markup \small \column { "Timp. in G, A♭, C, E♭" "soft sticks" } | c1:32~ | c1:32~ | c1:32 |
  R1*6 | aes,1:32\pp\< | aes,2:32\f~ aes,4 r4 | g,1:32\p~ |
  << { g,2:32~ g,4 } { s2\> s4\pp } >> r4 |  % c166: rolls end on a tied stroke (Adler part 2 PDF 80, Ex. XII-47; Tchaikovsky 6/i bars 71-75, 136, 154-162)
}
introVlnOne = {
  R1*8 |
  r2. g'4(\mp\< | es''2.) aes'4( | f''2) b'4( aes''4)~ | aes''2.\f\downbow g''4~ | << g''1\downbow { s4\> s2.\p } >> | R1 | % c226: bow changes on the tied A-flat5 and G5 (Adler adler1 PDF 38, Ex. II-20: down- and up-bow marked over the long note; PDF 39-40, Ex. II-23/24: a crescendo under a long slow slur must be broken into bows); was one 6 s up-bow to f, then a 6 s bow from f
}
introVlnTwo = {
  R1*5 | es'1\pp | f'1\< | e'1\p\> |
  es'1\pp\< | f'2. c'4( | aes'2) f'2 | fis'1\f |
  g'1\p\> | f'2.\pp r4 |
}
introVla = {
  R1*5 | bes1\pp | des'1\< | c'1\p\> |
  % c132: 11 c'2 b2 (was d'1): C held from 10 makes the bare root-position ii° a iiø7 with a prepared seventh, resolving to B over the D bass, then B to C at 12 (Aldwell & Schachter PDF 172, 177, 179)
  c'1\pp\< | c'1 | c'2 b2 | <c' es'>2.\f <c' es'>4 |
  % c190: from 13.3 the viola keeps only the 6-5 (E-flat-D); the horn call's C-B (4-3) is no longer doubled in unison, so the horn is led to its C by the viola's C at 13.1
  % and then sounds the cyclic B-natural alone (Adler adler2 PDF 274: accompaniment registrally distant from the soloist; PDF 283: helped in pitch, not doubled)
  <c' es'>2\p\>( d'2) | d'2.\pp r4 |
}
introVc = {
  % c251: sul G for the motto (G2-E-flat3-D3-C3-D-flat3-C3): the whole line on one string, no open D3 and no string crossing on the rising sixth, which becomes one shift
  % from the open G to the fourth position (Adler adler1 PDF 73-74: in slow expressive passages the open string stands out from the stopped notes; PDF 76: mark sul G;
  % PDF 74, Ex. III-5, Tchaikovsky 5/ii sul G). Ends with the D-flat3 at 3; the held C3 stays where the player puts it.
  r2. \once \override TextSpanner.bound-details.left.text = \markup \italic \small "sul G" g,4(\pp\startTextSpan | es2.~\< es8\> d8) | c2(\< des4\>\stopTextSpan c4)~ | c1\! |
  R1 | g1\pp | aes1\< | g1\p\> |
  g1\pp\< | aes1 | aes1 | c'2.\f c'4 |
  g1\p\> | g2.\pp r4 |
}
introCb = {
  % c236: one bow for 3-4 is 8 beats (9.6 s at q = 50) with a swell; the bass bow is shorter and heavier than the cello's, so long slurs and ties
  % are taken with staggered bow changes (Adler adler1 PDF 108: "ask the players to change bow at will"), as already marked at 13, 72, 117 and 179
  r2. g,,4(\pp | es,2.~\< es,8\> d,8) | c,2(\<^\markup \small \italic "change bow at will" des,4\> c,4)~ | c,1\! |
  % c097: the bass at 6-7 is not two octaves below the next voice (Rimsky-Korsakov: bass rarely more than an octave from the part above)
  % c229: unis. G2 / F2 (was div. G1+G2 / F1+F2): the same spacing without a bass section divided in octaves, which Rimsky-Korsakov
  % (rimsky-principles PDF 62, Note II) says to avoid: the halves play on strings that do not correspond and unity of tone is lost.
  % G2 is an octave under the cellos' G3, F2 a tenth under their A-flat3; the motto bass C2-G2-F2-C2 stays one line.
  c,1\pp | g,1 | f,1\< | c,1\p\> |
  c,1\pp\< | f,1 | d,1 | aes,1\f |
  g,1\p~\>^\markup \small \italic "change bow at will" | g,2.\pp r4 |
}

introCorAnglais = {
  R1*4 | r2. d'4(\p\<^\markup \italic "espr." | bes'2.\>~ bes'8\! a'8 | g'2\< aes'4\> g'4~ |
  % c150: the G4 is held into 9 and handed to Vln I's G4 on beat 4 (Rimsky-Korsakov PDF 125-126: the last note of one part coincides with the first of the next)
  % c198: part-only breath licence inside the held G (16 beats, about 19 s, from 5.4 to 9.3 at q = 50; Adler PDF 198: oboists need breathing points); the A-flat-G resolution at 7.3-7.4 stays in one breath (A&S PDF 348) and Vc G3 covers the held G
  g'1~\pp-\tag #'part ^\markup \small \italic "(breathe ad lib.)" | g'2.) r4 | R1*5 |
}