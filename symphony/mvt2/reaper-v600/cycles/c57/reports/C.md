# Cycle 57, critic C: whole-piece check of the c56 render (no per-note volume), doubles, phase, envelope density, mix; dynamics over time

Material: `cycles/c56/render/` (delivered stems and master, after the ten-row stem fix) with `cycles/c56/build_fix/parts.json` and `mix.json`; `cycles/c56/mvt2-mockup-c56.mp3`; for comparison `cycles/c55/render/`, `cycles/c54/render/` and `cycles/c54/build_fix/`. The written envelope is `tools/build_reaper.py` `vol_points` with the source cut before `ENV_LUA` (nothing sent to REAPER). Scratch, left in place, 25 MB, no audio: `/private/tmp/claude-501/mockup-loop/mvt2-c57-C/` (`cache.py`, `arc.py`, `hp.py`, `line.py`, `phase.py`, `dbl.py`, `wob.py`, `mixm.py`, `sim.py`, `envs.py`; `basses_pulse_cc11.json` holds the fitted lane of finding 2).

Method: 10 ms power frames and third-octave frames (50 ms hop) of every stem and master of c54, c55, c56; note body = 20-80 % of the note; ffmpeg `ebur128` on masters and mp3s; per-note left/right correlation and band analysis read from the stems in memory. "Estimate" below means dry-sum arithmetic on the c56 stems (master power plus the changed stem power, returns not modelled). Everything else is measured unless marked inferred. No fix below is a track volume move on a note; every proposal is CC11, CC1, note timing, a row choice, a region gain, or a mix value.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 57 (its last row is cycle 47), so no page range was read. Used from `loop/MANUAL-GAPS.md` and the kit:

| Source | Where it applies | Render follows it? |
|---|---|---|
| HO manual p.89-90 (MANUAL-GAPS 8): DIV A / DIV B patches are half sections with Close mics only | the three doubles of c56 (Violin I solo, Violins II div, Violoncellos div) and Violas div | Yes, and it is the cause of finding 5: each DIV stem is mono (L/R correlation 1.00), so a doubled span is narrower than the single section |
| HO manual p.138-139 (MANUAL-GAPS 4): Close = presence, Main = unified sound; each mic loads its own samples | Horn 1 (Close 0.48, Main 1.0): two pitches are out of phase between L and R (finding 5) | The anti-phase is in the recorded Main pair; no setting was changed for it |
| Kit LEARNINGS line 157: string sustains loop, long pp notes pulse 10-15 dB, the same in every render; an inverse periodic profile cut it 1-6 dB | Double basses' A flat 1 pedal, bars 82-85 and 90-92 (finding 2) | The c54 envelope flattened three of these notes; that layer is off since c55 |
| Kit LEARNINGS line 66: CC11 gives 5.7 / 3.5 dB per 10 steps at CC 0-40 / 30-60 | every CC11 value below | Used for the expected sizes |
| BRIEF S2 and `score_config.py` lines 1258-1346: the bar 47 fp was put on the beat with a fader shape in c48-c50 | finding 3 | The shape is a per-note move and is off; the attack is late again |

## Slot C part

### 1. Whole piece: c56 against c55 and c54

Delivered mp3: -19.8 LUFS in all three; LRA 15.1 / 15.4 / 15.3 LU; short-term 10th percentile -28.4 / -28.8 / -28.5, maximum -10.3 / -9.7 / -10.1 LUFS, span 18.1 / 19.1 / 18.4 dB (limit 19); true peak -1.5 dBFS. Master -23.2 LUFS, LRA 24.2. Climax over the ff cadence: bar 61 -13.8 against bar 79 -18.8 dB (5.0; c54 5.3). Bars 53-61 rise every bar except the printed restart at 57: -35.3, -29.8, -28.5, -25.7, -26.4, -23.1, -21.3, -17.3, -13.8.

Master bars off c54 by 1.0 / 1.5 / 2.0 dB or more: c55 32 / 20 / 11, c56 28 / 10 / 4.

