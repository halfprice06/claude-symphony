\version "2.20.0"

\include "cadenza.ily"


theSolo = \relative d' {
	\clef "treble"
	\key d \major
	
	r1
	
	R1*21
	
	%%% SOLO %%%
	
	r8 a8\p( b-flat4~ b-flat8)[ a( c-sharp e])												|
	\tuplet 3/2 { g8[(\< a c-sharp] } e16[ g a c-sharp]\! e8)[_\cr d( c-sharp b-flat])		|
	a8\f[ g-sharp(_\markup { \italic rit. } a a-sharp])
		b4^\markup { \italic ritenuto }_\markup { \italic dim. }
		\grace { a16[ b] } a8(\> g-sharp												|
	c-sharp,4) d8( d-sharp f-sharp4) \grace { e16[ f-sharp] } e8( c-sharp\!				|
	a8)[ g-sharp( a a-sharp]\> b) a4\fermata g8\!
	
	%%% TUTTI %%%
	
	\set Score.tempoHideNote = ##f
	\appoggiatura a,8 \tempo "Moderato assai." 4 = 80
		f-sharp'8 r\p f-sharp2 e16[( d f-sharp a]) e4.( f-sharp8) e4 f-sharp					|															|
	\set Score.tempoHideNote = ##t
	\appoggiatura b,8 g'8 r g4~( g8.[ a16]) b[( c-sharp d e])							|
	a,4. \tuplet 3/2 { b16[( d b] } a8)[^\markup { \italic dolce } b( c-sharp d])			|
	e8( g a,4)~ a8[ b( c-sharp d])														|
	e8( g a,4)~ \tuplet 3/2 { a8[( g-sharp a]) } \tuplet 3/2 { a-sharp[( g-sharpsharp a-sharp]) } |
	\tuplet 3/2 { b8[( d f-sharp)] } g-sharp,4~ g-sharp16[ d-sharp( e f-sharp]
		g-sharp[ a b e])																	|
	e4~(\< e16[ e-sharp f-sharp g-sharp])\! a8\mf[( b16.-.) b32]( c-sharp,4~				|
	c-sharp8[ e16-.) r32 e]( g,4~ g8[ b16-.) r32 b]( c-sharp,8[ g'16-.) r32 g](			|
	b,8[\cresc e16-.) r32 e](
		b-flat8[ c-sharp16-.) r32 c-sharp32]( a8[ b-flat16-.) r32 b-flat-.](\<
		g-sharp8[ b-flat16-.) r32 b-flat](\!												|
	a8[ b-flat16-.) r32 b-flat32]( g-sharp8[ b-flat16-.) r32 b-flat]( a8[ b-flat16-.)
		r32 b-flat32]( g-sharp8[\> b-flat16-.) r32 b-flat](									|
	g-sharp8[ a16-.) r32 b-flat]( g-sharp8[ a16-.)\! r32 b-flat\p](
		\tuplet 3/2 { g-sharp16[ a b-flat } \tuplet 3/2 { g-sharp16 a b-flat }
		\tuplet 3/2 { g-sharp16 a b-flat } \tuplet 3/2 { g-sharp16 a b-flat]) }							|
	\tuplet 3/2 { g-sharp16[(\< a b-flat } \tuplet 3/2 { b16 b-sharp c-sharp] }
		\tuplet 3/2 { d16[ d-sharp e } \tuplet 3/2 { e-sharp16 f-sharp g] }
		\tuplet 3/2 { g-sharp16[ a b-flat } \tuplet 3/2 { b16 c c-sharp]\! } d16[ d-sharp e e-sharp]) |
	< d, a' f-sharp' >8 r < d a' f-sharp' >2\downbow \grace { e'16[ f-sharp] } e16[( d f-sharp a])
	\appoggiatura a,8 < c-sharp e >4.( < d f-sharp >8) \tuplet 3/2 { < c-sharp e >(
		< b-sharp d-sharp > < c-sharp e >) }
		<< { \tuplet 3/2 { f-sharp8( e f-sharp) } } \\ { < d,! c' >8 r } >>
	< d b' g' >8 r < d b' g' >4\downbow(\( < b' g' >8.[\) a'16]) b16[( c-sharp d e)]
	a,4.( \tuplet 3/2 { b16[ d b] } a8)[ b( c-sharp d)]
	e8( g a,4~ a8)[_\cr b( c-sharp d])
	e8( g a,4~\< a16[ a-sharp) b--( c-sharp--] d--[ e-- f-- f-sharp--])\!
	g-sharp8\f[( a16-.) r32 a]( a,8[ f-sharp'16-.) r32 f-sharp]( g-sharp,8[ c-sharp16-.) r32 c-sharp](
		d,8[ b'16-.) r32 b](
	c-sharp,8[ a'16-.) r32 a]( a,8[ e'16-.)_\markup { \italic dim. } r32 e](
		f-sharp,8[ c-sharp'16-.) r32 c-sharp]( e,8[ a16-.) r32 a](
	c-sharp,8[\tempo "Ben sostenuto il tempo." f-sharp16-.) r32 f-sharp]( e8[ f-sharp16-.) r32 f-sharp]( c-sharp8[ f-sharp16-.) r32 f-sharp](
		e8[ f-sharp16-.) r32 f-sharp](
	e8[ g16-.) r32 g]( c-sharp,8[ e16-.) r32 e]( b8[ e16-.) r32 e](
		c-sharp8[ a'16-.) r32 a](
	\tuplet 3/2 { d,16[ f-sharp a] } \tuplet 3/2 { b8[ c-sharp16]) } \tuplet 3/2 { f-sharp,16[( a b] }
		\tuplet 3/2 { c-sharp8[ d16]) } \tuplet 3/2 { a16[( d e] } \tuplet 3/2 { e-sharp8[ f-sharp16]) }
		\tuplet 3/2 { b16[( a f-sharp] } \tuplet 3/2 { d[ a f-sharp]) }
	e8\f[( g16-.) r32 g]( c-sharp,8[ e16-.) r32 e]( b8[ e16-.) r32 e](
		c-sharp8[ a'16-.) r32 a](
	\tuplet 3/2 { d,16[ f-sharp a] } \tuplet 3/2 { b8[ c-sharp16]) } \tuplet 3/2 { f-sharp,16[( a b] }
		\tuplet 3/2 { c-sharp8[ d16]) } \tuplet 3/2 { a16[( d e] } \tuplet 3/2 { e-sharp8[ f-sharp16]) }
		\tuplet 3/2 { b16[( a f-sharp] } \tuplet 3/2 { d[ a f-sharp]) }
	f-sharp8\f[( g16-.) r32 g]( f-sharp8[ g-sharp16-.) r32 g-sharp](
		\tuplet 3/2 { f-sharp16[ a-sharp16 c-sharp] } \tuplet 3/2 { e16[ e-sharp f-sharp]) }
		\tuplet 3/2 { a-sharp,!16[( b d] } \tuplet 3/2 { f-sharp16[ a-sharp b]) }
	b,8[( c16-.) r32 c]( b8[ c-sharp16-.) r32 c-sharp]( \tuplet 3/2 { b16[ d-sharp f-sharp }
		\tuplet 3/2 { a! a-sharp b]) } \tuplet 3/2 { d-sharp,![( e g } \tuplet 3/2 { b d-sharp e]) }
	\tuplet 3/2 { e,[( f-sharpsharp g-sharp } \tuplet 3/2 { b d-sharp e]) }
		\tuplet 3/2 { e,[( g-sharp a } \tuplet 3/2 { c d-sharp e]) }
		\tuplet 3/2 { g-sharp,[( b d-sharp } \tuplet 3/2 { e f-sharpsharp g-sharp]) }
		\tuplet 3/2 { a,[( c! d-sharp } \tuplet 3/2 { e g-sharp a]) }
	\tuplet 3/2 { \noDynamic b-flat-.\ff[ d,( e-flat } \tuplet 3/2 { f) b-flat,( c-sharp!] }
		\tuplet 3/2 { d)[ f,( a } \tuplet 3/2 { b-flat!) d,( e-flat] }
		\tuplet 3/2 { f!)[ b-flat,( c-sharp! } \tuplet 3/2 { d) f,( a] }
		\tuplet 3/2 { b-flat!)[ b-flat,( c-sharp! } \tuplet 3/2 { d) f( b-flat] }
	\tuplet 3/2 { b!)[ f( g } \tuplet 3/2 { a-flat) a-flat( b] } \tuplet 3/2 { f')[ f( g }
		\tuplet 3/2 { a-flat) a-flat( b!] } \tuplet 3/2 { f')[ a-flat,( b } \tuplet 3/2 { f') b,( f'] }
		\tuplet 3/2 { a-flat)[ f( a-flat } \tuplet 3/2 { b!) a-flat( b] }
	c8) r r4 c,,,32[( e f-sharp! g a! b-flat b c] d-sharp[ e f-sharp! g g-sharp a b-flat b])
	c8 r r4 c,,32[( e f-sharp! g a! b-flat b c] d-sharp[ e f-sharp! g g-sharp a b-flat b])
	c8 r8 d,,32[( f-sharp a d) d( f-sharp a d]) d8 r e,,32[( g-sharp d' e) e( g-sharp d' e])
	e8 r d,32[( f g-sharp b) b( d f g-sharp]) g-sharp8 r c,,32[( d d-sharp a') a( b c d-sharp])
	e16_>-.\ff[ a,,_>-. f-sharp''_>-. a,,32-. f-sharp''-.] e16_>-.[ a,,_>-. f-sharp''_>-. a,,32-. f-sharp''-.]
		e32[( b a e]) e32[( b e, f-sharp] g-sharp[ a b d-sharp] e[ f-sharp g-sharp b])
	e16_>-.[ a,,_>-. f-sharp''_>-. a,,32-. f-sharp''-.] e16_>-.[ a,,_>-. f-sharp''_>-. a,,32-. f-sharp''-.]
		e32[( b a e]) e32[( b e, f-sharp] g-sharp[ a b d-sharp] e[_\cr f-sharp g-sharp a])
	b32[( g-sharp e b]) g-sharp[(\< b c-sharp d-sharp] e[ d-sharp e f-sharp] g-sharp[ a b c-sharp]) d![( b g-sharp e]
		b[ d-sharp! e f-sharp] g-sharp[ f-sharp g-sharp a] b[ c-sharp d! e])\!
	f-sharp32[( e d c-sharp]) b[( d b a]) g-sharp[( b g-sharp f-sharp]) e[( f-sharp d c-sharp]) b[( d b a)
		g-sharp( b g-sharp f-sharp]) e[( f-sharp d c-sharp) b( d b a]
	g-sharp16)[ a8 g-sharp16]~ g-sharp[ f-sharpsharp8 g-sharp16]~( g-sharp[ a a-sharp) b-.] c-.[ c-sharp-. d-. d-sharp-.]
	e8_\markup { \italic dim. } f4 e8~\> e f4(\! f-sharp8\p)
	a4(_\markup { \italic {con molto espr.} } g-sharp) b16[( a g-sharp b] a4)
	b4( a-sharp4) c-sharp16[( b a-sharp c-sharp] b4)
	\tuplet 3/2 { c-sharp8[(\< d e] } \tuplet 3/2 { f-sharp[ g! f-sharp])\! } f-sharp8(\> b4 f-sharp8)\!
	
	\override TupletBracket.transparent = ##t
	\grace { e16[ f-sharp] } \tuplet 3/2 { e8[(\< d-sharp-. e-.] } \tuplet 3/2 { g[-. f-sharp-. e-.])\! }
		f-sharp8(\> b4 f-sharp8)\!
	\grace { f16[ g] } \tuplet 3/2 { f8[( e f] } \tuplet 3/2 { a)[ a,-. b-.] } b-sharp-.[ c-sharp]~
		\tuplet 3/2 { c-sharp[ c-sharp,-.( d-.]) }
	d-sharp8(^\< e~ \tuplet 3/2 { e)[ e-sharp-.( f-sharp-.] } \tuplet 3/2 { f-sharpsharp-.[ g-sharp-. a-.])^\! }
		\tuplet 3/2 { a-sharp[(^\> c-sharp b])^\! }
	a!4( g-sharp) b16[( a g-sharp b] a4)
	b4( a-sharp4) c-sharp16[( b a-sharp c-sharp] b4)
	\tuplet 3/2 { c-sharp8[(_\markup { \italic {poco cresc.}} d e] } \tuplet 3/2 { f-sharp[ g! f-sharp]) } f-sharp8( b4-> f-sharp8)
	\tuplet 3/2 { f[( g-sharp a!] } \tuplet 3/2 { b)[ c-sharp-. b-.] } b-. e4--~ e8--
	\tuplet 3/2 { f-sharp!8\f[ e d] c-sharp[ d e] g![ f-sharp e] d[ c-sharp b] }
	\grace { a16[ b] } \tuplet 3/2 { a8[ g-sharp( a] c)[ a,( b] c-sharp!)[ c-sharp,!( d] e)[\> a8.( a,16)]\! }
	a4( g-sharp) b16[( a g-sharp b] a4)
	b4( a-sharp4) c-sharp16[( b a-sharp c-sharp] b4)
	\tuplet 3/2 { c-sharp8[( d e] f-sharp)[ g8.( f-sharp16]) } f-sharp8 b4(_> f-sharp8)
	\tuplet 3/2 { b8[( c-sharp d]) d[( e f-sharp]) f-sharp-.[ d,-. f-sharp'->]~( f-sharp[ e d]) }
	\tuplet 3/2 { c-sharp[( d e]) e[( f-sharp g]) g-.[ e,-. g'->]~( g[_\markup { "" \raise #-2.5 \italic {poco a poco cresc.} } f-sharp e]) }
	\tuplet 3/2 { g-sharp-.[ f,-. g-sharp'-.]~( g-sharp[ g f]) a-.[ f-sharp, a'](~ a[ g-sharp f-sharp]) }
	\tuplet 3/2 { b-flat[( a g!]) b[( a-sharp g-sharp]) c-sharp[( b a-sharp]) d[( c-sharp b]) }
	\tuplet 3/2 { e8[(\< d-sharp c-sharp]) e[( d-sharp c-sharp]) e16[( d-sharp c-sharp) e( d-sharp c-sharp) e( d-sharp c-sharp) b-sharp( c-sharp e)]\! }
	f4\f( e) g16[( f e g] \tuplet 3/2 { f-sharp8)[ a-flat( g] }
	\tuplet 3/2 { e-flat)[ g( f] } \tuplet 3/2 { d)[ f( e-flat] } \tuplet 3/2 { c)[ e( d] } \tuplet 3/2 { b-flat)[ d( c]) }
	f4( e!) g16[( f e g] f)[ f( a-flat g]
	e-flat)[ e-flat( g f] d)[ d( f e-flat] c)[ c( e-flat d] b-flat)[ b-flat( d c])
	b-flat4( a) c16[( b-flat a c] b-flat)[ b-flat( d b-flat])
	a4( g-sharp) b!16[( a g-sharp b] a)[ a( c-sharp! a])
	g-sharp4 f-sharp16[( g-sharp a f-sharp]) f-sharp[( e d-sharp f-sharp] e)[ c-sharp( b-sharp d]
	c-sharp)[ a( g-sharp b] a)[ e( d-sharp f-sharp] e)[ c-sharp( b-sharp d] c-sharp)[ a( g-sharp b]
	
	\override TupletBracket.transparent = ##f
	a8->\ff)[\< b32( c-sharp d e] \tuplet 11/8 { f-sharp[ g-sharp a b c-sharp d e f-sharp g-sharp a b])\! }
		\tuplet 3/2 { c-sharp8->[ d-> e->] } r4
	a,,,8->[ b32( c-sharp d e] \tuplet 11/8 { f-sharp[ g-sharp a b c-sharp d e f-sharp g-sharp a b]) }
		\tuplet 3/2 { c-sharp8->[ d-> e->] } r4
	\tuplet 5/4 { e,,32[( f-sharp g-sharp a b] } \tuplet 7/4 { c-sharp[ d-sharp e f-sharp g-sharp a b]) }
		\tuplet 3/2 { c-sharp8->[ d-sharp-> e->] } \tuplet 5/4 { e,,32[( f-sharp g-sharp a b] }
		\tuplet 7/4 { c-sharp[ d-sharp e f-sharp g-sharp! a a-sharp] } \tuplet 3/2 { b8->)[ d-sharp!-> e->] }
	\tuplet 5/4 { e,,32[( f-sharp g-sharp a b] } \tuplet 7/4 { c[ d! e f-sharp g-sharp a b]) }
		\tuplet 3/2 { c8->[ d-sharp-> e->] } \tuplet 5/4 { e,,32[( f-sharp! g-sharp! a b] }
		\tuplet 7/4 { c![ d e f g a b] } \tuplet 3/2 { c!8->)[ d-sharp!-> e->] }
	\stemDown f16:32[^\fff \stemNeutral c,,: d!: e:] f:[ g: a: c:] b:[ f-sharp: b: f-sharp':] b:[ c-sharp!: d-sharp: f:]
	b:[ e,,: b: g-sharp:] e:[ f-sharp: g-sharp: b:] a:[ e: a: e':] a:[ b: c-sharp: e:]
	a-.[ a,,-. d'-. a,-.] a''-.[ a,,-. c'-. a,-.] a''-.[ d,,,-. d'-. d,-.] f32[( a d f] a[ d f a])
	a16-.[ a,,-. d'-. a,-.] a''-.[ a,,-. c'-. a,-.] a''-.[ d,,,-. d'-. d,-.] f32[( a d f] a[ d f a])
	\tuplet 3/2 { r16 g-sharp,,,( < f' b >) } \tuplet 3/2 { < f b >( g-sharp, < f' b >]) } \tuplet 3/2 { r16 e[( < a e' >) }
		\tuplet 3/2 { < a e' >( e < a e' >]) } \tuplet 3/2 { r16 d,[( < b' e >) } \tuplet 3/2 { < b e >( d, < b' e >]) }
		\tuplet 3/2 { r16 < a, e' >( < c' a' >) } \tuplet 3/2 { < c a' >( < a, e' > < c' a' >]) }
	\tuplet 3/2 { r16 b[( b') } \tuplet 3/2 { b( b, b']) } \tuplet 3/2 { r16 a,[( < e' c-sharp'! >) }
		\tuplet 3/2 { < e c-sharp' >( a, < e' c-sharp' >]) } \tuplet 3/2 { r16 a,[( a') } \tuplet 3/2 { a( a, a']) }
		\tuplet 3/2 { r16 a,[( a'') } \tuplet 3/2 { a( a,, a'']) }
		
	%%% DOUBLE BAR %%%
	
	\tuplet 3/2 { e16-.\p[ c-sharp-. e-. } \tuplet 3/2 { f-sharp-. c-sharp-. f-sharp-.] } \tuplet 3/2 { d-.[ b-. d-. }
		\tuplet 3/2 { g-sharp!-. d-sharp-. g-sharp-.] }
		\override TupletBracket.transparent = ##t
		\tuplet 3/2 { e16-.[ c-sharp-. e-. f-sharp-. c-sharp-. f-sharp-.] } \tuplet 3/2 { d-.[ b-. d-. g-sharp-. d-sharp-. g-sharp-.] }
	\tuplet 3/2 { e-.[ c-sharp-. e-. g!-. e-. g-.] d!-.[ b-. d-. f-sharp-. d-. f-sharp-.] c-sharp-.[ a-. c-sharp-.
		e-. c-sharp-. e-.] a,-.[ f-sharp-. a-. c-sharp-. a-. c-sharp-.] }
	\tuplet 3/2 { b[( g-sharp e]) f-sharp'-.[ c-sharp-. f-sharp-.] d-.[ b-. d-. g-sharp-. d-sharp-. g-sharp-.] }
	\tuplet 3/2 { e-.[ c-sharp-. e-. f-sharp-. c-sharp-. f-sharp-.] d!-.[ b-. d-. g-sharp-. d-sharp-. g-sharp-.]
		e-.[ c-sharp-. e-. g!-. e-. g-.] d!-.[ b-. d-. f-sharp-. d-. f-sharp-.] c-sharp-.[ a-. c-sharp-. e-. c-sharp-. e-.]
		a,-.[ f-sharp-. a-. c-sharp-. a-. c-sharp-.] }
	\tuplet 3/2 { b16[(_\markup { "" \raise #-2.0 { \dynamic pp \italic {poco a poco cresc.}}} g-sharp e]) < a-sharp, f-sharp' >-.[
		c-sharp,-. < a-sharp' f-sharp' >-.] b,-.[ < f-sharp' d' >-. b,-.] < b-sharp' g-sharp' >-.[ d-sharp,-. < b-sharp' g-sharp' >-.]
		c-sharp,-.[ < a' e' >-. c-sharp,-.] < a-sharp' f-sharp' >-.[ c-sharp,-. < a-sharp' f-sharp' >-.]
		b,-.[ < f-sharp' d' >-. b,-.] < b-sharp'! g-sharp'! >-.[ d-sharp,!-. < b-sharp' g-sharp' >-.] }
	\tuplet 3/2 { c-sharp,-.[ < a'! e' >-. c-sharp,-.] < c-sharp' a' >-.[ e,-. < c-sharp' a' >-.] d,![ < a' f-sharp' >-. d,-.]
		< d-sharp' b' >-.[ f-sharp,-. < d-sharp' b' >-.] e,-.[ < b' g-sharp' > e,-.] < c-sharp' a' >-.[ e,-. < c-sharp' a' >-.] d,![ < a' f-sharp' >-. d,-.]
		< d-sharp'! b' >-.[ f-sharp,-. < d-sharp' b' >-.] }
	\tuplet 3/2 {  e,-.[ < b' g-sharp' > e,-.] < e' c-sharp' >-.[ g-sharp,-. < e' c-sharp' >-.] f-sharp,-.[ < c-sharp' a' >-. f-sharp,-.] < f-sharp' d' >-.[
		a,-. < f-sharp' d' >-.] g-sharp,-.[ < e' b' >-. g-sharp,-.] < g-sharp' e' >-.[ b,-. < g-sharp' e' >-.] a,-.[ < e' c-sharp' >-. a,-.]
		< a' f-sharp' >-.[ c-sharp,-. < a' f-sharp' >-.] }
	\tuplet 3/2 { b,-.[ < f-sharp' d' >-. b,-.] < b' g-sharp' >-.[ d,-. < b' g-sharp' >-.] d,-.[_\cr < b' f-sharp' >-. d,-.]
		< b' g-sharp' >-.[ d,-. < b' g-sharp' >-.] a'16[( f-sharp d a f-sharp d]) d[( f-sharp a d f-sharp a]) }
	\tuplet 3/2 { d,,-.[ < b' f-sharp' >-. d,-.] < b' g-sharp' >-.[ d,-. < b' g-sharp' >-.] d,-.[ < b' f-sharp' >-. d,-.]
		< b' g-sharp' >-.[ d,-. < b' g-sharp' >-.] a'[( f d a f d]) d[( f a d f a]) }
	\tuplet 3/2 { f,-.[ < d' a' >-. f,-.] < d' b' >-.[ f,-. < d' b' >-.] f,-.[ < d' a' >-. f,-.]
		< d' b' >-.[ f,-. < d' b' >-.] c'[( a f c a f]) c[( a c f a c]) }
	\tuplet 3/2 { a,-.[ < f' c' >-. a,-.] < f' d' >-.[ a,-. < f' d' >-.] a,-.[ < f' c' >-. a,-.]
		< f' d' >-.[ a,-. < f' d' >-.] e-flat'[( c! a-flat e-flat c a-flat]) a-flat[( c e-flat a-flat c e-flat]) }
	\tuplet 3/2 { c,-.[ < a-flat' e-flat' >-. c,-.] < a-flat' f' >-.[ c,-. < a-flat' f' >-.] c,-.[ < a-flat' e-flat' >-. c,-.]
		< a-flat' f' >-.[ c,-. < a-flat' f' >-.] f-sharp'[( d-sharp b! f-sharp! d-sharp b!]) b[( d-sharp f-sharp b d-sharp f-sharp]) }
	
	%%% DOUBLE BAR %%%
	
	g-sharp4\trill g-sharp4\trill g-sharp4\trill g-sharp4\trill
	a_>\ff^\trillflat a,,_>^\trillflat a'_>^\trillflat a'_>^\trillflat
	a_>^\trillnatural a,,_>^\trillnatural a'_>^\trillnatural a'_>^\trillnatural
	a4_>\trill a,,_>\trill a'_>\trill a'_>\trill
	\tuplet 3/2 { b-sharp,,,16[( f-sharp' a) a( f-sharp b-sharp,]) b-sharp16[(_\cr f-sharp' a) a( f-sharp b-sharp,])
		a[( f-sharp' b-sharp) b-sharp( f-sharp a,]) a[( f-sharp' b-sharp) b-sharp( f-sharp a,]) }
	\tuplet 3/2 { b-sharp16[( a' f-sharp') f-sharp( a, b-sharp,]) b-sharp16[( a' f-sharp') f-sharp( a, b-sharp,])
		f-sharp'[( b-sharp a') a( b-sharp, f-sharp]) f-sharp[( b-sharp a') a( b-sharp, f-sharp]) }
	\tuplet 3/2 { a16[( f-sharp' b-sharp) b-sharp( f-sharp a,]) f-sharp16[( b-sharp a') a( b-sharp, f-sharp])
		a[( f-sharp' b-sharp) b-sharp( f-sharp a,]) b-sharp[( a' f-sharp') f-sharp( a, b-sharp,]) }
	\tuplet 3/2 { r16\ff f-sharp[( a b-sharp) a^( b-sharp] f-sharp'^)[ b-sharp,( f-sharp'] a)[ f-sharp( a] b-sharp)[ a( b-sharp] f-sharp')[ b-sharp,( f-sharp']
		a)[ f-sharp( a] b-sharp)[ a( b-sharp] }
		
	%%% DOUBLE BAR %%%
	
	c-sharp8) r r4 r2
	
	R1*32
	
	b,8\f[ \grace { b16[ c] } b( a-sharp] b8)[ \grace { b16[ c] } b16( a-sharp] b[ g-sharp e d-sharp]) e[( f-sharp g-sharp a])								|
	b8--[ \grace { b16[ c] } b( a-sharp] b8)[ \grace { b16[ c] } b(\> a-sharp] b[ c d c]) b[( a g f])\!
	< c e >16\mf[\tempo "Molto sostenuto il tempo, moderatissimo." g,-. e'-. g-.] < c e >[_( g,) e'-.(_\( g-.]
		a-.[ b-. c-. d-.]_) \grace { e[ f] } e-.[_( c e g]_)_\)
	< b, d! >->[ g, g'-. < a-sharp e' >-.] < b d >[( d, e) f-sharp-.]( g-.[ a-. b-. d-.]) < c-sharp e >->[ a-. b-. c-sharp-.]
	< d f >-.->[ d,-. a'-. d-.] < d f >[( f,) g-.^\( a-.] b-.[ c-sharp-. d-. e-.] \grace { f[ g] } f[( d f a])^\)
	< c-sharp,! e >->[ a, a' < d f >] < c-sharp e >->[( e, f-sharp g-sharp]) a-.[( b-. c-sharp-. d-.]) < c-sharp e >-.[ d-. c-sharp-. e-.]
	a->-.[ < f, a >-. < f a >-. b'-.->] c->[( a,) b'-.-> a-.->] g-.[ < g,, e' c' >-. b''-. < g,, e' c' >-.] c''-.[ < g,, e' c' >-. a''-.( g-.)]			|
	< a, f' >-.[ < d, a' >-. < d a' >-. g-sharp'-.] a[( a,) g'-. f-.] e-.[ < a,, e' a >-. g-sharp''-. < a,, e' a >-.]
		a''-.[ < a,, e' a >-. f''-.( e-.])
	d32[( e f e d c b a]) b[( c d c b a g! f]) e16:32[ e': g-sharp,: b:] e:[ g-sharp: b: e:]
	d,32[( e f e d c b a]) b[( c d c b a g! f]) e16:32[\> e': b: g-sharp:] e:[ f: g-sharp: b:]\!
	< c e >16[ g,-. e'-. g-.] < c e >[( g,) e'-.( g-.] a-.[ b-. c-. d-.]) \grace { e[ f] } e-.[( c e g])
	< b, d! >16->[ g, g'-. < a-sharp e' >-.] < b d >[( d, e) f-sharp-.]( g-.[ a-. b-. d-.]) < c-sharp e >->[ a-. b-. c-sharp-.]
	< d f >-.->[ d,-. a'-. d-.] < d f >[( f,) g-.^\( a-.] b-.[ c-sharp-. d-. e-.] \grace { f[ g] } f[( d f a])^\)
	< c-sharp, e >->[ a, a' < d f >] < c-sharp e >->[( e, f-sharp g-sharp]) a-.[( b-. c-sharp-. d-.]) < c-sharp e >-.[ d-. c-sharp-. e-.]
	a->-.[ < f, a >-. < f a >-. b'-.->] c->[( a,) b'-.-> a-.->] g-.[ < g,, e' c' >-. b''-. < g,, e' c' >-.] c''-.[ < g,, e' c' >-. a''-.( g-.)]			|
	< a, f' >-.[ < d, a' >-. < d a' >-. g-sharp'-.] a[( a,) g'-. f-.] e-.[ < a,, e' a >-. g-sharp''-. < a,, e' a >-.]
		a''-.[ < a,, e' a >-. f''-.( e-.])
	d-sharp-.[ f-sharp,!-. < d-sharp' b' >-. f-sharp,-.] < d-sharp' c' >-.[ f-sharp,-. < f-sharp d' >-. b,-.] < f-sharp' d-sharp' >-.[ b,-.
		< f-sharp' a >( < g b >] < a c >)[ b,-. < c-sharp! e >( < d-sharp f-sharp >]																		|
	< e g >)[ g,-. < e' a-sharp >( < f-sharp a-sharp >] < g a-sharp >)[ g,-. < a-sharp' e' >( < b e >] < c-sharp e >)[ e,-.
		< c-sharp' a-sharp' >-. e,-.] < e' c-sharp' >-.[ g,-. < g' e' >-. a-sharp,!-.]
	< f-sharp' d-sharp' >-.[ b,-. < d-sharp b' >-. f-sharp,-.] < d-sharp' c' >-.[ f-sharp,-. < f-sharp d' >-. b,-.] < f-sharp' d-sharp' >-.[
		b,-. < f-sharp' a >( < g b >] < a c >)[ b,-. < c-sharp e >( < d-sharp f-sharp >]
	< e g >)[ g,-. < e' a-sharp >(< f-sharp a-sharp >] < g a-sharp >)[ g,-. < a-sharp' e' >( < b e >] < c-sharp e >)[ e,-. < c-sharp' a-sharp' >-. e,-.]
		< e' c-sharp' >-.[ g,-. < g' e' >-. b,-.]
	< g' e' >-.[ a,!-. < c-sharp a' >-. e,-.] < c-sharp' b-flat' >-.[ e,-. < e c' >-. a,-.] < e' c-sharp' >-.[ a,-. < e' g >( < f a >])
		< g b-flat >-.[ a,-. < b! d >-.( < c-sharp e >]																				|
	< d f >)[ a-.< d a' >( < e a >] < f! a >)[ d-. d'( < d e >] < d f >)[ d,-. < d' a' >-. d,-.] < f' d' >-.[ d,-. < a'' f' >-. d,,-.]					|
	< c-sharp'' a' >-.[ a,-. < c-sharp a' >-. e,-.] < c-sharp' b-flat' >-.[ e,-. < e c' >-. a,-.] < e' c-sharp' >-.[ a,-. < e' g >( < f a >]
		< g b-flat >-.)[ a,-. < b! d >-.( < c-sharp e >]
	< d f >)[ a-.< d a' >( < e a >] < f a >)[ d-. d'( < d e >] < d f >)[ d,-. < d' a' >-. d,-.] < f' d' >-.[ d,-. < d' f' >-. d,-.]
	< d' f' >-.[ d,-. < d b' >( < e b' >] < f b >)[ g-sharp,-. d''( < d e >] < d f >)[ d,-. < d' a' >-. d,-.] < f' d' >-.[ d,-. < d' f' >-. d,-.]
	< d' f' >-.[ d,-. < d b' >( < e b' >] < f b >)[ g-sharp,-. d''( < d e >] < d f >)[ d,-. < d' a' >-. d,-.] < f' d' >-.[ d,-. < f' f'! >-. d,-.]
	< d' f-sharp'! >16:32[ d,:-. f-sharp:-. b:-.] d:[ f-sharp: b: d:] g-sharp:[ d,,: g-sharp: b:] d:[ g-sharp: b: d:]											|
	g-sharp:[ d,,: g-sharp: b:] d:[ g-sharp: b: d:] g-sharp:[ g-sharp,,: b: f':] g-sharp:[ b: f': g-sharp:]													|
	a8\ff r r4 r2
	
	R1*18
	
	< a,,, e' a >8\downbow\ff r < a e' c-sharp' >\downbow r < a e' c-sharp' e >\downbow r < a e' c-sharp' a' >\downbow r
	R1
	< a e' a >8\downbow\ff r < a e' c-sharp' >\downbow r < a e' c-sharp' e >\downbow r < a e' c-sharp' a' >\downbow r
	R1
	< a e' a >8_\downbow\ff < a e' c-sharp' >_\downbow < a e' c-sharp' e >_\downbow
		< a e' c-sharp' a' >_\downbow < a' e' c-sharp' >^\markup { \italic \larger Cadenza } r < c-sharp a' e' > r											|
		
	%%% CADENZA %%%

	\theCadenza
	
	%%% TUTTI %%%
	
	\override TupletBracket.transparent = ##f
	<<a'1\p {s4\startTrillSpan s s s\stopTrillSpan}>> |
	<<a1 {s4\startTrillSpan s s s\stopTrillSpan}>> |
	<<d2 {s4\startTrillSpan s\stopTrillSpan}>>
		d16[( d, d' c-sharp] b[ a g g,] |
	f-sharp)[ d( f-sharp a] \tuplet 6/4 { d[ f-sharp a b d b] } a8)[ b( c-sharp_\markup { \italic dolce } d]			|
	e)[ g]( a,4~ a8)[ b(_\cr c-sharp d])
	e[( g] a,4~ \tuplet 3/2 { a8)[ g-sharp( a] } \tuplet 3/2 { a-sharp)[ g-sharpsharp-- a-sharp--] }
	\tuplet 3/2 { b--[ d-- f-sharp--] } g-sharp,,,4\f~ \tuplet 11/8 { g-sharp32[\< a( b c-sharp d e f-sharp g-sharp a b c-sharp] }
		\tuplet 10/8 { d[ e f-sharp g-sharp a b c-sharp d d-sharp])\! s }
		%%% NOTE: The edition left out a note in the 8/10! I don't know what it is, so I just added an s32.
	e4~ e16[ e-sharp--( f-sharp-- g-sharp--]) a8[ b16 r32 b32]( c-sharp,4~
	c-sharp8[ e16-.) r32 e]( g,4~ g16)[ b32-. b-. c-sharp,-. c-sharp-. e-. e-.] g,[ g b b c-sharp, c-sharp e e]
	a,[ a b-flat b-flat g-sharp g-sharp b-flat b-flat] a[ a b-flat b-flat g-sharp g-sharp b-flat b-flat] a[ a b-flat b-flat g-sharp g-sharp b-flat b-flat]
		a[ a b-flat b-flat g-sharp g-sharp b-flat b-flat]
	a[ b-flat g-sharp a a b-flat g-sharp a] a[ b-flat g-sharp a a b-flat g-sharp a] a[ b-flat g-sharp a a b-flat g-sharp a]
		\tuplet 15/8 { a[^( b-flat g-sharp a b c-sharp d e f-sharp g! a] b[ c-sharp d e]^) }
	f-sharp8\mf r < d, a' f-sharp' >2 \grace { e'16[ f-sharp] } e16[( d f-sharp a])
	<< { e4.( f-sharp8) } \\ { \appoggiatura e,8 \stemDown a2 } >> \tuplet 3/2 { e'8[( d-sharp e]) } \tuplet 3/2 { < d,! a' f-sharp' >[( e' f-sharp]) }
	< d, d'! g >8 r < d d'~ g~ >4( <d' g>8.[ f-sharp16]) g16[( a b c-sharp])
	f-sharp,4.( g8 f-sharp8.)[ f-sharp16]( g[ a b c])
	e,4.( f-sharp8 e8.)[ e16]( f[ g a b-flat])
	d,4.( e-flat8 d8.)[ d16]( c-sharp[ d f-sharp! g])
	g8.--[\< g16]( f-sharp[ g a b-flat]) b-flat8.--[ f-sharp16]( g[ a b-flat c-sharp])\!
	d8\f[( e!16-.) r32 e32]( b8[ d16-.) r32 d]( g,8[ b16-.) r32 b]( e,8[ g16-.) r32 g](
	c,8[_\markup { \italic {dim. molto} } e16-.) r32 e]( a,8[ e-flat'16-.) r32 e-flat]( c8[ e16-.) r32 e]( a,8[ e-flat'16-.) r32 e-flat](
	c8[ e16-.) r32 e]( c8[ e-flat16-.) r32 e-flat]( b8[ d16-.) r32 d]( b-flat8[ c-sharp16-.) r32 c-sharp](
	a8[_\markup { \dynamic p \italic grazioso }\tempo "Ben sostenuto." c16-.) r32 c]( f-sharp,8[ a16-.) r32 a]( 
		e8[ a16-.) r32 a32]( f-sharp8[ d'16-.) r32 d-.]
	\tuplet 3/2 { g,16[(\< b d] } \tuplet 3/2 { e8[ f-sharp16]) } \tuplet 3/2 { b,16[( d e] } \tuplet 3/2 { f-sharp8[ g16]) }
		\tuplet 3/2 { d16[( g a]\! } \tuplet 3/2 { b-flat8[ b16]) } \tuplet 3/2 { e16[(\> d b] } \tuplet 3/2 { g[ d b])\! }
	a8[ c16-. r32 c]( f-sharp,8[ a16-.) r32 a32]( e8[ a16-.) r32 a]( f-sharp8[ d'16-.) r32 d-.]
	\tuplet 3/2 { g,16[(\< b d] } \tuplet 3/2 { e8[ f-sharp16]) } \tuplet 3/2 { b,16[( d e] } \tuplet 3/2 { f-sharp8[ g16]) } \tuplet 3/2 { d16[( g a] }
		\tuplet 3/2 { b-flat8[ b16])\! } \tuplet 3/2 { e16[(\> d b] } \tuplet 3/2 { g[ e d])\! }
	\override TupletBracket.transparent = ##t
	b8[( c16-.) r32 c]( b8[ c-sharp16-.) r32 c-sharp]( \tuplet 3/2 { b16[ d-sharp f-sharp a a-sharp b]) d,[( e g b d-sharp e]) }
	e,8[( f16-.) r32 f]( e8[ f-sharp16-.) r32 f-sharp]( \tuplet 3/2 { e16[ g-sharp b d d-sharp e]) a,[( b c e g-sharp a]) }
	\tuplet 3/2 { a,[( b-sharp c-sharp! e g-sharp a]) a,[( c-sharp d f g-sharp a]) a,,[( b! b-sharp c-sharp e a]) c-sharp,[( d e f a d]) }
	\tuplet 3/2 { e-flat16-.[ g,( a!] b-flat)[ e-flat,( f-sharp!] g!)[ b-flat,( d] e-flat!)[ g,( a] b-flat)[ e-flat,( f-sharp!]
		g[ a b-flat] d-.)[ e-flat( f-sharp g b-flat e-flat] }
		
	\tuplet 3/2 { e!)[ b-flat( c d-flat) e,!( a] b-flat)[ b-flat,( e-flat e) b-flat( c] d-flat)[ b-flat( d-flat e! b-flat'! d-flat!] e!)[ d-flat!( e
		\ottava #1 b-flat' d-flat e-flat] }
	f8\f) \ottava #0 r r4 f,,,32[(_\cr a b c d e-flat e f] g-sharp[ a b c c-sharp d e-flat e])
	
	f8 r r4 f,,32[( a b c-sharp d! e-flat e f-sharp] g-sharp[ a b c c-sharp d e-flat e])
	f8 r g,,32[( b d g]) g[( b d g]) g8 r a,,32[( c-sharp! g' a]) a[( c-sharp! g' a])
	a8 r d,,32[( g b-flat e]) \ottava #1 e[( g b-flat c-sharp!]) c-sharp8 \ottava #0 r f,,32[( g g-sharp d']) d[( e f g-sharp])
	\stemDown a16-.[ a,,-. b''-. a,,32-. b''-.] a16-.[ a,,-. b''-. a,,32-. b''-.] a32[( e d a]) a[( e a, b] c-sharp[ d e g-sharp a b c-sharp e])
	a16-.[ a,,-. b''-. a,,32-. b''-.] a16-.[ a,,-. b''-. a,,32-. b''-.] a32[( e d a]) a[( e a, b] c-sharp[ d e g-sharp a b c-sharp e]) \stemNeutral
	e32[( c-sharp a e]) c-sharp[( e f-sharp g-sharp] a[ g-sharp a b] c-sharp[ d e f-sharp])
		g![( e c-sharp a]) e[( g-sharp a b] c-sharp b c-sharp d e f-sharp g! a])
	b[( a g f-sharp) e( g e d]) c-sharp[( e c-sharp b) a( b g f-sharp]) e[( g e d) c-sharp( e c-sharp b]) a[( b g f-sharp) e( g e d]
	c-sharp16)[ d8 c-sharp16]~ c-sharp[ b-sharp8 c-sharp16]~( c-sharp[ d) d-sharp e] e-sharp[\> f-sharp g b](
	a,)[ b-flat8 a16]~\! a[ b-flat8 b16]~ b8 b-sharp4( c-sharp8)
	d4\p(^\markup { \italic {con molto espress.} } c-sharp) e16[( d c-sharp e] d4)
	e( d-sharp) f-sharp16[( e d-sharp f-sharp] e4)
	\tuplet 3/2 { f-sharp8[( g a] b[ c b]) } b(\< e4\!\> b8)\!
	\grace { a16[ b] } \tuplet 3/2 { a8[( g-sharp a] c)[\< b-- a--]\! } b( e4\> b8)\!
	\grace { b-flat16[ c] } \tuplet 3/2 { b-flat8[( a b-flat] d)[ d,-- e--] } e-sharp[ f-sharp]~ \tuplet 3/2 { f-sharp[ f-sharp-.( g-.]) }
	g-sharp[( a])~ \tuplet 3/2 { a[\< a-sharp^.^( b!^.] b-sharp-.[ c-sharp-. d-.]) d-sharp[( f-sharp e])\! }
	d!4( c-sharp) e16[( d c-sharp e] d4)
	e4( d-sharp) f-sharp16[( e d-sharp f-sharp] e4)
	\tuplet 3/2 { f-sharp8[( g a] b)[ c-. b-.] } b( e4-> b8)
	\tuplet 3/2 { b-flat8[( c-sharp d] e)[ f-sharp-- e--] } e a4~ a8--
	\tuplet 3/2 { \ottava #1 b!8\p--[ a-- g--] f-sharp--[ g-- a--] c--[ b-- a--] g--[ f-sharp-- e--] }
	\tuplet 3/2 { b'--[ a-- g-sharp--] g-sharp--[ a-- b--] d--[ c-sharp!-- b--] b--[ a-- g-sharp--] }
	\tuplet 3/2 { d'[( c-sharp) b]( g-sharp)[ f-sharp( d] \ottava #0 b)[_\cr g-sharp( b] d-sharp[ f-sharp a]) }
	\ottava #1 b-flat4\f( a) c16[( b-flat a c] \tuplet 3/2 { b-flat8)[ d-flat( c] }
	\tuplet 3/2 { a-flat)[ c( b-flat] g)[ b-flat( a-flat] f)[ a-flat( g] e-flat)[ g( f]) }
	b-flat4( a!) c16[( b-flat a c] b-flat)[ b-flat( d-flat c]
	a-flat)[ a-flat( c b-flat] g)[ g( b-flat! a-flat] f)[ f( a-flat g] e-flat)[ e-flat( g f])
	e-flat4( d) f16[( e-flat d f] e-flat)[ e-flat( g e-flat]) \ottava #0
	d4( c-sharp!) e!16[( d c-sharp e] d)[ d( f-sharp d])
	c-sharp4( b16[ c-sharp d b]) b[( a g-sharp b] a)[ f-sharp( e-sharp g-sharp]
	f-sharp)[ d( c-sharp e] d)[ a( g-sharp b] a)[ f-sharp( e-sharp g] f-sharp)[ d( c-sharp e])
	
	\override TupletBracket.transparent = ##f
	d8->[ e32^( f-sharp g a] \tuplet 11/8 { b[ c-sharp d e f-sharp g a b c-sharp d e]) } \tuplet 3/2 { f-sharp8->[ g-> a->] } r4
	d,,,8->[ e32^( f-sharp g a] \tuplet 11/8 { b[ c-sharp d e f-sharp g a b c-sharp d e] } \tuplet 3/2 { f-sharp8->)[ g-sharp-> a->] } r4
	\tuplet 5/4 { a,,32[( b c-sharp d e] } \tuplet 7/4 { f-sharp[ g-sharp a b c-sharp d e] } \tuplet 3/2 { f-sharp8->)[ g-sharp-> a->] }
		\tuplet 5/4 { a,,32[( b c-sharp d e] } \tuplet 7/4 { f-sharp[ g-sharp a b c-sharp d d-sharp] } \tuplet 3/2 { e8->)[ g-sharp!-> a->] }
	\tuplet 5/4 { a,,32[( b c-sharp d e] } \tuplet 7/4 { f[ g! a b c-sharp d e] } \tuplet 3/2 { f8->)[ g-sharp!-> a->] }
		\tuplet 5/4 { a,,32[( b c d e] } \tuplet 7/4 { f[ g! a b-flat c-sharp! d e]) } \tuplet 3/2 { f8->[ g-sharp!-> a->] }
	\stemDown b-flat16:32[ f,,: g: a:] b-flat:[ c: d: f:] e:[ b: e: b':] e:[ f-sharp!: g-sharp: b:]
	\ottava #1 e:[ \ottava #0 a,,,: e: g-sharp:] a:[ b: c-sharp: e:] d:[ a: d: a':] d:[ e: f-sharp: a:]
	\ottava #1 d:[\< \ottava #0 d,,: d,: d':] d':[ d,: d,: d':] d':[ d,: d,: d':]\! g,:[ b-flat: d: g:]
	d':[\< d,: d,: d':] d':[ d,: d,: d':] d':[ d,: d,: d':]\! g,:[ b-flat: d: g:]
	\tuplet 3/2 { r16 e,[( < b-flat' e >) } \tuplet 3/2 { < b-flat e >( e, < b-flat' e >]) } \tuplet 3/2 { r16 a[( a') } \tuplet 3/2 { a( a, a']) }
		\tuplet 3/2 { r16 a,[( a') } \tuplet 3/2 { a( a, a']) } \tuplet 3/2 { r16 d,,[( < f' d' >) } \tuplet 3/2 { < f d' >( d, < f' d' >]) }
	\tuplet 3/2 { r16 e,[( < a e' >]) } \tuplet 3/2 { < a e' >[( e < a e' >]) } \tuplet 3/2 { r16 d,[( < a' f-sharp' >]) }
		\tuplet 3/2 { < a f-sharp' >[( d, < a' f-sharp' >]) } \tuplet 3/2 { r < d, d' >[( < d' d' >]) } \tuplet 3/2 { < d d' >[( d, < d' d' >]) }
		\tuplet 3/2 { r < d, d' >[( < d' d' >]) } \tuplet 3/2 { < d d' >[( d, < d' d' >]) }
	
	\override TupletBracket.transparent = ##t
	\tuplet 3/2 { a'16-.\p[ f-sharp-. a-. b-. f-sharp-. b-.] g-.[ e-. g-. c-sharp-. g-sharp-. c-sharp-.] a-.[ f-sharp-. a-. b-. f-sharp-. b-.]
		g-.[ e-. g-. c-sharp-. g-sharp-. c-sharp-.] }
	\tuplet 3/2 { a-.[ f-sharp-. a-. c-. a-. c-.] g!-.[ e-. g-. b-flat-. g-. b-flat-.] f-sharp-.[ d-. f-sharp-. a-. f-sharp-. a-.]
		d,-.[ b-. d-. f-sharp-. d-. f-sharp-.] }
	\tuplet 3/2 { e[( c-sharp a]) b'-.[ f-sharp-. b-.] g-.[ e-. g-. c-. g-sharp-. c-.] a-.[ f-sharp-. a-. b-. f-sharp-. b-.]
		g-.[ e-. g-. c-. g-sharp-. c-.] }
	\tuplet 3/2 { a-.[ f-sharp-. a-. c-. a-. c-.] g!-.[ e-. g-. b-flat-. g-. b-flat-.] f-sharp-.[ d-. f-sharp-. a-. f-sharp-. a-.]
		d,-.[ b-. d-. f-sharp-. d-. f-sharp-.] }
	\stemNeutral
	\tuplet 3/2 { e[(_\markup { "" \raise #-1.5 \italic {poco a poco cresc.}} c-sharp a]) b-.[ d-sharp,-. b'-.] g-.[ e-. g-.] < e-sharp c-sharp' >-. g-sharp,-.
		< e-sharp' c-sharp' >-.] a,-.[ < f-sharp' a >-. a,-.] b'-.[ d-sharp,-. b'-.] g!-.[ e-. g-.] < e-sharp c-sharp' >-. g-sharp,-. < e-sharp' c-sharp' >-.] }
	\tuplet 3/2 { a,-.[ < f-sharp' a >-. a,-.] < f-sharp' d'! >-.[ a,-. < f-sharp' d' >-.] g,!-.[ < d'! b' >-. g,-.] < g-sharp' e' >-.[ b,-. < g-sharp' e' >-.]
		a,-.[ < e' c-sharp' >-. a,-.] < f-sharp' d' >-.[ a,-. < f-sharp' d' >-.] g,!-.[ < d'! b' >-. g,-.] < g-sharp' e' >-.[ b,-. < g-sharp' e' >-.] }
	\tuplet 3/2 { a,-.[ < e' c-sharp' >-. a,-.] < a' f-sharp' >-.[ c-sharp,-. < a' f-sharp' >-.] b,-.[ < f-sharp' d' >-. b,-.] < b' g'! >-.[ d,-. < b' g' >-.]
		c-sharp,-.[ < a' e' >-. c-sharp,-.] < c-sharp' a' >-.[ e,-. < c-sharp' a' >-.] d,-.[ < a' f-sharp' >-. d,-.] < d' b' >-.[ f-sharp,-. < d' b' >-.] }
	\tuplet 3/2 { e,-.[ < b' g' >-. e,-.] < e' c-sharp' >-. g,-. < e' c-sharp' >-.] g,-.[ < e' b' >-. g,-.] < e' c-sharp' >-.[ g,-. < e' c-sharp' >-.]
		d'[( b g d b g]) d'[( b g d b g]) }
	\tuplet 3/2 { g'-.[ < e' b' >-. g,-.] < e' c-sharp' >-.[ g,-. < e' c-sharp' >-.] g,-.[ < e' b' >-. g,-.] < e' c-sharp' >-.[ g,-. < e' c-sharp' >-.]
		d'[( b-flat g d b-flat g]) d'[( b-flat g d b-flat g]) }
	\tuplet 3/2 { b-flat'-.[ < g' d' >-. b-flat,-.] < g' e' >-.[ b-flat,-. < g' e' >-.] b-flat,-.[ < g' d' >-. b-flat,-.] < g' e' >-.[ b-flat,-. < g' e' >-.]
		f'[( d b-flat f d b-flat!]) b-flat[( d f b-flat d f]) }
	\tuplet 3/2 { d,-.[ < b-flat' f' >-. d,-.] < b-flat' g' >-.[ d,-. < b-flat' g' >-.] d,-.[ < b-flat' f' >-. d,-.] < b-flat' g' >-.[ d,-. < b-flat' g' >-.]
		a-flat'[( f d-flat a-flat f d-flat]) d-flat[( f a-flat d-flat f a-flat]) }
	\tuplet 3/2 { f,-.[ < d-flat' a-flat' >-. f,-.] < d-flat' b-flat' >-.[ f,-. < d-flat' b-flat' >-.] f,-.[ < d-flat' a-flat' >-. f,-.] < d-flat' b-flat' >-.[
		f,-. < d-flat' b-flat' >-.] b'[( g-sharp e! b! g-sharp e]) e[( g-sharp b e g-sharp b]) }
	c-sharp4\ff\trill c-sharp\trill c-sharp\trill c-sharp\trill
	
	\override Staff.OttavaBracket.outside-staff-priority = 1000
	\ottava #1 d^\trillflat
		\ottava #0 d,,^\trillflat
		d'^\trillflat
		d'^\trillflat \ottava #0
	\ottava #1 d^\trillnatural \ottava #0
		d,,^\trillnatural
		d'^\trillnatural \ottava #1
		d'^\trillnatural \ottava #0
	\ottava #1 d^\trillnatural \ottava #0
		d,,^\trillnatural
		d'^\trillnatural
		d'^\trillnatural \ottava #0
	\revert OttavaBracket.outside-staff-priority
	
	\tuplet 3/2 { g,,,,16[( b e-sharp) e-sharp( b g]) g[(_\cr b e-sharp) e-sharp( b g]) g[( d' b') b( d, g,]) g[( d' b') b( d, g,]) }
	\tuplet 3/2 { b[( e-sharp d') d( e-sharp, b]) b[( e-sharp d') d( e-sharp, b]) d[( b' e-sharp) e-sharp( b d,]) d[( b' e-sharp) e-sharp( b d,]) }
	\tuplet 3/2 { e-sharp[( d' b') b( d, e-sharp,]) b'[( e-sharp d') d( e-sharp, b]) d[( b' e-sharp) e-sharp( b d,]) d[( b' e-sharp) e-sharp( b d,]) }
	\tuplet 3/2 { g,,[(\< b d) b( d e-sharp]) d[( e-sharp b') e-sharp,( b' d]) b[( d e-sharp) d( e-sharp b']) e-sharp,[( b' d) b( d e-sharp])\! }
	
	%%% CODA %%%
	
	f-sharp16\fp[ d,,-. d-. e!-.] f-sharp-.[ c-sharp-. d-. e-.] f-sharp-.[ f-sharp-. g-sharp-. a-sharp-.] b-.[ f-sharp-. g-. a-.]
	b[_\cr b c-sharp d-sharp] e[ b c-sharp d] e[ e f-sharp g] a[ a b c-sharp]
	d[ e f g] a[ e f g] a[ e f g] a[ f g a]
	b-flat[ f g b-flat] b-flat[ f d b-flat] f[ d b-flat f] < d' b-flat' >[ f, < b g-sharp' > e,]
	< a a' >[ e'' f-sharp! g-sharp] a[ e c-sharp a] e[ c-sharp a e] < a a' >[ a < a f-sharp' > d,]
	< b' g' >[ d' e f-sharp] g[ d b g] d[ b g d] < d' g >[ d, < c' e > e,]
	f[ c'' d e] f[ c b d-sharp] e[ b c-sharp d-sharp] e[ b a c-sharp]
	d[ d,, d' d,] f-sharp'[ d, < a' a' > d,] < d' d' >[ d, < f-sharp' f-sharp' > d,] \ottava #1 < a'' a' >[ \ottava #0
		d,, \ottava #1 < d'' d' > \ottava #0 d,,]
	r d[ d' d,] f'[ d, < a' a' > d,] < d' d' >[ d, < f' f' > d,] \ottava #1 < a'' a' >[ \ottava #0
		d,, \ottava #1 < d'' d' > \ottava #0 d,,]
	r16 a-flat[ b-flat c] d[ f g a-flat] b-flat[ c d e-flat] f[ b-flat c d]
	
	\override TupletBracket.transparent = ##f
	e-flat8\f[ \tuplet 3/2 { c-sharp!16( a c-sharp] } d8)[ \tuplet 3/2 { d16( b-flat d] } e-flat8)[ \tuplet 3/2 { c-sharp16( a c-sharp] }
		d8)[ \tuplet 3/2 { d16( b-flat d]) }
		
	\override TupletBracket.transparent = ##t
	\tuplet 3/2 { e-flat16[( d e-flat) b-flat( a b-flat]) g[( f-sharp g) e-flat( d e-flat]) b-flat[( a b-flat) g( f-sharp g]) e-flat[( d e-flat) b-flat( a b-flat]) }
	\tuplet 3/2 { f'''[( e! f) d( c-sharp! d]) b[( a-sharp b) f( e f]) d[( c-sharp! d) b!( a-sharp b]) f[( e f) d( c-sharp! d]) }
	\tuplet 3/2 { a!16[( b a\p]) } << { \noDynamic f-sharp'8\mf \noBeam g \noBeam a b c-sharp d } \\ { \tuplet 3/2 { a,16[(\<
		c a]) b[( d b]) c-sharp[( e c-sharp]) d[( f d]) e[( g e]) f[( a f])\! } } >> \tuplet 3/2 { e'[( a, e]) }
	\tuplet 3/2 { f'16[( a, d,) f-sharp'(_\cr a, d,]) g'[( d d,) g-sharp'( d d,]) a''[( a, a') b-flat( a, b-flat']) b[( a, b') c-sharp( a, c-sharp']) }
	\tuplet 3/2 { < d, d' >\ff[( < d, d' > < d' d' >\p]) } << { \noDynamic f-sharp,8\mf \noBeam g \noBeam a b c-sharp d } \\ { \tuplet 3/2 { a,16[(\<
		c a]) b[( d b]) c-sharp[( e c-sharp]) d[( f d]) e[( g e]) f[( a f])\! } } >> \tuplet 3/2 { e'[( c-sharp e,]) }
	\tuplet 3/2 { f'16[( a, d,) f-sharp'(_\cr a, d,]) g'[( d d,) g-sharp'( d d,]) a''[( a, a') b-flat( a, b-flat']) b[( a, b') c-sharp( a, c-sharp']) }
	d8\ff[ \tuplet 3/2 { e-flat16( c-sharp e-flat] } d8)[ \tuplet 3/2 { e-flat16( c-sharp e-flat] } d8) r r4
	r8 \tuplet 3/2 { e-flat16[( c-sharp e-flat] } d8)[ \tuplet 3/2 { e-flat16( c-sharp e-flat] } d8) r r4
	r8 \tuplet 3/2 { e-flat16( c-sharp e-flat] } d8) r r \tuplet 3/2 { e-flat16( c-sharp e-flat] } d8) r
	r8 \tuplet 3/2 { e-flat16[( c-sharp e-flat] } d8) r r \tuplet 3/2 { d,,16[( d' d']) d[( d, d,)
		d( d' d']) }
	< d, d' >16\ff[( < d, d' >) < d d' >( < d' d' >]) < d d' >16[( < d, d' >) < d d' >( < d' d' >]) < d d' >16[( < d, d' >) < d d' >( < d' d' >])
		< d d' >16[( < d, d' >) < d d' >( < d' d' >])
	< d d' >16[( < d, d' >) < d d' >( < d' d' >]) < d d' >16[( < d, d' >) < d d' >( < d' d' >]) < d d' >16[( < d, d' >) < d d' >( < d' d' >])
		< d d' >16[( < d, d' >) < d d' >( < d' d' >])
	d'8 d4 e8 d c-sharp4 d8
	c-sharp b4 g8 r < g, e-flat' b-flat' >16-.\fff[ < g e-flat' b-flat' >-. < g, g' >-. < g g' >-.] r8
	< d'' d' >16[( < d, d' >) < d d' >( < d' d' >]) < d d' >16[( < d, d' >) < d d' >( < d' d' >]) < d d' >16[( < d, d' >) < d d' >( < d' d' >])
		< d d' >16[( < d, d' >) < d d' >( < d' d' >])
	< d d' >16[( < d, d' >) < d d' >( < d' d' >]) < d d' >16[( < d, d' >) < d d' >( < d' d' >]) < d d' >16[( < d, d' >) < d d' >( < d' d' >])
		< d d' >16[( < d, d' >) < d d' >( < d' d' >])
	d'8 d4 e8 d c-sharp4 d8
	c-sharp b4 g8 r < g, e-flat' b-flat' >16-.\fff[ < g e-flat' b-flat' >-. < g, g' >-. < g g' >-.] r8
	r16 d'-.[ d( d']) d[( d,) d( < a' f-sharp' >)]
	< a f-sharp' >[( d,) d( < d' a' >]) < d a' >[( d,) d( < f-sharp' d' >])
	< f-sharp d' >[( d,) d( d']) d[( d,) d( < a' f-sharp' >)]
	< a f-sharp' >[( d,) d( < d' a' >]) < d a' >[( d,) d( < f-sharp' d' >])
	< f-sharp d' >16[( d,) d( < f-sharp' d' >]) < f-sharp d' >16[( d,) d( < f-sharp' d' >]) < f-sharp d' >16[( d,)
		d( < f-sharp' d' >]) < f-sharp d' >16[( d,) d( < f-sharp' d' >])
	< f-sharp d' >16[( d,) d( < f-sharp' d' >]) < f-sharp d' >16[( d,) d( < f-sharp' d' >]) < f-sharp d' >16[( d,)
		d( < f-sharp' d' >]) < f-sharp d' >16[( d,) d( < f-sharp' d' >])
	< f-sharp d' >8[ d, f-sharp a] < d, d' >[ < d d' > < d a' f-sharp' > < d a' a' >]
	< d f-sharp' d' >4 < d f-sharp' d' > < d f-sharp' d' > < d d' f-sharp' >
	< d d >1\fermata
}
