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
#(define (gould-ledger-beam-positions grob)
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
