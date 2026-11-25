# Cycle 56 (actor): faults of the first render without per-note volume moves, fixed on the instrument side

Rendered 2026-11-15 18:42-18:50 (one full render), one stem fix after it (ten slow section rows), written to REAPER
before the quit. Lock held 17:31:30-18:57:04 (85.5 min; offline work 11 Nov, then a usage-limit stop; second wait 2 h 28 min
behind the scherzo and Movement I). Owner's rule (Dan, 11 Nov): no per-note track volume move in any form. Nothing in this
cycle adds one; every fix is CC11 / CC1 / CC7, velocity, row, note length, a region volume in the Opus state, a doubling
on an idle instance, or a slow row (section, three notes or more, fade).

To reverse: `cycles/c56/before/` holds every tool and build file as it was (45 files). `MVT2_C56_OFF=1` builds without
the c56 block of `build/score_config.py`; each item has its own switch there (`MVT2_C56_DBL`, `_LIFT`, `_SUS`, `_SKIP23`,
`_TBN`, `_TBN1`, `_TOPS`, `_VCLONG`, `_ENTRY`, `_LEGVEL`).

## What was done (lead_c56.md numbering)
1.1 **Envelope edges inside notes.** `tools/build_reaper.py vol_points()`, mix.json `env_edge_slew` {db_s 3.0, tail_s 0.25}:
   while a track sounds the whole envelope (roles, section rows, hairpin-gain releases, dynamic trims) moves at most
   3 dB per second (forward and backward slew limit, averaged: a step becomes a ramp centred on its edge), free in
   rests; a printed sudden dynamic change (24 CC or more) keeps its step, moved to 0.02 qn before the led note-on.
   `env_simplify_db` 0.1 -> 0.2. Entries checked after it (envelope at the first note): Violin I solo 48 +5.9 dB (c55
   +5.7), Horn 1 226 +7.4 from the note-on (c55 +0.8 rising to +6.2 inside the note), Bass clarinet 90, Flute 1 108.
1.2 **Bar 63.** The four c31 CC7 lanes (half of a pair with level shapes that c55 switched off) are gone, with two more
   half-pairs: Flute 1's CC7 57 over 211.96-213 and Clarinet 1's dip before 283. New: the tremolo row's level as region
   volumes (Violins I +5.5, Violoncellos +4.8, Violins II -1.5 dB; the row plays only the two tremolo notes), CC7 127
   over the head, then a straight dB fall 212.15-212.75 by the same amount (Violins I on to -8 dB), held to the end of
   the tremolo. Section rows [204, 220] end at 212. Not checked: the other old CC7 lanes (Cor anglais 266-268, Clarinet 1
   205-210 and 291.4-292.5, Bass clarinet 272.75-276, Trombone 2 208-210, strings' niente lanes).
1.3 **Region and row gains.** `region_gain()` (scherzo c16) and `row_volume_db` (finale c16) ported. The row volume knob
   had no effect on range pass a1 (Flute 1 136 and the tremolo rows 0.0 dB), so row levels are region volumes
   (`region_gain_db` `row_db`). Tables (mix.json; fitted by critic B on the c55 render, not from the old pitch trims;
   every note each one touches is listed in `region_gain_usage.txt`): Horn 1 {53 +3, 55 +2, 56 +3, 60 -1.5, 62 -4,
   65 -2.5, 66 +3, 67 +2, 68 +5}, Double basses A flat 1 -5 (Sus / Leg rows, 23 notes), Bass clarinet A flat 2 -4
   (12 notes), Cor anglais A 4 -4 (2), Bassoon 1 pitch 61 -3.5 on Sus MAX, Clarinet 1 D flat 5 +3 (6), Violas
   "Pizz RRx4" {49 +5, 51 +7.5, 53 / 54 +5, 58 +3, 61 -2, 65 / 66 -7} with the c55 velocity offsets taken out, Flute 1
   "LegRep RRx4" -9.5. Pass a1: every gain arrived to within 0.3 dB, Horn 1's legato-joined notes included (Bassoon 1 206 read -2.7 for -3.5).
   Rejected: B's tables for Violins I / II, Violoncellos, Flute 1 pitches, Bassoon 2, Clarinet 2 and the basses' other
   pitches. Simulated on the c55 stems they made the lines worse (median step Violoncellos 71-78 1.85 -> 4.30 dB,
   Violins II 22-30 1.14 -> 2.10): the celli's hot notes are long notes, not pitches (238 E flat 3 -34.1 against 250
   E flat 3 -39.1).
   Section rows refitted twice against the c54 section levels (`comp56.py`, `build/cell_rows_c56.json`: 117 rows, c55
   had 114). **All 117 exist only to give a track's section the level the old per-note layers gave it**; none is a
   printed dynamic or a role. The rows over 1 dB that c57 could move to CC11 / velocity / row choice first: Clarinet 2
   [0, 18, +9.4], Double basses [220, 238, +8.1], Flute 1 [262, 274, -6.1], Violins I [140, 172, -5.5], Horn 3 [66, 90,
   -5.3], Bassoon 2 [220, 238, -4.4] and [262, 274, -4.1], Timpani [140, 172, -4.6] and [204, 220, +4.4].
