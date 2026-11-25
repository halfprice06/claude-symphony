# Cycle 21, critic C: blend and space (render c20)

Lens: one room. Reverb, seats and panning, mic positions, tone matching between sample sets (trumpets and cymbals are new in this movement), and low-end build-up against several reference recordings.

Material: `cycles/c20/render/` (master and 33 stems) and `cycles/c20/rendered_build/` (parts.json, mix.json). References: the Dvořák 9/i MP3 (decoded to 48 kHz), and the stored metrics of Brahms 1/i (C minor, the same key as this movement), Brahms 4/i and Dvořák 9/i (`symphony/render/critics/c00/ref_*/metrics.json`). I ran `symphony/render/tools/measure.py` on the c20 master so its numbers compare directly with those stored metrics.

Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c21-C/`:
- `lib.py`: third-octave L/R/cross-spectrum frames, 0.1 s hop, cached per stem;
- `shape.py`, `shape2.py`, `contrib.py`, `ownspec.py`, `loudpass.py`: spectra of loud and soft frames, and each stem's share of the master;
- `tilt.py`, `simbrass.py`: brass brightness, with an EQ simulation;
- `ttspec.py`, `ttbar.py`, `ttabs.py`, `tt3.py`, `simtt.py`, `simtt2.py`: tam-tam and cymbals;
- `seats.py`, `hornseat2.py`, `hornpitch.py`, `pitchpan.py`, `mrl.py`, `simside.py`: seats and correlation;
- `tails.py`, `gp.py`, `octdecay.py`: release tails and decay;
- `loopchk.py`, `loopmaster.py`, `acc25.py`: brief items 7 and 8. These are critic C c20's scripts, run on c20.

Levels are power dB.

## State through this lens (measured)

**The room is consistent.** Every track feeds one true-stereo hall.

Release tails, measured as the stem level 1.0-1.3 s after a note end followed by at least 1.6 s of rest, relative to the sustain:

| Family | Tail level |
|---|---|
| Strings | -35 to -37 dB |
| Woodwinds | -33 to -36 dB (bass clarinet -39) |
| Horns, trumpets, trombones | -31 to -35 dB |

That is the right depth order: brass furthest back, strings nearest.

Decay at the bar-170 fermata, master, time from the release:

| Measure | c20 | Brahms 1/i |
|---|---|---|
| To -20 dB | 0.53 s | 0.485 s (median of 12 cut-offs) |
| To -30 dB | 0.93 s | |
| RT60 estimate | 1.89 s | 1.33 s |

The octave bands 63 Hz to 4 kHz all reach -20 dB within 0.22-0.62 s, so the low end does not build up in the reverb. The final tail is shorter than Brahms 1/i: -20 dB at 1.30 s against 2.42 s.

**The Close:Main mic ratio is close to uniform:**

| Tracks | Close:Main |
|---|---|
| Strings | 0.66 |
| Woodwinds | 0.62 |
| Horns, trumpets | 0.50 |
| Trombones | 0.49 |
| Tuba | 0.45 |
| Timpani | 0.40 |
| Percussion | 0.30 |

Surround is off everywhere. The 1TP KS Master's factory Surround (loaded at 1.0) is unloaded by the trumpet group's `mics`.

**Seats hold.** Stem R-L at 250 Hz-4 kHz:

| Section | R-L |
|---|---|
| Vln I | -7.6 |
| Vln II | -3.2 |
| Violas | +1.9 |
| Celli | +5.5 |
| Basses | +5.7 |
| Trumpets | +2.0..+2.8 |
| Trombones | +5.0..+6.4 |
| Tuba | +6.5 |
| Percussion | +0.7..+1.9 |

The master's R-L by band in loud frames is within 1.5 dB of Dvořák in every band. The exception is the top octave, see finding 1.

Master correlation:

| | c20 | References |
|---|---|---|
| L/R | 0.516 | 0.49-0.55 |
| Below 250 Hz | 0.512 | 0.54-0.58 |
| Above 4 kHz | 0.542 | 0.38-0.53 |

**Brief item 7 (loop pulse) passes.** Autocorrelation at 3.95 s, band / centroid:

| Passage | Band | Centroid |
|---|---|---|
| Lento 5-12 | -0.08 | +0.08 |
| Bars 43-46 | -0.24 | 0.00 |
| Coda 175-178 | -0.07 | +0.04 |
| Tempo I 179-182 | -0.37 | -0.10 |

The final-chord stems are between -0.12 and +0.13. The only notes over 8 s are the tam-tam strokes and Bassoon 2 at 476, all at or under +0.04.

**Brief item 8 (accents) passes.** 2-5 kHz in the first 80 ms minus the body:

| Family | n | Median | p90 |
|---|---|---|---|
| Strings | 171 | -8.7 | -3.9 |
| Winds | 234 | -11.3 | -5.3 |
| Brass | 172 | -10.3 | -5.2 |

The one outlier is Violas 536 at +7.9, the known bar-135 bump, which is masked on the master.

What follows is ranked by how much a listener would gain.

## 1. Trumpets sound duller than the trombones: the trombones supply the brass brilliance, also where the trumpets have the theme (measured; listener effect inferred)

**Where.** Every f-fff brass passage, most of all:
- the climax, bars 158-161 (qn 628-644): Tpt 1-2 carry the theme with oboes, horns 1-2 and violins, while the trombones hold chords;
- bars 116-123 and 131-142.

**Evidence: each stem's own spectrum, 5-10 kHz and 10-16 kHz minus 0.5-2 kHz.**

| Span | Tpt 1 / 2 / 3 | Tbn 1 / Tbn 2 / B.tbn |
|---|---|---|
| Whole movement, 5-10 kHz | -23.1 / -24.5 / -26.1 | -19.6 / -19.0 / -19.7 |
| Whole movement, 10-16 kHz | -50.2 / -51.8 / -53.2 | -41.2 / -45.0 / -44.5 |
| Bars 158-161, 5-10 kHz | -22.4 / -21.2 / -29.8 | -19.0 / -16.6 / -19.6 |
| Bars 116-123, 5-10 kHz | -20.4 / -32.4 / -21.0 | -17.2 / -16.8 / -18.6 |

CC1 is equal or higher on the trumpets:
- bars 131-140: 86 on both families;
- bars 158-162: trumpets 120 / 120 / 114 against trombones 114 / 120 / 120;
- bars 116-123: trumpets 120 against trombones 108-110.

So the difference is in the sample sets.

The mic setup does not explain it. The trumpets have the same Close:Main ratio as the trombones (0.50 against 0.49). Their reverb send is higher (0.65 against 0.45), and their late tail is 1.5-3 dB wetter (above). The hall's 5.5 kHz high cut therefore darkens them a little more.

**Effect on the master: share of master band power in the loudest 10% of frames.**

| | 2-5 kHz | 5-10 kHz | 10-17 kHz |
|---|---|---|---|
| Trombones | 22.8% | 30.8% | 25.2% |
| Trumpets | 12.0% | 7.4% | 6.0% |

At 8-13 kHz, Trombone 1 alone is 18.2%, more than Violins I (12.1%). In bars 116-123 the trombones are 46.5% of the master's 10-17 kHz.

The loud top octave of the master leans right because of this: R-L above 4 kHz is -1.0 dB, against -2.2 in the Dvořák loud frames, where the violins on the left dominate the top.

Two settings add to it:
- The bass trombone plays on the tenor 1TB KS Master. Hollywood Brass has no solo bass trombone patch; the folder list has "2 Trombones and 1 Bass Trombone" and "Low Brass" only. Its top is as bright as Trombone 1's.
- At the climax, Trumpet 1 carries a -14 dB 5 kHz shelf (c17 C #2, `loud_eq` 633.8-640.05). That darkens the theme exactly where it leads.

Inferred result: the brass sound is set by the trombones' edge, and the trumpet theme sounds distant and covered. In a hall, the trumpets carry the brass brilliance.

**Fix (mix only, `build_reaper.py --mix-only` on six tracks).** In `build/mix.json`:
- Trombone 1, Trombone 2 and Bass trombone `eq`: add `{"band": "highshelf", "hz": 4000, "db": -4}`. Each has only a high-pass now, so ReaEQ band 3 is free.
- Trumpet 1, 2 and 3 `eq`: add `{"band": "highshelf", "hz": 4000, "db": 2.5}`.
- Trumpet 1 `loud_eq` (633.8-640.05): highshelf 5000 Hz -14 -> -6.

**Simulated on the c20 stems** (band power with a 2nd-order shelf curve, stems summed by power):

| Window | Change | Master 5-10 kHz | Master 10-17 kHz | Brass shares of 5-10 kHz |
|---|---|---|---|---|
| Loudest 10% of frames | All three changes | -0.48 dB | -0.46 dB | Tbn 30.8% -> 18.7%, Tpt 7.4% -> 12.2% |
| qn 634-640 | All three changes | +0.07 dB | +0.26 dB | Tbn 17.0% -> 9.0%, Tpt 4.8% -> 13.9% |

Per stem at qn 634-640, 5-10 kHz minus 0.5-2 kHz becomes:
- Trumpet 1: -21.9 -> -16.2;
- Trombone 1: -18.3 -> -20.8.

The master's total level changes by less than 0.05 dB everywhere. The shelves are static, so each accent's front-minus-body (brief item 8) does not change.

**Targets.**
- In bars 158-161 and 116-123, each leading trumpet's 5-10 kHz share at or above the trombones'.
- The master's 5-10 and 10-17 kHz within ±0.5 dB of c20 in the loud frames.
- Climax order 160 > 122 > 167-170 unchanged.
- The delivery limiter not higher than now (1.7 dB).

**Alternative**, if a trumpet rebuild is planned anyway: trumpet group Close 0.5 -> 0.8 at the same Main, with send 0.65 -> 0.5. It is a more direct trumpet sound, but it is a full Opus-state rebuild of three tracks plus accent refits, and its brightness gain is not measured.

## 2. The tam-tam's 86 Hz partial is the loudest sound below 95 Hz for five bars of the second climax, and again in the coda: a low F against the G pedal (measured)

**Where.**
- Tam-tam fff, heavy beater, qn 484 (bars 122-126, damped at 504). Under it: the G pedal (basses and contrabassoon G1, bass trombone and timpani G2) and the fff tutti falling to pp at bar 126.
- Tam-tam pp, soft stick, l.v., qn 696 (bars 175-178). Under it: the pp chorale, with basses and celli moving G -> E-flat -> D -> C.

**Evidence: the partial.** A fine FFT of the stem (8-10 s windows) finds its strongest component at 85.9 Hz (fff stroke) and 86.1 Hz (pp stroke). That is F2 about 25 cents flat, a whole tone under the G2 pedal. Its partials at 257-262 Hz are 11-21 dB weaker.

The partial decays slowly: the stem falls 10 dB in 4.1 s after the fff peak and in 9.2 s after the pp peak, while its upper bands die away. By bar 124 the tam-tam is mainly this low tone.

**Evidence: the 71-89 Hz third-octave**, tam-tam against everything else:

| Bars | Tam-tam | Rest of orchestra | Difference |
|---|---|---|---|
| 122-123 | 42.0 | 23.8 | +18 |
| 124-126 | 34.6 | 18.1 | +16.5 |
| 175-176 | 24.8 | 14.2 | +10.6 |

The tam-tam supplies:
- 85-95% of the master's 40-80 Hz in each of bars 122-126 and 82-95% in bars 175-176;
- 94-99% of the master's 80-125 Hz in bars 177-178.

From bar 121 to bar 122 the master's 40-80 Hz rises 13.3 dB, and the orchestra itself contributes only 5 dB of that. Over the loudest 10% of frames, the tam-tam is 25.7% of the master's 63-79 Hz.

The rest of the orchestra is thin in this band partly by design: the basses' 87 Hz -6 dB bell2 (c18) and the 80 Hz loud shelf (c20). The tam-tam fills the gap that EQ opened.

Inferred: heard as a low hum a tone under the bass pedal, standing out as the tutti dies away in bars 124-126 and under the pp coda. A tam-tam should add a wash, not a pitched bass note.

**Fix (mix only).** `build/mix.json`, Tam-tam `eq`: add `{"band": "bell2", "hz": 86, "db": -9, "bw_oct": 0.3}`, keeping the 30 Hz high-pass. Because the EQ is static, it works under `tail_hold: false` and the bar-127 damp.

**Simulated:**

| Bars | Master 71-89 Hz | Master below 112 Hz | Tam-tam stem total | Master total |
|---|---|---|---|---|
| 122-123 | 42.1 -> 33.5 | 50.5 -> 49.9 | -0.3 dB | -0.03 dB |
| 124-126 | 34.7 -> 26.3 | | -1.9 dB | |
| 175-176 | 25.2 -> 18.1 | | -2.5 dB | |
| 177-178 | | | -3.2 dB | |

Every bar's master total stays within 0.2 dB. A high-pass alone does much less (HP 90 Hz: -3.2..-3.8 dB in 40-80 Hz), because the energy is one partial at 86 Hz, not broad rumble.

The pp stroke keeps its 130/261 Hz partials and the rest of its band. Do not raise it back: c01 B #4's complaint was its level above 2 kHz, and that is unchanged.

**Targets.**
- The tam-tam's 71-89 Hz at most +9 dB over the rest in bars 122-126 (now +16..+18), and at most +4 in bars 175-176.
- The bar-122 climax level within 0.2 dB.
- The fff stroke's 0.5-5 kHz bloom unchanged.

## 3. The horns move across the stage from note to note: the solo horn samples carry their own L/R balance per pitch, and Horn 4 sits in the middle (measured)

**Where.** Horns 1-4 on the 1FH KS Master; most audible in exposed lines:
- the second theme, bars 47-52 and 147-152 (Horn 1 with the celli);
- Horn 1 bars 13-14;
- the horn chords at bars 43-44 and in the coda.

**Evidence: stem R-L at 250 Hz-4 kHz per pitch.** Only frames where the stem is within 14 dB of the master are counted, so the direct sound dominates.

The image depends on the pitch, in the same way on every horn track. The horn track seats are within 0.15 of each other (-0.45..-0.30):

| Pitch | R-L, Horns 1 / 2 / 3 / 4 |
|---|---|
| G3 | -4.4 / – / -0.4 / -0.0 |
| C4 | -5.4 / -3.7 / -3.2 / – |
| E-flat4 | -9.2 / -7.4 / -7.0 / – |
| F4 | -10.1 / -11.2 / -10.4 / – |
| G4 | -9.9 / -6.9 / -8.5 / – |
| A-flat4 | -4.0 / -6.9 / -2.6 / – |

Weighted SD of the per-pitch R-L:

| Tracks | SD (dB) |
|---|---|
| Horns 1-3 | 2.8 / 2.9 / 2.3 |
| Trumpet 1 | 2.6 |
| Clarinets | 2.2-2.5 |
| Trombones | 0.9-1.3 |
| Strings | 0.5-1.1 |

Section means: Horns 1-4 at -6.5 / -6.6 / -4.0 / -1.6 dB. Horn 4 plays G3 most of the time (301 frames), so it sits near the centre, 5 dB right of Horns 1-2.

The second-theme phrase C5-B♭4-A♭4-G4-F4 runs -5.0 / -2.8 / -4.0 / -9.9 / -10.1 dB, a 7 dB drift to the left inside one slur.

Cause (inferred): the width 0.3 pans each mic pair's L channel to seat - 0.3 and its R channel to seat + 0.3. Each horn sample's own L/R imbalance then becomes a position offset, up to about 10 dB between neighbouring pitches.

Inferred effect: on headphones the horn section does not sit in one place. Single lines wander, and the fourth horn sounds from the middle of the stage.

**Fix (Opus state, so a full rebuild of the four solo-horn tracks).** `build/mix.json`:
- Horn 1, 2, 3 and 4: add `"width": 0.15` (the group's 0.3 stays for Horns a2, whose per-pitch SD is 1.7).
- Horn 4: `seat` -0.30 -> -0.40, Horn 3 -0.35 -> -0.38, so the section sits between -0.45 and -0.38.

Halving the width should roughly halve the per-pitch offsets. That is inferred: the offsets scale with the pan spread, but the mix of mics inside each sample is not known.

Expect level changes of ±1 dB on imbalanced pitches, from the pan law. Measure the horn note bodies against c20 and fix them with `stem_fix.py`, as for any rebuild. The hall return stays centred at full width, so the horns keep their room.

**Targets.**
- Per-pitch R-L SD at most 1.6 dB on Horns 1-3.
- The Horn 4 mean within 2 dB of Horn 3.
- The second-theme phrase within 4 dB end to end.
- Horn note-body levels within 1 dB of c20 after the stem fix.

Do not use REAPER pan or a side cut for this. Both act after the hall return and around the centre, not around the seat (LEARNINGS 12).

## Measured, no change proposed

**Low end against the references.**
- Sub-bass is in range. In the loudest frames, the master's 63-79 Hz third-octave is now 4-6 dB under the soft frames, as in Brahms 1/i (-4.7 dB at 79 Hz). The basses' 80 Hz loud shelf (c20) did that. Finding 2 takes the loud 79 Hz band down a further 2.7 dB.
- The remaining difference from all three references is the 88-177 Hz body. Loud minus soft at 157 Hz:

  | c20 | Brahms 1/i (same key) | Brahms 4/i | Dvořák |
  |---|---|---|---|
  | -2.8 | +2.8 | +4.2 | +5.2 |

  Measured against Dvořák's loud frames, the 88-177 Hz octave is 2.5-6 dB short in every loud passage.
- The basses, tuba, timpani and celli already supply about 90% of the band. They already carry +4..+6 dB loud bells at 140-160 Hz.
- At the two big climaxes the gap is the 126 Hz band (-22..-25 dB re total), which falls between the harmonics of the G and A-flat pedals. More EQ on those tracks would make the bass boomy without filling it. I would not chase it with EQ.

**Reverb amount.** The c20 C #5 test (`fx_volume` 0.19 -> 0.16) is not needed:
- the fermata reaches -20 dB in 0.53 s against the Brahms 0.485 s median;
- the final tail is shorter than Brahms;
- the low octaves do not ring longer than the mids.

The IR envelope (`irSetup.simpleDecay` / `envelopeMode`, Opus manual pp. 133-134) is the control to try if a shorter tail is ever wanted, not the wet level.

**Low-mid correlation.** At 120-250 Hz the master correlation is 0.46, against Dvořák's 0.55. A side-only 250 Hz -2 dB shelf on celli and basses would raise it to about 0.49 but push 60-120 Hz to 0.73 (more mono than the references). Not worth it now.

**Cymbals.** The 22in K crash (qn 636) makes up 0.5-3 dB less than the master in 5-17 kHz for the first second and falls 20 dB in 3.6 s. The suspended-cymbal swell peaks at -9 dB under the master in 5-17 kHz just before it. Seats are +1.4..+1.9 dB R-L. Their timing and level fit the tutti.

## Do not touch

- The shared true-stereo hall (IR, `fx_volume` 0.19, wet 2.0, 5.5 kHz high cut, pre-fader sends) and the per-group send levels. The depth order is right and the decay is close to the references.
- The Close:Main ratios per group, with Surround unloaded (including the trumpets' factory Surround).
- The string, wind, brass and percussion seats (except Horns 3-4 above), and the c17 percussion width 0.7.
- The basses' 87 Hz bell2, the c20 80 Hz loud shelf, the 140-160 Hz loud bells on the bass instruments, and the coda 66 Hz spec.
- The Horns a2 shelves (c17).
- The re-bow and loop work (item 7 passes) and GENTLE_ACCENT / ACC_ART_LEAD with the accent fits (item 8 passes).
- Climax order 160 > 122 > 167-170.
