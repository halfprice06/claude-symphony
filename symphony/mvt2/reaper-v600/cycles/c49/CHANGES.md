# Cycle 49 (actor): state drift (Trombone 1 rebuild, Violas reset), pitch trims, pedal refit, sul tasto joins, Oboe 1 and Harp harmonics image

Rendered 2026-11-09 16:32 (`cycles/c49/mvt2-mockup-c49.mp3`), one render, no stem fix and no splice. Inputs: critics
A / B / C on the c48 render (`reports/`), the loop lead's merge notes, `loop/ONE_TIME.md` (finale techniques 18-23 and
three items carried from c48). Snapshot before the changes: `before/`. Data the render was made from: `rendered_build/`
(19 files: the `build/` tables, `score_config.py`, `build_reaper.py`, `score_to_parts.py`); `build/` is the same
(regenerating `parts.json` from the current config gives an identical file, 0 warnings). Scripts: `actor_scripts/`.
Range-render job files: `rangetest/` (the range audio is deleted). No note pitch, start or length of the score changed.

## Lock and drive
- Turn rule: Movement I's c52 actor held the lock from 14:25:44; I waited from 15:14 and took it when it was released.
- **Lock 15:37:42-16:44:34 (67 min).**
- 15:38-15:54 start, open, three full rebuilds (Trombone 1, Oboe 1, Harp harmonics), eleven tracks `--midi-only`,
  `--mix-only`, five range renders (s1 qn 41.5-67, v1 and v2 qn 143-170, f1 qn 90.3-126, g1 qn 265.5-292). REAPER grew
  to 45 GB (compressed 34 GB at the peak, 26 GB at the end of this phase).
- 16:03 `parts.json` regenerated with the fitted fills and the final fp shape, `--mix-only` on every track, the test
  return "R Stage" removed (36 tracks again). 16:04-16:06 five range renders (v3, f2, s2, g2, g3; 12-25 s each).
- 16:08:53-16:11:03 `save` and `restart`; settled at 44 GB / 27 GB compressed by 16:21. 16:24:01 the usual
  `Audio_Init` script after the restart (device read only: 48000 Hz, block 512, no input, Mac Studio Speakers; no
  device setting changed).
- 16:24:06 `render_cycle.py 49` refused by the memory gate (27 GB compressed, limit 6.0; `render_cycle_refused.log`).
  The figure was 27 GB when the memory settled at 16:21 and still 27 GB at 16:24, after one restart already, so I ran
  `render_cycle.py 49 --force-memory` (the c29-c39 precedent): **16:24:37-16:32:12**, attack probe 0.
- **After the render: REAPER 44 GB, 27 GB compressed.** Post-render checks until 16:43, `quit` 16:43:20-16:44:29,
  `unlock` 16:44:34. Disk 32 GiB free after the render, 34 GiB after the quit.

## Results (c49 render; c48 in brackets)
- **Master -22.9 LUFS** (-22.9), **LRA 23.5** (23.5), **true peak -3.7 dBFS** (-3.6), sample peak 0.650.
- **Delivered -19.8 LUFS**, **LRA 14.6** (15.3), true peak -1.6 dBTP, **limiter about 1.9 dB** (2.1), **p10-to-max span
  18.0 dB** (18.8), length 354.70 s.
- **Attack probe: late or hole 0.** Motion (master): dS4 p90 7.03 (7.18), 1 s / 20 s 4.24 (4.28).
- Targets: disk 32-34 GiB (at least 30); span 18.0 (at most 19); limiter 1.9 (at most 3); probe 0; wetness t20 strings /
  winds / brass **0.376 / 0.299 / 0.253 s** (0.376 / 0.304 / 0.253; limits 0.55 / 0.50 / 0.50); final chord t20
  **0.444 s**, t10 0.289 (unchanged; limit 0.45). All met.
- S1 (`s1_c49.txt`, 49 repeat points): own-band median dip 7.3 -> **8.1 dB**; points under 3 dB 8 -> **3** (Bass
  clarinet 265 1.5, Contrabassoon 265 0.0, Double basses 168 0.0; the basses' 168 shows 8.3 dB in the 30-120 Hz band,
  see technique 18); master median 3.7 -> 3.8 dB.
