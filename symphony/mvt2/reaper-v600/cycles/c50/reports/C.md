# Cycle 50, critic C: dynamics over time (review of the c49 render)

## Method

I measured the c49 master, its 36 stems and the delivered mp3 with my own numpy scripts. I did not use REAPER and changed no setting.

- Loudness per bar is the mean EBU R128 short-term loudness (S, LUFS) of the frames in the bar.
- Stem levels are RMS in dB with the power of the two channels summed, read in 50 ms frames. "Frames from qn x" are consecutive windows that start at x. A note "body" is the level from 0.08 s after the played onset to the played end.
- Controller and fader values come from `cycles/c49/rendered_build/` (parts.json, roles.json, score_config.py: the data as rendered). The live `build/` differs from it only on Flute 1 and the Cor anglais at qn 106.9-108.75 (the score change approved after the render); every number in this report is from the c49 audio and the data as rendered.
- I re-implemented the ride of `tools/deliver_master.py` and checked it against the real mp3 (rms error 0.19 dB on short-term loudness), then ran it with other settings.
- I simulated stem fixes by scaling the stem inside the master (the master equals the sum of the stems to -136 dB). This scales the dry track only, not its reverb send.
- c48 was measured the same way for comparison. Flute 1 (108-113), Horn 1 (31.5-35), Violins I and II (249.5-255.5), Violoncellos (243.5-249) and Violins II (192-204) are identical in c48 and c49 in every frame, so the shapes reported below come from the data, not from render variation.

Each judgement is marked measured (read from audio or data), simulated (from the two simulations above) or inferred.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 50 (its last row is cycle 47), so there was no page range to read. The `loop/MANUAL-GAPS.md` items that touch this lens:

| MANUAL-GAPS item (May 2021 HO manual, PDF page) | Where it applies | Does the render follow it |
|---|---|---|
| 1: brass and clarinet dynamics on CC1 (p.101) | Horn 1, bars 10-13 | In use since c30. Horn 1's CC1 moves only 65 to 67 across the printed crescendo of bar 11, by the c31 horn map (soft range on CC1 57-72). By design; see finding 2 |
| 5: Leg Slur Exp / Sus Exp rows for espr. and dolce wind solos (p.109) | Flute 1 bars 37-40, Cor anglais bars 41-44 | Never tried. The crescendos of these solos are flat or reversed on the current rows (finding 2). A patch change, not for c50 |
| 6: slower legato transitions on cantabile string lines (p.144, p.99) | Violoncellos bars 71-74 | Not tried. The crescendo of bars 72-73 peaks one beat early (finding 4) |
| 7: recorded Felt Cresc timpani rolls (p.123, p.125) | Timpani rolls | Not tried. No finding from this lens |
| 13: Marcato Sustain rows (p.91-92) | Bar 47 fp | Not tried. The string fp works with the c48 chain (see "Checked"); the open problem in bar 47 is the oboe (finding 3) |

## The two open points from c49

