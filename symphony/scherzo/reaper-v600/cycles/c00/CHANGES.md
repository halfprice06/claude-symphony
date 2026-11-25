# Cycle 00, part 2: baseline render of the scherzo port

No critic reports this cycle and no musical tuning. The port is described in `PORT.md` (part 1). This file covers the build, the render, the measurements and the open items for c01.

## What was done

- parts.json: generated with `score_to_parts.py`, then `space_rebows.py --write` (0 moves), then generated again. No WARNING. 31 tracks, 5671 notes. Logs: `build/s2p.log`, `build/lily.log`.
- REAPER lock: taken at 07:10:41 after waiting about 24 min for the finale thread (owner mvt3, "mvt3 c00 port build"), released at 07:36:10, so held for 25.5 min. No other owner's lock was touched.
- `reaper_ctl.py start` and `open`. The project was the header-only .rpp, 0 tracks.
- Full build: `build_reaper.py build/parts.json jobs` with an empty `jobs/`. All 31 tracks were built with `okset` true in 68 s. 321 tempo markers, no mismatches, pre-roll 3 s, end at 281.47 s. Log: `build.log`.
- `reaper_ctl.py restart`: 31 tracks. Memory settled after about 10 min at 45 GB (0 GB compressed at 07:23, then 21 GB compressed from 07:24 on, steady). `/Volumes/MAC DRIVE` was mounted and 107 GB were free.
- Audio device reopened with `jobs/audio_init.lua`: 48000 Hz, 512, input "CoreAudio " (none), output Mac Studio Speakers.
- `render_cycle.py 0`: the memory gate refused at 21 GB compressed. The rerun with `--force-memory` (the audio-device check stays on) rendered, measured, probed and delivered in 6.7 min (07:26:19-07:32:59). Log: `render_cycle.log`.
- No stem fix. `reaper_ctl.py quit`, then `unlock`. The saved .rpp has `RENDER_1X 1` and 31 tracks.
- After the render: `build/probe.json`'s Violins I 756 reference was replaced by Violins I 90 (a probe artefact, below). `cycles/c00/port/` holds the port checks.

## Key numbers

