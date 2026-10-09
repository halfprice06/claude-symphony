\version "2.24.0"
subP = #(make-dynamic-script (markup #:line (#:normal-text #:italic "sub." #:dynamic "p")))
pedAflat = \markup \harp-pedal #"^-^|^--^"
pedNat = \markup \harp-pedal #"---|----"
% MIDI-only tempo step: realises rit./allargando/largamente/fermatas in score.midi; prints nothing.
mt = #(define-music-function (bpm) (integer?) #{ \set Score.tempoWholesPerMinute = #(ly:make-moment bpm 4) #})
global = {
  \accidentalStyle Score.modern
  \key c \minor \time 4/4
  \tempo "Lento" 4 = 50
  s1*14
  \break
  \mark \default
  \tempo "Allegro appassionato" 4 = 126
  s1*18
  \mark \default
  s1*12 \tempo \markup \medium \italic "poco rit." \mt 120 s2 \mt 116 s2 \mt 110 s2 \mt 104 s2
  \break
  \bar "||" \key aes \major \mark \default
  \tempo "Poco meno mosso" 4 = 112
  s1*15 \tempo \markup \medium \italic "poco animando" \mt 115 s1 \mt 118 s1*3 \tempo \markup \medium \italic "rit." \mt 110 s2 \mt 104 s2 \mt 98 s2 \mt 92 s2 \mt 86 s2 \mt 80 s2
  \mark \default
  \tempo "Tempo dell'Allegro" 4 = 126
  s1*4
  s1*4
  \break
  \bar "||" \key c \minor \mark \default
  s1*8 \break
  s1*12
  \bar "||" \key b \minor \mark \default
  s1*6
  \bar "||" \key a \minor
  s1*8
  \bar "||" \key c \minor
  s1*6
  \mark \default
  s1*4 \tempo \markup \medium \italic "allargando" \mt 120 s2 \mt 114 s2 \mt 106 s1 \tempo \markup \medium \italic "sostenuto" \mt 100 s1*4 \tempo "a tempo" \mt 126 s1*4
  \mark \default
  s1*14 \tempo \markup \medium \italic "poco rit." \mt 120 s2 \mt 116 s2 \mt 110 s2 \mt 104 s2
  \break
  \bar "||" \key c \major \mark \default
  \tempo "Poco meno mosso" 4 = 112
  s1*13 \tempo \markup \medium \italic "poco animando" \mt 115 s1 \mt 118 s1
  \pageBreak \mark \default
  \mt 120 s1*2 \tempo \markup \medium \italic "largamente" \mt 100 s1*5 \tempo \markup \medium \italic "rit." \mt 94 s2 \mt 88 s2 \mt 82 s2 \mt 76 s2
  \break
  \bar "||" \key c \minor \mark \default
  \tempo "Tempo dell'Allegro" 4 = 126
  s1*3 s2. \mt 40 s4
  \break
  \mark \default
  \tempo "Più lento" 4 = 72
  s1*6 \tempo \markup \medium \italic "rit." \mt 66 s2 \mt 62 s2 \mt 58 s2 \mt 54 s2
  \tempo "Tempo I (Lento)" 4 = 50
  s1*3 \mt 30 s1
  \bar "|."
}
