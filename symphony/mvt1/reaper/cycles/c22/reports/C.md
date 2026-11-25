# Cycle 22, critic C: dynamics over time (render c21)

Lens: hairpin and phrase shapes; the loudness arc against the score (bars 121-126 with the tam-tam, the fff at 160 after the cymbal roll, the recapitulation at 131, the ppp coda); loudness range of the master and the mp3 (BRIEF item 6); swells and loop pulsing on held notes (item 7); decays; comparison with real recordings.

## Method

- Material: the stem-fixed c21 render (`cycles/c21/render/`; the float sum of the 33 stems equals `00_Master.wav` to -159 dB), `mvt1-mockup-c21.mp3`, and `build/parts.json` (02:34, the stem-fixed state). c21 is on the plain parts.json tempo map (no render shift).
- Loudness: ffmpeg ebur128 at 10 Hz, M shifted 0.2 s and S 1.5 s to centre them. Stem levels are plain stereo power in 10 ms frames.
- Simulations: piecewise dB shapes applied to the c21 stems and summed (`simshape.py`), then a copy of `tools/deliver_master.py` (`dmx.py`, and `dmy.py` with the change in finding 3). With no shapes the chain reproduces c21 exactly (LRA 14.4 LU, span 19.0 dB, limiter 2.0 dB).
- Scripts in `/private/tmp/claude-501/mockup-loop/mvt1-c22-C/`: the c18-C battery pointed at c21 (`bars.py`, `hp.py`, `hptrack.py`, `hpexp.py`, `arr.py`, `swell.py`, `loops2.py`, `climax.py`, `ev4.py`, `evalm.py`); new: `beats.py`, `fine.py`, `fam.py`, `win.py`, `cmpc.py` (one stem across cycles), `holes.py` (post-attack holes on loud long notes), `lowshare.py`, `ttb.py` (tam-tam bands over time), `lm.py` (master loop check), `rank.py` (delivered momentary ranking and ride gain), `dmy.py`, `acc/acc25.py` (item 8).

## State of the arc (measured)

- Master -16.4 LUFS, LRA 22.6 LU. Bar level against the bar's loudest printed dynamic: r = 0.886 (c17 0.885).
- Delivered: -19.8 LUFS, LRA 14.4 LU, p10-to-max span 19.0 dB, limiter 2.0 dB, -1.7 dBTP. 268 five-second moves: median share kept 0.79, 0 inversions. All inside the BRIEF item 6 targets.
- Climax order holds. Delivered S max: 160 -10.04 > 122 -11.47 > 167-170 -13.09; M max 160 -9.45, 122 -10.50. Bar 160 arrives +2.0 dB (master M) over the last beat of the bar-159 crescendo; bars 160-161 hold within 1 dB; 162-164 fall 14.3 dB.
- Bar 121 crescendo +2.3 dB, fff arrival at 484 +2.0 dB over its last beat. Bars 124-126 fall smoothly, -14.1 -> -30.5 dB per beat. The tam-tam fff blooms in 2-12 kHz within 0.25-0.5 s and holds to about 2 s, then fades (2-5 kHz 17 dB under the master by 4 s); the damp at 504 is in place.
- Recapitulation, bar 131: the downbeat steps +2.9 dB over 519-520, then bars 131-134 sit at -15.9..-16.9 dB per bar (M power), within 1 dB of the exposition ff (bars 27-31, -14.6..-15.6). No change proposed.
- Coda: the pp chorale 175-178 holds -34.3..-34.9; 179-180 -36.7; the bar-181 decrescendo and the ppp morendo fall steadily (master 724 -43.3, 726 -46.1, 727 -48.7, release reaches -68 at 728). The fermata rest at 679 decays 50 dB in 2.2 s.
- Per-track hairpins: 429, of which 52 move less than 1 dB the printed way (c17: 55); crescendo median +4.8, decrescendo median -5.3 dB.
- Against the recordings (S distribution; recordings from `symphony/render/critics/c00/ref_*`):

  | | p50-p10 | p90-p50 | p99-p90 | max-p95 |
  |---|---|---|---|---|
  | Brahms 1/i | 11.2 | 6.7 | 2.2 | 2.6 |
  | Brahms 4/i | 7.6 | 5.0 | 3.1 | 3.8 |
  | Dvořák 9/i | 11.7 | 12.4 | 1.5 | 1.6 |
  | c21 master | 8.5 | 12.7 | 6.7 | 5.7 |
  | c21 delivered | 4.9 | 7.8 | 5.1 | 4.6 |

  The two fff climaxes stand 2-3 times further above the other loud passages than in the recordings, and the delivered soft half is squeezed. c18-C showed the ride parameters cannot open the soft half inside the 19 dB span; this is a composed single climax, so I propose no change beyond finding 3.
