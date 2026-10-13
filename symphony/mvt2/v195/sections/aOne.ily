% A SECTION, bars 7-30 (Adagio, 3/4).
% 7-14  a : the theme in horn 1, accompanied only by clarinets, bassoon 2, bass clarinet and harp (no strings).
%          Theme: a rising A flat arpeggio to a held E flat, then the motto's tail E flat-D-D flat-C
%          read in A flat (5-#4-4-3), harmonised vi7 - V7/V(6) - V7 - I.
% 15-22 b : oboe 1 and the first violins answer each other; to F minor and back to a half cadence.
% 23-30 a': the theme in both violin sections, with a cello counter-melody; full close in A flat.

aOneHnOne = {
  \set Staff.soloText = "1."
  aes4. c'8 es'4~\< | es'4\> d'4 des'4 | c'4.\! bes8 aes4 | g2) \breathe es8( f8 |
  aes4. c'8 f'4~\< | f'4 \once \stemUp bes'4\mp\> aes'4 | g'4 es'8 des'8 c'8 bes8 | aes2.)\p |
  R2.*16 |
}

% Clarinets tacet 7-14 (critic 004): the accompaniment now lies under the horn (2 bassoons + bass clarinet).
aOneBassCl = {
  aes,2.\pp | f,4( bes,,4-\tag #'part ^\markup \small \italic "(no low C: 8va)" es,4) | aes,2( des,4) | es,2 r4 |  % c036: breath at 10 b3 with bassoon 1; bassoon 2 holds the B flat
  aes,4( c4 des4) | des2( bes,4) | es,2. | aes,2. |
  R2.*16 |
}
% 7-14 (critic 004): close four-part harmony under the horn, Rimsky-Korsakov's "2 Fag. over Cl. basso":
% horn on top, bassoons 1-2 in the middle (thirds and sixths where the progression allows), bass clarinet bass.
aOneBsnOne = {
  es2.(\pp | aes4-- aes4-- g4 | aes2.) | es2 r4 |  % c126: legato slurs, repeated notes soft-tongued (slur + tenuto), as the bass clarinet's slurs (c078) (Adler part 1 PDF 176-177, Ex. VI-5, VI-7)
   % c036: breath at 10 b3 under the horn's pickup (Adler part 1 PDF 175, 188)
  es4( aes4-- aes4-- | aes2-- des'4 | bes2 g4 | aes2.) |
  R2.*16 |
}
aOneBsnTwo = {
  c2.(\pp | c4-- bes,4-- bes,4-- | c2 f4 | bes,2.) |  % c126: slurs as bassoon 1 and the bass clarinet; the slur break at 10-11 lets the player re-tongue or snatch air (7-12 b2 is about 20 s); breath at 12 b3 unchanged
 
  c4( es4 f4 | f2--) r4 | es2.( | c2.) |  % c036: bassoon 2 breathes at 12 b3 (repeated F dropped), staggered from bars 10
  R2.*16 |
}

% c019: chords voiced so that no harp note sounds above the horn at its attack (Rimsky-Korsakov PDF 90 rule 2, PDF 97 no. 4; Dvorak 7/ii bars 1-8)
aOneHarpR = {
  % c057: top notes removed where they struck the pitch the horn was holding or attacking (A flat3 at 7 and 11, C4 and A flat3 at 9 (b3 F3 alone: E flat3-D flat3 under the horn's B flat3-A flat3 made fifths), G3 at 10,
  % F4 at 12): the harp re-articulated the solo's own note (Sebesky PDF 13: focus; PDF 12-13, Ex. 1: a voice taken out so the soloist dominates)
  \clef bass r4 <c es>2\arpeggio | R2. | r4 <es aes>4\arpeggio f4 | r4 <bes, es>2\arpeggio |
  r4 <c es>4\arpeggio r4 | <aes des'>4\arpeggio r2 | r4 <g bes>2\arpeggio | \clef treble r4 <aes c' es'>2\arpeggio |  % c117: 13 D flat4 dropped (was <g bes des'>): the horn carries the 7th E flat4-D flat4-C4 itself; the ringing harp D flat4 sat inside the solo's descent and fell D flat4-C4 at 14 b2 in octaves with Bsn 2's E flat3-C3 (Adler 2 PDF 179, 184; closes the c073 item)
  R2.*16 |
}
% Harp LH doubles the bass an octave lower and changes with it (critic 004), so it never sounds a different bass.
aOneHarpL = {
  \set Staff.ottavationMarkups = #ottavation-numbers \ottava #-1 % c025: 8 bassa for the whole phrase; written pitches were 3-5 ledger lines below (Gould PDF 46-47)
  <aes,, es,>2.\pp\arpeggio-\tag #'score ^\markup \small \harp-pedal #"^-^|^--^"  % c026: the two lowest strings have no pedal; D flat 1 at bar 10 (Adler part 1 PDF 111 footnote)
  | <f,, f,>4\arpeggio <bes,, bes,>4\arpeggio <es,, es,>4\arpeggio | <aes,, aes,>2\arpeggio des,4 | <es,, es,>2.\arpeggio |  % c089: 8 and 13 octaves, not fifths: A flat-E flat/F-C/B flat-F/E flat-B flat and E flat-B flat/A flat-E flat were consonant parallel fifths (A&S PDF 341)  % c049: 9 A flat octave, not A flat-E flat: E flat2-D flat1 under the horn's passing B flat3-A flat3 made compound fifths with the melody (Rimsky-Korsakov PDF 132-133: the harmonic basis reduced to fundamental notes)
  <aes,, es,>4\arpeggio c,4 \once \stemUp des,4 | <des, aes,>2\arpeggio bes,,4 | <es,, es,>2.\arpeggio | << { <aes,, es,>2.\arpeggio } { s4 \ottava #0 s2 } >> |  % c115: 8 bassa line ends with its corner just after the chord, not at the barline (Gould PDF 44)
  R2.*16 |
}

aOneOboeOne = {
  R2.*8 |
  c''4.(\p\<^\markup \italic "dolce" des''8 es''4 | f''2\> es''4)\! | R2.*2 |  % c158: character word on the oboe's solo entry, as every other solo entry of a melody (Sebesky PDF 17-18, Ex. 2/2A: each new colour gets its dynamic and a word)
  c''4(\p\< des''8 c''8 bes'4 | aes'2\> g'4)\! | R2.*2 |
  R2.*8 |
}

% c039: strings con sord. 15-30 (Rimsky-Korsakov Ex. 222: solo violin senza sord. over muted strings; Ex. 228, 256; Dvorak 9/ii Largo and
% Tchaikovsky Op. 35/ii: muted strings in the A section). Mutes on during the rests 4-14, off during 31-36 (all strings rest); senza sord. at 37/45.
aOneVlnOne = {
  R2.*8 |
  R2.*2 | aes''8(\p\<^\markup \italic "solo, senza sord., dolce" bes''8 g''4 f''4 | es''2\> des''4)\! |
  R2.*2 | f''8(\p\< g''8 es''4 d''4\! | es''2) es'8(\mp-\tag #'part _\markup \italic "(solo player: mute on, join at bar 24)" -\tag #'score -\tweak X-offset #-16 ^\markup \italic \override #'(baseline-skip . 2.4) \column { "gli altri con sord.," "espr., sul D" } -\tag #'part -\tweak X-offset #-9 ^\markup \italic \override #'(baseline-skip . 2.4) \column { "gli altri con sord.," "espr., sul D" } f'8 |  % c065: two lines, moved left over the bar: as one line at the system end it widened bar 22 (Gould PDF 53-54)  % c125: the part-only '(solo player ...)' line is now kept out of the score (score.ly), where it stretched bar 22's last eighth to three times a quarter's width (Gould PDF 54); score copy 16 units left so it clears the barline
  aes'4. c''8) es''4~\< | es''4\>^\markup \italic "tutti" d''4( des''4) | c''4.(\! bes'8 aes'4 | g'2) es'8( f'8 |  % c175: "tutti" where the leader rejoins (Adler part 1 PDF 32: when all play again, tutti must appear); 22 b3 now "gli altri con sord."
  aes'4.\<^\markup \italic "ord." c''8) f''4~ | f''4 bes''4(\f\> aes''4) | g''4( es''8 des''8 c''8 bes'8) | \after 2 \pp aes'2.\p\> |  % c063: the strings fade as the bassoon/contrabassoon pedal takes the chord (Adler part 2 PDF 190)
}
aOneVlnTwo = {
  R2.*8 |
  aes'2--(\pp\<^\markup \italic "con sord." aes'4--) | aes'2--(\> g'4--\!) | aes'2--( aes'4--) | aes'2--( f'4--) |  % c139: no swell under the solo violin at 17-18, 21 (Rimsky-Korsakov PDF 123: a solo string's weak tone needs light, transparent accompaniment; PDF 133: the harmonic basis of inferior dynamic power); the swells stay under the oboe at 15-16, 19-20  % c138: Vln II takes the oboe's and solo violin's swells one level down (Casanelles PDF 149-150; Dvorak 9/ii 13-14 violins with the cor anglais)
  aes'2--(\< g'4--\>) | r2\! e'4--\pp | f'2--( bes4--~) |  % c157: 20 b1-2 rest (was aes'2--(\> e'4--\!)): the pedal re-struck A flat4 in unison with the oboe's resolution B flat4-A flat4, the only bar of 15-22 where the pedal lands on the melody's own note; the oboe's arrival is now alone over the violas' answer and the cellos, and Vln II re-enters on the leading tone E natural4 of C7 (Sebesky PDF 13: focus, the ear is not to be diverted from the primary element; PDF 12-13, Ex. 1: a line removed so the others are clearer). F4 at 20 b1 would make octaves G-F with the cellos 19-20.
  bes2 es'8(\mp^\markup \italic "sul D" f'8 |
  aes'4. c''8) es''4~\< | es''4\> d''4( des''4) | c''4.(\! bes'8 aes'4 | g'2) es'8( f'8 |
  aes'4.\<^\markup \italic "ord." c''8) f''4~ | f''4 bes''4(\f\> aes''4) | g''4( es''8 des''8 c''8 bes'8) | \after 2 \pp aes'2.\p\> |
}
aOneVla = {
  R2.*8 |
  % c017: in each bar where the oboe or Vln I holds, the violas answer in the rhythm of the bar just heard,
  % so the dialogue overlaps and the texture has a middleground (Adler PDF 179, 181; Meistersinger PDF 177-178).
  % c067: the answers at 18 and 22 go to the upper cellos (see aOneVc); the violas rest those bars (Sebesky PDF 138: economy).
  es'2.\pp^\markup \italic "con sord." | des'4.( c'8 bes4) | f'2 f'4 | R2. |
  f'2\pp e'4 | c'4( des'8 c'8 bes4) | aes2 aes4 | R2. |
  <c' es'>2.\p^\markup \italic "div." | <c' aes'>4 <bes aes'>4 <bes g'>4 | <c' es'>2 f'4 | es'2. |  % c127: 25 C4 (was A flat3) and 26 E flat4 alone (was B flat3-E flat4): the lower violas sat on the cello counter-melody's A flat3 and B flat3 for two beats each (Adler part 2 PDF 259-260, Ex. XVII-3: the figuration neither duplicates the melodic counterpoint)
  <c' es'>2\< <aes des'>4 | <des' f'>4 <des' f'>4\f\> f'4 | <es' g'>2. | \after 2 \pp <es' aes'>2.\p\> |  % c127: 28 b3 F4 alone (was D flat4-F4 on the cellos' D flat4)
}
aOneVc = {
  R2.*8 |
  % c067: div. at 18 and 22: the upper half answers the solo violin in the viola's rhythm (the violas rest), the lower half keeps the bass with the basses,
  % so the 15-22 conversation has four voices (oboe, solo violin, violas, cellos) and the cellos' answer at 22 leads into their counter-melody at 23
  % (Sebesky PDF 134-136, Ex. 188: the centre of attention passes from player to player; PDF 140 rule 7: the lowest cello need not double every bass note;
  % PDF 139 rule 3: the basses do not sustain the line alone, so half the cellos stay with them; PDF 144: cellos divided, unison for an important counter line).
  c2.\pp^\markup \italic "con sord." | des2 es4 | f2 des4 | << { c'8(-\tweak stencil ##f \pp^\markup \italic "div." es'8 c'4 des'4) } \\ { c2-\tweak stencil ##f \pp bes,4 } >> |  % c160: hidden dynamic for MIDI only: this voice had no dynamic of its own, so score.midi played it at LilyPond's default volume 0.71 (louder than ff) against the printed mark (Sebesky PDF 240-241: compare the score with the recorded result)
  f2^\markup \italic "unis." g4 | f2 c4 | \once \stemUp des2 <fes aes>4^\markup \italic "div." | << { g8(-\tweak stencil ##f \pp aes8 bes4 g4) } \\ { es2.-\tweak stencil ##f \pp } >> |  % c160: hidden dynamic for MIDI only: this voice had no dynamic of its own, so score.midi played it at LilyPond's default volume 0.71 (louder than ff) against the printed mark (Sebesky PDF 240-241: compare the score with the recorded result)  % c192: div. from 21 b3: the upper half takes the French sixth's A flat3 (with the violas) and resolves it to G3 at 22; it played F flat3-G3, an augmented 2nd into V (A&S PDF 136 Ex. 9-3c 'even worse', PDF 138 Ex. 9-6c, PDF 139 Ex. 9-7f); F flat stays in the lower half and the basses
  es2\p^\markup \italic "unis., cantabile" aes8( g8 | f2) g4( | aes2\< c'4)\> | bes2 g4\! |  % c138: the counter-melody swells to its C4 as the violins relax (Casanelles PDF 149-150, 155)  % c032: G3 on beat 3 breaks the B flat-E flat / E flat-A flat fifths with the bass into 27 (A&S PDF 266, 271)  % c118: bes2 g4 on two bows, so the crescendo at 27 is an up-bow and the diminuendos at 28 and 30 down-bows (Adler part 1 PDF 38)
 
  es2(\< f4) | \after 4 \f \after 4 \> aes2( des'4) | bes2( des'4) | \after 2 \pp c'2.\p\> |
}
aOneCb = {
  R2.*8 |
  % c074: basses tacet 15-20 under the oboe/solo-violin dialogue and enter at 21 for the approach to the half cadence (Adler part 1 PDF 130-131, Ex. V-6:
  % the bass is dropped for a lighter texture and brought back at the dominant and the cadence; Dvorak 9/ii Largo: basses rest under the cor anglais tune, 7-14, and return at the cadence)
  R2.*6 |
  \once \stemUp des,2\pp^\markup \italic "senza sord." fes,4 | es,2. |  % c119: basses unmuted under the muted upper strings; from 23 they carry the bass alone (Rimsky-Korsakov Ex. 125, PDF 300: "V-c. II e C-b. (senza sord.)"; Ex. 102, 110, 120: basses not muted; PDF 28: mutes greatly reduce volume)
  aes,,2.\p | f,4 bes,,4 es,4 | aes,,2 des,4 | es,2. |  % c052: 25 bass holds A flat; the cellos' A flat3-C4 no longer moves in octaves with it
  aes,,4\< c,4 des,4 | \after 4 \f \after 4 \> des,2 bes,,4 | es,2. | \after 2 \pp aes,,2.\p\> |
}
aOneHnThree = { R2.*22 | r2 des'4-\tag #'part \pp -\tag #'score -\tweak stencil ##f \pp | c'2. | }  % c099: pp in the part only; on the shared staff horn 4's pp at 29 b1 already covers it (duplicate pp)  % c097: enters with the cellos' D flat4 on 29 b3 instead of holding it from b1, so the counter-melody's last rise B flat3-D flat4 is not pre-sounded by the horn (Adler part 2 PDF 42-44: each line in the clear; PDF 44: horns joining a line in unison)  % c094: D flat4 (the 7th of V7), not B flat3: the two horns held an open fifth E flat3-B flat3 under the strings' melody, and B flat3 was the cellos' own note; D flat4 resolves to C4 at 30 (Rimsky-Korsakov PDF 97 no. 4: when the strings have the upper part, the wind's middle parts use seconds, sevenths, thirds or sixths, no open fourths or fifths; PDF 85: no harmonic note lacking)  % c052: G3 -> E flat3 (inner voice), so the leading tone doubled with the violas' G4 does not resolve in octaves (A&S PDF 425 Ex. 25-14, PDF 439)  % c160: hidden dynamic for MIDI only: this voice had no dynamic of its own, so score.midi played it at LilyPond's default volume 0.71 (louder than ff) against the printed mark (Sebesky PDF 240-241: compare the score with the recorded result)
aOneHnFour = { R2.*22 | es2.\pp~ | es2. | }
% c063: the contrabassoon takes the A flat pedal over from the strings' last chord: it enters pp in unison with the double basses at 30 and
% ties into the woodwind choir at 31, so the colour change from strings to winds overlaps instead of meeting at a barline (Adler part 2 PDF 190:
% the new group "enters unperceived" before the old chord ends, "it is essential that the two chords overlap"; PDF 192: dovetailing, "make
% certain that the seams don't show"; Dvorak 9/ii Largo bars 4-5, 45-46, 53-54: the outgoing group carries into the new section's downbeat).
% Bassoon 2 still enters at 31: an A flat2 at 30 would make a low third with horn 4's C3.
aOneCbsn = { R2.*23 | aes,,2.~\pp | }
