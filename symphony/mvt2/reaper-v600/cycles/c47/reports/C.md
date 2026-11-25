# Cycle 47, critic C: holistic comparison (on the c46 render)

This report compares the c46 render with four references:
- c41, the last render before the EastWest template mix;
- the c27 port baseline;
- series 1's c26 render of v77, on the unchanged bars 1-22;
- recordings: the local Dvořák 9/i, the stored Brahms 1/ii and 4/ii band shares, and the recordings' cutoff times in `mockup-kit/LEARNINGS.md`.

It also checks Dan's standing notes and answers the coordinator's question about the final chord.

Method: stems and master were measured with my own scripts, each render on its own `parts.json` tempo map. The tools used were `pcx.py` attack functions, the c44 `s1check44.py`, `rbdip44.py` and `check44.py`, and a dry run of `auto_fills.py` on a scratch copy of `build/`. Everything is measured unless marked inferred.

c47 is the last render before Dan listens, so the fixes below are data changes only: timing, fills and level shapes, with no Opus state change. None of them touches the audio device, the hall, the returns or the mics.

## Manual notes (row c47 / C: T1, May 2021 HO manual PDF pp. 143-146, read in full; `loop/MANUAL-GAPS.md` read)

| PDF page | What it says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| 143 | Performance scripts are automated by CC: 5 legato/portamento time, 15 con sordino, 22 mono/poly, 36 RR reset, 57 legato script, 65 portamento script, 69 repetitions, 70 finger position. Without CC data a script keeps its default. | parts.json sends CC15 (mutes), CC70 (on Violins I/II, violas, celli), CC69 in the pre-roll, and the pre-roll RR reset (CC16). | Yes. The coda mutes switch on in rests before each "con sord." entry: Violins I at 274.5 for 292, Violins II and violas at 273.5 for 286 and 279. No mute switches under a sounding note. |
| 143-144 | The Portamento and Legato scripts are emulations. True legato lives only in the legato patches, through the Monophonic True Legato script. | Every slurred line uses the KS Masters' Leg rows. | Yes. CC57 and CC65 are correctly unused. |
| 144 | True legato: velocity sets the transition time (50-60 longer, "allowing the melody to breathe more"; 110-127 shorter) and does not change loudness. | c45 `LEG_VEL_BY_CC` moved wind targets to v86-104 and horn targets to v80-98 (they were v60-124). | Partly. The bodies kept their level, but the transitions changed shape and timing. Join fills and two CC7 cuts fitted to the old transitions now sit beside the holes (finding 1). Example: Clarinet 1 at 283 went from v60 to v88, and a +2 dB transition bump became a 10 dB hole in the stem. |
| 144 | Con Sordino script: fewer high overtones, on CC15. | Strings in bars 15-30 and the coda. | Yes. |
| 145 | The Repetition script randomises repeated notes. RR Reset makes playback repeatable (2025 p.92: the reset follows the CC set in Preferences). | S1 repeats; render-to-render repeatability. | Yes. The CC16 reset gave level-identical unchanged notes in c46. The Repetition script stays off, which keeps renders repeatable. Repeats still alternate takes. |
| 145-146 | Finger Position on CC70 (FP4, nearest the bridge, is warmer). It exists for 1st and 2nd violins, violas and celli, and is only a preference where the note allows. | Sul D (Violins I opening; celli in bars 23-28 and 71-74), sul A (violins in bars 53-56), sul G and sul C (bar 64). | The lanes are present. The basses carry none, which agrees with p.145: the HO basses have no table. The tables on pp. 147-149 belong to row T2 and were not checked here. |

## Where c46 stands (measured)

