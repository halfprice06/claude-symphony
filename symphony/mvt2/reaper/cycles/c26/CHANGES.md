# Cycle 26 changes (actor)

Snapshot of the c25 tools and data: `cycles/c26/before/`. Session: fresh `-new` open, `--midi-only` update of 13 tracks; Trombone 1, Violins I and Violins II were fully rebuilt because their Opus states changed (Trombone 1 no longer plays Sus Accent MAX, so that row is unloaded; Violins I/II now load Sus MAX). Then save, quit, fresh `-new` open, one render. No tempo change.

After the render, two gain-only fixes (volume envelope shapes only, applied to the stems, master rebuilt as the stem sum, which matched the rendered master to 8e-7 before the change; metrics, attack probe, mp3 and motion figures regenerated; REAPER updated with `--midi-only` for the six tracks and saved). The first render's master, the six changed stems, metrics and mp3 are in `/private/tmp/claude-501/mockup-loop/c26-actor/render1/`.

## Memory (BRIEF rule 7)

| | REAPER memory | compressed |
|---|---|---|
| fresh open, at render start (still loading) | 24 GB | 0 GB |
| settled and after the render | 44 GB | 0 GB |
| after the post-render `--midi-only` update, before quitting | 45 GB | 34 GB (macOS compressed the idle process during the analysis) |

The added Sus MAX rows on Violins I/II cost no measurable memory (c25: 44 GB). REAPER was saved and quit at the end.

## Accepted

