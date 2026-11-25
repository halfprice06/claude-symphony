# Cycle 21, critic C: blend and space (render of cycle 20)

Material: `cycles/c20/render/` (31 dry stems, 4 returns, `00_Master.wav`), `cycles/c20/mvt3-mockup-c20.mp3`, `cycles/c19/render/` (for the variance check), `build/parts.json`, `build/mix.json`, `build/score_config.py`, `build/mockup-events.tsv`, `cycles/c20/CHANGES.md`, the Dvořák 9/i reference (`symphony/render/assets/refs/`, lossy MP3, used only for the loud-tutti spectrum above 100 Hz and for loudness shape). Scripts were in the scratch folder (deleted). K-weighting and momentary loudness (400 ms) follow BS.1770. "Measured" means a number from these files; "inferred" means reasoning that no render has tested. Nobody in the loop can hear, so every statement about audibility is inferred.

Delivery simulations: an unmodified copy of `tools/deliver_master.py` run on the c20 master, with the `build/parts.json` ride trims. On the unchanged master it reproduces c20 exactly (-14.8 LUFS, limiter 7.8 dB, the same climax order).

## Manual notes

MANUAL-READING.md has no row for cycle 21 (the third round ended at c20), so I read no fixed range. These are the pages behind this lens's open problems, plus the MANUAL-GAPS items that apply.

| Manual (May 2021 HO, PDF page) / gap | What it says | Where it applies here | Does the render follow it |
|---|---|---|---|
| p.121, 36in Ludwig Bass Drum | D1 (key 38) is the felt long hit. Velocity sets the dynamic layer (up to 12 levels), and CC11 plus velocity set loudness. "Deep, rumbling quality." | Bass drum at qn 888 (ff, bar 223) and 1108 (bar 278). Velocity is 114 and 112, and `gain_db` is -7.4. | Only in part. The stroke sits 10-12 dB under the basses in 30-90 Hz, so the rumble the patch is chosen for never reaches the mix (finding 1). |
| p.141, 4.2.6 Channel Routing | Mono From Left sends the left channel to both outputs and discards the right. | Horns 1 and 3 have used it since c19. Horns 2 and 4 are stereo. | Not consistently. The horn section has two kinds of image (finding 5). |
| p.138-139, mic positions; MANUAL-GAPS #4 (Mid mics on the winds) | Close mics sit in front of each section; Main mics pick up more room. | Oboes are at Close 0.939 / Main 0.088 and the cor anglais at 0.912 / 0.24, both template values. Stem correlation is 0.99 (oboes) and 0.93 (cor anglais), against 0.83-0.89 for flutes and clarinets. | The template default is kept. The wind return makes up for it: winds are 7-10 dB wet against 13-14 dB for strings and brass, the same in every section. No change asked; #4 is still untested. |
| MANUAL-GAPS c18, region volumes (Opus regionMap) | Each row group can take its own region gains. | The basses' "Sus MAX" / "Leg" rows have pitch gains, but the "Tremolo" row has none. Its only notes are the two fff C2s at 888 and 1108. | No (finding 1). |
| MANUAL-GAPS #6, CC16 round-robin reset (p.145) | Round-robin resets make takes repeatable. | Violins I / II / Violas in bars 1-10 (coordinator item). | Not on those tracks in c20. Different samples played there (see "Coordinator items"). |

## Findings, ranked

### 1. At the C-major arrival (bar 223, qn 888) the bottom octave gets weaker, and the ff bass drum is not heard in the low band (also at bar 278, qn 1108)

Measured. Score: at 884 the basses play D2 f cresc. (Sus MAX). At 888 they play a C2 tremolo fff, with tuba C2, contrabassoon C1, crash cymbals fff and bass drum ff. Levels are taken over 884.5-887.8 against 888.05-889.5:

| stem | 30-90 Hz before -> after (dB) | full band before -> after (dB) |
|---|---|---|
| master | -27.5 -> -29.9 | -19.3 -> -12.8 |
| Double basses | -27.2 -> -31.5 | -26.9 -> -28.1 |
| Tuba | -51.3 -> -43.1 | -33.5 -> -27.0 |
| Bass drum | silent -> -41.5 | silent -> -35.8 |
| Contrabassoon | -55.0 -> -56.2 | -37.3 -> -31.1 |

