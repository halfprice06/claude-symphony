# Cycle 4: changes (critics A, B, C on the c03 render)

Render: `cycles/c04/mvt3-mockup-c04.mp3`. Before-state in `before/`. Actor checks: `actor_scripts/m04.py
ends|joins|rebows|wpcx|spcx|stac|bal` (c03 on `cycles/c03/rendered_build/parts.json`, c04 on `build/parts.json`).
Priority this cycle: Dan's "mushy" note (string releases, re-bow holes, wind staccatos), then timing (S2).

## Accepted

### Carry-over (cycles/c04/CARRYOVER.md)
- Horns 1-4: the c03 stem-fix roles for the stopped notes (roles.json Horn 1 [192, 200, +2.5], Horn 2 [668, 676, +8.5],
  Horn 3 [548, 552, +10.5], Horn 4 [548, 552, +7.5]) written into REAPER with this cycle's build (`--midi-only` list).

### Clarity (Dan: "mushy")
- **C #1, string legato and tremolo releases:** `build/mix.json` Violins I, Violins II, Violas, Violoncellos, Double
  basses `sus_release_cap_ms` rows ["Sus MAX", "Sus Marc LITE"] -> ["Sus MAX", "Sus Marc LITE", "Leg Slur MAX",
  "Leg BC MAX", "Leg Port MAX", "Tremolo"] (150 ms, pp-ff). Dry run on the patches (`cap_release` logic): the legato /
  tremolo sustain groups shipped 316-931 ms (2nd Violins 323-931, Violas 323-931, Celli 237-931, Basses 316-931);
  TLeg transitions, RT trails and the 133 ms slur groups are untouched; no group mixes listed and unlisted rows.
  Opus state change: all five string tracks fully rebuilt.
- **C #5, re-bow holes:** `tools/fit_rebows.py 3 cycles/c03/rendered_build/parts.json --write` (build/rebow_fills.json
  was empty): 24 re-bows on 5 tracks fitted on the c03 stems (re-bow times unchanged in c04, checked).
