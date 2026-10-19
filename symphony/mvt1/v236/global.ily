\version "2.24.0"
subP = #(make-dynamic-script (markup #:line (#:normal-text #:italic "sub." #:dynamic "p")))
pedAflat = \markup \harp-pedal #"^-^|^--^"
pedNat = \markup \harp-pedal #"---|----"
pedBflatAflat = \markup \harp-pedal #"--^|---^"
% MIDI-only tempo step: realises rit./allargando/largamente/fermatas in score.midi; prints nothing.
% Ritardando steps (cycle 79) follow v(x) = [1 + (v_end^2 - 1) x]^(1/2) (Friberg & Sundberg 1999, q = 2): little slowing at first, most at the end;
% a poco rit. into Poco meno mosso ends just above 112 so the new tempo is reached, not undershot.
% c125: a solo on a shared staff that carries a hairpin stays in the part-combiner's "apart" voice (\voiceOne, stems up);
% these restore normal stem direction for the solo (Gould, Behind Bars PDF 38: stem direction follows the notes' position on the stave).
soloStemsOn = \context Voice = "one" \oneVoice
soloStemsOff = \context Voice = "one" \voiceOne
% c225: Gould, Behind Bars PDF 27-28: a note on the middle stave-line takes the stem direction of the surrounding stems when
% these go one way only, and keeps the direction of the notes in the same beat or half-bar (LilyPond always turns it down).
% Applied to unbeamed single notes whose direction is not set explicitly; the neighbours are the previous and next stemmed
% notes of the same voice in the same bar.
#(define (gould-head-positions stem)
   (let ((hs (ly:grob-object stem 'note-heads)))
     (if (ly:grob-array? hs)
         (map (lambda (h) (ly:grob-property h 'staff-position)) (ly:grob-array->list hs)) '())))
#(define (gould-natural-dir stem)
   (let ((d (ly:grob-property-data stem 'direction)) (beam (ly:grob-object stem 'beam)))
     (if (ly:dir? d) d
         (let* ((ps (if (ly:grob? beam) ; a beamed neighbour: the beam's direction, set by its notes farthest from the middle line
                        (let ((ss (ly:grob-object beam 'stems)))
                          (apply append (map gould-head-positions (if (ly:grob-array? ss) (ly:grob-array->list ss) (list stem)))))
                        (gould-head-positions stem))))
           (if (null? ps) 0
               (let ((hi (apply max ps)) (lo (apply min ps)))
                 (cond ((> (+ hi lo) 0) DOWN) ((< (+ hi lo) 0) UP) (else 0))))))))
#(define (gould-middle-line-engraver ctx)
   (let ((items '()))
     (make-engraver
      (acknowledgers
       ((stem-interface engraver grob source)
        (set! items (cons (cons grob (ly:context-property ctx 'internalBarNumber)) items))))
      ((finalize engraver)
       (let* ((v (list->vector (reverse items))) (n (vector-length v)))
         (define (stemmed? i)
           (let* ((g (car (vector-ref v i))) (hs (ly:grob-object g 'note-heads)))
             (and (ly:grob-array? hs) (> (ly:grob-array-length hs) 0)
                  (> (ly:grob-property g 'duration-log) 0))))
         (define (nbr i step)
           (let loop ((j (+ i step)))
             (cond ((or (< j 0) (>= j n)) #f)
                   ((not (= (cdr (vector-ref v j)) (cdr (vector-ref v i)))) #f)
                   ((stemmed? j) j)
                   (else (loop (+ j step))))))
         (do ((i 0 (1+ i))) ((>= i n))
           (let* ((g (car (vector-ref v i))) (hs (ly:grob-object g 'note-heads)))
             (if (and (stemmed? i)
                      (not (ly:dir? (ly:grob-property-data g 'direction)))
                      (not (ly:grob? (ly:grob-object g 'beam)))
                      (= (ly:grob-array-length hs) 1)
                      (= 0 (ly:grob-property (ly:grob-array-ref hs 0) 'staff-position)))
                 (let* ((ns (filter (lambda (x) x) (list (nbr i -1) (nbr i 1))))
                        (ds (map (lambda (j) (gould-natural-dir (car (vector-ref v j)))) ns)))
                   (if (and (pair? ds) (every (lambda (d) (= d UP)) ds))
                       (ly:grob-set-property! g 'direction UP)))))))))))
% c235: Gould, Behind Bars PDF 33-36 (beam angles). LilyPond's default beam slopes are kept except in three cases:
% (1) a group whose inner note is closer to the beam than both outer notes (concave shape) takes a horizontal beam (PDF 36 (c));
% (2) a group of up to four notes crosses at most one stave-space, a longer group at most two (PDF 33-34);
% (3) a group whose notes all lie beyond the first ledger line slopes at most half a space (PDF 35).
% The beam moves only away from the noteheads (stems lengthen, never shorten), and the far end keeps its sit/hang/straddle quant.
% Kneed beams and beams across a line break keep LilyPond's positions.
#(define (gould-beam-positions grob)
   (let* ((pos (beam::place-broken-parts-individually grob))
          (d (ly:grob-property grob 'direction))
          (ss (ly:grob-object grob 'stems))
          (stems (if (ly:grob-array? ss) (ly:grob-array->list ss) '()))
          (near (filter number?
                  (map (lambda (s)
                         (let ((hs (ly:grob-object s 'note-heads)))
                           (if (and (ly:grob-array? hs) (> (ly:grob-array-length hs) 0))
                               (let ((ps (map (lambda (h) (ly:grob-property h 'staff-position)) (ly:grob-array->list hs))))
                                 (if (= d UP) (apply max ps) (apply min ps)))
                               #f)))
                       stems)))
          (sdirs (map (lambda (s) (ly:grob-property s 'direction)) stems))
          (n (length near)))
     (if (or (< n 2) (not (= n (length stems))) (not (ly:dir? d))
             (not (every (lambda (x) (eqv? x d)) sdirs))
             (not (eq? (ly:spanner-bound grob LEFT) (ly:spanner-bound (ly:grob-original grob) LEFT)))
             (not (eq? (ly:spanner-bound grob RIGHT) (ly:spanner-bound (ly:grob-original grob) RIGHT))))
         pos
         (let* ((L (car pos)) (R (cdr pos))
                (first (car near)) (last (car (last-pair near)))
                (inner (if (> n 2) (list-head (cdr near) (- n 2)) '()))
                (closest (max (* d first) (* d last)))
                (concave (any (lambda (x) (> (* d x) closest)) inner))
                (ledger (or (every (lambda (x) (> x 6)) near) (every (lambda (x) (< x -6)) near)))
                (cap (cond (ledger 0.5) ((<= n 4) 1.0) (else 2.0)))
                (far (if (= d UP) (max L R) (min L R))))
           (cond
            (concave (cons far far))
            ((> (abs (- R L)) (+ cap 0.01))
             ;; keep the end farther from the noteheads; bring the other end toward the beam direction
             (if (= far L)
                 (cons L (- L (* d cap)))
                 (cons (- R (* d cap)) R)))
            (else pos))))))
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
  % c145: 73-76 were spaced tighter than 77-84 (an eighth ~21 pt in 74 vs ~35 pt in 77-78); own spacing section evens the note-value widths (Gould PDF 54)
  \newSpacingSection \override Score.SpacingSpanner.common-shortest-duration = #(ly:make-moment 1/16)
  s1*4
  \bar "||" \key c \minor \mark \default \newSpacingSection \revert Score.SpacingSpanner.common-shortest-duration
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
  \bar "||" % c130: thin double barline before attacca (Gould PDF 53)
}
