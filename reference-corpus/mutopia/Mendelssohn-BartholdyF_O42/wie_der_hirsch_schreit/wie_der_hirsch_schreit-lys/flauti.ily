\version "2.22.0"

\new Staff = "flauti" {
	\set Staff.instrumentName = "Flauti"
	\set Staff.midiInstrument = "flute"
	<<
		\partCombine \flautoI \flautoII
		\Markings
	>>
}
