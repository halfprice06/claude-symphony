# Cycle 30, critic B: balance and levels (render c29)

## Method

All numbers come from `cycles/c29/render/`, the stems and master after the c29 stem fix. Notes, articulations, CC11 and volume envelopes come from `build/parts.json`, and printed marks from `build/mockup-events.tsv`. Trims and fills come from `build/roles.json`, `build/pitch_trims.json`, `build/note_trims.json`, `build/early_fills.json` and the `LEVEL_SHAPES` rows in `build/score_config.py`.

Each stem and the master got a 10 ms STFT envelope (stereo power), in A weighting, approximate K weighting, and six bands. "re M" means stem minus master over the same window. A note body runs from onset + 0.04-0.06 s to the note end, at most 1 s. The simulations add (gain - 1) x stem power to the master frame by frame. That is exact for level-only changes up to frame resolution.

I ran four scans over the whole movement:

1. Every track's note bodies by printed dynamic.
2. Family sums per bar against the master.
3. Every lead-line note in `LEAD_SPANS` against the loudest non-doubling track.
4. Every note against the neighbouring notes of the same track at the same printed dynamic, outside hairpins. I split this scan by pitch and articulation row.

Scan 4 found most of the findings below. They are single notes or short spans where a sample, a trim or a fill makes one instrument jump 5-10 dB out of its line.

Score pages checked: 3, 5, 7-9, 11-13, 15-18.

## What holds (measured)

**Dynamic mapping between families.** Median note-body levels of single stems, in K:

| Dynamic | Strings | Woodwinds | Horns | Trombones | Timpani |
|---|---|---|---|---|---|
| pp | -45..-49 | -44..-48 | -44..-46 | -46..-49 (coda chorale) | -53 |
| f | -31..-33 (basses -37) | -35.7..-36.9 | -34.3..-34.5 | -30.9..-34.3 | -31.7 |

At f the trumpets sit at -31.9/-34.9/-33.5 and the tuba at -31.3.

The new trumpet tracks sit with the trombones at every loud dynamic:

| Dynamic | Trumpet 1 | Trombone 1 |
|---|---|---|
| f | -31.9 | -30.9 |
| ff | -25.3 | -27.5 |
| fff | -21.9 | -21.4 |

That is the Rimsky-Korsakov forte equation (trumpet = trombone = two horns).

So p sounds like p and f like f across the families, within about 3 dB once role and section size are allowed for.

**Timpani, percussion and brass do not cover.** I checked every 1 qn window where the master is above -45 dB (A):
- No window has timpani, tam-tam, suspended cymbal or crash within 6.5 dB of the master. At the tam-tam's bar 122 stroke it is -9.8 A re M, and the master's top stem is a melody or tutti voice.
- The only brass windows within 6.5 dB of the master are:
  - Trumpet 1 carrying the bars 167-169 a2 tune (-4.8..-5.9), which is correct;
  - Trombone 1 in bars 80-81 (see the smaller items);
  - single coda chorale notes.

**Lead lines.** In the `LEAD_SPANS` scan the median gap between each lead note and the loudest non-doubling voice is:
- Violins I: -1.5 to -4.8 dB;
- Horn 1 and celli second themes: -3.8 to -9.9;
- Clarinet 1 bar 127: -11.3.

Nothing outside the items below covers a lead by more than 2-4 dB on more than one note. The bars 167-170 violas span is covered, but there the tune is carried by Trumpet 1 and Horns a2, which sit at the top. So the scan's flag is a doubling artefact, not a balance fault.

**Dan's checks (BRIEF 7-8).**
- Loop pulsing: 100-300 Hz band and spectral-centroid autocorrelation at 3.95 s, after detrending:

  | Passage | Master band | Master centroid | Stems |
  |---|---|---|---|
  | Bars 1-4 | +0.07 | -0.05 | +0.18 or lower |
  | Bars 175-178 | -0.23 | -0.18 | |
  | Bars 179-182 | -0.20 | -0.12 | -0.34..+0.08 |
  | Bars 123-126 | -0.23 | -0.08 | Horn 3 band +0.39 (its held pedal under the tam-tam; the master does not carry it) |

  No pulsing.
