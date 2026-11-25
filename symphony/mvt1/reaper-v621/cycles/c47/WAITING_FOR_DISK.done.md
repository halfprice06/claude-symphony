# Cycle 47: waiting for disk space (2026-11-07)

`df -g /` before step 5: 22-25 GB free during this run (23 GB at the end), under the coordinator's 30 GB floor. REAPER was
not locked, started or touched. c46 used 9.8 GB; c47's pass 2 holds 20 tracks (c46: 14), so expect about 11-12 GB.

## Done (steps 1-4)

- **Snapshot:** `cycles/c47/before/` (tools/*.py, build/score_config.py, build/*.json = the c46 final data).
- **Tools** (generic; with the tools changes alone, the c46 config gives a byte-identical parts.json, checked):
  - `tools/state_check.py` (new): per-note level / pcX check of two renders on unchanged data. On c45 -> c46 it lists exactly
    the Trumpet 1 runs (bars 69-71 +6.6 dB / -41 ms, bars 113-114 +5.6 dB / -46 ms, 643 +4.6 dB) and Horn 3 164 (+5.5 dB,
    -95 ms), plus the known c45 Violas swap (qn 132.5-138, 146.5-152.75, 537-541: -5..-8 dB). Output kept in
    `cycles/c47/state_check_c45_c46.txt`. `render_cycle.py` now runs it after the probe (metrics/state_check*.txt).
  - `score_to_parts.py`: ART_SPANS `"stroke_row"`; STR_REP_NEW_BOW strokes keep a span row listed in STR_STROKE_ROWS, are
    never merged into the legato note before, and keep the stroke lead on a "Stac ..." row; windowed test aliases
    (`in_alias_win`): hairpins and re-bow fill lists only from their own windows, CC70 lane from the source.
- **Data** (parts.json regenerated and diffed: only Clarinet 1, Clarinet 2, Bassoon 1, Violins I, Violas, Violoncellos,
  Cello solo, Violins I f62, Violins II f62 changed among the production tracks, plus 13 pass-2 test aliases):
  - B #2 roles Clarinet 1 [575.75, 582, -5, 0.25]; B #3 roles (Bassoon 1, Clarinets, Violins I); B #4 celli -8 dB at
    157.5-159.6; B #5 RIDE_TRIMS +0.5 dB on nine soft spans.
  - A #2 Cello solo fills 687 / 694 (+ Bassoon 1 135, Clarinet 1 700); A #3 PICKUP_LIFT Violins I 136.5 12 -> 6, Clarinet 1
    504.5 9.5 -> 6.5; A #6a Violas 78 as an exact LEVEL_SHAPES row from the A-flat4's moved onset (the roles row removed:
    a role's start ramp is always 0.5 qn); A #6b entry_leads Violins I 472.5 0.05, 474.5 0.04; A #6d leg_leads Violins I /
    II 232.0 +0.04 / +0.02 (Violins II with a listed cap of 0.82, else the cap absorbed it).
  - Pass-2 tests (TEST_TRACKS, mix.json entries = source copies with only the tested key changed):
    - soft cap, no pp cap (350 p, 150 mf-ff): "Vln II / Vla / Vc / Cb ppcap test", whole-piece windows (Violins I left out
      for memory); fallback 700 ms at pp on the coda: "Vln II / Vla / Vc / Cb pp700 test" (680/696-730).
    - stroke rows: variant A ("Stac Leg BC + Slur + Port MAX", v40-60) on the celli strokes 84, 88, 152, 156, 448, 456 inside
      "Vc ppcap test" and on Violas 80, 372, 500 inside "Vla ppcap test" (mf-f notes, both caps 150 ms there); variant B
      ("Sus Marc LITE", v25-45) on the same celli strokes in "Vc stroke B" (main caps). Celli 47 is not tested (its stroke
      holds a later re-bow point; the pipeline supports that only on Sus MAX). Timing equals the main strokes'; the test
      strokes miss the main strokes' Sus row trim (Violas 80 +4.5 dB, celli 156 +1.5 dB in the envelope): remove the
      envelope difference when comparing levels.
    - brass "Marc Sus LITE" (MANUAL-GAPS #1) at v45-75, swell +1 dB, on the accents of bars 32-33 / 142-143: "Tbn1 / BTbn /
      Hn1 / Hn3 marc test" (horn tests: the 237 ms horn cap also on the row). The test notes are unled (the main accents
      take a 0.1 qn re-tongue lead): fit the lead from pcX if the row passes.
    - `alias_check` (score_to_parts log): every test differs only in the tested rows, velocities, swells and the release
      cap key, plus window-start notes of "Vc stroke B" (80, 144, 440).
    - Rows loaded in pass 2: 70 (c46: 61, settled at 34 GB, 37 after). If pass 2 settles above about 44 GB, delete the
      pp700 tests first.
- **Simulated on the c46 stems** (level-only items, `stem_fix.py --out` + `cycles/c47/actor_scripts/lvl47.py`):
  - B #2: Clarinet 1 re M at 576-578 -3.8 -> -7.3 dB K; oboe minus the loudest other at 578.0 -3.3 -> +0.9, then +5.2..+11.8.
  - B #3: Violins I minus the loudest other median +1.2 -> +2.8 dB, beats under 0: 3 -> 0, under +3: 15 -> 8.
  - B #4: celli minus the loudest other (K) +1.7 / +5.6 / +6.4 / +2.4 -> -1.3 / +2.6 / +3.4 / -0.6 at 157.5-159.
  - B #5: delivered span 19.3 -> 19.0 dB, LRA 14.9 -> 14.7, limiter 1.0 dB (all c47 level changes together).
  - A #2: Cello solo dips 687 8.6 -> 2.5 dB, 694 6.2 -> 1.2 dB, peaks +1.4 / +1.3 dB over the louder body.
  - A #3: Violins I accent 3.4 dB over its pickup (was -0.2), Clarinet 1 2.1 dB (was -0.5).
  - A #6a: Violas pre-join peak over the A-flat4's body +8.1 -> +2.2 dB.

## Left (steps 5-6), in order

1. `df -g /` (30 GB or more), then the turn rule and `reaper_ctl.py lock "mvt1 c47 actor"`.
2. Main pass: `start`, `open`, `build_reaper.py build/parts.json jobs --midi-only` (the five string tracks rebuild fully:
   350 ms caps, checked offline), then `build_reaper.py build/parts.json jobs "Trumpet 1" "Horn 3"` (full rebuild,
   coordinator (a)), `restart`; 33 tracks, memory, MAC DRIVE; `render_cycle.py 47`. Read metrics/state_check.txt: if
   Trumpet 1 or Horn 3 flip again, `cycles/c47/actor_scripts/splice47.py` (c45 audio; data identity checked). `quit`.
3. Pass 2: `start`, `--pass2 open`, `--pass2 --midi-only` (f62 aliases rebuild fully, Cello solo envelope rewritten, 13 test
   tracks new), `--pass2 restart`, memory check, `render_cycle.py 47 --pass2`; check every stem's length (c46 crash).
4. Decide the tests: soft cap with `cycles/c46/actor_scripts/softcap46.py` adapted to the ppcap / pp700 pairs (C #1 / A #5
   criteria: master final -10 dB at >= 0.20 s and -20 dB at >= 0.48 s after the swap; pp chord changes: old pitch down 10
   dB within 0.35 s; re-bow steps no worse; mf-ff / p ends unchanged; report 10 / 20 dB fall times as in c46), splice the
   passing sections where the effect is, then refit the final chord's re-bow fills (`fit_rebows.py`, stem fix). Strokes
   with strokes46.py / under46.py (A #4 criteria; keep a variant only per onset where all pass). Marc Sus LITE: 2-5 kHz
   first 80 ms minus body (-6..-2 dB, never over +3), master 2-5 kHz jump, level over neighbours 2-4 dB, pcX.
5. Stem fix, `render_cycle.py 47 --measure-only`, delete the test tracks from the pass-2 project and from score_config /
   mix.json, save, `--pass2 quit`, `unlock`. Delete test stems and scratch WAVs once measured.
6. CHANGES.md (opens "For Dan: what to listen for in c47"; "Values for the other movements" incl. c46's Trumpet 1 being too
   loud in bars 69-71, 113-114 and 161 and whether c47 fixes it), HISTORY, LEARNINGS, MANUAL-GAPS #1 result, mockups page.
