# Cycle 4: changes (render of c04, reviewed by the critics of c05)

Inputs: critic reports A (articulation), B (balance), C (holistic) on the c03 render, and the c03 open list. Snapshot before the changes: `before/`. One render from a freshly restarted REAPER (`--midi-only --tempo` on all 32 tracks; Bassoon 1 and Double basses fully rebuilt, because the reverted tests unload their test rows), then one level-only stem fix (below). First render: `render_first/`, `metrics_first/`, `render_first_delivery.mp3`; `render/`, `metrics/` and `mvt1-mockup-c04.mp3` are the fixed version, and the REAPER project matches it (`--mix-only` on the seven changed tracks, saved).

## Changes

Carried over from c03:
1. Reverted the two failed articulation tests: `ART_SPANS = {}` (Bassoon 1 Stac DblTng, Double basses Marc Shrt) and the Double basses role [104,112,-6].
2. Wind entry extras halved (`ENTRY_LEAD_ART_S` wind: Leg Slur MAX / Leg Slur 0.11 -> 0.055 s, Sus Non Vib 0.07 -> 0.035 s): Fl1/Ob1 pickups move 0.06 s later (13 onsets each), Cl1 41, CA 6.
3. `auto_fills.py 3` (`--exclude Violoncellos:504`): 30 new, 8 raised, the rest lowered or removed (`build/early_fills.json`). `fit_rebows.py 3 --hold-max-after 720:0`, then (stem fix) `fit_rebows.py 4` on this render.

