# Cycle 27: changes (actor)

There was no ONE_TIME.md. Of the critics' 12 findings, 10 were accepted (A #1, A #2, B #1, B #3, B #4, C #1-C #4). Two were not taken as written: B #2 was replaced by A #2, and A #3 was deferred. C #5 was a note that asked for no change.

The tempo map changed (C #2, C #4) and string notes moved (C #1, C #3, A #1's 348 stroke). REAPER got all 33 tracks through `build_reaper.py build/parts.json jobs --midi-only --tempo`: 499 tempo markers, no mismatches, no Opus state reloaded. The Double basses' new static ReaEQ came in through the same path. After the render, one level-only stem fix (Violoncellos 348, Clarinet 1 414/422) was applied with `stem_fix.py` and written with `--mix-only "Clarinet 1" "Violoncellos"` from a fresh start, then saved.

Files:
- `before/` holds the c26 tools and data.
- `rendered_build/` holds what the render was made from.
- `render_first/` holds the master and the Clarinet 1 / Violoncellos stems as rendered.
- `actor_scripts/c27check.py RENDER_DIR PARTS [--no-cross] [--show]` measures every critic pass criterion, including a simplified version of C's crossover/arrival measure.
- `check_c26.txt`, `check_c27.txt` and `check_c27_final.txt` hold its output on c26, on c27 as rendered, and on c27 after the stem fix. The levels are plain stereo power except where K is marked.

REAPER steps:
1. Fresh start, open (33 tracks), `--midi-only --tempo` (all tracks), save, quit (timed out; killed after the save).
2. Fresh start, open, `render_cycle.py 27`.
3. Stem fix, then `render_cycle.py 27 --measure-only`.
4. Fresh start, open, `--mix-only "Clarinet 1" "Violoncellos"`, save, quit (killed after the save).

## Accepted

| Finding | Change | Measured, c26 -> c27 (final) | Pass? |
|---|---|---|---|
| A #1 fugato staccatos | The trims are A's values, applied as exact `LEVEL_SHAPES` steps on the attack rather than note trims, because a note trim ramps in over 0.1 s from the score onset and misses the 50 ms stroke peak. Celli: -2 at 338.5, -4 over 339-339.5, -4 over 343.5-347.6 (one step through the rests). Violas: -2.5 at 350.5-351.5, 356 and 358. Violins II: -5 at 367.5 | Celli 50 ms peaks: 343.5-346 -26.4..-27.4 -> -30.4..-31.4. The 342 accent is -30.2, so it is now at or over them (c26: 4 dB under). Violins II 367.5 -26.8 -> -31.8, against the 366 accent at -27.3. Violas 356/358 -33.6/-34.7 -> -36.0/-37.2. Master bars 85-92 -29.9 -32.2 -32.5 -35.8 -33.8 -29.8 -29.6 -27.8 -> -31.4 -33.6 -35.5 -36.2 -33.9 -30.2 -29.4 -27.8 | partly. Bars 85-87 fell 1.4-3.0 dB, more than A's 1.5 dB limit, because the staccatos were most of those bars' level |
| A #1 celli 348 | `DOWNBOW_STROKE_AT` celli += 348 (Sus MAX stroke; 349.5 becomes a short stroke too, through `STR_SHORT_AFTER_SUS`). The +1.5 shape and the +3 role were extended to 348.5. As rendered, the stroke sat at -48.1 (c26 Leg Slur first note -46.0). Stem fix: A's fallback step, sized to the target: +8 dB from the moved onset 347.78 to 349.35 | Celli 348 body -46.0 -> -40.1 (target -39.5). Master 348.0-348.5 -43.9 -> -39.0 (target -40). Celli 349.5-351 -46.5 -> -45.4, violas -39.4 (gap 6.0) | yes (body 0.6 dB short) |
| A #2 Clarinet 1 state check | Classified on the c27 stem: 414 and 422 bright (front-body +10.3 / +8.1, master front-pre +7.6 / +8.6), 626 dull (-11.4). Stem fix: `LEVEL_SHAPES_S` Clarinet 1 at 414/422, -7.5 dB from 0 to +0.12 s, back by +0.30 s. A proposed -5; simulated on c27, -5 left the master at +4.6/+4.7. No accent fit, note trim or fill was changed | Master 2-5 kHz front-pre 414 +7.6 -> +3.6, 422 +8.6 -> +3.2 (target 3.5). Stem front-body +4.5 / +2.3 | 422 yes, 414 0.1 dB over |
| B #1 basses B1/D2 | `mix.json` Double basses `mute_eq` from qn -2.5: bell 61.7 Hz -6 and bell2 73.4 Hz -5, both 0.25 oct | Master 30-100 minus 300-2k Hz: bar 11 -6.0 -> -12.2, bars 97-98 -8.8 -> -15.3, bar 114 -10.6 -> -16.8, bar 26 -16.9 -> -22.4 (B's simulation: -12.2 / -15.2 / -16.8 / -22.0). Bars 1-4 -2.6 -> -3.8. Bar 3 -6.2 -> -11.3, with master K unchanged (-33.8). Coda 167-170 -17.3 -> -22.6: the bells partly cancel that passage's 66 Hz +4 loud EQ. Master K changed by -0.4 dB or less | yes |
| B #3 bar 40 timpani | `LEVEL_SHAPES` Timpani (157.5, 0), (158.25, -2.5), (159.9, -2.5), (160, 0) | Timpani K re master at 158.0-159.0: -10.3/-9.7/-10.0 -> -12.4/-12.1/-12.2, against Violins I -10.8/-11.3/-12.7. 159.5 -7.6 -> -8.9, then the bar-41 sf (160 -12.1 unchanged) | yes |
| B #4 bars 27-31 brass | `roles.json` Trombone 1, Trombone 2 and Tuba [104, 124, -2, 0.5] | f brass group K re master -4.9..-7.1 -> -5.6..-8.0. Melody margin over the brass 0.6-3.6 -> 1.8-4.9 dB. Delivered S max over 104-124 -16.22 -> -16.31 | yes (about 1 dB, against B's 1.3) |
| C #1 Violins I / celli leads | `LEG_ART_EXTRA_S` Violins I Leg BC +0.05. Celli Leg BC -0.06 -> -0.02. `leg_leads.json`: Violins I 30 listed Leg Slur onsets +0.05 and 228/373/477/523 -0.05; celli 192/568/600/628 -0.04. `LEG_CAP_FRAC` Violins I [(56, 728, 0.95, "listed"), (56, 728, 0.75)]. `LEG_MIN_GAP_S` Violins I 0.06, not C's 0.10: at 0.10, 21 Violins I Leg Slur targets after an unled eighth lost lead (0.17 -> 0.135 s), 9 of them listed. Early fills on the moved celli targets moved with them (`early_fills.json` pre_s + 0.04; 40 rows) | Crossover medians (own measure, c26 -> c27): Violins I Leg BC +0.061 -> +0.021 (arrival +0.081 -> +0.056); listed Leg Slur +0.086 -> +0.056; all Violins I Leg Slur +0.056 -> +0.041; celli Leg BC +0.076 -> +0.031 (arrival +0.071 -> +0.041). The other sections are unchanged within 0.03 | Leg BC yes; listed partly (+0.056 against +0.04): 9 of the 30 have an unled eighth before them and gained under 0.01 s |
| C #3 early targets | `leg_leads.json` negative extras: Violins II 6, violas 9, celli 8, as C gave them. Fills moved with them (celli 10 / 646) | Crossovers c26 -> c27: Violins II -0.094..-0.119 -> -0.049..+0.021; violas 119.5/600/647 -0.189/-0.089/-0.079 -> +0.061/-0.039/-0.024; celli 225.5/555/562/593.5/616/643/646 -0.08..-0.14 -> -0.069..+0.041. Arrival outliers left: violas 496 +0.296 and 682 -0.129, celli 555 +0.221 and 593.5 -0.209 (C called 369/593.5-type arrivals window artefacts) | mostly |
| C #2 development arcs | `PHRASE_ARCS` (384, 396) and (440, 452) -> "open", (432, 440) -> "sub". Two follow-ups after reading the new map: `APEX_SKIP` += 440 (the apex hold put a 4% slower beat at 448, bar 113), and new generic `PHRASE_RETURN_AFTER_OPEN` (default True; False here). Without it, the open (384, 396) still gave the next arc a 0.97 return beat (122.2 bpm on bar 100's downbeat) | Bar 99 126/126/121/115.9 -> 126 x4. Bar 100 downbeat 122.2 -> 126. Bars 111-116 have no slowing beat (bar 113 121/126/123.5/119.7 -> 126 x4). Bar 110 keeps C's "sub": 126/126/123.5/119.7 (3.1% at the last beat). 384-464 38.466 -> 38.281 s (-0.19). Violas 451/451.5 now play the short_sus Sus MAX eighth like every other 126-bpm slurred string eighth (art_counts: violas Leg Slur -2 / Sus +2) | yes, except bar 110 (C's own "sub") |
| C #4 coda arc | (680, 688, "sub") + (688, 696, "main") -> (680, 696, "main") | Bars 171-174: 72 \| 73.1 x4 \| 73.1 x4 \| 72 x4 \| 69.1 72 68.4 63.4 (the apex hold on the top note at 692, then the phrase end). 3 direction changes (C's limit 2; c26 5). 680-696 13.61 -> 13.44 s (C's limit 0.2 s) | partly |

## Rejected / deferred
- **B #2 (Clarinet 1 accent_fits [5, 1] -> [2, 1]):** replaced by A #2. A showed that the same data renders in one of two attack states (c14-c26 history; c18 -> c19 -> c20 flipped with identical hashes). A permanent swell cut would leave the accent without weight in the dull state. The bright state is now fixed on the stems, per render, after it is measured.
- **A #3 (Trumpets / Trombones a2):** deferred again, as A asked (memory and a separate render).
- **C #5:** no change asked.
- **A's note-trim mechanism** for the fugato was replaced by exact steps with the same values (see above). C's `LEG_MIN_GAP_S` 0.10 became 0.06 (see above).

## Before / after (c26 -> c27, after the stem fix)

| | c26 | c27 |
|---|---|---|
| Master integrated | -16.5 LUFS | -16.5 LUFS |
| Master LRA | 22.1 LU | 22.3 LU |
| Master sample peak / true peak | 1.538 / +3.7 dBFS | 1.541 / +3.8 dBFS |
| Delivered integrated | -19.8 LUFS | -19.8 LUFS |
| Delivered LRA | 15.0 LU | 15.0 LU |
| p10-to-max span | 19.8 dB | 19.9 dB |
| Delivery limiter | 2.3 dB | 2.3 dB |
| Delivered true peak | -1.6 dBTP | -1.7 dBTP |
| Motion, mp3 (dS4 p90 / 1 s-20 s) | 8.57 / 4.50 | 8.69 / 4.54 |
| Length | 433.48 s of music | 433.15 s of music (mp3 434.55 s) |

- **Climax order** (delivered S max): 160 -10.02 > 122 -11.05 > 167-170 -13.04 > bar 26 -14.53. c26: -10.10 / -11.03 / -13.04 / -14.56.
- **Attack probe:** 0 flagged (12 checks).
- **REAPER memory:** 22 GB with 0 compressed at the render start, 46 GB with 1.4 GB compressed after the render.

## Notes for c28
- **Clarinet 1 414/422 state.** These were bright again (c26 and c27 both bright). The c27 stem fix is a per-render shape in `LEVEL_SHAPES_S`. If c28 renders the dull state, remove these two shapes (stem fix +7.5 back), because they would cut a dull attack. Check with `c27check.py`.
- **Bars 85-87 fell 1.4-3.0 dB.** The staccatos were most of their level. If the fugato now reads too soft against bars 89-92, raise the subject's legato notes rather than undo the staccato steps.
- **Violins I listed Leg Slur targets** are still +0.056. The ones after an unled eighth can only move by leading the eighth too.
- **Coda 167-170 low end.** The new 61.7/73.4 bells take back part of the 66 Hz +4 coda loud EQ (30-100 re 300-2k -17.3 -> -22.6, now level with the other ff tuttis). Check it by listening, if anyone can.
