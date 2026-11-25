# Cycle 29, critic A: articulation and phrasing (render c28)

Scope: the c28 render after its stem fix (`cycles/c28/render/`) against `build/parts.json`. c27 is the control where a result needed checking for repeatability. Features (5 ms hop, 1024-point FFT: power, 2-5 kHz, 100-300 Hz, centroid) and simulations used scratch scripts in `/private/tmp/claude-501/mockup-loop/mvt1-c29-A/` (deleted at the end). Score pages 1 and 5 (bars 1-14 and 47-63) were checked. All levels are plain stereo power. In the 40-50 ms frame tables, frame 0 is the start of the window named in each finding.

## Checks that passed (measured, no action)

- **Chords on legato rows.** None: no note on a Leg Slur, Leg BC, Leg Port or Slur Runs row overlaps a different pitch that starts at the same onset.
- **Slur boundaries.** No wind or brass note that starts a new slur, or follows a slur end, is played as a legato transition. The strings play 64 unslurred held chord notes on Leg Slur MAX. Most are pp chorale or pedal notes (Vln II 700-712, violas 690-724, celli 704/712), where a new bow is not audible. No action.
- **Legato joins** (30 ms frames, dip under both bodies). Medians: Vln I 2.8, Vln II 3.0, violas 2.4, celli 1.9, winds 2.1-3.3, horns -0.2..2.4 dB. The joins of 6 dB or more are mostly the known ones (Clarinet 1 227, Vln II 220/234/393/637, celli 112/215). The new exposed ones are in findings 1 and 3.
- **Item 8, accents.** 2-5 kHz over the first 80 ms against the body, medians: winds -2.2 (n 232), brass -3.8 (n 168), strings -1.2 (n 170), timpani -4.5 dB. The master front over the 0.3 s before it: +1.7..+1.9 dB median. Every master front over +4 dB where the stem matters is a phrase entry after a softer bar (Vln I 57/65/105/128/145, celli 337), not a bright attack. Vln I 128 (+5.2 stem) is the ff tutti arrival after the Slur Runs pickup.
- **Item 7.** The `loopscan.py` run on c28 matches c28's own numbers. Master Lento +0.40, 160-164 -0.51, final chord -0.38 at 3.95 s. No stem over 0.42 on a window long enough to measure.
- **Re-bows.** Median dips 1.2-3.3 dB. The large steps are printed hairpins (basses 506.408 inside the 504-512 pp < mf; celli 163.877). The one left is finding 4.
- **Staccato.** Marked eighths render at 0.23-0.24 s spacing on Stac RRx9/RRx14 (strings) and on shortened Sus (winds; the wind Stac DblTng test failed in c03). The quarter staccatos at 368-371 / 356-359 decay 12 dB in 0.26-0.44 s.
- **Tenuto.** Tenuto notes are full length on legato rows (1.9-2.3 qn of 2), with no hole at the onset.
- Harp étouffez, sul tasto EQ, pizzicato rows and portamento (225, 685) are unchanged from c28 and were not re-measured.

## 1. Lento bars 6-7 (qn 23.5-24.6), cor anglais espr. solo: the A4 eighth sags 7 dB inside the note, and the G4 legato arrival then bursts 6 dB over its own body on the master (measured; deterministic; fix simulated)

**Where.** Cor anglais, the main voice of the passage (-0.9 dB re master at the join). Score page 1: a tied B-flat 4 ends with an eighth A4 (23.5). Then comes G4 (24.0), a half note with a printed < > in bar 7.

**Evidence (measured).** 40 ms frames from 23.5 qn - 0.2 s. The c10, c20, c26 and c28 renders agree within 1 dB.

| | A4 0-0.16 s | A4 0.16-0.28 | A4 0.28-0.40 | 0.40-0.56 | join 0.56-0.64 | G4 +0.06..+0.3 s | G4 later |
|---|---|---|---|---|---|---|---|
| CA stem | -38..-39 | -35 | **-42..-43** | -37..-34 | **-31** | -39..-41 | -38..-40 |
| master | -35..-36 | -33..-34 | -37..-38 | -35..-33 | **-30** | -37..-39 | -37..-38 |

- **Cause.** The volume envelope (parts.json `vol_db`) carries `pitch_trims.json` Cor anglais A4 -5. On this joined eighth, `trim_shape()` (score_to_parts.py line ~3466) ramps it in over 0.25 qn from the moved onset 23.4577. At 50.75 bpm that is 0.30 s of a 0.59 s note, so it reaches -5 only at 23.7077 and leaves at 23.9077-23.9877, just before the G4's legato transition.
- **Result.** The trim forms a V inside the eighth (-4.1 dB at 23.71). It then rises +4.8 dB into the Leg Slur transition sample, which is itself loud.
- **On the master.** The 30 ms peak at the join is -29.7 dB, 6-8 dB over the G4 body that follows (-37..-38). The printed < on the G4 therefore starts with a burst and a fall.

