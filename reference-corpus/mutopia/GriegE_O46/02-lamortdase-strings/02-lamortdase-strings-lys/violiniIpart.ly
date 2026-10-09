\version "2.22.0"

#(set-global-staff-size 20)

\include "header.ly"
\include "violiniI.ly"

\score {
  << 
    \new Staff = violiniI \with {
      midiInstrument = #"violin"
      instrumentName = \markup {
        \center-column { "Violini I" \line {"(con sordini)"} }
      }
      shortInstrumentName = #"Vl.I "
    }
	\partCombine \violinioneI \violinioneII
  >>
\include "paper.ly"
\include "midi.ly"
}
