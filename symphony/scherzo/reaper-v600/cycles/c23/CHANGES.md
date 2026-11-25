# Cycle 23: changes (actor, on the c22 render)

STATUS: **rendered once**, 2026-11-17 19:44-19:51 CST, from a freshly restarted REAPER (state guard 0 before the render).
- mp3: `cycles/c23/scherzo-mockup-c23.mp3` (with the new room-noise bed). Data as rendered: `cycles/c23/build_render/`.
- Lock: queued 18:00 behind mvt3 (c25 actor), held 18:40-19:52 (72 min; `phase.log`): open, settle 44 GB, guard 0,
  control pass (12 ranges), passes A, B, C, A2 (Violins I), restart, settle 44 GB, passes L, SW, M, final `--midi-only`
  build of all 31 tracks, restart, settle 44 GB, guard 0, audio_init, render, save, quit, unlock.
- **The save after the render left Horn 2 / Horn 4 stale** (state guard: 1FHs attack values rewritten by Opus on save,
  as in c22). I had already quit and unlocked, so they were not rebuilt: the next actor's guard run must rebuild them.
  The render itself was made with guard 0.
- REAPER memory: 44 GB settled before the render, 44 GB after it (0 GB compressed); 50 GB after the first batch of
  range tests (restart before the second batch).
- Disk: 34-41 GB free during the cycle, 39 GB at the end. c22's stems deleted (00_Master.wav and mp3 kept), my range
  WAVs deleted. Backups/ not touched. Probe: late or hole 0. Master -21.4 LUFS, LRA 22.5, TP -2.0 dBFS, sample peak
  0.788 (no clipping).

## Bar 23 figure (first check)

Range tests (Violins I, qn 54-132, one start; control = c22 state). Decay = dB the note has fallen at the next note-on.

| variant | pair vs neighbours | decay F#->G, G->A, A->B (median) |
|---|---|---|
| control | -8.5 / -12.8 | 3.8, 10.7, 1.5 (2.7) |
| **a: lead 0.10 s on both, each ending 0.03 s before the next moved note-on** | -2.3 / -4.3 | 1.1, 8.4, **6.6** (3.9) |
| a, second pass (in pass L) | -3.2 / -5.1 | 1.2, 5.3, **7.1** (3.3) |
| a2: lead 0.10 s on the A only | +5.2 / +3.0 | -3.2, 10.4, 2.0 (3.3) |
| b: CC1 floor 108 over the pair (new `CC1_FLOOR_SPANS`) | -7.7 / **+3.5** | 3.4, 1.1, **-1.9** (0.6) |
| c: Sus MAX p-layer release cap 150 ms | -8.2 / -10.9 | 3.4, 7.9, 1.4 (2.4) |

- b made the A louder than its neighbours and still rising into the B. c changed nothing measurable. a2 was worse.
  Combinations with b or c were not run (neither helped alone). **a adopted on bar 23 only.**
- The loud pairs (125 / 209 / 821 / 893) with route a (pass L): pairs 1-3 dB nearer their neighbours, but the second
  note's decay before the landing note fell 2.0 -> 0.4 (125), 1.9 -> 0.4 (209), figure median 9.0 -> 4.4 dB (821 / 893).
  Rejected (blur). Bars 38 / 263 untouched.

Every occurrence on the full renders (`records/fig23.txt`, decay before the next note-on / trough, dB):

