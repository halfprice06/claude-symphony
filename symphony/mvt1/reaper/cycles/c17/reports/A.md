# Cycle 17, critic A: articulation and phrasing (render c16)

Scope: every wind, brass, string, harp, timpani and percussion note in `build/parts.json` (the c16 build after both stem fixes), measured on the c16 stems and master (`cycles/c16/render/`). For before/after checks I used c15 (features in `mvt1-c15-actor/A/feat_c15`, parts in `cycles/c16/before/parts.json`).

Scripts and outputs are in `/private/tmp/claude-501/mockup-loop/mvt1-c17-A/`. The c16-A battery was rerun on c16 (`out_*.txt`, 5 ms feature frames in `feat_c16/`). New scripts:
- `plat.py`, `plat2.py`: the pickup's own sound with the volume envelope removed, against its target.
- `slope.py`: how much a pickup rises during its own sounding time.
- `sync.py`: off-beat string notes after a rest.
- `accpk2.py` / `accpk3.py`: long accents peak-to-peak against the notes before them, with unaccented long notes as the control (`CTRL=1`).
- `capacc.py`: accent fits against the following notes.
- `pk17.py`, `jt.py`, `tr.py`: traces.

## Checks that passed (measured)

- **Legato.** No chord on a Leg row. String join dips: median 1.5-2.4 dB per section. Joins of 6 dB or more:
  - celli 365/369 (9.9/7.6 dB) and 112, Violins II 236/296/405/637, violas 612/180/517;
  - all of these stems sit 6-12.5 dB under the master at the join. Leave them.
  - Wind and brass joins: no join at 6 dB or more.
- **Keyswitches.** No keyswitch lands just after the note-on it belongs to. Every keyswitch sent while a note sounds is either a Sus-to-short row change (strokes, pizz.) or a timpani roll restrike.
- **Re-bows (item 7).**
  - Master dip at the 62 re-bows before qn 700 is -1.83 dB, against -1.61 at 35 control times.
  - Final chords 708-728: -2.31 dB.
  - The largest stem steps are printed dynamics: celli 163.877 is the sf > to mf of bar 41-42, and the 727 notes are the morendo.
- **Loop pulsing on held notes.** No held note within 6 dB of the master shows a pulse with a level swing over 3 dB. The one exposed note with a centroid autocorrelation of 0.68 (Bass clarinet qn 11, 6.1 s, period 3.95 s) swings 1.4 dB, and its fold covers only 1.5 loop cycles.
- **Accent attacks (item 8).** 2-5 kHz in the first 80 ms minus the body:
  - brass median -8.2 dB (max Horn 3 321/317 +3.5/+3.4, Trumpet 1 676 +3.0);
  - winds -6.0 (Clarinet 1 558/414/105 +6.3/+6.2/+4.9: the timbre change of the slurred run, as in c16);
  - strings -3.7 (Violas 536 +15 is the printed sub. mf; celli 536/125 +5.1/+4.7 sit under ff tuttis).
- **Other techniques.**
  - Staccato separation: 7.1-14.6 dB per track.
  - Tremolo joins: median -0.8 dB, 1 of 33 at 4 dB or more.
  - Celli measured tremolo autocorrelation at lag 9: -0.10/+0.03/+0.10.
  - Pizzicato reaches -3 dB of its peak at a median +0.015-0.065 s.
  - Breath marks: 3.1-15 dB.
  - The harp étouffez at 244/650/654 damps the old pitches.
  - Tied timpani and basses notes are held through.

## 1. The theme's pickups after a rest are 7-18 dB under their targets because the sample plateaus. A lead cannot fix this; a measured level lift on each pickup can.

**Measured** (`plat.py`, `plat2.py`, `slope.py`, `pk17.py`).

For every pickup in `pickup_sus` I compared two levels, each with the volume envelope at that time subtracted, so only the sample's own level is left:
- the pickup's level over its own sounding time (moved onset + 0.04 s to the target's moved onset);
- the target's body (score onset + 0.15 s to + 0.7 s).

| Family | n | Sample deficit, pickup minus target (median) | p10 |
|---|---|---|---|
| Winds | 39 | -4.4 dB | -9.6 |
| Brass | 10 | -8.2 dB | -12.0 |
| Strings | 22 | -2.8 dB | -9.2 |

- The deficit is a property of each note. On c15, where the same pickups played the Leg rows, the same measure differs from c16 by a median 1.7 dB (59 pickups). So the row was never the cause, which agrees with the c16 test result.
- The pickup does not rise slowly. It sits on a plateau. The second half of its sounding time is only +2.9 dB (median) over the first half. Oboe 1 312.5 is flat to +0.4 dB: -57..-54 dB from its onset to the target.
- Violins I 136.5 already had a 0.12 s lead in c16 (moved onset 136.248). It still sat at -56..-52 dB until the target joined, against a target body of -30.
- An entry lead (the c17 plan from the c16 CHANGES) therefore buys at most 1-2 dB.

