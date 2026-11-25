# Critic C, cycle 59: holistic (render c58 against c56, c53, c0 and a recording; score v621)

Scripts and outputs: `cycles/c59/critic_scripts/C/` (`lib.py`, `mkcache.py`, `bars.py` + `bars.txt`, `leads.py` + `leads_*.txt`, `notes.py`, `misc.py`, `pitchlev.py`, `horncorr.py`, `ends.py`, `tails.py`, `wet.py`, `rebow.py`, `flat.py`, `mp3cmp.py`; `cache/` holds 10 ms level frames of every stem of c53, c56, c57, c58, 194 MB). Nobody listened. Every figure is measured on the dry stems, the return stems, the master, the delivered mp3s or `rendered_build/parts.json` unless marked inferred. Each render is read on its own tempo map. c0 has no stems (mp3 only). Expected sizes after a fix are estimates from the family CC11 slopes (strings 0.30, winds 0.21, brass 0.29 dB per unit) or from the same quantity elsewhere in this render; none was simulated.

## Manual notes (pages chosen for this lens; MANUAL-GAPS.md and DIGEST.md used)

| Manual (PDF page) | What it says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| p.89 | Divisi instruments "are only available with the close microphones"; for the other positions "include the same articulations (in their non-divisi versions) and adjust the loudness". | Cello solo (Celli KS Master DIV A), bars 171-174 | Half. The track is Close only. The Main-mic alias is on the c58 "not done" list. The dry stem falls 16.4 dB in 0.2 s after its last note, then holds (the hall), so the solo has less stage sound than the section it sits in. |
| p.97 | Sustains have 5 dynamic levels on CC11; "Velocity ... does not control the loudness". | Every level fix proposed below is CC11, row or region gain, never velocity on sustain or legato rows | Followed. |
| p.98-99 | Slur, portamento and bow-change legato are different recordings; "the first note of a phrase has no legato effect"; Opus chooses the component from the MIDI data. | Cello solo: 8 keyswitches between Leg Slur, Leg BC and Leg Port in 12 notes | The rows differ in level by up to 10 dB at one CC11 (finding 1). c56 hid this with a -9.8 dB per-note cut at 685; nothing replaced it. |
| p.138 | Close mics give presence; Main mics (fifth row, Decca tree) capture "more room reflections than direct sound". | Woodwinds run Close 0 dB with Main at -3.4 to -20.6 dB (template layout) | Applied as the template has it. Cost measured in finding 6: upper-woodwind stems carry almost no stage sound after a note end. |
| DIGEST section 2 (p.144) | Velocity on true-legato rows sets the transition time, not loudness. | Cello solo 685 (velocity 100 on Leg Port MAX, the others 70) | Consistent: the +9.8 dB at 685 is the row, not the velocity. |
| MANUAL-GAPS #8 | Legato velocity 50-75 for a longer slide on cantabile lines; never tried. | Second theme, Cello solo | Still not tried. Not proposed before the levels of those lines are right. |

EW-TEMPLATE-PLAN sections this lens touched: section 1 (woodwinds Close-led) applied, with the cost in finding 6; section 5 / 8 (repeated-note gap 60-100 ms) applied, and applied to held notes where it should not be (finding 5); sections 6-8 ("long notes keep moving", 0-13 % of long notes flat in 15 of 20 expert files) not met: 31 % of string, 41 % of wind and 38 % of brass notes of 1.5 s or more have 4 units or less of CC11 movement inside them (c56: 31 / 33 / 37 %), though only one of them is exposed (Violins I 711.86); section 6 (two tracks per string section) not applied; section 8 (seeded tutti entry spread) not applied; section 10 (doublings share one curve) not checked.

## What c57 and c58 cost and gained against c56

