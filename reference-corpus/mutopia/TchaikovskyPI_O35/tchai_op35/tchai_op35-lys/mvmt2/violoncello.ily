\version "2.20.0"

theCellos =  \relative c {
	\clef "bass"
	\key g \minor
	
	R1*3/4*17
	
	d2.\pp
	a2.
	d
	< g, d' >\p
	< g d' >
	g'2.~
	g8[ g( f-sharp e f-sharp d])
	< g, d' >2.
	<< { d'2. } { s4.\< s4 s8\! } >>
	c'4\< b-flat, < a d >\!
	< g d' > r r
	d'( g) r
	b-flat,( e-flat) r
	e-flat\pp( d) r
	e-flat( d) r
	r d2
	
	R1*3/4*4
	
	g8\pp[ a\p( b-flat c g) a](
	b-flat[ c g) a-flat( g f]
	e-flat) r r4 r
	e-flat8\pp r r4 r
	e-flat4~ e-flat8 r r4
	e-flat4 e-flat a-flat,~
	a-flat4.( d8) g,4
	f'8[( e-flat d c] b-flat4)
	e-flat8\< r r4 r
	d-flat4 c2\!
	f2._\markup { \italic piu \dynamic f }
	f4( e-flat e)
	f\pp b-flat,( e-flat!)
	a-flat,2\< g4\!
	f'2\p\< e-flat4
	d e-flat\! r
	
	R1*3/4*7
	
	g2._\markup { \dynamic p \italic cresc. }
	f2 e-flat4
	e-flat2._\markup { \italic piu \dynamic f }
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
	g,4\pp r g
	g r g
	g r g
	g r g
	g r g
	d' r
		\set Staff.midiInstrument = #"string ensemble 1"
		d^arco
	c8\< r b-flat r a\! r
	g r r16 g'16-.[ d-. b-flat-.] g8 r
	d'4\mf( g) r
	b-flat,( e-flat) r
	e-flat(_\markup { \dynamic p \italic cresc. } d) r
	e-flat( d) r
	
	R1*3/4*3
	
	c-sharp2\p r4
	
	R1*3/4
	r1*3/4\fermata
	
	R1*3/4*8
	
	e-flat2.\mf~
	e-flat2 r4
	d2.
	R1*3/4
	d-flat2.~
	d-flat2 r4
	c2.
	R1*3/4
	< b a-flat' >2.
	R1*3/4
	b-flat!2.
	
	R1*3/4*2
	
	r4 r b-flat\pp
	d8[( c-sharp] d2)
	g-sharp,8[( f-sharpsharp] g-sharp2\fermata)
}
