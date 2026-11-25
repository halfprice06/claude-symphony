# Cycle 59, critic B: balance and levels (render under review: c58)

Nobody listened. Every figure is measured on the c58 stems and master (30 ms frames, 10 ms hop, power means) against
the c57 and c56 renders, unless marked "inferred". "Margin" is a melody stem's level minus the power sum of all other
dry stems over the same beat. "Instrument output" is stem level minus the written envelope. Scripts and tables:
`cycles/c59/critic_scripts/B/` (`lib59.py`, `bars.py`, `shifts.py`, `batch.py` / `batch.txt`, `passage.py`, `trace.py`,
`envd.py`, `notes.py`, `cccurve.py` / `cccurve.json`, `theme.py`, `dynmap.py`, `hp.py` / `hp_items.json`, `pps.py`,
`thin.py`). The variant `parts.json` files there (`v_base`, `v_nohp`, `v_norole`, `v_none`) were built with
`tools/score_to_parts.py` into the scratch folder only; `v_base` is byte-identical to `build/parts.json`.
`build_reaper.py` was used only cut before `ENV_LUA`. `render_cycle.py`, REAPER and the bridge were not used.

Not done this cycle: I did not re-read `EW-TEMPLATE-PLAN.md`, `LEARNINGS.md` or `HISTORY.md` in full (time went to the
measurements the coordinator asked for). The plan sections c58's critic B listed as not applied (5 legato velocity
90-98, 6 shorts by velocity, 10 short-note velocity by beat position) are still open according to c58 `CHANGES.md`.

## Manual notes (2021 HO Opus manual)

| Manual says (PDF page) | Where it applies | Does the render follow it |
|---|---|---|
| CC7 sets a level relative to other instruments; CC11 shapes each instrument's own dynamics (p. 64) | Solo and accompaniment roles that left the envelope in c58 | Partly. 17 role rows became CC11 offsets, 62 were dropped with nothing in their place (findings 1 and 4) |
| Leg Bow Change accents the second note; CC11 and CC1 set loudness (p. 79) | Celli half notes bars 15-22; Cello solo 684, 688, 692 | The celli's Leg BC MAX row reads 5.5 dB over Sus MAX at one CC11 (10 pitches), so the phrase entry on Sus MAX is the weakest note (finding 5) |
| Divisi instruments are recorded with the close microphones only (p. 89) | Cello solo track (Celli KS Master DIV A) | Yes; its rows differ in level by up to 10 dB at one CC11 (finding 3) |

## The 23 master bars over c57 and the 17 under (measured; c56 in brackets where it decides)

| bars | master against c57 | stems that moved | judgement |
|---|---|---|---|
| 171, 172 | +3.7, +4.7 | Cello solo -35.1 -> -31.3, -35.3 -> -29.5 (c56 -35.5, -35.2) | fault, finding 3 |
| 173, 174 | -1.7, -2.8 | Cello solo crest -37.3 -> -41.3 | fault, finding 3 |
| 74 | +4.4 | Flute 1 solo -37.1 -> -32.2 | fault, finding 1 row 6 |
| 175-180 | +1.6 to +4.2 | Violins I +2.5 to +5.8, trombones +2.4 to +3.5 | fault in 179-180, finding 1 row 12 |
| 15 | +3.0 | Violins I +3.6, basses +3.6 | Violins I wanted; see finding 5 |
| 25, 26, 27 | +1.6, +2.0, +2.8 | Violins I +2.3 to +6.2, Violins II +3.6 to +4.5, celli +3 to +5.2 | ff tutti, no melody covered; theme margin -10.8 -> -9.2 |
| 81, 83 | +2.2, +2.0 | Violins II +4.8, Trombone 1 +4.1; Violins I +7.3, Violas +6.5 | tutti; not a solo balance |
| 115-118 | +1.8 to +2.3 | celli +7.1 to +8.3 (115-116), Horns a2 +8.2 and Flute 1 +6 to +8.4 (116-117), Tuba +4 | accompaniment up; wind tune margin 455.5-479.5 unchanged at the median (-7.5 -> -7.4), lower quartile -9.2 -> -10.3 |
| 61, 156 | +1.6, +1.5 | Horn 4 -47.3 -> -36.8, -49.6 -> -41.5 | fault, finding 2 |
| 139, 162 | +1.6, +2.3 | Violins I +5.6; Violins I / II +3.2, Tuba +4 | recap theme: wanted (finding 1 row 13) |
| 7 (6, 8) | -7.8 (-1.6, -2.0) | Cor anglais -29.4 -> -37.8 (c56 -32.6), celli -5.6 | finding 1 row 1 |
| 47, 50, 147-153 | -1.8 to -4.0 | celli -3.0 to -5.4, Horn 1 -2.5 to -4.4, basses -7 | second theme: margins unchanged within 1 dB; master 1.4-3.6 dB under c56; finding 1 row 14 |
| 21 | -3.2 | Violins II -27.8 -> -37.5 (c56 -41.3) | wanted |
| 85, 86 | -1.6, -2.8 | celli -1.6, -2.8 | fugato subject; within 1.4 dB of c56 in bar 86 |
| 3, 5 | -1.7, -1.7 | celli -3.4, basses -4.7 | Lento accompaniment; back within 1 dB of c56 |
| 78 | -1.5 | Bass clarinet solo -40.1 -> -44.6 | fault, finding 1 row 4 |

