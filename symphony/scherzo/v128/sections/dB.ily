% DEVELOPMENT, shortened, bars 289-304: fugato entries in G minor (cellos, 289) and D minor (violas over the countersubject, 293),
% c035: 297 Fl 1/Ob 1 print "1."; 299 Bn 1 crescendo from the downbeat with Bn 2 (one hairpin on the shared staff).
% stretto onto A major ff (297-300 = 69-72), then straight to the hemiola on V7 (301-304 = 101-104). The F major episode is not repeated.

% c097: 297-300 the stretto at one-bar distance, as 69-72 (see sB.ily).
% c126: 300 Fl, Ob, Cl, Bn 2, Cbn and Hn 1-2 end the ff chord on beat 2 and breathe before the p of 301, as Bn 1 has since c086 and as the winds rest at 73
%   (Adler I PDF 175, 198: the oboe must exhale and needs frequent rests; PDF 188: the flute needs breath; PDF 174: dynamics are hardest to control after the top register). The strings hold beat 3.
dBFluteOne = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | a''4-.\f^\markup \bold "1." e''8-. e''-. a''4-. | c'''2->( b''8 bes''8 | a''4-.) b''-.\< cis'''-. | e'''2->\ff r4 | b''2\p\< a''4~ | a''4 fis''2 | dis'''2 b''4~ | b''4 a''2-\tweak stencil ##f \ff | }
dBFluteTwo = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | a''2->\ff r4 | fis''2.\p\< | fis''2. | fis''2. | fis''2.\ff | }
dBOboeOne = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | a''4-.\f^\markup \bold "1." e''8-. e''-. a''4-. | c'''2->( b''8 bes''8 | a''4-.) b''-.\< cis'''-. | cis'''2->\ff r4 | dis''2.\p\< | dis''2. | dis''2. | dis''2.\ff | }
% c014: 308 Ob 2 F sharp 5 and Cl 2 A5 above Tpt 1's D sharp 5, so the woodwind harmony lies above the trumpets (Rimsky-Korsakov PDF 110-111)
dBOboeTwo = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | a''2->\ff r4 | b'2\p\< a'4~ | a'4 fis'2 | dis''2 b'4~ | b'4 a'2-\tweak stencil ##f \ff | }
dBCorAnglais = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | }
dBClOne = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | e''4-.\f b'8-. b'-. e''4-. | fis''4-. gis''-.\< a''-. | cis'''2->\ff r4 | a'2\p\< fis'4~ | fis'4 dis'2 | a'2. | a''2.\ff | }
dBClTwo = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | a'2->\ff r4 | dis'2.\p\< | dis'2. | fis'2 dis'4~ | dis'4 fis'2-\tweak stencil ##f \ff | }
dBBassCl = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | }
% c086: 300 Bsn 1 ends on beat 2 (as at 72) and breathes before the sub. p of 301: from 297 to 320 it otherwise played 24 bars of f-ff with no rest (Sebesky PDF 24, 70).
dBBsnOne = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | a2.\f | e2. | a4-.\< e8-. e-. a4-. | a2\ff r4 | b2.\p\< | a2. | b2. | a2.\ff | }
dBBsnTwo = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | a,2.\f | a,2. | a,2.\< | a,2\ff r4 | b,2.\p\< | b,2. | b,2. | b,2.\ff | }
dBCbsn = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | a,,2.\f | a,,2. | a,,2.\< | a,,2\ff r4 | b,,2.\p\< | b,,2. | b,,2. | b,,2.\ff | }
dBHnOne = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | a'4-.\f\< e'8-. e'-. a'4-. | cis''2\ff r4 | fis'2.\p\< | fis'2. | fis'2. | fis'2.\ff | }
dBHnTwo = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | a'4-.\f\< e'8-. e'-. a'4-. | a'2\ff r4 | dis'2.\p\< | dis'2. | dis'2. | dis'2.\ff | }
dBHnThree = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | b2.\p\< | b2. | b2. | b2.\ff | }
dBHnFour = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | \tag #'score \clef bass fis2.\p\< | fis2. | fis2. | fis2.\ff | }
dBTptOne = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | b'4-.\pp\< b'8-. b'-. b'4-. | R2. | b'4-. b'8-. b'-. b'4-. | dis''2.\ff | }
dBTptTwo = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | fis'4-.\pp\< fis'8-. fis'-. fis'4-. | R2. | fis'4-. fis'8-. fis'-. fis'4-. | fis'2.\ff | }
dBTptThree = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | }
% c033: trombones and tuba rest through the reprise (289-324): the low brass play 101-120 and return fresh at the coda's 333 after 212 bars (Rimsky-Korsakov PDF 136, economy of colour; PDF 119, partial tutti: horns and trumpets). Dvorak 9/iii has no trombones at all.
dBTbnOne = { R2.*16 | }
dBTbnTwo = { R2.*16 | }
dBBassTbn = { R2.*16 | }
dBTuba = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | }
dBTimp = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | b,2.:32\p\<~ | b,2.:32~ | b,2.:32 | b,4\ff b,8 b,8 b,4 | }
dBHarpR = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | }
dBHarpL = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | }
dBVlnOne = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | a''4-.\f e''8-. e''-. a''4-. | c'''2->( b''8 bes''8 | a''4-.) b''-.\< cis'''-. | e'''2->\ff\dnb~ e'''4\upbow | b''2\sfp\< a''4~ | a''4 fis''2 | dis'''2 b''4~ | b''4 a''2\ff | }
% c044: 300 strings in double stops on the ff A-major chord, as at 72 (Adler II PDF 161, 164)
% c101: 301-304 Vln II on the hemiola melody's lower octave, as at 101-104 (Rimsky-Korsakov PDF 58-59, 62).
dBVlnTwo = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | e''4-.\f\dnb b'8-. b'-. e''4-. | fis''4-. gis''-.\< a''-. | <e'' cis'''>2->\ff\dnb~ <e'' cis'''>4\upbow | b'2\sfp\< a'4~ | a'4 fis'2 | dis''2 b'4~ | b'4 a'2\ff | }
% c073: 296 violas E4-B3-G sharp 3 and cellos E3-B2 (were E4-C sharp 4-A3 over A2-E3, V of D): the 4-bar cut of the fugato (exposition 65-68) had joined
%   V of D minor straight to the A-minor stretto at 297, so the top voice's leading tone C sharp went to C natural and the f entry came without its dominant.
%   Now 296 is V of A, as 68 is before 69 (Aldwell-Schachter PDF 93: V-I harmonic and contrapuntal motion; PDF 97: V that creates the expectation of I;
%   PDF 100: the leading tone in the top voice goes to the tonic; PDF 129: root-position V before the arrival). The subject's last bar now leads to the next key.
dBVla = { R2. | R2. | R2. | R2. | d''4-.\p a'8-. a'-. d''4-. | f''2->( e''8 es''8 | d''4-.)\< a'8-. a'-. f'4-. | e'4-. b-. gis-. | c''4-.\f a'-. a'-. | e''2->\dnb d''4-. | cis''4-. d''-.\< e''-. | <e' a'>2->\ff\dnb~ <e' a'>4\upbow | dis'2\sfp\< fis'4~ | fis'4 a'2 | b'2 fis'4~ | fis'4 dis'2\ff | }
% c017: 302-303 Vc with Bsn 1 take motive x a bar after Vln I (stretto in the bass) over the A pedal, as at 70-71 (Adler PDF 175-176)
dBVc = { g4-.\p d8-. d-. g4-. | bes2->( a8 aes8 | g4-.) d8-. d-. bes,4-. | a,4-. fis,-. d,-. | d'4(\pp c' bes | a4 bes g) | f4(\< e d | e2 b,4) | a,4-.\f a-. a-. | e2.-- | a4-. e8-.\< e-. a4-. | <a, e>2->\ff\dnb~ <a, e>4\upbow | b,2\sfp\< b,4~ | b,4 b,2 | b,2 b,4~ | b,4 b,2\ff | }
dBCb = { R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2. | a,,4-.\f r4 r4 | a,,4-. r4 r4 | a,,4-.\< r4 r4 | a,,2->\ff\dnb~ a,,4\upbow | b,,2\sfp\< b,,4~ | b,,4 b,,2 | b,,2 b,,4~ | b,,4 b,,2\ff | }
% c115: 301-320 the Horns 3·4 staff in bass clef (score only; \tag #'score is dropped from the parts). Since c114, Hn 4 holds the bass an octave up at 305-320 down to A2/B2: five ledger lines under the treble stave, its rests and breath hung four spaces below it. Gould, Behind Bars PDF 46-47: use about three ledger lines, then change clef; brass never take octave signs; PDF 51: rests sit at the level of the surrounding pitches. Clef back to treble at 321 (dC.ily).
