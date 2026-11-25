\version "2.24.0"
\paper { indent = 0 line-width = 120\mm }
\layout { \context { \Score \remove "Bar_number_engraver" } }
{ \clef treble \key c \minor \time 4/4 \omit Staff.TimeSignature
  r8 g'8( es''4.->) d''8( des''8 c''8 | c''4--) b'8( c''8) aes'4.-> g'8 \bar "" }