### BRIEF item 8: the final chord's "bowing effect" (A #1, C #1)
Measured on c25: each string section held one sample for 15-25 s, so the 3.93-3.97 s sustain loops of four sections ran in step (master 100-300 Hz loop autocorrelation 0.58, centroid 0.39), plus CC11 bow notches at 289/292 (Vln II) and 295/298/301 (Vln I).
- `tools/score_to_parts.py` `REBOW_AT` (A's staggered list; Vln II starts from its printed 289 note): the held final notes are split at the output stage into same-pitch pieces. The first piece ends `REBOW_GAP_QN` 0.03 qn early, each new piece is `Sus MAX` at v41 with no lead, and the keyswitch sits 0.02 qn before it. CC11, CC1 and the volume envelope stay those of the held note. A first version split the notes before the controller code; each piece then took its own long-note swell and entry shape (CC11 rising 32 -> 40 at every re-bow), so the split was moved to the output. Sus MAX, not Leg Slur MAX, because a same-pitch re-attack on the legato patch plays its slow first-note layer (c03: 7-15 dB holes).
  - Violins I 295, 298, 301, 302.75. Violins II 289, 290.9, 293, 295.8, 297.6, 300.2, 302.2, 303.4. Violas 294.1, 296.9, 299.2, 301.5, 303.1. Violoncellos 293.6, 296.3, 298.6, 300.6, 302.35. Double basses 294.5, 297.2, 299.8, 302.0, 303.3 (A's 303.35 moved 0.05 qn away from Vln II 303.4). Pieces 1.8-4.5 s; the closest two re-bows of different sections are 0.25 s apart.
- `NOTCH_SKIP`: the CC11 notches at Vln I 295/298/301 and Vln II 289/292 are removed.
- `build/loop_profiles.json`: the five final-chord entries (Vln I/Vla/Vc/Cb 292, Vln II 286) removed.
- `JOIN_NOTCH` (C #1 fix 2, at about half of C's dB, because removing the 292 profiles already raised the trough by 1.5-4 dB in a simulation on the c25 stems): Violas (292.62, 292.98, +2.5), Violoncellos (292.60, 293.00, +3.0), Double basses (292.48, 292.95, +3.0).
- **Post-render fix 1, `build/rebow_fills.json`** (new; read by `score_to_parts.py` `REBOW_FILLS`). On the first render each Sus MAX re-bow dipped 6-15 dB on its stem for about 0.9 s (soft attack), and several pieces settled 3-9 dB away from the level before them (Sus MAX bodies differ from the Leg Slur sustain at the same CC11). For each re-bow a level shape was fitted on the first-render stem (`fitfill2.py` in the scratch folder; method in the file's `_doc`): over the first 1.5 s it follows the pre-re-bow level minus the morendo that c25 played over the same span, then holds the offset until the next re-bow (or to the release). Clamped -6..+9 dB.
- **Post-render fix 2, `build/roles.json`**: [292.5, 304] Violas -3.5, Double basses -4.0, Violins II +2.5. Removing the profiles and chaining the shapes had moved the sections' chord means by +3.9 / +4.6 / -2.8 dB against c25; these rows put them back within 0.6 dB of c25.
- Smaller (A): `score_to_parts.py` holds each track's vol_db at its value at the last release (END) after it. `build_reaper.py` already held the envelope after a track's last note (c19 tail hold), so this only makes parts.json agree with the envelope.

### BRIEF item 9: Trombone 1's accents at bars 63-64 (A #2, B #3, C #2)
- `ACCENT_ART_AT` Trombone 1 212.5/213/218: Sus MAX instead of Sus Accent MAX (no lead, as before).
- `ACCENT_BUMP_AT` Trombone 1: 0 (CC11 stays at the ff 114 and the decrescendo's own values; it was 122).
- `VEL_SET` 108/105/110 -> 96/96/92.
- `ACCENT_DB_AT` with `ACCENT_SWELL_S_AT`: a swell in seconds (0 at onset - 0.01 qn, full at +0.07 s, held to +0.25 s, 0 by +0.6 s). First render +3.0/+3.0/+2.5 dB; 212.5 and 218 then sat only +1.2 and -1.8 dB against the marcato eighths' bodies, so post-render fix 3 raised them to +4.5/+3.0/+6.0 (gain only).

### Other
- B #1 Clarinet 1 292: note trim +3 and its 3 s ramp removed (`note_trims.json`, `NOTE_TRIM_RAMP_S`).
- B #2 bar 81: `HP_TARGET_AT` {Hn3, Hn4: {268: "p"}} (new; an untargeted hairpin goes to the listed dynamic): Horns 3-4 CC11 87 -> 46 instead of 87 -> 74. `roles.json` Oboe 1 [268, 271, 4] removed.
- B #4 bar 30: Horns 3-4 [86, 90, -3] -> [86, 90, -5.5].
- C #3 coda: the six accompaniment rows [283.0, 291.5, -2.0, 0.5] -> [282.25, ...]; Double basses [274, 286, 2] -> [274, 282.5, 2].
- A #3 timpani: `loop_profiles.json` "Timpani" 226 (2.93 s) and 292 (3.12 s), fitted by me on the c25 Timpani stem with the c17 method (`timpfit.py`), corr clamped -3..+3 dB.

## Rejected or deferred
- A #1 second step (CC1 56 on the final chord, Sus Vib alone): not needed this cycle; the loop correlation fell without it. Keep in reserve if critics still hear a cycle.
- C #1 fix 1 as written (Vln II merge notches at depth 3): superseded; the re-bows replace the notches.
- C small item, `_all` morendo -3 -> -4.5: not done (`deliver_master.py` and the morendo rows are do-not-touch; the mp3 morendo is 8.7 dB).
- Open from c25 (not done): Cb F2 pitch trim; Fl1/Bn1 reproducibility; Vln I 72/74/240/252 spikes; Hn1 27.

## Measured (c25 -> c26, final files)
- Master: -22.6 -> -22.6 LUFS, LRA 23.6 -> 23.6 LU, TP -4.2 -> -4.1 dBFS, sample peak 0.616 -> 0.626. No clipping.
- mp3: -19.8 -> -19.8 LUFS, LRA 16.0 -> 16.0 LU, TP -1.6 -> -1.7 dBTP, span 18.5 -> 18.5 dB, limiter 1.6 -> 1.7 dB.
- Motion: master dS4 p90 5.71 -> 5.87, 1 s/20 s 3.80 -> 3.80; mp3 5.06 -> 5.19, 2.87 -> 2.87.
- Attack probe: 3 of 21, the same three as c24/c25 (Vln I 171 +0.34 s; Vln II/Vc 212 holes 6.9/6.2 dB). All 33 files present.
- Item 8, final chord (critic A's `fold.py`/`mcent.py`, qn 292.6-303):
  - Master 100-300 Hz: the loop period is gone. c25 best period 3.94 s with autocorrelation 0.58; c26 best period 1.68 s with 0.24. Folded at 3.96 s: 5.0 -> 4.2 dB p2p.
  - Master spectral centroid: autocorrelation at its best period 0.39 (3.94 s) -> 0.19 (4.08 s). Swing 655 -> 1013 cents (more irregular movement, no period).
  - The 100-300 Hz band's residual p2p rose 4.8 -> 7.1 dB.
  - Re-bow dips (`rebow.py`, -0.1..0.6 s against -0.45..-0.1 s): first render, stems -6..-15 dB, master median -3.0 dB (c25 control at the same times -1.9). After fix 1, the median profile per section stays within 0..-2 dB of the pre-level; the master median is -2.3.
  - Section means over 292.5-303.5 (c25 / c26): Vln I -52.5 / -51.7, Vln II -53.0 / -53.3, Vla -54.8 / -54.3, Vc -52.7 / -53.1, Cb -54.9 / -54.3.
- Item 9, Trombone 1 (A's `tbn.py`; 212.5 / 213 / 218):
  - 2-5 kHz attack (0-80 ms) minus body: +6.9 / -0.9 / +12.7 -> -0.8 / -3.2 / -9.4 dB.
  - Tbn1 2-5 kHz over the strings in the attack window: -3.2 / +2.7 / +7.9 -> -26.0 / -4.8 / -18.1 dB.
  - Master 2-5 kHz jump at the attack: -3.1 / +1.9 / +10.1 -> -4.3 / -0.7 / +2.1 dB.
  - Bodies -23.9 / -22.8 / -25.2 -> -23.5 / -22.2 / -25.2. The marcato eighths' mean body is -26.1, so the accents are +2.6 / +3.9 / +0.9 over it (218 is +1.5 over its neighbours at 217-217.5).
  - The first 60 ms now sit 2-10 dB under the body (Sus MAX speaks more slowly than the accent sample). The probe still reads Tbn1 212.5 as on time (+0.04 s).
- B #1 Cl1 (plain RMS, 292-293.5 / 293.5-295 / 295-296): -45.8 / -48.2 / -51.8 -> -46.6 / -50.9 / -54.8. It now falls through the bar: 4.6 dB over Vln I, then 0.4 and 2.9 dB under it.
- B #2 bar 81 (0.5 qn, 268.5 ... 270.5): Hn3 -44.3 / -40.0 / -41.1 / -41.5 / -40.0 -> -44.4 / -41.3 / -43.3 / -45.5 / -44.4; Hn4 -36.5 ... -38.1 -> -37.4 ... -42.9; Ob1 4 dB lower throughout. Fl1/Vln I unchanged.
- B #4 bar 30: Horns 3-4 -2.5 dB at 87.5-89.5; violins unchanged.
- C #3 coda (283-284 -> 285.5-286.5): Violas and Violoncellos unchanged (-63.2 -> -53.3, -52.1 -> -48.5). Double basses -56.1 / -55.1 -> -58.1 / -56.5, so the rise is +1.6 instead of +1.0. The fix had no measurable effect on the violas and cellos.
- A #3 timpani loop pulse (stem residual 5-95% range, 3 s detrend): 226-237 4.2 -> 1.0 dB (autocorrelation at the period 0.99 -> 0.75); 292-303 2.6 -> 1.1 dB (0.92 -> 0.53).
