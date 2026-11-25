# Cycle 28: changes (actor)

There was no ONE_TIME.md. The critics made 12 findings. 11 were accepted: A #1-#2, B #1-#5 and C #1-#4. C #3 went in as a test. A #3 (the a2 trumpets) was deferred again.

parts.json changed in three ways:
- harp velocities at 14 onsets (A #2);
- CC11 and CC1 on the held letter-G notes (C #1);
- volume envelopes.

Note durations and keyswitches did not change, and the tempo map is the same. REAPER got all 33 tracks through `build_reaper.py build/parts.json jobs --midi-only`. Every track stayed `midi_only`, so no Opus state was reloaded. The celli's new loud-EQ band (C #3) went in through the same path.

After the render, one level-only stem fix was applied to 29 tracks with `stem_fix.py 28 cycles/c28/rendered_build build --apply`. It was then written to REAPER with `--mix-only` (all tracks) from a fresh start, and saved.

Files:
- `before/`: the c27 tools and data.
- `rendered_build/`: what the render was made from.
- `render_first/`: the master and the 29 stems as rendered.
- `actor_scripts/c28check.py RENDER_DIR PARTS`: measures every c28 pass criterion. A = A-weighted, K = approximate K.
- `check_c27.txt`, `check_c28.txt`, `check_c28_final.txt`: its output on c27, on c28 as rendered, and on c28 after the stem fix.
- `c27check_c28.txt`: c27's battery on c28. It covers the fugato, the Clarinet 1 state, the low bands and the brass groups.

REAPER steps:
1. Fresh start, open (33 tracks), `--midi-only` (all tracks), save, quit. The quit timed out, so REAPER was killed after the save.
2. Fresh start, open, `render_cycle.py 28`.
3. Stem fix, then `render_cycle.py 28 --measure-only`.
4. Fresh start, open, `--mix-only` (all tracks), save, quit. REAPER was killed after the save.

## Accepted

| Finding | Change | Measured, c27 -> c28 (final) | Pass? |
|---|---|---|---|
| A #1 coda cello solo (bars 172-174) | `LEVEL_SHAPES` Violoncellos: A's exact steps at 689.18-690.34 (+5) and 690.80-693.0. These add to the c26 691.6 crest shape. Cor anglais +4 over 684.1-687.2. Stem fix after the render: 691 step 3 -> 3.5, and the 692 step 2.5 -> 4.0, held flat through the 691.95 join and falling to 1.5 by 693.0, 0 at 693.8 | Master per note: 688 -33.1 -> -32.7; 689.5 -36.0 -> -33.4; 690 -32.6 -> -32.0; 691 -36.4 -> -33.4; 691.5 -35.4 -> -32.1; 692 -32.9 -> -30.8. The largest note-to-note fall is now 1.4 dB, and 692 is the loudest note of 684-694 (685 -31.2). Celli 30 ms peak over the 692 body +4.0 -> +2.2. Cor anglais 684 -41.2 -> -37.7 against its pickup at -35.8 | yes (the peak is 0.2 dB over A's limit) |
| A #2 harp, bars 47-59 | `VEL_SET["Harp"]` with A's 14 velocities. The patch file shows two RR groups, Pluck Lng and Thumb Pick, each with its own velocity layers (Pluck p/mp at 57/58, Thumb mp/mf at 70/71), so velocity does not move the RR order. The response was 0.6-1.0 dB per step, not 0.4: 185.5 -13.1, 198 +11.4, 222 -11.8, and bar 59 alternated ±7..9 dB. Stem fix: exact steps on the attack, held to the next onset (`_h28`: 185.5 +4.5, 190 +2, 198 -5.5, 200.5 -2, 206 +3, 222 +4.5, 231 +3, 234/234.5/235/235.5 +5.5/-5.5/+3.5/-3.5) | Single notes outside ±3.5 dB of their bar's median: 17 -> 5 of 52. p10-p90 11.2 -> 5.6 dB. The listed onsets are now within -1.1..+0.7, except 235.5 at +2.8. The 5 left are unlisted bar-54 notes (212.5-216.5, +4..+6). Harp max re master at +0.1 s: -1.0 -> -4.0 dB | mostly (A's -6 dB master limit not met; bar 54 not in A's list) |
| B #1 violas, bars 19-21 | roles.json Violas [77.5, 82.75, +5, 0.5]. Stem fix: +6.5 (as rendered, 78-82 rose only 2.5-4.8 dB) | Violas A re M: 76 -7.8 -> -4.6, 78 -12.1 -> -8.3, 80 -12.0 -> -7.0, 81 -13.8 -> -7.7, 82 -11.0 -> -9.8. Violins I is 5.7-8.8 dB over them, and they are 2.1-6.2 dB over Violins II | yes |
| B #2 letter G Flute 1 / Oboe 1 | roles.json [463.5, 479.5, +4, 1.5] on both | Re M A, 464-476: Flute 1 -15.0..-17.2 -> -10.6..-13.8, Oboe 1 -15.0..-17.3 -> -11.4..-13.7. Gap to Violins I: Flute 2.9-7.1 dB, Oboe 4.6-8.1 dB (c27 8-11). 2-5 kHz fronts unchanged: Fl1 front-body median -1.4, Ob1 -3.0 -> -2.7; master front-pre median -0.2 -> 0.0 | mostly (Oboe 468-470 still 7-8 dB) |
| B #3 Violins II pp chords | roles.json Violins II [211.5, 218.25, -4, 0.5] and [610.5, 618.0, -4.5, 0.5] | 612-618 -7.3..-8.8 -> -11.2..-13.0 (A re M). The cor anglais is now within ±2 dB of them. 213-218 -10.3..-7.6 (c27 -8.5..-5.4). At 215 they are level with Clarinet 1 (-8.2 / -8.4), where B asked for Clarinet 1 1.4-2.3 dB over | mostly |
| B #4 basses G2/A♭2 | pitch_trims.json Double basses 43/44 -6. Every other G2/A♭2 onset is in `_skip_onsets`: 20, 22.003, 184, 340, 344, 413, 554, 555.5, 612, 614, 654 | Master 85-120 Hz minus 300-2 kHz: bar 12 -5.5 -> -10.8, bar 14 -7.1 -> -10.8, 356-358 -1.5 -> -5.3, 358-360 +1.0 -> -4.0. Cb K re M in bar 12 -7.8 -> -13.2 | yes |
| B #5 bass clarinet | roles.json Bass clarinet [440, 456, -3.5, 2.0] (from 440, not 439.5, to keep it clear of the [432, 440, -2] row) and [703.5, 707.5, -3, 0.5]; Clarinet 1 [705.75, 707.75, +2.5, 0.25] | 440-450 BCl re M -6.8..-12.8 -> -9.8..-16.2, under Violins I by 4.8-11 dB, with Bn2 and celli at -10.7..-19. 704-706: BCl -9.6/-9.1/-8.1 against Cl1 -5.7/-6.4/-6.7 | yes |
| C #1 letter G sag | `ARRIVAL_HOLD_SPANS` [(464, 480)]: swell_sost on long notes. The CC11 holds at 118 instead of 118 -> 109. Stem fix: `_all` +0.8 dB over 468.5-482, gone by 483.5 | Master K, 2 qn windows from 464: c27 -13.9 -14.8 -15.1 -15.9 -16.2 -16.4 -15.7 -16.0 \| -14.5. As rendered: -13.6 -14.3 -14.7 -15.6 -15.3 -15.3 -15.3 -15.4 \| -14.5. Final: -13.7 -14.3 -14.0 -14.8 -14.5 -14.5 -14.5 -14.6 \| -13.7 -12.2 -9.1. 468-480 now sits within 0.8 dB of 464-466, and bar 121 is at or over the plateau. Delivered 117-120 S median -16.48 -> -15.53, max -14.70 -> -14.60 | yes |
| C #2 violas, letter F | `METRIC_BOWED["Violas"]` += (384, 408) | Beats 1/3 minus the other eighths (first 80 ms) -0.10 -> +1.10 dB. Violas mean 384-408 -36.24 -> -36.21 | yes |
| C #3 celli low-mid (test) | mix.json Violoncellos `loud_eq` bands += bell2 200 Hz +3 dB, 1 oct. Stem fix: celli roles [104, 124, -0.8, 0.5] and [464, 480, -0.8, 0.5]: as rendered, the celli rose 1.2-1.3 dB K re M in bars 27-31 and 117-120 | Master loud frames (top 10%, 0.4 s) re 250-2 kHz: 160-250 Hz -8.75 -> -7.11 (+1.64), 100-160 -12.09 -> -12.03, 60-100 -14.76 -> -14.52 (+0.24). Soft frames within 0.02. Celli K re M in bars 27-31 / 117-120 as rendered +1.3 / +1.2; after the roles +0.6 / +0.4 (other loud windows +1.4..+2.0, where the celli carry the bass line). Master sample peak 1.541 -> 1.531 | yes, except bars 27-31 at +0.6 (by measurement; whether it sounds boxy is not known) |
| C #4 Tempo I | `LEVEL_SHAPES["_all"]` (711, 0) -> (712, +1) held to the end. Stem fix: +1.5 (+1 gave span 19.6) | Delivered span 19.9 -> 19.4 dB. Tempo I S median -31.21 -> -29.92, still 1.1 dB under bars 175-178 (-28.81) | yes |

## Rejected / deferred

- **A #3 (Trumpets a2 on a 34th track):** deferred again. It needs a cycle with its own render and memory headroom.
- **A #2 as written:** A's velocity table alone overshot, because the response was about twice A's 0.4 dB per step. The velocities are kept, and the residual was corrected with level steps on the stem (see above).

## Before / after (c27 final -> c28 final)

| | c27 | c28 |
|---|---|---|
| Master integrated | -16.5 LUFS | -16.2 LUFS |
| Master LRA | 22.3 LU | 23.0 LU |
| Master sample peak / true peak | 1.541 / +3.8 dBFS | 1.531 / +3.7 dBFS |
| Delivered integrated | -19.8 LUFS | -19.7 LUFS |
| Delivered LRA | 15.0 LU | 14.7 LU |
| p10-to-max span | 19.9 dB | 19.4 dB |
| Delivery limiter | 2.3 dB | 2.0 dB |
| Delivered true peak | -1.7 dBTP | -1.7 dBTP |
| Motion, mp3 (dS4 p90 / 1 s-20 s) | 8.69 / 4.54 | 8.80 / 4.56 |

- **Climax order** (delivered S max): 160 -10.07 > 122 -11.01 > 167-170 -13.20 > bar 26 -14.42. In c27: -10.02 / -11.05 / -13.04 / -14.50.
- **Attack probe:** 0 flagged (12 checks).
- **Item 7:** the loop scan (`cycles/c25/actor_scripts/loopscan.py`) of every held note of 6 s or more matches c27 within 0.05 in autocorrelation. Master Lento / 175-178 / 179-182 / 160-164 band at 3.95 s: +0.40 / -0.08 / -0.38 / -0.51.
- **Item 8:** accent data is unchanged outside letter G. The letter-G fronts are unchanged (see B #2).
- **Clarinet 1 state:** 414 and 422 rendered bright again. With the c27 cut in place, the stem front-body reads -1.2 / +2.3 and the master front-pre +1.3 / +4.3. The c27 shapes are kept.
- **REAPER memory:** 18 GB with 0 compressed at the render start, 46 GB with 28 GB compressed after the render (`metrics/memory.txt`). Another process (com.apple.Virtualization) held 2.7 GB plus 4.7 GB compressed.

## Notes for c29

- **C #3 is a test.** Keep it only if a listener does not hear the celli as boxy in the loud tuttis. If it is reverted, remove the bell2 band and the two -0.8 celli roles together. That is level and EQ only: `--mix-only`.
- **Harp bar 54** (212.5-216.5): the unlisted notes are +4..+6 / -4..-6 against their bar. The harp's peak re master is -4 dB (A wanted -6). Use exact steps from this render rather than velocities, since the velocity response crosses layers.
- **Clarinet 1 414/422** shapes: still per-render. Re-check them on every render.
- **Violins II at 215** are level with the Clarinet 1 mp solo. B asked for the clarinet to be 1.4-2.3 dB over.
