\version "2.20.0"

theClarinets =  \relative a' {
	\transposition a'
	
	\clef "treble"
	\key f \major
	
	r1
	
	R1*5
	
	r2 r4 < d f >\p
	< g, e' > < d' f > < g, e' >2
	
	R1*5
	
	<< { b-flat,1\mf\< } \\ { R1 } >>
	<< { c'4\f\! a-flat8( g f4) a-flat8( c) } \\ { a-flat,1 } >>
	<< { d'2 } \\ { a-flat2 } >> r2
	<< { d2 } \\ { a-flat2 } >> r2
	<< { d4 } \\ { a-flat4\ff } >> r4 << { d4 } \\ { a-flat4 } >> r4
	< a-flat a-flat' >8[ < a-flat a-flat' >8 < a-flat a-flat' >8 < a-flat a-flat' >8] < a-flat a-flat' >2:8
	< g g' >8 << { g'8[( g]) c,[( d-flat]) a-flat[( a-flat]) } \\
		{ d-flat\f[( c]) b-flat[( a-flat]) g-flat[( f]) } >> r8
	r8 << { g'8[( g]) c,[( d-flat]) a-flat[( a-flat]) } \\
		{ d-flat\mf[( c]) b-flat[( a-flat]) g-flat[( f]) } >> r8
	
	R1*35
	
	r4 < a-flat d-flat >4\f~ < a-flat d-flat >8 r r4
	r4 < a-flat d! >4~ < a-flat d >8 r r4
	< e-flat e-flat' >8\f[ < f f' >16. < g g' >32] < e-flat e-flat' >8[ < f f' >16. < g g' >32]
		< e-flat e-flat' >8 r r4
	< e-flat e-flat' >8[ < f f' >16. < g g' >32] < e-flat e-flat' >8[ < f f' >16. < g g' >32]
		< e-flat e-flat' >8 r r4
	< e-flat e-flat' >8[ < f f' >16. < g-flat g-flat' >32] < e-flat e-flat' >8 r
		<< { f'8[ g16. a-flat32] g8 } \\ { f8[ f16. f32] f8 } >> r8
	<< { g8[ a-flat16. b-flat32] a-flat8 } \\ { f8[ f16. f32] f8 } >> r8
		< e-flat b' >8[ < e-flat c' >16. < e-flat d' >32] < e-flat c' >8 r
	<< { e8 } \\ { e8\ff } >> r8 << { e-flat8 } \\ { e-flat8 } >> r
		<< { d4-> } \\ { d4-> } >> r4
	<< { e8 } \\ { e8 } >> r8 << { e-flat8 } \\ { e-flat8 } >> r
		<< { d4-> } \\ { d4-> } >> r4
		
	R1*16
		
	<< { r2 \tuplet 3/2 { r8 g^\mf^>[~ g]~( } \tuplet 3/2 { g8[ \tuplet 3/2 { g16 e c } \tuplet 3/2 { g e c] } } } \\ { R1 } >>
	<< { g8) r r4 \tuplet 3/2 { r8 a''^>[~ a]~ } \tuplet 3/2 { a8[ \tuplet 3/2 { a16( f d } \tuplet 3/2 { a f d] } } } \\ { R1 } >>
	<< { a8) } \\ { s8 } >> r8 r4 r2
	
	R1*2
	
	< d f >2_\markup { \dynamic pp \italic {poco cresc.} } < e-flat a >
	<< { g4 f g a-flat } \\ { d-flat, d e! f } >>
	<< { d-flat'2~ d-flat8 } \\ { g,2\mf~ g8 } >> r8 r4
	\tuplet 3/2 { r16^\markup {I. Solo.} f\f[( a-flat } \tuplet 3/2 { d-flat f a-flat] } d-flat8) r8 r2
	R1
	\tuplet 3/2 { r16 f,,[( a-flat } \tuplet 3/2 { d-flat f a-flat] } d-flat8) r8 r2
	
	R1*5
	
	r2 r4 \tuplet 3/2 { < e, c' >8\f[ < e c' > < e c' >] }
	r2 r4 \tuplet 3/2 { < e c' >8[ < e c' > < e c' >] }
	r8 < e c-sharp' > r4 r8 < d d' > r4
	r8 < e-flat c'! > r4 r8 < e-flat b-flat' > r4
	<< { a-flat2^\fp a } \\ { R1 } >>
	<< { g2 g } \\ { R1 } >>
	<< { f4 g a-flat~ a-flat8 } \\ { R1 } >>
	<< { f4 g a-flat~ a-flat8 } \\ { R1 } >>
	
	R1*2
	
	< g, e' >16\pp[ r < a e' > r < a f' > r < b f-sharp' >] r c16[ r < a e' > r < a f' > r < b f-sharp' >] r
	c[ r < g e' > r < f d' > r < f d' >] r < e c' >[ r < e c' >] r < f-sharp c' >4->
	< g e' >16\pp[ r < a e' > r < a f' > r < b f-sharp' >] r c16[ r < a e' > r < a f' > r < b f-sharp' >] r
	c[ r < g e' > r < f d' > r < f d' >] r < e c' >[ r < e c' >] r < f-sharp c' >4->
	< g d' >16\pp r r8 r4 r2
	R1
	<< { r8 b16[\< r c r c] r d[ r d r e r e] r } \\ { R1 } >>
	<< { f16[ r f r f r f]\! r a8 } \\ { r2 c,8\f } >> r8 r4
	<< { f16\mf[ r f r f r f] r a-flat8 } \\ { r2 c,8\f } >> r8 r4
	<< { c16\mf[ r d r c r d] r e-flat8 } \\ { c16[ s c s c s c] s c8\f } >> r8 r4
	< c e-flat >16\mf[ r < c f > r < c e-flat > r < c f >] r < c-flat g-flat' >8->\f r r4
	<< { g-flat'16\mf[ r a-flat r g-flat r a-flat] r a8 } \\ { c-flat,16[ s c-flat s c-flat s c-flat] s c8\f } >> r8 r4
	<< { g'!8\f } \\ { f8 } >> r8 r4 r2
	<< { a-flat8 } \\ { f8 } >> r8 r4 r2
	< f c' >8 r r4 r2
	< a c >8 r r4 r2
	r8 < a,, c >\mf~_\markup { \translate #(cons 4 -1) \italic cresc. } < a c >4 r8 < a c >8~ < a c >4
	r8 < a c >8~ < a c >4 r8 < a c >8~ < a c >4
	r8 < a c > r < a c > r < a c > r < a c >
	< c' d-sharp >8\f[\< < c d-sharp > < c d-sharp > < c d-sharp >] < c d-sharp >[ < c d-sharp > < c d-sharp > < c d-sharp >]\!
	< c e >8\ff[ \tuplet 3/2 { < c e >16 < c e > < c e >] } < c e >8[ < c e >] < c e >[ < c e > < c e > < c e >]
	< b d >8[ \tuplet 3/2 { < b d >16 < b d > < b d >] } < b d >8[ < a-sharp c-sharp >] < b d >[ < b d >] r < c-sharp! e >
	< d f >8[ \tuplet 3/2 { < d f >16 < d f > < d f >] } < d f >8[ < d f >] < d f >[ < d f > < d f > < d f >]
	< c-sharp e >[ \tuplet 3/2 { < c-sharp e >16 < c-sharp e > < c-sharp e >] } < c-sharp e >8[ < b-sharp d-sharp >]
		< c-sharp e >[ < c-sharp e >] r < c-sharp e >
	< c! f > r r4 < c g' >8 r r4
	< f, a >8 r r4 < e a >8 r r4
	< f a >8 r r4 < d a' >8 r < g-sharp b > r
	< f a > r r4 < d a' >8 r < g b > r
	< c e >8\ff[ \tuplet 3/2 { < c e >16 < c e > < c e >] } < c e >8[ < c e >] < c e >[ < c e > < c e > < c e >]
	< b d >8[ \tuplet 3/2 { < b d >16 < b d > < b d >] } < b d >8[ < a-sharp c-sharp >] < b d >[ < b d >] r < c-sharp! e >
	< d f >8[ \tuplet 3/2 { < d f >16 < d f > < d f >] } < d f >8[ < d f >] < d f >[ < d f > < d f > < d f >]
	< c-sharp e >[ \tuplet 3/2 { < c-sharp e >16 < c-sharp e > < c-sharp e >] } < c-sharp e >8[ < b-sharp d-sharp >]
		< c-sharp e >[ < c-sharp e >] r < c-sharp e >
	< c! f > r r4 < c g' >8 r r4
	< f, a >8 r r4 < e a >8 r r4
	<< { f-sharp8 r r d'!^>^\p( d-sharp) r r4 } \\ { d-sharp,8 r r4 r2 } >>
	r2 r4 << { e4 } \\ { e4\p\< } >>
	<< { f-sharp8 r r d'!^>^\p( d-sharp) r r4 } \\ { d-sharp,8\mf\! r r4 r2 } >>
	r2 r4 << { s4 } \\ { \stemUp < g, e' >\p\< } >>
	<< { e'8 r r f-sharp'^>( g) r r4 } \\ { c-sharp,,8\mf\! r r4 r2 } >>
	<< { r4 r8 f-sharp'^>( g) r r4 } \\ { R1 } >>
	<< { r4 r8 b^>( c) r r d-sharp,,( } \\ { r2 r4 r8 b~ } >>
	<< { e8) r r g'!^>( g-sharp) r r g-sharp,( } \\ { b,8 r r4 r r8 g-sharp'( } >>
	<< { a8) } \\ { a8) } >> r8 r < d, f-sharp >( < d g >) < g g' >4 < e' c' >8\f(
	< f! c' >) r8 << { r8 a-flat,^>^\p( a) r r4 } \\ { r4 r2 } >>
	r2 r4 << { b-flat'4 } \\ { b-flat4\p\< } >>
	<< { c8 r r a-flat,^>^\p( a) r r4 } \\ { a'8\mf\! r r4 r2 } >>
	r2 r4 << { b-flat4^>^\< } \\ { d-flat,4 } >>
	<< { b-flat'8^\mf^\! r r c,^>^\mf( d-flat)[ d-flat]~ d-flat r } \\ { g8 r r4 r8 d-flat,\mf~ d-flat r } >>
	<< { r4 r8 c'8^>( d-flat)[ d-flat]~ d-flat r } \\ { r2 r8 d-flat,~ d-flat r } >>
	<< { r4 r8 f^>( g-flat) r r a,( } \\ { r2 r4 r8 f~ } >>
	<< { b-flat8) r r d-flat^>( d) } \\ { f,8 s4 d-flat'8_>( d) } >> r8 r4
	r4 r8 << { c8( d-flat) r r b-flat'( } \\ { a-flat,8~_\cr a-flat s4 g-flat'8~ } >>
	<< { c-flat8) r r g-sharp( a!) } \\ { g-flat8 s4 e!8~ e } >> r r < d f-sharp >8(
	< d g >\ff) r < d g >2\mf < d g >8 r
	< f a-flat >8\f r < f a-flat >2\mf\> < f a-flat >8\! r
	
	R1*14
	
	<< { r2 r8 f-sharp8^\p[^( a d] } \\ { R1 } >>
	<< { g8^) r r4 r2 } \\ { R1 } >>
	<< { r2 r8 f-sharp,8[^( a d] } \\ { R1 } >>
	<< { g8^) r r4 r2 } \\ { R1 } >>
	<< { r2 r8 e,[^( g c] } \\ { R1 } >>
	<< { f8^) r r4 r2 } \\ { R1 } >>
	<< { r2 r8 e,[^( g c] } \\ { R1 } >>
	<< { f8^) r r4 r2 } \\ { R1 } >>
	r2 < f, d' >\p_\markup { \translate #(cons 4 -1) \italic cresc. }
	r < f d' > < f d' >\< < f d' >
	< g d' > < a-flat d >4\! < b a-flat' >
	< c a-flat' >8\ff[ \tuplet 3/2 { < a-flat, c >16 < a-flat c > < a-flat c >] } < a-flat c >8 < a-flat c > < a-flat c >
		< a-flat c > < a-flat c > < a-flat c >
	< g b-flat >8[ \tuplet 3/2 { < g b-flat >16 < g b-flat > < g b-flat >] } < g b-flat >8 < f-sharp a! > < g b-flat > < g b-flat > r < a! c >
	r8 \tuplet 3/2 { < b-flat d-flat >16[ < b-flat d-flat > < b-flat d-flat >] } < b-flat d-flat >8 < b-flat d-flat >
		< b-flat d-flat > < b-flat d-flat > < b-flat d-flat > < b-flat d-flat >
	< a c >8[ \tuplet 3/2 { < a c >16 < a c > < a c >] } < a c >8 < g-sharp b > < a c > < a c > r < a c >
	< a-flat d-flat >8 r r4 < a-flat e-flat' >8 r r4
	< b-flat d-flat >8 r r4 < c f >8 r r4
	< g-flat' d-flat' >8 r < a-flat d-flat >8 r < g-flat e-flat' > r < b-flat, b-flat' > r
	< e! c' >\ff r < e, g >4( < f a-flat > < f-sharp a >
	< g b-flat >8) r r4 r r8 << { b'8 } \\ { b8 } >>
	<< { c8 } \\ { c8 } >> r8 < e,, g >4( < f a-flat > < f-sharp a >
	< g b-flat >8) r r4 r r8 << { b'8 } \\ { b8 } >>
	<< { c8 } \\ { c8 } >> r8 < f,,! a-flat >4( < f-sharp a > < g b-flat >
	< g-sharp b >8) r8 r4 << { r8 b-flat'!8~ b-flat[ a-flat'] } \\ { r4 r8 d, } >>
	< e-flat g-flat >8 r  < f-sharp,, a >4( < g! b-flat! > < g-sharp b >
	< a c >8) r r < d-flat g >4 < d a-flat' > << { e-flat8 } \\ { e-flat8 } >>
	<< { e8 } \\ { e!8 } >> r8 < b-flat' c >4 < b d > < c e-flat >
	< d-flat e! > < d f > < e-flat f-sharp > < e g >
	< f a-flat >8\ff r < f, d' > r < f d' > r < f d' > r
	< f d' > r < f d' > r < f d' > r < f d' > r
	< g c > r r4 r2
	< f d' >8 r < f d' > r < f d' > r < f d' > r
	< g c > r r4 r2
	< f d' >8 r < f d' > r < f d' > r < f d' > r
	< g c > r r4 r2
	
	s1*46
	
	s1*11
	
	< c, a' >1\pp
	< c c' >2._\cr < c a' >4
	< b-flat b-flat' >1
	< a g' >2 < a f-sharp' >
	< g f'! > < g e' >
	< f e-flat' > < f d' >
	< b-flat e-flat > < b-flat e >
	< b-flat f' >8\mf r r4 r2
	
	R1*11
	
	< a-flat' f' >8\f[ < b-flat f' >16. < c f >32] < a-flat f' >8[ < b-flat f' >16. < c f >32] < a-flat g-flat' >8 r r4
	< a-flat f' >8[ < b-flat f' >16. < c f >32] < a-flat f' >8[ < b-flat f' >16. < c f >32] < a-flat g-flat' >8 r r4
	<< { f'8[ f16. f32] f8 } \\ { a-flat,8[_\cr b-flat16. c-flat32] b-flat8 } >> r8
		< b-flat b-flat' >8[ < c b-flat' >16. < d-flat b-flat' >32] < c b-flat' >8 r
	< c b-flat' >8[ < d-flat b-flat' >16. < e-flat b-flat' >32] < d-flat b-flat' >8 r
		<< { e8[ f16. g32] f8 } \\ { a-flat,8[ a-flat16. a-flat32] a-flat8 } >> r
	< f' a! >8\ff r < f a-flat > r << { g4^> } \\ { f8[( e]) } >> r4
	< f a! >8 r < f a-flat > r << { g4^> } \\ { f8[( e]) } >> r4
	
	R1*14
	<< { f-sharp,2(^\markup { \dynamic pp \italic cresc. } g } \\ { d1~ } >>
	<< { a'2 g-sharp) } \\ { d2 e } >>
	< f a >2._\cr < f-sharp a >4
	<< { \tuplet 3/2 { b-flat16[( b-flat, d-flat } \tuplet 3/2 { g-flat! b-flat d-flat] } g-flat8) r8 r4 r4 } \\
		{ g-flat,8\f r r4 r2 } >>
	R1
	<< { \tuplet 3/2 { r16 b-flat,\f[( d-flat } \tuplet 3/2 { g-flat b-flat d-flat] } g-flat8) r8 r4 r4 } \\ { R1 } >>
	R1
	<< { \tuplet 3/2 { r16\f a-flat,,[( c-flat } \tuplet 3/2 { g-flat' a-flat c-flat] } f!8) r r4 r4 } \\ { R1 } >>
	<< { \tuplet 3/2 { r16 g,,[( b-flat } \tuplet 3/2 { f' g b-flat] } e8) r8 r4 r4 } \\ { R1 } >>
	
	R1*2
	
	r2 r4 \tuplet 3/2 { < f a >8\f[ < f a > < f a >] }
	r2 r4 \tuplet 3/2 { < f a >8[ < f a > < f a >] }
	r8 < f-sharp a > r4 r8 < c g' > r4
	r8 < f! a-flat > r4 r8 < e-flat a-flat! > r4
	r8 < d-flat a-flat' >4->\pp < d-flat a-flat' >8 r8 < d g >4-> < d g >8
	r8 < c g' >4-> < c g' >8 r < c f >4-> < c f >8
	r8\< < b-flat f' >8 r < c f > r < d-flat f >~ < d-flat f >\! r
	r8\< < b-flat f' >8 r < c f > r < d-flat f >~ < d-flat f >\! r
	
	R1*2
	
	< f, c' >16\pp[ r < f-sharp d' > r < g d' > r < g-sharp e' >] r << { a16[ r d r d r e] r } \\ { a,16[ s f-sharp s g s g-sharp] s } >>
	<< { a16[ r a r g r g] } \\ { a16[ s c, s b-flat s b-flat] } >> r16 < a f' >[ r < d a' >] r < d b' >4^>
	< e c' >16[ r < f-sharp d' > r < g! d' > r < g-sharp e' >] r << { a16[ r d r d r e] r } \\ { a,16[ s f-sharp s g s g-sharp] s } >>
	<< { a16[ r a r g r g] } \\ { a16[ s c, s b-flat s b-flat] } >> r16 < a f' >[ r < d a' >] r < d b' >4^>
	< e c' >16 r r8 r4 r2
	
	R1*2
	
	r2 < f d' >8\f r r4
	r2 < f d-flat' >8\f r r4
	r2 < a-flat f' >8 r r4
	r2 < b e! >8\f r r4
	r2 < b b' >8\f r r4
	< b-flat! b-flat'! >8\f r r4 < b-flat b-flat' >8 r r4
	< b-flat b-flat' >8 r r4 < b-flat b-flat' >8 r r4
	< g' b-flat >8 < g b-flat > r < g b-flat >[ < g b-flat > < g b-flat >] r < g b-flat >
	< f d' >[ < f d' >] r < f d' >[ < f d' > < f d' >] r < f d' >
	r8 < b-flat, f' >\mf~ < b-flat f' >4_\cr r8 < b-flat f' >8~ < b-flat f' >4
	r8 < b-flat f' >8~ < b-flat f' >4 r8 < b-flat f' >8~ < b-flat f' >4
	r8 < b-flat f' > r < b-flat f' > r < b-flat f' > r < b-flat f' >
	< b-flat f' >2:8 < b-flat f' >2:
	< c a' >8\f r r4 r2
	
	R1*2
	
	r4 < d-flat a-flat' >2\f r4
	r < c g' >2 r4
	r < b-flat f' >2 r4
	r4 < e-flat, a-flat >8[ < d f-sharp >] < d g > r < d g >[ < c e-flat >]
	< c f! > r r4 r2
	< c f >8 r r4 r2
	< c-flat f >8 r r4 r2
	< d-flat g-flat >8\f r < c f > r < d-flat g-flat > r < c f > r
	< d-flat g-flat >1
	< f a-flat' >1
	< f a'! >8\ff r r4 r2
	
	R1*3
	
	r8 < c' e >\f[ < d-flat f > < c e >] < d-flat f >[ < c e >\ff < c e > < c e >]
	< d-flat f >[ < c e >\f < d-flat f > < c e >] < d-flat f >[ < c e >\ff < c e > < c e >]
	< d-flat f >[ < c e >\f < d-flat f > < c e >\ff] < d-flat f >[ < c e >\f < d-flat f > < c e >\ff]
	< d-flat f >[ < c e > < d-flat f > < d-flat g >] < d g-sharp >[ < b-flat d > < b-flat d > < d g-sharp >]
	< c a' >\ff < f, f' >4 < f f' >8~ < f f' >[ < g g' > < a a' > < b-flat b-flat' >]
	< c c' > < f, f' >4 < f f' >8~ < f f' >[ < g g' > < a a' > < b-flat b-flat' >]
	< c c' > << { f4 g8 f e4 f8 } \\ { g-sharp,,8[ a b-flat] b[ c c-sharp d] } >>
	<< { e'8 d4 b-flat8 d-flat8^> r r c } \\ { e,8[ f f-sharp g] g-flat_> s s b-flat } >>
	<< { c8 } \\ { a8 } >> < f f' >4 < f f' >8~ < f f' >[ < g g' > < a a' > < b-flat b-flat' >]
	< c c' > < f, f' >4 < f f' >8~ < f f' >[ < g g' > < a a' > < b-flat b-flat' >]
	< c c' > << { f4 g8 f e4 f8 } \\ { g-sharp,,8[ a b-flat] b[ c c-sharp d] } >>
	<< { e'8 d4 b-flat8 d-flat8^> r r c } \\ { e,8[ f f-sharp g] g-flat_> s s b-flat } >>
	< a c >8 r < a f' > r < c a' > r < c a' > r
	< c a' > r < a f' > r < c a' > r < c a' > r
	< c a' > r < d a' > r < c a' > r < d a' > r
	< c a' > r < d a' > r < c a' > r < d a' > r
	< a a' >[ < a, f' > < f' a > < f c' >] < a f' >[ < a f' > < c f > < c f >]
	< c f >4 < c f > < c f > < c f >
	< a, c >1\fermata
}
