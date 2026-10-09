\version "2.20.0"

theCadenza =  \relative d'' {
	\cadenzaOn
	\override TupletBracket.transparent = ##f
	
	< a e' c-sharp' a' >8\ff_\markup { \italic legato } r8 g-sharp''4( a) << { c-sharp,4 } \\ { a,4^( } >>
	<< { r s r } \\ { b-flat < g,! e' >^)( g-sharp) } >> < g-sharp d' b' e >8 r
	<< {a4( c-sharp32[ e a c-sharp e a c-sharp e]) g-sharp4( a } \\ { } >>
	<< { c-sharp,4) r s r } \\ { a,4^( b-flat < g,! e' >^)( g-sharp) } >>
	< g-sharp d' b' e >8 r \bar "" \break a4 c-sharp32[( e a c-sharp e a e'])
	<< { e,2 a, } \\ { b-sharp4( c-sharp) < b-sharp, d-sharp >( < c-sharp e >) } >>
	g-sharp!4( \stemUp a8)[ \stemNeutral\stemDown g-sharp'''!]( \stemNeutral a)[ < b-sharp,,! e >]( < c-sharp e >)[ < b-sharp,! d-sharp! a' >](
	< c-sharp e a >)[ g-sharp!]( \stemUp a)[ \stemNeutral\stemDown g-sharp'''!]( \stemNeutral a)[ < b-sharp,,! e >]( < c-sharp e >)[ < b-sharp,! d-sharp! a' >](
	< c-sharp e a >)[ g-sharp!] \bar ""\break a32[( c-sharp e a c-sharp e]) a[( e c-sharp a e c-sharp]) a32[( c-sharp e a c-sharp e a])
	c-sharp[( a e c-sharp a e c-sharp]) a[( c-sharp e a c-sharp e a c-sharp e a]) c-sharp8--[ \ottava #1 e8] \bar ""\break
	< a,, d\harmonic >2\fermata \ottava #0 s2 g,,32[( a c-sharp e a c-sharp e] a[ e c-sharp a e c-sharp]) g[( c-sharp e a c-sharp e a] c-sharp[ a e c-sharp a e c-sharp a])
	g[( a c-sharp e a c-sharp e a c-sharp e a]) c-sharp8[ e] \bar ""\break
	< a,, d\harmonic >2\fermata s2
	< g,, a' e' c-sharp' >8 r < g a' e' c-sharp' >4 < g' a >8[( c-sharp']) \grace { c-sharp16[ d] } c-sharp16[( b c-sharp e])
	< f-sharp,, a >8 d32[( f-sharp a d f-sharp a d]) f-sharp8-.[ a-.]
	d2\fermata s2
	< a,, f-sharp' d-sharp' >8 r < a f-sharp' d-sharp' >4\downbow < a, f-sharp' a >8[( d-sharp'' ]) \grace { d-sharp16[ e] } d-sharp16[( c-sharp d-sharp f-sharp])
	g-sharp,,,8[( b32 e g-sharp b e g-sharp b e]) g-sharp!8[ b] \bar ""\break
	\ottava #1 e2\fermata s2
	e8-0[ \ottava #0 < g-sharp,,,, e' >( < a f' > < a-sharp f-sharp' >]) e'''-0[ < b-flat,, g' >( < b g-sharp' > < c-sharp a' >])
	e'-0 < d, b' >8[( < d-sharp b-sharp' > < e c-sharp' >]) < f' d' >32--[ < e c-sharp' >( < d-sharp b-sharp' > < d b' > < c-sharp a-sharp' > < c a' > < b g-sharp' > < a-sharp f-sharpsharp' > < a f-sharp' > < g-sharp e-sharp' > < g e' > < f-sharp d-sharp' >] < f d' >8)
	r s8.. \bar "" \break
	\ottava #1 e'''8 \ottava #0 < b,,, g-sharp' >[( < c a' > < c-sharp a-sharp' >]) e''-0 < d,, b' >[( < d-sharp b-sharp' > < e c-sharp' >]) \bar ""
	e'-0 < e, c-sharp' >[( < f-sharp d'! > < f-sharpsharp d-sharp' >]) < g-sharp' e' >32--[ < f-sharpsharp d-sharp' >( < f-sharp d' > < e-sharp c-sharp' > < e c' > < d-sharp b' > < c-sharpsharp a-sharp' > < c-sharp a' > < b-sharp g-sharp' > < b g' > < a-sharp f-sharp' > < g-sharpsharp e-sharp' >] < g-sharp e' >8)
	r s4 \bar ""
	\ottava #1 e'''!8 \ottava #0 < e,,, d'! e >\downbow[ < f-sharp! d' e >\downbow < g! d' e >\downbow] \bar ""\break < g-sharp d' e >\downbow[ < a d e >\downbow < b-flat d e >\downbow < b d e >\downbow] \bar ""
	< c d e >[ < c-sharp d e > < d e > < d-sharp e >] << { e8\downbow[ e\downbow e\downbow] e\upbow[ } \\ { e8[ e e] e[ } >>
	<< { e8\downbow e\upbow] } \\ { e8 e]_\markup { \italic dim. } } >>
	
	< e e >1^\trillsharp\fermata
	< e e >1^\trillnatural \grace { d-sharp16[ e\p] }
	\tempo "Quasi andante"
	<< { f4( e!) } \\ { s4 < b-flat, g' d-flat' >8 r } >> f''16[( e d-sharp f] \tuplet 3/2 { e)[ c--( c-sharp--] } \tuplet 3/2 { d--[ d-sharp-- e--]) } \bar ""\break
	<< { g4( f!) } \\ { s4 < a,, f' >8 r } >> g''!16[( f! e g] \tuplet 3/2 { f)[ c( d-flat-.] } d!32-.[ e-flat-. e-. f-.])
	<< { g4(^\markup { \italic {cresc. e accelerando}} f-sharp) } \\ { s4 < c, a' >8 r } >> a''16[( g f-sharp a]) << { g4 } \\ { < b,, g' >8 r } >>
	<< { a''4( g-sharp) } \\ { s4 < d, b' >8 r8 } >> \stemUp b''16[( a g-sharp b] a8)[ < c,,! e a >\downbow] \stemNeutral \bar ""\break
	b''16\upbow[( a g-sharp! b] a8)[ < c-sharp,, e a >] b''16[( a g-sharp b] a8)[ < d,, f-sharp a >-.]
	a''-.[ < d-sharp,, f-sharp a >-.] a''-.[ < e, g! a >-.] a'-.[ < f, a >-.] \tuplet 3/2 { a'-.[ < f-sharp, a >-. a'-.] }
	\tuplet 3/2 { < g,! a >-.[ a'-. < g-sharp, a >-.] } \tuplet 3/2 { a'-.[ a,-. a'-.] } \tuplet 3/2 { a,-.[ a'( a,]) } < g, e' c-sharp' b-flat' >8.\ff[( b-flat'''16])
	b-flat4~ b-flat8[ a-- g--] \bar ""\break f--[^\markup { "" \raise #2.0 \italic {meno mosso} } e-- d--]
	c-sharp!--[( b-flat-- a--]) g[( f e]) d[_( c-sharp! \bar ""
	b-flat!] a32[\( g f e d c b-flat a]_)\) < g-sharp f'! d' b' >8.[( b'''16]) b4~
	b8[ a-- g-sharp--] f--[ e-- d--] b--[( a--
	g-sharp--]) f![( e d]) b![( a g-sharp] \bar ""\break
	f!32[ e e-flat d c-sharp c b b-flat]) \tuplet 3/2 { a4( b-flat a) }
	\tuplet 3/2 { a'4( b-flat! a) } \tuplet 3/2 { a,4( b-flat a) }
	\tuplet 3/2 { a'4( b-flat a) } \tuplet 3/2 { a,8[( b-flat! a]) } \tuplet 3/2 { a'8[( b-flat! a]) }
	\tuplet 3/2 { a,8[( b-flat a]) } \tuplet 3/2 { a'8[( b-flat! a]) } \tuplet 3/2 { a,16[( b-flat a]) } \tuplet 3/2 { a'16[( b-flat a]) } \bar "" \break \tuplet 3/2 { a'16[( b-flat a]) } \tuplet 3/2 { a,16[( b-flat! a]) }
	\tuplet 3/2 { a'[( b-flat! a) } \tuplet 3/2 { a'( b-flat a]) } \tuplet 3/2 { a,( b-flat! a) } \tuplet 3/2 { a,( b-flat! a]) } \tuplet 3/2 { a,[( b-flat! a) } \tuplet 3/2 { a'( b-flat! a]) } \tuplet 3/2 { a'( b-flat! a) } \tuplet 3/2 { a,( b-flat! a]) }
	\tuplet 3/2 { a'[( b-flat! a) } \tuplet 3/2 { a'( b-flat! a]) } \bar "" \break \tuplet 3/2 { a,[( b-flat! a)] } \tuplet 3/2 { a,[( b-flat! a]) } \tuplet 3/2 { a'[(\( b-flat a]) } \tuplet 3/2 { a,[( b-flat a])\) } \tuplet 3/2 { a'[(\( b-flat a]) } \tuplet 3/2 { a,[( b-flat a])\) }
	\tuplet 3/2 { a'[(\( b-flat a]) } \tuplet 3/2 { a,[( b-flat a])\) } \tuplet 3/2 { a'[(\( b-flat a]) } \tuplet 3/2 { a,[( b-flat a])\) }
	a'2^\trillsharp\fermata
	a2^\trillnatural\fermata
	
	\cadenzaOff
	\bar "||" \break
}


 
