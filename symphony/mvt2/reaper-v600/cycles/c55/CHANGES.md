# Cycle 55 (actor): every per-note volume move off

Rendered 2026-11-11 13:20-13:28 (one full render), one stem fix after it (five slow rows), written to REAPER before
the quit. Lock held 12:22:49-13:32:52 (70 min; wait 2 h 58 min behind the finale and the scherzo).

Subject (Dan, 2026-11-11, on the track view): "the volume adjustment was adjusted in large peaks and valleys on so
many individual notes ... To me it seemed unnatural". The cycle went through three states, each built and measured on
the c54 stems before the next (`build_pass1/`, `build_pass2/` hold the tables of the first two):
1. `lead_c55.md`: rule layers off, 59 early fills pruned, trims keyed to the score onset, ramps (8,855 points).
2. The lead's first update (keep a row only if its removal causes an audible fault): 8,172 points.
3. **Dan's decision, 16:30Z: "i want to nuke all the volume adjustments per note i think they are very not helpful,
   there has to be other ways to fix our problem". This is what was rendered.** No per-note layer, no exceptions.

To reverse: `cycles/c55/before/` holds every tool and build file as it was (41 files). With the c54 config and
tables the new tools write the c54 `parts.json` unchanged (checked on every key). `MVT2_C55` (environment) with `n`
builds state 2; the tables and rows are still in the files, switched off by class, not deleted.

## What is in the envelope now
Classes level and shape off (`ENV_CLASS` in the last block of `build/score_config.py`), 1,245 items: re-bow fills 79
and their levels 32, early fills 172, join notches 51, `LEVEL_SHAPES` / `LEVEL_SHAPES_S` / level_fits rows that are not
slow 141 (S1 gap dips, start shapes, body rows, pickup and breath shapes among them), pitch trims 133 + 16 pizzicato +
4 early/body, note trims 60, role rows over one or two notes 179 (`ROLE_NOTE_MIN` 3), long-note swell 193, sostenuto
hold 54, phrase tops 31, metric steps 65, slur-pair release 15, accent swells 9, timpani attack lifts 4, unison boost
3, loop fills 3, bloom cut 1.
Kept (class slow, 848 items): roles over three or more notes 383, hairpin gains 207, slow rows 226 (among them 111
section rows, below), final fade 7, timpani roll rules 20 (settle, soft-roll cut, roll trims, roll hairpins), divisi
chord cut 5; plus the mix's dynamic and soft trims and the phrase arch.
Section rows (`build/cell_rows_c55.json`, `comp55.py`): where a track's level over one of 13 sections moved 0.5 dB
or more against c54 with the per-note layers off, a row of minus that change over the section (25 tracks, largest
9.4 dB). They hold each track's section level; they do not hold the balance between the notes of a section.

## Envelope statistics (`tools/env_stats.py`; `envstats_c54.txt`, `envstats_c55_fix.txt`)

| | c54 | state 1 | state 2 | c55 as rendered |
|---|---|---|---|---|
| points, 32 tracks | 22,022 | 8,855 | 8,172 | **2,572** |
| points per second, all tracks / per onset | 63.6 / 14.6 | 25.6 / 5.9 | 23.6 / 5.4 | **7.4 / 1.7** |
| Violins I, points per second | 4.77 | 2.15 | 1.94 | **0.44** |
| Violins II | 7.02 | 3.13 | 2.92 | **0.57** |
| Violas | 5.81 | 2.50 | 2.37 | **0.66** |
| Violoncellos | 7.11 | 3.12 | 2.72 | **0.60** |
| Double basses | 6.76 | 3.37 | 3.36 | **0.52** |
| travel, dB | 12,125 | 10,751 | 9,898 | **2,667** |
| of it inside single notes / at note edges / in rests | 76 / 18 / 7 % | 74 / 18 / 8 | 75 / 17 / 8 | **66 / 8 / 26 %** |
| notes moving 3 dB or more strictly inside the sounding note (of 1,507) | 631 | 545 | 500 | **157** |
| of those with no hairpin or dynamic change in the note | 288 | 225 | 196 | **47** |

