# Cycle 6, critic C: dynamics over time (on the cycle 5 render)

Under review: `cycles/c05/render` (master and 27 stems), `build/parts.json`, `build/roles.json`, `build/mix.json`, `tools/score_to_parts.py`, `tools/build_reaper.py`, and the score pages for bars 1-14 and 53-92.

Method. All levels are K-weighted (BS.1770 filter in the frequency domain) on 10 ms frames. The stems are post-fader, so they include vol_db and the mix.json trims. Positions use the parts.json tempo map, which includes the caesuras. "Momentary" means a 0.4 s window and "short-term" a 3 s window. The reference is `symphony/render/assets/refs/dvorak9_i_columbia.mp3`, run through the same filter. Its Adagio introduction (0:05-1:00) is the closest comparison for a slow movement. Scripts are in `/private/tmp/claude-501/mockup-loop/c06-C/`:
- `prep.py`, `lib.py`: frames and the tempo map (adapted from critic B's c05 scripts).
- `arc.py`, `dynbar.py`: loudness per bar, and grouped by printed dynamic.
- `beats.py q0 q1 step tracks`: stem levels on a qn grid.
- `hp.py`: the level change across every hairpin.
- `within.py`: dB per CC11 inside sustained notes.
- `longn.py`: the contour of long notes outside hairpins.
- `micro.py`, `cmp.py`: phrase-level movement against the reference.
- `steps.py`: level steps that run against the printed direction.

**Overall arc (measured, LUFS per bar).**

| Bars | Level |
|---|---|
| Opening, bar 1 (ppp) | -48.7 |
| Build, bars 53 → 58 → 59 → 60 | -37.2 → -26.1 → -24.9 → -21.4 |
| Climax, bars 61 / 62 / 63 / 64 | -17.6 / -18.3 / -21.5 / -25.6 |
| Return, bars 65 / 66 | -45.9 / -51.5 |
| Second climax, bars 79 / 80 / 81 | -19.0 / -19.2 / -22.6 |
| Bar 84 (ppp) | -50.7 |
| Bar 92 | -50.3 |

Median master level by the bar's printed dynamic: ppp -48.7, pp -41.4, p -37.1, mp -29.9, f -24.9, ff -19.1. The steps between dynamic levels are now even. The final morendo works. Six problems remain, ranked by how much fixing each would change what a listener hears.

## 1. Crescendos that rise to f or ff hardly grow, and the level arrives as a jump at the next barline (measured)

**Where:**
- Bar 60 (qn 200-204, f to ff): all woodwinds, celli, Horn 1.
- Bars 75-77 (qn 250-259, p/mp to f): double basses, celli, violins.

**What is wrong:** in the printed long crescendo into each climax, the held notes stay flat. The missing level then arrives all at once on the downbeat of the target bar. A real orchestra grows through the crescendo. Here the music stands still and then steps up.

**Evidence (measured):**
- **Bar 60.** Fl1, Ob1, Cl1 and Bn1 each hold one note from qn 200 to 203.8 while CC11 rises from 88 to 113. Over the hairpin they change -3.5, -1.1, -2.8 and -1.8 dB (`hp.py`). Celli go from -37.5 at qn 200 to -40.9 at qn 203, so they get quieter during the crescendo.
- **Arrival at qn 204** (qn 203.5 → 204.25): Flute 1 +9.3 dB, Oboe 1 +5.3, celli +9.8.
- **Celli cause:** the roles.json cut `[188, 204, -6]` ends with its 0.5 qn ramp exactly at the ff.
- **Response to CC11 near the top of its range:** within sustained notes, CC11 moves the level 5.7 dB per 10 CC at CC 0-40, 3.5 at CC 30-60, 2.5 at CC 50-80 and only 1.2 at CC 88-128 (`within.py`, 115 notes). Wind patches average 1.8 dB per 10 CC.
- **All crescendos starting at CC ≥ 72:** median +3.3 dB across the hairpin. Crescendos starting under CC 60 manage a median +5.9 dB.
- **Bars 75-77:**
  - Double basses: p → f measures -45.5 → -43.8 (+1.7 dB over three bars), then +6 dB at the bar 79 ff.
  - Celli: +4.6 dB. Violins I: +4.8 dB.
  - Master: +6 dB over the three bars, flat through bar 78, then +7.3 dB into bar 79.

**Fix:** `tools/score_to_parts.py`, `build_track()`, next to the ROLES loop.

1. Add a dB-domain hairpin gain for every crescendo whose target is f or louder:

   ```python
   HP_GAIN_DB = {"wind": 4.0, "string": 3.0, "brass": 2.0}
   for a, b, k in hps:
       if k == "cresc" and base(b - 0.01) >= DYN["f"] - 2 and family in HP_GAIN_DB:
           nx = min([n["qn"] for n in ns if n["qn"] >= b - EPS], default=b)
           vol_parts.append(("hpgain", a, b, min(nx, b + 2.0), HP_GAIN_DB[family]))
   ```

2. In `vol()`, ramp the gain linearly from 0 at `a` to `g` at `b`. Hold `g` until `nx`, then release it to 0 over 0.25 qn. The new note at the target dynamic carries its own level.
3. Add `a, b, nx, nx + 0.25` to `vbreaks`.

The dyn_trim endpoints do not change. Only the inside of the hairpin rises, and the jump at the barline shrinks by the same amount.

4. Let a roles.json span take an optional fourth value, `end_ramp` in qn: the cut fades out linearly from `b - end_ramp` to `b` (the "span" branch of `vol()`). Then set:
   - Violoncellos `[188, 204, -6, 4]`
   - Bass clarinet `[188, 204, -5, 4]`
   - Violas `[196, 204, -4, 4]`
   - Double basses `[188, 204, -3, 4]`
   - Horn 1 `[188, 204, -2, 4]`

   The cuts now open across bar 60 instead of on the ff downbeat.

**Targets:**
- Fl1, Ob1, Cl1 and Bn1: at least +3 dB from qn 200.25 to 203.5.
- No woodwind or cello stem jumps more than 4 dB from qn 203.5 to 204.25.
- Double basses: at least +5 dB from qn 250 to 259.
- Master: the last beat of bar 60 at least 5 dB over its first beat (it is +3.9 now).

## 2. The sf at bar 63 collapses within one beat instead of dying away across the bar (measured)

**Where:** bar 63 (qn 212-216), Violins I/II, violas, celli and basses.

**What is wrong:** the score has sf on the tremolo, then a diminuendo hairpin across the whole bar to p at bar 64. The trombone ff solo enters on the "and" of beat 1. In the render the strings lose most of their level on beat 1, then barely move. The bar sounds like the strings stop rather than die away under the trombone.

**Evidence (measured), Violins I per beat:**

| qn | 211 | 212 (sf) | 213 | 214 | 215 | 216 (p) |
|---|---|---|---|---|---|---|
| dB | -24.3 | -26.0 | -34.3 | -35.7 | -38.4 | -39.6 |

- The level falls 8.3 dB in the first beat and 5.3 dB over the next three.
- Violins II, violas and celli have the same shape: -29.2 → -36.8, -32.5 → -40.5, and -33.4 → -37.9 at qn 212 → 213.
- **Cause, in `base_points()`:** for an sf followed by a decrescendo, `post = min(level, DYN["mf"])` sets CC11 to 72 by qn 212.75. From ff (114), that is a drop of 42 CC in 0.75 qn. The printed hairpin then has only 72 → 46 left to cover.
- The sf peak itself is only 1.6 dB over the bar before (qn 212.12: -22.7 against qn 211: -24.3), partly because the divisi cut of -6 dB starts at qn 211.9.

**Fix:** `tools/score_to_parts.py`, `base_points()`, sf branch with `hp_here`:
- When `level >= DYN["f"]`, use `post = level - 10`. Otherwise keep `min(level, DYN["mf"])`.
- Move the `(q + 0.25, spike - 6)` point to `(q + 0.25, spike - 4)`.
- The hairpin then runs from `post` at `q + 0.75` to the printed p at 216, a steady fall across the bar.

**Targets:**
- Violins I: qn 213 no more than 4.5 dB under qn 212-212.5, and qn 214 and 215 each 2.5-5 dB under the beat before.
- Violins I: p at qn 216 still about -39 to -40 dB.
- Trombone 1 stays at least 5 dB over Violins I from qn 213 on (it is 12 dB over now).

## 3. Clarinet 2 swells through the morendo in bar 91 (measured; a parser edge case)

**Where:** Clarinet 2, bars 90-92 (qn 295-301). The same kind of fault occurs at Violins I qn 65 (bar 22) and Clarinet 1 qn 280-282 (bar 85).

**What is wrong:** bar 91 is marked *morendo* with a decrescendo to ppp. While the strings fall 4-5 dB, Clarinet 2 rises 5.5 dB: -60.6 at qn 297 to -55.1 at qn 301. It is the only stem in bar 91 moving against the score, and it is the line the morendo is written for.

**Evidence (measured):**
- The bar 90 decrescendo has no target, so it takes Clarinet 2 from pp (34) down to CC 12.
- The bar 91 decrescendo targets the ppp at qn 301 (CC 22), so `base_points()` draws a rising line, 12 → 22, under a decrescendo sign.
- `steps.py` and `hp.py` find two more cases:
  - **Violins I:** an untargeted crescendo at qn 60-62 reaches CC 68, then the printed mp at qn 65 drops it 10 CC (-40.4 → -41.4 dB).
  - **Clarinet 1:** the qn 280-282 crescendo to pp starts at pp and stays flat at CC 34 (+0.1 dB).

**Fix:** `base_points()`, hairpin branch:
- A decrescendo whose target is at or above the current level ends at `level - 6` instead.
- A printed mark that arrives within 1 qn after a decrescendo stop, and is louder than the level the decrescendo reached, does not raise the level. Keep the lower value.
- For a crescendo whose target equals the current level (the "niente <" shape at Cl1 qn 280), start it 12 CC lower at its first onset.

**Target:** Clarinet 2 falls at least 4 dB from qn 298 to 301, and no hairpin in parts.json has CC moving against its printed direction (`hp.py`: 0 cases, now 2).

## 4. The main climax is barely louder than the second one: timpani ff and f are only 1.4 dB apart (measured; the target is inferred from the scoring)

**Where:** bars 61-62 (Largamente, ff, with trombones, tuba, four horns and a timpani ff roll) against bars 79-80 (ff in winds and strings, horns f, timpani f, no low brass).

**What is wrong:**
- The master measures -17.6 / -18.3 in bars 61-62 against -19.0 / -19.2 in bars 79-80, a margin of only 1.1-1.4 LU.
- The orchestration makes bar 61 the summit: trombones and tuba join, the timpani are ff, and the tempo is Largamente.
- A listener hears two equal peaks, and the second, lighter one is just as big.

**Evidence (measured), bars 61-62 against 79-80 by family:**

| Family | 61-62 | 79-80 |
|---|---|---|
| Strings | -21.5 | -23.1 |
| Winds | -21.7 | -22.4 |
| Brass | -26.3 | -27.9 |
| Timpani | -36.6 | -37.6 |

- **Timpani:** the ff roll at qn 204 has CC7 57 and the f roll at qn 262 has CC7 51. In `roll_db`, ff is -14 and f is -16. Measured: -33.6 at qn 204 against -35.0 at qn 262.
- **Low brass at mf:** Tbn2 -34.4, BTbn -37.7, Tuba -38.3. That is 11-15 dB under Violins I, so they add almost nothing to the sum.

**Fix:**
- `score_to_parts.py`, `roll_db`: set ff to -11 and fff to -9. Keep f at -16 and the settle unchanged. The settle still brings the roll under the texture after the stroke.
- `build/roles.json`: Trombone 2, Bass trombone and Tuba `[204, 212, +2]`. They are printed mf under an ff tutti, so a weight that the low end can feel is consistent with the score.
- Re-measure before trimming bars 79-80. If the margin is still under 2 LU, add `[262, 270, -1]` to the string and woodwind tracks.

**Target:** bars 61-62 at least 2 LU over bars 79-80, and the timpani ff stroke at least 3 dB over the f stroke at qn 262.

## 5. Long notes and phrases hardly breathe: the swell is written in CC11, where it is worth about 0.5 dB (measured; the benefit is inferred)

**Where:** sustained notes of 1.8 s or more outside printed hairpins, in all families. 224 notes, most of all the wind chorales (bars 1-14, 31-36), the string pads (bars 15-30, 37-52) and the coda (bars 83-92).

**What is wrong:** the c02 long-note swell adds +4 CC at 40% of the note and ends at -2 CC. At CC 40-90 that is about 1 dB at most.

**Evidence (measured), median contour of these notes in five equal segments, re the first:**

| Family | Notes | Contour (dB) | Median range |
|---|---|---|---|
| Winds | 104 | 0 / +0.3 / +0.5 / -0.2 / -0.6 | 3.1 dB |
| Brass | 39 | 0 / 0 / -0.3 / -1.0 / -1.1 | |
| Strings | 81 | 0 / -0.2 / -0.2 / -1.2 / -0.9 | |

- The strings have no swell at all, only a sag.
- **Against the reference:** momentary loudness around its own 4 s average, with rests excluded, has a standard deviation of 1.35 dB in the master for bars 1-14 and 1.7 dB in bars 15-52. For bars 53-63 it is 0.9 dB. The reference Adagio introduction measures 3.3 dB.
- The comparison is between different pieces, so the size of the gap is inferred. The direction is consistent across every section.

**Fix:** `score_to_parts.py`, where the contours are applied:
- Keep the CC11 swell for timbre.
- Add a dB part through `vol_parts`, as a new item `("swell_db", q0, e, taper)`:
  - +1.5 dB at 40% of the note, back to 0 at 80%;
  - on `swell_taper` notes, -1.5 dB at the end.
- Exclude the same notes as now: inside hairpins, repeated pitches, the timpani and the final bars.
- In `vol()`, the swell must add to the role spans and the divisi cut. It must not replace them.

**Targets:**
- Median long-note contour peak at least +1.2 dB in winds and strings.
- Master momentary deviation (`micro.py`) at least 2.2 dB in bars 1-52.

## 6. The ff trombone line in bars 63-64 holds one flat level for five beats (measured; small)

**Where:** Trombone 1, qn 213-218.

**What is wrong:**
- The marcato descending solo stays within 2.4 dB, from -21.9 to -24.5, from qn 213 to 217.5.
- It is the loudest stem by 10 dB, and the master in bar 64 (-25.6) is still within 8 dB of the climax.
- The printed decrescendo starts only at qn 218, so the level is correct as printed. A player still shapes a falling line, and the accented 218 note is +6.9 dB over its own sustain, which reads as an attack spike.

**Fix:** `build/note_trims.json` Trombone 1:
- `214.5: -1`, `215.0: -1.5`, `215.5: -2`, `216.0: -2`, `217.0: -2.5`, `217.5: -2.5`: a gentle fall inside the ff.
- For the qn 218 accent, lower the velocity from 121 to about 105 (brass accent velocity in `build_track()`). This keeps the accent at the 2-4 dB that rule 4 of the brief allows.

**Target:** Trombone 1 falls about 3 dB from qn 213 to 217.5, and the qn 218 peak is no more than 4 dB over its sustain.

**Do not touch:**
- the final fade: bar 92 at -50.3, with the last chord falling from -47 to -72 dB from qn 301.5 to 304 and no hard cut;
- soft-range hairpins: median +5.9 dB across the hairpin;
- decrescendos from loud levels: median 8.6 dB;
- the horn solo shapes in bars 7-14 and 67-70: +5 to +7 dB swells and an 11 dB fade to pp;
- the bar 53-59 build: -37.2 to -24.9;
- f to ff at bars 59 to 61: +7.3 LU;
- the return at bar 65: -45.9, then -51.5;
- the dyn_trim f/ff endpoints;
- the timpani settle.
