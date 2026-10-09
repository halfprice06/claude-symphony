\version "2.20.0"

theBass =  \relative d {
	\clef "bass"
	\key g \minor
	
	r1*3/4
	R1*3/4*36
	
	g8\pp[ a\p( b-flat c g) a](
	b-flat[ c g) a-flat( g f]
	e-flat) r r4 r
	
	R1*3/4*3
	
	r4 r8 d\pp( g) r
	f[( e-flat d c] b-flat4)
	e-flat8\< r r4 r
	d-flat c2\!
	f2._\markup { \italic piu \dynamic f }
	r4 r c'\pp
	f, b-flat,( e-flat
	a-flat8) r r4 r
	f2\p\< e-flat4
	d e-flat\! r
	
	R1*3/4*9
	
	a-flat2._\markup { \italic piu \dynamic f }
	<< { e-flat2. } { s4.\> s4 s8\! } >>
	f4\p e-flat d
	f e-flat d
	c\< b-flat a\!
	d r r
	R1*3/4
	
	\set Staff.midiInstrument = #"pizzicato strings"
	g,4\p^\markup {pizz.} r g
	g r g
	g r g
	g r g
	g r g
	d' r r
	a r a
	d8 r r4 r
	g,\pp r g
	g r g
	g r g
	g r g
	g r g
	d' r
		\set Staff.midiInstrument = #"string ensemble 1"
		d4^arco
	c8\< r b-flat r a r
	g r r4 r
	d'\mf( g) r
	b-flat,( e-flat) r
	e-flat(_\markup { \dynamic p \italic cresc. } d) r
	e-flat( d) r
	
	R1*3/4*28
	
	d8\pp[( c-sharp] d2)
	g-sharp,8[(_\markup { "" \raise #-3 \italic {Attacca subito}} f-sharpsharp] g-sharp2)^\fermata
}
