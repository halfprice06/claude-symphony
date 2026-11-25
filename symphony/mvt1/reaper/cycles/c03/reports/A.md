# Cycle 3, critic A: articulation and phrasing (render c02)

Scope: every wind, brass, string, timpani, harp and percussion note in `build/parts.json` (the c02 build), measured on the c02 post-fader stems and master (stereo power), with `cycles/c01/render` and `cycles/c02/before/parts.json` for comparison. Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c03-A/`: lib.py (critic A's c02 library), lag2.py, onsets2.py, rbplan.py, rebow4.py, finalrb.py, longloop2.py, strlong.py, trem.py, accs.py, accshape.py, accpre.py, rep.py, stac.py, joincat.py, xo.py, kscheck.py.

## Checks that passed (measured)

- **Accents.** 2-5 kHz energy over the first 80 ms minus the note body has these per-track medians:
  - strings -5.7..-9.6 dB;
  - brass -5.2..-10.7 dB;
  - winds -6.1..-12.8 dB.
- **Accent weight.** Each accent sits a median +2..+6 dB over the note before it. Only Horn 3 qn 317/321 (+1.7/+2.2 dB) and Violas 536 (+0.4, the open merged-legato case) have a 2-5 kHz attack over their body.
- **Legato structure.** Median join dips are 2.2-3.7 dB in every family. `ks_clash` is empty on every track, and no chord reaches a legato row.
- **Keyswitches.** Every keyswitch sits 24-29 ms or more before its note.

## 1. The whole render runs about 1/6 quarter note ahead of the parts.json time map, so every shape fitted from audio lands early (all tracks; worst in the Lento)

**What is wrong (measured).**
- Every tool that reads audio (`fit_rebows.py`, `auto_fills.py`, `fit_loops.py`, `measure.py`, `probe_attacks.py`) converts score qn to file seconds with the parts.json tempo map. In the rendered files, notes and envelope changes both arrive earlier than that map says.
- **Note onsets** (`onsets2.py`; first 4 ms frame at peak - 15 dB, isolated strokes):

  | Instrument | Where | Onset vs map |
  |---|---|---|
  | Timpani | q=126, 15 strokes | -0.080 s (0.168 qn) |
  | Timpani | q=50, qn 712-717 | -0.200 s (0.167 qn) |
  | Harp | q=112 | -0.09 s |
  | Harp | q=100 | -0.098 s |
  | Basses pizz. | | -0.08 s |
  | Tam-tam | 696, q=72 | -0.12 s |

- **Envelope changes** (`lag2.py`): 274 c02-minus-c01 envelope changes, measured on the stems against the planned change, best-lag correlation 0.95-1.0.
  - The lead fits 0.022 s + 0.165 qn, with a residual sd of 0.004 s.
  - That is 0.10 s at q=126, 0.12 s at q=100, 0.16 s at q=72, 0.22 s at q=50 and 0.35 s at q=30.
- So the c02 CHANGES "envelope lead" is not an envelope fault. Notes and envelope move together, within about 0.02 s.
- The attack probe cannot see this: it searches only after the score onset, so an early note reads +0.00 s.

**Consequences (measured).** Any fitted correction is written at the time where the feature was measured, and it then renders 1/6 qn before that feature.

- **Re-bow fills.** At Violoncellos qn 37.37 (bar 10) the planned fill rises 10 dB at the re-bow.
  - The stem peaks 0.25 s before the re-bow (-28 dB) and dips to -43.6 dB at +0.3 s.
  - The plan's own dip at +0.55 s shows in the stem at +0.33 s.
- **Refits.** Each refit chased the previous misplacement.
  - The Violoncellos 25.39 shape now swings +17 / +2 / +16 / +1 / +10 dB within 1.1 s.
  - The stem shows the same pattern 0.2 s earlier.
  - The intro celli re-bows still dip 13.3 dB (25.39) and 11.5 dB (37.37) on the stem, and 3.2/4.5 dB in the master.
  - Celli re-bow steps of 3 dB or more: 11 of 29.
- **Loop profiles.** The c02 timpani and Horn 4 profiles made the pulse worse, for the same reason.
- **The "inaudible" tie stroke at qn 46 is there.**
  - The stroke peaks at -31 dB against a roll at -36 dB, at qn 45.87, 0.2 s before q2s(46).
  - Each Timpani stroke's CC7 rises 51 -> 64 and its keyswitch sits at 45.94.
  - The c02 measurement looked 0.2 s too late.
- **Leads (inferred).** All lead tables were tuned to crossovers measured against the shifted map, so slow attacks sit 1/6 qn behind the fast ones.
  - In the Allegro the Violins I legato crossovers measure +0.013 s against the map (`xo.py`), and the timpani and pizz. strokes -0.08 s.
  - So the violins' legato arrives about 0.09 s after the percussion.

**Fix.**

1. **Find the cause with one bridge read-back job** (no render).
   - For the Timpani take, read the note at score qn 100 and the one at 712 with `MIDI_GetProjTimeFromPPQPos`, and one volume-envelope point near qn 100.
   - Subtract `pre_sec` and compare with q2s(100) and q2s(712).
   - If REAPER's positions equal q2s, the shift happens at render (inferred: inside Opus or the render path), and the measurement side must carry it.
2. **Until the cause is removed, put one shared time function in every audio reader** (`fit_rebows.py`, `auto_fills.py`, `fit_loops.py`, `measure.py`, `probe_attacks.py`, `stem_fix.py` if it maps envelopes to samples):
   - `file_s(q) = q2s(q) - (RENDER_LEAD_S + RENDER_LEAD_QN * 60 / bpm_at(q))`, with `RENDER_LEAD_S = 0.022` and `RENDER_LEAD_QN = 0.165`.
   - Put both constants in `build/score_config.py` so a later measurement can change them.
   - Make `probe_attacks.py` search from `file_s(q) - 0.3 s`, so an early note is reported.
3. **Refit `build/rebow_fills.json` with `fit_rebows.py` on the c02 stems with the corrected map.**
   - Its "remove the old shapes" step must use the corrected map too.
   - Then rerun `auto_fills.py 2` the same way.
4. **Do not shift the lead tables in this cycle.**
   - They are relative to the shifted grid, and a cut of 0.08-0.2 s would need its own measured cycle.
   - Record the bias in `loop/LEARNINGS.md`.

**Pass criteria.** In the next render:
- the c03-minus-c02 envelope change shows a best lag of 0.00 ± 0.02 s against the plan at q=50 and q=126;
- the celli intro re-bows (25.39, 37.37) dip 6 dB or less on the stem;
- celli re-bow steps of 3 dB or more fall to 5 or fewer of 29.

## 2. The final chord changes bow in all sections at once (bars 181-182, "change bow at will")

**Where.** Qn 712-728, Violins I/II, Violas, Celli, Basses.

**What is wrong (measured, `finalrb.py`).** `AUTO_REBOW` gives each track its own phase but does not look at the other tracks. On the final chord the re-bows of different sections bunch together:

| Qn | Sections | Spread | Master dip |
|---|---|---|---|
| 722.60 / 722.67 / 722.78 | Vln II, Cb, Vln I | 0.21 s | 4.0-4.9 dB |
| 724.78 / 724.80 / 724.89 | three sections | 0.22 s | 2.0-2.4 dB |
| 725.20 / 725.21 | Vla, Vc | 0.03 s | 2.6-2.8 dB |
| 726.40 / 726.40 / 726.47 / 726.51 / 726.57 | all five sections | 0.34 s | 2.5-5.2 dB |

- Master dip at the 30 re-bows after qn 704 (80 ms window): median 2.6 dB, p90 4.5 dB.
- At 300 control times more than 0.6 s from any re-bow: median 2.0 dB, p90 3.7 dB.
- Stem dips at these points are 8-13 dB, with steps of -5.5 to -6.9 dB on Violas 725.2 and Violins II 722.6 and 724.78.

**As heard (inferred).** The ppp chord swells and sags together at those moments, the coordinated bow change that "change bow at will" exists to prevent. This is the last sound before the attacca.

**Fix** (`tools/score_to_parts.py`, after all tracks are built):
- Add a cross-track pass, `REBOW_MIN_SEP_S = 0.6`.
  - Sort every string track's automatic re-bows.
  - When two re-bows of different tracks fall less than 0.6 s apart, move the later one later by the shortfall.
  - Keep every piece between 1.8 and 4.5 s. If the move would break that, move the earlier one earlier instead.
  - Never move a re-bow listed in `REBOW_AT`.
- Alternative: list explicit `REBOW_AT` times for the five sections from qn 712 in `build/score_config.py`, at least 0.6 s apart.
- The moved re-bows lose their fitted shapes (keyed by onset), so refit them with the corrected map of finding 1.

**Pass criterion.**
- No two sections re-bow within 0.6 s after qn 704.
- Master dip at the re-bows is within 0.5 dB of the control median.
- Master 100-300 Hz and centroid autocorrelation at 3.95 s stays under 0.3 over qn 712-728.

## 3. The timpani rolls pulse at their sample loop; the opening roll is exposed

**Measured** (`longloop2.py`): the 80-4000 Hz level and spectral centroid of each note over 6 s, detrended. Autocorrelation is the maximum over lags 2.8-4.3 s.

| Note | Length | Level | Centroid | Swing | Level vs master |
|---|---|---|---|---|---|
| Timpani, opening roll, qn 0-16 | 19.2 s | 0.85 at 3.5 s | 0.95 | 4.3 dB | -9.4 dB (the first sound of the movement) |
| Timpani 48, bars 13-14 | | 0.91 | 0.97 | | -17 dB |
| Timpani 484, bars 122-126 | | | 0.99 | 12.5 dB | |
| Timpani 720, final roll | | | 0.94 | 5.7 dB | |
| Horn 4 qn 720 | 12.9 s | 0.38 | 0.81 | 7.8 dB | -11.3 dB |
| Bass clarinet 492, bar 124 | | 0.70 | 0.94 | 9.3 dB | -13 dB |

The c02 profiles failed because of finding 1, not because the kit method is wrong: mvt II c26 took two timpani rolls from 4.2 to 1.0 dB and from 2.6 to 1.1 dB.

**Fix.**
- After the time map is corrected, refit `build/loop_profiles.json` with `fit_loops.py` for these notes:
  - Timpani 0, 720, 484 and 48;
  - Horn 4 720;
  - Bass clarinet 492, with period 3.45 s (centroid).
- Use the measured periods, ±3 dB clamp, and `vol_db` removed before folding.
- A level profile cannot remove the colour cycle (kit LEARNINGS 6). If the opening roll still has centroid autocorrelation over 0.5, test re-striking it in a later cycle: new Rls notes at irregular 2.4-3.2 s spacing, with no same-pitch overlap.

**Pass criterion.** Level swing 2.5 dB or less and level autocorrelation under 0.3 on Timpani 0 and 720.

## 4. Violins II "div. sul tasto" tremolo plays as an ordinary, bright tremolo (bars 147-155, qn 584-619)

**What is wrong (measured, `trem.py`).**
- The tremolo rule comes before the sul tasto rule in the string branch (`score_to_parts.py` around line 1180), so the mark has no effect.
- The Hollywood Strings 2nd Violins folder has no sul tasto tremolo patch: only `Trem`, `Meas Trem TS` and `Flautando`, which is not a tremolo.
- Measured brightness (2-6 kHz minus 250-1000 Hz):
  - this pp passage, CC11 35: -3.1 dB;
  - the other Vln II tremolo passages at mf/f: -7.7..-7.9 dB (qn 144, 304, 440).
- So the passage marked to be the softest and darkest is the brightest tremolo in the movement. Part of that is register (A5-B♭5 on top; inferred).

**Fix.**
- In `build/mix.json` "Violins II", add a `loud_eq` list entry (one more wet ReaEQ through `mute_lua`): points `[[583.9, 0], [584, 1], [618.8, 1], [619, 0]]`, bands `highshelf 2500 Hz -7 dB` and `bell 1200 Hz -2 dB bw_oct 1.5`. This is the horn-mute method of kit LEARNINGS 3.
- Raise the level role over 584-619 by about +2 dB if the passage then falls more than 2 dB under its c02 level. This is `--mix-only`; no patch reload.

**Pass criterion.** 2-6 kHz minus 250-1000 Hz at -9 dB or lower over qn 588-616, with level within ±1.5 dB of c02.

## 5. Woodwind staccato still speaks 0.05-0.08 s after its string doubling (development, bars 87-96)

This is c02-A #5, deferred twice.

**Measured** (`stac.py`, peak time after the onset):
- Winds, printed staccato played as Sus MAX at half length: Cor anglais 0.128 s, Bassoon 1 0.095 s, Clarinet 1 0.245 s, Oboe 1 0.065 s, Flute 1 0.050 s.
- Strings on their Stac rows: 0.028-0.050 s.
- Both sit on the same shifted grid, so the comparison holds.

**Fix as a contained test.**
- Play only Bassoon 1's staccato notes (bars 87-89, qn 348-359, doubled by the violas) on `Stac DblTng RRx9` (BS KS Master key 28) at the Sus velocity +10.
- The Cor anglais passage (qn 362-371) stays on Sus MAX as the control.
- This is a full rebuild of one track only.

**Pass criterion.** Bassoon 1 staccato peak time within 0.04 s of the violas' median, and level within ±2 dB of the c02 Sus notes. If it passes, extend it to the Cor anglais, Flute 1, Oboe 1 and Clarinet 1 next cycle.

## 6. The repeated ff bass eighths blur into a held tone (bars 27-31, 82, 131-134, 140-142, 167-170; 122 notes)

**Measured (`rep.py`).**
- The Double basses play these unmarked same-pitch eighths on Sus MAX, each note 0.22 s long with a 0.02 s gap.
- The level rise at each re-attack is a median 3.9 dB, p10 2.1 dB.
- Bar 30 measures 1.7 dB and bar 29 3.3 dB.
- The trumpets' repeated eighths at bars 27-30 rise 1.2-1.4 dB (Tpt 2/3).

**As heard (inferred).** The motor rhythm under the first theme's ff tutti loses its pulse. Real basses re-articulate each eighth with a fresh bow stroke.

**Fix as a test.**
- Play Double basses bars 27-28 (qn 104-112) on the Basses KS Master `Marc Shrt RRx4` (key 77) at full written length.
- Bars 131-132 are the control.
- This loads one row, so it is a full rebuild of the Double basses track.

**Pass criterion.** Re-attack rise of at least 6 dB median, with the bar's mean level within ±2 dB of c02.

## Smaller items (not ranked)

- **Harp étouffez is not implemented** (no rule reads the text).
  - At qn 244 (bar 62, sub. p) the f chord of qn 242 still sounds at -41..-46 dB under the p arpeggio (-44..-47 dB). It falls only 8 dB in 0.5 s.
  - Fix: a -12 dB volume step on the harp, 0.05 qn after the étouffez mark, released at the next note-on. Apply it at qn 244 and 654.
- **Violins II "metà"** (qn 184-196, held A♭4 under the horn solo) still plays on the full section, as do the Violas' "div." chords. Use the 2nd Violins DIV A patch when the memory allows (c01 A5).

Do not touch: `GENTLE_ACCENT` for brass, winds and strings; `STR_ACC_AFTER_SUS`; `DETACH_ACCENTS`; `SHORT_SUS_TO_LONG`; `AUTO_REBOW` piece lengths (only add the cross-track spacing); the legato structure and keyswitch placement; the string Stac and pizz. rows; `TIMP_TIE_STROKES` (the qn 46 stroke works; see finding 1); the suspended-cymbal timing.