The envelope on the targets makes the gap larger. The target's accent swell plus its fitted step sit 3-8 dB over the pickup in the volume envelope (column "env" below). Several accent fits sit at the fitter's cap of 5 + 3 dB, because the fitter keeps chasing a quiet pickup (see #2).

Pickups within 10 dB of the master with a deficit of 4 dB or more (c16 / c15 deficit; stem against master at the target):

| Track | Pickup sq (bar) | Deficit c16 / c15 | Env over pickup | Stem re master | Lift |
|---|---|---|---|---|---|
| Oboe 1 | 312.5 (79) | -17.9 / -16.0 | -5.6 | -3.5 | +10 |
| Violins I | 136.5 (35) | -14.0 / -17.5 | -7.7 | -2.7 | +10 |
| Oboe 2 | 408.5 (103) | -12.2 / -10.5 | -2.8 | -3.9 | +9.3 |
| Trumpet 1 | 672.5 / 664.5 (169/167) | -12.1 / -11.0, -12.0 / -9.8 | +2.1 / 0 | -6.8 / -6.0 | +9.6 / +8.9 |
| Horns a2 | 664.5 / 310.5 | -11.3 / -7.4, -6.2 / -7.1 | +1.5 / -3.0 | -6.6 / -0.4 | +7.4 / +4.7 |
| Trombone 1 | 520.5 (131) | -10.3 / -6.2 | -4.2 | -3.1 | +6.2 |
| Violas | 132.5 / 146.5 | -9.5 / -8.2, -8.1 / -9.5 | | -6.3 / -8.4 | +6.8 / +6.8 |
| Bass clarinet | 304.5 (77, Solo) / 432.5 (109) | -9.0 / -7.8, -7.4 / -6.9 | -3.2 / -5.9 | -1.1 / -1.8 | +6.4 / +5.2 |
| Clarinet 1 | 504.5 / 416.5 | -8.7 / -7.7, -4.5 / -9.7 | -4.2 / -1.9 | -0.4 / -7.0 | +6.2 / +5.1 |
| Violins I | 312.5 / 72.5 / 148.5 / 144.5 | -8.6 / -9.2, -5.8 / -9.0, -5.2 / -5.5, -4.0 / -5.8 | | -8.7 / -3.2 / -6.3 / -4.6 | +6.9 / +5.4 / +3.3 / +2.9 |
| Flute 1 | 552.5 / 104.5 | -8.4 / -6.8, -8.1 / -7.0 | | -7.5 / -9.6 | +5.6 / +5.5 |
| Clarinet 1 | 272.5 | -4.4 / -7.2 | | -9.9 | +3.8 |

The lift is clip(-(mean deficit) - 2, 0, 10) dB, which leaves each pickup about 2 dB under its target's unaccented body.

**Inferred.** This is the movement's main cell: an eighth upbeat slurred into an accented dotted quarter.
- With the upbeat 10-20 dB down, the cell starts on the accent.
- The accent then sounds like a swell, not a stress.
- It is most exposed in the Violins I at bar 35, the bass clarinet solo at bar 77, Oboe 1 at bar 79, Clarinet 1 at bar 127 and the coda trumpets.

**Fix:**
1. Revert `PICKUP_SUS` as planned (`PICKUP_SUS = None` in `build/score_config.py`, with its string -3.5 dB). The deficits do not depend on the row, and the c15 rows measured better on the pickup's own time.
2. Do not add a pickup entry lead.
3. Add a new table `PICKUP_LIFT = {track: {pickup sq: dB}}` in `build/score_config.py` with the "Lift" values above.
4. Apply it in `tools/score_to_parts.py` as an exact level shape. It starts at the pickup's moved onset (0.01 qn ramp in), holds, and ends 0.02 qn after the target's moved onset (0.02 qn ramp out). This uses the c13 lesson: score-keyed trims miss early notes.
5. The lift replaces the +3 dB note trims on Trumpet 1 664.5/672.5 and Horns a2 272.5/664.5/672.5. Do not add it on top of them.
6. After the revert, rerun `plat2.py` on c17 and adjust the lifts by the new deficits. The two renders agree within 1.7 dB.
7. Refit the targets' accents (see #2), because the pickup is their neighbour.

**Pass** (`plat.py` on c17, envelope not subtracted, i.e. what is heard):
- The pickups listed above sit between -6 and -2 dB under their target's peak.
- None louder than the target's body.
- `acclate.py`: the targets reach peak - 3 dB by +0.15 s.

## 2. String accents are too heavy, about 5 dB over the line, because `fit_accents.py` measures the front of the note and misses the peak

**Measured** (`accpk2.py`, `accpk3.py`, `capacc.py`, traces; code read in `tools/fit_accents.py` `windows()`).

For long accents (written 1 qn or more), I took the 200 ms peak against the peaks of the unaccented notes in the 2 qn before them. As a control I measured unaccented long notes the same way: strings +1.0 dB, winds +2.2, brass +0.8. "Excess" is the accent's reading minus its family's control.

| Family (stems within 10 dB of the master, pickup targets excluded) | n | Excess median | p75 | In 2-4 dB | Over 6 dB |
|---|---|---|---|---|---|
| Strings | 97 | +4.9 dB | +6.2 | 26 | 26 |
| Winds | 19 | +1.9 | +4.0 | 4 | 3 |
| Brass | 14 | +2.4 | +4.3 | 4 | 2 |

- Winds and brass are inside Dan's 2-4 dB. Strings are not.
- String accents peak at a median +0.30 s after the score onset (p75 +0.43). The control notes peak at +0.35 s, so the late peak is the sample's own bloom.
- `fit_accents.py` measures each accent on the window from the moved onset + 0.05 s to + 0.35 s.
  - 58% of string accents are legato targets led 0.10 s or more (median lead 0.11 s), so the window ends about 0.2 s after the score onset, before the peak.
  - The 200 ms peak (score onset - 0.05 to + 0.5 s) is 2.2 dB over the fitter's window (median; 2.6 dB on led targets, 1.7 on unled).
  - The fitter therefore asks for about 2-2.5 dB more than the note needs. 29 of the 126 string fits total 6 dB or more, and many sit at the cap of 5 + 3.

Exposed cases:

| Track | Accent sq (bar) | Fit (swell + step) | Peak over the line before | Stem re master |
|---|---|---|---|---|
| Violoncellos | 342 (86) | 5 + 3 | +11.4 dB: line -38, peak -24 at +0.24 s, body still -28 | +0.6, the loudest stem |
| Violas | 354 (89) | 5 + 2 | +10.9 | -0.5 |
| Violins I | 62 (16), 65 (17), 82 (21) | 5 + 3 each | +6.5, +5.9, +4.3. Peaks come at +0.27/+0.34/+0.20 s. The accent's first 0.3 s sits +9.6 / +2.7 / +11.2 dB over the notes after it: the eighth after 62 (63.5) is 13 dB under the peak, the one after 82 is 10-12 under | -0.6..-1.2 |
| Violins I | 110 (28), 137 (35) | 5 + 2.5, 5 + 3 | +10.6, +15.4 (137 includes the pickup of #1) | -1.1, -1.3 |
| Violoncellos | 337 (85) | 4.4 | +11.3 | -0.1 |

**Inferred.**
- In the first theme (bars 15-22, recapitulation 131-138) the Violins I accents bulge 8-10 dB and then drop away, so the eighth after the accent is barely heard.
- That is the "accent swells in" effect, and twice the weight Dan asked for.

**Fix** (`tools/fit_accents.py`):
1. In `windows()`, measure a note whose written length is 1 qn or more as the 200 ms peak inside [score onset - 0.05 s, min(score onset + 0.5 s, end - 0.02 s)]. Do this for accents and neighbours alike, in place of the moved-onset + 0.05..0.35 s mean.
2. Keep the current window for shorter notes.
3. Add `--max-total` (swell + step) per family: strings 4.5, winds/brass 6.
4. Refit all three families with `--keep-long-qn 1.4 --pickup-over 2.5` after #1's lifts are in, because the pickups are the accents' neighbours.
5. Simulate on the c16 stems first. The first theme's accents are fitted together with the `DOWNBOW_STROKE_AT` strokes.

**Pass** (`accpk2.py` / `accpk3.py` on c17):
- Strings excess median between +2 and +3.5 dB, and fewer than 10 of 97 over 6.
- Violins I 62/65/82 peaks 3-5 dB over the line before, and the following eighth no more than 6 dB under the peak.
- Celli 342 no longer the loudest stem.
- 2-5 kHz front minus body unchanged (strings median -3.7).

## 3. The Allegro's syncopated accompaniment (Violins II, violas) swells through each note and peaks on the next downbeat

**Measured** (`sync.py`, `tr.py`).

In bars 15-22 (qn 56.5-84.5) the Violins II and violas play r8 + an eighth tied to a quarter, twice a bar, at mf (score page 2). They play the Leg Slur MAX row (the c02 "unslurred notes stay on Leg Slur MAX" branch), single notes from 56.5 to 62.5, and Sus MAX dyads in the violas at 64.5/66.5. Each note is moved 0.12 s early.

Median level profile of 13 Violins II and 10 viola notes, against the note's maximum, in seconds from the score onset:

| | -0.12..0 | 0..0.1 | 0.1..0.2 | 0.2..0.3 | 0.3..0.45 | 0.45..0.6 | 0.6..0.8 |
|---|---|---|---|---|---|---|---|
| Violins II | -7.0 | -8.4 | -5.7 | -4.1 | -3.4 | -0.6 | 0.0 |
| Violas | -6.9 | -8.3 | -5.4 | -3.5 | -3.0 | -2.0 | 0.0 |

- Every syncope grows by 8 dB from its start to its last 0.2 s. The peak falls at or after the next downbeat (+0.24 s) and just before the next syncope.
- The violas' Sus MAX dyads swell the same way (rise 10.8-11.7 dB, peak +0.57 s), so changing the row does not cure it.
- The rest before each note (0.24 s written, 0.12 s after the lead) is filled to 6-9 dB under the peak.
- The stems sit 11-15 dB under the master, under the Violins I tune.
- The same pattern recurs in the recapitulation violas (qn 525.5-534.5: rise 7-8.8 dB, peak +0.24 s) and Violins II / violas at 569.5/570.5 (rise 8-10 dB).
- Nothing in the envelope shapes these notes now (only the bar-15 entry ramp).

**Inferred.**
- The agitation of the Allegro comes from these off-beat starts. Played as swells that crest on the beat, the off-beat starts disappear and the inner parts sound like a breathing pad on the beat.
- Real players give a syncope its weight at the start, then taper slightly.

**Fix** (generic, `tools/score_to_parts.py`; values in `build/score_config.py`):
1. Add `SYNCO_SHAPE = {"families": ("string",), "min_bpm": 100, "rest_qn": 0.25, "len_qn": (0.75, 2.0), "pts": [(-0.12, 6.0), (0.10, 6.0), (0.25, 3.0), (0.45, 0.0), (0.60, -3.0)]}`.
2. The points are (seconds from the score onset, dB). Hold the last value to the note's end, and return to 0 over the following rest by the next moved onset.
3. It applies to a note that:
   - starts off the beat (sq mod 1 = 0.5);
   - follows a written rest of at least 0.25 qn in its own track;
   - has a written length of 0.75-2 qn;
   - is not accented and not slurred from the note before.
4. Write it as an exact level shape, not on the envelope grid.
5. About 59 notes (Violins II 16, violas 43).
6. Simulate on the c16 stems: the planned front +6 / back -3 should bring the profile to about -2.4 dB at 0-0.1 s against -3 at the end.
7. An optional test on the Violins II at bars 15-18 only (8 notes): the `Sus Marc LITE` row, which is loaded by default in the 2nd Violins KS Master and has never been tried in either loop. Accept it only if 2-5 kHz front minus body stays under +2 dB (item 8).

**Pass** (`sync.py` with the profile print):
- Median front (0..0.2 s) within ±2 dB of the note's last 0.2 s, and no later bin more than 2 dB over the front.
- Stem mean level over bars 15-22 within ±1 dB of c16.
- No master change of more than 0.5 dB in those bars.

## Patches

I found no Hollywood Orchestra patch to recommend in place of a current one this cycle.
- `Sus Marc LITE` is the only untried option for #3, and it is listed as a test.
- The woodwind KS Masters also have `Leg Slur Accent MAX` rows, which would put the motive's accent into the legato transition. I do not recommend it: winds already meet the 2-4 dB accent rule, and the accent samples are the harsh-front risk of item 8.
- The second-staff Horns 3-4 a2 routing at bars 80-81 remains the open patch item from c15/c16.

Do not touch:
- the legato rows and leads (string joins median 1.5-2.4 dB);
- `_REBOW_FROZEN` / `REBOW_AT` with `rebow_fills.json` (master re-bow dips equal to the controls);
- `GENTLE_ACCENT` rows and fronts (2-5 kHz front minus body: brass -8.2, winds -6.0, strings -3.7 dB);
- `MEAS_TREM` alt_row with seed 464;
- `TREM_JOIN` / `TREM_SPLIT`;
- `WIND_DETACH` (wind and brass gap holes -5.6/-5.1 dB);
- `SLUR_START_SUS` first-note rule and `RETONGUE_LEAD_S`;
- the staccato, pizzicato and tremolo rows;
- harp `env_release_ms` 200 with `HARP_RING_S` and the étouffez note-offs;
- `PORT_TARGETS`;
- `TIMP_CC1_MAP` with `TIMP_ROLL_TRIM_DB`;
- tam-tam / suspended-cymbal keys and timing;
- the Horns a2 windows and roles;
- the climax order (160 > 122 > 169).
