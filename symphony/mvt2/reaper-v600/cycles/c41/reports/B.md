# Cycle 41, critic B: balance and levels (on the c40 render)

**Method.** I analysed every stem and the master of `cycles/c40/render/` (final, after the stem fix) and of `cycles/c39/render/` for comparison. Both renders use the same tempo map. Frames were 4096 points with a 1024 hop, both channels summed, and each frame was weighted three ways: approximately K (38 Hz high-pass plus a +4 dB shelf above 1.5 kHz), A, and octave bands. A-weighting is used wherever low and high instruments are compared at soft levels. Levels carry an arbitrary offset, so only differences are meaningful.

Note data came from `cycles/c40/rendered_build/parts.json` and `build/parts.json`, the fills from `build/rebow_fills.json` and `cycles/c39/before/rebow_fills.json`, and the printed marks from `build/mockup-events.tsv`. I also looked at score page 8 (bars 87-92).

Simulations scale stem powers and re-sum. They ignore the hall, so trust them to about 1 dB. "Measured" means a number from the render or the data. "Inferred" means a judgement about what a listener hears.

## Manual notes (B2: May 2021 HO manual pp. 194-200; `loop/MANUAL-GAPS.md` read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.194, p.196: the Mix page has a strip per instrument. Its Sub Mixer channels are the mic positions, each with volume, pan and load/unload. | `build/mix.json` `mics` per track: winds and horns Close + Main, strings Close + Main, DIV tracks Close only. | Followed. Mics are loaded or unloaded by script, and sub-channel pans are 0 with seats written into the mic pans (c05). The Close-only DIV tracks are matched by level (see "Divisi and soli" below), not by mic. MANUAL-GAPS #4 (Mid mics on the solo winds) is still open and not needed for the findings below. |
| p.195: Store/Restore Mix saves all channel settings. | None. | Not used, correctly: the mix lives in `mix.json` and is rebuilt by `build_reaper.py`, which the brief requires. |
| p.196-198: FX Bus channels carry a Reverb insert. Sub Mixer channels feed it through an Effects Send with a level and a Pre/Post switch. "For reverb, post fader is typically used", so the main mix and the send stay in proportion. | The shared hall: `reverb.send_pre_fader` (c09) with level = send x channel volume, fx_volume 0.095, low cut 160 Hz, ir_setup 0.7. | Followed in effect. The pre-fader send is scaled by the channel volume, which is what post-fader gives. Balance moves made in REAPER's volume envelope act after the hall and move dry and wet together. Moves made in CC7/CC11 act before it (BRIEF S3). The fixes below say which they use. |
| p.199-200: Opus EQ inserts (Bass Comp 32-256 Hz, 3-band Channel Equalizer, 6-band Equalizer) can sit on any channel, including a mic sub-channel before its send. | The ReaEQ chains in `mix.json` (`eq`, `loud_eq`, `side_shelf`) sit after Opus, so they shape the instrument's hall return as well as its dry sound. | A deliberate difference, not a fault. A low-mid or bass cut in ReaEQ also cuts that instrument's share of the hall, which the 160 Hz hall low cut mostly makes moot. No finding here needs an Opus insert. The Cb bell in finding 5 is post-hall and windowed, like the existing `loud_eq`. |

MANUAL-GAPS: #8 (basses 4 soli on DIV A) remains timbre only. After finding 1 the 4-soli level is consistent with the tutti, so it is not needed for balance.

## Extra check: did the c40 caps thin the accompaniment under the uncapped wind solos? Which c39 balance fixes should be undone? (measured)

**The thinning did not happen at phrase level.**
- For each solo bar I measured the solo over the summed accompaniment, A and K, c39 against c40. Within ±1 dB everywhere: Horn 1 bars 7-14, Oboe 1 15-20, the solo violin 17-21, the bass clarinet 31-36, Flute 1 37-44, the cor anglais 41-50, Oboe 1 45-47, Clarinet 1 85-89.
- The accompaniment's per-bar mean and its 10th-percentile level (the dips between chords) also moved by under 1 dB.
- The solos in bars 37-50 lost 0.5-0.9 dB of K margin because c40's celli/basses gain went up by 1.5 dB, not because the strings thinned. The caps act on phrase ends followed by silence, and the accompaniment here is legato or pizzicato.
- The one solo that lost real margin is Horn 1 in bars 66-68: A +5.1/+14.5/+7.2 fell to +2.2/+12.1/+6.2, because the basses got louder (finding 1).
- No solo lift is needed.

