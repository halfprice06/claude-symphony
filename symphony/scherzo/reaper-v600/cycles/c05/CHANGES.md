# Cycle 05 (actor), on the c04 render and the critics' reports A, B, C

No ONE_TIME.md this cycle. Snapshot in `before/`; the data rendered is in `build_render/`. Measurement scripts: `cycles/c05/actor_scripts/gp.py` (G.P. decay), `m5.py` (one check per accepted finding), `pchk.py` (parts.json diff). `m5_c04.txt` / `m5_c05.txt` hold the before / after output.

## Changes

No tool changes this cycle. Data only:

1. **Hall length (critic C #1, coordinator note).** `mix.json reverb.ir_setup` endPos 0.5 -> 0.7 and decayLength 0.5 -> 0.7 (envelopeMode 2 unchanged). This is the value Movement II adopted at its c40 for the same reason (its `build/mix.json` `ir_setup._doc`; its LEARNINGS: 21.4 dB at +0.3 s, a hall plateau at -24..-31 dB out to 0.8 s). `fx_volume` 0.095, the 160 Hz low cut, the IR, wet and the sends are unchanged (Dan's S4). It changes every Opus state, so all 31 tracks were fully rebuilt.
2. **Coda build, Violins II Spiccato regression (critic B #2, coordinator note).** c04 moved the coda's staccato pairs (981-1005) onto the tutti staccatissimo rows. `ROW_TRIM_DB`'s string branch trims only notes that have a Leg-row note within 3 qn, and these all-staccato bars have none. So Violins II's "Spiccato RRx9" (-3 dB in the table) played untrimmed, 7-12 dB over c03. Fix in `roles.json`: Violins II `[984, 995.5, -7]`, Violas `[984, 995.5, +3]`, Violins I `[987, 995.5, +2]`, all back to 0 by the ff head at 996.
3. **Hemiola accents (critic A #1).**
   - `accent_bodies.json` (empty until now): -3 dB on the strings and -2 dB on the cor anglais at the eleven `_HEM` onsets (300-310, 902-910), with the existing `ACCENT_BODY_S_SHORT` (0.18, 0.28) s. The oboes have no accent there, so they got no cut. At 902 the strings get no cut: the new 0.2 s lead on 904 leaves no room after 0.28 s.
   - `REATTACK_LEAD_AT`: Violins I 302-310 0.13 s; 902 / 904 0.20 s on Violins I, Violins II and celli, 0.18 s on violas. Violins I 300 follows a rest, so it was dropped.
   - `VEL_SET` Violins I / II 904: v65 -> v85.
4. **Violins II con sord. arpeggios (critic A #2).** `GROUP_LEAD_AT["Violins II"] = [(501.5, 587.5, 0.05)]`. Every note now moves 0.05 s. Before, the group heads moved 0.12 s and the followers 0.
5. **Horn 1 tenuto repeats (critic A #3).** `WIND_REP_RETONGUE_BY` now starts with `"Horn 1": {gap_s 0.035, frac 0.15, fall_cc 4, fall_s 0.08}`, ahead of "Horn" (the lookup takes the first prefix match), and `RETONGUE_LEAD_S["Horn 1"] = 0.09`. I first tried a per-onset `REATTACK_LEAD_AT` on the five repeats. It ended the old note 0.02 qn before the moved onset, a 5 ms gap, so I dropped it. As a side effect, all 54 Horn 1 re-tongues in the piece now start 0.04 s earlier.
6. **Soft arco entries after pizz. (critic A #4).** `entry_leads.json`: Violoncellos 504 +0.10 s and 756 +0.07 s; Double basses 840 +0.07 s.
7. **Accent levels (critic A #5).** `tools/fit_accents.py 4 cycles/c04/build_render/parts.json --family string --write`, then `--family wind --write` (`actor_scripts/fit_string.log`, `fit_wind.log`). I removed 29 fits by hand:
   - the hemiola onsets (item 3);
   - 899, the accent before the sfp, where the neighbours lie across the trough (it would have trimmed Violins II and the celli by -6 dB);
   - 1005, the summit, which has `ARRIVAL_WEIGHT_AT`;
   - Violins I's Marc LITE heads, fitted in c02-c03.
8. **Viola portato pairs (critic A #6).** `STR_REP_NEW_BOW["portato"]`: gap 0.05 -> 0.08 s, frac 0.25 -> 0.3, fall 6 / 8 -> 12 / 14 CC, fall time 0.04 -> 0.08 s.
9. **Flutes in the ff tutti theme (critic B #1).**
   - `ROW_TRIM_DB` Flute 1 / Flute 2 `"Stac DblTng RRx9": (+6, 100)`: the ff staccatos only.
   - `roles.json`: Flute 1 315 / 351 -7, 915 / 951 -6, 999 -4; Flute 2 315 / 351 -3.
   - C #3's blanket -3 over the a2 spans was not added on top (item list below).
10. **Oboe 1 as the leading voice (critic B #3).**
    - `LEVEL_SHAPES["Oboe 1"]` over 827.5-840.5: +7, then +2 at the hairpin peak, then +4.
    - `roles.json`: Oboe 1 672-676.5 +4 and 1032-1041 +4; Clarinet 1 1032-1041 -2; Flute 1 834-836 -3.
11. **Retransition bass clarinet pedal (critic B #4).** `roles.json` Bass clarinet `[732, 756, -5]`.
12. **sfp trough (critic B #5).** `roles.json` Flute 2 `[900, 906, -6]`, Horns 1 and 2 `[900, 906, -3]`. The ramps end on the note-on, so nothing falls while the hall tail rings (S3).
13. **Celli in the G major second idea (critic B #6).** `roles.json` Violoncellos `[132, 156, -3]`.
14. **Close-only DIV tracks (critic C #2).**
    - `mix.json` Violas div: a high shelf at 2 kHz, -4 dB.
    - Violin I solo: the high shelf moved from 5 kHz -4 to 2.5 kHz -5.5.
    - `roles.json` Violas div `[648, 672, -3]`.

parts.json: no WARNING. No track's set of articulation rows changed, so memory is unchanged; the full rebuild comes only from the hall. Tracks whose data changed: Flutes 1-2, Oboes 1-2, cor anglais, Clarinets 1-2, bass clarinet, Bassoon 1, contrabassoon, Horns 1-2, Violins I/II, violas, celli, basses, Violas div.

## Rejected / deferred

- **C #3** (flutes -3 over the whole a2 spans). B #1 targets the same flutes more precisely: it raises the staccato head and cuts the top notes. Stacking both would leave the head 5-12 dB under Violins I. The flute-pair-minus-Violins I numbers are re-measured below.
- **C #4** (`reverb.width` 1.5). Optional and untested in any movement. It would also widen the hall that Dan called too wet, and it would mix a stereo change into the G.P. decay measurement. Deferred.
- **C #5** (timpani hard sticks, MANUAL-GAPS #6). A large change: a patch swap plus a second track for the soft-stick coda, and every roll level re-fitted. Deferred.
- **A #1(a) for the oboes.** They have no accented note at the hemiola onsets, so there is nothing to cut.
- B's unranked notes (Violins I's harmonic, Flute 1 at 780-804): left as the critic advised (check by ear).

## Stem fix

`tools/stem_fix.py 5 cycles/c05/build_render build --apply "Flute 1" "Violin I solo"`. The originals are in `render_first/`. The same data went into REAPER with `--midi-only` and a save before the quit. Then I ran `render_cycle.py 5 --measure-only`.
- **Flute 1's accented G6.** With the -7 / -6 roles and a fitted swell of 0 (fit_accents dropped the 3.5 dB gentle swell), the G6 came out 4.5-5.4 dB under Violins I. The two cuts were counted twice. Roles changed to -4 at 315 / 351 and -3 at 915 / 951.
- **Violin I solo.** It sat only 2.9 / 1.7 dB over Flute 1 after the darker shelf. Role 1044-1068 changed from +7 to +8 (the critic's fallback).

## Measured (c04 -> c05; `actor_scripts/gp.py`, `gpslope.py`, `m5.py`, `s1.py`, `pcxchk.py`; plain RMS)

**G.P. after the fff summit (C #1), for the shared guide.** Master level drop after the last note-off (qn 1015.81) against the last chord's body, 50 ms windows. "Without timpani" is the stem sum minus the drum, and it is identical within 0.4 dB.

| render | +0.1 s | +0.2 s | +0.3 s | +0.45 s | +0.6 s | +0.8 s | +1.0 s | +1.3 s |
|---|---|---|---|---|---|---|---|---|
| c04, endPos / decayLength 0.5 | 11.2 | 16.8 | **21.9** | 31.5 | **36.8** | 43.7 | **50.1** | 57.9 dB |
| c05, endPos / decayLength 0.7 | 12.9 | 17.5 | **22.2** | 31.5 | **34.8** | 41.7 | **47.5** | 54.8 dB |

- Absolute master level from the G.P.'s start (qn 1017) at +0 / +0.3 / +0.6 / +1.0 s: -41.5 / -55.9 / -66.8 / -75.1 -> -41.3 / -53.8 / -63.2 / -72.6 dBFS.
- Fitted late slope on the master:

  | fit range | c04 | c05 |
  |---|---|---|
  | -12..-40 dB | 48 dB/s (T60 1.25 s) | 41 dB/s (T60 1.47 s) |
  | -25..-45 dB | 34 dB/s (1.77 s) | 29 dB/s (2.07 s) |
  | -5..-25 dB | 51 dB/s | 51 dB/s (unchanged) |

- Reading:
  - 0.7 lengthens only the hall's late tail, by 2-3.5 dB from +0.6 s on. The first 0.3 s is the release-capped samples plus the early hall, and it did not move: +0.3 s changed 21.9 -> 22.2 dB.
  - The late decay now reaches the bottom of the brief's 1.5-2 s.
  - It still misses critic C's targets of 24-31 dB at +0.6 s and at most 45 dB at +1.0 s.
  - Movement II measured 21.4 dB at +0.3 s with the same values (slow movement, final chord), which agrees.
  - A longer tail at the G.P. would need endPos nearer the factory 1.0 or longer release caps. Neither was tried: both are shared values.
- **S1 side effect.** Median master pair dip over twelve theme-head and coda eighth pairs: 2.7 -> 2.2 dB. The coda pairs 1003 / 997 fell from 4.7 / 3.0 to 2.5 / 2.0. That comes partly from the longer tail and partly from the Violins II cut.

**Hemiola (A #1).** Master front minus body (0-0.1 s against 0.2-0.4 s):

| onset | 300 | 302 | 304 | 306 | 308 | 310 | 902 | 904 | 906 | 908 | 910 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| c04 (dB) | -4.3 | -5.8 | -1.9 | -2.8 | -0.3 | -2.2 | -1.7 | -1.4 | -1.7 | -2.4 | -2.2 |
| c05 (dB) | -2.6 | -5.0 | -1.1 | -1.6 | +1.2 | -0.7 | -2.0 | -1.1 | -2.0 | -1.5 | -0.4 |

- Violins I stem: 902 -9.3 -> -0.5 dB, 904 -9.9 -> -5.4.
- Better at 9 of 11 onsets, but short of the +1 dB target. Master peaks still fall 140-430 ms after the beat. Partial.

**Violins II arpeggios (A #2, pcx).** Heads -0.012 -> -0.003 s, followers +0.050 -> +0.025 s (medians; 16 / 64 notes). Within target.

**Horn 1 repeats (A #3).**

| onset | 630 | 633 | 639 | 651 | 663 |
|---|---|---|---|---|---|
| dip, c04 (dB) | 11.9 | 11.8 | 8.5 | 7.5 | 11.3 |
| dip, c05 (dB) | 11.4 | 9.6 | 3.1 | 5.7 | 9.6 |

Two of five are now in the 3-6 dB target. The sample's own decay remains (next step: MANUAL-GAPS #10, the 1FH "Port Lng" row).

**Soft arco entries (A #4, pcx).**
- Celli 756: +0.080 -> +0.025 s. Basses 840: +0.083 -> +0.037 s. Both within target.
- Celli 504: +0.112 -> +0.155 s, worse with 0.10 s more lead. Open: check the stem by hand before adding more.

**Viola portato (A #6).** Median dip: Violas 1.8 -> 3.6 dB, Violas div -1.0 -> +0.7 dB. Partial; the div track is still flat.

**Flutes (B #1, after the stem fix).**
- Flute 1 G6 against Violins I: +6.3 / +2.8 -> -2.4 / -1.5 dB.
- G6 over its own staccatos: 18.4 / 15 -> 5.1-6.4 dB.
- Flute 1 staccato head up about 6 dB.
- Flute pair against Violins I in the 12 qn windows: +2.3 / +3.2 / +1.2 / +1.9 -> +0.7 / +1.2 / -0.8 / -0.1 dB. C #3's 0..-2 target is met in two of four windows.

**Coda build (B #2).**
- Violins II in qn 984-993: -36.6 / -31.3 / -26.8 / -25.7 -> -43.6 / -38.3 / -33.8 / -32.6 dB.
- Violins I over Violins II: +9.4 / +5.2 / +1.2 / -2.5 dB (critic's target +10.4 / +6.4 / +1.8 / -1.0).
- Violas +3 dB.
- Master 0.5-2.2 dB lower in the build.

**Oboe 1 (B #3).**
- 828-840: was 6.5-12 dB under Flute 1; now 0.7-5.7 under, and 2.5 dB over at the hairpin peak (832.5).
- 1032-1041: level with Clarinet 1 on the first beat, then 3.4-6.2 dB over it.
- 672: -46.9 / -44.4 dB, over Violins II.

**Bass clarinet (B #4).** 744-753: was +4.4..+5.0 dB over Violins I; now -0.1..-2.8 dB under (plain RMS).

**sfp (B #5).**
- Flute 2 at 900-904: -35 -> -41..-42 dB.
- Horns 1-2: 2.6-3.0 dB lower.
- Master trough 901-902: -29.7 / -28.9 dB (c04 -27.6 / -27.9).

**Celli in the G major second idea (B #6).** Celli minus Violins I over 132-156: was -0.8..+6.7 dB; now -4.9..+0.6.

**DIV tracks (C #2).**

| track, window | level against its section | hi-mid tilt | section's tilt |
|---|---|---|---|
| Violas div, 624-648 | -0.8 dB | -9.3 -> -12.2 dB | -12.6 dB |
| Violas div, 648-672 | -0.3 dB | -8.0 -> -11.0 dB | -12.6 dB |
| Violin I solo | | -1.9 / -0.8 -> -4.8 / -3.9 dB | Violins I -5.1 dB |

The solo now sits 3.9 / 2.7 dB over Flute 1.

**Accent fits (A #5).** Not measured separately (next critics).

## Render

- **Lock.** Waited behind the finale thread (held 10:18-12:06) and Movement I's waiter, which had waited longer: Movement I held the lock 12:06:36-12:09. I held it from 12:09:01 to 12:34:07 (25.1 min) for:
  - the full build of 31 tracks (65 s);
  - restart (memory settled at 45 GB, 0 compressed);
  - audio_init and the render (6.5 min, no forced memory gate);
  - the stem fix and `--midi-only` of 2 tracks, save, quit, unlock.
- **Disk.**
  - Before the lock I deleted this folder's c03 stems and the old REAPER backups.
  - The render still ran at 28 GB free, because other threads' renders had used space; the auto-mode classifier refused to delete the c04 stems before my render was checked.
  - After the checks I deleted the c04 non-master WAVs, including render_first's Trumpet 1 stem. Every 00_Master.wav and mp3 is kept.
  - **33 GB free at the end.**
- **REAPER memory.** 45 GB settled (0 compressed) before the render; 45 GB (27-28 GB compressed) after.
- **Master.** -20.5 LUFS integrated, LRA 23.1 LU, true peak -1.2 dBFS, sample peak 0.872 (no clipping).
- **Delivered** `cycles/c05/scherzo-mockup-c05.mp3`:
  - -19.9 LUFS, LRA 13.9 LU (c04 14.3; the target is 14-16), TP -1.6 dBTP, limiter about 2.9 dB, p10-to-max span 19.2 dB.
  - Delivered bar 337 is 3.8 / 3.9 / 3.5 dB over bars 104 / 304 / 72 and 2.0 dB over bar 300 (c04: 3.5 / 3.4 / 3.8 / 2.3).
- **Attack probe.** All 20 attacks and the opening are ok. The legato spread is flagged on Violins I only: 77 ms against the 75 ms limit (c03 75, c04 76; pre-existing). The violas read 92 ms (limit 90, ok); in c04 they were flagged at 116 ms.

## Open for c06

- G.P. hall: +0.6 s at 34.8 dB and +1.0 s at 47.5 dB, still short of C's targets. The next step would be endPos nearer 1.0, a shared value: decide it with the other threads.
- Hemiola fronts still under their bodies on the master (-5.0..+1.2 dB).
- Horn 1 repeats at 630 / 633 / 663 still 9.6-11.4 dB: try the 1FH Port Lng row (MANUAL-GAPS #10, 775 regions).
- Celli 504 entry late at +0.155 s.
- Violas div portato flat.
- Delivered LRA 13.9, just under the 14-16 target.
- Every Horn 1 re-tongue now starts 0.04 s earlier (side effect of item 5): check Horn 1 against Horns 2-4.
- Deferred: C #4 hall width, C #5 hard sticks.
