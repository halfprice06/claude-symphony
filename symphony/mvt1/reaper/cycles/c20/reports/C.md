# Cycle 20, critic C: holistic comparison (render c19)

## Method

I compared the c19 render (`cycles/c19/render/`, `cycles/c19/rendered_build/parts.json`) with c00, with c14 (five cycles back), with the Dvořák 9/i reference (lossy MP3, decoded to 48 kHz) and with the stored measurements of Brahms 1/i (musopen, lossless; `symphony/render/critics/c00/ref_brahms1_i_musopen/metrics.json`). Note times use each cycle's own tempo map.

Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c20-C/`:
- `bars.py`: bar levels against the printed dynamic;
- `feat.py`, `shape.py`, `low2.py`, `lowpass.py`, `simlow.py`: level-binned band shares, loud-minus-soft spectral shape, and an EQ simulation on the stems;
- `solos.py`, `lumpy.py`: solo margins, and note-to-note jumps inside connected melody lines;
- `rr.py`, `alt.py`: repeated-note patterns;
- `loopchk.py`, `loopmaster.py`, `acc25.py`, `accfront.py`, `onsetshape.py`: brief items 7 and 8;
- `decay.py`, `ferm.py`: cut-off decays;
- `simwidth.py`: a stereo-width simulation.

Levels are RMS dB unless stated otherwise.

## State of the render (measured)

**What has improved since c00:**
- Note-level work: the share of connected melody-note pairs that jump more than 6 dB fell from 13% (c00) and 12% (c14) to 6%.
- Solo margins: the Lento cor anglais is +3.5 dB over the loudest other stem (c00 +1.2), and the bass clarinet and flute solos rose by 4-9 dB.
- Brightness: the loud tutti's 2-5 kHz share is -10.9 dB against the Dvořák reference's -11.1 (c15 was -9.8).

**The macro shape has not moved.** Fitted to the printed dynamic and the number of staves playing, bar levels give:

| | c00 | c19 |
|---|---|---|
| dB per dynamic step | 2.61 | 2.62 |
| Residual SD | 3.04 | 3.13 |

**Brief item 7 (loop pulse) passes.** Master autocorrelation at 3.95 s, 100-300 Hz band / centroid:

| Passage | Band | Centroid |
|---|---|---|
| Lento 5-12 | -0.07 | +0.09 |
| Bars 43-46 | -0.20 | +0.11 |
| Coda 175-178 | -0.07 | +0.04 |
| Tempo I 179-182 | -0.37 | -0.09 |

The final-chord stems are between -0.14 and +0.13. Single notes longer than 10 s (tam-tam, Bassoon 2 at 476) are at or under +0.04.

**Brief item 8 (accents) passes.** 2-5 kHz in the first 80 ms minus the 0.12-0.4 s body, on the stems:

| Family | n | Median | p90 |
|---|---|---|---|
| Strings | 171 | -8.5 | -3.9 |
| Winds | 234 | -11.1 | -4.6 |
| Brass | 172 | -10.2 | -4.7 |

The one outlier is Violas 536 at +7.9, the c19 bar-135 bump, which is masked on the master. Master accent fronts have a median of -1.9 dB (c00 -1.2). Loud master onsets reach body -1 dB in 10 ms; Dvořák takes 20 ms.

What follows is ranked by how much a listener would gain.

## 1. The loud tutti has become bass-heavy below 100 Hz since c15, the opposite of a real orchestra (measured; the fix is simulated)

**Where.** Every f/ff/fff tutti, the most in:
- bars 82-83 and 117-123;
- bars 131-142;
- bars 158-161.

**Evidence: band level relative to 250 Hz-2 kHz.** "Loud" is the loudest 10% of 0.4 s frames; "soft" is the softest 30% of active frames.

| | 30-60 Hz loud / soft | 60-100 Hz loud / soft | 100-250 Hz loud / soft |
|---|---|---|---|
| Dvořák | -41.2 / -25.9 | -23.3 / -15.6 | -4.4 / -7.8 |
| c00 | -31.1 / -27.5 | -15.6 / -12.8 | -9.3 / -5.0 |
| c14 | -29.6 / -25.0 | -18.6 / -10.5 | -9.8 / -5.5 |
| c19 | -26.2 / -27.7 | -13.4 / -11.3 | -7.5 / -5.1 |

The absolute low end of one lossy recording is not a target (LEARNINGS 14). The direction, though, is the same in both references:
- From soft to loud, the sub-bass and 60-100 Hz fall and the 100-250 Hz body rises.
- Loud-minus-soft shape at 39/79/157 Hz: Brahms 1/i -4.5/-4.7/+2.8, Dvořák -15.9/-5.5/+3.1.

c19 does the reverse: +1.9/-0.9/-2.8. Loud frames now carry more 30-60 Hz than soft frames.

**The change since c14 is large.** Master 56-112 Hz share by passage:

| Passage | c14 | c19 |
|---|---|---|
| Bars 82-83 | -15.4 | -10.6 |
| Bars 117-121 | -15.3 | -11.1 |
| Bars 122-123 | -17.7 | -11.8 |
| Bars 158-161 | -17.7 | -11.5 |

The 28-56 Hz band rose 2-4 dB in the same passages. In loud frames the basses supply 93% of the master's 28-56 Hz and 71% of its 60-100 Hz. Their stem's 56-112 Hz in these passages rose 6-9 dB from c14 to c19.

**Cause (measured in mix.json).** Two changes made in other cycles add up:
- c16 B #4 raised the basses' `dyn_trim_db` f/ff from 1/2 to 2.5/4.
- c18 B #4 replaced the static `bell2` 100 Hz -2 dB bw 0.8 with 87 Hz -6 dB bw 0.25. The narrow notch fixes F2 but takes nothing from 50-80 Hz or 95-115 Hz.

Inferred: the tutti sounds thick and boomy at the bottom while the cello, bassoon and trombone body under it stays thin. This is the main tonal difference between this mockup and a recording. It also feeds the low-end crest that sets the delivery limiter (c17: top peak 1.538 at 484.53, low brass plus celli).

**Fix.** `build/mix.json`, Double basses `loud_eq`: add a third spec, a separate ReaEQ, with:
- the first spec's points, without the coda span 660-680, so the coda's 66 Hz +4 spec keeps its work;
- `"bands": [{"band": "lowshelf", "hz": 80, "db": -5}]`.

Keep the 87 Hz bell2 and the 160 Hz bells.

Simulated on the c19 stems (power sum, basses only):

| | Loud 30-60 Hz | Loud 60-100 Hz | Loud 100-250 Hz | Loud-frame level |
|---|---|---|---|---|
| Now | -26.2 | -13.4 | -7.5 | |
| Low shelf 80 Hz -5 dB | -30.0 | -14.7 | -7.7 | -0.07 dB |
| Bell 70 Hz -6 dB, bw 1.2 (stronger option; needs the band-1 slot or another spec) | -30.8 | -16.5 | -8.4 | |

Targets:
- loud 30-60 Hz at least 2 dB under soft (-27.7);
- loud 60-100 Hz at least 3 dB under soft (-11.3);
- loud 100-250 Hz within 0.5 dB of now;
- climax order 160 > 122 > 167-170 unchanged;
- note the delivery limiter.

Do not lower the basses' level instead: B (c16) measured them fading behind the celli at f/ff.

## 2. Coda, bars 167-169 (qn 664-676): the basses' 24 repeated C2 eighths alternate strong-weak like a drum machine, and it shows on the master (measured)

**Where.** Double basses, f, 24 unmarked C2 eighths on Sus MAX, all at velocity 83. Every other low instrument holds whole notes here (Tuba, Btbn, Cbn, Bn2, Timp).

**Evidence.** First 100 ms of each eighth:

| | Stem, 40-300 Hz | Master, 40-300 Hz |
|---|---|---|
| On-beat minus off-beat | +4.8 dB | +3.8 dB |
| Note to note (median) | 5.5 dB | 4.9 dB |
| Note n against n-2 (median) | 0.09 dB | |

On the stem, 86% of n/n-2 pairs are within 0.3 dB. That is the same two samples in turn, 12 times. The fronts' lag-4 autocorrelation is 0.96: the most periodic run in the movement, and up from 0.93 in c14.

The c17 rejection of c16 C #5 used whole-note RMS (-0.7 dB). The difference is in the attacks, and with no other moving bass part it reaches the master's low band as an even oom-pah. Real basses playing f eighths give the beat 1-2 dB at most and never repeat exactly.

**Fix.** `build/score_config.py`, add one Double basses `LEVEL_SHAPES` entry with steps on the attacks. Use the plucked-note step shape (LEARNINGS 13: full value 0.01-0.03 qn before the onset), so the weak notes' fronts are lifted:

```python
_cb = [(663.97, 0.0)]
for i_ in range(24):
    q_ = 664.0 + 0.5 * i_
    v_ = -1.0 if i_ % 2 == 0 else 2.5
    v_ += (0.6, -0.4, 0.0, 0.5, -0.6, 0.2)[i_ % 6]   # small irregularity
    _cb += [(q_ - 0.02, v_), (q_ + 0.47, v_)]
