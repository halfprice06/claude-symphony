# Cycle 58, critic B: balance and levels (render under review: c57)

Nobody listened. Every figure is measured on the c57 stems and master (30 ms frames, 10 ms hop) unless marked
"simulated" or "inferred". Scripts and intermediate tables: `cycles/c58/critic_scripts/B/` (`sort2.py`, `classify.py`,
`carry_tags.txt`, `carry_class.json`, `shapes.txt`, `pitchres.py/.txt`, `dynmap.py/.txt`, `theme.py`, `theme2.py`,
`themesim.py`, `horn4.py`, `horn4b.py`, `bars.py`, `delsim.py`). The variant `parts.json` files there were built with
`tools/score_to_parts.py` into the scratch folder only (C57=0 with `STP_DROP_TAGS` per rule; `STP_DUMP_VP` dumps).
`build_reaper.py`, `render_cycle.py`, REAPER and the bridge were not used.

## Manual notes (2021 HO Opus manual)

| Manual says (PDF page) | Where it applies | Does the render follow it |
|---|---|---|
| Note velocity is for short articulations, CCs for sustained ones (p. 53) | String shorts on "Stac RRx9" with CC11 parked at 120 (`SHORT_CC11_PARK`) | No since c57: the park's level return was in the envelope and is gone; the shorts play 6-11 dB over their line at velocity 77 (finding 2) |
| CC7 sets the level relative to other instruments, CC11 shapes each instrument's dynamics (p. 64) | Track gain and dynamic trims against per-bar rows | Partly: 368 bar rows still do the work of CC11 and of sample levels (finding 1) |
| "Leg Bow Change" accents the second note; velocity sets the timing of the transition (p. 79) | Celli bars 15-22, every half note on "Leg BC MAX" at velocity 124 | The accent is 7-10 dB over the note body for about 0.3 s and covers the theme (finding 3) |
| Short string rows: CC11 and velocity control loudness, velocity the dynamic layer (p. 92) | Same passages as row 1 | Velocity is not used for the level yet |

EW-TEMPLATE-PLAN sections my lens touches that are not applied: 5 (legato velocity 90-98; ours 124 on Leg BC / Leg
Slur), 6 (shorts: CC parked, dynamics by velocity 24-52; ours velocity 77 with no level return), 10 (short-note
velocity by position in the beat; our metric steps were envelope steps and are gone).

## Finding 1 (largest). The carry rows, sorted by cause

File state: `build/balance57.json` holds 368 rows (358 bar rows and the ten 16 qn Violins I rows), not 375 + 10.

