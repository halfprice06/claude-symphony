% SCHERZO, development, bars 57-104.
% 57-72: fugato on the head of theme A: Vc and Bn 1 in G minor (57), violas in D minor over the cellos' countersubject (61),
%   Vln II in A minor over the violas' countersubject (65), stretto in all strings 69-72 onto A major, ff (V of D minor).
% 73-88: F major, the Neapolitan of E (A major -> F major is a falling major third, the symphony's key relation). No strings:
%   the harp has the theme head as a melody 73-80 (still unused colour: a melodic harp line); Cl 1 dolce 81-88, from D minor to the
%   Neapolitan sixth over A (85-86, chromatic tail C-B-B flat) and vii7 of E over A (87-88).
% 89-104: retransition over the B pedal (pizzicato basses, timpani motive x), the head rising Vla -> Vln II -> Vln I; hemiola build 101-104.

sBFluteOne = { R2.*12 | a''4-.\f e''8-. e''-. a''4-. | c'''2->( b''8 bes''8 | a''4-.) b''-. cis'''-. | e'''2.->\ff | R2.*16 | R2.*12 | b''2\f a''4~ | a''4 fis''2 | dis'''2 b''4~ | b''4 a''2\ff | }
sBFluteTwo = { R2.*15 | a''2.->\ff | R2.*28 | fis''2.\f | fis''2. | fis''2. | dis''2.\ff | }
sBOboeOne = { R2.*8 | a''4-.\pp e''8-. e''-. a''4-. | c'''2->( b''8 bes''8 | a''4-.) e''8-. e''-. c''4-. | b'4-. gis'-. e'-. | a''4-.\f e''8-. e''-. a''4-. | c'''2->( b''8 bes''8 | a''4-.) b''-. cis'''-. | e'''2.->\ff | R2.*28 | b'2\f a'4~ | a'4 fis'2 | dis''2 b'4~ | b'4 a'2\ff | }
sBOboeTwo = { R2.*15 | cis'''2.->\ff | R2.*28 | dis''2.\f | dis''2. | dis''2. | b'2.\ff | }
sBClOne = { R2.*4 | d''4-.\pp a'8-. a'-. d''4-. | f''2->( e''8 es''8 | d''4-.) a'8-. a'-. f'4-. | e'4-. cis'-. a-. | R2.*4 | e''4-.\f b'8-. b'-. e''4-. | a''2->( gis''8 g''8 | fis''4-.) gis''-. a''-. | cis'''2.->\ff | a'2.\pp | a'2. | bes'2. | bes'2. | a'2. | a'2. | bes'2. | a'2. | d''4\p^\markup \italic "dolce" a'8 a' d''4 | f''2( e''8 d''8 | bes'4) g'8 g' bes'4 | a'2. | a'4 f'8 f' a'4 | c''2( b'8 bes'8 | a'4) fis'8 fis' dis'4 | fis'2. | R2.*12 | a'2\f fis'4~ | fis'4 dis'2 | fis'2 dis'4~ | dis'4 fis'2\ff | }
sBClTwo = { R2.*15 | a'2.->\ff | f'2.\pp | f'2. | d'2. | d'2. | c'2. | d'2. | e'2. | f'2. | f'2. | f'2. | g'2. | f'2. | f'2. | f'2. | dis'2. | dis'2. | R2.*12 | dis'2.\f | dis'2. | a'2. | a'2.\ff | }
sBBassCl = { R2.*16 | f,2.\pp | f,2. | g,2. | g,2. | a,2. | d,2. | e,2. | f,2. | d,2. | bes,,2. | g,2. | a,2. | a,2.~ | a,2.~ | a,2.~ | a,2. | R2.*16 | }
sBBsnOne = { g4-.\p d8-. d-. g4-. | bes2->( a8 aes8 | g4-.) d8-. d-. bes,4-. | a,4-. fis,-. d,-. | R2.*8 | a2.\f | a2. | a2. | a2.\ff | c'2.\pp | c'2. | bes2. | bes2. | c'2. | a2. | bes2. | c'2. | a2. | bes2. | bes2. | a2. | a2. | a2. | a2. | a2. | R2.*12 | b2.\f | a2. | b2. | a2.\ff | }
sBBsnTwo = { R2.*12 | a,2.\f | a,2. | a,2. | a,2.\ff | R2.*16 | R2.*12 | b,2.\f | b,2. | b,2. | b,2.\ff | }
sBCbsn = { R2.*12 | a,,2.\f | a,,2. | a,,2. | a,,2.\ff | R2.*28 | b,,2.\f | b,,2. | b,,2. | b,,2.\ff | }
sBHnOne = { R2.*14 | cis''2.\f | cis''2.\ff | R2.*28 | fis'2.\f | fis'2. | fis'2. | a'2.\ff | }
sBHnTwo = { R2.*14 | a'2.\f | a'2.\ff | R2.*28 | dis'2.\f | dis'2. | dis'2. | fis'2.\ff | }
sBHnThree = { R2.*16 | c'2.\pp^\markup \italic "senza sord." | c'2. | d'2. | d'2. | c'2. | d'2. | e'2. | c'2. | d'2. | d'2. | d'2. | c'2. | c'2. | c'2. | c'2. | c'2. | R2.*12 | b2.\f | b2. | b2. | b2.\ff | }
sBHnFour = { R2.*16 | f2.\pp^\markup \italic "senza sord." | f2. | g2. | g2. | f2. | f2. | g2. | f2. | f2. | f2. | g2. | f2. | a2. | a2. | a2. | a2. | R2.*12 | fis2.\f | fis2. | fis2. | fis2.\ff | }
sBTptOne = { R2.*44 | b'4-.\f b'8-. b'-. b'4-. | R2. | b'4-. b'8-. b'-. b'4-. | dis''2.\ff | }
sBTptTwo = { R2.*44 | fis'4-.\f fis'8-. fis'-. fis'4-. | R2. | fis'4-. fis'8-. fis'-. fis'4-. | a'2.\ff | }
sBTbnOne = { R2.*44 | fis2.\f | fis2. | a2. | a2.\ff | }
sBTbnTwo = { R2.*44 | dis2.\f | dis2. | fis2. | fis2.\ff | }
sBBassTbn = { R2.*44 | b,2.\f | b,2. | b,2. | b,2.\ff | }
sBTimp = { R2.*32 | b,4\pp b,8 b,8 b,4 | R2. | b,4 b,8 b,8 b,4 | R2. | b,4 b,8 b,8 b,4 | R2. | b,4 b,8 b,8 b,4 | R2. | b,4\p b,8 b,8 b,4 | R2. | b,4 b,8 b,8 b,4 | b,4 b,8 b,8 b,4 | b,2.:32\< | b,2.:32 | b,2.:32 | b,4 b,8 b,8 b,4\ff | }
sBHarpR = { R2.*16 | a''4\p f''4 a''4 | c'''2 bes''8 a''8 | g''4 d''4 g''4 | bes''2 a''8 g''8 | f''4 c''4 f''4 | a''2 g''8 f''8 | e''4 g''4 bes''4 | a''2. | r4 <d' f' a'>4 <d' f' a'>4 | r4 <d' f' bes'>4 <d' f' bes'>4 | r4 <d' g' bes'>4 <d' g' bes'>4 | r4 <c' f' a'>4 <c' f' a'>4 | r4 <c' f' a'>4 <c' f' a'>4 | r4 <c' f' a'>4 <c' f' a'>4 | R2. | R2. | R2.*16 | }
sBHarpL = { R2.*16 | f,4 <c f a>2 | f,4 <c f a>2 | g,4 <d g bes>2 | g,4 <d g bes>2 | a,4 <c f a>2 | d,4 <d f a>2 | e,4 <e g bes>2 | f,4 <c f a>2 | d,2. | bes,,2. | g,,2. | a,,2. | a,,2. | a,,2. | R2. | R2. | R2.*16 | }
sBVlnOne = { R2.*12 | a''4-.\f e''8-. e''-. a''4-. | c'''2->( b''8 bes''8 | a''4-.) b''-. cis'''-. | e'''2.->\ff | R2.*16 | R2.*8 | e''4-.\p\< b'8-. b'-. e''4-. | g''2->( fis''8 f''8 | e''4-.) b'8-. b'-. g''4-. | fis''4-. dis''-. b'-. | b''2\f a''4~ | a''4 fis''2 | dis'''2 b''4~ | b''4 a''2\ff | }
sBVlnTwo = { R2.*8 | a''4-.\p e''8-. e''-. a''4-. | c'''2->( b''8 bes''8 | a''4-.) e''8-. e''-. c''4-. | b'4-. gis'-. e'-. | e''4-. b'8-. b'-. e''4-. | a''2->( gis''8 g''8 | fis''4-.) gis''-. a''-. | cis'''2.->\ff | R2.*16 | R2.*4 | e''4-.\pp b'8-. b'-. e''4-. | a''2->( gis''8 g''8 | fis''4-.) r4 r4 | R2. | fis''4-.\p\< dis''-. b'-. | a'4-. fis'-. dis'-. | b'4-. fis'-. dis'-. | a'4-. fis'-. dis'-. | fis''2\f dis''4~ | dis''4 b'2 | fis''2 dis''4~ | dis''4 fis''2\ff | }
sBVla = { R2.*4 | d''4-.\p a'8-. a'-. d''4-. | f''2->( e''8 es''8 | d''4-.) a'8-. a'-. f'4-. | e'4-. cis'-. a-. | a'4( g' f' | e'2 d'4 | c'4 b a | b2 e'4) | c''4-.\f a'-. a'-. | e''2-> d''4-. | cis''4-. d''-. e''-. | a'2.->\ff | R2.*16 | e'4-.\pp b8-. b-. e'4-. | g'2->( fis'8 f'8 | e'4-.) r4 r4 | R2. | R2.*4 | b4-.\pp b-. b-. | b4-. b-. b-. | b4-.\< b-. b-. | b4-. b-. b-. | dis'2\f fis'4~ | fis'4 a'2 | b'2 fis'4~ | fis'4 dis'2\ff | }
sBVc = { g4-.\p^\markup \italic "arco" d8-. d-. g4-. | bes2->( a8 aes8 | g4-.) d8-. d-. bes,4-. | a,4-. fis,-. d,-. | d'4( c' bes | a2 g4 | f4 e d | a,2 e4) | a,2. | a,2. | d,2. | e,2. | a,4-.\f a-. a,-. | a,4-. a-. a,-. | a,4-. a-. a,-. | a,2.->\ff | R2.*16 | b,4\pp^\markup \italic "pizz." r4 r4 | b,4 r4 r4 | b,4 r4 r4 | b,4 r4 r4 | b,4 r4 r4 | b,4 r4 r4 | b,4 r4 r4 | b,4 r4 r4 | b,4 r4 r4 | b,4 r4 r4 | b,4 r4 r4 | b,4 r4 r4 | b,2\f^\markup \italic "arco" b,4~ | b,4 b,2 | b,2 b,4~ | b,4 b,2\ff | }
sBCb = { R2.*8 | a,,2.\p | a,,2. | d,2. | e,,2. | a,,4-.\f r4 r4 | a,,4-. r4 r4 | a,,4-. r4 r4 | a,,2.->\ff | R2.*16 | b,,4\pp^\markup \italic "pizz." r4 r4 | b,,4 r4 r4 | b,,4 r4 r4 | b,,4 r4 r4 | b,,4 r4 r4 | b,,4 r4 r4 | b,,4 r4 r4 | b,,4 r4 r4 | b,,4 r4 r4 | b,,4 r4 r4 | b,,4 r4 r4 | b,,4 r4 r4 | b,,2\f^\markup \italic "arco" b,,4~ | b,,4 b,,2 | b,,2 b,,4~ | b,,4 b,,2\ff | }
