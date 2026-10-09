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
stripAcc = #(define-music-function (m) (ly:music?)
  (music-map (lambda (x) (if (memq (ly:music-property x 'name) '(ArticulationEvent)) (ly:music-set-property! x 'midi-extra-velocity 0)) x) m))
\score { <<
\new Staff = "fluteOne" \with { midiInstrument = "acoustic grand" } { \stripAcc \fluteOne }
\new Staff = "fluteTwo" \with { midiInstrument = "acoustic grand" } { \stripAcc \fluteTwo }
\new Staff = "oboeOne" \with { midiInstrument = "acoustic grand" } { \stripAcc \oboeOne }
\new Staff = "oboeTwo" \with { midiInstrument = "acoustic grand" } { \stripAcc \oboeTwo }
\new Staff = "corAnglais" \with { midiInstrument = "acoustic grand" } { \stripAcc \corAnglais }
\new Staff = "clOne" \with { midiInstrument = "acoustic grand" } { \stripAcc \clOne }
\new Staff = "clTwo" \with { midiInstrument = "acoustic grand" } { \stripAcc \clTwo }
\new Staff = "bassCl" \with { midiInstrument = "acoustic grand" } { \stripAcc \bassCl }
\new Staff = "bsnOne" \with { midiInstrument = "acoustic grand" } { \stripAcc \bsnOne }
\new Staff = "bsnTwo" \with { midiInstrument = "acoustic grand" } { \stripAcc \bsnTwo }
\new Staff = "cbsn" \with { midiInstrument = "acoustic grand" } { \stripAcc \cbsn }
\new Staff = "hnOne" \with { midiInstrument = "acoustic grand" } { \stripAcc \hnOne }
\new Staff = "hnTwo" \with { midiInstrument = "acoustic grand" } { \stripAcc \hnTwo }
\new Staff = "hnThree" \with { midiInstrument = "acoustic grand" } { \stripAcc \hnThree }
\new Staff = "hnFour" \with { midiInstrument = "acoustic grand" } { \stripAcc \hnFour }
\new Staff = "tptOne" \with { midiInstrument = "acoustic grand" } { \stripAcc \tptOne }
\new Staff = "tptTwo" \with { midiInstrument = "acoustic grand" } { \stripAcc \tptTwo }
\new Staff = "tptThree" \with { midiInstrument = "acoustic grand" } { \stripAcc \tptThree }
\new Staff = "tbnOne" \with { midiInstrument = "acoustic grand" } { \stripAcc \tbnOne }
\new Staff = "tbnTwo" \with { midiInstrument = "acoustic grand" } { \stripAcc \tbnTwo }
\new Staff = "bassTbn" \with { midiInstrument = "acoustic grand" } { \stripAcc \bassTbn }
\new Staff = "tuba" \with { midiInstrument = "acoustic grand" } { \stripAcc \tuba }
\new Staff = "timp" \with { midiInstrument = "acoustic grand" } { \stripAcc \timp }
\new Staff = "harpR" \with { midiInstrument = "acoustic grand" } { \stripAcc \harpR }
\new Staff = "harpL" \with { midiInstrument = "acoustic grand" } { \stripAcc \harpL }
\new Staff = "vlnOne" \with { midiInstrument = "acoustic grand" } { \stripAcc \vlnOne }
\new Staff = "vlnTwo" \with { midiInstrument = "acoustic grand" } { \stripAcc \vlnTwo }
\new Staff = "vla" \with { midiInstrument = "acoustic grand" } { \stripAcc \vla }
\new Staff = "vc" \with { midiInstrument = "acoustic grand" } { \stripAcc \vc }
\new Staff = "cb" \with { midiInstrument = "acoustic grand" } { \stripAcc \cb }
>> \midi { \context { \Score dynamicAbsoluteVolumeFunction = #(lambda (d) (assoc-get d (quote (("ppp" . 0.25) ("pp" . 0.33) ("p" . 0.42) ("mp" . 0.5) ("mf" . 0.58) ("f" . 0.66) ("ff" . 0.72) ("fff" . 1.0))) #f)) } } }
