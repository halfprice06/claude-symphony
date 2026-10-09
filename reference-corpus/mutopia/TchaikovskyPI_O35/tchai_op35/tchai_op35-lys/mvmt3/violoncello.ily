\version "2.20.0"

theCellos =  \relative c {
	\clef "bass"
	\key d \major
	
	a8\ff[ a'16( g-sharp] a8)[ a,]
	b-flat2
	b-flat'
	b-flat,4 a8 r
	a8[ a'16( g-sharp] a8)[ a,]
	b-flat4 b
	c-sharp d
	c-sharp8 r r4
	
	R1*2/4*2
	
	r4 r8 g8-.\f
	f-sharp'8-.[ f-sharp16( e-sharp] f-sharp8)[ f-sharp,-.]
	g4 g-sharp
	a a-sharp
	b b-flat
	a < a e' a >8\ff r
	
	R1*2/4*36
	
	r8 d\p r d
	r d r d
	r d r d
	r d d r
	< d b' >8\f r r4
	d8_\markup { \italic dim. } r r4
	d8 r < d a' > r
	r < d a' > r < d a' >
	f-sharp\p r f r
	e r e r
	c-sharp\< r b r
	a r a\! r
	d\f r r d\p
	e r r4
	R1*2/4
	r4 r8 a
	b-flat\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 g\p\< r f
	r e r a\!
	b-flat\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 g\p\< r f
	r e r a\!
	b-flat\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 g\p r f
	r e r a
	R1*2/4
	e2\mf
	f-sharp
	f
	e_\cr
	e-flat4 d
	d-flat2
	c4 b
	b-flat( b-flat')
	a8 r r4
	b-flat,( b-flat')
	a8 r r4
	
	R1*2/4*2
	
	f-sharp4\< f
	e a,\!
	
	R1*2/4*3
	
	d16\f[( c-sharp d8]) a16[( g-sharp a8])
	d8\p r r4
	
	\set Staff.midiInstrument = #"pizzicato strings"
	d8^\markup {pizz.} r r4
	d8 r r4
	d8 r d r
	< d b' >\f r r4
	< d b' >8\mf r r4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	< d b' >8^arco r < d a' > r
	d r f-sharp r
	b\f r r e,
	a r g r
	f-sharp-.\p[\< e-. d-. c-sharp-.]
	b[ a] d4->\!
	f-sharp8\f r r e
	a r e'\p[ d]
	c-sharp-.[\< b-. a-. g-.]
	f-sharp-.[ e-.]\! d-.\f r
	
	\set Staff.midiInstrument = #"pizzicato strings"
	b8\mf[^\markup {pizz.} a-sharp b d]
	b8 r b r
	b r f-sharp' r
	e r r4
	b8[ a-sharp b d]
	b8 r b r
	b r f-sharp' r
	e r r4
	b'8\f r r4
	g8 r r4
	b8 r r4
	g8 r r4
	b8 r r4
	a8 r r4
	g-sharp8 r f-sharp r
	f r e r
	d-sharp r r4
	d!8 r r4
	c-sharp8 r r4
	b8 r b-flat r
	a r r4
	a-flat8 r r4
	g8\> r f-sharp\! r
	e\p r r4
	
	R1*2/4*4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	< a e' a >8\ff^arco r < a e' >4\>
	< a e' > < a e' >
	< a e' > < a e' >
	< a e' > < a e' >\p\!
	< a e' > < a e' >
	< a e' > < a e' >
	< a e' > < a e' >
	< a e' > < a e' >
	< a e' > < a e' >
	< a e' > < a e' >
	< a e' > < a e' >
	< a e' >8 r a\pp r
	r4 a8 r
	r4 a8 r
	r4 a8 r
	r4 a8 r
	r4 a8 r
	r4 a8 r
	r4 a8 r
	
	R1*2/4*8
	
	r4 < a e' >4\p~
	< a e' > < a e' >~
	< a e' > < a e' >~
	< a e' > < a e' >~
	< a e' > < a e' >~
	< a e' > < a e' >~
	< a e' > < a e' >~
	< a e' > < a e' >~
	< a e' >8[ < a e' >] r < e a >\mf
	r < e a > r < e a >
	r < e a > r < e a >
	r < e a > r < e a >
	r < e a > r < e a >
	r < e a > r < e a >
	r < e a > r < e a >
	r < e a > r < e a >
	r a f-sharp'\mf[ f-sharp]
	f-sharp4 e8[ d]
	c-sharp[( b]) f-sharp'[ f-sharp]
	f-sharp4 e8[ d]
	c-sharp[( b]) a[ a']
	f-sharp4 e8[ d]
	c-sharp[( b]) f-sharp'[ f-sharp]
	e[ d c-sharp b]
	a8 r r4
	f-sharp'8\p r r4
	f-sharp8 r r4
	f-sharp8 r r4
	f-sharp8 r r4
	f-sharp8 r r4
	f-sharp8 r r4
	f-sharp8 r r4
	f-sharp8 r r4
	c8 r r4
	b8 r r4
	e,2~
	e4 r
	e'2~
	e4 c-sharp8-.[(_\markup { \dynamic p \italic espress. } d-sharp-.])
	e4 \grace { d-sharp16[( e] } d-sharp8[ c-sharp])
	\grace { c16[( d!] } c8[ b]) r4
	e2~
	e4 c-sharp8[( d-sharp])
	e4 \grace { d-sharp16[( e] } d-sharp8[ c-sharp])
	\grace { c16[( d!] } c8[ b]) r4
	
	R1*2/4*7
	
	\set Staff.midiInstrument = #"pizzicato strings"
	e8^\markup {pizz.} r r4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	d2~^arco
	d8 r r4
	d8 r r4
	c-sharp8 r r4
	b8 r r4
	R1*2/4
	r8 b-flat4.~
	b-flat8 r r4
	r8 a4.~
	a8 r r4
	
	R1*2/4*8
	
	r8 d\p r d
	r d r d
	r d r d
	r d d r
	< d b' >8\f r r4
	d8_\markup { \italic dim. } r r4
	d8 r < d a' > r
	r < d a' > r < d a' >
	f-sharp\p r f r
	e r e r
	c-sharp\< r b r
	a r a\! r
	d\f r r d\p
	e r r4
	R1*2/4
	r4 r8 a\mf
	b-flat r r4
	a8_\markup { \italic dim. } r r4
	r8 g\p\< r f
	r e r a\!
	b-flat\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 g\p\< r f
	r e r a\!
	b-flat\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 g\p\< r f
	r e r a\!
	R1*2/4
	e2\mf
	f-sharp
	f
	e_\cr
	e-flat4 d
	d-flat2
	c4 b
	b-flat\f( b-flat')
	a8 r r4
	b-flat,( b-flat')
	a8 r r4
	g,2\f~
	g4 r
	r8 a[ g a]
	g[ a] g r
	g-sharp2~
	g-sharp4 r
	r8 a[ g-sharp a]
	g-sharp[ a] g-sharp r
	g-sharp2\f
	a
	b
	c4~ c8 r
	
	R1*2/4*17
	
	\set Staff.midiInstrument = #"pizzicato strings"
	e8[^\markup {pizz.} d] r4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	b-flat8\ff^arco r b-flat[ b-flat]
	f'[ f] e r
	
	R1*2/4*2
	
	b-flat8 r b-flat[ b-flat]
	f'[ f-sharp] g r
	
	R1*2/4*2
	
	e-flat8 r e-flat[ e-flat]
	e-flat[ e-flat] e-flat r
	
	R1*2/4*2
	
	g8 r g[ g]
	g[ g] g r
	r4 r8 g
	g[ g] g r
	r4 r8 g
	g[ g g g]
	g[ g g g]
	g[ g g g]
	f-sharp![ f-sharp\p] r f-sharp_\cr
	r8 f-sharp r f-sharp
	r f-sharp\< r f-sharp
	r f-sharp[ f-sharp f-sharp]\!
	f\f[ f\p] r f\<
	r f r f
	r f r f
	r f[ f f]\!
	e\f[ e\p]\< r e
	r e[ e e]\!
	e-flat\f[ e-flat\p] r e-flat\<
	r e-flat[ e-flat e-flat]\!
	d8\f r r4
	
	R1*2/4*3
	
	< g, d' b' >8\ff r < g d' >4\>
	< g d' > < g d' >
	< g d' > < g d' >
	< g d' > < g d' >\p\!
	< g d' > < g d' >
	< g d' > < g d' >
	< g d' > < g d' >
	< g d' > < g d' >
	< g d' > < g d' >
	< g d' > < g d' >
	< g d' > < g d' >
	< g d' >8 r < g d' >\pp r
	r4 < g d' >8 r
	r4 < g d' >8 r
	r4 < g d' >8 r
	r4 < g d' >8 r
	r4 < g d' >8 r
	r4 < g d' >8 r
	r4 < g d' >8 r
	r8 < g d' >\p[ < g d' > < g d' >]
	< g d' >[ < g d' > < g d' > < g d' >]
	< g d' >[ < g d' > < g d' > < g d' >]
	< g d' >[ < g d' > < g d' > < g d' >]
	< g d' >[ < g d' > < g d' > < g d' >]
	< g d' >[ < g d' > < g d' > < g d' >]
	< g d' >[ < g d' > < g d' > < g d' >]
	< g d' >[ < g d' > < g d' > < g d' >]
	< g d' >[ < g d' >] r
		\set Staff.midiInstrument = #"pizzicato strings"
		< g d' a' >8\mf^\markup {pizz.}
	r < g d' a' > r < g d' a' >
	r < g d' a' > r < g d' a' >
	r < g d' b' > r < g d' b' >
	r < g d' b' > r < g d' b' >
	r < g d' a' > r < g d' a' >
	r < g d' a' > r < g d' a' >
	r < g d' b' > r < g d' b' >
	r < g d' b' > r < d g >8\mf
	r < d g > r < d g >
	r < d g > r < d g >
	r < d g > r < d g >
	r < d g > r < d g >
	r < d g > r < d g >
	r < d g > r < d g >
	r < d g > r < d g >
	r < d g > r4
	
	R1*2/4*8	
	
	e8\p^\markup {pizz.} r r4
	g8 r r4
	a-sharp8 r r4
	a-sharp8 r r4
	e8 r r4
	g8 r r4
	b-flat8 r r4
	a8 r r4
	d8 r r4
	d8 r r4
	d8 r r4
	d8 r r4
	d8 r r4
	d8 r r4
	d8 r r4
	d8 r r4
	r8 c\pp r4
	r8 b r4
	r8 a r4
	r8 g r4
	r8 f-sharp r4
	r8 e r4
	r8 e-flat r4
	r8 d r4
	r8 c' r4
	r8 b r4
	r8 a r4
	r8 g r4
	r8 f-sharp r4
	r8 e r4
	r8 e-flat r4
	r8 d\< r4
	r8 c r4
	r8 b' r4
	r8 b-flat\! r4
	a2\pp~
	a
	a~
	a
	
	R1*2/4*20
	
	r8 d\p r d
	r d r d
	r d r d
	r d d r
	< d b' >8\f r r4
	d8_\markup { \italic dim. } r r4
	d8 r < d a' > r
	r < d a' > r < d a' >
	f-sharp\p r f r
	e r e r
	c-sharp\< r b r
	a r a\! r
	d\f r r d\p
	e r r4
	R1*2/4
	r4 r8 a
	b-flat\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 g\p\< r f
	r e r a\!
	b-flat\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 g\p\< r f
	r e r a\!
	b-flat\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 g\p r f
	r e r a
	R1*2/4
	e2\mf
	f-sharp
	f
	e_\cr
	e-flat4 d
	d-flat2
	c4 b
	b-flat( b-flat')
	a8 r r4
	b-flat,( b-flat')
	a8 r r4
	
	R1*2/4*2
	
	f-sharp4\< f
	e a,\!
	
	R1*2/4*3
	
	d16\f[( c-sharp d8]) a16[( g-sharp a8])
	d8\p r r4
	
	\set Staff.midiInstrument = #"pizzicato strings"
	d8^\markup {pizz.} r r4
	d8 r r4
	d8 r d r
	< d b' >\f r r4
	< d b' >8\mf r r4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	< d b' >8^arco r < d a' > r
	d r f-sharp r
	b\f r r e,
	a r g r
	f-sharp-.\p[\< e-. d-. c-sharp-.]
	b[ a] d4->\!
	f-sharp8\f r r e
	a r e'\p[ d]
	c-sharp-.[\< b-. a-. g-.]
	f-sharp-.[ e-.]\! d-.\f r
	
	\set Staff.midiInstrument = #"pizzicato strings"
	b8\mf[^\markup {pizz.} a-sharp b d]
	b8 r b r
	b r f-sharp' r
	e r r4
	b8[ a-sharp b d]
	b8 r b r
	b r f-sharp' r
	e r r4
	b'8\f r r4
	g8 r r4
	b8 r r4
	g8 r r4
	b8 r r4
	a8 r r4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	g8^arco r f-sharp r
	e r b r
	f-sharp'2\f\>
	e2\!_\markup { \dynamic pp \italic {poco a poco cresc.}}
	d-sharp4( c-sharp8[ b]
	a[ d-sharp]) r4
	g-sharp2^\cr
	f-sharp
	e-sharp4( d!8[ c-sharp]
	b[ e-sharp]) r4
	f-sharp2~^\markup { \italic {sempre cresc.}}
	f-sharp4 e-sharp8[ f-sharp]
	f2~
	f4 d8[ f]
	c-sharp'2~
	c-sharp4 c-sharp,8[ c-sharp']
	< d, b' >2~
	< d b' >4 < b d >8[ < d b' >]
	b-flat'4->\f( a)
	b-flat->( a)
	b-flat->( < g a >)
	b-flat->( < g a >)
	r8 < a, e' c-sharp' > r < a e' c-sharp' >
	r < a e' c-sharp' > r < a e' c-sharp' >
	r < a e' c-sharp' > r < a e' c-sharp' >
	r < a e' c-sharp' >[ < a e' c-sharp' > < a e' c-sharp' >]
	< d a' >\ff r < d a' >[ < d a' >]
	g[ g] < d a' > r
	
	R1*2/4*2
	
	< b f-sharp' d' >8 r b[ b]
	e[ e] b r
	
	R1*2/4*2
	
	g'8 r g[ g]
	c,[ c] g' r
	
	R1*2/4*2
	
	e8 r e[ e]
	a[ a] e r
	
	R1*2/4*2
	
	e8 r e[ e]
	a[ a] e r
	
	R1*2/4*2
	
	e8 r e[ e]
	R1*2/4
	e8 r e[ e]
	R1*2/4
	e8[ e] r4
	e8[ e] r4
	d8[ d] r4
	c-sharp8[ c-sharp] r4
	c8[ c] r4
	< b g' >8[ < b g' >] r4
	< b-flat g-sharp' >8[ < b-flat g-sharp' >] r_\markup { \dynamic p \italic cresc. } b-flat
	r b-flat r b-flat
	r b-flat r b-flat
	r b-flat r b-flat
	a\f[ a-sharp b c-sharp]
	d[ d-sharp] e[ f-sharp]
	g[ g-sharp a b]
	a[ g! f-sharp e]
	d r d\f[ d]
	d2~
	d4 c-sharp8->[ c-sharp->]
	c-sharp4-> b8->[ a->]
	d8-> r d8[ d]
	d2~
	d4 c-sharp8->[ c-sharp->]
	c-sharp4-> b8->[ a->]
	d8 r f-sharp r
	g r b r
	e, r d4->~
	d8 r c-sharp r
	d r f-sharp r
	g r b r
	e, r d4->~
	d8 r c-sharp r
	d\f r a r
	d r a r
	d r a r
	d r a r
	d[ f-sharp a a-sharp]
	b[ d a! g]
	f-sharp[ d a'! a-sharp]
	b[ d a! g]
	f-sharp[ b a g]
	f-sharp[ b a g]
	f-sharp r r4
	< f a >8 r r4
	e8 r r4
	a8 r r4
	d,8\ff[ a d a]
	d[ a d a]
	d[ a d a]
	d[ a d a]
	d8 r < d a' >[ < d a' >]
	a'[ a] d,[ f-sharp]
	a r r4
	< d,, a' f-sharp' d' >8 r r4\fermata
}
