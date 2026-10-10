% CODA, bars 167–182 (v100 numbering; 171–186 before cycle 80). Forte C minor (167–170: brass take the first-theme head; fermata on the denied tutti, vii°7 with Tpt/Hn on B♮),
% then the second theme's head returns in C minor in the cellos (171–174, no pickup) against the cor anglais's motto (pickup 171, 172–174);
% bass clarinet, low strings and three trombones (pp chorale, tam-tam at 175) state the motto in augmentation (175–179); Cl1 recalls the intro horn call E♭–C–B (175–177);
% the violins' last motto (177–182) sinks through the Neapolitan to C, and the violas alone turn the minor third to major at the very end (E♭ 181 → E♮ 182).
% Rotation: 167–170 stand where the codetta 69–72 stood (after the S cadence, Tempo dell'Allegro, forte, 4 bars) and 171–174 where the
% flute motto 73–76 stood; the closing zone returns in C minor, split into its P and S components. Do not insert a C-major codetta after 166.

codaClOne = {
  % c096: Cl 1 breathes on beat 1 of 167 after the unbroken counterline 162-166 (E-flat at 166 kept); Ob 1 holds the same g'' from the downbeat
  \partCombineApart r4\f g''2. | \partCombineAutomatic g''2 aes''2 | aes''1\< | aes''2.->\ff r4\fermata |
  R1*4 | r2. es'4(\pp | c''1~ | c''2 b'2) |
  R1*4 | R1\fermata |
}
codaBassCl = {
  c1\f | c1 | c1\< | c2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
  g,1\pp( | es1) | d1( | c2 des2 | c1) | R1*2 | R1\fermata |
}
codaBsnTwo = {
  c1\f | c1 | c1\< | c2.->\ff r4\fermata | c1\pp | f1 | f1 | g,1 |
  R1*7 | R1\fermata |
}
codaHnOne = {
  \partCombineUnisono r8 g8\ff( es'4.->) d'8( des'8 c'8 | c'4) b8( c'8) aes4.-> g8 | r8 g8( f'4.->) es'8( d'8 c'8) | b2.-> r4\fermata \partCombineAutomatic |
  R1*11 | R1\fermata |
}
codaHnThree = {
  \clef treble c'1\f | c'1 | c'1\< | d'2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
  % c097: Hn 3 takes C4 from 180 (fills the C3-E-flat4 gap when the chorale stops); Hn 4 takes G3 (fifth above the bass octave, C2-C3-G3-C4 as in the harmonic series)
  R1*5 | c'1\ppp~^\markup \bold "3." | c'1~ | c'1\fermata |
}
codaHnFour = {
  g1\f | g2 aes2 | aes1\< | aes2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
  R1*6 | g1\ppp~ | g1\fermata |
}
codaTimp = {
  c1:32\f~ | c1:32~ | c1:32\< | c4->\ff r4 r4 r4\fermata | R1 | R1 | R1 | g,1:32\pp |
  R1*4 | c4\pp r4 c4 r4 | c4 r4 c4 r4 | c1:32\ppp~ | c1:32\fermata |
}
codaHarpL = {
  R1 | R1 | R1 | r2. r4\fermata | R1 | R1 | R1 | R1 |
  R1*7 | <c, g, c>1\ppp\laissezVibrer\fermata |
}
codaVlnOne = {
  <g'' es'''>1:32\f^"div." | <g'' es'''>2:32 <aes'' es'''>2:32 | <aes'' f'''>1:32\< | <aes'' f'''>2.:32->\ff r4\fermata |
  R1*6 | r2. g'4(\pp^"unis." | es''1)~ | es''2. d''4( |
  c''2 des''2) | c''1~\> | c''1\ppp\fermata \textEndMark \markup \italic "attacca" | % attacca into movement II (common-tone link; movement II thread, 2026-10-10)
}
codaVlnTwo = {
  <c'' g''>1:32\f^"div." | <c'' g''>2:32 <c'' aes''>2:32 | <c'' aes''>1:32\< | <d'' aes''>2.:32->\ff r4\fermata |
  % c107: Vln II rests 171-174 (its A-flat4 sat on the cello's tenuto peak at 172; background left to violas and bassoon, Adler PDF 135, 146);
  % it re-enters with the chorale at 175.
  R1*4 |
  es'1\pp^"unis." | g'1 | f'1 | g'2 f'2 |
  g'1 | g'2 f'2 | g'1~\> | g'1\ppp\fermata |
}
codaVla = {
  r8 g8\downbow\ff( es'4.->) d'8( des'8 c'8 | c'4) b8\upbow( c'8) aes4.-> g8 | r8 g8\downbow( f'4.->) es'8( d'8 c'8) | <d' f'>2.-> r4\fermata |
  % c127: A-flat3 on 173 beats 3-4 (was F4, above the cello solo's D-flat4): the viola stays under the solo, the N6 is complete (F-A-flat-D-flat)
  % (Adler PDF 274: accompaniment registrally distant from the soloist)
  c'2\pp( b2 | c'1) | c'2 aes2 | es'2 d'2 |
  c'1 | c'1 | aes1 | es'2 aes2 |
  es'1 | es'2 aes2 | es'1\>^\markup \italic "morendo" | e'1\ppp\fermata |
}
codaVc = {
  c'2\f es'2 | es'2 f'2 | es'2\< c'2 | d'2.->\ff r4\fermata | \clef tenor es'2.~(\mp\<^\markup \italic "espr." es'8 d'8\> | c'4\! aes'2--\< g'4\!) | f'4.( es'8 des'4 f'8\< aes'8 | c''2\> b'2\!) |
  \clef bass g,1\pp( | es1) | d1 | c2( des2) | c1 | c1 | c1~\> | c1\ppp\fermata |
}
codaCb = {
  c,8\f \repeat unfold 7 { c,8 } | \repeat unfold 8 { c,8 } | \repeat unfold 8 { c,8 } | c,2.->\ff r4\fermata | R1*4 |
  g,,1\pp | es,1 | d,1 | c,2 des,2 | c,1~^\markup \italic "change bow at will" | c,1~ | c,1~\> | c,1\ppp\fermata |
}
codaFluteOne = {
  es'''1\f | es'''2 es'''2 | f'''1\< | f'''2.->\ff r4\fermata |
  R1*11 | R1\fermata |
}
codaFluteTwo = {
  g''1\f | g''2 aes''2 | aes''1\< | aes''2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
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
  g1\f | g2 aes2 | aes1\< | aes2.->\ff r4\fermata | R1 | R1 | R1 | g1\pp |
  R1*7 | R1\fermata |
}
codaCbsn = {
  c,,1\f | c,,1 | c,,1\< | c,,2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
  R1*7 | R1\fermata |
}
codaHnTwo = {
  r8 g8\ff( es'4.->) d'8( des'8 c'8 | c'4) b8( c'8) aes4.-> g8 | r8 g8( f'4.->) es'8( d'8 c'8) | b2.-> r4\fermata | R1 | R1 | R1 | R1 |
  R1*7 | R1\fermata |
}
codaTptOne = {
  \partCombineUnisono r8 g'8\ff( es''4.->) d''8( des''8 c''8 | c''4) b'8( c''8) aes'4.-> g'8 | r8 g'8( f''4.->) es''8( d''8 c''8) | b'2.-> r4\fermata \partCombineAutomatic |
  R1*11 | R1\fermata |
}
codaTptTwo = {
  r8 g'8\ff( es''4.->) d''8( des''8 c''8 | c''4) b'8( c''8) aes'4.-> g'8 | r8 g'8( f''4.->) es''8( d''8 c''8) | b'2.-> r4\fermata |
  R1*11 | R1\fermata |
}
codaTptThree = {
  es'1\f | es'1 | f'1\< | f'2.->\ff r4\fermata | R1 | R1 | R1 | R1 |
  R1*7 | R1\fermata |
}
codaTbnOne = {
  es'1\f | es'1 | c'1\< | d'2.->\ff r4\fermata |
  R1*4 | g1(\pp | es'1) | d'1( |
  c'2 des'2 | c'1) | R1*2 | R1\fermata |
}
codaTbnTwo = {
  g1\f | g2 aes2 | aes1\< | aes2.->\ff r4\fermata |
  R1*4 | es1\pp | g1 | f1 |
  g2 f2 | es1 | R1*2 | R1\fermata |
}
codaBassTbn = {
  c1\f | c1 | c1\< | c2.->\ff r4\fermata |
  R1*4 | g,1(\pp | es1) | d1( |
  c2 des2 | c1) | R1*2 | R1\fermata |
}
codaTuba = {
  c,1\f | c,1 | c,1\< | c,2.->\ff r4\fermata |
  R1*11 | R1\fermata |
}
codaCorAnglais = { R1*3 | r2. r4\fermata | \tag #'score r2. \tag #'part \cueDuring #"cueVc" #DOWN { s4*0^\markup \fontsize #-3 "Vc." r2. } g'4(\p_\markup \italic "espr." | es''2.~ es''8 d''8~ | d''4 c''4 des''4 c''4~ | c''2) r2 | R1*7 | R1\fermata | }

codaPerc = \drummode { R1*3 | r2. r4\fermata | R1*4 | tt1\pp\laissezVibrer^\markup { "1: Tam-tam" \italic "soft stick, l.v." } | R1*6 | R1\fermata | }

% c095: final-bar fermata over the rest (Dvořák 7/ii Mutopia, resting winds: R1 \fermata)
codaHarpR = { R1*3 | r2. r4\fermata | R1*11 | R1\fermata | }
