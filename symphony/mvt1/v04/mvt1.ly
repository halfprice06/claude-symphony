\version "2.24.0"
% Symphony No. 1 in C minor, movement I — v4 short score (condensed, 4 staves)
% New motto: G -> Eb (rising minor sixth), then D, Db, C (chromatic sigh).

\header {
  title = "Symphony No. 1 in C minor"
  subtitle = "I. Lento — Allegro appassionato"
  subsubtitle = "Short score, draft v4"
  tagline = ##f
}

\paper { #(set-paper-size "a4") }

global = {
  \key c \minor \time 4/4
  \tempo "Lento" 4 = 50
  s1*14
  \mark \default
  \tempo "Allegro appassionato" 4 = 126
  s1*18
  \mark \default
  s1*14
  \key aes \major \mark \default
  \tempo "Poco meno mosso" 4 = 100
  s1*22
  s1*8
  \key c \minor \mark \default
  \tempo "Tempo I" 4 = 126
  s1*46
  \mark \default
  s1*12
  \key c \major
  \tempo "Poco meno mosso" 4 = 100
  s1*24
  \key c \minor \mark \default
  \tempo "Più lento" 4 = 72
  s1*8
  \tempo "Lento" 4 = 50
  s1*10
  \bar "|."
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% INTRO 1–14
introUpper = {
  R1*4 |
  r2. d'4(\p | bes'2. a'4 | aes'2. g'4~ | g'1) |
  r2. g'4(\mp\< | es''2.) aes'4( | f''2.) b'4( | aes''2.)\f g''4~ | g''1\> | R1\! |
}
introMiddle = {
  R1*4 |
  R1 | <es' g'>1\pp | <des' f'>1 | <c' e'>1 |
  <c' es'>1\< | <c' f'>1 | <d' f'>1 | <c' es' fis'>2. <c' es' g'>4 |
  <g d'>1\p | <b d' f'>1 |
}
introLower = {
  r2. g,4(\pp | es2. d4 | des2. c4~ | c1) |
  R1 | g1\pp | aes1 | g1 |
  g1\< | aes1 | aes1 | c'2.\f c'4 |
  r4 es4(\mp c'2~ | c'4 b2.) |
}
introBass = {
  c,1\ppp~ | c,1~ | c,1~ | c,1 |
  c,1 | es,1 | des,1 | c,1 |
  c,1\< | f,1 | d,1 | aes,1\f |
  g,1\p~ | g,1 |
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% FIRST THEME 15–32
tOneUpper = {
  r8 g'8\f es''4.-> d''8 des''8 c''8 | c''4 b'8( c''8) aes'4.-> g'8 |
  r8 g'8 f''4.-> es''8 d''8 c''8 | b'4 d''8( c''8) g'2 |
  r8 c''8 aes''4.-> g''8 ges''8 f''8 | f''8 g''8 aes''8 c'''8 bes''4.-> aes''8 |
  aes''8 g''8 f''8 es''8 d''4.-> c''8 | b'8 c''8 d''8 b'8 c''4 r4 |
  es''4(\< d''4 c''4) f''4( | es''4 d''4) g''4( f''4 | es''4) aes''4( g''4 f''4) | b''2.->\ff r4 |
  r8 g''8\ff es'''4.-> d'''8 des'''8 c'''8 | c'''4 b''8( c'''8) aes''4.-> g''8 |
  r8 g''8 f'''4.-> es'''8 d'''8 c'''8 | b''8 c'''8 d'''8 b''8 c'''4 g''4 |
  aes''4.-> g''8 f''4 d''4 | c''2 r2 |
}
tOneMiddle = {
  r8 <es' g'>8~\mf <es' g'>4 r8 <es' g'>8~ <es' g'>4 | r8 <es' g'>8~ <es' g'>4 r8 <d' f'>8~ <d' f'>4 |
  r8 <d' f' aes'>8~ <d' f' aes'>4 r8 <d' f' aes'>8~ <d' f' aes'>4 | r8 <d' f'>8~ <d' f'>4 r8 <b d'>8~ <b d'>4 |
  r8 <c' f'>8~ <c' f'>4 r8 <c' f'>8~ <c' f'>4 | r8 <c' f'>8~ <c' f'>4 r8 <es' aes'>8~ <es' aes'>4 |
  r8 <c' f'>8~ <c' f'>4 r8 <c' f'>8~ <c' f'>4 | r8 <d' f'>8~ <d' f'>4 r8 <es' g'>8~ <es' g'>4 |
  <es' g'>4-> <es' g'>4 <es' g'>4 <d' f'>4-> | <d' f'>4 <d' f'>4 <es' g'>4-> <es' g'>4 |
  <es' g'>4 <c' f'>4-> <c' f'>4 <c' f'>4 | <b d' f' aes'>2.-> r4 |
  \repeat unfold 4 { r8 <es' g' c''>8 } | \repeat unfold 2 { r8 <es' g' c''>8 } \repeat unfold 2 { r8 <d' f' b'>8 } |
  \repeat unfold 4 { r8 <d' f' aes'>8 } | r8 <d' f' b'>8 r8 <d' f' b'>8 r8 <es' g' c''>8 r8 <es' g' c''>8 |
  <c' f' aes'>4 r8 <c' f' aes'>8 <b d' f'>4 r8 <b d' f'>8 | <g c' es'>2 r2 |
}
tOneLower = {
  c2\mf d2 | es2 d2 | f2 aes2 | g2 g,2 |
  f2 es2 | des2 c2 | f2 g2 | g2 c2 |
  c4 c4 c4 b,4 | b,4 b,4 c4 c4 | c4 f4 f4 f4 | <f aes>2. r4 |
  c'2 d'2 | es'2 d'2 | f2 aes2 | g2 c'2 |
  aes2 g2 | c2 r2 |
}
tOneBass = {
  c,4\f r8 c,8 c,4 r8 c,8 | c,4 r8 c,8 g,,4 r8 g,,8 |
  aes,,4 r8 aes,,8 aes,,4 r8 aes,,8 | g,,4 r8 g,,8 g,,4 r8 g,,8 |
  f,,4 r8 f,,8 f,,4 r8 f,,8 | f,,4 r8 f,,8 aes,,4 r8 aes,,8 |
  f,,4 r8 f,,8 g,,4 r8 g,,8 | g,,4 r8 g,,8 c,4 r8 c,8 |
  c,4 c,4 c,4 b,,4 | b,,4 b,,4 c,4 c,4 | c,4 f,,4 f,,4 aes,,4 | d,2.-> r4 |
  \repeat unfold 8 c,8 | \repeat unfold 4 c,8 \repeat unfold 4 g,,8 |
  \repeat unfold 8 aes,,8 | g,,8 g,, g,, g,, c, c, c, c, |
  f,,4 r8 f,,8 g,,4 r8 g,,8 | c,2 r2 |
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% TRANSITION 33–46
transUpper = {
  R1*2 |
  r8 f'8\mf des''4.-> c''8 ces''8 bes'8 | bes'4 a'8( bes'8) g'4. f'8 |
  r8 bes'8\< ges''4.-> f''8 fes''8 es''8 | r8 c''8 aes''4.-> g''8 ges''8 f''8 |
  r8 d''8 bes''4.-> a''8 aes''8 g''8 | r8 es''8 c'''4.-> b''8 bes''8 aes''8 |
  g''1\ff~ | g''2 f''2 | es''2 des''2 | c''1\> |
  bes'1\p~ | bes'2 r2 |
}
transMiddle = {
  R1 | r8 c'8\mf aes'4.-> g'8 ges'8 f'8 | f'4 e'8( f'8) d'2 | <es' g'>1 |
  \repeat unfold 4 { r8 <ges' bes'>8 } | \repeat unfold 4 { r8 <f' aes'>8 } |
  \repeat unfold 4 { r8 <f' aes'>8 } | \repeat unfold 4 { r8 <g' bes' des''>8 } |
  <g' bes' des''>1 | <g' bes' des''>1 | <g' bes'>1 | <g' bes'>1 |
  <g bes des'>1\pp~ | <g bes des'>2 r2 |
}
transLower = {
  r8 g8\mf es'4.-> d'8 des'8 c'8 | c'4 bes8( aes8) g4 f4 | f2 aes2 | g2 es2 |
  ges1 | aes1 | aes1 | g1 |
  r2. es4(\mf | c'1) | r2. es4( | c'2 bes2) |
  g1\pp | g2 r4 es4\p |
}
transBass = {
  c,1\mf | f,1 | bes,,1 | es,1 |
  es,1\< | f,1 | bes,,1 | es,1 |
  es,1\ff~ | es,1~ | es,1~ | es,1\>~ |
  es,1\pp~ | es,2 r2 |
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% SECOND THEME 47–67 (A♭ major)
tTwoUpper = {
  % harp: breathing arpeggios under the cello/horn melody
  aes8\pp es' aes' c'' es''2 | g8 es' g' bes' es''2 | f8 c' f' aes' c''2 | es8 aes c' es' aes'2 |
  des8 aes des' f' c''2 | c8 ges c' es' ges'2 | bes,8 f bes des' f'2 | es8 bes des' g' bes'2 |
  aes,8 es aes c' es'4 es'4(\p |
  % violins
  c''2.~ c''8 b'8 | bes'2 aes'4 g'8 aes'8 | f''2.~\< f''8 e''8 | es''2 des''4 c''8 des''8 |
  bes''2.~ bes''8 a''8 | aes''2 ges''4 fes''8 es''8 | c'''2.~\f c'''8 bes''8 | bes''2 aes''4 g''8 aes''8 |
  f''2.~ f''8 e''8 | es''2 des''4 c''8 des''8 | f''2.~\> f''8 es''8 | es''4 des''4 c''4 bes'4 | aes'1\p) |
}
tTwoMiddle = {
  <es' aes'>2\pp <es' aes'>2 | <es' g'>2 <es' g'>2 | <aes' c''>2 <aes' c''>4 <g' bes'>4 | <aes' c''>2 <g' des''>2 |
  <f' aes' c''>1 | <es' ges' bes'>1 | <des' f' aes'>1 | <des' g' bes'>1 | <c' es' aes'>1 |
  es'2\p r8 es'8( f'8 g'8 | g'2) es'2 | aes'2 r8 aes'8( g'8 f'8 | es'2) g'2 |
  f'2 r8 f'8( es'8 des'8 | fes'2) ces'2 | c'2 es'2 | des'2 des'2 |
  c'2 r8 c'8( des'8 es'8 | f'2) aes'2 | des'2 des'2 | des'2 des'2 | c'1 |
}
tTwoLower = {
  c'2.~\mf c'8 b8 | bes2 aes4 g8 aes8 | f'2.~ f'8 e'8 | es'2 des'4 c'8 des'8 |
  aes'2.~ aes'8 g'8 | ges'2 f'4 es'8 f'8 | es'2. des'8 c'8 | des'2 c'4 bes4 | aes1 |
  aes,8\p es aes c' es'2 | g,8 c es bes c'2 | f,8 c f aes c'2 | es,8 aes, c es aes2 |
  ges,8 des ges bes des'2 | des,8 aes, des fes aes2 | es,8 aes, c es aes2 | es,8 bes, des g bes2 |
  f,8 c f aes c'2 | des,8 aes, des f aes2 | bes,,8 f, bes, des f2 | es,8 bes, des g bes2 | aes,,8 es, aes, c es2 |
}
tTwoBass = {
  aes,1\p | g,1 | f,1 | es,1 | des,1 | c,1 | bes,,1 | es,1 | aes,,1 |
  aes,,1 | g,,1 | f,,2 e,,2 | es,1 | ges,1 | des,1 | es,1 | es,1 |
  f,1 | des,1 | bes,,1 | es,1 | aes,,1 |
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% CLOSING 68–75
closUpper = {
  r2. c''4(\pp | aes''2.~ aes''8 g''8 | ges''2 f''4 es''8 f''8) |
  r2. es'4( | ces''2. bes'4 | beses'2. aes'4~ | aes'1) | R1 |
}
closMiddle = {
  <c' es'>1\ppp | <c' es'>1 | <c' ges'>1 | <des' fes'>1 |
  <ces' es'>1 | <ces' fes'>1 | <ces' es'>1 | R1 |
}
closLower = {
  aes1\ppp~ | aes1~ | aes1~ | aes1~ | aes1~ | aes1~ | aes1~ | aes1 |
}
closBass = {
  aes,,1\ppp~ | aes,,1~ | aes,,1~ | aes,,1~ | aes,,1~ | aes,,1~ | aes,,1~ | aes,,1 |
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% DEVELOPMENT 76–121
devUpper = {
  % D1: motto-head dialogue, falling major thirds
  R1 | r8 es''8\mp ces'''4.-> bes''8 beses''8 aes''8 |
  R1 | r8 b'8\mf g''4.-> fis''8 f''8 e''8 |
  R1 | r8 g'8\f es''4.-> d''8 des''8 c''8 |
  r8 g''8\ff es'''4.-> d'''8 des'''8 c'''8 | <b' d'' f'' aes''>4-> r4 <b' d'' f'' aes''>4-> r4 |
  % D2: fugato
  R1*9 |
  r8 f''8\f des'''4.-> c'''8 ces'''8 bes''8 | bes''4 a''8( bes''8) ges''4.-> f''8 |
  r8 f''8 des'''4.-> c'''8 ces'''8 bes''8 |
  % D3: second theme transformed, B♭ minor
  r2. f'4(\ff | des''2.~ des''8 c''8 | c''2 bes'4 a'8 bes'8 | ges''2.~ ges''8 f''8 |
  f''2 es''4 des''8 es''8 | bes''2.~ bes''8 a''8) |
  aes''2.~\< aes''8 g''8 | bes''2.~ bes''8 a''8 | c'''2.~ c'''8 b''8 | des'''2.~ des'''8 c'''8 | d'''2.~ d'''8 cis'''8 | d'''1 |
  % D4: dominant pedal, motto augmented, collapse
  d'''1:32\ff | es'''1:32 | f'''1:32 | f'''1:32 | es'''1:32 |
  aes''1:32\fff | g''1:32 | g''2\> f''2 | es''2 d''2 | d''1\p |
  R1*4 |
}
devMiddle = {
  <ces' es'>1:32\p | <ces' es'>1:32 | <g' b'>1:32 | <g' b'>1:32 |
  <es' g'>1:32\< | <es' g'>1:32 | \repeat unfold 4 { r8 <es' g' c''>8 } | <b d' f'>4-> r4 <b d' f'>4-> r4 |
  R1*6 |
  r8 c'8\f aes'4.-> g'8 ges'8 f'8 | f'4 e'8( f'8) des'4.-> c'8 | f'4 g'4 aes'4 a'4 |
  bes4. c'8 des'8( es'8) f'4 | des'4 c'8( bes8) es'4. des'8 | r8 bes'8 ges''4.-> f''8 fes''8 es''8 |
  \repeat unfold 2 { des'8 f' bes' f' } | \repeat unfold 2 { des'8 f' bes' f' } |
  \repeat unfold 2 { c'8 es' a' es' } | \repeat unfold 2 { des'8 ges' bes' ges' } |
  des'8 f' bes' f' c' es' a' es' | \repeat unfold 2 { des'8 ges' bes' ges' } |
  <c' f' aes'>1:32 | <des' f' bes'>1:32 | <es' g' c''>1:32 | <f' aes' des''>1:32 | <f' aes' b'>1:32 | <fis' a' c''>1:32 |
  \repeat unfold 4 { \tuplet 3/2 { b8 d' f' } } | \repeat unfold 4 { \tuplet 3/2 { c'8 es' g' } } |
  \repeat unfold 4 { \tuplet 3/2 { b8 d' f' } } | \repeat unfold 4 { \tuplet 3/2 { bes8 des' f' } } |
  \repeat unfold 4 { \tuplet 3/2 { c'8 es' g' } } |
  <c' es' aes'>1:32 | <b d' f'>1:32 | <b d' f'>1 | <c' es'>1 | <b d'>1 |
  r8 g8\pp es'4.-> d'8 des'8 c'8 | c'4 b8( c'8) aes4.-> g8 |
  r8 g8\< es'4.-> d'8 des'8 c'8 | b8 c'8 d'8 es'8 f'8 g'8 aes'8 b'8 |
}
devLower = {
  r8 es8\mp ces'4.-> bes8 beses8 aes8 | aes1 |
  r8 b,8\mf g4.-> fis8 f8 e8 | e1 |
  r8 g,8\f es4.-> d8 des8 c8 | c1 | c2 c2 | <g b>4-> r4 <g b>4-> r4 |
  R1*3 |
  r8 g8\f es'4.-> d'8 des'8 c'8 | c'4 b8( c'8) aes4.-> g8 | c'4 d'4 es'4 e'4 |
  f4. g8 aes8( bes8) c'4 | aes4 g8( f8) bes4. aes8 | des'2 c'2 |
  bes2 bes2 | es2 des2 | r4. f8 des'4.-> c'8 |
  ces'8\ff bes8 r2. | bes2 r8 f8 des'8 c'8 | c'2 r8 f8 c'8 bes8 |
  ges2 r8 ges8 des'8 c'8 | bes2 a2 | ges2 r8 ges8 bes8 des'8 |
  f1 | f1 | g1 | f1 | f1 | fis1 |
  g1\ff | es'1~ | es'2. d'4 | des'2. c'4~ | c'1 |
  aes1\fff | g1 | <g b>1\> | <g c'>1 | <g b>1\p |
  R1*4 |
}
devBass = {
  aes,,1\p | aes,,1 | e,1 | e,1 | c,1\< | c,1 | \repeat unfold 8 c,8 | g,,4-> r4 g,,4-> r4 |
  r8 d,8\f bes,4.-> a,8 aes,8 g,8 | g,4 fis,8( g,8) es,4.-> d,8 | g,4 a,4 bes,4 b,4 |
  c4. d8 es8( f8) g4 | es4 d8( c8) f4. es8 | aes,2 g,2 |
  f,1 | bes,,2 c,2 | des,2 c,2 | bes,,1 | es,2 f,2 | bes,,4 r4 bes,,4 r4 |
  bes,,1 | bes,,1 | a,,1 | ges,,1 | f,,1 | ges,,1 |
  f,1\< | des,1 | c,1 | bes,,1 | aes,,1 | a,,1 |
  g,,1\ff~ | g,,1~ | g,,1~ | g,,1~ | g,,1~ |
  g,,1\fff~ | g,,1~ | g,,1\>~ | g,,1~ | g,,1\pp~ |
  g,,1~ | g,,1~ | g,,1~ | g,,1\< |
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% RECAPITULATION 122–154
recUpper = {
  r8 g''8\ff es'''4.-> d'''8 des'''8 c'''8 | c'''4 b''8( c'''8) aes''4.-> g''8 |
  r8 g''8 f'''4.-> es'''8 d'''8 c'''8 | b''4 d'''8( c'''8) g''2 |
  es''4( d''4 c''4) f''4( | es''4 d''4) g''4( f''4 | es''4) aes''4( g''4 f''4) | b''2.-> r4 |
  r8 g'8\f es''4.-> d''8 des''8 c''8 | c''4\> b'8( c''8) aes'4. g'8 | g'1\p~ | g'2 r2 |
  % second theme in C major: high string tremolo, then violins
  <e'' g''>1:32\pp | <d'' g''>1:32 | <e'' a''>1:32 | <e'' g''>2:32 <f'' g''>2:32 |
  <e'' a''>1:32 | <d'' g''>1:32 | <c'' f''>1:32 | <d'' f''>1:32 | <c'' e''>2:32 r4 g'4(\mf |
  e''2.~ e''8 dis''8 | d''2 c''4 b'8 c''8 | a''2.~\< a''8 gis''8 | g''2 f''4 e''8 f''8 |
  d'''2.~ d'''8 cis'''8 | c'''2 bes''4 aes''8 g''8 | e'''2.~\ff e'''8 d'''8 | d'''2 c'''4 b''8 c'''8 |
  es'''2.~\fff es'''8 d'''8 | d'''2 c'''4 b''8 c'''8 | a''2.~\> a''8 gis''8 | g''2 f''4 e''8 f''8 |
  a''2.~ a''8 g''8 | g''4 f''4 e''4 d''4 | c''1\mf) |
}
recMiddle = {
  \repeat unfold 4 { r8 <es' g' c''>8 } | \repeat unfold 2 { r8 <es' g' c''>8 } \repeat unfold 2 { r8 <d' f' b'>8 } |
  \repeat unfold 4 { r8 <d' f' aes'>8 } | \repeat unfold 4 { r8 <d' f' b'>8 } |
  <es' g'>4-> <es' g'>4 <es' g'>4 <d' f'>4-> | <d' f'>4 <d' f'>4 <es' g'>4-> <es' g'>4 |
  <es' g'>4 <c' f'>4-> <c' f'>4 <c' f'>4 | <b d' f' aes'>2.-> r4 |
  \repeat unfold 4 { r8 <es' g'>8 } | <es' g'>2 <d' f'>2 | <d' f'>1\p | <d' f'>2 r2 |
  r2 r8 g'8(\p a'8 b'8 | c''2) r2 | r2 r8 c''8( d''8 e''8 | e''2) r2 |
  r2 r8 a'8( g'8 a'8 | bes'2) r2 | c''2 a'2 | b'2 d''2 | c''2 r2 |
  g'2\mp r8 g'8( a'8 b'8 | b'2) g'2 | c''2 r8 c''8( b'8 a'8 | g'2) b'2 |
  f'2 r8 f'8( g'8 a'8 | aes'2) f'2 | g'2 c''2 | b'2 f'2 |
  c''2 r8 c''8( bes'8 aes'8 | aes'2) f'2 | e'2 r8 e'8( f'8 g'8 | a'2) c''2 |
  f'2 f'2 | f'2 d'2 | e'1 |
}
recLower = {
  c'2 d'2 | es'2 d'2 | f2 aes2 | g2 g,2 |
  c4 c4 c4 b,4 | b,4 b,4 c4 c4 | c4 f4 f4 f4 | <f aes>2. r4 |
  c2 d2 | es2 d2 | b,1 | r2. g4(\mf |
  e'2.~ e'8 dis'8 | d'2 c'4 b8 c'8 | a'2.~ a'8 gis'8 | g'2 f'4 e'8 f'8 |
  c''2.~ c''8 b'8 | bes'2 a'4 g'8 a'8 | g'2. f'8 e'8 | f'2 e'4 d'4 | c'1) |
  c8\p g c' e' g'2 | g,8 d g b d'2 | a,8 e a c' e'2 | g,8 c e g c'2 |
  bes,8 f bes d' f'2 | f,8 c f aes c'2 | g,8 c e g c'2 | g,8 d f b d'2 |
  aes,8 es aes c' es'2 | d8 aes b d' f'2 | a,8 e a c' e'2 | f,8 c f a c'2 |
  d,8 a, d f a2 | g,8 d f b d'2 | c,8 g, c e g2 |
}
recBass = {
  \repeat unfold 8 c,8 | \repeat unfold 4 c,8 \repeat unfold 4 g,,8 |
  \repeat unfold 8 aes,,8 | \repeat unfold 8 g,,8 |
  c,4 c,4 c,4 b,,4 | b,,4 b,,4 c,4 c,4 | c,4 f,,4 f,,4 aes,,4 | d,2.-> r4 |
  c,4 r8 c,8 c,4 r8 c,8 | c,2 g,,2 | g,,1~ | g,,2 r2 |
  c,1 | b,,1 | a,,1 | g,,1 | f,1 | e,1 | d,1 | g,1 | c,1 |
  c,1 | g,,1 | a,,1 | g,,1 | bes,,1 | f,1 | g,1 | g,1 |
  aes,1 | d,2 g,,2 | a,,1 | f,,1 | d,1 | g,1 | c,1 |
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% CODA 155–172
codaUpper = {
  c''1\mp~ | c''2 r2 | R1*6 |
  r2. g'4(\pp | es''1~ | es''2. d''4 | des''1~ | des''2. c''4~ |
  c''1~ | c''1~ | c''1~ | c''1~ | c''1\fermata) |
}
codaMiddle = {
  <e' g'>1 | r2. g'4(\p | e''2. d''4 | des''2. c''4~ | c''1) |
  <c' es'>1\pp | <c' es'>1 | <c' es'>1 | <c' es'>1 | <c' es'>1 |
  <c' f'>2. <b f'>4 | <des' f'>1 | <des' f'>2. <c' es'>4 | <c' es'>1 | <c' es'>1 |
  <g c'>1 | <g c'>1 | <g c'>1\fermata |
}
codaLower = {
  g1 | aes1 | g1 | aes2. g4 | g1 |
  r2. g,4(\pp | es2. d4 | des2. c4~ | c1) |
  aes1 | aes2. g4 | f1 | f2. es4 | es1 | es1 |
  R1 | R1 | R1\fermata |
}
codaBass = {
  c,1\mp | aes,,1 | g,,1 | des,2. c,4~ | c,1~ |
  c,1\pp~ | c,1~ | c,1~ | c,1~ | c,1~ | c,1~ | c,1~ | c,1~ | c,1~ | c,1~ |
  c,1~ | c,1~ | c,1\fermata |
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ASSEMBLY
upper  = { \introUpper  \tOneUpper  \transUpper  \tTwoUpper  \closUpper  \devUpper  \recUpper  \codaUpper }
middle = { \introMiddle \tOneMiddle \transMiddle \tTwoMiddle \closMiddle \devMiddle \recMiddle \codaMiddle }
lower  = { \introLower  \tOneLower  \transLower  \tTwoLower  \closLower  \devLower  \recLower  \codaLower }
bass   = { \introBass   \tOneBass   \transBass   \tTwoBass   \closBass   \devBass   \recBass   \codaBass }

\score {
  <<
    \new Staff \with { instrumentName = "Upper" midiInstrument = "violin" } << \global \upper >>
    \new Staff \with { instrumentName = "Middle" midiInstrument = "string ensemble 1" } << \global \middle >>
    \new Staff \with { instrumentName = "Lower" midiInstrument = "cello" } << \clef bass \global \lower >>
    \new Staff \with { instrumentName = "Bass" midiInstrument = "contrabass" } << \clef bass \global \bass >>
  >>
  \layout { }
  \midi { }
}
