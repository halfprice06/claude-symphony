\version "2.22.0"

\new Staff = "trombe" {
	\set Staff.instrumentName = "Trombe in C"
	\set Staff.midiInstrument = "trumpet"
	<<
		\transposition f \partCombine \trombeI \trombeII
		\Markings
	>>
}
