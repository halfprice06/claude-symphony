# Cycle 39: changes (actor, on the critics' reports of the c38 render, the first with the drier hall)

Snapshot before the changes: `before/`. Data the render was made from: `rendered_build/`. Script: `actor_scripts/check39.py` (c38 against c39 at every accepted finding, each render on its own tempo map).

The hall is unchanged (fx_volume 0.095, hall low cut 160 Hz, sends as c38). No Opus state changed: no row set, patch, mic or hall change on any track, so the build was `--midi-only --tempo` on all 32 tracks (the tempo map changed at qn 203.75) and no track was fully rebuilt.

## Accepted (`build/score_config.py` block "c39", `build/early_fills.json`, `build/rebow_fills.json`, `build/rebow_moves.json`)

- B #2 bars 61-62: Violins I shape +3 dB over 204.9-207.8 (205.15-207.6 full); Horn 1's c37 lift 7.5 -> 5.5 dB at 205.0-207.75 (its front and the 208-211.6 +3 kept); Violins II CC7 127 -> 95 (-2.5 dB, pre-hall) over 205.95-207.0, back to 127 by 207.6.
- B #1 bars 79-80: Violins II CC7 127 -> 76 (-4.5 dB, pre-hall) over 264.0-265.75, back at 265.8 (the 266 note starts at 265.81); Violins I's 264.417 re-bow fill +2.5 dB on every point from 0.6 s to 1.763 s (floor -6.0 -> -3.5, tail -4.4 -> -1.9).
- A #1 Trombone 1 bar 63: the c33 CC7 floors raised, 213 85 -> 110 (+2.2 dB), 215 95 -> 120 (+2.0 dB). Velocities, swells and the 218 accent unchanged.
- C #2 bar 25: `VEL_SET["Violins I"][72.0] = 124` (the v63 slow legato transition -> Violins II's v124; manual p.144: velocity sets the transition time only). The c35 re-attack lead 0.20 s kept.
- C #3 coda: early fill Violoncellos 286 {4 dB, pre 0, hold 0.25 s}.
- C #4: early fills Double basses 184 and 216, Violas 140, each {3 dB, pre 0, hold 0.12 s}.
- A #3 (S1) repeats: Violins II 289 and 292 taken out of `NOTCH_SKIP` (289 keeps its re-bow; its rebow_fills lift from +0.08 to +0.56 s scaled by 0.6, peak +9.6 -> +5.7 dB), `MERGE_NOTCH_AT["Violins II"][292.0] = 12`; `MERGE_NOTCH_AT["Violas"][62.0] = 16`, `MERGE_NOTCH_AT["Violas div"][70.0] = 16`; `REP_RETONGUE_AT["Double basses"]` 144, 156, 168, 253, 265 plus a pre-hall CC7 fall 127 -> 100 (-2.1 dB) over the last 0.12 qn into each (the re-tongue only lengthens the existing 0.03 qn gap to 0.06 qn). The re-tongue at 168 moved the basses' automatic re-bow point 166.049 -> 166.034: `rebow_moves.json` re-keyed (the fitted point 166.395 and its fill unchanged).
- A #4 join fills (drier hall): Flute 1 130 5.6 -> 7.1 dB, Flute 1 131.5 new {2.7, hold 0.2}, Flute 1 271 new {3.5, hold 0.3}, Oboe 1 143 4.4 -> 5.5, Horn 1 193 new {3.5, hold 0.3}.
- B #4 bars 66-70: Double basses +3 dB from Horn 1's entry (226.0, full by 226.5) to 237.6, back to 0 at the tutti onset 238.
- C #1 fallback: `CAESURA[204.0]` 0.22 -> 0.10 s (beat 4 of bar 60 0.487 -> 0.367 s on the tempo map).

## Rejected or deferred

- B #6 (wind and horn mics Close -> Main to soften exposed phrase ends): deferred by the coordinator. It adds room sound while Dan asked for less wet, and it changes 16 Opus states (full rebuilds). An open option to raise with Dan.
- C #1 FRESH_AT (fresh string strokes at 204): not tried. Undoing the strings' legato targets on the climax downbeat could drop them onto the legato row's slow first-note layer, and one render could not test it and its fallback both; the fallback was taken. C #6 (Violins I/II join fills at 204 if the fallback is used) left for the next critics: Violins II already has a 3.9 dB fill there, and a Violins I fill there would sit under the delivery limiter's loudest region.
- A #2 Flute 1 136 on Leg Slur Rep: a row change (full Flute 1 rebuild) and a new tool option; deferred again in favour of level/timing changes.
- A #4 Bassoon 1 256: it already has a 4.4 dB fill (c38 tried a deeper one and reverted it for overshoot); left.
- A #5 Horn 2 208 re-tongue: low priority, masked in the ff tutti.
- A #3 Violas div 79: the 78/79 E flat 4 is not merged by the string merge path that `MERGE_NOTCH_AT` acts on (no CC11 notch was written at 79 with or without the entry); left open. The Violas div re-bow moves to 289/292 wait for the Violins II result.
- B #3 (more bass at the ff climaxes: Cb loud_eq low shelf off, celli bell +1.5, tuba +1.5): not this cycle; the limiter is at 2.3 dB of its 3 dB ceiling and the B #2 and A #1 changes add level at the same climax.
- B #5 (horn 300 Hz bell): only if Dan hears the horn solos as thick; no action.
- C #5 (Horn 1 196 / Horn 3 267 level shapes): needs a stem simulation first; left.

