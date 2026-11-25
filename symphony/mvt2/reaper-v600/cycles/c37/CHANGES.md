# Cycle 37: changes (actor, on the critics' reports of the c36 render)

Snapshot of tools and data before the changes: `before/`. Data the render was made from: `rendered_build/` (parts.json, mix.json, score_config.py before the post-render Flute 1 fix).

## Changes

Tools:
- `tools/score_to_parts.py`: new generic option `WIND_SLUR_REP_MERGE_SKIP = {}` ({track: [score onsets]}): the listed slurred wind repeats are not merged into the note before (the repeat stays its own note, e.g. for a repetition row in ART_SPANS).

Config (`build/score_config.py`, block "c37"):
- A #1 (S1): Flute 1's slurred repeat E flat 5 at 136: `WIND_SLUR_REP_MERGE_SKIP {"Flute 1": [136.0]}`, `MERGE_NOTCH_AT["Flute 1"]` removed, `ART_SPANS["Flute 1"]` 135.95-139.5 on "LegRep RRx4" (re-tongued repetition samples, manual p.109-110). I used LegRep rather than the critic's first choice, Leg Slur Rep over the whole slur: 136 is the slur's last note, so only that note changes row and the rest of the slur keeps Leg Slur MAX. The 135 note now ends 0.06 qn before 136 (same-pitch rule). Opus state changed (new row), so Flute 1 was fully rebuilt.
- After the render: the LegRep note's body played 8-11 dB over the merged note it replaced, so I added a Flute 1 level shape from 136.4 to 139.7 (-3 to -9 dB) that leaves the re-attack alone. Applied by stem fix plus `--mix-only`.
- B #2: Clarinet 1's held ff F5 at 204: a `CC7_POINTS` lane 205-209.9 (127/106/90/80/80/101/113/127), pre-hall.
- B #3: bars 61-62 brass: `LEVEL_SHAPES` +3 dB over 204-211.9 on Horn 2, Horn 3, Trombone 2, Bass trombone and Tuba. Horn 1's c36 shape lift goes from +4.5 to +7.5 (205-207.75), then +3 to 211.6 (the front is still kept off). The c34 string holds are 1 dB lower: Violins I/II 3 -> 2, celli 3.5 -> 2.5 (Violins I and celli end at 211.5 since c35).
- B #4: violas' F4 at 83: `CC7_POINTS["Violas"]` adds (82.93,127), (82.98,64), (83.95,64), (84.05,127), which is -6 dB pre-hall.
- A #2: the basses' coda pedal piece from 273.229: a `LEVEL_SHAPES["Double basses"]` shape fitted to the c36 stem toward -54 dB (+3..+7 on the dips at 273.5-273.65, 274.05-274.15, 274.75-274.85 and 275.12-275.25; -6 on the 275.5-275.65 attack bump). The c34 274.24-274.67 shape is kept. The critic's fill alternative was not used because the 276.05 fill key and the piece's moved point (275.698) do not line up in time.

