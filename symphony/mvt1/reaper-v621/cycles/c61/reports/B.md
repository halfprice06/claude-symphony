# Cycle 61, critic B: inner lines hidden behind the tune (c60 render)

Lens: balance and levels, with this cycle's emphasis on the lines with their own musical interest that sit behind the tune (COORDINATOR-NOTES item 1; Dan, 2026-11-17: "instruments with interesting internal lines that are hidden behind the melody or other instruments"). Every proposal below is on the instrument side or is a role row of a phrase or more with its edges in rests, keyed in `build/roles.json`, `build/mix.json` or `build/score_config.py`. Nothing is per note and nothing is fitted to a render. Scripts, cache (152 MB) and score page images are in `cycles/c61/critic_scripts/B/`.

## Manual notes

| Reading (source) | Where it applies here | Does the render follow it? |
|---|---|---|
| HO 2021 manual p.78-79, Celli/Violas "Leg Bow Change": "overlapping notes produce a dramatic and expressive bowing to accent the second note". CC11 and CC1 control overall loudness. | Celli on Leg BC MAX: 13 of 15 notes in bars 15-22, 9 of 12 in 27-32, 7 of 12 in 91-96, but only 5 of 30 in 47-54 and 4 of 34 in 147-155. | Partly. The accent shows only where BC notes sit among slurred notes. Second theme, c59: BC notes +3.2 dB (47-54) and +2.0 dB (147-155) over their neighbours. Where the whole line is BC, the BC notes sit with their neighbours (15-22 +1.2, 27-32 +0.4). c60's row-wide -4 dB was right for the first case and buried the second (finding 1). Measured. |
| HO 2021 manual p.78 (Legato group): monophonic true legato; CC11/CC1 set overall loudness. LEARNINGS section 4: CC11 flattens at the ends of its range. | Lines whose CC11 sits where the track's own curve (build/cccurve59.json) is flat: Bassoon 1 at CC 88, 0.06 dB/unit (167-170); Violas at CC 34, 0.06 dB/unit (171-174). | A CC11 lift cannot move these lines, so the proposals for them are role rows. Where the curve is steep enough and the lift stays inside the printed dynamic's layer, CC11 is proposed instead (Violins II 107-110: 0.55 dB/unit at CC 36). |
| MANUAL-GAPS #5 (expressive rows for the espr./dolce wind solos) and #7 (half-section divisi for soft div. passages). | Cor anglais answers 147-152 and counter 171-174 (Leg Slur MAX); Violins II pp div. 107-110 (Sus MAX, full section). | Not applied. Not proposed this cycle (no range test possible from the critic side). |
| EW-TEMPLATE-PLAN: section 3 (section EQ) applied in c50; section 5 (one CC1 lane for dynamics) not applied; section 8 (phrase arch, entry spread) partly applied. FINDINGS part 6: the CC11-CC1 offset is used as a per-track balance setting. | Violas: the c52 315 Hz -3 dB bell (not from the template) lies on the violas' best band in 7 of 13 viola lines (250-400 Hz). | Inferred: this bell costs the violas audibility exactly where they are masked. Not proposed (it is a blend decision). Listed under finding 2. |
| Orchestration: Adler, The Study of Orchestration p.116 (foreground / middleground = countermelodies and important contrapuntal material / background). Rimsky-Korsakov, Principles, "Comparison of resonance": in forte a string section is about +3 dB over one woodwind, and a horn equals about two woodwinds (LEARNINGS section 13). | The targets I used: middleground lines (countermelodies, imitative entries, fugato counter-voices) 2-6 dB under the tune, K-weighted, and not masked in their own best band (0 dB or better). Background figures 6-10 dB under, with the best band at -6 dB or better. | See the findings and the table. |

## Method (measured unless marked)

- **Lines.** 71 lines were read from the score, pages 2-18 at 80 dpi. They are countermelodies, imitative entries, fugato counter-voices, moving inner voices, bass lines with motion, solo wind figures, and harp and pizzicato figures. Each line is paired with the tune it sits under (`lines.py`). The pitches of each line were checked against `build/parts.json` to find unison doublings, which count as part of their line or of the tune. Examples: Bn1 doubles the celli at 19-22, 27-31 and 167-170; the violas double Cl1 at 129-130; Vln II, cor anglais and celli double the B-minor S tune at 97-102.
- **Measures, on the c60 stems.** The stems sum exactly to the master (residual -inf dB), so "everything else" is master minus line, sample for sample.
  - **K re tune.** K-weighted level of the line minus that of the tune, over the 50 ms frames where both sound. A-weighting was also computed. It reads low lines 3-8 dB lower still, so K is used.
  - **Best band.** The 1/3-octave band from 100 Hz to 8 kHz, among the line's own bands (within 20 dB of its strongest), where line power over everything else is highest, as a phrase mean.
  - **Maskers.** The stems with the most power in that band.
