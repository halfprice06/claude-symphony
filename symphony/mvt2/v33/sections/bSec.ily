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
  f''2(\p^\markup \italic "dolce cantabile" ges''8 f''8 es''4 | des''4 c''8 des''8 es''2) | ges''4( \tuplet 3/2 4 { f''8 ges'' f'' } es''4 des''4 | c''2 bes'2) |  % c031: head rhythm 2 8 8 4 at 37/45/53, so theme B does not open with theme A's 4. 8 (Dvorak 9/ii: bar 7 vs bar 46)
  aes'4(\< des''4 f''4. ges''8 | aes''4\mp\> bes''8 aes''8 ges''4 f''4 | es''4. f''8 des''4 bes'4 | c''2.)\p r4 |
  R1*8 |
  R1*4 |
  \stemDown aes''4(\mf\<^\markup \bold "1." des'''4 f'''4. ges'''8 | aes'''4 bes'''8 aes'''8 ges'''4 f'''4 | es'''4.\f f'''8 des'''4 bes''4 | c'''1)\< |  % c015: Fl 2 rests, so stems follow the notes (Gould PDF 38); the combiner keeps voice one here
  \stemNeutral \partCombineUnisono aes''2--(\ff des'''2-- | f'''2-- fes'''2--) \partCombineAutomatic | R1*2 |  % c021: a2 with flute 2
}
% c021: flute 2 joins flute 1 in unison on theme B's augmented head at the climax, so the upper octave of trumpet 1's
% A flat-D flat-F-F flat has two flutes (Rimsky-Korsakov PDF 75: "in the top register two flutes will suffice").
bSecFluteTwo = {
  R1*8 | R1*8 | R1*8 |
  aes''2--(\ff des'''2-- | f'''2-- fes'''2--) | R1*2 |
}
bSecOboeOne = {
  R1*8 |
  R1*2 | r2 r4 cis'4(\p^\markup \bold "1."^\markup \italic "espr." | a'2.~ a'8 gis'8 | fis'4 d''2 cis''4) | cis''2( b'4 a'4) |
  aes'2(\> ges'2 | f'2. ges'4)\pp |
  f'2 r2 | R1*3 |
  \stemDown aes'4(\mf\<^\markup \bold "1." des''4 f''4. ges''8 | aes''4 bes''8 aes''8 ges''4 f''4 | es''4.\f f''8 des''4 bes'4 | c''1)\< |
  \stemUp f''1(\ff | f''2 fes''2) | R1*2 |  % c014: oboe 1 above the trumpets at 61 (Rimsky-Korsakov PDF 110-111)
}
bSecOboeTwo = {
  R1*8 | R1*8 | R1*8 |
  aes'2--\ff des''2-- | des''2-- fes''2-- | R1*2 |  % c014: was F4 = Tpt 2 + Hn 2; takes the melody's lower octave at 61
}
% c009: the lower octave of theme B goes to the cor anglais (Rimsky-Korsakov Ex. 57: Fl / Eng. horn in octaves).
% c021: 37-40 flute 1 alone (Rimsky-Korsakov PDF 66-67: an intimate melody to a solo instrument of simple timbre;
% doubling where the expression broadens); the lower octave would sit in unison with the Vln II chord tones F4, D flat4, G flat4.
% The cor anglais joins at 41 with the crescendo.
bSecCorAnglais = {
  R1*4 |
  aes4(\p\<^\markup \italic "solo, dolce cantabile" des'4 f'4. ges'8 | aes'4\mp\> bes'8 aes'8 ges'4 f'4 | es'4. f'8 des'4 bes4 | c'2.)\p r4 |
  R1*20 |
}
bSecClOne = {
  R1*8 |
  R1*8 |
  r2 r4 aes8(\p bes8 | des'4.\< f'8 aes'2 | ges'2\mp f'2 | es'2 des'2) |  % c019: unison with Hn 1's counter-line, which the viola triplets cover in the same register
  f'2\mp\< des'2 | des'4 des'4 c'4 des'4 | es'2\f es'2 | c''1\< |
  aes'2\ff des''2 | bes'2 ces''2 | R1*2 |  % c014: clarinets with the trumpets in unison, under the oboes (Rimsky-Korsakov PDF 106; natural order PDF 67)
}
bSecClTwo = {
  R1*8 | R1*8 |
  R1*4 |
  des'2\mp\< des'2 | aes4 ges4 aes4 ces'4 | bes2\f des'2 | aes'1\< |  % c032: A flat4, not a second C under the melody's leading tone before the D flat climax (A&S PDF 266, 286); resolves to F4
  f'1\ff | ges'2 aes'2 | R1*2 |  % c014: was F3 inside the trombones
}
bSecBassCl = {
  des'2)\! r2 | R1*7 |
  R1*8 | R1*4 |
  f2\mp\< ges2 | bes,4 es4 aes,4 des4 | ges2\f g2 | aes,1\< |  % c017: takes the cellos' bass line 57-60
  des1\ff | ges,2 fes,2 | R1*2 |
}
bSecBsnOne = {
  f2\pp r2 | R1*7 |
  R1*8 |
  R1*4 |
  f2\mp\< bes2 | f4 es4 es4 f4 | ges2\f es2 | es1\< |
  f1\ff | ges2 aes2 | R1*2 |
}
bSecBsnTwo = {
  R1*8 |
  bes,1\pp | bes,2 bes,2 | gis,1\> | R1\! | R1*4 |
  des2\p des2 | bes,2 aes,2 | es2 des2 | a,2 bes,2 |
  f2\mp\< ges2 | bes,4 es4 aes,4 des4 | ges2\f g2 | aes,1\< |
  des1\ff | ges,2 fes,2 | R1*2 |
}
bSecCbsn = {
  R1*24 |
  des,1\ff | ges,,2 fes,,2 | R1*2 |
}
bSecHnOne = {
  R1*8 | R1*8 |
  r2 r4 aes8(\p^\markup \bold "1."^\markup \italic "espr." bes8 | des'4.\< f'8 aes'2 | ges'2\mp f'2 | es'2 des'2) |  % c019: crescendo with the violins; Cl 1 doubles (Rimsky-Korsakov PDF 74-75: wind + horn in unison, finer legato)
  \partCombineSoloI aes'2(\mp\<^\markup \bold "1." ges'2 | f'4 es'2 f'4 | ges'2\f es'2 | es'4\< f'4 ges'4 f'4) |  % c025: horn 2 tacet 57-60; force solo so its rests are not printed under horn 1 (Gould PDF 51: parts share a rest)
  \partCombineAutomatic aes'1\ff | bes'2 ces''2 | R1*2 |
}
% c024: horn 2's first entry is the ff of 61, not mp at 57 (Rimsky-Korsakov PDF 136: brass re-entries pp or ff; mp/mf "colourless");
% its 57-60 notes were in unison with clarinet 1, which keeps them. Brass now enter only at the top of the crescendo (PDF 130).
bSecHnTwo = {
  R1*8 | R1*8 | R1*4 |
  R1*4 |
  f'1\ff | ges'2 aes'2 | R1*2 |
}
bSecHnThree = {
  R1*23 | es'1\p\< |  % c029: horns 3-4 enter p cresc. on V7 and grow into the ff (Rimsky-Korsakov Ex. 168, PDF 337-338)
  des'1\ff | des'2 fes'2 | R1*2 |
}
bSecHnFour = {
  R1*23 | aes1\p\< |
  aes1\ff | bes2 ces'2 | R1*2 |
}
bSecTptOne = { R1*24 | aes'2--\ff des''2-- | f''2-- fes''2-- | R1*2 | }
bSecTptTwo = { R1*24 | f'1\ff | bes'2 ces''2 | R1*2 | }  % c014: the major 7th G flat-F at 62 split between horns and trumpet (Rimsky-Korsakov PDF 102-103)
bSecTptThree = { R1*24 | des'1\ff | des'2 fes'2 | R1*2 | }
bSecTbnOne = {
  R1*24 |
  aes1\ff | bes2 ces'2 |
  r8 e8->\ff^\markup \italic "marcato" c'4.-> b8 bes8 a8 | a4 gis8 a8 f4.->\> e8\mf |  % c028: dim. after the last accent (Dvorak 9/ii Largo: the quotation steps ff to f; Adler part 2 PDF 503 sf > pp)
}
bSecTbnTwo = { R1*24 | f1\ff | ges2 aes2 | R1*2 | }
bSecBassTbn = { R1*24 | des1\ff | ges,2 fes,2 | a,1\f | a,2\> d,4 e,4\p | }
bSecTuba = { R1*24 | des,1\ff | ges,,2 fes,,2 | R1*2 | }
bSecTimp = {
  R1*15 | aes,1:32\pp\< |
  aes,4\p r4 r2 | R1*5 |
  R1 | aes,2.:32\p\< r4\! |
  des1:32\ff | des2:32 aes,2:32 | R1*2 |
}

bSecVlnOne = {
  R1*8 |
  des''2(\p es''8 des''8 c''4) | bes'4( aes'8 bes'8 des''2) | cis''1\> | R1\! | R1*4 |
  f''2(\p\<^\markup \italic "sul A" ges''8 f''8 es''4) | des''4( c''8 des''8 es''2)\mp | ges''4(\< \tuplet 3/2 4 { f''8 ges'' f'' } es''4 des''4) | c''2(\mf bes'2) |
  aes''4(\<^\markup \italic "ord." des'''4) f'''4.( ges'''8 | aes'''4 bes'''8 aes'''8) ges'''4( f'''4) | es'''4.(\f f'''8) des'''4( bes''4) | c'''1\< |
  <f'' des'''>1\ff^\markup \italic "non div., molto sostenuto" | f'''2 fes'''2 | e'''1:32\sf\> | e'''2:32\p r2 |  % c024: double stop fills the upper octave of the tutti chord (Rimsky-Korsakov appendix PDF 505: violins in 2-4-note chords at the top)
}
bSecVlnTwo = {
  <des' f'>1\pp^\markup \italic "div., sul tasto" | <des' ges'>2 <c' ges'>2 | <des' ges'>2 <des' f'>2 | <es' ges'>2 <des' f'>2 |
  % c027: Vln II tacet 41-44 when the cor anglais takes theme B's lower octave: its chord (B flat3-G flat4) lay on the cor anglais'
  % own notes (D flat4 at 41, F4 at 42, D flat4 at 43, C4 at 44) and repeated the viola triplets' harmony (Adler part 2 PDF 274:
  % keep the accompaniment registrally distant from a woodwind soloist; the same reason c021 gave for keeping the cor anglais out of 37-40).
  R1*4 |
  des'1\pp^\markup \italic "unis., ord." | des'2 des'2 | eis'1 | fis'1 | fis'2. eis'4 | fis'2 d'2 | es'1 | es'1\< |  % c032: D4 at 50 b3 removes the F sharp4/B1 to E flat4/A flat1 fifths and the F sharp-E flat augmented 2nd (A&S PDF 266-267). c027: 49 held through b2-3, so only the bass moves with the oboe's D5 (Adler part 2 PDF 279: Bizet keeps the accompaniment rhythmically apart from the solo)
  f''2(\p\<^\markup \italic "sul A" ges''8 f''8 es''4) | des''4( c''8 des''8 es''2)\mp | ges''4(\< \tuplet 3/2 4 { f''8 ges'' f'' } es''4 des''4) | c''2(\mf bes'2) |
  aes'4(\<^\markup \italic "ord." des''4) f''4.( ges''8 | aes''4 bes''8 aes''8) ges''4( f''4) | es''4.(\f f''8) des''4( bes'4) | c''1\< |
  aes'2--\ff^\markup \italic "molto sostenuto" des''2-- | f''2-- fes''2-- | <e'' c'''>1:32\sf\>^\markup \italic "non div." | <e'' c'''>2:32\p r2 |
}

bSecVla = {
  \stemDown % c015: one stem direction for the triplet figure (Gould PDF 38-39)
  \tuplet 3/2 4 { aes8(\pp^\markup \italic "unis." des' f' des' aes des') } \tuplet 3/2 4 { aes8( des' f' des' aes des') } |
  \tuplet 3/2 4 { bes8( des' ges' des' bes des') } \tuplet 3/2 4 { c'8( es' ges' es' c' es') } |
  \tuplet 3/2 4 { bes8( des' ges' des' bes des') } \tuplet 3/2 4 { bes8( des' f' des' bes des') } |
  \tuplet 3/2 4 { a8( c' es' c' a c') } \tuplet 3/2 4 { bes8( des' f' des' bes des') } |
  \tuplet 3/2 4 { aes8( des' f' des' aes des') } \tuplet 3/2 4 { bes8( des' ges' des' bes des') } |
  \tuplet 3/2 4 { aes8( des' f') } \tuplet 3/2 4 { bes8( des' ges') } \tuplet 3/2 4 { ges8( c' es') } \tuplet 3/2 4 { aes8( des' f') } |
  \tuplet 3/2 4 { ges8( bes es' bes ges bes) } \tuplet 3/2 4 { aes8( des' es') } \tuplet 3/2 4 { aes8( c' es') } |
  \tuplet 3/2 4 { ges8( c' es' c' ges c') } \tuplet 3/2 4 { ges8( c' es' c' ges c') } |
  \stemNeutral f1\pp | f2 ges2 | b1 | a1 | a2. gis4 | a2 d'2 | c'1 | c'1\< |  % c027: 49 A held over the B (iv7), so the upper strings do not move in the quotation's rhythm
  \stemDown \tuplet 3/2 4 { aes8(\p\< des' f' des' aes des') } \tuplet 3/2 4 { aes8( des' f' des' aes des') } |
  \tuplet 3/2 4 { bes8( des' ges' des' bes des') } \tuplet 3/2 4 { c'8( es' ges' es' c' es') } |
  \tuplet 3/2 4 { bes8(\mp\< des' ges' des' bes des') } \tuplet 3/2 4 { bes8( des' f' des' bes des') } |
  \tuplet 3/2 4 { a8( c' es' c' a c') } \tuplet 3/2 4 { bes8( des' f' des' bes des') } |
  \tuplet 3/2 4 { aes8(\mf\< des' f' des' aes des') } \tuplet 3/2 4 { bes8( des' ges' des' bes des') } |
  \tuplet 3/2 4 { aes8( des' f') } \tuplet 3/2 4 { bes8( des' ges') } \tuplet 3/2 4 { ges8( c' es') } \tuplet 3/2 4 { aes8( ces' f') } |  % c013: V7/IV at 58 b4 (A&S PDF 444-445)
  \tuplet 6/4 4 { ges16(\f bes es' bes ges bes es' bes ges bes es' bes) } \tuplet 6/4 4 { bes16( des' es' des' bes des' es' des' bes des' es' des') } |  % c029: figure doubles its speed for the last two bars of the animando (Rimsky-Korsakov Ex. 168, PDF 337-338; Ex. 153, PDF 325-328)
  \tuplet 6/4 4 { ges16(\< c' es' c' ges c' es' c' ges c' es' c') } \tuplet 6/4 4 { ges16( c' es' c' ges c' ges c' es' ges' es' ges') } |  % c029: last note G flat resolves to the F of the 61 double stop (no C-D flat octaves with Vln I)
  \stemNeutral <des' f'>1:32\ff^\markup \italic "non div., molto sostenuto" | <bes des'>2:32 <ces' fes'>2:32 | <c' e'>1:32\sf\> | <c' e'>2:32\p r2 |  % c032: C4-E4 at 63-64 (was E4-A4: fifths and octaves with the bass E-A). c019: 61-64 double stops, not divisi (Rimsky-Korsakov PDF 88)
}

bSecVc = {
  des4\p^"pizz." r4 des4 r4 | bes,4 r4 aes,4 r4 | es4 r4 des4 r4 | a,2 bes,2 |
  f4 r4 ges4 r4 | bes,4 es4 aes,4 des4 | ges4 r4 aes4 r4 | aes,4 r4 r2 |
  % c011: cellos in octaves below Vln I on the A and D strings (Rimsky-Korsakov PDF 56, 60-61, Ex. 29-30); bass to Bsn 2 + Cb.
  \clef tenor des'2(\p^"arco" es'8 des'8 c'4) | bes4( aes8 bes8 des'2) | cis'1\> | \clef bass cis1\pp | fis4 b,2 cis4 | fis2 b,2 | ges1 | ges1\< |
  des2\p\< des2 | bes,2 aes,2\mp | es2\< des2 | a,2 bes,2\mf |
  % c017: cellos double horn 1's counter-line an octave lower from 57 b3 (b1 stays on the bass: no B flat-A flat octaves with Vln I at 56-57) (Adler PDF 177-178: Meistersinger, cellos with Horn I); bass to B.cl., Bsn 2, Cb.
  f2\< ges2(^\markup \italic "espr." | f4) es2( f4) | ges2\f es2 | es4(\< f4 ges4 f4) |
  aes2\ff^\markup \italic "molto sostenuto" des'2 | f'2 fes'2 | a1:32\sf\> | a2:32\p d4( e4) |
}
bSecCb = {
  des,4\p^"pizz." r4 des,4 r4 | bes,,4 r4 aes,,4 r4 | es,4 r4 des,4 r4 | a,,2 bes,,2 |
  f,4 r4 ges,4 r4 | bes,,4 es,4 aes,,4 des,4 | ges,4 r4 aes,4 r4 | aes,,4 r4 r2 |
  bes,,1\pp^"arco" | bes,,2 ges,,2 | cis,1 | fis,1 | fis,4 b,,2 cis,4 | fis,2 b,,2 | aes,,1 | aes,,1\< |
  des,2\p\< des,2 | bes,,2 aes,,2\mp | es,2\< des,2 | a,,2 bes,,2\mf |
  f,2\< ges,2 | bes,,4 es,4 aes,,4 des,4 | ges,2\f g,2 | aes,,1\< |
  des,1\ff^\markup \italic "molto sostenuto" | ges,,2 fes,,2 | a,,1\sf\> | a,,2\p d,4 e,4 |
}

% c026: harp doubles the pizzicato bass 37-44 (Adler part 1 PDF 117: harp as a doubling instrument; PDF 113-114: low two octaves dark and sonorous).
% Pedals: G to G flat during the rests 15-36 (diagram at 37); A natural for bar 40 (right foot, during the rest at 39 b4), back to A flat during 40 b3-42 b2;
% G flat back to G natural during 45-70 (diagram at 71). One pedal per foot at a time (Adler part 1 PDF 112-113).
bSecHarpL = {
  <des, des>4\p^\markup \small \harp-pedal #"^-^|^-^^" r4 <des, des>4 r4 | <bes,, bes,>4 r4 <aes,, aes,>4 r4 | <es, es>4 r4 <des, des>4 r4_\markup \small "A♮" | <a,, a,>2 <bes,, bes,>2_\markup \small "A♭" |
  <f, f>4 r4 <ges, ges>4 r4 | <bes,, bes,>4 <es, es>4 <aes,, aes,>4 <des, des>4 | <ges, ges>4 r4 <aes, aes>4 r4 | <aes,, aes,>4 r4 r2 |
  R1*20 |
}
