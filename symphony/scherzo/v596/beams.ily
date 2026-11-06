\version "2.24.0"
% c195: the c015/c105 beam callback moved here from score.ly so that score.ly and the parts (parts-gen.py) share it.
% Gould, Behind Bars PDF 31-37 applies to what the players read: before c195 the parts kept LilyPond's default beams
% (theme A's A5-F#5 pair at 24/116/264/316 sloped 0.62 over notes 2 spaces apart; the trio call's concave turn sloped at 185/197 in Ob 1;
% Fl 1 253-267 flat on the middle line with 4-7-space stems).

% c015: beams of groups lying wholly beyond the first ledger line (Gould, Behind Bars PDF 33 and 35). By default every stem
% reached the middle line, so Fl 1 at 169-184 and 257-272 had stems of 5½-7 spaces and flat beams on the middle line.
% Gould: such a beam sits inside the stave with one clear stave-line between it and the first ledger line, stems close to
% 3-3½ spaces, slope ¼ space for a second and ½ for wider intervals, horizontal for repeated or concave groups (PDF 36-37).
% Other groups keep LilyPond's default placement.
% c105: second pass on Gould PDF 31-41. (1) The c015 ledger callback put one end of a ¼-slope beam at 1.49 spaces, in the middle of a
% space (Fl 1 254, 258, 262, 263, 266; Vln I 355), and sloped the repeated figure A6-G6-A6-G6 at 261. Gould PDF 31 and 34: both ends of
% a slanted beam touch a stave-line; PDF 36 (b): a repeated pattern takes a horizontal beam. Now each end is chosen from attached
% positions (straddle, sit, hang). (2) For all other groups LilyPond's placement is kept except: a concave group (an inner note nearer
% the beam than both outer notes) is made horizontal (PDF 36 (c); the trio call F#-E-D#-E at 186 and 198); and a group whose notes are
% closer than three spaces apart takes at most a ½-space slope (PDF 34; Fl 1 256 had 0.82 and a 2.74-space stem; theme A at 25, 117,
% 265, 317 had 0.65), the shortest stem kept at 3 spaces (PDF 35).
#(define (c105-near-ys stems d)
  (map (lambda (s)
         (let* ((hs (ly:grob-object s 'note-heads))
                (ps (if (ly:grob-array? hs) (map (lambda (h) (ly:grob-property h 'staff-position)) (ly:grob-array->list hs)) '())))
           (if (null? ps) #f (/ (if (> d 0) (apply max ps) (apply min ps)) 2.0))))
       stems))
#(define (c105-repeated? ys)
  (let ((n (length ys)))
    (and (>= n 4) (even? n) (> (length (delete-duplicates ys)) 1)
         (let loop ((l ys)) (or (< (length l) 3) (and (= (car l) (caddr l)) (loop (cdr l))))))))
#(define (c105-beam-positions grob)
  (let* ((stems (ly:grob-array->list (ly:grob-object grob 'stems)))
         (dirs (map (lambda (s) (ly:grob-property s 'direction)) stems))
         (n (length stems))
         (d (and (pair? dirs) (car dirs)))
         (raw (and d (c105-near-ys stems d))))
    (if (or (< n 2) (not raw) (memq #f raw) (not (apply = dirs)))
        (beam::place-broken-parts-individually grob)
        (let* (;; mirrored so that the beam lies below the notes (stems down) whatever the direction
               (near (map (lambda (y) (* -1 d y)) raw))
               (first (car near)) (last (car (last-pair near)))
               (inner (if (> n 2) (cdr (reverse (cdr (reverse near)))) '()))
               (concave (any (lambda (y) (< y (min first last))) inner))
               (flat (or concave (= first last) (c105-repeated? near)))
               (sys (ly:grob-system grob))
               (xs (map (lambda (s) (ly:grob-relative-coordinate s sys X)) stems))
               (x0 (car xs)) (x1 (car (last-pair xs)))
               (frac (lambda (x) (if (= x1 x0) 0 (/ (- x x0) (- x1 x0)))))
               (stems-ok? (lambda (a b minlen)  ; a, b mirrored beam centres at the first and last stem
                            (every (lambda (x y) (>= (+ (- y (+ a (* (- b a) (frac x)))) 0.24) minlen)) xs near))))
          (if (every (lambda (y) (>= y 3.5)) near)
              ;; c015 case: every note at or beyond the first ledger line on the beam's far side
              (let* ((iv (abs (- last first)))
                     (up (> last first))
                     (pairs (cond (flat (map (lambda (y) (cons y y)) '(1.24 0.76 0.24 -0.24 -0.76)))
                                  ((<= iv 0.5) '((1.0 . 1.24) (0.76 . 1.0) (0.0 . 0.24) (-0.24 . 0.0) (-1.0 . -0.76)))
                                  (else '((0.76 . 1.24) (0.24 . 0.76) (-0.24 . 0.24) (-0.76 . -0.24)))))
                     (ok (find (lambda (p) (let ((a (if up (car p) (cdr p))) (b (if up (cdr p) (car p)))) (stems-ok? a b 3.24))) pairs)))
                (if ok
                    (let ((a (if up (car ok) (cdr ok))) (b (if up (cdr ok) (car ok))))
                      (cons (* -1 d a) (* -1 d b)))
                    (beam::place-broken-parts-individually grob)))
              (let* ((def (beam::place-broken-parts-individually grob))
                     (a0 (* -1 d (car def))) (b0 (* -1 d (cdr def)))
                     (spacing (/ (abs (- x1 x0)) (- n 1))))
                (cond
                 ((and flat (> (abs (- b0 a0)) 0.01))
                  (let ((y (min a0 b0))) (cons (* -1 d y) (* -1 d y))))
                 ((and (not flat) (< spacing 3.0) (> (abs (- b0 a0)) 0.55))
                  (let* ((q (append-map (lambda (k) (list (- k 0.24) k (+ k 0.24))) (iota 11 -5)))
                         (sgn (if (> b0 a0) 1 -1))
                         (cands (append-map (lambda (a) (filter-map (lambda (b)
                                   (let ((s (* sgn (- b a))))
                                     (and (>= s 0.2) (<= s 0.53) (stems-ok? a b 2.98) (cons a b)))) q)) q))
                         (best (and (pair? cands)
                                    (car (sort cands (lambda (p r) (< (+ (abs (- (car p) a0)) (abs (- (cdr p) b0)))
                                                                       (+ (abs (- (car r) a0)) (abs (- (cdr r) b0))))))))))
                    (if best (cons (* -1 d (car best)) (* -1 d (cdr best))) def)))
                 (else def))))))))

% c375: beamed stems in double-stemmed (part-combined) staves (Gould, Behind Bars PDF 32-33 and 35; PDF 28-29 as read by c365).
% PDF 32: "The stem length (including the width of the outer beam) should be as close to 3½ spaces (normal stem length) as possible",
% 3¼ for a note on a line (PDF 33); PDF 35: the shorter stem of an angled beam may come down to 3 spaces inside the stave, 2½ outside it.
% c365 lengthened every unbeamed stem that points away from the stave centre to 3½ while its open-end note is inside the stave, then a
% quarter space less per staff position outside it (3¼, 3, 2¾, 2½), and left beamed stems to this file. LilyPond still shortened the
% beamed ones to 2.56-2.74 spaces, so in the shared staves a quaver pair stood ¾-1 space shorter than the crotchets on either side
% (Hn 1·2 71/299, Bn 1·2 105/305, Hn 3·4 246, Fl/Ob 333-334). Here a group whose stems all point away from the centre takes at least the
% c365 length at its shortest stem (3½ / 3¼ inside the stave, 3 for an angled beam; the c365 ladder outside), moved outward only; an end
% that then lies inside the stave is moved further out to the next stave-line attachment (PDF 31, 34). Other groups are unchanged.
% c465: the same minimum for a horizontal group of three or more notes in a single voice whose stems do not all point away from the centre
% (PDF 32-33: 3½ for a note in a space, 3¼ on a line, whatever the beam's position). Vln II's arpeggios at 173-175, 177, 179-180 (c407)
% are arches whose end notes lie nearest the beam; LilyPond shortened those end stems to 2.74 spaces (the inner stems are 4-5) and left the
% beam on the bottom stave-line at 177/179 but below the stave in the bars around them. Only these six beams move (probe); pairs are unchanged.
% c555: and for a sloped group of three or more notes in a single voice (PDF 35: "This stem may be shortened to 3 stave-spaces ... when
% inside the stave"). c511 rewrote Vln II 182 (F sharp 4 - C sharp 5 - E5 - C sharp 5 - A sharp 4); LilyPond gave the F sharp 4 a 2.74-space stem
% under a rising beam, the only angled beam in the score below 2.92. Pairs and shared-staff minority directions stay as c375 left them.
#(define (c375-target p sloped)
  (let ((t (if (<= p 4) (if (even? p) 3.25 3.5) (max 2.5 (- 3.5 (* 0.25 (- p 4)))))))
    (if sloped (min t 3.0) t)))
#(define (c375-attached? y)
  (any (lambda (line) (any (lambda (c) (< (abs (- y c)) 0.02)) (list line (+ line 0.24) (- line 0.24)))) '(-2 -1 0 1 2)))
#(define (gould-ledger-beam-positions grob)
  (let* ((res (c105-beam-positions grob))
         (stems (ly:grob-array->list (ly:grob-object grob 'stems)))
         (dirs (map (lambda (s) (ly:grob-property s 'direction)) stems))
         (d (and (pair? dirs) (car dirs)))
         (raw (and d (c105-near-ys stems d))))
    (if (or (not (pair? res)) (< (length stems) 2) (not raw) (memq #f raw) (not (apply = dirs)))
        res
        (let* ((near (map (lambda (y) (* -1 d y)) raw))
               (ps (map (lambda (y) (inexact->exact (round (* -2 y)))) near))   ; d x staff position: >= 0 points away from the centre
               (a (* -1 d (car res))) (b (* -1 d (cdr res)))
               (sloped (> (abs (- b a)) 0.01))
               (sys (ly:grob-system grob))
               (xs (map (lambda (s) (ly:grob-relative-coordinate s sys X)) stems))
               (x0 (car xs)) (x1 (car (last-pair xs)))
               (at (lambda (x a b) (+ a (* (- b a) (if (= x1 x0) 0 (/ (- x x0) (- x1 x0)))))))
               (deficit (apply max (map (lambda (x y p) (- (c375-target p sloped) (+ (- y (at x a b)) 0.24))) xs near ps))))
          (if (or (and (any negative? ps) (< (length stems) 3)) (<= deficit 0.15))   ; c465: horizontal groups of 3+ also; c555: sloped groups of 3+ also
              res
              (let* ((inside? (lambda (y) (<= (abs y) 2.3)))
                     (ok? (lambda (s) (every (lambda (y) (or (not (inside? y)) (c375-attached? y))) (list (- a s) (- b s)))))
                     (s (let loop ((s deficit)) (if (or (ok? s) (> s (+ deficit 1.0))) s (loop (+ s 0.01))))))
                (cons (* -1 d (- a s)) (* -1 d (- b s)))))))))
