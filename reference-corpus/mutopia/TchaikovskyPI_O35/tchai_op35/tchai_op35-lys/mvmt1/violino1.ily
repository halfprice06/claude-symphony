\version "2.20.0"

theFirstViolins =  \relative d' {
	\clef "treble"
	\key d \major
	
	f-sharp2.\p e8( d									|
	a4) d8( e f-sharp4) b8( g-sharp						|
	a4) f-sharp2 f-sharp4									|
	g! f-sharp e r										|
	e2. c-sharp8( b										|
	a4) c-sharp8( d e4) f-sharp8( c-sharp					|
	e4) d r2											|
	
	R1*2
	
	c-sharp8^>\p r c-sharp2^> \appoggiatura d8( c-sharp16)[(_\markup { "" \raise #-2.5 \italic cresc. }
		b c-sharp e])
	d1
	g-sharp8^> r g-sharp2^> \appoggiatura a8( g-sharp16)[( f-sharpsharp g-sharp b])
	< e, a >1\<
	c-sharp'8 r c-sharp2\mf\! \appoggiatura d8( c-sharp16)[(_\cr b c-sharp e])
	d1\<
	g-sharp8\f\! r g-sharp2 \appoggiatura a8( g-sharp16)[( f-sharpsharp g-sharp b])
	g-sharp8 r g-sharp2 \appoggiatura a8( g-sharp16)[( f-sharpsharp g-sharp b])
	g-sharp8\ff g-sharp \appoggiatura a8( g-sharp16)[( f-sharpsharp g-sharp b])
		g-sharp8 g-sharp \appoggiatura a8( g-sharp16)[( f-sharpsharp g-sharp b])
	g-sharp8[ d f g-sharp] b[ d f g-sharp]
	a r r4 r4 r8 g-sharp,,\f(
	a) r r4 r4 r8 g-sharp\mf(
	a) r r g-sharp\p( a) r r g-sharp(
	a) r r4 r2
	
	R1*3
	
	r2 r8 r4\fermata r8
	
	R1*2
	
	d,1\p
	d2~ d8 r a4~
	a8[ b( c-sharp e]) e-sharp[( f-sharp] a,4)~
	a8[ b( c-sharp e!]) e-sharp[( f-sharp] e4)
	d4~ \tuplet 3/2 { d8[( e f-sharp]) } b,2
	g-sharp16[(\< a b c-sharp]) d4( c-sharp8)\! r r g'!\p
	b r r e, g r r4
	
	R1*4
	
	\set Staff.midiInstrument = #"pizzicato strings"
	< d a' >8\p^\markup { pizz. } r r4 r < d a' >8 r
	
	< e a > r r4 r < d a' >8 r
	g r r4 r g8 r
	
	\set Staff.midiInstrument = #"string ensemble 1"
	f-sharp4.(^\markup { arco } e-sharp8 f-sharp) r a4~
	a8[^\markup { \italic dolce } b( c-sharp e]) e-sharp[( f-sharp] a,4)~
	a8[ b( c-sharp e]) e-sharp[( f-sharp] a,8)\< r
	f-sharp\! r e r e r r4
	e8 r r4 r2
	R1
	r8 d\pp r c-sharp r < b d > r < g! e' >
	r d' r f-sharp r a[ f-sharp d]
	r d r c-sharp r < b d > r < g! e' >
	r d' r f-sharp r a-.[ f-sharp-. d-.]
	r e_\cr r d r c-sharp r b
	r a' r g r f-sharp r e
	r e r e r g-sharp r a
	b-flat8\f r b-flat4~ b-flat8 r r4
	b!8 r b4~ b8 r r4
	c8\f[ d16. e32] c8[ d16. e32] c8 r r4
	c8[ d16. e32] c8[ d16. e32] c8 r r4
	c8[ d16. e-flat32] d8 r d8[ e16. f32] e8 r
	< a, e' >8[ < a f' >16. < a g' >32] < b f' >8 r g-sharp'8[ a16. b32] a8 r
	< e, c-sharp'! e >8\ff r < e c' e > r \grace e8( < b' e >4->) r4
	< e, c-sharp'! e >8 r < e c' e > r \grace e8( < b' e >4->) r4
	r8 \noDynamic b_\markup { \italic dim. } r4 r8 b r4
	b8 r r4 r2
	
	R1*2
	
	r8 e,8\pp[( d e]) r e[( c-sharp e])
	r f-sharp[( c-sharp f-sharp]) r f-sharp[( d f-sharp])
	r f-sharp[( c-sharp f-sharp]) r f-sharp[( d f-sharp])
	r g[( e g]) r f-sharp[( d f-sharp])
	r f[( c f]) r e[( c-sharp e])
	b4(\< c-sharp)\! d8(\> e d4)\!
	r16 b\pp[( d b]) r b[( d b]) r c-sharp[( e c-sharp]) r c-sharp[( e c-sharp])
	r c-sharp[( e c-sharp]) r c-sharp[( f-sharp c-sharp]) r b[( f-sharp' a-sharp,]) b[( c-sharp d f-sharp])
	r16 c-sharp[(_\markup { "" \raise #-1.5 \italic {poco cresc.} } f-sharp c-sharp]) r c-sharp[( f-sharp c-sharp])
		r b[( f-sharp' b,]) r b[( f-sharp' b,])
	r b[( f' b,]) r b[( f' b,]) r b[( e b]) r b[( e b])
	r c-sharp![( f-sharp c-sharp]) r c-sharp[( f-sharp c-sharp]) r d[( f-sharp d]) r d[( f-sharp d])
	r f[( a f]) r f[( a f]) r e[( a e]) c-sharp!8 r
	
	R1*2
	
	e2\p d~
	d_\markup { \italic {poco a poco cresc.} } d
	c-sharp c-sharp
	\tuplet 3/2 { r8 g-sharp'[( d] } \tuplet 3/2 { g-sharp[ d g-sharp]) } \tuplet 3/2 { r a[( f-sharp] } \tuplet 3/2 { a[ f-sharp a]) }
	\tuplet 3/2 { r b-flat[( g]) } \tuplet 3/2 { r b[( g-sharp]) } \tuplet 3/2 { r c-sharp![( g]) } \tuplet 3/2 { r d'[( b]) }
	\tuplet 3/2 { r e\mf[( c-sharp] } \tuplet 3/2 { e[ c-sharp e]) } \tuplet 3/2 { r e[( c-sharp] } \tuplet 3/2 { e[ c-sharp e]) }
	f4\mf e4~ e8[ g-.]( f-.[ f-.])
	e-flat-.[( e-flat-.]) d-.[( d-.]) c-.[( c-.]) b-flat-.[( b-flat-.])
	f'4 e!4~ e8[ g-.]( f-.[ f-.])
	e-flat-.[( e-flat-.]) d-.[( d-.]) c-.[( c-.]) b-flat-.[( b-flat-.])
	b-flat4 a~ a8[ b-flat( d f])
	a,4 g-sharp~ g-sharp8[ a( c-sharp! e])
	r8 f-sharp,!8 a'4 a8 r r4
	R1
	r2 r4 \tuplet 3/2 { c-sharp,8\f[ d e] }
	r2 r4 \tuplet 3/2 { c-sharp8[ d-sharp e] }
	r8 < a-sharp, e' > r4 r8 < b e > r4
	r8 < a e' > r4 r8 < c e > r4
	f4\fp( e) e16[( d-sharp c-sharpsharp e] d-sharp4)
	e( d!) d16[( c-sharp! b-sharp d] c-sharp4)
	d( c) c16[( b! a-sharp c] b8) r
	d4( c) c16[( b a-sharp c] b8) r
	b4_\markup { \italic {poco cresc.} } a a16[( g-sharp f-sharp g-sharp]) a4
	b4 c-sharp! e16[( d c-sharp e]) d8 d-sharp
	e8\mf r r4 r2
	
	R1*3
	
	r8 < a-sharp,, f-sharp' >16\pp[_\markup { \translate #(cons 4 -1) \italic {poco a poco cresc.} } r
		< b f-sharp' > r < b-sharp g-sharp' >] r c-sharp[ r < a-sharp f-sharp' > r < b f-sharp' > r < b-sharp g-sharp'! >] r
	c-sharp[ r < e a! > r < f-sharp a > r < d-sharp b' >] r e[ r < e a > r < f-sharp a > r < d-sharp b' >] r
	e[ r c-sharp r c-sharp r d!] r d[ r e r e r f-sharp] r
	f-sharp16\mf[ r g-sharp r f-sharp r g-sharp] r < f-sharp a >2\f\>
	f-sharp16\mf[\! r g-sharp r f-sharp r g-sharp] r < f a >2\f
	a16\mf[ r b r a r b] r c2\f\>
	c16[ r d\mf\! r c r d] r e-flat2\f\>
	e-flat16[ r f\mf\! r e-flat r f] r < a, f-sharp' >2\f
	< d! g-sharp >8\mf < d g-sharp > r < d g-sharp >[ < d g-sharp > < d g-sharp >] r < d g-sharp >
	< d a' > < d a' > r < d a' >[ < d a' > < d a' >] r < d a' >
	< d b' > < d b' > r < d b' >[ < d b' > < d b' >] r < d b' >
	< f-sharp! b-sharp > < f-sharp b-sharp > r < f-sharp b-sharp >[ < f-sharp b-sharp > < f-sharp b-sharp >] r < f-sharp b-sharp >
	
	R1*4
	
	< a, c-sharp' >8\ff r8 c-sharp'2 b16[( a c-sharp e])
	b4.( c-sharp8) b4 c-sharp
	< d,, f-sharp' d' >8 r d''2 c-sharp16[( b d f-sharp])
	c-sharp4.( d8) c-sharp4 c-sharp
	f-sharp8 g-sharp a[ g-sharp16( f-sharp] e8) g-sharp a[ f-sharp16( e]
	d8) e-sharp f-sharp[ e16( d] c-sharp8) e-sharp f-sharp[ d16( c-sharp]
	b8) c-sharp d[ c-sharp16( b] a8)[ g-sharp16( f-sharp] e-sharp)[ c-sharp( e-sharp g-sharp])
	b8 c-sharp d[ c-sharp16( b] a8)[ g-sharp16( f-sharp] e!)[ f-sharp( g-sharp b])
	< a, c-sharp' >8\ff r8 c-sharp'2 b16[( a c-sharp e])
	b4.( c-sharp8) b4 c-sharp
	< d,, f-sharp' d' >8 r d''2 c-sharp16[( b d f-sharp])
	c-sharp4.( d8) c-sharp4 c-sharp
	f-sharp8 g-sharp a[ g-sharp16( f-sharp] e8) g-sharp a[ f-sharp16( e]
	d8) e-sharp f-sharp[ e16( d] c-sharp8) e-sharp f-sharp[ d16( c-sharp]
	b-sharp8)[ c-sharp,\p]~ c-sharp[ f-sharp,]~ f-sharp r r4
	r8 c-sharp4 e8~ e16[(\< g-sharp c-sharp b-sharp]) c-sharp[( d-sharp e d-sharp])\!
	g-sharp8\mf[ c-sharp,\p]~ c-sharp[ f-sharp,]~ f-sharp r8 r4
	r8 c-sharp4 e8~ e16[(\< g-sharp c-sharp b-sharp]) c-sharp[( d-sharp e c-sharp])\!
	d-sharp8\mf[ c-sharp\p]~ c-sharp[ c-sharp,!]~ c-sharp r8 r8 e(
	d-sharp)[ c-sharp'!]~ c-sharp[ c-sharp,!]~ c-sharp r r e(
	d-sharp) a-sharp'[~ a-sharp] r r b-sharp~ b-sharp[ d-sharp](
	g-sharp)[ b,!]~ b r r e-sharp,~ e-sharp[ g-sharp](
	c-sharp) d-sharp4\< f-sharp8 b c-sharp4 e8(\!
	a\mf) r r4 r8 a,,,16\p[( b-flat c8]) r8
	r8 g'~\< g[ b-flat]~ b-flat16[( d g f-sharp]) g[( a b-flat a])\!
	d8\mf r r4 r8 a,,16\p[( b-flat c8]) r8
	r8 g'~\< g[ b-flat]~ b-flat16[( d g f-sharp]) g[( a b-flat g])\!
	a8\mf[ g]~ g[ g,]~ g r r b-flat(
	a)[ g']~ g[ g,]~ g r r b-flat(
	a)[ g]~ g r r f-sharp~ f-sharp[ a](
	d)[ f,]~ f r r b,~_\cr b[ d]
	g[ a]~ a[ c]( f)[ g]~ g[ b-flat](
	e-flat)[ f,]~ f[ g-sharp]( c-sharp!)[ d-sharp,]~ d-sharp[ f-sharp](
	b!\ff) r r4 r2
	< d, b' >8\f r r4 r2
	
	\set Staff.midiInstrument = #"pizzicato strings"
	e,8\pp^\markup {pizz.} \noDynamic r\p e r r4 e'8 r
	d r d, r r4 e8 r
	f r f r r4 f'8 r
	e r e, r r4 e8 r
	f r a r g r c r
	f, r < d a' > r e r a r
	
	\set Staff.midiInstrument = #"string ensemble 1"
	a2\p(\>^\markup {arco} g-sharp8)\! r r4
	a2^>(\> g-sharp8)\! r
		\set Staff.midiInstrument = #"pizzicato strings"
		e\pp^\markup {pizz.} r
	e8 r e r r4 e'8 r
	d r d, r r4 e8 r
	f r f r r4 f'8 r
	e r e, r r4 e8 r
	f r a r g r c r
	f, r < d a' > r e r a r
	f-sharp r r4 f-sharp8 r r4
	< e c-sharp'! >8 r r4
		\set Staff.midiInstrument = #"string ensemble 1"
		e2^\markup {arco}
	d-sharp8 r r4
		\set Staff.midiInstrument = #"pizzicato strings"
		f-sharp8^\markup {pizz.} r r4
	< e c-sharp' >8 r r4
		\set Staff.midiInstrument = #"string ensemble 1"
		e2^\markup {arco}
	e8 r r4
		\set Staff.midiInstrument = #"pizzicato strings"
		e8^\markup {pizz.} r r4
	< d a' >8 r r4
		\set Staff.midiInstrument = #"string ensemble 1"
		f2^\markup {arco}
	e8 r r4
		\set Staff.midiInstrument = #"pizzicato strings"
		e8^\markup {pizz.} r r4
	< d a' >8 r r4
		\set Staff.midiInstrument = #"string ensemble 1"
		f2\<^\markup {arco}
	f8\! r r4 r2
	f8 r r4 r2
	
	R1*2
	
	< a a' >8\ff r < a a' >2 \grace { g'16[ a] } g16[( f a c])
	g4.( a8) g4 a
	b-flat8 r b-flat2 \grace { a16[ b-flat] } a16[( g b-flat d])
	a4.( b-flat8) a4 a
	d8 e f[ e16( d] c8)[ e] f[ d16( c]
	b-flat8)[ c-sharp!] d[ c16( b] a8)[ c-sharp] d[ b-flat16( a])
	g16[ a b-flat g] f[ a b-flat f] e-flat[ f-sharp g e-flat] d[ f-sharp g d]
	c-sharp!8\ff[ a'] b-flat[ b-flat,] b[ b,!] c[ c']
	c-sharp!8 c-sharp4 d e g-sharp8
	< a, a' >[ a'] b-flat[ b-flat,] b[ b,!] c[ c']
	c-sharp!8 c-sharp4 d < d e > g-sharp8
	< a, a' >[ b-flat'] b[ b,] c[ c,] c-sharp[ c-sharp']
	d8 d4 d-sharp < b-flat e > b'!8
	c8[ b] c[ c,] c-sharp[ c-sharp,!] d[ d']
	d-sharp8 d-sharp4 < b-flat e > < b f' > c'8
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
	
	f-sharp,2.\pp f-sharp4
	e2. d4
	d2. d4
	d4. d8~ d r\pp a'4~_\markup { \italic dolce }
	a8[ b( c-sharp e]) e-sharp[( f-sharp] a,4)~
	a8[ b(_\markup { \italic {poco cresc.} } c-sharp e!]) e-sharp[( f-sharp] e4)
	d4~( \tuplet 3/2 { d8[ e f-sharp]) } b,2\<
	g-sharp16[( a b c-sharp]) d4(\! c-sharp8) r r g'!8\p
	b r r e, g r r4
	
	R1*2
	
	\set Staff.midiInstrument = #"pizzicato strings"
	< d, a' >8\pp^\markup {pizz.} r r4 r < d a' >8 r
	< e a >_\cr r r4 r < d a' >8 r
	g r r4 r g8 r
	r4
		\set Staff.midiInstrument = #"string ensemble 1"
		c-sharp,8[(^\markup {arco} f-sharp]) r4 b,8[( f-sharp'])
	r4 b,8[( e]) r4 a,8[( e'])
	r4 a,8[( d]) r4 g,8[( b])
	r4 c8[( g']) r4 c-sharp,8[( g'])
	d2_\markup { \dynamic {mf} \italic dim. } < g, e' >
	f-sharp'2~\> f-sharp8\! r8 r4
	R1
	r8 g\pp r f-sharp r g r < d a' >
	r g r b r d-.[ b-. g-.]
	r g r f-sharp r g r < d a' >
	r g r b r d-.[ b-. g-.]
	r a_\cr r g r f-sharp r e
	r d' r c r b r < e, a >
	r < e a > r < f a > r c-sharp' r d
	e-flat r e-flat4~ e-flat8 r r4
	< b-flat e! >8 r < b-flat e >4~ < b-flat e >8 r r4
	
	\set Staff.midiInstrument = #"pizzicato strings"
	< b-flat f' >8\f^\markup {pizz.} r r4 r2
	< b-flat f' >8 r r4 r2
	< b-flat f' >8_\cr r < b g' > r < c g' > r < a a' > r
	< a a' > r < d, d' b-flat' > r < g-sharp f' c-sharp'! > r < g-sharp f' d' > r
	
	\set Staff.midiInstrument = #"string ensemble 1"
	< d a' f-sharp'! d' >8\ff^\markup {arco} r < d a' f' d' > r < a' a' >4 r
	< d, a' f-sharp'! d' >8 r < d a' f' d' > r < a' a' >4 r
	r8 e8 r4 r8 e r4
	r8 e~ e4~ e8 r r4
	
	R1*2
	
	r8 a4\pp a8 r a4 a8
	r8 b4 b8 r b4 b8
	r f-sharp8\p[( d-sharp f-sharp]) r g[( e g])
	r a[( e a]) r g[( e g])
	r f[( d f]) r f-sharp[( d f-sharp])
	e4(\< f-sharp) g8[(\! a] g) r
	r16 e\pp[( g e]) r e[( g e]) r f-sharp[( a f-sharp]) r f-sharp[( a f-sharp])
	r f-sharp[( a f-sharp]) r f-sharp[( b f-sharp]) r e[( b' d-sharp,]) e[( f-sharp g b])
	r_\markup { "" \raise #-1.0 \dynamic p \italic cresc. } b,[( f-sharp' b,])
		r b[( f-sharp' b,]) r b[( e b]) r b[( e b])
	r b-flat[( e b-flat]) r b-flat[( e b-flat]) r a[( e' a,]) r a[( e' a,])
	r b![( f-sharp' b,]) r b[( f-sharp' b,]) r b[( g' b,]) r b[( g' b,])
	r b[( g-sharp' b,]) r b[( g-sharp' b,]) r c-sharp[( g-sharp' c-sharp,]) r c-sharp[( g-sharp' c-sharp,])
	r d[( g-sharp d]) r g-sharp,[(_\cr f-sharp' g-sharp,]) r g-sharp[( f-sharp' g-sharp,]) r a[( f-sharp' a,])
	g'!4\mf f-sharp!~ f-sharp8 a( b-flat) b-flat(
	a-flat)[ a-flat]( g)[ g]( f)[ f-.( e-flat-. f-.])
	g4 f-sharp!~ f-sharp8 a!( b-flat) b-flat(
	a-flat) a-flat( g) g( f) f-.( e-flat-. e-flat-.)
	e-flat4 d~ d8[ e-flat g b-flat]
	d,4 c-sharp!~ c-sharp8[ d f-sharp! a]
	r4 < d, d' >\f < d d' >8 r r4
	R1
	r2 r4 \tuplet 3/2 { f-sharp'8\f[ g a] }
	r2 r4 \tuplet 3/2 { f-sharp8[ g-sharp a] }
	r8 < a, a' >8 r4 r8 < a a' > r4
	r8 < a a' > r4 r8 < a a' > r4
	b-flat'4\pp( a) a16[( g-sharp f-sharpsharp a]) g-sharp4
	a( g!) g16[( f-sharp e-sharp g]) f-sharp4
	g4(\< f) f16[( e d-sharp f] e8)\! r
	g4(\< f) f16[( e d-sharp f] e8)\! r
	e4\mf d! d16[( c-sharp b-sharp c-sharp]) d4
	< a e' >\< < a f-sharp' > a'16[( g f-sharp a]) g8[ g-sharp]\!
	a8 r r4 r2
	
	R1*3
	
	r8\pp b,,16_\markup { \italic {poco a poco cresc.} } r b[ r c-sharp] r d[ r b r b r c-sharp] r
	d[ r d r d r e] r c-sharp[ r d r d r e] r
	c-sharp[ r < a f-sharp' > r < b f-sharp' > r g'] r < g, g' >[ r < e' a > r < f-sharp a > r < d b' >] r
	< e b' >[\< r < e c-sharp' > r < e b' > r < e c-sharp' >]\! r < g d' >2\f\>
	< e b' >16[ r\mf\! < e c-sharp' > r < e b' > r < e c-sharp' >] r < g d' >2\f\>
	d'16[ r\mf\! < d e > r d r < d e >] r < b-flat f' >2\f\>
	< b-flat f' >16[ r\mf\! < b-flat g' > r < b-flat f' > r < b-flat g' >] r < d-flat a-flat' >2\f\>
	< d-flat a-flat' >8[\! < d-flat b-flat' > < d-flat a-flat' > < d-flat b-flat' >] < d b' >2\f
	< a c-sharp' >8\mf[ < a c-sharp' >] r < a c-sharp' >[ < a c-sharp' > < a c-sharp' >] r < a c-sharp' >
	< g' d' >8[ < g d' >] r < g d' >[ < g d' > < g d' >] r < g d' >
	< g e' >[ < g e' >] r < g e' >[ < g e' > < g e' >] r < g e' >
	e-sharp'8[ e-sharp] r e-sharp[ e-sharp e-sharp] r e-sharp
	
	R1*4
	
	< d,, a' f-sharp' >8\f r f-sharp\p r f-sharp r f-sharp r
	f-sharp_\cr r e r e r d r
	d r e r f r f r
	f r r4 r b-flat8\f g-sharp
	a r r4 r a8 f-sharp
	g! r r4 r g8 e
	f r r d-sharp e r r c-sharp
	d r d'2 r4
	d,8 r d'2 r4
	d8[ d~ d d]~ d[ d~ d d]
	e-flat\f[ c-sharp->] d[ d->] e-flat[ c-sharp->] d[ d->]
	e-flat8 e-flat4 e-flat e-flat e-flat8
	< d f >8 < d f >4 < d f > < d f > < d f >8
	< d f-sharp! >8\ff r r4 r2
	d,4\p(\< e8)[ e-sharp]\! f-sharp r < g, g' >\f r
	R1
	d'4(\< e!8)[ e-sharp]\! f-sharp r < g a >\f r
	< d b-flat' > r r4 r8 < a' c-sharp' >8\ff[ < a a' > < a c-sharp' >]
	d' r r4 r8 < a, c-sharp' >8[ < a a' > < a c-sharp' >]
	d' r r < a, c-sharp' > d' r r < a, c-sharp' >
	d' r r e e-sharp r r e-sharp
	f-sharp\ff < d,, d' >4 < d d' >8~ < d d' > e'8:16[ f-sharp: g:]
	a < d,, d' >4 < d d' >8~ < d d' > e'8:16[ f-sharp: g:]
	a d4 e8 d c-sharp4 d8
	c-sharp b4 g8 b-flat-> r r < c-sharp, a' >
	< d, d' > < d d' >4 < d d' >8~ < d d' > e'8:16[ f-sharp: g:]
	a < d,, d' >4 < d d' >8~ < d d' > e'8:16[ f-sharp: g:]
	a d4 e8 d c-sharp4 d8
	c-sharp b4 g8 b-flat-> r r < c-sharp, a' >
	< d, d' > r < d d' > r < d a' f-sharp' > r < d a' a' > r
	< d a' d' > r < d d' > r < d a' f-sharp' > r < d a' a' > r
	< d a' d' > r < d d' d' > r < d d' d' > r < d d' d' > r
	< d d' d' > r < d d' d' > r < d d' d' > r < d d' d' > r
	< d d' d' >[ d f-sharp a] < d, d' >[ < d d' > < a' f-sharp' > < a a' >]
	< d, d' d' >4 < d d' d' >4 < d d' d' >4 f-sharp''
	< a,,, d >1\fermata
}
