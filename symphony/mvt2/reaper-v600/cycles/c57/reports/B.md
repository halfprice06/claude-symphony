# Critic B, cycle 57 (render of cycle 56): balance and levels, last cycle of the run

Data used: the delivered stems `cycles/c56/render/` (after the stem fix) with `cycles/c56/build_fix/` (`parts.json` is
byte-identical to `build/parts.json`); c54 from `cycles/c54/render/` with `cycles/c54/build_fix/`. `tools/build_reaper.py`
was read only up to `ENV_LUA` (through `cycles/c53/actor_scripts/lib53.py`). The old per-note layers of c54 come from the
tagged run my c55 report made (`items.json`, copied as data, no code imported from another cycle's folder).
Scratch folder, left in place (1.8 MB, no audio): `/private/tmp/claude-501/mockup-loop/mvt2-c57-B/`
(`notes.json` / `notes_c54.json` per-onset tables, `lines57.py`, `len2.py`, `pit57.py`, `sim57.py`, `rows57.py` +
`rows57.json` (every section row with its decomposition), `cmp57.py`, `steps.py`, `short57.json` and `region57.json`
with the data of findings 2 and 3). No REAPER, no bridge job, nothing written outside this report and the scratch folder.
Nothing below proposes a per-note track volume move; every volume row named covers three notes or more, a section or a fade.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 57, so no scheduled page reading. Pages that bear on the fixes (read for
the c56 report, not re-read in full this cycle):

| reading (2021 HO manual, PDF page) | where it applies | does the render follow it |
|---|---|---|
| p.150-151, p.53: CC7 is the instrument's volume, before the hall; CC11 / CC1 shape longs; velocity sets level and layer on strokes | Timpani (all), final chord spans, bar 63 heads | Partly. The timpani level is split between CC7 (16-71) and a fader rule of up to +19 dB that switch at different times (finding 1) |
| p.137: each row of a KS Master has its own volume knob | Flute 1 "LegRep RRx4", tremolo rows | The knob had no effect on c56 pass a1 (CHANGES 1.3); region volumes are the working control. Worth a line in `MANUAL-GAPS.md` |
| `MANUAL-GAPS.md`, c37 entry (legato targets speak late and low) | short slurred notes in Flute 1, Oboe 1, Cor anglais, Bassoon 1, Violoncellos | No: with the early fills off these notes sit 2-4.6 dB under their line (finding 2) |

## Re-measurement of the main lines (measured)

Same method as the c56 report (per onset: stem level over 20-80 % of the note minus the written envelope, fitted on row +
CC11 + pitch; a note's deviation is taken against its line's median). The script counts 377 notes in the 24 lines (the
c56 report counted 364); by this script c55 reads 170 / 100.

| | c55 | c56 |
|---|---|---|
| notes 2 dB or more out of their line | 170 | **152** |
| notes 3 dB or more out | 100 | **83** |

Better: Horn 1 theme 7-14 (sd 3.0 -> 1.5 dB, 14 -> 4 notes out; the region gains worked, no Horn 1 pitch is now more
than 1.9 dB off), Horn 1 65-70 (2.0 -> 0.8), Bass clarinet 31-36 (2.7 -> 1.6), Double basses 71-78 (3.9 -> 2.9), Cor
anglais 47-52 (2.4 -> 1.9), Oboe 1 15-22 (4.2 -> 3.2). Unchanged within 0.2 dB: every string line, Flute 1 theme B
(3.1, 16 of 27 out), Cor anglais 41-44 (3.0), Oboe 1 45-47 (3.0), Violoncellos 71-78 (3.5, 10 of 18 out), Bassoon 1
71-78 (4.1), Flute 1 79-82 (3.9). The lines that did not move are the ones whose tables the actor rejected in c56 and
the ones with short slurred notes; findings 2 and 3 are about them.

Solo margins are the actor's (confirmed from the per-bar stems): Horn 1 7-14 +8.4, Bass clarinet +5.5, Flute 1 37-44
-2.9, Oboe 1 45-52 -6.0, Horn 1 65-70 +4.3, Clarinet 1 coda +0.6. The flute of theme B is the one solo that sits under
its accompaniment; its weak notes are the short ones and the low register (C5-F sharp 5), both below.

## Findings, ranked

### 1. MUST DO. Timpani: the level is split between CC7 and the fader, and the two halves do not switch together

Where: Timpani, every entry; worst at qn 171.9-172 (bar 53 downbeat), bar 84 (qn 277-280.5), qn 203, 209.5, 262.
What (measured): 10 of the 14 remaining envelope moves of 1.5 dB or more within 0.25 s inside a note are on the
timpani (`steps.py`; the slew limit skips the family). At 172 the envelope goes +6.0 -> -5.0 dB between qn 171.875 and
172.0 (140 ms) while CC7 goes 28 -> 71 (+8.1 dB) at 171.98. The total level step is only -3 dB, but for 120 ms the
envelope has fallen and CC7 has not risen: the stem drops from -42.1 to -52.5 dB before the stroke (the hole before
172). All six timpani section rows cover one to three notes ([0,18] -2.9, [140,172] -4.6, [172,204] +1.8, [204,220]
+4.4, [220,238] -2.7, [238,262] +1.0), so they are per-note levels on the fader. Bar 84: stroke peaks -36.3 / -33.7 /
-37.0 dB against c54 -38.9 / -38.5 / -39.7 (+2.6 / +4.8 / +2.7); the middle stroke is 3 dB over its neighbours, c54's
were even within 1.2 dB. Velocity 56-60 -> 72 measured 0.2-0.4 dB per step on these strokes, not the 3 dB per 22 steps
the c55 note assumed.
Fix (CC7 and velocity only; finale technique 72):
- `tools/score_to_parts.py`, timpani block (`TIMP_ROLL_TRIM_DB` at about line 3987, the roll settle / soft-roll rules,
  roles, section rows): for `family == "timp"` write no volume envelope. Compute the planned level as now, L(q) = envelope
  dB + 20·log10(CC7/127), and emit it as one CC7 lane, CC7' = 127·10^((L - L_ref)/20) (CC7 is linear amplitude,
  `mockup-kit/LEARNINGS.md` line 54), with `mix.json` Timpani `gain_db` raised by L_ref so the largest CC7' is about 120
  (the roll at qn 200-203 sets it: +14.4 dB at CC7 36 gives L = +3.5; L_ref = +4.5, so `gain_db` rises by 4.5 dB and the largest CC7' is 113). Steps between
  a roll and a stroke go at the stroke's note-on minus 0.02 qn, as the CC7 jump does now. Delete the six Timpani rows of
  `build/cell_rows_c56.json` after folding their values in.
- `build/score_config.py`: `VEL_SET["Timpani"][277.0] = 64`, `TIMP_VEL = {278.5: 60, 279.0: 60}` (c54's values for the
  second and third stroke under the same envelope; 64 on the first replaces c54's +2.5 dB fader lift).
Expected: 14 -> 5 fast moves inside notes (the five left: Clarinet 1 262, Violas 261.3, and the final fade on three
tracks); no hole before 172 (one -3 dB step instead of -11 then +8); bar 84 master +2.2 -> about 0 against c54, the three
strokes within 1.5 dB. Decidable offline: the level is the same by construction; simulate as a gain on the stem
(`lib53.Render`) and rerun `steps.py`. The hall return follows CC7, which the simulation does not show.

### 2. MUST DO. Short slurred notes sit 2-4.6 dB under their line: give them CC11 by note length

Where: Flute 1 bars 37-44 (qn 110-133.5, 21 notes), Cor anglais 41-44 (6), Oboe 1 45-46 (qn 142-145.5, 4), Bassoon 1
45-46 (4), Violoncellos bars 23, 45-46, 60, 64, 71, 74 (11). This is the "long notes over short ones" fault.
What (measured, `len2.py` / `pit57.py`: slurred targets on a legato row, residual after row, CC11 and pitch, against notes
of 0.9 s or more): notes under 0.6 s read Oboe 1 -4.6 dB (CC11 under 56) / -2.1 (above), Violoncellos -3.6 / -3.6,
Bassoon 1 -3.5, Cor anglais -2.7, Flute 1 -2.2 / -1.1, Violins I -2.2 (above 56 only). Notes of 0.6-1.3 s are within
0.8 dB of the long ones on every track, so it is not a slow bloom of the whole note. The stem shows why: after each
slurred note-on the level dips 6-12 dB for 0.25-0.4 s (Flute 1 qn 131.5: -45 -> -54.7 dB, back to -46.5 after 0.3 s; qn
133.5: -45 -> -58.0; Violoncellos 240.0: -37 -> -45.9 for 0.5 s) and an eighth note is over before the level returns.
c54 covered it with early fills of +8 to +12 dB on the fader (Flute 1 131.5 +8.1, 133.5 +11.6, Cor anglais 131.5
+13.4). Heard against c54: Flute 1 133.5 -5.8 dB, Cor anglais 131.5 -7.7, 133.5 -3.6, Oboe 1 142 -2.9. The hole depth
does not depend on CC11 (median 4-5 dB in every CC11 band on Flute 1, Violins, Violoncellos), so raising the whole
phrase's CC11 against a lower trim would not close it; that test can be skipped. The violoncellos' long notes (1.3 s or more, CC11 under 56) read -0.6 dB against the fit once the short notes have
their own term: the fault is the short notes plus pitch
(finding 3), not the long ones, and the c56 lanes of -10 on 238 / 244 / 253 can stay.
Control: CC11, held flat over the whole short note (one value per note, changed in the join, no ramp inside the note).
Fix: `build/score_config.py`, `CC_SHAPES_S` (keyed to the note, seconds from the moved note-on), for each onset in
`short57.json`: `(11, sq, [(-0.03, 0), (0.0, N), (len_s - 0.03, N), (len_s, 0)])`, where consecutive short notes share one
plateau. N from each track's own CC11 slope on c56 (dB per unit at CC11 46 / 64: Violoncellos 0.43 / 0.34, Flute 1
0.29 / 0.28, Cor anglais 0.36 / 0.26, Bassoon 1 0.51 / 0.35; Oboe 1 +14 gave +2.9 dB on pass b1):
Violoncellos +8 (68, 68.5, 142, 142.5, 145.5, 195.5, 219, 240, 240.5, 248, 248.5), Oboe 1 +14 (142, 142.5, 145, 145.5),
Cor anglais +9 (127.5, 129, 129.5, 131.5, 133.5, 155.5), Bassoon 1 +8 (142, 142.5, 145, 145.5), Flute 1 +7 (110, 110.5,
113, 113.5, 117, 117.333, 117.667, 121, 121.5, 127.5, 129, 129.5, 131.5, 133.5, 191.5, 195.5, 197.5, 257, 257.5, 258,
258.5). Not on Violins I / II, Horn 1, Clarinet 1 or Oboe 1 bars 15-22: simulated there the lines get no better or worse.
Expected (simulated on the per-note table, `sim57.py`, median step of the instrument level with the CC11 term removed):
Violoncellos 23-30 3.33 -> 2.16 dB and 71-78 4.25 -> 3.05, Cor anglais 41-44 3.50 -> 2.54, Flute 1 theme B 4.38 -> 3.93,
Oboe 1 45-47 3.40 -> 2.91; the notes themselves +2 to +3.5 dB. The dip at the join stays (slot A). Needs a render: one
range pass of bars 41-47 and 71-74 if the disk allows, otherwise the final render is the test. Check that no lifted note
ends more than 1.5 dB over the long note after it, and S on Flute 1 131.5 / 133.5.

### 3. MUST DO. Second round of region gains, fitted on c56 with the short notes separated; they replace the sample-level rows

Where: Flute 1 (bars 37-44 and 79-82), Bassoon 1 (7-14, 31-36, 65-70, 71-78), Bassoon 2, Cor anglais, Violoncellos,
Double basses (65-70 pedal, 61-62), both violin sections' C5.
What (measured, `pit57.py`, pitch offsets on c56 after row, CC11, a short-note term and an entry term; n notes):
- Flute 1: C5 -3.1 (4), C sharp 5 -4.8 (4), E flat 5 -2.8 (6), F sharp 5 -2.2 (5), C6 +3.5 (4), C sharp 6 +2.9 (4), F6
  +2.3 (3), F sharp 6 +5.1 (2), G6 +5.8 (2): a register trend, low weak and high hot, the same signs as on c55. In bars
  79-82 the row [262, 274, -6.1] holds down B flat 6 / A flat 6 / G6 (G6 at qn 268 reads -23.5 dB instrument level at
  CC11 104 against -31.0 for the two notes before it at CC11 115) and takes the rest of the phrase with it: qn 269-271
  are 6.0 / 6.1 / 4.2 / 6.8 / 9.1 dB under c54 (A flat 5 at 271, held 4.1 s: -56.8 against -47.6). Master bar 82 -1.9 dB.
- Bassoon 1 at pp (CC11 34): E flat 3 -60.5 dB, A flat 3 -59.8 to -64.7, C sharp 4 -53.6; fit E flat 3 -3.2 (8), A flat 3
  -4.7 (10), C sharp 4 +2.8 (10). Its rows [18,42] +3.9, [90,108] +3.7, [220,238] +4.2 and [140,172] -2.1 are these
  three pitches (cells of A flat 3 / E flat 3 are lifted, the cell of C sharp 4 is cut).
- Bassoon 2: C3 -4.2 (7), E flat 3 -2.4 (7), A flat 2 -1.8 (7). Cor anglais: F4 -3.1 (6), C sharp 4 -2.8 (3), C sharp 5
  -3.5 (2), A flat 3 +2.3 (2).
- Violoncellos: A flat 2 +4.4 (8), E flat 3 +2.2 (12), A flat 3 +1.9 (11), C3 -2.0 (9), G3 -1.9 (7), C4 -3.5 (7).
  Bars 71-74: G3 at 243 / 249 reads -42.8 / -45.1 dB between long notes at -38.5 to -40.1; first note of bar 61 (A flat 3)
  5.7 dB over the next (c54 2.3).
- Double basses: E flat 2 -4.6 (15), C sharp 2 +2.7 (10), E2 -2.7 (3), E flat 3 -5.5 (2); bars 62: F sharp 1 -29.2 then
  E1 -20.6 dB, a step of 8.6 dB on equal CC11 (c54 4.7). The row [220, 238, +8.1] is seven E flat 2 pedal notes: 3.9 dB
  of it was the old pitch trim, 4.4 dB the mean of the re-bow fills.
- Violins I C5 +3.2 (18) and C sharp 5 +2.7 (6); Violins II C5 +3.4 (13), C sharp 4 +3.8 (6), C4 +3.2 (2), F4 -2.2 (9).
  The pickup C5 at qn 171 is +2.0 dB over c54 even under the row [140, 172, -5.5] that exists for this one note.
The actor's c56 objection (the celli's hot notes are long notes, not pitches) is answered by the short-note term: with
it the pitch offsets keep their signs and sizes.
Fix: `build/mix.json`, `region_gain_db.pitch_db` per track (`region57.json` holds the table in this form; rows as in c56,
leaving "Tremolo" and "Pizz RRx4" out on the strings):
Flute 1 {72: +3, 73: +4, 75: +2.5, 78: +2, 84: -3, 85: -3, 89: -2, 90: -5, 91: -5.5, 92: -2, 94: -4} (92 and 94 are the
old pitch-trim values; four notes and one); Bassoon 1 {51: +3, 56: +4.5, 61: -3 on all rows}; Bassoon 2 {44: +2, 48: +4,
51: +2.5}; Cor anglais add {56: -2, 61: +3, 65: +3, 73: +3.5}; Violoncellos {44: -4, 48: +2, 51: -2, 55: +2, 56: -2,
60: +3.5}; Double basses add {28: -3, 30: +2.5, 37: -2.5, 39: +4.5, 40: +2.5, 51: +5}; Violins I {72: -3, 73: -2.5};
Violins II {60: -3, 61: -3.5, 65: +2, 72: -3}; Oboe 1 {77: -3.5, 78: -2.5}; Clarinet 1 add {75: +2.5, 79: -2.5};
Clarinet 2 {51: +3, 68: +3}; Bass clarinet add {39: +3.5}. Shared regions as listed in the c56 report (finding 1.3).
Then rerun `comp56.py` and delete the rows the gains replace (finding 5); Flute 1 [262, 274] should come out near -2.
Expected (simulated, `sim57.py`, in-sample for the pitch terms): steps of 3 dB or more between consecutive notes of the
24 lines 157 -> 147 with finding 2 -> 96 of 371 with the gains; Bassoon 1 71-78 median step 4.35 -> 0.82 dB, Cor anglais
41-44 2.54 -> 1.30, Violoncellos 23-30 2.16 -> 1.33, Violins II 22-30 3.17 -> 1.66, Violins I 22-30 2.20 -> 1.99,
Flute 1 79-82 6.08 -> 3.00, Double basses 53-60 2.93 -> 1.91; basses' bar 62 step 8.6 -> 3.1 dB; Flute 1 269-271 about
4 dB closer to c54. Needs a render (c56 pass a1: every gain arrived within 0.3 dB, so the final render can carry it);
the row refit after it is offline. If the session is short, do Flute 1, Bassoon 1, Violoncellos and Double basses first.

