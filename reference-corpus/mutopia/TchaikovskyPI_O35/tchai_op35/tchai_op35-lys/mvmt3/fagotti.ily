\version "2.20.0"

theBassoons =  \relative d {
	\set Score.skipBars = ##t
	
	\clef "bass"
	\key d \major
	
	< a a' >8\ff r r4
	< b-flat, b-flat' >2
	< b-flat' b-flat' >2
	< b-flat b-flat' >4 < a a' >8 r
	R1*2/4
	< b-flat, b-flat' >4 < b b' >
	< c-sharp c-sharp' > < d d' >
	< c-sharp c-sharp' >8 r r4
	R1*2/4
	
	\clef "tenor"
	<< { g-sharp'''8-.[ g-sharp16( f-sharpsharp] g-sharp8)[ g-sharp,-.] } \\
		{ g-sharp'8-.[ g-sharp16( f-sharpsharp] g-sharp8)[ g-sharp,-.] } >>
	<< { a4~ a8 } \\ { a4~ a8 } >> r8
	
	\clef "bass"
	<< { a-sharp,4~ a-sharp8 } \\ { a-sharp4\ff~ a-sharp8 } >> r8
	<< { b2 } \\ { b2 } >>
	d2
	< e d' >4 < e-sharp d' >
	< f-sharp d' > << { a,8 } \\ { a8 } >> r8
	
	R1*2/4*40
	
	< d, d' >16\f r r8 r4
	
	R1*2/4*9
	
	< e' c-sharp' >8\p r < e c' > r
	< e d' > r < a c-sharp > r
	
	R1*2/4*32
	
	< d, a' >2:\p
	< d g >2:
	< d g >2:
	< d g >8[\< < d g >] < d f-sharp >[ < d f-sharp >]\!
	< d, d' >16\f r r8 r4
	< d d' >16\mf r r8 r4
	
	R1*2/4*38
	
	< a' a' >8 r r4
	
	R1*2/4*3
	
	<< { b'2^>^\p~ } \\ { R1*2/4 } >>
	<< { b4 d,~( } \\ { R1*2/4 } >>
	<< { d4 c-sharp8[ b-sharp] } \\ { R1*2/4 } >>
	<< { c-sharp8) r r4 } \\ { R1*2/4 } >>
	<< { b'2^>^\p~ } \\ { R1*2/4 } >>
	<< { b4 d,~( } \\ { R1*2/4 } >>
	<< { d4 c-sharp8[ b-sharp] } \\ { R1*2/4 } >>
	<< { c-sharp8) r r4 } \\ { R1*2/4 } >>
	
	R1*2/4*7
	
	r4 < a e' >4^>\p
	< a e' >4^> < a e' >4^>
	< a e' >4^> < a e' >4^>
	< a e' >4^> < a e' >4^>
	< a e' >4^> < a e' >4^>
	< a e' >4^> < a e' >4^>
	< a e' >4^> < a e' >4^>
	< a e' >4^> < a e' >4^>
	< a e' >4^> r
	
	R1*2/4*15
	
	r4 < f-sharp f-sharp' >8\mf[ < f-sharp f-sharp' >]
	< f-sharp f-sharp' >4 < e e' >8[ < d d' >]
	< c-sharp c-sharp' >[( < b b' >]) < f-sharp' f-sharp' >8[ < f-sharp f-sharp' >]
	< f-sharp f-sharp' >4 < e e' >8[ < d d' >]
	< c-sharp c-sharp' >[( < b b' >]) a'[ < a a' >]
	< f-sharp f-sharp' >4 < e e' >8[ < d d' >]
	< c-sharp c-sharp' >[( < b b' >]) < f-sharp' f-sharp' >8[ < f-sharp f-sharp' >]
	< e e' >[( < d d' > < c-sharp c-sharp' > < b b' >]
	a'8) r r4
	
	R1*2/4*9
	
	<< { r4 a'8-.[( b-.]) } \\ { R1*2/4 } >>
	<< { c4 \grace { b16[( c] } b8[ a]) } \\ { R1*2/4 } >>
	<< { \grace { a16[( b] } a8[ g-sharp]) r4 } \\ { R1*2/4 } >>
	
	R1*2/4*38
	
	< d, d' >16\f r r8 r4
	
	R1*2/4*9
	
	< e' c-sharp' >8\p r < e c' >\< r
	< e d' > r < a c-sharp >\! r
	
	R1*2/4*53
	
	r4 r8 < c, e-flat' >8\p
	< b-flat b-flat' >8\ff r < b-flat,! b-flat' >[ < b-flat b-flat' >]
	< f' f' >[ < f f' >] < e! e'! > r
	
	R1*2/4*2
	
	< b-flat b-flat' >8 r < b-flat b-flat' >[ < b-flat b-flat' >]
	< f' f' >[ < f-sharp f-sharp' >] < g g' > r
	
	R1*2/4*2
	
	< e-flat e-flat' >8 r < e-flat e-flat' >[ < e-flat e-flat' >]
	< e-flat e-flat' >[ < e-flat e-flat' >] < e-flat e-flat' > r
	
	R1*2/4*2
	
	< g g' >8 r < g g' >[ < g g' >]
	< g g' >[ < g g' >] < g g' > r
	r4 r8 < g g' >
	< g g' >[ < g g' >] < g g' > r
	r4 r8 < g g' >
	< g g' >[ < g g' > < g g' > < g g' >]
	< g g' >[ < g g' > < g g' > < g g' >]
	< g g' >[ < g g' > < g g' > < g g' >]
	< f-sharp! f-sharp'! > r r4
	
	R1*2/4*15
	
	< g g' >8\ff r r4
	
	R1*2/4*3
	
	<< { a'2^>^\p~ } \\ { R1*2/4 } >>
	<< { a4 c,~( } \\ { R1*2/4 } >>
	<< { c4 b8[ a-sharp] } \\ { R1*2/4 } >>
	<< { b8) r r4 } \\ { R1*2/4 } >>
	<< { a'2^>~ } \\ { R1*2/4 } >>
	<< { a4 c,~( } \\ { R1*2/4 } >>
	<< { c4 b8[ a-sharp] } \\ { R1*2/4 } >>
	<< { b8) r r4 } \\ { R1*2/4 } >>
	
	R1*2/4*32
	
	< g' d' >2\pp
	< g d' >
	< g d' >
	< g d' >
	< g d' >
	< g d' >
	< g d' >
	
	%%% MOLTO MENO MOSSO %%%
	
	< g d' >8 r r4
	
	R1*2/4*9
	
	<< { r4 b8-.^\p[( c-sharp-.]) } \\ { R1*2/4 } >>
	<< { \grace { b16[ c-sharp] } d4 c-sharp8[ b] } \\ { R1*2/4 } >>
	<< { \grace { b16[^( c-sharp] } b8[ a]^) } \\ { R1*2/4 } >>
	R1*2/4
	<< { r4 b8-.[( c-sharp-.]) } \\ { R1*2/4 } >>
	<< { \grace { b16[ c-sharp] } d4 c-sharp8[ b] } \\ { R1*2/4 } >>
	<< { \grace { b16[^( c-sharp] } b8[ a]^) } \\ { R1*2/4 } >>
	
	R1*2/4*23
	
	<< { r8 e,\p[^(\< g b-flat] } \\ { d,1*2/4\rest } >>
	<< { c-sharp'8[ e]^)\! a4^>~ } \\ { R1*2/4 } >>
	<< { a8[( d,,\< f b]\! } \\ { R1*2/4 } >>
	<< { d8[ f]) b4->( } \\ { R1*2/4 } >>
	<< { a8) r r4 } \\ { R1*2/4 } >>
	<< { r4 < d,, f' >4\pp( } \\ { R1*2/4 } >>
	<< { < a' e' >4) r } \\ { R1*2/4 } >>
	<< { r4 < d, f' >4( } \\ { R1*2/4 } >>
	<< { < a' e' >4) r } \\ { R1*2/4 } >>
	
	R1*2/4*15
	
	< d, d' >16\f r r8 r4
	
	R1*2/4*9
	
	< e' c-sharp' >8\p r < e c' > r
	< e d' > r < a c-sharp > r
	
	R1*2/4*32
	
	< d, a' >2:\p
	< d g >2:
	< d g >2:
	< d g >8[\< < d g >] < d f-sharp >[ < d f-sharp >]\!
	< d, d' >16\f r r8 r4
	< d d' >16\mf r r8 r4
	
	R1*2/4*26
	
	<< { a'2~ } \\ { a2\p~ } >>
	<< { a2~ } \\ { a2~_\markup { \italic {poco a poco cresc.}} } >>
	<< { a2~ } \\ { a2~ } >>
	<< { a2 } \\ { a2 } >>
	<< { a2~ } \\ { a2~ } >>
	<< { a2~ } \\ { a2~ } >>
	<< { a2~ } \\ { a2~ } >>
	<< { a2 } \\ { a2 } >>
	<< { a2~^\cr } \\ { a2~ } >>
	<< { a2~ } \\ { a2~ } >>
	<< { a2~ } \\ { a2~ } >>
	<< { a2~ } \\ { a2~ } >>
	<< { a2~ } \\ { a2~ } >>
	<< { a2~ } \\ { a2~ } >>
	<< { a2~ } \\ { a2~ } >>
	<< { a2 } \\ { a2 } >>
	<< a2 \\ a2\f >>
	<< a2 \\ a2 >>
	<< a2 \\ a2 >>
	<< a2 \\ a2 >>
	r8 << a8 \\ a8 >> r << a8 \\ a8 >>
	r << a8 \\ a8 >> r << a8 \\ a8 >>
	r << a8 \\ a8 >> r << a8 \\ a8 >>
	r << { a8[ a a] } \\ { a8[ a a] } >>
	< d, d' >8\ff r < d d' >[ < d d' >]
	< g g' >[ < g g' >] < d d' > r
	
	R1*2/4*2
	
	< b b' >8 r < b b' >[ < b b' >]
	< e e' >[ < e e' >] < b b' > r
	
	R1*2/4*2
	
	< g' g' >8 r < g g' >[ < g g' >]
	< c g' >[ < c g' >] < g g' > r
	
	R1*2/4*2
	
	< e e' >8 r < e e' >[ < e e' >]
	< a a' >[ < a a' >] < e e' > r
	
	R1*2/4*2
	
	< e e' >8 r < e e' >[ < e e' >]
	< a a' >[ < a a' >] < e e' > r
	
	R1*2/4*2
	
	< e e' >8 r < e e' >[ < e e' >]
	R1*2/4
	< e e' >8 r < e e' >[ < e e' >]
	R1*2/4
	< e e' >8[ < e e' >] r4
	< e e' >8[ < e e' >] r4
	< d d' >8[ < d d' >] r4
	< c-sharp c-sharp' >8[ < c-sharp c-sharp' >] r4
	< c c' >8[ < c c' >] r4
	< b b' >8[ < b b' >] r4
	< b-flat b-flat' >8[ < b-flat b-flat' >] r4
	
	R1*2/4*3
	
	r8 << { a-sharp'8[ b c-sharp] } \\ { a-sharp\f[ b, c-sharp] } >>
	< d d' >8[ < d-sharp d-sharp' > < e e' > < f-sharp f-sharp' >]
	< g g' >[ < g-sharp g-sharp' > < a a' > < b b' >]
	< a a' >[ < g! g'! > < f-sharp f-sharp' > < e e' >]
	< d d' > r r4
	R1*2/4
	r4 << { c-sharp'8->[ c-sharp->] } \\ { c-sharp,8->\f[ c-sharp->] } >>
	<< { c-sharp'4-> b8->[ a->] } \\ { c-sharp,4-> b'8->[ a->] } >>
	< d, d' >8\f r r4
	R1*2/4
	r4 << { c-sharp'8->[ c-sharp->] } \\ { c-sharp,8->[ c-sharp->] } >>
	<< { c-sharp'4-> b8->[ a->] } \\ { c-sharp,4-> b'8->[ a->] } >>
	< d, d' >8 r r4
	
	R1*2/4*3
	
	< d d' >8 r r4
	
	R1*2/4*3
	
	< d d' >8\f r << a'8 \\ a8 >> r
	< d, d' >8 r << a'8 \\ a8 >> r
	< d, d' >8 r << a'8 \\ a8 >> r
	< d, d' >8 r << a'8 \\ a8 >> r
	< d, d' >[^( < f-sharp f-sharp' > < a a' > < a-sharp a-sharp' >]
	< b b' >[ < d d' >^) < a! a'! >^( < g g' >]
	< f-sharp f-sharp' >[ < d d' >^) < a'! a'! >^( < a-sharp a-sharp' >]
	< b b' >[ < d d' >^) < a! a'! >^( < g g' >]
	< f-sharp f-sharp' >^)[ < b b' > < a a' > < g g' >]
	< f-sharp f-sharp' >[ < b b' > < a a' > < g g' >]
	< f-sharp f-sharp' > r r4
	< f f' >8 r r4
	< e e' >8 r r4
	< a a' >8 r r4
	<< { d8[ a d a] } \\ { d,8\ff[ a' d, a'] } >>
	<< { d8[ a d a] } \\ { d,8[ a' d, a'] } >>
	<< { d8[ a d a] } \\ { d,8[ a' d, a'] } >>
	<< { d8[ a d a] } \\ { d,8[ a' d, a'] } >>
	< d, d' >8 r < d d' >[ < d d' >]
	< a' a' >[ < a a' >] < d, d' >[ < f-sharp f-sharp' >]
	< a a' > r r << a8 \\ a8 >>
	< d, d' >8 r r4\fermata
}
