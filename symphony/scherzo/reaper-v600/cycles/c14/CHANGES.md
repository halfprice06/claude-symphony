# Cycle 14: changes (actor, on the c13 render)

Snapshot before this cycle: `cycles/c14/before/`. Data as rendered and stem-fixed: `cycles/c14/build_render/`. Scripts:
`cycles/c14/actor_scripts/` (`apply14.py` mix and table edits; `themefit14.py` theme-head level rows; `rebowres14.py`
re-bow residuals; `eqsim14.py` EQ simulation on stems; `envdiff14.py` envelope diff of two builds; `envstats14.py`
envelope points per track; `check14.py DIR [blocks]`; `hall14.py CYCLE` hall check with the corrected soft-end measure;
`s14.py` measure S on legato joins; `wholepass14.py`, `refit14.py`, `fillshift14.py`, `rowlevel14.py`, `scmp14.py` the
one-row refit; `lk.sh` lock-phase steps; `wait_lock.py` queue waiter). Records: `cycles/c14/records/`.
Do not rerun `apply14.py` by itself: it rewrites the tables from `before/` and would drop the refitted
`leg_leads.json`, the moved early fills and the stem-fix roles (the final tables are in `build/` and `build_render/`).

STATUS: rendered once on 2026-11-11 (06:59-07:13 CST, freshly restarted REAPER, 43 GB settled, 0 GB compressed). One
stem fix after the render (level only: Violoncellos and Harp roles; originals in `cycles/c14/render_first/`) and a
second delivery of the same master (two delivery rows). Lock held 05:44:05-07:16:38 CST (92.5 min) after a wait from
19:10 on 2026-11-10 behind Movement II, Movement I and the finale (the session also stopped on a usage limit from
22:08 to 04:57). mp3: `cycles/c14/scherzo-mockup-c14.mp3`.

**REAPER is one step behind `build/`:** the stem-fix roles (Violoncellos `[312, 360, 2.5]`, `[912, 960, 2.5]`,
`[624, 672, 1.5]`; Harp `[216, 240, -1.5]` -> 0) are in `build/roles.json` and `build/parts.json` but were made after the
unlock. c15 must write them first (`build_reaper.py build/parts.json jobs --mix-only`, or build those two tracks).

Positions are score quarter notes (qn); bar b starts at qn 3(b-1). Levels are plain mean-square dB unless noted.

## Result in numbers

| | c13 | c14 |
|---|---|---|
| master | -21.0 LUFS, LRA 23.4, TP -1.6 | -20.8 LUFS, LRA 22.7, TP -1.5, sample peak 0.835 |
| delivered mp3 | -19.8 LUFS, LRA 15.0, TP -1.6, limiter 2.8 dB, span 19.8 | -19.8 LUFS, LRA 14.9, TP -1.5, limiter 3.0 dB, span 19.8 |
| attack probe | late or hole 0 | late or hole 0 |
| measure S, `timing13.py` (16 tracks, Allegro sections) outside 25 / 60 ms | 749 of 2679 (28 %) / 154 (6 %) | 702 of 2678 (26 %) / 141 (5 %) |
| legato joins, whole movement (`s14.py`), outside 25 / 60 ms: Violins I | 48 / 7 of 100 | 9 / 3 of 100 |
| Violoncellos | 101 / 23 of 200 | 24 / 9 of 200 |
| Violin I solo | 10 / 2 of 18 | 3 / 0 of 18 |
| Violins II (control, data unchanged but for two strokes) | 40 / 10 of 104 | 43 / 13 of 104 |
| hall: G.P. drop at +0.3 s, 20 dB fall, RT60 | 20.7 dB, 0.27 s, 1.30 s | 20.7 dB, 0.24 s, 1.30 s (final chord 20.6 dB, 0.29 s, 1.32 s) |
| soft ends, from the note-off on the dry stem (`hall14.py`) | 0.06, 0.22, 0.12, 0.11 s | 0.06, 0.22, 0.12, 0.10 s |
| returns re dry | -12.71 dB | -12.81 dB |
| REAPER memory | 45 GB settled | 43 GB settled, 43 GB / 0 compressed after the render (65-68 GB during the refit passes, before the restart) |

Tracks with unchanged data reproduce c13: Horn 1 -0.03 dB, Trumpet 1, Trombone 1, Oboe 2 0.00 dB (whole stem).

