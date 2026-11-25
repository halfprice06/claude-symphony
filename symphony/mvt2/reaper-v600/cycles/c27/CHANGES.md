# Cycle 27, part 2: baseline render of the v600 port

No critic reports this cycle and no musical changes. The port itself is in `PORT.md` (part 1). This file records the build, the render, the measurements and the baseline checks.

## What was done

- `cycles/c27/before/`: snapshot of `tools/*.py`, `build/score_config.py`, `build/*.json` before the build.
- `build/parts.json` regenerated with `score_to_parts.py`: no WARNING, byte-identical to the port's parts.json (32 tracks, 1526 notes).
- REAPER lock taken 16:40:00, released 17:15:37 (35.6 min).
- Full build of all 32 tracks (`tools/build_reaper.py build/parts.json jobs`; `jobs/` was empty). The first attempt crashed: Opus segfaulted in one of its worker threads while loading Clarinet 1's state (`~/Library/Logs/DiagnosticReports/REAPER-2026-11-06-164112.ips`, EXC_BAD_ACCESS, every faulting frame inside Opus). The bridge then waited out its 600 s job timeout before reporting it. The same kind of Opus crash happened at 16:32, before this cycle took the lock. The retry, after a fresh start and open, built all 32 tracks in 59 s (`okset` true on all 32, 403 tempo markers, no mismatches).
- `reaper_ctl.py restart`, then memory settled at 43.9 GB (5.1 GB compressed) after about 9 min. `/Volumes/MAC DRIVE` mounted, 203 GB free. Audio device reopened with `cycles/c27/_c27_audio_init.lua` (48000 Hz, 512, input "CoreAudio " = none).
- `render_cycle.py 27` (no `--force` options needed). Render, measurement, attack probe and delivery took 7.3 min.
- No fixes were needed: no silent track, no wrong keyswitch, no clipping. `stem_fix.py` was not used.
- Added `cycles/c27/baseline_check.py`. For each stem it prints the peak, the notes whose span is silent, and the mean level per articulation row, with the rows new in the port listed separately. It also prints the master clip count and the Double basses' level around the "4 soli" spans. Output: `metrics/baseline_check.json`.

## Key numbers (c26 of series 1 in brackets)