- Item 7 (measured): master 100-300 Hz / centroid autocorrelation at 3.95 s: Lento 5-12 +0.05/0.00, bars 43-46 +0.05/+0.26, coda 175-178 +0.05/+0.14, Tempo I 179-182 -0.14/-0.03, 122-126 -0.12/-0.06, 73-76 +0.26/+0.30 (two Allegro bars are 3.81 s, so this is rhythm). Held-note flags over 0.35 are masked stems or merged repeated notes (Bassoon 2 476 and Bass clarinet 464, 18 dB under the master in the fff), as in c18. Passes.
- Item 8 (measured): 2-5 kHz first 80 ms minus body: strings n 171 median -9.0 / p90 -3.9, winds 234 -11.3 / -5.5, brass 172 -10.3 / -4.6, timpani -11.0. Only Violas 536 (+8.2, known, masked). Passes.

## 1. Bar 122, the fff downbeat of the sostenuto climax: the celli drop out for 0.8 s right after the attack, a 19 dB hole that takes 6 dB out of the master's 100-250 Hz (measured)

**Where.** Violoncellos, qn 484.0 (bar 122 beat 1), fff whole note A-flat3 under the tam-tam stroke.

**Evidence (measured).**
- Celli per eighth-qn from 484: -15.3 -18.1 -19.9 -24.3 -28.0 -31.6 -33.3 -31.5 -34.0 -33.5 -30.5 -31.4 -29.7 -28.1 -24.7 -21.2, then -21.9..-20.4 from 486. The note's body sits at -21; for 484.4-485.6 it is 10-13 dB under its body and 19 dB under its attack.
- Cause: the note is the first note of a Leg Slur MAX phrase directly after the measured-tremolo Stac strokes (ks: `Stac RRx9` to 483.69, `Leg Slur MAX` at 483.94). A Leg Slur first note after a short note plays the slow first-note layer (LEARNINGS section 5/6). The envelope does not cause it (vol +0.04 -> +1.47 dB over 484-484.5, CC11 124-127).
- `holes.py` over every string, wind and brass note of 1.6 s or longer at velocity 100+: this is the only post-attack hole over 9 dB in the movement.
- The same hole is in c15, c18, c19, c20 and c21 (within 1-3 dB; c13 and c17 had a 10 dB version), so it is not round-robin luck.
- Effect on the master, 100-250 Hz band (celli A-flat3 and its octave): 484.0 13.6 dB, 484.5 7.6, 485.0 12.7, 486.0 14.9. Celli re master in that band: -7.4 at the attack, -12.8 in the hole, -2.3 at 486. The tenor of the fff chord thins for half a beat right after the climax stroke (listener effect inferred).
- Precedent: the same Leg Slur first-note sag at the Allegro's first downbeat (qn 56) and at the bar-160 fff downbeat (636) was fixed with `DOWNBOW_STROKE_AT` strokes (c06 A #1, c16 C #1).

**Fix.** `build/score_config.py`: add 484.0 to the celli strokes, e.g. after the line-1084 block:

```python
DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{"Violoncellos": DOWNBOW_STROKE_AT["Violoncellos"] + [484.0]})
```

The stroke plays Sus MAX at v127, and the bar-123 note (sq 488, now a Leg BC MAX target at 487.78) joins it through the existing "stroke into the note after it" path. MIDI change on one track; `--midi-only` rebuild of Violoncellos. After the render, compare the celli 484-488 body with c21's 486-488 level (-21..-22 dB per eighth-qn) and stem-fix any difference (c21's 607 stroke needed +5 dB on the body). Check its 2-5 kHz front against item 8.

**Criterion.** Celli 484.25-486.0: no eighth-qn window more than 6 dB under the 486-488 median. Master 100-250 Hz at 484.5 within 3 dB of 484.0. Master M at 484-485 within 0.5 dB of c21 (the limiter peak is at 484.53).

## 2. Bars 122-123: the fff sostenuto loses 2.8 dB before its printed decrescendo; brass fall 3-7 dB inside the held chords (measured, simulated)

**Where.** qn 484-492: bar 122 fff, bar 123 sostenuto (fff, new chord), decrescendo only from bar 124 (page 11 of the score).

**Evidence (measured).**
- Master M per beat 484-491: -7.5 -7.4 -8.7 -9.6 | -9.0 -9.3 -9.8 -10.3. Delivered: -10.7 -10.6 -11.8 -12.6 | -11.9 -12.1 -12.5 -12.9.
- Family power per beat: brass -13.9 -14.3 -14.9 -17.1 | -15.8 -15.7 -16.4 -17.3. Horns 1-2 fall 7 dB from 484.4 to 485.75 (-20.6 -> -27.5) inside their fff whole notes; strings and winds fall about 1-2 dB.
- c18-C found a horn-only hold moves the master 0.2 dB: the sag is shared. A held fff chord with a tam-tam bloom under it should not fade before the printed decrescendo (inferred).

