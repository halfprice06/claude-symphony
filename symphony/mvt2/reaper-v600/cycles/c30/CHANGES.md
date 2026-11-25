# Cycle 30 (actor): brass and clarinet dynamics on CC1, plus seven small fixes

Critic reports: `cycles/c30/reports/A.md`, `B.md`, `C.md` (on the c29 render). Snapshot before any change: `cycles/c30/before/`. Data the render was made from: `cycles/c30/rendered_build/`. First-render stems and metrics: `render_first/` (the 12 stem-fixed stems), `metrics_first/`. Measurement scripts: `cc1meas.py` + `lv.py` (per-note body level and 1-5 kHz share by printed dynamic, old render against new); result table `cc1_levels_by_dynamic.txt`.

## Main change: MANUAL-GAPS #1 (loop/ONE_TIME.md; B #5)

- Patch check (`opus_state.load_oib`, read 2026-11-06): in `1FH`, `2FH`, `1TB`, `1TU` KS Master and `CL KS Master` every sustain and legato layer group (`1FH pp/mf/f/ff`, `2FH pp/mf/f/ff`, `1Tb p/mp/f/ff`, `Tu pp/mf/f/ff`, `Cl p/mp/f`) has a `cc 1` MidiController feeding its Source volume through a rescaler table; the only CC11 controller is on the Global Group. Example, 1FH Sus (CC1 0/30/50/70/90/110/127): pp 1.0/0.59/0/0/0/0/0, mf 0/0.45/1.0/0.62/0.06/0/0, f 0/0/0.14/0.68/0.91/0.28/0, ff 0/0/0/0/0.38/0.82/1.0. The ff group also has a CC1->filter frequency table. `CB KS Master`: CC11 crossfades p/mp/f, and CC1 crossfades Non Vib (1.0 to 60, 0 by 80) and Vib (0 to 40, 1.0 from 70).
- `build/score_config.py` (c30 block): `CC1_DYN_TRACKS = ("Horn", "Trombone", "Bass trombone", "Tuba", "Clarinet ")` ("Horn" covers Horns 1-2 a2), `CC1_HOLD = {"Contrabassoon": 40}`, generic `CC1_DYN_MAP`. CC1 on these tracks went from 53-87 to 18-108.
- Measured on the first render against c29 (note bodies, envelope unchanged on these tracks; bass clarinet and Oboe 2 controls read exactly 0.0 dB):
  - Level: horns pp -8.3..-10.6 dB, p -3.5..-6.1, mp -4.7..-5.1, mf -0.4, f +1.4..+2.6, ff +0.4..+2.8; trombones/tuba pp -0.6..-3.0, p -4.3, f +1.6..+2.5, Trombone 1 ff +2.8; clarinets pp -3.6/-5.4, f +1.9/+3.1; contrabassoon pp -1.7, p -3.4, ff +0.8. First-render master -19.9 LUFS (c29 -21.3), TP -1.1.
  - Timbre, 1-5 kHz share of the note body, c29 -> c30 (final): Horn 1 pp -14.4 -> -24.2, p -15.0 -> -21.4, mp -13.2 -> -17.6, f -17.0 -> -14.6, ff -10.3 -> -10.2. Horn 1's p-to-f spread is now 6.8 dB brighter at f (c29: f was 2 dB darker than p). Horns 3/4 pp -11.3/-13.6 -> -20.7/-20.4; Trombone 2 pp -8.3 -> -18.9; Trombone 1 ff -5.7 -> -3.4; Tuba f -24.4 -> -19.9; Clarinet 2 pp -3.0 -> -15.7, Clarinet 1 pp -2.7 -> -7.9 (clarinet f/ff almost unchanged: the f layer starts at CC1 80).
