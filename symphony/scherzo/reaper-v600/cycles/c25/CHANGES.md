# Cycle 25: changes (actor, on the c24 render)

STATUS: **rendered once**, 2026-11-18 04:06-04:14 CST, from a freshly restarted REAPER (guard 0 stale, memory settled
at 44 GB, 0 GB compressed). Attack probe: late or hole 0. No stem fix. The mp3 was delivered a second time from the same
master after a delivery-only change (ride trims, item 7), with no new REAPER render.
- mp3: `cycles/c25/scherzo-mockup-c25.mp3`. Data as rendered: `cycles/c25/build_render/`. Records: `cycles/c25/records/`.
- Lock (`phase.log`): taken 03:21 with no other waiter, released 04:17: **56 min**. In that time: control range renders,
  two variant builds with range renders, the final build of all 31 tracks, restart, render, save, rebuild of the stale
  tracks, save.
- REAPER memory: 44 GB settled before the render and **44 GB after it** (0 compressed). It reached 56 GB during the range
  passes (before the restart).
- After the save that followed the render, Bassoon 2, Contrabassoon and Horn 4 were stale. I rebuilt them and saved
  again; the guard reads 0 stale, also on the project saved at quit.
- Disk: c24's stems deleted (its 00_Master.wav and mp3 kept), my range WAVs deleted; 43 GB free at the end.
- Master -21.1 LUFS, LRA 22.1, sample peak 1.048 (TP +0.5 dBFS). render_cycle replaced the clipped master with the float
  stem sum, so the samples are not clipped; the mp3 has TP -1.3. All 36 files are present and sounding.

## Bar 23 figure (first check, every occurrence; `records/fig25.txt` pitch-resolved, `records/fig24_old.txt` old measure)

