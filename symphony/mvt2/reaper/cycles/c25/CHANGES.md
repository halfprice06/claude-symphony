# Cycle 25 changes (actor)

Snapshot of the c24 tools and data: `cycles/c25/before/`. No Opus state changed, so this was a `--midi-only` update of 9 tracks (Oboe 1, Clarinet 1, Clarinet 2, Bass clarinet, Horn 1, Timpani, Violoncellos, Horns 1-2 a2, Double basses) in a session opened fresh (`-new` + `Main_openProject`). The tempo map is unchanged. One render, once memory had settled; no post-render fixes. Afterwards REAPER was saved and quit.

## Memory (BRIEF rule 7)

| | REAPER memory | compressed |
|---|---|---|
| fresh open, settled (about 07:11, 15 s samples) | 44 GB | 0 GB |
| render, peak | 44 GB | 0 GB |
| after the render | 44 GB | 0 GB |

## Accepted

### Critic A
- **A #1 coda clarinet** (`build/roles.json` Clarinet 1): [280,292,3] -> [280,297,3,2], [286,292,2.5] -> [286,297,2.5,2], [283,292,1.5,1] -> [283,297,1.5,2]; Clarinet 2 [286,292,-2] -> [286,295,-2]. `note_trims.json` Clarinet 1 292 +3, `NOTE_TRIM_RAMP_S` Clarinet 1 292.0: 3.0 s.
- **A #2 bass clarinet bar 32** (`tools/score_to_parts.py` `JOIN_NOTCH`, new key): Bass clarinet (93.03, 93.33, -4.5), (93.39, 93.85, +4.0), (93.89, 94.15, +1.5).
- **A #3 old negative trims**: `note_trims.json` Oboe 1 190 -8 -> -4, Clarinet 1 256 -5 -> -2, Violoncellos 180 -7 -> -2. `NOTE_TRIM_RAMP_S` Oboe 1 45.0: 2.1, 190.0: 0.1; Clarinet 1 256.0: 0.1; Violoncellos 180.0: 1.8.

### Critic B
- **B #1** `note_trims.json` Violoncellos 204 -3, 265 -4 (hot f/ff A flat 3).
- **B #2** `roles.json` Timpani [3,8.5,4], [226,237.5,3], [292,304,4] (ppp rolls).
- **B #3** `note_trims.json` Horns 1-2 a2 261 -3, `NOTE_TRIM_RAMP_S` Horns 1-2 a2 261.0: 0.1. B wrote the key as the moved onset 260.892; the lookup compares the score onset (`n["qn"]` before the move, see `new_on`), so the key is 261.0. Checked in parts.json: vol_db at 261.75 +4.2 -> +1.2, the f arrival at 262 unchanged (+6.0).
- **B #4** `note_trims.json` Bass clarinet 108 -3.

### Critic C
- **C #1 double-bass low end** (`build/mix.json` Double basses, ReaEQ only): static bell 80 Hz -6 dB 1 oct as a new `"bell2"` band (ReaEQ band 2, type 8; `config_eq` in `tools/build_reaper.py` now maps `bell2` to band 2, C's cleaner alternative to a third `loud_eq`); the 160 Hz bell +3 -> +4.5; the bars 37-44 pizz `loud_eq` (90 Hz shelf -5) removed; the climax `loud_eq` low shelf 100 Hz -6 -> -3 (its points and 150 Hz +4 bell kept). Applied by `--midi-only` (ReaEQ readback: bell 160 4.5, bell2 80 -6.0 bw 0.99, loud shelf 99.9 Hz -3.0).

### Routine
- `auto_fills.py 24 cycles/c25/before/parts.json --write`, excluding the hand-set and flip-flop entries (Fl1 200, CA 132, Ob1 145, Cl1 178/266, Hn1 202, Vc 203/210/256): Oboe 1 143 3.2 -> 3.3; Horn 1 26 new {3.5, 0, 0.22} (dip 6.5 dB at +0.17 s).

## Rejected or deferred
- None of the findings rejected. A's optional Cl2 [286,295,-2] taken.
- A's "not findings" (Vln I bars 53-56 leads, Hn1 bar 54.5 dip, Cb pizz. 116/120, Fl1 bars 76-77) and B #5 (Ob1 54 speech, bar 61 single bursts, harp in 71-78): no change, as the critics advised.
- C's residuals: Cb F2 still +3.9 dB (bar 57.1); the next step is a Cb `pitch_trims.json` pitch 41 -2 `_all_arts`, if bar 57.1 still reads over -9.