1.4 Timpani bars 84-85 all three strokes velocity 72; Violas 81 played gap 0.15 s with a CC11 fall of 16; Violins II div
   120 gap 0.15 s. Oboe 1 phrase heads: velocity 53 -> 86 changed nothing on pass a1 (0.0 dB): reverted, CC11 +22 over
   the five head notes instead (+14 gave +2.9 / +3.0 dB on pass b1). Basses 144 not changed (`REP_GAP_AT` drops its
   0.1 qn lead; `soft_gap_s_at` does not reach a "sus_min_s" repeat). Violas pizzicato CC11 park not done.
1.5 `acc56.py`: the row of a note is the last keyswitch; classes pitch-change / level step / same pitch / pizzicato.
   c55's 379 "holes" are 194 pitch-change (of 806), 74 level steps, 66 same-pitch, 45 pizzicato. Of the 44 S readings c55
   lost against c54, 25 sat on c54 envelope steps of 2 dB or more at the beat: c54's 640 was partly made by the fader.
1.6 `_all` climax role -0.4 -> -1.0 dB; basses' coda row split at 286.
2.2 **Re-bows.** a) bars 2-3: Violins II, Violas, Violoncellos, Double basses keep one bow (their points were listed
   `REBOW_AT` points; fills moved to `_removed_c56`). b) new `TRACK_DOUBLES`: Violins I bars 1-3 and final chord on
   "Violin I solo" (DIV A), Violins II's final chord on "Violins II div" (DIV B), the celli's on "Violoncellos div",
   copies on Sus MAX, bow changes at the midpoints, CC7 per span fitted on pass a1 (127 / 100, 90, 90 with the celli
   copy at 36). c) new `REBOW_CC_LIFT` +7 CC11 over 0.45 s with a 4-unit fall before it, not on the basses (pass a1:
   their dips got deeper, median 3.8 -> 4.9 dB), 223 down-bow +7 falling over 0.75 qn. d) Violins I 0 and 292 start
   on Sus MAX (not Violins II 286: it broke the printed repeat at 289). e) CC68 not tried. Morendo: CC11 33 at 298.3
   to 20 at 301 to 15 at 303.5 on all string tracks.
2.3 Not tested (build ready in `build_legvel/`): the range passes were deleted to stay over the disk limit.
2.4 Basses' pizzicato sf velocity 118 (front -23.1 dB, c54 -22.2); Bass trombone CC11 +10 (+1 dB only).
2.5 Trombone 1: CC11 104 / heads 124 for 0.07 s / 112 moved levels by under 1 dB (about 0.1 dB per unit near the top);
   CC1 -4 on 216 and -7 on 217-217.5 (CC1 -14 took 4-9.5 dB on pass c1; the final values were not range-tested).
   Owner's note on the finale's accents ("a little bit over done") applied: aim +1.5 to +2.5 dB.