- The master gets 6.5 dB louder at the fff, but its bottom octave falls 2.4 dB. The basses carry 76-89 % of the master's 25-100 Hz band at 223 and 278, and they drop 1.2 dB overall and 4.3 dB in 30-90 Hz.
- The cause is in the data. The note changes from "Sus MAX" D2 to "Tremolo" C2. D2 is one of the hot fundamentals of the Basses KS Master (kit LEARNINGS §14: D2 +8.6 dB). The "Tremolo" row has no `region_gain_db` entry, and CC11 rises from 105 to 116-118, which cannot make up the difference.
- The bass drum supplies 1 % of the master's 25-100 Hz at 223 and under 1 % at 278-279. Its stroke is 11.6 dB under the master's 30-90 Hz band at 888 and 9.2 dB under at 1108.
- An orchestra's ff bass drum under a fff tutti is felt as a low thump. Here the arrival's low end thins out at the moment it should grow (inferred).

Fix (instrument side and static gain only, no envelope moves):
- `build/mix.json` "Double basses" `region_gain_db`: add `{"rows": ["Tremolo"], "pitch_db": {"36": 4.0}}`. This row plays only these two notes (qn 888 and 1108), so nothing else moves. Target: the basses' 30-90 Hz band at 888 at least 1 dB over the f bar before. Now it is 4.3 dB under; the expected result is about -0.3 dB, so measure it and raise to +5 if needed.
- "Bass drum" `gain_db` -7.4 -> -1.4. It plays only these two strokes. Simulated on the c20 stems:
  - master 30-90 Hz over the first 0.4 s of each stroke: -30.1 -> -27.7 dB at 888 and -30.0 -> -27.6 at 1108;
  - window sample peak: +0.17 dB at 223, +0.34 at the final chord;
  - with +9 dB the band gains 4.1 dB and the peaks +0.32 / +0.77 dB.
- Alternative per manual p.121: velocity 127 on both strokes (`PERC_VEL_ADD` or the percussion map) with `gain_db` -4.4. This uses the top dynamic layer, but its level gain is not measured, so check it on the stem. Target: bass-drum stroke 30-90 Hz within 3 dB of the basses' band at the stroke.

### 2. The loud tutti is thin at 100-250 Hz and bright above 6 kHz; mid-level passages match the reference

Measured on the loudest 10 % of 0.68 s frames (bars 1, 5, 90-93, 110-112, 146-150, 199, 212-213, 222-223, 255-263, 271-278) and on the 40th-70th percentile frames. Band shares are dB of total power:

| frames | 100-250 | 250-500 | 500-2k | 2-6k | 6-16k |
|---|---|---|---|---|---|
| master, loud 10 % | -11.7 | -7.9 | -2.1 | -9.4 | -23.4 |
| Dvořák 9/i, loud 10 % | -6.0 | -6.4 | -3.6 | -11.2 | -28.5 |
| mp3 c20, loud 10 % | -10.6 | -6.9 | -2.5 | -9.8 | -26.2 |
| master, mid frames | -8.4 | -6.0 | -3.4 | -10.3 | -29.2 |
| Dvořák 9/i, mid frames | -7.9 | -6.0 | -3.3 | -10.0 | -31.0 |

- At mid levels the mix is within 0.5 dB of the reference from 100 Hz to 6 kHz.
- In the loud frames it is 5.7 dB short at 100-250 Hz and 5.1 dB over at 6-16 kHz. The mp3's master EQ narrows these to 4.6 and 2.3 dB. This is level-dependent: the fff/ff layers and the trims added in c20 sit in the brass top, while the lower body does not scale with them.
- Who makes the bands in those frames:
  - 6-16 kHz: Trumpets 1-3 36 % (Trumpet 1 alone 21 %), crash 18 %, Violins I / II 16 %, Trombones 1-2 and Bass trombone 20 %.
  - 100-250 Hz: celli 32 %, basses 17 %, tuba 14 %, timpani 13 %, trombones 12 %.
- I do not tune the low end below 100 Hz to this MP3 (kit LEARNINGS §14). The 100-250 Hz band survives MP3 coding, and the slow-movement Brahms references in `metrics.md` also sit at -6.6 to -8.8 dB there over the whole file.

Fix: the `loud_eq` tool exists, one ReaEQ per spec with automated Wet, 0 elsewhere (`tools/build_reaper.py` `mute_lua`).
- Wet points: 0 -> 1 over the last 2 qn before each ff/fff tutti span, held, and back to 0 over 1 qn after it. Spans: 584-600, 792-818, 840-862, 884-893, 1016-1057, 1100-1116 (plus 0-24 and 360-376 if the actor wants them).
- Bands:
  - Violoncellos: bell 160 Hz +3 dB, 1.5 oct.
  - Trombone 1, Trombone 2, Bass trombone: bell 180 Hz +2 dB, 1 oct.
  - Tuba: bell 160 Hz +2 dB, 1 oct.
  - Violas: bell 200 Hz +2 dB, 1 oct.
  - Trumpets 1-3: high shelf 5 kHz -4 dB.

