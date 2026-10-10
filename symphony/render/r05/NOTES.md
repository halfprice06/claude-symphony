# r05: rolls follow the printed dynamics, Iowa woodwinds, segment-wise roll balance, hairpins kept

Actor 5. Built from r04 and critic 4's plan (critics/c04.md, section 9).
Test inputs: movement I is mvt1/v156 and movement II is mvt2/v30.
"Before" is r04/out-m1.mp3 and r04/out-m2.mp3, measured by critic 4 on the same inputs (critics/c04/).
All numbers come from fresh renders made with the brief's commands, measured with r05/meas/scripts/meas.sh. The tables are in r05/meas/m1 and r05/meas/m2.
Tags: [measured] means read from those tables or tools; [inferred] means reasoned, not measured.

## 1. What changed, by plan item

### Item 1. Rolls follow the dynamics and hairpins printed inside a tied roll: done

- **lib/score_events.py: a bug fix that affects every stem, not only the timpani.**
  - Events at the same score position are now ordered: hairpin stops, then dynamics, then hairpin starts.
  - Before, a plain string sort put "cresc-1" ahead of "dyn:p". The dynamic then cleared the hairpin, so every note printed `\p\<` lost its whole hairpin.
  - Hairpin rows in m1 went from 416 to 1049 [measured].
- **New notes.csv column `inner`.** It lists the dynamics and hairpins printed strictly inside a note (tied notes merged), plus the first dynamic within a quarter note after the note ends.
- **articulate.py: new `roll_curve()`, which replaces the old settle loop for sample-mode rolls.**
  - It moves 3.5 dB per printed step (`timp_roll_step_dB`).
  - A hairpin ramps to the next printed dynamic, or by one step if no dynamic follows.
  - Flat stretches settle by -4.5·(1-exp(-t/1.0 s)), then sink 1 dB per bar after 2 s, with a floor of -7.5 dB.
  - The settle restarts at each new printed dynamic, and a hairpin starts from the settled level.
  - Sources: critic 4's targets; https://freepercussionlessons.com/how-to-play-timpani-rolls-from-soft-to-loud-and-back-to-soft; https://forum.vsl.co.at/topic/53560/best-practices-to-get-dynamic-timpani-rolls-in-sychron-sound-nice.
- **lib/marks.py `roll_segments()` and lib/balance.py: the balance cuts once per printed roll segment, not once per bar.**
  - The cut is the maximum need over the segment.
  - Need is measured against the other stems' level while the roll sounds.
  - The margin is 3 dB, or 0.5 dB inside crescendo segments.
  - This removes critic 4's per-bar safety net that flattened exposed soft rolls.
- **Start stroke and drum.**
  - The roll start stroke is off (`timp_roll_start_stroke_vel` 0).
  - New sfz/timpani-roll-r05.sfz plays E-flat 3 from the E3 sample pitched down instead of D3 pitched up, with a pitch trim of +0.8 dB.

### Item 2. Even dB per printed step: partly done

- **Per-stem `printed_trim_dB` set from a one-note calibration per printed dynamic** (meas/scripts/engcal.py).
  - This covers every new Iowa stem, plus trumpet mp -2 and the contrabassoon at +1 dB per step centred on f.
- **Master curve `extra_dB_points`:** the top is lowered by 0.5 dB.
- **A "soft lift" curve (+1.5 dB at pp-p) was tested and rejected:**
  - m2 LRA improved, 22.0 -> 20.9;
  - but m1 LRA fell to 17.5, and m1 inversions outside hairpins rose 221 -> 274 [measured].
- **Slope trims on trumpets, oboes and horns were tested and reverted:** no gain in Spearman or in inversions.

### Item 3. Woodwinds from the University of Iowa MIS samples: done (clarinets, bass clarinet, oboes, flutes, bassoons)

- **Source.**
  - Recordings: https://theremin.music.uiowa.edu/MIS.html (pre-2011 chromatic runs, pp/mf/ff, mono, "free for any use without restrictions").
  - Files are logged in assets/README.md (assets/iowa/).
