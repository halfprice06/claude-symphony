\version "2.24.0"
\language "nederlands"

\header {
  title = "Symphony No. 1 in C minor"
  subtitle = "III. Scherzo: Allegro vivace"  % c100: the four titles name the movement and its tempo, as I ("Lento — Allegro appassionato"), II ("Adagio") and IV ("Finale: Allegro con fuoco") do
  subsubtitle = \markup \center-column { "Full score in C — draft v104" \small "Contrabassoon and double basses sound an octave lower than written" \small "After movement II (Adagio): a pause" \small "Trumpet 3 tacet" \small "Duration: about 4½ minutes" }  % c045: approximate duration of the movement (MOLA PDF 6)
  tagline = ##f
}

#(set-global-staff-size 14)
\paper {
  #(set-paper-size "a3")
  left-margin = 15\mm
  right-margin = 12\mm
  system-separator-markup = \slashSeparator
}

% A section variable, or full-bar rests of the section's length if the instrument is silent there.
% mvt2: mixed metre, so the rest length is bars x quarter-beats per bar.
sec = #(define-music-function (name bars beats) (string? integer? integer?)
  (let ((v (ly:parser-lookup (string->symbol name))))
    (if (ly:music? v) v
        (make-music 'MultiMeasureRestMusic 'duration (ly:make-duration 2 0 (* bars beats))))))
secDrum = #(define-music-function (name bars beats) (string? integer? integer?)
  (let ((v (ly:parser-lookup (string->symbol name))))
    (if (ly:music? v) v
        (make-music 'MultiMeasureRestMusic 'duration (ly:make-duration 2 0 (* bars beats))))))

