# r01: stems, printed articulations, per-stem balance, one hall, linear mastering

Actor 1, 2026-10-09. Built from r00 and critic 0's ranked plan (critics/c00.md, section 6). Score unchanged: everything is read from `mvt1/v120/score.midi` and from a scratch compile of the v120 LilyPond source.

Rebuild: `python3 render.py` (about 4.5 min on 4 CPUs: 37 s LilyPond event log + MIDI processing, 160 s for 23 stems, 70 s mixing, limiting and encoding; `--events <events.tsv>` skips the LilyPond compile). Work files go to `/tmp/render-01/build`.

Files: `render.py` (one command), `articulate.py` (MIDI rules), `stem.py` (per-staff render chain; also the `--render` command for tools/stems.py), `config.json` (all numbers), `lib/` (frozen copies of tools/score_events.py, rtk.py, ly/eventlog.ily), `r01.midi` (the processed MIDI), `out.mp3`, `meas/` (my measurements).

Every number below is **[measured]** with tools/measure.py, compare.py, stems.py unless marked **[inferred]**.

## 1. What changed, by plan item

### 0. Architecture: one stem per staff
- `articulate.py` writes a MIDI with the same tracks, names, onsets and tempo map as v120, with new note lengths, extra channels and controllers. Channels are numbered inside each staff (0 main, 1 tremolo strings, 2 pizzicato, 3 string staccato), so the file is meant to be split per staff; it is not meant to be played as one file.
- `render.py` splits it per staff exactly like tools/stems.py does (track-name prefix), and `stem.py` renders each: FluidSynth 2.3.4 with FluidR3_GM, internal reverb and chorus off (`-R 0 -C 0`), gain 0.2, 48 kHz 32-bit float WAV, polyphony 512 (FluidSynth manual, source 10 of c00). The mix is the sum of the stems. Because stems.py is run with `--render "python3 r01/stem.py {midi} {wav}"`, the stem measurements are the mix's own stems.
- No clipping anywhere before mastering: float output; the summed premaster has a true peak of +3.2 dBTP in float, which the master gain (-2.2 dB) and limiter bring to -1.4 dBTP. 0 samples at full scale in the MP3.

