# Cycle 21, critic C: blend and space (on the cycle 20 render)

Lens: one room. Reverb, seating and panning, mic positions, tone matching between sample sets, low-end build-up against the reference spectrum.

Under review: `cycles/c20/render` (master and 32 stems), `cycles/c20/metrics`, `cycles/c20/CHANGES.md`, `build/parts.json`, `build/mix.json`, `tools/build_reaper.py` (`apply_mix`, `set_side_shelf`, `mute_lua`), the Opus states of every patch (read with `opus_state.load_oib`), score pages 4 and 6.

Scripts and outputs are in `/private/tmp/claude-501/mockup-loop/c21-C/`:
- `bands.py` (`bands_c19.json`, `bands_c20.json`): per-stem L/R correlation, R-L and energy share in 7 bands.
- `shelfest.py`: the side shelf's actual response, read from c19 -> c20 stems.
- `sidesim.py`, `combosim.py`, `widesim2.py`, `finalsim.py`, `itdsim.py`: M/S simulations on the c20 stems (the stems sum to the master).
- `lowpow.py`, `lowdist.py`, `lowbars.py`, `lowcontrib.py`, `cbsim.py`, `cbharm.py`, `pizz.py`: low end against the Dvorak reference, per loudness third, per bar, per stem.
- `mics.py`, `divtone.py`, `divtail.py`, `horntone.py`, `harpsim.py`, `midcorr.py`: mic columns, close-only tracks, tails, tone, harp.
- `m_c20/`: `symphony/render/tools/measure.py` on the c20 master.

Delivery numbers (from c20 metrics; this lens does not move them): master -22.6 LUFS, LRA 23.6 LU, TP -3.8 dBFS. mp3 -19.8 LUFS, LRA 16.0 LU, TP -1.6 dBTP, span 18.5 dB, limiter 2.2 dB.

## Where the room stands (measured)

| | c19 | c20 | Brahms 1/ii | Brahms 4/ii | Dvorak 9/i |
|---|---|---|---|---|---|
| corr L/R, whole | 0.557 | 0.631 | 0.512 | 0.554 | |
| corr <250 Hz | 0.434 | 0.754 | 0.601 | 0.624 | |
| corr 25-60 / 60-120 / 120-250 | 0.47 / 0.52 / 0.39 | 0.90 / 0.88 / 0.71 | | | 0.48 / 0.56 / 0.56 |
| corr 250 Hz-4 kHz | 0.600 | 0.611 | 0.483 | 0.522 | |
| corr >4 kHz | 0.496 | 0.496 | 0.378 | 0.465 | |
| side/mid (dB) | -5.5 | -6.4 | -4.9 | -5.4 | |
| pan spread std | 0.349 | 0.323 | 0.323 | 0.314 | |
| centre two pan bins | 41% | 46% | 50% | 50% | |

The hall is right: the same true-stereo IR on every track, final decay RT60 2.59 s (Brahms 2.5 / 2.9), and the tail drops 0.2-1.0 s after phrase ends are similar across families (`divtail.py`: strings 6-13 / 22-28 / 32-37 dB at 0.2 / 0.7 / 1.0 s, winds 12-18 / 23-29 / 32-37). Close/Main ratios run from front to back as they should: strings -3.6 dB, winds -4.1, harp and Cb -4.4, horns -6, trombones -6.2, tuba -6.9, timpani -8. The c20 side shelf fixed the anti-phase harp and the diffuse bass, but overshot. What is left is the low end and the image of the solo instruments.

## 1. The side shelf made the bass nearly mono: master correlation below 120 Hz 0.88-0.90, against 0.48-0.62 in the references. Set the bass tracks' shelf to -2 dB. Measured; fix simulated.

**Where:** every bar with Vc, Cb, Tuba, BTbn, Cbn or timpani. c20 `build/mix.json` `side_shelf {hz 200, db -6}` on those six tracks.

