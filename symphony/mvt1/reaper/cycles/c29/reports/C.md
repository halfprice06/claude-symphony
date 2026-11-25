# Cycle 29, critic C: blend and space (render c28)

Lens: one room. Reverb, seating and panning, mic positions, tone matching between sample sets (trumpets and cymbals are new in this movement), and the low-end build-up against several reference recordings.

## Method

- **Material.** The stem-fixed c28 render (`cycles/c28/render/`, master and 33 stems) and `cycles/c28/rendered_build/parts.json` (tempo map, notes, CC lanes, dynamic curves), plus `build/mix.json`.
- **References.** The Dvořák 9/i MP3, decoded to 48 kHz. Also the stored Brahms 1/i and 4/i metrics (`symphony/render/critics/c00/ref_brahms*_i_musopen/metrics.json`). Brahms 1/i is in C minor, the same key as this movement.
- **Base data.** Every stem and both masters cut into third-octave bands (25 Hz to 16 kHz), 4096-point frames, 25 ms hop. For each band I kept L power, R power and the real L·R cross-spectrum.
- **What I computed from it:**
  - band correlations (sum of the cross-spectrum over sqrt(L·R));
  - R-L seats;
  - loud frames (top 10% of 0.4 s blocks) and soft frames (bottom 30%);
  - stem shares of the master;
  - tails after notes that are followed by at least 1.8 s of rest.
- **Exact simulations.** For side-channel EQ I worked on the whole file in the frequency domain: master minus stem plus the re-filtered stem, using the RBJ biquad's complex response on the stem's side channel only. That is the filter `side_shelf` builds.
- **Other tools.**
  - The c25 actor's `stereo.py` and `loopscan.py`, run on c28, for per-pitch seats and the loop scan.
  - My own accent front measure: 2-5 kHz over -10..+80 ms against +120..+400 ms, with the broadband ratio subtracted.
  - Per-note harmonic profiles for the brass.
- **Score.** Pages 16-17 read (bars 158-170).
- **Scratch.** The scratch folder is deleted (BRIEF rule). Every window is stated below so the actor can repeat it.

## State through this lens

- **Depth order holds (measured).** The median stem tail at +0.6 s after a release, re the sustain:

  | Strings | Woodwinds | Brass |
  |---|---|---|
  | -24.4 dB | -21.7 dB | -19.8 dB |

  - Strings are nearest and brass furthest. The trumpets (send 0.65) sit with the trombones and horns: -17.4..-19.7 dB at +0.6 s and -28.3..-28.8 at +1.0 s.
  - The one sharp tutti cut-off the `rtk.cutoff_decays` rule finds (qn 380) falls 20 dB in 0.55 s. Brahms 1/i's median is 0.485 s.
- **Master image.**

  | | c28 | Dvořák | Brahms 1/i | Brahms 4/i |
  |---|---|---|---|---|
  | Correlation, all | 0.531 | 0.546 | 0.491 | 0.553 |
  | 250 Hz-4 kHz | 0.549 | 0.559 | 0.473 | 0.539 |
  | Above 4 kHz | 0.552 | 0.519 | 0.384 | 0.480 |
  | Side/mid | -5.1 dB | -5.3 dB | | |

  The exception is the band just above the deep bass (finding 2).
- **Seats (measured R-L, 1-4 kHz).**
  - Strings: Vln I -7.9, Vln II -3.3, violas +1.4, celli +5.3, basses +7.7.
  - Horns: -3.7..-7.1.
  - Trumpets: +1.3..+2.6.
  - Trombones and tuba: +4.6..+7.2.
  - Percussion: +1.2..+2.1.
  - Timpani: +0.5.
- **Trumpet timbre follows dynamics (measured).** The cause I checked first does not apply: the trumpets and trombones get identical CC1 at each dynamic (28 at pp, 108 at ff), and the 1TP layers darken properly. Trumpet 1, harmonics 5-8 against the fundamental:

  | Dynamic | H5 | H6 | H7 | H8 |
  |---|---|---|---|---|
  | pp | -18 | -27 | -35 | -37 |
  | f | -11 | -15 | -23 | -23 |
  | fff | -7 | -11 | -12 | -16 |

  The trombones span a similar range (H6 -22 at pp, +1 at fff).