Method (measured): for each row, the c56 envelope was rebuilt 33 times with one per-note rule left out
(`STP_DROP_TAGS`), and the rule's share of the row is its power-weighted mean over the row's span on the c56 stem. On
253 of 368 rows the shares add up to the fitted value within 0.5 dB; on the others a remainder is left (non-additivity
from c56's `NOTE_LEVEL` pass, and timpani and harp, which `STP_DROP_TAGS` does not reach: sorted by hand from the dump).
The rule with the largest share decides the cause. Every row with its shares: `carry_tags.txt`; with its cause: `carry_class.json`.

Totals: a 70, b 106, c 100, d 92.

| cause | rows | rules behind them (rows) |
|---|---|---|
| a: a dynamic or role the mapping should give | 70 | theme per-note levels `steady_level` 26 + the ten 16 qn rows; `held_decresc` 14; `pickup` 8; swell cap `pre` 7; parked shorts `park` 2; timpani and harp metric steps 3 |
| b: per-pitch or per-row sample level | 106 | `ntrim` 47; `rebow` 29; `early` 20; `bloomv` 4; `rowtrim` 3; `steady_body` 2; `loop` 1 |
| c: bar mean of a shape that no longer exists | 100 | config shapes under 2 s 51; accent swells 35; rows with no source in c56 (post-render refit) 9; timpani metric steps that end in a rest 3; other 2 |
| d: a level decision of a phrase or more | 92 | unison boost `keep:note` (+3 dB, two players on one sample) 46; config shapes of 2-45 s on one held note 36; timpani roll levels 9; harp final fade 1 |

Per track. Each cell: rows, then what deleting them does to the c57 stem over those bars in dB (power mean, and the
range per row), then the two commonest rules.

| track | rows | a mapping | b sample level | c residue | d slow decision |
|---|---|---|---|---|---|
| Flute 1 | 5 | - | 2: +1.9 (-2.1..+4.4); ntrim | 3: -2.3 (-2.5..-2.2); accent | - |
| Flute 2 | 6 | - | 5: -1.3 (-4.6..+3.6); ntrim 3, early 2 | 1: -2.1; accent | - |
| Oboe 1 | 14 | 2: -4.2 (-6.6..+3.6); held_decresc, pickup | 3: +4.4 (-7.5..+5.2); ntrim | 4: -2.5 (-3.0..-2.1); shape 2, accent 2 | 5: -3.5 (-6.4..-2.7); unison 3, shape 2 |
| Oboe 2 | 7 | 1: +3.8; held_decresc | 1: -2.6; early | 5: -2.4 (-2.7..-2.0); accent 4 | - |
| Cor anglais | 2 | - | - | 1: -6.7; shape | 1: -3.5; shape |
| Clarinet 1 | 20 | 1: -3.2; pickup | - | 5: -2.5 (-2.6..-2.1); accent 3 | 14: -3.3 (-6.0..-2.5); unison 14 |
| Clarinet 2 | 2 | - | - | 2: -2.2; accent | - |
| Bass clarinet | 10 | 4: -0.4 (-4.7..+3.1); held_decresc 2 | 4: +2.9 (+2.0..+3.8); ntrim | - | 2: -3.7 (-4.3..-2.5); shape |
| Bassoon 1 | 15 | 3: -2.7 (-3.0..-2.2); swell cap | 4: +2.4 (-2.8..+4.5); ntrim 2, early 2 | 2: -3.0; accent | 6: -3.1 (-4.1..-2.1); unison 6 |
| Bassoon 2 | 11 | 5: -1.4 (-3.5..+4.7); swell cap 3, held_decresc 2 | 1: +4.2; ntrim | 1: -2.4; accent | 4: -1.8 (-2.5..+3.8); shape |
| Contrabassoon | 6 | 2: +3.6; held_decresc | - | 3: -2.4; accent | 1: -2.1; shape |
| Horn 1 | 16 | - | 2: -4.2 (-4.3..+5.8); ntrim | 8: -2.9 (-9.9..-2.3); shape 7 | 6: -2.4 (-3.6..+6.1); unison 3, shape 3 |
| Horn 2 | 8 | - | 2: -4.1; ntrim | 2: +2.6; no source | 4: -2.4; unison 2, shape 2 |
| Horn 3 | 14 | - | 1: +2.1; ntrim | 2: -2.2; no source, shape | 11: -2.9 (-4.2..+4.2); unison 8, shape 3 |
| Horn 4 | 17 | - | 13: +6.2 (-2.9..+9.4); ntrim 12 | 1: +2.0; no source | 3: +3.8; shape |
| Trumpets 1-3 | 12 | - | 1: -4.0; ntrim | 4: -2.7; accent | 7: -2.2; unison 4, shape 3 |
| Trombones 1-2, Tuba | 15 | - | - | 7: -0.4 (-2.6..+4.0); shape 5, accent 2 | 8: -0.9 (-4.5..+4.2); unison 6 |
| Timpani | 14 | 2: +3.2 (+2.1..+4.4); metric | - | 3: +3.0; metric step ending in a rest | 9: 0.0 (-3.1..+4.2); roll levels |
| Harp | 2 | 1: +4.3; chord level | - | - | 1: +2.3; final fade |
| Violins I | 37 | 29: +1.1 (-5.6..+8.7); steady_level 17, 16 qn rows 10 | 3: +3.5; rowtrim, early | 5: +2.9 (-3.8..+6.7); shape | - |
| Violins II | 31 | 7: +5.3 (+2.9..+7.7); steady_level | 16: -1.1 (-8.4..+3.8); rebow 11, steady_body 2 | 6: +2.3; shape 5 | 2: +4.8; shape |
| Violas | 24 | 6: +2.8 (-4.2..+4.5); steady_level 2, pickup 2 | 8: +1.6 (-4.9..+5.2); rebow 4, early 2 | 10: +1.9 (-3.1..+4.9); shape 4, no source 3 | - |
| Violoncellos | 43 | 4: +1.6; held_decresc 2 | 22: 0.0 (-7.7..+4.7); early 11, ntrim 5 | 16: -0.1 (-6.1..+4.0); shape 13 | 1: +2.7; shape |
| Double basses | 29 | 3: +3.2; held_decresc | 17: -0.4 (-10.2..+8.5); rebow 9, ntrim 8 | 2: -2.5 | 7: -1.7 (-4.9..+2.6); shape |
| Horns a2, Trumpets a2, stac aliases | 8 | - | 1: -2.2 | 7: -0.9 (Horns a2 +2.3..+8.0, others -2.6..-5.5) | - |

Cost at the mix (simulated on the sum of the dry c57 stems): deleting all 368 rows moves 45 bars by 1 dB or more and
16 by 2 dB or more (-6.3 dB bar 7, -3.7 bar 21, -3.5 bar 181, -3.4 bars 47 and 86, +3.3 bar 87, +2.5 bar 139). Group c
alone: 19 bars / 8 bars. Group b alone: 10 / 3. Group a alone: 11 / 4.

Points per second: without any carry row the strings' `vol_db` lanes have 0.48-0.76 corner points per second (with:
0.69-1.00). The rest is hairpin gain (24-45 items per string track), roles (15-26) and slow shapes (14-28). Deleting the
rows alone does not reach 0.4; hairpin gain is the next source (inferred from the item counts, not simulated).

