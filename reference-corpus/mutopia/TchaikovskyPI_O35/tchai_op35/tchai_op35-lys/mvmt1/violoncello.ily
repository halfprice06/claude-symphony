\version "2.20.0"

theCellos =  \relative c {
	\clef "bass"
	\key d \major
	
	r1
	R1
	
	r2 r4 d\p
	c-sharp d a r
	R1
	r4 a( b c-sharp)
	r4 b r2
	R1
	a2:8\p a2:
	a2: a2:_\cr
	a2: a2:
	a2: a2:
	a2: a2:
	a2:\mf a2:
	a2:\< a2:
	a2:\f\! a2:
	a2: a2:
	a4\ff r a r
	a2: a2:
	a8 r r4 r r8 e'8\f(
	< e a >) r r4 r4 r8 e8\mf(
	< e a >) r r e8\p( < e a >) r r e(
	< e a >) r r4 r2
	
	R1*3
	
	r2 r8 r4\fermata r8
	
	\set Staff.midiInstrument = #"pizzicato strings"
	a,8[^\markup { pizz. } d, a' d] a' r r4
	a,8[ d, a' d] a' r r4
	g,8[ d g d'] g r r4
	g,8[ d g d'] f-sharp r
		\set Staff.midiInstrument = #"string ensemble 1"
		f-sharp^\markup { arco } r
	c-sharp r a r d r f-sharp r
	c-sharp r a r d r c-sharp4
	b e d2
	c-sharp4\< b( a8)\! r8 r4
	
	R1*5
	
	\set Staff.midiInstrument = #"pizzicato strings"
	a8\p[^\markup { pizz. } a d a'] d r a, r
	a8[ a e' a] e' r a,, r
	g[ g] d'[ g] d' r g,, r
	< a d >[ a] d r r4
		\set Staff.midiInstrument = #"string ensemble 1"
		f-sharp8^\markup {arco} r
	c-sharp r a r d r f-sharp r
	c-sharp r a r d r d\< r
	d-sharp\! r e r e r r4
	e8 r r4 r2
	R1
	r8 a,\pp r a r a r a
	r a r a r a r a
	r a r a r a r a
	r a r a r a r a
	r a-sharp_\cr r b r c-sharp r d
	r d-sharp r e r f-sharp r g
	r g-sharp r a r b r c
	d\f r d,4~ d8 r8 r4
	d-flat'8 r d-flat,4~ d-flat8 r r4
	c8\f r c r c r r4
	c8 r c r c r r4
	< f a >8[ < f a >16. < f a >32] < f-sharp a >8 r d'8[ e16. f32] e8 r
	a,8[ a16. a32] g-sharp8 r c8[ c16. c32] c8 r
	< e, a >8\ff r < e a > r < e a >8->[( g-sharp]) r4
	< e a >8 r < e a > r < e a >8->[( g-sharp]) r4
	r8 \noDynamic e\mf_\markup { \italic dim. } r4 r8 e r4
	e8 r r4 r2
	
	R1*2
	
	\set Staff.midiInstrument = #"pizzicato strings"
	e4\pp^\markup { pizz. } r e r
	e r e r
	e r d r
	c-sharp r d r
	d-sharp r e r
	
	\set Staff.midiInstrument = #"string ensemble 1"
	d!4(\<^\markup { arco } c-sharp)\! c-sharp8(\> b g-sharp4)\!
	r2 a8\pp[( c-sharp e a])
	g!4( f-sharp8 e) d[( c-sharp d f-sharp])
	e2_\markup { \italic {poco cresc.} } d
	d d
	c-sharp b
	d-sharp e4~ e8 r
	
	\set Staff.midiInstrument = #"pizzicato strings"
	e4\p^\markup { pizz. } r e r
	e r d r
	c-sharp r b r
	a_\markup { \italic {poco a poco cresc.} } r g-sharp r
	g! r f-sharp r
	f' r e-flat r
	c-sharp! b! a-sharp g-sharp
	f-sharp\mf r
		\set Staff.midiInstrument = #"string ensemble 1"
		f-sharp'2^\markup {arco}
	f4\mf f4~ f8[ f-.]( f-.[ f-.])
	f-.[( f-.]) f-.[( f-.]) f-.[( f-sharp-.]) g-.[( g-flat-.])
	f4 f4~ f8[ f-.]( f-.[ f-.])
	f-.[( f-.]) f-.[( f-.]) f-.[( f-sharp-.]) g-.[( g-.])
	r8 g-flat4 f r8 r4
	r8 f4 e! r8 r4
	r8 d-sharp8 d-sharp4 e8 r r4
	R1
	r2 r4 \tuplet 3/2 { e8\f[ e e] }
	r2 r4 \tuplet 3/2 { f-sharp8[ f-sharp f-sharp] }
	r8 f-sharpsharp r4 r8 g-sharp r4
	r8 a r4 r8 b-flat r4
	a8\f r r4 a8\p r r4
	g-sharp8 r r4 g8 r r4
	f8 r e r d r r4
	f8 r e r d r r4
	d4_\markup { \italic {poco cresc.} } c b a
	g-sharp g f-sharp f-sharp'8 f
	e\mf r r4 r2
	
	R1*3
	
	r8 e16\pp[_\markup { \translate #(cons 4 -1) \italic {poco a poco cresc.} } r e r e]
		r e[ r e r e r e] r
	e[ r < e a > r < e a > r e] r e[ r < e a > r < e a > r e] r
	e[ r e r e r e] r e[ r e r e r e] r
	e\mf[ r e r e r e] r d2\f\>
	e16\mf[\! r e r e r e] r d2\f
	d'16\mf[ r d r d r d] r c2\f\>
	c16\mf[\! r c r c r c] r c2\f\>
	c16\mf[\! r c r c r c] r b2\f
	e8\mf e r e[ e e] r e
	f f r f[ f f] r f
	f, f r f[ f f] r f
	< d b-sharp' > < d b-sharp' > r < d b-sharp' >[ < d b-sharp' > < d b-sharp' >] r < d b-sharp' >
	
	R1*4
	
	< a e' c-sharp' >8\ff r8 c-sharp'2 b16[( a c-sharp e])
	e,4 r d c-sharp
	b8 r d'2 c-sharp16[( b d f-sharp]) f-sharp,4 r8 d'8( c-sharp) r e,4
	d8 r r4 c-sharp8 r r4
	< b f-sharp' d' >8 r r4 < a f-sharp' c-sharp' >8 r r4
	g-sharp8 r r4 d'8 r c-sharp r
	g-sharp8 r r4 d'8 r e r
	< a, e' c-sharp' >8\ff r8 c-sharp'2 b16[( a c-sharp e])
	e,4 r d c-sharp
	b8 r d'2 c-sharp16[( b d f-sharp]) f-sharp,4 r8 d'8( c-sharp) r e,4
	d8 r r4 c-sharp8 r r4
	< b f-sharp' d' >8 r r4 < a f-sharp' c-sharp' >8 r r4
	g-sharp8 r r4 r8 d-sharp'16\p[( e] f-sharp8)[ a-sharp,16( b-sharp]
	c-sharp8)[ e16( d-sharp] e8)[ b16( a-sharp] c-sharp8)[\< g-sharp a! f-sharpsharp]\!
	
	g-sharp8\mf r r4 r8 d-sharp'16\p[( e] f-sharp8)[ a-sharp,16( b-sharp]
	c-sharp8)[ e16( d-sharp] e8)[ c-sharp16( b-sharp] c-sharp8)[\< g-sharp a! g-sharp]\!
	f-sharpsharp8\mf r r g-sharp'8~ g-sharp[ a-sharp,16( b] c-sharp8)[ a-sharp16( g-sharp]
	f-sharpsharp8) r r g-sharp'8~ g-sharp[ a-sharp,16( b] c-sharp8)[ a-sharp16( g-sharp]
	f-sharpsharp8)[ d-sharp'']~ d-sharp r r f-sharp,!16[( g-sharp] a!8)[ g-sharp16( f-sharp]
	e-sharp8)[ c-sharp']~ c-sharp r8 r b,16[( c-sharp] d!8)[ c-sharp16( b]
	a!8) a'16[( b] c8)[\< b16( a] g!8)[ g16( a] b-flat8)[ a16( g]\!
	f-sharp8\mf) r8 r4 r8 a,16\p[( b-flat] c8)[ e16( f-sharp]
	g8)[ b-flat16(\< a] b-flat8)[ g16( f-sharp] g8)[ d] e-flat[ c-sharp]\!
	d8\mf r8 r4 r8 a16\p[( b-flat] c8)[ e16( f-sharp]
	g8)[ b-flat16(\< a] b-flat8)[ g16( f-sharp] g8)[ d] e-flat[ d]\!
	c-sharp8\mf r8 r4 r8 e16[( f-sharp] g8)[ e16( d]
	c-sharp8) r r4 r8 e16[( f-sharp] g8)[ e16( d]
	c-sharp8)[ a']~ a r r8 c,16[( d] e-flat8)[ d16( c]
	b8)[ g'8]~ g r r8 f16[(_\cr g] a-flat8)[ g16( f]
	e-flat8)[ e-flat16( f] g-flat8)[ f16( e-flat] d8)[ d-flat16( e-flat!] f-flat8)[ e-flat16( d-flat]
	c8)[ b!16( c-sharp] d8)[ c-sharp16( b] a!8)[ a16( b] c8)[ b16( a]
	g-sharp8\ff) r r4 r2
	< g! g'! >8\f r r4 r2
	
	\set Staff.midiInstrument = #"pizzicato strings"
	c-sharp8\pp^\markup {pizz.} r c-sharp r r4 c'8 r
	g r < g, d' > r r4 e'8 r
	d r d r r4 d'8 r
	a r a, r r4 g'8 r
	f r f r e r e r d r d r c r c r
	b\p r r4 e8 r r4
	b8 r r4 e8 r d\pp r
	c r c r r4 c'8 r
	g r < g, d' > r r4 e'8 r
	d r d r r4 d'8 r
	a r a r r4 g8 r
	f r f r e r e r
	d r d r c r c r
	b r r4 b8 r r4
	b8 r r4
		\set Staff.midiInstrument = #"string ensemble 1"
		b2^\markup {arco}
	b8 r r4
		\set Staff.midiInstrument = #"pizzicato strings"
		b8^\markup {pizz.} r r4
	b8 r r4
		\set Staff.midiInstrument = #"string ensemble 1"
		b2^\markup {arco}
	a8 r r4
		\set Staff.midiInstrument = #"pizzicato strings"
		a8^\markup {pizz.} r r4
	< a d >8 r r4
		\set Staff.midiInstrument = #"string ensemble 1"
		a2^\markup {arco}
	a8 r r4
		\set Staff.midiInstrument = #"pizzicato strings"
		a8^\markup {pizz.} r r4
	< a d >8 r r4
		\set Staff.midiInstrument = #"string ensemble 1"
		a2\<^\markup {arco}
	g-sharp8\! r r4 r2
	
	R1*3
	
	< c, c' >4\ff r r2
	< c c' >4 r b-flat' a
	g r r2
	d'4 r d c
	< b-flat f' d' >8 r r4 < a f'! c' >8 r r4
	< g d' b-flat' >8 r r4 < f d' a' >8 r f' r
	e-flat r d r c r b-flat r
	a\ff r c-sharp!4( d) d-sharp(
	e8)[ a] b-flat[ e,] f[ b-flat,] b[ e,]
	a r c-sharp!4( d) d-sharp(
	e8)[ a] b-flat[ e,] f[ b-flat,] b[ e,]
	a8 r d!4( d-sharp) e(
	f8)[ b!] c[ f,] f-sharp[ c] c-sharp[ g-sharp]
	a r d-sharp!4( e) e-sharp(
	f-sharp!8)[ b!] c[ f,] g![ c-sharp,!] d![ g-sharp,]
	a1~
	a~
	a8\ff r < a d a' >8 r < a d a' >8 r < a d a' >8 r
	< a d a' >8 r < a d a' >8 r < a d a' >8 r < a d a' >8 r
	< a d a' >8 r r4 r2
	< a d a' >8 r < a d a' >8 r < a d a' >8 r < a d a' >8 r
	< a d a' >8 r r4 r2
	< a d a' >8 r < a d a' >8 r < a d a' >8 r < a d a' >8 r
	< a d a' >8 r r4 r2
	
	s1*46
	
	\set Staff.midiInstrument = #"pizzicato strings"
	d8\pp[^\markup {pizz.} d,] a'[ d] a'[ d,] d r
	r d,[ a' e'] a[ d,] d r
	r d,[ g d'] g[ d] d r
	r d, a' r r4
		\set Staff.midiInstrument = #"string ensemble 1"
		f-sharp'8\pp^\markup {arco} r
	c-sharp r a r d r f-sharp r
	c-sharp r_\markup { \italic {poco cresc.}} a r d r c-sharp4
	b e d2\<
	c-sharp4 b(\! a8) r r4
	
	R1*3
	
	\set Staff.midiInstrument = #"pizzicato strings"
	a8\pp[^\markup {pizz.} a d a'] d r a, r
	a[ a] e'[ a] e'_\cr r a,, r
	b[ d] g[ b] d r b, r
	a-sharp4 r a r
	g-sharp r g r
	f-sharp r f r
	e e' e-flat r
	
	\set Staff.midiInstrument = #"string ensemble 1"
	d2^\markup {arco}_\markup { \dynamic {mf} \italic {dim.} } d
	d2~\> d8\! r r4
	R1
	r8 d\pp r d r < d a' > r < d a' >
	r d r d r d-.[ d-. d-.]
	r d r d r < d a' > r < d a' >
	r d r d r d-.[ d-. d-.]
	r d-sharp_\cr r e r f-sharp r g
	r g-sharp r a r b r c
	r c-sharp! r d r e r f
	g, r g4~ g8 r r4
	g-flat8 r g-flat4~ g-flat8 r r4
	
	\set Staff.midiInstrument = #"pizzicato strings"
	f8\f^\markup {pizz.} r r4 r2
	f8 r r4 r2
	f8_\cr r f r e r e-flat r
	d r d r b r b-flat r
	
	\set Staff.midiInstrument = #"string ensemble 1"
	< a f-sharp' d' >8\ff^\markup {arco} r < a f' d' > r d'( c-sharp) r4
	< a, f-sharp' d' >8 r < a f' d' > r d'( c-sharp) r4
	r8 a,8 r4 r8 a r4
	r8 a8~ a4~ a8 r r4
	
	R1*2
	
	\set Staff.midiInstrument = #"pizzicato strings"
	a'4\pp^\markup {pizz.} r a r
	a r a r
	a\p r g r
	f-sharp r g r
	g-sharp r a r
	
	\set Staff.midiInstrument = #"string ensemble 1"
	g!4(\<^\markup {arco} f-sharp) e8[(\! d] c-sharp) r
	b4\pp a2.~
	a1
	a'2_\markup { \dynamic p \italic cresc. } g
	g g
	f-sharp\pp e
	d c-sharp
	b4 b2_\cr b4
	b-flat1\mf~
	b-flat2~ b-flat8[ b-.( c-. c-flat-.])
	b-flat1~
	b-flat2~ b-flat8[ b-.]( c-.[ c-.])
	r8 c-flat4 b-flat8~ b-flat[ b-flat b-flat b-flat]
	r8 b-flat4 a!8~ a[ a a a]
	r8 < g-sharp d' >8\f < d' b' >4 < d a' >8 r r4
	R1
	r2 r4 \tuplet 3/2 { a'8\f[ a a] }
	r2 r4 \tuplet 3/2 { b8[ b b] }
	r8 b-sharp r4 r8 c-sharp8 r4
	r8 d, r4 r8 e-flat r4
	d2\pp d
	c-sharp! c
	b-flat4\< a g8[ g']~ g\! r
	b-flat,4\< a g8[ g']~ g\! r
	g4\mf f e d
	c-sharp\< c b b'8[ b-flat]\!
	a8 r r4 r2
	
	R1*3
	
	r8\pp d-sharp,16_\markup { \italic {poco a poco cresc.}} r16  e[ r a,] r a[ r d-sharp r e r a,] r
	a[ r a r a r a] r a[ r a r a r a] r
	a[ r a r a r a] r a[ r a r a r a] r
	a[\< r a r a r a]\! r < g g' >2\f\>
	a16[ r\mf\! a r a r a] r < g g' >2\f\>
	b-flat'16[ r\mf\! b-flat r b-flat r b-flat] r f2\f\>
	f16[ r\mf\! f r f r f] r f2\f\>
	f8[\! f f f] e2\f
	< e a >8\mf[ < e a >] r < e a >[ < e-flat a > < e-flat a >] r < e-flat a >
	< d b-flat' >[ < d b-flat' >] r < d b-flat' >[ < d b-flat' > < d b-flat' >] r < d b-flat' >
	b-flat[ b-flat] r b-flat[ b-flat b-flat] r b-flat
	g[ g] r g[ g g] r g
	
	R1*4
	
	< d a' f-sharp' d' >8\f r d'\p r c-sharp r b r
	a'_\cr r g-sharp r g r f-sharp r
	f r e r d r e-flat r
	d r r4 r d8\f[ d]
	c-sharp r r4 r c-sharp8[ c]
	b r r4 r b8[ b-flat]
	a r r a g-sharp r r g
	f-sharp r f-sharp4 f-sharp'8[( d a f-sharp])
	f r f4 f'8[( d a f])
	f'8[ f~ f f]~ f[ f~ f f]
	g\f[ g->] f-sharp![ a-flat->] g[ g->] f-sharp[ a-flat->]
	g8 g4 g g g8
	g-sharp8 g-sharp4 g-sharp g-sharp g-sharp,8
	<< { a1^> } \\ { s2\p s2_\cr } >>
	d8[(\< c] b)[ b-flat]\! a r a\f r
	<< { a1\p } \\ { s2 s2_\cr } >>
	d8[(\< c] b)[ b-flat]\! a r a\f r
	g r r4 r8 a'8\ff[ a a]
	g r r4 r8 a[ a a]
	g r r a g r r a
	g r r g g r r g
	d\ff[ d' c-sharp b] b-flat4 a8[ g]
	f-sharp[ d' c-sharp b!] b-flat4 a8[ g]
	f-sharp[ e-sharp f-sharp g] g-sharp[ a a-sharp b]
	c-sharp[ d d-sharp e] e-flat-> r r a,
	< d, a' >[ d' c-sharp b] b-flat4 a8[ g]
	f-sharp[ d' c-sharp b!] b-flat4 a8[ g]
	f-sharp[ e-sharp f-sharp g] g-sharp[ a a-sharp b]
	c-sharp[ d d-sharp e] e-flat-> r r a,
	< d, a' > r b' r a r < f-sharp a > r
	< d a' > r b' r a r < f-sharp a > r
	< d a' > r b r < d a' > r b r
	< d a' > r b r < d a' > r b r
	d[ d d d] d[ d d d]
	< d, a' f-sharp' d' >4 < d a' f-sharp' d' > < d a' f-sharp' d' > < d a' f-sharp' d' >
	d'1\fermata
}
