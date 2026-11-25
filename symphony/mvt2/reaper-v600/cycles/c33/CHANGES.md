# Cycle 33 actor: changes (on the c32 render; critics A articulation, B balance, C blend)

Snapshot of tools and build data before the changes: `before/`. Check script: `actor_scripts/check.py RENDER PARTS`.

## Changes

- **A #1, harp envelope.** `build/mix.json` "Harp" and "Harp harmonics": `env_sustain` 1.0 (both patches decay to sustain 0.001 over 6 s on every group and the instrument envelope; Movement I c35 fix). Harp keeps `env_release_ms` 200 and HARP_RING_S. Opus state change: both tracks fully rebuilt.
- **A #4 / C #5, celli "4 soli" on the half section.** `build/score_config.py` `TRACK_SPLITS["Violoncellos div"]` adds the window (274, 286, lowest pitch 0): the coda A flat 2 pedal plays on Celli KS Master DIV A. New generic options in `tools/score_to_parts.py`: a split window may carry its own lowest pitch (third element); `META_SKIP_TRACKS` (half-section patches ignore metà/soli; movement II: Violoncellos div). `ART_SPANS["Violoncellos div"]` Sus MAX 273.5-286 (the full section played the entry on Sus MAX). Role `[273.9, 286, -3, 0.5]` on the div track, level then set by stem fix. The five Violoncellos re-bow fills 275.494-284.151 dropped (fitted to the full-section samples); `rebow_moves.json` Violoncellos 283.724 dropped, Violoncellos div 283.757 -> 284.141 added (space_rebows.py's value; its full rerun was reverted because it resets the hand-set c28/c31 moves). The div track gains the Sus MAX row: full rebuild.
- **A #2b/c, Trombone 1 213 and 215.** `CC7_POINTS["Trombone 1"]` 85 at 212.9-213.35, 95 at 214.9-215.3 (pre-hall, S3); `mix.json` Trombone 1 `loud_eq` high shelf 2 kHz -4 dB switched on over the same two heads (critic's (c) at -4 instead of -6, since (b) also applies).
- **A #5, solo violin legato velocity.** `VEL_SET["Violin I solo"]` 72-80 on the nine legato targets (was v124); `build/leg_leads.json` Violin I solo +0.04 s on the same onsets.
- **A #6, harp details.** `HARP_PITCH_VEL` 61 +6, 68 +4, 54 -5 (config override); harmonics 275.5 shape -5 -> -7 dB, 276 v66 -> 70.
- **B #1** `roles.json` Horn 1 `[203.95, 208, 4.5, 0.25]`, Horn 2 `[203.9, 212, 2, 0.25]`.
- **B #2** `mix.json` Violins II `dyn_trim_db` f -2.5 -> -0.5, ff -1.5 -> 0.5; roles `[188, 204, 2, 0.5]`, `[249.9, 258.5, 2.5, 0.5]`.
- **B #3** `note_trims.json` Bass clarinet 91 +8.5, 91.5 +6.5, 92 -5.5, 92.5 -2 (the critic's +6/+4.5/-4/-1.5 simulated only +2.8 dB at 91 on the c32 stem, so deepened).
- **B #4** Bassoon 1 `[252.9, 258, -3, 0.5]`.
- **B #5** Violoncellos `[65.8, 72, 2, 0.5]`, Double basses `[65.8, 72, -3, 0.5]`.
- **B #6** Violas and Violas div `[297.9, 304, 2.5, 1]`, Violoncellos `[297.9, 304, -2, 1]`.
- **C #1** `mix.json` side shelves: Double basses {100 Hz, -15 dB} (was 200/-2), Timpani {150 Hz, -9 dB} (was 200/-2).
- **C #2** Bass clarinet side shelf low shelf 250 Hz -6 dB (was high shelf 250 +1.5).
- **C #3** Violins II div EQ high shelf 1 kHz -10 dB (was 1.5 kHz -6); its 108-124 role -1 -> +0.4.
- Stale fill: `rebow_fills.json` Violins II 263.411 (no re-bow there since c31, WARNING) moved to `_stale_c33`; it was not applied in c32 either.
- After the render (stem fix): Violoncellos div coda role -3 -> -5.2 dB (`stem_fix.py 33 cycles/c33/rendered_build build --apply "Violoncellos div"`, then `build_reaper.py --mix-only "Violoncellos div"`, `build-mix-stemfix.log`): the half-section pedal came out 2.2 dB over c32's full section at -6. `rendered_build/` holds the data the render was made from.

