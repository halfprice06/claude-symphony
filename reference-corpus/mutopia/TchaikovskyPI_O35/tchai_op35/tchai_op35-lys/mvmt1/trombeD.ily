\version "2.20.0"

theTrumpets =  \relative d' {
	\clef "treble"
	\time 4/4
	\key c \major
	
	\transposition d'
	
	r1
	
	R1*12
	
	<< { g4\mf } \\ { g4 } >> r4 r2
	< c e-flat, >4 r4 r2
	< a c >4\f r r2
	< a c >4 r r2
	< a c >4\ff r < a c > r
	< a c >8[ < a c > < a c > < a c >] < a c >2:8
	< g b >8 r r4 r2
	
	R1*42
	
	< d d' >8\ff r < d d' >8 r < d d' >4-> r4
	< d d' >8 r < d d' >8 r < d d' >4-> r4
	
	R1*54
	
	< c c' >8\f r r4 r2
	< c c' >8 r r4 r2
	< c c' >8 r r4 r2
	< e e' >8 r r4 r2
	
	R1*4
	
	< g b >8\ff[ \tuplet 3/2 { < d d' >16 < d d' > < d d' >] } < d d' >8[ < d d' >]
		< d d' >[ < d d' > < d d' > < d d' >]
	< d d' >[ \tuplet 3/2 { < d d' >16 < d d' > < d d' >] } < d d' >8[ < d d' >]
		< d d' >[ < d d' >] r < e e' >
	< e e' >[ \tuplet 3/2 { < e e' >16 < e e' > < e e' >] } < e e' >8[ < e e' >]
		< e e' >[ < e e' >] < e e' >[ < e e' >]
	< e e' >[ \tuplet 3/2 { < e e' >16 < e e' > < e e' >] } < e e' >8[ < e e' >]
		< e e' >[ < e e' >] r < e e' >
	< e e' > r r4 < d d' >8 r r4
	< e c' >8 r r4 < e b' >8 r r4
	< a e' >8 r r4 < a e' >8 r < b d-sharp > r
	< a e' > r r4 < a e' >8 r < d, d' > r
	< g b >8\ff[ \tuplet 3/2 { < d d' >16 < d d' > < d d' >] } < d d' >8[ < d d' >]
		< d d' >[ < d d' > < d d' > < d d' >]
	< d d' >[ \tuplet 3/2 { < d d' >16 < d d' > < d d' >] } < d d' >8[ < d d' >]
		< d d' >[ < d d' >] r < e e' >
	< e e' >[ \tuplet 3/2 { < e e' >16 < e e' > < e e' >] } < e e' >8[ < e e' >]
		< e e' >[ < e e' >] < e e' >[ < e e' >]
	< e e' >[ \tuplet 3/2 { < e e' >16 < e e' > < e e' >] } < e e' >8[ < e e' >]
		< e e' >[ < e e' >] r < e e' >
	< e e' > r r4 < d d' >8 r r4
	< e c' >8 r r4 < e b' >8 r r4
	< f-sharp a-sharp >8 r r4 r2
	
	R1*8
	
	r2 r8 << { c'4 c8~ } \\ { b-flat4\p a-flat8~ } >>
	<< { c8 } \\ { a-flat8 } >> r8 r4 r2
	r2 r8 << { c4 c8~ } \\ { b-flat4\p a-flat8~ } >>
	<< { c8 } \\ { a-flat8 } >> r8 r4 r2
	
	R1*34
	
	< b-flat, b-flat' >8\ff[ \tuplet 3/2 { < b-flat b-flat' >16 < b-flat b-flat' > < b-flat b-flat' >] }
		< b-flat b-flat' >8 < b-flat b-flat' > < b-flat b-flat' > < b-flat b-flat' >
		< b-flat b-flat' > < b-flat b-flat' >
	< b-flat b-flat' >8[ \tuplet 3/2 { < b-flat b-flat' >16 < b-flat b-flat' > < b-flat b-flat' >] }
		< b-flat b-flat' >8 < b-flat b-flat' > < b-flat b-flat' > < b-flat b-flat' > r < c c' >
	< c c' >8[ \tuplet 3/2 { < c c' >16 < c c' > < c c' >] } < c c' >8 < c c' >
		< c c' > < c c' > < c c' > < c c' >
	< c c' >8[ \tuplet 3/2 { < c c' >16 < c c' > < c c' >] } < c c' >8
		< c c' > < c c' > < c c' > r < c c' >
	< c c' > r r4 < b-flat b-flat' >8 r r4
	< c c' >8 r r4 < g' c >8 r r4
	< f d-flat' >8 r < e-flat e-flat' > r < f d-flat' > r < f c' > r
	< g b >\ff r r4 r2
	r2 r4 r8 << { d'8 } \\ { c8 } >>
	<< { d8 } \\ { b8 } >> r8 r4 r2
	r2 r4 r8 << { d8 } \\ { c8 } >>
	<< { d8 } \\ { b8 } >> r8 r4 r2
	r2 r4 r8 << { e-flat8 } \\ { e-flat8 } >>
	<< { e!8 } \\ { d-flat8 } >> r8 r4 r2
	r2 r4 r8 << { e8 } \\ { e8 } >>
	<< { f8 } \\ { d8 } >> r8 r4 r2
	R1
	< c e-flat >8\ff r < c e-flat > r < c e-flat > r < c e-flat > r
	< c e-flat > r < c e-flat > r < c e-flat > r < c e-flat > r
	< b d >8 r r4 r2
	< c e-flat >8 r < c e-flat > r < c e-flat > r < c e-flat > r
	< b d >8 r r4 r2
	< c e-flat >8 r < c e-flat > r < c e-flat > r < c e-flat > r
	< b d >8 r r4 r2
	
	s1*46
	
	s1*34
	
	< c, c' >8\ff r < c c' > r << { g'8 } \\ { g8 } >> r r4
	< c, c' >8 r < c c' > r << { g'8 } \\ { g8 } >> r r4
	
	R1*47
	
	< b, b' >8\f r r4 < b b' >8 r r4
	< c c' >8 r r4 < c c' >8 r r4
	< c' d >8 < c d > r < c d >[ < c d > < c d >] r < c d >
	< c e-flat > < c e-flat > r < c e-flat >[ < c e-flat > < c e-flat >] r < c e-flat >
	
	R1*4
	
	< c, c' >8\f r r4 r2
	
	R1*12
	
	< c c' >8\ff r r4 r2
	
	R1*7
	
	< c c' >8\ff r r4 < c c' >4 < c c' >8 < c c' >
	< c c' > r r4 < c c' >4 < c c' >8 < c c' >
	< c c' > r r4 r2
	r2 < f f' >8^> r r << { g8 } \\ { g8 } >>
	< c, c' >8 r r4 < c c' >4 < c c' >8 < c c' >
	< c c' > r r4 < c c' >4 < c c' >8 < c c' >
	< c c' > r r4 r2
	r2 < f f' >8^> r r << { g8 } \\ { g8 } >>
	< c, c' >8 r < c c' > r < c c' > r < c c' > r
	< c c' > r  < c c' > r < c c' > r < c c' > r
	< c c' > r < c c' > r < c c' > r < c c' > r
	< c c' > r < c c' > r < c c' > r < c c' > r
	<< { c'8[ c, e g] } \\ { c,8[ c c e] } >> < c c' >8[ < c c' > < c c' > < c c' >]
	< c c' >4 < c c' > < c c' > < c c' >
	<< { c1\fermata } \\ { c1 } >>
}