### 4. MUST DO. Coda and final chord: the top of the chord enters low, the basses end loud; one double correction

Where: bars 89-92 (qn 292-304), strings and their doubles; Oboe 1 qn 139; master bar 92 +2.1, bar 91 +1.3 against c54.
What (measured, stems summed per pair, c54 -> c56): Violins I + Violin I solo bar 89 -47.4 -> -51.2 (-3.9), bar 90
+1.0, bar 92 +2.6: the chord's top rises 2.2 dB from bar 89 to 90 where c54 fell 2.5. Violins I alone at 292: -53.7 dB
against -49.7 on its next bow at the same CC11 34 (the first bow on "Sus MAX"). Violins II pair bar 89 -2.1, bar 91
+2.3, bar 92 +1.9. Violoncellos pair bars 89-91 -1.0 / -2.3 / -1.6. Double basses bar 91 +2.2, bar 92 **+4.6** (qn 299.8
+5.2, 302 +4.4): at -55.0 dB they are the loudest stem of the last bar (Violins I pair -55.7, the others -59 to -60).
CC11 cannot bring them down: the basses' slope at CC11 34 -> 17 is 0.18 dB per unit. These are the "balance cells off
c54" of bars 83-92 (Violins I -3.3, Violins II -2.7, Violoncellos -1.3, Violoncellos div +1.2). The sixth cell, Oboe 1
37-44 +4.1, is one note: qn 139 carries the CC11 +22 head lift and the row [108, 140, +4.7] that was fitted before it
(-42.4 dB against c54 -46.6).
Fix (CC7 lanes, linear amplitude; `TRACK_DOUBLES` "cc7" takes one value per span now, so write the lanes in
`CC_SHAPES` with "set", or let "cc7" take a point list):
- Violins I and Violin I solo: CC7 127 over 291.9-294.6, 100 at 295.2 (first bow +2.1 dB), 100 -> 80 over 300.5-302.
- Violins II and Violins II div: CC7 115 over 291.9-295.6, 90 at 296.2 (+2.1 dB), 90 -> 74 over 300.5-302.
- Violoncellos: CC7 113 over 291.9-300, 90 at 300.6 (+2 dB); Violoncellos div copy 45 then 36 at the same times.
- Double basses: new CC7 lane, 127 to 298.3, 76 at 300.0, held to the end (-4.5 dB over the last three bows; a fade).
- Delete Oboe 1 [108, 140, +4.7] from `cell_rows_c56.json`.
Expected: Violins I pair bar 89 -3.9 -> about -2 against c54 and no rise into bar 90; master bar 92 +2.1 -> about 0
(stem sum -50.4 -> -52.4 dB, computed from the bar levels); Oboe 1 139 at -47.1 (c54 -46.6). Decidable offline: CC7 as a
gain on the stems (`LEARNINGS.md`: within 0.5 dB, 1.5 dB where a fall overlaps a release).

