# Cycle 16, critic C: holistic comparison (render c15)

## Method

I compared the c15 render (`cycles/c15/render/`, `cycles/c15/rendered_build/parts.json`) with three others: c00, c10 (five cycles back) and the Dvořák 9/i reference (`symphony/render/assets/refs/dvorak9_i_columbia.mp3`, decoded to 48 kHz). I also measured the delivered `mvt1-mockup-c15.mp3`.

Cross-cycle note timings use each cycle's own tempo map:
- c08 and c11-c15: their `rendered_build/parts.json`;
- every other cycle: `cycles/c(N+1)/before/parts.json`;
- c00-c02: additionally passed through `tools/rendermap.wrap`.

Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c16-C/`:
- `bars.py`, `ladder.py`: per-bar level against the printed dynamic;
- `solos.py`, `vs.py`: marked solos against their accompaniment;
- `feat.py`, `tilt.py`: level-binned band shares and stereo, against the reference;
- `accfront.py`, `onsetshape.py`: accent fronts;
- `loopchk.py`, `loopmaster.py`: brief item 7;
- `rr.py`, `alt.py`: round-robin repetition;
- `decay.py`: room decay;
- `dm.py`: a parameterised copy of `deliver_master.py`, writing only to scratch.

Levels are RMS dB unless stated otherwise.

## What has improved and what passes (measured)

Since c00 the loop has worked at note level, and the macro shape of the movement has barely moved. Bar levels at c15 are within 2 dB of c00 in 150 of 182 bars.

What changed is inside the bars:
- accents;
- joins and entries;
- tempo arcs;
- timpani;
- re-bows.

**Brief item 7 (loop pulse).** Master autocorrelation at 3.95 s, 100-300 Hz band / spectral centroid:

| Passage | Band | Centroid |
|---|---|---|
| Lento 5-12 | -0.06 | +0.04 |
| bars 43-46 | -0.21 | +0.04 |
| coda 175-178 | -0.10 | +0.08 |
| Tempo I 179-182 | -0.36 | -0.10 |

On the final chord every string stem is between -0.15 and +0.13. No single note longer than 8 s is left except two tam-tam notes and Bassoon 2 at 476, all at or under +0.04. Passes.

**Brief item 8 (accents).** 2-5 kHz in the first 80 ms minus the 0.12-0.4 s body:

| Family | Median | p90 |
|---|---|---|
| Brass (n 145) | -6.2 | +0.7 |
| Winds (n 220) | -6.3 | +1.0 |
| Strings (n 192) | -9.2 | -2.9 |

The outliers are the second of the repeated accented quarters at qn 125: Hn2 +7.1, Fl1 +8.3, Vln I +5.5 on the stems. On the master, qn 125 is -9.0 at 2-5 kHz, so these are masked.

I also detected onsets the same way on the master and on the reference. The first 60 ms minus the body is -0.3 dB for c15 and -0.4 dB for Dvořák. Passes.

**Room.** After the bar-170 fermata the master reaches -10/-20/-30 dB at 0.13/0.42/0.89 s. The reference's tutti stops reach those levels at 0.08-0.14/0.35-0.43/0.52-0.66 s. The decay is close; the mockup's tail is slightly longer.

**Delivery.** The delivered file meets its targets:
- LRA 14.5 LU;
- span 19.1 dB;
- limiter 2.0 dB;
- climax momentary maximum: bar 160 -13.9 > bar 122 -14.7 > bar 169 -19.4.

## 1. Bar 121: the printed crescendo into the first fff is cancelled, so the fff at bar 122 arrives as a 5 dB jump (measured)

**Where.** Bar 121, qn 480-484. Fifteen staves are marked cresc from ff; fff at 484, allargando.

**What is wrong.** Master level (qn ranges):

| | Bar 120 (476-480) | Bar 121 first half (480-482) | Bar 121 last beat (483-484) | Bar 122 beat 1 (484-485) | Rise inside bar 121 | Step at 484 |
|---|---|---|---|---|---|---|
| c00 | -18.9 | -17.8 | -16.2 | -13.9 | +2.8 | +2.3 |
| c05 | | | | | +4.8 | +2.4 |
| c10 | | | | | +3.0 | +4.2 |
| c15 | -17.8 | -18.0 | -16.7 | -11.5 | +1.2 | +5.2 |

So the bar marked crescendo now starts *quieter* than the ff bar before it. The fff then switches on as a terrace instead of being reached. The second fff, at bar 160, is reached properly: bar 159's crescendo rises +2.2 dB and the step is +2.1.

**Cause (measured in the data).** The c14 critic C #4 shape in `build/score_config.py` (the loop after "the ff after letter G (bars 118-120) sagged") raises ten held ff parts +2.5 dB over 468.6-479.6 and takes them back to 0 dB at 480.4:
- Horn 3, Horn 4, Horns a2;
- Bass trombone, Tuba, Contrabassoon;
- Violins II;
- Bassoon 1, Bassoon 2, Bass clarinet.

The return lands exactly at the start of the printed crescendo, and the -1.5 dB `ARRIVAL_WEIGHT_AT` hold-back at 484 removes the last half beat of it as well.

**Fix.**
- `build/score_config.py`, the c14 loop over those ten tracks: change the shape to `[(467.6, 0.0), (468.6, 2.5), (479.6, 2.5), (483.5, 4.0), (484.0, 0.0)]`. This holds the letter-G lift and adds +1.5 dB through the crescendo.
- `ARRIVAL_WEIGHT_AT[484.0]`: change from `(-1.5, 1.5, 0.5)` to `(-0.5, 1.5, 0.5)`.
- The Double basses shape in the same block already holds +3 to 483.6. Keep it.
- Targets:
  - master bar 121 last beat 3.5-4.5 dB over bar 120;
  - step at 484 2-3 dB;
  - bar 122 itself unchanged, so 160 > 122 is kept;
  - check the delivery limiter (master peak at 484-486).

## 2. Soft exposed solos are covered by their own accompaniment, mostly by the soft-trimmed basses (measured)

**Where.** The places where one wind or horn has a marked solo at p/mp over pp/p strings.

**Evidence.** Solo minus the power sum of every other stem, per 1-2 qn window:

- **Cor anglais, p espr., bars 5-6** (qn 19-24, strings pp).
  - c00: +3.8 / +2.8 / +2.0 dB.
  - c15: -0.1 / -0.6 / -0.5 dB.
  - The basses (pp) are only +1.2..+4.4 dB under it (c00 +6.0..+8.3).
- **Horn 1 "1." solo mp > p, bars 13-14** (qn 49-55, strings p > pp).
  - c15: -4.7, -1.6, -5.0, -6.8, -4.9 dB.
  - The basses are louder than the horn at qn 52 and 54 (-0.8, -6.6).
- **Oboe 1 dolce p, bars 145-146** (qn 579-581, strings, clarinets and horns pp).
  - c00: +2.2 / +6.6 / +6.0 dB.
  - c10: -6.7 / -1.8 / -0.2 dB.
  - c15: -5.7 / -1.7 / -0.5 dB.
  - The c00 oboe stood +12.5..+12.8 dB over the basses; c15 is +4.1. The `note_trims` +8 on 578 covers only the first note (g').
- **Cor anglais p espr. against the celli mp espr., bars 171-174.** The CA median is 5.2 dB under the celli (7.9 at qn 685). Printed p against mp suggests about 2-3 dB. This is the only one of the four that is better than c00 (-10.3).

**Measured: the basses' soft level is the common factor.**
- The basses are the loudest stem in 9 of the 71 bars where they play p or softer: bars 5, 8, 9, 11, 13, 14, 76, 145, 175. c00 had 4.
- Their median margin to the loudest other stem rose from -7.9 (c00) to -4.8 dB.
- Their `soft_trim_db` is pp +10 / p +8 / ppp +8, against +7/+5 for the default and +5..+6 on the other strings.
- `deliver_master.py` then compresses everything under the knee 2.5:1. In the delivered file, p sits only 1.6 dB and pp only 3.5 dB under mf (density-corrected ladder, `ladder.py`). So the solo margin has to be made in the mix. I simulated the delivery parameters: KNEE_BELOW 8-14, RATIO 1.7-2.2, TOP 1.6-2.0. Widening the soft ladder by 1 dB costs 1.5-4 dB of span, which breaks the 16-19 dB target.

**Fix.** `build/roles.json`, keeping the c14 string soft trims (do-not-touch):

| Track | Roles to add | Note |
|---|---|---|
| Cor anglais | `[19.5, 27.0, 3.0, 0.5]` | |
| Horn 1 | `[48.5, 55.5, 3.0, 0.5]` | |
| Oboe 1 | `[578.5, 583.5, 4.0, 0.5]` | Keep the 578 note trim. |
| Cor anglais | `[683.0, 694.0, 2.0]` | On top of the existing +2.5/+1.5. |
| Double basses | `[16.0, 28.0, -3.0, 0.5]`, `[48.0, 56.0, -2.5, 0.5]`, `[576.0, 584.0, -3.0, 0.5]` | |

Targets:
- each solo at least +2 dB over the sum of the rest, and at least +5 dB over the loudest single accompanying stem, at its printed peak;
- the CA in bars 171-172 within 3 dB of the celli.

Do not lift the bars 7-8 CA, where the strings' printed < p > takes over while the CA falls to pp.

## 3. The loud tutti is brighter and thinner than a real orchestra, and has become brighter since c00 (measured; what the listener hears is inferred)

**Where.** Every f/ff/fff tutti. I used the level-binned frames, and also bars 26, 82-83, 122-123, 140, 158-161 and 167-170.

**Evidence.** Band share of total energy in 0.4 s frames, by level relative to the file maximum:

| | 2-5 kHz, -20..-12 | 2-5 kHz, -6..0 | 100-300 Hz, -20..-12 | 100-300 Hz, -6..0 |
|---|---|---|---|---|
| Dvořák | -12.6 | -11.1 | -8.3 | -6.5 |
| c00 | -13.4 | -12.2 | -7.3 | -9.5 |
| c10 | -12.7 | -9.5 | -7.3 | -9.1 |
| c15 | -12.5 | -9.8 | -7.1 | -9.0 |

- At mid level the mockup matches the reference.
- At the top, the 2-5 kHz share rises with level about twice as fast as in the reference. The upper band went from 1.1 dB darker than the reference (c00) to 1.3 dB brighter (c10/c15), following the c09 CC1 brass layers and the violin ff trims.
- In the reference, 100-300 Hz grows from mid to loud (+1.8 dB). In the mockup it falls (-1.9 dB).

Inside the loud bars:
- Violins I and II supply 26% and 23% of the master's 2-5 kHz.
- Strings as a family supply 52% and brass 35%.
- The 4-12 kHz left/right correlation is 0.57 against 0.39 in the reference: the highs are less diffuse.

Inferred: a hard, close, "sampled" edge in the tutti instead of a hall sound.

The lower band has no cheap fix. Critic B (c15 #4) simulated a 200 Hz bell on the trombones and horns: +0.4 dB. The celli already carry a +6 dB 150 Hz `loud_eq` over these spans. So reduce the top instead of adding more bass.

**Fix.**
- `build/mix.json` Violins I and Violins II: add a `loud_eq` spec with the celli's points and `{"band": "highshelf", "hz": 2500, "db": -2.5}`. The celli's points are 92-104, 108-128, 316-332, 456-496, 516-536, 548-568, 624-646, 660-680.
  - For Violins II, append it to the existing list. Its second-theme spec at 584-619 does not overlap.
- Estimated from the shares: master loud 2-5 kHz -9.8 -> about -10.8 dB (reference -11.1). The K-level drop on the violins is about 0.5 dB.
- Then re-check:
  - the Vln I tune margins in bars 27-31, 117-121 and 158-161;
  - the 2-4 dB accent rule on the violin accents in those spans (`accent_fits.json` refit for strings).

## 4. The second theme's first dolce horn note does not swell in either exposition or recapitulation (measured)

**Where.** Bar 47 (qn 184-187.5) and bar 147 (584-587.5). Horn 1 and celli are marked `c'2.~\<` to the eighth, then `\>`.