## Timing (critic A)

| finding | status | change | measured c13 -> c14 |
|---|---|---|---|
| A #4 one legato row per line | accepted, with the full refit | `ROW_REMAP` Leg BC MAX -> Leg Slur MAX on Violins I, Violoncellos, Violin I solo; `KS_MIN_LEAD_S` 0.15 on the three; Leg BC MAX unloaded. Refit of every legato join of the three tracks on whole-piece passes of the three stems (three passes per step, the first discarded): step 1 offset + mean S (250 rows), step 2 gain 0.8 (65 rows); `build/leg_leads.json`; 17 early fills moved with their note-ons (`fillshift14.py`); join notches now in seconds from the note-on (new generic `JOIN_NOTCH_S`, ported from Movement II c53) | two passes of identical data: 1 of 100, 1 of 200, 0 of 18 joins moved 25 ms or more; the full render (another session) against the last pass: 2, 1, 0. Outside 25 ms: Violins I 48 -> 9 of 100, celli 101 -> 24 of 200, solo 10 -> 3 of 18 (table above). Row level: former Leg BC notes of 0.45 s or more start -2.0 dB (Violins I), -6.2 dB (celli), -1.0 dB (solo) softer; 19 notes 3 dB or more softer got a flat step (`build/c14_row_levels.json`, at most 6 dB, crossfade on the score onset). Memory 45 -> 43 GB |
| A #1 / B #1 theme head (Violins I, nine soft statements) | accepted, one combined level fix | A's velocity cure tested on a whole-piece pass and rejected (below). c13's pair rows replaced by one row per figure fitted on the c13 stem (`themefit14.py`): lift of the half note's second beat (0 to +3.5 dB), one level for both eighths (-7 to -11.5), the landing staccato (0 to -8); every step is a 0.04 qn crossfade on the next note's score onset (Movement I c56). Rows, leads, velocities, note ends as c13 | pair against the half note's first 300 ms -4.6..-10.4 -> -2.5..-3.7 dB; landing staccato against the pair +3.1..+13.4 -> -1.4..+1.3 dB; half note's last 140 ms against its first 300 ms -7.1..-14.7 -> -4.7..-7.8 dB (`records/check14_c13.txt`, `check14_c14.txt`). The MIDI is c13's, so the timing is c13's; the landing notes at 42, 288, 774, 798 now read S -61..-130 ms because their level step falls on the beat (a reading effect of the step, coordinator note 2026-11-11) |
| A's velocity table for the eighths | tested, rejected | eighths at v56-70 instead of v78-94 (`C14_THEME=vel`) | the eighths played at -26..-31 dB against -32..-39 for the half note (5-11 dB over, as before): Sus Marc LITE does not take its level from velocity |
| A #3 late legato heads after short notes | accepted in part | `DOWNBOW_STROKE_AT` + 0.06 s `REATTACK_LEAD_AT` + new generic `REATTACK_KEEP_END` (the pickup keeps its end): Violins I 144, 157.5, 385.5, 853.5; Violins II 144, 123, 819, 853.5; Violas 144, 855; celli 157.5, 853, 207, 891, 648, 840 | S: Violins I 144 +116 -> +76, 157.5 +84 -> -7, 385.5 +80 -> +37, 853.5 +52 -> +37; Violins II 144 +105 -> +34, 123 +127 -> +62, 819 +125 -> +46, 853.5 +162 -> -45; Violas 144 +139 -> +28, 855 +55 -> +68; celli 157.5 +90 -> -6, 853 +124 -> +7, 207 +99 -> -18, 891 +141 -> -14, 840 +164 -> +56. Not done: Violas 382 / 387 (as strokes they took the lead of the repeated note after them), celli 171 (p: a soft stroke speaks as late). Violas 828 entry lead +0.13 s: +187 -> +261 ms, worse (take it back in c15) |
| A #5 Flute 2 in 912-960, Oboe 1 lead | accepted in another form | Flute 2's lead request was already 100 ms and capped at 51 ms on eighths; the 17 joins of A's eight slow pitch pairs are listed in `leg_leads.json` and take `LEG_CAP_FRAC` 0.75 "listed" (85 ms). Oboe 1 `LEG_HEAD_AFTER_ROW_LEAD_S` 0.055 -> 0.02 | Flute 2 912-960: over 60 ms 14 -> 7 of 65, over 25 ms 35 -> 34, median +13 -> +12. Oboe 1's loud heads -42..-56 -> -5..-20 ms; Oboe 1 over 25 ms 45 -> 33 of 231 |
| A #6 celli fugato pairs | accepted | `SHORT_SUS_LEAD_AT` 0.16 -> 0.10 | 173 -76 -> -11, 173.5 -36 -> -11, 869 -52 -> -7 |
| A #6 soft-end check | accepted | `hall14.py`: from the note-off on the dry stem, reference the 50 ms before it | all four ends 0.06-0.22 s in both cycles; hall unchanged |
| A #2 celli trio tune | superseded by the one-row refit | | joins of 504-552 are part of the celli total above |

