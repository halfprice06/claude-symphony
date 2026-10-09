
\version "2.22.0"

\include "header.ly"

\include "violiniI.ly"
\include "violiniII.ly"
\include "viole.ly"
\include "violoncelli.ly"
\include "contrabassi.ly"

\score {
  <<
    \context StaffGroup = strings <<
      \new Staff = violiniI \with {
        midiInstrument = #"violin"
        instrumentName = \markup {
          \center-column { "Violini I" \line {"(con sordini)"} }
        }
        shortInstrumentName = #"Vl.I"
      }
      \partCombine \violinioneI \violinioneII

      \new Staff = violiniII \with {
        midiInstrument = #"violin"
        instrumentName = \markup {
          \center-column {"Violini II" \line { "(con sordini)" } }
        }
        shortInstrumentName = #"Vl.II"
      }
      \partCombine \violinitwoI \violinitwoII

      \new Staff = viole \with {
        midiInstrument = #"viola"
        instrumentName = \markup {
          \center-column { "Viole" \line { "(con sordini)" } }
        }
        shortInstrumentName = #"Vla."
      }
      \partCombine \violeI \violeII

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

      \context Staff = contrabassi \with {
        midiInstrument = #"contrabass"
        instrumentName = #"Contrabassi"
        shortInstrumentName = #"Cb."
        %\property Staff.transposing = #-12
        } <<
          \transposition c 
          \clef "bass"
          \new Voice=contrabassi \contrabassi
        >>
    >>
>>

\include "paper.ly"
\include "midi.ly"
}