| passage | against c55 | against c54 (what is left) |
|---|---|---|
| bars 1-6 | better: the Violins I pair at the first bow change reads -49.5 dB (c55 -53.5), the second -49.4 (c55 -54.4) | level within 0.5 dB per bar; the doubled C5 is 2.5 dB brighter at 2-5 kHz and narrower (part 3) |
| 7-14 Horn 1 theme | better in bars 11 and 13 (bar 11 +1.5 against c54, was +3.0) | bar 9 -1.4, bar 12 -1.8, bar 14 +1.4; the crescendo 30-34 still arrives flat (finding 4); 37.5 is 6 dB under both neighbours (unchanged from c55) |
| 15-22 | better: Oboe 1 heads 42 and 54 back (-44.0 and -48.7; c55 -51.5 and -53.3); Violins II 47 lifted | bar 16 +1.6 (Oboe 1 45 is +3.2, so the decrescendo 45-47 starts hot and reads flat until the last note); bar 20 -2.0 (Oboe 1 55.5 -6.3, 57 -3.9) |
| 23-30 violins' theme | better: crescendo 78-82 arrives +4.0 / +7.3 dB (c55 reversed); bar 30 +1.0 (was +3.2) | bars 25-26 +1.5 / +1.4 (celli +2.3, Violins II +1.9); celli decrescendo 74-77 reversed (+2.4; c54 -2.0) |
| 31-36 | better: bar 35 +1.0 (was +3.9) | bar 31 -2.3 (Bass clarinet 91.5 -4.0, 92 -2.8); margin +5.6 unchanged |
| 37-44 | better: bar 44 +1.2 (was +3.3) | bar 40 -1.7 (Flute 1 -2.8); Cor anglais 131.5 and 133.5 are 7.5 and 2.7 dB under c54 (the decrescendo 131-136 reads 0.0, c54 -4.3) |
| 45-52 | better: bar 48 +0.1 (was +3.0) | the fp of bar 47 peaks 210 ms after the beat (finding 3); bar 51 -1.3 |
| 53-60 | unchanged | bars 53-55 +0.7 to +1.1 (Horn 1 +2.5, celli +1.8); the rise per bar is intact |
| 61-64 | better: bar 63 downbeat -17.1 (c55 -19.9, c54 -17.5), monotonic fall after it | bar 62 first half 2.7 dB under the quarters around it (c54 1.0; finding 6); Trombone 1's tenuto 216 -2.6 dB, its margin over the rest +4.8 (c54 +6.4) |
| 65-70 | better: the down-bow at 223 drops the strings 2.8 dB (c55 4.5) | c54 had no drop there; after it the strings are flat for 1.5 beats (basses +3.4 at 224) before the fall to niente; Horn 1 margin +7.1 (c54 +6.9) |
| 71-78 | better: bars 71 and 73 +1.0 / +0.9 (were +3.2 / +2.7) | every bar 71-77 +0.8 to +1.2 (celli and basses +1.6, Clarinet 1 +5.8); bar 78 -1.3 |
| 79-82 | bar 82 2.3 dB lower (Flute 1 -9.3, basses -3.1) | bars 79-81 within 0.2; bar 82 -1.9: the close falls -36.7, -38.5, -42.6 into -46.0 at 274 |
| 83-92 | better: bars 87-89 within 1 dB (were -1.7 / -1.7 / +2.0) | bar 84 +2.2 (timpani +3.9), bar 86 -1.4 (basses -6.4), bar 91 +1.3, bar 92 +2.1; the basses' pedal pulses (finding 2); the final chord is as loud as the second half of the morendo bar (finding 1) |

Printed hairpins on the stems (114 crescendos, 119 diminuendos that sound at both ends), c54 / c55 / c56: median change +4.4 / +4.8 / +4.4 dB and -5.2 / -4.9 / -4.8 dB; reversed 4 / 8 / 5 and 5 / 8 / 10; crescendos whose arrival note is under their start 8 / 15 / 11. Solo margins (lead minus the sum of the other stems) are within 1 dB of c54 except Trombone 1 212.5-219.5 (+6.4 -> +4.8) and Oboe 1 140-148 (-0.7 -> +2.0).

### 2. Does anything sound less natural than with the old automation, and is it one of Dan's notes?