- **A #3, wind staccato rows (MANUAL-GAPS #11):** `build/score_config.py` ART_SPANS "Stac DblTng RRx9" (key 28) with
  `"mark": "staccato"` over the whole piece on Flute 1, Flute 2, Oboe 1, Clarinet 1 (velocity map (58, 72), (72, 82),
  (88, 96), (114, 104), Bassoon 1's), Bassoon 1's span extended from 40-132 to the whole piece; STAC_LEAD_S 0.03 s on
  the four. parts.json: Fl1 45, Fl2 22, Ob1 38, Cl1 26, Bn1 55 notes on the row. New row on four tracks: Opus state
  change, fully rebuilt.

### Timing (S2)
- **A #1, wind legato targets at v60-v90:** `tools/score_to_parts.py` LEG_VEL_EXTRA_S accepts a list of
  (velocity at or below, extra s) pairs per key (generic; a tuple keeps the old meaning). `build/score_config.py`:
  Bassoon [(60, 0.16), (80, 0.09)], Oboe 1 [(60, 0.10), (80, 0.07)], Oboe 2 [(60, 0.12), (80, 0.11)], Cor anglais
  [(80, 0.05), (90, 0.08)], Flute 2 [(60, 0.10), (80, 0.06)], Flute 1 [(60, 0.07), (80, 0.03)], Clarinet 2 [(80, 0.02)],
  Clarinet 1 [(60, 0.0)], Bass clarinet (70, 0.09), wind (70, 0.04); LEG_SOFT_EXTRA_S Flute 1 (50, 0.06) -> (50, 0.03).
- **C #4, string legato leads:** `build/leg_leads.json` per-onset offsets for Violins I (101), Violins II (81), Violas
  (93), Violoncellos (124): 0.6 x the mean pcX error re +0.01 s where c02 and c03 agree (late > 40 ms, early > 60 ms),
  else 0.5 x the c03 error where late > 60 ms; clamped +-0.12 s. LEG_CAP_FRAC: a listed join may lead up to 0.9 of the
  previous note (entry `(0, SCORE_END, 0.9, "listed")` before the 0.75 default). Realised / requested lead change
  (median): Violins I +0.027 / +0.033 s, Violins II +0.000 / +0.026 (the 0.1 s LEG_MIN_GAP_S binds on 23), Violas
  -0.038 / -0.041, Violoncellos +0.034 / +0.047 s. `build/entry_leads.json` Violas 1048.0 +0.15 s.

### Balance (critic B, roles.json / mix.json)
- B #1 final chord: Violins II [1107.9, 1113.5] +5 -> +2; Horn 1 [1104, 1113.5, -3.5]; Trumpet 1 [1104, 1113.5, +3];
  Trumpets 2-3, Trombones 1-2 [1104, 1113.5, +1.5].
- B #2 Violins II doubling the tune: [48, 96, +3], [264, 328, +3], [744, 788, +3], [936, 968, +2.5]; Harp [264, 328]
  -4 -> -6.
- B #3 Trumpet 2 `dyn_trim_db` ff 10.0 -> 8.0; Trumpet 1 [840, 866, +1].
- B #4 soft accompaniments: Violins II [201, 264, -3] (pizz under the trumpet solo), Double basses [464, 488, -3],
  Clarinet 1 [481, 486, -4].
- B #5 inner voices: Clarinet 2 [200, 266, +5], [676, 744, +3]; Horn 2 [296, 310, +6, ramp 6].

### Movement I c45 values (coordinator, arrived before the build)
- **Re-bow fill ends (generic):** `tools/score_to_parts.py` REBOW_FILL_END_S 0.12 s ported from Movement I (a
  rebow_fills list ending on a non-zero value holds only to the end of its note; parts.json `rebow_fill_ends`). Check
  after the refit: 12 lists end on a non-zero value (-6.0..+3.7 dB), and every one is followed by the next re-bow of
  the same note, so none holds into a later note (`rebow_fill_ends` empty on every track).
- **Sus-gap repeats take the re-tongue lead (generic):** `rt_for` / `rep_sus_gap` ported (STR_REP_NEW_BOW "sus_min_s"
  repeats pass `retongue_ok` and take RETONGUE_LEAD_S, or `"sus_lead_s"`); `build/score_config.py`
  STR_REP_NEW_BOW["sus_lead_s"] 0.10 (the basses have no RETONGUE_LEAD_S). Newly led: Double basses 12 of 12 sus-gap
  repeats, Violins I 1 of 1 (Violas 1, Violoncellos 6 were already led or blocked by other rules).
- **Stereo width:** `tools/build_reaper.py apply_mix` reads mix.json `width_by_mic` (code from
  mockup-kit/pipeline/build_reaper.py). mix.json groups wind / horn / trumpet / lowbrass {"Main": 0.35}; Violoncellos,
  Double basses {"Main": 0.45}; Clarinet 1, Horn 1, Trumpet 1 {"Main": 0.2} (no widening past their track width).
  Side-only low cuts to 0 dB: the 200 Hz -2 lowshelf removed from Contrabassoon, Bass trombone, Tuba; Timpani 200 Hz
  -2 -> 0; Violoncellos / Double basses 170 Hz side bell -2 -> 0 (the 250 Hz +1.5 side high shelves and the harp's
  300 Hz -8 stay, as on Movement I). Opus state change on every wind, horn, trumpet and low-brass track and on the
  celli and basses.
- Hall unchanged (fx_volume 0.095, low_cut_hz 160, ir_setup); `rt_gain_db` not adopted (passed only on violas).

`score_to_parts.py`: 0 WARNING lines.

### Movement I correction (coordinator): rt_gain_db and the alias boost-span bug
- `rt_gain_db` is not adopted and not ported (Movement I's c45 pass-2 alias stems carried wrong CC data).
- This folder's `tools/score_to_parts.py` has the same espr./dolce boost-span code as Movement I (line 3155: for a
  track in TRACK_WINDOWS the boost stops at the window end or the next text, and the rest-based stops are dropped). It
  is inactive here: TRACK_WINDOWS, ALIAS_TRACKS and PASS2_TRACKS are empty and no parts.json track has "pass": 2, so no
  c04 data is affected. Whoever ports the "Horns a2" track (a TRACK_WINDOWS / alias track) must take Movement I's fix
  first and diff the alias's notes and CC lanes against its source track (cycles/c05/CARRYOVER.md).

## Rejected or deferred
- **A #2 / C #2, "Horns a2" track on 2FH:** deferred. The main project settled at 45 GB with 31 instances (budget about
  45), so no 32nd main instance; a pass-2 project is a larger setup (alias windows, level fit on its first render) and
  must first take Movement I's boost-span fix for alias windows (see the correction above). Open for c05.