## Finding 1 (largest). Solos and melodies that sit wrong against their accompaniment, with the fix for each

Four causes account for the list (all measured):
- a. A role row that covers one or two notes is dropped unless it lasts 4 s (`LEVEL_TO_CC` `min_s`): 62 rows gone
  (`parts.json` `vol_slow_only.to_cc`, entries `role` with `False`). Finding 4 gives the CC11 values for those that matter.
- b. Oboe 1's soft dynamics were held up by carry rows, not by its trims. Every Oboe 1 note at p, mp or mf lost 2.3 to
  7.6 dB of envelope (14 notes: c57 envelope +1.2..+9.4, c58 -3.2..+2.9). Oboe 1 now reads p -55.4, mf -53.7, f -43.1,
  ff -38.9 dB (median note body) against Clarinet 1 p -47.0, mf -42.8, f -39.3 and Cor anglais p -45.5.
- c. Region gains fitted on the c57 render moved long solo notes: Flute 1 A-flat 5 +5 dB, Bass clarinet A-flat 2 -4.5 dB.
- d. Row-level steps that per-note items used to hide: Violins I Sus MAX over Leg Slur MAX at pp (+5.4 dB on E-flat 5 at
  711.86), Cello solo rows (finding 3), Horn 4's soft layer (finding 2).

Slopes used below are this render's own, per track, from `cccurve.json` (note bodies, envelope removed, pitch and row
effects removed). They differ from the family values in `LEVEL_TO_CC` (0.30 / 0.21 / 0.29 dB per unit): winds give 0.07
dB per unit between CC11 88 and 104 (244 notes) and 0.16 above 104; Cor anglais 0.00 at 88-104; horns 0.55-0.61 at
46-58; Flute 1 1.3 at 34-58 (5 notes, thin).

