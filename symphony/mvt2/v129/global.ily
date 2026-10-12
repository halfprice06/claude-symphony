\version "2.24.0"
subP = #(make-dynamic-script (markup #:line (#:normal-text #:italic "sub." #:dynamic "p")))
% MIDI-only tempo step: realises rit./allargando/fermatas in score.midi; prints nothing.
mt = #(define-music-function (bpm) (integer?) #{ \set Score.tempoWholesPerMinute = #(ly:make-moment bpm 4) #})
% c045: rehearsal letter (and tempo) repeated above the highest string staff when Violins I rest (MOLA PDF 4: tempo marks above the
% top staff and above the first violins, or the similarly positioned staff; rehearsal letters as landmarks). 
strMark = #(define-event-function (letter tempo) (string? markup?)
  #{ -\tag #'score -\tweak outside-staff-priority #1000 -\tweak X-offset #-1 ^\markup \column { \override #'(box-padding . 0.5) \box \bold \fontsize #3 #letter \bold #tempo } #})
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
  % c048: the 3-bar group 45-47 ends on the C sharp 7 goal; the quotation is held back as movement I holds back its S theme
  % (mvt I: poco rit. into Poco meno mosso) and as Dvorak 9/ii 53-54 does (poco ritard. - Poco meno mosso); A&S PDF 47 note, 53-54
  s2 \tempo \markup \medium \italic "poco rit." \mt 57 s4 \mt 55 s4
  \tempo \markup \medium \italic "poco sostenuto" \mt 54 s1 \break s1*2
  \bar "||" \key des \major
  s1*2 \break
  \mark \default % F 53
  \tempo \markup \medium \italic "a tempo, poco a poco animando" \mt 60 s1*2 \mt 61 s1*2 \break \mt 62 s1*2
  % c035: 59-60 have viola sextuplets; a tighter spacing section keeps a quarter as wide here as in 57-58 (Gould, Behind Bars p. 40, PDF 54: equal durations take equal space across a system)
  \newSpacingSection \override Score.SpacingSpanner.shortest-duration-space = #1.0
  \mt 64 s1 \once \override Staff.MetronomeMark.extra-offset = #'(1.8 . -0.7) \tempo \markup \medium \italic "poco allargando" \mt 62 s2 \mt 58 s2 \break
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