Not done from A: first eighths' lead 0.09 -> 0.07 s (the pair rows are fitted to the c13 timing), CC11 dip between
same-pitch staccato pairs on trumpets and celli, removal of the `STAC_LEN_SPANS` 0.7 rows (no audible effect either
way), CC1 phrase shape on the solo.

## Balance (critic B)

| finding | change | measured c13 -> c14 |
|---|---|---|
| B #2 low-mid weight (Dan: mushy) | `mix.json`: Double basses bell 87.3 Hz -10 and mute bell 61.7 Hz -6 removed (73.4 Hz kept), loud_eq 160 Hz +6 -> +3 and 98 Hz -4 -> -2; Tuba bell 84 Hz removed; Violoncellos bells 170 / 125 Hz +3 removed, gain 0.54 -> 1.0. Basses' pizz. pitch trims E1 +2 -> 0, E2 +1 -> 0; the eleven arco E2 rows +3 -> +1; ff arco E1 / B1 of the two tuttis +2 (22 note trims) | 70-112 Hz share: tuttis -16.3 / -16.9 -> -14.7 / -15.0 dB (B's figure -14.5), trio 153-168 -18.4 -> -15.7, Meno mosso -17.6 -> -15.1, whole -15.3 -> -14.4. 140-355 Hz share: tuttis -7.1 / -7.6 -> -7.8 / -8.5, reprise -7.1 -> -8.6, trio 169-184 -5.1 -> -5.3 (B's -6.3 not reached: the tune got +2 dB back, below). Master level per passage within 0.7 dB except the F major episode (-1.15 before the harp fix). Bass notes ff arco: E1 -33.8 -> -32.1, B1 -34.2 -> -32.4, A1 -31.8 -> -31.2, G1 -31.2 -> -29.1: the gap from E1 / B1 to A1 closed by 1.1-1.2 dB, to G1 (one note) it stayed. Limiter 2.8 -> 3.0 dB |
| deviation from B | the 98 Hz band halved, not removed | removing it lifted G1 / G sharp 1 / A1 by 1.9-3.9 dB against +0.7 for E1 / B1 (simulated, `eqsim14.py`) |
| cellos after the bell removal (coordinator, Movement II c53) | roles: fugato 168-180 / 864-876 +5, trio tune 504-552 +2; stem fix: tuttis 312-360 / 912-960 +2.5, 624-672 +1.5 | celli stem: fugato -43.4 -> -40.9, trio tune -39.8 -> -39.4; before the stem fix the tuttis read -30.8 -> -33.9 and 624-672 -39.1 -> -40.6 |
| B #3 harp, bars 73-80 | left hand (31 notes, A3 and lower) velocity 56 -> 46; role -3 -> -1.5, then 0 in the stem fix; bell 200 Hz -4 | harp 158 + 198 Hz bands against its 630-1000 Hz bands +6.5 -> -0.1 dB; harp level -37.9 -> -40.9 before the stem fix (+1.5 after); passage 140-355 Hz share -2.9 -> -3.9 |
| B #4 clarinets | roles as B gave them | bars 269-270: Clarinet 2 -43.0 -> -49.0 (Bassoon 1 -48.4), Clarinet 1's G4 -51.7 -> -47.7; bar 134 chord -36.3 -> -41.3 (bar 133 -42.5); bars 29 / 33 Clarinet 2 -47.5 -> -49.5 |
| B #5 Flute 1 staccato eighths | pitch trims on the staccato row B4 +6, D5 +5, B5 +3; first quarters at 84 / 96 -2 | envelope +5..+6 dB on the eighths (not measured per note on the render) |
| B #6 solo send | `send_offset_db` 3.6 -> 2.4 | R Strings re dry -14.82 -> -15.30 dB; solo level -40.5 -> -40.2 |

