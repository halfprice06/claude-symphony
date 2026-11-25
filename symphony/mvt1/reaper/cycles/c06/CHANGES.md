# Cycle 6: changes (render of c06, reviewed by the critics of c07)

Inputs: critic reports A (articulation), B (balance), C (dynamics over time) on the c05 render. Snapshot before the changes: `before/`. One render from a freshly restarted REAPER (`--midi-only` on 30 tracks; no Opus state changed, so no track was fully rebuilt), then one level-only stem fix (below). First render: `render_first/`, `metrics_first/`, `render_first_delivery.mp3`; `render/`, `metrics/` and `mvt1-mockup-c06.mp3` are the fixed version, and the REAPER project matches it (`--midi-only` on the same 30 tracks after a restart, saved, REAPER quit).

## Changes

Tools (`tools/score_to_parts.py`, generic rules with defaults; movement I values in `build/score_config.py`):
1. A #1 `DOWNBOW_STROKE_AT` (default empty): a listed string note is a fresh Sus MAX stroke (the c06 Leg -> Sus entry path: entry lead, velocity 105, the legato note before it cut at the keyswitch), velocity from `REBOW_VEL_BY_CC`; the Leg BC pass and the note-length pass let the next note join from the stroke as a Leg BC legato target (as `SHORT_SUS_JOIN`). Movement I: Violins I 636, Violins II 628 and 636, Violoncellos 636.
2. A #2 `WIND_REP_RETONGUE` {gap_s 0.06, frac 0.25, fall_cc 6, fall_s 0.12} (on by default): an unslurred same-pitch wind/brass repeat on a Sus row ends min(0.06 s, 25% of the note) before the next onset and its CC11 falls 6 CC over its last 0.12 s, back at the next onset (`cc_falls` rows now take an optional return length). 297 repeats on 22 tracks (parts.json `rep_retongued`).
3. A #3 `TENUTO_SWELL_DB` 1.5: a slurred string tenuto at f or louder that is a legato target gets +1.5 dB from +0.05 s to its end (Violins I 4, Violins II 3, Violas 1, Violoncellos 2 notes).
4. B #1 `ACC_SRC_EXTRA`, `ACC_PLAIN_WIN` and `GENTLE_ACCENT[family]["vel_add"]`: an accented note on a gentle family plays the median source velocity of the unaccented notes around it plus vel_add. Rendered with brass +5, winds/strings +10 (485 notes 10-15 velocity lower): no measurable effect (below), so movement I sets no vel_add and the rule is off.
5. C #1 `ARRIVAL_WEIGHT_AT` {qn: (pre_db, db)}: on every wind, brass and string track that starts a note on the arrival, the level falls linearly from 0 at qn - 4 to pre_db at qn - 0.1 and steps to +db (full at +0.05 s, held to qn + 0.5, gone by qn + 1). Movement I: 636 (-2.5, +1.5; +2.5 in the render, see the stem fix), 484 (-1.5, +1.5).
6. C #2 `LEVEL_SHAPES` {track or "_all": [[(qn, dB), ...]]}: exact piecewise-linear level shapes from the config. `PT_OFF_IN_CRESC` True: phrase-top pitch contours are 0 inside every crescendo (before: only inside soft lead hairpins).
7. C #5 percussion damp: `PERC_MAP[track]["_damp"] = [(qn, dB, s)]` fades the track by dB over s seconds from qn and holds it until the track's next stroke (`build_perc_track`, exact breakpoints in `vol_bp`).
8. A #5 (test) `SHORT_SUS_LEG_TRACKS` / `SHORT_SUS_LEG_S` (0.20, 0.25): slurred, monophonic, non-first notes of 0.20-0.25 s on the listed tracks stay Leg Slur MAX legato targets instead of Sus MAX (not when their own pitch follows in the slur).

