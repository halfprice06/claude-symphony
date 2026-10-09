\version "2.22.0"

\layout {
	\compressEmptyMeasures
}

\score{
\include \instrument
	\layout {
		\context {
			\Staff
			\override InstrumentName.stencil = ##f
		}
	}
\include \incmidi
	\header {
		piece = \pPiece
	}
}