**Fix (level-only, stem fix can apply it).** `build/score_config.py`, `LEVEL_SHAPES`, the same shape on every wind, brass and string track (not Timpani, percussion or Harp; the timpani roll keeps its settle):

```python
_sost = [(485.5, 0.0), (486.5, 0.8), (487.0, 1.5), (487.8, 1.5), (488.1, 0.5), (489.0, 0.8), (490.5, 1.2),
         (491.75, 1.5), (492.25, 0.0)]
for tn_ in [t_[0] for t_ in TRACKS if t_[0] not in ("Timpani", "Tam-tam", "Suspended cymbal", "Crash cymbals", "Harp")]:
    LEVEL_SHAPES[tn_] = LEVEL_SHAPES.get(tn_, []) + [_sost]
```

(`TRACKS` holds tuples with the name first, Horns a2 included.) The shape starts after `ARRIVAL_WEIGHT_AT` 484's 0.5 qn and after finding 1's stroke attack. It ends as the bar-124 decrescendo starts.

**Simulated (`s2`).**

| | 484 | 485 | 486 | 487 | 488 | 489 | 490 | 491 | 492 |
|---|---|---|---|---|---|---|---|---|---|
| master c21 | -7.5 | -7.4 | -8.7 | -9.6 | -9.0 | -9.3 | -9.8 | -10.3 | -14.1 |
| master fix | -7.5 | -7.2 | -7.9 | -8.6 | -8.3 | -8.3 | -8.6 | -9.2 | -14.0 |
| delivered c21 | -10.7 | -10.6 | -11.8 | -12.6 | -11.9 | -12.1 | -12.5 | -12.9 | -16.3 |
| delivered fix | -10.9 | -10.6 | -11.2 | -11.8 | -11.5 | -11.4 | -11.5 | -12.0 | -16.5 |

- Whole file: LRA 14.4, span 19.0, limiter 1.9 dB, 0 inversions.
- Climax margin: delivered S 160 -10.13 > 122 -11.19 (0.94 dB; c21 1.43), M 160 -9.52 > 122 -10.40. A +2.5 dB version (`s1`) brought the margin down to 0.75 S / 0.43 M, so do not go higher than this shape.

**Criterion.** Master M over 484-492 falls at most 1.8 dB before 492; delivered S 160 at least 0.8 dB over 122; limiter not above 2.0 dB.

## 3. The delivery ride lifts short ff stabs by the lift of the soft music around them: the bar-33 stab is the 4th-loudest moment of the mp3 and bar 41 plays louder than letter G (measured, simulated)

**Where.** `tools/deliver_master.py`. Short loud events beside soft passages: bar 33 (B: one ff eighth chord, then the bassoon solo), bar 32, bars 40-41 (the transition peak before the bar-41 decrescendo), bar 83, bar 143.

**Evidence (measured).** Delivered minus master momentary max (dB): bar 160 -3.9, 122 -3.2, 117 -2.5, but bar 33 -0.2, 32 -0.3, 83 -0.5, 41 +0.7, 40 +0.6.
- The stabs get 2.5-4.6 dB more gain than the climaxes. Delivered M ranking: 160 -9.45, 161, 122 -10.50, then bar 33 -11.05, ahead of 170, 159, 26, 123, 121. On the master bar 33 is 5.3 dB under 160 and 3.5 under 122.
- Bar 41 delivers at -12.25, louder than letter G's ff arrival bar 117 (-13.39); on the master it is 2.0 dB under it. The ride reverses the order of two ff points.
- Cause: the slow lift and `FAST_CAP_ABOVE` both read short-term loudness S (3 s window). A 0.3 s stab barely moves S, so the stab inherits the lift computed for the soft bars on each side (ride at qn 128: +1.8 dB; at qn 160: +2.5; at 636: -1.5).

**Fix.** In `deliver_master.py`, after the `FAST_CAP_ABOVE` block, add a cap read from momentary loudness (scratch `dmy.py` has the tested code):

```python
MOM_CAP_ABOVE, MOM_CAP_SMOOTH_S = 6.0, 0.5
Mo = momentary(SRC)   # ebur128 lavfi.r128.M at 10 Hz, same parsing as short_term(); shift 2 frames (0.2 s) to centre
Mo = np.concatenate([Mo[2:], np.full(2, Mo[-1])])[:len(S)]
Mmax = np.lib.stride_tricks.sliding_window_view(np.pad(Mo, (5, 5), mode="edge"), 11).max(axis=1)   # +-0.5 s
mcap = np.clip(knee + MOM_CAP_ABOVE - Mmax, 0, CAP_DB)
lift = np.minimum(lift, smooth(np.minimum(lift, mcap), MOM_CAP_SMOOTH_S))
```

