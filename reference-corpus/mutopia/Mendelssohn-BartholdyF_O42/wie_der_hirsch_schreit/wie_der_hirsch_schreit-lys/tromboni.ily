\version "2.22.0"

\new Staff = "tromboni" {
	\set Staff.instrumentName = "Tromboni Alto. Tenore"
	\set Staff.midiInstrument = "trombone"
	<<
		\partCombine \tromboneI \tromboneII
		\Markings
	>>
}