**What is wrong:** c20 C #2 set a target of 0.55-0.65 below 250 Hz. The c20 render reads 0.754 (measure.py), and per band 0.90 / 0.88 / 0.71. Per stem at 60-120 Hz, Cb is 0.88, Vc 0.97, Tuba 0.95 and BTbn 0.98, so each bass instrument is close to a mono point. Effect (inferred): on headphones the bass sits as one narrow source in the middle of the head, under a string section that is spread from wall to wall. In a hall the bass has a place but also some width from the room. The low band also lost energy: the stereo power at 25-60 / 60-120 / 120-250 Hz went down 0.7 / 0.6 / 0.9 dB from c19 to c20 (side energy removed; the mono sum is unchanged).

**Evidence (measured).**
- `shelfest.py` reads the shelf as built: -6.0 dB up to 100 Hz, -5 at 140, -3 at 200, -1 at 280, 0 above 400. So it is a plain low shelf, as specified.
- `sidesim.py`: the c20 stems with the shelf replaced, master correlation at 25-60 / 60-120 / 120-250 Hz:

| bass tracks | 25-60 | 60-120 | 120-250 | 250-500 | power vs c20 at 25-60 / 60-120 / 120-250 |
|---|---|---|---|---|---|
| -6 at 200 Hz (c20) | 0.90 | 0.88 | 0.71 | 0.63 | 0 |
| -3 at 200 Hz | 0.79 | 0.79 | 0.60 | 0.62 | +0.4 / +0.3 / +0.3 |
| -2 at 200 Hz | 0.73 | 0.75 | 0.56 | 0.62 | +0.7 / +0.4 / +0.4 |
| -1.5 at 200 Hz | 0.70 | 0.72 | 0.53 | 0.62 | +0.8 / +0.5 / +0.5 |
| off | 0.54 | 0.63 | 0.45 | 0.61 | +1.2 / +0.8 / +0.7 |

- `itdsim.py` (row "0 ms", the -2 dB shelf alone, through `rtk.stereo_stats`): corr <250 Hz 0.608, whole 0.598, centre two pan bins 43%. Those are the Brahms values.
- Keep the harp at -8 dB at 300 Hz. `harpsim.py`: the harp shelf costs the harp only 0.5 dB of total power. With -5 dB the harp 120-250 corr falls back to 0.46 and its 250-500 corr to 0.18, so -8 is right. The level loss the actor saw in some passages came from roles and width, not the shelf.

**Fix:** `build/mix.json`: `"side_shelf": {"hz": 200, "db": -2}` on Double basses, Violoncellos, Tuba, Bass trombone, Contrabassoon, Timpani. Leave Harp and Harp harmonics at `{"hz": 300, "db": -8}`. Apply with `--mix-only` (the chain is REAPER FX). This is exact on the c20 stems, so it can also go in as a stem fix.

**Check:** master corr <250 Hz 0.58-0.65 (measure.py), 25-60 and 60-120 Hz each 0.65-0.78 (`bands.py`). 250 Hz-4 kHz within 0.01 of c20. Cb, Vc and Tuba 60-120 Hz corr 0.70-0.85.

## 2. In the loud tutti the double-bass fundamentals boom: 60-100 Hz is 7.5 dB over the reference relative to the mids, while the soft passages match it. Deepen and widen the Cb `loud_eq` shelf. Measured; the fix is simulated; the size of the target is inferred because the references are in other keys.

**Where:** bars 54-64 and 75-81 (qn 190-216 and 254-271), Double basses. Score: bars 60-62 ff, Cb on Db (69 Hz fundamental); bar 78 f (poco allargando) to the ff of bar 79.

**What is wrong:** in a real orchestra the low end grows more slowly than the mids as the music gets louder, because loud playing adds upper harmonics. In the render it grows faster. The Cb supplies 95% of the master's 30-100 Hz in the loud blocks (`lowcontrib.py`). Effect (inferred): the two climaxes carry a low boom under the tutti, with the 100-250 Hz body thinner than in a recording.

**Evidence (measured, `lowpow.py`, 2 s blocks split into loudness thirds; band power relative to 250 Hz-2 kHz):**

| | 30-60 | 60-100 | 100-250 |
|---|---|---|---|
| Dvorak, soft third | -26.4 | -14.7 | -8.4 |
| c20, soft third | -24.6 | -15.9 | -4.2 |
| Dvorak, loud third | -40.8 | -21.0 | -4.5 |
| c20, loud third | -30.4 | -13.5 | -6.5 |
| Dvorak, loudest 10% | -40.6 | -23.2 | -3.9 |
| c20, loudest 10% | -31.2 | -13.4 | -6.5 |

