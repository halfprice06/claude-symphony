# Cycle 7, critic C: tempo, timing and transitions (render c06)

## Method

Everything below was measured on the stem-fixed c06 render (`cycles/c06/render/`, `mvt1-mockup-c06.mp3`) against `build/parts.json` (`sq` = score onset, `qn` = moved onset) on the parts.json tempo map. c06 is on the corrected time axis, so score qn maps to file time with no shift.

Measures used:
- Stereo-power envelopes: 20 ms window, 5 ms hop.
- Entries after a rest: the time a note reaches body - 12, - 8 and - 4 dB, where the body is the median level from +0.3 s to +0.7 s.
- Pitch changes: the crossover, meaning the first 30 ms over which the new pitch's harmonics 1-4 lead the old pitch's. This uses a 2048-point STFT, 5 ms hop. Bass lines and horns use 8192 points and harmonics 2-8 (kit LEARNINGS 16). Values on the search-window edge are dropped. I also measured the time the new pitch's own harmonics reach their maximum - 6 dB.
- Ensemble alignment: each track's value minus the median of the other tracks at the same score onset. There were 224 onsets with 4 or more tracks.
- Tempo map: beat lengths compared with the printed `\mt` steps in `global.ily`.

Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c07-C/`: lib.py, envs.py, onsets.py, xover.py, xover2.py, bassx.py, agg.py, sync.py, thr.py, shape.py, timp.py, rel_end.py, loops.py, acc.py. "Measured" means taken from the c06 files or parts.json; "inferred" means reasoned.

## Checks that passed (measured)

**Alignment.** Per-track median offsets from the other tracks at shared onsets lie within ±0.03 s for all 29 pitched tracks. The extremes are Harp -0.040 and Violas +0.030.

**Timpani.** Timpani minus the others: median -0.010 s over 45 strokes. The c02 value was -0.080.

**Wind pickups.** The wind pickups that c03 found late (Fl1/Ob1 at qn 88, 104.5, 552.5) now make their first sound within 0.025 s of Violins I. Their apparent lateness in the -6 dB measure came from the louder next note.

**Keyswitches.** All 913 precede their notes, by at least 9.5 ms (median 29 ms). None falls after its note.

**Printed tempos.** Every printed tempo step is realised within 0.6%. The one exception is bars 158-159 at -3.3% (the ramp plus the 636 caesura). Total length is 432.6 s against 430.8 s printed.

**Bar 170 fermata.** The ff chord releases together at qn 679, and the master falls from -10 to -67 dB during the 2.5 s fermata before the cello enters.

**Tutti cut-offs.** At qn 128.5, 288, 331, 504, 568.5 and 679, all stems fall 20 dB within 0.5-0.8 s of the note-off (hall tail). No section hangs on.

**Brief item 7 (loop pulsing).** Detrended, autocorrelation at 3.95 s:

| Passage | Level | 100-300 Hz | Centroid |
|---|---|---|---|
| Master, final chord (qn 712-728) | -0.14 | -0.13 | 0.06 |
| Sostenuto (488-504) | -0.08 | -0.01 | -0.20 |
| Lento chords (20-40) | -0.11 | -0.09 | -0.16 |

Horn 3 on the final chord: 100-300 Hz 0.36 at 3.95 s, best 0.56 at 3.25 s. That matches the 3.2 s spacing of its first two breath splits. This is left to the articulation critic.

**Brief item 8 (accents).** 2-5 kHz energy over the first 80 ms minus the body:
- Brass: median -7.7 to -16.0 dB, maximum +3.9 (Horn 1, qn 124).
- Strings: -10.5 to -11.1 dB.
- Winds: -12.1 to -13.1 dB.

Timing of accents: the first sound is on time (body - 8 dB at +0.00..+0.05 s). The swell's top arrives at +0.07..+0.15 s: Trombone 1 reaches body - 3 dB at +0.145 s and Trumpet 1 at +0.110 s. This is not ranked below. Inferred: it may sound like a slight lean after the beat rather than an attack.

## 1. The double basses change pitch 0.15 s late throughout the Allegro: the kit's abutting-note lead was not carried into movement I (measured)

**Where.** Double basses, 95 arco Sus MAX pitch changes that abut the previous note, in bars 10-46, 58-72, 78-101, 111-117, 135-144, 157-166 and 177-179. Also Horns 2-4 Sus MAX chord changes.

**What is wrong.** Crossovers measured with 8192 points and harmonics 2-8, from the score onset:
- Double basses: median +0.155 s, p75 +0.263, p90 +0.319. The 63 changes at Allegro tempos have a median of +0.150 s.
- Celli, same method: median +0.050 s (n=210).
- Basses minus celli at 60 shared changes: median +0.105 s, p75 +0.205.

Examples (basses / celli):

| Bar | qn | Basses | Celli |
|---|---|---|---|
| 22 | 86 | +0.365 | +0.025 |
| 25 | 97 | +0.340 | +0.095 |
| 36 | 140 | +0.300 | -0.025 |
| 46 | 182 | +0.290 | +0.050 |
| 69-70 | 276 | +0.285 | +0.100 |
| 90 | 358 | +0.325 | +0.075 |
| 94 | 372 | +0.310 | +0.090 |

At 126 bpm an eighth lasts 0.238 s, so the bass reaches each new harmony more than half an eighth after the celli. Every lead is 0.000 s.

**Cause.** This is the kit's LEARNINGS 6 (mvt II c20): on the Basses KS Master the old pitch takes about 0.46 s to fall 10 dB. Movement II fixed it with `ABUT_LEAD` "Double basses" 0.16 s and `skip_next_same`, which took the median from +0.20 to +0.03 s. In movement I, `score_to_parts.py` has `ABUT_LEAD = {}` and `build/score_config.py` does not set it.

**Horns.** Horns 2/3/4 on Sus MAX cross at a median of +0.087 / +0.100 / +0.115 s (n=16/56/29; p75 +0.139 / +0.120 / +0.175). Worst cases: Hn3 404 +0.32, Hn4 652 +0.305, Hn4 244 +0.23, Hn3 676 +0.225, Hn3 448 +0.215. Brass Sus entries after a rest arrive at +0.00..+0.03 s.

**Fix.** In `build/score_config.py`:

```
ABUT_LEAD = {"Double basses": {"lead_s": 0.12, "max_cc": 127, "overlap_qn": 0.0, "skip_next_same": True},
             "Horn 3": {"lead_s": 0.06, "max_cc": 127, "overlap_qn": 0.0, "skip_next_same": True},
             "Horn 4": {"lead_s": 0.06, "max_cc": 127, "overlap_qn": 0.0, "skip_next_same": True}}
