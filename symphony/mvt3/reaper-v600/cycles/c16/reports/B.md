# Cycle 16, critic B (balance and levels), on the c15 render

Data: `build/parts.json` (identical to `cycles/c15/rendered_build/parts.json`), `build/mix.json`, the c15 stems and master. Method notes are at the end. "Measured" = from the stems, the master or parts.json; "computed" = from the config with a filter model; "inferred" = my reading.

## Manual notes

Third round, pages chosen for the first priority (where level shaping belongs): May 2021 HO manual PDF p.53-54, 64, 150-151. `loop/MANUAL-GAPS.md` read; it has no item on this subject (proposed addition under finding 1).

| What the manual says (PDF page) | Where it applies here | Does the render follow it |
|---|---|---|
| Lines are shaped with CC envelopes; velocity is for short articulations because it cannot change inside a note (p.53-54) | every sustained line; the staccato quarters inside the first theme, the hammered eighths | Partly. CC11 + CC1 carry 3-5 points/s per track (Violins I 3.1 + 2.0). The track fader carries 9.3-16.3 points/s on the strings, more than the CC lanes. The staccato rows' level inside the theme is set by fader steps (`level_default`), not by velocity |
| "Volume should be used to set a loudness level relative to other instruments, while Expression should be used to shape the continually changing dynamics ... of each instrument individually" (p.64; the same on p.151: Volume sets "the overall upper limit ... as opposed to shaping an individual musical line") | the volume envelope of all 29 pitched tracks | No. 59 % of the envelope's breakpoints are per-note shapes (table in finding 1). The reason is recorded in BRIEF ("make balance corrections in the volume envelope so CC11 keeps each printed dynamic's timbre"); the per-note fits were then added to the same lane |
| CC11 crossfades the dynamic layers on long instruments, so a level change by CC11 is also a timbre change (p.64, p.151) | the proposal to move layers to CC11 | This is why only corrections of 3 dB or less are candidates for CC11, and why accents stay out of it (closed: the CC11 bump into the top layer was heard as harsh) |
| Velocity maps to recorded dynamic samples on short instruments, e.g. p at 1-25, mp at 26-45 (p.150) | "Stac RRx9" / "Staccatissimo RRx9" notes inside the one-row theme | The violas' staccato row sits 12.0 dB over their "Sus MAX" notes before the level steps in bars 11-26 (measured); a lower velocity would give the softer sample, the fader step only turns the loud sample down |
| Send CC1 and CC11 before the first note (p.151) | pre-roll | Followed (pre-roll values, c06 / c14) |

## 1. The per-note volume automation: what it is, what it does, what to remove (bars 1-279, all tracks; first priority)

**Counts (measured on the envelope `build_reaper.py vol_points` writes; 423.8 s, 9,061 note onsets).** 53,349 points on 29 tracks. Reference projects: 0.01-0.36 points/s on the fader, EastWest's templates none; expert mockups put 7-44 points/s into CC1 / CC11 instead (FINDINGS Parts 1, 4, 6).

