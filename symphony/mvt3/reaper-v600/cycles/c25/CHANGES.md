# Cycle 25 (2026-11-17): inner lines, string chords, celli on Detache, basses' re-bows, timpani arrival, harp, oboe, trumpets, tone, delivery

Critics' reports: `reports/A.md`, `B.md`, `C.md` (on the c24 render), the coordinator's rulings 1-9 and its later note (scherzo items). Snapshot before this cycle: `before/`. Scripts: `actor_scripts/` (`meas25.py` the ruled targets, `mono25.py` horn image, `rowread.py` patch rows, `edge.py` notes at role edges, `rvalid.py` range starts, `ridevar.py` delivery ride variants; lock phase `auto1.sh`, `p1.sh`, `pa.sh`, `ana.sh`, `p2b.sh`, `p2c.sh`, `p2.sh`, `p3.sh`, `after.sh`). Logs: `logs/` (`T1_meas.log` range test, `render/meas25.log` c24 against c25), `phase.log`.

Standing rule (Dan): no per-note move in the track volume envelope. Every change is on the instrument side (CC11 / CC1 / CC7, velocity, rows, note lengths and leads), a held passage level with its edges in rests, or a delivery ride. `stepcheck.py`: fader moves of 2 dB or more within 60 ms inside a note 30 -> 30.

## For Dan

- **Loudness unchanged at -14 LUFS.** The final chord is the loudest moment, 0.7 dB over bar 223 (c24: 0.6) and 0.5 over the next loudest bar. The limiter on the final chord is lighter (5.4 dB, c24 5.8).
- **The hidden inner lines come forward:**
  - The second violins' countersubject in bars 159-165 was 15-17 dB under the first violins; now 9-13 dB under (they no longer vanish; still under the 5-7 dB target, because more controller would switch them into their bright top layer).
  - The horn's soft counter-line in bars 67-74 is about 5 dB more present (best band -11..-13 -> -7..-9 dB under the rest).
  - The cor anglais and muted trumpet in bars 171-186 now stand 6-13 dB over their soft accompaniment (c24: 2-8).
  - The cor anglais / horn line in bars 217-218 is 2.5-4 dB clearer against the held violin chords.
  - The trumpets' theme at bar 211 enters 3 dB stronger against the accompaniment (still 3.8 dB under on the downbeat itself; the violas' chord still covers it there).
- **The cellos' half-note bass line under the first theme (bars 11-26, 151-166) no longer swells into each note.** It now plays the detached-bow samples: no note swells more than 4 dB (c24: 11 of 42), and repeated notes are separated 1.5-6.6 dB (c24: about 0).
- **The basses' soft pedal in bars 43-50** swells 2.6 / 1.6 / 4.1 dB after each new bow (c24 6.3 / 4.9 / 8.6); the low-end pulse in the whole orchestra there is 4 dB smaller.
- **The timpani's fff roll at the C-major arrival (bar 223)** now carries the printed decrescendo over the bar instead of dropping out after a quarter beat: 4-8 dB stronger over the bar, never the loudest instrument (22nd of 31).
- **The harp chord of bar 132** no longer sticks out 13 dB over the orchestra, and its soft arpeggio in bars 123-128 sits 5 dB under the bassoon solo (c24: level).
- **Oboe 1 in bars 143-144** now sits 5.4 dB under the clarinet (c24: 1.4).
- **The bass drum** at bars 223 and 278 has a deeper, bigger patch (the 40-inch drum); its low rumble is now level with the double basses (c24: 4 dB under).
- **The four horns share one stereo image** (Horns 2 and 4 now like Horns 1 and 3): no horn note loses more than 2 dB on mono playback (c24: 21 notes).
- **Trumpet 3's accent at bar 262** (qn 1044), which had no accent at all, is now 3.8 dB over its neighbours.
- **Not fixed or only partly:**
  - The first violins' accented chords in bars 1, 5, 94, 147 still have a front 5 dB over the second violins (the body came down 4 dB; the attack sample did not).
  - The stops after bars 94 and 113 now ring 13.1 / 13.5 dB down at +0.3 s on the mp3 (c24 14.9 / 14.4; floor 14.5): a little more hall is heard after those two cut-offs.
  - The muted trumpet's slurred joins at bars 172 and 182 still dip 4 dB (two other joins improved).
  - The lower strings' chord at bar 5 still reaches its body late on violas and cellos.

## Results (main render 18:29-18:39)