| # | passage | now (c57 in brackets) | fix (file, key) | expected |
|---|---|---|---|---|
| 1 | Cor anglais solo, bar 7 (qn 24-28) | stem -37.8 (-29.4; c56 -32.6). Margin +6.1, +8.7, +7.6, +3.0 per beat (+7.0, +14.8, +12.7, +4.1). G4 at 24 reads -45.0 at CC11 66->87, 7 dB under the B-flat 4 of bar 5 | The crest cannot rise by CC11 (flat 88-104). `build/roles.json` Cor anglais `[24, 28, 3]` (three notes; `ROLE_EDGE` makes the edges 2 s ramps) and, in the phrase lane, start the hairpin at CC11 74 instead of 66 at qn 24 (`HP_TARGET_AT["CA"]` in `score_config.py`, or a flat CC11 offset of +8 over 23.9-25), crest unchanged at 87 | bar 7 about -34.5; margin +9 to +11; G4 +1.7 dB from CC11 (0.21 dB per unit at 58-72) |
| 2 | Horn 1, bars 103-104 (qn 408-416), mf solo with Bassoon 1 | margin 412-415: -8.8, -7.4, -7.6, -8.2 (-1.2, -2.6, -4.7, -6.6). D4 at 412 -42.1 (-34.5), B-flat 4 tenuto at 413 on Sus MAX -42.2 (-38.2). Dropped: shapes +5.5 (410.95) and +3.5 (414.95), D4 legato gain -4 added | Phrase CC11 over 412-416: 86 -> 94 at the B-flat 4 (413-415), 90 on D4 and A4 (now 79-89), written as a flat CC11 offset over the span (a `LEVEL_TO_CC`-style offset keyed to 412-416, +8 units) or through `HP_TARGET_AT["Hn1"]` at 413 and 415; Horn 1 slope 0.43-0.51 dB per unit at 72-104. `mix.json` Horn 1 `region_gain_db` B-flat 4 (70) on `Sus MAX` +3 (row reads -2.9 against +7.2 on Leg Slur MAX, 3 and 2 notes) | bar 104 notes +3 to +4 dB; margin about -4 to -5 |
| 3 | Horn 1, bar 111 (qn 440-444), p, held A-flat 4 | -54.9 (-44.9). Not a solo: the line now rises as printed, -54.9 / -53.1 / -46.7 / -40.7 over bars 111-114 (c57 fell 8 dB from bar 111 to 112). Horn 4's F3 beside it reads -40.7 | No lift on the note. Start the six-bar crescendo at CC11 52 instead of 46 (440: 52, 444: 60, 448: 69 as now); the rest is finding 2 | A-flat 4 about -51.5; Horn 4 F3 at -47 |
| 4 | Bass clarinet Solo, bars 77-78 (qn 304.5-310), mf espr. | A-flat 2 tenuto at 308 on LegRep RRx4 -44.4 (-39.9); margin at 308-310 +0.1, -5.3 (+5.6, -0.5) | `mix.json` Bass clarinet `region_gain_db`: restrict the A-flat 2 entry to `"rows": ["Sus Non Vib", "Leg Slur"]` (the LegRep RRx4 note was in line before the gain: -39.9 after B2 -39.6) | 308-310 back to -39.9; margin +4.6, -0.8 |
| 5 | Oboe 1, bar 79 (qn 312.5-316), mf motif | -47.8 (-41.7; c56 -43.7); margin -9.6, -9.2, -12.2 (-4.2, -2.6, -7.3); Horns a2 -39 to -44 over it | `mix.json` Oboe 1 `soft_trim_db`: `"mf": 3.1 -> 7.0`, add `"mp": 8.5`, `"p": 5 -> 9.5` (cause b). It is a dynamic trim, so it follows the printed dynamic only | motif -43.9; margin -5.7, -5.3, -8.3; Oboe 1 mf median -49.8, p -50.9 |
| 6 | Flute 1 solo, bars 73-75 (qn 291-300), p espr. | A-flat 5 crest at 294 -28.3 (-33.3), 9 dB over the G-flat 5 that follows; margin +16.6 (+10.8); master bar 74 +4.4 | `mix.json` Flute 1 `region_gain_db` A-flat 5 (80): +5 only on `Sus MAX`; on `Leg Slur MAX` +2. Hairpin 292-295 arrival CC11 71 -> 66 | crest about -32.5; bar 74 within 1 dB of c57 |
| 7 | Clarinet 1 theme over the pedal, bars 127-129 (qn 504.5-516) | margin per two beats from 504: -1.6, +0.1, +6.2, +1.9, +0.8 (+1.9, +5.7, +10.2, +5.2, +4.1). Double basses' pedal G1 -41.3 / -39.3 at 506-516 (-47.0 / -44.7; c56 -47.4 over 504-516): envelope +1 to +3 where c57 had -4.6 to -9.8. Clarinet entry 504.5-507 3 to 6 dB lower | `roles.json` Double basses `[500.5, 516, -5, 2]` (three re-bow pieces, 7 s; replaces the dropped `[508, 516, -2]`). Clarinet 1: a flat CC11 offset of +8 units over 504.4-508 (46-62 -> 54-70; slope 0.14-0.25, about +1.7 dB), starting in the rest at 504.2 | margin +3.5 to +9; basses within 1 dB of c57 |
| 8 | Oboe 1 p dolce, bars 145-146 (qn 578-582) | G4 -51.1 (-43.6), E5 -44.2 (-39.3); margin 578-580 -9.8, -4.5 (-1.6, +2.9). Clarinet 1's pp F4 beside it -48.0 (-53.0): its row `[575.75, 582, -5]` was dropped | The Oboe 1 trim of row 5 (+4.5 at p). Clarinet 1 F4 576-582: CC11 25->22 -> 17->14 (finding 4) | Oboe -46.6 / -39.7; clarinet -53; margin about -1, +3.5 |
| 9 | Violins I, Oboe 1, Flute 1 over the low brass, bar 124 (qn 492-496.5) | group margin -7.4 (-5.8). Flute 1 G5 -48.7 (-44.8), F5 -59.9 (-52.0); Trombone 1 -41.3 (-46.5), Bass trombone -39.3 (-43.3) | finding 4 rows (Trombone 1, Bass trombone, Tuba 492.5-496.5; Flute 1 492-496.5) | margin about -5 |
| 10 | Horn 1 mp espr., bars 125-126 (qn 497-501) | margin -4.9, -5.3, -6.8 (-3.0, -4.6, -5.0); Tuba's pp G1 at 500-504 -49.5 (-57.2) | finding 4 rows (Horn 1 `[496.5, 501, 2]`, Tuba `[499.9, 504.5, -4]`) | margin back to c57 |
| 11 | Cor anglais and Violins II fugato entry, bars 91-93 (qn 360-372) | margin median -8.7 (-6.7), lower quartile -15.0 (-11.8) | no role change proposed: the row `[360.25, 372, 4]` is in place; the loss is in the Cor anglais stac alias (shapes of -5 / -6 / +3 dropped). Left for a range render | - |
| 12 | Violins I pp espr., bars 177-180 (qn 707-720) | E-flat 5 re-attack at 711.86 on Sus MAX -43.2 (-47.9; c56 bar 179-180 -48.7): 6.8 dB over the same pitch on Leg Slur MAX before it (-50.0); bars 179-180 master +4.2 / +2.9 | Row choice: play the 711.86 re-attack on `Leg Slur MAX` as its neighbours (`SUS_ENTRY_AT` exception or the tie rule in `score_config.py`). If it must stay on Sus MAX: phrase CC11 712-720 at 30 instead of 35-39 (Violins I 0.55 dB per unit at 34-46, 0.34 below) | 712-716 about -46.5; bar 179 within 1.5 dB of c57 |
| 13 | Violins I recap theme, bars 135-139 (qn 536-556) | +5 to +7.5 dB over c57; margin -8.9 (-12.9); with Flute 1 and Oboe 1 -5.8 (-6.3); first statement bars 23-25 -3.9 | none: the +3.7 dB is in the right direction; the theme is still 2 dB lower against its accompaniment than in bars 23-25 | - |
| 14 | Second theme, Horn 1 and celli, bars 47-55 and 147-153 | both down 2.5 to 5.4 dB; Horn 1 minus celli +0.8 (c56 -1.3); master 1.4 to 3.6 dB under c56 | optional: celli flat CC11 offset of +6 units over 184-220 and 584-606 (77-91 -> 83-97; 0.33-0.41 dB per unit) | celli +2.2 dB, bars within 1.5 dB of c56 |

