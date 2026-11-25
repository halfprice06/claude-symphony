# Cycle 24, critic A: articulation and phrasing (on the c23 render)

Material: `cycles/c23/render` stems and `cycles/c23/build_render/parts.json` (the data as rendered), `cycles/c23/records/`, `metrics/attacks.txt`. Patch files were read with `mockup-kit/opus/opus_state.py` `load_oib` (read only).

Method:
- Levels are the mean of the two channels' powers in 5 ms frames, on the parts.json tempo map.
- Separation is measured as in c21-c23: the lower of the two notes' 10 ms peaks within 0.11 s of each moved note-on, less the lowest frame between the peaks.
- Celli legato timing comes from `tools/pcx.py` (run read only, JSON to scratch).

"Measured" means a number from the render, from parts.json or from a patch file. "Inferred" means reasoned from those numbers.

## Manual notes

`MANUAL-READING.md` has no row for c24 ("cycles after c20 pick their own pages"). I chose group A1's shorts and read printed pages 91-94 of the May 2021 HO manual in full (strings "Short" folder: pizzicato, Bartók, ricochet, col legno, marcato, spiccato, staccato, Shorts MOD SPEED, repetitions). I also read `MANUAL-GAPS.md`.

| source (page) | what it says | where it applies here | does the render follow it |
|---|---|---|---|
| p.92 | Spiccato: very short notes made by bouncing the bow. The Spiccato patch has 9 sample sets in rotation | Violins I's leggiero theme eighths (finding 1) | partly. Violins I plays 4 of its 51 eighth pairs on "Spiccato RRx9" and 37 on "Staccatissimo RRx9". The patch read agrees with the manual: all 9 Spiccato groups carry a RoundRobin index (0-8), with a 318 ms release |
| p.93 | Staccatissimo is like Staccato with even shorter notes. All staccato patches rotate 9-16 sample sets. Staccato On Bow ends each note with the bow stopping on the string | Violins I's short rows (findings 1, 2) | the patch does not match the manual. "Staccatissimo RRx9" rotates only 8 groups (RoundRobin indices 0-7). Its 9th group, "V1 Stac rrx9", has **no start mode**, a 721 ms attack, sustain 0.001 and a 1,000 ms release. "Stac RRx14" has the same kind of group ("V1 Stac rrx16"). "Stac On Bow RRx9" has one too ("V1 stac rrx9": 733 ms attack, **sustain 1.0**, 1,000 ms release) |
| p.93 | Repetitions: one note bowed about a dozen times, with bow changes. It is not round robin and it has release trails | the repeated eighths (S1) | not suitable. The theme's repeats are pairs of two eighths, not runs. Its fixed internal rhythm would not follow quarter 264 (inferred). Keep the current route |
| p.91 | Pizzicato: round robin with 2 or 4 sample sets per note | celli / basses pizz. | followed ("Pizzicato RRx4"). No pizz. faults found this cycle |
| `MANUAL-GAPS.md` #3, #5 | Spiccato for the leggiero theme; woodwind staccato rows | finding 1 | #3 is still open. Finding 1 measures where it is needed |

## Findings, ranked by what a listener would hear

### 1. Violins I's staccato eighth pairs blur only at D5, D sharp 5 and F sharp 5, on every row and at every velocity. Re-route those pitches; do not re-test a global cap.

Where: Violins I, same-pitch eighth pairs on D5 (74), D sharp 5 (75) and F sharp 5 (78):
- the counterstatement, bars 35-43 (qn 103, 109, 115, 121, 127);
- bars 19-22 (qn 55, 64), bar 27 (79), bars 259-267 (775, 784, 799), bar 273 (817), bar 275 (823);
- the tuttis (331, 340, 355, 931, 940, 955) and the coda (988).

These are 24 of the 51 pairs. Violins II and violas are fine.

Evidence (measured, c23):

| pitch | pairs | separation, median dB |
|---|---|---|
| B4 (71) | 20 | 5.8 |
| E5 (76) | 3 | 5.4 |
| B5 (83) | 6 | 6.4 |
| D5 (74) | 5 | **1.0** |
| D sharp 5 (75) | 12 | **2.3** |
| F sharp 5 (78) | 3 | **0.2** |

- By row: "Staccatissimo RRx9" 4.5, "Stac RRx14" 4.9, "Spiccato RRx9" 4.6. Every row fails at these pitches: "Stac RRx14" on D sharp 5 at 340 / 940 gives 0.1 / 0.6.
- By velocity it is flat: D5 at velocity 57, 59, 75 and 87 gives 0.8, 1.0, 2.0 and 0.0. So the velocity layer is not the cause.
- Same pitches on the other sections: Violins II's D5 / D sharp 5 / F sharp 5 pairs separate by 7.2 / 6.6 / 7.0 dB.
- Envelope at qn 109 (D5 pair, velocity 59 / 61):
  - the first D5 rises 40 ms after its note-on to -45 dB and then stays flat at -44 for 170 ms;
  - the second D5 starts 0.114 s after the first and adds about 1 dB (-44 -> -42 at 26.24 s);
  - nothing dips between the two notes.