**The three c39 fixes.**
- **Basses +3 at 226-238 (c39 B #4): undo it.**
  - c40's +1.5 gain and refitted pedal fills already raised the pedal by about 3 dB against c39 (finding 1). Without the +3, the pedal lands at c39's level.
  - Simulated basses minus Horn 1, K per qn: -7.9..-14.6 at 226-230 (c39 B's target was 11-15 under) and -3.4..-8.6 at 231-237, where the horn is pp.
- **Bars 79-80 Violins II CC7 -4.5 (c39 B #1): undo most of it.**
  - The c40 refit added a -1.3..-3.9 dB fill on the same 263.921 re-bow, so the bloom is corrected twice. The refit also dropped c39's +2.5 dB on the Violins I 264.417 fill.
  - Finding 2 gives the numbers and the partial undo (CC7 76 -> 101, Violins I +2.5 back).
- **Bars 61-62 Violins I +3, Horn 1 lift 5.5, Violins II CC7 -2.5 (c39 B #2): keep.**
  - Violins I is the loudest stem in A on every half beat 204-212. The margin is +0.8..+5.5, with the smallest +0.1 at 209.5 against the celli.
  - In K the celli pass it by 0.1-2.5 dB at 208.5-209.5, but that is their 100-250 Hz energy, not presence.
  - Trombone 2 (printed f) now sits 3.2-3.5 dB under Violins I (A) at 205-208, and the bass trombone 5.5 dB under. They do not cover it.
  - The timpani are 18-22 dB under the master (A) at 204-206 and rank 13-20. In the 63 Hz octave they are -3 to -10 dB re master, so they are audible as the low floor without covering anything.

## 1. Bars 65-70 and the coda: the basses' 4-soli pedal is now too loud and swells in step with its re-bows (measured; audible as a pulsing pp pedal under the horn solo, inferred)

**Where.** Double basses, the E flat 2 "4 soli, sul A" pedal, qn 220-238, under Horn 1 (p dolce at 226, mp at 229, pp at 235). Also the coda A flat 1 pedal, 273-286 (ppp, under the timpani answer at 277-280).

**Evidence (measured).**
- **Level against c39 (K per qn).** 221-225 +1.0..+2.2 dB, which is the +1.5 gain. 226-237 +0.4..+7.5 dB.
- **Bumps in the pedal (per 0.25 qn).** +8.5 at 226.5, +7.1/+10.9 at 231.5/231.75, +7.4/+7.7 at 236.75/237.0, and +3.6..+4.7 at 228.5-229.25 and 234.0-234.5.
  - Each bump comes 1.3-1.6 s after a re-bow (225.215, 227.775, 230.393, 233.038, 235.659), at 52 bpm.
  - That is the Basses KS Master's own E flat 2 swell at "moved start + 1.40-1.95 s" (series 1 c22 note in `score_config.py`).
  - c34 cancelled it by fitting these pedals with `fit_rebows.py --window "Double basses:2.6"`. The c39 lists run to 2.6 s and dip to -4..-5 dB at 1.5-1.9 s.
  - The c40 refit ran without `--window`, so every list in `build/rebow_fills.json` (221.8-235.659) now ends at 1.48 s on a +3..+6 hold. The swell is no longer cancelled.
- **Dynamic mapping between passages.** One printed pp now plays at three levels:

  | Passage | Printed | K | A |
  |---|---|---|---|
  | 4-soli pedal, 226-238 | pp | 20.0 | 11.0 |
  | Tutti, bars 71-74 | pp | 18.2 | 5.6 |
  | 4 soli, coda 286-298 | pp | 12.8 | -0.8 |

  The 4 soli at 226-238 are louder than the tutti at the same printed pp.
- **Against Horn 1 (K).** At 234-237 the basses are within 0.4-3.2 dB of Horn 1. c39: 1.6-5.5.
- **Coda.** The A flat 1 pedal is 2.5 dB over c39 on average (K mean 13.2 -> 15.7), with +3.4..+5.3 at 275.5-276.5 and 277.5-279.5 after the 276.05 / 278.351 re-bows. That is the same missing window, plus the gain.

**Fix.**
1. `build/score_config.py` line 876: delete `LEVEL_SHAPES["Double basses"] += [[(226.0, 0.0), (226.5, 3.0), (237.6, 3.0), (238.0, 0.0)]]` (c39 B #4).
2. Refit the two pedals with the c34 window and re-levelling:
   - Run `tools/fit_rebows.py 40 cycles/c40/rendered_build/parts.json --hold-max-after 301:0 --window "Double basses:2.6"` (with `--stems` on the stem-fixed c40 stems, if that is the current practice).
   - Then re-level each list so that each piece keeps its c39 piece mean minus 1.5 dB (the new gain), as c34 did for c29-c33.
   - Keep 273.229 unfilled (c29) and keep c40's x0.6 / x0.5 attack scaling on 276.05-283.605.
3. If a refit is not possible this cycle, a stopgap: append c39's points from 1.52 s to 2.6 s (`cycles/c39/before/rebow_fills.json`) to each c40 list 221.8-235.659, shifted so the first appended point equals the c40 list's last value.

**Expected (simulated for step 1 only).** Basses minus Horn 1, K: -7.9, -14.6, -12.4, -13.8, -10.7 at 226-230; -6.1, -8.6, -7.5, -4.6, -3.4, -3.5, -6.2 at 231-237. A: -7.4..-17.4. Pedal K mean 16-17 (c39 16.3, tutti pp 18.2).

**Check.**
- Basses per 0.25 qn over 226-238: range at most 6 dB (now 12.5).
- Horn 1 at least 6 dB over the basses (A) at every qn.
- The bar 66 niente still falls at least 7 dB in the master (223 -> 225.5).
- Coda basses per 0.5 qn within 2 dB of c39 + 1.5.

S3: the deleted shape ended on the 238 tutti onset and the fills are pre-existing shapes, so no new tail cut.

## 2. Bars 79-80 (qn 263.9-265.8): Violins II is corrected twice, and the ff "molto sostenuto" sags in bar 80 (measured)

**Evidence.**
- **Violins II (A) against c39.** -2.6/-2.9/-2.9/-2.2 dB at 264.0/264.5/265.0/265.5. The CC7 -4.5 (c39) now stacks on the new c40 fill for re-bow 263.921: -1.3 dB at the join, -2.0..-3.9 dB from 0.16 s, holding -2.9.
- **Violins I.** -0.4/-0.7/-2.5/-1.9 dB against c39 at 264.0-265.5. The c40 refit of 264.417 sits at the -6 clamp from 0.76-1.12 s and dropped c39's "+2.5 dB from 0.6 s".
- **Result: Violins I over Violins II (K).**
  - 263.75-264.75: +4.1..+5.1 (c39 +2.1..+3.4; c39 B's criterion was at least +1).
  - The master falls 0.4-0.7 dB (A) at 264.75-265.75, in the cadence the score marks ff molto sostenuto with no hairpin until 268.
  - Both sections now sag inside a held ff note.

**Fix.**
- `build/score_config.py` line 855: Violins II `CC7_POINTS` (263.94, 127), (264.0, **101**), (265.75, **101**), (265.8, 127), i.e. -2.0 dB instead of -4.5. Pre-hall, same times, so no new tail cut.
- `build/rebow_fills.json` "Violins I" "264.417": add +2.5 dB to every point from 0.6 s to 1.763 s. This is c39's change re-applied to the refitted list, so the clamp floor -6.0 becomes -3.5.

**Simulated (stems, ±1 dB).**
- Violins I over Violins II per 0.25 qn 264.0-265.75: +2.0, +1.7, +2.6, +1.6, +2.6, +2.6, +1.2, +3.1. All at least +1.
- Master A 264.0-265.75: 46.9 / 46.2 / 46.2 / 45.3 / 45.3 / 47.1 / 45.9 / 45.5. c39: 46.9 / 46.4 / 46.3 / 45.5 / 45.3 / 47.1 / 45.8 / 45.3.

**Check.**
- Violins I is the top string stem (A) on every 0.25 qn 262-265.75.
- Climax order holds (bars 61-62 louder than 79-80 by at least 3 dB in the master).

## 3. Bars 56-58 (qn 182-196): Horn 1's espr. counter-melody drops 10-17 dB under the violins' theme where the score has it one step under (measured; audibility inferred)

**Where.** Horn 1 mp from 182 ("1., espr." at 175, pp < mp), mp < from 188, f at 196. Violins I/II mp at 178, mf at 184, cresc. to f at 196.

**Evidence.**
- **Horn 1 minus Violins I, per bar.** Bar 55 -5.9, bar 56 -10.7, bar 57 -9.4, bar 58 -8.7, bar 59 (both f) -3.2 dB (A).
- **Per 0.25 qn.** -9.9..-17.1 at 183.0-183.75, -7.6..-13.5 at 184-188, -10.4..-15.0 at 188-189.75.
- **Two causes:**
  1. The soft-horn shelf (`mix.json` Horn 1 `loud_eq`, 800 Hz -8 dB) is fully wet until 186 and ramps out only by 194, so the mp counter-melody plays with the p/pp colour.
     - Removing that shelf adds +4.4 dB A at 182.5-184 and +2.7 at 184-188 (simulated from the horn's octave bands).
     - c37 set the shelf for the p/pp layers. Its 1-5 kHz target was measured at p, not mp.
  2. The 182 arrival collapses inside the note. K 35.1 at 182.5, 21.8-24.1 at 183.0-183.75.
     - That is an 11-13 dB fall in a two-beat mp note. About 4.5 dB of it is the envelope (early fill 182 +4 dB for 0.43 s, plus the 176-182 hairpin gain ending). The rest is the legato head over the body.
     - The same fall was in c39 (K within 0.3 dB).
- **What the score and the books ask.**
  - One printed step under the theme, about 4-5 dB on this mockup's scale (c39 B #4), not 9-17.
  - Rimsky-Korsakov, *Principles*, PDF p.41: horns played softly have "the same weight as other brass instruments played softly". At mp a single horn is a full melodic voice against a string section, not a background colour (inferred).

**Fix.**
- `build/mix.json` Horn 1 `loud_eq[0].points`: replace `[186, 1], [194, 0]` with `[180, 1], [182, 0]`. The wet-0 spans 194-220 and 261-270 from the c32 do-not-touch stay, and so does the pp entry at 175-180.
- `build/score_config.py`: `LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES.get("Horn 1", []) + [[(182.6, 0.0), (182.95, 5.0), (183.8, 5.0), (183.9, 0.0)]]`. This lifts the 182 body back toward its head. The shape is inside the note and returns to 0 before the 184 legato target, so no tail is cut.
- Then refit Horn 1's mp soft trim by stem fix if the shelf change moves the 182-194 mean by more than 1 dB over the target below.

**Expected.** Horn 1 minus Violins I (A) -4..-8 dB on every 0.25 qn 182.75-195.5. Horn 1's 1-5 kHz share at 182-194 between -19 and -15 dB (between c30's measured p -21.4 and f -14.6).

**Check.**
- The Horn 1 1-5 kHz share at the pp bars 54-55 (175-181) is unchanged.
- Bassoon 1 and Clarinet 1 (p/mp under the horn) stay at least 4 dB under Horn 1. Now +5.7..+8.4 (A), so there is room.

## 4. Divisi and soli tracks against the full sections, and the dynamic mapping between families (measured; no change needed except finding 1)

- **Median A level by printed dynamic over note bodies.**

  | Printed | Instrument | A |
  |---|---|---|
  | p | Flute 1 | 26.1 |
  | p | Oboe 1 | 25.9 |
  | p | cor anglais | 24.4 |
  | p | bass clarinet | 20.8 |
  | p | Horn 1 | 20.1 |
  | p | Violins I | 25.6 |
  | p | Violins II | 23.7 |
  | p | celli | 19.9 |
  | pp | winds and horns | 10.3-21.4 |
  | pp | strings | 12.1-16.6 |

  This matches Rimsky-Korsakov's piano balance (p.51, cited by c40 B) within the register effect of A-weighting.
- **Half-section and soli tracks against their sections at the same mark.**
  - Violoncellos div pp 13.6 against celli pp 13.5.
  - Violins II div pp 15.8 against Violins II pp 16.6.
  - Violas div ppp/pp/p 4.9/8.7/19.2 against violas 3.0/12.1/17.8.
  - The Violin I solo at p is 27.5 against Violins I at p 25.6 (its solo role +2).
  - All within about 3.5 dB.
- **The final chord (301.3-303.8, K).** Violins I 10.0, Violins II 8.0, violas 6.6 + div 8.7, celli 10.8, basses 6.2, Clarinet 2 8.2. The top C5 leads by 1-2 dB, and no section is buried.
- **The one inconsistency is the basses' 4-soli pedal at 226-238** (finding 1).

## 5. Bars 76-78 (qn 256-262): the basses' E flat 2 / E2 fundamental is 9 dB under its own octave, so the f crescendo has no floor (measured; "not solid" inferred)

**Evidence.**
- **Master 56-125 Hz re 500-2000 Hz.**
  - 256-262: -18.3 dB. 262-265: -15.4. 265-268: -9.6.
  - Bars 61-62: -11.3 (c39 -12.5).
  - c40 B measured -8.9 for Dvořák 9/i's loudest 10%.
- **Basses stem at 256-262.** 78/82 Hz at 60.5/59.8 against 156/164 Hz at 69.5/69.4, so the fundamental is 9 dB under the 2nd harmonic. Three cuts stack here: the static `bell2` 80 Hz -6, the `loud_eq` 100 Hz shelf -3 (wet 1 from 259), and the patch's weak recorded fundamentals.
- **The D flat 2 at 262-266.** 69 Hz 65.8 against 138 Hz 64.4, already level. This is series 1 c16's boom note, so the climax shelf's reason still holds at 262-266 and at 204 (also D flat 2).

**Fix.** `build/mix.json` "Double basses" `loud_eq`: add a second entry `{"points": [[254, 0], [255, 1], [261.6, 1], [261.9, 0]], "bands": [{"band": "bell", "hz": 80, "db": 4, "bw_oct": 0.5}]}`.
- It is wet only over the E flat 2/E2 notes of bars 76-78 and gone before the D flat 2 at 262.
- Keep the existing entry (100 Hz -3, 150 Hz +4) and the static bells unchanged.
- This replaces c40 B #2's 78 Hz proposal, which also touched bars 61-62.

**Check.**
- 56-125 Hz at 256-262 between -15 and -12.
- 69 Hz at 262-265 unchanged.
- Delivered limiter at most 2.5 dB (bars 76-78 are 4-5 dB under the climax peak, so a 4 dB bell on one stem's fundamental should not reach the limiter; inferred).

S3: the wet ramp-out (261.6-261.9) is post-hall but falls at the 261-262 pitch change of a crescendo, not under a decaying chord.

## 6. Climax covering and roll levels: no change (measured)

- **Bars 61-62 (204-212, A).** The low brass sit under Violins I: Trombone 2 -2.4..-3.5, the bass trombone -3.0..-5.5, the tuba -9..-14.
- **Bars 63-64.** Trombone 1's ff quotation is 8-15 dB over the p tremolo strings (213-218), as the marks ask (ff against p).
- **Timpani.**
  - Bars 61-62: the roll starts at A 33-38 at 203-204 and falls to 25-27 by 205-206.
  - Bars 79-81: 28.8 at the f entry (262), 22 under the texture after. In the 63 Hz octave it is -3..-14 dB re master, so it is heard as the low floor.
  - Rank 13-21 of 32 throughout. This follows Dan's rule 5 (start at the printed level, then settle).
- **Bars 79-82 have no low brass.** The contrabassoon (ff) sits 9-12 dB under Violins I (A).

**Do not touch:**
- the c39 bars 61-62 balance (Violins I +3, Horn 1 lift 5.5, Violins II CC7 -2.5);
- Trombone 1's level and CC7 110/120 at 212.5-219.5;
- the timpani levels at bars 61-64, 79-82 and 84-85 (strokes +4..+6 dB A over the celli pedal at 277/278.5/279);
- the solo levels of the winds, Horn 1 bars 7-14 and the solo violin (unchanged within 1 dB by the caps);
- Clarinet 1 and the cor anglais as an equal pp duet in bars 87-89 (printed so);
- the divisi/soli track levels listed in finding 4;
- the final-chord balance;
- fx_volume 0.095, the 160 Hz hall low cut and ir_setup 0.7;
- the celli gain +1.5;
- the static Cb bell2 80 Hz and 160 Hz bells, and the basses' existing climax loud_eq entry (100 Hz -3, 150 Hz +4) as set.
