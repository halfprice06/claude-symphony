# Cycle 56: changes (actor)

Render: `cycles/c56/render/` (main pass, then pass 2; Cor anglais, Horn 3, Trumpet 2 and Violoncellos carry a level fix,
originals in `render_first/`). Delivered: `cycles/c56/mvt1-mockup-c56.mp3`. Data as rendered: `cycles/c56/rendered_build/`;
`build/` is that plus four `NOTE_LEVEL` skip rows, which are in REAPER too (written after the render, guard 0 stale).
Nobody listened. Every figure is measured on the stems or simulated; simulated figures are marked.

## Priority 1: the per-note track volume envelope (Dan, 2026-11-11)

### Before / after, all tracks (per track: `cycles/c56/envelope_table.md`; `actor_scripts/count56.py`, `interior56.py`)

| | c55 | c56 | aim |
|---|---|---|---|
| envelope points written to REAPER, all tracks | 52200 | 32612 | |
| points per second, Violins I / Violins II / Violas / celli / basses | 9.0 / 10.5 / 11.3 / 14.3 / 12.9 | 5.0 / 6.4 / 7.6 / 9.6 / 7.9 | |
| notes with 3 dB or more inside, critic C's window (moved note-on to note end; includes the step to the next note) | 2334 of 5282 | 2129 | 1167 or fewer: **not met** |
| the same, 6 dB or more | 931 | 793 | |
| share of the 3 dB notes with no marking | 45 % | 45 % | |
| notes with 3 dB or more strictly inside the sounding note (30 ms in from the onset and from the next onset) | 1331 of 5051 | 1054 | |
| the same, 6 dB or more / notes of an eighth or shorter with 3 dB | 513 / 134 | 386 / 94 | |
| Violins I bars 15-16: points, range | 78, -4.7..+6.5 dB | 44, -4.1..+6.5 dB (`ab/envelope_violins1_bars15-16.txt`) | |

The count was not halved. What is left, by rule (notes with 3 dB or more strictly inside, strings / winds / brass):
the one-level-per-note layer's kept shapes (capped accent swells, join fills, crescendo fronts) 168 / 205 / 27; config
level shapes on marked notes or over several notes 117 / 44 / 59; repeated-note dips 83 strings; the theme's body lifts
64; re-bow fills 51; join notches 18 / 9 / 10; plus hairpin gain and the dynamic trim. The largest part of critic C's
count is the level step between two notes, which that window counts inside one of them.

### What was changed
a. `NOTE_LEVEL` (new generic pass in `tools/score_to_parts.py`, values in `build/score_config.py`): every rule that
   writes into the volume envelope now carries its name (`vol_parts.tag`). Level layers (pitch trims, note trims, metric
   steps, row trims, pickup lifts, the theme's level steps, phrase tops) become ONE value per onset: the mean of what the
   note carried in c55, held to the next onset, no return to 0 between the notes of a run. Shapes inside a note (accent
   swells and bodies, join fills, crescendo fronts, syncopation, pair release, tenuto weight) stay on notes longer than
   an eighth, scaled down where they exceed 6 dB in one note, and are folded into the level on notes of an eighth or
   shorter. A config level shape inside one unmarked note becomes that note's level (1d). Slow layers pass unchanged.
b. Where the level changes: a led note (legato target, one-row line) changes over 40 ms centred on its SCORE onset when
   the note before still sounds (critic A #1); other notes, and every entry after a rest, change 30..8 ms before the
   moved note-on. The theme's body and tail lifts end -20..+20 ms around the next score onset (`body_end_score`).
c. Accents: `ACCENT_SWELL_CAP_DB` 3, `ACCENT_SHAPE_MAX_DB` 6 (the body cut gives way); `build/accent_fits.json`
   refitted as residuals on the simulated stems (`accrefit56.py`): 83 swells lowered, fitted accents more than 5 dB over
   their neighbours' fronts 51 -> 20 of 273 (the 20 stand out with no swell at all). `ACCENT_PLAIN` (swell at most 1.5
   dB, no step trim, no body cut) on Oboe 1 88-104, Clarinet 1 520-536, Horn 1 400-430, Trumpet 1 456-496.
d. `EARLY_FILL_CAP` brass 4 dB / 0.15 s.
e. Oboe 1 fills: 90 at 3 dB held 0.12 s, 95 and 99 held 0.12 s. Final chord: the re-bow fills of Violas and Violins II
   from qn 716 lowered by the stem's excess over the level before and after each re-bow (`rebowres56.py`; a plain +4 dB
   cap was simulated first and left holes of 6-10 dB): bumps of 3-8 dB -> 0-2 dB (simulated; the final chord of the
   render was not re-measured).
