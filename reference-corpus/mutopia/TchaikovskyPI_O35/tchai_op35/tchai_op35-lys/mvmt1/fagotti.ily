\version "2.20.0"

theBassoons =  \relative d' {
	\set Score.skipBars = ##t
	
	\clef "bass"
	\key d \major
	
	r1
	
	R1*5
	
	<< { r2 r4 b\p } \\ { R1 } >>
	<< { e4 e a,2 } \\ { R1 } >>
	<< { R1 } \\ { a,1\p~^\markup { \italic {poco a poco cresc.} } } >>
	<< { R1 } \\ { a1~ } >>
	<< { R1 } \\ { a1~ } >>
	<< { R1 } \\ { a1~ } >>
	<< { R1 } \\ { a1 } >>
	<< { a'1\mf\< } \\ { a,1~ } >>
	<< { a'1\! } \\ { a,1~ } >>
	<< { a1\f~ } \\ { a1~ } >>
	<< { a1 } \\ { a1 } >>
	<< { a4\ff } \\ { a4 } >> r4 << { a4 } \\ { a4 } >> r
	<< { a8[ a a a] a2:8 } \\ { a8[ a a a] a2:8 } >>
	<< { a8 } \\ { a8 } >> r8 r4 r2
	R1
	r8 << { e-flat'8[( d]) } \\ { e-flat8[( d]) } >> r r << { e-flat8[( d]) } \\ { e-flat8[( d]) } >> r
	
	R1*34
	
	r4 < d b-flat' >4\f~ < d b-flat' >8 r r4
	r4 < d-flat b'! >4~ < d-flat b' >8 r r4
	< c, c' >8\f r < c c' > r < c c' > r r4
	< c c' >8 r < c c' > r < c c' > r r4
	<< { c'8[ c16. c32] c8 } \\ { c8[ c16. c32] c8 } >> r
		<< { b8[ b16. b32] b-flat8 } \\ { b8[ b16. b32] b-flat8 } >> r
	< a a' >8[ < a a' >16. < a a' >32] < g-sharp g-sharp' >8 r < f-sharp! f-sharp'! >8[
		< f-sharp f-sharp' >16. < f-sharp f-sharp' >32] < f f' >8 r
	< e e' >8\ff r < e e' > r < e e' >4-> r
	< e e' >8 r < e e' > r < e e' >4-> r
	
	R1*21
	
	<< { g-sharp'2 a } \\ { f2\pp_\markup { \translate #(cons 4 -1) \italic {poco cresc.} } e-flat } >>
	<< { g4 g-sharp g f } \\ { c-sharp4 b a-sharp g-sharp } >>
	<< { c-sharp'!2~ c-sharp8 } \\ { f-sharp,,2\mf~ f-sharp8 } >> r8 r4
	R1
	r8\mf < f f' >8~ < f f' >4~ < f f' >8[ < f-sharp f-sharp' >] < g g' >[ < g-flat g-flat' >]
	< f f' > r r4 r2
	r8 < f f' >8~ < f f' >4~ < f f' >8[ < f-sharp f-sharp' >] < g g' >[ < g g' >]
	r8 < g-flat g-flat' >4\mf < f f' >4 r8 r4
	r8 < f f' >4 < e! e'! > r8 r4
	
	R1*2
	
	r2 r4 \tuplet 3/2 { < e e' >8\f[ < e e' > < e e' >] }
	r2 r4 \tuplet 3/2 { < f-sharp f-sharp' >8\f[ < f-sharp f-sharp' > < f-sharp f-sharp' >] }
	r8 < f-sharpsharp f-sharpsharp' > r4 r8 < g-sharp g-sharp' > r4
	r8 < a a' > r4 r8 < b-flat b-flat' > r4
	
	R1*6
	
	< a' c-sharp >16\pp[ r < a-sharp c-sharp > r < b d > r < b-sharp d-sharp >] r < c-sharp e >[ r
		< a-sharp c-sharp > r < b d > r < b-sharp d-sharp >] r
	< c-sharp e >[ r < a-sharp g'! > r < b f-sharp' > r < g-sharp f' >] r < a-sharp e' >[ r < f-sharp a >] r < f-sharp a >4->
	< g-sharp b >16\pp[ r < a-sharp c-sharp > r < b d > r < b-sharp d-sharp >] r < c-sharp e >[ r
		< a-sharp c-sharp > r < b d > r < b-sharp d-sharp >] r
	< c-sharp e >[ r < a-sharp g'! > r < b f-sharp' > r < g-sharp f' >] r < a e' >[ r < f-sharp a >] r < f-sharp a >4->
	< g-sharp b >16\pp r r8 r4 r2
	
	R1*2
	
	r2 < d, d' >8\f r r4
	r2 < d d' >8\f r r4
	< d' d' >16\mf[ r < d d' > r < d d' > r < d d' >] r < c c' >8\f r r4
	< c c' >16\mf[ r < c c' > r < c c' > r < c c' >] r < c c' >8->\f r r4
	< c c' >16\mf[ r < c c' > r < c c' > r < c c' >] r < b b' >8\f r r4
	< b-flat b-flat' >8\f r r4 r2
	< a a' >8 r r4 r2
	< f f' >8 r r4 r2
	< d d' >8 r r4 r2
	r8 < d' d' >8\mf~_\markup { \translate #(cons 4 -1) \italic cresc. } < d d' >4
		r8 < d d' >8~ < d d' >4
	r8 < d d' >8~ < d d' >4 r8 < d d' >8~ < d d' >4
	r8 < d d' > r8 < d d' > r8 < d d' > r8 < d d' >
	<< { d8[\< d d d] d[ d d d]\! } \\ { d8[ d d d] d[ d d d] } >>
	< a a' >8\ff[ \tuplet 3/2 { < a' c-sharp >16 < a c-sharp > < a c-sharp >] } < a c-sharp >8[ < a c-sharp >]
		< a c-sharp >[ < a c-sharp > < a c-sharp > < a c-sharp >]
	< e, e' > \tuplet 3/2 { < g-sharp' b >16[ < g-sharp b > < g-sharp b >] } < g-sharp b >8 r
		< d, d' > r < c-sharp c-sharp' > r
	< b b' >8 \tuplet 3/2 { < b'' d >16[ < b d > < b d >] } < b d >8[ < b d >]
		< b d >[ < b d >] < b d >[ < b d >]
	< f-sharp, f-sharp' >8[ \tuplet 3/2 { < a-sharp' c-sharp >16 < a-sharp c-sharp > < a-sharp c-sharp >] }
		< a-sharp c-sharp >8[ < a b-sharp >] < a-sharp c-sharp >[ < a-sharp c-sharp >] < e, e' >[ < a' c-sharp >]
	< d,, d' >8 r r4 < c-sharp c-sharp' >8 r r4
	< b b' >8 r r4 << { a'8 } \\ { a8 } >> r8 r4
	<< { g-sharp8 } \\ { g-sharp8 } >> r8 r4 < d d' >8 r < c-sharp c-sharp' >8 r
	<< { g-sharp'8 } \\ { g-sharp8 } >> r8 r4 < d d' >8 r < e e' > r
	< a a' >8\ff[ \tuplet 3/2 { < a' c-sharp >16 < a c-sharp > < a c-sharp >] } < a c-sharp >8[ < a c-sharp >]
		< a c-sharp >[ < a c-sharp > < a c-sharp > < a c-sharp >]
	< e, e' > \tuplet 3/2 { < g-sharp' b >16[ < g-sharp b > < g-sharp b >] } < g-sharp b >8 r
		< d, d' > r < c-sharp c-sharp' > r
	< b b' >8 \tuplet 3/2 { < b'' d >16[ < b d > < b d >] } < b d >8[ < b d >]
		< b d >[ < b d >] < b d >[ < b d >]
	< f-sharp, f-sharp' >8[ \tuplet 3/2 { < a-sharp' c-sharp >16 < a-sharp c-sharp > < a-sharp c-sharp >] }
		< a-sharp c-sharp >8[ < a b-sharp >] < a-sharp c-sharp >[ < a-sharp c-sharp >] < e, e' >[ < a' c-sharp >]
	< d,, d' >8 r r4 < c-sharp c-sharp' >8 r r4
	< b b' >8 r r4 << { a'8 } \\ { a8 } >> r8 r4
	<< { g-sharp8 } \\ { g-sharp8 } >> r8 r4 r2
	r2 r4 << { c-sharp'4 } \\ { c-sharp4\p\< } >>
	<< { \stemDown < b-sharp d-sharp >8 \stemNeutral } \\ { s8\mf\! } >> r8 r4 r2
	r2 r4 << { < e, c-sharp' >4 } \\ { s4\p\< } >>
	<< { c-sharp'8 r r d-sharp->( e) r r4 } \\ { a-sharp,8\f\! r r4 r2 } >>
	<< { r4 r8 d-sharp->( e) r r4 } \\ { R1 } >>
	<< { r4 r8 g-sharp8( a!) r r b-sharp,( } \\ { r2 r4 r8 g-sharp~ } >>
	<< { c-sharp8) r r e!->( e-sharp) r r e-sharp,( } \\ { g-sharp8 r r4 r r8 e-sharp8( } >>
	<< { f-sharp8) } \\ { f-sharp8) } >> r8 r < b d-sharp >( < b e >)
		<< { g!16[( a] b-flat8)[ a16( g] } \\ { g,!16\f[( a] b-flat8)[ a16( g] } >>
	<< { f-sharp'8) } \\ { f-sharp,8) } >> r8 r4 r2
	
	R1*3
	
	r2 r8
		\clef "tenor"
		< g' d' >8\mf~ < g d' > r
	r2 r8 < g d' >~ < g d' > r
	r2 r4 r8
		\clef "bass"
		< d f-sharp >8(
	< d g >) r r4 r r8 < g b >(_\cr
	< g c >) r r < f a >( < f b-flat >) r r
		\clef "tenor"
		< e-flat' g >(
	< e-flat a-flat >) r r < c-sharp! e-sharp >( < c-sharp f-sharp! >) r r < b! d-sharp >(
	< b e! >\ff) r
		\clef "bass"
		<< { g-sharp2 g-sharp8 } \\ { g-sharp2\mf g-sharp8 } >> r8
	<< { b8 r b2 b8 r } \\ { g!8\f s g2\mf\> g8\! s } >>
	
	R1*6
	
	<< { b,8^\p[^( d f b] e^) r r4 } \\ { R1 } >>
	<< { b,8^\p[^(^\< d f b] e^)^\! r r4 } \\ { R1 } >>
	
	R1*6
	
	<< { r8 b,^\p[^( d-sharp f-sharp] b^) r r4 } \\ { R1 } >>
	R1
	<< { r8 b,[^( d-sharp f-sharp] b^) r r4 } \\ { R1 } >>
	R1
	<< { r8 a,[^( c-sharp e] a^) r r4 } \\ { R1 } >>
	R1
	<< { r8 a,[^( c-sharp e] a^) r r4 } \\ { R1 } >>
	R1
	r2 < g-sharp, f' >\p_\markup { \translate #(cons 4 -1) \italic cresc. }
	r2 < g! f' >
	< f-sharp! f-sharp'! >\< < f g-sharp' >
	< e g-sharp' > < d d' >4\! < d-flat d-flat' >
	< c c' >4\ff r r2
	< c c' >4 r << { b-flat'4 a } \\ { b-flat,4 a' } >>
	<< { g4 } \\ { g4 } >> r r2
	< d d' >4 r < d d' > < c c' >
	< b-flat b-flat' >8 r r4 << { a'8 } \\ { a8 } >> r8 r4
	<< { g8 } \\ { g8 } >> r r4 << { f8 } \\ { f8 } >> r < f f' >8 r
	< e-flat e-flat' > r < d d' > r < c c' > r < b-flat b-flat' > r
	<< { a'1~ } \\ { a1\ff~ } >>
	<< { a8[ a'] b-flat[ e,] f[ b-flat,] b[ e,] } \\ { a8[ a] b-flat[ e,] f[ b-flat,] b[ e] } >>
	<< { a1~ } \\ { a1~ } >>
	<< { a8[ a'] b-flat[ e,] f[ b-flat,] b[ e,] } \\ { a8[ a] b-flat[ e,] f[ b-flat,] b[ e] } >>
	<< { a1~ } \\ { a1~ } >>
	<< { a8[ b'!] c[ f,] f-sharp[ c!] c-sharp[ g-sharp] } \\ { a8[ b!] c[ f,] f-sharp[ c] c-sharp[ g-sharp'] } >>
	<< { a1~ } \\ { a1~ } >>
	<< { a8[ b'!] c[ f,] f-sharp[ c!] c-sharp[ g-sharp] } \\ { a8[ b!] c[ f,] f-sharp[ c] c-sharp[ g-sharp'] } >>
	<< { a1~ } \\ { a1~ } >>
	<< { a1~ } \\ { a1~ } >>
	<< { a8 } \\ { a8\ff } >> r < a a' >8 r < a a' >8 r < a a' >8 r
	< a a' >8 r < a a' >8 r < a a' >8 r < a a' >8 r
	< a a' >8 r r4 r2
	< a a' >8 r < a a' >8 r < a a' >8 r < a a' >8 r
	< a a' >8 r r4 r2
	< a a' >8 r < a a' >8 r < a a' >8 r < a a' >8 r
	< a a' >8 r r4 r2
	
	s1*46
	s1*11
	
	< d d' >1\pp
	< c-sharp e' >2._\cr < c d' >4
	< b d' >1
	< a-sharp c-sharp' >2 < a b' >
	< g-sharp b' > < g a' >
	< f-sharp a' > < f g' >
	< e g' > < e-flat a-sharp' >
	< d b'' >8\mf r r4 r2
	
	R1*11
	
	< b-flat'' d >8\ff[ < b-flat d >16. < b-flat d >32] < b-flat d >8[ < b-flat d >16. < b-flat d >32] < c e-flat >8 r r4
	< b-flat d >8[ < b-flat d >16. < b-flat d >32] < b-flat d >8[ < b-flat d >16. < b-flat d >32] < c e-flat >8 r r4
	< b-flat d >8[_\cr < b-flat d >16. < b-flat d >32] < b d >8 r < e, c' >8[
		< e c' >16. < e c' >32] < e-flat c-sharp' >8 r
	< d d' >8[ < d d' >16. < d d' >32] < d d' >8 r << { b!8[ b16. b32] b-flat8 } \\ { b8[ b16. b32] b-flat8 } >> r8
	<< { a8 } \\ { a8\ff } >> r8 << { a8 } \\ { a8 } >> r << { a4^> } \\ { a4_> } >> r4
	<< { a8 } \\ { a8 } >> r8 << { a8 } \\ { a8 } >> r << { a4^> } \\ { a4_> } >> r4
	
	R1*10
	
	<< { r2 d8^\p[( f-sharp a d]) } \\ { R1 } >>
	<< { c4( b8[ a] g[ f-sharp g b]) } \\ { R1 } >>
	<< { b1^\cr } \\ { R1 } >>
	<< { b-flat2( a) } \\ { R1 } >>
	<< { a2\pp g } \\ { R1 } >>
	<< { g-sharp1~ } \\ { R1 } >>
	<< { g-sharp2. a4 } \\ { R1 } >>
	<< { b-flat8 r r4 r2 } \\ { R1 } >>
	
	R1*3
	
	r2 r8 < b-flat, g' >8\p[ < b-flat g' > < b-flat g' >]
	r2 r8 < a f-sharp' >8\p[ < a f-sharp' > < a f-sharp' >]
	
	R1*2
	
	r2 r4 \tuplet 3/2 { < a a' >8\f[ < a a' > < a a' >] }
	r2 r4 \tuplet 3/2 { < b b' >8[ < b b' > < b b' >] }
	r8 < b-sharp b-sharp' > r4 r8 < c-sharp c-sharp' > r4
	r8 < d d' > r4 r8 < e-flat c' > r4
	
	R1*6
	
	< a, f-sharp' >16\pp[ r < a f-sharp' > r < a g' > r < a g-sharp' >] r < a a' >[ r < a f-sharp' > r < a g'! > r < a g-sharp' >] r
	< a a' >[ r < a d-sharp > r < a e' > r < a c-sharp >] r < a d >[ r < a f-sharp >] r < a d >4->
	< a c-sharp >16[ r < a f-sharp' > r < a g' > r < a g-sharp' >] r < a a' >[ r < a f-sharp' > r < a g'! > r < a g-sharp' >] r
	< a a' >[ r < a d-sharp > r < a e' > r < a c-sharp >] r < a d >[ r < a f-sharp >] r < a d >4->
	< a c-sharp >16 r r8 r4 r2
	
	R1*2
	
	r2 < g g' >8\f r r4
	r2 < g g' >8\f r r4
	r2 < f f' >8 r r4
	r2 < f f' >8\f r r4
	< f f' >8[ < f f' > < f f' > < f f' >] < e e' >\f r r4
	< e e' >8\f r r4 < e-flat e-flat' >8 r r4
	< d d' >8 r r4 < d d' >8 r r4
	< b-flat b-flat' >8[ < b-flat b-flat' >] r < b-flat b-flat' >[ < b-flat b-flat' > < b-flat b-flat' >] r < b-flat b-flat' >
	<< { g'8[ g] r g[ g g] r g } \\ { g8[ g] s g[ g g] s g } >>
	r8 < b'! d >8\mf~ < b d >4_\cr r8 < b d >8~ < b d >4
	r8 < b! d >8~ < b d >4 r8 < b d >8~ < b d >4
	r8 < b d > r8 < b d > r8 < b d > r8 < b d >
	< b d >2:8 < b d >:
	
	%%% CODA %%%
	
	< d,, d' >8\f r r4 r2
	
	R1*2
	
	r4 << { d'2 } \\ { d2\f } >> r4
	r4 << { c-sharp2 } \\ { c-sharp2 } >> r4
	r4 << { b2 } \\ { b2 } >> r4
	r4 < a f' >8[ < a f-sharp >] < g-sharp e' > r < g-sharp e' >[ < g e' >]
	< f-sharp d' > r r4 r2
	< f d' >8 r r4 r2
	< f f' >8 r r4 r2
	< g g' >8\f r < f-sharp! f-sharp'! > r < g g' > r < f-sharp f-sharp' > r
	< g g' >1\f
	<< { g-sharp'2.( g-sharp,8)[ g-sharp] } \\ { g-sharp2.~ g-sharp8[ g-sharp] } >>
	<< { a8 } \\ { a8\ff } >> r8 r4 r2
	
	R1*3
	
	r8 < a' c-sharp >\f[ < b-flat d > < a c-sharp >] < b-flat d > < a, a' >\ff[ < a a' > < a a' >]
	< g g' > < a' c-sharp >\f[ < b-flat d > < a c-sharp >] < b-flat d > < a, a' >\ff[ < a a' > < a a' >]
	< g g' > < a' c-sharp >\f[ < b-flat d >] < a, a' >\ff[ < g g' >] < a' c-sharp >\f[ < b-flat d >] < a, a' >\ff
	< g g' > < a' c-sharp >[ < b-flat d >] < g, g' >[ < g g' >] r r < g g' >
	< d d' >\ff[ < d' d' > < c-sharp c-sharp' > < b b' >] < b-flat b-flat' >4 < a a' >8[ < g g' >]
	< f-sharp f-sharp' >[ < d' d' > < c-sharp c-sharp' > < b! b'! >] < b-flat b-flat' >4 < a a' >8[ < g g' >]
	< f-sharp f-sharp' > < e-sharp e-sharp' >[ < f-sharp f-sharp' > < g g' >] < g-sharp g-sharp' >[ < a a' > < a-sharp a-sharp' > < b b' >]
	<< { c-sharp'8[ d, d-sharp e] e-flat-> } \\ { c-sharp8[ d d-sharp e] e-flat_> } >> r8 r < a, a' >8
	< d, d' > < d' d' >[ < c-sharp c-sharp' > < b b' >] < b-flat b-flat' >4 < a a' >8[ < g g' >]
	< d d' > < d' d' >[ < c-sharp c-sharp' > < b b' >] < b-flat b-flat' >4 < a a' >8[ < g g' >]
	< f-sharp f-sharp' > < e-sharp e-sharp' >[ < f-sharp f-sharp' > < g g' >] < g-sharp g-sharp' >[ < a a' > < a-sharp a-sharp' > < b b' >]
	<< { c-sharp'8[ d, d-sharp e] e-flat-> } \\ { c-sharp8[ d d-sharp e] e-flat_> } >> r8 r < a, a' >8
	< d, d' > r < b' b' > r < a a' > r < f-sharp f-sharp' > r
	< d d' > r < b' b' > r < a a' > r < f-sharp f-sharp' > r
	< d d' > r < b b' > r < d d' > r < b b' > r
	< d d' > r < b b' > r < d d' > r < b b' > r
	< d d' >[ < d d' > < d d' > < d d' >] < d d' >[ < d d' > < d d' > < d d' >]
	< d d' >4 < d d' > < d d' > < d d' >
	< d d' >1\fermata
}
