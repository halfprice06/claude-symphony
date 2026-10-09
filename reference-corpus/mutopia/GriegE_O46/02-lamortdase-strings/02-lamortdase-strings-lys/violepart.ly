\version "2.22.0"

#(set-global-staff-size 20)
\include "header.ly"
\include "viole.ly"

\score {
  << 
    \new Staff = viole \with {
      midiInstrument = #"viola"
      instrumentName = \markup {
        \center-column { "Viole" \line { "(con sordini)" } }
      }
      shortInstrumentName = #"Vla. "
    }
 	\partCombine \violeI \violeII
  >>
\include "paper.ly"
\include "midi.ly"
}
