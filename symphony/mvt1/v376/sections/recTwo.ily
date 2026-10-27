% c149: 156 horns 2-4 re-enter p< (was mp<) after 13-24 bars' rest; Hn 1 continues from its p at 155 (Rimsky-Korsakov PDF 136: mp re-entries are colourless; as c143 at 113)
% c108: 156 horns and bassoons enter mp< under the violins' mf melody (strings lead the crescendo; brass basis weaker than the melody: Rimsky-Korsakov PDF 130, 133)
% RECAPITULATION, second theme in C major, bars 147–166 (20 bars; exposition 47–68 has 22). A = 147–155 (horn + violas + cellos, CA answers).
% Cycle 80: the violins' literal restatement of the head (old 156–159, = 47–50 / 56–59 in the exposition) is cut and withheld for movement III.
% The violins enter at 156 with the head's rhythm a step lower on ♭VII (pickup f''–d''' = the rising sixth), whose descent falls on the motto's
% own pitches D–D♭–C (spelled D♭: passing tone over B♭ → F minor); climax head at K (158), ♭VI fff at 160.

% Withheld in the recapitulation since cycle 80 (the violins' C-major head, unused here): reserved for movement III.
% recTwoMelodyA below is the withheld violin statement without its pickup (the slur opens in the pickup). The complete passage, with pickup, the chromatic counter (Cl1/Hn2) and bass, is in v99/sections/recTwo.ily (bars 156–159 of v99), kept for movement III.
recTwoMelodyA = { e''2.~ e''8 d''8 | c''4 a''2-- g''4) | f''4.(\< e''8 d''4 f''8 a''8 | c'''2 b''2) | }
recTwoMelodyB = {
  d'''2.~\< d'''8 des'''8) | c'''2( bes''4 aes''8 g''8) | g''4\ff\downbow e'''2.--~ | e'''4\< f'''4 g'''2 |
  c'''4\fff\downbow aes'''2--~ aes'''8 g'''8 | f'''2\downbow d'''4( b''8 c'''8) | a''2.~(\ff a''8 gis''8) | a''4.\>( g''8 f''4 a''8 c'''8) |
  d'''2\mp( c'''2~\> | c'''8 b''8 a''8 g''8 f''4 d''4) | c''2\p~ c''2\< |
}
recTwoCounter = {
  f'2\mp\< r8 f'8( g'8 a'8 | aes'2) f'2 | g'2\ff c''2 | b'2\< f'2 |
  es'4\fff c''4 r8 c''8( bes'8 aes'8 | aes'2) f'2 | e'2\ff\> r8 e'8( f'8 g'8 | f'2) c''2 |
  f'4\mp aes'8( g'8) d''2~ | d''2( b'4 f'4) | e'2 es'2\< |
}
recTwoMelody = { \recTwoMelodyB }
% c169: 158-161 the violas leave the tune (Hn 1-2 and Vc keep its lower octave) and repeat the chord in eighths, the inner pulse under the
% violins' tune in Brahms 3/i mm. 183-87 (Adler PDF 163-164, Ex. XV-14: violas and cellos in eighths, winds and brass hold the chords; PDF 181: figuration gives buoyancy)
recTwoSync = {
  % c227: 156-157 the viola arpeggio starts a third lower and peaks at B-flat4 / A-flat4 (was D5 in unison with Vln II's D5, then C5 above Vln II's
  % B-flat4, and 157 ran in octaves with the cello arpeggio): the background stays under the tune's lower octave and moves in sixths with the cello
  % (Adler adler1 PDF 135: keep background out of the melody's register when the colours are alike; PDF 136: coupling in thirds/sixths). Chords unchanged (c182).
  r8 bes8(\mp\< d'8 f'8 bes'4) r4 | r8 aes8( c'8 f'8 aes'4) r4 |
  <c' g'>8[\ff <c' g'> <c' g'> <c' g'>] <c' g'>[ <c' g'> <c' g'> <c' g'>] | <b f'>8[\< <b f'> <b f'> <b f'>] <b f'>[ <b f'> <b f'> <b f'>] |
  <c' es'>8[\fff <c' es'> <c' es'> <c' es'>] <c' es'>[ <c' es'> <c' es'> <c' es'>] | <d' f'>8[ <d' f'> <d' f'> <d' f'>] <b f'>[ <b f'> <b f'> <b f'>] | r4 e'4~\ff\> e'8 d'8( c'8 b8) |
  r4 c'4~ c'8 a8( c'8 f'8) | r4 f'4~\mp f'8 e'8( d'8 g8) | r4 g4~ g8 b8( d'8 b8) | % c326: div. on the E4/G4 - E-flat4/G4 thirds (non-div. they force E4 onto the G string in third position at mp; div. puts E4-E-flat4 on the D string in first position; Adler adler1 PDF 76, 88)
  <e' g'>2\mp^"div." <es' g'>2\< |
}
recTwoArp = {
  bes,8(\mp\< d bes4.) a8( aes8 g8) | f,8( c f aes c'2) | \clef tenor g4\ff\downbow e'2.--~ | e'4\< f'4 g'2 |
  c'4\fff\downbow aes'2--~ aes'8 g'8 | f'2\downbow d'4( b8 c'8) | \clef bass a,8(\ff\> e a c' e'2) | f,8( c f a c'2) |
  d,8(\mp aes, d f) g,2 | g,8(\> d f b f2) | c,8(\p g, c e es2\<) |
}

recTwoFluteOne = {
  R1*11 |
  % c186: flutes and Ob 1 breathe with the brass at the end of 159 (c156), Fl 1 again before its 162 phrase: four bars of fff in the third octave
  % plus 162-163 were one unbroken span of about 14 s (Rimsky-Korsakov PDF 37: wood-wind players must take breath; give them a little rest). Violins hold the tune.
  \partCombineUnisono g''4\ff( e'''2.--~ | e'''4\< f'''4 g'''2) \breathe | c'''4(\fff aes'''2--~ aes'''8 g'''8 |
  % c197 (closes c187's optional item): after 161 the single wind doubling of the tune moves from the upper octave (Fl 1 with Vln I, A5) to the lower
  % (Ob 1 with Vln II, A4), which stands among the ff brass E4-C5 (Hn 1-2, Tpt 1-2) at 162. Rimsky-Korsakov PDF 78 (of two octave parts only one doubled:
  % double the lower); Adler adler2 PDF 44 (two horns in unison equal one trumpet or trombone: the brass around A4 outweigh one violin section).
  f'''2 d'''4 b''8 c'''8) | \partCombineAutomatic R1*5 |
}
recTwoFluteTwo = {
  R1*11 |
  g''4\ff( e'''2.--~ | e'''4\< f'''4 g'''2) \breathe |
  c'''4(\fff aes'''2--~ aes'''8 g'''8 | f'''2 d'''4 b''8 c'''8) | R1*5 |
}
% c241: 158-161 the oboes exchange lines. Ob 1 takes the counterline in the upper octave, in unison with Cl 1 (G5-C6 | B5-F5 | E-flat5-C6 ... | A-flat5 G5 F5),
% and Ob 2 takes the tune's middle octave with Tpt 1 and Vln II (G4-E5 ... A-flat5), continuing with Vln II at 162-163 (c197's line, same notes).
% Before, the counterline stood Cl 1 (G5) over Ob 2 + Hn 3-4 (G4): a clarinet above an oboe in octaves, the inverted order Rimsky-Korsakov calls an
% unnatural resonance (rimsky-principles PDF 67), with one wind above two horns where he asks for three or four in forte (PDF 75: 1 Ob + 1 Cl over 1 Horn;
% 2 Fl + 2 Cl over 2 Horns). Now Ob 1 + Cl 1 sit over Hn 3-4, and the tune's middle octave is Vln II + Ob + Tpt, his most natural three-group unison (PDF 79).
recTwoOboeOne = {
  R1*11 | g''2\ff c'''2 | b''2\< f''2 | es''4\fff c'''4 r8 c'''8( bes''8 aes''8 | aes''2--) g''4 f''4 | R1*5 |
}
recTwoOboeTwo = {
  R1*11 | g'4\ff( e''2.--~ |
  e''4\< f''4 g''2) \breathe | c''4(\fff aes''2--~ aes''8 g''8 | f''2 d''4 b'8 c''8) \breathe | a'2.~(\ff a'8 gis'8) | a'4.\> r8\! r2 | R1*3 |  % c197: 162-163 with Vln II (was Fl 1 with Vln I)
  % c364: Ob 2 leaves after the A4 of 163 (was A4-G4-F4, ending on F4 in the oboe's lowest fifth inside the diminuendo); Vln II carries the line down alone (Adler adler1 PDF 270-271, Copland Ex. VIII-41)
}
recTwoCorAnglais = {
  r2 r8 g'8(\p a'8 b'8 | c''2) r2 | r2 r8 a'8( b'8 c''8 | d''2) r2 |
  r2 r8 bes'8( a'8 g'8 | a'2) r2 | c''1 | g'2 f'2 | e'2 r2 |
  R1*11 |
}
% c104: Cl 1 takes the counterline an octave higher at 158–162 (Ob 2 and Hn 3 keep it at pitch), so the octave under the
% tune's top doubling holds a chord tone at the climax (it was empty on every beat of 158–161).
% c172: 161 beat 4 Cl 1 F5 (was G5 held): A-flat-G-F-E keeps cycle 170's flat 6 to 5 and lets the V7's seventh resolve to E at 162; G5-E5 made
% parallel fifths with the cellos' C4-A2 into the deceptive cadence (Aldwell & Schachter PDF 202, Ex. 13-12; PDF 83)
recTwoClOne = { R1*5 | r2. f''4~(\mp | f''4 e''8 d''8 c''4 a'4) | R1*2 |
  % c170: 156 beat 4.5 B-flat4 (was A4): the A-natural sounded right after the cellos' A-flat and against the violins' D-flat, a split chromatic
  % succession (Aldwell & Schachter PDF 394, Ex. 23-12a); G-B-flat-D-flat now leads as one minor-mode colour into iv at 157 (PDF 391, 395)
  % c337: 156-157 an octave up (was F4-G4-B-flat4 | A-flat4-F4, written G4-C5, the throat register, on Hn 1's held F4 and inside the violas' arpeggios and
  % the four horns): the counter that becomes the climax's middleground at 158 is heard in the clear clarion between Vln II (D5) and Vln I (D6) and
  % steps F5-G5 into its own 158 statement with Ob 1 (was a ninth leap F4-G5). Adler adler2 PDF 184 (each fragment to an instrument that will be heard in the
  % texture; weak registers need help), PDF 177/181 (elements exposed separately before they are combined), PDF 176 (keep the colour that carries the element)
  f''2\mp\< r8 f''8( g''8 bes''8 | aes''2) f''2 |
  g''2\ff c'''2 | b''2\< f''2 |
  es''4\fff c'''4 r8 c'''8( bes''8 aes''8 | aes''2--) g''4 f''4 |
  % c187: 162 beats 4-4.5 F4 held into 163 (was f'8 g'8): the G-natural4 sounded against the tune's G-sharp on the same eighth (Vln II G-sharp4, Vln I and Fl 1 G-sharp5),
  % a simultaneous chromatic clash involving the top voice (Aldwell & Schachter PDF 420: keep chromatic conflicts away from the top voice; Rimsky-Korsakov PDF 81: no good
  % resonance from faulty part movement). The F anticipates 163's F major and makes the G-sharp beat a V-flat-9 colour (E in Vc/Hn 1/Tpt 2, B in Vla). An E4 ending made octaves with Bsn 1/Hn 4 E-F.
  e''2\ff\> r8 e'8( f'4~ | f'2) c''2 |
  % c252: 164 A-flat4-G4 (was A-flat4-B4): no melodic augmented second 6-sharp7 into V (Aldwell & Schachter PDF 268, 284 Ex. 17-26c); flat 6 goes to 5 as in Hn 3 (c152)
  f'4\mp aes'8( g'8) d''2~ | d''2( b'4 f'4) | e'2 es'2\< |
}
% c124: Cl 2 an octave higher at 158-161 (was E4-D4-C4-D4 inside the horns, doubling Tpt 3/Tbn 1): clarinets above the brass, not inside the horns (Rimsky-Korsakov PDF 108, 110-111)
recTwoClTwo = { R1*11 | e''1\ff | d''1\< | c''4\fff es''2 c''4 | d''1 | R1*5 | } % c154: E-flat5 on beats 2-3 of 160 (C5 back on beat 4, where Ob 2, Hn 3 and Cl 1 pass through B-flat): the woodwinds had no fifth of the A-flat chord (Adler PDF 160, 164)
recTwoBsnOne = {
  % c146: Bsn 1 takes 147-150 and Bsn 2 151-155, so neither sustains the pp bass for 18 s and Bsn 2 rests before its long 156-174 stretch (Adler PDF 188, 192)
  \partCombineSoloI c1\pp^\markup \bold "1." | f1 | d1 | g,1 | \partCombineAutomatic R1*5 |
  % c334: 158-161 Bsn 1 an octave above Bsn 2 (G3 G3 A-flat3 D4-G3, was unison G2 G2 A-flat2 D3-G2): the bassoons split in octaves on the bass as in every
  % f-fff chord of Rimsky-Korsakov's appendix (PDF 505 chords 1, 3, 4: Fag. in octaves; chords 2, 5 on tenor chord tones), and the fff A-flat chord at 160 gets
  % its root in the tenor (the octave E-flat3-C4 was empty: Tbn 2 E-flat3 alone between A-flat2 and C4; appendix chords 1-5, 9-12: no gap wider than a sixth above the bass fifth)
  % c314: Bsn 1 takes the upper note at 156, 162, 164 and 166 (was the lower: F2, E2, D2, C2 under Bsn 2's B-flat2, A2, D3, C3), so the pair keeps the
  % normal order of register on its shared staff (Rimsky-Korsakov PDF 90 rule 2; PDF 95: crossed parts give octaves against the natural order, here D2/D3 and C2/C3)
  bes,1\mp\< | \partCombineUnisono f,1 | \partCombineAutomatic g1\ff | g1\< \breathe | aes1\fff | d'2 g4 r4 | a,2.\ff\> \once \override Rest.staff-position = #2 r4 | \partCombineUnisono f,1 \breathe | \partCombineAutomatic d2\mp \partCombineUnisono g,2~ | g,1\> | \partCombineAutomatic c2.\p r4 |
}
% c170: 161 Ob 2, Cl 1 (8va) and Hn 3 take the counterline's A-flat to G on beat 3 (was A-flat-F): the borrowed flat 6 of the iiø7 reaches 5 over V7
% before A-natural (vi) at 162; Hn 3 had A-flat4-F4-A3, flat 6 replaced by natural 6 before 5 (Aldwell & Schachter PDF 388, 395; c152's rule at 164).
recTwoBsnTwo = {
  R1*4 |
  e1\pp | f1 | f1 | g1 |
  c2 r2 |
  f,1\mp\< | f,1 | g,1\ff |
  g,1\< \breathe | aes,1\fff | d2 g,2 | e,1\ff\> | % c314: Bsn 2 takes the lower note at 156, 162, 164, 166 (see Bsn 1); c135's rest override moves to Bsn 1 at 162
  f,1 \breathe | d,2\mp g,2~ | g,1\> | c,2.\p r4 |
  % c346: Bsn 2 breathes after 159 (with Fl 1-2, Ob 2, horns, trumpets, trombones, B.tbn) and after 163 (into the mp at 164; Bsn 1 in unison breathes too).
  % 156.1-166.3 was one unbroken ff-fff stretch on F2-A-flat2 of about 25 s (then C2 f-ff at 167-170 after one crotchet rest); now 8.1, 9.6 and 7.0 s.
  % Adler adler1 PDF 175 (limitations of the player in certain registers), 188 (rest after sustained passages; the Brahms dovetail), 230 (low reeds need much breath: periodic rests).
  % The bass goes on through both breaths in Cbsn/Cb (159-160) and Vc/Cb/harp (163-164).
}
recTwoCbsn = { R1*11 | g,,1\ff | g,,1\< | aes,,1\fff | d,2 g,,2 | R1*5 | }
recTwoHnOne = {
  e'2.~\< e'8 d'8\> | c'4\! a'2--\< g'4\!) | f'4.( e'8 d'4 f'8\< a'8 | c''2\> b'2\!) |
  % c186: 154 c'4 b4 d'4 f'4 (was c''4 b'4 d''4 f'4): the concert D5 was written A5, above the horn's tenth partial (written E5), the top of the
  % register Rimsky-Korsakov's Table C marks "very frequent" (PDF 43), entered mp after a one-bar rest; Hn 1 rests only at 153 and 163 between 147 and 170. The horn now doubles
  % the cellos for three notes and meets the violas on F4; the violas keep the line's upper octave.
  g4( e'2--\< d'4\!) | c'4.(\> b8 a2\!) | R1 | c'4(\mp\> b4 d'4 f'4) |
  e'2\p d'2 | f'1\< | f'2. r4 |
  \partCombineUnisono g4\ff e'2.--~ | \partCombineAutomatic e'4\< f'4 g'2 \breathe | c'4\fff aes'2--~ aes'8 g'8 | f'2 d'4( b8 c'8) | % c355: one 'a2' on beat 1 of 158 (the combiner put it on the E4, so the G3 read as Hn 1 alone; Gould PDF 61, 65; MOLA PDF 11 Ex. 6)
  e'1\ff\> | R1 | f'1\p | f'1 |
  e'2\mp es'2\< |
}
recTwoHnTwo = {
  R1*9 | d'2.~(\p\< d'8 des'8) | c'2. r4 | % c188: slur as Vln II's D-D-flat (Adler adler1 PDF 309)
  g4\ff e'2.--~ |
  e'4\< f'4 g'2 \breathe | c'4\fff aes'2--~ aes'8 g'8 | f'2 d'4( b8 c'8) | c'1\ff\> |
  c'1 | c'2\p r2 | R1 | c'2\mp~ c'2\< |
}
recTwoHnThree = {
  % c153: Hn 3's B3 (145-146) resolves to C4 at 147 (A&S PDF 220, 456)
  c'2 r2 | R1*8 | bes1\p\< | aes1 | \partCombineUnisono g'2\ff c''2 | \partCombineAutomatic % c255: 158 one 'a2' for the whole bar (Gould PDF 61, 65). c087: Hn 3 holds 157 (entered at 156; breathes at 160), so one horn bridges into K
  b'2\< f'2 | es'4\fff c''4 r8 c''8( bes'8 aes'8 | aes'2--) g'2 | \clef bass a1\ff\> |
  R1 | aes2\p( g2~ | g4 b2.) | c'1\mp | % c222: 166 C4 (was G3): the V7's leading tone B3 resolves to C (A&S PDF 76); no d5 B-F to P5 G-C with the cellos (PDF 83, Ex. 5-20b); the line B-C-C into 167 is conjunct (PDF 80)
  % c152: 164 A-flat3-G3 (was A-flat3-A3): once introduced, flat 6 goes to 5, not to natural 6 (Aldwell & Schachter PDF 388, 395)
}
% c124: Hn 4 rests from 164 beat 3 (its G3 sat a second under Hn 3's A3; the ninth now sounds against bassoons and low strings, Rimsky-Korsakov PDF 102-103)
% c174: Hn 4 doubles Hn 3's counterline 158-161 (was a G3/A-flat3 pedal already held by Tbn 2, B.tbn, tuba): at ff-fff one horn has half the
% strength of a trumpet or trombone, so a horn line against full brass needs two horns in unison (Adler adler2 PDF 15 and 44; Rimsky-Korsakov ch. I, "two horns are needed to one trumpet")
% c185: part-only label (c181): Hn 4 doubles Hn 3 at 158-161
recTwoHnFour = { R1*9 | f1\p\< | f2. \once \override Rest.staff-position = #-10 r4 | g'2\ff-\tag #'part ^\markup \bold "a2 with 3." c''2 | b'2\< f'2 | es'4\fff c''4 r8 c''8( bes'8 aes'8 | aes'2--) g2 | e1\ff\> | f1 | d2\p r2 | R1 | g1\mp | } % c234: 166 G3 (was C3, a doubling of the bass in Bsn 2/Vc): the four horns hold the whole chord G3-C4-C4-E4/E-flat4 without the bass (Rimsky-Korsakov PDF 100-101); G3 is held into 167
% c156: staggered breaths in the ff-fff brass block 158-162 (Adler PDF 292: brass need frequent breaths, more for loud playing; adler2 PDF 8: tuba).
% Sustained Gs (Hn 4, Tpt 2, Tbn 2, tuba) breathe after 158; the tune (Hn 1-2, Tpt 1) and Tpt 3, Tbn 1, B.tbn after 159; tuba again after 160. No note or dynamic changed.
recTwoTptOne = {
  R1*11 | g'4\ff e''2.--~ | e''4\< f''4 g''2 \breathe | c''4\fff aes''2--~ aes''8 g''8 |
  f''2 d''4( b'8 c''8) | c''2\ff\>~ c''2\mp | R1*4 |
}
recTwoTptTwo = {
  R1*11 | \once \override NoteColumn.force-hshift = #1.7 g'1\ff \once \override BreathingSign.direction = #DOWN \breathe | g'1\< | aes'1\fff |
  f'2 f'2 | e'2\ff\>~ e'2\mp | R1*4 |
}
% c244: heavy brass harmony (Tpt 3, Tbn 1-2, B.tbn, tuba) stays ff through 158-161 (no crescendo to fff) under the fff tune and countermelody at 160, as the score already grades it at 27-32, 97-102, 131, 140 and 167 (Rimsky-Korsakov appendix PDF 505 chords 2-3, Ex. 206 PDF 369, Ex. 209 PDF 375; PDF 41 horns half as strong as trombones at forte)
recTwoTptThree = {
  % c154: E-flat4 at 160 (was C4, a unison with Tbn 1 through 158-162): the fff A-flat chord had its fifth only in Tbn 2's E-flat3 (Adler PDF 164, 165)
  % c169: 161 D4 (was B3, at pitch with Tbn 1): Tpt 3 falls E-flat4-D4-C4 through 160-162 (Adler PDF 165, 161)
  R1*11 | c'1\ff | b1 \breathe | es'1\ff |
  d'1 | c'2\>~ c'2\mp | R1*4 |
}
% c169: 159 D4 (was B3, at pitch with Tpt 3): the V7 gets its fifth in the brass and the leading tone is no longer doubled at pitch (Adler PDF 164-165; completes c154)
% c374: 159 D4 for beats 1-2, B3 for beats 3-4 (resolving to C4 at 160): when Ob 1, Cl 1 and Hn 3-4 leave B for F on beat 3, the V7's leading tone had only Tpt 3's low B3 in the brass at ff< into fff (Adler PDF 15: low trumpet weaker; Ex. XI-1: third present in loud chords). The trumpet B-C stays reserved for the finale.
recTwoTbnOne = {
  R1*11 | c'1\ff | d'2 b2 \breathe | c'1\ff |
  b1 | c'2\>~ c'2\mp | R1*4 |
}
recTwoTbnTwo = {
  R1*11 | g1\ff \once \override BreathingSign.direction = #DOWN \breathe | g1 | es1\ff |
  f2 f2 | e2\>~ e2\mp | R1*4 |
}
recTwoBassTbn = {
  R1*11 | g,1\ff | g,1 \breathe | aes,1\ff |
  d2 g,2 | a,2\>~ a,2\mp | R1*4 |
}
recTwoTuba = {
  R1*11 | g,,1\ff \breathe | g,,1 | aes,,1\ff \breathe |
  d,2 g,,2 | a,,2\>~ a,,2\mp | R1*4 |
}
recTwoTimp = { R1*11 | g,1:32\ff | g,1:32\< | aes,1:32\fff | g,4:32\>~ g,4\! r2 | R1*4 | r2 c2:32\p\< | }
% c250: no clashed cymbals in movement I. The roll swells into one soft-stick stroke on the suspended cymbal at 160; the clashed pair is first heard
% at the finale's C-major arrival (IV 223), the symphony's reward sound (Casanelles, hyper-orchestra PDF 227: Man of Steel holds its drum ensemble back
% until the last part of the climax, after only a modest earlier appearance; PDF 235, 237-238: Annihilation keeps its synthetic colour for the one reveal).
% c366: part only, the beater change is announced in the rests before the entry (Adler part 2 PDF 70 Ex. XII-22 'take brushes', 'take bow'; PDF 59 q. 1)
recTwoPerc = \drummode { R1*9 | \tag #'part { R1*2^\markup \small \italic "take soft sticks" } \tag #'score { R1*2 } | R1 | cymr1:32\pp\<^\markup { "Susp. cym." \italic "soft sticks" } | cymr1->\fff~ | cymr1~ | cymr1~\>_\markup \small \italic "damp gradually" | cymr1\p | R1^\markup \small \italic "damp" | R1*2 | }  % c276: written length instead of open l.v.; rings through 160-163 (the largamente and the ff> of 162-163), damped at 164 where the strings reach mp (Adler part 2 PDF 70 Ex. XII-22, PDF 71, PDF 80; as the tam-tam at 122-127)
recTwoHarpR = {
  % 156–166: one rolled chord per harmony on beat 1 in the upper register (the exposition had broken eighths);
  % beats 3–4 are left to the viola fills. No chord on beat 3 of 168 (4–3 suspension in the tune).
  R1*9 | <f'' bes'' f'''>2\arpeggio r2 | <aes'' c''' f'''>2\arpeggio r2 | R1*4 |
  <a'' c''' e'''>2\arpeggio r2 | <a'' c''' f'''>2\arpeggio r2^\markup \small \italic "étouffez" | <aes'' d''' f'''>2\arpeggio r2^\markup \small \italic "étouffez (m.d.)" | <g'' d''' f'''>2\arpeggio r2 |
  <c'' g'' c'''>4\arpeggio r4 r2 |
}
recTwoHarpL = {
  R1*8 | R1_\pedBflatAflat |
  <bes,, bes,>2\mf r2 | <f,, f,>2\f r2 | R1*3 | R1_\markup \small "A♮" |  % c246: no B-natural (no B is played 156-182; movement II needs B-flat); A-natural marked late, at 161, after the A-flat5 of 157 has decayed (Adler adler1 PDF 112-113)
  <a,, a,>2\f r2 | <f,, f,>2 r2_\markup \small "A♭" | <d, d>2\mp <g,, g,>2 | <g,, g,>2 r2 |
  <c, c>4\p r4 r2 |
}
% c107: Vln I rests 147-155 (the sul tasto halo is taken by Vln II div.), so the first violins' high colour is first heard with the tune at 155-156
% (Adler PDF 135: background in the palest register; the higher violin colour saved for the foreground statement).
recTwoVlnOne = {
  R1*8 |
  r2 r4 f''4\mf( | \recTwoMelody | % c358: the pickup F5 is slurred into the rising sixth to D6, as every other S pickup (46.4, 55.4, 97.4, 146.4) (Casanelles PDF 151, 155)
}
% cycle 82: 148 IV–IV+ (C–C#–D in Vln II) into ii at 149; 155 beats 3–4 E→D in Vla/Vc/Hn1 under the violins' f pickup.
% c194: 150 <f'' a''> (was <d'' f''>): D5 out of the halo, so the cor anglais's held D5 is not a unison with the tremolo (c190 optional item;
% Casanelles PDF 277-278: an instrument added at a section's pitch is not heard as a note of its own). A held over from 149; D stays in the C.a.
% c257: 152 beats 3-4 <a'' c'''> (was <f'' a''> all bar): the halo held F5, the note on which the violas and Cl 1 reach the phrase's peak at 152.4, so the peak arrived on a pitch
% the background already sounded at the unison; the halo now moves to A5/C6 (same IV chord) before it (Adler adler2 PDF 217: background and tune kept apart; PDF 229; as c194 at 150)
% c312: 151 Vln II lower div. C5 (was G5): V6/5 of IV had no root (E-G-B-flat over the pizz. E); C5 gives the chord its root, as Va A-flat3 does at 51 (c272; Aldwell & Schachter PDF 76: only the fifth may be omitted). B-flat5-A5 still resolves the seventh
recTwoVlnTwo = {
  <e'' g''>1:32\pp^\markup { "div." \italic "sul tasto" } | <c'' a''>2:32 <cis'' a''>2:32 | <d'' a''>1:32 | <f'' a''>1:32 | <c'' bes''>1:32 | <f'' a''>2:32 <a'' c'''>2:32 | <d'' a''>1:32 | <c'' e''>4:32 <b' d''>2.:32 |
  <c'' e''>2:32 r4 f'4\mf(^\markup { "unis." \italic "ord." } |
  % c229: 158-161 Vln II an octave below Vln I (was in unison with it at E6-A-flat6): the high climax line gets a string octave under it, as at 20, 27-32,
  % 82, 97-102 and 122 (Rimsky-Korsakov PDF 58-59: violin melodies in the very high register are doubled in octaves; PDF 59 note to Ex. 24 and PDF 62
  % Note I: the octave below takes the expression and the top loses its stridency; Ex. 22, 23, 25; Brahms 2/i 118-123). 161 ends on C5, a third above 162's A4.
  d''2.~\< d''8 des''8) | c''2( bes'4 aes'8 g'8) | g'4\ff\downbow e''2.--~ | e''4\< f''4 g''2 |
  c''4\fff\downbow aes''2--~ aes''8 g''8 | f''2\downbow d''4( b'8 c''8) | a'2.~(\ff a'8 gis'8) | a'4.\>( g'8 f'4 a'8 c''8) |
  d''2\mp( c''2~\> | c''8 b'8 a'8 g'8 f'4 d'4) | c'2\p~ c'2\< |
}
recTwoVla = {
  % c325: 152.3 the three-beam group slants one whole space with the outer beam sitting on a line at both ends (was 0.18, an inner beam in mid-space; Gould PDF 32, 35 (a)); also Vc
  e'2.~\< e'8 d'8\> | c'4\! a'2--\< g'4\!) | f'4.( e'8 d'4 f'8\< a'8 | c''2\> b'2\!) |
  g'4( e''2--\< d''4\!) | c''4.(\> b'8 \once \override Beam.positions = #'(-1.824 . -0.824) a'8\! b'32 c''32 d''32 e''32 f''4~ | f''4 e''8 d''8 c''4 a'4) | c''4(\> b'4 d''4 f'4) |
  e'2\p d'2 | \recTwoSync |
}
recTwoVc = {
  % c315: in bass clef (was tenor 146-155): G2-F4, at most two ledger lines (Gould PDF 21)
  e2.~\< e8 d8\> | c4\! a2--\< g4\!) | f4.( e8 d4 f8\< a8 | c'2\> b2\!) |
  g4( e'2--\< d'4\!) | c'4.(\> b8 \once \override Beam.positions = #'(-1.824 . -0.824) a8\! b32 c'32 d'32 e'32 f'4~ | f'4 e'8 d'8 c'4 a4) | c'4(\> b4 d'4 f4) |
  e2\p d2 | \recTwoArp |
}
% c163: 153 bass F (ii6/5 over the held 4^ of 152, Vln II D5-A5; was D, root ii), so the cadence 151-155 rises E-F-F-G-C as 51-55 does (Aldwell & Schachter PDF 291-292, 302). Bsn 2 follows.
recTwoCb = {
  c,4\pp^"pizz." r4 r2 | f,4 r4 r2 | d,4 r4 r2 | g,,4 r4 g,,4 r4 |
  e,4 r4 r2 | f,4 r4 r2 | f,4 r4 r2 | g,4 r4 g,4 r4 |
  c,4 r4 r2 | bes,,1\mp\<^"arco" | f,,1 | g,,1\ff |
  g,,1\< | aes,,1\fff | d,2\downbow g,,2 | a,,1\ff\> |
  % c338: 166 bow change on the tied C2 (down, then up for the crescendo), so the f quavers of 167 start down-bow and the ff stop chord at 170 is down-bow
  % with the other strings (was: crescendo down-bow, 167 and 170 up-bow; Adler adler1 PDF 38 and Ex. II-20: down- and up-bow over the long note so that the following attack is solid)
  f,,1 | d,2\mp g,2~ | g,1\> | c,2\p~\downbow c,2\<\upbow |
}
