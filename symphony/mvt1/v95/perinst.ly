\version "2.24.0"
\language "nederlands"

\header {
  title = "Symphony No. 1 in C minor"
  subtitle = "I. Lento — Allegro appassionato"
  subsubtitle = "Full score in C — draft v93"
  tagline = ##f
}

#(set-global-staff-size 14)
\paper {
  #(set-paper-size "a3")
  left-margin = 15\mm
  right-margin = 12\mm
  system-separator-markup = \slashSeparator
  page-count = 17
}

% A section variable, or full-bar rests of the section's length if the instrument is silent there.
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

\score { << \new Staff = "fluteOne" << \global \fluteOne >>
\new Staff = "fluteTwo" << \global \fluteTwo >>
\new Staff = "oboeOne" << \global \oboeOne >>
\new Staff = "oboeTwo" << \global \oboeTwo >>
\new Staff = "corAnglais" << \global \corAnglais >>
\new Staff = "clOne" << \global \clOne >>
\new Staff = "clTwo" << \global \clTwo >>
\new Staff = "bassCl" << \global \bassCl >>
\new Staff = "bsnOne" << \global \bsnOne >>
\new Staff = "bsnTwo" << \global \bsnTwo >>
\new Staff = "cbsn" << \global \cbsn >>
\new Staff = "hnOne" << \global \hnOne >>
\new Staff = "hnTwo" << \global \hnTwo >>
\new Staff = "hnThree" << \global \hnThree >>
\new Staff = "hnFour" << \global \hnFour >>
\new Staff = "tptOne" << \global \tptOne >>
\new Staff = "tptTwo" << \global \tptTwo >>
\new Staff = "tptThree" << \global \tptThree >>
\new Staff = "tbnOne" << \global \tbnOne >>
\new Staff = "tbnTwo" << \global \tbnTwo >>
\new Staff = "bassTbn" << \global \bassTbn >>
\new Staff = "tuba" << \global \tuba >>
\new Staff = "timp" << \global \timp >>
\new Staff = "harpR" << \global \harpR >>
\new Staff = "harpL" << \global \harpL >>
\new Staff = "vlnOne" << \global \vlnOne >>
\new Staff = "vlnTwo" << \global \vlnTwo >>
\new Staff = "vla" << \global \vla >>
\new Staff = "vc" << \global \vc >>
\new Staff = "cb" << \global \cb >> >> \midi { } }
