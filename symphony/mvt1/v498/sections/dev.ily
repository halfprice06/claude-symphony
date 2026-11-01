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
% c245: "loco" tagged score-only: the Violin I part has no 8va (parts-lib.ily, Gould PDF 47), so it needs no loco.
% c175: Vln I "loco" at 124: the same written G5 follows the last note under the 8va at 123 (Gould PDF 48)
% c106: no 8va at 98-100 (Fl 1 tops at G6, four ledger lines; Gould PDF 47; cycle 5 rule: no ottava on the shared flute staff)
devFluteOne = {
  R1*4 | \partCombineSoloI r2 r8 g''8\f^\markup \bold "1." es'''4-> |
  \partCombineAutomatic r8 g''8\ff es'''4.-> d'''8 des'''8 c'''8 | aes''4-> r4 aes''4-> r4 | R1*10 | r8 f''8\f des'''4.-> c'''8-. ces'''8-. bes''8-. |
  bes''4\< a''8( bes''8) ges''4.-> f''8-. | r8 f''8 des'''4.-> c'''8-. ces'''8-. bes''8-. | \transpose c cis { r2. f''4(\ff | des'''2.~\< des'''8 c'''8\> |
  bes''4\! ges'''2--\< f'''4\!) | es''4.( des''8 c''4 es''8\< ges''8 | % c289: Fl 1 joins the violins' octave on the downbeat of 100, at the start of the two-bar unit, not on beat 3 where the line climbs C-sharp5-E5-G5 to D6 at 102 (was E6-D6-C-sharp6 then a drop of a sixth to E5). Adler adler2 PDF 147-148 (d'Indy: leave out what cannot play the whole passage), PDF 151 (Mozart 40/iv: no instrument forced to leave the line mid-gesture)
  bes''2--\> a''2\!) | f''4( des'''2--\< c'''8\! g''8) } |
  % cycle 74: 107–110 Fl 1 doubles the violas on the second-theme head
  % c109: Fl 1 joins only at 109 (D♭5 upward); at 107–108 (G4–C5, the flute's weakest register) a single flute adds nothing
  % to a viola section in unison (Rimsky-Korsakov PDF 76: strings predominate; best unisons are register-matched; PDF 66–67)
  % c167: Fl 1 pp (was mp, above the violas' p): a flute doubling a string line is marked lower than the strings (Sebesky PDF 164)
  % c178: back to mp: D-flat5-A-flat5 is the flute's 'sweet, little carrying power' register, where the player cannot add volume (Adler adler1 PDF 185-186);
  % at pp in unison with violas on the A string it is not heard at all
  R1*4 | R1*2 | des''4.(\mp^\markup { \bold "1." \italic "espr." } c''8 bes'4 des''8 f''8 | aes''2--\< g''4 c''4\!) |
  R1*4 |
  \partCombineUnisono des'''4\f c'''4 des'''4 es'''4 | d'''1\< | % c175: a2 held through 116 (was two side-by-side semibreves after the a2 label)
  % c424: Fl 2 joins Fl 1 on the head 117-121 (a2); the held F5-G5 line moves to Ob 1 (see devOboeOne)
  \partCombineUnisono r8\ff b'8 aes''4.-> g''8 f''8 d''8 | r8 es''8 c'''4.-> b''8 c'''8 g''8 |
  r8 d''8 b''4-> r8 f''8 d'''4-> | r8 f''8 des'''4-> r8 bes''8 f'''4-> | es'''4.\< f'''8 g'''2 | \partCombineAutomatic aes'''1\fff |
  g'''2\> r2\! | g''2.~\mf\>( g''8 f''8)\! | R1*6 | % c399: Fl 1 leaves the G6 at 123.3 and re-enters mf on G5 at 124: a flute at G6 cannot make the fff-p diminuendo, so the strings, Ob 1 and Fl 1's lower octave make it (Adler adler2 PDF 213, Dvorak Slavonic Dance 8 m. 33; PDF 224 diminuendo by dropping out; as c179 at 41)
}
devFluteTwo = {
  % c254: 82 Fl 2 in unison with Fl 1 on the head (was G4-E-flat5, the flute's weak low octave, at pitch with Tpt 1 ff; the same octave already has Ob 1, Cl 1-2, Tpt 1, Vln II).
  % Adler adler2 PDF 151 (Mozart 40/iv: every note played effectively by every instrument used); PDF 152 (Beethoven 9/i: two flutes alone on the top octave)
  R1*5 | r8 g''8\ff es'''4.-> d'''8 des'''8 c'''8 | f''4-> r4 f''4-> r4 | R1*27 |
  R1*4 |
  % c131: Fl 2 joins Fl 1 in the upper octave at 115-116 (a2) when Tpt 1 enters on the line with Ob 1 (Rimsky-Korsakov PDF 75: a trumpet doubled in the octave above needs 2 Fl + Ob)
  des'''4\f c'''4 des'''4 es'''4 | d'''1\< |
  % c424: 117-121 Fl 2 doubles Fl 1 on the head (was a held F5-G5-F5-F5-G5 under and across Fl 1's head: the second flute in its weak middle
  % register as the only sustained part above G4 under the ff brass motto; Rimsky-Korsakov PDF 51: in forte 1 horn = 2 flutes; PDF 90 rule 3: 'the second
  % flute will sound too weak'; PDF 91 b: one colour for the stationary part, another for the moving parts). The held line is now in Ob 1.
  r8\ff b'8 aes''4.-> g''8 f''8 d''8 | r8 es''8 c'''4.-> b''8 c'''8 g''8 |
  r8 d''8 b''4-> r8 f''8 d'''4-> | r8 f''8 des'''4-> r8 bes''8 f'''4-> | es'''4.\< f'''8 g'''2 | d'''1\fff |
  d'''2\> r2\! | R1*7 | % c399: Fl 2 D6 leaves with Fl 1 at 123.3 (D stays in Ob 2 D5, Vln II)
}
devOboeOne = {
  R1*2 | r8 b'8\mf( g''4.->) fis''8( f''8 e''8) | r2 r8 g'8\f es''4-> | R1 |
  \partCombineApart r8\ff g'8 es''4.-> d''8 des''8 c''8 | \partCombineAutomatic d''4-> r4 d''4-> r4 | R1*13 | \transpose c cis { r2. f'4(\ff | des''2.~\< des''8 c''8\> |
  bes'4\! ges''2--\< f''4\!) | es''4.( des''8 c''4 es''8\< ges''8 | bes''2--\> a''2\!) | f''4( des'''2--\< c'''8\! g''8) } |
  % 103–110 (inserted, cycle 70): first-theme head over the second-theme head (lower octave of the violins)
  % cycle 76: Ob 1 rests 103-110 (it played 97-102 ff); Ob 2 takes the first-theme head
  R1*4 | R1*4 |
  R1*4 |
  % c424: 117-120 Ob 1 holds F5-G5-F5-F5 (Fl 2's former line, whose G5 at 121 is now the a2 climb; breaths on 119.4 and 120.4, where Ob 2's head has F5), Ob 2 takes the head's
  % lower octave with Cl 1 and Vln II (was Ob 1 on the head, Ob 2 resting): the stationary line gets a colour that carries under ff brass and differs from
  % the moving head (Rimsky-Korsakov PDF 51, 84 upper pedal, 91 b), and both pairs keep the normal order of register (PDF 90 rule 2)
  des''4\f c''4 des''4 es''4 | d''1\< | \partCombineApart f''1\ff | g''1 |
  f''2. r4 | f''2. r4 | \partCombineAutomatic es''4.\< f''8 g''2 | aes''1\fff | % c424: 121 Ob 1 back on the line with Ob 2 (a2) into the fff
  % c198: slur split at 125 with Vln I (see devVlnOne)
  \after 2.. \! g''1\> | g''2.~\>( g''8 f''8) | es''4.( d''8 c''2) | d''1\p |
  R1*4 |
}
devOboeTwo = {
  R1*5 | c''1\ff | b'4-> r4 b'4-> r4 | R1*19 |
  \partCombineSoloII r8 a'8(\f f''4.->) e''8( es''8 d''8 | d''4--) cis''8( d''8) g''4.-> f''8 | r8 d''8( bes''4.->) a''8( aes''8 g''8 | b''4) ais''8( b''8) g''4.->\> fis''8 | R1\! | R1*3 |
  \partCombineSoloII aes'1\mp\cresc | bes'1 | c''1 | c''2 b'2 |
  \partCombineAutomatic bes'2\f aes'2 | aes'1\< |
  r8\!\ff b8 aes'4.-> g'8 f'8 d'8 | r8 es'8 c''4.-> b'8 c''8 g'8 |
  r8 d'8 b'4-> r8 f'8 d''4-> | r8 f'8 des''4-> r8 bes'8 f''4-> | es''4.\< f''8 g''2 |
  % c124: Ob 2 D5 at 122-123 (was F4 under Tpt 1, doubling Hn 2): woodwinds complete the chord above the trumpets (Rimsky-Korsakov PDF 110-111); no second against Ob 1's G5 at 123 (PDF 102)
  d''1\fff |
  \after 2.. \! d''1\> | R1*7 |
}
devCorAnglais = {
  % c096: part-only cue (82 bars rest before an off-beat fugato entry); removed from the full score by \removeWithTag #'part in score.ly
  R1*12 | \tag #'score R1*2 \tag #'part \cueDuring #"cueVla" #DOWN { s4*0^\markup \fontsize #-3 "Vla." R1*2 } | r8 c'8\f aes'4.-> g'8-. ges'8-. f'8-. | f'4 e'8( f'8) des'4.-> c'8-. | f'4-. g'4-. aes'4-. a'4-. |
  % c264: 94-95 the C.a. keeps Vln II's countersubject (its F4-G4-A-flat4-A4 scale now reaches B-flat4 in the same instrument; it was cut off on the leading tone
  %   and the B-flat went to Cl 1). Adler adler2 PDF 176 (Jupiter 389-400: keep an established colour intact long enough; each voice keeps its wind partner,
  %   as Bsn 1 stays with the violas 88-95). Unison with Vln II, register-matched (c187's reason kept). Written F5-C6. Rests 96 (breath before 97).
  bes'4. c''8 des''8( es''8) f''4 | des''2\<( es''8 des''8 c''8 des''8) | R1\! | R1 | \transpose c cis { des'2.~\ff\<( des'8 c'8\> | bes4\! ges'2--\< f'4\!) | es'4.( des'8 c'4 es'8\< ges'8 | bes'2--\> a'2\!) | f'4( des''2--\< c''8\! g'8) } |
  R1*28 |
}
% c230 (cyclic; A&S Unit 32 PDF 586-587, 596, 599-600 Ex. 32-19): 78 the held A-flat5 is re-struck on beat 3 over the E bass, so it is spelled G-sharp5 (third of E major,
%   the common tone A-flat/G-sharp, as in Widmung and the Appassionata's A-flat - E - C - A-flat), and it ends with beat 3: E major for one beat, then E minor with the horns' G4
%   (was A-flat5 held through beat 4 against the horns' G4). The development's A-flat - E - C - A-flat (77-82) is the symphony's own key cycle; 78 now previews the II->III join (A-flat = G-sharp over E).
devClOne = {
  r2 r8 es''8\mp( ces'''4->~ | ces'''8) bes''8( beses''8 aes''8 gis''4) r4 | R1 | r2 r8 g'8\f es''4-> |
  R1 | \partCombineUnisono r8 g'8\ff es''4.-> d''8 des''8 c''8 \partCombineAutomatic | aes'4-> r4 aes'4-> r4 | R1*10 |
  % c187: 94-95 Cl 1 in unison with Vln II on the countersubject (was an octave below, B-flat3-F4, starting on the Bsn 1/Vc B-flat3 and ending on the Vla F4):
  % Rimsky-Korsakov PDF 76-77: the best string-wind unisons are register-matched (Vns + Cl.); PDF 78 (editor's note): a string and a wood-wind part in octaves, each undoubled, is not recommended. Leads into 96's D-flat5 without the octave leap.
  % c264: 94-95 now in the C.a. (it continues the line it doubled at 91-93; Adler adler2 PDF 176); Cl 1 joins Vln II at the ff restatement 96
  R1*2 | r8 des''8\ff bes''4.-> a''8-. aes''4 |
  % c184: clarinets rest 97-102 (they doubled the violas' D4-B4 arpeggio in the register of the theme's lower octave, Vln II sul G + C.a.;
  % Adler adler1 PDF 135: keep background out of the melody's register when the colours are alike; PDF 144: thin the counterpoint, separate theme and accompaniment by register)
  R1*6 |
  % critic 84: Cl 1 joins Cl 2 and Ob 2 on the first-theme head 103-106 (balance against Hn 1 + Bsn 1 after the ff tutti)
  % c199: no manual "a2" here: the part-combiner already prints "a2" over the first note (both clarinets identical), so the score showed "a2 a2" at 103
  r8 a'8(\f f''4.->) e''8( es''8 d''8 | d''4--) cis''8( d''8) g''4.-> f''8 | r8 d''8( bes''4.->) a''8( aes''8 g''8 | b''4) ais''8( b''8) g''4.^>\> fis''8 | R1\! | R1*3 |
  aes'1\mp\cresc | bes'1 | c''1 |
  % c382: 115 B4 moves to A-flat4 through B-flat4 (was B4-A-flat4, an augmented second in Cl 1, Ob 2, Hn 1, Vln II, Tbn 1): C-B-B-flat-A-flat runs in sixths over the wedge bass E-flat-D-D-flat-C (A&S PDF 552-553, chromatic 6/3s and 7-6 chains); B-flat over D-flat is a 6-5 into the plain triad at 115.3
  c''2 b'2 | bes'2 aes'2 | aes'2.\ff r4 |
  % c147: 117-121 Cl 1 leaves the triplet unison (Cl 2 + Vla keep it) and doubles Ob 1 / Vln II on the theme's lower octave, which runs B3-G5 through
  % the held Hn 1·2 + Tbn 1·2 + Bsn 1 line (E-flat4-C4, ff) and the horn octave G3/G4 (Rimsky-Korsakov PDF 108-109: in forte horns outweigh woodwind,
  % double the upper woodwind part; PDF 108: clarinets rarely inside the horns). Marked f like Cl 2 on the shared staff (c117 layered dynamics kept).
  \partCombineApart r8\f b8 aes'4.-> g'8 f'8 d'8 | r8 es'8 c''4.-> b'8 c''8 g'8 |
  r8 d'8 b'4-> r8 f'8 d''4-> | r8 f'8 des''4-> r8 bes'8 f''4-> | es''4.\< f''8 g''2 | \partCombineAutomatic
  f''1\fff | d''1\> | f''2. r4 | es'1 |
  d'1-\tweak X-offset #-2 \p | r8 g8\p\<( es'4.->) d'8( des'8 c'8 | c'4--) b8( c'8) aes4.-> g8 | g4\mf( es'2 d'4 |
  des'4 c'2.) |
}
devClTwo = {
  % c254: 82 Cl 2 joins Cl 1 on the head (was off-beat E-flat4 eighths inside the held ff E-flat4 of Hn 2 and Tpt 3, which added nothing: Adler adler2 PDF 147);
  % it takes over Fl 2's place in the head's middle octave, so that octave keeps its weight (c144/c194 reason)
  R1*5 | r8 g'8\ff es''4.-> d''8 des''8 c''8 | f'4-> r4 f'4-> r4 | R1*13 |
  R1*6 | % c184: rests 97-102, see Cl 1

  % cycle 74: Cl 2 doubles Ob 1 on the first-theme head 103–106 (strings rest)
  r8 a'8(\f f''4.->) e''8( es''8 d''8 | d''4--) cis''8( d''8) g''4.-> f''8 | r8 d''8( bes''4.->) a''8( aes''8 g''8 | b''4) ais''8( b''8) g''4.^>\> fis''8 | R1*4\! | f'1\mp\cresc | g'2. \once \override Rest.staff-position = #-4 r4 | % c335: Cl 2's rest at its own level below the centre line, not pushed below the stave by Cl 1's held B-flat4 (Gould PDF 50-51)
  g'1~( | g'4 f'2.) | f'1 | fis'2.\ff r4 |
  \tuplet 3/2 { b8\f d' f' } \repeat unfold 3 { \tuplet 3/2 { b8 d' f' } } | \omit Staff.TupletNumber \repeat unfold 4 { \tuplet 3/2 { c'8 es' g' } } | \repeat unfold 3 { \tuplet 3/2 { b8 es' f' } } \tuplet 3/2 { b8 d' f' } | \repeat unfold 3 { \tuplet 3/2 { bes8 des' f' } } r4 | % c196: Cl 2 breath on beat 4 of 120 before the 121-123 cresc. to fff (was 117-123 tongued f-fff without a rest, about 13 s); Vla keep the triplets (Sebesky PDF 23-24, 44)
  \tuplet 3/2 { c'8\< es' g' } \repeat unfold 3 { \tuplet 3/2 { c'8 es' g' } } \undo \omit Staff.TupletNumber | b'1\fff | b'2.\> r4 | d'1 |
  c'1 | \once \override NoteColumn.force-hshift = #1.7 c'4-\tweak X-offset #-2 \p( b2.) | R1*4 |
}
% c129: B.cl solo at 77-78 (was Bsn 1): the instrument of the opening motto (1-4) opens the development with the head (Rimsky-Korsakov Ex. 191, PDF 357: B.cl solo dolce in its upper-middle register)
devBassCl = {
  % c151: 77-78 down an octave (E-flat2-C-flat3 = written F3-D-flat4), into the chalumeau where the B.cl stated the motto at 1-4; no slurred crossing of the break
  % (Adler adler1 PDF 217: the B.cl chalumeau is its most distinctive, warmest, most effective register, and loses that quality as it goes up; PDF 210: the break)
  r8 es,8\mf^\markup \bold "Solo"_\markup \italic "espr."( ces4.->) bes,8( beses,8 aes,8 | aes,2--) r2 | R1*12 | f,1\f | bes,2^\markup \small "(low C instr.)" c,2 | des,2 c,2 |
  bes,1 | es,2\< f,2 | bes,4 r4 bes,4 r4 | \transpose c cis { bes,1\ff |
  bes,1 | es1 | c2. r4 | f,1 |
  f,1 } |
  % c278: B.cl mf at 103 (was f), the level of Bsn 2 on the same D2 and of the S head (Hn 1, Bsn 1, Vc mf) above it (Sebesky PDF 12-14)
  d,1\mf | d,4 g,2 a,4 | bes,,2 c,2 | b,,2.\> r4\! |
  % c094: B.cl alone on the first-theme head in the bass 107–109 (was Bsn 2 + Vc in unison; same notes and octave), its only line of its own in the movement
  r8 b,8(\p^\markup \italic "espr." g4.->) fis8( f8 e8 | e4--) g8( fis8) b,2 | r8 f,8( des4.->) c8( ces8 bes,8 | c1\<) | f1\mp\cresc | e1 | es2. r4 |
  d1 | des1 | c1 | g,1\ff~ |
  g,1~ | g,1~ | g,2. r4 | g,1\<~ |
  g,1\fff~ | g,2. r4 | g,1\>~ | g,1~ |
  g,1\pp | R1*4 |
}
% c129: 77-78 the head's solo moves to the bass clarinet (the bassoon already has it at 33; Rimsky-Korsakov PDF 117-118: a recurring idea in a new colour)
devBsnOne = {
  R1*3 | \partCombineApart r8\f g,8 es4-> r2 |
  % c344: 82 Bsn 1 takes the head with the violas (was C4 held, beside the C4 of Hn 3, Hn 4 and Tbn 1); the head's lowest octave had the violas alone inside the held brass chord.
  % Adler adler2 PDF 151 (Mozart 40/iv: the lowest octave of the unison scored with violas and woodwind; every note played effectively), PDF 147 (an instrument that adds nothing is better used elsewhere); continues Bsn 1's head fragment at 81
  r8 g8 es'4-> r2 | r8\ff g8 es'4.-> d'8 des'8 c'8 | \partCombineAutomatic b4-> r4 b4-> r4 | R1*4 |
  r8 g8\mf es'4.-> d'8-. des'8-. c'8-. | c'4 b8( c'8) aes4.-> g8-. | c'4-. d'4-. es'4-. e'4-. | f4.\f g8 aes8( bes8) c'4 |
  aes2( bes8 aes8 g8 aes8) | f1 | f2.( aes4~ | aes4\< ges4 f2) | % c237: 94-95 Bsn 1 stays with the violas (lower octave) on the free voice, as at 88-93 (Adler adler2 PDF 176: keep an established colour)
  r4. f8 des'4.-> c'8 | \transpose c cis { ces'8\ff bes8 r4 r2 | bes2 r8 f8 des'8 c'8 | bes2 r8 es8 ges8 bes8 |
  c'2 r8 ges8 es'8 des'8 | c'2 a2 | bes2 r8 f8 a8 c'8 } |
  % c388: part-only swells 103-105 as the cellos it doubles in unison and Hn 1 (c348); the shared Bsn staff in the score keeps Bsn 2's plain bass (MOLA Ex. 6 PDF 11: every doubling of a line carries its marks; PDF 7: one player per part)
  f2.~(\mf -\tag #'part \< f8 e8 -\tag #'part \> | d4 -\tag #'part \! bes2-- -\tag #'part \< a4 -\tag #'part \!) | g4.( f8 e4 g8 -\tag #'part \< b8 | e'2\> dis'2) |
  R1\! | R1*2 | c2\p\< g2 |
  f1\mp\cresc |
  g1 | g1~( | g4 f2.) | f1 |
  fis2. r4 | g1\ff | es'1~ | es'2. \partCombineApart d'4 |
  \partCombineAutomatic des'2. \breathe c'4~ | c'1\< | aes1\fff | g1 |
  g2.\> r4 | g1 | g1\p | R1*3 |
  \partCombineSoloI \soloStemsOn g,4(\f\<^\markup \bold "1." es2 d4) \soloStemsOff | % c225: stems by position (Gould PDF 27)
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
  g,1\<~ | g,1\fff~ | g,1~ | g,2. r4 |
  g,1\>~ | g,1\p | R1*4 | % c288: diminuendo starts on the note at 125, not on the rest (MOLA PDF 8, Ex. 7)
}
devCbsn = {
  R1*5 | aes,,1\ff | g,,4-> r4 g,,4-> r4 | R1*12 |
  bes,,4\f r4 bes,,4 r4 | \transpose c cis { bes,,1\ff | bes,,1 | es,1 |
  c,1 | f,,1 | f,,2. r4 } |
  R1*8 | f,1\mp\cresc |
  e,1 | es,1 | d,1 | des,2. r4 | % c146: breath (Adler PDF 230); Bsn 2 and B.cl. breathe at 113, Vc/Cb hold the line
  c,1 | g,,1\ff~ | g,,2. r4 | g,,1~ |
  g,,1~ | g,,2. r4 | g,,1\fff~ | g,,1~ |
  g,,2. r4 | g,,1\>~ | g,,1\pp | R1*4 | % c288: hairpin on the note at 125, not the rest
}
% c128: 98-102 horns 1-2, trombone 1 and bass trombone drop to f after the ff hit at 97, so the counter answers the violins' and oboe's ff tune without covering it
% (Adler: the loud attack is the short note, the sustained notes after it are softer, adler2 PDF 189-190, Ex. XV-35; dynamic chosen by register and role, PDF 501 = adler2 188)
devHnOne = {
  R1 | r2 r8 b8\mf( g'4->~ | g'8) fis'8( f'8 e'8 e'2--) | R1*2 |
  aes'1\f | aes'4->\ff r4 aes'4-> r4 | R1*12 | r4. f8\f des'4.-> c'8 |
  \transpose c cis { ces'8\ff bes8 r4 r2 | bes2\f r8 f8 des'8 c'8 | bes2 r8 es8 ges8 bes8 | c'2 r8 ges8 es'8 des'8 |
  c'2 a2 | bes2 \override Staff.CombineTextScript.extra-offset = #'(0.8 . 1.6) d''2\rest } | \revert Staff.CombineTextScript.extra-offset % c165: lift the part-combiner's "2." clear of this rest (they touched)
  % c155: Hn 1 half rest on a ledger line above Hn 2's beam (Gould PDF 51; it floated a space above the stave)
  % c445: on the fourth line instead (pitched rest d''): Hn 2's beam lies below the middle line and Hn 1's own notes lie below the stave, so nothing needs the rest
  % outside the stave (Gould PDF 50: upper-part rests above the centre line, outside only to avoid a collision; PDF 51: level with the part's own pitches)
  % c348: the S head's swells of 47-50 on the long notes, the tenuto minim and the pickup (Adler adler2 PDF 38, Ex. XI-20: every statement and every part carrying the tune keeps the < >; PDF 188); f/p levels unchanged
  f'2.~(\mf\< f'8 e'8\> | d'4\! bes'2--\< a'4\!) | g'4.( f'8 e'4 g'8\< b'8 |
  % c185: part-only ossia 8va bassa for the undoubled written B5 (c156/c176/c177: keep the note in the score; offer the lower octave in the part)
  \tag #'score { \soloStemsOn e''2\> dis''2) \soloStemsOff } \tag #'part << { e''2\> dis''2) } \new Staff \with { alignAboveContext = "part" \remove "Time_signature_engraver" \remove "Key_engraver" fontSize = #-3 \override StaffSymbol.staff-space = #(magstep -3) \override StaffSymbol.thickness = #(magstep -3) } { \once \override TextScript.font-size = #-1 e'2^\markup \italic "ossia" dis'2 } >> | R1*4\! |
  aes'1\p\cresc | bes'1 |
  c''1 | c''2 b'2 | bes'2 aes'2 | aes'2. r4 |
  % c186: Hn 1-2 breathe before the D at 119 (were unbroken 117-123, ff-fff, about 14 s); Tbn 1-2 hold the line there and breathe at the end of 121,
  % Bsn 1 before the C at 120 (Rimsky-Korsakov PDF 37 and 44: wind and brass players must be given a little rest from time to time)
  \partCombineUnisono g1\ff | es'1~ | es'2. \breathe d'4 | des'2. c'4~ |
  c'1\< | \partCombineAutomatic aes'1\fff | \partCombineChords \after 2.. \! g'1\> | \partCombineAutomatic R1*7 | % c345: G4/F4 semibreves of equal value as one chord, F4 left of G4 (Gould PDF 60, 61, 63); the combiner printed them as two offset voices
}
devHnTwo = {
  R1 | r2 r8 b8\mf(^\markup \bold "a2" g'4->~ | g'8) fis'8( f'8 e'8 e'2--) | R1*2 |
  es'1\f | f'4->\ff r4 f'4-> r4 | R1*12 | r4. f8\f des'4.-> c'8 |
  \transpose c cis { ces'8\ff bes8 r4 r2 | bes2\f r8 f8 des'8 c'8 | bes2 r8 es8 ges8 bes8 | c'2 r8 ges8 es'8 des'8 |
  c'2 a2 | bes2 r8 f8 a8 c'8 } |
  R1*8 | f'1\p\cresc | g'1 |
  g'1~( | g'4 f'2.) | f'1 | fis'2. r4 |
  g1\ff | es'1~ | es'2. \breathe d'4 | des'2. c'4~ |
  c'1\< | f'1\fff | \after 2.. \! f'1\> | R1*6 |
  % c120: Hn 2 sounds the dominant's seventh F4 on beats 3-4 of 130 and resolves it to E-flat4 at 131 (its existing es'1); the leading tone B is
  % last heard at 128 and no seventh since 123, so the pedal reaches the reprise as a bare G under the motto's C (Aldwell & Schachter PDF 449, 456).
  r2 f'2\mf\<^\markup \bold "2." |
}
devHnThree = {
  R1*3 | r8 g8\f es'4-> r2 | r8 g8 es'4-> r2 | c'1\f |
  d'4->\ff r4 d'4-> r4 | R1*2 | R1*11 | \transpose c cis { des'1\f |
  des'2. r4 | ges'1 | ges'1 | es'1 |
  des'2 c'4 r4 } |
  % c347: Hn 3 rests on 104.1 and 105.3, the two beats where Hn 1's S head attacks the same pitch (D4, E4) at the same moment; the inner horn line no longer doubles
  % the tune's attacks in its own colour (Adler adler2 PDF 264: Mozart keeps the orchestral horns out of the solo horn's way; PDF 274: accompaniment registrally apart from the soloist; PDF 283: the line is helped in pitch, not doubled)
  \clef bass d'1\mp | r4 d'2( cis'4 | d'2) r4 e'4( | fis'2\> b2) | % c188: legato (soft-tongued) inner line under the theme (Adler adler1 PDF 306 Ex. X-16, 309)
  R1*3\! | \clef treble \partCombineSoloI c'1\pp\< | \partCombineAutomatic
  c'1\p\cresc | c'1 | es'1 |
  d'1 | des'1 | d'2. r4 | g'1\ff |
  g'1 | g'1 | g'2. r4 | g'1\< |
  b1\fff | b2.\> r4 | b1\f\> | c'1 | % c408: f on the re-attack after the breath, inside the collapse (Adler adler1 PDF 308: horn re-entry shaped sf>p; X-25, X-40 held brass f>p)
  % c284: Hn 3 takes the leading tone B3 at 122-123 (was D4) and holds it to its resolution at 125: at the fff V-flat-9 B was in Tpt 3's low B3 alone among the brass, A-flat in nine parts (Adler adler2 PDF 15: above mf double the horns; a low trumpet is weaker) % c266: Hn 3 breathes on beat 4 of 123 with Hn 4 (was unbroken 121-126, about 14 s from ff< through fff; Adler PDF 292). Hn 1-2 and Tpt 2 hold through the beat.
  c'4\p( b2.) | R1*4 |
}
devHnFour = {
  % c132: Hn 4 C4 at 82 (was A♭3): A♭3–B3 at 82–83 was a melodic augmented second; the third of VI is doubled instead (Aldwell & Schachter PDF 166, Ex. 11-5)
  R1*3 | r8 g8\f es'4-> r2 | r8 g8 es'4-> r2 | c'1\f |
  b4->\ff r4 b4-> r4 | R1*2 | R1*11 | \transpose c cis { bes1\f |
  bes1 | bes1 | bes1 | bes2 a2 |
  bes2 a4 r4 } |
  a1\mp | f4( g2 e4 | d2 c2 | b,1\>) | R1*3\! | R1 |
  f1\p\cresc | g2. r4 | g1~( |
  g4 f2.) | f2. r4 | fis1 | g1\ff |
  g1 | g2. r4 | g1 | g1\< |
  g1\fff | g2.\> r4 | g1\f\> | g1 | % c408: level on the re-attack at 124, as Hn 3
 
  g2.\p \once \override Rest.staff-position = #-10 r4 | g1\pp\<~ | % c445: 126.4 rest level with Hn 4's G3 (was 2.5 spaces lower; Gould PDF 51)
  g1 \once \override BreathingSign.direction = #DOWN \breathe | g1\mf~ | % c156: breath and restrike at the printed mf (was tied 127-130 into the ff at 131 with no gap; Adler PDF 292, 303)
  g1\< | % c388: crescendo from the tied mf of 129 to f at 131 (was f< on the tied note into f at 131: a hairpin that arrived at its own level, and a new level on a tie; MOLA Ex. 3 PDF 10)
}
devTptOne = {
  % c186: trumpets, trombones, bass trombone (113) and tuba (111) pp, one level under the horns' p (Rimsky-Korsakov PDF 41: horns one degree stronger than the rest of the brass; if trumpets and trombones play pp, horns p)
  % c143: trumpets, trombones and bass trombone enter the wedge p (was mp) and crescendo faster than the strings to ff at 116-117 (Rimsky-Korsakov PDF 127: the second group enters p or pp and reaches its crescendo more rapidly; PDF 136: mp re-entries are colourless)
  R1*5 | \partCombineApart r8\ff g'8 es''4.-> d''8 des''8 c''8 | \partCombineAutomatic d''4-> r4 d''4-> r4 | R1*27 |
  % c108: trumpets join the wedge at 113 with the trombones, after strings and woodwinds (Rimsky-Korsakov PDF 130: crescendo by adding strings, wood-wind, brass)
  R1*2 | c''2.~(\pp\cresc c''8 b'8) | c''4.( b'8 f'4 aes'8 c''8) |
  des''4 c''4 des''4 es''4 | d''1\ff | R1*5 | aes'1\fff |
  \after 2.. \! g'1\> | R1*7 |
}
devTptTwo = {
  % c308: Tpt 2 rests at 82 (was A-flat4 held ff, the only held brass above f under the ff head, kept ff only because it shares Tpt 1's staff, c304):
  % a held trumpet in its clear middle register carries over the section (Adler adler1 PDF 300, 302, 316) and sat a semitone over the head's G4 in the same colour; A-flat4 stays in Hn 1 (f).
  % Tpt 2 returns on the ff strokes at 83 (part-only ff: the score shows Tpt 1's ff of 82 on the shared staff).
  R1*6 | aes'4->-\tag #'part \ff r4 aes'4-> r4 | R1*27 |
  R1*2 | g'1~(\pp\cresc | g'4 f'2.) |
  f'1 | fis'1\ff | R1*5 | d'1\fff |
  \after 2.. \! d'1\> | R1*7 |
}
devTptThree = {
  R1*5 | es'1\f | b4->\ff r4 b4-> r4 | R1*27 |
  R1*2 | es'1\pp\cresc | d'1 |
  des'1 | d'1\ff | R1*5 | b1\fff |
  \after 2.. \! b1\> | R1*7 |
}
devTbnOne = {
  R1*3 | r8 g,8\f es4-> r2 | r8 g8 es'4-> r2 | c'1\f |
  aes4->\ff r4 aes4-> r4 | R1*12 | r4. f8\f des'4.-> c'8 | \transpose c cis { ces'8\ff bes8 r4 r2 |
  bes2\f r8 f8 des'8 c'8 | bes2 r8 es8 ges8 bes8 | c'2 r8 ges8 es'8 des'8 | c'2 a2 |
  bes2 r8 f8 a8 c'8 } | R1*10 |
  % c319: 113-116 Tbn 1 takes Tbn 2's line an octave higher (C4, C4-B3, A-flat3, A-flat3) and Tbn 2 takes Tbn 1's (G3, G3-F3, F3, F-sharp3): Tbn 2 lay under the
  % B.cl's upper octave of the wedge bass (A-flat2-C3 third over C2 at 116, B2-D3 at 114), the only close low interval in any held chord outside the protected stop chord 26;
  % now the A-flat falls a step to G3 at 117 (was A-flat2 leaping a seventh up) and the F-sharp rises to it (Casanelles hyper-orchestra PDF 274: wide intervals low, thirds higher; Rimsky-Korsakov PDF 85). Breaths stay staggered (c087).
  c'1\pp\cresc | c'2 b2 | bes2 aes4 \once \override Rest.staff-position = #4 r4 | aes1 | \partCombineUnisono g1\ff | % c335: Tbn 1's rest at 115 on the top line, level with its A-flat3, not two spaces above the stave (Gould PDF 50-51)
  es'1~ | es'2. d'4 | des'2. c'4~ | c'2..\< r8\! | % c087: eighth breath at 121 (Tchaikovsky 6/i 134 tuba)
  \partCombineAutomatic aes1\fff | \partCombineChords g1\> | \partCombineAutomatic g1\f\> | R1\! | % c408: level on the restruck G3 at 124
  % c345: 123 G3/F3 as one chord (Gould PDF 60, 61, 63)
  R1*5 |
}
devTbnTwo = {
  R1*3 | r8 g,8\f es4-> r2 | r8 g8 es'4-> r2 | aes1\f |
  f4->\ff r4 f4-> r4 | R1*27 | R1*2 |
  % c087: Tbn 2 breathes at 115 beat 4 and holds A2 through 116, so the low brass do not all breathe on beat 4 of 116
  g1~(\pp\cresc | g4 f2.) | f1 | fis2. r4 | % c319: Tbn 1's former line (see Tbn 1)
  g1\ff | es'1~ | es'2. d'4 | des'2. c'4~ |
  c'2..\< r8\! | f1\fff | f1\> | R1\! | % c324: Tbn 2 leaves with the trumpets after 123 (was G3 at 124 in unison with Tbn 1: five brass on G against one horn on the leading tone; Rimsky-Korsakov PDF 100, 102)
  R1 | R1*5 |
}
devBassTbn = {
  R1*5 | aes,1\f | g,4->\ff r4 g,4-> r4 | R1*12 |
  % c119: B.tbn takes F-sharp3 at 101-102 (was F-sharp2, the octave of Vc/Bsn 2/B.cl): fills the empty eleventh F-sharp2-B3 under the ff 6/4-V (Rimsky-Korsakov PDF 85-86: bass rarely more than an octave below the next part; no wide empty intervals in forte)
  bes,4\f r4 bes,4 r4 | \transpose c cis { bes,1\ff | bes,1\f | es1 |
  c1 | f1 | f1 } | R1*8 | R1 |
  R1*2 | d,1\pp\cresc | des,1 |
  c,2. r4 | g,1\ff | es1~ | es2. d4 |
  des2. c4~ | c2..\< r8\! |
  % c134: B.tbn on the bass G2 at 122-123, an octave over the tuba (Rimsky-Korsakov appendix PDF 505-507: Tbn III and tuba in octaves on the bass in every fff chord; PDF 82: the bass is doubled in the lower octave only); B stays in Tpt 3, Vla, Cl
  g,1\fff | g,1 |
  g,1\> | R1\! | R1*5 |
}
devTuba = {
  % c304: 82 held brass f under the ff head, strokes ff at 83, as at 27-32, 131, 167 and 160 (Casanelles PDF 271-272, 287, 289)
  R1*5 | aes,,1\f | g,,4->\ff r4 g,,4-> r4 | R1*27 |
  % c087: tuba breathes at 114 beat 4 (B.tbn holds the same D2) and holds C2 through 116
  f,1\pp\cresc | e,1 | es,1 | d,2. r4 |
  des,1 | c,1 | g,,1\ff~ | g,,1~ |
  g,,2. r4 | g,,1~ | g,,2..\< r8\! | g,,2.\fff r4 | % c266: tuba breathes at the end of 121 with Tbn 1-2 and B.tbn and strikes the fff at 122 (was tied 120-122, about 5.7 s ff< fff on G1; Adler PDF 292, adler2 PDF 8). Cb, Cbsn keep the G.
  g,,1\>~ | g,,1~ | g,,2. r4 | g,,1\pp |
  R1*4 |
}
% c176: B2 at 97 on the A-flat drum (free 84-114; F2-C3), not the C drum lowered below its resonant range (Adler App. A, adler2 PDF 307)
devTimp = {
  % c354: roll at 80 starts p (was f) and swells into the ff at 82, so the f head entries at 80-81 are not covered (Adler adler2 PDF 184: Bloch marks the rolls p, then crescendo)
  R1*3 | c1:32\p\< | c1:32 | aes,8\ff aes,8 aes,8 aes,8 aes,8 aes,8 aes,8 aes,8 |
  % c375: the muta at 84 is right-aligned to the bar centre; centred, it ran past the end of the system (Gould PDF 41, 56)
  g,4-> r4 g,4-> r4 | R1^\tweak self-alignment-X #RIGHT ^\markup \small "muta A♭ in B♮" | R1*12 |
  % c296: the muta is printed at 98, right after the B stroke at 97 (was at 111, four bars before the A-flat roll at 115): Rimsky-Korsakov (rimsky-principles PDF 48)
  % expects a drum to be retuned "during a pause of some length"; the player now has the soft bars 103-110 to tune and check the A-flat, as at 34, 44 and 84.
  \transpose c cis { bes,4\ff r4 r2 } | R1^\markup \small "muta B♮ in A♭" | R1*13 |
  R1*3 | aes,1:32\mf\<~ | aes,4\f r4 r2 |  % c166: the crescendo ends on a tied stroke on the A♭ still sounding at 116.1 (Adler PDF 80)
  g,1:32\f~ |
  g,1:32~ | g,1:32~ | g,1:32~ | g,1:32\< |
  g,1:32\fff~ | g,1:32~ | g,1:32\>~ | g,1:32~ |
  g,1:32\pp~ | g,1:32\<~ | g,1:32~ | g,1:32\mf~ |
  g,1:32\f\< |
}
% c366: part only, the beater change is announced in the rests before the entry (Adler part 2 PDF 70 Ex. XII-22 'take brushes', 'take bow'; PDF 59 q. 1)
devPerc = \drummode { R1*40 | \tag #'part { R1*4^\markup \small \italic "take heavy beater" } \tag #'score { R1*4 } | R1 | tt1\fff~^\markup { "Tam-tam" \italic "heavy beater" } | tt1~ | tt1~\>_\markup \small \italic "damp gradually" | tt1~ | tt1\p | R1^\markup \small \italic "damp" | R1*3 | }  % c166: written length shows where the sound stops (Adler PDF 71, 73 Ex. XII-29; Tchaikovsky 6/iv 137-141)
% c248: 98-102 the ff B-minor second theme takes the swells the theme has at 47-52 and 147-152 (< to the long note, > after it; < to the minim peak), in every
% tune part (Fl 1, Ob 1, C.a., Vln I, Vln II, Vc); the counter, arpeggio and bass stay flat (Adler adler2 PDF 38, Ex. XI-20 Franck: the f climax of the
% lyrical theme keeps a per-bar < > in every doubling part; PDF 501 Ex. XV-33: the tune's hairpins belong to the line, not to its level).
devVlnOne = {
  R1*2 | r8 b'8\mf( g''4.->) fis''8( f''8 e''8) | r2 r8 g'8\f es''4-> | r2 r8 g''8 es'''4-> |
  r8 g''8\ff es'''4.-> d'''8 des'''8 c'''8 | <b' aes''>4->\downbow r4 <b' aes''>4->\downbow r4 | R1*10 | r8 f''8\f des'''4.-> c'''8-. ces'''8-. bes''8-. |
  bes''4\< a''8( bes''8) ges''4.-> f''8-. | r8 f''8 des'''4.-> c'''8-. ces'''8-. bes''8-. | \transpose c cis { r2. f'4(\ff | des''2.~\< des''8 c''8\>) |
  bes'4(\! ges''2--\< f''4\!) | es''4.( des''8 c''4 es''8\< ges''8) | bes''2--(\> a''2\!) | f''4( des'''2--\< c'''8\! g''8) } |
  % 103–110 (inserted, cycle 70): the two theme heads combined; 103–106 P head over S head in the tenor (D minor → V of E minor), 107–110 inverted (S head on top, P head in the bass), into F minor at 111
  % cycle 74: Vln I rest 103–110 (103–106 winds and horns alone; 107–108 violas alone, 109–110 violas and Fl 1), re-entering at 111 (trumpets from 113 since cycle 108)
  R1*8 |
  aes''2.~(\mp\cresc aes''8 g''8) | bes''2.~( bes''8 a''8) | c'''2.~( c'''8 b''8) | c'''4.( b''8 f''4 aes''8 c'''8) |
  % c180: 115 beats 3-4 D-flat-E-flat (was E-flat-D-flat), also Fl 1·2, Ob 1, Tpt 1: the top line no longer moves D-flat (over the bII) straight up to D (A&S PDF 484, Ex. 28-3c; PDF 488, Ex. 28-12b); D arrives from E-flat, the motto's E-flat-D
  des'''4 c'''4 des'''4 es'''4 | d'''1 | r8 b'8\ff aes''4.-> g''8 f''8 d''8 | r8 es''8 c'''4.-> b''8 c'''8 g''8 |
  r8 d''8 b''4-> r8 f''8 d'''4-> | r8 f''8 des'''4-> r8 bes''8 f'''4-> | es'''4.\< f'''8 g'''2 | aes'''1:32\fff |
  % c198: 124-125 two bows (was one slur 4.8 s from fff); the new bow starts on the cadential 6/4 at 125, which A&S PDF 348 has stressed and resolved softer (126); Ob 1 split identically (c88 rule), Fl 1 already ends at 124
  % c445: no 8va at 121-123 (was the score's only string octave sign): A-flat6 is written at pitch at 31, 72, 140 and 160 in this staff and in Fl 1 here; the
  % sign made Vln I look like Vln II's unison at 121 and hid the G6-G5 octave drop at 123-124 behind a written G5-G5 (Gould PDF 47: score octave signs only
  % to save space, five ledger lines for strings, keep the contour visible; PDF 48: loco no longer needed). Page breaks unchanged.
  g'''1:32\> | g''2.~( g''8 f''8) | es''4.( d''8 c''2) | d''1\p |
  R1*4 |
}
% c141: 98-102 Vln II sul G (B3-D5; c186: now 98-100, B3-G4, the octave under Vln I at ff): G-string intensity, no open D on the held D4 at 98
% (Adler PDF 73-74, Ex. III-5 Tchaikovsky 5/ii sul G; PDF 134 Ex. V-9; Tchaikovsky 6/iv bar 148, Vln I and II sul G f).
devVlnTwo = {
  es'1:32\p | es'2:32 e'2:32 | e'1:32 | es'1:32\< |
  es'1:32 | r8 g'8\ff es''4.-> d''8 des''8 c''8 | <d'' f''>4->\downbow r4 <d'' f''>4->\downbow r4 | R1*7 |
  r8 c''8\f aes''4.-> g''8-. ges''8-. f''8-. | f''4 e''8( f''8) des''4.-> c''8-. | f''4-. g''4-. aes''4-. a''4-. | bes'4. c''8 des''8( es''8) f''4 |
  des''2\<( es''8 des''8 c''8 des''8) | r8 des''8 bes''4.->\ff a''8-. aes''4 | \transpose c cis { r1 | \once \override TextSpanner.bound-details.left.text = \markup \italic \small "sul G" des'2.~(\ff\<^\startTextSpan des'8 c'8\>) |
  % c186: sul G ends with bar 100 (top note G4, the octave of the open string); 101-102 (B4-D5) on the D string. Rimsky-Korsakov PDF 26: the highest note
  % on any of the three lower strings should be the one in the fourth position, the octave or the ninth of the open string; D5 on the G string is a twelfth up.
  bes4(\! ges'2--\< f'4\!) | es'4.( des'8 c'4 es'8\< ges'8)\stopTextSpan | bes'2--(\> a'2\!) | f'4( des''2--\< c''8\! g'8) } |
  R1*4 |
  << { e'1\pp^"div." | e'2( dis'2) | f'1( | f'2\< e'2) } \\ { b1\pp | g4( a2.) | bes2( des'2 | c'1\<) } >> |
  <c' f'>1:32\mp\cresc | <g' bes'>1:32 | <g' c''>1:32 | <g' c''>4:32 <f' c''>4:32 <f' b'>2:32 |
  <f' bes'>2:32 <f' aes'>2:32 | <fis' aes'>1:32 | r8^"unis." b8\ff aes'4.-> g'8 f'8 d'8 | r8 es'8 c''4.-> b'8 c''8 g'8 |
  r8 d'8 b'4-> r8 f'8 d''4-> | r8 f'8 des''4-> r8 bes'8 f''4-> | es''4.\< f''8 g''2 | <d'' aes''>1:32\fff^"non div." | % c406: double stops kept (c236); 'non div.' because div. ran 107-116 and returns at 124 (Adler adler1 PDF 30: write non div. when each player is to play the double stop)
  <d'' g''>1:32\> | <d' f'>1^"div." | es'1^"unis." | d'1\p |
  R1*3 | g'4(\f\< es''2 d''4) |
}
devVla = {
  % c127: E-flat3 at 77 (was C-flat4, in unison with the bassoon solo's accented C-flat4 head note); C-flat4 from 78
  % (Adler PDF 274: keep the accompaniment registrally distant from a woodwind soloist)
  es1:32\p | ces'2:32 b2:32 | b1:32 | c'1:32\< |
  c'1:32 | r8 g8\ff es'4.-> d'8 des'8 c'8 | <b f'>4->\downbow r4 <b f'>4->\downbow r4 | R1*4 |
  r8 g8\mf es'4.-> d'8-. des'8-. c'8-. | c'4 b8( c'8) aes4.-> g8-. | c'4-. d'4-. es'4-. e'4-. | f'4.\f g'8 aes'8( bes'8) c''4 |
  aes'2( bes'8 aes'8 g'8 aes'8) | f'1 |
  % c237: 94-95 the violas take the free voice the cellos had at 91-93, a fourth higher (f'2. aes'4~ | aes'4 ges'4 f'2; was f'1~ | f'4 ges'4 bes2),
  % so each voice runs subject -> countersubject -> free voice and the fourth entry has three moving parts like the third (Adler adler2 PDF 175-176: Mozart thickens
  % the web with each entry and keeps each element's own rhythm; A&S Unit 17 via c142: all voices follow the sequential bass). The A-flat4 is a prepared 4-3 over E-flat, as the cellos' E-flat4 over B-flat at 92.
  f'2.( aes'4~ | aes'4\< ges'4 f'2) |
  r8 des'8 bes'4.->\ff a'8-. aes'4 | \transpose c cis { bes'8\f f' des' f' bes' f' des' f' | f' des' bes des' f' des' bes des' | bes' ges' es' ges' bes' ges' es' ges' |
  ges' es' c' es' ges' es' c' es' | bes' es' c' es' a' es' c' es' | bes' f' des' f' a' es' c' es' } |
  R1*4 |
  % c348: violas' S head 107-108 swells as 47-48 (Adler adler2 PDF 38, Ex. XI-20; PDF 188); 109-110 unchanged (Fl 1 joins there, c167/c178 settled)
  g'2.~(\p\<^\markup \italic "espr." g'8\> fis'8 | e'4\! c''2--\< b'4\!) | des''4.( c''8 bes'4 des''8 f''8 | aes''2--\< g''4 c''4) | % c115: stays in alto (one A-flat5 on the 4th ledger line; Gould PDF 21)
 
  c'8\mp\cresc c'8 b8( c'8) c'8 c'8 b8( c'8) |
  c'8 c'8 bes8( c'8) c'8 c'8 bes8( c'8) | c'8 c'8 b8( c'8) c'8 c'8 b8( c'8) | c'8 c'8 b8( c'8) aes8 aes8 g8( aes8) | aes8 aes8 bes8( aes8) aes8 aes8 bes8( aes8) |
  c'8 c'8 b8( c'8) c'8 c'8 b8( c'8) | \tupletUp \tuplet 3/2 { b8\f d' f' } \repeat unfold 3 { \tuplet 3/2 { b8 d' f' } } | \omit TupletNumber \repeat unfold 4 { \tuplet 3/2 { c'8 es' g' } } | \repeat unfold 3 { \tuplet 3/2 { b8 es' f' } } \tuplet 3/2 { b8 d' f' } | % c295: \tupletUp: the triplet 3s sat under the notes against the f at 117 (MOLA PDF 8, Ex. 7 PDF 12: collisions); c292: middle note follows the brass motto E-flat (119.1-3) to D (119.4), D-flat to C (120.4); the 6th displaces the 5th of V instead of sounding against it (A&S PDF 537, 301)
  \repeat unfold 3 { \tuplet 3/2 { bes8 des' f' } } \tuplet 3/2 { bes8 c' f' } | \tuplet 3/2 { c'8\< es' g' } \repeat unfold 3 { \tuplet 3/2 { c'8 es' g' } } \undo \omit TupletNumber \tupletNeutral | <b d'>1:32\fff | <b d'>1:32\> |
  b1 | c'1 | c'4\p( b2.)~ | b2. r4 | R1 |
  r2 g4(\mf\< es'4~ | es'4 d'4 des'4 c'4) |
}
devVc = {
  R1 | r2 r8 b,8\mf( g4->~ | g8) fis8( f8 e8 e2--) | r8 g,8\f es4-> r2 |
  r8 g8 es'4-> r2 | aes,2\ff aes,2 | g,4->\downbow r4 g,4->\downbow r4 | g,1\subP |
  % c392: 83 cellos G2 (was G3) with the bass (B.tbn, Bsn 2): the V-flat-9 keeps its root in the bass only, so Tbn 1's A-flat3 no longer sounds a semitone above a struck G3 (A&S PDF 463 Ex. 27-2, PDF 469-470); the fugato's A-flat3-G3 at 85 now brings the G3 itself (PDF 467)
  % c197: the countersubject at 88-90 lies a fourth to a sixth ABOVE the subject's second entry (Vla + Bsn 1, G3-E-flat4) in the cello's bright
  % A-string register, at the same mf; the cello drops to mp under the entry and rejoins the crescendo at 90 with the basses (Cb mf< to f at 91).
  % Adler adler2 PDF 42-43 (Ex. XI-23, Hindemith fugato: each entering voice mf over p continuing voices; 'the subject comes through clearly every time');
  % PDF 45-47 (Ex. XI-24, Bartok: every entry marked on its own, 'f, ben marc.'). Notes unchanged (c107/c142 protection).
  r8 d8\mf bes4.-> a8-. aes8-. g8-. | g4 fis8( g8) es4.-> d8-. | g4-. a4-. bes4-. b4-. | c'4.\mp d'8 es'8( f'8) g'4 |
  es'2( f'8 es'8 d'8 es'8) | aes2\< g2 |
  % c257: 91 rest on beat 1 (was c'2. from the downbeat): the cello's free voice held C4 from the downbeat, the pitch on which the C.a. starts the third entry at 91.1.5,
  % so the entry's first note sounded inside a held unison; the free voice now enters on beat 2, after the head (Adler adler2 PDF 213: Dvorak delays the oboe's entrance so the tune is clearer and the texture polyphonic; PDF 229: at-pitch doubling of like colours swallows a line)
  r4 c'2\f es'4~( | es'4 des'4) c'2~( |
  c'4 bes4) f2 | bes2\f bes2~ | bes2\< des2 | r4. f8 des'4.-> c'8 |
  % c285: tenor clef before the pickup F-sharp3 on beat 4 of 97, not between the pickup and its downbeat, so the phrase is read in one clef (Gould, Behind Bars PDF 22: clef between phrases; as c115 at 46 and 146)
  % c231: 98-102 the cellos leave the bass (still Cb + Cbsn on B1, B.cl + Bsn 2 + B.tbn on B2) and play the B-minor second theme with Vln II and the C.a.,
  % sul A/D in tenor clef, taking the pickup F-sharp3 at 97 that the violins' lower octave cannot reach (below the open G). The ff statement now has
  % Vln I / Vln II + Vc in octaves, as at 158-161 and as at 47 (the theme's own cello colour). Rimsky-Korsakov PDF 56 (cellos: tense passionate cantabile
  % on the A string), PDF 60-61 e) and Ex. 30 PDF 207 (violins and cellos in octaves, more resonant), PDF 60 c) (lower octave below the open G), PDF 62 a).
  \transpose c cis { bes,2.\ff \clef tenor f4( | des'2.~\< des'8 c'8\>) | bes4(\! ges'2--\< f'4\!) | es'4.( des'8 c'4 es'8\< ges'8) |
  bes'2--(\> a'2\!) | f'4( des''2--\< c''8\! g'8) } | \clef bass  % c296 octave-down proposal rejected: professional cellos play B4/D5 at ff (Adler App. A professional range, c286); keeps c231's at-pitch doubling
  % c117: Vc doubles Bsn 1 on the second-theme head 103-106, an octave under Hn 1 (the theme keeps its horn + cello colour from 47;
  % Adler PDF 178: Meistersinger second theme = Horn I with octave-lower cellos; each element at least one string, one woodwind, one brass)
  % c348: swells as Hn 1 and as 47-50 (Adler adler2 PDF 38, Ex. XI-20)
  f2.~(\mf\< f8 e8\> | d4\! bes2--\< a4\!) | g4.( f8 e4 g8\< b8 | e'2\> dis'2) |
  R1\! | R1*2 | c2\p\< g2 |
  f1\mp\cresc | g1 |
  g1~ | g4 f2. | f1 | fis1 |
  g,1:16\f | g,1:16 | g,1:16 | g,1:16 |
  % c444: cellos join the upper strings' tremolo on the fff chord and its resolution at 122-123 (was a plain held A-flat3/G3 after five bars of G2 tremolo): in every fff tremolo chord of Rimsky-Korsakov's appendix (chords 1, 2, 4, 6, 7, PDF 505) all five string groups tremolo together or none do
  g,1:16\< | aes1:32\fff | g1:32\> | <g b>1^"div." |
  <g c'>1 | <g c'>4\p( <g b>2.) | g,4\pp\<^"unis." g,4 g,4 g,4 | g,8 g,8 g,8 g,8 g,8 g,8 g,8 g,8 |
  \tuplet 3/2 { g,8\mf g,8 g,8 } \repeat unfold 3 { \tuplet 3/2 { g,8 g,8 g,8 } } | g,16\f\< g,16 g,16 g,16 \repeat unfold 12 { g,16 } |
}
devCb = {
  aes,,1\p | aes,,2 e,2 | e,1 | c,1\< |
  c,1 | aes,,8\ff aes,,8 aes,,8 aes,,8 aes,,8 aes,,8 aes,,8 aes,,8 | g,,2->\downbow g,,2->\downbow | g,,2.\subP r4 |
  % c227: Cb rest 85-89 (were pizz. D, G-E-flat, G-B-flat under the cello's subject 85-87): the fugato subject is heard alone at first
  % (Adler adler1 PDF 145: "in a fugal exposition the subject heard alone at the beginning carries added weight"; PDF 144 Ex. V-21 and 147 Ex. V-23:
  % the bass either doubles the subject or waits). The basses re-enter arco at 90 under the second entry's last bar, as before.
  R1*5 |
  aes,2\mf\< g,2 | f,1\f | bes,,2 c,2 | des,2 c,2 |
  bes,,1 | es,2\< f,2 | bes,,4 r4 bes,,4 r4 | \transpose c cis { bes,,1\ff |
  bes,,1 | es,1 | c,1 | f,,1 |
  % c195: quarter rest before the pizz. at 103 (was f,,1): the ff bowed note ran to the barline with no time to take the pizz.
  % (Adler PDF 54: time must be allowed to change from arco to pizz.; Cbsn already rests on this beat)
  f,,2. r4 } |
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