- The B4 pair at qn 73, for comparison: peak -39, dip to -47, second peak -42.
- What a listener hears (inferred): in the counterstatement (Dan's "lasting too long" figure family) the D5 / D sharp 5 repeats sound as one note of a quarter's length.
- Why not a global cap: c21 and c23 found that the short-row cap cuts peaks. c23's `STAC_MIN_SOUND_S` 0.10 plus a 150 ms cap lost 5-20 dB on the 60 ms peaks. B4 / E5 / B5 already separate at 5.4-6.4 dB without any cap, so a fix on every pitch would put the working pitches at risk.

Fix: a per-pitch route on Violins I, range-tested.
- Add a generic `STAC_ROW_BY_PITCH` {track: [(lo, hi, row)]} in `tools/score_to_parts.py`, beside the `ART_SPANS` logic, applied to short-row notes only. Default empty.
- Test (a), Spiccato:
  - scherzo value: `{"Violins I": [(74, 78, "Spiccato RRx9")]}`;
  - manual p.92: the bounced stroke is what players use for leggiero eighths at this speed;
  - the row has 9 RoundRobin groups and no odd group, and a 318 ms release instead of 524;
  - it is already loaded on Violins I, so the set of rows does not change and there is no memory cost.
- Test (b), Stac On Bow:
  - "Stac On Bow RRx9" on the same keys: 16 ms attack, 319 ms release, three velocity layers (1-59 / 60-114 / 115-127);
  - it needs a row load. Apply finding 2 to its odd group first: that group has sustain 1.0 and would swell under longer notes.
- Range tests: 96-132 (counterstatement) and 326-358 (tutti), each against a control from the same start.
- Acceptance, at the three pitches:
  - separation median 4.5 dB or more;
  - 60 ms peaks within 1.5 dB of c23;
  - B4 / E5 / B5 pairs unchanged, since they stay on their rows;
  - bar 23 figure no worse than c23.
- Then rebalance the moved notes with `region_gain_db` row_dyn_db on "Spiccato RRx9" (Opus state), not with volume rows.

### 2. Every Violins I short row carries an extra round-robin group with no start mode and a 1 s release. It probably sounds under every note, so Violins I's staccatos ring 0.6 s longer than the other sections'. Cap only that group: this removes ring without touching the peaks.

Where: Violins I, all staccatos (277 notes on "Staccatissimo RRx9", "Stac RRx14" and "Spiccato RRx9"). It is worst on the isolated staccato quarters before rests: bars 28, 32, 56, 132, 268, 276, 288, 320 (qn 81, 95, 165, 393, 801, 827, 861, 957).

Evidence:
- Patch (measured):
  - "Staccatissimo RRx9": groups "V1 Stac rrx1-8" carry RoundRobin indices 0-7; "V1 Stac rrx9" has no startModes, attack 721 ms, decay 1,000, sustain 0.001, release 1,000.
  - "Stac RRx14": the same kind of group, "V1 Stac rrx16".
  - "Stac On Bow RRx9": "V1 stac rrx9", attack 733 ms, sustain **1.0**, release 1,000.
  - The 2nd Violins and Violas KS Masters have the same kind of group in each short row ("V2 Stac rrx9", "Va stac rrx9", "Va Stac rrx16").
- Tails of isolated staccato quarters (measured; dB under the note's peak at +0.2 / 0.5 / 0.8 s after the peak):

  | track | dB at +0.2 / 0.5 / 0.8 s |
  |---|---|
  | Violins I, uncapped (8 notes) | -12..-23 / -39..-51 / -59..-73 |
  | Violins II "Stac RRx9", c20 150 ms any_dyn cap (which also caps the odd group) | -35..-88 / digital silence (-81..-93) by 0.2-0.3 s where no other note sounds |
  | violas, same | same |

- The primary groups' 524 ms release ends about 0.48 s after the peak. Violins I still has signal at 0.8 s, and only a group with a 1 s release can produce that. That points to the odd group sounding on every note (inferred: in Opus a group with no start condition is not limited to one round-robin turn).
- It adds a low tail, at about -20 dB at the note-off, rising with note length. This is part of Dan's "lasting too long" on the theme. It is not the cause of finding 1's D5 plateau (inferred: too low).

Fix (instrument side, Opus state):
- Add a generic option to `tools/build_reaper.py` `cap_release` (`mix.json` "sus_release_cap_ms" spec):
  - `"no_start_mode_only": true` caps only the groups of the listed rows that have no startModes while the row's other groups have RoundRobin modes;
  - or a separate "mute_orphan_groups": {"rows": [...]} that sets those groups' `"active": false`.
- Scherzo value: Violins I, rows "Staccatissimo RRx9", "Stac RRx14", "Spiccato RRx9" (and "Stac On Bow RRx9" if finding 1b loads it), release 100 ms or inactive.
- The eight rotating groups keep their 524 ms, so the peaks cannot move (inferred).
- Check on a range test of 84-132:
  - 60 ms peaks within 0.5 dB of the control;
  - tail at +0.5 s after the peak of the isolated quarters at -55 dB or lower (now -39..-51);
  - separation median unchanged or better.
- Then the same on Violins II / violas: their 150 ms caps already include the group, so there is no change there.

### 3. Bar 23: the F sharp before the G is not a new blur; the 1.4 dB figure is a measurement artefact. The pair still dips 8 dB inside the printed crescendo, and a CC11 lift that starts after the trough can lift it.

Where: Violins I, bar 23:
- F sharp 5 staccato quarter, qn 66 (moved 65.802);
- G / A slurred pair on "Sus MAX", moved 66.560 / 67.060;
- B landing at 67.802;
- C accented at 68.296.

The printed hairpin is crescendo 66-69.

Evidence (measured, c23 stem, 10 ms frames):

| time (s) | what happens | level (dB) |
|---|---|---|
| 16.32 | F sharp note-on | |
| 16.43 | F sharp peak | -40 |
| 16.49 | G's moved note-on; the F sharp has fallen 4 dB | -44 |
| 16.55-16.57 | trough (the G has not started to sound) | -53 |
| 16.59-16.73 | G and A, one flat slurred plateau | -48 / -49 |
| 16.75 | dip before the B | -53 |
| 16.89 | B peak | -29 |

- `fig22.py` reads the F sharp's decay at the G's *moved* note-on. The 0.10 s lead puts that 0.09 s before the G sounds. The real valley between the F sharp and the G is 13 dB, so there is no blur.
- The slurred G-A join is legato as printed, and the A ends cleanly before the B (5 dB dip). Dan's blur note is met at bar 23.
- What is left: the pair at -48 sits 8 dB under the F sharp and 19 dB under the B, so the line dips in the middle of a crescendo.
- c22's lift (`C22_PAIRS` "short", from 66.45) raised the F sharp's tail because it started while the F sharp still sounded. With c23's lead, the F sharp is 10 dB down by 66.72 (16.546 s).

Fix (`build/score_config.py`, CC11 only, no envelope):
- Add `CC11_ADD_SPANS["Violins I"]` += `(66.72, 67.12, 20, 20)`. It starts at the trough and ends 0.06 qn after the A's moved note-on, the same "short" rule c22 adopted on bars 38 / 263. Keep `C22_SKIP` "66" so the old 66.45 lift stays off.
- Opus smooths CC11 over about 120 ms, so by 16.58 s the lift has added about 1 dB to the F sharp's tail, by which time that tail is already 12 dB down (inferred).
- Range test from qn 54, against a control from the same start:
  - pair within 6 dB of the F sharp;
  - trough between the F sharp's peak and the G's first 10 ms peak at 8 dB or more under the F sharp;
  - A -> B dip 4 dB or more;
  - B and C first 100 ms within 1 dB.
- Also change the measure (`fig22.py` / `rt23.py pairs`): for a note with a set lead, read the previous note's decay at the trough before the new note's first 10 ms peak, not at its moved note-on.

### 4. Celli legato joins land late: median +29 ms, 27% over 60 ms late. The trio tune and every wide leap are worst.

Where: Violoncellos, all 200 legato joins on "Leg Slur MAX". The trio tune, bars 169-184 (qn 504-552, celli espress.), is late at:
- 512 (+84 ms), 514 (+84), 516 (+182), 519 (+86), 522 (+157), 528 (+144);
- 540 (+111), 542 (+161), 544 (+102), 570 (+179), 576 (+157).

Also the second idea (148 +193, 154 +236), the tutti countermelody (312 +255, 912 +248), 366-378 (+84..+318), 630-663 (bars 211-221, +64..+292) and the reprise 761-797.

Evidence (measured, `pcx.py` on c23; perceived attack against the score onset):

| passage | joins | median | over 60 ms late |
|---|---|---|---|
| trio, 456-720 | 68 | +33 ms | 29% |
| reprise / coda, 720-1020 | 61 | +30 ms | 38% |
| second idea, 132-168 | 16 | +29 ms | 25% |
| coda Meno mosso | 7 | +2 ms | |

| join type | median | over 60 ms late |
|---|---|---|
| intervals of 6 semitones or more (22 joins) | **+76 ms** | 59% |
| intervals of 0-2 semitones | +27 ms | 24% |
| joins whose lead is already 0.25 s or more (20 joins) | +112 ms | 75% |

- Velocity is 80 or more on all 198 joins, so velocity is not holding the soft, slow transitions.
- The late joins at long leads show the lead is not the limit: the wide-interval transition samples are slow. HO manual p.144 (cited by c15): velocity sets the legato transition speed. c15's velocity 112 on five trio pickups landed bars 209-224 at +38..+57 ms.
- At the trio's quarter 228 an eighth is 0.13 s, so +100-180 ms puts the cello tune about an eighth behind the harp's off-beat chords. This is S2, inferred audible: the tune limps.

Fix (`build/score_config.py` `VEL_SET` and `build/leg_leads.json`):
- a) `VEL_SET["Violoncellos"]`: velocity 112 on every legato target 6 or more semitones from the previous note. A generic `LEG_LEAP_VEL` {track: (semitones, vel)} in `tools/score_to_parts.py` would avoid a list.
- b) Refit the per-onset offsets in `leg_leads.json` "Violoncellos" from this cycle's `pcx.py --json`:
  - add (pcx - 0.015 s), capped at +0.08 s, to each join late by more than 40 ms, within `LEG_LEAD_CLAMP` (0.35 s);
  - do this after a), since faster transitions change the fit.
