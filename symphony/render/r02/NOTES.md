# r02: real string and percussion samples, staccato fix, per-dynamic balance, melodies, timpani rolls

Actor 2, 2026-10-09. Built from r01 and critic 1's ranked plan (critics/c01.md, section 8), plus Dan's two timpani notes
(BRIEF.md, 2026-10-09). The score is unchanged: everything is read from `mvt1/v120/score.midi` and the v120 LilyPond
source (compiled only in a scratch copy, read-only otherwise).

Rebuild: `python3 render.py` (one command; 309 s wall time on 4 CPUs for the final build: 35 s LilyPond event log,
about 200 s for the 23 stems, the rest mixing, limiting and encoding). Work files go to `/tmp/render-02/build`.
`--events <events.tsv>` skips the LilyPond compile.

Files: `render.py` (one command), `articulate.py` (MIDI rules), `perc.py` (percussion events read from the LilyPond
source), `sfzplay.py` (new: a Python SFZ sample player), `stem.py` (per-staff render chain; also the `--render`
command for tools/stems.py), `config.json` (all numbers), `sfz/perc-r02.sfz` (percussion map), `lib/` (frozen copies of
tools/score_events.py, rtk.py, ly/eventlog.ily), `r02.midi` (the processed MIDI), `out.mp3`, `meas/` (my measurements and
the scripts that made them, `meas/scripts/`).

Every number below is **[measured]** with tools/measure.py, compare.py, stems.py, critic 1's melody.py, or the scripts in
`meas/scripts/`, unless marked **[inferred]**. All r01 numbers are critic 1's (critics/c01/) unless stated.

## 1. What changed, by plan item

### Item 1. Staccato double shortening (bug): fixed
- `articulate.py` now takes every length rule from the notated length (`notated_s` in notes.csv), not from the MIDI
  note-off. I checked first that the MIDI length equals the notated length for every articulation except staccato
  (ratio 1.00 for 4,240 unmarked notes, accents, tenuto, fermata and tremolo; 0.50 for all 81 staccato notes).
- Staccato: 45 % of the notated length for winds (minimum 80 ms) and strings (minimum 110 ms), maximum 0.3 s.
  Strings play staccato from real staccato samples (item 3), which are one-shot samples, so the note length only matters
  for the FluidSynth fallback.
- Per-stem staccato level: the string staccato sample sets are trimmed so that a staccato note peaks at the level of a
  short sustained note at the same velocity (calibration in `meas/scripts/cal.py`, then corrected once from the stem
  measurement). Cor anglais staccato gets +8 velocity (its FluidR3 sample measured 2-3 dB low when cut short).
- Minimum gap for detached notes 40 → 30 ms (critic item 7 in section 2).

### Item 2. Volume: balance at every dynamic, melodies on top
- **Headroom (2c).** Every CC11 curve is 6 dB below 127 (config `dynamics.headroom_dB`); `stem.py` gives the 6 dB back as
  stem gain. Held-note crescendos can now rise up to 6 dB above the ff level before CC11 saturates. CC11 time at 127 in
  the final MIDI: 0.02-1.0 s per unit (r01: 11 capped crescendos).
- **Per-stem response by printed dynamic (2a).** New config `stems.<staff>.dyn_corr_dB`: a correction in dB by printed
  dynamic, added to the CC11 curve, and `balance_targets_dB`: the target level of each stem relative to Violins I at
  the same printed dynamic (Violins II -1, violas -2, cellos -1.5, basses -2.5, woodwind pairs -2.5, bass clarinet -3.5,
  bassoons -3, contrabassoon -5, horns 1-2 -1, horns 3-4 -1.5, trumpets 1-2 +1, trumpet 3 -0.5, trombones 1-2 +1, bass
  trombone 0, tuba -1, timpani -4). The gains and corrections were fitted from four measured stem renders (rounds a-e
  in `meas/scripts/calib.py` and `calib_lin.py`). The final fit is a straight line per stem in printed-dynamic steps
  (at most 2 dB per step), because per-step corrections from the first rounds produced zig-zag curves (for example an
  oboe mf 9 dB below its mp) that would contradict the printed dynamics; I discarded them.
  Result: the stems that were 4-10 dB too loud at p/pp in r01 (violas, cellos, basses, horns, contrabassoon, bass
  clarinet, tuba) now get 5-12 dB less at pp than at ff, relative to the violins.
