# Cycle 5, critic C: blend and space (review of the c04 render)

Lens: one room. Reverb, seating and panning, mic positions, tone matching between sample sets (trumpets and cymbals are new here), and low-end build-up against several references. I measured the stem-fixed c04 render (`cycles/c04/render/`), whose time map is correct, so score qn maps to file time through the parts.json tempo map. References: the movement II c26 final master (same library and hall) and the Dvořák 9/i master (lossy MP3; I used it only next to the other reference). Scripts and output are in `/private/tmp/claude-501/mockup-loop/mvt1-c05-C/`: perc.py, sim.py, longloop.py, fold.py, third.py, thirdhi.py, ratios.py, lowstems2.py, fund.py, leq.py, simlow.py, simlow2.py, hishare.py, brass.py, depth.py, stereo.py, tails.py, states.py, acc.py, acc2.py, acc3.py.

What I checked and found unchanged since c01 (measured): every one of the 32 Opus states uses the same true-stereo hall (`S. Cal Hall Perc TS FR 3.3s`, fx 0.19, wet 2.0, pre-fader sends). Master release decay at bar 170 is 14.7 / 21.3 / 32.0 dB at 0.3 / 0.6 / 1.0 s. The master stereo image is correlation 0.542, side/mid -5.3 dB, below 250 Hz 0.60, 250 Hz-4 kHz 0.54, above 4 kHz 0.47 (mvt II c26: 0.542 / -5.3 / 0.59 / 0.54 / 0.48). The trumpet gap from c01 is closed: over bars 158-161 Trumpet 1 measures 46.3 dB(A) against Trombone 1's 46.0, and Trumpets 2-3 measure 43.4 against Trombone 2's 43.0.

## 1. The fff crash at the main climax is gone within about a second (Crash cymbals, qn 636, bar 160)

**What is wrong.** This is the movement's single fff, and the crash is the stroke that marks it. In the render it is a short tick under the tutti, and its ring disappears into the strings and brass before the largamente bar has started.

**Evidence (measured, perc.py, 0.1 s RMS).**
- The stem peaks at -26.8 dB at +0.4 s, while the master is at -10.7 dB at the same moment. The crash is 16 dB under the master broadband.
- In the 4-12 kHz band, the crash against the master measures:
  - at the hit: 39.6 against 44.0 (-4.4 dB);
  - at +0.9 s: 29.7 against 39.2 (-9.5 dB);
  - at +1.4 s: 22.3 against 39.9 (-17.6 dB).
- The stem falls about 10 dB per second (-47.5 dB at +1.9 s, -63.7 at +3.9 s) and stops at +6.4 s, which is the end of the sample.
- The metrics table gives the crash a bar median of -69.8 dB at fff.

The patch is still `19in Zildjian A Crash` at key 60 v124, gain -6. Critic C of c01 proposed a crash swap (C4), which was deferred. The other HO pairs are longer: c01 read the `.ews` header frame counts as 22in Zildjian K Crash 9.4 s, 20in Constantinople Crash 9.7 s and 20in Zildjian Crash 8.8 s, against 6.2-8.8 s for the 19in A Crash "Long" samples at v120-127.

**Fix.**
- In `build/score_config.py` `TRACKS`, change the crash patch to `Cymbals/Cymbal Pairs/22in Zildjian K Crash.oib`. Before building, confirm that its Long articulation is key 60 by reading its region map with `opus_state.py`, as was done for the 19in patch. Keep v124, `min_s` 9 and `delay_s` 0.05.
- In `build/mix.json`, raise Crash cymbals `gain_db` from -6 to -1.

Effect on the climax (sim.py, +5 dB on the c04 crash stem): the bar 158-162 short-term maximum stays at -7.4 LUFS, and the 632-640 sample peak goes from 1.440 to 1.449. The limiter does not change, because the master peak at qn 637.9 comes from the strings and horns, not the crash.

**Targets in c05 (inferred):** crash 4-12 kHz at or above the master's at the hit, and within 6 dB of it at +1.5 s.

## 2. A loop pulse in tone colour on the exposed held horn notes of the final chord (Horn 4 and Horn 3, qn 720-728, bars 179-182; also Bass clarinet qn 492)