**Evidence.** Horn 1 stem, 0.5 qn windows from the onset:
- Exposition: -37.6 -36.3 -36.6 -38.9 -38.9 -37.0 -35.6 -36.6. From 184.3-185 to 186.5-187.5: +0.4 dB.
- Recapitulation: +0.2 dB (c10: -1.9 / -1.6).
- Master over the same span: +0.8 dB in the exposition.

The c10 `LEVEL_SHAPES` ramp (`for o_ in (0, 400)`: 0 -> +3.5 dB at 187.4, celli +3.0) is linear. The sample decays 2.3 dB in the middle of the note (185.5-186.5), so the ramp only offsets the decay, and the rise shows in the last 0.3 s.

This is the first sound of the second theme, and a horn player would make the < clearly heard.

**Fix.** `build/score_config.py`, that loop:
- Horn 1: `[(184.25+o_, 0.0), (185.0+o_, 1.5), (186.0+o_, 4.0), (187.4+o_, 5.5), (187.6+o_, 5.5), (187.85+o_, 0.0)]`.
- Celli: the same shape with peak +5.0.
- Target: the Horn 1 stem +3 dB from 184.3-185 to 186.5-187.5, and the eighth at 187.5 still over the 188 quarter (the decrescendo).

## 5. Smaller items