**Fix.** Add this exact shape to `build/score_config.py`. It adds to the existing CA shape at line ~832, which is flat +2 over 19.5-27.

```
LEVEL_SHAPES["Cor anglais"] = LEVEL_SHAPES["Cor anglais"] + [
    [(23.66, 0.0), (23.72, 4.0), (23.84, 4.0), (23.90, 0.0), (23.94, -4.0), (24.04, -4.0), (24.10, 2.0), (24.60, 2.0), (25.00, 0.0)]]
```

It is level only, so a stem fix plus `--mix-only` on Cor anglais is enough.

Simulated on the c28 stems:

| | old | new |
|---|---|---|
| CA frames, 23.6-24.6 qn | -31..-43 | -33..-39 |
| Join 30 ms peak, CA | -30.1 | -34.1 |
| Join 30 ms peak, master | -29.7 | -33.2 |
| G4 24.1-24.9, CA | -38.6 | -36.9 |
| G4 24.1-24.9, master | -37.0 | -35.8 |
| 24.9-25.9 (the < continues) | -36.1 | -36.1 |

- The bars around it are unchanged.
- Optional generic fix (inferred; do not do it this late without a full check): in `trim_shape()`, cap the joined-note ramp at min(0.25 qn, 0.10 s). The same V can occur on any short trimmed legato note at a slow tempo.

**Pass.**
- CA 40 ms frames from 23.6 to 24.6 qn within -33..-39 dB.
- Master join peak at most 2 dB over the G4 body.
- G4 body within 1.5 dB of the A4 body.

## 2. Second theme bar 52 (qn 204-208), Horn 1 + celli dolce unison: the printed > on 204-206 comes out as a 7 dB hole and a 6 dB rebound (measured; fix simulated)

**Where.** Horn 1 (Leg Slur MAX) and Violoncellos in unison, p dolce. Score page 5, bar 52: A-flat dotted quarter (204), G eighth (205.5), then F (206: a half note in the horn, a quarter in the celli), with a > from 204 to 206. The celli's F5 at 207 starts the next phrase.

**Evidence (measured).** Per note, onset +0.06 s to the next onset (at most 0.9 s). Values are the power sum of the two stems / the master:

| qn | 203 | 204 | 205.5 | 206 | 207 |
|---|---|---|---|---|---|
| Hn1 + Vc | -27.4 | -31.4 | **-38.4** | **-32.8** | -34.7 |
| master | -27.4 | -30.8 | -37.0 | -32.1 | -34.0 |

- **The hole.** The celli fall 10 dB from 204 to 205.5 (-33 -> -43..-44 in 50 ms frames).
- **The rebound.** Horn 1's F4 arrives with a burst at about 206.1 (-39 -> -32). It then blooms back to -32 over 206.6-207.0, louder than its own 204 note (-36.8 alone).
- So the diminuendo goes down 7 dB and back up 6 dB on the last note it covers. The other halves of this theme (bars 47-51, the recap at 604-606) do not show this.

**Fix.** Add these exact shapes to `build/score_config.py`:

```
LEVEL_SHAPES["Violoncellos"] += [[(205.35, 0.0), (205.5, 4.0), (206.5, 4.0), (206.9, 0.0)]]
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(205.35, 0.0), (205.5, 3.0), (206.0, 3.0), (206.08, 0.0),
                                                    (206.12, -4.0), (207.8, -4.0), (208.0, 0.0)]]
```

The horn cut must not start before 206.08: a cut from 206.05 opened a -44 dB hole in the eighth's tail in the simulation. These are level only, so use a stem fix plus `--mix-only`.

Simulated:

| qn | 204 | 205.5 | 206 | 207 |
|---|---|---|---|---|
| Hn1 + Vc | -31.4 | -35.0 | -35.5 | -36.8 |
| master | -30.7 | -34.3 | -34.2 | -35.3 |

- The diminuendo is now monotone.
- Horn 1 alone: -36.7 / -37.5 / -37.5 / -39.8.

**Pass.**
- Hn1 + Vc and the master fall from 204 to 206, with no note-to-note step over 4 dB.
- 206 is not louder than 205.5 by more than 0.5 dB.
- No 50 ms frame of Horn 1 over 205.9-206.3 is more than 3 dB over its 205.5 body.

## 3. Two exposed wind legato joins with holes from the volume envelope: Clarinet 1 213 (bar 54) and Oboe 1 579 (recap dolce, bar 145) (measured; partly fixable; stem level only)

**Clarinet 1, 212 -> 213** (A-flat 4 -> G4, slurred, p, -8.7 dB re master).
- **Cause.** The `vol_db` drops from +4.28 at 212.857 to -0.78 at 212.937, then returns to +2.65 at 213.017. The A-flat 4 throat trim (+5) ramps out at the G4's moved onset - 0.05, and the G4's early fill (`early_fills.json`, pre_s 0) starts only at the score onset 213.0.
- **Stem.** In 40 ms frames from 212.5 the stem reads -45 -45 -46 -49 -51 -52 **-54** -49 -47 -45: a 9 dB hole over 0.25 s. The master dips -37 -> -40.
- **Fix.** `LEVEL_SHAPES["Clarinet 1"] += [[(212.64, 0.0), (212.72, 5.0), (213.04, 5.0), (213.12, 0.0)]]`.
- **Simulated.** The stem reads -45 -45 -43 -44 -46 -47 -49 -46 -46 -45: the hole is now 4-6 dB, and the master changes by 1 dB or less. The rest of the hole is the sample's crossfade.