- Check with `pcx.py` on the next render: median +15 ms or less, 15% or less over 60 ms, trio joins no later than +60 ms. Then the legato swell check (`rt22 legsag`): the higher velocity must not add more than 1 dB of crest at the join.

### 5. The hemiola accents of Violins I and II lose their CC11 bump under the crescendo to 312 / 912, while the violas keep theirs.

Where: bars 101-104 and 301-304, the accented half notes of the f hemiola at qn 300, 302, 304, 306, 308, 310 and 900-910.

Evidence (measured, parts.json and stems):
- CC11 bump at the accent (maximum within ±0.3 qn less CC11 0.4 qn before):

  | track | bump at 304 / 306 / 308 (units) | at 904-908 | configured add_loud (top) |
  |---|---|---|---|
  | Violins I | +0 / +0 / +0 | +0..+1 | 12 (124) |
  | Violins II | +0 | +0 | 6 (124) |
  | violas | +21 / +21 / +20 | | 20 |

  So the violins' bump is removed. The resting lane is 101-109, well under the top 124, so the bump is removed by the crescendo's own ceiling toward the arrival, not by "top". This is the finale's c25 lesson 122.
- First 100 ms against the note before, Violins I: +2.6, +1.1, +1.5, -0.5 (302-308) and +3.7, -0.1, +5.5 (904-908). These include the crescendo's own rise, so the accents add about 0-1 dB.
- Whole movement (`rt23 acc2`): Violins I accents median -4.5 dB against the detached note before (target +1..+2). The isolated-accent measure (c17) read +2.6, so this item is limited to the crescendo spans, where the shortfall is clear.

