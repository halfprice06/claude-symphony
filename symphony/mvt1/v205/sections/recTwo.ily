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
  d'''2.~(\< d'''8 des'''8) | c'''2( bes''4 aes''8 g''8) | g''4\ff\downbow e'''2.~ | e'''4\< f'''4 g'''2 |
  c'''4\fff\downbow aes'''2~ aes'''8 g'''8 | f'''2 d'''4( b''8 c'''8) | a''2.~(\ff a''8 gis''8) | a''4.\>( g''8 f''4 a''8 c'''8) |
  d'''2\mp( c'''2\> | b''4 a''8 g''8 f''4 d''4) | c''2\p~ c''2\< |
}
recTwoCounter = {
  f'2\mp\< r8 f'8( g'8 a'8 | aes'2) f'2 | g'2\ff c''2 | b'2\< f'2 |
  es'4\fff c''4 r8 c''8( bes'8 aes'8 | aes'2) f'2 | e'2\ff\> r8 e'8( f'8 g'8 | f'2) c''2 |
  f'4\mp aes'8( b'8) d''2~ | d''2( b'4 f'4) | e'2 es'2\< |
}
recTwoMelody = { \recTwoMelodyB }
% c169: 158-161 the violas leave the tune (Hn 1-2 and Vc keep its lower octave) and repeat the chord in eighths, the inner pulse under the
% violins' tune in Brahms 3/i mm. 183-87 (Adler PDF 163-164, Ex. XV-14: violas and cellos in eighths, winds and brass hold the chords; PDF 181: figuration gives buoyancy)
recTwoSync = {
  r8 d'8(\mp\< f'8 bes'8 d''4) r4 | r8 c'8( f'8 aes'8 c''4) r4 |
  <c' g'>8[\ff <c' g'> <c' g'> <c' g'>] <c' g'>[ <c' g'> <c' g'> <c' g'>] | <b f'>8[\< <b f'> <b f'> <b f'>] <b f'>[ <b f'> <b f'> <b f'>] |
  <c' es'>8[\fff <c' es'> <c' es'> <c' es'>] <c' es'>[ <c' es'> <c' es'> <c' es'>] | <d' f'>8[ <d' f'> <d' f'> <d' f'>] <b f'>[ <b f'> <b f'> <b f'>] | r4 e'4~\ff\> e'8 d'8( c'8 b8) |
  r4 c'4~ c'8 a8( c'8 f'8) | r4 f'4~\mp f'8 e'8( d'8 g8) | r4 g4~ g8 b8( d'8 b8) | <e' g'>2\mp <es' g'>2\< |
}
recTwoArp = {
  bes,8(\mp\< d bes4.) a8( aes8 g8) | f,8( c f aes c'2) | \clef tenor g4\ff e'2.~ | e'4\< f'4 g'2 |
  c'4\fff aes'2~ aes'8 g'8 | f'2 d'4( b8 c'8) | \clef bass a,8(\ff\> e a c' e'2) | f,8( c f a c'2) |
  d,8(\mp aes, d f) g,2 | g,8(\> d f b f2) | c,8(\p g, c e es2\<) |
}

recTwoFluteOne = {
  R1*11 |
  \partCombineUnisono g''4\ff( e'''2.~ | e'''4\< f'''4 g'''2) | c'''4(\fff aes'''2~ aes'''8 g'''8 |
  f'''2 d'''4 b''8 c'''8) | \partCombineAutomatic a''2.~(\ff a''8 gis''8) | a''4.\>( g''8 f''2)\! | R1*3 |
}
recTwoFluteTwo = {
  R1*11 |
  g''4\ff( e'''2.~ | e'''4\< f'''4 g'''2) |
  c'''4(\fff aes'''2~ aes'''8 g'''8 | f'''2 d'''4 b''8 c'''8) | R1*5 |
}
recTwoOboeOne = {
  R1*11 | g'4\ff( e''2.~ |
  e''4\< f''4 g''2) | c''4(\fff aes''2~ aes''8 g''8 | f''2 d''4 b'8 c''8) | R1*5 |
}
recTwoOboeTwo = { R1*11 | \once \override NoteColumn.force-hshift = #1.5 g'2\ff c''2 | b'2\< f'2 | es'4\fff c''4 r8 c''8( bes'8 aes'8 | aes'2) g'2 | R1*5 | }
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
  f'2\mp\< r8 f'8( g'8 bes'8 | aes'2) f'2 |
  g''2\ff c'''2 | b''2\< f''2 |
  es''4\fff c'''4 r8 c'''8( bes''8 aes''8 | aes''2) g''4 f''4 |
  e''2\ff\> r8 e'8( f'8 g'8 | f'2) c''2 |
  f'4\mp aes'8( b'8) d''2~ | d''2( b'4 f'4) | e'2 es'2\< |
}
% c124: Cl 2 an octave higher at 158-161 (was E4-D4-C4-D4 inside the horns, doubling Tpt 3/Tbn 1): clarinets above the brass, not inside the horns (Rimsky-Korsakov PDF 108, 110-111)
recTwoClTwo = { R1*11 | e''1\ff | d''1\< | c''4\fff es''2 c''4 | d''1 | R1*5 | } % c154: E-flat5 on beats 2-3 of 160 (C5 back on beat 4, where Ob 2, Hn 3 and Cl 1 pass through B-flat): the woodwinds had no fifth of the A-flat chord (Adler PDF 160, 164)
recTwoBsnOne = {
  % c146: Bsn 1 takes 147-150 and Bsn 2 151-155, so neither sustains the pp bass for 18 s and Bsn 2 rests before its long 156-174 stretch (Adler PDF 188, 192)
  \partCombineSoloI c1\pp^\markup \bold "1." | f1 | d1 | g,1 | \partCombineAutomatic R1*5 |
  f,1\mp\< | \partCombineUnisono f,1 | g,1\ff | g,1\< | aes,1\fff | \partCombineAutomatic d2 g,4 \once \override Rest.staff-position = #2 r4 | e,1\ff\> | \partCombineUnisono f,1 | \partCombineAutomatic d,2\mp \partCombineUnisono g,2~ | g,1\> | \partCombineAutomatic c,2.\p r4 |
}
% c170: 161 Ob 2, Cl 1 (8va) and Hn 3 take the counterline's A-flat to G on beat 3 (was A-flat-F): the borrowed flat 6 of the iiø7 reaches 5 over V7
% before A-natural (vi) at 162; Hn 3 had A-flat4-F4-A3, flat 6 replaced by natural 6 before 5 (Aldwell & Schachter PDF 388, 395; c152's rule at 164).
recTwoBsnTwo = {
  R1*4 |
  e1\pp | f1 | f1 | g1 |
  c2 r2 |
  bes,1\mp\< | f,1 | g,1\ff |
  g,1\< | aes,1\fff | d2 g,2 | a,2.\ff\> \once \override Rest.staff-position = #-2 r4 | % c135: rests 161-162 inside the stave, clear of the hairpin (Gould PDF 50-51)
  f,1 | d2\mp g,2~ | g,1\> | c2.\p r4 |
}
recTwoCbsn = { R1*11 | g,,1\ff | g,,1\< | aes,,1\fff | d,2 g,,2 | R1*5 | }
recTwoHnOne = {
  e'2.~\< e'8 d'8\> | c'4\! a'2--\< g'4\!) | f'4.( e'8 d'4 f'8\< a'8 | c''2\> b'2\!) |
  g4( e'2--\< d'4\!) | c'4.(\> b8 a2\!) | R1 | c''4(\mp\> b'4 d''4 f'4) |
  e'2\p d'2 | f'1\< | f'2. r4 |
  g4\ff e'2.~ | e'4\< f'4 g'2 \breathe | c'4\fff aes'2~ aes'8 g'8 | f'2 d'4( b8 c'8) |
  e'1\ff\> | R1 | f'1\p | f'1 |
  e'2\mp es'2\< |
}
recTwoHnTwo = {
  R1*9 | d'2.~\p\< d'8 des'8 | c'2. r4 | g4\ff e'2.~ |
  e'4\< f'4 g'2 \breathe | c'4\fff aes'2~ aes'8 g'8 | f'2 d'4( b8 c'8) | c'1\ff\> |
  c'1 | c'2\p r2 | R1 | c'2\mp~ c'2\< |
}
recTwoHnThree = {
  % c153: Hn 3's B3 (145-146) resolves to C4 at 147 (A&S PDF 220, 456)
  c'2 r2 | R1*8 | bes1\p\< | aes1 | g'2\ff c''2 | % c087: Hn 3 holds 157 (entered at 156; breathes at 160), so one horn bridges into K
  b'2\< f'2 | es'4\fff c''4 r8 c''8( bes'8 aes'8 | aes'2) g'2 | \clef bass a1\ff\> |
  R1 | aes2\p g2 | b1 | g1\mp | % c152: 164 A-flat3-G3 (was A-flat3-A3): once introduced, flat 6 goes to 5, not to natural 6 (Aldwell & Schachter PDF 388, 395)
}
% c124: Hn 4 rests from 164 beat 3 (its G3 sat a second under Hn 3's A3; the ninth now sounds against bassoons and low strings, Rimsky-Korsakov PDF 102-103)
% c174: Hn 4 doubles Hn 3's counterline 158-161 (was a G3/A-flat3 pedal already held by Tbn 2, B.tbn, tuba): at ff-fff one horn has half the
% strength of a trumpet or trombone, so a horn line against full brass needs two horns in unison (Adler adler2 PDF 15 and 44; Rimsky-Korsakov ch. I, "two horns are needed to one trumpet")
% c185: part-only label (c181): Hn 4 doubles Hn 3 at 158-161
recTwoHnFour = { R1*9 | f1\p\< | f2. \once \override Rest.staff-position = #-10 r4 | g'2\ff-\tag #'part ^\markup \bold "a2 with 3." c''2 | b'2\< f'2 | es'4\fff c''4 r8 c''8( bes'8 aes'8 | aes'2) g2 | e1\ff\> | f1 | d2\p r2 | R1 | c1\mp | }
% c156: staggered breaths in the ff-fff brass block 158-162 (Adler PDF 292: brass need frequent breaths, more for loud playing; adler2 PDF 8: tuba).
% Sustained Gs (Hn 4, Tpt 2, Tbn 2, tuba) breathe after 158; the tune (Hn 1-2, Tpt 1) and Tpt 3, Tbn 1, B.tbn after 159; tuba again after 160. No note or dynamic changed.
recTwoTptOne = {
  R1*11 | g'4\ff e''2.~ | e''4\< f''4 g''2 \breathe | c''4\fff aes''2~ aes''8 g''8 |
  f''2 d''4( b'8 c''8) | c''2\ff\>~ c''2\mp | R1*4 |
}
recTwoTptTwo = {
  R1*11 | \once \override NoteColumn.force-hshift = #1.7 g'1\ff \once \override BreathingSign.direction = #DOWN \breathe | g'1\< | aes'1\fff |
  f'2 f'2 | e'2\ff\>~ e'2\mp | R1*4 |
}
recTwoTptThree = {
  % c154: E-flat4 at 160 (was C4, a unison with Tbn 1 through 158-162): the fff A-flat chord had its fifth only in Tbn 2's E-flat3 (Adler PDF 164, 165)
  % c169: 161 D4 (was B3, at pitch with Tbn 1): Tpt 3 falls E-flat4-D4-C4 through 160-162 (Adler PDF 165, 161)
  R1*11 | c'1\ff | b1\< \breathe | es'1\fff |
  d'1 | c'2\ff\>~ c'2\mp | R1*4 |
}
% c169: 159 D4 (was B3, at pitch with Tpt 3): the V7 gets its fifth in the brass and the leading tone is no longer doubled at pitch (Adler PDF 164-165; completes c154)
recTwoTbnOne = {
  R1*11 | c'1\ff | d'1\< \breathe | c'1\fff |
  b1 | c'2\ff\>~ c'2\mp | R1*4 |
}
recTwoTbnTwo = {
  R1*11 | g1\ff \once \override BreathingSign.direction = #DOWN \breathe | g1\< | es1\fff |
  f2 f2 | e2\ff\>~ e2\mp | R1*4 |
}
recTwoBassTbn = {
  R1*11 | g,1\ff | g,1\< \breathe | aes,1\fff |
  d2 g,2 | a,2\ff\>~ a,2\mp | R1*4 |
}
recTwoTuba = {
  R1*11 | g,,1\ff \breathe | g,,1\< | aes,,1\fff \breathe |
  d,2 g,,2 | a,,2\ff\>~ a,,2\mp | R1*4 |
}
recTwoTimp = { R1*11 | g,1:32\ff | g,1:32\< | aes,1:32\fff | g,4:32\>~ g,4\! r2 | R1*4 | r2 c2:32\p\< | }
recTwoPerc = \drummode { R1*12 | cymr1:32\pp\<\laissezVibrer^\markup { "2: Susp. cym." \italic "soft sticks, l.v." } | cymc1\fff\laissezVibrer^\markup { "1: Crash cym." \italic "l.v." } | R1*6 | }
recTwoHarpR = {
  % 156–166: one rolled chord per harmony on beat 1 in the upper register (the exposition had broken eighths);
  % beats 3–4 are left to the viola fills. No chord on beat 3 of 168 (4–3 suspension in the tune).
  R1*9 | <f'' bes'' f'''>2\arpeggio r2 | <aes'' c''' f'''>2\arpeggio r2 | R1*4 |
  <a'' c''' e'''>2\arpeggio r2 | <a'' c''' f'''>2\arpeggio r2^\markup \small \italic "étouffez" | <aes'' d''' f'''>2\arpeggio r2^\markup \small \italic "étouffez (m.d.)" | <g'' b'' f'''>2\arpeggio r2 |
  <c'' g'' c'''>4\arpeggio r4 r2 |
}
recTwoHarpL = {
  R1*8 | R1_\pedBflatAflat |
  <bes,, bes,>2\mf r2 | <f,, f,>2\f r2 | R1_\markup \small "B♮ A♮" | R1*3 |
  <a,, a,>2\f r2 | <f,, f,>2 r2_\markup \small "A♭" | <d, d>2\mp <g,, g,>2 | <g,, g,>2 r2 |
  <c, c>4\p r4 r2 |
}
% c107: Vln I rests 147-155 (the sul tasto halo is taken by Vln II div.), so the first violins' high colour is first heard with the tune at 155-156
% (Adler PDF 135: background in the palest register; the higher violin colour saved for the foreground statement).
recTwoVlnOne = {
  R1*8 |
  r2 r4 f''4\mf | \recTwoMelody |
}
% cycle 82: 148 IV–IV+ (C–C#–D in Vln II) into ii at 149; 155 beats 3–4 E→D in Vla/Vc/Hn1 under the violins' f pickup.
recTwoVlnTwo = {
  <e'' g''>1:32\pp^\markup { "div." \italic "sul tasto" } | <c'' a''>2:32 <cis'' a''>2:32 | <d'' a''>1:32 | <d'' f''>1:32 | <g'' bes''>1:32 | <f'' a''>1:32 | <d'' a''>1:32 | <c'' e''>4:32 <b' d''>2.:32 |
  <c'' e''>2:32 r4 f'4\mf^\markup { "unis." \italic "ord." } |
  d''2.~(\< d''8 des''8) | c''2( bes'4 aes'8 g'8) | g''4\ff\downbow e'''2.~ | e'''4\< f'''4 g'''2 |
  c'''4\fff\downbow aes'''2~ aes'''8 g'''8 | f'''2 d'''4( b''8 c'''8) | a'2.~(\ff a'8 gis'8) | a'4.\>( g'8 f'4 a'8 c''8) |
  d''2\mp( c''2\> | b'4 a'8 g'8 f'4 d'4) | c'2\p~ c'2\< |
}
recTwoVla = {
  e'2.~\< e'8 d'8\> | c'4\! a'2--\< g'4\!) | f'4.( e'8 d'4 f'8\< a'8 | c''2\> b'2\!) |
  g'4( e''2--\< d''4\!) | c''4.(\> b'8 a'8\! b'32 c''32 d''32 e''32 f''4~ | f''4 e''8 d''8 c''4 a'4) | c''4(\> b'4 d''4 f'4) |
  e'2\p d'2 | \recTwoSync |
}
recTwoVc = {
  \clef tenor e2.~\< e8 d8\> | c4\! a2--\< g4\!) | f4.( e8 d4 f8\< a8 | c'2\> b2\!) |
  g4( e'2--\< d'4\!) | c'4.(\> b8 a8\! b32 c'32 d'32 e'32 f'4~ | f'4 e'8 d'8 c'4 a4) | c'4(\> b4 d'4 f4) |
  e2\p d2 | \clef bass \recTwoArp |
}
% c163: 153 bass F (ii6/5 over the held 4^ of 152, Vln II D5-A5; was D, root ii), so the cadence 151-155 rises E-F-F-G-C as 51-55 does (Aldwell & Schachter PDF 291-292, 302). Bsn 2 follows.
recTwoCb = {
  c,4\pp^"pizz." r4 r2 | f,4 r4 r2 | d,4 r4 r2 | g,,4 r4 g,,4 r4 |
  e,4 r4 r2 | f,4 r4 r2 | f,4 r4 r2 | g,4 r4 g,4 r4 |
  c,4 r4 r2 | bes,,1\mp\<^"arco" | f,,1 | g,,1\ff |
  g,,1\< | aes,,1\fff | d,2 g,,2 | a,,1\ff\> |
  f,,1 | d,2\mp g,2~ | g,1\> | c,2\p~ c,2\< |
}
