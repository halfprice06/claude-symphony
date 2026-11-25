# Cycle 7: changes (render of c07, reviewed by the critics of c08)

Inputs: `loop/ONE_TIME.md` (brass accents, Dan's item 8) and critic reports A (articulation), B (balance), C (timing) on the c06 render. Snapshot before the changes: `before/`. One render from a freshly restarted REAPER (`--midi-only --tempo` on all 32 tracks; no Opus state changed, so no patch reloaded), then one level-only stem fix (below). First render: `render_first/`, `metrics_first/`, `render_first_delivery.mp3`; `render/`, `metrics/` and `mvt1-mockup-c07.mp3` are the fixed version, and the REAPER project matches it (`--mix-only` on the 8 fixed tracks after a restart, saved, REAPER quit).

## Changes

Tools (`tools/score_to_parts.py`: generic rules with defaults, movement I values in `build/score_config.py`):
1. ONE_TIME: `build/accent_fits.json` (new per-note table, read as `ACCENT_FITS`): a fitted swell level per accent, `{track: {score qn: swell dB or [swell dB, step trim dB]}}`; a fitted accent on a GENTLE_ACCENT family takes that swell with the family's shape (0 at the onset, full at +0.07 s, held to +0.25 s, gone by +0.6 s; no ACCENT_MINUS_HPGAIN, since the fit measured the result) and the trim as a step note trim (0.1 s ramp). A per-onset `ACCENT_DB_AT` level on a gentle family now also keeps the gentle shape (before it fell back to the c11 10 ms rise). parts.json `acc_fitted`, `acc_trimmed`.
2. New tool `tools/fit_accents.py PREV RENDERED_PARTS [--write]`: measures each accent's level (+0.05..+0.35 s) against up to two unaccented notes each side within 2.5 qn at the same CC11 (±6), separates what the volume envelope contributes from what the samples/rows give (residual), rebuilds parts.json with the current config and iterates the fitted swells (max 5 dB, then a step trim of -6..+3 dB) until every predictable accent is predicted inside 2-4 dB. Accents whose articulation changed since the render are not predicted. Also prints 2-5 kHz energy over the first 80 ms minus the body.
3. A #1 `ROW_TRIM_DB` {track: {row: (dB, min_cc)}}, `ROW_TRIM_NEAR_QN` 3.0, `ROW_TRIM_SKIP`: a loud note on a listed Sus/Stac row in a line that has a Leg-row note within 3 qn gets a step trim; consecutive trimmed notes are one step (no bump at each join). Excluded: chords, down-bow strokes, re-bowed notes, REP_SPLIT strokes, listed spans. Accents and STR_SHORT_AFTER_SUS strokes are trimmed (see the stem fix). parts.json `row_trimmed`.
4. A #2 `WIND_REP_RETONGUE_BY` (overrides by track-name prefix or family), `WIND_REP_RETONGUE_SHORT` (repeats of 0.5 qn or less at 100 bpm or faster), `BREATH_FALL_BY` (CC11 fall at loud wind/brass breaths by prefix/family).
5. B #4 a timpani roll that continues another roll takes no `TIMP_LOUD_ATTACK_DB` bump unless a printed dynamic louder than the last mark starts on it (`TIMP_CHAIN_BUMP_AT` lists exceptions); parts.json `timp_chain_skip` (320, 632, 640).
6. A #5 `TIMP_METRIC_VEL` {down, mid, beat, off, jit, min_cc}: velocity offsets on loud Flt Lng strokes by position, seeded jitter.
7. B #1 `build_perc_track` reads `LEVEL_SHAPES` (exact breakpoints).
8. C #2 `SHORT_SUS_LEAD_KEEP_OVERLAP`: with `SHORT_SUS_LEAD_TRACKS`, the previous slurred note ends at the moved onset + this many qn.
9. C #3 `ENTRY_LEAD_S` tuples may carry a third value for entries at CC11 51-80 at `ENTRY_MID_MIN_BPM` (100) or faster.
10. C #4 `smooth_tempo`: a printed rit. ramp (falling steps) never speeds up: when its start tempo is under the first printed step, it holds the start tempo until the steps fall below it. `phrase_arcs` warns when an arc ends where a ramp starts.
11. `ABUT_LEAD` no longer leads into or out of a note that `AUTO_REBOW` splits (its re-bow points and fitted shapes are keyed to its start; the first build moved 26 basses re-bow rows).
12. A #6 `SHORT_SUS_LEG_SKIP` {track: [qn]}: exceptions to `SHORT_SUS_LEG_TRACKS`.
13. C #6 `tools/deliver_master.py`: the mp3 ends 1.0 s after the last 50 ms window above -65 dBFS, with a 0.5 s fade (`TAIL_DB`, `TAIL_S`, `FADE_S`); the wav render keeps its +8 s for measurement. Delivered length 440.60 -> 434.25 s (tail 1.00 s).

Config (`build/score_config.py`, `build/*.json`):
14. ONE_TIME + A #3: `GENTLE_ACCENT["brass"]["keep_legato"] = True` (Horn 1 273/665/673, Trumpet 1 665/673, Trombone 1 521/529 now legato targets with the legato lead and v124); `accent_fits.json` (below).
15. A #1 `ROW_TRIM_DB`: Violins II Sus MAX -4.0, Violas Sus MAX -4.5 / Stac RRx9 -4.0, Violoncellos Sus MAX -1.5 / Stac RRx9 -4.0, Violins I Sus MAX -1.5 / Stac RRx14 -3.0, all at CC11 >= 80 (48/48/40/21 notes after the stem fix: Vln I/II/Vla/Vc). `ROW_TRIM_SKIP` Violas [388.5,408] and [464,484] (the c05 stroke roles).
16. A #2 horns `{"gap_s": 0.10, "frac": 0.3, "fall_cc": 12, "fall_s": 0.15}`; short repeats `{"max_qn": 0.5, "min_bpm": 100, "gap_s": 0.10, "frac": 0.45, "fall_cc": 8}` (A proposed frac 0.45 with the 0.06 s gap, which the gap would have capped); `BREATH_FALL_BY` Horn 10 CC; `BREATH_GAP_AT` / `BREATH_FALL_CC` Trombone 1, Bass trombone, Trumpet 3 at 632: 0.22 qn, 10 CC.
17. A #5 `TIMP_METRIC_VEL` down 0, mid -3, beat -5, off -9, jit 2, at f and louder.
18. A #6 Violins I test kept (A's evidence: crossover +0.065 against +0.095 s, master dips equal to the control at shared onsets); 77.5, 259.5, 455.5 back to Sus MAX. Wind portato joins Oboe 1 405 and Flute 1 393 back to the re-tongue (they dipped less there in c05).
19. C #1 `ABUT_LEAD` Double basses 0.12 s, Horns 3/4 0.06 s (skip_next_same, old note ends at the moved start): 72 / 42 / 20 notes led.
20. C #2 `SHORT_SUS_LEAD_S` 0.06, `SHORT_SUS_LEAD_TRACKS` ("Violins II",), `SHORT_SUS_LEAD_KEEP_OVERLAP` 0.03 (Violas the control; Violins I is on the A #6 Leg Slur test).
21. C #3 `ENTRY_LEAD_S["string"] = (0.12, 0.06, 0.12)`, Double basses kept at (0.12, 0.06) (their off-beat eighths were already on time).
22. C #4 `PHRASE_ARCS` (568,576) "main" -> "sub"; `RAMP_SPANS` (576,584) 126 -> 120, (244,260) 112 -> 115, (620,632) 112 -> 115. Beats 576-579 now 120 bpm, then falling to 112 (before: 111 at 575, 126 at 576, a 13% speed-up inside the poco rit.); the animandos start at the printed 115.
23. B #1 roles [628,644]: Violins I +1.5 -> -0.5, Violins II, Trumpet 1, Horn 1 +1.5 -> +2.5; `LEVEL_SHAPES["Crash cymbals"]` -4 dB on the attack (636.02-636.6, back by 637.2).
24. B #2 roles: bars 69-71 Horn 1, Violins II, Clarinet 1 [272,284,+2], Violas +1.5, Trumpet 2 -3, Horns 3/4, Oboe 2, Bass clarinet, Violoncellos -2; bars 131-134 Violoncellos, Bassoons 1/2 [520,536,+2], Trombones 1/2 +2.5, Violins I/II [520,536] -2 -> -3.5.
25. B #3 `pitch_trims.json`: Clarinet 1 B-flat5 -4, `_all_arts_pitches` [68] -> [68, 79, 80, 82]; Cor anglais A-flat4 -4, `_all_arts_pitches` [68, 69].
26. B #4 Timpani [637,640,+3]; B #5 Trombones 1/2, Bass trombone [696,712,+2.5], Bass clarinet +2, Clarinet 1 [699,712,+2].
27. `accent_fits.json`: first fit on the c06 render (17 brass accents), refit on the c07 render (stem fix, below).

The parts.json diff against c06 was checked before rendering: every `rebows` and `restrikes` row unchanged (after change 11); tempo differs only at 244-260, 576-584, 620-632; note changes only at the listed rules; CC11 at every newly led note-on equals its score-onset value except slurred Sus eighths inside crescendos (1-2 CC) and legato targets (by design).

## Stem fix after the render (`stem_fix.py`, level only; master rebuilt as the stem sum)

- Brass accents: `fit_accents.py 7` on the c07 render (rendered parts as reference). The legato accents of change 14 measured +0.0..+2.3 dB over their slur (the theme-head pickups carry the c06 +3 dB legato trims and the legato transition); fitted swells of 4.9-5 dB (+0.7..+3 dB trims on three). Horn 1 382 and Trombone 1 382 (+5.8/+7.9, their neighbour 383.5 now shorter) got -0.4/-3.1 dB trims. 17 -> 26 fitted accents.
- Row trims: the violas' accented Sus notes 110 and 670 measured 6.6-6.8 dB under the STR_SHORT_AFTER_SUS stroke after them, which change 3 had excluded; strokes are now trimmed with their line except in the c05 stroke-role spans (`ROW_TRIM_SKIP`): +2 / +6 / +1 trimmed notes on Violins II / Violas / Violoncellos (48 / 40 / 21 in all).
Only `vol_db` changed on 8 tracks (Horn 1, Horn 2, Horn 4, Trumpet 1, Trombone 1, Violins II, Violas, Violoncellos), so the fix is exact; master peak unchanged (1.331).

## Measured, c06 -> c07 (fixed render)

**ONE_TIME, brass accents** (`tools/fit_accents.py`: level over the unaccented neighbours at the same CC11 within 2.5 qn; 2-5 kHz energy over the first 80 ms minus the body, +0.15..+0.5 s, from the sounding onset). 36 accents with such neighbours: in 2-4 dB 16 -> 33, median +3.55 -> +3.0 dB.

| Track | qn | over c06 | over c07 | 2-5 kHz c06 | 2-5 kHz c07 | row c07 | fit (swell, trim) |
|---|---|---|---|---|---|---|---|
| Horn 1 | 124 | 4.0 | 3.0 | 3.1 | 4.2 | Sus MAX | 1.3 |
| Horn 1 | 273 | 5.1 | 3.1 | -2.6 | -1.4 | Leg Slur MAX | 5.0 |
| Horn 1 | 278 | 4.5 | 3.0 | -18.6 | -17.6 | Sus MAX | 0, -0.63 |
| Horn 1 | 282 | 2.8 | 3.5 | -21.2 | -16.9 | Sus MAX | |
| Horn 1 | 284 | 1.7 | 3.0 | -4.8 | -4.8 | Sus MAX | 4.68 |
| Horn 1 | 285 | 2.6 | 2.9 | 2.8 | 2.4 | Sus MAX | 4.26 |
| Horn 1 | 311 | 0.3 | 3.0 | 0.8 | -2.1 | Leg Slur MAX | 5.0, +0.56 |
| Horn 1 | 382 | 2.2 | 3.0 | -5.4 | -4.1 | Sus MAX | 0, -0.38 |
| Horn 1 | 665 | 2.6 | 2.9 | -2.1 | 3.6 | Leg Slur MAX | 5.0, +0.72 |
| Horn 1 | 673 | 9.5 | 3.0 | -11.3 | -0.5 | Leg Slur MAX | 5.0, +0.85 |
| Horn 1 | 676 | 5.2 | 2.8 | -17.8 | -17.4 | Sus MAX | 0.22 |
| Horn 2 | 124 | -0.5 | 3.0 | -5.6 | -11.1 | Sus MAX | 5.0, +0.52 |
| Horn 3 | 124 | 3.5 | 3.8 | -2.6 | -3.3 | Sus MAX | |
| Horn 3 | 317 | 3.8 | 3.8 | 2.8 | 2.6 | Sus MAX | |
| Horn 3 | 321 | 3.9 | 3.8 | 2.6 | 2.4 | Sus MAX | |
| Horn 4 | 124 | 5.5 | 3.1 | -7.9 | -4.5 | Sus MAX | 0, -1.01 |
| Trumpet 1 | 284 | 14.0 | 6.3 | -5.7 | -2.3 | Sus Non Vib MAX | 0, -6.0 |
| Trumpet 1 | 285 | 13.4 | 5.7 | -8.1 | -4.1 | Sus Non Vib MAX | 0, -6.0 |
| Trumpet 1 | 325 | 4.2 | 2.9 | -12.2 | -10.9 | Sus Non Vib MAX | 1.06 |
| Trumpet 1 | 328 | 2.2 | 2.3 | -6.7 | -6.4 | Sus Non Vib MAX | |
| Trumpet 1 | 330 | 1.0 | 3.0 | -19.8 | -21.4 | Sus Non Vib MAX | 4.54 |
| Trumpet 1 | 665 | 5.3 | 2.6 | -12.0 | -4.6 | Leg Slur MAX | 4.94 |
| Trumpet 1 | 670 | 3.4 | 2.8 | -12.7 | -12.5 | Sus Non Vib MAX | 1.09 |
| Trumpet 1 | 673 | 3.5 | 2.3 | -12.7 | -15.6 | Leg Slur MAX | 5.0, +3.0 |
| Trumpet 1 | 676 | 7.7 | 3.0 | -9.9 | -7.7 | Sus Non Vib MAX | 0, -3.32 |
| Trumpet 3 | 124 | 1.8 | 3.2 | -8.0 | -9.3 | Sus Non Vib MAX | 3.89 |
| Trombone 1 | 124 | 3.1 | 3.1 | -9.6 | -9.6 | Sus MAX | |
| Trombone 1 | 317 | 1.9 | 3.2 | -5.0 | -5.4 | Sus MAX | 3.83 |
| Trombone 1 | 321 | 9.8 | 2.9 | -11.5 | -7.8 | Sus MAX | 0, -4.68 |
| Trombone 1 | 382 | 3.7 | 2.6 | -15.1 | -9.8 | Sus MAX | 0, -3.13 |
| Trombone 1 | 521 | 4.3 | 2.3 | -15.4 | -7.4 | Leg Slur MAX | |
| Trombone 1 | 526 | 3.1 | 3.2 | -13.9 | -13.0 | Sus MAX | |
| Trombone 1 | 529 | 4.6 | 3.2 | -18.3 | -13.8 | Leg Slur MAX | 5.0, +1.11 |
| Trombone 2 | 124 | 2.4 | 2.4 | -6.8 | -6.8 | Sus MAX | |
| Bass trombone | 124 | 3.6 | 3.6 | -12.6 | -12.6 | Sus MAX | |
| Tuba | 124 | -3.7 | 1.6 | -7.9 | -13.1 | Sus MAX | 5.0, +3.0 |

What lifted them (measured on c06 by separating the volume envelope from the rest): the swell (2.5 dB) and the arrival/role lifts explain only part; the residual (rows, pitch, samples) ran -6..+9 dB per accent. The slurred theme-head accents (Horn 1 273/665/673, Trumpet 1 665/673, Trombone 1 521/529) were re-tongued on Sus after a 0.07 qn gap (residual +4.4..+8.4 dB over the legato notes); Trumpet 1 284/285 (+14 dB) sit after legato notes that sag 6-8 dB into a join; Trombone 1 321 (+9.8) after a short pickup. Velocity has no effect (c06); CC11 at the accents equals their same-dynamic neighbours' (no bump; measured from parts.json); the DETACH_ACCENTS gaps are not in the measure (neighbour levels are taken inside each note's body; inferred to play no part). Not met: Trumpet 1 284/285 at +6.3/+5.7 (trim at its -6 dB limit; against the bar's earlier notes 280-282 they sit about +4); Tuba 124 +1.6 (swell at its 5 dB limit). 2-5 kHz first 80 ms minus body over 3 dB: Horn 1 124 (+4.2; +3.1 in c06, its swell went 2.5 -> 1.3) and Horn 1 665 (+3.6: the window holds the end of the pickup eighth, which is 10-16 dB brighter than the accent's body; the accent itself is not bright).

