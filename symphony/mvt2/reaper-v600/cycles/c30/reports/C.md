# Cycle 30, critic C: dynamics over time (on the c29 render)

Scope: loudness arc of the whole movement against the score, hairpins, the bar 47 fp, the animando crescendo of bars 53-60 into the Largamente climax, the niente of bar 66, the ff cadence 79-82, the coda and the bar 91 morendo, the master and the delivered mp3 (BRIEF item 6), swells and loop pulsing (item 8), decays. Levels are stereo-power RMS on the c29 stems and master (they sum to the master exactly, residual -202 dB), and EBU short-term loudness at 10 Hz. "Smax" means the maximum short-term loudness in a bar. Simulations multiply the c29 stems by the proposed dB shapes, sum them, and run a copy of `tools/deliver_master.py` with its constants overridden. The copy reproduces the c29 mp3 within 0.2 LU.

## Manual notes (MANUAL-READING row 30, slot C: D1 pp. 53-54, 64; A3 pp. 75-81; B3 pp. 123-126; plus MANUAL-GAPS.md)

| Manual (PDF page) | Where it applies here | Followed? |
|---|---|---|
| p.53: velocity shapes short notes; CCs shape sustained notes mid-note | every sustained line (CC11 shapes); pizz. bars 41-44, harp, timpani strokes (velocity) | yes (read in parts.json) |
| p.64: in HO strings and woodwinds CC11 sets loudness and dynamics and CC1 sets vibrato. CC7 sets a level relative to the other instruments; CC11 shapes. | all strings and woodwinds | Mostly. Relative levels sit in REAPER's post-hall volume envelope, not in CC7, and CC7 is used only on Violas 152-168. Finding 4 proposes CC7 for a fade, which goes against the manual's split of roles. The reason is S3: CC7 acts before the hall. |
| p.75, p.81: the Solo Violin links dynamics and vibrato on CC1; LegSus | the bars 17-22 solo (DIV A track) | Not installed (MANUAL-GAPS #3). The DIV A track shapes with CC11 plus volume. Its crescendos grow +2.1 dB (48-51) and +4.6 dB (60.5-62.5), measured. That is acceptable. |
| p.124-125: Felt Rolls (KS D#0), CC1 crossfades 8 layers for crescendos and decrescendos | ppp rolls bars 2-3 and 67-70; crescendo rolls 168, 200, 261 | yes (CC1 layers since c28). The ppp roll 226-237 falls -55.5 to -58.5 dB, measured. |
| p.123, p.125: Felt Cresc (KS E0), recorded crescendos, "the most realism" | crescendo rolls 168-172, 200-203, 261-262 | no (MANUAL-GAPS #7, still open) |
| p.124: Felt Short (KS C#0) gives realistic stops and damping | printed "damp" at 173 and 210 | No. The 172 stroke decays naturally: -45 dB at the stroke, -61 at 173, -76 at 174.5. That ring sits 15-25 dB under the strings, so it is inaudible (measured). The 210 ring sits under the ff tutti. No change needed. |
| p.123: Felt Long gives double hits within 65 ms | none (no strokes closer than 65 ms) | n/a |

## Findings, ranked by what a listener would hear

### 1. The delivery master halves both long crescendos and flattens bars 54-59 (measured)

**Where:** delivered mp3, bars 52-61 and 70-79.

**What is wrong:** the master's arc is right. It rises 19.9 dB from bar 52 to the climax (Smax) and 16.2 dB over bars 71-78. The mp3 keeps only 10.3 dB (52%) and 6.6 dB (41%). In the mp3, bars 54-59 of "poco a poco animando ... cresc." form a plateau at -18.7, -18.2, -17.8, -19.3, -17.6 and -17.5 LUFS: bar 57 is 1.5 LU under bar 56, and the f arrival at bar 59 (qn 196) is 0.1 LU over bar 58. The listener hears the growth only in bars 60-61.

**Cause:** the gain ride is +11.1 dB at bar 52 and +3.9 dB at bar 59, so it removes 7.2 dB of the crescendo. `tools/deliver_master.py` uses `RATIO, KNEE_BELOW = 3.0, 5.0`, taken from movement I c36. With them the delivered LRA is 14.0 LU and the span 16.3 dB, both at the bottom of the BRIEF targets. The loudness motion is 3.16 dB, against 3.92-4.56 dB in the two Brahms slow movements in LEARNINGS §16. The 5 s moves check passes (94% kept, 0 inversions) because these crescendos last 30-40 s; add a check of the rise across each long printed crescendo.

**Fix:** in `tools/deliver_master.py`, set `RATIO, KNEE_BELOW = 2.0, 6.0`. These are the values recommended in `loop/DYNAMICS-RESEARCH.md`. Alternatively, pass `DELIVER_RATIO=2.0 DELIVER_KNEE_BELOW=6` from `render_cycle.py` for movement II.

Simulated on the c29 master:

| Measure | Current | With 2.0 / 6.0 |
|---|---|---|
| LRA | 14.0 LU | 16.0 LU |
| p10-to-max span | 16.3 dB | 18.3 dB |
| Limiter | 1.1 dB | 2.1 dB |
| Inversions | 0 | 0 |
| 5 s moves kept | 94% | 91% |
| Rise bar 52 to climax | 10.3 dB | 12.6 dB |
| Rise bars 71-78 | 6.6 dB | 9.2 dB |
| Bar 1 | -26.3 LUFS | -25.3 LUFS |
| Coda bars 83-84 | -29.1 / -29.0 LUFS | -29.6 / -29.2 LUFS |

The soft passages stay as audible as now.

**Rejected:**
- `LIFT_SMOOTH_S` 8-12: the coda falls 1.5 dB.
- `TOP_RATIO` 1.6: the limiter reaches 3.2 dB together with finding 3.

### 2. Bars 55-58: the strings' mf of bar 56 is louder than the crescendo that follows (measured)

**Where:** Violins I, Violins II and Violoncellos, qn 184-196.

**What is wrong:** printed, the strings arrive at mf at 184, crescendo from 188 and reach f at 196. In the master, qn 184 peaks at -26.5 dB and the level falls to -30.1/-30.2 at 188-189. Bar 57's Smax is only 0.3 LU over bar 56.

The stems show the same reversal:

| Stem | Bar 56 (mf) | Bar 57 | Bar 58 | Bar 59 (f) |
|---|---|---|---|---|
| Violins I | -32.1 | -35.3 | -35.0 | -34.3 |
| Violoncellos | -32.0 | -37.1 | -34.0 | -31.8 |

The hairpin check reads Violins I 188-195 at 0.0 dB, Violoncellos 180-184 at -2.3 and Flute 1 188-195 at -3.5. The celli are cut inside their printed crescendo by `roles.json` [188,190,-1.5] and `note_trims.json` 190 -1.5, on top of [190.5,204,-3,4] and 193 -3.

**Fix:**
- `build/score_config.py` `LEVEL_SHAPES`:
  - Violins I: `[(183.5,0),(184.25,-2.5),(187.75,-2.5),(188.5,0)]` and `[(190,0),(195,2),(204,2),(206,0)]`.
  - Violins II: the same two shapes with 1.5 dB in place of 2.
  - Violoncellos: `[(183.5,0),(184.25,-2.5),(187.75,-2.5),(188,0)]`.
- Delete the Violoncellos role [188,190,-1.5] and the note trim 190 -1.5. Keep 193 -3 and [190.5,204,-3,4], because the balance needs them.

**Simulated result:**
- Bar 57 is 2.6 LU over bar 56 in the master; with finding 1, 1.2 LU in the mp3. Delivered bars 56-59 read -19.7, -18.5, -16.4, -16.3.
- Violins I bars 56-59: -34.5, -35.3, -33.4, -32.3. Violoncellos: -34.5, -35.7, -33.7, -31.8, so the celli stay level with or under the violins.
- Bar 61 is unchanged within 0.3 dB.

**Inferred:** the 2 dB release over 204-206 should be masked by the ff tremolo. Check bar 61's first two beats on the render.

### 3. The climax is barely louder than the ff cadence (measured)

**Where:** bars 61-62 against 79-80.

**What is wrong:** BRIEF item 6 asks for the climax to stay clearly the loudest. In the master, bars 61-62 (Smax -12.0 / -12.0) are only 2.3 LU over bars 79-80 (-14.3 / -15.2). In the mp3 the gap is 1.2 LU (bar 62 -10.7 against bar 79 -11.9), and 1.1 LU with finding 1. The top ride (2.5:1 above loud - 3) takes the rest.

**Fix:** `LEVEL_SHAPES["_all"]` += `[(203.75,0),(204.25,1.0),(211.5,1.0),(211.9,0)]` and `[(261.75,0),(262.25,-0.8),(267.75,-0.8),(268.25,0)]`. The shapes end before the 212 sf, and bar 63 holds the limiter's peaks.

**Simulated result:** master gap 4.0 LU. In the mp3, 2.0 LU (limiter 1.6 dB) on the current delivery, or 1.8 LU (limiter 2.6 dB) with finding 1. Bars 81-82 are unchanged.

### 4. The bar 66 niente does not fade; it ends with the note release (measured)

**Where:** Violins II, Violas and Violoncellos, qn 223-226. The decrescendo runs from the printed down-bow on the tied note at 223 to niente at 226.

**What is wrong:** CC11 falls 33 to 12, but over 223-226 the stems fall only 3.5 dB (Violins II, -44.9 to -48.4), 4.0 dB (Violas) and 4.6 dB (Violoncellos). The rest of the fall, 25-30 dB, happens in the 0.5 s release after 226.

On the violas, the re-bow fill `rebow_fills.json` "Violas" "223" holds +2.98 dB from 1.48 s to 3.45 s, which works against the decrescendo. The violas' volume envelope rises from +4 to +7.3 dB across the hairpin. A listener hears a level hold and then a stop, not a fade to nothing.

**Fix:**
- `CC7_POINTS` for "Violins II", "Violoncellos" and (appended) "Violas": a ramp in 0.125 qn steps from (223.5, 127) to (226.0, 25), i.e. -14 dB, back to 127 at 236.9, before their next notes at 237/238. Use CC7 because it acts before the hall (S3), so the hall ring fades with the line.
- Set the Violas 223 fill's hold points (1.48-3.446 s) to 0 dB.

**Simulated result (stem gain only):**

| Stem | 225-226 now | 225-226 after | 226-226.5 now | 226-226.5 after |
|---|---|---|---|---|
| Violins II | -48.4 | -56.4 | -57.4 | -71.5 |
| Violas | -53.4 | -65.0 | | |
| Violoncellos | -58.3 | -65.9 | | |

The upper strings now fade 11-12 dB through the hairpin. The master over 225-225.9 goes -44.6 to -48.1; the basses' 4 soli pedal (-50) carries the rest, as printed.

### 5. Unprinted 6-8 dB swells on soft accompaniment notes (measured)

**What is wrong:** long notes with no hairpin, at pp/ppp, rise 6-8 dB and fall back inside the note:

| Note | Swell | Where it peaks | Notes |
|---|---|---|---|
| Bassoon 2 B♭2, qn 140 (bar 45, under Oboe 1's solo) | +7.7 dB | -54 to -46 at +2.0..+2.75 s, then back to -54 | |
| Bassoon 2 B♭2, qn 26 | +5.7 dB | +1.75..+2.75 s | |
| Violas, qn 42 (bar 15, under the oboe) | +7.6 dB | by +2.5 s | follows a CC11 swell 34 to 38 near a layer edge |
| Violins II, qn 108 | +7.1 dB | | CC11 35 to 38 |
| Violins II, qn 0 (ppp) | +6.8 dB | by +1.2 s | CC11 22 to 26 |

Bassoon 2 B♭2 is already capped at CC 34 (`SWELL_CC_CAP`), so its swell is in the sample itself, as LEARNINGS §4 records for c23. **Inferred:** in a pp texture a 7 dB rise on an inner part is heard as a pad that breathes, which the score does not ask for.

**Fix:**
- `LEVEL_SHAPES_S["Bassoon 2"]` += `(140.0, [(1.2,0),(1.75,-4),(2.75,-5),(3.2,0)])` and `(26.0, [(1.3,0),(1.9,-4.5),(2.75,-4.5),(3.1,0)])`.
- `SWELL_CC_CAP` add `"Violas": {"*": 0}` and `"Violins II": {"*": 0}`. This holds CC11 on long notes starting at CC 40 or less and moves the swell to the envelope; LEARNINGS §4 measured the median pp swell going 3.3 to 1.2 dB.
- Re-measure the swells on the render (aim at most 3 dB).

### 6. The bar 47 fp spike is short and weak on the violins (measured level, inferred perception)

**Where:** qn 148 (`FP_SPIKE = ("f", 0.12, 0.25)`, generic default).

**What is wrong:** the spike lasts about 0.13 s at the poco rit. tempo. It peaks 5 dB over its body on Violins II (-42.8 against -48), 6-9 dB on the violas and 10 dB on the basses. The master rises only 3.3 dB for 0.3 s under Oboe 1's mf line (-36 to -38). The drop is in CC11, so S3 is met.

**Fix:** `FP_SPIKE = ("f", 0.2, 0.4)` in `build/score_config.py` (movement II only; this is the only fp). **Inferred:** about +2 dB more peak on the violins. Check that the spike stays under 3 dB over Oboe 1 in the master.

## Checked and fine (measured)

- **Loop pulsing (item 8):** no held passage shows loop periodicity any more. The 100-300 Hz band autocorrelation at 3.95 s is -0.46..+0.10 and the centroid's is at most 0.06, over 12 held passages: Vln I 0-9, BCl/Hn4 bars 3-6, Cb 221-238 and 274-292, Timp 226-237, Vc 274-286 and 286-301, Vln II 286-301, Violas div 279-301, Hn3 286-297, and the master over 274-301. On the final chord the master reads -0.76 / -0.40.
- **Morendo and coda:** master bars 89-92 read -40.1, -41.7, -45.3 and -51.1 dB. The final chord is 9.1 dB under the opening chord, and in the mp3 bar 92 is 7.5 LU under bar 1. The release after the fermata falls 52 to 73 dB in about 1.25 s, a natural hall decay, and the file keeps its tail.
- **The rest of the arc:** bars 60-61 rise 7 LU in the master. The 82 to 83 decrescendo into the coda is smooth. 96 of 115 crescendos of 1 qn or longer rise at least 1 dB (median +4.6 dB) and 106 of 112 decrescendos fall at least 1 dB (median -5.8). Apart from those named in findings 2 and 5, the shortfalls are harp arpeggios, phrase-end dips and entries.

**Do not touch:** every re-bow and fill on the held notes (no loop periodicity left); the coda balance and the morendo steps; the timpani ppp roll decrescendo 226-237; the CC11 fp and breath dips (S3 is met); the delivery's 5 s smoothing and its tail handling; the climax tremolos and Trombone 1's quotation shapes; the c29 Cb/Vc fill offsets.
