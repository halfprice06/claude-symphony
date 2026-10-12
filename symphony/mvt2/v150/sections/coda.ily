% CODA, bars 83-92 (3/4). c013: one harp/timpani exchange instead of two (85-88 of v13 cut; A&S PDF 448, 455: proportion of coda to reprise).
% (old header) CODA, bars 91-104 (3/4). Over a tonic pedal (violas, cellos, basses ppp) the harp plays the theme's rising head
% and the timpani answer with the motto's tail on their four drums (E flat-D flat-C, A flat): melodic moments for
% instruments movement I kept from melody. Close: plagal iv-I with D flat-C in the top voice (Vln I),
% ending on C5 on top, the pitch movement I ended on and this movement began with.

codaHarpR = {
  << \new Voice \with { \remove "Note_performer" } { \voiceOne aes4.(-\flageolet^\markup \small \italic "harm. (sound 8va)" c'8-\flageolet es'4-\flageolet) } \new Voice { \voiceTwo \hideNotes aes'4. c''8 es''4 \unHideNotes } >> | R2.*3 |  % c026: harmonics (Adler part 1 PDF 116: practical range C3-A5 written; accompany very lightly - strings ppp)
  R2.*4 |
  R2.*2 |  % c050: no harp chord at 91: a new timbre entering in the closing diminuendo (Rimsky-Korsakov PDF 127) that doubles held notes and repeats movement I's last scoring (harp ppp + timp roll under Vln I C5)
}
codaHarpL = {
  aes,,2. \ottava #0 | R2.*3 |  % c026: closes the 8 bassa line from 71
  R2.*4 |
  R2.*2 |  % c050: chord at 91 removed (see codaHarpR); c045 had moved its ppp below the LH
}
codaTimp = {
  % c040: the timpani answer the harp's rising head A flat-C-E flat with its mirror E flat-C-A flat in the head's rhythm (4. 8 4), so the coda
  % states the motto's tail once, complete, in clarinet 1 (85-89); v40's E flat-D flat-C here was a second, incomplete tail one bar before it.
  R2. | es4.\pp c8 aes,4~ | aes,2. | R2. |  % c019: answer at 84-85, heard alone; Vln I's tail E flat-D-D flat-C follows at 85 (no two statements of the tail at once)
  % c120: no roll at 89-92: movement I ends with a C timpani roll under Vln I's C5 (its 181-182); with the roll here movement II ended in the same
  % scoring a second time (c050 removed the harp for this reason). The timpani's last sound is now its melodic answer at 84-85, as Dvorak 9/ii Largo's
  % timpani stop before the last bars (corpus percussion.notesL.ily: df4 r r2 R1 R1*2). The close's harmony and top voice are unchanged.
  R2.*2 | R2.*3 | R2.\fermata |
}
codaVla = {
  % c063: the violas enter at 84, after the harp's head in harmonics (sounding A flat4-C5-E flat5), so the harmonics sound over the low
  % A flat pedal alone and not over the violas' C4-E flat4 attacked on the same beat (Adler part 2 PDF 267: the orchestra is reduced drastically
  % when the soloist plays in the softest part of its range; PDF 269: a transparent background for an entrance; PDF 274: registral distance)
  R2.\strMark "K" \markup \concat { \hspace #2 "a tempo" } | r2 <c' es'>4~\ppp^\markup \italic "div., change bow at will" | <c' es'>2. |  % c124: violas enter on 84 b3 as the timpani land on A flat, so the answer E flat3-C3 is heard over the ppp pedal alone and is not doubled at the octave by a chord attacked with it (Adler part 2 PDF 156: a rest before a colour enters; PDF 158: no two instruments with identical parts)
  <c' f'>2.\< |  % c085: div. without parentheses (Adler part 1 PDF 30: without the word the chord is played as a double stop)
  % c020: unis. sul C an octave lower (F3-F flat3-E flat3 with horn 4, then alone): the E/F flat-E flat thread on the viola's C string
  % (cyclic-notes, critic 126; Adler part 1 PDF 86); clarinet 1 keeps the upper octave.
  f2.\pp^\markup \italic "unis., sul C" | fes2. | es2.~^\markup \italic "change bow at will" | es2.~ | es2.~\> | es2.\ppp\fermata |
}
codaVc = {
  aes,2.~\ppp^\markup \italic "change bow at will" | aes,2.~ | aes,2.~ | aes,2.\< |
  % c080: D flat chord over F once, at 87 (IV6 of A flat = the Neapolitan sixth of C minor, movement I's F-bass N6 at 7, 21, 141, 173):
  % A&S PDF 494 (Unit 28 sec. 14): "the Neapolitan 6th of a minor key becomes IV6 in the major key a 3rd lower". The bass falls A flat-F
  % and reaches the root D flat at 88 (iv), so the cadence itself (D flat-A flat, D flat5-C5 on top) is unchanged; F (the bass of the N6,
  % A&S PDF 484: the best tone to double) is doubled, D flat5 (flat 2 of C) stays alone in the top voice (PDF 483).
  f,2.\pp | \once \stemUp des2. | aes,2.~^\markup \italic "change bow at will" | aes,2.~ | aes,2.~\> | aes,2.\ppp\fermata |
}
codaCb = {
  aes,,2.~\ppp^\markup \italic "change bow at will" | aes,,2.~ | aes,,2.~ | aes,,2.\< |
  f,,2.\pp | \once \stemUp des,2. | aes,,2.~^\markup \italic "change bow at will" | aes,,2.~ | aes,,2.~\> | aes,,2.\ppp\fermata |  % c085: 89-92 (about 20 s and a fermata under the rit.): bow-change instruction renewed in Vla, Vc, Cb after the separate bows at 87-88 (Adler part 1 PDF 38-39)
}
% c010: Vln I enters at 89: E flat5-D5 (89-90), then D flat5-C5 (91-93), so the last top line is the motto's tail E flat-D-D flat-C
% at movement I's pitch, one note per bar; it supplies the D natural the timpani (A flat, C, D flat, E flat) cannot play (A&S PDF 600-603).
% c030: the tail E flat-D-D flat-C (85-90) goes to clarinet 1; Vln I takes the C5 over from it at 89 and holds it to the end,
% so the movement still ends on Vln I's C5 (its first sound in bar 1), but its last tail is not the sound movement I ended with
% (Vln I alone, E flat5-D5-(C5)-D flat5-C5, ppp). Bowing keeps an up-bow entry and a down-bow ending (c016).
codaVlnOne = {
  R2.*6 | c''2.~\pp\upbow | c''2.~\downbow | c''2.~\upbow\> | c''2.\downbow\ppp\fermata |
}
codaVlnTwo = {
  R2.*4 |
  aes'2.\pp | aes'2. | aes'2.~^\markup \italic "change bow at will" | aes'2.~ | aes'2.~\> | aes'2.\ppp\fermata |
}
% c030: horns 3-4 con sordino for their last two bars (the only muted brass in the symphony so far; Rimsky-Korsakov PDF 44:
% muted brass give an effect of distance, tender in piano; mute in during 82-86).
codaHnThree = { R2.*4 | aes2.\pp^\markup \italic "con sord." | aes2. | aes2.~ | \once \override Staff.Hairpin.circled-tip = ##t aes2\> r4\! | R2.^\markup \italic "via sord." | R2.\fermata | }  % c136: printed in the score as well as the parts (both horns untagged, as "mettere sord." at 82, so the combined rest prints it once): mute instructions in both parts and score, and the change out of the mute must be marked (Adler part 1 PDF 295, 308)
codaHnFour = { R2.*4 | f2.\pp-\tag #'part ^\markup \italic "con sord." |  % c046: the mute instruction in horn 4's own part too (Adler part 1 PDF 295); the score prints horn 3's
 fes2. | es2.~ | \once \override Staff.Hairpin.circled-tip = ##t es2\> r4\! | R2.^\markup \italic "via sord." | R2.\fermata | }
% c008: clarinets take the held A flat / E flat from the horns and die away (Rimsky-Korsakov PDF 130: clarinets for morendo; brass leave first).
% c020: clarinet 1 enters at 87 with the F4-F flat4-E flat4 line the violas leave; clarinet 2 takes A flat3.
% c030: clarinet 1 plays the last tail E flat5-D5-D flat5-C5 (85-90) and hands the C5 to Vln I at 89 (Rimsky-Korsakov PDF 130:
% clarinets decrease their tone to a breath); clarinet 2 takes the F4-F flat4-E flat4 line over the violas' sul C octave.
% c041: the last motto tail starts with the clarinet's niente attack (Adler part 1 PDF 195, Ex. VII-57): the E flat5 grows out of the
% ppp pedal without an articulated start; clarinet 2 rests at 85-86, so the shared staff has no second dynamic.
% c050: clarinet 1 fades as it hands C5 to Vln I (Rimsky-Korsakov PDF 125-126 transfer on a common note; PDF 127: removing a timbre belongs to the diminuendo); clarinet 2 shares the hairpin (shared staff)
codaClOne = { R2.*2 | \once \override Staff.Hairpin.circled-tip = ##t \after 2 \pp es''2.(\<^\markup \italic "dolce" | d''2.) \breathe | des''2.(\pp | des''2.-- | c''2.~ | c''2)\> r4\! | R2. | R2.\fermata | }
codaClTwo = { R2.*6 | es'2.~-\tag #'part \pp | es'2~\> es'4~\! | es'2.~\>^\markup \italic "morendo" | es'2.\ppp\fermata | }
% c104: the cor anglais takes clarinet 2's F4-F flat4 at 87-88 beside the muted horns; clarinet 2 enters on E flat4 at 89 for the morendo. Muted horns 'resemble the oboe and Eng. horn in quality; the combination of these instruments produces a magnificent tone' (Rimsky-Korsakov PDF 107; PDF 110: stopped horns with oboe or cor anglais in one chord, p); the clarinet's throat F4-F flat4 is neither that pairing nor the 'deep notes in the clarinet' of PDF 107. Pitches unchanged.
codaCorAnglais = { R2.*4 | f'2.\pp^\markup \italic "dolce" | fes'2. | R2.*3 | R2.\fermata | }  % c125: fermata on the last bar's rest, as clarinets and horns 3-4 have it
