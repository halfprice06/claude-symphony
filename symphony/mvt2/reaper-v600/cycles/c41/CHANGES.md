# Cycle 41: changes (actor; coordinator's release-cap decision, ONE_TIME stereo width, critics A/B/C on the c40 render)

Snapshot before the changes: `before/`. Data the render was made from: `rendered_build/`. Final data (after two stem fixes) in `build/`. Scripts: `actor_scripts/` (m41.py ends/final chord/image, check41.py accepted-finding checks, pk41.py per-onset levels, relevel41.py re-bow list re-levelling; c40's rbdips.py / envdiff.py reused). Measures of c39/c40/c41 by the same scripts: `actor_scripts/m41_c39.txt`, `m41_c40.txt`, `m41_c41_final.txt`, `check41_final.txt`.

Every track but Timpani, Harp and Harp harmonics changed its Opus state; all 32 were fully rebuilt in one build (32/32 states set).

## Main fix: release caps (coordinator)

- `tools/build_reaper.py`: `sus_release_cap_ms` may be a list of specs (Movement I c46's code); the cap printout is per (track, ms).
- `build/mix.json`: Violins I, Violins II, Violas, Violoncellos, Double basses `[300 ms at mf/f/ff, 400 ms at pp/p]` (same six rows); Violin I solo, Violoncellos div, Violins II div, Violas div 300 ms at all layers; Horns 1-4 and Horns 1-2 a2 237 ms at mf/f, 350 ms at pp.
- Measured (m41.py: phrase ends followed by >= 0.6 s silence; t10/t20 = time from the played end to -10/-20 dB under the 0.15 s before it; c39 uncapped / c40 / c41):
  - string sections, soft ends (n 38): t10 median 0.21 / 0.11 / **0.21 s**; ends with t10 >= 0.20 s 56 / 18 / **55 %**; t20 median 0.44 / 0.26 / **0.34 s**; drop at +0.15 s 7.2 / 13.5 / 7.3 dB.
  - divisi/solo tracks: t10 0.20 / 0.12 / 0.18; t20 0.46 / 0.29 / 0.32.
  - falls over 10 dB in the first 0.05 s: only Violoncellos 87 (10.6; c39 10.7, c40 12.1). Violins I 7.35 and the final C5 no longer.
  - final chord, master: t10 0.35 / 0.11 / **0.22 s**, t20 0.72 / 0.24 / **0.34 s**; Violins I / celli / basses stems t10 0.22-0.24 s.
  - horns: unchanged (t10 0.15, t20 0.30). The horns play their soft dynamics on the mf CC1 layers (c31), so the pp groups the 350 ms cap acts on are not used.
- Target check: the soft-end target (t10 >= 0.20 s, nothing over 10 dB in 0.05 s) is met; the 20 dB target (0.43-0.58 s) is **not**: 0.34 s at phrase ends and the final chord. Uncapped c39 measured 0.43-0.44 by the same script, so 400 ms at pp/p still shortens the -10..-20 dB part. Open for c42: no cap (the shipped 524-931 ms) on the pp/p groups, or 600 ms, keeping 300 ms at mf-ff.
- Re-bows refit after the render: `tools/fit_rebows.py 41 cycles/c41/rendered_build/parts.json --hold-max-after 301:0 --window "Double basses:2.6" --skip "Double basses:273.229" --tracks <8 string tracks> --write` (the c34 window back, critic B #1); Bass clarinet not refit (c40 do-not-touch). Then `relevel41.py`: basses pedal 221.8-235.659 to the c39 piece means +1.5 dB (first run -1.5 as B wrote left Horn 1 11.5-20.5 dB A over the pedal, back to c38's 14-18 dB gap that c39 B #4 had fixed; +1.5 = c39's output level without its +3 shape, B's stated target), coda lists 276.05-283.605 to the c39 means, Violoncellos div to the rendered (c40) means. Violins I 264.417 +2.5 dB from 0.6 s (B #2).
  - re-bow dips on the final stems: median 3.1 dB (c40 after refit 5.0), p90 5.8, none over 8 (first render with the old fills: 2 over 8 and 50 attack peaks over 2.5 dB); peaks over 3.5 dB at 7 points (max Violas div 79 5.0). Final chord re-bows: median 3.6, max 7.8 dB.
  - basses pedal 226-238: range per 0.25 qn 11.1 -> 3.5 dB; Horn 1 over the basses (A, per 0.5 qn) c40 4.6-15.8 -> 8.5-17.5 dB.
- Basses' pp sus-gap repeats (A's watch): new generic `STR_REP_NEW_BOW["sus_fall"]` (CC11 fall over the note before's last s seconds), basses 10 CC / 0.06 s at p or softer. Dips 156 / 168: c40 9.8 / 8.5, c41 5.7 / 7.1 dB.

## ONE_TIME (done; appended to `loop/ONE_TIME.done.md`)

1. Hall kept. Records: final chord as above. The "breath at 268" is a flute breath under a sounding tutti (critic C: master falls 3-4 dB; flute stems 15.5 / 12.0 dB at +0.15 s, uncapped winds, unchanged); no tutti stop exists in this movement to measure.
2. Stereo width. Before (c40, m41.py): master corr < 250 Hz 0.81, 250 Hz-4 kHz 0.64, side/mid -6.8 dB (references 0.54-0.62, -4.7..-5.4): below the references, so done:
   - mix only: side low shelves to 0 dB on Contrabassoon, Bass trombone, Tuba, Violoncellos (200 Hz -2) and Bass clarinet (250 Hz -6). Kept: basses 100 Hz -15 (seat), timpani 300 Hz -9, harps 300 Hz -8.
   - `width_by_mic` (kit `apply_mix` code copied into `tools/build_reaper.py`): groups wind, horn, lowbrass Main 0.35; Violoncellos, Double basses Main 0.45; Clarinet 1, Horn 1 Main 0.2.
   - After (with the longer string releases): corr < 250 Hz 0.81 -> **0.66**, 120-250 Hz 0.79 -> 0.62, 250 Hz-4 kHz 0.64 -> **0.61**, all 0.66 -> 0.60, side/mid -6.8 -> **-6.1 dB**; R-L < 250 Hz +3.4 dB (unchanged), 35-63 Hz +0.8 dB (unchanged, the basses' side shelf holds the deep bass centred). Movement I: 0.78 -> 0.57, -7.3 -> -6.3. Close to C's acceptance (0.65 / 0.60 / -6.0); hall Width 1.5 remains the fallback.
3. `rt_gain_db` not adopted (waiting for Movement I c46).

## Critic findings

Accepted:
- B #1: c39's basses +3 at 226-238 removed; pedal refit with the window (above).
- B #2: Violins II CC7 at 264-265.75 76 -> 101 (-2 dB instead of -4.5); Violins I 264.417 fill +2.5 from 0.6 s. Violins I over Violins II (A) per 0.25 qn 264-265.75: c40 4.8 4.2 5.0 3.8 2.4 1.8 0.9 -0.3 -> 5.3 4.1 4.4 4.6 4.2 3.5 2.7 0.8; master 264-265.75 +0.4..+0.9 dB.
- B #3: Horn 1 soft shelf ramps out 180-182 (was 186-194); +5 dB shape inside the 182 note. Horn 1 minus Violins I (A) at 182.75 / 183.75 / 184.75: -2.1 / -20.2 / -7.7 -> +5.1 / -11.4 / -5.4; from 186 on unchanged (-8..-22), so B's -4..-8 target is met only at 182-185. Horn 1 1-5 kHz share at 182-194 -13.2 -> -11.1 dB; pp bars 54-55 unchanged (-22.4).
- B #5 (series 1's climax shelf touched only outside it): basses loud_eq second entry, 80 Hz bell +4 dB (0.5 oct) wet 255-261.6 only. Taken because the measurement holds: master 56-125 Hz re 500-2000 Hz at 256-262 -20.0 -> -16.5 dB (B's target -15..-12, Dvorak loud -8.9), basses 78/82 Hz vs their octave -9.1 -> -5.7 dB; D flat 2 at 262-265 unchanged (-15.3 -> -15.6), so series 1 c16's reason for the climax shelf stands. Limiter 2.3 dB.
- A #2: Trombone 1 214.5 shape held at +2.5 to 0.60 s, 215 shape starts at +2.5; 215 velocity 112 -> 124. Stem per 1/16 qn 214.75-215.25: c40 7.0 5.5 3.2 -0.7 4.2 5.3 5.0 5.9 -> 7.0 5.5 4.9 5.4 5.9 5.2 4.9 6.0; master minimum at the transition 1.5 -> 5.5 (no dip left).
- A #3: portato gap 0.05 -> 0.03 s and fall 6/8 -> 3/4 CC; Violins II 44 note trim +4; after the render level shapes (`LEVEL_SHAPES_S`, c41 block): Violoncellos 128 +5, Violas 248.5 +6, Violas 69 +4, Violins II 44 +3 over the holes, basses 144 -5 over its attack. Stem pre / minimum / body (dB) c40 -> c41 final: Vln II 44 -42/-58/-46 -> -42/-49/-42; Vc 128 -40/-54/-44 -> -40/-48/-44; Vla 69 -44/-58/-45 -> -44/-49/-45; Vla 248.5 -42/-55/-46 -> -42/-49/-46; Cb 144 peak over body +7.0 -> +2.3. Dips now 7-8 dB, none 10 dB or more.
  - Tried and reverted: taking basses 144 out of `DOWNBOW_STROKE_AT` made it an unled Leg Slur MAX slur head (it is not a sus gap because it is on a legato row), so it stays a stroke with the level shape.
- Delivery: after the first stem fix the span read 19.1 dB; `_all` -0.4 dB over 204-212 (slow ramps) brought it to 18.9.

Rejected or deferred:
- C #3 widen Violins II div / Violas div: deferred as the coordinator asked (re-measure after the width change); the div tracks are Close-only, so `width_by_mic` did not touch them. Their phrase-end t20 (0.32 s) now matches the sections' (0.34).
- C #1 as written (300 ms everywhere, 150 on the div tracks): superseded by the coordinator's values.
- A #4 Violins II 112 sul tasto refit: not done separately (the general refit covered it; not re-measured).
- A #5, MANUAL-GAPS: no gap tried this cycle (release and width work).
- Violas 71 bump (+5.6, A #3): not in this cycle's list.

## Render, stem fix, delivery

- Master (final stems): -20.4 LUFS, LRA 24.3 LU, TP -1.3 dBFS, sample peak 0.856 (first render -20.0 / 24.2 / -0.9).
- Delivered `cycles/c41/mvt2-mockup-c41.mp3`: -19.8 LUFS, LRA 15.5 LU, TP -1.6 dBTP, p10-to-max span 18.9 dB, limiter about 2.3 dB (c40: -19.8 / 15.2 / -1.6 / 18.8 / 2.4).
- Attack probe: 0 late or holes (first render and both stem fixes). No clipping; all 32 stems present. Climax order: bars 61/62/79/80 34.5 / 34.1 / 28.1 / 27.8 dB (A).
- Bar 66 niente (master 223 vs 225.5, same measure for both): c40 5.7, c41 6.4 dB.
- Stem fixes: (1) `stem_fix.py 41 cycles/c41/rendered_build build --apply` on the 8 string tracks (refit fills, A #3 shapes, the Cb pedal re-levelling); (2) from a scratch build of that state to `build/` on 26 tracks (`_all` -0.4). Originals in `render_first/`. Then `render_cycle.py 41 --measure-only` and `build_reaper.py --mix-only` (all tracks) while holding the lock.
- REAPER: 44 GB, 0 compressed after the open (memory flat for 2 min before the build), 44 GB / 0 compressed before the render (no `--force-memory`); 45 GB (27 GB compressed) after the render.
- Lock: no other waiter; held 16:47:52-17:32:39 (45 min). Build of 32 tracks about 2 min, render about 8 min.

## Open for c42

- String t20 0.34 s against 0.43-0.58 s (phrase ends and the final chord): lift the pp/p caps further (shipped values or 600 ms) and refit the re-bows again.
- Horn 1 against the violins at 186-196 still 8-22 dB under.
- C #3 divisi width, hall Width 1.5 if side/mid should reach -6.0.
