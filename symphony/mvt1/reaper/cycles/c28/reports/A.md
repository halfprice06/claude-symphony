# Cycle 28, critic A: articulation and phrasing (render c27)

Scope: the c27 render (`cycles/c27/render/`, after its stem fix) against `build/parts.json`. c26 (`cycles/c27/before/parts.json`) is the control: on most notes the two renders have the same data. Scripts and per-frame features (5 ms hop, 1024-sample FFT, 2-5 kHz, 100-300 Hz and 1-8 kHz bands, power) were in `/private/tmp/claude-501/mockup-loop/mvt1-c28-A/`. That folder was deleted at the end, as the brief requires. I reran the c22 battery on c27 (kscheck, chordleg2, ties, joins, rebow, breath, acchf). New scripts: `accm.py` (accent 2-5 kHz on the stem and the master, with each stem's share), `accw.py` (accent body against plain neighbours), `dbow2.py`/`lift.py`/`rise.py` (printed down-bows and up-bows: row, gap, lift depth, rise), `rep.py` (same-pitch re-attacks), `even.py` (note-to-note level of exposed monophonic lines), `harp2.py`/`harp3.py`/`harpfix.py`/`harpm.py` (harp note peaks within each figure, and against the master), `pz.py` (pizzicato and stroke evenness), `env.py` (each note's planned envelope dB, CC11 and rendered body), `sim.py`/`sim2.py` (level shapes simulated on the stem and the master). Score pages 1, 3, 5, 15 and 17 checked.

## Checks that passed (measured, no action)