- **New r05/build_iowa.py turns the recordings into per-note samples and SFZ maps.**
  - Notes are segmented by envelope. Pitch is assigned in chromatic order from the file-name range, with an autocorrelation check.
  - The onset is the first 2 ms frame within 20 dB of the sustain, and the sample starts 8 ms before it.
  - Each layer is level-normalised; loops sit on zero crossings with loop_sustain.
  - Each instrument gets a centre map, L and R maps (pan ±35) and an a2 map (two players, ±4 cents, 12 ms apart).
  - SFZ opcode references: https://sfzformat.com/opcodes/lovel/, https://sfzformat.com/opcodes/xfin_lovel/, https://sfzformat.com/opcodes/loop_mode/.
- **Velocity layers switch hard (no crossfade).** Crossfading two takes of one pitch beat: the envelope rippled by 3.3 dB [measured].
- **Section staves split by voice.** Player 1 goes left, player 2 right, unisons use the a2 map, and the clarinet +5 dB shelf is removed.
- **Results [measured, m1].**
  - Accent boosts:
    - oboes 6.5 dB;
    - clarinets 4.6 dB;
    - flutes 5.1 dB;
    - bassoons 7.1 dB;
    - bass clarinet 7.7 dB.
  - Short notes:
    - flute staccato length ratio 2.07 -> 1.9;
    - flute detached ratio 1.53 -> 1.46;
    - oboe detached ratio 1.46 -> 1.35.
  - dB per printed step:
    - flutes 1.78 -> 2.56;
    - oboes 1.21 -> 1.72.
- **Brass (horns, trumpets, trombones) and cor anglais are still FluidR3.** Iowa's brass needs a separate build and calibration, and there was no time left in this cycle.

### Item 4. Relief for marked melodies at the same printed dynamic: partly done

- **`per_bar_need`.** Lifts and ducks follow the median need of the bar and its two neighbours, not the phrase maximum.
- **`tutti_lift_dB` 2.** A phrase that starts inside a tutti keeps a capped 2 dB lift.
- **Result [measured].**
  - m1 melodies against the sum of the other stems: 14 -> 16 of 20.
  - m1 melodies against the loudest other stem: 12 -> 11 of 20.
  - m2 is flat (see section 3).

### Item 5. Spectral finishing: done

- **Bus EQ retuned against the mean of the four Brahms references** (meas/scripts/eqtune4.py):
  - 720 Hz -2.0;
  - 3 kHz -0.7;
  - 7 kHz +2.5;
  - a new low shelf at 90 Hz, +2.0.
- **Result [measured, premasters].**
  - 2.5 and 3.2 kHz now sit +0.5/+0.5 dB (m1) and +0.2/+0.9 dB (m2) against the references; critic 4 measured +2.5 dB in r04.
  - 62 Hz is still about -5 dB.

### Item 6. Roll realism: partly done

- The start stroke is off, and E-flat 3 is resampled from E3.
- The stroke autocorrelation is still 0.27 in m1 41-43 and 0.25 in m2 67-70 [measured].

### Item 7. Bass trombone accents: partly done

- `accent_extra_vel` raised to 10.
- Accent boost: -1.9 -> -0.9 dB [measured]. The target is ≥ 3 dB, so this is not reached.

### Item 8. Tools: done

- **meas.sh** now runs rollcurve.py and melody_nt.py; melody_nt's balanced-bar count is the standard melody measure.
- **New scripts:**
  - inv_nohp.py and bardyn_nohp.py: inversions and Spearman without hairpin bars;
  - engcal.py: calibrates printed_trim per dynamic;
  - eqtune4.py;
  - unmatched.py.
- **Unmatched MIDI notes, 0 unexplained.**
  - m1 had 22. They were mostly the second note of unisons on one staff; articulate.py now matches these to the printed note with the same staff, onset and pitch class (`match_shared_notes`). The rest are on the percussion track (track 48).
  - m2 had 9, now 6. The 6 are grace notes in the violins, which have no printed duration.

### Generality

