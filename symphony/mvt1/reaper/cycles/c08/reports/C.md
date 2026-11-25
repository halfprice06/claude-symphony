# Cycle 8, critic C: holistic comparison (render c07)

## Scope and method

I reviewed the stem-fixed c07 render (`cycles/c07/render/`, `metrics/`, `mvt1-mockup-c07.mp3`) against three baselines:
- cycle 0 and cycle 2 (five cycles back), each read on its own time map (c00/c02 via `before/parts.json` with the 1/6 qn shift, as `rendermap.py` does);
- the real recordings' loudness series (Brahms 1/i, 4/i, 1/ii, 4/ii Musopen, Dvořák 9/i) in `symphony/render/critics/c00` and `c04`.

Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c08-C/`:
- `dist.py`, `dist2.py`, `sect.py`: loudness distribution and per-section levels;
- `dynbar.py`: bar level against the printed dynamic;
- `tempo.py`: beats on the printed mark;
- `hp2.py`, `hpall.py`, `tutticresc.py`, `ptop.py`: hairpins and phrase tops;
- `dip.py`, `simclimax.py`: the climax approaches;
- `simdel.py`: a copy of `deliver_master.py` with a top ride, for simulation;
- `loop.py`, `timp.py`, `acc.py`, `sync.py`, `metric.py`: Dan's two checks, tutti sync, metric weight.

Levels are stereo power. Score qn maps to file time through the parts.json tempo map.

## c00 -> c02 -> c07 in brief (measured)

**What improved:**
- The tempo now moves inside the arcs: beats exactly on a printed mark 88% -> 73%.
- The timpani rolls no longer loop. Opening roll stem band autocorrelation at 3.95 s: 0.17 -> 0.15 -> -0.03; best lag 0.73 -> 0.15.
- The brass accents measure inside the brief:
  - on the master, 2-5 kHz over the first 80 ms minus the body is a median -7.4 dB (worst -1.0, qn 536);
  - the c07 fit put 33 of 36 accents at 2-4 dB over their neighbours.
- The ending is quieter but audible: delivered Lento 179-182 short-term max -8.7 -> -6.3 LU re integrated.
- The phrase tops are now slightly up: top note minus the rest -0.55 -> +0.7 dB.

**What has not moved or got worse:**
- The middle of the dynamic range: per-track step from mf to f 2.9 -> 2.3 -> 1.8 dB.
- The top of the range has grown away from the body:
  - master p50->max 19.0 -> 19.5 -> 20.7 dB;
  - delivered p75->max 9.6 -> 10.3 -> 10.6 dB.
- The two climax approaches do not crescendo (finding 1).
- The longest stretch of the movement still plays at one metronome value (finding 2).

**Dan's checks on the master, all held passages:**
- Loop (item 7):
  - band and centroid autocorrelation at 3.95 s is 0.28 or less everywhere;
  - the opening 0-16 reads +0.22 / +0.20 on the master, but the timpani stem is clean, so this comes from the low strings and bass clarinet;
  - the control (Allegro) reads -0.06.
- Accents (item 8): none is harsh.

Tutti entry spread (p10-p90) is a median 0.138 s, the same as c02.

## 1. The crescendos into both fff climaxes do not grow, because ARRIVAL_WEIGHT_AT holds back the whole crescendo bar (bars 121 and 159; every wind, brass and string track)

**Where.** Bar 159 (qn 632-636) is ff < into the fff of bar 160, the movement's main climax, with the suspended-cymbal roll pp <. Bar 121 (qn 480-484) is the allargando < into the fff of bar 122.

**Measured, master level (0.3 s windows):**
- Bar 159:
  - 630 -12.9, 631.5 -14.8, 632 -15.1, 633.5 -13.2, 635.5 -13.0 dB;
  - the crescendo bar ends 0.1 dB under bar 158's beat 3;
  - then the arrival comes at 636.5 -9.1.
- c02 rose to -11.1 at 635.5, 1.8 dB over its 630. On this passage c07 is worse than five cycles back.
- Shared hairpins of 5 or more tracks (`tutticresc.py`, last third minus first third):
  - 632-636 (29 tracks) +0.8 dB;
  - 480-484 (15 tracks) +1.6 dB;
  - the other ff/f approach crescendos (88-100, 440-464, 620-628) rise +5.9 to +12.4.
- Per stem 628.5 -> 634.5 (`dip.py`):
  - Violins II -20.8 -> -29.7;
  - Violins I -22.4 (630) -> -28.4 (633.5);
  - Trumpet 1 -21.5 -> -26.2;
  - Trumpet 2 -26.1 -> -32.9.
- The violins' held E6 (Vln I/II 629-633, v124, CC11 107 flat) decays 6-9 dB inside the ff before the crescendo's quarter notes start.

**Cause (measured in config and parts.json).**
- `ARRIVAL_WEIGHT_AT = {636.0: (-2.5, 1.5), 484.0: (-1.5, 1.5)}` lowers every wind, brass and string track linearly from 0 at qn - 4 to the pre value at the arrival (`score_to_parts.py` line 3013). That span is exactly the printed crescendo bar.
- In parts.json the Violins I volume envelope goes 2.55 dB at 632.5 -> 2.88 at 635.5, although `hpgain` lists [632, 636, 6.0].
- Horn 1 goes 7.41 -> 5.98 dB, and Trombone 1 -0.04 -> -0.55 dB, across the same crescendo.
- So the hairpin gain is cancelled and the step happens only at the downbeat.

**As heard (inferred).** Two bars of ff that sag and then a jump: the run-up to the climax stands still. A conductor would hear this before anything else in the recapitulation.

**Fix** (`tools/score_to_parts.py`, ARRIVAL_WEIGHT_AT block; `build/score_config.py`):
- Give the hold-back an optional length, `{qn: (pre_db, db, pre_qn)}`, defaulting to 4. Set:
  ```
  ARRIVAL_WEIGHT_AT = {636.0: (-2.5, 1.5, 0.5), 484.0: (-1.5, 1.5, 0.5)}
  ```
  The level then stays at the crescendo's value until 0.5 qn before the arrival, then dips, as a breath before the downbeat. The printed breath and `CAESURA` 636 already sit there.
- Add a sustain fill on the held E6 of both violin sections: `LEVEL_SHAPES["Violins I"]` and `["Violins II"]` gain `[(629.5, 0), (631.5, 4.0), (633.0, 4.0), (635.4, 4.0), (635.9, 0)]`.

**Simulated** (`simclimax.py`, level only, c07 stems):
- Master 632 -> 635.5:
  - +2.1 dB before;
  - +3.8 dB with the shorter hold-back;
  - +4.1 dB with the fill as well.
- 635.5 against 630: -0.1 before, +1.7 with the shorter hold-back, +2.2 with the fill.
- The arrival step 635.5 -> 636.5 goes from 3.9 to 1.3-2.1 dB, with the crash still on the downbeat.
- Peak unchanged (1.331).
- Bar 121: master 480.25 -> 483.5 +2.3 -> +3.5 dB.

**Pass criteria:**
- master at 635.5 at least 1.5 dB over 630 and 3.5 dB over 632;
- bar 121's last beat at least 3 dB over its first;
- the 636 downbeat at least 1.5 dB over 635.5;
- climax order 160 > 122 > 169;
- limiter 3 dB or less.

## 2. The closing and the whole development (bars 69-120, qn 272-480: 208 beats, 99 s) play at exactly 126.000 bpm; the coda's cello solo at exactly 72

**Measured** (`tempo.py`, c07 tempo map). The longest constant runs are:
- 208 beats at 126.0 from qn 272;
- 56 at 50 from qn 0 (the whole Lento);
- 48 at 126 from qn 128;
- 24 at 72 from qn 680.

The c04 arcs cover only the first theme, second theme and recapitulation. The development is the longest stretch of the movement. It has these phrase ends and arrivals, all at an unchanging pulse:
- the p -> ff build of bars 77-82;
- the ff block 82-83 before the sub. p of 84;
- the fugato entries 84/88/91;
- the ff tutti 97-102;
- the espr. p of 107-110;
- the build of 111-120.

**Re-bow conflicts (measured from parts.json `rebows`):**
- No string note carries a re-bow anywhere in qn 304-464.
- In 272-286 there is none either: the celli's 289/294/298 and the basses' 292/297 belong to notes that start at 286.
- The basses' pedal from 464 is re-bowed, so spans must end by 464.
- In the coda only the violas re-bow inside 680-712 (686.694 and 699.507). The celli and basses have none there.

**As heard (inferred).** After finding 1, this is the clearest machine trait left. Ninety-nine seconds without a single lengthened phrase end, and builds that never press forward.

**Fix** (`build/score_config.py`, appended after the c07 block; every span ends by 464 and touches no re-bowed note):
```
PHRASE_ARCS = PHRASE_ARCS + [(272, 286, "main"), (324, 332, "main"), (332, 348, "sub"), (348, 360, "sub"),
                             (384, 396), (396, 408, "main"), (408, 416, "sub"), (416, 424), (424, 432, "sub"),
                             (432, 440, "main"), (440, 452, "sub")]
