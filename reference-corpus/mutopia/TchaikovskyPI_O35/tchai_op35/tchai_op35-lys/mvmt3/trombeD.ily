\version "2.20.0"

theTrumpets =  \relative d' {
	\clef "treble"
	\time 2/4
	\key c \major
	
	\set Score.skipBars = ##t
	\override Score.TupletBracket.bracket-visibility = ##f
	
	\transposition d
	
	<< { g8 } \\ { g8\ff } >> r8 r4		|
	r4 << { d'4~ } \\ { c4~ } >>		|
	<< { d4 d,~ } \\ { c'4 c,4~ } >>	|
	<< { d4 g8 } \\ { c,4 b8 } >> r8	|
	R1*2/4
	r4 < f-sharp' d' >4~					|
	< f-sharp d' > < d f-sharp! >			|
	< d g >8 r r4						|
	
	R1*2/4*7
	
	r4 < b' d >8\ff r
	
	R1*2/4*128
	
	< b d >8 r r4
	
	R1*2/4*167
	
	< a-flat, a-flat' >8\ff r < a-flat a-flat' >[ < a-flat a-flat' >]
	< b-flat b-flat' >[ < b-flat b-flat' >] < b a-flat' > r
	
	R1*2/4*2
	
	< a-flat a-flat' >8 r < a-flat a-flat' >[ < a-flat a-flat' >]
	< b-flat b-flat' >[ < b-flat b-flat' >] < c a-flat' > r
	
	R1*2/4*2
	
	< f d-flat' >8 r < f d-flat' >[ < f d-flat' >]
	< e! d-flat' >[ < e d-flat' >] < f d-flat' > r
	
	R1*2/4*2
	
	< b-flat d >8 r < b-flat d >[ < b-flat d >]
	< f c' >[ < f c' >] < f d' > r
	r4 r8 < b-flat d >
	< f c' >[ < f c' >] < f d' > r
	r4 r8 < b-flat d >
	< f c' >[ < f c' > < f d' > < f d' >]
	< f c' >[ < f c' > < f d' > < f d' >]
	< f c' >[ < f c' > < f d' > < f d' >]
	< g d-flat' > r r4
	
	R1*2/4*15
	
	< f f' >8\ff r r4
	
	R1*2/4*190
	
	< c c' >8\f r r4
	
	R1*2/4*23
	
	< c c' >8\ff r < c c' >[ < c c' >]
	< c c' >[ < c c' >] < c c' > r
	
	R1*2/4*2
	
	< c c' >8 r < c c' >[ < c c' >]
	< b b' >[ < b b' >] < c c' > r
	
	R1*2/4*2
	
	< f c' >8 r < f c' >[ < f c' >]
	< f d' >[ < f f' >] < f c' > r
	
	R1*2/4*2
	
	< d d' >8 r < d d' >[ < d d' >]
	< d d' >[ < d d' >] < d d' > r
	
	R1*2/4*2
	
	< d d' >8 r < d d' >[ < d d' >]
	< d d' >[ < d d' >] < d d' > r
	
	R1*2/4*2
	
	< d d' >8 r < d d' >[ < d d' >]
	R1*2/4
	< d d' >8 r < d d' >[ < d d' >]
	R1*2/4
	< d d' >8[ < d d' >] r4
	< d d' >8[ < d d' >] r4
	< d d' >8[ < d a-flat' >] r4
	< d d' >8[ < d g >] r4
	< e e' >8[ < c c' >] r4
	< f f' >8[ < c c' >] r4
	< c c' >8[ < c c' >] r4
	
	R1*2/4*6
	
	r4 r8 << g'8 \\ g8\f >>
	< e c' >8 r r4
	
	R1*2/4*3
	
	< c c' >8\f r r4
	
	R1*2/4*3
	
	< c c' >8 r r4
	
	R1*2/4*3
	
	< c c' >8 r r4
	
	R1*2/4*3
	
	< c c' >8\f r < d b' > r
	< e c' >8 r < d b' > r
	< e c' >8 r < d b' > r
	< e c' >8 r < d b' > r
	< c c' > r r4
	r4 < c c' >~
	< c c' >8 r r4
	r4 < c c' >~
	< c c' >8 r < c c' >4~
	< c c' >8 r < c c' >4~
	< c c' >8 r r4
	< c c' >8 r r4
	< c c' >8 r r4
	< b b' >8 r r4
	< c c' >8\ff[ < g' b >] < c, c' >[ < g' b >]
	< c, c' >8[ < g' b >] < c, c' >[ < g' b >]
	< c, c' >8[ < g' b >] < c, c' >[ < g' b >]
	< c, c' >8[ < g' b >] < c, c' >[ < g' b >]
	< c, c' >8 r < c c' >[ < c g' >]
	< d b' >[ < b' d >] << c8 \\ c8 >> r
	< b d >8 r r4
	< e, c' >8 r r4\fermata
}
