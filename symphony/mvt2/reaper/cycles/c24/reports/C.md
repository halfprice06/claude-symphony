# Cycle 24, critic C: holistic comparison (on the cycle 23 render)

Under review: `cycles/c23/render` (master and 32 stems), `cycles/c23/mvt2-mockup-c23.mp3`, `cycles/c23/metrics`, `build/parts.json` (05:18, before the c23 render at 05:19), `build/{roles,note_trims,early_fills}.json`, `tools/score_to_parts.py`, `tools/deliver_master.py`, and score pages 1-8.

Comparisons:
- cycle 0 (`cycles/c00`, tempo from `cycles/c00/before/parts.json`)
- five cycles back, cycle 18 (`cycles/c18`, tempo from `cycles/c19/before/build/parts.json`)
- c19-c22 for the trend
- the references: Brahms 1/ii and 4/ii (stored metrics from c04) and the Dvorak 9/i MP3

Scripts and outputs are in `/private/tmp/claude-501/mockup-loop/c24-C/`:
- `m_c18..m_c23`, `m_c*mp3`: `symphony/render/tools/measure.py` on each master and mp3
- `sections.py`, `motion2.py`: section loudness and loudness motion
- `bardyn.py`: bar level against the printed dynamics
- `hp.py`: crescendo rise per printed hairpin
- `dec.py`: decrescendo shape
- `kb.py`, `beats.py`, `beatsK.npy`, `beats.txt`: K-weighted levels per beat or half-beat, for any stem and cycle
- `lead.py`: lead margin over the rest of the orchestra
- `spread.py`: ensemble onset spread
- `tempo.py`, `beatbpm.py`: tempo
- `sim.py`: level-only simulation on the c23 stems, which sum to the master. `sim_base.mp3` reproduces the c23 delivery exactly (I -19.8, LRA 16.0, limiter 1.7, span 18.5).

## Where the render stands (measured)

| | c00 | c18 | c23 | c18 mp3 | c23 mp3 | Brahms 1/ii | Brahms 4/ii |
|---|---|---|---|---|---|---|---|
| I (LUFS) | -24.2 | -22.5 | -22.5 | -19.8 | -19.8 | -23.0 | -19.1 |
| LRA (LU) | 20.0 | 23.6 | 23.7 | 16.0 | 16.0 | 15.2 | 16.9 |
| phrase-scale motion, 1 s vs 20 s (dB) | 3.48 | 3.76 | 3.76 | 2.94 | 2.84 | 4.56 | 3.92 |
| 4 s change of short-term loudness, p90 (dB) | 7.28 | 6.66 | 5.79 | 5.80 | 4.99 | 8.55 | 6.29 |
| bar level per printed dynamic level (dB) | 1.4 | 3.9 | 4.0 | 2.4 | 2.5 | | |
| residual std, bar level against dynamics (dB) | 3.8 | 2.7 | 2.5 | 2.0 | 1.9 | | |

The mp3 trend from c18 to c23 for the 4 s p90 was 5.80, 5.20, 5.03, 4.90, 4.92, 4.99.

Since cycle 0 the render has gained the things a listener notices first:
- The printed dynamics map onto level about three times as steeply.
- The two climaxes are shaped: bars 61-64 sit 7.7 LU over integrated and bars 79-82 6.2 LU in the mp3, a gap of 1.3 LU.
- The f -> ff build of bars 57-61 rises 6 dB, and the bars 75-78 build rises 8.7 dB (measured).

