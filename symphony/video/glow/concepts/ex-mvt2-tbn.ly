\version "2.24.0"
\paper { indent = 0 line-width = 120\mm }
\layout { \context { \Score \remove "Bar_number_engraver" } }
{ \clef bass \key a \minor \time 4/4 \omit Staff.TimeSignature
  r8 e8( c'4.->) b8( bes8 a8 | a4--) gis8( a8) f4.-> e8 \bar "" }