- **Delivered (`mvt3-mockup-c25.mp3`, re-delivered after the render with refitted ride rows; starts 0.30 s before qn 0):** -14.0 LUFS, LRA 11.3 LU, true peak -1.3 dBTP, p10 short-term -21.8 LUFS, limiter 5.4 dB (final chord). First delivery (`mvt3-mockup-c25-first.mp3`, rows written before the render): -14.0, LRA 11.4, TP -1.0, p10 -21.9, limiter 6.3 dB, final over 223 / bar 212 by 0.5 / 0.5.
- **Shared delivery spec, on the mp3:**
  1. -14.0 LUFS, -1.3 dBTP: met.
  2. Final (bars 278-279) -7.8; bar 223 -8.4 (+0.7), 263 -8.4, loudest other bar 227 -8.3 (+0.5): met. 223 and 263 tie (263 0.1 louder by the margin script, 0.1 quieter by the bar list); c24 had 223 0.1 over 263.
  3. f -> ff +3.8 LU (medians f -15.6, ff -11.7): met.
  4. p10 -21.8: met.
  5. Limiting on climaxes 5.4 dB: met (first delivery 6.3, not met).
  6. LRA 11.3: met.
- **In-bar steps on the mp3:** 223 over 222 +2.5 dB (c24 +3.1), 263 over 262 +0.3 (c24 +0.6), final over 277 +0.6 (c24 +0.9).
- **mp3 stops at +0.3 s:** bars 2 / 6 / 94 / 113 / 166 / 204 / final 15.4 / 15.0 / 13.1 / 13.5 / 17.4 / 15.1 / 16.3 dB. Bars 94 and 113 under the 14.5 floor (fault left).
- **Master:** -19.3 LUFS, LRA 22.6, sample peak 1.110 (float stem sum). Loud-frame 100-250 Hz share: band shares over the movement 100-250 Hz -9.57 dB, 6-20 kHz -25.97 dB (c24 metrics: see `cycles/c24/metrics/metrics.md`).
- **Attack probe:** 0 late or holes. All 36 files present. The "pre-roll not silent" notes (8 files) are the led attacks before qn 0, as in c24 (8).
- **REAPER memory:** 46 GB before the render (0 compressed), 46 GB after (0 compressed).
- **Lock:** 17:39:28-18:40:25, 61 min (free when taken; no waiters). Start and settle 13 min, CTRL range 6, T1 build 1, T1 range 7, analysis, refit parts.json 4, final build of 4 tracks 3, state guard 2 stale (Bassoon 1, Trombone 2: legato attack times) rebuilt in full, restart and settle 11, render 10.

| target (ruling) | c24 | c25 | goal |
|---|---|---|---|
| Violins II best band, bars 159-165 (1) | -13..-16 | -9..-10 | -7 or higher (close) |
| Violins II minus Violins I, bars 159-165 (1) | -14.5..-19.7 | -8.9..-12.8 | -5..-7 (not met) |
| Clarinet 1 best band, bars 159-165 (1) | -9..-13 | -8..-11 | -8 or higher (partly) |
| Horn 1 best band, bars 67-70 (1) | -11..-13 | -7..-9 | -6..-8 (met) |
| theme B melody minus rest 840 / 842 / 856 (1) | -6.8 / +0.8 / -0.2 | -3.8 / +2.6 / +1.3 | +2 or more (842 / 856 nearly; 840 not) |
| violas minus Trumpet 1 840-842 (1) | +8.5 | +5.2 | -3 or less (not met) |
| espressivo line minus rest 864 / 866 / 868 (1) | -8.8 / -6.5 / -2.9 | -4.8 / -3.2 / -0.3 | 0 or more (partly) |
| cor anglais minus loudest accompaniment, bars 171-186 (1) | +1.5..+8.1 | +6.0..+12.6 | +5 or more (met) |
| Violins I front / body qn 0 (2) | -26.9 / -28.3 | -27.5 / -32.3 | front within 3 dB of Violins II (-32.2): not met; body near c23 -29.8 (2.5 under) |
| master front qn 0 / 16 (2) | -21.4 / -21.2 | -21.4 / -21.3 | about -21.5 (met) |
| lower strings -3 dB point at 16: Vln II / Vla / Vc (2) | +90 / +140 / +100 ms | +280 / +120 / +360 | +30 (not met; data unchanged from the range, see below) |
| celli back - front median, 40-104 / 600-664 (3) | +2.9 / +2.9 (over +4: 7 / 4) | -0.5 / -0.9 (0 / 0) | +2 or less, none over +4 (met) |
| celli minus basses 40-104 / 600-664 (3) | +0.3 / -0.6 | +0.9 / -0.3 | level kept (met) |
| basses' bow rise 170.9 / 181.7 / 190.5 (4) | +6.3 / +4.9 / +8.6 | +2.6 / +1.6 / +4.1 | +3 or less (2 of 3) |
| master 30-150 Hz range 168-199 (4) | 13.1 | 8.9 | 4 (not met) |
| timpani minus master 888 / 888.5 / 889 / 891 (5) | -15.5 / -21.0 / -24.9 / -27.2 | -11.5 / -13.0 / -17.7 / -19.9 | -10..-12 / -15..-18 at 891 (888 met, 891 2 dB short) |
| harp 524 peak re next loudest (6) | +11.7 dB | under the top 4 | 5 or less over Violins I (met) |
| harp minus Bassoon 1, 488-512 (6) | -0.9 | -4.9 | -2 or less (met) |
| Oboe 1 minus Clarinet 1, 568-576 (7) | -1.4 | -5.4 | -4..-5 (0.4 over) |
| Trumpet 3 accented minus neighbours, 1020-1044 (8) | +1.8 +1.8 +1.4 +3.2 +1.3 -0.6 +0.3 | +2.3 +1.1 +1.7 +3.1 +1.3 +0.3 +3.8 | +2..+3 on all (1044 fixed, median +1.7) |
| muted Trumpet 1 join dips 688 / 715 / 726 / 727 (8) | 3.7 / 5.2 / 4.9 / 2.9 | 4.2 / 3.0 / 4.2 / 0.5 | 3 or less (2 of 4) |
| dips before 888: Horn 1 / Trumpet 1 (8) | 3.5 / 1.6 | 3.7 / 3.2 | 5 / 3 (Trumpet 1 met) |
| bass drum minus basses 30-90 Hz, 888 / 1108 (9) | -4.2 / -3.9 | -0.5 / -0.9 | within 5 dB (met) |
| Horns 2 / 4 notes losing over 2 dB in mono (9) | 11 / 9 | 0 / 0 | 0 (met; correlation 0.54 / 0.65 -> 0.98) |

