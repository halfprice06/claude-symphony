# Cycle 40: changes (actor; ONE_TIME "too wet, mushy" from Movement I c44, plus critics A/B/C on the c39 render)

Snapshot before the changes: `before/`. Data the render was made from: `rendered_build/` (parts.json, mix.json, score_config.py, the per-note tables, build_reaper.py). The final data (after the stem fix) is in `build/`. Scripts: `actor_scripts/` (capcheck, strokecheck, envdiff, reps40, ends40, rbdips, qnlev, check40, restore_cl2; hall measures with `cycles/c38/actor_scripts/hall38.py`, results `hall_c39.json` / `hall_c40.json`).

Every Opus state changed (the hall's IR envelope is in each patch, release caps on 14 tracks), so all 32 tracks were fully rebuilt in one build.

## ONE_TIME (done; appended to `loop/ONE_TIME.done.md`)

1. **Shorter hall tail.** `build/mix.json` `reverb.ir_setup` = {envelopeMode 2, endPos 0.7, decayLength 0.7} (the coordinator's value). `tools/build_reaper.py` `apply_mix` got the kit's irSetup block (a track's `reverb_ir_setup` overrides it; unknown keys stop the build). Sends, IR, wet, high cut, true stereo, fx_volume 0.095 and the 160 Hz low cut are unchanged.
   - Final chord (qn 304), master drop at +0.3 / +0.6 / +1.0 s: c39 8.4 / 17.3 / 35.9 -> c40 21.4 / 30.7 / 42.5 dB. Level against time after the cutoff (c40): -19.7 dB at 0.2 s (the capped string releases), a hall plateau of -24..-31 dB from 0.4 to 0.8 s, -46 at 1.0 s, -62 at 1.4 s, the noise floor (-79) from 2.0 s. The decay of the hall alone from 0.4 to 1.4 s is about 37 dB/s (RT60 about 1.6 s), inside the 1.1-1.6 s of the recordings. hall38's "late RT60" fit (-20..-40 dB) now reads 3.12 s; that fit spans the plateau and is no longer a valid measure here. The morendo does not end in a dry room (the plateau carries the chord for 0.8 s). Keep 0.7; do not go to 0.5.
2. **Release caps** (`sus_release_cap_ms`, `cap_release` was already in tools/). Row names checked against the patches (`actor_scripts/capcheck.py`, a dry run of cap_release on each patch):
   - Strings, 150 ms on pp/p/mf/f/ff, rows Sus MAX, Sus Marc LITE, Leg Slur MAX, Leg BC MAX, Leg Port MAX, Flautando (rows a patch lacks are ignored): Violins I, Violins II, Violas, Violoncellos, Double basses, and by name Violin I solo, Violoncellos div, Violins II div, Violas div. Groups hit ship 237-931 ms. Tremolo, Pizz and Detache rows are not capped.
   - Horns 1-4 and Horns 1-2 a2, 237 ms on pp/mf/f, rows Sus MAX, LegRep RRx4, Leg Slur MAX (ship 316-562 ms).
   - Measured (`ends40.py`, phrase ends with at least 0.6 s of silence, median drop at +0.05 / +0.15 / +0.3 s): strings 1.7 / 6.9 / 12.6 -> 3.7 / 12.7 / 19.5 dB (C's target: at least 9 at +0.15); horns 2.6 / 7.1 / 17.4 -> 3.1 / 10.9 / 20.4; winds unchanged (3.2 / 11.8 / 19.0). hall38 stem cutoffs at +0.3 s: strings 13.0 -> 20.5, horns 17.7 -> 19.2.
   - Legato joins (hall38): string median dip 2.4 -> 2.7 dB (within the 1 dB limit, so 150 ms stays on the legato rows); per track Violins I 3.1 -> 3.3, Violins II 2.2 -> 2.2, violas 2.3 -> 2.25, celli 2.5 -> 2.5, basses 2.25 -> 4.1 (Sus MAX to Sus MAX steps: the joins now separate), horns 1.25 -> 1.2.
   - Endings falling over 10 dB in their first 0.05 s: Flute 1 271 (12.6, as c39), Violoncellos 87 (12.1, c39 10.7), Violins I 7.35 (10.4, the opening chord's last re-bow piece). No others.
   - Re-bow fills refitted (below).
3. **STR_REP_NEW_BOW** ported from Movement I (c44 classification, merge, note-length, lead and output changes; c45's `sus_lead_s` and the lead for "sus_min_s" repeats). Settings in `build/score_config.py` (block "c40"): gap 0.06 s / 25 %, stroke_cc mf, stroke_mark mp, head_cc p, sus_min_s 0.4, sus_lead_s 0.10, portato {0.05 s, 25 %, fall 6/8 CC, 0.04 s}, and the new `sus_cc_by` {"Double basses": pp}.
   - Result: strokes Violins II 45, Violas 82 / 253, celli 128 / 148, Violas div 82; portato Violins II 44 / 50; soft re-bows Violins II 51 / 144 / 289 / 292, violas 50 / 62 / 69 / 71 / 87 / 248.5 / 271 / 283, Violas div 70 / 289; sus gaps on the basses 144 / 156 / 168 / 253 / 265 and Violas 82.
   - Movement II needed three tool changes beyond the port (comments "mvt2 c40" in `tools/score_to_parts.py`): (a) a stroke joins the next note of its own slur as a legato target also when it carries a tenuto (Violins II's louré slur heads 45 / 51 were caught by the tenuto branch, leaving 47 / 53 unled on the first-note layer); (b) strokes and sus-gap repeats take their lead at any tempo (the entry leads' mid-tempo gate, 100 bpm, left every one unled in this Adagio; now 0.08-0.10 s); (c) `sus_cc_by`.
   - Reconciled with the old rules: c39's notches out (MERGE_NOTCH_AT Violins II 292, violas 62, Violas div 70), Violins II 289 / 292 in NOTCH_SKIP, listed points Violins II 290.9 / 293.0 / 45 / 51 and Violas div 287.3 / 288.6 out (Violas div keeps 291.7 as the loop point of its 6.3 qn 289 piece; its 292 is not a printed repeat), basses 144-265 out of REP_RETONGUE_AT and their c39 CC7 falls removed. 19 orphaned rebow_fills rows removed (kept in `actor_scripts/removed_rebow_fills.json`); Cb 166.034 move dropped and the fill 170.048 re-keyed to 170.003 (the lead moved the automatic point). space_rebows.py was run without --write (clashes left: printed coincidences at 120 / 223 / 289 and Violas div 291.7 against Violins II's printed 292, 0.35 s).
   - S1 (`reps40.py`, broadband 50 ms, dip / re-attack, the 36 flagged or new repeats): stem dip median 2.7 -> 6.9 dB, master 2.0 -> 2.9. Strokes 6.5-16 dB in the stem; soft re-bows mostly 2-7 dB after the refit (Violas 69 12.5 and 248.5 11.5, short pieces the fit skips; Violas 87 / 271 1.7). Basses 156 / 168 / 253 now 8-10.5 dB (c39 -1.8..2.5). Horn 2 208 re-tongue: no change (2.3 -> 2.4).

## Critic findings

Accepted:
- A #1 bar 25: new generic `BC_NEWP_KEEP` ({"Violins I": [72.0]}); Violins I's C5 is a Leg BC MAX target with the normal leg lead and v124; c35's re-attack lead and the c30 join notch removed. Own-pitch C5 now at body level by 0 to +0.12 s (c39: +0.18 to +0.36 s), level with Violins II.
- A #2 (with ONE_TIME #3), plus `DOWNBOW_STROKE_AT` basses 144 and celli 66 (the bar 23 counter-melody head).
- A #3 Violins II sul tasto: REBOW_AT Violins II div 114 / 116 / 119 / 120 and Violins II 112 / 120 (Flautando re-bows on the printed bows); automatic points removed; `AUTO_REBOW_SKIP["Violins II div"] = [108.0]`. Stem dips at the printed bows 2.1-7.0 dB after the refit (Violins II 112 13.8: the fit clamps that piece).
- A #4 Trombone 1 214.5 +4 -> +2.5, 215 +1.5 -> +2.5. Per 0.125 qn 214.5-215.5: c39 -22.4 -20.3 -20.2 -25.3 -24.2 -23.4 -22.8 ... -> c40 -23.9 -21.8 -21.7 -26.0 -23.2 -22.5 -21.8. 215 is now 1.5 dB under the head (was 4), but the transition at 214.875 still dips 4.3 dB (open).
- A #5 Horn 2 208 re-tongued: no measured effect (masked by the ff tutti).
- B #1 Horn 1 / Horn 3 loud_eq 300 Hz bell -2 dB (not -3: set before the new hall could be measured), Horn 1 soft trims +1 (pp 5.0, p 5.5, mp 3.8); bass clarinet soft-span highshelf 1.2 kHz -3 over qn 0-42. Bars 7-14: Horn 1 over the rest at 1-2 kHz +0.4 -> +2.6, at 2-4 kHz -6.0 -> -2.2; Horn 1 bar levels within 0.5 dB of c39; master 200-500 Hz re 630-1600 Hz bars 1-6 / 7-14 / 65-70: 7.0 / 8.1 / 10.7 -> 6.5 / 7.4 / 10.0.
- B #3 Trombone 2 CC7 95 over its 208 note: Violins I over Trombone 2 per 0.5 qn 208-210: 0.2 / 0.6 / -1.6 / -1.9 -> 2.4 / 3.1 / 0.9 / 0.6.
- B #4 Horn 4 CC7 90 from 280: Horn 4 minus Horn 3 per qn 286-294 +4.0..-0.8 -> +1.9..-3.8; Clarinet 1 over Horn 4 bars 87 / 88 2.3 / 4.3 -> 5.2 / 7.1 (target 5.5-7.5).
- C #1 legato-row and divisi caps (ONE_TIME #2). C #4 endPos 0.7.
- C #3 after the render: Clarinet 2's opening E flat 3 (6.0, 15.0) note trims +3 -> +9 (per 3 qn 6-18: c39 -52.7 / -51.9 / -45.7 / -52.5, c40 -47.2 / -46.1 / -45.6 / -47.3, back level with c37); Violoncellos and Double basses gain_db +1.5. Master 100-250 Hz share -9.2 -> -8.3 dB (aim about -8.5).
- B #6 checks: climax order holds (master bars 61 / 62 / 79 / 80: -11.0 / -11.7 / -17.0 / -17.9 dB); Vln I over Vln II at 262-265.75 +0.1..+3.9 (c39 -0.2..+4.0; the Vln II CC7 kept); solo margins unchanged within 0.5 dB.

Rejected or deferred:
- B #2 basses loud bell 78 Hz instead of the series 1 "climax shelf -3": not taken (no measured reason recorded yet; the limiter is at 2.4 of 3 dB). Open for c41 with B's numbers.
- B #5 Violoncellos div CC7 -2.5 in the coda: not needed; timpani over the pedal at 277-280 1.2 -> 2.1 dB after the caps and refit (target 1.5).
- C #2 BOW_CHANGE_DIP (slur-start CC7 dips): deferred; this cycle already changed every string join's release, measure first.
- C #5 div-track sends: deferred (a state change); after the caps the div tracks' phrase ends fall with the sections'.
- A #6 trombone breath before 204: small, deferred.
- Mic changes deferred (an open option to raise with Dan). No audio settings changed.

## Re-bow refit after the render (ONE_TIME #2)

The caps deepened the re-bow dips to 8-24 dB in the render (old fills, `rbdips.py`). `tools/fit_rebows.py 40 cycles/c40/rendered_build/parts.json --hold-max-after 301:0 --write`, then:
- Bass clarinet fills dropped (its pedal is levelled by LEVEL_SHAPES, c35 do-not-touch); no fill on Cb 273.229 (c29).
- Double basses and Violoncellos div re-levelled the c34 way (each list's hold moved back to its old hold, ramped in over 0.3-1.0 s), then the Cb coda lists 276.05 / 278.351 / 282.203 scaled x0.6 over their first 0.6 s and 283.605 x0.5 (the refit had lifted the coda pedal 2-4 dB with 5-8 dB attack peaks; now within 1.5 dB of c39 per qn except 276-278 +2).
- Result on the 88 re-bows: dip median 5.0 dB (p90 8.6), |step| median 1.1 (p90 3.1); peaks over the body above 2.5 dB at 23 points, at most 3.8 except Cb 276.05 / 278.351 (3.1 / 4.4) and Violas div 79 (5.3).
- No list ends on a non-zero hold into a later note: `REBOW_FILL_END_S` 0.12 (Movement I c45, ported on the coordinator's note) is on and wrote no `rebow_fill_ends` entries.

## Stem fix, delivery, run

- `tools/stem_fix.py 40 cycles/c40/rendered_build build --apply` on 9 tracks (fills, Clarinet 2 trims, low-string gains), then `render_cycle.py 40 --measure-only` and `build_reaper.py --mix-only` on the same 9 tracks while holding the lock.
- Incident: the first --apply wrote Clarinet 2 through a symlink I had put into the stem_fix scratch folder, overwriting `render/07_Clarinet 2.wav` before its original was copied. The original was reconstructed exactly (divided by the same envelope gain, `restore_cl2.py`; the original master equals the sum of the restored stems within 1e-6) and the fix re-applied. Lesson: never put links into stem_fix's --out folder.
- Master (final stems): -20.2 LUFS, LRA 24.0 LU, TP -1.1 dBFS, sample peak 0.882 (render before the fix: -20.4 / 24.3 / -1.3). c39: -20.2 / 24.3 / -1.3.
- Delivered `cycles/c40/mvt2-mockup-c40.mp3`: -19.8 LUFS, LRA 15.2 LU, TP -1.6 dBTP, p10-to-max span 18.8 dB, limiter about 2.4 dB (c39: -19.8 / 15.4 / -1.6 / 19.0 / 2.2).
- Attack probe: 0 late or holes (before and after the fix). No clipping; all 32 stems sound. Loop autocorrelation at 3.95 s (100-300 Hz): final chord -0.10, Cb pedal 220-238 -0.07, Vc div coda -0.04, opening -0.15 (no pulsing).
- REAPER: 26 GB at open, 44 GB settled (0 compressed) before the build; 44 GB / 33 GB compressed after the restart's 2 min flat settle, rendered with `--force-memory`; 45 GB (28 GB compressed) after the render.
- Lock: requested 14:40 (Movement I held REAPER; no other waiter), held 15:35:04-16:19:15 (44 min). Build of 32 tracks 66 s, render 7.5 min.

## Open for c41

- Basses against Horn 1 at 226-238: -12.4..-3.0 -> -10.1..-0.7 dB (caps + refit + gain); the c39 +3 there is now too much (at 234-238 the 4-soli pedal is within 1 dB of the solo).
- Trombone 1's 214.875 transition dip (4.3 dB).
- Violins II 112 (13.8 dB) and Violas 69 / 248.5 (11.5-12.5 dB) soft re-bows deeper than the 3-5 dB target; Violas div 79 attack peak +5.3.
- B #2 (bass fundamental at the climaxes), C #2, C #5.