Gained (from `cycles/c58/CHANGES.md`, not re-measured unless stated): 0 per-note envelope items and 0 fitted rows; envelope points 6962 -> 4515; notes with 3 dB or more of fader movement inside 720 -> 365; Violins II quarters in bars 23-25 on the beat (+220 -> +9 ms); pitches 4 dB out of line 23 -> 7; held-note pulses 17 -> 13; the c57 Violins II fault in bar 21 is gone (three eighths at 80.5-81.5 were +17 to +20 dB in c57, measured here: -22.3 -> -34 dB). Tutti stops are as dry as before (master 16.9-24.2 dB down 0.3 s after the five stops of c55's list; c56 13.8-25.1). The delivered file is unchanged in loudness and range (-19.8 LUFS, LRA 14.9; c56 14.4).

Cost, measured with `leads.py` (a note of 0.4 qn or more that was within 6 dB of the sum of all other dry stems and fell 3.5 dB or more against that sum): c56 -> c57 13 notes, c57 -> c58 16, c56 -> c58 17, c53 -> c58 22. Newly prominent notes (up 4 dB or more and now within 3 dB of everything else): c56 -> c58 one (Bassoon 1 133.5, +8.4 dB). So the two cycles did not break the balance in general. The losses sit in six places, which are findings 1-4 below. Master bars that moved 2 dB or more against c56: 24 (`bars.txt`), the largest bar 179 +5.6, bar 7 -4.6, bars 171-172 +4.1 / +4.6, bar 74 +4.5, bar 182 +4.0, bar 47 -3.7.

Not a loss on inspection: Cor anglais bar 7. The stem is -37.8 dB against -32.6 in c56, but it is still 9 dB or more over every other stem in the bar and within 0.5 dB of c53 on three of four notes. What is missing is the peak of the printed hairpin (finding 4, last row). Basses' pedal bars 126-130: +7.1 / +6.0 dB over c56, but the notes are still 10.6-16.3 dB under the rest of the dry mix, and G1 is not out of line with the basses' other pitches (`pitchlev.py`): listen before cutting.

## Findings, ranked by what a listener would gain

### 1. Cello solo, bars 171-174: the level follows the sample row and the note length, not the phrase (measured)

**Where.** "Cello solo", qn 680-696, the most exposed line of the movement (0.1 to 5.6 dB under the sum of everything else).

**What is wrong.** Note levels in dB, c56 then c58:

| qn | 680 Eb4 | 683.5 D4 | 684 C4 | 685 Ab4 | 687 G4 | 688 F4 | 689.5 Eb4 | 690 C#4 | 691 F4 | 691.5 Ab4 | 692 C5 | 694 B4 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| c56 | -35.7 | -35.5 | -34.4 | -36.9 | -34.1 | -32.9 | -38.2 | -36.2 | -38.3 | -36.6 | -34.8 | -43.5 |
| c58 | -31.3 | -33.1 | -34.7 | **-27.1** | -35.3 | -34.1 | -39.3 | -37.4 | **-42.5** | -39.0 | **-40.0** | -42.5 |
| row | Slur | Slur | BC | Port | Slur | BC | Slur | Slur | Slur | Slur | BC | Slur |

The print has a crescendo over 691-692 into the C5 and a diminuendo after it. In c58 the C5 is 12.9 dB under the Ab4 of bar 172 and 8.7 dB under the first note; the crescendo bar (691-692) is the softest stretch of the phrase. Range of the 12 notes: 15.4 dB (c56 10.6 including the printed fade, 5.4 without the last note). CC11 is 77 ± 3 from 684 to 692, so the differences are the rows: Leg Port MAX on Ab4 is about 10 dB over Leg Slur MAX (c56 carried a -9.8 dB envelope point at 685.8), Leg BC MAX on C5 is about 5 dB under, and slurred notes of 0.5 s (689.5, 691, 691.5) are 4-7 dB under long ones on the same row at the same CC11. Master bars 171-172 are +4.1 / +4.6 dB over c56 and bar 174 is -2.5.

**Fix** (no envelope; range render bars 170-175 first):
- `build/mix.json` `tracks["Cello solo"]["region_gain_db"]` (new key on this track; the `all_db` and per-row forms of c58): `[{"rows": ["Leg Port MAX"], "all_db": -8.0}, {"rows": ["Leg BC MAX"], "pitch_db": {"72": 5.0}}]`. Expected: 685 -27.1 -> about -35; 692 -40.0 -> about -35.
- One CC11 lane for the phrase in `build/score_config.py` (the track's `phrase_shapes` already has `[680, 696, "lyric"]`; write the values as that phrase's lane, flat across the joins): 56 at 680 rising to 70 at 683.5 (the first note is +4.4 dB over c56; 61 -> 56 and the slow envelope arch already gives the rise), 76 through 684-690, 76 -> 96 over 690-692 (the printed crescendo: +20 units, about +6 dB on the two short slurred notes and the C5), 96 -> 70 over 692-694, 70 -> 58 to 696. Expected: 691 -42.5 -> about -37, 691.5 -39 -> about -35, 692 about -34 with the region gain, so the C5 is the top of the phrase by 1-2 dB.
- If the range render still has more than 4 dB between neighbours, the fallback is one row: all 12 notes on Leg Slur MAX (no Leg BC / Leg Port keyswitches in `ALIAS_TRACKS["Cello solo"]`), which removes the row steps at the cost of the portamento into 685.
- Target: every note within 3 dB of the lane's shape; C5 at 692 the loudest note; bars 171-172 back within 1.5 dB of c56 on the master.

### 2. Horn 4's soft low notes are 6-11 dB over the horns above them, and Horn 1's soft G4 / A-flat 4 are 4-5 dB under (measured)

**Where.** Horn 4 on C3, D3, E3, F3 at p and mp: bars 11, 19-21, 57, 61, 105, 111, 156, 164. Horn 1 A-flat 4 at 204, 440, 545 and G4 at 94, 205.5, 416, 419, 542.

**What is wrong.** Horn 4, median level by pitch and CC11 band (`misc.py`), c56 -> c58: F3 soft (7 notes, CC11 46) -48.4 -> -40.6 (+7.5); E3 soft +7.7; D3 soft +8.2; C3 soft +5.8; G3 soft -56.0 -> -51.2 (+3.1); every mid and loud note within 1 dB. F3 now reads -40.6 at CC11 46, -40.7 at 88 and -40.9 at 94: the pitch has no dynamics left, and soft F3 is 10.6 dB over soft G3. In the chords: bar 111 (qn 440) Horn 4 F3 -39.9 against Horn 1 A-flat 4 -57.4 (c56 -49.0 / -49.3): the fourth horn is 17.5 dB over the first. Bars 19-20: Horn 4 F3 -39.8, Horn 3 C4 -50.3 / -53.0. Bar 61: Horn 4 E3 -36.6, Horn 3 A-flat 3 -42.3, Horn 2 E4 -38.2. Bar 11: Horn 4 +9.7 dB over c56. The only c58 changes on this track are `soft_trim_db` mp 6.0 -> 9.0 and the `region_gain_db` entry with `"dyn": ["pp"]` (CHANGES: "did not work"). The trim explains +3 on mp notes; the p notes on the four listed pitches rose 5.8-8.2 dB while p notes on G3 rose 3.1 and on A-flat 3 / B-flat 3 0.5-1.6, so the extra rise is on exactly the pitches of that entry, or on per-note cuts that c56 / c57 had there.
Horn 1 at CC11 75 or less, level moved to CC11 55 (`pitchlev.py`): F4 -41.7 (7 notes), A4 -40.2, C4 -46.8, C5 -48.3, G4 -52.6 (5), A-flat 4 -54.0 (3). Soft A-flat 4 is 12 dB under soft F4. c56 had a +13 dB shape on the note at 440; it was dropped.

**Fix** (`build/mix.json`, no envelope):
- Horn 4: `soft_trim_db` mp 9.0 -> 6.0. Delete the `"dyn": ["pp"]` entry and check in the Opus state which group sounds at CC11 46 on keys 48-53 (if the note crossfades two layers, the cut must name both: `"dyn": ["pp", "mp"]`). If the dynamic filter cannot be made to act, use `{"rows": ["Sus MAX"], "pitch_db": {"48": -6, "50": -8, "52": -8, "53": -8}}` on all layers. Cost of that form: the 13 mid / loud notes on F3 fall from -40.8 to about -49 (G3 loud is -33.4), all inside tutti. Expected for the soft notes: F3 -40.6 -> about -48.5, 2.7 dB over G3; bar 111 Horn 4 under Horn 1 once the next line is applied.
- Horn 1: `region_gain_db` add `{"rows": null, "pitch_db": {"68": 5.0, "67": 4.0}}` after checking the same offsets on its loud A-flat 4 / G4 (17 A-flat 4 notes of 0.8 s or more in the movement); if the loud notes are in line, restrict the entry with the working dynamic filter. Expected: bar 111 A-flat 4 -57.4 -> about -52; with Horn 4 at about -48 the chord is within 4 dB top to bottom (c56: 0.3).
- Bassoon 1: the c58 gains on A-flat 3 (`"56": 3.5` on Sus MAX, `5.5` on Leg Slur MAX) overshoot: A-flat 3 is now 3.6 dB over G3 at mid dynamics (c56 0.5 under), and the eighth at 133.5 rose 8.4 dB to within 0.8 dB of everything else. Halve both (1.5 / 2.5).

### 3. The theme's phrase end falls 12.6 dB and goes under the accompaniment (bars 21-23), and the celli's counter-line is 3.4 dB further down (measured)

**Where.** Violins I qn 82-89 (the printed diminuendo 80-86 and the first two notes of the forte restatement); Violoncellos 56-88.

**What is wrong.** Violins I, c53 / c56 / c58: 82 G5 -30.5 / -35.8 / -33.7; 83.5 F5 -36.2 / -38.5 / -40.7; 84.5 D5 -38.8 / -39.6 / -44.4; 85.5 B4 -36.5 / -40.9 / -45.7; 86 C5 -37.5 / -41.5 / -46.3; 88 E-flat 5 -45.6 / -40.1 / -44.1; 89 D5 -39.3 / -38.6 / -44.9. From 82 to 86 the line falls 12.6 dB (c53 7.0, c56 5.7) for a CC11 fall of 104 -> 73. Against the sum of all other dry stems the notes at 85-89 are -10.6 to -13.1 dB (c56 -7.0 to -8.4). The theme is the leading voice here. The row is Sus MAX (the c57 theme row), which is steeper below CC11 88 than the rows the dynamic map was made for. The same holds for the short notes at 146.5-148.5 (-44 to -46 dB against -37 to -43 in c53).
Celli under the theme, per quarter over bars 15-22: celli minus everything else -13.3 dB median, lower quartile -17.0 (c56 -9.9 / -12.5; c53 -10.5 / -13.2). Violins I minus celli +6.9 median, upper quartile +11.0 (c56 +4.6, c53 +4.8; target 3.9). The coordinator's question: yes, the celli are further down than in any earlier render I can measure, by 3 dB.

**Fix.**
- `build/score_config.py`: give Violins I a floor on the theme row. If `CC11_REMAP` takes a track key (as `ACCENT_FLAT` does), add `CC11_REMAP["Violins I"] = [(60, 78), (88, 90), (104, 104), (124, 124), (127, 127)]` limited to the `STEADY_LINE` spans (56-127, 536-576); if not, add that key. The diminuendo then ends at CC11 84 instead of 73 and the crescendo from 88 starts there. Expected: 86 C5 -46.3 -> about -42 (c56 -41.5), fall over 82-86 12.6 -> about 8 dB, notes at 85-89 from -11 / -13 to about -8 dB against the rest.
- `build/roles.json` Violoncellos `[56, 88, -3.5]` -> `[56, 88, -2.0]` (the c53 value; a slow role, 8 bars). Expected: celli -13.3 -> -11.8 against the rest, Violins I minus celli +6.9 -> +5.4.
- Guard: `theme_S.py c59 "Violins I" 56 90` stays at robust SD 9-10 ms (a CC11 change does not move onsets on Sus MAX, inferred).

### 4. Short solo lines of the winds and Horn 1 that lost a shape and got nothing (measured)

**Where and what.** Level in dB, then level against the sum of all other dry stems; CC11 now.

| Passage | Note | c56 | c58 | against the rest c56 -> c58 | CC11 now -> proposed | Expected |
|---|---|---|---|---|---|---|
| Clarinet 1, bars 45-46 (the link into the second theme) | 178 A-flat 4 | -42.1 | -48.8 | -0.9 -> -6.0 | 58 -> 80 | about -44 |
| | 179.5 G4 | -45.3 | -54.0 | -3.9 -> -15.3 | 62 -> 84 | about -49 |
| | 182 E-flat 4 | -51.5 | -56.5 | -8.0 -> -15.0 | 35 -> 50 | about -53 |
| Clarinet 1, bar 127 | 504.5 G3 | -40.0 | -49.0 | -2.3 -> -8.1 | 46 -> 66 | about -45 |
| Clarinet 1, bar 105 | 416.5 D5 | -37.2 | -43.7 | -3.5 -> -9.0 | lane +16 over 416-418 | about -40 |
| Bass clarinet, bars 77-78 (solo) | 304.5 E-flat 2 | -43.5 | -50.0 | -4.4 -> -8.8 | 65 -> 85 | about -46 |
| | 308 A-flat 2 (held) | -35.6 | -41.7 | -2.7 -> -6.3 | 86 -> 100 | about -39 |
| Bass clarinet, bar 109 | 432.5 F2 | -43.6 (c53) | -51.8 | -5.5 -> -12.2 | +20 | about -47.5 |
| Horn 1, bars 43-44 | 171 C5 (3.2 qn) | -47.0 | -49.8 | -5.4 -> -8.6 | 54 -> 63 (the c56 value) | about -47 |
| Horn 1, bar 125 | 498 C4 (3.1 qn) | -39.1 | -42.6 | -4.7 -> -9.0 | +12 | about -39 |
| Horn 1, bar 147 | 587.5 D4 | -35.0 | -41.5 | -5.2 -> -8.7 | lane +12 over 586-589 | about -38 |
| Cor anglais, bar 7 | 24 G4, 26 A-flat 4 (peak of the hairpin) | -35.9, -28.0 | -37.7, -35.9 | lead by 9 dB or more in both | 66 -> 74, 87 -> 100 | -36, -33 (c53: -36.2, -33.5) |

The bass clarinet's low register is also 5-8 dB under its middle at one CC11 (C2 -4.8, C-sharp 2 -5.7, D2 -8.4, E-flat 2 -5.0 against the track median, `pitchlev.py`).

**Fix.** `build/score_config.py`: write each row as one CC11 lane over the phrase (the coordinator's item 1), with the proposed values as the lane's level at those notes and straight lines between; no value is a bump inside a note. Where a span has three or more notes and the whole span needs the same lift (Clarinet 1 176-183, Bass clarinet 304.5-310), a role row in `roles.json` with its edges in the rests does the same job without changing the timbre: Clarinet 1 `[175.5, 183.5, 4.0]`, Bass clarinet `[304.25, 310, 2]` -> `5`. `build/mix.json` Bass clarinet `region_gain_db` add `"36": 4, "37": 4, "38": 6, "39": 4` (C2 to E-flat 2; `"44": -4.5` stays). Target: each note within 2.5 dB of its c56 level against the rest.

### 5. Bow changes on held notes: a 90 ms silence at printed same-pitch repeats, and one 8 dB step inside a tied note of the coda (measured)

**Where.** (a) Printed repeats of one pitch between two notes of 1 s or more on string tracks, which take `REP_MIN_GAP["string"]` 0.09 s: 32 joins, mostly the basses', violas' and celli's pedal notes at bar lines (bars 37, 40, 42, 53, 57, 77, 78, 81, 94, 98, 102, 115, 159). (b) Violins I 708-715, the tied E-flat 5 of bars 178-179.

**What is wrong.** (a) `rebow.py`: stem dip at these joins median 9.5 dB (quartiles 5.3 / 13.1; basses 12.6-21.7 dB at 144, 156, 224, 304, 308, 320, 388, 632), against a median 5.9 dB at the 77 joins with a 5-45 ms gap (the automatic re-bows and printed bow changes). On the master 12 of the 32 show 3 dB or more: bar 77 (qn 304) 7.0 dB, bar 94 (372, Violas) 6.2, bar 57 (224) 5.7, bar 78 (308) 5.3, bar 53 (208) 4.0. At bars 77-78 the basses are 6 dB under the rest and the bass clarinet has its solo. A section changing bow on a held pedal does not leave a tenth of a second empty; the 60-100 ms gap of plan section 8 is for repeated notes that must be heard as separate (Dan's S1), and these are not that. (b) The re-bow piece at 711.86 (Sus MAX, CC11 39) plays -40.8 dB after the first piece (Leg Slur MAX, CC11 37) at -49.2: +8.4 dB inside one tied pp note (c56 -52.1 / -49.7 with a fitted fill; c53 -51.1 / -50.8). It is the one note `leads.py` flags as newly prominent against c53, and the master's bar 179 is +5.6 dB over c56, the largest change of any bar.

**Fix** (`build/score_config.py`, note lengths and gaps only):
- `REP_MIN_GAP`: add a held-note class, e.g. `"held_s": 1.0, "held_gap": {"string": 0.03}` (both notes 1 s or more, no accent, staccato or sf on the second; the tool needs the key), so these joins get the gap the re-bows already have. Expected: stem dip median 9.5 -> about 6 dB, master at bars 77 / 78 / 94 from 5.3-7.0 to about 3 dB. The 17 re-bow holes of critic A's list are a different set and stay.
- `REBOW_NONE["Violins I"]`: add `(707.5, 715.5)`, the form c58 used for the last chord (one bow, 7.9 s at CC11 37-40). Expected: no step; bar 179 back within 2 dB of c56. Check the loop pulse on that note (the last chord's single bow moves 4 dB on the Violins I stem).

### 6. Checks from the other movements, and the comparison with c0, c53 and a recording

**Horn L/R correlation (measured, `horncorr.py`; 352 held notes of 0.8 s or more on Horns 1-4 and Horns a2).** Median correlation per track 0.61-0.83. Horn 1 B-flat 4 is in anti-phase: 444 (bar 112) -0.43 with a 0.3 s minimum of -0.83, mono sum -5.4 dB; 413 (bar 104) -0.33, mono -4.7 dB; three B-flat 4 notes, median -0.33. No other pitch on any horn track has a median under 0.15 (Horn 1 E5 0.15, one note; Horn 2 B-flat 4 0.23, one note; Horns a2 B-flat 3 0.31). The scherzo's pitch (A-flat 4 on the same patch) reads 0.62 here over 17 notes, with single notes at 0.03 and 0.28 (545, 552). Neither B-flat 4 is exposed (-11.1 and -22.5 dB against the rest), so this is the smallest item here. Fix if wanted: `mix.json` Horn 1 `mic_db` Close -6.3 -> -3 for the track (the Close pair is the correlated one), or leave it and list it; a region gain cannot change phase.

**Tutti note ends before bar lines (measured, `ends.py`).** The finale's fault is not present in that form. Note ends before a beat cluster at 80-100 ms (685 of all ends in the last 200 ms; only 442 at 20-50 ms), because of the gap floors. At the 37 loud tutti beats where 12 or more tracks end together, the ends lie 64-100 ms before the beat (10th to 90th percentile; median spread 73 ms) and the master dips a median 3.4 dB (c53: 2.6 dB over 31 beats), 2.6 dB at bar lines. Five beats dip about 4 dB or more against both sides: 122 and 124 (bars 31-32, 6.8 / 4.8 dB), 564 (bar 142, 5.5; 562 reads 3.5), 484 (bar 122, 4.2), 392 (bar 99, 4.4). Those of bars 31-32 and 141-142 are separated accented chords, where a dip between strokes is the printed articulation. No change proposed; if the actor staggers anything, stagger the celli against the basses at 122-124 and 562-564.

**Upper-woodwind stems after note ends (measured, `tails.py`, `wet.py`; ends followed by 0.5 s of rest).** Fall of the dry stem 0.2 s after the note end: Cor anglais 39.3 dB, Oboe 1 29.4, Flute 1 28.2, Clarinet 2 27.5, Bass clarinet 26.2, Clarinet 1 25.5, Oboe 2 24.1, Bassoons 20.6-21.0, Flute 2 20.4; Violins I 13.7, Violins II 17.5, Violas 16.8, celli 10.0, basses 10.6; horns 11.1-13.9, trombones 13.0-18.4, tuba 16.9; trumpets 36.4-43.3. The wind return sits 14.4 dB under the dry winds (strings 15.9, brass 21.2), so after a woodwind or trumpet note ends, only the hall is left 0.2 s later, 14-21 dB down, while a string or horn stem still carries its own stage sound. Main mic level against Close: Oboes -20.6 dB, Cor anglais -11.6, Bass clarinet -9.8, Bassoons -8.6, Flute 1 -4.7, Clarinets and Flute 2 -3.4. The fall does not follow the Main level alone (clarinets at -3.4 still fall 25-27 dB), so the patch release is part of it. Test, one track, range render bars 5-9: `mix.json` Cor anglais `mic_db` Main -11.6 -> -4.0 with `gain_db` lowered to hold the stem's level; adopt for the oboes and Cor anglais if the fall at 0.2 s comes down to the clarinets' 25 dB and the stem's 2-6 kHz share does not drop by more than 1 dB. Do not raise sends (BRIEF S4).

**c58 against c0, c53 and the recording (measured on the delivered mp3s, `mp3cmp.py`).**

| | c0 (v221) | c53 | c56 | c58 | Dvořák 9/i (lossy mp3) |
|---|---|---|---|---|---|
| LRA, LU (all at -19.8 LUFS except the recording, -14.8) | 17.3 | 14.5 | 14.4 | 14.9 | 21.8 |
| 3 s level, 10th to 95th percentile, dB | 17.1 | 14.1 | 13.7 | 14.1 | 23.8 |
| Band share 100-250 / 250-500 / 2-6 k / 6-14 k Hz, dB re 40 Hz-14 kHz | -8.8 / -6.2 / -12.2 / -30.9 | -8.7 / -5.9 / -10.0 / -30.2 | -8.9 / -6.0 / -9.9 / -30.2 | -7.6 / -6.4 / -9.9 / -30.3 | -6.8 / -6.5 / -10.4 / -28.6 |
| Spectral centroid of the louder half, median / IQR, Hz | 722 / 260 | 861 / 344 | 840 / 354 | 835 / 375 | 835 / 375 |
| L/R correlation under 250 Hz / 250 Hz-2 kHz / 2-8 kHz | 0.63 / 0.51 / 0.49 | 0.60 / 0.57 / 0.42 | 0.62 / 0.56 / 0.42 | 0.64 / 0.56 / 0.43 | 0.56 / 0.55 / 0.66 |
| Side minus mid, dB | -5.0 | -5.3 | -5.3 | -5.4 | -5.3 |
| Change of level between neighbouring 0.4 s frames, SD in the louder half, dB | 1.94 | 1.74 | 1.76 | 1.89 | 2.64 |

Against c0 the tone has moved to the recording's (centroid and its spread now equal to it; 2-6 kHz share -12.2 -> -9.9 against -10.4), and the width matches. Against c53 and c56 the only spectral change is +1.3 dB in 100-250 Hz (the basses' and celli's levels after the carry rows went), which moves toward the recording. Two measures still separate the render from the recording: the level changes less from moment to moment (1.89 against 2.64 dB), and the top band is 1.7 dB lower. The 14 dB range is the headphone target, not a fault. The 40-100 Hz band is not compared (lossy reference).

**Weakest passages now (measured, in this order):** the Cello solo bars 171-174 (finding 1); the horn chords at p, bars 11, 19-21, 57-61, 105-111 (finding 2); the theme's phrase ends, bars 21-23 (finding 3); the link bars 44-46 and the bass clarinet solo bars 77-78 (findings 4 and 5); the Lento bars 6-13 and bars 72-76, where critic A's 17 re-bow holes of 7-13 dB sit; the tied violin note of bars 178-179 (finding 5).

**What still reads as a machine (inferred from the measures above):** levels that step with the sample row or the pitch on an exposed line (Cello solo, Horn 4 F3 at one level for p and f, Horn 1 with 12 dB between soft F4 and soft A-flat 4); a tenth of a second of silence wherever a held string note repeats its pitch; a diminuendo that is twice the size of its neighbours because one row is steeper; woodwind and trumpet notes that stop with no stage sound; a third of long notes with a static CC11; less moment-to-moment level change than a recording.

## Do not touch

The envelope state of c58 (0 per-note items, 0 fitted rows) and the rule behind it; the constant 126 and the one-row theme lines (Violins I robust SD 9 ms over 56-90); Violins II and Violas on the Marc spans 88-100 and 536-548 (+9 ms); the Violins II Sus Marc LITE row gain of -4 dB (bar 21 is right again); the family EQs, returns and sends (tutti stops 16.9-24.2 dB down at 0.3 s; tone and width at the recording's values); the delivery chain (-19.8 LUFS, LRA 14.9); the gap floors at separated tutti chords (bars 31-32, 141-142); the Cor anglais solo's level in bars 5-9 apart from the hairpin peak; the basses' pedal bars 125-130 until someone has listened.
