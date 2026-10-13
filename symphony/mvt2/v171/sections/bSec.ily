% B SECTION, bars 37-64 (Poco più mosso, 4/4), D flat major.
% 37-44 B1: new theme in flute 1 alone (37-40), then the cor anglais with flute 1 in tenths and sixths (41-44, c021/c090),
%          over viola triplets (pizz. 41-44) and the pizzicato bass with harp.
%          It opens with a rising fourth. c120: bars 42 and 58 are a diatonic turn over ii7 (A flat-B flat-A flat-G flat-F, accepted in cycle 11
%          to reduce the tail count), not the motto's tail; the tail statements are 8, 24, 33, 63 (in the quotation), 68, 72, 85-89.
% 45-52 B2: the theme's head in B flat minor (oboe 1, cellos an octave lower, c041), D flat 7 = C sharp 7, then F sharp minor (= G flat minor):
%          the cor anglais (since c040; oboe 1 plays theme B's B flat minor head at 45-47) quotes the movement I second-theme head
%          in minor with its pickup (cyclic-notes §3), once, 47 b4-50.
%          G sharp 7 respelled A flat 7 leads back to D flat.
% 53-60 B3: the theme in both violin sections (unison at 53-56, octaves from 57), horn 1 counter-melody from the A theme's head;
%          woodwinds and horns join for the crescendo.
% 61-64 B4: climax on D flat (61), G flat to F flat (= E major) (62), then A minor: trombone 1 quotes the
%          movement I first-theme head once, ff, in a foreign key (cyclic-notes: Dvořák 9/ii 96-98 model).

bSecFluteOne = {
  f''2(\p\<^\markup \italic "dolce cantabile" ges''8 f''8 es''4\! | des''4\> c''8 des''8 es''2)\! | ges''4(\< \tuplet 3/2 4 { f''8 ges'' f'' } es''4\> des''4 | c''4\p des''8 c''8 bes'2) \breathe |  % c036: breath between theme B's two halves (Adler part 1 PDF 188). c031: head rhythm 2 8 8 4 at 37/45/53, so theme B does not open with theme A's 4. 8 (Dvorak 9/ii: bar 7 vs bar 46)
  r2 aes''4.(\pp\< bes''8 | f''4\p ges''8 f''8 es''4~ es''8\> f''8 | ges''4. aes''8 f''4 es''4 | es''2.)\pp r4 |  % c101: one level under the cor anglais (p< mp), so theme B's second phrase, the lower voice of the pair, keeps the lead (Rimsky-Korsakov PDF 54: a melody in the middle register needs relief by dynamic shading)  % c090: flute 1 in tenths and sixths above the cor anglais (41-44), not in octaves: the symphony's first melody in parallel thirds/sixths (cyclic-notes, mvt I c187; Dvorak 9/ii 55-56, clarinets in thirds in the middle section; Adler part 2 PDF 257-258: the repeat of a tune in a different colour; PDF 273: Beethoven Op. 61, melody harmonised by paired woodwinds). Was f''4.( ges''8 | aes''4 bes''8 aes''8 ges''4~ ges''8 f''8 | es''4. f''8 des''4 bes'4 | c''2.)  % c051: flute 1 rests 41 b1-2; the cor anglais starts theme B's second phrase alone in its strong low register and the flute joins on F5 (Sebesky PDF 219: compensate for a soloist's weak register; Adler part 1 PDF 185, 205)  % c061: 42 b3-4 the 7th G flat of A flat7 is held into the D flat chord as a 4-3 (A&S PDF 359-360, Ex. 21-23a: dissonant preparation), the theme's only suspension (also 58)
  R1*8 |
  R1*4 |
  \stemDown aes''4(\p\<-\tag #'score ^\markup \bold "1." des'''4 f'''4. ges'''8 | aes'''4. ges'''8~ ges'''4~ ges'''8 f'''8) \breathe | es'''4.(\f f'''8 des'''4 bes''4 | c'''1)\< \breathe |  % c015: Fl 2 rests, so stems follow the notes (Gould PDF 38); the combiner keeps voice one here  % c151: 58 A flat6 dotted quarter, G flat6 from b2.5 tied over b3: the A flat over the ii7 bass E flat now resolves on the weaker half of b2, and G flat (3rd of ii7) is held as the prepared 7th of V7 and the 4-3 over D flat (A&S PDF 347, 357-358, 364, 369)
  % c110: 58 top octave holds A flat6 (was aes'''4 bes'''8 aes'''8): the B section's ceiling stays A flat6/A6 (61-63) and B flat6 is first heard in A' (76, 79), the movement's peak above movement I's A flat6 (A&S PDF 600-601: register and key plan project the motive; Ob 1/Vln II keep the B flat turn an octave lower; the G flat-F 4-3 suspension is unchanged)
  \stemNeutral aes'''1--~\ff | aes'''1( | a'''4) \tweak staff-position #0 r4 \tweak staff-position #0 r2 | R1 |  % c070: the top voice's G sharp6 (A flat6) resolves to A6 in the flute that holds it, with the violins' A6, instead of stopping while the violins take the A (A&S PDF 394, Ex. 23-12: a chromatic succession split between voices)  % c059: flute 1 holds the A flat6 the upper half of Vln I had; flute 2 keeps the augmented head  % c021: a2 with flute 2
}
% c021: flute 2 joins flute 1 in unison on theme B's augmented head at the climax, so the upper octave of trumpet 1's
% A flat-D flat-F-F flat has two flutes (Rimsky-Korsakov PDF 75: "in the top register two flutes will suffice").
bSecFluteTwo = {
  R1*8 | R1*8 | R1*6 | \tag #'score { s1*2 } \tag #'part { \cueDuring #"oboeOneQ" #UP { <>^\markup \tiny "Ob. 1" R1*2 } } |  % c155: score spacer, as c115 at 63: the second player's whole rest at 59 sat on player 1's down-stems (Gould PDF 50: rests move clear of the other part; PDF 51: shared rests)  % c135: cue in the part before the entry after a long rest (MOLA PDF 5: logical, audible cues during long rests)
 
  aes''2--(\ff des'''2-- | f'''2-- fes'''2--) | \tag #'score s1 \tag #'part R1 | R1 |  % c115: in the score flute 2's tacet bar 63 is a spacer, so flute 1's rests are the only ones (Gould PDF 51: parts share a rest wherever possible)
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
  des''2 es''8 des''8 c''4) | bes'4( a'8 bes'8 des''2\<) | cis''2.\mf\> r4\! |
  R1*9 |  % c040: the movement I quotation 47-53 is in the cor anglais (see bSecCorAnglais)
  \stemDown aes'4(\p\<-\tag #'score ^\markup \bold "1." des''4 f''4. ges''8 | aes''4. ges''8~ ges''4~ ges''8 f''8) \breathe | es''4.(\f f''8 des''4 bes'4 | c''1)\< \breathe |  % c119: 58 holds A flat5 like Fl 1/Vln I's A flat6 (c110), so the two octaves of theme B match; B flat waits for A'  % c151: as Fl 1 at 58 (A&S PDF 347, 357-358)  % c166: breath after 58 with flute 1 and horn 1; 57-60 was about 15.5 s in one breath, p to f (Rimsky-Korsakov PDF 37, 44)
  \stemUp f''1--(\ff | f''2-- fes''2--) | R1*2 |  % c014: oboe 1 above the trumpets at 61 (Rimsky-Korsakov PDF 110-111)
}
bSecOboeTwo = {
  R1*8 | R1*8 | R1*6 | \tag #'score { s1*2 } \tag #'part { \cueDuring #"oboeOneQ" #UP { <>^\markup \tiny "Ob. 1" R1*2 } } |  % c155: score spacer, as c115 at 63: the second player's whole rest at 59 sat on player 1's down-stems (Gould PDF 50: rests move clear of the other part; PDF 51: shared rests)  % c135: cue in the part before the entry after a long rest (MOLA PDF 5: logical, audible cues during long rests)
 
  des''1--\ff | des''2-- aes'2-- | R1*2 |  % c086: A flat4, not F flat5 in unison with oboe 1 (Sebesky PDF 71, 80). c047: D flat5 held at 61 (was A flat4-D flat5 with trumpet 1, clarinet 1, horn 3 and Vln II): with oboe 1's F5 and the flutes' A flat5 the double reeds complete the D flat chord above the trumpets (Rimsky-Korsakov PDF 110-111), filling A flat4-F5. c014: was F4 = Tpt 2 + Hn 2
}
% c009: the lower octave of theme B goes to the cor anglais (Rimsky-Korsakov Ex. 57: Fl / Eng. horn in octaves).
% c021: 37-40 flute 1 alone (Rimsky-Korsakov PDF 66-67: an intimate melody to a solo instrument of simple timbre;
% doubling where the expression broadens); the lower octave would sit in unison with the Vln II chord tones F4, D flat4, G flat4.
% The cor anglais joins at 41 with the crescendo.
bSecCorAnglais = {
  f''4) r4 r2 | R1*3 |  % c139: the pickup C5 goes on to F5 in unison with flute 1's first note, so theme B's rising fourth is not split between two instruments (Rimsky-Korsakov PDF 125-126: in a phrase transferred between instruments the last note of one coincides with the first of the next)
  aes4(\p\<^\markup \italic "solo, dolce cantabile" des'4 f'4. ges'8 | aes'4\mp bes'8 aes'8 ges'4~ ges'8\> f'8 | es'4. f'8 des'4 bes4 | c'2.)\p r4 |
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
  r2 r4 aes8(\pp bes8 | des'4.\< f'8 \once \stemUp bes'2 | ges'1\p | c'2 des'2) \breathe |  % c038: one level under horn 1, so the unison is one colour (Casanelles PDF 147-148). c019: unison with Hn 1's counter-line, which the viola triplets cover in the same register  % c051: 56 C4-D flat4 (was E flat4-D flat4): the counter-line rises against the theme's C5-B flat4 instead of following it in sixths after its G flat-F-E flat-D flat descent (Sebesky PDF 211-212, Ex. 279-280)
  \partCombineApart r2 des''2\mp\< | des''2 c''4 des''4 | es''2\f r2 | c''1\< \breathe |  % c049: rests at 59 b3-4 (was E flat5, held over the theme's lower octave D flat5-B flat4 in Ob 1 and Vln II; Rimsky-Korsakov PDF 133, 157); both clarinets re-enter on the V7 swell at 60  % c047: 57 b3-59 an octave higher, above horn 1: the clarinets fill the empty F4-A flat5 space under the theme's lower octave instead of crowding A flat3-F4 with the violas and bassoon (Rimsky-Korsakov PDF 108: a horn chord is completed by clarinets in the upper register, clarinets rarely inside the horns; PDF 108-109: forte, double the upper harmonic parts); also no E flat4-C5 leap into 60  % c045: apart mode 57-60 (no a2 label on the single unison at 57 b3)  % c147: rest at 57 b1-2 (was F4, with clarinet 2's D flat4): the clarinets enter on b3 above horn 1, so they complete the chord in the upper register from their first note and no longer double the viola triplets' D flat4/F4 under the horn (Rimsky-Korsakov PDF 108)
  \partCombineAutomatic f''1--\ff~ | f''2 aes''2-- | R1*2 |  % c167: 62 b1-2 F5 held (was G flat5): G flat5 over Ob 1/Vln II F5 was the movement's only adjacent second above E5 (Sebesky PDF 139, rule 5, Ex. 190-192: seconds strident as the chord rises, keep them in the lower-middle register); the G flat-F major seventh stays in Hn 2 G flat4 over Vc/Bsn 1 F4  % c084: clarion F5-G flat5-A flat5 (written G5-A flat5-B flat5), following oboe 1's C5-F5 and doubling horn 2 / trombone 2 two octaves up; was A flat4-D flat5 | B flat4-C flat5, now in clarinet 2 (Casanelles PDF 257, 275: each register its own strength; PDF 277-278: a weak unison doubling adds nothing audible; Adler part 1 PDF 210: throat F4-A flat4 'rather pale')  % c014: clarinets with the trumpets in unison, under the oboes (Rimsky-Korsakov PDF 106; natural order PDF 67)
}
bSecClTwo = {
  R1*8 | R1*8 |
  R1*4 |
  \partCombineApart r2 bes'2~\mp\< | bes'4 ges'4 aes'4 ces''4 | bes'2\f r2 | aes'1\< \breathe |  % c049: rests at 59 b3-4 (was D flat5, over the theme's B flat4 at b4); breath before the swell at 60  % c047: 57 b3-59 an octave higher with clarinet 1 (see there); B flat4 held into 58 (vi7), no B flat-A flat octaves with the violas' arpeggio bass; C flat5 (7th of V7/IV) resolves to B flat4 at 59  % c032: A flat4, not a second C under the melody's leading tone before the D flat climax (A&S PDF 266, 286); resolves to F4
  \partCombineAutomatic aes'2--\ff des''2-- | bes'2-- ces''2-- | R1*2 |  % c084: clarinet 1's former line (A flat4 held from 60, then clarion D flat5, B flat4-C flat5 with horn 3); was F4 | G flat4-A flat4, all throat tones in unison with horn 2  % c014: was F3 inside the trombones
}
bSecBassCl = {
  des2)\p r2 | R1*7 |  % c140: D flat3 (was D flat4, with Vln II's D flat4), the end of the lowered solo
  R1*8 | R1*4 |
  f2\p\< ges2 | bes,4 es4 aes,4 \once \stemUp des4 | ges,2\f g,2 | aes,1\< \breathe |  % c033: enters p and catches up by 59 (Rimsky-Korsakov PDF 127). c017: takes the cellos' bass line 57-60
  des1--\ff | ges,2-- fes,2-- | R1*2 |
}
bSecBsnOne = {
  f2\pp r2 | R1*7 |
  % c087: bassoon 1 doubles the cellos' lower octave of theme B's head under oboe 1 (45-47). Oboe over cellos alone was strings and wood-wind in separate
  % octaves, which Rimsky-Korsakov's editor calls "not to be recommended, as the tone quality of the two groups is so widely different" (PDF 78 note);
  % with the bassoon the wood-wind runs in octaves and only the lower part is doubled by a string group (PDF 78), and "a bassoon with the 'cellos" is his
  % model of an equal-power unison in which the strings still predominate (PDF 76). Dynamics as bassoon 2 (shared staff). No pickup at 44: the bassoon staff is hidden in 41-44.
  des'2(\pp es'8 des'8 c'4) | bes4( a8 bes8 des'2\<) | cis'2.\p\> r4\! | R1*5 |
  R1 | des1~(\pp | des2 \once \stemDown c2 | ges2 f2) |  % c107: enters at 54 under the harp's arpeggio (Adler part 1 PDF 136: Brahms 3/iii, the bassoons 'clarify and support the arpeggiated harmony'; PDF 143, Ex. V-34: sustained harmony under an arpeggiated figure); D flat3 = 5th of IV6, 7th of ii6/5 and ii7, held to 55 b3  % c042: G flat3 = the 7th of A-C-E flat-G flat (vii°7 of B flat minor) at 56, upper neighbour to F as Vln II at 39-40 (A&S PDF 377, Ex. 22-6a); d7 A2-G flat3 resolves to P5 B flat2-F3 (PDF 381 box)
  % c145: 57-58 bassoon 2 alone with a score-only "2." label; bassoon 1 has spacers in the score, rests in its part (was r1 r1 in bassoon 1, which drew a whole rest on a ledger line above the staff at 57 and no player label; Adler part 2 PDF 294: each instrument labelled when it enters; App. A PDF 312: "1., 2.")
  \partCombineApart \tag #'score { s1*2 } \tag #'part { R1*2 } | ges2\f es4( fes4 | es4\< f4 ges4. f8) \breathe |  % c117: 60 follows the counter-line with Hn 1 and Vc (was es1): the line keeps its woodwind-brass-string colour into 61 (Adler 2 PDF 176: keep an established colour long enough; PDF 178: string + woodwind + brass per element)  % c057: rests 57-58 (was F3-B flat3 | F3-E flat3-E flat3-F3): at 57 b1 F3 was in four parts (B.cl., Bsn 1-2, Vc) and at 58 bassoon 1 re-struck the cello/horn counter-line's notes (Sebesky PDF 12-13, Ex. 1: economy; lighten the lower-middle register so the primary line dominates); joins the counter-line at the f of 59  % c045: apart mode 57-60: each unison prints as one note head with two stems, no single-beat a2 labels (MOLA Ex. 6 PDF 11)
  \partCombineAutomatic f2--\ff des'2-- | f'2-- fes'2-- | R1*2 |  % c087: F3 on 61 b1-2 (E flat3-A flat3 here made fifths with bassoon 2 and the bass, A flat-D flat), then the augmented head with the cellos from 61 b3 (was F3 | G flat3-A flat3, a unison with trombone 2, also in horn 2 and clarinet 1): the head's lowest octave was the cellos alone among the brass, and strings and brass "can never yield such a perfect blend" (Rimsky-Korsakov PDF 79); 'Cellos + Fag. is his natural unison (PDF 76-77), and a melody spread over three octaves is hard to balance (PDF 76)
}
bSecBsnTwo = {
  R1*8 |
  bes,1(\pp | bes,2-- bes,2--\< | \after 2. \pp gis,1)\p\> |  % c126: one breath, repeated B flat soft-tongued (Adler part 1 PDF 177, Ex. VI-7)
  R1 | R1*4 |  % c108: winds p, strings fp on the C sharp 7 (Rimsky-Korsakov PDF 129)
  R1*4 |  % c077: rests 53-56 (was des2 c2 | bes,2 ges,2 | es2 des2 | a,2 bes,4 r4, the cellos' line at pitch): a wind doubling strings at the unison "detracts from the clarity of a line" (Adler part 1 PDF 265-266); the woodwind bass enters fresh at 57 with B.cl., so the choirs are heard apart, then together (PDF 253)
  \partCombineApart f2\p\<-\tag #'score ^\markup \bold "2." ges2 | bes,4 es4 aes,4 des4 | ges,2\f g,2 | aes,1\< \breathe |
  \partCombineAutomatic des1--\ff | ges,2-- fes,2-\tweak padding #0.6 -- | R1*2 |  % c065: tenuto clear of the stem end (Gould PDF 55)
}
bSecCbsn = {
  % c165: Vc cues here and for Tbn 2, B.tbn, Tuba at 58-59 now #UP: with #DOWN the part's own whole rest sat on the top line among the cue notes (MOLA PDF 8, Ex. 7: collisions in extracted parts)
  R1*22 | \tag #'score { R1*2 } \tag #'part { \cueDuring #"vcQ" #UP { <>^\markup \tiny "Vc." R1*2 } } |  % c135: cue in the part before the entry after a long rest (MOLA PDF 5: logical, audible cues during long rests)
 
  des,,1--\ff | ges,,2-- fes,,2-- | R1*2 |
}
bSecHnOne = {
  R1*8 | R1*6 | \tag #'score { R1*2 } \tag #'part { \cueDuring #"corAnglaisQ" #UP { <>^\markup \tiny "C.a." R1*2 } } |  % c075: cue in the part (MOLA PDF 5, Ex. 4)
  r2 r4 aes8(\pp-\tag #'score ^\markup \bold "1."^\markup \italic "espr." bes8 | des'4.\< f'8 \once \stemUp bes'2 | ges'1\mp | c'2 des'2) \breathe |  % c019: crescendo with the violins; Cl 1 doubles (Rimsky-Korsakov PDF 74-75: wind + horn in unison, finer legato)  % c051: 56 C4-D flat4 (was E flat4-D flat4): the counter-line rises against the theme's C5-B flat4 instead of following it in sixths after its G flat-F-E flat-D flat descent (Sebesky PDF 211-212, Ex. 279-280)
  \partCombineSoloI aes'2(\mp\<-\tag #'score ^\markup \bold "1." ges'2 | f'4 es'2~ es'8 f'8) \breathe | ges'2\f es'4( fes'4 | es'4\< f'4 ges'4. f'8) |  % c158: G flat detached, slur from E flat, as Bsn 1 and the cellos play the same line (Sebesky PDF 213-215, Ex. 281: one figure, one articulation in every part)  % c082: 58 b4 A flat4, not F4: F was the resolution of the melody's G flat 4-3 suspension sounding under it (A&S PDF 469: suspensions are clearest when the tone of resolution is not in another voice; 42 is already clean); 60 b4 the F is an eighth-note anticipation, so it no longer sits a beat against the violas' G flat (A&S PDF 475)  % c046: breath after 58 (Adler part 1 PDF 292: a loud slurred phrase in a slow tempo needs more breaths; PDF 309: one slur = one breath; matches the cellos' bow change). c025: horn 2 tacet 57-60; force solo so its rests are not printed under horn 1 (Gould PDF 51: parts share a rest)  % c151: 58 b4 E flat4 held to b4.5 (was F4 on b4): the F no longer sounds under the melody's G flat-F suspension, and the held E flat is oblique to the bass A flat-D flat, so no fifths (A&S PDF 352, 356-359, 365-366; c082, c089)
  \partCombineAutomatic R1*4-\tag #'part \! |  % c075: in horn 1's part the crescendo of 60 ended nowhere and ran through the rests to 65; part-only, so the combiner is unchanged  % c046: horn 1 rests 61-66 before its exposed p solo at 67 (Adler part 1 PDF 292, 303: rests for the lips; the high line goes to horn 3, a high horn)
}
% c024: horn 2's first entry is the ff of 61, not mp at 57 (Rimsky-Korsakov PDF 136: brass re-entries pp or ff; mp/mf "colourless");
% its 57-60 notes were in unison with clarinet 1, which keeps them. Brass now enter only at the top of the crescendo (PDF 130).
bSecHnTwo = {
  R1*8 | R1*8 | R1*4 |
  \tag #'score { R1*4 } \tag #'part { \cueDuring #"hnOneQ" #UP { <>^\markup \tiny "Hn. 1" R1*4 } } |  % c135: cue in the part before the entry after a long rest (MOLA PDF 5: logical, audible cues during long rests)
  f'1--\f | ges'2-- aes'2-- | R1*2 |
}
bSecHnThree = {
  R1*20 | \tag #'score { R1*3 } \tag #'part { \cueDuring #"hnOneQ" #UP { <>^\markup \tiny "Hn. 1" R1*3 } } |  % c135: cue in the part before the entry after a long rest (MOLA PDF 5: logical, audible cues during long rests)
  \partCombineSoloII R1 | \partCombineUnisono % c086: a2 61-62. c069 (was Unisono, c064): a2 at 61-62 (horn 4 doubles horn 3). c055: "4." label on horn 4's lone entry at 60 (Adler part 2 PDF 294: each instrument labeled when it enters; App. A PDF 312)
   % c046: horn 3 rests at 60 (its E flat4 doubled horn 1 and the violas) and enters ff on horn 1's top line; held E flat4 -> A flat4 made fifths with the tuba's A flat1 -> D flat2. Horn 4 keeps the p cresc. into 61 (c029)
  aes'1--\f | bes'2-- ces''2-- | \partCombineAutomatic R1*2 |  % c054: brass harmony f, theme (Tpt 1, winds, strings) ff (Adler part 1 PDF 268; part 2 PDF 184, as c044 at 79). c046: horn 3 (high horn, Adler part 1 PDF 303) takes horn 1's top line; its D flat4/F flat4 stays in trumpet 3 (same pitches)
}
bSecHnFour = {
  R1*20 | \tag #'score { R1*3 } \tag #'part { \cueDuring #"hnOneQ" #UP { <>^\markup \tiny "Hn. 1" R1*3 } } |  % c135: cue in the part before the entry after a long rest (MOLA PDF 5: logical, audible cues during long rests)
  aes1\p\< \breathe |
  % c064: horn 4 doubles horn 3's top line A flat4-B flat4-C flat5 (a2) instead of trombone 1's A flat3/B flat3 and the C flat4. Brass at f:
  % above mf two horns in unison equal one trombone (Adler part 2 PDF 15; Ex. XI-1, PDF 15-16, horns paired at ff/f; PDF 44 and Ex. XI-24,
  % PDF 46: Bartok's horns a2 against single trumpets/trombones). With trumpets tacet (c060) horn 3 alone carried the brass top line at half a trombone's weight.
  aes'1--\f | bes'2-- ces''2-- | R1*2 |  % c086: a2 with horn 3 (Sebesky PDF 33, 37, 103). c069: horn 4 an octave below horn 3 (A flat3-B flat3-C flat4, trombone 1's notes) instead of a2 up to written G flat5: Adler part 2 PDF 26 (Schuller) - two horns in unison high and loud crack; give such lines to one high horn. Horn 3 (high horn) keeps the top line; it is a harmony voice, not the melody (PDF 159 rule 1, PDF 172).
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
  % c136: "solo" in the trombone 1 part: its first notes in the movement are the exposed quotation (Adler part 2 PDF 6: the trombone as soloist; the horn solos carry "solo" in their parts)
  r8 \shape #'((0 . 0) (0 . 0) (0 . 0) (-0.7 . -0.9)) Slur e8(\ff^\markup \italic "marcato"-\tag #'part ^\markup \italic "solo" c'4.->) b8 bes8 a8 | a4 gis8( a8) f4.->\> e8\mf |  % c148: pickup unaccented and slurred into the syncopated C4, turn slurred, as every ff statement of the P head in movement I (coda Hn 1 'r8 g8( es'4.->) ... b8( c'8) aes4.->', recOne, dev); an accented pickup weakens the syncopation (A&S PDF 51-52)  % c028: dim. after the last accent (Dvorak 9/ii Largo: the quotation steps ff to f; Adler part 2 PDF 503 sf > pp)
}
bSecTbnTwo = { R1*21 | \tag #'score { R1*2 } \tag #'part { \cueDuring #"vcQ" #UP { <>^\markup \tiny "Vc." R1*2 } } |  % c135: cue in the part before the entry after a long rest (MOLA PDF 5: logical, audible cues during long rests)
  es2\pp\< ges2 \breathe |  % c132: E flat3 on 60 b1-2, the 7th G flat3 enters on b3 with the passing E flat-F-G flat of Bsn 1, Hn 1 and Vc, so the bass G natural of 59 is not followed by G flat in another voice (A&S PDF 377, 394)
   % c119: G flat3, the 7th of V7, resolving to F3 at 61; the low brass at 60 held only A flat and E flat (open fifths/octaves) under the strings' melody (Rimsky-Korsakov PDF 97 no. 4: wind middle parts in seconds, sevenths, thirds or sixths, no open fourths or fifths; PDF 100: brass in close order; Ex. 115, PDF 289: brass enter p with a complete chord)
  f2--\mf aes2-- | bes2-- ces'2-- | R1*2 | }  % c104: F3 on 61 b1-2 (E flat3-A flat3 from 60 made fifths with the bass, c099), then trombone 1's former middle line A flat3-B flat3-C flat4 (c069) an octave under horns 3-4: with trumpets and trombone 1 tacet the brass had an empty octave F3-F4 (61) and G flat3-G flat4 / A flat3-A flat4 (62) between the low brass and the horns (Rimsky-Korsakov PDF 100: brass in close order 'with no empty spaces'; PDF 101: 3rd trombone and tuba the bass in octaves, the upper parts to the other trombones reinforced by horns)
bSecBassTbn = { R1*21 | \tag #'score { R1*2 } \tag #'part { \cueDuring #"vcQ" #UP { <>^\markup \tiny "Vc." R1*2 } } |  % c135: cue in the part before the entry after a long rest (MOLA PDF 5: logical, audible cues during long rests)
  aes,1\pp\< \breathe | des1--\mf | ges,2-- fes,2-- \breathe | a,1\sf\> | a,2\p d,4 e,4 | }  % c154: sf> with the strings' tremolo at 63, so the quotation's only sustained accompaniment does not stay f under trombone 1 while the strings fall to p (Adler part 2 PDF 42-44: the subject in the clear; PDF 50-51, Ex. XI-27: sf>p brass attack introducing a solo)
bSecTuba = { R1*21 | \tag #'score { R1*2 } \tag #'part { \cueDuring #"vcQ" #UP { <>^\markup \tiny "Vc." R1*2 } } |  % c135: cue in the part before the entry after a long rest (MOLA PDF 5: logical, audible cues during long rests)
  aes,,1\pp\< \breathe | des,1--\mf |  % c076: mf with horns f (Rimsky-Korsakov PDF 41: horn marks one degree stronger than trombones and tuba)
  ges,,2-- fes,,2-- | R1*2 | }
bSecTimp = {
  R1*13 | \tag #'score { R1^\markup \small "medium sticks" R1 } \tag #'part { <>^\markup \small "medium sticks" \cueDuring #"vcQ" #DOWN { <>^\markup \tiny "Vc." R1*2 } } |  % c146: medium sticks for the f rolls at 60-62 and 79-81 (Adler part 2 PDF 61, 80, 88: name hard/medium/soft; movement I changes to medium sticks in its tOne)  % c135: cue in the part before the entry after a long rest (MOLA PDF 5: logical, audible cues during long rests)
  aes,1:32\pp\< |
  aes,4\p r4 r2 | R1*5 |
  R1 | aes,2.:32\p\<~ aes,8\f r8 |  % c056: roll ends on a tied stroke with a target dynamic (Adler part 2 PDF 80, Ex. XII-47)
  des1:32\f | des4.:32~ des8 r2^\markup \small \italic "damp" | R1*2 |  % c146: D flat damped at 62 b3 under the F flat chord, before the A minor C natural at 63 (Adler part 2 PDF 58, 80)  % c099: no A flat2 (G sharp) roll under the F flat (E) chord at 62 b3: a major third F flat2-A flat2 below the brass/bass fundamentals (Casanelles PDF 274: the third enters the series only at partials 4-5; PDF 275: the drum's partly inharmonic spectrum)  % c084: f, not ff, level with the horns (c069 finding 4; Casanelles PDF 290: a sustained, constant-level sound is perceptually more present and thicker than a struck one; Adler part 2 PDF 184)  % c056: A flat (= G sharp) roll ends and is damped before the A minor downbeat at 63 (Adler part 2 PDF 58, 80)
}

bSecVlnOne = {
  R1*8 |
  R1*4 | R1*3 | r2 r4 c''4(\p^\markup \italic \override #'(baseline-skip . 2.4) \column { "senza sord., sul A," "cantabile" } |  % c158: the theme's first string statement is marked to sing; the horn counter-line already has "espr." (Sebesky PDF 13-14: focus on the primary element; PDF 17-18)  % c071: pickup C5-F5 (rising fourth), as flute 1 at 36-37
  % c041: 45-47 theme B head to oboe 1; the first violins rest 37-52 and re-enter fresh at 53
  f''2\< ges''8 f''8 es''4) | des''4( c''8 des''8 es''2)\mp | ges''4(\< \tuplet 3/2 4 { f''8 ges'' f'' } es''4 des''4) | c''4(\mf des''8 c''8 bes'2) |
  aes''4(\<^\markup \italic "ord." des'''4) f'''4.( ges'''8 | aes'''4.) ges'''8(~ ges'''4~ ges'''8 f'''8) | es'''4.(\f f'''8 des'''4 bes''4) | c'''1\upbow\< |  % c085: 59 in one bow, so the crescendo at 60 is an up-bow and the ff at 61 a down-bow (Adler part 1 PDF 38: crescendo natural on the up-bow; Ex. II-20 Coriolanus, bowing arranged so the accented attack is down-bow)  % c151: 58 rhythm as Fl 1
  des'''2~--\ff\downbow^\markup \italic "molto sostenuto" des'''2\upbow |  % c118: bow change on the tie (Adler part 1 PDF 38, Ex. II-20 Coriolanus), so 62 is D U and the sf at 63 is a down-bow with Vln II and Vc
  f'''2-- << { aes'''2--^\markup \italic "div." } \\ { fes'''2-- } >> |  % c059: non div. at the ff arrival (Adler part 1 PDF 152: divisi weakens the first violin line); the held A flat6 goes to flute 1  % c051: div. at the ff arrival: the upper half holds A flat6 (fifth of D flat, ninth of G flat, third of F flat) above the augmented head, so the B section's registral peak falls on its held climax and not on the passing eighth B flat6 at 58 (Sebesky PDF 223; c031 option, but held: B flat6-A flat6 here doubled horn 3 and trombone 1's A flat-B flat in octaves and pre-empted the B flat6-A flat6 of 79-80). The lower half keeps D flat6 on the downbeat, so the leading tone C6 of bar 60 still resolves in its own line (c039); A flat5 and F5 stay in Fl, Ob, Cl, Vln II
  << { a'''1:32\sf\>^\markup \italic "trem." } \\ { e'''1:32 } >> | e'''2:32\p^\markup \italic "unis." r2 |  % c052: the upper half's A flat6 (= G sharp6, leading tone of A minor over F flat = E) rises to A6 instead of leaping a diminished 4th to E6 (A&S PDF 406-407, 439)  % c024: double stop fills the upper octave of the tutti chord (Rimsky-Korsakov appendix PDF 505: violins in 2-4-note chords at the top)  % c034: top note on the theme's A flat5-D flat6 with the flutes, so the upper octave of the augmented head is in the same instruments for all four notes (Adler part 2 PDF 151, Mozart 40/iv); c024's F5-D flat6 kept on beat 3
}
bSecVlnTwo = {
  <des' aes'>1\pp\strMark "D" \markup { "Poco più mosso (" \fontsize #-2 \general-align #Y #DOWN \note {4} #1 "= 60)" }^\markup \italic "senza sord., div., sul tasto" | <des' bes'~>2 <ges' bes'~>2 | <des' bes'>2 ges'2 | <es' ges'>2 <des' f'>2 |  % c142: 39 b3-4 both halves on G flat4 (was B flat4 over G flat4): B flat4 doubled the viola's B flat3, the 7th of the half-diminished seventh on C, and left it by a leap; the 7th now sounds once and passes to the bass's A natural (A&S PDF 399, 406-407, 439 item 3)  % c141: top A flat4 at 37 and B flat4 tied through 38-39 (was F4, G flat4 throughout), lower half D flat4-G flat4 under it (was D flat4-B flat3, D flat4-E flat4): the held chord no longer sounds the flute's F5, G flat5 and E flat5 an octave below on the beat (only the D flat at 38 b1 is left); its top line A flat-B flat-G flat-F now has a shape of its own and takes chord tones the melody and bass lack (Sebesky PDF 210-212, Ex. 277, 279-280; PDF 219: the flute's weak register is not covered). Pitches only, from the viola arpeggio's chord: no new figure or colour (c124 rule)
  % c027: Vln II tacet 41-44 when the cor anglais takes theme B's lower octave: its chord (B flat3-G flat4) lay on the cor anglais'
  % own notes (D flat4 at 41, F4 at 42, D flat4 at 43, C4 at 44) and repeated the viola triplets' harmony (Adler part 2 PDF 274:
  % keep the accompaniment registrally distant from a woodwind soloist; the same reason c021 gave for keeping the cor anglais out of 37-40).
  R1*4 |
  f'1\pp\strMark "E" \markup \null ^\markup \italic "unis., ord." | f'2 ges'2\< |  % c044: F4/G flat4, not D flat4: the held note no longer sits on the cellos' theme head D flat4 at 45 and 46 b3 (Adler part 2 PDF 159 rule 1, PDF 165: unison doubling of a harmony note with the melody loses its colour)
  \after 2 -\tag #'score ^\markup \italic "poco rit." \after 2. \pp eis'1\fp\> | fis'2-\tag #'score ^\markup \italic "poco sostenuto" fis''2 | fis''2 g''4 eis''4 |  % c059: the leading tone E sharp4 of 47 resolves to F sharp4 in place; the octave shift waits for 48 b3, under the cor anglais' held A4  % c054: 48-52 an octave higher, clear of the cor anglais quotation (unison F sharp4 at 49; Adler part 1 PDF 241-243)  % c048: tempo words above the strings while Vln I rests (c045 practice)
  fis''2 d''2 | es''1 | es''2.\< c''4(\p^\markup \italic \override #'(baseline-skip . 2.4) \column { "sul A," "cantabile" } |  % c071: pickup with Vln I  % c032: D4 at 50 b3 removes the F sharp4/B1 to E flat4/A flat1 fifths and the F sharp-E flat augmented 2nd (A&S PDF 266-267). c027: 49 held through b2-3, so only the bass moves with the oboe's D5 (Adler part 2 PDF 279: Bizet keeps the accompaniment rhythmically apart from the solo)
  f''2\< ges''8 f''8 es''4) | des''4( c''8 des''8 es''2)\mp | ges''4(\< \tuplet 3/2 4 { f''8 ges'' f'' } es''4 des''4) | c''4(\mf des''8 c''8 bes'2) |
  aes'4(\<^\markup \italic "ord." des''4) f''4.( ges''8 | aes''4.) ges''8(~ ges''4~ ges''8 f''8) | es''4.(\f f''8 des''4 bes'4) | c''1\upbow\< |  % c085: as Vln I (Adler part 1 PDF 38)  % c119: 58 holds A flat5 with Ob 1 (see c110)  % c151: 58 rhythm as Fl 1
  aes'2--\ff^\markup \italic "molto sostenuto" des''2-- | f''2-- fes''2-- | <e'' c'''>1:32\sf\>^\markup \italic "non div., trem." | <e'' c'''>2:32\p b4(\>^\markup \italic "sul G" d'4 |  % c083: B3 on 64 b3 completes the diminished seventh G sharp-B-D-F (= A flat-C flat-D-F, vii°7 of V in A flat), so the last chord of the B section is a full pivot chord and not a root-position diminished triad D-F-A flat with D four times (A&S PDF 243: VII 5/3 seldom satisfactory, the missing 6th supplied; PDF 231: one chord, two meanings); D4-D flat4 slip into 65 unchanged
}

bSecVla = {
  \stemDown % c015: one stem direction for the triplet figure (Gould PDF 38-39)
  \override Beam.damping = #2 % c105: a three-note group slopes at most one stave-space (Gould PDF 33-34)
  \tuplet 3/2 4 { aes8(\pp^\markup \italic "senza sord., unis." des' f' des' aes des') } \tuplet 3/2 4 { aes8( des' f' des' aes des') } |
  \omit TupletNumber % c035: numbers on the first bar of each figure only (37, 53, 59); the slurred groups make the rhythm plain after that
  \tuplet 3/2 4 { bes8( des' ges' des' bes des') } \tuplet 3/2 4 { bes8( es' ges' es' bes es') } |  % c052: ii6 (bass G flat), not V7 -> ii7
  \tuplet 3/2 4 { bes8( des' ges' des' bes des') } \tuplet 3/2 4 { bes8( es' ges' es' bes es') } |
  \tuplet 3/2 4 { c'8( es' ges' es' c' es') } \tweak TupletNumber.stencil #ly:tuplet-number::print \tuplet 3/2 4 { bes8(\upbow des' f') } r4 |  % c066: beat 4 rest and an up-bow ending at the frog, so the violas have a beat to change from arco to pizz. at 41 (Adler part 1 PDF 54)
  % c057: 41-44 pizz. The cor anglais' lower octave of theme B (A flat3-B flat4) lies in the triplets' own register and attacks their pitches
  % (A flat3, D flat4 at 41; E flat4, D flat4 at 43; C4 at 44): plucked notes decay and leave the solo's held tones alone (Sebesky PDF 13: focus,
  % the background must not divert the ear from the primary element; Rimsky-Korsakov PDF 140: figures to pizz. strings and harp). Arco again at 45.
  \tuplet 3/2 4 { aes8\p\<^"pizz." des' f' des' aes des' } \tuplet 3/2 4 { ges8 bes des' ges bes des' } |  % c108: G flat3-B flat3-D flat4 under the cor anglais's F4 appoggiatura (was B flat3-D flat4-G flat4: the resolution G flat4 sounded in the melody's octave before it resolved; Rimsky-Korsakov PDF 132-133)  % c038: shares the cor anglais/flute swell 41-44 (Dvorak 9/ii Largo strings bars 15-16)
  \tuplet 3/2 4 { aes8\mp\> des' f' } \tuplet 3/2 4 { bes8 des' ges' } \tuplet 3/2 4 { aes8 c' es' } \tuplet 3/2 4 { aes8 des' f' } |
  \tuplet 3/2 4 { ges8 bes des' bes ges bes } \tuplet 3/2 4 { aes8 des' es' } \tuplet 3/2 4 { aes8 c' es' } |
  \tuplet 3/2 4 { ges8\p c' es' c' ges c' } r2 |
  % c042: 46 b3 B flat3, so B flat3-B3-A3 is one voice (no B flat2 bassoon / B3 viola split; A&S PDF 394, Ex. 23-12) and the 7th of C sharp7 is prepared
  \stemNeutral \revert Beam.damping f1\pp^"arco" | des2 \once \override Staff.DynamicLineSpanner.staff-padding = #3 bes2\< | b1\fp\> |  % c167: 46 b1-2 D flat3 (was F3): the B flat minor chord under the melody's B flat-A-B flat had no third for two beats (Sebesky PDF 144-145: the chordal third present somewhere in the ensemble; A&S PDF 76: the third is never omitted except for special effects); F stays in Vln II  % c155: the pp at 48 sat on the first eighth's tenuto-staccato (Gould PDF 55: no characters collide, at least half a space apart)
  % c107: 48-51 off-beat eighths on the same pitches under the cor anglais quotation, sotto voce (Adler part 1 PDF 158, Ex. V-32: on-off beat
  % accompaniment in an Adagio; PDF 160-161, Ex. V-36: the strings support the soloist, who 'can execute her part without orchestral interference';
  % PDF 135, 144 rule 4: background rhythmically unlike the foreground). Off-beats are not the quotation's rhythm (c027's reason); 48 b4 rests under the C.a.'s G sharp.
  r8 a8-_\pp-\tag #'part ^\markup \italic "sotto voce" r8 a8-_ r8 a8-_ r4 | r8 a8-_ r8 a8-_ r8 b8-_ r8 gis8-_ | r8 a8-_ r8 a8-_ r8 d'8-_ r8 b8-_ | r8 c'8-_ r8 c'8-_ r8 c'8-_ r8 c'8-_ | \after 2. \p c'1\< |  % c027: 49 A held over the B (iv7), so the upper strings do not move in the quotation's rhythm
  % c049: 53-56 the triplet figure goes to the harp and the violas rest, re-entering at 57 with the crescendo (Rimsky-Korsakov PDF 140: figures
  % of the accompaniment "better partially entrusted to pizz. strings and harp", which have "little chance of overpowering"; PDF 138: a sustained
  % or bowed line covers a melody more than short detached notes; Ex. 289-291, PDF 144 and PDF 118: a repeated idea is rescored by altering
  % details). 37-40 and 53-56 no longer have the same accompaniment, and the build is staged: harp 53, violas 57, sextuplets 59.
  R1*4 |
  \undo \omit TupletNumber
  \stemDown \override Beam.damping = #2 \tuplet 3/2 4 { aes8(\mp\< des' f' des' aes des') }  % c069: mp, not mf: the figure enters under Fl/Ob p< and violins mf (Adler part 2 PDF 159 rule 1; PDF 184)
   \omit TupletNumber \tuplet 3/2 4 { bes8( des' ges' des' bes des') } |
  \tuplet 3/2 4 { aes8( des' f') } \tuplet 3/2 4 { bes8( des' ges') } \tuplet 3/2 4 { aes8( c' es') } \tuplet 3/2 4 { aes8( ces' f') } |  % c013: V7/IV at 58 b4 (A&S PDF 444-445)
  \undo \omit TupletNumber
  \tuplet 6/4 4 { ges16(\f bes es' bes ges bes) es'( bes ges bes es' bes) } \tuplet 6/4 4 { bes16( des' es' des' bes des') fes'( des' bes des' fes' des') } |  % c029: figure doubles its speed for the last two bars of the animando (Rimsky-Korsakov Ex. 168, PDF 337-338; Ex. 153, PDF 325-328)  % c085: six notes per bow (one beat) at f, not twelve (Adler part 1 PDF 39, Ex. II-22: Mendelssohn's violas six to a bow at forte; slow tempo, do not overload the bow)
  \omit TupletNumber
  \tuplet 6/4 4 { aes16(\< c' es' c' aes c') es'( c' aes c' es' c') } \tuplet 6/4 4 { ges16( c' es' c' ges c') \once \override Beam.damping = #6 ges( c' es' ges' es' ges') } |  % c029: last note G flat resolves to the F of the 61 double stop (no C-D flat octaves with Vln I)
  \undo \omit TupletNumber
  \stemNeutral \revert Beam.damping <des' f'>1:32\ff^\markup \italic "non div., molto sostenuto, trem." | <bes des'>2:32 <aes fes'>2:32 | <e' c''>1:32\sf\> | <e' c''>2:32\p gis2(\>^\markup \italic "sul C" |  % c096: "sul C" where the slurred G sharp3-G3 begins, not on its second note at 65 (Adler part 1 PDF 64: the string must be marked where the passage on it starts)  % c099: 62 b3 A flat3/F flat4, not C flat4/F flat4: C flat4(B3)-E4 over the bass E-A made parallel fifths at 62-63 (introduced by c094; c032 had removed the same fault). F flat4 is held into 63 as the common tone.  % c094: E4-C5, not C4-E4: out of trombone 1's quotation (E3-C4, its C4 on 63 b1.5 was a unison with the violas) and into the empty E4-E5 octave under Vln II's E5-C6 (Rimsky-Korsakov PDF 86: no wide empty intervals between upper and lower parts in forte; PDF 85: close intervals at the top; PDF 88: forte tremolo on two strings may take the easiest intervals). The D string keeps F flat4 = E4 from 62; the G string's C flat4 moves to C5 on the A string
   % c032: C4-E4 at 63-64 (was E4-A4: fifths and octaves with the bass E-A). c019: 61-64 double stops, not divisi (Rimsky-Korsakov PDF 88)
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
  des1\pp\<\upbow^\markup \italic "senza sord." | \once \stemUp des4(\p\> bes,4 c4 \once \stemUp des4) | bes,2(\pp es2~ | es2) r4 \clef tenor aes4(\pp^\markup \italic "sul D" |  % 42: contrary motion to the cor anglais and flute on every beat; no doubled seventh with the violas  % c085: the whole note takes its own bow; the eight-beat slur was a phrase slur (Adler part 1 PDF 38: no long phrase slurs in string parts; PDF 39: cello bows are shorter)  % c118: 41 up-bow, so the swell 41-42 is up-bow crescendo, down-bow diminuendo (Adler part 1 PDF 38)
  % c011: cellos in octaves below Vln I on the A and D strings (Rimsky-Korsakov PDF 56, 60-61, Ex. 29-30); bass to Bsn 2 + Cb.
  des'2 es'8 des'8 c'4) | bes4( a8 bes8) des'2\< | cis'2.\mp\> r4\! | \clef bass cis1\pp^\markup \italic "ord." | fis4 b,2 cis4 | fis2 b,2 | es1 | es1\< |  % c124: pp < mp, one level under oboe 1, so the oboe octave, not the cello section, is heard as theme B's head (Adler part 2 PDF 150-151, Mozart 40/iv: the more heavily scored octave is heard as the theme)  % c042: E flat3, not a second G flat (the 7th) that leapt to D flat3 at 53; the cor anglais' A flat-G flat-F is the passing 7th and its resolution (A&S PDF 375, 377)  % c118: 46 des'2 its own up-bow for the crescendo, 47 down-bow for the diminuendo (Adler part 1 PDF 38)
  \once \stemUp des2\p\< c2 | bes,2 ges,2\mp | es2\< c2 | a,2\mf bes,2 |
  % c017: cellos double horn 1's counter-line an octave lower from 57 b3 (b1 stays on the bass: no B flat-A flat octaves with Vln I at 56-57) (Adler PDF 177-178: Meistersinger, cellos with Horn I); bass to B.cl., Bsn 2, Cb.
  f2\< ges2(^\markup \italic "espr." | f4) es2(~ es8 f8) | ges2\f es4( fes4) | es4(\upbow\< f4 ges4. f8) |  % c096: 59 in two bows (U, D), so 60 is a plain up-bow; as written 59 (up) and 60 (marked up) were two four-beat up-bows in succession at f (Adler part 1 PDF 37-38: a slur is one bow; Ex. II-19's two up-bows are short notes, not two long bows)  % c089: 58 b4 F3 again (c082's A flat3 made fifths A flat/E flat -> D flat/A flat with the bass; A&S PDF 352: resolution tone an octave lower in a contrasting timbre is acceptable)  % c082: 60 b4 anticipation  % c085: up-bow crescendo into the ff down-bow at 61 (Adler part 1 PDF 38, two up-bows as in Ex. II-19)  % c151: 58 b4 E flat3 held to b4.5, as Hn 1
  aes2--\ff^\markup \italic "molto sostenuto" des'2-- | f'2-- fes'2-- | a,1:32\sf\>^\markup \italic "trem." | a,2:32\p d,4( e,4) |  % c097: D2-E2, not D3-E3: the cellos' E3 on 64 b4 sounded the tone of resolution of trombone 1's F3 (a 9-8 over the bass E) in the same octave, a semitone under it, before the trombone resolved; in the bass octave it is the allowed 9-8 case (A&S PDF 352; Adler part 2 PDF 42: the quoted line must come through)
   % c074: tremolo A2, not A3: A3 lay inside trombone 1's quotation (E3-C4), in unison with its A3 and a semitone from its B flat3/G sharp3 (Adler part 1 PDF 144: theme and accompaniment separated registrally; PDF 161, Ex. V-37: Bizet's tremolo kept clear of the tune's register)
}
bSecCb = {
  des,4\p^"pizz." r4 des,4 r4 | bes,,4 r4 ges,,4 r4 | es,4 r4 c,4 r4 | a,,2 bes,,2 |
  f,4 r4 ges,4 r4 | bes,,4 es,4 aes,,4 des,4 | ges,,4 r4 aes,,4 r4 | aes,,4 r4 r2 |  % c122: 43 G flat1/A flat1 (was G flat2/A flat2), so the lower strand of the 42 fifths chain falls B flat1-A flat1-G flat1 as at 58-59 (A&S PDF 267: two stepwise lines, one thrown into relief by register)
  bes,,1\pp^"arco" | bes,,2 ges,,2\< | \after 2. \pp cis,1\fp\> | fis,1 | fis,4 b,,2 cis,4 | fis,2 b,,2 | aes,,1 | aes,,1 |
  R1*4 |  % c164: basses tacet 53-56 under the first string statement of theme B (cellos alone on the bass, harp triplets, p-mf) and re-enter at 57 where the cellos leave the bass for their counter-line and the tutti build starts (Adler part 1 PDF 130-131, Ex. V-6: -Bass for a lighter texture, +Bass for the build and cadence; PDF 139, Ex. V-16: adding cellos and basses sets off the second statement and prepares the tutti; PDF 137, Ex. V-14: crescendo by added octaves). Was des,2\p\< c,2 | bes,,2 ges,,2\mp | es,2\< c,2 | a,,2\mf bes,,2 (octaves with the cellos); 52 hairpin removed (the basses hold pp and drop out; the cellos keep the swell)
  f,2\mf\< ges,2 | bes,,4 es,4 aes,,4 \once \stemUp des,4 | ges,,2\f g,,2 | aes,,2~\downbow\< aes,,2\upbow |  % c096: the crescendo f-ff is split over two bows with the change on the tie (Adler part 1 PDF 38, Ex. II-20 Coriolanus: down- and up-bow over the long note so the next attack is solid; PDF 39-40, Ex. II-23/24: a crescendo on one long bass bow in a slow tempo is impossible); 61 still on a down-bow  % c085: 59 in one bow, up-bow crescendo at 60, down-bow ff at 61 (Adler part 1 PDF 38)
  des,1--\ff^\markup \italic "molto sostenuto, change bow at will" | ges,,2-- fes,,2-- | a,,1\sf\> | a,,2\p d,4 e,4 |
}

% c026: harp doubles the pizzicato bass 37-44 (Adler part 1 PDF 117: harp as a doubling instrument; PDF 113-114: low two octaves dark and sonorous).
% Pedals: G to G flat during the rests 15-36 (diagram at 37); A natural for bar 40 (right foot, during the rest at 39 b4), back to A flat during 40 b3-42 b2;
% G flat back to G natural during 57-70 (c049: after the harp figure at 53-56) (diagram at 71). One pedal per foot at a time (Adler part 1 PDF 112-113).
% c049: 53-56 the harp takes the violas' triplet figure (pitches as the violas had them in v49). Pedals as at 37 (D flat, C, B flat | E flat, F,
% G flat, A flat); A flat to A natural during 55 b3-4 for 56 b1-2 (right foot), and back to A flat during 57-70.
bSecHarpR = {
  R1*16 |
  \override Beam.damping = #2 % c105: as the violas' triplets (Gould PDF 34)
  \tuplet 3/2 4 { aes8\p-\tag #'score ^\markup \small \harp-pedal #"^-^|^-^^" des' f' des' aes des' } \tuplet 3/2 4 { aes8 c' es' c' es' c' } |  % c142: 53 b4 ends C4-E flat4-C4 (was C4-E flat4-A flat4): the figure's top A flat4 under the violins' E flat5 went on to G flat3/G flat4 under D flat5 at 54, consecutive fifths into the downbeat (A&S PDF 404, 434-435)  % c137: 53 b4 C4-E flat4-A flat4 (was C4-A flat3-E flat4): no A flat3 on horn 1/clarinet 1's A flat3 pickup, and no A flat3-G flat3 / E flat5-D flat5 fifths with the violins into 54
  \omit TupletNumber
  \tuplet 3/2 4 { ges8 bes ges' bes ges bes } \tuplet 3/2 4 { bes8 es' ges' es' bes es' } |  % c137: 54-56 no harp attacks on the Hn 1/Cl 1 counter-line's held D flat4 (54), G flat4 (55), C4 and D flat4 (56), nor on Bsn 1's G flat3/F3 (56): the figure was the violas' 37-40 figure, written before the counter-line took this octave (Adler part 2 PDF 203: layers in order of importance; PDF 217: like-moving layers need separating; PDF 230 item 3: middle parts not doubled while a solo line runs). Was bes8 des' ges' des' bes des'
  \tuplet 3/2 4 { bes8\mp des' es' des' bes des' } \tuplet 3/2 4 { bes8 c' es' c' bes c' } |  % c137: was bes des' ges' (x2) | bes es' ges' (x2)
  \tuplet 3/2 4 { es'8 ges' es' ges' es' ges' } \tuplet 3/2 4 { bes8 f' bes f' bes f' } |  % c137: was c' es' ges' es' c' es' | bes des' f' des' bes des'
  \undo \omit TupletNumber \revert Beam.damping
  R1*4 | R1*4 |
}
bSecHarpL = {
  <des, des>4\p-\tag #'score ^\markup \small \harp-pedal #"^-^|^-^^" r4 <des, des>4 r4 | <bes,, bes,>4 r4 <ges,, ges,>4 r4 | <es, es>4 r4 <c, c>4 r4-\tag #'score _\markup \small "A♮" | <a,, a,>2 <bes,, bes,>2 |
  <f, f>4 r4 <ges, ges>4 r4-\tag #'score _\markup \small "A♭" | <bes,, bes,>4 <es, es>4 <aes,, aes,>4 <des, des>4 | <ges,, ges,>4 r4 <aes,, aes,>4 r4 | <aes,, aes,>4 r4 r2 |  % c122: 43 an octave lower with the basses
  R1*20 |
}
