# Cycle 04 (actor), on the c03 render and the critics' reports A, B, C

No ONE_TIME.md this cycle. Snapshot in `before/`. Measurement script: `cycles/c04/actor_scripts/m.py`.

## Changes

Tools (generic, off by default):
- `tools/score_to_parts.py`: new `TIMP_DAMP_AT = [(from qn, to qn, CC7)]`. The timpani's CC7 lane falls linearly in 0.05 qn steps and holds the low value until the next timpani onset's own CC7 point. The drum is damped before the Opus hall, so the hall tail still rings. parts.json `timp_damp`.
- `tools/score_to_parts.py`: `STAC_LEAD_S` now applies to brass staccato rows too (it covered strings and winds only).
- `tools/auto_fills.py`: Clarinet 2 and Bassoon 1 added to `TRACKS` / `RAISE_TRACKS`.

Data:
1. **G.P. timpani ring** (B #4, C #3, c03 open item; the top fix). `TIMP_DAMP_AT = [(1014.5, 1015.25, 1)]`: CC7 127 -> 1 over about 0.16 s (quarter 288), after the bar-339 Sht chord has spoken, held until qn 1086. Timpani role `[1007.9, 1020, -4]` (the 1014 stroke was the loudest stem). C #3(a), putting 1012 on the Sht row, was not done: the CC7 damp covers it, and 1012 is a printed accented half note.
2. **Harp, F major episode** (B #2, C #5). `VEL_CAP_SPANS["Harp"] = [(216, 240, 56), (240, 264, 50)]` (Pluck p layer 1-57), plus roles `[216, 240, -3]` and `[240, 264, -2]`.
3. **Summit margin** (C #2, BRIEF item 6). `RIDE_TRIMS` (delivery ride only): -2 dB over 300-312 (ramp 300-303), -2 dB over 897-912 (ramp 897-900), -1.5 dB over bar 72 (212.5-216.3). B #3's celli EQ cut (below) lowers bars 104/304 and 1005 by about the same amount.
4. **Bassoons and bass clarinet over the lines** (B #1). `mix.json` Bassoon 1 / Bassoon 2 `gain_db` -2 -> -5. Roles: Bassoon 1 576-600 -3, 624-672 -3, 1032-1044 -3, 696-711 +2; Bassoon 2 624-672 -4; Bass clarinet 240-264 -5, 624-672 -4; Violoncellos 624-672 -3 -> -1.
5. **Celli in the tuttis** (B #3). `mix.json` Violoncellos `loud_eq` 150 Hz +6 -> +2 dB.
6. **Violins II** (B #5): roles 192-198 +4 and 501.5-588 +4.
7. **Doubling winds** (B #6): Flute 1 132-150 -3 and 372-384 -5; Oboe 1 372-384 -3; Cor anglais 144-150 -3.
8. **Clarinet 1 trio tune** (C #4): `pitch_trims.json` B4 3 -> 7.5, C#5 +4.5, D#5 -2.5, G#5 -3.5, A5 -4.
9. **Coda staccato pairs** (A #3): the tutti staccatissimo rows over 981-1005 too, for Violins I (Stac RRx14), Violins II (Spiccato RRx9) and violas (Staccatissimo RRx16). The celli were left out. Critic A wrote that every row was already loaded, but the celli have no staccato in the tuttis, so "Staccatissimo RRx16" is not loaded on that track (13.9 thousand regions).
10. **Theme A identical staccato samples** (C #1): the 2nd and 4th four-bar phrases of each p/mp statement (48-60, 72-84, 768-780, 792-804) play Violins I "Stac RRx14" (already loaded) instead of "Staccatissimo RRx9". Marc LITE heads unchanged.
11. **Trumpet 1 staccato head** (A #1, partial). Every printed staccato is on 1TP "StacSs DblTng RRx9" (4,080 regions), with the critic's velocity table (top 110, under the overblow band), and `STAC_LEAD_S` is 0.02 s. Trumpet 2 stays on Sus slices because of the 45 GB cap (its dips were already 3.5 dB in the critic's measurement).
12. **Horn tenuto repeats** (A #2 fallback). `WIND_REP_RETONGUE_BY["Horn"]` changed from gap 0.1 s / frac 0.3 / fall 12 CC / 0.15 s to 0.07 / 0.25 / 8 / 0.12.
13. **Woodwind legato joins** (A #4). `auto_fills.py 3` wrote 32 early fills (Oboe 1 2, Clarinet 1 12, Bassoon 1 13, Horn 1 5). The 17 celli fills it proposed were not kept.
14. **Celli bow changes 1074 / 1077** (A #5): hand entries in `rebow_fills.json` (+7 dB at +0.17..+0.24 s, +4 dB at +0.2..+0.28 s).

Rejected / deferred:
- A #2 brass portato rows (1FH Port Shrt/Lng, 1TB/1TU Portato) and Trumpet 2's staccato row: deferred for memory (45 GB cap). The fallback (item 12) was done instead.
- C #6 (align the violin sections' staccato leads with pcx): deferred. It needs a pcx measurement pass first.
- B "other observations" (trumpet f trims, summit second winds): left as the critic advised.

parts.json: no WARNING. Loaded regions 580,383 -> 584,463 (+4,080, Trumpet 1's new row only). Opus state changes only on Trumpet 1 (a new row), so it gets a full rebuild. The other changed tracks (Flute 1, Oboe 1, cor anglais, Clarinet 1, bass clarinet, Bassoons 1-2, Horns 1-4, Timpani, Harp, Violins I/II, violas, celli) get `--midi-only` (MIDI, volume envelope and ReaEQ).

Stem fix (`tools/stem_fix.py 4 cycles/c04/build_render build --apply "Trumpet 1"`, originals in `render_first/`). Trumpet 1's pp staccatos in bars 101-103 came out +6.2 dB over c03 on the StacSs row (-44.6 against -50.8 dB RMS over qn 300-309, and 6.6 dB over Trumpet 2). A `LEVEL_SHAPES` step of -6 dB over 299.7-308.75 fixes it. The same data went into REAPER with `--midi-only "Trumpet 1"` before the quit. Then `render_cycle.py 4 --measure-only`.

## Measured (c03 -> c04; `actor_scripts/m.py`, `t.py`, `t2.py`, `h.py`, `d.py`; plain RMS unless noted)

- **G.P. (B #4, C #3).**
  - Timpani stem after the 1014 stroke, at +0.3 / +0.6 / +1.0 s: -30.2 / -38.8 / -44.9 -> -42.0 / -58.9 / -72.6 dB.
  - From qn 1017 (G.P. start), timpani at +0.3 s: -43.8 -> -71.0. Master at +0.3 / +0.6 / +1.0 s: -43.6 / -48.4 / -54.3 -> -57.0 / -67.5 / -76.8.
  - Master drop from the 1014 stroke to +0.6 s: 18.7 -> 21.6 dB.
  - The G.P. is now the strings' hall, not the drum's ring.
- **Harp, F major episode (B #2, C #5).**
  - Harp over 216-240: -33.6 -> -41.3 dB. That is about C's -6 dB and about 1 dB more than B's target.
  - Over 240-264: -42.6 -> -45.2, now 1.8 dB under Clarinet 1 (B's target was 3 dB under).
  - Delivered episode -25.6 -> -29.4 dB, now 1.0 dB under theme A (-28.4). C's target was under theme A.
- **Summit, delivered mp3 bar RMS (C #2).**
  - Bar 337: -12.9 -> -13.1. Bar 104: -14.6 -> -16.6. Bar 304: -14.2 -> -16.5. Bar 72: -15.9 -> -17.0. Bar 300: -14.9 -> -15.4.
  - Bar 337 now sits 3.5 dB over bar 104, 3.4 over bar 304 and 3.9 over bar 72 (target 2.5-3), but only 2.3 over bar 300 (target 3).
  - The coda build still rises bar by bar: bars 333-336 at -17.4 / -16.9 / -15.9 / -13.8.
- **Bassoons and bass clarinet (B #1)**, X minus Y in the same window:
  - Bassoon 2 against Violins I at 207-210: +2.3 -> -0.7 dB.
  - Bassoon 1 against Violins I at 576-588: +5.1 -> -0.7.
  - Bassoon 1 against the violas at 588-600: +0.9 -> -6.7.
  - Bassoon 2 against the celli at 630-646: +3.5 -> -7.4.
  - Bassoon 1 against Oboe 1 at 1032-1036: +5.3 -> 0.0 (target -3).
  - Bass clarinet against Clarinet 1 at 249-262: +1.0 -> -4.4.
- **Celli (B #3).** Celli against Violins I at 300-312: +3.2 -> +0.8 dB. At 1005: +5.0 -> +2.2. At 1010: +7.9 -> +5.1.
- **Violins II (B #5).**
  - 192-198: -50.5 -> -46.5 dB, now 2.2 dB over the violas and 2.1 dB under the celli.
  - 504-552: -55.4 -> -51.4.
- **Trumpet 1 (A #1).**
  - In the ff tutti the quarter peaks about +0.0..+0.02 s after the score onset (c03 +0.06..+0.1 s).
  - Each repeated eighth now has its own attack. The dip between the two eighth peaks is 2-5 dB on most heads, but the 10 ms envelope still shows no separate second peak at 325, 331 and 337 (median 2.0 dB, c03 4.1 by the same script; c03's second "peak" was the first eighth's tail).
  - Level within 0.5 dB of c03 in 312-360 and 993-1005; the pp bars 101-103 after the stem fix.
- **Horn tenuto repeats (A #2 fallback).**
  - Horn 3 at 219 / 225 / 243 / 255 / 258: 6.5 / 7.2 / 9.1 / 10.5 / 10.5 -> 5.7 / 6.4 / 4.9 / 5.4 / 5.0 dB.
  - Horn 4: 2.3-2.6 -> 3.7-3.8 dB.
  - Horn 1 at 630-663: 11.0-13.7 -> 8.4-10.9 dB (still over the 3-6 dB target).
- **Coda staccato pairs (A #3)**, median first-to-second eighth dip at 982-1003:
  - Violins II 3.1 -> 5.5 dB, violas 3.5 -> 4.9 dB, with no pair at 0 dB.
  - Master 3.3 -> 3.4 dB (pairs 985 and 1003 still at 1.7 / 1.2).
- Not re-measured this cycle: C #1 (head xcorr), C #4 (clarinet residual SD), A #4 (fills), A #5 (celli 1074 / 1077), B #6. Next critics.

## Render

- Lock: waited from 09:17 behind Movement I (held from 08:49) and Movement II's waiter, which had waited longer (turn rule). Movement II took the lock at 09:46:17 and released it within a minute. Held 09:46:55-10:17:38 (30.7 min): `--midi-only` of 18 tracks (Trumpet 1 fully rebuilt), restart, render with `--force-memory`, stem fix, `--midi-only "Trumpet 1"`, quit, unlock.
- Disk: 27 GB free at the start, 24 GB when the lock was taken (other threads' renders). Freed about 1.3 GB in this folder: c02 string stems (master kept), `cycles/c01/render_first`, `cycles/c03/render_first` (the pre-fix copies), and the old REAPER backups except the newest. The render ran at 25 GB free, under the 30 GB rule. 31 GB free after it.
- **REAPER memory**: settled at 45 GB (5 GB compressed) before the render, 9.9 GB compressed at the render's start (memory gate forced), 46 GB (28 GB compressed) after the render.
- **Master**: -20.1 LUFS integrated, LRA 23.4 LU, true peak -1.1 dBFS, sample peak 0.875 (no clipping).
- **Delivered** `cycles/c04/scherzo-mockup-c04.mp3`: -19.8 LUFS, LRA 14.3 LU, TP -1.4 dBTP, limiter about 2.5 dB, p10-to-max span 19.3 dB.
- **Attack probe**: all 20 attacks and the opening are ok.
  - The legato spread is flagged on Violins I (76 ms, limit 75; c03 75, also flagged) and on the violas (116 ms, limit 90; c03 92). The violas flag is a render-to-render artefact. Their parts.json data is identical to c03 except two coda keyswitches at 981/1002, yet the same joins at 133-162 and 590-609 measured 50-200 ms earlier (pcx per join, same leads).

Open for c05:
- Horn 1's tenuto repeats at 630-663 still dip 8-11 dB.
- Trumpet 2 is still on Sus slices, and the brass portato rows are deferred (memory).
- The master's coda pairs at 985 and 1003 (1-2 dB).
- Bassoon 1 at 1032-1044 is level with Oboe 1 (target 3 dB under).
- C #6: align the violin sections' staccato leads with pcx.
- Measure C #1 (xcorr of the alternated phrases), C #4 (clarinet residual SD), the A #4 fills and the A #5 celli bow changes.
- The violas' legato spread flip: compare once more on the next render.