- **Percussion (measured).** Each stroke's 4-12.5 kHz minus the rest of the orchestra, in 0.2 s windows. Both strokes stay within c25's targets.

  | After the stroke | +0.5 s | +1.0 s | +1.5 s | +2.0 s | +2.5 s | +3.0 s |
  |---|---|---|---|---|---|---|
  | Crash, qn 636 | +0.2 | -2.5 | -1.9 | -5.7 | -9.2 | -15.4 |
  | Tam-tam, qn 484 | +1.0 | +0.4 | -3.4 | -3.9 | -9.4 | |

  The suspended-cymbal roll peaks at -0.4 dB re the rest at the crash.
- **BRIEF item 7 passes (measured).** Master autocorrelation at 3.95 s, 100-300 Hz band / centroid:

  | Passage | Band | Centroid |
  |---|---|---|
  | Lento 5-12 | -0.09 | -0.19 |
  | Bars 160-164 | -0.51 | -0.15 |
  | Bars 175-178 | -0.08 | +0.05 |
  | Bars 179-182 | -0.38 | -0.10 |

  The stem values match c27 (Violoncellos at qn 11 +0.69 on a short 6.3 s window, as before).
- **BRIEF item 8 passes (measured).** The accent front's 2-5 kHz excess over its broadband front-body:

  | Family | n | Median | p90 |
  |---|---|---|---|
  | Brass | 116 | -2.8 | +1.2 |
  | Winds | 186 | -1.7 | +3.1 |
  | Strings | 168 | -0.6 | +2.5 |

  The stem outliers (Clarinet 1 120/558, celli 526, Oboe 1 113) are all under 1 dB at the master, measured as front minus the previous 0.25 s. The exception is Oboe 1 113 at +5.2 dB, where the rest of the orchestra enters. The Clarinet 1 422 front makes -1.7 dB of the master's 2-5 kHz with front-body +2.5 (the known per-render state).

## 1. Revert the c28 celli 200 Hz loud bell: it added to a band that is already over all three references (measured; simulated)

**Where.** Violoncellos, the loud tutti spans of `loud_eq` (bars 24-32, 80-83, 115-124, 130-142, 157-162, 166-170). This is c28 C #3, kept as a test pending a listener.

**Evidence.** Long-term third-octave level re total (c28 / Dvořák / Brahms 1/i / Brahms 4/i):

| Band | c28 | Dvořák | Brahms 1/i | Brahms 4/i | c28 against the references |
|---|---|---|---|---|---|
| 125 Hz | -18.3 | -14.4 | -11.8 | -11.2 | 4-7 dB under |
| 157 Hz | -13.4 | -9.8 | -14.4 | -13.0 | |
| 198 Hz | -10.6 | -12.5 | -14.5 | -14.4 | 2-4 dB over |
| 315 Hz | -10.2 | -12.1 | -14.8 | -14.8 | 2-4.6 dB over |

- In loud frames, re 250 Hz-2 kHz:
  - 160-250 Hz is -9.1 against Dvořák's -10.9;
  - 100-160 Hz is -12.0 against -5.7.
- The c28 bell (+1.64 dB at 160-250 Hz in loud frames, per CHANGES) therefore went into the band that was already over the references, not into the shortfall.
- The celli supply 62% of the master's 198 Hz band in loud frames (stem share -2.1 dB).
- **Loud references grow at 157 Hz and this render does not.** Loud-minus-soft shape at 157 Hz: Brahms 1/i +2.8, Brahms 4/i +4.2, Dvořák +4.6, c28 -2.2 dB.
- **The shortfall is the voicing, as c25 found.** At qn 464-484 and 628-648 no sounding note has its fundamental between 112 and 178 Hz, except Bass trombone 15 qn and Trombone 2 7 qn. The basses, tuba and contrabassoon reach that band only with their third harmonic, and the celli are in G3 and above (196 Hz). An EQ cannot add those notes.

