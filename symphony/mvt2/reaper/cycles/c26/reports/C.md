# Cycle 26, critic C: dynamics over time (on the cycle 25 render)

Lens: the shape of every hairpin and phrase, the loudness arc against the score (climax bars 59-63, return at 65, coda), loudness range, swells and decays on long notes, and comparison with real orchestras. Dan's two listening notes from c24 (BRIEF items 8 and 9) both fall under this lens, so they come first.

Material:
- `cycles/c25/render` (master and 32 stems), `cycles/c25/mvt2-mockup-c25.mp3`, `cycles/c25/metrics`.
- The c24 render, for comparison. It is the render Dan heard, and its final-chord string data is identical to c25.
- `build/parts.json` (06:59, the data of the c25 render), `build/loop_profiles.json`, `build/roles.json`.
- `tools/score_to_parts.py`, in particular the notch rules at lines 1236-1295, `notch()` at line 1644, and the loop-profile writer at line 2435.
- `build/mockup-events.tsv` and score page 8.
- References: the stored Brahms 1/ii and 4/ii series.

Scripts are in `/private/tmp/claude-501/mockup-loop/c26-C/`:
- `fc*.py`, `fold*.py`, `percyc.py`, `seam.py`, `harm*.py`: final-chord envelope, loop folding, autocorrelation and harmonic stability.
- `scoop.py`: bow-change scoops against control times.
- `sim292.py`: an audio-gain simulation on the c25 stems, K-weighted.
- `tbn2.py`: trombone attacks.
- `barsK.py`, `hp.py`, `kb.py`, `sections.py`, `ride.py`: per-bar levels, hairpins, the arc and the mp3 ride.

Run the numpy/soundfile scripts with `~/.venvs/claude-composes-reaper/bin/python`. `measure.py` needs scipy, so it runs under `/usr/bin/python3`.

## Delivery, c25 (measured)

| | Master | mp3 |
|---|---|---|
| Integrated | -22.6 LUFS | -19.8 LUFS |
| LRA | 23.6 LU | 16.0 LU |
| True peak | -4.2 dBFS | -1.6 dBTP |
| p10 / max short-term | -40.0 / -13.3 | -27.9 / -9.4 |
| Span | 26.8 dB | 18.5 dB |
| Climax rise over the median of the preceding 20 s | 7.7 dB | 7.3 dB |

- mp3: limiter 1.6 dB, 0 inversions, median share of 5 s moves kept 0.84 (p10 0.63).
- Motion (mp3): dS4 p90 5.06 dB and 1 s/20 s 2.87 dB. The references are 6.29-8.55 and 3.92-4.56.
- All brief targets are met. None of the fixes below should move these figures by more than 0.2.

What holds (measured, K-weighted LUFS per bar, master/mp3):
- The arc. Bars 59-62 rise -20.7, -16.9, -13.9, -13.9 (mp3 -16.6 .. -9.9). Bar 63 is -18.2, bar 64 -25.1, and the return at bar 65 is -39.7, a drop of 14.6 dB.
- The two climaxes. Bar 61 is 1.5 dB over bar 79 (mp3 1.3 dB).
- The coda. It falls to -47.5 in bar 92, 6 dB under the opening ppp bar 1 (-41.5).
- The final release decays with RT60 2.7 s (Brahms 1/ii 2.5 s, 4/ii 2.9 s). The tail is not cut.
- Hairpins. The median crescendo rise is 4.4 dB against 3.7 expected.

## 1. The final chord (bars 89-92, qn 292-304, 18.7 s) carries a regular pattern that real players do not make: synthetic bow-change scoops in Violins I/II, a synchronized hollow in the lower strings 0.8 s after the chord change, and four sections replaying the same 3.97 s sample loop in step (measured; that this is the "bowing effect" Dan heard is inferred)

Ruled out first (measured, c24 and c25 stems). These are not the cause:
- Broadband level movement. The final chord moves no more than the opening chord. Fast std is 0.93 dB against 1.17 at qn 1-8.5, and the 0.5 s level detrended over 4 s has p5-95 1.8 dB against 2.7 dB.
- Timbre. Harmonic-by-harmonic stability is the same with CC11 held (293-298) and during the CC11 slide (298-303.5): timbre motion 2.81 and 2.90 dB.
- The CC1 vibrato line (42 -> 38).
- The release and hall tail (RT60 2.7 s).
- The mp3 ride. It rises smoothly, by 2.1 dB over bars 90-92.

What does stand out:

**a) Programmed bow-change scoops at regular intervals.** The tied held notes get CC11 notches from two rules in `score_to_parts.py`: the printed up-bow/down-bow rule (c06 A #5, line ~1287) and the merged-repeat rule (line ~1248). Each notch drops the CC11 and ramps back over 0.25 qn (`notch()`), which is about 0.35 s at this tempo.

| track | qn | CC11 notch | deepest 0.15 s in the 0.75 s after, against the surrounding 0.8 s |
|---|---|---|---|
| Violins II | 289 (merged repeat) | 34 -> 26 -> 34 | (under the clarinet solo) |
| Violins II | 292 (merged repeat, "change bow at will") | 34 -> 26 -> 34 | -3.3 dB |
| Violins I | 295 (printed down-bow inside the tie) | 34 -> 28 -> 34 | -1.4 dB |
| Violins I | 298 (printed up-bow) | 33 -> 28 -> 33 | -2.2 dB |
| Violins I | 301 (printed down-bow, the ppp arrival) | 22 -> 16 -> 22 | -3.7 dB |

Control: at 14 other times inside the chord the same statistic is -1.5 dB (Vln I) and -1.6 dB (Vln II) median. So 292 and 301 stand out by about 2 dB, and 298 by 0.7 dB.

The held note contains no sample bow change. Every dip comes from the CC lane, and it lands in the top voice about once per bar. At ppp a 16-player section changes bow without a level dip.

**b) A synchronized hollow 0.6-1.0 s after the chord change.** Violas, cellos and basses all go to their final note at 292. Each follows the same shape: up 3-6 dB at 0.2-0.6 s, down 4-6 dB at 0.8-1.2 s, then recovery. Per section (0.1 s frames, c25):
- Violas: -42.7 at qn 292.38, -54.3 at 292.88.
- Violoncellos: -42.6 at 292.12, -52.7 at 292.80.
- Double basses: -45.9 at 292.38, -54.2 at 292.80.

The K-weighted sum of Vln I, Vla, Vc and Cb has a 3.4 dB hollow at 292.6-292.9, one beat after the arrival.

The cause is partly in the samples (the legato crossfade valley: stem minus envelope dips 4-8 dB). The other part is the 292 loop profiles. They fade in at +0.8 s (`LP_START_S`) with -2..-4 dB exactly over the valley. At that phase the profile cancels a loop peak that the first pass of the sample does not have.

**c) Four sections loop in step.** Vln I, Violas, Celli and Basses start their final notes within 0.16 s of each other (moved starts 329.91-330.07 s). Their loop periods are 3.93-3.97 s. Each one replays its loop almost exactly: autocorrelation of the stem-minus-envelope level at the loop period is 0.93/0.63/0.94/0.91.

The c17 profiles still match:
- per-cycle correlation with the residual is -0.71 to -0.93, flat across the 4-5 cycles;
- refitting them on c25 lowers the folded residual by only 0.6-1.3 dB per section and does not change the K-weighted string sum (2.1 -> 2.2 dB folded).

So the level correction works, but it cannot remove the repetition. Each section plays the same 4 s of bowing and vibrato 4-4.7 times. After the profiles, the folded residual per section is 3.0 (Vla), 4.2 (Vc), 4.6 (Cb) and 5.5 dB (Vln I). In Vln I it is a 4 dB rise within 0.2 s at loop phase 1.4 s (`foldsec.py`), in the top voice, every 3.97 s.

The opening chord has the same loop (Vln I key 0) for only 2.3 cycles. Inferred: the long, exposed fermata chord is where a listener hears the repetition as a mechanical bowing cycle, and a) and b) make it more regular.

**Fix:**
1. **Bow-change scoops** (`tools/score_to_parts.py`).
   - `MERGE_NOTCH_AT`: add `"Violins II": {289.0: 3, 292.0: 3}`. That is the `BC_SOFT` soft depth, so the printed re-bows stay just marked.
   - Add a `BOW_NOTCH_SKIP = {"Violins I": [295.0, 298.0, 301.0]}` check to the printed-bowing rule at line ~1290: `... and not any(abs(bq - s_) < EPS for s_ in BOW_NOTCH_SKIP.get(tname, []))`.
   - Keep the Violoncellos 289 merge notch: that is a printed repeated note, under the clarinet.
