# Cycle 25, critic C: blend and space (render c24)

Lens: one room. Reverb, seats and panning, mic positions, tone matching between sample sets (trumpets and cymbals are new in this movement), and the low-end build-up against several reference recordings.

Material: `cycles/c24/render/` (master and 33 stems), `cycles/c24/rendered_build/` (parts.json, mix.json), and `cycles/c20/render/` for one comparison. References: the Dvořák 9/i MP3 decoded to 48 kHz, and the stored metrics of Brahms 1/i (C minor, the same key as this movement) and Brahms 4/i (`symphony/render/critics/c00/ref_*/metrics.json`). I ran `symphony/render/tools/measure.py` on the c24 master and on the Dvořák file so the whole-file numbers compare directly. My analysis used third-octave L/R/cross spectra in 50 ms frames for every stem, power (not mono) levels, and each cycle's own tempo map. The scratch folder has been deleted.

## State through this lens (measured)

- **One hall.** All 33 tracks feed the shared true-stereo hall. Tails after a note end followed by at least 1.8 s of rest, median level re the sustain at +1.0-1.3 s: strings -37 to -40 dB, woodwinds -33 to -38, horns/trumpets/trombones -31.7 to -35. The depth order is right: strings nearest, brass furthest. This is unchanged since c21.
- **Seats hold.** Stem R-L at 250 Hz-4 kHz: Vln I -7.6, Vln II -3.2, violas +1.7, celli +5.5, basses +5.4, horns -2.5..-7.5, trumpets +1.9..+2.8, trombones +5.1..+6.4, tuba +6.5, percussion +0.7..+1.9. Release tails sit within about ±4 dB of the centre.
- **Master image** against the references:

  | | c24 | Dvořák | Brahms 1/i | Brahms 4/i |
  |---|---|---|---|---|
  | Correlation | 0.519 | 0.546 | 0.491 | 0.553 |
  | Below 250 Hz | 0.502 | 0.550 | 0.541 | 0.583 |
  | 250 Hz-4 kHz | 0.529 | 0.561 | 0.473 | 0.539 |
  | Above 4 kHz | 0.540 | 0.525 | 0.384 | 0.480 |
  | Side/mid | -5.0 dB | -5.3 | -4.7 | -5.4 |

- **Brief item 7 passes.** Master autocorrelation at 3.95 s, 100-300 Hz band / centroid:

  | Passage | Band | Centroid |
  |---|---|---|
  | Lento 5-12 | -0.08 | -0.08 |
  | Bars 43-46 | -0.35 | +0.05 |
  | Bars 47-55 | +0.12 | +0.01 |
  | Bars 160-164 | +0.25 | -0.01 |
  | Bars 175-178 | -0.28 | -0.05 |
  | Bars 179-182 | -0.23 | -0.13 |

  Only one non-percussion note is over 6 s: Horn 4's A-flat3 at 289 (7.2 s). It sits 9.9 dB under the master and makes 17% of the 100-300 Hz band. The 7 s window is too short for a reliable autocorrelation (other lags reach ±0.6 on the master), so I propose no change.
- **Brief item 8 passes.** 2-5 kHz from -10 to +80 ms minus +120 to +400 ms, on every printed accent of 0.25 s or more:

  | Family | n | Median | p90 |
  |---|---|---|---|
  | Strings | 186 | -6.0 | -2.2 |
  | Winds | 219 | -7.9 | -2.9 |
  | Brass | 145 | -9.7 | -5.2 |
  | Timpani | 14 | -11.9 | -8.9 |

  The only outlier is Violas 536 at +12.0, the known double stop.
- **Vibrato matches across brass sample sets.** Pitch modulation on held notes (harmonic 2-3 track, drift removed) is under 2 cents SD median on every row: Trumpet Sus Non Vib 0.5-0.6, trumpet Leg Slur 0.3-1.3, Horn 1 0.8/1.3, Trombone 1 0.4/2.0.

## 1. The solo winds and brass change position from note to note, and the low and high harmonics of one note sit in different places (measured; the cause is inferred, with a model that matches the c21 test)

**Where.** Every solo wind and brass track: 1FH, 1TP, 1TB, 1TU and the woodwind KS Masters. It is most exposed in:
- the Lento solos: cor anglais bars 5-10, Horn 1 bars 13-14;
- the second-theme clarinet solo, bars 51-58;
- Horn 1 with the celli, bars 47-50 and 147-150;
- the trumpet themes, bars 69-71 and 167-169.

The string sections do not do this.

**Evidence: per-pitch stem R-L.** Measured on isolated sustains (+0.25 s to the end, no other note of the track sounding, stem within 14 dB of the master), in two bands. A seat is a single place, so both bands should agree, and every pitch should land in the same place.

