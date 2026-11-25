# Cycle 22 changes (actor)

Snapshot of the c21 tools and data: `cycles/c22/before/`. All 32 tracks were updated with `build_reaper.py build/parts.json jobs --midi-only`. No Opus state changed, so no track was fully rebuilt. Then save, quit (the quit job timed out after 60 s, but REAPER exited), `-new` restart and `Main_openProject` (32 tracks). One render: 21 GB and 0 GB compressed at the start; 63 GB with 42 GB compressed during the render. Attack gate 19 of 21: Vln II and Vc at qn 212 dip 6.7 and 7.6 dB, the same values as c20 and c21 (known threshold noise). No post-render fixes.

## Accepted

### Critic A
- **A #1 CC11/CC1 pull rounding (tools/score_to_parts.py).** The pull now starts `PULL_PAD_QN` (0.01 qn) before the moved note-on, rounded to the 4-decimal grid that `sample()` uses. Before, a moved onset that rounded down put the grid point just before the pull, and moved entries started on the previous phrase's CC11 (26 CC points on 15 tracks, critic A's count). Moved notes whose CC11 at note-on differs from the score onset by 15 or more: 19 -> 5. The 5 left are legato targets and crescendo arrivals at qn 65 and 262, which get no pull by design.
  - (b) Compensations removed: note_trims Bassoon 1 "196" -9 -> 0, Horn 4 "286" -5 -> -1; early_fills Horn 3 "204" 8 -> 2 dB; entry_leads Horn 3 "204" 0.10 -> 0. The fill is marked in `_auto` as "c22 set by hand (pull fix)".
  - (c) `cc1_fn` evaluates the vibrato at the pull's end (the entry's own CC1) inside a pull.
- **A #2 `JOIN_NOTCH`:** Vln I 72 widened to (71.90, 72.08, -4.5), Vln I (249.37, 249.44, -3.5), Vln II (73.33, 73.42, -4.0) and (82.84, 82.91, -3.5), Ob1 (144.81, 144.92, -4.0). Early fills Horn 1 "180" 4.2 -> 2.5 and "202" 8.0 -> 6.5, marked "lowered by hand" in `_auto`.
- **Routine `auto_fills.py 21`** on `cycles/c22/before/parts.json`: Clarinet 1 178 3.2 -> 0.3, Violoncellos 192 new (2.2), Violoncellos 195 removed. I excluded the hand-set notes (Hn1 202, Ob1 143/145, Vc 256), the entries that keep flipping on and off (Fl1 200, Vc 203, Vc 210, Cl1 266), and CA 132/134.

### Critic B
- **B #1 Bassoon 2 B flat 2 swells.** I checked the claim against the patch file (`BS KS Master.oib`, `opus_state.load_oib`): the "Bs f" group's CC11 table fades in over CC 33-38 (0.12 at 34, 0.37 at 36, 0.6 at 38) while "Bs mp" stays at 1.0 up to CC 40. A pp swell from 34 to 38 therefore adds the f layer. I used the critic's code option: new `SWELL_CC_CAP = {"Bassoon 2": {46: 36}}` caps the long-note swell's CC11 for that pitch while the printed level is at or under the cap (qn 27, 140, 247). The bar 69 entry (qn 232) was the A #1 pull bug, so it got no notch.
- **B #2 Double basses E flat 2 sample swell:** `JOIN_NOTCH` "Double basses" (64.12, 64.50, -4), (76.10, 76.62, -5), (85.10, 85.62, -6). These are placed for the c21 tempo map and the 0.16 s abut lead.
- **B #3 Violoncellos bar 60:** `JOIN_NOTCH` (200.52, 200.90, -5.0) and (202.84, 202.97, -3.0).
- **B #4 Harp bars 71-78:** roles.json Harp `[238, 262, 4]`.