| track | points | per s | per note | range inside a note, median / p90 dB | step between successive notes, median / p90 dB | share of fader movement inside notes | notes moving 3 dB or more | of those unmarked |
|---|---|---|---|---|---|---|---|---|
| Violins I | 3934 | 9.3 | 5.7 | 0.7 / 4.4 | 0.5 / 4.1 | 44 % | 140 | 52 |
| Violins II | 3990 | 9.4 | 4.9 | 0.5 / 3.5 | 0.3 / 3.8 | 41 % | 123 | 32 |
| Violas | 4062 | 9.6 | 4.8 | 0.6 / 3.4 | 0.3 / 4.1 | 38 % | 133 | 49 |
| Violoncellos | 4123 | 9.7 | 6.8 | 0.4 / 5.3 | 0.7 / 5.0 | 43 % | 154 | 59 |
| Double basses | 6905 | 16.3 | 10.0 | 3.0 / 6.2 | 1.6 / 4.3 | 27 % | 436 | 298 |
| Flute 1 / 2 | 2108 / 1367 | 5.0 / 3.2 | 4.6 / 4.9 | 0.0 / 4.2 | 0.15 / 3.6 | 70 / 74 % | 104 / 68 | 25 / 15 |
| Oboe 1 / 2 | 2234 / 778 | 5.3 / 1.8 | 6.2 / 7.6 | 1.8 / 5.0 | 0.9 / 3.8 | 63 / 81 % | 143 / 30 | 66 / 4 |
| Cor anglais | 262 | 0.6 | 2.8 | 0.0 / 3.5 | 0.0 / 2.7 | 85 % | 13 | 2 |
| Clarinet 1 / 2 | 2097 / 1244 | 5.0 / 2.9 | 3.4 / 4.2 | 0.0 / 3.5 | 0.0 / 2.2 | 70 / 69 % | 88 / 51 | 18 / 1 |
| Bass clarinet | 466 | 1.1 | 6.2 | 0.0 / 4.0 | 0.0 / 2.8 | 67 % | 17 | 2 |
| Bassoon 1 / 2 | 2110 / 1972 | 5.0 / 4.7 | 4.4 / 8.2 | 0.0 / 3.5 | 0.0 / 2.5 | 82 / 77 % | 92 / 55 | 28 / 4 |
| Contrabassoon | 1146 | 2.7 | 6.6 | 0.0 / 3.5 | 0.0 / 2.9 | 70 % | 29 | 0 |
| Horn 1 / 2 | 1910 / 1010 | 4.5 / 2.4 | 5.4 / 8.7 | 0.0 / 5.8 | 0.7 / 3.5 | 59 / 58 % | 104 / 39 | 52 / 7 |
| Horn 3 / 4 | 1510 / 1126 | 3.6 / 2.7 | 6.6 / 7.4 | 0.0 / 5.5 | 0.2 / 3.4 | 61 / 59 % | 63 / 28 | 22 / 5 |
| Trumpet 1 / 2 / 3 | 1149 / 699 / 912 | 2.7 / 1.7 / 2.2 | 5.8 / 6.9 / 7.9 | 0.1-2.2 / 4.0-4.5 | 0.2-0.7 / 2.8-3.4 | 48-51 % | 39 / 23 / 29 | 13 / 10 / 10 |
| Trombone 1 / 2, Bass trombone | 1278 / 1047 / 1024 | 3.0 / 2.5 / 2.4 | 7.5 / 10.1 / 8.6 | 1.7-2.2 / 4.8-6.3 | 0.2-0.8 / 3.4-3.9 | 51-65 % | 63 / 30 / 42 | 23 / 6 / 18 |
| Tuba | 985 | 2.3 | 7.9 | 2.2 / 4.8 | 0.2 / 2.8 | 50 % | 37 | 18 |
| Timpani | 1796 | 4.2 | 10.0 | 6.0 / 8.7 | 0.5 / 3.7 | 48 % | 153 | 73 |
| Harp | 103 | 0.2 | 0.4 | 0.0 / 0.1 | 0.0 / 0.1 | 21 % | 2 | 0 |

Totals: 2,328 of 9,061 onsets (26 %) move 3 dB or more between their note-on and the next note-on; 912 of them (39 %) carry no accent, sf, hairpin or dynamic. 48 % of all fader movement lies inside single notes (Movement I: 74 %). "Inside the note" includes the last 30 ms, where the next note's step already starts.

**By source rule (measured: every `vol_parts` item of `score_to_parts.py` tagged with its source line and evaluated alone; share of 61,300 breakpoints before gridding).**

| layer | items | share | items of 3 dB or more | kind |
|---|---|---|---|---|
| printed hairpins (`hpgain`) | 431 | 23.2 % | 169 | slow, printed |
| accent swells (`GENTLE_ACCENT`, up to 3.5 dB) | 1038 | 18.7 % | 617 | per note, printed |
| `STR_REP_DETACH` dips and `beat_gap_db` (basses, celli) | 493 | 7.4 % | 493 | per note, unprinted |
| roles | 245 | 6.5 % | 168 | slow |
| `UNI_BOOST` (+3.0 dB per doubled player on the kept unison note) | 579 | 6.5 % | 579 | per note, unprinted |
| pitch trims | 373 | 6.0 % | 352 | per note, unprinted |
| metric steps (`METRIC_BOWED_DB`, timpani) | 365 | 5.1 % | 34 | per note, unprinted |
| timpani attack / settle / roll shapes | 187 | 4.6 % | 180 | Dan's roll rule |
| held decrescendos | 96 | 3.4 % | 96 | printed |
| `ROW_TRIM_DB` | 232 | 3.0 % | 156 | per row |
| `LEVEL_SHAPES_S` (fronts, notches) | 171 | 2.5 % | 130 | per note |
| re-bow fills | 24 lists | 2.4 % | 24 | per re-bow |
| divisi chord cuts | 5 | 2.3 % | 5 | printed |
| `STEADY_LINE` level steps (c15) | 5 lists, 506 rows | 2.0 % | 5 | per note |
| slur pair release, note trims, `WIND_DETACH`, level shapes, arrival weight | 407 | 5.9 % | 233 | per note |

Slow or printed layers: 41 % of the breakpoints; per-note layers: 59 %. The layer that causes the largest swing in each note moving 3 dB or more: accent 504, repeat dips 313, pitch trims 233, `UNI_BOOST` 199, roles 175, hairpins 168, timpani shapes 153, `WIND_DETACH` 124, row trims 80, steady levels 77, fronts 72, held decrescendos 62. For the 912 unmarked notes: repeat dips 225, pitch trims 164, `UNI_BOOST` 133, `WIND_DETACH` 73, timpani 73, steady levels 68, row trims 60.