- Soft passages: within 1.2 dB of the reference at 30-100 Hz. Loud passages: 7.5-10 dB over it at 30-100 Hz and 2-2.6 dB under it at 100-250 Hz.
- The Dvorak is in E minor (E1 41 Hz, E2 82 Hz), so its bass fundamentals fall in the same two bands. The key does not explain a 7.5 dB difference that only appears when the music is loud. The Brahms references cannot be used below 100 Hz, because both have a peak in the 62.5 Hz third-octave that stands 2 dB over 1 kHz (mains hum, inferred).
- The Cb's own tone is not the cause. Its fundamental falls relative to harmonics 2-4 as CC11 rises: -5.9 dB below CC 50, -8.6 dB above CC 100 (`cbharm.py`). So the low end in the loud passages is a matter of the Cb's level at 30-100 Hz against the tutti.
- Per climax window (`cbsim.py`), master 60-100 Hz relative to 250 Hz-2 kHz: bars 60-62 -12.7, bars 78-80 -11.1. Its strongest low bin in both windows is 69 Hz (Db2). The current `loud_eq` (80 Hz low shelf -3 dB, ramps 199-201 and 257-259) does not reach bars 54-59 or 75-78, and takes only 1-2 dB off 60-100 Hz.

**Simulation (`cbsim.py`, the c20 Cb stem re-equalised per 2 s block, master = rest + new Cb), 30-60 / 60-100 / 100-250 relative to 250 Hz-2 kHz:**

| | soft third | loud third | loudest 10% |
|---|---|---|---|
| c20 | -24.6 / -15.8 / -4.1 | -30.4 / -13.6 / -6.5 | -31.2 / -13.4 / -6.5 |
| 100 Hz -6 dB, wider ramps | unchanged | -32.2 / -16.1 / -6.8 | -34.0 / -16.2 / -6.8 |
| 110 Hz -8 dB, wider ramps | unchanged | -33.2 / -17.5 / -7.0 | -35.8 / -18.0 / -7.1 |

**Fix:** `build/mix.json` "Double basses" `loud_eq`:
- `points` [[190,0],[200,1],[214,1],[216,0],[254,0],[259,1],[269,1],[271,0]]. The current points are [[199,0],[201,1],[213,1],[215,0],[257,0],[259,1],[268,1],[270,0]].
- `bands`: lowshelf 80 Hz -3 becomes lowshelf 100 Hz -6. Keep the 150 Hz +4 dB bell (1 oct), which supports the 100-250 Hz body.
- Apply with `--mix-only`. It is a wet-automated ReaEQ, so the soft passages keep their sound.
- Try -6 first. Go to 110 Hz -8 only if the check below still reads 60-100 Hz over -16 in the loudest 10%. The tonic Db2 should stay audible as the bass of the chord.

**Check (`lowpow.py` on the c21 master):**
- loudest 10% 60-100 Hz at -15.5 to -17.5. Soft third unchanged within 0.3 dB.
- 100-250 Hz in the loudest 10% no lower than -7.0.
- Cb stem f/ff medians (metrics.md) within 1.5 dB of c20, since RMS is dominated by the fundamental. The pitch definition at 120-400 Hz is unchanged.
- Limiter and mp3 LRA within 0.3 of c20.

## 3. The pizzicato basses under the flute solo (bars 37-44) are the most bass-heavy passage of the movement. Each pizz. note is almost pure fundamental. Measured; effect inferred.

**Where:** Double basses pizz., p, qn 108-140 (bars 37-44). Score page 4: flute solo p, Vc/Cb pizz., Db2 / Bb1 / Gb1 / Eb2 (46-78 Hz fundamentals).

**What is wrong:** master 60-100 Hz relative to 250 Hz-2 kHz is -6.8 dB over bars 37-40 (`cbsim.py`). Per bar (`lowbars.py`, 20-100 Hz): bar 39 -5.2 and bar 41 -8.4. Only bar 21 is higher in the movement. The c20 median across all soft blocks is -21.8 and the Dvorak soft median is -17.8 (`lowdist.py`). The Cb supplies 95-99% of it. Effect (inferred): on headphones each pizz. is a low thump at nearly the power of the flute's tune (bar 39: Cb 60-100 Hz -51.2 dB, flute 250 Hz-2 kHz -49.3 dB; `pizz.py`), more felt than heard as pitch.

