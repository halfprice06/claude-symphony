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

\include "el.ly"
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

\score { << \new Staff = "fluteOne" \with { instrumentName = "fluteOne" } << \global \removeWithTag #'part \fluteOne >>
\new Staff = "fluteTwo" \with { instrumentName = "fluteTwo" } << \global \removeWithTag #'part \fluteTwo >>
\new Staff = "oboeOne" \with { instrumentName = "oboeOne" } << \global \removeWithTag #'part \oboeOne >>
\new Staff = "oboeTwo" \with { instrumentName = "oboeTwo" } << \global \removeWithTag #'part \oboeTwo >>
\new Staff = "corAnglais" \with { instrumentName = "corAnglais" } << \global \removeWithTag #'part \corAnglais >>
\new Staff = "clOne" \with { instrumentName = "clOne" } << \global \removeWithTag #'part \clOne >>
\new Staff = "clTwo" \with { instrumentName = "clTwo" } << \global \removeWithTag #'part \clTwo >>
\new Staff = "bassCl" \with { instrumentName = "bassCl" } << \global \removeWithTag #'part \bassCl >>
\new Staff = "bsnOne" \with { instrumentName = "bsnOne" } << \global \removeWithTag #'part \bsnOne >>
\new Staff = "bsnTwo" \with { instrumentName = "bsnTwo" } << \global \removeWithTag #'part \bsnTwo >>
\new Staff = "cbsn" \with { instrumentName = "cbsn" } << \global \removeWithTag #'part \cbsn >>
\new Staff = "hnOne" \with { instrumentName = "hnOne" } << \global \removeWithTag #'part \hnOne >>
\new Staff = "hnTwo" \with { instrumentName = "hnTwo" } << \global \removeWithTag #'part \hnTwo >>
\new Staff = "hnThree" \with { instrumentName = "hnThree" } << \global \removeWithTag #'part \hnThree >>
\new Staff = "hnFour" \with { instrumentName = "hnFour" } << \global \removeWithTag #'part \hnFour >>
\new Staff = "tptOne" \with { instrumentName = "tptOne" } << \global \removeWithTag #'part \tptOne >>
\new Staff = "tptTwo" \with { instrumentName = "tptTwo" } << \global \removeWithTag #'part \tptTwo >>
\new Staff = "tptThree" \with { instrumentName = "tptThree" } << \global \removeWithTag #'part \tptThree >>
\new Staff = "tbnOne" \with { instrumentName = "tbnOne" } << \global \removeWithTag #'part \tbnOne >>
\new Staff = "tbnTwo" \with { instrumentName = "tbnTwo" } << \global \removeWithTag #'part \tbnTwo >>
\new Staff = "bassTbn" \with { instrumentName = "bassTbn" } << \global \removeWithTag #'part \bassTbn >>
\new Staff = "tuba" \with { instrumentName = "tuba" } << \global \removeWithTag #'part \tuba >>
\new Staff = "timp" \with { instrumentName = "timp" } << \global \removeWithTag #'part \timp >>
\new Staff = "harpR" \with { instrumentName = "harpR" } << \global \removeWithTag #'part \harpR >>
\new Staff = "harpL" \with { instrumentName = "harpL" } << \global \removeWithTag #'part \harpL >>
\new Staff = "vlnOne" \with { instrumentName = "vlnOne" } << \global \removeWithTag #'part \vlnOne >>
\new Staff = "vlnTwo" \with { instrumentName = "vlnTwo" } << \global \removeWithTag #'part \vlnTwo >>
\new Staff = "vla" \with { instrumentName = "vla" } << \global \removeWithTag #'part \vla >>
\new Staff = "vc" \with { instrumentName = "vc" } << \global \removeWithTag #'part \vc >>
\new Staff = "cb" \with { instrumentName = "cb" } << \global \removeWithTag #'part \cb >> >> \layout { } }