Replacements, instrument side (file and key):

- **Violins I theme, 29 rows (a).** Net effect of the bar rows plus the 16 qn rows per span: 56-128 -0.7 dB, 128-160
  +3.6 dB, 536-576 +0.3 dB (power means). Delete all 29. Add one role row `build/roles.json` Violins I `[128, 160, 3]`
  (edges in the rests). Expected: bars within -2.4..+3.6 dB of now in 56-128; bars 135-137 rise 4.8-7.6 dB, which is
  wanted (Violins I mf theme reads -46.8 / -47.9 / -44.4 dB there against celli -45.5 / -37.5 / -38.4).
- **Violins II and Violas theme doubling, 9 rows (a).** Violins II 104-128 rows add -4.6 dB, 552-572 -3.2 dB; Violas
  100-128 -2.0 dB. Delete; put the Violins II doubling notes on "Sus MAX" as Violins I (`build/score_config.py`, the
  `_C57_THEME` spans, extended to Violins II 80.5-82, 104-128, 552-572); then one role row per span if a range render
  still shows them over Violins I (expected -3 to -4).
- **Unison boost, 46 rows (d).** Keep, as role rows: in `tools/score_to_parts.py` write `UNI_BOOST` as one "role" span
  per run of three or more kept unison notes, with its edges in the rests around the run, and nothing for shorter runs.
  Cost of the shorter runs: -3 dB on one or two notes.
- **Held shapes of 2-45 s on one note, 36 rows (d).** They were dropped because `slow_min_onsets` is 2. Set
  `VOL_SLOW_ONLY["slow_min_onsets"] = 1` with `slow_min_s = 4.0` in `build/score_config.py`, so the coda fade
  (695.5-732 -3.5 dB, 724.25-729 -7 dB, 711-732 +1.5 dB), the basses' pedal 464.2-484 (+5 dB) and the bars 121-123
  rows return as slow rows. Better where the note has a printed hairpin: the same dB as CC11 on that hairpin.
- **`held_decresc`, 14 rows (a).** The -3 dB fall of a diminuendo on one held note: move it into the hairpin's CC11 end
  value (-10 units at the measured 0.3 dB per unit on string Sus MAX; winds need their own slope). Cost until then:
  +2.7..+3.9 dB at the end of 14 held diminuendos.
- **Swell cap `pre`, 7 rows (a).** Bassoon 1 584-596, 692-696; Bassoon 2 600-608, 680-688: `SWELL_CAP_TO_VOL_DB_PER_CC
  = None` in `build/score_config.py`, so CC11 carries the whole swell. Cost until then: -2.2..-3.3 dB on those swells.
- **`ntrim`, 47 rows (b).** Region gains (finding 4) for the pitches that recur; Horn 4 needs a layer filter (finding
  5); the others are deleted (cost per row in `carry_tags.txt`, -4.6..+5.6 dB, one bar each).
