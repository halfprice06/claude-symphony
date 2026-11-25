# Cycle 52 (actor): one legato row per string line, early keyswitches on the row changes that remain, level-only repairs

Rendered 2026-11-10 17:00-17:08 (one full render; range passes of the three string passages and one whole-piece
string pass for the test and the refit). Critic reports `reports/A.md`, `B.md`, `C.md`; the lead notes
(`lead_c52.md`, `lead_c52_inbox.md`) and three additions sent during the cycle were followed (test V2 first; check
start against body on the notes that change row; disk and resume instructions).

## 1. String join timing (critic A #1; the cycle's main item)
Test method: the three passages (bars 22-30, 53-60, 70-78; 127 of the 163 row-change joins of the four section
tracks) rendered as string stems, twice or more from one unchanged project, S by `tools/s_onsets.py`
(`actor_scripts/range52.py`, `cmp52.py`, `rows52.py`). Joins moving 25 ms or more (60 ms or more):

| Build | passes compared | former row-change joins (127) | joins same-row in c51 (154) |
|---|---|---|---|
| c51 rows (control) | c51a / c51b, one session | 6 (5) | 0 (0) |
| c51 rows | c51a / c51 full render, two sessions | 28 (14) | 4 (1) |
| V2 (all on Leg Slur MAX) | V2b / V2c, one session | 6 (1) | 0 (0) |
| V2K (V2 + keyswitch 0.15 s early) | V2Ka / V2Kb, one session | **0 (0)** | 0 (0) |
| V2K, first refit | V2Kc / V2Kw, two sessions, same data | 6 (0), all Violins II | 2 (1) |
| V2K | V2Kw / c52 full render, two sessions, lead changes taken out | 1 (0) | 3 (1) |

- V2 alone missed the limit of 2: its six movers are all among the 13 row changes it leaves in the passages (Sus MAX
  re-bow pieces into a legato row, into and out of Leg Port MAX); none of the 268 joins that are same-row under V2
  moved. V2a is not used: the violas and celli were still loading samples 69 s after their full rebuild and started
  200-400 ms late (74 of 281 joins differed from V2b).
- **Kept: V2K** = V2 (`BC_SOFT` on every string track at any dynamic, `BC_SOFT_SKIP` empty) plus V1's mechanism on
  the row changes that remain (new generic `KS_ROWCHANGE_LEAD_S` 0.15 s in `tools/score_to_parts.py`; 30 keyswitches).
  V1 alone (c51 rows with early keyswitches) was not tested: the lead's addition put V2 first and V2K needed no rebuild.
- The early keyswitch does not change the note still sounding: in the window between the new keyswitch time and the
  target's note-on the stem differs by a median 0.00 dB from the pass without it (`ksrow_V2K.txt`). With it the
  portamento joins take their later start every time (+50 to +108 ms against V2), so their leads were refitted.
- Loop-lead check, start against body (first 150 ms minus the body from 300 ms; 62 notes of a quarter or longer that
  moved to Leg Slur MAX, control pass against V2 pass, `startbody_V2K.txt`): median -2.1 -> -2.6 dB (change median
  -0.7 dB), so no general growth. 11 notes grew by more than 3 dB and 8 fell by more than 3 dB. Worst: Violas div 87
  (+7.2), Violoncellos 81 (+5.1), 253 (+4.7), 202 (+4.4), 186 (+4.4), 261 (+4.3), 193 (+3.8), 188 (+3.6), 182 (+3.0),
  Violins I 87 (+4.5), 80 (+3.3). For c53.