TEMPO_PUSH = TEMPO_PUSH + [(308, 324, 1.015), (364, 384, 1.015), (452, 464, 1.01)]
# coda cello solo: freeze the violas' two automatic re-bow points in qn so the arcs do not move them
REBOW_AT = dict(REBOW_AT, **{"Violas": [686.694, 699.507]})
PHRASE_ARCS = PHRASE_ARCS + [(680, 688, "sub"), (688, 696, "main")]
```

- The pushes lead into the ff of bar 82, the ff of bar 97 and the bar-117 tutti.
- The (324, 332) arc gives the ff block a broadened end before the subito p, which is the printed contrast.
- The intro arcs (c04-C step 2) still wait for a re-bow refit cycle.

**After the build:**
- diff parts.json `rebows` and `restrikes` against c07: every row must be identical except Violas 686.694/699.507, which must keep the same qn;
- check that no beat inside a printed rit. is faster than the beat before.

**Pass criteria:**
- beats exactly on a printed mark under 60%;
- the longest constant run under 40 beats;
- added length +1.5 to +3 s;
- no tempo jump over 8% at an arc's return.

## 3. The loud end of the range is still a set of walls over a compressed middle: delivered p75->max 10.6 dB against 4.8-7.6 in the recordings, and the delivered span 20.0 dB is over the brief's 16-19 (whole movement)

**Measured** (`dist2.py`; short-term percentiles re integrated, frames above -60 LUFS):

| | p50->max | p75->max | p10->max |
|---|---|---|---|
| c00 mp3 | 15.0 | 9.6 | 21.7 |
| c02 mp3 | 14.7 | 10.3 | 19.9 |
| c07 mp3 | 15.5 | 10.6 | 20.0 |
| Brahms 1/i | 10.3 | 4.9 | 21.5 |
| Brahms 4/i | 9.6 | 6.4 | 17.2 |
| Brahms 1/ii | 11.2 | 7.6 | 17.9 |
| Brahms 4/ii | 12.8 | 6.9 | 18.7 |
| Dvořák 9/i | 14.5 | 4.8 | 26.2 |

- Per track (metrics.md medians, 24 tracks with both marks), mf -> f is 1.8 dB (c00 2.9) and f -> ff 4.2 dB.
- Per bar (bar RMS by its loudest printed mark), mp and mf both sit at -32.3 dB, f at -28.5 and ff at -18.6.
- c04-C #3 (+1.5 dB on mf and f) was rejected because it moved p75->max only 10.3 -> 9.8 in simulation. The middle cannot be raised enough in the mix without taking f to ff away.

**Simulated** on the c07 master with `deliver_master.py`'s ride plus a slow top ride: above p95 - 3 dB, ratio 2:1, the same 3 s zero-phase smoothing, applied to the short-term curve before the gain.

| | LRA | span | p75->max | limiter | inversions (5 s swells > 3 dB) |
|---|---|---|---|---|---|
| as delivered | 15.3 | 20.0 | 10.7 | 2.0 | 0 of 259 |
| with the top ride | 14.7 | 18.2 | 8.9 | 1.5 | 0 of 259 |

Under the top ride:
- the delivered short-term maxima stay in order: 160 +9.3 > 122 +8.8 > 169 +7.9 LU re integrated (before: +10.4 / +9.7 / +7.4);
- the rises into the climaxes stay large: bars 147-155 -> 160 13.7 dB, 111-114 -> 122 10.9, 21-25 -> 26 10.4;
- a gentler version (p95 - 2, 1.6:1) gives span 19.0, p75->max 9.7, limiter 1.3.

**As heard (inferred).** Long stretches of the same medium level, and then a few sudden jumps. It is also why Dan needed the ride: the peaks set the volume.

**Fix** (`tools/deliver_master.py`, after `gdb` is computed from `knee`):
```
TOP_ABOVE, TOP_RATIO = -3.0, 2.0
g = np.clip((knee - smooth(S, SMOOTH_S)) * (1 - 1 / RATIO), 0, CAP_DB) \
    - np.clip((smooth(S, SMOOTH_S) - (loud + TOP_ABOVE)) * (1 - 1 / TOP_RATIO), 0, None)
