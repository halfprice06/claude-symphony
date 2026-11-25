# Cycle 43: changes (actor; critics A/B/C on the c42 render)

- Snapshot before the changes: `before/`. Scripts and logs: `actor_scripts/`.

## Changes

- **A #1, basses at soft pitch changes.**
  - `build/mix.json`: Double basses `sus_release_cap_ms` pp/p 600 -> 400 ms. The other string tracks keep 600. This is a basses-only Opus state change, so the basses get a full rebuild.
  - `build/rebow_fills.json`: the "Double basses" rows go back to `cycles/c42/before/rebow_fills.json`, c41's final rows. They were fitted on the 400 ms render and re-levelled with relevel41.py.
  - `build/score_config.py`: `ABUT_LEAD["Double basses"]["force_at"]` = [152, 204, **286**]. The coda's F 1 gets the 0.16 s lead (285.903), and the pedal's last piece ends at the moved onset.
  - That lead shortened the 271-286 pedal, which moved all five automatic re-bow points (273.229 -> 273.209 ... 283.605 -> 283.489). That left the fills and rebow_moves with no re-bow at their keys (score_to_parts WARNINGs). So the pedal is now in `AUTO_REBOW_SKIP`, and its c42 points [273.229, 276.05, 278.351, 282.203, 283.605] are listed in `REBOW_AT`. The split is the same as before; only the last piece's note-off moves.
- **C #1, clarinet legato leads (S2).** `LEG_LEAD_S`: "Clarinet 1" 0.03 -> 0.07 s (a new key placed before "Clarinet"), "Bass clarinet" 0.05 -> 0.09 s.
  - `build/leg_leads.json`: Bass clarinet 30 0.15 -> 0.11 (keeps its 0.20 s total), 32 +0.12, 108 +0.10, 26 +0.06; Clarinet 1 258 / 259 +0.10.
  - The increases are a little under the measured lags (+56 / +72 ms), because the kit says the response to added lead is often more than 1:1.
- **B #1, bar 62 sample swell (limiter).** LEVEL_SHAPES over 210-212: Horn 2 -4, Horn 3 -3, Double basses -4 (the basses' shape ends at 211.75, before the c41 +1.5 role and the 212 sf).
- **B #2, soft end of the span.** `build/roles.json` +1.5 dB on Violins II, Violoncellos and Double basses over [219.9, 225.9], with a 0.5 qn ramp. +2 dB on Harp harmonics, Violoncellos div, Violoncellos, Double basses and Violas div over [273.9, 283.0], with a 1 qn ramp.
- **B #3:** Harp -2 dB over [17.9, 44.0] (bars 7-14, under the horn solo).
- **B #4:** Violoncellos -2.5 dB over [291.9, 300.9] (the coda A flat over Violins I's C5).
- **B #5:** Horn 1's 182 shape: c42's +2 becomes -1.5 on the head and +3.5 on the body.
- **B #6:** Cor anglais role [93, 98.5, +2] -> [93, 96.0, +2, 0.5], so the lift releases into the bass clarinet's mf.
- **C #2 (S2):** Horn 1 196, a front-loaded LEVEL_SHAPES_S lift: +5 dB at -0.08 s, +4 at 0.25 s, 0 at 0.7 s.
- **C #3 (S2):** Violas 238, a front-loaded LEVEL_SHAPES_S lift: +8 dB at -0.17 s, +6 at 0.10 s, 0 at 0.45 s.
- **A #3 (S1), generic, `tools/score_to_parts.py`:** a same-pitch DOWNBOW_STROKE_AT stroke after a legato note now also gets the `STR_REP_NEW_BOW["sus_fall"]` CC11 fall. Violoncellos 66 gets 8 CC (32 -> 24 at 65.94).
- **A #4 (S2):** Violas 164.5 / 166.5 entry leads +0.08 -> +0.18 s in `build/entry_leads.json` (total 0.30 s, the cap). REATTACK_LEAD_AT does not apply to notes after rests.
- **A #5 (S3):** the timpani's post-hall notch before the p stroke at 172 (14 -> -4 dB for 0.05 qn) and before the 262 f roll (8.7 dB) are filled with LEVEL_SHAPES. The envelope now runs 14.05 / 12.0 / 11.4 dB into 172 and 17.5 / 17.5 / 16.0 into 262.
- **C #4, generic, `tools/score_to_parts.py` (`TIED_SLUR_SUS_WINDS`, default True):** when a wind/brass slur starts on the tied continuation of a note outside any slur, that note becomes `slur_start_sus` and overlaps the slur's next note by LEG_OVERLAP. Only Horn 4 265 changes (end 268.0 -> 268.04). Flute 1 208 gets the flag but no note change (its sost_sus branch comes first).

## Before the render

- parts.json against c42 (`pdiff.py`): the changes are only on the tracks and onsets listed above. No WARNINGs.
- Simulation of the level changes on the c42 stems (`stem_fix.py 42 before build`, then `deliver_master.py`; `actor_scripts/stemfix_sim.log`): delivered span 19.0 -> **18.7 dB**, limiter 2.6 -> **2.3 dB**, LRA 15.5, -19.8 LUFS. The loudest pre-limiter peak moved from 232.33 s (+1.06) to 234.43 s (+0.76).
- Opus state change: Double basses only (full rebuild). `--midi-only` on Cor anglais, Clarinet 1, Bass clarinet, Horns 1-4, Timpani, Harp, Violins II, Violas, Violoncellos, Harp harmonics, Violoncellos div, Violas div.