## Dynamics (critic C)

| finding | change | measured c13 -> c14 |
|---|---|---|
| C #1 fugato p entries | roles: celli +5 (168-180, 864-876), +2.5 (180-198); Violas +5 (180-192), +3.5 (192-198), +4 (876-888), +4.5 (975-978); Violins II 192-198 +4 -> +5.5; two delivery rows +2 dB (`RIDE_TRIMS`, second delivery) | master bars 57-60 -42.3 / -46.1 / -42.9 / -43.0 -> -40.1 / -42.7 / -41.0 / -40.3; 61-64 mean -44.4 -> -40.7; 65-66 -41.7 -> -40.0; delivered bars 57-60 were -34.8..-36.9 after the first delivery (c13 -36.2..-39.9; ppp opening -32.0 / -31.1), hence the rows; delivered span 19.8 dB (target 19 not reached) |
| C #2 crescendos taken back by the trim tables | new opt-in rule in `build_reaper.py` `vol_points`: `mix.json` `cresc_trim_hold` {keep 0.3, release 0.5 s, groups wind and string, at most 3.5 dB held, not on hairpins starting in 297-312 / 897-912}; f anchors Flute 1 / 2 -4 -> -1.5, Clarinet 1 -4.2 -> -1.5, Clarinet 2 -3.8 -> -1.0 | arrival against first note: Clarinet 1 840-852 -3.0 -> +1.9, Clarinet 2 372-384 -5.8 -> -0.8, Clarinet 2 576-588 +1.9 -> +5.9, Flute 1 144-156 -2.4 -> +1.5 dB; Violas 900-910 unchanged (skipped: the sfp). Winds minus strings at bars 129 / 197 / 285: -4.6 / -3.9 / -3.8 -> -3.6 / -2.5 / -3.1. Brass minus winds in bars 105-108 -2.2 / -4.2 / +2.4 / -3.6 -> -0.9 / -4.2 / +2.2 / -3.7; summit bars 336-338 master -15.3 / -14.7 / -14.9 against bar 304 -18.5 and the first eighth of 312 / 912 -15.8 / -16.2. Cause checked (coordinator): our tables fall 9-10.9 dB from p to f on these tracks, Movement II's 4.5-6.3. My own count of all hairpins (first sustained note against the arrival) did not improve (32 -> 37 of 158 under +0.5 dB on the simulation, several of them sfp hairpins measured from the sf note): C's count of 40 of 215 was not reproduced with my script and is not re-claimed |
| C #3 last re-bow | residual corrections added to the fills at 1116.299 and 1125.156 (`rebowres14.py`) | frames after 1125.156 against the 0.3 s before: -1.7..-5.5 -> -0.8..+0.6 dB; 1116.299 -0.3..-4.2 -> -0.6..+0.8 |
| C #4 single notes | Clarinet 1 note trims 243 -5, 735 -2, 904 -5 (not pitch trims: they would take 3-5 dB off the ff tutti); Bassoon 1 early fill 699 4.6 -> 1.0, note trims 699 -3.5 / 702 +3.5; Oboe 1 1036 +3 and a -4 dB step over 1038-1040 | Clarinet 1 243 against the note before +10.7 -> +4.7; Bassoon 1 699 / 702 -35.1 / -41.5 -> -36.7 / -37.6; Oboe 1 1036 / 1038 -41.4 / -35.8 -> -38.3 / -39.7 |
| C #5 | Timpani roll shape 713.5-718 to -6; Flute 1 312 / 912 -5 / -4, Flute 2 -4 / -4 (as loud as Flute 1 there) | roll per qn after 712: -55.1, -55.5, -54.9, -53.7, -51.2, -50.0 -> -55.1, -55.7, -56.6, -57.0, -56.5, -55.4; master first eighth of 312 / 912 -14.9 / -14.8 -> -15.8 / -16.2 |

## Volume envelope (Dan, 2026-11-11)

Points of the written volume envelope, points per note and share of notes with more than 3 dB of swing inside the note
(`envstats14.py`; full tables `records/envstats_c13.txt`, `envstats_c14.txt`):