Passages checked and found within 2 dB of c57 at the median and the lower quartile (no fix): Horn 1 bars 13-14, theme
bars 23-25 and 27-32, bars 35-40, bars 56-61 (violins, Clarinet 1 and Horn 2), bars 69-71, Flute 1 bars 109-110, Violins
I bars 111-114, bars 131-134, bars 158-161, bars 167-170, the trombone chorale 175-178. Horn 1 bars 44 and 48: within
1.4 dB of c56 (bar 44 -43.8 against -44.0, bar 48 -34.2 against -35.6); the c57 levels there were the outliers.

## Finding 2. Horn 4's F3 at p, and the nine bars where Horn 4 is now the loudest accompaniment

Where: Horn 4 qn 72-88 (bars 19-22) and every F3 at p: 224, 440, 620; master bars 11, 19, 57, 61-62, 104-105, 111,
156-157, 164 (Horn 4 +5.4 to +8.7 dB over c57, margin -6 to -12).

Evidence (measured): instrument output at CC11 46: F3 -53.4 dB in c57 and in c58 (5 notes, to 0.1 dB), G3 -64.3, G-flat
3 -63.4, A-flat 3 -65 to -67, B-flat 3 -66.6, D3 -56.6. The c58 region gain (`"dyn": ["pp"]`, -9 dB on C3-F3) changed
nothing, so the pp group is not what sounds on F3 at CC11 46. G3 gains 9.6 dB between CC11 46 and 55 (-64.3 -> -54.7),
F3 2.8 dB (-53.4 -> -50.6). At CC11 74 / 69 F3 and G3 read -46.1 / -49.5, at 91 / 98 -42.3 / -40.9. So from G-flat 3 up
the patch has a soft layer about 10 dB weaker than the layer above it, and F3 and below do not use it at this CC11. The p
trim (+14.4 dB) is sized for the weak layer and lifts F3 to -40.3 against G3 -51.2 (bars 19-22), and to -40.7 at 440
where Horn 1's A-flat 4 is -54.9 and the Violins I melody -42.

