\version "2.20.0"

theFirstViolins =  \relative d' {
	\clef "treble"
	\key g \minor
	
	r1*3/4
	R1*3/4*11
	
	\noDynamic b-flat2.\pp_\markup { \dynamic pp con sordini }
	c
	b-flat
	c
	b-flat
	a
	g
	R1*3/4
	r4 d'2^>\p~
	d8[ d( e g f-sharp d])
	g[( f-sharp g a] b-flat4)
	a2.
	r4 d,2~
	d8[ d(\< e g f-sharp d])\!
	g4\< < d b-flat' > < f-sharp d' >\!
	< g d' > r r
	f-sharp( g) r
	f!( e-flat) r
	g2\pp r4
	g2 r4
	r4 d2
	b-flat2.\pp
	c
	b-flat
	c
	b-flat8[ e-flat'\p( d g, b-flat) e-flat](
	d[ g, b-flat) c( b-flat a-flat])
	r8 g4\pp g g8~
	g8 g4 g g8
	a-flat8->[( b-flat]) r g4 g8
	a-flat8->[( b-flat]) r e-flat, r f
	r e-flat[( d c]) r d
	f4 f2
	r8 g4\< g g8
	r g4 g g8\!
	a-flat2._\markup { \italic piu \dynamic f }
	a-flat4( g2)
	f8\pp[( e-flat]) d4( d-flat)
	c2\< d4\!
	f2\p\< f4
	f e-flat\! r
	
	R1*3/4*5
	
	f2.\p
	f-sharp2( d4)
	g2._\markup { \dynamic p \italic cresc.}
	< c, a-flat' >2 < e-flat b-flat' >4
	e-flat4_\markup { \italic piu \dynamic f } f2
	<< { g2. } { s4.\> s4 s8\! } >>
	c,8\p[( d]) e-flat4 f
	c8[( d]) e-flat4 f
	c\< c-sharp2\!
	d4 r r
	R1*3/4
	
	\set Staff.midiInstrument = #"pizzicato strings"
	r4 b-flat\p^\markup {pizz.} b-flat
	r c c
	r b-flat b-flat
	r c c
	r b-flat b-flat
	r d d
	r c c-sharp
	d8 r r4 r
	
	\set Staff.midiInstrument = #"string ensemble 1"
	d2\pp^arco d4
	d2 d4
	d2 d4
	d2 d4
	d2 d4
	d2 d4
	e-flat8\< r f r f-sharp\! r
	g r r4 r
	f-sharp4\mf( g) r4
	f!4( e-flat) r
	g2_\markup { \dynamic p \italic cresc. } r4
	g2 r4
	< d d' >2.\mf~
	< d d' >8 r r4 r
	R1*3/4
	e-flat2\p r4
	b-flat'2.(
	a4) r r\fermata
	
	R1*3/4*8
	
	b-flat4\mf b-flat8[( a]) b-flat4~
	b-flat2 r4
	< f b >2.
	R1*3/4
	b4 b8[( a-sharp] b4)~
	b2 r4
	< f c' >2.
	R1*3/4
	d-flat'4 d-flat8[(_\markup { \italic dim. } c] d-flat4)
	R1*3/4
	d!4\p d8[( c-sharp] d4)
	R1*3/4
	r4 r g-sharp,\pp
	
	R1*3/4*2
	r1*3/4\fermata
}
