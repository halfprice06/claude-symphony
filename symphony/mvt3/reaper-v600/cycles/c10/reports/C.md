# Critic C, cycle 10 (dynamics over time), on the c09 render

Lens: the loudness arc against the score, hairpins and phrase shapes, the sfp of bar 149, the accelerando and the arrivals, the final Largamente and its ring, the loudness range of the master and the delivered mp3 (BRIEF item 6), and loop pulsing (item 7). I measured the stem-fixed c09 stems, `00_Master.wav` and `mvt3-mockup-c09.mp3`. I used K-weighted levels per bar, half bar and quarter, BS.1770 short-term (3 s) and momentary (0.4 s) curves, and 10 ms envelopes, all on the parts.json tempo map. To test delivery changes I ran `tools/deliver_master.py` unchanged on the c09 master, with edited `ride_trims` in a copy of `cycles/c09/rendered_build/parts.json` in scratch. Score pages 1, 8, 11-13 and 16 were rendered and read.

## Manual notes (MANUAL-READING c10 C = the c2 C row, second reading: May 2021 HO manual PDF p.53-54, 64, 101-102; cycles/c02/reports/C.md re-checked; MANUAL-GAPS.md read)

| Manual (PDF page) | What it says | Where in this mockup | Does the c09 render follow it? |
|---|---|---|---|
| p.53 | Shape held lines with CCs, which change mid-note. Velocity is one value at the note start and suits short notes. | Every hairpin; the fp / sfp attacks. | Mostly. In c02 the sfp spike was too short to cross layers. In c09 the sf is a CC step at the mark (FP_SPIKE_AT_MARK, 0.10 s hold, v110), but on 9 of 11 sfp tracks the first 0.1 s still sits 1-8 dB under the ff before it, and the peak lands 0.10-0.30 s after the mark. The CC hold is shorter than the sustain sample's own rise (finding 3). Measured. |
| p.54 | Velocity is one node per note; CC1 and CC11 are continuous lanes. | parts.json lanes. | Yes. Every held line carries a cc1 lane (brass, clarinets) or a cc11 lane (strings, other winds). Read. |
| p.64 | CC11 sets loudness and dynamics, CC1 sets vibrato (MAX strings and woodwinds). On LITE rows CC1 carries dynamics and vibrato. CC7 sets level against other instruments, CC11 shapes the line. | Balance in the volume envelope; CC keeps the printed layer. | Yes. No LITE row is played in c09 (art_counts), so the LITE CC1 rule does not apply. "Sus Marc LITE" is listed in the string release caps but unused. The delivered arc is not set by the CCs: the delivery ride reshapes it in four places (findings 1 and 2). Read and measured. |
| p.64 | Velocity sets loudness for short articulations. | Brass and wind short rows, string shorts. | Yes. Horn Marc Shrt v70-99, trumpet Stac DblTng v88, strings by velocity. Read. |
| p.101 | Brass Sustain: CC1 crossfades 4 layers, so a held note can crescendo or decrescendo. | Brass hairpins. | Mostly. Brass crescendos (1.5 qn or longer, stem last third minus first third, K-weighted): median +5.3 dB, n 15, 3 under +1 dB. Decrescendos: -5.9 dB, n 21, 1 wrong. In the printed crescendo of 275-276 (qn 1096-1104), Horn 1 falls 1.8 dB, Horn 3 falls 1.8 and the bass trombone holds; the master rises only 1 dB across those two bars. Measured. |
| p.101 | Sustains loop, so notes can be held indefinitely. | BRIEF item 7. | No pulsing. Master, at the 3.95 s lag, 100-300 Hz band / spectral centroid autocorrelation: chorale 888-936 -0.11 / -0.14; 1088-1112 +0.06 / +0.12; 548-584 +0.07 / -0.14. No stem note of 8 s or more peaks at the period. Contrabass 936-952 reads 0.62, but in a 7 s window; the master there reads -0.23 (noise, kit LEARNINGS c25). Measured. |
| p.101 | Sustain Accent: velocity sets the attack. Marcato: velocity opens a low-pass on the attack. | Brass accents; the sf at 592. | Not used (GENTLE_ACCENT; MANUAL-GAPS #1). The "Sfz Cres" row (p.103) is still untried for 592. Finding 3 offers a cheaper fix first. Read. |
| p.102 | Shorts have no release trails: hold the last note so the room rings. | Tutti stops, phrase ends. | Yes. Tutti stops fall 14.5-21.3 dB by +0.3 s and reach -20 dB in 0.27-0.45 s (coordinator answer A). Measured. |
| p.102 | Brass staccato at top velocity overblows. | Brass short rows. | Yes. Brass short velocities top out at 99, so no overblow layer. Read. |
| MANUAL-GAPS #12 (p.123, 125) | Recorded crescendo rolls. | Timpani crescendo hairpins. | Not needed. The timpani's fp < at 832-839 grows 9.2 dB. Measured. |

## State through this lens (measured)

- Master: -20.4 LUFS, LRA 22.0 LU. Short-term p10 -41.7, max -12.4 (bar 223).
- Delivered mp3: LRA 14.7 LU, p10 -30.3, max -11.5, span 18.8 dB, limiter 0.8 dB.
  - 211 five-second moves of 3 dB or more; median 80 % of each move kept; 2 inversions (bars 114.6 and 170.3, finding 1).
  - Climaxes, momentary max: 223 -9.7, 278 -9.9, 91 -12.4, 263 -12.8.
- Printed dynamic against tutti bar level (master, K, median): pp -41.7, p -31.4, mf -26.6, f -25.6, ff -19.5, fff -13.1. The order holds. mf and f sit only 1 dB apart, which is mostly texture. Not a finding.
- Hairpins (stems, K, last third minus first third):

  | family | crescendos | decrescendos |
  |---|---|---|
  | winds | +3.0 dB (18 % under +1) | -4.2 dB (0 % wrong) |
  | brass | +5.3 dB | -5.9 dB |
  | strings | +5.2 dB (16 %) | -3.4 dB (10 %) |

- Builds rise as printed:
  - 219-223 (sub. p < mp < f < fff), half bars: -35.0, -33.2 / -29.4, -25.5 / -18.7, -19.0 / -15.1, -11.0;
  - 245-247: -20.9 -> -18.7;
  - fp at 832: attack -21.7, then -26.6, rising to -17.1 at 838.
- Subitos: sub. p at 872 drops 4.4 dB from the mf before it; the sf / sub. p at 548 holds.

## Coordinator checks (answers first)

**A. Wetness, and is the mix now too dry? (measured)** c09's claim holds.
- Automatic detection on the master found 9 tutti stops: bars 2.3, 6.3, 18.7, 26.5, 94.5, 113.5, 166.5, 204.6, 279.3.
  - -20 dB in 0.38, 0.39, 0.28, 0.34, 0.45, 0.27, 0.41, 0.43, 0.37 s (median 0.38).
  - Drop at +0.3 s: 14.5-21.3 dB.
- Final chord: -10 / -20 / -30 / -40 dB at 0.20 / 0.43 / 0.63 / 0.88 s. RT60 is 1.29 s from the -10..-30 dB slope and 1.35 s from -20..-40.
- All inside Dan's ceiling (0.50 s, 1.5 s).
- Too dry? Not overall:
  - RT60 sits in the recordings' 1.1-1.6 s.
  - The stops are at or just under the references' 0.43-0.55 s. Bars 18.7 and 113.5 (0.27-0.28 s) are the driest.
  - The final fermata ring falls about 1.7 times faster than the Columbia Dvořák 9/i ending (-20 dB in about 0.75 s there). That recording is lossy and noisy, so this is only a pointer.
- Do not add hall. If Dan wants more ring under the final fermata alone, that is the place to try it, not the returns.

**B. Do the 90 ms string repeat gaps survive on the master? (measured)** Mostly yes. Dip in the repeated pitch's band (fundamental plus 2nd harmonic), stem / stem plus R Strings / master, medians:

| section | new-bow gaps | "plain" gaps |
|---|---|---|
| Violins I | 8.5 / 6.4 / 9.4 dB (n 6) | 2.6 / 2.2 / 5.9 dB (n 5) |
| Violins II | 7.6 / 7.2 / 4.3 dB (n 14) | 4.0 / 4.2 / 6.0 dB (n 5) |
| Violas | 12.1 / 11.2 / 7.9 dB (n 39) | |
| Violoncellos | 6.0 / 3.9 / 7.3 dB (n 15) | |

The hall fills these:
- the plain gaps at 992.5: Vln I 0.8, Vln II 0.3 dB on the master;
- the plain gaps at 800.5: 3.8 / 4.0 dB;
- the chorale portato quarters of Vln II at 929-930: 0.1-2.0 dB;
- the basses: stem median 6.4 dB, master 0.6 dB. The 896-932 chorale merges are by design.

Movement I's c51 lesson ("the hall fills them on violins and violas") applies here only to those spots.

**C. Inner held notes under a tune after the sfp / subito changes (measured).** No Movement I-style excess, with one exception, Horn 3 in J (finding 6).
- Q (235-242): Horns 3 / 4 at -42.5 / -41.1 against Violins I -32.9 (K).
- M (187-194): Horn 1 at -43.5 against Violins I -35.5.
- E (67-74): the inner strings and bassoons sit 2.6-13 dB under the tune.

**D. Horns' soft passages, weighted (measured).** K-weighting makes the gap larger, not smaller, because the violins are brighter. Horn 1's "1. dolce" pp line at 264-300 is 14.4 dB under Violins I (finding 4).

The "stubs" at qn 116-124 lie inside B's ff (bars 30-31), so they are not a soft passage. Only one note is weak: Horn 1's E-flat 4 at qn 118, at -50.1 K against -41.0 / -44.9 at 116 / 120. Fix that with a `note_trims.json` +5 dB on Horn 1 at qn 118 (inferred), not with the pp trim. Horn 2 at 122 is within 4 dB of its neighbours.

**E. 315 Hz hump in J / P / R (measured).** In J the hump is mostly a pitch, not a tone colour:
- Horn 3 holds D4 (294 Hz, inside the 315 Hz third octave) for 10.5 s and makes 43 % of the master's 315 Hz band in J (its own hump 24 dB).
- The violas hold the same D4 for 13.3 s (9 %).
- In P and R the band is spread: Horn 3 25 / 20 %, violas 23 / 16 %, Horn 1 8 / 16 %.

Judge the 3 dB target with held-pitch frames left out, or only in P / R. More EQ on the horns would thin every horn note to remove one sustained D.

**F. Loop pulsing:** none (manual table, p.101).

## Findings, ranked by what a listener would gain

### 1. The delivery ride adds unprinted crescendos to three soft passages and turns two diminuendos around (measured; fix simulated)

**Where:** `mvt3-mockup-c09.mp3`:
- transition C, bars 42-50 (qn 164-200), printed p -> pp, "dal niente", poco rit.;
- the bassoon solo H, bars 114-120 (qn 452-480), p, after the ff of 110-113;
- the morendo 169-171 into L.

**What is wrong:** after each loud passage the ride's lift (5 s smoothing, ratio 2.0) keeps climbing for 6-10 s. The listener hears the soft music fade in. The transition into the soft second theme, the moment this lens was asked about, gets louder while the score says it gets softer.

**Evidence (bar levels, K, mp3 vs master):**

| passage | mp3 | master | ride gain |
|---|---|---|---|
| Transition, bars 42 -> 48 | -33.2 -> -25.5 (+7.7 dB) | -39.2 -> -36.4 (+2.8 dB) | 6.0 -> 10.9 dB |
| Bassoon solo, bars 114 -> 117 | -37.3 -> -33.2 (+4.1) | -45.1 -> -44.4 (+0.7) | rising 7.9 -> 11.2 |
| 170 -> 173 | -32.9 -> -28.5 (+4.4) | -40.4 -> -40.7 (-0.3) | |

- The bassoon-solo window is flagged as an inversion: the master falls 5.0 dB at 114.6, the mp3 rises 0.6.
- Morendo at 170.3: the master falls 3.8 dB, the mp3 rises 1.4 (inversion).
- The current soft `RIDE_TRIMS` are flat steps (+1.275 / +2.55 dB), so they cannot cancel a ramp.

**Fix (`build/score_config.py`, `RIDE_TRIMS`, after the c02 x0.85 line):**
- Replace the 167-264 row and the 451-504 row with flat-lift rows from `tools/deliver_master.py <master> x.mp3 build/parts.json --fit-flat A B`, fitted on the c10 master, every value +1.5 dB, for A-B = 164-200, 200-264 and 452-504.
- Keep the 375-392, 583-600 and 679-744 rows.
- On the c09 master the fitted rows (rounded, every 4 qn) were:
  - 164-200: 4.8, 4.2, 3.5, 3.0, 2.5, 2.0, 1.7, 1.3, 1.0, 0.8;
  - 200-264: 2.2, 1.9, 1.8, 1.7, 1.6 (to 228), then rising 1.7 -> 4.2 at 263.9;
  - 452-504: 7.5, 5.3, 4.5, 3.8, 3.2, 2.7, 2.4, 2.2, 2.2, 2.3, 2.5, 2.9, 3.3, 3.7.
  - Each row starts and ends at 0, as the tool prints it.
- Simulated with finding 2's row, on the c09 master:
  - transition 42 -> 48: +3.6 dB (master +2.8);
  - bassoon solo 114 -> 117: +1.3 dB (master +0.7; no longer inverted);
  - LRA 14.6 LU, span 19.2 dB, limiter 1.7 dB, median move kept 0.82.
- Cost: the f -> p drop at 41 -> 42 falls from 10.0 to 5.7 dB in the mp3 (master 10.1), because the fitted row starts at bar 42.
  - Starting it at 168 keeps that drop but adds a +3.2 dB step at bar 43 (simulated). That is worse.
- The morendo 170 -> 171 stays as in c09:
  - a fitted 680-744 row made it +1.9 dB;
  - ramping that row in over 680-688 made 171 -> 173 creep +5.7 dB.
  - So keep the old 679-744 row.
- Targets: no soft passage grows more than 1.5 dB more in the mp3 than in the master; LRA 14-16 LU; span at most 19.5 dB.

### 2. The final crescendo (bars 275-277) is flat in the mp3: the 1088-1104 ride trim ends with a -2.5 dB step on the downbeat of 277 (measured; fix simulated)

**Where:** qn 1088-1108. The score has ff from 273 and a crescendo across 275-277 into the fff of 278.

**Evidence:**
- Master bars 275 / 276 / 277 / 278: -16.4 / -16.2 / -14.3 / -11.7 (it rises).
- mp3: -14.1 / -14.0 / -14.1 / -11.2 (flat until the fff).
- The ride's net gain drops from 2.2 to 0.2 dB at 277: the c02 trim `[(1087,0),(1088,2.5),(1103,2.5),(1104,0)]` ends there.
- In the mp3, 223 is louder than 278 on momentary max (-9.7 against -9.9). The printed fff ending sits just under the bar-223 climax.

**Fix:** replace that row with `[(1087,0),(1088,2.5),(1096,2.0),(1104,2.0),(1107.9,1.5),(1108,1.0),(1113,1.0),(1113.5,0)]`.
- Simulated together with finding 1:
  - mp3 bars 273-279: -14.6, -15.0, -14.7, -14.4, -12.5, -10.4, -15.9 (crescendo restored);
  - 278 momentary -9.2, now over 223 at -9.8;
  - 273-276 still 1.8 dB over 147-150 (the purpose of the c02 trim);
  - limiter 0.8 -> 1.7 dB (BRIEF limit about 3).
  - Extending the full +2.5 through the last chord pushed the limiter to 3.1 dB and the span to 20.7. Rejected.
- In the mix, also lift the horns' share of 1096-1104: Horn 1 and Horn 3 fall 1.8 dB inside the printed crescendo.
  - `LEVEL_SHAPES` "Horn 1" / "Horn 3" `[(1096,0),(1103.5,+2.5),(1104,0)]`.
  - Fit on 0.2 s frames as (linear target - measured), clipped -7..+1 (Movement I c34/c38). This part is inferred.

### 3. The sf of the sfp at bar 149 (qn 592) is a late swell, not a hit (measured; fix partly inferred)

**Where:** qn 591.5-594, every sfp staff. Score: ff whole notes in 148, then 149 sfp < ff, with the strings on a fresh down-bow.

**What is wrong:** the p after the mark is now right (c09 do-not-touch: 10-17 dB drops). But the sf itself is not heard. On the master the first 0.1 s after the mark is 2.5 dB under the ff of bar 148, then a swell peaks about 0.2 s late (-14.9 at qn 592.62), then the p. It reads "ff - sag - bulge - p", not "accent - p".

**Evidence (per stem, K):**

| track | ff before (590-591.4) | first 0.1 s after the mark | peak (time after the mark) |
|---|---|---|---|
| Violoncellos | -28.4 | -34.8 | -27.1 (+0.26 s) |
| Double basses | -28.7 | -35.4 | -33.8 (+0.30 s) |
| Violas | -26.1 | -31.5 | -28.1 (+0.10 s) |
| Horn 1 | -27.6 | -31.1 | -28.1 (+0.26 s) |
| Trombone 1 | -24.0 | -28.1 | -25.1 (+0.26 s) |
| Tuba | -32.8 | -34.0 | -30.2 (+0.22 s) |
| Flute 1 | -35.9 | -31.7 | -30.0 (+0.24 s) |
| Violins I | -24.9 | -28.3 | at the mark (the ff's own tail) |
| Violins II | -26.7 | -28.6 | at the mark (the ff's own tail) |

- Tempo there: 0.36 s per qn.
- The CC hold is 0.10 s, shorter than these samples' rise (kit LEARNINGS section 6: HO sustains bloom over 0.1-1 s). So by the time the sample reaches its body, the CC is already falling.

**Fix:**
1. Lead the re-attacked sfp notes so that their bloom peak lands on the mark, with the spike still timed from the mark (`FP_SPIKE_AT_MARK`):
   - `build/entry_leads.json` at 592.0: 0.12 s for Violoncellos, Double basses, Horns 1-4, Trombones 1-2, Bass trombone, Tuba;
   - 0.08 s for Violas and the flutes, oboes and clarinets.
   - c08's string leads made the violins early, so leave Violins I / II unled.
2. Give the strings and basses' attack the level of the ff they follow, with a post-fader bump: `build/roles.json`, 592.0-592.35 qn, +3 dB on Violins I, Violins II and Violas, +5 dB on Violoncellos and Double basses (ramp in at 592.0, out by 592.35, before the p rows at 593-596).
   - The envelope sits before the returns since c06, so the bump also feeds the hall (c09 C #6).
3. Targets per sfp stem:
   - first 0.1 s at most 1 dB under its ff before;
   - peak within ±0.06 s of the mark;
   - the 10 dB p drop kept;
   - master 592.0-592.25 at least -15 dB (now -17.2).
4. The "Sfz Cres" row (p.103) stays the fallback if the leads cannot reach the targets.

### 4. Horn 1's "1. dolce" counter-line at E (qn 264-300) is inaudible: 14.4 dB under the violins (measured; target inferred)

**Where:** bars 67-75, Horn 1, pp dolce, a slurred moving line under Violins I (mf, the second theme) and the cellos' mp counter-melody.

**Evidence:**
- K-weighted active level: Horn 1 -50.1, Violins I -35.7, Violoncellos -42.9, Violas -40.6, harp -40.9.
- So the horn sits 14.4 dB under the tune, 7.2 dB under the cello counter-melody and under every accompanying part.
- At M (187-194), a similar texture, Horn 1 sits 8.0 dB under Violins I.
- Plain RMS is 12.1 dB under, so weighting does not rescue it.
- Causes:
  - the c08 Horn 1 pp/ppp soft trim of -3 dB;
  - the c09 315 Hz horn bell (the actor measured -4.5 dB plain RMS on this span).

**Fix:** a `build/roles.json` row for Horn 1 over 264-300: +5 dB (ramps of 0.25 qn).
- Use a span row, not the global Horn 1 pp trim, so other pp horn notes stay as fitted.
- Target: Horn 1 9-10 dB under Violins I and about 2 dB under the cellos over 264-300, about as at M.

### 5. The first statement of motive x (bars 3-4, qn 8.8-16) is 2-7 dB under the strings' own f; the master drops 24 dB from the ff chord (measured; fix inferred)

**Where:** Violins I, Violins II, Violas and Violoncellos in octaves, f, bars 3-4, between the ff tutti chords of bars 1-2 and 5-6.

**Evidence (stem active level, K):**

| section | bar 3 | f theme, bars 11-12 | f, bars 205-206 |
|---|---|---|---|
| Violins I | -39.2 | -34.1 | -36.5 |
| Violins II | -39.6 | -37.8 | -36.7 |
| Violas | -41.0 | -37.6 | -39.2 |
| Violoncellos | -44.9 | -38.5 | -40.1 |

- Master, half bars: 1 -15.8, 2.5 -41.1, 3 -40.1, 3.5 -34.1, 4 -33.5. Bar 3 sits at the level of the pp transition (bars 43-50: -37..-41).
- mp3: bar 3 -30.3 against bar 1 -14.7.
- Cause: the phrase shape enters at CC11 81 and only reaches the f (88) at the bar-4 accent, on a Leg Slur first note after a rest.
- So the movement's main motive enters as a distant murmur between two ff blows.

**Fix:** a `build/roles.json` row for qn 8.8-15.9: Violins I +4, Violins II +2, Violas +3, Violoncellos +6 dB (ramp out over 15.5-15.9, before the bar-5 chord).
- Or exempt phrases that start on a printed f after a rest at Allegro tempo from the shape's low start (`PHRASE_SHAPE` "start" scaled to 0 for "f" when the phrase is 2 s or shorter).
- Target: each stem within 2 dB of its bars 11-12 level; master bar 3 about -35 dB or higher.

### 6. Horn 3's held D4 in J sits at the oboe's mf level while printed p, and is most of J's "315 Hz hump" (measured; balance target inferred)

**Where:** qn 552-564 (bars 139-141). Horn 3 is printed p on a held D4, under the mf oboe and clarinet lines (bar 141). The same D4 runs 10.5 s through J.

**Evidence:**
- At 560-564 Horn 3 (p) is -43.1 K against Oboe 1 (mf) -42.9 and Clarinet 1 (mf) -38.2. A printed p inner held note matches the mf tune, the kind Movement I c51 found too loud.
- Over J, Horn 3 makes 43 % of the master's 315 Hz third octave (coordinator answer E).

**Fix:** a `build/roles.json` row for Horn 3 over 552-564: -3 dB (and over its other p notes in 536-548 if the same check holds).
- Target: Horn 3 4-5 dB under the oboe at 560-564.
- Re-measure J's 315 Hz hump after it, rather than adding horn EQ.

## Not findings this cycle (measured, for the record)

- The Largamente arrival at 211 (qn 840). The master does not step up (838 -17.1, 840 -17.4), because the strings' f < ff reaches its top a beat early. Trumpet 1's theme enters at its normal ff (-31.6 K; ff median about -34 plain). Its printed untargeted < at 844-848 then lifts it 7.6 dB. That is as printed.
- Bars 205-208 (f, reduced scoring) are 8-10 dB under the ff of 199-204. That is texture; the per-stem levels are normal f.
- Brass accent tilt jump: left to critic A.

**Do not touch:**
- the returns, sends and IR envelope (tutti -20 dB in 0.27-0.45 s, RT60 1.29-1.35 s; inside Dan's ceiling);
- FINAL_RING (final chord -20 dB at 0.43 s);
- FP_SPIKE_AT_MARK's p drop at 592 / 832 and the sub. p at 872;
- the climax order (223 and 278 on top, 263 third);
- the build shapes of 219-223, 245-247 and 832-839;
- the c09 hairpin medians;
- the absence of loop pulsing on the chorale and the final chord;
- the string new-bow repeat gaps (master dips 4-9 dB);
- the delivery ratio 2.0 and its limiter at or under 1.7 dB.
