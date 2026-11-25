# Cycle 24 changes (actor)

Snapshot of the c23 tools and data: `cycles/c24/before/`. Every Opus state changed (rows unloaded), so all 32 tracks were fully rebuilt (`build_reaper.py build/parts.json jobs`, tempo map included), in a session opened fresh with `-new` + `Main_openProject`. Then save, quit, `-new` restart, open, and one render once memory had settled.

## Memory (BRIEF rule 7)

| | REAPER memory | compressed |
|---|---|---|
| c23 states, fresh open, settled (06:05, before the rebuild) | 61 GB | 0 GB |
| c24 states, fresh open, settled (06:17) | 43 GB | 0 GB |
| c24 render, peak during the render (15 s samples) | 44 GB | 0 GB |
| c24 after the render | 44 GB | 0 GB |

The c21-c23 "20-21 GB at the start" figures were taken before the samples had finished streaming in; the settled footprint of the c23 project was 61 GB. Unloading the unused rows took 18 GB (30%) off it. The render now ends at 44 GB with nothing compressed (c23: 63 GB, 44 GB compressed). The render took about 6 minutes.

## Accepted

### Critic A
- **A #4 unload unused articulation rows** (`tools/build_reaper.py` `load_articulations`, `UNLOAD_UNUSED_ROWS = True`): every KS Master row the track does not play (art_counts + first_art) gets `loaded`/`active` False. Only when at least one wanted row exists, so the single-row harp patches are unchanged. Checked in the written states (`jobs/21_*.b64`: Vln I loads Leg Slur MAX, Tremolo, Leg BC MAX, Leg Port MAX only; Flute 1 Sus MAX and Leg Slur MAX). It changed no sound: every stem with no data change before qn 151.5 (where the tempo map is unchanged) is bit-identical to c23: Flute 1/2, Oboe 2, CA, Cl1/2, Bn2, Cbn, Horns 2-4, all low brass, Timpani, Harp, Harp harmonics, Violas, Double basses, solo violin, Vc div, Vln II div, Horns a2.
- **A #3 render reproducibility** (`tools/build_reaper.py`, `RR_RESET_QN` 0.1, `REP_OFF_FAMILIES`): in the pre-roll every non-harp track gets CC36 = 127 (Round Robin Reset, HO manual CC table; every patch's controllerMap has `controller_36` "Repetition: Reset RR"), and the string tracks get CC69 = 0 (Repetition script off; `controller_69` "Repetition"). Effects measured: Bass clarinet and Bassoon 1 now play other round-robin samples than c23 (same level within 0.35 dB p95 over 0.5 qn bins), as the reset predicts. Whether the strings are now reproducible can only be shown by the c25 render: `det3.py "Violins I" 24 25`. Vln I still differs from c23 in qn 71.84-74.66 with no data change there (levels within 0.8 dB), but c23 had no reset, so this comparison cannot separate the causes.
- **A #1 `JOIN_NOTCH`**: Violins I (86.38, 86.51, -5.5), (258.85, 258.93, -5.5); Violins II (86.40, 86.50, -4.0), (258.81, 258.98, -4.0); Flute 1 (new key) (258.86, 258.93, -2.0), (266.00, 266.25, -5.0).
- **A #2 `build/leg_leads.json`** Horn 1: 18 0.06, 26 0.08, 27 0.05, 30 0.06, 39 0.08, 199 0.08.

### Critic B
- **B #1** `roles.json` Horn 1 `[179.25, 180.75, -6.5]`.
- **B #2** `HP_SOFT_ACC_SKIP = [298.0, 283.0]`; Clarinet 1 `[284.25, 285.75, 3]` (B asked 4; reduced by 1 because C #4 adds `[283, 292, 1.5, 1]` on the same notes).
- **B #3** `note_trims.json` Harp harmonics 276 +5; the plucked-step note-trim rule now covers the "harm" family too (`score_to_parts.py`; it covered only "harp").
- **B #4** `JOIN_NOTCH` Violoncellos (274.70, 275.30, -3.0).
- **B #5** `NOTE_TRIM_RAMP_S = {"Oboe 1": {42.0: 0.1, 54.0: 0.1}}` (new): the note trim reaches full value 0.1 s after the score onset instead of 0.6 s.

### Critic C
- **C #1** Horn 1 `[20.5, 23.5, -2.5, 1.0]`; `SWELL_SOFT_GAIN_AT` 68 removed (Vln I/II keep 240); note trims Vln I/II 83 +2.5, 84 +1.
- **C #2** Oboe 1 `[140, 143, -2, 0.5]`, `[148, 151, 3.5, 2]`; Violoncellos `[148, 151, 3, 2]`; `MERGE_NOTCH_AT = {"Violoncellos": {148.0: 3}}` (new: per-onset depth of the merged-repeat bow-change notch; it was 14 CC at the mf arrival; CC11 now 71 -> 69 at 148.0).
- **C #3** `tools/motion.py` (new) and `render_cycle.py` print the 4 s short-term change p90 and the 1 s vs 20 s motion for the master and the mp3 into `metrics.md`. Method checked against critic C's `motion2.py` on c23: 5.79/3.77 (master) and 5.00/2.84 (mp3), the same as C's figures. The loop rule (lower the covering voice first; a lowered crest stays 3 dB over its own phrase's earlier swells) is recorded in HISTORY.
- **C #4** `[283, 291.5, -2, 0.5]` on Horn 3, Horn 4, Violas, Violas div, Violoncellos, Double basses; Clarinet 1 `[283, 292, 1.5, 1]`.
- **C #5** `PHRASE_ARCS` + `(152, 160, "sub")`, `(160, 168)`.