(The reference projects have 0.01-0.36 points per second per track. The 157 notes are printed hairpins and dynamic
changes inside notes, hairpin-gain releases, role edges and section-row edges inside held notes; the 47 unmarked ones
are for c56 to look at: finale c17 item 6.)

## The cost, measured (c54 delivered stems against the c55 render; `acc_c55_fix.txt`, `post_fix.log`)

| | c54 | state 1 (simulated) | c55 render |
|---|---|---|---|
| join holes of 6 dB or more / 9 dB or more | 298 / 93 | 264 / 84 | **379 / 125** |
| notes of 0.6 s or more starting 3 dB or more under their body | 176 | 157 | **302** |
| join peaks of 3 dB / 6 dB or more over the louder body | 234 / 39 | 215 / 33 | 200 / 34 |
| joins 5 dB or more over both bodies with a master bump of 2 dB or more (`joinpeak53.py`) | 2 | 3 | **26** |
| S (`tools/s_onsets.py`): 727 legato joins within 25 / 60 ms | 640 / 711 | 633 / 710 | **613 / 709** |
| S readings moved 20 ms or more (no note-on changed) | | 17 | 66 |
| repeated-note separation (`s1check44.py`, 49 repeats): median stem dip / own-band under 3 dB | 7.4 dB / 5 | | 8.6 dB / 6 |
| re-bows over the 3 dB limit after the re-bow (of 37) | 16 | 16 | **30** |
| attack probe | 0 | | **1** (Violins I 212, 8.0 dB dip in the first 0.45 s, limit 6) |
| median note-to-note step, 44 lines: worse by more than 0.4 dB / better | | 1 / 12 | 14 / 12 |
| balance cells (171) moved 1 dB or more | | 3 | 4, all under -60 dB |
| master bars moved 2 dB or more | | 0 | 11 (bars 11, 20, 30, 35, 44, 48, 71, 73, 86, 89, 92: +3.9 to -2.3) |

Solo margins against c54: Horn 1 bars 7-14 +8.9 -> +8.7 dB, Bass clarinet 31-36 +5.5 -> +5.6, Flute 1 37-44
-2.4 -> -2.3, Oboe 1 45-52 -6.4 -> -6.5, Horn 1 53-60 -7.1 -> -7.3, Clarinet 1 coda -0.4 -> -0.3.
The render agrees with the simulation on the c54 stems (holes 379 / 379, soft starts 302 / 301, S 613 / 613).