- S2 (`pcx_c49.txt`, join medians of the perceived attack): Violins I +20 -> +17 ms, Violins II +20 -> +18, Violas
  +4 -> +4, Oboe 1 +40 -> +31, Trombone 1 -24 -> -24 (4 joins); robust SD 62-70 ms.
- S3 (`check46_c49.txt`): steepest 10 ms fall of the master at the caesuras at most 1.2 dB (at 188); at 148 0.5 ->
  0.3. Own measure (20 ms RMS in 5 ms steps; c47 / c48 / c49): fp bar 148.0-148.8 master 1.3 / 1.1 / 1.2 dB, R Strings
  2.3 / 1.7 / 1.9; breath 195-196 master 1.8 / 1.6 / 1.9, R Strings 2.3 / 2.3 / 2.3. No fast fall was added.

### State drift on unchanged data (the lead's first priority)
`state_check.txt` is c48 -> c49, `state_check_c47.txt` is c47 -> c49. Stems start at score qn 0 (no pre-roll offset).
- **Trombone 1, fully rebuilt. Qn 212.4-217.42 is identical to c47**: RMS difference 0.00 dB in every window, residual
  -109..-114 dB. c48's own render had been +2.74 / +3.10 / +2.52 dB there (212.91-214.5 / 214.91-215.41 / 215.41-216).
- **Trombone 1 at 217.5 differs from c47 after the full rebuild**: the legato target (p, Leg Slur MAX, velocity 112) is
  **-1.9 dB and +35 ms** (217.42-218: -29.08 dB against c47's -27.15 and c48's -27.30). The master there is -28.56
  against -26.87 dB (-1.7 dB) for about 0.75 s; 218-219.5 is within 0.12 dB. 40 ms RMS around the beat: c47 -30.9 -29.4
  -26.8 -27.2 -26.2, c49 -30.9 -30.8 -29.5 -29.5 -28.8 (the transition's low part lasts one window longer and the note
  stays 1.5-2 dB lower). Not compensated: a level shape would be fitted to one Opus state and cannot move the 35 ms.
  This is one measured case for c50 of what a full rebuild does to a loud legato join.