- Accents: the 2-5 kHz first 80 ms minus body (0.15-0.5 s) on f+ accents of 0.5 qn or longer has these medians:

  | Track | Median (dB) |
  |---|---|
  | Trumpets 1/2/3 | -8.9 / -12.2 / -14.6 |
  | Trombones | -8.5..-9.5 |
  | Horns a2 / Horn 3 | -4.0 / -4.2 |
  | Tuba | -16.8 |

  Two Trumpet 1 fronts stand over their bodies: qn 284 at +5.9 dB (6.1 dB under the master's 2-5 kHz) and qn 670 at +2.2 dB (only 1.8 dB under the master's 2-5 kHz). Those are for critic A.
- All fixes below are level only, so they change neither check.

## 1. Bars 45-46 (qn 176-183): Oboe 1's descending p solo rises 10 dB from its first note to its last, and the last note E♭4 jumps 5 dB over the F4 before it (measured; fix simulated)

**Where.** Score p. 5. Oboe 1 plays a slurred p phrase, B♭4 - A♭4 - G4 - F4 - E♭4, poco rit., over pp strings. It has no hairpin. The celli's mf pickup enters only on beat 4 of bar 46 (qn 183).

**Evidence (K note bodies).**

| Note | Body (K) |
|---|---|
| B♭4 176 | -44.7 |
| A♭4 178 | -42.1 |
| G4 179.5 | -42.3 |
| F4 180 | -40.2 |
| E♭4 182 | -34.9 |

- So the falling line grows 10 dB, and its last note sits at -2.1 re M, the top of the bar.
- On the E♭4 three things stack:
  - the `[176, 184, 4]` role;
  - the c01 `early_fills.json` "182" fill (+4.6 dB, which peaks the envelope at +8.6 at 182.17);
  - a louder low-register sample.
- The c24 `LEVEL_SHAPES` row only shapes 178-182 and returns to 0 at 182.0, so it does not reach the E♭4.
- A descending p phrase that ends at the solo's loudest level reads as an unprinted crescendo, in the most exposed bar before the second theme (inferred).

**Fix.** Add `LEVEL_SHAPES["Oboe 1"]` row `[(181.95, 0.0), (182.05, -6.0), (183.0, -6.0), (183.2, 0.0)]` in `build/score_config.py` next to the c24 row. It is level only, so it can go in by stem fix. Keep the "182" early fill; the shape is measured with it in place.

**Simulated.**
- E♭4 body: -34.8 -> -40.5 K, 0.7 dB under the F4. The line now relaxes slightly into the cadence instead of climbing.
- Oboe at 182: -2.0 -> -5.1 re M.
- Master bar 46 beat 3: -32.8 -> -35.4. Beat 4 (the celli pickup) -32.0 -> -32.3.

## 2. Bar 93 (qn 371): the cor anglais's last staccato quarter, A4 at f, is 5-9 dB over its other staccato notes and the top stem of the fugato (measured; fix simulated)

**Where.** Score p. 9. In bars 91-93 the cor anglais and Violins II play the fugato subject, f. Bar 93 has four staccato quarters, F4 - G4 - A♭4 - A4 (368-371). The cor anglais rests at bar 94.

**Evidence.**
- 40 ms peaks: G4 369 -33, A♭4 370 -35, A4 371 -26 K. Note bodies (K) are -34.7 / -40.1 / -29.4.
- The A4 is the loudest stem of the moment (-3.6 re M), and the master rises 3 dB on it (-29 -> -26 K) while nothing else is printed louder.
- Same patch, same velocity 87, CC11 flat at 88, the same staccato volume shapes.
- `pitch_trims.json` already trims Cor anglais A4 -5 and A♭4 -4 on every articulation (c07: Sus +9.8/+11 at 361/371). At p (587-604) those trims leave A4 within 1-4 dB of G4. At f the A4 trim is still about 5 dB short, and the A♭4 trim cuts about 5 dB too much.
- So it is a dynamic-dependent sample step, not a pitch constant. Changing the pitch trims would break the p notes (inferred from the p-note levels).

