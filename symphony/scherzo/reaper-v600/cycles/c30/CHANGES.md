# Cycle 30: changes (actor, on the c29 render; last cycle of the run)

STATUS: **rendered once in two passes**, 2026-11-18. Main pass 16:01-16:08 CST from a freshly restarted REAPER after a
full build of all 31 main tracks (guard 0 stale, memory settled at 44 GB, 0 compressed); second pass 16:15-16:22 (the
felt timpani alias in `scherzo-v600-mockup-pass2.rpp`). Attack probe: late or hole 0. No stem fix. The mp3 was delivered
twice from the same master (the coda ride row deepened after the first delivery read a summit lead of +0.46 LU).
- mp3: `cycles/c30/scherzo-mockup-c30.mp3`. Data as rendered: `cycles/c30/build_render/`. Records: `cycles/c30/records/`.
- Lock (`phase.log`): taken 15:01 (after the finale's c30 actor released it), released 16:22: **81 min** (open + settle,
  full build, Dan's range tests P0 / P1 with a build and a restart between, a failed string build (bridge busy after the
  ranges), restart, full build, restart, main render, stale fix of Horn 2 / 4, save, guard 0, pass 2, quit).
- REAPER memory: **45 GB after the main render** (0 compressed); pass-2 project 1.2 GB.
- Master -23.9 LUFS, LRA 21.1, true peak -3.1 dBFS, sample peak 0.702 (float sum of 36 stems). No file over -1 dBFS.
- Disk: c29's stems deleted (00_Master.wav and mp3 kept; c29-side measures recorded first in `records/lev_c29.txt`); my
  range WAVs deleted; 35 GB free. `Backups/` not touched.

## 0. Dan's note (first item)

> "in mov 3 at 39 seconds in the recording the strings overlapping slur together really bad something went wrong"

- **Where.** The mp3 starts at score qn 0 (C's alignment: +238 samples). 0:36-0:39 is bars 53-55 (qn 157-165), the
  end of the second idea: eighths E-D (157 / 157.5), then the slurred descent C (158, a quarter) - B (159, half) - A (161)
  - G (163) in octaves in Violins I / II and celli, violas on G - F sharp - D. Reprise: bars 285-287 (qn 853-859).
- **Cause (measured, `records/dan_P0.txt`, `dan_full.txt`; `tools/pcx.py` pair crossover and perceived attack re the
  score onset).** The B at 159 is a "Leg Slur MAX" target led 0.22 s = 0.96 qn at quarter 264, so its note-on falls 0.04 qn
  after the C's own note-on. The pitch crossover read **-316 ms** (Violins I / II) and -225 ms (celli): the B's band was
  over the C's before the C began, so the C was never heard as a note and the descent smeared into one slide; the B's
  attack was still +107 / +33 / +80 ms late. Also late: celli E at 154 (a new slur, played as a legato join from the F
  sharp) **+252 ms**, violas D at 162 +105 ms; reprise celli 850 +133, Violins II 855 +108.
- **Since when.** The same note data since c16 (the `lead_set.json` refit: Violins I 159 0.255 s, celli 154 0.18 / 159
  0.135) and identical in c18, c21, c24, c26-c29 (parts.json compared); c18 and c29 stems have the same 50 ms envelopes
  there (3 dB apart: global gain). Not a recent change; none of the Do-not-touch items is the cause.
- **Fix (instrument side; `build/score_config.py` c30 item 0, switch `C30_DAN`).** These notes play fresh "Sus MAX" heads
  (ART_SPANS) with REATTACK_LEAD_AT, and their lead_set entries are dropped: Violins I / II 159 and 855, celli 154, 159,
  850, 855, violas 162. (Violas 850 was tried and dropped: it re-timed the tenuto G repeats at 852-853.)
- **Range test** (same starts 153.6 / 851.2 / 849.4; control P0 = the c30 build without item 0; P1 with heads at 0.06 s):
  crossover at 159 -316 -> **+44 ms** (V1), -316 -> +44 (V2), -225 -> -4 (Vc); heads' perceived attack +78 / +91 / +61 ms,
  855 +111 / +134 / +143, so each head's lead was raised by its lateness beyond +20 ms (0.10-0.18 s; a lead moves the
  same attack earlier). The second step was not range-tested; the full render confirms it.
- **Full render, c29 -> c30** (perceived attack pc / crossover, ms re the score onset):