In the five cycles since c18, the large-scale shape has hardly changed:
- Section loudness moved by 0.3 LU or less everywhere except the horn solo (bars 7-14, -1.1 LU) and bars 31-36 (-3.0 LU).
- Both of those are balance cuts at solo crests (c19 B #1/#2).

The micro-fixes since c18 (joins, fills, entry leads) do not show up at this scale. The one global trend is down: the mp3's 4 s loudness change fell from 5.8 to 5.0 dB p90, under both slow-movement references.

Checked and fine:
- Ensemble onset spread on 12 multi-track entries (`spread.py`): IQR 10-125 ms, median arrival within ±0.05 s of the score. That is a plausible orchestra, neither machine-tight nor ragged.
- The solo margins in the A sections: horn, oboe and solo violin are 2-5.5 dB K over the rest of the orchestra.
- The B-section duets: Fl/CA at bars 41-44, where the CA is 2.2 dB over the flute at its crest.

What still sounds made by a machine is at the scale of the phrase. The printed high point of a phrase is not its loudest moment. The unmarked swells earlier in the phrase are as loud, and the crest is a single loud note followed by a drop. Each phrase therefore has two or three equal bumps instead of one arch. Inferred effect: the tunes sound evenly pressed rather than shaped. The weakest passages are:
- theme A in bars 23-30
- the horn solo in bars 7-14
- the end of theme B in bars 45-47

## 1. In the horn solo and in theme A, the printed crest is only 1.0-1.3 dB over the unmarked swell that comes before it, and the crest note falls 4-6 dB on the very next note. Measured; fix simulated

**Where.**
- Horn 1, bars 7-14 (qn 18-42). The swell is the p < > in bar 8 (qn 20-23); the crest is the < mp at bar 12 (qn 34), then > to p.
- Violins I and II, bars 23-30 (qn 66-90). The swell is the p < > in bar 24 (qn 68-72); the crest is the < mf at bar 28 beat 2 (qn 82), then a 5-beat > to p.

**Evidence (K-weighted, per beat, `kb.py`, c23):**
- Horn 1: bar 8 swell top -32.9 (qn 21). Bar 12 crest -31.9 (qn 34), then -35.9, -36.5, -37.2, -38.8.
  - The printed mp crest is +1.0 dB over an unmarked swell inside p.
  - c18 had the crest at -29.1 (+3.8). The c19 role `[33.5, 38.5, -1.0, 1.0]` lowered it. That role was set so the crest matched the same horn's p<mp in bars 67-70.
- Violins I: bar 24 swell top -33.5 (qn 69); bar 28 crest -32.2 (qn 82), +1.3 dB. The next beat is -38.2, a 6.0 dB fall in one beat. The printed > to p over 5 beats then continues -39.4, -41.8.
  - The c18 note (`SWELL_SOFT_GAIN_AT`) said the swell top should stay 2.2 dB under the printed mf. It is now 1.3 dB under.
- Master, p to mf from bar 23 to the bar 28 crest: +2.9 dB at the crest beat and +1.4 dB as bar averages. The fit over the movement gives 4 dB per dynamic level, so 8 dB is expected for two levels.
- Decrescendo shape (`dec.py`): in the lead lines the first beat of a > after a crest falls about twice the even rate:
  - Vln I 82-87: 3.8 dB against 1.9/beat
  - Horn 1 34-39: 3.2 against 1.4
  - BCl 96-99: 3.4 against 1.8
- Causes in the data:
  - Horn: the bar 8 swell gets the full untargeted soft hairpin step (`HP_STEP_SOFT` 22 CC). That is about 7 dB of CC on its own, even with `SWELL_NO_SOFT_GAIN`.
  - Violins: `SWELL_SOFT_GAIN_AT` +2.5 dB at 68.
  - The bar 28 Bb5 carries a +3.5 note trim (`note_trims.json` Vln I "82") that ends at the Ab5 (qn 82.85), where `vol_db` drops from +5.2 to +1.6 together with the CC fall.

**Fix (simulated in `sim.py` case F1, level only):**
1. `build/roles.json` "Horn 1": add `[20.5, 23.5, -2.5, 1.0]`. That is -2.5 dB on the bar 8 swell, closed by qn 23.5. Leave the c19 crest role as it is.
2. `tools/score_to_parts.py`: `SWELL_SOFT_GAIN_AT = {"Violins I": [240.0], "Violins II": [240.0]}`. 68 then falls through to `SWELL_NO_SOFT_GAIN`, which takes -2.5 dB off the bar 24 swell top. Keep 240, because the A2 theme has no mf crest after it.
3. `build/note_trims.json`: Violins I and Violins II add `"83": 2.5, "84": 1.0`. The Ab5 and G5 after the Bb5 crest then step down the 5-beat > instead of dropping 6 dB at once.

**Simulated result (c23 stems, per beat K):**
- Horn crest over the bar 8 swell: +1.0 -> +3.5 dB.
- Vln I crest over the bar 24 swell: +1.3 -> +4.1 dB. The fall after the crest: 6.0 -> 4.1 dB in the first beat.
- Master p (bar 23) -> mf crest: +2.9 -> +3.1 dB, and the swell bar 24 is 1.2 dB lower.
- Delivery unchanged: I -19.8, LRA 16.0, limiter 1.7, span 18.5. The 4 s p90 rises 4.99 -> 5.17.

Item 2 changes CC-free level only. Items 1 and 3 are volume envelope only, so the simulation is exact for level.

## 2. Bars 46-47: the B section's only mf, the oboe and cellos in unison, arrives softer than the crescendo before it. This is the weakest crescendo of the movement and has been since cycle 0. Measured; fix simulated

**Where.** Oboe 1 and Violoncellos, qn 146-151. They play p < mf > on C#5/C#4: a half note, then the repeated C# at the mf (bar 47, "poco rit."). Bassoon 2, Vln II, violas and basses play pp < mp >.

**Evidence:**
- Per-hairpin rise (`hp.py`), master, hairpin start -> arrival: +2.1 dB against an expected +7.4 for p -> mf (c00 +1.2, c18 +2.0).
- That is 28% of the expected rise. The median crescendo reaches 88%, and this is the lowest of all hairpins shared by two or more tracks. Single-track exceptions: timpani 200-203 33%, BCl 93-96 38%.
- Per beat, c23, K:

| qn | 145 | 146 | 147 | 148 (mf) | 149 | 150 |
|---|---|---|---|---|---|---|
| Oboe 1 | -39.6 | -39.6 | -37.3 | -34.9 | -37.5 | -37.1 |
| Vc | -42.7 | -41.7 | -42.5 | -37.4 | -39.0 | -40.9 |

  The bar 45 oboe (no hairpin printed) sits at -36.4. So the oboe's mf note is 1.1 dB under its own unmarked p bar, and the peak comes a beat early (qn 147, the crescendo's end on the tied half note).
