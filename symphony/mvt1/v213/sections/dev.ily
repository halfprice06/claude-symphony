% DEVELOPMENT, bars 77–130.
% D1 77–84 (8): motto-head dialogue, a new colour on every entry.
% D2 85–96 (12): fugato.  D3 97–102 (6): second theme in B minor (fugato ends in B♭ minor; shifted up a semitone at 97).
% D3a 103–110 (8, cycle 70): the two themes combined. 103–106 (f): first-theme head on top (Ob 2 + Cl 2; strings rest, cycles 74/76) over the second-theme head in the
%   tenor (Hn 1, Bsn 1), D minor → V of E minor; 107–110 (p): inverted, second-theme head on top (Fl 1 low + Va) over the first-theme
%   head in the bass (bass clarinet alone since cycle 94), E minor → B♭ minor → cadential 6/4 and V of F minor (the exposition's own pitches 49–50, D♭–C–B♭–D♭–F | A♭–G).
% D3b 111–116 (6): the wedge.  D4 117–130 (14): dominant pedal, trombone motto augmented, climax, collapse, retransition.

% c142: 93 beats 3-4 Vla F4 (was E4), Bsn 1 F3 and Vc F3 (were G3): F/C, the passing V6/4 of B-flat minor over the bass D-flat-C-B-flat, as bar 90 has C/G
% over A-flat-G-F; the tonic chain G-C-F-B-flat now reaches every entry by its own dominant (Aldwell & Schachter Unit 17, PDF 265-268: all voices follow a sequential bass)
% c107: fugato countersubject bar 2 (89 Vc; 92 Vla + Bsn 1; 95 Vln II + Cl 1) holds a half note, then a neighbour turn in eighths,
% so it no longer moves in the subject's rhythm (Adler PDF 144 item 4, 145, 147).
% c175: Vln I "loco" at 124: the same written G5 follows the last note under the 8va at 123 (Gould PDF 48)
% c106: no 8va at 98-100 (Fl 1 tops at G6, four ledger lines; Gould PDF 47; cycle 5 rule: no ottava on the shared flute staff)
devFluteOne = {
  R1*4 | \partCombineSoloI r2 r8 g''8\f^\markup \bold "1." es'''4-> |
  \partCombineAutomatic r8 g''8\ff es'''4.-> d'''8 des'''8 c'''8 | aes''4-> r4 aes''4-> r4 | R1*10 | r8 f''8\f des'''4.-> c'''8-. ces'''8-. bes''8-. |
  bes''4\< a''8( bes''8) ges''4.-> f''8-. | r8 f''8 des'''4.-> c'''8-. ces'''8-. bes''8-. | \transpose c cis { r2. f''4(\ff | des'''2.~ des'''8 c'''8 |
  bes''4 ges'''2-- f'''4) | es'''4.( des'''8 c'''4 es''8 ges''8 | bes''2-- a''2) | f''4( des'''2-- c'''8 g''8) } |
  % cycle 74: 107–110 Fl 1 doubles the violas on the second-theme head
  % c109: Fl 1 joins only at 109 (D♭5 upward); at 107–108 (G4–C5, the flute's weakest register) a single flute adds nothing
  % to a viola section in unison (Rimsky-Korsakov PDF 76: strings predominate; best unisons are register-matched; PDF 66–67)
  % c167: Fl 1 pp (was mp, above the violas' p): a flute doubling a string line is marked lower than the strings (Sebesky PDF 164)
  % c178: back to mp: D-flat5-A-flat5 is the flute's 'sweet, little carrying power' register, where the player cannot add volume (Adler adler1 PDF 185-186);
  % at pp in unison with violas on the A string it is not heard at all
  R1*4 | R1*2 | des''4.(\mp^\markup { \bold "1." \italic "espr." } c''8 bes'4 des''8 f''8 | aes''2--\< g''4 c''4\!) |
  R1*4 |
  \partCombineUnisono des'''4\f c'''4 des'''4 es'''4 | d'''1\< | % c175: a2 held through 116 (was two side-by-side semibreves after the a2 label)
  \partCombineApart r8\ff b'8 aes''4.-> g''8 f''8 d''8 | r8 es''8 c'''4.-> b''8 c'''8 g''8 |
  r8 d''8 b''4-> r8 f''8 d'''4-> | r8 f''8 des'''4-> r8 bes''8 f'''4-> | es'''4.\< f'''8 g'''2 | \partCombineAutomatic aes'''1\fff |
  g'''1 | g''2.~\>( g''8 f''8)\! | R1*6 |
}
devFluteTwo = {
  R1*5 | r8 g'8\ff es''4.-> d''8 des''8 c''8 | f''4-> r4 f''4-> r4 | R1*27 |
  R1*4 |
  % c131: Fl 2 joins Fl 1 in the upper octave at 115-116 (a2) when Tpt 1 enters on the line with Ob 1 (Rimsky-Korsakov PDF 75: a trumpet doubled in the octave above needs 2 Fl + Ob)
  des'''4\f c'''4 des'''4 es'''4 | d'''1\< | f''1\ff | g''1 |
  % c155: dot above the top line, clear of Fl 1's D5 eighth on beat 1-and (it read as Fl 1's dot; Gould PDF 67: a note on a line takes its dot in the space above)
  \tweak Dots.direction #UP f''2. r4 | f''1 | g''1\< | d'''1\fff |
  d'''1 | R1*7 |
}
devOboeOne = {
  R1*2 | r8 b'8\mf( g''4.->) fis''8( f''8 e''8) | r2 r8 g'8\f es''4-> | R1 |
  \partCombineApart r8\ff g'8 es''4.-> d''8 des''8 c''8 | \partCombineAutomatic d''4-> r4 d''4-> r4 | R1*13 | \transpose c cis { r2. f'4(\ff | des''2.~ des''8 c''8 |
  bes'4 ges''2-- f''4) | es''4.( des''8 c''4 es''8 ges''8 | bes''2-- a''2) | f''4( des'''2-- c'''8 g''8) } |
  % 103–110 (inserted, cycle 70): first-theme head over the second-theme head (lower octave of the violins)
  % cycle 76: Ob 1 rests 103-110 (it played 97-102 ff); Ob 2 takes the first-theme head
  R1*4 | R1*4 |
  R1*4 |
  des''4\f c''4 des''4 es''4 | d''1\< | r8\ff b8 aes'4.-> g'8 f'8 d'8 | r8 es'8 c''4.-> b'8 c''8 g'8 |
  r8 d'8 b'4-> r8 f'8 d''4-> | r8 f'8 des''4-> r8 bes'8 f''4-> | es''4.\< f''8 g''2 | aes''1\fff |
  g''1 | g''2.~\>( g''8 f''8 | es''4. d''8 c''2) | d''1\p |
  R1*4 |
}
devOboeTwo = {
  R1*5 | c''1\ff | b'4-> r4 b'4-> r4 | R1*19 |
  \partCombineSoloII r8 a'8(\f f''4.->) e''8( es''8 d''8 | d''4) cis''8( d''8) g''4.-> f''8 | r8 d''8( bes''4.->) a''8( aes''8 g''8 | b''4) ais''8( b''8) g''4.->\> fis''8 | R1\! | R1*3 |
  \partCombineSoloII aes'1\mp\cresc | bes'1 | c''1 | c''2 b'2 |
  \partCombineAutomatic aes'1\f | aes'2\< a'2 | R1\! | R1*4 |
  % c124: Ob 2 D5 at 122-123 (was F4 under Tpt 1, doubling Hn 2): woodwinds complete the chord above the trumpets (Rimsky-Korsakov PDF 110-111); no second against Ob 1's G5 at 123 (PDF 102)
  d''1\fff |
  d''1 | R1*7 |
}
devCorAnglais = {
  % c096: part-only cue (82 bars rest before an off-beat fugato entry); removed from the full score by \removeWithTag #'part in score.ly
  R1*12 | \tag #'score R1*2 \tag #'part \cueDuring #"cueVla" #DOWN { s4*0^\markup \fontsize #-3 "Vla." R1*2 } | r8 c'8\f aes'4.-> g'8-. ges'8-. f'8-. | f'4 e'8( f'8) des'4.-> c'8-. | f'4-. g'4-. aes'4-. a'4-. |
  R1*4 | \transpose c cis { des'2.~\ff( des'8 c'8 | bes4 ges'2-- f'4) | es'4.( des'8 c'4 es'8 ges'8 | bes'2-- a'2) | f'4( des''2-- c''8 g'8) } |
  R1*28 |
}
devClOne = {
  r2 r8 es''8\mp( ces'''4->~ | ces'''8) bes''8( beses''8 aes''8 aes''2) | R1 | r2 r8 g'8\f es''4-> |
  R1 | \partCombineApart r8 g'8\ff es''4.-> d''8 des''8 c''8 \partCombineAutomatic | aes'4-> r4 aes'4-> r4 | R1*10 |
  % c187: 94-95 Cl 1 in unison with Vln II on the countersubject (was an octave below, B-flat3-F4, starting on the Bsn 1/Vc B-flat3 and ending on the Vla F4):
  % Rimsky-Korsakov PDF 76-77: the best string-wind unisons are register-matched (Vns + Cl.); PDF 78 (editor's note): a string and a wood-wind part in octaves, each undoubled, is not recommended. Leads into 96's D-flat5 without the octave leap.
  bes'4.\f c''8 des''8( es''8) f''4 | des''2\<( es''8 des''8 c''8 des''8) | r8 des''8 bes''4.->\ff a''8-. aes''4 |
  % c184: clarinets rest 97-102 (they doubled the violas' D4-B4 arpeggio in the register of the theme's lower octave, Vln II sul G + C.a.;
  % Adler adler1 PDF 135: keep background out of the melody's register when the colours are alike; PDF 144: thin the counterpoint, separate theme and accompaniment by register)
  R1*6 |
  % critic 84: Cl 1 joins Cl 2 and Ob 2 on the first-theme head 103-106 (balance against Hn 1 + Bsn 1 after the ff tutti)
  r8^\markup \bold "a2" a'8(\f f''4.->) e''8( es''8 d''8 | d''4) cis''8( d''8) g''4.-> f''8 | r8 d''8( bes''4.->) a''8( aes''8 g''8 | b''4) ais''8( b''8) g''4.^>\> fis''8 | R1\! | R1*3 |
  aes'1\mp\cresc | bes'1 | c''1 |
  c''2 b'2 | aes'1 | aes'2\ff a'4 r4 |
  % c147: 117-121 Cl 1 leaves the triplet unison (Cl 2 + Vla keep it) and doubles Ob 1 / Vln II on the theme's lower octave, which runs B3-G5 through
  % the held Hn 1·2 + Tbn 1·2 + Bsn 1 line (E-flat4-C4, ff) and the horn octave G3/G4 (Rimsky-Korsakov PDF 108-109: in forte horns outweigh woodwind,
  % double the upper woodwind part; PDF 108: clarinets rarely inside the horns). Marked f like Cl 2 on the shared staff (c117 layered dynamics kept).
  \partCombineApart r8\f b8 aes'4.-> g'8 f'8 d'8 | r8 es'8 c''4.-> b'8 c''8 g'8 |
  r8 d'8 b'4-> r8 f'8 d''4-> | r8 f'8 des''4-> r8 bes'8 f''4-> | es''4.\< f''8 g''2 | \partCombineAutomatic
  f''1\fff | d''1 | f''2.\> r4 | es'1 |
  d'1-\tweak X-offset #-2 \p | r8 g8\p\<( es'4.->) d'8( des'8 c'8 | c'4) b8( c'8) aes4.-> g8 | g4\mf( es'2 d'4 |
  des'4 c'2.) |
}
devClTwo = {
  R1*5 | r8 es'8\ff r8 es'8 r8 es'8 r8 es'8 | f'4-> r4 f'4-> r4 | R1*13 |
  R1*6 | % c184: rests 97-102, see Cl 1

  % cycle 74: Cl 2 doubles Ob 1 on the first-theme head 103–106 (strings rest)
  r8 a'8(\f f''4.->) e''8( es''8 d''8 | d''4) cis''8( d''8) g''4.-> f''8 | r8 d''8( bes''4.->) a''8( aes''8 g''8 | b''4) ais''8( b''8) g''4.^>\> fis''8 | R1*4\! | f'1\mp\cresc | g'2. r4 |
  g'1~( | g'4 f'2.) | f'1 | fis'2.\ff r4 |
  \tuplet 3/2 { b8\f d' f' } \repeat unfold 3 { \tuplet 3/2 { b8 d' f' } } | \omit Staff.TupletNumber \repeat unfold 4 { \tuplet 3/2 { c'8 es' g' } } | \repeat unfold 4 { \tuplet 3/2 { b8 d' f' } } | \repeat unfold 4 { \tuplet 3/2 { bes8 des' f' } } |
  \tuplet 3/2 { c'8\< es' g' } \repeat unfold 3 { \tuplet 3/2 { c'8 es' g' } } \undo \omit Staff.TupletNumber | b'1\fff | b'2. r4 | d'1\> |
  c'1 | \once \override NoteColumn.force-hshift = #1.7 c'4-\tweak X-offset #-2 \p( b2.) | R1*4 |
}
% c129: B.cl solo at 77-78 (was Bsn 1): the instrument of the opening motto (1-4) opens the development with the head (Rimsky-Korsakov Ex. 191, PDF 357: B.cl solo dolce in its upper-middle register)
devBassCl = {
  % c151: 77-78 down an octave (E-flat2-C-flat3 = written F3-D-flat4), into the chalumeau where the B.cl stated the motto at 1-4; no slurred crossing of the break
  % (Adler adler1 PDF 217: the B.cl chalumeau is its most distinctive, warmest, most effective register, and loses that quality as it goes up; PDF 210: the break)
  r8 es,8\mf^\markup \bold "Solo"_\markup \italic "espr."( ces4.->) bes,8( beses,8 aes,8 | aes,2) r2 | R1*12 | f,1\f | bes,2^\markup \small "(low C instr.)" c,2 | des,2 c,2 |
  bes,1 | es,2\< f,2 | bes,4 r4 bes,4 r4 | \transpose c cis { bes,1\ff |
  bes,1 | es1 | c2. r4 | f,1 |
  f,1 } |
  d,1\f | d,4 g,2 a,4 | bes,,2 c,2 | b,,2.\> r4\! |
  % c094: B.cl alone on the first-theme head in the bass 107–109 (was Bsn 2 + Vc in unison; same notes and octave), its only line of its own in the movement
  r8 b,8(\p^\markup \italic "espr." g4.->) fis8( f8 e8 | e4) g8( fis8) b,2 | r8 f,8( des4.->) c8( ces8 bes,8 | c1\<) | f1\mp\cresc | e1 | es2. r4 |
  d1 | des1 | c1 | g,1\ff~ |
  g,1~ | g,1~ | g,2. r4 | g,1\<~ |
  g,1\fff~ | g,2. r4 | g,1\>~ | g,1~ |
  g,1\pp | R1*4 |
}
% c129: 77-78 the head's solo moves to the bass clarinet (the bassoon already has it at 33; Rimsky-Korsakov PDF 117-118: a recurring idea in a new colour)
devBsnOne = {
  R1*3 | \partCombineApart r8\f g,8 es4-> r2 |
  r8 g8 es'4-> r2 | \partCombineAutomatic c'2\ff c'2 | b4-> r4 b4-> r4 | R1*4 |
  r8 g8\mf es'4.-> d'8-. des'8-. c'8-. | c'4 b8( c'8) aes4.-> g8-. | c'4-. d'4-. es'4-. e'4-. | f4.\f g8 aes8( bes8) c'4 |
  aes2( bes8 aes8 g8 aes8) | f1 | bes2 bes2~ | bes2\< des2 |
  r4. f8 des'4.-> c'8 | \transpose c cis { ces'8\ff bes8 r4 r2 | bes2 r8 f8 des'8 c'8 | bes2 r8 es8 ges8 bes8 |
  c'2 r8 ges8 es'8 des'8 | c'2 a2 | bes2 r8 f8 a8 c'8 } |
  f2.~(\mf f8 e8 | d4 bes2-- a4) | g4.( f8 e4 g8 b8 | e'2\> dis'2) |
  R1\! | R1*2 | c2\p\< g2 |
  f1\mp\cresc |
  g1 | g1~( | g4 f2.) | f1 |
  fis2. r4 | g1\ff | es'1~ | es'2. \partCombineApart d'4 |
  \partCombineAutomatic des'2. \breathe c'4~ | c'1\< | aes1\fff | g1 |
  g2.\> r4 | g1 | g1\p | R1*3 |
  \partCombineSoloI g,4(\f\<^\markup \bold "1." es2 d4) |
}
devBsnTwo = {
  R1*3 | c1\f | c1 | aes,8\ff aes,8 aes,8 aes,8 aes,8 aes,8 aes,8 aes,8 |
  g,4-> r4 g,4-> r4 | R1*7 | f,1\f | bes,,2 c,2 |
  des,2 c,2 | bes,,1 | es,2\< f,2 | bes,,4 r4 bes,,4 r4 |
  \transpose c cis { bes,1\ff | bes,1 | es1 | c2. r4 |
  f,1 | f,1 } |
  d,1\mf | d,4 g,2 a,4 | bes,,2 c,2 | b,,1\> | % c168: mf with Bsn 1 (shared staff), which doubles the mf cellos in unison 103-106
  R1\! | R1*2 | c,1\p\< |
  f,1\mp\cresc | e,1 |
  es,2. r4 | d,1 | des,1 | c,1 |
  g,1\ff~ | g,1~ | g,2. r4 | g,1~ |
  g,1\<~ | g,1\fff~ | g,1~ | g,2. r4\> |
  g,1~ | g,1\p | R1*4 |
}
devCbsn = {
  R1*5 | aes,,1\ff | g,,4-> r4 g,,4-> r4 | R1*12 |
  bes,,4\f r4 bes,,4 r4 | \transpose c cis { bes,,1\ff | bes,,1 | es,1 |
  c,1 | f,,1 | f,,2. r4 } |
  R1*8 | f,1\mp\cresc |
  e,1 | es,1 | d,1 | des,2. r4 | % c146: breath (Adler PDF 230); Bsn 2 and B.cl. breathe at 113, Vc/Cb hold the line
  c,1 | g,,1\ff~ | g,,2. r4 | g,,1~ |
  g,,1~ | g,,2. r4 | g,,1\fff~ | g,,1~ |
  g,,2. r4\> | g,,1~ | g,,1\pp | R1*4 |
}
% c128: 98-102 horns 1-2, trombone 1 and bass trombone drop to f after the ff hit at 97, so the counter answers the violins' and oboe's ff tune without covering it
% (Adler: the loud attack is the short note, the sustained notes after it are softer, adler2 PDF 189-190, Ex. XV-35; dynamic chosen by register and role, PDF 501 = adler2 188)
devHnOne = {
  R1 | r2 r8 b8\mf( g'4->~ | g'8) fis'8( f'8 e'8 e'2) | R1*2 |
  aes'1\ff | aes'4-> r4 aes'4-> r4 | R1*12 | r4. f8\f des'4.-> c'8 |
  \transpose c cis { ces'8\ff bes8 r4 r2 | bes2\f r8 f8 des'8 c'8 | bes2 r8 es8 ges8 bes8 | c'2 r8 ges8 es'8 des'8 |
  c'2 a2 | bes2 \override Staff.CombineTextScript.extra-offset = #'(0.8 . 1.6) a''2\rest } | \revert Staff.CombineTextScript.extra-offset % c165: lift the part-combiner's "2." clear of this rest (they touched)
  % c155: Hn 1 half rest on a ledger line above Hn 2's beam (Gould PDF 51; it floated a space above the stave)
  f'2.~(\mf f'8 e'8 | d'4 bes'2-- a'4) | g'4.( f'8 e'4 g'8 b'8 |
  % c185: part-only ossia 8va bassa for the undoubled written B5 (c156/c176/c177: keep the note in the score; offer the lower octave in the part)
  \tag #'score { e''2\> dis''2) } \tag #'part << { e''2\> dis''2) } \new Staff \with { alignAboveContext = "part" \remove "Time_signature_engraver" \remove "Key_engraver" fontSize = #-3 \override StaffSymbol.staff-space = #(magstep -3) \override StaffSymbol.thickness = #(magstep -3) } { \once \override TextScript.font-size = #-1 e'2^\markup \italic "ossia" dis'2 } >> | R1*4\! |
  aes'1\p\cresc | bes'1 |
  c''1 | c''2 b'2 | aes'1 | aes'2 a'4 r4 |
  % c186: Hn 1-2 breathe before the D at 119 (were unbroken 117-123, ff-fff, about 14 s); Tbn 1-2 hold the line there and breathe at the end of 121,
  % Bsn 1 before the C at 120 (Rimsky-Korsakov PDF 37 and 44: wind and brass players must be given a little rest from time to time)
  \partCombineUnisono g1\ff | es'1~ | es'2. \breathe d'4 | des'2. c'4~ |
  c'1 | \partCombineAutomatic aes'1\fff | g'1 | R1*7 |
}
devHnTwo = {
  R1 | r2 r8 b8\mf(^\markup \bold "a2" g'4->~ | g'8) fis'8( f'8 e'8 e'2) | R1*2 |
  es'1\ff | f'4-> r4 f'4-> r4 | R1*12 | r4. f8\f des'4.-> c'8 |
  \transpose c cis { ces'8\ff bes8 r4 r2 | bes2\f r8 f8 des'8 c'8 | bes2 r8 es8 ges8 bes8 | c'2 r8 ges8 es'8 des'8 |
  c'2 a2 | bes2 r8 f8 a8 c'8 } |
  R1*8 | f'1\p\cresc | g'1 |
  g'1~( | g'4 f'2.) | f'1 | fis'2. r4 |
  g1\ff | es'1~ | es'2. \breathe d'4 | des'2. c'4~ |
  c'1 | f'1\fff | f'1 | R1*6 |
  % c120: Hn 2 sounds the dominant's seventh F4 on beats 3-4 of 130 and resolves it to E-flat4 at 131 (its existing es'1); the leading tone B is
  % last heard at 128 and no seventh since 123, so the pedal reaches the reprise as a bare G under the motto's C (Aldwell & Schachter PDF 449, 456).
  r2 f'2\mf\<^\markup \bold "2." |
}
devHnThree = {
  R1*3 | r8 g8\f es'4-> r2 | r8 g8 es'4-> r2 | c'1\ff |
  d'4-> r4 d'4-> r4 | R1*2 | R1*11 | \transpose c cis { des'1\f |
  des'2. r4 | ges'1 | ges'1 | es'1 |
  des'2 c'4 r4 } |
  \clef bass d'1\mp | d'4 d'2( cis'4 | d'2 e'2 | fis'2\> b2) | % c188: legato (soft-tongued) inner line under the theme (Adler adler1 PDF 306 Ex. X-16, 309)
  R1*3\! | \clef treble \partCombineSoloI c'1\pp\< | \partCombineAutomatic
  c'1\p\cresc | c'1 | es'1 |
  d'1 | des'1 | d'2. r4 | g'1\ff |
  g'1 | g'1 | g'2. r4 | g'1 |
  d'1\fff | d'1 | b1\> | c'1 |
  c'4\p( b2.) | R1*4 |
}
devHnFour = {
  % c132: Hn 4 C4 at 82 (was A♭3): A♭3–B3 at 82–83 was a melodic augmented second; the third of VI is doubled instead (Aldwell & Schachter PDF 166, Ex. 11-5)
  R1*3 | r8 g8\f es'4-> r2 | r8 g8 es'4-> r2 | c'1\ff |
  b4-> r4 b4-> r4 | R1*2 | R1*11 | \transpose c cis { bes1\f |
  bes1 | bes1 | bes1 | bes2 a2 |
  bes2 a4 r4 } |
  a1\mp | f4( g2 e4 | d2 c2 | b,1\>) | R1*3\! | R1 |
  f1\p\cresc | g2. r4 | g1~( |
  g4 f2.) | f2. r4 | fis1 | g1\ff |
  g1 | g2. r4 | g1 | g1 |
  g1\fff | g2. r4 | g1\> | g1 |
  g2.\p r4 | g1\pp\<~ | g1 \once \override BreathingSign.direction = #DOWN \breathe | g1\mf~ | % c156: breath and restrike at the printed mf (was tied 127-130 into the ff at 131 with no gap; Adler PDF 292, 303)
  g1\f\< |
}
devTptOne = {
  % c186: trumpets, trombones, bass trombone (113) and tuba (111) pp, one level under the horns' p (Rimsky-Korsakov PDF 41: horns one degree stronger than the rest of the brass; if trumpets and trombones play pp, horns p)
  % c143: trumpets, trombones and bass trombone enter the wedge p (was mp) and crescendo faster than the strings to ff at 116-117 (Rimsky-Korsakov PDF 127: the second group enters p or pp and reaches its crescendo more rapidly; PDF 136: mp re-entries are colourless)
  R1*5 | \partCombineApart r8\ff g'8 es''4.-> d''8 des''8 c''8 | \partCombineAutomatic d''4-> r4 d''4-> r4 | R1*27 |
  % c108: trumpets join the wedge at 113 with the trombones, after strings and woodwinds (Rimsky-Korsakov PDF 130: crescendo by adding strings, wood-wind, brass)
  R1*2 | c''2.~(\pp\cresc c''8 b'8) | c''4.( b'8 f'4 aes'8 c''8) |
  des''4 c''4 des''4 es''4 | d''1\ff | R1*5 | aes'1\fff |
  g'1 | R1*7 |
}
devTptTwo = {
  R1*5 | aes'1\ff | aes'4-> r4 aes'4-> r4 | R1*27 |
  R1*2 | g'1~(\pp\cresc | g'4 f'2.) |
  f'1 | fis'1\ff | R1*5 | d'1\fff |
  d'1 | R1*7 |
}
devTptThree = {
  R1*5 | es'1\ff | b4-> r4 b4-> r4 | R1*27 |
  R1*2 | es'1\pp\cresc | d'1 |
  des'1 | d'1\ff | R1*5 | b1\fff |
  b1 | R1*7 |
}
devTbnOne = {
  R1*3 | r8 g,8\f es4-> r2 | r8 g8 es'4-> r2 | c'1\ff |
  aes4-> r4 aes4-> r4 | R1*12 | r4. f8\f des'4.-> c'8 | \transpose c cis { ces'8\ff bes8 r4 r2 |
  bes2\f r8 f8 des'8 c'8 | bes2 r8 es8 ges8 bes8 | c'2 r8 ges8 es'8 des'8 | c'2 a2 |
  bes2 r8 f8 a8 c'8 } | R1*10 | g1~(\pp\cresc |
  g4 f2.) | f1 | fis2. r4 | \partCombineUnisono g1\ff |
  es'1~ | es'2. d'4 | des'2. c'4~ | c'2.. r8 | % c087: eighth breath at 121 (Tchaikovsky 6/i 134 tuba)
  \partCombineAutomatic aes1\fff | g1 | g1\> | R1\! |
  R1*5 |
}
devTbnTwo = {
  R1*3 | r8 g,8\f es4-> r2 | r8 g8 es'4-> r2 | aes1\ff |
  f4-> r4 f4-> r4 | R1*27 | R1*2 |
  % c087: Tbn 2 breathes at 115 beat 4 and holds A2 through 116, so the low brass do not all breathe on beat 4 of 116
  c1\pp\cresc | c2 b,2 | aes,2. r4 | aes,2 a,2 |
  g1\ff | es'1~ | es'2. d'4 | des'2. c'4~ |
  c'2.. r8 | f1\fff | f1 | g1\> |
  R1\! | R1*5 |
}
devBassTbn = {
  R1*5 | aes,1\ff | g,4-> r4 g,4-> r4 | R1*12 |
  % c119: B.tbn takes F-sharp3 at 101-102 (was F-sharp2, the octave of Vc/Bsn 2/B.cl): fills the empty eleventh F-sharp2-B3 under the ff 6/4-V (Rimsky-Korsakov PDF 85-86: bass rarely more than an octave below the next part; no wide empty intervals in forte)
  bes,4\f r4 bes,4 r4 | \transpose c cis { bes,1\ff | bes,1\f | es1 |
  c1 | f1 | f1 } | R1*8 | R1 |
  R1*2 | d,1\pp\cresc | des,1 |
  c,2. r4 | g,1\ff | es1~ | es2. d4 |
  des2. c4~ | c2.. r8 |
  % c134: B.tbn on the bass G2 at 122-123, an octave over the tuba (Rimsky-Korsakov appendix PDF 505-507: Tbn III and tuba in octaves on the bass in every fff chord; PDF 82: the bass is doubled in the lower octave only); B stays in Tpt 3, Vla, Cl
  g,1\fff | g,1 |
  g,1\> | R1\! | R1*5 |
}
devTuba = {
  R1*5 | aes,,1\ff | g,,4-> r4 g,,4-> r4 | R1*27 |
  % c087: tuba breathes at 114 beat 4 (B.tbn holds the same D2) and holds C2 through 116
  f,1\pp\cresc | e,1 | es,1 | d,2. r4 |
  des,1 | c,1 | g,,1\ff~ | g,,1~ |
  g,,2. r4 | g,,1~ | g,,1\<~ | g,,2.\fff r4 |
  g,,1\>~ | g,,1~ | g,,2. r4 | g,,1\pp |
  R1*4 |
}
% c176: B2 at 97 on the A-flat drum (free 84-114; F2-C3), not the C drum lowered below its resonant range (Adler App. A, adler2 PDF 307)
devTimp = {
  R1*3 | c1:32\f\< | c1:32 | aes,8\ff aes,8 aes,8 aes,8 aes,8 aes,8 aes,8 aes,8 |
  g,4-> r4 g,4-> r4 | R1^\markup \small "muta A♭ in B♮" | R1*12 |
  \transpose c cis { bes,4\ff r4 r2 | R1*4 | R1 } | R1*8 | R1^\markup \small "muta B♮ in A♭" |
  R1*3 | aes,1:32\mf\<~ | aes,4\f r4 r2 |  % c166: the crescendo ends on a tied stroke on the A♭ still sounding at 116.1 (Adler PDF 80)
  g,1:32\f~ |
  g,1:32~ | g,1:32~ | g,1:32~ | g,1:32\< |
  g,1:32\fff~ | g,1:32~ | g,1:32\>~ | g,1:32~ |
  g,1:32\pp~ | g,1:32\<~ | g,1:32~ | g,1:32\mf~ |
  g,1:32\f\< |
}
devPerc = \drummode { R1*45 | tt1\fff~^\markup { "1: Tam-tam" \italic "heavy beater" } | tt1~ | tt1~ | tt1~ | tt1 | R1^\markup \small \italic "damp" | R1*3 | }  % c166: written length shows where the sound stops (Adler PDF 71, 73 Ex. XII-29; Tchaikovsky 6/iv 137-141)
devVlnOne = {
  R1*2 | r8 b'8\mf( g''4.->) fis''8( f''8 e''8) | r2 r8 g'8\f es''4-> | r2 r8 g''8 es'''4-> |
  r8 g''8\ff es'''4.-> d'''8 des'''8 c'''8 | <b' aes''>4->\downbow r4 <b' aes''>4->\downbow r4 | R1*10 | r8 f''8\f des'''4.-> c'''8-. ces'''8-. bes''8-. |
  bes''4\< a''8( bes''8) ges''4.-> f''8-. | r8 f''8 des'''4.-> c'''8-. ces'''8-. bes''8-. | \transpose c cis { r2. f'4(\ff | des''2.~ des''8 c''8) |
  bes'4( ges''2-- f''4) | es''4.( des''8 c''4 es''8 ges''8) | bes''2--( a''2) | f''4( des'''2-- c'''8 g''8) } |
  % 103–110 (inserted, cycle 70): the two theme heads combined; 103–106 P head over S head in the tenor (D minor → V of E minor), 107–110 inverted (S head on top, P head in the bass), into F minor at 111
  % cycle 74: Vln I rest 103–110 (103–106 winds and horns alone; 107–108 violas alone, 109–110 violas and Fl 1), re-entering at 111 (trumpets from 113 since cycle 108)
  R1*8 |
  aes''2.~(\mp\cresc aes''8 g''8) | bes''2.~( bes''8 a''8) | c'''2.~( c'''8 b''8) | c'''4.( b''8 f''4 aes''8 c'''8) |
  % c180: 115 beats 3-4 D-flat-E-flat (was E-flat-D-flat), also Fl 1·2, Ob 1, Tpt 1: the top line no longer moves D-flat (over the bII) straight up to D (A&S PDF 484, Ex. 28-3c; PDF 488, Ex. 28-12b); D arrives from E-flat, the motto's E-flat-D
  des'''4 c'''4 des'''4 es'''4 | d'''1 | r8 b'8\ff aes''4.-> g''8 f''8 d''8 | r8 es''8 c'''4.-> b''8 c'''8 g''8 |
  r8 d''8 b''4-> r8 f''8 d'''4-> | r8 f''8 des'''4-> r8 bes''8 f'''4-> | \ottava #1 es'''4.\< f'''8 g'''2 | aes'''1:32\fff |
  g'''1:32 \ottava #0 | g''2.~\>(^\markup \italic "loco" g''8 f''8 | es''4. d''8 c''2) | d''1\p |
  R1*4 |
}
% c141: 98-102 Vln II sul G (B3-D5; c186: now 98-100, B3-G4, the octave under Vln I at ff): G-string intensity, no open D on the held D4 at 98
% (Adler PDF 73-74, Ex. III-5 Tchaikovsky 5/ii sul G; PDF 134 Ex. V-9; Tchaikovsky 6/iv bar 148, Vln I and II sul G f).
devVlnTwo = {
  es'1:32\p | es'2:32 e'2:32 | e'1:32 | es'1:32\< |
  es'1:32 | r8 g'8\ff es''4.-> d''8 des''8 c''8 | <d'' f''>4->\downbow r4 <d'' f''>4->\downbow r4 | R1*7 |
  r8 c''8\f aes''4.-> g''8-. ges''8-. f''8-. | f''4 e''8( f''8) des''4.-> c''8-. | f''4-. g''4-. aes''4-. a''4-. | bes'4. c''8 des''8( es''8) f''4 |
  des''2\<( es''8 des''8 c''8 des''8) | r8 des''8 bes''4.->\ff a''8-. aes''4 | \transpose c cis { r1 | \once \override TextSpanner.bound-details.left.text = \markup \italic \small "sul G" des'2.~(\ff^\startTextSpan des'8 c'8) |
  % c186: sul G ends with bar 100 (top note G4, the octave of the open string); 101-102 (B4-D5) on the D string. Rimsky-Korsakov PDF 26: the highest note
  % on any of the three lower strings should be the one in the fourth position, the octave or the ninth of the open string; D5 on the G string is a twelfth up.
  bes4( ges'2-- f'4) | es'4.( des'8 c'4 es'8 ges'8)\stopTextSpan | bes'2--( a'2) | f'4( des''2-- c''8 g'8) } |
  R1*4 |
  << { e'1\pp^"div." | e'2( dis'2) | f'1( | f'2\< e'2) } \\ { b1\pp | g4( a2.) | bes2( des'2 | c'1\<) } >> |
  <c' f'>1:32\mp\cresc | <g' bes'>1:32 | <g' c''>1:32 | <g' c''>4:32 <f' c''>4:32 <f' b'>2:32 |
  <f' aes'>1:32 | <fis' aes'>2:32 <fis' a'>2:32 | r8^"unis." b8\ff aes'4.-> g'8 f'8 d'8 | r8 es'8 c''4.-> b'8 c''8 g'8 |
  r8 d'8 b'4-> r8 f'8 d''4-> | r8 f'8 des''4-> r8 bes'8 f''4-> | es''4.\< f''8 g''2 | <d'' aes''>1:32\fff |
  <d'' g''>1:32 | <d' f'>1\> | es'1 | d'1\p |
  R1*3 | g'4(\f\< es''2 d''4) |
}
devVla = {
  % c127: E-flat3 at 77 (was C-flat4, in unison with the bassoon solo's accented C-flat4 head note); C-flat4 from 78
  % (Adler PDF 274: keep the accompaniment registrally distant from a woodwind soloist)
  es1:32\p | ces'2:32 b2:32 | b1:32 | c'1:32\< |
  c'1:32 | r8 g8\ff es'4.-> d'8 des'8 c'8 | <b f'>4->\downbow r4 <b f'>4->\downbow r4 | R1*4 |
  r8 g8\mf es'4.-> d'8-. des'8-. c'8-. | c'4 b8( c'8) aes4.-> g8-. | c'4-. d'4-. es'4-. e'4-. | f'4.\f g'8 aes'8( bes'8) c''4 |
  aes'2( bes'8 aes'8 g'8 aes'8) | f'1 | f'1~( | f'4\< ges'4) bes2 |
  r8 des'8 bes'4.->\ff a'8-. aes'4 | \transpose c cis { bes'8\f f' des' f' bes' f' des' f' | f' des' bes des' f' des' bes des' | bes' ges' es' ges' bes' ges' es' ges' |
  ges' es' c' es' ges' es' c' es' | bes' es' c' es' a' es' c' es' | bes' f' des' f' a' es' c' es' } |
  R1*4 |
  g'2.~(\p^\markup \italic "espr." g'8 fis'8 | e'4 c''2-- b'4) | des''4.( c''8 bes'4 des''8 f''8 | aes''2--\< g''4 c''4) | % c115: stays in alto (one A-flat5 on the 4th ledger line; Gould PDF 21)
 
  c'8\mp\cresc c'8 b8( c'8) c'8 c'8 b8( c'8) |
  c'8 c'8 bes8( c'8) c'8 c'8 bes8( c'8) | c'8 c'8 b8( c'8) c'8 c'8 b8( c'8) | c'8 c'8 b8( c'8) aes8 aes8 g8( aes8) | aes8 aes8 bes8( aes8) aes8 aes8 bes8( aes8) |
  c'8 c'8 b8( c'8) c'8 c'8 b8( c'8) | \tuplet 3/2 { b8\f d' f' } \repeat unfold 3 { \tuplet 3/2 { b8 d' f' } } | \omit TupletNumber \repeat unfold 4 { \tuplet 3/2 { c'8 es' g' } } | \repeat unfold 4 { \tuplet 3/2 { b8 d' f' } } |
  \repeat unfold 4 { \tuplet 3/2 { bes8 des' f' } } | \tuplet 3/2 { c'8\< es' g' } \repeat unfold 3 { \tuplet 3/2 { c'8 es' g' } } \undo \omit TupletNumber | <b d'>1:32\fff | <b d'>1:32 |
  b1\> | c'1 | c'4\p( b2.)~ | b2. r4 | R1 |
  r2 g4(\mf\< es'4~ | es'4 d'4 des'4 c'4) |
}
devVc = {
  R1 | r2 r8 b,8\mf( g4->~ | g8) fis8( f8 e8 e2) | r8 g,8\f es4-> r2 |
  r8 g8 es'4-> r2 | aes,2\ff aes,2 | g4->\downbow r4 g4->\downbow r4 | g,1\subP |
  r8 d8\mf bes4.-> a8-. aes8-. g8-. | g4 fis8( g8) es4.-> d8-. | g4-. a4-. bes4-. b4-. | c'4. d'8 es'8( f'8) g'4 |
  es'2( f'8 es'8 d'8 es'8) | aes2 g2 | c'2. es'4~( | es'4 des'4) c'2~( |
  c'4 bes4) f2 | bes2\f bes2~ | bes2\< des2 | r4. f8 des'4.-> c'8 |
  \transpose c cis { bes,1\ff | bes,1 | es1 | c1 |
  f,1 | f,1 } |
  % c117: Vc doubles Bsn 1 on the second-theme head 103-106, an octave under Hn 1 (the theme keeps its horn + cello colour from 47;
  % Adler PDF 178: Meistersinger second theme = Horn I with octave-lower cellos; each element at least one string, one woodwind, one brass)
  f2.~(\mf f8 e8 | d4 bes2-- a4) | g4.( f8 e4 g8 b8 | e'2\> dis'2) |
  R1\! | R1*2 | c2\p\< g2 |
  f1\mp\cresc | g1 |
  g1~ | g4 f2. | f1 | fis1 |
  g,1:16\f | g,1:16 | g,1:16 | g,1:16 |
  g,1:16\< | aes1\fff | g1 | <g b>1\>^"div." |
  <g c'>1 | <g c'>4\p( <g b>2.) | g,4\pp\<^"unis." g,4 g,4 g,4 | g,8 g,8 g,8 g,8 g,8 g,8 g,8 g,8 |
  \tuplet 3/2 { g,8\mf g,8 g,8 } \repeat unfold 3 { \tuplet 3/2 { g,8 g,8 g,8 } } | g,16\f\< g,16 g,16 g,16 \repeat unfold 12 { g,16 } |
}
devCb = {
  aes,,1\p | aes,,2 e,2 | e,1 | c,1\< |
  c,1 | aes,,8\ff aes,,8 aes,,8 aes,,8 aes,,8 aes,,8 aes,,8 aes,,8 | g,,2->\downbow g,,2->\downbow | g,,2.\subP r4 |
  d,4\mf^"pizz." r4 r2 | g,4 r4 es,4 r4 | g,4 r4 bes,4 r4 | R1*2 |
  aes,2\mf^"arco"\< g,2 | f,1\f | bes,,2 c,2 | des,2 c,2 |
  bes,,1 | es,2\< f,2 | bes,,4 r4 bes,,4 r4 | \transpose c cis { bes,,1\ff |
  bes,,1 | es,1 | c,1 | f,,1 |
  f,,1 } |
  % c134: pizz. bass under the wind/horn tutti 103-106 (Rimsky-Korsakov PDF 121: pizz. cellos and basses added to a wood-wind tutti make its sustained notes distinct; Ex. 210, PDF 377)
  d,4\f^"pizz." r4 r2 | d,4 g,4 r4 a,4 | bes,,4 r4 c,4 r4 | b,,4 r4 r2 |
  e,4\p r4 r2 | e,4 r4 b,,4 r4 | bes,,4 r4 r2 | c,1\p\<^"arco" |
  f,1\mp\cresc | e,1 | es,1 |
  d,1 | des,1 | c,1 | g,,1\ff~^\markup \italic "change bow at will" |
  g,,1~ | g,,1~ | g,,1~ | g,,1\<~ |
  g,,1\fff~ | g,,1~ | g,,1\>~ | g,,1~ |
  g,,1\pp~ | g,,1\<~ | g,,1~ | g,,1\mf~ |
  g,,1\f\< |
}