- Level refit (stem fix 1, `build/mix.json`): per-track `soft_trim_db` with explicit ppp/pp/p/mp/mf anchors and `dyn_trim_db` f/ff on the 11 brass tracks and both clarinets, each anchor = old effective trim minus the measured change (per-track median with 5+ notes, else the family median: horns, low brass, clarinets). Contrabassoon soft +1.7, ff -0.8. Horn 1 trims: pp 3 -> 12.1, p 3.5 -> 9.6, mp 2.8 -> 7.5, mf 2.0 -> 2.4, f 1 -> -0.8, ff 2 -> -0.8 (all values in mix.json).
  - Outliers fixed with note trims (`note_trims.json` Horn 1): 27 +4, 39 +4, 178 +3.5, 37.5 -4 (A flat 3 phrase ends had lost 5.8-6.3 dB, 37.5 gained 6).
  - After the fix (final stems against c29): every bucket with 3+ notes within -0.8..+1.0 dB except Horn 2 ff (-2.4, 3 notes, family median), Horn 3 f (-1.6: the role cut below) and Bass trombone pp (-2.7, 2 notes). Horn 1 bars 7-14 per bar within -1.8..+0.4 dB of c29 except bar 14 (-2.4). Master -21.4 LUFS.
- B #2 (part, level only, in the stem fix): Horn 3 role [204,212,5] -> [204,212,1]; Horn 4's [204,212,5] removed (its notes are dropped into Horn 3).
- B #3 (in the stem fix): Horn 1 182 added to the pitch trim's `_skip_onsets` (the +4 G flat 4 trim). Horn 1 at 182.5-182.75 now -37.7/-39.8 dB plain RMS against Violins I -38.3/-39.2 (c29 -31.2/-31.7, 5-7 dB over).
- Trombone 1 (BRIEF item 9): 2-5 kHz first 80 ms minus body on the ff layer: 213 -17.1 dB (c29 -16.9), 218 -4.4 (-7.2), all nine notes negative except the last, 219.5 (+1.5, a decrescendo body). Weight, no bite.

## Other accepted findings

- B #1 `pitch_trims.json` Bassoon 1 "61": -5. Bassoon 1 at 255-256 -32.3 -> -36.7 dB, at 206 -25.7 -> -29.7 (Violins I -29.7).
- B #4 timpani (`LEVEL_SHAPES["Timpani"]`, `LEVEL_SHAPES_S`): (a) bars 2-3 slow ramps -3/-6 dB: roll at 3.25-7.75 -50.4/-49.8/-49.5/-49.7/-50.9 -> -51.3/-52.7/-52.5/-53.9/-56.4 dB (basses -50.3/-50.4/-46.0/-56.3/-55.0); (b) bar 52 cap replaced by a flat -2.5 opening over the last beat, stroke +4 -> +6: 170.5-171.75 -45.2/-48.6/-50.7/-47.9/-46.5 -> -47.2/-47.9/-48.5/-44.5/-43.1 (no longer falls into the stroke), stroke peak -41.6 -> -39.6.
- A #2 `note_trims.json` Violin I solo 53: -3 -> -7. D flat at 53.25-53.5 -42.1/-44.3 -> -44.4/-48.3 dB, against the E flat's end at 52.75 -47.4 (now +3 at the onset, was +5).
- A #4 harp harmonics: 275.5 back to v58 with a -5 dB shape ending before the E flat (0.57 s; the critic's 0.9 s would have cut the arrival), arrival 276 v66. Peaks -47.4/-44.0/-49.1 -> -47.4/-45.8/-48.5 (the passing note 1.6-2.7 dB over, was 3.4-5.1).
- A #5 `entry_leads.json`: Oboe 1 and Clarinet 1 "268" removed (they took up the breath). Breath dip at 268: Oboe 1 12.3 -> 18.8 dB, Clarinet 1 5.4 -> 7.1 (Flute 1 24.6). Clarinet 1 still short of the 8-15 dB target.
- C #2 bars 55-58 (`LEVEL_SHAPES` Violins I/II/celli; celli role [188,190,-1.5] and note trim 190 removed): master bar 56 -29.3 -> -31.2, bar 57 -30.3 -> -30.1, bar 58 -28.3 -> -27.9 dB: the mf no longer louder than the crescendo after it.
- C #4 bar 66 niente (S3): `CC7_POINTS` on Violins II, violas, celli fall 0 -> -14 dB over 223.5-226 (pre-hall) and return over 230-236.5; the Violas 223 fill's hold ramps to 0 by 2.4 s. Over 225-226: -50.3/-54.3/-59.1 -> -59.7/-67.2/-68.2 dB; master -46.4 -> -49.8 (the basses' pedal carries on).
- C #1 delivery: `tools/deliver_master.py` RATIO/KNEE_BELOW 3.0/5 -> 2.2/6 (A/B on the c30 master: 3.0/5 LRA 14.3, span 16.5, limiter 0.4; 2.2/6 LRA 15.6, span 17.8, limiter 1.3; 2.0/6 LRA 16.3, over the target).