**A #1 rows** (`after.py`: accented note's first 0.03-0.2 s against the loudest of the next 2-3 unaccented notes; accents more than 2 dB under): Violins I 6 -> 4, Violins II 6 -> 7, Violas 7 -> 6, Violoncellos 2 -> 2. Vln II 105 -9.4 -> -3.7, 553 -12.3 -> -8.4 (partly the printed cresc.), 113 -4.8 -> -3.3; Vla 381 -7.8 -> -6.0, 349 -6.0 -> -5.5. Criterion (2 or fewer per track) not met.
**A #2 repeats** (median dip, repeats under 3 dB; gaps up to 0.4 qn counted): Horn 1 -2.7 -> -5.05 (8 -> 6 of 16), Horn 2 -2.1 -> -4.7 (9 -> 6 of 15), Horn 3 -4.1 -> -4.3 (11 -> 7 of 31), Horn 4 -2.05 -> -2.8 (29 -> 21 of 40), Bassoon 2 -3.1 -> -6.1 (bar 82 eighths all at 3 dB or more). Horn 4 not met. **Breaths**: at 636 Trombone 1 -0.7 -> -7.5, Bass trombone -1.6 -> -8.3, Trumpet 3 -2.5 -> -9.4 dB (Trumpet 1 -10.7 control); horn breaths Horn 1 475 -3.0 -> -3.1, Horn 4 512 -2.6 -> -2.6 (soft: the fall applies at mf or louder), Horn 3 536 -0.3 -> -2.1.
**A #3** see the accent table: the legato theme heads are 2.3-3.2 dB over their slurs after the fit; legato velocity 124, lead 0.06/0.10 s.
**A #5 timpani metric velocity**: off-beat stroke peak minus the next downbeat (bars 27-30, 82, 131-134; median of 15) -0.4 -> -1.0 dB (target 2-4: not met; round robins dominate the 9-step velocity offset).
**B #1**: Violins I minus Violins II / Trumpet 1 / Horn 1 per bar 158-161: +2.1..+6.6 / +2.2..+4.8 / +0.1..+3.3 -> -1.1..+3.8 / -0.7..+1.9 / -2.8..+0.3 dB; crash peak minus master peak over 636-637 -10.3 -> -14.7 dB. **B #2**: bars 69-71 theme minus harmony per bar +2.1/+1.8/+0.3 -> +5.8/+5.0/+3.5, Horn 1 minus Trumpet 2 +1.3..+2.5 -> +5.7..+6.6; bars 131-134 theme minus countermelody +0.4/+0.1/+1.6/-2.6 -> +3.1/+2.5/+4.4/+0.6. **B #3**: Clarinet 1 at 414/422 minus master -1.7/-0.9 -> -4.0/-3.4 (B simulated -7.7/-6.9), Cor anglais 361/371 -6.7/-7.6 -> -9.5/-10.9. **B #4**: timpani minus master over 320-320.5 (chained roll) -2.5 -> -5.6 (no second hit), 321.5-322 -12.3 -> -10.3, fff roll 637-640 -19.6 -> -16.7 dB. **B #5**: chorale trombones minus strings per 4 qn -4.4/-0.9/-4.0/-1.4 -> -1.9/+1.6/-1.5/+1.1.
**C #1** crossovers (8192-point, harmonics 2-8, from the score onset; median / p90): Double basses +0.155 / +0.319 -> +0.070 / +0.250 s, basses minus celli at shared changes +0.105 -> +0.050 (target +0.04), Horn 3 +0.100 -> +0.050, Horn 4 +0.115 -> +0.080 s (target +0.06).
**C #2** slurred Sus MAX eighths under 0.3 s: Violins II +0.122 -> +0.083 s (n 16 -> 20; target 0.07), Violas (control) +0.085 -> +0.080.
**C #3** string entries after a rest in the Allegro, time to body - 8 / - 4 dB (medians): Leg Slur MAX at CC11 51-80 +0.065/+0.170 -> +0.030/+0.130 s, Sus MAX +0.055/+0.173 -> -0.005/+0.118 s; f and p layers unchanged.
**C #4** beats 574-584: 123.5, 119.7, then 120.0 to 579, falling to 112 at 584 (before 119.7 -> 126 at 576).
**C #6** delivered mp3 434.25 s (was 440.60), 1.00 s after the last window above -65 dBFS.

