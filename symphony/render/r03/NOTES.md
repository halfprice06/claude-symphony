# r03: one renderer for both movements, rolls that settle, balance by ducking, bass back, loop clicks gone

r03 is built from r02 (symphony/render/r02) and critic 2's plan (critics/c02.md section 9). Test inputs:
movement I = symphony/mvt1/v156 (182 bars, 4/4, percussion), movement II = symphony/mvt2/v30 (92 bars, mixed 3/4 and
4/4, no percussion). Baselines: critics/c02/r02-m1.mp3 and r02-m2.mp3. Both outputs come from the same code and the
same config with one command each. The config has no bar numbers. The points in `dynamics.extra_dB_points` are MIDI
velocities, not bars.

Outputs: `out-m1.mp3`, `out-m2.mp3`, processed MIDIs `r03-m1.midi`, `r03-m2.midi`. Measurements are in `meas/m1` and
`meas/m2` (tables, PNG and JSON, no WAVs). Measurement scripts are in `meas/scripts`. The VPO wind A/B is in
`meas/vpo_winds_ab_m1.txt`.

## 1. What changed, by plan item

### Item 1. One renderer for any version and metre: done
- `lib/score_events.py` now takes bar and beat from the MIDI time-signature grid (`rtk.midi_info()["bar_ticks"]` plus
  bisect), so it works for mixed metre. Under r02, m2 bars after the first 3/4 bar were wrong. The `--ly-dir` default
  (it pointed at mvt1/v120) is removed. **For the critic: `tools/score_events.py` needs the same fix.**