| note | c29 | c30 |
|---|---|---|
| Violins I 159 (C -> B) | +107 / -318 | **+25 / -52** |
| Violins II 159 | +33 / -316 | **+32 / -21** |
| celli 159 | +80 / -225 | **+20 / -40** |
| celli 154 | +252 / +8 | **+62 / +114** |
| violas 162 | +105 / -2 | **-3 / +8** |
| Violins I 855 | +30 / -300 | +27 / -23 |
| Violins II 855 | +108 / +36 | +88 / -55 |
| celli 850 / 855 | +133 / +19 | **+12** / +82 |
| joins after the heads (161 / 857) | +15..+34 | -8..+19 (celli 857 +76) |

- The C quarters now sound until 20-50 ms before the B's beat at every occurrence. Still late: Violins II and celli 855
  (+88 / +82), and the reprise violas 854.5 / 857 (+116 / +222 ms, legato targets with no lead; not changed, not tested).
- Probe: string joins pcX median V1 +6, V2 +5, violas +10, celli +26 ms; > 60 ms off 6 / 8 / 10 / 23 %.

## Changes

### Tools
- `tools/score_to_parts.py` (generic, off by default):
  - `UNI_RUN_MERGE_VALUES` (adjacent unison-boost role runs merge whatever their boost; the run takes the boost its notes
    hold longest) and `UNI_RUN_GAP_QN` (the merge gap, default 1.0 as before); `STP_DEBUG_UB=<track>` prints the runs.
  - `ROLE_EDGE_MOVED_CHAINED_AT` (score onsets where a chained role crossfade is pinned before the led note's moved
    note-on, like an unchained edge).