### Critic C
- **C #1 solo soft hairpins (score_to_parts.py, build JSON).**
  - New `HP_SOFT_GAIN_AT`: Violin I solo 48 4.5 (critic 6.0; lowered because removing the phrase tops adds about 2 dB to the same crescendo), 60 4.5; Horn 1 32 4.0, 176 5.0; Flute 1 126 6.0.
  - `HP_SOFT_DEC_AT` Oboe 1 57: 5.0. That decrescendo is the second half of a messa di voce, so a listed depth larger than the crescendo gain now adds an extra decrescendo ramp of (depth - gain).
  - New `HP_SOFT_EXTRA_SPANS = {"Horn 1": [(174, 184)]}`. These spans get the lead-line ramp only. I did not add (174, 184) to `LEAD_SPANS`, because that table also steers phrase tops, metric steps and the tempo apexes.
  - Horn 1 qn 32: pitch_trims `_skip_onsets` [32.0], note_trims "32" 2.5 -> -2.0.
  - Phrase tops (`PT_*`) are 0 on onsets inside a soft lead hairpin (`hp_soft_spans`).
- **C #2 bar 56 -> 57 (code + roles).** New `HP_MF_BRIDGE_REL` (1.5 qn): an mf-arrival hpgain whose track starts another crescendo within `HP_CHAIN` qn, with no softer mark or decrescendo between them, holds its gain to that crescendo's start and releases it while the new ramp rises. It applies at qn 188 on Vln I, Vln II, Vc and Cb (parts.json `hp_bridged`). The Violoncellos role `[188,204,-3,4]` is split into `[188,190,-1.5]` and `[190.5,204,-3,4]`; I used 190.5 rather than the critic's 190, because the span's 0.5 qn ramp-in would otherwise add to the first row and reach -4.5 at 190. C #2(c) (Vln II 188 +3) was not done: the bridge already holds +2 dB there.
- **C #3 coda arrival at qn 286.** (a) `JOIN_NOTCH` Vc (285.75, 286.30, -3), Violas (286.00, 286.40, -3), Cb (285.95, 286.30, -3). (b) The source of the Cb's CC11 +7 was the soft re-struck "bloom" contour (+6 CC at the onset). That contour now skips a crescendo's arrival note, as `bloomv` has done since c10. (c) This is covered by C #4.
- **C #4 accompaniment soft hairpins.** New `HP_GAIN_SOFT_ACC_DB` 2.5. Every wind, brass and string soft hairpin outside the lead lines now gets a ramp: a crescendo held to the arrival, a < > pair as a messa di voce, and a lone decrescendo at -2.5. A hairpin with its own hpgain, one starting above CC 66, the `SWELL_*` swells, and the harp and timpani are excluded. The morendo at 298 is also excluded (`HP_SOFT_ACC_SKIP`): the rule's release after the decrescendo made the final ppp chord rise 2.3 dB, and C #5 handles that span. parts.json lists the ramps per track in `hp_soft_acc`.
- **C #5 morendo:** roles.json `_all` [298.5,299.5,-1], [299.5,300.5,-2], [300.5,303.5,-3] (the full version, which chains to -3 through the fermata).

### Tools
- `score_to_parts.py`: `STP_DEBUG_VOL="Track:q1,q2"` prints each volume-envelope item's dB at those qn (stderr). I used it to check that the C #1 trims and ramps combine as intended.

## Rejected or deferred
- B #1's bar 69 notch: not needed (A #1 fixed the cause).
- B #5 (Vln II [221,223,-2]; harp cut at 124-140 eased): left, as the critic suggested. The first works against the c19 soft lift, and the second is not required.
- C #2(c): see above.

## Measured (c21 -> c22)

| | c21 | c22 |
|---|---|---|
| Master integrated / LRA / TP | -22.5 LUFS / 23.6 LU / -3.9 dBFS | -22.5 LUFS / 23.6 LU / -3.9 dBFS |
| mp3 integrated / LRA / TP | -19.8 LUFS / 16.0 LU / -1.6 dBTP | -19.8 LUFS / 16.0 LU / -1.6 dBTP |
| mp3 span / limiter | 18.5 dB / 1.9 dB | 18.5 dB / 1.8 dB |

The scripts used: critic A's `flagged.py` and `spikescan.py` with `CYC=22`, and my `c22-actor/k/chk.py`, which reads K-weighted 50 ms frames of both renders. Levels are K-weighted dB.