## Render (third attempt, 2026-11-08)

- The first two attempts stopped on disk: 24 and 26 GiB free when the lock came (`NOTES-interrupted.md`). Dan then freed space (94 GiB).
- Lock 13:09:02-13:46:57 (38 min), taken after the turn rule (the finale c06 went first).
- Sequence: restart; settled at 44 GB in about 12 min (flat 2 min); the 16-track build (the basses rebuilt fully, about 3 min); restart; settled at 44 GB with 0 compressed; disk 88 GiB; audio 48000 Hz / 512, no input (after `_c43_audio_init.lua`); `render_cycle.py 43` with no `--force-memory`.
- After the render: Violins I fully rebuilt (see the state check); quit; unlock. REAPER after the render: **45 GB, 19 GB compressed**.
- Data the render was made from: `rendered_build/`, equal to `build/`. No stem fix.

## Measured (c42 final -> c43; `actor_scripts/check43_c42.txt`, `check43_c43.txt`)

- **Delivery.**
  - Master -20.4 LUFS, LRA 24.1 LU, TP -1.3 dBFS, sample peak 0.856.
  - Delivered `cycles/c43/mvt2-mockup-c43.mp3`: -19.8 LUFS, LRA 15.5 LU, TP -1.6 dBTP, span 19.0 -> **18.6 dB**, limiter 2.6 -> **2.1 dB**. The simulation predicted 18.7 / 2.3.
  - Attack probe 0 late or holes. 32 stems, no clipping.
- **A #1, basses' old pitch at +0.35 s from the score onset** (unique old harmonics vs the new pitch's harmonics, CC11 52 or lower, 48 changes):
  - 286 **-0.7 -> -13.7 dB**; 246 -9.5 -> -12.0; 220 -9.1 -> -11.4; 292 -24.9 -> -36.1.
  - Median -24.9 -> -25.7, worst -0.7 -> -4.5 (62: -9.6, c42 about the same). 11 changes are still above -15 dB on this stricter measure, mostly the semitone/tone steps at 62/63/159.
- **C #1, legato joins (`tools/pcx.py`):**
  - Clarinet 1 pcX median **+56 -> +12 ms** (robust SD 16).
  - Bass clarinet **+72 -> +33 ms** (just outside C's ±30).
  - Joins over 90 ms or under -60 ms: 11 -> 1 (Clarinet 1 194, +120 ms); none early.
- **B #1, bar 62** (dB per 0.5 qn at 210-212): Horn 2 -24.1 / -22.2 -> -28.0 / -26.2, now 3.6-4.5 dB under Violins I. Basses -24.9 / -22.3 -> -28.9 / -26.3. The limiter peak at 232.33 s is no longer in the top five.
- **C #2, Horn 1 196:** the front -37 / -36 -> -32 / -32 dB. Horn 1 minus Violins I at 0 / 0.2 / 0.4 / 0.6 s: -5.2 / -4.7 / -7.9 / -1.2 -> 0 / -0.6 / -2.7 / +1.6. The peak over the body is not above it.
- **C #3, Violas 238:** -60.5 / -57.4 -> -53.6 / -50.8 dB at -0.05 / 0 s; the maximum is unchanged.
- **A #5, timpani before 172:** the 40 ms hole -57.8 dB (13-14 dB under the roll) -> -44.1 dB, level with the roll.
- **Not effective:**
  - A #3, Violoncellos 66: the 8 CC fall is written (65.94), but the stem dip is unchanged (0.4 -> 0.5 dB, c39 measure) at this level.
  - C #4, Horn 4 268: with the 0.04 qn overlap the join played state B (first-note layer, G3 band -6.1 / 4.4 / 10.7 against 9.2 / 12.4 / 13.2), not state A. The overlap does not fix which state plays (inaudible in the master; C).
  - S1 own-band checks were not repeated. The stem dips on the listed repeats are unchanged within 0.1-2 dB (Violas 69 5.8 -> 3.9, no data change: render variation).
- **State check** (`actor_scripts/state_check.txt`, against c42): no state (level) runs. One timing run on Violins I (not rebuilt this cycle): qn 261.83-266, 4 notes, level median -0.3 dB, pcX ±50-104 ms in both directions, median -2 ms. Following the coordinator's rule, Violins I was fully rebuilt while I held the lock (`build_vln1.log`); the next render shows whether that holds.

## Rejected or deferred

- B #3 second part, MANUAL-GAPS #4 (Mid mics): for Dan (coordinator note); mics unchanged.
- A #4 second part (velocity alternation on the A3 portato): not tried.
- C #5 (CC11 tail hold in rests): inaudible now (stems 12-25 dB under the master); deferred.
- A #2: the S1 own-band test is noted for critics; no data change.
- MANUAL-GAPS: none tried (lean cycle).
