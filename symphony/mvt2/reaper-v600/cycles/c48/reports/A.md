# Cycle 48, critic A (articulation and phrasing), on the c47 render

Task this cycle (loop/ONE_TIME.md): check the finale's shared techniques (symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md) against Movement II's own measurements. In this lens that means item 2 (sfp/fp), item 3 (sub. p), item 7 (FINAL_RING against c47's fade), item 9 (harp velocity cap) and item 10 (brass accent tilt jump), plus the c47 carry-overs.

## Sources and method

- **Render and data.** `cycles/c47/render/` (dry stems 01-32, returns 33-36, `00_Master.wav`) and `cycles/c47/rendered_build/parts.json`, which equals `build/parts.json`. Seconds come from the parts.json tempo map (`tools/pcx.py` `TM`). c46's render was used as the no-fade reference for the final chord: its six string stems and R Strings are sample-identical to c47's for the 10 s before qn 304 (difference energy under -300 dB).
- **Levels.** 30-50 ms RMS (5 ms hop) of the stereo stem. Fp drop = the 50 ms peak in [147.8, 148.35] qn minus the median over [148.6, 149.4].
- **Final-chord tail.** Measured with `check44.py`'s method: L0 = the mean over the 0.2 s before the note-off, t20 = the first time the master falls under L0 - 20 dB. Fades were simulated on the dry string stems as gains (the post-END fade is linear in dB in REAPER: measured -0.74 / -1.37 / -2.04 / -2.70 / -3.40 / -4.00 dB at +0.05 to +0.30 s). R Strings was interpolated between c46 (no fade) and c47 (-4 dB) in proportion to the fade's linear depth. This is exact for the dry stems and approximate for the return, which sits 12-17 dB under them.
- **Tilt.** 2-5 kHz energy minus 0.5-2 kHz energy (Hann window). Stem tilt jump = tilt over the first 80 ms from the moved onset minus tilt over the body (+0.25 to +0.6 s). Master tilt jump = the 80 ms after the score onset minus the 80 ms before it.
- **Oboe 1 fill and trim changes.** Simulated on the c47 stem from `score_to_parts.py`'s early-fill and `trim_shape` formulas, with critic A's c47 hole and 200 ms overshoot measures.
- **Scratch.** `/private/tmp/claude-501/mockup-loop/mvt2-c48-A/`, deleted at the end.

## Manual notes

MANUAL-READING.md has no row for cycle 48, so no reading group applies. MANUAL-GAPS.md was read. These are the manual pages I used for this cycle's items (May 2021 HO manual, PDF pages):

| Manual (PDF page) | Where in this mockup | Does the render follow it? |
|---|---|---|
| p.53: velocity cannot change during a note, so it sets the attack and the loudness of short notes; CC sets the dynamic of sustained notes. | The fp at bar 47 (qn 148): Violins II, Violas, Double basses. | No. The f is only a CC11 crossfade after the note has started. The basses' attack plays v57, the p velocity. Violins II and Violas reach the fp through a slur-legato transition at v124 (finding 1). |
| p.91-92: each string section has a Marcato Sustain patch, a marcato attack sample on top of the sustain, giving "extra power at the start of the note". | The fp notes. The rows exist: Sus Marc LITE (key 25) on the 2nd Violins and Violas KS Masters, Marc Sus LITE (key 73) on the Basses KS Master. | Not used. This is the fallback for finding 1. Movement I c47 found that strings Sus Marc LITE removed a 64-124 ms swell-in on cello strokes (`mockup-kit/README.md`). Not listed in MANUAL-GAPS. |
| p.69: Harp Sustain RR alternates pluck and thumb at velocity 1-123 and plays the Nail Pick at 124-127. | Harp (Sus RR) and Harp harmonics. | Yes. The harp plays v44-104 on 158 notes and the harmonics v58-70 on 3 notes. No note reaches 118 (finding 4). |
| p.101: brass Sustain Accent sets the attack loudness by velocity; Sustain Marcato puts a velocity-controlled low-pass on the attack. | Trombone 1's accents at 213 and 218. | Yes. Both play plain Sus MAX (v112, v92) with the GENTLE_ACCENT swell. Their attacks are darker than their bodies (finding 4). |

## Findings, ranked by what a listener hears

### 1. The bar 47 fp is heard as a late swell, not an attack: every part peaks 200-320 ms after the beat (measured; fix inferred from the finale's measured result)

**Where.** qn 148 (bar 47 beat 1), Violins II, Violas and Double basses. These are the only fp marks in v600. Each is printed fp with a decrescendo to pp at 151, after a pp crescendo from 146.

**What the score asks for.** No slur leads into bar 47 in any of the three parts:
- Violins II: `ges'2\< | eis'1\fp\>`.
- Violas: the slur `des2( bes2)` ends at 146.
- Basses: `cis,1\fp\>`.

The score comments call it a down-bow at the frog, "the strings' sf-p attack under the woodwinds' p chord".

**What plays (read in parts.json).**
- **Violins II.** The 148 note is a Leg Slur MAX legato target at v124 (keyswitch at 147.815), overlapping the 146 note. Its transition starts 240 ms before the beat.
- **Violas.** Also a Leg Slur MAX legato target at v124 (the row has been on since 138.5). The transition starts 226 ms before the beat.
- **Basses.** A Sus MAX re-attack at **v57** (the p velocity), 159 ms before the beat.
- **CC11 spike.** In all three, CC11 sits at 46 at the moved onset (Violins II and Violas dip to 42 at 148.0). It jumps to 84-88 at 148.02 (+21 ms), holds to 148.188 (+196 ms) and is back at 46 by 148.4 (+417 ms). So the attack is played on the p layer and the f arrives as a crossfade.

**Is the spike overwritten?**
- **CC11.** No. The decrescendo printed at 148 starts after the spike points, and the spike is intact on all three tracks.
- **Volume envelope.** On the basses only, the 146-148 crescendo's dB gain is released under the attack: vol_db goes -0.63 → -1.33 → -2.62 dB at 147.897 → 148.0 → 148.147. On Violins II and Violas the envelope is flat across the spike (-1.5 → -1.7 and -0.5 → -0.6).
- **Trap when porting FP_SPIKE_AT_MARK.** If FP_SPIKE_AT_MARK is ported without the finale's hairpin shift (mvt3 `score_to_parts.py` line 1980, `fp_hp`), the decrescendo's own points at 148.0 are added after the mark's f point at the same qn. `value_at()` lets the later point win, so the curve would read p at the mark and ramp up into the f: a worse swell than now.

**Measured on the stems (dB re full scale, times re the beat):**

| part | crescendo end | peak | peak time | p after | own drop |
|---|---|---|---|---|---|
| Violins II | -54.3 | -45.9 | +293 ms | -51.5 | **5.6** |
| Violas | -52.6 | -41.2 (transition bump) / about -42 (the CC11 spike) | -87 / +200..+250 ms | -52.3 | 10-11 |
| Double basses | -52.4 | -39.6 | +323 ms | -48.6 | **9.0** |
| Master | -39.0 | -34.8 | +353 ms | -35.2 | 0.3 |

- **Slow attacks.** In the first 100 ms after the beat, Violins II sit 4-7 dB under their peak and the basses 6-10 dB under theirs.
- **No attack brightness.** The basses' 2-5 kHz band rises 8-10 dB only at +250..+350 ms, together with the level. Their tilt stays at -17 to -18 dB throughout, so there is no attack transient.
- **The master.** It shows no drop because Oboe 1 enters mf at 148 (oboe -36.4 dB after the beat). In the master the fp can only be an accent in the accompaniment on the downbeat, and at present that accent arrives a third of a second late.
- **Finale target.** Each part's own drop should be 10 dB or more. Violins II (5.6) and the basses (9.0) miss it.

**Fix (`tools/score_to_parts.py` port from mvt3, and `build/score_config.py`).**
1. **Port `FP_SPIKE_AT_MARK` and `FP_VEL`** from mvt3 (`score_to_parts.py` lines 772-778, 1820, 1865-1873, 1980, 3248-3249). The `fp_hp` hairpin shift at line 1980 is required (see the trap above). Set `FP_SPIKE_AT_MARK = True` and `FP_VEL = 96`. The basses' 148 note then plays v96 instead of v57, and every led fp note's pull carries the f level from its moved note-on.
2. **Make the fp notes fresh strokes:** `DOWNBOW_STROKE_AT["Violins II"] = [148.0]` and `DOWNBOW_STROKE_AT["Violas"] += [148.0]`. They then play Sus MAX instead of slurring from 146, with the entry lead, the pull and velocity 105 or more. This is the existing path used for Violas 69/87/248.5 and the basses at 144.
3. **Shorten the spike.** `FP_SPIKE = ("f", 0.12, 0.30)` qn, which is 125 ms / 312 ms at bar 47's 57.6 bpm, close to the finale's `FP_SPIKE_S` (0.10, 0.30) s. The c34 lengthening to (0.2, 0.4) was made while the attack was on the p layer. Keeping the qn form avoids porting `FP_CHECK_AT`, which the seconds form needs for the fp WARNING check (line 3643 reads `FP_SPIKE[2]`).
4. **Check the envelope after the build.** In parts.json vol_db, between each fp note's moved onset and 148.3: where a crescendo dB gain is released in that window (as on the basses now), hold it to 148.3 with a `LEVEL_SHAPES` term and release it with the decrescendo.

**Pass criteria for the render (measured on the stems):**
- Each part's 50 ms peak between -0.05 and +0.10 s of the beat.
- p reached within 3 dB by +0.35 s.
- Each part's own drop at least 10 dB. Where a part is short of 10 dB, add a `roles.json` row of -(10 - drop) dB, at most -8, over [148.3, 151.0]. That is the finale's item 2. The sends are post-fader, so the returns keep ringing (S3 holds).
- No rise of more than 2 dB in the 0.2 s before the beat. The f pull starts at the moved onset, while the cut 146 note's release still sounds.
- Master tilt jump at 148 of +3 dB or less. Weight, not bite.

**If the attack still swells in** (peak later than +0.1 s), put the three notes on the Sus Marc LITE / Marc Sus LITE row with `ART_SPANS` (p.91-92; Movement I c47's cello result). That loads a new row, so it is a full rebuild of those three tracks.

**Expected result (inferred).** On the finale the same port took each part's own drop at the sfp to 10-17 dB and the master's drop from 6.2 to 10.5 dB. Here the master should show a 2-4 dB accent at the beat instead of a rise at +350 ms.

### 2. The final chord now falls 20 dB in 0.40 s; a -1.0 dB post-END fade gives 0.44 s, and FINAL_RING is not needed (measured by simulation)

**Where.** qn 304, the final chord's release: Violins I, Violins II, Violas, Violas div, Violoncellos and Double basses (c47's `LEVEL_SHAPES` [(304.0, 0), (304.1, -4.0)]).

**Measured (master, check44 tail).**

| case | t20 | t10 | drop at +0.3 s |
|---|---|---|---|
| c46 render, no fade | 0.475 s | | 9.1 dB |
| c47 render, -4 dB fade | **0.400 s** | | 14.2 dB |
| c47 with the strings and R Strings of c46 (no fade) | 0.465 s | | 10.3 dB |

The last row differs from the c46 render only through Clarinet 2's 30 ms entry shift, which changes how the stems sum at -67 dB.

Fade depth over 0.1 qn (0.30 s at 20 bpm), simulated:

| fade | t20 | t10 | drop at +0.3 s |
|---|---|---|---|
| none | 0.465 s | 0.305 s | 10.3 dB |
| **-1.0 dB** | **0.440 s** | 0.285 s | 11.3 dB |
| -1.5 dB | 0.430 s | | 11.8 dB |
| -2.0 dB | 0.425 s | | 12.3 dB |
| -2.5 dB | 0.420 s | | |
| -3.0 dB | 0.415 s | | |
| -4.0 dB | 0.400 s (matches the render) | | |

A longer fade (0.2 qn) at -3 or -4 dB gives 0.420 s.

**Decision.** The window allowed by the 0.45 s limit and the recordings' 0.43-0.55 s is 0.43-0.45 s. FINAL_RING is the finale's tool for a chord that fell too fast: 0.27 s, raised to 0.42 s by holding the notes 0.45 s past the end. Here the same chord with no fade already takes 0.465 s. Holding it longer moves t20 the wrong way, and it would also change the note ends, under the fitted final-chord re-bows and fills. So drop FINAL_RING for Movement II and keep c47's post-END path at a smaller depth.

**Fix.** In `build/score_config.py` (c47 block), change the six string tracks' shape from `[(304.0, 0.0), (304.1, -4.0)]` to `[(304.0, 0.0), (304.1, -1.0)]`.

Expected: t20 0.44 s, drop at +0.3 s 11.3 dB, and a gentler fall than c47's on every stem. After the render, re-check t20 with check44. The renders now repeat (CC16 reset; c46 → c47 sample-exact), so the simulated value should hold within about 0.01 s.

### 3. Oboe 1's eighths at 142 / 142.5 sit 4.5-5.5 dB under the dolce espr. line; note trims restore them better than longer fills (measured by simulation)

**Where.** Oboe 1, bar 45 beats 3-4 (qn 142 E flat 5 and 142.5 D flat 5), inside the p "dolce espr." phrase 139-148. Carried from c47.

**Measured on c47 (note bodies, median over the middle 60 % of each note).**

| note | stem | master |
|---|---|---|
| 142 | -49.8 | -43.4 |
| 142.5 | -49.9 | -43.0 |
| neighbours 140 / 143 / 144 / 145 | -44.0 / -44.5 / -45.6 / -46.3 | 140: -40.8, 143: -40.7 |

c47's join holes: 142 3.0 dB, 142.5 4.3, 143 1.3. The 200 ms overshoot at 142 is +1.5 dB.

**Two fixes simulated on the c47 stem:**

| change | bodies 142 / 142.5 (stem) | master | holes 142 / 142.5 / 143 | overshoot at 142 |
|---|---|---|---|---|
| c46-length holds (0.30 / 0.28 s) | -47.2 / -49.2 | | 4.2 / 6.9 / 1.3 | |
| note trims +3 / +3, fills as in c47 | -46.8 / -46.9 | -42.4 / -42.2 (+1.0 / +0.8) | 3.5 / 5.4 / 4.2 | +2.6 |

The longer holds raise 142 only and open a 6.9 dB hole at 142.5. The trims raise both eighths. +4 / +4 deepens the 143 hole to 5.2 dB.

**Fix.**
- `build/note_trims.json` "Oboe 1": add "142": 3, "142.5": 3.
- `build/score_config.py` `NOTE_TRIM_RAMP_S["Oboe 1"]`: add 142.0: 0.1, 142.5: 0.1.
- Keep the c47 fills.

Effect: a 1 dB lift in the master on two eighths of the solo line. It is the smallest change in this report, so do it only if the cycle has room.

### 4. Items 3, 9 and 10 need no audible change in Movement II (measured)

**Item 3 (sub. p): not applicable.**
- **The score.** v600 prints no "sub." mark. A scan of the event list for drops of one level or more with no decrescendo, under sounding notes, finds only:
  - the fp at 148 (finding 1);
  - the sf at 212, which is followed by a printed decrescendo;
  - entries after rests.
- **qn 195-196 is a short dip into a breath, not a sub. p.** The master goes from -25 dB (195.2) to -29/-28 (195.54-195.75) and back to -25/-24 at 196.0-196.2. The steepest 10 ms master fall there is 3.1 dB (at 195.67). R Strings (-55..-57) and R Winds (-42..-45) keep ringing through the breath, so S3 holds.
- **PHRASE_SHAPE "drop".** It cannot apply. Bars 53-64 (qn 172-220) are a skip span, and no fp track has a phrase at 148. parts.json lists no lyrical phrase in 172-220.
- **HELD_DECRESC_CARRY.** It has nothing to carry: `HELD_DECRESC_DB` is off in Movement II, and every track's `held_decresc` and `subito_falls` is empty.
- **The "-4 dB on fresh brass entries" rule.** No brass enters at a drop.
- **Verdict.** Do not port item 3.

**Item 9 (harp cap 123): a guard only.**
- The harp plays v44-104 (158 notes) and the harmonics v58-70 (3). None reaches 118.
- Porting `HARP_VEL_MAX` (mvt3 lines 779-781, 5777-5778) with 123 changes nothing in parts.json. Adopt it as a safeguard, or skip it; nothing audible depends on it.

**Item 10 (tilt jump): Trombone 1's accents pass as weight, not bite.**

| onset | stem: 2-5 kHz first 80 ms - body | stem tilt jump | master tilt jump |
|---|---|---|---|
| 213 | -13.0 dB | -3.4 dB | -1.8 dB |
| 218 | -13.8 dB | -5.6 dB | -1.9 dB |

- The old "2-5 kHz jump" read +1.9 dB at 213, the entry over the pickup. The tilt jump shows the attack is darker than what was sounding.
- The brightest Trombone 1 onsets are the slurred transitions 215.0 / 215.5 (stem tilt jumps +4.6 / +3.3 dB). They are masked in the master (-5.6 / -1.8).
- The bars 61-62 molto sostenuto brass tenutos have stem tilt jumps from -16 to +1.5 dB.
- The one positive master value, +4.8 dB at 206, comes from the strings (celli +4.7 dB tilt jump), not the brass.
- No change.

### 5. The c47 carry-overs that need no change, with the measurement

**Bass clarinet 265 "lost its own-band dip (12.8 → 1.5 dB)": an estimator artefact.**
- The note data at 265 is unchanged, with a 63 ms gap before it. The broadband stem dip is 5.8 → 5.5 dB and the master dip 3.8.
- Band dips c46 → c47:
  - 60-300 Hz: 7.8 → **17.4 dB**
  - 300-1000 Hz: 7.1 → 5.4 dB
  - 1-4 kHz: 6.2 → 7.1 dB
- `s1check44.py`'s own band takes harmonics 1-4 within ±3 % from a 60 ms FFT (16.7 Hz bins). For this C sharp 3 that is no bin at all for h1 (139 Hz), one bin each for h2 and h3, and two for h4. The reading swings with one bin: h3 went -13.7 → -1.4 while h2 went -6.9 → -16.7.
- The separation is there, and stronger in the low band. For low notes the S1 tool should use a frame long enough for 3 or more bins per harmonic (0.2 s under 200 Hz) or ±6 %.

**Horn 4, qn 84 (7.6 s, pp): a loop-seam dip.**
- The stem minus its envelope falls from -48.3 dB at +1.5 s to -54.9 at +2.5 s and returns to -46.0 at +3.5 s. That is a 7-9 dB dip at +1.75..+2.75 s. A second, 4 dB dip falls at +4.75..+5.0 s.
- The horn sits 12-15 dB under the master there (-40..-42).
- An optional `build/loop_fills.json` "Horn 4": {"84": [[2.3, 5.5, 0.8]]} (seconds after the moved start, dB, width) takes the largest 1 s swing from 9.2 to 6.8 dB. The rest is a dip at +0.75 s in the attack phase. Not audible in the master either way; skip it unless the cycle is idle.

**Movement I c51 lessons.**
- *Winds ×1.4.* On the c47 dry stems, the lyrical wind phrases (parts.json `phrase_shape`) rise as much as the horn phrases. I measured the 75th percentile over 0.25-0.65 of each phrase against its first 0.5 s: median +6.1 dB on 14 wind phrases against +4.2 on 3 horn phrases. So the rise does not support scaling the wind offsets.
- The taper (the phrase's peak against its last second) is smaller on the winds: median +3.0 dB against +9.2. Two low cases:
  - Oboe 1 139-151 ends into the crescendo to mf at 148 (-0.3 dB), which is correct.
  - Bassoon 1 18-29, a pp line under Horn 1's theme with no hairpin, measures -0.2 dB: its planned -2.5 dB end offset did not show.
- If anything is scaled, it is the wind end offset, not the rise: a `PHRASE_SHAPE["level"]["wind"]` key (looked up by family, `score_to_parts.py` line 5637) equal to the default with ("end", 0.0, -3.5).
- The estimator includes each note's sample level and covers only 3 horn phrases, so this is a weak result. Measured, low priority.
- *Inner held notes.* c47 made no held-note dynamic change. Finding 1 changes only the three fp notes, which sit 12-16 dB under Oboe 1 after the fall (-51.5 / -52.3 / -48.6 against -36.4).

## Do not touch

- c47's post-END fade path (change only its depth, finding 2) and its fitted final-chord re-bows and fills.
- The c47 Oboe 1 fills' pre_s values.
- Trombone 1's Sus MAX accents, CC7 lanes and velocities (v112, v92).
- The harp setup (Sus RR at v44-104, harmonics on the soft layer, rolls, the étouffez at 274).
- The celli's 148 down stroke at mp.
- The bars 61-64 tenutos, tremolos and sf shapes.
- CAESURA_LIFT and the c46 caesuras.
- The Violins II portato pairs (bars 15-21) and the violas' portato (bars 48-51).
- The CC15 mute placement.