- **Comparison.** The same measures on the c59 stems.
- **Expected values after the fixes.** These come from scaling each stem's band power over the proposed spans (power sum, no cross terms; `sim.py`). The same simulation gives the change in master bar level and loudest 0.4 s at bars 26, 82, 83, 122, 160, 161 and 170. The expected values are inferred, not rendered.
- **Results.** The proposals below move 35 of the 71 lines. All 71 are in the table at the end, with c59, c60 and the expected values.

## Findings, ranked by how much a listener gains

### 1. The celli's own lines lost 2.5-4.5 dB in c60 to a row-wide cut meant for the second theme (bars 15-22, 27-32, 91-96, 139-142, 167-170)

**Measured, c59 to c60, K re tune / best band:**
- Bass line under the theme, 15-22 (with Bn1 from 19): -8.1 to -10.7 dB.
- Half-note counter-bass in the ff tutti, 27-31 (celli + Bn1): -5.6 to -8.1 dB, best band -2.0 to -6.3 dB. It is masked by the double basses' eighths (+3.2 dB in the 200 Hz band) and the timpani.
- Fugato free voice, 91-93: -6.6 to -9.1 dB.
- Fugato, 94-96: -7.3 to -10.6 dB, best band +0.2 to -2.6 dB.
- Celli line, 139-142: -6.8 to -9.1 dB.
- Bassoon/celli counter-line, 167-170: -3.6 to -5.6 dB, best band -2.2 to -4.2 dB.

**Cause.** `mix.json` Violoncellos `region_gain_db` {"rows": ["Leg BC MAX"], "all_db": -4.0} (c60 decision 4) acts on every BC note in the piece. In the second theme it evened the BC bumps: median over the neighbours +3.2 to +0.1 dB in 47-54, and +2.0 to -1.1 dB in 147-155. In 15-22 and 27-32 nearly every note is BC, so the whole line went down.

**The second theme is not buried. Measured:**
- The S tune (Hn1 + celli) stands +3.3 dB over the rest of the orchestra in 47-54 (c59 +3.7). Hn1 + Vla + Vc stand +4.2 dB over the rest in 147-155 (c59 +4.5).
- The celli are 2.0 / 2.7 dB over Horn 1 (K). The c59 critic C asked for less.
- Left: two BC notes now dip under their neighbours, the S-head pickup at 183 (-7.8 dB) and 600 (-4.9 dB). These are single notes, so they go to critic A's fault list, not to the envelope.

**Fix.** Keep the region gain, because it corrects the row's accent where the row is mixed. Give back the level on the BC-dominated phrases with role rows, editing existing rows where they exist (`build/roles.json`):
- Violoncellos [56, 88, -2.0] -> [56, 88, +1.0] (+3 dB).
- New Bassoon 1 [76, 88, +2] (Bn1 enters after a rest at 76).
- Violoncellos [104, 128, -3] -> [104, 128, +2.5]. The c02 cut ("f/ff half notes on Leg BC MAX 3.7 dB over the Vln I theme") is stale: the line is now 8.1 dB under.
- Delete Violoncellos [360, 372, -2, 0.5], and change [360, 408, -3] to [360, 408, -1].
- New Violoncellos [552, 568, +2]. Its edges are in the rests at 551.0-552 and 568.
- New Violoncellos and Bassoon 1 [664, 675.5, +3]. Bn1 rests at 663.1-664. The row ends before the bar-170 chord, so bar 170 does not move (critic C owns the climax order there).

**Why not CC11.** The celli at CC 75 in 15-22 have a slope of 0.41 dB/unit, so +3 dB would need +7 units, toward the f layer under a printed mf. Bn1 at CC 88 has a slope of 0.06 dB/unit and cannot be moved by CC11.

**Expected after the fix, K / best band:**

