\version "2.20.0"

theSolo =  \relative d' {
	\clef "treble"
	\key g \minor
	
	r1*3/4
	R1*3/4*10
	
	r4 r d_\markup { \dynamic p \italic {molto espress.}}^\markup {con sordino}
	\noDynamic g4.\p a8-.[ b-flat-. c-.]
	d4--~ d-- d--
	d2\trill^\( \tuplet 5/4 { d32[( e-flat d c-sharp d) } f16 e-flat]^\)
	d2( d,4)
	g4. a8[( b-flat c])
	d4--( d-- d--)
	c16[( b-flat a8]~ a4) b-flat16[( a g8])
	f-sharp16[( e-flat d8]~ d4) d
	g4. a8[( b-flat c])
	d4-- d-- d--
	d2\trill^\( \tuplet 5/4 { d32[( e-flat d c-sharp d) } f16 e-flat]^\)
	d2( d,4)
	g4. a8[( b-flat c])
	d4--~\< d-- d--\!
	e-flat^\trill \grace { d16[ e-flat] } f4_\cr f-sharp\trill \bar "" \grace { e16[ f] } \bar "|"
	g8--\f[ b-flat,( d b-flat') a-- g--]
	f-sharp[( a d,) g(_\markup { \italic dim. } f e-flat])
	d[( f b-flat,) a\p( b-flat c])
	c-sharp4( d8)[ b-flat( a g])
	c-sharp4( d8)[ b-flat( a g])
	f-sharp[( g] d) e4( f-sharp8)
	g4 r r
	
	R1*3/4*5
	
	g'8\f[( e-flat] b-flat4.)
	c'8(
	b-flat[\> g e-flat) b-flat( d e-flat])\!
	f\p[( g] b-flat,4.) e-flat8(
	f[ g] b-flat,)[ b( d c])
	f,4.( f-sharp8 g4)
	a-flat4~ \tuplet 3/2 { a-flat8[ b-flat c] } \tuplet 3/2 { d[ e-flat f] }
	g8\f[( e-flat]) b-flat4. c'8(
	b-flat8[ g] \tuplet 3/2 { e)[ c-- d--] } \tuplet 3/2 { e-flat--[ f-- g--] }
	a-flat4_\markup { \italic piu \dynamic f } g8--[ f-- e-flat( d])
	f[( d) b-flat( d-flat) c g--]
	a-flat[(\> c-flat) b-flat-- f-- g( b-flat])\!
	e-flat,[(\< e f) f-sharp( g g'])\!
	a-flat4\f g8--[ f-- e-flat( d])
	b-flat'[( g) e-flat-- e-flat--] e-flat'4~
	e-flat~ e-flat8[ e-flat,] e-flat'4~
	e-flat~ e-flat8[ e-flat,( e-flat' d])
	c-sharp[( a d) a( d_\markup { \italic dim. } c])
	b[( g) c-. b-flat-. a( f])
	b-flat-.[ a-flat-. g( b-flat e-flat, e])
	f[( e-flat! d) c( b c]
	e-flat)[ c,-.( d-. e-flat-. f-. f-sharp-.])
	\tuplet 3/2 { g-.\p[\< g,-. b-.] } \tuplet 3/2 { d[ g b]^(\!\> } \tuplet 3/2 { e-flat![ d b-flat]^)\! }
	\tuplet 3/2 { r8 a-flat,-.[\< c-.] } \tuplet 3/2 { f-.[ a-flat-. c-.]^(\!\> } \tuplet 3/2 { f[ e-flat b-flat!])\! }
	\override TupletBracket.transparent = ##t
	\tuplet 3/2 { r e-flat8[( d] c[ d e-flat]) a[( g a-flat]) }
	\tuplet 3/2 { b-flat[( g e-flat] c)[ b-flat g] e-flat[( b-flat g]) }
	\tuplet 3/2 { a-flat--[_\cr b-flat-- b--] c--[ d-- e-flat--] f--[ g-- a-flat--] }
	\tuplet 3/2 { c--[ b-- c--] c--[ d-- e-flat--] f--[ g-- a-flat--] }
	\tuplet 3/2 { c--[ d-- e-flat--] e-flat,[( f-sharp g] a)[ a, a']~ }
	\tuplet 3/2 { a[ b-flat( a] f-sharp[ d c]) a[( f-sharp a]) }
	
	\override TupletBracket.transparent = ##f
	d,8 r r4 d\p
	g4. a8[( b-flat c])
	d-.[( d-.]) \tuplet 3/2 { d-.[( d-. d-.] } \tuplet 3/2 { d-.[ d-. d-.]) }
	d2\trill^\( \tuplet 5/4 { d32[( e-flat d c-sharp d) } f16 e-flat]^\)
	d2( d,4)
	g4. a8[( b-flat c])
	d[( d,~ d d' d, d'])
	c16[( b-flat a8]~ a4) b-flat16[( a g8])
	f-sharp16[( e-flat d8]~ d4) d
	g4. a8[( b-flat c])
	d4-- d-- d--
	d2\trill^\( \tuplet 5/4 { d32[( e-flat d c-sharp d) } f16 e-flat]^\)
	d2( d,4) g4. a8[( b-flat c])
	d4 d d
	e-flat^\trill \grace { d16[ e-flat] } f4_\cr f-sharp\trill \bar "" \grace { e16[ f] } \bar "|"
	g8--\f[ b-flat,( d b-flat') a-- g--]
	f-sharp[( a d,) g(_\markup { \italic dim. } f e-flat])
	d[( f b-flat,) a\p( b-flat c])
	c-sharp4(_\cr d8)[ b-flat( a g])
	c-sharp4( d8)[ b-flat( a g])
	b-flat'\mf[( a g) b-flat'\f( a g])
	f-sharp16[( g) b-flat,( c] c-sharp[ d) f-sharp,( g] a[ b-flat) b-flat,( c]
	c-sharp[ d) a( b-flat]^\< f-sharp[ g)^\! c-sharp,( d] e-flat[ d b-flat a])
	g8[( b-flat) e-flat-- g-- a-- b-flat--]
	
	c-sharp2.~\>\startTrillSpan
	c-sharp!\fermata \bar "" \grace { b16[(\!\stopTrillSpan c-sharp]) } \bar "|"
	d8 r r4 r
	
	R1*3/4*23
}
