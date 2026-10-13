% A' SECTION, bars 71-82 (3/4).
% 71-78: the theme in Vln I (upper octave) and Vln II; cellos and horns 1-2 play the counter-melody of bar 23.
%        The cadence at 78 is deceptive (F minor).
% c023 (proposed): 78 b1-2 is flat VI (F flat major) under the melody's A flat, the common tone (A&S PDF 585-587, Widmung;
%        PDF 592-593, flat VI by deceptive cadence), F flat-F in the bass to vi on beat 3 (chromatic inflection, PDF 584-585).
% c070 (proposed): 78 b3 bass F flat-E flat (passing I6/4 between flat VI and ii6/5 at 79), not F flat-F: flat 6 goes to 5 before natural 6 returns
%        (A&S Unit 23, PDF 388 and 395 point 3: flat6-natural6-5 is poor; cyclic-notes, mvt I c170: F flat should resolve to E flat, not to F first).
% 79-82: the cadential bars again, ff, peak F6 at 79, full close at 82.
% v03's closing 83-90 (clarinet theme head, horn motto tail over a tonic pedal) is cut (critic 003).

aTwoVlnOne = {
  aes''4. c'''8) es'''4~\< | es'''4\> d'''4( des'''4) | c'''4.(\! bes''8 aes''4 | g''2) es''8( f''8 |
  aes''4.\mp\< c'''8) f'''4~ | f'''4 bes'''4( aes'''4) | g'''4( es'''8 des'''8 c'''8 bes''8) | aes''2\f c'''8( \tuplet 3/2 { f'''16 g''' aes''' } |  % c118: 77 one bow, 78 A flat up-bow into the f, C6 + grace run + B flat6 one down-bow (Adler part 1 PDF 38-39); was 77-78 b2 in one down-bow (about 6 s, mf<f)
  bes'''2.)~\ff | bes'''4(\upbow aes'''2) | g'''4(\> es'''8 des'''8 c'''8 bes''8) | \after 2 \pp aes''2.\p\> |  % c028: p > pp by beat 3 so the harp harmonics (pickup to the coda) are heard (Adler part 2 PDF 503, 505)
}
aTwoVlnTwo = {
  aes'4. c''8) es''4~\< | es''4\> d''4( des''4) | c''4.(\! bes'8 aes'4 | g'2) es'8( f'8 |
  aes'4.\mp\<^\markup \italic "ord." c''8) f''4~ | f''4 bes''4( aes''4) | g''4( es''8 des''8 c''8 bes'8) | aes'2\f c''8( \tuplet 3/2 { f''16 g'' aes'' } |  % c118: as Vln I
  bes''2.)~\ff | bes''4(\upbow aes''2) | g''4(\> es''8 des''8 c''8 bes'8) | \once \override Staff.Hairpin.circled-tip = ##t aes'2\p\> r4\! |  % c063: releases on b3 with the violas, so the harp's harmonic pickup E flat4-F4 is not inside a sustained A flat4/E flat4 (Adler part 2 PDF 274, 267)
}
aTwoFluteOne = {
  R2.*4 |
  R2.*2 | g'''4(\mp\< es'''8 des'''8 c'''8 bes''8 | aes''2)\f \breathe c'''8( \tuplet 3/2 { f'''16 g''' aes''' } |  % c105: grace stems up as in the violins; down-stems put the beam among the ledger lines (Gould PDF 33)  % c178: mp (was p, c123): G6 opens the flute register Adler marks "a bit shrill" (part 1 PDF 185, Ex. VII-2); matches clarinets 1-2 mp< in the same bar, still under the violins (Rimsky PDF 127)
   % c041: breath between the slurs before the ff B flat6 (Adler part 1 PDF 188). c036: B flat6 approached by scale, as in the violins (Adler part 1 PDF 186)
  bes'''2.~\ff | bes'''4 aes'''2) \breathe | g'''4(\> es'''8 des'''8 c'''8 bes''8 | \after 2 \pp aes''2.)\p\> |
}
% c014: flute 2 and oboe 2 double the upper harmony against four horns ff (Rimsky-Korsakov PDF 108-109).
aTwoFluteTwo = { R2.*8 | f'''2.~\ff | f'''2 r4 | R2.*2 | }
aTwoOboeTwo = { R2.*8 | f''2.~\ff | f''2 r4 | R2.*2 | }  % c054: oboe 2 leaves before the diminuendo; its G4-A flat4 doubled Cl 2, Vla and (at 82) oboe 1 in unison (Adler part 1 PDF 249-250, 270)  % c024: F5 fills the sixth between D flat5 and B flat5 (Rimsky-Korsakov appendix PDF 505-507: close spacing in the upper winds; PDF 125); B flat4 at 80 b3 leads to the old G4
aTwoOboeOne = {
  R2.*8 |
  bes''2.~(\ff | bes''4 aes''2) \breathe | g''4(\> es''8 des''8 c''8 bes'8 | \once \override Staff.Hairpin.circled-tip = ##t aes'2)\p\> r4\! |  % c063: as Vln II
}
aTwoVla = {
  c'8(\pp^\markup \italic "ord." es' aes') es'( c' aes) | c'( aes') bes( aes') bes( g') | c'( es' aes') c'( es' aes) | des'( es' g') es'( bes des') |  % c127: 74 b1 D flat4 (was B flat3 on the cellos' B flat3)  % c060: D flat4 (7th of V4/3) resolves to C4 at 75 (was bes( es' g') es'( bes es'))  % c085: "unis." dropped here and at 79: no divisi since 64 (Adler part 1 PDF 30: unis. cancels div.)
  c'(\p\< es' aes') es'( aes f') | f'( aes' f') bes( f' bes) | g( es' g') es'( bes g) | aes(\f fes' aes') fes'( c' g) |  % c127: 76 b3.5, 77 b1.5 and b3.5: the figure no longer strikes the counter-melody's D flat4 and B flat3 (Vc, Hn 2) on its own notes (Adler part 2 PDF 259-260, 274); 78 b3 C4 kept (E flat4 there moves in octaves with the bass's F flat-E flat)
  % c042: 80 b3 F flat4 (with horn 3): F-F flat-E flat (6-flat 6-5) into 81, ii-half-diminished 7th before V7 (A&S PDF 391-392, 395)
  bes'2.~\ff | bes'4(\upbow aes'2) | g'4(\> es'2) | \once \override Staff.Hairpin.circled-tip = ##t es'2\p\> r4\! |  % c074: the third octave leaves the theme at 81 b2 (was es'8 des'8 c'8 bes8 | aes2): its D flat4-C4-B flat3-A flat3 ran into and under the cello/horn counter-melody (D flat4-C4), unison at 81 b2.5 and crossed at 82 (Adler part 1 PDF 144: theme and countertheme separated registrally; PDF 142: order of priority)  % c071: the theme's third octave at the peak (Adler part 2 PDF 24, Ex. XI-8: Elgar's octave and double-octave doublings; PDF 23: the melody notes to stress made to dominate); F and A flat stay in Fl 2, Ob 2, Hn 3-4, Cl 2, harp  % c063: the violas' E flat4 was the harmonic pickup's own pitch (sounding E flat4) on b3; they release with Vln II and Ob 1
}
aTwoVc = {
  es2\p^\markup \italic "cantabile" aes8( g8 | f2) g4( | aes2\< c'4)\> | bes2 g4\! |  % c118: g4 its own bow, so the crescendo at 75 is an up-bow and the f at 78 a down-bow (Adler part 1 PDF 38)  % c032: as at 26 (fifths with the bass into 75; A&S PDF 266)
 
  es2(\mp\< f4) | aes2( des'4) | bes2( des'4) | ces'2\f c'4 |
  des'4 c'4 bes4 | aes2 bes4--~ | bes4\> des'2-- |  % c118: one bow per hemiola half note (A flat | B flat | D flat), so the diminuendo at 82 is a down-bow (Adler part 1 PDF 38)
  \after 2 \pp c'2.\p\> |  % c048: hemiola 80-81 (A flat 2 | B flat 2 | D flat 2): two bars of 3/4 heard as one bar of 3/2 before the cadence (A&S PDF 51, Ex. 3-8)  % c074: 79 stays f from 78 (was ff), as horns 1-2 (c034): the counter-melody on the cello's A string is its most intense register and is middleground under the ff theme (Adler part 1 PDF 135; PDF 144: dynamics graded)
}
aTwoHnOne = {
  R2.*7 | \partCombineUnisono r2 c'4(\mf\< |
  des'4\f c'4 bes4) \breathe | aes2( bes4--~ | bes4\> des'2-- | \once \override Staff.Hairpin.circled-tip = ##t c'2)\p\> r4\! \partCombineAutomatic |  % c048: hemiola 80-81 with the cellos; breath moved to the end of 79  % c034: f, not ff (also horn 2): the counter-melody stays middleground under the theme (Adler part 2 PDF 147, 154)
}
% c006: the 71-78 counter-melody moves to horn 2, so horn 1 rests after its solo at 67-70.
% c067: horn 2 joins the cellos' counter-melody at 75 with the crescendo, not at 71: horn and cello in unison is an intense sound to be used sparingly
% (Sebesky PDF 166), and here it already returns at 79-82 (Hn 1-2, Vc, Bsn 1); 71-74 keep the cellos alone, as at 23-26. Was es2\p aes8( g8 | f2 g4 | aes2 c'4 | bes2 g4) |
aTwoHnTwo = {
  R2.*4 |
  es2(\mp\< f4 | aes2 des'4 | bes2 des'4)\mf | r2 c'4(\mf\< |  % c035: the crescendo ends on mf at 77 b3, not on the p of the new entry
  des'4\f c'4 bes4) \breathe | aes2( bes4--~ | bes4\> des'2-- | \once \override Staff.Hairpin.circled-tip = ##t c'2)\p\> r4\! |  % c048: hemiola 80-81
}
% c037: at 80 the inner parts (Hn 3-4, Vla, Cl 2, Ob 2) hold instead of repeating quarters, so the only quarter-note motion
% is the counter-melody (Vc, Hn 1-2, Bsn 1) against the held B flat6-A flat6 (Adler part 2 PDF 230: lean texture makes the big chord tell;
% PDF 217: two layers in the same note values need separating).
aTwoHnThree = { R2.*8 | f'2.\f | f'2 fes'4~\< | \once \override Staff.Hairpin.circled-tip = ##t fes'4\> es'2 | R2.\!^\markup \small \italic "mettere sord." | }  % c082: F flat4 held over the bar as a 9-8 suspension: V minor-9th by mixture (A&S PDF 464 Ex. 27-3; PDF 465 Ex. 27-4c: the 9th as a common tone from II; PDF 466 Ex. 27-5: 9-8 inside V), resolving to E flat4 as the 7th D flat enters  % c064: advance mute warning, five bars before con sord. at 87 (Adler part 2 PDF 50, Ex. XI-27/XI-29: mutes marked where they go on and off)  % c024: horns 3-4 leave first in the diminuendo (Rimsky-Korsakov PDF 130). c014: horns 3-4 in the middle of the chord, bass left to Bsn 2 and B.cl. (Rimsky-Korsakov PDF 101, 108)
aTwoHnFour = { R2.*8 | aes2.\f | aes2~ aes4\< | \once \override Staff.Hairpin.circled-tip = ##t g2\> es4 | R2.\!^\markup \small \italic "mettere sord." | }  % c122: 81 b3 E flat3, not G3 held: the leading tone was doubled (Cl 2 G4, Hn 4 G3) on the beat before the goal tonic and horn 4's G3 stopped unresolved; G3 now moves to the root inside V7 and only Cl 2's G4 carries the leading tone, which resolves (A&S PDF 267, 286: doubled leading tone not before a goal tonic)  % c044: horns 3-4 f, not ff, at 79: sustained harmony inside the horn counter-melody's register is not marked louder than the counter-melody (Hn 1-2 f) (Adler part 2 PDF 184: dynamics graded by importance; PDF 159 rule 1)
aTwoClOne = {
  % c067: rests 71-74 and joins the lower octave at 75 with the crescendo, as flute 1 joins the upper octave: at 71-74 the lower octave (Vln II + Cl 1)
  % outweighed the lead (Vln I alone) (Sebesky PDF 138 rule 2: the lead line carried by more players than any other line; PDF 164: one woodwind weighs
  % about as much as sixteen violins; PDF 139 rule 4: the higher line needs more players). Was aes'4.(\pp dolce c''8 es''4~ | es''4 d''4 des''4 | c''4. bes'8 aes'4 | g'2) r4
  R2.*4 |  % c059: clarinet 1 doubles the theme's lower octave with Vln II from 71 (Brahms 1/ii reprise re-scored; Adler part 1 PDF 238, 255, 267 Ex. VIII-38)  % c036: breaths at 74 b3, 78 b3 and after 80 (Adler part 1 PDF 175, 188)
  % c079: rests 75-76 and joins at 77 with flute 1 (c078), so the two octaves gain a wind each at the same moment: with flute 1 gone from 75-76
  % the lower octave (Vln II + Cl 1) again outweighed the lead (Vln I alone), the imbalance c067 removed at 71-74 (Adler part 2 PDF 209: the melodic
  % figure emphasised by the most doubling; PDF 213, Bizet 13-18: the crescendo orchestrated by adding instruments). Was aes'4.(\p\< dolce c''8 f''4~ | f''4 bes''4 aes''4 |
  \partCombineSoloII R2.*2 | \partCombineAutomatic g''4(\mp\< es''8 des''8 c''8 bes'8 | aes'2)\f r4 |
  bes''2.~(\ff | bes''4 aes''2) \breathe | g''4(\> es''8 des''8 c''8 bes'8) | \after 2 \pp c''2.\p\> |  % c034: theme's middle octave with Ob 1 and Vln II, so the B flat5 line outweighs the ff counter-melody (Adler part 2 PDF 151: Mozart 40/iv, the heaviest-scored octave is heard as the theme)
}
aTwoClTwo = {
  aes'2.(\pp | aes'4-- f'8 bes'8~ \once \stemUp bes'4 | aes'2. | des'2) r4 |  % c126: legato slurs with soft-tongued repeats (Adler part 1 PDF 176-177); breaths unchanged
   % c073: 74 D flat4 (was G4, a unison with Vln II): the 7th of V4/3 sustained, so the chord over the B flat bass is complete (A&S PDF 127 sec. 7); it passes to the violas' D flat4-C4 (74 b3.5-75), the last voice that has it (PDF 102 sec. 15)  % c059: B flat4 at 72 b3: G4-A flat4 moved in octaves with the horn 2/cello counter-melody's G3-A flat3 into 73  % c036: breaths at 74 b3, 77 b3 (staggered with clarinet 1) and after 80  % c061: B flat4 anticipated on 72 b2.5 (A&S PDF 363-366): F4-B flat4 over B flat1-E flat2 made parallel 5ths with the bass at 72 b2-b3
  aes'2.(\p\< | aes'4-- f'2) | g'2\mp\< r4 | \tag #'score { r2\f } \tag #'part { r2 } g'4-\tag #'part \f |  % c145: in the part the f stood under the half rest; it now marks clarinet 2's own entry on b3 (Adler part 2 PDF 301, Ex. XVIII-10b: each part carries its own dynamics); the score is unchanged (shared f on b1, "2." at b3)
    % c144: rests at 78 b1-2 (was aes'2, a unison with clarinet 1 on the theme's A flat4 at f): two like winds in unison only thicken the pitch outside a full tutti, and the A flat stays in octaves with flute 1 (Adler part 1 PDF 249-250, 257); the f on the rest keeps one shared dynamic  % c124: mp (was mf) so clarinet 1's entry on the lower octave is not louder than flute 1's p< on the upper octave (c123); keeps c079's balance of the two octaves (Adler part 2 PDF 150-151)  % c079: mf< with clarinet 1's entry (shared staff, one dynamic)
  f'4\ff des''2 | des''2. \breathe | g'2.\> | \after 2 \pp aes'2\p\> r4 |  % c123: F4 on 79 b1 (was A flat4): the resolution A flat no longer sounds a second under the violas' B flat4 appoggiatura (Rimsky-Korsakov PDF 132-133); Hn 4 keeps A flat3  % c063: releases on b3 (A flat4 above the harmonic pickup); clarinet 1's pp ends the shared hairpin  % c034: takes clarinet 1's D flat5 (keeps c024's fill between D flat5 and B flat5); G4 at 81, not B flat4, so no D flat-B flat octaves with the cellos, horns and Bsn 1; A flat4 held over the bar line at 79 so it does not leap A flat-D flat in octaves with the cellos
}
% c094: bassoon 1 joins the cello/horn 2 unison from 75 (p<, as bassoon 2 on the shared staff): horn and cellos alone in unison 'do not blend so well', each heard too distinctly; 'the combination of the three different timbres in unison produces a rich, mellow and coherent tone', the bassoon linking wood-wind and brass (Rimsky-Korsakov PDF 51-53).
% c011: bassoon 1 joins the cello and horn counter-melody at the ff return (Rimsky-Korsakov PDF 54, 56: relief by doubling; Antar [63] cellos doubled by bassoons).
aTwoBsnOne = { R2.*4 | es2(\p-\tag #'part \< f4 | aes2 des'4 | bes2 des'4-\tag #'part \mf) \breathe | ces'2-\tag #'part \f c'4(-\tag #'part \< | des'4\ff c'4 bes4) \breathe | aes2( bes4--~ | bes4\> des'2-- | \after 2 \pp c'2.)\p\> | }  % c048: hemiola 80-81  % c134: 78 b1-2 C flat4 with the cellos (was r2): the F flat chord of the deceptive cadence had no C flat in the winds and the counter-melody lost its wind colour for two beats (Adler part 2 PDF 162, 164, 176)  % c176: breath at the end of 77 (the slur ends there; horn 2 rests 78 b1-2 but bassoon 1 plays on): 75-79 b3 was about 17.7 s without a breath, p< to ff (Sebesky PDF 24 item 11, PDF 30 Ex. 33)
aTwoBsnTwo = {
  c2.(\pp | f4 bes,4 es4 | aes,2 f4 | bes,2) r4 |  % c126: slurs (Adler part 1 PDF 176)
   % c060: with the basses (was aes,2. | es2 r4)  % c052: 71 C3 resolves the D flat3 of 69-70 in its own line; 73 A flat held (no A flat-C octaves with the cello/horn counter-melody)  % c036: breaths at 74 b3, 77 b3 and after 80; the double basses keep the bass
  aes,4(\p\< c4 des4 | des2-- bes,4 | es2) r4 | fes2(\f es4) |
  des2.\ff | des2 bes,4 \breathe | es2.\> | \after 2 \pp aes,2.\p\> |
}
% c024: contrabassoon doubles the double basses at the A' peak, so the ff bass has more than the double basses at 16' pitch
% (Rimsky-Korsakov, appendix of single tutti chords, PDF 505-507: every ff chord doubles the bass in the low octave with C-fag./tuba + Cb.).
aTwoCbsn = { R2.*8 | des,2.\ff | des,2 bes,,4 \breathe | es,2.\> | \once \override Staff.Hairpin.circled-tip = ##t aes,,2\p\> r4\! | }  % c176: breath at the end of 80 with bass clarinet and bassoon 2 on the same line (79-82 b2 was about 14 s at ff without one; Sebesky PDF 70, 74, PDF 30 Ex. 33)
aTwoBassCl = { R2.*8 | des2.\ff | des2 bes,4 \breathe | es,2.\> | \after 2 \pp aes,2.\p\> | }
aTwoCb = {
  aes,,2.\pp^\markup \italic "tutti" | f,4 bes,,4 es,4 | aes,,2 f,,4 | bes,,2. |  % c060: 73-74 I-vi7 | V4/3 (was A flat held | E flat, as at 25-26): the reprise's first phrase is not harmonised as at 23-26 (Sebesky PDF 19-20, Ex. 3/3A)  % c052: as at 25
  aes,,4\p\< c,4 des,4 | des,2 bes,,4 | es,2. | fes,2\f es,4 |
  des,2.\ff | des,2 bes,,4 | es,2.\> | aes,,2.~\p\> |  % c063: diminuendo to the coda's ppp (83), tied into the coda pedal, so the pedal is already sounding under the harp's pickup (Adler part 2 PDF 192)
}
aTwoTimp = { R2.*8 | des2.:32\f^\markup \small \italic "ord." | des2.:32 | \once \override Staff.Hairpin.circled-tip = ##t es2.:32\> | R2.\! | }  % c123: no A flat2 stroke at 82; the E flat roll is answered by the timpani's own E flat-C-A flat at 84-85 (Rimsky-Korsakov PDF 136: a group silent for some time gains fresh interest on its reappearance)  % c056: single stroke, no hairpin (a struck note cannot diminish); damped on b3 under the harp harmonics (Adler part 2 PDF 80)
aTwoHarpR = {
  R2.*4 |  % c034: RH tacet 71-74: its chords were the viola figure's own notes in the same octave on the same beat (Adler part 2 PDF 158: no two instruments with identical parts for more than a few notes); it re-enters after a rest with the crescendo at 75 (PDF 156)
  r4 <aes c' es'>4\arpeggio r4 | <des' f'>4\arpeggio r2 | r4 <g es'>2\arpeggio | r2 <g es'>4\arpeggio |  % c127: 76 without A flat3, 77 G3-E flat4 (was G3-B flat3-D flat4), 78 b3 G3-E flat4 (was G3-C4-E flat4): no attacks on the counter-melody's A flat3, B flat3, D flat4 and C4 (Adler part 2 PDF 259-260, 274)
  R2.*3 | r4 <aes c'>4\arpeggio es'8 f'8 |  % c116: pickup at pitch, not harmonics: at 82 b3 flutes, clarinets, B.cl., bassoons, Vln I, Vc and Cb still hold the p>pp chord; harmonics start at 83 over the ppp pedal only (Adler part 1 PDF 116, rule 1)  % c026: octave harmonics, written an octave below the sound (Adler part 1 PDF 116); hidden voice carries the sounding pitch to MIDI  % c019: harp head starts here (pickup), so the timpani answer and the Vln I tail in the coda do not overlap
}
aTwoHarpL = {
  \set Staff.ottavationMarkups = #ottavation-numbers \ottava #-1 % c025: as at 7-14 (Gould PDF 46-47)
  <aes,, es,>2.\pp\arpeggio-\tag #'score ^\markup \small \harp-pedal #"^-^|^--^" | <f,, f,>4\arpeggio <bes,, bes,>4\arpeggio es,,4 |  % c089: 72 octaves and 73 b3 single F, not fifths: A flat-E flat/F-C/B flat-F were consonant parallel fifths (A&S PDF 341); a dyad F1-F2 at 73 b3 made fifths F/C -> E flat/B flat with the cellos into 74
  <aes,, es,>2\arpeggio f,,4 | <bes,, bes,>2.\arpeggio |  % c114: B-flat octave, no fourth in the lowest octave (Rimsky-Korsakov PDF 124). c060: with the basses (was <aes,, es,>2. | <es,, es,>2.)
  <aes,, es,>4\p\<\arpeggio c,4 \once \stemUp des,4 | <des, aes,>2\arpeggio bes,,4 | <es,, es,>2.\mf\arpeggio | r2 <es,, es,>4\f\arpeggio \ottava #0 |  % c116: harp grows with the orchestra (p<mf, f at 78 b3; Adler part 1 PDF 113-114: middle register rich, carries)  % c115: line ends after the last note before the 79-81 rest (Gould PDF 45: separate signs across extensive rests; PDF 44: corner after the notehead)  % c114: octaves as at 10 and 13 (no fifth E-flat1-B-flat1 or sixth E-flat1-C2 in the lowest octave: Rimsky-Korsakov PDF 124-125)
  R2.*3 |  % c079: no re-entry on 81 (was <es,, bes,,>2.\mf\>, RH r4 <g bes des'>2): after the 79-80 rest a fresh mf attack fell inside the orchestrated diminuendo; the harp returns p on the tonic at 82 (Adler part 2 PDF 213, 224: the diminuendo made by instruments dropping out)  % c076: tacet 79-80 under the ff tutti (Rimsky-Korsakov PDF 47: three or four harps in unison to be heard against a full orchestra forte)
  \ottava #-1 <aes,, es,>2.\p\arpeggio |  % c115: new 8 bassa sign just before the first note after the rests (Gould PDF 44-45)  % c026: 8 bassa continues into 83 (no loco needed)  % c019: harp dies away with the orchestra (was f to the end)
}