% c125: an articulation on the stem side (the second voice of a shared staff, and up-stem chords with scripts above) sat on the
% stem end, touching it (bars 61-62: tenutos in Fl, Ob, Cl, Bn 1-2). Gould, Behind Bars PDF 55: characters at least half a space apart, none colliding.
% Scripts on the notehead side are unchanged; on a stem end they move 0.4 space further out (about 0.6 space clear of the stem).
#(define (stem-side-y-offset grob)
  (let* ((y (ly:side-position-interface::y-aligned-side grob))
         (nc (ly:grob-parent grob X))
         (stem (if (ly:grob? nc) (ly:grob-object nc 'stem) '()))
         (dir (ly:grob-property grob 'direction)))
    (if (and (ly:grob? stem) (>= (ly:grob-property stem 'duration-log 0) 1)
             (eqv? dir (ly:grob-property stem 'direction)))
        (let* ((ref (ly:grob-parent grob Y))
               (se (ly:grob-extent stem ref Y))
               (st (ly:grob-property grob 'stencil))
               (ex (if (ly:stencil? st) (ly:stencil-extent st Y) '(0 . 0)))
               (gap (if (> dir 0) (- (+ y (car ex)) (cdr se)) (- (car se) (+ y (cdr ex))))))
          (if (< gap 0.5)
              (+ y (* dir (if (< (abs y) 2.4) 1.0 (- 0.6 gap))))  ; inside the stave a whole space, so a quantized tenuto stays in a space
              y))
        y)))

% c015: beams of groups lying wholly beyond the first ledger line (Gould, Behind Bars PDF 33 and 35). By default every stem
% reached the middle line, so Fl 1 at 169-184 and 257-272 had stems of 5½-7 spaces and flat beams on the middle line.
% Gould: such a beam sits inside the stave with one clear stave-line between it and the first ledger line, stems close to
% 3-3½ spaces, slope ¼ space for a second and ½ for wider intervals, horizontal for repeated or concave groups (PDF 36-37).
% Other groups keep LilyPond's default placement.
#(define (gould-ledger-beam-positions grob)
  (let* ((stems (ly:grob-array->list (ly:grob-object grob 'stems)))
         (dirs (map (lambda (s) (ly:grob-property s 'direction)) stems))
         (heads (map (lambda (s)
                  (let ((hs (ly:grob-object s 'note-heads)))
                    (if (ly:grob-array? hs)
                        (map (lambda (h) (ly:grob-property h 'staff-position)) (ly:grob-array->list hs))
                        '())))
                 stems))
         (n (length stems)))
    (if (or (< n 2) (memq '() heads)
            (not (apply = dirs)))
        (beam::place-broken-parts-individually grob)
        (let* ((d (car dirs))
               ;; the note of each stem nearest the beam, in spaces, mirrored so that "above the stave, stems down" is the case
               (near (map (lambda (ps) (* -1 d (/ (if (< d 0) (apply min ps) (apply max ps)) 2.0))) heads)))
          (if (not (every (lambda (y) (>= y 3.5)) near))
              (beam::place-broken-parts-individually grob)
              (let* ((first (car near)) (last (car (last-pair near)))
                     (inner (if (> n 2) (cdr (reverse (cdr (reverse near)))) '()))
                     (concave (any (lambda (y) (< y (min first last))) inner))
                     (iv (abs (- last first)))
                     (slope (cond ((or concave (< iv 0.25)) 0.0) ((<= iv 0.5) 0.25) (else 0.52)))
                     (sgn (if (> last first) 1 -1))
                     (frac (lambda (i) (if (> sgn 0) (/ i (- n 1.0)) (- 1 (/ i (- n 1.0))))))
                     (ok? (lambda (base)
                            (let loop ((i 0) (ys near))
                              (or (null? ys)
                                  (and (>= (- (car ys) (+ base (* slope (frac i)))) 3.0)
                                       (loop (1+ i) (cdr ys)))))))
                     (base (let pick ((cands '(1.24 0.76 0.24 -0.24 -0.76)))
                             (cond ((null? cands) #f) ((ok? (car cands)) (car cands)) (else (pick (cdr cands))))))
                     (yl (and base (+ base (* slope (frac 0)))))
                     (yr (and base (+ base (* slope (frac (- n 1)))))))
                (if base
                    (cons (* -1 d yl) (* -1 d yr))
                    (beam::place-broken-parts-individually grob))))))))
\include "stems.ily"  % c095: middle-line stems follow the surrounding stems (Gould PDF 27-28, 60-61)

\include "global.ily"
\include "sections/intro.ily"
\include "sections/sA.ily"
\include "sections/sB.ily"
\include "sections/sC.ily"
\include "sections/link.ily"
\include "sections/tA.ily"
\include "sections/tB.ily"
\include "sections/tC.ily"
\include "sections/retr.ily"
\include "sections/dA.ily"
\include "sections/dB.ily"
\include "sections/dC.ily"
\include "sections/coda.ily"
\include "parts.ily"
\score { <<
  \new Staff = "fluteOne" << \global \removeWithTag #'part \fluteOne >>
  \new Staff = "fluteTwo" << \global \removeWithTag #'part \fluteTwo >>
  \new Staff = "oboeOne" << \global \removeWithTag #'part \oboeOne >>
  \new Staff = "oboeTwo" << \global \removeWithTag #'part \oboeTwo >>
  \new Staff = "corAnglais" << \global \removeWithTag #'part \corAnglais >>
  \new Staff = "clOne" << \global \removeWithTag #'part \clOne >>
  \new Staff = "clTwo" << \global \removeWithTag #'part \clTwo >>
  \new Staff = "bassCl" << \global \removeWithTag #'part \bassCl >>
  \new Staff = "bsnOne" << \global \removeWithTag #'part \bsnOne >>
  \new Staff = "bsnTwo" << \global \removeWithTag #'part \bsnTwo >>
  \new Staff = "cbsn" << \global \removeWithTag #'part \cbsn >>
  \new Staff = "hnOne" << \global \removeWithTag #'part \hnOne >>
  \new Staff = "hnTwo" << \global \removeWithTag #'part \hnTwo >>
  \new Staff = "hnThree" << \global \removeWithTag #'part \hnThree >>
  \new Staff = "hnFour" << \global \removeWithTag #'part \hnFour >>
  \new Staff = "tptOne" << \global \removeWithTag #'part \tptOne >>
  \new Staff = "tptTwo" << \global \removeWithTag #'part \tptTwo >>
  \new Staff = "tbnOne" << \global \removeWithTag #'part \tbnOne >>
  \new Staff = "tbnTwo" << \global \removeWithTag #'part \tbnTwo >>
  \new Staff = "bassTbn" << \global \removeWithTag #'part \bassTbn >>
  \new Staff = "tuba" << \global \removeWithTag #'part \tuba >>
  \new Staff = "timp" << \global \removeWithTag #'part \timp >>
  \new Staff = "harpR" << \global \removeWithTag #'part \harpR >>
  \new Staff = "harpL" << \global \removeWithTag #'part \harpL >>
  \new Staff = "vlnOne" << \global \removeWithTag #'part \vlnOne >>
  \new Staff = "vlnTwo" << \global \removeWithTag #'part \vlnTwo >>
  \new Staff = "vla" << \global \removeWithTag #'part \vla >>
  \new Staff = "vc" << \global \removeWithTag #'part \vc >>
  \new Staff = "cb" << \global \removeWithTag #'part \cb >>
>>
 \midi { } }
