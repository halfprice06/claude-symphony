# Cycle 7, critic B: balance and levels (render c06)

## Method

All numbers are from the stem-fixed c06 render (`cycles/c06/render/`), with score qn mapped to file time through the parts.json tempo map. Scripts and simulations are in `/private/tmp/claude-501/mockup-loop/mvt1-c07-B/`.

- **Levels:** K-weighted stereo power on 25 ms hops.
- **Note bodies:** onset +0.08 s to min(end, +1.5 s). For accents: +0.05 to +0.35 s.
- **Group levels:** the power sum of the listed stems, relative to the master.
- **Simulations** (`sim5.py`): roles, mix trims, short level shapes and per-note steps are applied to the stems, then delivered with `tools/deliver_master.py`. With no change the simulation reproduces c06 exactly: LRA 15.2 LU, span 20.0 dB, limiter 3.2 dB, bar 160 -9.41, bar 122 -10.36, bars 167-170 -12.18 LUFS short-term max.

## What holds (measured)

**The dynamic mapping is consistent between families at the soft and middle levels.** Median note-body levels by printed dynamic:

| Dynamic | Single winds (dB) | Horns (dB) | Trumpets / trombones / tuba (dB) | String sections (dB) |
|---|---|---|---|---|
| pp | -41.7..-46.5 | -41.3..-44.9 | -41.9..-46.3 | -43.4..-47.6 |
| p | -40.5..-46.2 | -39.9..-43.3 | — | -40.5..-44.4 |
| mf | -37..-42.5 | -35..-39 | -34..-38.6 | -35..-40.6 |

**The f and ff levels follow Rimsky-Korsakov's resonance ratios** (string section about +3 dB over one woodwind, horn about +3, trumpet or trombone about +6):

| Family at ff | Level (dB) | Over the woodwinds |
|---|---|---|
| Single woodwinds | -31..-33.5 (about -32.5) | — |
| Violins II, violas, celli | -27.7..-29.8 | +3.5 |
| Horns | -29..-30 | +3 |
| Trumpets and trombones | -26.1..-29.5 | +5..+6 |

The exceptions are Violins I (finding 1) and the double basses (note at the end).

**Inversions are rare.** The printed-dynamic inversion scan (a part printed two steps softer playing 3 dB louder) finds only single bars on any track.

**Percussion and trumpets:**

- **Tam-tam.**
  - fff stroke: -8 dB re master. It is the loudest stem at bar 122, as printed.
  - Damped tail at bar 126: -17 dB.
  - pp stroke at bar 175: -11 to -16 dB re master, 4-6 dB under the loudest string stem.
- **Suspended cymbal roll:** from -45 dB (pp, under a ff tutti) to -15.5 dB at its peak, 0.5 qn before the crash.
- **Crash:** -9 dB re master at the stroke, -20 dB 2 qn later.
- **Trumpets (bars 167-170):** Trumpet 1 leads the ff theme (-7.1 dB re master) with the violas (-8.6) and Horn 1 (-9.4).

## 1. At the fff climax (bars 158-161) Violins I covers its unison partners, and the crash stroke sets the delivery limiter

**Where:** qn 628-644. The melody is played in unison and octaves by:

- Fl 1-2 a2, Ob 1, Cl 1;
- Hn 1-2 a2 (one track with the +3 dB unison boost) and Tpt 1;
- Vln I and Vln II in unison, with the celli an octave lower.

**What is wrong (measured):**

- Violins I is the loudest stem at -6.5 to -7.5 dB re master. Its partners in the same line sit well under it:

  | Partner | Under Violins I (dB) | Note |
  |---|---|---|
  | Violins II | 2.6-7.5 | same pitches; medians per bar group +2.9 / +7.5 at fff |
  | Trumpet 1 | 4.2-7.6 | octave |
  | Flute 1 | 6.1-7.9 | unison |
  | Horn 1 | 3.5-5.1 | |

- Group sums re master, by bar:

  | Bar | Violins I/II + celli (dB) | Horn 1 + Trumpet 1 (dB) |
  |---|---|---|
  | 158 | -4.4 | -8.5 |
  | 159 | -5.4 | -8.0 |
  | 160 | -4.5 | -10.1 |
  | 161 | -4.7 | -9.0 |

