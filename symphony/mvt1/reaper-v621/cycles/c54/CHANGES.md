# Cycle 54: changes (actor)

Render: `cycles/c54/render/` (main pass, then pass 2; three stems carry a level fix, originals in `render_first/`).
Delivered: `cycles/c54/mvt1-mockup-c54.mp3`. Data the renders were made from: `cycles/c54/rendered_build/`.

## Priority 1 (Dan, 2026-11-10): the string theme at rehearsal A was choppy and not in steady time

### Before / after

Two measures. S (coordinator's `theme_S.py`: the earlier of pcX and the robust crossover, ms against the score beat) and
the dominant-pitch method (`theme_onsets.py`; my `theme54.py` is the same rule with printed lengths, level steps, a
-70 dB silence floor and a dip measure for same-pitch repeats). c53 = `cycles/c53/render` with its own parts.json and
tempo map; c54 = the full c54 render.

Violins I, bars 15-23 (qn 56-90), the coordinator's two scripts unchanged:

| script | c53 | c54 |
|---|---|---|
| `theme_S.py` (S) | n 41, median +3, robust SD 46, SD 47, min -81, max +163, 15 notes over 40 ms from the median, 7 over 60 | n 41, median +2, robust SD 6, SD 13, min -51, max +25, 1 over 40 ms, 0 over 60 |
| `theme_onsets.py` (dominant pitch) | found 39 of 42, median +26, SD 48, min -99, max +114, 15 over 40 ms | found 41 of 42, median +11, SD 30, min -82, max +93, 4 over 40 ms |

All theme lines (c53 → c54), from `cycles/c54/actor_scripts/allS54.sh` (`cycles/c54/theme/table_c53_c54.md`):

| line (score qn) | notes | S median | S robust SD | S SD | S min / max | over 40 ms (S) | dominant-pitch SD | over 40 ms (dom) | not sounding | under 60 % of length | eighths > 6 dB under |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Violins I 56-87.9 | 39 | +3 → +2 | 40 → 6 | 46 → 12 | -81/+163 → -51/+25 | 13 → 1 | 45 → 28 | 15 → 4 | 0 → 0 | 5 → 3 | 2 → 0 |
| Violins I 88-103 | 13 | -13 → -2 | 27 → 18 | 36 → 15 | -40/+84 → -30/+21 | 3 → 0 | 56 → 21 | 4 → 1 | 0 → 0 | 2 → 0 | 0 → 0 |
| Violins I 104-126 | 27 | +5 → +6 | 40 → 12 | 44 → 14 | -113/+84 → -26/+45 | 9 → 0 | 53 → 48 | 16 → 3 | 0 → 0 | 2 → 1 | 0 → 1 |
| Violins I 536-551.9 | 13 | -10 → -2 | 39 → 18 | 53 → 20 | -61/+127 → -30/+49 | 4 → 1 | 69 → 19 | 7 → 1 | 0 → 0 | 2 → 0 | 0 → 0 |
| Violins I 552-576 | 25 | +3 → +3 | 31 → 10 | 37 → 16 | -64/+100 → -28/+53 | 5 → 1 | 50 → 24 | 8 → 2 | 0 → 1 | 0 → 1 | 0 → 0 |
| Violins II 78-82 | 4 | -24 → +6 | 21 → 36 | 17 → 27 | -43/+2 → -20/+42 | 0 → 0 | 36 → 37 | 1 → 1 | 1 → 1 | 0 → 0 | 1 → 0 |
| Violins II 104-126 | 27 | -13 → +4 | 50 → 16 | 44 → 40 | -147/+93 → -197/+26 | 8 → 1 | 56 → 52 | 11 → 9 | 0 → 0 | 4 → 2 | 1 → 3 |
| Violins II 552-576 | 20 | -2 → -1 | 58 → 16 | 77 → 18 | -64/+234 → -26/+58 | 10 → 1 | 76 → 61 | 8 → 7 | 1 → 0 | 1 → 3 | 0 → 0 |
| Violas 104-126 | 27 | +1 → +0 | 62 → 15 | 41 → 17 | -66/+64 → -25/+48 | 14 → 1 | 88 → 65 | 9 → 5 | 1 → 1 | 5 → 3 | 1 → 1 |
| Violoncellos 520-536 | 19 | -10 → +2 | 41 → 28 | 45 → 56 | -109/+83 → -74/+196 | 4 → 5 | 71 → 70 | 10 → 5 | 0 → 1 | 2 → 1 | 1 → 1 |
| Flute 1 88-103 | 13 | +9 → +9 | 6 → 7 | 22 → 22 | -4/+84 → -6/+84 | 1 → 1 | 39 → 34 | 3 → 3 | 0 → 0 | 0 → 0 | 0 → 0 |
| Flute 1 104-126 | 23 | +5 → +5 | 10 → 10 | 25 → 16 | -68/+91 → -31/+50 | 2 → 1 | 41 → 44 | 5 → 5 | 0 → 0 | 1 → 1 | 1 → 1 |
| Flute 1 536-551.9 | 13 | +8 → +8 | 12 → 15 | 25 → 23 | -26/+81 → -12/+81 | 1 → 1 | 35 → 31 | 5 → 3 | 0 → 0 | 0 → 0 | 0 → 0 |
| Flute 1 552-576 | 16 | +13 → +12 | 17 → 16 | 17 → 13 | -22/+44 → -2/+37 | 0 → 0 | 39 → 27 | 2 → 3 | 0 → 0 | 1 → 0 | 0 → 0 |
| Oboe 1 88-103 | 13 | -23 → -11 | 33 → 32 | 42 → 47 | -109/+38 → -113/+36 | 4 → 6 | 50 → 52 | 4 → 5 | 0 → 1 | 1 → 1 | 0 → 0 |
| Oboe 1 104-126 | 23 | -21 → -20 | 13 → 15 | 21 → 25 | -48/+46 → -46/+76 | 2 → 2 | 46 → 37 | 4 → 3 | 4 → 4 | 4 → 3 | 2 → 1 |
| Oboe 1 536-551.9 | 13 | -13 → -13 | 34 → 37 | 43 → 42 | -115/+16 → -113/+18 | 4 → 4 | 47 → 46 | 4 → 4 | 0 → 0 | 1 → 1 | 0 → 0 |
| Oboe 1 552-576 | 15 | -4 → -2 | 30 → 30 | 29 → 26 | -65/+65 → -30/+68 | 2 → 1 | 42 → 77 | 5 → 5 | 2 → 1 | 3 → 3 | 0 → 0 |
| Clarinet 1 104-126 | 23 | -5 → +6 | 24 → 24 | 21 → 19 | -40/+35 → -34/+35 | 1 → 1 | 37 → 38 | 6 → 5 | 0 → 0 | 0 → 0 | 0 → 0 |
| Clarinet 1 520-536 | 19 | -3 → -2 | 33 → 14 | 45 → 37 | -48/+115 → -48/+112 | 4 → 4 | 30 → 25 | 3 → 2 | 0 → 0 | 0 → 0 | 0 → 0 |
| Clarinet 1 552-576 | 16 | -10 → +2 | 30 → 22 | 21 → 19 | -36/+27 → -37/+27 | 0 → 0 | 43 → 45 | 5 → 3 | 0 → 0 | 0 → 0 | 0 → 0 |
| Bassoon 1 520-536 | 19 | -16 → +9 | 34 → 15 | 50 → 31 | -87/+157 → -46/+103 | 4 → 3 | 49 → 48 | 6 → 4 | 0 → 0 | 2 → 2 | 2 → 1 |
| Trombone 1 520-536 | 19 | +4 → +8 | 27 → 30 | 34 → 50 | -97/+46 → -178/+54 | 5 → 6 | 61 → 51 | 9 → 4 | 0 → 1 | 2 → 1 | 2 → 2 |

Other measures:
- Row changes between consecutive notes of the theme lines (the cause of non-repeatable joins found in the Adagio):
  Violins I 53 of 106 joins → 2 of 108; Violins II 11 of 38 → 2 of 41; Violas 6 of 23 → 3 of 23; Violoncellos 5 of 17 → 0.
- Repeatability: the Violins I range (bars 15-23) rendered twice from one unchanged project gave identical readings on
  all 39 notes (pcX, crossover and dominant pitch: 0 ms difference). No per-note floor on the sustain row.
- Unprinted tempo steps inside the theme: 126 → 121 / 123 / 120 / 122 / 128 / 116 in bars 17-22 (and the same in the
  ff restatement and the return) → constant 126 from qn 56 to 128 and from qn 504 to 576.
- Per-note level (broadband RMS of each note against its section median and the printed shape; `levels54.py`):
  Violins I 56-88 residual SD 2.4 → 1.3 dB (range render m4; the full render was not re-fitted), section medians within
  1.1 dB of c53. Theme over celli 56-88 per quarter (my K-weighted measure, `q54.py`): median +6.33 → +6.47 dB, lower
  quartile +4.07 → +3.01, quarters under 0: 2 → 3.
- The repeated c'' across the bar 15-16 barline: c53 a 37 ms stub, the two C's one 630 ms note; c54 the eighth c''
  sounds, then a 14.9 dB dip with the tenuto c'' back at +85 ms (its dip minimum is 15 ms after the beat, so the
  re-articulation is about 40-80 ms late; see "Not done").

### What was changed
1. **Tempo** (`build/score_config.py`, c54 block): the phrase arcs (56, 72), (72, 88), (104, 120), (120, 128), (520, 536),
   (536, 552), (552, 568), (568, 576) and the pushes (88, 100), (552, 564) are removed. The printed poco rit. 576-584 and
   every arc in the Lento, transition, second theme, development and coda stay.
2. **One row, one lead per class** (`tools/score_to_parts.py` new generic rule `STEADY_LINE`, off by default): every
   monophonic note of a listed span that is not staccato, tremolo or pizzicato plays one row; note-on and note end are
   set after every other lead rule (leg_leads, slur-head, group, re-tongue, short-sus leads and caps no longer act on
   these notes). Movement I: **Sus Marc LITE** on Violins I 56-127 and 536-576, Violins II 77.9-82.1, 104-127, 552-576,
   Violas 104-127, Violoncellos 520-536. Leads: slurred note 90 ms, note after a bow change 50 ms, entry after a rest
   100 ms, same-pitch repeat 85 ms (celli +20 ms each). A slurred note ends at the next note-on (the 150 ms release cap
   carries it over), an unslurred one 30 ms before it, a note before a same-pitch repeat 50 ms before it. A round-robin
   reset (CC16) stands before each entry after a rest, so range renders and the full render play the same samples.
3. **Per-onset rows** (`build/steady54.json`, 58 rows; `fitrows54.py`): fitted once on range render m2 where pcX and the
   crossover agreed within 40 ms, checked on m3 / m4; rows on same-pitch repeats were taken out again (pcX cannot read
   them) and three overshooting rows halved.
4. **Per-note level steps** (`build/steady_levels54.json`, `levels54.py`): Sus Marc LITE plays 8-10 dB louder than the
   c53 mix of rows on the violins (3 dB on the violas, 1.5 dB on the celli) and the c53 per-note level rows were fitted
   to other samples; each note has a step that puts its section at the c53 median and the note on the printed shape.

### Variants tested (Violins I bars 15-22, range renders, measure S; `cycles/c54/theme/*_A_vln1_S.txt`)

| variant | S median | robust SD | SD | min / max | over 40 ms |
|---|---|---|---|---|---|
| c53 (per-note leads, three rows) | +3 | 40 | 46 | -81 / +163 | 13 |
| Sus MAX, one 90 ms lead | -28 | 27 | 44 | -76 / +211 | 6 |
| Sus Marc LITE, one 60 ms lead | +28 | 21 | 22 | -14 / +88 | 4 |
| Slur Runs (the fast legato row), 80 / 50 ms | -7 | 43 | 40 | -60 / +101 | 12 |
| Leg Slur MAX with one 240 ms lead | -56 | 47 | 57 | -282 / +22 | 16 |
| Sus Marc LITE, leads by class (m2) | +3 | 13 | 31 | -35 / +164 | 2 |
| the same with per-onset rows (m6, as shipped) | 0 | 9 | 12 | -51 / +25 | 1 |

Dominant pitch on the same renders: c53 SD 45; Sus MAX 35; Sus Marc LITE 31; Slur Runs 56; legato 53; shipped 22.
The Sus Marc LITE stem is 0.7 dB brighter than the Sus MAX stem in 2-5 kHz against 0.5-2 kHz (-1.4 against -2.1 dB).

Winds: the same rule on the legato row (Oboe 1, Clarinet 1, Bassoon 1, Trombone 1) was tested and **not shipped**:
Oboe 1 104-126 robust SD 13 → 16, 88-103 33 → 36, Clarinet 1 104-126 24 → 25 with the median at +40 ms. Flute 1 was
already at robust SD 6-17 in c53 and was left alone. The winds' theme lines changed only through decision 3 below.

### Limits not met
- Coordinator's target on S (robust SD under 20 ms, 0 notes over 40 ms from the median): met on robust SD for every
  string theme line except Violins II 78-82 (4 notes, 36) and Violoncellos 520-536 (28); notes over 40 ms: 0-1 per
  line except Violoncellos 520-536 (5, two of them same-pitch repeats that pcX cannot read).
- On the dominant-pitch script the Violins I line reads SD 30 with 4 notes over 40 ms. The four are g' (bar 17 beat
  1.5 +72, bar 18 beat 3 +93), a-flat' (bar 19 beat 1.5 -82) and the entry of bar 23 (-78); two more read short (d-flat''
  105 and 95 ms of 238). A 50 ms window cannot separate pitches a semitone apart (392 / 415 Hz, and d-flat'' between
  c'' and d''), and S reads the same notes within 25 ms. Bar 16 beat 1 (the repeated c'') is "not found" by that
  script because a same-pitch repeat merges with the note before it; the dip is measured above.
