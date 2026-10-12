% B SECTION, bars 37-64 (Poco più mosso, 4/4), D flat major.
% 37-44 B1: new theme in flute 1 with clarinet 1 an octave lower, over viola triplets and pizzicato bass.
%          It opens with a rising fourth; bar 42 is the motto's tail at the D flat level (A flat-G-G flat-F),
%          harmonised as in bar 8 (vi7 - V7/V - V7 - I).
% 45-52 B2: the theme's head in B flat minor (violins), D flat 7 = C sharp 7, then F sharp minor (= G flat minor):
%          oboe 1 quotes the movement I second-theme head in minor with its pickup (cyclic-notes §3), once.
%          G sharp 7 respelled A flat 7 leads back to D flat.
% 53-60 B3: the theme in both violin sections (an octave apart), horn 1 counter-melody from the A theme's head;
%          woodwinds and horns join for the crescendo.
% 61-64 B4: climax on D flat (61), G flat to F flat (= E major) (62), then A minor: trombone 1 quotes the
%          movement I first-theme head once, ff, in a foreign key (cyclic-notes: Dvořák 9/ii 96-98 model).

bSecFluteOne = {
  f''2(\p\< ges''8 f''8 es''4\! | des''4\> c''8 des''8 es''2)\! | ges''4(\< \tuplet 3/2 4 { f''8 ges'' f'' } es''4\> des''4 | c''4\! des''8 c''8 bes'2) \breathe |  % c036: breath between theme B's two halves (Adler part 1 PDF 188). c031: head rhythm 2 8 8 4 at 37/45/53, so theme B does not open with theme A's 4. 8 (Dvorak 9/ii: bar 7 vs bar 46)
  r2 f''4.(\< ges''8 | aes''4\mp\> bes''8 aes''8 ges''4~ ges''8 f''8 | es''4. f''8 des''4 bes'4 | c''2.)\p r4 |  % c051: flute 1 rests 41 b1-2; the cor anglais starts theme B's second phrase alone in its strong low register and the flute joins on F5 (Sebesky PDF 219: compensate for a soloist's weak register; Adler part 1 PDF 185, 205)  % c061: 42 b3-4 the 7th G flat of A flat7 is held into the D flat chord as a 4-3 (A&S PDF 359-360, Ex. 21-23a: dissonant preparation), the theme's only suspension (also 58)
  R1*8 |
  R1*4 |
  \stemDown aes''4(\p\<-\tag #'score ^\markup \bold "1." des'''4 f'''4. ges'''8 | aes'''4 bes'''8 aes'''8 ges'''4~ ges'''8 f'''8 | es'''4.\f f'''8 des'''4 bes''4 | c'''1)\< \breathe |  % c015: Fl 2 rests, so stems follow the notes (Gould PDF 38); the combiner keeps voice one here
  \stemNeutral aes'''1--~\ff | aes'''1( | a'''4) r4 r2 | R1 |  % c070: the top voice's G sharp6 (A flat6) resolves to A6 in the flute that holds it, with the violins' A6, instead of stopping while the violins take the A (A&S PDF 394, Ex. 23-12: a chromatic succession split between voices)  % c059: flute 1 holds the A flat6 the upper half of Vln I had; flute 2 keeps the augmented head  % c021: a2 with flute 2
}
% c021: flute 2 joins flute 1 in unison on theme B's augmented head at the climax, so the upper octave of trumpet 1's
% A flat-D flat-F-F flat has two flutes (Rimsky-Korsakov PDF 75: "in the top register two flutes will suffice").
bSecFluteTwo = {
  R1*8 | R1*8 | R1*8 |
  aes''2--(\ff des'''2-- | f'''2-- fes'''2--) | R1*2 |
}
% c043: 46 b3-47 a swell to the C sharp 7 (V7 of the F sharp minor quotation): oboe 1 and cellos mf, the accompaniment mp, back to pp
% at 48, so the middle section has a smaller wave before the build at 53-61 (A&S PDF 247-248: the applied dominant reached in a chain of
% descending 5ths is a goal chord; Dvorak 9/ii Largo, corpus MusicXML: f at 48 and 53 in the C sharp minor section before the ff at 96).
bSecOboeOne = {
  R1*7 | r2 r4 aes'4(\p-\tag #'score ^\markup \bold "1."^\markup \italic "dolce espr." |  % c071: pickup A flat4-D flat5 (rising fourth) into the head, alone on the empty fourth beat of 44
  % c041: theme B's head in B flat minor (45-47) moves from Vln I to oboe 1, so each statement of theme B has its own colour
  % (Fl 37, Fl + Eh 41, Ob 45, violins 53, tutti 57) and the oboe, "basically a lyrical instrument", sings one phrase of a theme
  % in its "warm, prominent, reedy and poignant" range F4-C6 (Adler part 1 PDF 198); it hands the C sharp5 to its sister
  % instrument, the cor anglais, whose quotation picks up on 47 b4 (PDF 204-205). Cellos keep the lower octave (c011).
  des''2 es''8 des''8 c''4) | bes'4( aes'8 bes'8 des''2\<) | cis''2.\mf\> r4\! |
  R1*9 |  % c040: the movement I quotation 47-53 is in the cor anglais (see bSecCorAnglais)
  \stemDown aes'4(\p\<-\tag #'score ^\markup \bold "1." des''4 f''4. ges''8 | aes''4 bes''8 aes''8 ges''4~ ges''8 f''8 | es''4.\f f''8 des''4 bes'4 | c''1)\< \breathe |
  \stemUp f''1--(\ff | f''2-- fes''2--) | R1*2 |  % c014: oboe 1 above the trumpets at 61 (Rimsky-Korsakov PDF 110-111)
}
bSecOboeTwo = {
  R1*8 | R1*8 | R1*8 |
  des''1--\ff | des''2-- fes''2-- | R1*2 |  % c047: D flat5 held at 61 (was A flat4-D flat5 with trumpet 1, clarinet 1, horn 3 and Vln II): with oboe 1's F5 and the flutes' A flat5 the double reeds complete the D flat chord above the trumpets (Rimsky-Korsakov PDF 110-111), filling A flat4-F5. c014: was F4 = Tpt 2 + Hn 2
}
% c009: the lower octave of theme B goes to the cor anglais (Rimsky-Korsakov Ex. 57: Fl / Eng. horn in octaves).
% c021: 37-40 flute 1 alone (Rimsky-Korsakov PDF 66-67: an intimate melody to a solo instrument of simple timbre;
% doubling where the expression broadens); the lower octave would sit in unison with the Vln II chord tones F4, D flat4, G flat4.
% The cor anglais joins at 41 with the crescendo.
bSecCorAnglais = {
  R1*4 |
  aes4(\p\<^\markup \italic "solo, dolce cantabile" des'4 f'4. ges'8 | aes'4\mp\> bes'8 aes'8 ges'4~ ges'8 f'8 | es'4. f'8 des'4 bes4 | c'2.)\p r4 |
  % c040: the quotation of movement I's second-theme head (minor, with pickup), once, moved here from oboe 1. Its pickup C sharp4 lay in the
  % oboe's lowest fifth, where Adler (part 1 PDF 198) says it "honks" and should not be asked to play softly; C sharp4-D5 is the cor anglais'
  % middle register (Adler part 2 PDF 188: the solo instrument is chosen for the tune's register and dynamic). In movement I the cor anglais
  % plays the motto with pickup at 5-8 and 171-174, whose first bar is the first bar of this quotation (Adler part 1 PDF 19: timbre
  % clarifies content). Pitches, rhythm, dynamics and "espr." as in v40.
  R1*2 | r2 r4 cis'4(\p^\markup \italic "solo, espr." | a'2.~ a'8 gis'8 | fis'4 d''2--\< cis''4\! ) | cis''2(\mp b'4 a'4) \breathe |  % c048: tenuto and swell on the syncopated D5, as on the S head's syncopated half note in every movement I statement (mvt I tTwo 32-33, dev 97-99, recTwo 79, coda 69; A&S PDF 51: a note held from a weak through a strong beat conflicts with the meter)
  aes'2(\> ges'2 | f'2. ges'4)\p |
  f'2 r2 | R1*3 |
  R1*8 |
}
bSecClOne = {
  R1*8 |
  R1*8 |
  r2 r4 aes8(\pp bes8 | des'4.\< f'8 bes'2 | ges'2\p f'2 | c'2 des'2) \breathe |  % c038: one level under horn 1, so the unison is one colour (Casanelles PDF 147-148). c019: unison with Hn 1's counter-line, which the viola triplets cover in the same register  % c051: 56 C4-D flat4 (was E flat4-D flat4): the counter-line rises against the theme's C5-B flat4 instead of following it in sixths after its G flat-F-E flat-D flat descent (Sebesky PDF 211-212, Ex. 279-280)
  \partCombineApart f'2\mp\< des''2 | des''2 c''4 des''4 | es''2\f r2 | c''1\< \breathe |  % c049: rests at 59 b3-4 (was E flat5, held over the theme's lower octave D flat5-B flat4 in Ob 1 and Vln II; Rimsky-Korsakov PDF 133, 157); both clarinets re-enter on the V7 swell at 60  % c047: 57 b3-59 an octave higher, above horn 1: the clarinets fill the empty F4-A flat5 space under the theme's lower octave instead of crowding A flat3-F4 with the violas and bassoon (Rimsky-Korsakov PDF 108: a horn chord is completed by clarinets in the upper register, clarinets rarely inside the horns; PDF 108-109: forte, double the upper harmonic parts); also no E flat4-C5 leap into 60  % c045: apart mode 57-60 (no a2 label on the single unison at 57 b3)
  \partCombineAutomatic f''1--\ff | ges''2-- aes''2-- | R1*2 |  % c084: clarion F5-G flat5-A flat5 (written G5-A flat5-B flat5), following oboe 1's C5-F5 and doubling horn 2 / trombone 2 two octaves up; was A flat4-D flat5 | B flat4-C flat5, now in clarinet 2 (Casanelles PDF 257, 275: each register its own strength; PDF 277-278: a weak unison doubling adds nothing audible; Adler part 1 PDF 210: throat F4-A flat4 'rather pale')  % c014: clarinets with the trumpets in unison, under the oboes (Rimsky-Korsakov PDF 106; natural order PDF 67)
}
bSecClTwo = {
  R1*8 | R1*8 |
  R1*4 |
  \partCombineApart des'2\mp\< bes'2~ | bes'4 ges'4 aes'4 ces''4 | bes'2\f r2 | aes'1\< \breathe |  % c049: rests at 59 b3-4 (was D flat5, over the theme's B flat4 at b4); breath before the swell at 60  % c047: 57 b3-59 an octave higher with clarinet 1 (see there); B flat4 held into 58 (vi7), no B flat-A flat octaves with the violas' arpeggio bass; C flat5 (7th of V7/IV) resolves to B flat4 at 59  % c032: A flat4, not a second C under the melody's leading tone before the D flat climax (A&S PDF 266, 286); resolves to F4
  \partCombineAutomatic aes'2--\ff des''2-- | bes'2-- ces''2-- | R1*2 |  % c084: clarinet 1's former line (A flat4 held from 60, then clarion D flat5, B flat4-C flat5 with horn 3); was F4 | G flat4-A flat4, all throat tones in unison with horn 2  % c014: was F3 inside the trombones
}
bSecBassCl = {
  des'2)\p r2 | R1*7 |
  R1*8 | R1*4 |
  f2\p\< ges2 | bes,4 es4 aes,4 des4 | ges2\f g2 | aes,1\< \breathe |  % c033: enters p and catches up by 59 (Rimsky-Korsakov PDF 127). c017: takes the cellos' bass line 57-60
  des1--\ff | ges,2-- fes,2-- | R1*2 |
}
bSecBsnOne = {
  f2\pp r2 | R1*7 |
  R1*8 |
  R1*2 | r2 f2(\p | ges2 f2) |  % c042: G flat3 = the 7th of A-C-E flat-G flat (vii°7 of B flat minor) at 56, upper neighbour to F as Vln II at 39-40 (A&S PDF 377, Ex. 22-6a); d7 A2-G flat3 resolves to P5 B flat2-F3 (PDF 381 box)
  \partCombineApart r1 | r1 | ges2\f es4 fes4 | es1\< \breathe |  % c057: rests 57-58 (was F3-B flat3 | F3-E flat3-E flat3-F3): at 57 b1 F3 was in four parts (B.cl., Bsn 1-2, Vc) and at 58 bassoon 1 re-struck the cello/horn counter-line's notes (Sebesky PDF 12-13, Ex. 1: economy; lighten the lower-middle register so the primary line dominates); joins the counter-line at the f of 59  % c045: apart mode 57-60: each unison prints as one note head with two stems, no single-beat a2 labels (MOLA Ex. 6 PDF 11)
  \partCombineAutomatic f1--\ff | ges2-- aes2-- | R1*2 |
}
bSecBsnTwo = {
  R1*8 |
  bes,1\pp | bes,2 bes,2\< | \after 2. \pp gis,1\mp\> | R1 | R1*4 |
  R1*4 |  % c077: rests 53-56 (was des2 c2 | bes,2 ges,2 | es2 des2 | a,2 bes,4 r4, the cellos' line at pitch): a wind doubling strings at the unison "detracts from the clarity of a line" (Adler part 1 PDF 265-266); the woodwind bass enters fresh at 57 with B.cl., so the choirs are heard apart, then together (PDF 253)
  \partCombineApart f2\mp\< ges2 | bes,4 es4 aes,4 des4 | ges2\f g2 | aes,1\< \breathe |
  \partCombineAutomatic des1--\ff | ges,2-- fes,2-\tweak padding #0.6 -- | R1*2 |  % c065: tenuto clear of the stem end (Gould PDF 55)
}
bSecCbsn = {
  R1*24 |
  des,1--\ff | ges,,2-- fes,,2-- | R1*2 |
}
bSecHnOne = {
  R1*8 | R1*6 | \tag #'score { R1*2 } \tag #'part { \cueDuring #"corAnglaisQ" #UP { <>^\markup \tiny "C.a." R1*2 } } |  % c075: cue in the part (MOLA PDF 5, Ex. 4)
  r2 r4 aes8(\p-\tag #'score ^\markup \bold "1."^\markup \italic "espr." bes8 | des'4.\< f'8 bes'2 | ges'2\mp f'2 | c'2 des'2) \breathe |  % c019: crescendo with the violins; Cl 1 doubles (Rimsky-Korsakov PDF 74-75: wind + horn in unison, finer legato)  % c051: 56 C4-D flat4 (was E flat4-D flat4): the counter-line rises against the theme's C5-B flat4 instead of following it in sixths after its G flat-F-E flat-D flat descent (Sebesky PDF 211-212, Ex. 279-280)
  \partCombineSoloI aes'2(\mp\<-\tag #'score ^\markup \bold "1." ges'2 | f'4 es'2 aes'4) \breathe | ges'2(\f es'4 fes'4 | es'4\< f'4 ges'4. f'8) |  % c082: 58 b4 A flat4, not F4: F was the resolution of the melody's G flat 4-3 suspension sounding under it (A&S PDF 469: suspensions are clearest when the tone of resolution is not in another voice; 42 is already clean); 60 b4 the F is an eighth-note anticipation, so it no longer sits a beat against the violas' G flat (A&S PDF 475)  % c046: breath after 58 (Adler part 1 PDF 292: a loud slurred phrase in a slow tempo needs more breaths; PDF 309: one slur = one breath; matches the cellos' bow change). c025: horn 2 tacet 57-60; force solo so its rests are not printed under horn 1 (Gould PDF 51: parts share a rest)
  \partCombineAutomatic R1*4-\tag #'part \! |  % c075: in horn 1's part the crescendo of 60 ended nowhere and ran through the rests to 65; part-only, so the combiner is unchanged  % c046: horn 1 rests 61-66 before its exposed p solo at 67 (Adler part 1 PDF 292, 303: rests for the lips; the high line goes to horn 3, a high horn)
}
% c024: horn 2's first entry is the ff of 61, not mp at 57 (Rimsky-Korsakov PDF 136: brass re-entries pp or ff; mp/mf "colourless");
% its 57-60 notes were in unison with clarinet 1, which keeps them. Brass now enter only at the top of the crescendo (PDF 130).
bSecHnTwo = {
  R1*8 | R1*8 | R1*4 |
  R1*4 |
  f'1--\f | ges'2-- aes'2-- | R1*2 |
}
bSecHnThree = {
  R1*23 | \partCombineSoloII R1 | \partCombineApart % c069 (was Unisono, c064): a2 at 61-62 (horn 4 doubles horn 3). c055: "4." label on horn 4's lone entry at 60 (Adler part 2 PDF 294: each instrument labeled when it enters; App. A PDF 312)
   % c046: horn 3 rests at 60 (its E flat4 doubled horn 1 and the violas) and enters ff on horn 1's top line; held E flat4 -> A flat4 made fifths with the tuba's A flat1 -> D flat2. Horn 4 keeps the p cresc. into 61 (c029)
  aes'1--\f | bes'2-- ces''2-- | \partCombineAutomatic R1*2 |  % c054: brass harmony f, theme (Tpt 1, winds, strings) ff (Adler part 1 PDF 268; part 2 PDF 184, as c044 at 79). c046: horn 3 (high horn, Adler part 1 PDF 303) takes horn 1's top line; its D flat4/F flat4 stays in trumpet 3 (same pitches)
}
bSecHnFour = {
  R1*23 | aes1\p\< |
  % c064: horn 4 doubles horn 3's top line A flat4-B flat4-C flat5 (a2) instead of trombone 1's A flat3/B flat3 and the C flat4. Brass at f:
  % above mf two horns in unison equal one trombone (Adler part 2 PDF 15; Ex. XI-1, PDF 15-16, horns paired at ff/f; PDF 44 and Ex. XI-24,
  % PDF 46: Bartok's horns a2 against single trumpets/trombones). With trumpets tacet (c060) horn 3 alone carried the brass top line at half a trombone's weight.
  aes1--\f | bes2-- ces'2-- | R1*2 |  % c069: horn 4 an octave below horn 3 (A flat3-B flat3-C flat4, trombone 1's notes) instead of a2 up to written G flat5: Adler part 2 PDF 26 (Schuller) - two horns in unison high and loud crack; give such lines to one high horn. Horn 3 (high horn) keeps the top line; it is a harmony voice, not the melody (PDF 159 rule 1, PDF 172).
}
% c060: trumpets tacet in movement II. Their only notes (61-62) doubled pitches already in Cl 1, Ob 1, Vln II, Hn 2-3 and the violas
% (Sebesky PDF 12-13 economy; PDF 11 delay a colour for its entrance). Movement III's chorale arrival is to be the first sustained forte
% major chord in trumpets and full brass, and III's D flat episode the forte D flat (cyclic-notes, mvt I cycle 160).
% v60: Tpt 1 aes'2--\ff des''2-- | f''2-- fes''2-- ; Tpt 2 f'1--\ff | bes'2-- ces''2-- ; Tpt 3 des'1--\f | des'2-- fes'2--
bSecTptOne = { R1*28 | }
bSecTptTwo = { R1*28 | }  % c014: the major 7th G flat-F at 62 split between horns and trumpet (Rimsky-Korsakov PDF 102-103)
bSecTptThree = { R1*28 | }
bSecTbnOne = {
  R1*23 | R1 |  % c069: trombone 1 rests 60-62 so its first sound in the movement is the quotation at 63 (Adler part 2 PDF 37: a colour held back for a specific event; PDF 156: a rest before a colour enters). Its A flat3/B flat3 go to horn 4. Trombone 2, bass trombone and tuba keep the c039 entry.
  \tag #'score { R1*2 } \tag #'part { \cueDuring #"bassTbnQ" #DOWN { <>^\markup \tiny "B.tbn." R1*2 } } |  % c075: cue in the part (MOLA PDF 5, Ex. 4)
  r8 e8->\ff^\markup \italic "marcato" c'4.-> b8 bes8 a8 | a4 gis8 a8 f4.->\> e8\mf |  % c028: dim. after the last accent (Dvorak 9/ii Largo: the quotation steps ff to f; Adler part 2 PDF 503 sf > pp)
}
bSecTbnTwo = { R1*23 | es1\pp\< | f1--\mf | ges2-- aes2-- | R1*2 | }
bSecBassTbn = { R1*23 | aes,1\pp\< | des1--\mf | ges,2-- fes,2-- \breathe | a,1\f | a,2\> d,4 e,4\p | }
bSecTuba = { R1*23 | aes,,1\pp\< | des,1--\mf |  % c076: mf with horns f (Rimsky-Korsakov PDF 41: horn marks one degree stronger than trombones and tuba)
  ges,,2-- fes,,2-- | R1*2 | }
bSecTimp = {
  R1*15 | aes,1:32\pp\< |
  aes,4\p r4 r2 | R1*5 |
  R1 | aes,2.:32\p\<~ aes,8\f r8 |  % c056: roll ends on a tied stroke with a target dynamic (Adler part 2 PDF 80, Ex. XII-47)
  des1:32\f | des2:32 aes,4:32~ aes,8 r8 | R1*2 |  % c084: f, not ff, level with the horns (c069 finding 4; Casanelles PDF 290: a sustained, constant-level sound is perceptually more present and thicker than a struck one; Adler part 2 PDF 184)  % c056: A flat (= G sharp) roll ends and is damped before the A minor downbeat at 63 (Adler part 2 PDF 58, 80)
}

bSecVlnOne = {
  R1*8 |
  R1*4 | R1*3 | r2 r4 c''4(\p^\markup \italic "senza sord., sul A" |  % c071: pickup C5-F5 (rising fourth), as flute 1 at 36-37
  % c041: 45-47 theme B head to oboe 1; the first violins rest 37-52 and re-enter fresh at 53
  f''2\< ges''8 f''8 es''4) | des''4( c''8 des''8 es''2)\mp | ges''4(\< \tuplet 3/2 4 { f''8 ges'' f'' } es''4 des''4) | c''4(\mf des''8 c''8 bes'2) |
  aes''4(\<^\markup \italic "ord." des'''4) f'''4.( ges'''8 | aes'''4 bes'''8 aes'''8) ges'''4(~ ges'''8 f'''8) | es'''4.(\f f'''8) des'''4( bes''4) | c'''1\< |
  des'''1--\ff^\markup \italic "molto sostenuto" | f'''2-- fes'''2-- |  % c059: non div. at the ff arrival (Adler part 1 PDF 152: divisi weakens the first violin line); the held A flat6 goes to flute 1  % c051: div. at the ff arrival: the upper half holds A flat6 (fifth of D flat, ninth of G flat, third of F flat) above the augmented head, so the B section's registral peak falls on its held climax and not on the passing eighth B flat6 at 58 (Sebesky PDF 223; c031 option, but held: B flat6-A flat6 here doubled horn 3 and trombone 1's A flat-B flat in octaves and pre-empted the B flat6-A flat6 of 79-80). The lower half keeps D flat6 on the downbeat, so the leading tone C6 of bar 60 still resolves in its own line (c039); A flat5 and F5 stay in Fl, Ob, Cl, Vln II
  << { a'''1:32\sf\>^\markup \italic "div." } \\ { e'''1:32 } >> | e'''2:32\p^\markup \italic "unis." r2 |  % c052: the upper half's A flat6 (= G sharp6, leading tone of A minor over F flat = E) rises to A6 instead of leaping a diminished 4th to E6 (A&S PDF 406-407, 439)  % c024: double stop fills the upper octave of the tutti chord (Rimsky-Korsakov appendix PDF 505: violins in 2-4-note chords at the top)  % c034: top note on the theme's A flat5-D flat6 with the flutes, so the upper octave of the augmented head is in the same instruments for all four notes (Adler part 2 PDF 151, Mozart 40/iv); c024's F5-D flat6 kept on beat 3
}
bSecVlnTwo = {
  <des' f'>1\pp\strMark "D" \markup { "Poco più mosso (" \fontsize #-2 \general-align #Y #DOWN \note {4} #1 "= 60)" }^\markup \italic "senza sord., div., sul tasto" | <des' ges'>2 <bes ges'>2 | <des' ges'>2 <des' f'>2 | <es' ges'>2 <des' f'>2 |
  % c027: Vln II tacet 41-44 when the cor anglais takes theme B's lower octave: its chord (B flat3-G flat4) lay on the cor anglais'
  % own notes (D flat4 at 41, F4 at 42, D flat4 at 43, C4 at 44) and repeated the viola triplets' harmony (Adler part 2 PDF 274:
  % keep the accompaniment registrally distant from a woodwind soloist; the same reason c021 gave for keeping the cor anglais out of 37-40).
  R1*4 |
  f'1\pp\strMark "E" \markup \null ^\markup \italic "unis., ord." | f'2 ges'2\< |  % c044: F4/G flat4, not D flat4: the held note no longer sits on the cellos' theme head D flat4 at 45 and 46 b3 (Adler part 2 PDF 159 rule 1, PDF 165: unison doubling of a harmony note with the melody loses its colour)
  \after 2 -\tag #'score ^\markup \italic "poco rit." \after 2. \pp eis'1\mp\> | fis'2-\tag #'score ^\markup \italic "poco sostenuto" fis''2 | fis''2 g''4 eis''4 |  % c059: the leading tone E sharp4 of 47 resolves to F sharp4 in place; the octave shift waits for 48 b3, under the cor anglais' held A4  % c054: 48-52 an octave higher, clear of the cor anglais quotation (unison F sharp4 at 49; Adler part 1 PDF 241-243)  % c048: tempo words above the strings while Vln I rests (c045 practice)
  fis''2 d''2 | es''1 | es''2.\< c''4(\p^\markup \italic "sul A" |  % c071: pickup with Vln I  % c032: D4 at 50 b3 removes the F sharp4/B1 to E flat4/A flat1 fifths and the F sharp-E flat augmented 2nd (A&S PDF 266-267). c027: 49 held through b2-3, so only the bass moves with the oboe's D5 (Adler part 2 PDF 279: Bizet keeps the accompaniment rhythmically apart from the solo)
  f''2\< ges''8 f''8 es''4) | des''4( c''8 des''8 es''2)\mp | ges''4(\< \tuplet 3/2 4 { f''8 ges'' f'' } es''4 des''4) | c''4(\mf des''8 c''8 bes'2) |
  aes'4(\<^\markup \italic "ord." des''4) f''4.( ges''8 | aes''4 bes''8 aes''8) ges''4(~ ges''8 f''8) | es''4.(\f f''8) des''4( bes'4) | c''1\< |
  aes'2--\ff^\markup \italic "molto sostenuto" des''2-- | f''2-- fes''2-- | <e'' c'''>1:32\sf\>^\markup \italic "non div." | <e'' c'''>2:32\p b4(\>^\markup \italic "sul G" d'4 |  % c083: B3 on 64 b3 completes the diminished seventh G sharp-B-D-F (= A flat-C flat-D-F, vii°7 of V in A flat), so the last chord of the B section is a full pivot chord and not a root-position diminished triad D-F-A flat with D four times (A&S PDF 243: VII 5/3 seldom satisfactory, the missing 6th supplied; PDF 231: one chord, two meanings); D4-D flat4 slip into 65 unchanged
}

bSecVla = {
  \stemDown % c015: one stem direction for the triplet figure (Gould PDF 38-39)
  \tuplet 3/2 4 { aes8(\pp^\markup \italic "senza sord., unis." des' f' des' aes des') } \tuplet 3/2 4 { aes8( des' f' des' aes des') } |
  \omit TupletNumber % c035: numbers on the first bar of each figure only (37, 53, 59); the slurred groups make the rhythm plain after that
  \tuplet 3/2 4 { bes8( des' ges' des' bes des') } \tuplet 3/2 4 { bes8( es' ges' es' bes es') } |  % c052: ii6 (bass G flat), not V7 -> ii7
  \tuplet 3/2 4 { bes8( des' ges' des' bes des') } \tuplet 3/2 4 { bes8( des' f' des' bes des') } |
  \tuplet 3/2 4 { a8( c' es' c' a es') } \tweak TupletNumber.stencil #ly:tuplet-number::print \tuplet 3/2 4 { bes8(\upbow des' f') } r4 |  % c066: beat 4 rest and an up-bow ending at the frog, so the violas have a beat to change from arco to pizz. at 41 (Adler part 1 PDF 54)
  % c057: 41-44 pizz. The cor anglais' lower octave of theme B (A flat3-B flat4) lies in the triplets' own register and attacks their pitches
  % (A flat3, D flat4 at 41; E flat4, D flat4 at 43; C4 at 44): plucked notes decay and leave the solo's held tones alone (Sebesky PDF 13: focus,
  % the background must not divert the ear from the primary element; Rimsky-Korsakov PDF 140: figures to pizz. strings and harp). Arco again at 45.
  \tuplet 3/2 4 { aes8\p\<^"pizz." des' f' des' aes des' } \tuplet 3/2 4 { bes8 des' ges' des' bes des' } |  % c038: shares the cor anglais/flute swell 41-44 (Dvorak 9/ii Largo strings bars 15-16)
  \tuplet 3/2 4 { aes8\mp\> des' f' } \tuplet 3/2 4 { bes8 des' ges' } \tuplet 3/2 4 { ges8 c' es' } \tuplet 3/2 4 { aes8 des' f' } |
  \tuplet 3/2 4 { ges8 bes es' bes ges bes } \tuplet 3/2 4 { aes8 des' es' } \tuplet 3/2 4 { aes8 c' es' } |
  \tuplet 3/2 4 { ges8\p c' es' c' ges c' } r2 |
  % c042: 46 b3 B flat3, so B flat3-B3-A3 is one voice (no B flat2 bassoon / B3 viola split; A&S PDF 394, Ex. 23-12) and the 7th of C sharp7 is prepared
  \stemNeutral f1\pp^"arco" | f2 bes2\< | \after 2. \pp b1\mp\> | a1 | a2 b4 gis4 | a2 d'2 | c'1 | c'1\< |  % c027: 49 A held over the B (iv7), so the upper strings do not move in the quotation's rhythm
  % c049: 53-56 the triplet figure goes to the harp and the violas rest, re-entering at 57 with the crescendo (Rimsky-Korsakov PDF 140: figures
  % of the accompaniment "better partially entrusted to pizz. strings and harp", which have "little chance of overpowering"; PDF 138: a sustained
  % or bowed line covers a melody more than short detached notes; Ex. 289-291, PDF 144 and PDF 118: a repeated idea is rescored by altering
  % details). 37-40 and 53-56 no longer have the same accompaniment, and the build is staged: harp 53, violas 57, sextuplets 59.
  R1*4\! |
  \undo \omit TupletNumber
  \stemDown \tuplet 3/2 4 { aes8(\mp\< des' f' des' aes des') }  % c069: mp, not mf: the figure enters under Fl/Ob p< and violins mf (Adler part 2 PDF 159 rule 1; PDF 184)
   \omit TupletNumber \tuplet 3/2 4 { bes8( des' ges' des' bes des') } |
  \tuplet 3/2 4 { aes8( des' f') } \tuplet 3/2 4 { bes8( des' ges') } \tuplet 3/2 4 { ges8( c' es') } \tuplet 3/2 4 { aes8( ces' f') } |  % c013: V7/IV at 58 b4 (A&S PDF 444-445)
  \undo \omit TupletNumber
  \tuplet 6/4 4 { ges16(\f bes es' bes ges bes es' bes ges bes es' bes) } \tuplet 6/4 4 { bes16( des' es' des' bes des' fes' des' bes des' fes' des') } |  % c029: figure doubles its speed for the last two bars of the animando (Rimsky-Korsakov Ex. 168, PDF 337-338; Ex. 153, PDF 325-328)
  \omit TupletNumber
  \tuplet 6/4 4 { ges16(\< c' es' c' ges c' es' c' ges c' es' c') } \tuplet 6/4 4 { ges16( c' es' c' ges c' ges c' es' ges' es' ges') } |  % c029: last note G flat resolves to the F of the 61 double stop (no C-D flat octaves with Vln I)
  \undo \omit TupletNumber
  \stemNeutral <des' f'>1:32\ff^\markup \italic "non div., molto sostenuto" | <bes des'>2:32 <ces' fes'>2:32 | <c' e'>1:32\sf\> | <c' e'>2:32\p gis2(\> |  % c032: C4-E4 at 63-64 (was E4-A4: fifths and octaves with the bass E-A). c019: 61-64 double stops, not divisi (Rimsky-Korsakov PDF 88)
}

bSecVc = {
  % c079: rests 37-40 (was des4\p pizz. r4 des4 r4 | bes,4 r4 ges,4 r4 | es4 r4 des4 r4 | a,2 bes,2): the pizzicato bass was in three parts on two
  % pitches (Vc D flat3 = harp LH upper note, Cb = harp LH lower note). The basses and harp keep the steady pizzicato bass; the cellos enter arco
  % at 41 as an independent part, fresh after a rest (Adler part 2 PDF 205, Brahms Hungarian Dance 1: "the steady pizzicato bass and the independent
  % cello part"; PDF 228, Stravinsky: a colour rested so its entrance is fresh; PDF 213, Dvorak: a delayed entrance clarifies).
  R1*4 |
  % c037: 41-44 the cellos leave the pizzicato bass (basses + harp keep it) and hold a slow arco tenor line under the cor anglais:
  % the sustained "harmonic counterpoint" under a soft melody and light accompaniment (Adler part 2 PDF 209, Dvorak Slavonic Dance 8),
  % the held residue of the viola arpeggio (PDF 230, Schoenberg-Brahms item 2) and a cello part independent of the pizzicato bass
  % (PDF 205, Brahms Hungarian Dance 1). D flat3-E flat3 lies below the cor anglais (A flat3-B flat4), the register c027 cleared of Vln II.
  des1(\pp\<^\markup \italic "senza sord." | des4\p\> bes,4 c4 des4) | bes,2(\pp es2~ | es2) r4 \clef tenor aes4(\p |  % 42: contrary motion to the cor anglais and flute on every beat; no doubled seventh with the violas
  % c011: cellos in octaves below Vln I on the A and D strings (Rimsky-Korsakov PDF 56, 60-61, Ex. 29-30); bass to Bsn 2 + Cb.
  des'2 es'8 des'8 c'4) | bes4( aes8 bes8 des'2\<) | cis'2.\mf\> r4\! | \clef bass cis1\pp | fis4 b,2 cis4 | fis2 b,2 | es1 | es1\< |  % c042: E flat3, not a second G flat (the 7th) that leapt to D flat3 at 53; the cor anglais' A flat-G flat-F is the passing 7th and its resolution (A&S PDF 375, 377)
  des2\p\< c2 | bes,2 ges,2\mp | es2\< des2 | a,2\mf bes,2 |
  % c017: cellos double horn 1's counter-line an octave lower from 57 b3 (b1 stays on the bass: no B flat-A flat octaves with Vln I at 56-57) (Adler PDF 177-178: Meistersinger, cellos with Horn I); bass to B.cl., Bsn 2, Cb.
  f2\< ges2(^\markup \italic "espr." | f4) es2( aes4) | ges2(\f es4 fes4) | es4(\< f4 ges4. f8) |  % c082: as horn 1 (58 b4 A flat3; 60 b4 anticipation)
  aes2--\ff^\markup \italic "molto sostenuto" des'2-- | f'2-- fes'2-- | a,1:32\sf\> | a,2:32\p d4( e4) |  % c074: tremolo A2, not A3: A3 lay inside trombone 1's quotation (E3-C4), in unison with its A3 and a semitone from its B flat3/G sharp3 (Adler part 1 PDF 144: theme and accompaniment separated registrally; PDF 161, Ex. V-37: Bizet's tremolo kept clear of the tune's register)
}
bSecCb = {
  des,4\p^"pizz."^\markup \italic "senza sord." r4 des,4 r4 | bes,,4 r4 ges,,4 r4 | es,4 r4 des,4 r4 | a,,2 bes,,2 |
  f,4 r4 ges,4 r4 | bes,,4 es,4 aes,,4 des,4 | ges,4 r4 aes,4 r4 | aes,,4 r4 r2 |
  bes,,1\pp^"arco" | bes,,2 ges,,2\< | \after 2. \pp cis,1\mp\> | fis,1 | fis,4 b,,2 cis,4 | fis,2 b,,2 | aes,,1 | aes,,1\< |
  des,2\p\< c,2 | bes,,2 ges,,2\mp | es,2\< des,2 | a,,2\mf bes,,2 |
  f,2\< ges,2 | bes,,4 es,4 aes,,4 des,4 | ges,2\f g,2 | aes,,1\< |
  des,1--\ff^\markup \italic "molto sostenuto" | ges,,2-- fes,,2-- | a,,1\sf\> | a,,2\p d,4 e,4 |
}

% c026: harp doubles the pizzicato bass 37-44 (Adler part 1 PDF 117: harp as a doubling instrument; PDF 113-114: low two octaves dark and sonorous).
% Pedals: G to G flat during the rests 15-36 (diagram at 37); A natural for bar 40 (right foot, during the rest at 39 b4), back to A flat during 40 b3-42 b2;
% G flat back to G natural during 57-70 (c049: after the harp figure at 53-56) (diagram at 71). One pedal per foot at a time (Adler part 1 PDF 112-113).
% c049: 53-56 the harp takes the violas' triplet figure (pitches as the violas had them in v49). Pedals as at 37 (D flat, C, B flat | E flat, F,
% G flat, A flat); A flat to A natural during 55 b3-4 for 56 b1-2 (right foot), and back to A flat during 57-70.
bSecHarpR = {
  R1*16 |
  \tuplet 3/2 4 { aes8\p-\tag #'score ^\markup \small \harp-pedal #"^-^|^-^^" des' f' des' aes des' } \tuplet 3/2 4 { aes8 c' es' c' aes es' } |
  \omit TupletNumber
  \tuplet 3/2 4 { bes8 des' ges' des' bes des' } \tuplet 3/2 4 { bes8 es' ges' es' bes es' } |
  \tuplet 3/2 4 { bes8\mp des' ges' des' bes des' } \tuplet 3/2 4 { bes8 des' f' des' bes f'-\tag #'score _\markup \small "A♮" } |
  \tuplet 3/2 4 { a8 c' es' c' a es' } \tuplet 3/2 4 { bes8 des' f' des' bes des' } |
  \undo \omit TupletNumber
  R1*4 | R1*4 |
}
bSecHarpL = {
  <des, des>4\p-\tag #'score ^\markup \small \harp-pedal #"^-^|^-^^" r4 <des, des>4 r4 | <bes,, bes,>4 r4 <ges,, ges,>4 r4 | <es, es>4 r4 <des, des>4 r4-\tag #'score _\markup \small "A♮" | <a,, a,>2 <bes,, bes,>2-\tag #'score _\markup \small "A♭" |
  <f, f>4 r4 <ges, ges>4 r4 | <bes,, bes,>4 <es, es>4 <aes,, aes,>4 <des, des>4 | <ges, ges>4 r4 <aes, aes>4 r4 | <aes,, aes,>4 r4 r2 |
  R1*20 |
}