- Over all loud frames (the top 10%), Violins I alone is 17.8% of the master's K-weighted power, as much as both trombones, the bass trombone and the tuba together.
- Its fff level (-17.8 dB median) is 7 dB over its own ff. Every other family gains 3-6 dB from ff to fff.
- **Inferred:** the movement's one fff tutti is heard as violins with backing. Rimsky-Korsakov puts a trumpet at about +3 dB over a string section in forte, so a trumpet and two horns in unison with the violins should be level with them, not 4-6 dB under.
- **The top master peak (1.562 at qn 636.33)** comes from the 22in crash stroke: +0.34 of the sample, the largest single stem contribution, against 0.10-0.15 for each of the next eight stems. That peak sets the 3.2 dB limiter.
  - Lowering Violins I alone raises that peak, and the limiter rises to 3.6 dB (simulated), because the delivery gain goes up while the crash peak stays.

**Fix:**

1. `build/roles.json`, rows at [628, 644]:
   - Violins I: +1.5 -> -0.5.
   - Violins II: +1.5 -> +2.5.
   - Trumpet 1: +1.5 -> +2.5.
   - Horn 1: +1.5 -> +2.5.
2. A short dip on the crash attack: -4 dB, full at qn 636.02, held to 636.6, back to 0 by 637.2. The ring at +1.4 s is untouched.
   - `build_perc_track` does not read `LEVEL_SHAPES` (only `build_track` does, line 2911). Make it read `LEVEL_SHAPES` the same way c05 made it read roles, then add `LEVEL_SHAPES["Crash cymbals"] = [[(636.0, 0), (636.02, -4), (636.6, -4), (637.2, 0)]]`.

**Simulated:**

- Groups re master: strings -4.9/-6.3/-5.1/-5.7, brass melody -7.5/-7.0/-9.1/-8.0 (the gap goes from 4-5.6 dB to 0.7-4 dB).
- Violins I is still the loudest stem in bars 160-161.
- Limiter 3.2 -> 2.9 dB; top peak 1.512 (the Violins I join at 637.89).
- LRA 15.2 LU, span 19.9 dB.
- Climax order kept: bar 160 -9.56 > bar 122 -10.36 > bars 167-170 -12.19. The margin over bar 122 narrows 0.95 -> 0.80 dB.

## 2. Inner-voice themes in the f/ff tutti are not the loudest layer (bars 69-71, recapitulation bars 131-134)

**Bars 69-71 (qn 272-284), all printed f.**

- Theme: Cl a2, Hn 1-2 a2, Vln II and Vla (unis.).
- Countermelody: Fl, Ob 1, Tpt 1 and Vln I.
- Harmony: Hn 3-4, Tpt 2, Ob 2, Bn 1 and timpani.
- Bass: Vc, Cb, BCl, Cbn and Bn 2.

**What is wrong (measured), bars 69-71.** Per half bar, re master:

| Layer | Level (dB) |
|---|---|
| Theme | -4.9..-7.4 |
| Countermelody | -3.9..-8.2 |
| Harmony | -5.4..-8.1 |
| Bass | -4.8..-8.4 |

- The theme is never more than 1.5 dB over the harmony, and it is under the harmony in bars 69.3, 71.1 and 71.3.
- Trumpet 2's sustained lower note (-9.6 to -12.6) is often over Horn 1, which carries the a2 horn theme (-7.8 to -11.8).
- The bass clarinet and celli bass line (-6.4 to -12.4) sits with the theme.

**Bars 131-134 (qn 520-536).**

- The recapitulation's first theme is in Vc ff, Bn a2, Cl a2 and Tbn 1-2 f.
- It is under the Violins I/II + Fl/Ob countermelody by 1.5-3.6 dB per bar (theme -5.2..-7.7, counter -3.7..-6.2).
- Violins I alone is 0.5-4.7 dB over the celli. The c02 cut ([520, 536, -2] on Vln I/II) is not enough.

**Fix: `build/roles.json`.**

| Bars | Track | Row |
|---|---|---|
| 69-71 | Horn 1, Violins II, Clarinet 1 | [272, 284, +2] |
| | Violas | [272, 284, +1.5] |
| | Trumpet 2 | [272, 284, -3] |
| | Horn 3, Horn 4, Oboe 2, Bass clarinet, Violoncellos | [272, 284, -2] |
| 131-134 | Violoncellos, Bassoon 1, Bassoon 2 | [520, 536, +2] |
| | Trombone 1, Trombone 2 | [520, 536, +2.5] |
| | Violins I, Violins II | add [520, 536, -1.5] (on top of -2) |

**Simulated:**

- Bars 69-71: theme -2.9..-5.5, 1-5 dB over the harmony and the bass, level with or over the countermelody.
- Bars 131-134: theme -3.3..-5.8, over the counter in 3 of 4 bars.
- Delivery unchanged (LRA 15.2, limiter 3.2, climaxes unchanged).

## 3. Clarinet 1's hot top notes are trimmed only on the legato row: G5, A-flat5 and B-flat5 stand 6-10 dB over the line on Sus notes