Config (`build/score_config.py`, `build/*.json`, `build/mix.json`):
9. Reverted the failed c05 test `SHORT_SUS_LEAD_TRACKS` (now empty).
10. A #1 `build/entry_leads.json` extras at 636: Oboe 1 +0.065, Flute 1/2 +0.015, Trumpet 3 +0.07, Trombone 1 +0.02, Bass trombone +0.01, Horn 1 and Trumpet 1 -0.02 s (totals 0.12 / 0.07 / 0.12 / 0.07 / 0.06 / 0.03 s; the caesura gap caps them at about 0.1 qn).
11. A #3 `PORTATO_JOIN_AT` += Oboe 1 277/393/400/405, Cor anglais 393/400/405, Flute 1 277/393/400/405/436, Flute 2 277, Bassoon 1 413, Trumpet 1 277.
12. A #5 test on Violins I with `LEG_CAP_FRAC` Violins I 0.75 over qn 56-728 (Violins II the control).
13. C #2 `LEVEL_SHAPES`: +4 dB ramp over the 236-244 crescendo on its nine tracks (gone at 243.94), `_all` -3 dB over the sub. p bar (244-247.5, back by 248), Horn 3 a further -3; Clarinet 1 +3 over its p < mf (504.5-512, held to 513, gone by 514).
14. C #4 `BREATH_SPLIT_AT` Horn 3 [722.3, 724.6, 726.6], Horn 4 [721.6, 723.8, 725.9] (pieces 1.9-4.2 s, irregular); `BREATH_SPLIT` dip -3 -> -1.5 dB (A #6).
15. C #5 Tam-tam `_damp` [(504.2, -24 dB, 0.5 s)]; mix.json Tam-tam `tail_hold: false` (the tail hold froze the envelope at the note-off at 504.19, just before the damp; the whole tam-tam sound is ring).
16. B #2 roles Oboe 1 [176,184,+4], Violins II [176,183,-2], Violoncellos [176,182.5,-2,0.25]; note trim Oboe 1 578 +8 (step). B #3 Tam-tam roles [484,500,2,4] and [487,496,4,4] (were [484,512,2], [487,512,4]). B #4 Timpani [711.5,719.5] +5 -> +10. B #5 mix.json Violins II `dyn_trim_db` ff -1.5 -> +1.0. B #6 note trims Horn 1 192 +4, 592 +5 (steps). B #1 (part 2) note trims +3 dB (steps, `NOTE_TRIM_RAMP_S` 0.1 s) on the 23 legato notes under 1 qn in Horn 1 bars 69-72 / 167-170 and the 11 in Trumpet 1 bars 167-170.
17. C #3 roles Violoncellos [338,348,+3] (on top of [336,358,+3]), Double basses [336,348,+2], Violas and Bassoon 1 [348,358] +3 -> +5.
18. `auto_fills.py 5` on c05 (excluded Vc 504, Vc 112 (hand-set), Vc 363 and Cl1 227 (re-added after the c05 pass removed them)): 4 new, 5 raised, lowered/removed the rest of its list.

