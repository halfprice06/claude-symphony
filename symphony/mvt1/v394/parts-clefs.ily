\version "2.24.0"
% c185: clef plans for parts whose written (transposed) range differs from the concert-pitch score staff.
% Run with PARTS_AUDIT=1 PARTS_AUDIT_POS=9 to list notes with three or more ledger lines.

% Bass clarinet: treble clef in French notation, sounding a major 9th lower (Adler PDF 216-217 recommends it).
% 91-106 would need four or five ledger lines below the treble stave, so they go into the bass clef, read as players
% ordinarily read a bass-clef bass clarinet part: sounding a major 2nd lower (Adler PDF 171). The part's pitches stay
% a 9th above concert; for the bass-clef bars, middle C moves from stave position 6 to -1, so the notes print an octave lower.
bclBassClefMtwo = { \set Staff.middleCClefPosition = #-1 \context Staff \applyContext #ly:set-middle-C! }
% c196: the part stays in treble clef, French notation, throughout (Sebesky PDF 64, Ex. 72: the full bass-clarinet range written in treble
% clef with ledger lines; VSL, https://www.vsl.co.at/academy/woodwinds/bass-clarinet: German bass clef with French treble clef is a historical
% mixed system). Was: bass clef sounding a major 2nd lower at 91-106. The written C3-D3 there take 4-5 ledger lines, as low-C parts normally do.
bclClefs = { \clef treble }

% Horns: the score's bass clefs on the Hn 3·4 staff are dropped. Hn 1-3 stay in treble (two ledger lines at most).
% Hn 4 needs the bass clef at 11-12 and 23-25, in new notation (Adler PDF 304: in all new scores the horn in F
% sounds a fifth lower in both clefs). Clef changes fall in rests where possible (Gould PDF 22-23).
hnFourClefs = {
  s1*10 \clef bass
  s1*0_\markup \small \italic "bass clef in new notation: sounds a 5th lower"
  s1*2 \clef treble
  s1*10 \clef bass
  s1*3 \clef treble % back to treble at 26: the ff C4 and f D4 at 26-27 sit at or just below the treble stave
  s1*109 \clef bass s1*3 \clef treble % c393: 135-137 as 23-25
}
