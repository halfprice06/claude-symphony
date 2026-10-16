% THEME RECORD for the scherzo (movement III): the current themes, NOT a lock (Dan, 2026-10-12: the themes are not locked
% and may evolve under the critics). Taken from scherzo/v04; hornCall refreshed from v31, trioT from v12. Only the scherzo thread edits this file; it refreshes it after any
% promotion that changes a theme (coherence/makelock.py, then the %@ lines) and sends the finale thread the old and new notes.
% Compared with each new version by symphony/coherence/themecheck.py (run in scherzo/kit/promote.sh; reports only).
% Variables: absolute pitch, 3/4, bar 1 = the theme's first bar. %@ lines: theme, part, bar, [notes [first note]].
\version "2.24.0"

% hornCall: v31 HnOne bars 1-7 (rising sixth since v11; since v31 it stops on the leading tone D sharp, unresolved as in movement I)
hornCall = { gis'2.~ | gis'2. | gis2. | e'2. | dis'2.~ | dis'2 r4 }

% motiveX: v04 Timp bars 9-12
motiveX = { b,4 b,8 b,8 g,4 | e,4 r2 | b,4 b,8 b,8 e4 | e,4 r2 }

% themeA: v04 VlnOne bars 13-28
themeA = { e''4 b'8 b'8 e''4 | g''2 fis''8 f''8 | e''4 b'8 b'8 g'4 | fis'4 dis'4 b4 | e''4 b'8 b'8 e''4 | a''2 gis''8 g''8 | fis''4 dis''8 dis''8 b'4 | e''4 r2 | a''4 g''4 fis''4 | e''4 dis''8 dis''8 e''4 | fis''4 g''8 a''8 b''4 | c'''2 b''8 fis''8 | e''4 b'8 b'8 e''4 | g''2 fis''8 f''8 | e''4 dis''8 dis''8 fis''4 | e''4 r2 }

% secondIdeaG: v32 VlnOne bars 45-56 (since v32 each two-bar answer ends dotted crotchet + quaver)
secondIdeaG = { d'''2 b''4~ | b''4 g'''2 | fis'''2 e'''4~ | e'''4 d'''4. e'''8 | e'''2 cis'''4~ | cis'''4 a'''2 | g'''2 fis'''4~ | fis'''4 e'''4. d'''8 | d'''4 b''4 g''4 | a''2 fis''4 | a''4 g''2 | g''4 r2 }

% secondIdeaE: v32 VlnOne bars 277-288 (same change)
secondIdeaE = { b''2 g''4~ | g''4 e'''2 | dis'''2 cis'''4~ | cis'''4 b''4. d'''8 | c'''2 a''4~ | a''4 fis'''2 | e'''2 dis'''4~ | dis'''4 b''4. cis'''8 | b''4 g''4 e''4 | fis''2 dis''4 | fis''4 e''2 | e''4 r2 }

% trioT: v12 ClOne bars 153-167 (since v12 the third phrase peaks on A5 in bar 11; since v62 the cadence E is tied over into bar 14 and resolves to D sharp on beat 2)
trioT = { gis'2 a'4 | b'2 e''4 | dis''4. cis''8 b'4 | a'4 gis'2 | a'2 b'4 | cis''2 fis''4 | e''4. dis''8 cis''4 | ais'4 b'2 | cis''2 dis''4 | e''4 gis''4 a''4~ | a''4. gis''8 fis''4 | cis''4 b'4 a'4 | gis'4 b'4 e''4~ | e''4 dis''4 fis''4 | e''2. }
% mottoTail: v04 HnOne bars 365-368 (the motto's chromatic tail E flat-D-D flat-C of movement I, on B)
mottoTail = { b'2. | ais'2. | a'2. | gis'2. }

% motiveXrepeated: v04 Timp 241 (retransition, repeated B; quoted by the finale's timpani at its 143-145; v24 bars 241 and 249)
motiveXrepeated = { b,4 b,8 b,8 b,4 }

% ---- where each theme must appear (v24 bar numbers; 376 bars) ----
%@ hornCall HnOne 1
%@ motiveX Timp 9
%@ motiveXrepeated Timp 241
%@ motiveXrepeated Timp 249
%@ themeA VlnOne 13
%@ themeA VlnOne 105
%@ themeA OboeOne 105
%@ themeA ClTwo 105
%@ themeA VlnOne 253
%@ themeA VlnOne 305
%@ themeA OboeOne 305
%@ themeA ClTwo 305
% fugato entries on theme A's head (first 14 notes = bars 1-4)
%@ themeA Vc 57 14
%@ themeA Vla 61 14
%@ themeA VlnTwo 65 14
%@ themeA VlnOne 95 8
%@ themeA Vc 289 14
%@ themeA Vla 293 11
% (since v74 the reprise fugato entry's fourth bar, 296, turns to the dominant of A: E4–B3–G♯3 instead of E4–C♯4–A3; bars 293–295 checked)
% retransition entries (first 8 notes = bars 1-2)
%@ themeA Vla 89 8
%@ themeA Vla 241 8
%@ themeA VlnTwo 245 8
%@ secondIdeaG VlnOne 45
%@ secondIdeaG FluteOne 45
%@ secondIdeaG OboeOne 45
%@ secondIdeaE VlnOne 121
%@ secondIdeaE FluteOne 125 15 8
%@ secondIdeaE OboeOne 125 15 8
%@ secondIdeaE VlnOne 277
%@ secondIdeaE FluteOne 285 8 15
%@ secondIdeaE OboeOne 281 15 8
%@ trioT ClOne 153
% v94 (c093): the second statement's consequent modulates to B at 180-184 (ii6/5 - cadential 6/4 - V7 - I of B), so only its first 27 notes match T
%@ trioT VlnOne 169 27
%@ trioT ClOne 197 9
%@ trioT Vla 197 9
%@ trioT ClOne 209
%@ trioT VlnOne 209
%@ trioT FluteOne 217 16 19
% coda: T shared out, bars 1-4 Hn 1, bars 5-8 Cl 1, bars 9-16 Vln I
%@ trioT HnOne 341 9
%@ trioT OboeOne 345 9 10
%@ trioT VlnOne 349 13 19
% (since v44 the coda statement's cadence differs: 354-356 gis'''2 fis'''8 e''' | dis'''2 fis'''4 | e'''2 r4, expanded cadential 6/4; checked through bar 353 only)
%@ mottoTail HnOne 357