## Render figures
Master -23.0 LUFS, LRA 24.2 LU, true peak -3.4 dBFS. Delivered `mvt2-mockup-c55.mp3`: -19.8 LUFS, LRA 15.4 LU, true
peak -1.6 dBTP, limiter 1.6 dB (3), **span 19.1 dB (limit 19; 18.9 before the stem fix)**. Wetness (`check52.py`):
side/mid -5.9 dB, correlation under 250 Hz 0.72, 315-500 Hz against 1 kHz +5.8 dB (c54 6.6). Master 56-112 Hz share
-11.5 -> -10.1 dB whole, bars 61-62 -12.2 -> -10.7, bars 79-81 -11.0 -> -8.8 (the basses' `loud_eq`, section 7).
State guard 0 stale at the start, after each build, after the render, after the stem-fix rows and after the quit;
`state_check.py` c54 -> c55 no state runs. REAPER 39 GB, 0 compressed, before and after the render. Disk 51 GB free.
REAPER holds every row: `rppenv55.py` on the project saved by the quit: 32 tracks, 2,572 points, 0 tracks that
differ from `build/`.

## Per section of lead_c55.md (and what Dan's decision did to it)
1. **Tooling**: done. `tools/score_to_parts.py` tags every item "class:layer" (`vol_add`), writes `vol_cls` /
   `vol_tags` / `env_off`; switches `ENV_CLASS`, `ENV_LAYER` (on / off / capN around each note's mean), environment
   `STP_ENV_CLASS` / `STP_ENV_LAYER`; new `tools/env_stats.py`. Switch test on state 1 (`switch_test.txt`): shape
   cap3 8,012 points, holes 279, soft starts 174; shape off 3,824 / 376 / 304; shape and level off 2,603 / 381 / 302.
2. **Remove**: the five rule layers, 59 + 79 early fills, the two re-bow fills: superseded, everything is off.
3. **Key differently**: `TRIM_KEY` "score" and its options, `START_SHAPE_CAP`, `REBOW_FILL_SPLIT`, `LEVEL_ROW_SPLIT`,
   `FILL_PRE_KEEP_SUM` are in the tool and were measured (state 1: 12 lines better, holes 298 -> 264); with the level
   and shape classes off they act on nothing. The lead's "move phrase-sized rows to roles" was not done.
4. **Slow layers as ramps**: done and in the render. `VOL_GRID_QN` 0.125, `VOL_BP_ALL` (not the timpani), mix.json
   `env_simplify_db` 0.1 (max segment 4 dB). Checked in REAPER on range passes before and after the envelopes were
   written (`rangechk_env.txt`): stem level change against the tools' prediction, 50 ms frames, 95th percentile of the
   residual 0.02-0.22 dB on every track that repeats between two passes (the tremolo strings and the basses of bars
   59-64 differ by 5-33 dB between two identical passes and cannot be read). REAPER's fader scale, read in the session
   (`env_scale.txt`): 0.676 at -12 dB, 0.507 at -20, 0.239 at -40 of its 0 dB value; amplitude ** 0.25 gives 0.708 /
   0.562 / 0.316, so `ENV_SCALE` is only right near 0 dB; the 4 dB segment limit keeps the error small.
5. **Keep unchanged**: superseded. Nothing per-note is kept.
6. **Instrument-side tests** (range passes; `pizzchk_v.txt`, `timpchk.txt`, `tbnchk.txt`):
   - Violas' pizzicato triplets bars 41-44: per-pitch fader trims off; velocity on 16 notes (F sharp 3 +16, B flat 3
     +12, F 4 -10, F sharp 4 -4). Spread of the pitch means 3.86 dB (c54, trims) / 6.10 (no trims) / 4.09 (velocity);
     median step 1.78 / 2.83 / 2.32 dB. Adopted. The row follows velocity by about 0.15 dB per step upward and by
     13 dB for -16 on the F 4.
   - Timpani strokes: fader lifts off; velocity 172: 72 -> 100, 203: 96 -> 106, 209.5: 96, 277: 56 -> 88. Stroke peaks
     c54 / c55 range pass: -37.7 / -38.0, -20.2 / -21.2, -31.1 / (92: -33.7, set to 96 unmeasured), -38.6 / -39.3 dB.
   - Not done: a CC11 lift in place of early fills; CC1 brass shape.
7. **Bass and small items**: Double basses `loud_eq` climax shelf 100 Hz -1.5 -> +1.0 dB and the 80 Hz +2 bell from
   bar 71 (largest K-weighted bar change +0.16 dB simulated; shares above). Trombone 1 215.0 velocity 124 -> 112:
   slur dip before 215 1.6 -> 2.5 dB, 2-5 kHz attack over body +1.0 -> +0.7 dB (first 80 ms from the note-on). Not
   done: Clarinet 1 289 "Leg Slur Rep" test, Violins II 47.

## Stem fix after the render (level only, slow rows; `build_fix/`, originals in `render_first/`)
Five section rows on tracks under -54 dB in their section, which the offline pass had left out: Timpani bars 83-92
-6.4 dB (the coda strokes with their new velocity) and 65-70 -2.7, Horn 3 bars 23-30 -5.3, Oboe 1 bars 37-44 +4.7,
Cor anglais bars 53-60 +2.8, Harp harmonics coda -2.3. `--mix-only` on the five tracks, save, guard, before the quit.

## Faults left audible (no per-note volume move goes back; for c56 on the instrument side)

| fault | where | size | instrument-side fix to test |
|---|---|---|---|
| repeated note no longer separate | Violas 81 (bar 28) | own dip 8.9 -> 1.5 dB | `REP_GAP_AT` gap 0.12-0.15 s with a CC11 fall, or a new-bow stroke row |
| | Double basses 144 (bar 46), 156 | 9.0 -> 3.0, 7.9 -> 5.1 dB | longer `REP_RETONGUE` gap, CC11 fall before the repeat; "Stac On Bow" is not usable for a held note |
| | Violins II div 120, Violoncellos 300.6 | 6.5 -> 3.7, 4.9 -> 2.8 dB | `STR_REP_NEW_BOW` `soft_gap_s_at` 0.15 s |
| soft start of a legato target | 302 notes (c54 176): bars 53-60 50, 71-78 45, coda 39, 23-30 35, 45-52 34, 37-44 26 | first 0.35 s 3 dB or more under the body | CC11 lift over the first 0.3 s of the target (Scherzo c11), legato velocity, shorter lead where S allows |
| join hole | 379 joins of 6 dB or more (c54 298); 137 deepened by 2 dB or more, worst Oboe 1 47 (11.1 dB), 57, 143, 140, Flute 1 195.5 (9.8) | | CC11 lift across the join, more overlap, a slower or faster legato row |
| transition burst | 26 joins with a master bump of 2 dB or more (c54 2); Violins I 75, 86, Violins II 271, Violas 238.5, Harp 253 | 6-12 dB over the louder body | legato velocity (transition speed), CC11 dip of 6-10 units over the transition, keyswitch timing |
| re-bow dip and loop pulsing on held notes (Dan's note 8) | 30 of 37 re-bows over the limit (16): the final chord, the coda pedals, bars 1-6, 65-70 | dips to 10-14 dB | overlap the two bows by 0.2-0.3 s with a CC11 crossfade, CC1 vibrato change at the bow change, stagger |
| note out of its line | per-pitch sample levels: Horn 1 theme (bars 9-13 master -1.1 to -1.7, bar 11 +2.9), Flute 1 bars 37-44, basses by pitch, Cor anglais 151-152, Violoncellos c52b notes | 2-5 dB | row volume in the patch (`layerMatrix.rows[].volume`, finale technique 64), CC11 offset per note where the layer allows, CC1 on the horns |
| bars sticking out | master bars 30 +3.2, 35 +3.9, 44 +3.3, 48 +3.0, 71 +3.2, 73 +2.7, 92 +3.1; bars 86-88 -1.7 to -2.3 | | phrase-sized role rows (three notes or more), then CC11 |
| printed attack | Violins I 212 sf tremolo chord: probe hole 8.0 dB; Trombone 1's accents 213 / 218 without their swell | | lower resting CC11 with the slow trim making up the level, accent CC bump (finale c17 item 1) |
| timpani | 209.5 stroke velocity unmeasured; rolls keep their rules | | range pass |
| delivery | span 19.1 dB (19) | 0.1 dB | `_all` climax row -0.4 -> -0.6, or soft-section rows |
| pizzicato triplets | violas bars 41-44: median step 2.32 dB (c54 1.78) | | second velocity fit; pitches 49 / 51 / 53 lie 6-11 dB under 61 with or without trims |

## Files
Tools: `tools/score_to_parts.py`, `tools/build_reaper.py`, `tools/stem_fix.py`, new `tools/env_stats.py` (README,
"c55"). Build: `build/score_config.py` (c55 blocks at the end), `mix.json` (`env_simplify_db`, basses `loud_eq`),
`early_fills.json`, `pitch_trims.json`, `note_trims.json`, `level_fits.json`, `rebow_fills.json` (pruned rows kept
under `_removed_c55*`; all of these layers are off), new `join_notch_fits_c55.json`, `row_off_c55.json`,
`cell_rows_c55.json`. Session: `s1.log`, `s2.log`, `s2b.log`, `s2c.log`, `s3.log`, `s4.log`; range passes in
`rangetest/`. Records of states 1 and 2: `early_fill_decisions.txt`, `prune2_decisions.json`, `restore_y1.txt`,
`notchfit.txt`, `switch_test.txt`.
