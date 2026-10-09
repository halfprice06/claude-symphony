\version "2.22.0"
\include "header.ly"
\include "violiniII.ly"
\header { instrument="Violini II" }

\score {
  \new Staff \with \violiniTwoStaffSettings
  {
    \partCombine \violinitwoI \violinitwoII
    \bar "|."
  }
  \layout {
    indent = 3 \cm
    short-indent = 1.5 \cm
  }

  \midi {
    \tempo 4 = 160
  }
}