## Measured (c24 -> c25)
- Master: -22.5 -> -22.6 LUFS, LRA 23.7 -> 23.6 LU, TP -3.9 -> -4.2 dBFS, sample peak 0.636 -> 0.616.
- mp3: -19.8 -> -19.8 LUFS, LRA 16.0 -> 16.0 LU, TP -1.6 -> -1.6 dBTP, span 18.4 -> 18.5 dB, limiter 1.9 -> 1.6 dB.
- Motion: master dS4 p90 5.80 -> 5.71, 1 s/20 s 3.78 -> 3.80; mp3 5.12 -> 5.06, 2.86 -> 2.87 (falls under 0.2 dB).
- Attack probe: 3 of 21, the same three as c24 (Vln I 171 +0.34 s, Vln II/Vc 212 holes 6.9/6.2 dB).
- A #1 (plain RMS, 292-293.5 / 293.5-295 / 295-296): Cl1 -50.1/-54.5/-55.6 -> -43.9/-44.8/-46.7; Cl2 -50.0/-48.5/-50.0 -> -51.8/-50.5/-50.7; Vln I -48.1/-47.5/-48.0 (unchanged). Cl1 is now 4.2/2.7 dB over Vln I and 7.9/5.7 over Cl2, and falls 0.9 dB from 292-293.5 to 293.5-295. That is about 2 dB hotter than A's simulation (-46..-47) and 1.7 dB over Cl1's own bar 88 (-45.6). Master bar 89 +1.0 dB. If critics judge the resolution note too prominent, the 292 trim +3 -> +1 brings it to the simulation.
- A #2 (40 ms, stem/master): 93.1-93.3 -32.2..-33.4 / -31.8..-32.5 -> -37.1..-38.5 / -35.8..-36.3; trough 93.5-93.8 -41.6..-43.2 / -38.3..-39.7 -> -37.6..-39.4 / -36.4..-37.7. The stem now lies in -36.1..-39.7 from 93.0 to 94.5 (was -32.2..-43.2); master attack-to-trough 7.9 -> 2.4 dB.
- A #3 (stem RMS in 0-0.3/0.3-0.6/0.6-0.9/0.9-1.3/1.3-1.8/1.8-2.4 s after the onset):
  - Ob1 45: -37.8/-40.0/-42.8/-42.1/-42.9/-43.0 -> -37.2/-36.6/-38.0/-38.4/-40.8/-42.6 (falls 4.6 dB from 0.6-0.9 to 1.8-2.4 s).
  - Ob1 190: -42.2/-42.6/-46.7/-45.3 -> -43.6/-40.8/-42.7/-41.3 (hole gone).
  - Cl1 256: -38.9/-42.9/-42.8/-38.6 -> -41.1/-41.7/-39.8/-37.8.
  - Vc 180: -38.4/-39.5/-43.4/-43.4/-42.7 -> -36.9/-34.7/-37.1/-37.5/-37.4.
- B #1 (plain RMS): Vc 204.1-205.9 -23.7 -> -26.3 (Vln I -27.5); 265.1-266.9 -24.7 -> -28.3 (Vln I -29.4). B's targets were K-weighted (Vc 1.8/2.5 under Vln I); the plain-RMS changes (-2.6/-3.6) match the trims.
- B #2 (timpani stem RMS): 3-6 -57.3 -> -53.3; 6-8.5 -60.1 -> -56.1; 226-231 -55.8 -> -53.1; 231-237 -58.1 -> -55.1; 292-297 -60.3 -> -56.3; 297-303 -63.8 -> -59.8.
- B #3 (Horns a2 per 0.25 qn, 261.0/261.25/261.5/261.75/262.0): -40.0/-37.5/-32.0/-27.7/-28.6 -> -42.4/-40.5/-35.0/-29.3/-28.6. The peak at 261.75 fell 1.6 dB (B predicted 3) and is now 0.7 dB under the f arrival (was 0.9 over).
- B #4 (Flute 1 minus bass clarinet, plain RMS at 108.5/109/109.5): +0.1/+1.2/-0.3 -> +3.0/+4.2/+2.7.
- C #1 (critic C's scripts on the c25 master; every figure within 0.3 dB of C's simulation):
  - `lowdist.py` loud third median -17.0 -> -20.4, p90 -9.0 -> -13.3; soft median -22.9 -> -25.3.
  - `lowpow.py` loud 60-100 -15.4 -> -17.7, top 10% -15.8 -> -17.8; loud 100-250 -6.3 -> -6.9 (C's check asked -6.6 or higher: missed by 0.3).
  - `barcmp.py` master 60-100 re 250-2k: bars 23-29 -11.9 -> -16.9, 37-44 -14.0 -> -15.3, 53-59 -10.9 -> -13.7, 60-62 -17.1 -> -19.2, 65-66 -9.7 -> -15.2, 75-81 -15.8 -> -18.0, 84-92 -17.1 -> -21.7.
  - `cbpitch.py` f0 re h2-4: Db2 -0.1 -> -5.1, Eb2 -5.1 -> -11.0, B1 +3.9 -> +0.8, F2 +9.5 -> +3.9, D2 +8.6 -> +3.2.
  - `cbh.py` Cb 120-400 Hz +0.3..+0.5 dB in every passage.
  - LTAS 63 Hz (metrics.md) +0.3 -> -2.3 re 1 kHz (Dvorak -6.2). Master corr 25-60/60-120 0.72/0.76 -> 0.71/0.76.
- Reproducibility (critic A `det3.py`, c24 vs c25, same tempo map, 50 ms frames, fraction of active frames decorrelated): Violins I 0.04, Violins II 0.02, Violas 0.01, Violin I solo 0.00, Oboe 2 0.00, Horn 2 0.00; Flute 1 0.12 (bar 63), Bassoon 1 0.20 (bars 8-15) with no data change on either. The c24 pre-roll CC36/CC69 made the strings render nearly the same twice; Flute 1 and Bassoon 1 still vary.
- REAPER memory: see the table above. After the render REAPER was saved and quit.
