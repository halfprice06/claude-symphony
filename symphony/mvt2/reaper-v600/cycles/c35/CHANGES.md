# Cycle 35 (actor): changes on the c34 render's critic reports

Snapshot of the tools and data before the changes: `before/`. Data the render was made from: `rendered_build/` (the two fills lowered after the render are in `build/` and in REAPER via `--mix-only`).

## Changes

Tool: `tools/score_to_parts.py` new generic options `REATTACK_LEAD_AT = {track: {score onset: s}}` and `REATTACK_LEAD_S = {family: s}` (default off), `REATTACK_MIN_S` 0.4: a re-attack straight after the previous note (written end within 0.10 qn) that no other lead branch moved (or moved less) starts that many seconds early, at most 0.45 of the previous note's played slot; the notes before end 0.02 qn before the moved onset (the re-attack stays a first note); CC11 holds from the moved onset. parts.json `reattack_leads`; a listed onset with no note or no abutting note prints a warning.

Config (`build/score_config.py`, block "c35") and tables:
- A #1 (bar 63 "trem. sf"): c34's climax hold on Violins I (+3) and the celli (+3.5) now ends 211.0 -> 211.5 (was 211.6 -> 211.9); Violins I's c31 CC7 lane at 212.0/212.025/212.063 84/94/112 -> 127/127/118 (no dip at the sf head; the c31 shape that held vol_db at the 211.9 level is unchanged); sf weight `LEVEL_SHAPES` +2.5 dB on Violins I and celli at 211.98-212.5 (falling with the CC7 fall). Not recomputed with `a2cc7.py` (it reads the already compensated vol_db; its reference 211.9 is after the hold).
- A #2 (bass clarinet pedal, BRIEF 8): the four c28 roles 8-16.75 replaced by one `LEVEL_SHAPES` curve that steps with each c34 piece (-1/-4/-9.5 on the first piece's swell, -3 from 10.03, -5.5/-6 on the second piece's swell, -3 from 13.53).
- A #3: `early_fills.json` Violins II 206 {db 5, pre 0.1, hold 0.05} (hold 0.15 simulated +2.8 dB on the note's bloom at +0.25 s).
- A #4: violas bar 41 role [123.6,125.95,-4,0.3] -> shape -4 at 124, -3 at 124.95, +1.8 over 125.05-125.9, -1.5 at 126, 0 at 127.9 (fitted on simulation to a monotone crescendo).
- A #6: timpani 172 stroke +3 dB (shape 171.99-172.5).
- B #1: Clarinet 1 role [279.9,291.9,-2,0.5], note trim 286 4 -> 2.5; cor anglais role [285.9,292.5,2,0.5].
- B #2: violas +2.5 over 204.2-207.8 (+1 to 211.6) and 259-265.6 (+1 to 267.75); Violas div +1 over 266-267.75.
- B #3: `pitch_trims.json` Horn 3 `_skip_onsets` [262, 265] (F4 -5 copied from Horn 1).
- B #4: Flute 1 +5 dB over 134.3-138 (3 dB to 139, 0 by 139.5).
- B #5: Bassoon 2 role [90.4,96,-3,0.4]; celli -7 over 139.5-140.15 (transition head under Oboe 1's pickup); Oboe 1 note trim 139 +2.
- C #1: `REATTACK_LEAD_AT` with the critic's start values (Vln I 249/72, Vln II 218, Va 218/252.5/266, Hn1 208/210/196, Hn2 210, Hn3 210/267, Ob1 210, Ob2 267, Fl1 116, Bn1 144/198/261, Cl2 256); Violins II 218 entry fill {4, 0, 0.15}; dead `leg_leads` Bassoon 1 198 removed; `rebow_moves.json` Violas 263.900 re-keyed to 263.833 (the 266 lead shortened the held B flat 4 and moved its automatic re-bow point; fitted fill kept).
- C #2: `leg_leads.json` Fl1 200 0.10 -> 0.20, 118 0.08; Ob1 271 0.12, 145.5/146 0.05; B.cl 30 0.15; Cl2 244 0.12; Vln II 80 0.08 -> 0.18; Vln I 80 0.10; Vc 240 0.08; Hn1 176 0.08.
- C #4: entry fills Violins II div 108 {4,0,0.20}, Violas div 78 {3,0,0.12}, 81 {5,0,0.15}, 84 {3,0,0.12}, Violoncellos 238 {4,0,0.15}, Violins I 292 {3,0,0.15} (simulated peaks -0.8..+2.2 dB over body).
- After the render (stem fix on 2 stems + `--mix-only`): Violas 266 fill 6 -> 2.5 dB, Bassoon 1 261 6 -> 1.7 dB (both peaked 6.0/6.8 dB over the body once led).

Build: no Opus state changed (no new rows, mix.json unchanged); `--midi-only` on 19 tracks, no full rebuilds.