- mvt1/v185 and mvt2/v61 parse with no config gap, and their roll segments are found [measured].
- Nothing is keyed on bar numbers.

## 2. Before / after

### Movement I (v156)

| measure | r04 | r05 | |
|---|---|---|---|
| LRA LU | 19.2 | 19.2 | [measured] |
| short-term p10/p50/p95/p99 LU | | -15.1/-5.3/+4.1/+6.2 | [measured] |
| short-term max LU | +7.1 | +6.8 | [measured] |
| Spearman, bar loudness vs printed dynamic | 0.82 | 0.81 | [measured] |
| Spearman, without hairpin bars | 0.89 | 0.88 | [measured] |
| inversions, all / outside hairpins | 365 / 250 | 359 / 208 | [measured] |
| bars <= mf louder than the median f bar | 10 | 8 | [measured] |
| step dB pp>p, p>mp, mp>mf, mf>f, f>ff | | 2.6, 4.8, -0.4, 6.0, 4.2 | [measured] |
| melodies >= 0 dB vs loudest other / vs sum (of 20) | 12 / 14 | 11 / 16 | [measured] |
| cuts >= 6 dB | 25 | 29 | [measured] |
| cuts >= 3 dB on stems printed >= the melody | 18 | 34 | [measured] |
| max fader slope dB/s | 5.3 | 5.0 | [measured] |
| < 100 Hz share dB | -9.9 | -9.6 | [measured] |
| 2-6 kHz share dB | -9.9 | -12.3 | [measured] |
| timpani loudest stem in roll bars | 0 / 31 | 0 / 31 | [measured] |
| roll 41-43 (ff > pp) change dB | -4.4 | -22.5 | [measured] |
| roll 117-121 (cresc) end change dB | about -4 | +7.0 | [measured] |
| roll 167-169 (cresc) dB | about -4 | +3.9 | [measured] |
| roll 1-4 settle dB / audible share | -1.0 / 0.62 | -4.7 / 0.38 | [measured] |
| bass trombone accent dB | -1.9 | -0.9 | [measured] |
| premaster spikes | 0 | 0 | [measured] |

### Movement II (v30); slow-movement references: Brahms 1 II and Brahms 4 II

| measure | r04 | r05 | Brahms 1 II / 4 II | |
|---|---|---|---|---|
| LRA LU | 20.9 | 22.1 | 15.2 / 16.9 | [measured] |
| short-term p95 / max LU | +6.9 / +9.7 | +6.8 / +9.2 | +5.0 / +7.6 and +5.4 / +7.0 | [measured] |
| Spearman | 0.74 | 0.66 | | [measured] |
| Spearman, without hairpin bars | 0.66 | 0.56 | | [measured] |
| inversions, all / outside hairpins | 19 / 12 | 30 / 12 | | [measured] |
| step dB pp>p, p>mp, mp>mf, mf>f, f>ff | | 2.8, 2.8, 5.8, 6.3, 4.1 | | [measured] |
| melodies vs loudest / vs sum (of 14, balanced bars) | 7 / 11 | 7 / 10 | | [measured] |
| cuts >= 3 dB | 79 | 64 | | [measured] |
| max fader slope dB/s | 3.3 | 5.4 | | [measured] |
| < 100 Hz share dB | -10.6 | -10.0 | | [measured] |
| 2-6 kHz share dB | -9.5 | -11.4 | | [measured] |
| roll settles dB | -2.1 / -7.1 / -5.2 | -1.4 / -3.7 / -4.4 | | [measured] |
| timpani loudest stem in roll bars | 0 / 10 | 0 / 10 | | [measured] |
| premaster spikes | 6 | 3 | | [measured] |

Notes on the tables:
- Raw inversions and Spearman count the restored hairpins as conflicts. A bar printed p with a crescendo to f is louder than a flat p bar, as intended. The "without hairpin bars" rows remove that effect [inferred].
- The A/B without the hairpin fix gave m2 LRA 22.0. So the wider m2 range does not come from the hairpin fix [measured].

## 3. What got worse

