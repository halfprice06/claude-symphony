\version "2.20.0"

theViolas =  \relative d' {
	\clef "alto"
	\key d \major
	
	r1
	R1
	
	r2 r4 a4\p
	a a a r
	
	R1*2
	
	r4 f-sharp r2
	
	R1*2
	
	< e g >1\p_\markup { \translate #(cons 4 0) \italic cresc. }
	f
	f
	< e a >\<
	c-sharp'8 r c-sharp2\mf\! \appoggiatura d8( c-sharp16)[(_\cr b c-sharp e])
	f,1\<
	g-sharp8\f\! r g-sharp2 \appoggiatura a8( g-sharp16)[( f-sharpsharp g-sharp b])
	g-sharp8 r g-sharp2 \appoggiatura a8( g-sharp16)[( f-sharpsharp g-sharp b])
	g-sharp8\ff g-sharp \appoggiatura a8( g-sharp16)[( f-sharpsharp g-sharp b])
		g-sharp8 g-sharp \appoggiatura a8( g-sharp16)[( f-sharpsharp g-sharp b])
	g-sharp8[ < b d > < b d > < b d >] < b d >[ < b d > < b d > < b d >]
	< c-sharp e > r r4 r4 r8 b8\f(
	a) r r4 r4 r8 b8\mf(
	a) r r b\p( a) r r b(
	a) r r4 r2
	
	R1*3
	
	r2 r8 r4\fermata r8
	a1\pp
	a
	g
	f-sharp2~ f-sharp8 r f-sharp4(
	e8) r e r a r f-sharp4(
	e8) r e r a r f-sharp4
	f-sharp4 b e,2
	e4\< e~ e8\! r r4
	
	R1*5
	
	\set Staff.midiInstrument = #"pizzicato strings"
	d8\p^\markup { pizz. } r r4 r d8 r
	e r r4 r4 d8 r
	d8 r r4 r d8 r
	
	\set Staff.midiInstrument = #"string ensemble 1"
	a'4.( g-sharp8 a) r f-sharp4(
	e8) r e r a r f-sharp4(
	e8) r a r a r a\< r
	f-sharp8\! r e r b' r r4
	a8 r r4 r2
	R1
	r8 e\pp r e r e r e
	r f-sharp r f-sharp r a[ f-sharp f-sharp]
	r e r e r e r e
	r f-sharp r f-sharp r a-.[ f-sharp-. f-sharp-.]
	r f-sharp_\cr r f-sharp r f-sharp r f-sharp
	r b r b r b r b
	r b r a r d r c
	d\f r b-flat4~ b-flat8 r r4
	f'8 r f4~ f8 r r4
	c8\f[ d16. e32] c8[ d16. e32] c8 r r4
	c8[ d16. e32] c8[ d16. e32] c8 r r4
	c8[ d16. e-flat32] d8 r < g, g' >8[ < g g' >16. < g g' >32] < g-sharp g-sharp' >8 r
	e'8[ f16. g!32] f8 r g-sharp8[ a16. b32] a8 r
	< e, c-sharp'! >8\ff r < e c' > r < e b' >4-> r
	< e c-sharp'! >8 r < e c' > r < e b' >4-> r
	r8 \noDynamic d'8\mf_\markup { \italic dim. } r4 r8 c-sharp r4
	d8 r r4 r2
	
	R1*2
	
	r4 b\pp r a
	r a-sharp r b
	r a-sharp r b
	r b r b
	r a r a
	d,( e) e2
	
	R1*2
	
	f-sharp1_\markup { \dynamic pp \italic {poco cresc.} }
	f2 e
	f-sharp! f-sharp
	a a4~ a8 r
	
	\tuplet 3/2 { r8 e'8\p[( e,]) } \tuplet 3/2 { e'[( e, e']) } \tuplet 3/2 { r e[( e,]) } \tuplet 3/2 { e'[( e, e']) }
	\tuplet 3/2 { r8 f-sharp8[( f-sharp,]) } \tuplet 3/2 { f-sharp'[( f-sharp, f-sharp']) } \tuplet 3/2 { r f-sharp[(
		f-sharp,]) } \tuplet 3/2 { f-sharp'[( f-sharp, f-sharp']) }
	\tuplet 3/2 { r8 f-sharp8[( f-sharp,]) } \tuplet 3/2 { f-sharp'[( f-sharp, f-sharp']) } \tuplet 3/2 { r f-sharp[(
		f-sharp,]) } \tuplet 3/2 { f-sharp'[( f-sharp, f-sharp']) }
	\tuplet 3/2 { r8_\markup { "" \raise #-4 \italic {poco a poco cresc.} } f-sharp8[( f-sharp,]) } \tuplet 3/2 { f-sharp'[(
		f-sharp, f-sharp']) } \tuplet 3/2 { r e[( e,]) } \tuplet 3/2 { e'[( e, e']) }
	\tuplet 3/2 { r e[( e,]) } \tuplet 3/2 { e'[( e, e']) } \tuplet 3/2 { r e[( e,]) } \tuplet 3/2 { e'[( e, e']) }
	\tuplet 3/2 { r b[( g-sharp] } \tuplet 3/2 { b[ g-sharp b]) } \tuplet 3/2 { r c[( a] } \tuplet 3/2 { c[ a c]) }
	\tuplet 3/2 { r e[( b-flat]) } \tuplet 3/2 { r d[( b]) } \tuplet 3/2 { r e[( c-sharp]) } \tuplet 3/2 { r f[( d]) }
	\tuplet 3/2 { r a-sharp'\mf[( e] } \tuplet 3/2 { a-sharp[ e a-sharp]) } \tuplet 3/2 { r a-sharp[( e] }
		\tuplet 3/2 { a-sharp[ e a-sharp]) }
	b-flat4\mf b-flat~ b-flat8 b-flat-.( b-flat-.[ b-.])
	g-.[( a-.]) f-.[( g-.]) e-flat-.[( d-.]) d-.[( c-.])
	b-flat'4 b-flat~ b-flat8 b-flat-.( b-flat-.[ b-.])
	g-.[( a-.]) f-.[( g-.]) e-flat-.[( d-.]) d-.[( c-.])
	c4 c~ c8[ d( f b-flat])
	b,!4 b~ b8[ c-sharp!( e a])
	r8 a, a'4 a8 r r4
	R1
	r2 r4 \tuplet 3/2 { c-sharp,8\f[ d e] }
	r2 r4 \tuplet 3/2 { c-sharp8[ d-sharp e] }
	r8 e r4 r8 e r4
	r8 e r4 r8 e r4
	f2\f f-sharp
	e e
	d4 e f~ f8 r
	d4 e f~ f8 r
	g-sharp,4_\markup { \italic {poco cresc.} } a d c
	b c-sharp! c-sharp16[( d e c-sharp]) b8 b-sharp
	c-sharp8\mf r r4 r2
	
	R1*3
	
	r8 f-sharp,16\pp[_\markup { \translate #(cons 4 -1) \italic {poco a poco cresc.} } r f-sharp r g-sharp] r
		a[ r f-sharp r f-sharp r g-sharp] r
	a[ r e r f-sharp r f-sharp] r g-sharp[ r e r f-sharp r f-sharp] r
	g-sharp[ r e r f-sharp r f-sharp] r g-sharp[ r g-sharp r a r a] r
	b16\mf[ r b r b r b] r f-sharp2\f\>
	b16\mf[\! r b r b r b] r f2\f
	a'16\mf[ r a r a r a] r a2\f\>
	f16\mf[\! r f r f r f] r e-flat2\f\>
	e-flat16\mf[\! r e-flat r e-flat r e-flat] r d-sharp2\f
	< b-flat d >8\mf < b-flat d > r < b-flat d >[ < b-flat d > < b-flat d >] r < b-flat d >
	< a d > < a d > r < a d >[ < a d > < a d >] r < a d >
	< d a' > < d a' > r < d a' >[ < d a' > < d a' >] r < d a' >
	< f-sharp! a > < f-sharp a > r < f-sharp a >[ < f-sharp a > < f-sharp a >] r < f-sharp a >
	
	R1*4
	
	< c-sharp e a >8\ff r c-sharp2 b16[( a c-sharp e])
	b4.( c-sharp8) b4 c-sharp
	< b d >8 r d2 c-sharp16[( b d f-sharp])
	c-sharp4.( d8) c-sharp4 c-sharp
	f-sharp8 g-sharp a[ g-sharp16( f-sharp] e8) g-sharp a[ f-sharp16( e]
	d8) e-sharp f-sharp[ e16( d] c-sharp8) e-sharp f-sharp[ d16( c-sharp]
	b8) c-sharp d[ c-sharp16( b] a8)[ g-sharp16( f-sharp] e-sharp)[ c-sharp( e-sharp g-sharp])
	b8 c-sharp d[ c-sharp16( b] a8)[ g-sharp16( f-sharp] e!)[ f-sharp( g-sharp b])
	< c-sharp e a >8\ff r8 c-sharp2 b16[( a c-sharp e])
	b4.( c-sharp8) b4 c-sharp
	< b d >8 r d2 c-sharp16[( b d f-sharp])
	c-sharp4.( d8) c-sharp4 c-sharp
	f-sharp8 g-sharp a[ g-sharp16( f-sharp] e8) g-sharp a[ f-sharp16( e]
	d8) e-sharp f-sharp[ e16( d] c-sharp8) e-sharp f-sharp[ d16( c-sharp]
	b-sharp8)[ d-sharp\p]~ d-sharp[ d-sharp]~ d-sharp r r4
	r4 r8 e8~ e[\< e16( d-sharp]) c-sharp8\! r
	r8 d-sharp\p[~ d-sharp d-sharp]~ d-sharp r r4
	r4 r8 e8~ e[\< e16( d-sharp]) c-sharp8\! r
	r f-sharpsharp\mf~ f-sharpsharp r r a-sharp,16[( b] c-sharp8)[ g-sharp](
	a-sharp)[ f-sharpsharp']~ f-sharpsharp r r a-sharp,16[( b] c-sharp8)[ g-sharp](
	a-sharp)[ f-sharpsharp']~ f-sharpsharp r r d-sharp~ d-sharp r
	r e-sharp~ e-sharp r r e-sharp,~ e-sharp r
	r f-sharp'~\< f-sharp[ f-sharp] b, c-sharp4 e8(\!
	a\mf) c4 < d, a' >8~ < d a' > r r4
	r4 r8 b-flat8\p~\< b-flat[ b-flat'16( a]) g4\!
	< f-sharp a >8\mf c'4\p < d, a' >8~ < d a' > r r4
	r4 r8 b-flat~\< b-flat[ b-flat'16( a]) g8\! r
	r a\mf~ a[ d,]~ d r r d(
	e)[ a]~ a[ d,]~ d r r d(
	e)[ c-sharp]~ c-sharp r r f-sharp,~ f-sharp r
	r b~ b r r d,~_\cr d[ d]
	g[ c]~ c r r g~ g[ b-flat](
	e-flat)[ f,]~ f[ g-sharp]( c-sharp!)[ d-sharp,]~ d-sharp[ f-sharp](
	b!\ff) r r4 r2
	< b f' >8\f r r4 r2
	
	\set Staff.midiInstrument = #"pizzicato strings"
	g8\pp^\markup {pizz.} \noDynamic r\p g r r4 g'8 r
	g r g, r r4 a8 r
	a r a r r4 a'8 r
	< e a > r a, r r4 a8 r
	a r c r g r c r
	a r a r a r a r
	
	\set Staff.midiInstrument = #"string ensemble 1"
	d2\p(\>^\markup {arco} b8)\! r r4
	d2^>(\> b8)\! r
		\set Staff.midiInstrument = #"pizzicato strings"
		g-sharp\pp^\markup {pizz.} r
	g!8 r g r r4 g'8 r
	g r g, r r4 a8 r
	a r a r r4 a'8 r
	< e a > r a, r r4 a8 r
	a r c r g r c r
	a r a r a r a r
	a r r4 a8 r r4
	< g g' >8 r r4
		\set Staff.midiInstrument = #"string ensemble 1"
		g2^\markup {arco}
	f-sharp8 r r4
		\set Staff.midiInstrument = #"pizzicato strings"
		a8^\markup {pizz.} r r4
	< g g' >8 r r4
		\set Staff.midiInstrument = #"string ensemble 1"
		g2^\markup {arco}
	g8 r r4
		\set Staff.midiInstrument = #"pizzicato strings"
		g8^\markup {pizz.} r r4
	f8 r r4
		\set Staff.midiInstrument = #"string ensemble 1"
		a2^\markup {arco}
	a8 r r4
		\set Staff.midiInstrument = #"pizzicato strings"
		g8^\markup {pizz.} r r4
	f8 r r4
		\set Staff.midiInstrument = #"string ensemble 1"
		a2\<^\markup {arco}
	b8\! r r4 r2
	b8 r r4 r2
	
	R1*2
	
	a8\ff r a2 \grace { g16[ a] } g16[( f a c])
	g4.( a8) g4 a
	b-flat8 r b-flat2 \grace { a16[ b-flat] } a16[( g b-flat d])
	a4.( b-flat8) a4 a
	d8 e f[ e16( d] c8)[ e] f[ d16( c]
	b-flat8)[ c-sharp!] d[ c16( b] a8)[ c-sharp] d[ b-flat16( a])
	g16[ a b-flat g] f[ a b-flat f] e-flat[ f-sharp g e-flat] d[ f-sharp g d]
	c-sharp!8\ff r e4( f) f-sharp(
	g8) e'4 d d g-sharp8
	< e a > r e,4( f) f-sharp(
	g8) e'4 d d g-sharp8
	< e a > r f,4( f-sharp) g(
	g-sharp8) f'4 d-sharp e b8
	c r f-sharp,!4( g!) g-sharp(
	a8) d-sharp4 a-sharp b b-sharp8
	c-sharp![ b-sharp] c-sharp[ c-sharp] d![ d] d-sharp[ d-sharp]
	e[ e] f[ f] f-sharp[ f-sharp] g[ g]
	g-sharp8\ff[ f16( g!] g-sharp8)[ f16( g] g-sharp8)[ f16( g] g-sharp8)[ f16( g]
	g-sharp8)[ f16( g] g-sharp8)[ f16( g] g-sharp8)[ f16( g] g-sharp8)[ g16( g-sharp]
	a8) r r4 r r8 f16[( g!]
	g-sharp8)[ f16( g] g-sharp8)[ f16( g] g-sharp8)[ f16( g] g-sharp8)[ g16( g-sharp]
	a8) r r4 r r8 f16[( g!]
	g-sharp8)[ f16( g] g-sharp8)[ f16( g] g-sharp8)[ f16( g] g-sharp8)[ g16( g-sharp]
	a8) r r4 r2
	
	s1*46
	
	a,2.\pp a4
	a2. a4
	g2. g4
	f-sharp4. f8( f-sharp) r\pp f-sharp4(
	e8) r e r a r f-sharp4(
	e8) r_\markup { \italic {poco cresc.}} e r a[( d]) f-sharp,4
	f-sharp4 b e,2\<
	e4 e~\! e8 r r4
	
	R1*3
	
	\set Staff.midiInstrument = #"pizzicato strings"
	d8\pp^\markup {pizz} r r4 r d8 r
	c-sharp_\cr r r4 r c8 r
	g' r r4 r g8 r
	r
		\set Staff.midiInstrument = #"string ensemble 1"
		f-sharp4.^\markup {arco} r8 f-sharp4.
	r8 e4. r8 e4.
	r8 d4. r8 d4.
	r8 g4. r8 g4.
	g2_\markup { \dynamic {mf} \italic {dim.} } a
	a2~\> a8\! r r4
	R1
	r8 a\pp r a r c-sharp r c
	r b r b r d-.[ b-. b-.]
	r a r a r c-sharp! r c
	r b r b r d-.[ b-. b-.]
	r b_\cr r b r b r b
	r e r e r e r e
	r a, r a r a r a
	e-flat' r e-flat4~ e-flat8 r r4
	e!8 r e4~ e8 r r4
	
	\set Staff.midiInstrument = #"pizzicato strings"
	< b-flat f' >8\f^\markup {pizz.} r r4 r2
	< b-flat f' >8 r r4 r2
	< b-flat f' >8_\cr r < b g' > r < c g' > r < c-sharp g' > r
	g' r g r g-sharp r g-sharp r
	
	\set Staff.midiInstrument = #"string ensemble 1"
	< a, f-sharp' a >8\ff^\markup {arco} r < a f' a > r e'4-> r
	< a, f-sharp'! a >8 r < a f' a > r e'4-> r
	r8 g, r4 r8 g r4
	r8 g~ g4~ g8 r r4
	
	R1*4
	
	r4 d-sharp'\p r e
	r e r e
	r d r d
	g,(\< a) a~\! a8 r
	
	R1*2
	
	r8\p b_\cr r b r b r b
	r b-flat r b-flat r a r a
	r b\pp r b r b r b
	r b r b r c-sharp r c-sharp
	r d r g-sharp,_\cr r g-sharp r a
	b-flat4\mf c4~ c8[ f-sharp!]( g)[ g](
	f)[ f]( e-flat)[ e-flat]( d)[ a-flat-.( g-. a-.])
	b-flat4 c~ c8[ f-sharp!]( g)[ g](
	f)[ f]( e-flat)[ e-flat]( d)[ a-flat]( g-.[ f-.])
	f4 f~ f8[ g b-flat e-flat]
	e,!4 e~ e8[ f-sharp! a d]
	r8 f,\f f4 f-sharp8 r r4
	R1
	r2 r4 \tuplet 3/2 { < d' f-sharp >8\f[ < d f-sharp > < d f-sharp >] }
	r2 r4 \tuplet 3/2 { < d f-sharp >8[ < d f-sharp > < d f-sharp >] }
	r8 < d-sharp f-sharp > r4 r8 e r4
	r8 < d! f >8 r4 r8 < c f! >8 r4
	
	R1*4
	
	c-sharp4\mf d a a
	a\< < a f-sharp' > f-sharp'16[( g a f-sharp]) e8[ e-sharp]\!
	f-sharp8 r r4 r2
	
	R1*3
	
	r8\pp f-sharp,16_\markup { \italic {poco a poco cresc.}} r g[ r e-sharp] r
		f-sharp[ r f-sharp r g r e-sharp] r
	f-sharp[ r f-sharp r g r g-sharp] r e[ r f-sharp r g r g-sharp] r
	e[ r f-sharp r f-sharp r g] r c-sharp[ r a r a r b] r
	< e, g >[\< r < e g > r < e g > r < e g >]\! r < d b' >2\f\>
	< e g >16[ r\mf\! < e g > r < e g > r < e g >] r < d b-flat' >2\f\>
	< g d' >16[ r\mf\! < g e' > r < g d' > r < g e' >] r < b-flat d >2\f\>
	< b-flat d >16[ r\mf\! < b-flat d > r < b-flat d > r < b-flat d >] r a-flat2\f\>
	< a-flat a-flat' >8[\! < a-flat a-flat' > < a-flat a-flat' > < a-flat a-flat' >] < a-flat a-flat' >2\f
	< c-sharp! g'! >8\mf[ < c-sharp g' >] r < c-sharp g' >[ < c-sharp g' > < c-sharp g' >] r < c-sharp g' >
	< d b-flat' >8[ < d b-flat' >] r < d b-flat' >[ < d b-flat' > < d b-flat' >] r < d b-flat' >
	< d g >8[ < d g >] r < d g >[ < d g > < d g >] r < d g >
	< d b'! >[ < d b' >] r < d b' >[ < d b' > < d b' >] r < d b' >
	
	R1*4
	
	< d, a' f-sharp' d' >8\f r a'\p r a-sharp r b r
	b_\cr r b r a r a r
	a r a r a r a r
	b-flat r r4 r b-flat8\f[ b]
	a r r4 r a8[ a]
	g r r4 r g8[ g]
	f r r f-sharp e r r e
	d r < a' d >2 r4
	d,8 r < a' d >2 r4
	a-flat'8[ a-flat~ a-flat a-flat]~ a-flat[ a-flat~ a-flat a-flat]
	e-flat\f[ e->] d[ f->] e-flat[ e->] d[ f->]
	e-flat8 e-flat4 e-flat e-flat e-flat8
	< b f' >8 < b f' >4 < b f' > < b f' > < b f' >8
	< a f-sharp'! >\ff[ c\p](^\< b[ a]) g-sharp[( g] f-sharp[ e])
	d4( e8)[ e-sharp]^\! f-sharp8 r e\f r
	d'[(^\< c] b[ a]) g-sharp[( g] f-sharp[ e])
	d4( e8)[ e-sharp]^\! f-sharp8 r e-sharp!\f r
	g r r4 r8 c-sharp\ff[ c-sharp c-sharp]
	< g g' > r r4 r8 c-sharp[ c-sharp c-sharp]
	< g g' > r r c-sharp < g g' > r r c-sharp
	< g g' > r r < d' b-flat' > < d b' > r r < d b' >
	< d a' >\ff[ < d d' >]~ < d d' >[ < d d' >]~ < d d' > < d d' >:16[ < d d' >: < d d' >:]
	< d d' >[ < d d' >]~ < d d' >[ < d d' >]~ < d d' > < d d' >:16[ < d d' >: < d d' >:]
	< d d' > d4 e8 d c-sharp4 d8
	d b4 g8 b-flat-> r r < g' a >
	< f-sharp a > < d d' >4 < d d' >8~ < d d' > < d d' >:16[ < d d' >: < d d' >:]
	< d d' >8[ < d d' >]~ < d d' >[ < d d' >]~ < d d' > < d d' >:16[ < d d' >: < d d' >:]
	< d d' >8 d4 e8 d c-sharp4 d8
	d b4 g8 b-flat-> r r < g' a >
	< f-sharp a >8 r < b, d > r < a d > r < a f-sharp' a > r
	< a f-sharp' a > r < b d > r < a d > r < a f-sharp' a > r
	< a f-sharp' a > r < b f-sharp' > r < a f-sharp' a > r < b f-sharp' > r
	< a f-sharp' a > r < b f-sharp' > r < a f-sharp' a > r < b f-sharp' > r
	< a f-sharp' a >[ f-sharp < a d > < a d >] < a f-sharp' >[ < a f-sharp' > < a f-sharp' > < a f-sharp' >]
	< a f-sharp' >4 < a f-sharp' > < a f-sharp' > < a f-sharp' >
	f-sharp1\fermata
}