- **Delivery**: master -16.5 -> -16.6 LUFS, LRA 21.6 -> 21.3 LU, sample peak 1.562 -> 1.331, true peak +4.0 -> +2.5 dBFS. Delivered -19.8 / -19.8 LUFS, LRA 15.2 -> 15.3 LU, p10 span 20.0 -> 20.0 dB, limiter 3.2 -> 2.0 dB, -1.7 dBTP. Motion (mp3) dS4 p90 / 1s-20s 9.07/4.79 -> 8.91/4.76.
- **Climax order** (delivered short-term max, LUFS): bar 160 -9.41 -> -9.33, bar 122 -10.36 -> -10.07, bars 167-170 -12.18 -> -12.40; margin 160 over 122 0.95 -> 0.74 dB.
- **Master top peaks**: 1.331 (qn 636.45: Violins I, Horn 1, Violins II), 1.287 (642.15: Bass trombone, Trombone 1, Trumpet 1), 1.201 (638.1), 1.200 (484.9: tam-tam).
- **Attack probe**: 0 flagged.
- **Dan's item 7**: no held-note data changed (re-bow and re-strike rows identical to c06).
- **Memory**: REAPER 17 GB (0 compressed) when the render started, 43 GB with 23 GB compressed after it; no other process over 3 GB.