Fix (dynamic mapping, instrument side): play Horn 4's p above the weak layer.
- `build/score_config.py` `CC11_REMAP["Horn 4"] = [(22, 44), (34, 50), (46, 56), (58, 62), (72, 72), (88, 88), (114, 100),
  (124, 124), (127, 127)]` (the brass map from 88 up is unchanged).
- `build/mix.json` Horn 4 `soft_trim_db`: `"p": 14.4 -> 5.0`, `"pp": 14.1 -> 8.0`, `"ppp": 14.1 -> 10.0`, `"mp": 9.0 ->
  5.0`; delete the `"dyn": ["pp"]` region-gain entry (inert) and add `{"rows": ["Sus MAX"], "pitch_db": {"53": -2}}`.
- Expected at p (from the measured points at CC11 54-59): G3 -54.5 + trim = about -51 (as now), F3 -50.3 - 2 + trim =
  about -48.5 (now -40.3): F3 over G3 2.5 dB instead of 11; at f F3 2 dB under G3. A-flat 3 stays 4-5 dB under G3 at mp
  (-59.1 against -54.7, 4 notes each): candidate for a region gain after the render.
- Inferred, not measured: the timbre of Horn 4's p moves toward the mp layer. Range render bars 19-22 and 111 first.
  If the remap is rejected, the fault stays and Horn 4's bars above must be listed as audible.

## Finding 3. Cello solo, bars 171-174: 12 dB between its loudest and softest held notes at one CC11

Where: Cello solo track (DIV A), qn 680-696. CC11 runs 64 -> 81 over the first note and then stays at 75-80 to 693.

Evidence (measured, per half beat): E-flat 4 at 680.5-683.5 -28.3 to -31.5 (c57 -33.6 to -36.2); D4 and C4 at 683.5-685
-33.1 to -36.4; A-flat 4 at 685.5-687 on Leg Port MAX -25.5 to -27.0 (c57 -35.6; master +8.2 and +7.6 on those beats);
G4, F4, E-flat 4, D-flat 4 at 687-691 -34.8 to -39.0; C5 at 692-693 on Leg BC MAX -40.3 to -41.3 (c57 -32.1 to -33.9),
which is the printed crest of the phrase (crescendo 691-692, diminuendo 692-694); B4 at 694 -45.5. Margin over the
accompaniment: +16 to +19 in bar 171, +16 at 685-686, +0.9 to +3.3 at 690-693 (Cor anglais -42.8 to -44.3 beside it).

Fix (rows and region volumes first, then one CC11 lane; slopes are the section celli's 0.41-0.45 dB per unit at 58-88,
the DIV A patch has only 12 notes to fit, so the lane values are inferred and need the range render 679-696):
- `mix.json` Cello solo `region_gain_db`: `{"rows": ["Leg Port MAX"], "all_db": -8}`; `{"rows": null, "pitch_db":
  {"72": 5, "71": 3}}` (C5, B4); `{"rows": ["Leg Slur MAX"], "pitch_db": {"63": -4}}` (E-flat 4).
- One CC11 lane for the phrase in place of the flat 75-80 (`score_config.py`: `HP_TARGET_AT["Vc"]` holds the solo's hairpin ends at 680, 685, 691, 692 as dynamics; the
  values below are the CC11 the lane should reach, so either give the targets as CC11 or add a flat offset per span): 680: 62, 683.5: 78, 684: 76, 685-687: 76, 687-691: 82, 692: 88, 692.5: 88, 693: 80, 694: 64, 695.5: 50.
- Expected: 680.5-683.5 about -34; A-flat 4 -34; 687-691 -33 to -37; C5 -32.5; B4 -42.5. Bars 171-172 within 1.5 dB of
  c57, bar 174 within 1 dB; margin at the crest about +9.

## Finding 4. The dropped role rows as CC11 values, and the slopes `LEVEL_TO_CC` uses

What: 62 role rows on one or two notes were dropped because they last under 4 s. Most are accompaniment cuts under a
melody or lifts of a short solo. A flat CC11 offset from the note's own onset to its end (as the 17 long rows already
get) is not a shape inside a note.

