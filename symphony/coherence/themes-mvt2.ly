% THEME RECORD for movement II (Adagio, A flat), 3/4 sections: the current exported themes and quotations, NOT a lock.
% Proposed by critic 340 (release check, cyclic lens). Taken from mvt2/v340. Compared with a version by
%   python3 symphony/coherence/themecheck.py themes-mvt2.ly symphony/mvt2/vNN            (3/4 sections)
%   python3 symphony/coherence/themecheck.py themes-mvt2-b.ly symphony/mvt2/vNN --beats 4 (4/4 section, bars 37-64)
% Variables: absolute pitch, 3/4, bar 1 = the theme's first bar (leading rests give the beat). %@ lines: theme, part, bar, [notes [first note]].
\version "2.24.0"

% link: the five parts tied over from movement I's last chord (I 182); the cellos, violas and Vln II move at bar 2
linkVlnOne = { c''2. | c''2. | c''2. }
linkVlnTwo = { g'2. | aes'2. }
linkVla = { e'2. | es'2. }
linkVc = { c2. | aes,2. }

% themeA: Hn 1 solo 6 b3 - 14 (quoted by the scherzo's trio-tune span and movement I's horn call span E flat3-C4)
themeA = { r2 es8 f8 | aes4. c'8 es'4~ | es'4 d'4 des'4 | c'4. bes8 aes4 | g2 es8 f8 | aes4. c'8 f'4~ | f'4 bes'4 aes'4 | g'4 es'8 des'8 c'8 bes8 | aes2. }

% mottoTailBcl: B.cl. 31-34, movement I's motto tail at its own pitch and instrument (E flat3)
mottoTailBcl = { r4 es,8 f,8 aes,8 c8 | es2.~ | es4 d4 des4 | c2 bes,4 }
% mottoTailHn: Hn 1 alone 67-70 over the E flat pedal
mottoTailHn = { es'2. | d'4 des'4 c'4 | bes2. }
% timpAnswer: 84-85, E flat3-C3-A flat2 (theme A's arpeggio falling; motive x link to the scherzo's timpani at its bar 9)
timpAnswer = { es4. c8 aes,4 }
% lastTail: Cl 1 85-90, E flat5-D5-D flat5-C5 (answered by the scherzo's B-A sharp-A-G sharp and the finale's Ob 1 at the same pitch, IV 95-98)
lastTail = { es''2. | d''2. | des''2. | des''2. | c''2. }
% mixtureLine: F-F flat-E flat at 87-89 (C.a. at F4; Hn 4 and lower violas at F3; the finale's violas and Hn 2 quote it at F3, IV 197-198)
mixtureLine = { f'2. | fes'2. | es'2. }
mixtureLineLow = { f2. | fes2. | es2. }
% lastCommonTone: Vln II A flat4 87-92 (taken as G sharp4 by the scherzo's Hn 1) and Vln I C5 89-92 (the pitch movement I ended on)
lastAflat = { aes'2. | aes'2. | aes'2. }
lastC = { c''2. }

% ---- where each item must appear ----
%@ linkVlnOne VlnOne 1 1
%@ linkVlnTwo VlnTwo 1
%@ linkVla Vla 1
%@ linkVc Vc 1
%@ themeA HnOne 6
% Vln I: the solo violin ends its phrase on E flat5 at 22 b1, so the check starts on the A flat at 23 (22 notes from note 3)
%@ themeA VlnOne 23 22 3
%@ themeA VlnTwo 22
% theme A in the reprise: the violins change the last bar into the run to B flat6 at 78, so the first 17 notes are compared
%@ themeA VlnOne 70 17
%@ themeA VlnTwo 70 17
%@ mottoTailBcl BassCl 31
%@ mottoTailHn HnOne 67
%@ timpAnswer Timp 84
%@ lastTail ClOne 85
%@ mixtureLine CorAnglais 87
%@ mixtureLineLow HnFour 87
%@ lastAflat VlnTwo 87
%@ lastC VlnOne 89