- **Master** (`render/00_Master.wav`): -19.7 LUFS integrated, LRA 20.8 LU. The sum overshoots full scale: true peak +2.7 dBFS, float sample peak 1.367. `render_cycle.py` replaced the clipped 24-bit master with the float sum of the stems (Movement I's c00 had the same, peak 1.11). The overshoot is at 240.9-242.8 s, the fff summit, bars 336-338.
- **Delivered mp3** (`cycles/c00/scherzo-mockup-c00.mp3`): -20.0 LUFS, LRA 13.9 LU, TP -1.6 dBTP, limiter about 4.9 dB on the loudest sample peak, p10-to-max span 20.5 dB, ride +10.0 / -1.5 dB, length 280.25 s. The limiter is over the brief's 3 dB and the LRA is under its 14-16 LU (BRIEF item 6). Pre-limiter peaks: 242.78 s +3.4, 241.93 s +3.3, 240.98 s +1.0 (all the summit), 72.08 s -0.7 (bar 104), 217.43 s -1.0 (bar 300).
- **Climax order**: the loudest bars of the master are the coda summit, 337 (-9.5 dB), 336 (-11.5) and 338 (-11.2). Next are 304 (-12.4), 104 (-13.4), 335 (-14.0) and 300 (-14.4). The summit is the loudest moment, as the score asks.
- **Attack probe**: 17 of 20 isolated attacks are on time. Timpani start +0.01..+0.08 s (limit 0.12), pizzicato 0.00..+0.02 s, Trumpet 1, Trombone 1 and Tuba at bar 101 -0.06..-0.02 s. The harp reads -0.25..-0.30 s ("early"); the earlier notes still ringing set the noise floor, so this is not a fault. Opening Horn 1 -39.6 dB, Violins I -44.9 dB. 3 flags:
  - Violins I 756 "+0.39 s LATE" is a probe artefact. The stem rises from -61 to -44.7 dB in the first 50 ms frame after the onset. The accented G5 at 759 sets the probe's 1.5 s peak, so the threshold fell after the first note. The reference was replaced by Violins I 90, which reads -0.03 s on this render.
  - String legato spread: Violins I robust SD 80 ms (limit 75), Violins II 96 ms (75). Violas (77 / 90) and celli (68 / 80) are within their limits. These limits were Movement I's at quarter 126; this is a real S2 timing finding for c01.
- **REAPER memory**: settled at 45 GB with 21 GB compressed before the render, 46 GB with 27-28 GB compressed after it. That is at the brief's 45 GB cap, with 31 instances; Movement II's 32 instances settled at 44 GB.
- **Stems**: all 31 rendered and sounding. The quietest are Harp harmonics (peak 0.026), Violin I solo (0.03) and Bass clarinet (0.051).

## Baseline checks

1. **Every track present and sounding.** Measured: 31 stems, each with signal at its notes. `metrics.md` "Silent notes" lists 4 candidates:
   - Bassoon 1 at 329 and 929 is a false alarm. The stem holds -34..-41 dB over the note; the fff median it is compared with is the tutti's.
   - Violas 585 (bar 196) is real. It is a same-pitch Leg Slur MAX re-attack (B3 584.5 -> 585 under the row change Sus MAX -> Leg Slur MAX at 584.94). The stem falls to -61 dB 0.2-0.3 s after the onset and reaches its body only at +0.6 s: the known first-note-layer case.
   - Violoncellos 816 (bar 273, a quarter at the arco change of the other strings) reads 18 dB under the median; check it in c01.
2. **Every mark read.** `port/mark_count.txt` accounts for all 13 sub. p, 15 sfp, 321 accents, every string staccato, every pizz./arco change and every hairpin. Wind staccatos are shortened sustains (`MANUAL-GAPS.md` #1).
3. **Ranges and keyswitches.** `port/range_check.txt`: every note of all 31 tracks lies inside a region of the row it plays and clear of the keyswitch keys.
4. **Tempo.** 278.5 s to qn 1128 on the parts.json map; the render's end is at 281.47 s including the 3 s pre-roll. The ramps are in the tempo map (312 of parts.json's 320 tempo points lie in the three RAMP_SPANS, 0.25 qn steps; REAPER got 321 markers with the pre-roll's).
5. **Mutes and CC70.** Read from the data: Violins II's CC15 is on from 393.85 (after its last note before the con sord. entry at 501.5) and off at 552.5 (before its senza sord. entry at 588). Every CC70 lane starts and ends at 127.
6. **Clipping.** The master sum peaks at +2.7 dBFS over the summit. The delivered mp3 is limited to -1.6 dBTP with 4.9 dB of limiting. This is level and balance for c01, not breakage, so no stem fix was made. A -4 dB timpani trim over bars 335-339 was simulated and does not lower the sum's peak (2.72 -> 2.85 dBFS). The peak comes from the correlated strings and woodwinds at fff: Violins I -5.2, cor anglais -6.4, celli -6.3, Violins II -6.9, Bassoon 1 -7.7, Flute 1 -8.2 dBFS stem peaks.

## Open for c01

- Summit loudness: master +2.7 dBFS and delivery limiter 4.9 dB. Lower the fff strings and woodwinds in bars 333-339 by roles in the volume envelope or by soft/loud trims, and keep the summit the loudest. Delivered LRA 13.9 LU is under target.
- S2: Violins I / II legato spread (80 / 96 ms).
- The lead, gap and fill rules in seconds were set for quarter 126: 111 Violins I notes and 167 celli notes are moved more than 0.1 s early (`loop/LEARNINGS.md`, Timing).
- Violas 585 same-pitch legato hole; Violoncellos 816.
- Port decisions to revisit: wind staccato rows (`MANUAL-GAPS.md` #1), timpani hard sticks (#6), basses div. octaves (#9), the Violins I natural harmonic (#14), the Movement I mix gains on this score (trumpets at f -34.7/-36.7 against horns -38 and strings -35..-39 dB stem medians).