## Rejected or deferred
- A #4 second step (drop `PORT_TARGETS`): not needed, the render ended at 44 GB. It is the next cut if a later cycle adds tracks or rows.
- B #6 (merge small tracks): not needed this cycle for the same reason. B's table of each small track's cost is the reference if it becomes necessary.
- A: the Vln I 72/74/240 spikes stay on hold until c25 shows whether the strings now render the same twice.
- C #4 second part (cap the Cl1 283 taper at 4 CC): not done; B #2's role offsets the taper in the volume envelope instead.
- `auto_fills.py 23` (routine): its only proposal was Violoncellos 199 1.9 -> 0.9, inside a span that decorrelates between renders (critic A #3); not written.

## Measured (c23 -> c24)
- Master: -22.5 -> -22.5 LUFS, LRA 23.7 -> 23.7 LU, TP -4.0 -> -3.9 dBFS.
- mp3: -19.8 -> -19.8 LUFS, LRA 16.0 -> 16.0 LU, TP -1.6 -> -1.6 dBTP, span 18.5 -> 18.4 dB, limiter 1.7 -> 1.9 dB.
- Motion (`motion.py`): master dS4 p90 5.79 -> 5.80, 1 s/20 s 3.77 -> 3.78; mp3 5.00 -> 5.12, 2.84 -> 2.86 (no fall).
- Attack probe: 3 of 21 flagged. Vln II/Vc 212 as in c20-c23. Vln I 171 reads +0.34 s (c23 +0.12), but its audio is identical to c23 at 10 ms resolution (the pre-onset floor moved 0.2 dB, which moved the threshold crossing to a later frame): threshold noise, not lateness.
- A #1 (`pk23.py`, master peak over its reference): 86.5 +6.0 -> +2.1; 259 +5.0 -> +1.8; Fl1 266 +3.9 -> +3.1 (stem +8.0 -> +5.5). Stems: Vln I 86.5 +7.4 -> +1.9, 259 +7.7 -> +3.9; Vln II 86.5 +5.9 -> +2.8, 259 +5.8 -> +2.0.
- A #2 (`leg.py` crossover / `rise.py` rise-6, s): 18 +0.14/+0.13 -> +0.02/+0.06; 26 +0.18/+0.16 -> +0.10/+0.09; 27 +0.05/+0.15 -> +0.05/+0.14; 30 +0.14/+0.14 -> +0.08/+0.07; 39 +0.19/+0.12 -> +0.10/+0.06; 199 +0.20/+0.27 -> +0.06/-0.00. No Horn 1 entry in `spikescan.py 5`.
- Spike scan: 35 -> 33 joins. Gone: Vln I 74, 86.5, 259; Vln II 86.5. New: Vln I 86.0 (its audio is unchanged; the 86.5 notch lowered the reference body after it) and Vln I 252.
- B #1 (Horn 1 minus Vln I + II, plain power per 0.5 qn, 179.0-180.5): -0.6/+4.4/+6.1/+6.7 -> -5.3/-2.1/-0.4/+1.1.
- B #2 + C #4: Vc qn 283 -> 285.5 rise +8.5 -> +6.4 dB; Cl1 minus Vc + Vla + Cb + Vla div at 284.5-285.5: -1.7/-6.1/-12.3 -> +6.3/+2.2/-4.1; Cl1 minus all other stems at 286-291 (0.5 qn bins): median -3.7 -> -0.5 dB.
- B #3: Harp harmonics E flat 6 at qn 276 +5.1 dB. B #4: Vc 274.75-275 -3.0 dB.
- B #5 (Oboe 1 minus Vln II at qn 54.0 / 54.25): -4.7/-6.3 -> -0.9/-4.5; at 42.0: +1.8 -> +6.5.
- C #1 (plain power per beat): Horn bar 12 crest over the bar 8 swell +0.9 -> +3.4 dB; Vln I bar 28 crest over the bar 24 swell +0.8 -> +2.9, fall after the crest 5.9 -> 4.6 dB.
- C #2: Oboe 1 qn 148 over bar 45 -1.0 -> +4.5 dB; master 148 over bar 45 +1.7 -> +4.9 dB.
- C #5: beats in bars 48-51 now 54.0 x5, 51.8, 52.9, 51.3 | 52.4, 54.8, 52.6, 54.8, 54.0, 54.0, 51.8, 49.7 (were 18 of 20 at 54.0).
- REAPER memory: see the table above. After the render REAPER was saved and quit.