**Where:** Clarinet 1 qn 118/120/121.5 (bars 30-31), 381/383 (bar 96), 414, 417 and 422 (bars 104-106), 482, 558/561.5, 628 and 642 (bars 158-161), 665-676 (bars 167-170).

**What is wrong (measured):**

- The `pitch_trims.json` Clarinet 1 entries (79: -6, 80: -3) apply to legato notes only. `_all_arts_pitches` holds only 68.
- The KS Master's G5 is the known +10 dB note (kit LEARNINGS 13).
- Raw residual against the track's notes at the same dynamic within 8 qn, on the Sus Non Vib row:

  | qn | Note | Residual (dB) |
  |---|---|---|
  | 118 | G5 | +9.1 |
  | 414 | G5 | +9.4 |
  | 422 | G5 | +6.9 |
  | 642 | G5 | +5.7 |
  | 120 | A-flat5 | +7.5 |
  | 383 | A-flat5 | +5.9 |
  | 558 | A-flat5 | +5.2 |
  | 417 | B-flat5 (legato, untrimmed) | +8.3 |

- **Bars 104-106:** Clarinet 1 is the loudest stem at -0.9 to -2.1 dB re master. That is 11-12 dB over Oboe 2, which plays the same f figure in unison, and 10-12 dB over the mf legato line of Horn 1, Bassoon 1 and the celli.

**Fix: `build/pitch_trims.json` Clarinet 1.**

- Add `"82": -4`.
- `_all_arts_pitches`: [68] -> [68, 79, 80, 82].

**Simulated** (non-legato G5/A-flat5/B-flat5 steps only):

- Clarinet 1 at 414/422 goes from -1.7/-0.9 to -7.7/-6.9 dB re master. It stays the leading voice of the f figure, about 4 dB over the next stem.
- Delivery unchanged.

**Also seen (inferred, smaller):** Cor anglais A-flat4/A4 on Sus at qn 361 and 371 (bars 91-93, f) run +9.8/+11.0 over their neighbours. Its A4 -5 trim is legato-only. Consider `"68": -4` and `_all_arts_pitches` [68, 69].

## 4. Timpani: a chained roll re-attacks inside a crescendo, and the fff roll body is buried at the climax

**Bars 80-81 (qn 316-324):** printed f < ff, a roll per bar, with chords and accented motive entries over it.

**What is wrong (measured):**

- `TIMP_LOUD_ATTACK_DB` (+6 dB, held 0.25 qn) fires on each roll note, including the second roll at 320, which continues the first.
- The timpani is the loudest stem on both downbeats (-2.9 and -3.0 dB re master). It then falls to -12.8 at 321.5 and -15.5 at 325.5.
- So the printed crescendo plays as two hits, with the roll receding between them.
- The same re-attack shows at 632 (-12.5 against a -18..-20 roll body) and at 628.

**The fff largamente roll at bar 160 (636.5-640):**

- -20 to -22.5 dB re master; it ranks 19-22 of 32 stems. In the 100-300 Hz band it is -9.7 dB re master.
- The ff/fff rolls of bars 117-125 and 158-161 sit 16-20 dB under the master.
- **Inferred:** the brief's settle rule exists so soft rolls do not cover. A fff roll at the main climax that ranks with the second oboe loses the weight a real timpanist gives it.

**Fix:**

1. `tools/score_to_parts.py`, the `TIMP_LOUD_ATTACK_DB` block (about line 2392): skip the bump on a roll whose onset is within 0.05 qn of another roll's end (a chain continuation), as `tie_stroke` already halves it. That covers 320, 632 and 636 (636 keeps its f-arrival stroke weight from the fff dynamic).
2. `build/roles.json` Timpani `[637, 640, 3]`, starting after the 636 attack so the limiter peak is not touched.

**Simulated** (bump removed at 320/632, +3 over 637-640, together with finding 1): limiter 3.0 dB, climax order kept.

## 5. The pp dolce wind-and-brass chorale of the coda (bars 175-178) sits 2-5 dB under the pp strings

**Where:** qn 696-712.

- Chorale: Tbn 1-2 and B.tbn (pp dolce), Cl 1 (pp, from 699) and B.cl.
- Strings: Vln II, Vla, Vc and Cb, all pp.

**What is wrong (measured):**

- Trombone group -3.7 to -6.8 dB re master, strings group -1.9 to -3.6.
- Trombone 1 is under the violas, celli or basses in 5 of 8 two-qn windows, by 1.5-2.5 dB.
- At bar 180 Trombone 1's "1." line (ppp) is 3-7 dB under the violas.
- **Inferred:** at equal printed dynamics the chorale is the new colour of the passage and should sit level with the strings, not under them.