- **A #1** (`flagged.py`, peak over body / master rise):
  - Bn1 229: +14.8 / +5.5 -> -3.1 / -0.7. Bn2 232: +13.8 / +4.1 -> -0.6 / -0.9.
  - Hn1 226: +4.2 -> +1.2.
  - Hn3 286 / Hn4 286: +4.1 / +7.0 -> -3.4 / -3.7.
  - Hn3 204: body - 6 dB reached at -0.02 s (was +0.04), peak +2.6.
  - Bn1 196: +9.2 -> +3.6 (the bulge is gone).
  - Hn2 250: +3.4 -> +1.9.
  - Side effect: the Cb's pp entry at 140 starts 3-5 dB softer for 0.4 s (CC1 42 instead of 55). The body is identical.
- **A #2** (`spikescan.py 5`): spiking joins 46 -> 37. All listed joins are now under 5 dB: Ob1 145, Vln I 72/249.5, Vln II 73.5/83, Hn1 180/202. Also gone: Vln I 175/186 and Vc 203. One new join, Vln I 244, at +5.1.
- **B #1:** Bn2 qn 28.25-28.75 -40.6 -> -42.7, against the horn at -37.8. qn 141.5-142.3 -40.3 -> -42.4 (the oboe is at -36.9). This is 2 dB, not the 6-7 dB the critic simulated for roles of -7: the cap leaves part of the f layer (0.37 at CC 36). Bn2 232 entry -36.8 -> -51.1 (A #1).
- **B #2:** Cb 85.07-85.64 -36.8 -> -42.4 (Vln I -43.3). 76.07-76.57 -38.4 -> -43.2 (Vln I -37.7). 64.12-64.50 -42.9 -> -46.8.
- **B #3:** Vc peak 200.5-200.9 -17.0 -> -22.0 (Vln I -24.1). Peak 202.85-202.97 -19.1 -> -22.0. The per-beat Vc levels at 201-203 are unchanged (±0.8).
- **B #4:** Harp 238-262 -47.5 -> -43.5. The master is unchanged (-26.7 -> -26.6).
- **C #1** (stem, median of last third minus first third):

  | Hairpin | c21 | c22 | Target |
  |---|---|---|---|
  | Violin I solo 48-51 | -0.8 | +1.8 | +3, not met |
  | Violin I solo 60-62 | +2.0 | +3.8 | +3 |
  | Horn 1 32-34 | -1.6 | +1.3 | +3, not met |
  | Horn 1 176-180 | +1.2 | +4.5 | +3 |
  | Flute 1 126-128 | -1.7 | +0.7 | +3, not met; the F5 sustain sag remains (critic A's area) |
  | Oboe 1 57-59 > | -1.3 | -2.4 | |

  - The solo violin peak (bars 17-18) is -30.8, against the oboe's bar 20 peak of -30.6 (within 3 dB).
  - The Bb4 at qn 34 (-31.9) is still Horn 1's loudest note in bars 11-13 (31.5-34 at -34.9, 35-38 at -36.4). The crest is 1.1 dB lower than in c21, because its phrase-top lift is gone.
- **C #2:** master per half beat, 186.5-188.5: c21 -24.5 / -27.7 / -30.0 / -28.8 / -27.1. c22 -23.4 / -26.2 / -28.2 / -27.3 / -26.3. The sag is 4.8 dB (was 5.5). The critic simulated 3.8 dB. The rest is the Vln I slur end at 186-188.
- **C #3:** string sum per half beat, 283-288. The crescendo now rises steadily (-45.0, -44.4, -44.0, -42.8, -41.2, -39.3, -38.6). The fall after the arrival, 286 -> 287.5, is 2.9 dB (was 5.2).
- **C #4:**
  - Accompaniment hairpins, group last third minus first third: Vla/Vc 124-128 -0.2 -> +1.7; Vla/Vc/Cb 168-172 +0.7 -> +2.5; Vln II 168-171 +1.2 -> +2.6; strings 223-226 -2.9 -> -3.2.
  - Phrase-scale movement (critic C's 6 s detrended momentary std, median, master) went 1.253 -> 1.229. The critic expected 1.31. Inferred cause: the bumps this cycle removed (A #1, notches) counted as movement too.
- **C #5:** string sum per beat, 298-303: c21 -40.5 / -41.6 / -42.8 / -44.1 / -43.6 / -46.3; c22 -41.1 / -43.0 / -45.2 / -47.1 / -46.6 / -49.1. The morendo falls 6.0 dB to 301 (was 3.6). Final chord (master 301-304): -44.5 -> -47.4, which is 5.6 dB under the opening chord (-41.8). mp3 LRA unchanged.
