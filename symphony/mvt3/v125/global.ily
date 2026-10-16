\version "2.24.0"
% c018: down-bow then up-bow on one long note (Adler ch. 2, PDF 38, Beethoven Coriolanus) so the next attack is again a down-bow
dnup = ^\markup \concat { \musicglyph "scripts.downbow" \hspace #1.2 \musicglyph "scripts.upbow" }
% c035: "change bow at will" on two lines, so the text stays inside its bar (it ran across the next barline at 224, 226, 229, 235, 255: Gould PDF 55, no characters may collide)
cbaw = ^\markup \italic \override #'(baseline-skip . 2.3) \column { "change bow" "at will" }
cbawU = ^\markup \italic \override #'(baseline-skip . 2.3) \column { "unis., change" "bow at will" }
subP = #(make-dynamic-script (markup #:line (#:normal-text #:italic "sub." #:dynamic "p")))
% MIDI-only tempo step: realises rit./allargando/fermatas in score.midi; prints nothing. Its unit is the quarter note (2 = 84 is \mt 168).
% c075: tagged 'score, so a part built with \removeWithTag #'score \global does not split its multi-measure rests at these silent steps (MOLA PDF 5: rests as numbered ranges)
mt = #(define-music-function (bpm) (integer?) #{ \tag #'score { \set Score.tempoWholesPerMinute = #(ly:make-moment bpm 4) } #})
% c075 (MOLA PDF 7: in the parts, page turns fall in rests): the score's line and page breaks are tagged 'score so the parts (parts-test.ly, \removeWithTag #'score \global) lay out their own pages
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
  \bar "||" \tag #'score \break \key es \minor \mark \default % D 51: second theme, E flat minor, trumpet solo
  \tempo "Poco meno mosso" 2 = 72
  s1*16
  \bar "||" \tag #'score \pageBreak \key es \major \mark \default % E 67: second theme in E flat major, violins
  s1*14 \tempo \markup \medium \italic "animando" \mt 152 s1 \mt 160 s1
  \mark \default % F 83: closing group
  \tempo "Tempo I" 2 = 84
  s1*4 \tag #'score \pageBreak s1*12 % c055: page turn before the 6/3 bridge (87), not inside it
  \bar "||" \key f \minor \mark \default % G 99: development, F minor
  s1*16
  \bar "||" \tag #'score \pageBreak \key g \minor \mark \default % H 115: G area (bassoon, then harp)
  s1*8
  \bar "||" \key g \major
  s1*12
  \bar "||" \key c \minor \mark \default % J 135: retransition, G with B natural in the bass
  s1*14 \tempo \markup \medium \italic "allargando" \mt 156 s1 \mt 140 s1
  % c065 (Gould PDF 53: thin double barlines mark divisions between sections): the recapitulation (151) and its second theme (171) get the double bar that 51 and 67 have
  \bar "||" \mark \default % K 151: recapitulation
  \tempo "Tempo I" 2 = 84
  % c073 (form): no poco rit. at 169-170 and no Poco meno mosso at 171. The recapitulated second theme keeps Tempo I, so it does not replay the exposition's
  % pacing (51 and 67 are Poco meno mosso); Dvorak 9/iv (corpus: no tempo change at its second theme, 68; its Poco meno mosso at 214-226 is the soft reprise of the first
  % theme, Tempo I from 227) and Dvorak 7/iv (no meno mosso for its second theme) keep their finales' second themes at the main tempo.
  s1*20
  \bar "||" \tag #'score \pageBreak \mark \default % L 171: second theme in C minor, muted trumpet with cor anglais (at Tempo I since c073)
  s1*16
  % c055 (Adler part 2 PDF 299, item 4; PDF 291, item 3): a letter at the C-major second theme; L-M was 28 bars, the longest gap
  % c073 (form; A&S PDF 95: a tonic's meaning comes from its function): the major statement goes to A flat, the key the deceptive cadence of 186 opens, so C major,
  % its E natural (the violas' thread pitch) and the tonic as a goal are heard first at the arrival (223). The rit. steps are now relative to Tempo I.
  \bar "||" \tag #'score \break \key aes \major \mark \default % M 187: second theme in A flat major, violins (was C major until c073)
  s1*10 \tempo \markup \medium \italic "poco rit." \mt 160 s1 \mt 150 s1
  \bar "||" \tag #'score \pageBreak \key c \minor \mark \default % N 199: coda, the last C-minor tutti
  % c111 (hypermetre: 199-204 is movement I's hammered tutti (its 27-32), 205-210 the F1-head build over A flat in 2-bar units): the MIDI steps were at 203 and 207, the first inside the six-bar quotation;
  % the quotation now stays at Tempo I and the acceleration starts with the build at 205 (printed there), 172 at 205, 176 at 207 (2 = 88, as before)
  \tempo "Tempo I" 2 = 84
  s1*6 \tempo \markup \medium \italic "poco a poco più animato" \mt 172 s1*2 \mt 176 s1*4
  \bar "||" \tag #'score \pageBreak \key des \major \mark \default % O 211: D flat episode, trumpets (c013: theme B augmented, 211-218)
  \tempo "Largamente" 2 = 72
  s1*8
  \bar "||" \key c \major
  % c045 (MOLA PDF 5: avoid over-crowding within each measure; Example 7, PDF 10: no colliding markings): 219-222 are the narrowest bars of the score and the
  % mp < f hairpins at 220-222 were drawn about 1 mm long; give hairpins a minimum length here so the bars widen to hold them
  \override Staff.Hairpin.minimum-length = #13 \override Staff.Hairpin.springs-and-rods = #ly:spanner::set-spacing-rods
  s1*2 \tempo \markup \medium \italic "allargando" \mt 124 s1 \mt 112 s1
  \revert Staff.Hairpin.minimum-length \revert Staff.Hairpin.springs-and-rods
  \bar "||" \tag #'score \pageBreak \newSpacingSection \override Score.SpacingSpanner.shortest-duration-space = #1.3 \mark \default % P 223 (was 219; O until c055): C major arrival and chorale
  \tempo "Maestoso" 2 = 56
  s1*12
  \bar "||" \mark \default % Q 235 (was 231): movement I's second theme in C major, violins
  \tempo \markup { "Poco più mosso" \medium \italic "molto cantabile" } 2 = 66
  % c023: page break before 239 (start of the second phrase of the second-theme head); with the 8 bars added at 269-276 the free page breaker otherwise turns the page after 239, inside that phrase
  s1*4 \tag #'score \pageBreak s1*4 \tempo \markup \medium \italic "poco a poco stringendo" \mt 140 s1 \mt 150 s1 \mt 160 s1 \mt 168 s1 % c076: the MIDI stringendo reaches 2 = 88 at R (247), not already at 246
  \bar "||" \mark \default % R 247 (was 243): Più allegro (Allegro molto 2 = 100 until Dan's note 2026-10-13: too fast), both heads of movement I in C major
  \tempo "Più allegro" 2 = 88
  s1*8
  % c013: the chorale's last statement (255-264) stays in the Più allegro, written in doubled values (Brahms 1/iv 407ff), instead of Maestoso 2 = 60
  % c038 (expression; Dvorak 7/iv "Molto maestoso" and 9/iv "Meno mosso e maestoso" over the closing tremolo/held chords): 273-279 Largamente, 2 = 72 (the tempo of 211), for the closing chain G-F sharp-F-E, the scherzo quotation and the last chord
  % c039 (Rimsky-Korsakov Ex. 209, PDF 375; Ex. 272, PDF 438): the broadening into 273 is written out over 271-272 (was 2 = 100 straight to 72)
  % c045 (MOLA PDF 4: rehearsal letters at the landmarks of the music): 33 bars of Q had one letter; R at the chorale's last statement (255), S at Largamente (273); since c055 (letter M added at 187) these are S and T
  \mark \default s1*10 s1*6 \tempo \markup \medium \italic "allargando" \mt 164 s1 \mt 152 s1 \mark \default \tempo "Largamente" 2 = 72 s1*6 s1
  \bar "|."
}
% c095 (MOLA PDF 5: rests in the parts as one numbered range; Gould PDF 23: rests drawn so the next entry is easy to find): in a part, every new spacer in
% \global and every new R event started a new multi-measure rest, so the score-only \mt steps and page breaks, removed with their tags, still left
% splits (Tpt 1: 81 | 82, 83-86 | 87-90; percussion 247-262 drawn as sixteen single bars). For the parts only, adjacent plain skips and adjacent plain
% full-bar rests (no text, dynamic or fermata attached; bar checks between them dropped) are joined. Marks, tempo marks, key changes and double bars still divide rests.
#(define (c095-mergeable? x)
  (and (memq (ly:music-property x 'name) '(SkipEvent MultiMeasureRestMusic))
       (null? (ly:music-property x 'articulations))
       (null? (ly:music-property x 'tags))))
#(define (c095-join a b)
  (let ((r (+ (ly:moment-main (ly:music-length a)) (ly:moment-main (ly:music-length b)))))
    (make-music (ly:music-property a 'name) 'duration (ly:make-duration 0 0 r))))
mergeRests = #(define-music-function (m) (ly:music?)
  (music-map
    (lambda (x)
      (if (eq? (ly:music-property x 'name) 'SequentialMusic)
          (let loop ((es (ly:music-property x 'elements)) (acc '()) (bcs '()))
            (cond
              ((null? es) (ly:music-set-property! x 'elements (append (reverse acc) (reverse bcs))) x)
              ((and (eq? (ly:music-property (car es) 'name) 'BarCheck) (pair? acc) (c095-mergeable? (car acc)))
               (loop (cdr es) acc (cons (car es) bcs)))
              ((and (c095-mergeable? (car es)) (pair? acc) (c095-mergeable? (car acc))
                    (eq? (ly:music-property (car es) 'name) (ly:music-property (car acc) 'name)))
               (loop (cdr es) (cons (c095-join (car acc) (car es)) (cdr acc)) '()))
              (else (loop (cdr es) (cons (car es) (append bcs acc)) '()))))
          x))
    m))
