\version "2.20.0"

theSolo =  \relative d' {
	\clef "treble"
	\key d \major
	
	R1*2/4*16
	
	a2\f(^\markup {senza sordini}						|
	b-flat8)[ b-flat16(\( a] b-flat8)[ d-.]\)
	a2(
	b-flat8)[ b-flat16(\( a] b-flat8)[ d-.]\)
	a8[ a] < a e' c-sharp' >[ a]
	< a e' a e' >[ a] < a f-sharp' c-sharp' a' >[ a]
	g-sharp4 < b-flat' d e >\downbow
	r4 g-sharp,\downbow
	a2\downbow(
	b-flat8)[ b-flat16(\( a] b-flat8)[ d-.]\)
	a2(
	b-flat8)[ b-flat16(\( a] b-flat8)[ d-.]\)
	a8[ a < a e' c-sharp' > a]
	< a e' a e' >[ a < a f-sharp' c-sharp' a' > a]		|
	
	\set Staff.midiInstrument = #"pizzicato strings"
	r4 < a e' c-sharp' >4^\markup {pizz.}				|
	< a e' a e' > < a e' c-sharp' a' >					|
	
	\set Staff.midiInstrument = #"violin"
	r8^\markup {arco} a[ < a e' c-sharp' > a]			|
	< a e' a e' >[ a < a f-sharp' c-sharp' a' > a]		|
	
	\set Staff.midiInstrument = #"pizzicato strings"
	r4 < a e' c-sharp' >4^\markup {pizz.}				|
	< a e' a e' > < a e' c-sharp' a' >					|
	
	\set Staff.midiInstrument = #"violin"
	a8_\marcato\ff[^\markup {arco} a16\( g-sharp] a4~	|
	a2(
	b-flat8)\)[ b-flat16\( a] b-flat4~
	b-flat2(
	a8)\)[ a16\( g-sharp] a4~
	a2(
	b-flat8)\)[ b-flat16\( a] b-flat4~
	b-flat2(
	b!8)\)[ b16\( a-sharp] b4~
	b2(_\markup { \italic dim. }
	c8)\)[ c16\( b] c4~
	c2(
	c-sharp!8)\)[ c-sharp16( b-sharp] c-sharp4~
	c-sharp)\< b!~
	b\! b-sharp\fermata~_\markup { \italic rit. }
	b-sharp\> c-sharp\fermata\!							|
	
	% TUTTI
	
	d8-.\p[ d16( c-sharp] d8)[ b-.]						|
	c-sharp[ e] a,[ c-sharp16( d])
	e16[\< c-sharp e f-sharp] g[ e a b]
	c-sharp[ a b c-sharp] d[ e f-sharp a]\!
	b8\f[ b16( a-sharp] b8)[ f-sharp-.]
	g-.[ g16( f-sharp] g8)[_\markup { \italic dim. } d-sharp]
	e[ b] c-sharp16[\> g-sharp a a-sharp]\!
	b[ d-sharp, e f-sharp] g[ a, b c-sharp]
	d!8-.\p[ d16( c-sharp] d8)[ b-.]
	c-sharp[ e] a,[ c-sharp16( d])
	e16[\< c-sharp e f-sharp] g[ e a b]
	c-sharp[ a b c-sharp] d[ e f-sharp a]\!
	b-flat8\f[ b-flat16( a] b-flat8)[ d,,-.\p]
	c-sharp[ e] a,[ c-sharp16( d])
	e[ c-sharp d-sharp e] f-sharp[ d-sharp g-sharp a]
	b[\< g-sharp a b] c-sharp[ d e a]\!
	f8\f[ f16( e] f8)[ d,]								|
	a'8[_\markup { \italic dim. } a16( g-sharp] a8)[ a,]
	b-flat16\p[ b c-sharp d] c-sharp[\< d e f]
	f-sharpsharp[ g-sharp a-sharp b] c-sharp[ d e a!]\!
	f8-.\f[ f16( e] f8)[ d,]
	a'8-.[_\markup { \italic dim. } a16( g-sharp] a8)[ a,]
	b-flat16\p[ b c-sharp d] c-sharp[ d e f]
	f-sharpsharp,[\< g-sharp a-sharp b] b-sharp[ c-sharp d-sharp e]\!
	f'8\f[ f16(\> e] f8)[ d,]
	a'8[ a16( g-sharp] a8)[ a,]\!
	b-flat16-.\p[ b-. c-sharp-. d-.] c-sharp[ d e f]
	f-sharpsharp[ g-sharp a-sharp b] c-sharp[ d e a!]
	f8\mf[ f16( e] f8)[ d,]
	a'8[ a16( g-sharp] a8)[ a,]							|
	f-sharp''!8[ f-sharp16( e-sharp] f-sharp8)[ c-sharp,]
	d'8[ d16( c-sharp] d8)[ d,-.]
	g'8[_\cr g16( f-sharp] g8)[ g,]
	a'8[ a, b-flat' b-flat,]
	b'!8[ b16( a-sharp] b8)[ b,!-.]
	c'8[ c, d' d,]
	d'8\f[ d16( c-sharp]) d[ g-sharp, e d]
	c-sharp16[ b-sharp c-sharp d] c-sharp[ e a c-sharp]
	d8[ d16( c-sharp]) d[ g-sharp, e d]
	c-sharp[ b-sharp c-sharp d] c-sharp[ e a c-sharp]
	d8-.[ d16( c-sharp] d8)[ d,-.]
	f'8-.[ f16( e] f8)[ f,-.]
	f-sharp'!-.[\< f-sharp,!-. g'-. g,-.]
	g-sharp'-.[ g-sharp,-. a'-. a,-.\f]\!
	d16[( c-sharp d8]) a16[( g-sharp a8])					|
	d,16[( c-sharp d8]) a16[( g-sharp a8])
	d,16[( c-sharp d8]) a16[(\< g-sharp a8])
	b-flat16[ b-flat b b] c[ c c-sharp c-sharp]\!
	d8\f[ d16\p( c-sharp] d8)[ b]
	c-sharp[ e] a,[ c-sharp16( d])
	e[ c-sharp e f-sharp] g[ e a b]
	c-sharp[\< a b c-sharp] d[ e f-sharp a]\!
	b8\f[ b16( a-sharp] b8)[ f-sharp-.]
	g8-.[ g16( f-sharp] g8)[ d-sharp-.]
	e[ b] c-sharp16-.[\< g-sharp-. a-. a-sharp-.]
	b[ e-sharp, f-sharp g-sharp] a-sharp[ a-sharp b c-sharp]\!
	< b, f-sharp' d' >8\f[ d'16(\( c-sharp] d8)[ b-.]\)
	< a, e' c-sharp' >[ e''] < a,, e' a >[ c-sharp'16 d]
	e[ c-sharp e f-sharp] g[\< e a! b]
	c-sharp[ a b c-sharp]\! d[ e f-sharp g]
	< d,, a' d' >8[ d''16(\( c-sharp] d8)[ b-.]\)		|
	< a, c-sharp' >[ e''] < a,, a' >16[ g-sharp' a b]
	c-sharp[ b c-sharp d] e[ f-sharp g g-sharp]
	\ottava #1 a[ a-sharp b c-sharp] d8\f \ottava #0 r
	d,8\f[ d16(\( c-sharp] d8)[ b-.]\)
	g16[ f-sharp e g] d[ c-sharp b d]
	g,[ f-sharp e g] d[ c-sharp b d]
	g,[ b e g] b[ e g b]
	d8[ d16(\( c-sharp] d8)[ b-.]\)
	g16[ f-sharp e g] d[ c-sharp b d]
	g,[ f-sharp e g] d[ c-sharp b d]
	g,[ b e g] b[ e g b]
	d8-.[ d16( c-sharp] d8)[ < d,, b' >-.]				|
	R1*2/4
	d''8-.[ d16( c-sharp] d8)[ < d,, b' >-.]
	R1*2/4
	d''8-.[ d16( c-sharp] d8)[ < d,, b' >-.]
	d''8-.[ d16( c-sharp] d8)[ < d,, b' >-.]
	d''8[ < d,, b' >-.] d''8[ < d,, b' >-.]
	d''8[ < d,, b' >-.] d''8[ < d,, b' >-.]
	d-sharp''-.[ d-sharp16( c-sharpsharp] d-sharp8)[ g-sharp,]
	b8[ b16( a-sharp] b8)[ b,]
	g-sharp'[ g-sharp, e-sharp' e-sharp,]
	b'!16[ d,! f g!] g-sharp[ d' f g-sharp]
	a8-.[ a16( g-sharp] a8)[ d,-.]
	f8[ f16( e] f8)[ f,]
	d'[\> d,] b'[ b,]\!
	g-sharp'16[ g-sharp, a b] c-sharp![ d e f-sharp!]
	g-sharp[ b, c-sharp d] e[ f-sharp g a]
	b[ d, e f-sharp] g-sharp[ a b c-sharp]
	d[ g-sharp, a b] c-sharp[\< d e f-sharp]
	g-sharp[ a b c-sharp] d[ e f-sharp g-sharp]\!			|
	
	%%% POCO MENO MOSSO %%%
	
	a8 r r4												|
	
	R1*2/4*2
	
	r4 a,,8-.\f[( e-.])									|
	g-sharp4( f-sharp8[ e])
	d-.[ \tuplet 3/2 { d16(\( e d]) } c-sharp8[ b]\)
	a2~(
	a4\glissando a'8[ e-.])
	g-sharp4( f-sharp8[ e])
	d-.[ \tuplet 3/2 { d16(\( e d]) } c-sharp8[ b]\)
	a2~(
	a4\glissando f-sharp'8[ f-sharp-.])
	f-sharp4( e8[ d])
	c-sharp[ b]( f-sharp')[ f-sharp-.]
	f-sharp4( e8[ d])
	c-sharp4( a'8[ e-.])
	f-sharp4( e8[ d])
	c-sharp[ b]( f-sharp')[ f-sharp-.]
	f-sharp4( e8[ d])									|
	
	%%% TEMPO 1 %%%
	
	c-sharp16[ c-sharp d e] f-sharp8[ f-sharp^\downbow]		|
	f-sharp4^\downbow e8^\downbow[ d^\downbow]
	c-sharp^\downbow[ b^\downbow]( f-sharp')[ f-sharp^\downbow]
	f-sharp4^\downbow e8^\downbow[ d^\downbow]
	c-sharp16[ e f-sharp g-sharp] a8^\downbow[ f-sharp^\downbow]
	f-sharp4^\downbow e8^\downbow[ d^\downbow]
	c-sharp^\downbow[ b^\downbow]( f-sharp')[ f-sharp^\downbow]
	f-sharp4^\downbow e8^\downbow[ d^\downbow]
	c-sharp8:16[ c8: b8: a8:]
	g-sharp!:[ e': g,: g-sharp:]
	a:[ g-sharp!:] a:[ b:]
	c-sharp:[ a': f-sharp: g-sharp:]
	a:[ a':] a,:[ a,:]
	g-sharp!:[ e': g,: g-sharp:]
	a:[ g-sharp:] a:[ b:]								|
	c-sharp:[ a': f-sharp: g-sharp:]
	a16[ c-sharp, e a] a[_\cr g-sharp a a-sharp]
	b[ a-sharp b c-sharp] b[ a g-sharp f-sharp]
	e[ f-sharp g-sharp a] b[ c-sharp d f-sharp]
	a[ e f-sharp g-sharp] a[ e f-sharp g-sharp]
	a[ e a b] c-sharp[ d c-sharp c]
	b[ a-sharp b c-sharp!] b[ a g-sharp f-sharp]
	e[ f-sharp g-sharp a] \ottava #1 b[ c-sharp d f-sharp]
	a[ e f-sharp g-sharp] a[ e f-sharp g-sharp]
	a[ \ottava #0 a, a a,] r a[ a a,]
	< g-sharp g-sharp' >8:[ < a a' >: < b b' >: < f-sharp' f-sharp' >:]
	< e e' >:[ < f-sharp f-sharp' >: < g-sharp g-sharp' >: < a a' >:]
	< g-sharp g-sharp' >:[ < a a' >: < b b' >: < g-sharp g-sharp' >:]
	< a a' >:[ < b b' >: < b-sharp b-sharp' >: < c-sharp c-sharp' >:]
	< g-sharp g-sharp' >:[ < a a' >: < b b' >: < f-sharp' f-sharp' >:]
	< e e' >:[ < f-sharp f-sharp' >: < g-sharp g-sharp' >: < a a' >:]
	< g-sharp g-sharp' >:[ < e e' >: < f-sharp f-sharp' >: < g-sharp g-sharp' >:]		|
	
	%%% MOLTO MENO MOSSO %%%
	
	< a a' >8 r r4										|
	
	R1*2/4*11
	
	r4 e8\p[( f-sharp])									|
	g-sharp4( \grace { f-sharp16[ g-sharp] } f-sharp8[ e])
	\slurUp \grace { d-sharp16[( e] } d-sharp8[ c-sharp]) \slurNeutral r4
	R1*2/4
	r4 e8\p[( f-sharp])
	g-sharp4( \grace { f-sharp16[ g-sharp] } f-sharp8[ e])
	\grace { d-sharp16[( e] } d-sharp8[ c-sharp]) r4
	R1*2/4
	r4 e8[( e-sharp])
	f-sharp4( \grace { e!16[ f-sharp] } e8[ d])
	\grace { c-sharp16[ d] } c-sharp8[(_\markup { \italic rall. } b]) a-sharp[ b]
	d4( \grace { c-sharp16[ d] } c-sharp8[ b])
	\grace { a16[( b] } a8[ g-sharp]) f-sharpsharp[ g-sharp]
	b4( \grace { a16[ b] } a8[ g])
	\grace { f-sharp16[( g] } f-sharp8[ e]) d-sharp[ e]
	g4( \grace { f-sharp16[ g] } f-sharp8[ e])
	g4(^\< \grace { f-sharp16[ g] } f-sharp8[ e])^\!
	g4(^\> \grace { f-sharp16[ g] } f-sharp8[ e])^\!
	\grace { d!16[( e] } d8[ c-sharp) d-- e--]			|
	g4( \grace { f-sharp16[ g] } f-sharp8[ e])
	g4(^\< \grace { f-sharp16[ g] } f-sharp8[ e])^\!
	g4( \grace { f-sharp16[ g] } f-sharp8[ e])
	\grace { d!16[( e] } d8[ c-sharp)\> d e]\!
	g4\p( \grace { f-sharp16[ g] } f-sharp8[ e])
	d8[( c-sharp) d-. e-.]
	g4( \grace { f-sharp16[ g] } f-sharp8[ e-.])
	\grace { d16[ e] } d8[( c-sharp) d e]
	b-flat8-.[ b-flat16( c] b-flat8)[ a]
	g-sharp!8-.[ g-sharp16( a] g-sharp8)[ a]
	b-flat8-.[ b-flat16( c] b-flat8)[ a]
	g-sharp!8-.[ g-sharp16( a] g-sharp8)[ a]
	b-flat16[ c b-flat a] g-sharp![ a g-sharp a]
	b-flat[ c b-flat a] g-sharp![ a g-sharp a]
	b-flat[\< c b-flat a] g-sharp![ a g-sharp a]
	b-flat[ b b-flat b] b-sharp[ c-sharp! b-sharp c-sharp]\!	|
	
	%%% TUTTI %%%
	
	d8-.\p[ d16( c-sharp] d8)[ b-.]						|
	c-sharp[ e] a,[ c-sharp16( d])
	e16[\< c-sharp e f-sharp] g[ e a b]
	c-sharp[ a b c-sharp] d[ e f-sharp a]\!
	b8\f[ b16( a-sharp] b8)[ f-sharp-.]
	g-.[ g16( f-sharp] g8)[_\markup { \italic dim. } d-sharp]
	e[ b] c-sharp16[\> g-sharp a a-sharp]\!
	b[ d-sharp, e f-sharp] g[ a,! b c-sharp]
	d8-.\p[ d16( c-sharp] d8)[ b-.]
	c-sharp[ e] a,[ c-sharp16( d])
	e16[\< c-sharp e f-sharp] g[ e a b]
	c-sharp[ a b c-sharp] d[ e f-sharp a]\!
	b-flat8\f[ b-flat16( a] b-flat8)[ d,,-.\p]
	c-sharp[ e] a,[ c-sharp16( d])
	e[ c-sharp d-sharp e] f-sharp[\< d-sharp g-sharp a]
	b[ g-sharp a b] c-sharp[ d e a]\!
	f8\f[ f16( e] f8)[ d,]								|
	a'8[_\markup { \italic dim. } a16( g-sharp] a8)[ a,]
	b-flat16\p[ b c-sharp d] c-sharp[\< d e f]
	f-sharpsharp[ g-sharp a-sharp b] c-sharp[ d e a!]\!
	f8-.\f[ f16( e] f8)[ d,]
	a'8-.[_\markup { \italic dim. } a16( g-sharp] a8)[ a,]
	b-flat16\p[ b c-sharp d] c-sharp[ d e f]
	f-sharpsharp,[\< g-sharp a-sharp b] b-sharp[ c-sharp d-sharp e]\!
	f'8\f[ f16(\> e] f8)[ d,]
	a'8[ a16( g-sharp] a8)[ a,]\!
	b-flat16-.\p[\< b-. c-sharp-. d-.] c-sharp[ d e f]
	f-sharpsharp[ g-sharp a-sharp b] c-sharp[ d e a!]\!
	f8\f[ f16( e] f8)[ d,]
	a'8[ a16( g-sharp] a8)[ a,]							|
	f-sharp''!8[ f-sharp16( e-sharp] f-sharp8)[ c-sharp,]
	d'8[ d16( c-sharp] d8)[ d,-.]
	g'8[_\cr g16( f-sharp] g8)[ g,]
	a'8[ a, b-flat' b-flat,]
	b'!8[ b16( a-sharp] b8)[ b,!-.]
	c'8[ c, d' d,]
	d'8-.\f[ d16( c-sharp]) d-.[ g-sharp,-. e-. d-.]
	c-sharp16[ b-sharp c-sharp d] c-sharp[ e a c-sharp]
	d8-.[ d16( c-sharp] d)[ g-sharp,-. e-. d-.]
	c-sharp[ b-sharp c-sharp d] c-sharp[ e a c-sharp]
	
	%%% NEW STUFF %%%
	
	e8[ b16( a-sharp] b8)[ e,16( d-sharp]
	e8)[ b16( a-sharp] b8)[ e,16( d-sharp]
	e8) r r4
	r4 r16 b''16-.[ c-sharp-. d-sharp-.]
	e8[ b16( a-sharp] b8)[ e,16( d-sharp]
	e8)[ b16( a-sharp] b8)[ e,16( d-sharp]
	e8) r r4
	r4 r16 b''16-.[ c-sharp-. d-sharp-.]
	e8 r8 r16 b-.[ c-sharp-. d-sharp-.]
	e8 r r16 c-.[ d!-. d-sharp-.]
	e8 r r16 b[ d! d-sharp]
	e8 r r16 c\p[ d! e]
	f8[ f16( e] f8)[ d-.]
	e[ g] c,[ b-flat16( c])
	c-sharp!-.[ d-. g,-. g-sharp-.] a-.[ b-flat-. e,-. f-.]
	f-sharp!-.[ g-. a-. b-flat-.] b-.[ c-. d-. e-.]
	f8[ f16( e] f8)[ d-.]
	e[ g] c,[ b-flat16( c])
	c-sharp!-.[ d-. g,-. g-sharp-.] a-.[ b-flat-. e,-. f-.]
	f-sharp!-.[ g-. g-sharp-. a-.] b-flat-.[ b-. c-. c-sharp-.]
	d8-.[ d16( c-sharp] d8)[ b]
	c-sharp[ e] a,[ g16( g-sharp])
	a[ b-flat e, f] f-sharp[ g c-sharp,! d]
	d-sharp[ e f g] g-sharp[ a b! c-sharp!]
	d8-.[ d16( c-sharp] d8)[ b]
	c-sharp[ e] a,[ g16( g-sharp])
	a[ b-flat e, f] f-sharp[ g c-sharp,! d]
	d-sharp[ e a, b!] b-sharp[ c-sharp f-sharp, g]
	g-sharp[ a c-sharp,! d] d-sharp[ e a, b]
	c[ c-sharp d\< e] f[ g g-sharp a]\!
	b-flat8\f r r4
	r4 r8 b-flat,16\f[ < g-flat' d-flat' >]
	< g-flat d-flat' >[ b-flat, d-flat < b-flat' g-flat' >]
		< b-flat g-flat' >[ d-flat, g-flat < d-flat' b-flat' >]
	< d-flat b-flat' >[ g-flat, b-flat < g-flat' d-flat' >] < g-flat d-flat' >[ b-flat, b-flat < g-flat' d-flat' >]
	< f d'! >8 r r4
	r4 r8 b-flat,,16[ < g'! d'! >]
	< g d' >[ b-flat, d < b-flat' g' >] < b-flat g' >[ d, g < d' b-flat' >]
	< d b-flat' >[ g, b-flat < g' d' >] < g d' >[ b-flat, b-flat < g' d' >]
	< g e-flat' >8 r r4
	r4 r8 \stemDown b-flat,,16[ < g' e-flat' >] \stemNeutral
	< g e-flat' >[ b-flat, e-flat < b-flat' g' >] < b-flat g' >[ e-flat, g < e-flat'! b-flat' >]
	< e-flat b-flat' >[ g, b-flat < g' e-flat' >] < g e-flat' >[ b-flat, b-flat < g' e-flat' >]
	< g e'! >8 r r4
	r4 r8 < g,, e'! >16\ff[ < c' g' >]
	< c g' >[ < g, e' > < g g' > < e'' c' >] < e c' >[ < g,, g' >] r8
	r4 r8 < g e'! >16[ < c' g' >]
	< c g' >[ < g, e' > < g g' > < e'' c' >] < e c' >[ < g,, g' >] r8
	
	R1*2/4*3
	
	r8 a16[_\markup { \dynamic p \italic cresc. } b] c[_\cr a c d]
	e-flat[ c a' b] c[ a c d]
	e-flat[ c a' b] c[ a c d]
	e-flat[\< a,, c a'] c-1[ d e-flat-1 g-sharp]\!
	\stemDown a8\f[ \stemNeutral \stemUp a,,,16\p( b]) \stemNeutral c[_\cr a c d]
	e-flat[ c a' b] c[ a c d]
	e-flat[ c a' b] c[ a c d]
	e-flat[\< a,, c a'] c[ d e-flat g-sharp]\!
	a8\f \noDynamic a,,,16\p[(_\markup { \dynamic p \italic cresc. } b]) c[ a c d-sharp]
	e[\< a c e] a[ c e-1 g-sharp]\!
	\stemDown a8\f[ \stemNeutral \stemUp \noDynamic a,,,16\p(_\markup { \dynamic p \italic cresc. }
		b]) \stemNeutral c[_\cr a c e]
	f[\< a c f] a[ c f g-sharp]\!
	a\ff[ f-sharp! g! a] c,[ d e a,] b[ c f-sharp, g] a[ c, d e]
	a,[ b c f-sharp,] g[ a c, d]
	e[ a, b c] d[ c b a]
	
	%%% POCO MENO MOSSO %%%
	
	g8 r r4
	
	R1*2/4*2
	
	r4 g'8-.\mf[( d-.])
	f-sharp4( e8[ d--])
	c!8[ \tuplet 3/2 { c16(\( d c]\) } b8[ a-.])
	g2~\(
	g4\glissando( g'8-0)[ d-.]\)
	f-sharp4( e8[ d--])
	c!8[ \tuplet 3/2 { c16(\( d c]\) } b8[ a-.])
	g2~\(
	g4\glissando( e'8)[ e-.]\)
	e4( d8[ c])
	b-.[( a\glissando]\( e'\)[ e-.])
	e4( d8[ c])
	b4\glissando( g'8[ d-.])
	e4( d8[ c])
	b8-.[( a\glissando]\( e'\)[ e-.])
	e4( d8[ c])
	b16[( d) g-. d'-.] < c! e >-.[ d,-. < c' e >-. d,-.]
	< c' e >[ d,-. d-. < c' e >-.] < b d >-.[ d,-. < a' c >-. d,-.]
	< g b >[ d < f-sharp a > d] < b' e >[ d, < b' e > d,]
	< b' e >[ d, d < b' e >] < b d >[ d, < a' c > d,]
	< g b >[ d d < g b >] < c a' >[ d, d' d,]
	< c' e >[ d, d < c' e >] < b d >[ d, < a' c > d,]
	< g b >[ d < f-sharp a > d] < b' e >[ d, < b' e > d,]
	< b' e >[ d, d < b' e >] < b d >[ d, < a' c > d,]
	< g b >[\< g, b d]\! < e e' >8\downbow\f[ < e e' >\downbow]
	< e e' >4\downbow < d d' >8\downbow[ < c c' >\downbow]
	< b b' >\downbow[ < a a' >\downbow\glissando]( < e' e' >)[ < e e' >\downbow]
	< e e' >4\downbow < d d' >8\downbow[ < c c' >\downbow]
	< b b' >4\glissando( < g' g' >8)[ < d d' >\upbow]
	< e e' >4\downbow < d d' >8\downbow[ < c c' >\downbow]
	< b b' >\downbow[ < a a' >\downbow\glissando]( < e' e' >)[ < e e' >\downbow]
	< e e' >4 < d d' >8[ < c c' >]
	< b b' >4 g'16[ f-sharp g g-sharp]
	a[ g-sharp a b] a[ g f-sharp e]
	d[ e f-sharp g] a[ b c e]
	g[ d e f-sharp] g[ d e f-sharp]
	g[ d g a] b[ c b b-flat]
	a[ g-sharp a b!] a[ g-sharp f-sharp e]
	d[ e f-sharp g] a[ b c e]
	g[ d e f-sharp] g[ d e f-sharp]
	g[ \ottava #1 a b d] e8-0[ e-0]
	e4-0 \ottava #0
	< d,, g\harmonic >8-.[( < c f-sharp\harmonic >-.])
	< b e\harmonic >[ < a d\harmonic >\glissando](\( < e' a\harmonic >)[ < e a\harmonic >]\)
	< e a\harmonic >4 < d g\harmonic >8-.[( < c f-sharp\harmonic >-.])
	< b e\harmonic >4\glissando( < g' c\harmonic >8)[ < d g\harmonic >]
	< e a\harmonic >4 < d g\harmonic >8-.[( < c f-sharp\harmonic >-.])
	< b f-sharp'\harmonic >[ < a d\harmonic >\glissando](\( < e' a\harmonic >)[ < e a\harmonic >]\)
	< e a\harmonic >4 < d g\harmonic >8-.[( < c f-sharp\harmonic >-.])
	
	%%% MOLTO MENO MOSSO %%%
	
	< b e\harmonic > r8 r4
	
	R1*2/4*15
	
	r4 f-sharp8\mf[( g])
	a4( g8[ f-sharp])
	\grace { e16[( f-sharp] } e8[ d-sharp]) a--[ b--]
	c4\glissando( b'8[ a])
	\grace { b,16[( c] } b8[ a]) a--[ b--]
	c4\glissando( b'8[ a])
	\grace { b,16[( c] } b8[ a]) a--[ b--]
	c4\glissando( b'8[ a])
	\grace { b,16[( c] } b16[ a) d-. e-.] f-sharp8[ g]
	a4( g8[ f-sharp])
	\grace { e16[( f-sharp] } e8[ d-sharp]) a--[ b--]
	c4\glissando( b'8[ a])
	\grace { b,16[( c] } b8[ a]) a--[ b--]
	c4\glissando( b'8[ a])
	\grace { b,16[( c] } b8[ a]) a--[ b--]
	c4\glissando( b'8[ a])
	\grace { g16[( a] } g8[ f-sharp])\< d'-.[ c-.]
	\grace { b16[( c] } b8[ a]) f-sharp'--[ e--]
	\grace { e16[^( f-sharp] } e8[ d-sharp]^) g-.[ f-sharp-.]
	\grace { f-sharp16[^( g] } f-sharp8[ e^) e'-- d--]\!
	\grace { d16[^( e] } d8[ c-sharp]^) e--[ g,--]
	b-flat4( a8[ g])
	\grace { g16[^( a] } g8[\> f^) a-- d,--]
	f4( e8[ d])\!
	\grace { d16[ e] } d8\p[( c-sharp) e-- g,--]
	b-flat4( a8[ g])
	\grace { g16[( a] } g8[ f) a-- d,--]
	f4(^\> e8[ d])^\!
	\grace { d16[( e] } d8[ c-sharp) e-- a,--]
	b-flat2\pp(
	a8)[ c-sharp( e a,])
	b-flat2(
	a8)[ c-sharp( e g-sharp,])
	a[( c-sharp) e( g-sharp,])
	\tuplet 3/2 { a-.[_\cr c-sharp-. e-.] } \tuplet 3/2 { g-sharp,-.[ a-. c-sharp-.] }
	\tuplet 3/2 { e-.[ g-sharp,-. a-.] } \tuplet 3/2 { c-sharp-.[ e-. g-sharp,-.] }
	a16-.[ c-sharp-. e-. g-sharp,-.] a[\< c-sharp e g-sharp,]
	a[ c-sharp e g-sharp,] a[ c-sharp e g-sharp,]
	a[ c-sharp e g-sharp,] a[ c-sharp e g-sharp,]
	a[ c-sharp e g-sharp,] a[ c-sharp e g-sharp,]\!
	a\ff[\> c-sharp e g-sharp,] a[ c-sharp e g-sharp,]
	a[ c-sharp e g-sharp,] a[ c-sharp e g-sharp,]
	a[ c-sharp e g-sharp,] a[ c-sharp e g-sharp,]\!
	a[ g-sharp a a-sharp] b[ a-sharp b c-sharp]
	
	%%% TEMPO 1 %%%

	d8-.\p[ d16( c-sharp] d8)[ b-.]						|
	c-sharp[ e] a,[ c-sharp16( d])
	e16[\< c-sharp e f-sharp] g[ e a b]
	c-sharp[ a b c-sharp] d[ e f-sharp a]\!
	b8\f[ b16( a-sharp] b8)[ f-sharp-.]
	g-.[ g16( f-sharp] g8)[_\markup { \italic dim. } d-sharp]
	e[ b] c-sharp16[\> g-sharp a a-sharp]\!
	b[\> d-sharp, e f-sharp]\! g[ a, b c-sharp]
	d!8-.\p[ d16( c-sharp] d8)[ b-.]
	c-sharp[ e] a,[ c-sharp16( d])
	e16[\< c-sharp e f-sharp] g[ e a b]
	c-sharp[ a b c-sharp] d[ e f-sharp a]\!
	b-flat8\f[ b-flat16( a] b-flat8)[ d,,-.\p]
	c-sharp[ e] a,[ c-sharp16^1( d])
	e[\< c-sharp d-sharp e] f-sharp[ d-sharp g-sharp a]
	b[ g-sharp a b] c-sharp[ d e a]\!
	f8\f[ f16( e] f8)[ d,]								|
	a'8[_\markup { \italic dim. } a16( g-sharp] a8)[ a,]
	b-flat16\p[\< b c-sharp d] c-sharp[ d e f]
	f-sharpsharp[ g-sharp a-sharp b] c-sharp[ d e a!]\!
	f8-.\f[ f16( e] f8)[ d,]
	a'8-.[_\markup { \italic dim. } a16( g-sharp] a8)[ a,]
	b-flat16\p[ b c-sharp d] c-sharp[ d e f]
	f-sharpsharp,[\< g-sharp a-sharp b] b-sharp[ c-sharp d-sharp e]\!
	f'8\f[ f16(\> e] f8)[ d,]
	a'8[ a16( g-sharp] a8)[ a,]\!
	b-flat16-.\p[\< b-. c-sharp-. d-.] c-sharp[ d e f]
	f-sharpsharp[ g-sharp a-sharp b] c-sharp[ d e a!]\!
	f8\mf[ f16( e] f8)[ d,]
	a'8[ a16( g-sharp] a8)[ a,]							|
	f-sharp''!8[ f-sharp16( e-sharp] f-sharp8)[ c-sharp,]
	d'8[ d16( c-sharp] d8)[ d,-.]
	g'8[_\cr g16( f-sharp] g8)[ g,]
	a'8[ a, b-flat' b-flat,]
	b'!8[ b16( a-sharp] b8)[ b,!-.]
	c'8[\< c, d' d,]\!
	d'8\f[ d16( c-sharp]) d[ g-sharp, e d]
	c-sharp16[ b-sharp c-sharp d] c-sharp[ e a c-sharp]
	d8[ d16( c-sharp] d)[ g-sharp, e d]
	c-sharp[ b-sharp c-sharp d] c-sharp[ e a c-sharp]
	d8-.[ d16( c-sharp] d8)[ d,-.]
	f'8-.[ f16( e] f8)[ f,-.]
	f-sharp'!-.[\< f-sharp,!-. g'-. g,-.]
	g-sharp'-.[ g-sharp,-. a'-. a,-.\f]\!
	d16[( c-sharp d8]) a16[( g-sharp a8])					|
	d,16[( c-sharp d8]) a16[( g-sharp a8])
	d,16[( c-sharp d8]) a16[(\< g-sharp a8])
	b-flat16[ b-flat b b] c[ c c-sharp c-sharp]\!
	d8\f[ d16\p( c-sharp] d8)[ b]
	c-sharp[ e] a,[ c-sharp16( d])
	e[ c-sharp e f-sharp] g[ e a b]
	c-sharp[\< a b c-sharp] d[ e f-sharp a]\!
	b8\f[ b16( a-sharp] b8)[ f-sharp-.]
	g8-.[ g16( f-sharp] g8)[ d-sharp-.]
	e[ b] c-sharp16-.[\< g-sharp-. a-. a-sharp-.]
	b[ e-sharp, f-sharp g-sharp] a-sharp[ a-sharp b c-sharp]\!
	< b, f-sharp' d' >8\f[ d'16(\( c-sharp] d8)[ b-.]\)
	< a, e' c-sharp' >[ e''] < a,, e' a >[ c-sharp'16 d]
	e[ c-sharp e f-sharp] g[\< e a! b]
	c-sharp[ a b c-sharp]\! d[ e f-sharp g]
	< d,, a' d' >8[ d''16(\( c-sharp] d8)[ b-.]\)		|
	< a, c-sharp' >[ e''] < a,, a' >16[ g-sharp' a b]
	c-sharp[ b c-sharp d] e[ f-sharp g g-sharp]
	\ottava #1 a[ a-sharp b c-sharp] d8\f \ottava #0 r
	d,8\f[ d16(\( c-sharp] d8)[ b-.]\)
	g16[ f-sharp e g] d[ c-sharp b d]
	g,[ f-sharp e g] d[ c-sharp b d]
	g,[ b e g] b[ e g b]
	d8[ d16(\( c-sharp] d8)[ b-.]\)
	g16[ f-sharp e g] d[ c-sharp b d]
	g,[ f-sharp e g] d[ c-sharp b d]
	g,[ b e g] b[ e g b]
	d8-.[ d16( c-sharp] d8)[ < d,, b' >-.]				|
	R1*2/4
	d''8-.[ d16( c-sharp] d8)[ < d,, b' >-.]
	R1*2/4
	d''8-.[ d16( c-sharp] d8)[ < d,, b' >-.]
	d''8-.[ d16( c-sharp] d8)[ < d,, b' >-.]
	d''8[ < d,, b' >-.] d''8[ < d,, b' >-.]
	d''8[ < d,, b' >-.] d''8[ < d,, b' >-.]
	d'' r r4
	
	R1*2/4*24
	
	r4 r8 a,,16\ff[ < f-sharp' d' >]
	< f-sharp d' >[ a, d < a' f-sharp' >] < a f-sharp' >[ d, f-sharp < d' a' >]
	< d a' >[ f-sharp, a < f-sharp' d' >] < f-sharp d' >[ a, a < f-sharp' d' >]
	< f-sharp d' >8 r r4
	r4 r8 b,,16[ < f-sharp' d' >]
	< f-sharp d' >[ b, d < b' f-sharp' >] < b f-sharp' >[ d, f-sharp < d' b' >]
	< d b' >[ f-sharp, b < f-sharp' d' >] < f-sharp d' >[ b, b < f-sharp' d' >]
	< d d' >8 r r4
	r4 r8 b,16[ < g' d' >]
	< g d' >[ b, d < b' g' >] < b g' >[ d, g < d' b' >]
	< d b' >[ g, b < g' d' >] < g d' >[ b, b < g' d' >]
	< g e' >8 r r4
	r4 r8 b,,16[ < g' e' >]
	< g e' >[ b, e < b' g' >] < b g' >[ e, g < e' b' >]
	< e b' >[ g, b < g' e' >] < g e' >[ b, b < g' e' >]
	< g e' >8 r r4
	r4 r8 b,,16[ < g' e' >]
	< g e' >[ b, e < b' g' >] < b g' >[ e, g < e' b' >]
	< e b' >[ g, b < g' e' >] < g e' >[ b, b < g' e' >]
	< g e' >8 r r4
	< g,, e' c' a-sharp' >8[ a-sharp''16( a] a-sharp8)[ e]
	R1*2/4
	< g,, e' c' a-sharp' >8-.[ a-sharp''16( a] a-sharp8)[ e-.]
	r4 < g,, e' c' a-sharp' >8[ g]
	r4 < g e' c' a-sharp' >8[ g]
	r4 < g d' b-flat' e >8[ g]
	r4 < c-sharp! g' a e' >8[ a']
	r4 < d, a' f-sharp' >8[ d]
	r4 < g, d' b' g' >8[ d']
	r4 d16\p[ c-sharp d f]
	f[_\cr e f g-sharp] g-sharp[ g g-sharp d']
	d[ c-sharp d f] f[ e f g-sharp]
	g-sharp[ g g-sharp d'] d[ e f g-sharp]
	a8:16\f[ f-sharp!8:] d:[ a-sharp:]
	b:[ f-sharp:] g:[ d-sharp:]
	e:[ b:] c-sharp:[ e:]
	a:[ a-sharp: b: c-sharp:]
	d16[ d,, c-sharp d] e[ f-sharp g a]
	b-flat[ e g, a] b-flat[ e d-sharp e]
	f-sharp[ g c-sharp, d!] e[ f-sharp g g-sharp]
	a[ b c-sharp d] e[ f-sharp g a]
	d,16[ d,, c-sharp d] e[ f-sharp g a]
	b-flat[ e g, a] b-flat[ e d-sharp e]
	f-sharp[ g c-sharp, d!] e[ f-sharp g g-sharp]
	a[ b c-sharp d] e[ f-sharp g a]
	d,[ d e f-sharp] a-sharp,[ a-sharp b c-sharp]
	b[ b c-sharp d] f-sharp,[ f-sharp g a]
	e[ e f-sharp g] < g,, d' >[ < b-flat' e > < b-flat e > < g, d' >]
	< b-flat g' >[ < d' e > < d e > < b-flat, g' >] a'[ a' b! c-sharp]
	d[ d e f-sharp] a-sharp,[ a-sharp b c-sharp]
	b[ b c-sharp d] f-sharp,[ f-sharp g a]
	e[ e f-sharp g] < g,, d' >[ < b-flat' e > < b-flat e > < g, d' >]
	< b-flat g' >[ < d' e > < d e > < b-flat, g' >] a'[ a' b! c-sharp]
	d[ d,, f-sharp g] a[ a b c-sharp]
	d[ e f-sharp g] a[ a b c-sharp]
	d[ e, f-sharp g] a[ a b c-sharp]
	
	\ottava #1
	d[ e f-sharp g] a[ a b c-sharp]
	d[ d d d] < d, d' >[ < d d' > < d d' > < d d' >]
	< d d' >2:16
	< d d' >:
	< d d' >:
	< d d' >:
	< d d' >:
	< d d' >16[ d' c-sharp b] a[ g f-sharp e]
	
	\ottava #0
	d[ a b c-sharp] d[ a b c-sharp]
	d[ c-sharp b a] g-sharp[ f-sharp e d]
	c-sharp[ b a g!] f-sharp[ e d c-sharp]
	d[ a b c-sharp] d[ f-sharp a c-sharp]
	d[ a b c-sharp] d[ f-sharp a c-sharp]
	d[ a, b c-sharp] d[ f-sharp a c-sharp]
	d[ a b c-sharp] d[ e f-sharp a]
	\ottava #1 d8 \ottava #0 r r4 
	R1*2/4
	r8 e,->[ a->] r
	< a,,, f-sharp' d' > r r4\fermata
}
