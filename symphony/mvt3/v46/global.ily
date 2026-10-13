\version "2.24.0"
% c018: down-bow then up-bow on one long note (Adler ch. 2, PDF 38, Beethoven Coriolanus) so the next attack is again a down-bow
dnup = ^\markup \concat { \musicglyph "scripts.downbow" \hspace #1.2 \musicglyph "scripts.upbow" }
% c035: "change bow at will" on two lines, so the text stays inside its bar (it ran across the next barline at 224, 226, 229, 235, 255: Gould PDF 55, no characters may collide)
cbaw = ^\markup \italic \override #'(baseline-skip . 2.3) \column { "change bow" "at will" }
cbawU = ^\markup \italic \override #'(baseline-skip . 2.3) \column { "unis., change" "bow at will" }
subP = #(make-dynamic-script (markup #:line (#:normal-text #:italic "sub." #:dynamic "p")))
% MIDI-only tempo step: realises rit./allargando/fermatas in score.midi; prints nothing. Its unit is the quarter note (2 = 84 is \mt 168).
mt = #(define-music-function (bpm) (integer?) #{ \set Score.tempoWholesPerMinute = #(ly:make-moment bpm 4) #})
global = {
  \accidentalStyle Score.modern
  \key c \minor \time 2/2
  \tempo "Allegro con fuoco" 2 = 84
  % 1-10: introduction. After the scherzo (movement III) and a pause: its last G sharp (Hn 1, Vln I) is taken as A flat, the root of the German sixth, ff, resolving to V of C
  s1*10
  \mark \default % A 11: first theme
  s1*16
  \mark \default % B 27: counterstatement, theme in the bass, modulating to V of E flat
  s1*16
  \mark \default % C 43: transition over the B flat pedal
  s1*6 \tempo \markup \medium \italic "poco rit." \mt 160 s1 \mt 150 s1
  \bar "||" \key es \minor \mark \default % D 51: second theme, E flat minor, trumpet solo
  \tempo "Poco meno mosso" 2 = 72
  s1*16
  \bar "||" \key es \major \mark \default % E 67: second theme in E flat major, violins
  s1*14 \tempo \markup \medium \italic "animando" \mt 152 s1 \mt 160 s1
  \mark \default % F 83: closing group
  \tempo "Tempo I" 2 = 84
  s1*16
  \bar "||" \key f \minor \mark \default % G 99: development, F minor
  s1*16
  \bar "||" \key g \minor \mark \default % H 115: G area (bassoon, then harp)
  s1*8
  \bar "||" \key g \major
  s1*12
  \bar "||" \key c \minor \mark \default % J 135: retransition, G with B natural in the bass
  s1*14 \tempo \markup \medium \italic "allargando" \mt 156 s1 \mt 140 s1
  \mark \default % K 151: recapitulation
  \tempo "Tempo I" 2 = 84
  s1*16 s1*2 \tempo \markup \medium \italic "poco rit." \mt 160 s1 \mt 150 s1
  \mark \default % L 171: second theme in C minor, muted trumpet with cor anglais
  \tempo "Poco meno mosso" 2 = 72
  s1*16
  \bar "||" \key c \major
  s1*10 \tempo \markup \medium \italic "poco rit." \mt 136 s1 \mt 128 s1
  \bar "||" \key c \minor \mark \default % M 199: coda, the last C-minor tutti
  \tempo \markup { "Tempo I" \medium \italic "poco a poco più animato" } 2 = 84
  s1*4 \mt 172 s1*4 \mt 176 s1*4
  \bar "||" \key des \major \mark \default % N 211: D flat episode, trumpets (c013: theme B augmented, 211-218)
  \tempo "Largamente" 2 = 72
  s1*8
  \bar "||" \key c \major
  % c045 (MOLA PDF 5: avoid over-crowding within each measure; Example 7, PDF 10: no colliding markings): 219-222 are the narrowest bars of the score and the
  % mp < f hairpins at 220-222 were drawn about 1 mm long; give hairpins a minimum length here so the bars widen to hold them
  \override Staff.Hairpin.minimum-length = #13 \override Staff.Hairpin.springs-and-rods = #ly:spanner::set-spacing-rods
  s1*2 \tempo \markup \medium \italic "allargando" \mt 124 s1 \mt 112 s1
  \revert Staff.Hairpin.minimum-length \revert Staff.Hairpin.springs-and-rods
  \bar "||" \pageBreak \newSpacingSection \override Score.SpacingSpanner.shortest-duration-space = #1.3 \mark \default % O 223 (was 219): C major arrival and chorale
  \tempo "Maestoso" 2 = 56
  s1*12
  \bar "||" \mark \default % P 235 (was 231): movement I's second theme in C major, violins
  \tempo \markup { "Poco più mosso" \medium \italic "molto cantabile" } 2 = 66
  % c023: page break before 239 (start of the second phrase of the second-theme head); with the 8 bars added at 269-276 the free page breaker otherwise turns the page after 239, inside that phrase
  s1*4 \pageBreak s1*4 \tempo \markup \medium \italic "poco a poco stringendo" \mt 140 s1 \mt 152 s1 \mt 164 s1 \mt 176 s1
  \bar "||" \mark \default % Q 247 (was 243): Allegro molto, both heads of movement I in C major
  \tempo "Allegro molto" 2 = 100
  s1*8
  % c013: the chorale's last statement (255-264) stays in the Allegro molto, written in doubled values (Brahms 1/iv 407ff), instead of Maestoso 2 = 60
  % c038 (expression; Dvorak 7/iv "Molto maestoso" and 9/iv "Meno mosso e maestoso" over the closing tremolo/held chords): 273-279 Largamente, 2 = 72 (the tempo of 211), for the closing chain G-F sharp-F-E, the scherzo quotation and the last chord
  % c039 (Rimsky-Korsakov Ex. 209, PDF 375; Ex. 272, PDF 438): the broadening into 273 is written out over 271-272 (was 2 = 100 straight to 72)
  % c045 (MOLA PDF 4: rehearsal letters at the landmarks of the music): 33 bars of Q had one letter; R at the chorale's last statement (255), S at Largamente (273)
  \mark \default s1*10 s1*6 \tempo \markup \medium \italic "allargando" \mt 184 s1 \mt 164 s1 \mark \default \tempo "Largamente" 2 = 72 s1*6 s1
  \bar "|."
}