2.6 CC11 +9 over the long F5s at 68 and 80 (both violin sections), Violins II 47 +10 (pass a1: -56.9 -> -51.2 dB, c54 -49.7).
2.7 Region gains only: spread of the pitch means 4.09 -> 1.97 dB, median step 2.32 -> 2.21 dB (c54 1.78).
2.8 New `SOFT_ENTRY_CC` (+8 over 0.5 s at 29 fresh soft string entries on Leg Slur MAX / Flautando); eight lead
   additions in `leg_leads.json` (critic A's list). `leg_sus_attack_scale` not done.
Also: Clarinet 1 role [282.9, 291.9, +2] (three notes) and CC11 -6 on 292; CC11 -10 / -10 / -9 over the celli's long
notes 238 / 244 / 253.

## Acceptance (c55 delivered render -> c56 delivered render; c54 where useful)
| | c54 | c55 | c56 |
|---|---|---|---|
| envelope points / per-note items | 22,022 | 2,572 / 0 | **2,343 / 0** |
| envelope moves of 1.5 dB or more within 0.25 s inside a note: all / unmarked (`steps56.py`) | | 140 / 58 | **14 / 11** |
| notes moving 3 dB or more inside the note / unmarked (`env_stats.py`) | 631 / 288 | 157 / 47 | 111 / 34 |
| re-bow dip, median, with the double where there is one: Violins I / Violins II / Violoncellos | 1.7 / 2.1 / 0.2 | 6.2 / 8.1 / 5.5 | **2.3 / 4.6 / 1.5** |
| the same: Violas / Violas div / Double basses | 1.1 / 0.8 / 1.2 | 6.4 / 5.9 / 3.5 | 4.9 / 4.5 / 4.2 |
| master dips of 6 dB or more / 3 dB or more at string re-bow points (250 ms window; 79 points, c56 93) | 2 / 15 | 7 / 25 | **4** / 30 |
| re-bows over the 3 dB "after" limit, single stems (`rebow53.py`) | 16 | 30 of 37 | 28 of 37 |
| soft starts 3 dB / 6 dB or more | 176 / 32 | 302 / 71 | 294 / **71** (no fall) |
| joins 5 dB over both bodies with a master bump of 2 dB (`joinpeak53.py`) | 2 | 26 | 24 |
| join holes of 6 dB, all / pitch-change joins | 298 / 181 of 877 | 379 / 194 of 806 | 360 / 196 of 830 |
| S: 727 joins within 25 / 60 ms | 640 / 711 | 613 / 709 | 613 / **707** (16 readings moved 20 ms or more) |
| bar 63: master 212.0-212.5 against 211.5-212.0 | 0.0 | -3.5 | **+0.2**, falls to 214.5 without a rise |
| balance cells (171) off c54 by 1 dB / 2 dB or more | | 4 moved | 6 / 4 (the doubled spans among them) |
| master bars off c54 by 2 dB or more | | 11 | 4 (bars 20 -2.0, 31 -2.3, 84 +2.2, 92 +2.1) |
| repeats (49): median stem dip / own-band under 3 dB | 7.4 / 5 | 8.6 / 6 | 8.5 / 5 |
Solo margins c55 -> c56: Horn 1 7-14 +8.7 -> +8.4, Bass clarinet +5.6 -> +5.5, Flute 1 -2.3 -> -2.9, Oboe 1 -6.5 -> -6.0,
Horn 1 53-60 -7.3 -> -6.7, Horn 1 65-70 +4.2 -> +4.3, Clarinet 1 coda -0.3 -> +0.6. Main-line notes out by 2 / 3 dB
(critic B's fit) were not re-measured.

## Render figures
Master -23.3 LUFS, LRA 24.2 LU, true peak -4.1 dBFS. Delivered `mvt2-mockup-c56.mp3`: -19.8 LUFS, LRA 15.3 LU, true peak
-1.5 dBTP, limiter 1.9 dB, **span 18.4 dB** (c55 19.1), attack probe 0. Wetness: side/mid -5.8 dB (c55 -5.9), correlation
under 250 Hz 0.70 (0.72), 315-500 Hz against 1 kHz +5.5 dB (5.8). State guard 0 stale at the start, after each build,
before and after the render and after the quit; the saved project holds the build's envelopes (32 tracks, 2,343 points,
0 that differ). REAPER 39 GB / 0 compressed before the render, 40 GB / 11 GB after. During the range passes it reached
55 GB / 41 GB compressed after 17 full rebuilds in one run and the bridge stopped answering in a `--midi-only` job:
killed without a save, restarted, the three tracks changed since the last save rebuilt, then the normal restart.
Disk: 30 GB free at the render gate (27-31 GB during the session; range passes deleted as soon as read), 23 GB after.

## Stem fix after the render (slow section rows only; originals in `render_first/`)
Ten cells 0.7 dB or more off c54: Oboe 2 / Bass trombone / Tuba bars 61-64 +0.7 / +0.8 / +0.7, Trombone 1 61-64 +0.8,
Bass clarinet 37-44 -0.8, Violins I 45-52 -1.5 and 65-70 -1.1, Violoncellos 71-78 +0.8, Double basses 15-22 -2.2 and
83-92 +0.9. `--mix-only` on every track, save, guard, before the quit. The timpani coda row was not refitted (its
cell is under -60 dB): strokes read -43.8 / -40.3 / -43.1 dB on pass a1 (c54 -46.5 / -46.1 / -45.4), bar 84 +2.2 dB.

## Faults left audible (no per-note volume move goes back)
| fault | where | size | instrument-side fix to test |
|---|---|---|---|
| re-bow dips without a double | Violas, Violas div, Double basses: coda, final chord, 220-238 | median 4.2-4.9 dB; basses 221.8 8.5, 225.2 7.7 | no idle instance: fewer bows (no-split limit 4.5 -> 5.2 s), CC68 Legato script, a second basses instance |
| re-bows at a double's first bow and at printed repeats | Violins II 289 (8.9 dB), 292 (7.8), Violas div 289 (10) | | start the copy one piece earlier; `REATTACK_LEAD_AT` 289 |
| soft starts of 6 dB or more | 71, unchanged | | the +8 entry lift did not show in the count; `leg_sus_attack_scale`, longer lifts, checked per note |
| transition bursts | 24 joins with a master bump (c55 26) | 5-13 dB over both bodies | string legato velocity (2.3, untested), region gain on the celli's A flat 3 -> G 3 transition |
| Trombone 1 second accent | 218: front 1.0 dB under 217.5 (c55 -3.7); 213 is +3.2 over its pickup, 0.7 over the aim | | CC1 contrast fitted on a range pass |
| long notes over short ones in a legato line | Violoncellos 71-78 and 23-30 (line step 4.3-6 dB in c54 terms), Oboe 1 45-47, Flute 1 133.5 (-6.1 dB), Cor anglais 131.5 (-7.6) | | CC11 per note length, `leg_sus_attack_scale` |
| Oboe 1 heads | 42, 54 (and 139, 144, 188 unmeasured) | 2-3 dB under c54 at +14; +22 rendered | measure on c56 |
| bar 63 | Violas' head 3.5 dB under c54 (their tremolo row also plays bars 61-62); Bass trombone sf 3 dB under c54 | | CC7 headroom over 204-212 with a section row; CC1 on the bass trombone |
| climax lines | Violoncellos / Double basses / Violins II 61-64 median step up 0.7-2 dB against c55 | | per-note reading of bars 61-62 |
| timpani | bar 84 +2.2 dB; the 55 ms hole before the stroke at 172 (roll rule against CC7) | | velocity 72 -> 66 or a coda row; fold the roll rule into CC7 |
| basses 144 repeat | own-band dip 1.6 dB | | a gap option on the "sus_min_s" path that keeps the lead |
| S | 707 of 727 within 60 ms (709) | 2 readings | lead refit on two renders |
| final chord | master bar 92 +2.1 dB over c54 (c55 +3.1) | | deeper CC11 from 301 |

## Files
Tools: `tools/build_reaper.py` (region_gain, row_volume_db, env_edge_slew), `tools/score_to_parts.py` (TRACK_DOUBLES,
CC_SHAPES, CC_SHAPES_S, REBOW_CC_LIFT, SOFT_ENTRY_CC). Build: `score_config.py` (c56 block at the end), `mix.json`,
`roles.json`, `leg_leads.json`, `rebow_fills.json`, new `cell_rows_c56.json`. Session logs `s1.log`, `s2.log`, `s2c.log`,
`s2d.log`, `s3.log`, `s4.log`, `fix56.log`; range checks `chk_a1.txt`, `chk_b1.txt`; `actor_scripts/` (README, "c56").
