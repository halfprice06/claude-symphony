# Cycle 21, critic B: balance and levels (on the c20 render)

All numbers come from the c20 stems, the c20 master and the delivered mp3, and from about 20 runs of the unchanged `tools/deliver_master.py` on copies of the master and of `parts.json` / `mix.json` (scratch only). The tool reproduces the c20 delivery exactly: -14.8 LUFS, final 7.8 dB and bar 223 6.1 dB of limiting. Bar loudness is momentary loudness (400 ms windows centred on the frame, K-weighted), maximum per bar. "Measured" means read from the audio or the data. "Inferred" means a judgement drawn from those numbers.

The coordinator's list "Findings from the other movements" is cut off in my task file: it ends at "say whether it applies:" with no items. I could not check those items.

## Manual notes

MANUAL-READING.md has no row for cycle 21, so I did not read a page range. These are the pages behind this cycle's findings, plus open MANUAL-GAPS items.

| what the manual says (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| Velocity is used for short articulations, CC for sustained ones (p.53). Velocity sets the loudness and dynamics of short instruments (p.64). CC7 sets the level against other instruments, CC11 shapes the dynamics (p.64). | Brass short rows: Trumpets 1-3 "Stac DblTng RRx9" at 633-662, Horns 1/3/4 "Marc Shrt RRx4" | No. The trumpets' mf staccatos carry CC11 72 and velocity 88, so both lower the note. On these KS Masters CC11 acts as volume at 40 log10 (c18), so 72 against the ff resting value of 100 costs 5.7 dB on top of the mf velocity layer. Finding 3. |
| Short brass rows have no release trails, and the highest velocity adds overblown attacks (p.101) | Same notes | Velocity 88 is well under the overblown layer, so raising it to 96-100 is safe (inferred). |
| Each KS Master row has its own volume (p.137). | Basses "Stac On Bow RRx9" | Not usable: c19 found that the row volume knob does not act on the basses' short rows. Region volumes do (c17, c19). Finding 4. |
| MANUAL-GAPS 13: the Bass trombone's three lowest notes are transposed tenor samples (p.100). | Bars 113-115 | Not the source of the bar 91 limiter peak. That peak is one E flat 2 at -10.6 dBFS (c20 peakwho), and it now takes 3.8 dB in the variant below. Still open, low priority. |

## 1. Delivery at -14: the three fff moments hit the limiter's ceiling. Ride rows and a loudness loop meet every target. Cutting single tracks does not (measured)

**What is wrong.** Before the limiter, the master's loudest bars are bar 278 at -1.8, bar 223 at -3.3, bar 263 at -7.0 and the ff bars at about -7.7 to -9.6 LUFS momentary. The limiter brings everything above about -8 down to the same ceiling: bar 278 loses 5.2 dB of momentary loudness, bar 223 3.8, bars 222 and 277 3.1, bar 263 1.2. As a result, a final chord that is 1.5 dB over bar 223 before the limiter is only 0.1 dB over it on the mp3. On this material the mp3 gains about 0.25 dB for each 1 dB of input above the ceiling. The 0.8 LU shortfall comes from the same place. The pre-limiter file is at -14.0 by construction, and the limiter's losses are concentrated in bars 271-279 (mean 1.0 dB) and 223-234 (0.27 dB). Only 3.5 % of frames lose more than 0.3 dB.

**What makes the peaks (measured).** I cut each group by 3-4 dB at 886-900, 1046-1054 and 1104-1118 on the master and re-ran the delivery:

| cut | limiter change, final / bar 223 |
|---|---|
| low end -3 dB (Tuba, Bass trombone, Double basses, Contrabassoon, Timpani, Bass drum) | -0.3 / -0.4 |
| trombones and tuba -3 dB | -0.3 / -0.6 |
| Violins I / II -3 dB (final only) | -0.4 / 0 |
| crash -4 dB | -0.1 / 0 |
| trumpets -3 dB | 0 / -0.1 |

No track or sample makes the crest. Like c20's peakwho, the peaks are the tutti sum. Instrument-side crest cuts cannot bring the limiter to 6 dB, so I reject that approach on these numbers.

**Should the mix narrow?** In the master the fff moments stand 5.7-7.7 dB over the ff bars: bar 223 -8.0 and bar 278 -8.8 against bars 1, 91 and 110 at -15.6 to -15.8. The f chorale at bar 225 is 15 dB under bar 223. Narrowing the top in the track envelopes would act after the hall, exactly like a delivery ride, so it gives the same result (measured equivalence: both are gains on dry stems). Narrowing it in CC11 / CC1 would undo the fff timbre steps c20 gained (brass +4.7 to +8.4 dB with the top dynamic layer). So: keep the instrument-side fff steps and do the level narrowing in the delivery rows (inferred).

**Fix (measured, variant w11).** Three changes:

- `build/score_config.py` RIDE_TRIMS: replace the row that starts at 1087.0 (+2.5 / +2.0 / +1.0 dB) with `[(1087.0, 0), (1088.0, 0), (1104.0, 0), (1107.9, -2.5), (1108.0, -2.5), (1113.0, -2.5), (1113.5, 0)]`, and add:
  - bars 222-223: `[(883.5, 0), (884.0, -3), (887.9, -3), (888.0, -4.5), (891.5, -4.5), (892.0, 0)]`
  - bar 263: `[(1045.5, 0), (1046, -1.5), (1051.5, -1.5), (1052, 0)]` and `[(1043.5, 0), (1044, -2), (1046, -2), (1046.5, 0)]`
  - the ff stabs, -3 dB each, written as `[(a - 0.5, 0), (a, -3), (b, -3), (b + 0.5, 0)]`: 360-376 (bars 91-94), 436-452 (110-113), 1052-1056 (264), 660-664 (166) and 848-852 (213). Also -2 dB at 524-528 (132) and 596-600 (150), and -1.5 dB at 0-8 and 16-24 (these add to the existing -2.5 dB rows).
- `build/mix.json` deliver.ratio 2.0 -> 1.8.
- `tools/deliver_master.py`: make up the limiter's loss. I simulated this as `DELIVER_TARGET_I=-13.4`. The better form is a loop like the true-peak loop: measure I on the mp3 and, if it is short, raise the pre-limiter gain by the shortfall and limit again (two passes at most).

| | c20 delivered | w11 simulated | goal |
|---|---|---|---|
| I / LRA / TP / p10 | -14.8 / 12.0 / -1.1 / -23.1 | -13.9 / 11.5 / -1.3 / -22.3 | -14 ±0.5 / about 12 / -1.0 / -23 or higher |
| limiter: final / 223 / 263 / bar 91 (dB) | 7.8 / 6.1 / 2.8 / 5.0 | 6.0 / 3.5 / 3.1 / 3.8 | 6 or less |
| momentary max: final / 223 / 263 / loudest ff bar | -7.0 / -7.1 / -8.2 / -9.1 | -7.3 / -7.7 / -8.3 / -9.1 | that order |

The shape around bar 223 is kept: bars 221 / 222 / 223 / 224 / 225 read -10.5 / -9.4 / -7.7 / -12.1 / -16.0 (c20: -12.0 / -8.6 / -7.1 / -12.9 / -17.6).

**Limit of the method (measured).** Across ten ride variants, at -14 LUFS with at most 6 dB of limiting the margins between the final, bar 223, bar 263 and the ff bars stayed at 0.3-0.9 dB. They never reached 1 dB, because all three fff moments sit near the limiter's ceiling. Wider margins need a lower delivered level, or more than 6 dB of limiting on the final.

**Correction to c20's log.** "Bar 222 louder than 263" is an artefact of uncentred windows. With centred 400 ms windows bar 222 reads -8.6 and bar 263 -8.2 on the c20 mp3, and in w11 bar 222 reads -9.4.

## 2. Inner lines: two of the reported shortfalls are measured against the wrong reference. The clarinets in 151-170 are a real shortfall, and CC1 cannot fix them (measured)

- **Celli in bars 67-79 (qn 264-316).** Violins I and II play the tune in unison (all 50 onsets shared, both marked mf cantabile). Against that pair the celli read -1.8 dB and the violas -3.9, which meets the -2.5 target overall. By half: 264-296 celli -4.8, 296-316 celli -0.4. The reported "+1.4 dB" compared the celli with Violins I alone. Fix: keep the c20 lift. At most, take 1.5 dB off the celli's CC11 at 296-316 only. Measured here, the celli move 0.27-0.47 dB per CC11 unit, so that is about -4 units.
- **Counter-line in bars 212-215 (qn 844-860).** Celli, Bassoon 1 and Horns 3 / 4 summed sit 6.0 dB under Trumpets 1 + 2 summed. The target was 5, so this is met within 1 dB. The "11-12 dB" figure compared one stem with the trumpet pair. Fix: no further lift.
- **Clarinets in bars 151-170 (qn 600-680).** CC1 +6 was applied (lane mean 71.8 -> 77.6 on both clarinets) and moved the level by -1.4 to +0.9 dB per 8 qn window. The +3 dB that c20 got in 40-104 came from deleting the -2.5 dB role rows. CC1 +6 alone was worth about +0.5 dB there, the same as in 600-680, at CC1 values from 59 to 92. On the CL KS Master, CC1 changes the dynamic layer's timbre much more than its level. Fix:
  - `build/roles.json`: Clarinet 1 +3.5 dB and Clarinet 2 +3.0 dB over 600-680. They have no rows there now. The aim is about -6 dB under Violins I, from -9.5 / -8.8.
  - Or, on the instrument side: CC11 x 10^(3.5/40) = 1.22 (c18: CC11 is volume at 40 log10 on this KS Master). That is 88 -> 107 at 600-632 and 72-83 -> 88-101 after.
  - Take back the CC1 +6 at 600-680 so the layer stays where the dynamic puts it.
- **F1's head in bars 83-86 (qn 328-344).** Clarinet 1 sits at -3.2 dB under Violins I (target within 3: met). Oboe 1 sits at -5.0. Fix: Oboe 1 +2 dB, as a role row or CC11 x 10^(2/40) = 1.12, at 328-344.

## 3. A hidden line nobody has listed: the trumpets' mf staccato off-beats in bars 159-166 are 22 dB under the violins, because CC11 and velocity both lower them (measured)

**Where.** Trumpets 1-3, qn 633-662 (bars 159-166): quarter-note off-beats, staccato, mf, on "Stac DblTng RRx9". They come in under the recapitulation, with Horn 3's f off-beats.

**Evidence.**

| stem, 636-664 | level (dBFS RMS) |
|---|---|
| Violins I | -31.9 |
| Bassoon 1 | -36.5 |
| Horn 3 | -42.5 |
| Trombone 1 | -42.6 |
| Horn 4 | -45.2 |
| Trumpet 1 | -54.2 |
| Trumpet 2 | -54.9 |
| Trumpet 3 | -58.9 |

The trumpets' data there is CC11 72, CC1 68 and velocity 88. On the 1TP KS Master, CC11 72 against the ff resting value of 100 is 40 log10(0.72) = -5.7 dB on top of the mf velocity layer. The same double cut sits on Horn 3's "Marc Shrt" notes (CC11 median 72, 51 notes) and Horns 1 / 4 (88).

The manual puts the dynamics of short rows in velocity (p.53, p.64). The research default (FINDINGS section 7) parks the CC high on shorts and takes the dynamics from velocity: brass shorts at velocity 62-95 with CC1 75-127. Our brass shorts sit below that CC1 range, and their CC11 follows the dynamic.

**Fix.**

- New generic rule in `tools/instr_post.py` (name it `SHORT_CC_PARK`; Finale values in `build/score_config.py`). On brass short rows ("Stac", "StacSs", "Marc Shrt"), hold CC11 at the track's ff resting value (100) from 0.05 s before each short note to its note-off, and hold CC1 at 85 or more. The printed dynamic then comes from velocity alone.
- Trumpets 633-662: velocity 88 -> 96 as well. Target: each trumpet 3-5 dB under Horn 3, from 11.7 dB.
- Horn short rows: check their level after the park. Horn 3's off-beats in bars 13-24 and 153-164 read 10.4-13.3 dB under the loudest stem now, so a lift of up to about 5 dB is welcome there (inferred).
- Do not apply the park to string pizzicato. It also carries CC11 34 with velocity 41, but its per-key table was fitted at those values (c19-c20) and the trumpet solo in bars 51-66 sits a proper 5.3 dB over the pizzicato strings summed.

## 4. Basses' hammered eighths: the muted release extension cost 4.1 dB at the stroke peaks, and 7.4 dB in the accelerando (measured)

**Evidence.** Median per-stroke peak (10 ms RMS maximum in each eighth slot), c19 -> c20:

| qn (bars) | c19 | c20 | change |
|---|---|---|---|
| 792-816 (199-204) | -31.4 | -35.5 | -4.1 |
| 984-1056 | -30.9 | -35.1 | -4.1 |
| 1056-1088 | -33.9 | -38.1 | -4.2 |
| 816-840 (205-210, poco a poco accel.) | -35.0 | -42.4 | -7.4 |

The celli in the same spans did not change (within 0.7 dB). c20's "2.5-2.8 dB" was an RMS figure, which includes the energy that used to fill the gaps.

**Fix.**

- `build/mix.json` `region_gain_db`: +4.0 dB on every region of the "Stac On Bow RRx9" stroke groups. The row volume does not act on this row (c19). Keep the -60 dB on the release-extension group and the 90 ms release, which give the 13 dB separation.
- 816-840: the strokes are 60 % of an eighth that shrinks to about 0.165 s, so they last about 0.10 s. I infer the note-off arrives before the sample reaches its level. Lengthen those notes to 72 % of the slot, or add CC11 +6 units on top of the +4 dB, and measure the stroke peak against 792-816 (target within 1 dB).

## 5. Trombones in bars 199-204 are 2.3-3.3 dB under the trumpets; CC1 +6 bought 0.8 dB (measured)

**Evidence (dBFS RMS, 792-816).** Trombone 1 -37.0, Trombone 2 -37.5; Trumpet 1 -34.7, Trumpet 2 -34.2. Target: within 2 dB.

**Fix.** Trombones 1 / 2 `cc_scale` +1.5 dB on CC11 (factor 10^(1.5/40) = 1.09, k 40) at 792-816. CC1 changes their layer more than their level, as on the clarinets.

## 6. Strings in bars 1-10: not render variance in c20; c19 was the odd render (measured)

Per quarter note over qn 0-40, c18 and c20 agree within 0.1 dB on Violins I, Violins II and Violas (span levels -35.3 / -35.4, -34.0 / -34.0, -35.5 / -35.5). c19 alone differs, and in a pattern: the held ff chords at qn 1-7 and 17-23 are 2-4 dB lower, and the turn figures at qn 9-12 and 34-39 are about 2 dB higher. That looks like a two-valued start state on the first notes after the pre-roll (inferred: the other bow-direction take), not a cause in c20's data. No action. Compare against c18 / c20, not c19, for bars 1-10, and add this to LEARNINGS.

## Other coordinator items, briefly

- **Cor anglais at qn 600 (-1.5 dB over 0.5 s inside a note).** The bar-150 gain release crosses the note at 600.2. Under the standing rule, end the release by 599.9 and put the -1.5 dB into the cor anglais' CC11 from 600.0 (woodwind CC11 acts as volume). Not measured.
- **Trumpet release trails.** That is lens A's item. On level: the trails at -45 dB under the note are not a balance fault.
- **Timpani, bass drum and low brass at the arrival and the ending.** The master's 30-150 Hz share is -13.9 dB at bar 223 and -12.6 at bars 278-279, against -12.2 to -13.0 in the ff bars and -10.0 in the f chorale. The tuba and basses are 3 dB under the trumpets at 223, and the timpani are 12 dB under. The bass is not covering (measured).

**Do not touch:**

- the instrument-side fff steps at 888 and 1048 (brass CC11 / CC1)
- Horn 1 "Mono From Left" and its chorale level (within 1.2 dB of Horns 3 / 4)
- the clarinets' levels in bars 11-26 (-6.0 / -5.3)
- the celli pizzicato per-key table (2.3-5.5 dB spread)
- the CC16 round-robin resets
- the basses' muted release extension and 90 ms stroke release (13 dB separation)
- the true-peak loop in `deliver_master.py`
- the c20 lifts for the celli in bars 67-79 and the counter-line in bars 212-215 (both on target against the summed melody)
