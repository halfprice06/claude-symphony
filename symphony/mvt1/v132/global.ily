\version "2.24.0"
subP = #(make-dynamic-script (markup #:line (#:normal-text #:italic "sub." #:dynamic "p")))
pedAflat = \markup \harp-pedal #"^-^|^--^"
pedNat = \markup \harp-pedal #"---|----"
pedBflatAflat = \markup \harp-pedal #"--^|---^"
% MIDI-only tempo step: realises rit./allargando/largamente/fermatas in score.midi; prints nothing.
% Ritardando steps (cycle 79) follow v(x) = [1 + (v_end^2 - 1) x]^(1/2) (Friberg & Sundberg 1999, q = 2): little slowing at first, most at the end;
% a poco rit. into Poco meno mosso ends just above 112 so the new tempo is reached, not undershot.
mt = #(define-music-function (bpm) (integer?) #{ \set Score.tempoWholesPerMinute = #(ly:make-moment bpm 4) #})
global = {
  \accidentalStyle Score.modern
  \key c \minor \time 4/4
  \tempo "Lento" 4 = 50
  s1*14
  \break
  \mark \default
  \tempo "Allegro appassionato" 4 = 126
  % c100: breaks before 23, 31 and 39 hold 15-46 at 8 bars per system (critic 99 found it reflowing to 10/11/11 after edits elsewhere)
  s1*8 \break s1*8 \break s1*2
  \mark \default
  s1*6 \break s1*6 \tempo \markup \medium \italic "poco rit." \mt 124 s2 \mt 121 s2 \mt 118 s2 \mt 114 s2
  \break
  \bar "||" \key aes \major \mark \default
  \tempo "Poco meno mosso" 4 = 112
  s1*15 \tempo \markup \medium \italic "poco animando" \mt 115 s1 \mt 118 s1 \break s1*2 \tempo \markup \medium \italic "rit." \mt 116 s2 \mt 111 s2 \mt 105 s2 \mt 100 s2 \mt 94 s2 \mt 88 s2
  \mark \default
  \tempo "Tempo dell'Allegro" 4 = 126
  s1*4
  % c099: system break moved from 77 to 73, so the codetta 64-72 and the flute's motto 73-76 are not squeezed into one 13-bar system (73-76 were about 30 pt wide each)
  \break
  s1*4
  \bar "||" \key c \minor \mark \default
  s1*8 \break
  s1*9 \break s1*3
  \bar "||" \key b \minor \mark \default
  s1*6 \break
  \bar "||" \key a \minor
  s1*8 \break
  \bar "||" \key c \minor
  s1*6
  \mark \default
  s1*2 s1*2
  % c099: system break moved from 119 to 121 (10 + 10 bars instead of 8 + 12), so the fff climax 122 and the collapse 123-126 are not printed at a quarter of the width of the triplet bars
  \break \tempo \markup \medium \italic "allargando" \mt 120 s2 \mt 114 s2 \mt 106 s1 \tempo \markup \medium \italic "sostenuto" \mt 100 s1*4 \tempo "a tempo" \mt 126 s1*4
  \break \mark \default
  s1*8 \break s1*6 \tempo \markup \medium \italic "poco rit." \mt 124 s2 \mt 121 s2 \mt 118 s2 \mt 114 s2
  \break
  \bar "||" \key c \major \mark \default
  \tempo "Poco meno mosso" 4 = 112
  s1*9 \tempo \markup \medium \italic "poco animando" \mt 115 s1 \mt 118 s1
  \pageBreak \mark \default
  \mt 120 s1*2 \tempo \markup \medium \italic "largamente" \mt 100 s1*3
  % c105: system break moved from 167 to 163 (5 + 8 bars instead of 9 + 4), so 167-170 are not spread over a whole page (Gould p. 40-41)
  \break s1*2 \tempo \markup \medium \italic "rit." \mt 98 s2 \mt 92 s2 \mt 87 s2 \mt 81 s2
  \bar "||" \key c \minor \mark \default
  \tempo "Tempo dell'Allegro" 4 = 126
  s1*3 s2. \mt 40 s4
  \break
  \mark \default
  \tempo "Più lento" 4 = 72
  s1*6 \tempo \markup \medium \italic "rit." \mt 70 s2 \mt 65 s2 \mt 59 s2 \mt 53 s2
  \tempo "Tempo I (Lento)" 4 = 50
  s1*3 \mt 30 s1
  \bar "|."
}
