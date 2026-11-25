# Critic A, cycle 51: articulation and phrasing (on the c50 render)

Data used: `cycles/c50/rendered_build/` (its `parts.json` is byte-identical to the live `build/parts.json` today) and `cycles/c50/render/` stems. Printed lengths, slurs and breaths from `build/mockup-events.tsv`; printed tempo from `symphony/mvt2/v600/global.ily`. No REAPER, no audio setting changed. Scratch folder left in place: `/private/tmp/claude-501/mockup-loop/mvt2-c51-A/` (2 MB; scripts `onsets.py`, `validate2.py`, `final.py`, `fix2.py`, `predict.py`, `tempo.py`, `tempo2.py`; results `final_S.txt`, `predict_S.txt`, `validate2.txt`, `tempo.txt`).

This cycle's priority from the loop lead was timing of the thematic lines and the tempo map, so the rest of the lens is short.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 51. I read the pages that bear on the lead question.

| Manual (May 2021, PDF page) | Where it applies | Does the render follow it |
|---|---|---|
| p.143-144: "Monophonic True Legato" plays a sampled transition for each interval; note velocity sets the transition time (50-60 longer, 110-127 shorter) and does not change loudness | every Leg Slur / Leg BC row | Strings are at velocity 124 (shortest). Winds are at 86-104 (`LEG_VEL_BY_CC`), so their transitions are not at the shortest setting. Measured latency agrees with "one sample per interval": the same pitch pair repeats its latency within 3 ms (winds), different pairs differ by up to 60 ms |
| p.143: CC5 "Time" acts on the scripted Legato and Portamento emulations, not on true-legato samples | string and wind KS Masters | Not used; it cannot shorten the Leg Slur MAX transition. No change proposed |
| `MANUAL-GAPS.md` item 6 (velocity 60-75 for slower cantabile transitions) | Vc bars 23-28, Vln I/II bars 53-56 | Do not apply it while finding 3 is open: the violin transitions already take 180-240 ms at velocity 124 |

## Method, and where each method loses the pitch (measured)

I measured three estimators on every note of 26 lines (411 notes) and tested them on synthetic lines built from the real pitches, lengths and data leads, with every note switched exactly on the beat (`validate2.py`).

| Estimator | Instant switch, dry | Instant switch, hall (RT60 1.5 s, tail energy = direct), level steps of up to 6 dB | 120 ms crossfade, hall, level steps |
|---|---|---|---|
| Dominant pitch, harmonics 1-3 (`theme50.py`, Movement I `theme_onsets.py`) | median +2, robust SD 5; 22 of 411 not found | median +18, robust SD 29, **113 of 411 over 60 ms**, up to +183 | median +29, 116 over 60 |
| Crossover of the two pitch bands (`pcx.pair_window`, and my version that handles A-B-A figures) | robust SD 2 | median +16, **89 of 356 over 60**, up to +159 | median +33, 93 over 60 |
| pcX (`pcx.attack_pcx`, rise of the new pitch) | robust SD 3 | median +3, robust SD 6, 11 over 60 | median +20, robust SD 13 |
| **S = the earlier of pcX and crossover** (used below) | robust SD 3, none over 25 | median +2, robust SD 4, 19 of 356 over 25, 2 over 60 | median +15, robust SD 15, 5th-95th percentile -14..+46 |

Where the methods fail:
- The dominant-pitch method and the crossover read late whenever the previous note's ring is louder than the start of the new note (a softer target, a diminuendo, a wet hall). Their errors are late only. A good part of the "+106" and "+126" readings in `theme_c50.txt` is this.
- The dominant-pitch method gives a false early reading on a leap after a rest: on the synthetic line it reads Violins I qn 249 at -145 ms although the note is on the beat. The actor's "-139 ms" in bars 74-75 is that artefact. It also does not find a line's first note or same-pitch repeats (22 of 411 on the dry test).
- `pair_window`'s crossover reads -250 to -350 ms on A-B-A figures (the new pitch still rings from two notes back): Violins II 181.333, the bar 78 run.
- pcX reads late on real audio when the target swells slowly (t50 minus the -10 dB point: median 56 ms on strings). The c47-c50 leads were fitted on pcX, so they pushed slow-swelling targets early.
- S has only small late errors (about 15 ms robust SD on a slow transition). Readings beyond +-40 ms are real. For entries and repeated notes S is pcX alone, which reads +15 to +21 ms late on the synthetic 30 ms attack; entries on soft string swells are less certain than joins.