| Line | Now | After |
|---|---|---|
| 15-22 bass | -10.7 / +3.5 | -8.1 / +6.5 |
| 27-31 | -8.1 / -6.3 | -4.4 / -0.9 |
| 91-93 | -9.1 / +0.8 | -5.1 / +4.8 |
| 94-96 | -10.6 / -2.6 | -8.6 / -0.6 |
| 139-142 | -9.1 / +1.0 | -7.1 / +3.0 |
| 167-170 | -5.6 / -4.2 | -3.8 / -2.3 |

**Theme guard.** The Violins I theme over the celli, 56-88, lower quartile, moves by the same 3 dB. By the actor's script it goes from +7.4 to about +4.4, which is over the 3.9 target (c59 was +4.3). The 15-22 bass line therefore stays about 8 dB under the theme: the guard sets that limit, and the Bn1 row is what gets past it without touching the guard. The actor should re-run the guard.

**Master.** Bars 17 / 31 / 32 rise +0.7 / +0.8 / +0.4 dB. Bars 26, 122, 160 and 170 do not move.

### 2. Viola running figures are masked 6-11 dB in their own band under every f/ff tune (97-102, 117-121, 139-142, 162-165, 69-72, 60-61, 156-157; pp 171-174)

**Measured, K re tune / best band (main maskers):**

| Bars | Line | K / best band | Main maskers |
|---|---|---|---|
| 97-102 | Running eighths | -14.2 / -10.9 | Vln II, the tune's lower octave, +6.5 dB at 315 Hz |
| 139-142 | Eighths | -14.3 / -10.3 | Contrabassoon +3.7, Horn 2 +3.6 |
| 162-165 | Line | -10.7 / -9.4 | Horn 1 +4.2 |
| 117-121 | Triplets with Cl2 | -13.0 / -3.5 | Tbn motto, Bn1, Cbn |
| 69-72 | Eighths | -6.8 / -5.2 | Tbn2 +2.7 |
| 60-61 | Figure | -14.6 / -10.5 | |
| 156-157 | Figures | -9.5 / -5.8 | Horn 3 +3.1 |
| 171-174 | pp moving line under the cello solo | -18.7 / -7.0 | |

**Causes.**
- The violas carry the deepest ff trim of the strings (`dyn_trim_db` ff -4.8).
- Two stale cuts: [552, 566, -2] (c49 era) and [680, 695.5, -3] (c13).
- The c52 315 Hz -3 dB bell lies on their best band (inferred).

**Fix (`build/roles.json`, Violas unless noted).** All edges are in rests except where an existing row already sets the edge:
- [388.5, 408, 2] -> [384, 408.1, 5]
- [552, 566, -2] -> [552, 568, 2]
- [464, 484, 2.5, 4] -> [464, 484, 4.5, 4], plus new Clarinet 2 [464, 479.07, 3]
- New [645, 664.2, 3]
- [272, 284, 1.5] -> [272, 288, 3.5]
- New [236.5, 243.3, 3]
- New [620.5, 627.3, 3]
- [680, 695.5, -3] -> [680, 695.5, +2]. CC11 there is 34 on a 0.06 dB/unit stretch of the violas' curve, so CC11 cannot do it.

**Expected, K / best band:**

| Bars | Now | After |
|---|---|---|
| 97-102 | -14.2 / -10.9 | -10.9 / -7.9 |
| 139-142 | -14.3 / -10.3 | -10.3 / -6.4 |
| 162-165 | -10.7 / -9.4 | -7.7 / -6.4 |
| 117-121 | -13.0 / -3.5 | -11.0 / -1.5 |
| 69-72 | -6.8 / -5.2 | -4.3 / -2.3 |
| 60-61 | -14.6 / -10.5 | -11.6 / -7.5 |
| 156-157 | -9.5 / -5.8 | -6.5 / -2.8 |
| 171-174 | -18.7 / -7.0 | -13.8 / -2.0 |

The tune stays on top everywhere.

**Optional, if 97-102 still sounds like a block.** Violins II [388, 408, -2]. Vln II doubles the tune an octave down and is the masker. Inferred cost: the tune about -0.5 dB.

### 3. The climax countermelody (bars 158-161, Ob1 + Cl1 with Hn3) is masked in its band by the flutes

**Measured.** K -5.9 dB re the tune. Best band 1 kHz at -4.0 dB, with Flute 1 at -1.5 and Violins I at -5.8 in that band. mvt1.md: "The counter is Ob 1 + Cl 1·2 over Hn 3·4". Oboe 1 and Horn 3 are already at CC11 123-125, where the slope is 0.16-0.26 dB/unit. Clarinet 1 carries a stale c03 cut, [628, 644, -3], whose reason was a master peak of 1.40 at qn 637.9 before the delivery limiter existed.

