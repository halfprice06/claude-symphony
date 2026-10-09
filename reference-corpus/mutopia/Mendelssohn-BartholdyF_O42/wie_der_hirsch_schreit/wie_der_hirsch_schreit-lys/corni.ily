\version "2.22.0"

\new Staff = "corni" {
	\set Staff.instrumentName = "4 Corni in F"
	\set Staff.midiInstrument = "english horn"
	<<
		\transposition f \partCombine \cornoI \cornoII
		\Markings
	>>
}