| track | c13 points / per note / over 3 dB | c14 |
|---|---|---|
| Flute 1 | 1813 / 4.9 / 23 % | 1974 / 5.3 / 27 % |
| Flute 2 | 989 / 6.1 / 30 % | 979 / 6.0 / 31 % |
| Oboe 1 | 1976 / 6.5 / 16 % | 2017 / 6.6 / 18 % |
| Clarinet 1 | 2165 / 8.2 / 52 % | 2283 / 8.7 / 51 % |
| Clarinet 2 | 1392 / 5.9 / 20 % | 1477 / 6.3 / 19 % |
| Bassoon 1 | 1729 / 7.7 / 19 % | 1845 / 8.2 / 20 % |
| Horn 1 / Horn 4 | 1251 / 8.1 / 28 %; 720 / 8.2 / 50 % | unchanged |
| Timpani | 999 / 5.5 / 52 % | 1030 / 5.7 / 52 % |
| Violins I | 5477 / 10.7 / 16 % | 5540 / 10.8 / 17 % |
| Violins II | 3582 / 7.1 / 13 % | 3539 / 7.0 / 12 % |
| Violas | 3878 / 7.9 / 20 % | 3963 / 8.0 / 23 % |
| Violoncellos | 3833 / 8.4 / 19 % | 3994 / 8.7 / 22 % |
| Double basses | 1970 / 6.3 / 22 % | 2047 / 6.6 / 22 % |
| all 31 tracks | 39634 / 6.9 / 21 % | 40786 / 7.1 / 22 % |

This cycle did not reduce the envelope: it added about 1150 points (the crescendo hold's releases, 19 row-level steps,
the notch and trim rows) and removed c13's nine six-point pair rows in favour of rows with fewer levels. The level of
the theme-head eighths could not be moved to the velocity (measured above). The split of `vol_points` into slow and
per-note layers for c15's test was not prepared.

## Coordinator messages and ONE_TIME_c14

- Movement II c53 / c54, Movement I c56, finale c15 notes: `JOIN_NOTCH_S` ported; level steps on score onsets; refit
  rows are offsets; differences of 25-30 ms not chased; no Close + Main patch on Violas div; cello themes checked after
  the bell removal; the basses' remaining `mute_eq` (73.4 Hz -5) kept (B: pizz. C sharp 2 is the hottest pitch);
  measure S on the cello leaps 648 / 840 is an entry reading (14 / 16 semitones, not octaves).
- Finale technique 53 (theme head on Sus MAX instead of Sus Marc LITE) was not range-tested: c01 / c02 measured Sus MAX
  strokes at p on these heads 9-15 dB under the staccato before them and slow; open for c15 with a CC11 lift.
- Not used: finale 35 (delivery rise delay; `deliver_master.py` here has no such key), 36, 40, 46 (`RR_RESET_ALL_AT`),
  50, 51; MANUAL-GAPS: none tried (lock time went to the refit).
- State guard: 0 stale at the start; 6 stale after the refit passes (rebuilt); 0 before the render; 3 stale after it
  (Horn 2, Horn 4, Violins I), rebuilt without playback; final save and the project after quit: 0 stale.
- Lock queue: a detached waiter process was refused by the session's permission check; the waiter ran in foreground
  calls of under three minutes with the queue kept in `cycles/c14/lock_queue.json`.
- Disk: c13's stems and range-test WAVs, c14's range-test WAVs (5.7 GB) and `Backups/` (2 GB) deleted; c13 keeps
  `00_Master.wav` and the mp3. 72 GB free.

## Research items

| item | status |
|---|---|
| EW template mix, returns, c08 EQ set, brass widths, seats, wind send, return pans | adopted (unchanged); solo send offset 3.6 -> 2.4 (R Strings re dry -14.8 -> -15.3 dB) |
| one row per string line (Movement I c54, Movement II c52) | adopted on Violins I, Violoncellos, solo with a full refit (joins outside 25 ms 159 -> 36 of 318) |
| keyswitch 0.15 s before a row change | adopted on the three one-row tracks |
| velocity as the level of short notes on a LITE row | rejected with numbers (eighths 5-11 dB over at v56-70) |
| unprinted tempo | rejected in c13, stays out |
| Slur Runs, Stereo Double on Violas div, Close + Main on divisi | rejected / not tried (Movement II c53: per-note levels +1 to +12 dB) |
| CC16 resets everywhere (finale 46), delivery rise delay, CC11 -> CC1 pass 2, separate legato tracks, timpani hard sticks | pending |
