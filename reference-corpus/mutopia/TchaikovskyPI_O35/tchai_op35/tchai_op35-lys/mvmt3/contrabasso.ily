\version "2.20.0"

theBass =  \relative d {
	\clef "bass"
	\key d \major
	
	a8\ff[ a'16( g-sharp] a8)[ a,]
	b-flat2
	b-flat'
	b-flat,4 a8 r
	a'8[ a16( g-sharp] a8)[ a,]
	b-flat4 b
	c-sharp d
	c-sharp8 r r4
	
	R1*2/4*3
	
	f-sharp8-.\f[ f-sharp16( e-sharp] f-sharp8)[ f-sharp,-.]
	g4 g-sharp
	a a-sharp
	b b-flat
	a a8\ff r
	
	R1*2/4*36
	
	r8 d\p r d
	r d r d
	r d r d
	r d d r
	d8\f r r4
	d8_\markup { \italic dim. } r r4
	d8 r d r
	r d r d
	
	\set Staff.midiInstrument = #"pizzicato strings"
	r8 d\p^\markup {pizz.} r d
	r d r d
	r d\< r d
	r d r d\!
	
	\set Staff.midiInstrument = #"string ensemble 1"
	r4 r8 d\p^\markup {arco}
	e r r4
	R1*2/4
	r4 r8 a
	b-flat\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 g\p\< r f
	r e r a\!
	b-flat\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 g\p\< r f
	r e r a\!
	b-flat\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 g\p r f
	r e r a
	g-sharp2\mf
	g!2
	f-sharp
	f
	e_\cr
	e-flat4 d
	d-flat2
	c4 b
	b-flat( b-flat')
	a8 r r4
	b-flat,( b-flat')
	a8 r r4
	g-sharp2\mf
	g!
	f-sharp4\< f
	e a,\!
	
	R1*2/4*4
	d8\p r r4
	
	\set Staff.midiInstrument = #"pizzicato strings"
	d8^\markup {pizz.} r r4
	d8 r r4
	d8 r d r
	d\f r r4
	d8\mf r r4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	d8^arco r d r
	d' r c-sharp r
	b\f r r e,
	a r g r
	f-sharp-.\p[\< e-. d-. c-sharp-.]
	b[ a] d4->\!
	f-sharp8\f r r e
	a r e'\p[ d]
	c-sharp-.[\< b-. a-. g-.]
	f-sharp-.[ e-.]\! d-.\f r
	
	\set Staff.midiInstrument = #"pizzicato strings"
	b8\mf^\markup {pizz.} r r4
	b8 r b r
	b r b' r
	b r r4
	b,8 r r4
	b8 r b r
	b r b' r
	b r r4
	b8\f r r4
	R1*2/4
	b8 r r4
	R1*2/4
	b8 r r4
	a8 r r4
	g-sharp8 r f-sharp r
	f r e r
	d-sharp r r4
	d!8 r r4
	c-sharp8 r r4
	b8 r b-flat r
	a r r4
	a-flat8 r r4
	g8\> r f-sharp\! r
	e\p r r4
	
	R1*2/4*4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	a8\ff^arco r r4
	
	R1*2/4*34
	
	r4 r8 a8
	r a r a
	r a r a
	r a r a
	r a r a
	r a r a
	r a r a
	r a r a
	r a f-sharp'\mf[ f-sharp]
	f-sharp4 e8[ d]
	c-sharp[( b]) f-sharp'[ f-sharp]
	f-sharp4 e8[ d]
	c-sharp[( b]) a[ a']
	f-sharp4 e8[ d]
	c-sharp[( b]) f-sharp'[ f-sharp]
	e[ d c-sharp b]
	a r r4
	
	R1*2/4*14
	
	\set Staff.midiInstrument = #"pizzicato strings"
	e'8^\markup {pizz.} r r4
	e8 r r4
	
	R1*2/4*2
	
	e8 r r4
	e8 r r4
	e'8\pp r r4
	d8 r r4
	c-sharp8 r r4
	b8 r r4
	a8 r r4
	g8 r r4
	f-sharp8 r r4
	e8 r r4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	d2~^arco
	d8 r r4
	d8 r r4
	c-sharp8 r r4
	b8 r r4
	
	R1*2/4*13
	
	r8 d\p r d
	r d r d
	r d r d
	r d d r
	d8\f r r4
	d8_\markup { \italic dim. } r r4
	d8 r d r
	r d r d
	
	\set Staff.midiInstrument = #"pizzicato strings"
	r8 d\p^\markup {pizz.} r d
	r d r d
	r d\< r d
	r d r d\!
	
	\set Staff.midiInstrument = #"string ensemble 1"
	r4 r8 d\p^\markup {arco}
	e r r4
	R1*2/4
	r4 r8 a\mf
	b-flat r r4
	a8_\markup { \italic dim. } r r4
	r8 g\p\< r f
	r e r a\!
	b-flat\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 g\p\< r f
	r e r a\!
	b-flat\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 g\p r f
	r e r a
	g-sharp2\mf
	g!2
	f-sharp
	f
	e_\cr
	e-flat4 d
	d-flat2
	c4 b
	b-flat\f( b-flat')
	a8 r r4
	b-flat,( b-flat')
	a8 r r4
	g,2\f~
	g4 r
	r8 a[ g a]
	g[ a] g r
	g-sharp2~
	g-sharp4 r
	r8 a[ g-sharp a]
	g-sharp[ a] g-sharp r
	g-sharp2\f
	a
	b
	c4~ c8 r
	
	R1*2/4*18
	
	b-flat8\ff r b-flat[ b-flat]
	f'[ f] e r
	
	R1*2/4*2
	
	b-flat8 r b-flat[ b-flat]
	f'[ f-sharp] g r
	
	R1*2/4*2
	
	e-flat8 r e-flat[ e-flat]
	e-flat[ e-flat] e-flat r
	
	R1*2/4*2
	
	g8 r g[ g]
	g[ g] g r
	r4 r8 g
	g[ g] g r
	r4 r8 g
	g[ g g g]
	g[ g g g]
	g[ g g g]
	f-sharp![ f-sharp\p] r f-sharp_\cr
	r8 f-sharp r f-sharp
	r f-sharp\< r f-sharp
	r f-sharp[ f-sharp f-sharp]\!
	f\f[ f\p] r f\<
	r f r f
	r f r f
	r f[ f f]\!
	e\f[ e\p]\< r e
	r e[ e e]\!
	e-flat\f[ e-flat\p] r e-flat\<
	r e-flat[ e-flat e-flat]\!
	d8\f r r4
	
	R1*2/4*3
	
	g,8\ff r r4
	
	R1*2/4*26
	
	\set Staff.midiInstrument = #"pizzicato strings"
	r4 r8 g'\mf^\markup {pizz.}
	r g, r g
	r g r g
	r g r g
	r g r g
	r g r g
	r g r g
	r g r g
	r g r g\mf
	r g r g
	r g r g
	r g r g
	r g r g
	r g r g
	r g r g
	r g r g
	r8 g r4
	
	R1*2/4*30
	
	\set Staff.midiInstrument = #"string ensemble 1"
	r8 e-flat''^arco r4
	r8 d r4
	
	R1*2/4*6
	
	r8 e-flat r4
	r8 d\< r4
	r8 c r4
	r8 b, r4
	r8 b-flat\! r4
	a2\pp~
	a
	a2~
	a
	a~
	a
	a~
	a~
	a8 r r4
	R1*2/4
	
	\set Staff.midiInstrument = #"pizzicato strings"
	a8\pp^\markup {pizz.} r r4
	R1*2/4
	a8 r r4
	
	R1*2/4*11
	
	\set Staff.midiInstrument = #"string ensemble 1"
	r8 d\p^arco r d
	r d r d
	r d r d
	r d d r
	d8\f r r4
	d8_\markup { \italic dim. } r r4
	d8 r d r
	r d r d
	
	\set Staff.midiInstrument = #"pizzicato strings"
	r8 d\p^\markup {pizz.} r d
	r d r d
	r d\< r d
	r d r d\!
	
	\set Staff.midiInstrument = #"string ensemble 1"
	r4 r8 d\p^\markup {arco}
	e r r4
	R1*2/4
	r4 r8 a
	b-flat\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 g\p\< r f
	r e r a\!
	b-flat\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 g\p\< r f
	r e r a\!
	b-flat\mf r r4
	a8_\markup { \italic dim. } r r4
	r8 g\p\< r f
	r e r a\!
	g-sharp2
	g!2\mf
	f-sharp
	f
	e_\cr
	e-flat4 d
	d-flat2
	c4 b
	b-flat( b-flat')
	a8 r r4
	b-flat,( b-flat')
	a8 r r4
	g-sharp2\mf
	g!
	f-sharp4\< f
	e a,\!
	
	R1*2/4*4
	d8\p r r4
	
	\set Staff.midiInstrument = #"pizzicato strings"
	d8^\markup {pizz.} r r4
	d8 r r4
	d8 r d r
	d\f r r4
	d8\mf r r4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	d8^arco r d r
	d' r c-sharp r
	b\f r r e,
	a r g r
	f-sharp-.\p[\< e-. d-. c-sharp-.]
	b[ a] d4->\!
	f-sharp8\f r r e
	a r e'\p[ d]
	c-sharp-.[\< b-. a-. g-.]
	f-sharp-.[ e-.]\! d-.\f r
	
	\set Staff.midiInstrument = #"pizzicato strings"
	b8\mf^\markup {pizz.} r r4
	b8 r b r
	b r b' r
	b r r4
	b,8 r r4
	b8 r b r
	b r b' r
	b r r4
	b8\f r r4
	R1*2/4
	b8 r r4
	R1*2/4
	b8 r r4
	a8 r r4
	
	\set Staff.midiInstrument = #"string ensemble 1"
	g8^arco r f-sharp r
	e r b r
	a2\f~\>
	a2~\!_\markup { \dynamic pp \italic {poco a poco cresc.}}
	a2~^\cr
	a2
	a2~^\cr
	a2~
	a2~
	a2
	a2~^\markup { \italic {sempre cresc.}}
	a2~
	a2~
	a2~
	a2~
	a2~
	a2~
	a2
	a2\f
	a
	a
	a
	r8 a r a
	r a r a
	r a r a
	r a[ a a]
	d\ff r d[ d]
	g[ g] d r
	
	R1*2/4*2
	
	b8 r b[ b]
	e[ e] b r
	
	R1*2/4*2
	
	g'8 r g[ g]
	c[ c] g r
	
	R1*2/4*2
	
	e8 r e[ e]
	a[ a] e r
	
	R1*2/4*2
	
	e8 r e[ e]
	a[ a] e r
	
	R1*2/4*2
	
	e8 r e[ e]
	R1*2/4
	e8 r e[ e]
	R1*2/4
	e8[ e] r4
	e8[ e] r4
	d8[ d] r4
	c-sharp8[ c-sharp] r4
	c8[ c] r4
	b8[ b] r4
	b-flat8[ b-flat] r_\markup { \dynamic p \italic cresc. } b-flat
	r b-flat r b-flat
	r b-flat r b-flat
	r b-flat r b-flat
	a\f[ a-sharp b c-sharp]
	d[ d-sharp] e[ f-sharp]
	g[ g-sharp a b]
	a[ g! f-sharp e]
	d r d\f[ d]
	d2~
	d4 c-sharp8->[ c-sharp->]
	c-sharp4-> b8->[ a->]
	d8-> r d8[ d]
	d2~
	d4 c-sharp8->[ c-sharp->]
	c-sharp4-> b8->[ a->]
	d8 r f-sharp r
	g r b r
	e, r d4->~
	d8 r c-sharp r
	d r f-sharp r
	g r b r
	e, r d4->~
	d8 r c-sharp r
	d\f r a r
	d r a r
	d r a r
	d r a r
	d[ f-sharp a a-sharp]
	b[ d a! g]
	f-sharp[ d a'! a-sharp]
	b[ d a! g]
	f-sharp[ b a g]
	f-sharp[ b a g]
	f-sharp r r4
	f8 r r4
	e8 r r4
	a8 r r4
	d,8\ff[ a'] d,[ a']
	d,[ a'] d,[ a']
	d,[ a'] d,[ a']
	d,[ a'] d,[ a']
	d,8 r d[ d]
	a'[ a] d,[ f-sharp]
	a r r4
	d,8 r r4\fermata
	
}