**Oboe 1, 578 -> 579** (G4 -> E5, a ninth up, p dolce, -8.3 dB re master).
- **Cause.** The E5 arrives late: the Leg Slur MAX large-leap transition. The 578.94-578.97 envelope step (+7.0 -> +3.4) deepens the join.
- **Stem.** In 50 ms frames from 578.5: G4 -39..-41, join **-46**, E5 -43 -42 -43 -45 for its first 0.2 s, then -38 (the E5 reaches its level 0.2 s after the score onset). c27 is identical.
- **Fix.** `LEVEL_SHAPES["Oboe 1"] += [[(578.90, 0.0), (578.96, 4.0), (579.40, 4.0), (579.55, 0.0)]]`, ahead of critic B's c27 cut that starts at 579.2.
- **Simulated.** Join -43, E5 -39 -38 -39 -41 then -36. The master changes by 1 dB or less. The oboe's line itself is the gain.

**Pass.**
- Clarinet 1 stem dip at 213 at most 6 dB.
- Oboe 1 579: first 0.2 s within 3 dB of the 578 G4 body.
- No 30 ms peak more than 2 dB over either target's body.

## 4. Final chord (bar 181, qn 723.921): the celli re-bow fill row puts a notch on the re-bow (measured; stem only)

- **The fill row.** `rebow_fills.json` Violoncellos `723.921` has -4.46 / -5.58 / -5.20 / -3.73 dB at 0.00 / 0.04 / 0.08 / 0.12 s, on top of a re-bow that already dips. It was fitted before the c26 coda -2, the c28 Tempo I +1.5 and the release changes.
- **Stem.** In 60 ms frames: -52 -> -57 / **-61** / -58 -> -53. In the 100-300 Hz band: -55 -> -64 / **-69** / -65, a 10-14 dB hole of 0.2 s in the ppp C3.
- **Master.** The master's 100-300 Hz band dips 2-3 dB and then rises 4-6 dB (-50 -> -53 -> -46) in the next 0.1 s. Master power is flat, since the celli are -11 dB re master.
- **Fix.** Edit only this row:
  - Add +2.5 / +5.5 / +6.0 / +6.0 / +4.5 / +2.0 dB to its values at -0.04 / 0.00 / 0.04 / 0.08 / 0.12 / 0.16 s.
  - The new values are -0.45, +1.04, +0.42, +0.80, +0.77, +0.65.
  - Leave the rest of the row as it is.
- **Alternative.** Refit this one row with `tools/fit_rebows.py 28 build/parts.json` and keep only the 723.921 result.
- **Simulated on the stem.** -57/-61/-58 -> -52/-55/-54 (hole 9 -> 3 dB). Master power unchanged.
- **Pass.** Celli dip at 723.921 at most 4 dB in power and at most 6 dB in 100-300 Hz, and no new bump over 3 dB.

## 5. Doubled brass lines are still one player at +3 dB (patch; inferred; carried from c26-c28)

- `unison_dropped` is unchanged: Trumpet 2 21, Trombone 2 29, Horn 4 18.
- The two exposed a2 melodies are:
  - Trumpets 1+2 in the coda theme, bars 167-170 (20 shared notes).
  - Trombones 1+2 in the recapitulation theme, bars 131-134 (19 shared notes).
- Patches on disk:
  - `2 Trumpets/04 Legato/2TP Leg Slur MAX.oib`, or the 2TP KS Master with only Sus and Leg Slur MAX loaded.
  - `2 Trombones EXP/01 Long/2TB Sus MAX.oib` (no legato patch in that folder).
- This is the last cycle in which an a2 track can still be rendered and checked before c30. Do it only if REAPER's settled footprint after the c28 render (46 GB, 28 compressed) leaves room for a 34th instance. Otherwise leave it as is.
- No new measurement.

## Do not touch

- The c28 coda celli / cor anglais steps.
- The harp `VEL_SET` with the `_h28` steps.
- The letter-G hold.
- GENTLE_ACCENT with the current accent fits and bodies. The item 8 fronts are soft on every family.
- The legato leads and LEG_CAP settings: no new join holes outside findings 1 and 3.
- The re-bow times and every other `rebow_fills.json` row.
- The Stac RRx9 / RRx14 string staccato and the shortened-Sus wind staccato.
- The tenuto handling.
- The Vln II sul tasto EQ.
- The portamento at 225 / 685.
- The existing CA, Horn 1, celli and Oboe 1 shapes. Findings 1-3 add to them and do not replace them.