### 5. MUST DO (the offline part). The 117 section rows by cause

Each row was set against the mean of every removed c54 layer over the track's sounding time in its cell (`rows57.py`,
table in `rows57.json`). "Unexplained" is the part of the row that no removed layer's time mean accounts for.

| group | rows | sum of abs dB | what they are | proposal |
|---|---|---|---|---|
| under 1 dB | 33 | 22.3 | fit noise; 66 envelope edges | delete all. No cell moves 1 dB; simulate with `lib53.Render` |
| one or two notes in the cell | 21 | 61.5 | per-note levels held by a row: Violins I [140,172] -5.5 (1 note), Horn 3 [66,90] -5.3 (2), Oboe 1 [108,140] +4.7 (1), Timpani x5, Bassoon 2 [220,238] -4.4 (2), Violas [220,238] +3.7 (2), Horn 4 [66,90] -3.4 (1), Violoncellos [0,18] -3.2 (2), Cor anglais [172,204] +2.8 (1), Flute 1 [90,108] +2.6 (1) and [204,220] -2.6 (2), and seven under 2.2 dB | Timpani into CC7 (finding 1); Oboe 1 delete (finding 4); Violins I [140,172], Bassoon 2 [220,238] (two C sharp 3), Flute 1 [90,108] and [204,220], Cor anglais [172,204] are pitch levels: region gains (finding 3), then delete. The rest: a flat CC11 offset over the note sized by the track's slope where it is under 10 units (Violas [220,238] +3.7 -> CC11 +11 on qn 220 / 223; Violoncellos [0,18] -3.2 -> CC11 -8), otherwise leave the row and say so (Horn 3 and Horn 4 [66,90] would need CC11 34 -> 18) |
| sample level | 20 | 53.4 | the old pitch / note trims and level fits: Clarinet 2 [0,18] +9.4 (note trim +8.3 on three chalumeau notes, E flat 3 / E3 at -60 to -62.6 dB), Bassoon 1 x5, Oboe 1 [140,172] +3.4, Horn 3 [204,220] +3.2 (unison boost), Bassoon 2 x2, Flute 1 [108,140] +2.2, Double basses x3 | region gains of finding 3, refit, delete what falls under 1 dB. Clarinet 2 [0,18]: region gain 51 / 52 +6 on "Sus Non Vib" only and the row down to about +3 (E flat 3 reads -3.1 over the movement, so not the whole +9.4) |
| unexplained by any removed layer | 22 | 52.4 | 13 of them are woodwind, horn and bass cells of bars 61-64 and 79-82 with one sign per track: Oboe 1 -2.1 / -3.3, Flute 2 -1.3 / -2.9, Bassoon 2 -2.5 / -4.1, Double basses -2.0 / -2.6, Bassoon 1 -0.4 / -1.7, Bass clarinet -1.6, Horn 1 -2.4, Flute 1 -2.6 / -6.1 (hot top pitches, finding 3). The rest are effects of the c55-c56 instrument-side changes (Clarinet 1 [238,262] +3.9, Violoncellos [238,262] +2.8, Double basses [238,262] +2.2, Trombone 1 [204,220] +3.7) | mapping: move the ff value into `mix.json` `dyn_trim_db` "ff" (these tracks play ff only in these two cells): Oboe 1 2.0 -> 0, Flute 2 1.0 -> -1, Bassoon 2 2.0 -> -1, Double basses 4.0 -> 2.0, Bassoon 1 3.0 -> 2.0, Bass clarinet -3.0 -> -4.6, Horn 1 -0.8 -> -3.2; delete those rows. The c56-change rows: keep (several notes, slow) |
| bar means of removed shapes | 16 | 42.1 | means of re-bow fills, early fills, sostenuto holds: Double basses [220,238] +8.1 (half fill mean), strings [204,212] +3.6 / +3.3 / +1.4 / +1.1, Violoncellos [262,274] +3.8, Cor anglais [108,140] +2.9, Violins I / II [66,90] +2.1 / +2.0 | delete where c56 fixed the cause on the instrument side: Violins I [0,18] +2.1 and Violoncellos div [274,304] +1.9 (doubled spans), Violins II and Violins II div [108,140] +2.0 / +1.6, and the fill half of Double basses [220,238] (-> +4, then 0 once E flat 2 has its gain). Keep the others this cycle: no replacement exists and each is several notes |
| phrase decisions | 5 | 12.6 | old role levels: Violins II [274,304] -3.5 and [220,238] -1.3, Cor anglais [90,108] -2.0, Horn 2 [204,220] -1.4, Timpani [204,220] +4.4 | move to `build/roles.json` as roles (Timpani into CC7) |