Fix (`tools/score_to_parts.py`, the accent CC11 add and the hairpin cap):
- Apply the crescendo cap (the `cc_cap` toward the arrival) to the resting lane before `ACCENT_CC` adds its bump, as the finale did (SHARED-TECHNIQUES 122: "capping only the resting lane brought a missing accent back (+3.8 dB)"). Keep `top`.
- Check: violin accents at 300-310 / 900-910 +1..+2 dB over the note before, after removing the crescendo trend (fit a line through the unaccented notes). The violas must stay unchanged, and the master arrival at 312 / 912 must not drop.

### 6. Smaller items measured this cycle (no action unless the above are done)

- Soft woodwind runs (finale c26 #6): measured. Only one woodwind eighth run in the scherzo starts soft after a rest (Flute 1, qn 780, velocity 53). Its next notes are +1.3 / -0.7 / -2.2 dB from the first, not the finale's 6-11 dB drop. No action.
- Harp "early" starts in `attacks.txt` (241, 553, 1021: -0.25..-0.30 s): measured to be the probe reading the previous held bass note. The chords at 241 sound at their beat (56.14 s). Not a fault; the probe could skip a starting note when a note on the same track is still within 6 dB.

## Do not touch

- Bar 23's 0.10 s lead and note ends (the A -> B dip and the 13 dB F sharp -> G valley are right).
- The bar 38 / 263 CC11 lifts.
- The 150 ms caps on Violins II / violas / celli / basses short rows.
- The B4 / E5 / B5 Violins I pairs on their current rows (5.4-6.4 dB).
- Violins II's same-pitch pairs (7.1 dB median).
- No release cap on the eight rotating Violins I short-row groups (twice negative).
- The flute / Oboe 1 accent rows.
- c15's velocity 112 on the trio pickups.