- **Global dynamic curve.** CC11 extra by printed dynamic: ppp/pp -5.8, p -5.4, mp -4.8, mf -3.4, f -2.6, ff -1.8,
  fff -2.2 dB (plus the 6 dB headroom), on top of the velocity's own 40·log10 law. Printed fff notes are played 22
  velocity steps lower (127 → 105, critic item 6).
- **Melodies (2b).** Config `melodies`: the 20 espr. / dolce / molto cantabile passages critic 1 lists (same phrase rule
  as `melody.py`: from the start bar while the staff plays, at most 8 bars) get a CC11 lift with 0.3 s ramps. Each
  lift was adjusted from the measured melody margin over three rounds (rate 0.6-0.8 per round): final lifts 1-10 dB
  (Violins I bar 55: 7 dB, Violins II bar 55: 10 dB, clarinets bar 56: 10 dB, cor anglais bar 5: 1 dB).
- **CC11 per voice (critic item 7).** Woodwind and brass staves get one dynamics curve and one MIDI channel per voice
  track (LilyPond writes one, two, shared and solo tracks), so an accent dip or a hold reset in one voice no longer moves
  another voice's held note. Strings, timpani and harp keep one curve per staff.
- **Stronger accents (critic item 7).** +8 velocity on accented notes for oboes, cor anglais, trumpets 1-2, trombones,
  timpani, Violins I and II and cellos; strings also play accents from the VPO accent sample set (item 3).

