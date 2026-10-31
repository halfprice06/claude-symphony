\version "2.24.0"
subP = #(make-dynamic-script (markup #:line (#:normal-text #:italic "sub." #:dynamic "p")))
pedAflat = \markup \harp-pedal #"^-^|^-^^"  % c246: G-flat from the start (first G is G-flat at 51; G-natural only from 54, changed at 53), one pedal change fewer (Adler adler1 PDF 112-113)
pedNat = \markup \harp-pedal #"---|----"
pedBflatAflat = \markup \harp-pedal #"--^|---^"
% MIDI-only tempo step: realises rit./allargando/largamente/fermatas in score.midi; prints nothing.
% Ritardando steps (cycle 79) follow v(x) = [1 + (v_end^2 - 1) x]^(1/2) (Friberg & Sundberg 1999, q = 2): little slowing at first, most at the end;
% a poco rit. into Poco meno mosso ends just above 112 so the new tempo is reached, not undershot.
% c125: a solo on a shared staff that carries a hairpin stays in the part-combiner's "apart" voice (\voiceOne, stems up);
% these restore normal stem direction for the solo (Gould, Behind Bars PDF 38: stem direction follows the notes' position on the stave).
soloStemsOn = \context Voice = "one" \oneVoice
soloStemsOff = \context Voice = "one" \voiceOne
% c315: when the neighbours disagree, the note follows the neighbour in its own half-bar (Gould PDF 28).
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
        (set! items (cons (list grob (ly:context-property ctx 'internalBarNumber) (ly:context-property ctx 'measurePosition)) items))))
      ((finalize engraver)
       (let* ((v (list->vector (reverse items))) (n (vector-length v)))
         (define (stemmed? i)
           (let* ((g (car (vector-ref v i))) (hs (ly:grob-object g 'note-heads)))
             (and (ly:grob-array? hs) (> (ly:grob-array-length hs) 0)
                  (> (ly:grob-property g 'duration-log) 0))))
         (define (nbr i step)
           (let loop ((j (+ i step)))
             (cond ((or (< j 0) (>= j n)) #f)
                   ((not (= (cadr (vector-ref v j)) (cadr (vector-ref v i)))) #f)
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
                   (cond
                    ((and (pair? ds) (every (lambda (d) (= d UP)) ds))
                     (ly:grob-set-property! g 'direction UP))
                    ((and (= (length ns) 2) (not (= (car ds) (cadr ds))))
                     (let* ((half (lambda (j) (floor (* 2 (ly:moment-main (caddr (vector-ref v j)))))))
                            (h (half i))
                            (same (filter (lambda (k) (= (half (list-ref ns k)) h)) '(0 1))))
                       (if (and (= (length same) 1) (= (list-ref ds (car same)) UP))
                           (ly:grob-set-property! g 'direction UP))))))))))))))
% c235: Gould, Behind Bars PDF 33-36 (beam angles). LilyPond's default beam slopes are kept except in three cases:
% (1) a group whose inner note is closer to the beam than both outer notes (concave shape) takes a horizontal beam (PDF 36 (c));
% (2) a group of up to four notes crosses at most one stave-space, a longer group at most two (PDF 33-34);
% (3) a group whose notes all lie beyond the first ledger line slopes at most half a space (PDF 35).
% The beam moves only away from the noteheads (stems lengthen, never shorten), and the far end keeps its sit/hang/straddle quant.
% Kneed beams and beams across a line break keep LilyPond's positions.
% c325 (second pass over PDF 31-41): (4) a group of only two pitches whose single different note stands at the start or end and lies
% farther from the beam than the others takes a horizontal beam (PDF 37); (5) notes closer together than three stave-spaces take a slope
% of at most half a space (PDF 34). Inside the stave both ends stay on a line (sit/straddle/hang, slope 0.18 or 0.35 space; PDF 31-32,
% 34); two-beam groups keep the outer beam hanging (up-stems) or sitting (down-stems) (PDF 32); ends only move away from the noteheads.
% Groups of three or more beams keep LilyPond's positions (PDF 35: whole-space slant).
% c415 (third pass over PDF 31-41): (6) ledger-line groups whose stems reach the middle line slope 1/4 (second) or 0.35 (wider) (PDF 35).
#(define (gould-close-pair L R d nb)
   ;; new end positions for a closely spaced group: slope 0.15-0.5 space in the original direction, each end on a line
   ;; inside the stave (or clear of it), neither end nearer the noteheads than before; least movement, then the larger slope
   (let* ((q 0.17591836734693886)
          (offs (cond ((> nb 1) (if (= d UP) (list 0 (- q)) (list 0 q))) (else (list (- q) 0 q))))
          (quants (apply append (map (lambda (l) (map (lambda (o) (+ l o)) offs)) '(-2 -1 0 1 2))))
          (free (filter (lambda (e) (>= (abs e) 2.5)) (map (lambda (k) (* k 0.25)) (iota 81 -40))))
          (cands (append quants free))
          (sg (if (> R L) 1 -1))
          (best #f) (bm 0) (bs 0))
     (for-each
      (lambda (a)
        (if (>= (* d a) (- (* d L) 0.001))
            (for-each
             (lambda (b)
               (let ((sl (* sg (- b a))) (mv (+ (* d (- a L)) (* d (- b R)))))
                 (if (and (>= (* d b) (- (* d R) 0.001)) (>= sl 0.15) (<= sl 0.501)
                          (or (not best) (< mv (- bm 0.001)) (and (< (abs (- mv bm)) 0.001) (> sl bs))))
                     (begin (set! best (cons a b)) (set! bm mv) (set! bs sl)))))
             cands)))
      cands)
     best))
% c415 (7): Gould PDF 35, "This stem may be shortened to 3 stave-spaces (a seventh) when inside the stave and to 2 1/2
% stave-spaces (a sixth) when outside the stave"; PDF 32-33: with a second beam the stem grows (here by 1/4 space). Stem length is
% measured from the notehead nearest the beam to the far edge of the outer beam. When a stem of a one- or two-beam group falls more
% than 0.1 space short, the beam moves away from the noteheads to the nearest pair of positions that keeps both ends on a line inside
% the stave (PDF 31-32, 34), the slope direction, and a slope no steeper than before; least movement wins.
#(define (gould-min-stem pos near xs d nb)
   (let* ((n (length near)) (x0 (car xs)) (x1 (car (last-pair xs))) (w (- x1 x0))
          (stem-ok (lambda (a b)
                     (every (lambda (p x)
                              (let* ((y (+ a (* (- b a) (if (> w 0.01) (/ (- x x0) w) 0))))
                                     (len (+ (* d (- y (/ p 2))) 0.24))
                                     (need (+ (if (< (abs y) 2.0) 3.0 2.5) (if (= nb 2) 0.25 0))))
                                (>= len (- need 0.1))))
                            near xs))))
     (if (or (> nb 2) (< nb 1) (< n 2) (stem-ok (car pos) (cdr pos)))
         pos
         (let* ((L (car pos)) (R (cdr pos)) (q 0.17591836734693886)
                (offs (cond ((> nb 1) (if (= d UP) (list 0 (- q)) (list 0 q))) (else (list (- q) 0 q))))
                (quants (filter (lambda (e) (< (abs e) 2.3))
                                (apply append (map (lambda (l) (map (lambda (o) (+ l o)) offs)) '(-2 -1 0 1 2)))))
                (free (filter (lambda (e) (>= (abs e) 2.3)) (map (lambda (k) (* k 0.25)) (iota 61 -15 0.5))))
                (cands (append quants free (map (lambda (k) (* k 0.25)) (iota 21 -50)) (map (lambda (k) (* k 0.25)) (iota 21 30))))
                (osl (- R L)) (best #f) (bm 0))
           (for-each
            (lambda (a)
              (if (>= (* d a) (- (* d L) 0.001))
                  (for-each
                   (lambda (b)
                     (let ((sl (- b a)) (mv (+ (* d (- a L)) (* d (- b R)))))
                       (if (and (>= (* d b) (- (* d R) 0.001))
                                (or (and (< (abs osl) 0.01) (< (abs sl) 0.01))
                                    (and (>= (abs osl) 0.01) (> (* sl osl) 0) (<= (abs sl) (+ (abs osl) 0.01))))
                                (stem-ok a b)
                                (or (not best) (< mv (- bm 0.001))))
                           (begin (set! best (cons a b)) (set! bm mv)))))
                   cands)))
            cands)
           (or best pos)))))
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
                (far (if (= d UP) (max L R) (min L R)))
                (vals (delete-duplicates near))
                (twopitch-far
                 (and (> n 2) (= (length vals) 2)
                      (let* ((odd (if (= (length (filter (lambda (x) (= x (car vals))) near)) 1) (car vals)
                                      (if (= (length (filter (lambda (x) (= x (cadr vals))) near)) 1) (cadr vals) #f)))
                             (other (and odd (if (= odd (car vals)) (cadr vals) (car vals)))))
                        (and odd (or (= odd first) (= odd last))
                             (< (* d odd) (* d other))))))
                (nb (- (apply max (map (lambda (s) (ly:grob-property s 'duration-log)) stems)) 2))
                (sys (ly:grob-system grob))
                (xs (map (lambda (s) (ly:grob-relative-coordinate s sys X)) stems))
                (close (< (apply min (map (lambda (a b) (abs (- b a))) (list-head xs (- n 1)) (cdr xs))) 3.0))) ; any two adjacent stems closer than 3 spaces
           (gould-min-stem
           (cond
            (concave (cons far far))
            (twopitch-far (cons far far))
            ;; c415 (6): Gould PDF 35, notes beyond the first ledger line: a group whose stems LilyPond extends to the middle
            ;; line comes out horizontal (or at a quarter slope for wider intervals); it slopes in the direction of the outer
            ;; interval, a quarter space for a second, half a space (0.35, the nearest slope with both ends on the middle line,
            ;; PDF 34) for wider intervals. With two beams the outer beam must sit (down-stems) or hang (up-stems) or straddle
            ;; (PDF 32), so the slope is a quarter space: the end at the note farther from the beam moves toward it.
            ((and ledger (<= nb 2) (not (= first last)) (< (abs L) 0.2) (< (abs R) 0.2)
                  (< (abs (- R L)) (if (or (= nb 2) (= (abs (- last first)) 1)) 0.17 0.34)))
             (let* ((q 0.17591836734693886)
                    (lnear (> (* d first) (* d last)))   ; the left note is the one nearer the beam
                    (away (* d q)))
               (cond ((= nb 2) (if lnear (cons 0 (- away)) (cons (- away) 0)))
                     ((= (abs (- last first)) 1) (if lnear (cons away 0) (cons 0 away)))
                     (else (if lnear (cons away (- away)) (cons (- away) away))))))
            ((and close (> (abs (- R L)) 0.51) (< nb 3) (gould-close-pair L R d nb))
             (gould-close-pair L R d nb))
            ((> (abs (- R L)) (+ cap 0.01))
             ;; keep the end farther from the noteheads; bring the other end toward the beam direction
             (if (= far L)
                 (cons L (- L (* d cap)))
                 (cons (- R (* d cap)) R)))
            (else pos))
           near xs d nb)))))
mt = #(define-music-function (bpm) (integer?) #{ \set Score.tempoWholesPerMinute = #(ly:make-moment bpm 4) #})
global = {
  \accidentalStyle Score.modern
  \key c \minor \time 4/4
  \tempo "Lento" 4 = 50
  s1*14
  \bar "||" % c345: thin double barline between the Lento introduction and the Allegro (Gould PDF 53: double barlines mark divisions between sections)
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
  s1*15 \tempo \markup \medium \italic "poco animando" \mt 115 s1 \mt 118 s1 \break s1*2 \tempo \markup \medium \italic "rit." \mt 116 s2 \mt 111 s2 \mt 104 s2 \mt 98 s2 \mt 90 s2
  % c368: the new tempo starts with the run at 68.3, the upbeat group of the codetta (Aldwell & Schachter PDF 49, 52: a group that begins on a weak beat belongs to the following downbeat); the rit. ends on the deceptive cadence at 68.1 (was: rit. through the run at 88, then 126 at 69)
  \tempo "Tempo dell'Allegro" 4 = 126 s2
  % c345: the sixteenth run into 69 (Fl 1-2, Vln I) left its last stem half a space from the barline; Gould PDF 57: stems never nearer a barline than one space
  \once \override Score.BarLine.extra-spacing-width = #'(-0.6 . 0)
  \mark \default
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

% c245: rests outside the stave on whole stave-spaces (Gould, Behind Bars PDF 49: "From the centre of the stave, rests move an
% exact number of stave-spaces up or down, so that they remain correctly positioned in relation to the stave-lines"; PDF 51:
% minim and semibreve rests outside the stave sit on a ledger line). LilyPond's rest collision leaves some rests in two-part
% staves half a space off (e.g. Hn 4 minim rest at 28, Fl 1 at 117-120); this moves such a rest a further half space away from
% the centre, so it cannot come nearer the other part. Rests already on whole spaces are untouched.
#(define (gould-rest-snap grob)
  (let ((ss (ly:grob-object grob 'staff-symbol)))
    (if (ly:grob? ss)
        (let* ((common (ly:grob-common-refpoint grob ss Y))
               (y (- (ly:grob-relative-coordinate grob common Y)
                     (ly:grob-relative-coordinate ss common Y)))
               (frac (- y (round y))))
          (if (> (abs frac) 0.01)
              (let ((target (if (>= y 0) (ceiling y) (floor y))))
                (ly:grob-translate-axis! grob (- target y) Y)))))))
