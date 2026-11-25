# Critic A, cycle 55 (render of cycle 54): the volume envelope, articulation part

Data used: `cycles/c54/build_fix` (the delivered stems after the stem fix) and the stems in `cycles/c54/render`.
Scratch (left in place, 9.5 MB, no audio): `/private/tmp/claude-501/mockup-loop/mvt2-c55-A/`.

## What was and was not done

- Done: the main task for Slot A. Every volume layer was separated by running a scratch copy of
  `tools/score_to_parts.py` that tags each `vol_parts.append` with its source line and writes one lane per line
  (`s2p_inst.py`; its `parts.json` is byte-identical to `build_fix/parts.json`). The lanes were sampled the way
  `build_reaper.py vol_points` writes them (0.125 qn grid plus `vol_bp`), and divided out of the stems offline.
- Not done: the manual reading (MANUAL-READING.md has no row for cycle 55) and most of the usual lens (keyswitch
  timing, tremolo, sul tasto, harp harmonics, timpani strokes were not measured this cycle). HISTORY.md, both
  LEARNINGS files and the research FINDINGS were not re-read in full; I read BRIEF.md, the c54 CHANGES, the lead's
  inbox and the code.
- One mistake to report. My first load of `build_reaper.py` for `vol_points` executed the whole file instead of
  the part before `ENV_LUA`. It stopped at line 983 (`returns_job()`, `NameError: __file__`), which is before any
  job is built or sent. I checked: no new file in `~/.rpr-bridge/inbox`, my jobs folder is empty, nothing was
  written to the bridge folder. Movement I's actor held the REAPER lock at that moment (since 08:09:06), so this
  would have reached their session had it not failed. Later loads cut the source at `ENV_LUA`, as `stem_fix.py` does.

## The layers, by class (source line in `tools/score_to_parts.py`, items, envelope travel over 32 tracks)

Total travel of the delivered envelopes: 12,125 dB. String tracks carry 1,650-2,461 points (Violins I 1,650,
Violins II 2,430, Violas 2,009, Violoncellos 2,461, Double basses 2,338; 4.8-7.1 per second).

| class | layer | line | data | items | travel dB |
|---|---|---|---|---|---|
| slow | roles | 4049, 4068 | `roles.json` | 562 | 1,951 |
| slow | hairpin gain | 4098-4233 | `HP_GAIN_DB` | 207 | 991 |
| slow | `LEVEL_SHAPES` rows over 3 or more notes | 4593 | `score_config.py` | 76 | 295 |
| slow | final fade, timpani hairpin half | 5084, 3889 | | 11 | 107 |
| slow | gain, dyn/soft trims, phrase arch, tail holds | `build_reaper.py vol_points`, `apply_phrase_shape` | `mix.json`, `PHRASE_SHAPE` | | about 100 per track |
| level | pitch trims | 4326 | `pitch_trims.json` | 179 | 1,177 |
| level | note trims | 4985 | `note_trims.json` | 81 | 605 |
| level | level rows on one note | 4597, 4593 | `level_fits.json`, `LEVEL_SHAPES(_S)` | 92 | 485 |
| level | timpani roll trim / soft flat | 3912, 3942 | | 13 | 256 |
| level | metric steps on plucked notes | 4359 | `METRIC_DB`, `METRIC_SPANS` | 113 | 177 |
| level | pizz. pitch trims, plucked note trims | 4320, 4970 | `pitch_trims.json`, `note_trims.json` | 18 | 109 |
| level | divisi chord cut, phrase tops, unison boost | 5071, 4876, 5034 | | 39 | 165 |
| shape | re-bow fills | 4570 | `rebow_fills.json` | 80 | 3,010 |
| shape | early fills | 4446, 4448 | `early_fills.json` | 308 | 2,306 |
| shape | shapes inside one note | 4597, 4593 | `level_fits.json`, `LEVEL_SHAPES(_S)` | 128 | 1,317 |
| shape | long-note swell | 4247 | `SWELL_DB` 1.5 | 193 | 681 |
| shape | join notches | 4574, 4585, 4588 | `JOIN_NOTCH`, `JOIN_NOTCH_S` | 44 | 411 |
| shape | sostenuto hold | 4424, 4429 | `SOST_SUSTAIN_DB` 2.5 | 54 | 260 |
| shape | slur-pair release | 4746 | `SLUR_PAIR_RELEASE` -2.5 | 15 | 75 |
| shape | accent swell | 4932 | `GENTLE_ACCENT`, `ACCENT_DB_AT` | 9 | 58 |
| shape | loop fill, early/body pitch trim, timpani attack and settle, bloom | 4481, 4324, 3956, 3928, 5029 | | 16 | 159 |