### Item 3. Real articulation samples for the strings (Virtual Playing Orchestra 3), played by my own SFZ player
- **No new software.** sfizz (critic 1's suggestion) is a software package, which the BRIEF's software rule forbids.
  I wrote `sfzplay.py` instead: it reads the SFZ files and WAV samples (including loop points from the WAV `smpl`
  chunk) and implements the opcodes these files use: key/velocity mapping, velocity and key crossfades (power curve),
  round robin (seq_length / seq_position), tune / transpose / pitch_keycenter, volume, amp_veltrack (amplitude
  (vel/127)², the same 40·log10 law as FluidSynth), amp/pitch/delay randomisation, delay and offset, DAHDSR envelope with
  vel2* modifiers, loop modes (no_loop, one_shot, loop_continuous) with an added loop crossfade, the eq1-3 peaking
  filters and the low-pass filter, group/off_by choke; 4-point Hermite resampling. Opcode semantics from
  https://sfzformat.com/ (e.g. https://sfzformat.com/opcodes/amp_veltrack , https://sfzformat.com/opcodes/loop_mode ,
  https://sfzformat.com/opcodes/xfin_lovel , https://sfzformat.com/opcodes/seq_position ,
  https://sfzformat.com/opcodes/loop_crossfade , https://sfzformat.com/opcodes/offset ); peaking filter from the
  Audio EQ Cookbook https://www.w3.org/TR/audio-eq-cookbook/ .
- **Check against sfizz** (critic 1's renders in /tmp/rcritic-01/vpotest, same notes): the velocity curve agrees within
  1.5 dB from velocity 32 to 127 (the difference is amp_random); the envelope shapes of sustain, staccato and tremolo
  notes agree to 1 dB over the first 2 s. The absolute level of the stereo SSO samples is 9-11 dB higher than sfizz's
  (mono samples 1.6 dB); this does not matter here because every articulation set is calibrated by measurement.
  Release tails decay slower than sfizz's (my release reaches -60 dB at the release time), so I set releases
  explicitly per channel.
- **Mapping.** Each string staff is rendered per MIDI channel from its own SFZ file: 0 detached notes and 5 slurred
  notes from `*-SEC-sustain.sfz`, 4 accents from `*-SEC-accent.sfz`, 3 staccato from `*-SEC-staccato.sfz`, 2 pizz. from
  `*-SEC-pizzicato.sfz`, 1 tremolo from `*-SEC-tremolo.sfz` (1st violins, 2nd violins, violas, cellos, basses: all
  section samples, so the solo viola/cello/bass presets of r01 are gone). CC11 of each channel is applied as gain.
- **Slow attacks of the SSO violin samples.** The sustain samples need 150-390 ms to reach -6 dB of their steady
  level (measured, `meas/scripts/cal.py` notes). Short notes therefore start later in the sample (offset to the point
  where the sample reaches -4 dB of steady level for notes < 0.35 s, -8 dB below 0.8 s, -14 dB for longer notes;
  attack 15-80 ms; slurred notes -6/-10/-16 dB and 30-150 ms), the sample-start technique of the SFZ `offset` opcode.
  Releases: detached 0.2-0.45 s, slurred 0.35-0.7 s.
- **Tone.** The VPO violin samples are close-microphone recordings: notes above G5 have 13-19 dB more energy above
  6 kHz (share of total) than the lower notes, and the first mix (round a) had a >6 kHz share of -24 dB against
  -30.8 dB in Brahms 1. A static high shelf at 4.5 kHz on the string stems (Violins I -7 dB, Violins II -4, violas -5,
  cellos -3) brings the mix to -32.9 dB (Brahms 1 -30.8, Brahms 4 -32.0). [inferred] At 20 m in a hall the direct sound
  also loses some top: air absorption is about 10 dB per 100 m at 8 kHz
  (https://sengpielaudio.com/calculator-air.htm ; https://dsprelated.com/freebooks/pasp/Air_Absorption.html).
- Woodwinds, brass and harp stay on FluidR3 (FluidSynth); I did not test VPO for them this cycle.

### Item 4. Missing percussion: rendered
- `perc.py` reads the DrumStaff part directly from the LilyPond source (`parts.ily` lists the section variables and
  bar counts; each `*Perc = \drummode {...}` gives the events) and finds: tam-tam fff bar 122, suspended cymbal roll pp
  with crescendo bar 159, crash cymbal fff bar 160, tam-tam pp bar 175 (the same four events critic 1 found).
  The drum track of the rendering MIDI is rewritten with these four notes (l.v. held 30 s).
- Samples (`sfz/perc-r02.sfz`, from VPO / VSCO 2 CE, CC0): tam-tam = VSCO 2 CE gong (27-31 s decay, two dynamic layers
  with velocity crossfade; the SSO tam-tam samples in VPO are cut after 2.8-3.8 s); cymbal roll = VSCO 2 CE suspended
  cymbal crescendo sample whose peak time (1.52 s) is nearest the printed one-bar roll (1.9 s), so the roll swells into
  the crash; crash = VSCO 2 CE crash ff layer.
- Measured in the final stems (K-weighted level per bar, drums against the sum of all other stems): bar 122 (tam-tam
  fff) -11.1 dB, bar 123 -23.2 dB, bar 124 -26.2 dB (decay audible through bar 124, about 6 s); bar 159 (roll) -10.7 dB;
  bar 160 (crash) -14.3 dB; bar 175 (tam-tam pp, quiet coda) -7.1 dB, bar 176 -17.2 dB. In round a, with the stem gain
  at 0 dB, the drums stem was the loudest stem of the movement and pushed the bar-122 short-term level to +10.5 LU;
  the gain is now -17 dB.

### Item 5. Blend: woodwind send and string width
- Woodwind reverb send -4 → -7 dB (same as strings). String width 0.6 → 0.35.
- Result: high-band L/R correlation 0.29 → 0.58 (target 0.35-0.55: now slightly above), Violins I stem correlation
  -0.02 → 0.41 (target > 0.3), overall correlation 0.58 → 0.61 (Brahms 1 0.49). Woodwind detached audible ratio:
  flutes 1.61 → 1.53, oboes 1.72 → 1.62 (target < 1.3: not met); flute staccato level at 75 % -9.2 → -9.3 dB (target
  below -15: not met). [inferred] The send change made little difference to these two measures; the remaining length
  probably comes from the FluidR3 wind release, not from the room.

### Item 6. Dynamic distribution of the mix
- fff velocity 127 → 105 and the CC11 headroom: short-term max +10.4 → **+6.7 LU**, p99 +9.9 → **+5.9 LU** relative
  to the integrated level (targets < 8 and < 7; references +6.1/+7.6 and +4.7/+6.1). Met.
- Median bar loudness by loudest printed dynamic, relative to I (r01 → r02): pp -16.8 → -16.8, p -15.3 → -13.4, mp
  -12.8 → -10.3, mf -11.4 → -8.5, f -7.9 → -4.6, ff -2.5 → +0.3, fff +0.3 → +1.5. Steps pp→p 3.4, p→mp 3.1, mp→mf 1.8,
  mf→f 3.9, f→ff 4.9 dB (r01 1.5, 2.5, 1.4, 3.5, 5.4). Two of the three soft steps now reach 2.5 dB; mp→mf does not.
- **LRA got worse: 18.8 → 21.3 LU** (target 17-20; Brahms 1 18.5). Short-term p10 / p95 relative to I: -17.2 / +4.2
  (r01 -16.1 / +2.7). The body of the music (p25-p95) moved up relative to the integrated level while the soft end
  stayed. Compressing the global CC11 curve between rounds e and f (pp -6.6 → -5.8, ff -1.6 → -1.8) did not change LRA
  (21.3 both). [inferred] The per-stem corrections that lower the low strings, horns and low winds at p/pp (5-12 dB)
  and the melody lifts widen the range more than the global curve narrows it.

### Item 7. Accents and CC11 per voice
- CC11 steps of 3 dB or more inside one 20 ms step while a note of the same channel is held: **51 → 10** (flutes 5,
  oboes 2, clarinets 2, Violins II 1; critic 1's ccjumps logic per channel, `meas/ccjumps.txt`). The 10 left are chords
  inside one voice track.
- Accent peak boost (wet, r01 → r02): Violins I 2.7 → 6.5, Violins II 2.8 → 7.2, violas 3.6 → 7.0, cellos 2.7 → 7.5,
  basses 4.6 → 6.3 (VPO accent samples); oboes 1.4 → 2.4, cor anglais 1.9 → 3.6 (n = 2), trombones 2.8 → 3.2, timpani
  2.0 → 7.6; trumpets 1-2 3.2 → 3.1; bass trombone 4.1 → 2.3 (worse; not investigated). Target ≥ 3 dB: met except
  oboes and bass trombone.

### Item 8. Brightness filter
- 0.15 → 0.10 dB per velocity step, and (new option `brightness.preserve_level`) the stem's broadband level is restored
  after the filter in 0.4 s windows (at most +3 dB), so the filter changes tone colour, not level, and no longer lowers
  bright stems more than dark ones at pp. Loud-minus-soft spectrum: 5 kHz +13.8 → **+8.9 dB**, 10 kHz +6.4 → **+7.8 dB**
  (target +6 to +10; Brahms 1 +10.3/+10.2, Brahms 4 +6.5/+5.9). Met.

### Item 9. Timing variation: not done.

### Timpani rolls (Dan, 2026-10-09)
- **Real roll samples.** Rolls are no longer strokes: each printed roll is one note played from VPO
  `Percussion/timpani-roll.sfz` (recorded rolls, 11 pitches, about 4 s loops), looped with a 150 ms equal-power
  crossfade at the loop seam (new `loop_crossfade` support in sfzplay.py). Single strokes use VPO `timpani-hit.sfz`
  (No Budget Orchestra samples). A soft stroke (roll velocity - 14) marks the start of every roll, because "a roll
  should start with an attack – a note played slightly louder than the following notes"
  (https://theinstrumentalist.com/march-2009/percussion-rolls/). Measured on a 10 s test roll at velocity 74: the 100 ms
  level varies within ±2.5 dB over 10 s with no level step at the loop seams; the roll body sits 4-5 dB below the peak
  of a single stroke at the same velocity.
- **Fade rule.** In the CC11 curve every roll without a printed crescendo settles from its printed level by -6 dB with a
  1 s time constant; rolls longer than 2.5 s sink a further -4 dB over their first 2.5 s. A printed crescendo hairpin
  (notes.csv `hairpin = cresc`) disables the settling and the roll follows the hairpin. Roll channel trim -8 dB under
  the strokes.
- **Measured (`meas/timproll.md`, K-weighted level per bar of each stem, every roll longer than one bar):**

| roll bars | printed dyn | length s | timpani minus loudest other stem (median, max) dB | bars where timpani is loudest |
|---|---|---|---|---|
| 1-4 | ppp | 19.2 | -6.5, +4.8 | 1 of 4 |
| 13-14 | p | 8.4 | -7.0, -3.2 | 0 of 2 |
| 41-43 | ff | 5.7 | -6.9, -5.6 | 0 of 3 |
| 117-121 | ff | 9.7 | -7.5, -3.4 | 0 of 5 |
| 122-130 | fff | 19.5 | -3.1, -2.7 | 0 of 9 |
| 144-146 | mp | 4.9 | +1.8, +2.6 | 2 of 3 |
| 167-169 | f | 5.7 | -10.1, -9.6 | 0 of 3 |
| 181-182 | ppp | 12.8 | -2.0, -1.9 | 0 of 2 |

  Timpani are the loudest stem in **3 of 31** roll bars (r01 with the same measure on round-a stems, before the fade
  rule and with the r01-style stroke rolls: 16 of 31 after a first gain correction; in r01 itself the stroke rolls stood
  10-33 dB above every other stem in round a's uncorrected gain, so r01's own value is not comparable). The three bars:
  bar 1 (opening, ppp, the roll enters before the strings) and bars 144-145 (mp roll under a thin texture, 1.8-2.6 dB
  over the violas). Neither place marks the timpani as the leading part; the bar-144 roll is still slightly too loud.

## 2. Before / after [measured]

Mix (`meas/compare_r02_r01_r00_refs.md`, full metrics `meas/r02/metrics.json`):

| | r00 | r01 | **r02** | Brahms 1 | Brahms 4 | target (c01) |
|---|---|---|---|---|---|---|
| integrated (LUFS) / true peak (dBTP) | -20.0 / -2.3 | -20.2 / -1.4 | **-20.0 / -1.5** | -20.2 / -2.1 | -16.2 / -1.0 | -20 / -1 |
| LRA (LU) | 12.1 | 18.8 | **21.3** | 18.5 | 13.4 | 17-20 (**not met**) |
| short-term p10 / p95 / p99 / max rel. I | -8.3 / 3.9 / 4.3 / 5.0 | -16.1 / 2.7 / 9.9 / 10.4 | **-17.2 / 4.2 / 5.9 / 6.7** | -15.3 / 3.4 / 4.7 / 6.1 | -9.5 / 3.9 / 6.1 / 7.6 | max < 8, p99 < 7 (met) |
| Spearman bar loudness vs bar max velocity | 0.78 | 0.84 | **0.75** | | | > 0.85 (**worse**) |
| spectral slope (dB/oct) / centroid (Hz) | -3.24 / 665 | -2.58 / 569 | **-2.96 / 691** | -2.68 / 710 | -2.93 / 693 | |
| share 2-6 kHz / > 6 kHz (dB) | -12.4 / -33.2 | -11.8 / -30.4 | **-11.3 / -32.9** | -11.5 / -30.8 | -11.7 / -32.0 | |
| loud minus soft 5 / 10 kHz (dB) | +5.0 / +4.2 | +13.8 / +6.4 | **+8.9 / +7.8** | +10.3 / +10.2 | +6.5 / +5.9 | +6 to +10 (met) |
| L/R correlation overall / > 4 kHz | 0.53 / -0.02 | 0.58 / 0.29 | **0.61 / 0.58** | 0.49 / 0.38 | 0.55 / 0.48 | high 0.35-0.55 (slightly above) |
| pan spread | 0.27 | 0.32 | **0.32** | 0.34 | 0.32 | 0.32-0.35 |
| cut-offs: time to -20 dB / RT60 est. | 0.47 / 0.9 s | 0.51 / 1.65 s | **0.51 / 1.47 s** | 0.49 / 1.33 s | | 0.45-0.55 s |
| onset lag audio after MIDI | 20 ms | 40 ms | **50 ms** | | | 20-40 ms |

Articulations (priority 1):

| measure | r01 | **r02** | target |
|---|---|---|---|
| staccato sounding / notated length (notes.csv) | strings 0.18, winds 0.25 | **0.46 / 0.45** | 0.4-0.5 (met) |
| staccato peak minus unmarked notes, same dynamic, ±2 bars (wet; `meas/staccpeak.txt`) | Vln I -6.3, Vln II -3.7, Vla -4.4, Vc -5.3 (critic, dry) | **Vln I -0.2, Vln II -0.2, Vla +0.3, Vc +1.1; winds -1.5 to +0.9** | ±1.5 dB (met) |
| string staccato level at 75 % (wet) | -13.6 to -16.5 | **Vln I -4.5, Vln II -5.5, Vla -6.2, Vc -5.0** | below -12 (**not met**) |
| tremolo :32 envelope energy 8-24 Hz minus 1-6 Hz (`meas/tremmod.txt`; r01 measured by me on r01's own stems) | Vln I +1.8, Vln II -3.1, Vla -10.1 | **Vln I +4.3, Vln II +3.1, Vla -3.0** (sustained notes +0.2, -5.5, -5.5) | ≥ 3 dB (met for violins, not violas) |
| pizz. audible length / ratio, basses (31) | 0.62 s / 1.17 | **0.61 s / 1.15** | < 0.6 s / < 1.0 (not met) |
| boundary dip slurred / detached, strings | Vln I -2.2/-5.7, Vla -0.1/-5.4, Vc +0.2/-7.4, Cb -0.3/-8.1 | **Vln I -1.1/-5.8, Vla -1.9/-6.3, Vc -0.7/-7.4, Cb -0.1/-4.6** | detached ≥ 4 dB deeper (met) |
| accent boost | see item 7 | | |

About the string staccato level at 75 %: the VPO staccato samples are recorded short notes with their own room and
decay (0.4-0.6 s to -40 dB) and are one-shot; at 75 % of a 0.24 s quaver they are 4-6 dB below their peak, against
13-16 dB for r01's release-cut GM notes. [inferred] The r01 value came from cutting the note before the sample's attack
had finished (which is why its peaks were 4-6 dB low); the VPO value is the length of a real staccato in a recording.
I report it as not met against critic 1's target and leave the target for critic 2 to judge.

Volume of individual tracks (priority 2), `meas/stems_report.txt`:

| | r01 | **r02** | target |
|---|---|---|---|
| spread of (stem minus Violins I) pp..ff, median over stems | 5.6 dB | **7.7 dB** | < 4 (**worse**) |
| same: violas / cellos / basses / horns 3-4 / tuba / contrabassoon | 11.0 / 9.8 / 12.3 / 10.0 / 12.1 / 8.3 | **7.0 / 9.2 / 7.0 / 8.5 / 8.5 / 4.9** | < 6 |
| same: horns 1-2 / trumpets 1-2 / trombones / flutes / oboes | 5.6 / 5.5 / 6.0 / 3.4 / 4.7 | **12.2 / 10.6 / 9.8 / 8.3 / 7.8** | < 6 (worse) |
| balance inversions | 688 | **531** | < 500 |
| Violins I loudest stem (bars) | 6 | **13** | ≥ 25 |
| loudest stem counts | cellos 35, violas 30, basses 22 | cellos 26, horns 1-2 24, violas 21, Vln II 14, tpts 13, Vln I 13 | |
| marked melodies at ≥ 0 dB against the loudest other stem (`meas/melody.md`) | 0 of 20 (16 below 0) | **12 of 20** (8 below 0: 6 of them within -1 dB; clarinets bar 56 -3.8, cellos bar 146 -2.5) | 20 of 20 |
| marked melodies at ≥ -6 dB against the sum of the others | (Vln I bar 55: -11.7) | **18 of 20** (clarinets bar 56 -9.8, bass clarinet bar 107 -7.1) | 20 of 20 |
| Violins I molto cantabile bar 55, vs loudest / vs all | -7.5 / -11.7 | **-0.1 / -4.1** | |
| dB per printed step per stem | 1.2-4.1 (Vln I 3.76) | **1.2-4.3 (Vln I 2.73)** | 4-5 (not met) |

[inferred] Why the median spread went up although the lower strings, tuba, contrabassoon and horns 3-4 came down:
the spread is measured against Violins I, and Violins I now carry a 7 dB melody lift in bars 55-62 (printed p), so
Violins I's "p" level rose and every other stem's "p" column fell (the p column is the outlier in almost every row:
trombones -7.3, bassoons -8.8, horns 1-2 -5.0). The stems that were calibrated with a straight line cannot follow a
single-column dip. A measure that leaves out the melody-lift bars, or uses the median of the strings instead of
Violins I as reference, would separate the two effects; I did not have time to add it.

## 3. What got worse or is still open
- LRA 21.3 LU (r01 18.8, target 17-20) and Spearman 0.75 (r01 0.84). See item 6.
- Median per-dynamic spread 7.7 dB (r01 5.6), mostly the p column (see above).
- Bass trombone accent boost 4.1 → 2.3 dB; oboe accent boost 2.4 dB (< 3).
- Woodwind short notes still long in the room (flute staccato -9.3 dB at 75 %, detached ratios 1.5-1.6).
- Viola tremolo: the VPO viola tremolo samples measure -3.0 dB (8-24 vs 1-6 Hz), below the 3 dB target (critic 1 had
  found the same). Not replaced.
- Onset lag 50 ms (r01 40). [inferred] VPO adds 0-12 ms random delay per note (`delay_random`) and the sustain samples
  start softly.
- Crash cymbal at bar 160 sits 14 dB under the tutti; it may be too soft for fff. Not tuned.
- Not done: VPO for woodwinds and brass, timing variation (item 9), early-reflection-only send for woodwinds.

## 4. How I measured
```
python3 lib/score_events.py --midi r02.midi --events <events.tsv> --out notes.csv --summary articulation_midi.json
python3 tools/measure.py r02/out.mp3 --midi r02/r02.midi --out meas/r02
python3 tools/stems.py --midi r02/r02.midi --notes notes.csv --out <dir> --render "python3 r02/stem.py {midi} {wav}"
python3 critics/c01/scripts/melody.py <dir>/stem_bars.csv notes.csv
python3 meas/scripts/staccpeak.py notes.csv <stem wavs>    # staccato peak vs unmarked notes
python3 meas/scripts/tremmod.py notes.csv <stem wavs>      # tremolo envelope modulation
python3 meas/scripts/timproll.py notes.csv r02.midi <stem wavs>   # timpani in every roll > 1 bar
python3 meas/scripts/ccjumps2.py r02.midi                  # critic 1's ccjumps, per channel
python3 tools/compare.py meas/r02 critics/c01/r01 critics/c00/r00 critics/c00/ref_brahms1_i_musopen critics/c00/ref_brahms4_i_musopen --md ... --png ...
```
`meas/scripts/meas.sh` runs the first four. The stem WAVs are those `render.py` writes to `/tmp/render-02/build/stems`
(the same chain as stems.py's). Six full builds were measured (rounds a-f in /tmp/render-02/meas; f is out.mp3).
Round b's timpani stem is invalid (the config changed while it rendered); I did not use its timpani numbers.

## 5. Housekeeping
- Assets: `assets/vpo3/` (248 MB: the string SFZ files and samples, timpani roll and hit, gong, cymbal samples, licence);
  source URL and licence in `assets/README.md`.
- To free space in /tmp (3.4 GB free at the start), I deleted actor 1's build caches `/tmp/render-01/build`,
  `/tmp/render-01/build_final` and three test WAVs (8.3 GB; all rebuildable with `r01/render.py`). Nothing under
  /mnt/project-files was deleted.
