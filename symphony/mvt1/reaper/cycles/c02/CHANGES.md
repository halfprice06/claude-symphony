# Cycle 2: changes (render of c02, reviewed by the critics of c03)

Inputs: critic reports A (articulation), B (balance), C (dynamics) on the c01 render. Snapshot before the changes: `before/`. One render from a freshly restarted REAPER (`--midi-only` on 29 tracks, no Opus state changed, so no patch reloads), then one level-only stem fix (the loop profiles, below). The first render's files are in `render_first/`, `metrics_first/` and `render_first_delivery.mp3`; `render/`, `metrics/` and `mvt1-mockup-c02.mp3` are the fixed version, and the REAPER project matches it (Timpani and Horn 4 updated with `--mix-only`, saved).

## Changes

Tools (`tools/score_to_parts.py`, generic, each with its default there):

1. **fff hold** (C #1a), `FFF_HOLD_CAP = 8.0`: a crescendo arriving at fff holds its whole hpgain to the track's next printed mark or hairpin (at most 8 qn), then releases over `HP_REL`. Before, the gain fell one beat after the arrival.
2. **fff chain rise** (C #1b), `HP_CHAIN_RISE_FFF = {wind 0.75, string 1.0, brass 0.5}`: a chained crescendo that arrives at fff adds this share of `HP_GAIN_DB`. Bar 160: strings +3 -> +6 dB, brass +2 -> +3. The other chains keep `HP_CHAIN_RISE`.
3. **Look-ahead stops at a softer or subito mark** (C #3), `NM2_STOP_SOFT`. Bars 60-61 Violins I/II and Horn 2 / Bassoon 2: the crescendo now reaches CC 86 (was capped at 80 by the f four bars after the sub. p). Only these four tracks changed.
4. **Accent on a crescendo arrival** (C #2), `ACCENT_MINUS_HPGAIN`: the gentle swell adds only max(0, swell - hpgain) on a note within 0.3 qn of a crescendo's end. Bar 170 winds: +7.5 -> +4 dB at qn 676.3. Applied on 57 track-onsets (`accent_on_arrival` in parts.json).
5. **Detached hammer strokes** (A #1), `DETACH_ACCENTS = {gap_qn 0.25, min_len_qn 1, max_len_qn 2}`: an unslurred accent followed with no rest by another unslurred accent ends 0.25 qn early; strings need a down-bow on both and play both on Sus MAX (no Leg BC join, no legato lead). A's `frac` form (0.75 x length) cut the bars 23-25 and 134-137 three-beat syncopated wind accents by 0.75 qn, so notes over 2 qn are excluded. Hits: bars 32, 72 (all sections), 142 (Fl/Ob/Cl, violins), 84 notes in all (`detached_accents`).
6. **String accent after Sus eighths** (A #2), `STR_ACC_AFTER_SUS`: an unslurred, monophonic accented string note abutting a Sus MAX / Stac / Tremolo note plays Sus MAX (`acc_sus` list: Vln I 8, Vln II 5, Vla 3, Vc 2), except when a same-pitch repeat follows (Vla 536 stays merged on Leg Slur).
7. **Gentle string accents** (A #2), `GENTLE_ACCENT["string"]` (db 3.0, soft 2.0, swell 0.07/0.25/0.6 s): no +8 CC11 bump, no +10 velocity.
8. A note with listed `REBOW_AT` points now gets the automatic path's keyswitch back (it raised an error before).
9. Re-bow fill lists run to the next list's first point (fills may now start before their re-bow).

Other tools:

10. `tools/fit_rebows.py` (A #6, C #4): refits on a render that already carries shapes: the old shapes are taken out of plan and stem, and each piece's target is the level before the note's first re-bow (the c01 fit chained each piece to the previous piece's unfilled level). Fill starts 0.12 s before the re-bow; first 0.4 s may reach +10 dB; `--hold-max-after 720:0` caps the final-chord holds at 0 dB. A's 0.04 s smoothing was tried and rejected: the stems swing +-6 dB at about 3 Hz inside held notes, and the fit followed it (+12 / -5 / +9 dB within 0.8 s). Refit on c01 and written.
11. New `tools/fit_loops.py` (A #4, C #4): periodic inverse loop profiles from a render. See the stem fix below.
12. `tools/build_reaper.py` `vol_points`: optional "mp" (CC 58) and "mf" (CC 72) anchors in `soft_trim_db` (B #5).
13. `tools/deliver_master.py`: ride `RATIO` 2.0 -> 2.5 (C #5).

Config and data (`build/`):

14. `score_config.py`: `TIMP_TIE_STROKES = [46, 460, 561, 641]` (A #3); `REBOW_AT["Violoncellos"] = [289.145, 293.758, 298.37]` (the c01 points, so their fitted shapes stay valid after the bar-72 detach moved that note's start).
15. `roles.json` (B #1, #2, #3, #6; C #5, #6): brass cuts under the ff/fff melody (Tbn1 [464,480,-5] [628,644,-3]; Tbn2 [628,644,-3]; BTbn [464,480,-3] [520,536,-6] [628,644,-3]; Tuba [520,536,-3] [628,644,-2]; Tpt1-3 [556,568,-3]; Tpt3 [628,644,-3]); melody +1.5 at [628,644] on Vln I/II, Fl1/2, Hn1, Tpt1; Vln I/II [520,536,-2]; Vc [56,72,-5] [104,128,-3]; Vln I [56,72,+2] [664,676,-3]; Vln II [440,464,-4] [664,680,-4] [676,680,-3]; Vla [664,680,+3]; Hn1 [664,680,+2]; Harp [232,268,-3, opens over 2]; Vln I/II [484,496,-4] (B asked -5); Tam-tam [696,712,+8]; Timpani [720,728,+4]; fugato Vc/Cb [336,358,+3], Vla/Bn1 [348,358,+3]; Vc [690.5,694,+2, opens over 2].
16. `pitch_trims.json` (B #4): Vc 43 -5, 51 -4 (all arts, skip qn 3); Tpt1 77 -6 (all arts); Cl1 79 -6, 80 -3, 68 +5 (all arts; B asked +6, kit LEARNINGS 13 says +6 was too much at ff); Fl1 91 -5 (all arts), 74 +4; Hn1 72 -5 (all arts); Ob1 76 -5, 72 +3; Bn1 61 -5, 54 -5.
17. `note_trims.json`: Vc 680 -6 (C #6).
18. `mix.json`: Flute 1/2 `soft_trim_db` {ppp 7, pp 7, p 5, mf 2.5} (B #5).
19. `early_fills.json`: `auto_fills.py 1` pass (29 entries: 6 new, 7 raised, 16 lowered or removed).
20. `rebow_fills.json`: refit on c01 (item 10). `loop_profiles.json`: fitted, rendered, removed (below).

Simulated before the render (`stem_fix.py` on the c01 stems, level changes only): delivered LRA 15.3 LU, span 19.8 dB, limiter 1.8 dB, bar 160-161 max S -9.7/-9.6, bar 122 -11.0, bar 169-170 -12.0. The render measured 15.2 / 19.9 / 1.9 and -9.5 / -10.9 / -12.0.

## Stem fix: loop profiles removed

The profiles (Timpani 0, 48, 464, 484, 720; Horn 4 720; periods 3.3-3.9 s, +-3 dB) made the pulse worse: timpani opening folded swing 3.5 -> 4.7 dB, Horn 4 4.6 -> 6.2. Comparing c02 - c01 stem level with the planned envelope change, the change appeared 0.09-0.25 s **before** its planned time (best-lag correlation 0.97-0.99, against -0.1..0.4 at zero lag); the same lead showed on roles (Tbn1, Harp: 0.11-0.12 s), the bar-170 accent swells (Fl1, Cl1: 0.09 s) and the re-bow shapes (Vc, Cb: 0.22-0.24 s). Note onsets are on time (attack probe). Dividing the profile out of the c02 stems at the measured lead brought the swings back to c01 (Timpani 0: 3.6, 484: 2.8; Horn 4: 5.8). The profiles were removed from `loop_profiles.json`, parts.json rebuilt (only Timpani and Horn 4 changed), the master rebuilt as the stem sum, `render_cycle.py 2 --measure-only` re-run, and REAPER updated with `--mix-only` and saved. The cause of the lead is not found (it is not in `vol_points`: the REAPER envelope points equal parts.json vol_db + gain + trims at the same qn). It matters for every fast envelope shape (fills, notches, accent swells, re-bow shapes): they land about 0.1-0.25 s early.

## Measured before (c01) / after (c02)

- **Delivery**: master -17.4 -> -17.5 LUFS, LRA 21.1 -> 21.0 LU, sample peak 1.177 -> 1.220 (float stem sum; the 24-bit render clipped and was replaced). Delivered -19.8 -> -19.7 LUFS, LRA 16.0 -> 15.2 LU, p10 span 20.4 -> 19.9 dB, limiter 1.9 -> 1.9 dB, -1.5 dBTP. Motion (mp3 dS4 p90 / 1s-20s) 8.93/4.71 -> 8.70/4.56.
- **Climax order** (delivered max short-term LUFS): bar 122 -9.9 -> -10.9, bar 123 -10.2 -> -10.9, bar 159 -11.3 -> -10.2, bar 160 -11.3 -> -9.5, bar 161 -12.3 -> -9.5, bars 167-170 -11.5 -> -12.0. Bar 160 is now the loudest and holds through 161. Master per 2 qn, qn 636-644: -12.7 / -14.2 / -13.8 / -15.6 -> -11.2 / -11.9 / -11.3 / -12.4. Top master peaks now qn 637.8 (1.22), 641.0, 636.1 (were 485.4, 676.2).
- **Detached strokes** (master break, lower body minus the minimum within +-0.15 s): qn 125 1.7 -> 4.3, 285 3.1 -> 5.8, 286 -0.2 -> 0.3, 565 0.7 -> 1.2, 566 -0.4 -> -0.1 dB. A's 6 dB criterion is not met: bar 142 and the third bar-72 stroke are covered by the held harmony in other sections.
- **String accents after Sus** (body 0.15-0.5 s minus the note before, stem): Vln I 62/82/110/142/154/378/558: -0.3/-3.1/-4.8/-2.5/-3.6/-3.4/-1.9 -> +1.7/+1.1/+1.8/-0.5/+4.0/+2.1/+2.0; Vln II 110/278/282/366/558: -9.4/-8.7/-6.4/-2.2/-6.6 -> -1.2/-1.1/+0.1/+4.9/+2.7; Vla 110/354/670: -5.9/-1.9/-4.8 -> +5.3/+2.3/+4.9. Vln I 128 (an eighth) -5.7 -> -4.3. 2-5 kHz attack minus body not measured this cycle.
- **Timpani tie strokes** (30 ms peak minus the roll's last half beat): 46 1.5 -> -3.5 (no stroke heard: open), 460 0.2 -> 2.1, 561 2.1 -> 3.0, 641 1.1 -> 4.2 dB.
- **Soft end**: tam-tam pp first beat -15.4 -> -12.6 dB under the master (qn 700-708 -16.0 -> -15.7); final timpani roll -8.2 -> -2.9 dB against the basses.
- **Bars 60-61**: Vln I hairpin last third minus first third -5.5 -> -5.2 dB, master -1.3 -> -1.0, drop into bar 62 -3.7 -> -3.3. C #3 changed the CC11 (80 -> 86) but not the result: the line's descent dominates. Open.
- **Coda cello** (per qn 680-695): first note -31.7 -> -37.1, the bar-174 crest (692) -39.6 -> -38.2; the phrase is now flat instead of falling 10 dB, the crest still not on top.
- **Final chord** (last 1.75 qn minus qn 724-725.75, stem): Vln I +3.6 -> +2.4, Vln II +1.1 -> -1.0, Vla +1.2 -> +0.3, Vc +2.2 -> +1.5, Cb +3.8 -> +4.3. The master still rises about 1.5 dB at qn 726.
- **Re-bows** (80 ms window, dip under the 0.5 s before / step 1-2 s after): median dip Vln I 6.7 -> 8.1, Vln II 5.8 -> 4.5, Vla 4.5 -> 4.4, Vc 5.5 -> 5.1, Cb 3.0 -> 2.8 dB; steps of 3 dB or more Vln II 4 -> 2, Vla 5 -> 4, Vc 3 -> 8, Cb 6 -> 12. Mixed; with the envelope lead above, the shapes land early.
- **Attack probe**: 4 flagged, all artefacts. Tbn1 qn 100 +0.14 s: stem identical to c01 frame for frame. Vln I 56.5 +0.54 s: same envelope shape as c01, 2 dB higher (the +2 role). Vln II 20 and Vc 20 identical to c01.
- **Memory**: REAPER 18 GB at the open, 41 GB after the render, 18 GB compressed (0.0 before).

## Rejected or deferred

- A #5 (wind staccato on Stac DblTng RRx9): deferred again. It loads a row on five tracks (full rebuilds) and its velocity-to-level response is unmeasured; it needs its own test with a control passage.
- A #6 re-bow lead 0.10 s: deferred (it moves every re-bow's attack, so all shapes would need a refit after a render); the refit alone was done. 0.04 s smoothing rejected (above).
- C #4 explicit `REBOW_AT` for the final chord (spacing 0.6 s, none after qn 726): not done. The last piece would be 5-7 s on one sample (loop pulse) or the re-bows bunch again; the hold cap was done instead. The 0.11-0.34 s clusters at 722.6, 724.8 and 726.4 remain.
- B #3 "+1 dB on all tracks at bar 160": not needed (bar 160 is now 1.4 LU over bar 122).
- B #4 Clarinet 2 copies of the Clarinet 1 trims: not done (too few long notes to measure).
- The `mf - 2.5` threshold for an untargeted mf crescendo's gain was tried and reverted: it also raised five other hairpins (winds 2 -> 4 dB at qn 154-160).

## Open for c03

- The envelope lead (0.1-0.25 s) against the plan: find the cause (REAPER PDC with Opus latency? the measurement?) before fitting more fast shapes; check whether the c01 auto fills and re-bow shapes also land early.
- Timpani roll loop pulse (opening 3.6 dB folded) and Horn 4's final note (5.8 dB): refit with the lead accounted for, or re-strike the rolls.
- Timpani tie stroke at qn 46 inaudible.
- Bars 60-61 crescendo still measures backwards on Violins I.
- Vla 536 accent (merged legato note) still under its eighths.
- Detach breaks under 6 dB at bar 142 and the third bar-72 stroke.
- Re-bow steps (Vc, Cb) and the final-chord swell (Cb +4.3 dB).
- 2-5 kHz attack minus body for the new string accent swells.
