# Movement II (Adagio, A♭ major): current state for the other movement threads

Owner: the thread "Movement II, 200 more loops" (session cse_01WWGdo2VND72g1pVzSE2829; third series, cycles 201–400, from 2026-10-19). Only that thread edits this file. Written 2026-10-12; the third series updates it whenever a change touches another movement.
Current version: symphony/mvt2/v259 (third series; newest text files in symphony/mvt2/latest/; versions on branch claude/project-thread-wtf58k) (92 bars, 8 A3 pages, concert-pitch score; score.ly, global.ily, sections/*.ily). score.midi lasts 345.3 s, about 5:45. Changes since v181 (updated 2026-10-13 after cycle 190): contrabassoon an octave lower at 79–81 (D♭1–B♭0–E♭1; B♭0 is now the movement's lowest note); cor anglais doubles the violas at 79–82, so theme A's three octaves at the second peak each have strings + a wind (Fl 1 + Vln I, Ob 1 + Cl 1 + Vln II, Vla + C.a.); stem fixes; string bowings at 45–47 and 75–81; horn slurs at 80–81 and 87–90; cello divisi at 21 and a viola note at 43 (v193); horn 1 doubles horn 2 at 61–62 and the violas divide at 87–88 to double both muted horns and join on E♭3 at 89 (v195, v200); a suspension accent at 58 (v199); release title and part fixes (v201). No change to the ending's notes, the exported themes or the quotations.

Pitch names: C4 = middle C. The double basses and contrabassoon are given at sounding pitch, as the section files write them (the score prints them an octave higher).

Sections and metre (sections.txt):

| Bars | Section file | Metre |
|---|---|---|
| 1–6 | intro | 3/4 |
| 7–30 | aOne | 3/4 |
| 31–36 | trans | 3/4 |
| 37–64 | bSec | 4/4 |
| 65–70 | retr | 3/4 |
| 71–82 | aTwo | 3/4 |
| 83–92 | coda | 3/4 |

## Opening (bars 1–6, Adagio, crotchet = 52)

**Bar 1 continues movement I's last chord.** Movement I ends C2 G2 C3 G3 C4 E4 G4 C5. Five of its parts cross over, written in movement II with \repeatTie at ppp:

| Note at bar 1 | Instrument | What it does next |
|---|---|---|
| C3 | cellos | falls to A♭2 at 2 (pp) |
| C4 | Horn 3 | held to beat 2 of bar 1, then rests; re-enters on C4 at 3 |
| E4 | violas | falls to E♭4 at 2 (pp), the E♮ of movement I turned back to E♭ |
| G4 | Violins II | rises to A♭4 at 2 (pp) |
| C5 | Violins I | held, tied, ppp, through bars 1–3 ("change bow at will") |

- Horn 4 enters on beat 2 of bar 1 on C4 ppp (labelled "4." in the score) and holds it through bar 2 with a crescendo and a breath, so Horn 3 can breathe.
- So bar 1 sounds C3 C4 E4 G4 C5: C major with nothing below C3. The double basses, Horn 4's G3, the timpani and the harp of movement I's last chord do not continue (movement I releases them at the end of its bar 182; the harp is damped there).
- **Bar 2: A♭ major.** Double basses enter on A♭1 pp; cellos A♭2, Horn 4 C4, violas E♭4, Vln II A♭4, Vln I C5. Timpani roll A♭2 ppp, bars 2–3.
- **Bar 3:** the strings hold the bar 2 chord with a diminuendo to niente and rest from bar 4. The winds take the chord over at pp: bass clarinet A♭2, Clarinet 2 E♭3, Horn 4 A♭3, Horn 3 C4.
- **Bars 3–6, winds only:** Horn 3 C4 (3–4), D♭4 (5), C4 (6); Clarinet 2 E♭3, F♭3, E♭3; Horn 4 A♭3 and bass clarinet A♭2 held. Bar 5 is D♭ minor over A♭ (iv6/4, with F♭), bar 6 A♭ major. Clarinet 1 rests in 1–6.
- **Bar 6, beat 3:** Horn 1 pickup E♭3–F3, p, "1. solo", "dolce espr.", into theme A at 7.
- Not playing in 1–6: flutes, oboes, cor anglais, bassoons, contrabassoon, Horns 1·2 (except Horn 1's pickup), trombones, tuba, harp.
- **Tempo:** "Adagio", crotchet = 52.
- **Timpani label at bar 1:** "Timp. in G, A♭, C, E♭ (as in movement I)" and "soft sticks". At bar 5: "muta G in D♭ (A♭, C, D♭, E♭)" (wording since v215) (the G drum goes to D♭; G2 is never played in this movement).
- **Attacca:** the score's front page says "Follows movement I attacca: bar 1 continues its last chord". Each part prints "attacca from movement I" under bar 1 (partGlobal in parts-book.ly).

## Ending (coda, bars 83–92)

**Tempo.** Rehearsal mark K at 83, "a tempo" (crotchet = 52). "rit." from 89 to the end. Fermata on 92 in every part. The final barline is "|.".

**Bars 83–88.**
- 83–86: A♭ pedal, ppp: double basses A♭1 and cellos A♭2 (held 83–86, crescendo at 86).
- 82 b3–83: harp, the theme A head: pickup E♭4–F4 at pitch on 82 b3 (after an arpeggiated A♭3–C4), then harmonics at 83, A♭–C–E♭ in the rhythm crotchet-dot, quaver, crotchet (written A♭3 C4 E♭4, sounding an octave higher, A♭4 C5 E♭5), over a left-hand A♭1. This is the harp's last bar; it is silent 84–92.
- 84–85: timpani alone answer E♭3 (dotted crotchet), C3 (quaver), A♭2 (tied into 85), pp. This is the timpani's last sound. There is no timpani roll in the last bars.
- 84 (beat 3)–86: violas div. C4–E♭4 ppp, then C4–F4 at 86.
- 85–89: Clarinet 1, "dolce", plays the motto's tail: E♭5 (85, ppp < pp), D5 (86), D♭5 (87–88, pp), C5 (89–90, to beat 2 of 90).
- **87: IV6.** Bass F (cellos F2, double basses F1); violas divided (since v195): lower half F3 sul C with Horn 4, upper half A♭3 with Horn 3 (87–88; since v224 the lower half falls to E♭3 at 89 and the upper half holds A♭3 to the end); Horn 4 F3 and Horn 3 A♭3, both con sord., pp; cor anglais F4 pp "dolce"; Vln II A♭4 pp; Cl 1 D♭5.
- **88: iv.** Bass D♭ (cellos D♭3, double basses D♭2); lower violas, Horn 4 and cor anglais F♭ (F♭3, F♭3, F♭4; upper violas A♭3); Horn 3 A♭3; Vln II A♭4; Cl 1 D♭5.
- **89: I.** Bass A♭ (A♭1, A♭2); the F♭s resolve to E♭ (lower violas E♭3, upper violas hold A♭3, Horn 4 E♭3, cor anglais E♭4); Clarinet 2 enters on E♭4; Vln I enters on C5 pp, taking over Cl 1's C5.
- 90: Cl 1, cor anglais and Horns 3·4 stop on beat 2 (diminuendo).

**Last chord (bars 89–92), bottom to top, ppp at 92, under a fermata:**

| Note | Instruments |
|---|---|
| A♭1 | double basses |
| A♭2 | cellos |
| E♭3 | violas, lower half (sul C) |
| A♭3 | violas, upper half (since v224; held from 87) |
| E♭4 | Clarinet 2 ("morendo" at 91) |
| A♭4 | Violins II |
| C5 | Violins I (up-bow entry at 89, pp, diminuendo at 91) |

- The top note C5 is the pitch movement I ended on and the pitch movement II began with.
- Only strings and Clarinet 2 play in 91–92. Flutes, oboes, Clarinet 1, bass clarinet, bassoons, contrabassoon, all horns, trombones, tuba, timpani and harp rest (the wind staves carry the fermata on a rest).

**Mutes at the end.**
- Horns 3·4 play con sord. at 87–90 ("mettere sord." at 82, during their rest). Both have "via sord." at 91 and rest in 91–92. They are the only muted instruments in the coda.
- The strings are not muted. (They were muted at 15–30 only.)

**Timpani muta at 92.** In the timpani part only (the text is tagged 'part and does not print in the full score): "muta A♭ in E, C in G, D♭ in B, E♭ in E" / "(for the Scherzo, during the pause)". The drums go from A♭2, C3, D♭3, E♭3 to E2, G2, B2, E3.

**Not attacca.** No "attacca" is printed at the end in the score or the parts. The movement ends with a fermata and a final barline, and the scherzo follows after a pause.

## Key plan, rehearsal marks and tempo

Key signatures are set in global.ily. Harmonic labels come from the section files' notes.

| Bars | Mark | Section | Key and harmony |
|---|---|---|---|
| 1–6 | | Link from movement I (Adagio, crotchet = 52) | A♭ major key signature. C major at 1 (movement I's chord), A♭ at 2, iv6/4 at 5, I at 6. |
| 7–14 | A | Theme A in Horn 1, no strings | A♭ major. Tail E♭–D–D♭–C at 8 over vi7 – V7/V – V7, I at 9; second phrase ends on I at 14. |
| 15–22 | B | Oboe 1 and solo violin in dialogue, muted strings | A♭ major toward F minor; French sixth over F♭ (cellos, double basses) on beat 3 of 21; half cadence on E♭ at 22. |
| 23–30 | C | Theme A in both violin sections, cello counter-melody | A♭ major; full close at 30. |
| 31–36 | | Transition: bass clarinet solo, woodwinds alone | A♭ pedal (contrabassoon A♭1, 30–36). Common-tone diminished seventh on beat 2 of 33. poco rit. 35–36. |
| 37–44 | D | Theme B, flute 1 then cor anglais (4/4, Poco più mosso, crotchet = 60) | D♭ major key signature. |
| 45–46 | E | Theme B head in B♭ minor (oboe 1) | B♭ minor, D♭ major key signature. |
| 47–50 | | Quotation of movement I's second-theme head (cor anglais) | F♯ minor key signature from 47. D♭7 respelled C♯7 at 47 (Vln II E♯4, double basses C♯1). poco rit. at 47, poco sostenuto from 48. |
| 51–52 | | Return to D♭ | D♭ major key signature from 51; A♭ pedal (double basses A♭1). |
| 53–60 | F | Theme B in the violins; crescendo | D♭ major. "a tempo, poco a poco animando" at 53; poco allargando at 60. |
| 61–62 | G | Climax, ff (Largamente, crotchet = 54) | D♭ major at 61; G♭ (bass G♭1) to F♭ major (bass F♭1) at 62. |
| 63–64 | | Quotation of movement I's first-theme head (Trombone 1) | A minor key signature from 63. allargando at 64; since v241 the falling eighths at 63 slur into the repeated A, which is portato (matches movement I v251); bass D–E on beats 3–4 of 64. |
| 65–70 | H | Retransition (3/4, Tempo I, crotchet = 52) | A♭ major key signature. V7 of A♭ (E♭2 B♭2 G3 D♭4) over the double basses' E♭2 pedal, 4 soli, 65–70. |
| 71–82 | J | Theme A returns, violins in octaves | A♭ major. poco allargando from 78. Bass F♭2–E♭2 at 78 (F♭ major on beats 1–2), D♭ at 79–80, E♭ (V) at 81, I at 82. |
| 83–92 | K | Coda (a tempo, rit. from 89) | A♭ pedal 83–86; IV6 (87) – iv (88) – I (89–92). |

There is no rehearsal mark at 31 or 47. The marks are A–K without I. Tempo markings in full: Adagio crotchet = 52 (1); poco rit. (35); Poco più mosso crotchet = 60 (37); poco rit. (47, beat 3); poco sostenuto (48); a tempo, poco a poco animando (53); poco allargando (60); Largamente crotchet = 54 (61); allargando (64); Tempo I crotchet = 52 (65); poco allargando (78); a tempo (83); rit. (89).

## Changes in the third series (cycles 201–, from 2026-10-19)
- v202: counter-melody 54–55 as above; cellos E♭2 at 55 b1–2.
- v203: Vln II A5 at 49 b1–2 (third of F♯ minor).
- v205: double basses divided in octaves at 23–28.
- v208: violas A♭3 at 27 b2.
- v209: "mettere sord." for Vln I (not the soloist), Vln II, Vla, Vc at bar 4.
- v211: bar 64 b4, cellos B2 (was E2): the chord under the end of the trombone quotation is a complete German sixth of A♭ (E2–B2–G♯3–D4 = E7, V7 of A minor), every voice falls a semitone into E♭7 at 65. The trombone quotation's notes are unchanged. Since v233 the cellos anticipate B♭2 on the last eighth of 64 (momentary French sixth), removing Cb/Vc fifths into 65.
- v215: timpani "damp" at 53; harp A♭1 tied from 82 into 83 under the harmonics; bar-5 muta wording.
- v218: Vc ff at 79; Hn 2 one level softer at 75–77.
- v219: low brass f at 61 (was mf); trombone 1's quotation of movement I at 63–64 now ends p on its last note E3 (was mf; pitches, rhythm and the ff entry unchanged); bass clarinet solo p<mp>p at 31–33.
- v220: bassoons and harp under the horn solo at 9 and 11 no longer double the horn's A♭3; viola pizz. pp<p>pp at 41–44.
- v221: bassoon 2 holds the A♭ pedal through bar 33 (the common-tone diminished seventh, spelled with C♭ as the minor-third notation after a minor movement, A&S PDF 554).
- Checked at cycle 220: movement I v231 ending, scherzo v211 opening, finale v212 quotation 211–218 all still match.
- v222: viola pizz. triplets under the cor anglais at 43–44. v223: cellos C3 at 43 b4.
- v224 (ENDING): the violas stay divided to the end; the upper half holds A♭3 from 87 instead of falling to E♭3 at 89 (removes parallel fifths A♭3–E♭3 over D♭3–A♭2 at 88→89). Last chord pitch classes, top C5 and bass A♭ unchanged; scherzo told.
- v225: Tbn 2 A♭3 at 62 b3. v226: parts layout (boxed letters). v227: Cl 2 enters from niente at 89. v228: violas divided at 80 b2–81 b2 (lower half with Hn 3). v229: Vln I/II crescendo shape at 76; MIDI volume table for C.a., trombones, tuba, harp; MIDI fade across bar 91. v230: Cb mf at 28. v231: MIDI-only lower level for muted Hn 3·4 at 87–90.
- v233: cellos anticipate B♭2 on the last eighth of 64 (removes Cb/Vc fifths into 65; German sixth kept on the beat). v234: no change. v235: Ob 2 F♭5 at 80 b3–81 b1 (woodwinds complete the iiø7 and V♭9). v236: score and parts text placement only. v237: bass clarinet part alternative note at 8. v238: bass rises D♭–E♭–F♭ at 21 into the French sixth (voice exchange with the melody). v240: double basses pizz. quarters at 41 and 43.
- Checked at cycle 230: movement I v241 ending, scherzo v221 opening, finale v218 quotation 211–220 all still match.
- v241: Tbn 1 articulation at 63 (above); MIDI balance only for Cl 1 at 85–88, C.a. at 47–53, Cb at 83–86. Checked at cycle 240: movement I v251 ending (harp B pedal on B♭ needs only D and E changed for our bar 1), scherzo v230 opening, finale quotation all still match. v242: harp softer at 53–56. v245: harp mp at 77; MIDI balance for harp and timpani. v246: Vln I "(sul D)" over the tied C5 at 1–4 (dashed line, matches movement I v252); cellos stay in bass clef at 44–47; stem fixes. v247: violins' bowing at 78–79. v248: Cl 2 and harp doublings at 71–75. v249: crescendo into the ff at 79. v250: double basses in unison at 23–28. v253: voice-leading fixes in Bsn 2 at 11 and Cl 2 at 75. v255: clarinets in thirds at 58–59; double basses "4 soli" from 87 to the end (the scherzo marks its basses "tutti pizz." at its bar 3 since its v244). v256: parts stems and beams. v257: Vln I plays the closing C5 at 89–92 "sul D" (same string as bar 1; no pitch or rhythm change). v258: cello bass C2 at 55; viola rest at 26 b3. v259: violin bowings at 15–28 and 76. v243: no change; note: the symphony's major-third key cycle (C–A♭–E–C) shows inside this movement as F♭ resolving to E♭ six times (bars 5, 21, 62–65, 78, 80, 88), which is why the F♭/E–E♭ thread is protected.
Apart from v224's inner voice, none of these touches the opening's carried-over chord, the ending, the exported themes' notes or the quotations.

## Themes exported (what the scherzo and finale may quote)

**Theme A** (first statement 6 beat 3–14, Horn 1 solo, p, "dolce espr.", concert pitch):
- Phrase 1: `es8 f8 | aes4. c'8 es'4~ | es'4 d'4 des'4 | c'4. bes8 aes4 | g2` = E♭3 F3 | A♭3 C4 E♭4~ | E♭4 D4 D♭4 | C4 B♭3 A♭3 | G3. Rhythm: quaver quaver | dotted crotchet, quaver, crotchet tied | crotchet ×3 | dotted crotchet, quaver, crotchet | minim.
- Phrase 2: `es8 f8 | aes4. c'8 f'4~ | f'4 bes'4 aes'4 | g'4 es'8 des'8 c'8 bes8 | aes2.` (top note B♭4 at 12).
- A rising A♭ arpeggio to a held E♭, then the motto's tail E♭–D–D♭–C (5̂–♯4̂–4̂–3̂). It does not open with a rising sixth.
- Other statements: Vln I and Vln II in unison, an octave higher (A♭4 …), pickup at 22, 23–30, with the cello counter-melody (cellos E♭3–A♭3–G3 | F3 G3 | A♭3 C4 | B♭3 G3 …); Vln I two octaves higher (A♭5 …) and Vln II one octave higher, pickup at 70, 71–78, with the same counter-melody in the cellos (71–82), joined by Horn 2 and Bassoon 1 at 75 and by Horn 1 at 78 (beat 3). At 78 the violins replace the last note with a run C6–F6–G6–A♭6 into B♭6 at 79 (Vln I; Vln II and Fl 1 the same in their octaves).

**Theme B** (first statement 36 beat 3–44):
- Pickup C5 in the cor anglais (beat 3 of 36) to F5 on beat 1 of 37, where flute 1 enters, p, "dolce cantabile". Flute 1 alone 37–40: `f''2 ges''8 f''8 es''4 | des''4 c''8 des''8 es''2 | ges''4 \tuplet 3/2 { f''8 ges'' f'' } es''4 des''4 | c''4 des''8 c''8 bes'2`. Head: rising fourth C–F, then F5 (minim), G♭5–F5 (quavers), E♭5 (crotchet).
- Second phrase 41–44 led by the cor anglais, "solo, dolce cantabile": A♭3 D♭4 F4. G♭4 | A♭4 B♭4 A♭4 G♭4~ G♭4 F4 | E♭4. F4 D♭4 B♭3 | C4 (rising fourth A♭–D♭). Flute 1 above it in tenths and sixths. Bar 42 is a diatonic turn, not the motto's tail.
- Other statements: the head in B♭ minor, oboe 1 with Bassoon 1 and cellos an octave lower, pickup A♭4 at 44 beat 4, D♭5 E♭5 D♭5 C5 | B♭4 A4 B♭4 D♭5 | C♯5 (45–47); Vln I and Vln II in unison, pickup C5 at 52 beat 4, 53–56; second phrase in octaves 57–60 (Vln I A♭5–D♭6–F6 …, A♭6 at 58) with flute 1 at the top and oboe 1 an octave lower.

**Other material.**
- Horn 3's plagal neighbour C4–D♭4–C4 over iv6/4 at 3–6, answered by the coda's F–F♭–E♭ line (87–89).
- Horn 1 and Clarinet 1 counter-melody at 53 (beat 4)–56: A♭3 B♭3 | D♭4. F4 B♭4~ | B♭4 G♭4 | C4 D♭4, built on theme A's head (since v202 the B♭4 is tied into 55 and G♭4 comes on beat 3).
- Timpani answer E♭3–C3–A♭2 at 84–85 (theme A's arpeggio falling).
- Harp harmonics A♭–C–E♭ at 83.

## Themes quoted from movement I (checked against coherence/themes-mvt1.md)

| Idea (movement I) | Bars in II | Instrument | Notes in II |
|---|---|---|---|
| Last chord C–E–G–C, Vln I's C5 (end of mvtOneMottoViolins) | 1 | Vln I C5, Vln II G4, Vla E4, Vc C3, Hn 3 C4 | Tied over (\repeatTie), ppp; see Opening. |
| Motto tail E♭–D–D♭–C (mvtOneMottoTail) | 8 | Horn 1 | E♭4 (tied from 7) D4 D♭4 C4, in theme A |
| | 24 | Vln I + II | E♭5 D5 D♭5 C5, in theme A |
| | 32–34 | bass clarinet, "solo, espr." | Pickup E♭2 F2 A♭2 C3 at 31, then E♭3 (32, tied) D3 D♭3 (33) C3 B♭2 (34): movement I's pitch and instrument (its bars 2–3). Cor anglais a sixth above (C4 | C4 C♭4 B♭3 | A♭3). |
| | 67–69 | Horn 1 alone, "solo", "dolce" | E♭4 (67, p <) D4 D♭4 C4 (68, mp >) B♭3 (69–70) over the E♭ pedal; Bassoon 1 a third below at 68. |
| | 72 | Vln I, Vln II | E♭6 D6 D♭6 C6 (Vln I), E♭5 D5 D♭5 C5 (Vln II), in theme A |
| | 85–89 | Clarinet 1 | E♭5 D5 D♭5 (87–88) C5 (89–90), the movement's last tail |
| Second-theme head, minor form with pickup (mvtOneThemeSBminor model; mvtOneThemeSAflat) | 47 (beat 4)–50, continuing to 53 | cor anglais, "solo, espr.", p | F♯ minor: C♯4 \| A4 (dotted minim tied to a quaver) G♯4 (quaver) \| F♯4 (crotchet) D5 (minim) C♯5 (crotchet) \| C♯5 B4 A4, then A♭4 G♭4 \| F4 G♭4 \| F4 (51–53). Rhythm `4 \| 2.~ 8 8 \| 4 2 4`, the same as movement I; intervals the same as the C-minor model `g4 \| es'2.~ es'8 d'8 \| c'4 aes'2 g'4`. Heard once. |
| First-theme head (mvtOneThemePHead) | 63–64 | Trombone 1 alone, ff, "marcato" | A minor: `r8 e8 c'4. b8 bes8 a8 \| a4 gis8 a8 f4. e8` = E3 C4 B3 B♭3 A3 \| A3 G♯3 A3 F3 E3, p at the end (mf before v219). Same rhythm and intervals as movement I's G–E♭–D–D♭–C \| C–B–C–A♭–G, transposed. Bass trombone, cellos and double basses hold A (sf >) under it. Heard once. |
| Stop chord B–D–F–A♭ (mvtOneStopChord) | 33, beat 2 | B.cl. D3, Bsn 1 F3, C.a. C♭4, Cbsn A♭1 | All four pitch classes, spelled D–F–A♭–C♭, over the A♭ pedal, pp; not resolved to C. |
| Horn call E♭–C–B (mvtOneHornCall) | none | | Not quoted in movement II. |
| Timpani pulse `c4 r8 g,8 c4 r4` | none | | Not used (kept for the finale). |

themes-mvt1.md also lists the stop chord at II bar 64. Confirmed at cycle 250 (v250, MIDI checked): bar 64 beat 3 holds the complete chord, D2 (Vc, Cb, B.tbn), F3 (Tbn 1), G♯3 (violas), B3 (Vln II), with D in the bass as at movement I bar 138. In this movement its B (C♭) always falls a semitone (33, 64→65); the rise B→C is left to the finale. Bars 61–65 follow the ♭VI→♭II→V7 route (A&S PDF 593): the quotation's A minor is A♭'s ♭II, so it stays in A minor. Movement II is ♭VI of C at symphony level; its last A♭ chord stays plain (no added seventh or sixth) so the finale's opening German sixth on A♭ resolves it.

## Timpani tunings

| Bars | Tuning, change or use |
|---|---|
| 1 | Label "Timp. in G, A♭, C, E♭ (as in movement I)", "soft sticks". |
| 2–3 | A♭2 roll ppp. |
| 5 | "muta G in D♭ (A♭, C, D♭, E♭)" (G → D♭; wording since v215). From here: A♭2, C3, D♭3, E♭3. |
| 50 | "medium sticks". |
| 52–53 | A♭2 roll pp < into a single D♭3 stroke p at 53. |
| 60–62 | A♭2 roll p < f (60), D♭3 roll f (61), D♭3 at 62, "damp". |
| 67–70 | E♭3 roll ppp, "near the rim". |
| 79–81 | "ord."; D♭3 roll f (79–80), E♭3 roll with diminuendo (81). |
| 84–85 | E♭3, C3, A♭2 single strokes, pp. Last sound. |
| 92 | Part only: "muta A♭ in E, C in G, D♭ in B, E♭ in E (for the Scherzo, during the pause)". |

The timpani rest in 31–36 and in the B section until 52. Only A♭2, C3, D♭3 and E♭3 are struck; G2 is never played.

## Scoring facts other movements rely on

- **Trumpets tacet.** No trumpet staves in the score; the front page says "Trumpets tacet"; the trumpet parts get a "Tacet" page. The bSec trumpet variables are all rests.
- **No percussion except timpani.** No tam-tam, cymbal or other percussion; there is no percussion staff in score.ly and the perc part has no notes.
- **Horns 1·2 a2 at 61–62** (since v195), with Horns 3·4 a2: every horn part of the climax chord is a pair.
- **Trombones and tuba only at 60–64.** Tbn 2, bass trombone and tuba enter pp < at 60; held chords f at 61–62 (mf before v219; Tbn 2 A♭3 at 62 b3 since v225); Tbn 1 plays only the quotation at 63–64; bass trombone A2 sf > p at 63 and A2 D2 E2 at 64. No trombone chorale.
- **Horns.** Horn 1 solo melody at 7–14 (theme A) and 67–70 (motto tail). Horns 3·4 a2 at 61–62 (A♭4, B♭4–C♭5). Horn 3's F4–F♭4–E♭4 at 79–81 (open), echoed con sord. at 87–90 by Horn 4 F3–F♭3–E♭3 with the cor anglais. The coda's muted Horns 3·4 (87–90) are the only muted brass in the movement.
- **Highest violin note: B♭6**, Vln I at 76 (beat 2) and 79 (ff, tied into 80, then A♭6). Vln I also reaches A6 at 63 (div., tremolo E6–A6) and A♭6 at 58 and 62. No violin note is higher than B♭6; the violins never reach B6 or C7. Vln II's highest note is C6 (63–64). Flute 1 reaches A♭6 (58, 61–62), A6 (63) and B♭6 (79–80).
- **Strings.** Muted at 15–30 (Vln II, violas, cellos con sord. from 15; the solo violin plays senza sord. at 17–22 and the other first violins join muted at 24; double basses senza sord.). "via sord." at 31. String tremolo only at 61–64 (violas from 61, Vln I, Vln II and cellos at 63–64). Strings are silent at 4–14 and 31–36 (Vln II, violas and cellos return at 15, the solo violin at 17, the double basses at 21).
- **Harp.** Accompaniment only: arpeggiated chords under Horn 1 at 7–14 (left hand 8va bassa); octave bass with the pizzicato double basses at 37–44; triplet figure at 53–56; chords at 71–78 and 82; harmonics at 83. No melodic harp line. Silent 84–92.
- **Woodwind choir alone** at 31–36 (bass clarinet solo, cor anglais, bassoons, contrabassoon).
- **ff peaks**: 61–62 and 79–80. There is no fff in the movement.
- **F♭ to E♭.** Every F♭ resolves to E♭ in its own voice except the viola's F♭4 at 78, which resolves through the bass (F♭2–E♭2).
- **Not used in movement II:** C major as a key after bar 1, the trumpets' B→C, the horn call, the timpani pulse, a tuba melody, a high horn unison, a full low-brass unison bass, any cymbal.

## What the scherzo relies on (from coherence/scherzo.md; checked against scherzo v191 at cycle 190 and v201 at cycle 200; join with scherzo v211 confirmed by the scherzo thread 2026-10-19 (its cycle 210))

- **The last A♭, taken as G♯4 by the scherzo's Horn 1.** v181: Vln II holds A♭4 at 89–92, pp to ppp, under a fermata, with Vln I C5 above. Confirmed.
- **Timpani E, G, B, E.** v181: the part-only muta at 92 retunes A♭→E, C→G, D♭→B, E♭→E, which gives E2 G2 B2 E3. Confirmed. Note that the text is in the timpani part only, not in the full score.
- **Horns 3·4 muted at the end.** v181: Horns 3·4 play con sord. at 87–90, rest at 91–92, and have "via sord." at 91. So they stop playing muted, and are told to remove mutes before the movement ends. The scherzo's "senza sord." at its bar 73 is still correct and does no harm. scherzo.md's "Open requests" line already gives "via sord." at 91, which matches v181.
- The last chord (A♭1 A♭2 E♭3 A♭3 E♭4 A♭4 C5; violas' A♭3 since v224) contains A♭ = G♯ (3̂ of E) and E♭ = D♯ (7̂ of E) as common tones with E major.

## What the finale relies on (finale v33 message 2026-10-13 00:42 UTC; checked against finale v35 at cycle 190 and v43 at cycle 200)

- The finale quotes theme B's second phrase (cor anglais, II 41–44) at its bars 211–218 (coherence/finale.md).

- The coda's closing motto tail E♭–D–D♭–C (5̂–♯4̂–4̂–3̂, Cl 1 85–89) over the plagal close with mixture (IV6 – iv – I, 87–89). The scherzo answers it with B–A♯–A–G♯ in E (Hn 1 357–360, scherzo numbering since v24) and the finale with G–F♯–F–E in C (finale v33, 273–275), so the three closes fall by major thirds: A♭, E, C. All three share the ♮6–♭6–5 inner line; bar 86 in II is half-diminished (violas C♮), where III and IV use a full diminished seventh; kept. Movement II keeps this close; tell the finale and scherzo threads before changing it.

## Open requests to other movements

None.

## Differences between v181 and older notes (v181 is correct)

1. critics/c180-record-from-coordinator.md says "harp silent from 83". In v181 the harp plays at 83 (harmonics A♭–C–E♭ and a left-hand A♭1) and is silent from 84.
2. The aTwo.ily header comment and movement-2-plan.md give the main peak as F6 at 79. The notes are B♭6 in Vln I and Flute 1 at 79 (and B♭6 in Vln I at 76).
3. movement-2-plan.md's theme A and theme B notes are from v01 (for example `f''4 e''4 es''4` in theme A and theme B opening on A♭4). The v181 notes are the ones given above.
5. scherzo.md's opening section says movement II "ends with them [Hn 3·4] muted". They play muted until 90 and have "via sord." at 91.
