# Cycle 16, critic C: holistic comparison, with the per-note volume envelope first

Under review: the c15 render (`cycles/c15/render`, 35 stems and the master) and the data that produced it (`cycles/c15/rendered_build/parts.json`, identical to `build/parts.json`). Compared with the c00, c10 and c14 masters, Movement I's c55 master, the Dvořák 9/i file and the stored Brahms spectra (`symphony/render/critics/c04/ref_brahms*_musopen/metrics.json`; their audio is not on disk).

Method for the envelope. I ran a copy of `tools/score_to_parts.py` in my scratch folder that tags every `vol_parts` item with the rule that wrote it. Its parts.json is byte-identical to the rendered one. I then rebuilt each track's envelope with `build_reaper.py`'s own `vol_points()` for any subset of rules (the rebuilt full envelope matches the written one within 0.02 dB). "Slow layers" below are roles, hairpin gain, held decrescendos, the dynamic and soft trims, divisi cuts, unison boosts, the timpani roll levels and settle, and the final fade. "Per-note layers" are everything else. "Without" values are the stem level minus the per-note layers' mean over the same window, which is exact for the dry stems because the envelope is a gain after the instrument.

## Manual notes

Third round: I read the pages behind the first priority (PDF pages 53-54, 64, 93, 150-151 of the May 2021 manual) and `loop/MANUAL-GAPS.md`.

| Manual (PDF page) | Where it applies | Does the render follow it |
|---|---|---|
| Velocity is the control for short articulations, because it cannot change inside a note; CCs are for sustained notes (p.53, p.64, p.150) | Staccato quarters of the first theme (bars 11-34, 151-166), timpani strokes, the basses' eighths | No. The staccato-row notes play at velocity 118 and are then turned down 3-14 dB each by a fader step (`steady_levels.json`); 296 of the basses' 338 notes of an eighth or less have 3 dB or more of fader movement inside them (finding 1, 2) |
| "Volume should be used to set a loudness level relative to other instruments, while Expression should be used to shape the continually changing dynamics" (p.64); CC7 is "the overall upper limit ... as opposed to shaping an individual musical line" (p.151) | Every track's volume envelope | Half. The slow layers do the manual's job for volume. 68 % of the envelope's travel is inside single notes (finding 1) |
| CC11 "can provide the kind of dynamic shaping of notes to create swells in the middle of a note, or over the course of a phrase" (p.151) | Accent swells, slur-pair releases, arrival weights (1,197 shapes) | No: they are fader shapes. The reason is on record (CC11 at f-ff hardly changes level; a CC11 bump into the top layer was heard as harsh), so this is a measured exception, but the size is not: 25-71 % of accents per track stand more than 4 dB over their neighbours (finding 1) |
| Basses (and Violins II) have a Marcato Long row beside Marcato Short: "the same strong attack but a slightly longer duration"; Marcato is 4 round robins, Staccato and Staccato On Bow 9 (p.93; DIGEST lines 154, 193) | The basses' repeated eighths, bars 199-210 and 247-277 (267 notes on "Sus MAX") | Not used. The eighths play the sustain row with a 9-10 dB fader dip before each one (finding 4) |
| Note velocity maps to dynamic layers, e.g. p 1-25, mp 26-45 (p.150) | Any level moved from the fader into velocity | To check in the range test: a velocity change on the staccato rows may cross a layer and change the tone. Measure 2-5 kHz with the level |
| MANUAL-GAPS items 1, 2, 5, 11 (brass marcato attack, re-tongue rows, expressive rows, wind staccato rows) | Unchanged since c13-c15 | Open; not re-tested here |

## Findings

### 1. The volume envelope: what Dan saw, why it is there, where it helps, and a plan (measured; the plan's effect is simulated on the c15 stems)

**What is in the project.** 53,696 volume points on 31 tracks, 127 points per second in all. The five string tracks carry 3,946-6,917 points each (9.3-16.3 per second, 4.8-10.0 per note); the winds and brass 264-2,246 (0.6-5.3 per second). The reference projects have 0.01-0.36 points per second and EastWest's templates none. 2,349 of 9,061 notes swing 3 dB or more inside the note; 1,439 of them (61 %) carry a mark that asks for it (accent, tenuto, sf, fp, a dynamic inside the note or a hairpin over it) and 910 (39 %) do not. 68 % of the envelope's travel is inside single notes (22,046 dB inside notes against 10,574 dB between successive note means; strings 65 %, winds 66 %, brass 70 %, timpani 89 %).

