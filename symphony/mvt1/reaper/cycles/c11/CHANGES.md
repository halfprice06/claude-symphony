# Cycle 11: changes (actor)

Render c11 from a freshly restarted REAPER (32 tracks; `build_reaper.py --midi-only --tempo` on every track, Harp fully rebuilt because its Opus state changed, then save, quit, restart, open, render), followed by one level-only stem fix (`tools/stem_fix.py 11 cycles/c11/rendered_build build --apply`; first-render files in `cycles/c11/render_first/`, the data that render was made from in `cycles/c11/rendered_build/`). REAPER was updated with `build_reaper.py --mix-only` for the 17 stem-fixed tracks, saved and quit, so the project matches `build/`. Snapshot of the c10 tools and data: `cycles/c11/before/`. Scratch: `/private/tmp/claude-501/mockup-loop/mvt1-c11-actor/` (`pdiff.py`, `cccheck.py`, `check.py`, `check2.py`, `c78.py`, `d78b.py`, `peaks.py`, `climax.py`, `rbdiff.py`).

## Accepted

### Tempo (C #1, C #2, C #5)
- C #2: every re-bow point of the c10 build (90 points on the five string tracks, after `space_rebows`) is listed in `REBOW_AT` (`_REBOW_FROZEN` in `build/score_config.py`), so tempo changes no longer move them. Then arcs for the Lento, the transition and Tempo I: `PHRASE_ARCS` += (0,16,"sub"), (16,36), (36,48), (48,56,"main"), (128,144), (144,160,"sub"), (712,724,"sub"); `TEMPO_PUSH` += (36,46,1.015). Check: every parts.json `rebows` row keeps its qn and pitch (only the piece ends moved, by under 0.02 qn, where a following note's lead moved). The arcs add only +0.6 s (the "sub"/default depths are mild at 50 bpm); tempo shaping total +0.82 s.
- C #1: bar 72 arc (272,286,"main") -> (272,284,"open") plus `BEAT_STRETCH` 284/285 x0.95: the three hammer strokes now come 0.501 / 0.501 s apart and the next beat is at 126 (c10 0.501 / 0.541 / 0.476). C asked for "sub"; "sub" slowed beats 282-283, which made the violas' slurred eighths 0.25 s long and switched them from Sus MAX to Leg Slur MAX targets (seen in the parts.json diff; articulation lengths are read on the shaped map), so the arc keeps its push and has no slowing. Bar 32 (120,128) -> "sub". Bars 61/155 arcs -> new depth "open" in `tools/score_to_parts.py` `phrase_arcs()` (push only, no slowing). No unprinted beat-to-beat change over 7.5% remains in qn 118-130, 228-248, 276-290, 596-624.
- C #5: `TIMP_DELAY_S` 0.06 -> 0.045 (with C #4).

### Timing (C #3, C #4)
- C #3: `ABUT_LEAD` Violins II (91/94/97/539/542/545) and Violas (+575), 0.10 s, `skip_next_same` False. Pitch crossovers (harmonics 1-4, 5 ms hop): Violins II median +0.187 -> +0.083 s, Violas +0.138 -> +0.030 s (two at -0.08). The next same-pitch strokes dip a little more (Violins II 92/540 -1.8/-2.2 -> -5.3/-5.4 dB; others -3..-7 as before): more even separation, not a hole.
- C #4: `ABUT_LEAD` 0.05 s on Horns 1-2, Trombones 1-2, Trumpets 1-3, Oboes 1-2, Flute 2; `ENTRY_LEAD_ART_S` "Flute"/"Oboe" = the wind values + Sus MAX 0.04. Crossover medians c10 -> c11: Horn 1 +0.085 -> +0.040, Horn 2 +0.055 -> +0.013, Trombone 1 +0.084 -> +0.031, Trumpet 1 +0.074 -> +0.018, Oboe 1 +0.069 -> +0.022, Oboe 2 +0.088 -> +0.038, Flute 2 +0.084 -> +0.036 s.
- Actor: `ABUT_LEAD["Violins I"]` 0.06 s at 78 (its sf stroke follows a Sus eighth, so it had no entry lead).

