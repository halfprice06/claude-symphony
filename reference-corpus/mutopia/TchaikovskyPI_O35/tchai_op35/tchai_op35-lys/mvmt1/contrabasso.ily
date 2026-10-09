\version "2.20.0"

theBass =  \relative d {
	\clef "bass"
	\key d \major
	
	r1
	R1
	
	r2 r4 d\p
	c-sharp d a r
	R1
	r4 a'( g f-sharp)
	r4 b, r2
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
	a) r r4 r4 r8 e8\mf(
	a) r r e8\p( a) r r e(
	a) r r4 r2
	
	R1*3
	
	r2 r8 r4\fermata r8
	
	\set Staff.midiInstrument = #"pizzicato strings"
	d,8\pp^\markup { pizz. } r r4 r2
	d8 r r4 r2
	d8 r r4 r2
	d8 r r4 r4
		\set Staff.midiInstrument = #"string ensemble 1"
		f-sharp8^\markup { arco } r8
	c-sharp8 r a r d r f-sharp r
	c-sharp r a r d r c-sharp4
	b e d2
	c-sharp4\< b( a8)\! r r4
	
	R1*5
	
	\set Staff.midiInstrument = #"pizzicato strings"
	d8\p^\markup { pizz. } r r4 r d8 r
	d8 r r4 r d8 r
	d8 r r4 r d8 r
	d8 r r4 r
		\set Staff.midiInstrument = #"string ensemble 1"
		f-sharp8^\markup { arco } r
	c-sharp8 r a r d r f-sharp r
	c-sharp r a r d r d\< r
	d-sharp\! r e r e r r4
	a8 r r4 r2
	R1
	r8 a,\pp r a r a r a
	r a r a r a r a
	r a r a r a r a
	r a r a r a r a
	r a-sharp_\cr r b r c-sharp r d
	r d-sharp r e r f-sharp r g
	r g-sharp r a r b r c
	d\f r d,4~ d8 r r4
	d-flat'8 r d-flat,4~ d-flat8 r r4
	c8\f r c r c r r4
	c8 r c r c r r4
	c'8[ c16. c32] c8 r b8[ b16. b32] b-flat8 r
	a8[ a16. a32] g-sharp8 r f-sharp!8[ f-sharp16. f-sharp32] f8 r
	e8\ff r e r e4-> r4
	e8 r e r e4-> r4
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
	R1
	f-sharp4\pp^\markup { arco } e2.~
	e1
	e2_\markup { \italic {poco cresc.} } d
	d d
	c-sharp b
	d-sharp e4~ e8 r
	
	\set Staff.midiInstrument = #"pizzicato strings"
	e4\p^\markup { pizz. } r e r
	e r d r
	c-sharp r b r
	a_\markup { \italic {poco a poco cresc.} } r g-sharp r
	g! r f-sharp f-sharp'
	f r e-flat r
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
	r8 d-sharp8 d-sharp'4 e8 r r4
	R1
	r2 r4 \tuplet 3/2 { e,8\f[ e e] }
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
	e[ r e r e r e] r e[ r e r e r e] r
	e[ r e r e r e] r e[ r e r e r e] r
	e\mf[ r e r e r e] r d2\f\>
	e16\mf[\! r e r e r e] r d2\f
	d'16\mf[ r d r d r d] r c2\f\>
	c16\mf[\! r c r c r c] r c2\f\>
	c16\mf[\! r c r c r c] r b2\f
	b-flat8\mf b-flat r b-flat[ b-flat b-flat] r b-flat
	a a r a[ a a] r a
	f f r f[ f f] r f
	d d r d[ d d] r d
	
	R1*4
	
	a8\ff r r4 r2
	e'4 r d c-sharp
	b8 r r4 r2
	f-sharp'4 r r e
	d8 r r4 c-sharp8 r r4
	b8 r r4 a8 r r4
	g-sharp8 r r4 d'8 r c-sharp r
	g-sharp r r4 d'8 r e r
	a,8\ff r r4 r2
	e'4 r d c-sharp
	b8 r r4 r2
	f-sharp'4 r r e
	d8 r r4 c-sharp8 r r4
	b8 r r4 a8 r r4
	g-sharp8 r r4 r8 d-sharp'16\p[( e] f-sharp8)[ a-sharp,16( b-sharp]
	c-sharp8)[ e16( d-sharp] e8)[ c-sharp16( b-sharp] c-sharp8)[\< g-sharp a! f-sharpsharp]\!
	g-sharp8\mf r r4 r8 d-sharp'16\p[( e] f-sharp8)[ a-sharp,16( b-sharp]
	c-sharp8)[ e16( d-sharp] e8)[ c-sharp16( b-sharp] c-sharp8)[\< g-sharp a! g-sharp]\!
	f-sharpsharp8\mf r r4 r4 r8 a-sharp16( g-sharp
	f-sharpsharp8) r r4 r r8 a-sharp16( g-sharp
	f-sharpsharp8) r r4 r8 f-sharp'!16[( g-sharp] a!8)[ g-sharp16( f-sharp]
	e-sharp8) r r4 r8 b16[( c-sharp] d!8)[ c-sharp16( b]
	a!8) a'16[( b] c8)[\< b16( a] g!8)[ g16( a] b-flat8)[ a16( g]\!
	f-sharp8\mf) r r4 r r8 e16\p( f-sharp
	g8)[ b-flat16(\< a] b-flat8)[ g16( f-sharp] g8)[ d] e-flat[ c-sharp]\!
	d8\mf r r4 r r8 e16\p( f-sharp
	g8)[ b-flat16(\< a] b-flat8)[ g16( f-sharp] g8)[ d] e-flat[ d]\!
	c-sharp8\mf r8 r4 r8 e16[( f-sharp] g8)[ e16( d]
	c-sharp8) r r4 r8 e16[( f-sharp] g8)[ e16( d]
	c-sharp8) r r4 r8 c16[( d] e-flat8)[ d16( c]
	b8) r r4 r8 f'16[(_\cr g] a-flat8)[ g16( f]
	e-flat8)[ e-flat16( f] g-flat8)[ f16( e-flat] d8)[ d-flat16( e-flat!] f-flat8)[ e-flat16( d-flat]
	c8)[ b!16( c-sharp] d8)[ c-sharp16( b] a!8)[ a16( b] c8)[ b16( a]
	g-sharp8\ff) r r4 r2
	g!8\f r r4 r2
	
	\set Staff.midiInstrument = #"pizzicato strings"
	c8\pp^\markup {pizz.} \noDynamic r\p r4 r2
	r2 r4 e8 r
	d r r4 r2
	r2 r4 g8 r
	f r r4 e8 r r4
	d8 r r4 c8 r r4
	b8\p r r4 e8 r r4
	b8 r r4
	e8 r d\pp r
	c r r4 r2
	r2 r4 e8 r
	d r r4 r2
	r4 a'8 r r4 g8 r
	f r r4 e8 r r4
	d8 r r4 c8 r r4
	b8 r r4 r2
	
	\set Staff.midiInstrument = #"string ensemble 1"
	r2 b^\markup {arco}
	b8 r r4 r2
	r2 b a8 r r4 r2
	r2 a
	a8 r r4 r2
	r a\<
	g-sharp8\! r r4 r2
	g!8 r r4 r2
	
	R1*2
	
	c4\ff r r2
	c4 r b-flat a
	g r r2
	d'4 r d c
	b-flat8 r r4 a8 r r4
	g8 r r4 f8 r f' r
	e-flat r d r c r b-flat r
	a1\ff~
	a8[ a'] b-flat[ e,] f[ b-flat,] b[ e,]
	a1~
	a8[ a'] b-flat[ e,] f[ b-flat,] b[ e,]
	a1~
	a8[ b'!] c[ f,] f-sharp[ c] c-sharp[ g-sharp]
	a1~
	a!8[ b'!] c[ f,] g![ c-sharp,!] d![ g-sharp,]
	a1~
	a~
	a8\ff r a' r a r a r
	a8 r a r a r a r
	a8 r r4 r2
	a8 r a r a r a r
	a8 r r4 r2
	a8 r a r a r a r
	a r r4 r2
	
	s1*46
	
	\set Staff.midiInstrument = #"pizzicato strings"
	d,8\pp^\markup {pizz.} r r4 r d8 r
	r2 r4 d8 r
	r2 r4 d8 r
	r2 r4
		\set Staff.midiInstrument = #"string ensemble 1"
		f-sharp8\pp^\markup {arco} r
	c-sharp r a r d r f-sharp r
	c-sharp r_\markup { \italic {poco cresc.}} a r d r c-sharp4
	b e d2\<
	c-sharp4 b(\! a8) r r4
	
	R1*3
	
	d8\pp^\markup {pizz.} r r4 r d8 r
	c-sharp r r4 r c8_\cr r
	b8 r r4 r b8 r
	a-sharp4 r a r
	g-sharp r g r
	f-sharp r f r
	e e' e-flat r
	
	\set Staff.midiInstrument = #"string ensemble 1"
	d2^\markup {arco}_\markup { \dynamic {mf} \italic {dim.} } d
	d2~\> d8\! r r4
	
	R1*2
	
	r8 d r d r d-.[ d-. d-.]
	R1
	r8 d r d r d-.[ d-. d-.]
	r d-sharp_\cr r e r f-sharp r g
	r g-sharp r a r b r c
	r c-sharp! r d r e r f
	g r g,4~ g8 r r4
	r4 g-flat~ g-flat8 r r4
	
	\set Staff.midiInstrument = #"pizzicato strings"
	f8\f^\markup {pizz.} r r4 r2
	f8 r r4 r2
	f8_\cr r f r e r e-flat r
	d r d r b r b-flat r
	
	\set Staff.midiInstrument = #"string ensemble 1"
	a8\ff^\markup {arco} r a r a'4 r
	a,8 r a r a'4 r
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
	r8 g-sharp\f g-sharp'4 a8 r r4
	R1
	r2 r4 \tuplet 3/2 { a8\f[ a a] }
	r2 r4 \tuplet 3/2 { b8[ b b] }
	
	r8 b-sharp r4 r8 c-sharp8 r4
	r8 d r4 r8 e-flat r4
	d4\pp r d,2
	c-sharp! c
	b-flat4\< a g8[ g']~ g\! r
	b-flat,4\< a g8[ g']~ g\! r
	g4\mf f e d
	c-sharp\< c b b'8[ b-flat]\!
	a8 r r4 r2
	
	R1*3
	
	r8\pp a16_\markup { \italic {poco a poco cresc.}} r16 \stemUp a[ r a,] \stemNeutral r a[ r a' r a r a,] r
	a[ r a r a r a] r a[ r a r a r a] r
	a[ r a r a r a] r a[ r a r a r a] r
	a[\< r a r a r a]\! r g2\f\>
	a16[ r\mf\! a r a r a] r g2\f\>
	g'16[ r\mf\! g r g r g] r f2\f\>
	f16[ r\mf\! f r f r f] r f2\f\>
	f8[\! f f f] e2\f
	e8\mf[ e] r e[ e-flat e-flat] r e-flat
	d[ d] r d[ d d] r d
	b-flat[ b-flat] r b-flat[ b-flat b-flat] r b-flat
	g[ g] r g[ g g] r g
	
	R1*4
	
	d'8\f r8 r4 r2
	a'8_\cr r g-sharp r g r f-sharp r
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
	d,[ d' c-sharp b] b-flat4 a8[ g]
	f-sharp[ d' c-sharp b!] b-flat4 a8[ g]
	f-sharp[ e-sharp f-sharp g] g-sharp[ a a-sharp b]
	c-sharp[ d d-sharp e] e-flat-> r r a,
	d, r b' r a r f-sharp r
	d r b' r a r f-sharp r
	d r b r d r b r
	d r b r d r b r
	d[ d d d] d[ d d d]
	d4 d d d
	d1\fermata
}