**Fix.** In `build/score_config.py`:
- Add `LEVEL_SHAPES["Cor anglais"]` row `[(370.98, 0.0), (371.08, -6.0), (371.75, -6.0), (372.0, 0.0)]`, which covers the release tail.
- Optionally add `[(369.98, 0.0), (370.05, 3.0), (370.6, 3.0), (370.7, 0.0)]` for the A♭4.

Leave `pitch_trims.json` as it is.

**Simulated.**
- A4 stem -30.2 -> -36.2 K at 371.0-371.5, level with the G4 (-35.4).
- CA re M -4.0 -> -8.5.
- Master -26.2 -> -27.7, so it no longer bumps on the last quarter.

## 3. Bassoon 1 C♯4/D♭4 on Sus MAX: every f/ff note of a half note or longer stands 5-7 dB over its neighbours (measured; fix simulated)

**Where.**
- Bassoon 1 MIDI 61 on the Sus MAX row:
  - 280 (bar 70);
  - 382 (bar 96);
  - 396 and 400 (bars 100-101, letter F countermelody);
  - 407.5 (bar 102);
  - 476 (bar 120, ff).
- The two legato C♯4s (131, 523) and two short Sus notes (351, 391.5) are level with their lines.

**Evidence (K body against the median of the neighbouring notes, same dynamic).**

| Onset | Deviation | re M |
|---|---|---|
| 382 | +5.9 | -10.5 |
| 396 | +6.4 | -9.5 |
| 400 | +5.2 | -11.4 |
| 407.5 | +6.7 | -8.2 |
| 476 | +5.2 | -9.2 |
| 280 | +4.7 | -11.9 (despite its -4 note trim) |