| track | points | per s | per note | range inside a note, median / p90 dB | step between notes, median / p90 dB | travel inside notes | notes ≥ 3 dB | of them marked | notes ≤ an eighth with ≥ 3 dB |
|---|---|---|---|---|---|---|---|---|---|
| Violins I | 3946 | 9.3 | 5.7 | 0.7 / 4.3 | 0.6 / 3.7 | 60 % | 143 | 89 | 28 of 280 |
| Violins II | 4002 | 9.4 | 4.9 | 0.5 / 3.4 | 0.3 / 3.7 | 61 % | 125 | 98 | 10 of 331 |
| Violas | 4074 | 9.6 | 4.8 | 0.6 / 3.1 | 0.3 / 4.2 | 61 % | 171 | 87 | 15 of 312 |
| Violoncellos | 4135 | 9.8 | 6.8 | 0.6 / 5.5 | 0.7 / 4.7 | 63 % | 147 | 95 | 9 of 128 |
| Double basses | 6917 | 16.3 | 10.0 | 3.0 / 5.9 | 1.6 / 4.3 | 73 % | 435 | 138 | 296 of 338 |
| Flute 1 | 2120 | 5.0 | 4.6 | 0.0 / 4.0 | 0.2 / 3.5 | 61 % | 101 | 79 | 9 of 120 |
| Oboe 1 | 2246 | 5.3 | 6.2 | 1.6 / 5.0 | 1.1 / 3.9 | 65 % | 143 | 79 | 21 of 75 |
| Clarinet 1 | 2109 | 5.0 | 3.4 | 0.0 / 3.5 | 0.0 / 2.2 | 65 % | 87 | 69 | 4 of 97 |
| Bassoon 1 | 2122 | 5.0 | 4.4 | 0.0 / 3.5 | 0.0 / 2.3 | 65 % | 92 | 65 | 2 of 87 |
| Horn 1 | 1923 | 4.5 | 5.4 | 0.0 / 5.8 | 0.6 / 3.4 | 66 % | 106 | 55 | 18 of 48 |
| Trumpet 1 | 1161 | 2.7 | 5.8 | 0.1 / 4.4 | 0.2 / 2.8 | 68 % | 39 | 26 | 4 of 24 |
| Trombone 1 | 1290 | 3.0 | 7.6 | 1.7 / 6.0 | 0.8 / 3.5 | 72 % | 59 | 40 | 11 of 17 |
| Tuba | 997 | 2.4 | 8.0 | 2.1 / 5.0 | 0.5 / 2.8 | 76 % | 33 | 28 | 5 of 11 |
| Timpani | 1798 | 4.2 | 10.0 | 6.0 / 8.7 | 0.4 / 2.8 | 89 % | 157 | 81 | 42 of 53 |
| other 15 pitched tracks | 16,727 | 0.2-4.7 | 0.4-10.2 | 0.0-2.2 / 0.1-7.4 | 0.0-1.1 / 0.1-5.3 | 37-73 % | 511 | 419 | 22 of 432 |

**Where the points come from** (marginal points: the count that disappears when the rule is switched off).

| rule | kind | shapes | tracks | points | largest dB |
|---|---|---|---|---|---|
| dynamic and soft trims, gain, tail holds (`mix.json`, `build_reaper.py`) | slow | - | 31 | 18,654 | - |
| accent swells (`GENTLE_ACCENT`, `ACCENT_DB_AT`) | per note | 1,038 | 27 | 8,854 | 5.4 |
| hairpin gain | slow | 431 | 27 | 6,873 | 7.0 |
| roles | slow | 245 | 29 | 1,962 | 12.0 |
| repeated-note detach dips, strings (`STR_REP_DETACH`) | per note | 493 | 2 | 1,318 | 10.0 |
| re-bow fills | per note | 24 lists | 5 | 1,270 | 10.0 |
| `STEADY_LINE` level steps (`steady_levels.json`) | per note | 506 notes | 5 | 1,042 | 14.0 |
| pitch trims | per note | 373 | 6 | 962 | 6.0 |
| `LEVEL_SHAPES_S` (fronts, notches, start shapes) | per note | 171 | 17 | 893 | 18.0 |
| divisi and chord cuts | slow | - | 5 | 787 | 11.8 |
| unison boosts | slow (flat per note) | 579 | 13 | 700 | 10.8 |
| timpani attack lift on f strokes and rolls | per note | 149 | 1 | 666 | 8.8 |
| metric steps on bowed and timpani eighths | per note | 365 | 4 | 586 | 3.0 |
| slur-pair release | per note | 107 | 24 | 571 | 3.0 |
| row trims | per note | 232 | 4 | 502 | 4.5 |
| `LEVEL_SHAPES` | per note | 49 | 17 | 492 | 7.0 |
| arrival weight | per note | 52 | 26 | 455 | 2.0 |
| held decrescendo | slow | 96 | 14 | 440 | 6.0 |
| note trims | per note | 90 | 10 | 413 | 9.0 |
| wind / brass detach dips | per note | 109 | 11 | 314 | 5.0 |
| the rest (final fade, long-note swell, timpani settle and roll trims, unison fades, tenuto swell) | mixed | 79 | - | 525 | - |

