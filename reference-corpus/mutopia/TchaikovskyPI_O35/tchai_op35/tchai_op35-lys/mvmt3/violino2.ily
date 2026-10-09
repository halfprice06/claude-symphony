\version "2.20.0"

theSecondViolins =  \relative d'' {
	\clef "treble"
	\key d \major
	\time 2/4
	
	< a a' >8\ff[ a16( g-sharp] a8)[ a,]
	b-flat2
	b-flat'
	b-flat,4 a8 r
	< a' a' >8[ a16( g-sharp] a8)[ a,]
	b-flat4 b
	c-sharp d
	c-sharp8 r r4
	
	R1*2/4*2
	
	g'8-.\f[ g16( f-sharp] g8)[ g,-.]
	a-sharp4~ a-sharp8 r
	
	R1*2/4*3
	
	r4 < e' a e' >8\ff r
	
	R1*2/4*36
	
	r8 a,\p r g-sharp
	r a r a
	r a r a
	r c-sharp a r
	< b f-sharp' >\f r r4
	< b g' >8_\markup { \italic dim. } r r4
	< b g-sharp' >8 r g' r
	r c-sharp, r c-sharp
	d\p r d r
	c-sharp r a r
	a\< r g r
	a r a\! r
	f'8\f r r b-flat,\p
	a r r4
	
	R1*2/4*2
	
	d8\mf r r4
	e8_\markup { \italic dim. } r r4
	r8 b-flat\p\< r a
	r d r c-sharp\!
	d\mf r r4
	e8_\markup { \italic dim. } r r4
	r8 b-flat\p\< r a
	r g-sharp r a\!
	d\mf r r4
	e8_\markup { \italic dim. } r r4
	r8 b-flat\p r a
	r d r c-sharp
	b!2\mf
	c-sharp
	c-sharp2
	d
	c_\cr
	c4 f
	< b,! a-flat' >2
	< c a-flat' >4 g-sharp'
	g-sharp2\f
	< c-sharp, a' >8 r r4
	g-sharp'2
	< c-sharp, a' >8 r r4
	b2\mf
	b
	b4\< b
	d c-sharp\!
	
	\set Staff.midiInstrument = #"pizzicato strings"
	r8 b'^\markup {pizz.} r a
	r a r < e a >
	r g-sharp r g
	r d r c-sharp
	< a d >8\p r r4
	g'8 r r4
	g8 r r4
	g8 r d r
	< b' f-sharp' >\f r r4
	< e, b' e >8\mf r r4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	e8^arco r < e a > r
	< b f-sharp' > r < c-sharp f-sharp > r
	< b f-sharp' >\f r r g-sharp'
	e r e r
	f-sharp-.\p[\< g!-.] g-.[ g-.]
	g-.[ g-.] f-sharp4^>\!
	a8\f r r g-sharp
	a r g!-.\p[ f-sharp-.]
	e-.[\< e-. e-. e-.]
	d-.[ c-sharp-.]\! d-.\f r
	
	\set Staff.midiInstrument = #"pizzicato strings"
	b\mf^\markup {pizz.} r r4
	b8 r b[ d]
	b r d r
	c-sharp r r4
	b8 r r4
	b8 r b[ d]
	b r d r
	c-sharp r r4
	< b f-sharp' d' >8\f r r4
	g'8 r r4
	< b, f-sharp' d' >8 r r4
	g'8 r r4
	< b, f-sharp' d' >8 r r4
	< b f-sharp' d' >8 r r4
	e8 r < b f-sharp' d' > r
	< b g' d' > r < d d' > r
	b r r4
	b8 r r4
	c-sharp8 r r4
	d8 r d r
	d r r4
	d8 r r4
	d8\> r d\! r
	d\p r r4
	
	R1*2/4*4
	
	%%% POCO MENO MOSSO %%%
	
	\set Staff.midiInstrument = #"string ensemble 1"
	< a e' c-sharp' e >8\ff^arco r r4
	
	R1*2/4*10
	
	r4 g-sharp8\pp r
	r4 g-sharp8 r
	r4 g-sharp8 r
	r4 a8 r
	r4 a8 r
	r4 g-sharp8 r
	r4 g-sharp8 r
	r4 a8 r
	
	R1*2/4*8
	
	r4 d'8-.\p[~ d-.]
	d4-> a-sharp8[( b])
	e,4 f-sharp8-.[( g-sharp-.])
	a4-> c-sharp8[( b])
	a4 c-sharp8-.[~ c-sharp-.]
	d4-> a-sharp8[( b])
	e,4 f-sharp8-.[( g-sharp-.])
	a4-> c-sharp8[( b])
	a4 r
	g-sharp,2\mf~
	g-sharp4 g-sharp8-.[ d'-.]
	c-sharp4.( b8
	a) r r4
	g-sharp2~
	g-sharp4 g-sharp8-.[ d'-.]
	c-sharp4.( b8
	a) r r4
	
	R1*2/4*2
	
	r4 g-sharp'4\mf
	f-sharp8[( g-sharp] a4)
	b g-sharp
	e8[( d]) d4
	b'8[ g-sharp e e]
	e8 r r4
	r8 f-sharp\p r4
	r8 f-sharp r4
	r8 b, r4
	r8 c-sharp r4
	r8 f-sharp r4
	r8 f-sharp r4
	r8 b, r4
	r8 c-sharp r4
	r8 a r4
	r8 a r4
	r8 f-sharp' r b,
	r b r4
	r8 e4.
	r8 e r f-sharpsharp
	r g-sharp r e
	r e r4
	r8 e4.
	r8 e r f-sharpsharp
	r g-sharp r e
	r e r4
	r8 d!4.\pp
	r8 b4.
	r8 b4.
	r8 b4.
	r8 c-sharp4.
	r8 a4.
	r8 a-sharp4.
	r8 a-sharp4.
	r8 b-flat4.~
	b-flat2
	r8 b-flat4.
	r8 a-sharp4.
	r8 b4.~
	b2
	r8 g4.~
	g8 r r4
	r8 g4.~
	g8 r r4
	
	R1*2/4*8
	
	r8 a\p r g-sharp
	r a r a
	r a r a
	r c-sharp a r
	< b f-sharp' >\f r r4
	< b g' >8_\markup { \italic dim. } r r4
	< b g-sharp' >8 r g' r
	r c-sharp, r c-sharp
	d\p r d r
	c-sharp r a r
	a\< r g r
	a r a\! r
	f'8\f r r b-flat,\p
	a r r4
	
	R1*2/4*2
	
	d8\mf r r4
	e8_\markup { \italic dim. } r r4
	r8 b-flat\p\< r a
	r d r c-sharp\!
	d\mf r r4
	e8_\markup { \italic dim. } r r4
	r8 b-flat\p\< r a
	r g-sharp r a\!
	d\mf r r4
	e8_\markup { \italic dim. } r r4
	r8 b-flat\p\< r a
	r d r c-sharp\!
	b!2\mf
	c-sharp
	c-sharp2
	d
	c_\cr
	c4 f
	< b,! a-flat' >2
	< c a-flat' >4 g-sharp'
	g-sharp2\f
	< c-sharp, a' >8 r r4
	g-sharp'2
	< c-sharp, a' >8 r r4
	b2\f~
	b4 r
	r8 b[ b b]
	b[ b] b r
	b2~
	b4 r
	r8 b[ b b]
	b[ b] b r
	b2\f
	c2
	d
	e4~ e8 r
	R1*2/4
	
	\set Staff.midiInstrument = #"pizzicato strings"
	r4 r8 g'8\p^\markup {pizz.}
	g[ f e d]
	c[ c b! b-flat]
	c r r4
	r4 r8 g'
	g[ f e d]
	c-sharp![ c-sharp d e]
	f r r4
	r4 r8 e
	e[ d] c-sharp![ g-sharp]
	a[ a a < g! a >]
	< f a > r r4
	r4 r8 e'
	e[ d c-sharp g-sharp]
	a[ f g! d]
	c-sharp[ g-sharp a] r
	R1*2/4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	< d b-flat' f' >8\ff[^arco b-flat'16( a] b-flat8)[ < d, b-flat' >]
	< a' f' >[ < a f' >] < b-flat g-flat' > r
	
	R1*2/4*2
	
	< d, b-flat' f' >8[ b-flat'16( a] b-flat8)[ < d, b-flat' >]
	e-flat'[ e-flat] < b-flat g'! > r
	
	R1*2/4*2
	
	< e-flat, b-flat' g' >8[ b-flat'16( a] b-flat8)[ < e-flat, b-flat' >]
	< e-flat c' >[ < e-flat c' >] < e-flat b-flat' g' >8 r
	
	R1*2/4*2
	
	< e c' e >8[ e'16( d-sharp] e8)[ < c e >]
	< d b' >8[ < d b' >] < c e > r
	r4 r8 < c e >
	< d b' >[ < d b' >] < c e > r
	r4 r8 < c e >
	< d b' >[ < d b' >] < c e >[ < c e >]
	< d b' >[ < d b' >] < c e >[ < c e >]
	< d b' >[ < d b' >] < c e >[ < c e >]
	e-flat[ e-flat,\p] r e-flat_\cr
	r e-flat r e-flat
	r e-flat\< r e-flat
	r e-flat[ e-flat e-flat]\!
	e-flat\f[ e-flat\p] r e-flat\<
	r e-flat r e-flat
	r e-flat r e-flat
	r e-flat[ e-flat e-flat]\!
	e-flat\f[ e-flat\p]\< r e-flat
	r e-flat[ e-flat e-flat]\!
	f\f[ f\p] r f\<
	r f[ f f]\!
	f-sharp!8\f r r4
	
	R1*2/4*3
	
	< g, d' b' g' >8\ff r r4
	
	R1*2/4*10
	
	r4 c8\pp r
	r4 c8 r
	r4 c8 r
	r4 b8 r
	r4 b8 r
	r4 c8 r
	r4 c8 r
	r4 b8 r
	
	R1*2/4*8
	
	\set Staff.midiInstrument = #"pizzicato strings"
	r4 r8 < f-sharp c' >8\mf^\markup {pizz.}
	r < f-sharp' c' > r < f-sharp c' >
	r < f-sharp c' > r < f-sharp c' >
	r < b, g' d' > r < b g' d' >
	r < b g' d' > r < b g' d' >
	r < f-sharp' c' > r < f-sharp c' >
	r < f-sharp c' > r < f-sharp c' >
	r < b, g' d' > r < b g' d' >
	r < b g' d' > r4
	R1*2/4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	r4 r8 c8-.\mf^arco
	b4.( a8
	g) r r4
	R1*2/4
	r4 r8 c8
	b4.( a8
	g4) r
	
	R1*2/4*8
	
	r8 b8\p r4
	r8 c r4
	r8 a-sharp r4
	r8 a-sharp r4
	r8 b r4
	r8 c r4
	r8 b-flat r4
	r8 a r4
	r8 a r4
	r8 b r4
	r8 e-sharp r4
	r8 f-sharp r4
	r8 a, r4
	r8 b r4
	r8 e-sharp r4
	r8 f-sharp r4
	r8 a,\pp r4
	r8 a r4
	r8 c r4
	r8 c r4
	r8 c r4
	r8 c r4
	r8 c r4
	r8 d r4
	r8 a r4
	r8 a r4
	r8 c r4
	r8 c r4
	r8 c r4
	r8 c r4
	r8 c r4
	r8 d\< r4
	r8 d r4
	r8 d-sharp r4
	r8 e\! r4
	
	R1*2/4*24
	
	r8 a,\p r g-sharp
	r a r a
	r a r a
	r c-sharp a r
	< b f-sharp' >\f r r4
	< b g' >8_\markup { \italic dim. } r r4
	< b g-sharp' >8 r g' r
	r c-sharp, r c-sharp
	d\p r d r
	c-sharp r a r
	a\< r g r
	a r a\! r
	f'8\f r r b-flat,\p
	a r r4
	
	R1*2/4*2
	
	d8\mf r r4
	e8_\markup { \italic dim. } r r4
	r8 b-flat\p\< r a
	r d r c-sharp\!
	d\mf r r4
	e8_\markup { \italic dim. } r r4
	r8 b-flat\p\< r a
	r g-sharp r a\!
	d\mf r r4
	e8_\markup { \italic dim. } r r4
	r8 b-flat\p r a
	r d r c-sharp
	b!2\mf
	c-sharp
	c-sharp2
	d
	c_\cr
	c4 f
	< b,! a-flat' >2
	< c a-flat' >4 g-sharp'
	g-sharp2\f
	< c-sharp, a' >8 r r4
	g-sharp'2
	< c-sharp, a' >8 r r4
	b2\mf
	b
	b4\< b
	d c-sharp\!
	
	\set Staff.midiInstrument = #"pizzicato strings"
	r8 b'^\markup {pizz.} r a
	r a r < e a >
	r g-sharp r g
	r d r c-sharp
	< a d >8\p r r4
	g'8 r r4
	g8 r r4
	g8 r d r
	< b' f-sharp' >\f r r4
	< e, b' e >8\mf r r4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	e8^arco r < e a > r
	< b f-sharp' > r < c-sharp f-sharp > r
	< b f-sharp' >\f r r g-sharp'
	e r e r
	f-sharp-.\p[\< g!-.] g-.[ g-.]
	g-.[ g-.] f-sharp4^>\!
	a8\f r r g-sharp
	a r g!-.\p[ f-sharp-.]
	e-.[\< e-. e-. e-.]
	d-.[ c-sharp-.]\! d-.\f r
	
	\set Staff.midiInstrument = #"pizzicato strings"
	b\mf^\markup {pizz.} r r4
	b8 r b[ d]
	b r d r
	c-sharp r r4
	b8 r r4
	b8 r b[ d]
	b r d r
	c-sharp r r4
	< b f-sharp' d' >8\f r r4
	g'8 r r4
	< b, f-sharp' d' >8 r r4
	g'8 r r4
	< b, f-sharp' d' >8 r r4
	< b f-sharp' d' >8 r r4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	< e b' e >8^arco r < b f-sharp' d' > r
	< b g' d' > r < g-sharp' e-sharp' > r
	< d a' f-sharp' >[ d16(^\markup { \dynamic p \italic {poco a poco cresc.}}
		c-sharp] d8)[ d'-.]
	c,8-.[ c16( b] c8)[ c']
	b,16[ c-sharp! d-sharp f-sharp] g-sharp[ a-sharp b c-sharp]
	d-sharp[ e f-sharp b,] r4
	e,8-.[^\cr e16( d-sharp] e8)[ e'-.]
	d,!8[ d16( c-sharp] d8)[ d'-.]
	c-sharp,16[ d-sharp e-sharp g-sharp] a[ b c-sharp d-sharp]
	e-sharp[ f-sharp g-sharp c-sharp,] r4
	f-sharp,8-.[^\markup { \italic {sempre cresc.}} f-sharp16( e-sharp] f-sharp)[ c-sharp d-sharp e]
	f-sharp[ g-sharp a b] c-sharp[ b a8]
	r8 g-sharp16[( f-sharpsharp] g-sharp)[ b, d e!]
	f[ g! g-sharp b] f'[ d b g]
	r8 b-flat16[( a] b-flat)[ e, g! a]
	b-flat[ b c-sharp e] g[ e c-sharp b-flat]
	r8 b!16[( a-sharp] b)[ d, f g-sharp]
	b[ c-sharp d f] g-sharp[ f-sharp d b]
	c-sharp\f[ d e d] c-sharp[ a e g!]
	c-sharp[ d e d] c-sharp[ a e e']
	e[ f-sharp g f-sharp] e[ a, e a]
	e'[ f-sharp g f-sharp] e[ a, e a]
	c-sharp[ d e d] c-sharp[ b a b]
	c-sharp[ b c-sharp d] e[ d-sharp e f-sharp]
	e[ f-sharp g f-sharp] e[ d! c-sharp d]
	e[ d-sharp e f-sharp] g[ a b c-sharp]
	d8-.\ff[ d,16( c-sharp] d8)[ < a f-sharp' >]
	< b g' >[ < b g' >] < a f-sharp' > r
	
	R1*2/4*2
	
	< b, f-sharp' d' >8-.[ d'16( c-sharp] d8)[ b]
	< c-sharp e >8[ < c-sharp e >] < d, d' > r
	
	R1*2/4*2
	
	< d d' >8[ d'16( c-sharp] d8)[ < d, b' >]
	< c' e >[ < c e >] < d, d' > r
	
	R1*2/4*2
	
	< e b' e >8-.[ e'16( d-sharp] e8)[ < b e >]
	< c e >[ < c e >] < e, b' e > r
	
	R1*2/4*2
	
	< e b' e >8-.[ e'16( d-sharp] e8)[ < b e >]
	< c e >[ < c e >] < e, b' e > r
	
	R1*2/4*2
	
	< e b' e >8-.[ e'16( d-sharp] e8)[ < b e >]
	R1*2/4
	< e, b' e >8-.[ e'16( d-sharp] e8)[ < b e >]
	R1*2/4
	< b e >8[ < b e >] r4
	< b e >8[ < b e >] r4
	< b-flat e >8[ < b-flat e >] r4
	< a e' >8[ < a e' >] r4
	< a f-sharp' >8[ < a f-sharp' >] r4
	g'8[ d] r4
	g-sharp8[ d] r8_\markup { \dynamic p \italic cresc.} < d, d' >
	r < d d' > r < d d' >
	r < d d' > r < d d' >
	r < d d' > r < d d' >
	< d d' >\f[ c-sharp' b f-sharp]
	f-sharp[ b] < b e >[ b]
	b[ b] < e, a >[ d']
	c-sharp[ e, f-sharp g]
	a r b-flat,\f[ b-flat]
	b-flat2(
	g4) a
	< a g' >4 < g g' >
	< f-sharp' a >8 r b-flat,[ b-flat]
	b-flat2(
	g4) a
	< a g' >4 < g g' >
	< f-sharp' a >8 r a-sharp r
	< d, b' > r f-sharp r
	g8 r g4->~
	g8 r < a, g' > r
	< f-sharp' a > r a-sharp r
	< d, b' > r f-sharp r
	g r g4->~
	g8 r < a, g' > r
	< f-sharp' a >\f r < e a > r
	< f-sharp a > r < e a > r
	< f-sharp a > r < e a > r
	< f-sharp a > r < e a > r
	< f-sharp a > r d'4:16
	d: c-sharp8:[ b:]
	a r d4:
	d4: c-sharp8:[ c-sharp:]
	a8:[ d: c-sharp: b:]
	a8:[ d: c-sharp: b:]
	< d, a' > r r4
	< d d' >8 r r4
	< d b' g-sharp' >8 r r4
	< a' g'! >8 r r4
	< a f-sharp' >8:\ff[ < a e' >: < a f-sharp' >: < a e' >:]
	< a f-sharp' >8:[ < a e' >: < a f-sharp' >: < a e' >:]
	< a f-sharp' >8:[ < a e' >: < a f-sharp' >: < a e' >:]
	< a f-sharp' >8:[ < a e' >: < a f-sharp' >: < a e' >:]
	< a f-sharp' >8-.[ d16( c-sharp] d8)[ < a f-sharp' >]
	< a e' >[ e'] d[ f-sharp]
	a r r4
	< f-sharp, d' a' >8 r r4\fermata
}
