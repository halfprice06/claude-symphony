# Cycle 3: changes (render of c03, reviewed by the critics of c04)

Inputs: critic reports A (articulation), B (balance), C (timing) on the c02 render, and `loop/ONE_TIME.md` (find the cause of the 0.09-0.25 s "envelope lead"; now `loop/ONE_TIME.done.md`). Snapshot before the changes: `before/`. One render from a freshly restarted REAPER (`--midi-only --tempo` on all 32 tracks; Bassoon 1 and Double basses fully rebuilt because they load a new row), then one level-only stem fix (below). First render: `render_first/`, `metrics_first/`, `render_first_delivery.mp3`; `render/`, `metrics/` and `mvt1-mockup-c03.mp3` are the fixed version, and the REAPER project matches it (`--mix-only` on the three tracks, saved).

## The one-time task: cause of the "envelope lead" (C #4, A #1)

Cause: `build_reaper.tempo_job` gave the pre-roll tempo marker the score's 4/4. The 3 qn pre-roll was then an incomplete bar, and REAPER moved the score's first marker (50 bpm) from 3.0 s to the next barline at 4.0 s (the .rpp read `PT 4.000 50`). The later markers were placed by time, so REAPER's quarter-note count ran 1/6 qn ahead from score qn 1 on, and every note, CC, keyswitch and envelope point written at qn + 3 sounded 1/6 qn early: 0.079 s at 126 bpm, 0.2 s at 50. Notes and envelopes moved together, so it was not plugin delay compensation and not an envelope fault. The build log had listed about 330 tempo-marker mismatches since c00.

Fix (`tools/build_reaper.py`): the pre-roll marker gets its own meter (3/4 for 3 qn), and the build stops if any marker is off its qn. Read back after the build: markers at 0 s (60 bpm, 3/4) and 3.000 s (50 bpm, 4/4); `TimeMap2_QNToTime` at score qn 100 and 712 equal the parts.json map to 1e-6 s; mismatches [].

Measured (first audio after at least 1.5 s of digital silence minus the parts.json note-on, 302 entries): c02 median -0.082 s, c03 median +0.000 s (p90 +0.0004; p10 -0.19 are entries with leads).

Old renders: `tools/rendermap.py` + `build/render_shift.json` map a score qn to its file time in c00-c02 (q * 60/60 up to qn 1, then q2s(q - 1/6)). `fit_rebows.py`, `auto_fills.py`, `fit_loops.py`, `measure.py`, `probe_attacks.py` and `stem_fix.py` use it.

## Changes