**Fix.** Delete Clarinet 1 [628, 644, -3].

**Expected.** K -4.3, best band -1.7. Bar 160 +0.17 dB and its loudest 0.4 s +0.16. Bars 122, 26 and 170 do not move, so the printed order holds and bar 160's margin over 170 grows by 0.16 dB.

**Tested and rejected.** Flute 2 [628, 644, 1.5] -> -1.5 adds only +0.1 dB to the counter's band. Not proposed.

### 4. Soft counter-lines just under the limit (bars 171-174, 152-153, 107-110)

**Measured, K / best band:**
- Cor anglais espr. counter to the cello solo, 171-174: -7.7 / 0.0. It carries four overlapping rows, one of which is a c41 cut [682.75, 689, -2.5, 0.5] set against the old cello solo. The solo was rebuilt in c59.
- Clarinet 1 mp line, 152-153: -9.5 / -0.9.
- Violins II pp moving voice under the violas' espr. tune, 107-110: -11.2 / -6.1. Horn 3 (+1.7) and Bassoon 2 mask it.

**Fixes:**
- Delete Cor anglais [682.75, 689, -2.5, 0.5]. Expected -6.1 / +2.4.
- New Clarinet 1 [606.5, 612.1, 3]. Five notes after a rest. Expected -6.5 / +2.1.
- `score_config.py` CC11_ADD Violins II `_flat59(423.9, 439.9, 5)`. The curve gives 0.55 dB/unit at CC 36, so this is about +2.8 dB and stays under the p value 46, keeping the pp layer. Expected about -8.4 / -3.3. A role row [424, 439.5, 3] does the same if the actor prefers the envelope. It must end before the existing [440, 464, -4].

### 5. Lines that are fine: do not lower them

**Measured, K / best band:**
- Imitative entries 37-39: Ob1 -3.3 / +0.8, Cl1 -2.4 / -0.2.
- Head dialogue 77-81: best band +2.6 to +8.7.
- Fugato countersubjects: 88-90 Vc -4.9 / +3.1; 91-93 Vla -2.3 / +0.1; 94-96 Vln II + CA -3.0 / -0.4.
- Bn1 / Tbn1 / horns answering figure 97-102: -3.8 / -1.7.
- S head against the P head 103-106: +2.8 / +6.1.
- Bcl espr. 107-110: -6.7 / +2.6.
- Fl1 espr. 109-110: +0.3 / +4.4.
- Trombone motto 117-121: -2.8 / -1.0.
- Hn1 espr. 125-126: -1.4 / +1.1.
- Stretto entries 130: -5.3 / +6.3.
- The tenor P theme 131-134 over the descant: +4.2.
- Bn1 answer 144: -6.7 / +4.8.
- Cl1 counters 156-157 and 164-166: -3.9 and -2.5.
- Vln II counter 162-166: -3.8 / -0.6.
- Cl1 horn call 175-177: +6.4 / +5.0.
- The violas' espr. line 19-22: -4.9 / +4.1.
- The Cl1 + Hn2 countermelody: 56-63 -6.6 / -1.5; 64-68 -3.6 / +1.2.

### 6. Left as they are, and why

- **Horns 3-4, 103-106 (mp).** -8.6 / -8.7. The basses' pizz. f covers them at 125 Hz. Accompaniment under two themes.
- **Bn1, 139-142.** -13.2 / -10.2. It partly doubles the celli, which are raised in finding 1.
- **Bn1, 91-93.** -6.6 / -5.6. Under the bass clarinet and basses.
- **Vln II quarters, 135-137.** -7.0 / -7.5. Under Cl1's held accented notes (+4.0 dB in band). A Cl1 cut there would thin the harmony. Inferred.
- **Accompaniment that is soft as it should be.** Harp, 56-61 (-12.0, p figures in the top octave); bassoons' pp held notes, 147-155 (-16.9); Horns 3-4 accented notes, 23-26 (-9.6).

## Proposals (files and keys; now -> expected; all inferred from the simulation)