| | c27 | c41 | c46 | reference |
|---|---|---|---|---|
| Delivered LRA, LU | 14.9 | 15.5 | 15.4 | target 14-16 |
| Delivered p10-to-max span, dB | 17.7 | 18.9 | 18.9 | target 16-19 |
| Delivered limiter, dB | 1.1 | 2.3 | 2.4 | at most about 3 |
| Band share 20-100 Hz | -19.4 | -19.1 | -18.0 | Dvořák -21.7 |
| Band share 100-250 Hz | -8.3 | -8.4 | -7.5 | Dvořák -6.6; Brahms -8.8 / -7.6 |
| Band share 250-500 Hz | -6.4 | -5.6 | -5.6 | -5.95 to -6.3 |
| Band share 500-2000 Hz | -2.7 | -3.2 | -3.7 | -3.5 to -4.4 |
| Band share 2-6 kHz | -11.3 | -10.6 | -9.9 | -10.5 to -12.4 |
| Band share 6-20 kHz | -30.1 | -30.2 | -29.4 | -28.8 to -32.3 |
| Final chord, time to fall 20 dB (master), s | 0.72 | 0.33 | 0.48 | recordings' cutoffs 0.43-0.58 |
| Beat deviation, median | 1.5 % | 1.5 % | 3.0 % | Duc 8 % |
| Beats more than 15 % slow | 7 | 7 | 16 | Duc 49 of 403 |
| S1 master dip at repeats, median, dB | n/a | 3.5 | 3.7 | |
| Wind entries, body - 6 dB, re beat (median) | n/a | -24 ms | -38 ms | strings +7, brass -23 |
| Legato joins on solo lines with a master dip of 5 dB or more | n/a | 7 | 15 | |

Notes on the table:
- **Family tails** (c46, `check44`): time to fall 20 dB is 0.38 s for strings, 0.30 s for winds and 0.25 s for brass. All are at or below the recordings' 0.43-0.58 s.
- **Stereo.** Side/mid is -5.4 dB and the L/R correlation below 250 Hz is 0.63, close to the references (-4.7 to -5.4 dB, 0.54-0.62).
- **Slow beats.** All 16 beats more than 15 % slow fall on phrase-end breaths or printed rits.
- **Delivered levels per bar, c46 against c41.** 73 of 92 bars are within 1.5 dB. The bars that moved most:

  | bar | change | reason |
  |---|---|---|
  | 8 | +5.4 dB | the Horn 1 swell came back in c44 |
  | 13 | +2.5 dB | |
  | 35 | +3.6 dB | |
  | 67 | +4.3 dB | Horn 1's p dolce entry after the niente |
  | 83 | +3.1 dB | |
  | 66 | -3.2 dB | deeper niente |

- **Bars 1-22 against series 1 c26.** The notes are unchanged. The delivered level is a median 2.2 dB louder, which is the delivery ride, not the mix.

### Dan's standing checks
- **Too wet.** Solved by these numbers. The tails sit at or below the recordings, and winds and brass are now drier than any recording. If Dan hears it as dry, the place to change it is the R Winds and R Brass return faders, not the IR. That is a question for Dan after he listens, not a c47 change.
- **Mushy.**
  - Between 100 Hz and 6 kHz the band shares are within about 1 dB of the references.
  - The 20-100 Hz band is 3.7 dB over the Dvořák, and 1.4 dB of that is new in c46: the basses' f/ff trims (+2.5 / +4) raised the basses' 20-100 Hz energy by 2.5 dB. This is a balance question for critic B; I note it but do not rank it.
  - The remaining smear is local and comes from the joins (finding 1), not from the hall.
- **S1.** 49 repeat points, master dip median 3.7 dB. Five are under 2 dB: Violins II at 51, 112 and 292, Violins II div at 114, celli at 128. All five are accompaniment under a louder line.
- **S2.** Strings (+7 ms) and brass (-23 ms) are near the beat. The winds have been early since c44 (finding 2).
- **S3.**
  - No master dip deeper than 9 dB anywhere. Dips of 5 dB or more that recover number 32 in c46 against 39 in c41.
  - All 24 caesuras are clean (c46 CHANGES).
  - Since c44 the hall sends are post-fader (`I_SENDMODE` 0), so the volume envelope also acts before the hall. A fast fall in the envelope can no longer cut the hall's tail; it can only cut the dry stem's own recorded release.