**What is wrong.** This is Dan's item 7, here on brass rather than strings. In the final ppp chord, Horn 4's G3 is one sample held for 12.3 s. Its tone colour cycles at the sample-loop period, while the strings around it have been re-bowed so that they do not. The horn is only 8.6 dB under the master in that chord, so the cycle is exposed.

**Evidence (measured, longloop.py and fold.py; 50 ms frames, quadratic trend removed).**

Horn 4 at qn 720:
- Autocorrelation at 3.95 s: 0.91 in the 100-300 Hz band level, 0.72 in the spectral centroid.
- Best period 3.85 s. At that period the folded swing is 19.7 dB in the 100-300 Hz band (the fundamental at 196 Hz) and 76 Hz in the centroid, while the total level swings only 3.1 dB.

That pattern is what the c03 loop profile (`build/loop_profiles.json` "Horn 4" 720.0) left behind: it flattened the level and left the colour cycle, the same failure movement II had on its final chord.

Other long notes:
- Horn 3 at qn 720: autocorrelation 0.05 / -0.23 at 3.95 s, best 0.36 at 4.5 s, so it is weaker.
- Bass clarinet at qn 492 (6.6 s, bar 124): autocorrelation 0.77 / 0.69, folded level swing 7.5 dB, but 13 dB under the master during the fff sostenuto, so it is probably masked (inferred).
- No other wind, brass or timpani note longer than 6 s exceeds 0.6 in both measures (Bassoon 2 qn 48: 0.60 / 0.26).

**Fix.** Give the brass held notes the same treatment as the timpani re-strikes:
- In `tools/score_to_parts.py`, add a `BREATH_SPLIT_AT` table, `{track: {score onset: [split qn, ...]}}`. At output it splits the note into abutting same-pitch pieces, with the earlier piece ending 0.05 qn before the split.
- The new piece starts on the note's own Sus row at the note's velocity minus 8. CC11 continues unbroken.
- The new piece gets a volume-envelope dip of -3 dB at the split that is gone by +0.4 s, so the re-entry stays under the chord, as a player's staggered breath does.
- Movement I values in `build/score_config.py`: `{"Horn 4": {720.0: [723.5]}, "Horn 3": {720.0: [725.0]}}`. These split the two horns at different times and keep every piece under 6 s.
- Remove `loop_profiles.json` "Horn 4" 720.0, because it is keyed to the old single note.

**Target:** Horn 4's 100-300 Hz and centroid autocorrelation at 3.95 s under 0.4, with no level step over 2 dB at the splits. Whether the re-entry is audible under Horn 3 and the strings is inferred; measure the master at each split against 0.5 s before it.

## 3. Low end in the loud tutti: a peak at 89-112 Hz and a hole at 112-180 Hz (Double basses; the G pedals of bars 24-32, 115-122, 130-134, 157-161)

**What is wrong.** The c01 fix moved this very little: the loudest 10% of frames measured 100 Hz -11.7 -> -12.6 dB and 160 Hz -16.0 -> -15.5 dB (third.py, re 500 Hz-2 kHz). The loud tutti still has one booming band and a thin body above it.

**Evidence (measured, ratios.py; band level re 300 Hz-1 kHz).**

| frames | 63-89 | 89-112 | 112-140 | 140-180 | 180-250 |
|---|---|---|---|---|---|
| loudest 10%, c04 | -21.2 | **-11.9** | -17.0 | -14.8 | -9.4 |
| loudest 10%, mvt II c26 | -17.6 | -14.7 | -14.0 | -12.0 | -7.7 |
| loudest 10%, Dvořák 9/i | -24.0 | -16.6 | -8.6 | -6.1 | -8.2 |

- The 89-112 Hz band is 2.8 dB over mvt II and 4.7 dB over Dvořák.
- 112-180 Hz is 2.8-3 dB under mvt II and 6-9 dB under Dvořák. The Dvořák difference is partly key and voicing.

