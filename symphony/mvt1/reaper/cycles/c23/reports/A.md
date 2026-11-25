# Cycle 23, critic A: articulation and phrasing (render c22)

Scope: every wind, brass and string note in `cycles/c22/rendered_build/parts.json`, measured on the c22 stems and master (`cycles/c22/render/`), with c21 as the control. I reran the c22-A battery on c22 (breath, joins, chordleg2, kscheck, ties, rebow, longloop, tremj, pz3, harp, timp, stacsep, rests2, reltime, acchf, accpk2, accshape, sstart, pkr3, ten200). Then I wrote new scripts in `/private/tmp/claude-501/mockup-loop/mvt1-c23-A/`:
- `accfb2.py`: front minus body of accented and plain notes;
- `accexc.py`: accent excess over the track's plain-note curve;
- `accprof.py`: median accent profiles;
- `hammer.py`: downbow-accent strokes;
- `stpk.py` and `stprof.py`: stroke timing;
- `offprof.py`: release after the note-off;
- `heads.py`: Violins I slur heads.

I read the Opus patch data with `opus_state.load_oib`.

## Checks that passed (measured, no action)

- **Legato.**
  - No chord goes to a legato row.
  - Wind and brass joins at 6 dB or more: 0.
  - String joins at 6 dB or more: 5, the same notes as c21 (Vc 112 7.8, 689.5 6.7, 215 6.3; Vla 612 6.6; Vln II 637 6.6). None of them shows on the master.
- **Keyswitches.** Shortest lead 14 ms. None under 4 ms. Every keyswitch inside a sounding note is a planned row switch.
- **Item 7 (loop pulsing).** No held note within 6 dB of the master pulses at the loop period. The bass clarinet C3 at qn 11 (acf 0.58 at 3.95 s) moves as one slow change (centroid 680 -> 250 Hz), not a cycle.
- **Re-bows.** c22's three refit celli rows: 39.879 -10.4 -> -4.4, 49.683 -8.2 -> -4.4. Celli worst is still 723.9 -7.9 / 163.877 (master -1.0/-1.8).
- **Item 8 (2-5 kHz first 80 ms minus body).**
  - Medians: brass -8.4, winds -5.8, strings -3.4.
  - The outliers are the known ones: Bn1 536/382, Tpt1 284 (15 dB under the master), Hn3 317/321, and Vla/Vc 536 (release of the ff eighth).
- **Other techniques.**
  - Pizzicato onsets: median -10 dB point +0.005 s.
  - Tremolo joins: median about -1.5 dB.
  - Tenutos: unchanged.
  - Breath marks: unchanged.
  - Ties: held.
  - Harp étouffez: unchanged.
  - Timpani strokes and rolls: within 1 dB of c21.
- **Violins I slur heads** (`heads.py`, 21 heads). Over the written eighth the head sits -0.4 dB (median) against the target's body. Own-pitch share 0.88. This is not a problem.

## 1. String and wind accents carry no weight at the start of the note: the emphasis is a swell centred 0.3 s after the beat (measured)

**Where.** Every string and wind accent of 1 qn or longer. At 126 bpm these are mostly quarter and dotted-quarter notes. Examples:
- Cor anglais 361 (bar 91, f);
- Oboe 1 313/533;
- Clarinet 1 414/422/505/553;
- Bassoon 1 529;
- Violins I 110/137/330/564;
- Violins II 94/100/118/548;
- Violas 100/349/548;
- Violoncellos 285/342/526.

**Evidence (measured).**
- `accfb2.py`: front (score onset .. +0.15 s) minus body (+0.30 .. min(+0.75 s, end - 0.05)), on notes of 1 qn or more within 14 dB of the master.

  | Family | Accented, under 0.75 s | Accented, 0.75 s or longer | Plain, under 0.75 s | Plain, 0.75 s or longer |
  |---|---|---|---|---|
  | Strings | -1.5 dB (n 93) | -1.0 (n 49) | -1.5 | -1.2 |
  | Winds | -1.5 (n 46) | -1.1 (n 31) | -0.8 | -2.3 |
  | Brass | +0.8 | +0.1 | -0.7 | -1.6 |

  - On strings and winds an accented note starts exactly like a plain one: 72-83% of the accents have the front under the body.
  - Brass accents (GENTLE_ACCENT swell from +0.04 s) are the only family with a front above plain notes.