- **Basses, coda bars 167-169 (qn 664-676), 24 repeated C2 eighths on Sus MAX, f (measured; the cause, two alternating samples, is inferred).** The on-beat notes peak 36.3-36.5 and the off-beats 30.8-31.0 on the stem, every bar, since at least c10. 82% of n / n-2 pairs are within 0.3 dB; the other Cb repeated runs score 6-29%. On the master the tutti masks most of it (50-140 Hz on/off +1.3 dB, irregular), but it is the most machine-like pattern left on a stem. Fix: play every second note of that run on another short row, as the c15 celli `MEAS_TREM` `alt_row` does. Or put a -2 dB `LEVEL_SHAPES` step on the on-beat notes of 664-676, so the metric difference is about 2 dB rather than 5.
- **High-frequency space (inferred).** Reverb `high_cut_hz` is 5500 and the strings' hall send is only 0.25 (winds 0.35, trumpets 0.65). This fits the narrow 4-12 kHz image above. Do not change it before item 3 is measured, because a higher cut adds brightness.

## Do not touch

- The re-bow and loop work (brief item 7 passes everywhere);
- GENTLE_ACCENT and `accent_fits.json` (item 8 passes; master accent fronts match the reference);
- the delivery parameters (simulations show no better trade inside the span target);
- climax order 160 > 122 > 169 and the bar-160 arrival shapes;
- the c14 string soft trims (make item 2 with roles);
- the celli 150 Hz `loud_eq`;
- tempo arcs and ramps;
- the hall and IR.
