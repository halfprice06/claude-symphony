\version "2.20.0"

theHornsfirst =  \relative c' {
	\transposition f
	\clef "treble"
	\key c \major	
	
	< e e' >8\ff r r4
	r4 << { b'4~ } \\ { a4~ } >>
	<< { b4 b,4~ } \\ { a'4 a,~ } >>
	<< { b b'8 } \\ { a,4 e'8 } >> r8
	
	R1*2/4
	
	r4 < d-sharp b' >~
	< d-sharp b' > < b d-sharp >
	< b e >8 r r4
	
	R1*2/4*4
	
	< a f-sharp' >2
	< c-sharp a' >
	< d b' >4 < d-sharp c' >
	< e c-sharp' > < g-sharp e' >8 r
	
	R1*2/4*40
	
	< f-sharp f-sharp' >16\f r r8 r4
	
	R1*2/4*7
	
	< f f' >8\f r r4
	R1*2/4
	< e b' >8\p r < e b' > r
	< f-sharp b > r < e b' > r
	
	R1*2/4*20
	
	< c c' >4\f^>(^\markup {I.II.} < b b' >)
	< b b' >8 r r4
	< c c' >4^>( < b b' >^>)
	< b b' >8 r r4
	
	R1*2/4*8
	
	<< { R1*2/4 } \\ { c-sharp2:8\p } >>
	< b e >2:
	< b e >2:
	< b e >8[\< < b e >] < a e' >[ < a e' >]\!
	< c-sharp c-sharp' >16\f r r8 r4
	< f-sharp d' >16\mf r r8 r4
	
	R1*2/4*38
	
	< e e' >8 r r4
	
	R1*2/4*34
	
	r4 << { c-sharp'8[^\markup {I.II.} c-sharp] } \\ { c-sharp8\mf[ c-sharp] } >>
	<< { c-sharp4-> b8[ a] } \\ { c-sharp4-> b8[ a] } >>
	<< { g-sharp8[ f-sharp] c-sharp'8[ c-sharp] } \\ { g-sharp8[ f-sharp] c-sharp'[ c-sharp] } >>
	<< { c-sharp4-> b8[ a] } \\ { c-sharp4-> b8[ a] } >>
	<< { g-sharp4 e'8[ b] } \\ { g-sharp4 e'8[ b] } >>
	<< { c-sharp4-> b8[ a] } \\ { c-sharp4-> b8[ a] } >>
	<< { g-sharp8[ f-sharp] c-sharp'8[ c-sharp] } \\ { g-sharp8[ f-sharp] c-sharp'[ c-sharp] } >>
	<< { c-sharp4-> b8[ a] } \\ { c-sharp4-> b8[ a] } >>
	<< { g-sharp4 } \\ { g-sharp4 } >> r4
	
	R1*2/4*58
	
	< f-sharp f-sharp' >16\f r r8 r4
	
	R1*2/4*7
	
	< f f' >8\f r r4
	R1*2/4
	< e b' >8\p r < e b' >\< r
	< f-sharp b > r < e b' >\! r
	
	R1*2/4*20
	
	< c c' >4\f^>(^\markup {I.II.} < b b' >)
	< b b' >8 r r4
	< c c' >4^>( < b b' >^>)
	< b b' >8 r r4
	
	R1*2/4*29
	
	r4^\markup {I.II.} r8 < c c' >8\p
	< c a' >\ff r < c a' >[ < c a' >]
	< e c' >[ < e c' >] < f d-flat' > r
	
	R1*2/4*2
	
	< c a' >8 r < c a' >[ < c a' >]
	< e c' >[ < e b-flat' >] < f d' > r
	
	R1*2/4*2
	
	< b-flat f' >8 r < b-flat f' >[ < b-flat f' >]
	< b-flat g' >[ < b-flat g' >] < b-flat f' > r
	
	R1*2/4*2
	
	< g d' >8 r < g d' >[ < g d' >]
	< f-sharp a >[ < f-sharp a >] < g b > r
	r4 r8 < g d' >
	< f-sharp a >[ < f-sharp a >] < g b > r
	r4 r8 < g d' >
	< f-sharp a >[ < f-sharp a > < g b > < g b >]
	< f-sharp a >[ < f-sharp a > < g b > < g b >]
	< f-sharp a >[ < f-sharp a > < g b > < g b >]
	< g b-flat >8 r r4
	
	R1*2/4*15
	
	< a f-sharp' >8\ff r r4
	
	R1*2/4*18
	
	<< { r4^\markup {I. Solo.} c-sharp4^>^\p~ } \\ { R1*2/4 } >>
	<< { c-sharp4 a^>~ } \\ { R1*2/4 } >>
	<< { a4 d^>~ } \\ { R1*2/4 } >>
	<< { d4 a^>~ } \\ { R1*2/4 } >>
	<< { a4 c-sharp4^>~ } \\ { R1*2/4 } >>
	<< { c-sharp4 a^>~ } \\ { R1*2/4 } >>
	<< { a4 d^>~ } \\ { R1*2/4 } >>
	<< { d4 a^>~ } \\ { R1*2/4 } >>
	<< { a4 r4 } \\ { R1*2/4 } >>
	
	R1*2/4*7
	
	r4^\markup {I.II.} << { b8[ b] } \\ { b8\mf[ b] } >>
	<< { b4^> a8[ g] } \\ { b4-> a8[ g] } >>
	<< { f-sharp8[ e] b'[ b] } \\ { f-sharp8[ e] b'[ b] } >>
	<< { b4^> a8[ g] } \\ { b4-> a8[ g] } >>
	<< { f-sharp4 d'8[ a] } \\ { f-sharp4 d'8[ a] } >>
	<< { b4^> a8[ g] } \\ { b4-> a8[ g] } >>
	<< { f-sharp8[ e] b'[ b] } \\ { f-sharp8[ e] b'[ b] } >>
	<< { b4^> a8[ g] } \\ { b4-> a8[ g] } >>
	<< f-sharp4 \\ f-sharp4 >> r4
	
	R1*2/4*71
	
	< f-sharp f-sharp' >16\f r r8 r4
	
	R1*2/4*7
	
	< f f' >8\f r r4
	R1*2/4
	< e b' >8\p r < e b' > r
	< f-sharp b > r < e b' > r
	
	R1*2/4*20
	
	< c c' >4\f^>(^\markup {I.II.} < b b' >)
	< b b' >8 r r4
	< c c' >4^>( < b b' >^>)
	< b b' >8 r r4
	
	R1*2/4*8
	
	<< { R1*2/4 } \\ { c-sharp2:8\p } >>
	< b e >2:
	< b e >2:
	< b e >8[\< < b e >] < a e' >[ < a e' >]\!
	< c-sharp c-sharp' >16\f r r8 r4
	< f-sharp d' >16\mf r r8 r4
	
	R1*2/4*26
	
	< c-sharp' e >8\f r r4
	r4 << { c-sharp8[ c-sharp] } \\ { c-sharp8\p[ c-sharp] } >>
	<< { c-sharp4-> b8[ a-sharp] } \\ { c-sharp4-> b8[ a-sharp] } >>
	<< { g8[( f-sharp]) } \\ { g8[( f-sharp]) } >> < e a >8->\p[ < e a >->]
	R1*2/4
	r4 << { d-sharp'8[ d-sharp] } \\ { d-sharp8[_\cr d-sharp] } >>
	<< { d-sharp4-> c-sharp8[ b-sharp] } \\ { d-sharp4-> c-sharp8[ b-sharp] } >>
	<< { a8[( g-sharp]) b-sharp[ b-sharp] } \\ { a8[( g-sharp]) f-sharp\mf[ f-sharp] } >>
	<< { g-sharp2~^\cr } \\ { e2~ } >>
	<< { g-sharp4 g-sharp8[ g-sharp] } \\ { e4 f-sharp8[ e] } >>
	<< { a2~ } \\ { f-sharp2~ } >>
	<< { a4 f-sharp8[ a-sharp] } \\ { f-sharp4 c!8[ f-sharp] } >>
	< b, g-sharp' >2~
	< b g-sharp' >4 < g-sharp b >8[ < b g-sharp' >]
	< a f-sharp' >2~
	< a f-sharp' >4 < f-sharp d-sharp' >8[ < a f-sharp' >]
	<< { f'!4->( e->) } \\ { b2\f } >>
	<< { f'!4->( e->) } \\ { b2 } >>
	<< { a'4->( g-sharp->) } \\ { d2 } >>
	<< { a'4->( g-sharp->) } \\ { d2 } >>
	r8 < g-sharp e' > r < g-sharp e' >
	r < g-sharp e' > r < g-sharp e' >
	r < g-sharp e' > r < g-sharp e' >
	r < g-sharp e' >[ < g-sharp e' > < g-sharp e' >]
	< c-sharp e >\ff r < c-sharp e >[ < c-sharp e >]
	< d f-sharp >[ < d f-sharp >] < c-sharp e > r
	
	R1*2/4*2
	
	< f-sharp, f-sharp' >8 r < f-sharp f-sharp' >[ < f-sharp f-sharp' >]
	< f-sharp f-sharp' >[ < f-sharp f-sharp' >] < f-sharp f-sharp' > r
	
	R1*2/4*2
	
	< f-sharp f-sharp' >8 r < f-sharp f-sharp' >[ < f-sharp f-sharp' >]
	< g g' >[ < b g' >] < a f-sharp' > r
	
	R1*2/4*2
	
	< f-sharp d' >8 r < f-sharp d' >[ < f-sharp d' >]
	< g e' >[ < g e' >] < f-sharp d' > r
	
	R1*2/4*2
	
	< f-sharp d' >8 r < f-sharp d' >[ < f-sharp d' >]
	< g e' >[ < g e' >] < f-sharp d' > r
	
	R1*2/4*2
	
	< f-sharp d' >8 r < f-sharp d' >[ < f-sharp d' >]
	R1*2/4
	< f-sharp d' >8 r < f-sharp d' >[ < f-sharp d' >]
	R1*2/4
	< f-sharp d' >8[ < f-sharp d' >] r4
	< f-sharp d' >8[ < f-sharp d' >] r4
	< f! d' >8[ < f d' >] r4
	< e d' >8[ < e d' >] r4
	< a e' >8[ < a e' >] r4
	< a d >8[ < a d >] r4
	< d-sharp, d-sharp' >8[ < d-sharp d-sharp' >] r4
	
	R1*2/4*3
	
	r8 < g-sharp c-sharp >\f[ < f-sharp c-sharp' > < e-sharp c-sharp' >]
	< f-sharp c-sharp' > r r4
	R1*2/4
	< e e' >8[ < g-sharp b > < a c-sharp > < g-sharp d' >]
	<< { c-sharp8 r b8->[ b->] } \\ { a8 r8 r4 } >>
	<< { b4-> a8->[ g-sharp->] } \\ { R1*2/4 } >>
	<< { f!8->[( e]) r4 } \\ { R1*2/4 } >>
	R1*2/4
	< e e' >8\f r << { b'8->[ b->] } \\ { r4 } >>
	<< { b4-> a8->[ g-sharp->] } \\ { R1*2/4 } >>
	<< { f8->[( e]) r4 } \\ { R1*2/4 } >>
	R1*2/4
	< e e' >8 r r4
	
	R1*2/4*3
	
	< c-sharp c-sharp' >8 r r4
	
	R1*2/4*3
	
	< c-sharp c-sharp' >8 r < e e' > r
	< e e' > r < e e' > r
	< e e' > r < e e' > r
	< e e' > r < e e' > r
	< e e' > r < a c-sharp >[ < a c-sharp >]
	< a c-sharp >4 < a c-sharp >8[ < a d >]
	< a e' > r < a c-sharp >[ < a c-sharp >]
	< a c-sharp >4 < a c-sharp >8[ < a d >]
	< a e' >8[ < a c-sharp > < a c-sharp > < a d >]
	< a e' >8[ < a c-sharp > < a c-sharp > < a d >]
	< a e' > r r4
	< e e' >8 r r4
	< f-sharp f-sharp' >8 r r4
	< d' e >8 r r4
	< c-sharp e >8\ff[ < e, b' >] < e c-sharp' >[ < e b' >]
	< e c-sharp' >[ < e b' > < e c-sharp' > < e b' >]
	< e c-sharp' >[ < e b' > < e c-sharp' > < e b' >]
	< e c-sharp' >[ < e b' > < e c-sharp' > < e b' >]
	< e c-sharp' > r < e c-sharp' >[ < e c-sharp' >]
	< e e' >[ < e e' >] << a8 \\ a8 >> r8
	< g-sharp b > r r < e e' >
	< e e' > r r4\fermata
}
