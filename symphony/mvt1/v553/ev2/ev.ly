\version "2.24.0"
\language "nederlands"

\header {
  title = "Symphony No. 1 in C minor"
  subtitle = "I. Lento — Allegro appassionato"
  subsubtitle = \markup \center-column { "Full score in C — draft v165" \small "Contrabassoon and double basses sound an octave lower than written" }
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
\include "el.ly"
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

\score { << \new Staff \with { instrumentName = "fluteOne" } << \global \removeWithTag #'part \fluteOne >>
\new Staff \with { instrumentName = "fluteTwo" } << \global \removeWithTag #'part \fluteTwo >>
\new Staff \with { instrumentName = "oboeOne" } << \global \removeWithTag #'part \oboeOne >>
\new Staff \with { instrumentName = "oboeTwo" } << \global \removeWithTag #'part \oboeTwo >>
\new Staff \with { instrumentName = "corAnglais" } << \global \removeWithTag #'part \corAnglais >>
\new Staff \with { instrumentName = "clOne" } << \global \removeWithTag #'part \clOne >>
\new Staff \with { instrumentName = "clTwo" } << \global \removeWithTag #'part \clTwo >>
\new Staff \with { instrumentName = "bassCl" } << \global \removeWithTag #'part \bassCl >>
\new Staff \with { instrumentName = "bsnOne" } << \global \removeWithTag #'part \bsnOne >>
\new Staff \with { instrumentName = "bsnTwo" } << \global \removeWithTag #'part \bsnTwo >>
\new Staff \with { instrumentName = "cbsn" } << \global \removeWithTag #'part \cbsn >>
\new Staff \with { instrumentName = "hnOne" } << \global \removeWithTag #'part \hnOne >>
\new Staff \with { instrumentName = "hnTwo" } << \global \removeWithTag #'part \hnTwo >>
\new Staff \with { instrumentName = "hnThree" } << \global \removeWithTag #'part \hnThree >>
\new Staff \with { instrumentName = "hnFour" } << \global \removeWithTag #'part \hnFour >>
\new Staff \with { instrumentName = "tptOne" } << \global \removeWithTag #'part \tptOne >>
\new Staff \with { instrumentName = "tptTwo" } << \global \removeWithTag #'part \tptTwo >>
\new Staff \with { instrumentName = "tptThree" } << \global \removeWithTag #'part \tptThree >>
\new Staff \with { instrumentName = "tbnOne" } << \global \removeWithTag #'part \tbnOne >>
\new Staff \with { instrumentName = "tbnTwo" } << \global \removeWithTag #'part \tbnTwo >>
\new Staff \with { instrumentName = "bassTbn" } << \global \removeWithTag #'part \bassTbn >>
\new Staff \with { instrumentName = "tuba" } << \global \removeWithTag #'part \tuba >>
\new Staff \with { instrumentName = "timp" } << \global \removeWithTag #'part \timp >>
\new Staff \with { instrumentName = "harpR" } << \global \removeWithTag #'part \harpR >>
\new Staff \with { instrumentName = "harpL" } << \global \removeWithTag #'part \harpL >>
\new Staff \with { instrumentName = "vlnOne" } << \global \removeWithTag #'part \vlnOne >>
\new Staff \with { instrumentName = "vlnTwo" } << \global \removeWithTag #'part \vlnTwo >>
\new Staff \with { instrumentName = "vla" } << \global \removeWithTag #'part \vla >>
\new Staff \with { instrumentName = "vc" } << \global \removeWithTag #'part \vc >>
\new Staff \with { instrumentName = "cb" } << \global \removeWithTag #'part \cb >> >> \layout { } }