| Track (width) | Per-pitch SD, 400-1000 Hz | Per-pitch SD, 1.25-4 kHz | Mean R-L, 400-1000 / 1.25-4k | 400-1000 range |
|---|---|---|---|---|
| Horn 1 (0.15) | 3.4 | 0.8 | -4.6 / -7.4 | -11.4..0.0 |
| Horn 3 (0.15) | 2.7 | 1.1 | -4.1 / -5.1 | -9.7..+0.7 |
| Horns a2 (0.3) | 2.0 | 0.9 | -4.8 / -4.9 | -8.9..+0.6 |
| Trumpet 1 (0.3) | 5.1 | 2.1 | +5.0 / +1.0 | -4.6..+12.0 |
| Trumpet 2 (0.3) | 4.6 | 2.3 | +8.6 / +1.3 | -2.8..+13.5 |
| Oboe 1 (0.5) | 4.5 | 2.2 | +6.2 / +3.9 | +2.1..+12.7 |
| Clarinet 1 (0.5) | 3.3 | 1.7 | -2.1 / -3.0 | -10.3..+6.5 |
| Cor anglais (0.3) | 2.7 | 1.6 | +2.6 / +3.4 | +1.0..+8.3 |
| Trombone 1 (0.3) | 1.4 | 1.0 | +6.0 / +4.5 | +4.9..+9.6 |
| Violins I (0.5) | 1.6 | 1.1 | -6.0 / -8.4 | |
| Violoncellos (0.28) | 0.2 | 0.1 | +4.9 / +5.6 | |

**Evidence: note by note in exposed lines** (R-L 400-1000 Hz | 1.25-4 kHz):
- **Cor anglais, bars 5-8:** G4 +2|+4, then A-flat4 +11|+2.
- **Clarinet 1, bars 51-58:**
  - 207 -8|-2, 209 +1|-4, 210 -6|+4, 215 +4|-6, 220 -10|-1, 223 -7|+5, 223.5 -1|-8.
  - Jumps of 6-14 dB between neighbouring notes, in both bands.
- **Trumpet 1, bar 168:** 670 +8|+2 between 669.5 +1|+2 and 671.5 +4|+1.
- **Horn 1, F4 inside one note**, per third-octave from 400 Hz to 4 kHz: -13, -4, -2, -8, -6, -6, -8, -9, -6, -7, -7 dB. The harmonics under 1 kHz move by up to 11 dB from the seat. Above 1.25 kHz the image is stable at -6..-9.

**Cause (inferred, with a model).**
- `build_reaper.py apply_mix` pans each mic channel's left input to seat - width and its right input to seat + width. On a solo patch, the two inputs are a spaced pair recorded on one instrument. They carry the same note with a pitch-dependent phase and level difference.
- At a small width the two inputs land close together and add. Where they arrive in phase, the sum leans to one side; where they arrive in antiphase, it leans to the other. Each harmonic below about 1 kHz therefore gets its own position.
- I modelled this with a sin/cos pan law at seat -0.45 and the two inputs at random relative phase, with a level ratio within ±6 dB. Per-pitch R-L SD:

  | Width | 0.5 | 0.3 | 0.15 | 0.10 | 0.05 | 0.03 | 0 |
  |---|---|---|---|---|---|---|---|
  | SD (dB) | 5.3 | 4.3 | 3.5 | 2.8 | 1.7 | 1.1 | 0 |

- This explains why c21's 0.3 -> 0.15 test changed the horns by under 1 dB: I re-measured c20 against c24 and got Horn 1 SD 3.7 -> 3.4, Horn 2 2.2 -> 2.1, Horn 3 2.7 -> 2.7.
- On the wide wind tracks (0.5), the samples' plain L/R level difference also becomes a position: a 16 dB input imbalance moves the seat by 10 dB at width 0.5, and by 1 dB at 0.05. That is the clarinet's high-band jumping.
- The section patches are many players, so their mic channels are not coherent, and the cello stem is stable to 0.2 dB at width 0.28.
- The hall return is centred and does not carry it: tails are within ±4 dB of the centre while sustains read +12.

**Inferred effect.** On headphones a solo line does not stay in one seat: the clarinet and cor anglais solos step left and right between notes, and a horn or trumpet note sounds split, with its lower harmonics in one place and its upper harmonics in another. A player in a hall is one source in one place, so this is the main thing that still marks the winds and brass as separately recorded samples.

**Fix (Opus state: a full rebuild of the listed tracks).** Test it on the exposed tracks first, together with the horn rebuild that HISTORY has owed since c21. In `build/mix.json`, per-track `width` 0.05, with seats set to keep each track's current 1.25-4 kHz image (tan-law inverse of the measured R-L). Only the seat moves; the measured high-band image stays.

