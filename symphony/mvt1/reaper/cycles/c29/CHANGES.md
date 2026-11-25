# Cycle 29: changes (actor)

There was no ONE_TIME.md. The critics made 13 findings. 11 were accepted: A #1-#4, B #1-#4 and C #1-#3. A #5 (a2 brass tracks) and C #4 (oboe seats) were deferred.

Every accepted change is level or EQ only. parts.json changed only in `vol_db` / `vol_bp` (and `pitch_trimmed` on the basses) on 12 tracks. Notes, keyswitches, CC lanes and the tempo map are identical to c28. REAPER got the changes through `build_reaper.py build/parts.json jobs --mix-only` on those 12 tracks, which also wrote the new side-channel EQs.

After the render, one level-only stem fix on two tracks (Cor anglais, Violoncellos) was applied with `stem_fix.py 29 cycles/c29/rendered_build build --apply`. The same data was then written to REAPER with `--mix-only` from a fresh start, and saved.

Files:
- `before/`: the c28 tools and data.
- `rendered_build/`: what the render was made from (parts.json, mix.json, score_config.py, build_reaper.py).
- `render_first/`: the master, Cor anglais and Violoncellos stems as rendered.
- `actor_scripts/c29check.py RENDER_DIR PARTS`: every c29 pass criterion (A = A-weighted, K = approximate K).
- `check_c28.txt`, `check_c29.txt`, `check_c29_final.txt`: its output on c28, on c29 as rendered, and on c29 after the stem fix.

REAPER steps:
1. Fresh start, open (33 tracks), `--mix-only` (12 tracks), save, quit. The quit timed out, so REAPER was killed after the save.
2. Fresh start, open, `render_cycle.py 29`, save, quit (killed after the save).
3. Stem fix, then `render_cycle.py 29 --measure-only`.
4. Fresh start, open, `--mix-only` (Cor anglais, Violoncellos), save, quit (killed after the save).

## Accepted