2. **The 292 hollow** (`JOIN_NOTCH`, existing mechanism with 0.04 qn ramps):
   - "Violas" `(292.60, 292.98, 4.0)`
   - "Violoncellos" `(292.60, 293.02, 5.0)`
   - "Double basses" `(292.55, 293.00, 3.5)`

   Simulated on the c25 stems (`sim292.py`, K-weighted):
   - section troughs: Vla -54.1 -> -50.1, Vc -53.6 -> -48.6, Cb -54.8 -> -51.3;
   - string sum at 292.67/292.83/292.92: -41.3/-41.8/-40.0 -> -39.6/-40.2/-38.7;
   - the new values stay under the 292.33 attack peak (-38.5 -> -38.5).

   I also tried moving the profile start to +1.8 s. It removes useful later correction (Vc at 293.16 fell 3 dB), so do not do that.
3. **Break the lock-step loops (a test; effect inferred).** Real sections re-bow at staggered times; Vln II is marked "change bow at will" at 292, and Vln I has a printed up-bow at 298.
   - Add `REBOW_AT = {"Violins I": [298.0], "Violas": [297.0], "Violoncellos": [299.5], "Double basses": [296.0]}` (score qn). It splits each held final note there into two abutting same-pitch notes.
   - The second note is a fresh note-on on `Sus MAX`, at the current CC11, v41, with the keyswitch 0.05 qn before. It must be exempt from the merge rule, and it gets no notch.
   - Each section's loop then restarts at a different moment, so the cycles stop coinciding, and no section completes more than 2.5 identical cycles.
   - Refit or drop the 292 profiles after the split point: the new note's loop phase starts at the split, so set its `loop_profiles.json` entry from the same profile with the new key.
   - Check on the render (`percyc.py`, `scoop.py`): every split dips at most 2 dB against the control statistic, with a `JOIN_NOTCH` fill if it dips more; autocorrelation at the loop period over 293-303.5 falls below 0.6 on every track; and the K-weighted string sum folded at 3.97 s (`foldsum.py`, 2.4 dB now against 1.7-2.2 at other periods) drops to the control level.
   - If the split attacks are audible, keep fixes 1 and 2 and drop this one.

## 2. Bars 63-64 (Trombone 1, Dan's item 9): the three accented notes are bright, not heavy. Their 2-5 kHz band jumps 7-8 dB on the attack while their overall level rises only 0-2.6 dB, and the envelope adds +2 dB steps in 7 ms on top (measured)

**Where:** Trombone 1, qn 212.5 (v108), 213.0 (v105) and 218.0 (v110). These are `Sus Accent MAX`, ff marcato, "accent". The eighths between them (214.5-217.5) are `Marc Lng RRx4`.

**Evidence (`tbn2.py`, c25 stem, 10 ms windows, from the moved note-on).** Peak in the first 80 ms against the median of 100-250 ms:

| note | 2-5 kHz | broadband | Tbn1 over Violins I at 2-5 kHz, at the peak |
|---|---|---|---|
| 212.5 | +6.8 dB | +1.3 | +2.8 |
| 213.0 | +6.9 dB | +2.6 | +14.5 |
| 218.0 | +8.3 dB | +0.0 | +13.5 |

The marcato eighths read -7.6 to +0.6 dB at 2-5 kHz: the eighths are not the harsh part.

So the accent is almost entirely a burst of brass blare in the presence band, and on 213 and 218 it sits 14 dB over the ff violins in that band. That is the "hard front edge" the BRIEF rule 4 forbids. Inferred: what Dan hears as harsh is this band, not the level.

The volume envelope (`parts.json` `vol_db`) adds to it:
- 212.5: +5.1 -> +7.0 dB within 0.009 qn (about 7 ms);
- 213.0: +4.6 -> +6.0;
- 218.0: +2.6 -> +4.5.

These come from `ACCENT_DB_AT` `{"Trombone 1": {212.5: 4.0, 213.0: 3.0, 218.0: 4.5}}` with the 0.01 qn rise.