Renders repeat exactly: of 410 line notes with unchanged data, c48 to c49 moved by median 0.0 ms (robust SD 0.0), 15 notes by more than 25 ms. The scatter below is in the data and the samples, not render noise.

## Per line: audible start against the beat (S, ms; c50 render; measured)

"Constant row lead" is the estimate with one lead per patch row equal to that row's median latency (note-on to audible start), all per-onset rows and extras removed. "After fixes" is the estimate for findings 2 and 3 (0.9 of a lead change arrives; measured slope 0.82-0.93).

| Line | Notes | Min | Max | Median | Outside 25 | Outside 60 | Slur pairs | Pair diff median | Pairs over 25 | Pairs over 60 | Constant row lead: outside 25 / 60 | After fixes 2-3 (predicted): outside 25 / 60 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Horn 3, intro C-Db-C, bars 3-6 | 3 | -47 | +10 | +5 | 1 | 0 | 2 | 31 | 1 | 0 | 2 / 0 | 0 / 0 |
| Horn 1, theme A, bars 6-14 | 24 | -86 | +64 | -26 | 14 | 6 | 22 | 28 | 14 | 5 | 10 / 2 | 4 / 1 |
| Oboe 1, answer, bars 15-22 | 11 | -59 | +48 | -14 | 6 | 0 | 9 | 40 | 6 | 2 | 4 / 1 | 0 / 0 |
| Violin I solo, bars 17-22 | 11 | -28 | +165 | +9 | 4 | 2 | 9 | 30 | 5 | 2 | 3 / 2 | 4 / 2 |
| Violins I, theme A, bars 22-30 | 24 | -59 | +102 | +2 | 10 | 3 | 15 | 31 | 9 | 5 | 19 / 7 | 7 / 1 |
| Violins II, theme A, bars 22-30 | 24 | -76 | +92 | -3 | 11 | 5 | 15 | 60 | 11 | 7 | 15 / 7 | 3 / 0 |
| Violoncellos, counter-melody, bars 22-30 | 19 | -73 | +122 | -18 | 10 | 5 | 9 | 40 | 6 | 0 | 14 / 5 | 8 / 2 |
| Bass clarinet, solo, bars 31-36 | 12 | -45 | +35 | -9 | 3 | 0 | 10 | 16 | 2 | 0 | 2 / 0 | 1 / 0 |
| Flute 1, theme B, bars 36-40 | 19 | -57 | +62 | +10 | 3 | 1 | 17 | 14 | 8 | 1 | 3 / 0 | 2 / 0 |
| Cor anglais, theme B, bars 41-44 | 14 | -110 | +24 | -15 | 3 | 1 | 13 | 18 | 3 | 2 | 2 / 0 | 0 / 0 |
| Flute 1, theme B answer, bars 41-44 | 12 | -114 | +32 | -51 | 10 | 2 | 11 | 16 | 4 | 3 | 2 / 0 | 2 / 0 |
| Oboe 1, B flat minor head, bars 45-47 | 10 | -62 | +50 | +11 | 6 | 1 | 7 | 40 | 6 | 2 | 8 / 0 | 4 / 0 |
| Violoncellos, B flat minor head, bars 45-47 | 9 | -66 | +14 | -6 | 4 | 1 | 5 | 43 | 3 | 2 | 4 / 1 | 3 / 0 |
| Cor anglais, quotation, bars 47-52 | 13 | -36 | +42 | -12 | 3 | 0 | 10 | 25 | 5 | 1 | 2 / 0 | 1 / 0 |
| Violins I, theme B, bars 53-60 | 30 | -80 | +74 | -8 | 18 | 5 | 21 | 30 | 11 | 6 | 21 / 5 | 6 / 1 |
| Violins II, theme B, bars 53-60 | 30 | -125 | +102 | 0 | 20 | 9 | 21 | 51 | 16 | 9 | 20 / 11 | 10 / 2 |
| Horn 1, counter-melody, bars 53-60 | 19 | -164 | +32 | -24 | 10 | 3 | 15 | 48 | 9 | 5 | 11 / 5 | 3 / 0 |
| Violoncellos, bars 53-60 | 19 | -98 | +70 | -17 | 9 | 4 | 3 | 82 | 3 | 3 | 10 / 5 | 3 / 0 |
| Violins I, climax, bars 61-64 | 6 | +11 | +229 | +29 | 3 | 2 | 0 | - | 0 | 0 | 5 / 3 | 3 / 2 |
| Trombone 1, quotation, bars 63-64 | 10 | -73 | +106 | +12 | 8 | 3 | 5 | 65 | 4 | 3 | 7 / 2 | see finding 5 |
| Horn 1, motto tail, bars 65-70 | 5 | -47 | -13 | -36 | 4 | 0 | 4 | 14 | 0 | 0 | 3 / 0 | 1 / 0 |
| Violins I, theme A', bars 70-78 | 28 | -106 | +112 | -18 | 18 | 9 | 18 | 58 | 17 | 9 | 20 / 11 | 7 / 3 |
| Violins II, theme A', bars 70-78 | 28 | -133 | +38 | -25 | 19 | 8 | 18 | 55 | 13 | 7 | 22 / 10 | 13 / 3 |
| Violoncellos, counter-melody, bars 71-78 | 18 | -101 | +80 | -31 | 12 | 5 | 8 | 37 | 5 | 2 | 8 / 4 | 7 / 1 |
| Violins I, cadence, bars 79-82 | 9 | -87 | +41 | +2 | 3 | 1 | 4 | 14 | 1 | 0 | 4 / 2 | 2 / 1 |
| Clarinet 1, motto tail, bars 85-88 | 4 | +11 | +34 | +22 | 2 | 0 | 2 | 18 | 0 | 0 | 2 / 0 | 1 / 0 |
| All 26 lines | 411 | | | | 214 | 76 | 264 | | 162 | 76 | 223 / 83 | 101 / 21 |