## Rejected or deferred

- A #1 (solo violin CC1 target 112 / dip floor, a new generic option): deferred; a vibrato change on the strings, next cycle.
- A #3 (bar 63 sf fall moved into CC7): deferred. It needs the hairpin fall taken out of vol_db and put into CC7 on four tremolo tracks (a new generic rule); the effect was inferred, not measured.
- A #6 (re-bow refit of the coda basses and the opening Violins I with longer smoothing): deferred.
- B #2 rest (Violins II role [204,212,2] -> 0, Violins I fill 205.949 +2, Violins I swells): deferred; C #2 already lifts Violins I +2 dB over 195-206.
- B #6 (soft trims on violas/Bassoon 2), C #3 (`_all` climax shapes), C #5 (swell caps, Bassoon 2 shapes), C #6 (FP_SPIKE): deferred to keep this cycle's other changes few.
- Climax: master bars 61-62 -17.0 against 79-80 -19.8 dB (plain RMS; c29 -16.8 / -19.6): unchanged order.

## Build and render (2026-11-06)

- `parts.json` regenerated, no WARNING. pdiff against `before/`: changes only on the listed tracks (CC1 on the 12 CC1 tracks, CC7 on 3 strings, two notes moved at 268, harp velocities, vol_db). No articulation row, mic or hall changed, so no Opus state changed: `--midi-only` on 21 tracks, 0 errors.
- Lock waited from about 22:00 (Movement I's c39 held it), taken 22:39:51, released 23:09:07: **held 29 min**. Fresh start and open, build, restart; memory rose to 44 GB and stayed with 33-36 GB compressed, so `--force-memory`. Audio device 48000 / 512 / no input (Mac Studio Speakers). Disk 170 GB free; MAC DRIVE mounted.
- After the render: stem fix (`stem_fix.py 30 cycles/c30/rendered_build build --apply`, 12 tracks: the CC1 refit, Horn 3/4 roles, Horn 1 trims) and `--mix-only` on those 12 tracks while locked; then `--measure-only` and the delivery with 2.2/6.
- **REAPER memory after the render: 45 GB (26 GB compressed).**

## Key numbers (c29 in brackets)

- Master (after the stem fix): -21.4 LUFS (-21.3), LRA 24.4 (23.9), TP -2.3 dBFS, sample peak 0.766 (0.822), no clipping. First render -19.9 LUFS, TP -1.1.
- Delivered `cycles/c30/mvt2-mockup-c30.mp3`: -19.8 LUFS (-19.7), LRA 15.6 LU (14.0), TP -1.7, span 17.8 dB (16.3), limiter 1.3 dB (1.1).
- Attack probe: 2 of 20 flagged. Violins II 212 tremolo dip 6.5 dB (known since c27). Horn 1 34 sustain dip 6.5 dB (c29 2.4): probe artefact of the new layer. The join sag into 35 is the same in absolute level (-46.0/-47.1 dB against c29 -45.0/-47.5), but the note before it now plays 1.5-2 dB louder on the mp/mf layers, so the dip relative to it is larger.
