# Cycle 8: changes (render of c08, reviewed by the critics of c09)

Inputs: critic reports A (articulation), B (balance), C (holistic) on the c07 render. Snapshot before the changes: `before/`. One render from a freshly restarted REAPER (`--midi-only --tempo` on all 32 tracks; no Opus state changed, so no patch reloaded), then one level-only stem fix (accent refit, below). First render: `render_first/`, `metrics_first/`, `render_first_delivery.mp3`, and the data it was made from in `rendered_build/` (parts.json, mix.json, accent_fits.json, score_config.py). `render/`, `metrics/` and `mvt1-mockup-c08.mp3` are the fixed version; the REAPER project matches it (`--mix-only` on the 17 fixed tracks, saved, REAPER quit).

## Changes

Tools (`tools/score_to_parts.py`; generic rules with defaults, movement I values in `build/score_config.py`):
1. C #1 `ARRIVAL_WEIGHT_AT` values may carry a third element, the hold-back length in qn (default 4, the old behaviour).
2. A #4 `TREM_JOIN` {track: [(from, to)]}, `TREM_JOIN_LEAD_S` 0.3, `TREM_JOIN_OVERLAP_QN` 0.4: tremolo notes inside the spans join through the c15 Flautando mechanism (common tones held as one note, moving voices start early, old moving notes end at the new score onset + overlap). `TREM_SPLIT` {max_s 4.4, seg_s (2.5, 3.3), clear_qn 0.3, gap_qn 0.005}: a held tremolo note from these spans is split at the output stage into abutting same-pitch tremolo pieces of seeded length that start at least clear_qn from any onset and barline; AUTO_REBOW skips these notes. parts.json `trem_splits`.
3. C #5 / A #6 `METRIC_BOWED` {track: spans}, `METRIC_BOWED_DB` {down 1.0, mid 0.5, beat 0, off -0.5}, `METRIC_BOWED_MAX_QN` 0.5, `METRIC_BOWED_REP` (REP_SPLIT strokes too), `METRIC_TIMP_DB`: the c20 METRIC_DB step shape (full on the attack, held to the next onset, once per onset) on short unslurred unaccented bowed notes and on loud Timpani Flt Lng strokes. parts.json `metric_db` keys `m_*`.
4. Note trims are applied once per onset (the longest note at the onset carries them). Before, a trim on a 2-note chord was applied twice (the celli's new -5 dB trims at qn 100/548 came out -10). No earlier trim sat on a chord, so nothing else changed.
5. `tools/fit_accents.py`: `--pickup-qn` (default 0.5; A #2): a note of that length or less that starts a slur is not a neighbour. `--keep-long-qn` (default 1.5): no negative step trim on an accent note longer than that or on a crescendo's arrival note (an existing negative trim there is dropped and refit). The default starting swell follows the family (brass 2.5, wind 3.5, string 3.0).
6. C #3 `tools/deliver_master.py`: a slow top ride (above the 95th percentile - 3 dB, ratio 1.6, the same 3 s smoothing) after the low ride. The critic's 2.0 ratio simulated bar 160 only 0.35 LU over bar 122 on these changes; with 1.6, 0.49.

Config (`build/score_config.py` c08 block, `build/*.json`):
7. C #1 `ARRIVAL_WEIGHT_AT` {636: (-2.5, 1.5, 0.5), 484: (-1.5, 1.5, 0.5)}. Violins I/II E6 fill `LEVEL_SHAPES` [(629.5,0),(631.5,4),(633,4),(635.4,4),(635.9,0)].
8. C #4 (hand version) celli hairpin shapes at 184-188, 196-198.3, 201-203.3, 589-591.3.
9. B #2 bar 122 shapes (484 -> 484.2 ramp, to 492, gone by 492.5): Violins I/II -3, Horns 1-4 +4, Violas +6, Double basses +4, Trumpets 1-3 +1.5.
10. B #3 bar 82: Trumpet 1 shape +4 (324.2-328), Violoncellos -3 (324-328); roles Trumpets 2/3 [324,328,-2], Violas [324.5,328,+3]. B #4 Violas [104,120,+2.5].
11. B #1 `note_trims.json` (steps, NOTE_TRIM_RAMP_S 0.1 s): Violoncellos 100/548/556 -5, 526/272 -3; Oboe 1 95 -3, 99/100 -4, 113 -5, 479 -3, 553 -6, 557 -4; Horn 1 97 -4, 633 -5; Flute 1 118/121.5/482/561.5 -4, 160 -5; Flute 2 285/459 -6; Bass clarinet 284/286 -4, 554 -5; Clarinet 1 414/417 -3, 422 -2; Trombone 1 632/676 -2. A #1: Violins I 59.5 -4, 571.5 -3.5.
12. A #5 `BREATH_GAP_AT` / `BREATH_FALL_CC` (0.4 qn, 8 CC): Horn 1 468, Horn 3 252/532, Horn 4 504 (keys are the onsets of the notes that end at the breath; 468 and 504 are merged held notes); Flute 1 / Oboe 1 634 (0.12 qn, the caesura gap, + 8 CC). `WIND_REP_RETONGUE_BY["Horn 4"]` {gap_s 0.14, frac 0.35, fall_cc 14, fall_s 0.18}.
13. A #4 `TREM_JOIN`: Violins II (304,324), (440,464), (584,620); Violas (154,168), (304,324); Violoncellos (464,484). Result: 15 Vln II notes merged, 1 split (592.33); celli G2 464-484 one note in 3 pieces (splits 469.87, 476.33).
14. C #5 `METRIC_BOWED` Violas, Violoncellos, Double basses on (56,128), (272,286), (520,568) with REP_SPLIT strokes: steps on 46 viola, 1 cello, 90 bass onsets (the celli's notes there are slurred or longer). A #6 `METRIC_TIMP_DB` {down 0, mid -1, beat -2, off -3, at f+}: 29 strokes.
15. C #2 `PHRASE_ARCS` + (272,286 main), (324,332 main), (332,348 sub), (348,360 sub), (384,396), (396,408 main), (408,416 sub), (416,424), (424,432 sub), (432,440 main), (440,452 sub), (680,688 sub), (688,696 main); `TEMPO_PUSH` + (308,324,1.015), (364,384,1.015), (452,464,1.01); `REBOW_AT["Violas"]` [686.694, 699.507].
16. B #5 `mix.json` `loud_eq` bell 140 Hz (1 oct) on the celli's loud spans: Tuba, Bass trombone, Contrabassoon +4, Bassoon 2, Timpani +3.
17. `accent_fits.json`: A #1/#2 string and wind fits added (string `--max-trim 5`, wind `--min-trim -4`), brass refit (`--pickup-qn 0 --keep-long-qn 0`, unchanged rules), all on the c07 render; refit on the c08 render (stem fix).

parts.json checked against c07 before rendering: `rebows`, `restrikes`, `breath_splits` identical except the violas' two listed points (same qn; piece start 695.73 -> 695.76 and note end 689.65 -> 689.64 from the arc leads); CC11 at moved note-ons equal to the score-onset value except the same legato targets as c07 (182 -> 181); tempo differs only in 272-464 and 680-696 (+0.60 s; longest constant run 208 -> 56 beats, the Lento; the development's longest 23); breath ends and Horn 4 gaps as planned.

## Stem fix after the render (level only, exact)

`fit_accents.py 8 build/parts.json` for strings, winds and brass with the new `--keep-long-qn` rule. The first render showed that a fitted -6 dB step on Violins I's whole-bar ff arrival (qn 100) took the section 4.7 dB down in bar 26 (and -4 dB on 558 lowered bar 140): the step covers the whole note, the measure only its first 0.35 s. 17 tracks changed (`vol_db` only); master peak unchanged (1.387).

## Measured, c07 -> c08 (fixed render)

**Accents** (`fit_accents.py` measure: +0.05..+0.35 s over up to two unaccented same-dynamic neighbours each side):

| Family | n | in 2-4 dB c07 -> c08 | under 1 dB | over 5 dB | median |
|---|---|---|---|---|---|
| Strings | 134 | 26 -> 112 | 51 -> 3 | 25 -> 1 | +1.8 -> +3.0 |
| Woodwinds | 140 | 32 -> 126 | 32 -> 3 | 49 -> 1 | +3.65 -> +2.9 |
| Brass | 36 | 33 -> 33 | 0 | 2 -> 2 | +3.0 |

(c08 = first render; the stem-fixed refit predicts strings 127, winds 127, brass 33 of each.) Violins I theme heads on the first render: 57 +1.8, 65 -0.2, 73 +4.8, 521 +3.5, 529 +3.5 (A's criterion +2: 57 and 65 short; both at the 5 dB swell + 5 dB step caps). 2-5 kHz first 80 ms minus body: string median -10, wind -11, brass -6.8; over 3 dB: 2 string (Violas 536 +11.2, the earlier-note artefact A described; Violas 120 +3.9), 1 wind, 4 brass (c07: Horn 1 124/665 and the known artefacts).

**Climax approaches** (master, 0.3 s windows): 635.5 minus 630 -0.2 -> +2.2 dB, minus 632 +2.1 -> +4.2; arrival step 636.5 minus 635.5 3.9 -> 1.4 (criterion 1.5); bar 121 last beat minus first +2.6 -> +3.4.

**Tremolo** (min 50 ms level in -0.4..+0.8 s around each change minus the level before): Violins II 588/596/600/604/608/612 -5.8/-8.1/-7.1/-8.5/-6.0/-8.0 -> -2.4/-2.6/-2.4/-3.5/-2.2/-2.9, but 592 -3.3 -> -6.2 (the held A5's split piece at 592.33 re-attacks 0.33 qn after the change); 308 -6.5 -> -4.3, 444-460 -1.3..-4.0 -> -0.7..-3.3; Violas 160 -8.3 -> -5.2 but 156 -3.2 -> -5.3, 164 -5.5 -> -6.2; celli 472/476 -7.6 -> -6.2/-3.4, 468 -9.1 (the bar-117 f crescendo gain released after 4 qn, not a re-attack), 480 -7.9. Celli 464-484 level autocorrelation at the two-bar lag 0.93 -> -0.44 (swing 7.3 -> 7.0 dB). Violins II mean over 584-619 -42.8 -> -42.0 dB.

**Breaths** (min 50 ms in the last 0.35 s minus the level before): Horn 1 475 -2.9 -> -5.1, Horn 3 256 -2.9 -> -5.6, 536 -1.9 -> -6.7, Horn 4 512 -0.5 -> -8.7, Oboe 1 636 -2.5 -> -4.3, Flute 1 636 +0.3 -> -1.8 (not met). **Horn 4 repeats** (A's hrep measure, gaps up to 0.5 qn): median -2.8 -> -4.2 dB, under 3 dB 21 -> 9 of 40.

**Balance (B)**, stem minus master per bar: bar 26 loudest Violoncellos -6.7 -> Violins II -7.9 (celli -10.2); bar 138 Violoncellos -6.3 -> Violas -8.8 (celli -10.0); bar 140 Violoncellos -8.2 -> Violins I -11.0 (celli -11.1, Bassoon 2 -11.9: not the 3.4 dB margin B simulated; the low winds rose 0.4-1.7 dB with the new loud EQ); bar 159 Horn 1 -8.7 -> -10.4 (Violins I -8.1 on top); bar 170 Trombone 1 -8.5 -> -10.4 (level with Trombone 2). Bars 104-106 Clarinet 1 still the loudest (-7.1/-6.5/-4.1; c07 -6.2/-5.4/-4.8). Bar 122 (484.3-487.5): Violins I/II -11.4/-9.3 -> -14.7/-12.6, Trumpet 1 -13.0 -> -11.9, horns -16.5..-19.5 -> -12.8..-15.8, Violas -20.6 -> -14.9, basses -24.7 -> -21.0. Bar 82 (325-327.5): Trumpet 1 -14.1 -> -9.9, Trumpet 2 -11.9 -> -13.8, celli -7.4 -> -10.2, Violas -18.2 -> -14.6. Violas bars 27-30 minus Violins I -5.6/-8.5/-2.5/-8.3 -> -6.1/-6.6/-4.7/-7.3.
**Low end** (loudest 10% of master frames, 1/3 octave re 1 kHz): 125 Hz -7.0 -> -7.7, 160 Hz -6.6 -> -4.7, 100 Hz -5.5 -> -5.0, 63 Hz -15.2 -> -15.4.
**Celli hairpins** (last third minus first third): 184 < -0.1 -> +2.0, 201 < +0.3 -> +2.6, 589 < -0.4 -> +1.2, 187.5 > +2.4 -> +0.1, 196 > +1.8 -> +0.1 (decrescendos now flat, not falling).
**Metric** (C's metric.py, downbeat minus neighbours): Violas +0.61 -> +0.92, Double basses -0.42 -> +0.49, Violoncellos -0.30 -> -0.30 (no eligible notes). Timpani off-beat stroke peak minus the next downbeat (5 cases, my measure) median -4.4 -> -7.2 dB.
**Tempo**: +0.60 s; beats exactly on a mark fell (longest constant run 208 -> 56); jumps over 8% at the returns after the new "main" arcs (110.9 -> 126 bpm at 286, 332, 408, 440; 63 -> 72 at 696), as at the c04 main arcs.

- **Delivery**: master -16.6 -> -16.4 LUFS, LRA 21.3 -> 21.1 LU, sample peak 1.331 -> 1.387, true peak +2.5 -> +2.9 dBFS. Delivered -19.8 -> -19.7 LUFS, LRA 15.3 -> 14.8 LU, p10 span 20.0 -> 18.7 dB, p75->max 10.6 -> 9.4 dB, limiter 2.0 -> 1.2 dB, -1.6 dBTP.
- **Climax order** (delivered short-term max, LUFS): bar 160 -9.33 -> -10.30, bar 122 -10.07 -> -10.89, bars 167-170 -12.40 -> -12.04; margin 160 over 122 0.74 -> 0.59 dB.
- **Master top peaks**: 1.387 (qn 636.42: Violins I, Horn 1, Violins II), 1.299 (640.59: Trombone 2, Tuba, Trombone 1), 1.292 (642.15: Bass trombone, Trombone 1, Trumpet 1), 1.264 (635.54: celli, violas, Trombone 2).
- **Attack probe**: 0 flagged.
- **Dan's item 7**: re-bow and re-strike rows unchanged; new tremolo pieces 2.3-4.8 s (the Violins II A5 at 604 is one 4.8 s piece: the split rule leaves pieces up to 5.3 s); the celli's 9.5 s tremolo pedal now 2.8-3.7 s pieces.
- **Memory**: REAPER 24 GB (0 compressed) when the render started, 43 GB with 3.6 GB compressed after it (24 GB compressed when idle before the quit); another Python process (not this actor's) held 2.9 GB.

## Rejected or deferred

- A #3 a2 horns (and trumpets): deferred again. It adds a 33rd Opus instance and a new routing rule (A2_ROUTE) with its own refits; c07 ended at 43 GB with 23 compressed against the brief's 45 GB.
- A #4 TREM_JOIN for Violins I/II 484-492 and 664-679: not added (the 484 tremolo starts the fff arrival; the coda has its own accents).
- A #6 Horn 2 joins 453/266: left to the next auto_fills pass (not run this cycle: the tempo changed in 272-464). Celli re-bow refit at 163.877/37.377 and basses 166.01: deferred (no re-bow change this cycle).
- A #1 point 3 (theme heads 65, 113, 479 to ACCENT_DB_AT with a higher cap): open; 65 measured -0.2 on the first render with the fit at its caps.
- B #2's 0.2 qn ramp done as LEVEL_SHAPES (roles ramp over 0.5 qn before their start).
- C #3 at ratio 1.6, not 2.0 (climax margin, above).
- C #5 on the celli: no eligible notes in the spans (their notes are slurred or longer than 0.5 qn); the violas' syncopated tied notes are not touched (an off-beat cut would weaken the syncopation).

## Open for c09

- Tremolo splits: the Violins II A5 piece at 592.33 re-attacks right after a chord change (-6.2 dB); raise `TREM_SPLIT["clear_qn"]` to about 1 qn and cap pieces at 4.4 s. Violas 156/164 tremolo joins dip 5-6 dB.
- Arrival step at 636 1.4 dB (target 1.5); bar 160 over bar 122 0.59 LU.
- Clarinet 1 bars 104-106 still the loudest stem; bar 140 Violins I only level with the celli and low winds.
- The new 140 Hz loud EQ raised 160 Hz by 1.9 dB but not 125 Hz, and put Tuba/Contrabassoon/Bassoon 2 0.4-1.7 dB higher in loud bars.
- Violins I 57/65 accents under +2 dB; Flute 1 breath at 636.
- Main-arc returns jump 12% (110.9 -> 126 bpm).