The lead's four ranges: Flute 1 bars 36-40: -57..+62, 3 of 19 outside 25 (the actor's 10 of 19 is mostly method error). Violins I bars 54-61: -80..+74, 16 of 28 outside 25, 4 outside 60. Violins I bars 74-75: -67..+112, 4 of 6 outside 25. Violoncellos bars 22-27: -62..+122, 7 of 13 outside 25. The harp, timpani and pizzicato lines have no legato lead and were not measured.

## Findings

### 1. The tempo map has 233 a-tempo beats and 103 of them are 3 % or more away from the printed tempo; 13 phrase-end beats are 20-42 % long and the next beat snaps back (measured; audibility inferred)

Where: the whole movement. The mockup lasts 353.30 s against 345.33 s at the printed tempos (+8.0 s). Printed changes (kept, do not remove): poco rit. bars 35-36, Poco più mosso 60 at bar 37, poco rit. bar 47, poco sostenuto 54 at bar 48, a tempo and animando bars 53-59 (60 to 64), poco allargando bar 60, Largamente 54 at bar 61, allargando bar 64, Tempo I at bar 65, poco allargando bars 78-82, a tempo bar 83, rit. bars 89-92, the fermata. The build ramps these in quarter-beat steps (`RAMP_SPANS`), which is fine.

Everything else is not printed. All of it comes from `build/score_config.py`:

- `CAESURA`, 24 entries, +3.50 s in total. Time is added in the last quarter of the beat before the listed qn.

| qn | Bar, beat | Added | That beat lasts (printed) | Printed breath at qn | What moves through it |
|---|---|---|---|---|---|
| 29 | 10, 2 | 220 ms | 1.594 s (1.154), +38 % | Hn 1, B.Cl. | held notes |
| 42 | 14, 3 | 180 | 1.622 (1.154), +41 % | none | held |
| 48 | 16, 3 | 150 | 1.304, +13 % | none | held |
| 54 | 18, 3 | 100 | 1.382, +20 % | none | held |
| 60 | 20, 3 | 100 | 1.254, +9 % | none | held |
| 65 | 22, 2 | 200 | 1.642, +42 % | none | held |
| 77 | 26, 2 | 150 | 1.524, +32 % | none | held |
| 90 | 30, 3 | 150 | 1.592, +38 % | none | held |
| 96 | 32, 3 | 150 | 1.281, +11 % | none | held |
| 102 | 34, 3 | 150 | 1.304, +13 % | B.Cl., Bn 1 | held |
| 116 | 38, 4 | 100 | 1.211 (1.000), +21 % | none | viola triplet eighths 370, 370, **470** ms |
| 124 | 40, 4 | 220 | 1.410 (1.000), +41 % | Fl 1 | held |
| 139 | 44, 3 | 150 | 1.340 (1.000), +34 % | none | held |
| 148 | 46, 4 | 100 | 1.245 (1.000), +25 % | none | held; 7 tracks enter after it |
| 164 | 50, 4 | 200 | 1.279 (1.111), +15 % | C.A. | viola eighths 539, **739** ms |
| 171 | 52, 3 | 100 | 1.211 (1.111), +9 % | none | basses |
| 188 | 56, 4 | 120 | 1.097 (0.984), +11 % | Hn 1, Cl 1 | harp triplets 326, 326, **445** ms |
| 196 | 58, 4 | 80 | 1.030 (0.968), +6 % | Fl 1, Ob 1, Hn 1, B.Cl. | the eighth pickup in six tracks, 476 then **554** ms |
| 204 | 60, 4 | 100 | 1.153 (1.034), +11 % | all winds and brass | viola sextuplets 173, 174, 175, 176, **210, 244** ms, ff, into the climax |
| 237 | 70, 2 | 180 | 1.622 (1.154), +41 % | none | held |
| 249 | 74, 2 | 150 | 1.524 (1.154), +32 % | none | viola and cello eighths 687, **837** ms |
| 259 | 77, 3 | 100 | 1.226 (1.154), +6 % | Bn 1 | eighths in Fl 1, Cl 1, Vln I, Vln II, Vla: 563, **663** ms |
| 268 | 80, 3 | 150 | 1.430 (1.250), +14 % | all winds | held |
| 286 | 86, 3 | 200 | 1.574 (1.154), +36 % | Cl 1 | held |