f. `ENV_THIN` (new in `tools/build_reaper.py vol_points`): ramp points within 0.1 dB of the line between the kept points
   are dropped (largest difference against every point written: 0.11 dB; kept points at most 2 dB and 4 qn apart).
   REAPER interpolates in its own envelope scale; no difference showed between simulation and render on any line.

### Decided by simulation, with the result
- Repeated-note dips (`str_rep_dips`, `detach_dips`) kept: with the dip's own envelope taken out of the c55 stems the
  separation between repeated notes falls from 5.5 / 7.0 / 7.3 / 4.6 dB to 3.6 / 3.0 / 4.8 / 2.1 dB (basses, Violas,
  Violins II, celli; medians); only 59 of 251 string dips stay 6 dB apart without it. No range render was needed
  (level only). They are 431 of the notes that still count.
- One common level for the theme's eighths (variant T) not shipped: Violins I 56-90 body step 1.8 -> 2.2 dB (per-note
  1.9), celli 520-536 3.0 -> 2.7 (per-note 2.2). `C56_COMMON=1` builds it.
- Smoothing the per-note levels over a run (2 s window) not shipped: 8-13 of 21 lines read a larger step.
- Spans left as built because one level per note read worse: Violins II 104-128 and 552-576, Bassoon 1 520-536
  (simulated); Cor anglais, Horn 3, Trumpet 2 (whole track) and celli 184-244 (on the render; applied with
  `tools/stem_fix.py 56 cycles/c56/rendered_build build --apply` and written into REAPER).

### Note-to-note step on the render, c55 -> c56 (`realcmp_final.txt`; body 0.05-0.35 s / front, median dB)
Violins I 56-90 1.8 -> 1.9 / 1.7 -> 1.8; 104-128 2.1 -> 1.6 / 1.7 -> 1.4; 304-384 4.4 -> 3.2 / 2.8 -> 2.3; 536-576
1.7 -> 1.4 / 1.8 -> 2.1. Violas 104-128 2.4 -> 2.3 / 2.1 -> 1.8. Celli 584-636 2.6 -> 2.5 / 2.9 -> 2.6. Basses 56-128
2.8 -> 2.6 / 3.1 -> 2.7. Flute 1 88-128 4.0 -> 3.6 / 4.1 -> 2.4. Oboe 1 88-104 3.2 -> 2.0 / 4.2 -> 2.4. Clarinet 1
520-536 4.0 -> 2.6 / 3.1 -> 1.9. Horn 1 400-430 1.3 -> 1.5 / 3.9 -> 2.4. Whole tracks: 28 of 28 within 0.3 dB or
better after the stem fix (Trumpet 2 body 3.7 -> 4.0 is unchanged by the fix and read 3.8 in the simulation).
**Worse by more than 0.3 dB on one measure, left in:** Violins I 128-158 body 3.0 -> 3.4 (front 2.4 -> 1.9, p90 7.7 ->
6.7); celli 520-536 front 2.4 -> 3.1 (body 3.0 -> 2.2, p90 8.1 -> 4.2).

### Theme targets on the render (`theme_final.txt`; c55 scripts)
| | c55 | c56 | target |
|---|---|---|---|
| S Violins I 56-87.9: robust SD / over 40 ms | 9 / 2 | 9 / 1 | 15 or less, at most 2 |
| front minus tail, long notes 56-87.9 / 56-127 | 2.6 / 1.9 dB | 2.0 / 2.0 | under 4 |
| Violins I minus celli 56-88, lower quartile | +4.95 | **+3.56** | +3.9: fails |
| S Violins I 536-576 / Violins II 104-127 / 552-576 | 14 / 2; 16 / 0; 15 / 1 | 12 / 4; 15 / 0; 16 / 1 | |
| S Violas 104-127 | 12 / 2 | 21 / 3 | |
| S celli 520-536 | 24 / 5 | 19 / 6 | still fails |
| join holes over 9 dB: Violins I 56-90 / 536-576 / whole track | 9 / 10 / 66 | 6 / 3 / 49 | |
| bar 138 Violins I minus II at 549, 550 | -0.3, +0.1 | -0.1, +0.3 | within 3 |

