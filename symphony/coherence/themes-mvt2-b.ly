% THEME RECORD for movement II, 4/4 section (bars 37-64): theme B and the two quotations of movement I. NOT a lock.
% Proposed by critic 340; taken from mvt2/v340. Run with --beats 4 (see themes-mvt2.ly). Same conventions as themes-mvt2.ly.
% Needs lyparse.py with lyparse-c340.patch (scales \tuplet durations; skips quoted Scheme lists and \shape's grob name).
\version "2.24.0"

% themeBone: first phrase, Fl 1 37-40 (pickup C5 in the C.a. at 36)
themeBone = { f''2 ges''8 f''8 es''4 | des''4 c''8 des''8 es''2 | ges''4 \tuplet 3/2 4 { f''8 ges'' f'' } es''4 des''4 | c''4 des''8 c''8 bes'2 }
% themeBtwo: second phrase, C.a. 41-44 (quoted by the finale at IV 211-218, Tpt 1 + Ob 1 + Cl 1, doubled values; Hn 1.2 at 217-218 at this pitch)
themeBtwo = { aes4 des'4 f'4. ges'8 | aes'4 bes'8 aes'8 ges'4~ ges'8 f'8 | es'4. f'8 des'4 bes4 | c'2. }
% themeBtwoBuild: the second phrase as the build plays it, 57-60 (A flat held over the barline, no B flat neighbour)
themeBtwoBuild = { aes'4 des''4 f''4. ges''8 | aes''4. ges''8~ ges''4~ ges''8 f''8 | es''4. f''8 des''4 bes'4 | c''1 }
% themeBminor: head in B flat minor, Ob 1 44 b4 - 47
themeBminor = { r2 r4 aes'4 | des''2 es''8 des''8 c''4 | bes'4 a'8 bes'8 des''2 | cis''2. }
% quoteS: movement I's second-theme head in minor with its pickup (rhythm 4 | 2.~ 8 8 | 4 2 4), C.a. 47 b4 - 50; heard once
quoteS = { r2 r4 cis'4 | a'2.~ a'8 gis'8 | fis'4 d''2 cis''4 | cis''2 b'4 a'4 }
% quoteP: movement I's first-theme head, Tbn 1 alone, ff, A minor, 63-64; heard once
quoteP = { r8 e8 c'4. b8 bes8 a8 | a4 gis8 a8 f4. e8 }

%@ themeBone FluteOne 37
%@ themeBtwo CorAnglais 41
%@ themeBminor OboeOne 44
%@ quoteS CorAnglais 47
%@ quoteP TbnOne 63
% theme B in the violins (pickup C5 at 52 b4), first phrase 53-56
%@ themeBone VlnOne 53
%@ themeBone VlnTwo 53
% second phrase at the build, 57-60, in octaves (Vln I A flat5 ..., Vln II and Ob 1 an octave lower, Fl 1 above): the varied form,
% A flat held over the barline without the B flat neighbour (12 notes)
%@ themeBtwoBuild VlnOne 57 12
%@ themeBtwoBuild VlnTwo 57 12
%@ themeBtwoBuild OboeOne 57 12
%@ themeBtwoBuild FluteOne 57 12