**Fix:**
1. `score_to_parts.py`: play 212.5, 213.0 and 218.0 on `Sus MAX`, not `Sus Accent MAX`, at velocity 95.
2. Replace the step with a swell. `ACCENT_DB_AT` for Trombone 1 at 212.5, 213.0 and 218.0 should become 2.5 dB with a 0.1 s rise and a 0.3 s hold. The entry shape (`(q0 - 0.01, 0), (q0 + 0.01 * bpm/60, ov), ...`) should take its rise from a per-onset seconds value instead of 0.01 qn.
3. If the 2-5 kHz burst stays over +4 dB, add a `loud_eq` spec on Trombone 1 in `build/mix.json`: `{"points": [[212.3, 0], [212.45, 1], [219.4, 1], [219.6, 0]], "bands": [{"band": "bell", "hz": 3200, "db": -4, "bw_oct": 1.2}]}`.
4. Check on c26 (`tbn2.py`):
   - 2-5 kHz peak over body at most +4 dB on the three notes;
   - broadband peak over body +2..+4 dB;
   - Tbn1 over Vln I at 2-5 kHz at most +6 dB;
   - Tbn1 still 2-3 dB over Violins I in K at bar 63 (critic B's c25 balance).

## 3. The coda's ppp < pp (bar 86, qn 283-286) does not rise in the basses and comes only in the last beat in the violas, because the coda accompaniment cut ramps in during the hairpin's first half beat (measured; fix inferred)

**Evidence (K, per half beat, qn 283 -> 285.5 -> 286):**
- Violas -58.8 -> -54.5 -> -48.0. Most of the rise falls on the last beat.
- Violoncellos -48.6 -> -45.7.
- Double basses -53.5 -> -54.1. No rise at all.

Printed: ppp < pp in all three, arriving at pp in bar 87, under the clarinet's dolce pp. On the master the hairpin reads -0.1 dB (expected +3.7); c22 C #3 reported the same.

In `vol_db` the bass level falls from about -2..+1 dB (282.5-282.9) to -10 dB at 283.15-283.3, just as the CC11 crescendo (22 -> 34) starts. Three roles combine to do this:
- the c24 C #4 `[283.0, 291.5, -2.0, 0.5]` on Vla/Vc/Cb/Hn3/Hn4/Vla div;
- `_all` `[283.5, 304, -2]`;
- the end of the Cb role `[274, 286, 2]`.

`HP_SOFT_ACC_SKIP` 283 (c24 B #2) is a deliberate balance choice: it keeps the clarinet on top. This fix keeps that choice.

**Fix (`build/roles.json`):**
- Move the accompaniment cut ahead of the hairpin: `[283.0, 291.5, -2.0, 0.5]` -> `[282.25, 291.5, -2.0, 0.5]` on the same six tracks.
- Double basses `[274, 286, 2]` -> `[274, 282.5, 2]`.

The level at 286 is then unchanged, and the cut no longer eats the crescendo. Check on c26: the Vla/Vc/Cb group rises at least +3 dB from 283-284 to 285.5-286.5, and the Cl1 median margin over the accompaniment in 283-292 stays where c25 has it (`lead.py` from c24-C).

## Smaller items, measured, for the actor's judgement

- **Morendo in the mp3.** The mp3 ride rises from +12.4 dB (qn 295) to +14.0 dB (301), so the delivered morendo is 8.7 dB against 10.3 dB on the master. That is acceptable, and `deliver_master.py` is a do-not-touch. If the ending should recede more in the mp3, deepen the `_all` row `[300.5, 303.5, -3]` to -4.5. Bars 91-92 are already in the bottom 10% of short-term loudness, so the LRA should not move.
- **Bar 56 -> 57.** The level dips 0.7 dB (master) and 1.5 dB (mp3) into the mf < f crescendo. In the mp3, 0.8 dB of that is the ride falling ahead of the climax, by design. A real orchestra often makes this drop. No action.
- **Phrase motion.** In the mp3, phrase-scale motion (1 s vs 20 s) is lowest in the B section (bars 37-52, 1.93) and the A1 solos (1.88-1.92), against 3-4 for the references. Within those spans the printed hairpins now reach their levels (the CA 124-128 arrival is +4.5 dB per half beat). I found no single fix there this cycle.

## Do not touch

- The arc: the bars 52-62 rise, bar 61 over bar 79 (1.5 dB master, 1.3 dB mp3), the bar 63-64 fall, the 14.6 dB return at bar 65, and the coda's level order down to bar 92 at 6 dB under the opening ppp.
- `deliver_master.py`: LRA 16.0, span 18.5, limiter 1.6, 0 inversions, 84% of 5 s moves kept, climax rise 7.3 dB.
- The loop profiles as a method. They cancel 70-90% of the loop dips (per-cycle correlation -0.7 to -0.9). Only their first 0.8-1.2 s at qn 292 is wrong; finding 1 fix 2 covers it.
- The final release and hall tail (RT60 2.7 s), and the `_all` morendo rows.
- The Violoncellos 289 merge notch, which marks a printed repeated note.
- Trombone 1's level and balance at bars 61-63 (critic B c25); only the attack shape and band change in finding 2.