- "Every eighth at least 60 % of its printed length": 3 notes of 42 read under 60 % on the dominant-pitch measure
  (the semitone cases above).

## Coordinator decisions on the critic reports

| # | Decision | Done | Measured on the c54 render |
|---|---|---|---|
| 1 | C #2 Violins I 128 a down-bow stroke | yes | C6 reads S -26 ms (c53 +175): pass |
| 2 | C #5 string legato after Sus-row notes | yes (SHORT_SUS_AT for slurred notes, DOWNBOW_STROKE_AT for Violas 368, Violoncellos 356, Violins II 400; 0.09 s leads through retongue_leads.json) | S: Violas 76 +18, 428 +24, 434 -2, 436 +6, Violoncellos 356 +28, Violins II 400 -24: 6 of 8 within ±40. Violas 368 -52 and Violins II 290 -61 (pcX only) fail. Violas 168 fill in. Oboe 1 578 +27 ms (c53 +95 / +117) |
| 3 | C #1 slur-start joins | shipped after the range test (`SLUR_START_SUS["head_end_s"]` 0.03, `SOST_JOIN_LEAD_S` 0.07 for winds / brass; 97 joins) | crossover against the beat, range test → full render: Bassoon 1 131 +50 → +4, 133.5 +82 → +24, Clarinet 1 509.5 +57 → +22, 507 -3 → -20 (its row halved). Cor anglais 275: row deleted (C's fix); crossover +42 ms, pcX +157: **late, fails ±20** |
| 4 | C #3 wind entry leads | yes | half-amplitude against the beat: Bassoon 1 13 entries -10..+10 ms (c53 91-115 ms early); Oboe 2 44 / 520 / 664 / 552 / 408.5 -25..0; Flute 2 100 / 104 / 160 / 548 / 552 -10..+10; Horn 2 324 -5; Horn 1 520 +35 (c53 -75; over the ±30 target). Bassoon 2 464, Contrabassoon 464 and Horn 2 104 are not clean entries (no reading) |
| 5 | A #1 cor anglais 26 | yes | stem dip 0.9 dB, master dip 1.1 dB (c53 7 / 5.6): pass |
| 5 | A #2 basses final chord | yes (RR reset at 712, six fills refitted on a range render, then per-piece steps as a stem fix) | pieces -58.6 -58.0 -58.0 -58.3 -59.4 -62.7 -62.9 dB, steps +0.6 0.0 -0.3 -1.1 -3.3 -0.2 (c53 +6.0 -1.8 +6.3 -10.7 +2.7 -2.7): pass |
| 6 | B #1 celli under the tune | yes | celli minus Violins I 97-99 -1.9 -1.2 -2.3 (pass); melody group minus celli 156-159 +4.0 +7.4 +4.7 +3.2 (quarter 159 0.8 dB short after a stem fix); accent at 526 3.2 dB (pass); 557.0 / 557.5 -2.4 / -3.6 (pass) |
| 6 | B #2 bass clarinet 464-492 -5 | yes | minus tuba -6.8..-1.0; share of 30-150 Hz 9-16 %: pass |
| 6 | B #3 Oboe 1 pitch trims | yes | minus Violins I on 22 onsets: median -5.4 (pass), max -0.4, 4 over -2 (fails "none over -2"); 496-503 as c53 |
| 6 | B #4 basses E2 and pizzicato | yes (resets at 184, 408, 584 with the 712 one) | spread 3.3 dB at 184-216 and 5.8 dB at 584-616 (c53 9.3 / 12.8): pass. Arco E2 against the track's fit not measured |
| 7 | A #3 first bar-30 staccato | no row needed | with the c54 resets the four strokes read S +7 +45 +16 +11 ms; the row tried first (lead 0) read +49 on a range render and was taken out |
| 7 | A #5 Flute 1 115.5 breath gap | yes | not measured (pass-2 pair) |
| 8 | B #5 timpani 532-536 | yes | 7.0 6.1 6.2 6.0 dB under the theme group (after a stem fix on quarter 535): pass |
| 8 | A #6 three join fills | rows in (`early_fills.json`) | not measured |
| 8 | C #4 bar 152 run, wind hang at stops | not done | open |