- **Loop pulsing.**
  - Master autocorrelation at 3.95 s: -0.33 on the opening, 0.01 on the basses' pedal at 220-238, 0.15 and 0.00 on the coda.
  - A sweep of every held span of 7 s or longer on every stem found three periodic notes:

    | note | autocorrelation at 3.95 s | context |
    |---|---|---|
    | Horn 4 at 84 | 0.77 | finding 5 |
    | Horn 4 at 262 | 0.89 | under the ff tutti, masked |
    | Violas at 279 | 0.55 | shaped, SD 4.8 dB |

## Findings, ranked by what a listener would hear

### 1. Holes inside the slurred solo lines: master join dips of 5 dB or more went from 7 (c41) to 15 (c46), the worst at 7-8 dB in the bass clarinet and horn solos (measured)

**Where.** The legato joins of the six solo lines:
- Horn 1, bars 7-14 and 65-70;
- Oboe 1, bars 15-20 and 45-47;
- bass clarinet, bars 31-36;
- Flute 1 and cor anglais, bars 37-44;
- Clarinet 1, bars 85-89;
- the Violin I solo.

97 joins in all.

**What is wrong.** Inside a slur the line drops away for 0.1-0.4 s at a note change and comes back. On an exposed wind solo this sounds like a gap in the phrase, which is a machine trait.

**Evidence.** Each join measured with 30 ms windows: the minimum in [-0.10, +0.15] s around the score onset, against the mean over [-0.35, -0.12] s.

| render | master dips ≥ 5 dB | master median | stem dips ≥ 6 dB |
|---|---|---|---|
| c41 | 7 | 2.5 dB | 16 |
| c43 | 7 | 2.8 dB | 16 |
| c44 | 12 | 3.0 dB | 31 |
| c45 | 16 | 2.7 dB | 31 |
| c46 | 15 | 3.0 dB | 26 |

The worst joins in c46, with c41 in brackets:

