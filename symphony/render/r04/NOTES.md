# r04: balance that obeys the printed dynamics, audible rolls in printed order, bus EQ, VSCO harp

r04 is built from r03 and critic 3's plan (critics/c03.md section 9). Test inputs (TESTSET.md): movement I =
symphony/mvt1/v156, movement II = symphony/mvt2/v30. "Before" = r03 on the same inputs, as measured by critic 3
(critics/c03/m1, m2, nobal-m1, nobal-m2; critic 3's renders are bit-identical to r03/out-m*.mp3). "After" = r04/out-m1.mp3
and out-m2.mp3, measured with the same scripts (r04/meas/scripts/meas.sh = critic 3's meas.sh plus duckaudit, rollband
and melody_nonmel). Tables are in r04/meas/m1 and m2, no WAVs. Every number below is **[measured]** unless marked
**[inferred]**. Nobody listened.

Both outputs come from the same code and config with one command each. The config holds no bar numbers. Checked on the
newest versions as well: mvt1/v169 (182 bars, 20 melodies, 8 rolls, 0 unmatched notes) and mvt2/v44 (92 bars, 16
melodies, 3 rolls, 0 unmatched) run through score_events, articulate and marks without errors.

## 1. What changed, by plan item

### Item 1. Balance stage obeys the printed dynamics: done (lib/balance.py)
Each bar's printed dynamic per stem comes from notes.csv (the loudest printed dynamic of the stem's notes in that bar;
fp counts as p).
- **(a) Caps by printed dynamic.** A stem printed louder than the melody is never cut in that bar. A stem printed at the
  same dynamic is cut by at most `duck_same_dB` = 5. A stem printed softer is cut by at most `duck_max_dB` = 8. The
  comparison uses the softest marked melody sounding in the bar. Otherwise a cut made for one melody (e.g. the m2
  cello espr. at mf, bars 57-64) put the violins (mf) under a second melody printed softer (horns, mp). In the
  offline simulation that rule took m2 from 31 to 16 inversions.
- **(b) Tutti.** A bar is a tutti when at least half of the sounding stems are printed f or louder. A phrase ends at its
  first tutti bar where the melody itself is printed f or louder. No stem is cut in a tutti bar.
- **(c) Marked melodies are never cut.** Concurrent melodies are only lifted, within `lift_max_dB` = 3. New
  `inv_margin_dB` = 1: in each bar, a melody is lifted at most to 1 dB over any sounding stem printed louder than it.
  A lift should not turn the printed order upside down.
- **(d) Bar loudness kept.** After the gains are set, each bar gets a common offset so that the summed whole-bar
  loudness of all stems stays within ±1 dB (`preserve_dB`) of the no-balance bar. The result is relief between
  staves, not a quieter bar. The roll rule runs after this offset.
- **(e) Slow faders.** `smooth_s` 0.4 → 1.5 s, a centred moving average, so the ramp starts about 0.75 s before the
  bar.
- Parameters were tuned offline (`meas/scripts/sim.py`). The simulation passes critic 3's no-balance stem levels
  through the balance code. It reproduced the full-render numbers to within 5 inversions and 0 melodies
  (`meas/balance_sim.txt`). `duck_same` 4 → 5 and `duck_max` 6 → 8 (critic 3 suggested 4 / 6) recovered 2 m1
  melodies (10 → 12 at or over the loudest other stem) without an inversion cost in m2.