- Master: -20.1 LUFS (-22.6), LRA 24.9 LU (23.6), true peak -2.0 dBFS (-4.1), sample peak 0.794 (0.626), 0 samples at full scale.
- Delivered mp3 (`cycles/c27/mvt2-mockup-c27.mp3`, Movement I's c36 `deliver_master.py`, so this is not directly comparable with c26): -19.8 LUFS, LRA 14.9 LU, TP -1.6 dBTP, p10-to-max span 17.7 dB, limiter about 1.1 dB, ride +10.0 / -1.9 dB, length 349.95 s.
- Attack probe: 1 of 20 checks flagged (c26: 3 of 21). The flag is Violins II qn 212, a 6.4 dB dip against a 6 dB limit (c26: 6.9 dB, also flagged). The note's data did not change, so this is the same tremolo-entry dip as in c26, not a port fault. Violoncellos 212 is now 5.2 dB (c26 6.2, flagged). Violins I 171 now starts 0.14 s early, within the limit (c26 0.34 s late).
- REAPER memory: 43 GB with 5.1 GB compressed before the render, and 44 GB with 25 GB compressed after it. Settled after the restart at 43.9 GB RSS.

## Baseline checks

`PORT.md` has no section titled "baseline must check". I took the items below from what PORT.md says the port changed and flagged as risky.

1. **Every track present and sounding.** Measured: all 32 stems rendered. Every note span is above -70 dBFS, with two exceptions that are not faults. The string notes at sq 0.0 start inside the pre-roll, which `baseline_check.py` cannot read (the probe's opening checks measure them at -48 to -51 dB, ok). The Double basses' last note at 303.3 is at -71 dB, the end of the ppp morendo. The div tracks sound as expected: Violin I solo, Violoncellos div, Violins II div (Flautando), Violas div and Horns 1-2 a2.
2. **New articulation rows load and play** (mean level over each row's notes): Clarinet 2 Leg Slur 12 notes at -47.2 dB; Bassoon 2 Leg Slur MAX 24 at -48.9; Horn 1 Sus MAX 4 at -33.1; Horn 3 Leg Slur MAX 8 at -49.0; Horn 4 Leg Slur MAX 5 at -47.8; Double basses Leg Slur MAX 6 at -47.6; Violoncellos div Leg BC MAX 1 at -49.9; Violas div Sus MAX 8 at -53.8; Horns 1-2 a2 Sus MAX 2 at -40.7. None is silent, and each sits within a few dB of the same track's other rows at similar dynamics.
3. **No clipping.** Master sample peak 0.794, 0 samples at or above 0.999. The loudest stem peak is Violins I at -6.6 dBFS.
4. **Final chord mutes stay on ("via sord." after the last note is ignored).** Read from the data: the CC15 lanes end at 127 (Violins I from 274.5, Violins II and Violas from 273.5, Violas div from 268.5), with no off event after them.
5. **Held tremolos in bars 61-64 not re-bowed (`AUTO_REBOW_SKIP_TREM`).** Read from the data: the string Tremolo keyswitches at 211.94 (Violas 203.94) run to 217.94 with no re-bow keyswitch between. The only re-bow in that span is Violins I 205.9 on Sus MAX, which is not a tremolo.
6. **Violins II div Flautando re-bowed on Flautando (`REBOW_SAME_ROWS`).** Read from the data: the keyswitches at 117.5 and 121.5 are Flautando. Measured: all 8 notes are Flautando, mean -53.7 dB, none silent.
7. **Allargando from qn 216 (`RAMP_SPANS`).** Read from the tempo map: 54 bpm until 216, then a ramp of 53.25 to 39.4 bpm over 216-219.75, then Tempo I 52 at 220. The tempo markers were verified in REAPER with no mismatches.
8. **SOLI_AS_META on the basses (220-238, 286-304) and celli (274-286).** In the data, as the -3 dB "half" segments of the volume envelope. On the stem it cannot be measured separately from the loop profiles and roles. The Double basses read -48.0 dB at 214-220, -54.6 at 220-226 and -53.0 at 226-238 (the bar 64 ff is followed by the pp pedal).
9. **Climax still the loudest (BRIEF item 6).** Measured, and this one fails. The mix bar levels are 61: -16.3 and 62: -16.4, against 79: -15.6 and 80: -16.3. In c26 the climax was 2 dB above bar 79. The cause is the score: v600 prints ff where v77 printed f (celli and others in bars 79-80; the cor anglais and the Violas div now play there). Strings in bars 79-80 are 4-6 dB up on c26, and the master's 5 highest pre-limiter peaks are at qn 262-265. This is a level and balance question, not port breakage, so it is left for c28.
10. **Notable level change from the score: the bass clarinet pedal in bars 3-6.** Measured: +6 to +7 dB over c26 from qn 9 (stem -48.5 to -42/-40 dB at pp), so it is the loudest stem in bars 4-5. v600 ties the A flat 2 through bars 3-6, so it is now one 11 qn Sus Non Vib note where v77's repeated notes were re-tongued (c23 `REP_RETONGUE_AT`, now a dead entry for this onset; the same applies to Horn 4). The level climbs inside the held sample. Left for c28: it is a level and loop question, and the ties are printed.
11. **Loudness and range against c26.** The master is 2.5 dB louder and its LRA is 1.3 LU wider. Bars that changed by 2 dB or more: up in 4-5 (bass clarinet), 35-36 (bass clarinet solo an octave lower, now mp) and 78-80 (ff); down in 8, 31 and 43-44.

## Rejected or deferred

- No critic findings this cycle. Series 1's c27 critic findings and `MANUAL-GAPS.md` #1 (CC1 dynamics on brass and clarinets) stay open for c28, as the port entry in HISTORY says.
- Items 9 and 10 above are deferred to c28 (balance, not port breakage).
- The loop-pulse check on long held notes (BRIEF item 8) and the perceptual-onset check (S2) were not run. They are for the c28 critics.