**1. The delivered LRA fell from 15.3 to 14.6 LU with the master LRA unchanged: traced (measured).** Master LRA 23.47 (c48) and 23.44 (c49); delivered 15.27 and 14.58. The delivered 95th percentile did not move; the delivered 10th percentile rose from -28.88 to -28.17 LUFS. Master bars that changed by more than 0.5 dB: bar 8 -0.8, bars 41-42 +0.5, bar 51 +0.8, bar 68 -1.0, bars 85-86 +1.2 and +1.4. Bars 85-86 are the cause: c49 (critic B #3) changed the Clarinet 1 role row `[280, 286, -2.5, 0.5]` to `[280, 286, 0.5, 0.5]` (+3.0 dB on the stem), and delivered bars 85-86 rose from -29.6 to -28.4 and from -28.0 to -26.6. In c48 these frames lay just under the delivered 10th percentile, so raising them raised the percentile. In the master they stay below the master's 10th percentile, so the master LRA did not move. This was an intended balance change, not a fault. LRA 14.6 and the span of 18.0 dB are inside the BRIEF item 6 targets (14-16 LU, 16-19 dB). The margin over the 14 LU floor is 0.6 LU; another change of that size in the soft bars would reach the floor (inferred). If the c50 delivery reads under 14.2 LU, run it with `DELIVER_KNEE_BELOW=7` (simulated on c49: LRA 15.1, span 18.5, no inversions).

**2. "The bar 73 subito keeps 12.1 of 15.9 dB": the step is in bar 64 and is a printed diminuendo (measured).** `cycles/c49/actor_scripts/item23.py` line 40 labels bars with `int(q // 3) + 1`, which is wrong from qn 108 on. The step it reported at qn 218.8 is bar 64 beat 3.8: the end of Trombone 1's last quotation note (qn 218, accent, printed decrescendo to p at 219.5). The stem falls from -22.3 dB (first 0.3 s) to -47.6 (last 0.3 s), CC11 114 to 49, CC1 108 to 45, over strings at -44 to -50 dB. The ride gain rises from +7.0 to +12.0 dB across qn 217.9-220 and removes 3.8 dB of the fall. Delivered bar 64 to bar 65 falls 11.8 dB (master 17.5). Nothing to fix; the item can be closed. The other steps of that list with correct bars: qn 28.3 is bar 10, 83.2 is bar 28, 150.2 is bar 47 (after the fp), 270.8 is the end of bar 81. If item23.py is reused, take the bar from the mapping in BRIEF "The music".

## The arc of the movement (measured)

Mean short-term loudness per bar, master / delivered mp3, LUFS:

| Bars | Printed | Master | Delivered |
|---|---|---|---|
| 1-6 | pp opening | -45.2, -41.2, -40.4, -41.4, -42.3, -42.1 | -28.0, -24.1, -23.6, -24.8, -26.2, -26.4 |
| 47, 48 | fp, then p | -34.6, -39.8 | -20.5, -25.6 |
| 53-57 | p cresc., mp (54), mf (56) | -34.2, -30.5, -28.9, -27.4, -26.2 | -22.3, -19.9, -19.6, -18.9, -18.6 |
| 58-60 | cresc., f (59), cresc. | -23.1, -22.3, -17.2 | -16.2, -16.3, -13.3 |
| 61-64 | ff Largamente, dim. | -13.7, -14.4, -20.0, -26.0 | -10.8, -10.9, -14.9, -18.9 |
| 65-66 | pp, niente | -43.5, -44.5 | -30.7, -30.0 |
| 77-82 | cresc., ff cadence (79), dim. to p | -25.9, -20.6, -18.9, -20.3, -24.8, -36.0 | -18.3, -14.2, -12.9, -13.9, -16.9, -24.1 |
| 83-92 | ppp (83-86), pp (87-89), morendo (91) | -44.8, -46.7, -45.0, -43.4, -40.6, -41.0, -39.8, -42.9, -47.7, -52.9 | -30.1, -30.8, -28.4, -26.6, -23.9, -24.3, -22.8, -25.8, -30.5, -35.6 |

- The climax is the loudest passage. Bar 61 is 5.2 dB over bar 79 in the master and 2.1 dB over it in the mp3 (finding 5).
- The printed levels are in the right order at bar scale, with one exception: bar 59 (f) is level with bar 58 (finding 1).
- The ppp bars of the coda are 3-5 dB under its pp bars in both files.
- The mp3's pp coda bar 89 (-22.8) is 3.9 dB under the mf of bar 56 (-18.9); in the master the distance is 12.4 dB. This is the cost of the ride and is inside the BRIEF targets.

## Findings

### 1. Bars 58-60 (qn 192-204), Violins I and II: the f of bar 59 is no louder than the end of the crescendo before it, because the level fader falls 6 dB between qn 195 and 200.2

**Where.** Violins I and II in octaves. Printed in both parts: crescendo to qn 195, a short decrescendo 195-195.5 and a breath, f at 196, crescendo from 200, ff at 204.

**What is wrong (measured).** Level per quarter note, frames from qn 193:

| | bar 58 beats 2-4 | bar 59 (f) | bar 60 (cresc.) | 204 (ff) |
|---|---|---|---|---|
| Violins I | -30.2, -30.1, -30.3 | -29.1, -32.1, -31.3, -30.6 | -30.2, -30.0, -27.6, -24.6 | -22.5 |
| Violins II | -30.8, -30.5, -31.7 | -31.7, -34.9, -32.6, -33.0 | -30.6, -29.6, -26.9, -24.4 | -24.6 |

After its first beat, the f bar is 0.4-1.9 dB (Violins I) and 1.6-3.9 dB (Violins II) under the mean of the three beats before it (Violins II's first beat is also 0.7 dB under), and the whole rise from f to ff happens in the last two beats of bar 60. In the master, bar 58 to bar 59 rises 0.8 dB (-23.1 to -22.3); in the mp3 it is level (-16.2 to -16.3). The next two bars rise 5.1 and 3.5 dB.

**Cause (measured in the data).** The controllers follow the print: CC11 88 at 194.8, 82 at 195.5, 88 at 196.0, then 88 to 114 over 200-204. The fader lane (`vol_db`) does not. Violins I: 9.3 dB (195), 7.5 (196.0), 6.0 (196.5), 5.8 (199.6), 3.1 (200.2), 5.6 (203.5). Violins II: 8.8, 7.0, 5.5, 5.4, 3.1, 5.6. There are two falls:

- 3.2 dB over 195.5-196.5. The arrival gain of the hairpin 188-195 (`hpgain` `[188, 195, 3.0]`) is released over `HP_REL` = 1.0 qn, because the printed half-beat decrescendo at 195 blocks the chain test in `tools/score_to_parts.py` (lines 4074-4091). `hp_chained` is `[261.0]` on both violin tracks; Violas, Clarinets, Bass clarinet, Horn 1, Violoncellos, Double basses and Bassoon 2 have 200.0 chained.
- 2.7 dB over 199.6-200.2. The shape at line 1008 of `build/score_config.py` ends there (`(199.6, 2.0), (200.2, 0.0)`), and the role rows `[200, 214, -1, 1]` (Violins I) and `[200, 214, -0.5, 1]` (Violins II) begin.

**Fix.** In `build/score_config.py`, after line 1008:

```python
for _tr in ("Violins I", "Violins II"):
    LEVEL_SHAPES[_tr] = LEVEL_SHAPES.get(_tr, []) + [[(195.5, 0.0), (196.5, 3.0), (201.0, 3.0), (204.0, 0.0)]]
```

It cancels the first fall exactly, so there is no new fader movement at the f, holds through bar 59, and tapers while the hairpin gain of 200-204 comes in.

**Expected (simulated on the c49 stems).** Violins I from qn 193: -30.2, -30.1, -29.9 | -26.4, -29.1, -28.3, -27.6 | -27.2, -27.5, -26.2, -24.2 | -22.5. Violins II: -30.8, -30.5, -31.2 | -29.0, -31.9, -29.6, -30.0 | -27.6, -27.2, -25.5, -23.9 | -24.6. Master short-term loudness: bar 59 from -22.3 to -21.2, so bar 58 to 59 rises 1.7 dB instead of 0.8; delivered bar 59 from -16.3 to -15.5, so +0.7 dB instead of 0.0. Bar 61 does not change. Delivered LRA and span do not change (14.59 LU, 18.25 dB in the simulation). No inversions. (The loudness figures were simulated with the taper starting at 200 instead of 201; the master RMS of bars 59 and 60 differs by 0.0 and 0.1 dB between the two.)

Adding the Violoncellos (`[(196.5, 0), (197.5, 2.5), (200, 2.5), (202, 0)]`) gives 0.2 dB more in bar 59, and Flute 1 and Oboe 1 a further 0.1 dB. I do not ask for them.

**Acceptance on the c50 render.** Violins I at 197-199 at least 1.5 dB over 193-195. Violins II at 197-199 at least level with 193-195; if not, use 4.0 instead of 3.0 on Violins II (expected -30.9, -28.6, -29.0). Master bar 59 at least 1.5 dB over bar 58. The note at 203.84 and bar 61 unchanged within 0.3 dB. Tolerance: Violins I at 197-198 read 1.2 dB lower in c49 than in c48 with identical part data, trims and mix settings (cause not traced), so allow about 1 dB between renders.

**Protected items.** The c38 list (179.5-196) is not edited; the new list overlaps its last half beat as a separate list (effect on bar 58: +0.2 dB in the master). The levels at 204 (c34, c39) do not change.

**Code alternative, not for this cycle.** In the chain test, do not let a decrescendo shorter than 1 qn block the chain when a printed mark at or above the arrival level follows it before the next hairpin.

Inferred: the build from p (bar 53, -34.2) to ff (bar 61, -13.7) puts 8.6 dB of its 20.5 dB into the last printed step. The research default (a build enters low and peaks at the end) supports a late rise, so I ask only for the f arrival, not for an even slope.

### 2. Solo crescendos that are reversed or flat: Horn 1 bar 11, Cor anglais bars 41-42 (Flute 1 bar 37 is covered by B #3)

These notes are on legato rows, so the c50 rebuild will change their levels. Order of work: the rebuild, then B's refit to the c49 levels (B #1), then measure the thresholds below on the first render and apply a shape only where a threshold fails. The shapes are offsets against the c49 levels.

**Horn 1, bar 11 (qn 32-34), the first long note of the solo's second phrase (measured).** Printed: crescendo 32-34, decrescendo 34-39. Notes: C4 at 31.41, F4 at 31.91 (2.01 qn, the crescendo note), B flat 4 at 33.88, A flat 4 at 34.92. Frames of 0.25 qn from 31.5: -40.7, -36.2, -38.5 (32.0), -34.7, -31.9 (32.5), -32.9, -37.0 (33.0), -38.1, -37.2, -36.6, -37.6 (34.0), -34.6, -32.2 (34.5). The crescendo note reaches -31.9 0.6 qn after its onset and then lies 5-6 dB lower for its second half, under a printed crescendo. The phrase has two peaks with a 5 dB trough between them where the print has one rise. The controllers do not do this: fader 4.5 (31.94), 3.6 (32.5), 4.5 (33.0), 5.0 (33.75), 7.3 (33.91); CC11 47 to 57; CC1 65 to 67. The F4 pitch trim (`pitch_trims.json` Horn 1 `"65": {"early": 1, "body": -5}`) is not applied at this onset, because 32.0 is in its `_skip_onsets`. That the early peak is the legato transition layer of the F4 joined from C4 is inferred.

Fix, only if the peak is still there after the rebuild (level at 32.4-32.8 more than 3 dB over 33.0-33.8):

```python
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(32.1, 0.0), (32.3, -2.5), (32.5, -4.5), (32.75, -3.5), (32.95, 0.0), (33.25, 3.0), (34.1, 3.0), (34.4, 0.0)]]
```

Expected frames from 32.0 (the measured frames plus the shape; inferred): -39.1, -37.9, -35.9, -34.3, -35.3, -35.1, -34.2, -33.6, then -35.1 (34.0), -34.2, -32.2 (34.5). That is a 5.5 dB rise across the printed crescendo into the crest note, whose peak does not change. Acceptance: no frame in 32.25-33.75 more than 1.5 dB over the frame at 33.75-34.0, and 33.5-33.9 at least 2 dB over 32.0-32.25.

**Cor anglais, bars 41-42 (qn 124-128), the solo's first crescendo (measured).** Printed: solo dolce cantabile at 124, crescendo 124-128, decrescendo 131-136; `hpgain` `[124, 128, 3.0]`. Frames of 0.5 qn from 124.25: -38.8, -39.1, -39.1, -38.8, -39.1, -38.9, -40.6 (127.25), -38.8 (127.75), -37.0 (128.25), -38.5, -37.4, -39.7 (129.75), -39.2, -39.9, -41.7 (131.25), -43.9. The level stays within 0.3 dB for three of the four beats of the crescendo and the arrival is 1.8 dB over the start. The level steps down 2.3 dB at 129.75 (A flat 4 to F sharp 4), 1.25 qn before the printed decrescendo. In c48 the crescendo was reversed (a dip of 2-5 dB at 126-127.5); c49's +3 pitch trims on F4 and F sharp 4 made it level. The controllers rise (CC11 54 to 66, CC1 66 to 110), and the fader rises to 11.2 dB at 126 and is back at 4.4-5.4 dB at 127.4-128. The role row `[127.5, 133.5, -3.5, 2.5]` (c19) cuts 3.5 dB from half a beat before the top of the crescendo; that it accounts for the flat arrival is inferred.

Fix (B lists that role row and the c49 F4 / F sharp 4 levels under "Do not touch", so the row stays and this is a separate entry):

```python
LEVEL_SHAPES["Cor anglais"] = LEVEL_SHAPES.get("Cor anglais", []) + [[(124.9, 0.0), (127.9, 3.0), (130.9, 3.0), (131.9, 0.0)]]
```

Expected frames from 124.25 (inferred): -38.8, -39.0, -38.5, -37.7, -37.5, -36.8, -38.0, -35.8, -34.0, -35.5, -34.4, -36.7, -36.2, -37.3, -40.5, -43.8. The entry raises B's target levels at 126 and 127.5 by 1.1 and 2.6 dB on purpose; B measured this solo with the smallest margin of all solos (+0.1 dB over the other stems in bars 41-44), so the rise does not cost balance. Acceptance: 127.75-128.75 at least 3 dB over 124.25-125.25 (expected 4.0; c49: 1.0). The shape holds to 130.9 so that the level does not fall further before the printed decrescendo, but it does not change the 2.3 dB step down at 129.75; I ask for no change there, because B sets the c49 F sharp 4 level as a target. The dip at 127.25 is the join that A #2 treats.

**Flute 1, bar 37 (qn 108-112).** My note bodies agree with B #3 within 1 dB: F5 at 108 -36.8, 110 -37.3, 110.5 -36.2, E flat 5 at 111 (the note at the top of the printed crescendo) -40.0, 112 -41.6, 113 -42.9. The arrival is 3.2 dB under the first note (reversed). B's note trims are the fix; do not add a shape as well. Two additions from this lens:

- After B's trims the crescendo is a plateau (B predicts 108 at -36.6 and 111 at -36.9). In the c50 build the F5 at 108 becomes a legato target after the new C5 pickup. On this patch the same F5 measured 2.5-3 dB weaker as a legato target than as a slur's first note at equal fader and CC11 (110.47 against 107.96; one pair, so the general rule is inferred). If the 108 note comes out 2-3 dB lower in c50, B's trims then give a real crescendo. Do not trim the 108 note back to its c49 level unless B's margin in bar 37 needs it.
- Acceptance from this lens: the body of the note at 111 at least as loud as the notes at 110 and 110.5 and at least 1.5 dB over the note at 108 as rendered in c50. If it fails, raise B's `"111"` trim from 2.5 to 4.

### 3. Bar 47 (qn 148), Oboe 1: the mf goal note of the oboe's phrase reaches its level about 0.3 s after the fp and swells for a second, so the printed "mf >" plays as "<" and covers the fp's drop

**Where.** Oboe 1, the last note of its phrase (C sharp 5, 3 qn, printed mf with a decrescendo 148-151), re-tongued on the same pitch after the crescendo note 146-148. Violins II, Violas and Double basses have the fp on the same downbeat; the cor anglais solo enters at 151.

**What is wrong (measured).** Oboe 1 in 50 ms frames relative to the downbeat (170.177 s): -0.15 s -35.6; -0.05 s -40.0; 0.00 -43.5; +0.05 -42.0; +0.10 -42.3; +0.15 -41.9; +0.20 -39.8; +0.25 -37.9; +0.30 -36.3; +0.50 -36.0; +0.70 -33.1; +0.90 -33.2; +1.10 -34.0; +1.50 -34.6; +2.00 -37.2. The note regains the level of the crescendo note's end 0.3 s after the downbeat and reaches its maximum 0.7-0.9 s after it, 8.8 dB above its level at +0.15 s. The string stems peak at 0.0 to +0.2 s and fall 8-11 dB within 0.5 s. Frames of 0.25 qn from 148.0, Oboe 1 / master / master without the oboe: -41.8 / -28.1 / -28.2; -37.1 / -31.6 / -33.1; -34.3 / -32.6 / -37.7; -33.6 / -32.7 / -39.7; -33.6 / -31.9 / -36.8; -34.1 / -32.3 / -37.0; -35.9 / -34.8 / -41.3 (149.5). The master stays within 4.6 dB of the fp peak for 1.25 qn, while the rest of the orchestra is 5-11.5 dB down: the oboe's late swell fills the drop of the fp.

**Cause (measured in the data; the last step inferred).** The onset is on the grid with no lead (`rep_retongued [148.0]`), while the oboe's other onsets in this phrase are 0.12-0.14 qn early. The fader is already at its maximum at 148.0 (12.6 dB, including the role row `[148.0, 151.0, 3.5, 2.0]` and the c42 step) and falls from there; CC11 72 to 58; CC1 72 to 62. So the rise after the downbeat is the sample's own attack (inferred). The note is a re-tongued sustain, not a legato target, so the legato rebuild does not change it: this fix can be made in c50 independently.

**Fix.** In `build/score_config.py`:

```python
REATTACK_LEAD_AT["Oboe 1"][148.0] = 0.15
LEVEL_SHAPES["Oboe 1"] = LEVEL_SHAPES["Oboe 1"] + [[(148.3, 0.0), (148.7, -2.0), (149.3, -2.0), (149.9, 0.0)]]
```

An explicit `REATTACK_LEAD_AT` entry is accepted for a same-pitch re-attack (the same-pitch exclusion in `tools/score_to_parts.py` line 3528 applies only to the family-wide `REATTACK_LEAD_S`); check that `reattack_leads` of Oboe 1 in parts.json lists 148.0. The value follows the c35 rule (measured body - 6 dB at +0.20 s, minus about 0.05 s). 0.15 s is 0.12 qn here, so the moved onset is near 147.88. Move the first two points of the c42 onset shape at line 1015 (`(147.97, 0.0), (148.0, 4.2)`) to 0.03 qn before the moved onset and to the moved onset, so that the step stays in the re-tongue gap; its size (4.2 dB, which B protects) stays.

**Expected (simulated by shifting the c49 stem).** Relative to the downbeat: -0.15 s -43.5; -0.05 -42.3; 0.00 -41.9; +0.05 -39.8; +0.10 -37.9; +0.15 -36.3; +0.30 -37.2; +0.50 -35.1; +0.70 -36.6; +1.10 -35.8; +2.00 -37.3. The re-tongue gap falls before the downbeat, the note is within 1.3 dB of its maximum by +0.15 s, and it holds within 2.6 dB for about a second before the printed fall. With the lead alone the note still rises 2.5 dB after +0.15 s.

**Acceptance.** Oboe 1 at +0.15 s within 2 dB of the note's maximum (c49: 8.8 dB under). No frame after 148.4 more than 2 dB over the mean of +0.15 to +0.30 s. The string stems and the c48 fp chain unchanged. The timing part touches A's lens (S2).

### 4. Bars 72-75: the Violoncellos' crescendo peaks one beat early, and Violins II stay flat against Violins I in the unison crescendo of bars 74-75

Both lines may change with the rebuild; measure first and apply the shape if the threshold fails.

**Violins I and II, bars 74-75 (qn 250-255), unison (measured).** Both parts have the same print (mp at 249, crescendo 250-254, decrescendo from 254), the same `hpgain` (`[250, 254, 2.0]`, `[254, 255, -2.0]`), the same velocities and the same `dyn_curve` (58 to 80). Note bodies, Violins I: 249.85 -38.7; 251.35 -39.1; 251.85 -37.9; 253.85 (B flat 5, the top) -33.9; 254.85 -40.4. Violins II: 249.78 -39.9; 251.29 -39.1; 251.78 -40.5; 253.78 (the top) -40.6; 254.79 -38.9. Violins I rise 4.8 dB to the top; Violins II are level and their top note is under the notes on both sides of it (reversed). The two parts are 6.7 dB apart at the top of a unison line, against the default that doublings share one curve (EW-TEMPLATE-PLAN). In the data the two tracks differ in CC1 (Violins I 78 to 105 over 252-254; Violins II 62 to 80) and in the join handling (`leg_leads` `[]` against `[252.0, 254.0]`; `bcsoft` 0 against 2), and the Violins II fader falls 3.5 dB into the top note (5.3 dB at 253.25, 1.8 at 253.78), because the c42 shape at line 1011 ends at that onset.

Fix: extend the c42 shape of Violins II through the top note. Replace the list at line 1011 by `[(252.25, 0.0), (252.5, 4.0), (254.5, 4.0), (254.79, 0.0)]`. Expected top note about -36.6 (inferred): 3.9 dB over the note before it, 2.3 dB over the note after it and 2.7 dB under Violins I. Acceptance: Violins II's note at 253.78 at least 2 dB over its note at 251.78 and within 3 dB of Violins I's top note. Why the two tracks get different CC1 lanes and join handling for one unison line is not traced (Violins II's `bcsoft` 2 and its state before the "ord." at 250 are the candidates); the actor should check it when rebuilding these tracks.

**Violoncellos, bars 72-73 (qn 243.8-249) (measured).** Printed: crescendo 244-246, decrescendo 246-249; `hpgain` `[244, 246, 2.5]`. Notes: A flat 3 at 243.81, C4 at 245.68 (2.18 qn, the note at the printed peak). Frames of 0.5 qn from 243.5: -43.2, -42.3, -39.2, -36.4 (245.0), -42.0, -41.3 (246.0). Bodies: -39.1 and -41.9. The line peaks at 245.0-245.5 and the note at the printed peak is 5.5 dB under that. Fader: -4.2 dB (245.0), -5.6 (245.5), 0.9 (245.9), 1.2 (246.17), -1.6 (246.39), -2.0 (247.25): the role row `[245.5, 250, -2]` begins at the printed peak. CC1 75 to 94 at 244.75, 85 at 246.0.

Fix:

```python
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(244.6, 0.0), (245.0, -1.5), (245.55, -1.5), (245.75, 4.0), (246.6, 4.0), (247.8, 0.0)]]
```

Expected (inferred): -37.9 at 245.0-245.5 and -37.3 at 246.0-246.5. Acceptance: the frame at 246.0-246.5 within 1 dB of the loudest frame of 244-246, and at least 3 dB over 244.0-244.5. Related: MANUAL-GAPS 6 (p.144, p.99), not for c50.

### 5. Delivery: the ride leaves the climax 2.1 dB over the ff cadence (5.2 dB in the master) and keeps 1.3 of the 4.3 dB rise of bars 54-57; one setting can be refitted, the rest cannot be recovered inside the BRIEF targets

**What is measured.** Bar 61 against bar 79: 5.2 dB in the master, 2.1 dB in the mp3 (by maximum short-term loudness: 4.7 and 1.9 dB). The ride gain relative to the gain of the loud passages is -4.2 dB in bar 61, -3.7 in bar 62 and -1.1 in bar 79: the top ride (`TOP_ABOVE, TOP_RATIO = -3.0, 2.5`, line 23 of `tools/deliver_master.py`) takes 3.1 dB more from the climax than from the cadence. Bars 53-61 rise 20.5 dB in the master and 11.5 dB in the mp3; bars 54-57 rise 4.3 and 1.3 dB. Against the stored slow-movement references (the definitions of `tools/motion.py`): 1 s / 20 s motion 3.30 in the mp3 and 4.24 in the master, against 3.92 (Brahms 4/ii) and 4.56 (Brahms 1/ii); the 90th percentile of 4 s level changes is 6.31 dB in the mp3 and 7.03 in the master, against 6.29 and 8.55. The mp3 moves 16-28 % less than the two recordings on the first measure and equals Brahms 4/ii on the second.

**What other ride settings give (simulated on the c49 master).**

| Setting | LRA | p10-to-max span | Bars 53-61 | Bars 54-57 | Bar 61 over bar 79 | Limiter |
|---|---|---|---|---|---|---|
| Real mp3 | 14.58 | 18.10 | 11.5 | 1.3 | 2.1 | 1.9 dB |
| Simulation of the current settings | 14.59 | 18.26 | 11.6 | 1.4 | 2.1 | reference |
| `TOP_RATIO` 2.0 | 14.76 | 18.81 | 12.3 | 1.4 | 2.6 | +0.40 dB |
| `TOP_RATIO` 1.8 | 14.86 | 19.11 | 12.7 | 1.4 | 2.9 | +0.62 dB |
| `RATIO` 2.4, `KNEE_BELOW` 7 | 15.11 | 18.62 | 12.2 | 1.7 | 2.1 | 0 |
| `RATIO` 2.4, `KNEE_BELOW` 8 | 15.67 | 19.18 | 12.8 | 2.1 | 2.1 | 0 |
| `RATIO` 3.0, `KNEE_BELOW` 9 | 15.39 | 18.90 | 12.9 | 2.3 | 2.1 | 0 |
| `LIFT_SMOOTH_S` 8 | 14.96 | 18.73 | 11.9 | 1.7 | 2.1 | +0.01 dB |
| `TOP_RATIO` 2.0 with `RATIO` 2.7, `KNEE_BELOW` 8 | 15.35 | 19.23 | 13.2 | 1.9 | 2.6 | +0.73 dB |

No row has an inversion. The simulation reads the span about 0.15 dB high. The full grid (17 settings) is in the scratch folder.

**Fix (optional, one number).** `TOP_RATIO` 2.5 to 2.0 at line 23 of `tools/deliver_master.py`. It is the only single change that raises the climax over the cadence (2.1 to 2.6 dB) and stays inside both targets (LRA 14.8, span about 18.7). Cost: about 0.4 dB more limiting on the loudest peak at qn 204.2 (1.9 to about 2.3 dB, inferred from the pre-limiter peak; the BRIEF limit is about 3 dB), and 33 instead of 13 blocks of 10 ms over -1.5 dBFS. `TOP_RATIO` 1.8 and every combination exceed the 19 dB span. No setting inside the targets lifts bars 54-57 above about 2.3 dB or changes bars 58-59; that passage has to be fixed in the master (finding 1). If the actor keeps changes small this cycle, this item can wait; nothing in it is a fault of c49.

## Noted, no fix asked this cycle (measured)

- Bars 64-65, strings under Trombone 1's last note: Violins II's printed p > pp is level (-47.4 at 216, -49.5, -48.7, -48.7 at 219.8); the Violas have one 0.25 qn frame at -62.3 near 218.0; the Violoncellos' tremolo at 216 (-40.4) is 7 dB over Violins II and Violas at the same printed p. Low audibility until about qn 219.2.
- Clarinet 1, qn 176-182 (pp cresc.): the 4 qn note at 177.93 rises 2.0 dB and the next note enters at -43.8.
- Flute 1 and Oboe 1, bars 57-58: the printed p < f is level at -40 to -45 dB and arrives as a step of 7-9 dB at 196 (Flute 1 has the role cut `[191.5, 196, -3]`). Masked by Violins I.
- Violoncellos, the note at 198.76 is 6 dB under its neighbours (-35.2). Re-check after the rebuild.
- Horn 1 is the loudest stem in bar 59 (-28.8 and -28.4 per half bar, two-channel mean): B's lens.
- Violoncellos, the decrescendo at qn 74-77 (bars 25-26) read flat (-0.1 dB) in my hairpin survey (227 hairpins; median crescendo +4.6 dB, median decrescendo -6.2 dB); not examined further.
- The mp3 ends 1.4 s after the score end; its last half second falls from -49.9 to -74.4 dB. The c47/c48 post-END fade is protected and I ask for no change.

## Checked, no finding (measured)

- Loop pulsing (BRIEF item 8). No string note in c49 is longer than 4.8 s. Folding band levels and the spectral centroid at 3.95 s against control periods of 2.7, 3.3 and 4.6 s: master qn 0-18, 100-300 Hz 2.8 dB (largest control 3.9); master 219-226 4.8 dB (6.3); master 274-286 3.6 dB (4.2); final chord 292-304 3.9 dB (5.8), autocorrelation -0.28 (c25, before the re-bows: 4.8 dB and 0.58). No stem of the final chord exceeds its control by more than 1.3 dB (Violins I 4.5 against 3.2). The long wind notes (Clarinet 2 18.7 s at 292, Horn 4 12.7 s at 6, Bassoon 2 11.7 s at 90) show no period; Horn 4's note drifts between -47.4 and -54.6 dB without a pattern.
- The niente of bar 66. Master in 0.5 s steps from qn 223.05: -42.1, -43.4, -45.3, -46.1, -47.2, -49.8, -50.6; the mp3 falls 1:1 (-28.2 to -36.2). Violins II, Violas and Violoncellos fall 20-26 dB to -70 or lower by 225.95; the Double basses hold their printed pp pedal at -50 to -52; Horn 1 enters at 225.9 at -40.1.
- The string fp of bar 47. Double basses -33.5 at the downbeat, -42.3 at 148.3-148.8, -51.8 at 149.5-150.5; Violas -33.9, -44.2, -46.7; Violins II -39.7, -47.8, -51.8. The c48 chain works.
- The morendo and the final chord. Bar 91 falls 7 dB (-44.6 to -51.6); bar 92 holds -51.4 within 0.3 dB for about 4.5 s, with no dip or re-swell at the re-bows; then the fade.
- The ff cadence, bars 78-80: -20.6, -18.9, -20.3 in the master. Its loudest bar is 5.2 dB under bar 61 (4.7 dB by maximum short-term loudness), so the climax stays the loudest passage.
- The coda levels: see the arc table.

Scripts and cached data are in `/private/tmp/claude-501/mockup-loop/mvt2-c50-C/` (about 170 MB; notes in `FINDINGS.md`). I left the folder in place, because the launcher's instruction for this run was not to delete files.

**Do not touch:** the c31/c35 lanes of bar 63 and Trombone 1's shape at 217.5-219.5 (the step at 218.8 is the printed diminuendo); the c34/c39 holds and levels of bars 61-62 and the level at 204; the c38 string shape of bars 54-57 (179.5-196; the new violin entry is a separate list); the c30/c42 niente lanes of bar 66 and the Double basses' pedal in bars 65-67; the re-bow design of the long string notes and the c49 pedal fills; the c46 tempo map and caesuras; the c47/c48 post-END fade; the c48 string fp chain at 148 and the size of Oboe 1's 4.2 dB step there; the cor anglais role row `[127.5, 133.5, -3.5, 2.5]` and c49's F4 / F sharp 4 pitch trims; the Clarinet 1 role row `[280, 286, 0.5, 0.5]` (it is the cause of the LRA change and it is correct); the coda's ppp and pp levels; and in `tools/deliver_master.py` `RATIO` 2.4, `KNEE_BELOW` 6, `LIFT_SMOOTH_S` 5, `MOM_CAP_ABOVE` 3 and `CAP_DB` 10, unless the c50 delivery reads under 14.2 LU.