| join | master dip | stem dip |
|---|---|---|
| bass clarinet 92 / 92.5 (bar 31, the solo's slurred eighths into the E flat) | 8.2 / 6.9 (6.3 / 2.4) | 10.9 / 7.5 |
| Horn 1 230 (bar 68, the step down from the mp peak) | 7.1 (3.9) | 10.0 |
| Horn 1 23 / 35 / 37.5 (bars 8, 12, 13) | 6.2 / 5.3 / 6.2 (3.1 / 2.5 / 2.5) | |
| Oboe 1 44 / 57 / 59 / 143 | 5.7 / 5.3 / 5.0 / 5.5 (4.6 / 3.7 / 2.8 / 4.2) | |
| Flute 1 and cor anglais 133.5 | 5.5 (2.5) | |
| Clarinet 1 283 (bar 86, coda solo) | 4.0 (1.5) | 10.0 (2.4) |

**Why (measured, mechanism inferred).**
- The per-note join fills (`build/early_fills.json`) and two CC7 cuts were fitted up to c38 on wet stems, which then carried the Opus hall and filled part of each transition.
- Since then four changes moved the transitions, and none of them refit the fills:
  - c43 led the clarinet and bass clarinet joins 0.04 s earlier;
  - c44 made the stems dry;
  - c45 changed wind and horn legato velocities;
  - c46 led Oboe 1 0.04 s earlier.
- The jump in the table is at c44 and c45.
- **Bass clarinet 92.** The fill starts at the score onset (`pre_s` 0). The transition hole at qn 91.92-91.96 falls in the valley between the 91.5 and 92 fills: `vol_db` reads 5.65 at 91.87, 1.17 at 91.95 and 4.33 at 92.0. The fills now deepen the hole they were written to fill.
- **Clarinet 1 283.** The c38 B #3 CC7 dip (`score_config.py`, lines 820-821) was cut for a "4-5 dB bump" at v60. At c45's v88 the bump is gone: c41's stem rose 2 dB at the join, while c46's stem sits 6-10 dB low from +0.04 to +0.4 s.
- **Horn 1 230.** Since c45 the 229 mp peak is 3 dB louder and the 230 target body 2-3 dB softer, so the printed decrescendo (229 mp to 235 pp) drops 7 dB in one beat and then stays flat. A-weighted per beat: 229 -42.9, 230 -49.8, 231 -49.6, 232 -51.2 dB.

**Fix.** All of these are volume-envelope or CC7 changes on six tracks. They can be simulated on the c46 stems with `stem_fix.py` before the render.

**a. Refit the fills on the six wind and horn solo tracks.**
- Run `tools/auto_fills.py 46 cycles/c46/rendered_build/parts.json` with `build/auto_fills.json` "tracks"/"raise" limited to Flute 1, Oboe 1, Cor anglais, Clarinet 1, Bass clarinet and Horn 1 for this pass.
- My dry run on a scratch copy proposes these changes for those tracks:
  - **Retimes:** Bass clarinet 92 (`pre_s` 0.05); Horn 1 22 (`pre_s` 0.11); Flute 1 130 and 271; Oboe 1 143.
  - **New fills:** Bass clarinet 92.5 (+3.5 dB / 0.10 s) and 98; Flute 1 113.5 and 129; Oboe 1 146, 193.5, 199 and 269.5; Clarinet 1 175.5, 258, 259 and 270.5.
  - **Raises:** Horn 1 27, 39 and 176; Oboe 1 55.5, 57, 200 and 271; Bass clarinet 26; cor anglais 97 and 136; Clarinet 1 176 and 283.
  - Plus its own lowerings and removals where a fill overshoots.
- Keep an entry only if the simulated master dip at that join falls under about 4 dB and no front rises more than 2 dB over the louder body (the tool's overshoot rule).
- Do not `--write` the whole dry run. It proposes 125 changes on 14 tracks, mostly strings, and the c38 caution about `pre_s` fills lifting the previous note applies there. The string joins' master median is already 2.3-2.7 dB.

**b. Clarinet 1, bar 86.** Delete the four 283 points (282.6, 282.75, 283.1, 283.3) from the c38 B #3 `CC7_POINTS["Clarinet 1"]` row. Keep the 291.4-292.5 points.

**c. Horn 1, bar 68.** auto_fills does not flag 230, because its body window reads the decrescendo. Add `LEVEL_SHAPES["Horn 1"] += [[(229.95, 0.0), (230.1, 3.0), (230.85, 3.0), (231.0, 0.0)]]`. The target is a steady fall of about 3 dB per beat from 229 to 232 (229 -43, 230 about -47, 231 -49.6), with the 230 master dip under 4 dB. Check it against the existing 231 fill.

**Target.** No solo join dips 5 dB or more in the master. The median dip on the solo lines is back to 2.5 dB or less.

### 2. Woodwind entries speak 15-130 ms earlier since the c44 template mix: median 38 ms before the beat, and at bar 79 the winds lead the horns by up to 100 ms (measured; cause inferred)

**Where.** Every woodwind entry after a rest: 57 entries over 11 tracks. The clearest cases:
- Clarinet 1's coda solo entry at qn 280 (bar 85): -132 ms;
- Clarinet 1 at 175 and 262: -92 and -88 ms;
- Bassoon 1 at 196 and 229: -96 and -118 ms (c41: +36 and +16);
- Flute 2 at 262: -116 ms.

**Evidence.**
- Measure: the time each stem first reaches its body - 6 dB (body = median over +0.15..+0.6 s), against the score onset.
- Woodwind median by render: c41 -24 ms, c43 -24, c44 -40, c45 -38, c46 -38 ms. Entries more than 60 ms early: 4 in c41 and c43, 10 in c44-c46. The leads were unchanged across these renders.
- Brass (-20 to -23 ms) and strings (+4 to +10 ms) did not move.
- Per track, c46 against c41:

  | track | c46 | c41 |
  |---|---|---|
  | Flute 1 | -7 | -15 |
  | Oboe 1 | -38 | -16 |
  | cor anglais | -36 | -29 |
  | Clarinet 1 | -74 | -49 |
  | Clarinet 2 | -38 | -26 |
  | bass clarinet | -40 | -14 |
  | Bassoon 1 | -38 | +10 |
  | Bassoon 2 | -43 | -28 |
  | contrabassoon | -56 | -32 |

- The pcx perceived-attack estimator agrees: wind median -38 ms in c46 against -15 ms in c41.
- On the five entries where no other wind sounds (Oboe 1 54, Clarinet 1 175 and 280, Bassoon 1 229, contrabassoon 87), adding R Winds to the stem moved the estimate by 4 ms or less, so the master hears the same timing.
- **Bar 79 (qn 262, the ff downbeat).** Flute 2 -116, Clarinet 1 -88, contrabassoon -56, bass clarinet -44, Oboe 1 -38, cor anglais -36, Oboe 2 -30 ms, against the horns at -12/-14. That is a 104 ms spread on the cadence's main downbeat.
- **Cause (inferred).** The template's Close-led woodwind mics reach full level sooner than c41's Main-heavy wet stems. In Bassoon 1 at 229, the stem stands at -6 dB of its peak 0.10 s before the beat in c46, against -16 dB at the same point in c41.

**Fix.** Timing only, `--midi-only` on the 11 woodwind tracks. The leads respond about 1:1 (c43 LEARNINGS).

`build/score_config.py`:
- `ENTRY_LEAD_S["Bassoon"] = (0.03, 0.03)` (was 0.06) and `ENTRY_LEAD_S["Contrabassoon"] = (0.02, 0.02)` (was 0.06).
- `ENTRY_LEAD_ART_S = {"wind": {"Leg Slur MAX": 0.03, "Leg Slur": 0.04, "Sus Non Vib": 0.04, "Sus MAX": 0.02}, "Flute 1": {"Leg Slur MAX": 0.06, "Leg Slur": 0.11, "Sus Non Vib": 0.07, "Sus MAX": 0.05}, "brass": {}, "Bassoon": {}, "Contrabassoon": {}}`.
  - The previous wind values were 0.06 / 0.11 / 0.07 / 0.05.
  - "Leg Slur" is the clarinets' row.
  - Flute 1 keeps its values, since it is already at -7 ms.

`build/entry_leads.json`: delete Clarinet 1 "280" (0.06), Flute 2 "262" (0.10), Bassoon 1 "229" (0.10) and Bassoon 1 "196" (0.06).

After the build, check the wind entries' leads in parts.json, since `by_name` matches by substring.

**Predicted.**
- Wind median about -6 ms.
- No wind entry more than 60 ms early.
- Bar 79's wind spread goes from -116..-30 ms to about -18..+14 ms around the horns' -13 ms.
- The median spread at the 11 mixed tutti entries goes from 92 to about 80 ms. The rest is the late soft string entries, which this cycle should leave alone.

### 3. Bars 41-44: the cor anglais' "solo, dolce cantabile" shares the top with the flute's countermelody, printed one dynamic softer (measured)

**Where.** qn 124-139, cor anglais and Flute 1.

**What is wrong.** The printed balance:

| | at 124-126 | from 128 | from 136 |
|---|---|---|---|
| cor anglais (the solo) | p | mp | p |
| flute | pp, from 126 | p | pp |

In c46 the two are level. `check44`'s cor anglais margin over the rest of the orchestra here is 1.2 dB, the lowest of its nine wind and horn solo margins (the others are 3.2-8.0).

**Evidence.** A-weighted, per two beats, cor anglais minus flute:

| qn | c46 | c41 | c27 |
|---|---|---|---|
| 126 | +0.3 | +1.9 | +5.1 |
| 128 | +2.4 | +3.6 | +7.2 |
| 130 | -1.0 | -1.2 | +3.4 |
| 132 | +2.8 | +4.9 | +5.6 |
| 134 | +3.0 | +4.7 | +9.5 |
| 136 | +3.2 | +4.4 | +11.8 |
| 138 | -0.7 | -0.4 | +7.2 |

The flute's lift dates from c35 B #4: a +3 dB role over 125.75-131.5 and a +5 dB shape over 134.3-138, made when the flute sat 8-13 dB under. The c44 woodwind mic layout then moved about 1.5 dB further toward the flute.

**Fix.** In `build/roles.json`, change Flute 1 `[125.75, 131.5, 3, 0.5]` to `[125.75, 131.5, 1, 0.5]`. That is -2 dB on the flute's entry and its p phrase; it is level-only and can be done by stem fix.

**Target.** The cor anglais 2-4 dB over the flute at 126-133, and the `check44` cor anglais b41-44 margin at about 2.5 dB. Leave 134-138, where the cor anglais leads by 3 dB.

### 4. The final chord's 0.479 s to fall 20 dB is inside the recordings' range and is not a regression; if the 0.45 s guard stays, an exact fix exists (measured)

**Where.** The final chord, qn 301-304, master and the six string stems.

**Evidence.**
- **The data did not change.** Notes, CC11, the volume envelope and the tempo of the last 1.65 qn are identical to c45. The CC11 morendo goes 22 to 8 over the last 0.44 qn, which is 1.3 s at 20 bpm, and the master level before the note-off is -68.1 dBFS.
- **Celli.** Their dry release measures -6.5 dB at +0.3 s against -8.3 in c45.
- **Violins I.** -18.9 dB at +0.45 s against -19.8.
- **Why t20 moves.** Both stems cross -20 dB at 0.479 s. The crossing falls on the slow stretch of the 600 ms ppp release: -18 to -20 dB between 0.40 and 0.48 s, just before the cap ends. A 1-2 dB difference between release samples therefore moves t20 by 30-80 ms (c45 0.451, c46 0.479, c42 0.47).
- **The returns.** R Strings sits 15-19 dB under the dry stems here, so a return change does nothing, as c46 found.
- **Against the recordings.** Their cutoffs take 0.43-0.58 s to fall 20 dB, and this happens about 50 dB under the climax. I would leave it.

**Fix, if the 0.45 s guard is kept.** Add `LEVEL_SHAPES[name] += [[(304.0, 0.0), (304.1, -4.0), (306.0, -4.0)]]` for Violins I, Violins II, Violas, Violas div, Violoncellos and Double basses. 0.1 qn is 0.30 s at the final 20 bpm.

Simulated on the c46 stems, with the returns unchanged:

| | t20 | drop at +0.15 s | drop at +0.3 s |
|---|---|---|---|
| now | 0.479 s | 0.7 dB | 9.1 dB |
| -4 dB fade | 0.434 s | 2.6 dB | 13.0 dB |
| -6 dB fade | 0.419 s | | |

The fade lasts 0.3 s, so no ending falls 10 dB in 0.05 s. Because the sends are post-fader, the fade also lowers what the releases send into R Strings, so the rendered result will be slightly shorter than simulated (inferred).

Check that `apply_vol_tail_hold()` does not hold the fall (its `vol_tail_holds` should not list 304) and that the points after 304 reach REAPER's envelope. If they do not, apply the same fade as a stem fix with `--mix-only` after the render.

### 5. Horn 4, bars 29-30: a 5.5 dB role step inside its held pp E flat 3, on top of a loop period, makes the note dip 10 dB and swell back within 1 s (measured; audibility inferred as low)

**Where.** Horn 4, the tied pp E flat 3 from qn 84 to 90 (7.6 s).

**Evidence.**
- `roles.json` Horn 4 `[86, 90, -5.5]` steps the volume envelope from +0.9 to -4.3 dB between 85.5 and 86, under the sounding note.
- The stem falls from -49 to -59 dB at +2.3-2.5 s after the onset and comes back to -50.5 dB by +3.1 s as the sample swells.
- The note's 100-300 Hz envelope correlates 0.77 at the 3.95 s loop lag (SD 1.2 dB). c46 flagged this note for a listen-check.
- Horn 4 is among the three loudest stems in bar 30 (-53.4 dB against a master of -45.0). The master moves 1-2.5 dB over the same 2 s.

**Fix (optional).**
- Delete the role row.
- Add `LEVEL_SHAPES["Horn 4"] += [[(84.5, 0.0), (86.5, -5.5), (90.0, -5.5), (90.5, 0.0)]]`. This keeps the bar 30 level, but the fall takes 2.3 s instead of 0.6 s.
- Simulate on the stem. Keep it if the stem's largest 1 s swing inside the note drops under 5 dB.

## Weakest passages now, and what still sounds like a machine

Ranked by what a listener would notice.

1. **Bars 31-36, the bass clarinet solo.** The woodwinds play alone, and the slurred eighths of bar 31 have 7-8 dB holes (finding 1).
2. **Bars 65-70, the Horn 1 retransition.** The decrescendo after the mp peak is one 7 dB drop at 230 (finding 1).
3. **Bars 17-22, the solo violin.** It is played by the DIV A half section, so it is still a section sound with chorus, not one player. This is a library limit: the fix is Hollywood Solo Violin, licensed but not installed (`MANUAL-GAPS.md` #3). That is Dan's decision, not a c47 change.
4. **Bars 41-44.** The cor anglais solo is level with the flute (finding 3).
5. **Bar 79's ff downbeat, and the B section's entries at 108, 124 and 188.** The woodwinds speak 30-120 ms ahead of the horns and strings (finding 2).
6. **The horn theme, bars 7-14.** Joins at 23, 35 and 37.5 dip 5-6 dB (finding 1).

The strongest passages:
- the animando and climax, bars 53-64: climax order kept, Trombone 1's accents +5.7 dB over the pickup with the 2-5 kHz attack 13 dB under the body;
- the coda balance: Clarinet 1 7.8 dB over the cor anglais;
- the rubato: every slow beat sits on a breath or a printed rit;
- the held chords: no loop periodicity in the master.

Machine traits, in order:
1. holes inside slurs on the solo lines;
2. winds entering ahead of the band since c44;
3. the half-section "solo" violin.

The expert files' entry spread (36-55 ms, `EW-TEMPLATE-PLAN.md` section 8) is not needed. The tutti entries already spread a median 92 ms by the body - 6 dB measure, with the winds early and the soft strings late, so the work is to tighten them, not to spread them.

## Changes for c47, in order of effect
1. Finding 1: the fill refit on the six solo wind and horn tracks, the Clarinet 1 283 CC7 points removed, and the Horn 1 230 shape.
2. Finding 2: the woodwind entry leads lowered and the four per-onset extras deleted.
3. Finding 3: Flute 1's 125.75-131.5 role from +3 to +1 dB.
4. Finding 4, only if the 0.45 s guard is kept: the -4 dB fade after 304 on the six string tracks.
5. Finding 5, optional: Horn 4's role made into a 2 qn fall.

All five can be simulated on the c46 stems before taking the lock. Only finding 2 changes timing.

**Do not touch:**
- the hall and returns (R Strings -17.97, R Brass -4.97, IR envelope 0.5, low-instrument sends off) and the mic layout;
- the release caps (strings 600/300 ms, basses 400, horns 237/350);
- the c46 tempo map, the caesuras and `CAESURA_BREATH_S` 0.34;
- Trombone 1's accent handling;
- the CC16 round-robin reset;
- the climax order (delivered bars 61-62 at -18.3 against bars 79-80 at -20.5 / -20.2);
- the coda balance (Clarinet 1 7.8 dB over the cor anglais);
- the pinned re-bow points and their fills (master loop autocorrelation -0.33 to 0.15);
- the mute placement;
- the string join fills (the string tracks stay out of the auto_fills pass).