- `lib/marks.py` (new) derives the marked melodies from the LilyPond event log. It takes the text scripts that match
  `espr|dolce|cantabile|solo`. A phrase runs while the staff plays in consecutive bars, for at most 8 bars (the rule in
  critic 2's `melody2.py`). It finds 20 phrases in m1 and 14 in m2, the same passages as critic 2's `melody.md`. It
  also finds the timpani rolls longer than one bar: 8 in m1, 3 in m2. There is no bar list in config.
- `perc.py` reads the DrumStaff of the `--score` folder, places its events on the MIDI bar grid, has no 4/4 assert,
  and does nothing when the score has no percussion. The 4 percussion events of m1 land on the same ticks as in r02.
- `render.py` takes `--score` (`--v120` is kept as an alias). It writes only to `--work`, plus `--out` and `--midi-out`.
  It never writes into the code folder or a score folder.

### Item 2. Timpani rolls: done
- **The settle never reached the rolls in r02.** The sample roll plays on its own channel, and that channel had no
  CC11. Now `articulate.py` copies the program to the roll channel and writes CC11 there too, so the settle, the
  hairpins and the per-stem trims all apply to it.
- **CC11 hold bug (sfz path, `stem.py`).** r02 interpolated linearly between sparse CC11 messages, so a settle that
  ended in one message 17 s later drifted back up over the whole roll. Now a CC11 value holds until the next message,
  as it does in a MIDI synth: a point (t_next − 20 ms, previous value) is inserted between messages more than 21 ms
  apart. This changes nothing for dense curves.
- Settle: `settle_tau` 1.5 s; rolls longer than 3.5 s fall a further 7 dB (`long_s`, `long_dB`). Only a printed `\<`
  makes a roll grow. The roll trim went from −8 to +6 dB, because r02's level depended on the missing CC11 headroom.
- Loop pattern: `sfzplay.random_loop()` builds the roll from random segments of the loop (0.9–1.8 s) joined by 250 ms
  equal-power crossfades, with ±1 dB slow random drift (configured per region in `loop_random`).
- Balance (lib/balance.py, roll rule): in every bar of a roll longer than a bar, the timpani is cut until it sits 3 dB
  under the loudest other stem (at most 15 dB). The comparison uses whole-bar levels. The rule does not apply where the
  timpani carries a solo or espr. mark. After the settle, only 4 bars of m1 and 1 bar of m2 needed a cut (0.8–1.8 dB).
- Sources: Dan (BRIEF.md); https://www.percussionclinic.com/art_timptech.htm ;
  https://theinstrumentalist.com/march-2009/percussion-rolls/ ;
  https://sfzformat.com/opcodes/loop_mode ; https://sfzformat.com/opcodes/loop_crossfade

### Items 3 and 4. Balance by ducking, melodies on top: done (new mix stage)
- The CC11 melody lift of r02 is removed from `articulate.py`. Melodies are now balanced in the mix stage, like riding
  faders on the measured stems:
  1. Every stem is synthesised once (`stem.py --synth-out`) and placed.
  2. Each stem's K-weighted level while it sounds is measured per bar (the measure behind tools/stems.py).
  3. `lib/balance.py` computes a gain per bar and per stem.
  4. The changed stems are placed again from their synthesised signal with a smoothed gain curve (0.4 s; `stem.py
     --from-synth --gain-curve`).
- Rule per phrase:
  - The melody gets at most +3 dB to sit 1 dB over the loudest other stem.
  - Each louder non-melody stem is cut by its median excess, at most 8 dB.
  - Marked melodies that sound together are brought level with each other: the louder one is cut by at most 4 dB.
  - If the melody is more than 5 dB under the power sum of the others, the non-melody stems get a common extra cut.
  - Harp and percussion are left out of the comparison.
  - The rule runs in 4 passes. No stem is ever raised more than 3 dB in total.
- The global velocity-to-dB curve (`dynamics.extra_dB_points`) was refitted for wider mp→mf and mf→f steps.
- New `printed_trim_dB` per stem, keyed on the printed dynamic: oboes ff/fff −3, flutes −2, clarinets −2, horns 1-2 −3,
  trumpets 1-2 f −2 and ff/fff −4, basses −2. My first attempt keyed these trims on `dyn_corr_dB`, which is keyed on
  velocity, and they did nothing. LilyPond scales velocity per instrument (oboes ff = velocity 64; see
  https://lilypond.org/doc/v2.24/Documentation/internals/beat_005fperformer and the performer docs), so the same
  velocity means a different printed dynamic on different staves.
- Velocity outliers: within a group of (staff, printed dynamic, accent class), outside hairpins, a note more than 15
  velocity steps *above* the group median (groups with n ≥ 10) is set to the median. 86 notes in m1, 19 in m2. A
  first version that also raised low outliers made the m2 bassoons at f 10 dB too soft, so only high outliers are
  corrected now.
- Sources: https://vi-control.net/community/threads/questions-about-prepping-ahead-for-dynamics-and-volume-for-orchestral-mock-ups.159951/ ;
  https://vi-control.net/community/threads/poll-how-do-you-use-dynamics-and-expression.101377/ ;
  https://vi-control.net/community/threads/rant-about-cc1-cc11-and-velocity.168479/ ; https://tech.ebu.ch/docs/tech/tech3342.pdf

### Item 5. Bass back, less air: done
- New per-stem `tone.low_shelf_Hz/low_shelf_dB` and an `air` high shelf in `stem.py`:
  - Double basses +6 dB below 100 Hz.
  - Cellos +3 dB below 150 Hz, with the cello stem gain −2 dB.
  - All VPO string stems −14 dB above 9 kHz (air absorption over about 20 m is several dB per 10 m at 8–12 kHz:
    https://sengpielaudio.com/calculator-air.htm).
- The bass was checked with `lowstem.py` (unweighted) as well as with LUFS.

### Item 6. Woodwinds and brass from VPO: tested, not kept
- I downloaded the VPO 3 archive (https://www.virtualplaying.com/virtual-playing-orchestra/) into /tmp only and
  played 14 wind and brass stems of m1 through sfzplay, with the same sample-offset attack handling as the strings.
  Results are in `meas/vpo_winds_ab_m1.txt` [measured]:
  - Articulation lengths did not get shorter. Flute detached audible ratio: VPO 1.65 vs FluidR3 1.53. Flute staccato:
    1.86 vs 2.07, still far from the 1.3 target.
  - Dynamic layers are irregular: cor anglais f is louder than ff, and the trumpets change only 0.96 dB per printed
    step.
  - Levels are 15–20 dB hotter, so the change would need a full recalibration of every wind and brass stem.
- Winds and brass therefore stay on FluidR3. Nothing was added to assets/, so assets/README.md is unchanged.

### Item 7. Loop-seam clicks: done
- `sfzplay.py` gives every looped sustain a 100 ms equal-power loop crossfade (`DEFAULT_LOOP_XF`), not only the
  timpani roll (https://sfzformat.com/opcodes/loop_crossfade).
- Cause of the bass clicks 1.857 s apart: the Hermite resampler read 3 frames past the loop end, which held unrelated
  sample data. Those frames are now copies of the frames after the loop start.
- Samples started at an `offset` get at least a 3 ms attack.
- `trigger=release` regions now play at note-off as one-shots (https://sfzformat.com/opcodes/trigger: "Region will play
  on note-off"). The round robin is keyed per (key, trigger).

### Item 8. Section timing: not done (time).

### Inactive code
`articulate.py` can send wind and brass staccato and accent notes to their own channels (`artic_channels`: +4
staccato, +8 accent). No stem uses this in this config, because the winds stayed on FluidR3.

## 2. Before / after

r02 = critic 2's baseline (critics/c02/m1, m2); r03 = meas/m1, meas/m2. Same tools, bars from the MIDI time
signatures. Brahms 1 and Dvořák values are critic 2's references.

### Movement I (v156)

| measure | r02 | r03 | target (c02) | |
|---|---|---|---|---|
| LRA (LU) | 22.2 | **18.9** | 18–20.5 | [measured] |
| short-term p10 / p50 / p95 / p99 / max (LU rel. integrated) | −17.6 / −5.9 / +4.9 / +6.1 / +6.9 | −14.8 / −5.4 / +4.3 / +5.6 / +6.1 | max < +8 | [measured] |
| Spearman, bar loudness vs printed dynamic | 0.74 | **0.83** | ≥ 0.80 | [measured] |
| bars printed ≤ mf louder than median f bar | 25 | **11** | ≤ 10 | [measured] |
| step p→mp / mp→mf / mf→f (dB) | 4.1 / 1.4 / 1.7 | 1.7 / **3.7** / **3.9** | ≥ 2.5 (mp→mf, mf→f) | [measured] |
| melodies ≥ 0 dB vs loudest other stem | 11/20 | 10/20 | ≥ 17/20 | [measured] |
| melodies ≥ −6 dB vs sum of the others | 17/20 | 17/20 | 20/20 | [measured] |
| melodies vs loudest *non-melody* stem: ≥ 0 dB, median | 19/20, +4.2 | 19/20, +4.4 | (companion measure, see 3) | [measured] |
| timpani loudest stem in roll bars | 3/31 | **0/31** | 0 | [measured] |
| roll level at end vs 0.4–0.8 s (dB) | −0.9 … +1.7 | **−7.3 … −11.0** | ≤ −6 (≤ −8 if > 2.5 s) | [measured] |
| roll loop autocorrelation 1.5–6 s | 0.60–0.77 | **0.09–0.21** | < 0.4 | [measured] |
| roll stroke autocorrelation | < 0.25 | up to 0.29 (bars 41–43) | < 0.25 | [measured] |
| share below 100 Hz (dB) | −14.7 | **−11.6** (lowstem −10.4) | −9 to −11 | [measured] |
| 63 Hz third-octave (dB) | −24.1 | −17.9 | within 4 dB of Brahms | [measured] |
| 12.7 kHz third-octave (dB) | −45.8 | −47.1 | 6 dB lower | [measured] |
| loud − soft at 5 / 10 kHz (dB) | 6.6 / 6.2 | 8.4 / 11.6 | | [measured] |
| L/R correlation; pan spread | 0.60/0.59; 0.34 | 0.60/0.60; 0.32 | | [measured] |
| cut-offs median / p90 (s) | 0.54 / 1.39 | 0.54 / 1.43 | | [measured] |
| onset lag; peak correlation | 50 ms; 0.52 | 50 ms; 0.56 | | [measured] |
| isolated HF spikes in premaster | 5 | **0** | 0 | [measured] |
| mp3 click candidates (critic 1 clicks.py) | 43 | 43 | ≤ 11 | [measured] |
| balance inversions; spread vs Violins I; vs string median; stems > 6 dB | 467; 6.2; 4.0; 6 | 431; 4.5; 4.1; 4 | not worse | [measured] |
| Violins I loudest stem (bars) | 13 | 13 | | [measured] |
| tremolo modulation Vln I / II / Vla (dB) | +3.2 / +9.1 / +3.5 | +3.5 / +9.1 / +3.9 | | [measured] |
| string accents; bass trombone accent; flute staccato ratio; fl/ob detached ratios | 6.4–7.8; −1.9; 2.07; 1.53/1.46 | unchanged | | [measured] |
| render time | – | 279 s | | [measured] |

### Movement II (v30)

| measure | r02 | r03 | target (c02) | |
|---|---|---|---|---|
| LRA (LU) | 22.0 | **17.7** | 18–20.5 | [measured] |
| short-term p10 / p50 / p95 / p99 / max | −15.4 / −11.2 / +6.6 / +8.8 / +9.7 | −10.6 / −6.7 / +7.2 / +10.3 / +10.6 | max < +8 | [measured] |
| Spearman, bar loudness vs printed dynamic | 0.64 | **0.72** | ≥ 0.80 | [measured] |
| dynamic steps (5 printed steps, dB) | 2.7 / 2.2 / 5.6 / 5.7 / 5.3 | 3.0 / 2.5 / 5.0 / 3.3 / 4.0 | ≥ 2.5 | [measured] |
| melodies ≥ 0 dB vs loudest other stem | 6/14 | **9/14** | ≥ 12/14 | [measured] |
| melodies ≥ −6 dB vs sum; median vs sum | 9/14; −1.2 | **14/14**; +0.1 | 14/14 | [measured] |
| melodies vs loudest non-melody stem: ≥ 0 dB, median | 8/14, +0.3 | **13/14, +3.8** | | [measured] |
| timpani loudest stem in roll bars | 5/10 | **0/10** | 0 | [measured] |
| roll level at end vs 0.4–0.8 s (dB) | c02: −0.9 … +1.7 (both mvts) | −6.1 / −11.2 / −8.6 | ≤ −6 / −8 | [measured] |
| roll loop autocorrelation | c02: 0.60–0.77 (both mvts) | 0.10 / 0.16 / 0.20 | < 0.4 | [measured] |
| share below 100 Hz (dB) | −15.2 | **−12.2** | −9 to −11 | [measured] |
| 63 Hz third-octave (dB) | −18.4 | −14.3 | | [measured] |
| 12.7 kHz third-octave (dB) | −47.5 | **−60.6** | 6 dB lower | [measured] |
| loud − soft at 5 / 10 kHz (dB) | 13.3 / 14.7 | 10.0 / 11.0 | | [measured] |
| L/R correlation | 0.56/0.53 | 0.53/0.51 | | [measured] |
| cut-offs median / p90 (s) | 0.56 / 1.50 | 0.48 / 1.18 | | [measured] |
| onset lag; peak correlation | 60 ms; 0.23 | 60 ms; 0.29 | | [measured] |
| premaster HF spikes | 2 | 3 (all −89 to −152 dB) | 0 | [measured] |
| mp3 click candidates | 1 | **0** | ≤ 0 | [measured] |
| balance inversions; spread vs string median; stems > 6 dB | 23; 3.6; 0 | 46; 4.6; 5 | not worse | [measured] |
| Violins I loudest stem (bars) | 23 | 12 | | [measured] |
| tremolo modulation (4 string stems, dB) | – | +2.9 / +7.1 / +6.4 / +8.2 | | [measured] |
| render time | – | 235 s | | [measured] |

[inferred] The rolls and the mid-loud bars should sound calmer, and soft passages in m2 are less buried at normal
playback level, because p10 went from −15.4 to −10.6 LU. I have not checked this by listening.

## 3. What got worse
- **m2 balance spread:** balance inversions 23 → 46, spread vs string median 3.6 → 4.6 dB, stems more than 6 dB off
  0 → 5, Violins I loudest stem 23 → 12 bars. The cause is the melody ducking: in m2 the accompaniment is often the
  first violins, so they get cut under the viola, cello and wind espr. passages. This is intended, but the static
  metric counts it as an inversion.
- **m2 short-term max** +9.7 → +10.6 LU (target < +8). It is the full tutti in bars 79–80, set against a quieter
  integrated level. Limiting it further would push the LRA below 18 (it is already 17.7).
- **m2 LRA 17.7** is just under the 18–20.5 target band.
- **m1 p→mp step** 4.1 → 1.7 dB, from the refitted global curve. The mp→mf and mf→f steps got much wider.
- **m1 melodies ≥ 0 dB vs loudest other stem** 11 → 10 of 20. Many m1 passages have two or more marked melodies
  together (Violins I + II, or clarinets + horns), and two equal lines cannot both be ≥ 0 dB against each other.
  Against the loudest non-melody stem, 19/20 are on top (median +4.4 dB). Critic: please judge item 4 with this
  companion measure too (`meas/scripts/melody_nonmel.py`).
- **Rolls may now be too quiet.** Long rolls sit about 15 dB under the loudest other stem, and up to 23 dB at the end
  of a long roll. Dan asked for rolls under the texture, but this may be more than he wants.
- **Roll stroke autocorrelation** reaches 0.29 in m1 bars 41–43 (target < 0.25).
- **mp3 click candidates** in m1 are unchanged at 43, although the premaster has 0 isolated spikes. So the candidates
  are not loop seams. They may be MP3 pre-echo on attacks or true transients; not investigated.

## 4. Still open
- Winds and brass are still FluidR3 (item 6 rejected on the A/B evidence above), so flute staccato 2.07, detached
  1.53/1.46 and the bass trombone accent −1.9 dB are unchanged. A next step would be VPO for selected staves only, with
  per-layer level correction.
- Section timing (item 8) is not done.
- 63 Hz is still about 5 dB under Brahms 1 in m1. The share below 100 Hz is 0.6–1.2 dB short of the band.
- Concurrent-melody metric: see section 3.
- `tools/score_events.py` should get the same MIDI-grid bar fix as `lib/score_events.py`.
- `artic_channels` code is inactive.

## 5. How to rebuild
```
cd /mnt/project-files/symphony/render
ps aux | grep render.py          # one render at a time
python3 r03/render.py --score /mnt/project-files/symphony/mvt1/v156 --out r03/out-m1.mp3 --work /tmp/render-03-m1 --midi-out r03/r03-m1.midi
python3 r03/render.py --score /mnt/project-files/symphony/mvt2/v30  --out r03/out-m2.mp3 --work /tmp/render-03-m2 --midi-out r03/r03-m2.midi
# measure (tools/ and critic 2's scripts): WORK MP3 OUTDIR LABEL
bash r03/meas/scripts/meas.sh /tmp/render-03-m1 r03/out-m1.mp3 /tmp/meas-m1 r03-m1
```
Options: `--events` reuses an events.tsv (skips the LilyPond compile), `--no-balance` turns off the mix stage for A/B
tests, and `--keep-synth` keeps the stage-1 stem signals. Each render takes about 4–5 minutes with 4 jobs. Stems stay
in `--work` (/tmp).

## 6. Housekeeping
No assets were added (the VPO wind test used a /tmp download only), so assets/README.md is unchanged. Nothing was
written into symphony/mvt1 or symphony/mvt2. My /tmp work folders are deleted.
