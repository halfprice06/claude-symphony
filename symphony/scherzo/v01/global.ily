\version "2.24.0"
subP = #(make-dynamic-script (markup #:line (#:normal-text #:italic "sub." #:dynamic "p")))
% MIDI-only tempo step: realises rit./accel./fermatas in score.midi; prints nothing. Its unit is the quarter note (2. = 88 is \mt 264).
mt = #(define-music-function (bpm) (integer?) #{ \set Score.tempoWholesPerMinute = #(ly:make-moment bpm 4) #})
global = {
  \accidentalStyle Score.modern
  \key e \minor \time 3/4
  \tempo "Allegro vivace" 2. = 88
  % 1-12: introduction. Hn 1 G sharp (movement II's A flat) -> horn call in E major -> E minor; timpani motive x
  s2.*12
  \mark \default % A 13: theme A, strings
  s2.*16
  \mark \default % B 29: counterstatement, winds and strings in call and response
  s2.*16
  \mark \default % C 45: second idea, G major, hemiola
  s2.*12
  \bar "||" \mark \default % D 57: development, fugato on the theme head
  s2.*16
  \bar "||" \key f \major \mark \default % E 73: F major (the Neapolitan of E), winds and harp without strings
  s2.*14 \tempo \markup \medium \italic "poco rit." \mt 252 s2. \mt 240 s2.
  \bar "||" \key e \minor \mark \default % F 89: retransition over the B pedal
  \tempo "a tempo" \mt 264
  s2.*16
  \mark \default % G 105: theme A, tutti
  s2.*16
  \mark \default % H 121: second idea in E minor
  s2.*12
  s2.*8
  \bar "||" \mark \default % J 141: link to the trio, E minor -> E major
  s2.*8 \tempo \markup \medium \italic "poco rit." \mt 252 s2. \mt 240 s2. \mt 232 s2. \mt 228 s2.
  \bar "||" \key e \major \mark \default % K 153: Trio
  \tempo \markup { "Trio" \medium \italic "Un poco meno mosso" } 2. = 76
  s2.*32
  \mark \default % L 185: trio, middle part
  s2.*32
  \mark \default % M 217: trio tune returns
  s2.*28 \tempo \markup \medium \italic "poco rit." \mt 216 s2. \mt 204 s2. \mt 196 s2. \mt 228 s2.
  \bar "||" \mark \default % N 249: retransition
  \tempo \markup \medium \italic "poco a poco accelerando" \mt 228
  s2.*4 \mt 236 s2.*4 \bar "||" \key e \minor \mt 244 s2.*4 \mt 256 s2.*4
  \bar "||" \mark \default % O 265: scherzo returns
  \tempo "Tempo I" 2. = 88
  s2.*36
  \mark \default % P 301: development, shortened
  s2.*16
  \mark \default % Q 317: theme A, tutti
  s2.*24
  \bar "||" \mark \default % R 341: coda
  \tempo "Più mosso" 2. = 96
  s2.*15 s2.\fermata
  \bar "||" \key e \major \mark \default % S 357: the trio tune recalled
  \tempo \markup { "Meno mosso" \medium \italic "(tempo del Trio)" } 2. = 76
  s2.*29 \tempo \markup \medium \italic "rit." \mt 210 s2. \mt 196 s2. \mt 180 s2. \mt 160 s2. \mt 140 s2.*2 s2.\fermata
  \bar "|."
}