**Evidence (measured, `pizz.py`):** the Cb pizz. stem has 60-100 Hz 8-14 dB over its own 120-400 Hz in bars 37-43 (10.2, 7.9, 9.1, 14.5, 10.8, 9.9). For the arco notes, the fundamental sits 6-9 dB under harmonics 2-4 (`cbharm.py`). The Vc in the same bars has 18-32 dB less at 60-100 Hz. Bar 38 is the exception, where the two are level. The c15 Cb pizz. role (2) and the c20 `METRIC_DB` steps set the level and the downbeats. Both are right and stay as they are; what needs changing is the spectrum.

**Fix:**
- `tools/build_reaper.py` `mute_lua`: accept `loud_eq` as a list of specs (`for le in (v if isinstance(v, list) else [v])`). Each spec becomes its own wet-automated ReaEQ, because `set_wet_eqs` already takes a list.
- `build/mix.json` "Double basses": add a second spec `{"points": [[107.5,0],[108,1],[139.5,1],[140,0]], "bands": [{"band": "lowshelf", "hz": 90, "db": -5}]}`.
- `--mix-only`.

**Check:**
- bars 37-44 master 60-100 Hz relative to 250 Hz-2 kHz at -11 to -13 dB
- Cb 120-400 Hz per bar unchanged within 0.3 dB
- `metric2.py` Cb downbeat step unchanged within 0.5 dB

## 4. The winds, the brass and the close-only divisi tracks are near-mono points (250 Hz-4 kHz corr 0.7-0.9), so the master's mids stay at 0.61 against 0.48-0.52 in the references. Measured; fix simulated; it has a cost in pan spread.

**Where:** all wind and brass tracks; Violins II div (bars 37-40), Violas div (bars 23-30 and 84-86), Violoncellos div (bars 17-22). Open since c17 ("mid corr 0.61, target 0.55").

**What is wrong:** 250 Hz-4 kHz corr per stem (`bands.py`, `midcorr.py`):
- Violin I section: 0.41; Vln II 0.63; Violas 0.68
- Flute 1 0.74, Oboe 1 0.76, BCl 0.90, Bn2 0.68, Cbn 0.76
- Tbn1 0.80, Horn 4 0.81
- the DIV patches 0.83-0.88

The divisi patches have only one mic. Their samples are in `HS Dv` folders with no Main or Surround (`/Volumes/MAC DRIVE/EW Hollywood Strings Diamond/Hollywood Strings Samples/*/HS Dv*`), and they are fully mono above 6 kHz (corr 0.99-1.00, because the hall is cut at 5.5 kHz). In bars 23-30, Violas div is 1.6 dB louder than the Violas section (`divtone.py`), so half of the viola line comes from a narrower, closer image than the other half.

Effect (inferred): the solo winds and horns sound like panned close mics placed in front of the hall, not like players heard through it. The divisi halves do not merge with their sections.

The depth is not the problem. Tail drops of the divisi tracks match their sections within 2 dB (Violas 10.1/18.3/24.0, Violas div 10.8/16.2/24.6 at 0.2/0.4/0.7 s), so a larger send would not help.

**Simulation (`finalsim.py`, `widesim2.py`):** a side-channel high shelf at 250 Hz on the listed tracks, together with finding 1:

| | corr whole | <250 | 250-4k | >4k | side/mid | pan std | centre two bins |
|---|---|---|---|---|---|---|---|
| c20 | 0.631 | 0.754 | 0.611 | 0.496 | -6.4 | 0.323 | 46% |
| finding 1 alone | 0.598 | 0.608 | 0.607 | 0.496 | -6.0 | 0.333 | 43% |
| + winds/brass +1, no div | 0.566 | 0.603 | 0.568 | 0.486 | -5.6 | 0.343 | 41% |
| + winds/brass +1.5, div +3 | 0.548 | 0.600 | 0.545 | 0.481 | -5.3 | 0.348 | 40% |
| + winds/brass +2, no div | 0.528 | 0.597 | 0.522 | 0.474 | -5.1 | 0.353 | 40% |