## Rejected or deferred

- A #4 tremolo chord joins (TREM_JOIN_TRACKS, held pitches merged across chord changes): deferred to c08 (a new joining rule on the Tremolo row; needs its own pass criterion and a render).
- A #6 celli re-bow refit at 163.877 / 37.377 / basses 166.01: deferred (fit_rebows refits a whole track; do it with the next re-bow change).
- A #6 Flute 2 277/279 portato join (10 dB on both rows): no better option found; left.
- A #6 a2 horns: deferred again (memory: 43 GB with 23 compressed after this render).
- A #1's exclusion of accents from the row trim: not followed (an accent on the row keeps its relation to the Sus notes around it; excluding it would have put Sus accents 4 dB higher over their trimmed neighbours plus the swell).
- B #6 (Trumpet 1 665/670/673 -2 dB trims): replaced by the accent fit (now 2.6/2.8/2.3 dB).
- B #3's Clarinet 1 fit fell short of the simulation (-2.3 dB of -6 at 414/422): to measure in c08.
- C #5 Lento and coda phrase arcs with frozen re-bows: deferred (it moves 74 re-bow rows and their fitted shapes; a cycle of its own with a refit).
- C #4's `(576, 584, 120)` alone would have made a hump (120 -> 123.8 -> 112, the ramp interpolates to the first printed step of 124); the tool change 10 holds 120 instead.

## Open for c08

- Horn 4 repeats (median 2.8 dB) and soft horn breaths (the fall applies only at mf or louder).
- String accents still under later Sus notes: Violins II 4-7 (553, 125, 105, 536, 113), Violas 151/381/349.
- Timpani metric weight: velocity alone gives 0.6 dB; a level step in the volume envelope (kit section 3, `METRIC_DB`) is the next try.
- Trumpet 1 284/285 accents (+6 dB over a sagging legato join before them): fill the join at 283.5 instead.
- Basses minus celli +0.05 s, Horn 4 +0.08 s, Violins II eighths +0.083 s: slightly more lead.
- Tremolo joins (A #4), Lento arcs (C #5).
