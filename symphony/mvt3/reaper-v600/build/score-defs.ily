\version "2.26.0"
\language "nederlands"
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
\include "global.ily"
\include "sections/intro.ily"
\include "sections/pOne.ily"
\include "sections/pTwo.ily"
\include "sections/trans.ily"
\include "sections/sOne.ily"
\include "sections/sTwo.ily"
\include "sections/clos.ily"
\include "sections/dev.ily"
\include "sections/retr.ily"
\include "sections/recP.ily"
\include "sections/recS.ily"
\include "sections/codaOne.ily"
\include "sections/codaTwo.ily"
\include "sections/arrival.ily"
\include "sections/sHead.ily"
\include "sections/finale.ily"
\include "parts.ily"
% c075 (MOLA PDF 5: logical cues during long rests in the parts): sources of the part-only cues (tag 'part, see trans, sOne, recP, retr, arrival).
% Every staff below reads its player through \removeWithTag #'part, so the cues never reach the score or the MIDI.
\addQuote "oboeOne" { \removeWithTag #'part \oboeOne }
\addQuote "tptOne" { \removeWithTag #'part \tptOne }
\addQuote "vlnOne" { \removeWithTag #'part \vlnOne }
\addQuote "vlnTwo" { \removeWithTag #'part \vlnTwo }
\addQuote "bsnOne" { \removeWithTag #'part \bsnOne }
\addQuote "clOne" { \removeWithTag #'part \clOne }  % c435: cue source for Fl 1, Hn 3, Hn 4 at 127-128 (MOLA PDF 5)
\addQuote "vc" { \removeWithTag #'part \vc }  % c105: cue source for the low brass and timpani at 197-198