- `tools/deliver_master.py`: `MOM_CAP_ABOVE` 3 -> **0** (critic C #1; scherzo comment).
- Actor scripts `cycles/c30/actor_scripts/`: `apply30.py` (roles / mix / lead_set from `before/`), `chk30.py OLD NEW`
  (parts.json lanes changed per track), `show30.py`, `lev30.py CYCLE` (the c30 item levels), `env30.py`, `rng30.py`
  (pcx attack / crossover at listed onsets of any render), `dan30.sh`, `m30.sh`, `ranges30.sh`, `rr30.py`, `post30.sh`,
  `bars30m.py`, copies of the c29 checks (`guard30`, `net30`, `gate30`, `snap30`, `netshow30`), `wait_lock.py`, `lk.sh`.

### Data
1. **Summit stroke** (A #1): string role edges 1004.75 -> 1005 (apply30.py); Violins II's and the violas' rows chain
   there, so `ROLE_EDGE_MOVED_CHAINED_AT = (1005.0,)`. CC7 rise inside the stroke: Violins II 5.9 -> 2.0 dB within the first
   50 ms (now a 1.8 dB step about 12 ms after the note-on, the CC7 lane's point grid), violas 2.1 -> under 1.5, Violins I
   2.0 -> 1.7; net level of the body unchanged (+14.1 dB Violins II).
2. **Horn 3** (B #1, #2): E4 region gain -1.0 -> **-5.0** dB (full rebuild); the in-note swells at 349.7 / 352.7 came from
   the unison-boost role split where a three-player E4 (+4.77) sat inside a two-player run (+3.01): runs merge
   (`UNI_RUN_MERGE_VALUES`); B's breath inference was wrong (the runs met with no gap). UNI_RUN_GAP_QN 3.0 tried and left
   at 1.0 (it merged Oboe 1's 120-128.5 / 816-824.5 runs across rests and changed nothing on Horn 3).
3. **Celli countermelody head** (A #2): roles [312, 360, 4.5] / [912, 960, 4.5]; NOTE_END_AT celli {310: 311.5, 910: 911.5}.
4. **Close** (C #2): Horn 1 [1100.25, 1128, 6] deleted; CC11_ADD_SPANS Horn 1 14 -> 20; LEAD_SET_AT Horn 1 1101 0.06 s
   (the CC11 change had moved the note-on 1100.772 -> 1100.81, and the c11 LEVEL_SHAPES rows depend on 1100.772).
5. **Delivery** (C #1): MOM_CAP_ABOVE 0; RIDE_TRIMS horn call (5-18, -2), violin solo and Hn 1 tail (1043-1080, -2),
   close (1088-1128, -1 -> -2.5), 305-320 -1.0 -> -1.5; after the first delivery the coda row's last points -5 / -5.5 ->
   **-6 / -6.5** (summit lead +0.46 -> +0.56, simulated on the c30 master; `records/deliver_final.txt`).
6. If-time items, all done: (a) celli fugato CC11 +9 at 866.3-870 (B #3); (b) the 205-208 roll: role [612, 621, -3, 3]
   (end_ramp opens over 618-621), LEVEL_SHAPES release 618 -> 621, 618 removed from TIMP_ROLL_TRIM_HOLD_SKIP (C #3);
   (c) coda ppp strokes VEL_SET 1110 / 1111.5 40 (+10 lh_vel_add = 50), 1111 / 1112 / 1122 44 (A #5); (d) brass
   drop_always {309, 310} on Trumpets 1-2, Trombones 1-2, Bass trombone, Tuba (B #4). Flute 1 sfp row (A #4): not done
   (needed a range test; lock time went to Dan's note).

Opus state changes (full rebuild): Horn 3 (E4 region gain). Every main track was built in full before the render; the
alias rebuilt with `--pass2`. parts.json: one pre-existing WARN (celli early fills 582 / 600 / 780 ramp inside led legato
transitions; also in c28 / c29), not fixed.

## Full render: measured (c29 -> c30)

### Figure, first check (`records/fig25.txt`, `fig29w.txt`)
- Violins I / II: all 64 + 47 steps at every occurrence within 1.0 dB of c29 (low values unchanged: V1 83->82 0.9 / 0.8,
  83->78 0.4; V2 0.4-0.6 at bars 315 / 328).
- Woodwinds, gate: Flute 1 median +17.9, under +3 **0**, worst +9.3; Flute 2 +18.9 / 0 / +9.7; Oboe 1 +20.7 / 0 / +10.6;
  Clarinet 2 +22.2 / 0 / +6.3. c26 woodwind state kept.

### Guard, net in-note moves, gates (`records/guard_render.txt`, `netmoves_build.txt`, `gate_build.txt`, `snap.txt`)
| | c29 | c30 |
|---|---|---|
| step 1.5 dB / 0.5 s at > 6 dB/s | 1 (+14 harp) | 1 (+14 harp) |
| first 0.35 s 1.5 dB | 2 | 2 |
| B's 2 dB / 20 dB/s | 0 | 0 |
| CC7 moves 1 dB+ in notes outside hairpins | 85 | **81** (Horn 3 350 / 353, celli 317 / 917 gone) |
| CC7 change 1.5 dB+ in a note's first 50 ms | 33 | **32** (violas 1005 gone; Violins II 3.9 -> 2.0) |
| envelope points / per note / per second | 2,540 / 0.46 / 9.1 | 2,467 / 0.44 / 8.9 |
- Net-level gate against c29 (1 qn, 1.5 dB): only the intended spans: Horn 1 1100-1128 -6.0 (role deleted; CC11 not
  counted by the gate), brass 306-315 -2.0..-2.1, celli 311-318 / 911-918 +4.1.

### Item checks (`records/lev_c29.txt` / `lev_c30.txt`; full-band mean power)
| check | c29 | c30 | target |
|---|---|---|---|
| summit Violins II / violas / V1 front - body (0-80 / 150-400 ms) | -14.5 / -8.3 / -3.7 | -12.9 / -6.8 / -3.7 | -3 or better: **not met** |
| master 20 ms bins around the stroke | -21.6 -21.8 -21.1 -19.7 | -21.0 -21.5 -20.5 -19.3 | still a swell |
| summit step (summit29.py) | +0.8 dB | +1.0 dB | |
| Horn 3 E4 317 / 350 / 917 / 950 | -32.2 / -34.1 / -35.2 / -35.1 | -35.7 / -37.2 / -38.7 / -39.1 | within 1.5 of A3 / B3 |
| Horn 3 B3 after the E4 (320 / 920) | -28.1 / -30.9 | -31.6 / -34.5 | still 4-6 dB over the line (transition sample) |
| Horn 3 bar 107 / Violins I | -27.5 / -34.2 | -31.3 / -34.2 | |
| celli head 312-315 minus 318-321 | -3.9 | **-1.2** (912: -4.3 -> -1.8) | -1.5 or better |
| horn sum at the relay 1099 / 1101 / 1103 | -51.0 / -49.2 / -46.6 | -51.0 / -52.0 / -51.2 | rise 1 dB or less: met |
| Horn 1 bars 368-373 | -48.1..-50.6 | -53.0..-55.5 | about 2.5 dB down: 2.5 dB too far |
| Horn 1 minus Violins I + solo, 368-374 | +0.5..+4.7 | -0.2..-4.5 | within 2 dB: bar 371 -4.5 |
| master 364 -> 368 | +3.5 dB | **+0.6** | 1 dB or less |
| celli fugato 866.4-870 vs 170.4-174 | -6.8 | **-2.4** | within 1.5: not met |
| roll 617.5 -> 618 / 618 -> 618.5 | +5.1 / +3.3 | +2.2 / +2.8 | no 0.5 qn step over 2 dB: 2.8 |
| roll 618 -> 623.5 rise | 9.2 | **19.6** | 8 or more |
| roll under master at 622 / 623 | -8.6 / -7.3 | **-4.1 / -2.8** | 6 or more under: **not met** |
| coda strokes pp 1098 / ppp 1110 / 1111.5 / 1122 (10 ms peak) | -51.1 / -53.5 / -52.4 / -61.0 | -51.1 / -63.1 / -60.6 / -64.5 | 4-6 dB under: 9-12 under (too soft) |
| brass bar 104 Tpt 1 / Tbn 1 / Tuba | -33.0 / -35.3 / -35.4 | -34.9 / -37.3 / -37.4 | -2 dB |

### Trio climax (`records/trio.txt`): bars 209-217 identical to c29 (celli minus Violins I -7.3..-0.3; tune over the
celli + Bsn 2 -0.2..+10.4; tune over the violas +6.3..+13.7).

### Horn 3 width and the relay (`records/h3.txt`)
Countermelody 312-360 corr 0.97 -> 0.96, L-R +4.0, level -34.2 -> -36.3; relay 1094-1097 corr 0.74 / L-R +1.9 / tilt -9.0
(unchanged); Horn 1 1083-1092 0.69 / +1.0 / -8.5.

### Timpani sticks by passage (`records/extra.txt`): hard-stick Allegro and its rolls identical to c29; felt alias as c29
except the 205-208 roll (above) and the coda ppp strokes.

### Accents (`records/acc2.txt`, against the detached note before)
Strings unchanged (Violins I -3.8, Violins II -2.2, violas +0.2, celli +0.9); woodwinds moved with round robins (Flute 2
-0.9 -> -2.7, Clarinet 2 -3.2 -> -4.7). No track's median over +3; still under Dan's +1..+2 on the violins.

### Tutti downbeat weight on the mp3 (`records/down_mp3.txt`)
Theme A +2.3 (c29 +2.4); 312-360 +0.3 (+0.3); 912-960 +0.6 (+0.5); 984-1005 -0.2; 1005-1017 +0.4 (+0.1).

### Delivery against the shared spec (final delivery; `records/spec_final.txt`, `deliver_final.txt`)
| | c29 | **c30** |
|---|---|---|
| 1. I / TP | -14.1 / -1.2 | **-13.8 LUFS / -1.4 dBTP** |
| 2. summit lead | +0.60 (bar 318) | **+0.56 (bar 335)** |
| 3. f -> ff | 2.23 | **2.07 LU** |
| 4. p10 short-term | -21.0 | **-21.1** |
| 5. limiter (summit) | 3.9 | **4.2** (tuttis 1.6-2.2) |
| 6. LRA | 11.4 | **11.8** |
- Solos on the mp3 (Mmax, `records/solos_mp3.txt`): horn call bars 4 / 5 -10.4 -> **-13.0 / -12.9**; violin solo 350 / 351
  -11.8 / -11.6 -> **-13.4 / -13.3**; Hn 1 357 -12.8 -> -13.7; Clarinet 1 82 / 162 -11.4 / -11.4; f bars 41 -10.3, 101 -10.9,
  197 -12.3, 209 -11.9. The close (bar means 364 / 368 / 372 / 376): -22.2 / -18.1 / -18.0 / -21.2 -> **-21.2 / -21.1 / -21.5
  / -24.1** (no longer rising).
- Climax order on the mp3: summit -7.1, bar 300 -8.1, 105-120 -8.1, 305-320 -8.3, bars 72 / 304 -8.5, bar 53 -8.6.
- Crescendo arrivals: 41 +2.2, 72 +0.4, 105 -0.5 (still reversed), 129 +0.3, 197 +1.1, 209 +0.4, 285 +0.6, 300 +1.1, 304
  +1.0, **305 -0.3** (was +0.3: the deeper 305-320 row), 329 +2.9, 336 +0.6.
- Quiet means: intro -18.1, theme A -16.0, counterstatement -18.3, fugato -21.3, trio dolce -15.8, stretto -26.9, Meno pp
  -18.9 (all 0.5-0.8 LU louder than c29: the mp3 is 0.3 LU hotter overall and the cap no longer limits their peaks).
- Hall (`records/hall.txt`, `hall14.txt`): master G.P. drop at +0.3 s 18.7 dB, 20 dB fall 0.33 s, RT60 1.42 / fitted 1.45 /
  late 1.46 s; mp3 17.2 dB / 0.37 s / 1.40-1.50 s; soft ends 0.06-0.19 s; returns re dry -12.7 dB. Inside Dan's limit.
- Master sample peak 0.702 (-3.1 dBFS); no clipping.

### Timing (`records/timing.txt`): over 25 ms 26 %, over 60 ms 5 % (unchanged).

### Per-bar master against c29 (`records/bars_c30_vs_c29.txt`, median 0.0)
Over +1.5: bar 290 +3.9 (celli fugato CC11), 365 +2.2 (Horn 3 relay G sharp: round robin, it was -1.7 against c28),
61 +1.6 (no data change in that bar: round robin). Under -1.5: 368-376 -1.7..-2.6 (Horn 1's close), 342 -1.6 (Horn 3 E4
at the recall).

## Rejected, deferred, not done
- UNI_RUN_GAP_QN 3.0 (coordinator item 2 form): changed other tracks, not the fault; value merge used instead.
- C #5 Più mosso ride row +4: not adopted (summit lead margin +0.56).
- A #3 (other guard-carried role edges: Violins II 198, bass clarinet 264, celli 648 / 840): not done.
- A #4 Flute 1 / 2 sfp on "Sus Accent MAX": not done (range test needed).
- A #6 hairpin-end twin of HP_START_MOVED: not done.
- MANUAL-GAPS: no new gap tried this cycle.

## Faults still audible (instrument side not found or overshot)
- Summit stroke still swells in the strings (Violins II front 12.9 dB under its body): the CC7 step was not the main
  cause; the strings' ff attack sample itself is slow. Summit step +1.0 dB.
- The 205-208 roll arrives only 2.8-4.1 dB under the master at its f (c29 7-9 dB): the trim hold plus the slower release
  added about 5 dB at the arrival.
- Coda ppp strokes 9-12 dB under the pp strokes (target 4-6): v50 / v44 fell a felt layer; v56 / v50 would be the next try.
- Horn 1's last G sharp 2.5 dB softer than C's target (bar 371 4.5 dB under the violins).
- Reprise violas 854.5 / 857 legato targets +116 / +222 ms late; Violins II / celli 855 +88 / +82.
- Horn 3's B3 after the E4 (320 / 920) 4-6 dB over the line (the E4 -> B3 legato transition sample).
- Arrival 105 reversed (-0.5), 305 -0.3; tutti downbeats +0.3 / +0.6 dB on the mp3; violin accents -2..-4 dB.

## Research items
| item | status |
|---|---|
| EW template mix, returns, seats | adopted (unchanged) |
| no volume automation per note | adopted; Horn 1's one-note row removed; CC7 in-note moves outside hairpins 85 -> 81 |
| dynamic trims as CC7, role edges in rests | adopted; chained edges pinned at 1005 |
| accents by the KS Masters' accent rows | adopted (unchanged) |
| tenuto ends 34 ms before the next beat | adopted (unchanged) |
| timpani hard sticks / felt alias in pass 2 | adopted (unchanged windows) |
| second render pass | adopted |
| CC16 resets | adopted (unchanged) |
| shared -14 delivery + room bed | adopted; MOM_CAP_ABOVE 0, ride rows for exposed solos |
| per-onset leads from whole-piece refits (c16 lead_set) | **dropped at 7 notes** with measured evidence: a legato target after a quarter at quarter 264 swallowed the quarter (crossover -316 ms); fresh heads +4..+68 ms |
| oboe Main lower than -9 dB | pending (not run) |

## State at the end of cycle 30

**What the movement does well (measured on c30).** The delivery meets all six shared spec items (-13.8 LUFS, -1.4 dBTP,
summit +0.56 LU, f -> ff 2.07 LU, p10 -21.1, limiter 4.2 dB, LRA 11.8) inside Dan's hall limit; exposed p / pp solos sit
2-3 LU under the f passages; the close fades (bars 364-372 within 0.4 LU). Dan's bar 23 figure is clean at every
occurrence in strings and woodwinds (gate 0 under +3). The bars 53-55 descent (Dan's 0:39) now plays each note in
time. Trio climax, sfp at 301 and both sub. p's hold; the fugato grows 16 LU; theme A's downbeats +2.3 dB on the mp3;
no loop pulsing; string legato joins pcX median +5..+26 ms; guard 1 / 2 / 0.

**Faults still audible, by priority.**
1. Summit stroke swell in the strings (Violins II front -12.9 dB against its body; summit step +1.0 dB).
2. Tutti downbeats in the ff theme only +0.3 / +0.6 dB on the mp3; arrival 105 reversed (-0.5 LU), 305 -0.3.
3. 205-208 roll too close to the master at its f (-2.8 dB); coda ppp strokes too soft (9-12 dB under the pp).
4. Reprise string joins at 854.5-857 late (+82..+222 ms).
5. Accent fronts under their neighbours on the violins (-2.2 / -3.8 dB).
6. Horn 3's B3 transition after the E4 hot by 4-6 dB; Horn 1's last G sharp about 2.5 dB under target.
7. Celli fugato subject 2.4 dB under its exposition twin.

**Open items for a future run, in order.**
1. Summit: try the strings' "Sus Marc LITE" / accent rows or a CC11 front for the 1005 stroke (range test); then lower
   the strings' crests in bars 337-339 (C #4) so the coda ride row can shorten.
2. Run `pcx.py` over every fast slurred string passage and convert each legato target whose crossover precedes its
   quarter (crossover < -lead) into a fresh head, as at 159 / 855.
3. Roll 205-208: put 618.0 back in TIMP_ROLL_TRIM_HOLD_SKIP (keep the 618-621 release); coda ppp strokes v56 / v50.
4. Horn 3 pitch 59 transition region gain; Horn 1 CC11 +24 (or Mid mic); A #3 role edges; A #4 flute sfp; C #5 stretto ride.

**Rebuild and render from this state** (from `symphony/scherzo/reaper-v600/`):
```
cd build && ~/.venvs/claude-composes-reaper/bin/python ../tools/score_to_parts.py . ~/.rpr-bridge/libs/ew_ho/ks_maps.json parts.json && cd ..
~/.venvs/claude-composes-reaper/bin/python tools/reaper_ctl.py lock "scherzo cNN actor"
~/.venvs/claude-composes-reaper/bin/python tools/reaper_ctl.py start && ~/.venvs/claude-composes-reaper/bin/python tools/reaper_ctl.py open
# wait for memory to settle (cycles/c11/actor_scripts/wait_mem.py), then every track in full:
~/.venvs/claude-composes-reaper/bin/python tools/build_reaper.py build/parts.json jobs
~/.venvs/claude-composes-reaper/bin/python tools/reaper_ctl.py save && ~/.venvs/claude-composes-reaper/bin/python tools/state_guard.py scherzo-v600-mockup.rpp build/parts.json jobs
~/.venvs/claude-composes-reaper/bin/python tools/reaper_ctl.py restart          # settle again
python3 ~/.rpr-bridge/rpr.py run jobs/audio_init.lua
~/.venvs/claude-composes-reaper/bin/python tools/render_cycle.py NN
# guard; full build of any stale track; save; quit; then pass 2:
~/.venvs/claude-composes-reaper/bin/python tools/reaper_ctl.py start && ~/.venvs/claude-composes-reaper/bin/python tools/reaper_ctl.py --pass2 open
~/.venvs/claude-composes-reaper/bin/python tools/build_reaper.py build/parts.json jobs --pass2
~/.venvs/claude-composes-reaper/bin/python tools/reaper_ctl.py --pass2 restart && python3 ~/.rpr-bridge/rpr.py run jobs/audio_init.lua
~/.venvs/claude-composes-reaper/bin/python tools/render_cycle.py NN --pass2
~/.venvs/claude-composes-reaper/bin/python tools/reaper_ctl.py --pass2 quit && ~/.venvs/claude-composes-reaper/bin/python tools/reaper_ctl.py unlock
```
The saved main project matches `build/parts.json` (guard 0 stale after the render); the pass-2 project matches the alias.
`build/` is the rendered state plus nothing else (`cycles/c30/build_render/` is a copy).
