\version "2.20.0"

theHornsfirst =  \relative c' {
	\transposition f'
	\clef "treble"
	\key c \major	
	
	\override Staff.TupletBracket.bracket-visibility = ##f
	
	r1
	
	R1*12
	
	< e e' >1\mf\<
	< e e' >\!
	< f-sharp c' >\f
	< f-sharp c' >
	<< { c'4 } \\ { f-sharp,4\ff } >> r4 << { c'4 } \\ { f-sharp,4 } >> r
	< f-sharp c' >8[ < f-sharp c' > < f-sharp c' > < f-sharp c' >] < f-sharp c' >2:8
	< g-sharp b >8 r r4 r2
	R1
	r8 < e c' >8\p( < f! f'! >) r r < e c' >( < f f' >) r
	
	R1*36
	
	< e e' >8\f[ < e e' >16. < e e' >32] < e e' >8[ < e e' >16. < e e' >32] < f f' >8 r r4
	< e e' >8[ < e e' >16. < e e' >32] < e e' >8[ < e e' >16. < e e' >32] < f f' >8 r r4
	< e e' >8[ < e e' >16. < e e' >32] < e e' >8 r < a d >8[ < a d >16. < a d >32] < a d-sharp >8 r
	< a e' >8[ < a e' >16. < a e' >32] < a f-sharp' >8 r < g d-sharp' >8[ < g e' >16. < g f-sharp' >32] < g e' >8 r
	< g-sharp e' >8\ff r < g e' > r << { e'8[(^> d-sharp]) } \\ { f-sharp,4_> } >> r4
	< g-sharp e' >8 r < g e' > r << { e'8[(^> d-sharp]) } \\ { f-sharp,4_> } >> r4
	
	R1*16
	
	<< { b2^\markup { I.II. } b } \\ { a2\pp g-sharp } >>
	<< { c-sharp2 c-sharp~ } \\ { g-sharp2 a( } >>
	<< { c-sharp8 } \\ { b8) } >> r8 r4 r2
	
	R1*3
	
	<< { R1 } \\ { b,4\pp^\markup {I.II.} a_\markup { \italic {poco cresc.} } b c-sharp } >>
	<< { f!2~ f8 } \\ { c-sharp!2\mf~ c-sharp8 } >> r8 r4
	< f c' >4\mf < f d' >~ < f d' >8[ < f b >8] < f c' >[ < f-sharp d' >]
	< g d' >[ < e c' >] < f! c' >[ < d b-flat' >] < e b-flat' >[ < e g >] << { f4 } \\ { f8 r } >>
	< f c' >4\mf < f d' >~ < f d' >8[ < f b >] < f c' >[ < f-sharp d' >]
	< g d' >[ < e c' >] < f c' >[ < d b-flat' >] < e b-flat' > << { r8 r4 } \\ { e8 d r } >>
	r2 r8 < f c' >8\mf[ < f c' > < f c' >]
	r2 r8 < e b' >[ < e b' > < e b' >]
	r8 < e c-sharp' > < e c-sharp' >4 < e b' >8 r r4
	
	R1*5
	
	r8^\markup {I.II.}
	< e g >4\p < e g >8 r < e f-sharp >4 < e f-sharp >8
	r8 < d-sharp f-sharp >4 < d-sharp f-sharp >8 r < d e >4 < d e >8
	r8 < c a' > r < e b' > r < e c' >4 r8
	r < c a' > r < e b' > r < e c' >4 r8
	r2 < b b' >
	< b b' >4^\markup {I.II.} < b b' > << { e'8 r r4 } \\ { c-sharp,4~ c-sharp8 r } >>
	<< { R1 } \\ { b16\pp[ r b r b r b] r b[ r b r b r b] r } >>
	<< { R1 } \\ { b16[ r b r b r b] r b[ r b] r b4_> } >>
	<< { R1 } \\ { b16\pp[ r b r b r b] r b[ r b r b r b] r } >>
	<< { R1 } \\ { b16[ r b r b r b] r b[ r b] r b4_> } >>
	<< { R1 } \\ { b16 r r8 r4 r2 } >>
	
	R1*2
	
	r2 < e c-sharp' >8\f r r4
	r2 < e c'! >8\f r r4
	<< { c'16\mf[ r c r c r c] r c8\f r8 r4 } \\ { R1 } >>
	<< { c16\mf[ r c r c r c] r b-flat8^>\f r8 r4 } \\ { R1 } >>
	<< { b-flat16\mf[ r c r b-flat r c] r c-sharp8 } \\ { b-flat16[ s b-flat s b-flat s b-flat] s b-flat8\f } >> r8 r4
	<< { d-sharp8\f } \\ { a8 } >> r8 r4 r2
	<< { e'8 } \\ { a,8 } >> r8 r4 r2
	<< { f-sharp'8 } \\ { f-sharp,8 } >> r8 r4 r2
	<< { g'!8 } \\ { g,!8 } >> r8 r4 r2
	r8 < g e' >8\mf~_\markup { \translate #(cons 4 -1) \italic cresc. } < g e' >4
		r8 < g e' >~ < g e' >4
	r8^\markup {I.II.} < g e' >~ < g e' >4 r8 < g e' >~ < g e' >4
	r8 < g e' > r8 < g e' > r8 < g e' > r8 < g e' >
	< e c-sharp' >8[\< < e c-sharp' > < e c-sharp' > < e c-sharp' >] < e c-sharp' >[ < e c-sharp' > < e c-sharp' > < e c-sharp' >]\!
	
	%%% DOUBLE BAR %%%
	
	< e b' >8\ff \tuplet 3/2 { < e e' >16[ < e e' > < e e' >] } < e e' >8[ < e e' >] < e e' >[ < e e' > < e e' > < e e' >]
	< d-sharp d-sharp' >8[ \tuplet 3/2 { < d-sharp d-sharp' >16 < d-sharp d-sharp' > < d-sharp d-sharp' >] } < d-sharp d-sharp' >8[ < d d' >]
		< d-sharp d-sharp' >[ < d-sharp d-sharp' >] r < e-sharp e-sharp' >
	< f-sharp f-sharp' >[ \tuplet 3/2 { < f-sharp f-sharp' >16 < f-sharp f-sharp' > < f-sharp f-sharp' >] }
		< f-sharp f-sharp' >8[ < f-sharp f-sharp' >] < f-sharp f-sharp' >[ < f-sharp f-sharp' >] < f-sharp f-sharp' >[ < f-sharp f-sharp' >]
	< e-sharp e-sharp' >8[ \tuplet 3/2 { < e-sharp e-sharp' >16 < e-sharp e-sharp' > < e-sharp e-sharp' >] } < e-sharp e-sharp' >8[ < e e' >]
		< e-sharp e-sharp' >[ < e-sharp e-sharp' >] r < e-sharp e-sharp' >
	< e! e'! > r r4 < e e' >8 r r4
	< a f-sharp' >8 r r4 < g-sharp c-sharp >8 r r4
	< f-sharp c-sharp' >8 r r4 < f-sharp c-sharp' >8 r < g-sharp d-sharp' > r
	< f-sharp c-sharp' >8 r r4 < f-sharp c-sharp' >8 r < f-sharp f-sharp' > r
	< e b' >8\ff \tuplet 3/2 { < e e' >16[ < e e' > < e e' >] } < e e' >8[ < e e' >] < e e' >[ < e e' > < e e' > < e e' >]
	< d-sharp d-sharp' >8[ \tuplet 3/2 { < d-sharp d-sharp' >16 < d-sharp d-sharp' > < d-sharp d-sharp' >] } < d-sharp d-sharp' >8[ < d d' >]
		< d-sharp d-sharp' >[ < d-sharp d-sharp' >] r < e-sharp e-sharp' >
	< f-sharp f-sharp' >[ \tuplet 3/2 { < f-sharp f-sharp' >16 < f-sharp f-sharp' > < f-sharp f-sharp' >] }
		< f-sharp f-sharp' >8[ < f-sharp f-sharp' >] < f-sharp f-sharp' >[ < f-sharp f-sharp' >] < f-sharp f-sharp' >[ < f-sharp f-sharp' >]
	< e-sharp e-sharp' >8[ \tuplet 3/2 { < e-sharp e-sharp' >16 < e-sharp e-sharp' > < e-sharp e-sharp' >] } < e-sharp e-sharp' >8[ < e e' >]
		< e-sharp e-sharp' >[ < e-sharp e-sharp' >] r < e-sharp e-sharp' >
	< e! e'! > r r4 < e e' >8 r r4
	< a f-sharp' >8 r r4 < g-sharp c-sharp >8 r r4
	< g! d-sharp' >8 r r4 r8 < d-sharp d-sharp' >8\p~ < d-sharp d-sharp' >[~ < d-sharp d-sharp' >]~
	< d-sharp d-sharp' > r8 r4 r2
	r2 r8 < d-sharp d-sharp' >8\p~ < d-sharp d-sharp' >[~ < d-sharp d-sharp' >]~
	< d-sharp d-sharp' > r8 r4 r2
	r2 r8 < g-sharp d-sharp' >->\mf[~ < g-sharp d-sharp' >] r
	r2 r8 < g-sharp d-sharp' >->[~ < g-sharp d-sharp' >] r
	r4 r8 < g! c-sharp >~ < g c-sharp > r r4
	r4 r8 < f-sharp d-sharp' >~ < f-sharp d-sharp' > r r4
	r2 r4 r8 < g-sharp e' >\mf(
	< a e' >) r r4 r8 << { a4^\p a8~ } \\ { g!4 f8~ } >>
	<< { a8 } \\ { f8 } >> r8 r4 r2
	r2 r8 << { a4\p a8~ } \\ { g!4 f8~ } >>
	<< { a8 } \\ { f8 } >> r8 r4 r2
	
	R1*2
	
	r4 r8 << { g8~ g } \\ { c-sharp,8\mf~ c-sharp } >> r8 r4
	r r8 << { a'8~ a } \\ { c,8~ c } >> r8 r << { f-sharp8( } \\ { d8~_\cr } >>
	<< { g8) } \\ { d8 } >> r8 r4 r8 < f f' >8~ < f f' > r
	r8 < e-flat e-flat' >~ < e-flat e-flat' > r r < c-sharp c-sharp' >~ < c-sharp c-sharp' > r
	
	R1*24
	
	r2 < a f-sharp' >2\p_\markup { \translate #(cons 4 -1) \italic cresc. }^\markup {I.II.}
	r2 < a f-sharp' >
	< a f-sharp' >\< < a f-sharp' >
	< b f-sharp' >\! < c f >4 < e-flat c' >
	<< { c'8[ \tuplet 3/2 { e16 e e] } } \\ { e,!8\ff[ \tuplet 3/2 { e16 e e] } } >>
		< e e' >8[ < e e' >] < e e' >[ < e e' >] < e e' >[ < e e' >]
	< d d' >[ \tuplet 3/2 { < d d' >16 < d d' > < d d' >] } < d d' >8[ < c-sharp c-sharp' >]
		< d d' >[ < d d' >] r < e e' >
	r8 \tuplet 3/2 { < f f' >16[ < f f' > < f f' >] } < f f' >8[ < f f' >] < f f' >[ < f f' >] < f f' >[ < f f' >]
	< e e' >8[ \tuplet 3/2 { < e e' >16 < e e' > < e e' >] } < e e' >8[ < d-sharp d-sharp' >] < e e' >[ < e e' >] r < e e' >
	< f! f'! > r r4 < g g' >8 r r4
	< f f' >8 r r4 < e e' >8 r r4
	< f f' >8 r < f f' > r < b-flat g' > r < a d > r
	< e b' >\ff r4 << { f8 f-sharp } \\ { r4 } >> r8 r4
	r2 r4 r8 << { b8 } \\ { a8 } >>
	<< { b8 } \\ { g-sharp8 } >> r4 << { f!8 f-sharp } \\ { r4 } >> r8 r4
	r2 r4 r8 << { b8 } \\ { a8 } >>
	<< { b8 } \\ { g-sharp8 } >> r4 << { f-sharp8 g } \\ { r4 } >> r8 r4
	r2 r4 r8 << { c!8 } \\ { c8 } >>
	<< { c-sharp8 } \\ { a-sharp8 } >> r4 << { g!8 g-sharp } \\ { r4 } >> r8 r4
	r2 r4 r8 << { c-sharp8 } \\ { c-sharp8 } >>
	<< { d!8 } \\ { b!8 } >> r8 < b, b' >4 < c! c'! > < c-sharp c-sharp' >
	< d d' > < d-sharp d-sharp' > < e e' > < f! f'! >
	< f-sharp f-sharp' >8\ff r < f-sharp f-sharp' > r < f-sharp f-sharp' > r < f-sharp f-sharp' > r
	< f-sharp f-sharp' >8 r < f-sharp f-sharp' > r < f-sharp f-sharp' > r < f-sharp f-sharp' > r
	< g-sharp e' > r r4 r2
	< f-sharp f-sharp' >8 r < f-sharp f-sharp' > r < f-sharp f-sharp' > r < f-sharp f-sharp' > r
	< g-sharp e' > r r4 r2
	< f-sharp f-sharp' >8 r < f-sharp f-sharp' > r < f-sharp f-sharp' > r < f-sharp f-sharp' > r
	< g-sharp e' > r r4 r2
	
	s1*46
	
	s1*30
	
	< c, c' >8\f r < c c' > r < c c' > r r4
	< c c' >8 r < c c' > r < c c' > r r4
	< c c' >8[_\cr < c c' >16. < c c' >32] < c c' >8 r < d d' >8[ < d d' >16. < d d' >32] < d d' >8 r
	< d d' >8[ < d d' >16. < d d' >32] < d d' >8 r < e-flat e-flat' >8[ < e-flat e-flat' >16. < e-flat e-flat' >32] < e-flat e-flat' >8 r
	< a e'! >8\ff r < a e' > r << { e'4^> } \\ { a,8[( g-sharp]) } >> r4
	< a e'! >8 r < a e' > r << { e'4^> } \\ { a,8[( g-sharp]) } >> r4
	
	R1*4
	
	r4^\markup {I.II.} < b d >->\pp r < a c-sharp >->
	r < c-sharp e >-> r < b d >->
	
	R1*11
	
	<< { R1 } \\ { r2 r8 c-sharp,8\pp d[ d] } >>
	<< { R1 } \\ { e-flat8[ c] d[ b-flat] c r r4 } >>
	<< { R1 } \\ { r2 r8 c-sharp8 d[ d] } >>
	<< { R1 } \\ { e-flat8[ c] d[ b-flat] c r r4 } >>
	r2 r8 < b-flat f' >\p[^\markup {I.II.} < b-flat f' > < b-flat f' >]
	r2 r8 < a e' >\p[ < a e' > < a e' >]
	
	R1*2
	
	r2^\markup {I.II.} r4 \tuplet 3/2 { < a' c-sharp >8\f[ < a c-sharp > < a c-sharp >] }
	r2 r4 \tuplet 3/2 { < a c-sharp >8[ < a c-sharp > < a c-sharp >] }
	r8 < a-sharp c-sharp > r4 r8 < b e > r4
	r8 < a! c! > r4 r8 < g c > r4
	r8 < f c' >4->\pp < f c' >8 r < f-sharp b >4-> < f-sharp b >8
	r8^\markup {I.II.} < e b' >4-> < e b' >8 r < e a >4-> < e a >8
	r8 < d a' >\< r < e a > r < f a >~ < f a >\! r
	r8 < d a' >\< r < e a > r < f a >~ < f a >\! r
	
	R1*2
	
	< a, e' >16\p[^\markup {I.II.} r < a-sharp f-sharp' > r < b f-sharp' > r < b-sharp g-sharp' >] r
		< c-sharp a' >[ r < a-sharp f-sharp' > r < b f-sharp' > r < b-sharp g-sharp' >] r
	<< { a'16[ r g! r f-sharp r f] r e[ r a,] r b4^> } \\ { c-sharp16 r r8 r4 r2 } >>
	<< { e16[ r f-sharp r f-sharp r g-sharp] r a[ r f-sharp r f-sharp r g] r } \\
		{ b,16[ s a-sharp s b! s b-sharp] s c-sharp[ s a-sharp s b s b-sharp] s } >>
	<< { a'16[ r g! r f-sharp r f] r e[ r a,] r b4^> } \\ { c-sharp16 r r8 r4 r2 } >>
	<< { e16 } \\ { b16 } >> r16 r8 r4 r2
	
	R1*2
	
	r2 < a f-sharp' >8\f r r4
	r2 < a f'! >8^\f r r4
	r2 < f' a >8 r r4
	r2 < e-flat a-flat >8\f r r4
	< e-flat a-flat >8[ < e-flat a-flat > < e-flat a-flat > < e-flat a-flat >] < e-flat a >\f r r4
	< e! e'! >8\f r r4 < e e' >8 r r4
	< f f' >8 r r4 < f f' >8 r r4
	< a b >8[ < a b >] r < a b >[ < a b > < a b >] r < a b >
	< a c >[ < a c >] r < a c >[ < a c > < a c >] r < a c >
	r8^\markup {I.II.} < d, c' >8\mf~ < d c' >4_\cr r8 < d c' >8~ < d c' >4
	r8 < d c' >8~ < d c' >4 r8 < d c' >8~ < d c' >4
	r8 < d c' > r < d c' > r < d c' > r < d c' >
	< d c' >2:8 < d c' >2:
	
	%%% CODA %%%
	
	< e c-sharp' >8\f r r4 r2
	
	R1*2
	
	r4^\markup {I.II.} < f c' >2\f r4
	r4 < e b' >2 r4
	r4 < d a' >2 r4
	
	R1*5
	
	<< { f'1\f } \\ { R1 } >>
	< f-sharp, f-sharp' >1\f
	< e e' >8\ff r r4 r2
	
	R1*2
	
	r4^\markup {III.IV.} < a, a' >4^>\mf~\< < a a' >8\! r r4
	r2 r8 < d' e >8\ff[ < d e > < d e >]
	< d f > r r4 r8 < d e >\ff[ < d e > < d e >]
	< d f > r r < d e > < d f > r r < d e >
	< d f > r r < a b > < a c >[ < a c > < a c > < a c >]
	< a c-sharp >\ff r r4 < a, a' >4 < a a' >8 < a a' >
	< a a' > r r4 < a a' >4 < a a' >8 < a a' >
	< a a' > r r4 r2
	r2 < d d' >8^> r r << { d'8 } \\ { d8 } >>
	<< { e8 } \\ { c-sharp8 } >> r r4 < a, a' >4 < a a' >8 < a a' >
	< a a' > r r4 < a a' >4 < a a' >8 < a a' >
	< a a' > r r4 r2
	r2 < d d' >8^> r r << { d'8 } \\ { d8 } >>
	< c-sharp e >8 r < f-sharp, c-sharp' > r < c-sharp' e > r < c-sharp e > r
	< c-sharp e >8 r < f-sharp, c-sharp' > r < c-sharp' e > r < c-sharp e > r
	< c-sharp e > r < c-sharp f-sharp > r < c-sharp e > r < c-sharp f-sharp > r
	< c-sharp e > r < c-sharp f-sharp > r < c-sharp e > r < c-sharp f-sharp > r
	<< { e8[ a, c-sharp! c-sharp] } \\ { c-sharp8[ a a a] } >> < c-sharp e >8[ < c-sharp e > < c-sharp e > < c-sharp e >]
	< c-sharp e >4 < c-sharp e > < c-sharp e > < c-sharp e >
	< c-sharp, e >1\fermata
}