| Finding | Change | Measured, c28 -> c29 (final) | Pass? |
|---|---|---|---|
| A #1 cor anglais, bars 6-7 | `LEVEL_SHAPES["Cor anglais"]`: A's shape. As rendered, the A4's own rise at 23.84-23.87 kept A's +4 and read 4 dB over the A4 body, and the master join peak was 4.0 dB over the G4. Stem fix: refitted on 20 ms frames: +4 / +4.5 over 23.725-23.80, -1.5 over 23.85-23.92, -5.5 at the 23.99 join, back to 0 at 24.07, +2 over 24.10-24.60 | CA 40 ms frames 23.6-24.6: -31..-43 -> -35..-40. Master join peak minus G4 body +7.3 -> +1.7 dB (CA +8.5 -> +2.0). G4 body -38.6 -> -36.8, A4 body -37.4 -> -37.6 | yes (one 40 ms frame at -40, A's range -33..-39) |
| A #2 bar 52 Horn 1 + celli | A's exact shapes: celli +4 over 205.5-206.5, Horn 1 +3 over 205.5-206.0 and -4 over 206.12-207.8 | Hn1 + Vc per note 204 / 205.5 / 206 / 207: -31.5 / -38.4 / -32.9 / -34.6 -> -31.4 / -35.0 / -35.4 / -36.7. Master -30.8 / -37.0 / -32.1 / -34.0 -> -30.7 / -34.2 / -34.1 / -35.3. Horn 1 50 ms over 205.9-206.3 at most +1.5 dB over its 205.5 body (c28 +8.5) | yes |
| A #3 Clarinet 1 213, Oboe 1 579 | Clarinet 1 +5 over 212.72-213.04; Oboe 1 +4 over 578.96-579.40 | Clarinet 1 stem dip 9 -> 4-5 dB (-45 ... -49 ... -45). Oboe 1 E5 first 0.2 s -43.3 -> -39.3, G4 body -41.3 | yes |
| A #4 final chord celli re-bow | `rebow_fills.json` Violoncellos 723.921: A's +2.5/+5.5/+6/+6/+4.5/+2 at -0.04..+0.16 s. As rendered the sample's dip ran on to +0.24 s (-55..-57 against -51 before). Stem fix: a further -1.5 at -0.04 s and +1.5/+3.5/+3/+4/+4.5/+3/+1 at +0.04..+0.28 s | Celli 60 ms frames -51 -52 -57 -61 -58 -57 -55 -> -51 -50 -51 -52 -52 -53 -54 (dip 10 -> 3 dB). 100-300 Hz -55 ... -69 -> -56 ... -61 (hole 14 -> 5 dB). No new bump over 1 dB | yes |
| B #1 bars 103-106 counter-line | roles.json Horn 1 [407.5, 419.5, 3.5, 0.5], Bassoon 1 and Violoncellos [407.5, 423.5, 3.5, 0.5] | A re M, 2 qn windows: line group -9.1..-3.4 -> -7.5..-2.9; figure group -4.3..-1.2 -> -6.1..-1.9. Horn 1 -15.9..-12.1 -> -12.3..-9.6 (408-419), celli -14.5..-11.3 -> -11.5..-8.4 | yes (line 0.5-3.2 dB under the figure per window) |
| B #2 bars 115-116 flutes / Oboe 1 | roles.json Flute 1 and Oboe 1 letter-G rows start at 455.5; Flute 2 [455.5, 463.5, 4, 0.5] | A re M per quarter 456-462: Flute 1 -16.4..-20.9 -> -12.5..-17.4; Flute 2 -16.4..-24.0 -> -13.0..-20.2; Oboe 1 -12.5..-19.1 -> -9.2..-15.2; Violins I -7.1..-10.5 (still the top line). Master K 2 qn windows within 0.1 dB | yes |
| B #3 basses F1 / F2 / G1 | pitch_trims.json Double basses 29: +3, 41: 0 -> +3, 31: -2 | K body minus same-CC11 neighbours of other pitches (my measure, not B's): F1 -4.4 -> -1.3, F2 -3.7 -> -0.7, G1 +3.7 -> +1.7 dB median | mostly (G1 0.2 dB over B's ±1.5) |
| B #4 bar 40 trombones | roles.json Trombone 1 / 2 / Bass trombone [155.5, 159.75, -3, 0.2] | A re M: Trombone 1 -8.9..-14.4 -> -11.2..-15.8, Trombone 2 -7.9..-12.1 -> -9.7..-13.3; Violins I -8.2..-10.5 and Flute 1 now over both. Master K bar 40 -21.0 -> -21.4, bar 41 -19.4 -> -19.6 | yes |
| C #1 celli 200 Hz loud bell | mix.json Violoncellos `loud_eq` bell2 200 Hz +3 removed with the two c28 -0.8 celli roles | Master loud frames 160-250 re 250-2k -7.91 -> -9.82 dB (c27 about -9.5). Celli K re M bars 27-31 -11.39 -> -12.04 (c27 about -12.0), bars 117-120 -14.94 -> -16.02 (c27 about -15.3) | mostly (117-120 0.7 dB under c27, target ±0.5) |
| C #2 low-mid width | mix.json `side_shelf` bell 170 Hz -2 dB 1 oct on Violoncellos and Double basses | Master correlation 120-250 Hz 0.443 -> 0.534 (target 0.52-0.58), 60-120 Hz 0.666 -> 0.701 (at most 0.71), 20-60 0.583 -> 0.566. Seats 120-250 Hz R-L: celli +4.61 -> +3.96, basses +5.40 -> +4.90. Master 120-250 Hz level -1.2 dB (with C #1) | mostly (celli seat 0.65 dB, over C's 0.5) |
| C #3 celli top width | Violoncellos `side_shelf` + high shelf 1.5 kHz +4 dB | Celli stem correlation above 4 kHz 0.871 -> 0.612. Bars 85-87 master above 4 kHz 0.87 -> 0.62, 1-4 kHz 0.80 -> 0.64; bars 171-174 0.87 -> 0.61 / 0.82 -> 0.73. Whole master above 4 kHz 0.556 -> 0.552. Celli K 336-348 -0.2 dB, 680-696 +0.1 dB. Celli 1-4 kHz R-L +5.37 -> +5.96 | yes |