- **Keyswitches and chords.** No chord on a legato row (chordleg2 is empty). The keyswitches that land inside sounding notes are the planned row changes, as in c26. Ties re-attack only at the timpani re-strikes (44, 456, 560, 640) and the basses' "change bow at will" (288, 716).
- **Legato joins.** Stem dip medians: Vln I 2.0, Vln II 2.5, violas 1.8, celli 1.4 dB. Winds 1.1-3.2, horns 0.1-2.7. The joins of 6 dB or more are the known ones (Vln II 637/393/234, violas 361.5, celli 112/215, Clarinet 1 227). The c27 lead changes (C #1, C #3) opened no new hole.
- **Item 8, 2-5 kHz first 80 ms minus body.** Brass median -8.1 dB (n 81), winds -3.8 (n 98), strings -3.3 (n 129).
  - Clarinet 1 414/422 rendered bright again. After the actor's c27 stem fix they read +4.9 / +3.1.
  - The other loud fronts (Clarinet 1 558 +10.4 and 120 +7.6, Bassoon 1 536, Trumpet 1 284 +6.9) are 7-15 dB under the master in that window. The master's 2-5 kHz front over the 0.3 s before them is +2.9 dB or less.
- **Accent weight** (accent body against its plain neighbours within 2 qn; exposed accents only, n 65). 59 are level with or over their neighbours. The six under them are the known 536 dyad releases, the Clarinet 1 state notes and Vln I 381.
- **Item 7, re-bows.** Dip medians and steps are unchanged from c26. The two large steps (celli 163.877 and 727.116) are printed diminuendos.
- **Pizzicato.** Basses bars 47-55 within 5.4 dB, peaks 0.03-0.23 s. Fugato and recapitulation within 3-5 dB.
- **Timpani.** Coda strokes 712-718 within 1.8 dB. Breath gaps are as in c26.
- **Repeated down-bows** (bars 32, 72, 83, 142). The master lifts 8-13 dB between the strokes. On the stems, Vln II 124 -> 125 lifts only 0.8 dB and the basses 284 -> 285 3.6 dB. The master covers both, so there is no action.

## 1. Coda, Più lento, bars 172-174 (qn 684-694): the cello solo's level jumps up and down from note to note, and the crescendo into the top note runs backwards. The cor anglais' long E-flat 5 sinks under it (measured; fix simulated)

**Where.** Violoncellos qn 688-693, the mp espr. solo that is the master's main voice (celli -0.6 to -2.9 dB re master). Cor anglais qn 684-687, its p espr. partner (score page 17).

**Score.** Bar 172 has a < from 685 to 687. Bar 173 is flat (688 dotted quarter, 689.5 eighth, 690 quarter) and then has a < over 691 and 691.5 into the half note 692, the top of the phrase. 692 is followed by a > to 694.

**Evidence (measured, c27; c26 within 0.5 dB on every note).**

Master per note (score onset +0.1 s to the next onset):

| qn | 685 | 687 | 688 | 689.5 | 690 | 691 | 691.5 | 692 | 694 |
|---|---|---|---|---|---|---|---|---|---|
| dB | -31.9 | -33.3 | -33.0 | **-36.0** | -32.5 | **-36.4** | **-35.6** | -32.8 | -38.1 |

- The eighth E-flat 4 at 689.5 is 3.3 dB under its flat neighbours on the master and 5.5 dB under them on the stem (-40.3 against -34.8 / -34.5).
- In 50 ms frames, the stem sits at -38..-43 dB from qn 689.22 to 690.25. That is 0.85 s, covering the E-flat and the first 0.25 s of the D-flat after it, against -31..-35 on both sides.
- The two eighths that carry the crescendo (691, 691.5) are 3-4 dB under the 690 before them. The top note 692 is not louder than 690 (-32.8 against -32.5). The printed crescendo comes out as a fall and a recovery.
- **Cause.** CC11 is flat at 67 from 686.6 to 691.1, so the cause is samples plus the existing fills (`env.py`).
  - The envelope already lifts the legato targets: +6.3 at 687, +5.0 at 690, +7.3 at 691.5, +6.4 at 692.
  - 689.5 sits in the decay of the 688 fill (+2.1 dB).
  - The rendered body minus the envelope varies from -37.3 to -44.3 dB from note to note. The quietest are 689.5, 691 and 691.5.
- **Cor anglais.** The E-flat 5 at 684 (a legato target a sixth above the pickup) is 5.4 dB under its own pickup G4 at the same envelope (-41.2 against -35.8; body minus envelope -47.6 against -41.9). It sits 8.1 dB under the master: inside the duet, the long note of the p answer falls under the mp cello by twice the printed step.

**Fix.** Add these to `build/score_config.py` as exact `LEVEL_SHAPES` steps (score qn breakpoints, written exactly, not on the grid, as for the c27 fugato steps). Do not ramp into a join.

```
LEVEL_SHAPES["Violoncellos"] += [
    [(689.18, 0.0), (689.26, 5.0), (690.22, 5.0), (690.34, 0.0)],
    [(690.80, 0.0), (690.90, 3.0), (691.25, 3.0), (691.35, 4.0), (691.80, 4.0), (691.95, 2.5), (692.6, 2.5), (693.0, 0.0)]]
LEVEL_SHAPES["Cor anglais"] = LEVEL_SHAPES.get("Cor anglais", []) + [[(684.1, 0.0), (684.4, 4.0), (686.8, 4.0), (687.2, 0.0)]]
```

These are level-only, so a stem fix plus `--mix-only` on the two tracks would do.

Simulated on the c27 stems:
- Master: 689.5 -36.0 -> -35.2 (frames 689.26-690.25 rise from -35..-39 to -32..-37), 691 -36.4 -> -33.6, 691.5 -35.6 -> -33.0, 692 -32.8 -> -31.8. The top note is now the loudest of bars 172-174.
- 30 ms peaks at the joins rise 0.2-3 dB. None goes over the 692 body.
- Cor anglais 684: -41.2 -> -37.7 (master -33.2 -> -32.4).
- Leave 684 (the cello's C4 at the end of the > from 683.5, master -36.0). The printed diminuendo explains part of its dip.

**Pass.**
- Master per note from 688 to 692 never falls by more than 1.5 dB from one note to the next.
- 691, 691.5 and 692 rise, and 692 is the loudest note of 684-694.
- The cor anglais at 684 sits within 2 dB of its pickup.
- No 30 ms peak at 689.5-692 is more than 2 dB over the 692 body.

## 2. Harp, second theme bars 47-59 (qn 184-236): single notes of the p arpeggios jump 7-10 dB over the rest of their figure, and the half-note tops fall 5-8 dB under it (measured; deterministic)

**Where.** Harp (Harp Sus RR), the right-hand eighth-note arpeggios under the cello and horn dolce theme. Score page 5: p, each bar four eighths up to a half note.

**Evidence (measured).** Each note's 10 ms peak in its own window, minus the median of the other single notes of the same bar (`harp3.py`). The c26 and c27 renders are identical to 0.1 dB on all 110 harp onsets, so this is the sample set's round robin, not chance.
- **Too loud.**
  - 185.5 (C6, v74) +7.1
  - 193.5 (D-flat 5, v76) +7.5
  - 200.5 (G-flat 4, v52) +7.8
  - 209.5 (D-flat 5, v76) +7.3
  - 222.0 (C6) +6.5
  - 231.0 (B-flat 6) +7.6
  - Bar 59 at mf: 234.0 / 235.0 +4.8 / +4.7.
- **Too weak.**
  - The half-note tops: 190.0 (A-flat 5) -4.9, 198.0 (B-flat 5) -4.9, 206.0 (A-flat 5) -7.9.
  - 218.0 (E-flat 5) -5.3.
  - 234.5 / 235.5 -5.4 / -4.8.
- **On the master** (`harpm.py`, 0.1 s from the onset): the harp note at 193.5 is -1.5 dB re master and at 209.5 -0.7 dB. The figure's other notes sit -12..-15 dB under the master. For one eighth the harp becomes the loudest thing in the orchestra, inside a p accompaniment.
- **Cause.** The same pitch at the same velocity renders 10-12 dB apart at different points in the round robin: D-flat 5 v76 measures -29.8 / -33.0 at 193.5 / 209.5 and -39.4..-42.1 at 189, 197, 205 and 213.
  - `HARP_PITCH_VEL` (score_config.py line 1339) is a per-pitch table, so it cannot follow this.
  - 17 of its 31 entries already sit at the ±12 cap, D-flat 5 among them (+12).

**Fix.** Per-onset velocities through the existing `VEL_SET` (`score_to_parts.py` line 2331, applied after `HARP_PITCH_VEL`). Values: the deviation divided by 0.4 dB per velocity step, capped at ±20 and floored at 40. The figure-first note at 222.0 gets a half correction.

```
VEL_SET["Harp"] = {185.5: 56, 190.0: 76, 193.5: 57, 198.0: 88, 200.5: 40, 206.0: 84, 209.5: 58,
                   218.0: 65, 222.0: 66, 231.0: 57, 234.0: 86, 234.5: 111, 235.0: 86, 235.5: 110}
```

Velocity changes do not move the round-robin order (the CC36 reset is in the pre-roll), so the cycle stays where it is. The response per velocity step is inferred (kit LEARNINGS 9: 0.3-0.6 dB per step), so measure it after the render. Do not change `HARP_PITCH_VEL`: the onsets not listed keep their c27 levels.

**Pass.**
- Bars 47-59: every single harp note within ±3.5 dB of its figure's median, and each half-note top at -2 dB or more.
- No harp note louder than 6 dB under the master in bars 47-58.
- Harp level per bar within 1 dB of c27.

## 3. Doubled brass lines are still one player at +3 dB (patch; inferred, carried)

- `unison_dropped` is unchanged:
  - Trumpet 2 21 notes (the coda theme 167-170, and 131-132)
  - Trombone 2 29 notes
  - Horn 4 18 notes
- In the coda theme, Trumpet 1 is the top 2-5 kHz source at 665-676 (-2.0..-7.0 dB re master at its accents). It is one solo-trumpet sample where the score has two trumpets a2.
- The route is as in c26 A #2 / c27 A #3: `2 Trumpets/04 Legato` Leg Slur MAX (or the 2TP KS Master with only Sus Non Vib MAX and Leg Slur MAX loaded) on a 34th track for 664.4-676.5. Do this only in a cycle with its own render, and only if the settled footprint stays at about 45 GB (c27: 46 GB).
- No new measurement. This finding is kept short.

## Do not touch

- The c27 fugato steps and the celli 348 stroke, and the Clarinet 1 414/422 per-render check.
- The c27 leads (Vln I Leg BC +0.05, the listed cap 0.95, LEG_MIN_GAP_S 0.06, celli Leg BC -0.02, the C #3 negative extras) with their moved fills: no new join holes.
- GENTLE_ACCENT on brass, winds and strings, and the accent fits and bodies.
- The re-bow times with `rebow_fills.json`, the down-bow strokes and Marc LITE rows, the pizzicato and timpani velocities, and the breath and caesura settings.
- `HARP_PITCH_VEL`: keep it as the base and correct only the listed onsets.
- The existing coda celli shapes (682.15-683.3, the 691.6 crest): finding 1 adds to them and does not replace them.
