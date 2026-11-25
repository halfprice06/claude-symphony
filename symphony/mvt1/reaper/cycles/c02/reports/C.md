# Cycle 2, critic C: dynamics over time (review of the c01 render)

Lens: the loudness arc of the movement against the score, the shape of hairpins and phrases, the two fff climaxes (bar 122 with the tam-tam and sostenuto bar 123; bar 160 largamente after the cymbal roll), the coda, the delivered mp3's range (BRIEF item 6), loop pulsing and re-bow steps on long notes (item 7), decays, and comparison with the Dvořák 9/i reference.

Method. Master and mp3: ffmpeg ebur128 momentary (M) and short-term (S) loudness at 10 Hz (the mp3 lines up with the master at lag 0, correlation 0.98). Stems: stereo-power envelopes (50 ms hop, 200 ms window), grouped into winds, horns, the other brass, timpani, percussion and strings. Every hairpin of 1 qn or longer in `parts.json`: last third minus first third, on the stem. Loop checks: level, 100-300 Hz band and spectral centroid, detrended, with autocorrelation at 3.95 s and a profile folded at 3.95 s. Level-only changes were simulated on the c01 stems: stem × (10^(dB/20) − 1) added to the master, then a copy of `tools/deliver_master.py` was run. Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c02-C/` (`lib.py`, `grp.py`, `hp.py`, `loop.py`, `sim.py`, `meas.py`, `dm.py`). Times are score time from the `parts.json` tempo map, and bar b starts at qn 4(b−1). "Measured" means taken from the c01 render or `parts.json`; "inferred" means reasoned.

## 1. The main fff (bars 159-161) is no louder than the ff before it and loses its gain after two beats; the sostenuto fff of bar 123 also falls before its printed decrescendo

Where: bars 159-161 (qn 632-644) and bars 122-123 (qn 484-492); all wind, brass and string tracks.

Score: in bar 158 the whole orchestra plays ff. Bar 159 has a crescendo in every part. Bar 160 is fff largamente, and the fff holds through bar 161; bar 162 is ff with a brass decrescendo. Bar 122 is fff tutti with the tam-tam, and bar 123 is a held sostenuto chord at fff; the decrescendo starts only in bar 124 (score page 11, page 15).

Evidence (measured):
- **Master momentary loudness, mean per 2 qn**:

  | | 158 | 159a | 159b | 160a | 160b | 161a | 161b |
  |---|---|---|---|---|---|---|---|
  | Master (LUFS) | −11.5/−11.2 | −10.3 | −9.5 | −9.4 | −11.0 | −10.7 | −12.7 |

  So the fff arrival is only 2 dB over the ff bar, and it falls 1.6 dB at beat 3 of bar 160 and 3.3 dB by the end of bar 161, both still marked fff. The bar-159 crescendo is the weakest tutti crescendo in the movement: 24 tracks, median +1.7 dB on the stems and +1.4 dB on the master. Every other tutti crescendo measures +2.4 to +8.6 dB, for example bar 156 at +6.7 and bar 111 at +8.6.
- **Strings**: as a group they rise only 0.5 dB from bar 158 to the fff and then fall 2.3 dB at qn 638. Violins I and II at the bar 160 fff (Leg BC MAX, the melody) measure −25.8 / −29.3 dB. At the bar 122 fff (Tremolo) they measure −19.2 / −18.4 dB, and at the bar 170 ff they measure −23.1 / −21.5 dB. The melody of the main climax is therefore 6-11 dB under the same sections' other fff.
- **Cause, from `parts.json` `vol_db`**:
  - Every hpgain is released over 1 qn from the first onset after the arrival note (`HP_HOLD_CAP` rule, `score_to_parts.py` lines 2174-2187). At qn 637→638: winds 4 → 0, strings 3 → 0, Clarinet 1 7 → 0.
  - The bar-159 crescendo chains onto the bar 156-157 crescendo. `HP_CHAIN_RISE = {"wind": 0.75}` gives the strings and brass no added dB, so the string gain is 3.0 dB in bar 158 and still 3.0 dB at the fff. CC11 moves 114 → 124, which is about 1.2 dB at the top of the table.
- **Bar 123**: the same release happens at the bar 123 chord change (qn 488).
  - Strings: −14.9 (122a) → −16.6 (123a) → −18.5 dB (123b).
  - Master: −7.2 → −9.3 → −11.2 LUFS M.
  - Part of this fall is the tam-tam decaying, as it should.
- **Reference**: the Dvořák 9/i recording holds its climaxes. The S loudness in the 3.5 s after its peaks at 526 s and 282 s falls 1.1-1.6 dB. The c01 master falls 4.9 dB after the bar 122 peak and 2.2 dB after bar 160.

Fix (config; simulated on the stems as a level-only change):
- (a) `build/score_config.py`: `SOSTENUTO_SPANS = [(484.0, 492.0), (636.0, 644.0)]` and `SOST_HOLD_SHARE = 1.0`. Each fff arrival's hpgain is then held to the span end and released over `HP_REL` into the printed decrescendo or ff. Both passages are marked sostenuto or largamente in the score. Check the span's side effects in the build log: string legato velocity 108 and swell_sost contours on long notes. If any of these is unwanted, add a generic rule that does only the hold: hold an fff arrival's hpgain until the next printed mark or hairpin on that track, capped at 8 qn.
- (b) `HP_CHAIN_RISE = {"wind": 0.75, "string": 1.0, "brass": 0.5}`, or apply it only to chains whose second arrival is fff. Strings then reach +6 dB at qn 636 and brass +3.
- **Simulated on the c01 stems** (strings +3, brass +1, winds held, all held to qn 643 and released by 644.5; bar 123 held to qn 491.5, released by 494; together with fixes 2 and 5):
  - Delivered M, mean per 2 qn:

    | | 158 | 159a | 159b | 160a | 160b | 161a | 161b |
    |---|---|---|---|---|---|---|---|
    | Before | −13.0 | −12.1 | −11.1 | −11.2 | −12.5 | −12.3 | −13.9 |
    | After | −13.3 | −12.0 | −10.5 | −10.2 | −9.9 | −9.9 | −11.6 |

  - Bar 123: −10.7 → −9.7 (beats 1-2) and −12.2 → −11.1 (beats 3-4).
  - The two fff climaxes come out equal: delivered max S −9.8 at bar 122 and −9.9 at bar 160.
  - Limiter 1.9 → 2.0 dB; the new top peaks are at qn 636, 639 and 641.5.
  - With brass +2 instead of +1 the limiter reached 2.9 dB. Keep brass at +1, or notch the loudest join at qn 641.5.

## 2. The coda's ff chord (bar 170) is as loud as the fff climax, because accent swells add to the crescendo gain

Where: qn 672-680 (bars 169-170), every wind, brass and string track.

Score: bars 167-168 are f, bar 169 has a crescendo, and bar 170 is an ff accented chord with a fermata. The only fff marks in the movement are at bars 122 and 160.

Evidence (measured):
- Group levels on the bar 170 chord against the bar 160 fff downbeat:

  | Group | Bar 170 (ff) | Bar 160 (fff) |
  |---|---|---|
  | Brass | −15.1 | −16.0 |
  | Winds | −19.5 | −21.0 |
  | Strings | −17.9 | −19.8 |
  | Master | −12.0 | −12.7 |

- In the mp3 the maximum S of bars 167-170 is −11.5, against −11.3 for bars 160-161: 0.2 LU apart. The bar-170 momentary peak (−7.4 LUFS on the master) is the loudest moment after bar 122.
- Third-highest sample peak of the master: 1.153 at qn 676.2.
- Cause, from `vol_db`:
  - The winds carry hpgain +4 plus the gentle-accent swell +3.5, which comes to +7.5 dB at qn 676.3. The brass get +2 plus +4 = +6 dB.
  - At bar 160 the winds and brass get only +4 and +2 dB, and the strings +3, as at bar 158.
  - Both swells are full at the same time on the arrival note.

Fix:
- Generic, in `tools/score_to_parts.py` (where the gentle swell is set, lines 2552-2561): on a note that is a crescendo's arrival and still carries hpgain, the accent swell adds only max(0, swell dB − hpgain dB). An accent is weight over the surrounding notes, not over the crescendo's gain.
- Or in `build/roles.json`: all wind, brass and string tracks [675.5, 680, −2.5].
- Simulated with −2.5 dB from qn 674 to 680: the coda's maximum S drops to 3.1 LU under bar 160 in the mp3 (−13.0 against −9.9), and the limiter falls 0.4 dB.

## 3. The bar 60-61 string crescendo into the subito p plays as a diminuendo

Where: qn 236-244. Violins I and II, Violas, Double basses, Horns 2-4, Clarinet 1 and Bassoon 2.

Score: mf in bar 60, a two-bar crescendo with no target, then sub. p and poco animando in bar 62 (score page 6).

Evidence (measured):
- Stem change over the hairpin (last third minus first third): Violins I −5.4 dB, Violins II −4.5, Horn 2 −2.4, Violas +0.4, Clarinet 1 +0.2. On the master the change is −1.7 dB, and on the mp3 −1.9 dB.
- It is the only tutti hairpin in the movement that measures backwards.
- Cause: Violins I CC11 rises only from 74 to 80 over the two bars.
  - The c11 look-ahead in `base_points()` (lines 938-948, `nm2`) caps an untargeted swell 8 CC under the next louder mark within 16 qn. Here that is the f at qn 252 in bar 64, after the sub. p, so the crescendo is capped at CC 80.
  - With that cap the hairpin counts as an mf arrival, so the strings get the 2 dB `HP_GAIN_MF_DB` instead of 3.
  - The line also descends from B♭5 to C5, and the violins lose about 6 dB over that range.
- The bar 61 → 62 drop into the sub. p is only 3.7 dB, because the crescendo never rose.

Fix:
- Generic, in `base_points()`: the `nm2` horizon stops at the first mark softer than the current level, or at any `SUBITO` mark. A crescendo whose next mark is a subito p then takes the full `HP_STEP` (72 → 86, so the strings get 3 dB of gain).
- Or, for this passage only, `HP_TARGET_AT` in `score_config.py`: `"VlnI": {236.0: "f"}, "VlnII": {236.0: "f"}, "Vla": {236.5: "f"}, "Cb": {236.0: "f"}, "Hn2": {236.0: "f"}, "Hn3": {236.0: "f"}, "Hn4": {236.0: "f"}, "Cl1": {236.0: "f"}, "Bn2": {236.0: "f"}`.
- Expected (inferred): the violins end the crescendo about 4 dB higher, and the sub. p drop becomes about 7-8 dB.

## 4. The final ppp chord swells about 3 dB in its last 3 s, with all five string sections re-bowing within 0.34 s; Horn 4 pulses at the loop period

Where: bars 181-182 (qn 720-728, 418-431 s).

Score: a decrescendo and morendo through bar 181, then ppp with a fermata ("change bow at will"); Horns 3-4, Trombone 1 and timpani ppp.

Evidence (measured):
- **The swell**: master per 0.25 qn, 200 ms power:
  - Through the morendo it falls in the printed direction: −36.1 (qn 720) → −42.9 (qn 724).
  - Over qn 724-725.75 the ppp holds at −43.0..−44.5.
  - From qn 726.25 it rises to −39.9, −42.5, −40.3, −40.9, −41.2 before the release.
  - Stems: Double basses −55.0 → −48.3..−49.6, Violoncellos −55.6 → −51.7..−50.7, Violas −51.0 → −48.9; Violins I and II +0.5..+1 dB.
- **Synchronized re-bows**: the last re-bows are Cb 726.403, Vln II 726.396, Vc 726.466, Vln I 726.511 and Vla 726.566, which is 427.60-427.94 s. Five sections change bow within 0.34 s, 2.9 s before the end.
  - Their fitted `rebow_fills.json` shapes hold +4.73 (Cb), +2.99 (Vc), +0.78 (Vln I) and +0.59 (Vla) dB to the end of the note.
  - The c26 rule that sections never change bow together is broken here, in the tail where the 30 bpm fermata stretches each qn.
  - Two more clusters: qn 722.60-722.78 (Vln II, Cb, Vln I) and qn 724.78-724.89 (Vln II, Vln I, Cb). At 30 bpm 0.11 qn is 0.22 s.
- **Re-bow dips over the movement** (80 ms window, dip under the 0.5 s before): Violins I median 7.3 dB (4 of 6 dip 5 dB or more), Violoncellos 5.3 dB (17 of 29), Violins II 5.4 dB (9 of 13). The deepest are on the final chord: Vla 726.6 12.1 dB, Vln I 711.9 10.3 dB, Vc 721.8 9.5 dB.
- **Horn 4's ppp held note** (qn 720, 12.9 s, the second-loudest stem in bar 182):
  - Level autocorrelation 0.76 at 3.95 s (best lag 3.90 s, 0.64), folded swing 4.1 dB.
  - 100-300 Hz band 0.77 / 6.5 dB; centroid 0.74.
  - Horn 3, on the same chord, shows none of this (−0.39).
  - Timpani rolls have no loop: autocorrelation −0.15..+0.05 on the 0 s, 484 and 720 rolls.
  - The master over bars 179-182 measures 100-300 Hz autocorrelation 0.09, so there is no section-wide pulse.

Fix:
- **Re-bow times**: list explicit `REBOW_AT` points in `score_config.py` for the bar 179-182 notes of the five string tracks. Space them at least 0.6 s apart across sections, and put no re-bow in the last 3.0 s of the fermata (after qn 726.0). The auto rule keeps listed points. Then refit with `tools/fit_rebows.py` and add the residual, as c01 left open.
- **Re-bow shapes**: for every re-bow after qn 720, clamp the fitted hold offset to at most 0 dB, so the shape can only follow the morendo, never rise against it. In `fit_rebows.py` that means a per-note upper clamp: use 0 instead of +9 when the printed dynamic curve falls or holds at ppp.
- **Horn 4**: put an inverse loop profile in `build/loop_profiles.json` for the qn 720 note, using kit LEARNINGS section 6: fold at 3.90 s, apply from the start + 0.8 s to the end − 0.3 s, clamp ±3 dB.

## 5. The delivered span is still 20.4 dB, and the mf cello fugato (bars 85-88) sits as low as the pp introduction

Where: the whole delivery; bars 85-90 (qn 336-360).

Evidence (measured):
- **Delivered c01 figures**: LRA 16.0 LU (the edge of the 14-16 target), p10-to-max span 20.4 dB (target 16-19), limiter 1.9 dB.
- **Direction kept**: 0 inversions among the 2,584 five-second moves of 3 dB or more, and a median of 83% of each move kept.
- **Frames under the delivered p10**:
  - The introduction (bars 1-5 and 14): ride +4.8..+7.7 dB, not at the cap.
  - The mf fugato, bars 85-88.
  - Bars 107-109 (pp/p).
  - Bars 127-128.
  - Bars 154-155.
  - The final chord and its tail (bars 181-183).
- **The fugato**:
  - Master S medians in bars 85-88: −35.7, −36.7, −38.2, −36.4. The mp bars 172-174 measure −30.8..−33.5, and the pp final chord −36..−40.
  - Fitting bar level against the loudest printed CC11, bars 85-88 are −7.3..−11.9 dB under the fit, the largest negative residuals in the movement among bars without stale marks.
- **Ride ratio, simulated on the c01 stems with fixes 1-3**:

  | Ratio | Delivered LRA | Span | Inversions | 5 s moves kept |
  |---|---|---|---|---|
  | 2.0 (current) | 15.6 LU | 20.5 dB | 0 | |
  | 2.5 | 14.9 LU | 19.7 dB | 0 | 82% |
  | 3.0 | 14.3 LU | 18.9 dB | 6 | |

  With ratio 2.5 the limiter stays at 2.0 dB and the climaxes keep their order. Ratio 3 must not be used, because of the inversions.

Fix:
- `build/roles.json`: Violoncellos [336, 358, +3], Double basses [336, 358, +3], Violas [348, 358, +3], Bassoon 1 [348, 358, +3]. Release them before the crescendo into the f of bar 91. Simulated: p10 +0.4 dB, with the fugato in line with the other mf passages (inferred).
- `tools/deliver_master.py`: `RATIO` 2.0 → 2.5. Simulated span 19.7 dB, LRA 14.9 LU, no inversions.
- The remaining 0.7 dB of span is the ppp introduction and the final chord. Give the introduction's exposed solo lines the kit's +2..+3 dB solo lift (cor anglais bars 6-9, horn bars 12-14) rather than lifting the ppp itself.

## 6. The coda cello solo plays its phrase backwards: the first note is 8-11 dB over the printed crest

Where: Violoncellos, bars 171-174 (qn 680-696), mp espr., the c01 open item "Vc bar 171 loud".

Score: mp. A < to the c01 `HP_TARGET_AT` mf at qn 683.5, then >; < > in bar 172; a < into the C5 crest at bar 174 (target mf at qn 691), then > (score page 17).

Evidence (measured):
- Vc stem per qn, 680 → 695: −31.7, −28.4, −30.1, −35.7, −40.6, −36.8, −34.1, −38.1, −36.4, −38.8, −39.6, −42.2, **−39.5** (the crest, C5 at qn 692, CC11 70), −40.0, −42.2, −40.7.
- The first E♭4 (qn 680, CC 63-74) sits 8-11 dB over the bar-174 crest, at the same printed mf. The phrase falls 10 dB from bar 171 to bar 174.
- The cor anglais imitation (p, qn 683-694) measures −39..−45 dB, so in bar 171 it is about 10 dB under the cello and level with it by bar 174.
- `note_trims.json` has nothing on this note. Inferred: the bloom of the first note on its first-note layer, as at the opening pickup (qn 3, trimmed −8 dB in c01).

Fix:
- `build/note_trims.json` "Violoncellos": add "680.0": −6. Use the default 0.6 s ramp: the note is a crescendo start, not a join (kit section 4 asks for a step on crescendo notes only when the note sags).
- Then raise the crest: `roles.json` Violoncellos [690.5, 694, +2, release 2] with the gain released across the printed decrescendo. Target: the bar-174 crest 2-3 dB over the qn 681-682 crest.
- Re-measure the cello against the cor anglais afterwards: the cor anglais should stay 2-4 dB under the cello, not 10.

## Do not touch

- The subito handling (bar 62 −3.7 dB, cello bar 84 −9 dB).
- The bar 124-126 decrescendo: −10.0 dB on the master, −8.4 on the mp3, the largest and cleanest in the movement.
- The bar 111-120 crescendo arc (+8.6 dB).
- The suspended-cymbal timing into bar 160 (key 64, lead 0.45 s).
- The delivery chain's structure: 0 inversions, climaxes kept.
- The timpani rolls: no loop at the 3.95 s period.
- The master peak at the bar-122 downbeat, which sets the limiter. Do not raise the bar-122 downbeat; fix 1 raises only bar 123 and bar 160-161.