Layer travels add to more than the total because layers cancel each other. The shape class holds 8,276 dB of
travel, level 2,975, slow 3,344. An on / cap3 / off switch per class can use this table directly: tag each
`vol_parts` item with its class at the append, and classify `LEVEL_SHAPES` / `LEVEL_SHAPES_S` / `level_fits` rows
by how many note onsets they span (my rule: 3 or more onsets, or over 6 s, is slow; a plateau over at least 70 %
of one note is level; the rest is shape).

Measured on the stems, all 951 joined note pairs of winds, brass and strings (20 ms RMS; hole = softer body minus
the minimum between moved onset - 0.12 s and score onset + 0.10 s; peak = maximum over the louder body):

| | with the envelope | shape class divided out | all per-note classes divided out |
|---|---|---|---|
| holes over 6 dB | 188 | 211 | 172 |
| holes over 9 dB | 54 | 60 | 48 |
| peaks over 3 dB | 316 | 337 | 304 |
| peaks over 6 dB | 83 | 93 | 93 |
| re-bow dips over 6 dB (85 re-bows) | 30 | 54 | |
| same-pitch repeats dipping under 3 dB (85, S1) | 26 | 27 | 29 |

The shape class as a whole removes about 23 holes and 21 peaks at joins and halves the bad re-bows. The level
class adds holes at joins (finding 1). The "all off" column compares against bodies that are themselves lower
without the trims, so it understates the holes a listener would hear on weak notes.

## Findings

### 1. Level trims are keyed to the moved note-on and ramp inside the note: they cut the end of the previous note and fall to 0 dB between two notes that both need a lift (measured)

Layer: note trims and pitch trims (level class). Code: `trim_shape()` in `tools/score_to_parts.py` (lines
4270-4302), called at 4326 and 4985; data `build/note_trims.json`, `build/pitch_trims.json`. Verdict: **key differently**.

What the code does. A trim on a note that another note follows ends over `[next moved onset - 0.05 qn, + 0.03 qn]`.
The next note's moved onset is its legato lead (140-350 ms on strings) before the beat, while the old pitch is
still sounding. A trim on a joined note then starts from 0 at its own moved onset (pitch trims: 0.25 qn ramp) or
at its score onset (note trims: 0.6 s ramp). The breakpoints are not flagged exact, so `vol_points` writes them
on the 0.125 qn grid (144 ms at q = 52): the 0.08 qn crossfade becomes a 144 ms ramp placed by the grid.

- Violins I 82 (note trim +6 on the note before, lead 210 ms): designed release -268 to -175 ms before the beat,
  written -288 to -144 ms. On the stem the old note's last 140 ms sit 6.2 dB under its body, and the join hole is 7.2 dB.
- Clarinet 2 at 12 and 15 (note trims +9 / +10 / +9 on three joined notes): the envelope goes 10.0, 3.8 on the
  beat, 0.5 at +144 ms, 4.3 at +288 ms, 8.7 at +577 ms. Holes 6.9 and 6.1 dB; with the per-note classes divided out 3.1 and 0.5.
- Double basses 194 (pitch trims +4 then -5, lead 160 ms): the envelope is at -0.6 dB 120 ms before the beat and
  at -3.3 on the beat; the old note's end is 4.8 dB under its body.

