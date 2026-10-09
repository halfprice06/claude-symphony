\version "2.20.0"

theOboes =  \relative d' {
	
	\clef "treble"
	\key d \major
	
	r1
	
	R1*5
	
	r2 r4 < f-sharp f-sharp' >\p
	< a e' > < g-sharp e' > < a e' >2
	
	R1*2
	
	<< { a4^\mf^\<^\markup { \italic marcato } f8( e d4) f8( a } \\ { b,1\rest } >>
	<< { d'8)\! r8 r4 r2 } \\ { R1 } >>
	<< { e4(^\markup { \italic piu \dynamic f } c-sharp8 b a4) c-sharp8( e } \\ { R1 } >>
	<< { a8) r8 r4 r2 } \\ { R1 } >>
	< a, a' >4\f < f f' >8( < e e' > < d d' >4) < f f' >8( < a a' >)
	< f' b >2 r
	< f b > r
	< f b >4\ff r < f b > r
	< f b >8[ < f b > < f b > < f b >] < f b >2:8
	< e a >8 << { g-sharp8[( a]) a[( b-flat]) c,[( f]) } \\ { d8\f[( c-sharp]) c-sharp[( d]) a[( b-flat]) } >> r8 
	r8 << { g-sharp'8[( a]) a[( b-flat]) c,[( f]) } \\ { d8\mf[( c-sharp]) c-sharp[( d]) a[( b-flat]) } >> r8
	
	R1*35
	
	r4 < f' b-flat >4\f~ < f b-flat >8 r r4
	r4 < a-flat, a-flat' >4~ < a-flat a-flat' >8 r r4
	< f' a >8\f[ < f a >16. < f a >32] < f a >8[ < f a >16. < f a >32] < g b-flat >8 r r4
	< f a >8[ < f a >16. < f a >32] < f a >8[ < f a >16. < f a >32] < g b-flat >8 r r4
	< f a >8[ < f a >16. < f a >32] < f-sharp a >8 r < g d' >8[ < g d' >16. < g d' >32] < g-sharp d' >8 r
	< a d >8[ < a d >16. < a d >32] < b d >8 r < d-sharp, c' >8[ < d-sharp c' >16. < d-sharp c' >32] < d-sharp c' >8 r
	< a' c-sharp! >8\ff r < a c > r << { b4-> } \\ { a8_>[( g-sharp]) } >> r4
	< a c-sharp! >8 r < a c > r << { b4-> } \\ { a8_>[( g-sharp]) } >> r4
	
	R1*21
	
	g-sharp,2_\markup { \dynamic pp \italic {poco cresc.} } a
	<< { b-flat4 b c-sharp d } \\ { g,4\p g-sharp g b } >>
	<< { e2~ e8 } \\ { c-sharp2\mf~ c-sharp8 } >> r8 r4
	
	R1*8
	
	r2 r4 \tuplet 3/2 { < c-sharp c-sharp' >8\f[ < d c-sharp' > < e c-sharp' >] }
	r2 r4 \tuplet 3/2 { < c-sharp c-sharp' >8[ < d-sharp c-sharp' > < e c-sharp' >] }
	r8 < e c-sharp' > r4 r8 < e b' > r4
	r8 < e c' > r4 r8 < e c' > r4
	
	R1*6
	
	< a, e' >16\pp[^\markup { \huge {Piu mosso.} } r < a-sharp f-sharp' > r < b f-sharp' > r < b-sharp g-sharp' >] r
		< c-sharp e >[ r < a-sharp! f-sharp' > r < b f-sharp' > r < b-sharp g-sharp'! >] r
	< c-sharp e > r r8 r4 r8 < f-sharp, c-sharp' >16 r < f-sharp d-sharp' >4^>
	< a e' >16\pp[ r < a-sharp! f-sharp' > r < b f-sharp' > r < b-sharp g-sharp'! >] r
		< c-sharp e >[ r < a-sharp f-sharp' > r < b f-sharp' > r < b-sharp g-sharp' >] r
	< c-sharp e > r r8 r4 r8 < f-sharp, c-sharp' >16 r < f-sharp d-sharp' >4^>
	< g-sharp e' >16\pp^\markup { \huge {Poco piu lento.} } r r8 r4 r2
	R1
	r8 < e c-sharp' >16\p[\< r < f-sharp c-sharp' > r < f-sharp d' >] r < g-sharp d' >[ r < g-sharp e' > r
		< a e' > r < a f-sharp' >] r
	< b g' >[ r < b g-sharp' > r < b f-sharp' > r < b g-sharp' >]\! r < d a' >8\f r r4
	< b g' >16\mf[ r < b g-sharp' > r < b f-sharp' > r < b g-sharp' >] r < d a' >8\f r r4
	< f a >16\mf[ r < f a > r < f a > r < f a >] r < f a >8\f r r4
	< f a >16\mf[ r < f a > r < f a > r < f a >] r < e-flat a-flat >8->\f r r4
	< e-flat a-flat >16\mf[ r < e-flat a-flat > r < e-flat a-flat > r < e-flat a-flat >] r < d-sharp a' >8 r r4
	
	% PIU MOSSO %
	
	< g-sharp d'! >8\f r r4 r2
	< a d >8 r r4 r2
	< d, a' >8 r r4 r2
	< f-sharp a >8 r r4 r2
	r8 < f-sharp, b-sharp >8\mf~_\markup { \translate #(cons 4 -1) \italic cresc. } < f-sharp b-sharp >4 r8
		< f-sharp b-sharp >8~ < f-sharp b-sharp >4
	r8 < f-sharp b-sharp >8~ < f-sharp b-sharp >4 r8 < f-sharp b-sharp >8~ < f-sharp b-sharp >4
	r8 < f-sharp b-sharp > r8 < f-sharp b-sharp > r8 < f-sharp b-sharp > r8 < f-sharp b-sharp >
	< f-sharp' a >8\f[\< < f-sharp a > < f-sharp a > < f-sharp a >] < f-sharp a >[ < f-sharp a >
		< f-sharp a > < f-sharp a >]\!
	< e a >8\ff[ \tuplet 3/2 { < c-sharp e >16 < c-sharp e > < c-sharp e >] } < c-sharp e >8[ < c-sharp e >]
		< c-sharp e >[ < c-sharp e > < c-sharp e > < c-sharp e >]
	< b e >8[ \tuplet 3/2 { < b e >16 < b e > < b e >] } < b e >8[ < a-sharp e' >] < b e >[ < b e >] r < c-sharp f-sharp >
	< d f-sharp >8[ \tuplet 3/2 { < d f-sharp >16 < d f-sharp > < d f-sharp >] } < d f-sharp >8[
		< d f-sharp >] < d f-sharp >[ < d f-sharp >] < d f-sharp >[ < d f-sharp >]
	< c-sharp! f-sharp >8[ \tuplet 3/2 { < c-sharp f-sharp >16 < c-sharp f-sharp > < c-sharp f-sharp >] } < c-sharp e >8[
		< b-sharp f-sharp' >] < c-sharp f-sharp >[ < c-sharp f-sharp >] r < c-sharp f-sharp >
	< d f-sharp > r r4 < a e' >8 r r4
	< b d >8 r r4 < f-sharp c-sharp' >8 r r4
	< b f-sharp' >8 r r4 < b f-sharp >8 r < c-sharp e-sharp > r
	< b f-sharp > r r4 < b f-sharp' >8 r < b e! > r
	< e a >8\ff[ \tuplet 3/2 { < c-sharp e >16 < c-sharp e > < c-sharp e >] } < c-sharp e >8[ < c-sharp e >]
		< c-sharp e >[ < c-sharp e > < c-sharp e > < c-sharp e >]
	< b e >8[ \tuplet 3/2 { < b e >16 < b e > < b e >] } < b e >8[ < a-sharp e' >] < b e >[ < b e >] r < c-sharp f-sharp >
	< d f-sharp >8[ \tuplet 3/2 { < d f-sharp >16 < d f-sharp > < d f-sharp >] } < d f-sharp >8[
		< d f-sharp >] < d f-sharp >[ < d f-sharp >] < d f-sharp >[ < d f-sharp >]
	< c-sharp! f-sharp >8[ \tuplet 3/2 { < c-sharp f-sharp >16 < c-sharp f-sharp > < c-sharp f-sharp >] } < c-sharp e >8[
		< b-sharp f-sharp' >] < c-sharp f-sharp >[ < c-sharp f-sharp >] r < c-sharp f-sharp >
	< d f-sharp > r r4 < a e' >8 r r4
	< b d >8 r r4 < f-sharp c-sharp' >8 r r4
	<< { b-sharp8^\p[ g-sharp'->]( a) r } \\ { g-sharp,8 r r4 } >> r2
	r2 r4 << { c-sharp4 } \\ { c-sharp4\p\< } >>
	<< { d-sharp8^\p[ g-sharp->]( a) r } \\ { b-sharp,8\mf\! r r4 } >> r2
	r2 r4 << { c-sharp4 } \\ { e,4\p\< } >>
	<< { c-sharp'8[ d-sharp->]( e) r } \\ { a-sharp,8\mf\! r8 r4 } >> r2
	<< { r8 d-sharp->[( e]) r r2 } \\ { R1 } >>
	<< { r8 c-sharpsharp->[( d-sharp]) r r4 r8 b-sharp8( } \\ { r2 r4 r8 g-sharp8~ } >>
	<< { c-sharp!8)[ c-sharp->]( d!8) r r4 r } \\ { g-sharp,8 r r4 r r } >>
	r4 r8 < b d-sharp >8( < b e >) < e, e' >4 < c-sharp' a' >8\f(
	< d! a' >) << { d8->[( e-flat) f->]( f-sharp) r r4 } \\ { r8 r4 r2 } >>
	R1
	<< { d8->^\p[( e-flat) f->]( f-sharp) r r4 } \\ { R1 } >>
	R1
	<< { r8 a->^\mf[( b-flat) a->]( b-flat)[ d,]~ d r } \\ { r2 r8 g,\mf~ g r } >>
	<< { r8 a'->[( b-flat) a->]( b-flat)[ d,]~ d r } \\ { r2 r8 g,~ g r } >>
	<< { r8 g-sharp->[( a) d->]( e-flat) r r f-sharp,( } \\ { r2 r4 r8 d8~ } >>
	<< { g8)[ g->]( a-flat)[ b-flat->]( b) r r4 } \\ { d,8 r r4 r2 } >>
	r4 r8 << { a'8( b-flat) } \\ { f8~_\cr f } >> r8 r << { g'8( } \\ { e-flat8~ } >>
	<< { a-flat8) } \\ { e-flat8 } >> r r < c-sharp! e >8( < c-sharp f-sharp! >) r r < b! d-sharp >(
	< b e! >\ff) r < b e >2\mf < b e >8 r
	< b d >8\f r < b d >2\mf\> < b d >8\! r
	
	R1*22
	
	r2 < f d' >\p_\markup { \translate #(cons 4 -1) \italic cresc. }
	r2 < f d' >
	< f-sharp! d' >\< < g-sharp d' >
	< g-sharp e' > < g-sharp f' >4\! < b g-sharp' >
	< c a' >8\ff \tuplet 3/2 { < f, a >16[ < f a > < f a >] } < f a >8[ < f a >] < f a >[ < f a >] < f a >[ < f a >]
	< e g >[ \tuplet 3/2 { < e g >16 < e g > < e g >] } < e g >8[ < d-sharp f-sharp! >]
		< e g >[ < e g >] r < f-sharp! a >
	r8 \tuplet 3/2 { < g b-flat >16[ < g b-flat > < g b-flat >] } < g b-flat >8[ < g b-flat >] < g b-flat >[ < g b-flat >]
		< g b-flat >[ < g b-flat >]
	< f-sharp a >8[ \tuplet 3/2 { < f-sharp a >16 < f-sharp a > < f-sharp a >] } < f-sharp a >8[ < e-sharp g-sharp >]
		< f-sharp a >[ < f-sharp a >] r < f-sharp a >
	< f b-flat > r r4 < f c' >8 r r4
	< g b-flat >8 r r4 < a d >8 r r4
	< g e-flat' >8 r < b-flat f' > r < g e-flat' > r < g d' > r
	<< { c-sharp!8[ a] b-flat r r4 c,8 } \\ { e8\ff r8 r4 r2 } >>
	<< { c-sharp8 g'4 g-sharp g-sharp e'8 } \\ { r8 e,4 d d d'8 } >>
	<< { e8[ a,] b-flat r r4 r8 c, } \\ { c-sharp'8 r r4 r r } >>
	<< { c-sharp,!8 g'!4 g-sharp g-sharp e'8 } \\ { r8 e,4 d d d'8 } >>
	<< { e8[ b-flat] b r r4 r8 c-sharp,! } \\ { c-sharp'8 r r4 r2 } >>
	<< { d,8 g-sharp4 a b-flat b'!8 } \\ { r8 f,4  d-sharp e f'8 } >>
	<< { c'8 r r4 r } \\ { f-sharp,!8[ b,] c r r4 } >> r8 d,!8
	<< { d-sharp8 a'4 b-flat b } \\ { r8 d-sharp,4 e f } >> < b-sharp b-sharp' >8
	< c-sharp! c-sharp'! > r < g a >4 < g-sharp b! > < a c >
	< b-flat c-sharp! > < b d > < c e-flat > < c-sharp e >
	< d f >8\ff r < d f >8 r < d f >8 r < d f >8 r
	< d f >8 r < d f >8 r < d f >8 r < d f >8 r
	< c-sharp e > r r4 r2
	< d f >8 r < d f >8 r < d f >8 r < d f >8 r
	< c-sharp e > r r4 r2
	< d f >8 r < d f >8 r < d f >8 r < d f >8 r
	< c-sharp e > r r4 r2
	
	s1*46
	
	s1*30
	
	< b-flat f' >8\f[ < b-flat g' >16. < b-flat a' >32] < b-flat f' >8[ < b-flat g' >16. < b-flat a' >32] < c f >8 r r4
	< b-flat f' >8[ < b-flat g' >16. < b-flat a' >32] < b-flat f' >8[ < b-flat g' >16. < b-flat a' >32] < c f >8 r r4
	< b-flat f' >8[_\cr < b-flat g' >16. < b-flat a-flat' >32] < b g' >8 r < c g' >8[ < c a' >16. < c b-flat' >32] < c-sharp a' >8 r
	< d a' >8[ < d b-flat' >16. < d c' >32] < d b-flat' >8 r < f g-sharp >8[ < f g-sharp >16. < f g-sharp >32] < f g-sharp >8 r
	< d f-sharp! >8\ff r < d f >8 r << { e4-> } \\ { d8[( c-sharp]) } >> r4
	< d f-sharp! >8 r < d f >8 r << { e4-> } \\ { d8[( c-sharp]) } >> r4
	
	R1*25
	
	r2 r4 \tuplet 3/2 { < d f-sharp >8\f[ < d f-sharp > < d f-sharp >] }
	r2 r4 \tuplet 3/2 { < d f-sharp >8[ < d f-sharp > < d f-sharp >] }
	r8 < d-sharp f-sharp > r4 r8 < e a > r4
	r8 < d! f > r4 r8 < c! f > r4
	
	R1*6
	
	<< { f-sharp,16_\pp[^\markup { \huge {Piu mosso.}} r f-sharp r g r g-sharp] r a[ r f-sharp r g r g-sharp] r } \\ { R1 } >>
	<< { a16 r r8 r4 r8 d,16 r d4-> } \\ { R1 } >>
	<< { e16[ r f-sharp r g r g-sharp] r a[ r f-sharp r g r g-sharp] r } \\ { R1 } >>
	<< { a16 r r8 r4 r8 d,16 r d4-> } \\ { R1 } >>
	e16 r r8 r4 r2
	
	R1*2
	
	r2 < g d' >8\f r r4
	r2 < g d' >8\f r r4
	r2 < b-flat f' >8 r r4
	r2 < d-flat a-flat' >8\f r r4
	r2 < g-sharp, g-sharp' >8\f r r4
	< a a' >8\f r r4 < a a' >8 r r4
	< b-flat b-flat' >8 r r4 < b-flat b-flat' >8 r r4
	< g' d' >8[ < g d' >] r < g d' >[ < g d' > < g d' >] r < g d' >
	< b! d >[ < b d >] r < b d >[ < b d > < b d >] r < b d >
	r8 < b, e-sharp >8\mf~ < b e-sharp >4_\cr r8 < b e-sharp >8~ < b e-sharp >4
	r8 < b e-sharp >8~ < b e-sharp >4 r8 < b e-sharp >8~ < b e-sharp >4
	r8 < b e-sharp >8 r < b e-sharp > r < b e-sharp > r < b e-sharp >
	< b e-sharp >2:8 < b e-sharp >:
	
	< a f-sharp' >8\f r r4 r2
	
	R1*2
	
	r4 < b-flat f' >2\f r4
	r4 < a e' >2 r4
	r4 < g d' >2 r4
	r4 < c f >8[ < b d-sharp >] < b e > r < b e >[ < a c >]
	< a d! > r r4 r2
	< a d >8 r r4 r2
	< a-flat d >8 r r4 r2
	< b-flat e-flat >8\f r < a d > r < b-flat e-flat > r < a d > r
	< e-flat' b-flat' >1
	< d b'! >
	< d a' >8\ff r r4 r2
	
	R1*3
	
	r8 < g, g' >8\f[ < g g' > < g g' >] < g g' >[ < g' a >\ff < g a > < g a >]
	< g b-flat >[ < g, g' >\f < g g' > < g g' >] < g g' >[ < g' a >\ff < g a > < g a >]
	< g b-flat >[ < g, g' >\f < g g' > < g' a >\ff] < g b-flat >[ < g, g' >\f < g g' > < g' a >\ff]
	< g b-flat >[ < g, g' > < g g' > < d' b-flat' >] < d b' >[ < d-sharp e > < d-sharp e > < d-sharp b' >]
	< d a' >8\ff < d, d' >4 < d d' >8~ < d d' >[ < e e' > < f-sharp f-sharp' > < g g' >]
	< a a' >8 < d, d' >4 < d d' >8~ < d d' >[ < e e' > < f-sharp f-sharp' > < g g' >]
	< a a' >8 < d, d' >4 < e e' >8 < d d' > < c-sharp c-sharp' >4 < d d' >8
	<< { c-sharp'8 b4 g8 b-flat8-> } \\ { c-sharp,8[ d d-sharp e] e-flat8-> } >> r8 r < c-sharp' g' >
	<< { d8 } \\ { d8 } >> < d, d' >4 < d d' >8~ < d d' >[ < e e' > < f-sharp f-sharp' > < g g' >]
	< a a' > < d, d' >4 < d d' >8~ < d d' >[ < e e' > < f-sharp f-sharp' > < g g' >]
	< a a' >8 < d, d' >4 < e e' >8 < d d' > < c-sharp c-sharp' >4 < d d' >8
	<< { c-sharp'8 b4 g8 b-flat8-> } \\ { c-sharp,8[ d d-sharp e] e-flat8-> } >> r8 r < c-sharp' g' >
	<< { d8 } \\ { d8 } >> r8 < f-sharp, d' > r < d' f-sharp > r < f-sharp a > r
	< f-sharp a > r < f-sharp, d' > r < d' f-sharp > r < f-sharp a > r
	< f-sharp a > r < f-sharp b > r < f-sharp a > r < f-sharp b > r
	< f-sharp a > r < f-sharp b > r < f-sharp a > r < f-sharp b > r
	< f-sharp a >[ d, < d f-sharp > < f-sharp a >] < a d >[ < a d > < d f-sharp > < f-sharp a >]
	< f-sharp a >4 < f-sharp a > < f-sharp a > < f-sharp a >
	<< { d,1\fermata } \\ { d1 } >>
}