| Track | width | seat |
|---|---|---|
| Horn 1 | 0.15 -> 0.05 | -0.45 -> -0.48 |
| Horn 2 | 0.15 -> 0.05 | -0.40 -> -0.42 |
| Horn 3 | 0.15 -> 0.05 | -0.38 -> -0.38 |
| Horn 4 | 0.15 -> 0.05 | -0.40 -> -0.34 (it measures -0.28 now) |
| Horns a2 (optional, it alternates with Horn 1 in the themes) | 0.3 -> 0.05 | -0.42 -> -0.46 |
| Trumpet 1 | 0.3 -> 0.05 | 0.05 -> 0.07 |
| Cor anglais | 0.3 -> 0.05 | 0.20 -> 0.24 |
| Oboe 1 | 0.5 -> 0.05 | 0.10 -> 0.28 |
| Clarinet 1 | 0.5 -> 0.05 | -0.15 -> -0.22 |

Keep every send, mic level, side_shelf and the hall unchanged.

**Correlation (simulated, inferred).** Narrowing makes the direct sound coherent. I simulated it on the c24 stems by making 25% (horns) to 50% (Oboe 1, Clarinet 1) of each test stem's power coherent:

| Change | Master correlation | 250 Hz-4 kHz | Above 4 kHz |
|---|---|---|---|
| Now | 0.519 | 0.529 | 0.544 |
| The test tracks | 0.536 | 0.550 | 0.554 |
| All solo winds and brass | 0.582 | 0.600 | over the references |

So extend it to the other solo tracks (Flute 1/2, Oboe 2, Clarinet 2, Bass clarinet, bassoons, contrabassoon, Trumpets 2-3, trombones, tuba) only after the test passes. Spread their seats a little to keep the section width, and raise the winds' and brass side_shelf high shelf from +1.5 to about +2.5 dB if 250 Hz-4 kHz goes over 0.56.

**Levels.** Width changes move levels slightly (c21: within 0.3 dB on most horn notes, -1..-2 dB in two spans). After the render:
- compare per-dynamic note medians with c24 and restore them by stem fix (c09 method);
- re-check the accent 2-5 kHz front against the body on the rebuilt tracks.

**Targets.**
- Per-pitch R-L SD at 400-1000 Hz at most 1.5 dB on every test track.
- The 400-1000 Hz and 1.25-4 kHz means within 1.5 dB of each other.
- Neighbouring-note R-L steps at most 3 dB in cor anglais bars 5-8 and Clarinet 1 bars 51-58.
- Master correlation at 250 Hz-4 kHz at most 0.56, and above 4 kHz at most 0.56.
- Note levels within 1 dB of c24 after the stem fix.

## 2. The fff crash at bar 160 is under the tutti's top band by 1.5 s and 11 dB under it by 2 s (measured; simulated fix)

**Where.** Crash cymbals, qn 636, "Crash cym. l.v." fff. It is the movement's single fff and its main climax, and the tutti holds fff largamente for four bars after it.

**Evidence.** Crash stem 4-12.5 kHz minus the rest of the orchestra, 0.2 s windows around each time after the stroke:

| Time after stroke | 0.1 s | 0.5 s | 1.0 s | 1.5 s | 2.0 s | 2.5 s | 3.0 s |
|---|---|---|---|---|---|---|---|
| Crash minus rest (dB) | -4.2 | -0.2 | -4.7 | -6.6 | -10.8 | -14.9 | -21.5 |

- On its own stem the ring decays about 8 dB per second at 5-10 kHz and about 14 dB per second at 10-16 kHz, even with the c05 22in K patch and the current lift (+5 dB at 638.5 to +6 dB at 644).
- The shared hall's 5.5 kHz high cut means the room adds almost nothing above that frequency, so the cymbal's shimmer is its dry ring only.
- The crash makes 27.6% of the master's 10-16 kHz in the loudest frames, so it sets the top of the climax.

**Inferred effect.** The crash marks the downbeat and then disappears into the brass within about a second and a half. An l.v. pair at fff in a hall usually stays audible as a shimmer over the tutti for about 2-3 s.

**Fix (level only; can be simulated and applied by stem fix).** `build/score_config.py` line 374:

```python
LEVEL_SHAPES["Crash cymbals"] = [[(636.0, 0.0), (636.02, -4.0), (636.6, -4.0), (637.2, 0.0), (638.0, 6.0), (638.5, 9.0), (644.0, 10.0)]]
```

That is +2.9 dB at 638.0 and +4 dB from 638.5 over the current shape. The stroke itself, the first 0.6 s and the -4 dB dip that protects the 636.04 master peak are unchanged.

**Simulated on the c24 stems.**

| Time after stroke | 1.0 s | 1.5 s | 2.0 s | 2.5 s |
|---|---|---|---|---|
| Crash minus rest, now (dB) | -4.7 | -6.6 | -10.8 | -14.9 |
| Crash minus rest, with the fix (dB) | -3.1 | -2.7 | -6.8 | -10.9 |