1. **The m2 range and order.**
   - LRA 20.9 -> 22.1; Spearman 0.74 -> 0.66 (0.66 -> 0.56 without hairpin bars).
   - The main cause is the woodwind mp passage in bars 31-36: it sits 2-4 dB lower with the Iowa bass clarinet and bassoons [measured].
   - These stems are calibrated per printed dynamic in a one-note test, but exposed soft woodwind writing still lands below the strings around it [inferred].
2. **m1 roll 1-4 is less audible.** Its audible share fell 0.62 -> 0.38. The settle is now right (-4.7 dB), but the whole-bar floor of the segment balance trims it.
3. **m1 cuts of 3 dB or more on stems printed at or above the melody:** 18 -> 34. per_bar_need now cuts per bar instead of keeping the cut at the phrase maximum.
4. **m1 melodies against the loudest other stem:** 12 -> 11 of 20. **m2 melodies against the sum:** 11 -> 10 of 14.
5. **The m2 maximum fader slope:** 3.3 -> 5.4 dB/s. This is still below critic 3's 16-20 dB/s problem level.
6. **The 2-6 kHz share fell 2-2.4 dB in both movements.** This is a band share against the whole mix. The third-octave comparison with the Brahms references puts 2.5-3.2 kHz within +1 dB, so this measure moved toward the references [measured on premasters].

## 4. Still open

- **Instruments.** Horns, trumpets, trombones and cor anglais are still FluidR3.
  - Horns step 1.76 dB per printed step and trumpets 1.31 dB.
  - Iowa has brass at pp/mf/ff, and build_iowa.py should work for it with its own calibration.
- **The m2 range (LRA 22.1 against the references' 15-17) and the soft woodwind passages.**
  - Next step: a per-stem level check of exposed p/mp woodwind passages against the strings.
- **Equal-dynamic melodies are still under their competitor** (m1: 9 of 20 against the loudest other stem).
- **Timpani.**
  - Pitch-51 roll periodicity is 0.25-0.27.
  - m1 roll 1-4 is masked at the end by the floor.
- **Bass trombone accents** are -0.9 dB; the target is ≥ 3 dB.
- **The low end:** 62 Hz is still about -5 dB against the references.
- **Uneven steps:** m1 mp>mf is -0.4 dB and mf>f is 6.0 dB.

## 5. How to rebuild

```
cd /mnt/project-files/symphony/render
ps aux | grep render.py          # one render at a time
python3 r05/render.py --score /mnt/project-files/symphony/mvt1/v156 --out r05/out-m1.mp3 --work /tmp/render-05-m1
python3 r05/render.py --score /mnt/project-files/symphony/mvt2/v30  --out r05/out-m2.mp3 --work /tmp/render-05-m2
# the processed MIDI is <work>/render.midi (r05-mX.midi here); --midi-out PATH writes it elsewhere
bash r05/meas/scripts/meas.sh /tmp/render-05-m1 /tmp/out-m1.mp3 /tmp/meas-m1 r05-m1
```

Rebuild the Iowa samples from assets/iowa/src (the downloaded originals are unchanged):

```
python3 r05/build_iowa.py clarinet assets/iowa/src/clarinet assets/iowa/clarinet r05/sfz/clarinet-iowa.sfz --pan-spread 35
# the same for bassclarinet, oboe and flute; bassoon adds --vel 35,52
```

Calibration helpers:
- `[WORK_B=dir] python3 r05/meas/scripts/engcal.py WORK STEM_BASENAME STAFF_KEY CONFIG_A CONFIG_B [WAVDIR]`: the level per printed dynamic for one stem under two configs (WORK_B: an articulate.py run with config B, because the CC11 trims live in the MIDI); printed_trim_dB is set from it;
- `python3 r05/meas/scripts/eqtune4.py OLD_EQ_JSON NEW_EQ_JSON <work folder>...`: the premaster LTAS with the EQ change applied, against the mean of the four Brahms references.

## 6. Housekeeping

- WAV stems were kept in /tmp only, and the /tmp work folders were deleted at the end.
- No score was changed, and nothing was written into mvt1/ or mvt2/.
- No software was installed.
