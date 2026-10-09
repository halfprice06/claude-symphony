\version "2.20.0"

theSecondViolins =  \relative d' {
	\clef "treble"
	\key d \major
	
	r1
	R1
	
	r2 r4 d\p
	e d c-sharp r
	R1
	r4 c-sharp( b a-sharp)
	r4 b r2
	
	R1*2
	
	a1
	a1
	< b d >
	c-sharp\<
	c-sharp8 r c-sharp2\mf\! \appoggiatura d8( c-sharp16)[(_\markup { "" \raise #-2.5 \italic cresc. }
		 b c-sharp e])
	< d a' >1\<
	g-sharp8\f\! r g-sharp2 \appoggiatura a8( g-sharp16)[( f-sharpsharp g-sharp b])
	g-sharp8 r g-sharp2 \appoggiatura a8( g-sharp16)[( f-sharpsharp g-sharp b])
	g-sharp8\ff g-sharp \appoggiatura a8( g-sharp16)[( f-sharpsharp g-sharp b])
		g-sharp8 g-sharp \appoggiatura a8( g-sharp16)[( f-sharpsharp g-sharp b])
	g-sharp8[ d f g-sharp] < d b' >[ < d d' >] f'[ g-sharp]
	< a, a' > r r4 r r8 d,\f(
	c-sharp) r r4 r r8 d\mf(
	c-sharp) r r d\p( c-sharp) r r d(
	c-sharp) r r4 r2
	
	R1*3
	
	r2 r8 r4\fermata r8
	d1\pp
	c-sharp
	b
	a2~ a8 r r4
	
	R1*3
	
	r2 r4 r8 e'\p
	g r r c-sharp, e r r4
	
	R1*4
	
	\set Staff.midiInstrument = #"pizzicato strings"
	a,8\p^\markup { pizz. } r r4 r a8 r
	a8 r r4 r a8 r
	< g d' > r r4 r < g d' >8 r
	
	\set Staff.midiInstrument = #"string ensemble 1"
	d'2~^\markup { arco } d8 r a4~
	a8[^\markup { \italic dolce } b( c-sharp e]) e-sharp[( f-sharp] a,4)~
	a8[ b( c-sharp e]) e-sharp[( f-sharp] d)\< r
	b-sharp8\! r c-sharp r d r r4
	c-sharp8 r r4 r2
	R1
	r8 b-flat\pp r a r g-sharp r c-sharp
	r a r a r d[ d a]
	r b-flat r a r g-sharp r c-sharp
	r a r a r d-.[ d-. a-.]
	r c-sharp_\cr r b r a-sharp r4
	r8 f-sharp' r e r d-sharp r4
	r8 d! r c r e r e
	f\f r f4~ f8 r r4
	a-flat8 r < b,! a-flat' >4~ < b a-flat' >8 r r4
	< f' a >8\f[ < f a >16. < f a >32] < f a >8[ < f a >16. < f a >32] < g b-flat >8 r r4
	< f a >8[ < f a >16. < f a >32] < f a >8[ < f a >16. < f a >32] < g b-flat >8 r r4
	< f a >8[ < f a >16. < f a >32] < f-sharp a >8 r < d d' >8[ < d d' >16. < d d' >32] < d d' >8 r
	< d d' >8[ < d d' >16. < d d' >32] < d d' >8 r < d-sharp c' >8[ < d-sharp c' >16. < d-sharp c' >32] < d-sharp c' >8 r
	< e a >8\ff r < e a > r a^>( g-sharp) r4
	< e a >8 r < e a > r a^>( g-sharp) r4
	r8 g-sharp_\markup { \italic dim. } r4 r8 g-sharp r4
	g-sharp8 r r4 r2
	
	R1*2
	
	r4 d4\pp r c-sharp
	r c-sharp r d
	r c-sharp r d
	r e r d
	r c r c-sharp
	g-sharp(\< a)\! b8(\> c-sharp d4)\!
	
	R1*2
	
	a-sharp2_\markup { \dynamic pp \italic {poco cresc.} } b
	a! g-sharp
	a-sharp b
	c c-sharp4~ c-sharp8 r
	
	\tuplet 3/2 { r8 d8\p[~ d]~ } d4 \tuplet 3/2 { r8 c-sharp8[~ c-sharp]~ } c-sharp4
	\tuplet 3/2 { r8 c-sharp8[~ c-sharp]~ } c-sharp4 \tuplet 3/2 { r8 d8\p[~ d]~ } d4
	a-sharp2 b~
	b_\markup { \italic {poco a poco cresc.} } b~
	b a-sharp
	\tuplet 3/2 { r8 d[( b] } \tuplet 3/2 { d[ b d]) } \tuplet 3/2 { r f-sharp[( c] } \tuplet 3/2 { f-sharp[ c f-sharp]) }
	\tuplet 3/2 { r g[( e]) } \tuplet 3/2 { r g-sharp[( d]) } \tuplet 3/2 { r g[( e]) } \tuplet 3/2 { r b'[( f]) }
	\tuplet 3/2 { r c-sharp'\mf[( a-sharp] } \tuplet 3/2 { c-sharp[ a-sharp c-sharp]) } \tuplet 3/2 { r c-sharp[( a-sharp] } \tuplet 3/2 { c-sharp[ a-sharp c-sharp]) }
	d4\mf c-sharp!4~ c-sharp8[ c-sharp-.]( d-.[ d-.])
	c-.[( c-.]) b-flat-.[( b-flat-.]) a-.[( a-.]) d,-.[( e!-.])
	d'4 c-sharp!4~ c-sharp8[ c-sharp-.]( d-.[ d-.])
	c-.[( c-.]) b-flat-.[( b-flat-.]) a-.[( a-.]) g-.[( e-flat-.])
	e-flat4 e-flat~ e-flat8[ f( b-flat d])
	d,4 d~ d8[ e!( a c-sharp!])
	r8 c,!8 c'4 c-sharp8 r r4
	R1
	r2 r4 \tuplet 3/2 { < a c-sharp >8\f[ < a c-sharp > < a c-sharp >] }
	r2 r4 \tuplet 3/2 { < a c-sharp >8[ < a c-sharp > < a c-sharp >] }
	r8 c-sharp r4 r8 b r4
	r8 c r4 r8 g r4
	c2\fp b
	b a
	a4 a a~ a8 r
	a4 a a~ a8 r
	f4_\markup { \italic {poco cresc.} } e e e
	e a a a
	a8\mf r r4 r2
	
	R1*3
	
	r8 c-sharp,16\pp[_\markup { \translate #(cons 4 -1) \italic {poco a poco cresc.} } r d r d-sharp] r
		e[ r c-sharp r d! r d-sharp] r
	e16[ r c-sharp r d! r < b f-sharp' >] r < b g-sharp' >[ r c-sharp r d r < b f-sharp' >] r
	< b g-sharp' >[ r g-sharp r a r a] r b[ r b r c-sharp r c-sharp] r
	d\mf[ r d r d r d] r < a d >2\f\>
	d16\mf[\! r d r d r d] r < a d >2\f
	f'16\mf[ r f r f r f] r f2\f\>
	a16\mf[\! r a r a r a] r a-flat2\f\>
	< a-flat e-flat' >16[ r < a-flat e-flat' >\mf\! r < a-flat e-flat' > r < a-flat e-flat' >] r d-sharp!2\f
	< g-sharp, e'! >8\mf < g-sharp e' > r < g-sharp e' >[ < g-sharp e' > < g-sharp e' >] r < g-sharp e' >
	< a f' > < a f' > r < a f' >[ < a f' > < a f' >] r < a f' >
	< b a' > < b a' > r < b a' >[ < b a' > < b a' >] r < b a' >
	< b-sharp a' > < b-sharp a' > r < b-sharp a' >[ < b-sharp a' > < b-sharp a' >] r < b-sharp a' >
	
	R1*4
	
	< e, c-sharp' e >8\ff r c-sharp'2 b16[( a c-sharp e])
	b4.( c-sharp8) b4 c-sharp
	< b, f-sharp' d' b' >8 r d'2 c-sharp16[( b d f-sharp])
	c-sharp4.( d8) c-sharp4 c-sharp
	f-sharp8 g-sharp a[ g-sharp16( f-sharp] e8) g-sharp a[ f-sharp16( e]
	d8) e-sharp f-sharp[ e16( d] c-sharp8) e-sharp f-sharp[ d16( c-sharp]
	b8) c-sharp d[ c-sharp16( b] a8)[ g-sharp16( f-sharp] e-sharp)[ c-sharp( e-sharp g-sharp])
	b8 c-sharp d[ c-sharp16( b] a8)[ g-sharp16( f-sharp] e!)[ f-sharp( g-sharp b])
	< e, c-sharp' e >8\ff r8 c-sharp'2 b16[( a c-sharp e])
	b4.( c-sharp8) b4 c-sharp
	< b, f-sharp' d' b' >8 r d'2 c-sharp16[( b d f-sharp])
	c-sharp4.( d8) c-sharp4 c-sharp
	f-sharp8 g-sharp a[ g-sharp16( f-sharp] e8) g-sharp a[ f-sharp16( e]
	d8) e-sharp f-sharp[ e16( d] c-sharp8) e-sharp f-sharp[ d16( c-sharp]
	b-sharp8)[ f-sharp\p]~ f-sharp[ g-sharp,]~ g-sharp r r4
	r8 g-sharp4 g-sharp8~ g-sharp[\< c-sharp16( b-sharp]) c-sharp[( d-sharp e d-sharp])\!
	g-sharp8\mf[ f-sharp\p]~ f-sharp[ g-sharp,]~ g-sharp r r4
	r8 g-sharp4 g-sharp8~ g-sharp[\< c-sharp16( b-sharp]) c-sharp[( d-sharp e c-sharp])\!
	d-sharp8\mf[ a-sharp']~ a-sharp[ a-sharp,]~ a-sharp r r c-sharp~
	c-sharp a-sharp'[~ a-sharp] a-sharp,[~ a-sharp] r r c-sharp~
	c-sharp c-sharp'[~ c-sharp] r r b-sharp,~ b-sharp[ d-sharp](
	g-sharp)[ g-sharp]~ g-sharp r r g-sharp,~ g-sharp[ g-sharp](
	c-sharp) d-sharp4\< f-sharp8 b c-sharp4 e8(\!
	a\mf) < a, g'! >4 a8~ a r r4
	r8 d,~\< d[~ d]~ d[ g16( f-sharp]) g[( a b-flat a])\!
	d8\mf < a g' >4\p a8~ a r r4
	r8 d,~\< d[~ d]~ d[ g16( f-sharp]) g[( a b-flat g])\!
	a8\mf[ < c-sharp e >]~ < c-sharp e >[ e,]~ e r r g~
	g8[ < c-sharp e >]~ < c-sharp e >[ e,]~ e r r g~
	g[ e]~ e r r a,~ a[ a](
	d)[ d]~ d r r b~_\cr b r
	r a~ a[ c]( f)[ g]~ g[ b-flat](
	e-flat)[ f,]~ f[ g-sharp]( c-sharp!)[ d-sharp,]~ d-sharp[ f-sharp](
	b!\ff) r r4 r2
	< d, b' f' >8\f r r4 r2
	
	\set Staff.midiInstrument = #"pizzicato strings"
	c'8\pp^\markup {pizz.} \noDynamic r\p c r r4 c'8 r
	< d, b' > r b, r r4 c-sharp8 r
	d r d r r4 d'8 r
	c-sharp! r c-sharp, r r4 c-sharp8 r
	c r f r c r g' r
	d r f r a, r e' r
	
	\set Staff.midiInstrument = #"string ensemble 1"
	f2\p(\>^\markup {arco} e8)\! r r4
	f2^>(\> e8)\! r
		\set Staff.midiInstrument = #"pizzicato strings"
		b\pp^\markup {pizz.} r
	c8 r c r r4 c'8 r
	< d, b' > r b r r4 c-sharp!8 r
	d r d r r4 d'8 r
	c-sharp r c-sharp, r r4 c-sharp8 r
	c r f r c r g' r
	d r f r a, r e' r
	d-sharp r r4 d-sharp8 r r4
	c-sharp!8 r r4
		\set Staff.midiInstrument = #"string ensemble 1"
		c-sharp2^\markup {arco}
	b8 r r4
		\set Staff.midiInstrument = #"pizzicato strings"
		d-sharp8^\markup {pizz.} r r4
	c-sharp8 r r4
		\set Staff.midiInstrument = #"string ensemble 1"
		c-sharp2^\markup {arco}
	c-sharp8 r r4
		\set Staff.midiInstrument = #"pizzicato strings"
		c-sharp8^\markup {pizz.} r r4
	< a f' >8 r r4
		\set Staff.midiInstrument = #"string ensemble 1"
		d2^\markup {arco}
	c-sharp8 r r4
		\set Staff.midiInstrument = #"pizzicato strings"
		c-sharp8^\markup {pizz.} r r4
	< a f' >8 r r4
		\set Staff.midiInstrument = #"string ensemble 1"
		d2\<^\markup {arco}
	d8\! r r4 r2
	d8 r r4 r2
	
	R1*2
	
	< a' a' >8\ff r < a a' >2 \grace { g16[ a] } g16[( f a c])
	g4.( a8) g4 a
	b-flat8 r b-flat2 \grace { a16[ b-flat] } a16[( g b-flat d])
	a4.( b-flat8) a4 a
	d8 e f[ e16( d] c8)[ e] f[ d16( c]
	b-flat8)[ c-sharp!] d[ c16( b] a8)[ c-sharp] d[ b-flat16( a])
	g16[ a b-flat g] f[ a b-flat f] e-flat[ f-sharp g e-flat] d[ f-sharp g d]
	c-sharp!8\ff[ a'] b-flat[ b-flat,] b[ b] c[ c]
	c-sharp!8 g'4 g-sharp g-sharp < d' e >8
	< c-sharp e >[ a] b-flat[ b-flat,] b[ b] c[ c]
	c-sharp!8 g'!4 g-sharp g-sharp < d' e >8
	< c-sharp e >[ b-flat] b[ b,] c[ c] c-sharp[ c-sharp]
	d8 g-sharp4 a g b!8
	c[ b] c[ c,] c-sharp[ c-sharp] d[ d]
	d-sharp < f-sharp! a >4 e f c'8
	c-sharp![ b-sharp] c-sharp[ c-sharp,] d![ d'!] d-sharp[ d-sharp,]
	e[ e'] f[ f,] f-sharp[ f-sharp'] g[ g,]
	g-sharp8\ff[ f'16( g!] g-sharp8)[ f,16( g] g-sharp8)[ f'16( g] g-sharp8)[ f,16( g]
	g-sharp8)[ f'16( g] g-sharp8)[ f,16( g] g-sharp8)[ f'16( g] g-sharp8)[ g,16( g-sharp]
	a8) r r4 r r8 f16[( g!]
	g-sharp8)[ f'16( g] g-sharp8)[ f,16( g] g-sharp8)[ f'16( g] g-sharp8)[ g,16( g-sharp]
	a8) r r4 r r8 f16[( g!]
	g-sharp8)[ f'16( g] g-sharp8)[ f,16( g] g-sharp8)[ f'16( g] g-sharp8)[ g,16( g-sharp]
	a8) r r4 r2
	
	s1*46
	
	d,2.\pp d4
	c-sharp2. c4
	b2. b4
	a4. b8( a) r\pp a4~_\markup { \italic dolce }
	a8[ b( c-sharp e]) e-sharp[( f-sharp] a,4)~
	a8[ b(_\markup { \italic {poco cresc.}} c-sharp e!]) e-sharp[( f-sharp] e4)
	d4~( \tuplet 3/2 { d8[ e f-sharp]) } b,2\<
	g-sharp16[( a b c-sharp]) d4(\! c-sharp8) r r e'\p
	g r r c-sharp, e r r4
	
	R1*2
	
	\set Staff.midiInstrument = #"pizzicato strings"
	a,,8\pp^\markup {pizz.} r r4 r a8 r
	a_\cr r r4 r < a f-sharp' >8 r
	d8 r r4 r d8 r
	r4
		\set Staff.midiInstrument = #"string ensemble 1"
		c-sharp8[(^\markup {arco} e]) r4 b8[( d-sharp])
	r4 b8[( d!]) r4 a8[( c-sharp])
	r4 a8[( c]) r4 g8[( b])
	r4 c r b-flat
	b!2_\markup { \dynamic {mf} \italic dim. } c-sharp
	c2~\> c8\! r r4
	R1
	r8 e-flat\pp r d r e r f-sharp
	r d r d r g-.[ g-. d-.]
	r8 e-flat r d r e r f-sharp
	r d r d r g-.[ g-. d-.]
	r f-sharp_\cr r e r d-sharp r b
	r b' r a r g-sharp r a,
	r g' r d r < g a > r < f a >
	b-flat r b-flat4~ b-flat8 r r4
	d-flat8 r d-flat4~ d-flat8 r r4
	
	\set Staff.midiInstrument = #"pizzicato strings"
	< d,! d'! >8\f^\markup {pizz.} r r4 r2
	< d d' >8 r r4 r2
	< d d' >8_\cr r < d d' > r g r < c-sharp! g' > r
	< d, d' g > r < d b-flat' g' > r < f c-sharp'! g-sharp' > r < f d' g-sharp > r
	
	\set Staff.midiInstrument = #"string ensemble 1"
	< f-sharp! d' a' >8\ff^\markup {arco} r < f d' a' > r << { e'4 } \\ { d8[( c-sharp]) } >> r4
	< f-sharp,! d' a' >8 r < f d' a' > r << { e'4 } \\ { d8[( c-sharp]) } >> r4
	r8 c-sharp, r4 r8 c-sharp r4
	r8 c-sharp8~ c-sharp4~ c-sharp8 r r4
	
	R1*2
	
	r8 a4\pp a8 r a4 a8
	r8 b4 b8 r b4 b8
	r4 b4\p r b
	r c r b
	r b-flat r a
	c-sharp(\< d) e8[(\! f-sharp] a,) r
	
	R1*2
	
	r16_\markup { "" \raise #-1.0 \dynamic p \italic cresc. } b[( d-sharp b]) r b[( d-sharp b]) r b[( e b]) r b[( e b])
	r b-flat[( d! b-flat]) r b-flat[( d b-flat]) r a[( c-sharp a]) r a[( c-sharp a])
	r b![( d-sharp b]) r b[( d b]) r b[( e b]) r b[( e b])
	r b[( f-sharp' b,]) r b[( f-sharp' b,]) r c-sharp![( e-sharp c-sharp]) r c-sharp[( e-sharp c-sharp])
	r d[( f-sharp d]) r g-sharp,[(_\cr d' g-sharp,]) r g-sharp[( d' g-sharp,]) r a[( d-sharp a])
	e-flat'2\mf~ e-flat8 e-flat~ e-flat e(
	f)[ d]( e-flat)[ c]( d)[ d-.( e-flat-. e-flat-.])
	e-flat2~ e-flat8 e-flat~ e-flat e(
	f)[ d]( e-flat)[ c]( d)[ d]( c-.[ a-flat-.])
	a-flat4 a-flat~ a-flat8[ b-flat e-flat g]
	g,4 g~ g8[ a d f-sharp!]
	r8 b,\f f'4 f-sharp8 r r4
	R1
	r2 r4 \tuplet 3/2 { f-sharp8\f[ g a] }
	r2 r4 \tuplet 3/2 { f-sharp8[ g-sharp a] }
	r8 < d-sharp f-sharp >8 r4 r8 < a e' > r4
	r8 < d! f > r4 r8 < c f! > r4
	b-flat4\pp( a) a16[( g-sharp f-sharpsharp a]) g-sharp4
	a4( g!) g16[( f-sharp! e-sharp g]) f-sharp4
	g4(\< f) f16[( e d-sharp f] e8)\! r
	g4(\< f) f16[( e d-sharp f] e8)\! r
	b-flat'4\mf a < g a > < f a >
	e\< < d d' > < d d' > < d d' >8 < d d' >\!
	< d d' >8 r r4 r2
	
	R1*3
	
	r4 r8 g-sharp,16\pp r a_\markup { \italic {poco a poco cresc.}} r r8 r g-sharp16 r
	a[ r a r b r b] r a[ r a r b r b] r
	a[ r c-sharp r < b d > r < b d >] r e[ r c-sharp r d r f-sharp] r
	< b, g' >[\< r < c-sharp g' > r < b g' > r < c-sharp g' >]\! r < d b' >2\f\>
	< b g' >16[ r\mf\! < c-sharp g' > r < b g' > r < c-sharp g' >] r < d b-flat' >2\f\>
	< d b-flat' >16[ r\mf\! < d b-flat' > r < d b-flat' > r < d b-flat' >] r < f d' >2\f\>
	< f d' >16[ r\mf\! < g d' > r < f d' > r < g d' >] r < d-flat a-flat' >2\f\>
	< d-flat a-flat' >8[\! < d-flat b-flat' > < d-flat a-flat' > < d-flat b-flat' >] < d b' >2\f
	< c-sharp' g'! >8\mf[ < c-sharp g' >] r < c-sharp g' >[ < c-sharp g' > < c-sharp g' >] r < c-sharp g' >
	< d, d' >[ < d d' >] r < d d' >[ < d d' > < d d' >] r < d d' >
	< d' e >[ < d e >] r < d e >[ < d e > < d e >] r < d e >
	d'[ d] r d[ d d] r d
	
	R1*4
	
	< d,, a' f-sharp' >8\f r d\p r e r d-sharp r
	d-sharp_\cr r b r c-sharp r a r
	a r c r d r c r
	b-flat r r4 r f'8\f e
	e r r4 r e8 d
	d r r4 r d8 c
	c r r b b r r a
	a r a'2 r4
	a,8 r a'2 r4
	< d, b-flat' >8[ < d b-flat' >~ < d b-flat' > < d b-flat' >]~ < d b-flat' >[ < d b-flat' >~ < d b-flat' > < d b-flat' >]
	b-flat'\f[ a->] a[ b-flat->] b-flat[ a->] a[ b-flat->]
	b-flat8 b-flat4 b-flat4 b-flat4 b-flat8
	< d, b'! >8 < d b' >4 < d b' > < d b' > < d b' >8
	< d a' >8\ff[ e-flat\p](^\< d[ c-sharp!]) b[( b-flat] a4)
	a4( d8)[ d]^\! d r c-sharp\f r
	f-sharp8\p[(^\< e-flat] d[ c-sharp]) b![( b-flat] a4)
	a( d8)[ d]^\! d r c-sharp\f r
	g' r r4 r8 < g a >\ff[ < g a > < g a >]
	< d b-flat' > r r4 r8 < g a >[ < g a > < g a >]
	< d b-flat' > r r < g a > < d b-flat' > r r < g a >
	< d b-flat' > r r < d' e > < d e-sharp > r r < d e-sharp >
	< d f-sharp >\ff < d, d' >4 < d d' >8~ < d d' > e8:16[ f-sharp: g:]
	a < d, d' >4 < d d' >8~ < d d' > e8:16[ f-sharp: g:]
	a d4 e8 d c-sharp4 d8
	c-sharp b4 g8 b-flat-> r r < g a >
	< f-sharp a > < d d' >4 < d d' >8~ < d d' > e8:16[ f-sharp: g:]
	a < d, d' >4 < d d' >8~ < d d' > e8:16[ f-sharp: g:]
	a d4 e8 d c-sharp4 d8
	c-sharp b4 g8 b-flat-> r r < g a >
	< f-sharp a >8 r < b, f-sharp' > r < a f-sharp' d' > r < d a' f-sharp' > r
	< d a' f-sharp' > r < b f-sharp' > r < a f-sharp' d' > r < d a' f-sharp' > r
	< d a' f-sharp' > r < d b' f-sharp' > r < d a' f-sharp' > r < d b' f-sharp' > r
	< d a' f-sharp' > r < d b' f-sharp' > r < d a' f-sharp' > r < d b' f-sharp' > r
	< d a' f-sharp' >[ a d f-sharp] < f-sharp a >[ < f-sharp a > < f-sharp a > < a f-sharp' >]
	< d, a' f-sharp' >4 < d a' f-sharp' > < d a' f-sharp' > < d a' f-sharp' >
	< a d >1\fermata
}