Expected: 117 -> 30 to 40 rows, none covering fewer than three notes except the two horn rows; master bars within 1 dB of
c56 except where findings 3 and 4 move them on purpose. All of it is decidable offline once finding 3's gains are
rendered; the deletions under 1 dB, the doubled spans and the "ff" trims need no render at all (level-only, simulate on
the stems, compare `acc56.py` cells).

### 6. Bar 63 heads and the climax steps (not marked must do)

Where: qn 212 (bar 63 sf), Violas and Bass trombone; bars 61-62 Violoncellos and Double basses.
What (measured): head peak in the first 250 ms, Violas -25.0 dB against c54 -20.7 (-4.3), Bass trombone -26.2 against
-22.7 (-3.5); the bodies are 0.7-1.8 dB over c54, so only the front is missing. Bass trombone's CC11 goes 86 -> 106 on
the head and the track gains about 0.1 dB per unit there (+10 gave +1 dB in c56), so CC11 cannot make the sf. Climax
steps: Violoncellos 204 -> 206 5.7 dB (c54 2.3), Double basses 208 -> 210 8.6 dB (c54 4.7); both are pitch levels
(finding 3: A flat 3 -2, F sharp 1 +2.5, E1 -3).
Fix: the c56 recipe of the other strings with CC7 headroom. Violas and Bass trombone: CC7 90 over 203.9-211.95 with
their section row raised by 3.0 dB (Violas [204, 212] +1.4 -> +4.4; Bass trombone [204, 220] +0.8 -> +3.8; three notes
or more each), CC7 127 at 211.98, held to 212.15, straight fall to 90 at 212.75 and held; the row keeps its value to the end of
its cell. Expected: both heads +3.0 dB (20·log10(127/90)), bodies unchanged from 212.75. Decidable offline by the CC7 law;
the head against Violins I's needs the final render. Trombone 1's accents are slot A's.

