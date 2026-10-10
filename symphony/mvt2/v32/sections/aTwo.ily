% A' SECTION, bars 71-82 (3/4).
% 71-78: the theme in Vln I (upper octave) and Vln II; cellos and horns 1-2 play the counter-melody of bar 23.
%        The cadence at 78 is deceptive (F minor).
% c023 (proposed): 78 b1-2 is flat VI (F flat major) under the melody's A flat, the common tone (A&S PDF 585-587, Widmung;
%        PDF 592-593, flat VI by deceptive cadence), F flat-F in the bass to vi on beat 3 (chromatic inflection, PDF 584-585).
% 79-82: the cadential bars again, ff, peak F6 at 79, full close at 82.
% v03's closing 83-90 (clarinet theme head, horn motto tail over a tonic pedal) is cut (critic 003).

aTwoVlnOne = {
  aes''4. c'''8) es'''4~\< | es'''4 d'''4(\> des'''4) | c'''4.(\! bes''8 aes''4 | g''2) es''8( f''8 |
  aes''4.\mp\< c'''8) f'''4~ | f'''4 bes'''4( aes'''4) | g'''4( es'''8 des'''8 c'''8 bes''8 | aes''2)\f \afterGrace c'''4 { f'''16( g''' aes''' } |
  bes'''2.)~\ff | bes'''4(\upbow aes'''2) | g'''4(\> es'''8 des'''8 c'''8 bes''8) | \after 2 \pp aes''2.\p\> |  % c028: p > pp by beat 3 so the harp harmonics (pickup to the coda) are heard (Adler part 2 PDF 503, 505)
}
aTwoVlnTwo = {
  aes'4. c''8) es''4~\< | es''4 d''4(\> des''4) | c''4.(\! bes'8 aes'4 | g'2) es'8( f'8 |
  aes'4.\mp\<^\markup \italic "ord." c''8) f''4~ | f''4 bes''4( aes''4) | g''4( es''8 des''8 c''8 bes'8 | aes'2)\f \afterGrace c''4 { f''16( g'' aes'' } |
  bes''2.)~\ff | bes''4(\upbow aes''2) | g''4(\> es''8 des''8 c''8 bes'8) | \after 2 \pp aes'2.\p\> |
}
aTwoFluteOne = {
  R2.*4 |
  aes''4.(\mp\< c'''8 f'''4~ | f'''4 bes'''4 aes'''4 | g'''4 es'''8 des'''8 c'''8 bes''8 | aes''2)\f c'''4( |
  bes'''2.~\ff | bes'''4 aes'''2) \breathe | g'''4(\> es'''8 des'''8 c'''8 bes''8 | \after 2 \pp aes''2.)\p\> |
}
% c014: flute 2 and oboe 2 double the upper harmony against four horns ff (Rimsky-Korsakov PDF 108-109).
aTwoFluteTwo = { R2.*8 | f'''2.~\ff | f'''2. | R2.*2 | }
aTwoOboeTwo = { R2.*8 | f''2.~\ff | f''4 f''4 bes'4 | g'2.\> | \after 2 \pp aes'2.\p\> | }  % c024: F5 fills the sixth between D flat5 and B flat5 (Rimsky-Korsakov appendix PDF 505-507: close spacing in the upper winds; PDF 125); B flat4 at 80 b3 leads to the old G4
aTwoOboeOne = {
  R2.*8 |
  bes''2.~(\ff | bes''4 aes''2) | g''4(\> es''8 des''8 c''8 bes'8 | \after 2 \pp aes'2.)\p\> |
}
aTwoVla = {
  c'8(\pp^\markup \italic "unis., ord., espr." es' aes') es'( c' aes) | c'( aes' bes) aes'( bes g') | c'( es' aes') c'( es' aes) | bes( es' g') es'( bes es') |
  c'(\p\< es' aes') es'( aes f') | f'( aes' f') bes( des' bes) | g( bes es') g'( es' des') | ces'(\f fes' aes') fes'( c' aes) |
  <f' aes'>2.:32\ff^\markup \italic "div." | <f' aes'>4:32 <f' aes'>4:32 <f' aes'>4:32 | <es' g'>2.:32\> | \after 2 \pp <es' aes'>2.\p\> |
}
aTwoVc = {
  es2\p^\markup \italic "cantabile" aes8( g8 | f2) g4( | aes2 c'4) | bes2. |
  es2(\mp\< f4) | aes2( des'4) | bes2( des'4) | ces'2\f aes4 |
  des'4\ff c'4 bes4 | aes4( bes4 des'4) | bes2\> des'4 | \after 2 \pp c'2.\p\> |
}
aTwoHnOne = {
  R2.*7 | \partCombineUnisono r2 c'4(\f |
  des'4\ff c'4 bes4 | aes4 bes4 des'4) \breathe | bes2(\> des'4 | \after 2 \pp c'2.)\p\> \partCombineAutomatic |
}
% c006: the 71-78 counter-melody moves to horn 2, so horn 1 rests after its solo at 67-70.
aTwoHnTwo = {
  es2\p aes8( g8 | f2 g4 | aes2 c'4 | bes2.) |
  es2(\mp\< f4 | aes2 des'4 | bes2 des'4) | r2 c'4(\f |
  des'4\ff c'4 bes4 | aes4 bes4 des'4) \breathe | bes2(\> des'4 | \after 2 \pp c'2.)\p\> |
}
aTwoHnThree = { R2.*8 | f'2.\ff | f'4 f'4 f'4 | es'2.\> | R2.\! | }  % c024: horns 3-4 leave first in the diminuendo (Rimsky-Korsakov PDF 130). c014: horns 3-4 in the middle of the chord, bass left to Bsn 2 and B.cl. (Rimsky-Korsakov PDF 101, 108)
aTwoHnFour = { R2.*8 | aes2.\ff | aes4 aes4 aes4 | g2.\> | R2.\! | }
aTwoClOne = {
  c''2.\pp | c''4 bes'4 bes'4 | c''2. | bes'2. |
  c''2.\p\< | des''4 des''4 des''4 | bes'2. | aes'2.\f |
  des''2.\ff | des''4 des''4 des''4 | bes'2.\> | \after 2 \pp c''2.\p\> |
}
aTwoClTwo = {
  aes'2.\pp | aes'4 f'4 g'4 | aes'2. | g'2. |
  aes'2.\p\< | aes'4 aes'4 bes'4 | g'2. | aes'2\f aes'4 |
  aes'2.\ff | aes'4 aes'4 aes'4 | g'2.\> | \after 2 \pp aes'2.\p\> |
}
% c011: bassoon 1 joins the cello and horn counter-melody at the ff return (Rimsky-Korsakov PDF 54, 56: relief by doubling; Antar [63] cellos doubled by bassoons).
aTwoBsnOne = { R2.*7 | r2 c'4( | des'4\ff c'4 bes4 | aes4 bes4 des'4) \breathe | bes2(\> des'4 | \after 2 \pp c'2.)\p\> | }
aTwoBsnTwo = {
  aes,2.\pp | f4 bes,4 es4 | aes,2 c4 | es2. |
  aes,4\p\< c4 des4 | des2 bes,4 | es2. | fes2\f f4 |
  des2.\ff | des2 bes,4 | es2.\> | \after 2 \pp aes,2.\p\> |
}
% c024: contrabassoon doubles the double basses at the A' peak, so the ff bass has more than the double basses at 16' pitch
% (Rimsky-Korsakov, appendix of single tutti chords, PDF 505-507: every ff chord doubles the bass in the low octave with C-fag./tuba + Cb.).
aTwoCbsn = { R2.*8 | des,2.\ff | des,2 bes,,4 | es,2.\> | aes,,2\p\> r4\! | }
aTwoBassCl = { R2.*8 | des2.\ff | des2 bes,4 | es,2.\> | \after 2 \pp aes,2.\p\> | }
aTwoCb = {
  aes,,2.\pp | f,4 bes,,4 es,4 | aes,,2 c,4 | es,2. |
  aes,,4\p\< c,4 des,4 | des,2 bes,,4 | es,2. | fes,2\f f,4 |
  des,2.\ff | des,2 bes,,4 | es,2.\> | \after 2 \pp aes,,2.\p\> |
}
aTwoTimp = { R2.*8 | des2.:32\f | des2.:32 | es2.:32\> | \after 2 \pp aes,2.\p\> | }
aTwoHarpR = {
  r4 <aes c' es'>2\arpeggio | R2. | r4 <aes c' es'>2\arpeggio | r4 <g bes es'>2\arpeggio |
  r4 <aes c' es'>2\arpeggio | <aes des' f'>4\arpeggio r2 | r4 <g bes des'>2\arpeggio | r2 <aes c' f'>4\arpeggio |
  r4 <aes des' f'>2\arpeggio | <aes des' f'>4\arpeggio r2 | r4 <g bes des'>2\arpeggio | r4 <aes c' es'>4\arpeggio << \new Voice \with { \remove "Note_performer" } { \voiceOne es8-\flageolet^\markup \small \italic "harm. (sound 8va)" f8-\flageolet } \new Voice { \voiceTwo \hideNotes es'8 f'8 \unHideNotes } >> |  % c026: octave harmonics, written an octave below the sound (Adler part 1 PDF 116); hidden voice carries the sounding pitch to MIDI  % c019: harp head starts here (pickup), so the timpani answer and the Vln I tail in the coda do not overlap
}
aTwoHarpL = {
  \set Staff.ottavationMarkups = #ottavation-numbers \ottava #-1 % c025: as at 7-14 (Gould PDF 46-47)
  <aes,, es,>2.\pp\arpeggio^\markup \small \harp-pedal #"^-^|^--^" | <f,, c,>4\arpeggio <bes,, f,>4\arpeggio <es,, bes,,>4\arpeggio | <aes,, es,>2\arpeggio c,4 | <es,, es,>2.\arpeggio |
  <aes,, es,>4\p\arpeggio c,4 des,4 | <des, aes,>2\arpeggio bes,,4 | <es,, bes,,>2.\arpeggio | r2 <f,, c,>4\arpeggio |
  <des, aes,>2.\f\arpeggio | <des, aes,>2\arpeggio bes,,4 | <es,, bes,,>2.\>\arpeggio | <aes,, es,>2.\p\arpeggio |  % c026: 8 bassa continues into 83 (no loco needed)  % c019: harp dies away with the orchestra (was f to the end)
}