| | c21 | c22 | c23 |
|---|---|---|---|
| bar 23 (median) | 2.9 / 1.2 | 2.9 / 1.2 | **3.4 / 3.4** |
| bar 23 per note (F#->G, G->A, A->B) | | 7.0, 3.9, 1.8 | 1.4, 5.4, **5.8** |
| bar 23 pair vs neighbours | | -13.5 / -13.2 | **-7.6 / -10.7** |
| bar 38 | 6.5 / 7.2 | 7.3 / 11.0 | 7.3 / 11.0 |
| bar 263 | 5.1 / 4.3 | 5.7 / 4.7 | 5.7 / 4.7 |
| other 15 Violins I + 15 Violins II | | | identical (unchanged data) |

The A no longer sounds when the B starts (5.8 dB decay against 1.8). On the full render the pair is still 7.6 / 10.7 dB
under its neighbours, short of the 6 dB target that the range tests reached (round-robin positions differ). The F sharp
before the G now decays only 1.4 dB when the G starts: the G sits in the staccato's ring. Nothing at any occurrence is
worse than c21 on the figure median.

## Changes made

### Tools (generic, off by default)
- `tools/score_to_parts.py`:
  - `CC1_FLOOR_SPANS` {track: [(q0, q1, CC1)]}: a CC1 minimum, applied after `CC1_SET_SPANS` (tested, not used here).
  - `STAC_MIN_SOUND_S` {track: s} + `STAC_MIN_SOUND_GAP_S`: a short-row note sounds at least s from its moved
    note-on, but never past the next note-on less the gap (tested, not used here).
  - `ROW_CHANGE_ACC_SKIP` may be a dict {track: [onsets], "_all": [...]}.
- `tools/deliver_master.py`: **room-noise bed** (shared spec, mockup-kit README): pink, extra first-order fall above
  2.5 kHz, fourth-order low cut at 84 Hz, L = 0.8a + 0.6c / R = 0.8b + 0.6c, seed 20261118. It is scaled to -60 LUFS
  integrated and added after the limiter and the trim / fade, before the encode. env `DELIVER_ROOM_BED_LUFS` (default
  -60, "off"). Movement I's file did not contain the function yet, so it is written from the README spec.

### `build/score_config.py` (c23 block; switches C23_F23, C23_LOUD, C23_LEAD, C23_LEAD1, C23_STAC, C23_WACC, C23_FHP, C23_MARCLNG)
1. Bar 23: `LEAD_SET_AT` Violins I 67.0 / 67.5 0.10 s; `NOTE_END_AT` 67.0 -> 66.928, 67.5 -> 67.670 (0.03 s before
   the next moved note-on).
2. Oboe 1's tutti accents (315, 327, 345, 351, 915, 927, 945, 951) on "Sus Accent MAX": velocity 90 (middle overlay
   layer 75-114, read from the .oib), no CC11 bump on that row, lead 0.04 s (was 0.08 with the ROW_CHANGE add).
3. Flute 1 crescendos 304-311.75 / 904-911.75: CC11 ramp +0 -> +20 over the last 6 qn, gone before the ff staccato.
   **It does not work**: CC11_REST_MAP caps woodwind CC11 at 108, and the stem rose only 0.1-0.4 dB. The max_arrival_cc
   route also does nothing, because these two hairpin gains are never converted (no note sounds 0.25 s past the release).
   Kept, because it is harmless; listed as open.