- BRIEF item 8 (pulsing on long notes): yes. Double basses' pedal at 273.2, 278.4 and 299.8 swings 11-12 dB on the stem with a 1.3 s period (c54 2.6-7.7 dB); the master swings 5.5-6.7 dB there (c54 2.4-3.9). Finding 2.
- BRIEF item 8 (re-bows): Violas, Violas div and basses dip 4.2-4.9 dB at bow changes (c54 0.8-1.2); slot A's item.
- S2 (attack on the beat): the fp of bar 47 is 210 ms late on the master (c54 110 ms). Finding 3.
- "Themes not choppy": level steps of 6-8 dB onto short notes inside slurred wind lines (Cor anglais 131.5, Oboe 1 55.5, Horn 1 37.5); slot B's item. Soft starts of 6 dB or more 71 (c54 32).
- S1: 49 repeats, median stem dip 8.5 dB, 5 under 3 dB in their own band (c54 5); no change.
- S3: no cut tail. The fastest envelope falls left inside sounding notes are the timpani roll rules (262: -5.9 dB in 0.25 s) and one Clarinet 1 edge (262.16: -2.3 dB); 13 moves of 1.5 dB or more (8 on the timpani), 7 of 2 dB or more (6 on the timpani).
- "Too wet and mushy": unchanged. Returns against the dry stems -16.9 dB (c54 -16.9); side/mid -5.8 dB (-5.7); 315-500 Hz against 1 kHz in bars 7-30 +2.5 dB (c54 +3.5); 2-4 kHz share of bars 7-30 -11.6 dB (c54 -11.1, c55 -12.0).
- Accents: movement II prints two (Trombone 1 213 and 218). 213 is +2.9 dB over its pickup, 218's front is 0.6-1.0 dB under 217.5; neither is overdone. The tenuto at 216 between them lost 2.6 dB to the CC lowering made for 218 (CC11 92 against 104, CC1 -4).

### 3. Doubled held notes: stereo image and timbre

| span | pair c55 (single) | pair c56 (main + copy) | copy alone |
|---|---|---|---|
| Violins I bars 1-3: side/mid, L/R correlation | -3.8 dB, 0.58 | -5.4 dB, 0.72 | -10.8 dB, 1.00 |
| the same: 2-5 kHz share, centroid | -14.1 dB, 626 Hz | -11.6 dB, 720 Hz | -9.5 dB, 848 Hz |
| Violins I final chord: side/mid, correlation | -4.1, 0.56 | -5.8, 0.74 | -10.8, 1.00 |
| Violins II final chord | -4.9, 0.52 | -7.9, 0.76 | -14.7, 1.00 |
| Violoncellos final chord | -4.4, 0.53 | -7.2, 0.73 | -16.1, 1.00 |
| master, qn 292-304: side/mid, correlation | -9.1, 0.78 (c54 -7.5, 0.70) | -9.9, 0.81 | |

The copies are mono, so each doubled pair is 1.7-3.0 dB narrower than the section alone. On the master the last 30 s are 2.4 dB narrower than c54; 1.6 dB of that was already in c55 (the basses, which sit in the middle, are louder), 0.8 dB is the doubles. Timbre: the final chord is unchanged within 2 dB; the opening C5 is 2.5 dB brighter at 2-5 kHz because DIV A is brighter than the section at ppp. No chorusing: the fundamental-band level wobble of the pair (50 ms frames, detrended) is 4.4 dB standard deviation against 5.5 for the section alone in bars 1-3, 4.1 against 5.0 in the final chord. No level bump where the two overlap: the pair stays inside -44.6 to -50.7 dB through bars 1-3 where c55 fell to -54.4 and -56.9 at the bow changes. Pair level against c54: bars 1-3 +1.0 dB, final chord +1.9 dB on all three pairs (finding 1).

### 4. Horn 1: left/right phase per held note

Per note, the fundamental band and the whole note (c56 stem):

