# Cycle 1: changes (render of c01, reviewed by the critics of c02)

Inputs: critic reports A (articulation), B (balance), C (blend) on the c00 render. Snapshot of tools and data before the changes: `before/`. One render from a freshly restarted REAPER, then one level-only stem fix (kit LEARNINGS 15). The first render's files are kept in `render_first/`, its metrics in `metrics_first/` and its delivery in `render_first_delivery.mp3`; `render/`, `metrics/` and `mvt1-mockup-c01.mp3` are the fixed version, and the REAPER project matches it (updated with `--mix-only` and saved).

## Changes

Tools (generic rules, each with its default in the tool):

1. **Subito dynamics** (B #1), `tools/score_to_parts.py`. The event reader maps `sub. X` / `subito X` to `X` and records the position in `SUBITO`. Before this, `DYN` had no `sub. p` key, so all 13 subito marks were dropped: bar 62 played loud and bar 84 played ff. A subito mark is never a hairpin's target, so the bar-60/61 crescendo stays a crescendo into bar 62. Every positive dB gain (`hpgain`: hold, release, sostenuto share) ends at a softer subito mark.
2. **Gentle accents on woodwinds** (A #3), `GENTLE_ACCENT["wind"]` in the tool defaults:
   - Sus MAX / Sus Non Vib instead of Sus Accent MAX. No CC11 bump and no +10 velocity.
   - A volume swell of +3.5 dB at f and louder, +2.0 dB softer. The shape is (0.07, 0.25, 0.6) s.
   - `keep_legato`: an accent on a note joined inside its slur stays on the legato row and takes only the swell.
3. **Pickup into a long note** (A #1, a test), `SHORT_SUS_TO_LONG = 1.0`. When a slur's first note is shorter than 0.25 s and the next note in the slur is 1 qn or longer, the first note stays on Leg Slur MAX instead of the `short_sus` Sus MAX rule. The target note gets the normal legato lead. This changed 25 pickups: Vln I 11, Vln II 4, Vla 7, Vc 3.
4. **Percussion velocity floor**, `PERC_MAP` spec `vel_min` (B #4).
5. **Re-bow list in parts.json.** Each string track gets `rebows`: [qn, end of the split note, pitch].
6. **New tool `tools/fit_rebows.py`** (A #2). It fits `build/rebow_fills.json` from a render by the movement II c26 method:
   - It follows the pre-re-bow level, minus the plan's own change, over the first 1.5 s.
   - It then holds the offset to the next re-bow, clamped -6..+9 dB.
   - It returns to 0 at the end of the note.
7. **New tool `tools/stem_fix.py`.** It applies a level-only data change to rendered stems, using `build_reaper.vol_points()` of the old and new data, and rebuilds the master as the float stem sum.
8. **`tools/render_cycle.py --measure-only`** re-runs the measurement, the probe and the delivery on the files already rendered.

Config and data (`build/`):

9. `score_config.py`:
   - Suspended cymbal on key 64 (the f3 take) with `lead_s` 0.45 (A #4, B #4, C #2).
   - Tam-tam `vel_min` 60 (B #4).
   - Coda cello hairpin targets `HP_TARGET_AT["Vc"]` = {680 mf, 683.5 mp, 685 mp+, 691 mf, 692 mp}, with `DYN["mp+"] = 65` (B #3).
   - `NOTE_TRIM_RAMP_S` 0.3 s on the opening cello and bass pickup (B #5).
10. `roles.json`:
    - Timpani [0, 16, +12] and [300, 304, +8]. B #5 proposed +7 and +4; both were raised after the render.
    - Clarinet 1 [220, 244, +3, release 2] and Horn 2 [220, 244, +2, release 2] (B #6).
    - Cor anglais [683, 695, +2.5] (B #3).
11. `note_trims.json`: Violoncellos 3.0 -8 dB and Double basses 3.0 -6 dB (B #5).
12. `mix.json`:
    - Trumpets `dyn_trim_db` f/ff 0/0 -> 7/8, and Trumpet 3 -> 8/11 (B #2, C #1).
    - Trombone 1 3/4 -> 1/3, Trombone 2 6/8 -> 4/6, Horn 2 2/4 -> 1/1 (B #2).
    - Oboes 1/0 -> 2/4 (B #6).
    - Tam-tam gain -4 -> +1 (B #4, C #4). Suspended cymbal -6 -> -8.
    - Double basses: body bell 160 Hz +4.5 dB bw 1.4 -> 180 Hz +4 dB bw 1.0. `bell2` 80 Hz -6 dB bw 1.0 -> 100 Hz -5 dB bw 0.8.
    - `loud_eq` (160 Hz +4 dB, 1 oct) on the celli and basses over the c00 loud spans qn 94-104, 110-128, 318-332, 458-496, 518-536, 550-568, 626-646 and 662-680, with 2 qn ramps in and 1 qn ramps out (C #3).
    - Soft trims: global ppp/pp/p 3/3/3.5 -> 5/5/4.5 before the render, then 7/7/5 by the stem fix. Every per-track override moved by the same amounts (+4/+4/+1.5 in all).
13. `early_fills.json`: 84 fills from `tools/auto_fills.py 0` on the c00 render (A #6.1). The lead-line list is in the new `build/auto_fills.json` (Fl1, Ob1, CA, Cl1, BCl, Bn1, Hn1, Vc). Vc 311, 521 and 529 were excluded because the pickup rule changed those joins.
14. `rebow_fills.json`: 94 re-bows (Vln I 6, Vln II 13, Vla 16, Vc 29, Cb 30), fitted on c00 with `fit_rebows.py`. The re-bow points did not change between the c00 and c01 builds; this was checked.

The REAPER update was `build_reaper.py --midi-only` on 31 tracks; the crash track was unchanged. The 11 wind tracks were fully rebuilt, because unloading the unused Sus Accent rows changed their Opus state. The project was then saved, REAPER restarted, and the render made. After the render, the stem fix (soft trims +2/+2/+0.5 dB, timpani roles +12/+8) was applied with `stem_fix.py --apply`, written to REAPER with `--mix-only`, saved, and REAPER quit.

## Measured before (c00) / after (c01)

- **Subito p**:
  - Master bar 61 -> bar 62: c00 -28.9 -> -28.4 dB (no drop); c01 -26.9 -> -30.6 dB (-3.7).
  - Celli bar 84: -23.7 -> -33.0 dB. Harp bar 62: -35.6 -> -40.2 dB.
- **Suspended cymbal**: the peak came 0.86 s after the roll's start, 1.12 s before the crash, and the roll was 16 dB down at the crash (c00). In c01 the key 64 take peaks 2.40 s after its start, 0.03 s before the crash. The 4-12 kHz peak is 1.3 dB under the crash.
- **Brass**, per-dynamic stem medians, Trumpet 1 against Trombone 1 and Horn 1:
  - f: c00 -42.2 / -29.9 / -36.5 -> c01 -35.2 / -32.0 / -36.5.
  - ff: c00 -37.5 / -27.6 / -31.0 -> c01 -29.5 / -28.9 / -31.0.
  - fff: Trumpet 1 -26.6 against Trombone 1 -26.3.
  - Bars 158-161, A-weighted: Tpt1 31.8 -> 39.8 and Tpt3 25.6 -> 36.6, against Tbn1 40.4 -> 39.4.
  - Horn 2 ff -28.2 -> -31.2, level with Horns 1, 3 and 4 (-31).
  - Bars 167-170: Tpt1 is now 4 dB over Tbn1 and 5 dB over Violins I. Check this against the score.
- **Oboe 1 f -> ff**: c00 -40.4 -> -40.6 (no growth); c01 -39.2 -> -36.5 (+2.7).
- **Woodwind accents**, 10 ms peak in the first 120 ms minus the body, median (p90):

  | Track | c00 | c01 |
  |---|---|---|
  | Flute 1 | +7.6 (+11.2) | +3.4 (+6.9) |
  | Flute 2 | +7.4 | +2.1 |
  | Oboe 1 | +4.2 | +1.0 |
  | Clarinet 1 | +4.3 (+12.4) | +3.1 (+7.6) |
  | Bassoon 1 | +4.7 | +1.9 |
  | Bassoon 2 | +4.9 | +3.1 |
  | Contrabassoon | +4.4 | +3.2 |

- **Pickup rule** (25 changed pickups): target body minus pickup body, median -2.3 -> +1.2 dB. At least +1 dB in 7 -> 14 of 25. No new dips after the target onset (median 2.6 -> 2.9 dB, none of 6 dB or more).
  - A's 12 listed onsets: median -5.7 -> -3.1. Vln II 110, 278 and 282 are not slurred pickups: the accent at 110 follows a two-note slur and is unslurred. The rule does not touch them, and they stay 5-9 dB under their eighths (open).
- **Re-bows**, 80 ms envelope, dip under the pre level / step after 1-2 s:

  | Section | c00 dip | c01 dip | c00 steps of 3 dB or more | c01 steps of 3 dB or more |
  |---|---|---|---|---|
  | Celli | 7.6 | 6.3 | 15/29 | 6/29 |
  | Violins II | 6.7 | 5.9 | 4/13 (median -0.1) | 6/13 (median -2.7, overcorrected) |
  | Basses | 4.1 | 3.3 | 15/30 | 9/30 |
  | Violas | 5.2 | 5.6 | 6/16 | 5/16 |
  | Violins I | 5.3 | 8.1 | 2/6 | 2/6 |

  - The stems reproduce at the re-bows: c01 minus the planned fill minus c00 is 2.0 dB everywhere, which is the soft-trim change. The fit's 0.12 s smoothing leaves the narrow part of each dip.
- **Legato join dips** (`auto_fills.py` measure): 84 lead-line joins dipped 5 dB or more on c00 (4 dB or more for flute, oboe and cor anglais). On c01, 13 still do, and 13 fills overshoot the body by more than 2 dB.
- **Opening**:
  - Timpani solo roll -57.7 -> -45.7 dB.
  - Bars 1-4: roll against the basses -13.6 -> -4.1 dB.
  - Bar 76: against the violas -7.9 -> -3.8 dB.
  - The cello pickup is now 1.4 dB under the following note; in c00 it was 5.6 dB over it.
- **Coda cello solo**:
  - Bars 172-174: -37.3 / -35.5 / -37.8 -> -36.8 / -38.8 / -40.5 dB.
  - Bar 171 is still -30.8.
  - The cor anglais is 4.1 dB under the cellos; it was 9.5 dB under.
- **Tam-tam**:
  - fff, first second, A-weighted: 13 -> 9 dB under the master; 4-12 kHz: 13.5 -> 9 dB under.
  - pp stroke at qn 696: +9 dB on the stem, but still about 20 dB under the master.
- **Low end**, loudest 10% of frames, third-octaves relative to 500 Hz-2 kHz:
  - 100 Hz -11.8 -> -12.6 (target about -15).
  - 125 / 160 / 200 Hz: -17.0 / -16.8 / -11.3 -> -16.3 / -16.0 / -9.8.
  - 63 Hz -27.6 -> -25.3.
- **Delivery**:

  | | c00 | c01 render | c01 after stem fix |
  |---|---|---|---|
  | Master integrated | -17.6 LUFS | -17.3 LUFS | -17.4 LUFS |
  | Master LRA | 23.1 LU | 21.9 LU | 21.1 LU |
  | Delivered LRA | 17.3 LU | 17.0 LU | 16.0 LU |
  | p10-to-max span | 21.7 dB | 21.3 dB | 20.4 dB (target 16-19) |
  | Limiter | 1.3 dB | 1.8 dB | 1.9 dB |

  - Master true peak +1.4 dBFS as a float stem sum (sample peak 1.177); the 24-bit render clipped and was replaced, as in c00. Delivered -19.8 LUFS, -1.5 dBTP.
  - The top master peaks are qn 484 (fff tutti: Vln II, Vln I, bass trombone, tam-tam), 377.7 s and 354.6 s (the crash).
  - Raising the ride cap from 10 to 12 dB (simulated) changed the delivered LRA by only 0.1-0.2 LU.
- **Motion** (mp3, dS4 p90 / 1 s-20 s): 9.55 / 5.00 -> 8.93 / 4.71. The fall comes from narrowing the delivered range, which the brief asks for; the first render had 9.43 / 4.90.
- **Attack probe**: 3 of 12 flagged; all are probe artefacts or repeat c00 exactly.
  - Tbn1 qn 100 +0.14 s, Vln II qn 20 +0.34 s and Vc qn 20 +0.63 s are identical to c00 to 0.01 s, so they are sample attack, not engine lateness.
  - Vln I qn 56.5 read +1.19 s on the first render. Its first sound is at the same frame as in c00 (-0.13 s), and the probe's peak - 20 dB threshold moved to a later, louder note.
  - Opening -43.9 dB, passes.
- **Memory**: REAPER settled at 19 GB after the open and grew to 41-42 GB while it streamed. 14-25 GB was compressed by the time of the render (the Mac had about 0.1 GB free; the page cache was full of streamed samples). After the render: 42 GB, 24 GB compressed. Timing was intact (see the probe).

## Rejected or deferred

- **A #5** (a2 horns on 2FH, Violins II metà on DIV B, 2TB/2TP): deferred. Each is a new Opus instance plus routing; this cycle already rendered with 24 GB compressed. Give it a cycle of its own.
- **A #6.2** (woodwind staccato on Stac DblTng): deferred. It loads new rows (a full rebuild of five tracks), and the velocity-to-level response is unmeasured.
- **A #6.3** (harp étouffez): deferred. The tail hold in `build_reaper.vol_points` holds the envelope through rests, so a damping cut at the étouffez would be undone; it needs an exception. The effect is mostly masked (inferred).
- **A #6.4** (breath before the climax): left, as A suggested (a 2 dB dip).
- **B #6** harp role in bars 56-61: not made. B asked to re-measure after the subito fix.
- **C #4** crash patch swap: deferred. B measured the crash level as right; C's case for a longer ring is inferred. Measure 4-12 kHz 2 s after the hit first.
- **C #5** percussion seating: not made. Nothing was measured wrong, and the seats are in the Opus state (full rebuilds).
- **A #1** fallback (accent target on Sus MAX with a swell): not needed. The legato pickup rule passed on the changed set.

## Open for c02

- Run `auto_fills.py 1` (29 entries planned: 6 new, 7 raised, 16 lowered or removed).
- Refit the re-bows with less smoothing, adding the residual: celli dips about 6 dB; Violins II steps overcorrected to -2.7 dB.
- Delivered p10 span 20.4 dB, above the 16-19 dB target. The quietest 10% is the intro (bars 1-5, 14), bars 34, 85-88, 107-109, 127-128 and the final chord with its tail.
- Tam-tam pp stroke about 20 dB under the master.
- Celli coda bar 171 at -30.8 dB.
- Trumpets 4-5 dB over Trombone 1 in bars 140-143 and 167-170: check against the score.
- 100 Hz in the loud frames 2.4 dB over movement II.
- The three repeating probe items are soft string entries and the Sus MAX trombone accent. Fix them with entry leads plus fills (kit LEARNINGS 6), or move the probe limits.
