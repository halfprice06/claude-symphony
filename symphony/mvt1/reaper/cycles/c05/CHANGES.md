# Cycle 5: changes (render of c05, reviewed by the critics of c06)

Inputs: critic reports A (articulation), B (balance), C (blend and space) on the c04 render. Snapshot before the changes: `before/`. One render from a freshly restarted REAPER (`--midi-only` on 19 tracks; Violins I, Violins II, Violoncellos and Crash cymbals fully rebuilt because their Opus state changed), then one level-only stem fix (below). First render: `render_first/`, `metrics_first/`, `render_first_delivery.mp3`; `render/`, `metrics/` and `mvt1-mockup-c05.mp3` are the fixed version, and the REAPER project matches it (`--mix-only` on the four changed tracks, saved, read back).

## Changes

Tools (`tools/score_to_parts.py`, generic, defaults there; movement I values in `build/score_config.py`):
1. A #1 `SLUR_REP_MERGE_SUS`, `SLUR_REP_NOTCH` (6 CC, 8 above CC11 90): a string short_sus eighth followed by the same pitch in the same slur on a Leg row is merged into one Sus MAX note with a CC11 notch. `WIND_SLUR_REP_MERGE`, `WIND_SLUR_REP_NOTCH` 8: the same for a wind Leg Slur note and its repeat inside the slur (no tenuto, no breath). The merged note's legato velocity is computed from the eighth's own length (`vel_end`; without it the merged wind eighths dropped from v100 to v60-80). Merged (parts.json `slur_rep_merged`): Vln I 60/108/140/572, Vln II 108, Vla 108/136/668, Vc 314/524; Fl1 108, Ob1 108, Ob2 412/640, Cl1 108/232/310/412/508/524/640, Cl2 412/524 (unison-dropped), BCl 308/428, Bn1 132/524, Bn2 524.
2. A #2 `STR_SHORT_AFTER_SUS` (`max_s` 0.3, `abut_qn` 0.06): an unslurred monophonic string note under 0.3 s whose predecessor ends at its onset on Sus MAX / a stroke / Stac / Tremolo is a Sus MAX stroke (velocity `REBOW_VEL_BY_CC`, end min(0.04 qn, 10%) early, pitch trims as steps, kept off the c06 Leg -> Sus entry path). Checked in order, as A asked, so a run cascades: besides A's 22 notes it converted the violas' unslurred f eighths of bars 98-102 (qn 388.5-407.5) and triplets of bars 117-121 (464-483.7), which were Leg BC MAX joins (parts.json `short_strokes`).
3. A #3 (test) `SHORT_SUS_LEAD_S` 0.05 with `SHORT_SUS_LEAD_TRACKS` = Violins I, II: slurred short_sus notes that are not the first of their slur start 0.05 s early; Violas and Violoncellos are the control.
4. C #2 `BREATH_SPLIT_AT` / `BREATH_SPLIT`: listed held wind/brass notes are split at output into same-pitch pieces on the note's own row (earlier piece ends 0.05 qn before, new piece velocity -8), with a -3 dB dip from +0.03 to +0.12 s, gone by +0.4 s. Movement I: Horn 4 720 at [723.0, 725.5], Horn 3 720 at [723.5, 726.0] (C's 723.5/725.0 left pieces of 8.6 and 6.8 s on the 1.2/2.0 s-per-qn final bars; these give 3.0-5.0 s pieces, the horns 0.6-1.0 s apart). Horn 4's loop profile at 720 removed.
5. A #5 `META_DB` -3: "metà" on a string part lowers single notes by 3 dB until "tutti"/"unis."/"div." (Violins II qn 184-216).
6. `build_perc_track` now applies `roles.json` rows. Found in the stem fix: the percussion tracks wrote a flat envelope, so the c02 Tam-tam row [696,712,+8] had never taken effect.

