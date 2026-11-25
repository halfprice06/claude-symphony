# Cycle 1 (2026-11-07): actor changes on the c00 port baseline

Critics: `reports/A.md` (articulation), `B.md` (balance), `C.md` (blend). Orchestrator notes (Dan, 2026-11-07): the hall was too wet; a shared reverb change and the REAPER turn rule. Snapshot of the earlier tools and data: `before/`.

## Changes

### Tools (generic, with defaults that change nothing)
- `tools/score_to_parts.py`
  - `ROW_GAIN_DB` {track: {row: dB}}: a level offset on stretches where all of a string track's sounding notes are on one row. It is folded into the chord/divisi cut (B #2).
  - `LAST_DESK_DB`: the texts "last desk" and "last N desks" cut the part until "tutti" or "ord.". Divisi chords inside such a span keep their divisi cut (A #4).
  - `TASTO_CC1`: string notes in a "sul tasto" span, on sections without a Flautando row, get this CC1 value (A #4; manual p.92).
  - `REBOW_KEEP_ARTS` (default ("Flautando",)): the pieces of an AUTO_REBOW split keep that row (A #4).
  - `HARM_ON_TRACK` {harp track: semitones}: flageolet notes stay on the harp track, HARM_VEL_CUT under the harp's dynamic (A #5).
  - `GLISS_SPANS` {staff: [(a, b, lo, hi, pitch classes, v0, v1)]}: writes out a printed glissando that the event list does not carry (A #5).
  - `UNI_CHORD_SPLIT` (default True): when same-patch tracks play the same chord, the chord is split by pitch between them. Before, the whole chord stayed on one track; on a legato row that track sounded only one note (A #3).
- `tools/build_reaper.py`
  - mix.json `"bandpass"` {rows, low_hz, high_hz}: rewrites the Opus "Bandpass Filter" processors of the listed rows (C #5).
  - Reverb `low_cut_hz` (ported from mockup-kit, orchestrator note).

### build/score_config.py (c01 block)
- `ART_SPANS`, staccato marks only:
  - Horns 3/4: "StacSs RRx9" at qn 40-104 and "Marc Shrt RRx4" at qn 600-664, velocities `vel_by_cc` 70/88/98/100.
  - Bassoon 1: "Stac DblTng RRx9" at qn 40-132 (v72-104).
  - Trumpets 1-3: "Stac DblTng RRx9" at qn 632-664.
  - Bassoon 1 also takes `STAC_LEAD_S` 0.03 (A #1).
- `STR_REP_DETACH` on the double basses at qn 792-840.25 and 984-1108.25: dip -5 dB, 0.08 s, min_cc 72. `LEVEL_SHAPES` add +1.5 dB on the basses over the same spans. `METRIC_BOWED` on Vla/Vc/Cb at qn 792-816 and 984-1080 (A #2, S1).
- `TASTO_CC1 = 0`, `LAST_DESK_DB = -4` (A #4).
- `HARM_ON_TRACK = {"Harp": 0}`: mockup.midi already carries the sounding B flat 4. `GLISS_SPANS` for the bar-277 harp glissando: 15 notes G3-E6 on C-D-E-G-A at qn 1106-1107.9, v90-112 (A #5).
- `HP_CHAIN_RISE_FFF` wind 0, string 0, brass 0.5 (B #1).
- `ROW_GAIN_DB`: Violins I Tremolo -3 dB, Violins II Tremolo -4 dB (B #2).

### build/roles.json (it was empty)
- Brass (Horns 1-4, Trumpets 1-3, Trombones 1-2) +2 dB at qn 888-892 (B #1).
- Violoncellos:
  - +2 dB at 264-328, 744-792 and 1016-1032 (B #3).
  - Pizzicato at 200-264 and 680-744: -5 dB as rendered, changed to -1 dB by the stem fix (B #5).
- Solos and accompaniment (B #4):
  - Trumpet 1 +2.5 dB at 200-264, +2 dB at 680-712 and 732-792.
  - Clarinet 1 -4 dB at 200-264 and +4 dB at 176-184.
  - Flute 1 +4 dB at 168-176; Oboe 1 +4 dB at 184-192.
  - Violins I -3 dB at 168-200; Bass clarinet -4 dB at 680-744.
- Harp -4 dB at 264-328 and -3 dB at 952-968 (B #6).
- Bass octave in the 13 loud tutti spans (C #1): +3 dB on Double basses, Contrabassoon, Bassoon 2, Tuba and Bass trombone, +2 dB on Bass clarinet. Each span opens over 4 qn after it ends.
- Stem fix, also written into REAPER with `--mix-only` (see below):
  - Horn 3 +3 dB and Horn 4 +5 dB at 40-104; both +2.5 dB at 600-664.
  - Trumpets 1-3 +3 dB at 632-664.
  - Violas +4 dB at 678-720 and 728-744.

### build/mix.json
- `loud_eq` on the 13 loud spans (wet 0 -> 1 over the 2 qn before each span, back over the 2 qn after), Movement I's c42 bands (C #1):
  - Violoncellos: 150 Hz +6 dB.
  - Double basses: 160 Hz +6 dB and 98 Hz -4 dB.
  - Bassoon 2: 140 Hz +3 dB. Contrabassoon, Bass trombone, Tuba: 140 Hz +4 dB. Timpani: 140 Hz +3 dB.
  - Violins I/II: high shelf at 2.5 kHz, -2.5 dB.
- Timpani: a second switched EQ, high shelf at 1.5 kHz -6 dB, at qn 707.5-711.5 and 871.5-985, where soft and medium sticks are printed (C #6).
- Double basses (C #2):
  - `mute_eq` bells narrowed: 61.7 Hz -5 dB and 73.4 Hz -4 dB, both at 0.12 oct.
  - `eq` bell2 at 87.3 Hz: -12 dB at 0.15 oct.
- Tuba: the 70 Hz low shelf is removed; the 84 Hz bell is narrowed to 0.2 oct (C #2).
- Violoncellos: `gain_db` 0 -> -4; soft trim pp 6 -> 4 and p 5 -> 3.5 (B #3).
- `dyn_trim_db` fff: Flutes -5, Oboes +2 (B #1, C #4).
- Clarinet 2 `width` 0.05; Cor anglais `send` 0.5 (C #3a).
- Trumpet 1 `bandpass` on the Mute Sus row: 250 Hz-8 kHz, opened from 90 Hz-3 kHz (C #5).
- Reverb (Dan / orchestrator, shared with Movement I): `fx_volume` 0.19 -> 0.095 (-6 dB hall return) and `low_cut_hz` 160. Sends, IR, wet, high cut and true stereo are unchanged.
- This changed every Opus state, so all 31 tracks were fully rebuilt.

## Rejected or deferred
- A #1, the remaining Sus-row staccatos ending at 0.35 instead of 0.5 of the written length: deferred. First measure the short rows on this render.
- A #6, soft brass legato velocity on Trumpet 1's dolce solo: deferred. The leads were fitted at v124 and would need a refit.
- C #3b, Mid mics on the woodwinds (MANUAL-GAPS #4): deferred. The hall change already moves depth this cycle; one variable at a time.
- C #6, a felt timpani track in a second pass: deferred (interim EQ above).
- Vln I "harm." at bar 43 on the Vln II Harmonics row: needs another instance; deferred.
- Orchestrator S1 note: four slurred same-pitch string repeats are merged into the note before (mvt1 c05 rule, `slur_rep_merged`):
  - Violins I, Violins II and Violas at qn 796 (an unslurred eighth into a tenuto that starts a slur);
  - Violins I, Violins II and Violoncellos at qn 988.
  - These are in the hammered coda and Più allegro. Open for c02: make them re-attacks.

## Measured, c00 -> c01 (stem RMS dB over the span; c01 after the stem fix unless marked)
- Bar 223, family sums: woodwinds -12.9 -> -17.7, brass -13.6 -> -12.2, strings -12.0 -> -17.1, so brass are on top. Master over the bar -8.0 -> -10.1.
- Climax order: bar 223 -10.1, bar 263 -11.3, bars 278-279 -11.6. All three are still the loudest bars.
- Master sample peak 1.99 -> 1.61. The master is still the float sum of the stems: the 24-bit file clipped.
- Bars 11-26: Violoncellos -29.4 -> -34.6 against Violins I -34.3 -> -34.5. The cellos are now level with the tune, not 5 dB over it. The critic's target was 2-4 dB under.
- Tremolo against the chorale: bars 224-225 Vln I -29.9 -> -33.8 vs Trumpet 1 -31.2; bars 255-262 Vln I -21.4 -> -24.8 vs Trumpet 1 -24.7; bars 273-277 Vln II -21.9 -> -24.6 vs Horn 1 -24.4.
- D (bars 51-66), Trumpet 1 solo against Clarinet 1: -45.6 / -44.7 -> -44.0 / -49.6. The cello pizzicato rendered at -57.9; after the stem fix it is about 4 dB higher.
- C (bars 43-48), motive x solos: Flute 1 -46.9 -> -43.6 against Violins I -43.7 -> -46.8; Oboe 1 -46.1 -> -42.3.
- L (qn 680-700): cor anglais -43.6, Trumpet 1 -48.2 (from -49.3), bass clarinet -45.0 -> -50.3.
- E (bars 67-82): harp -32.6 -> -36.7 against Violins I -36.2.
- Muted trumpet, 5-10 kHz minus 0.5-2 kHz: -60.0 -> -49.2 dB.
- Harp harmonics, qn 168-172: silent -> -50.1 dB. Harp glissando, qn 1106-1108: -36.9 -> -25.7 dB.
- Horn 2, C4 band at qn 996.3-997.7: absent -> present (+43 dB relative band energy). Horn 1 no longer carries the C4.
- Basses' repeated eighths, re-attack dip: median 3.0 -> 7.3 dB (p10 1.4 -> 5.4) at qn 792-840, and 3.7 -> 7.9 dB (p10 1.4 -> 4.8) at qn 984-1108. Target was 7 dB / p10 4: met.
- Staccato -10 dB length:
  - Horn 3: 0.35 -> 0.15 s at qn 40-104 (StacSs); 0.44 -> 0.31 s at qn 600-664 (Marc Shrt).
  - Bassoon 1: 0.39 -> 0.24 s. Trumpet 2: 0.36 -> 0.29 s.
  - Horn StacSs is now shorter than the strings' 0.27-0.33 s. Marc Shrt is closer to the target, so it is the candidate for both spans in c02.
  - The short rows came out 3.6-8.6 dB under the old Sus notes (rendered), hence the +2.5..+5 dB stem fix.
- Sul tasto: Violas at qn 376-392 -44.8 -> -49.1 (CC1 0 plus the -4 dB desk cut). At qn 680-720 the rendered level was -58.2 against -50.6: CC1 0 selects the quieter Non Vib samples (about -7.6 dB). The +4 dB stem fix brings it to about -54.
- Hall (Dan's note): at the tutti cut-off at 1.8 s (the only cut-off with 1.2 s of silence after it), the master drop 0.3 s after the cut-off went 9.8 -> 15.6 dB (target 13 dB or more). The late decay at 1.5-2 s went 15.8 -> 16.8 dB under the pre-cutoff level. The early-tail measures across the stems are left to critic C on this render.
- Delivered mp3, after the stem fix: -19.8 LUFS integrated, LRA 17.0 LU (c00 15.7), true peak -1.6 dBTP, limiter about 1.8 dB, p10-to-max span 21.4 dB (c00 21.5). The LRA is now over the 14-16 LU target: the soft passages fell (solo accompaniment cuts, cello gain). Open for c02: raise soft-passage levels or the ride.
- Master: -15.8 LUFS integrated, LRA 22.5 LU.
- Attack probe: the same two flags as c00. Oboe 1 qn 36 +0.10 s (unchanged). Violoncellos qn 24 +0.15 s against a 0.15 s limit (c00 +0.42). The strings still sound in the pre-roll because their first notes are led before qn 0, as at c00.

## REAPER
- Lock held 09:23:53-09:59:49 (36 min): fresh start, full build of 31 tracks, restart, settle, audio-device reopen (48000 Hz, 512, no input), render, `--mix-only` for the stem-fix tracks, quit, unlock.
- REAPER memory: 43 GB settled (0 compressed) before the render; 44 GB after the render, with 26 GB compressed at the end.
- Before taking the lock I waited for Movement I's turn, per the turn rule.
