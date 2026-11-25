# Cycle 28 (actor): changes on the c27 render's findings

Critic reports: `cycles/c28/reports/A.md` (articulation), `B.md` (balance), `C.md` (holistic), all on the c27 render. Snapshot of the tools and data before any change: `cycles/c28/before/`.

## What changed

### Balance and levels (`build/roles.json`, level only, simulated on the c27 stems before the render)

- Climax order (B #1, C #1). Flute 1's bar 79 B flat 6: the series 1 lifts [262.6,263.5,3] and [263.5,265.9,7] (written when v77 printed f) became [261.5,262.6,-6], [262.6,263.5,-3], [263.5,265.9,1]: the whole note 6 dB down with c17's decay compensation kept as its shape. The c12 string lifts [262,268,2.5] (Violins I, Violins II, Violas, Double basses) and [266,268,2.5] (Violas div) removed, and [262,268,-1.5] added on the six string tracks (the simulation without it left the delivered climax only 0.7 LU over bars 78-82). `_all` [204,212,-1.4,3.5] -> [204,212,-0.4,3.5].
- Bass clarinet A flat 2 (B #3, C #4): [8,9,-1], [9,13,-7], [13,14,-5], [14,16.75,-3] over the tied pp pedal of bars 3-6 (the sample swells about 10 dB at a flat CC11), and [102,105,-5] on the bar 35 entry (it entered 8 dB over the B flat before it under a printed decrescendo).
- Violins II under the oboe's dolce (C #5): [42,48,-4], [54,60,-4].
- Violas div coda (B #5): [286,304,-4] (B proposed -6; with the refitted re-bows the simulation put the div voice 2-5 dB under the section at -6).
- Double basses' last four beats (B #6): [299.75,304,5].

### Re-bows and fills

- `tools/fit_rebows.py 27 cycles/c28/before/parts.json --write --hold-max-after 301:0` (A #2): every listed and automatic re-bow refitted on the c27 stems (series 1's final-chord shapes no longer fitted v600's levels; the opening chord, bar 66 and Violas div had none).
- Violins II bars 15-21 (A #5, S1): `REBOW_AT["Violins II"] += [45, 51]` and `NOTCH_SKIP` (the printed new slurs on the same pitch) instead of the automatic re-bows at 44.34 and 50.35 that fell between the beats.
- Double basses' bar 66 automatic re-bow 222.452 -> 221.8 (A #2), by hand in `build/rebow_moves.json` after `space_rebows.py --write`.
- Violoncellos final chord: `LEVEL_SHAPES` -5 dB over 302.05-302.9 (the piece from 300.6 swells about 7 dB by itself at 302.0; the master rose 3-5 dB inside the ppp fermata, A #2).
- `tools/auto_fills.py 27 cycles/c28/before/parts.json --write` (A #4) with a new `build/auto_fills.json` that adds Bassoon 1, Clarinet 2, Violins I, Violins II, Violas and Violoncellos div to the measured tracks (Bassoon 1 also to the raised ones). Then an overshoot check of every changed fill on the simulated stems: 11 fills whose 200 ms front rose more than 1 dB to over +2.5 dB over the louder body were lowered by (over - 2) dB, one deleted (Violas 56, +11.5 dB over its body with the 56.81 notch's spike).

### Articulations and controllers (`build/score_config.py`; not simulated)

- Trombone 1's quotation (A #1): `MARCATO_SPANS`, `MARC_ACC_CUT_AT` and 213 in `ACCENT_ART_AT` removed; `GENTLE_ACCENT["brass"]["keep_legato"] = True` (213 is the slurred target of the 212.5 pickup: Leg Slur MAX with its swell); legato targets 213, 215, 215.5, 217.5 at v112; `WIND_REP_PORTATO = True` (215.5 -> 216 "a4--" re-tongued on Sus MAX; it also re-tongues the slurred tenuto repeats of Clarinet 1 288.95, Horn 3 288.95 and Bassoon 2 20.95/143.94/252.95); a +2 dB swell on the slur heads 214.5 and 217.0 (`LEVEL_SHAPES_S`). The track's rows change (Marc Lng out, Leg Slur MAX in): full rebuild.
- Timpani (A #3, C #2): `TIMP_CC1_MAP` and `TIMP_ROLL_TRIM_DB` from movement I c12 (the Rls row's eight CC1 layers; ppp-pp on V4); `HP_TARGET_AT["Timp"] = {268: "p"}` (B #2: the bar 81 roll decrescendo had no target and fell 1.8 dB while the master fell 9.4). MIDI only; no state change.
- Violas' portato eighths, bars 48-51 (A #6, C #6, test): `ART_SPANS` Detache 152.5-168 (row loaded: full rebuild). New generic option `ENTRY_LEAD_ROWS` in `tools/score_to_parts.py` (the rows that take the after-rest entry lead; "Detache" added in the config, so the notes keep c27's 0.108 qn lead and length and only the row changes).

## Rejected or deferred

- CC1 dynamics on brass and clarinets (B #4, C #3, MANUAL-GAPS #1): deferred to c29. It moves the level of every note on 13 tracks by -5..-10 dB at soft dynamics and needs its own per-dynamic trim refit (movement I took two cycles); this cycle already changes the timpani layers, Trombone 1's articulation and the re-bow fits, and C advised the timpani first.
- B minor: Horn 3's climax role +5 -> +3; Violoncellos div's upper voice in bars 21-22; Violoncellos over Violins I in the bar 60 crescendo: left for a balance pass after CC1 dynamics.
- C: Clarinet 1 in bars 61-63 (possible dropped trim): not measured this cycle.
- A minor: the violas' pizz. triplets at 124 (velocity floor), MANUAL-GAPS #8 (Basses DIV A for the 4 soli, memory): open.

## Build and render attempt (2026-11-06)

- `build/parts.json` regenerated with no WARNING; diffed against c27 (`symphony/mvt1/reaper-v621/cycles/c33/actor_scripts/pdiff.py`): changes only where listed above. Opus state changes: Trombone 1 (Leg Slur MAX in, Marc Lng out) and Violas (Detache row): both fully rebuilt; every other track `--midi-only`.
- Simulated on the c27 stems with `tools/stem_fix.py 27 cycles/c28/before build` (every track but Timpani and Trombone 1, whose changes are not level-only), then `deliver_master.py`: bars 61/62 -12.6/-12.8 dB against 79/80 -14.3/-14.7 (c27: -13.3/-13.4 against -12.6/-13.3); delivered max short-term bars 60-64 -10.7 LUFS against bars 78-82 -11.8 (c27 -11.1 against -10.2); delivered -19.7 LUFS, LRA 14.7 LU, span 16.6 dB, limiter 0.8 dB, top pre-limiter peaks now in the climax (qn 210-212). Bass clarinet bars 3-6 -43..-46 dB, level with Clarinet 2 and Horn 4 and under Horn 3's D flat (c27 -36..-38). Violins II 6-7 dB under Oboe 1 at the hairpin tops of bars 15-16. Violas div within -2..+2 dB of the section from 286. Re-bow stem dips median 4.8 -> 2.0 dB; bar 66 master hole at 223 9.7 -> about 1 dB. Changed fills: median join dip 5.1 -> 3.4 dB, joins of 6 dB or more 40 -> 8 of 140.
- Lock taken 18:13:19 (waited 24 min for the Movement I c37 actor). `reaper_ctl.py start` + `open`, `build_reaper.py build/parts.json jobs --midi-only` (32 tracks, 0 errors), `reaper_ctl.py restart`; memory settled at 44 GB (13 GB compressed, then 9.1 GB) at 18:28. /Volumes/MAC DRIVE mounted, 190 GB free.
- **Not rendered.** The audio-device job (`cycles/c28/_c28_audio_init.lua`) read SRATE 24000, BSIZE 480, input "CoreAudio Default": the system's default input and output are AirPods Pro (Bluetooth, 24 kHz, with a microphone), the condition that shifted every Opus output by 256 samples in Movement I c33. `render_cycle.py` stopped first at its memory gate (9.1 GB compressed); its audio check would also have refused. Changing the system audio device is outside what the actor may do, so REAPER was saved and quit and the lock released at 18:30 (held 17 min). The project now holds the c28 data.
- Dan then approved the Movement I thread setting REAPER's own audio device (reaper.ini) to the Mac Studio Speakers with no input, 48000 / 512. The Movement I thread made that change while REAPER was closed.

## Render (2026-11-06, second attempt)

- Lock taken 19:55:26 (waited for the Movement I c38 actor), released 20:23:54: held 28.5 min. `reaper_ctl.py restart` (32 tracks). Memory settled at 44 GB with 0 GB compressed by 20:05, about 10 minutes after the open. `/Volumes/MAC DRIVE` mounted, 189 GB free.
- `_c28_audio_init.lua`: SRATE 48000, BSIZE 512, IDENT_IN "CoreAudio " (no input), IDENT_OUT "CoreAudio Mac Studio Speakers", running.
- `render_cycle.py 28` passed both gates (no `--force-memory`). Render, measurement, probe and delivery took 7.3 min. REAPER memory: 44 GB with 0 GB compressed before the render, 45 GB with 29 GB compressed after it.
- Level-only fix after the render (below): `build/roles.json` Violas `[152.45, 167.98, -13, 0.08]`. Then `score_to_parts.py` (the only change in parts.json was the Violas vol_db), `stem_fix.py 28 cycles/c28/rendered_build build --apply Violas` (the originals are in `render_first/`; the rendered master equalled the float stem sum, max difference 8e-7), `render_cycle.py 28 --measure-only`, and `build_reaper.py build/parts.json jobs --mix-only Violas` while the lock was still held (`build-mix-stemfix.log`). REAPER then reads -6 dB on the Violas envelope over 152.6-167.8: the -13 role plus the track's gain and soft trim. `reaper_ctl.py quit`, `unlock`.

## Key numbers (c27 in brackets)

- Master: -21.1 LUFS (-20.1), LRA 24.6 LU (24.9), true peak -1.7 dBFS (-2.0), sample peak 0.820 (0.794), 0 samples at full scale. It was -21.3 LUFS before the Violas fix, which lowered the master RMS by 0.02 dB; the integrated value rose because the relative gate drops more quiet blocks.
- Delivered `cycles/c28/mvt2-mockup-c28.mp3`: -19.8 LUFS (-19.8), LRA 14.6 LU (14.9), TP -1.6 dBTP (-1.6), p10-to-max span 16.7 dB (17.7), limiter about 1.2 dB (1.1), ride +10.0 / -2.6 dB, 349.80 s. The top pre-limiter peaks are now in the climax: qn 210.6, 211.5, 212.2 and 204.1-204.6 (-0.26 to -1.5 dBFS).
- Attack probe: 1 of 20 flagged (c27: 1 of 20). The flag is the same one as in c27 and c26: Violins II qn 212, a 6.5 dB tremolo-entry dip against a 6 dB limit (c27 6.4). Trombone 1 212.5 now starts 0.07 s early, inside its limit. This is the new legato pickup's 0.1 qn lead.
- No clipping. All 32 stems are present. None is near silent apart from c27's Timpani 279 roll at -72.9 dB, which is the same in both renders (not a c28 change).

## Did each change work (measured on the render; c27 in brackets)

- **Climax order: yes.** On the delivered mp3, the maximum short-term loudness over bars 60-64 is -10.7 LUFS and over bars 78-82 is -11.9 (c27 -11.1 and -10.2). The climax is now 1.2 LU over bars 78-82 (c27 was 0.9 LU under), matching the simulation (-10.7 / -11.8). Master bars 61/62 are -15.6/-15.8 dB and bars 79/80 are -17.9/-18.3 (c27 -16.3/-16.4 and -15.6/-16.3).
- **Timpani layers: yes.** Mean stem level over each roll: pp roll at qn 3 -50.0 (-54.9), 168 crescendo roll -47.7 (-53.1), ppp 226 -54.4 (-54.8), 261 -38.0 (-33.5), 262/265 -33.3/-34.3 (-32.2/-33.2). The bar 81 roll decrescendo (268-271) now falls 7.5 dB, where the master falls 11.1 (c27: 3.0 against 10.7). In bars 1-3 the roll is still 9 dB under the master's p90 (-48.1 against -38.9).
- **Trombone 1 legato: yes, with one soft beat.** The level dips at the joins in 213-218 are now -0.2 to 3.0 dB (c27 4.2-6.9 dB, a re-attack on each note). The exception is 215.0, at 4.7 dB, where the line sags to -29/-30 dB over 215.1-215.5 between -23 at 214.9 and -26 at 215.75. The pickup is about 3 dB softer than c27's marcato (-26/-27 against -23/-24). The phrase now runs -24 to -30 dB with no gaps (c27 peaks -20 to -25 with -30 to -39 gaps). The 215 sag was left for the critics: fixing it would change a level on a legato transition that has not been heard yet.
- **Re-bow dips: yes.** 87 listed re-bows, stem level 0.45-0.10 s before each minus the minimum over -0.05..+0.4 s: median 1.7 dB, p90 4.0, 5 of 6 dB or more (c27: median 3.8, p90 9.9, 30). This is a different window from the simulation's 4.8 -> 2.0, so the two sets of numbers are not comparable.
- **Bar 66 hole: yes.** The master dip at qn 223 (the same window) is 1.9 dB (c27 8.9).
- Bass clarinet: maximum over bars 3-6 is -45.2 dB (c27 -38.6), level with Clarinet 2 and Horn 4 (-44.8) and under Horn 3 (-42.2). Bar 35 entry maximum -40.1 (-35.1).
- **Violas Detache test (bars 48-51): the row plays, but 17 dB too loud, now fixed on the stems.** As rendered, the pp sotto voce eighths peaked at -31.4 dB (c27 -48.7), 3 dB over the cor anglais melody's maximum (-34.3) and 10 dB over Violins II and the Violoncellos (-42). The -13 dB role puts the eighths at -44.4 to -51.2 dB: under the other strings, about 10 dB under the cor anglais, and 4 dB over c27. The 168.0 note after the span is unchanged at -47.0 dB.