The 17 stem-fix rows of c53 reached REAPER (every main and pass-2 track was rebuilt with `--midi-only --tempo`, which
writes the volume envelopes): Oboe 1 minus Violins I at 496-503 reads -4.3 -3.4 -3.5 -3.2 -2.8 -3.0 -5.0 -4.2, as c53's
fixed stems (-4.3 -3.4 -3.5 -3.3 -2.9 -3.0 -5.0 -4.2). The other 16 rows were not checked one by one.

## Stem fix after the render (level only, `tools/stem_fix.py 54 cycles/c54/rendered_build build --apply`)
Double basses (final-chord steps), Violoncellos (-2.5 dB in quarter 159), Timpani (-1.5 dB in quarter 535). The rows are
at the end of `build/score_config.py` and are **not yet in the REAPER projects** (next build). `rendered_build/` holds
the data as rendered.

## Tools
- `tools/score_to_parts.py`: `STEADY_LINE` (see its default: row, leads by class, ends, `at` rows, `level_db` steps,
  `rr_reset`; parts.json `steady_line`, `cc16`), `SLUR_START_SUS["head_end_s"]`. With neither set parts.json is unchanged.
- `cycles/c54/actor_scripts/`: `theme54.py`, `theme_S54.py` (S for any render folder, range renders included; `S/` holds
  the coordinator's onsets.py / pcx.py / lines.py), `allS54.sh`, `table54.py`, `fitrows54.py`, `levels54.py`, `q54.py`
  (critic B's c54 table), `checks54.py`, `pdiff54.py`, `rangetest54.py`, `apply54.py` (the json edits; the basses' fills
  come from `fit_rebows.py --only ... --render-dir cycles/c54/rangetest/cb --render-t0 703.5 --fine --write`),
  `turnlock54.py`, `r1`-`r7.sh` (the REAPER phases).

## Render conditions
- State guard: 0 stale before the main render (Violas read stale after the range tests and was rebuilt in full); the
  save after the main render read 3 (Trumpet 1, Trumpet 2, Trombone 1), rebuilt, 0 at quit. Pass 2: 0 before, 3 after
  (Bassoon 1 stac, Cor anglais stac, Flute 1 stac), rebuilt, 0 at quit.
- **Memory**: another user process (a 31 GB Python job of another project) ran during the main render. REAPER 46 GB
  with 45 GB compressed before the render, 34 GB after; rendered with `--force-memory`. Checked afterwards: attack probe
  "late or hole: 0"; Flute 1 464-480, Trumpet 1 628-644 and Violins I 440-456 on their own tempo maps against c53: pcX
  median change 0 ms, 1 of 39 notes moved 25 ms or more. Pass 2: REAPER 20 GB, 0 compressed.
- `metrics/state_check.txt` lists 18 runs; they come from comparing against c53 across the changed tempo map (pcX
  medians of about -150 ms, the removed arcs' total) and are not state changes (see the Flute 1 check above).
- Disk: 12-28 GB free during the renders (the brief asks 30).

## Delivery (`master_eq` unchanged)
-19.7 LUFS integrated, LRA 14.3 LU, true peak -1.6 dBTP, limiter about 0.8 dB, p10-to-max span 18.9 dB, 433.6 s.
Climax order kept: bar 160 -11.3 > 122 -11.9 > 167-170 -13.6 > 26 -14.6. Shares: 100-250 Hz -8.97, 250-500 Hz -5.65,
2-6 kHz -10.00, 6-20 kHz -30.04 dB (c53 -8.77, -5.85, -9.95, -30.22). Master before delivery: -21.0 LUFS, LRA 23.1,
true peak -1.2 dBFS. No limit fails.

## Not done, not verified
- The tutti-stop decays were not re-measured: `deliv53.py --stops` holds the stops in seconds of the c53 map.
- Re-bow fills in bars 15-32 and 131-144 were not refitted after the tempo steps were removed (piece lengths changed by
  up to about 40 ms there); join fills of the non-theme tracks in those bars were not refitted either.
- Existing rows on the other 93 slur-start joins (Flute 2 275.5-283.5, Bassoon 1 413 / 531.5 / 575.5, Clarinet 1 421.5)
  were not re-checked after decision 3.
- Same-pitch repeats inside the theme (Violins I 60, 108, 572, celli 524): lead 85 ms from one range test; the
  re-articulation reads 40-80 ms late.
- Violas 368 (-52 ms), Violins II 290 (-61), cor anglais 275 (+42), Horn 1 520 (+35), Violoncellos 520-536 as a line:
  timing rows for c55.
- Winds' theme lines (Oboe 1 robust SD 15-37, Trombone 1 30): the coordinator's row-lead plus pitch-pair table was not built.
- MANUAL-GAPS: no new gap tried.
- EW-TEMPLATE-PLAN sections still not applied: 5 (legato overlap 45-80 ms; the theme now has none), 6 (two tracks per
  string section), 7 (per-note lean-off), 8 (tutti entry spread), 10 (beat-position velocity outside the listed spans).