- Per stem at +1.5 / +3:
  - Flute 1 0.74 -> 0.65, Oboe 1 0.76 -> 0.67, Horn 1 0.49 -> 0.34, Tbn1 0.80 -> 0.73
  - Vln II div 0.84 -> 0.71, Vla div 0.83 -> 0.71
- Seats move by at most 0.6 dB (Oboe 1 R-L +3.1 -> +3.6, Tbn1 +4.2 -> +4.8, Vln II div -2.9 -> -3.8).
- The cost: the pan-spread metric rises 0.323 -> 0.348 against 0.31-0.32 in the references. Even a pure decorrelation (`itdsim.py`) raises that metric, so part of this is how the metric is built, but the centre share does fall. That is why I propose +1.5 and not +2.
- An inter-channel delay (ITD) instead is not usable: 0.6 ms gave >4 kHz corr -0.09, a comb filter on a mono fold.

**Fix:**
- `tools/build_reaper.py` `set_side_shelf` / `side_lua`: accept `side_shelf` as a list of bands and pass them to `config_eq`, which already handles `lowshelf` (band 0) and `highshelf` (band 3). Keep the single-dict form working.
- `build/mix.json`:
  - every wind and brass track (Fl1-2, Ob1-2, CA, Cl1-2, BCl, Bn1-2, Hn1-4, Tbn1-2, Horns 1-2 a2): `"side_shelf": [{"band": "highshelf", "hz": 250, "db": 1.5}]`
  - Contrabassoon, Bass trombone, Tuba: `[{"band": "lowshelf", "hz": 200, "db": -2}, {"band": "highshelf", "hz": 250, "db": 1.5}]`
  - Violins II div, Violas div, Violoncellos div: `[{"band": "highshelf", "hz": 250, "db": 3}]`
- `--mix-only`. This is exact on stems, so the actor can verify it on c20 before rendering.
- Leave Violin I solo out. It has no side signal above 6 kHz to raise, and its seat was set in c13.

**Check:**
- master corr 250 Hz-4 kHz 0.53-0.57 and >4 kHz 0.47-0.49 (measure.py)
- centre two pan bins 40% or more, pan std 0.35 or less
- each listed stem's R-L within 0.7 dB of c20
- mono-fold level of the master within 0.3 dB of c20 at 250 Hz-4 kHz

## Measured, no action proposed

- **High-band lean.** The master's top end leans left: R-L -4.7 dB at 2-6 kHz and -5.8 dB at 6-16 kHz, against Dvorak -3.6 / -2.3. Violins I supply 57% and 72% of those bands. With the violins on the left this is normal, and the 2-6 kHz difference is only 1.1 dB, so leave the seat at -0.55.
- **Horn tone.** The a2 horns (2FH Leg Slur) measure 5-8 dB more 2-5 kHz relative to 0.5-1.5 kHz than Horn 4 (1FH Sus) at the same pitch and CC 88 in bars 78-80. Horn 1's own notes spread over 20 dB on this measure, so this is not evidence of a mismatch between the sample sets.
- **The divisi and solo tracks above 6 kHz** stay mono whatever the mix does: one-mic samples under a hall cut at 5.5 kHz. Their energy there is under 1% of the band.

## Do not touch

- The true-stereo hall, its `fx_volume` 0.19, pre-delay 0.0303 and 5.5 kHz high cut (RT60 2.59 s, tails consistent across families).
- The group sends and the Close/Main columns: strings default 0.66/1.0, winds 0.5/0.8, horns 0.5/1.0, Cb 0.6/1.0, tuba 0.45/1.0, timpani 0.2/0.5, harp 0.6/1.0. Leave Surround and Mid unloaded.
- Every seat and width. The harp side shelf at 300 Hz -8 and width 0.3 (harp 120-250 Hz corr 0.66, mono loss 1.0 dB).
- The soft-passage low end (within 1.2 dB of the reference).
- The Cb 150 Hz bell, the Vc `loud_eq`, `METRIC_DB`, and the Cb pizz. role.