Pitch-resolved crossover (critic A's measure, `actor_scripts/fig25.py`): dB, c24 -> c25, Violins I.

| occurrence | F sharp -> G | G -> A | A -> B | B -> C |
|---|---|---|---|---|
| **bar 23** (qn 67) | 19.3 -> 18.0 | 4.3 -> 4.3 | 8.9 -> 8.9 | 9.0 -> 9.4 |
| bar 115 / 315 | 22.1 / 22.4 -> 22.1 / 22.5 | 4.6 / 4.7 (same) | 9.3 / 8.5 (same) | 9.5 / 9.4 (same) |
| bar 263 | 15.4 -> 18.7 | 4.3 | 3.9 | 20.9 |
| E -> B at bars 117 / 317 (qn 349 / 949) | 11.0 / 11.9 (same) | | | |

- Every other Violins I occurrence (38, 42, 70, 106, 110, 116, 118, 274, 298, 306, 310, 316, 318, 334) is within
  ±0.2 dB, except bar 38 79->74 13.6 -> 14.6 and bar 110 79->78 2.3 -> 4.5. The 15 Violins II occurrences are identical.
- Old measure (decay before the next note-on / at the trough / trough): bar 23 4.4 / 7.7 / 5.5 -> 4.5 / 7.3 / 5.2.
  The other occurrences are within 0.1 dB.
- Nothing is more than 2 dB under c24 (A's acceptance). The F sharp at qn 66 is a Spiccato note and lost 1.3 dB of
  crossover when it was lowered.
- The E -> B residual at bars 117 / 317 (c18 15.4 dB): cause not found. The data is identical to c18 and no c25 change
  touches it.

## Changes made

### Tools (generic, off by default)
- `tools/build_reaper.py`:
  - mix.json **`dyn_trim_to_cc7`** (critic B #1, finale technique 135). The dynamic trims leave the post-hall volume
    envelope and go into a CC7 lane inside Opus, with the 20·log10 law.
    - The trims are read on moved time: each mark and each hairpin start / end that falls on a led note's score onset
      moves to that note's moved note-on less `lead_s` (0.02 s), through a piecewise-linear warp (`dyn_warp`, `warp_fn`).
    - The envelope holds gain + vol_db + the largest trim. It is capped at `env_max_db` (23 dB), because the trombones
      would otherwise reach +28 dB and REAPER's envelope range ends at +24. The capped share of the softest trims stays
      in the envelope.
    - In rests the lane is held like the envelope's tail hold, and it ends on its last value.
    - Harp, harp harmonics and timpani stay in the envelope.
    - `item_lua` calls `vol_points` first so that `cc7_lane` can merge the trim lane.
  - mix.json per-track **`cc7_spans_db`** `[[q0, q1, dB, ramp_in_qn, ramp_out_qn]]`: passage levels before the hall,
    added to the same lane. A lift is cut at CC7 127, with a warning.
- `tools/score_to_parts.py`:
  - **`HP_START_MOVED`** (B #4a): a hairpin ramp that starts on a led note's score onset starts 0.02 s before the
    note's moved onset.
  - **`HP_HOLD_TO_NOTE_END`** (B #4d): when a note sounds across a hairpin gain's hold end, the hold runs to that note's
    end (at most N qn), but only when a rest follows, so that the release falls in the rest. A first version without the
    rest condition pushed releases into the next joined notes; note_move_guard then held them, and Bassoon 1's bar 221
    rose 4 dB. Fixed before the build.
  - **`ARRIVAL_WEIGHT_RISE_ONLY`** and **`ARRIVAL_WEIGHT_HOLD_CAP`** (B #3). parts.json `arrival_skipped`,
    `hp_start_moved`, `hp_held_end`.
  - `STAC_ROW_BY_PITCH` rows take an optional 4th value `vel_add` and 5th value `vel_below` (A #1b).

### Data (`build/score_config.py` c25 block; `actor_scripts/apply25.py [B]` writes roles.json and mix.json from `before/`)
1. **Violins I Spiccato level** (A #1, C #1; range tests P1 / P2).
   - The row's velocity layers are v1-54 / 55-89 / 90-114 / 115-127 (load_oib). A's "vel>=80" would have missed the 14
     rerouted notes at v81-87.
   - Adopted: the rerouted notes under velocity 90 lose 13 steps, so all of them play the 1-54 layer, which is cut
     2 dB (`row_dyn_db` "vel<55"). The v95 tutti notes are cut 4 dB (`row_dyn_db` "vel>=90"). No original Spiccato note
     plays in either cut layer.
2. **Dynamic trims in CC7** on moved time (B #1; coordinator item 2). Every track except the harp, harmonics and
   timpani.
3. **Summit** (B #3): weight only for tracks with a printed rise into 1005 (the horns, trumpets and trombones lose it),
   hold capped at qa + 1.5 qn, remaining tracks 2.5 -> 3.0 dB.
4. **Inner lines** (B #4 / #5, C #3).
   - Flute 1 [828, 840, -3.5] deleted; Flute 1 [1044, 1068] -9.5 -> -6.5.
   - CC7 -2 dB on the reprise's pp accompaniment: Clarinet 1, Horn 2, Horn 3 and violas, from each track's moved
     note-on at 828 to 840.
   - CC7 -2 dB under the codetta oboe (Violins II, violas, Clarinet 2, 671-684).
   - CC7 lifts on the violas' div. thirds, 636.5-672: violas +2, Violas div +2.5. At 5 / 6 points the lift reached
     CC7 127 and was cut there.
5. **Role edges into CC7 or rests** (B #4b).
   - Oboe 1 [386.8, 393, -4.5] / [854.8, 861, -4.5] became CC7 spans ramping 386.3-386.8 / 854.3-854.8, so the printed
     crescendo rises from the lower level. The guard had held these levels and reversed the crescendo by 6 dB.
   - Clarinet 2 [828, 840, -3] became a CC7 span from 827.70.
   - Horn 1 [1020, 1068, -2.5] -> [1020, 1060, -2.5], so the 1068 row starts unchained and ROLE_EDGE_MOVED ends it on
     the moved note-on.
   - The trombones' softer pp head at 993 (B's do-not-touch): CC7 -3 dB (Trombone 1) and -4 dB (Tuba) over 992.69-993.3,
     back to 0 by 994.5.
6. **Timing** (A #3, A #5).
   - `leg_leads.json` celli +0.08 s at 510, 512, 516, 522, 528, 542 and 570. 576 is set apart (total 0.15 s; it was
     0.03).
   - `entry_leads.json` cor anglais +0.05 s on its 29 accented onsets (900 keeps 0.06).
7. **Delivery**: RIDE_TRIMS fugato lifts (167.5-204, 863.5-888) +2 -> +1.5 dB. The first delivery read LRA 10.4,
   under spec item 6. The fix was tested on the c25 master; it needs no REAPER work.

Opus state changes: Violins I only (region gains). The final build wrote all 31 tracks with `--midi-only` (CC7 lanes and
envelopes everywhere; Violins I and the legato tracks rebuilt fully).

## Guard (`actor_scripts/guard25.py`: guard24 plus hairpin starts at the moved onset; `records/guard_*.txt`)

| measure | c24 as rendered | trims in CC7 only | c25 as rendered |
|---|---|---|---|
| step: 1.5 dB within 0.5 s at over 6 dB/s | 25 (+14 harp) | 12 | **9 (+14 harp)** |
| first 0.35 s: 1.5 dB or more | 64 (+6 harp) | 30 | **9 (+6 harp)** |
| critic B's 2 dB / 20 dB/s | 0 | 0 | **0** |

Remaining notes (18 entries, 13 notes), with their causes (`records/guard_layers.txt`):
- **Printed short hairpins on held notes**: Clarinet 2 210 / 894 (+3.2 dB over 0.4 s), Bassoon 1 1001, Horn 1 442,
  and Oboe 1 1002 (hairpin plus the summit's arrival weight). These are allowed hairpin ramps that end outside the exempt
  window.
- **Role edges with no rest within reach**:
  - Flute 1 156 / 384 and cor anglais 156: hairpin release at the arrival, followed by a joined note.
  - Positive role ends that CC7 cannot carry without headroom: celli 876 [864, 876, +5], Violins I 1012 [1008, 1014,
    +4.5], Horn 3 1028 [1020, 1032, +3].
- **The solo passage's small printed hairpins on joined notes**: Violin I solo / Violins II 1057 / 1064.
- **Horn 3 950**: 2.8 dB at +0.31 s, no layer named; not found.

Envelope table: c24 4,522 points, 0.81 per note, 16.3 per second -> **c25 2,683, 0.48, 9.7** (timpani left out).

## CC7 law per family (range test, `records/ranges.txt`)

P1 (trims in CC7, moved time) against the same-start control P0, per-bar stem level:

| family (track) | CC7 range in the passage | per-bar difference |
|---|---|---|
| HO woodwind (Clarinet 1, 0-132) | 44-127 | median +0.00 dB, no bar over 1.0 |
| HO brass (Horn 1, 0-40) | 95-127 | median +0.01 dB, no bar over 1.0 |
| HS strings (violas, 0-132) | 51-127 | median +0.01 dB, no bar over 1.0 |

The 20·log10 law holds on all three families. Opus treats a track with no CC7 lane as CC7 127. The harp was not tested
and stays in the envelope.

## Track-bars more than 1.5 dB off

- Simulated (envelope + CC7 against c24's envelope, `records/sim_vs_c24.txt`): 102. Most are intended:
  - the CC7 spans and role edits above (reprise 277-281, codetta 225-228, violas 213-224, Oboe 1 130-132 / 286-288,
    Flute 1 277-280 / 348-356);
  - notes where c24's note_move_guard / note_slew had held a level the written envelope did not have (Bassoon 2 183-184
    now follows its written role ramp).
- With the c25 data in both, the CC7 conversion alone moves 78 track-bars (`records/sim_cc7_only.txt`). These are
  essentially the same intended spans plus the summit's arrival-weight change.
- Measured on the stems (`records/stembars_c25_vs_c24.txt`): 145 track-bars. Most are listed above.
  - Unexplained: Flute 1 bar 56 +5.3 on unchanged data and an unchanged effective level (one short note; round robin
    suspected).
  - Violins I 19 bars at -1.6..-3.3: the Spiccato cut.
- **The celli before the sub. p of 277 and the 349 entry** (c24 fault, +4.7 / +5.4 from slew anticipation): their
  trims now step in CC7 at the moved onset, and no celli bar 276 / 348 differs by more than 1.5 dB from c24 on the stem.
  B measured that c24's forte before the mark was unchanged from c18, so nothing is left to fix there.

## Spiccato notes against their neighbours (`records/spic.txt`; 68 rerouted notes, whole render)

| | c24 | c25 |
|---|---|---|
| median over neighbours | +3.8 dB | **+1.4 dB** |
| p90 | +7.8 | +4.9 |
| over +3 / over +5 | 45 / 23 | 15 / 6 |
| F sharp 342 / 942 vs accented C 345 / 945 | -23.8 / -23.8 vs -26.8 / -27.2 | **-27.8 / -27.9 vs -26.9 / -27.2** |

- Separation (rt25 sep): whole movement 5.2 -> 4.8; 48-132 7.1 -> 5.0; 311-360 6.0 -> 6.0; 756-828 6.3 -> 5.5;
  912-960 6.1 -> 6.1. Every passage is 4.5 dB or more.
- c24's separation gain over c23 (4.2) is mostly kept.

## Measured (c24 -> c25)

- **Summit** (stem level 1005-1008): Trumpet 1 -26.7 -> -29.1, Horn 1 -29.8 -> -32.1, Flute 1 -27.3 -> -26.1,
  Oboe 1 -31.6 -> -31.1. Trumpet 1 is now under the fff flute, but still 3 dB over Horn 1, which lost its weight too.
  Per-bar stems: Trumpet 1 / Horn 1 bar 336 -2.3.
- **Inner lines** (inner23, line over all others):
  - reprise second idea (Flute 1 + Oboe 1, 828-840): -0.4 / -0.1 -> **+2.4 / +3.2**;
  - violas + Violas div 648-672: +3.8 / -0.7 / -4.6 / -1.3 -> +5.6 / +0.4 / **-2.6** / +0.2 (target -2 not met in
    bar 221);
  - codetta oboe 672-684: -0.5 / +3.6 -> +0.5 / +4.1.
- **Flute 1 col Vl. solo 1044-1068**: -48.9 -> **-45.9 dB**, solo -40.6 -> -40.1 (C's target -46.5..-45.5 and solo
  within 0.5: met).
- **Accents** (revised measure, against the detached note before; `records/acc2.txt`):
  - Flute 1 -0.9 -> -0.1, cor anglais -2.9 -> -2.3 (peak 0.28 -> 0.23 s), Flute 2 -2.2 -> -3.6, Clarinet 2 -3.8 -> -5.4,
    Violins I -3.4 -> -3.2;
  - others within 0.2; celli +1.0.
  - Over +3: unchanged. Dan's median +1..+2 is still met only by the celli. No unaccented note is louder than the
    accent after it at 342 / 942 now.
- **Timing**:
  - measure S (`records/timing.txt`): over 25 ms 27 %, over 60 ms 5 % (c24 27 / 5).
  - celli trio tune 504-552 (pcx): median +36 -> **+30 ms**, over 60 ms 38 -> 31 % (A's target +15 / 15 % not met).
    - 576: +144 -> +2 ms.
    - 542 overshot to -89.
    - 510 / 512 / 528 are still +79..+101; 512's and 570's leads are capped by the note before, so they did not grow.
  - all celli joins: +31 ms / 31 % -> +30 / 26 %.
- **Per-bar master against c24** (`records/bars_c25_vs_c24.txt`): median 0.0.
  - Over +1.5: bar 279 +2.1 (Flute 1's reprise row removed).
  - Under -1.5: bars 19 / 22 -1.7 (Violins I Spiccato cut).
  - No round-robin swings over 1.5 dB.
- **Hall** (`records/hall.txt`, `hall14.txt`):
  - master G.P. drop at +0.3 s 18.7 dB, 20 dB fall 0.33 s, RT60 1.40 s;
  - mp3 17.2 / 0.34 / 1.44;
  - hall14 17.2 dB, t20 0.35, RT60 1.50, soft ends 0.07-0.19 s, returns -12.77 dB re dry.
  - Inside Dan's limit on both, and not drier than c24.

## Delivery, against the shared spec (c25 mp3, second delivery; `records/order_mp3_final.txt`)

| | c24 | c25 |
|---|---|---|
| 1. I / TP | -14.0 / -1.3 | **-14.0 LUFS / -1.3 dBTP** |
| 2. summit lead | +0.55 over 335 | **+0.56 over 335** (no bar outside 336-339 within 0.5 LU) |
| 3. f -> ff | 2.24 | **2.31 LU** |
| 4. p10 short-term | -20.1 | **-20.3** |
| 5. limiter summit / 105-120 / 305-320 / 72 / 300 / final | 3.8 / 2.3 / 2.2 / 0.5 / 0.9 / 0.1 | **3.7** / 1.8 / 1.8 / 0.8 / 0.9 / 0.1 |
| 6. LRA | 10.5 | **10.5** (first delivery 10.4) |

- Climax order on the mp3: 336 -7.2, 337 -7.5, 338 -7.6, 335 -7.7, 339 -7.8, then 110 / 300 -8.3.
- Crescendo arrivals: 41 +0.5, 72 +0.7, 105 -0.4, 129 0.0, 197 +0.6, 209 +1.2, 285 +0.4, 300 +1.5, 304 +0.2, 305 -0.4,
  329 +2.3, 336 +0.6 (as c24 within 0.2).
- Quiet means: fugato -20.5 -> -21.1 (the ride change), others within 0.3.

## Range tests (`records/ranges.txt`)

- P0 control: same starts, from the c24 project.
- P1 (vA): Violins I, Clarinet 1, Horn 1, violas, celli.
- P2 (vB): Violins I.
- Memory was settled before each pass, two discards were rendered before P1 and P2, and no notes were silent in any
  pass.
- Spiccato: P1 (velocity -10, v>=90 -4) left the soft rerouted notes at +2.5 / +2.9. P2 (velocity -13 plus the 1-54
  layer -2) gave +1.3 / -0.1 / -0.9, inside A's -1..+1.5. Adopted P2.
- Critic C's whole-row -2.5 (vC) was prepared but not rendered: P2 met the acceptance, and a whole-row cut also lowers
  the original Spiccato phrases, which are not hot.

## Rejected, deferred, not done

- Coordinator item 6 (smaller items):
  - A #4 (Violins I STAC_MIN_SOUND_S 0.14 s + 220 ms cap) and C #2 (oboe / cor anglais Main -9 / -6 test): not done
    (lock time spent on items 1-3).
- B #4c (the sfp at 900 as a CC11 shape) and B #4d phrase shapes into CC11: not done. Clarinet 1 / Clarinet 2 /
  Flute 1 / Oboe 1 at 900 no longer appear in the guard (the trims' fall is now in CC7).
- B #5a's alternative (bass clarinet -2 dB) not needed.
- Positive role ends (celli 876, Violins I 1012, Horn 3 1028) were not moved into CC7: the lane has no headroom at those
  dynamics.
- `WARN Violoncellos: 3 level rows ramp inside a led legato transition` (early fills 582 / 600 / 780): present since c21.
  Those rows are in the shape class, which VOL_CLASSES ("slow",) does not write, so they do not sound.

## Faults still audible (Dan's rule: no envelope fix)

- Celli trio tune joins still +30 ms median (510 / 512 / 528 about +80..+100 ms late; 542 now 89 ms early).
- Violas' div. thirds bar 221: -2.6 dB under the rest.
- Trumpet 1 at the summit 3 dB over Horn 1 (both printed one step apart: f / ff).
- 9 + 9 guard notes (listed above).
- E -> B at bars 117 / 317 11-12 dB against c18's 15.4.

## Research items

| item | status |
|---|---|
| EW template mix, returns, seats | adopted (unchanged) |
| no volume automation per note | adopted; guard 25 / 64 -> 9 / 9 |
| dynamic trims as CC7 (finale technique 135) | **adopted** (law measured on HO woodwind, HO brass, HS strings: 0.00-0.01 dB median) |
| role / passage edges into rests with CC7 (finale technique 136) | adopted in part (Oboe 1, Clarinet 2, Horn 1, accompaniment spans) |
| accents by the KS Masters' accent rows | adopted: flutes, Oboe 1; rejected: cor anglais, Clarinet 2, Violins II / violas Marc rows |
| shared -14 delivery + room-noise bed | adopted |
| one legato row per string line, keyswitch 0.15 s ahead | adopted (unchanged) |
| per-region / per-row volume in the Opus state | adopted (+ Spiccato velocity-layer cuts) |
| CC16 resets | adopted on the celli fugato; separate legato tracks, timpani hard sticks, recorded crescendo rolls pending |
| oboe Main lower than -9 dB (RESEARCH part 1) | pending (C #2's test not run this cycle) |
