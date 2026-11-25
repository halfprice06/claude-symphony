# Cycle 26, critic C: dynamics over time (render of cycle 25)

Material: `cycles/c25/render/` (31 dry stems, 4 return stems, `00_Master.wav`), `cycles/c25/mvt3-mockup-c25.mp3`, `cycles/c25/CHANGES.md`, `cycles/c24/render/` and `cycles/c24/parts_rendered.json` for comparison, `build/parts.json`, `build/mix.json`, `build/score_config.py`, `build/mockup-events.tsv`, `tools/deliver_master.py`, `tools/score_to_parts.py`, the score (pages 5, 6, 8, 11, 13, 16), and the Dvořák 9/i reference. Loudness is BS.1770 through ffmpeg ebur128 (M = momentary 400 ms, centred, 10 Hz). Bar values on the mp3 are read 0.30 s later (the head). Stem levels are plain RMS on the parts.json tempo map. "Measured" means a number from these files. "Inferred" means reasoning that no render has tested.

Delivery simulations: I ran `tools/deliver_master.py` on the c25 master with a copy of parts.json in which only `ride_trims` was edited (mix.json linked), using the c25 head. Then I measured the result with the actor's `cycles/c25/actor_scripts/deliv24.py` and `stops24.py`. The unedited run reproduces the delivered c25 file exactly (-14.0 LUFS, LRA 11.3, TP -1.3, limiter 5.4, stops 13.1 / 13.5). For the stop fixes I also built a master in which the four return stems are rescaled exactly as a changed `return_rides` row would rescale them (the ride is a post-reverb fader, so this is exact), and in which the celli stem's tail after its note-off at bar 94 is lowered. The celli part is approximate because the celli's own hall send is not lowered with it.

## Manual notes

MANUAL-READING.md has no row for cycle 26 (the plan ends at c20), so I read no fixed range. These are the pages behind this lens's open problems, plus the MANUAL-GAPS items that touch them.

| Manual (May 2021 HO, PDF page) / gap | What it says | Where it applies here | Does the render follow it |
|---|---|---|---|
| p.142 (envelope: attack, hold, decay, sustain, release); DIGEST §3 (2025 p.87, Release Trails on/off) | Each patch has a release stage, and the 2025 edition has a separate release-trail switch. | The celli note that ends the tutti stop of bar 94 (qn 373.89, "Leg BC MAX"). | Partly. The 150 ms ff cap (`sus_release_cap_ms`) is on the row, yet the celli dry stem holds a plateau about 7 dB under the note for about 0.3 s after the note-off. It is the loudest tail at +0.3 s (finding 2). Either a release-trail group the cap does not reach, or CC11 still at 109 when the release plays. |
| p.99 (Leg BC: bow change with its own sound) | Bow-change legato has its own sample set. | The same note. | Followed for the attack; the release behaviour above is the problem. |
| p.94 / p.101 / p.109 (sustains are looped) and BRIEF item 7 | Held sustains loop; long notes can pulse. | Every note held 5 s or longer (17 notes: woodwinds, horns, timpani rolls, cymbals; the strings are re-bowed). | Followed. Folded at 3.95 s, residual level swings are 1.5-4.6 dB on winds and horns. The largest is the timpani roll at 920 (6.6 dB), and that is the printed settle from f (CC7 42 -> 24 over 921-923), not a loop. |
| MANUAL-GAPS #12, recorded crescendo rolls (p.123, p.125) | Felt Cresc rolls end on a stroke. | Timpani crescendos 1040-1048, 1096-1108. | Not needed. The CC1 rolls rise (c22 numbers) and the 223 roll now carries its printed decrescendo (`TIMP_ARRIVAL_RAMP`). |
| p.104, brass Crescendo patches | Recorded single-note crescendos. | 1040-1048, 1096-1108. | Not needed now. The master rises into 263 (+2.4 dB, 261 -> 262) and into the final (+2.7, +1.4). |

## Answers to the coordinator's items (my lens; the others belong to A and B)