- `PHRASE_ARCS`, 16 arcs, +3.21 s: (18,29), (29,42), (48,54), (60,65), (65,77), (77,90), (108,116), (116,124), (124,139), (139,148), (152,160), (160,168), (220,226), (226,237), (237,249), (274,286). Each slows its last two beats (x0.96 and x0.92; "sub" x0.98 and x0.95; "main" x0.95 and x0.88), pushes its first half x1.015 and takes the next arc's first beat at x0.97. With the caesura on top, the last beat of bars 10, 14, 22, 26, 30, 40, 44, 70, 74 and 86 is 32-42 % long, bars 18, 38 and 46 are 20-25 % long, and the following beat is 15-30 % shorter than the one before it.
- `APEX_AGOGIC` (0.93 in this build): one beat 7.5 % long in mid-phrase at qn 20, 34, 49, 61, 68, 82, 110, 117, 129, 142, 157, 162, 229, 240.
- `BEAT_STRETCH`, 57 single beats at x0.94 to x1.04, including the Largamente downbeats 204 and 208 (x0.94, +6.4 %).
- `TEMPO_PUSH`, 5 spans at x1.015 to x1.025 (22-24, 79-84, 94-99, 141-147, 251-259).
- Together: 104 beat-to-beat changes of 6 % or more that the score does not print (`tempo.txt`, lines marked STEP). 42 a-tempo beats are 6 % or more off the printed tempo, 24 are 10 % or more off.

What a listener hears as out of time (inferred from the sizes; a single beat changed by about 6 % or more is above the usual detection threshold at this tempo):
1. Certain: the 13 phrase ends of 20-42 % followed by a snap back. The pulse stops every four bars and restarts. In bars 1-36 this happens in bars 10, 14, 18, 22, 26 and 30.
2. Certain: the eight caesuras with notes moving through them (qn 116, 164, 188, 196, 204, 249, 259, and 171 in the basses). The last subdivision is 17-39 % longer than its neighbours. Bar 60 is the worst: the viola sextuplets stumble into the Largamente.
3. Likely: the 14 apex beats and the arcs' second-last beats (7-13 % on one beat), and the Largamente downbeats.
4. Not by itself: a single x0.96 or x1.04 beat or a 2 % push. They do add to the 6 % steps where they sit next to an opposite change (for example qn 17-21: +4 %, -3 %, +3 %, +7.5 %, -7 %).

Fix (`build/score_config.py`, appended at the end; the keys of `CAESURA` stay because the breath-gap code and `CAESURA_LIFT` test membership, and `add_caesuras` with 0.0 leaves the tempo unchanged):

```
PHRASE_ARCS = []
TEMPO_PUSH = []
BEAT_STRETCH = {}
CAESURA = {k_: 0.0 for k_ in CAESURA}
```