## Range pass (under the lock)

CTRL is the c24 project as saved; T1 the c25 data (the first build/parts.json). Same starts: -3, 263.25, 455.75, 535.25, 679.25, 831.25, 967.75 (each valid for the measured tracks, `rvalid.py`). T1 build: 5 full rebuilds, exactly the Opus-state changes (Violins I, Violoncellos, Horn 2, Horn 4, Bass drum).
- Violins I chords: the -5 dB CC11 scale plus the region gain removal took the front 8.5 dB and the body 14 dB down (bar 1 -35.4 / -42.8 against Violins II -34.1 / -30.1). Withdrawn: the render plays the c24 lane with the region gain removed (front -27.5, body -32.3).
- Celli: Detache flat in both statements (back - front +0.9 / -0.8); levels refitted: f statement role -5 -> -6.3 dB, ff statement new role -4.5 dB (Detache 4.6 dB over Sus MAX at ff). The render matched CTRL within 0.6-0.9 dB.
- Basses' re-bows at -10 units: rises 3.6 / 2.0 / 5.7 dB; -14 written for the render (2.6 / 1.6 / 4.1).
- Bass drum 40in: +6.7 dB in 30-90 Hz at 888; gain -3 dB for the render (bass drum minus basses +2.5 -> -0.5).
- Every other T1 result transferred to the render within about 1 dB (Horn 1 1-2 dB lower in the render) (`logs/T1_meas.log` against `logs/render/meas25.log`); the full build wrote the T1 lanes except the three refits above (`pdiff`: Violins I CC11, celli vol_db, basses CC11 only).
- Range variance (`logs/T1_eq.log`): notes of unchanged tracks read +0.00 dB T1 against CTRL.

## Changes (files and values)