- `accexc.py`: accent level minus the same track's median plain-note curve, in 40 ms bins from the score onset.
  - Strings: +2.1 dB over 0-0.12 s and +3.1 over 0.20-0.44 s. The excess is centred at 0.30 s.
  - Winds: +0.0 and +1.8. The excess is centred at 0.32 s.
  - In 62% of the wind accents and 51% of the string accents the later window carries more than the front.
- `accprof.py`, string accents of 0.85 s or more, re the late body. By time after the score onset:

  | Time | 0.00 s | 0.08 s | 0.16 s | 0.28-0.36 s | 0.60 s |
  |---|---|---|---|---|---|
  | Level | -0.5 | +1.2 | +3.0 | +3.4 (peak) | +0.8 |

  At 126 bpm the emphasis lands on the second sixteenth of the beat. Inferred: it is heard as a small hairpin on each accented note rather than an accent.
- Cause, part 1 (measured from the data).
  - The string and wind swell is `swell_s` (0.07, 0.25, 0.6) and `swell_s_leg` (0.04, 0.35, 0.7). By construction its centre is about 0.28 s.
  - It rides a Sus MAX attack that still rises for about 0.25 s.
- Cause, part 2 (measured from the data). `fit_accents.py` measures long notes by their loudest 200 ms in onset .. +0.5 s, which is the late bloom. It then zeroes or cuts the swell:
  - Cor anglais 361 [0, -2.95];
  - Violins I 328 [0, -3.41], 564 0;
  - Oboe 1 533 0;
  - Violas 548 0 and 349 0.

  Example, Cor anglais 361: the volume envelope steps from +1.6 at the onset to -2.95 dB at +0.1 s. The stem sits at -42 dB at +0.1 s and blooms to -31.8 dB at +0.42 s, 10 dB of growth through the accented note.
- Cause, part 3 (measured from the data). `fit_accent_bodies.py`, which cuts the body after the front, has run only on strings, with `--min-s 0.75`. A 1 qn note at 126 bpm is 0.476 s and 1.5 qn is 0.714 s, so it covers 18 accents. It has never run on winds.

**Fix.**
1. `tools/score_to_parts.py` GENTLE_ACCENT, string and wind (set in `build/score_config.py`):
   - `swell_s` (0.07, 0.25, 0.6) -> (0.03, 0.15, 0.40);
   - `swell_s_leg` (0.04, 0.35, 0.7) -> (0.03, 0.22, 0.50).

   Brass unchanged.
2. `tools/fit_accent_bodies.py`:
   - `--min-s 0.45`;
   - for notes shorter than 0.8 s, body window = +0.28 s .. end - 0.03 s;
   - in `score_to_parts.py`, a short-note body ramp `ACCENT_BODY_S_SHORT = (0.18, 0.28)` for notes under 0.8 s (the current (0.25, 0.45) cannot fit in a 0.476 s note).

   Run with `--family string` and `--family wind`, `--front-min 2.0 --max-cut 3.0`.
3. `tools/fit_accents.py`: new option `--front-s` (default 0 = off). When set, accent and neighbour levels are the power mean over [min(moved onset, score onset - 0.03), score onset + front_s]. Refit string and wind with `--front-s 0.18 --lo 2 --hi 4`.

Apply step 1 in the build. Do steps 2-3 after the render; they are level only, so `stem_fix.py` can apply them.

**Pass.**
- Per family, accented minus plain front-body is +2 dB or more.
- The `accexc` centre is 0.18 s or less.
- Accents stay 2-4 dB over their neighbours on the front window.
- 2-5 kHz first 80 ms minus body rises no more than 1 dB (strings -3.4, winds -5.8).
- Brass is unchanged.

## 2. The downbow hammer strokes swell through the note instead of striking: test the `Sus Marc LITE` row (measured; patch effect inferred)

**Where.** The 43 notes marked accent + downbow in Violins I/II, violas, celli and basses:
- bar 32: 124/125/128;
- bar 72: 284-286;
- bar 83: 328/330;
- bar 131: 521;
- bar 142: 564/566.

