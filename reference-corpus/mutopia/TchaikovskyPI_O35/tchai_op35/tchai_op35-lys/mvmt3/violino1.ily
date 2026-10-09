\version "2.20.0"

theFirstViolins =  \relative d'' {
	\clef "treble"
	\key d \major
	
	< a a' >8\ff[ a'16( g-sharp] a8)[ a,,]
	b-flat2
	b-flat'2
	b-flat,4 a8 r
	< a' a' >8\ff[ a'16( g-sharp] a8)[ a,,]
	b-flat4 b
	c-sharp d
	c-sharp8 r r4
	
	R1*2/4*2
	
	g'8-.\f[ g16( f-sharp] g8)[ g,-.]
	a-sharp4~ a-sharp8 r
	
	R1*2/4*3
	
	r4 < a e' c-sharp' a' >8\ff r
	
	R1*2/4*36
	
	r8 a\p r b
	r c-sharp r c-sharp
	r c-sharp r c-sharp
	r < g e' > d' r
	< b' f-sharp' >\f r r4
	< b e >8_\markup { \italic dim. } r r4
	< b e >8 r < a e' > r
	r < e a > r < e a >
	a\p r g-sharp r
	g! r c-sharp, r
	a\< r b r
	c-sharp r d\! r
	b-flat'\f r r d,\p
	c-sharp r r4
	
	R1*2/4*2
	
	g-sharp'8\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 b-flat,\p\< r d
	r e r e\!
	g-sharp\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 b-flat,\p\< r d
	r d r c-sharp\!
	g-sharp'\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 b-flat,\p r d
	r e r e
	d2\mf
	e
	f-sharp
	< g, g' >
	g'_\cr
	< f a >4 b-flat
	b!2
	c4 < f, d' >
	< d d' >2\f
	c-sharp'8 r r4
	< d, d' >2
	c-sharp'8 r r4
	d,2\mf
	d
	d4\< d
	e e\!
	
	\set Staff.midiInstrument = #"pizzicato strings"
	r8 f'^\markup {pizz.} r < c-sharp e >
	r d r c-sharp
	r < d, b' > r < e a >
	r < f a > r < e a >
	< f-sharp! a >8\p r r4
	< e a >8 r r4
	< e a >8 r r4
	< e a >8 r < f-sharp a > r
	b'8\f r r4
	< e,, b' g' >8\mf r r4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	< b' e >8^\markup {arco} r c-sharp r
	b r a-sharp r
	< d, b' >\f r r b'
	a r a r
	a-sharp-.\p[ a-sharp-.] b-.[ a-.]
	e'-.[ a,-.] b[( a])
	d\f r r d
	c-sharp r a-.\p[ a-.]
	a-.[\< b-. c-sharp-. c-sharp-.]
	d-.[ a-.]\! a-.\f r
	
	\set Staff.midiInstrument = #"pizzicato strings"
	d,\mf^\markup {pizz.} r r4
	c-sharp8 r d r
	e[ g b d]
	e[ e,] r4
	d8 r r4
	c-sharp8 r d r
	e[ g b d]
	e[ e,] r4
	< d b' f-sharp' >8\f r r4
	< d b' >8 r r4
	< d b' f-sharp' >8 r r4
	< d b' >8 r r4
	< d b' f-sharp' >8 r r4
	< d b' f-sharp' >8 r r4
	< e b' e >8 r < d b' f-sharp' > r
	< d b' g' > r < d b' g-sharp' > r
	d-sharp r r4
	e8 r r4
	e-sharp8 r r4
	f8 r f r
	f r r4
	f8 r r4
	f8\> r f\! r
	g-sharp\p r r4
	
	R1*2/4*4
	
	%%% POCO MENO MOSSO %%%
	
	\set Staff.midiInstrument = #"string ensemble 1"
	< a, e' c-sharp' a' >8\ff^\markup {arco} r r4
	
	R1*2/4*10
	
	r4 d8\pp r8
	r4 d8 r
	r4 d8 r
	r4 c-sharp8 r
	r4 c-sharp8 r
	r4 d8 r
	r4 d8 r
	r4 c-sharp8 r
	
	R1*2/4*8
	
	r4 f-sharp'8\p-.[~ f-sharp-.]
	f-sharp4-> e8[( d])
	c-sharp[( b]) f-sharp'-.[~ f-sharp-.]
	f-sharp4-> e8[( d])
	c-sharp4 f-sharp8-.[~ f-sharp-.]
	f-sharp4-> e8[( d])
	c-sharp[( b]) f-sharp'-.[~ f-sharp-.]
	f-sharp4-> e8[( d])
	c-sharp4 r
	g-sharp2\mf~
	g-sharp4 g-sharp8-.[ d'-.]
	c-sharp4.( b8
	a) r r4
	g-sharp2~
	g-sharp4 g-sharp8-.[ d'-.]
	c-sharp4.( b8
	a) r r4
	r4 g-sharp4\mf~
	g-sharp8[ d] d'4~
	d g-sharp
	f-sharp8[( g-sharp] a4)
	d,4 b
	g-sharp8[( d]) b'4
	e8[ b a b]
	c-sharp r r4
	r8 a\p r4
	r8 g-sharp r4
	r8 f-sharp8 r4
	r8 f-sharp r4
	r8 a r4
	r8 g-sharp r4
	r8 f-sharp r4
	r8 f-sharp r4
	r8 f-sharp r4
	r8 f-sharp r4
	r8 a r d-sharp,
	r e r4
	r8 g-sharp4.
	r8 f-sharpsharp r a-sharp
	r b r f-sharpsharp
	r g-sharp r4
	r8 g-sharp4.
	r8 f-sharpsharp r a-sharp
	r b r f-sharpsharp
	r g-sharp r4
	r8 g-sharp4.\pp
	r8 f-sharp!4.
	r8 e-sharp4.
	r8 d!4.
	r8 e!4.
	r8 c-sharp4.
	r8 c-sharp4.
	r8 c-sharp4.
	r8 d4.~
	d2
	r8 d4.
	r8 e4.
	r8 e4.~
	e2
	r8 d4.~
	d8 r r4
	r8 c-sharp4.~
	c-sharp8 r r4
	
	R1*2/4*8
	
	r8 a\p r b
	r c-sharp r c-sharp
	r c-sharp r c-sharp
	r < g e' > d' r
	< b' f-sharp' >\f r r4
	< b e >8_\markup { \italic dim. } r r4
	< b e >8 r < a e' > r
	r < e a > r < e a >
	a\p r g-sharp r
	g! r c-sharp, r
	a\< r b r
	c-sharp r d\! r
	b-flat'\f r r d,\p
	c-sharp r r4
	
	R1*2/4*2
	
	g-sharp'8\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 b-flat,\p\< r d
	r e r e\!
	g-sharp\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 b-flat,\p\< r d
	r d r c-sharp\!
	g-sharp'\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 b-flat,\p\< r d
	r e r e\!
	d2\mf
	e
	f-sharp
	< g, g' >
	g'_\cr
	< f a >4 b-flat
	b!2
	c4 < f, d' >
	< d d' >2\f
	c-sharp'8 r r4
	< d, d' >2
	c-sharp'8 r r4
	e,2\f~
	e4 r
	r16 b[ c-sharp d-sharp] e[ b c-sharp d-sharp]
	e[ b c-sharp d-sharp] e8 r
	e2~
	e4 r
	r16 b[ c-sharp d-sharp] e[ b c-sharp d-sharp]
	e[ b c-sharp d-sharp] e8 r
	r16 b\f[ c-sharp d-sharp] e8 r
	r16 c[ d! d-sharp] e8 r
	r16 b[ d! d-sharp] e8 r
	r16 c[ d! d-sharp] e8 r
	R1*2/4
	
	\set Staff.midiInstrument = #"pizzicato strings"
	r4 r8 b-flat''\p^\markup {pizz.}
	b-flat[ g g e]
	e[ f d < c-sharp e >]
	< a f' > r r4
	r4 r8 b-flat'
	b-flat[ g g e]
	e[ e a a]
	a r r4
	r4 r8 g
	g[ e] e[ b!]
	c-sharp[ d b c-sharp]
	d r r4
	r4 r8 g
	g[ e e b]
	c-sharp[ a a e]
	e[ b c-sharp a]
	a[ a] r4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	< b-flat f' d' b-flat' >8\ff[^arco b-flat''16( a] b-flat8)[ f]
	< a, a' >[ < a c' >] < d-flat b-flat' > r
	
	R1*2/4*2
	
	< b-flat, f' d' b-flat' >8[ b-flat''16( a] b-flat8)[ f]
	< a, a' >[ < a c' >] < d! b-flat' > r
	
	R1*2/4*2
	
	< g,, g' e-flat' b-flat' >8[ b-flat''16( a] b-flat8)[ g]
	< a, c' >[ < a e-flat'' >] < e-flat' b-flat' >8 r
	
	R1*2/4*2
	
	e'8[ e16( d-sharp] e8)[ c]
	d[ g] c, r
	r4 r8 c
	d[ g] c, r
	r4 r8 c
	d[ g] c,[ c]
	d[ g] c,[ c]
	d[ g] c,[ g']
	< a,, a'' >[ a\p] r a_\cr
	r a r a
	r a\< r a
	r a[ a a]\!
	a\f[ a\p] r a\<
	r a r a
	r a r a
	r a[ a a]\!
	a\f[ a\p]\< r a
	r a[ a a]\!
	a\f[ a\p] r a\<
	r a[ a a]\! a\f r r4
	
	R1*2/4*3
	
	< g, d' b' g' >8\ff r r4
	
	R1*2/4*26
	
	\set Staff.midiInstrument = #"pizzicato strings"
	r4 r8 < a' f-sharp' >8\mf^\markup {pizz.}
	r < a f-sharp' > r < a f-sharp' >
	r < a f-sharp' > r < a f-sharp' >
	r < g, d' b' g' > r < g d' b' g' >
	r < g d' b' g' > r < g d' b' g' >
	r < a' f-sharp' > r < a f-sharp' >
	r < a f-sharp' > r < a f-sharp' >
	r < g, d' b' g' > r < g d' b' g' >
	r < g d' b' g' > r4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	f-sharp'2\mf~^arco
	f-sharp4 f-sharp8-.[ c'-.]
	b4.( a8
	g) r r4
	f-sharp2~
	f-sharp4 f-sharp8-.[ c'-.]
	b4.( a8
	g4) r
	
	R1*2/4*8
	
	r8 e\p r4
	r8 e r4
	r8 e r4
	r8 e r4
	r8 e r4
	r8 e r4
	r8 e r4
	r8 e r4
	r8 d r4
	r8 e-sharp r4
	r8 g-sharp r4
	r8 a r4
	r8 d, r4
	r8 e-sharp r4
	r8 g-sharp r4
	r8 a r4
	r8 e\pp r4
	r8 d-sharp r4
	r8 < a e' > r4
	r8 < a e' > r4
	r8 < a e' > r4
	r8 < a e' > r4
	r8 < a f' > r4
	r8 < a f-sharp'! > r4
	r8 e' r4
	r8 d-sharp r4
	r8 < a e' > r4
	r8 < a e' > r4
	r8 < a e' > r4
	r8 < a e' > r4
	r8 < a f' > r4
	r8 < a f-sharp'! >\< r4
	r8 < a f-sharp' > r4
	r8 < a f-sharp' > r4
	r8 g'\! r4
	
	R1*2/4*24
	
	%%% TEMPO 1 %%%
	
	r8 a,\p r b
	r c-sharp r c-sharp
	r c-sharp r c-sharp
	r < g e' > d' r
	< b' f-sharp' >\f r r4
	< b e >8_\markup { \italic dim. } r r4
	< b e >8 r < a e' > r
	r < e a > r < e a >
	a\p r g-sharp r
	g! r c-sharp, r
	a\< r b r
	c-sharp r d\! r
	b-flat'\f r r d,\p
	c-sharp r r4
	
	R1*2/4*2
	
	g-sharp'8\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 b-flat,\p\< r d
	r e r e\!
	g-sharp\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 b-flat,\p\< r d
	r d r c-sharp\!
	g-sharp'\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 b-flat,\p r d
	r e r e
	d2\mf
	e
	f-sharp
	< g, g' >
	g'_\cr
	< f a >4 b-flat
	b!2
	c4 < f, d' >
	< d d' >2\f
	c-sharp'8 r r4
	< d, d' >2
	c-sharp'8 r r4
	d,2\mf
	d
	d4\< d
	e e\!
	
	\set Staff.midiInstrument = #"pizzicato strings"
	r8 f'^\markup {pizz.} r < c-sharp e >
	r d r c-sharp
	r < d, b' > r < e a >
	r < f a > r < e a >
	< f-sharp! a >8\p r r4
	< e a >8 r r4
	< e a >8 r r4
	< e a >8 r < f-sharp a > r
	b'8\f r r4
	< e,, b' g' >8\mf r r4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	< b' e >8^\markup {arco} r c-sharp r
	b r a-sharp r
	< d, b' >\f r r b'
	a r a r
	a-sharp-.\p[ a-sharp-.] b-.[ a-.]
	e'-.[ a,-.] b[( a])
	d\f r r d
	c-sharp r a-.\p[ a-.]
	a-.[\< b-. c-sharp-. c-sharp-.]
	d-.[ a-.]\! a-.\f r
	
	\set Staff.midiInstrument = #"pizzicato strings"
	d,\mf^\markup {pizz.} r r4
	c-sharp8 r d r
	e[ g b d]
	e[ e,] r4
	d8 r r4
	c-sharp8 r d r
	e[ g b d]
	e[ e,] r4
	< d b' f-sharp' >8\f r r4
	< d b' >8 r r4
	< d b' f-sharp' >8 r r4
	< d b' >8 r r4
	< d b' f-sharp' >8 r r4
	< d b' f-sharp' >8 r r4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	< e b' e >8^arco r < d b' f-sharp' > r
	< d b' g' > r < d b' g-sharp' > r
	< d a' a' >[ d16(^\markup { \dynamic p \italic {poco a poco cresc.} } c-sharp] d8)[ d'-.]
	c,8-.[ c16( b] c8)[ c']
	b,16[ c-sharp! d-sharp f-sharp] g-sharp[ a-sharp b c-sharp]
	d-sharp[ e f-sharp b,] r4
	e,8-.[^\cr e16( d-sharp] e8)[ e'-.]
	d,![ d16( c-sharp] d8)[ d'-.]
	c-sharp,16[ d-sharp e-sharp g-sharp] a[ b c-sharp d-sharp]
	e-sharp[ f-sharp g-sharp c-sharp,] r4
	f-sharp,8-.[^\markup { \italic {sempre cresc.} } f-sharp16( e-sharp] f-sharp)[ c-sharp d-sharp e-sharp]
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
	d8-.\ff[ d16( c-sharp] d8)[ a]
	b[ d] a r
	
	R1*2/4*2
	
	d8-.[ d16( c-sharp] d8)[ b]
	c-sharp[ e] b r
	
	R1*2/4*2
	
	d8-.[ d16( c-sharp] d8)[ b]
	e[ g] d r
	
	R1*2/4*2
	
	e8-.[ e16( d-sharp] e8)[ b]
	c[ e] b r
	
	R1*2/4*2
	
	e8-.[ e16( d-sharp] e8)[ b]
	c[ e] b r
	
	R1*2/4*2
	
	e8-.[ e16( d-sharp] e8)[ b]
	R1*2/4
	e8-.[ e16( d-sharp] e8)[ b]
	R1*2/4
	e8[ b] r4
	e8[ b] r4
	e8[ b-flat] r4
	e8[ a,] r4
	< a, f-sharp'' >8[ < a d' >] r4
	g''8[ d] r4
	g-sharp8[ d] r8_\markup { \dynamic p \italic cresc.} < g-sharp,, f' >8
	r8 < g-sharp f' > r < g-sharp f' >
	r < g-sharp f' > r < g-sharp f' >
	r < g-sharp f' > r < g-sharp f' >
	< a f-sharp'! >8\f[ f-sharp'] d[ a-sharp]
	b[ f-sharp'] g[ d-sharp]
	e[ b] c-sharp[ e]
	e[ a-sharp, b c-sharp]
	d r e,->\f[ e->]
	e4-> d8->[ c-sharp->]
	b-flat->[( a]) e'4
	< e a > < e c-sharp' >
	< d d' >8 r e->[ e->]
	e4-> d8->[ c-sharp->]
	b-flat->[( a]) e'4
	< e a > < e c-sharp' >
	< d d' >8 r c-sharp' r
	b r b r
	b r b-flat4->~
	b-flat8 r < a e' > r
	< d, d' > r c-sharp' r
	b r b r
	b r b-flat4->~
	b-flat8 r < a e' > r
	< d, d' >\f r < e c-sharp' > r
	< d d' > r < e c-sharp' > r
	< d d' > r < e c-sharp' > r
	< d d' > r < e c-sharp' > r
	< d d' > r d''4:16
	d: c-sharp8:16[ b8:16]
	a8 r d4:16
	d: c-sharp8:16[ b8:16]
	a8:[ d: c-sharp: b:]
	a:[ d: c-sharp: b:]
	a8 r r4
	< a, a' >8 r r4
	< d, d' b' >8 r r4
	< a' c-sharp' >8 r r4
	< a d' >8:16\ff[ < a c-sharp' >: < a d' >: < a c-sharp' >:]
	< a d' >8:16[ < a c-sharp' >: < a d' >: < a c-sharp' >:]
	< a d' >8:16[ < a c-sharp' >: < a d' >: < a c-sharp' >:]
	< a d' >8:16[ < a c-sharp' >: < a d' >: < a c-sharp' >:]
	< a d' >8-.[ d'16( c-sharp] d8)[ < a, a' >]
	< a c-sharp' >[ < a e'' >] d'[ f-sharp]
	a r r4
	< d,,, a' f-sharp' d' >8 r r4\fermata
}