**The answer for Dan, in three parts.**
1. This score prints 1,109 accents. Each one is played as a rise and fall of 2.5-5.4 dB in the fader (1,038 shapes, 8,854 points), because CC11 hardly changes level at f-ff and the library's accent samples were heard as harsh. Where every note of a figure is accented, the fader peaks on every note.
2. The library's rows and pitches differ in level, so levels were fitted note by note: `steady_levels.json` (-14.0 to +9.0 dB on 506 notes of the first theme), pitch trims, row trims, note trims.
3. Repeated notes are separated with the fader: a 5-10 dB dip before each of the basses' 493 repeated eighths (1,318 points on that one track) and a lift on each loud timpani stroke.
A fourth part is only drawing: the slow layers are written as stairs on a grid of an eighth of a quarter note, so a hairpin shows as 30 or more points. 33,565 points remain with every per-note layer off. Thinning collinear points (0.1 dB tolerance) takes the present envelope from 53,648 to 34,936 points and the slow-only envelope to 15,415, with no change in sound.

**Does it help?** Stem level over the first 0.35 s of each note; median step between abutting notes (p90, count over 6 dB) with the envelope, without the per-note layers, and with them capped at ±3 dB.

| passage, track | pairs | with | without | capped ±3 | verdict |
|---|---|---|---|---|---|
| first theme 11-26, Violins I | 49 | 1.93 (5.1, 3) | 1.56 (6.1, 5) | 1.98 (5.1, 2) | level SD 2.42 / 3.37 / 2.37: the cap keeps the gain |
| first theme 11-26, Violins II | 53 | 1.48 (3.4, 1) | 1.21 (4.3, 2) | 1.46 (3.3, 1) | SD 1.89 / 2.20 / 1.93: the cap keeps the gain |
| first theme 11-26, Violas | 71 | 1.95 (3.9, 1) | 1.27 (4.2, 0) | 1.37 (4.1, 0) | SD 3.57 / 6.53 / 4.23: helps, needs more than 3 dB |
| first theme 151-170, Violas | 60 | 1.48 (4.0, 2) | 2.06 (4.4, 1) | 2.01 (4.4, 1) | helps |
| first theme 11-26 and 151-170, Horn 1 | 53, 54 | 2.77, 3.02 | 2.31, 2.79 | 2.77, 3.02 | hurts a little (accent swells) |
| counterstatement 27-34, Violoncellos | 27 | 3.62 (6.5, 4) | 2.33 (7.2, 5) | 2.16 (3.9, 0) | hurts as written; capped is best (SD 2.95 / 3.59 / 2.05) |
| counterstatement 27-34, Double basses | 27 | 1.76 (4.2, 0) | 2.52 (8.4, 6) | 1.86 (4.1, 2) | helps (SD 1.71 / 4.38 / 2.87) |
| second theme 67-82 and 187-198, Violins I, II, Violoncellos | 30-47 | 1.2-2.6 | within 0.3 of "with" | same | does nothing (mean per-note layer 0.1-0.5 dB) |
| trumpet solo 51-66, transition solos 43-50, cor anglais 171-186, chorale 223-234, coda 2 | 8-40 | 0.5-3.6 | equal | equal | does nothing (no per-note layer there, except Oboe 1 0.4 dB) |
| muted Trumpet 1, 171-186 | 22 | 1.80 | 3.17 | 1.80 | helps (note trims and level shapes of 0.5 dB mean) |
| bassoon solo 115-124 | 19 | 1.56 (3.1, 0) | 1.82 (4.6, 1) | 1.59 (3.4, 0) | helps; the cap keeps it |
| codetta 91-98, Trumpet 1 / Trombone 1 | 6 | 6.52 / 4.09 | 4.39 / 1.18 | 6.52 / 3.95 | hurts (accent swells on the chords) |
| coda 199-210, Violas | 43 | 3.88 (7.3, 12) | 2.88 (5.7, 3) | 3.09 (7.2, 11) | hurts |
| coda 199-210, Timpani | 5 | 2.12 | 4.27 | 3.01 | helps |
| Più allegro 247-270, Violins I | 75 | 2.14 (4.0, 3) | 1.44 (4.4, 4) | 1.87 | hurts a little |
| Più allegro 247-270, Violoncellos | 68 | 3.08 (6.5, 10) | 2.76 (6.7, 8) | 2.70 | hurts a little |
| Più allegro 247-270, Double basses | 176 | 4.02 (5.1, 9) | 3.12 (4.5, 5) | 3.14 | by design (metric steps and dips); see finding 4 |
| Più allegro 247-270, Trumpet 1 | 31 | 1.95 (4.9, 0) | 2.20 (6.1, 4) | 2.03 | helps |

