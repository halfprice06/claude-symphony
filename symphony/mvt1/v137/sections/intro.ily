% INTRODUCTION, bars 1–14 (Lento). Concert pitch; Cb and Cbsn at sounding pitch.

introFluteOne = {
  R1*10 | r2 b'4(\mf\< aes''4~ | aes''2.)\f g''4~ | g''2\> r2\! |
  R1 |
}
introOboeOne = { R1*11 | c''2.\f c''4 | R1*2 | }
introOboeTwo = {
  R1*11 | fis'1\f | g'2\p r2 | R1 |
}
introClOne = { R1*10 | f'1\p\< | es'2.\f es'4 | R1*2 | }
introClTwo = { R1*10 | d'1\p\< | c'2.\f c'4 | R1*2 | }
introBassCl = {
  r2. g,4(\pp | es2.~\< es8\> d8) | c2(\! des4\< c4~\> | c1\!) |
  R1*10 |
}
introBsnOne = { R1*8 | g1\pp\< | aes1 | aes1 | c'2.\f c'4 | R1*2 | }
introBsnTwo = { R1*8 | c1\pp\< | f1 | d1 | aes,2.\f r4 | g,1\p~\> | g,2.\pp r4 | }
introHnOne = { R1*10 | f'1\p\< | es'2.\f es'4 | r4 es4(\mp c'2~ | c'4\> b2)\p r4 | }
introHnTwo = { R1*10 | d'1\p\< | c'2.\f c'4 | R1*2 | }
introHnThree = {
  R1*10 | \clef bass aes1\p\< | fis1\f | g2\p r2 |
  R1 \clef treble | % c115: return to treble at the end of the system, after the rests (Gould PDF 23)
}
introHnFour = { R1*10 | d1\p\< | aes,1\f | R1*2 | }
introTbnOne = {
  R1*11 | c'2.\mf c'4 | R1*2 |
}
introTbnTwo = {
  R1*11 | es2.\mf es4 | R1*2 |
}
introBassTbn = {
  R1*11 | aes,1\mf | R1*2 |
}
introTimp = {
  c1:32\ppp~^\markup \small "Timp. in G, A♭, C, E♭" | c1:32~ | c1:32~ | c1:32 |
  R1*6 | aes,1:32\pp\< | aes,2.:32\f r4 | g,1:32\p~ |
  << g,2.:32 { s2\> s4\pp } >> r4 |
}
introVlnOne = {
  R1*8 |
  r2. g'4(\mp\< | es''2.) aes'4( | f''2) b'4( aes''4~ | aes''2.)\f g''4~ | g''1\> | R1\! |
}
introVlnTwo = {
  R1*5 | es'1\pp | f'1\< | e'1\p\> |
  es'1\pp\< | f'2. c'4( | aes'2) f'2 | fis'1\f |
  g'1\p\> | f'2.\pp r4 |
}
introVla = {
  R1*5 | bes1\pp | des'1\< | c'1\p\> |
  c'1\pp\< | c'1 | d'1 | <c' es'>2.\f <c' es'>4 |
  es'2\p\>( d'2) | <g d'>2.\pp r4 |
}
introVc = {
  r2. g,4(\pp | es2.~\< es8\> d8) | c2(\! des4\< c4)~\> | c1\! |
  R1 | g1\pp | aes1\< | g1\p\> |
  g1\pp\< | aes1 | aes1 | c'2.\f c'4 |
  g1\p\> | g2.\pp r4 |
}
introCb = {
  r2. g,,4(\pp | es,2.~\< es,8\> d,8) | c,2(\! des,4\< c,4)~\> | c,1\! |
  % c097: div. in octaves at 6-7 so the bass is not two octaves below the next voice (Rimsky-Korsakov: bass rarely more than an octave from the part above)
  c,1\pp | <g,, g,>1^"div." | <f,, f,>1\< | c,1\p\>^"unis." |
  c,1\pp\< | f,1 | d,1 | aes,1\f |
  g,1\p~\> | g,2.\pp r4 |
}

introCorAnglais = {
  R1*4 | r2. d'4(\p\<^\markup \italic "espr." | bes'2.\>~ bes'8\! a'8 | g'2\< aes'4\> g'4~ |
  g'1\!) | R1*6 |
}