### Articulation (A #1-#5)
- A #2: `DOWNBOW_STROKE_AT` Violins I/II 78 and `SF_ARRIVAL_AT[78] = "ff"`. The first render overshot: the arrival rule applies to every track with an sf there, and Violins II had no crescendo (mp), so its sf body sat at ff for two beats (+10..+14 dB over the note before; Violins I +10..+12). Stem fix: level shapes on both (`LEVEL_SHAPES`, c11 stem-fix block). Result, first 0.25 s minus the note before: Violins I +1.7 -> +4.5 dB, Violins II -5.3 -> +4.0, master -0.1 -> +2.1; 2-5 kHz first 80 ms minus body -12.5 (Vln I) / -19.6 (Vln II); Violins I 78-80 over the bar before +5.2 (c10 +5.4), Violins II back to about its mp. The Violins II CC11 stays on the ff layer as rendered (see Open).
- A #1: quarter fills held to the tenuto (`hold_s` 0.40 -> 0.55; celli 684 0.72; celli 685 `pre_s` 0.08, `hold_s` 0.25, 7 dB after the stem fix), tenuto trims ramp 1.0 s. Master hole / tenuto's first 0.35 s re the quarter (c10 -> c11): 189 -4.0/-1.5 -> -3.7/+0.1; 201 -5.2/-1.9 -> -4.9/-2.7; 589 -3.0/-1.9 -> -0.8/-0.1; 601 +0.1 -> +0.4; 685 -5.7/-2.2 -> -3.2/-1.0 (celli -9.3 -> -3.9, 30 ms peak +2.2). Horn 1 tenutos now start +1.4..+1.8 over the quarter. Pass (2.5 dB) met at 589/601 only: at 201 the basses' decay and the harp take the master down, at 189 the trim ramp and the sample's sag at +0.3 s.
- A #3: violas solo 424-432 (`LEAD_SPANS`, fill 429, trims 429 +3 / 428 -2.5, role +2.5): tenuto's first 0.5 s minus the 428 quarter -6.1 -> +0.1 dB, body over the G4 -1.0 -> +6.1, violas over Violins II +3.2 -> +7.5. A 0.1 s sag of 4.5 dB just before the tenuto (the join) is left; the master's 100 ms minimum there is unchanged (-6.0). The LEAD_SPANS arc also gives beat 429 an apex x0.96.
- A #4: harp damps by note-off. `mix.json` Harp `env_release_ms` 200 (new generic key, `tools/build_reaper.py`: every AHDSR release and the patch's envelope proxy; the Harp Sus RR groups ship 3019 ms, read with `opus_state.load_oib`); `HARP_RING_S` 2.0 s in `tools/score_to_parts.py` (each note rings 2 s past its written end, cut at the next "étouffez" mark, "(m.d.)" only on the right-hand staff, and before a same-pitch onset); the c10 650 volume damp removed, `tail_hold` back on. At 244 the old E3/E4 fall -19.7/-15.2 dB within 0.25-0.5 s (c10 -8.9/-5.8); broadband harp stem at 650: -16.9 dB at +0.2 s, -30.7 at +0.8 s (c10 -34.6 / -39.8: the c10 envelope cut the hall too); unaffected notes 216-256 within ±0.5 dB of c10 over 1.5 s; the final chord now stops at its étouffez (727).
- A #5: `FP_SPIKE` (generic: an fp is an f attack held 0.12 qn, at p by 0.25 qn; the only fp is the basses' at 128) with a -4 dB note trim on Cb 128; `WIND_REP_AFTER_SLUR` (generic: an unslurred repeat after a slur's last legato note is re-tongued; 11 more re-tongues, 309 -> 320); `loop_fills` Violoncellos 8.0 [1.0 s, +5, 0.35].

