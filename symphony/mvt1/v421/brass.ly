\version "2.24.0"
\language "nederlands"
sec = #(define-music-function (name bars) (string? integer?)
  (let ((v (ly:parser-lookup (string->symbol name))))
    (if (ly:music? v) v
        (make-music 'MultiMeasureRestMusic 'duration (ly:make-duration 0 0 bars)))))
secDrum = #(define-music-function (name bars) (string? integer?)
  (let ((v (ly:parser-lookup (string->symbol name))))
    (if (ly:music? v) v
        (make-music 'MultiMeasureRestMusic 'duration (ly:make-duration 0 0 bars)))))
\include "global.ily"
\include "sections/intro.ily"
\include "sections/tOne.ily"
\include "sections/trans.ily"
\include "sections/tTwo.ily"
\include "sections/clos.ily"
\include "sections/dev.ily"
\include "sections/recOne.ily"
\include "sections/recTwo.ily"
\include "sections/coda.ily"
\include "parts.ily"
\score { <<
 \new Staff = "hn1" << \global \hnOne >>
 \new Staff = "hn2" << \global \hnTwo >>
 \new Staff = "hn3" << \global \hnThree >>
 \new Staff = "hn4" << \global \hnFour >>
 \new Staff = "tp1" << \global \tptOne >>
 \new Staff = "tp2" << \global \tptTwo >>
 \new Staff = "tp3" << \global \tptThree >>
 \new Staff = "tb1" << \global \tbnOne >>
 \new Staff = "tb2" << \global \tbnTwo >>
 \new Staff = "btb" << \global \bassTbn >>
 \new Staff = "tba" << \global \tuba >>
 \new Staff = "timp" << \global \timp >>
>> \midi { \context { \Score midiChannelMapping = #'staff
      dynamicAbsoluteVolumeFunction = #(lambda (d) (if (string? d)
      (assoc-get d '(("ppp" . 0.25) ("pp" . 0.33) ("p" . 0.42) ("mp" . 0.5) ("mf" . 0.58) ("f" . 0.66) ("ff" . 0.72) ("fff" . 1.0) ("sf" . 0.66) ("fp" . 0.42)) #f)
      0.42)) } } }