_cb += [(676.0, 0.0)]
LEVEL_SHAPES["Double basses"] = LEVEL_SHAPES.get("Double basses", []) + [_cb]
```

The irregularity row has period 6, so n/n-2 no longer match.

Targets:
- stem on-minus-off front 1-2 dB, and n/n-2 median at least 0.5 dB;
- master 40-300 Hz front on-minus-off under 1.5 dB;
- bar 167-169 RMS within 0.5 dB.

If a row test is wanted later, the MEAS_TREM `alt_row` mechanism (generalised to a span list) with `Stac On Bow RRx9` on every second note would also break the timbre repeat. That needs a basses rebuild.

## 3. Violas' p espr. solo, bars 107-110 (qn 424-440): the stacked fixes put the peak on the middle tenuto, and the line falls 9-13 dB before its top note (measured)

**Where.** Violas, p espr., one slurred line from 424 to its A-flat5 tenuto (436) and the fall to 439. The bass clarinet's p espr. runs alongside, and Flute 1 enters mp espr. at 432.

**Evidence.** Stem bodies, 0.12-0.7 s:

| | 428 | 429 C5 tenuto | 431 | 432 | 434 | 436 A-flat5 top |
|---|---|---|---|---|---|---|
| c19 | -36.2 | -34.3 (envelope peak -30.5) | -43.5 | -47.5 | -45.8 | -42.0 |
| c00 | | | | -46 to -49 (flat) | | |

So the C5 tenuto is now the loudest note by 8-13 dB, and the phrase's top note sits 8 dB under it.

In 2-qn windows the violas go from -34.6 dB (428-430), 5 dB over everyone else, to -46.5 (432-434), 5.5 dB under the flute.

The data stack +13.7 dB of volume on 429:
- role `[424, 432, 2.5, 0.5]`;
- `note_trims` 429 +5;
- `early_fills` 429 +5 dB;
- the CC11 swell.

The role ends at 432, exactly where the line climbs. Each fix was right when made (429 sagged 4-9 dB), and together they overshoot. Inferred: heard as a single swollen note in the middle of a phrase.

**Fix.**
- `build/note_trims.json` Violas 429.0: 5.0 -> 1.5.
- `build/early_fills.json` Violas 429: db 5.0 -> 2.5.
- `build/roles.json` Violas: `[424, 432, 2.5, 0.5]` -> `[424, 437.5, 1.5, 0.5]`.

Targets:
- 429 body within +2 dB of 428;
- the notes 431-436 within 4 dB of 429, rising to 436;
- Flute 1 still at or over the violas from 432 (now +5.5 / +1.0 / +1.9 dB in the 432/434/436 windows).

## 4. Second theme, bars 51-52 (qn 202.9-205.5, exposition only): the dolce phrase bumps on B-flat4 and then falls 12-16 dB through A-flat4-G4; the recapitulation does not (measured)

**Where.** Horn 1 with the celli in unison, `c'' -- bes' | aes'4. g'8 f'2`. Printed: < into 203, then < > on the A-flat. HP_TARGET 201 "mf-", 204 "mp".

**Evidence.** 0.1 s envelope:

| | Peak on 203 (B-flat4) | A-flat4 to G4 (204.5-205.5) | Master: peak to dip |
|---|---|---|---|
| Exposition, Horn 1 stem | -30.3 | -42 to -46.5 | -27.0 to -39.8 / -41.1 (12-14 dB) |
| Exposition, celli | | -41 to -48 | |
| Recap, Horn 1 stem (600 + same beats) | -32.8 | -41 to -43 | under 7 dB |

The exposition is the first statement of the movement's main lyric phrase.

Cause (inferred):
- the 203 quarter is a velocity-124 legato target with +4 dB volume (202.88-204.0);
- the A-flat4 is a weak horn sample (LEARNINGS 13: A-flat4 -5 dB at flat CC11) with no pitch trim (`pitch_trims.json` Horn 1 has 72 and 65 only);
- the CC11 falls from 69 to 63 across 204-205.5.

**Fix.**
- `build/score_config.py`: add a Horn 1 `LEVEL_SHAPES` entry `[(204.15, 0.0), (204.3, 3.5), (205.6, 3.5), (205.9, 0.0)]`, and the same for the celli at +2.5.
- Leave the 202.88-204.0 shape as it is; the bump falls if the following notes rise.

Target: the Horn 1 stem 204.3-205.5 within 6 dB of the 203 peak, and the master fall at most 7 dB, as in the recapitulation.

Recap 604 is fine; do not apply there.

## 5. Tutti cut-offs decay slower than in a hall recording (measured; cause and fix inferred, test only)

**Evidence.** Master, time to -10/-20/-30 dB after the release:

| Cut-off | -10 dB | -20 dB | -30 dB |
|---|---|---|---|
| Bar 26 rest | 0.42 | 0.60 | |
| Bar 32 rest | 0.51 | 0.80 | |
| Bar 170 fermata | 0.35 | 0.56 | 1.06 |
| Dvořák tutti stops | 0.08-0.14 | 0.35-0.43 | 0.52-0.66 |

- Brahms 1/i: median to -20 dB 0.485 s, RT60 estimate 1.3 s.
- At the bar-170 fermata the strings start to fall 0.17-0.20 s before the brass, and Trombone 1 takes 0.46 s to fall 10 dB, so the stop reads as ragged.

The note data end every track at 679.000. The spread comes from the samples' releases and the hall, not the MIDI.

**Fix (test, for a cycle that rebuilds every track anyway).** `mix.json` reverb `fx_volume` 0.19 -> 0.16 (LEARNINGS 12: toward 0.15 was proposed and never tried).
- Target: tutti stops at -20 dB within 0.5 s.
- Do not combine it with other level work, because every fill and re-bow shape was fitted on the current hall.

Not worth doing this cycle: brass widths. The trombones and trumpets are 0.86-0.89 correlated at 4-12 kHz and supply about 27% of the master's 4-12 kHz. A side-scale simulation of wider brass moved the master 4-12 kHz correlation only from 0.57 to 0.54; the references are 0.38-0.39.

## Smaller items (measured; no change proposed)

- **Clarinet 2, letter G (qn 464-479).** The 45 triplet notes repeat the same samples (same pitch n/n-3 within 0.17 dB). This is under the ff tutti and masked.
- **Melody contour.** The level-versus-pitch slope of the main melodies fell from +0.4..+0.6 dB/semitone (c00) to +0.2..+0.4 (c19). The pitch trims have flattened the line. This is not a defect by itself; watch for it if lines are said to sound flat.

## Do not touch

- The re-bow and loop work, since brief item 7 passes;
- GENTLE_ACCENT, ACC_ART_LEAD and the accent fits, since item 8 passes;
- the c16 violin 2.5 kHz loud shelves (the loud 2-5 kHz share now matches the reference);
- the celli 150 Hz `loud_eq` and the basses' 87 Hz bell and 160 Hz bells (change only the sub-bass, finding 1);
- the coda 66 Hz spec;
- the delivery parameters;
- climax order 160 > 122 > 167-170;
- the bar 145-146 and other tempo arcs;
- the hall IR and true-stereo setting.
