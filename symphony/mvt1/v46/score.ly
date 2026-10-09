\version "2.24.0"
\language "nederlands"

\header {
  title = "Symphony No. 1 in C minor"
  subtitle = "I. Lento — Allegro appassionato"
  subsubtitle = "Full score in C — draft v46"
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

\layout {
  \context { \Staff \RemoveEmptyStaves soloText = "1." soloIIText = "2." }
  \context { \DrumStaff \RemoveEmptyStaves }
  % One set of dynamics per staff: two players sharing a staff print a shared dynamic once.
  \context { \Voice \remove "Dynamic_engraver" \remove "Dynamic_align_engraver" }
  \context { \Staff \consists "Dynamic_engraver" \consists "Dynamic_align_engraver" }
  \context { \Score
    rehearsalMarkFormatter = #format-mark-box-letters
    \override RehearsalMark.font-size = #3
    \override BarNumber.break-visibility = ##(#f #t #t)
    \override BarNumber.font-size = #-1
    \override BarNumber.padding = #2
    barNumberVisibility = #(every-nth-bar-number-visible 1)
  }
}

pc = #(define-music-function (a b) (ly:music? ly:music?) #{ \partCombine #a #b #})

\score {
  <<
    \new StaffGroup <<
      \new Staff = "Flutes 1·2" \with { instrumentName = "Flutes 1·2" shortInstrumentName = "Fl." midiInstrument = "flute" }
        << \global \pc \fluteOne \fluteTwo >>
      \new Staff = "Oboes 1·2" \with { instrumentName = "Oboes 1·2" shortInstrumentName = "Ob." midiInstrument = "oboe" }
        << \global \pc \oboeOne \oboeTwo >>
      \new Staff = "Cor anglais" \with { instrumentName = "Cor anglais" shortInstrumentName = "C.a." midiInstrument = "english horn" }
        << \global \corAnglais >>
      \new Staff = "Clarinets 1·2" \with { instrumentName = "Clarinets 1·2" shortInstrumentName = "Cl." midiInstrument = "clarinet" }
        << \global \pc \clOne \clTwo >>
      \new Staff = "Bass clarinet" \with { instrumentName = "Bass clarinet" shortInstrumentName = "B.cl." midiInstrument = "clarinet" }
        << \clef bass \global \bassCl >>
      \new Staff = "Bassoons 1·2" \with { instrumentName = "Bassoons 1·2" shortInstrumentName = "Bn." midiInstrument = "bassoon" }
        << \clef bass \global \pc \bsnOne \bsnTwo >>
      \new Staff = "Contrabassoon" \with { instrumentName = "Contrabassoon" shortInstrumentName = "Cbn." midiInstrument = "bassoon" }
        << \clef bass \global \transposition c \transpose c c' \cbsn >>
    >>
    \new StaffGroup <<
      \new Staff = "Horns 1·2" \with { instrumentName = "Horns 1·2" shortInstrumentName = "Hn. 1·2" midiInstrument = "french horn" }
        << \global \pc \hnOne \hnTwo >>
      \new Staff = "Horns 3·4" \with { instrumentName = "Horns 3·4" shortInstrumentName = "Hn. 3·4" midiInstrument = "french horn" }
        << \global \pc \hnThree \hnFour >>
      \new Staff = "Trumpets 1·2" \with { instrumentName = "Trumpets 1·2" shortInstrumentName = "Tpt. 1·2" midiInstrument = "trumpet" }
        << \global \pc \tptOne \tptTwo >>
      \new Staff = "Trumpet 3" \with { instrumentName = "Trumpet 3" shortInstrumentName = "Tpt. 3" midiInstrument = "trumpet" }
        << \global \tptThree >>
      \new Staff = "Trombones 1·2" \with { instrumentName = "Trombones 1·2" shortInstrumentName = "Tbn." midiInstrument = "trombone" }
        << \clef bass \global \pc \tbnOne \tbnTwo >>
      \new Staff = "Bass trombone" \with { instrumentName = "Bass trombone" shortInstrumentName = "B.tbn." midiInstrument = "trombone" }
        << \clef bass \global \bassTbn >>
      \new Staff = "Tuba" \with { instrumentName = "Tuba" shortInstrumentName = "Tba." midiInstrument = "tuba" }
        << \clef bass \global \tuba >>
    >>
    \new Staff = "Timpani" \with { instrumentName = "Timpani" shortInstrumentName = "Timp." midiInstrument = "timpani" }
      << \clef bass \global \timp >>
    \new DrumStaff \with { instrumentName = \markup \center-column { "Cymbals" "Tam-tam" "(2 players)" } shortInstrumentName = "Cym. T.-t." }
      << \global \perc >>
    \new PianoStaff \with { instrumentName = "Harp" shortInstrumentName = "Hp." } <<
      \new Staff = "Harp RH" \with { midiInstrument = "orchestral harp" } << \global \harpR >>
      \new Staff = "Harp LH" \with { midiInstrument = "orchestral harp" } << \clef bass \global \harpL >>
    >>
    \new StaffGroup <<
      \new Staff = "Violins I" \with { \consists "Mark_engraver" \consists "Metronome_mark_engraver" instrumentName = "Violins I" shortInstrumentName = "Vln. I" midiInstrument = "string ensemble 1" }
        << \global \vlnOne >>
      \new Staff = "Violins II" \with { instrumentName = "Violins II" shortInstrumentName = "Vln. II" midiInstrument = "string ensemble 1" }
        << \global \vlnTwo >>
      \new Staff = "Violas" \with { instrumentName = "Violas" shortInstrumentName = "Vla." midiInstrument = "viola" }
        << \clef alto \global \vla >>
      \new Staff = "Violoncellos" \with { instrumentName = "Violoncellos" shortInstrumentName = "Vc." midiInstrument = "cello" }
        << \clef bass \global \vc >>
      \new Staff = "Double basses" \with { instrumentName = "Double basses" shortInstrumentName = "Cb." midiInstrument = "contrabass" }
        << \clef bass \global \transposition c \transpose c c' \cb >>
    >>
  >>
  \layout { }
  \midi { \context { \Score midiChannelMapping = #'instrument } }
}
