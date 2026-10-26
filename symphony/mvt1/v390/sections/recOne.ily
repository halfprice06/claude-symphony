% RECAPITULATION, first group, bars 131–146.
% c108: 138 marked f in every part: the 135 crescendo arrives on the hemiola's stop chord, and trumpets / Hn 3·4 / timpani enter at f, not mf (Rimsky-Korsakov PDF 130, 136)

recOneFluteOne = {
  \partCombineApart r4\ff es'''2-> des'''4~ | des'''4 c'''2-> b''4 | r4 aes''2-> f''4~ | \once \override NoteColumn.force-hshift = #1.7 f''4 d''2-> r4 |
  % 135–137: Fl1 at the violin octave (A♭6 first at 140)
  \partCombineSoloI es''4(\mf\< d''4 c''4) f''4( | es''4 d''4) g''4( f''4 | es''4) aes''4( g''4 f''4) | \partCombineAutomatic b''2.->\f r4 |
  \partCombineApart r8\f g''8\<( f'''4.->) es'''8( d'''8 c'''8 | des'''8\ff es'''8 f'''8 g'''8) aes'''2->~ | aes'''4. g'''8 f'''4 d'''4 | c'''2-> b''2-> | \partCombineAutomatic c'''8->\ff r8 r4 r2 | R1*3 |
}
recOneFluteTwo = {
  es''1\ff | c''2 d''2 | f''1 | g''1 |
  % c144: Fl 2 rests 135-137, as at 23-25, and enters on the stop chord at 138
  R1*3 | aes''2.->\f r4 |
  % c104: F6 at 140 beats 3–4 fills the octave under the A♭6 peak
  \after 8 \< aes''2\f c'''2 | aes''2\ff f'''2 | aes''2 f''2 | g''1 | g''8->\ff r8 r4 r2 | R1*3 |
}
recOneOboeOne = {
  \partCombineApart r4\ff es''2-> des''4~ | des''4 c''2-> b'4 | r4 aes'2-> f'4~ | \once \override NoteColumn.force-hshift = #1.7 f'4 d''2-> r4 |
  \partCombineSoloI es''4(\mf\< d''4 c''4) f''4( | es''4 d''4) g''4( f''4 | es''4) aes''4( g''4 f''4) | \partCombineAutomatic f''2.->\f r4 |
  \partCombineApart r8\f g'8\<( f''4.->) es''8( d''8 c''8 | des''8\ff es''8 f''8 g''8) aes''2->~ | aes''4. g''8 f''4 d''4 | c''2-> b'2-> | \partCombineAutomatic R1*2 | \partCombineSoloI r2 g'4(\p^\markup \italic "dolce" e''4~ | e''2\> d''2)\! \partCombineAutomatic |
}
recOneOboeTwo = {
  g'1\ff | g'2 f'2 | f'1 | g'1 |
  % c119: Ob 2 rests 135-137 (as 23-25: no sevenths/ninths against Ob 1's melody; Rimsky-Korsakov PDF 90 rule 4)
  R1*3 | d''2.->\f r4 |
  % c278: 142 accents on C5-B4 as Ob 1, Fl 1 and the violins, which it doubles (Sebesky PDF 214-215, Ex. 281: a doubled line is articulated alike)
  \after 8 \< c''1\f | \once \override NoteColumn.force-hshift = #-1.45 des''1\ff | des''2 c''2 | c''2-> b'2-> | c''8->\ff r8 r4 r2 | R1 | r1 | R1 |
}
recOneClOne = {
  r8 g8\ff( es'4.->) d'8( des'8 c'8 | c'4--) b8( c'8) aes4.-> g8 | r8 g8( f'4.->) es'8( d'8 c'8 | b4) d'8( c'8) g2 |
  \partCombineApart g'2.->\mf\< f'4->~ | f'2 g'2->~ | g'4 f'2.-> | b'2.->\f r4 |
  r8\f g'8\<( f''4.->) es''8( d''8 c''8 | des''8\ff es''8 f''8 g''8) aes''2->~ | aes''4. g''8 f''4 d''4 | c''2-> b'2-> | \partCombineAutomatic es''8->\ff r8 r4 r2 | R1 | f'1\pp~ | f'2 r2 | % c224: 145-146 F4 (was G4 on Vln I's G4): Cl 1-2 F4/D4, a third, not a fifth; with Hn 3-4 G3/B3 the wind chord is the whole V7 (Rimsky-Korsakov PDF 90 rule 4, PDF 97 remark 4)
}
recOneClTwo = {
  r8 g8\ff( es'4.->) d'8( des'8 c'8 | c'4--) b8( c'8) aes4.-> g8 | r8 g8( f'4.->) es'8( d'8 c'8 | b4) d'8( c'8) g2 |
  es'2.->\mf\< d'4->~ | d'2 es'2->~ | es'4 c'2.-> | aes'2.->\f r4 |
  \after 8 \< aes'1\f | aes'1\ff | aes'2 aes'2 | g'1 | c''8->\ff r8 r4 r2 | R1 | d'1\pp~ | d'2 r2 |
}
recOneBsnOne = {
  \partCombineUnisono r8 g8\ff( es'4.->) d'8( des'8 c'8 | c'4--) b8( c'8) aes4.-> g8 | r8 g8( f'4.->) es'8( d'8 c'8 | b4) d'8( c'8) g2 |
  \partCombineAutomatic c2.\mf\<-> b,4->~ | b,2 c2->~ | c4 f2.-> | f2.->\f r4 |
  % c157: 139-142 Bsn 1 with the cellos on a tenor line in contrary motion to the tune (the bass was in eight parts; 27-30 have the cello/bassoon tenor line; Sebesky PDF 12-13)
  c'2.\f\<( bes4) | aes2\ff( f2~ | f4) g4( aes4 c'4~ | c'2-> b2->) | % c388: accents on C-B at 142 as Tbn 2 on the same line and every part on the hammered C-B (MOLA Ex. 6 PDF 11)
  % cycle 77: Bsn 1 answers the Vln I head one bar later (as Bsn/Vla/Vln I at 33-35); tail D-C-B, no D-flat (avoids the head's own fifths)
  c1\f | r8 g8\mf\>( es'4.->) d'4( c'8 | b1\pp) | R1 |
}
recOneBsnTwo = {
  r8 g8\ff( es'4.->) d'8( des'8 c'8 | c'4--) b8( c'8) aes4.-> g8 | r8 g8( f'4.->) es'8( d'8 c'8 | b4) d'8( c'8) g2 |
  c2.\mf\<-> b,4->~ | b,2 c2->~ | c4 f,2-> aes,4 | d2.->\f r4 |
  f,2\f\< aes,2 | des,1\ff | f,2 d,2 | g,1 |
  R1*4 |
}
recOneCbsn = {
  % c256: breath on beat 4 of 134 (Cbsn had 131.1-138.3 unbroken, about 15 s of low quarters at ff/f; Adler adler1 PDF 230: the low contrabassoon
  % takes considerable breath, give periodic rests). Tuba, B.tbn and Cb hold G1/G2 through 134; Cbsn re-enters with the mf hemiola at 135.
  c,4\ff c,4 c,4 c,4 | c,4 c,4 g,,4 g,,4 | aes,,4 aes,,4 aes,,4 aes,,4 | g,,4 g,,4 g,,4 r4 |
  c,4\mf\<-> c,4 c,4 b,,4-> | b,,4 b,,4 c,4-> c,4 | c,4 f,,4-> f,,4 aes,,4 | d,2.->\f r4 |
  f,,2\f\< aes,,2 | des,,1\ff | f,,2 d,,2 | g,,1 | c,8->\ff r8 r4 r2 | R1*3 |
}
recOneHnOne = {
  % c354: 139-141 held horns 1-2 and trumpets stay f (were f< ff) under the ff tune and the tenor line, as the held brass at 27-32, 82, 131 and 160 sit one level below the tune (Adler adler2 PDF 159 rule 1, PDF 184); accents at 142 and the ff strokes at 143 unchanged
  g'1\f | g'2 f'2 | f'1 | g'1 | % c177: c176's breath dropped: Hn 1-2 now rest 135-136.2
  R1 | r2 g'2->\mp\< ~ | g'4 f'2.-> | aes'2.->\f r4 | % c177: Hn 1-2 join the clarinets' pad at the third hemiola cell (136.3), not from 135 (Adler adler1 PDF 255: alter the third statement; PDF 257: unison overlap)
  aes'1\f | aes'1 | aes'2 aes'2 | g'1 | g'8->\ff r8 r4 r2 | R1*2 | r2. g4(\mp^\markup \italic "dolce" |
}
recOneHnTwo = {
  es'1\f | es'2 d'2 | f'1 | f'1 |
  R1 | r2 es'2->\mp\< ~ | es'4 c'2.-> | f'2.->\f r4 |
  f'1\f | f'1 | f'2 f'2 | d'1 | es'8->\ff r8 r4 r2 | R1*3 |
}
recOneHnThree = {
  c'1\f | c'2. b4 | d'1 | d'1 \breathe | % c264: f at 131 (was ff>f): C4 sits inside the low theme G3-E-flat4, so it is graded with the other accompanying brass (Adler adler2 PDF 159 rule 1, PDF 497)
  \partCombineSoloI c'2.->\mp\< d'4->~ | d'2 c'2->~ | % c162: D4 (was B3), as at 23-24 (no d5 to P5 with Hn 1)
  c'4 aes2.-> | \partCombineAutomatic d'2.->\f r4 |
  c'1\f | des'1 | des'2 c'2 | c'2-> b2-> | % c288: accents on C-B at 142 as every doubling of it (Fl, Ob, Cl, Vln) and as at 32 (MOLA PDF 11 Ex. 6)
  % c153: Hn 3 holds the leading tone through 146 and resolves it to C4 at 147, so the V7 keeps its third into the C-major arrival (A&S PDF 220, 456)
  % c348: Hn 3 enters pp on beat 3 of 145, under the bassoon's B3 after it has sounded alone for two beats, and holds it as Bsn 1 releases: the B3 is overlapped, not handed over at the barline (Adler adler2 PDF 191, Ex. XV-37: a held note passed between instruments at the same level with overlap; PDF 192, Ex. XV-40: seams must not show). c347's point (the answer's arrival not struck by the horn) still holds.
  R1*2 | \partCombineApart r2 b2\pp~-\tag #'score ^\markup \bold "3." \partCombineAutomatic | b1 | % c348: apart from 145.3 with a "3." label, so the held B3 does not print under Hn 4's "4." label; c347: Hn 3 enters on B3 at 146, where Bsn 1's answer releases (was B3 from 145, struck with the bassoon's arriving B3 at the same pitch; Adler adler2 PDF 257-258, 264, 274). The wind V7 at 145 stays complete: Hn 4 G3, Bsn 1 B3, Cl 2 D4, Cl 1 F4
}
% c139: 132 Hn 4 releases G3 on beat 3 under the trombones' A-flat3 appoggiatura (brass basis in the melody's octave; Rimsky-Korsakov PDF 132-133), as at 28
recOneHnFour = {
  g1\f | g2 r2 | f1 | g1 | % c264: f at 131, as Hn 3
  R1*3 | f2.->\f r4 |
  f1\f | f1 | f2 d2 | g1 |
  R1*2 | g1\pp | \tag #'score { \once \omit MultiMeasureRest } R1 | % c355: no Hn 4 rest at 146 in the score: it printed above Hn 3's B3 (labelled '3.' at 145) and read as Hn 3 resting (Gould PDF 49-51; MOLA PDF 8 Ex. 7)
}
% c174: trumpets 131-134 in the timpani rhythm (as at 27-30) instead of whole notes, so the low trombone/cello theme is not covered by a held trumpet chord at its own pitch;
% pitches unchanged (Adler adler2 PDF 39-41, Ex. XI-21 Tchaikovsky 4/i: trombone cantus firmus under short rhythmic trumpet and horn chords; Tchaikovsky 6/i 263-266)
recOneTptOne = {
  g'4\f r8 g'8 g'4 r8 g'8 | g'4 r4 g'4 b'4 | b'1 | b'4 r8 b'8 b'4 r8 b'8 | % c242: 133 B4 (was A-flat4): common tone through V - vii°4/2 - V, no augmented seconds B-A-flat-B (Aldwell & Schachter Ex. 11-10d, PDF 169)
  R1*3 | b'2.->\f r4 | c''2\f c''2 | aes'1 |
  aes'2 aes'2 | g'1 | c''8->\ff r8 r4 r2 | R1*3 |
}
recOneTptTwo = {
  g'4\f r8 g'8 g'4 r8 g'8 | g'4 r4 f'4 r4 | f'1 | g'4 r8 g'8 g'4 r8 g'8 |
  R1*3 | f'2.->\f r4 | aes'2\f aes'2 | f'1 |
  f'2 f'2 | d'1 | es'8->\ff r8 r4 r2 | R1*3 |
}
recOneTptThree = {
  es'4\f r8 es'8 es'4 r8 es'8 | es'4 r4 d'4 r4 | d'1 | d'4 r8 d'8 d'4 r8 d'8 |
  R1*3 | d'2.->\f r4 | f'2\f f'2 | f'2 des'2~ | % c324: 140 beat 3 D-flat4 (was F4 for the whole bar, in unison with Tpt 2): the three trumpets hold the close triad A-flat4-F4-D-flat4 of the flat-II chord (Rimsky-Korsakov PDF 100-101); D-flat4 is held into 141
  des'2 c'2 | c'2-> b2-> | R1*4 | % c288: accents at 142 as the doubled C-B (MOLA PDF 11 Ex. 6)
}
% c129: trombones, bass trombone and tuba rest 135-137 (as at 23-25, where low brass are silent): the drop from the ff theme to mf is made by the
% brass leaving, not by a written subito; horns, bassoons, contrabassoon and low strings keep the held chord and the hemiola bass (Rimsky-Korsakov PDF 113; Ex. 169, PDF 339-340)
% c144: Tbn 1·2 f (was ff) on the low theme 131-134: in a unison statement the trombones are marked below the woodwinds and strings so they do not
% dominate it (Adler adler2 PDF 147, D'Indy Istar Ex. XV-1: trombones ppp under f); Cl a2, Bsn a2 and Vc stay ff, so the theme is a blend, not a trombone solo
recOneTbnOne = {
  r8 g8\f( es'4.->) d'8( des'8 c'8 | c'4--) b8( c'8) aes4.-> g8 | r8 g8( f'4.->) es'8( d'8 c'8 | b4) d'8( c'8) g2 |
  R1*3 | aes2.->\f r4 |
  c'1\f | des'1 | des'2 c'2 | c'2-> b2-> | c'8->\ff r8 r4 r2 | R1*3 |
}
recOneTbnTwo = {
  r8 g8\f( es'4.->) d'8( des'8 c'8 | c'4--) b8( c'8) aes4.-> g8 | r8 g8( f'4.->) es'8( d'8 c'8 | b4) d'8( c'8) g2 |
  R1*3 | f2.->\f r4 |
  % c317: 139-142 Tbn 2 joins the Vc/Bsn 1 tenor counterline (was A-flat3 held three bars, then G3): a cello section and one bassoon in F3-C4 sat inside the
  % ff held brass chord's own register (Tbn 1 + Hn 3 on C4/D-flat4, Tbn 2 A-flat3, Hn 4 F3); a trombone carries the line in its best register
  % (Adler adler2 PDF 42 Ex. XI-23: every instrument in its best register so the line comes through each time; PDF 44: independence of the trombones against the trumpets and winds).
  % Tbn 2 stays at or under Tbn 1 (no crossing on the shared staff); A-flat and G remain in Hn 1, Tpt 2, Cl 2 and Hn 4. Level f as before (graded brass at 139).
  c'2.\f( bes4) | aes2( f2~ | f4) g4( aes4 c'4~ | c'2-> b2->) | g8->\ff r8 r4 r2 | R1*3 |
}
recOneBassTbn = {
  % c308: f (was ff) under the low P theme, as B.tbn and tuba at 27 and 167 and as Tbn 1-2 on the theme here (c144): the held bass trombone C3 in the same family a fifth under the trombones' theme outweighed it (Adler adler1 PDF 316, 329)
  c1\f | c2 g,2 | aes,1 | g,1 |
  R1*3 | d2.->\f r4 |
  f,2\f aes,2 | des1 | f2 d2 | g,1 | c8->\ff r8 r4 r2 | R1*3 |
}
recOneTuba = {
  c,1\f | c,2 g,,2 | aes,,1 | g,,1 | % c308: f (was ff), as B.tbn
  R1*3 | d,2.->\f r4 |
  f,,2\f aes,,2 | des,1 | f,2 d,2 | g,,1 | c,8->\ff r8 r4 r2 | R1*3 |
}
recOneTimp = {
  c4\ff r8 c8 c4 r8 c8 | c4 r4 g,4 r4 | aes,4 r8 aes,8 aes,4 r8 aes,8 | g,8 g,8 g,8 g,8 g,8 g,8 g,8 g,8 |
  % c143: timpani rest 135-137 with the low brass (c129), as at 23-25; after 117-134 without a break they re-enter f on the 138 stop chord (Rimsky-Korsakov PDF 136: economy, fresh re-entry; PDF 130: diminuendo by elimination)
  R1*3 | g,2.->\f r4 |
  R1 | aes,1:32\f\< | aes,4:32\ff~ aes,4 r2 | g,4-> r4 g,4-> r4 | c8->\ff r8 r4 r2 | g,1:32\mp\>~ | g,1:32\pp~ | g,4:32~ g,4 r2 |
}
recOnePerc = \drummode {
  R1*16 |
}
recOneVlnOne = {
  r4 es'''2->\ff\downbow des'''4~ | des'''4 c'''2-> b''4 | r4 aes''2-> f''4~ | f''4 d''2-> r4 |
  es''4(\mf\< d''4 c''4) f''4( | es''4 d''4) g''4( f''4 | es''4) aes''4( g''4 f''4) | b''2.->\f r4 |
  % c194: 139-142 an octave lower, in unison with Vln II (as at 56-59); Fl 1 alone keeps A-flat6, so the violins' A-flat6 is saved for the 160 climax
  % (c184, c191, c193; Adler PDF 129, 133: extremes not spent before the final build; Casanelles PDF 277-278: a flute above the violin unison adds upper partials, it is not heard as a second melodic peak)
  r8 g'8\downbow\f\<( f''4.->) es''8( d''8 c''8 | des''8\ff es''8 f''8 g''8) aes''2->~ | aes''4. g''8 f''4 d''4 | c''2->\downbow b'2->\downbow |
  % c338: down-bow pickup and hooked up-bow as in every other string statement of the head (15, 27, 34-37, 131, 167), so the accented E-flat5 is a down-bow (Adler adler1 PDF 38, Ex. II-19)
  r8 g'8\downbow\f( es''4.->) d''8( des''8 c''8 | c''4--)\> b'8\upbow( c''8) aes'4. g'8 | g'1\pp~ | g'2 r2 |
}
recOneVlnTwo = {
  r4 es''2->\ff\downbow des''4~ | des''4 c''2-> b'4 | r4 aes'2-> f'4~ | f'4 d'2-> r4 |
  g'4->\mf\< g'4 g'4 f'4-> | f'4 f'4 g'4-> g'4 | g'4 f'4-> f'4 f'4 | <d'' aes''>2.->\f r4 |
  r8 g'8\downbow\f\<( f''4.->) es''8( d''8 c''8 | des''8\ff es''8 f''8 g''8) aes''2->~ | aes''4. g''8 f''4 d''4 | c''2->\downbow b'2->\downbow |
  r4 r8 g'8\f r8 g'8 r8 g'8 | % c294: no G4 on 1-and, where Vln I's pickup G4 sounds (Adler adler1 PDF 135; as c227 at 15/17)
  g'2\mp\> f'2 | f'1\pp | f'2 r2 |
}
% c261: 144 Vln II, Vla, Vc, Cb drop to mp (was a diminuendo from f) where Bsn 1 enters mf> with its answer of the P head on the violas' G3
% (Adler adler1 PDF 226: an accompanied bassoon is swallowed; mark the accompanying instruments so they do not overshadow it). Vln I keeps its f> tail; timpani already mp.
recOneVla = {
  % c264: f at 131-134 (was ff): the off-beat E-flat4/G4 dyads lie on the theme's own pitches (Cl, Bsn, Tbn, Vc G3-E-flat4); accompaniment marked below the theme (Adler adler2 PDF 159, 482, 497)
  r8 <es' g'>8\f \repeat unfold 3 { r8 <es' g'>8 } | \repeat unfold 2 { r8 <es' g'>8 } \repeat unfold 2 { r8 <d' f'>8 } | \repeat unfold 4 { r8 <d' f'>8 } | \repeat unfold 4 { r8 <d' f'>8 } |
  es'4->\mf\< es'4 es'4 d'4-> | d'4 d'4 es'4-> es'4 | es'4 c'4-> c'4 c'4 | <f' b'>2.->\f r4 |
  c'8\f\< c'8 b8 c'8 f'8 f'8 e'8 f'8 | f'8\ff f'8 es'8 f'8 aes'8 aes'8 g'8 aes'8 | aes'8 aes'8 g'8 aes'8 f'8 f'8 e'8 f'8 | g'8 g'8 fis'8 g'8 d'8 d'8 cis'8 d'8 |
  % c247: 144-146 G3 (was E-flat4-D4 | D4 | D4): the violas held the bassoon's answering head notes E-flat4 and D4 in unison while it played them;
  % the cellos keep E-flat3-D3 an octave lower, so the bassoon's answer is heard alone in its register (Adler adler2 PDF 274; dialogue, PDF 257; as c127 at 77)
  r4 r8 es'8\f r8 es'8 r8 es'8 | % c294: as Vln II
  % c327: 144 the G3 enters on 2-and, under the bassoon's held E-flat4, not on beat 1 where it already sounded the pitch of the bassoon's pickup G3 on 1-and
  % (Adler adler1 PDF 135: the background leaves the anacrusis undisturbed; PDF 144: rhythm and register before dynamics; as c227 at 15/17, c294 at 143)
  r4 r8 g8~\mp\> g2 | g1\pp | g2 r4 \once \override TextScript.self-alignment-X = #RIGHT g4(\mf^\markup \italic "dolce" | % c175: text clear of the barline (Gould PDF 55)
}
recOneVc = {
  r8 g8\downbow\ff( es'4.->) d'8( des'8 c'8 | c'4--) b8\upbow( c'8) aes4.-> g8 | r8 g8\downbow( f'4.->) es'8( d'8 c'8 | b4) d'8( c'8) g2 |
  c2.\mf\<-> b,4->~ | b,2 c2->~ | c4 f2.-> | <d aes>2.->\f r4 |
  % c157: 139-142 tenor line (Vc + Bsn 1): C4-B-flat-A-flat-F under the rising tune, F-G-A-flat-C under the falling one, C held into the 4-3 at 142; Cb, B.cl, Bsn 2, Cbsn, B.tbn, tuba keep the bass (Sebesky PDF 12-13: economy)
  c'2.\f\<\upbow( bes4) | aes2\ff( f2~ | f4) g4( aes4 c'4~ | c'2-> b2->) | % c388: accents as Tbn 2, Hn 3, Tpt 3, Tbn 1 on the same C4-B3 (MOLA Ex. 6 PDF 11)
  c1\f | es2.\mp\> d4~ | d1\pp | % c222: 145 D3 tied (was B2): the leading tone is not doubled under Bsn 1/Hn 3's B3 at pp (A&S PDF 76; PDF 80: inner voices by common tone)
   r2. \once \override TextScript.self-alignment-X = #RIGHT g,4(\mf^\markup \italic "dolce" | % c315: bass clef kept: 146-155 (G2-F4) need at most two ledger lines in bass, so no tenor clef here (Gould PDF 21); c115 clef-before-pickup no longer needed
}
recOneCb = {
  c,8\ff \repeat unfold 7 c,8 | \repeat unfold 4 c,8 \repeat unfold 4 g,,8 | \repeat unfold 8 aes,,8 | \repeat unfold 8 g,,8 |
  c,4\mf\<-> c,4 c,4 b,,4-> | b,,4 b,,4 c,4-> c,4 | c,4 f,,4-> f,,4 aes,,4 | d,2.->\f r4 |
  f,4\f\< r8 f,8 aes,4 r8 aes,8 | des,8\ff \repeat unfold 7 { des,8 } | \repeat unfold 4 { f,8 } \repeat unfold 4 { d,8 } | \repeat unfold 8 { g,,8 } |
  c,4\f r8 c,8 c,4 r8 c,8 | g,,1\mp\> | g,,1\pp~ | g,,2 r2 |
}
recOneBassCl = {
  R1*8 | f,2\f\< aes,2 | des1\ff | f2 d2 |
  g,1 | R1*4 |
}
% c096: cor anglais rests 103-147; part-only cue of the oboe's dolce G-E (145-146) before the answer at 147. Removed from the full score (score.ly).
recOneCorAnglais = { R1*14 | \tag #'score R1*2 \tag #'part \cueDuring #"cueObOne" #UP { s4*0^\markup \fontsize #-3 "Ob. 1" R1*2 } | }
