% CODA, bars 83-92 (3/4). c013: one harp/timpani exchange instead of two (85-88 of v13 cut; A&S PDF 448, 455: proportion of coda to reprise).
% c170: current state (replaces the v01 header for bars 91-104, which described a timpani motto tail and Vln I's D flat-C; both are gone).
% 83: harp harmonics A flat-C-E flat (theme A's head) over the ppp A flat pedal; 84-85: timpani answer E flat-C-A flat (head mirrored, not the tail).
% 85-89: clarinet 1 plays the movement's last motto tail E flat5-D5-D flat5-C5 (one statement); Vln I takes over C5 at 89 and ends on it.
% 87-89: IV6-iv-I with the top D flat5-C5 (Cl 1) and the mixture line F-F flat-E flat (Vla sul C, Hn 4 con sord., C.a.): natural 6 - flat 6 - 5,
% Chopin Op. 32/2 in A flat (A&S Unit 23, PDF 387-388, Ex. 23-2f; Points for Review 3, PDF 395); it answers bar 5's iv6/4 (Cl 2 E flat-F flat-E flat,
% Hn 3 C-D flat-C). The F flat at 78 (viola figuration) resolves through the bass (Bsn 2, Cb F flat-E flat), not in the viola: doubling the resolution
% would make octaves with the bass (c070, c127). Ends on C5 on top, the pitch movement I ended on and this movement began with.

codaHarpR = {
  << \new Voice \with { \remove "Note_performer" } { \voiceOne aes4.(\p-\flageolet_\markup \small \italic "R.H. étouffez"^\markup \line { \italic "dolce," \small \italic "harm., L.H. (sound 8va)" } c'8-\flageolet es'4-\flageolet) } \new Voice { \voiceTwo \hideNotes aes'4. c''8 es''4 \unHideNotes } >> | R2.*3 |  % c298: p dolce on the harmonics (was pp from 82 b3): harmonics sound much softer than plucked notes at the same marking (Adler part 1 PDF 116 rule 1), so p keeps the theme head at the pickup's pp level; the harp solo is marked one level over the strings (Sebesky PDF 217, Ex. 284) and, as every solo lead here, gets a character word (Sebesky PDF 18, Ex. 2A)  % c026: harmonics (Adler part 1 PDF 116: practical range C3-A5 written; accompany very lightly - strings ppp)
  % c406: R.H. damps at 83 b1 the strings it plucked at 82 b2-3 (A flat3, C4, E flat4, F4): undamped, their plucked fundamentals ring under the softer harmonics an octave above, and F4 rings as a sixth over the tonic (Adler part 1 PDF 116: harmonics are very soft and must be accompanied very lightly; PDF 117: sons etouffes, the hand damps the strings)
  R2.*4 |
  R2. | R2.\fermata |  % c168: fermata on the last bar in the harp part too (MOLA PDF 5, Ex. 4: tempo changes in every part, even in rests)  % c050: no harp chord at 91: a new timbre entering in the closing diminuendo (Rimsky-Korsakov PDF 127) that doubles held notes and repeats movement I's last scoring (harp ppp + timp roll under Vln I C5)
}
codaHarpL = {
  aes,,2. \ottava #0 | R2.*3 |  % c026: closes the 8 bassa line from 71
  R2.*4 |
  R2.*2 |  % c050: chord at 91 removed (see codaHarpR); c045 had moved its ppp below the LH
}
codaTimp = {
  % c345: the bar-92 retuning is printed in the score too, above the timpani staff, which is kept in the last system for it (Adler part 2 PDF 291 item 3: every detail for every instrument in the score; PDF 294: "muta in" above the player's staff), as the clarinets' muta at 92
  % c040: the timpani answer the harp's rising head A flat-C-E flat with its mirror E flat-C-A flat in the head's rhythm (4. 8 4), so the coda
  % states the motto's tail once, complete, in clarinet 1 (85-89); v40's E flat-D flat-C here was a second, incomplete tail one bar before it.
  R2.^\markup \small "soft sticks" | es4.\pp c8 aes,4~ | aes,2. | R2.^\markup \small \italic "damp" |  % c436: the last strokes (E flat, C, A flat) are damped at 86 b1, so their length is shown as at 53 and 62 (Adler part 2 PDF 80: show how long a note may ring) and the drums are still before the muta at 92  % c019: answer at 84-85, heard alone; Cl 1's tail E flat-D-D flat-C follows at 85-89, Vln I taking its C5 at 89 (no two statements of the tail at once; c380: comment corrected, was 'Vln I's tail')
  % c120: no roll at 89-92: movement I ends with a C timpani roll under Vln I's C5 (its 181-182); with the roll here movement II ended in the same
  % scoring a second time (c050 removed the harp for this reason). The timpani's last sound is now its melodic answer at 84-85, as Dvorak 9/ii Largo's
  % timpani stop before the last bars (corpus percussion.notesL.ily: df4 r r2 R1 R1*2). The close's harmony and top voice are unchanged.
  \tag #'score { \set Staff.keepAliveInterfaces = #'(rhythmic-grob-interface multi-measure-rest-interface) } R2.*2 | R2.*3 | R2.\fermata -\tag #'score -\tweak parent-alignment-X #RIGHT -\tweak self-alignment-X #RIGHT -\tweak extra-offset #'(5 . 0) ^\markup \small \italic \right-column { "muta A♭ in E, C in G, D♭ in B, E♭ in E" "(for the Scherzo, in the pause)" } -\tag #'part -\tweak self-alignment-X #RIGHT _\markup \small \italic \right-column { "muta A♭ in E, C in G, D♭ in B, E♭ in E" "(for the Scherzo, during the pause)" } |  % c200: right-aligned on the last bar; centred on it, the text ran past the right margin of the timpani part and lost "E" and "pause)" (MOLA PDF 8, Ex. 7: anchored markings in extracted parts)  % c150: part-only retuning note for the next movement (MOLA PDF 5: a change is marked at the end of the previous passage; Rimsky-Korsakov PDF 21, axiom II); c180: retuning for the scherzo (E2 G2 B2 E3), which now follows; was "muta D flat in G (for III)"
}
codaVla = {
  % c063: the violas enter at 84, after the harp's head in harmonics (sounding A flat4-C5-E flat5), so the harmonics sound over the low
  % A flat pedal alone and not over the violas' C4-E flat4 attacked on the same beat (Adler part 2 PDF 267: the orchestra is reduced drastically
  % when the soloist plays in the softest part of its range; PDF 269: a transparent background for an entrance; PDF 274: registral distance)
  <>\strMark "L" \markup \concat { \hspace #1 "a tempo" } R2. |  % c435: letter on the bar's first musical column, in line with the winds' L, not on the whole-bar rest at the system's left edge (Gould PDF 9, 13; MOLA PDF 4) r2 <c' es'>4~\ppp^\markup \italic "div., change bow at will" | <c' es'>2. |  % c124: violas enter on 84 b3 as the timpani land on A flat, so the answer E flat3-C3 is heard over the ppp pedal alone and is not doubled at the octave by a chord attacked with it (Adler part 2 PDF 156: a rest before a colour enters; PDF 158: no two instruments with identical parts)
  <c' f'>2.\< |  % c085: div. without parentheses (Adler part 1 PDF 30: without the word the chord is played as a double stop)
  % c020: unis. sul C an octave lower (F3-F flat3-E flat3 with horn 4, then alone): the E/F flat-E flat thread on the viola's C string
  % (cyclic-notes, critic 126; Adler part 1 PDF 86); clarinet 1 keeps the upper octave.
  % c194: 87-90 the violas stay divided and double both muted horns, lower half F3-F flat3-E flat3 sul C with horn 4, upper half A flat3 with horn 3,
  % joining the lower half on E flat3 at 90 b3 as the horns release (Rimsky-Korsakov PDF 113: strings and brass are seldom combined, the exception being
  % 'the splendid effect of horns doubled by divided violas or cellos'; PDF 107, 110: muted horns with the cor anglais). Was unis. F3-F flat3-E flat3, the whole
  % section on horn 4's note and none on horn 3's. Pitches of every chord and the last chord unchanged.
  % c199: both halves reach E flat3 at 89 b1, with the chord change (I), and hold it unis. to the end, as v189-v194 did from 89; the upper half's
  % A flat3-E flat3 at 90 b3 was the only new attack in 90-92 (rit., morendo): an attack transient added where the texture is meant to decay
  % (Casanelles PDF 275-276, 279; Fig. 6.1, PDF 272: the closing field is a static pedal). Horn 3's A flat3 stays doubled at 87-88, where the line moves.
  <f aes>2.\pp | <fes aes~>2. | <es aes>2.~-\tag #'score ^\markup \italic "change bow at will" -\tag #'part _\markup \italic "change bow at will" | <es aes>2.~ | <es aes>2.~\> | <es aes>2.\ppp\fermata |  % c223: upper half keeps A flat3 (common tone of iv-I) instead of falling to E flat3 with the cellos D flat3-A flat2: removes parallel fifths A flat/D flat - E flat/A flat at 88-89 (A&S PDF 366 sec. 27, PDF 367 Ex. 21-40, Review 12 PDF 369); no new attack in 89-92 (c199)  % c235: in the part "lower half sul C" (87) and "change bow at will" (89) go below the staff, so the "rit." at 89 sits on its own line instead of under bars 76-77 of the line above (c225 open item; Gould PDF 43; MOLA PDF 8, Ex. 7)
   % c200: two lines (as the c065 text at 22): on one line the c199 text widened bar 89 and pushed the viola part onto a second page, with a turn at 83 under the harp harmonics (c165: viola part one page; MOLA PDF 7; Adler part 2 PDF 299 item 5)
}
% c366: "lower half sul C" at 87 removed: F3, F flat3 and E flat3 lie below the viola's open G3, so they can only be played on the C string; a string name is a colour choice only where a note lies on two strings (Rimsky-Korsakov PDF 26-27, Table A PDF 29). Pitches and dynamics unchanged.
codaVc = {
  \set Staff.midiExpression = #0.75 aes,2.~\ppp^\markup \italic "4 soli, change bow at will" | aes,2.~ | aes,2.~ | aes,2.\< |  % c259: four cellos on the octave of the basses' A flat1 under the divided violas 84-86 (Rimsky-Korsakov PDF 88: under divided upper strings the non-divisi cellos and basses "will prove a trifle heavy ... reducing the number of players"); the basses are tied from 82, so the cellos thin first; tutti at 87 for the plagal bass, where the basses go to 4 soli (c254). MIDI CC11 0.75 as the basses (c240)
  % c080: D flat chord over F once, at 87 (IV6 of A flat = the Neapolitan sixth of C minor, movement I's F-bass N6 at 7, 21, 141, 173):
  % A&S PDF 494 (Unit 28 sec. 14): "the Neapolitan 6th of a minor key becomes IV6 in the major key a 3rd lower". The bass falls A flat-F
  % and reaches the root D flat at 88 (iv), so the cadence itself (D flat-A flat, D flat5-C5 on top) is unchanged; F (the bass of the N6,
  % A&S PDF 484: the best tone to double) is doubled, D flat5 (flat 2 of C) stays alone in the top voice (PDF 483).
  \set Staff.midiExpression = #1.0 f,2.\pp^\markup \italic "tutti" | \once \stemUp des2. | aes,2.~^\markup \italic "change bow at will" | aes,2.~ | aes,2.~\> | aes,2.\ppp\fermata |
}
% c240: MIDI only: the A flat1 is tied from 82 (p), so score.midi held velocity 57 through the ppp pedal 83-86, above the harp harmonics (53); CC11 0.75 until the new note at 87
codaCb = {
  \set Staff.midiExpression = #0.75 aes,,2.~\ppp^\markup \italic "change bow at will" | aes,,2.~ | aes,,2.~ | aes,,2.\< |
  \set Staff.midiExpression = #1.0 f,,2.\pp^\markup \italic "4 soli" | \once \stemUp des,2. | aes,,2.~^\markup \italic "change bow at will" | aes,,2.~ | aes,,2.~\> | aes,,2.\ppp\fermata |  % c085: 89-92 (about 20 s and a fermata under the rit.): bow-change instruction renewed in Vla, Vc, Cb after the separate bows at 87-88 (Adler part 1 PDF 38-39)
}
% (superseded by c030 below) c010: Vln I entered at 89: E flat5-D5 (89-90), then D flat5-C5 (91-93), so the last top line is the motto's tail E flat-D-D flat-C
% at movement I's pitch, one note per bar; it supplies the D natural the timpani (A flat, C, D flat, E flat) cannot play (A&S PDF 600-603).
% c030: the tail E flat-D-D flat-C (85-90) goes to clarinet 1; Vln I takes the C5 over from it at 89 and holds it to the end,
% so the movement still ends on Vln I's C5 (its first sound in bar 1), but its last tail is not the sound movement I ended with
% (Vln I alone, E flat5-D5-(C5)-D flat5-C5, ppp). Bowing keeps an up-bow entry and a down-bow ending (c016).
codaVlnOne = {
  R2.*6 | c''2.~\pp\upbow^\markup \italic "sul D" | c''2.~\downbow | c''2.~\upbow\> | c''2.\downbow\ppp\fermata |  % c256: the movement ends on the C5 it began with, on the same string: bar 1 holds it sul D (tied from movement I's last motto, sul D); without a mark the section takes it in first position on the A string, 'quite strong in first position', while the D string is 'warm and rather subdued ... mellows even more in its higher positions' (Adler part 1 PDF 75), the colour for a ppp morendo; PDF 73: a string is named only when the timbre needs it
}
codaVlnTwo = {
  R2.*4 |
  aes'2.\pp | aes'2. | aes'2.~^\markup \italic "change bow at will" | aes'2.~ | aes'2.~\> | aes'2.\ppp\fermata |
}
% c230: MIDI only: Staff.midiExpression 0.7 for the muted horns 87-90 (the global fade at 91 resets it to 1.0 after they stop), so the render plays the
% con sord. echo of horn 3's open F-F flat-E flat (79-81) farther away than the open statement, not as the same open horn at pp (Casanelles PDF 18, 32: a mockup
% aims at the dramatic effect of the recorded result, e.g. muted and unmuted string instruments combined; Rimsky-Korsakov PDF 44: muted brass give distance). No printed change.
% c030: horns 3-4 con sordino for their last two bars (the only muted brass in the symphony so far; Rimsky-Korsakov PDF 44:
% muted brass give an effect of distance, tender in piano; mute in during 82-86).
% c280: horn 3's A flat3 tied 88-89 as the upper violas it doubles (it was re-tongued at 89 under the slur while they hold); the re-attack at 88 stays, with the chord change, as in the violas and Vln II (Adler part 2 PDF 192: seams do not show)
codaHnThree = { R2.*4 | \set Staff.midiExpression = #0.7 \partCombineChords aes2.(\pp^\markup \italic "con sord." | aes2.--~ | aes2.~ | \once \override Staff.Hairpin.circled-tip = ##t aes2)\> r4\! \partCombineAutomatic | R2.^\markup \italic "via sord." | R2.\fermata | }  % c136: printed in the score as well as the parts (both horns untagged, as "mettere sord." at 82, so the combined rest prints it once): mute instructions in both parts and score, and the change out of the mute must be marked (Adler part 1 PDF 295, 308)
% c326: horn 3's A flat3 at 88 is re-tongued under the slur (score.midi re-strikes it); tenuto added, as clarinet 1's repeated D flat5 in the same bar (c126 convention: slur + tenuto = soft re-articulation; Sebesky PDF 23 item 1, PDF 24 item 11), so the part does not read as a tie
codaHnFour = { R2.*4 | f2.(\pp-\tag #'part ^\markup \italic "con sord." |  % c046: the mute instruction in horn 4's own part too (Adler part 1 PDF 295); the score prints horn 3's
 fes2. | es2.~ | \once \override Staff.Hairpin.circled-tip = ##t es2)\> r4\! | R2.^\markup \italic "via sord." | R2.\fermata | }
% c008: clarinets take the held A flat / E flat from the horns and die away (Rimsky-Korsakov PDF 130: clarinets for morendo; brass leave first).
% c020: clarinet 1 enters at 87 with the F4-F flat4-E flat4 line the violas leave; clarinet 2 takes A flat3.
% c030: clarinet 1 plays the last tail E flat5-D5-D flat5-C5 (85-90) and hands the C5 to Vln I at 89 (Rimsky-Korsakov PDF 130:
% clarinets decrease their tone to a breath); clarinet 2 takes the F4-F flat4-E flat4 line over the violas' sul C octave.
% c041: the last motto tail starts with the clarinet's niente attack (Adler part 1 PDF 195, Ex. VII-57): the E flat5 grows out of the
% ppp pedal without an articulated start; clarinet 2 rests at 85-86, so the shared staff has no second dynamic.
% c050: clarinet 1 fades as it hands C5 to Vln I (Rimsky-Korsakov PDF 125-126 transfer on a common note; PDF 127: removing a timbre belongs to the diminuendo); clarinet 2 shares the hairpin (shared staff)
codaClOne = { R2.*2 | \set Staff.midiMinimumVolume = #0.2 \set Staff.midiMaximumVolume = #0.9 \once \override Staff.Hairpin.circled-tip = ##t \after 2 \pp es''2.(-\tweak stencil ##f \ppp \<^\markup \italic "dolce" | d''2.) \breathe | \tweak Stem.direction #DOWN des''2.(\pp-\tag #'score ^\markup \bold "1." | << \tweak Stem.direction #DOWN des''2.-- { s2 \unset Staff.midiMinimumVolume \unset Staff.midiMaximumVolume s4-\tweak stencil ##f \pp } >> |  % c185: Cl 1 alone at 87-88, D flat5 above the middle line takes a down-stem as at 85-86 (Gould PDF 27); the combiner had put it in voice one because Cl 2 enters at 89
  c''2.~ | c''2)\> r4\! | R2. | \once \override MultiMeasureRestText.parent-alignment-X = #RIGHT \once \override MultiMeasureRestText.self-alignment-X = #RIGHT \once \override MultiMeasureRestText.extra-offset = #'(5 . 0) R2.\fermata ^\markup \small \italic \right-column { "muta in A" "(for the Scherzo)" } | }  % c265: the scherzo is the only movement with clarinets in A (its v251 asks for this text); clarinet 1 is free from 90 b3 and changes in the pause; printed once on the shared score staff, as the scherzo prints its "muta in B flat" (Gould PDF 51: one shared indication where parts share a staff; MOLA PDF 5: a change is marked at the end of the previous passage)  % c240: MIDI only, 85-88: the clarinet equalizer (0-0.7) rendered the last motto tail at velocity 22-29, under the ppp/pp pedal and chords (31-57); 0.2-0.9 renders it above them as printed; reset on 88 b3 with a hidden pp on a spacer (velocity is computed only at a dynamic event; one at 89 would clash with Cl 2's) so Vln I takes the C5 over (Sebesky PDF 240-241)  % c160: hidden ppp at the start of the niente hairpin: without a start dynamic score.midi attacked the last motto tail at 0.71 scaled (velocity 56), the loudest note in the coda, against the printed niente < pp (Sebesky PDF 240-241, 13-14)
codaClTwo = { R2.*6 | es'2.~-\tweak stencil ##f \ppp _\tweak circled-tip ##t \< | \after 2 \! es'2.~-\tag #'part \pp \> |  % c226: niente attack at 89 (was attacked pp in the part, no mark in the score): clarinet 2 enters on the E flat4 the cor anglais is still holding, so it starts from silence without articulation, the effect the clarinet does 'better than any other woodwind' (Adler part 1 PDF 211, Ex. VII-57: N < p > N); hidden ppp start for MIDI as clarinet 1 at 85 (c160); the hairpin ends where clarinet 1's diminuendo starts at 90
  es'2.~\>^\markup \italic "morendo" | es'2.\ppp\fermata \tag #'part { \textEndMark \markup \small \italic \right-column { "muta in A" "(for the Scherzo, in the pause)" } } | }  % c265: clarinet 2 plays to the last note, so it changes in the pause between movements; the scherzo's clarinets first enter at its bar 7 (after Hn 1's fermata at 2 and the horn call), part-only text as the timpani muta (c150, c200)
% c104: the cor anglais takes clarinet 2's F4-F flat4 at 87-88 beside the muted horns; clarinet 2 enters on E flat4 at 89 for the morendo. Muted horns 'resemble the oboe and Eng. horn in quality; the combination of these instruments produces a magnificent tone' (Rimsky-Korsakov PDF 107; PDF 110: stopped horns with oboe or cor anglais in one chord, p); the clarinet's throat F4-F flat4 is neither that pairing nor the 'deep notes in the clarinet' of PDF 107. Pitches unchanged.
% c150: the cor anglais resolves its own F flat4 to E flat4 at 89 and leaves with the muted horns at 90, so clarinet 2 enters on a note the cor anglais
% is still holding (Rimsky-Korsakov PDF 125-126: in a transferred phrase the last note of one part coincides with the first note of the next; PDF 126-127:
% a chromatic progression passing between groups stays regular) and the coda's F4-F flat4-E flat4 is complete in one colour, as horn 3's open F4-F flat4-E flat4
% at 79-81 (PDF 128: an echo in muted brass of the same phrase unmuted; the cor anglais has the muted horns' affinity, c104). Was R2.*4 | f'2. | fes'2. | R2.*3 | R2.\fermata
codaCorAnglais = { R2.*4 | f'2.(\pp^\markup \italic "dolce" | fes'2. | es'2.~ | \once \override Staff.Hairpin.circled-tip = ##t es'2)\> r4\! | R2. | R2.\fermata | }  % c125: fermata on the last bar's rest, as clarinets and horns 3-4 have it

% c168: the closing fermata (92) in every part that rests through the coda, as the strings, clarinets, cor anglais, horns 3-4 and timpani
% already have it (MOLA PDF 5 and Ex. 4, PDF 10: tempo changes must be shown in all parts, even during extended rests). In the score
% these staves are hidden in the last system, so the score is unchanged.
codaFluteOne = { R2.*9 | R2.\fermata | }
codaFluteTwo = { R2.*9 | R2.\fermata | }
codaOboeOne = { R2.*9 | R2.\fermata | }
codaOboeTwo = { R2.*9 | R2.\fermata | }
codaBassCl = { R2.*9 | R2.\fermata | }
codaBsnOne = { R2.*9 | R2.\fermata | }
codaBsnTwo = { R2.*9 | R2.\fermata | }
codaCbsn = { R2.*9 | R2.\fermata | }
codaHnOne = { R2.*9 | R2.\fermata | }
codaHnTwo = { R2.*9 | R2.\fermata | }
codaTbnOne = { R2.*9 | R2.\fermata | }
codaTbnTwo = { R2.*9 | R2.\fermata | }
codaBassTbn = { R2.*9 | R2.\fermata | }
codaTuba = { R2.*9 | R2.\fermata | }