| # | File / key | Change | Line now -> expected (K re tune / best band) |
|---|---|---|---|
| 1a | roles.json Violoncellos | [56,88,-2.0] -> [56,88,+1.0]; new Bassoon 1 [76,88,+2] | 15-22 bass -10.7/+3.5 -> -8.1/+6.5; guard about +4.4 |
| 1b | roles.json Violoncellos | [104,128,-3] -> [104,128,+2.5] | 27-31 -8.1/-6.3 -> -4.4/-0.9 |
| 1c | roles.json Violoncellos | delete [360,372,-2,0.5]; [360,408,-3] -> [360,408,-1] | 91-93 -9.1/+0.8 -> -5.1/+4.8; 94-96 -10.6/-2.6 -> -8.6/-0.6 |
| 1d | roles.json Violoncellos | new [552,568,+2] | 139-142 -9.1/+1.0 -> -7.1/+3.0 |
| 1e | roles.json Violoncellos, Bassoon 1 | new [664,675.5,+3] on each | 167-170 -5.6/-4.2 -> -3.8/-2.3 |
| 2a | roles.json Violas | [388.5,408,2] -> [384,408.1,5] | 97-102 -14.2/-10.9 -> -10.9/-7.9 |
| 2b | roles.json Violas | [552,566,-2] -> [552,568,2] | 139-142 -14.3/-10.3 -> -10.3/-6.4 |
| 2c | roles.json Violas, Clarinet 2 | [464,484,2.5,4] -> 4.5; new Cl2 [464,479.07,3] | 117-121 triplets -13.0/-3.5 -> -11.0/-1.5 |
| 2d | roles.json Violas | new [645,664.2,3] | 162-165 -10.7/-9.4 -> -7.7/-6.4 |
| 2e | roles.json Violas | [272,284,1.5] -> [272,288,3.5] | 69-72 -6.8/-5.2 -> -4.3/-2.3 |
| 2f | roles.json Violas | new [236.5,243.3,3], new [620.5,627.3,3] | 60-61 -14.6/-10.5 -> -11.6/-7.5; 156-157 -9.5/-5.8 -> -6.5/-2.8 |
| 2g | roles.json Violas | [680,695.5,-3] -> [680,695.5,2] | 171-174 -18.7/-7.0 -> -13.8/-2.0 |
| 3 | roles.json Clarinet 1 | delete [628,644,-3] | 158-161 counter -5.9/-4.0 -> -4.3/-1.7; bar 160 +0.17 dB |
| 4a | roles.json Cor anglais | delete [682.75,689,-2.5,0.5] | 171-174 CA -7.7/0.0 -> -6.1/+2.4 |
| 4b | roles.json Clarinet 1 | new [606.5,612.1,3] | 152-153 -9.5/-0.9 -> -6.5/+2.1 |
| 4c | score_config.py CC11_ADD Violins II | `_flat59(423.9, 439.9, 5)` | 107-110 -11.2/-6.1 -> about -8.4/-3.3 |

**Climax check for the whole set (simulated).**

| Bar | Bar level | Loudest 0.4 s |
|---|---|---|
| 26 | 0.00 | 0.00 |
| 82 | 0.00 | 0.00 |
| 83 | 0.00 | 0.00 |
| 122 | 0.00 | 0.00 |
| 160 | +0.17 | +0.16 |
| 161 | +0.20 | +0.15 |
| 170 | 0.00 | 0.00 |

The largest master bar changes are 31 +0.8, 17 +0.7, 97 +0.5 and 22 +0.5 dB. In every line the tune stays on top. The actor should range-render 15-32, 88-102 and 156-174 before the full render: these are band-power estimates without round-robin or crossfade effects.

**Do not touch:**
- The Leg BC MAX -4 region gain on the celli. It fixed the second-theme BC bumps; lift the BC-dominated phrases around it instead.
- The second-theme CC11 lanes for the celli and Horn 1.
- The theme guard (Violins I over the celli, 56-88, lower quartile at least 3.9).
- The ff trims that set the climax order.
- The fugato countersubject levels at 88-96 for violas, Vln II and cor anglais.
- The S head at 103-106, the trombone motto at 117-121 and the stretto at 130.
- No per-note value and no fitted row on the envelope.

## Appendix: all 71 lines (imp 1 = counter, imitation or thematic; 2 = moving inner voice or bass; 3 = figure)

