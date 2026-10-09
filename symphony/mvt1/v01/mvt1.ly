\version "2.24.0"
% Symphony No. 1 in C minor, movement I — v1 short score (condensed, 4 staves)
% Staves: Upper (melody), Middle (inner harmony / counter), Lower (tenor line / cello / horn), Bass.

\header {
  title = "Symphony No. 1 in C minor"
  subtitle = "I. Lento — Allegro appassionato"
  subsubtitle = "Short score, draft v1"
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
  s1*16
  \key aes \major \mark \default
  \tempo "Poco meno mosso" 4 = 104
  s1*24
  s1*8
  \key c \minor \mark \default
  \tempo "Tempo I" 4 = 126
  s1*44
  \mark \default
  s1*12
  \key c \major
  \tempo "Poco meno mosso" 4 = 104
  s1*16
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
  r2 c'2(\p | aes'2. g'4 | f'2 des'4. c'8) | c'1 |
  r4 g'4(\mp\< es''2) | r4 aes'4( f''2) | r4 c''4(\f aes''2~ | aes''4 g''2.~) | g''1\>~ | g''2\! r2 |
}
introMiddle = {
  <g c' es'>1\pp~ | <g c' es'>2. <g c' e'>4 | <aes c' f'>1 | <g b f'>2 <g c' es'>2 |
  <es g>1 | <f aes>1 | <f aes>2 <f g b>2 | <e g>1 |
  <c' es'>1\< | <c' f'>1 | <c' es' fis'>1\f | <c'' es''>2 <b' d''>2 |
  <b d'>1\p | <b d' f'>1 |
}
introLower = {
  r2 g,2(\pp | es2. d4 | c2 aes,4. g,8) | g,1 |
  c1~ | c1 | des1 | c1 |
  g1\< | aes1 | c'1\f | g1 |
  r4 g4(\mp es'2~ | es'4 d'2.) |
}
introBass = {
  c,1\ppp~ | c,1~ | c,1~ | c,1 |
  c,1~ | c,1 | des,1 | c,1 |
  c,1\< | f,1 | aes,1\f | g,1 |
  g,1\p~ | g,1 |
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% EXPOSITION T1 + TRANSITION 15–48
expUpper = {
  % T1
  r8 g'8\f c''8 d''8 es''4.-> d''8 | c''8 b'8 c''4~ c''8 g'8 aes'8 b'8 |
  c''8 es''8 g''4~ g''8 f''8 es''8 d''8 | es''4. d''8 c''4 r4 |
  r8 c''8 f''8 g''8 aes''4.-> g''8 | f''8 e''8 f''4~ f''8 c''8 des''8 e''8 |
  f''8 aes''8 c'''4~ c'''8 bes''8 aes''8 g''8 | aes''4. g''8 f''4 r4 |
  r8 g'8\< c''8 d''8 es''8 f''8 g''8 aes''8 | b''4.-> aes''8 g''4 f''4 |
  r8 aes'8 d''8 es''8 f''8 g''8 aes''8 b''8 | d'''2.->\ff r4 |
  r8 g'8\f c''8 d''8 es''4.-> d''8 | c''8 b'8 c''4~ c''8 g'8 aes'8 b'8 |
  c''8 es''8 g''4~ g''8 aes''8 g''8 f''8 | es''8 d''8 c''8 b'8 c''4 g'4 |
  aes'4.-> g'8 f'4 d'4 | c'2 r2 |
  % transition
  es''8(\mf d''8 c''4) es''8( d''8 c''4) | aes''8( g''8 f''4) aes''8( g''8 f''4) |
  f''8( es''8 d''4) aes''8( g''8 f''4) | g''8( f''8 es''4) bes''8( aes''8 g''4) |
  bes''8(\< aes''8 g''4) es'''8( d'''8 c'''4) | c'''8( bes''8 aes''4) aes''8( g''8 f''4) |
  f''8( es''8 d''4) d''8( c''8 bes'4) | bes'4( aes'4 g'4 f'4) |
  bes''2.->\ff aes''8 g''8 | aes''2.-> g''8 f''8 | g''4 f''4 es''4 des''4 | des''1 |
  des''2(\> c''2) | c''2( bes'2) | bes'1\p~ | bes'2 r2 |
}
expMiddle = {
  \repeat unfold 4 { r8 <es' g'>8 } | \repeat unfold 2 { r8 <es' g'>8 } \repeat unfold 2 { r8 <d' f'>8 } |
  \repeat unfold 2 { r8 <es' g'>8 } \repeat unfold 2 { r8 <c' f'>8 } | r8 <c' f'>8 r8 <b d'>8 \repeat unfold 2 { r8 <c' es'>8 } |
  \repeat unfold 4 { r8 <aes' c''>8 } | \repeat unfold 2 { r8 <aes' c''>8 } \repeat unfold 2 { r8 <g' bes'>8 } |
  \repeat unfold 2 { r8 <aes' c''>8 } \repeat unfold 2 { r8 <f' bes'>8 } | r8 <f' bes'>8 r8 <e' g'>8 \repeat unfold 2 { r8 <f' aes'>8 } |
  \repeat unfold 4 { r8 <es' g'>8 } | \repeat unfold 4 { r8 <d' f'>8 } |
  \repeat unfold 4 { r8 <c' f'>8 } | <b d' f' aes'>2.-> r4 |
  \repeat unfold 4 { r8 <es' g'>8 } | \repeat unfold 2 { r8 <es' g'>8 } \repeat unfold 2 { r8 <d' f'>8 } |
  \repeat unfold 2 { r8 <es' g'>8 } \repeat unfold 2 { r8 <c' f'>8 } | r8 <es' g'>8 r8 <d' f'>8 r8 <es' g'>8 r8 <d' g'>8 |
  r8 <c' f'>8 r8 <c' f'>8 r8 <b d'>8 r8 <b d'>8 | <g c' es'>2 r2 |
  % transition
  <g c'>1 | <aes c'>1 | <aes d'>1 | <g bes>1 |
  <g bes>2 <g c'>2 | <aes c'>2 <aes es'>2 | <aes d'>1 | <aes d'>1 |
  <g bes des'>1 | <aes c'>1 | <g bes des'>1 | <g bes des'>1 |
  <g bes>1 | <g bes>1 | <g bes des'>1~ | <g bes des'>2 r2 |
}
expLower = {
  es1 | es2 d2 | es2 c2 | aes4 g4 g2 |
  aes1 | aes2 g2 | aes2 f2 | des4 c4 c2 |
  es1 | d1 | c1 | d2. r4 |
  es1 | es2 d2 | es2 c2 | g2 g2 |
  aes2 g2 | g2 r2 |
  % transition: imitation one beat behind the upper line
  r4 es'8( d'8 c'4) es'8( d'8 | c'4) aes'8( g'8 f'4) aes'8( g'8 |
  f'4) f'8( es'8 d'4) aes'8( g'8 | f'4) g'8( f'8 es'4) bes'8( aes'8 |
  g'4) bes8( aes8 g4) es'8( d'8 | c'4) c'8( bes8 aes4) aes8( g8 |
  f4) f8( es8 d4) d8( c8 | bes,4) r4 r2 |
  es'2.( des'4 | c'1) | bes2( aes2 | g1) |
  g1~ | g1 | g1~ | g2 r4 es4(\p |
}
expBass = {
  \repeat unfold 8 c,8 | \repeat unfold 8 c,8 |
  \repeat unfold 4 c,8 \repeat unfold 4 aes,,8 | f,,8 f,, g,, g,, \repeat unfold 4 c,8 |
  \repeat unfold 8 f,8 | \repeat unfold 8 f,8 |
  \repeat unfold 4 f,8 \repeat unfold 4 des,8 | bes,,8 bes,, c, c, \repeat unfold 4 f,8 |
  \repeat unfold 8 c,8 | \repeat unfold 8 g,,8 |
  \repeat unfold 8 aes,,8 | b,,2.-> r4 |
  \repeat unfold 8 c,8 | \repeat unfold 8 c,8 |
  \repeat unfold 4 c,8 \repeat unfold 4 aes,,8 | c,8 c, g,, g,, c, c, g,, g,, |
  f,,4 f,, g,, g,, | c,2 r2 |
  % transition
  c,1 | f,1 | bes,,1 | es,1 |
  es,2 c,2 | f,1 | bes,,1 | bes,,1 |
  es,1~ | es,1~ | es,1~ | es,1~ |
  es,1~ | es,1~ | es,1~ | es,2 r2 |
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% SECOND THEME 49–72
tTwoUpper = {
  R1*7 | r2. es'4(\p |
  c''2. bes'8 c''8 | des''4 aes''2 g''8 f''8 |
  es''2~ es''8 des''8 c''8 des''8 | es''2.) aes'4( |
  f''2.\< es''8 f''8 | ges''4 des'''2\f c'''8 bes''8 |
  aes''4 fes''2 es''8 des''8 | c''2~ c''8 bes'8 aes'8 bes'8 |
  ces''4 aes''2 ges''8 fes''8 | es''2. des''4 |
  c''2~ c''8 des''8 es''8 f''8 | g''4. aes''8 bes''4 des'''4 |
  c'''2.\> bes''8 aes''8 | aes''2~ aes''8 g''8 f''8 g''8 |
  aes''1\p~ | aes''2) r2 |
}
tTwoMiddle = {
  aes8\pp es' aes' c'' es'' c'' aes' es' | des'8 f' aes' c'' f'' c'' aes' f' |
  f8 c' es' aes' bes des' f' aes' | bes8 es' g' bes' des'' bes' g' es' |
  c'8 f' aes' c'' f'' c'' aes' f' | des'8 ges' bes' des'' ges'' des'' bes' ges' |
  es'8 aes' c'' es'' es' g' bes' des'' | aes8 es' aes' c'' es'' c'' aes' es' |
  es'1\p | f'2 g'2 | aes'2 f'2 | g'2. es'4 |
  c'2 f'2 | bes'2 ges'2 | fes'1 | es'1 |
  aes'2 fes'2 | fes'1 | es'1 | des'2 des'2 |
  c'2 es'2 | es'2 des'2 | c'1~ | c'2 r2 |
}
tTwoLower = {
  c'2.\mf bes8 c'8 | des'4 aes'2 g'8 f'8 |
  es'2~ es'8 des'8 c'8 des'8 | es'2.) aes4( |
  f'2. es'8 f'8 | ges'4 des''2 c''8 bes'8 |
  aes'2~ aes'8 g'8 f'8 g'8 | aes'1) |
  aes,8\pp es aes c' es' c' aes es | des8 aes c' f' aes' f' c' aes |
  f,8 c f aes bes, f bes des' | es8 g bes des' es' des' bes g |
  f,8 c f aes c' aes f c | ges,8 des ges bes des' bes ges des |
  des8 aes des' fes' aes' fes' des' aes | es8 aes c' es' aes' es' c' aes |
  fes8 ces' fes' aes' ces'' aes' fes' ces' | des8 fes aes bes des' bes aes fes |
  es8 aes c' es' aes' es' c' aes | es8 g bes des' g' des' bes g |
  aes,8 es aes c' es' c' aes es | des8 aes des' f' es g bes des' |
  aes,8 es aes c' es' c' aes es | aes,2 r2 |
}
tTwoBass = {
  aes,1\p | des,1 | f,2 bes,,2 | es,1 | f,1 | ges,1 | es,1 | aes,,1 |
  aes,,1 | des,1 | f,2 bes,,2 | es,1 | f,1 | ges,1 | des,1 | es,1 |
  fes,1 | des,1 | es,1 | es,1 | aes,,1 | des,2 es,2 | aes,,1~ | aes,,2 r2 |
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% CLOSING 73–80
closUpper = {
  r2 es''2(\pp | ces'''2. bes''4 | aes''2 fes''4. es''8) | es''1 | R1*4 |
}
closMiddle = {
  <c' es'>1\ppp | <ces' es'>1 | <ces' fes'>2 <des' g'>2 | <c' es'>1 |
  r2 es'2(\pp | ces''2. bes'4 | aes'2 fes'4. es'8) | es'1 |
}
closLower = {
  aes1\ppp~ | aes1~ | aes1~ | aes1 |
  <aes c'>1 | <aes ces'>1 | <aes ces'>2 <g des'>2 | <aes c'>1 |
}
closBass = {
  aes,,1\ppp~ | aes,,1~ | aes,,1~ | aes,,1~ | aes,,1~ | aes,,1~ | aes,,1~ | aes,,1 |
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% DEVELOPMENT 81–124
devUpper = {
  r8 es'8\mf aes'8 bes'8 ces''4.-> bes'8 | aes'8 g'8 aes'4~ aes'8 es'8 fes'8 g'8 |
  r8 b'8\< e''8 fis''8 g''4.-> fis''8 | e''8 dis''8 e''4~ e''8 b'8 c''8 dis''8 |
  r8 g''8\f c'''8 d'''8 es'''4.-> d'''8 | c'''8 b''8 c'''4~ c'''8 g''8 aes''8 b''8 |
  <b' d'' f'' aes''>4->\ff r4 <b' d'' f'' aes''>4-> r4 | R1 |
  R1*6 |
  r8 g''8\f c'''8 d'''8 es'''4.-> d'''8 | c'''8 b''8 c'''4~ c'''8 g''8 aes''8 b''8 |
  c'''8 g''8 es''8 c''8 r8 aes''8 f''8 d''8 | r8 b''8 g''8 d''8 r8 c'''8 aes''8 es''8 |
  r8 d'''8 b''8 f''8 r8 es'''8 c'''8 g''8 | f'''4-> es'''4-> d'''4-> c''4(\ff |
  aes''2. g''8 aes''8 | bes''4 f'''2 e'''8 des'''8 |
  c'''2~ c'''8 bes''8 aes''8 bes''8 | c'''2.) f''4( |
  des'''2. c'''8 des'''8 | es'''4 bes''2 aes''8 g''8 |
  f''2~ f''8 e''8 des''8 e''8 | f''1) |
  des'''2 c'''2 | b''2 aes''2 | g''1~ | g''1 |
  d'''1:32\ff | es'''1:32 | f'''1:32 | es'''1:32 |
  d'''1:32\fff | d'''1:32 | b''1:32 | g''1:32 |
  g''8 f'' es'' d'' c'' b' aes' g' | f'8 es' d' c' b g aes b |
  <g' b' d'' f''>4-> r4 <g' b' d'' f''>4-> r4 | <g' b' d'' f''>2.-> r4 |
}
devMiddle = {
  \repeat unfold 4 { r8 <ces' es'>8 } | \repeat unfold 2 { r8 <ces' es'>8 } \repeat unfold 2 { r8 <bes des'>8 } |
  \repeat unfold 4 { r8 <g' b'>8 } | \repeat unfold 2 { r8 <g' b'>8 } \repeat unfold 2 { r8 <fis' a'>8 } |
  \repeat unfold 4 { r8 <es'' g''>8 } | \repeat unfold 2 { r8 <es'' g''>8 } \repeat unfold 2 { r8 <d'' f''>8 } |
  <b d' f'>4-> r4 <b d' f'>4-> r4 | R1 |
  R1*4 |
  r8 d'8\f g'8 a'8 bes'4.-> a'8 | g'8 fis'8 g'4~ g'8 d'8 es'8 fis'8 |
  g'4 f'4 es'4 d'4 | c'8 d'8 es'8 f'8 g'4 a'4 |
  <es' g'>2 <d' f'>2 | <d' g'>2 <es' aes'>2 | <d' f'>2 <es' g'>2 | <c' f' aes'>2 <c' e' g'>2 |
  \repeat unfold 4 { r8 <c' f'>8 } | \repeat unfold 2 { r8 <des' f'>8 } \repeat unfold 2 { r8 <e' g'>8 } |
  \repeat unfold 2 { r8 <c' f'>8 } \repeat unfold 2 { r8 <des' f'>8 } | \repeat unfold 4 { r8 <e' bes'>8 } |
  \repeat unfold 4 { r8 <f' aes'>8 } | \repeat unfold 4 { r8 <g' bes'>8 } |
  \repeat unfold 2 { r8 <c' f'>8 } \repeat unfold 2 { r8 <e' g'>8 } | \repeat unfold 4 { r8 <c' f'>8 } |
  <f' aes'>1 | <f' aes'>1 | <b d' f'>1 | <b d' f'>1 |
  \repeat unfold 4 { r8 <b d'>8 } | \repeat unfold 4 { r8 <c' es'>8 } |
  \repeat unfold 4 { r8 <b d' f'>8 } | \repeat unfold 4 { r8 <c' es'>8 } |
  \repeat unfold 4 { r8 <c' es' aes'>8 } | \repeat unfold 4 { r8 <b d' f' aes'>8 } |
  \repeat unfold 4 { r8 <b d' f'>8 } | \repeat unfold 4 { r8 <b d' f'>8 } |
  <b d' f'>1 | <b d' f'>1 |
  <g b d'>4-> r4 <g b d'>4-> r4 | <g b d'>2.-> r4 |
}
devLower = {
  aes1 | aes2 g2 | e1 | e2 dis2 | c'1 | c'2 b2 |
  <g b>4-> r4 <g b>4-> r4 | R1 |
  R1*2 |
  r8 a8\f d'8 e'8 f'4.-> e'8 | d'8 cis'8 d'4~ d'8 a8 bes8 cis'8 |
  d'4 c'4 bes4 a4 | g8 a8 bes8 c'8 d'4 fis4 |
  es'1 | es'2 d'2 |
  c'4 r4 aes4 r4 | g4 r4 aes4 r4 | g4 r4 g4 r4 | aes2 bes2 |
  r8 c8 f8 g8 aes4.-> g8 | f8 e8 f4 r2 |
  r8 c8 f8 g8 aes4.-> g8 | f8 e8 f4 r2 |
  r8 des8 f8 aes8 bes4.-> aes8 | g8 fis8 g4 r2 |
  r8 c8 f8 g8 aes4.-> g8 | f8 e8 f4 r2 |
  aes1 | aes1 | g1 | g1 |
  g1\ff | es'1~ | es'2. d'4 | c'1 |
  aes1\fff~ | aes2. g4 | g1~ | g1 |
  g1 | g1 |
  <g b>4-> r4 <g b>4-> r4 | <g b>2.-> r4 |
}
devBass = {
  \repeat unfold 8 aes,,8 | \repeat unfold 4 aes,,8 \repeat unfold 4 es,8 |
  \repeat unfold 8 e,8 | \repeat unfold 4 e,8 \repeat unfold 4 b,,8 |
  \repeat unfold 8 c,8 | \repeat unfold 4 c,8 \repeat unfold 4 g,,8 |
  g,,4-> r4 g,,4-> r4 | R1 |
  r8 d,8\f g,8 a,8 bes,4.-> a,8 | g,8 fis,8 g,4~ g,8 d,8 es,8 fis,8 |
  d,4 c,4 bes,,4 a,,4 | g,,8 a,, bes,, c, d,4 a,,4 |
  g,,4 a,,4 bes,,4 c,4 | d,2 d,2 |
  c,1 | c,2 g,,2 |
  c,4 r4 d,4 r4 | g,,4 r4 aes,,4 r4 | b,,4 r4 c,4 r4 | c,2 c,2 |
  f,1 | bes,,2 c,2 | f,2 des,2 | c,1 |
  des,1 | es,1 | f,2 c,2 | f,1 |
  des,1 | des,1 | g,,1~ | g,,1~ |
  g,,1~ | g,,1~ | g,,1~ | g,,1~ |
  g,,1~ | g,,1~ | g,,1~ | g,,1 |
  g,,1 | g,,1 |
  g,,4-> r4 g,,4-> r4 | g,,2.-> r4 |
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% RECAPITULATION 125–152
recUpper = {
  r8 g'8\ff c''8 d''8 es''4.-> d''8 | c''8 b'8 c''4~ c''8 g'8 aes'8 b'8 |
  c''8 es''8 g''4~ g''8 f''8 es''8 d''8 | es''4. d''8 c''4 r4 |
  r8 g'8 c''8 d''8 es''4.-> d''8 | c''8 b'8 c''4~ c''8 g'8 aes'8 b'8 |
  c''8 es''8 g''4~ g''8 aes''8 g''8 f''8 | es''8\> d''8 c''8 b'8 c''4 g'4 |
  aes'4. g'8 f'4 d'4 | c'2\p r2 | R1 | r2. g'4(\p |
  e''2. d''8 e''8 | f''4 c'''2 b''8 a''8 |
  g''2~ g''8 f''8 e''8 f''8 | g''2.) c''4( |
  a''2.\< g''8 a''8 | bes''4 f'''2\ff e'''8 d'''8 |
  c'''4 aes''2 g''8 f''8 | e''2~ e''8 d''8 c''8 d''8 |
  es''4 c'''2 bes''8 aes''8 | g''2. f''4 |
  e''2~ e''8 f''8 g''8 a''8 | b''4. c'''8 d'''4 f'''4 |
  e'''2.\> d'''8 c'''8 | c'''2~ c'''8 b''8 a''8 b''8 |
  c'''1\mf~ | c'''2) r2 |
}
recMiddle = {
  \repeat unfold 4 { r8 <es' g'>8 } | \repeat unfold 2 { r8 <es' g'>8 } \repeat unfold 2 { r8 <d' f'>8 } |
  \repeat unfold 2 { r8 <es' g'>8 } \repeat unfold 2 { r8 <c' f'>8 } | r8 <c' f'>8 r8 <b d'>8 \repeat unfold 2 { r8 <c' es'>8 } |
  \repeat unfold 4 { r8 <es' g'>8 } | \repeat unfold 2 { r8 <es' g'>8 } \repeat unfold 2 { r8 <d' f'>8 } |
  \repeat unfold 2 { r8 <es' g'>8 } \repeat unfold 2 { r8 <c' f'>8 } | r8 <es' g'>8 r8 <d' f'>8 r8 <es' g'>8 r8 <d' g'>8 |
  r8 <c' f'>8 r8 <c' f'>8 r8 <b d'>8 r8 <b d'>8 | <g c' es'>2 r2 | <b d' f'>1\pp | <b d' f'>1 |
  g'1 | a'2 b'2 | c''2 a'2 | b'2. g'4 |
  e'2 a'2 | d''2 bes'2 | aes'1 | g'1 |
  c''2 aes'2 | aes'1 | g'1 | f'2 f'2 |
  e'2 g'2 | g'2 f'2 | e'1~ | e'2 r2 |
}
recLower = {
  es1 | es2 d2 | es2 c2 | aes4 g4 g2 |
  es1 | es2 d2 | es2 c2 | g2 g2 |
  aes2 g2 | g2 r2 | g1 | g1 |
  c8 g c' e' g' e' c' g | f,8 c e a c' a e c |
  a,8 e a c' d a d' f' | g8 b d' f' g' f' d' b |
  a,8 e a c' e' c' a e | bes,8 f bes d' f' d' bes f |
  f8 c' f' aes' c'' aes' f' c' | g8 c' e' g' c'' g' e' c' |
  aes,8 es aes c' es' c' aes es | f8 aes c' d' f' d' c' aes |
  g8 c' e' g' c'' g' e' c' | g8 b d' f' b' f' d' b |
  c8 g c' e' g' e' c' g | f8 c' f' a' g b d' f' |
  c8 g c' e' g' e' c' g | c2 r2 |
}
recBass = {
  \repeat unfold 8 c,8 | \repeat unfold 8 c,8 |
  \repeat unfold 4 c,8 \repeat unfold 4 aes,,8 | f,,8 f,, g,, g,, \repeat unfold 4 c,8 |
  \repeat unfold 8 c,8 | \repeat unfold 8 c,8 |
  \repeat unfold 4 c,8 \repeat unfold 4 aes,,8 | c,8 c, g,, g,, c, c, g,, g,, |
  f,,4 f,, g,, g,, | c,2 r2 | g,,1~ | g,,1 |
  c,1 | f,1 | a,2 d,2 | g,1 | a,1 | bes,1 | f,1 | g,1 |
  aes,1 | f,1 | g,1 | g,1 | c,1 | f,2 g,2 | c,1~ | c,2 r2 |
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% CODA 153–170
codaUpper = {
  R1*8 |
  r2 g'2(\pp | es''1~ | es''2. d''4 | c''1) | R1 |
  es''1\ppp~ | es''1 | d''1~ | d''1~ | d''1\fermata |
}
codaMiddle = {
  r2 g'2(\p | es''2. d''4 | c''2 aes'4. g'8) | g'1 |
  <c' es'>1\pp | <c' es'>1 | <c' f'>2 <b d'>2 | <c' es'>1 |
  <c' es'>1 | <c' es'>1 | <c' f'>2 <b f'>2 | <c' es'>1 | <g c'>1 |
  <g c'>1 | <g c'>1 | <g c'>1 | <g c'>1 | <g c'>1\fermata |
}
codaLower = {
  <e g>1\p | <es aes>1 | <des f>1 | <b, d f>1 |
  r2 g,2(\pp | es2. d4 | c2 aes,4. g,8) | g,1 |
  g1 | aes1 | aes2 g2 | g1 | es1 |
  es1~ | es1 | g1~ | g1~ | g1\fermata |
}
codaBass = {
  c,1\p | aes,,1 | des,1 | g,,1 |
  c,1\pp~ | c,1~ | c,1~ | c,1~ |
  c,1~ | c,1~ | c,1~ | c,1~ | c,1~ |
  c,1~ | c,1~ | c,1~ | c,1~ | c,1\fermata |
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ASSEMBLY
upper  = { \introUpper  \expUpper  \tTwoUpper  \closUpper  \devUpper  \recUpper  \codaUpper }
middle = { \introMiddle \expMiddle \tTwoMiddle \closMiddle \devMiddle \recMiddle \codaMiddle }
lower  = { \introLower  \expLower  \tTwoLower  \closLower  \devLower  \recLower  \codaLower }
bass   = { \introBass   \expBass   \tTwoBass   \closBass   \devBass   \recBass   \codaBass }

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
