\version "2.26.0"
% Scherzo v600 definitions for the mockup extraction: score.ly's \sec / \secDrum helpers and its includes, without the
% \layout, \score, \midi blocks, beams.ily / stems.ily (print only), rolls-midi.ily and the chordFadeMidi / hornFadeMidi
% expression fades (MIDI-only; the mockup draws the printed hairpins as CC11 itself).
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