gdb = smooth(g, SMOOTH_S)
```
- This is a delivery change only; the master wav is unchanged. It is not the low-threshold compressor that the kit warns against: it acts only on the top 5-8% of frames.
- Do it after finding 1, since that raises the approach to 160.
- Recheck the 160-over-122 margin (0.5 LU in simulation, 0.74 now). If it falls under 0.5, take 0.5 dB off `ARRIVAL_WEIGHT_AT[484]`'s `db`.

**Pass criteria:**
- span 16-19 dB;
- LRA 14-16 LU;
- p75->max 9.5 dB or less;
- no inversions;
- climax order kept;
- limiter 3 dB or less.

## 4. The dolce second theme in the celli (with the horn and violas) still plays its small hairpins flat or the wrong way on held notes (bars 47-52, 147-152)

**Measured** (`hp2.py`; last third minus first third of each printed hairpin, 0.1 s windows):
- Violoncellos, 7 of 19 hairpins flat or the wrong way (c02: 6 of 19):
  - 184-187.5 < -0.4;
  - 187.5-188 > +2.0;
  - 196-198 > +0.9;
  - 201-203 < +0.3;
  - 229-231.5 > -0.7;
  - 587.5-588 > +0.8;
  - 589-591 < +0.9.
- Horn 1 595-596 < -0.1 and 596-598 > +0.5.
- Violas 595-596 < -0.8, 596-598 > +1.5 and 612-616 > +5.2.
- Across the whole movement, held-note crescendos go the right way by 1 dB or more in 78 of 92, and moving lines in 154 of 183. The failures cluster in this theme.

**Cause (measured in parts.json).**
- On the celli's held C at 184 (3.5 qn), CC11 rises 74 -> 86 and the volume envelope 0 -> +2 dB, yet the stem stays at -38.5 ± 1 dB.
- The Sus/Leg sustain decays at constant CC11 by about as much as the hairpin adds. The `LEAD_SPANS` ramps (+3 dB) are sized for moving lines.

**As heard (inferred).** The theme's breathing, which the composer marked on every half bar, is missing in the lower octave of the melody. The horn carries it alone.

**Fix.** A per-hairpin fit like `fit_accents.py`: a new `tools/fit_hairpins.py PREV RENDERED_PARTS [--write]` writing `build/hairpin_fits.json` `{track: {start qn: dB}}`.
- For every hairpin on a `LEAD_SPANS` track (plus Violas 584-620), measure the rise as above.
- Add a linear volume ramp over the hairpin, sized to bring a crescendo to +3 dB and a decrescendo to -3 dB, clamped to ±5 dB.
- End each ramp 0.05 qn before the next onset, so it does not deepen a legato join (kit section 6).
- Apply it with `LEVEL_SHAPES`' piecewise-linear code.
- A hand version for this cycle, `LEVEL_SHAPES["Violoncellos"]` additions: `[(184.0, 0), (187.45, 3.0), (187.5, 3.0), (188.0, 0)]`, `[(201.0, 0), (202.95, 3.0), (203.3, 0)]`, `[(589.0, 0), (590.95, 2.5), (591.3, 0)]`, `[(196.0, 0), (197.95, -2.5), (198.3, 0)]`.

**Pass criteria:**
- Violoncellos 3 or fewer of 19 wrong, and Horn 1 / Violas 1 or fewer each in 584-620;
- no new legato-join dips of 5 dB or more in 184-244 and 584-628 (A's `joins.py`).

## 5. The accompaniment eighths have no metric shape (Allegro: Violas, Violoncellos, Double basses; bars 15-32, 69-72, 131-142)

**Measured** (`metric.py`; peak of each unslurred eighth of 0.3-0.55 qn, first 0.12 s, minus the mean of its neighbours within 1 qn):

| | downbeat | beat 3 | beats 2 and 4 | off-beats |
|---|---|---|---|---|
| Violas (295 notes) | +0.61 | -0.10 | +0.28 | -0.46 |
| Violoncellos | -0.30 | -0.45 | -0.03 | +0.15 |
| Double basses | -0.42 | +0.44 | +0.16 | -0.17 |

- c02 was the same within 0.5 dB.
- Note-to-note steps are 1.0-1.8 dB of round-robin noise with no pattern.
- The KS Master Sus/Stac rows ignore velocity (c06), and `METRIC_DB` applies only to plucked and harp onsets (`score_to_parts.py` line 2829).

**As heard (inferred).** A sequenced, even pulse under the first theme. A real section leans on the downbeat and lifts the off-beats by about 1-2 dB without any printed accent.

**Fix.**
- Let the `METRIC_DB` step code also take bowed tracks: `METRIC_BOWED = {track: [(a, b), ...]}`.
- Apply it to unslurred, unaccented notes of 0.5 qn or less, not on `REP_SPLIT` strokes, at down +1.0, mid +0.5, beat 0, off -0.5 dB.
- Spans: Violas, Violoncellos, Double basses [(56, 128), (272, 286), (520, 568)].
- This is level only, so it can be checked first as a stem simulation.

**Pass criteria:**
- downbeat minus neighbours +0.8 to +1.5 dB on all three tracks;
- the accents in those spans still 2-4 dB over their neighbours (`fit_accents.py` report);
- no change in delivered LRA over 0.2 LU.

## Do not touch

- `GENTLE_ACCENT` with `accent_fits.json`: master accent 2-5 kHz a median 7.4 dB under the body.
- The `TIMP_ROLL_RESTRIKE` plans: the timpani stem has no loop.
- `AUTO_REBOW` rows, `rebow_moves.json` and `rebow_fills.json`: the master loop autocorrelation is 0.28 or less on every held passage.
- The c04 `PHRASE_ARCS` with the c07 rit. clamp.
- The tutti breath and `CAESURA` at 636, `TIMP_DELAY_S` and the suspended-cymbal timing.
- The climax order 160 > 122 > 169 and `FFF_HOLD_CAP`.
- The ride's low end (`KNEE_BELOW` 6, `RATIO` 2.5, `CAP_DB` 10): the soft passages are where Dan needs them.
- The pre-roll meter fix.