## Rejected / deferred

- **A #5 (Trumpets a2 / Trombones a2 on 34th-35th tracks):** deferred. REAPER ended the c28 render at 46 GB with 28 compressed (c29: 46 GB, 29 compressed), at BRIEF item 9's limit, and the a2 tracks also need per-window staves and full rebuilds. With one cycle left there is no render to check them after c30.
- **C #4 (oboe seats):** deferred. It is an Opus state change (a full rebuild of both oboe tracks) and requires an Oboe 1 accent/fill refit afterwards. C rates it small and inferred, and asked for it to be bundled with an oboe rebuild. No oboe rebuild is planned.
- **A #1 optional generic fix** (`trim_shape()` ramp capped at min(0.25 qn, 0.10 s) on joined notes): not made this late. It would move every trimmed joined note at slow tempos, and nothing would be left to check them after c30.
- **B smaller notes** (bar 143 stab tail; coda Clarinet 1 over the chorale): no change, as B advised.

## Before / after (c28 final -> c29 final)

| | c28 | c29 |
|---|---|---|
| Master integrated | -16.2 LUFS | -16.4 LUFS |
| Master LRA | 23.0 LU | 22.9 LU |
| Master sample peak / true peak | 1.531 / +3.7 dBFS | 1.524 / +3.7 dBFS |
| Delivered integrated | -19.7 LUFS | -19.8 LUFS |
| Delivered LRA | 14.7 LU | 14.6 LU |
| p10-to-max span | 19.4 dB | 19.5 dB |
| Delivery limiter | 2.0 dB | 2.1 dB |
| Delivered true peak | -1.7 dBTP | -1.6 dBTP |
| Motion, mp3 (dS4 p90 / 1 s-20 s) | 8.80 / 4.56 | 8.69 / 4.54 |
| Band shares 20-100 / 100-250 Hz | -16.22 / -8.0 | -16.84 / -8.61 |

- **Climax order** (delivered S max): 160 -9.99 > 122 -11.19 > 167-170 -13.14 > bar 26 -14.60. In c28: -10.07 / -11.01 / -13.20 / -14.42.
- **Attack probe:** 0 flagged (12 checks).
- **Item 7:** `cycles/c25/actor_scripts/loopscan.py 29`: master Lento / 175-178 / 179-182 / 160-164 band at 3.95 s +0.40 / -0.10 / -0.38 / -0.45 (c28 +0.40 / -0.08 / -0.38 / -0.51). Stems as in c28.
- **Item 8:** no accent data changed. The c27 battery: the celli fugato notes are within 0.5 dB of c28 except 340 (-1.6, Stac round robin). Clarinet 1 414 rendered bright again (stem front-body +4.7, master front-pre +2.7) and 422 +2.3 / +2.3, both under the c27 cut's target.
- **100-250 Hz share** fell 0.6 dB (C #1 and C #2 together). It is now -8.61 against the references' -6.6 / -8.75 / -7.55.
- **REAPER memory:** 27 GB with 0 compressed at the render start, 46 GB with 29 GB compressed after the render (`metrics/memory.txt`). Another process (com.apple.Virtualization) held 2.7 GB plus 4.7 GB compressed, and two python3.12 processes held 2.1 and 1.5 GB.

## Notes for c30

- The celli now carry two side EQs (170 Hz bell -2, 1.5 kHz high shelf +4). A listener should check whether the exposed celli (bars 85-87, 171-174) sound wider without a hollow or phasey top.
- The 100-250 Hz band share is at the low end of the references. C advised not to chase the 125-160 Hz shortfall with EQ, because it comes from the voicing.
- Celli K re master in bars 117-120 is 0.7 dB under c27 after the C #1 revert.
- Clarinet 1 414/422: still per render (bright on c29).