Counts. The level class moves 1 dB or more inside 460 of 1,534 notes and 3 dB or more inside 173, so it is not one
value per note. At 67 led joins where the level drops 2 dB or more, the old note's last 140 ms are 2.0 dB (median)
under its body and 26 joins have a hole over 6 dB. 85 joined pairs carry same-sign trims that swing back towards
0 dB across the join (40 by 1.5 dB or more; 14 of those have a hole over 6 dB). 15 detached pairs with equal
trims return towards 0 in the gap (Bassoon 1 five times, Bassoon 2, Clarinet 2, basses).

Simulation on the stems (level class re-keyed: one value per note, crossfaded over 80 ms centred on the next
note's score onset, no return to 0 between joined notes):

| | now | re-keyed |
|---|---|---|
| 67 led joins with a drop of 2 dB or more: old note's end against its body | -2.0 dB | +0.2 dB |
| the same joins: holes over 6 dB | 26 | 17 |
| the same joins: peaks over 3 dB | 13 | 29 |
| 40 joined pairs with equal-sign trims: holes over 6 dB | 14 | 8 |
| Violins I 82 hole | 7.2 | 4.1 |
| Clarinet 2 12 / 15 holes | 6.9 / 6.1 | 3.5 / 1.9 |
| Bassoon 1 199 hole | 11.1 | 6.4 |
| Trombone 1 217 hole | 7.7 | 4.0 |
| 84 led joins with a rise of 2 dB or more: holes over 6 dB | 24 | 26 |

The gain is at drops and at equal-trim pairs; rises do not improve. The cost is in the third row: where the trim
no longer falls under the transition, 16 more transition peaks pass 3 dB, so the join-peak check must run after
the change and some joins will want a `JOIN_NOTCH_S` row.

Fix, in `trim_shape()`: for a joined pair, end the old trim and start the new one over the same window,
`[next score onset - 0.04 s, + 0.04 s]`, as one segment from the old value to the new (when both notes carry a
trim, no point at 0); drop the 0.25 qn and 0.6 s ramps on joined notes (keep the ramp only for the first note
after a rest and for the negative note trims named in the c09 comment, where a fast step deepened the sag: test
those three, Oboe 1 190, Cor anglais 152, Flute 1 254); return the points with the exact flag so `vol_bp` carries
them. For detached pairs closer than 0.5 s with trims of the same sign, hold the value through the gap. Check
S at the changed joins (a level step on the beat moves single S readings, Scherzo c14).

### 2. Three layers cure no measured fault and write movement on notes with no marking (measured)

- **Long-note swell** (`swell_db`, line 4247, `SWELL_DB` 1.5; shape class; 193 notes, 681 dB of travel). On 197
  sustained notes of 1.2 s or more with no hairpin, the range of the 100 ms level inside the note is 6.2 dB with
  the swell and 5.5 dB with it divided out; the swell makes 108 notes less even and 18 more even. Verdict:
  **remove** (`SWELL_DB = 0` in `score_config.py`). If a swell on long notes is wanted as a player's liberty, put
  it on CC1 (the vibrato crossfade on strings and woodwinds) as part of the phrase shape, not on every long note.
- **Metric steps on plucked notes** (`metric_db`, line 4359, `METRIC_DB` +1.5 / +0.5 / -1.0 in `METRIC_SPANS`;
  level class; 113 onsets). Note-to-note step of the attack peak, with / without: basses' pizzicato bars 37-44
  3.2 / 2.5 dB, harp bars 53-56 2.9 / 2.5, harp bars 7-14 0.5 / 0.4, harp bars 37-44 0.6 / 1.1, violas' triplets
  2.6 / 3.2. The round robins vary by more than the step in four of five passages. Verdict: **remove**
  (`METRIC_SPANS = []`), or keep only if the range test shows a listener-level difference. Velocity is not an
  alternative (mockup-kit LEARNINGS line 61: velocity steps gave 0.5-1.2 dB and raised the spread).
- **Slur-pair release** (`slur_pair_release`, line 4746, -2.5 dB on the second note of 15 two-note slurs; shape
  class). It is a fall under a sounding line written after the hall. No fault is named for it. Verdict: **move to
  CC11** (about -6 CC over the same window) so the hall keeps the first note's ring (S3 rule), or remove.

The passage where the envelope moves on every fast note is the violas' pizzicato triplets, bars 41-44 (qn
124-140): 42 onsets, 190 points, 140 dB of travel, of which 90 dB is the pizzicato pitch trims (-8 to +4 dB by
pitch, `pitch_trims.json` "Violas") and 41 dB the metric steps. The pitch trims help there (finding 3); the metric
steps are the removable part. The portato eighths of bars 48-51 carry almost nothing (15 notes, 5 points).