## Rejected or deferred

- A #5 (basses 4 soli on DIV A, MANUAL-GAPS #8): a 33rd instance plus a refit of every basses re-bow fill in 220-238/286-304; level already on target (B); deferred, recorded in MANUAL-GAPS.
- C #3 (tutti breath at 204 as fresh string strokes): needs a new generic FRESH_AT rule and an A/B with a fixed pass test; deferred so this cycle's timing changes can be measured alone.
- C #5 (CC70 finger positions for the "sul D" pickups): changes CC70 inside legato phrases (join-time risk the critic names); deferred.
- `REATTACK_LEAD_S` family values not set: only the measured onsets are led (a family rule would move many fitted notes at once).
- Violins II 80: `leg_leads` 0.18 had no effect (the moved onset stayed at 79.775: the lead is at its clamp); Vln I 80 now moves with it.

## Measured (c34 -> c35; stem RMS dB, windows in score qn)

- A #1: sf (212.0-212.3) minus 211.2-211.8: Violins I -3.6 -> +2.2, celli -1.6 -> +3.3, Violins II +5.7 (unchanged; now 0.5 dB over Violins I instead of 4.2); master -0.8 -> +0.8.
- A #2: bass clarinet half-qn levels 6.5-16.5 against 6.4-7.6: max deviation 5.0 -> 1.0 dB.
- A #4: violas bar 41 per beat -54.8/-56.7/-47.4/-46.8 -> -54.2/-51.5/-48.7/-47.3, bar 42 -45.1.
- A #6: timpani stroke over the roll's end 0 -> +3.0 dB.
- A #3: Violins II 206 join dip 9.1 -> 4.2 dB, b-6 +0.115 -> +0.09 s.
- B #1: Clarinet 1 280/283/286/289 -46.2/-41.9/-41.6/-44.3 -> -48.2/-43.9/-45.0/-46.3; cor anglais 286/289 -48.6/-49.4 -> -46.6/-47.4 (clarinet leads the duet by 1.6/1.1 dB); master 280-292 -1.2 dB.
- B #2: violas (+div) minus Violins II (+div) at 204/208/259/262/265: -4.8/-1.7/-4.1/-5.4/-2.0 -> -2.7/-0.6/-2.0/-3.0/-0.5.
- B #3: Horn 3 262/265 -36.9/-37.7 -> -33.0/-34.1 (Horn 4 -32.7/-34.0).
- B #4: Flute 1 minus cor anglais 134-138: -8.0/-13.1/-11.8/-10.9/-5.7 -> -3.7/-8.1/-6.8/-5.9/-2.3.
- B #5: bass clarinet over Bassoon 2 on the bar 31 eighths +1.2/+3.3/+7.7/+5.5 -> +4.2/+6.3/+10.7/+8.5; Oboe 1 minus celli at 139.4-139.9 -8.1 -> +0.3.
- C #1/#2 (own-stem envelope, body - 6 dB from the score onset; rough where the previous note still sounds): Vln I 249 +0.10 -> +0.02 (Vln II +0.005), Vln I 72 +0.225 -> +0.12, Vln II 218 now -0.015, Va 252.5 +0.315 -> on time, Horns 1/2/3 210 +0.15/+0.17/+0.115 -> +0.04 each, Ob1 210 +0.265 -> -0.045, Ob2 267 +0.23 -> -0.095, Bn1 198/261 +0.18/+0.185 -> -0.01, Cl2 256 +0.12 -> -0.08, Fl1 200 +0.175 -> +0.075, Ob1 271 +0.20 -> +0.015, B.cl 30 +0.18 -> +0.045, Cl2 244 +0.11 -> -0.03, Vln I 80 +0.165 -> +0.085. Not improved by this measure: Bn1 144 (+0.19 -> +0.23), Hn1 196 (+0.17), Hn1 176 (+0.10 -> +0.16), Vc 240 (0.0 -> +0.125). Peaks: Ob2 267 5.5, Ob1 210 4.9, Vln I 249 4.5 dB over body (no fill; for the next critics).
- Master -20.3 LUFS (c34 -20.5), LRA 23.8, TP -0.3 dBFS, sample peak 0.962 (no clipping); bars 61-62 -14.3/-15.0, 79-80 -19.3/-19.9 (climax order kept). Delivered: -19.8 LUFS, LRA 15.2, TP -1.4, span 18.3 dB, limiter 2.5 dB (c34 2.6; the stem_fix + deliver simulation before the render predicted 2.5). Attack probe 0/20 flagged. All 32 stems sound.
- REAPER: fresh open settled at 44 GB, 0 compressed (no `--force-memory`); 44 GB (4.7 GB compressed) after the render. Lock held 05:30:28-05:52:46 (22 min), after waiting 37 min for the Movement I thread.