**Evidence (measured, `hammer.py`).**
- Peak at +0.30 s (median). Front (-0.03..+0.15 s) minus body: -1.7 dB. 63% of the strokes have the front under the body.
- Violins I 330 (ff double stop G4+A♭5, followed by a rest): -30.7 dB at +0.02 s, -24.9 at +0.18, -23.2 at +0.5 s. It grows 7.5 dB to the end of the quarter.
- Other fronts:
  - Violins I 564 -6.3, 330 -5.9;
  - Violoncellos 285 -9.2, 330 -4.8 (330 is on Leg Slur MAX after a rest);
  - Violins I/II 521, the recapitulation's ff downbeat: -5.2/-6.5, on the Leg Slur MAX first-note layer;
  - Double basses 284 -6.3.
- Sus MAX velocity cannot help: the patch has `velocitySensitivity 0.0` (measured from the .oib).
- The row approaches tried so far:
  - DOWNBOW_STROKE_AT on Leg BC notes failed in c19;
  - Marc Shrt failed on the basses' eighths in c03.
- `Sus Marc LITE`:
  - it is key 25 in every Hollywood Strings KS Master and loaded by default, but `UNLOAD_UNUSED_ROWS` unloads it;
  - it is a sustain with a recorded marcato bow start;
  - it was proposed in c02, c17 and c18 and never rendered.

**Fix (test).** In `build/score_config.py`, `ART_SPANS` (generic rule, existing), row "Sus Marc LITE", at the current stroke velocity (111):
- Violins I and Violins II over 327.9-331.0 and 563.9-567.9;
- Violoncellos over 283.9-286.0.

Controls: bars 32 and 72 in the upper strings, and bar 83 in the violas, stay on Sus MAX. The violas' fronts there are already +2.0/+3.8. This is a full rebuild of three tracks with one extra row each, so record REAPER memory.

**Pass.**
- On the test strokes, front minus body is +1 dB or more and the peak is at +0.15 s or earlier.
- 2-5 kHz first 80 ms minus body is +2 dB or less (weight, not bite).
- After an accent refit, the strokes are 2-4 dB over their neighbours.
- The release into the following rest is no longer than Sus MAX's (-10 dB point).

If it passes, extend it to bars 32, 72 and 131 (including the Violins I/II 521 downbeat).

## 3. Violins I staccato strokes land 0.05 s behind the rest of the tutti (measured)

**Where.** Violins I Stac RRx14, 11 notes:
- bar 30: 116-117.5;
- bars 94-96: 374.5-375.5, 379.5, 382.5-383.

The winds, Violins II and violas play the same staccato eighths.

**Evidence (measured, `stpk.py` / `stprof.py`).**
- -3 dB point from the score onset (median):

  | Part | -3 dB point | Peak |
  |---|---|---|
  | Violins I Stac RRx14 | +0.10 s (p90 +0.12) | +0.13 s |
  | Violins II Stac RRx9 | +0.04 s | |
  | Violas Stac RRx9 | +0.07 s | |
  | Flute 1 | +0.04 s | |
  | Clarinet 1 | +0.07 s | |

- Bar 30, averaged over the four strokes, peak position:

  | Part | Peak |
  |---|---|
  | Violins I | +0.12..+0.14 s (11 dB under its peak at +0.00) |
  | Clarinet 1 | +0.06..+0.08 s |
  | Violins II | +0.08..+0.10 s |
  | Double basses | +0.06 s |

- Violins I is the loudest string stem there: -23.5 dB, -8 dB re the master. The master's loudest 20 ms in each eighth is at +0.12 s, which is Violins I's late peak.
- In parts.json the string Stac notes have qn = sq, so no lead. The winds lead 0.035 s. `retongue_ok()` admits only "Sus MAX" for strings.

**Fix.** New generic `STAC_LEAD_S = {}` in `tools/score_to_parts.py`:
- A string note on a row whose name starts "Stac" starts that many seconds early (`lead_qn`).
- A previous note that would then overlap ends at least 0.02 qn before the moved onset.
- CC11 holds; the span goes into `pulls`.

`build/score_config.py`: `STAC_LEAD_S = {"Violins I": 0.05, "Violas": 0.03}`.

**Pass.**
- Violins I Stac -3 dB point is +0.05 s or less from the score onset.
- Peak is at +0.09 s or earlier.
- `stacsep` separation median stays 10 dB or more (now 14.3).
- Stem level within 0.5 dB.