### 3. Per-note layers that cure a named fault: keep, with limits (measured)

| layer | fault | without | with | verdict |
|---|---|---|---|---|
| re-bow fills (`rebow_fills.json`) | dip and step at re-bows | dip median 7.6 dB, 55 of 85 over 6 dB; step over 2 dB at 58 | 4.8 dB, 30 over 6 dB; 29 | keep |
| early fills (`early_fills.json`, 276 notes of 0.5 s or more) | front of a legato target under its body | front minus body -3.6 dB; 166 fronts more than 3 dB under | -0.9 dB; 52 | keep, prune |
| join notches (`JOIN_NOTCH`, `JOIN_NOTCH_S`, 36 joins) | transition peak | peak median 6.5 dB, 20 over 6 dB | 3.7 dB, 2 over 6 dB | keep |
| pizz. pitch trims (Violas bars 41-44) | uneven sample levels by pitch | step median 3.4, P90 9.2 dB | 2.6, 6.9 | keep as level |
| S1 dips (`LEVEL_SHAPES_S`: basses 144 / 156 / 253, violas 81) | repeated note not separate | own dip 0.6 / 4.8 / 4.8 / 1.3 dB | 8.8 / 12.4 / 8.0 / 6.3 | keep |
| sostenuto hold (bars 61-62, 56 notes) | printed molto sostenuto | tilt -0.3 dB | +0.5 dB | keep (printed), or CC11 |

Limits to apply:
- Early fills: 204 of 276 help, 52 make the front-to-body difference worse by 0.5 dB or more, 28 put the front
  more than 3 dB over the body, and the 29 fills under 2 dB change the median by 0.4 dB. Remove the 52 and the 29,
  and cap the rest at +6 dB (34 are over 6, up to 8.3). `tools/auto_fills.py` can refit after finding 1 changes the joins.
- Join notches: one cuts a hole, Violoncellos 68.5 (two notches overlap to -9.6 dB, 193 ms before the beat; peak
  6.1 -> 2.1 dB but hole 1.7 -> 7.5 dB). Keep one of the two rows.
- Re-bow fills: several reach +10 dB 160-350 ms after the re-bow (Violoncellos 153.37, Violins II 165.86, 120).
  They work, so keep them out of the cap3 rule; treat them as their own sub-switch.

Moving these to a controller: the fills and notches act on the sample's own transition and loop, at fixed
times after the note-on, so CC11 would change the dynamic layer as well as the level; I see no evidence that
it would do better and did not test it (inferred). The level class on pizzicato could not go to velocity for the
reason in finding 2.

### 4. Start shapes stack and often peak after the attack (measured)

Of 1,008 notes of 0.5 s or more, 85 have two or more shape layers active at the start. The stacked peak is 5 dB or
more at 42 notes and 8 dB or more at 16. Of 392 notes with a start shape of 2 dB or more, 155 are 2 dB or more
lower on the beat than at the shape's peak, and at 72 the peak comes later than 250 ms after the beat.

- Violoncellos 253: early fill 5.9 + `level_fits` row 7.0 = 12.9 dB at +304 ms.
- Cor anglais 132: early fill 4.4 + `level_fits` 5.9: 3.1 dB on the beat, 10.1 at +80 ms, 7.2 at +250 ms.
- Horn 1 37.5: early fill 3.8 + `LEVEL_SHAPES_S` 6.0: 0.1 dB on the beat, 9.8 at +141 ms.
- Violins II 212 (the sf tremolo): accent 3.0 + `LEVEL_SHAPES` 10.6: 4.6 dB on the beat, 11.7 at +250 ms.

