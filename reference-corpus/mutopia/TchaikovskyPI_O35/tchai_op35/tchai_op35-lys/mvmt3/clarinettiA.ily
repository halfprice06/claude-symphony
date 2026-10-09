\version "2.20.0"

theClarinets =  \relative a' {
	\transposition a
	
	\clef "treble"
	\key f \major
	
	< c c' >8\ff r r4
	
	R1*2/4*2
	
	r4 < e,, g >8 r
	R1*2/4
	r4 < b'' g' >4~
	< b g' > < b g' >
	< c g' >8 r r4
	R1*2/4
	b'8-.\f[ b16( a-sharp] b8)[ b,-.]
	c4~ c8 r
	
	R1*2/4*2
	
	< a, f' >2\ff
	< b-flat! g' >4 < b a-flat' >
	< c a'! > < g' c >8 r
	
	R1*2/4*40
	
	< d a' >16\f r r8 r4
	
	R1*2/4*9
	
	< g e' >8\p r < a e-flat' > r
	< b f' > r < c g' > r
	
	R1*2/4*21
	
	<< { g'8\f[ g16( f-sharp] g[ e c g] } \\ { R1*2/4 } >>
	<< { f8) r r4 } \\ { R1*2/4 } >>
	<< { g'8[ g16( f-sharp] g[ e c g] } \\ { R1*2/4 } >>
	<< { f8) r r4 } \\ { R1*2/4 } >>
	
	R1*2/4*7
	
	< c' f >2:8\p
	< c g' >2:
	< c g' >2:
	< c g' >8[\< < c g' >] < c f >[ < c f >]\!
	< d a' >16\f r r8 r4
	
	R1*2/4*20
	
	<< { a-flat'8^\f[ a-flat16^( g] a-flat8-.)[ f,-.] } \\ { R1*2/4 } >>
	R1*2/4
	<< { a-flat'8[ a-flat16^( g] a-flat8-.)[ f,-.] } \\ { R1*2/4 } >>
	
	R1*2/4*16
	
%	\key c \major
	
	< c' g' >8 r r4
	
	R1*2/4*18
	
	r4 r8 < c, e >8\p
	r < d f > r < g b >
	r < b f' > r < d f >
	r < e g > r << c8 \\ c8 >>
	r8 << c8 \\ c8 >> r < e, g >8
	r < d f > r < g b >
	r < b f' > r < d f >
	r << e8 \\ e8 >> r << c'8 \\ c8 >>
	r8 << g8 \\ g8 >> r4
	
	R1*2/4*18
	
	r4 < g, g' >4\mf~
	< g g' >2
	
	R1*2/4*5
	
	<< { r4 e'8-.[(_\markup { \dynamic p \italic espress. }
		^\markup { \smaller {1\super{mo} Solo.}} d-.]) } \\ { R1*2/4 } >>
	<< { f4 \grace { e16[( f] } e8[ d]) } \\ { R1*2/4 } >>
	<< { \grace { c16[ d] } c8[( b] a) r } \\ { R1*2/4 } >>
	R1*2/4
	<< { r4 e'8-.[( d-.]) } \\ { R1*2/4 } >>
	<< { f4 \grace { e16[( f] } e8[ d]) } \\ { R1*2/4 } >>
	<< { \grace { c16[ d] } c8[( b] a) r } \\ { R1*2/4 } >>
	
	R1*2/4*38
%	\key f \major
	R1*2/4*4
	
	< d, a' >16\f r r8 r4
	
	R1*2/4*9
	
	< g e' >8\p r < a e-flat' >\< r
	< b f' > r < c g' >\! r
	
	R1*2/4*21
	
	<< { g'8\f[ g16( f-sharp] g[ e c g] } \\ { R1*2/4 } >>
	<< { f8) r r4 } \\ { R1*2/4 } >>
	<< { g'8[ g16( f-sharp] g[ e c g] } \\ { R1*2/4 } >>
	<< { f8) r r4 } \\ { R1*2/4 } >>
	
	R1*2/4*11
	
	< a-flat e-flat' >4\p < a-flat e-flat' >8[ < a-flat e-flat' >]
	< a-flat e-flat' >4 r
	
	R1*2/4*2
	
	< a-flat e-flat' >4\p < a-flat e-flat' >8[ < a-flat e-flat' >]
	< a-flat e-flat' >4 r
	
	R1*2/4*2
	
	< f c' >4 < f c' >8[ < f c' >]
	< f c' >4 r
	
	R1*2/4*2
	
	< f c' >4 < f c' >8[ < f c' >]
	< f c' >4 r
	
	R1*2/4*4
	
	<< { d-flat'8[ d-flat16( c] d-flat8)[ d-flat] } \\ { a-flat8\ff r a-flat[ a-flat] } >>
	<< { e-flat'8[ a-flat] b-flatflat } \\ { c,8[ e-flat!] f-flat } >> r8
	
	R1*2/4*2
	
	<< { d-flat8[ d-flat16( c] d-flat8)[ d-flat] } \\ { a-flat8 r a-flat[ a-flat] } >>
	< c e-flat >8[ < c e-flat >] < d-flat f > r
	
	R1*2/4*2
	
	<< { g-flat8 r g-flat[ g-flat] } \\ { d-flat8[ d-flat16( c] d-flat8)[ d-flat] } >>
	< c g-flat' >[ < c g-flat' >] < d-flat g > r
	
	R1*2/4*2
	
	< e-flat b-flat' >8 r < e-flat b-flat' >[ < e-flat b-flat' >]
	< d b-flat' >[ < d b-flat' >] < e-flat b-flat' > r
	
	r4 r8 < e-flat b-flat' >
	< d b-flat' >[ < d b-flat' >] < e-flat b-flat' > r
	r4 r8 < e-flat b-flat' >
	< d b-flat' >[ < d b-flat' > < e-flat b-flat' > < e-flat b-flat' >]
	< d b-flat' >[ < d b-flat' > < e-flat b-flat' > < e-flat b-flat' >]
	< d b-flat' >[ < d b-flat' > < e-flat b-flat' > < e-flat b-flat' >]
	< e-flat c' > r r4
	
	R1*2/4*15
	
%	\key b-flat \major
	
	< d b-flat' >8\ff r r4
	
	R1*2/4*43
	
	<< { f,4\pp( g } \\ { R1*2/4 } >>
	<< { a-flat4 a) } \\ { R1*2/4 } >>
	<< { b-flat4( d } \\ { R1*2/4 } >>
	<< { f8) r r4 } \\ { R1*2/4 } >>
	<< { f,4( g } \\ { R1*2/4 } >>
	<< { a-flat4 a) } \\ { R1*2/4 } >>
	<< { b-flat4( d } \\ { R1*2/4 } >>
	<< { f8) r r4 } \\ { R1*2/4 } >>
	
	%%% MOLTO MENO MOSSO %%%
	
	R1*2/4
	<< { r4 g,8-.^\p[( a-.]) } \\ { R1*2/4 } >>
	<< { \grace { g16[ a] } b-flat4 a8[ g] } \\ { R1*2/4 } >>
	<< { \grace { f16[^( g] } f8[ e-flat]^) } \\ { R1*2/4 } >>
	R1*2/4
	<< { r4 g8-.[( a-.]) } \\ { R1*2/4 } >>
	<< { \grace { g16[ a] } b-flat4 a8[ g] } \\ { R1*2/4 } >>
	<< { \grace { f16[^( g] } f8[ e]^) } \\ { R1*2/4 } >>
	
	R1*2/4*27
	
	<< { r8 g,\p[^(\< b-flat d-flat] } \\ { d,1*2/4\rest } >>
	<< { e'8[ g]^)\! c4~ } \\ { c,1*2/4\rest } >>
	<< { c'8[ f,,^(\< a-flat c] } \\ { d,1*2/4\rest } >>
	<< { f'8[ a-flat]^)\! d4^>( } \\ { R1*2/4 } >>
	<< { c8) r r4 } \\ { R1*2/4 } >>
	r4 << { g4^>( } \\ { e4_>\p( } >>
	<< f8) \\ c8) >> r8 r4
	r4 << { b4^>( } \\ { a-flat_>( } >>
	<< c8) \\ g8) >> r8 r4
	r4 < f b >\pp(
	< e c' >) r
	r4 < f b >(
	< e-flat c' >) r
	
	R1*2/4*11
%	\key f \major
	R1*2/4*4
	
	< d' a' >16\f r r8 r4
	
	R1*2/4*9
	
	< g e' >8\p r < a e-flat' > r
	< b f' > r < c g' > r
	
	R1*2/4*21
	
	<< { g'8\f[ g16( f-sharp] g[ e c g] } \\ { R1*2/4 } >>
	<< { f8) r r4 } \\ { R1*2/4 } >>
	<< { g'8[ g16( f-sharp] g[ e c g] } \\ { R1*2/4 } >>
	<< { f8) r r4 } \\ { R1*2/4 } >>
	
	R1*2/4*7
	
	< c' f >2:8\p
	< c g' >2:
	< c g' >2:
	< c g' >8[\< < c g' >] < c f >[ < c f >]\!
	< d a' >16\f r r8 r4
	
	R1*2/4*20
	
	<< { a-flat'8^\f[ a-flat16^( g] a-flat8-.)[ f,-.] } \\ { R1*2/4 } >>
	R1*2/4
	<< { a-flat'8[ a-flat16^( g] a-flat8-.)[ f,-.] } \\ { R1*2/4 } >>
	
	R1*2/4*4
	
	< c' a' >8\f r r4
	
	R1*2/4*2
	
	r4 << { f-sharp16[( g a d,]) } \\ { f-sharp\p[( g a d,]) } >>
	
	R1*2/4*3
	
	r4 << { g-sharp16[( a b e,]) } \\ { g-sharp16\mf[( a b e,]) } >>
	r4 << { c8[^\cr c] } \\ { c8[ c] } >>
	<< { c4 b8[( a]) } \\ { c4 b8[( a]) } >>
	r4 << { d8[ d] } \\ { d8[ d] } >>
	<< { d4 c8[( b]) } \\ { d4 c8[( b]) } >>
	r4 << { e8[ e] } \\ { e8[ e] } >>
	<< { e4 d8[( d-flat]) } \\ { e4 d8[( d-flat]) } >>
	r4 << { f8[ f] } \\ { f8[ f] } >>
	<< { f4 e8[( d!]) } \\ { f4 e8[( d]) } >>
	r8 < g, g' >16\f[ < g g' >] < g g' >8[ < f f' >16( < e e' >])
	r8 < g g' >16[ < g g' >] < g g' >8[ < f f' >16( < e e' >])
	r8 < b-flat' b-flat' >16[ < b-flat b-flat' >] < b-flat b-flat' >8[ < a a' >16( < g g' >])
	r8 < b-flat b-flat' >16[ < b-flat b-flat' >] < b-flat b-flat' >8[ < a a' >16( < g g' >])
	r8 < e c' > r < e c' >
	r < e c' > r < e c' >
	r < e c' > r < e c' >
	r < e c' >[ < e c' > < e c' >]
	<< { f'8[ f16( e] f8)[ f] } \\ { c8\ff r c[ c] } >>
	< d f >8[ < d f >] < c f > r
	
	R1*2/4*2
	
	<< { f8-.[ f16( e] f8)[ d] } \\ { d8 r d[ a] } >>
	<< { e'8[ g] f } \\ { d8[ d] d } >> r8
	
	R1*2/4*2
	
	<< { f8[ f16( e] f8)[ f] } \\ { d8 r d[ d] } >>
	<< { b-flat'8[ b-flat] f } \\ { e-flat8[ e-flat] d } >> r8
	
	R1*2/4*2
	
	<< { g8-.[ g16( f-sharp] g8)[ g] } \\ { d8 r d[ d] } >>
	<< { g8[ g] g } \\ { e-flat8[ e-flat] d } >> r8
	
	R1*2/4*2
	
	<< { g8-.[ g16( f-sharp] g8)[ g] } \\ { d8 r d[ d] } >>
	<< { g8[ g] g } \\ { e-flat8[ e-flat] d } >> r8
	
	R1*2/4*2
	
	<< { g8[ g16( f-sharp] g8)[ g] } \\ { d8 r d[ d] } >>
	R1*2/4
	<< { g8[ g16( f-sharp] g8)[ g] } \\ { d8 r d[ d] } >>
	R1*2/4
	< d g >8[ < d g >] r4
	< d g >8[ < d g >] r4
	< d-flat g >8[ < g b-flat >] r4
	< c, g' >8[ < g' b-flat >] r4
	< a c >8[ < a c >] r4
	< f b-flat >8[ < f b-flat >] r4
	< f b >8[ < f b >] r4
	
	R1*2/4*3
	
	r8 < a, e' >\f[ < a f' > < a c-sharp >]
	< a d >[ < a d > < g d' > < d f-sharp >]
	< d g >[ < d g > < e g > < f g >]
	< e g >[ < e c-sharp' > < f d' > < c'! c'! >]
	< c! c'! > r r4
	
	R1*2/4*3
	
	< c f >8\f r r4
	
	R1*2/4*3
	
	< c f >8 r r4
	
	R1*2/4*3
	
	< c f >8 r r4
	
	R1*2/4*3
	
	< c f >8\f r < c e > r
	< c f > r < c e > r
	< c f > r < c e > r
	< c f > r < c e > r
	< c f > r < f a >[ < f a >]
	< f a >4 < f a >8[ < f b-flat >]
	< f c' > r < f a >[ < f a >]
	< f a >4 < f a >8[ < f b-flat >]
	< f c' >[ < f a > < f a > < f b-flat >]
	< f c' >[ < f a > < f a > < f b-flat >]
	< f c' > r r4
	< c f >8 r r4
	< f b >8 r r4
	< b-flat! c >8 r r4
	< a c >8\ff[ < g c > < a c > < g c >]
	< a c >8[ < g c > < a c > < g c >]
	< a c >8[ < g c > < a c > < g c >]
	< a c >8[ < g c > < a c > < g c >]
	<< { f8[ f16( e] f8)[ f] } \\ { c8 r c[ c] } >>
	< e g >8[ < e g >] < f, f' >[ < a a' >]
	< c c' > r r < c c' >
	< a' c > r r4\fermata

}
