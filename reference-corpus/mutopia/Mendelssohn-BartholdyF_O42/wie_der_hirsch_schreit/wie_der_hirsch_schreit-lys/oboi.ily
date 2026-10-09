\version "2.22.0"

\new Staff = "oboi" {
	\set Staff.instrumentName = "Oboi"
	\set Staff.midiInstrument = "oboe"
	<<
		\partCombine \oboeI \oboeII
		\Markings
	>>
}