The master total changes by +0.02/+0.05/+0.01 dB over 637-638/638-640/640-644, and the master 5-16 kHz by +0.23/+0.37/+0.02 dB. The limiter and the 636.04 peak should not move.

**Targets.**
- Crash 4-12.5 kHz within 3 dB of the rest at +1.5 s, and within 7 dB at +2.0 s.
- Delivery limiter at most 1.9 dB.
- Climax order 160 > 122 > 167-170 unchanged.

**Alternative (inferred, not measured).** A per-group hall high cut (perc 10-12 kHz) in `build_reaper.py` would add a reverberant shimmer. It needs a perc rebuild and a code change, so try the level shape first.

## Measured, no change proposed

**Low-mid body: do not run c24 C #5 (static 125-170 Hz bells on 12 tracks).** The deficit it targets is in the notes of the climaxes, not in the mix.

- **Long-term third-octaves re total** (125 / 158 Hz):

  | c24 | Brahms 1/i | Brahms 4/i | Dvořák |
  |---|---|---|---|
  | -16.9 / -15.4 | -11.8 / -14.4 | -11.2 / -13.0 | -13.2 / -10.9 |

  At 198-315 Hz the mockup is 2-4 dB over Brahms 1/i. Loud minus soft at 157 Hz is -2.7, against +2.8..+5.2 in the references.
- **The deficit is in the loud frames only.** Re 250-2000 Hz in the loudest 10% of frames, 90-112 / 112-141 / 141-178 Hz is -12.5 / -19.5 / -13.5 dB. In soft frames it is -10.8 / -13.1 / -11.4, and soft frames are +2..+4 dB over Dvořák at 125-200 Hz.
- **The loud frames are mostly two climaxes.** 179 of them fall in bars 158-161 and 313 in bars 116-123. Re 250-2000 Hz, 112-141 Hz there is:
  - -27.4 dB at bars 158-161;
  - -24.0 dB at bars 116-123;
  - -11.5 to -16.9 dB at bars 25-26, 131-142 and 167-170.
- **No note puts a harmonic in that band at the main climax.** Over qn 628-644, no sounding note of any pitched track has harmonics 1-6 in 112-141 Hz, except the harp's low F for 2 beats. The bass is G1/G2 and A-flat1/A-flat2 (49/98/147/196 and 52/104/156/208 Hz). At 464-492 only the bass trombone's C3/D-flat3 (7.4 beats) reaches it.
- A static bell boosts nothing there, which is why c24's simulation gained only about 1 dB long-term, and that came from other passages. The 20-100 Hz share (-15.5 dB) is between Dvořák's lossy -22.1 and the Brahms recordings' -8.9. The Brahms recordings' 62 Hz band (-12.3/-12.7 re total in both) looks like room rumble, so I do not tune to it.

**Hall amount and decay.** Tails, depth order and the bar-170 fermata decay are as c21 measured. The shared hall, fx 0.19, wet 2.0 and the pre-fader sends need no change.

**Trumpet versus trombone brightness (c21 shelves).** At ff, 2-5 kHz minus 0.5-1 kHz:

| Trumpets 1-3 | Trombones 1-2 | Bass trombone |
|---|---|---|
| -2.3 / -4.6 / -5.2 | -6.8 / -2.8 | -5.6 |

Trumpet 1 makes 11.7% of the loud 5-10 kHz and 19.7% of 10-16 kHz, against Trombone 1's 6.6/5.8%. The trumpets now carry the brass top.

The bass trombone, on the tenor 1TB patch, is as bright as Trombone 1 and supplies 6.8% of the loud 2-5 kHz. That is inferred to be a little bright for a bass trombone. It is small, so I propose no change.

**Percussion.** The tam-tam fff stroke at 484 stays 3.6-4.6 dB under the rest at 2-5 kHz for 2 s, and the 86 Hz bell holds. The pp stroke at 696 is 9-20 dB under the rest. The suspended-cymbal roll's 5-16 kHz reaches 10 dB under the rest 1-4 s after 632 and meets the crash.

## Do not touch

- The shared true-stereo hall (IR, fx 0.19, wet 2.0, 5.5 kHz cut, pre-fader sends) and the per-group sends and Close:Main levels.
- The string seats and widths, the perc width 0.7, and the side shelves.
- The brass 4 kHz shelves and the Trumpet 1 climax shelf.
- The basses' 87.3 Hz bell2, the 80 Hz loud shelf and the existing loud bells.
- The tam-tam 86 Hz bell2.
- The re-bow and loop work (item 7) and the accent swells and fits (item 8).
- Climax order 160 > 122 > 167-170.
- Every c24 do-not-touch item in HISTORY.md.
