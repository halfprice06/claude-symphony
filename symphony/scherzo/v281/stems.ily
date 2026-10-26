\version "2.24.0"
% c095: stems of notes on the middle stave-line follow the surrounding stems (Gould, Behind Bars PDF 27-28: "Continue the stem
% direction of surrounding stems that are in one direction only"; keep one direction within a beat or half-bar; PDF 60-61: the same for
% chords whose outer notes are equidistant from the middle line, and the majority rule for chords of three or more notes).
% LilyPond gave every such stem a down-stem, so a figure that sits below the middle line flipped on its one middle-line note
% (Vla 18, 21, 23, 258, 261, 263 r4 c' c' among up-stems; Vln II B4-A4-D#4 at 95-99; Cl 1-2 G4-D5 at 45-46). Only unbeamed stems with no set
% direction change (part-combined voices keep theirs). A run of such notes lasting up to a bar takes the direction of the stems on either
% side of it; if they disagree, or the run lasts more than a bar (Vln II B4 at 37-39), the down-stem stays (PDF 28: no clear-cut case).
#(define (c095-head-positions stem)
  (let ((hs (ly:grob-object stem 'note-heads)))
    (if (ly:grob-array? hs)
        (map (lambda (h) (ly:grob-property h 'staff-position)) (ly:grob-array->list hs))
        '())))
#(define (c095-own-dir stem)
  (let ((d (ly:grob-property-data stem 'direction)))
    (if (number? d) d
        (let ((ps (c095-head-positions stem)))
          (if (null? ps) #f
              (let ((s (+ (apply max ps) (apply min ps)))
                    (maj (apply + (map (lambda (p) (cond ((> p 0) 1) ((< p 0) -1) (else 0))) ps))))
                (cond ((> s 0) DOWN) ((< s 0) UP)
                      ((and (> (length ps) 2) (> maj 0)) DOWN)
                      ((and (> (length ps) 2) (< maj 0)) UP)
                      (else #f))))))))
middleLineStemEngraver =
#(lambda (context)
  (let ((stems '()))
    (make-engraver
     (acknowledgers
      ((stem-interface engraver grob source)
       (if (>= (ly:grob-property grob 'duration-log 2) 1)
           (set! stems (cons (list grob (ly:context-current-moment context)
                                   (ly:context-property context 'currentBarNumber)) stems)))))
     ((finalize engraver)
      ;; runs of neutral stems (middle-line notes, balanced chords) lasting less than a bar take the direction of the stems
      ;; on either side of the run (within a bar's length); if those disagree, nothing changes
      (let* ((v (list->vector (filter (lambda (e) (pair? (c095-head-positions (car e)))) (reverse stems)))) (n (vector-length v)) (lim (ly:make-moment 3 4))
             ;; (stems of rests, which have no note heads, are left out above)
             (st (lambda (j) (car (vector-ref v j)))) (mo (lambda (j) (cadr (vector-ref v j))))
             (beamed? (lambda (j) (ly:grob? (ly:grob-object (st j) 'beam))))
             (neutral? (lambda (j) (and (not (c095-own-dir (st j))) (pair? (c095-head-positions (st j))))))
             (within? (lambda (a b) (not (ly:moment<? lim (ly:moment-sub b a))))))
        (let run ((i 0))
          (if (< i n)
              (if (and (neutral? i) (not (beamed? i)))
                  ;; collect the run i..k (neutral stems; neutral beamed stems are skipped)
                  (let collect ((k i) (members (list i)))
                    (let ((j (1+ k)))
                      (if (and (< j n) (neutral? j))
                          (collect j (if (beamed? j) members (cons j members)))
                          (let* ((last-i k)
                                 (prev (and (> i 0) (within? (mo (1- i)) (mo i)) (c095-own-dir (st (1- i)))))
                                 (next (and (< j n) (within? (mo last-i) (mo j)) (c095-own-dir (st j))))
                                 (dir (cond ((not (within? (mo i) (mo last-i))) #f)
                                            ((and prev next) (if (= prev next) prev #f))
                                            (else (or prev next)))))
                            (if (eqv? dir UP)
                                (for-each (lambda (m) (ly:grob-set-property! (st m) 'direction UP)) members))
                            (run j)))))
                  (run (1+ i))))))))))