Config (`build/score_config.py`, `build/*.json`):
7. A #4 `PORT_TARGETS` Violoncellos 685 (v100), Violins I/II 225 (v100): loads the Leg Port MAX row on three tracks.
8. A #6 `TIMP_ROLL_RESTRIKE["at"]` += 464, 484 (7 more re-strikes, same seed rule and dip); loop profile Timpani 484 removed.
9. C #1 Crash cymbals patch `19in Zildjian A Crash` -> `22in Zildjian K Crash` (key 60 = Long RRx1-3, 62/64 Short, read from its region map with `opus_state.load_oib`; same layout as the 19in), gain -6 -> -1.
10. C #3 loud_eq: Double basses + bell2 98 Hz -4 dB bw 0.5; Violoncellos bell 160 +4 -> 150 Hz +6 dB bw 1.0. C #5 (test): Violins I loud_eq bell 3 kHz +2 dB bw 1.5 on the basses' loud spans.
11. B #1 Violins II `soft_trim_db` {ppp 7, pp 7, p 2} (p 5 -> 2) and roles [144,156,-3,4], [304,320,-3,4]; B #2 note trims Bassoon 1 144 -5, 280 -4, Violins I role [144,160,+2,2]; B #3 roles Flute 1 [291,300,+3], Bass clarinet [304.5,310,+2]; B #4 Horn 2 [220,244,+2,2] -> [220,244,-1,2]; B #5 note trim Violoncellos 696 -6; B #6 Oboe 1/2 ff trim 4 -> 6. C #4 Tam-tam roles [484,512,+2] + [487,512,+4] (+2 at the stroke, +6 from about +1.5 s).
12. `auto_fills.py 4` on c04 (`--exclude Violoncellos:504`): 5 new, 5 raised, 10 lowered, 2 removed (Cl1 227, Vc 363, Vc 484); Vc 112 (A's 8.1 dB hole) gets +6.

The parts.json diff against c04 was checked around every changed rule before rendering: re-bow rows (`rebows`) identical on every string track, tempo map identical, the only note changes are the merges, strokes, leads, port targets, splits and re-strikes above.

## Stem fix after the render (`stem_fix.py`, level only; master rebuilt as the stem sum)

- Violas roles [388.5,408,-4] and [464,484,-3.5, opening over 480-484]: the new strokes of item 2 played 3.0-5.6 dB louder than the Leg BC joins they replaced (bars 98-102 +4.35 dB, bars 117-121 +3.57 dB stem mean); back to the c04 balance.
- Tam-tam: the roles of item 11 now apply (item 6). The c02 row [696,712,+8], active for the first time, put the pp soft-stick stroke 3-5 dB over every string stem of the bar-175 chorale (plain power); critic B accepted the current balance, so the row is removed rather than made active unmeasured.
- Trombone 1/2 [484,496] +3 -> +2.5 (C #4: the tam-tam rows narrowed the margin of bar 160 over bar 122).
Every other parts.json field was unchanged by these (checked), so the fix is exact.

## Measured before (c04) / after (c05, fixed)

- **Delivery**: master -17.0 -> -16.5 LUFS, LRA 21.5 -> 21.8 LU, sample peak 1.440 -> 1.519 (float stem sum; the 24-bit render clipped). Delivered -19.8 / -19.8 LUFS, LRA 15.5 -> 15.6 LU, p10 span 20.2 -> 20.3 dB, limiter 2.8 -> 3.0 dB, -1.6 dBTP. Motion dS4 p90 / 1s-20s 8.91/4.81 -> 9.08/4.86. Top master peak still qn 637.9 (Vln I 0.36, Horn 1 0.22, Violas); third peak now the crash at 636.8 (0.31).
- **Climax order** (delivered short-term max, LUFS): bar 160 -9.6 -> -9.6, 122 -10.6 -> -10.3, 169-170 -12.1 -> -12.1. Order kept; margin 160 over 122 1.0 -> 0.73 dB (C's floor 0.8; the -0.5 dB trombone change moved it 0.05 dB).
- **A #1** (stem, arrival minus the eighth before; +0.05-0.2 / +0.2-0.5 s): strings Vln II 108 -7.4/-12.9 -> +0.6/+2.1, Vla 668 -4.9/-13.1 -> +1.0/+0.5, Vla 108 -4.6/-12.9 -> +1.1/+0.7, Vln I 108 -4.2/-12.8 -> +0.2/+0.9, Vc 314 -3.2/-9.9 -> -1.4/-1.2, Vln I 140 -> +2.1/+3.1, Vln I 60 -> -1.5/+2.8, Vc 524 -> +1.3/+1.6, Vla 136 -0.5/-2.7 -> +2.6/+5.6, Vln I 572 -> -1.4/+2.7: every string arrival passes (within -3 dB). Winds, deepest 30 ms frame -0.05..+0.2 s against the louder body: Cl1 412/508/524/108/310 -10.7/-11.6/-9.6/-9.7/-11.5 -> -5.1/-3.7/-3.5/-4.9/-5.6, Ob1 108 -11.9 -> -4.7 (criterion 4 dB: 2 of 6 pass; the rest is the 8 CC notch). Ob2 412 reads +10.9 dB / -14.4 dB on both renders' scale (its eighth before is near silent), not judged. Master qn 60.5-60.9 minus 59.5-59.95 -5.7 -> +2.9 dB (the bar-16 arrival now louder than the eighth before, not falling); Vln I dips 61.0 -14.3 -> -8.5, 109.0 -18.3 -> -3.2 dB.
- **A #2** crossovers on A's 22 notes plus the violas' 553-567 returns (28 measurable): median +0.198 -> +0.125 s, over 0.15 s 21 -> 8 (criterion median 0.08, none over 0.15: improved, not met; Sus MAX strokes themselves cross at +0.10-0.13 s). Violas bars 139-142 per-eighth swing 8.1 -> 7.6 dB (criterion 4: pass).
- **A #3 test** slurred Sus eighth crossovers (median): Vln I 0.130 -> 0.115, Vln II 0.125 -> 0.105; control Vla 0.105 -> 0.098, Vc 0.115 -> 0.138 s. Criterion 0.07 s not met: 0.05 s of lead moved the crossover 0.015-0.02 s. Failed; revert in c06.
- **A #4 portamento**: intermediate-semitone energy around the join (re the later body) Vln I +11.6 -> +15.3, Vln II +10.7 -> +13.2, Vc -6.6 -> -4.9 dB (a glide on all three); deepest 30 ms frame at the join Vc -13.0 -> -10.0, Vln I -4.5 -> -4.1, Vln II -5.2 -> -4.9 dB (Vc criterion under 5 on A's measure not met).
- **A #5** Violins II over qn 184-212 -43.0 -> -46.0 dB, violas -43.3: now 2.7 dB under the violas' stem (criterion 3 +- 1.5: pass).
- **A #6 timpani** (centroid autocorrelation, best lag 2.8-4.3 s, detrended): qn 464-484 0.85 -> 0.55, 488-504 0.95 -> 0.16, 500-520 0.95 -> 0.48 (criterion 0.45: 1 of 3 pass, two near); re-strike level steps -1.6..+1.6 dB.
- **C #2 horns** at qn 720 (autocorrelation at 3.95 s, 100-300 Hz / centroid): Horn 4 0.92/0.75 -> 0.80/0.26 (best lag 4.2 s 0.85/0.64, which is the spacing of the two splits); Horn 3 -0.08/-0.28 -> 0.43/0.20. Master final chord -0.15/0.02 -> -0.15/0.03 (unchanged). Split re-entries on the stems: dips -3.6..-8.9 dB within 0.4 s, level after +-3 dB; master 0.5 s after minus before -0.8, -3.0 (726.0, inside the morendo), +0.1, +0.7 dB. Criterion 0.4 met on Horn 4's centroid only; the dips themselves now set the level autocorrelation.
- **C #1 crash** (4-12 kHz, stem minus master): +0.4 s -4.2 -> -0.9, +0.9 s -9.9 -> -4.0, +1.4 s -17.5 -> -9.7, +1.9 s -24.4 -> -15.1 dB (C's target within 6 dB at +1.5 s: not met, 8 dB better).
- **C #4 tam-tam** (stem minus master, broadband / 4-12 kHz): +0.5 s -8.9/-5.1 -> -7.8/-4.0, +1.5 s -12.0/-7.1 -> -8.6/-4.7, +2.5 s -17.3/-16.1 -> -11.7/-11.0, +4.0 s -21.4 -> -15.8 dB.
- **C #3 low end** (loudest 10% of frames re 300 Hz-1 kHz): 89-112 Hz -11.9 -> -13.9 (target -14), 112-140 -17.0 -> -16.5, 140-180 -14.8 -> -14.4 (target -14), 63-89 -21.2 -> -21.7.
- **C #5 test** loudest 10% 2-4 kHz re 500 Hz-2 kHz -9.6 -> -8.6 dB (target +1-1.5), middle frames -9.3 -> -9.4 (unchanged); Violins I accents in bars 116-122 and 158-161, 2-5 kHz first 80 ms minus body median -12.6 -> -12.5, max -9.9 -> -9.9 (limit +3): passes.
- **B** (stem plain power, c04 -> c05): Violins II qn 144-160 -31.5 -> -33.0, 304-324 -33.9 -> -35.2; Violins I 144-160 -36.4 -> -34.1; Bassoon 1 144-148 -33.5 -> -37.6, 280-284 -33.1 -> -36.6; Flute 1 291-300 -45.2 -> -42.2; Bass clarinet 304.5-310 -39.3 -> -37.1; Horn 2 220-244 -36.8 -> -39.7 (Clarinet 1 -41.4, Violins I -35.5 -> -35.4); Violoncellos 696-700 -36.5 -> -41.6 (Trombone 1 -42.6); Oboe 1 ff 104-128 -35.1 -> -32.9, 628-644 -30.1 -> -28.1 (Flute 1 -31.0 / -25.9).
- **Dan's item 7**: master final chord unchanged (above); timpani rolls above. **Item 8**: no accent articulation added; Violins I accents unchanged under the new EQ.
- **Attack probe**: 0 flagged (first render and fixed).
- **Memory**: REAPER 23 GB before the render, 43 GB after it with 0 GB compressed. Quit after the render and again after the `--mix-only` update (both quit jobs timed out at 60 s; REAPER killed after the save, as in c18-c23).

## Rejected or deferred

- C #6 percussion seats: deferred (inferred only; seats are on the do-not-touch list and need a full rebuild of three tracks).
- A's smaller items: brass repeat re-tongue test (Horns 3/4 bars 19-22, 31), breath marks (Hn3 536), soft string legato velocity test, harp étouffez, a2 horns: deferred. Re-bow residuals: not refit (the c04 stem fix already fitted `fit_rebows.py 4` on c04, and the re-bow rows are unchanged).
- B's optional generic `TREMOLO_DB`: not done; the roles cover the single-note p tremolos in this score.
- The c02 Tam-tam [696,712,+8] row: removed (see the stem fix).

## Open for c06

- Revert the A #3 lead (`SHORT_SUS_LEAD_TRACKS = ()`): failed its criterion.
- A #2 strokes still cross at +0.10-0.2 s (8 of 28 over 0.15 s); the violas' cascaded strokes in bars 98-102 and 117-121 are a larger change than A measured: check them by ear-proxy (per-note swing, crossovers) and against the c04 Leg BC joins.
- Horn 3/4 split dips (up to 8.9 dB on the Horn 4 stem at 723.0) and Horn 3's level autocorrelation 0.43: tune the dip or the split times.
- Timpani 464 window 0.55 and 500-520 0.48: shorter pieces there.
- Crash ring still 9.7 dB under the master's 4-12 kHz at +1.4 s; low-end 140-180 Hz still 0.4 dB under C's target.
- Wind slurred repeats keep a 3.5-5.6 dB dip from the 8 CC notch; a 4-6 CC notch would meet A's 4 dB criterion.
- Delivery limiter 3.0 dB (peak 1.52 at qn 637.9: Violins I, Horn 1, Violas, Trombone 1).
