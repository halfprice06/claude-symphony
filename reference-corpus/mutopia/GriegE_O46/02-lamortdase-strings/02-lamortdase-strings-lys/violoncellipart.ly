\version "2.22.0"

#(set-global-staff-size 20)
\include "header.ly"
\include "violoncelli.ly"

\score {
    << 
      \context Staff = violoncelli \with {
        midiInstrument = #"cello"
        instrumentName = \markup {
          \center-column { "Violoncelli" \line{ "(con sordini)" } }
        }
        shortInstrumentName = #"Vc."
      } <<
        \clef "bass"
        \partCombine \violoncelliI \violoncelliII \violoncelliIII
      >>
    >>
\include "paper.ly"
\include "midi.ly"
}