- Refit of leads (`build/leg_leads.json`): first refit of the former row-change targets on V2Ka / V2Kb (91 rows
  changed, 14 kept, 13 outside the passages deleted; `leads_refit.json`). The check pass then showed that 34 of the
  154 joins that were already same-row in c51 had dropped out of the 60 ms band (24 remained outside, mostly violins,
  70-150 ms early, the same in two sessions): with no keyswitch between the notes they take the earlier of the two
  start times. Second refit on a whole-piece string pass (`refit2_52.py`, `leads_refit2.json`): 83 rows inside the
  passages (W and C readings and the latency of A agree within 25 ms), 88 outside (one reading), 12 left where the
  readings disagree. 76 early fills moved with their note-ons (`fillshift52.py`). The second refit was not
  range-rendered before the full render.
- What V2 loses: 116 notes that played Leg BC MAX (a sampled bow change) now play Leg Slur MAX with the 3-4 CC bow
  change notch; a printed bow change or new slur there has no separate attack. List by track and bar: `bc_lost.txt`.
  The 30 remaining row changes are in the same file. Leg BC MAX is no longer loaded on six string tracks.
- Result on the full render, by S (`S_report_c52.txt`; c51 -> c52): all 727 joins within 25 ms 522 -> **647**, within
  60 ms 678 -> **706**. Four string sections (439 joins): within 25 ms 275 -> 390, within 60 ms 398 -> 421. All 26
  lines: outside 25 / 60 ms 112 / 28 -> 58 / 18 of 410. Wind and brass joins unchanged (28 / 2 of 263 outside).
- Violins I against Violins II on the 82 common onsets: over 60 ms apart 14 -> **7** (6 + 0 + 1; max 184 -> 103 ms).
  The six are in bars 22-27 (66, 72, 74, 75, 78, 80), where Violins II is the track that still moved between
  sessions. Violins II 197.5: S +33 -> +14 ms (Violins I -31 -> 0; leads 250 / 220 ms). Its level over the half beat
  is still 3.7 dB under Violins I (-37.0 against -33.3; c51 5.6, c50 0.9): a level row for c53.

Thematic string lines by S (ms), c51 against c52:

| Line | c51 min / max / median | outside 25 / 60 | c52 min / max / median | outside 25 / 60 | of |
|---|---|---|---|---|---|
| Violin I solo, bars 17-22 | -26 / +109 / +8 | 4 / 2 | -17 / +109 / +2 | 2 / 2 | 11 |
| Violins I, theme A, bars 22-30 | -41 / +126 / -0 | 10 / 2 | -25 / +70 / -0 | 2 / 1 | 24 |
| Violins II, theme A, bars 22-30 | -58 / +92 / -7 | 8 / 1 | -127 / +46 / -5 | 8 / 5 | 24 |
| Violoncellos, counter-melody, bars 22-30 | -64 / +73 / +12 | 8 / 3 | -18 / +38 / +6 | 2 / 0 | 19 |
| Violoncellos, B flat minor head, bars 45-47 | -54 / +70 / +1 | 3 / 1 | -20 / +153 / -1 | 2 / 1 | 9 |
| Violins I, theme B, bars 53-60 | -96 / +88 / -9 | 10 / 3 | -18 / +24 / +1 | 0 / 0 | 30 |
| Violins II, theme B, bars 53-60 | -77 / +85 / -2 | 11 / 2 | -15 / +39 / +4 | 3 / 0 | 30 |
| Violoncellos, bars 53-60 | -40 / +44 / -10 | 4 / 0 | -20 / +24 / -2 | 0 / 0 | 19 |
| Violins I, climax, bars 61-64 | +14 / +229 / +30 | 3 / 2 | -1 / +229 / +37 | 3 / 2 | 5 |
| Violins I, theme A', bars 70-78 | -57 / +101 / -4 | 7 / 3 | -34 / +19 / -4 | 2 / 0 | 28 |
| Violins II, theme A', bars 70-78 | -78 / +100 / -11 | 11 / 2 | -44 / +40 / -6 | 4 / 0 | 28 |
| Violoncellos, counter-melody, bars 71-78 | -88 / +26 / -20 | 8 / 1 | -56 / +41 / +2 | 3 / 0 | 18 |
| Violins I, cadence, bars 79-82 | -86 / +21 / +1 | 2 / 1 | -2 / +89 / +10 | 2 / 2 | 9 |