Where the 89-112 Hz band comes from (lowstems2.py, fund.py, measured):
- In the loudest frames, the basses supply 62% of 89-112 Hz (share -2.1 dB).
- The most-held bass pitch in the loud spans is G1 (55 qn, from the dominant pedals; Ab1 13 qn). The fundamental of G1 sits 18 dB under harmonics 2-4, so G1 sounds mostly as its 98 Hz second harmonic.
- Over the loud_eq spans, the bass stem's 89-112 Hz is 9.5 dB over its own 140-180 Hz, even with the static `bell2` (100 Hz -5 dB).

Who supplies 112-180 Hz in the loudest frames: celli 26%, timpani 19%, tuba 19%, basses 10%.

**Simulated on the c04 stems (simlow.py, simlow2.py, EQ applied inside the existing loud_eq spans), loudest 10%:**

| change | 89-112 | 140-180 |
|---|---|---|
| c04 | -11.9 | -14.8 |
| Basses bell 98 Hz -4 dB, 0.5 octave | -14.0 (mvt II level) | -14.9 |
| plus a celli bell 150 Hz +3 dB, 1 octave | -13.8 | -13.7 |
| bass-octave roles instead (Tuba/Cbn/Bn2 +3, BTbn/Timp +2) | -13.6 | -13.8 |

63 Hz stays within 0.6 dB in every case.

**Fix in `build/mix.json`.**
- Add a second band to the Double basses `loud_eq`: `{"band": "bell", "hz": 98, "db": -4, "bw_oct": 0.5}`. Keep the existing points.
- Raise the Violoncellos `loud_eq` bell from 160 Hz +4 to 150 Hz +6 dB, bw 1.0.
- The bass-octave roles add less and cost balance, so leave them out.

**Targets in c05, loudest 10%:** 89-112 Hz at or below -14 dB re 300 Hz-1 kHz, 140-180 Hz at or above -14 dB. The size of the remaining 112-180 Hz gap against Dvořák is a voicing question (mockup-kit LEARNINGS section 14, inferred); do not chase it with more EQ.

## 4. The fff tam-tam does not carry through the sostenuto (Tam-tam, qn 484, bars 122-126)

**What is wrong.** The tam-tam stroke is printed fff with a heavy beater and l.v. through bar 126, under the sostenuto brass. In the render it is heard at the stroke and is then gone from the texture within about 2 s.

**Evidence (measured, perc.py and sim.py).**
- The stem peaks at -20.2 dB at +0.65 s, 8.7 dB under the master.
- Broadband against the master:
  - +0.5 s: -9.5 dB
  - +1.5 s: -13.1 dB
  - +2.5 s: -18.3 dB
  - +4.0 s: -20.6 dB
- In 4-12 kHz, the tam-tam against the master:
  - at +0.4 s: 33.8 against 39.1 (-5.3 dB);
  - at +1.4 s: 28.8 against 36.5 (-7.7 dB);
  - at +2.4 s: 20.0 against 36.6 (-16.6 dB).
- The c01 target, 4-12 kHz within 4 dB of the master for the first 2 s, is met only for about the first 0.5 s.

**Fix.** Add a role to `build/roles.json` "Tam-tam": `[484, 486, 2]`, then `[486, 512, 6]`, with a 2 qn ramp between them. The shape is +2 dB at the stroke rising to +6 dB from about +2 s on, which follows the instrument's bloom and leaves the stroke itself almost unchanged.

Simulated (sim.py, with crash +5 from finding 1): tam-tam against the master is -7.4 / -7.8 / -12.5 / -14.7 dB at +0.5 / 1.5 / 2.5 / 4 s. The bar 120-125 short-term maximum goes from -8.5 to -8.1 LUFS, while bar 158-162 stays at -7.4.

That narrows the climax margin (160 over 122) on the master from 1.1 to 0.7 dB. If the delivered margin falls under 0.8 dB, take 0.5 dB off the c04 brass roles at [484, 496] (Tbn1/Tbn2 +3 -> +2.5); do not lower the tam-tam. A plain +4 dB gain instead raises bar 122 by 0.5 dB, which is why I propose the role shape.

## 5. Loud tutti top is 2-3 dB darker than both references at 2-4 kHz, and only the first violins supply it (inferred; Violins I, loud spans)