```

- The bass value is 0.12 rather than movement II's 0.16, because the lag here is 0.15 s, not 0.20 s.
- The old note ends at the moved start, as in mvt II.
- Target: basses minus celli median under +0.04 s, horns 3-4 median under +0.06 s.
- Check the same-pitch repeats next to every led note for new troughs. Mvt II c20 found one new 7.7 dB trough of 0.06 s.

## 2. Slurred Sus MAX string eighths change pitch 0.09-0.12 s late; the c05 lead test failed because the old note kept sounding (lateness measured, cause inferred)

**Where.**
- Violins II: 16 slurred short Sus MAX notes (bars 21, 29, 69-71, 95, 102, 139-140).
- Violas: 102 notes (bars 29, 69-71, 92, 98-102, 112-121, 139-142, 169).
- Violins I: the same eighths after the c06 Leg Slur test is reverted (c05: median +0.12 s).

**What is wrong.**
- Violins II: crossover median +0.122 s (p25 +0.102, p75 +0.143). The new pitch reaches its own maximum - 6 dB at +0.085 s.
- Violas: +0.085 s (p75 +0.115). The new pitch reaches its own maximum - 6 dB at +0.060 s.
- Worst cases: Vln II 277/279.5/281 (bars 70-71, the brass theme's counter-figure) +0.16/+0.175/+0.195; Vla 273 +0.18, 566 +0.185, 445.5/447.5 +0.17.
- For comparison, legato joins on the same tracks cross at +0.03..+0.065 s.

At 126 bpm these eighths land a third to half of an eighth late, and the slurred figures of the first theme drag.

**Why the c05 test failed (inferred).**
- The c05 test (`SHORT_SUS_LEAD_S` 0.05 s on Vln I/II) moved the crossover only 0.015-0.02 s.
- The branch in `score_to_parts.py` ("the old note's end stays: a longer crossfade") moves the new note-on earlier but leaves the previous eighth's note-off where it was. So the old pitch keeps full level over the whole lead. In c06 the previous eighth still ends +0.014 s after the score onset.
- Movement II's bass fix worked only with the old note ending at the moved start (kit LEARNINGS 6, c20).

**Fix.** In `tools/score_to_parts.py`, short_sus lead branch: when the lead is applied, also set the previous slurred note's `end` to the moved onset + 0.03 qn, so the overlap stays 0.03 qn relative to the new note-on. Make this a flag, `SHORT_SUS_LEAD_KEEP_OVERLAP = True`.

In `build/score_config.py`, in the same cycle:
- Set `SHORT_SUS_LEAD_S = 0.06` and `SHORT_SUS_LEAD_TRACKS = ("Violins I", "Violins II")`, with the Violas as the control.
- Revert the failed c06 test: `SHORT_SUS_LEG_TRACKS = ()` and remove the Violins I `LEG_CAP_FRAC` entry.

Targets:
- Crossover median at or under +0.07 s on Vln I/II.
- Joins dipping 6 dB or more no more numerous than in c05 (9 of 72 on Vln I).

If it works, extend it to the Violas.

## 3. String entries at the mf layer arrive 0.17 s late; the off-beat motor of bars 15-22 loses its syncopation (measured)

**Where.**
- Violins II (13 entries) and Violas (5 entries), bars 15-22 (qn 56.5-84.5): the eighth-tied-to-quarter on the "and" of beats 1 and 3.
- Violas, bars 64-67 (qn 253-265).
- Vc 348; Vln I 440 and 619; Vln II 619.

**What is wrong.** There are 33 string entries after a rest in the Allegro at CC11 51-80. Times to body - 8 / body - 4 dB, from the score onset (medians):

| Row and layer | n | Body - 8 dB | Body - 4 dB |
|---|---|---|---|
| Leg Slur MAX, CC11 51-80 | 23 | +0.065 s | +0.170 s |
| Sus MAX, CC11 51-80 | 10 | +0.055 s | +0.173 s |
| Leg Slur MAX, CC11 > 80 | 16 | +0.050 s | +0.092 s |
| Sus MAX, CC11 > 80 | 20 | +0.032 s | +0.050 s |

Specific entries:
- Vln II bars 15-22: body - 4 dB at +0.155..+0.25 s (56.5 +0.17, 62.5 +0.25, 68.5 +0.25, 70.5 +0.235).
- Vla 56.5-70.5: +0.14..+0.185.
- Vla 253-265: +0.165..+0.185.
- Vln I 440: +0.265.
- Vc 348: +0.215.

Shape of Vln II 58.5: -7..-8 dB re the body until +0.10 s, -3 dB at +0.175 s.

In bars 15-22 the basses' off-beat eighths on the "and" of beats 2 and 4 are at body level at their onset. The violins' and violas' off-beats on 1 and 3 swell in about an eighth later, so the interlocking pattern is uneven.

The cause is the family entry lead: `ENTRY_LEAD_S["string"] = (0.12, 0.06)` gives only 0.06 s above CC 50. The mf layer of these rows starts quieter and rises over about 0.2 s, about 0.1 s slower than the f layer (measured above).

**Fix.** In `tools/score_to_parts.py`, entry-lead branch (`s_ = ... (ent_s[0] if final(q) <= 50 else ent_s[1])`), add a third value used for CC11 51-80 at 100 bpm or faster:

```
ENTRY_LEAD_S["string"] = (0.12, 0.06, 0.12)
```

The existing rest cap (L ≤ q - pe - 0.02 qn) allows up to 0.23 s after an eighth rest at 126.

Config-only alternative: add +0.06 s per onset in `build/entry_leads.json`:
- Violins II: 56.5, 58.5, 60.5, 62.5, 64.5, 66.5, 68.5, 70.5, 72.5, 74.5, 76.5, 82.5, 84.5, 619.
- Violas: 56.5, 58.5, 60.5, 64.5, 70.5, 253, 257, 261, 265.
- Violoncellos: 348.
- Violins I: 440, 619.

Targets:
- Body - 8 dB at -0.02..+0.02 s.
- Body - 4 dB under +0.12 s.
- First sound no more than 0.06 s before the beat.

## 4. The tempo speeds up again at the start of the printed "poco rit." of bar 145 (measured)

**Where.** Bars 144-146 (qn 572-584). In milder form, the beats before the two printed "poco animando" bars (qn 243-244 and 619-620).

**What is wrong.** Beat lengths on the c06 map:
- qn 574: 501 ms (120 bpm)
- qn 575: 541 ms (111 bpm)
- Bar 145, where "poco rit." is printed: 480, 487, 493, 499, 505, 513 ms
- The printed ritardando gets back to the 541 ms of beat 575 only at about qn 583.

So the music slows on the last beat of bar 144, speeds up by 13% for six beats inside a printed rit., and then slows again. The oboe's dolce entry at qn 578 comes at 122 bpm, after a beat at 111.

**Cause.** `PHRASE_ARCS (568, 576, "main")` (x0.95/x0.88 on its last two beats) ends exactly where `RAMP_SPANS (576, 584, 126)` begins. `phrase_arcs()` skips an arc only when it overlaps a ramp (`a < e2 - EPS and e > a2 + EPS`), so an arc that ends at a ramp's start is not caught. Movement II removed its (90, 102) arc by hand for the same reason.

The same adjacency, without a reversal, happens before both animandos. Beats 243 and 619 run at 103 bpm (582 ms). Then the animando ramps start at 112 bpm on qn 244 and 620, where 115 is printed, so the animando begins from below the printed tempo.

Inferred: beat 127 at 111 bpm (x0.88), the violins' sixteenth run into the ff of bar 33, also drags. A "sub" depth would be enough there.

**Fix** in `build/score_config.py`:
- `(568, 576, "main")` → `(568, 576, "sub")`.
- `RAMP_SPANS (576, 584, 126)` → `(576, 584, 120)`. The rit. then continues from beat 575 (about 120 at "sub" depth) down to 112.
- `RAMP_SPANS (244, 260, 112)` → `(244, 260, 115)`.
- `RAMP_SPANS (620, 632, 112)` → `(620, 632, 115)`.

In `tools/score_to_parts.py`, `phrase_arcs()` should warn, or drop the last-beat slowing, when an arc ends within 0.01 qn of a ramp whose tempo falls.

**Check.** No beat in qn 568-584 should be slower than the beat after it.

## 5. The Lento and the coda solos run at an exactly constant tempo (tempo map measured; musical effect inferred)

**Where.**
- Bars 1-14 (qn 0-56): Vc/Cb/BCl phrase, cor anglais espr. solo bars 5-9, crescendo to the f of bar 12, horn solo bars 13-14.
- Più lento bars 171-176 (qn 680-704): the cello solo espr. with five hairpins and the cor anglais imitation.

**What is wrong.**
- The tempo map has a single point at 50.0 bpm for all 56 beats of the Lento: every beat is 1.200 s, 67.2 s in total.
- It has one point at 72.0 for the 24 beats of the Più lento: every beat 0.833 s.
- The Allegro and second theme have had phrase arcs since c04. The Lento and coda arcs were deferred because they move the string re-bow points:
  - Before qn 56: 6, 12, 16, 21 and 19 re-bows on Vln I, Vln II, Vla, Vc and Cb.
  - After qn 680: 3-8 per track.
- About 70 s of slow espressivo music has no agogic shape at all.

**Fix.**
1. Freeze the re-bows first. For each string track, add its current parts.json `rebows` points with qn < 56 or qn ≥ 680 to `REBOW_AT`. A note with listed points uses exactly those points and no automatic ones. Then check that every `rebows` row is unchanged in qn after the build.
2. Add arcs:

```
PHRASE_ARCS += [(0, 16, "sub"), (16, 36), (36, 48), (48, 56, "main"), (680, 688, "sub"), (688, 696)]
TEMPO_PUSH += [(36, 46, 1.015)]
```

The push leads into the f of bar 12.

Do not end an arc at 704, where the printed rit. ramp starts; that is finding 4's problem.

**Expected and checks.** About +2 s in total. After the render:
- Rerun `fit_rebows.py` on the Lento pieces. The shapes are timed in seconds from the points, which move less than 5% in time.
- Check the climax order and the first-theme entry at qn 56.

## 6. The delivered mp3 ends with 7.2 s of silence, so the printed "attacca" into movement II becomes a long pause (measured)

**Where.** The end of `mvt1-mockup-c06.mp3`.

**What is wrong.**
- The final chord's note-offs are at qn 728 = 432.60 s. The master is at -56 dBFS at +0.1 s, -67 at +0.6 s and -82 at +1.1 s, and is digitally silent from +2.6 s.
- The delivered mp3 is 440.60 s long. Its last 50 ms window above -60 dBFS is at 433.11 s, and above -70 dBFS at 433.41 s. That leaves 7.2-7.5 s of silence.
- The render runs to `score_end` + 8 s (`render_cycle.py` line 58: `TimeMap2_QNToTime(...) + 8`).
- The score marks the last bar "attacca", and movement II's mockup sounds from 0.00 s. Played in sequence, the attacca becomes a pause of more than 7 s.

**Fix.** In `tools/deliver_master.py`, after the limiter:
- Find the last 50 ms window above -65 dBFS.
- Trim the mp3 to 1.0 s after it, with a 0.5 s fade-out (ffmpeg `atrim=end=T+1.0,afade=t=out:st=T+0.5:d=0.5`).
- Keep the wav render at +8 s for measurement.
- Print the trimmed tail length in the delivery metrics.
- Target: under 1.5 s of tail.

## Do not touch

- `TIMP_DELAY_S` 0.06 and the crash and tam-tam `delay_s` 0.05: timpani minus the others median -0.010 s.
- The sus. cymbal `lead_s` with `CAESURA {636: 0.15}`.
- `BEAT_STRETCH {679: 0.6}`: a 2.5 s fermata, with the master at -67 dB before the cello.
- The `RAMP_SPANS` realisation of the printed rit., allargando and animando steps: within 0.6% of every printed step.
- The final bar at 30 bpm with its fade and staggered re-bows (master loop autocorrelation ≤ 0.06).
- Keyswitch placement: 913 keyswitches, minimum 9.5 ms before their notes.
- The c04 halved wind entry extras: pickups now on time.
- Brass Sus entries: median -0.01 s relative to the others.
- The Leg BC MAX leads: Vln I/II, Vla and Vc median crossovers +0.045..+0.065 s, within ±0.03 s of the other tracks.
- The Allegro and second-theme phrase arcs, apart from the (568, 576) end in finding 4.