Worse than c51: Violins II bars 22-30 (5 outside 60 ms, was 1), Violins I cadence (2, was 1), the celli's note at
bar 45-47 (+153 ms).

## 2. Other findings
Applied:
- A2 (S1): -9 dB gap shapes at Double basses 144 / 156 / 168 (20 ms stem level in the gap: 144 -55 -> -65 dB,
  156 -60 -> -69, 168 -48 -> -57). `s1check44.py` own-band reads 0.3 / 4.9 / 0.0 dB at these low pitches although
  the stem dips 8-10 dB, so 144 and 168 still count as failing by that measure. Violins II 120 own-band 2.6 -> 6.8 dB,
  Violins II div 120 2.0 -> 5.8. New generic `REP_GAP_AT`: Horn 2 208 (gap 33 -> 80 ms with a CC11 fall) and Violas 81
  (the note before ends 150 ms before the beat). Neither is in the 49-point S1 list and neither was measured after the
  render. S1 list: own-band median 7.1 -> 8.0 dB, under 3 dB 6 -> 4. A's `sus_fall` code change was not made.
- A3: lifts over the holes of the nine wind joins, fitted on the c51 stems (`joinfit52.py`, `build/level_fits.json`):
  holes 7.8-10.7 dB -> 2.6-4.4 dB, no 50 ms peak more than 2.0 dB over the higher body; 9 of 9 pass on the render.
- A4 / B1: `tools/fit_rebows.py` made the fills worse on stems that already carry fills (steps of -4 to -5 dB), so its
  result was discarded; residual corrections instead (`resid52.py`) at seven re-bows. Dips: Violoncellos div 275.527
  6.2 -> 1.9 dB, 277.599 3.8 -> 1.1, 284.141 7.0 -> 3.3 (step -3.8 -> -1.3; fill at its +10 dB cap); Double basses
  225.215 4.5 -> 3.8 (cap), 227.775 2.5 -> 1.2, 233.038 3.0 -> 1.0, 235.659 4.4 -> 1.2; Violoncellos 293.6 3.4 -> 0.8.
  Left alone: Violins II 292 and Violas div 289 / 291.7 (printed soft repeats that need their dip).
- A5: Violins I 249 lead 0.18 -> 0.26 s (later refitted with the other joins).
- B3 (check only): `actor_scripts/check52.py` keeps the string stops by score position (qn 9, 90, 138).
- B4 Bass clarinet 108 shape timing: 30 ms steps now -42.3 ... -44.8 dB with no bump (C3 before: -45.0).
- B5 Flute 1 108: hole under the head 4.1 -> 2.6 dB. The second test at 111 reads +2.6 against the new 3.0 limit.
- C1 breaths (gap; stem dip by `breath52.py`, c51 -> c52): Flute 1 196 95 -> 190 ms, 10.6 -> 29.1 dB; Oboe 1 196
  95 -> 190 ms, 8.9 -> 24.8; Trombone 2 204 74 -> 177 ms, 3.2 -> 13.7; Bass trombone 204 24 -> 170 ms, 1.4 -> 14.4.
  **Horn 1 196 fails**: 137 -> 184 ms but the dip is 5.9 dB (need 10). Master dip 196 3.8 -> 4.4 dB (limit 5),
  204 2.5 -> 3.9 (limit 4).
- C2: `tools/deliver_master.py` rise delay, mix.json `"deliver": {"rise_delay_s": 0.6}`. On the c51 master: mp3 level
  over qn 219-220 -0.8 dB, 269-271 -0.9 dB; LRA unchanged, limiter 1.0 -> 0.9 dB.
- C3: `actor_scripts/pdiff52.py` lists every printed breath's gap in ms, old and new (`pdiff_c51_c52.txt`). One gap
  under 120 ms remains: Bassoon 2 at 268 (116 ms, unchanged).
