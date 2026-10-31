% CODA, bars 167–182 (v100 numbering; 171–186 before cycle 80). Forte C minor (167–170: brass take the first-theme head; fermata on the denied tutti, vii°7 with Tpt/Hn on B♮),
% then the second theme's head returns in C minor in the cellos (171–174, no pickup) against the cor anglais's motto (pickup 171, 172–174);
% bass clarinet, low strings and three trombones (pp chorale, tam-tam at 175) state the motto in augmentation (175–179); Cl1 recalls the intro horn call E♭–C–B (175–177);
% the violins' last motto (177–182) sinks through the Neapolitan to C, and the violas alone turn the minor third to major at the very end (E♭ 181 → E♮ 182).
% Rotation: 167–170 stand where the codetta 69–72 stood (after the S cadence, Tempo dell'Allegro, forte, 4 bars) and 171–174 where the
% flute motto 73–76 stood; the closing zone returns in C minor, split into its P and S components. Do not insert a C-major codetta after 166.

codaClOne = {
  % c096: Cl 1 breathes on beat 1 of 167 after the unbroken counterline 162-166 (E-flat at 166 kept); Ob 1 holds the same g'' from the downbeat
  \partCombineApart r4\f g''2. | \partCombineAutomatic g''2 aes''2 | aes''1\< | aes''2.->\ff r4\fermata |
  % c298: Cl 1 carries the line at 175-177 and hands it to Vln I 'pp espr.'; it gets the same word (Adler adler1 PDF 205-206, 211: solo wind lines carry an expressive word)
  R1*4 | r2. es'4(\pp_\markup \italic "espr." | c''1~ | c''2 b'2\>) |
  R1\! | R1*3 | R1\fermata |
}
codaBassCl = {
  c1\f | c1 | c1\< | c2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
  g,1\pp( | es1) | d1( | c2 des2 | c1\>) | R1\! | R1 | R1\fermata | % c328: the last C fades out under Vc/Cb (Rimsky-Korsakov PDF 130), as Cl 1 at 177
}
codaBsnTwo = {
  c1\f | c1 | c1\< | c2.->\ff r4\fermata | c1\pp | f1 | f1 | g,1 |
  R1*7 | R1\fermata |
}
codaHnOne = {
  \partCombineUnisono r8 g8\ff( es'4.->) d'8( des'8 c'8 | c'4--) b8( c'8) aes4.-> g8 | r8 g8( f'4.->) es'8( d'8 c'8) | b2.-> r4\fermata \partCombineAutomatic |
  R1*11 | R1\fermata |
}
codaHnThree = {
  % c425: bass clef (from 162) kept through 167-170: C4/G3-A-flat3/D4 need one ledger line in bass, two in treble, and the held C4/G3
  % no longer change clef across 166-167; treble returns at the system start 171, in the rests before 181 (Gould PDF 21, 23)
  c'1\f | c'1 | c'1\< | d'2.->\ff r4\fermata | \clef treble R1 | R1 | R1 | R1 |
  % c097: Hn 3 takes C4 from 180 (fills the C3-E-flat4 gap when the chorale stops); Hn 4 takes G3 (fifth above the bass octave, C2-C3-G3-C4 as in the harmonic series)
  % c140: Hn 3 enters at 181 with Hn 4 (was 180): Tbn 1 carries the chorale's last C4 through 180 and overlaps Hn 3's entry by a beat
  % (Adler PDF 191 Ex. XV-37, held C coloured; PDF 192 Ex. XV-40, dovetailing). Hn 3's hold to Hn 4's relief in movement II drops from ~19 s to ~14 s.
  R1*6 | c'1\ppp~ | c'1\fermata\laissezVibrer |
}
codaHnFour = {
  g1\f | g2 aes2 | aes1\< | aes2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
  R1*6 | g1\ppp~ | g1\fermata |
}
codaTimp = {
  c1:32\f~ | c1:32~ | c1:32\< | c2.->\ff r4\fermata | R1 | R1 | R1 | g,1:32\pp |
  R1^\markup \small "soft sticks" | R1*3 |
  % c189: 179-180 the first group's pulse (quarter, eighth rest, eighth: Cb 15-22, timpani/trumpets 27-30, 131-134) instead of plain quarters, so the
  % last soft pulse recalls the Allegro's head rhythm (Beethoven Op. 37/i coda, timpani pp c4 r8 g, c4: corpus timpani.ly; Bruckner 8/i 1890 coda;
  % Aldwell & Schachter PDF 503 note: chromatic/structural events that recall the opening motive at the close of a phase)
  c4\pp r8 g,8 c4 r4 | c4 r8 g,8 c4 r4 | c1:32\ppp~ | c1:32\fermata |
}
codaHarpL = {
  R1 | R1 | R1 | r2. r4\fermata | R1 | R1 | R1 | R1 |
  % c150: no l.v. into movement II: the harp keeps its attack at 182 (c140, Adler XV-37) but releases with the basses and timpani it doubles,
  % so its G2 does not ring against movement II's A-flat bass at its bar 2; only the five tied parts cross the attacca (Rimsky-Korsakov PDF 126-127)
  % c183 (relay from movement II): retune cue at 176 removed; movement II no longer uses the harp's D-flat1 (cue was added by c156).
  R1 | R1 | R1*5 | << <c, g, c>1\ppp\fermata { s2. s4_\tweak self-alignment-X #RIGHT -\markup \small \italic "étouffez" } >> |
}
% c251: sul D for the last motto 177-182 (G4 then E-flat5-D5-C5-D-flat5-C5 in the fifth position): the rising sixth is one shift on the D string instead of a
% crossing to the A string, and the line keeps the D string's veiled colour to the end (Adler adler1 PDF 75: the D string warm and subdued, mellower in the higher
% positions; PDF 73-74: equal, controlled tone in slow expressive passages; PDF 76: sul markings). The C5 crosses into movement II on the D string.
% c278: Vln I 'espr.' at 177 (pp unchanged): the last motto is marked as the primary line among the pp chorale, as the trombones' 'dolce' and the C.a.'s and solo cello's 'espr.' (Sebesky PDF 13-14, 18 Ex. 2A)
ppEspr = #(make-dynamic-script (markup #:line (#:dynamic "pp" #:hspace 0.5 #:normal-text #:italic "espr.")))
codaVlnOne = {
  <g'' es'''>1:32\f^"div." | <g'' es'''>2:32 <aes'' es'''>2:32 | <aes'' f'''>1:32\< | <aes'' f'''>2.:32->\ff r4\fermata |
  R1*6 | r2. \once \override TextSpanner.bound-details.left.text = \markup \italic \small "sul D" \once \override TextSpanner.bound-details.right.padding = #3 g'4(\ppEspr^"unis."\startTextSpan | es''1)~ | es''2. d''4( | % c395: sul D dashes stop 3 spaces short of the last note, so they no longer run into "attacca" in the Vln I part (c385 open item; Adler adler1 PDF 53)
  c''2 des''2) | c''1~\>^\markup \small \italic "change bow at will" | c''1\ppp\fermata\laissezVibrer\stopTextSpan \tag #'score \textEndMark \markup \italic "attacca" | % c200: score-only here; every part gets "attacca" from parts-gen.py (partGlobal). attacca into movement II (common-tone link; movement II thread, 2026-10-10)
}
codaVlnTwo = {
  <c'' g''>1:32\f^"div." | <c'' g''>2:32 <c'' aes''>2:32 | <c'' aes''>1:32\< | <d'' aes''>2.:32->\ff r4\fermata |
  % c107: Vln II rests 171-174 (its A-flat4 sat on the cello's tenuto peak at 172; background left to violas and bassoon, Adler PDF 135, 146);
  % it re-enters with the chorale at 175.
  R1*4 |
  % c192: 178 E-flat4 (was g'2): the F4 of the vii-dim7/V(b9) at 177 falls to E-flat in parallel tenths with the bass D-C; F no longer rises in both Vln II and Tbn 2
  % (A&S PDF 466: 9ths may be left unresolved when the 7th resolves; unresolved 7ths are rare; PDF 471-472, 27-11)
  % c247: 175 G4 (was E-flat4): Cl 1's recall of the horn call enters on E-flat4 at 175.4 on a pitch of its own, not on a note the violins already hold
  % (Adler adler2 PDF 274: keep the accompaniment registrally distant from a woodwind soloist; PDF 283: the solo is helped in pitch, not doubled; as c190 at 13-14).
  % The tonic 6/4 keeps its third in Tbn 2 (E-flat3) and doubles the bass G (A&S); Vln II now holds G4 175-176.
  g'1\pp^"unis."~ | g'1 | f'1 | es'2 f'2 |
  % c160: 180 holds the tonic (was g'2 f'2): Vln I's D-flat is a bare neighbour over C minor, as at bar 3, not a third D-flat triad after 173 and 178 (Sebesky PDF 19)
  g'1 | g'1 | g'1^~\>^\markup \small \italic "change bow at will" | g'1\ppp\fermata\laissezVibrer |
}
codaVla = {
  r8 g8\downbow\ff^"unis."( es'4.->) d'8( des'8 c'8 | c'4--) b8\upbow( c'8) aes4.-> g8 | r8 g8\downbow( f'4.->) es'8( d'8 c'8) | <d' f'>2.-> r4\fermata |
  % c127: A-flat3 on 173 beats 3-4 (was F4, above the cello solo's D-flat4): the viola stays under the solo, the N6 is complete (F-A-flat-D-flat)
  % (Adler PDF 274: accompaniment registrally distant from the soloist)
  c'2\pp( b2 | c'1) | c'2 aes2 | es'2 d'2 |
  % c192: 178 C4 (was es'2): with Vln II on E-flat4 the root is doubled (Vla) and the third is not tripled (Vln I, Vln II only); A-flat (the 9th) is left unresolved, as the 7th resolves (A&S PDF 466)
  % c262: 177 A-flat3 falls to G3 on beat 4 (was aes1, then a leap up to C4): over the bass D the A-flat is the seventh of vii°6/5 (Cl 1's B4 from beat 3), not the
  % ninth of a root-position V9 (no G in the bass), so it resolves by step to the root of V7 as the violins' G4 enters (Aldwell & Schachter PDF 375, 377 box, 378 sec. 9);
  % 177 beat 4 is V4/3, and i6-V4/3-i over the motto bass E-flat-D-C replaces vii°6/5-i5/3 (PDF 376, Ex. 22-4b "poor")
  c'1 | c'1 | aes2. g4 | c'2 aes2 |
  % c160: 180 holds E-flat (was es'2 aes2); see Vln II
  es'1 | es'1 | es'1\>^\markup \column { \small \italic "change bow at will" \italic "morendo" } | e'1\ppp\fermata\laissezVibrer | % c316: the E4 is held under the fermata and tied into movement II bar 1 (about 10-12 s at ppp); the other tied string parts already stagger (Adler adler1 PDF 40, Ex. II-25)
}
% c251: cellos sul G on the chorale's motto bass 175-178 as at 1-3 (held D3 at 177 stopped, not the open D string; Adler adler1 PDF 73-74, 76)
% c269: 171-174 one cello (Solo), the section re-enters (Tutti) on the chorale's motto bass at 175. Notes, dynamics and timing unchanged. The duet with the
% cor anglais (p) is two single players, as Rimsky-Korsakov's Ex. 284 (PDF 457: V-c. solo dolce with the oboe over the muted section); a solo string for
% "that singular difference in colour" over a light accompaniment (PDF 122-123; PDF 142); Elgar 1/i coda, Eulenburg pp. 58-61: SOLO / 2 SOLI / TUTTI.
codaVc = {
  c'2\f es'2 | es'2 f'2 | es'2\< c'2 | d'2.->\ff r4\fermata | \clef tenor es'2.~(\upbow\mp\<^\markup { \bold "Solo" \italic "espr." } es'8 d'8)\> | c'4(\! aes'2--\< g'4\!) | f'4.( es'8 des'4 f'8\< aes'8) | c''2(\> b'2\!) |
  \clef bass \once \override TextSpanner.bound-details.left.text = \markup \italic \small "sul G" g,1\pp(\startTextSpan^\markup \bold "Tutti" | es1) | d1 | c2( des2\stopTextSpan) | c1 | c1 | c1~\>^\markup \small \italic "change bow at will" | c1\ppp\fermata\laissezVibrer |
}
codaCb = {
  c,8\f \repeat unfold 7 { c,8 } | \repeat unfold 8 { c,8 } | \repeat unfold 8 { c,8 } | c,2.->\ff r4\fermata | R1*4 |
  % c341: sul A 176-178 as at 2-3: the whole-bar D2 at 177 is stopped (A string, third position), not the open D string under the cellos' stopped D3 (c251 sul G); Adler adler1 PDF 73-74, 76, 106
  g,,1\pp | \once \override TextSpanner.bound-details.left.text = \markup \italic \small "sul A" es,1\startTextSpan | d,1 | c,2 des,2\stopTextSpan | c,1~^\markup \italic "change bow at will" | c,1~ | c,1~\> | c,1\ppp\fermata |
}
codaFluteOne = {
  es'''1\f | es'''2 es'''2 | f'''1\< | f'''2.->\ff r4\fermata |
  R1*11 | R1\fermata |
}
% c164: Fl 2 c'''/c'''/c'''/d''' (was g''1 | g''2 aes''2 | aes''1 | aes''2.): the upper winds in close position under Fl 1's E-flat6/F6, filling the empty sixth;
% Fl 2 no longer makes a third unison with Ob 1 and Cl 1 on G5/A-flat5 (Adler adler1 PDF 257: upper woodwinds in close position, wider gaps toward the bass; unison doubling
% only yields a stronger pitch; Ex. VIII-26/27, PDF 258). Dvorak 9/i: held flute pairs lie within a sixth in 57 of 58 cases.
codaFluteTwo = {
  c'''1\f | c'''1 | c'''1\< | d'''2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
  R1*7 | R1\fermata |
}
codaOboeOne = {
  g''1\f | g''2 aes''2 | aes''1\< | aes''2.->\ff r4\fermata |
  R1*11 | R1\fermata |
}
codaOboeTwo = {
  es''1\f | es''1 | c''1\< | d''2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
  R1*7 | R1\fermata |
}
codaClTwo = {
  es'1\f | es'2 es'2 | c'1\< | d'2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
  R1*7 | R1\fermata |
}
codaBsnOne = {
  % c097: Bsn 1 G3 at 174 fills the G2-E-flat4 gap under the cadential 6/4 and hands the G3 to Tbn 1 at 175
  % c150: 167-170 Bsn 1 doubles the cellos' tenor line, as Bsn 1 + Vc do at 27-30 (its G3/A-flat3 stay in Hn 4 and Tbn 2);
  % alone at f under the ff brass head the line was covered (Rimsky-Korsakov PDF 18, his own Golden Cockerel 233 note)
  c'2\f es'2 | es'2 f'2 | es'2\< c'2 | d'2.->\ff r4\fermata | R1 | R1 | R1 | g1\pp |
  R1*7 | R1\fermata |
}
codaCbsn = {
  c,,1\f | c,,1 | c,,1\< | c,,2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
  R1*7 | R1\fermata |
}
codaHnTwo = {
  r8 g8\ff( es'4.->) d'8( des'8 c'8 | c'4--) b8( c'8) aes4.-> g8 | r8 g8( f'4.->) es'8( d'8 c'8) | b2.-> r4\fermata | R1 | R1 | R1 | R1 |
  R1*7 | R1\fermata |
}
codaTptOne = {
  \partCombineUnisono r8 g'8\ff( es''4.->) d''8( des''8 c''8 | c''4--) b'8( c''8) aes'4.-> g'8 | r8 g'8( f''4.->) es''8( d''8 c''8) | b'2.-> r4\fermata \partCombineAutomatic |
  R1*11 | R1\fermata |
}
codaTptTwo = {
  r8 g'8\ff( es''4.->) d''8( des''8 c''8 | c''4--) b'8( c''8) aes'4.-> g'8 | r8 g'8( f''4.->) es''8( d''8 c''8) | b'2.-> r4\fermata |
  R1*11 | R1\fermata |
}
codaTptThree = {
  es'1\f | es'1 | f'1\< | f'2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
  R1*7 | R1\fermata |
}
codaTbnOne = {
  es'1\f | es'1 | c'1\< | d'2.->\ff r4\fermata |
  R1*4 | g1(\pp_\markup \italic "dolce" | es'1) | d'1( |
  c'2 des'2 | c'1) \breathe | c'1~\> | c'4\ppp r4 r2 | R1\fermata | % c156: breath after 179 and a soft restrike at 180 (was tied: one breath 177-181, about 19 s; Adler PDF 292, 309; adler2 PDF 3). The C still overlaps Hn 3's entry at 181 (c140).
}
codaTbnTwo = {
  g1\f | g2 aes2 | aes1\< | aes2.->\ff r4\fermata |
  R1*4 | es1(\pp-\tag #'part _\markup \italic "dolce" | g1) | f1( | % c188: slurs as Tbn 1 and B.tbn (they were only in the score's combined chord, not in the Tbn 2 part; Adler adler1 PDF 309, 321)
  g2 f2 | es1) | R1*2 | R1\fermata |
}
codaBassTbn = {
  c1\f | c1 | c1\< | c2.->\ff r4\fermata |
  R1*4 | g,1(\pp_\markup \italic "dolce" | es1) | d1( |
  c2 des2 | c1\>) | R1\! | R1 | R1\fermata | % c328: fades out under Vc/Cb, as the bass clarinet (Rimsky-Korsakov PDF 130)
}
codaTuba = {
  c,1\f | c,1 | c,1\< | c,2.->\ff r4\fermata |
  R1*11 | R1\fermata |
}
% c400: D-flat5 held for two beats at 173.3-4 and C5 on the downbeat of 174 (was des''4 c''4~ c''2): the N6 lasts beats 3-4 with flat-2 on top while the solo cello arpeggiates F-A-flat under it, and flat-2 reaches C only over the cadential 6/4, from where the solo cello takes it to B4 (A&S PDF 483, 484 Ex. 28-2c, 499 Pt 3); the motto's D-flat is a minim falling to C on the downbeat, as at 3, 178 and 180
codaCorAnglais = { R1*3 | r2. r4\fermata | \tag #'score r2. \tag #'part \cueDuring #"cueVc" #DOWN { s4*0^\markup \fontsize #-3 "Vc." r2. } g'4(\p_\markup \italic "espr." | es''2.~ es''8 d''8~ | d''4 c''4 des''2 | c''2) r2 | R1*7 | R1\fermata | }

% c366: part only, the beater change is announced in the rests before the entry (Adler part 2 PDF 70 Ex. XII-22 'take brushes', 'take bow'; PDF 59 q. 1)
codaPerc = \drummode { R1*3 | r2. r4\fermata | \tag #'part { R1*4^\markup \small \italic "take soft stick" } \tag #'score { R1*4 } | tt1\pp\laissezVibrer^\markup { "Tam-tam" \italic "soft stick, l.v." } | R1*6 | R1\fermata _\markup \small \italic "damp" | }  % c276: the tam-tam stops with the harp, basses and timpani at the end of 182, so nothing but the five tied parts crosses into movement II (Adler part 2 PDF 71, 73 Ex. XII-29)

% c095: final-bar fermata over the rest (Dvořák 7/ii Mutopia, resting winds: R1 \fermata)
codaHarpR = { R1*3 | r2. r4\fermata | R1*11 | R1\fermata | }