Per-note tables:
- `rebow_fills.json` Double basses "276.05": the front at -0.12/-0.08/-0.04 s goes from 6.64/5.14/2.31 to 2.0/1.5/1.0 dB (A #2).
- `early_fills.json`: Violoncellos "246" goes from {8.0, pre 0.29, hold 0.35} to {3.0, 0.12, 0.2} (B #1). Violins II "82" removed (B #4).
- `note_trims.json` Violoncellos "246" +4 -> +1 (B #1).
- `roles.json` Flute 1 adds [125.75, 131.5, 3, 0.5] (B #5).
- `entry_leads.json` Violas 152.5/154.5/157.5/161.5: 0.10 -> 0.17 s (A #5).

Mix (`build/mix.json`):
- C #1: the soft-horn `loud_eq` on Horns 1, 2 and 4 goes from highshelf 1.2 kHz -4 to 800 Hz -8. Horn 3 gets the same shelf with Horn 4's points (it had none). Horns 1-2 a2 gets it for bar 82 (271-304). soft_trim ppp/pp/p goes up +1 dB on Horns 1-4 and +1.5 on the a2 track.
- C #2: Harp harmonics width 0.3 -> 0.05 (Opus state, full rebuild).
- C #3: Timpani side shelf 150 Hz -> 300 Hz (-9 dB) and width 0.6 -> 0.3 (Opus state, full rebuild).

REAPER: one `--midi-only` job on 17 tracks. Flute 1, Timpani and Harp harmonics were fully rebuilt (Opus state change). Afterwards `restart`, a 10-minute settle (23 -> 44 GB, flat for 2 minutes, 2.2 GB compressed), `Audio_Init` (48000 / 512 / no input), then `render_cycle.py 37` without `--force-memory`. After the render: the Flute 1 stem fix (`stem_fix.py --apply`, originals in `render_first/`), `--mix-only "Flute 1"`, `save`, `quit`, `unlock`, then `render_cycle.py 37 --measure-only`.

## Rejected or deferred

- A #3 (Cor anglais Leg Slur Exp, MANUAL-GAPS #5): deferred. It is an A/B that needs the entry and legato leads refitted for the slower attack, and this cycle already changes a wind row (Flute 1).
- A #4 / MANUAL-GAPS #8 (basses 4 soli on DIV A): deferred again (memory for a 33rd instance, and a refit of the basses' re-bow fills).
- C #4 (spreading the wind seats): deferred. It needs 11 wind Opus states rebuilt, and every wind level table measured by B would need rechecking. It was the lowest-ranked item in C.

## Measured (c36 -> c37, plain RMS on stems unless stated)

- Master: -20.3 -> -19.9 LUFS, LRA 23.9 -> 23.8, TP -0.8 -> -0.7 dBFS, no clipping. Bars 61/62 -13.8/-14.3, bars 79/80 -19.4/-20.0, so the climax order holds.
- Delivered: -19.8 LUFS, LRA 15.3 -> 15.2, TP -1.5, span 18.3 -> 18.5 dB, limiter 2.0 -> 1.9 dB. The simulation before the render predicted 2.0.
- Attack probe 0 flagged (as c36). Unchanged tracks (Oboe 1, Cor anglais, Harp, Violin I solo) are sample-exact against c36.
- A #1 Flute 1 136: c36 showed a dip (-53.7) inside the vibrato. Now 135.9 -49.9, then the re-attack at 136.0-136.2 reaches -44..-46 (about 5 dB over the 135 note's end). After the fix the body is -47..-49, about 3 dB under the cor anglais.
- A #2 Cb 273.3-276.2: range -62.4..-47.1 -> -57.0..-52.2 dB.
- B #1 Vc 246: 0.1 qn peaks -33.9/-35.5 -> -41.2/-42.0. The body is -44.4 and Violins I -46. The fill's dip at 245.8-246.0 is -46.6..-47.5.
- B #2 Clarinet 1 204.5-209.5: peak -26.7 -> -29.5..-31.2, flat (the swell is gone). The bar mean is -28.9 -> -30.8.
- B #3, 204.2-211.8: Horn 1 -27.9 -> -25.1, Horn 2 -27.5 -> -24.6, Horn 3 -30.9 -> -27.9, Trombone 2 -27.2 -> -24.2, bass trombone -28.7 -> -25.7, tuba -29.9 -> -26.9. Violins I -23.2 -> -24.1, Violins II -23.9 -> -24.9, celli -23.7 -> -24.7. Master -14.6 -> -14.0.
- B #4: Violins II over Violins I at 82.2-82.4 went from +6 to +3 dB. Violas 83 body -38..-39 -> -43.5..-45.
- A #5 violas portato: the -6 dB arrival of 152.5/154.5/157.5/161.5 moved from +0.07 to 0.00 s. The other notes are unchanged.
- C #1 horn 1-5 kHz share: Horn 1 bars 7-10 -16.0 -> -19.9, bars 11-14 -16.6 -> -20.4, bars 67-70 -16.6 -> -20.8; Horn 3 bars 1-6 -13.7 -> -19.2; a2 bar 82 -11.8 -> -17.3. Levels are within 0.2 dB of c36 after the soft trims.
- C #3 timpani: the stem's 120-250 Hz correlation in bars 67-70 went from 0.39 to 0.83 and the master's from 0.39 to 0.46. Roll level -0.5 dB.
- C #2 harp harmonics: 250-4000 Hz correlation over 274-277 went from 0.23 to 0.24. Width 0.05 had no measured effect on this near-pure tone; the image comes from the mic pair's phase, not from the pan.

REAPER memory after the render: 45 GB (19-20 GB compressed). Lock held 07:36:14-08:02:37 (26 min); the wait for the scherzo thread's lock was 07:18-07:36.