- Inbox, finale technique 44 on the bars 36-37 Cor anglais removal: none of the three effects (the note at 99 has no
  trim running on, its length is its breath gap, the entry at 124 keeps velocity 53 and its CC lanes).
After the render, by stem fix: the notes that moved to Leg Slur MAX played softer at f-ff (celli bars 60-62 and 78-81
-2.3 to -5.2 dB per bar, single notes to -7.2 dB). 66 per-note level rows (`rowlevel52.py`, `build/level_fits.json`)
restore the c51 body level within 1 dB on 109 of 110 notes. Originals in `render_first/`, pre-fix data in
`rendered_build_first/`. The return stems were not re-simulated. **REAPER still holds the envelopes from before the
stem fix on Violins I, Violins II, Violas, Violoncellos, Violoncellos div and Violas div: the next actor must write
them (`--mix-only` or `--midi-only` on these six tracks) before rendering.**

Not done / open: Violins II 197.5 level; Horn 1 196 breath; the 11 long notes with a stronger start; Violins II bars
22-27 (still moves between sessions); 12 joins whose readings disagreed; basses 144 / 168 by the own-band measure;
Double basses 225.215 and Violoncellos div 284.141 at the fill cap; final chord t20 0.46 s (inside 0.45 +- 0.02).

## 3. Render, state, checks
- Lock: waited 09:56-12:19 (the first waiter ended at about 10:58 with its background task and was restarted at
  11:31; the finale went first). Held 12:19:12-17:09:41 = **4 h 50 min**, of which about 3 h 3 min idle (13:45-16:48,
  a usage limit stopped the actor with REAPER open) and about 1 h 47 min of work.
- REAPER deadlocked once (12:58, main thread waiting for the track lock in the Violins I MIDI job 35 s after a range
  pass; killed 13:09, restarted from the saved V2K project). The first two control passes wrote only a master file
  (`RENDER_SETTINGS` 2) and were deleted; 1 with the string tracks selected gives the stems.
- State guard: 0 stale before the work, after each build, before the render, inside `render_cycle.py`, on the
  post-render save and on the project saved by quit. Trombone 1 was stale once (after the whole-piece pass) and was
  rebuilt in full before the last restart.
- state_check: against c51 no state run and no timing run; against c50 three runs (Clarinet 2, Violas, Double
  basses), the same map artefacts as in c51 (one map for both renders).
- Master after the stem fix: -22.9 LUFS, LRA 23.4, true peak -4.6 dBFS, sample peak 0.585 (c51 -22.8, 23.4, -3.7,
  0.654). Delivered: -19.7 LUFS, LRA 14.7, TP -1.6 dBTP, limiter about 1.2 dB, p10-to-max span 18.2 dB, 347.40 s.
  Attack probe: late or hole 0. Motion dS4 p90 6.91, 1 s / 20 s 4.30.
- Wetness t20 by the corrected check (fixed stops): strings 0.434 s (c51 like for like 0.414; stops 0.665, 0.434,
  0.372), winds 0.284, brass 0.272; final chord 0.46 s (t10 0.285), unchanged.
- REAPER memory: 39 GB / 0 compressed before the render (no `--force-memory`), **40 GB / 0.6 GB compressed after**.
  Audio device at every reading: CoreAudio, Mac Studio Speakers, 48000 Hz, 512, no input; no setting changed.
- Disk: 36 GB at launch, 19 GB at 12:19 (other threads' renders), 97 GB before the render after the coordinator had
  space freed. Range-pass audio deleted, measurements kept.
- S3 (`check46_c52.txt`): steepest 10 ms fall of the master at the caesuras at most 1.1 dB (139); dips at the kept breaths 5.6 (29), 9.5 (102), 8.4 (124), 4.0 (268), 2.8 dB (286).