| note | where | fundamental L/R correlation | mono-sum loss at the fundamental | whole-note correlation |
|---|---|---|---|---|
| A flat 4 (68), 35.0 | bar 12, theme, exposed | -0.40 | 4.9 dB | 0.01 |
| B flat 4 (70), 34.0 | bar 12, the printed mp top of the theme | +0.21 | 2.4 dB | 0.14 |
| A flat 4, 188.0 | bar 57, counter-melody | -0.73 | 8.2 dB | -0.10 |
| B flat 4, 178.0 | bar 54 | +0.15 | 2.4 dB | 0.08 |
| A flat 4, 210.0 (ff layer) | bar 62 | +0.49 | 1.4 dB | 0.86 |
| the other 16 held notes | | 0.56 to 1.00 | 0.1-1.8 dB | 0.62-0.97 |

Horn 3 (same patch) reads -0.19 and -0.34 on the same two pitches. Horns 2 and 4, the a2 patch and Trombone 1 have no fundamental under +0.79. So the two highest notes of the horn theme in bar 12 are decorrelated between the speakers while the notes around them are at 0.72-0.97: on headphones the horn widens for those two notes. The soft and mp layers are affected, the ff layer is not. Finding 5 has the test.

### 5. Envelope points per second against the references

| project | points per second per track |
|---|---|
| EW templates | no volume envelope on any track |
| Duc, Mahler Adagietto / LOTR | 0.01-0.21 / 0.02-0.12 |
| movement II c54 | strings 4.8-7.1 |
| movement II c55 | strings 0.44-0.66, winds 0.06-0.34, brass 0.06-0.25 |
| movement II c56 | strings 0.40-0.63 (Violins I 0.40, Violins II 0.54, Violas 0.63, Violoncellos 0.51, basses 0.41), winds 0.05-0.36, brass 0.05-0.22; 2,343 points |

What the 2,343 points are (items in `vol_tags`): roles over three or more notes 384, slow level rows 235 (117 of them the section rows of `cell_rows_c56.json`), hairpin gains 207, timpani roll rules 20, fades and chord cut 12. Median gap between points 0.45-0.9 s on the strings, median step 0.7-0.9 dB: ramps written as chains of small steps.

What remains to thin, in order of size:
1. Simplification tolerance. A line simplification of the written points at 0.5 dB (now `env_simplify_db` 0.2) leaves 1,618 points (estimate, dB against seconds; the tool works in fader scale): strings 0.25-0.36 per second, winds at most 0.25, brass at most 0.16. At 0.75 dB: 1,410 points, strings 0.23-0.31. The level error this adds is below the 0.7-0.9 dB median step. Offline, one value in `build/mix.json`.
2. The 117 section rows (slot B sorts them by cause). Each row costs four points.
3. Hairpin gains (207 items): the references carry hairpins in CC1 / CC11. Moving them needs the CC11 slope per track and dynamic and is too large for one session.

### 6. Wetness, bass share, span, LRA

| measure | c54 | c55 | c56 |
|---|---|---|---|
| returns against dry stems, whole / bars 23-30 / coda | -16.9 / -21.9 / -12.4 | -17.0 / -21.6 / -11.1 | -16.9 / -21.7 / -11.9 dB |
| side/mid, whole | -5.7 | -5.9 | -5.8 dB |
| 63-100 Hz share, whole / bars 71-74 / bars 79-81 / coda | -12.1 / -11.6 / -11.5 / -7.3 | -10.7 / -7.4 / -9.4 / -7.6 | -11.7 / -9.8 / -10.5 / -7.7 dB |
| 125-315 Hz share, whole | -5.5 | -5.3 | -5.5 dB |
| 315-500 Hz against 1 kHz, bars 7-30 | +3.5 | +2.7 | +2.5 dB |
| delivered LRA / span / limiter | 15.1 / 18.1 / 1.0 | 15.4 / 19.1 / 1.6 | 15.3 / 18.4 / 1.9 |

The A flat 1 region gain took bars 71-74 from -7.4 to -9.8 dB; the c55 shelf is still visible in the tutti bars, as intended. Nothing to change in the mix. I did not re-measure a recording; the Brahms figures in `shares_c56_fix.txt` (56-112 Hz -7.9 / -7.3 dB) are stored values and the master is still 3-4 dB under them.

### 7. For the owner: what the no-per-note rule cost and gained in this movement

