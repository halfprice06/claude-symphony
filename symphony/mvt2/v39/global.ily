\version "2.24.0"
subP = #(make-dynamic-script (markup #:line (#:normal-text #:italic "sub." #:dynamic "p")))
% MIDI-only tempo step: realises rit./allargando/fermatas in score.midi; prints nothing.
mt = #(define-music-function (bpm) (integer?) #{ \set Score.tempoWholesPerMinute = #(ly:make-moment bpm 4) #})
global = {
  \accidentalStyle Score.modern
  \numericTimeSignature
  \key aes \major \time 3/4
  \tempo "Adagio" 4 = 52
  % 1-6: common-tone link from movement I (C held on top, E natural falls to E flat)
  s2.*6 \break
  \mark \default % A 7: horn theme, no strings
  s2.*8 \break
  \mark \default % B 15: oboe and violins in dialogue
  s2.*8 \break
  \mark \default % C 23: theme in the violins, cello counter-melody
  s2.*8 \break
  % 31-36: bass clarinet over an A flat pedal, to D flat
  s2.*4 \tempo \markup \medium \italic "poco rit." \mt 49 s2. \mt 45 s2. \break
  \bar "||" \key des \major \time 4/4 \mark \default % D 37
  \tempo "Poco più mosso" 4 = 60
  s1*4 \break s1*4 \break
  \mark \default % E 45
  s1*2
  \bar "||" \key fis \minor
  s1*2 \break s1*2
  \bar "||" \key des \major
  s1*2 \break
  \mark \default % F 53
  \tempo \markup \medium \italic "poco a poco animando" s1*2 \mt 61 s1*2 \break \mt 62 s1*2
  % c035: 59-60 have viola sextuplets; a tighter spacing section keeps a quarter as wide here as in 57-58 (Gould, Behind Bars p. 40, PDF 54: equal durations take equal space across a system)
  \newSpacingSection \override Score.SpacingSpanner.shortest-duration-space = #1.0
  \mt 64 s1 \tempo \markup \medium \italic "poco allarg." \mt 62 s2 \mt 58 s2 \break
  \newSpacingSection \revert Score.SpacingSpanner.shortest-duration-space
  \mark \default % G 61
  \tempo "Largamente" 4 = 54
  s1*2
  \bar "||" \key a \minor
  \tempo \markup \medium \italic "allargando" \mt 50 s1 \mt 46 s2 \mt 40 s2 \break
  \bar "||" \key aes \major \time 3/4 \mark \default % H 65
  \tempo "Tempo I" 4 = 52
  s2.*6 \break
  \mark \default % J 71
  s2.*4 \break s2.*3 \tempo \markup \medium \italic "poco allargando" \mt 50 s2. \break \mt 48 s2.*2 \mt 46 s2. \mt 44 s2. \break
  \mark \default % K 83: coda (v03's closing 83-90 cut)
  \tempo "a tempo" \mt 52
  s2.*4 \break s2.*2 \tempo \markup \medium \italic "rit." \mt 48 s2. \mt 44 s2. \mt 40 s2. \mt 36 s4 s4 \mt 20 s4
  \bar "|."
}
