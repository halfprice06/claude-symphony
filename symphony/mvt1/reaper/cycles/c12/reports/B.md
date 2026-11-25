# Cycle 12, critic B: balance and levels (render c11)

## Method

All numbers come from the stem-fixed c11 render (`cycles/c11/render/`), mapped onto the tempo map in `build/parts.json`. That parts.json matches the stem-fixed state. Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c12-B/`. They are the c11-B set, with these additions:
- `ratchet.py`: dynamic curve against the last printed mark.
- `timp.py`: timpani strokes against the other stems.
- `s1.py`-`s5.py`: simulations.

Definitions:
- **Level:** K-weighted power in 10 ms hops, mean of L and R. Only differences between levels are used.
- **re master:** the stem level minus the master level over the same window.
- **Note body:** from onset +0.08 s to the note's end or to onset +1.5 s, whichever comes first.
- **Melody margin:** the loudest melody stem minus the loudest other sounding stem, per 1 qn window.
- **Simulations:** the dB change is applied to the stem envelopes and the master is re-summed.

## What holds (measured)

**Dynamic mapping by family.** Stem minus the median of the same-dynamic stems in the same 1 qn window:

| Group | f | ff | fff |
|---|---|---|---|
| Trumpets | +0.0..+1.7 | +1.3..+2.7 | -0.6..+2.4 |
| Trombones and bass trombone | +1.2..+1.7 | +2.4..+3.1 | +2.6..+3.7 |
| Horns 1-2 | 0.0..+0.9 | 0.0..+1.1 | |
| Violas | +0.9 | 0.0 | |

- Same-onset trumpet pairs: Trumpet 1 - Trombone 1 is -0.4 at f, +0.7 at ff and +0.2 at fff. That matches Rimsky-Korsakov's "Trumpet = Trombone = Tuba = 2 Horns" (Principles, "Comparison of resonance"). The c11 trumpet trims landed.
- Single woodwinds at p and pp sit within -1.5..+0.3 of the median, except the cor anglais and Flute 1 solos (+3..+4, correct). Timpani rolls sit at -6.2 at pp and -2.1 at p.

**Percussion.** No change.
- Tam-tam fff (qn 484): top stem for 4 beats.
- Crash (qn 636): -17 dB re master over its 9 s.
- Tam-tam pp (qn 696): -9..-13 re master, a 4th to 7th stem.

**Dan's two checks.**
- *Loop pulse:* 14 notes are longer than 6 s. The worst autocorrelations are Bass clarinet qn 480 (band 0.60, at -19 dB re master) and Horn 4 qn 289 (centroid 0.56, -11 dB). On the master, qn 464-500 and 696-728 read -0.23/-0.27 (band) and +0.09/-0.08 (centroid): no pulse.
- *Accent attacks:* 2-5 kHz, first 80 ms minus body. Brass medians are -0.0 (Horn 3) to -12.3 (tuba). The only brass accents over +3 are the known Horn 3 qn 91 (+14.2) and Horn 2 qn 665 (+10.1, the pickup's brightness).
- None of the fixes below adds an accent, lengthens a note or changes an attack.

## 1. Second theme (bars 47-54 and 147-155): the untargeted dolce hairpins ratchet Horn 1 and the celli (and the recap violas) up to f-ff layers (measured)

**Score.** The theme is a unison duet: Horn "1. dolce" with a printed mp pickup at qn 183, and celli "dolce" with mf at qn 183 (violas join at mf in the recap, qn 583). Every swell is an untargeted < or >, and the next printed mark is p at qn 216/616.

**What the build does** (parts.json `dyn_curve` and `cc11`). The hairpins at 184, 187.5, 189, 195, 196, 201 and 204 follow the untargeted rules (step, short-> return, messa di voce):

| Track | Printed | Base level reached | Crests | Max CC11 / CC1 |
|---|---|---|---|---|
| Celli | mf (72) | 86 from qn 190.9 (bar 48) | CC 100 at 196 and 203 | CC11 100 |
| Horn 1 | mp (58) | 80 | 94 | CC11 94, CC1 (its dynamic-layer control) 89 |

- The line never returns to its printed level. Recap qn 583-616 is identical; the violas follow the celli curve, also to 100.
- `ratchet.py` lists Horn 1 qn 191-208 and 593-608 as printed mp, curve 94 (+36 CC).

**What it does to the sound (measured):**
- Celli note bodies at the phrase tops: 192 / 203 / 204 = -30.8 / -28.6 / -30.4 dB. That is the celli's own ff median (-28.7) and 4-6 dB over their f median (-34.3), inside a dolce mf theme.
- Horn 1 at 203: -30.1 dB, against its own ff median of -28.7 and f of -33.6.
- The celli are the loudest stem in 27 of 32 beats of bars 147-155. Horn 1 margin under them: median -2.3, p10 -8.5 dB.
- So the theme plays on the loud layers, with their brighter, heavier timbre. This is the same fault the c01 B #3 fix removed from the coda cello solo with `HP_TARGET_AT` (it had gone from mp to CC 93).

**Fix:**
- `build/score_config.py`: add `DYN["mf-"] = 68`, `DYN["mf+"] = 78`, `DYN["f-"] = 84`. `DYN["mp+"] = 65` already exists.
- Extend `HP_TARGET_AT`. Keep the existing `"Vc"` coda entries and add these, with the same values again at +400 qn (584, 587.5, 589, 595, 596, 601, 604):

| Staff | 184 | 187.5 | 189 | 195 | 196 | 201 | 204 |
|---|---|---|---|---|---|---|---|
| `"Vc"` | mf+ | mf | mf+ | f- | mf+ | f- | mf |
| `"Hn1"` | mp+ | mp | mp+ | mf- | mp+ | mf- | mp |

- Violas (staff `"Vla"`, recap only): the `"Vc"` values at 584 … 604.
- No target equals the level in force when its hairpin starts, so the "niente <" rule does not fire. The 212 > and 612 > keep their printed p targets.
- Result:
  - Celli and violas: 72-84 (crest 84 at the bar-50 and bar-51 tops) instead of 72-100.
  - Horn: 58-70 instead of 58-94. CC1 follows the curve.
- Check the `hpgain` rows in 183-216 / 583-616 after the rebuild. The targeted hairpins now arrive at the mf/f levels, so the crescendo dB-gain rules may add a ramp; the c10 second-theme fills and trims stay as they are.
- This changes CC (timbre), so it needs the render.

**Then fit levels, by stem fix after the render.** Inferred from the CC slopes in LEARNINGS section 4:
- The celli lose about 2-3 dB and Horn 1 about 4-6 dB.
- Restore the c11 relation with `roles.json` rows over [183, 216] and [583, 616]: Horn 1 about +4, Violoncellos about +1, Violas about +1 (recap). Fit them so that:
  - Horn 1 sits 1-3 dB under the celli (mf over mp, as printed), with p10 no worse than -4 (now -8.5).
  - The master over bars 47-54 and 147-155 stays within 1 dB of c11, so the delivered soft-passage level is unchanged.
- Refit `accent_fits.json` only if an accent falls in these spans (none is printed there).

## 2. Bars 23-25 and 135-137: the tune (Fl1/Ob1/Vln I) is covered by the hemiola accompaniment (measured)

**Score:**
- Tune: Fl1, Ob1 and Vln I, mf < into the ff of bar 26 (recap: mf, f at qn 542).
- Accompaniment: Vln II and violas in repeated quarters with accents every three beats (qn 88, 91, 94, 97), and accented celli dotted halves.

**What is wrong (measured):**

| Bars | Melody margin | Covered windows | Top accompaniment |
|---|---|---|---|
| 23-25 (qn 88-100) | -1.4 dB | 9 of 12 | Vln II 6, Va 3, Vc 2 |
| 135-137 (qn 536-548) | +0.1 dB | 6 of 12 (8 of 15 to 552) | Vc 5, Vln II 4, Bn1 3 |

- The Vln II accents stand at -4.5 / -4.9 / -4.5 dB re master at 94.5 / 97 / 97.5, against Vln I at -7.1..-9.5.
- The c11 celli cut (`[88,104,-3]`, `[536,552,-3]`) did not clear it. c11 rejected the optional Vln II/viola cuts because they took 1 dB off the crescendo into bar 27.

**Fix** (`build/roles.json`, level only, so it can be a stem fix): raise the tune and lower the accompaniment by about the same amount, so the crescendo keeps its level.

| Track | Bars 23-25 | Bars 135-137 |
|---|---|---|
| Violins I | `[88, 100, 2.5]` | `[536, 548, 2.5]` |
| Flute 1 | `[88, 100, 2]` | `[536, 548, 2]` |
| Oboe 1 | `[88, 100, 2]` | `[536, 548, 1.5]` |
| Violins II | `[88, 99.5, -2.5]` | `[536, 547.5, -2.5]` |
| Violas | `[88, 99.5, -2.5]` | `[536, 547.5, -2]` |
| Violoncellos | | `[536, 547.5, -1.5]`, on top of the existing -3 |

- Vln I already has `[520, 536, -3.5]`, which ends where the new row starts. Let `ROLE_CHAIN` crossfade them; a 6 dB step at the bar-135 downbeat would be audible otherwise.
- The accent fits on the Vln II/viola accents are relative to their neighbours, so they keep their 2-4 dB.

**Simulated:**

| Bars | Margin | Covered | Master |
|---|---|---|---|
| 23-25 | -1.4 -> +1.6 dB | 9/12 -> 1/12 | +0.16 dB (bars 23/24/25: +0.2 each); bar 26 ff and bar 27 unchanged |
| 135-137 | +0.1 -> +3.4 dB | 6/12 -> 1/12 | +0.23 dB; bar 138 unchanged |

## 3. Final chord, bars 180-182: the celli fade twice as fast as the violins and the ppp chord ends top-heavy (measured)

**Score:** every string part has the same > to ppp in bar 181 and ppp in bar 182 ("change bow at will", morendo on the violas).

**What is wrong (measured):**
- Level change from bar 180 to bar 182, all under the same printed hairpin:

| Stem | Bar 180 -> 182 |
|---|---|
| Vln I | -4.9 dB |
| Vln II | -4.1 dB |
| Violas | -6.2 dB |
| Celli | -9.0 dB |
| Basses | -6.2 dB |
| Master | -4.4 dB |

- The celli drop 5.9 dB within one beat after their re-bow at qn 721.869: -49.1 at qn 721, -55.0 at qn 722. They do not recover.
- In bar 182 the celli are 10.3 dB and the basses 10.1 dB under Vln I (in bar 180: 6.1 / 8.7). The ppp horns 3-4 (-51.3/-52.5) now sit 4-5 dB over the celli (-56.6).
- The cause is the low-CC slope of the Celli KS Master plus that re-bow's piece. Their CC11 falls 32 -> 15, the same as the other sections.

**Fix:** `build/score_config.py` `LEVEL_SHAPES`, level only (stem fix). Leave `rebow_fills` and the frozen re-bows untouched.
- Violoncellos: `[(721.5, 0), (722.3, 3), (724.0, 4), (728.6, 4), (729.0, 0)]`
- Double basses: `[(722.0, 0), (723.0, 1.5), (728.6, 1.5), (729.0, 0)]`

**Expected:**
- Celli fall 180 -> 182 about -5 dB; basses about -4.7 dB, close to the violins.
- Celli under Vln I in bar 182 about -6.3 dB, as in bar 180.
- Master bar 182 rises under 0.3 dB, so the morendo remains.

## 4. Coda bars 171-174: the violas' pp line covers the cor anglais' p espressivo counter-line (measured)

**Score:**
- Celli: mp espr. solo.
- Cor anglais: p espr., an imitation from qn 683.
- Violas: pp espr. sustained line.
- Bassoon 2: pp.

**What is wrong (measured):**
- Cor anglais minus violas over 683-695: median +1.1 dB, with the violas louder in 4 of 11 beats (qn 685-687: Va -6.2..-6.6 re master, CA -8.7..-10.6).
- So a pp accompaniment equals or covers a p solo line. Rimsky-Korsakov (Principles): in p one string section = one wind, so the p line should sit over the pp one.
- The cor anglais already carries +4 dB of roles there, and is 4.8 dB under the cello solo (correct, mp over p).

**Fix:** `build/roles.json` Violas `[680, 695.5, -3]` (stem fix). Do not raise the cor anglais further: a +2.5 trial put it within 2.3 dB of the cello solo, under it in 3 beats.

**Simulated:**
- CA minus Va: +1.1 -> +4.1 dB, covered 4/11 -> 0/11.
- Master bars 171-174: within 0.1 dB.

## 5. Horns 3-4 at f sit 2 dB under the rest of the f texture and 4.9 dB under the trombones (measured; reference Rimsky-Korsakov)

**What is wrong (measured):**
- At f, against the median of the same-dynamic stems: Horn 3 -2.0 (130 windows), Horn 4 -2.1 (123), against Horns 1-2 at +0.9 / 0.0.
- Same bars, same dynamic: Horn 3 - Trombone 2 at f is -4.9 dB (14 bars), while Horn 1 - Trombone 1 is -1.2.
- Rimsky-Korsakov's "Trombone = 2 Horns" puts a horn about 3 dB under a trombone in loud passages, so the inner horn pair is about 2 dB light. They hold the harmony of the f tuttis (bars 27-30, 38-40, 80-81, 112-114, 167-169).
- This is the smallest of the six findings: the master moves under 0.25 dB anywhere.

**Fix:** `build/mix.json` `dyn_trim_db` f anchor (ff and fff unchanged, so the climaxes and the c11 Horn 4 low-note trims are not touched; stem fix):
- Horn 3: f -0.9 -> +0.9.
- Horn 4: f 0.7 -> 2.5.

**Simulated (+1.8 dB where their curve is at f):** master +0.17..+0.21 dB in bars 40, 80 and 114, and under 0.15 elsewhere. Horn 3 - Trombone 2 at f goes to about -3.1.

## 6. Timpani f/ff strokes at qn 125, 284, 316 and 532 are the loudest stem by 3.4-6.7 dB (measured fact, inferred judgement; low priority)

**What is measured** (first 0.3 s after the stroke):

| qn | Bar | Dynamic | Over the next stem | re master | 2-5 kHz first 80 ms minus body |
|---|---|---|---|---|---|
| 125 | 32 | ff | +4.5 | | |
| 284 | 72 | f | +5.4 | -4.8 (half beat) | +5.2 |
| 316 | 80 | f roll entry | +6.7 | -3.3 (half beat) | |
| 532 | 134 | ff | +3.4 | | |

On average the timpani sit at the same-dynamic median (f +0.5, ff +0.3), so this concerns single tutti downbeats.

**Judgement (inferred):** at bar 72 every part is f, so the stroke should land as weight under the strings' hammer strokes. At 6.5 dB over the next stem (Horn 1) it is the timpani's beat. At 316 the roll is printed f over a p string tremolo, so its lead there is correct.

**Fix, only if the actor has room:** `build/note_trims.json` Timpani 284.0: -2.5 dB and 125.0: -2 dB, as a step on the attack (struck-note rule, LEARNINGS section 13). Leave 316 and the 316.3-324 shapes alone.
- Expected: master -0.8 dB over the first 0.3 s of those beats. Bar 72 still opens with the timpani, 3 dB over Horn 1.

## Do not touch

- The c11 trumpet f/ff trims (the trumpets now equal the trombones).
- The percussion gains, patches and timing.
- The climax 158-161 balance and the climax order (160 > 122 > 169).
- The c10 viola rows, the c11 bar-124 roles and brass shapes, and the c11 bars 13-14 shapes.
- `UNI_BY_DYN` and the existing `HP_TARGET_AT["Vc"]` coda targets.
- `rebow_fills.json` and `_REBOW_FROZEN`.
- `accent_fits.json`: refit it only where finding 1's CC change moves levels around an accent; none of findings 2-6 changes an accent's level against its neighbours.
- The c10 second-theme fills and trims as a set.
- `FAST_CAP_ABOVE` 4 with top ride 1.6.