- **Pipeline fix:** `build/score_config.py` line 1034 had a syntax error (a comment placed before the closing comma, left by the c24 edits after its last build): fixed. No data change.
- **Ruling 1 (inner lines):**
  - Violins II countersubject 632-660: `note_cc` add +13 (sq 631.9-644.9) and +10 (644.9-659.9) on the Sus rows: CC11 75-82 -> 88-92 (under the 94 layer step); `vel_cap` Sus MAX 100 (was 83); `roles.json` [600, 680, -2.9] split into [600, 631.8, -2.9], [631.8, 659.8, 0], [659.8, 680, -2.9] with the edges in rests (`ROLE_EDGE_XF` 631.8: (630.95, 631.8), 659.8: (659.775, 659.85)).
  - Clarinets 1-2 +2 dB at k 20 over 631.7-659.88 (`cc_scale`; Clarinet 1 reaches the CC11 ceiling 127 on its first notes).
  - Horn 1 dolce counter-line: role span [263.72, 295.75, +4, 0.2] (to the breath at 296; the slur runs on past bar 70, so the role ends in the breath, not inside the slur).
  - Theme B: new generic rule `HP_END_AT_TARGET` (`tools/score_to_parts.py`, default off; Finale: spans [(831.5, 840)], within 1 qn, marks up to ff): the 832-839 crescendo gains (+2 brass, +3 strings, +4 winds) now peak at 836.0-837.8 and are 0 by 839.98, falling at 2.8 dB/s at most. Changed on 19 tracks (list in parts.json `hp_end_tgt`). Roles: Trumpet 1 [840, 866, +1] -> [839.79, 856, +3] and [856, 866, +2]; Trumpet 2 [839.7, 866, +2]; Flute 1, Oboe 1, Clarinet 1 span [839.85, 859.7, +1.5, 0.3].
  - Espressivo 862-872: Cor anglais span [863.86, 871.98, +4, 0.15]; Horn 1 span [863.77, 871.75, +2, 0.2]; the violins' held chord at 864 CC11 -5 units (`note_cc`, both sections; a passage level inside the patch instead of B's -3 dB role, whose ramp would have fallen inside the chord before).
  - Muted trumpet / cor anglais 680-744: Cor anglais [680, 744, +2.5]; Trumpet 1 +2 -> +4.5; Clarinet 2 [676, 744] +3 -> +1; Bass clarinet -4 -> -6; Double basses -4 -> -6.
