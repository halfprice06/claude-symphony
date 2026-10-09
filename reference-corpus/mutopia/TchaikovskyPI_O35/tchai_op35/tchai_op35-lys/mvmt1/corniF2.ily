\version "2.20.0"

theHornssecond =  \relative c' {
	\transposition f'
	\clef "treble"
	\key c \major
	
	\override Staff.TupletBracket.bracket-visibility = ##f
	
	r1
	
	R1*12
	
	< d b' >1\mf\<
	< c a' >\!
	< c a' >\f
	< c a' >
	<< { a'4^\ff } \\ { c,4 } >> r4 << { a'4 } \\ { c,4 } >> r4
	< c a' >8[ < c a' > < c a' > < c a' >] < c a' >2:8
	< b e >8 r r4 r2
	R1
	r8 << { g'8[( c]) } \\ { c,8\p[( c]) } >> r8 r << { g'8[( c]) } \\ { c,8\p[( c]) } >> r
	
	R1*36
	
	< c c' >8\f[ < c c' >16. < c c' >32] < c c' >8[ < c c' >16. < c c' >32] < d d' >8 r r4
	< c c' >8[ < c c' >16. < c c' >32] < c c' >8[ < c c' >16. < c c' >32] < d d' >8 r r4
	< c c' >8[ < c c' >16. < c c' >32] < c-sharp c-sharp' >8 r < d a' >8[ < d b' >16. < d c'! >32] < d-sharp b' >8 r
	< e b' >8[ < e c'! >16. < e d' >32] < f-sharp c' >8 r < c-sharp a-sharp' >8[ < c-sharp a-sharp' >16.
		< c-sharp a-sharp' >32] < c a-sharp' >8 r
	< g-sharp' e' >8\ff r < g e' > r << { e'8[(^> d-sharp]) } \\ { f-sharp,4_> } >> r4
	< g-sharp e' >8 r < g e' > r << { e'8[(^> d-sharp]) } \\ { f-sharp,4_> } >> r4
	
	R1*24
	
	<< { a4\mf g-sharp~ g-sharp8[ g-sharp] a[ a] } \\ { R1 } >>
	<< { b-flat8[ g!] a[ f] g r r4 } \\ { R1 } >>
	<< { a4\mf g-sharp~ g-sharp8[ g-sharp] a[ a] } \\ { R1 } >>
	<< { b-flat8[ g!] a[ f] g[ g] f[ f] } \\ { R1 } >>
	r2 r8 < c a' >8\mf[ < c a' > < c a' >]
	r2 r8 < b g-sharp' >[ < b g-sharp' > < b g-sharp' >]
	r8 g'!8 g4 g-sharp8 r r4
	
	R1*7
	
	<< { r8 e\p r g r a4 r8 } \\ { r4 s8 b,8\p s a4 s8 } >>
	<< { r8 e' r g r a4 r8 } \\ { r4 s8 b,8 s a4 s8 } >>
	
	R1*9
	
	r2 < c-sharp a' >8\f r r4
	r2 < c! a' >8\f r r4
	r2 < g' e' >8\f r r4
	r2 < g e-flat' >8->\f r r4
	r2 < e! e'! >8\f r r4
	< f b >8\f r r4 r2
	< e c'! >8 r r4 r2
	< e e' >8 r r4 r2
	< e e' >8 r r4 r2
	
	R1*3
	
	< c-sharp g' >8[\< < c-sharp g' > < c-sharp g' > < c-sharp g' >] < c-sharp g' >[ < c-sharp g' >
		< c-sharp g' > < c-sharp g' >]\!
	< b g-sharp' >\ff[ \tuplet 3/2 { < b g-sharp' >16 < b g-sharp' > < b g-sharp' >] } < b g-sharp' >8[ < b g-sharp' >]
		< b g-sharp' >[ < b g-sharp' >] < b g-sharp' >[ < b g-sharp' >]
	< b f-sharp' >[ \tuplet 3/2 { < b f-sharp' >16 < b f-sharp' > < b f-sharp' >] } < b f-sharp' >8[ < b e-sharp >]
		< b f-sharp' >[ < b f-sharp' >]  r < c-sharp g-sharp' >
	< c-sharp a' >[ \tuplet 3/2 { < c-sharp a' >16 < c-sharp a' > < c-sharp a' >] } < c-sharp a' >8[ < c-sharp a' >]
		< c-sharp a' >[ < c-sharp a' >] < c-sharp a' >[ < c-sharp a' >]
	< c-sharp g-sharp' >[ \tuplet 3/2 { < c-sharp g-sharp' >16 < c-sharp g-sharp' > < c-sharp g-sharp' >] } < c-sharp g-sharp' >8[
		< c-sharp g' >] < c-sharp g-sharp' >[ < c-sharp g-sharp' >] r < c-sharp g-sharp' >
	< c-sharp a' > r r4 < b e' >8 r r4
	< c-sharp f-sharp >8 r r4 < c-sharp g-sharp' >8 r r4
	< c-sharp a' >8 r r4 < a f-sharp' >8 r < d-sharp c'! > r
	< c-sharp a' > r r4 < a f-sharp' >8 r < d-sharp d-sharp' > r
	< b g-sharp' >\ff[ \tuplet 3/2 { < b g-sharp' >16 < b g-sharp' > < b g-sharp' >] } < b g-sharp' >8[ < b g-sharp' >]
		< b g-sharp' >[ < b g-sharp' >] < b g-sharp' >[ < b g-sharp' >]
	< b f-sharp' >[ \tuplet 3/2 { < b f-sharp' >16 < b f-sharp' > < b f-sharp' >] } < b f-sharp' >8[ < b e-sharp >]
		< b f-sharp' >[ < b f-sharp' >]  r < c-sharp g-sharp' >
	< c-sharp a' >[ \tuplet 3/2 { < c-sharp a' >16 < c-sharp a' > < c-sharp a' >] } < c-sharp a' >8[ < c-sharp a' >]
		< c-sharp a' >[ < c-sharp a' >] < c-sharp a' >[ < c-sharp a' >]
	< c-sharp g-sharp' >[ \tuplet 3/2 { < c-sharp g-sharp' >16 < c-sharp g-sharp' > < c-sharp g-sharp' >] } < c-sharp g-sharp' >8[
		< c-sharp g' >] < c-sharp g-sharp' >[ < c-sharp g-sharp' >] r < c-sharp g-sharp' >
	< c-sharp a' > r r4 < b e' >8 r r4
	< c-sharp f-sharp >8 r r4 < c-sharp g-sharp' >8 r r4
	< d-sharp a-sharp' >8 r r4 r8 < c-sharp c-sharp' >8\p~ < c-sharp c-sharp' >[ < b b' >]~
	< b b' > r r4 r2
	r2 r8 < c-sharp c-sharp' >8\p~ < c-sharp c-sharp' >[ < b b' >]~
	< b b' > r r4 r2
	<< { r2 r8 b'^>\mf[~ b] r8 } \\ { R1 } >>
	<< { r2 r8 b^>[~ b] r8 } \\ { R1 } >>
	r4 r8 << { a-sharp8~ a-sharp } \\ { c-sharp,8\mf~ c-sharp } >> r8 r4
	r4 r8 << { g-sharp'8~ g-sharp } \\ { d-sharp8~ d-sharp } >> r8 r4
	<< { r2 r4 r8 e\mf~ } \\ { R1 } >>
	<< { e8 r r4 r2 } \\ { R1 } >>
	
	R1*5
	
	r4 r8 << { e8~ e } \\ { g,8\mf~ g } >> r r4
	r r8 < a d >8~ < a d > r r4
	R1
	r8 < e-flat' e-flat' >~ < e-flat e-flat' > r r < c-sharp c-sharp' >~ < c-sharp c-sharp' > r
	
	R1*27
	
	r2 r4 < c f-sharp >
	<< { g'8[ \tuplet 3/2 { c16 c c] } } \\ { c,8\ff[ \tuplet 3/2 { c16 c c] } } >>
		< c c' >8[ < c c' >] < c c' >[ < c c' >] < c c' >[ < c c' >]
	< b b' >[ \tuplet 3/2 { < b b' >16 < b b' > < b b' >] } < b b' >8[ < a-sharp a-sharp' >]
		< b b' >[ < b b' >] r < c-sharp c-sharp' >
	r8 \tuplet 3/2 { < d d' >16[ < d d' > < d d' >] } < d d' >8[ < d d' >] < d d' >[ < d d' >] < d d' >[ < d d' >]
	< c-sharp c-sharp' >[ \tuplet 3/2 { < c-sharp c-sharp' >16 < c-sharp c-sharp' > < c-sharp c-sharp' >] } < c-sharp c-sharp' >8[
		< b-sharp b-sharp' >] < c-sharp c-sharp' >[ < c-sharp c-sharp' >] r < c-sharp c-sharp' >
	< c! c' > r r4 < c c' >8 r r4
	< d d' >8 r r4 << { a'8 } \\ { a8 } >> r r4
	< f b-flat >8 r < f f' > r < d g > r < d a' > r
	< b g-sharp' >\ff r r4 r2
	r2 r4 r8 << { b'8 } \\ { a8 } >>
	<< { b8 } \\ { g-sharp8 } >> r8 r4 r2
	r2 r4 r8 << { b8 } \\ { a8 } >>
	<< { b8 } \\ { g-sharp8 } >> r8 r4 r2
	r2 r4 r8 << { c!8 } \\ { c8 } >>
	<< { c-sharp8 } \\ { a-sharp8 } >> r8 r4 r2
	r2 r4 r8 << { c-sharp8 } \\ { c-sharp8 } >>
	<< { d!8 } \\ { b!8 } >> r8 << { e,4 f-sharp g } \\ { d4 d-sharp e } >>
	<< { g-sharp4 a b-flat b } \\ { f!4 f-sharp g g-sharp } >>
	< a c >8\ff r < a c > r < a c > r < a c > r
	< a c > r < a c > r < a c > r < a c > r
	< e b' > r r4 r2
	< a c >8 r < a c > r < a c > r < a c > r
	< e b' > r r4 r2
	< a c >8 r < a c > r < a c > r < a c > r
	< e b' > r r4 r2
	
	s1*46
	
	s1*33
	
	r2 < c f-sharp >8\f[ < c f-sharp >16. < c f-sharp >32] < c f >8 r
	< e c-sharp' >8\ff r < e c' > r < e b' >4-> r
	< e c-sharp' >8 r < e c' > r < e b' >4-> r
	
	R1*17
	
	r2 r8 < b-flat g' >8\p < b-flat f' >[ < b g' >]
	< c g' >[ < a f' >] < b-flat f' >[ < g e-flat' >] < a f' > r r4
	r2 r8 < b-flat g' >8 < b-flat f' >[ < b g' >]
	< c g' >[ < a f' >] < b-flat f' >[ < g e-flat' >] < a f' > r r4
	
	R1*25
	
	r2 < f-sharp' f-sharp' >8\f r r4
	<< { d'8 } \\ { d8\f } >> r8 r4 << { d8 } \\ { d8 } >> r8 r4
	< d, d' >8 r r4 < d d' >8 r r4
	< d d' >8[ < d d' >] r < d d' >[ < d d' > < d d' >] r < d d' >
	< f-sharp f-sharp' >[ < f-sharp f-sharp' >] r < f-sharp f-sharp' >[ < f-sharp f-sharp' > < f-sharp f-sharp' >] r < f-sharp f-sharp' >
	
	R1*4
	
	%%% CODA %%%
	
	< e c-sharp' >8\f r r4 r2
	
	R1*11
	
	<< { c'1\f } \\ { R1 } >>
	< e, c-sharp' >8\ff r r4 r2
	r4 < a, a' >4^>\mf~\< < a a' >8\! r r4
	
	R1*2
	
	<< { r2 r8 g-sharp'8[ g-sharp g-sharp] } \\ { r8 d8[ d d] d[ e\ff e e] } >>
	<< { a8 r r4 r8 g-sharp[ g-sharp g-sharp] } \\ { r8 d[ d d] d[ e\ff e e] } >>
	<< { e8 r r g-sharp a r r g-sharp } \\ { f-sharp8[ d\f d e\ff] f-sharp\f[ d d e\ff] } >>
	<< { a8 r r f-sharp } \\ { f-sharp8[ d d d] } >> < d f-sharp >8[ < d f-sharp > < d f-sharp > < d f-sharp >]
	< c-sharp e >\ff r r4 < a a' >4 < a a' >8 < a a' >
	< a a' > r r4 < a a' >4 < a a' >8 < a a' >
	< a a' > r r4 r2
	r2 < d d' >8^> r r << { e8 } \\ { e8 } >>
	<< { e8 } \\ { e8 } >> r r4 < a, a' >4 < a a' >8 < a a' >
	< a a' > r r4 < a a' >4 < a a' >8 < a a' >
	< a a' > r r4 r2
	r2 < d d' >8^> r r << { e8 } \\ { e8 } >>
	<< { e8 } \\ { e8 } >> r < a c-sharp > r < e c-sharp' > r < e c-sharp' > r
	< e c-sharp' >8 r < a c-sharp > r < e c-sharp' > r < e c-sharp' > r
	< e c-sharp' > r < f-sharp c-sharp' > r < e c-sharp' > r < f-sharp c-sharp' > r
	< e c-sharp' > r < f-sharp c-sharp' > r < e c-sharp' > r < f-sharp c-sharp' > r
	< e c-sharp' >8[ < c-sharp e > < c-sharp e > < c-sharp e >] < c-sharp e >[ < c-sharp e > < c-sharp e > < c-sharp e >]
	< c-sharp e >4 < c-sharp e > < c-sharp e > < e a >
	< c-sharp e >1\fermata
}