The parts.json diff against c05 was checked before rendering: tempo map and every `rebows` row identical; note changes only at the listed rules (Vln I qn/dur changes from the reverted c05 lead and the A #5 test); CC11 at the re-tongued repeats falls 6 CC over the last 0.12 s and is back at the onset.

## Stem fix after the render (`stem_fix.py`, level only; master rebuilt as the stem sum)

The first render delivered a 4.4 dB limiter (master sample peak 1.84 at qn 636.2, against 1.52 in c05):
- The down-bow strokes at 636 played well over the planned arrival weight: per stem over 636.0-636.25 against c05, Violins II +11.5 dB (of which +2.5 arrival, +2.5 the new ff trim), Violins I +6.4, Violoncellos +4.6. `LEVEL_SHAPES` cuts take each stroke back to c05 + the arrival weight: Violins II -6.0 -> -3.5 dB over 635.94-637.4, Violins I -3.5 -> -1.5, Violoncellos -2.0 -> -1.2.
- With the strokes cut, the arrival itself (crash + every track +2.5 dB) made a 1.70 peak at 636.3: `ARRIVAL_WEIGHT_AT[636]` +2.5 -> +1.5 (the step from the held-back crescendo top stays 4 dB).
- C #6: `JOIN_NOTCH` Violins I (637.6, 638.1, -1.5 dB) on the A-flat6 join peak (the second master peak, 1.60).
- B #1: the accented notes' 10-15 lower velocity changed nothing (below); `GENTLE_ACCENT["brass"]["db"]` 4.0 -> 2.5 instead, and `vel_add` removed (parts.json velocities back to the c05 values; the audio is the same).
- B's fallback for the climax margin: `_all` [484,492,-0.5,2] (the 484 arrival narrowed the delivered margin of bar 160 over bar 122 to 0.54 dB).
Every other parts.json field was unchanged by these (velocities aside), so the fix is exact.

## Measured, c05 -> c06 (fixed render)

- **Delivery**: master -16.5 -> -16.5 LUFS, LRA 21.8 -> 21.6 LU, sample peak 1.519 -> 1.562 (float stem sum; the 24-bit render clipped), true peak +3.6 -> +4.0 dBFS. Delivered -19.8 / -19.8 LUFS, LRA 15.6 -> 15.2 LU, p10 span 20.3 -> 20.0 dB, limiter 3.0 -> 3.2 dB, -1.5 dBTP. Motion dS4 p90 / 1s-20s 9.08/4.86 -> 9.07/4.79.
- **Climax order** (delivered short-term max, LUFS): bar 160 -9.56 -> -9.41, bar 122 -10.29 -> -10.36, bars 167-170 -12.10 -> -12.18; margin 160 over 122 0.73 -> 0.95 dB.
- **Arrivals (A #1, C #1)**: delivered momentary step (M over [t, t+0.4] minus the highest M ending in the 0.9 s before t): 636 -0.4 -> +2.6 dB, 484 +1.3 -> +3.5 dB; master 0-0.15 s minus -0.45..-0.05 s at 636 -1.3 -> +3.0 dB (A's criterion +1.5). At 636 the stems reach body - 3 dB at: Trumpet 3 +0.17 -> +0.03 s, Horn 1 +0.04 -> +0.01, Trumpet 1 +0.03 -> +0.01, Violins I +0.11 -> +0.06, Violins II +0.01 -> +0.09, Violoncellos -0.10 -> +0.09 (strokes reach their fuller body slightly later; there is no sag at the beat any more: Violins I -27 dB at -0.05 s -> -17 dB at +0.05 s). Stroke 2-5 kHz first 80 ms minus body: Vln I -10.9, Vln II -12.1 (628: -7.1), Vc -10.9 dB (criterion <= 0). Not met: C's +3 dB delivered step at 636 (+2.6).
- **Repeats (A #2)**: median dip, repeats under 3 dB (c05 -> c06): Flute 1 3.6 -> 7.3, Oboe 1 3.0 -> 4.6, Oboe 2 2.3 -> 4.7 (7 -> 3 of 12), Clarinet 1 3.3 -> 6.5, Clarinet 2 3.1 -> 6.1 (5 -> 0 of 11), Bass clarinet 0.7 -> 3.5, Bassoon 1 2.6 -> 4.3 (12 -> 4 of 17), Bassoon 2 0.7 -> 1.6, Contrabassoon 1.4 -> 3.1 (34 -> 19 of 41), Horn 1 2.2 -> 3.4, Horn 2 0.1 -> 1.1, Horn 3 1.1 -> 2.9 (25 -> 16 of 31), Horn 4 0.2 -> 1.9 (32 -> 29 of 36), Trumpets 1/2/3 2.6/2.1/1.2 -> 5.6/4.3/3.9, Trombones 1/2 1.4/1.6 -> 3.3/3.1, Bass trombone 2.0 -> 3.9, Tuba 1.8 -> 3.0; no repeat deeper than 12.8 dB (the deepest were as deep before). Criterion (median 4-7 on every track) met on the winds and trumpets, not on the horns, Bassoon 2 and the low brass.
- **Wind tenutos (A #3)**, dip / body minus the note before: Oboe 1 393 4.4/-0.5 -> 4.8/+3.7 (pass), 400 10.1/-6.7 -> 6.9/-4.5, 405 4.4/-2.8 -> 9.2/-3.4 (worse); Cor anglais 400 5.3/-2.0 -> 8.7/-0.8, 405 5.5/+0.4 -> 3.1/+1.3; Flute 1 393 6.1/+3.7 -> 7.8/-3.6 (worse), 400/405 dips 5.2/6.8 -> 7.6/7.6; Flute 2 277 12.1 -> 10.3; Bassoon 1 413 6.2/-4.7 -> 4.8/-3.1; Trumpet 1 277 5.2/+4.0 -> 3.9/-1.3. Mixed: the 8-9-semitone joins of bars 98-102 dip 7-9 dB on Leg Slur MAX. String tenutos (body - before): Violins I 393/400 -3.4/-3.9 -> -1.0/+4.9, Violins II 393 -2.7 -> -0.9, Violas 429 -7.0 -> -7.0.
- **Accent velocity (B #1)**: on all 27 tracks the 485 accented notes rendered at 10-15 lower velocity (c06 first render) have body (+0.05-0.35 s) and peak (-0.05..+0.12 s) levels identical to c05 to 0.01 dB (median per track; p10/p90 within 0.4 dB except Violins II, which carries its +2.5 dB ff trim). After the swell change: accented minus other notes, Horn 1 bars 69-72 +7.6 -> +4.8, Horn 1 bars 167-170 +8.1 -> +4.5, Trumpet 1 bars 167-170 +7.5 -> +6.0 dB (target 2-4).
- **B #2** oboe minus the loudest string stem per 2 qn over 176-184: -10.5/-5.9/-4.8/-7.1 -> -4.2/+0.1/+1.2/-1.5 dB; 578 pickup -50.3 -> -45.1 dB (579 -39.9). **B #3/C #5** tam-tam minus master: qn 500 -5.0 -> -10.1, 502 -6.2 -> -12.2, 505.5 -7.8 -> -37.3 dB (criterion 15 under), stroke at 490 unchanged (-14.0 -> -13.8). **B #4** coda timpani stroke peaks minus master -11.8..-15.2 -> -7.3..-10.3 dB. **B #5** Violins I minus Violins II, bars 117-120 +6.8 -> +4.5, bars 157-161 +7.2 -> +4.2 dB. **B #6** Horn 1 minus celli at 192/592 -11.0/-12.2 -> -7.0/-7.7 dB.
- **C #2** master per beat, bar 60 -27.4/-27.9/-27.8/-30.9 -> -27.5/-27.6/-26.9/-29.6, bar 61 -28.6/-28.5/-28.3/-29.4 -> -27.2/-25.9/-25.4/-26.9 (now louder than bar 60), bar 62 -32.0.. -> -35.5..; fall into the sub. p (242-244 vs 244.5-246) 2.8 -> 9.4 dB. Violins I notes 236/239.5/240/242/243/243.5: -30.2/-36.0/-35.4/-38.3/-36.4/-37.1 -> -30.6/-34.4/-33.0/-34.3/-33.4/-36.6 (still falling 3-6 dB: criterion not met). **C #5** Clarinet 1 511-512 minus 504.5-505.5 +0.2 -> +2.6 dB (criterion 4).
- **C #3** fugato bars 85-87 master -35.4/-37.1/-39.5 -> -33.5/-34.4/-36.9 (Vc -36.5/-39.2/-41.9 -> -34.4/-36.1/-38.9); delivered momentary means -29.5/-31.0/-31.1 -> -28.4/-29.0/-29.3 against the coda's -26.4..-25.8 (still 2-3 dB under).
- **C #4 / item 7** final chord (720.5-727.7, detrended, max autocorrelation at 3.9-4.7 s): master 250-274 Hz 0.39 -> 0.08 (p95-p5 17.0 -> 15.5 dB), Horn 3 C4 0.73 -> 0.27 (p95-p5 14.3 -> 11.5; criterion 10), Horn 4 G3 0.85 -> 0.29.
- **A #5 test** (72 Violins I slurred eighths moved from Sus MAX to Leg Slur MAX): pitch crossover median +0.120 -> +0.070 s, p90 +0.169 -> +0.110; join dips of 6 dB or more 9 -> 15 of 72 (median 3.0 -> 4.1 dB). Control Violins II (28 same onsets): +0.110 -> +0.110 s, 2 -> 4 dips. Criteria (median <= 0.06 s, dips >= 6 dB 10 or fewer) not met: failed, revert in c07 unless the critics find the dips inaudible.
- **Dan's item 8**: no accent articulation added; new strokes' 2-5 kHz attack minus body -7..-12 dB; brass accent swells lowered.
- **Attack probe**: 0 flagged (first render and fixed).
- **Master top peaks** (fixed): 1.562 (qn 636.3: crash, celli, Violins II, Trombone 1, basses), 1.543 (637.9: Violins I A-flat6 join, Horn 1), 1.421 (637.0), 1.362 (640.6).
- **Memory**: REAPER 26 GB with 0 compressed when the render started, 43 GB with 27 GB compressed after it (macOS: 94 GB used, about 1 GB free during the render; no other large process). Probe and timing as clean as c05.

## Rejected or deferred

- A #4 a2 horns on the 2FH KS Master (new track): deferred again. The render peaked at 43 GB with 27 GB compressed, against the 45 GB guide; a 33rd instance needs memory freed first (unused mics on the solo horns).
- A #6 smaller items: celli tremolo merge (bars 117-121; stem 14 dB under the master), harp étouffez: deferred. Violins I final-chord re-bows: refit with `fit_rebows.py 5 --tracks "Violins I"` gave the same shapes within 0.5 dB (711.855 already at the +10 dB cap), so the c04 shapes were kept.
- B #1 velocity part: rendered, no effect (above); replaced by the brass swell change.
- C #1's articulation part was done as A #1; C's +2.5 dB arrival step was reduced to +1.5 at 636 for the limiter.

## Open for c07

- Revert the A #5 test (`SHORT_SUS_LEG_TRACKS = ()`, `LEG_CAP_FRAC` Violins I) unless the critics judge otherwise.
- Wind portato joins that now dip 7-9 dB (Oboe 1 405, Cor anglais 400, Flute 1 393/400/405, Flute 2 277): A's fallback (Sus MAX, 0.05 s lead, v105) or a fill.
- Repeats still under 3 dB on Horns 2-4, Bassoon 2: raise their `fall_cc` to 10 (A's next step).
- Brass accents still +4.5..+6 dB over the notes around them (target 2-4); Trumpet 1 the highest.
- Delivered arrival step at 636 +2.6 dB (C wanted +3); limiter 3.2 dB (top peak at the 636 arrival with the crash).
- Bars 60-61: Violins I's line still falls 3-6 dB inside the crescendo; Clarinet 1's p < grows only 2.6 dB; fugato bars 85-87 still 2-3 dB under the pp coda in the delivered file.
- Violas 429 tenuto -7 dB under the note before (no change).
