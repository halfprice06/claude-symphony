% FIRST THEME, bars 15–32 (Allegro appassionato).
% c102: Hn 4 24–25 holds G (was G–C under the melody D–G: parallel fifths).

tOneFluteOne = {
  R1 | R1 | R1 | R1 |
  R1 | R1 | R1 | R1 |
  % 23–25: Fl1 at the violin octave (top line rises into 26/27; A♭6 first at 31)
  \partCombineSoloI es''4(\mf\<^\markup \bold "1." d''4 c''4) f''4( | es''4 d''4) g''4( f''4 | es''4) aes''4( g''4 f''4) | \partCombineAutomatic b''2.->\ff r4 |
  \partCombineApart r8 g''8( es'''4.->) d'''8( des'''8 c'''8 | c'''4--) b''8( c'''8) aes''4.-> g''8 | r8 g''8( f'''4.->) es'''8( d'''8 c'''8) | bes''8-. c'''-. des'''-. bes''-. g'''4.-> f'''8 |
  aes'''4.-> g'''8 f'''4 d'''4 | c'''4-> b''4-> r2 \partCombineAutomatic |
}
tOneFluteTwo = {
  R1*8 |
  % c144: Fl 2 rests 23-25 (was in unison with Fl 1, Ob 1 and Vln I on E-flat5-A-flat5) and enters on the ff stop chord at 26: crescendo by addition
  % (Adler adler2 PDF 150, Barber: the doubling grows bar by bar; PDF 151, Mozart: a flute in unison with the violins adds nothing; PDF 156: a rest before a colour enters)
  R1*3 | aes''2.->\ff r4 |
  % c104: C6 at 31 beats 1–2 (fifth of iv) fills the octave under the A♭6 peak
  g''1\ff | aes''1 | aes''1 | bes''1 | c'''2 f''2 | g''4-> g''4-> r2 | % c162: F5 (was A-flat5) at 31.3: A-flat5 over the D5 of Ob 1/Cl 1/Vln II fell to G5 over C5 (d5 to P5); F5 is the octave under the F6 melody note
 
}
tOneOboeOne = {
  R1*8 | \partCombineSoloI es''4(\mf\< d''4 c''4) f''4( | es''4 d''4) g''4( f''4 | es''4) aes''4( g''4 f''4) |
  \partCombineAutomatic f''2.->\ff r4 | \partCombineApart r8 g'8( es''4.->) d''8( des''8 c''8 | c''4--) b'8( c''8) aes'4.-> g'8 | r8 g'8( f''4.->) es''8( d''8 c''8) |
  bes'8-. c''-. des''-. bes'-. g''4.-> f''8 | aes''4.-> g''8 f''4 d''4 | c''4-> b'4-> r2 \partCombineAutomatic |
}
tOneOboeTwo = {
  R1*8 |
  % c119: Ob 2 rests 23-25 (it held the syncopated G-F line against Ob 1's melody: sevenths/ninths at 24.1, 24.4, 25.3; Rimsky-Korsakov PDF 90 rule 4: no discords between two oboes). The line stays in Cl 1, Hn 1, Vln II.
  R1*3 | d''2.->\ff r4 |
  g'1\ff | f'1 | aes'1 | g'1 | aes'2 f'2 | f'4-> f'4-> r2 |
}
tOneClOne = {
  R1 | R1 | R1 | R1 |
  R1 | R1 | R1 | R1 |
  g'2.\mf\<-> f'4->~ | f'2 g'2->~ | g'4 f'2.-> | b'2.->\ff r4 |
  \partCombineApart r8 g'8( es''4.->) d''8( des''8 c''8 | c''4--) b'8( c''8) aes'4.-> g'8 | r8 g'8( f''4.->) es''8( d''8 c''8) | bes'8-. c''-. des''-. bes'-. g''4.-> f''8 |
  aes''4.-> g''8 f''4 d''4 | c''4-> b'4-> r2 \partCombineAutomatic |
}
tOneClTwo = {
  R1*8 |
  es'2.\mf\<-> d'4->~ | d'2 es'2->~ | es'4 c'2.-> | aes'2.->\ff r4 |
  es'1\ff | d'1 | c'1 | des'1 | c'2 d'2 | % c162: 30 D-flat4 (was B-flat3): B-flat3 over the bass trombone's E3 rose to C4 over F3 (d5 to P5); D-flat, the seventh of the vii°7/iv, falls to C as in Tpt 1/Tbn 1 (A&S PDF 375, 406)
  d'4-> d'4-> r2 |
}
tOneBsnOne = {
  R1*4 | f2\mf aes,2 | des1 | f2 g2 |
  g2 c2 | c2.\<-> b,4->~ | b,2 c2->~ | c4 f2.-> |
  f2.->\ff r4 | c'2\ff es'2 | d'2 f'2 | es'2 c'2 |
  e'2 bes2 | aes2 f2 | g4-> g,4-> r2 |
}
tOneBsnTwo = {
  R1*8 |
  c2.\mf\<-> b,4->~ | b,2 c2->~ | c4 f,2-> d4 | d2.->\ff r4 | % c242: 25 beat 4 D3 (was A-flat2), repeated at the stop chord
  c1\ff | d1 | es1 | e1 | f2 d2 | g,4-> g,4-> r2 |
}
tOneCbsn = {
  % c152: 26 B1 (was D2): root-position vii°7 resolves B-C into 27; the 6/5 position with D falling to C under A-flat-G is Aldwell & Schachter's "poor" Ex. 22-4b (PDF 376)
  R1*11 | b,,2.->\ff r4 |
  c,4\ff c,4 c,4 c,4 | d,4 d,4 d,4 d,4 | es,4 es,4 es,4 es,4 | e,4 e,4 e,4 e,4 |
  f,4 f,4 d,4 d,4 | g,,4-> g,,4-> r2 |
}
tOneHnOne = {
  % c297: Hn 1-2 rest 23-24.2 and enter on the third hemiola cell (24.3), as at 136.3 (c177): they doubled Cl 1-2 at the unison from 23
  % (Adler adler1 PDF 257: overlapping robs both timbres; PDF 253/255: alter something the third time a sequence is scored alike; PDF 253: choirs apart, then together)
  R1*8 | R1 | r2 g'2->\mp\< ~ | g'4 f'2.-> |
  aes'2.->\ff r4 | g'1\ff | f'1 | aes'1 |
  g'1 | aes'2 aes'2 | g'4-> g'4-> r2 |
}
tOneHnTwo = {
  R1*8 |
  R1 | r2 es'2->\mp\< ~ | es'4 c'2.-> | f'2.->\ff r4 |
  es'1\ff | f'1 | f'1 | g'1 | f'2 f'2 | f'4-> f'4-> r2 | % c224: 30 G4 (was E4, the diminished seventh's bass; octaves with the bass E-F into 31; Rimsky-Korsakov PDF 83-84)
}
tOneHnThree = {
  R1*4 | c'1\p | des'1 | des'2 b2 |
  b4 d'4 c'2 | \clef bass c'2.\mp\<-> d'4->~ | d'2 c'2->~ | % c162: D4 (was B3) at 23.4-24.2: B3-F4 (Hn 3/Hn 1, Cl 1) rose to C4-G4, a d5 to P5 against the leading tone (Aldwell & Schachter PDF 83, 122)
  c'4 aes2.-> |
  % c192: 27-28 C4 tied into 28 and resolved to B3 on beat 2 with the tune (was c'1 | b1): the leading tone no longer sounds under the tune's C on the downbeat;
  % beat 1 reads as ii-half-dim7 over the dominant, as at 32 (A&S PDF 469: suspension weak when its resolution is anticipated; PDF 471: 5th, 7th, 9th above V form a II chord without the leading tone)
  d'2.->\ff r4 | \clef treble c'1\f~ | c'4 b2. | c'1 |
  des'1 | c'2 c'2 | c'4-> b4-> r2 |
}
tOneHnFour = {
  R1*4 | f1\p | f1 | f2 g2 |
  % c259: 25 beat 4 rest (was F2 held through the beat): when c242 moved the bass to D2 on beat 4, the held F2 made a minor third D2-F2 in the
  % lowest register under the crescendo (Rimsky-Korsakov PDF 124: harmonic intervals close together in the lowest octaves sound badly; Ex. 232);
  % the horn breathes and re-attacks F3 ff on the stop chord (PDF 136: brass re-entry at ff). Hn 3 keeps A-flat3, Bsn 1/Vc keep F3.
  g2 g2 | c2.\mp\<-> g,4->~ | g,2 g,2->~ | g,4 f,2-> r4 |
  % c139: 28 Hn 4 releases G3 on beat 3: it held the resolution note in the same octave under the violas' A-flat3 appoggiatura (Rimsky-Korsakov PDF 132-133: the basis stays an octave from the melodic design)
  f2.->\ff r4 | g1\f | g2 r2 | aes1 |
  bes1 | aes2 aes2 | g4-> g4-> r2 |
}
tOneTptOne = {
  R1*11 | b'2.->\ff r4 | c''4\f r8 c''8 c''4 r8 c''8 | g'4 r4 b'4 r4 |
  % c152: 30 D-flat5 (was B-flat4): the d5 E4-B-flat4 over Tpt 3 moved in similar motion to the fifth F4-C5 (Aldwell & Schachter PDF 375, Ex. 22-3c "avoid"); the d7 E4-D-flat5 resolves inward to F4-C5 (Ex. 22-2), and C-D-flat-C is the 5-6-5 neighbour of the diminished seventh (PDF 377)
  c''1 | des''4 r8 des''8 des''4 r8 des''8 | c''2 aes'2 | g'4->\ff g'4-> r2 |
}
tOneTptTwo = {
  % c224: 28 G4 (was F4), 30 B-flat4 (was G4): Tpt 3 leaves the bass line (see tOneTptThree); the trumpets keep the upper chord tones in normal order (Rimsky-Korsakov PDF 90 rule 2)
  R1*11 | f'2.->\ff r4 | g'4\f r8 g'8 g'4 r8 g'8 | g'4 r4 g'4 r4 |
  aes'1 | bes'4 r8 bes'8 bes'4 r8 bes'8 | aes'2 f'2 | f'4->\ff f'4-> r2 |
}
% c224: 28-31 Tpt 3 F4-F4-G4-A-flat4/F4 (was D4-E-flat4-E4-F4/D4, the chromatic bass two octaves up): the bass of V4/3 (28), iv4/2 (29) and the
% diminished seventh (30) is no longer doubled in an upper part, and the trumpet no longer moves in octaves with the bass (Rimsky-Korsakov PDF 82 note, 83-84)
tOneTptThree = { R1*11 | d'2.->\ff r4 | es'4\f r8 es'8 es'4 r8 es'8 | f'4 r4 f'4 r4 | f'1 | g'4 r8 g'8 g'4 r8 g'8 | aes'2 f'2 | d'4-> d'4-> r2 | }
% c152: 30 D-flat4 (was B-flat3): same d5-to-fifth motion against the bass trombone's E3 (Aldwell & Schachter PDF 375); D-flat4 resolves to C4 as in Tpt 1
% c192: 27-28 C4 tied and resolved to B3 on beat 2, as Hn 3 (see tOneHnThree)
tOneTbnOne = { R1*11 | aes2.->\ff r4 | c'1\f~ | c'4 b2. | c'1 | des'1 | c'2 c'2 | c'4-> b4-> r2 | }
tOneTbnTwo = { R1*11 | f2.->\ff r4 | g1\f | f1 | aes1 | g1 | aes2 aes2 | g4-> g4-> r2 | }
tOneBassTbn = { R1*11 | b,2.->\ff r4 | c1\f | d1 | es1 | e1 | f2 d2 | g,4-> g,4-> r2 | }
tOneTuba = { R1*11 | b,,2.->\ff r4 | c,1\f | d,1 | es,1 | e,1 | f,2 d,2 | g,,4-> g,,4-> r2 | }
tOneTimp = {
  % c134: timpani on the ff stop chord at 26, as at 138 (Rimsky-Korsakov appendix of tutti chords, PDF 505-507: timpani in every f/ff tutti chord)
  R1^\markup \small "medium sticks" | R1*10 | g,2.->\ff r4 | c4\ff r8 c8 c4 r8 c8 | g,4 r4 g,4 r4 | R1 |
  c4 r8 c8 c4 r8 c8 | R1 | g,4-> g,4-> r2 |
}
tOneVlnOne = {
  r8 g'8\downbow\f( es''4.->) d''8( des''8 c''8 | c''4--) b'8\upbow( c''8) aes'4.-> g'8 | r8 g'8\downbow( f''4.->) es''8( d''8 c''8 | b'4) d''8( c''8) g'2 |
  r8 aes'8\downbow\<( aes''4.->) g''8( f''8 es''8 | des''8 es''8 f''8 aes''8) des'''2~\sf | des'''8\>( c'''8 bes''8 aes''8) g''4.-> f''8 | es''8( d''8 c''8 b'8) c''4\mf r4 |
  es''4(\< d''4 c''4) f''4( | es''4 d''4) g''4( f''4 | es''4) aes''4( g''4 f''4) | b''2.->\ff r4 |
  r8 g''8\downbow\ff( es'''4.->) d'''8( des'''8 c'''8 | c'''4--) b''8\upbow( c'''8) aes''4.-> g''8 | r8 g''8\downbow( f'''4.->) es'''8( d'''8 c'''8) | bes''8-. c'''-. des'''-. bes''-. g'''4.-> f'''8 |
  \ottava #1 aes'''4.-> g'''8 f'''4 d'''4 \ottava #0 | c'''4->\downbow b''4->\downbow r4 f''16(\< g'' aes'' b'') |
}
tOneVlnTwo = {
  % c227: 15 and 17 the syncopation enters on beat 2-and, under the theme's held E-flat5/F5, not on beat 1-and with the motto's pickup G4 (Vln II doubled it
  % at the unison at 15 and sounded A-flat4 against it at 17); 16 and 18 already move only where the tune holds (Adler adler1 PDF 135: the background adds
  % intensity to the melody's longer notes and leaves its anacrusis figure undisturbed; PDF 132: radical rhythmic difference between foreground and background)
  r4 r8 g'8~\mf g'2 | r8 g'8~ g'4 r8 f'8~ f'4 | r4 r8 aes'8~ aes'2 | r8 f'8~ f'4 r8 d'8~ d'4 |
  r4 r8 c'8~\mp c'2 | % c294: 19 enters on 2-and under the held A-flat5, not with the pickup A-flat4 on 1-and (as c227 at 15/17; Adler adler1 PDF 135: background leaves the anacrusis undisturbed)
  % c121: 20.3-21.2 Vln II doubles the D♭6 peak and its descent an octave below, then resumes the syncopation (Rimsky-Korsakov PDF 58-59, 62 Note I:
  % a violin melody in the very high register is isolated from the ensemble unless doubled in octaves; as at 60-63 and 139-142). Hn 3 holds the D♭ the syncopation left.
  r8 des'8~ des'4 des''2~\sf | des''8\>( c''8 bes'8 aes'8) r8 d'8~\mp d'4 | r8 d'8~ d'4 r8 g'8~ g'4 |
  g'4\mf\<-> g'4 g'4 f'4-> | f'4 f'4 g'4-> g'4 | g'4 f'4-> f'4 f'4 | <d'' aes''>2.->\ff r4 |
  r8 g'8\downbow\ff( es''4.->) d''8( des''8 c''8 | c''4--) b'8\upbow( c''8) aes'4.-> g'8 | r8 g'8\downbow( f''4.->) es''8( d''8 c''8) | bes'8-. c''-. des''-. bes'-. g''4.-> f''8 |
  aes''4.-> g''8 f''4 d''4 | c''4->\downbow b'4->\downbow r4 f'16(\< g' aes' b') |
}
tOneVla = {
  r4 r8 es'8~\mf es'2 | r8 es'8~ es'4 r8 d'8~ d'4 | r4 r8 <d' f'>8~ <d' f'>2 | r8 d'8~ d'4 r8 b8~ b4 | % c227: entries at 15/17 on beat 2-and, as Vln II
  aes'2.~\mf\<(^\markup \italic "espr." aes'8 g'8 | f'2\f aes'2) | aes'4\>( g'4 f'2~ | f'2\mf es'2) |
  es'4\<-> es'4 es'4 d'4-> | d'4 d'4 es'4-> es'4 | es'4 c'4-> c'4 c'4 | <f' b'>2.->\ff r4 |
  r8 g8\downbow\ff( es'4.->) d'8( des'8 c'8 | c'4--) b8\upbow( c'8) aes4.-> g8 | r8 g8\downbow( f'4.->) es'8( d'8 c'8) | bes8-. c'8-. des'8-. bes8-. g'4.-> f'8 |
  aes'4.-> g'8 f'4 d'4 | <d' f'>4->\downbow <d' f'>4->\downbow r2 |
}
tOneVc = {
  % c278: Vc/Cb mf under the f tune (was f): the bass is a level below the primary line (Sebesky PDF 13-14, focus), and 19 keeps the level
  % with Bsn 1 added instead of dropping f->mf where the continuation crescendos to the sf at 20
  c2\mf d2 | es2 d2 | f2 aes2 | g2 g,2 |
  f2 aes,2 | des1 | f2 g2 | g2 c2 |
  c2.\<-> b,4->~ | b,2 c2->~ | c4 f2.-> | <b, aes>2.->\ff r4 |
  c'2\ff es'2 | d'2 f'2 | es'2 c'2 | e'2 bes2 |
  aes2 f2 | g4->\downbow g,4->\downbow r2 |
}
tOneCb = {
  c,4\mf r8 c,8 c,4 r8 c,8 | c,4 r8 c,8 g,,4 r8 g,,8 | aes,,4 r8 aes,,8 aes,,4 r8 aes,,8 | g,,4 r8 g,,8 g,,4 r8 g,,8 | % c278: mf (was f), as Vc
  f,,4 r8 f,,8 f,,4 r8 f,,8 | des,4 r8 des,8 des,4 r8 des,8 | f,,4 r8 f,,8 g,,4 r8 g,,8 | g,,4 r8 g,,8 c,4 r8 c,8 |
  % c242: 25 beat 4 D2 (was A-flat1): iv - ii(half-dim)7 - vii°7 by falling thirds, no augmented second A-flat-B in the bass into the stop chord (Aldwell & Schachter Ex. 11-14b, PDF 171; Unit 12, PDF 179)
  c,4\<-> c,4 c,4 b,,4-> | b,,4 b,,4 c,4-> c,4 | c,4 f,,4-> f,,4 d,4 | b,,2.->\ff r4 |
  c,8\ff \repeat unfold 7 c,8 | \repeat unfold 8 d,8 | \repeat unfold 8 es,8 | \repeat unfold 8 e,8 |
  \repeat unfold 4 f,8 \repeat unfold 4 d,8 | g,,4->\downbow g,,4->\downbow r2 |
}
