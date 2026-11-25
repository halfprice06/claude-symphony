# Cycle 53 (actor): what the one-row string change left; low-mid weight

Rendered 2026-11-10 19:32-19:40 (one full render; two range passes of bars 20-30 / 78-80 and one test pass for the
Violas div patch before it), stem fix after the render. Critic reports `reports/A.md`, `B.md`, `C.md`; the lead notes
(`lead_c53.md`, `lead_c53_inbox.md`) were followed, and win where they differ from a report. Scripts:
`actor_scripts/` (`lib53.py` is the shared reader / simulator; every figure below comes from one of them).

## 1. Timing (data, rendered)
- **A2, Violins II bars 22-27** (`build/leg_leads.json`): 66 / 72 / 74 / 75 / 78 played lead 240 -> 165 / 155 / 175 /
  165 / 165 ms, 68: 260 -> 240 ms. A row in `leg_leads.json` is added to the track's row lead (Violins I 0.17 s,
  Violins II 0.24 s), the sum clamped to 0.03-0.35 s; the played lead is score onset minus note-on in parts.json
  (`actor_scripts/leads53.py`). Four early fills moved with their note-ons (`fillshift53.py`).
- **A3, Violins I 80**: 170 -> 210 ms (range pass -5 ms, full render -5 ms). **Violins I 262**: A's 230 ms read
  -105 ms in range pass r1 and its note-on lay before the audible start of the run's last note (A flat 6 at 261.833:
  S +11 -> -45 ms, own-band level -1.4 dB); 190 ms read +47 ms in r2 with the run note back at +5 ms. Kept: 190 ms
  (`GROUP_LEAD_AT`). With the start shape of the stem fix it reads +2 ms.
- **A4**: `tools/s_onsets.py` `LINE_SKIP` (Violins I 205.949, 216, 264.417; Violoncellos 148): re-bow / tremolo pieces
  and a same-pitch repeat are no longer line notes. c52 was measured again with it (`S_c52_relined.json`: lines
  outside 25 / 60 ms 55 / 15 of 407, was 58 / 18 of 410). No lead change for Violin I solo 48 / 60, Violins I 210.
- **A5, Horn 2 208**: note-on and gap 40 ms earlier (`REP_GAP_AT` gap 0.12 s, `REATTACK_LEAD_AT` 0.04). Result: gap
  floor at +10 -> -10 ms, dip 10.0 -> 9.6 dB, back within 3 dB of the body at +50 -> +60 ms: no gain at the re-attack.
- **C5**: `HP_CURVE["linear"]` (268, 271) on Flute 1, Oboe 1, Cor anglais, Clarinet 1, Bassoon 1, Horn 3, Horn 4,
  Violins I. Master steps per quarter 268-271 (`dim53.py`): -4.7 / -2.0 / -5.9 -> -4.7 / -2.9 / -4.8 dB (C wanted the
  last at most 4.5); Violins I largest share of the fall in one quarter 74 -> 49 %.

By S (`S_report_c53_fix.txt`, `S_lines_c53_fix.txt`; c52 -> c53 after the stem fix):

| | c52 | c53 |
|---|---|---|
| all 727 joins within 25 / 60 ms | 647 / 706 | 643 / 711 |
| 26 lines, outside 25 / 60 ms (of 407) | 55 / 15 | 54 / 11 |
| Violins II theme A bars 22-30, outside 25 / 60 (of 24) | 8 / 5 | 5 / 1 |
| Violins II 66 / 68 / 72 / 74 / 75 / 78 (ms) | -93 / -30 / -128 / -74 / -76 / -82 | -18 / -16 / -46 / -13 / -3 / -3 |
| Violins I - II over 60 ms apart, bars 22-30 (of 24) | 6 | 1 (86.5, -77) |
| Violins I cadence bars 79-82, outside 25 / 60 (of 8) | 1 / 1 | 0 / 0 |
| Violins I 262 / 80 (ms) | +89 / +70 | +2 / -5 |
| Violoncellos counter-melody bars 22-30, outside 25 / 60 (of 19) | 2 / 0 | 3 / 1 (68: +38 -> -65) |

Before the stem fix the same render read 633 / 709 (see section 3: level shapes move pcX). Violins II's five joins:
range pass r1 -5 / -16 / +13 / +22 / -15 ms, full render -18 / -46 / -13 / -3 / -3 ms; three moved by 25 ms or more
between the two (72, 74, 75), so C's trial `RR_RESET_AT["Violins II"] = [58.0]` is a note for c54 (not done here).
Between r1 and r2 (one session, same data) Violins II 259 and 261 moved by 79 and 124 ms.