### 1. Articulations (Dan's priority 1), rules in `articulate.py`, values in `config.json/articulation`
Printed marks come from `notes.csv` (tools/score_events.py on v120). MIDI notes are matched to printed notes per track and onset, allowing for the staff's transposition (double basses sound an octave lower; matching only on pitch would miss them): 5101 of the 5121 pitched MIDI notes are matched; the 20 unmatched keep their original length and velocity, and the 2 notes of the untitled channel-10 percussion track are left unchanged.
- Slurred notes (slur start/in, next note contiguous): note-off moved to the next onset + 40 ms (legato by overlap, the method the Virtual Playing Orchestra author recommends for samples without legato transitions, c00 source 6); repeated pitch under a slur ends 30 ms before the next note. 1111 notes.
- Detached unmarked notes: gap of 13 % of the notated length, at least 40 ms, at most 120 ms, never more than 40 % of the note (critic: 85-90 %, gap 60-120 ms). 3034 notes. Slur-end notes: gap 10 %, 30-100 ms. 433 notes.
- Staccato: winds and brass 50 % (max 0.25 s); strings 35 % (max 0.18 s) on a separate channel whose envelope release is shortened by 2400 timecents through the SoundFont 2.01 NRPN (CC99 = 120, CC98 = generator 38 releaseVolEnv, data entry 8192 + value/2). Checked in FluidSynth: release of the string-ensemble sample to -20 dB falls from 0.30 s to 0.08 s. 80 notes. Sources: SoundFont 2.01 spec section 9.6 (NRPN select MSB 120, LSB = generator), https://raw.github.com/bradhowes/SF2Lib/main/SoundFont%20Spec%202.01.pdf and https://polyphone.io/doc/files/sf_specifications_v2.04.pdf ; Polyphone forum on NRPN generator numbering https://www.polyphone.io/en/forum/help/626-nrpn ; timecents = 1200·log2(seconds), https://lists.nongnu.org/archive/html/fluid-dev/2018-06/msg00052.html .
- Violins I and II main channel: release shortened by 1200 timecents (0.30 s to 0.14 s to -20 dB, the same as the cello sample's own 0.17 s), because the long release of GM 48 filled every detached gap.
- Tenuto: full length, +5 velocity. Fermata: full length.
- Accent / marcato (strings, winds, brass) and sf: LilyPond's +20 velocity is kept for the attack; a CC11 dip from 80 ms to 250 ms after the onset brings the sustain back to the unaccented level (dip = level difference of the two velocities, max 6 dB), held until the next onset in the staff. Marcato also 80 % length. fp (1 event, double basses): attack at f velocity, then CC11 down to the p level. 608 accents, 1 sf, 1 fp.
- String tremolo :32 (93 notes, violins and violas): GM 44 (tremolo strings) on channel 1. CC7 trims match its level to the arco program using critic 0's sfcal (program 44 is 0.9 dB quieter than 48 and 3.4 dB quieter than 41 at the same velocity); the renderer adds the trim back as gain (text meta "r01 stem trim").
- Measured tremolo :16 (cellos, 5 notes): repeated 16th notes at 85 % length.
- Pizz. (35 notes: basses 31, cellos 4): GM 45 on channel 2, level matched to arco minus 2 dB (sfcal: 45 is 11.4 dB quieter than 48), note length min(60 %, 0.35 s) because a plucked note only starts its release at note-off.
- Timpani rolls (26): repeated strokes at 14 per second, velocity = the dynamic curve at that moment - 6 ± 6 (seeded random, so the build is reproducible). Rolls under hairpins now crescendo and diminuendo stroke by stroke. 1739 strokes.
- Sul tasto (21 notes): velocity -6.

### 2. Volume of individual tracks (Dan's priority 2)
- Continuous dynamics as CC11 per staff, 20 ms grid (`config.json/dynamics`). A velocity-equivalent dynamic curve V(t) is built from the unaccented notes' velocities (LilyPond already interpolates velocities across hairpins); it is linear between onsets inside hairpins and stepped elsewhere. CC11 = extra dynamic range f(V) + hold term. f(V) is 0 dB at ff and -1.4 (f) ... -4 dB (pp/ppp), multiplied per stem by `dyn_scale` (1.3 strings and winds, 2.0 brass, violas, cellos, contrabassoon, 2.2 basses: these samples change little with velocity). The hold term makes notes held under a hairpin follow V(t) (40·log10(V(t)/V(last onset)), the FluidSynth velocity law): the 242 long notes under hairpins now swell and fade. Calibrated in FluidSynth: CC11 and CC7 attenuation = 40·log10(value/127) dB to within 0.1 dB, and velocity level = 40·log10(vel/127) dB (default SoundFont modulators, concave 960 cB; SF2 spec section 8.4).
- Static stem gains (`config.json/stems.*.gain_dB`) set in two measured steps against these f/ff targets relative to Violins I (my reading of Rimsky-Korsakov's forte ratios as +3 dB per "twice", applied about halfway, c00 source 3): Violins II -0.5, violas -2, cellos -1, basses -2, each woodwind pair -2, bass clarinet and bassoons -3, contrabassoon -5, each horn pair +1.5 (later 0, see below), trumpets 1-2 +3, trumpet 3 +1.5, trombones 1-2 +3, bass trombone +1.5, tuba +1, timpani -2, harp -4. The horn pairs were lowered by 1.5 dB in the second step because they caused most balance inversions.
- Width processing keeps each stem's power (otherwise narrowing the wide-stereo string and wind samples lowered them by up to 3 dB while the mono brass kept their level; measured: Violins I rose 3 dB relative to the trombones when this was fixed).

### 3. Blend (Dan's priority 3)
- One hall for all stems: measured impulse responses of the Detmold Konzerthaus (about 600 seats, RT30 about 1.6 s), Set C "loudspeaker orchestra": 8 loudspeakers at orchestra positions, receiver seat R163, omni and figure-of-eight microphones recorded together. Decoded as mid/side stereo, L = omni + 1.3·fig8, R = omni - 1.3·fig8 (sign checked: the figure-of-eight's positive lobe points left, correlation +0.93 for the left source S1 and -0.94 for the right source S4); mid/side decoding: https://www.soundonsound.com/sound-advice/q-how-does-mid-sides-recording-actually-work . Direct sound removed (the dry stem is the direct sound), 2 ms fade-in 4 ms after it; all sources scaled by one factor (S3's energy gain in 250-2000 Hz = 1), so the measured differences between positions stay. Database: https://zenodo.org/records/4116247 (CC BY 4.0); positions from Sahin, Amengual, Kob, DAGA 2017 (in the zip). Only 16 files (4.5 MB) were fetched, by HTTP range requests on the zip, because the whole 986 MB file downloads at about 50 kB/s from here.
- Each stem uses the loudspeaker nearest its seat: Violins I S1, Violins II S2, violas S3, cellos S4 (front row), basses, trombones, tuba S8, horns S5, woodwinds, trumpets, timpani S6/S7 (second step), harp S1. Sends: strings -7 dB (basses -6), woodwinds -4, brass and timpani -3, harp -5 (front sections drier, back sections wetter; c00 sources 9).
- Pans (constant power, after mid/side narrowing to 0.4-0.6): Violins I -0.75, Violins II -0.4, violas +0.25, cellos +0.55, basses +0.7, harp -0.75, flutes -0.2, clarinets -0.25, bass clarinet -0.35, oboes +0.15, cor anglais +0.3, bassoons +0.1, contrabassoon +0.25, horns -0.55/-0.65, trumpets +0.15/+0.22, trombones +0.4, bass trombone +0.48, tuba +0.55, timpani -0.05. Values were widened in two steps until L/R correlation and pan spread reached the reference range.
- Tone colour with dynamics: per stem, a zero-phase 2nd-order crossover at 2.5 kHz; the band above it gets 0.15 dB per velocity step relative to mf (-6 dB at ppp to +3 dB at fff), following V(t) from CC20 (an undefined controller FluidSynth ignores), smoothed over 50 ms. Not applied to timpani.

### 4. Mastering
Plain gain to -20 LUFS integrated (measured with ffmpeg ebur128 on the premaster), then, only because the true peak after gain would be +1.0 dBTP, a limiter at -1.5 dBFS on a 4x oversampled signal (ffmpeg `alimiter`, attack 5 ms, release 200 ms, https://ffmpeg.org/ffmpeg-filters.html#alimiter), then libmp3lame 256 kb/s. No loudnorm. LRA is the same before and after the limiter (18.8 LU), so the limiter touches only peaks. Why: single-pass loudnorm is dynamic (c00 sources 1, 2).

### 5. Timing variation: not done (lowest rank).

## 2. Before / after [measured]

Mix (`meas/compare_r01_r00_refs.md`, full metrics `meas/r01/metrics.json`):

| | r00 mp3 | r00 before loudnorm | **r01** | Brahms 1 (Musopen) | target (c00) |
|---|---|---|---|---|---|
| integrated (LUFS) | -20.0 | -14.7 | **-20.2** | -20.2 | about -20 |
| LRA (LU) | 12.1 | 19.4 | **18.8** | 18.5 | 17-20 |
| short-term p10 / p95 rel. I | -8.3 / +3.9 | -14.6 / +4.9 | **-16.1 / +2.7** | -15.3 / +3.4 | p10 about -15 |
| pp bars rel. I (median) | -8.0 | -14.9 | **-16.8** | | -13 to -16 |
| p / mf / f / ff bars rel. I | -6.8 / -3.8 / -3.3 / +0.7 | -13.2 / -10.9 / -7.6 / -0.7 | **-15.3 / -11.4 / -7.9 / -2.5** | | |
| Spearman bar loudness vs bar max velocity | 0.78 | 0.85 | **0.84** | | > 0.85 |
| true peak (dBTP) / samples at full scale | -2.3 / 0 | +0.1 / 2743 | **-1.4 / 0** | -2.1 | -1 |
| spectral slope 100 Hz-10 kHz (dB/oct) | -3.24 | -2.71 | **-2.58** | -2.68 | |
| share 2-6 kHz / above 6 kHz (dB) | -12.4 / -33.2 | -11.7 / -31.3 | **-11.8 / -30.4** | -11.5 / -30.8 | |
| loud minus soft, 5 kHz / 10 kHz (dB) | +5.0 / +4.2 | +9.2 / +6.6 | **+13.8 / +6.4** | +10.3 / +10.2 | +6 to +10 |
| L/R correlation overall / above 4 kHz | 0.53 / -0.02 | 0.61 / 0.02 | **0.58 / 0.29** | 0.49 / 0.38 | high band 0.35-0.55 |
| pan spread | 0.27 | 0.25 | **0.32** | 0.34 | 0.32-0.35 |
| cut-off decays: RT60 estimate (n) | 0.9 s (9) | 0.9 s | **1.65 s (6)** | 1.33 s (12) | 1.3-2.0 s |
| general pauses: time to -20 dB (bars 14, 26, 170) | 0.21-0.26 s | | **0.56, 0.44, 0.51 s** | | > 0.4 s |
| onset lag audio after MIDI | 20 ms | 20 ms | **40 ms** | | about 20 ms |

Stems (`meas/stems_r01/stems_summary.json`; r00 values from critics/c00/stems_r00), level at f/ff relative to Violins I (dB):

| stem | r00 | r01 | | stem | r00 | r01 |
|---|---|---|---|---|---|---|
| Violins II | -1.7 | -0.7 | | Horns 1-2 / 3-4 | -4.2 / -3.9 | 0.0 / +0.3 |
| Violas | -8.1 | -2.1 | | Trumpets 1-2 / 3 | -3.4 / -8.6 | +3.2 / +1.0 |
| Cellos | -4.9 | -0.8 | | Trombones 1-2 | +2.8 | +3.3 |
| Basses | -6.6 | -1.7 | | Bass trombone / Tuba | -1.4 / -3.7 | +1.8 / +1.3 |
| Flutes / Oboes / Clarinets | -0.9 / -2.5 / -1.8 | -1.7 / -1.8 / -1.8 | | Timpani | -14.1 | -1.7 |
| Cor anglais / Bass clarinet | -2.6 / -8.2 | -1.7 / -2.7 | | Harp LH | -7.1 | -3.8 |
| Bassoons / Contrabassoon | -7.8 / -13.2 | -1.7 / -4.5 | | | | |

Blend: balance inversions 793 to **688**; trombones 1-2 are no longer louder than trumpets 1-2 (difference 6.2 to 0.1 dB); strings within 2.1 dB of each other at f/ff (target ±3); loudest stem per bar now cellos 35, violas 30, basses 22, horns 17+16, trumpets 13, trombones 12 (r00: trombones 52); loudest-minus-second median 1.7 to 1.2 dB. dB per printed step per stem: 1.2-4.1 (r00 1.3-3.5); brass 2.0-3.5 (r00 1.5-2.5). Target 4-5 not reached.

Articulations per stem (r00 → r01):

| measure | r00 | r01 | target |
|---|---|---|---|
| boundary dip slurred / detached, Violins I | -1.9 / -1.8 | -2.2 / -5.7 | detached ≥ 4 dB deeper |
| same, Violins II / violas / cellos / basses | -1.1/-1.7, -2.8/-2.9, +0.1/-2.2, -1.5/-3.6 | -1.2/-5.3, -0.1/-5.4, +0.2/-7.4, -0.3/-8.1 | |
| same, flutes / oboes / clarinets / bassoons | -7.2/-6.9, -2.9/-2.8, -10.5/-11.3, -4.2/-3.7 | -1.1/-7.4, -1.4/-7.9, -0.5/-8.4, -0.7/-8.0 | |
| same, horns 1-2 / trumpets 1-2 / trombones 1-2 | -3.7/-3.2, -0.7/-0.8, -5.9/-5.3 | -2.1/-5.8, -0.6/-6.2, -1.8/-6.8 | |
| staccato level at 75 % of notated length, Violins I / II | -2.9 / -4.8 dB | -14.0 / -13.6 dB | below -12 |
| staccato, flutes / bassoons / cor anglais | -17.9 / -22.9 / -22.0 | -9.2 / -13.6 / -11.4 | (see section 3) |
| tremolo, violins/violas | one GM 48 note | GM 44 tremolo strings | GM 44 or > 10 peaks/s |
| tremolo :16, cellos: envelope peaks/s | 0 | 8.3 | |
| timpani roll level at 75 % of the roll | -34.1 dB | -1.2 dB | within 6 dB |
| pizz. audible length / ratio to notated, basses (31) | 0.67 s / 1.30 | 0.62 s / 1.17 | < 0.6 s and < 1.0 |
| accent sustain at 75 % (Violins I, horns 1-2, trumpets 1-2) | -1.5, -1.7, -1.4 | -5.0, -5.1, -4.3 | (sustain back to base) |
| accent peak boost, median of stems | 2.3-7.1 | 1.4-7.4 | audible |

## 3. What got worse or is still open
- Wind staccato measures less short than in r00 (flutes -17.9 to -9.2 dB at 75 %), and the pizz. length target is missed by 0.02 s: the measured tails now include the hall's reverberation, which r00 did not have. Detached wind notes measure -0.4 to -1.3 dB at the same point, so staccato is still 8-13 dB shorter than detached. [inferred] A real hall adds the same tail.
- Accent peak boost fell for oboes (3.4 to 1.4 dB), cor anglais (6.3 to 1.9), trombones (4.9 to 2.8) and timpani (3.6 to 2.0). [inferred] The reverb raises the level between notes, and the hold term raises unaccented notes under crescendos. Could be offset by a larger accent velocity in r02.
- Onset lag rose from 20 to 40 ms. [inferred] Reverb smears the spectral-flux onsets the tool uses; note onsets in the MIDI are unchanged.
- High-band L/R correlation 0.29 is below the 0.35-0.55 target (overall 0.58 is slightly above the references' 0.49-0.55). The figure-of-eight gain trades these two: 1.6 gave 0.18 / 0.57, 1.0 gave 0.40 / 0.72.
- dB per printed step per stem is still 1.2-4.1, below the 4-5 target; the per-bar measure is confounded by register and number of notes, and stronger expansion pushed LRA above 21 LU.
- Loud minus soft at 5 kHz (+13.8 dB) now overshoots the reference range a little; 10 kHz (+6.4) is inside it.
- 688 balance inversions remain, mostly horns 3-4 and trombones louder than contrabassoon, bassoons and violas in bars where those are marked one step louder. [inferred] Part of this follows from the forte ratios themselves (a horn pair is meant to outweigh a woodwind pair).
- Not done: Virtual Playing Orchestra articulation samples (would replace length tricks with real staccato, pizz. and tremolo samples), small timing variation (plan item 5), melody-against-accompaniment check in espr./dolce bars (not measured by the tools).
- The Detmold impulse responses are 1.5 s long (energy -80 dB at the end), so nothing is cut off.

## 4. How I measured
```
python3 tools/measure.py r01/out.mp3 --midi r01/r01.midi --out <dir>
python3 tools/compare.py <dir> critics/c00/r00 critics/c00/ref_brahms1_i_musopen ... --md ... --png ...
python3 tools/score_events.py --midi r01/r01.midi --events <events.tsv> --out notes_r01.csv --summary articulation_midi_r01.json
python3 tools/stems.py --midi r01/r01.midi --notes notes_r01.csv --out <dir> --render "python3 r01/stem.py {midi} {wav}"
```
Copies of the results: `meas/r01/` (measure.py), `meas/compare_r01_r00_refs.*`, `meas/stems_r01/`, `meas/articulation_midi_r01.json`, `meas/articulate_report.json` (counts of each rule), `meas/render_report.json` (loudness before and after mastering, render time). Intermediate versions (a-f) were measured the same way in /tmp; the main steps were: IR energy normalised over the whole band made the reverb about 10 dB too strong at mid frequencies (2-6 kHz share -16.4 dB, too dark); normalising over 250-2000 Hz fixed it (-13.4, then -11.8 with the brightness reference at mf).
