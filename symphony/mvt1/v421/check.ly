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

\score { << \new Staff = "fluteOne" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \fluteOne >>
\new Staff = "fluteTwo" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \fluteTwo >>
\new Staff = "oboeOne" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \oboeOne >>
\new Staff = "oboeTwo" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \oboeTwo >>
\new Staff = "corAnglais" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \corAnglais >>
\new Staff = "clOne" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \clOne >>
\new Staff = "clTwo" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \clTwo >>
\new Staff = "bassCl" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \bassCl >>
\new Staff = "bsnOne" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \bsnOne >>
\new Staff = "bsnTwo" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \bsnTwo >>
\new Staff = "cbsn" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \cbsn >>
\new Staff = "hnOne" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \hnOne >>
\new Staff = "hnTwo" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \hnTwo >>
\new Staff = "hnThree" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \hnThree >>
\new Staff = "hnFour" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \hnFour >>
\new Staff = "tptOne" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \tptOne >>
\new Staff = "tptTwo" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \tptTwo >>
\new Staff = "tptThree" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \tptThree >>
\new Staff = "tbnOne" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \tbnOne >>
\new Staff = "tbnTwo" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \tbnTwo >>
\new Staff = "bassTbn" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \bassTbn >>
\new Staff = "tuba" \with { midiInstrument = "flute" } << \global \removeWithTag #'part \tuba >> >> \midi { \context { \Score dynamicAbsoluteVolumeFunction = #(lambda (d) (if (string? d)
      (assoc-get d '(("ppp" . 0.25) ("pp" . 0.33) ("p" . 0.42) ("mp" . 0.5) ("mf" . 0.58) ("f" . 0.66) ("ff" . 0.72) ("fff" . 1.0) ("sf" . 0.66) ("fp" . 0.42)) #f)
      0.42)) } } }