- **`rebow`, 29 rows (b).** Level difference between the first piece and the re-bow pieces. Delete with item 3 of the
  notes (no split under 6 s, held notes start on Sus MAX). Largest costs: Double basses 720-724 -10.2, 496-516 +6.5 to
  +8.5; Violoncellos 20-28 -4.7..-6.6; Violins II 192-196 -7.5.
- **`early`, 20 rows (b).** Bar means of fills on soft legato targets. Delete; cost -1.9..-6.0 dB on soft entries at
  -47..-63 dB (Violins II 420, Violins I 436, celli 11 bars). Replacement: legato velocity and overlap (item 4).
- **`bloomv`, 4 rows (b).** Soft re-attacks on "Leg Slur MAX" that swell: play them on "Sus MAX" (row choice).
- **Group c, 100 rows.** Delete without replacement. The 35 accent rows are +1.4..+2.4 dB bar means of accent swells
  in bars 31-33, 41, 72, 82, 138, 143; item 2 (accents by CC11) replaces them. Largest single costs: Horn 1 bar 111
  -9.9 dB (a +13 dB shape on one p note; if it is a solo it needs a role row or a higher CC11), Cor anglais bar 7 -6.7,
  Oboe 1 bars 125 and 145, celli bar 88 -6.1.

## Finding 2. String shorts are 6-11 dB too loud since the park's envelope half went

Where: celli 338.5-340, 343.5-348, 464-484, 512-520; Violas 350.5-352, 355.5-360; Violins I 374-386; Violins II
362-372 (184 notes inside 45 `park` items).

What: `SHORT_CC11_PARK` holds CC11 at 120 over short-row runs and took the level difference back in the volume
envelope. c57 dropped the envelope half (`park` is in `VOL_SLOW_ONLY["drop"]`) and kept CC11 at 120.

Evidence (measured): celli 338.5 / 339 / 339.5 staccato eighths -38 / -37 / -39 dB in c56, -31 / -27 / -28 in c57;
the Leg BC note before them is -37. Violas 350.5-352: -47 -> -36. Front level c57 minus c56 over all parked notes:
median +0.1..+4.0 per track, maximum +11.4 (celli), +10.8 (Violas), +6.1 (Violins I), +5.5 (Violins II). Master bars
85 / 88 / 89 are +4.3 / +1.8 / +2.5 dB over c56 for this reason; no carry row covers bar 85.

Fix: `build/score_config.py` line 3517, `SHORT_CC11_PARK = None` (CC11 follows the printed dynamic again; level-exact,
the c50 state). Expected: the listed notes back within 1 dB of c56, bars 85-89 within 1.5 dB. If the park is kept for
its timbre, the level must come from velocity (EastWest: 24-52 with the CC parked; ours 77), fitted on a range render
after critic A's velocity table. Then delete the five carry rows that hold the park's bar mean (Violas 356-360; celli
344-348, 464-480, 512-516, 516-520).

## Finding 3. Theme over the celli, bars 15-22