### `build/roles.json`, `build/mix.json` (`actor_scripts/apply23.py --flacc`, rerunnable from `before/`)
- Bars 333-335 (B #2): the ten woodwind summit rows start at 996 again at the c22 halved values. Celli and Horn 1 stay
  at 1004.75.
- Trio climax (B #3): Flute 1 [648, 660, -4].
- Flute 1 / Flute 2 "Sus Accent MAX" (A #3, B #1): overlay `vel>=75` -1.5 dB, G6 (pitch 91) -2.0 dB. The coordinator's
  -3 / -3.5 went too far on the range test: Flute 1's tutti accents 0.1 -> -2.3 dB against their neighbours, and
  against the note before -1.6 -> -4.0 (Flute 2 +1.4 -> -3.0), all under Dan's +1..+2. So both values were halved,
  which keeps G6 at -3.5 in total.
- Opus state changes (full rebuild): Flute 1, Flute 2 (region gain), Oboe 1 (new row). The final build wrote all 31 tracks.

## Rejected (range tests against a control from the same start)
- Violins I staccato blur (A #2): `STAC_MIN_SOUND_S` 0.10 s (realised 0.094 s) plus a 150 ms any_dyn cap on the three
  short rows. Separation went 4.5 -> 5.8 dB (56-132) but 4.7 -> 1.2 dB in the tutti (313-360), and the 60 ms peaks fell
  -48.9 -> -53.8 and -36.9 -> -56.9 dB. The cap still cuts the peaks. A #2 stays open.
- Cor anglais and Clarinet 2 on their accent rows (C #2a): cor anglais against the note before -3.0 -> -4.2 dB, peak
  0.28 -> 0.34 s; Clarinet 2 -4.5 -> -6.8.
- Dropping the 0.04 s ROW_CHANGE add on the violins' tutti accents (C #2): Violins II -4.0 -> -6.3, Violins I
  -1.6 -> -1.8 dB, peaks unmoved.
- Violins II "Marc Lng RRx4" (A #4): accents -4.0 -> -20.2 dB, the staccatos' 60 ms peaks -34.0 -> -54.3, separation
  7.2 -> 0.0. The row change broke the notes after it. The fallback (Sus Marc LITE with a capped attack) was not tried;
  the finale reports (c25) that that row's CC11 is not 20 log10 on Violins I.
- Violins I CC11 shape inside the tutti accented half notes (C #2b): not tried (lock time).

## Measured (c22 -> c23 full renders; `records/`)
- **Accents**:
  - First 100 ms against neighbours (old measure): Flute 1 +1.4 -> +1.1, Flute 2 +0.4 -> -1.8, Oboe 1 -1.8 -> -0.4
    (peak 0.27 -> 0.24 s), others unchanged.
  - Revised measure (`rt23.py acc2`: against the note before, when it is detached and within 2 qn; isolated and
    post-G.P. notes left out; the slurred follower not used):

  | track | median c22 -> c23 | p90 c22 -> c23 | over +3 | peak after beat | first 100 ms minus 150-350 ms |
  |---|---|---|---|---|---|
  | Flute 1 | -0.9 -> -0.4 | +4.6 -> +3.7 | 6 -> 5 | 0.04 | +1.2 -> +1.0 |
  | Flute 2 | -1.9 -> -2.2 | +3.2 -> +1.3 | 1 -> 1 | 0.06 | +3.6 -> +3.7 |
  | Oboe 1 | -3.8 -> -2.5 | +2.8 | 2 | 0.27 -> 0.18 | -1.0 -> -0.3 |
  | cor anglais / Clarinet 2 / strings | unchanged | | | 0.22-0.34 | negative |

  - Flute 1 G6 over Violins I (first 0.3 s): 315 +1.1 -> -0.9, 351 +1.8 -> -0.2, 999 +6.4 -> +2.3, 819 C6 +2.9 -> +1.9.
  - Tutti downbeats: the string accents' fronts are unchanged, so their weight still arrives 0.2-0.3 s after the beat
    (open).
- **Bars 333-335**: winds minus strings +2.6 / +2.4 / +3.2 -> +0.9 / +0.4 / +1.3 dB. Master bars 333-336 -17.6 / -17.6 /
  -16.8 / -15.5 -> -18.4 / -18.4 / -17.7 / -15.6, so the step into the summit grew from 1.3 to 2.1 dB.
- **Trio climax**: Flute 1 minus Violins I per 3 qn from 648: +0.6 / +4.8 / +5.4 / -0.1 -> -3.4 / +0.8 / +1.4 / -4.0.
- **Flute 1 crescendos**: 902-910 note levels -34.2 / -31.9 / -32.7 / -32.5 / -33.4 -> -34.2 / -32.0 / -32.3 / -32.4 /
  -33.4. The ff at 912 is still about 10 dB over the A5 (open; see above).
- **Violins I staccato separation**: 4.0 -> 4.2 dB median (unchanged data; the bar 23 notes moved).
- **Per-bar master against c22**: median 0.0. Over 1.5: none. Under -1.5: bar 58 -2.9 (celli round robins on unchanged
  data; c22 read +2.9 there).
- **Inner lines** (`inner23.py`, doubling tracks now join the line, B #4): the tune of bars 37-43 (Flute 1 + Oboe 1 +
  doublings) is +3.7..+16.9 dB over everything. Clarinets were not cut further. The doubling rule also absorbs
  accompaniment that shares pitch classes: the bass clarinet's 630-666 "line" took in the low strings (+17..+31 dB, an
  artefact). Its threshold needs a pitch, not only a pitch-class, test.
- **Envelope** (`slope17.py`): 4,770 points, 0.83 per note, 17.2 per second; 0 per-note rows. The slope guard lists the
  same 9 notes as c19-c22. Each is a slow-class move inside a note held across it:

  | track, qn | size | what writes it |
  |---|---|---|
  | celli 312 (note from 310.64) | 4.3 | role row [312, 360, +4.5] edge inside the tied arrival note |
  | celli 912 (910.61) | 4.3 | role row [912, 960, +4.5], same |
  | celli 362 (359.47) | 4.0 | role row [362, 396, -4] edge (sub. p area) inside the held note |
  | Horn 2 1005 (1004.76) | 3.2 | crescendo gain into the fff, inside the led note |
  | Horn 3 953 / 936 | 3.0 / 2.3 | gain release (4.3 -> 2.0 dB) inside the note, within the [913, 960, +2] row |
  | harp 708 (chords ringing from 702-708) | 3.0 | trio rit. area row inside ringing harp chords |
  | Oboe 1 1005 (1002-1005.02) | 2.3 | crescendo gain 1002-1005 arriving inside the held note |
  | violas 197 (196.74) | 2.2 | role row [192, 198, +3.5] end edge inside the note |

  None were removed this cycle: each needs a row moved to a rest, or a CC11 equivalent, plus a check that its level is
  not lost. They are listed for c24.
- **Timing** outside 25 / 60 ms: not measured this cycle.
- Faults still audible (Dan's rule, no envelope fix): the bar 23 pair 8-11 dB under; the Flute 1 crescendos into 105 /
  305; the string tutti accent fronts; Violins I counterstatement staccato separation; the string legato swell.

## Delivery, against the shared spec (c23 mp3, with the bed / without the bed)

| | c22 mp3 | c23 with bed | c23 without bed |
|---|---|---|---|
| 1. I / TP | -14.0 / -1.4 | **-14.0 LUFS / -1.4 dBTP** | -14.0 / -1.4 |
| 2. summit lead | +0.61 over 335 | **+0.64 over 318** (335 now -8.2, +0.7 behind) | +0.64 |
| 3. f -> ff | 2.24 | **2.22 LU** | 2.22 |
| 4. p10 short-term | -20.2 | **-20.2** | -20.2 |
| 5. limiter summit / 105-120 / 305-320 / 72 / 300 / final | 2.7 / 2.2 / 2.1 / 1.0 / 0.8 / 0.1 | **2.8 / 2.2 / 2.1 / 1.0 / 0.8 / 0.1** | same |
| 6. LRA | 10.6 | **10.5** | 10.5 |

- Climax order on the mp3: summit -7.5, then 318 -8.1, 335 -8.2, 110 -8.3; no bar within 0.5 LU of the summit.
- Crescendo arrivals: 41 +0.6, 72 +0.5, 105 -0.4, 129 +0.2, 197 +1.1, 209 +1.4, 285 +0.5, 300 +1.4, 304 +0.2, 305 -0.3,
  329 +2.1, 336 +0.6 (209 +0.9 -> +1.4 from the Flute 1 trio row).
- Ride rows (coordinator's c26 note): bar 53 and the trio A6 rows sit on held ff passages, not on arrivals. Bar 209
  (the trio ff arrival) reads +1.4 and bar 41 +0.6 (the counterstatement lift returns to 0 across that crescendo).
  Not changed.
- Hall (`hall17.py`, G.P. drop at +0.3 s / 20 dB fall / RT60):
  - master 18.0 dB / 0.37 s / 1.40 s;
  - mp3 with bed 18.9 / 0.33 / 1.38;
  - mp3 without bed 18.9 / 0.33 / 1.38.
  - The bed only removes the late-slope fit (-25..-55 dB reaches the bed). Inside Dan's limit.

## Research items

| item | status |
|---|---|
| EW template mix, returns, seats | adopted (unchanged) |
| no volume automation per note | adopted; 0 per-note rows; 9 slow-row moves inside notes listed above |
| accents by the KS Masters' accent rows | adopted: flutes, Oboe 1 (now also on its tutti accents). Rejected: cor anglais, Clarinet 2 (tutti, range test), Violins II / violas Sus Marc LITE (c22), Violins II Marc Lng (c23) |
| shared -14 delivery + room-noise bed | adopted (spec items 1-6 met with the bed) |
| one legato row per string line, keyswitch 0.15 s ahead | adopted (unchanged) |
| per-region / per-row volume in the Opus state | adopted (flute accent overlay and G6) |
| CC16 resets, separate legato tracks, timpani hard sticks, recorded crescendo rolls | pending |

## Coordinator notes received during the cycle
- Finale c25 (Sus Marc LITE CC11 law, accent bumps under cc_cap, crescendo gains held into an ff): no accent cap
  check was run. The Flute 1 hairpin gain is still held over the 912 / 312 arrival (vol_db 4 dB released over 912-913).
- Finale c26 (slope guard, ride rows, soft woodwind runs): the slope list is named above. Soft woodwind runs were not
  checked.
- Room-noise bed: ported and in this delivery.