- **Violas 152-168 (A #1), reset at 152.06. The takes are back in c47's order**: E flat 4 peaks at +140 / +50 / +135 /
  +55 ms in c47 and c49 (c48 -130 / +320 / -125 / +315). All 15 eighths: peak times within 5 ms of c47, levels within
  -1.0..+0.7 dB; SD of the -3 dB time 37 ms (c47 36, c48 104). 40 ms envelope over 152.2-168.5 against c47: median
  difference 0.33 dB, p95 0.90, max 2.29, residual -17.1 dB re the stem (c48 against c47: 1.82 / 5.46 / 8.82 dB,
  residual +3.0 dB). Two range renders of qn 143-170 were identical after the reset point (difference -246..-252 dB),
  so a CC16 inside the music does reset the row and A's fallback was not needed. The nine Violas entry leads were kept
  (the attacks are c47's, which they were fitted on). One flag c47 -> c49: 156.5 perceived attack -51 ms.
- The new "take swap" lines print for c48 -> c49 ("take swap Violas: qn 152.50-167.50, pitch 57: 156.50 +55 ms, 160.50
  -51 ms" and pitch 63 at 165.5 / 166.5 / 167.5: -32 / +49 / -35 ms). They report the return from c48's order. No take
  swap line for c47 -> c49.
- **New: c48 had more drift than was reported.** c48 -> c49 flags the Double basses on unchanged data at qn 3 and
  60-80 (12 notes, Sus MAX: 60 -2.61 dB / -36 ms, 66 -2.87 / +101, 72 -3.38 / +39, 79 -6.53 / +41, 80 -4.15 / -102;
  level median -1.7 dB), Violoncellos div 63 (-4.03 dB / -60 ms) and Horn 1 198 (+2.16 dB / -32 ms). Against c47 the
  same tracks have 1 / 2 / 0 flags (basses 75 +0.19 dB / +33 ms; Violoncellos div 52 +91 ms, 63.5 -59 ms), and
  `pitch_check` c47 -> c49 has no basses flag. So in c48 these notes differed from c47 on unchanged data, and c49's
  builds are back in c47's state. c48's basses were about 1.7 dB louder at 60-80 than in c47 and c49.
- Other flags c47 -> c49 (no state run, no timing run; levels within 1.1 dB): Oboe 1 269 -76 ms and 271 -60 ms (full
  rebuild with new mics); Violins I 9 notes (86 +61 ms, 195.5 +107, 262 +99, 266 -71), Violins II 3 (262 +101), Violas
  10 (208 Tremolo +124), Violoncellos 5 (164 +125), Violas div 1 (283 +57).

### The fp at qn 148 (`m48_c49.txt`)
| part | note-on | peak (time re beat) | own drop | at +0.1 s re peak | p within 3 dB |
|---|---|---|---|---|---|
| Violins II | -120 ms (-60) | -39.6 dB at **+60 ms** (-39.7 at +115) | 12.7 / 13.2 dB (12.8) | -1.1 dB | 400 ms |
| Violas | -60 ms | -34.3 dB at +5 ms | 14.1 / 13.8 dB | -1.2 dB | 400 ms |
| Double basses | -160 ms | -34.1 dB at +50 ms | 13.8 / 14.1 dB | -0.6 dB | 440 ms |

Master at -100 / 0 / +150 / +350 ms: -36.3 / -31.1 / -31.3 / -35.1 dB (c48 -36.1 / -31.2 / -31.2 / -35.0). **Master
tilt jump 2.2 dB** (c48 3.3; ceiling 3.0). Own tilt jumps: Violins II 4.6, Violas 3.2, basses 0.7. Every drop stays over
10 dB.

### B #1-#5 against B's predictions (`bcheck_c49.txt`; K-weighted note bodies, dB)
- #1 Horn 1 D4: 22 -32.1 -> -35.0 (predicted -35.1), 229 -31.7 -> -34.6 (-34.7).
- #2 Cor anglais: 126 -38.1 (-38.1), 127.5 -38.6 (-37.2; **1.4 dB under**), 130 -38.9 (-39.0), 131.5 -40.1 (-40.6),
  133.5 -42.4 (-41.9), 156 -39.0 (-38.9), 166 -39.6 (-39.7), 168 -43.3 (-43.4), 171 -42.8 (-42.7), 286 -50.2 -> -47.2
  (B asked for the F4 trim to act at 286).
- #3 Clarinet 1: 280 -46.6 (-46.5), 283 -43.5 (-43.7), 286 -41.7 (-41.7), 289 -41.9, 292 -44.1.
- #4 Bassoon 1 A flat 3: +4.4..+5.0 dB at eight notes (21 -51.4, 22 -51.1, 24 -55.2, 32 -51.6, 33 -54.0, 39 -55.6,
  231 -51.0 against a predicted -50.1, 238 -52.4).
- #5 Oboe 1: 42 -43.1 (-43.2), 43.5 -39.1 (-38.7), 44 -38.9 (-38.2; 0.7 under after the mic change), 45 -38.4 (-38.5).
- #6 `tools/pitch_check.py` added (`pitch_check.txt`). c48 -> c49: Oboe 1 and Harp harmonics have no pitch 2.5 dB or
  more from their track's median change after the mic and width changes. Flags: basses C sharp 3 at 74 / 80 / 81
  (-4.0 dB; c48's drift, see above); Violins II E flat 4 at 120 (-5.7 dB) and Violins II div F4 at 122 (-4.5 dB), which
  are window effects of A #3 (the note at 120 is 2.15 qn long now, was 2.7, and the stem at 120.5-122 is unchanged; at
  122 the old note's overlap now ends at 122.15). Limitation: the check flags a note whose length or overlap changed.

### Solo margins (`check44.txt`, dB; c48 -> c49)
Violin I solo bars 17-22 -4.8 -> -4.5; Flute 1 bars 37-40 7.0 -> 7.5; Cor anglais bars 41-44 2.5 -> 3.2; Oboe 1 bars
45-47 4.9 -> 4.5; Horn 1 bars 67-70 8.7 -> 7.6 (B #1); Clarinet 1 over the Cor anglais bars 87-88 7.8 -> 6.3 (the Cor
anglais's 286 is 3 dB up, as B asked); Harp harmonics over Violoncellos div + basses bars 83-86 -3.9 -> -2.4;
Clarinet 1 bars 85-89 3.4; Trombone 1 bars 63-64 10.6. Timpani share of 30-150 Hz: bars 1-3 8.3 -> 10.8 %, bars 84-85
16.2 -> 18.7 %.

### A #2: the pedal at bars 85-87 (0.4 s RMS over qn 275.5-284)
Double basses swing 8.4 -> **4.7 dB** (SD 1.79 -> 1.16); Violoncellos div 6.6 -> **1.0 dB** (SD 1.63 -> 0.26). Master,
0.1 s RMS around 320.6-321.1 s: c48 rose from -52.1 to -45.0 dB in 0.4 s (7.1 dB), c49 from -49.4 to -47.4 (2.0 dB).

### A #3: Violins II and Violins II div sul tasto pad, bars 37-40 (`flaut_c49.txt`)
- Time at which the new pitch passes the old one after the join: 114 +0.50 s, 116 +0.20, 118 +0.40, 119 +0.50 (the lead
  is limited to 0.44 s by the 1 qn note before), 122 +0.30, div 112 +0.15, div 118 +0.33, div 122 +0.48 (c48
  +0.38..+1.00 s). **Within A's ±0.3 s at 3 of 8 joins** (116, 122, div 112). Pad troughs 0.5-4.6 dB.
- Weak join at 119: Violins II alone at 119.5-120 -57.5 dB (c48 -52.6); at 118.0 / 118.5 -2.9 / -2.4 dB. The master
  there is within 0.4 dB of c48. A's fallback (Sus MAX with CC1 0 for the pad) was not tried.
- A track-level fill raises the old and the new pitch alike, so it cannot move the crossing time; only the lead and the
  overlap do.
- S2 kept: the pad's note-ons moved earlier, the perceived attacks stay on the beat (Violins II median +20 -> +18 ms).

### C #2 and C #4 (`gain_c49.txt`)
- Oboe 1 (Main 0.088 -> 0.24): stem 1-4 kHz correlation 0.98 -> **0.89**; level qn 42-48 -41.98 dB (-42.15; +0.17, of
  which B #5's +2 dB at 44); per-note R-L +2.39 dB (+2.24; without the pan +2.68); per-pitch spread 1.9 dB (0.6).
- Harp harmonics (width 0.05 -> 0.3): per-note R-L -10.10 -> **-3.08 dB** (target -2..-4); level -50.43 dB (-50.39);
  per-pitch spread 3.8 dB (2.2); correlation median 0.75.

### Master level against c48 (3 s RMS; every change comes from a data change)
24-25 s -0.8 / -1.3 dB (Horn 1 B #1, with Bassoon 1 +3.1); 177 s +0.7 and 189-192 s +0.9..+1.4 (Cor anglais F4 / F
sharp 4, B #2); 257-259 s -1.2..-1.3 (Horn 1 at 229); 321-325 s +0.9..+2.0 (Clarinet 1 +3.0, basses -0.8, Violoncellos
div +0.7). The delivered LRA fell 15.3 -> 14.6 with the master LRA unchanged; I did not trace it to one passage.

## Changes (files and parameters)

Opus state changed on three tracks, which were fully rebuilt (patch reloaded): **Trombone 1** (no data change; the
lead's state-drift fix), **Oboe 1** (mics) and **Harp harmonics** (width). Eleven data tracks took `--midi-only` (Cor
anglais, Bassoon 1, Clarinet 1, Horn 1, Bass trombone, Double basses, Violoncellos div, Violins II, Violas, Violins II
div, Violas div) and every track `--mix-only`. In `parts.json` the `notes` differ only in the played timing of led /
overlapped notes (Violins II, Violas, Violins II div, Violas div).

Tools (generic, each with a default that leaves other scores as they were):
- `tools/score_to_parts.py`:
  - `RR_RESET_AT = {}` ({track: [score qn, ...]}): extra round-robin reset points, merged into the track's `cc36` lane
    as value 127 (A #1).
  - `STR_REP_NEW_BOW["soft_gap_s_at"]` ({track: {qn: seconds}}): the played gap before a listed soft repeat, in place
    of the one `soft_gap_s` for all of them (finale technique 21).
  - `build/level_fits.json` ({track: {"score qn": [[seconds, dB], ...]}}; keys starting with "_" are notes): fitted
    post-FX level shapes on score-anchored seconds, appended to `LEVEL_SHAPES_S` (A #3's fills).
  - Finale technique 20: a per-note legato lead (`lx`) is added to the family lead before `LEG_LEAD_CLAMP` is applied,
    not after it. No Movement II onset moved (the timing of legato targets in `parts.json` is identical).
- `tools/build_reaper.py`: the `parts.json` `cc36` lane is sent on `RR_RESET_CC` (CC16, the controller Opus resets on;
  CC36 inside the music did not reset a stroke row in Movement I c14) and is not repeated in the pre-roll, which has
  its own reset at `RR_RESET_QN`.
- `tools/state_check.py`: "take swap" lines. On the rows named by `--swap-arts` (default Detache), compared notes are
  chained while they are within 4 qn of each other, and a line is printed when two notes of one pitch moved their
  perceived attack by more than `--ms` in opposite directions between the two renders (A #1's signature).
- `tools/pitch_check.py` (new, B #6): per-pitch level change between two renders against the track's own median
  change (K-weighted body, notes of at least 0.9 qn with the same CC1 / CC11; the envelope change removed). To run
  after every render in which `mics`, a family EQ, a width or a patch changed.

Config (`build/score_config.py`, c49 block at the end):
- A #1: `RR_RESET_AT = {"Violas": [152.06]}` (after the Detache keyswitch region starts at 152.0, before the keyswitch
  at 152.125 and the first eighth at 152.5).
- A #3: `FLAUT_LEAD_S, FLAUT_OVERLAP_QN = 0.75, 0.15` (were 0.45 s and 0.7 qn; the lead stays capped at 0.45 of the
  previous note). Fills in `build/level_fits.json`, fitted by `actor_scripts/meas49.py flaut --fit` on a range render
  made without a fill; each fitted value falls linearly to 0 at 1.2 s after the note-on (or at the note's end).
- Finale 18: basses `LEVEL_SHAPES_S` (253.0, [(-0.160, 0), (-0.154, -9), (-0.103, -9), (-0.097, 0)]).
- Finale 19: Bass trombone `LEVEL_SHAPES_S` (212.0, [(-0.02, 0), (0.0, 3), (0.08, 3), (0.15, 0)]).
- Finale 21: `STR_REP_NEW_BOW["soft_gap_s_at"]` = 0.12 s at Violas 271, Violins II 289 and 120, Violas div 79, Violins
  II div 114 and 119.
- Finale 22: Oboe 1's +3 dB shape over 142 / 142.5 ends at 142.858-142.879 (was 142.70-142.72).
- The fp at 148, `FP148_V2_EARLY = True`: the Violins II note-on 60 ms earlier (`build/entry_leads.json` Violins II
  `"148": 0.06`; -120 ms re the beat), and their bump (148.0, [(-0.06, 0), (-0.04, 3), (0.06, 3), (0.16, 0)]) replaced
  by (148.0, [(-0.12, 0), (-0.10, 3), (0.06, 3), (0.14, -2), (0.27, -2), (0.36, 0)]). The -2 dB part holds down the
  sample's later swell, which had been the +115 ms peak.

Per-note tables (`build/`):
- B #1 `pitch_trims.json` Horn 1 `"62": -3`.
- B #2 `pitch_trims.json` Cor anglais `"65": 3, "66": 3` with `"_all_arts_pitches": [65, 66]`; `note_trims.json` Cor
  anglais `"130": 1`.
- B #3 `roles.json` Clarinet 1 [280, 286, -2.5, 0.5] -> [280, 286, 0.5, 0.5]; `note_trims.json` Clarinet 1 `"286"`
  2.5 -> 1.5.
- B #4 `pitch_trims.json` Bassoon 1 `"56": 5`.
- B #5 `note_trims.json` Oboe 1 `"44": 2`.
- A #2 `rebow_fills.json`: Double basses 278.351 (70 -> 111 points) and 282.203, Violoncellos div 275.527, 277.599,
  279.67, 281.716 and 284.141 refitted (`actor_scripts/refit49.py`, fit window 4.1 s).
- `entry_leads.json`: Violins II `"148": 0.06`.

Mix (`build/mix.json`, note `_c49`):
- C #2 Oboe 1: `mics.Main` 0.088 -> 0.24 (the cor anglais's value), `track_pan` -0.03, `gain_db` unchanged.
- C #4 Harp harmonics: `width` 0.05 -> 0.3 (the Harp's), `track_pan` 0.25, `gain_db` 2.2 -> 3.7. Width 0.3 with pan 0
  gave a per-note R-L of -5.9 dB, pan 0.12 gave -4.7, pan 0.25 gave -3.1.

Loop files: `README.md` (c49 line under the tool changes), `loop/HISTORY.md`, `loop/LEARNINGS.md`,
`loop/MANUAL-GAPS.md` (gap 10: the mid-score reset), `loop/ONE_TIME.md` appended to `loop/ONE_TIME.done.md`.

## ONE_TIME items (finale techniques 18-23 and the items carried from c48)
- 18 (low-string repeats judged at 30-120 Hz, a -9 dB dip in the played gap): **adopted at the basses' 253**, the one
  low repeat under 3 dB in that band. Dip at 30-120 Hz 2.7 -> **7.7 dB** (broadband stem 2.4 -> 5.1). The basses' other
  repeats already had 8.0 / 8.9 / 8.3 / 11.5 dB (144 / 156 / 168 / 265) and were left.
- 19 (sf bump on a wind / brass sf whose first 0.1 s is more than 2 dB under the f before it): **adopted for the Bass
  trombone at 212**. First 0.1 s -32.4 -> **-29.4 dB**, next 0.3 s -28.7 -> -28.2; the f before (211-211.8) is -30.8.
  **Not needed for Flute 1 at 212** (it starts 2.5 dB over its f).
- 20 (negative per-onset lead row added before the clamp): **adopted** in the tool; no Movement II onset moved.
- 21 (a longer gap for a soft repeat that starts a new slur): **adopted** at the six S1 points under 3 dB (0.12 s).
  Own-band dip (stem in brackets): Violas 271 3.2 (2.9) -> 8.2 (9.8); Violins II 289 2.0 (1.9) -> 5.9 (5.7); Violins
  II 120 2.2 (4.4) -> 3.3 (2.9); Violins II div 114 1.7 (2.3) -> 8.1 (6.9); Violins II div 119 1.5 (1.8) -> 4.5 (3.9);
  Violas div 79 2.2 (3.5) -> 9.0 (9.9).
- 22 (a level shape must cover the whole run it lifts): **adopted** for Oboe 1 at 142 / 142.5. Stem bodies -46.4 /
  -47.8 -> **-46.6 / -46.3 dB** (the 142.5 eighth +1.5; K-weighted body -43.7 -> -42.3).
- 23 (hold the delivery ride through a subito bar): **dropped**. Movement II's delivery has no ride rows to hold. The
  subito steps on c49, master / delivered: qn 28.3 (bar 10) 6.5 / 6.5 dB; 83.2 (bar 28) 7.0 / 5.7; 150.2 (bar 51)
  6.9 / 6.7; 218.8 (bar 73) 15.9 / 12.1; 270.8 (bar 91) 6.5 / 5.2 (c48: 6.5 / 6.5, 7.6 / 6.3, 7.0 / 6.8, 15.9 / 12.2,
  6.5 / 5.2). The bar 73 subito loses 3.8 dB in the delivery in both renders.
- Carried, Trombone 1 full rebuild: done (results above).
- Carried, the fp at 148: done (`FP148_V2_EARLY`; tilt jump 3.3 -> 2.2, Violins II peak +115 -> +60 ms).
- Carried, stale legato state: **deferred to c50 by the loop lead** (the full legato rebuild and lead refit get their
  own cycle so that the effect on S2 can be measured alone). Nothing of it was done here.

## Rejected or deferred
- **C #1 (a short "R Stage" return fed only from the solo violin): tested on a range render (qn 41.5-67), dropped.**
  Master 1-4 kHz correlation in bars 17 / 18 / 21 / 22 without it: 0.98 / 0.97 / 0.97 / 0.83 (the recordings' band is
  0.83-0.90). With the return at fader -7.0: 0.93 / 0.90 / 0.92 / 0.79, level +0.49 dB; -6.0: 0.92 / 0.89 / 0.90 /
  0.78, +0.59; -4.0: 0.89 / 0.85 / 0.87 / 0.75, +0.85 dB; -1.0: 0.82 / 0.76 / 0.79 / 0.69, +1.46 (the return's stem
  scales with the fader, so one range render gives every value). The correlation does fall toward the recordings, but
  no fader meets C's own acceptance (0.83-0.90 in bars 17, 18 and 21 with at most +0.5 dB): the values inside the band
  cost +0.85 dB. The return alone takes 0.55 s (qn 54) and 0.61 s (qn 65) to fall 20 dB against C's 0.25 s, and the
  solo's decay with it goes from 0.26 / 0.33 s to 0.45-0.46 / 0.40-0.42 s. The lead's condition (the solo's decay must
  not lengthen; Dan's note is "too wet and mushy") is not met. The track and its send were removed before the render.
  A variant with an impulse of about 0.1 s or less is open.
- C #3 (timed pan for Clarinet 1, bars 87-88): not done. It needs a pan envelope path in `build_reaper.py`; the lock
  was already at 67 min. Open.
- A #1's fallback (the Violas' eighths on one fixed take): not needed, the mid-score reset works.
- A #3's fallback (Sus MAX with CC1 0 instead of the sul tasto patch): not tried; the result above is 3 of 8 joins.
- Trombone 1 at 217.5 (-1.9 dB, +35 ms after the full rebuild): not compensated, see above.
- The full legato rebuild and lead refit: deferred to c50 by the lead (`loop/ONE_TIME.next.md`).
- Technique 23: dropped (above).

## Open
- **c50: the full rebuild of the stale legato state and the lead refit** (`loop/ONE_TIME.next.md`). Evidence from this
  cycle: Trombone 1's fully rebuilt track has its loud legato join at 217.5 35 ms later and 1.9 dB lower than in c47
  (master -1.7 dB for about 0.75 s).
- State drift is wider than c48 reported: in c48 the basses at 60-80 (median +1.7 dB, up to +6.5 dB at 79),
  Violoncellos div 63 and Horn 1 198 differed from c47 and c49 on unchanged data. Compare each render with the two
  before it (`state_check.py` against c(N-1) and c(N-2)).
- A #3: the crossing is within ±0.3 s at 3 of 8 joins; the join at 119 is 4.9 dB weaker on the Violins II stem than in
  c48 (master within 0.4 dB). Next: A's fallback, or a shorter overlap only at 119.
- C #1 with an impulse of 0.1 s or less; C #3.
- Cor anglais 127.5 is 1.4 dB under B's prediction; Bassoon 1 231 0.9 dB under.
- Clarinet 1 over the Cor anglais in bars 87-88: margin 7.8 -> 6.3 dB (B's 286 trim on the Cor anglais).
- Harp harmonics: per-pitch spread 3.8 dB (2.2) after the width change; Oboe 1 1.9 dB (0.6) after the mic change. Both
  under `pitch_check`'s 2.5 dB against the track median, but B may want pitch trims.
- Delivered LRA 15.3 -> 14.6 (master LRA unchanged); the bar 73 subito keeps 12.1 of 15.9 dB in the delivery.
- S1 points still under 3 dB: Bass clarinet 265 (1.5), Contrabassoon 265 (0.0), Double basses 168 (0.0 own-band; 8.3
  dB at 30-120 Hz).
- `pitch_check.py` flags notes whose length or overlap changed (two false flags this cycle).
- The render needed `--force-memory` (27 GB compressed after the restart; probe 0).