| line (bars) | imp | dyn | K re tune c59 / c60 | best band c59 / c60 (Hz) | main maskers c60 | after proposals (K / best) |
|---|---|---|---|---|---|---|
| Lento 9-13 Vln II | 2 | pp-f | -5.6 / -5.5 | -4.0 / -4.1 (400) | Violoncellos -2.8, Bassoon 2 -3.6 | no change |
| Lento 9-13 Vla | 2 | pp-f | -4.7 / -5.1 | -4.2 / -4.5 (2000) | Violins I -1.0, Violins II -1.0 | no change |
| 15-22 celli bass | 1 | mf | -8.1 / -10.7 | +3.5 / +3.5 (200) | Double basses -7.2, R Strings -10.9 | -8.1 / +6.5 |
| 19-22 Vla espr. | 1 | mp-f | -5.5 / -4.9 | +2.8 / +4.1 (315) | R Strings -10.3, Violins II -10.4 | -4.9 / +3.3 |
| 23-26 celli | 2 | mf | -3.0 / -4.9 | +2.3 / +3.5 (125) | Double basses -6.8, Tuba -14.6 | no change |
| 23-26 Hn3-4 | 3 | mp | -10.1 / -9.6 | -9.9 / -9.8 (630) | Violins II +2.8, Flute 1 +1.8 | no change |
| 27-31 celli+Bn1 | 1 | ff | -5.6 / -8.1 | -2.0 / -6.3 (200) | Double basses +3.2, Timpani +0.1 | -4.4 / -0.9 |
| 34-36 Vla imitation | 1 | mp | -4.4 / -5.6 | -3.4 / -4.2 (400) | Violins I +0.7, Bassoon 1 -0.7 | no change |
| 37-38 Ob1 entry | 1 | mf | -3.5 / -3.3 | +1.4 / +0.8 (1250) | Violins I -3.7, Violins II -10.2 | no change |
| 38-39 Cl1 entry | 1 | mf | -2.4 / -2.4 | -0.3 / -0.2 (1600) | Violins II -5.0, Violins I -5.8 | no change |
| 37-39 Vla | 2 | p | -7.3 / -7.8 | -0.9 / -0.6 (315) | Horn 3 -1.6, Bassoon 2 -3.6 | no change |
| 44-46 Vla | 2 | pp | -2.9 / -2.9 | +3.8 / +3.8 (250) | Violins II -5.1, R Strings -10.0 | no change |
| 47-54 harp | 3 | mp | -8.5 / -7.8 | +8.2 / +8.2 (160) | R Perc -7.8, R Strings -24.2 | no change |
| 52-55 Cl1 | 1 | mp | -5.5 / -5.5 | +0.6 / +1.0 (1250) | Violoncellos -1.0, Violas -12.9 | no change |
| 56-63 Cl1+Hn2 counter | 1 | p-mf | -6.7 / -6.6 | -1.3 / -1.5 (315) | Bassoon 2 -5.9, Horn 4 -8.3 | -6.6 / -1.5 |
| 56-61 celli figures | 2 | pp-p | -11.0 / -11.2 | +1.9 / +1.5 (125) | Double basses -4.1, Harp -10.3 | no change |
| 56-61 harp | 3 | p | -12.0 / -12.0 | -2.1 / -2.0 (8000) | Violins I f62 +1.2, Violins II f62 -7.2 | -12.0 / -2.1 |
| 60-61 Vla | 2 | p | -13.4 / -14.6 | -9.4 / -10.5 (1250) | Violins II f62 +7.7, Horn 2 +1.7 | -11.6 / -7.5 |
| 64-68 Cl1+Hn2 counter | 1 | mf/mp | -4.1 / -3.6 | +1.2 / +1.2 (250) | R Winds -8.5, Violoncellos -12.5 | no change |
| 64-68 celli | 2 | mf | -9.1 / -9.1 | +3.2 / +3.1 (200) | Harp -7.1, Double basses -10.0 | no change |
| 69-72 Vla eighths | 2 | f | -6.7 / -6.8 | -6.0 / -5.2 (250) | Trombone 2 +2.7, Timpani -2.3 | -4.3 / -2.3 |
| 69-72 P head (inner) | 1 | f | -3.2 / -3.2 | -1.6 / -1.7 (400) | Horn 3 -6.0, Violas -6.2 | -3.2 / -2.1 |
| 77 Bcl solo | 1 | mf | n/a / n/a | +8.1 / +8.7 (400) | R Winds -11.5, Violas -23.6 | no change |
| 78 Cl1 | 1 | mp | n/a / n/a | +5.4 / +5.7 (1600) | Violins II -10.2, R Winds -13.3 | no change |
| 78-79 Hn a2 | 1 | mf | n/a / n/a | +4.6 / +2.6 (1000) | Violins II -5.1, Violoncellos -8.7 | no change |
| 79 Vc | 1 | mf | n/a / n/a | +11.8 / +7.9 (100) | Double basses -9.2, Timpani -17.0 | no change |
| 88-90 Vc countersubject | 1 | mp | -3.2 / -4.9 | +3.4 / +3.1 (200) | Double basses -8.3, Bassoon 1 stac -11.7 | no change |
| 91-93 Vla counter | 1 | f | -2.7 / -2.3 | -0.7 / +0.1 (315) | Bass clarinet -4.4, Bassoon 1 -9.4 | -2.3 / -0.2 |
| 91-93 Vc counter | 1 | f | -6.6 / -9.1 | +2.2 / +0.8 (160) | Double basses -3.9, Bassoon 2 -6.3 | -5.1 / +4.8 |
| 91-93 Bn1 | 2 | f | -6.7 / -6.6 | -5.9 / -5.6 (200) | Double basses +3.0, Bass clarinet +2.2 | -6.6 / -6.1 |
| 94-96 Vln II+CA counter | 1 | f | -2.3 / -3.0 | -0.6 / -0.4 (500) | Bassoon 1 -2.6, Violas -8.4 | -3.0 / -0.6 |
| 94-96 Vla | 1 | f | -6.5 / -7.1 | -1.0 / -1.4 (400) | Bass clarinet -1.8, Bassoon 1 -7.7 | -7.1 / -1.6 |
| 94-96 Vc | 2 | f | -7.3 / -10.6 | +0.2 / -2.6 (160) | Double basses -1.9, Bassoon 2 -5.6 | -8.6 / -0.6 |
| 97-102 Vla eighths | 2 | f | -15.9 / -14.2 | -12.7 / -10.9 (315) | Violins II +6.5, Horn 3 +2.5 | -10.9 / -7.9 |
| 97-102 answer figure | 1 | f | -5.3 / -3.8 | -2.4 / -1.7 (500) | Violins II -4.7, Bassoon 2 -6.9 | -3.9 / -1.8 |
| 103-106 S head | 1 | mf | +3.0 / +2.8 | +7.4 / +6.1 (500) | Bassoon 2 -10.7, Horn 4 -15.6 | no change |
| 103-106 Hn3-4 | 2 | mp | -8.5 / -8.6 | -9.8 / -8.7 (125) | Double basses +8.5, Bass clarinet -2.5 | no change |
| 103-106 Bcl | 2 | mf | -10.1 / -10.8 | -2.6 / -2.9 (100) | Double basses +2.7, Bassoon 2 -9.3 | no change |
| 107-110 Bcl espr. | 1 | p | -7.2 / -6.7 | +2.6 / +2.6 (160) | R Winds -8.7, Double basses -12.7 | no change |
| 109-110 Fl1 espr. | 1 | mp | -0.7 / +0.3 | +3.6 / +4.4 (800) | Violas -5.6, R Winds -11.6 | +0.3 / +4.3 |
| 107-110 Vln II | 2 | pp | -12.8 / -11.2 | -6.8 / -6.1 (250) | Horn 3 +1.7, Bassoon 2 +1.0 | -8.4 / -3.3 |
| 111-116 Vla eighths | 2 | mp cresc | -7.9 / -7.3 | -3.8 / -4.0 (250) | Tuba -0.2, Bassoon 2 -4.1 | no change |
| 113-115 Tpt1-2 | 2 | pp cresc | +0.8 / +0.8 | -2.5 / -3.2 (1000) | Violins I -3.8, Flute 1 -8.1 | no change |
| 113-116 Cl1/Hn1/Ob2 | 2 | mp cresc | +0.2 / +1.2 | -2.3 / -2.5 (1600) | Trumpet 1 -3.4, Trumpet 2 -4.3 | no change |
| 117-121 Tbn motto | 1 | ff | -3.3 / -2.8 | -0.8 / -1.0 (250) | Violas -4.1, Contrabassoon -6.1 | -2.8 / -1.4 |
| 117-121 triplets | 2 | f | -14.5 / -13.0 | -4.1 / -3.5 (250) | Trombone 1 -2.0, Bassoon 1 -3.0 | -11.0 / -1.5 |
| 125-126 Hn1 espr. | 1 | mp | -1.3 / -1.4 | +1.0 / +1.1 (500) | Violins I -1.2, Bassoon 2 -5.6 | no change |
| 129-130 Vla (doubles Cl1) | 3 | mf | -14.1 / -13.8 | -9.0 / -8.3 (3150) | Violins II +5.5, Clarinet 1 +5.3 | no change |
| 130 stretto entries | 1 | f/mf | -5.3 / -5.3 | +6.6 / +6.3 (500) | Timpani -11.9, Violas -12.1 | no change |
| 131-134 theme (tenor) | 1 | ff/f | +3.9 / +4.2 | +2.6 / +0.8 (315) | Horn 2 -8.4, R Winds -10.7 | no change |
| 135-137 Vln II | 2 | mf | -6.7 / -7.0 | -7.4 / -7.5 (1000) | Clarinet 1 +4.0, R Winds -4.3 | no change |
| 139-142 Vla eighths | 2 | f-ff | -14.7 / -14.3 | -9.1 / -10.3 (315) | Contrabassoon +3.7, Horn 2 +3.6 | -10.3 / -6.4 |
| 139-142 celli | 2 | f-ff | -6.8 / -9.1 | +4.4 / +1.0 (200) | Contrabassoon -6.1, Tuba -8.5 | -7.1 / +3.0 |
| 139-142 Bn1 | 2 | f-ff | -14.3 / -13.2 | -10.6 / -10.2 (250) | Violoncellos +4.5, Contrabassoon +2.5 | -13.2 / -11.0 |
| 144 Bn1 answer | 1 | mf | -7.0 / -6.7 | +3.8 / +4.8 (250) | Horn 3 -5.0, Double basses -17.4 | no change |
| 147-152 CA answers | 1 | p | -7.0 / -6.7 | -0.6 / -0.4 (1000) | Horn 1 -4.6, Violas -6.2 | no change |
| 152-153 Cl1 | 1 | mp | -10.0 / -9.5 | -1.8 / -0.9 (1250) | Violas -1.2, Violoncellos -3.0 | -6.5 / +2.1 |
| 147-155 Bn | 3 | pp | -17.6 / -16.9 | -10.6 / -10.4 (500) | Horn 1 +5.8, Violas +4.6 | -16.9 / -10.4 |
| 156-157 Cl1 counter | 1 | mp | -4.0 / -3.9 | -1.1 / -1.5 (1600) | Violins I -3.0, Violins II -4.4 | -3.9 / -1.6 |
| 156-157 Vla | 2 | mp | -9.3 / -9.5 | -4.7 / -5.8 (400) | Horn 3 +3.1, Horn 1 -0.6 | -6.5 / -2.8 |
| 156-157 celli | 2 | mp | -6.9 / -6.8 | -1.7 / -1.3 (200) | Double basses -2.6, Horn 3 -4.0 | -6.8 / -1.4 |
| 158-161 counter | 1 | ff-fff | -6.6 / -5.9 | -4.0 / -4.0 (1000) | Flute 1 -1.5, Violins I -5.8 | -4.3 / -1.7 |
| 162-166 Vln II | 1 | ff-p | -3.6 / -3.8 | +1.5 / -0.6 (400) | Violas -7.7, R Strings -8.3 | -3.8 / -1.2 |
| 162-165 Vla | 2 | ff-mp | -10.6 / -10.7 | -7.7 / -9.4 (315) | Horn 1 +4.2, Violoncellos +2.4 | -7.7 / -6.4 |
| 162-166 celli | 2 | ff-p | -8.3 / -7.0 | +1.1 / -0.2 (160) | Harp -1.9, R Strings -7.7 | no change |
| 164-166 Cl1 | 1 | mp | -2.6 / -2.5 | -1.3 / -1.5 (630) | Horn 4 -4.9, Bassoon 1 -6.6 | -2.5 / -2.0 |
| 167-170 Bn1+Vc counter | 1 | f | -3.6 / -5.6 | -2.2 / -4.2 (315) | Violas -1.3, Clarinet 2 -3.2 | -3.8 / -2.3 |
| 171-174 CA counter | 1 | p | -7.6 / -7.7 | -0.2 / -0.0 (1250) | Cello solo -5.1, R Winds -6.6 | -6.1 / +2.4 |
| 171-174 Vla | 2 | pp | -19.0 / -18.7 | -7.1 / -7.0 (200) | Cello solo +3.2, Timpani +2.4 | -13.8 / -2.0 |
| 175-177 Cl1 horn call | 1 | pp | +6.3 / +6.4 | +4.5 / +5.0 (1600) | Violins I -9.2, Violins II -11.6 | no change |
| 175-178 Vln II | 2 | pp | -3.6 / -3.6 | -8.2 / -7.9 (1000) | Clarinet 1 +4.6, Trombone 1 +0.8 | no change |