- **C #3, `rt_gain_db`:** not adopted (coordinator: Movement I's result is invalid).
- **A #4, grace run into bar 35:** rejected as stated. parts.json (c03 and c04) has all three grace notes on both
  violin sections (sq 135.244 / 135.496 / 135.748, pitches 75 / 77 / 79). What is real: the violin run is led as a
  whole by its target's legato lead (Violins I starts at 134.768, Violins II 134.684, against Flute 1 135.160, i.e.
  0.14-0.17 s earlier than the winds). Open for c05 (cap the grace-group lead).
- **A #5, Clarinet 1 sub. p at 548:** rejected. parts.json `vol_db` is the pre-processing curve; `build_reaper.py`
  SUBITO_TAIL (Movement I c36) holds the level to the fall qn (547.902) and then falls 4 dB at once and the rest over
  0.35 s, so the post-hall step the critic read is not what REAPER plays. The stem dip there is mostly the 0.14 qn gap
  between the old note's end (547.762) and the moved sub. p onset.
- **C #4 part:** Double basses 900 (+170 ms, an ABUT_LEAD whole note) not changed (one note; ABUT_LEAD has no
  per-onset table). Raising the 0.75 cap was done only for listed joins (LEG_CAP_FRAC "listed"), not for every join.
- A #6 (soli DIV A, muted trumpet slur overlap): deferred, as in c03.