## 2. Levels (data in the render; all simulated first on the c52 stems, `lib53.py`)
- **B1 transition peaks.** New generic `JOIN_NOTCH_S` in `tools/score_to_parts.py` ({track: {score onset: (from s,
  to s, dB) | {"shape": [[s, dB], ...]} | list}}, seconds from the target's moved note-on; parts.json
  `join_notch_s`). The 25 string `JOIN_NOTCH` windows that belonged to legato joins were dropped and refitted from the
  un-notched state (`joinpeak53.py`, `notchsel53.py`: 27 shaped rows, cap 12 dB; residuals after the render
  `notchres53.py` -> `build/join_notch_fits.json`: Violins I 271, Violas 249.5). Early fill Violoncellos 68 ended at the
  note-on of 68.5. The c52 body rows of +2 dB or more start on the beat (0 at -0.06 s), not at the note-on
  (`rows53.py`; B's +0.02 / +0.14 s was rendered and replaced in the stem fix, section 3).
  Stem peak over both bodies / master bump, c52 -> c53 (`joinpeak_c52.json`, `joinpeak_c53_fix.json`):
  Violoncellos 68.5 +15.2 / +8.3 -> +2.1 / +3.8 (peak level -25.6 -> -39.1 dB; B: not over -34); 240.5 +8.5 / +5.3 ->
  +2.1 / +1.8; 249 +8.0 / +4.6 -> +2.3 / +0.6; 81 +7.9 / +3.5 -> +2.8 / +0.2; 174 +6.1 / +3.2 -> +2.8 / +1.1; 193
  +10.6 / +2.5 -> +2.4 / -2.2; 77 +6.6 / +4.1 -> +3.3 / +1.1; Violins II 190 +8.6 / +3.7 -> +2.8 / -0.2; 266 +7.0 /
  +2.1 -> +1.2 / 0.0; Violins I 186 +5.5 / +4.8 -> +2.6 / +2.1; 86.5 +7.2 / +4.2 -> +3.8 / +3.6 (B simulated 2.6);
  Violas 256 +7.1 / +1.9 -> +2.6 / 0.0; Violas div 71 +9.0 -> +3.1. Joins 6 dB / 8 dB or more over both bodies:
  35 / 12 -> 20 / 5 of 460; over 5 dB with a master bump over 2.5 dB: 21 -> 3 (Violins I 65.5, Violins II 177: the
  peak lies 60-90 ms before the note-on, on the note before, not a transition; Violas 3, the intro entry).
- **A1 start sags** (`start53.py`, `build/level_fits.json`): start shapes merged into the rows of the new-bow notes
  whose first half second was 2.5 dB or more under c51 (100 ms steps, cap +6 dB), A's shape at Violas div 87, +5 dB
  over 0.07-0.17 s at Violoncellos 148 (A's +4 to 0.30 s overshot c51 after 0.2 s). Moved-row notes of 0.6 s or
  longer with the first half second 2.5 dB or more under c51: 21 -> 4 of 97. Master against c51, worst 100 ms step
  from the beat to +0.7 s (`mstart53.py`; c52 -> c53): qn 71 -4.0 -> -2.2; 84 -3.9 -> -2.8; 176 -2.1 -> -1.9;
  256 -2.3 -> -1.4; 262 -1.9 -> -1.3; 253 -2.5 -> -2.8 (no shape, section 3). A's limit of 1.5 dB per step is met at
  256 and 262 only.
- **B2**: Violins II rows 197.5 (B's shape from -0.25 s at +3.5 dB put Violins II over Violins I in the quarter
  before; used: from -0.10 s, +3.0 / +2.5), 204 / 208 / 210 (+2.0 / +1.9 / +1.4). Violins I minus II (`v2bal53.py`):
  197.5 / 197.75 / 198: +4.9 / +2.7 / +4.7 -> +1.9 / -0.3 / +2.2 dB; bodies 204 / 208 / 210: +4.3 / +5.0 / +5.7 ->
  +2.3 / +3.1 / +4.1.
- **B3 + C4, Horn 1 bars 57-59** (`note_trims.json` 190 -2, 192 +3.5, 198 +3.0 with 0.2 s ramps; the pickup at 195.5
  as a `LEVEL_SHAPES_S` row, +4 dB to the note-off: as a note trim it rang on in the breath). Bodies 188-202
  (`horn53.py`): -37.1 -32.3 -36.0 -29.8 -36.8 -27.9 -31.6 ... -> -37.1 -34.2 -32.9 -29.8 -33.0 -27.9 -29.6. Pickup
  -6.8 -> -2.8 dB against the E flat's body, so C's hold was not added. **Breath at 196**: gap 184 ms (unchanged);
  dip 5.9 -> 8.9 dB by `breath52.py` (9 wanted), 12.4 dB against the body of 193 (C's check, 10 wanted); master dip
  4.4 -> 4.1 dB.
- **B4**: `tools/score_to_parts.py` drops a re-bow fill list's points that lie after the next list's first point (the
  double-counted point at Violoncellos div 284.021, +4.8 dB, is gone; no other track changed).
- **A5**: Violas 81 gap shape -5 dB: dip 5.8 -> 10.6 dB.
- **B5 / C6 (checks)**: `rebow53.py` adds B's acceptance (lowest 50 ms within 0.4 s after the re-bow under the mean of
  0.5-0.9 s after it, limit 3 dB, with the piece's 5th-95th percentile spread): Double basses 225.215 2.4 dB,
  Violoncellos div 284.141 1.6 dB; no fill changed. Final chord t20 0.46 s (limit 0.45 +- 0.02): off the open list.

## 3. Stem fix after the render (level-only; `fix53.sh`, originals in `render_first/`, data in `rendered_build/`
## (as rendered) and `build_fix/` (delivered))
On the first measurement the level shapes had moved S: celli joins outside 25 ms 7 -> 15, Violins II 146 / 154
-1 -> +55 / +135 ms, with no MIDI change. Cause: pcX takes its reference from the highest 30 ms level of the new
pitch up to 0.45 s after the beat, so a lift that arrives after the attack makes the attack read late (and a notch or
a shorter fill before the beat makes it read early: celli 68 +38 -> -65, 77 -4 -> -49 ms). Changes:
- body rows of +2 dB or more: rise from -0.06 s to the beat (was +0.02 to +0.14 s, B #1c);
- start shapes up on the beat (max(step 1, 0.6 x the larger of steps 2-3)), fitted again on the c53 stems, with
  Violins I 262 (A #3); no shape where it moved S by more than 25 ms: Violins I 80, Violins II 146 / 154,
  Violoncellos 253 (their first half second stays 2.9-5.9 dB under c51);
- two residual join shapes.
Simulated first (`S_sim_fix.json`): celli outside 25 / 60 ms 15 / 2 -> 8 / 1, Violins I 262 +47 -> +2 ms. Four stems
changed (Violins I, Violins II, Violas, Violoncellos; gain -6.0 to +7.2 dB). The return stems were not re-simulated.
**REAPER does not hold these stem-fix rows yet**: see section 6.

## 4. Mix (Dan's "mushy" note; C #1; `build/mix.json`, `--mix-only`, `mix53.py`)
Violoncellos bell 170 Hz +3 -> **+1.5 dB** (not removed: removal took 2.8 dB off the celli's fundamental band,
147-277 Hz, against the other stems in bars 22-27 and 1.7 dB in bars 45-47, over the lead's 1 dB limit; simulated
with +1.5: -1.4 / -0.9 dB). Harp bell 200 Hz -4 dB (1.2 oct). Share of 140-355 Hz in the master:

| | c52 | simulated, bell removed | simulated, +1.5 | c53 | C's range | Brahms 1/ii, 4/ii |
|---|---|---|---|---|---|---|
| bars 23-30 | -4.70 | -5.89 | -5.31 | -5.66 | -5.9 | |
| bars 53-60 | -4.76 | -5.39 | -5.11 | -5.07 | -5.3 | |
| bars 71-78 | -4.68 | -5.89 | -5.75 | -5.85 | -5.8 | |
| whole | -5.36 | -5.85 | -5.66 | -5.67 | | -9.0, -8.5 |

Celli check on the render: the stem against all other stems in its fundamental band, bars 22-27 +8.55 -> +6.45 dB
(-2.1: -1.4 from the EQ, the rest from the transition notches at 68.5 and 77), bars 45-47 -2.88 -> -3.69 dB (-0.8).
Third octaves bars 23-30 relative to the total: 158 Hz -9.0 -> -10.2, 198 Hz -9.9 -> -11.9 dB; bars 71-78 198 Hz
-7.9 -> -11.0 dB.

**C3 test (not kept)**: Violas div on the section's KS Master (Close + Main), range A, second pass after the rebuild
(`divtest.txt`): correlation 1.00 -> 0.51, side/mid -126.5 -> -4.9 dB (Violas section 0.26, -2.3). Level +4.7 dB
median, but its note bodies spread over 11.1 dB against the DIV B patch (70: +12.3, 78: +9.0, 72: +1.1): after one
trim 6 of 11 notes within 1 dB. Joins by S 69: +138 -> +29, 71: +28 -> +35, 72: +1 -> +19, 87: +34 -> +66 ms. The
lead's condition (levels within 1 dB after a trim) fails, so the track was rebuilt on DIV B; Violins II div not tried.
The test variant builds with `MVT2_C53_DIVTEST=1` (`cycles/c53/divtest/`).

## 5. Render, state, checks
- Master -22.9 LUFS, LRA 23.4, true peak -4.7 dBFS, sample peak 0.581 (c52 -22.9, 23.4, -4.6, 0.585). Delivered
  -19.8 LUFS, LRA 14.8, TP -1.6 dBTP, limiter about 1.2 dB, p10-to-max span 18.3 dB, 347.40 s (c52 -19.7, 14.7, -1.6,
  1.2, 18.2). Attack probe: late or hole 0.
- Wetness t20 (`check52.py`): strings 0.434 s, winds 0.284, brass 0.272; final chord 0.46 s (t10 0.28); as c52.
- S1 (`s1check44.py`): own-band median 8.0 dB, under 3 dB 4 of 49 (as c52). S2: the S table above. S3
  (`check46.py`): steepest 10 ms fall of the master at the caesuras at most 0.6 dB; master dip at 204 3.4 -> 3.9 dB
  (limit 4; 4.5 before the stem fix), at 196 4.4 -> 4.1.
- state_guard: 0 stale of 32 before the work, after the `--mix-only`, after the `--midi-only`, before the restart,
  inside `render_cycle.py`, on the post-render save and on the project saved by quit. state_check against c52 and
  c51: no state run, no timing run.
- REAPER: 39 GB / 0 compressed before the render (no `--force-memory`), **40 GB / 21 GB compressed after**. Audio
  device at every reading: CoreAudio, Mac Studio Speakers, 48000 Hz, 512, no input; no setting changed.
- Builds: `--mix-only` on the six string tracks and the Harp (c52's stem-fix rows with the c53 rows, EQ), `--midi-only`
  on 16 tracks, Violins I once more (262), Violas div rebuilt twice (test and back), Trombone 1 rebuilt in full.
- Lock: waited 18:00:50-18:47:03 (46 min; the two waiters ahead were gone when the scherzo released). Held
  18:47:03-19:42:57 = **56 min**, no idle time. REAPER was quit and the lock released straight after the post-render
  save and guard; the analysis and the stem fix ran without the lock.
- Disk: 92 GB free before the render, 85 GB at the end. Range-pass audio deleted (286 MB), measurements kept.

## 6. Not done / open
- **REAPER does not hold the stem-fix rows** on Violins I, Violins II, Violas, Violoncellos (the envelopes of
  `build_fix/` = `build/`): the next actor writes them first (`--mix-only` or `--midi-only` on these four tracks), then
  saves and runs the state guard. A second lock for this was requested at 19:55 and given up at 20:54 (Movement I
  held REAPER from 19:42, the finale was waiting ahead); `actor_scripts/s4_53.sh` is the prepared session.
- Start sag against c51 left on Violins I 80, Violins II 146 / 154, Violoncellos 253 (a lift there moves S late);
  Violoncellos 68 reads -65 ms and 77 -49 ms by pcX after the fill / notch change (crossover -8 / -2 ms).
- Violins II bars 22-27 still move between passes (72 / 74 / 75 by 26-30 ms range pass to render; 86.5 +61 ms):
  `RR_RESET_AT["Violins II"] = [58.0]` trial for c54.
- Horn 1 breath 8.9 dB by the old check (9); Horn 2 208 re-attack not earlier; C5 master step 4.8 dB (4.5).
- 140-355 Hz share in bars 53-60 -5.07 dB (C -5.3): the bell stays at +1.5 dB by the lead's celli rule.
- C3: the section patch gives the divisi track width, but needs its own per-note level fit (and re-bow fills) before
  it can replace DIV B.
- `loop/MANUAL-GAPS.md`: no new gap tried beyond the C3 test (recorded under item 8).