- **Stops after bars 94 / 113 (13.1 / 13.5 dB on the mp3):** measured causes and a simulated fix are in finding 2 (15.5 / 15.3 dB). The ride is not the cause. The mp3's gain over the master stays at +4.1..+5.0 dB until 0.7 s after each cut-off and rises only after that, so `rise_delay_s` 0.6 is working. The master itself fell from c24 to c25: bar 94 15.8 -> 13.8 dB, bar 113 14.9 -> 14.1.
- **In-bar arrival steps:** 263 over 262 rises +0.3 -> +0.9 with finding 1(c). 223 over 222 is +2.5 and I would not spend more there. 223 and 263 tie at -8.4. Both are fff with the same forces, so I leave the tie, as in c22.
- **Basses' pp re-bows, master 30-150 Hz:** smoothed over 0.6 s, the master's range over qn 166-200 is 7.7 dB (c24 10.5) and the basses stem's is 10.3. The counter-shape now makes a dip. Finding 4.
- **Timpani at 223:** I did not re-measure it under the master. The roll at 920 starts at f and settles 5-7 dB, as Dan's rule asks.
- **loud_eq (loudest 10 % of 0.4 s frames, band share of the total):**
  - 100-250 Hz: master -11.25 (c24) -> -10.04 (c25); mp3 -9.75 -> -8.72; Dvořák -6.14.
  - Above 6 kHz: master -24.04 -> -25.08; mp3 -27.48 -> -28.31; Dvořák -28.08.
  - On the delivered file the top band now matches the reference, and the 100-250 Hz band is 2.6 dB short.
  - 20-100 Hz is 11.7 dB over the reference, which is a lossy mp3, so I would not tune to it alone.
  - Next step (inferred, for B): lower 20-100 Hz in the loud spans (the basses' 72 Hz +4 bell to +2 inside the loud_eq points, and the 40in bass drum gain -4.4 -> -5.4 dB) before adding more at 160 Hz.
- **The 30 fader steps inside notes:** none is at a printed fp or sfp, so all 30 break the standing rule. 22 come from one generic cause (finding 3). The other 8:
  - celli 15.5 (-6.0) and 1031.99 (-5.8): crescendo gain released inside a held note at the ff arrival;
  - Violins II / Violas / Celli 375.9 (-4.0): the role step for the mp entry of bar 95, which falls 0.43 qn inside the led note;
  - Trombone 2 151.99 (-3.5);
  - Violins I 484.9 (-3.0, pp of the 4 soli);
  - Harp 511.99 (+10.0).
  For each of these, move the edge to the note's moved onset or into the preceding rest. Of the eight, the master steps at 1032 (+3.0 dB), 375.9 (+2.4) and 152 (+1.5).
- **The -9 dB 3:1 peak compressor (scherzo c22):** not needed. My variant keeps the final 0.7 LU over 223 and the limiter at 5.4 dB.
- **CC11 lifts that raise the previous tail (scherzo c23):** this applies to finding 4's re-bow shape. Start CC moves after the previous bow's release, not at the re-bow.
- **sfp, bar 149 (qn 592):** master in 0.1 s windows: ff -18, sf -17, -20, then -24 / -25 / -28 0.4-0.6 s later, a 12 dB crescendo, and ff at 596. The p arrives about 10-11 dB down, and the hall of the sf rings under it. No change asked.
- **Loop pulsing:** no held note pulses audibly (see Manual notes). The final chord falls 16.4 dB at +0.3 s and has an RT60 of 1.25-1.39 s, inside the recordings' 1.1-1.6 s. The mp3 is within 1 dB of the master through the ring, so the -8 dB tail row does not cut the ring.

## Findings, ranked

### 1. The delivery flattens three ff tutti arrivals and makes the f of bars 205-208 sound mp

Measured on the c25 mp3; master in brackets. Bar medians of M; the step is arrival bar minus the bar before.

**Arrival steps:**

| arrival (printed) | mp3 step | master step |
|---|---|---|
| bar 91 (qn 360, f cresc -> ff tutti with trumpets) | +1.4 | (+5.1) |
| bar 110 (qn 436, strings p cresc over 3 bars -> ff tutti) | -0.4: bar 109 is -10.5, louder than the ff at -10.9 | (+3.8) |
| bar 199 (qn 792, f cresc -> ff, the last C-minor tutti) | +0.4 | (+2.5) |

**Bars 205-208 (qn 816-832), f, "poco a poco più animato":** strings, bassoons, four horns a2, trombones, tuba and timpani, all f.
- mp3: -19.9 / -20.3 / -17.2 / -19.4.
- The f of bars 11-26 reads -14.0 to -18.7 (median -16.2).
- On the master the two passages are level (-27.6 / -28.0 against -26..-30). The delivery lifts bars 11-26 by about 12 dB and bars 205-208 by only 7.7.

**Causes:** deliver_master's quiet lift is smoothed over 5 s (`LIFT_SMOOTH_S`) and centred.
- The gain is already falling across each crescendo bar (bar 109 +10.0 dB, bar 110 +5.9) while the arrival bar carries a -3 dB ride row: [359.5-376.5 -3] over bars 91-94, [435.5-452.5 -3] over 110-113, [791.5-840.5 -1.5] over 199-210.
- The ff bars need those rows to stay under the fff climaxes, so removing them is not the fix.
- Bars 205-208 sit between the ff of 199-204 and the Largamente, so their lift stays at the ff value of about 7.5 dB.

**Fix (`build/score_config.py`, the RIDE_TRIMS rows; delivery only, nothing in the track envelopes):**
- **(a) Arrival steps:** extend each arrival row back over its crescendo as a ramp, so that the bar before the ff is lowered and the ff bars themselves do not change:
  - `[(352.0, 0), (354.0, 0), (359.9, -3.0), (360.0, -3.0), (376.0, -3.0), (376.5, 0)]` replaces the 359.5 row;
  - `[(427.5, 0), (428.0, 0), (432.0, -2.0), (435.9, -4.0), (436.0, -3.0), (452.0, -3.0), (452.5, 0)]` replaces the 435.5 row;
  - `[(783.5, 0), (784.0, 0), (788.0, -1.0), (791.9, -3.0), (792.0, -1.5), (815.5, -1.5)]` begins the 791.5 row.
- **(b) Bars 205-208:** the same 783.5 row continues `(816.0, +1.0), (818.0, +2.0), (831.9, +2.0), (836.0, 0), (839.9, -1.5), (840.0, -1.5), (840.5, 0)`. The rise starts 1.4 s after the bar-204 stop, so the mp3 stop there stays at 15.1 dB.
- **(c) 262 -> 263 and bar 227:**
  - the 1023.5 row becomes `[(1023.5, 0), (1024.0, -2.5), (1032.0, -3.5), (1040.0, -3.3), (1044.0, -3.5), (1047.8, -4.8), (1047.95, 0)]`;
  - new row `[(903.5, 0), (904.0, -1.5), (907.9, -1.5), (908.4, 0)]` for bar 227. That bar is printed ff and peaks at -8.3, over both fff arrivals.

**Simulated on the c25 master (variant v_abc2, together with finding 2):**

| check | c25 | v_abc2 |
|---|---|---|
| step at 91 | +1.4 | +2.4 |
| step at 110 | -0.4 | +2.6 |
| step at 199 | +0.4 | +2.2 |
| bars 205-208 | -19.9 / -20.3 / -17.2 / -19.4 | -16.7 / -16.8 / -13.7 / -15.9 (the level of the bar 11-26 f) |
| 209 -> 210 -> 211 | still rising | -14.3, -11.3, -10.0 (+1.3 at 211, was +2.3) |
| 263 over 262 (in-bar) | +0.3 | +0.9 |
| bar 227 maximum | -8.3 | -9.4 |

Unchanged in the simulation:
- I -14.0, TP -1.0, LRA 11.2 (c25 11.3), p10 -21.8, limiter 5.4 dB;
- final over 223 +0.7, final over every other bar 0.6 or more.

Cost: the strings' crescendo of bars 107-109 now rises 5.4 dB to bar 108 and stays flat to bar 109 (c25: +6.1, +2.0). The printed ff entry of the whole orchestra matters more than the last bar of the crescendo (inferred). The f -> ff median gap may lose about 0.1-0.2 LU from (b), estimated from 4 of about 60 f bars (inferred); c25 had 3.8.

### 2. The stops after bars 94 and 113: the celli's release tail and a +6.5 dB return lift held after the cut-off

Measured. On the master (`stops24.py`) the bar-94 drop at +0.3 s fell from 15.8 (c24) to 13.8 dB (c25), and the bar-113 drop from 14.9 to 14.1. The mp3 adds about 0.6 dB of loss (13.1 / 13.5). Per stem, at +0.3 s after the stop:

**Bar 94 (stop at qn 374.06):**
- The celli dry stem is the loudest tail: -39.3 dB, 6.9 dB under its pre-stop level (c24 -42.0).
- Its envelope falls 6 dB in 0.15 s after the note-off at 373.89 ("Leg BC MAX"). It then holds a plateau at -39 / -40 for about 0.3 s, then falls.
- The celli level before the stop rose 2.5 dB from c24 to c25 (-34.9 -> -32.4). The new loud_eq 160 Hz +3 dB bell covers qn 360-376, and the celli note is E flat 3 (155 Hz).
- CC11 is still at 109 at the note-off and falls to 58 only at 375.46.

**Bar 113 (stop at qn 450.0):** the hall returns are the three loudest tails (R Brass -40.0, R Strings -41.0, R Winds -44.1). `mix.json` `return_rides` holds +6.5 dB on all four returns from 448.0 to 451.3, 1.3 qn past the cut-off. This row is from c16, when this stop was too short.

**Fix:**
- **(a)** `mix.json` `return_rides`: the bar-113 row becomes `{"pts": [[447.5, 0.0], [448.0, 3.0], [451.3, 3.0], [451.4, 0.0]]}`, or 2.5 dB. This is a lower held lift, not a cut, so the S3 rule (no fast fall after the hall) is kept.
- **(b) Bar 94 celli, instrument side:** bring the CC11 fall from 375.46 to the note-off for a string note that ends a tutti stop. Ramp CC11 109 -> about 75 between the note-off minus 0.02 s and plus 0.08 s, so the release plays about 6 dB lower. Opus CC11 is a global volume, so the release follows it.
  - As a generic rule: `STOP_TAIL_CC11` in `tools/score_to_parts.py`, default off. A track's note that ends at a tutti stop (no note-on in any track within 0.4 qn) gets its post-note CC11 fall moved to the note-off.
  - Finale value: Violoncellos at bars 94 and 113, -6 dB target.
  - String CC11 per unit is not 20 log10 (c25 Violins I LITE), so range-test the unit count.
  - If the plateau turns out to be a release-trail group, cap that group in the celli `sus_release_cap_ms` entry for "Leg BC MAX" at ff instead.

**Simulated:**

| variant | master 94 | master 113 | mp3 94 | mp3 113 |
|---|---|---|---|---|
| c25 | 13.8 | 14.1 | 13.1 | 13.5 |
| return lift 3.0 dB and celli tail -6 dB from the note-off (v_abc2) | 16.3 | 16.0 | 15.5 | 15.3 |
| return lift 2.5 dB and celli tail -10 dB | 17.3 (over the 17 ceiling) | 16.2 | | |

The v_abc2 results are inside the 14.5-17 band. Bars 2, 6, 166 and 204 are unchanged. The celli figure is a dry-stem approximation; the real change also lowers the celli's hall send, so it could land 0.5-1 dB higher (inferred). Use -6 dB, not -10.

### 3. Every held decrescendo ends with a +3 dB fader snap inside the next (led) note

This accounts for 22 of the 30 inside-note steps.

**What happens:** measured from parts.json and the stems. `HELD_DECRESC_DB` (strings / winds 3 dB, `tools/score_to_parts.py` near line 5612) ramps the track fader to -3 dB at the hairpin's end and releases it at "the next moved onset". When the next note is led (legato or pickup leads), its moved onset is earlier than the hairpin end. `he_ = max(b_, nx_ - 0.03)` then puts the release at the hairpin end, 0.01 qn after the -3 point, inside the new note.

**Where:** +2.6..+2.9 dB at
- 295.88 (Violins I / II);
- 383.85, 551.85, 967.9 (Violoncellos);
- 531.85 (Violins II);
- 775.85 (Violins I / II, Violas);
- 909.9 and 913.9 (Violins I / II, Oboes 1 / 2);
- 931.9 (Oboes 1 / 2, Violas, Violoncellos, Double basses);
- 949.88 (Violins I / II).

**What it does to the music:**
- At bar 234 (qn 932), the end of the chorale's diminuendo to mf / mp / p, the violas' held G steps +3 dB and the basses +5 dB on the stems. The master steps from -38 to -35 dB in 50 ms windows exactly at 932.
- The master steps +3.3 dB at 913.9 (the f of bar 229 after the <> swell) and +2.3 dB at 295.9.
- Each of these diminuendos ends with a bump up instead of arriving at its softer mark. That reverses the printed shape and breaks the standing rule.

**Fix (generic, `tools/score_to_parts.py`, the `held_decresc` block):** when the next moved onset `nx_` is at or before `b_ + 0.01` (a led note), end the -3 dB ramp and its hold at `nx_ - 0.03`, and release to 0 at `nx_`. The release then sits at the note change, which stepcheck counts as "noteon", and the new note's CC11 (its printed dynamic) carries the level. The `held_decresc_carry` branch needs the same guard.

Expected: inside-note steps 30 -> 8, and no master step at 932 or 913.9 (inferred; stepcheck on the rebuilt parts.json confirms it before the render).

### 4. The basses' pp pedal (qn 164-200): the CC11 counter-shape now digs a 5-6 dB hole after each re-bow

Measured. The basses' 30-150 Hz band was averaged over the three re-bows (170.859, 181.676, 190.533) in 0.2 s frames:
- just before the re-bow: 13-14 dB;
- 0.4-0.6 s after it: 8.2 / 8.3;
- 1.0-1.6 s after it: 16.0 / 16.1;
- then a slow fall.

The master's 30-150 Hz band follows the same shape: 15.7 -> 9.2 -> 19.5. Smoothed over 0.6 s, its range is 7.7 dB (target 4).

The `rebow_cc11.json` shape `[(0, 0), (0.35, -14), (1.6, -14), (2.6, 0)]` reaches -14 at 0.35 s, while the new bow's sample is still in its soft start. That makes the dip, and the sample's bloom still rises 8 dB over it.

**Fix (`build/rebow_cc11.json`, the three Finale rows):** `[(0, 0), (0.45, 0), (0.9, -14), (1.9, -14), (2.9, 0)]`. This keeps the counter-move where the bloom peaks (1.0-1.6 s) and removes it from the bow start. Expected (inferred from the c25 range slope of about 0.25-0.4 dB per unit):
- the dip at 0.4-0.6 s fills by about 4-5 dB;
- the master 30-150 Hz range comes to about 5 dB.

Re-fit the shape with `tools/fit_rebows.py --cc11` on the range pass. Following the scherzo's lesson, the shape starts after the previous bow's release, not at the re-bow.

### 5. In-note fader edges at three printed arrivals

The rest of the 30. These are measured and small, but each is audible as a dip or step at a printed mark.

- **Celli at bar 5 and bar 259:** the crescendo gain releases inside the note before or at the ff arrival.
  - Bar 5: `vol_db` +6 -> 0 over 15.5-15.9, inside the 15.0-16.0 note, the last quarter of the crescendo.
  - Bar 259: +6 -> 0 over 1032.0-1032.5, inside the 1031.82-1040 held note; the master steps +3.0 dB there.
  - Fix: end the release at the next moved onset, in the `hpgain` release, like finding 3; for bar 259, after 1040.
- **Bar 95 entry:** the role step at 375.9 (-4 dB on Violins II, Violas, Violoncellos) falls 0.43 qn inside the led note that starts at 375.47. Move the role edge into the 374.06-375.4 rest, where the stop's tail is still falling.
- **Trombone 2 at 151.99 (-3.5), Violins I at 484.9 (-3.0), Harp at 511.99 (+10):** each edge goes to the nearest rest or moved onset.

## Do not touch

- The -14 delivery chain with `rise_delay_s` 0.6: the gain does not rise into a stop's tail before 0.7 s.
- The c25 ride rows for the final, 223 and 263.
- `TIMP_ARRIVAL_RAMP` 888 / 1048.
- The fff caps and steps at 888 / 1048: master steps 223 +6.9, 263 +1.4, final +4.3.
- The 1040-1048 crescendo: master rises 2.4 dB into 262.
- The sfp of bar 149: 10-11 dB drop and crescendo back within the bar.
- The final chord's ring: RT60 1.25-1.39 s, mp3 within 1 dB of the master.
- AUTO_REBOW on the strings: no held string note over 5 s; no loop pulse over 4.6 dB on any held wind or horn note.
- loud_eq's high shelf: above 6 kHz on the mp3 now matches the Dvořák reference.
- The celli Detache bass line.