## Rejected or deferred

- A #2a, CC16 round-robin reset on every track: B measured that unchanged tracks render bit-identically from a fresh restart, so takes are already repeatable; a reset would change every track's takes and void the fitted re-bow and accent tables. Deferred; the CC7/EQ fix answers the audible part.
- A #3, CC16 reset before each double-bass re-bow piece: which bow direction is the steady one is unknown (the alternation's phase differs between the two pedals); needs a test render of the basses alone. Deferred.
- C #4, loud-frame 125 Hz bells: optional, closes a third of the gap; deferred behind the image fixes.
- MANUAL-GAPS: #8 (half-section patch for 4 soli) used for the celli (above); nothing else tried.

## Measured (c32 -> c33, `actor_scripts/check.py`, power-sum RMS; c32 numbers on the c32 render)

- Harp, drop from 0.1 s after a pluck to just before the next: 19 6.0 -> 2.9, 28 5.6 -> 5.8, 108 17.7 -> 13.1, 247 21.7 -> 11.1 dB. Coda let-ring A flat 1 at 274 +0/1/2/3 s: -61/-82/-107/-121 -> -55/-57/-58/-61 dB (now rings under the harmonics). Harmonics 276: -50 -> -70 became -49 -> -67 dB 1.5 s later (the note ends after 1.15 s; release 3 s).
- Trombone 1 2-5 kHz in the first 80 ms: 213 42.8 -> 36.5, 215 43.9 -> 38.7 (212.5 unchanged 32.2); 30 ms peak 213 -18.4 -> -22.0, 215 -20.4 -> -23.5. Master 2-5 kHz jump 213 +3.6 -> -1.2, 215 +7.3 -> +2.4 dB. 213 now 2 dB under the critic's -20 target peak; left (weight on the ff layer, no bite).
- Horn 1 204.5-208 -31.6 -> -27.3, Horn 2 204-212 -29.6 -> -27.6 (Violins I -25.7).
- Violins II minus Violins I: bars 59-60 -6.0 -> -2.0, bars 76-77 -5.3 -> -1.8 dB.
- Bass clarinet bar 31 note bodies -48.4/-45.5/-35.5/-39.7 -> -44.9/-42.4/-38.5/-40.9 (Bassoon 2 pedal -46.5): the first note now 1.6 dB over the pedal, the jump at 92 3.9 dB instead of 10.
- Bassoon 1 253-257 -37.1 -> -40.1 (Violins I -36.6). Celli minus basses at 66-69 -2.4 -> +2.7 dB.
- Final chord 301-303: violas sum -60.2 -> -57.7, celli -54.8 -> -56.8.
- Celli coda 274-286 (Vc + div) -54.2 -> -54.1 after the stem fix (Cb -52.6).
- Master 35-63 Hz R-L: bars 1-3 +14.2 -> +2.4, bars 83-86 +13.5 -> +1.6 dB. Bass clarinet 93-97 below 250 Hz R-L -13.8 -> -6.6 dB.
- Master per bar: bars 61-62 -15.6/-16.0 (c32 -16.0/-16.1), bars 79-80 -18.2/-18.7: the climax order holds. Bar 63 -20.3 -> -21.2 (Trombone 1 heads).

## Render

- Master -21.0 LUFS, LRA 24.3, TP -2.3 dBFS; delivered -19.7 LUFS, LRA 15.7, span 17.7 dB, TP -1.6, limiter 1.4 dB. Attack probe: late or hole 0. No clipping (sample peak 0.770).
- Lock held 03:13:29-03:37:54 (24 min). Fresh restart, memory rose 24 -> 44 GB in 10 minutes and stayed flat with 0 compressed (no `--force-memory`). Audio_Init: 48000 / 512 / no input, Mac Studio Speakers. 138 GB free, MAC DRIVE mounted. REAPER 44 GB after the render (45 GB, 27 compressed, after the --mix-only write).
- Not done: `fit_rebows.py --stems` refit for the div-track coda re-bows (their old full-section fills were dropped); the harp's per-dynamic level re-check after the sustain change.
