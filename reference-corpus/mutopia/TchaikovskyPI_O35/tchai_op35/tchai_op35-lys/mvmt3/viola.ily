\version "2.20.0"
theViolas =  \relative d' {
	\clef "alto"
	\key d \major

	a8\ff[ a16( g-sharp] a8)[ a]
	b-flat2
	b-flat
	b-flat4 a8 r
	a8[ a16( g-sharp] a8)[ a]
	b-flat4 b
	c-sharp, d
	c-sharp8 r r4
	
	R1*2/4*2
	
	g'8-.\f[ g16( f-sharp] g8)[ g-.]
	
	R1*2/4*4
	
	r4 < c-sharp e a >8\ff r
	
	R1*2/4*36
	
	r8 f-sharp,\p r f
	r < e g > r < e g >
	r < e g > r < e g >
	r a f-sharp r
	f-sharp\f r r4
	< g e' >8_\markup { \italic dim. } r r4
	< g-sharp e' >8 r < g e' > r
	r g r g
	a\p r b r
	a r g r
	e\< r e r
	e r f-sharp\! r
	b-flat\f r r f\p
	e r r4
	R1*2/4
	r4 r8 c-sharp'
	d\mf r r4
	c-sharp8_\markup { \italic dim. } r r4
	R1*2/4
	r8 g-sharp\< r a\!
	d\mf r r4
	c-sharp8_\markup { \italic dim. } r r4
	
	R1*2/4*2
	
	d8\mf r r4
	c-sharp8_\markup { \italic dim. } r r4
	R1*2/4
	r8 g-sharp r a
	f2\mf
	a
	a-sharp2
	b
	g_\cr
	a4 b-flat
	< a-flat f' >2
	< a-flat f' >4 < g-sharp d' >
	g-sharp2\f
	a8 r r4
	g-sharp2
	a8 r r4
	f2\mf f
	f-sharp!4\< g
	g-sharp a\!
	
	\set Staff.midiInstrument = #"pizzicato strings"
	r8 g-sharp'^\markup {pizz.} r g
	r f r g
	r f r c-sharp
	r b r a
	d,8\p r r4
	a'8 r r4
	a8 r r4
	a8 r a r
	< b f-sharp' >\f r r4
	< b g' >8\mf r r4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	g-sharp8^arco r g r
	f-sharp r e' r
	f-sharp,\f r r d'
	c-sharp r c-sharp r
	c-sharp-.\p[\< c-sharp-.] d-.[ e-.]
	e-.[ e-.] d4->\!
	d8\f r r < d b' >
	e r r4
	r8 a-.[\< a-. a-.]
	a-.[ g-.]\! f-sharp-.\f r
	
	\set Staff.midiInstrument = #"pizzicato strings"
	f-sharp,\mf^\markup {pizz.} r r4
	e8[ g] f-sharp r
	g r b r
	b r r4
	f-sharp8 r r4
	e8[ g] f-sharp r
	g r b r
	b r r4
	f-sharp8\f r r4
	b8 r r4
	f-sharp8 r r4
	b8 r r4
	f-sharp8 r r4
	< d' b' >8 r r4
	b8 r < b d > r
	< b d > r < b g-sharp' > r
	g-sharp r r4
	g-sharp8 r r4
	g-sharp8 r r4
	g-sharp8 r g-sharp r
	a r r4
	b-flat8 r r4
	b!8\> r b\! r
	b\p r r4
	
	R1*2/4*4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	< c-sharp e a >8\ff^arco r r4
	
	R1*2/4*10
	
	r4 e,8\pp r8
	r4 e8 r
	r4 e8 r
	r4 e8 r
	r4 e8 r
	r4 e8 r
	r4 e8 r
	r4 e8 r
	
	R1*2/4*8
	
	r4 g-sharp'8\p-.[( a-.])
	b4-> r
	d,4 c-sharp8-.[( d-.])
	e4-> a8[( f])
	e4 a8-.[~ a-.]
	b4-> r
	d,4 c-sharp8-.[( d-.])
	e4-> a8[( f])
	e4 r8 e,8\mf
	r e r e
	r e r e
	r e r e
	r e r e
	r e r e
	r e r e
	r e r e
	r e r4
	r4 g-sharp\mf~
	g-sharp8[ d] d'4~
	d g-sharp,4
	f-sharp8[( g-sharp] a4)
	d4 b
	g-sharp8[( d]) b'4
	e8[ e e d]
	c-sharp8 r r4
	r8 c-sharp\p r4
	r8 b r4
	r8 g-sharp r4
	r8 a r4
	r8 c-sharp r4
	r8 b r4
	r8 g-sharp r4
	r8 a r4
	r8 f-sharp r4
	r8 f-sharp r4
	r8 d-sharp' r f-sharp,
	r e r4
	r8 b'4.
	r8 a-sharp r a-sharp
	r b r f-sharpsharp
	r a r4
	r8 b4.
	r8 a-sharp r a-sharp
	r b r f-sharpsharp
	r g-sharp r4
	r8 b4.\pp
	r8 g-sharp4.
	r8 g-sharp4.
	r8 f4.
	r8 g4.
	r8 e4.
	r8 f-sharp!4.
	r8 g4.
	r8 g4.~
	g2
	r8 g4.
	r8 g4.
	r8 g4.~
	g2
	r8 e4.~
	e8 r r4
	r8 e4.~
	e8 r r4
	
	R1*2/4*8
	
	r8 f-sharp\p r f
	r < e g > r < e g >
	r < e g > r < e g >
	r a f-sharp r
	f-sharp\f r r4
	< g e' >8_\markup { \italic dim. } r r4
	< g-sharp e' >8 r < g e' > r
	r g r g
	a\p r b r
	a r g r
	e\< r e r
	e r f-sharp\! r
	b-flat\f r r f\p
	e r r4
	R1*2/4
	r4 r8 c-sharp'\mf
	d r r4
	c-sharp8_\markup { \italic dim. } r r4
	R1*2/4
	r8 g-sharp\< r a\!
	d\mf r r4
	c-sharp8_\markup { \italic dim. } r r4
	
	R1*2/4*2
	
	d8\mf r r4
	c-sharp8_\markup { \italic dim. } r r4
	R1*2/4
	r8\< g-sharp r a\!
	f2\mf
	a
	a-sharp2
	b
	g_\cr
	a4 b-flat
	< a-flat f' >2
	< a-flat f' >4 < g-sharp d' >
	g-sharp2\f
	a8 r r4
	g-sharp2
	a8 r r4
	e2\f~
	e4 r
	r8 g[ f-sharp g]
	f-sharp[ g] f-sharp r
	e2~
	e4 r
	r8 f-sharp[ e f-sharp]
	e[ f-sharp] e r
	e2\f
	f-sharp2
	g-sharp2
	a4( b-flat8) r
	R1*2/4
	
	\set Staff.midiInstrument = #"pizzicato strings"
	r4 r8^\markup {pizz.} f''\p
	e[ d c b!]
	b-flat[ a a-flat g]
	f r r4
	r4 r8 f'
	e[ d c b-flat]
	a[ < g a > < f a > < e a >]
	< d a' > r r4
	r4 r8 d'
	c-sharp![ b-flat] a[ g-sharp]
	g![ f f e]
	d r r4
	r4 r8 d'
	c-sharp[ b-flat a g-sharp]
	g![ f e b-flat]
	a[ g-sharp g f]
	g[ f] r4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	< b-flat f' >8\ff^arco r < b-flat f' >[ < b-flat f' >]
	< c f >[ < c f >] < d-flat g-flat > r
	
	R1*2/4*2
	
	< b-flat f' >8 r < b-flat f' >[ < b-flat f' >]
	< f' a >[ < e-flat a >] < d b-flat' > r
	
	R1*2/4*2
	
	< b-flat g' >8 r < b-flat g' >[ < b-flat g' >]
	< a f-sharp'! >[ < a f-sharp' >] < b-flat g' > r
	
	R1*2/4*2
	
	< c g' >8 r < c g' >[ < c g' >]
	< b g' >[ < b g' >] < c g' > r
	r4 r8 < c g' >
	< b g' >[ < b g' >] < c g' > r
	r4 r8 < c g' >
	< b g' >[ < b g' >] < c g' > < c g' >]
	< b g' >[ < b g' >] < c g' > < c g' >]
	< b g' >[ < b g' >] < c g' > < c g' >]
	c'[ c,\p] r c_\cr
	r c r c
	r c\< r c
	r c[ c c]\!
	c\f[ c\p] r c\<
	r c r c
	r c r c
	r c[ c c]\!
	c\f[ c\p]\< r c
	r c[ c c]\!
	c\f[ c\p] r c\<
	r c[ c c]\!
	c\f r r4
	
	R1*2/4*3
	
	< g g' d' >8\ff r r4
	
	R1*2/4*10
	
	r4 f-sharp8\pp r
	r4 f-sharp8 r
	r4 f-sharp8 r
	r4 g8 r
	r4 g8 r
	r4 f-sharp8 r
	r4 f-sharp8 r
	r4 g8 r
	
	R1*2/4*8
	
	\set Staff.midiInstrument = #"pizzicato strings"
	r4 r8 c\mf^\markup {pizz.}
	r c r c
	r c r c
	r < g d' b' > r < g d' b' >
	r < g d' b' > r < g d' b' >
	r c r c
	r c r c
	r < g d' b' > r < g d' b' >
	r < g d' b' > r d\mf
	r d r d
	r d r d
	r d r d
	r d r d
	r d r d
	r d r d
	r d r d
	r d r4
	
	R1*2/4*8
	
	\set Staff.midiInstrument = #"string ensemble 1"
	r8 g\p^arco r4
	r8 g r4
	r8 g r4
	r8 g r4
	r8 g r4
	r8 g r4
	r8 g r4
	r8 g r4
	r8 f-sharp r4
	r8 g-sharp r4
	r8 b r4
	r8 d r4
	r8 f-sharp, r4
	r8 g-sharp r4
	r8 b r4
	r8 d r4
	r8 f-sharp,\pp r4
	r8 f-sharp r4
	r8 f-sharp r4
	r8 e r4
	r8 e r4
	r8 e r4
	r8 f r4
	r8 f-sharp! r4
	r8 f-sharp r4
	r8 f-sharp r4
	r8 f-sharp r4
	r8 e r4
	r8 e r4
	r8 e r4
	r8 f r4
	r8 f-sharp!\< r4
	r8 f-sharp r4
	r8 f-sharp r4
	r8 < g d' >\! r4
	
	R1*2/4*24
	
	r8 f-sharp\p r f
	r < e g > r < e g >
	r < e g > r < e g >
	r a f-sharp r
	f-sharp\f r r4
	< g e' >8_\markup { \italic dim. } r r4
	< g-sharp e' >8 r < g e' > r
	r g r g
	a\p r b r
	a r g r
	e\< r e r
	e r f-sharp\! r
	b-flat\f r r f\p
	e r r4
	R1*2/4
	r4 r8 c-sharp'
	d\mf r r4
	c-sharp8_\markup { \italic dim. } r r4
	R1*2/4
	r8 g-sharp\< r a\!
	d\mf r r4
	c-sharp8_\markup { \italic dim. } r r4
	
	R1*2/4*2
	
	d8\mf r r4
	c-sharp8_\markup { \italic dim. } r r4
	R1*2/4
	r8 g-sharp r a
	f2\mf
	a
	a-sharp2
	b
	g_\cr
	a4 b-flat
	< a-flat f' >2
	< a-flat f' >4 < g-sharp d' >
	g-sharp2\f
	a8 r r4
	g-sharp2
	a8 r r4
	f2\mf f
	f-sharp!4\< g
	g-sharp a\!
	
	\set Staff.midiInstrument = #"pizzicato strings"
	r8 g-sharp'^\markup {pizz.} r g
	r f r g
	r f r c-sharp
	r b r a
	d,8\p r r4
	a'8 r r4
	a8 r r4
	a8 r a r
	< b f-sharp' >\f r r4
	< b g' >8\mf r r4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	g-sharp8^arco r g r
	f-sharp r e' r
	f-sharp,\f r r d'
	c-sharp r c-sharp r
	c-sharp-.\p[\< c-sharp-.] d-.[ e-.]
	e-.[ e-.] d4->\!
	d8\f r r < d b' >
	e r r4
	r8 a-.[\< a-. a-.]
	a-.[ g-.]\! f-sharp-.\f r
	
	\set Staff.midiInstrument = #"pizzicato strings"
	f-sharp,\mf^\markup {pizz.} r r4
	e8[ g] f-sharp r
	g r b r
	b r r4
	f-sharp8 r r4
	e8[ g] f-sharp r
	g r b r
	b r r4
	f-sharp8\f r r4
	b8 r r4
	f-sharp8 r r4
	b8 r r4
	f-sharp8 r r4
	< d' b' >8 r r4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	< b e >8^arco r < b d > r
	< b d > r < d b' > r
	a2\f~\>
	a2\!_\markup { \dynamic pp \italic {poco a poco cresc.}}
	b8 r r4
	R1*2/4
	b2~^\cr
	b(
	c-sharp8) r r4
	R1*2/4
	c-sharp2~^\markup { \italic {sempre cresc.}}
	c-sharp4 c-sharp8[ c-sharp]
	d2~
	d4 b8[ d]
	< e, g >2~
	< e g >4 < e g >8[ < e g >]
	f2~
	f4
	g-sharp8[ f]
	< e g! >2\f
	< e g >
	< g! d' >4->( c-sharp)
	< g d' >->( c-sharp)
	r8 < a g' a > r < a g' a >
	r < a g' a > r < a g' a >
	r < a g' a > r < a g' a >
	r < a g' a >[ < a g' a > < a g' a >]
	< a f-sharp' a >\ff r < f-sharp' a >[ < d d' >]
	< d d' >[ < d d' >] < d d' > r
	
	R1*2/4*2
	
	< d b' >8 r < d b' >[ < d b' >]
	< b g' >[ < b g' >] < b f-sharp' > r
	
	R1*2/4*2
	
	< g d' b' >8 r < b g' >[ < b g' >]
	< g g' >[ < g g' >] < d' b' > r
	
	R1*2/4*2
	
	< b g' >8 r < b g' >[ < b g' >]
	< e a >[ < e a >] < b g' > r
	
	R1*2/4*2
	
	< b g' >8 r < b g' >[ < b g' >]
	< e a >[ < e a >] < b g' > r
	
	R1*2/4*2
	
	< b g' >8 r < b g' >[ < b g' >]
	R1*2/4
	< b g' >8 r < b g' >[ < b g' >]
	R1*2/4
	< b g' >8[ < b g' >] r4
	< b g' >8[ < b g' >] r4
	< b-flat g' >8[ < b-flat g' >] r4
	< a g' >8[ < a g' >] r4
	< d d' >8[ < d d' >] r4
	< d d' >8[ g] r4
	< f d' >8[ < f d' >] r_\markup { \dynamic p \italic cresc.} < g-sharp, f'! >
	r < g-sharp f' > r < g-sharp f' >
	r < g-sharp f' > r < g-sharp f' >
	r < g-sharp f' > r < g-sharp f' >
	< a f-sharp'! >\f[ f-sharp' f-sharp c-sharp]
	b[ < b f-sharp' >] < b g' >[ f-sharp']
	e[ e a, g-sharp']
	a[ c-sharp, d < e a >]
	< f-sharp a > r g,\f[ g]
	g2(
	e4) g
	g < e c-sharp' >
	< a d >8 r g[ g]
	g2(
	e4) e
	g < e c-sharp' >
	< a d >8 r f-sharp' r
	d r d-sharp r
	e r e4->~
	e8 r < a, e' > r
	< a d > r f-sharp' r
	d r d-sharp r
	e r e4->~
	e8 r < a, e' > r
	< a d >\f r c-sharp r
	< a d > r c-sharp r
	< a d > r c-sharp r
	< a d > r c-sharp r
	< a d > r < d f-sharp >4:16
	< d f-sharp >: f-sharp8:[ g:]
	a r < d, f-sharp >4:16
	< d f-sharp >: f-sharp8:[ g:]
	a8:[ < d, f-sharp >: < d f-sharp >: g:]
	a8:[ < d, f-sharp >: < d f-sharp >: g:]
	< d a' > r r4
	< d a' >8 r r4
	< b g-sharp' >8 r r4
	< a e' c-sharp' >8 r r4
	< f-sharp' d' >8\ff[ < e c-sharp' > < f-sharp d' > < e c-sharp' >]
	< f-sharp d' >[ < e c-sharp' > < f-sharp d' > < e c-sharp' >]
	< f-sharp d' >[ < e c-sharp' > < f-sharp d' > < e c-sharp' >]
	< f-sharp d' >[ < e c-sharp' > < f-sharp d' > < e c-sharp' >]
	< f-sharp d' > r < f-sharp a >[ < d d' >]
	< e c-sharp' >[ < e a >] d[ f-sharp]
	a r r4
	< d,, a' f-sharp' d' >8 r r4\fermata
}