- Sources: Rimsky-Korsakov, *Principles of Orchestration* (https://gutenberg.org/files/33900/33900-h/33900-h.htm):
  the printed dynamics express the balance, and the melody gets relief by one step, not by undoing a tutti. Fader
  riding as a slow, phrase-length move
  (https://vi-control.net/community/threads/questions-about-prepping-ahead-for-dynamics-and-volume-for-orchestral-mock-ups.159951/).

### Item 2. Timpani rolls audible again, in printed order: done (articulate.py, calib_timp_roll.py)
- Settle -6 dB (tau 1.5 s) plus -2.5 dB for rolls over 3.5 s. r03 used -6 plus -7.
- The start stroke is now an accent at the roll velocity +4. In r03 it was -14.
- The roll note is exempt from `fff_velocity_cut` (`timp_roll_fff_cut: false`).
- New `timp_roll_trim_dB` by **printed** dynamic: f +1.5, ff +5, fff +5.5. LilyPond's velocities plus the global
  velocity curve made printed f, ff and fff rolls almost equal: ff/fff velocity 89/92 against f 84, while the CC11
  curve falls 2.5 dB between velocity 84 and 91.
- New `timp_roll_pitch_trim_dB`: the recorded roll samples differ by up to 3 dB from drum to drum. The table is
  measured by `calib_timp_roll.py` (K-weighted level 1-3 s into a 4 s roll per MIDI pitch), so the same printed
  dynamic gives the same level on every drum.
- The balance stage's roll rule (3 dB under the loudest other stem) stays as the safety net. It now holds the fff
  climax roll 122-130 at exactly -3 dB.
- Sources: Dan (BRIEF.md); https://www.percussionclinic.com/art_timptech.htm (a roll begins with a defined first stroke).

### Item 3. Wind staccato from recorded staccato samples: tested, not enabled
- The VPO 3.2 archive has only one woodwind staccato set: VSCO 2 CE flute, 10 samples (zip index read). Oboe, clarinet
  and bassoon staccatos do not exist there. I added the 10 flute files to assets and wrote `sfz/flute-stac-vsco2.sfz`.
  `stem.py` gained an `sfz_overlay`: chosen MIDI channels of a FluidSynth stem are played by sfzplay. `articulate.py`
  can put wind staccatos on channel base+4 without the accent channel base+8, which would collide with GM drum
  channel 9 for the second voice.
- One-note test (`meas/scripts/flcal.py`), dry, note 0.11 s: FluidR3 flute sounds 0.16-0.21 s to -20 dB, and the VSCO
  staccato sample sounds 0.21-0.29 s. **The recorded staccato is longer, not shorter.**
- In the m1 flute stem (11 staccatos, wet): FluidR3 gives -13.6 dB at +250 ms and 0.24 s audible. VSCO, level-matched
  within 3 dB, gives -11.1 dB at +250 ms and 0.16 s audible. The decay at +250 ms is worse; the -20 dB length is
  shorter, but only because the peak is 3.3 dB lower.
- The 2.07 "audible ratio" of flute staccato is mostly the hall. The VPO violin staccato samples measure 1.99 by the
  same measure (critic 3's stemcmp). [inferred] The < 1.3 target cannot be met with a 1.6 s room and -20 dB as the
  end point.
- Kept off; the code and samples stay for a later cycle.

### Item 4. Spectral blend EQ: done
- **Mix-bus EQ** (`lib/busq.py`, config `master.eq`): RBJ cookbook biquads (https://www.w3.org/TR/audio-eq-cookbook/)
  run forward-backward at half gain, so the net response has zero phase:
  - bell 280 Hz -3.5 dB, Q 1.2;
  - bell 720 Hz -1.5 dB, Q 1.4;
  - bell 6.3 kHz +2.5 dB, Q 1.0.
  These were tuned offline on both premasters against the mean third-octave LTAS of Brahms 1 and 4
  (`meas/scripts/eqtune.py`). Mix-bus EQ leaves the stem balance untouched. Sources: cutting about 200-350 Hz against
  low-mid build-up from stacked sample ambience
  (https://old.cinematiccomposing.com/blog/composing-part-iv-eq-reverb ; https://mastering.com/muddy-mixes/).
- String `air` shelf: -14 dB above 9 kHz → -8 dB above 10.5 kHz.
- Clarinets and bass clarinet: high shelf +5 dB above 3 kHz.

### Item 5. Harp from VSCO 2 CE: done
- The 18 KSHarp samples (CC0) were added to assets. `sfz/harp-vsco2.sfz` has key ranges between the sample pitches.
  The names were checked by pitch detection; the samples are about 8 cents flat, so `tune=8`.
- Velocity is gain only. The string rings after note-off and is damped over 2 s (`ampeg_release`).
- Level: the one-note test against FluidR3 harp (program 46) gave -21 dB in the core register (C2-G5). FluidR3 is
  8-10 dB weaker above C6, so VSCO is more even. The stem levels then measured 0.3-4.1 dB under FluidR3 in the
  four harp stems, so `sfz.gain_dB` = -18.5. That puts them within about ±2 dB [inferred from the linear gain].
- FluidR3 is the fallback: set `engine` back to `fluidsynth`.

### Item 6. Top-end balance: done (printed_trim_dB)
- Trumpets 1-2: f -2 → -5 dB.
- Trombones 1-2: mp +3. Bass trombone: mp +4. These stems were 6.3 / 8.4 dB under the string median at mp. Critic 3's
  table reads "p", but the column is mp; my first try trimmed p and changed nothing.

### Item 7. Section timing: tested, disabled
`articulate.py` has a `timing` block: a family offset (strings +10 ms soft / +4 ms loud, brass +4 / +2, others 0) plus
±5 ms random held per 8 s segment, per staff. With it on (render i3), onset peak correlation fell 0.56 → 0.551 (m1)
and 0.29 → 0.26 (m2), and the m2 lag rose 60 → 70 ms. Critic 3's target was "not lower", so it is off
(`timing.enabled: false`). The code stays. Sources: https://forum.vsl.co.at/post/232667 ;
https://vi-control.net/community/threads/timing-of-brass-strings.121576/

### Item 8. Robustness: done
- `lib/staffmap.py`: a staff with no config entry borrows the entry of the instrument its name names: Piccolo →
  Flutes 12, English horn → Cor anglais, Violins 2 → Violins II, Contrabasses → Double basses, and so on.
  `articulate.py` and `stem.py` use it, so a renamed staff no longer aborts the render. Tested with a stem MIDI renamed
  to "Oboe 3", which rendered with the Oboes 12 entry.
- `tools/score_events.py` and `tools/rtk.py` are identical to `r04/lib/` (diff).

### Other
- `render.py --reuse-synth` (for tuning only): a stem's stage-1 signal is reused when its MIDI, its stem config and
  the synth code are unchanged (sha1). The final outputs were rendered without it, in fresh work folders.
- Tested and rejected: a slow top-only master leveler (`lib/leveler.py`, unused), meant to bring the m2 short-term
  max and p95 down. On the m2 premaster (threshold +6 LU, ratio 2) the LRA fell 20.0 → 18.9, but max relative to I
  only fell 10.0 → 9.3, and p95 did not move (7.2 → 7.3). The integrated level falls with the climax, because the
  loud bars dominate the gated integrated loudness. [inferred] m2's p95 is the shape of a slow movement with one
  big tutti, not a mix fault.

## 2. Before / after

### Movement I (v156)

| measure | r03 | **r04** | target (c03) | |
|---|---|---|---|---|
| LRA (LU) | 19.0 | **19.2** | 18-20.5 | [measured] |
| short-term p10 / p50 / p95 / p99 / max (LU rel. I) | -14.8 / -5.4 / +4.3 / +5.6 / +6.1 | -15.0 / -5.5 / +4.2 / +6.4 / +7.1 | max < +8 | [measured] |
| Spearman bar loudness vs printed dynamic | 0.83 | 0.82 | >= 0.83 | [measured] |
| bars printed <= mf louder than the median f bar | 11 | **10** | <= 10 | [measured] |
| melodies >= 0 dB vs loudest other stem | 10/20 | **12/20** | >= 10 | [measured] |
| melodies >= -6 dB vs sum of the others | 17/20 | **14/20** | >= 17 | [measured] worse |
| melodies vs loudest non-melody stem >= 0 dB; median | 19/20; +4.4 | 19/20; +3.7 | | [measured] |
| balance inversions | 431 | **365** | not worse | [measured] |
| stems > 6 dB from string median; median spread | 4; 4.1 | **2**; 4.1 | <= 3 | [measured] |
| stem-bars cut >= 3 / >= 6 dB | 205 / 171 | 145 / **25** | >= 6: <= 30 | [measured] |
| stem-bars cut while printed above the melody | 0 | 0 | 0 | [measured] |
| max fader slope (dB/s) | 20.0 | **5.3** | <= 6 | [measured] |
| timpani loudest stem in roll bars | 0/31 | 0/31 | 0 | [measured] |
| roll start level f (117, 167) / ff (41) / fff (122), LUFS | -31.5, -37.0 / -33.5 / -35.1 | -30.3, -32.6 / **-28.8** / **-25.9** | rising by >= 2 dB per step | [measured] |
| roll body vs loudest other stem (bars after the first) | -12 to -23 | -3 to -17 (ff 41: -7/-10, f 117: -7 to -10, fff: -3, the safety net) | -4 to -9 | [measured] |
| roll in its own band, rest of roll: ff / f / f / fff | -14.3 / -13.3 / -14.5 / -14.6 | **-6.6 / -8.8 / -8.2 / -3.0** | >= -8 for f-fff | [measured] |
| roll end change (dB) | -7.3 to -11.0 | -3.9 to -7.5 (ppp 1-4: -0.8) | -5 to -8 | [measured] worse |
| roll stroke / loop autocorrelation | <= 0.29 / <= 0.21 | <= 0.29 / <= 0.20 | < 0.25 / < 0.4 | [measured] |
| share < 100 Hz (mix; lowstem) | -11.6; -10.4 | **-9.9; -9.6** | -9 to -11 | [measured] |
| third-octave vs mean(Brahms 1, 4): 250 / 315 / 6.3k / 8k Hz | +3.2 / +3.1 / -4.1 / -3.8 | **+0.9 / +1.0 / -0.3 / -0.1** | ±1.5 / ±2 | [measured] |
| third-octave 2.5 / 3.2 / 10 kHz | +0.9 / +0.3 / -0.2 | +2.8 / +2.5 / +2.7 | | [measured] worse |
| clarinets / bass clarinet share > 6 kHz (dB) | -69.5 / -85.3 | -65.6 / -80.5 | > -60 | [measured] |
| harp RH / LH share > 6 kHz | -34.8 / -57.8 | -35.8 / -53.6 | RH <= -35 | [measured] |
| trumpets 1-2 at f vs string median | +5.0 | **+2.2** | about +1 | [measured] |
| bass trombone / trombones at mp vs string median | -8.3 / -6.2 | -4.5 / -3.3 | | [measured] |
| L/R correlation; pan spread | 0.60; 0.32 | 0.61; 0.32 | | [measured] |
| cut-offs to -20 dB / RT60 est. | 0.54 / 1.43 s | 0.55 / 1.44 s | | [measured] |
| onset lag; peak correlation | 50 ms; 0.56 | 50 ms; 0.555 | not lower | [measured] |
| premaster isolated HF spikes | 0 | 0 | 0 | [measured] |
| articulations: tremolo Vln I/II/Vla; string staccato +250 ms; flute stacc ratio; bass trombone accent | +3.5/+9.1/+3.9; -11.3/-11.9/-4.1; 2.07; -1.9 | +3.8/+9.0/+3.9; same; 2.07; -1.9 | | [measured] unchanged |

### Movement II (v30)

| measure | r03 | r03 no-bal | **r04** | target (c03) | |
|---|---|---|---|---|---|
| LRA (LU) | 17.7 | 20.1 | **20.9** | 18.5-20.5 | [measured] slightly over |
| short-term p10 / p50 / p95 / p99 / max | -10.6 / -6.7 / +7.2 / +10.3 / +10.6 | -13.2 / -9.5 / +6.9 / +9.0 / +9.6 | -14.0 / -9.6 / +6.9 / +9.2 / **+9.7** | max <= +9, p95 <= +6 | [measured] not met |
| Spearman | 0.72 | 0.71 | **0.74** | >= 0.80 | [measured] |
| balance inversions | 46 | 22 | **19** | <= 25 | [measured] |
| stem-bars cut while printed above the melody | 2 | – | **0** | 0 | [measured] |
| stem-bars cut >= 3 / >= 6 dB | 197 / 1 | – | 79 / 0 | | [measured] |
| max fader slope (dB/s) | 18.5 | – | **3.3** | <= 6 | [measured] |
| Violins I loudest stem (bars) | 12 | 17 | 18 | | [measured] |
| melodies >= 0 dB vs loudest other | 9/14 | 6/14 | 7/14 | >= 12 | [measured] worse than r03 |
| melodies >= -6 dB vs sum | 14/14 | 9/14 | 10/14 | 14 | [measured] worse than r03 |
| melodies vs loudest non-melody stem >= 0 dB; median | 13/14; +3.8 | – | 10/14; +2.3 | | [measured] |
| stems > 6 dB from string median | 5 | 1 | 5 | 0 | [measured] |
| timpani loudest in roll bars | 0/10 | | 0/10 | 0 | [measured] |
| roll body vs loudest other (3 ppp rolls) | -3 to -14 | | -4 to -9 | -4 to -9 | [measured] |
| roll end change (dB) | -6.1 / -11.2 / -8.6 | | -1.4 / -7.2 / -4.6 | -5 to -8 | [measured] worse |
| roll stroke autocorrelation (67-70) | 0.27 | | 0.27 | < 0.25 | [measured] |
| share < 100 Hz | -12.2 | | **-10.6** (lowstem -11.4) | -9 to -11 | [measured] |
| third-octave vs Brahms: 250 / 315 / 6.3k / 8k Hz | +5.3 / +2.8 / -6.2 / -5.0 | | **+1.8 / +0.2 / -0.6 / +0.9** | ±1.5 / ±2 | [measured] |
| cut-offs to -20 dB / RT60 est. | 0.48 / 1.18 s | | 0.45 / 1.31 s | | [measured] |
| onset lag; peak correlation | 60 ms; 0.29 | | 60 ms; 0.267 | not lower | [measured] worse |
| premaster isolated HF spikes | 3 | | 6 (all at 104.4-104.9 s, -50 dBFS region) | | [measured] |
| tremolo (4 string stems) | +2.9 / +7.1 / +6.4 / +8.2 | | +3.0 / +7.2 / +6.4 / +8.2 | | [measured] |

## 3. What got worse
- **Melodies against the sum of the others: m1 17 → 14 of 20; m2 14 → 10 of 14.** In m2 the count against the loudest
  other stem also fell, 9 → 7. This is the price of item 1.
  - r03 reached those counts by cutting stems printed at or above the melody, by up to 8 dB.
  - The remaining failures are passages where the score prints the competing stems louder than the melody, or several
    marked melodies at once:
    - m2 horns p espr. 53-60 under strings at mf;
    - m2 violas pp espr. 71-78 under Violins I p;
    - m1 Violins II pp, clarinets p, horns p and Violins I p, all marked, in 55-63;
    - the m2 cello espr. 57-64, whose phrase is measured into the ff tutti (-12.4 dB against the sum) but which the
      balance now ends there.
  - [inferred] To lift those lines further, the render would have to contradict the printed dynamics (inversions)
    or change the score.
- **m2 LRA 20.9** is 0.4 LU over the band. That is the no-balance shape (20.1) plus the timpani and bus EQ changes;
  the references span 13.4-21.8.
- **m2 short-term max +9.7 / p95 +6.9** are still over target (they were +9.6 / +6.9 with no balance in r03). The
  master leveler test (section 1, Other) shows they do not respond to master compression.
- **Roll settle is smaller:** the end change is -3.9 to -7.5 dB in m1 (r03 -7.3 to -11.0). The m1 bar 1-4 ppp roll and
  the m2 bar 2-3 roll show only -0.8 / -1.4 dB, because the roll rule cuts the exposed first bar to 3 dB under the soft
  strings, which flattens the curve. All three m2 rolls are printed ppp. Dan asked for rolls that fade (BRIEF.md), so
  the critic should judge whether -4 to -5 dB over 5-10 s is enough.
- **m1 f rolls:** the 117 roll starts only +1.5 dB under the ff roll (target 2 dB per step). The 167 roll starts
  +3.8 dB under it.
- **Onset peak correlation** m2 0.29 → 0.267 and m1 0.56 → 0.555 with timing off. [inferred] The cause is the harp
  samples (slower plucks than FluidR3's) or the 6.3 kHz bus bell; not separated.
- **2.5-3.2 kHz is now +2.5 to +2.8 dB over Brahms** in both movements (r03 within 1 dB). This comes from the
  clarinet shelves and the skirt of the 6.3 kHz bell. Watch for edge.
- **m2 premaster HF spikes 3 → 6**, all at 104.4-104.9 s. They are the FluidR3 contrabassoon's low-note pulse train
  (clicks2 finds 232 such pulses in that stem from 104.0 s, in r03 too). They pass the detector more often after the
  +2.5 dB at 6.3 kHz. The region is around -50 dBFS RMS; [inferred] harmless.

## 4. Still open
- Melody relief where the score prints the accompaniment louder (see 3); the m2 cello espr. into the tutti.
- Wind short notes: flute staccato 2.07 (mostly the room, see item 3). Oboes, clarinets and bassoons have no recorded
  staccato in the VPO archive.
- Bass trombone accent -1.9 dB (n = 5); clarinets' share > 6 kHz still -65.6 dB (target -60).
- Roll stroke autocorrelation 0.29 (m1 41-43) and 0.27 (m2 67-70). [inferred] This is the recorded roll's own stroke
  rate on one sample.
- Settle depth against audibility (see 3).
- Section timing needs an attack-delay measurement per articulation before any offset (critic 3, 8.3).
- dB per printed step 1.0-3.7 (target 4-5); the m1 mp→mf step is 1.0 dB.

## 5. How to rebuild
```
cd /mnt/project-files/symphony/render
ps aux | grep render.py          # one render at a time
python3 r04/render.py --score /mnt/project-files/symphony/mvt1/v156 --out r04/out-m1.mp3 --work /tmp/render-04-m1 --midi-out r04/r04-m1.midi
python3 r04/render.py --score /mnt/project-files/symphony/mvt2/v30  --out r04/out-m2.mp3 --work /tmp/render-04-m2 --midi-out r04/r04-m2.midi
# measure: WORK MP3 OUTDIR LABEL (copy the MP3 to /tmp first; the shared folder can fail reads)
bash r04/meas/scripts/meas.sh /tmp/render-04-m1 /tmp/out-m1.mp3 /tmp/meas-m1 r04-m1
python3 r04/meas/scripts/ltas.py r04-m1=/tmp/meas-m1      # third-octave vs Brahms 1/4
python3 r04/calib_timp_roll.py                            # re-derive timp_roll_pitch_trim_dB if the roll samples change
```
Each render takes 5-6 minutes with 4 jobs. Options:
- `--events` reuses an events.tsv;
- `--no-balance` turns off the mix-stage balance for A/B tests;
- `--keep-synth` keeps the stage-1 stem signals;
- `--reuse-synth` reuses unchanged stage-1 signals, for tuning.

Offline tools in `meas/scripts`:
- `sim.py`: balance simulation on no-balance stem levels;
- `timptest.py`: timpani stem only;
- `stemtest.py`: one stem;
- `eqtune.py`: bus EQ on a premaster;
- `flcal.py`, `hpcal.py`: one-note calibration;
- `staccheck.py`, `harpcmp.py`, `levtest.py`.

## 6. Housekeeping
- Assets added (assets/README.md updated): VSCO 2 CE harp (18 files) and flute staccato (10 files) under
  assets/vpo3/libs/VSCO2-CE/, CC0, fetched from the VPO 3.2 archive's zip index.
- Nothing was written into symphony/mvt1 or symphony/mvt2.
- `lib/leveler.py` is unused (tested, rejected). The flute staccato overlay and the timing block are in the code and
  switched off.