Gained:
- The track view: 22,022 envelope points became 2,343; 1,245 per-note items became 0. The strings carry 0.4-0.6 points per second, which is 2-3 times the densest track in Duc's Mahler project instead of 30 times and more.
- Fader moves of 1.5 dB or more inside a sounding note: 13, and 8 of them are the timpani roll rules.
- The loudness arc survived: 88 of 92 bars are within 2 dB of the c54 master, the loudness range and the climax height are unchanged (LRA 15.3 LU, climax 5.0 dB over the ff cadence).
- Three faults are now fixed in the instrument where a real player would fix them: the opening note and the final chord are bowed by two half-sections in turn (bow-change dips 2.3 dB on Violins I, 1.5 on the celli), the bar 63 sf is as loud as the bar before it, and single hot pitches (basses' low A flat, Horn 1) are corrected in the sampler.

Cost, still audible:
- The basses' low pedal note throbs every 1.3 s by 11-12 dB at the start of the coda and under the last chord (5-8 dB before).
- Bow changes on Violas and basses dip 4-5 dB (1 dB before).
- 71 soft notes start 6 dB or more under their body (32 before); 24 legato joins have a 5-13 dB burst (2 before).
- The fp of bar 47 arrives 0.2 s late (0.1 s before).
- 15 of 233 printed hairpins run the wrong way on their track (9 before), among them the top of the horn theme in bar 12.
- The final chord is 2.7 dB louder than it was and no softer than the end of the bar before it.
Findings 1-4 and 6 below remove or shrink the last four without a fader move.

## Findings

Ranked for one lock session. "Must do" marks four.

### 1. MUST DO. Bars 91-92: the morendo stops falling halfway and the ppp final chord is as loud as the end of it, 2.7 dB over c54 (measured; decidable offline, CC11 lanes only)

Where: qn 298-304, all strings, Clarinet 2.

Evidence. Master per half beat (0.75-0.8 s at this tempo). Bar 91 from qn 298: -43.7, -43.3, -45.4, -48.4, -48.4, -46.8; the chord from 301: -49.6, -47.5, -48.7, -48.6, -51.0, -55.1. c54: -44.4, -45.1, -46.6, -47.7, -49.3, -50.7; chord -52.2, -51.3, -50.8, -50.7, -51.9, -55.9. In c54 bar 91 falls 6.3 dB without a rise and the chord lies 1-2 dB under its end. In c56 bar 91 falls 4.7 dB, rises 1.6 dB on its last half beat (the basses' swell at 300.7, finding 2), and the chord's first three beats (-48.6 dB) are level with bar 91's second half (-47.9). The chord over 301-303 is at -48.5 dB against -51.2 in c54. Violins I's printed decrescendo 298-301 reads -0.9 dB on its stem (c54 -6.1). Stems over 300.4-303 against c54: Double basses +4.8 dB (41 % of the change; -53.4 dB, the loudest stem of the chord), the three doubled pairs +1.9 each, Clarinet 2 +2.9. Cause: in c54 the envelope carried the fall (basses' envelope -5.6 dB at 298 to -12.8 at 301; Clarinet 2 -0.8 to -4.6); the c56 CC lane (33 at 298.3, 20 at 301, 15 at 303.5) replaces about half of it, and the copies add level.

Fix (`build/score_config.py`, the c56 block, the "set" lanes at lines 1926 and 1944):
- Double basses: `(11, [(298.3, 33), (300.4, 22), (301.0, 13), (303.5, 10), (303.75, 9), (303.94, 8), (304.0, 8)], "set")`. That is 7 units lower from 301 (about -4 dB at 5.7 dB per 10) and 2 dB lower through bar 91's second half.
- Violins I, Violins II, Violoncellos and their three copies (`TRACK_DOUBLES` loop at line 1944): `(298.3, 33), (301.0, 17), (303.5, 12), (303.75, 10), (303.94, 8), (304.0, 8)` (3 units lower, about -1.7 dB). Violas and Violas div keep the present lane (they are 0.6 dB under c54).
- Clarinet 2 (new `CC_SHAPES["Clarinet 2"]`): `(11, [(299.9, 0), (301.0, -8), (303.5, -8), (303.56, 0)])`. Its lane reads 22 from 300.94; the Clarinet KS Master takes its layer from CC1, so this is level only (about -2.8 dB).

Expected (estimate): bar 91 per half beat -43.9, -43.6, -45.8, -48.7, -48.8, -48.3, the chord -51.5, -50.6, -50.2, -50.3, -53.7, -56.9; chord 301-303 at -50.6 dB (c54 -51.2), 2-3 dB under bar 91's second half. The delivered 10th percentile does not move (these bars are already under it); span stays 18.4. Check after the render with the half-beat table.

### 2. Double basses' A flat 1 pedal pulses every 1.3 s in bars 82-85 and 90-92 (measured; needs a range pass of the basses alone)

Where: Double basses, notes at 271.0, 273.23, 278.35, 297.2, 299.8 (pitch 32, Sus MAX, CC11 20-39). In bars 83-85 the basses are 4-5 dB under the master with only harp harmonics and timpani over them.

Evidence. Stem level, 0.1 s frames, written envelope removed, detrended: peak to peak 9.9 / 10.7 / 12.2 / 9.0 / 11.0 dB on these five notes, autocorrelation 0.84-0.87 at 1.3 s. On the delivered stems (0.3 s smoothing) 273.23 swings 11.8 dB (c54 3.4), 278.35 11.5 (2.6), 299.8 11.1 (7.7); the master over the same notes 5.9 / 6.7 / 5.5 dB (c54 4.0 / 3.9 / 2.4). Example, master per 0.25 s around qn 275.5-276.5: -40.2, -42.6, -43.9, -45.4, -48.8, -49.5 (c54 -43.0 to -43.6 with no fall). The swing is in the sample at every dynamic (A flat 1 at CC11 100, qn 200: 9.1 dB) and on other low pitches (median 6.5 dB over 30 held bass notes, the same in c54); the second harmonic (104 Hz, the strongest partial, 18 dB over the fundamental) has two components 1.6 Hz apart and nulls by 30 dB. c54 flattened three of these notes with a fitted envelope (it moved between -8 and +3 dB inside each note). This is the effect Dan described in item 8, now on the basses.

Fix. No row, region gain or velocity changes a wobble that is inside the sample, and the basses have no idle instance for a double. The remaining instrument-side control is CC11 riding against the swing, which is what the mod wheel does in the reference MIDIs (7-13 points per second on sustained lines). `basses_pulse_cc11.json` in my scratch folder holds an additive CC11 lane for each of the five notes and 276.05, fitted from the c56 stem (minus the detrended level, 0.57 dB per unit, clamped to 8 units either way, from 0.35 s after the note-on to 0.25 s before the end): 19-33 points per note, to be entered as `CC_SHAPES["Double basses"]` items `(11, pts)`. Expected: the fit removes the swing down to 1.1-3.1 dB if the slope holds exactly; the kit's experience with the same shape in the fader was 11.7 -> 5.3 dB, so expect 5-7 dB on the stem and under 4 dB on the master. Range pass: Double basses only, qn 270-286 and 296-304, measure with the 0.1 s frame method above. Take it only if the three worst notes come under 7 dB; otherwise drop the lanes and report the pulse as left audible. Finding 1's lower basses level in the final chord reduces its share there by 4 dB either way.

Not a "must do": it needs the only range pass I ask for, and the result is uncertain.

### 3. MUST DO. Bar 47 fp: the attack peaks 180-210 ms after the beat (measured; decidable offline from the measured rise times)

Where: qn 148, Violins II, Violas, Double basses (Sus MAX, CC11 spike 88 from the note-on to 148.12, at 46 by 148.30).

Evidence. Stem peak against the beat: Violins II +180 ms (c54 +60), Violas +190 (c54 -20), Double basses +210 (c54 -40). Each stem comes within 1 dB of its peak 290 / 220 / 340 ms after its note-on; the note-ons are 126 / 63 / 168 ms before the beat. Master: peak -25.6 dB at +210 ms (c54 -26.1 at +110 ms); the 100 ms on the beat reads -30.5 dB (c54 -27.6). The CC lane starts to fall at 148.12, so the samples reach their peak just as the lane leaves it. c48-c50 had put this attack on the beat with fader shapes on the three tracks; those are per-note moves and stay off.

Fix: start the three notes earlier, by the rise time. `build/entry_leads.json` (seconds, added to the family lead, total capped at 0.30 s): Violins II `"148": 0.06 -> 0.20`, Violas `"148": 0.13`, Double basses `"148": 0.13` (new entries; if the cap clips the basses at 0.30 s that is the wanted value). The CC11 spike is keyed to the moved note-on and moves with it; keep its fall at 148.12-148.30. The notes before end 0.04 qn before the present note-ons (147.84, 147.90, 147.80): let them end 0.04 qn before the new ones. Expected: stems within 1 dB of their peak 20-40 ms after the beat, master peak inside +60 ms, the 100 ms on the beat about -27.5 dB (inferred from the rise times). Check with the 10 ms table of `sim.py`'s source data after the render. If the early swell is heard before the beat, the fallback is the `Sus Marc LITE` row for these three notes (fast attack, then its own sag; a row change needs a full rebuild of the three tracks, so not in this session).

### 4. MUST DO. Horn 1's theme, bars 11-12: the crescendo arrives flat (measured; decidable offline from the CC11 slope)

Where: Horn 1, qn 30-35 (crescendo printed from 32 to mp at 34, then decrescendo).

Evidence. Bodies: 30 -39.5, 31.5 -38.5, 32 -34.9, 34 (B flat 4, the printed top) -35.0, 35 -37.6, 36 -39.7 dB. The hairpin 32-34 reads -1.7 dB on the stem (c54 +4.5); the arrival is 0.1 dB under the note before it. CC11 is 55 on 32 and 57 on 34; pitch 65 (F4, qn 32) already has -2.5 dB region gain. This is the first theme of the movement, with nothing but clarinets, bassoons and harp around it (margin +8.4 dB).

Fix: `CC_SHAPES["Horn 1"]` (new): `(11, [(33.9, 0), (34.0, 8), (34.9, 8), (35.05, 0)])` and `(11, [(31.95, 0), (32.1, -3), (33.9, -3), (33.95, 0)])`. Brass at CC11 40-60 give 0.34 dB per unit (my c56 table): +2.7 dB on 34, -1.0 dB on 32. Expected: 32 -35.9, 34 -32.3, 35 -37.6: the top stands 3.6 dB over the note before and the fall after it is 5.3 dB. Not a region gain: pitch 70 also sounds at 178, which is level.

The same control, smaller, for two string hairpins that still read under 1 dB (optional): Violins I and II 252 (F5, 2 qn, inside the crescendo 250-254: -37.7 / -40.1 dB after -37.3 / -38.4 at 250): `(11, [(251.9, 0), (252.3, 9), (253.6, 9), (254.0, 0)])` on both, the shape c56 used at 68 and 80; expected +4 dB.

### 5. Stereo: mono copies under the doubles, and two Horn 1 pitches out of phase (measured; a mix test, optional)

Evidence: slot C parts 3 and 4. The doubled pairs are 1.7-3.0 dB narrower than the section alone; the opening C5 is 2.5 dB brighter at 2-5 kHz; Horn 1's B flat 4 and A flat 4 in bar 12 have whole-note L/R correlation 0.14 and 0.01 against 0.72-0.97 around them.

Fixes, none of them urgent:
- Opening C5: a `loud_eq` row on "Violin I solo" over qn 0-9 only (`points [[0, 1], [9, 1], [9.5, 0], [291, 0], [304, 0]]`, band high shelf 2 kHz -4 dB) brings the pair's 2-5 kHz share from -11.6 to about -13.5 dB (estimate; c55 -14.1). Offline: an EQ on one stem.
- Narrowing: leave it. The alternative (the section patch with its Main mic on the DIV instance) was tested in c53 on Violas div and needed a per-note level fit; it also costs memory.
- Horn 1: one range pass of bars 11-12 with Close 0.48 -> 0.80 and Main 1.0 -> 0.70 on Horn 1 (`build/mix.json` tracks, "mics"), gain re-matched; pass if the whole-note correlation of 34 and 35 comes over 0.4 with the 2-5 kHz share within 1 dB. It changes the horn's distance for the whole movement, so I would not take it in the last cycle without that pass. Otherwise report it as left audible: two notes of the horn theme widen on headphones.

### 6. Bar 62, first half: the ff sags 2.7 dB for two beats (measured; partly decidable offline)

Where: qn 208-210, "ff molto sostenuto". Master per quarter 204-211: -13.4, -13.8, -13.9, -14.0, -16.3, -16.7, -13.8, -15.1 (c54: -13.8, -13.5, -13.7, -13.3, -14.5, -14.9, -14.2, -14.8).

Evidence. Every CC11 is at 122, so there is no headroom. Bodies at 208 against the same track at 204 / 210: Violins I F6 on Leg Slur MAX -28.2 against -23.2 / -23.4; Double basses G flat 1 (pitch 30) -29.2 against -24.4 / -20.6; Horn 1 F sharp 4 -29.3 against -25.7 / -24.2; celli -26.7 against -21.1 / -25.2; Bassoon 2 -29.9. Violins I's F6 gains 1.2 dB between CC11 88 (197.5: -29.4) and 122: its top layer on Leg Slur MAX is weak. The basses' pitch 30 is weak at f as well (196: -36.2, 8.3 dB under 198).

Fix (two changes, both in the instrument):
- Violins I: `ART_SPANS["Violins I"]` add `{"from": 207.9, "to": 208.1, "art": "Sus MAX"}` (a tenuto is printed on the note, and 205.95 and 210 already play Sus MAX). At the same pitch Sus MAX read 1.9 dB over Leg Slur MAX (205.95 against 204); for F6 the gain is not known, expected +2 to +5 dB (inferred). MIDI only, the row is loaded.
- Double basses: `region_gain_db` `pitch_db` add `"30": 4`. Notes it touches: 196 and 208 on Sus MAX (wanted), 146 on Leg Slur MAX (pp, -45.4 dB between -55.1 and the fp; +4 puts it at -41.4, check it; if it stands out use +3), and three pizzicato notes on a row the table does not cover.
Expected (estimate, with Violins I +5): quarters 208 and 209 at -15.5 / -15.9, sag 1.9 dB. The rest (Horn 1, celli, Bassoon 2 at 2.5-4 dB under c54 on this one chord) has no instrument-side fix with CC11 at 122: Horn 1's pitch 66 is already +3 and stands 2.4-4.5 dB over its neighbours at mf (190, 196). Left audible: about 1 dB of sag more than c54. The delivered maximum rises about 0.3 dB (span about 18.7, limit 19).

## Left audible, no instrument-side fix proposed

- Trombone 1's tenuto at 216: 2.6 dB under c54 and 2.9-3.2 dB under the notes around it. Slot A owns the accents; from the dynamics side, CC11 92 -> 104 and CC1 back to 108 over 215.94-216.94 would return about 2.5 dB (inferred from the c56 range figures), at the cost of 218's contrast.
- Bar 66: the down-bow at 223 is a 2.8 dB step and the strings then hold level for 1.5 beats (basses +3.4 dB at 224) before falling. A CC11 dip of 5 units on the basses over 223.5-225 would restore a steady fall (inferred, 3 dB).
- Bar 84 timpani +2.2 dB over c54 (strokes -43.7 / -40.3 / -43.1 dB); velocity 72 -> 68 on the middle stroke would level the three.
- Bar 82 is 1.9 dB softer than c54; it leads into the ppp coda and I would keep it.

## Do not touch

The removal itself and `env_edge_slew`. The doubles on the three DIV instances with their CC7 values (the bow-change dips they closed are worth the 0.8 dB of width). The bar 63 region volumes with their CC7 falls (downbeat level with bar 62, monotonic fall). The Oboe 1 head lifts, the A flat 1 region gain, the Flute 1 LegRep row gain (bars 30, 35, 44, 48, 71, 73 are back within 1.2 dB of c54). Bars 53-61 (the rise per bar). The climax 5.0 dB over the cadence, the delivery chain (LRA 15.3, span 18.4, limiter 1.9). The hall and the returns. The printed re-articulations at 223 and 289.