## Smaller measured points

- The 14 moves inside notes: Timpani 10 (finding 1); Clarinet 1 qn 262 (-2.3 dB in 0.25 s, the edge of its row
  [262, 274, -1.8]: gone when the row is deleted or moved to "ff"); Violas 261.3 (-1.9, role start at 262: end the ramp
  0.02 qn before the note-on at 261.281 or start it at 262 after the next note-on); Double basses, Violas and Violas div
  303-304 (-1.6 dB per 0.25 s, the final fade: leave).
- 91 of the 234 row edges fall inside a sounding note; the slew limit holds them under 3 dB per second. Deleting 70-odd
  rows removes most of them.
- Master bars 2 dB or more off c54: 20 (-2.0), 31 (-2.3), 84 (+2.2), 92 (+2.1); 1.5 dB or more: 11, 12, 16, 25, 40, 82.
  Bars 84 and 92 are findings 1 and 4, bar 82 finding 3.
- Bars 61-64 and 79-82 balance (timpani and low brass against the strings): unchanged within 1 dB of c54 as stem levels;
  no change proposed beyond the "ff" trims above, which lower Oboe 1, Flute 2, the bassoons and the basses by the amount
  their rows already do.

## Do not touch

Horn 1's and Bass clarinet's region gains (Horn 1 theme sd 1.5 dB, no pitch over 1.9 dB off); the envelope edge slew
(3 dB per second) and `env_simplify_db` 0.2; the c56 doubles and their bow-change times (only the CC7 values per span
change in finding 4); the CC11 morendo from 298.3 on the strings; Flute 1 "LegRep RRx4" -9.5 (qn 136 at -48.3, c54
-48.4); the tremolo rows' region volumes and the bar 63 CC7 falls on Violins I / II and Violoncellos; the celli's CC11
-10 lanes on 238 / 244 / 253; the 172 stroke's velocity 100 with its level (only the lane it is written in changes).
No per-note fader move goes back, and none is proposed here.