Simulated on the c20 stems over the loud frames:
- 100-250 Hz -11.7 -> -10.4 dB, 6-16 kHz -23.4 -> -24.3, K-weighted loudness +0.02 dB (the limiter does not change).
- A stronger set (celli +4, low brass +3, violas +3, horns 200 Hz +2, basses 130 Hz +3, trumpets shelf at 4 kHz -5, crash 6 kHz -3) reaches -9.6 / -25.0 dB, still 3.6 dB short of the reference.

The rest of the gap is probably voicing (inferred): at the arrivals the score leaves 100-250 Hz to the basses' second harmonic, the celli and the timpani. Finding 1 adds some of it back. Start with the moderate set. Check that the mid-frame shares stay within 0.5 dB of the c20 values.

### 3. Climax peaks and -14 LUFS: no instrument makes the crest; the master's top is too far above its body, and the delivery top ride undoes two thirds of any mix-side move (answer to the coordinator's first two items)

Measured.

No single stem makes the peaks.
- For each climax window I removed each stem from the sum and measured the peak drop and the momentary-loudness drop:
  - final chord (qn 1108-1113): largest Violins II, 0.83 dB peak for 0.84 LU;
  - bar 223: largest Flute 1, 0.23 dB;
  - bar 263: Horn 3 0.82 / 0.62 LU, Trumpet 1 0.76 / 0.77.
- Every stem that lowers the peak lowers the loudness about as much, so no instrument has an excess crest to cut.
- The crash and the low end are not involved. Below 150 Hz the master's peak is 13-14 dB under the full-band peak at 223, 263 and 278, and cutting the low instruments' <150 Hz part by 3 dB changes the peaks by 0.01-0.03 dB.
- Crests are normal. Sample peak minus momentary maximum is 7.7-8.2 dB at the climaxes, against 7.6-7.8 dB in the Dvořák recording's loudest moments.

The excess is in loudness shape.
- The master's momentary maximum is 11.9 LU over its integrated loudness. In the reference recording it is 5.8 LU.
- Per bar on the master (RMS), the ff body sits 6-8 dB under the arrivals: bar 110 -19.9, bar 1 -20.1, bar 199 -21.3 against 223 -12.4 and 278 -13.1.
- The delivery's top ride (3:1 from 10 dB under the 95th percentile) folds this into the 1.6 LU that separates them on the mp3, and the rest is left to the limiter.

Simulated mix-side trims at the arrivals (copy of `deliver_master.py`, c20 master with gain windows):

| variant | limiter max | I | final / 223 / 263 / loudest ff bar (mp3 momentary max) |
|---|---|---|---|
| c20 | 7.8 dB | -14.8 | -7.0 / -7.1 / -8.2 / -9.1 |
| 888-892, 1048-1056 and 1108-end all -2 dB | 6.3 | -14.6 | -7.2 / -7.3 / -8.9 / -8.9 (263 ties the ff bars) |
| A: 888-892 -3, 1108-end -2, 1048 unchanged | 6.2 | -14.7 | -7.1 / -7.5 / -8.2 / -8.9 |
| B: 884-888 -1.5, 888-892 -3, 1048-1056 +1, 1108-end -1.5 | 6.7 | -14.7 | -7.1 / -7.4 / -7.9 / -8.9 |

Recommendation:
- Use variant A in the mix: `dyn_trim_db` fff -3 dB at 888-892 and -2 dB at 1108-end on the 17 fff tracks. Keep c20's CC caps, CC11/CC1 steps and holds, which are the timbre of the arrival.
- Measured result on the simulation: limiter 7.8 -> 6.2 dB, final chord over bar 223 by 0.4 dB (c20: 0.1), 223 over 263 by 0.7, 263 over the loudest ff bar by 0.7.
- Do not lower bar 263. Any cut there puts it level with the ff bars 93 / 110.
- About 0.6 dB of integrated loudness is still missing after that. It is the limiter's own loss, so the last step belongs to the delivery: a slower pre-limiter stage, or a top ride closer than 10 dB under p95. That is not a mix job.
- Instrument-side crest exceptions:
  - bar 91: Bass trombone, window crest 10.8 dB; removing it costs 1.27 dB of peak for 0.29 LU, limiter 5.0 dB there. The fix is a further CC11 -10 units on the notes at 360 / 364 (-15 in c20 took 1.4 dB).
  - bar 277: Trombone 1, 0.70 dB of peak for 0.44 LU (limiter 4.0).