The margin over the celli: c55's quarters 86-87 carried a 14 dB jump in the envelope on the release of the note at 86
(the level step went back to 0 while the 15 dB body lift was still up: +24 dB for 0.16 qn); c56 holds the note's level
through the rest, and those two quarters fall 4 and 13 dB. Quarters 66 and 69 fall 2-3 dB with the eighths' levels.
No row was added to win the margin back. No note-on moved in this cycle, so the S changes on Violas 104-127 and
Violins I 536-576 are readings of the moved level steps (scherzo c14: a step on the beat moves S by 60-130 ms), not
timing changes; the range render of bars 15-23 (twice, second kept) read S 9 / 1 and front minus tail 2.0 as the full
render.

## Decision 2: bottom octave
`build/mix.json` Double basses: `mute_eq` (61.7 Hz -6, 73.4 Hz -5) deleted, 87.3 Hz bell -10 -> -4, `loud_eq` kept
(track rebuilt in full). On the render: master 70-112 Hz share -15.0 -> -13.7 (acceptance -14.2), 79 Hz band -25.6 ->
-20.2 (-21.5), 140-355 Hz -6.3 -> -6.3; by passage 0-56 -14.2 -> -10.3, 56-88 -14.3 -> -12.4, 184-244 -18.2 -> -15.3,
584-636 -14.3 -> -12.5, 680-728 -21.1 -> -20.4; bar 84 +1.5 dB (limit 1.8), next bars 111 +1.2, 44 +1.1; sample peak
0.917 -> 0.899. Range render of bars 1-14 (twice): 70-112 Hz -14.2 -> -10.4, bars 2-14 within +0.8 dB (bar 1 of a
range render that starts at qn 0 lacks the timpani's lead-in: not a finding). Single bass pitches were not checked one
by one on the render (scherzo c14's caution): open.
120 Hz +3 dB / 0.8 oct on celli and basses: simulated, **not adopted**: 112-140 Hz share -17.2 -> -15.8 and celli
+0.1..+0.8 dB as required, but bar 84 rises 3.0 dB and bar 3 1.7 dB (limit 1.5). Timpani and tuba untouched.

## Decision 3: dynamics rows (per quarter on the render, dB)
- Violas 72-77: -42.2 -43.1 -43.0 -42.9 -44.5 | -36.1 -> -41.8 -41.5 -40.4 -39.0 -38.5 | -37.8 (ramp row). Pass.
- Horn 1 408-411 and 415: -35.1 -37.0 -37.6 -39.7 ... -37.9 -> -38.5 -35.7 -35.6 -36.4 ... -35.5 (rows on 411 and 415;
  the note at 408 lost its fitted accent). Pass on the rise, 408 itself is 3.4 dB lower.
- Celli 601-603: -37.6 -38.9 -42.1 -> -36.7 -36.1 -37.5. Rise at 602, the arrival 0.8 dB under 601: part.
- Flute 2 480-483: -31.7 -32.2 -38.8 -32.7 -> -31.7 -32.0 -33.7 -31.5. Pass (flat at the ff ceiling).
- Violas 612-616 diminuendo: -50.4 -47.2 -49.3 -45.3 -> -51.6 -50.4 -52.9 -50.4 (ramp row; `soft_decresc_keep` 0 per
  track, new in `vol_points`, gave 0.4-0.7 dB of it). No longer rises; falls 0 dB net: part.
- Clarinets bars 9-12: `dyn_trim_db.f` -4.2 / -3.8 -> -2.5: quarters 42-44 +0.2 +1.1 +1.7 (Clarinet 1), +0.1 +0.8 +1.3.
  Bars 26-32 and 139-142 not checked separately (Clarinet 1 bar 104 +2.1 dB is the largest clarinet bar change).
- Bar 160 over bar 122 (mp3 short-term): -11.3 against -12.0, 0.7 dB as in c55. Order 160 > 122 > 167-170 > 26 kept.

## Decision 4 and the rest
- The three c55 stem-fix rows (celli 159, celli 526, cor anglais 24) are in REAPER (every main track was rebuilt).
- Not done: celli 520-536 S; Horns 3-4 p +2 dB; Horn 1 crescendo-note trim limit (40, 94, 620, 662: a limit inside the
  note needs a step back at the arrival or a lower p trim, neither tested); LEVEL_SHAPES fronts on marked wind and brass
  notes and the 484 horn front; harp levels to velocity; Oboe 1 95-100 straight-line trims.
- Not done from the standing lists: MANUAL-GAPS (none tried this cycle); EW-TEMPLATE-PLAN sections 5, 6, 7, 8, 10 are
  still not applied (section 5's "no per-note bumps in the dynamics lane" is what this cycle moved toward).

## Notes from the other movements, checked here
- Stairs on the 0.125 qn grid: yes (slow layers reach vol_db as 0.25 qn steps); `ENV_THIN` at 0.1 dB removes 38 % of
  the points; 0.3 dB would remove 57 % and was not taken.
- Accent swell timing: here the swell is full 0.03 s after the score onset and gone by 0.40 s (front-weighted); fitted
  accents' fronts stand a median 1.7 dB over their neighbours after the cap. Not the finale's fault.
- `UNI_BOOST`: 178 notes at +3 dB, in runs; only 10 switches between abutting neighbours on all tracks. Left.
- Trims returning to 0 between the notes of a run: present in c55 (pitch trims moved 3 dB or more inside 314 notes,
  row trims 19); `NOTE_LEVEL` holds one level per note to the next onset, so the pattern is gone on every track and span
  outside the skip list.

## Render conditions
- Lock: waiter from 06:01, behind the scherzo and Movement II; held 08:09-09:45 (build 08:09-08:30, range renders to
  08:37, main render to 08:50, pass 2 to 09:29, four tracks and saves to 09:45). Nothing taken by hand.
- State guard: 0 stale at the start, after the build, before and after the main render; pass 2 0 before, 3 after the
  render save (Bassoon 1 stac, Cor anglais stac, Flute 1 stac), rebuilt in full, 0 at quit; main 0 at the last quit.
- Memory: REAPER 41 GB before and 44 GB after the main render, 0 compressed; pass 2 20 GB. Attack probe: late or hole 0.
- State check against c55: one run, Double basses 196-214 +4.4 dB (the removed bells).

## Delivery (`master_eq` and delivery chain unchanged)
-19.7 LUFS integrated, LRA 14.4 LU, true peak -1.7 dBTP, limiter about 0.8 dB, p10-to-max span 18.9 dB, 433.45 s.
Master: -20.8 LUFS, LRA 23.0 LU, true peak -0.9 dBFS.

## For Dan
`cycles/c56/ab/`: bars 15-23 and bars 23-26, c55 then c56 with 0.8 s between, from the masters with one gain for both
halves; the same two passages on the Violins I and Oboe 1 stems; `envelope_violins1_bars15-16.txt`.

## Tools
`tools/score_to_parts.py`: `_VolParts` (rule names on envelope items), `NOTE_LEVEL`, `ACCENT_SWELL_CAP_DB`,
`ACCENT_SHAPE_MAX_DB`, `ACCENT_PLAIN`, `EARLY_FILL_CAP`, `STEADY_LINE` `body_end_score`, `STP_DUMP_VP` (debug dump of
every envelope item with its rule). With none set parts.json is unchanged (checked byte for byte).
`tools/build_reaper.py`: `ENV_THIN`, mix.json per-track `soft_decresc_keep`. `cycles/c56/actor_scripts/`: `lib56.py`
(written envelope in seconds, cached stem frames, level simulation), `count56.py`, `interior56.py`, `attrib56.py`,
`sim56.py`, `simstems56.py`, `dips56.py`, `accrefit56.py`, `rebowres56.py`, `bell120.py`, `hpq56.py`, `barcheck56.py`,
`realcmp56.py`, `envtable56.py`, `abclips56.py`, `theme56.sh`, `mkvar56.sh`, `p1.sh`-`p6.sh`, `wait_lock.py`.

## Not verified
The final chord's re-bow bumps and the Oboe 1 fills on the render; accents' 2-5 kHz fronts; single bass pitches after
the bell change; tutti-stop decays; the 61 fixed-quarter breakpoints of c55's list; clarinets in bars 26-32 / 139-142;
whether the smaller count is what Dan meant by "unnatural" (the envelope still steps from note to note where a fitted
level differs); no listening.