- Causes:
  - Oboe 1 bar 45 is raised by role `[139, 151, 2.5]`, the note trims "144" +7 and "145.5" +3, and fills: `vol_db` is +7..+9.5 at 140-142.5.
  - The re-tongued C#5 at 148 (v100) starts from its attack inside the printed >.
  - In the cello the two C#4 are merged into one 5 qn note (146-151), and CC11 dips 70 -> 58 -> 69 exactly at 148.0. I did not trace which rule writes this 12 CC bow-change dip. It takes about 3 dB away on the mf downbeat.

**Fix (simulated, case F1):**
1. `build/roles.json` "Oboe 1": add `[140.0, 143.0, -2.0, 0.5]` (bar 45 down 2 dB) and `[148.0, 151.0, 3.5, 2.0]` (the mf held a beat, then opened across the >).
2. "Violoncellos": add `[148.0, 151.0, 3.0, 2.0]`.
3. In `score_to_parts.py`, limit the 148.0 cello dip to the soft bow-change notch (`BC_SOFT` `notch_soft` 3 CC), or skip it at a printed dynamic arrival.

**Simulated result:**
- Master from bar 45 to the mf: 147/148 now -30.6/-30.9 against bar 45 -35.4. The arrival is +4.5 dB, was +1.0.
- Oboe arrival -34.0 against its bar 45 -38.4.
- Vc -36.0 against the oboe's -34.0, so the oboe stays on top.

The CC dip fix is not simulated; it adds to this.

## 3. Phrase-scale loudness motion has fallen for five cycles and is now under both slow-movement references, because balance fixes lowered solo crests. Measured; the cause is partly inferred

**Evidence.** These are the largest beat-level changes in the master from c18 to c23 (`beatsK.npy`), and every one is a crest or peak that was lowered:
- bar 12 horn crest: -2.1 to -2.8 dB
- bars 32-33 BCl/CA: -2.2 to -5.2
- bar 42 CA crest: -2.7 to -2.9
- bars 75-76: -2.3 to -3.0 (the c20 build fix, which was right)
- bar 92: -2.4 to -3.5

The mp3 loudness motion follows: 4 s p90 5.80 -> 4.99 dB and phrase-scale 2.94 -> 2.84, against Brahms 1/ii 8.55/4.56 and 4/ii 6.29/3.92.

Each cut made sense against an absolute target ("a p<mp solo should not reach this instrument's f level"). But a listener hears level relative to the phrase. Five such cuts and no compensating lifts have made the soft half flatter. Inferred: this is the main reason the mockup still sounds evenly pressed after 23 cycles.