- Finding 1's bass-drum raise costs +0.17 / +0.34 dB of peak at 223 / final, which variant A more than covers.

Master LRA 22.8: narrow it at the top only, by the variant A trims. The lift ratio and the soft trims already hold p10 at -23.1.

### 4. Muted Trumpet 1 and cor anglais in unison (bars 171-174 and 179-183, qn 680-696 and 712-731): the doubled line changes colour inside every long note

Measured: A-weighted level per note, early (first 0.15 s) against body (0.25 s to the note end), on the 24 unison notes.
- The cor anglais body rises a median +2.5 dB over its start: 692 +4.5, 720 +1.7, 728 +1.5, and +6.7 to +8.3 dB on the 1-qn notes 683, 686, 715 and 718. The one exception is 688 (-2.3). The trumpet stays level (median +0.4).
- Trumpet minus cor anglais in the body ranges from -8.6 to +2.5 dB note by note. On the long notes it is 692 -8.1, 720 -2.3, 728 -2.4. So the line sounds as a trumpet at each attack and as a cor anglais half a beat later.
- The joins differ too:
  - the trumpet's "Mute Sus" row re-attacks every note, with gaps of 45-50 ms on 7 of 22 joins and overlaps of 30-60 ms on the rest;
  - the cor anglais is legato on "Leg Slur MAX", with a uniform 35 ms overlap.
- Space is already matched, so no mic or send change is needed:
  - stereo position R-L +2.6 / +4.2 dB;
  - correlation 0.80 / 0.93;
  - returns in 171-186 brass -11.6 dB, winds -7.0 dB.
- The spectra are what a straight mute gives (1.2-2.4 kHz share -3.6 against -12.5 dB) and are not a fault.

Fix: the swell is the cor anglais's Leg Slur MAX bloom, which A measured in c20 and ruling 8 deferred. For the unison spans only:
- put the cor anglais on "Sus MAX" over 680-696 and 712-731 (`ART_SPANS`), with no row change inside a span, so the note after a held note is never the unled entry into a legato row that c19 hit;
- copy Trumpet 1's join table there (the 45-50 ms gaps and 30-60 ms overlaps, same leads), so both instruments articulate together.

The effect is inferred: the bloom is absent on the sustain row in c19's first build, per CHANGES c20. Target: trumpet minus cor anglais body within ±3 dB on every unison note, and the cor anglais body within +1.5 dB of its start. If the row change cannot be made this cycle, the fallback is a CC11 dip on the cor anglais's long notes sized from its own curve. c19's -10 was too small; the bloom is 4.5 dB against a slope of about 0.5 dB per unit, so about -14 units starting 0.15 s after the note-on.

### 5. The horn section has two images: Horns 1 / 3 are point sources, Horns 2 / 4 are wide

Measured over the chorale 888-932:

| | Horn 1 | Horn 2 | Horn 3 | Horn 4 |
|---|---|---|---|---|
| L/R correlation | 0.98 | 0.47 | 0.98 | 0.80 |
| mono loss (dB) | -0.2 | -1.4 | -0.2 | -0.5 |
| R-L (dB) | -3.9 | -3.6 | -3.4 | -2.1 |

- Over the whole file, side/mid is -13.3 / -5.0 / -13.7 / -6.6 dB.
- Horns 1 / 3 have used Channel Routing "Mono From Left" (p.141) since c19 ruling 4. Horns 2 / 4 kept the recorded stereo.
- The four horns hold chords together through the chorale and the climaxes. Two of them are narrow points and two are spread across about half the stage. Horn 2 also loses 1.4 dB in mono, the same fault c19 fixed on Horns 1 / 3.

Fix: `Mono From Left` (the `channelMap` option that `build_reaper.py` writes, line 440) on Horns 2 and 4. Full rebuild of those two tracks; no memory cost.
- Re-check Horn 2 / Horn 4 levels afterwards. Horns 1 / 3 rose 1-2.5 dB when they were switched (mix.json `_c20`), so expect about -1.5 dB of `gain_db` on each.
- Targets:
  - all four horns with correlation 0.95 or more and mono loss under 0.3 dB;
  - R-L within 1.5 dB of each other;
  - master side/mid still about -5 dB (now -5.3, inside the reference range -4.7 to -5.4).

## Coordinator items (verified on the c20 files)

