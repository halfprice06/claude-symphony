\version "2.20.0"

theFlutessecond =  \relative d''' {
	\clef "treble"
	\key d \major
	
	r1
	R1*5
	
	r2 r4 b4\p
	a b a2
	
	R1*6
	
	a4\f f8( e d4) f8( a)
	d2 r2
	d r
	d4\ff r d r
	d8[ d d d] d2:8
	c-sharp8 r r4 r8 f,\f( b-flat) r
	r2 r8 f( b-flat) r
	
	R1*35
	
	r4 f4\f~ f8 r r4
	r4 f~ f8 r r4
	c'8\f[ d16. e32] c8[ d16. e32] c8 r r4
	c8[ d16. e32] c8[ d16. e32] c8 r r4
	c8[ d16. e-flat32] d8 r d8[ e16. f32] e8 r
	e8[ f16. g32] f8 r d-sharp8[ d-sharp16. d-sharp32] d-sharp8 r
	e8\ff r e r e4-> r4
	e8 r e r e4-> r4
	
	R1*32
	
	r2 r4 \tuplet 3/2 { c-sharp8\f[ d e] }
	r2 r4 \tuplet 3/2 { c-sharp8[ d-sharp e] }
	r8 e r4 r8 e r4
	r8 e r4 r8 e r4
	c2\fp b
	b a
	a4 a a~ a8 r
	a4 a a~ a8 r
	
	R1*11
	
	a16\mf[ r b r a r b] r c8\f r r4
	c16\mf[ r d r c r d] r e-flat8->\f r r4
	e-flat16\mf[ r e-flat r e-flat r e-flat] r d-sharp8\f r r4
	e8\f r r4 r2
	f8 r r4 r2
	b,8 r r4 r2
	b-sharp8 r r4 r2
	
	R1*3
	
	b-sharp8\f[\< b-sharp b-sharp b-sharp] b-sharp[ b-sharp b-sharp b-sharp]\!
	c-sharp8\ff r8 c-sharp2 b16[( a c-sharp e])
	b4.( c-sharp8) b4 c-sharp
	d8 r d2 c-sharp16[( b d f-sharp])
	c-sharp4.( d8) c-sharp4 c-sharp
	f-sharp,8 g-sharp a[ g-sharp16( f-sharp] e8) g-sharp a[ f-sharp16( e]
	d8) e-sharp f-sharp[ e16( d] c-sharp8) e-sharp f-sharp[ d16( c-sharp]
	b'8) c-sharp d[ c-sharp16( b] a8)[ g-sharp16( f-sharp] e-sharp)[ c-sharp( e-sharp g-sharp])
	b8 c-sharp d[ c-sharp16( b] a8)[ g-sharp16( f-sharp] e!)[ f-sharp( g-sharp b])
	c-sharp8\ff r8 c-sharp2 b16[( a c-sharp e])
	b4.( c-sharp8) b4 c-sharp
	d8 r d2 c-sharp16[( b d f-sharp])
	c-sharp4.( d8) c-sharp4 c-sharp
	f-sharp,8 g-sharp a[ g-sharp16( f-sharp] e8) g-sharp a[ f-sharp16( e]
	d8) e-sharp f-sharp[ e16( d] c-sharp8) e-sharp f-sharp[ d16( c-sharp]
	b-sharp'8) r r4 r2
	r2 r4 c-sharp,4\p\<
	d-sharp8\mf\! r r4 r2
	r2 r4 e,4\p\<
	a-sharp8[\mf d-sharp'->]( e) r r2
	r8 d-sharp->( e) r r2
	r8 c-sharpsharp->( d-sharp) r r4 r8 g-sharp,,~
	g-sharp[ c-sharp'!->]( d!) r r4 r4
	r4 r8 b,~ b r r c-sharp'(
	d!)[ d->\p]( e-flat) r r2
	r2 r4 g,\p\<
	f-sharp8\mf[\! d'->]( e-flat) r r2
	r2 r4 b-flat,4\p\<
	e8\mf[\! a'->]( b-flat)[ a,->]( b-flat) r r4
	r8 a->( b-flat4) r2
	r8 g-sharp->[( a) d,,->]( e-flat) r r d~
	d g'->( a-flat)[ b-flat,->]( b) r r4
	r4 r8 f~_\cr f r r e-flat'~
	e-flat r r c-sharp!~ c-sharp r r b!~
	b\ff r r4 r2
	f'8\f r f2\mf\> f8\! r
	
	R1*26
	
	a8\ff r a2 \grace { g16[ a] } g16[( f a c])
	g4.( a8) g4 a
	b-flat8 r b-flat2 \grace { a16[ b-flat] } a16[( g b-flat d])
	a4.( b-flat8) a4 a
	d8 e f[ e16( d] c8)[ e] f[ d16( c]
	b-flat8)[ c-sharp!] d[ c16( b] a8)[ c-sharp] d[ b-flat16( a])
	g16[( a b-flat g]) f[( a b-flat f]) e-flat[( f-sharp g e-flat]) d[( f-sharp g d])
	c-sharp!8\ff[ a'] b-flat[ b-flat,] b r r c
	c-sharp!8 c-sharp4 d e g-sharp8
	a[ a] b-flat[ b-flat,] b r r c
	c-sharp!8 c-sharp4 d e g-sharp8
	a[ b-flat] b[ b,] c r r c-sharp
	d8 d4 d-sharp e b'!8
	c8[ b] c[ c,] c-sharp r r d!
	d-sharp8 d-sharp4 e f b-sharp8
	c-sharp![ b-sharp] c-sharp[ c-sharp,] d![ d'!] d-sharp[ d-sharp,]
	e[ e'] f[ f,] f-sharp[ f-sharp'] g[ g,]
	g-sharp8\ff[ f16( g!] g-sharp8)[ f16( g] g-sharp8)[ f16( g] g-sharp8)[ f16( g]
	g-sharp8)[ f16( g] g-sharp8)[ f16( g] g-sharp8)[ f16( g] g-sharp8)[ g16( g-sharp]
	a8) r r4 r r8 f16[( g!]
	g-sharp8)[ f16( g] g-sharp8)[ f16( g] g-sharp8)[ f16( g] g-sharp8)[ g16( g-sharp]
	a8) r r4 r r8 f16[( g!]
	g-sharp8)[ f16( g] g-sharp8)[ f16( g] g-sharp8)[ f16( g] g-sharp8)[ g16( g-sharp]
	a8) r r4 r2
	
	s1*46
	s1*33
	
	r2 c-sharp!8\f[ d16. e32] d8 r
	a8\ff r a r a4-> r
	a8 r a r a4-> r
	
	R1*25
	
	r2 r4 \tuplet 3/2 { f-sharp8\f[ g a] }
	r2 r4 \tuplet 3/2 { f-sharp8[ g-sharp a] }
	
	r8 a r4 r8 a r4
	r8 a r4 r8 a r4
	
	R1*17
	
	r2 b!8\f r r4
	c-sharp!8\f r r4 c-sharp8 r r4
	d8 r r4 d8 r r4
	d8[ d] r d[ d d] r d
	d[ d] r d[ d d] r d
	
	R1*4
	
	d,8\f r r4 r2
	
	R1*2
	
	r4 b-flat'2\f r4
	r4 a2 r4
	r4 g2 r4
	
	R1*6
	
	d'1\f
	d!8\ff r r4 r2
	
	R1*3
	
	r2 r8 c-sharp8\ff[ a c-sharp]
	d r r4 r8 c-sharp[ a c-sharp]
	d r r c-sharp d r r c-sharp
	d r r d d r r d
	d\ff d,4 d8~ d[ e f-sharp g]
	a d,4 d8~ d[ e f-sharp g]
	a d4 e8 d c-sharp4 d8
	c-sharp b4 g8 b-flat-> r r a
	d,8 d4 d8~ d[ e f-sharp g]
	a d,4 d8~ d[ e f-sharp g]
	a d4 e8 d c-sharp4 d8
	c-sharp b4 g8 b-flat-> r r a
	d, r d r f-sharp r a r
	d r d, r f-sharp r a r
	d r d r d r d r
	d r d r d r d r
	d[ d,, f-sharp a] d[ d f-sharp a]
	d4 d d d
	d,,1\fermata
}