- `pitch_trims.json` has Bassoon 1 `"61": -5` on legato notes only. The Sus MAX row carries the same hot sample untrimmed.
- At -8..-11 re M one bassoon pops out of the ff countermelody on every C♯ (inferred as audible; a real player's C♯4 is not 6 dB louder than the D4 next to it).

**Fix.** In `build/pitch_trims.json`, Bassoon 1:
- add `"_all_arts_pitches": [61]`;
- add `"_skip_onsets": [351.0, 391.5]` (the two short Sus notes, which are not hot).

Keep the 280 note trim (-4).

**Simulated (stem K, against the neighbours).**

| Onset | Before | After | Neighbours |
|---|---|---|---|
| 382 | -30.4 | -35.4 | -34.2 |
| 396 | -29.4 | -34.4 | -35.1 |
| 400 | -29.4 | -34.4 | -33.9 |
| 407.5 | -28.8 | -32.4 | -33.9 |
| 476 | -24.6 | -29.6 | -29.1 |
| 280 | -34.2 | -39.2 | -38.0 |

The master moves 0.2-0.4 dB.

## 4. Bar 114 (qn 453-455.5): the Violins I melody drops 4-5 dB inside the long mp cresc., under the clarinets (measured; fix simulated)

**Where.** Score p. 11. In bars 111-116 the whole orchestra plays mp cresc. into the ff of letter G. In bar 114 the Violins I tune descends C6 - B5 - F5 - A♭5 (453.5-455.5) before climbing to the D♭6 of bar 115. It plays on Leg Slur MAX, with the volume envelope rising +1.6 -> +1.9 and CC11 87 -> 93.

**Evidence (K, 0.5 qn windows).**
- Violins I: -29.1 at 452.5, then -31.1 / -34.2 / -35.2 / -32.9 / -33.3 over 453-455.5, then -29.3 at 455.5 and -28.0 at 456.
- Re M it falls from -6.2 to -13.7 while the printed crescendo continues.
- In A, Clarinet 1 (-7.4 re M at 452.5-453) and Violins II (-10.2) sit level with the tune or over it.
- The master itself dips 1.5 dB (-20.1 -> -21.5 K) in the middle of a printed crescendo.

**Fix.** Add `LEVEL_SHAPES["Violins I"]` row `[(453.05, 0.0), (453.25, 4.0), (455.35, 4.0), (455.55, 0.0)]`. It is level only, so it can go in by stem fix.

**Simulated (K).**
- Violins I 453-455.5: -28.9 / -30.2 / -31.2 / -28.9 / -29.6. That is level with 452.5 and 455.5.
- Re M -9.1..-10.0, in line with -8.2..-8.7 either side.
- Master +0.3 dB.

The remaining 1 dB master dip comes from the winds' long notes and is small.

## 5. Bars 91-96 (qn 364-383): the bass clarinet's B♭2s stand 5-9 dB over its own line and up to 7 dB over the whole bass section, level with the fugato subject (measured; fix simulated)

**Where.** Score p. 9. The bass clarinet (low C instrument) plays the f bass line with Bassoon 2, the celli and the basses, under the CA/Violins II subject.

**Evidence.**
- Bass clarinet bodies (K): B♭2 364 -33.6 and 372 -33.7, against C2/C♯2 neighbours at -37.9..-40.1.
- The cresc. notes 380/382 sit at -31.1/-29.1, against -37.3..-38.8 for 376-378.
- At 364 and 372 the bass clarinet is -6.8/-7.4 K re M. The basses are at -14.2/-12.2 and the cor anglais subject at -8.9/-7.4.
- So one bass clarinet is as loud as the subject and 7 dB over eight basses.
- Its other B♭2s (276 f, 306.5 mf, 435.5 p) are not hot.
- Adler's and Rimsky-Korsakov's descriptions of the low bass clarinet (dark, soft-edged, a colour inside the bass) do not fit a voice that leads the bass line over the section (inferred).

**Fix.** In `build/note_trims.json`, add Bass clarinet `{"364.0": -4, "372.0": -4, "380.0": -4, "382.0": -4}`. In `build/score_config.py`, add `NOTE_TRIM_RAMP_S["Bass clarinet"] = {364.0: 0.1, 372.0: 0.1, 380.0: 0.1, 382.0: 0.1}`.

**Simulated.**
- Stems: 364 -38.1, 372 -37.7, which is level with C2/C♯2. 380 -35.2 and 382 -33.3 still rise into the ff at 384.
- Re M: -10.5 / -9.9 / -12.0 / -15.5.
- Master -0.2..-0.6 dB.
- The subject is then the top line of bars 91-93.

## Smaller items (measured; no change proposed)

- **Bars 80-81 (qn 316.5-321).** Trombone 1 alone carries the "a2" f stab (Trombone 2 is silent there), at -3.2..-3.7 A re M. That is 4.5 dB over Horn 3, which carries the horns' a2 in the same figure. Rimsky-Korsakov's forte equation predicts about +3 for a2 trombones over a2 horns. The excess is 1.5-2 dB, too small to change in the last cycle.
- **Recapitulation second theme (bars 147-155).** Horn 1 (mp) and the mf celli trade the top within ±3 dB, the same as the exposition. Horn 1's D4 (587.5, 603) is +3.4/+4.5 over the celli.
- **Letter D (bars 69-70).** Violins I carry the f tune at -4.2 re M. The a2/unis. counter-theme (clarinets, horns a2, Violins II, violas) is 4-5 dB under the tune group as a whole. That is acceptable, since the tune should lead.
- **Trumpet 1 accent at qn 670 (bar 168).** Its 2-5 kHz front is +2.2 dB over the body and only 1.8 dB under the master's 2-5 kHz. That is for critic A.

Do not touch:
- the trumpet levels against trombones, horns and woodwinds (dyn trims and roles);
- timpani and percussion levels (crash and suspended-cymbal shapes, tam-tam rows, the bar-40 timpani shape);
- the bars 167-170 letter-L roles (Trumpet 1 and Horns a2 on top);
- the c29 rows (bars 103-106 counter-line roles, letter-G flute/oboe rows, basses 29/41/31 trims, bar-40 trombone roles, celli/basses side EQs);
- the c24 Oboe 1 178-182 shape and the "182" early fill (finding 1 adds a row after them);
- the Cor anglais A4/A♭4 pitch trims (finding 2 fixes the f note locally);
- the Bassoon 1 280 note trim;
- every c29 do-not-touch item.
