% Finale (movement IV) record of its scherzo quotations, as they appear in the finale (2/2, compare with --beats 4).
% Owner: finale thread. Compare by eye with themes-scherzo.ly each cycle; run
%   python3 themecheck.py themes-finale-quotes.ly ../mvt3/vNN --beats 4
% motiveXretr: the scherzo's motive x in its retransition form (scherzo v04 Timp 241, 243, 249, 251, 253-255; at scherzo v24 the statements are at 241 and 249: b,4 b,8 b,8 b,4),
% transposed down a major third, finale Timp 143-145 (on the dominant G before the recapitulation).
motiveXretr = { g,4 g,8 g,8 g,4 r4 }

%@ motiveXretr Timp 143 4
%@ motiveXretr Timp 144 4

% c029 proposal: scherzoHeadC: the scherzo's theme A head (scherzo VlnOne 13: e''4 b'8 b'8 e''4 | g''2 fis''8 f''8 | e''4), transposed to C
% and turned to major (its G becomes E natural), note values kept, rebarred in 2/2 (starts on beat 1 of finale 275). Tpt 1-2, Cl 1, Fl 1 (8va), Hn 1-2 (8vb).
scherzoHeadC = { c''4 g'8 g'8 c''4 e''4~ | e''4 d''8 des''8 c''4 r4 }

%@ scherzoHeadC TptOne 275
%@ scherzoHeadC TptTwo 275
%@ scherzoHeadC ClOne 275
%@ scherzoHeadC FluteOne 275
%@ scherzoHeadC VlnOne 275

% ---- c030 proposal: movement I and movement II quotations as they stand in the finale (v30 + c030), 2/2, --beats 4 ----
% Same purpose as the scherzo entries: any later finale cycle that alters one of these is reported by themecheck.py.
% Source and transposition of each are listed in critics/reports/c030.md and coherence/finale.md.
% mvtOneHammeredHead: movement I 27-28 (VlnOne), same pitch, C minor; finale 199-200
mvtOneHammeredHead = { r8 g''8 es'''4. d'''8 des'''8 c'''8 | c'''4 b''8 c'''8 aes''4. g''8 }
% mvtOneHammeredTenor: movement I 27-32 Vc/Bsn 1 tenor line, same pitch; finale 199-204
mvtOneHammeredTenor = { c'2 es'2 | d'2 f'2 | es'2 c'2 | e'2 bes2 | aes2 f2 | g4 g,4 r2 }
% mvtTwoThemeB: movement II 41-44 (C.a., second phrase of theme B), note values doubled, an octave higher, ending held on D flat; finale 211-218
mvtTwoThemeB = { aes'2 des''2 | f''2. ges''4 | aes''2 bes''4 aes''4 | ges''2. f''4 | es''2. f''4 | des''1~ | des''1~ | des''1 }
% choraleFirst: movement I 175-179 top line in major (G E D C D flat C); finale 224-228 Tpt 1 (Tbn 1 an octave lower), canon Vln I/II 226-230
choraleFirst = { g'1 | e''1 | d''1 | c''2 des''2 | c''1 }
% timpaniPulse: movement I 179-180, same pitch; finale 229-230
timpaniPulse = { c4 r8 g,8 c4 r4 | c4 r8 g,8 c4 r4 }
% sHeadViolins: movement I v99 155-159 (withheld S head), same pitch; finale 235-238 (its pickup G4 at 234 is not checked)
sHeadViolins = { e''2.~ e''8 d''8 | c''4 a''2 g''4 | f''4. e''8 d''4 f''8 a''8 | c'''2 b''2 }
% sCounter: movement I v99 156-159 (Cl 1 + Hn 2), same pitch; finale 235-238
sCounter = { r4 c''4 b'4 bes'4 | a'2 c''2~ | c''4 bes'4 a'2 | g'2 f'2 }
% sBass: movement I v99 156-159 bass (Bsn 1 pitch); finale 235-238 Vc
sBass = { c1 | c1 | d2 f,2 | g,1 }
% hornCallMajor: movement I 13-14 (Hn 1 E flat3-C4-B3) in major, resolved; finale 243-246 Tpt 1 (Tpt 2, Hn 1 lower octaves; Hn 2 at movement I's pitch)
hornCallMajor = { e''2 c'''2~ | c'''4 b''2.~ | b''2 c'''2~ | c'''1 }
% pHeadMajor: movement I 15-16 head in C major, an octave higher; finale 247-248
pHeadMajor = { r8 g''8 e'''4. d'''8 des'''8 c'''8 | c'''4 b''8 c'''8 a''4. g''8 }
% sHeadBrass: movement I 146-150 (Hn 1 + Vla), Tpt 1 an octave higher; finale 247-250 (pickup G3 at 246 in Hn 2, Cl 1, Vla since c030)
sHeadBrass = { e''2.~ e''8 d''8 | c''4 a''2 g''4 | f''4. e''8 d''4 f''8 a''8 | c'''2 b''2 }
% choraleLast: the major motto with B before C, doubled values; finale 255-264 Tpt 1 (Fl 1, Vln I an octave higher)
choraleLast = { g'1~ | g'1 | e''1~ | e''1 | d''1~ | d''1 | c''1 | b'1 | c''1~ | c''1 }

%@ mvtOneHammeredHead VlnOne 199
%@ mvtOneHammeredHead FluteOne 199
%@ mvtOneHammeredHead Vla 199
%@ mvtOneHammeredTenor Vc 199
%@ mvtOneHammeredTenor BsnOne 199
%@ mvtTwoThemeB TptOne 211
%@ mvtTwoThemeB FluteOne 211
%@ mvtTwoThemeB OboeOne 211
%@ mvtTwoThemeB ClOne 211
%@ choraleFirst TptOne 224
%@ choraleFirst TbnOne 224
%@ choraleFirst VlnOne 226
%@ timpaniPulse Timp 229
%@ sHeadViolins VlnOne 235
%@ sHeadViolins VlnTwo 235
%@ sCounter ClOne 235
%@ sCounter Vla 235
%@ sBass Vc 235
%@ hornCallMajor TptOne 243
%@ hornCallMajor HnTwo 243
%@ pHeadMajor VlnOne 247
%@ pHeadMajor FluteOne 247
%@ pHeadMajor TbnOne 247
%@ pHeadMajor TbnTwo 247
%@ sHeadBrass TptOne 247
%@ sHeadBrass HnOne 247
%@ sHeadBrass Vla 247
%@ choraleLast TptOne 255
%@ choraleLast VlnOne 255