**Evidence (measured, thirdhi.py and hishare.py).**
- Loudest 10% of frames, re 500 Hz-2 kHz:
  - 2 kHz: -13.6 against -9.7 (mvt II c26) and -10.7 (Dvořák);
  - 4 kHz: -20.1 against -17.3 and -17.4;
  - 2.5 and 3.15 kHz match mvt II but are 1-2.6 dB under Dvořák.
- Middle and soft frames are within 0.5-2 dB of mvt II.
- In the loudest frames, Violins I supply 56% of the master's 2.5-4 kHz (share -2.5 dB), and Violins II 19%. All three trumpets together supply about 3.5%, because the 1TP stems' own 2.5-4 kHz sits 14-16 dB under their 300-800 Hz band.
- A brass presence boost therefore could not move the master (+3 dB on the trumpets adds about 0.15 dB there). The Violins I `highshelf` 5 kHz -4 dB (a movement II choice) takes some of what the loud tutti lacks.

**Fix (test, inferred).** In `build/mix.json` Violins I, add `loud_eq` with the Double basses' points and `[{"band": "bell", "hz": 3000, "db": 2, "bw_oct": 1.5}]`. Leave the static shelf.

**Target:** loudest-10% 2-4 kHz up 1-1.5 dB, with soft and middle frames unchanged.

**Check:** run the accent 2-5 kHz first-80 ms test on Violins I in bars 158-161 and 116-122. If any accent rises above +3 dB over its body, drop the change. Harshness is the risk here, and nobody in the loop can hear it.

## 6. The percussion stands in three places (Tam-tam seat -0.15, Crash cymbals +0.10, Suspended cymbal +0.25; inferred, low priority)

**Evidence (measured, depth.py).** Sustain R-L: tam-tam -1.9 dB, suspended cymbal +1.7, timpani +0.6. The suspended cymbal and the crash play into each other at qn 632-636 from different positions.

**Fix (inferred).** In `build/mix.json`, set all three cymbal and tam-tam tracks to seat +0.3 and width 0.4 (one section, to the right of the timpani at the back, beside the low brass). This is a placement change only, and it can be done in the same rebuild as the crash patch swap. The Opus pan is set by the seat, so it needs that track's full rebuild anyway.

## Other checks (measured)

- **Item 8 (accents).** 2-5 kHz in the first 80 ms minus the note body (acc.py):

  | track | median | worst |
  |---|---|---|
  | Trumpet 1 | -8.7 dB | -2.1 dB |
  | Trumpet 2 | -11.5 dB | -1.4 dB |
  | Trumpet 3 | -10.2 dB | -4.0 dB |
  | Trombone 1 | -9.9 dB | +0.3 dB |
  | Trombone 2 | -11.5 dB | — |
  | Bass trombone | -11.1 dB | — |
  | Horns | -0.9 to -7.2 dB | three exceptions below |

  The three horn exceptions are slurred accents at mf/f: Horn 1 qn 311 (+7.9 dB), Horn 3 qn 317 and 321 (+8.8 / +8.6 dB). They are 11-19 dB under the master's 2-5 kHz, and the master rises by only 0.5-2.6 dB at them. They are masked; note them for critic A.
- **Item 7 on the master.** Final chord at 3.95 s: 100-300 Hz -0.15, centroid 0.02. Timpani opening roll -0.07 / -0.16. Fine.
- **Depth.** Release drop at 0.3-0.5 s is 15-20 dB for winds, trumpets and upper strings and 12-17 dB for horns and low brass. No family is drier or wetter than the rest.

## Do not touch

- The shared true-stereo hall and its settings (one IR, fx 0.19, wet 2.0, 5.5 kHz high cut, pre-fader sends), the per-group mic and send levels, all seats except the percussion, the side-only shelves and the Vc/Cb widths 0.28: the master image matches the reference to 0.01 in correlation.
- The c01 trumpet loud trims (trumpets now level with the trombones at ff/fff) and the trumpet group mics (Close 0.5 / Main 1.0).
- The suspended-cymbal key 64 and lead 0.25 s: the roll peaks at 355.2 s, 0.1 s before the crash.
- GENTLE_ACCENT on all brass.
- The Basses static `bell`/`bell2` and the existing loud_eq points: add to them, do not replace them.
- Climax order 160 > 122 > 169.