Measured per quarter (Violins I minus Violoncellos, power over each of the 32 quarters; this measure reads lower than
the actor's): median +2.2, lower quartile -0.5, 10 quarters under 0.

Causes (measured):
1. Celli half notes on "Leg BC MAX" at velocity 124: the transition into Ab3 (66), G3 (68), F3 (72), G3 (82) and the
   end of F3 (64, 80) reads -33..-38 dB for about 0.3 s against bodies of -43..-45. 11 % of the celli frames in the
   span are 6 dB or more over the span median.
2. Carry rows work against the theme: Violins I -1.1 / -2.8 / -1.1 / +0.9 / -2.2 net per bar group, celli +2.2 on
   64-68 and +3.0 on 84-88.
3. Bar 22: Violins I falls f > mf to CC11 62-73 (instrument level -55 dB) while the celli stay at CC11 79 (-44).
   Violins I Sus MAX gives 0.31 dB per CC11 unit on the theme spans (n 131, sd 2.4 dB, no pitch more than 3 dB out
   with 3 or more notes).

Simulated on the c57 stems (same measure; add about 2.2 to compare with the actor's 1.7):

| change | median | lower quartile | quarters under 0 |
|---|---|---|---|
| as rendered | +2.2 | -0.5 | 10 |
| A: carry rows of both tracks deleted in 56-88 | +3.5 | +0.9 | 5 |
| A + celli role `[56, 88, -2]` -> `-3.5` | +5.0 | +2.4 | 2 |
| A + role + Violins I `soft_trim_db.mf` 1.0 -> 3.5 | +5.0 | +2.6 | 2 (bar 22: -3.6 -> +5.0) |
| the same with the celli transitions at body level (upper bound for a legato-velocity fix) | +6.7 | +4.3 | 2 |

Cheapest fix that is a role or dynamic mapping: A plus `build/roles.json` Violoncellos `[56, 88, -2]` -> `[56, 88,
-3.5]`. Lower quartile +2.9 dB over now, so about 4.6 on the actor's measure (target 3.9). The mf trim is optional and
moves every Violins I mf passage by up to 2.5 dB, so it needs a look at the other mf passages first. The remaining two
quarters under 0 are the transitions of cause 1: celli "Leg BC MAX" velocity 124 -> 92-98 (item 4), range render first.

## Finding 4. Region gains refitted on the c57 render

Method (measured): note body (0.12-0.7 s after the note-on, notes of 0.3 s or more, alone on the track) minus the
written envelope gives the instrument's output; the model is the track's running median over CC11 (plus or minus 8
units); the residual is listed per pitch and row where 3 or more notes agree. Full table: `pitchres.txt`. Values are
the new total for `mix.json` `tracks[...]["region_gain_db"]`; expected residual after: within 1.5 dB.

| track | pitch | residual now (n; rows) | region gain now | new |
|---|---|---|---|---|
| Flute 2 | Eb6 (87) | Sus MAX +10.9 (4, quartiles +10.7..+10.9); Leg Slur -0.6 (1) | Leg Slur -5 | add Sus MAX -10 |
| Flute 2 | F6 (89) | Sus MAX +9.1 (2); Leg Slur +2.2 (3) | Leg Slur -3 | Sus MAX -8 (2 notes only), Leg Slur -5 |
| Flute 2 | Db6 (85) | -6.0 (4) | none | +6 |
| Flute 2 | G5 (79) | -5.1 (8) | none | +5 |
| Flute 1 | D6 (86) | Sus MAX -10.4 (5); Leg Slur -4.8 (3) | none | Sus MAX +8, Leg Slur +4.5 |
| Flute 1 | G6 (91) | Sus MAX +4.9 (4) | -5 | Sus MAX -10 |
| Flute 1 | Ab5 (80) | -5.5 (12, quartiles -6.0..-4.3) | none | +5 |
| Oboe 1 | F5 (77) | Sus MAX +5.9 (10); Leg Slur +0.2 (9) | -2.5 | Sus MAX -8.5, Leg Slur -2.5 |
| Oboe 1 | C5 (72) | Sus MAX -3.4 (8); Leg Slur -0.9 (7) | Leg Slur +3 | every row +3 |
| Oboe 1 | Ab5 (80) | +2.6 (11) | -4 | -6.5 |
| Oboe 2 | F5 (77) | +9.0 (3) | none | -9 |
| Oboe 2 | C5 (72) | -3.9 (10) | none | +4 |
| Oboe 2 | G5 (79), Bb4 (70) | +4.8 (3), +4.4 (3) | none | -4.5, -4 |
| Clarinet 1 | Eb5 (75) | -4.5 (7) | none | +4.5 |
| Bass clarinet | Ab2 (44) | +4.8 (5) | none | -4.5 |
| Bassoon 1 | Ab3 (56) | Sus MAX -3.3 (8); Leg Slur -5.5 (5) | none | Sus MAX +3.5, Leg Slur +5.5 |
| Bassoon 1 | B3 (59) | +3.7 (8, quartiles +3.7..+3.7) | none | -3.5 |
| Horn 1 | D4 (62) | Leg Slur +3.9 (4) | none | Leg Slur -4 |
| Horn 2 | Eb4 (63) | Sus MAX -5.9 (9, quartiles -6.5..+0.5) | none | Sus MAX +3 (wide spread) |
| Horn 3 | C4 (60) | +3.7 (35) | none | -3.5 |
| Horn 3 | Ab3 (56) | -3.7 (14) | none | +3.5 |
| Trumpet 1 | Db5 (73) | -3.8 (5) | none | +3.5 |
| Trombone 1 | D4 (62) | +5.7 (4) | none | -5.5 |
| Tuba | Ab1 (32) | -4.7 (6) | none | +4.5 |
| Tuba | D2, Eb2, F2 | +3.1 (6), +3.2 (3), +3.8 (3) | none | -3, -3, -3.5 |
| Violoncellos | Ab2 (44) | +7.9 (4; +4.4..+9.6 across three rows) | none | -6 |
| Double basses | Ab2 (44) | -5.8 (5) | -6 | 0 |
| Double basses | G2 (43) | -3.1 (10) | -4 | -1 |
| Horns a2 | F4 (65), G3 (55) | +4.9 (4), -4.8 (3) | none | -5, +4.5 |

Differences from the list in the notes: Bassoon 1 Ab3 reads -3.6 here (not -7.7), Horn 1 D4 +3.6 on the legato row
only, Flute 1 D6 -10.4 on Sus MAX. Violins II D4 (+6.7) and Double basses Ab1 (-5.7) do not show against the CC11
model (Ab1 +1.6, n 14, with its -5 gain in place): they read out of line against their neighbours because of the
envelope around them, not the sample. Leave both until the carry rows are gone, then measure again. Double basses
Eb2 pizzicato reads +9.3 (n 4) with the +5 gain that was fitted for the bowed rows: restrict that entry to
`"rows": ["Sus MAX", "Leg Slur MAX"]`.

## Finding 5. Horn 4 bars 19-22, and Horn 3 beside it

Where: Horn 4 qn 72-88 (printed p, no hairpin): F3 at 72, 76, 80; G3 at 82, 84, 86.

Evidence (measured): instrument output at CC11 46: F3 -55.1 / -54.0 / -53.7 dB, G3 -63.6 / -63.3 / -63.7. Over the
whole movement at CC11 41-52: D3 -59, E3 -54, F3 -55 (n 6) against Gb3 -64, G3 -64 (n 4), Ab3 -66; at CC11 81-100:
F3 -43 (n 8), G3 -43 (n 11). The soft layer's samples from F3 down are 9 dB hot; the loud layer is even. The carry
rows 72-80 (-8.6) and 80-84 (-6.2) cut the F3 bars; the row of bar 21 also cuts the G3 at 82-84, which reads -56.7
against -47.4 for the F3 before it. That is the 4.7 dB fall. Without the rows the F3s would stand 9-10 dB over the G3s.

Fix: a region gain limited to the soft layer. `tools/build_reaper.py` `region_gain()`: add an optional layer filter to
the spec (by group name or index of the 1FH KS Master's dynamic layers; the actor has to read the names from the
patch), then `mix.json` Horn 4 `region_gain_db`: `{"rows": ["Sus MAX"], "layers": [soft layer], "pitch_db": {"48": -9,
"50": -5, "52": -9, "53": -9}}`. Expected: F3 and G3 within 1.5 dB at p, f unchanged; then delete Horn 4's 12 `ntrim`
rows. A gain on all layers is wrong: it would cut F3 at f by 9 dB. If the layer filter cannot be built, the fault
stays and is listed.

Also measured: Horn 4 `soft_trim_db` falls from p 14.4 to mp 6.0, so mp notes (median -53.3 dB, n 14) are under p
notes (-51.1, n 17). Set mp to 9.0 (Horn 3 has 9.2). Horn 3 in the same bars: C4 -59.9 against Db4 / B3 / D4 -64..-65
(the C4 gain of finding 4), and its Db4 notes at 76 and 80 dip 9 dB for 0.15 s in mid-note with CC11 falling 46 -> 36
inside the note (not my lens; for critic A).

## Finding 6. The 15 master bars more than 1.5 dB over c56, and the dynamic mapping between instruments

Bars over c56 (measured, master RMS per bar; the stems that rose most):

| bar | master | cause | fix |
|---|---|---|---|
| 21 | +5.5 | Violins II -40.4 -> -26.8: the notes at 80.5-82 double the theme an octave lower on "Sus Marc LITE" at CC11 103-107 (the sf of 78 holds until the mp of 82.5); c56 held them with -13.5..-15.4 dB note cuts; the carry row is +8.4 | delete rows 76-80 and 80-84 (-8.4); these notes on "Sus MAX" (finding 1); expected about -36, Violins I is -34 |
| 181, 182 | +2.8, +5.4 | final ppp chord: Double basses row +10.2, celli +7.7, Violins I +3.8 (re-bow fills and the dropped fade) | delete the rows; restore the fade as a slow row (finding 1, `slow_min_onsets`) |
| 85, 88, 89 | +4.3, +1.8, +2.5 | parked shorts (finding 2) | `SHORT_CC11_PARK = None` |
| 7 | +3.1 | Cor anglais row +6.7, celli row +4.7 | delete; Cor anglais then 3.6 dB under c56 in bar 7: a role row over the solo if the solo needs it |
| 48, 103, 44 | +2.1, +1.8, +1.5 | Horn 1 +3.9..+5.1 (rows +2.3 / +2.4 and dropped per-note cuts) | delete rows; Horn 1 D4 legato gain -4 |
| 146 | +1.9 | Oboe 1 582 (p, CC11 41) -47.5 -> -43.4, no row | none proposed; within the p range of the winds |
| 132 | +1.8 | celli 526 (Sus Marc LITE, velocity 111) -31 -> -24 | velocity 111 -> 91 as its neighbours (the accent was an envelope item before) |
| 40, 13, 5 | +1.6 each | Violins I 16 qn rows +5.6 / +4.0, basses +2.3 | delete rows |

Simulated on the dry stems: after deleting every row, bars 85 and 87 remain over c56 (+4.4, +4.6, the parked shorts)
and bar 35 is 3.6 dB under.

Dynamic mapping (measured, median stem body level of notes of 0.3 s or more per printed dynamic; `dynmap.txt`):

- p: winds -44.5..-52.3, Horn 1 -46.7, Horns 3-4 -51, strings -49.4..-52.1, harp -50.4. pp: brass -54..-58, strings
  -50.4..-58.7. f: winds -36.5..-42.9, horns -40.2..-42.8, trumpets -37.2..-40.4, trombones and tuba -36.6..-39.8,
  strings -39.3..-42.2. Horns sit 3-5 dB under trumpets and trombones at f, which agrees with Rimsky-Korsakov (two
  horns to one trumpet or trombone in forte, `reference-books/text/rimsky-principles/p0041.txt`, `p0051.txt`).
- Steps that are missing or reversed: Clarinet 1 p / mp / mf -46.5 / -46.7 / -47.0 (f -40.0); Violins II mp -47.8, mf
  -49.2; Horn 4 p -51.1, mp -53.3; Bassoon 1 mp -44.7, mf -44.9; Horn 1 p to f 3.9 dB (trombones 12-14). Proposed
  (inferred from medians of 13-29 notes, roles mixed): Clarinet 1 `soft_trim_db` mp 2.2 -> 3.5, mf 0.1 -> 3.0;
  Violins II mf -0.8 -> 1.0; Horn 4 mp 6.0 -> 9.0. Horn 1 and Bassoon 1: no change proposed, their soft trims carry
  solo roles.
- Violins II pp is -58.7 (n 69) against Violins I -52.1, Violas -53.6, celli -55.3, Double basses -50.4. The basses at
  pp are the loudest string stem; `soft_trim_db.pp` 8.5 -> 6.5 would put them at -52.4 (inferred; check bars 6-7, where
  c48 raised them on purpose).
- Deleting every carry row changes these medians by less than 1.5 dB except ppp strings (-3.7..-7.0, the final chord),
  Oboe 1 p and mf (-6.2), Flute 2 p (-4.6), Trumpet 2 pp (-4.0), Horn 4 soft dynamics (+1.0..+3.1).

## Do not touch

The Violins I theme on "Sus MAX" with its c57 leads; the roles of bars 15-22 other than the celli value; trumpet,
trombone and tuba dynamic trims (f and ff steps of 3.5-7 dB, horns 3-5 dB under at f); the c57 region gains that read
within 1.5 dB (Double basses F1, G1, C2, Db2, E2, F2; Clarinet 1 Ab4, G5, Ab5, Bb5; Clarinet 2 Ab4; Bassoon 1 Db4;
Horn 3 D4; Cor anglais Ab4; Violoncellos G2, Eb3); the timpani roll levels and settle in the envelope; `REP_MIN_GAP`.