## Measured (c03 -> c04; `actor_scripts/m04.py`, `cycles/c03/actor_scripts/m03.py tails 4`)
- **String phrase ends, legato and tremolo rows (C #1; drop 0.15 s after the note-off, median):** Violins I Leg 10.8 ->
  15.4 dB (time to -20 dB 0.23 -> 0.17 s), Violins II Leg 5.5 -> 16.6 (0.43 -> 0.19 s), Violas Leg 9.1 -> 13.0 (0.35 ->
  0.24), Double basses Leg 5.1 -> 22.3; Tremolo ends Vln I 8.0 -> 10.7, Vln II 6.3 -> 18.5, Vla 3.3 -> 23.4, Vc -0.2 ->
  6.6, Cb 2.7 -> 19.2. No ending falls more than 10.2 dB in its first 0.05 s (Vla max 12.8 on one note). Sus MAX ends
  unchanged. **Celli legato ends unchanged** (10.5 -> 9.6 dB, 0.45 -> 0.50 s to -20 dB): the celli stay the slowest
  stem at every tutti cut-off (0.45-0.64 s); cause not found this cycle.
- **Legato joins (cap side effect):** broadband dip at the moved onset, median Violins I 5.9 -> 6.0, Violins II 4.9 ->
  4.8, Violas 4.2 -> 4.1, celli 4.0 -> 4.0 dB; joins >= 6 dB 104 -> 107, 66 -> 58, 39 -> 39, 56 -> 52. No new holes.
- **Hall (master):** final fermata drop at 0.15 / 0.3 / 0.6 / 1.0 s 12.1 / 18.5 / 31.3 / 36.7 -> 14.1 / 21.8 / 31.2 /
  37.0 dB; RT(-5..-25) 1.31 -> 1.17 s; late RT 1.98 -> 2.18 s. Tutti cut-offs qn 5 / 21 / 374 / 450 / 814 at 0.3 s:
  17.9 / 19.1 / 15.7 / 19.6 / 17.5 dB.
- **Re-bow dips (C #5; stem dip dB / time more than 6 dB down / master dip):** celli 172.6 / 178.95 / 185.3 / 192.3
  14.8 / 20.1 / 15.4 / 15.7 -> 8.8 / 10.0 / 10.7 / 9.7 dB (135-165 -> 20-85 ms), master 192.3 8.1 -> 5.9; basses
  170.9 / 181.7 / 190.55 / 560.0 / 567.0 14.6 / 9.1 / 13.6 / 10.5 / 6.5 -> 9.1 / 6.3 / 7.9 / 5.1 / 4.1. Worse: Violins I
  178.99 3.7 -> 14.6 (master 4.8 -> 4.6), Violins II 174.49 6.8 -> 12.4 (master 1.2 -> 1.8); Violins I 188.78 25.3 ->
  17.8. The fits clamped at +9/+10 dB on 8 of 24 re-bows: refit on c04 (refit mode reads the c04 shapes) in c05.
- **Wind legato timing (A #1, pcX median by velocity):** Bassoon 1 v80 +105 -> +55 ms, v60 +141 -> +86; Oboe 1 v80 +72
  -> +39, v60 +55 -> +42; Oboe 2 v80 +147 -> +59; Cor anglais v90 +91 -> +41, v80 +62 -> +12 (duet 680-740 median +46 ->
  +8, notes over +80 ms 8 -> 4); Flute 1 v80 +38 -> -1, v60 +49 -> +19; Flute 2 v80 +91 -> +63, v60 +86 -> +148 (n 3);
  Clarinet 2 v80 +42 -> +21. Bassoon solo 456-500 median +44 -> +51 ms, max +187 -> +144, over +80 ms 8 -> 6 (its v100
  notes are the remaining late ones: per-onset leads next). v100 medians unchanged.
- **String legato timing (C #4, pcX):** robust SD Violins I 84 -> 61 ms, Violins II 73 -> 50, Violas 70 -> 47, celli 64
  -> 43; joins more than 60 ms off the median 47 / 42 / 42 / 39 -> 22 / 22 / 19 / 19 %; listed joins' median |pc - 10 ms|
  85 / 93 / 93 / 92 -> 36 / 48 / 41 / 43 ms. The probe's Violins I join-spread flag cleared.
- **Wind staccato rows (A #3; harmonic-band peak after the score onset, median):** Flute 1 +135 -> +70 ms, Flute 2 +162
  -> +97, Oboe 1 +165 -> +57, Clarinet 1 +148 -> +85 (Bassoon 1 +80 -> +75); peak level c04 - c03 median -1.3 / -0.1 /
  +1.4 / -0.4 dB (p10 -6.4..-2.3, p90 +3.6..+6.6): no level refit needed.
- **Balance (re master, dB):** final chord 1108-1112 Violins II -9.2 -> -12.1, Horn 1 -8.9 -> -12.4, Trumpet 1 -15.0 ->
  -12.0, Trumpet 2 -14.3 -> -12.7 (trumpets now over the horn and Violins II); F2 264-328 Violins II -10.5 -> -7.6,
  harp -7.3 -> -9.3, Violins I -6.7 -> -6.8; M 744-788 Vln II -10.1 -> -7.4; F1 51-94 -11.3 -> -8.6; theme B 840-864
  Trumpet 1 -8.2 -> -7.2, Trumpet 2 -6.6 -> -8.1; pizz 201-264 Violins II -13.0 -> -16.1 (Trumpet 1 -3.0 -> -3.1);
  basses 464-488 -9.6 -> -11.6; Clarinet 1 481-486 -4.0 -> -6.8; Clarinet 2 200-264 -17.5 -> -12.5, 676-744 -16.5 ->
  -13.7; Horn 2 296-304 -22.2 -> -16.1. Stopped horns (now in REAPER): Horn 1 192-200 -8.9 (c03 after the stem fix)
  -> -11.1, Horn 2 668-676 -16.1 -> -16.1, Horn 3 / 4 548-552 -14.2 / -17.3 -> -13.9 / -17.1. Climaxes: 888-892
  -10.0 -> -9.9, 1108-1112 -10.5 -> -10.5 dB.
- **Master:** -16.1 LUFS, LRA 22.0 LU, float-sum peak 1.619 (+4.2 dBTP; the 24-bit file replaced by the float sum).
  Loudest bars 223 (-9.9), 278 (-10.5), 279, 263.
- **Delivered** `cycles/c04/mvt3-mockup-c04.mp3`: -19.8 LUFS, LRA 14.5 LU, TP -1.6 dBTP, limiter about 2.0 dB, p10-to-max
  span 18.9 dB.
- **Attack probe:** 0 late or holes (c03: 1, the Violins I join spread).
- No stem fix (every changed level landed within about 1.5 dB of the critics' predictions).

## REAPER
- Lock 16:19:39-16:47:35 (28 min). Waited behind mvt2 c40 (longest waiter, held 15:35-16:19); my waiter started 15:42
  with no other waiter.
- `start`, `open`, `build_reaper.py build/parts.json jobs --midi-only` in three batches with a save after each (27
  tracks fully rebuilt: every wind but the contrabassoon, all brass, all strings; Contrabassoon, Timpani, crash, bass
  drum and harp MIDI/envelope/EQ only), `restart` (31 tracks), Audio_Init (48000 / 512, no input), `render_cycle.py 4`,
  `quit`, `unlock`.
- REAPER memory: 45 GB settled before the render (0 compressed), 46 GB after it (26-28 GB compressed).