- **Ruling 2 (string chords):** mix.json Violins I `region_gain_db` "Sus Marc LITE" +4 removed (Opus state change: full rebuild). The -5 dB CC11 scale over each chord was range-tested and withdrawn (front -8.5 dB, body -14 dB: Violins I fell under Violins II); kept in the config behind env C25_V1CC=1. Lower strings at 16: `cc_shape` from the note-on [(-0.06, +17), (-0.005, +17), (0, +5), (0.12, +5), (0.30, 0)] on Violins II, Violas, Celli (A's shape re-based on the lane, which steps at the note-on: lane 87-89 -> 104-106 ahead, then 100 + 5 at the knee). Celli at 584: `onset_lead` 0.04 s and the step [(-0.06, +18), (0.035, +18), (0.04, 0)] with a new `cc_shape` key `no_pre_cap` (the accent's pre-note ceiling, taken from the lane before the step, had held the front at 89).
- **Ruling 3 (celli bass line):** both statements on "Detache" (`C24_VC` default "det"); the f statement's CC11 +14 on the Detache row (89-92 -> 99-101); the ff statement role [600, 663.62, -4.5] chained to a 0 row (range fit: Detache 4.6 dB louder than Sus MAX at ff), edges in the 598.9-599.9 and 663.60-663.66 windows; `vel_cap` Detache 91 (39.9-664.1); mix.json celli release cap list adds Detache mp 300 / ff 150 ms; role [39.86, 103.81, -6.3 dB] (range fit: T1 at -5 read +1.3 dB over CTRL) chained to a 0 row [30, 39.86] with the edges in the 39.85-39.88 and 103.80-103.82 gaps.
- **Ruling 4 (basses' re-bows):** `build/rebow_cc11.json` (new) with CC11 counter-shapes [(0, 0), (0.35, -14), (1.6, -14), (2.6, 0)] (range T1 at -10: rises 6.3 / 4.9 / 8.6 -> 3.6 / 2.0 / 5.7 dB, so -14 for the render) at 170.859 / 181.676 / 190.533, read by score_config into `cc_shape` (from the moved note-on); `tools/fit_rebows.py --cc11 DB_PER_UNIT` writes fitted shapes into that file instead of volume fills.
- **Ruling 5 (timpani):** new generic `TIMP_ARRIVAL_RAMP` (`tools/score_to_parts.py`, default []): Finale [(888, 892), (1048, 1050)]. CC7 888.0-891.96: 97 -> 75 dB-linear (c24: 96 -> 36 within 0.01 qn, then 37-42 and 29-32); 1048.03-1049.96: 51 -> 36 (c24: 36 flat).
- **Ruling 6 (harp):** `vel_cap` 96 on the 524 chord (was 123); mix.json Harp dyn_trim ff +2 -> -2; role [488, 512] -6 -> -10.
- **Ruling 7 (Oboe 1):** CC11 kept (82-88); role span [567.9, 575.9, -4, 0.22] (edges in the 567.42-567.92 and 575.68-575.92 gaps).
- **Ruling 8:** Trumpet 3 accents 1016-1048: CC11 hold 0.15 -> 0.20 s, back by 0.35 s; CC1 bump +3 -> +7, held 0.25 s, back by 0.40 s, max 112 -> 127; the 1040-1048 crescendo ceilings (cc_cap CC11 102-106, CC1 108-116) now hold the resting lane only (`cc_cap` new key `acc_free`, `tools/instr_post.py`). The cause of the missing bump at 1044: the ceiling (A asked). Trumpet 1 muted solo: pitch-changing joins inside the slurs 680-694 and 712-728 overlap 0.06 s (`gap_set` rows "Mute"); leads 688 / 715 / 727 0.035 -> 0.075 s, 726 0.085 -> 0.125 s. Horn 1 / Trumpet 1 CC1 taper before 888: [(-0.38, 0), (-0.14, -25), (-0.006, -25), (-0.005, 0)] (-25 on the raw lane: the 108 ceiling of the crescendo absorbed 10 of the critic's 15 units; played 108 -> 92-95).
- **Ruling 9:** mix.json `loud_eq` (ff / fff spans, Violins I's points): celli bell 160 Hz +3 dB (1.5 oct), Trombones 1-2 bell 180 Hz +2 (1 oct), Violas bell 200 Hz +2 (1 oct), Trumpets 1-3 high shelf 5 kHz -4. Bass drum: 36in -> 40in Ludwig (`_BD_PATCH`, env C25_BD), gain -1.4 -> -4.4 dB (range T1: +6.7 dB in 30-90 Hz). Horns 2 / 4 `channel_map` 2 and gain 2.0 -> 1.0 dB (full rebuilds).
- Tracks whose Opus state changed (full rebuild): Violins I, Violoncellos, Horn 2, Horn 4, Bass drum.
- **Delivery (after the render):** RIDE_TRIMS final -4.5 -> -5.5, bar 223 -7.4 -> -8.4, bar 263 -2.0 -> -2.6, new row bar 212 (844-848) -1.0 dB (variant c of five simulated on the c25 master).

## Coordinator's scherzo note (read during the lock)

- "Marc Lng RRx4" (6 ms attack) for the lower strings' chord fronts: not used; it is a short row and cannot hold the printed half and whole notes. The lower strings' 16 / 584 fronts were done in CC11 (Violins II's -3 dB point at 16 moved +280 -> +100 ms in the range test, +280 in the render: variance or the restart, not settled).
- CC11 lifting the previous note's tail: the Violins II note_cc offsets start 0.02 s before each note-on (`pad_s`), so the earlier note's tail rises for 20 ms only. The CC1 floor alternative was not tried.
- Doubling tracks counted in a line: the theme B and espressivo measures sum the doubling tracks (Trumpets 1-2, Flute 1, Oboe 1, Clarinet 1; cor anglais + Horn 1).
- The -9 dB 3:1 peak compressor: not needed (the final leads by 0.7 LU after the ride refit).

## Rejected or deferred

- Violins I -5 dB CC11 scale over the chords (B #1): rejected on the range numbers above (LITE CC11 is not 20 log10 on this row). The marcato fronts stay 5 dB over Violins II: the region gain removal lowered only the sustain body.
- A's Trumpet 3 alternative (resting lane -3 dB and a +3 dB role): not needed for the ruling's B version.
- Lower strings on "Sus Marc LITE" (A's second option): not tried (c24 range negative on these sections).
- "4 soli" DIV track (C #5) and celli legato sags 286 / 860: not this cycle (coordinator).
- Theme B: the violas' chord still 5.2 dB over Trumpet 1 on the downbeat; a violas role was not ruled and not added.
- Stops after bars 94 / 113 at 13.1 / 13.5 dB on the mp3: not treated (no data change touches those cut-offs directly; to check in c26 with return rides).

## Faults introduced or left

- mp3 stops after bars 94 / 113: 14.9 / 14.4 -> 13.1 / 13.5 dB (under the 14.5 floor).
- 263 over 262 on the mp3 +0.6 -> +0.3 dB; 223 over 222 +3.1 -> +2.5 (the ride refit lowered 223 and 263 to keep the final ahead).
- Bar 223 and bar 263 tie on the mp3 (c24: 223 0.1 over).
- Not measured: Horns 2 / 4 per-pitch levels and Horn 3 against Horn 4 after the routing change (c19 found +1 to +2.5 dB on Horn 3 after the same switch).
- Clarinet 1 reaches the CC11 ceiling (127) on the first notes of bar 159 (+2 dB asked, about +1.5 delivered).
