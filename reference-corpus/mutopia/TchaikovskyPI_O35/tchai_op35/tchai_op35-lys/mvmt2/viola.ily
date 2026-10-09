\version "2.20.0"
theViolas =  \relative d {
	\clef "alto"
	\key g \minor
	
	R1*3/4*12
	
	\noDynamic
	g2.\pp_\markup { \dynamic pp {con sordini} }
	a
	g
	a
	g
	f-sharp
	e-flat
	f-sharp
	r8 d\p[( e f-sharp] g[ e])
	f-sharp4( g a)
	b-flat8[( a b-flat c] d4)
	d2.
	r8 d,[( e f-sharp g e])
	f-sharp4(\< g a)\!
	< c, g' >\< < d b-flat' > a'\!
	g r r
	a( b-flat) r
	a-flat( g) r
	g8\pp[( a] b-flat4) r
	g8[( a] b-flat4) r
	r b-flat( a)
	g2.\pp
	a
	g
	a
	d8[ c\p( d e-flat d) c](
	d[ e-flat d) b-flat( c d])
	r b-flat4\pp b-flat b-flat8~
	b-flat b-flat4 b-flat b-flat8
	c-flat8^>[( b-flat]) r b-flat4 b-flat8
	c-flat8^>[( b-flat]) r g r a-flat
	r a-flat4 a-flat8 r g
	a-flat4 a-flat2
	r8 b-flat4\< b-flat b-flat8
	r b-flat4 b-flat b-flat8\!
	c2(_\markup { \italic piu \dynamic f } c-flat4)
	b-flat2.(
	a-flat8\pp) r f4( e-flat8) r
	a-flat4\< d,2\!
	a-flat'2\p\< a-flat4
	a-flat g\! r
	
	R1*3/4*5
	
	a-flat2.\p
	a!
	b_\markup { \dynamic p \italic cresc. }
	a-flat2 b-flat4
	c2(_\markup { \italic piu \dynamic f } c-flat4)
	<< b-flat2. { s4.\> s4 s8\! } >>
	a-flat4\p g f
	a-flat g f
	e-flat2\< e4\!
	f-sharp r r
	R1*3/4
	
	\set Staff.midiInstrument = #"pizzicato strings"
	r4 d^\markup {pizz.} d
	r d d
	r d d
	r d d
	r d d
	r d d
	r e-flat e
	f-sharp8 r r4 r
	
	\set Staff.midiInstrument = #"string ensemble 1"
	g2\pp^arco g4
	a2 a4
	g2 g4
	a2 a4
	g2 g4
	f-sharp2 f-sharp4
	g8\< r b-flat r c\! r
	b-flat r r4 r
	a4\mf( b-flat) r
	a-flat( g) r
	g8[(_\markup { \dynamic p \italic cresc. } a] b-flat4) r
	g8[( a] b-flat4) r
	g'2.\mf~
	g8 r r4 r
	R1*3/4
	g,2\p r4
	e-flat'2.~
	e-flat4 r r4\fermata
	
	R1*3/4*8
	
	c-sharp2.\mf~
	c-sharp2 r4
	a-flat4 a-flat8[( g] a-flat4)
	R1*3/4
	a-flat2.~
	a-flat2 r4
	a-flat4 a-flat8[( g] a-flat4)
	R1*3/4
	f2.
	R1*3/4
	< e b-flat' >2.
	R1*3/4
	r4 r b-flat'\pp
	r r e,
	R1*3/4
	r1*3/4\fermata
}