## Measured (`actor_scripts/check39.py`, plain RMS on stems, each render on its own tempo map)

- Master: -20.3 -> -20.2 LUFS, LRA 24.6 -> 24.3, TP -1.5 -> -1.3 dBFS, sample peak 0.863, no clipping, no silent stem. Bars 61/62 -14.2/-14.8, bars 79/80 -20.2/-21.1 (the climax order holds).
- Delivered: -19.8 LUFS, LRA 15.6 -> 15.4, TP -1.6 dBTP, span 19.1 -> 19.0 dB, limiter 2.3 -> 2.2 dB. Attack probe 0 flagged. Before the lock, a stem_fix simulation of the envelope changes on the c38 stems (old tempo map) gave limiter 2.3 dB, unchanged.
- A #1 Trombone 1: the 213 accent over the 212.6 pickup (200 ms) +1.5 -> +3.7 dB (target 2.5-4); the 215 hole under 214.8 3.2 -> 1.4 dB (target <= 4); master 213.0 vs 212.6 -1.2 -> +0.3 dB (target >= +1: not quite). 2-5 kHz not re-measured.
- B #1 Violins I minus Violins II per 0.25 qn over 264.0-265.75: -1.1..-6.8 -> -0.5..+1.9 dB (positive on 7 of 8 steps; target >= +1 on every step, missed at 265.5/265.75).
- B #2 Violins I minus the loudest of Violins II, Horn 1, Trombone 2, bass trombone and celli per 0.5 qn 204-208: c38 +1.1 +0.6 -2.4 -2.5 -5.5 -3.6 -1.3 -1.7 +0.2 -> c39 +1.2 +0.7 +0.2 0.0 -0.5 +1.7 +1.8 0.0 +0.2. Violins I is now the loudest stem in bars 61 and 62 (metrics). Master over 204-208 within ±0.6 dB of c38.
- C #2 bar 25: Violins I broadband b-6 at 72 +0.12 -> +0.20 s (Violins II -0.05 both). No gain on this measure, so v124 did not bring the arrival forward. The next critic should measure own-pitch and decide between keeping it and cutting the c35 lead.
- C #3 celli 286 b-6 +0.245 -> +0.025 s. C #4 b-6: basses 184 +0.110 -> +0.030, basses 216 +0.125 -> +0.035, violas 140 +0.115 -> +0.025 s.
- A #3 repeats (dip / re-attack, dB, c38 -> c39): Violins II 289 4.9/3.0 -> 4.9/0.9 (the scaled fill lowered the re-attack); Violins II 292 1.3/1.9 -> 2.9/1.7; violas 62 1.4/3.2 -> 1.4/2.4 and Violas div 70 0.0/2.5 -> 0.0/2.3 (the 16 CC notch had no measured effect); basses 144 -0.4 -> 1.4 dB dip, 156/168/253/265 unchanged (2.5, -0.4, 1.2, 4.1). The basses' re-tongue plus the CC7 fall did not open the repeats. S1 on the basses and violas is still open.
- A #4 join holes (200 ms): Flute 1 130 6.1 -> 5.2, 131.5 5.5 -> 3.2, 271 2.8 -> 1.9, Oboe 1 143 6.0 -> 5.3, Horn 1 193 4.5 -> 4.1 dB; 30 ms peaks over the louder body at most +2.5 dB (Flute 1 130).
- B #4 Horn 1 over the basses per qn 226-235: 14.1-17.7 -> 11.9-14.7 dB at 226-229 (target 11-15). Bar 66 niente in the master 7.2 -> 7.2 dB.
- C #1 fallback: beat 4 of bar 60 0.487 -> 0.367 s. Master dip into 204 1.5 -> 1.3 dB.

REAPER: 44 GB settled before the render (0 compressed, no `--force-memory`, 2 min settle after the restart), 45 GB with 27-29 GB compressed after the render. Lock held 13:27:49-14:04:39 (37 min). The wait behind Movement I and the finale (mvt3) ran from 11:21 to 13:27; under the turn rule mvt3, already waiting, went first. No stem fix.
- loop/ONE_TIME.md appeared during this cycle; the coordinator said it is for c40, so it was left in place and not acted on.