With no arcs the apex loop does nothing. Breaths then take their time from the note before them (`CAESURA_BREATH_S` 0.34 s, unchanged), which is what a breath mark means. `CAESURA_LIFT` stays. Acceptance: every beat outside `RAMP_SPANS` within 0.5 % of 60 / printed bpm; inside the ramps no quarter-beat step more than 3 % off the straight line between the printed steps; total length 345.3 s +-0.3; the viola sextuplets of bar 60 within 5 % of each other except for the printed allargando. After the rebuild check the re-bow points and fitted fills (seconds-based) with `fit_rebows.py` as after any map change. If the lead wants a smaller step first: zero only the 14 caesuras with no printed breath and the eight with moving notes, and set `PHRASE_SLOW`, `PHRASE_SLOW_SUB`, `PHRASE_SLOW_MAIN` to (1.0, 1.0); that removes groups 1 and 2.

### 2. Winds and brass: the per-onset rows and stacked extras put thematic notes 50-180 ms early; one lead per row plus a pitch-pair table is better (measured)

Where: every wind and brass legato line, 263 joins on 14 tracks.

Evidence:
- Latency (note-on to audible start) per row: Flute 1 median 42 ms (robust SD 12), Cor anglais 59 (15), Clarinet 1 69 (7), Clarinet 2 66 (15), Bassoon 2 73 (8), Bassoon 1 69 (19), Oboe 1 78 (42), Bass clarinet 88 (33), Horn 1 94 (33), Trombone 1 74 (16).
- The same pitch pair on the same row repeats its latency within 3 ms robust SD (13 ms SD; 33 joins in pairs that occur three times or more). Pairs differ from the row median by -26 to +34 ms (5th-95th percentile). This is the patch's own transition time varying by sampled interval. It does not depend on velocity, CC11, CC1 or the previous note's length (|r| under 0.15 on the winds).
- The 43 per-onset rows on these tracks: 35 % within 25 ms of the beat and 67 % within 60. The 220 joins without a row: 69 % and 96 %. The rows make it worse. They were fitted on pcX, which reads slow-swelling targets late.
- All 202 wind joins: 33 % outside 25 and 6 % outside 60 now; 21 % and 3 % with a constant row lead. Brass (58 joins): 52 % and 17 % now. With a pair table tested leave-one-out on the pairs that recur: winds 23 % and 0 % (87 joins), brass 8 % and 0 % (24 joins).
- Stacking: Horn 1 qn 202 has the row lead 100 ms + `LEG_EXTRA_S` (leaving F4) 150 + per-onset row 100 = 350 ms against a latency of 186: it sounds **164 ms early**. Flute 1 200: row +0.20, lead 230 against latency 48: **-182 ms**. Cor anglais 131.5: lead 160 against 50: -110. Clarinet 1 258 and 259: lead 170 against 66 and 88: -104 and -82. Horn 1 18, 26, 27, 39 (the theme's opening): -85, -86, -58, -70. Flute 1 135: -64. Oboe 1 145.5 and 197.5: -62, -58.
- Lines where the per-note leads are worse than a constant: Horn 1 theme A (14 / 6 outside 25 / 60 against 10 / 2; median -26 against -1), Oboe 1 bars 15-22 (min -59 against -32), Cor anglais bars 41-44 (min -110 against -10), Flute 1 bars 41-44 (10 / 2 against 2 / 0; median -51 against +2), Cor anglais bars 47-52, Horn 1 bars 65-70, Horn 1 bars 53-60 (min -164 against -56).

Fix:
- `build/leg_leads.json`: delete every row of Flute 1, Oboe 1, Cor anglais, Clarinet 1, Clarinet 2, Bass clarinet, Bassoon 1, Bassoon 2, Horn 1, Horn 4 (43 rows).
- `build/score_config.py`: remove `LEG_EXTRA_S["Horn 1"]`, and the existing `LEG_PAIR_EXTRA_S` entries of Horn 1, Oboe 1, Flute 1, Bassoon 1. Set `LEG_LEAD_S` so the row lead is: Flute 1 0.04, Oboe 1 0.08, Cor anglais 0.06, Clarinet 1 0.07, Clarinet 2 0.065, Bass clarinet 0.09, Bassoon 1 0.07, Bassoon 2 0.075, Horn 1 0.095, Horn 2 0.09, Horn 3 0.08, Horn 4 0.11, Trombone 1 0.075, Horns 1-2 a2 0.08. Check that `SLUR_JOIN_LEAD_AT` Horn 4 268 (0.10, overshoot noted by the actor) becomes 0.05.
- New `LEG_PAIR_EXTRA_S` (seconds; pairs whose latency is consistent within 40 ms and more than 25 ms from the row):

```
"Flute 1": {(72, 73): +0.035, (75, 77): +0.025, (85, 82): +0.035, (90, 89): +0.030, (92, 94): +0.040},
"Oboe 1": {(68, 67): +0.030, (69, 70): -0.030, (70, 68): +0.065, (70, 72): +0.030, (70, 73): +0.030, (72, 70): -0.035, (73, 72): +0.025, (73, 77): -0.030, (75, 73): +0.030, (77, 78): -0.035, (82, 80): -0.045},
"Cor anglais": {(58, 60): +0.045, (66, 68): +0.030, (69, 68): +0.025},
"Clarinet 1": {(75, 74): +0.035},
"Bass clarinet": {(41, 44): -0.025, (43, 44): +0.030, (44, 37): +0.070, (46, 48): -0.045, (48, 49): +0.055},
"Bassoon 1": {(53, 51): +0.035, (53, 56): +0.075, (56, 55): -0.030, (60, 61): -0.060},
"Bassoon 2": {(51, 49): -0.025},
"Horn 1": {(56, 58): -0.055, (58, 61): +0.075, (60, 65): +0.025, (61, 60): -0.040, (62, 61): -0.050, (63, 61): -0.030, (63, 64): +0.105, (64, 63): +0.075, (65, 63): +0.080, (65, 66): +0.090, (66, 60): -0.040, (68, 66): -0.040, (68, 67): -0.030, (70, 68): -0.040},
"Horn 2": {(58, 61): +0.030},
"Horn 3": {(60, 61): +0.030, (61, 60): -0.030, (64, 63): +0.070},
"Horn 4": {(52, 51): +0.105, (56, 55): -0.080},
"Trombone 1": {(56, 57): -0.050},
```

Predicted (`fix2.py`): 263 joins, outside 25: 97 now, 13-17 after (in-sample; leave-one-out on recurring pairs gives about one in five); outside 60: 23 now, 1 after. Six joins stay 40-80 ms off because their pair is not consistent (Flute 1 113 and 118, Oboe 1 197.5, Clarinet 1 257, Bassoon 1 143 and 263): leave them. Acceptance, measured with S: per wind or horn line, median within +-15 ms, no join outside +-60, at most a quarter outside +-25, and no slur-neighbour difference over 60 ms.

### 3. Strings: the transition time varies by 100-200 ms between joins and is not predictable from the row, the interval or the pitch pair; the two violin sections change note up to 217 ms apart on the same onset (measured)

Where: Violins I, Violins II, Violas, Violoncellos, all thematic statements (448 joins).

Evidence:
- Row latency: Violins I Leg Slur MAX median 182 ms (robust SD 64, 5th-95th percentile 99-245), Leg BC MAX 176 (50); Violins II 231 (53) and 183 (58); Violoncellos 205 (44) and 157 (40); Violas Leg Slur MAX 205 (37).
- A constant lead per row gives 59 % outside 25 and 22 % outside 60; now it is 54 % and 21 %. A pair table, leave-one-out: 55 % and 26 %. Neither helps. Of 61 pitch pairs that recur on violins and celli, 39 differ by more than 60 ms between occurrences (Violins II 65 to 68: 242, 244, 158, 264 ms). No relation to interval class, velocity, CC11, CC1, the previous note's length or the note's count on the track (|r| at most 0.21). Cause not identified. It repeats exactly from render to render.
- So on the strings a per-onset row is the only data that reaches a join. The 60 existing string rows do work: 65 % within 25 ms and 95 % within 60, against 43 % and 76 % for the 404 joins without a row.
- `leadguard.txt`: 20 of the 22 kept rows that fail its 25 ms neighbour condition sound within 25 ms of the beat (S). The two that do not are Flute 1 113.5 (-32) and Horn 1 193 (-74), both removed by fix 2. The guard compares data leads of neighbours; with latencies that differ by 100 ms between neighbours, equal data leads produce unequal starts. The test should be on the audible start.
- Violins I against Violins II on the same onset: bars 22-30, 4 of 24 onsets more than 60 ms apart (max 124); bars 53-60, 6 of 30 (max 175); bars 70-78, 8 of 28 (max 217; qn 244, 246, 252). A doubled line that changes note in two steps sounds smeared.
- Lines where the per-note leads are better than a constant: Violins I bars 22-30 (10 / 3 against 19 / 7), Violins II bars 22-30, Violoncellos bars 22-30, Violins I bars 53-60, Violins II bars 70-78.

Fix: keep the string rows and add rows for the joins where the start is more than 40 ms off (late: both estimators over +40; early: S under -40 and the other under -25). New row = old row + 0.9 x S, at most 100 ms per pass. `build/leg_leads.json` values in seconds (these replace or add; 109 rows, list in `predict_S.txt`):

```
"Violins I": {"77": 0.09, "78": 0.06, "84": 0.05, "176": -0.04, "177": -0.04, "177.5": 0.05, "178": 0.05, "181": -0.04, "181.333": 0.04, "181.667": 0.07, "191.5": -0.07, "197.5": 0.05, "198": 0.04, "199": 0.07, "200": 0.01, "237.5": -0.07, "239.5": -0.06, "244": 0.08, "246": 0.05, "251.5": -0.06, "252": 0.16, "254": 0.07, "255": -0.04, "257": -0.04, "258": 0.05, "261": 0.05, "270.5": 0.04}
"Violins II": {"65": 0.06, "65.5": -0.06, "71": -0.06, "73.5": 0.08, "77.5": -0.07, "83": -0.04, "85": 0.07, "86.5": 0.05, "154": 0.04, "168": 0.08, "172": 0.05, "177": -0.09, "178": 0.04, "181": -0.1, "181.667": 0.07, "182": 0.09, "185": -0.04, "193.5": -0.06, "196": 0.05, "197.5": -0.1, "199": 0.08, "204": 0.1, "206": 0.04, "208": 0.06, "237.5": -0.04, "238": -0.07, "242": -0.08, "244": -0.1, "245.5": -0.02, "246": -0.08, "255": -0.08, "262": 0.08, "269": -0.04, "270.5": 0.05, "271": -0.09}
"Violas": {"60": -0.05, "70": 0.07, "74": -0.06, "109": 0.06, "110": -0.08, "111": 0.05, "111.333": -0.08, "114": -0.07, "118": -0.07, "188.667": -0.04, "189": 0.06, "194.667": 0.06, "195.333": 0.06, "240.5": -0.07, "242": -0.06, "243": -0.04, "244.5": -0.06, "247": -0.08, "248": -0.05, "249.5": 0.04, "257": 0.06, "257.5": 0.05, "258.5": -0.04, "286": -0.06}
"Violoncellos": {"51": -0.05, "68": 0.1, "68.5": 0.06, "81": -0.07, "130": -0.05, "131": 0.05, "145": -0.06, "156": 0.1, "160": -0.1, "184": 0.05, "188": 0.06, "190": 0.04, "193": -0.08, "199": -0.07, "200": -0.09, "219": -0.06, "219.5": -0.07, "241": -0.05, "244": -0.09, "255": 0.0, "259": -0.07, "261": 0.07, "292": -0.08}
```

Replace the lead guard's neighbour test by: after a range render, a changed row is kept if its start (S) is within 40 ms of the beat and no further from each slur neighbour's start than before. The actor should copy `robust_cross` from my `onsets.py` into `tools/pcx.py` and report S = the earlier of `pcx` and that crossover.

Acceptance (S): per string line at most a third of the joins outside +-25 and at most 2 outside +-60 (now 5-9); Violins I and II on a common onset never more than 60 ms apart and within 30 ms on two thirds of the onsets. Predicted: all lines 214 / 76 outside 25 / 60 now, 101 / 21 after fixes 2 and 3; violin pairs over 60 ms apart 18 now, 1 after. Every string note within 25 ms is not reachable in one pass: S itself has about 15 ms of error on a slow transition and the lead effect is 0.82-0.93 of the change.

### 4. Short figures are played unevenly because the lead is capped under the transition time; four viola triplet notes sound at 0.59-0.72 of their length (measured)

Heard length = next audible start minus own audible start, for 600 joined notes on all tracks. Four are under 0.75 of the printed length and six short notes are over 1.3.

- Bar 55, the theme's triplet (qn 181, 181.333, 181.667, then 182), printed 330, 330, 329 ms. Violins I sound 425, 354, 282. Violins II 454, 385, 357. Cause: the first triplet note has the full row lead (170 / 240 ms) but a short latency (124 / 134), so it is 46 / 106 ms early; the next two are capped at 0.45 of 330 = 148 ms (`LEG_CAP_FRAC` default) against latencies of 198-266, so they are 50-102 ms late.
- Violas bar 37 qn 111: 195 of 333 ms (0.59); bar 57 qn 189: 197 of 324 (0.61); bar 39 qn 116: 245 of 340 (0.72). Their neighbours qn 108.667, 110.667, 188.667, 190.333 sound 1.30-1.34 long. Cause: latencies of 133-322 ms inside one triplet under one lead (225-269 ms); no row.
- Violins I qn 77 (bar 26): 405 of 566 ms (0.72): it starts +102 late (lead 170, latency 272) and the next note (77.5) is 59 early. Violins I 251.5: 1.31 long, because 252 is +112 late with a 230 ms lead (latency 342).
- The actor's Violins I 192 "0.65" is not short in the audio: it starts at +6 ms and its successor at -6; its 280 ms lead matches a 286 ms latency. The "heard under 70 %" list in CHANGES.md (Cor anglais 125, 134, 135, 136, 151; Violins I 178, 182, 186) is the dominant-pitch method losing the pitch; by S none of these is under 0.75.
- No joined note is swallowed: every one of the 727 joins has an audible start.

Fix: the rows in finding 3 cover these notes (Violins I 181 / 181.333 / 181.667, Violins II 181 / 181.667 / 182, Violas 109-114 and 188.667-195.333, Violins I 77, 78, 252). They only act if the cap allows them: `LEG_CAP_FRAC["Violins I"]` add `(181.0, 182.01, 0.75)`, `LEG_CAP_FRAC["Violins II"]` change `(177.0, 187.0, 0.75, "listed")` to cover 181-182 unconditionally (drop "listed" for a `(181.0, 182.01, 0.75)` entry). Acceptance: the three triplet notes of bar 55 within 40 ms of 330 ms in both sections; no joined note under 0.75 or (for notes up to 1.2 s) over 1.3 of its printed length.

### 5. Trombone 1's quotation alternates early and late by 59-121 ms from note to note; the bar 78 run starts 100-118 ms early (measured)

- Trombone 1, bars 63-64 (qn 212.5-219.5), start of each note: -65, -18, +41, -35, -13, +52, +48, -73, +38, +106 ms. The slurred targets have a 100 ms lead against a 74 ms latency (early), the re-tongued notes (214.5, 216, 217, 218) have none (late by 38-52), the first note has a 110 ms entry lead (65 early), and the last note (219.5, Sus MAX after a join, in the allargando) is 106 late by both estimators. This is the passage Dan named for its accents; uneven starts add to the harsh impression.
  Fix: row lead 0.075 and the pair extra in finding 2; `REATTACK_LEAD_AT["Trombone 1"] = {214.5: 0.04, 216.0: 0.05, 217.0: 0.05, 218.0: 0.04, 219.5: 0.10}`; the 212.5 entry lead 0.11 to 0.05. Acceptance: all ten notes within +-30 ms, neighbours within 40 ms.
- Violins I and II, the run into bar 79 (qn 261.5-262, Sus MAX): starts -98, -106, -53 and -118, -106 ms. `GROUP_LEAD_AT` gives both tracks 0.15 s. Fix: `(261.5, 262.0, 0.05)` on both. Acceptance: within +-30 ms.
- Entries that read 65-229 ms late are soft or tremolo starts where pcX alone is less certain (Violin I solo 48 and 60: +110, +165 with leads of 260 and 160; Violins I 216 tremolo +229; Violins I 65 and 210: +65). Inferred, not for fitting this cycle; check them by level (time to body level minus 6 dB) after the tempo change.

### 6. Winds play their legato at velocity 86-104, not at the shortest transition (manual p.144; inferred)

The manual gives 110-127 as the short-transition range. The wind joins have both pitches within 6 dB for a median 55 ms, and the flute's audible start trails its note-on by 42 ms with spreads of 12-42 ms across the wind rows. Raising `LEG_VEL_BY_CC["wind"]` to 110-124 may shorten and tighten them, but it changes every wind latency, so the table in finding 2 would have to be measured again. Do not combine it with fix 2 in one render. Proposal for a later cycle: a range render of bars 36-47 with wind legato velocity 118 and compare the row latency spread.

## Do not touch

The printed tempo ramps (`RAMP_SPANS`) and the fermata; the 60 existing string per-onset rows other than those re-valued in finding 3 (they bring 95 % of their joins within 60 ms); Bass clarinet solo bars 31-36, Cor anglais quotation bars 47-52, Clarinet 1 bars 85-88 and Flute 1 bars 36-40 timing (all within about +-60, few outside 25); `CAESURA_LIFT` and the breath lengths (`CAESURA_BREATH_S`); string legato velocity 124; the viola rows 109.333 and 193.667, Violoncellos 76, 77, 145.5 and Violins I 185.5, 192, 258.5 kept by the lead guard.
