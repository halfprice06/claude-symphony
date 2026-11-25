# Cycle 60, critic B: balance and levels (render under review: c59)

Nobody listened. Every figure is measured on the c59 stems and master (30 ms frames, 10 ms hop, power means) against the
c58, c57 and c56 renders, unless marked "inferred". "Body" is the median level 0.1-0.7 s into a note. "Margin" is a
melody stem minus the power sum of all other dry stems. "Pitch-adjusted" is a level with a fixed effect per pitch
removed. Scripts and tables: `cycles/c60/critic_scripts/B/` (`lib60.py`, `notes.py`, `sp.py`, `who.py`, `mg.py`,
`dynmap.py`, `dynstep.py` / `dynstep.json`, `simul.py` / `simul_c59.json`, `cccurve.py` / `cccurve.json`, `spread.py` /
`spread_c59.json`, `plateaus.py`). `build_reaper.py` was used only cut before `ENV_LUA`. Nothing was built or rendered.

Not done: `README.md`, `HISTORY.md`, `LEARNINGS.md`, `EW-TEMPLATE-PLAN.md` and `FINDINGS.md` were not re-read (the
coordinator's notes, c59 `CHANGES.md`, c59 report B and `BRIEF.md` were). The plan sections c58's critic B listed as not
applied (5, 6, 10) were not re-checked. No spectra this cycle; the band shares in `metrics.md` are inside the range of
the three references (20-100 Hz -14.6 dB against -21.7 / -8.5 / -7.9), so the bass is not treated as a fault.

## Manual notes (2021 HO Opus manual) and Rimsky-Korsakov

| Source | Where it applies | Does the render follow it |
|---|---|---|
| Volume sets a level relative to other instruments, CC11 shapes each instrument's dynamics; velocity sets the loudness of short articulations (p. 63) | celli staccato strokes in the fugato; the role rows that have no CC11 room at fff | Partly: the celli strokes carry a fitted -7.5 dB row on the envelope as well as the velocity cut (finding 2); the trumpets' fff rows were lost (finding 1) |
| Timpani Felt Long: velocity controls dynamics in up to 16 levels, CC11 and velocity control loudness (p. 123) | ff timpani strokes, median velocity 107 | No: the strokes get +6 dB from the track envelope for 0.75 qn instead of velocity (finding 5) |
| Rimsky-Korsakov, Principles, p. 33: in forte trumpet = trombone = tuba = 2 horns, horn = 2 woodwinds, a string section = 2 woodwinds; in piano all winds are about equal and a string section = 1 wind | every track at one printed dynamic at one moment (`simul.py`) | At p and pp yes within 3 dB, except Horn 4 and the clarinets in bar 145. At ff and fff no: Horns 1-2 are over the trumpets and trombones (finding 1) |

## The balance items under "Left audible" (measured; c57 is the last render with the per-note envelope)

| item | c57 / c58 / c59 | judgement | fix |
|---|---|---|---|
| Horn 1 qn 497-501 (mp espr.) | stem -41.4 / -43.4 / -42.0; margin -5.0 / -7.0 / -5.3 | resolved: margin within 0.3 dB of c57 | none |
| Horn 1 qn 587.5-589 (crest of the hairpin) | stem -38.6 / -43.5 / -41.8; margin -4.1 / -7.9 / -6.1. Phrase 584-606 margin median -6.2 / -6.4 / -6.2 | crest 2 dB short, phrase equal to c57 | optional: `CC11_ADD` Horn 1 587.5-589 +7 -> +13. The +7 gave +1.2 / +2.0 dB here (0.17-0.29 dB per unit, half the track's 0.51 at 72-88), so expect +1.0 to +1.7 |
| Horn 3 qn 165-168 (under Horns a2) | stem -42.0 / -38.2 / -39.5; Horns a2 minus Horn 3 5.3 / 2.2 / 3.3 | 2 dB short | `CC11_ADD` Horn 3 165-168: 84 -> 54 becomes 78 -> 54 (100 -> 84 gave 1.4 dB, on the flat 88-104 segment; below 88 the track's slope is 0.46): expect -1.5 to -2.5 |
| Trumpet 3 qn 456-464 | stem -37.7 / -33.5 / -34.5; margin -15.3 / -12.7 / -13.7 in a tutti at -20.8 | 3 dB over c57 but 14 dB under the tutti: low priority | 80 -> 81 becomes 73 -> 74 (0.35 dB per unit at 72-88: -2.5) |
| Clarinet 1 qn 576-582 (pp F4 under the oboe) | stem -51.3 / -46.3 / -55.2; Oboe 1 margin +2.3 / -2.1 / +3.6 | 3.9 dB under c57: too far | CC11 12 -> 17 flat. Measured on this note: CC11 23.5 -> -48.0, 12 -> -56.6, so 0.75 dB per unit: expect -52.8. See also Clarinet 2 in finding 3 |
| Celli bar 87 | bars 85 / 86 / 87 master: c57 -33.6 / -38.5 / -45.0, c59 -35.6 / -42.5 / -47.0 | fault: finding 2 | finding 2 |
| Notes after the sf at qn 78 (Violins I 80.5-81.5) | -33.1 / -34.8 / -37.7 in c58, -36.5 / -37.5 / -40.7 in c59 | not a fault. A diminuendo is printed from 80 to the mf at 86. The sf itself fell 2.9 dB by design, and the line now falls evenly: sf -31.1, 80.5-81.5 -36.5 to -40.7, 84-85.5 -41.5 to -44.5, mf at 86 -42.4. In c58 the notes at 85-86 were 5-6 dB under the mf arrival (-48.4, -47.6, -46.7) | none |
| Trumpet 1 fff, bar 122 (qn 484) | stem -29.8 / -34.8 / -34.9 | fault, and it is all three trumpets: finding 1 | finding 1 |
| Horn 4 over Horn 1, bar 111 (qn 440-444) | whole bar: Horn 1 -49.2, Horn 4 -50.6, so Horn 4 is not over. By beat: Horn 1 -46.2 / -48.3 / -53.6 / -53.3, Horn 4 -52.5 / -49.1 / -50.8 / -50.7 | Horn 4 is over by 2.6 dB on beats 3-4 only, because Horn 1's A-flat 4 falls 7 dB inside the note while its CC11 rises 52 -> 59 (it fell 4-5.6 dB in c57 too: the sample) | Horn 1 crescendo: 440: 52, 444: 64, 448: 70 (now 52, 60, 69). 0.36 dB per unit at 46-72: +1.4 dB at the end of bar 111. Do not lower Horn 4 here |

## The 28 dropped short role rows: which matter (c57 -> c59 on the covered notes)

- `[672, 676, -2.5]` on eight tracks (bar 169): Flute 1 +2.9, Clarinet 1 +3.1, Trombones 1 / 2 +3.4 / +3.3, Violins I / II
  +2.9 / +2.1, Oboe 1 +0.4, celli -0.6. The theme (Violas, Horns a2, Trumpets a2) rose as well: its margin over 672-676 is
  -5.4 in c57 and -5.1 in c59, over 664-680 median -5.4 and -4.1. Does not matter. Leave dropped.
- `[567.75, 572.5, +1 / +2]` on eleven brass tracks (bars 142-143): Trumpet 1 -0.7, trombones and Tuba -0.6 to -0.7,
  Trumpet 2 -2.7, Horn 2 +3.2 (both hold E-flat 4, so the pitch's level is unchanged), master -28.7 / -28.7. Does not
  matter. Leave dropped.
- Bass clarinet `[703.5, 707.5, -3]` and Clarinet 1 `[705.75, 707.75, +2.5]` (bar 177, Clarinet 1 over the trombone
  chorale, morendo): Bass clarinet +2.5 (-53.5 -> -51.0), Clarinet 1 minus Bass clarinet 2.8 -> 1.7 dB, Clarinet 1's margin
  at 706-707 -9.5 -> -12.2. Matters a little. Fix: Bass clarinet D3 CC11 34 -> 27 flat over 704-708 (0.39 dB per unit at
  34-46, thin below: inferred -2 to -3); Clarinet 1 B4 start 48 -> 54 (0.33 at 46-58: +2).
- Violas `[320.5, 324.25, -3]` (bar 81 tremolo): +2.9; Violins II the same row: back at c57's level without it (-38.9 /
  -38.3); basses +0.9. The tutti is at -29.4. Violas only: tremolo CC11 84 -> 102 becomes 78 -> 96 (0.44 / 0.29 dB per
  unit: about -2.2). Low priority.
- Violins II `[176, 183, -2]`: +2.1, but Clarinet 1's margin there is better than c57 (-2.5 -> -1.3). Does not matter.
- Trumpet 2 `[279.75, 284, -1.5]`: +2.2 at a margin of -14.9. Does not matter.
- Horn 3 165.5 and Trumpet 3 456: in the table above.

## Finding 1 (largest). Brass at ff and fff: the trumpets are under the horns at the bar-122 climax, and Horns 1-2 at ff are level with the violins' theme

Where: bar 122 (qn 484-492), bars 26-31 (qn 100-124), every ff chord with Horns 1-2.

Evidence (measured):
- Bar 122, fff, note bodies at qn 484: Trumpet 1 A-flat 4 -35.2, Trumpet 2 D4 -35.6, Trumpet 3 B3 -35.2; Horn 1 -30.1,
  Horn 2 -30.2; Trombones 1 / 2 -31.7 / -32.1; Tuba -30.8. Each trumpet is 5 dB under each of Horns 1-2 and 3.5 under
  each trombone. Rimsky-Korsakov gives a trumpet twice a horn in forte.
- Against c57 over 484-488: Trumpet 1 -29.8 -> -34.9, Trumpet 2 -32.4 -> -36.3, Trumpet 3 -31.2 -> -34.9; master bar 122
  -16.6 -> -18.1. Cause: the role rows Trumpet 1 `[484, 488.5, 2]` + `[484, 486.5, 2]` and Trumpets 2 / 3
  `[484, 488.5, 2]` were sent to CC11 (`to_cc` entries marked True), and CC11 is already 124, so nothing is played.
  Trombone 1's `[484, 492.5, 2.5]` and the Tuba's `[484, 492.5, 2]` are long enough to stay on the envelope as slow rows
  and are still there. Trumpet 1's A-flat 4 also reads 3.2 dB under its G4 at the same CC11 124 (-44.1 against -40.9
  with the envelope removed).
- Same dynamic, same moment (`simul.py`: 68 moments with five or more tracks at ff; each track's level minus the median
  of the tracks at ff): Horn 1 +2.6 (n 17), Horn 2 +3.0 (n 10), Horn 3 -1.3, Horn 4 -0.7; Trumpets 1 / 2 / 3 +2.2 / -0.7 /
  -0.1; Trombones 1 / 2 +0.8 / +1.3; Bass trombone -1.8; Tuba +1.7. At f the same horns read -2.3 and 0.0. So Horn 1 rises
  9.0 dB from f to ff (pitch-adjusted; Horn 3 5.8, Horn 4 6.8, Trombone 1 4.4, Trumpet 1 6.2).
- Bars 29 and 31: Horn 2 (F4) -32.3 / -33.6 and Horn 1 (A-flat 4) -32.9 / -32.5 hold whole-note harmony and are the
  second and third loudest stems, 0.4-1.0 dB under the Violins I theme (-31.9 / -32.1) and over Flute 1 and Violins II
  on the theme (-33.9 / -33.7). The role `[104, 112, -3]` covers bars 27-28 only.

Fix (dynamic trims and slow rows; no per-note value):
- `build/roles.json`: Trumpet 1 `[484, 488.5, 2, 1]` and `[484, 486.5, 2, 0.25]` -> one row `[484, 492.5, 3, 1]`; Trumpet
  2 and Trumpet 3 `[484, 488.5, 2, 1]` -> `[484, 492.5, 2, 1]`. The span is the one Trombone 1 and the Tuba already have
  (two whole notes, about 5.5 s), so it stays a slow row. Alternative in the tool: `LEVEL_TO_CC` keeps a row on the
  envelope when it lasts 4 s and CC11 has no room.
- `build/mix.json` `dyn_trim_db`: Horn 1 `"ff": 1.5 -> -0.5`, `"f": -0.8 -> 0.7`; Horn 2 `"ff": 0.4 -> -1.6`.
- Expected: trumpets at 484 -32.2 / -33.6 / -33.2 (c57 -29.8 / -32.4 / -31.2), still 2-3 dB under Horns 1-2; master bar 122
  +0.2 dB. Horns 1 / 2 at ff +0.6 / +1.0 over the ff median (trombones +0.8 / +1.3); bars 29 and 31 Horns 1-2 2.4-3 dB
  under Violins I. Horn 1 at f -2.3 -> -0.8 (Horn 2 0.0, Horn 3 -1.5); its f -> ff step 9.0 -> 5.5 dB.
- Inferred: Horn 1's f passages in bars 131-142 are harmony (it reads -1 to -5 dB against the f median there), so +1.5
  does not put it over a melody. Check the margins of bars 131-134 after the render.

## Finding 2. The fugato subject, celli alone, bars 85-87: 14 dB between its notes, and a fitted row is still on the envelope

Where: Violoncellos qn 336.5-349, mf, no other instrument plays (rest -84 dB).

Evidence (measured, peak of each note): head B-flat 3 (accent, Leg BC MAX) -30.5; staccato eighths 338.5-339.5 -32.3 /
-31.2 / -39.3; G3, G-flat 3, G3 on Sus MAX -38.3 / -39.4 / -41.2; the accented E-flat 3 at 342 -39.0, no louder than
its unaccented neighbours and 8.5 dB under the first accent (c57 -30.4); strokes at 343.5 and 344 -38.0; strokes at
345, 346, 347 -44.7 / -44.6 / -40.2; C4 at 348 (mp) -54.1 (c57 -46.6). Bars 85 / 86 / 87 on the master: -35.6 / -42.5 /
-47.0 (c57 -33.6 / -38.5 / -45.0). The violas' answer (bars 88-90) spans 7 dB (-36.0 to -42.9).

Causes:
- The track envelope steps from +11.9 to +4.4 dB at qn 344.82-344.95 and back at 347.62-347.75. These are two
  `LEVEL_SHAPES["Violoncellos"]` rows fitted to the c26 and c47 renders: `score_config.py` line 1498
  `[(343.45, 0.0), (343.48, -4.0), (347.6, -4.0), (347.72, 0.0)]` and line 3277 `[(343.44, 0.0), (343.47, -3.5), (347.6,
  -3.5), (347.72, 0.0)]`. Together -7.5 dB over three staccato notes for under 2 s. This is a fitted level row on the
  track volume envelope; c59's count of "fitted rows 0" missed it (the rule dump lists it as slow).
- On top of it c59 cut the velocity of the same strokes 77 -> 68 (measured -2.3 dB at 338.5-340, 0.26 dB per unit).
- The accent at 342 and the lift on the C4 at 348 were envelope shapes (+4.5 and +8) and are gone with nothing in CC11.

Fix:
- `build/score_config.py`: delete those two rows from `LEVEL_SHAPES["Violoncellos"]`.
- `VEL_SET["Violoncellos"]`: 345.0 and 346.0 68 -> 62, 347.0 68 -> 52 (its B3 sample reads 4.4 dB over A3 and B-flat 3 at
  one velocity), 338.5 and 339.0 68 -> 60. Velocity values below 68 are extrapolated from one measured step (inferred).
- `CC11_ADD` Violoncellos 342-343.5 +9, flat (69 -> 65 becomes 78 -> 74; the track's slope 0.45 at 58-72 and 0.41 at
  72-88: +3.7 dB); 348-349.75 +10 (58 -> 68: +4.5 dB).
- Expected peaks: strokes 338.5 / 339 -34.4 / -33.3 (3-4 dB under the head); accent at 342 -35.3; strokes 344-347 -38.0 /
  -38.8 / -38.7 / -36.9; C4 at 348 -49.6. Range of the subject 14 -> about 8.5 dB; bars 85 / 86 / 87 about -36 / -41.5 /
  -41.5. Range render 336-349 first.
- Not proposed again as a first step: `region_gain_db` Leg BC MAX -2.5 on the celli (the head on Leg BC MAX reads 8 dB
  over the Sus MAX notes at CC11 72). It would also bring the head down, and it changes every Leg BC passage.

Two more short level steps on an envelope that are not on a printed dynamic (`plateaus.py`): Violas 244.1-248.7 -8.7 dB
for 2.3 s over four notes (`LEVEL_SHAPES`, lines 203 and 395) and Bass clarinet 424.4-432.1 +4.5 dB for 3.7 s over nine
notes (line 2005 plus a second lift). Both are phrase rows written as steps. The actor should check whether they are
roles (then write them in `roles.json` with ramps) or fitted rows (then remove them).

## Finding 3. The dynamic mapping per track: in order on most tracks; five places where a step is missing or a track is out of line with its family

Method (measured): `dynstep.py` takes notes of 0.3 s or more on long rows whose printed dynamic is within 2 CC11 units of
an anchor, and gives the median body, raw and pitch-adjusted. `simul.py` compares tracks that hold the same printed
dynamic at the same moment. Full tables: `dynstep.json`, `simul_c59.json`.

In order with steps of 2 dB or more (pitch-adjusted): Clarinet 1 (pp -56.9, p -48.7, mp -45.9, mf -41.0, f -38.2, ff -33.5),
Bass clarinet, Bassoon 1, Horn 2, Horn 3, Trombones, Violins II, Violoncellos (pp -54.4, p -50.6, mp -48.3, mf -44.1,
f -40.1, ff -34.5), trumpets and Tuba (f and ff only). Families at one dynamic at one moment (median deviation from the
tracks sharing the dynamic): at pp winds +2.9, horns -2.1, low brass 0.0, strings -0.5; at f winds -1.2, horns -1.0,
trumpets +1.3, low brass +1.1, strings +2.8; at ff winds -0.7, horns +0.9, trumpets 0.0, low brass +0.4, strings +2.3.
So p and pp agree between families within 3 dB. Timpani rolls of 2 s or more are never the loudest stem after their first
0.8 s (closest: bar 160, 2.1 dB under Trumpet 1; bar 124, 3.3 dB under the basses).

Faults and fixes (`build/mix.json` unless stated):

| track | measured | fix | expected |
|---|---|---|---|
| Horn 4, soft dynamics | pitch-adjusted pp -55.2, p -55.0, mp -51.4, mf -48.5, f -42.7: no step from pp to p. At p it is 5.6 dB under the tracks sharing p (n 7: qn 246, 268-270, 502, 660-662); Horn 2 on the same chords -0.9. By pitch at CC11 64 or less: G3 -54.8 (n 15), A-flat 3 -56.4, F3 -52.4; Horn 3 -50 to -52, Horn 2 -46 to -49.5 | `soft_trim_db` Horn 4 `"p": 5.0 -> 7.5`, `"mp": 5.0 -> 6.0`, `"mf": 4.0 -> 5.5`; `region_gain_db` F3 on Sus MAX, the entry with `"dyn": ["pp", "mf"]`: -6 -> -8.5 so that F3 stays where it is | pp -55.2, p -52.5, mp -50.4, mf -47.0, f -42.7; at p 3 dB under the group; F3 over G3 at p 1.7 -> -0.8 dB; bar 111 unchanged |
| Oboe 1, mf | p -49.7, mf -48.5, f -43.2: 1.2 dB from p to mf. Cause is three pitches on the soft layer. Instrument output at CC11 61-80: E-flat 5 -53.2 (n 4), E5 -51.5 (n 2), F5 -50.2 (n 1) against D5 -46.5, C5 -47.1, G-flat 5 -40.5, G5 -41.9. At CC11 81-100 they are in line (E-flat 5 -45.2, F5 -43.3, G5 -42.0). The existing gains cut E5 by 5 and F5 by 2.5 / 8.5 on every layer. Bar 79 motif: G5 -40.7, then G-flat 5 -47.3, F5 -49.2, E5 -49.8; margin on beats 3-4 -9.4 / -7.8 | `region_gain_db` Oboe 1: give the three existing E5 / F5 entries a `"dyn"` list with the loud layers only; add an entry for the soft layers, all rows: `{"75": 7, "76": 0, "77": 2}` (E-flat 5 +7, F5 +2, E5 no cut). Layer names from the patch's group names, as for Horn 1 | E-flat 5, E5, F5 at mf -45 to -46.5; bar 79 F5 / E5 +4.5 / +5.0, margin about -6 / -3.5; Oboe 1 mf about -45 (p -49.7, f -43.2). Thin (1-4 notes per pitch): range render bars 22, 38, 79, 135 |
| Violas, p | pp -54.0, p -49.0, mp -48.9, mf -45.4: no step from p to mp (raw p -48.3, mp -50.2). At p the violas are +2.6 over the tracks sharing p (n 8) | `soft_trim_db` Violas `"p": 5 -> 3` | p -51.0: steps 3.0, 2.1, 3.5; at p +0.6 |
| Oboe 2, f | f -46.6, ff -35.7: 10.9 dB step. At f 5.0 dB under the tracks sharing f (Oboe 1 -2.4), at ff -1.8 | `dyn_trim_db` Oboe 2 `"f": 3.5 -> 6.0` | f -44.1, step 8.4; at f -2.5 |
| Clarinet 2, pp, bar 145 (qn 576-582) | D4 -48.5 at CC11 28 -> 22: 7 to 12 dB over the other pp parts (Violins I -53.8, Bassoon 1 -56.2, Horn 3 -56.5), 6.3 dB under the oboe's p dolce and 6.7 over Clarinet 1 | CC11 28 -> 22 becomes 21 -> 16 over 576-582 (`CC11_ADD` -7; Clarinet 2's slope 0.52-0.66 below 46, thin: about -4), with Clarinet 1 at 17 | Clarinet 2 about -52.5, Clarinet 1 -52.8, oboe margin +3.6 -> about +5 |

Also measured, no fix proposed: Violins I pp is +5.2 over the tracks sharing pp, all of it the coda melody 708-722;
Trombone 1 at f +3.8 (bars 98-101 +5 to +9 on the same notes as Horns a2, which read 2.6 dB lower; melody group there
-25.5 against Trombone 1 -33.3); Flute 2 at f 4.9 dB under Flute 1 (lower register); Tuba and Double basses f -> ff 9.4
and 9.1 dB; Timpani single strokes f -> ff 1.7 dB on the body measure (peak -27.9 -> -24.6).

## Finding 4. Tutti entries: 93 ms between the first and last track, most of it Oboe 2

Method (measured): 16 chords where 8 or more tracks start a note after a rest of 0.5 qn or more. Half-rise is the first
time a stem's 10 ms level reaches its body level minus 6 dB, against the score beat. Run on c58 and c59: the track
medians agree within 7 ms, so these are not render-to-render shifts.

- Spread per chord: maximum minus minimum median 93 ms (38 to 212), 10th to 90th percentile 47 ms. The chord median sits
  5 ms before the beat.
- Oboe 2 is first in 11 of its 13 chords: median 40 ms before the chord median (quartiles -77 / -27), 47 ms before the
  beat. Where its note-on lead is 180 ms (qn 100, 324, 330, 548) it arrives 77, 84, 160 and 92 ms early; with a lead of
  40 ms (qn 628) it is 6 ms late. So its half-rise is about 20 ms and its leads are 4 to 9 times that.
- Late: Trumpet 2 +20 ms (lead 60; +80 at 104, +46 at 552, +40 at 272), Horn 3 +10, Tuba +12, Flute 1 +11. At the fff
  chord of bar 122 (qn 484) Horn 1 +69 (c58 +69), Horn 2 +63 and Trumpet 1 +49 ms after the chord median, which is itself
  8 ms late. Bassoon 2 at 620: +115 ms.
- All other tracks: within 14 ms of the chord median (Horn 2 -14, Violas -11, Trombone 1 -10). Timpani +22 ms with a note-on 20 ms after the beat
  (`TIMP_DELAY_S`): by intent, left.

Fix: `score_config.py` `ENTRY_LEAD_S["Oboe 2"]` `(0.0, 0.14, 0.0)` -> `(0.0, 0.05, 0.0)`, and in `build/entry_leads.json`
cap Oboe 2's totals at 0.06 s for the onsets 100, 324, 330, 484 and 548. `ENTRY_LEAD_S["Trumpet 2"]` `(0.06, 0.06, 0.05)`
-> `(0.08, 0.08, 0.05)`. `entry_leads.json`: Horn 1 484.0 +0.06, Horn 2 484.0 +0.06, Trumpet 1 484.0 +0.04, Bassoon 2
620.0 +0.10. Expected: Oboe 2 within 15 ms of the chord median; chord 330 212 -> about 90 ms; chord 484 110 -> about 60 ms;
median spread 93 -> about 70 ms.

## Finding 5. Timpani: the last per-note shape on a track envelope

Evidence (measured): `TIMP_LOUD_ATTACK_DB = 6.0` writes +6 dB at each f and ff stroke and takes it away over 0.75 qn. On
47 ff strokes the envelope falls 6.0 dB within 0.6 s of the stroke (median); `plateaus.py` counts 148 short level steps on
the Timpani envelope and none of this kind on any other track. `envelope_table.md` lists it as "timp:settle" (77 of
109 notes with 3 dB or more of envelope inside). The ff stroke peaks at -24.6 dB, 1.8 dB under the sum of all other
stems over the same 0.3 s (quartiles -3.4 / -0.1). The strokes play at a median velocity of 107, and the manual gives
this patch up to 16 velocity levels (p. 123).

The coordinator's notes list timpani dynamics as allowed on the envelope. This item is a shape inside each note, so I
report it for a decision. Fix if it is to go: `TIMP_LOUD_ATTACK_DB = 0`, ff strokes at velocity 120-127 and f at 108-112
(`TIMP_VEL`), `dyn_trim_db` Timpani `"ff": 2.0 -> 4.0`. Inferred, not measured: the peak stays within 2 dB of now and the
ring after the stroke is 2-4 dB louder. Range render bars 27-28 with the peak and the level at +0.5 s compared with c59.

## Finding 6. Small items in one list

The fixes in the "Left audible" table (Horn 3 165, Trumpet 3 456, Clarinet 1 576, Horn 1 bar 111 and 587.5) and in the
dropped-rows list (Bass clarinet 704, Clarinet 1 706, Violas 320.5). None changes a bar of the master by more than 1 dB.

## Do not touch

Horn 1 qn 497-501 (margin back at c57's); the 672-676 and 567.75-572.5 rows left dropped; the line after the sf at
qn 78 (even fall to the mf at 86); the theme's margin in bars 27-31 (-2.2 against -3.2 in c57) and in bars 167-170;
Clarinet 1, celli and Violins II dynamic steps; timpani roll levels (never the loudest stem); `TIMP_DELAY_S`; the leads
of the tracks that arrive within 14 ms of the chord median; the envelopes of the other tracks as c59 left them (no
per-note item found by `plateaus.py` outside the three rows named in finding 2 and the timpani).