**The answer for Dan (measured, except where marked).**
1. The fader lane is where the pipeline puts every level correction, because in this library CC11 changes the timbre layer together with the level. The samples differ in level from pitch to pitch and from row to row, and each cycle fitted another per-note correction on top. That is the reason for the peaks and valleys.
2. 35 % of the points say nothing: the writer samples every ramp on a 1/32-note grid. Dropping points that lie within 0.1 dB of the line between their neighbours leaves 34,598 of 53,349 with the same curve.
3. Layers stack on the same note and partly cancel. On the first theme's accented halves a +3 dB front (`LEVEL_SHAPES_S`) sits on a fitted steady level of -3.5 to -6.8 dB (Violins I 40: -6.8, 44: -6.2, 46: -5.3).
4. Balance does not depend on the per-note layers: with all of them removed each stem's whole-movement level changes by 0.0-1.25 dB, except Horn 1 -2.4, Horn 2 -1.5, Trumpet 1 -1.5 (`UNI_BOOST`) and Harp +1.65 dB (48 note trims that are one role).

**What the per-note layers do to the lines (measured: stem RMS over the first 0.35 s of each note, or the note's slot if shorter; "without" = the same minus the mean of the per-note layers over that window; median step between successive notes, and SD of the note levels).**

| passage, track | notes | step with / without | SD with / without | verdict |
|---|---|---|---|---|
| F1 11-26 Violins I | 59 | 1.88 / 1.85 | 2.4 / 2.8 | nothing |
| F1 11-26 Violins II | 59 | 1.60 / 1.18 | 2.0 / 2.3 | hurts the step |
| F1 11-26 Violas | 79 | 1.91 / 1.36 | 3.6 / 6.4 | row level helps, per-note steps hurt |
| F1 151-170 Violins I / II / Violas | 77 / 105 / 67 | 1.47 / 1.49, 1.62 / 1.16, 1.75 / 2.05 | 5.1 / 4.9, 3.8 / 4.4, 5.9 / 6.6 | nothing, hurts, helps |
| F1 11-26 and 151-170 Horn 1 | 59 / 61 | 2.16 / 2.30, 2.84 / 2.23 | 3.0 / 2.6, 3.6 / 2.9 | `UNI_BOOST` hurts in the recap |
| counterstatement 27-34 Violoncellos | 30 | 2.21 / 3.43 | 1.9 / 4.2 | helps |
| counterstatement 27-34 Double basses | 30 | 1.15 / 2.52 | 1.5 / 4.2 | helps |
| counterstatement 27-34 Bassoon 1 / Tuba | 30 / 23 | 2.77 / 1.68, 2.32 / 1.48 | 3.4 / 2.7, 3.3 / 3.2 | hurts (`UNI_BOOST`; accents and detach dips, printed) |
| F2 67-82 Violins I / II / Violoncellos | 48 / 48 / 44 | 1.17 / 1.20, 2.00 / 1.87, 2.49 / 2.49 | | nothing (few layers there) |
| F2 187-198 Violins I / II | 31 / 31 | 2.60 / 2.30, 1.43 / 1.43 | | nothing |
| Trumpet 1 solo 51-66 | 41 | 1.68 / 1.68 | | no per-note layer |
| muted Trumpet 1 171-186 | 24 | 1.88 / 3.20 | 3.3 / 3.8 | level shapes help |
| Cor anglais 171-186; Flute 1, Clarinet 1 43-50 | 41; 11, 11 | equal | | no per-note layer |
| Bassoon 1 solo 115-122 | 20 | 1.56 / 1.80 | 1.9 / 2.2 | shapes help a little |
| codetta 91-98 Trumpet 1 / 2, Trombone 1 | 9 each | 3.34 / 2.35, 3.42 / 1.70, 3.19 / 0.95 | | printed accents: the steps are the accents |
| hammered 199-210 Violins I / II / Violas / Violoncellos | 61 / 66 / 45 / 35 | 2.40 / 1.85, 1.96 / 1.84, 3.66 / 2.56, 2.15 / 2.05 | | hurt slightly (accents printed; row trims do nothing: Violas 3.66 with or without them) |
| Più allegro 247-270 Violins I / II / Violas / Violoncellos | 80 / 115 / 87 / 73 | 1.99 / 1.51, 1.75 / 1.74, 1.46 / 1.77, 2.80 / 2.58 | | mixed, all within 0.5 dB |
| Più allegro Horn 1 / Trombone 1 | 45 / 41 | 1.62 / 1.33, 2.19 / 1.62 | | `UNI_BOOST` hurts |
| chorale 223-234 Trombone 1 | 12 | 1.45 / 0.72 | 4.1 / 3.8 | `UNI_BOOST` hurts; the other six brass tracks carry no per-note layer there |
| Timpani 199-210 / 247-270 | 16 / 41 | 2.12 / 3.51, 2.48 / 3.35 | | metric steps help |

Double basses' repeated eighths (792-840, 984-1108), body over the first 55 % of the slot against the lowest 20 ms of the gap: separation 6.5-9.1 dB with the dips, 0.2-4.9 dB without (five sub-spans, 295 repeats). The dips are needed (S1). The metric steps on the basses give a median 6.2 dB alternation between successive eighths in 1088-1108 (1.5 dB without them) and 5.6 dB in 1056-1088 (4.4 without).

One level per row or a cap instead of per-note steady levels (computed from the same stems): with every steady level limited to 3 dB either side of the span's median, the violins' steps are 1.69 / 1.44 (bars 11-26) and 1.20 / 1.44 (151-170), better than the current 1.88 / 1.60 / 1.47 / 1.62, with SD within 0.3 dB. Celli and basses 27-34 keep their steps (2.18 and 1.46 against 2.21 and 1.15) and lose 0.6 / 0.9 dB of SD. The violas in bars 11-26 need the row offset first: their staccato row is 12.0 dB over "Sus MAX" before the steps.

**Fix for the actor (range-test "per-note layers off", "capped at 3 dB" and the current state on 37-138, 598-682, 838-894, 984-1110; `tools/score_to_parts.py`, `build/score_config.py`, `tools/build_reaper.py`).**
- Add `VOL_PER_NOTE` = "on" / "cap3" / "off" in `score_to_parts.py` acting on the per-note groups only (steady levels, `LEVEL_SHAPES_S` fronts on the theme, pitch trims, `UNI_BOOST`, row trims, metric, note trims), so the three states can be rendered from one config. Expected from the stems: "off" hurts the celli / basses in 27-34 (step 2.2 -> 3.4, 1.15 -> 2.5), the violas' row level (SD 3.6 -> 6.4), the basses' separation (to 0.2-4.9 dB), the muted trumpet (1.9 -> 3.2) and the timpani (2.1 -> 3.5); it helps Violins II in the theme (1.60 -> 1.18), Bassoon 1 27-34, Horn 1 151-170 and Trombone 1 in the chorale. "cap3" should keep all of the first group within 0.3 dB of step.
- Remove: the +3 dB fronts on the theme's accented halves where a negative steady level sits under them (fold both into one value per note, then cap); the harp's 48 note trims of -6 dB at 488-511.5 (replace by one `roles.json` row `[488, 512, -6]`); Double basses' pitch trims E2 / F2 / E flat 2 / F1 once the EQ bells of finding 3 are changed.
- Cap at 3 dB around the span's median: `steady_levels.json` (Violins I 27 of 136 rows are outside, Violins II 10 of 164, Violas 38 of 146, Violoncellos 13 of 30, Double basses 12 of 30); the basses' metric table in 1056-1108 (sum of "down" and "off" 3 dB at most).
- Move to velocity: the staccato-row offsets inside the theme spans (`level_default` for "Stac RRx9" / "Staccatissimo RRx9"; Violas need about -12 dB in bars 11-26, Violins I -3.3, celli and basses -5): set these notes' velocity so the row is within 3 dB of "Sus MAX" before any fader step (manual p.53, p.150; FINDINGS batch 2: shorts by velocity).
- One level per note on notes of an eighth or less: already the case for steady levels and pitch trims (steps); keep it so, no shape inside those notes except the basses' gap dips.
- Keep: accent swells (printed, 3.5 dB at most, Dan's rule 4), the basses' and celli's repeat dips, re-bow fills, timpani shapes and metric steps, the muted trumpet's and the bassoon solo's level shapes, hairpins, held decrescendos, roles, divisi cuts.
- `build_reaper.py vol_points`: drop collinear points (tolerance 0.1 dB, checked in the envelope's own scaling) before writing. 53,349 -> about 34,600 points, same sound. This also makes the lane readable in REAPER.
- `loop/MANUAL-GAPS.md`: add an item "level shaping of sustained lines belongs in CC11 / CC1, relative level in the fader (p.64, p.151)" with this table as its measured state.

## 2. Level steps keyed to a led note-on cut or lift the end of the note before (one-row theme, bars 11-34 and 151-170)

Where: `STEADY_LINE` `level_db` and pitch-trim steps start 0.03 s before the moved note-on; slurred notes lead by 41-96 ms (Violins I 59-74, Violins II 60-84, Violas 54-96, Violoncellos 65, Double basses 41 ms), and the old note sounds through the lead.

Measured on 284 slurred joins of the five tracks (dip = mean of the two bodies minus the lowest 20 ms within -0.06..+0.14 s of the note-on; the "lead window" is the stem level from the moved note-on to the score onset against the old note's body; "without" = the per-note layers taken out of the stem):

| step at the join | joins | dip with / without | lead window with / without |
|---|---|---|---|
| down 3 dB or more: Violins I / II, Violas, Double basses | 4 / 6 / 7 / 4 | 8.0 / 6.5, 7.4 / 4.7, 6.7 / 4.5, 6.1 / 3.6 dB | -4.2 / +0.8, -1.1 / +3.3, -3.5 / +1.0, -2.4 / +2.2 dB |
| within 1.5 dB (all five tracks) | 160 | 2.8-5.3 / 3.1-6.0 | +0.8..+1.4 / +0.8..+1.6 |
| up 3 dB or more: Violins I / II, Violas, Violoncellos, Double basses | 7 / 7 / 4 / 8 / 4 | 3.7 / 5.2, 4.4 / 6.0, -0.5 / 0.3, 2.4 / 6.3, 5.7 / 8.9 | +4.1 / +0.2, +2.6 / -1.3, +5.9 / +2.0, +3.4 / -0.7, +3.8 / -0.6 |

At the 21 steps down, 15 joins dip more than 6 dB with the envelope and 6 without it. At steps up the old note's last 40-96 ms is lifted 2.6-5.9 dB. Worst: Violoncellos 113.5 (step -14 dB, dip 17.0 against 7.1), Violins II 651 (10.1 / 6.0), Violas 78 (10.6 / 8.0), Violins I 42 (10.1 / 6.8) and 97.5 (10.1 / 7.8). This is Movement I's finding (join holes 9.0 with, 4.7 without) at a smaller size, because most steps are small.

Fix (`tools/score_to_parts.py`, the `level_db` block near line 5245 and the pitch-trim step near 4947): for a note whose class lead is 0.03 s or more, start the step 0.015 s before the note's score onset and reach it 0.015 s after (a 30 ms crossfade on the measured attack centre) instead of 0.03 / 0.008 s before the moved note-on. Entries after rests and new bows keep the current timing (nothing sounds before them). With the 3 dB cap of finding 1 the largest step at a join becomes 6 dB. Check on the range render: lead window within 1.5 dB of the old body on all 53 joins with steps of 3 dB or more, dips over 6 dB 15 -> 6 or fewer.

## 3. "Mushy": the bottom octave is 5-11 dB under the Brahms spectra, and the basses' EQ bells put it there (whole movement; `build/mix.json` Double basses)

**Every low EQ band (read from mix.json) and its summed gain at the bass fundamentals (computed with peaking-filter models of ReaEQ's bells; soft passages / inside the `loud_eq` spans).**

| track | bands | C1 32.7 | G1 49 | B1 61.7 | C2 65.4 | D2 73.4 | E flat 2 | E2 | F2 87.3 | G2 98 | A flat 2 | C3 131 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Double basses | `eq` 150 Hz +4 (1 oct), 87.3 Hz -12 (0.15 oct); `mute_eq` (static) 61.7 Hz -5, 73.4 Hz -4 (0.12 oct); `loud_eq` 160 Hz +3, 98 Hz -4 (0.5 oct); `family_eq` HP 35, 240 Hz -3, 456 -2.2 | -3.7 | -1.2 / -1.3 | -5.8 / -6.0 | -2.7 / -3.0 | -5.4 / -6.0 | -3.6 / -4.5 | -5.6 / -7.0 | -11.8 / -13.8 | -1.6 / -4.6 | -0.2 / -2.6 | +2.0 / +3.1 |
| Violoncellos | `eq` 170 Hz +3 (1.5 oct), 125 Hz +3; `loud_eq` 150 Hz +3; `family_eq` HP 53 | -8.7 | -3.1 | -0.8 | -0.4 / 0.0 | +0.6 / +1.1 | +1.0 / +1.6 | +1.5 / +2.2 | +2.0 / +2.8 | +3.0 / +4.2 | +3.6 / +5.0 | +5.2 / +7.8 |
| Tuba | `eq` 84 Hz -5 (0.2 oct); `loud_eq` 140 Hz +2; `family_eq` HP 41, 143 Hz -4.3 (1.39 oct) | -5.7 | -2.5 | -2.2 | -2.4 / -2.1 | -3.2 | -4.6 | -7.2 / -6.6 | -6.6 / -5.9 | -4.3 / -3.3 | -4.3 / -3.1 | -5.4 / -3.5 |
| Contrabassoon | `eq` low shelf 70 Hz -4; `loud_eq` 140 Hz +2 | -3.8 | -3.2 | -2.5 | -2.3 / -2.0 | -1.9 | -1.7 | -1.5 | -1.3 | -1.0 / 0.0 | -0.8 | -0.6 / +1.4 |
| Bass trombone | `loud_eq` 140 Hz +2; `family_eq` HP 41 | -5.5 | -1.9 | -1.0 | -0.9 | -0.8 | -0.7 | -0.7 | -0.7 | -0.7 / +0.2 | -0.8 | -1.1 / +0.8 |
| Bass clarinet | HP 30 | -2.3 | -0.6 | -0.3 | -0.2 | | | | | | | |
| Timpani | `family_eq` HP 44, 385 Hz -6 (2.54 oct) | -6.5 | -2.6 | -1.6 | -1.5 | -1.4 | -1.4 | -1.4 | -1.4 | -1.6 | -1.7 | -2.3 |
| Bass drum | HP 25 | -1.3 | -0.3 | | | | | | | | | |

The basses' most-sounded pitches (parts.json, seconds; in brackets at f or louder): C2 66 (46), G1 40 (27), B flat 1 33, D2 30 (20), A flat 1 30, B1 24, E flat 2 21, F2 21 (19). So the tonic C2 is cut 3 dB, its neighbours B1 and D2 5-6 dB (bells copied from Movement I, whose key they fit), F2 12-14 dB, and G1's second harmonic (98 Hz) 4.6 dB in the loud spans, while 130-160 Hz is raised 2-4.5 dB on the basses and 5-8 dB on the celli. The four bass pitch trims of c12 (E2 +6, F2 / E flat 2 / F1 +3) are the pitches whose fundamental or second harmonic lies in the 87.3 Hz bell: the trim raises the whole note to make up for a cut of its fundamental, which moves that note's energy to its overtones.

**Shares of total energy, master, dB (measured; Brahms figures from the third-octave tables in `symphony/render/critics/c00` and `c04`, whole movements; Brahms 1/i is in C minor like this finale).**

| | 56-71 Hz (C2) | 71-89 Hz | 89-112 Hz (G2) | 56-112 Hz | 112-140 Hz | 140-355 Hz |
|---|---|---|---|---|---|---|
| Brahms 1/i | -12.3 | -16.8 | -10.7 | -7.8 | -11.8 | -9.1 |
| Brahms 4/i | -12.7 | -13.2 | -13.5 | -8.3 | -11.2 | -8.2 |
| Brahms 1/ii, 4/ii | | | | -7.9, -7.3 | | -9.1, -8.5 |
| c15 whole | -22.7 | -24.9 | -15.7 | -14.5 | -15.7 | -6.7 |
| soft: transition 43-50 / trumpet solo 51-66 / F2 67-82 / F2 171-198 | -23.2 / -26.8 / -23.4 / -20.8 | | | -22.2 / -16.4 / -14.2 / -10.3 | | -5.2 / -5.4 / -5.9 / -7.0 |
| loud: counterstatement 27-34 / recap 151-170 / coda 199-210 | -29.4 / -22.9 / -28.6 | -21.4 / -21.4 / -23.2 | -17.3 / -13.6 / -16.7 | -15.7 / -12.5 / -15.6 | | -4.8 / -5.2 / -5.8 |
| loud: chorale 223-234 / Più allegro 247-270 / end 271-279 | -20.2 / -22.8 / -21.5 | -33.5 / -24.7 / -32.3 | -20.4 / -15.4 / -23.7 | -17.2 / -14.2 / -19.3 | | -8.1 / -6.4 / -7.4 |

The whole movement is 6.7 dB short at 56-112 Hz (10.4 dB in the C2 band) and 2.4 dB over at 140-355 Hz; the two fff climaxes are 9-11 dB short at 56-112 Hz. The Double basses supply 53 % of the master's 56-112 Hz (58-95 % in the passages above), the celli 27 %, timpani 8 %, tuba 3 %, contrabassoon 1 %. Below 56 Hz the master (-28.4 dB) matches the recordings (about -29.5): nothing to add there.

**Fix, simulated on the c15 stems (per-bin gain on the stem's spectrum inside and outside the `loud_eq` spans, summed back into the master).**

`build/mix.json` "Double basses":
- `mute_eq`: delete both bells (61.7 Hz -5, 73.4 Hz -4).
- `eq` `bell2` 87.3 Hz: -12 -> -4 dB (0.15 oct). `build/pitch_trims.json` Double basses: 40 (E2) +6 -> +2, 41 (F2) / 39 (E flat 2) / 29 (F1) +3 -> 0, then refit on the range render (the c12 method: the four pitches against C2 / G1 / A flat 1 at the same CC11, within 3 dB).
- `loud_eq`: delete both bands (98 Hz -4, 160 Hz +3).
- `eq` `bell` 150 Hz +4 -> a bell at 72 Hz +4 dB, 1.5 oct.

| | 56-71 | 71-89 | 89-112 | 56-112 | 140-355 | master level |
|---|---|---|---|---|---|---|
| whole: c15 -> bells only -> with the 72 Hz bell | -22.7 -> -19.9 -> -16.6 | -24.8 -> -20.6 -> -17.7 | -15.6 -> -14.5 -> -13.3 | -14.4 -> -12.6 -> -10.7 | -6.6 -> -6.9 -> -7.0 | +0.17 dB |
| F1 11-26 | | | | -10.4 -> -8.2 | -5.5 -> -5.9 | +0.25 |
| counterstatement 27-34 | | | | -15.6 -> -10.0 | -4.9 -> -5.6 | +0.09 |
| trumpet solo 51-66 / F2 67-82 | | | | -16.4 -> -11.5, -14.2 -> -10.9 | | +0.2 |
| recap 151-170 | | | | -12.6 -> -7.7 | -5.2 -> -6.0 | +0.46 |
| F2 171-198 | | | | -10.6 -> -8.1 | | +0.30 |
| chorale 223-234 / Più allegro / end 271-279 | | | | -17.2 -> -12.9, -14.2 -> -11.3, -19.3 -> -14.3 | -8.1 -> -8.5, -6.5 -> -6.8, -7.4 -> -7.6 | +0.1 |

The basses' stem rises 2.4 dB overall. With the 72 Hz bell at +6 the recap and bars 171-198 pass the Brahms figure (-6.5, -6.9): stay at +4. Tuba (`eq` 84 Hz -5 -> -2) and Contrabassoon (shelf off) change every figure by 0.1 dB or less: leave them. Removing the celli's `loud_eq` bell takes 0.1-0.4 dB off 140-355 Hz in the loud spans and 0.9 dB off the celli stem: optional. Conditions on the render: 56-112 Hz whole movement -11.5 dB or higher and no passage above -7.5; 28-56 Hz no higher than -26 (it goes -28.3 -> -26.0; the delivery chain's 42 Hz high pass stays); sample peak under 0.95; the bars-255-256 bass level of c12 (closed) re-measured; basses' note levels on E2 / F2 within 3 dB of C2. The 315 Hz hump is closed and not touched here.

## 4. `UNI_BOOST` switches a line's level by 3 dB from note to note (Horn 1, Horn 3, Bassoon 1, Oboe 1, Trombone 1, Clarinet 1, Trumpet 1; 579 notes)

Where: when two tracks on the same patch play a unison, one note is dropped and the kept one gets +10·log10(players) dB for that note only (`tools/score_to_parts.py` line 6634, applied at line 5774 with a 0.02 qn ramp). Where the second player doubles only some notes of a line, the line jumps by 3 dB on those notes.

Measured: it is the largest cause of in-note 3 dB moves on Horn 1 (63 notes, 43 unmarked), Horn 3 (30 / 20), Bassoon 1 (20 / 17), Clarinet 1 (12 / 12). Step medians with / without this layer alone: Horn 1 recap 2.84 / 2.39 and Più allegro 1.62 / 1.33, Bassoon 1 bars 27-34 2.77 / 2.52, Oboe 1 bars 11-26 2.59 / 2.25, Trombone 1 chorale 1.45 / 0.72 and Più allegro 2.19 / 1.89, Horn 3 chorale 4.15 / 3.09. It makes the line less even in all seven cases. It carries balance: Horn 1's stem is 2.4 dB lower without it, Horn 2 1.5, Trumpet 1 1.5, Horn 3 1.2.

Fix (`tools/score_to_parts.py`, a new option `UNI_BOOST_HOLD_QN`, default None; Finale value 2.0 in `build/score_config.py`): hold the boost across unboosted notes when the next boosted note of the track starts within 2 qn, and ramp it in and out over 0.25 qn in rests or at phrase ends, so a doubled phrase has one level. Isolated boosted notes shorter than 0.5 qn get half the boost. Expected: the 199 in-note swings from this layer fall to the phrase edges, the seven step medians reach their "without" values within 0.2 dB, and the stems keep their level within 0.5 dB (inferred from the share of boosted notes; check Horn 1 against Violins I in 600-664, now Horn 1 -33.9 / Violins I -36.1 dBFS plain RMS in bars 151-154).

## 5. The four stops that are too dry (bars 2, 6, 113, 166): what restores 14-17 dB

Measured on the stems at each cut-off (0.3 s before against 0.26-0.34 s after): the dry stems fall 26.0-29.2 dB, the four returns 13.7-13.9 dB, and before the stop the returns sit 11.5-12.7 dB under the dry sum (9.3 dB at bar 94, which measures 15.6). The tail at +0.3 s is half returns and half dry releases.

- Bars 2 and 6: the largest dry part of the tail is the Violoncellos (-53.0 / -53.5 dBFS), which still carry the -4 dB release fade of c13 / c15. Delete the fades: `build/score_config.py` `POST_SHAPES_S` rows at 5.0 and 21.0 on Violoncellos and Double basses (keep 374.0). Computed from the stems: the tail rises 1.3 dB, the drops go 17.4 -> about 16.1 and 18.0 -> about 16.7 dB. (c15's -5 -> -4 moved bar 2 by 0.3 dB, which fits the same sum.)
- Bar 166 (chord at 660, cut at 662.6): the tail is R Strings -55.7, R Winds -58.9, Timpani -59.6, Violas -60.0, Double basses -61.4. First try the data that measured 14.9 in c14: take the chord at 660 out of the `STEADY_LINE` spans on Violins I / II and Violas (end the spans at 660), so it plays on its c14 row with its c14 end; the notes before it stay on one row. If the range render still reads over 17: a ride on the return faders (next item), R Strings and R Winds +2.5 dB over 659.8-664 (computed: tail +1.45 dB, 18.1 -> about 16.6).
- Bar 113 (half-note tutti at 448, cut at 450): the returns are 12.7 dB under the dry sum because trombones, tuba, bassoons, contrabassoon and basses have no send; the dry sum falls 29.2 dB. No per-note setting reaches this. Add `return_rides` to mix.json and `build_reaper.py` `returns_job` (a volume envelope on a return track, rows `[qn, dB]`): all four returns 0 dB at 447.5, +5 dB from 448 to 451.5, 0 dB at 453. Computed: tail +3.8 dB, 20.5 -> about 16.7 dB. The ride starts with the chord, so nothing steps under a sounding tail.
- Limits to re-check after these: every stop 14-17 dB at +0.3 s, tutti -20 dB in 0.50 s or less, RT60 1.5 s or less (the ceiling is untouched: no send or return level changes outside the two rides).

## 6. Smaller level items

- Crescendos on their own stem (measured, last quarter minus first quarter of each printed crescendo of 1.5 qn or more with the track sounding 60 % of it): 59 of 390 do not rise 1 dB; in 20 of them the envelope falls 1 dB or more. Clearest: Clarinet 1 / 2 over 1032-1048 (bars 259-262, crescendo to the fff of 263): stems -3.5 / -5.4 dB while the envelope falls 3.2 / 4.7 dB, because `dyn_trim_db` fff is -4 / -6 against ff 0. Fix: mix.json Clarinet 1 fff -4 -> -2, Clarinet 2 -6 -> -3, with ff -1 / -1.5 so the fff level stays (c03 set these against the other woodwinds at fff). The master still rises there (bars 259-263: -19.9, -20.4, -19.5, -17.6, -16.8), so this is a detail.
- Double basses' metric steps in 1088-1108 (bars 273-277): 6.2 dB median alternation between successive eighths (finding 1). `METRIC_BOWED_DB_SPANS["Double basses"]` for that span: "down" and "off" no more than 3 dB apart.
- Muted Trumpet 1 with the cor anglais, bars 171-186 (measured, A-weighted stems): Cor anglais -50.4 / -49.2, Trumpet 1 -55.5 / -54.0, Clarinet 2 -57.6: the trumpet is 5 dB under the instrument it doubles and 2-4 dB over the accompaniment. Its per-bar roles are protected; if Dan finds the colour missing, +2 dB on the whole span is the change. No fix asked now.

## Checked and in order (measured)

Trumpet 1 solo 51-66: 10.4 dB over the next stem (A-weighted). Violins' F2 67-82: Violins I -40.8, II -43.6, celli counter-melody -48.6, harp -49.2. Bassoon solo 115-118: 10 dB over the next stem; Clarinet 1's pp is 4.3 dB under it in 119-122. Theme in the bass 27-34: Horn 3, tuba, basses, bass clarinet, celli and bassoons (-33.1 to -38.7 plain RMS) against the violins' countersubject -38.5. Trumpets' theme B 211-218: Trumpet 1 / 2 -31.3 / -32.4, next stem -38.0. Arrival 223: master by half bar from 880: -29.8, -24.4, -22.3, -20.0, then -15.8 at 888 (no dip at 884); crash -33.8 against the top stem -29.9 (263: -32.4 against -26.2; 278: -33.9); bass drum 8 % of 30-150 Hz. Timpani: never above rank 9 among the stems in any roll, 6-19 % of 30-150 Hz in the rolls of 147-150, 209-210, 219-222, 243-246, 273-279. Bars 271-279 master: -23.6, -21.8, -21.2, -21.6, -22.0, -20.7, -18.4, -16.6.

**Do not touch:** the accent swells (3.5 dB at most); the basses' and celli's repeat dips and `beat_gap_db` (separation 6.5-9.1 dB); the re-bow fills; the timpani attack / settle / roll shapes and metric steps; Trumpet 1's shapes in 680-744 and Bassoon 1's solo shapes; the one-row theme spans and their leads (only the level steps' size and timing change, and the chord at 660 if the bar 166 test needs it); the bar 222 fronts; the crash and bass-drum strokes; the solo roles and sends; the hall sends and return levels outside the two rides; the 315 Hz bells; the delivery chain.

## Method notes

- Source breakdown: a scratch copy of `tools/score_to_parts.py` with a list subclass that records the source line of every `vol_parts.append`; its parts.json is byte-identical to `build/parts.json`. Envelope points: `build_reaper.py vol_points` executed without REAPER (code above the job section only).
- "Marked" = an accent, sf / sfz / fp / sfp or dynamic on the note's score onset, or a hairpin overlapping the note, on any of the track's staves.
- "Without" levels subtract the layer's mean over the measurement window from the stem level, valid because the envelope is a gain after the instrument. Sends are post-fader, so the returns follow the same gain; return stems were not corrected (they are 9-13 dB under the dry stems).
- EQ gains are computed with standard peaking / shelf / 12 dB-per-octave models; ReaEQ's own curves can differ by about 1 dB on the 0.12-0.15 octave bells. The simulation applies gain per frequency bin to each stem's energy spectrum and adds it to the master's (stems treated as uncorrelated).
- The Brahms recordings are not on this disk; their third-octave tables are (whole movements), so soft and loud passages of the mockup are compared with whole-movement reference figures.