**Fix:**
1. Adopt as a loop rule for balance fixes: when a solo crest covers another voice, lower the covering voice or the accompaniment first. A crest is lowered only if it then stays 3 dB or more over the earlier swells of its own phrase. Finding 1 applies this to the horn: the swell is lowered, not the crest.
2. `tools/measure.py`, or `render_cycle.py` after `deliver_master.py`, should print two motion figures to `metrics.md` for the master and the mp3:
   - the 4 s short-term change p90
   - the 1 s vs 20 s detrended std

   The method is in `motion2.py`: momentary loudness at 10 Hz, the power mean over 1 s minus the power mean over 20 s, std. Treat a fall of more than 0.2 dB from the previous cycle as a regression the actor must justify in CHANGES.md.

## 4. Coda, bars 85-89: the clarinet's dolce pp solo, the last statement of the tune, is the only solo that sits under its accompaniment. Measured; fix simulated

**Where.** Clarinet 1, qn 283-292, over:
- Horns 3-4 con sord. pp
- violas unis. sul C pp, celli and basses pp
- from 286, Vln II pp and the timpani

**Evidence (`lead.py`, c23, K, 0.5 s frames):**
- Clarinet 1 median margin over the sum of all other stems: -2.7 dB, under in 81% of frames.
- Every other solo passage: horn +4.7, oboe +2.2/+4.3, solo violin +2.0/+5.5, CA bars 48-51 +2.7, horn bars 67-70 +5.3.
- Per beat, 286-291: Clarinet 1 -41.9, -39.1, -42.5, -42.5, -43.0, -45.3. Horn 4 -46.6..-49.0, Vla -44.8..-48.1, Vc -43.9..-46.3.
- The c23 B #4 lift on the Db5 (`[287.4, 289, 2.5]`) moved only that note.

**Fix:** `build/roles.json`:
- `[283.0, 291.5, -2.0, 0.5]` on Horn 3, Horn 4, Violas, Violas div, Violoncellos and Double basses
- Clarinet 1 `[283.0, 292.0, 1.5, 1.0]`

Simulated with the accompaniment cut alone: Cl1 median margin -2.5 -> -1.2 dB. With the +1.5 the median comes to about +0.3; that part is inferred, since it adds linearly in the level-only model. Master bars 85-87 fall by 0.4-1.6 dB.

One more point, inferred and not simulated: Cl1's first note tapers on CC11 from 41 to 32 before the breath at 286 (the `swell_taper` phrase-end rule), which is a 6.4 dB dip to -47.7 at qn 285. Under a pp that leaves a hole in the tune. Cap that taper at 4 CC for Clarinet 1 at 283.

## 5. Bars 48-52: the cor anglais's "solo, espr." runs at an exact metronome tempo. Measured tempo; effect inferred

**Evidence (`beatbpm.py`):**
- Bars 48-52 are 54/54/54/54, 54x4, 54/54/54/50, 54x4, 54/54/50/54: 18 of 20 beats at exactly 54.0.
- Phrase arcs cover every other exposed solo: horn, oboe, solo violin, flute B, CA bars 41-44 and the coda. This passage has none, because `PHRASE_ARCS` stops at (124, 140).
- Across the movement, the exposed solos now vary 1.3-2.3 bpm in std. Bars 48-52 are at 1.34 only because of the two stretched beats.

**Fix:** `tools/score_to_parts.py`: add `(152, 160, "sub"), (160, 168)` to `PHRASE_ARCS`:
- bars 48-49: sub-phrase, no push, x0.98/x0.95 on the last two beats
- bars 50-51: push to the middle, x0.96/x0.92 into the bar 52 violin entries

Neither arc touches `RAMP_SPANS` (150-152 ends at 152; 172-200 starts at 172). The entry leads follow the tempo map, as in c12.

## Do not touch

- The two climax builds (bars 57-61 f -> ff +6 dB; bars 75-78 +8.7 dB with the c20 `_all` rows) and the 1.3-1.8 LU gap between the climaxes.
- `deliver_master.py` as it is: LRA 16.0, span 18.5, limiter 1.7. c20 showed slower rides lift the second climax.
- The ensemble onset spread and the entry leads.
- The A-section solo margins.
- The Fl/CA duet balance in bars 41-44.
- The tempo map outside bars 48-52.
