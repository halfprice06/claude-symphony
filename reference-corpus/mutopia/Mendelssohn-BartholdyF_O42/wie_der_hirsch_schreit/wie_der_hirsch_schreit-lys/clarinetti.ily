\version "2.22.0"

\new Staff = "clarinetti" {
	\set Staff.instrumentName = "Clarinetti in B"
	\set Staff.midiInstrument = "clarinet"
	<<
		\transposition bes \partCombine \clarinettoI \clarinettoII
		\Markings
	>>
}
