# Cycle 15 changes (actor)

Snapshot of the c14 tools and build/*.json: `before/`. Scratch and analysis: `/private/tmp/claude-501/mockup-loop/c15-actor/` (`tl.py` measures c14 and c15 stems each on its own tempo map; `cC/` holds critic C's scripts and `leg_15.json`; `pdiff2.txt` is the parts.json diff).

## Process

1. Edited `tools/score_to_parts.py` and `build/{roles,pitch_trims,note_trims,early_fills,leg_leads,entry_leads}.json`, regenerated parts.json and diffed it against `before/build/parts.json`.
2. `build_reaper.py build/parts.json jobs --midi-only --tempo` (the phrase arcs changed the tempo map). Violas were fully rebuilt (the Detache row changed the Opus state); the other 28 tracks were updated in place.
3. Saved, quit and reopened REAPER. The first reopen deadlocked inside Opus's `VST3_LoadState` (main thread waiting on an Opus mutex, 406 MB, no progress for 3 minutes). I killed REAPER and started it again with `open -a REAPER --args -new`, waited 30 s, then opened the project with a bridge job. That load worked: 56 GB, 0 GB compressed.
4. One render (`render_cycle.py 15`). Attack gate 17 of 19:
   - Vc 212 at 6.8 dB. This is the known marginal probe (c14 7.0).
   - Vln II 212 at 7.8 dB (c14 5.5). The 25 ms envelopes of c14 and c15 around qn 212, each measured on its own tempo map, match within 1 dB, frame for frame. The tremolo entry is unchanged. The probe takes the minimum 10 ms frame, and that frame differs between the renders.
   - Not re-rendered. No post-render stem fixes were made.

## Accepted

**A #1: sostenuto hold-through** (`SOST_HOLD_THROUGH`). A swell_sost note followed without a rest by another swell_sost note holds +2.5 dB to the next onset + 0.25 qn, then releases to 0 at 40% of the next note. Before the last note of the span, or before a rest, it still drops to 0. Clarinet 1 qn 204: the Ab4 +6 pitch trim is skipped there (`_skip_onsets` [204]) and replaced by a note trim of +2.

**A #2:** early fills for Violoncellos 74 {5, pre 0.05, hold 0.35}, 75 {6, 0.05, 0.40}, 246 {4, 0.05, 0.35}, 247 {5, 0.05, 0.40}, 249 {5, 0.05, 0.35}.

**A #3: Violins II sul tasto chords** (`FLAUT_JOIN_TRACKS`, `FLAUT_LEAD_S` 0.15, `FLAUT_OVERLAP_QN` 0.35).
- Same-pitch common tones of consecutive Flautando chords are merged into one held note, with no notch.
- The moving voices start 0.15 s early.
- The old chord's moving notes end at the new onset + 0.35 qn.
- These notes get no swell contour.

**A #4: Trombone 1, bars 63-64.**
- `ACCENT_DB_AT` 213 +3.
- `MARC_ACC_CUT_AT` 213: 0.25, so 213 ends at 214.25.
- The Marc Lng attack moves to where the sample speaks (`MARC_ATTACK_S` 0.04/0.16/0.30 s), and `MARC_ATTACK_DB` goes from 2 to 3. The body stays +2.

**A #5 (test): Violas bar 59 on the Detache row** (`DETACHE_SPANS`, v100, written length + 0.01 qn, no lead). Bar 60 is the Sus MAX control.

**A #6: Horn 1 breath at qn 196** (`BREATH_GAP_AT` 195: 0.5 qn, and `BREATH_FALL_CC` 10 CC over the note's last 0.2 qn).

**B #1:** `SWELL_NO_SOFT_GAIN` stops the soft hairpin gain on three unmarked swells: Horn 1 qn 20, and Violins I/II qn 68 and 240.

**B #2:** roles Double basses [108, 137.5, 5] -> 2.

**B #3:** pitch_trims Flute 1 Bb4 +4, C5 +3, Db5 +3.

**B #4:** roles Violoncellos [78, 90, -6] -> [78, 87, -6] and [87, 90, -2] (the two spans crossfade), plus Double basses [87, 90, -2].

**B #5:** roles Violoncellos [262, 265, 2, 0.25].

**C #1:** `LEG_SOFT_EXTRA_S` Flute 1 (CC11 <= 50): +0.06 s.

**C #2:** `LEG_ART_EXTRA_S` (exact track names):
- Violins II: Leg Slur MAX +0.04, Leg BC MAX -0.03.
- Violoncellos: Leg Slur MAX +0.05.
- Violas: Leg Slur MAX +0.025.

**C #3:**
- leg_leads:
  - Horn 1: 193 +0.10, 195 +0.08, 200 +0.07, 202 +0.10.
  - Violins II: 164 +0.06, 60 +0.03 and 245.5 +0.03 (all net of C #2), and 252 +0.13.
  - Violins I 75 +0.08, Flute 1 200 +0.10, Cor anglais 131.5 +0.08.
- entry_leads: Flute 2 262 +0.10, Bassoon 2 268 +0.08.

**C #4 (test): `ABUT_LEAD`.** In the Bassoon tracks, a soft (CC11 <= 60) Sus re-attack at a new pitch with no gap starts 0.10 s early, and the previous note ends 0.02 qn after the moved start.

**C #5: phrase arcs with depth.**
- "sub" (0.98/0.95, no push): (42,48), (48,54), (54,60), (220,226).
- "main" (0.95/0.88): (30,42), (60,66), (78,90), (226,238).
- An arc that starts where another ends takes its first beat at x0.97.
- The total length is +0.5 s (348.3 -> 348.8 s).

## Rejected or deferred

- **B #6** (Cb 69 Hz bell test): deferred. It needs its own range render, and there was only one render this cycle.
- **C #6** (viola C4 -> Eb4 cap exception): deferred, low priority (inner voice).
- **A #5 failed its pass criterion.** In bar 59 on Detache, the own-pitch share is 0.32 (c14 Sus MAX 0.33, bar 60 control 0.32). The median first dominance is +0.068 s against -0.035 on the control. The bar levels are equal (-32.7 / -32.7).
  - It is no clearer and slightly later. It is kept in this render and in the tools, so the render matches parts.json.
  - Next cycle: set `DETACHE_SPANS = {}`. That needs a full Violas rebuild, because the row unloads.
- **C #4 failed and made the bassoon repeats worse.**
  - Bassoon 1 arrival at body - 3 dB, at the abutting changes:

    | qn | c14 (s) | c15 (s) |
    |---|---|---|
    | 27 | 0.25 | 0.165 |
    | 31 | 0.17 | 0.09 |
    | 24 | 0.015 | 0.29 |
    | 35 | 0.025 | 0.225 |
    | 36 | 0.00 | 0.21 |

  - The same-pitch repeats that follow a led note (qn 22 and 32) now open with 11 dB and 21.6 dB holes about 0.1 s long (c14: 3 dB). The volume envelope there is 0 in both cycles and the MIDI gap is identical (0.03 qn), so the holes come from the sample playback.
  - Kept in this render for consistency with parts.json. Next cycle: set `ABUT_LEAD = {}`.

## Measured, c14 -> c15

Each render is measured on its own tempo map. Levels are plain RMS unless noted.

**Delivery**

| | c14 | c15 |
|---|---|---|
| Master integrated | -23.8 LUFS | -23.6 LUFS |
| Master LRA | 23.5 LU | 23.2 LU |
| Master true peak | -4.5 dBFS | -4.5 dBFS |
| mp3 integrated | -19.8 LUFS | -19.8 LUFS |
| mp3 LRA | 16.0 LU | 15.9 LU |
| mp3 true peak | -1.7 dBTP | -1.6 dBTP |
| mp3 span (p10 to max) | 18.2 dB | 18.7 dB |
| Limiter | 2.0 dB | 1.9 dB |

No clipping. All 29 stems are present.

**Findings**

- **A #1** (`sost.py`): the median step at the onset went from -1.6 to -0.8 dB, and joins falling 4 dB or more from 13 to 8.
  - Master, 0.5 s after against 0.35 s before each onset:
    - qn 208: -1.7 -> -0.4 dB.
    - qn 210: -0.7 -> -0.4 dB.
    - qn 206: +0.6 -> +0.5 dB.
  - Bar 61 is -18.7 -> -18.5 dB, and bar 62 is -20.1 -> -19.6 dB.
  - The target (no join falling 3 dB or more) is not met. Fl2 206/210, Bn2 210 and Hn3 210 still fall 5.5-6.7 dB.
- **A #2:** the Vc first 0.5 s against the body:

  | qn | c14 (dB) | c15 (dB) |
  |---|---|---|
  | 74 | -6.5 | +0.5 |
  | 75 | -10.3 | -3.4 |
  | 246 | -3.7 | +2.3 |
  | 247 | -8.7 | -3.2 |
  | 249 | -6.2 | -0.5 |

  The minima are 4.2-7.3 dB shallower.
- **A #3:** the Vln II trough after each chord change (10 ms frames, 60 ms smoothing):

  | qn | 112 | 114 | 116 | 118 | 120 | 122 |
  |---|---|---|---|---|---|---|
  | c14 (dB) | 14.7 | 11.9 | 6.6 | 10.0 | 10.2 | 8.6 |
  | c15 (dB) | 8.6 | 9.0 | 5.4 | 2.5 | 10.5 | 2.3 |

  The RMS over qn 108-124 went from -50.3 to -49.2 dB. Only partly fixed: qn 114 and 120 still trough 9-10 dB, about 0.9-1.1 s after the change.
- **A #4:** peak over body in the first 0.12 s:

  | qn | 213 | 214.5 | 215 | 215.5 | 216 | 217 | 217.5 |
  |---|---|---|---|---|---|---|---|
  | c14 (dB) | +1.2 | +0.4 | +2.9 | +1.9 | -2.0 | -1.1 | +4.7 |
  | c15 (dB) | +3.2 | -3.2 | +3.8 | +2.6 | -1.3 | -0.2 | +4.9 |

  - The 213 accent is now within Dan's 2-4 dB.
  - The level before 214.5 went from -26.9 to -39.9 dB against a body of -26: a clear break.
  - The Marc Lng attacks are still mixed.
- **A #6:** the Hn1 breath before qn 196 dips 7.2 dB (c14 1.9; target 8).
- **B #1** (lead line per qn):
  - Horn: the swell top at qn 22 went from -34.8 to -37.1 dB. The mp crest at qn 32-33 (-33.9 / -35.2) is now 2-3 dB over it.
  - Theme A: the swell at qn 69-70 went from -37.3 to -39.5 dB, against the mf at qn 82 of -34.8: a 4.7 dB gap.
  - Bar 72: the swell top is -39.0 dB, against -37.3 / -36.2 at qn 250-251.
- **B #2:** Cb minus Vc pizz. peak, median over bars 37-40: +6.7 -> +3.2 dB. Cb peak over the flute: +11.5 -> +7.7 dB.
- **B #3:** Flute 1 minus the summed accompaniment on the low notes: +1.3 to +5 dB better (qn 120 -11.6 -> -8.1, qn 123 -1.8 -> +3.3).
- **B #4:** bar 30, qn 88-89.5: Vc -59.3 -> -55.3 dB, Cb -48.5 -> -50.3 dB. The violas are at -52.8.
- **B #5:** bar 79, Vc+Bn1 per qn: -32.2 / -34.4 / -32.8 -> -31.2 / -33.0 / -31.6 dB.
- **C #1-#3** (crossover medians, `cC/leg.py`):
  - Flute 1 qn 108-140: +0.078 -> +0.038 s (p75 0.118 -> 0.073).
  - Leg Slur MAX:

    | | c14 (s) | c15 (s) |
    |---|---|---|
    | Vln II | +0.058 | +0.013 |
    | Vla | +0.038 | +0.015 |
    | Vc | +0.068 | +0.013 |

  - Vln II Leg BC MAX: -0.017 -> +0.008 s.
  - The listed late notes:

    | Note | c14 (s) | c15 (s) |
    |---|---|---|
    | Hn1 193 | +0.183 | +0.058 |
    | Hn1 195 | +0.173 | +0.093 |
    | Hn1 200 | +0.153 | +0.078 |
    | Hn1 202 | +0.178 | +0.073 |
    | Vln II 164 | +0.268 | +0.153 |
    | Vln II 60 | +0.183 | +0.123 |
    | Vln II 245.5 | +0.193 | +0.138 |
    | Vln II 252 | +0.243 | -0.047 |
    | Vln I 75 | +0.208 | +0.128 |
    | Fl1 118 | +0.233 | +0.173 |
    | Fl1 200 | +0.218 | -0.032 |
    | CA 131.5 | +0.183 | +0.088 |

  - Vln II 252 moved 0.29 s for 0.10 s of added lead, which is not 1:1.

## Open

- Revert the two failed tests: `DETACHE_SPANS = {}` (full Violas rebuild) and `ABUT_LEAD = {}`.
- Sostenuto joins: Fl2 206/210, Bn2 210 and Hn3 210 still fall 5.5-6.7 dB.
- Vln II sul tasto: qn 114 and 120 still trough about 10 dB.
- Marc Lng attack weight is still not consistent.
- Hn1 196 breath: 7.2 dB, against a target of 8.
- Vln II 252 is now early (-0.05 s); reduce its lead by about 0.05.
- B #6 low-end test; C #6.