### Balance (B #1-#5)
- B #1 bar 124: roles to 492.5 (brass) / 492 (Vln I, Fl1) and brass decrescendo shapes 492-496.3. Melody minus loudest brass per qn 492-495: -7.0/-9.3/-9.9/-9.6 -> -4.5/-1.8/-2.0/-1.9 dB; master falls 13.2 -> 24.1 over bars 123-124.
- B #2 celli roles -3 at 88-104, 360-408, 536-552. Melody margin (median, my measure: loudest melody stem minus loudest other stem per qn): bars 23-26 -4.7 -> -3.5, 91-93 -3.6 -> -2.1, 98-102 -1.9 -> +1.0 (covered 16 -> 4 of 20), 135-138 -3.2 -> -1.7.
- B #3 Horn 4 low-note trims (0.1 s steps): re master bars 19-21 -10.8 -> -15.7, bar 105 -9.6 -> -11.9, bars 162-164 -9.3 -> -13.0 dB.
- B #4 trumpet f/ff trims (Tpt1 f 6.1; Tpt2 f 6.2, ff 10.5; Tpt3 f 7.7, ff 12.1): Trumpet 1 re master bars 69-71 -13.9 -> -11.5, bars 131-134 -16.0 -> -13.6 (Trumpet 1 - Trombone 1 -5.1 -> -2.6); bars 167-170 unchanged; tune margin bars 69-71 -2.7 -> -0.5.
- B #5 bars 13-14 shapes (Vln I, Fl1) and Vln II role: Horn 1 margin -4.0 -> +0.5 dB (covered 6 -> 3 of 7).

### Accents
- `fit_accents.py 11 cycles/c11/rendered_build/parts.json --family brass|string|wind --keep-long-qn 1.4 --write` (78 rows changed), applied in the stem fix; Violins I 477 [0, -6] removed by hand again. Measured on the first c11 render: brass 29/37, strings 97/135, winds 119/140 in 2-4 dB (the leads and roles moved them); refit prediction 33/37, 116/135, 124/140. 2-5 kHz first 80 ms over 3 dB: 0 brass, 2 strings, 1 wind (the known artefacts).

## Rejected or deferred
- A #6 (tam-tam + crash in one instance, a2 horns on the freed slot): deferred; it needs a cycle with no other build change, as A says.
- B #2 optional violas/Vln II rows in bars 23-25: not done (they cut the crescendo into bar 27 by 1 dB on the master).
- C #1 "sub" at bar 72: replaced by "open" (see above).
- Re-bow refits: not done. Lento/coda re-bow dips on the stems are as c10 in median (Vc -2.6, Cb -1.4 dB); nine rows got 1.5-5 dB deeper (Violas 24.863, 52.384; Celli 39.879, 723.921; Basses 22.003, 46.003, 52.92, 722.671, 724.803), on the master within 1 dB of c10 except Cb 722.671 (-2.2 -> -4.5 dB).

## Open
- `SF_ARRIVAL_AT` applies to every track with the sf; at 78 it should apply to Violins I only (Violins II's CC11 is on the ff layer under a -12 dB level shape). Make the table per track and re-render 78 next cycle.
- Second-theme tenuto holes at 189/201 (master -3.7/-4.9) and the violas' 0.1 s join sag at 429.
- The master's top peak is now 637.97 (celli 0.27, bass trombone 0.24, Horn 1 0.22; 1.489 against 1.381): the brass chord changes now land with the strings; delivery limiter 1.0 -> 1.7 dB.
- Celli still over the tune in bars 23-26 (-3.5) and 135-138 (-1.7).

## Before / after (c10 -> c11, after the stem fix)
- Master (float stem sum): -16.3 -> -16.3 LUFS, LRA 21.9 -> 21.8 LU, sample peak 1.381 -> 1.489 (true peak +3.5 dBFS on the float sum).
- Delivered mp3: -19.8 -> -19.8 LUFS, LRA 14.2 -> 14.2 LU, p10-to-max span 18.2 -> 18.1 dB, limiter 1.0 -> 1.7 dB, -1.6 dBTP. Climax (delivered S max): bar 160 -10.35 > bar 122 -10.75 > bars 167-170 -12.69 (c10 -10.30 / -10.86 / -12.76). Motion (mp3) 8.59/4.48 -> 8.74/4.52 dB.
- Attack probe: 0 flagged (first render and stem fix).
- REAPER memory: 18 GB (0 compressed) before the render, 43 GB with 18 GB compressed after it (32 GB compressed by the time of the save and quit, after the analysis). Other processes: VM 2.8 GB, Steam 2.1 GB, two other users' Python processes 1.5 and 4.6 GB.
