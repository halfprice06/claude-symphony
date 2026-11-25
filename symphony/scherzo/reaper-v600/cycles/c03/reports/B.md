# Cycle 03, critic B (balance and levels), on the c02 render

Material: `cycles/c02/render/` (stems after c02's Violins I stem fix, and the master), with `cycles/c01/render/` for comparison; `build/parts.json` (the c02 render's data), `build/mockup-events.tsv`, `build/mix.json`, `build/roles.json`, `build/score_config.py`, `cycles/c02/metrics/metrics.md`, and the score comments in `symphony/scherzo/v600/sections/*.ily`.

Method: unless a line says otherwise, levels are dB of power through an approximate K-weighting (a 4th-order high-pass at 38 Hz and a +4 dB shelf above 1.5 kHz). They are computed per 10 ms frame from 2048-point spectra of each stem (both channels summed) and averaged over windows on the parts.json tempo map, with qn 0 at 0 s of the rendered files. "Bar" means a 3 qn window. Judgements are marked **measured** (numbers from the stems), **read** (data, code, score or manual) or **inferred**.

## Manual notes (cycle 3, slot B: group B3, PDF pages 123-126, read in full; MANUAL-GAPS.md read)

| page | what it says | where it applies here | does the render follow it? |
|---|---|---|---|
| 123 (Felt Long), 124-125 (Felt KS, C0) | Strokes more than 65 ms apart play long hits. Strokes closer than 65 ms play "double hits" that damp the previous hit. Velocity = up to 16 dynamic layers, round robin x2 | All 174 strokes on "Timpani Flt Lng" (keyswitch 24) | **Yes**. The closest strokes are the motive-x eighths, 114 ms apart (64 pairs, with the right-hand alternation +24 at B4). None is under 65 ms, so no unintended double hits (measured on the parts.json tempo map). |
| 124 (Felt Short), 124-125 (KS C#0); 126 (Hard Short: "more pronounced than with felt mallets") | Short hits muted quickly, "particularly useful when you know that each hit needs to be cut off within a beat or two" | The 10 printed timpani staccatos (qn 12, 165, 393, 549, 597, 722, 861, 968, 984, 1014). The last is the staccato-accent E2+E3 stroke of bar 339, before the G.P. | **No**. Every staccato plays the Lng row and rings out. See finding 2. |
| 124 (Felt Rolls), 125 (KS D#0) | Rolls: CC1 crossfades 8 dynamic layers for crescendos and diminuendos; CC11 and velocity set loudness | The 8 roll notes on "Timpani Flt Rls" (keyswitch 27), with `TIMP_CC1_MAP`, `TIMP_ROLL_TRIM_DB` and c02's `TIMP_ROLL_TRIM_HOLD_CRESC` 0.6 | **Yes**. Roll levels against the texture are in finding 5 and "Do not touch". |
| 124 (Felt Sus Pedal); DIGEST CC64 row | CC64 switches short and long hits in the Sus Pedal patches; in the KS Masters CC64 is "Repetition: Sustain" | All timpani notes | **Yes**: parts.json carries no CC64 lane for the timpani (read). |
| 123 (Felt Cresc), 125 (KS E0, Hard Cresc) | Live-recorded crescendo rolls in three ranges of different lengths, velocity selects one of 2 dynamics; "the most realism" | The printed roll crescendos 101-103 (qn 300-309), 205-208 (612-624), 301-303 (906-909), 332 (993-996) | **No** (MANUAL-GAPS #7). The CC1 rolls at 300-309 now grow 5.4 dB and sit 7-10 dB under the celli and Violins I (measured), so the Crs row is a realism option, not a balance fix. |
| 125-126 (Hard Long, Hard Rolls, Hard KS) | Hard mallets: "brighter timbre overall", rolls "with clear individual hits"; same rows and keyswitches as felt | The score prints "hard sticks" from bar 1 to 340 and "soft sticks" from 341 | **No** (MANUAL-GAPS #6, open since c00). Balance effect (inferred): felt strokes need more level to cut through a tutti than hard strokes would. That is part of why the bar-339 stroke runs at v125 with a +6 dB accent envelope. |

## Standing checks (Dan's ears), measured on c02

- **Loop pulsing (item 8): none found.** Autocorrelation at 3.95 s of the detrended K-level, the 100-300 Hz band and the spectral centroid:
  - Violins I 0-23: +0.11 / -0.35 / -0.27.
  - Violins I 1089-1128: +0.03 / -0.09 / +0.02.
  - Horn 1 1110-1128: -0.32 / -0.08 / -0.13.
  - Horn 4 drone 456-504: about 0.
  - Master 1089-1128: -0.05 / +0.11 / -0.15.
  - Two higher values are explained by the music, not by a loop:
    - Horn 3 456-504: band and centroid +0.34. The drone figure repeats every two bars.
    - Double basses 672-708: +0.80. A pizz. every bar, and five bars at quarter 228 last exactly 3.95 s.
- **S3 at the sub. p's.** The master in 50 ms frames from 0.2 s before qn 360 reads -28.5, -28.6, -30.2, -33.0, -31.3, -30.8, -29.8. At 828 it reads -30.5, -31.8, -36.3, -37.4, -36.3, -34.8. There is no step to silence (measured). Finding 1 adds a celli role after 360; its first breakpoint must come after the E2 at 360 (see the fix).
- **The tutti timpani strokes do not double-hit** (manual notes above).

## Findings, ranked by what a listener would hear

### 1. The celli's bass and countermelody lines sit over the tune they accompany (bars 193-204, 209-224, 121-132, 277-288; less in 101-104 and 301-304)

- **The pattern (measured).** Violoncellos are the loudest stem in 103 of 376 bars, K-weighted. Violins I are the loudest in 89.
- **At the same printed dynamic (median bar level):**

  | dynamic | celli | Violins I | Violins II | violas |
  |---|---|---|---|---|
  | mp | -33.9 | -36.1 | – | – |
  | mf | -30.8 | -33.0 | -35.0 | -40.5 |

- **In these passages the celli do not have the tune, but they play over it.** Each figure below is celli minus the loudest of Violins I, Violins II, Flute 1, Oboe 1, Clarinet 1 and violas, per bar.
  - **Bars 193-204 (qn 576-612), measured: +10.0, +7.8, +7.1, +6.9, +7.1, +5.0, +9.2, +8.6, +8.6, +10.4, +7.9.**
    - The score gives the oboe's call to Vln I and II, crescendo to the trio's forte at 197. T is in Cl 1, Vln II and violas, with the call in Vln I + Fl 1 (tB.ily c037, c117) (read).
    - The celli play the bass in dotted halves: F sharp 2, B2, C sharp 3, E2 ... (read).
    - At 197-200 the celli read -25.5 / -28.8 / -23.9 / -23.7. Against them: Vln II (T) -34.9 / -37.6 / -36.5 / -33.5, violas (T) -32.6 / -35.8 / -34.2 / -32.3, Cl 1 (T) -38.7 / -41.4 / -33.7 / -35.2.
    - The CC11 is the same as Vln II's and the violas' (88 at the f, vol +3 at the hairpin's end). The celli samples are simply louder at the same controller value (measured, read).
    - Unchanged since c01 (celli -28.2 vs Vln II -37.9 over 576-600).
  - **Bars 209-224 (qn 624-672), measured.** The score's "cellos' countermelody", mf under T at f in Vln I, Vln II and Cl 1 (tC.ily header, read).
    - Celli -30.8 / -29.7 / -29.4 / -28.1 / -29.1 / -28.6 at bars 209, 210, 215, 216, 222, 223.
    - Vln I over the same bars: -31.6 / -31.9 / -31.0 / -29.5 / -29.8 / -30.6. The countermelody is level with or 2 dB over the tune.
    - It is 5-7 dB over Vln II (-34.2..-37.4) and 8-11 dB over Cl 1, which carry T's lower octave.
  - **Bars 121-132 (qn 360-396), the sub. p second idea.** The tune is in Vln I and II, espress.; the celli play the minim bass line (read).
    - Celli minus tune: -3.0, +0.3, 0.0, **+8.0**, +0.8, +0.5, +3.7, +4.6, +2.0, +0.8, 0.0, +3.8.
    - At qn 369-372 (the G2/A2 minims): celli -29.1 against Vln I -37.0 (measured).
  - **Bars 277-288 (qn 828-864):** +3.9 at 280, +2.9 at 282, +1.7 and +2.6 at 286-287 (measured).
  - **Bars 101-104 and 303 (the f hemiola):** +4.4 at 101, +2.7 at 103, +4.6 at 303 over Vln I (measured).
- **Judgement (inferred).** In the trio's forte the listener hears a bass line with the tune behind it. The second idea and the ff return of T have their weight in the wrong register. This is the largest balance error left in the render.
- **Fix: `build/roles.json`, "Violoncellos".** Add these to the existing [36, 84, -2] and [1044, 1068, -2]:
  - `[362, 396, -4]`: start after the E2 at 360, so the role's ramp does not fall under the ff ring (S3).
  - `[576, 612, -7]`
  - `[624, 672, -3]`
  - `[828, 864, -3]`
  - Optional: `[300, 312, -3]` and `[900, 912, -3]`. Check the c02 hemiola strokes' weight there afterwards.
- **Target.** Celli 1-3 dB under the loudest upper line in 193-204, 2-4 dB under Vln I in 209-224, and level with or under Vln I in 121-132.
- **Side effect.** The master at 193-203 drops about 1.5-2.5 dB, because the celli carry about 40% of its power there (inferred from the stem sums). The trio's f stays well over its p (bars 185-188 are -43 dB).
- **Generic alternative.** `mix.json tracks.Violoncellos.gain_db` 0 -> -2, with the roles reduced by 2. The roles are safer: the celli's own tunes are already in balance. Those are the fugato 57-68, the trio tune 169-184 (celli -37 against Horn 3 -46 and Vln I -41) and the answer 189-192.

### 2. The G.P. (bar 340) is filled by an undamped timpani stroke, not by the orchestra's hall

- **Where.** Timpani E2+E3 at qn 1014, printed staccato + accent (the short stroke of the last chord), and the G.P. at qn 1017-1020.
- **Evidence (measured).**

  | qn (window) | timpani | Violins I | Violins II | celli | master |
  |---|---|---|---|---|---|
  | 1014 | -18.3 | -18.1 | -22.5 | -26.9 | -12.6 |
  | 1016 | -29.5 | -30.9 | -30.3 | -33.9 | -23.0 |
  | 1017 | -35.6 | -47.6 | -46.1 | -46.0 | -33.8 |
  | 1018 | -44.3 | -65.1 | -62.4 | -74.7 | -43.9 |

  - Across the whole G.P. (1017-1019) the timpani reads -39.6 against a master of -38.2. The silence after the fff is the timpani ringing alone, 12-20 dB over every other stem.
  - c02's once-per-onset accent fix lowered the stroke 3 dB (c01 G.P. -36.6), but the ring is still there.
- **Cause (read).** Both notes play "Timpani Flt Lng" at v125 with a +6 dB accent envelope (`vol_db` 1014.048 +6.0). The 0.5 qn note-off does not damp the Lng sample. All 174 strokes use Lng (art_counts).
  - Manual p.124 (Felt Short) / p.126 (Hard Short): "Quickly muted, short ... hits ... particularly useful when you know that each hit needs to be cut off within a beat or two". That is the printed staccato.
- **Fix.**
  - Play the printed timpani staccatos on "Timpani Flt Sht" (KS C#0 = key 25; MANUAL-GAPS #6 lists the rows Lng 24, Sht 25, Flm 26, Rls 27, Crs 28).
  - At least the 1014 stroke; best all 10 (qn 12, 165, 393, 549, 597, 722, 861, 968, 984, 1014).
  - Mechanism: a timpani `ART_SPANS` entry `{"from": 1013.99, "to": 1014.01, "art": "Timpani Flt Sht", "mark": "staccato"}`, if ART_SPANS applies after the row choice at `score_to_parts.py` line 2138. Otherwise add a generic option there: `TIMP_STAC_ROW` = "Timpani Flt Sht" for notes with a staccato mark, default off.
  - Memory: one short row on one instance, about 1-2 thousand regions (inferred from the Lng row's size).
  - Fallback if the row is deferred again: `LEVEL_SHAPES` on Timpani only, -12 dB from 1015.0 to 1016.0. This cuts the drum's own tail as a damped stroke would; the strings' hall still rings (S3 is about the orchestra's tail).
- **Target.** Timpani at least 6 dB under Violins I from 1016, so that the G.P. rings with the whole chord.

### 3. Summit, bar 336 (qn 1005): Violins I's fff B6 is still under Violins II and Flute 1 on the downbeat

- **Evidence (measured).** First half quarter of 1005:

  | | Violins I | Violins II (B5) | Flute 1 (B6) |
  |---|---|---|---|
  | c02 | -18.5 | -15.1 | -15.8 |
  | c01 | -21.5 | -16.8 | -17.8 |

  - c02's roles and v112 gained 3 dB. The melody's top note is still 3.4 dB under the second violins' lower octave, and 4.1 dB under its own staccato eighth at 1004 (-14.4).
  - Violins I recover by 1005.5 (-16.1) and lead from 1007.
- **Fix: `build/roles.json`.**
  - `"Violins II": [1004.75, 1008, -3]`
  - `"Flute 1"`: `[1005, 1007, -2]`, on top of its [996, 1017, -4].
  - Do not raise Violins I further: the master peak and the limiter (3.2 dB) sit here.
- **Target.** Violins I level with or over Violins II in the first 0.1 s of 1005. The master's first 0.15 s of 1005 should still be at least 1 dB over 1004; check this, because lowering Violins II removes power from the arrival.

### 4. The pp harp chords are level with the p dolce woodwind tunes in the trio's middle part and the codetta (bars 185-192, 225-237)

- **Evidence, tune minus harp per bar (measured).** The c02 trims fixed the trio's first part: Cl 1 is 1-8 dB over the harp in 153-168.
  - Oboe 1, p "1. espress." (185-188): +2.0, -0.1, +1.2, +0.2.
  - Codetta:
    - Oboe 1 (225-228): -2.2, +2.6, +7.4, +1.0.
    - Clarinet 1 (229-232): +0.6, +0.5, +2.4, -3.6.
    - Bassoon 1 (233-236): +2.6, +2.9, +1.9, +1.1.
  - Bars 189-192: the celli's answer reads -39.1 / -39.2 against the harp's -41.4 / -40.7.
- **Read.** The harp is printed pp under p dolce lines (tB.ily, tC.ily). The c02 `VEL_CAP_SPANS` (v78 over 216-240) did not reach 225-237's level.
- **Fix.** `build/roles.json` `"Harp"`: `[552, 576, -3]` and `[672, 711, -3]`. Leave 711-720: the rit. bars where the harp is alone.
- **Target.** The tunes 3-5 dB over the harp.

### 5. The pp timpani roll at bars 205-206 (qn 612-618) is louder than Hn 1's p espress. motto tail above it

- **Evidence (measured, 1.5 qn windows).**

  | qn | 612 | 613.5 | 615 | 616.5 | 618 |
  |---|---|---|---|---|---|
  | timpani | -41.1 | -40.8 | -39.6 | -38.2 | -36.6 |
  | Horn 1 | -44.0 | -39.2 | -41.7 | -37.4 | -33.2 |

  - The roll is the loudest stem at 612 and 615. Horn 1 has the line (p, espress.; the score's motto-tail preview, tB.ily header).
  - The crescendo starts at 618 (read).
  - Dan's rule 5: a roll starts at its printed dynamic, then settles under the texture.
- **Fix.** `build/roles.json` `"Timpani"`: add `[612, 618, -3]`. Keep the existing [300.0, 300.5, -12]. c02's LEVEL_SHAPES -3 at 621-624 and `TIMP_ROLL_TRIM_HOLD_SKIP` [618] stay.
- **Target.** The roll 2-3 dB under Horn 1 in 612-618. The printed crescendo then still grows about 8 dB into the f at 624.

### 6. Counterstatement bar 33 (qn 96): a pp arco staccato A1 in the basses is louder than the p leggiero theme

- **Evidence (measured).**
  - The Double basses' A1 at qn 96 (staccato, v45, arco since the "arco" at 90) peaks at -36.6 in its first 0.25 s, against Flute 1's -38.0.
  - Bar level: -42.6 for the basses against Flute 1 -44.8 and Oboe 1 -45.5.
  - It rings into the theme's B-B pair at 97, the counterstatement pair whose master separation c02 measured at 2.5 dB (S1; the link is inferred).
- **Read.** The c01 pitch trim for A1 (-6) applies only to "Pizz RRx4" (`pitch_trims.json` `_arts`), so this arco note does not get it.
- **Fix.** `build/note_trims.json` `"Double basses": {"96": -6}`.
- **Target.** The basses' note 3 dB or more under Flute 1's peak.

## Other observations (not ranked)

The violas sit 7-10 dB under both violin sections at f and ff, as median bar levels:

| dynamic | violas | Violins I | Violins II |
|---|---|---|---|
| f | -35.6 | -28.6 | -34.9 |
| ff | -32.6 | -22.2 | -21.9 |

At the summit (1005) they are 11 dB under Violins II. Most of these are inner double stops ("non div.") where that is acceptable (inferred). Revisit after the summit and celli changes, not before.

## Do not touch

- The trio's Clarinet 1 over the harp and the horn drone (153-168).
- The celli's trio tune over Horn 3 (-37 vs -46) and their answer 189-192.
- The Violin I solo over Flute 1 at 349-356 (5-6 dB).
- Hn 1's motto tail at 357-360, and its last G sharp level with the Violins I at 372-376.
- Theme A's Violins I 5-17 dB over the pizz. bass and violas (13-28).
- The roll levels at 300-309 (growing 5.4 dB, 7-10 dB under the strings), 384, 708 (10 dB under the texture), 852, 906 and 993.
- The printed-f timpani solos at bars 91 and 94.
- The sub. p transitions at 360 and 828.
- No loop pulsing on any held note checked.
- c02's harp pp trim, the horn soft trims, the summit arrival weight and the Marc LITE heads with their level steps.