**Fix: `build/roles.json`.**

- Trombone 1, Trombone 2, Bass trombone: `[696, 712, 2.5]`.
- Bass clarinet: `[696, 712, 2]`.
- Clarinet 1: `[699, 712, 2]`.
- Leave bar 180 alone. Its morendo belongs to critic C's lens.

**Simulated:**

- Brass -1.7..-4.1 dB, strings -1.9..-3.1: level within 2 dB.
- The ride sits at its cap here, so delivery is unchanged.

## 6. Trumpet 1's accents in the bars 167-170 theme still stand 5.8 dB over its legato notes

**Where:** Trumpet 1, qn 665, 670 and 673 (ff, a2 theme with Horn 1 and the violas).

**What is wrong (measured):**

- Accent body minus the other notes of the same theme: Trumpet 1 +5.8 dB. Horn 1 in the same bars: +3.8.
- The target is 2-4 dB.
- 2-5 kHz attack minus body: -5.0 (no bite). This is level only.

**Fix:** `build/note_trims.json` Trumpet 1 `"665.0": -2, "670.0": -2, "673.0": -2` (steps, `NOTE_TRIM_RAMP_S` 0.1 s). The +3 legato trims stay.

**Simulated:** +5.8 -> +3.8 dB.

## Combined simulation of findings 1-6

Spec: `s_all.json` (finding 3 includes only the non-legato notes).

- Delivered: LRA 15.2 LU, span 19.9 dB, limiter 3.2 -> 3.1 dB, -1.6 dBTP.
- Climax order: bar 160 -9.47 > bar 122 -10.26 > bars 167-170 -12.21. The margin narrows 0.95 -> 0.79 dB.
- If the render narrows the margin further, add a -0.5 dB `_all` row over [484, 492]; it is already there at -0.5, so take it to -1.0 (inferred).

## Low end (measured; no change proposed)

**Loud frames (top 10%), band shares against the Dvořák reference:**

| Band | Mix minus reference (dB) |
|---|---|
| 60-100 Hz | +6.5 |
| 100-160 Hz | -5.2 |
| 160-250 Hz | -3.8 |

**Where the energy comes from:**

- The basses carry 44% of 20-100 Hz but only 8.6% of 100-300 Hz.
- The celli carry 39% of 100-300 Hz.
- The basses sit 3-8 dB under the celli in octaves at f/ff (1 dB at p).

**Why not raise the basses:** raising them (f +2.5, ff +4, simulated) lifts 20-60 Hz by 2.6 dB and 100-160 Hz by only 0.6, and the limiter to 3.4. The basses' level is not the fix for a thin body, and the reference is a lossy MP3 (kit LEARNINGS 14). Leave this alone unless a lossless reference says otherwise.

## Dan's two checks (measured)

**Loop pulse.** Only 16 notes are longer than 6 s; strings and the long rolls are re-bowed or re-struck. The highest:

| Note | Autocorrelation at 3.95 s | Stem re master |
|---|---|---|
| Tuba, qn 488 | 100-300 Hz 0.92 | -17.0 dB |
| Horn 4, qn 289 | 100-300 Hz 0.76 | -9.8 dB |
| Harp, qn 724 | 0.56 | -21.1 dB |

The tam-tam, crash and the other wind notes are at 0.36 or below.

**Accents.** 2-5 kHz in the first 80 ms minus the body, median (p90):

| Track(s) | Median (p90), dB |
|---|---|
| Trumpet 1 | -5.0 (-2.8) |
| Trumpets 2-3 | -11.4 / -12.8 |
| Trombones, bass trombone, tuba | -9.2..-11.9 |
| Horn 1 | -4.5 (+4.5) |
| Horn 3 | +0.4 (+2.4) |
| Violins I | -3.0 |
| Celli | -2.7 |
| Oboe 1, Clarinet 1, Flute 1 | -4.2..-5.5 |

No accent bites. Finding 6 is about body level.

## Do not touch

- The global soft trims 7/7/5 and the per-track soft overrides; they give the even p/pp mapping above.
- The trumpet dyn trims (f 7, ff 8; Tpt3 8/11) and the trombone and horn trims.
- The c06 B roles: Oboe 1 [176, 184, 4], timpani coda +10, Violins II ff +1.0, the Horn 1 192/592 trims.
- The tam-tam fff stroke, damp and `tail_hold` false.
- The sus. cymbal level and timing.
- The climax order (160 > 122 > 167-170).
- `GENTLE_ACCENT` articulations for every family.