Data refitted on c02 with the corrected map:
1. `build/rebow_fills.json`: refit by `fit_rebows.py 2 ... --hold-max-after 720:0` (A #1 step 3).
2. `build/early_fills.json`: all 86 entries moved 1/6 qn later (seconds at each onset's tempo): pre_s - L (negative = starts after the onset; new support in `score_to_parts.py`), hold_s + L. The `auto_fills.py` pass was not run: several lead tables changed in this cycle (below), so new fills fitted on c02 would be misplaced. Run it on c03.
3. `build/loop_profiles.json` (A #3): Timpani 0, 720, 484, 48 and Horn 4 720 fitted by `fit_loops.py` on c02 (periods 3.30-3.90 s, ±3 dB). The Bass clarinet 492 note was skipped (autocorrelation 0.20 at 3.45 s).

Tools (`tools/score_to_parts.py`, generic, defaults there):
4. Cross-section re-bow spacing (A #2): new `tools/space_rebows.py` writes `build/rebow_moves.json` (automatic point -> moved point; local search, nearest valid spot at most 1.5 s away, 0.6 s from every other section's point, pieces 1.2-4.5 s). It moved 30 of 97 automatic points and moved their fitted shapes with them (plus 7 cello shapes whose points moved with their notes after the lead change). Four pairs stay under 0.6 s, three on the final chord (Vln II/Cb 714.5, Cb/Vln I 722.7, Vln II/Cb 724.8, Vln II/Vln I 726.4): the last bar at 30 bpm has no room for 10 points 0.6 s apart with pieces of at least 1.2 s. parts.json `rebows` rows now carry the piece start and the automatic point.
5. `SHORT_SUS_JOIN` (C #1): the last Sus MAX eighth of a fast slur that overlaps the next legato note makes that note a legato target (legato lead and velocity; Leg BC MAX across a slur boundary, via the bow-change pass). Notes newly led: Vln I 18, Vln II 5, Vla 11 (the celli's count is mixed with their lead change); of these, moved from Leg Slur MAX to Leg BC MAX: Vln I 13, Vln II 4, Vla 6, Vc 3.
6. `ENTRY_LEAD_ART_S` (C #2): extra entry lead by articulation, wind Leg Slur MAX / Leg Slur +0.11 s, Sus Non Vib +0.07, brass Leg Slur MAX +0.06; bassoons none.
7. `TIMP_DELAY_S = 0.06` (C #3): timpani strokes and roll starts start 0.06 s after the score onset (ends moved too; CC7 and volume shapes stay). `PERC_MAP` `delay_s`: crash and tam-tam +0.05 s.
8. `ART_SPANS` (A #5, A #6 tests): an articulation over a listed span, with velocity and length options.
9. `probe_attacks.py`: searches from 0.3 s before the onset (early notes read negative); Timpani limit 0.12 s (`build/probe.json`).

Config (`build/score_config.py`, `build/*.json`):
10. `CAESURA = {636: 0.15}` (C #6, the tutti breath before the fff), `BEAT_STRETCH = {679: 0.6}` (bar-170 fermata rest 1.5 -> 2.5 s). Suspended cymbal `lead_s` 0.45 -> 0.25 (the crash is now 0.05 + 0.15 s later; C asked +0.05, which has the wrong sign): planned peak 0.034 s before the crash, as in c01.
11. Legato leads (C #5, from the axis-independent "relative to the other sections' attacks" numbers only): `LEG_LEAD_S` Oboe 0.06 -> 0.03, Cor anglais 0.08 -> 0.05, Clarinet 0.03 -> 0, Horn 0.10 -> 0.06; `LEG_ART_EXTRA_S` Violoncellos Leg BC MAX -0.06; Oboe 1 (77, 75) pair 0.10 -> 0.05. Kept: the Leg Slur extras and movement II's per-pitch tables (C's absolute numbers for them carry the 1/6 qn axis error).
12. `ART_SPANS` tests: Bassoon 1 staccato notes, qn 348-360, on Stac DblTng RRx9 at velocity +10; Double basses qn 104-112 on Marc Shrt RRx4, v96/104, full written length.
13. `roles.json` (B #1, #3, #4): Clarinet 1 [504,520,+5] [252,262,+3]; Horn 4 [504,518,-4,2] [248,268,-4]; Timpani [504,518,-3,2]; Vc and Cb [508,516,-2,2]; Tuba [440,456,-5,2]; Horn 3 [248,268,-4]; Bassoon 2 [252,264,-3]; Tbn1/Tbn2/BTbn [324,332,-3]; Horn 1 [104,112,-3] [464,472,-2]; Trumpet 3 [456,464,-3].
14. `pitch_trims.json` (B #2): Horn 3 72 -5 (all arts); Flute 2 87 -5, 89 -3, 91 -6; Clarinet 2 68 +4; Cor anglais 69 -5; Tuba 40 -4.
15. `mix.json`: B #5 ff trims (Cl1/Cl2/BCl -3 -> 0, Bn1 -0.5 -> 2.5, Bn2 0 -> 3, Cbn -2 -> 1); A #4 Violins II `loud_eq` over qn 584-619 (high shelf 2.5 kHz -7 dB, bell 1.2 kHz -2 dB).

## Stem fix after the render (`stem_fix.py`, roles only)

- Clarinet 1 [628,644,-3]: the ff trim change put Clarinet 1 3-5 dB up in the fff climax, and the master's top peak (1.40 at qn 637.9, limiter 2.8 dB) carried it.
- Violins II [584,619,+2]: the sul tasto EQ lowered the passage 2.1 dB (A's criterion ±1.5).
- Double basses [104,112,-6]: the Marc Shrt test played 6.6 dB louder than Sus MAX.
Simulated and applied: master peak 1.400 -> 1.369, delivered limiter 2.8 -> 2.7 dB, LRA 15.3 LU.

## Measured before (c02, on the corrected map) / after (c03)

- **Delivery**: master -17.5 -> -17.2 LUFS, LRA 21.0 -> 21.4 LU, sample peak 1.220 -> 1.369 (float stem sum; the 24-bit render clipped). Delivered -19.7 -> -19.7 LUFS, LRA 15.2 -> 15.3 LU, p10 span 19.9 -> 19.9 dB, limiter 1.9 -> 2.7 dB, -1.7 dBTP. Motion (mp3 dS4 p90 / 1s-20s) 8.70/4.56 -> 8.78/4.76.
- **Climax order** (master per bar): bar 160 -11.4, 161 -11.8, 122 -12.6, 169 -16.6, 82 -16.1: unchanged order. The top master peaks are all in bars 160-161 (1.37 at qn 637.8, 1.10 at 643.8).
- **Re-bows** (80 ms window: dip under the 0.5 s before / steps of 3 dB or more 1-2 s after): median dip Vln I 7.3 -> 2.8, Vln II 3.1 -> 2.8, Vla 3.7 -> 2.1, Vc 3.7 -> 2.7, Cb 2.8 -> 1.0 dB; p90 9.2/6.1/9.4/7.3/6.1 -> 5.0/5.2/3.8/5.9/4.5; steps >= 3 dB Vla 5 -> 3, Vc 7 -> 7, Cb 12 -> 5. Celli 37.37 dip 5.5 -> 5.7 dB (A's limit 6).
- **Final chord** (qn 704-728, master): dip at re-bows median 2.1 -> 2.0 dB (p90 4.1 -> 3.2) against 1.7 at control times; pairs of sections re-bowing within 0.6 s 16 -> 5 of 30.
- **Loop pulse** (detrended level folded at the period, p95-p5 / autocorrelation): Timpani 0 3.8 / 0.93 -> 1.5 / 0.76; Timpani 720 4.1 / 0.71 -> 2.6 / 0.63; Timpani 484 2.8 -> 1.2; Timpani 48 2.8 -> 1.5; Horn 4 720 5.5 / 0.76 -> 1.7 / -0.08. The level swing passes on Timpani 0; the timpani autocorrelation stays over 0.3 (a smaller pulse at the same period; the colour cycle is not addressed).
- **Timpani against the band** (19 Allegro tutti strokes; stroke minus the other tracks' -6 dB arrival): -0.068 -> -0.030 s.
- **New bow strokes after slurred eighths** (C #1; new-pitch crossover, harmonics 1-4, 21 of the listed notes): median +0.253 -> +0.145 s (p25 +0.095, p75 +0.190). Better by 0.11 s, still late (C's target +0.04..+0.07).
- **Wind pickups** (Fl1/Ob1 at qn 88, 104.5, 146.5, 312.5, 552.5; -6 dB of the 0.2 s peak): median +0.05 -> -0.03 s; Violins I at the same pickups +0.01..+0.03 s in both renders. The extra lead overshot by about half: the winds now speak 0.04-0.09 s before the violins (inferred: C's +0.15 s used a different arrival measure).
- **A #4 Violins II sul tasto** (qn 588-616, 2-6 kHz minus 250-1000 Hz): -3.4 -> -6.7 dB (target -9); level after the stem fix within 0.1 dB of c02.
- **A #5 Bassoon 1 staccato test**: peak +0.060 -> +0.073 s after the onset (violas +0.032), level +1.3 dB. Fails (target within 0.04 s of the violas). Revert next cycle (full rebuild of Bassoon 1).
- **A #6 Double basses Marc Shrt test** (bars 27-28): re-attack rise 2.6 -> 2.4 dB (control bars 131-132: 2.8 -> 3.3), level +6.6 dB before the stem fix. Fails (target 6 dB). Revert next cycle (full rebuild of the Double basses).
- **Balance** (stem RMS dB over the span): bars 127-128 Clarinet 1 / Horn 4 -45.6 / -40.6 -> -40.6 / -44.6; bar 129 Cl1 / Hn4 / Timp / Vc -43.4 / -37.1 / -38.0 / -38.2 -> -38.5 / -41.1 / -41.0 / -40.7; qn 252-262 Cl1 / Hn3 / Bn2 -43.4 / -35.3 / -36.5 -> -40.1 / -39.3 / -39.5; bar 82 Vln I / Tbn2 -26.3 / -25.6 -> -26.3 / -28.6; qn 440-456 Tuba / Vln I -34.0 / -35.9 -> -38.7 / -34.9.
- **Attack probe**: 0 flagged (it now searches from 0.3 s before the onset). Timpani 100/128 +0.06/+0.05 s (the planned delay).
- **Memory**: REAPER 18 GB settled before the render, 42 GB after it with 16 GB compressed. Quit after the stem fix.

## Rejected or deferred

- B #6 (+2 dB on every wind and string f trim): rejected. It would add 0.6 LU between mf and f bars but take 1.1 LU from f to ff (B's own simulation: f -23.0 -> -22.2, ff -18.2 -> -18.5).
- C #6 PHRASE_ARCS: deferred. They change the tempo inside the Lento and coda notes and so move the re-bow points that were refitted this cycle; do them in a cycle without a re-bow refit.
- C #5 in full (removing the movement II per-pitch and Leg Slur extras): not done; C's absolute numbers for them include the 1/6 qn axis error. Re-measure on c03.
- `auto_fills.py` pass: deferred to c04 (lead tables changed here).
- Harp étouffez (A, smaller items): not done; a track-wide -12 dB step would also cut the new p arpeggio. Needs a note-level approach (end the f chord's notes at the mark is already the case; the ring is the sample's).
- Violins II "metà" on a DIV patch: not done (memory/rebuild cost, separate cycle).

## Open for c04

- Revert the two failed articulation tests (Bassoon 1 staccato, Double basses Marc Shrt) and the -6 dB Cb role [104,112].
- Wind entry lead by articulation overshoots: halve wind Leg Slur MAX / Leg Slur +0.11 -> about +0.05 s after measuring c03 against the violins.
- C #1 strokes still +0.145 s: re-measure; consider a larger cap than 0.45 x the eighth for these joins.
- Run `auto_fills.py 3` and `fit_rebows.py 3` on this render (first render on a correct axis; moved re-bows carry copied shapes).
- Remaining re-bow pairs on the final chord (3 under 0.6 s); timpani roll loop autocorrelation 0.6-0.8.
- Delivery limiter 2.7 dB: the bar 160-161 peaks (1.37, 1.10).
- PHRASE_ARCS (C #6).
