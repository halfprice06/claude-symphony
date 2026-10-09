\version "2.20.0"

theBassoons =  \relative d' {
	\set Score.skipBars = ##t
	
	\clef "bass"
	\key g \minor
	
	<< { R1*3/4 } \\ { d2.\p\< } >>
	<< { e-flat2^\p^\< d4^\! } \\ { c2 b-flat4^\! } >>
	<< e-flat2. \\ e-flat,2. >>
	<< f2. \\ b-flat,2. >>
	<< { c4( d e-flat) } \\ { c4\pp( b-flat a) } >>
	<< { c4( d e-flat) } \\ { c4( b-flat a) } >>
	<<  { e-flat'4( d-flat) e( } \\ { a-flat,4(\< d-flat) a(\! } >>
	<< { d!4) d,!4^\p e-flat!8[( g] } \\ { d'8) r r4 r } >>
	<< { b-flat!8[ e-flat g b-flat!)^\< b c]^\! } \\ { r2 e-flat,!4\mf~ } >>
	<< { d'8[_(^\> e-flat d c b a]_)^\! } \\ { e-flat2. }  { s4.\> s4 s8\! } >>
	<< { b-flat'!2 b-flat4~ } \\ { d,2\p d4\pp~ } >>
	<< { b-flat'4 a8[( b-flat] a4) } \\ { d,4 d2 } >>
	
	R1*3/4*40
	
	<< { r4 r r8 d-flat'8^\mf } \\ { R1*3/4 } >>
	<< { c8[ c-flat] b-flat4 r8 d-flat8 } \\ { r4 e-flat,\mf r4 } >>
	<< { c'!8[ c-flat] b-flat4 } \\ { r4 e-flat, } >> r4
	< e-flat e-flat' >4 < d d' > r
	< d-flat d-flat' >_\markup { \italic dim. } < c c' > < c c' >
	< b-flat b-flat' > < b-flat b-flat' > < a-flat a-flat' >8 r
	
	R1*3/4*18
	
	<< { a'4.^> r8 r4 } \\ { d,4. c8[( b-flat a]~ } >>
	<< { R1*3/4 } \\ { a8) r r4 r } >>
	
	R1*3/4*16
	r1*3/4\fermata
	
	<< { R1*3/4 } \\ { d'2._\p\< } >>
	<< { e-flat2 d4 } \\ { c2 b-flat4\! } >>
	<< { \stemDown < e-flat, e-flat' >2. \stemNeutral } \\ { s4.\< s4 s8\! } >>
	<< f2. \\ b-flat,2. >>
	<< { c4( d e-flat) } \\ { c4\pp( b-flat a) } >>
	<< { c4( d e-flat) } \\ { c4( b-flat a) } >>
	<<  { e-flat'4( d-flat) e( } \\ { a-flat,4(\<_\cr d-flat) a(\! } >>
	<< { d4) d,!4( e-flat!4) } \\ { d'8) r r4 r } >>
	R1*3/4
	<< { r4 r e-flat'\mf } \\ { R1*3/4 } >>
	R1*3/4
	<< d2. \\ R1*3/4 >>
	R1*3/4
	<< { r4 r d-flat } \\ R1*3/4 >>
	R1*3/4
	<< c2. \\ R1*3/4 >>
	R1*3/4
	<< { b4 b8[( a-sharp] b4) } \\ { R1*3/4 } >>
	R1*3/4
	<< { e2. } \\  { b-flat!4 b-flat8[( a] b-flat4) } >>
	R1*3/4
	< d, d' >8\pp[( < c-sharp c-sharp' >] < d d' >2)
	R1*3/4
	r1*3/4^\fermata	
}