It caps the lift so that no momentary peak is lifted above knee + 6 dB, and leaves passages whose momentary level stays under that untouched.

**Simulated on c21 (`v2`).**

| Bar | 32 | 33 | 40 | 41 | 83 | 116 | 117 | 122 | 160 |
|---|---|---|---|---|---|---|---|---|---|
| Delivered M max, c21 | -11.46 | -11.05 | -12.76 | -12.25 | -12.04 | -14.00 | -13.39 | -10.50 | -9.45 |
| Delivered M max, fix | -12.78 | -12.40 | -14.16 | -13.66 | -13.25 | -14.00 | -13.39 | -10.50 | -9.45 |

- Bar 33 moves from 4th to 10th. Bars 40/41 fall back under 116/117, as on the master.
- Whole file unchanged: LRA 14.4, span 19.0, limiter 2.0 dB, 0 inversions, median share 0.79 -> 0.78.
- The gain differs from c21 by more than 1 dB only at qn 127.2-129.9, 159.4-161.7 and 330.2-331.9 (at most -1.6 dB). The bassoon solo after B is 0.6-0.9 dB lower in its first beat and identical from 130.5.
- Combined with finding 2 (`v3`): S 160 -10.0 > 122 -11.1, LRA 14.4, span 19.0, limiter 2.0.

**Criterion.** No bar outside 121-123, 158-161 and 167-170 among the 8 loudest delivered M maxima; delivered bar 41 under bar 117; LRA, span, limiter and inversions unchanged.

## 4. Bar 19-20: the first violins' crescendo to the sf at 78 is flat for five beats (measured)

**Where.** Violins I, qn 72.5-78 (cresc from f into sf at 78), the Allegro theme's second phrase; the stem is 5 dB under the master and level with the celli.

**Evidence (measured).**
- Violins I per half-qn: 73.0 -31.9 (accent), then 74.0-77.5: -33.4 -33.8 -33.3 -34.3 -32.3 -32.9 -33.5 -32.7, then 78 -29.0. The hairpin measures 0.0 dB (`hpexp.py`).
- CC11 rises 89 -> 101, but the line descends (E6 -> C#6 -> E6), and the envelope falls from the accent body at 73 (+4.8..+5.2 dB to 73.75) to +1.4 at 75.0, rising only to +2.3 by 77.
- Master over the same beats: -28.2 -27.0 -27.7 -29.5 -27.8 -26.9 -27.1 -27.8, then -25.4.

**Fix (level-only).** `LEVEL_SHAPES["Violins I"]` add `[(74.25, 0.0), (77.75, 2.0), (78.0, 0.0)]`. It leaves the 73 accent fit (`accent_fits.json` "73": 4.5) as it is.

**Expected (stem arithmetic).** 74.0-74.5 -33.4 -> 77.5 -30.7: the crescendo grows +2.7 dB over its body. The sf step 77.5 -> 78 becomes +1.7 dB (was +3.7). The master gains about +0.8 dB at 77.5 (inferred from the stem's share).

**Criterion.** Violins I 77.0-77.75 at least 2 dB over 74.0-74.75, and 78.0-78.5 still over 77.5-78.0.

## Measured, no change proposed

- Second-theme swells (bars 47-52, 147-155). Some per-track swells are still flat: Horn 1 589-591 -1.4 dB on one half note, celli 196-203 ±0.1. The master swells are +0.2..+3.8 dB. They are inside the c12/c16 set (do not touch) and move 1-2 dB between renders.
- Coda contrast. The mp cello solo of 171-174 against the pp chorale 175-178 is 4.1 dB on the master and 1.4 dB delivered. Each chorale stem sits at its own pp median (-45..-50 dB); there are ten of them. This is the ride limit c18-C measured, not the mix.
- Violins I bar 145 pp held G4 rises 6-8 dB unmarked under the oboe's dolce entry. It stays 8 dB under the oboe.

## Do not touch

- The delivery settings: RATIO 2.5, CAP 10, 3 s smoothing, TOP_RATIO 1.6, FAST_CAP_ABOVE 4. Finding 3 only adds a cap.
- Climax order 160 > 122 > 167-170, and `ARRIVAL_WEIGHT_AT` 484/636.
- The bar-121 shape and the letter-G hold.
- The 636 strokes and E6 fill, and the morendo shape 724-729.
- The tam-tam damp at 504 and its 86 Hz bell. The timpani roll settle with the c21 +3 tutti roles.
- The c12/c16 second-theme shapes.
- AUTO_REBOW rows, _REBOW_FROZEN and the c21 basses/violas rebow fills (item 7 passes on the master).
- GENTLE_ACCENT / ACC_ART_LEAD with the accent fits (item 8 passes).
- sus_release_cap_ms (the fermata and cut-off decays stay natural: 50 dB in 2.2 s at 679).