Accents (level of an accented note over its unaccented neighbours, first 0.35 s; Dan's rule is 2-4 dB): with the envelope the medians are Violins I +2.7, Violins II +2.7, Violas +3.7, Violoncellos +3.9, Double basses +5.6, Flute 1 +4.1, Oboe 1 +2.4, Clarinet 1 +3.8, Bassoon 1 +2.8, Horn 1 +4.2, Trumpet 1 +1.9, Trombone 1 +3.1, Tuba +3.1; without the per-note layers +0.9, +0.3, +1.6, +2.6, +3.0, +1.4, -0.3, +1.5, +0.4, +2.0, -0.4, +0.6, +1.0. So the accent swell is needed. But the spread is wide (p10 to p90 about -1 to +8 dB) and 25-71 % of the accents per track stand more than 4 dB over their neighbours (Double basses 71 %, Flute 1 54 %, Horn 1 54 %, Violas 46 %, Violoncellos 45 %), while 12-34 % stand under +1 dB.

Balance does not depend on the per-note layers (movement RMS per stem without them): within 0.7 dB on 25 of 29 tracks; Oboe 1 +1.8, Harp +1.6, Violoncellos +1.3, Timpani -2.9 dB. With the cap at ±3 dB every track is within 0.4 dB except Harp +0.8 and Timpani -1.4.

**Plan for the actor's range test** (three states per passage: current, per-note layers off, capped ±3 dB; ranges 37-138, 598-682, 790-842, 982-1082).
- Keep as they are, with the measurement that justifies each: re-bow fills (Movement I's result; not re-measured here), unison boosts and divisi cuts (structural), pitch trims and note trims as one level per note (bassoon solo 1.56 against 1.82 without; muted trumpet 1.80 against 3.17), the timpani attack lift (2.12 against 4.27) and roll shapes, the basses' level steps in 104-136 (1.76 against 2.52, steps over 6 dB 0 against 6).
- Cap at 3 dB: the sum of the per-note layers on any accented note (`score_to_parts.py`: a new `PER_NOTE_CAP_DB = 3.0` applied to the per-note part of `vol()` in the note's first 0.5 s; start value for `GENTLE_ACCENT["string"]["db"]` on the Double basses 1.5 and on Violas / Violoncellos 2.0, the others unchanged). Target: accent over neighbours p90 under +5 dB, median 2-4 dB, share under +1 dB not larger than now.
- Cap at 3 dB: `steady_levels.json` on Violins I, Violins II and Violoncellos (the capped state measures as even as the fitted one; table above). Violas and Double basses keep larger steps only on notes where finding 2 does not move the level into velocity.
- One level per note on notes of an eighth or less (no shape inside): 4,350 points lie inside such notes, 2,090 of them on the basses. By construction this does not change the level over the note (the measurement window covers the whole note); it removes the visible saw-tooth.
- Remove: accent swells on the codetta chords 360 / 364 / 369 for Trumpet 1 and Trombone 1 (6.52 and 4.09 against 4.39 and 1.18 without; `ACCENT_DB_AT` 0 there), and the per-note layers on Violas in 792-816 (steps over 6 dB 12 against 3 without).
- Move to CC11: slur-pair releases (107 shapes of -3 dB) and arrival weights (52 of +2 dB). Both are shapes inside a held note at levels where CC11 still acts (manual p.151); the research files show the taper in the CC lane.
- Move to velocity: the staccato-row levels of the first theme (finding 2) and, if the short-row test of finding 4 passes, the basses' metric steps and detach dips (1,758 points).
- `build_reaper.py vol_points`: thin collinear points before writing (keep a point only if the line through its neighbours misses it by more than 0.1 dB). Expected: 53,648 to about 34,900 points now, and to about 15,000-20,000 after the items above; no audible change. Check by rendering nothing: compare the interpolated envelope before and after on a 5 ms grid (largest difference 0.1 dB).

### 2. Level steps of up to 18 dB are placed on the moved note-on and cut the note before (measured)

Where: the `STEADY_LINE` spans (Violins I, Violins II, Violas 40-104 and 600-680; Violoncellos, Double basses 104-136), and single trims elsewhere (Double basses 272; Trumpet 1 989).

What: `steady_levels.json` gives each note its own level. Successive values differ by up to 18.4 dB (Violoncellos 125.5 +4.4, 126 -14.0, 127 -13.6; 113 +3.8, 113.5 -10.2; Double basses 107.5 +1.8, 108 -9.4; Violins I 75.5 +3.0, 76 -8.4; 619.5 -0.5, 620 -9.4). 52 notes have 6 dB or more. The step is written at the next note's moved note-on, 30-96 ms before the beat, while the note before still sounds (it ends 20 ms after that note-on and then releases under the 150 ms cap). The step therefore cuts the end and the release of the earlier note and its hall send.

Evidence (20 ms frames, lowest level from 80 ms before to 120 ms after the join against the lower of the two note bodies; "without" divides the per-note layers out of the stem):
- Joins where the per-note envelope moves 2 dB or more: holes over 6 dB with / without: Violins I 11 / 3 of 70, Violins II 5 / 2 of 96, Violas 12 / 4 of 85, Violoncellos 13 / 11 of 87, Trombone 1 2 / 0, Trumpet 1 2 / 0. Double basses 39 / 10 of 121, which includes the deliberate dips before repeated eighths. Joins where the envelope does not move show no difference (Violins I 10 / 10, Violas 13 / 10).
- Single cases, hole with / without: Violoncellos 126 15.5 / -0.5 dB, 113.5 13.9 / 2.5; Violins I 76 9.8 / -0.5, 42 8.6 / 2.1, 620 6.7 / 1.3, 97.5 10.0 / 5.1; Double basses 108 10.8 / 2.4, 124 14.6 / 6.2, 126 11.3 / 4.1, 272 9.4 / 2.1 (note and pitch trims ending at the note-on); Violas 78 7.2 / 2.2; Trumpet 1 989 9.3 / 2.5 (`LEVEL_SHAPES` +7 ending 10 ms before the note).
- The largest negative values sit on the staccato-row notes, which play at velocity 118: their raw level is 3.6-10 dB over the "Sus MAX" notes around them (Violoncellos -35.2 against -39.1 dB; Violas 151-170 -34.2 against -44.4).

Fix (the manual's tool for a short note is its velocity, p.53, p.64, p.150):
1. `build/score_config.py`, c15 block: give the staccato-row notes of the spans a velocity table instead of a level step. Start: velocity 118 -> 100 where the fitted step is -3 to -6 dB, -> 88 where it is -6 to -10, -> 78 below -10 (the slope is not on record for "Stac RRx9" / "Staccatissimo RRx9": measure it on the first range render from these three values, then refit). Delete those notes' rows from `steady_levels.json` and refit the remainder with `actor_scripts/fit15.py`, capped at ±3 dB. Check 2-5 kHz over the first 80 ms of the strokes against c15 (a lower velocity layer must not turn them dull: within 3 dB).
2. `tools/score_to_parts.py`, the `STEADY_LINE` `level_db` item (line 5245) and `trim_shape` (note and pitch trims): a step between two notes becomes a linear crossfade from the new note's moved note-on to its score onset (at least 40 ms), not a step at the moved note-on. For a fall of more than 3 dB after a slurred note, start the crossfade at the earlier note's note-off.
3. Trumpet 1 989: end the +7 dB shape of 988 at the note's own note-off (now 10 ms before the next note-on, 24 ms after its own end).

Target: no join in the spans with a hole more than 3 dB deeper than without the envelope (now 16 on the four upper string tracks and celli); the spans' level SD not above the c15 values (Violins I 2.42, Violins II 1.89, Violas 3.57 in bars 11-26).

### 3. The bottom octave has thinned since c00 and the octave above it has grown: Dan's "mushy" (measured; the fix is simulated)

Where: whole movement; Double basses, Violoncellos, Tuba, Contrabassoon.

Evidence, band shares of total energy (dB):

| | 32-56 Hz | 56-112 Hz | 112-140 Hz | 140-355 Hz |
|---|---|---|---|---|
| c00 | -31.2 | -11.8 | -18.4 | -8.3 |
| c10 | -29.1 | -13.5 | -17.5 | -6.7 |
| c15 | -28.8 | -14.1 | -17.1 | -6.6 |
| c15 soft third / loud third of frames | -27.5 / -29.1 | -13.0 / -14.3 | -15.1 / -17.3 | -5.7 / -6.7 |
| Movement I c55 | -31.5 | -14.6 | -17.8 | -6.3 |
| Brahms 1/ii, 4/ii (stored third-octave spectra) | - | -7.9, -7.3 | - | -9.1, -8.5 |
| Dvořák 9/i (lossy file) | -42.0 | -18.2 | -14.0 | -6.1 |

The 140-355 Hz band is 7.5 dB over the 56-112 Hz band; in c00 it was 3.5 dB over and in the Brahms files it is 1.2 dB under. (Both Brahms movements are slow and in E major; treat their 56-112 Hz value as an upper bound, not a target.)

Who carries the bands (c15 stems, loud third): 56-112 Hz: Double basses 48 %, Violoncellos 29 %, Timpani 8 %, Bass clarinet 6 %, Tuba 3 %, Contrabassoon 1 %, Bass trombone under 1 %. 140-355 Hz: Violoncellos 16 %, Violas 10 %, Tuba 8 %, Horn 3 8 %, Double basses 8 %, Horn 1 7 %. In the soft third the basses carry 69 % of 56-112 Hz.

Summed EQ gain at the fundamentals (track EQ + mute_eq + family EQ + master high pass; RBJ models of the ReaEQ bands, so ±0.5 dB; second value with `loud_eq` on):

| | G1 49 | B1 62 | C2 65 | D2 73 | E♭2 78 | F2 87 | G2 98 | C3 131 | G3 196 |
|---|---|---|---|---|---|---|---|---|---|
| Double basses | -3.1 | -6.6 / -6.8 | -3.4 / -3.7 | -5.8 / -6.4 | -4.0 / -4.9 | -12.0 / -14.1 | -1.7 / -4.8 | +1.9 / +3.1 | -0.3 / +1.7 |
| Violoncellos | - | - | -1.0 / -0.7 | +0.1 / +0.6 | +0.7 / +1.3 | +1.7 / +2.6 | +2.9 / +4.1 | +5.1 / +7.7 | +3.7 / +5.5 |
| Tuba | -4.4 | -3.1 | -3.0 / -2.7 | -3.7 | -4.9 | -6.8 / -6.1 | -4.4 / -3.5 | -5.5 / -3.5 | -5.4 / -4.4 |
| Contrabassoon | -5.1 | -3.4 | -3.0 | -2.3 | -2.0 | -1.5 | -1.1 | -0.6 / +1.3 | -0.7 |
| Bass trombone | -3.8 | -1.9 | -1.6 | -1.2 | -1.1 | -0.9 | -0.9 | -1.2 / +0.8 | -2.4 |
| Timpani | -4.5 | -2.5 | -2.2 | -1.8 | -1.7 | -1.7 | -1.7 | -2.4 | -3.9 |

The basses' tonic C2 is 5.3-6.8 dB under its octave C3, and the celli's 6.1-8.4 dB: the EQ moves the weight of every bass note up an octave, into the band that is already too full. The bands: Double basses `eq` bell 150 Hz +4 (1 oct) and bell2 87.3 Hz -12 (0.15 oct), `mute_eq` 61.7 Hz -5 and 73.4 Hz -4 (0.12 oct), family bell 240 Hz -3, high pass 35 Hz, `loud_eq` 160 Hz +3 and 98 Hz -4; Violoncellos `eq` 170 Hz +3 (1.5 oct) and 125 Hz +3, `loud_eq` 150 Hz +3, family high pass 53 Hz; Tuba `eq` 84 Hz -5 (0.2 oct), family bell 143 Hz -4.3, high pass 41 Hz, `loud_eq` 140 Hz +2; Contrabassoon low shelf 70 Hz -4, `loud_eq` 140 Hz +2; Bass trombone and Bassoon 2 `loud_eq` 140 Hz +2 / +1.5; Timpani family high pass 44 Hz; Bass drum high pass 25 Hz.

Fix (`build/mix.json`), simulated on the c15 stems with the `loud_eq` spans switched as in the project:
- Double basses: `eq` 150 Hz +4 -> +1; 87.3 Hz -12 -> -9; `mute_eq` 61.7 Hz -5 -> -2, 73.4 Hz -4 -> -2; `loud_eq` 160 Hz +3 -> 0, 98 Hz -4 -> -1.5; add a low shelf 90 Hz +3.
- Violoncellos: `eq` 170 Hz +3 -> +1, 125 Hz +3 -> +1.5; `loud_eq` 150 Hz +3 -> 0; `gain_db` +1.5 (the stem falls 2.7 dB without it).
- Tuba: remove the 84 Hz -5 bell; add a low shelf 110 Hz +3; `loud_eq` 140 Hz +2 -> 0.
- Contrabassoon: low shelf 70 Hz -4 -> 0; `loud_eq` 140 Hz -> 0. Bass trombone, Bassoon 2: `loud_eq` 140 Hz -> 0.
- Timpani and Bass drum unchanged (rolls must not drown the parts).

Simulated result (before the celli make-up): 56-112 Hz -14.1 -> -13.0 (soft third -13.0 -> -11.6, loud third -14.3 -> -13.3), 32-56 Hz -29.0 -> -26.4, 112-140 Hz -17.1 -> -18.8, 140-355 Hz -6.6 -> -7.1; the gap between the two main bands 7.5 -> 5.9 dB. Per second the 56-112 Hz band rises 2.4 dB at the median, 4.0 at p90, 6.6 at most, and in no second does it come within 3 dB of the total, so it stays "solid but not boomy" on this measure. Check after the render: no bar where Double basses' F2 is more than 4 dB over its neighbours (the reason for the 87.3 Hz bell); the tail's 60-250 Hz share at the stops not more than 2 dB over c15.

This closes a third of the distance to c00's balance. The rest is level, not EQ: the tuba, contrabassoon and bass trombone together hold under 5 % of the band, so a second step would be a +2 dB role for Tuba and Contrabassoon in the ff tuttis (bars 27-39, 199-204, 247-262), tested after this one.

### 4. The weakest passages are now the coda 1 and the Più allegro (bars 199-210, 247-270): the theme there is still on mixed rows and the basses' eighths are made with the fader (measured; the fix follows c15's result on the first theme)

Evidence:
- Timing on S (c15 table): bars 247-270 54 / 19 of 120 notes outside 25 / 60 ms (45 % / 16 %, the worst segment; Horn 1 22 / 8 of 45, Trombone 1 20 / 7 of 41, Trumpet 1 12 / 4 of 34), bars 199-210 51 / 9 of 151. The first theme after c15: 31 % / 7 % and 28 % / 5 %. The string theme lines of 247-270 are not among the 29 measured lines.
- Rows: the first theme's head returns in 792-816 and 984-1056 on Violins I, Violins II, Violas and Violoncellos, still as "Leg Slur MAX" / "Leg BC MAX" / "Sus MAX" changes: 14 changes onto a legato row in 792-816 (4, 4, 4, 2) and 63 in 984-1056 (8, 14, 23, 18), with leads up to 0.45 qn. In 40-104 the three upper tracks have 0, 0 and 1 after c15 (the celli still 3). Trombone 1 has 9 changes onto the legato row in 984-1056.
- Note-to-note steps (finding 1's table): Violas 199-210 3.88 dB with 12 steps over 6 dB; Violoncellos 247-270 3.08 with 10; Double basses 247-270 4.02.
- The basses' 267 repeated eighths (792-840, 984-1108) play "Sus MAX" at one velocity (91), 65 % of the slot, with a fader dip before each (median dip between eighths 9.4-9.6 dB on the stem) and metric steps: 1,758 envelope points. Six cycles of work on them are on record (c01, c09-c12, c15), and c15's own conclusion is that the up-bow take "rises slowly whatever the note-on" (off-beat rise +50 / +68 ms). The sample class is the limit.
- The other strings' eighths in these bars are full length (length / slot 0.98-1.06) with a 5-6 dB dip between them; the clarinet, bassoon and trombone eighths 2.9-3.7 dB (83 % under 6 dB). Inferred: the figures read as a continuous band, not as separate strokes, at the movement's loudest point.

Fix:
1. `build/score_config.py`: `STEADY_LINE` "Sus MAX" spans on Violins I, Violins II, Violas and Violoncellos over 792-816 and 984-1056, built like the c15 spans (staccato quarters on their rows, accented halves as their own class, `overlap_s` 0.02, `gap_s` 0.03). Start leads: the 600-680 classes in `build/steady_leads.json`; fit on two range rounds (790-842, 982-1082). Add these four lines to the S table. Target: under 35 % outside 25 ms and under 8 % outside 60 ms on each.
2. Range A/B on the basses' eighths, 792-840: "Stac On Bow RRx9" and "Marc Shrt RRx4" (both in the Basses KS Master's default rows; "Marc Lng RRx4" is there unloaded; manual p.93), note length 55-60 % of the slot, velocity by position in the beat 110 / 88 / 98 / 88 with ±5 seeded variation (research batch 7), no detach dips and no metric steps in the fader. Measure at the fundamental (30-120 Hz): dip before each beat (now 9.5 dB), rise time on and off the beat (off-beat now +50 to +68 ms late), level within 2 dB of c15 per bar. Adopt the row that separates by 6 dB or more with the off-beats within 25 ms; then the same on 984-1108.
3. Trombone 1 984-1056 on one row ("Sus MAX", re-tongued) as a range test against its 20 / 7.

### 5. Stops at bars 2, 6, 113 and 166 fall too fast: lift the hall returns after the cut-off only (measured; the gains are computed from the stems)

Evidence (my windows: 0.3 s before the stop against 50 ms centred 0.3 s after it; they read 1.5-2 dB lower than the actor's, so the gains below are converted to the actor's numbers). Before each stop the four return stems together are 11.2-13.5 dB under the dry stems (bar 2 -12.0, bar 6 -12.6, bar 94 -11.2, bar 113 -13.5, bar 166 -12.5, bar 204 -12.7). At +0.3 s dry and returns are about equal (bar 2: dry -36.9, returns -36.2 dB; bar 113: -38.0 / -39.0; bar 166: -37.5 / -38.5). The dry stems fall 20 dB in 0.3 s (150 ms release caps at f-ff, no send on basses and low brass), and bar 113's chord has the weakest hall because its weight is in the tracks without a send. At bar 204, which meets the limit, the celli alone hold -36.3 dB at +0.3 s.

Fix: do not raise sends or the returns' level in general (the wetness ceiling). Lift only the tail: a volume shape on the return tracks that starts at the stop (`mix.json` returns, a new key such as `"tail_lifts": [[stop qn, dB]]`, written by `build_reaper.py` as the return track's volume envelope; 0 dB up to the stop, the lift reached 50 ms after it, held until 0.1 s before the next entry, then back to 0). Gains that bring the drop to 17 dB on the actor's measure, from the power sums above: bar 2 (stop at qn 5.0) +1 dB, bar 6 (21.0) +2 dB, bar 166 (661.9) +2.5 dB, bar 113 (449.9) +6 dB; start bar 113 at +4 dB and measure. The same shape can be tried first on the four return stems with `tools/stem_fix.py`, without a render. Checks: each stop 14-17 dB at +0.3 s; time to -20 dB still 0.50 s or less (now 0.29-0.39 s at these four, so there is room); bars 94 and 204 unchanged.

For bar 166 the alternative is to end the `STEADY_LINE` spans of 632-664 at 660, so the last chord returns to its c14 rows (c14 measured 14.9 dB there).

### 6. 57 of 393 crescendos do not rise on their own stem, 18 of them because the dynamic trims fall across the hairpin (measured)

Method: every printed crescendo of 1.5 qn or more in which the track sounds at both ends; stem RMS of the last third plus 0.4 qn against the first third. 57 rise less than 1 dB (winds 24 of 159, brass 13 of 102, strings 19 of 121, timpani 1 of 11): 15 %, between Movements I / II ("few") and the scherzo (40 of 215). In 18 the dynamic and soft trims fall 2 dB or more across the hairpin; in 13 the whole envelope does.

Largest: Clarinet 2 1032-1048 -3.8 dB (trims -6.0), Clarinet 1 1032-1048 -3.0 (trims -4.0), Flute 2 1032-1048 -2.2 (trims -3.0), Horn 1 1040-1048 -2.7 (trims -2.7): the crescendo of bars 259-262 into the crash at 263. Horn 2 516-520 -2.7 (trims -3.3). Trombone 1 880-884 -1.9 (trims -8.7) and Horn 3 880-884 -1.3 (trims -9.7): bar 221, into the C-major arrival. Violins I and Violoncellos 884-888 -3.8 / -2.7 dB with the envelope falling 12 / 16 dB (c15's counter-shapes at bar 222; the master does rise there, bars 221-223 -24.6 / -19.6 / -15.3). Horn 2 and Horn 1 832-839 -3.4 / -2.6 and Flute 1 832-838 -1.3 with the envelope rising 5-7 dB (the sample falls: a held-note decay; a body shape is needed, stated as a slow rise over the whole note).

Fix: `build_reaper.py vol_points` already holds the trim in soft decrescendos (`SOFT_DECRESC_HOLD_MAX_CC`). Add the mirror for crescendos: inside a crescendo the trim may rise but falls only by half of its fall (`CRESC_TRIM_KEEP = 0.5`), from the hairpin's start to the first note-on after its end. Expected on the 18 cases: half of the 2-9.7 dB the trims take back, so 14 of them rise 1 dB or more; the arrival levels after the hairpin do not change. For 1032-1048, also give Clarinets 1-2 and Flute 2 the master's rise (+2.2 dB over the four bars) as a role ramp.

## The comparison in short

- Against c00: integrated level and peaks are under control (c00 clipped at +6 dBTP), stops are drier, the first theme is steadier (S outside 25 ms 104 -> 79 and 118 -> 90 against c14). The low end is worse (finding 3). Attack definition on a crude measure has not improved: mean rise of the 1-4 kHz envelope in loud frames 60 dB/s in c00, 57 in c10, 58 in c15, Movement I c55 64, Dvořák 70; fast level variation (10 ms frames against a 1 s mean) 2.67 dB in c00, 2.55 in c15, 2.34 in Movement I, 2.95 in the recording. Side / mid -5.0 dB (references -4.9 to -5.4): fine.
- Against c10 and c14: band shares and width are unchanged within 0.6 dB; the gains are in timing and in single passages.
- Against Movement I c55 on the same tools: the Finale has more bottom octave (-14.1 against -14.6) and the same low-mid excess; Movement I's envelope findings repeat here with smaller numbers (68 % inside notes against 74 %; 39 % of the 3 dB notes unmarked against 45 %).
- What still sounds like a machine, by measurement: accents that vary from -1 to +8 dB over their neighbours while the score prints one sign (finding 1); joins with a 7-15 dB hole made by a level step (finding 2); the peroration's theme on changing rows and bass eighths without a bow attack (finding 4); a bass line whose notes sound an octave up (finding 3).

Do not touch: the hall sends, return levels and IR envelope outside the tail lifts of finding 5; the first theme's one-row layout and class leads (`STEADY_LINE`, `steady_leads.json`); the keyswitch 0.15 s early on the first theme only; re-bow fills and the loop work on the chorale and final chords; the basses' level steps in 104-136 (they help); the timpani roll levels, settle and attack lifts; the second theme, the trumpet and wind solos, the chorale and coda 2, where the per-note layers do nothing and the levels are even; the delivery chain (LRA 14.8 LU, limiter 2.1 dB); the closed items in the coordinator's list.
