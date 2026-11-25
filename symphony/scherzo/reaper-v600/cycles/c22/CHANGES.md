# Cycle 22: changes (actor, on the c21 render)

STATUS: **rendered once**, 2026-11-17 17:19-17:25 CST, from a freshly restarted REAPER (state guard 0 before the render;
Horn 2 / Horn 4 stale after the save, rebuilt, saved, guard 0).
- mp3: `cycles/c22/scherzo-mockup-c22.mp3`. Data as rendered: `cycles/c22/build_render/` (= `build/`).
- Lock: queued 16:13 behind mvt3 (c24 actor), held 16:38-17:30 (52 min; `phase.log`): open, settle 43 GB, guard 0,
  control pass (10 ranges), build A, pass A, three Violins I variants (C, D, E), final `--midi-only` build of all 31
  tracks, restart, settle 44 GB, guard 0, audio_init, render, save, stale rebuild, save, guard 0, quit, unlock.
- REAPER memory: 44 GB settled before the render, 45 GB after it (0 GB compressed). 60 GB (42 GB compressed) during the
  range tests.
- Disk: 32-39 GB free during the cycle, 39 GB at the end. c21's 35 stems deleted (00_Master.wav and mp3 kept); my range
  WAVs deleted. Backups/ not touched.
- Probe: late or hole 0. Master -21.2 LUFS, LRA 22.4, TP -2.1 dBFS, sample peak 0.787 (no clipping).

## Dan's bar 23 figure (first check)

Range tests (bars 21-43 from qn 54 and bars 256-266 from qn 767; one start per range; control = the c21 state).
"Decay" = how far a note has decayed (dB from its peak) when the next note starts; "pair" = each pair note's peak
against its detached neighbours.

| variant | bar 23 pair / decay G, A, B | bar 38 pair / decay A->B | bar 263 pair / decay A->B |
|---|---|---|---|
| control (c21) | -8.5 / -12.8; F#->G 3.8, G->A 10.7, A->B 1.5 (median 2.7) | -6.9 / -13.1; 5.5 | -17.3 / -11.7; 4.1 |
| A: coordinator's lift +20 / +20 / +16 to q+0.7, loud pairs +8 | -3.4 / -6.9; 0.0, 10.6, **-4.2** (median 0.0) | -2.1 / -5.1; 5.3 | -1.1 / +2.3; 2.1 |
| C: soft pairs on "Sus Marc LITE" (theme-head treatment) | -3.7 / -1.0; 0.8, 8.5, -3.2 | -10.0 / -1.8; 2.4 | -0.2 / +2.4; -0.7 |
| D: lift ending at q+0.30 (just after the second note-on), from q-0.70 | -0.4 / -1.5; -3.1, 5.8, 3.6 | -3.6 / -9.4; 6.0 | -4.1 / -2.6; 5.3 |
| **E: as D, lift from q-0.55** | -2.4 / -0.8; **-2.9**, 1.4, 8.2 (median 0.9) | -3.9 / -8.5; **7.3** | +1.2 / +2.4; **5.3** |

- In A the second pair note, now on the mf groups (slow attack, 150 ms cap), was still rising when the landing note
  started; the loud pair at bar 42 went 5.2 -> 1.7. Rejected.