**Simulated (celli band power times the bell's response at each band, following the loud_eq wet curve; inferred to be within about 0.3 dB because cross terms are ignored).** Removing the bell:
- 198 Hz loud -9.1 -> -10.6 (Dvořák -10.9);
- 198 Hz long-term -10.6 -> -11.7;
- 157 Hz -0.3/-0.4;
- 125 and 315 Hz unchanged.

**Inferred effect.** A boxy, cardboard colour in the loud tuttis around G3/A♭3. The real orchestras put their extra weight lower, at 125-160 Hz.

**Fix (level/EQ only, `--mix-only` Violoncellos).** In `build/mix.json` Violoncellos `loud_eq`, remove `{"band": "bell2", "hz": 200, "db": 3, "bw_oct": 1.0}`. Keep the 150 Hz +6 band. Remove the two compensating celli roles from c28 at the same time (`roles.json` Violoncellos [104, 124, -0.8, 0.5] and [464, 480, -0.8, 0.5]), as the c28 notes say. Then re-check:
- celli K re master in bars 27-31 and 117-120 against c27 (+0.0 ± 0.5 dB);
- master loud 160-250 Hz re 250 Hz-2 kHz, target -10.0..-10.9.

Do not chase the 125-160 Hz shortfall with EQ.

## 2. The cello and bass body (120-250 Hz) is more diffuse than in any reference (measured; exact simulation)

**Where.** The whole movement. The band 120-250 Hz is carried by Violoncellos (share -3.2 dB), Double basses (-6.2), Timpani (-8.9) and Tuba (-11.1).

**Evidence.** Master correlation:

| | 20-60 Hz | 60-120 Hz | 120-250 Hz | 250 Hz-1 kHz |
|---|---|---|---|---|
| c28 | 0.584 | 0.667 | 0.442 | 0.534 |
| Dvořák | | 0.54 (under 120 Hz) | 0.556 | 0.546 |

- Brahms 1/i and 4/i read 0.541 and 0.583 under 250 Hz.
- c13 removed the Vc/Cb side shelf. Its own target was 0.48 or higher at 120-250 Hz (0.55 in c12, 0.49 simulated). It has drifted to 0.44.
- **Per stem, 120-250 Hz is the least correlated band.**

  | Stem | Under 120 Hz | 120-250 Hz | 250 Hz-1 kHz |
  |---|---|---|---|
  | Celli | 0.80 | 0.51 | 0.73 |
  | Basses | 0.60 | 0.39 | 0.67 |

  This is the true-stereo hall decorrelating the low mids (kit LEARNINGS section 12).

**Inferred effect.** On headphones the cello and bass body sounds spread out and phasey, rather than a section sitting right of centre in the room. The c13 shelf was a low shelf, so it also narrowed the deep bass. A bell centred on the problem band does not.

**Fix (`--mix-only` on both tracks; `set_side_shelf` is in the mix job, build_reaper.py ~line 697).** In `build/mix.json`:
- Violoncellos: `"side_shelf": [{"band": "bell", "hz": 170, "db": -2, "bw_oct": 1.0}]` (see finding 3 for a second band on the same track);
- Double basses: `"side_shelf": [{"band": "bell", "hz": 170, "db": -2, "bw_oct": 1.0}]`.

**Simulated exactly on the c28 master and stems.**

| Change | 20-60 Hz | 60-120 Hz | 120-250 Hz | 250 Hz-1 kHz |
|---|---|---|---|---|
| Bell 170 Hz -2 dB | 0.598 | 0.691 | 0.547 | 0.537 |
| Bell 170 Hz -3 dB | 0.605 | 0.702 | 0.588 | 0.538 |

- Power changes with -2 dB: 60-120 Hz -0.08 dB, 120-250 Hz -0.31 dB, 250-500 Hz -0.01 dB.
- -3 dB overshoots the references.

**Targets.**
- 120-250 Hz correlation 0.52-0.58.
- 60-120 Hz at most 0.71.
- Celli and basses seats within 0.5 dB of now (+5.3 / +5.5 R-L at 1-4 kHz and 120-250 Hz).
- 120-250 Hz master level within 0.5 dB.

## 3. In their exposed passages the celli sound as a narrow point, so the whole picture collapses to the right (measured; exact simulation; audible effect inferred)

**Where.**
- The fugato entry, bars 85-87 (qn 336-348): the celli are 91% of the master.
- The coda cello solo, bars 171-174 (qn 680-696).
- To a lesser degree wherever the celli lead (bars 47-50, 147-150 with Horn 1).

**Evidence.** Celli stem correlation above 4 kHz is 0.87 at width 0.28, where this band is all direct sound (the hall cuts at 5.5 kHz). The other string sections and the references:

| Vln I | Vln II | Violas | Master | Dvořák, 8 s windows (p50 / p90) |
|---|---|---|---|---|
| 0.42 | 0.66 | 0.71 | 0.552 | 0.52 / 0.62 |

Per bar, the master above 4 kHz / R-L at 250 Hz-4 kHz:
- bars 85-87: 0.86-0.87 / +5.3..+5.7 dB;
- bars 171-174: 0.85-0.87 / +4.2..+4.7 dB.

These are the most mono and most one-sided bars of the movement. The Dvořák windows never pass R-L -0.1 (p90), and their above-4 kHz correlation p90 is 0.62.

**Inferred effect.** A section of 10-12 cellos plays as one narrow source on the right, while Violins I at the same distance is 2-3 times as wide. It is the sample set's width, not the room. The cellos' width cannot be raised in Opus without undoing the c18 bass-correlation work and refitting, but a side-only high shelf widens only the top.

**Fix (same `--mix-only` edit as finding 2).** Violoncellos:

```json
"side_shelf": [{"band": "bell", "hz": 170, "db": -2, "bw_oct": 1.0}, {"band": "highshelf", "hz": 1500, "db": 4}]
```

**Simulated exactly (with finding 2's bells on both tracks).**

| Shelf | 336-348, 1-4 kHz / above 4 kHz | 680-696, 1-4 kHz / above 4 kHz |
|---|---|---|
| c28 | 0.80 / 0.84 | 0.82 / 0.86 |
| +3 dB | 0.68 / 0.68 | 0.76 / 0.70 |
| +5 dB | 0.56 / 0.46 | 0.69 / 0.49 |

- +4 dB should land near 0.57-0.62 above 4 kHz.
- Whole master above 4 kHz 0.556 -> 0.551 (+5 dB).
- R-L of the passages unchanged (+5.3 / +4.4).
- The side boost adds about +0.4-0.6 dB to the celli stem above 1.5 kHz (inferred from its side share). Check the celli front-body on the bar-85 staccato steps and the coda solo levels against c28, and trim with a roles row if they move more than 0.5 dB.

**Targets.**
- Bars 85-87 and 171-174: master above-4 kHz correlation 0.55-0.65.
- Celli stem above-4 kHz correlation 0.55-0.65.
- Whole master above 4 kHz at most 0.56.

## 4. The oboes sit in the wrong order (measured seats; effect inferred; small)

**Where.** Oboe 1 / Oboe 2 together: bars 158-162 (fff melody in thirds), letter G, and the second-theme chords.

**Evidence.** The current seats, against standard seating:

| Track | Seat | Width | Measured R-L, 1-4 kHz |
|---|---|---|---|
| Oboe 1 | 0.28 (set in c25 to keep its old image) | 0.05 | +4.3 dB |
| Oboe 2 | 0.15 | 0.5 | +3.0 dB |

- In standard seating the principals sit at the centre of the wind rows (Fl2 Fl1 | Ob1 Ob2, Cl2 Cl1 | Bn1 Bn2). The flutes and bassoons are in order. The clarinets measure Cl1 -3.3 / Cl2 -3.9, effectively together.
- Only the oboes are reversed: the first oboe's upper line comes from the outer seat, away from Flute 1 and Clarinet 1, which it doubles at bars 158-161.

**Fix (Opus state: a full rebuild of the two oboe tracks).** Bundle it with the next oboe rebuild rather than spending a render on it. In `build/mix.json`, Oboe 1 seat 0.28 -> 0.15 and Oboe 2 seat 0.15 -> 0.25, with widths unchanged. Refit the Oboe 1 accents and fills afterwards, as after any rebuild. Target: Oboe 1 R-L 1.0-2.0 dB left of Oboe 2 at 1-4 kHz, both between Flute 1 (-3.5) and the cor anglais (+2.9).

## Measured, no change proposed

- **Trumpet 1's position still varies by pitch in its fundamental band, and width is not the cause.**
  - Per note, 400-1000 Hz R-L SD 5.1 dB: 0..+15.6 dB at 122/484/556/637, with that band's L/R correlation 0.0-0.46 on exactly those notes.
  - 1.25-4 kHz SD 1.6 and 5-10 kHz SD 0.2, with correlation 0.96.
  - The track is already at width 0.05. The dry direct sound (above the hall's 5.5 kHz cut) is stable, and the moving part is the decorrelated hall return around the fundamental (inferred). Oboe 1 shows the same pattern (SD 4.9 / 0.8 / 0.5).
  - Do not run another width test. A lower send would move the trumpets forward of the trombones, which they now match in tail depth.
- **Low end against the references.**
  - Band shares, c28 / Dvořák / Brahms 1/ii / Brahms 4/ii:

    | 20-100 Hz | 100-250 Hz |
    |---|---|
    | -16.2 / -21.7 / -8.5 / -7.9 | -8.0 / -6.6 / -8.75 / -7.55 |

  - At the main climaxes, 60-100 Hz re 500 Hz-2 kHz is -9.9..-11.7 dB against Dvořák's loud -15.9. It is 85% the basses' G1 second harmonic. Dvořák is the lossy reference with 13 dB less 20-100 Hz (kit section 14), and the long-term 99 Hz band (-14.9) is under Brahms 1/i (-10.7), so I do not propose a cut.
  - The 315 Hz excess (finding 1 table) is spread over celli, violas, Horn 3, tuba and horns (none above a -8 dB share). It is pitch content in C minor, not one track.
- **High-frequency tails.** 5-10 kHz decays 9-16 dB faster than 1-2 kHz by +0.6 s on the trumpets and flutes. That is about what air absorption gives in a real hall (RT 8 kHz about 55% of RT 1 kHz), so the 5.5 kHz hall cut stays.
- **Crash.** Its 8-16 kHz ring falls about 15-20 dB per second after +1.7 s, where the c25 shape stops lifting. It meets c25's targets. A perc-only hall cut at 10-12 kHz remains the alternative if a listener finds the shimmer too short.

## Do not touch

- The shared true-stereo hall (IR, fx 0.19, wet 2.0, 5.5 kHz cut, pre-fader sends).
- The group sends, including the trumpets at 0.65, and the Close/Main levels.
- The string seats and the celli/basses widths (finding 3 widens only the top, in REAPER).
- The woodwind and brass width 0.05 and the c25 seats (apart from finding 4).
- The winds' and brass side shelves.
- The basses' 87.3 Hz bell2, mute_eq bells, 43/44 pitch trims and the 80 Hz loud shelf.
- The tuba and tam-tam bell2s.
- The brass 4 kHz shelves and the Trumpet 1 climax shelf.
- The crash shape and the suspended-cymbal timing.
- The celli 150 Hz +6 loud bell and the static 125/170 Hz bells.
- The re-bow and loop work (item 7) and the accent swells and fits (item 8).
- Climax order 160 > 122 > 167-170.
- Every c28 do-not-touch item in HISTORY.md except C #3.
