# Cycle 36 (actor): changes on the c35 render's critic reports

## Changed
- **C #2 Horn 1 bar 61 front.** `build/roles.json` Horn 1 row `[203.95, 208, 4.5, 0.25]` removed; `build/score_config.py` `LEVEL_SHAPES["Horn 1"]` 203.95: 0, 204.15: -1, 204.6: 0, 205.0: +4.5, 207.75: +4.5, 208.0: 0. Horn 1 50 ms max over 204.0-204.8 -20.6 -> -25.9 dB (Horn 2 -28.9; body 205-207 -29.5, unchanged); master max frame -12.7 -> -13.5 dB; bar 61 mean unchanged (-15.4); delivery limiter 2.5 -> 2.0 dB.
- **B #2 timpani f roll bars 61-62.** `LEVEL_SHAPES["Timpani"]` +5 dB 204.05-209.4 (release before the 209.5 stroke). Roll 204-209.4 -38.8 -> -33.8 dB.
- **B #1 bar 28.** Celli shape -5 dB 81.1-81.65, +4 dB 81.9-82.6, back to 0 by 83.2 (slow release, no fast post-hall fall): 81.15-81.9 -33.0 -> -37.0, 82.15-82.9 -39.7 -> -36.0 (the f arrival is now 1 dB over its approach). Violas main: `ART_SPANS` Sus MAX 80.95-82.5 (81 and its printed repeat at 82; a Leg Slur MAX repeat at 82 would hit the same slow layer), `REATTACK_LEAD_AT["Violas"][83.0] = 0.12` for the new slur's F4 after the row change. Violas 81.1-81.8 -52.7 -> -45.2 (80 body -42.3, Violas div F4 -40.6), 82 -46.9 -> -46.5, 83 -38.5 -> -37.5.
- **A #3 violas 248 / 252.5.** New generic option `MERGE_JOIN_OWN_SLUR_AT` in `tools/score_to_parts.py` (default `{}`): a listed note that absorbs the next slur's same-pitch first note keeps its own slur, and the absorbed slur's next note joins on from it (bc_from, Leg Slur MAX, no extra notch). Movement II: `{"Violas": [248.0, 252.5]}`; `REATTACK_LEAD_AT["Violas"][252.5]` removed. parts.json: 248 now a led legato target (247.805, v124; was 248.0 v37), 252.5 at 252.30 v124 (was v49); the following notes keep their joins. Stem 248.05-248.45 -57.2 -> -46.0 dB (G3 before -48.3); minimum at the 248.5 bow change about 10 dB under (30 ms window).
- **A #1 basses re-bows (bar 66).** `build/rebow_fills.json` "Double basses" 225.215 +3.5 dB over 0.0-0.92 s, +5 over 0.96-1.32 s, +2.5 at 1.36 s; 221.8 +3 over -0.04..+0.28 s (cap 9). 225.215: stem 0-0.9 s -53.9 -> -50.4 (pre-re-bow -50.4), 1.0-1.3 s -57.8 -> -52.8; master 0-0.9 s -52.5 -> -49.7 (pre -48.8: dip 4 -> 0.9 dB). 221.8 0-0.4 s -56.6 -> -55.0.
- **B #3 Clarinet 2 pp.** `build/mix.json` `soft_trim_db` pp 5.1 -> 2.6, ppp 2.3 -> 1.0: bars 3-6 -47.6 -> -50.1, 238-250 -47.3 -> -49.8, 292-304 -51.7 -> -53.7.
- **B #4 harp 253.** `build/note_trims.json` Harp "253": -4.5: 253-253.5 -34.8 -> -39.3 (251 -39.3, 257 -37.7).
- **A #2 Flute 1 136.** `MERGE_NOTCH_AT["Flute 1"] = {136.0: 14}` (CC11 26 -> 20 at the repeat). No measured effect: notch minimum -56.6 -> -56.7, master unchanged. Open (see below).

Tracks rebuilt `--midi-only`: Flute 1, Clarinet 2, Horn 1, Timpani, Harp, Violas, Violoncellos, Double basses. No Opus state change. parts.json: no warnings; the only note changes are the violas' (pdiff).

## Rejected / deferred
- **C #1 violas sextuplets on Detache (bars 59-60).** Rejected: series 1 tested exactly this (mockup-kit LEARNINGS §5/§7, c14-c16: Detache own-pitch share 0.32 against 0.32 for Sus MAX on these 0.157 s notes; Leg Slur and the Stac Leg rows no better). Only a dedicated runs patch or the Slur Runs row (violins only) is left.
- **C #3 Horns 3-4 a2 on the a2 track.** Deferred: the a2 track reads staff Hn1 only (one source per track in `TRACK_WINDOWS`/`TRACK_SPLITS`); routing Hn3 to it needs a multi-source window option and a level refit.
- **C #4 basses 4 soli on DIV A (MANUAL-GAPS #8).** Deferred: a 33rd instance and a refit of every basses fill in 220-238 and 286-304; critic B measured the level on target.
- A #1's alternative (DIV A) as above.

## Render
- Lock 06:21:33-06:46 (25 min). REAPER started fresh, built, restarted, Audio_Init (48000/512, no input), `render_cycle.py 36` without `--force-memory` (32 GB, 0 compressed at the render start).
- Master -20.3 LUFS, LRA 23.9 LU, TP -0.8 dBFS (c35 -0.3), sample peak 0.907, no clipping. Delivered: -19.8 LUFS, LRA 15.3, TP -1.6, span 18.3 dB, limiter 2.0 dB (c35 2.5; stem_fix simulation predicted 2.0). Attack probe: 0 late or holes.
- Climax order: bar 61/62 -14.3/-15.0, 79/80 -19.4/-19.9 (unchanged).
- Unchanged tracks were not sample-exact against c35 this time (Oboe 1, Horn 2 exact; Violins I/II, Bassoon 1, Horn 3, Violas div with a median 0.0 dB difference and a few 0.5 s windows 1-5 dB apart, all at soft levels, e.g. Violins II -50..-62 dB at qn 218). The render started while REAPER was still at 32 GB (45 GB after). Not a broken render; no stem fix needed.
- REAPER memory after the render: 45 GB (27 GB compressed).
