\version "2.24.0"
subP = #(make-dynamic-script (markup #:line (#:normal-text #:italic "sub." #:dynamic "p")))
% MIDI-only tempo step: realises rit./accel./fermatas in score.midi; prints nothing. Its unit is the quarter note (2. = 88 is \mt 264).
mt = #(define-music-function (bpm) (integer?) #{ \set Score.tempoWholesPerMinute = #(ly:make-moment bpm 4) #})
% c018: down-bow sign for accented strokes (Adler PDF 38: mark the bow only to counteract the players' habit). avoid-slur ignore:
% with the default, the stem-side Y-offset callback (score.ly, c125) failed on the high C under a short slur ("Nothing to minimise"), and 'inside made a cyclic slur dependency.
dnb = -\tweak avoid-slur #'ignore \downbow
global = {
  \accidentalStyle Score.modern
  \key e \minor \time 3/4
  \tempo "Allegro vivace" 2. = 88
  % 1-12: introduction. Hn 1 G sharp (movement II's A flat) -> horn call in E major -> E minor; timpani motive x
  % c020: fermata on bar 2: the pivot G sharp 4 (movement II's last A flat 4) is held before the tempo starts at 3 (was 1.4 s, now about 2.7 s in the MIDI)
  s2. \mt 88 s2.\fermata \mt 264
  s2.*10
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
  \tempo \markup { "a tempo" \medium \italic "(ritmo di tre battute)" } \mt 264
  % c019: 89-100 in three-bar groups (head entries at 89, 92, 95; timpani at 89, 92, 95, 98-100), as Beethoven 9/ii bars 177-233 "Ritmo di tre battute"
  s2.*12 \tempo \markup \medium \italic "ritmo di quattro battute" \mt 264 s2.*4
  \mark \default % G 105: theme A, tutti
  s2.*16
  \mark \default % H 121: second idea in E minor
  s2.*12
  s2.*8
  \bar "||" \mark \default % J 141: link to the trio, E minor -> E major
  s2.*8 \tempo \markup \medium \italic "poco rit." \mt 252 s2. \mt 240 s2. \mt 232 s2. \mt 228 s2.
  \bar "||" \break \key e \major \mark \default % K 153: Trio (c005: the trio starts a system, not the last bar of one)
  \tempo \markup { "Trio" \medium \italic "Un poco meno mosso" } 2. = 76
  s2.*32
  \mark \default % L 185: trio, middle part (c003: 24 bars)
  s2.*24
  \mark \default % M 209: trio tune returns
  s2.*28 \tempo \markup \medium \italic "poco rit." \mt 216 s2. \mt 204 s2. \mt 196 s2. \mt 188 s2.  % c028: 240 the slowest bar of the printed poco rit. (was \mt 228, a MIDI-only a tempo that the score does not print)
  % c023: retransition 12 bars (was 16); the E-minor key signature now falls on 241, where Hn 1's G sharp turns to G natural
  \bar "||" \key e \minor \mark \default % N 241: retransition
  \tempo \markup \medium \italic "poco a poco accelerando" \mt 204  % c028: the accelerando starts from the rit.'s tempo
  s2.*4 \mt 228 s2.*4 \mt 248 s2.*4
  \bar "||" \break \mark \default % O 253: scherzo returns (c025: the reprise starts a system, as the Trio does since c005)
  \tempo "Tempo I" 2. = 88
  s2.*36
  \bar "||" \mark \default % P 289 (c035: double bar as at D 57, the same juncture; Gould PDF 53): development, shortened
  s2.*16
  \mark \default % Q 305: theme A, tutti (c023: 20 bars, the close cut to 4)
  s2.*20
  \bar "||" \mark \default % R 325: coda (c030: bar numbers in these comments are v24-v30 numbers)
  \tempo "Più mosso" 2. = 96
  s2.*15 \mt 96 s2.\fermata  % c043: the G.P. with fermata lasts about two bars in the MIDI (it played as one plain bar, 0.6 s)
  \bar "||" \key e \major \mark \default % S 341: the trio tune recalled; G.P. at 340, rit. 370-376
  \tempo \markup { "Meno mosso" \medium \italic "(tempo del Trio)" } 2. = 76
  s2.*29 \once \override Score.MetronomeMark.outside-staff-padding = #1.2  % c035: the rit. touched "change bow freely" (Vln I, 369); Gould PDF 55: no characters collide
  \tempo \markup \medium \italic "rit." \mt 210 s2. \mt 196 s2. \mt 180 s2. \mt 160 s2. \mt 140 s2.*2 \mt 100 s2.-\tweak staff-padding #2 \fermata  % c035: the last fermata cleared the incoming ties of Vln I and Hn 1 (it touched them; Gould PDF 55)
  \bar "|."
}
