\version "2.20.0"

theSecondViolins =  \relative d {
	\clef "treble"
	\time 3/4
	\key g \minor
	
	r1*3/4
	R1*3/4*11
	
	\noDynamic
	g2.\pp_\markup { \dynamic pp con sordini }
	g
	g
	g
	g
	
	R1*3/4*3
	
	b-flat4.( a8 g4)
	
	R1*3/4*3
	
	b-flat4.( a8 g4)
	R1*3/4
	e-flat'4\< f! < d c' >\!
	< d b-flat' > r r
	c( d) r
	d( e-flat) r
	g,2\pp r4
	g2 r4
	r4 d'( c)
	g2.\pp
	g
	g
	g
	g'8[ g-.\p( g-. g-. g-. g-.])
	g-.[( g-. g-.) d( e-flat f])
	r e-flat4\pp e-flat e-flat8~
	e-flat e-flat4 e-flat e-flat8
	d4 r8 e-flat4 e-flat8
	d4 r8 d-flat r c
	r c4 c8 r b
	c4 b-flat!2
	r8 e-flat4\< e-flat e-flat8
	r8 e4 e e8\!
	f2._\markup { \italic piu \dynamic f }
	f4( g2)
	a-flat,4 a-flat( b-flat
	c8)\< r r4 b\!
	c2\p\< c-flat4
	b-flat b-flat\! r
	
	R1*3/4*5
	
	c2.\p
	c
	d_\markup { \dynamic p \italic cresc. }
	f2 < g, g' >4
	a-flat2._\markup { \italic piu \dynamic f }
	<< { < g e-flat' >2. } { s4.\> s4 s8\! } >>
	c4\p c c
	c c c
	<< { g2. } { s4.\< s4 s8\! } >>
	a4 r r
	R1*3/4
	
	\set Staff.midiInstrument = #"pizzicato strings"
	r4 g\p^\markup {pizz.} g
	r a a
	r g g
	r a a
	r g g
	r a a
	r g g
	a8 r r4 r
	
	\set Staff.midiInstrument = #"string ensemble 1"
	b-flat2\pp^arco b-flat4
	c2 c4
	b-flat2 b-flat4
	c2 c4
	b-flat2 b-flat4
	a2 a4
	c8\< r d r d\! r
	d r r4 r
	c4\mf( d) r
	d( e-flat) r
	g,2_\markup { \dynamic p \italic cresc. } r4
	g2 r4
	b-flat'2.\mf~
	b-flat8 r r4 r
	R1*3/4
	b-flat,2\p r4
	g'2.~
	g4 r r\fermata
	
	R1*3/4*8
	
	< g, g' >2.\mf~
	< g g' >2 r4
	b2.
	R1*3/4
	< b f' >2.~
	< b f' >2 r4
	c2.
	R1*3/4
	d-flat4 d-flat8[(^\markup { \italic dim. } c] d-flat4)
	R1*3/4
	d!4 d8[( c-sharp] d4)
	R1*3/4
	r4 r e\pp
	r r g-sharp,
	R1*3/4
	r1*3/4^\fermata

}
