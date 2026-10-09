\version "2.22.0"

\new Staff = "fagottii" {
	\set Staff.instrumentName = "Fagotti"
	\set Staff.midiInstrument = "bassoon"
	<<
		\partCombine \fagottoI \fagottoII
		\Markings
	>>
}
