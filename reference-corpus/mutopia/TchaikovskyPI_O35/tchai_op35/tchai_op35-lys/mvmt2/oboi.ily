\version "2.20.0"
theOboes =  \relative d'' {
	
	\clef "treble"
	\key g \minor
	
	<< { a2.^\p^\< } \\ { R1*3/4 } >>
	<< { c2 d4^\! } \\ { r4 r f,\p\< } >>
	<< { b-flat8 r r4 r } \\ { g2( g-flat4)\! } >>
	<< b-flat2. \\ f2. >>
	
	R1*3/4*2
	
	<< { g-flat4^\pp(^\<  f) g(^\! } \\ { R1*3/4 } >>
	<< { f-sharp4) r r } \\ { R1*3/4 } >>
	
	R1*3/4*44
	
	r4 r r8 < b-flat g' >8\mf
	< a-flat a-flat' >[ < a f-sharp' >] < b-flat g' >4 r8 < b-flat g' >8
	< a-flat a-flat' >[ < a f-sharp' >] < b-flat g' >4 r
	< c-sharp g' > < d f-sharp > r
	< b f' >_\markup { \italic dim. } < c! e > < a e-flat' >
	< b-flat d > < g d-flat' > < a-flat c >8 r
	
	R1*3/4*36
	r1*3/4^\fermata
	
	<< { a2.^\p^\< } \\ { R1*3/4 } >>
	<< { c2 d4\! } \\ { r4 r f,\p } >>
	<< { b-flat8 r r4 r } \\ { g2(_\< g-flat4)\! } >>
	<< { b-flat2. } \\ { f2. } { s4\> s4 s4\! } >>
	
	R1*3/4*2
	
	<< { g-flat4(^\cr f) g( } \\ { R1*3/4 } >>
	<< { f-sharp4) r r } \\ { R1*3/4 } >>
	
	R1*3/4*7
	
	< f c' >2.\mf
	R1*3/4
	< a-flat f' >2.\p
	R1*3/4
	< d g-sharp >2.
	
	R1*3/4*3
	r1*3/4^\fermata
}
