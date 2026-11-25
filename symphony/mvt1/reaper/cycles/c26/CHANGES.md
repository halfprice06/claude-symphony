# Cycle 26: changes (actor)

There was no ONE_TIME.md. Of the 12 critic findings, 11 were accepted (A #1 with two corrections after the render). A #2 (Horns 3-4 a2 on the 2FH track, Trumpets a2) was deferred again, and A #3 was a note with no fix requested.

Every accepted change is level or EQ only. `parts.json` notes, keyswitches and CC lanes are identical to c25; only `vol_db`/`vol_bp` changed, plus the Tuba ReaEQ. REAPER got the data through `--mix-only` on the 19 changed tracks. No Opus state was reloaded and the tempo map did not change.

After the render, three level-only stem fixes were applied and written to REAPER with `--mix-only`, each from a fresh start, then saved:
1. Horn 1 (A #1 balance).
2. Violoncellos (the exposition notch).
3. Violas (the 436 trim).

Files:
- `before/` holds the c25 tools and data.
- `rendered_build/` holds what the render was made from.
- `render_first/` holds the master and the Horn 1, Violas and Violoncellos stems as rendered.
- `actor_scripts/` holds the scripts:
  - `c26check.py`: every critic pass criterion on one render folder;
  - `joinframes.py`: 50 ms frames around an onset;
  - `repdiff.py`: where two renders of one stem differ;
  - `envdiff.py` / `envpts.py`: new-minus-old volume envelope.
- `check_c25.txt` / `check_c26.txt` hold the outputs. These measures are plain stereo power except where marked K, so their numbers differ from the critics' own measures.

REAPER steps:
1. Fresh start, open (33 tracks), `--mix-only` on the 19 tracks, save, quit (the quit timed out; REAPER had exited).
2. Fresh start, open, `render_cycle.py 26`.
3. `--mix-only "Horn 1"` (fix 1), save, quit.
4. Fresh start, open, `--mix-only "Horn 1" "Violoncellos"` (fix 2), save, quit.
5. Fresh start, open, `--mix-only "Violas"` (fix 3), save, quit.

## Accepted

| Finding | Change | Measured, c25 -> c26 (final) | Pass? |
|---|---|---|---|
| A #1 dolce second theme | Celli shapes rise after the transition burst: recap `[(595.65,0),(595.95,0),(596.15,6),(597,5),(598.6,3),(599.6,0)]`, expo the same pattern to (199.6,0). `JOIN_NOTCH` celli (595.66, 595.92, -5). Horn 1 (597.6,4) -> (198.6,3)/(199.6,0) in the c24 expo shape. **Changed from A's version after the render (fix 1):** A's Horn 1 falls (-4 / -2.5 held to 599.5 / 199.5) were simulated and rendered at Horn 1 - celli -5.6 / -4.4 dB over the 598/198 half notes (c25 -0.4 / -2.4; A's own pass is within 2). The c09 Horn 1 cuts now end rising into the join: recap `[(596.1,0),(597.5,-3),(598,0),(598.6,1),(599.6,0)]`, expo `[(196.1,0),(197.5,-2),(198,0),(198.6,1.5),(199.6,0)]`. Horn 1 598 join sag (10 dB at +0.15..+0.6 s) gets `LEVEL_SHAPES_S` (598.0, +2.5 from +0.2 to +0.55 s). **Fix 2:** the expo notch (195.66-195.92, -4) fell on the sag before that burst, which in the exposition sits at +0.2..+0.3 s and had already lost 4.5 dB with the old +6.5 ramp. The celli stem read -41.8 dB at +0.15 s against -33 dB bodies, so the notch was removed. auto_fills was not rerun (the hand shapes cover both joins) | Celli 595.5 burst over the bodies +7.6 -> -0.3 dB. 596 body minus 595 +1.0 -> +1.2. Expo 195.5 +0.6 -> -2.8 (a 4-5 dB transition sag; master smooth, -33..-30 dB). Master hole at 598 4.3 -> 2.6 dB, at 198 4.5 -> 3.5 dB. Horn 1 - celli 596/598 -1.2/-0.4 -> -1.4/-1.3, 196/198 +0.7/-2.4 -> +0.5/-1.9 | burst/body yes; recap hole 0.1 dB over 2.5; expo hole no (3.5) |
| B #1 letter G | roles Horn 3 [464,484,-3.5,4], Horn 4 [464,484,-2.0,4] (B's -4.0 minus the -2 from B #3, as B said), Tuba [464,484,-3,4] | K re master per 4 qn from 464: horns -6.8/-5.9/-5.4/-5.6/-7.6 -> -8.9/-7.2/-6.8/-7.0/-8.8. Melody over horns +1.6/+1.1/-0.3/+0.1/+3.5 -> +4.1/+3.2/+2.0/+2.3/+5.0. Tuba -9.2..-11.5 -> -10.1..-13.9. Horn 4 at 464-468 -10.0 vs a2 -14.9 -> -13.2 vs -14.1. Master K 464.5-465 -14.3 against -13.7 at 462 | margin yes; the downbeat is now 0.6 dB under bar 116 (B simulated +0.3 over) |
| B #2 violas 436 | note trim 5 -> 0, then 3 by fix 3. c25 had played a louder sample on that note: c25 minus c24 +4.4 dB with identical data, and c26 matches c24 (`repdiff.py`). With 0 the c26 Ab5 sat level with its phrase and 5 dB under the flute | K body: -32.6 (c25) -> -39.3. Neighbours -40.4..-42.7, mp flute -36.5: now +2.2 over the phrase median and 2.8 under the flute | yes (a crest, no jump) |
| B #3 Horn 4 | `dyn_trim_db` ff 4.0 -> 2.0; role [524,536,-2.5,1] | Horn 4 - Horn 3 (K): 160 +3.8 -> +1.8, 328/330 +3.6/+3.9 -> +1.6/+1.9, 492 +3.3 -> +2.1, 520 +3.0 -> +1.4, 528/532 +1.8/+4.9 -> -0.7/+2.4. The f chords 120/122/556/560 did not move (-3.9/-4.0/-2.4/-1.9). 272/276 stay +3.6/+3.3 (mf, untouched) | yes |
| B #4 bar 97 | role Bass clarinet [384,388,-3,0.5] | K re master: bass clarinet -7.5 -> -10.1 (Bassoon 2 -10.1, bass trombone -10.3); celli -6.2 | yes |
| B #5 tuba E2/F2 | Tuba eq bell2 84 Hz -5 dB 0.3 oct (`--mix-only`) | Master 30-100 minus 300-1k at 116/120/560: -18.0/-15.5/-14.1 -> -20.5/-18.1/-16.0. Tuba share of the master's 30-100: -2.2/-3.6/-5.7 -> -4.4/-5.4/-8.4. Tuba level within 0.3 dB | yes |
| C #1 coda | `_coda26` -2 dB on `_all` and Tam-tam from 695.875. **Moved onto the 0.125 qn envelope grid:** C's breakpoint at 695.95 sharpened the grid-smeared soft-trim step at the chorale entries; the first simulation had the Trombone 1 entry at -10.6 dB for 0.05 qn | Delivered per bar 171-182: -29.6 -28.5 -28.0 -28.4 \| -29.6 -28.9 -29.2 -29.5 \| -31.4 -31.5 -32.2 -37.7 -> -29.1 -28.6 -28.0 -28.3 \| -31.1 -30.5 -30.9 -31.4 \| -33.3 -33.4 -34.1 -39.6. Solo minus chorale 0.7 -> 2.5 dB. The ppp end is now under the Lento's pp bars 4-5 (-34.9/-36.1) | yes (2.5 at the limit) |
| C #2 retransition | Clarinet 1 `[(504.75,0),(511.5,4),(512.9,4),(513.2,0)]` | Clarinet 1 510.5-512 minus 505.5-507 +0.7 -> +2.6 (simulated +3.6; renders differ). Master 510-512 minus 504-506 +1.2 -> +3.2. Master per qn 504-513: -34.9 -33.7 -32.8 -33.0 -31.5 -33.5 -31.3 -30.8 -30.7 -28.6. Delivered bar 128 -31.1 -> -29.6 | master yes, stem 0.4 short |
| C #3 Lento bar 3 | celli, basses, bass clarinet `[(8.5,0),(9.75,3),(10.25,3),(11,0)]` | Bar-3 master crest (half qn) -33.6 -> -30.9, against bar 2's -30.5. Rise from 8.0 +2.6 -> +5.3. The decrescendo 10-12 is unchanged | yes |
| C #4 coda solo | celli `[(682.15,0),(682.55,3.5),(683.15,3.5),(683.3,0)]` | Celli per 0.2 s from 680, at 1.8-2.8 s: -32.3 -35.0 -36.1 -36.0 -31.9 -> -31.6 -32.0 -32.6 -32.5 -30.7. The 2.6-2.8 s window is the loudest | yes |

## Rejected / deferred
- **A #2 (Horns 3-4 a2 on the 2FH track at 316.5-322.5; Trumpets a2), deferred a third time.** The Horns a2 track takes its notes and also its dynamics, hairpins, slurs and per-note tables from the Hn1 staff (`TRACKS` staves, `hairpins_and_marks(t[1])`, `_in_a2` copies of Horn 1's tables). A per-window staff list would have to reach each of those, not only `tw_spans`. The benefit is inferred. On the master, Horn 3 317/321 measure -1.3/-1.8 dB at 2-5 kHz front-body, so they are not harsh. It needs its own cycle with a full rebuild of Horn 3, Horn 4 and Horns a2.
- **A #3:** no fix was asked. If the hemiola must be heard on the master, B's lever (Violins I -2 dB at 538.5-546) remains.
- **C #1 span.** The p10-to-max span is now 19.8 dB, over the brief's 16-19. Accepted for the printed morendo, as C recommended: LRA 15.0 is in the middle of 14-16, the limiter is 2.3 dB, and the climax order holds.

## Before / after (c25 -> c26, after the stem fixes)

| | c25 | c26 |
|---|---|---|
| Master integrated | -16.4 LUFS | -16.5 LUFS |
| Master LRA | 22.5 LU | 22.1 LU |
| Master sample peak | 1.538 (qn 484.53) | 1.538 (same) |
| Master true peak | +3.7 dBFS | +3.7 dBFS |
| Delivered integrated | -19.8 LUFS | -19.8 LUFS |
| Delivered LRA | 14.4 LU | 15.0 LU |
| p10-to-max span | 19.1 dB | 19.8 dB |
| Delivery limiter | 2.2 dB | 2.3 dB |
| Delivered true peak | -1.7 dBTP | -1.6 dBTP |
| Motion, mp3 (dS4 p90 / 1 s-20 s) | 8.53 / 4.50 | 8.57 / 4.50 |

- Climax order (delivered S max): 160 -10.10 > 122 -11.03 > 167-170 -13.04 > bar 26 -14.53. In c25: -10.00 / -11.08 / -13.17 / -14.52. All within 0.15 dB of c25 (C's criterion 0.2). The margin of 160 over 122 is 0.93 dB (c25 1.08).
- Simulated before the render on the c25 stems: LRA 15.0, span 19.9, limiter 2.2. The render gave 15.0 / 19.8 / 2.3.
- Attack probe: 0 flagged (12 checks).
- REAPER memory: 27 GB with 0 compressed at the render start, 45 GB with 0 compressed after the render.

## Notes for c27
- **Renders are not repeatable on some string notes.** Violas, identical data, frames differing by more than 3 dB:
  - c25 against c24 and c26: 50-52.7 (+4..+5 in c25 against c26), 119, 367-376, 436 (+4.4).
  - c24 against c26: none at 50-52 or 436. So c25 was the outlier render.
  
  Before acting on a single string note's level, compare it with the render before.
- Master hole at the 198 join is 3.5 dB. The exposition celli 196 transition sag is 4-5 dB on the stem.
- The bar-117 arrival is now 0.6 dB under bar 116 in K (B #1).
- A #2 is open, with the code reach described above.
- Open from c25 and not addressed: width 0.05 on the other solo woodwinds, Oboe 1 498/538 crossovers, the 484.53 master peak, and a full auto_fills pass.