The printed accents are only Trombone 1 213 and 218 (plus the sf at 212). Their swell (`GENTLE_ACCENT`
`swell_s` 0.07 / 0.25 / 0.6 s) is front-weighted: 213 reads 1.6 dB on the beat, 3.9 at +80 ms, 0 by +500 ms, and
its 2-5 kHz attack is 1.3 dB under the body's (weight, not bite: Dan's note 9 holds). 218 reads 6.5 dB at +80 ms
and 8.0 at +250 ms (the accent row plus a level shape), over a 3 dB cap. Accented notes do not start weaker than
plain ones here; the late-peak cases are fills and level rows, not accents.

Verdict: **cap** the summed shape class at +6 dB per note in the build (not per layer), and where a `level_fits`
row and an early fill sit on the same onset, refit one row. Fix: after `vol_parts` is complete, evaluate the
shape-class sum on `vgrid` and scale it where it passes the cap; print each capped onset. The cap3 range test
will show which of the 42 notes need more than 3 dB (Violoncellos 253 was fitted in c54 and measured: 100 ms
steps -35.2 -34.7 -33.4 -33.3 dB, so that one is doing its job).

### 5. Re-bows that still dip more than 6 dB with their fills (measured; which are printed repeats is inferred)

30 of 85 entries in parts.json `rebows` dip more than 6 dB (30 ms level, minimum within -0.25 / +0.30 s against the
median of the second before and after). Worst: Violas 71.0 14.7 dB (the fill changes nothing), Violas div 79.0
13.9 (10.3 with the fill divided out: the fill makes it worse), Violas div 289.0 12.7, Double basses 283.605 11.6,
Violins II 292.0 11.0, Violins II 112.0 10.8, Violas div 70.0 9.9, Violas 271.0 9.7. Violins II 112 and 292 and
Violas 271 are S1 repeat points where a gap is wanted, so check each against `STR_REP_NEW_BOW` before changing it.
Violas div 79.0 and Violins I 205.949 (7.0 with, 4.8 without) are fills to refit with `tools/fit_rebows.py`.

### 6. Trombone 1 215.0: a bright attack on an unaccented eighth (measured)

In the quotation the 2-5 kHz level of the first 80 ms against the same band in the body is +9.9 dB at 215.0
(velocity 124) and between -1.3 and +1.0 dB on the other eighths and on the accented 213 (velocities 100-112).
`VEL_SET` lists 215.0 at 112; the written note has 124, so a later rule raises it. Fix: find the rule that adds
12 and set 215.0 to 112 like 215.5. This spot was tuned in c29-c41, so compare the level of 215 with its
neighbours after the change (the `LEVEL_SHAPES_S` row at 215.0 is +1.5 dB).

## Answers to the Slot A questions

- Do level steps and notches cut the end of the previous note? Level steps: yes (finding 1; 2.0 dB median at the
  67 drops, up to 6-10 dB at single joins). Notches: no, except Violoncellos 68.5; holes over 6 dB are 6 with and 6
  without the notches at their 36 joins.
- Are steps keyed to the moved note-on? Yes, `trim_shape()` uses `next_moved()` and `new_on()`, and the grid moves
  them up to 144 ms further.
- Accent and start shapes: finding 4.
- Which per-note shape layers cure a named fault: finding 3; which do not: finding 2.
- Do trims return to 0 dB between detached notes? Plucked trims do not (they crossfade 30-10 ms before the next
  onset). Bowed and blown trims do: 15 detached pairs and 85 joined pairs (finding 1).

Do not touch: the re-bow fills as a class, the early fills that help (204), the join notches, the pizzicato
pitch trims of the violas, the S1 dips of the basses (144, 156, 168, 253) and violas 81, Trombone 1's 213 accent
shape, the sostenuto hold of bars 61-62, and the slow layers (roles, hairpin gain, final fade).