- In E the A->B decay improved at every occurrence. At bar 23 the lift raised the preceding staccato quarter's tail
  (F# -> G 3.8 -> -2.9 dB), so the figure median fell 2.7 -> 0.9. Following the rule (no occurrence worse than c21),
  **E is adopted on bars 38 and 263 only; bar 23 keeps the c21 state** (`C22_SKIP` "66").
- The loud-pair +8 was dropped (the A pass's bar 42 reading). An unchanged bar 42 pair read 5.2 / 2.0 / 5.2 dB across
  three passes: a row change moves the round-robin position of the later notes, so single-note readings scatter by 3-11 dB.
- Release-trail cap on "Sus MAX" (rt_ms): not tested (lock time went to the variants above). The finale's c23 #108
  found an 80 ms trail cap had no effect on celli.

Every occurrence on the full renders, c21 -> c22 (`records/fig23.txt`, decay before the next note-on / trough, dB):
bar 23 2.9 / 1.2 -> 2.9 / 1.2; **bar 38 6.5 / 7.2 -> 7.3 / 11.0**; **bar 263 5.1 / 4.3 -> 5.7 / 4.7**; the other 15
Violins I and 15 Violins II occurrences identical (unchanged data). Pair levels on the full render (`rt22.py pairs`):
bar 23 -13.5 / -13.2 (unchanged), bar 38 -7.0 / -13.2 -> -3.9 / -8.7, bar 263 -17.4 / -11.9 -> -7.9 / -5.8.
Nothing is worse than c21.

## Delivery, against the shared spec (2026-11-17) in its order

| | c21 mp3 | **c22 mp3 (adopted: peak comp -9 dB 3:1, top ride 6 dB under p95, lift 2.1, rides)** | c22 master, no peak comp (finale c24 advice, simulated) |
|---|---|---|---|
| 1. I / TP | -14.1 / -1.3 | **-14.0 LUFS / -1.4 dBTP** | -14.0 / -1.2 |
| 2. summit lead (M max per bar) | +0.44 over 318 | **+0.61 over bar 335** (the bar before it); +0.7 over every other rival (305-320 -8.1, 105-120 -8.3, 300 -8.4, 304 -8.6, 72 -8.7, 53 -8.9, trio -9.5) | +0.39 over 318 (fails) |
| 3. f -> ff (passage means) | 1.71 | **2.24 LU** | 2.66 |
| 4. p10 short-term | -21.5 | **-20.2** | -21.5 |
| 5. limiter (summit / 105-120 / 305-320 / 72 / 300 / final) | 5.7 / 3.4 / 2.9 / 3.8 / 1.9 / 0.1 | **2.7 / 2.2 / 2.1 / 1.0 / 0.8 / 0.1** | 9.7 at the summit (fails) |
| 6. LRA | 12.1 | **10.6** (accepted: it buys items 2 and 3) | 12.3 |

- Without the peak compressor the summit takes 9.7 dB of limiting and loses its lead, so it stays.
- Quiet passages on the mp3 (energy mean of M), c21 -> c22: intro -18.3 -> -17.0, theme A -17.7 -> -16.2, counterstatement -21.5 -> **-18.5**, fugato -22.3 -> -21.0, trio dolce -17.3 -> -16.0, stretto -28.8 -> -28.1, Meno pp -20.0 -> -19.2.
- Crescendo arrivals on the mp3 (rise over the bar before): 41 +0.6 (c21 +1.2), 72 +0.5, 105 -0.4, 129 +0.2, 197 +1.0, 209 +0.9, 285 +0.5, 300 +1.4, 304 +0.2, 305 -0.4, 329 +2.1, 336 +0.5.
  - No new inversion. 105 / 305 read -0.4 as in c21: the tutti's first bar against the crescendo bar.
  - 41 is smaller: the counterstatement lift (+2 dB) returns to 0 across the crescendo, and the clarinets' role row covers bars 37-43.
- Hall (`hall17.py`; G.P. drop at +0.3 s, 20 dB fall, RT60):
  - master: 18.0 dB, 0.37 s, 1.40 s (c21 18.4 / 0.33 / 1.38);
  - mp3: 18.9 dB, 0.33 s, 1.38 s (c21 19.5 / 0.32 / 1.28).
  - Inside Dan's limit on both (fall 0.50 s or less, RT60 1.5 s or less, drop 15 dB or more).
- Simulated first on the c21 master: limiter 3.0, LRA 10.6, p10 -20.3 (critic C's numbers).

## Changes made

### Tools (generic, off by default)
- `tools/score_to_parts.py` `HP_TARGET_LOOKAHEAD_QN` (critic C #3):
  - An untargeted crescendo takes the next louder printed mark of its own staves as its target. The mark must lie more than 1 qn and at most this many qn after the hairpin's stop, with no other mark or hairpin start between, and the gap must be at most half the hairpin's length.
  - Printed in the build log (`HP_TARGET_LOOKAHEAD`).
  - Scherzo 2.5 qn. It hits Flute 1 300-310 -> ff 312 and 900-910 -> ff 912.
  - Without the half-length condition it also hit the basses' 0.5 qn hairpin at 210 (ff reached 2.5 qn early) and celli / basses 291-292 (mp at 294).
- `tools/deliver_master.py` (scherzo values):
  - `TOP_ABOVE` -6 (was -10), quiet lift `RATIO` 2.1 (was 1.6);
  - `PEAK_COMP` -9 dB 3:1 (was -6 dB 2:1);
  - `DELIVER_RATIO` override kept.

### `build/score_config.py` (c22 block at the end; switches C22_PAIRS, C22_SKIP, C22_LIFT_FROM, C22_WACC, C22_MARC, C22_V1LEAD, C22_LOOK)
1. Violins I soft pairs (A #1): `CC11_ADD_SPANS` (112.45, 113.30, +20), (786.45, 787.30, +16); bar 23 left out (above).
2. Crescendo look-ahead 2.5 qn (C #3).
3. Accents (A #3, B #4):
   - Flute 1 (35 accented Sus MAX notes) and Flute 2 (10) on "Sus Accent MAX": velocity 70 where CC11 is under 80, else 90; no CC11 bump on that row.
   - Oboe 1's four accents at velocity 96 / 96 / 96 / 105 (was 70 / 70 / 70 / 90; the row's layers are 1-74 / 75-114 / 115-127, read from the .oib).
4. Violas fugato entries (C #5): CC11 +8 over 179.6-182.9 and 875.6-878.9.
5. Delivery ride rows (C #1, C #4): bar 53 -1.5 (154-166), the trio's A6 -1.5 (645-659), counterstatement +1.5..+2 (83.5-116, back to 0 across the printed crescendo).
6. Tested and left off (switches): the coordinator's lift on all pairs (C22_PAIRS=1), "Sus Marc LITE" pairs (marc), Violins II / violas accents on "Sus Marc LITE" (C22_MARC=1), the 0.07 s first-eighth lead (C22_V1LEAD=1).

### `build/roles.json`, `build/mix.json` (`actor_scripts/apply22.py`, rerunnable from `before/`)
- Clarinet 1 [108, 129, -6], Clarinet 2 [108, 129, -4] (B #1; Clarinet 1 chains from its [102, 108, -4]).
- Violins II [985, 995.5, -7 -> -3]; Violas [984, 995.5, +3 -> +5] (B #2).
- Bass clarinet [624, 672, -4] deleted; Horn 4 [648, 669, +3] (B #3).
- The twelve summit cuts start at 1004.75 instead of 996, halved (C #2):
  - Violoncellos -3;
  - Clarinet 2 -2.5, Bassoon 1 -2.35;
  - Flute 1 / Flute 2 / Oboe 2 -2;
  - cor anglais / Contrabassoon / Horn 1 -1.5;
  - Clarinet 1 -1, Bassoon 2 -0.75, Oboe 1 -0.5.
- Clarinet 1 [906, 912, -5] -> [900.5, 912, -5] (C #3).
- mix.json (C #6):
  - cor anglais `dyn_trim_db` f 0 -> +1.5, `soft_trim_db` mf 2.5 -> 1.5;
  - Horn 2 f -1.0 -> 0, mf 2.4 -> 1.4.
- Opus state changes: Flute 1 and Flute 2 load "Sus Accent MAX" (full rebuild). The final build wrote all 31 tracks.

## Measured (c21 -> c22 full renders; `records/`)

- **Inner lines** (item 2; `inner20.py` best band per 3 qn, line against all other stems and returns, dB):

  | line | c21 | c22 |
  |---|---|---|
  | Clarinets 1-2 bars 37-43 (the chord that covered the tune) | +9.2 +16.7 +15.5 +7.5 +20.8 +12.5 +12.0 | +4.4 +13.7 +10.5 +2.4 +16.6 +8.2 +6.8 |
  | Flute 1 + Oboe 1 (the tune) bars 37-43 | +2.6 +4.0 -5.0 -1.5 +6.6 -4.9 -4.1 | +2.8 +4.2 -4.4 +0.3 +6.7 -4.5 -1.8 |
  | Violins II bars 329-332 | -10.1 -6.7 -5.0 -9.1 | -7.5 -2.8 -1.9 -5.6 |
  | Violas bars 329-332 | -0.5 -9.7 -12.3 -6.9 | +0.6 -8.3 -10.3 -5.0 |
  | Bass clarinet bars 211-222 | -6.2 +8.6 -2.0 -2.6 -3.7 -6.8 +2.9 -1.2 -3.8 -4.7 | -2.5 +12.1 +2.0 +1.3 +0.2 -2.8 +6.0 +2.7 0.0 -0.7 |
  | Horn 4 bars 217-223 | -6.8 -7.8 -0.4 -5.7 -5.6 -8.8 -9.7 | -4.0 -5.1 +1.9 -2.7 -2.7 -5.8 -6.7 |

  Every line gained 2-4 dB; the clarinets' chord is still over the tune in bars 38-39 and 41 (the tune's best band
  -4.4 / +0.3 in 39-40). Horn 4 is still under its neighbours in 222-223 (Bassoon 2 -8.8 there): the finale's CC1 +12
  for a soft upper horn voice is a candidate for c23.
- **Coda ff to fff** (item 3, stems, dB):
  - celli 993-995.4 / 996-998.4 / 1005-1010: -31.2 / -38.4 / -31.6 -> -31.2 / **-32.4** / **-28.6** (fff over ff: yes);
  - Clarinet 1 996-998.4 -34.3 -> -32.3; Bassoon 1 -37.9 -> -33.2; Oboe 1 fff -33.2 -> -32.7.
  - Master 996-1002 -19.4 -> -17.6, summit 1005-1011 -15.9 -> -15.2: the summit leads the ff by 2.4 dB (was 3.5; C's target 3) and bar 104 by 3.8.
  - mp3 summit M max -7.1 -> -7.5 (bars 333-335 +1.6..+2.0 dB on the master).
- **Flute 1 crescendos** (item 4, quarter levels): 900-911 was -32.4 ... -44.1 ... -38.6, then -29.1 at 912; now -32.2 ... -31.8 ... -35.1, then -26.2.
  - The line no longer falls 12 dB through the crescendo, but it does not rise either, and the step at the ff is still 8.9 dB.
  - 300-312: 305 -42.5 -> -39.8, 309 -38.0 -> -34.4, step at 312 10.4 dB.
  - Clarinet 1 901-905 is 5 dB lower (the row from 900.5), then flat at -35.
- **Accents, first 100 ms against the neighbours** (median; p90; accents over +3), c21 -> c22:

  | track | c21 median | c22 median | p90 | over +3 | peak after the beat |
  |---|---|---|---|---|---|
  | Flute 1 | -2.2 | **+1.4** | +6.7 | 12 of 36 | 0.22 -> 0.07 s |
  | Flute 2 | -1.4 | **+0.4** | +8.1 | 3 of 10 | 0.30 -> 0.06 s |
  | Oboe 1 | -2.1 | -1.8 | +3.9 | 6 of 28 | 0.27 |
  | cor anglais | -1.2 | -1.6 | +2.4 | 3 | 0.21 |
  | Clarinet 2 | -0.4 | -0.4 | +1.8 | 2 | 0.31 |
  | Violins I | -0.4 | -0.7 | +4.6 | 10 | 0.14 |
  | Violins II | -2.7 | -2.7 | +4.6 | 9 | 0.26 |
  | violas | -0.6 | -0.6 | +4.0 | 6 | 0.14 |
  | celli | +0.1 | +0.1 | +5.8 | 6 | 0.04 |

  No track median over +3. The flutes' accented notes in the range test: 87-123 -4.0 -> +3.2 (p), 891-910 -2.2 -> +0.4.
  The Oboe 1 range test (87-123): -2.4 -> +0.2. The string accent fronts (A #2) are unchanged: their fix failed (below).
- **Per-bar master against c21** (`records/bars_c22_vs_c21.txt`): median 0.0.
  - Over +1.5: 58 +2.9 (celli round robins on unchanged data; c21 read 58 -2.8), 264 +1.8 (Flute 1's 789 accent on the new row), 333-335 +1.6 / +2.0 / +1.8 (summit cuts moved to 1004.75).
  - Under -1.5: 38 -2.0, 43 -1.8 (the clarinets' role row).
- **Envelope** (`slope17.py`): 4,824 -> 4,769 points, 0.84 -> 0.83 per note, 17.4 -> 17.2 per second; notes with over 3 dB strictly inside
  them and unprinted moves: not counted this cycle; the slope guard lists the same 9 notes as c21 (celli 312 / 912 / 362, Horn 2 1005,
  Horn 3 953 / 936, harp 708, Oboe 1 1005, violas 197), all printed hairpin or role edges from earlier cycles.
- **Timing** (`timing13.py`): 27 % of readings outside 25 ms, 5 % outside 60 ms (c21 27 / 6).
- **String staccato separation**: Violins I 4.0 dB median (counterstatement 0.7, unchanged), Violins II 6.6, violas 6.8, celli 3.9.
- Harp's loudest moments (finale c25 note): its biggest lead over every other stem is +13.7 dB at 55.8 s, at -41.8 dB in the F major episode where it plays alone with the winds. No hot ff chord.

## Rejected, deferred, not done
- The coordinator's lift on all seven pairs (blur into the landing note), "Sus Marc LITE" pairs, the lift at bar 23: numbers above.
- Violins II / violas accents on "Sus Marc LITE" (A #2): range test from the same starts.
  - Violins II's hemiola accents read -47 / +49 dB against their neighbours (300 / 302): the row's notes did not start like the Sus MAX ones.
  - The violas' 902-910 median went -0.8 -> -2.8.
  - The finale's c24 found the row negative on held chords too. Not adopted (A #2 stays open).
- 0.07 s first-eighth lead on Violins I (A #4): separation 4.5 -> 3.8 / 4.6 -> 5.1 dB, p10 0.4 -> 0.8 / 3.1 -> 0.9. No gain.
- Release-trail cap on Violins I "Sus MAX": not tested (lock time).
- Faults still audible (Dan's rule, no envelope fix):
  - bar 23's soft pair (13 dB under its neighbours);
  - the Flute 1 crescendos into 105 / 305 (flat, then a 9-10 dB step);
  - the summit only 2.4 dB over the coda ff on the master;
  - the string accent fronts;
  - Violins I's counterstatement eighths (0.7 dB separation);
  - the string legato swell.

## Research items

| item | status |
|---|---|
| EW template mix, returns, seats | adopted (unchanged) |
| no volume automation per note (Dan 2026-11-11) | adopted; 0 per-note rows; the c22 rows are role and section rows |
| accents by the KS Master's own accent rows | adopted on flutes and Oboe 1 ("Sus Accent MAX"); rejected on Violins II / violas ("Sus Marc LITE", range test) |
| shared -14 delivery (top ride 6 dB under p95, lift 2.1, peak comp -9 dB 3:1, ride rows) | adopted (spec items 1-6 met) |
| one legato row per string line, keyswitch 0.15 s ahead | adopted (unchanged) |
| per-region / per-row volume in the Opus state | adopted (unchanged) |
| CC16 resets everywhere, separate legato tracks, timpani hard sticks, recorded crescendo rolls | pending |