Fix: `build/score_config.py` `LEVEL_TO_CC["min_s"] = 0.5` for rows whose notes start after a rest or at a printed
dynamic, and replace `db_per_cc` by the per-track curve in `cycles/c59/critic_scripts/B/cccurve.json` (keys `K` knots
and `sl` slopes; `inv()` in `hp.py` inverts it). With the family values the winds' rows at CC11 88-104 give a third of
their dB and the horns' rows at 46-58 overshoot by half.

Rows that bear on a melody (measured stem change c57 -> c58 on the covered note; CC11 now -> CC11 that gives the row's dB
on the track's own curve):

| row (dropped) | note, stem c57 -> c58 | CC11 now -> new |
|---|---|---|
| Trombone 1 `[492.5, 496.5, -3.5]` | G3 -46.5 -> -41.3 | 88->62 -> 82->46 |
| Bass trombone `[492.5, 496.5, -3.5]` | G2 -43.3 -> -39.3 | 88->62 -> 80->50 |
| Tuba `[499.9, 504.5, -4]` (bar 126 pp under Horn 1) | G1 -57.2 -> -49.5 | 34->25 -> 18->12 (curve thin below 34; range render) |
| Bassoon 2 `[496, 500, -3]` | G2 -46.4 -> -42.7 | 78 -> 62 at the start of its diminuendo |
| Clarinet 1 `[575.75, 582, -5]` (under the oboe, bar 145) | F4 -53.0 -> -48.0 | 25->22 -> 17->14 |
| Clarinet 1 / Clarinet 2 `[136.75, 144, -3]` (under the violins, bars 35-36) | +3.0 / +3.0 dB | 46 -> 36 / 46 -> 42 |
| Flute 1 `[492, 496.5, 2.5]` | G5 -44.8 -> -48.7, F5 -52.0 -> -59.9 | 54->37 -> 56->39, 38->43 -> 40->45 (the rest of the loss is a dropped shape; not recovered) |
| Horn 1 `[496.5, 501, 2]` (mp espr.) | E-flat 3 and C4 -2.0 dB | 58->69 -> 64->74, 69->63 -> 74->68 |
| Horn 3 `[165.5, 168, -3.5]` (under Horns a2, bar 42) | B-flat 3 -43.1 -> -39.1 | 100->60 -> 84->54 |
| Trombone 2 `[551.95, 555.1, -4]` | C4 +1.4, B-flat 3 -2.2 dB | 83-86 -> 76-79 |
| Bass clarinet `[384, 388, -3]` (ff whole note level with the celli) | B2 -35.4 -> -32.3 | 104 -> 78 |
| Trumpet 3 `[456, 464, -3]` | D-flat 4 +3.3, D4 +4.4 dB | 87-100 -> 80-81 |
| Violins II `[320.5, 324.25, -3]`, Violas the same | 0.0 dB (unchanged in the render) | no change needed |

Not convertible: Trumpet 1 `[484, 488.5, +2]` (CC11 117-124, no room; A-flat 4 reads -35.5 against -29.6 in c57, the
largest single loss at the fff of bar 122; it needs the `dyn_trim_db` fff anchor of Trumpet 1 +2, a section dynamic).

## Finding 5. Does the theme at +5.9 dB lower quartile hide the celli in bars 15-22? Mostly not; three bars are too wide

Measured (power over each of the 32 quarters, Violins I minus Violoncellos; this measure reads about 2.5 dB under the
actor's): median +6.9, lower quartile +3.1, 7 quarters over +12 (c57 +2.2 / -0.5 / 3). Per bar: 15 +14.3, 16 +7.8, 17
+2.3, 18 +4.7, 19 +7.2, 20 +12.8, 21 +12.1, 22 +0.3. In their own octave band (125-250 Hz) the celli are still the
largest stem: celli minus all other stems +1.7 dB at the median (c57 +4.6), lower quartile -3.6 (+0.9). In 250-500 Hz
they are -9.5 (c57 -6.6). The theme no longer dips under the rest (margin lower quartile -0.4 against -5.4).

So the celli are audible as the bass of the texture, but not in three places: bar 15, where the first note C3 on Sus MAX
reads -57 / -52 dB in its first two quarters against the theme at -33 (the Leg BC MAX notes after it read -44 to -46 at
the same CC11; Leg BC MAX is 5.5 dB over Sus MAX on this track, 10 pitches), and bars 20-21, where the theme's sf and
crescendo reach -27 to -29 against celli at -43 to -44.

Fix: `build/roles.json` Violoncellos `[56, 88, -3.5]` -> `[56, 88, -2.0]` (the c53 value). Expected on the actor's
measure: lower quartile 5.9 -> about 4.4 (target 3.9), median 9.3 -> 7.8. For bar 15: `mix.json` Violoncellos
`region_gain_db` `{"rows": ["Leg BC MAX"], "all_db": -2.5}` with the role at -1.0 instead of -2.0 would close half of the
row step for every phrase entry; this changes all Leg BC passages, so range render bars 15-22 and 27-32 first.

## Finding 6. Which hairpin gains can move into CC11, and what the strings' points per second would be

Measured on variant builds (`v_base`, `v_nohp` = `STP_DROP_TAGS=hp:hpgain`, `v_norole`, `v_none`) with the shipped
`ENV_THIN`:

| track | now | no hairpin gain at all | no roles | only dynamic trims, chord cuts and the fade | hairpin-gain items: arrival below ff / soft / arrival at ff or fff |
|---|---|---|---|---|---|
| Violins I | 0.50 | 0.46 | 0.43 | 0.36 | 7 / 3 / 14 |
| Violins II | 0.61 | 0.52 | 0.55 | 0.38 | 7 / 7 / 15 |
| Violas | 0.64 | 0.61 | 0.57 | 0.40 | 15 / 5 / 8 |
| Violoncellos | 0.73 | 0.66 | 0.64 | 0.54 | 21 / 13 / 11 |
| Double basses | 0.49 | 0.38 | 0.47 | 0.35 | 7 / 10 / 10 |

- Hairpin gain is not the main source. Taking all of it out leaves the strings at 0.38-0.66 points per second. The floor
  is the dynamic trim lane itself (0.35-0.54): the trims differ by 8.5 dB between p and ff on the celli, so every printed
  dynamic and hairpin writes points.
- Movable: hairpins that arrive below ff (57 items on the five string tracks) and the soft ones (38). Raise the
  hairpin's CC11 arrival by the gain divided by the track's slope there: +3 dB is +10 to +12 units at an arrival of
  82-96 (strings 0.27-0.33 dB per unit), +2 dB is +5 to +7; the soft ±2.5 dB is 5 to 9 units. Each item with its new
  arrival value: `hp_items.json` (the same for 10 wind and brass tracks). Key: `HP_GAIN_DB` / `HP_GAIN_MF_DB` /
  `HP_GAIN_SOFT_ACC_DB` to 0 for these arrivals, with the dB as an added CC11 arrival (a new option in
  `score_to_parts.py` beside `HELD_DECRESC_CC`, reading `cccurve.json`; `HP_TARGET_AT` can do single cases).
- Not movable: 58 items that arrive at ff or fff (CC11 104 and up gives 0.13-0.17 dB per unit on the violins; +3 dB
  would need 124, the fff anchor). They are section dynamics as ramps and may stay.
- Expected with the movable and soft items in CC11 (by item share of the measured saving): Violins I 0.48, Violins II
  0.57, Violas 0.62, celli 0.67, basses 0.42. That does not reach 0.4.
- What does reach it (measured, `thin.py`): `tools/build_reaper.py` `ENV_THIN["tol_db"]` 0.5 -> 0.75 gives 0.42 / 0.52 /
  0.55 / 0.61 / 0.41 with the largest deviation from the shipped envelope 0.7 dB; with all hairpin gain out as well 0.37
  / 0.46 / 0.50 / 0.54 / 0.33; `tol_db` 1.0 with hairpin gain out 0.32 / 0.41 / 0.44 / 0.48 / 0.29 (deviation 1.0 dB).
  The celli need a narrower trim spread to go under 0.5.

Do not touch: the Violins I role `[128, 160, 3]` and the recap theme's new level (bars 135-139); the Violins II theme
doubling on Sus Marc LITE with its -4 dB row gain (bar 21 now -37.5, between c56 and c57); the theme's margin over the
rest in bars 15-22 (lower quartile -0.4, was -5.4); Horn 1 bars 44, 48 and 111 without their old lifts (the line in bars
111-114 now rises as printed); the brass against each other at f (horns 3-5 dB under trumpets and trombones); zero
per-note items and zero fitted rows on the envelope.
