\version "2.20.0"

theClarinets =  \relative a'' {
	\transposition b-flat
	
	\clef "treble"
	\key a \minor
	
	<< e2.^\p \\ g-sharp,2.\p >>
	<< { f'2^\< g4 } \\ { a,2_\< c4_\! } >>
	<< { c4\! d2 } \\ { c,2( b4) } >>
	<< e'2. \\ c,2. >>
	<< { a'8^\pp[( b] c4 d) } \\ { f,4( e d) } >>
	<< { a'8[( b] c4 d) } \\ { f,4( e d) } >>
	<< { c'8[( d] e-flat4) c-sharp8[( d-sharp] } \\ { d,4(\< e-flat) d-sharp(\! } >>
	<< { e'!4) f-sharp,8( g-sharp] a4) } \\ { e!4) b4\p( a) } >>
	<< { r4 r8 a''8^\mf[_(^\< g f]_)^\! } \\ { R1*3/4 } >>
	<< { e8[_(^\> d c-sharp d e f]_)^\! } \\ { R1*3/4 } >>
	<< { a,2^\p e8^\p[( f] } \\ { r4 r a,4~ } >>
	<< { e'4) e2 } \\ { a,4 a( g-sharp) } >>
	
	R1*3/4*7
	
	r4 c16\pp[(^\markup { \smaller {1\super{o} Solo.}} b a8]) g-sharp16[( f e8])
	
	R1*3/4*14
	
	<< { r4 r g-sharp'^\markup { \dynamic p \italic espress. } } \\ { R1*3/4 } >>
	<< { a4.^\< b8[( c d])^\! } \\ { R1*3/4 } >>
	<< { \tuplet 3/2 { e8-.[ e-. e-.]_\> } e16-.[ e-. e-. e-.]
		e4\trill \bar "" \grace { d-sharp16[_\! e] } } \\ { R1*3/4 } >>
	<< { a,8 r r4 r } \\ { R1*3/4 } >>
	
	R1*3/4*14
	
	r4 r r8 < f f' >\mf
	< f f' >[ < f f' >] < f f' >4 r8 < f f' >
	< f f' >[ < f f' >] < f f' >4 r
	< b, a' > < b g-sharp' > r
	< a g'! >^\markup { \italic dim. } < a f-sharp' > < g f' >
	< g e' > < f e-flat' > < f d' >8 r
	
	R1*3/4*10
	
	<< { \tuplet 3/2 { r8^\p c''[( b] } \tuplet 3/2 { g-sharp[ e c] }
		\tuplet 3/2 { b[ g-sharp e]) } } \\ { g1*3/4\rest } >>
	<< { r16 a[( c f] e8) e4^> e8 } \\ { g,1*3/4\rest } >>
	<< { r16 b'16[( e a] g-sharp8) g-sharp4^> g-sharp8 } \\ { R1*3/4 } >>
	<< { r16 e16[( a d] c8) c4^> c8 } \\ { R1*3/4 } >>
	<< { r16 b[( e a] g-sharp8) g-sharp4^> g-sharp8 } \\ { R1*3/4 } >>
	
	R1*3/4*3
	
	<< { < g-sharp,, e' >4.\p^> < e g-sharp! >8[( < f-sharp a > < g-sharp! b >] } \\ { s2. } >>
	<< { < a c >16)[ e^. a^. c^.] e^.[ c^. a^. e^.] } \\ { a8 r r4 } >> r4
	r16 e-.[ b'-. d-.] e-.[ d-. b-. e,-.] r4
	r16 e-.[ a-. c-.] e-.[ c-. a-. e-.] r4
	r16 e-.[ b'-. d-.] e-.[ d-. b-. e,-.] r4
	r16 e-.[ a-. c-.] e-.[ c-. a-. e-.] r4
	<< { r16 e-.[ g-sharp-. b-.] e-.[ b-. g-sharp-. e-.] r4 } \\ { c1*3/4\rest } >>
	<< { r16 f-.[ a-. d-.] r g,-.[ c-. e-.] r g-sharp,-.[ d'-. e-.] } \\ { f,1*3/4\rest } >>
	<< { a'16-.[ c-. a-. e-.] c8 r r4 } \\ { r1*3/4 } >>
	
	R1*3/4*9
	r1*3/4^\fermata
	
	<< { e'2.^>^\< } \\ { g-sharp,2.\< } >>
	<< { f'2^\! g4 } \\ { a,2\! c4 } >>
	<< { c4^\< d2^\! } \\ { c,2( b4) } >>
	<< { e'2. } \\ { c,2. } { s4\> s s\pp\! } >>
	<< { a'8[( b] c4 d) } \\ { f,4( e d) } >>
	<< { a'8[( b] c4 d) } \\ { f,4( e d) } >>
	<< { c'8[( d] e-flat4) c-sharp8[( d-sharp] } \\ { d,4(_\cr e-flat) d-sharp( } >>
	<< { e'!4) f-sharp,8[( g-sharp a b] } \\ { e,!4) b4( a) } >>
	<< { c'8) r r4 r } \\ { R1*3/4 } >>
	r4 r < a e-flat' >\mf
	R1*3/4
	< g c-sharp >2.
	R1*3/4
	r4 r < g c-sharp >
	R1*3/4
	< b-flat g' >2.
	R1*3/4
	< g e-flat' >2.\p
	R1*3/4
	< a-sharp f-sharp' >2.
	< e e' >8\pp[( < d-sharp d-sharp' >] < e e' >2)
	
	R1*3/4*2
	r1*3/4^\fermata
	
}