Tools (`tools/score_to_parts.py`, generic, defaults there; movement I values in `build/score_config.py`):
4. `REP_SPLIT` (A #1): written-out unslurred same-pitch repeats (each 1.5 qn or shorter, 100 bpm or faster, monophonic, not pizz./tremolo/slurred) are separate strokes instead of one merged Leg Slur note with CC11 notches: Sus MAX at the re-bow velocity (`REBOW_VEL_BY_CC`), ending min(0.04 qn, 10%) early; under 0.2 s (triplets and sixteenths at 126) the track's Stac row at a velocity table (mf 80, f 96), written length - 0.02 qn. No new rows, so `--midi-only`. The first stroke after a legato note keeps the c06 Leg -> Sus entry path; later strokes do not (it gave every pp quarter v105 and a 0.12 s lead). A pitch trim on these strokes is a step held to the next onset (the 0.25 qn ramp made a 3 dB sawtooth on every eighth in the render; fixed by the stem fix). New notes: Violins II 18 (bars 23-25, 135-137, 144), Violas 44 (23-25, 98-100, 111-116, 135-146), Violoncellos 37 (bars 127-130; 48 written notes instead of 3); Vc re-bows at 508.157 and 513.49 and their fitted shapes are gone. Stac set at 0.2 s, not A's 0.3 s: the violas' unslurred "c c b(c)" eighths of bars 111-116 (0.24 s) are a detache accompaniment, not staccato.
5. `PORTATO_JOIN_AT` (A #2): Horn 1 189, 201, 589, 601 are Leg Slur MAX targets from the previous note of the slur (velocity `SOST_VEL` 100, `SOST_NOTCH` 10 CC, normal lead and overlap); the tenuto bump stays.
6. `TIMP_ROLL_RESTRIKE` (A #3, C #4): rolls listed in `at` and longer than 6 s are split at output into abutting same-pitch roll notes of 2.5-3.3 s (seeded per note; a remainder over 3.3 s is halved), velocity +-3, the old piece ending 0.002 qn before the next; CC7 and the volume envelope stay those of the whole roll. Each new piece gets a -1.5 dB dip (full at +0.03 s, held to +0.14 s, gone by +0.22 s) over its measured re-strike bump (stem fix). Movement I: qn 0, 48, 720 (12 re-strikes); 464 and 484 stay whole as the control; the loop profiles of 0, 48, 720 removed. parts.json `restrikes`.
7. `SF_ARRIVAL_AT` (C #5): `{160.0: "ff"}`: the bar-41 sf spikes to ff (114) and falls to 106 by +0.75 qn (was 96-100 -> 78), the printed decrescendo carrying it to bar 42's mf.

Config (`build/score_config.py`, `build/*.json`):
8. `LEAD_SPANS` and `HP_SOFT_EXTRA_SPANS` (C #1, exactly as proposed): phrase tops on 30 lead slurs, soft-hairpin ramps on 15 hairpins.
9. `PHRASE_ARCS` (C #2 step 1, 13 arcs as proposed) and `TEMPO_PUSH` (88-100, 552-564). C's (148, 160) push was dropped: it moved the celli re-bows at 152.46 and 163.88 by 0.01 qn, and C's own rule says to drop an arc that changes a re-bow row. After that, the parts.json `rebows` rows equal c03's except the two removed by item 4. Tempo-map markers 421, mismatches [].
10. `TIMP_VEL` coda strokes 712-718 = 62 (B #2); roles (B #1): the c02 [628,644] brass cuts removed (Tbn1/Tbn2/BTbn/Tpt3 -3, Tuba -2), Tbn1/Tbn2 [484,496,+3,2], BTbn/Tuba/Tpt1/Tpt2/Tpt3 [484,496,+2,2], Bn1 [628,644,-4], Bn2 [628,644,-2], Fl1 [484,494,-3], Fl2 [484,494,-2]; Timpani [692,696,+6] (B #2); Cor anglais [586,620,+4] (B #3). `pitch_trims.json` Trumpet 3 B3 (59) +4, all articulations (B #4).

## Stem fix after the render (`stem_fix.py`, level only; master rebuilt as the stem sum)

- Violoncellos: pitch trims on the new strokes as steps (item 4), plus role [512,520,-4, opens over 2 qn]: the triplets and sixteenths of bars 129-130, now Stac strokes, played 5-8 dB louder than the merged note and covered the Clarinet 1 theme by 2-3 dB.
- Horn 1 early fill 201.0 +9 dB from +0.06 s to +0.45 s: the portato join E-flat4 -> C5 (9 semitones, with the 10 CC notch and the C5 pitch trim -5) left a 10-12 dB hole for 0.45 s.
- Timpani: re-strike dips (item 6) and role [711.5,719.5,+5] (the v62 coda strokes still peaked 5-11 dB under the loudest string section; v56 -> v62 had moved them -1.3..+4.9 dB, median +2).
- Violins I/II, Violas, Violoncellos, Double basses: `fit_rebows.py 4` refit of every re-bow shape.
Every other parts.json field was unchanged by these (checked), so the fix is exact.

## Measured before (c03) / after (c04, fixed)

- **Delivery**: master -17.2 -> -17.0 LUFS, LRA 21.4 -> 21.5 LU, sample peak 1.369 -> 1.440 (float stem sum; true peak +3.2 dBFS; the 24-bit render clipped and was replaced by the sum). Delivered -19.7 -> -19.8 LUFS, LRA 15.3 -> 15.5 LU, p10 span 19.9 -> 20.2 dB, limiter 2.7 -> 2.8 dB, -1.6 dBTP. Motion (mp3 dS4 p90 / 1s-20s) 8.78/4.76 -> 8.91/4.81. First render before the fix: LRA 15.6, span 20.4, limiter 2.8.
- **Climax order** (delivered short-term max, LUFS): bar 160 -9.7 -> -9.6, 122 -10.8 -> -10.6, 169-170 -11.8 -> -12.1: order kept. Top master peaks all in bars 160-161 (1.44 at qn 637.9: Violins I, Horn 1, Violas, Trombone 1).
- **A #1 celli bars 127-130** (per written note, 10 ms level max-min, median): bar 128 4.5 -> 3.7, bar 129 3.4 -> 8.2 (target 5), bar 130 1.1 -> 4.7 (target 4). Bar RMS -43.1/-46.8/-40.7/-31.0 -> -44.8/-45.9/-39.7/-29.5 dB (within 2 dB). Clarinet 1 theme now 1-3 dB over the celli per beat in bar 129. Violins II / Violas bars 23-25 per quarter 7.5/6.7 -> 7.0/6.5 dB. New Stac strokes: 2-5 kHz in the first 40 ms minus the rest of the note, median -0.6 dB (p90 +1.0).
- **A #2 Horn 1 portato** (body +0.1..+0.5 s minus the last 0.2 s before): 189 +9.4 -> +8.4, 589 +8.2 -> +7.5, 201 +4.1 -> -1.7 (after the fill; -10.6 before it), 601 +1.8 -> +1.9 dB. The Sus attack peak is gone (189: -47 -> -36 dB in 50 ms in c03; c04 rises -47 -> -41 over 0.15 s and then follows the printed crescendo); the remaining body rise at 189/589 is the hairpin that starts on the tenuto plus the new soft-hairpin ramp, so A's +1..+4 criterion is not met as measured. 201 still dips about 4-5 dB for 0.3 s. Horn 1 over bars 47-52 -37.2 -> -37.6 dB.
- **A #3 / C #4 timpani rolls** (detrended, autocorrelation at the best lag 2.8-4.3 s): centroid qn 0 0.95 -> 0.26, qn 48 0.89 -> 0.46, qn 720 0.92 -> 0.39; 100-300 Hz 0.89/0.90/0.63 -> 0.17/0.48/0.29; control 464 0.79 -> 0.79. Level steps at the re-strikes -1.5..+0.8 dB; mean re-strike bump +2.1 dB -> under +1 dB after the dip. Master, bars 1-4: 100-300 Hz / centroid best autocorrelation 3.2-4.0 s 0.13/0.20 -> 0.10/0.17.
- **A #4 joins and re-bows**: legato joins dipping 6 dB or more 24 -> 17 (Horn 1 201 then filled); per-section worst re-bow dip Vln II -7.3 -> -4.0, Vla -7.6 -> -3.9, Cb -9.0 -> -7.0, Vc -8.0 -> -7.2 dB; master median dip at re-bows -1.6..-2.3 dB.
- **B #1 fff** (plain RMS, not K-weighted): qn 636-644 Tbn1 -25.2 -> -22.2, Tbn2 -28.4 -> -25.4, Tuba -27.7 -> -25.7, Tpt3 -27.7 -> -24.7, Bn1 -24.4 -> -28.4, Vln I -20.3 (melody 1.9 dB over the loudest brass stem); qn 488-492 Fl1 -23.9 -> -26.9, Tpt1 -29.4 -> -27.4, Tbn2 -26.5 -> -23.5.
- **B #2 timpani**: coda stroke peaks -51.8..-59.3 -> -46.7..-49.5 dB against the loudest string section at -42.9..-46.9 (3-6 dB under); bar-174 roll -54.4 -> -48.4 against the violas' -44.3.
- **B #3** Cor anglais minus Violins II over qn 586-620: median -1.4 -> +2.0 dB. **B #4** Trumpet 3 minus Trumpet 2 on B3: -4.0..-8.2 -> -0.1..-1.6 dB.
- **C #1 lead lines**: top note loudest in 3 -> 4 of C's 18 slurs, median top minus rest -0.8 -> -0.3 dB, level/pitch slope -0.12 -> -0.02 dB per semitone; crescendos rising 1 dB or less 13 -> 10 of 26, decrescendos rising 2 -> 2 (Horn 1 596 +2.5 -> +1.3, Vc 196 +3.2 -> +1.9). Every lead slur moved the right way, but by 0.5-1.5 dB, not C's targets.
- **C #2 tempo**: total length +0.65 s (431.95 -> 432.60 s); 113 of 728 beats changed.
- **C #5 bar 41** (master per half beat, beat 1): -17.1/-19.1 -> -15.6/-17.3 dB; bar 26 -12.9; bar 42 -26.7 -> -26.5. Fall in the first beat 1.7 dB, 2.7 dB under bar 26 (target 2).
- **Dan's item 7** (master, autocorrelation at 3.95 s, 100-300 Hz / centroid): final chord -0.12/0.01 -> -0.13/-0.02. **Item 8**: no new accent articulation; the new strokes are not bright (above).
- **Attack probe**: 0 flagged.
- **Memory**: REAPER 20 GB before the render, 41 GB after it with 0 GB compressed. Quit after the render and again after the `--mix-only` update.

## Rejected or deferred

- C #3 (+1.5 dB mf anchor and f trims on every wind, brass, string and harp track): rejected for now. Simulated on the c03 stems with this cycle's data: delivered p75-to-max 10.3 -> 9.8 dB (target 8.5), p50-to-max 14.9 -> 14.7, limiter 2.8 -> 2.5, climaxes 0.2-0.4 dB lower. It moves the distribution a third of the way at the cost of 1.5 dB of the f-to-ff step (c03's reason for rejecting B #6). The gap is in the delivery ride, which lifts only passages under its knee; a ride change or a soft-knee compression of the top 10 dB should be simulated instead.
- A #5 (recorded a2 horn track) and Violins II metà: deferred (a new instance; REAPER peaked at 41 GB, under the 45 GB limit, so one more small instance is possible in a cycle that changes little else).
- A #6 harp étouffez on a "damped" track: deferred (new track).
- C #2 step 2 (Lento and coda arcs): waits for a cycle that refits the re-bows anyway.

## Open for c05

- Horn 1 portato joins: 201 (and 601) as legato targets across 9-semitone leaps leave a hole (201 filled +9 dB, still 4-5 dB); consider listing only 189/589 and returning 201/601 to Sus.
- Phrase tops and soft hairpins are still weak (C #1 targets not met): raise `PT_DB_PER_ST`/`PT_CLIP` or the soft ramp for the violin and cello lines, after measuring which samples sag at the top.
- Timpani qn 48 roll centroid 0.46 (8.4 s split in 3 pieces); the 464/484 rolls (control) still 0.79.
- Bar 41 arrival 2.7 dB under bar 26.
- Celli re-bow 163.877 (bar 41-44) still -7.2 dB dip with a -9 dB step that includes the new sf decrescendo.
- Delivery limiter 2.8 dB (peak 1.44 at qn 637.9, Violins I + Horn 1).
