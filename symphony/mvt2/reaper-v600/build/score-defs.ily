\version "2.26.0"
sec = #(define-music-function (name bars beats) (string? integer? integer?)
  (let ((v (ly:parser-lookup (string->symbol name))))
    (if (ly:music? v) v
        (make-music 'MultiMeasureRestMusic 'duration (ly:make-duration 2 0 (* bars beats))))))
secDrum = #(define-music-function (name bars beats) (string? integer? integer?)
  (let ((v (ly:parser-lookup (string->symbol name))))
    (if (ly:music? v) v
        (make-music 'MultiMeasureRestMusic 'duration (ly:make-duration 2 0 (* bars beats))))))

\include "global.ily"
\include "sections/intro.ily"
\include "sections/aOne.ily"
\include "sections/trans.ily"
\include "sections/bSec.ily"
\include "sections/retr.ily"
\include "sections/aTwo.ily"
\include "sections/coda.ily"
\include "parts.ily"

