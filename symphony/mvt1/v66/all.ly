\version "2.24.0"
\language "nederlands"

\header {
  title = "Symphony No. 1 in C minor"
  subtitle = "I. Lento — Allegro appassionato"
  subsubtitle = "Full score in C — draft v61"
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
\score { <<
\new Staff = "fluteOne" \with { midiInstrument = "acoustic grand" } { \fluteOne }
\new Staff = "fluteTwo" \with { midiInstrument = "acoustic grand" } { \fluteTwo }
\new Staff = "oboeOne" \with { midiInstrument = "acoustic grand" } { \oboeOne }
\new Staff = "oboeTwo" \with { midiInstrument = "acoustic grand" } { \oboeTwo }
\new Staff = "corAnglais" \with { midiInstrument = "acoustic grand" } { \corAnglais }
\new Staff = "clOne" \with { midiInstrument = "acoustic grand" } { \clOne }
\new Staff = "clTwo" \with { midiInstrument = "acoustic grand" } { \clTwo }
\new Staff = "bassCl" \with { midiInstrument = "acoustic grand" } { \bassCl }
\new Staff = "bsnOne" \with { midiInstrument = "acoustic grand" } { \bsnOne }
\new Staff = "bsnTwo" \with { midiInstrument = "acoustic grand" } { \bsnTwo }
\new Staff = "cbsn" \with { midiInstrument = "acoustic grand" } { \cbsn }
\new Staff = "hnOne" \with { midiInstrument = "acoustic grand" } { \hnOne }
\new Staff = "hnTwo" \with { midiInstrument = "acoustic grand" } { \hnTwo }
\new Staff = "hnThree" \with { midiInstrument = "acoustic grand" } { \hnThree }
\new Staff = "hnFour" \with { midiInstrument = "acoustic grand" } { \hnFour }
\new Staff = "tptOne" \with { midiInstrument = "acoustic grand" } { \tptOne }
\new Staff = "tptTwo" \with { midiInstrument = "acoustic grand" } { \tptTwo }
\new Staff = "tptThree" \with { midiInstrument = "acoustic grand" } { \tptThree }
\new Staff = "tbnOne" \with { midiInstrument = "acoustic grand" } { \tbnOne }
\new Staff = "tbnTwo" \with { midiInstrument = "acoustic grand" } { \tbnTwo }
\new Staff = "bassTbn" \with { midiInstrument = "acoustic grand" } { \bassTbn }
\new Staff = "tuba" \with { midiInstrument = "acoustic grand" } { \tuba }
\new Staff = "timp" \with { midiInstrument = "acoustic grand" } { \timp }
\new Staff = "harpR" \with { midiInstrument = "acoustic grand" } { \harpR }
\new Staff = "harpL" \with { midiInstrument = "acoustic grand" } { \harpL }
\new Staff = "vlnOne" \with { midiInstrument = "acoustic grand" } { \vlnOne }
\new Staff = "vlnTwo" \with { midiInstrument = "acoustic grand" } { \vlnTwo }
\new Staff = "vla" \with { midiInstrument = "acoustic grand" } { \vla }
\new Staff = "vc" \with { midiInstrument = "acoustic grand" } { \vc }
\new Staff = "cb" \with { midiInstrument = "acoustic grand" } { \cb }
>> \midi { } }