## 4. The violas' off-beat ff dyads in bars 131-134 fill their rests (measured; cause partly inferred)

**Where.** Violas, 16 unslurred eighth dyads on the off-beats, 520.5-535.5, each followed by an eighth rest, ff.

**Evidence.**
- Measured:
  - Each dyad plays 0.626 qn from a 0.06 s lead, so it ends on the next beat at the full written value.
  - Drop by the end of the rest (`rests2`): 8.4, 7.1, 8.0, 5.6, 7.8, 2.8, 5.8, 2.1, 5.9, 1.9, 5.6, 2.2, 5.8, 4.4 dB (median 5.8). The dyads at 526.5, 528.5, 530.5 and 532.5 drop only 1.9-2.8 dB.
  - Trace at 526.5-527.5: -28.5 dB on the note, -31..-34 through the whole rest.
  - After a Sus MAX note-off the violas hold their level for about 0.06 s and only then fall (-10 dB at +0.20 s, `offprof.py`).
- Inferred. The Violas KS Master's release-trail (RT) groups have AHDSR attack 70.7 ms, hold 0.1, decay 750 ms, sustain 1.0 (read from the .oib).
  - The trail fades in as the capped sustain release fades out, so the level stays flat for the first 0.06 s.
  - Its sustain is 1.0, so only decay/sustain or the source volume can shorten it. That explains why the c22 `rt_ms` (AHDSR release) test changed nothing.

**Fix (test, violas only).**
1. Note length (the main fix). New generic `STR_REST_SHORT = {"at": {track: [(a, b)]}, "frac": 0.6, "max_qn": 0.5, "min_bpm": 120}`. An unslurred string note of `max_qn` or less followed by a written rest ends at `frac` of its written length after the score onset. The moved onset keeps its lead.

   `build/score_config.py`: `{"Violas": [(520.0, 536.0)]}`.
2. Only if step 1 leaves rests under 6 dB: in `build_reaper.py cap_release()`, new spec keys `rt_sustain` and `rt_decay_ms` for the listed rows' RT groups. On Violas Sus MAX mf/f/ff, use 0.3 and 120. This replaces the reverted `rt_ms`.

**Pass.**
- Every one of the 16 rests drops 6 dB or more (now 1.9-8.4).
- The dyads' level (first 0.15 s) is unchanged within 0.5 dB.
- The violas' re-bow dips are no deeper than c22.

## Patches

- #2 is the one new patch test this cycle: `Sus Marc LITE`.
- The woodwind KS Masters have `Sus Accent MAX` (key 25) and `Leg Slur Accent MAX` (key 34). The clarinets use `Sus Accent` and `Leg Slur Accent`.
  - On c00 they were measured only with the +8 CC11 bump and +10 velocity, never at plain velocity.
  - Test one track (Clarinet 1, accents 409-422) only if #1 does not reach +2 dB front weight for the winds.
- The 2nd Violins "metà" passage (bars 47-54, pp held notes) is played by the full section at -3 dB (`META_DB`). A `2nd Violins Divisi` DIV patch would give the half-section colour. It is not recommended at the current 46 GB footprint.
- Hollywood Brass has no solo bass trombone. The bass trombone part (C2-F#3) lies inside the 1TB KS Master's range. `LB KS Master` is a low-brass ensemble.
- 2TP, 3TP and 3TB are not recommended: the parts move in harmony, not unison.

**Do not touch:**
- GENTLE_ACCENT brass (swell from +0.04 s, the only family whose accents have front weight), ACC_ART_LEAD, and the brass/wind 2-5 kHz results;
- STR_REP_DETACH on the basses;
- the c22 celli re-bow rows;
- DOWNBOW celli 484 with the `_sost` shape;
- sus_release_cap_ms 250 on the basses and celli;
- the Slur Runs spans and `_lg()`;
- SLUR_HEAD_LEAD 0.10 (the heads measure level with their targets);
- RETONGUE_LEAD_S;
- MEAS_TREM alt_row;
- TREM_JOIN/TREM_SPLIT;
- WIND_DETACH;
- breath splits and CAESURA_BREATH_QN;
- harp env_release_ms 200 with HARP_RING_S;
- TIMP_CC1_MAP and the re-strike plans;
- _REBOW_FROZEN;
- the violas' Stac On Bow revert.

Revert Violas `rt_ms` as planned.
