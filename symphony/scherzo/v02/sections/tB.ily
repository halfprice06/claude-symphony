% TRIO, middle part, bars 185-216.
% 185-200: call and response between a woodwind and the cellos: Ob 1 in C sharp minor (185), the cellos answer (189);
%   Ob 1 and cor anglais in B major (193), the cellos answer (197).
% 201-208: the strings together, crescendo to the trio's forte: the oboe's call in C sharp minor in Vln I and II, ending on G sharp (V of C sharp).
% 209-216: A major, then A minor (mixture, iv), to the dominant pedal B; T's head in Cl 1 and Fl 1, diminuendo.

tBFluteOne = { R2.*24 | R2.*4 | gis''2(\pp a''4 | b''2.~ | b''2.~ | b''2) r4 | }
tBFluteTwo = { R2.*20 | cis''2.\f | cis''2. | cis''2. | bis'2. | R2.*8 | }
tBOboeOne = { e''2(\p dis''4 | cis''2 gis'4) | a'4.( b'8 cis''4) | gis'2. | R2.*4 | dis''2( cis''4 | b'2 fis'4) | gis'4.( a'8 b'4) | fis'2. | R2.*4 | R2.*4 | e''2(\f dis''4 | cis''2 gis'4) | a'4.( b'8 cis''4) | gis'2. | R2.*8 | }
tBOboeTwo = { R2.*20 | gis'2.\f | gis'2. | fis'2. | gis'2. | R2.*8 | }
tBCorAnglais = { R2.*8 | dis'2( cis'4 | b2 fis4) | gis4.( a8 b4) | fis2. | R2.*20 | }
tBClOne = { R2.*16 | a'2.\p\< | cis''2. | b'2. | a'2. | e''2.\f | e''2. | cis''2. | dis''2. | R2.*4 | gis'2(\p a'4 | b'2.~ | b'2.~ | b'2) r4 | }
tBClTwo = { R2.*16 | fis'2.\p\< | fis'2. | e'2. | dis'2. | gis'2.\f | gis'2. | a'2. | gis'2. | e'2.\p | e'2. | dis'2.\> | dis'2. | dis'2.\! | dis'2. | dis'2. | dis'2. | }
tBBsnOne = { R2.*16 | a2.\p\< | a2. | gis2. | fis2. | gis2.\f | gis2. | fis2. | bis,2. | cis'2.\p | c'2. | b2.\> | a2. | fis2.\! | fis2. | fis2. | fis2. | }
tBBsnTwo = { R2.*20 | cis2.\f | cis2. | fis,2. | gis,2. | a,2.\p | a,2. | b,2. | b,2. | R2.*4 | }
tBHnOne = { R2.*20 | gis'2.\f | gis'2. | a'2. | gis'2. | R2.*8 | }
tBHnTwo = { R2.*20 | e'2.\f | e'2. | fis'2. | dis'2. | R2.*8 | }
tBHnThree = { R2.*24 | e'2.\p | e'2. | dis'2.\> | dis'2. | dis'2.\! | dis'2. | dis'2. | dis'2. | }
tBHnFour = { R2.*24 | cis'2.\p | c'2. | b2.\> | b2. | b2.\! | b2. | b2. | b2. | }
tBTimp = { R2.*28 | b,2.:32\pp | b,2.:32 | b,2.:32 | b,4 r4 r4 | }
tBHarpR = { r4 <gis cis' e'>4 <gis cis' e'>4 | r4 <gis cis' e'>4 <gis cis' e'>4 | r4 <a cis' fis'>4 <a cis' fis'>4 | r4 <gis bis dis'>4 <gis bis dis'>4 | r4 <gis cis' e'>4 <gis cis' e'>4 | r4 <gis cis' e'>4 <gis cis' e'>4 | r4 <a cis' fis'>4 <a cis' fis'>4 | r4 <gis bis dis'>4 <gis bis dis'>4 | r4 <b dis' fis'>4 <b dis' fis'>4 | r4 <b dis' fis'>4 <b dis' fis'>4 | r4 <gis b e'>4 <gis b e'>4 | r4 <ais cis' fis'>4 <ais cis' fis'>4 | r4 <b dis' fis'>4 <b dis' fis'>4 | r4 <b dis' fis'>4 <b dis' fis'>4 | r4 <gis b e'>4 <gis b e'>4 | r4 <ais cis' fis'>4 <ais cis' fis'>4 | R2.*16 | }
tBHarpL = { cis,4 r4 r4 | cis,4 r4 r4 | fis,,4 r4 r4 | gis,,4 r4 r4 | cis,4 r4 r4 | cis,4 r4 r4 | fis,,4 r4 r4 | gis,,4 r4 r4 | b,,4 r4 r4 | b,,4 r4 r4 | e,4 r4 r4 | fis,,4 r4 r4 | b,,4 r4 r4 | b,,4 r4 r4 | e,4 r4 r4 | fis,,4 r4 r4 | R2.*16 | }
tBVlnOne = { R2.*16 | fis''2(\< gis''4 | a''2 cis'''4) | b''4.( a''8 gis''4) | fis''2. | e'''2(\f dis'''4 | cis'''2 gis''4) | a''4.( b''8 cis'''4) | gis''2. | a'4--\p r4 r4 | c''4-- r4 r4 | R2.*6 | }
tBVlnTwo = { R2.*16 | fis'2(\< gis'4 | a'2 cis''4) | b'4.( a'8 gis'4) | fis'2. | e''2(\f dis''4 | cis''2 gis'4) | a'4.( b'8 cis''4) | gis'2. | cis'4--\p r4 r4 | e'4-- r4 r4 | R2.*6 | }
tBVla = { R2.*16 | a2.\p\< | a2. | gis2. | a2. | cis'2.\f | cis'2. | cis'2. | bis2. | e'2.\p | e'2. | fis'2.\> | fis'2. | fis'2.\! | fis'2. | fis'2. | fis'2. | }
tBVc = { R2.*4 | e2(\p dis4 | cis2 gis,4) | a,4.( b,8 cis4) | gis,2. | R2.*4 | dis2( cis4 | b,2 fis,4) | gis,4.( a,8 b,4) | fis,2. | fis,2.\p\<^\markup \italic "arco" | fis,2. | gis,2. | b,2. | cis2.\f | cis2. | fis,2. | gis,2. | a,2.\p | a,2. | b,2. | b,2. | b,2. | b,2. | b,2. | b,2. | }
tBCb = { cis,4 r4 r4 | cis,4 r4 r4 | fis,,4 r4 r4 | gis,,4 r4 r4 | cis,4 r4 r4 | cis,4 r4 r4 | fis,,4 r4 r4 | gis,,4 r4 r4 | b,,4 r4 r4 | b,,4 r4 r4 | e,4 r4 r4 | fis,,4 r4 r4 | b,,4 r4 r4 | b,,4 r4 r4 | e,4 r4 r4 | fis,,4 r4 r4 | fis,,2.\p\<^\markup \italic "arco" | fis,,2. | gis,,2. | b,,2. | cis,2.\f | cis,2. | fis,,2. | gis,,2. | a,,2.\p | a,,2. | b,,2. | b,,2. | b,,4^\markup \italic "pizz." r4 r4 | b,,4 r4 r4 | b,,4 r4 r4 | b,,4 r4 r4 | }