- **Delivery, limiter, LRA**: finding 3.
- **Climax order on the mp3**: finding 3. Variant A gives final -7.1 > 223 -7.5 > 263 -8.2 > ff -8.9. Bars 222 (-7.9) and 277 (-7.7) still sit above 263. Bar 222 is the f crescendo; lowering it would weaken the step into 223 that c20 built, so leave it.
- **Clarinets 151-170 (why CC1 +6 did nothing)**: measured in parts.json.
  - CC1 +6 went in at both 40-104 and 600-680 (median 63 -> 69 and 61.5 -> 68).
  - The +3 dB in bars 11-26 came from deleting the -2.5 dB role rows: Clarinet 1 `vol_db` median -0.94 -> +2.0. In 600-680 `vol_db` stayed at 0.74 and the level did not move.
  - So CC1 +6 near 62-68 on the Clarinet KS Master is worth about 0 dB (measured).
  - Fix: a held phrase level of +3 dB on Clarinets 1 / 2 over 600-680 (role row; slow balance, allowed), or CC11 `cc_scale` +3 dB, k 40, the same as the other c20 lifts.
- **Counter-line 212-215 (qn 844-860)**: still 11-12 dB under, target 5. Split the remaining 6-7 dB: a held -3 dB on Trumpets 1-3 over 844-857, and +3.5 dB more on the celli (CC11 `cc_scale`, k 47), Bassoon 1 (k 33) and Horn 3 (CC11, k 40). Not re-measured by me beyond the c20 table.
- **F1 head 83-86**: +1.5 dB more on Clarinet 1 / Oboe 1 (same `cc_scale` rows as c20, 3 -> 4.5).
- **Celli 67-79**: +1.4 dB over Violins I against a target of -2.5. Change the c20 CC11 lift from +3 to -0.9 dB (k 47).
- **Basses' eighths**: the measured drop is 2.5 / 2.8 dB. Set "Stac On Bow" `all_db` -1.5 -> +1.2 and keep the release-extension group at -60 and the 90 ms release.
- **Trumpet release trails**: A's lens. No blend-side fix: raising the trumpets' sends would add hall to every trumpet note, and the master stop at 814 is already 14.4 dB.
- **Cor anglais qn 600, -1.5 dB over 0.5 s**: that is a fader move after the hall, so it also cuts the hall tail of the bar-150 release (S3). Do it in CC11 (`cc_scale`, k 33, -1.5 dB over 599.5-600.2), or drop the cor anglais from the bar-150 `vol_set` hold.
- **Violins I / II / Violas 1-2 dB louder in bars 1-10 with unchanged data**: not level variance; different samples played.
  - c19 against c20 waveform correlation in bars 1-10 is 0.016 / 0.039 / 0.044.
  - The celli and basses, which were fully rebuilt in c20, are sample-identical to c19 (0.997 / 1.000).
  - The upper-string differences alternate by bar: +2 to +4.5 dB in bars 1-2 and 5-6, -1 to -2.2 dB in bars 3-4 and 9-10. That fits the bow-direction round robin starting on the other bow (inferred). These three tracks were MIDI-only builds; a fresh full build was deterministic on the other two.
  - Fix: rebuild Violins I / II / Violas in full in c21. Check bars 1-10 against c20 and c19 and keep the take that puts the bar 1-2 chords level with bars 5-6.
- **Hidden lines elsewhere** (unweighted per-bar scan of moving, undoubled lines more than 10 dB under the loudest stem; rough):
  - Clarinet 1 bars 188-190 (-12.6) and 257-258 (-13.5);
  - Violas 21-22 (-13.4), 176-177 (-13.0), 184-185 (-15.1);
  - Violins II 207-208 (-16.0).
  - Candidates for B to confirm with A-weighting.
- **Loop pulsing (item 7)**: chorale 223-234, 100-300 Hz level autocorrelation at 3.95 s is -0.10 to +0.11 on the master and every string, horn and trombone stem. Bars 273-277 master +0.30: that is the basses' repeated eighths (+0.63, a rhythm, not a held note). No pulsing on held notes.
- **Findings from the other movements**: the list in my task file was empty, so none were checked.

## Do not touch

- The four returns with their sends: return under its family's dry sum is strings -13.0 to -14.3, brass -11.4 to -15.3, winds -5.6 to -12.6, perc -4.8 to -8.4 dB, and every section stays within these ranges.
- The seats: master correlation 0.54, side/mid -5.3 dB.
- The crash level at the arrivals: it gives half the master's 4-12 kHz there, -1.9 to -3.6 dB re the master band.
- c20's fff CC caps, steps and holds at 888 and 1048 (finding 3 changes only the dynamic trims).
- Horns 1 / 3 on Mono From Left.
- The chorale overlaps.
- The celli / basses region tables and the CC16 resets that make them repeatable.
