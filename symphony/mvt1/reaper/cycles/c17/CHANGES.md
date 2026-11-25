# Cycle 17: changes (actor)

One render from a freshly restarted REAPER: 33 tracks, 30 updated with `--midi-only`, and the three percussion tracks fully rebuilt (their Opus pan state changed). Before the build, the Opus states were checked offline against `jobs/*.b64`. Only Tam-tam, Suspended cymbal and Crash cymbals differed.

After the render, one level-only stem fix: `tools/stem_fix.py 17 cycles/c17/rendered_build build --apply`. It covered the pickup lifts measured on the render, the Horns a2 level restore and the accent refit. Then:
- `render_cycle.py 17 --measure-only`;
- `build_reaper.py build/parts.json jobs --mix-only` (all tracks);
- save, then quit. The quit job timed out after the save, and REAPER had exited.

Where things are:
- First-render stems: `cycles/c17/render_first/`.
- The data and code the render was made from: `cycles/c17/rendered_build/`.
- Snapshot of the c16 tools and data: `cycles/c17/before/`.
- Scratch: `/private/tmp/claude-501/mockup-loop/mvt1-c17-actor/`:
  - `lib17.py`;
  - `pick.py`: pickup minus target;
  - `synco.py`: syncope profile;
  - `acc.py`: long accents against the line before, A's measure;
  - `hf.py`: brass and top-octave brightness, master band correlation;
  - `perc.py`;
  - `loud.py`;
  - `statecheck.py`: offline Opus state check;
  - the pre-render simulation in `sim/`, and the stem-fix simulations in `fix1/` and `fix2/`.

Simulation before the render (c16 stems with the c17 envelopes, `stem_fix.py` into scratch, then `deliver_master.py`): delivered LRA 14.4 LU, span 19.1 dB, limiter 2.1 dB. The render measured 14.4 / 19.1 / 2.3.

## Accepted

### A #1: pickups after a rest
**Revert of the c16 test.**
- `PICKUP_SUS = None` in `build/score_config.py`. Its string -3.5 dB goes with it.
- The pickups play their c15 rows again. A diff of parts.json against the c15 build shows only the c16 `DETACH_LEAD_KEEP_QN` note (basses 285) different.

**Lift.** New generic `PICKUP_LIFT` in `tools/score_to_parts.py` (`{track: {pickup score qn: dB}}`).
- It is an exact level shape:
  - starts at the pickup's moved onset, with a 0.01 qn ramp in;
  - holds to the target's moved onset;
  - is gone 0.02 qn after it.
- parts.json key `pickup_lift`.
- Render values were A's table. After the render, they were moved toward -4 dB under the target's 200 ms peak, capped at 12 dB:

  | Pickup | Lift, render -> after stem fix (dB) |
  |---|---|
  | Flute 1 104.5 | 5.5 -> 3.2 |
  | Flute 1 552.5 | 5.6 -> 8.0 |
  | Oboe 1 312.5 | 10 -> 12 |
  | Clarinet 1 272.5 | 3.8 -> 1.8 |
  | Clarinet 1 416.5 | 5.1 -> 7.3 |
  | Clarinet 1 504.5 | 6.2 -> 9.5 |
  | Bass clarinet 432.5 | 5.2 -> 8.2 |
  | Trumpet 1 664.5 | 8.9 -> 6.9 |
  | Trumpet 1 672.5 | 9.6 -> 6.4 |
  | Trombone 1 520.5 | 6.2 -> 3.8 |
  | Violins I 136.5 | 10 -> 12 |
  | Horns a2 664.5 | 7.4 -> 5.2 (it stood +1.4 dB over its target's body) |

  The others kept A's values.
- The +3 dB note trims on Trumpet 1 664.5/672.5 and Horns a2 664.5 were removed (`note_trims.json`). The lift replaces them.
- Horns a2 272.5/672.5 keep their +3 trims: A's table has no lift for them.

**Result.** Pickup minus its target's 200 ms peak, as heard, median over the 21 pickups: c16 -14.2 dB -> render -4.2 -> after the fix -4.0.
- 18 of 21 are within the pass range of -6..-2 dB.
- Outside it: Violins I 136.5 -8.8 (at the 12 dB cap), Oboe 1 312.5 -8.0 (cap), and Violins I 72.5 -8.5. For 72.5, the refit raised its target 73 to 4.5 dB.
- None is louder than its target's body. The highest is Horns a2 664.5 at -0.5.
- No entry lead was added, as A advised.

### A #2: string accents measured at their peak
`tools/fit_accents.py` has three new options:
- `--peak-long-qn` (default 1.0): a note written 1 qn or longer (accent or neighbour) is measured as its loudest 200 ms inside [score onset - 0.05 s, min(+0.5 s, end - 0.02 s)]. The envelope's share is read over that 200 ms. Written length comes from `mockup-events.tsv`.
- `--max-total`: a cap on swell + step. Defaults: strings 4.5, winds and brass 6. Existing fits are brought under it first.
- `--skip Track:q`: leaves listed accents as they are.

How it was run:
- A pre-render refit on the c16 stems, for all three families with `--keep-long-qn 1.4 --pickup-over 2.5`.
- A post-render refit on c17, applied by the stem fix.
- Trombone 1 521/529 were set by hand (B #1) and skipped in both refits.
- Fitter's prediction after the c17 refit, in 2-4 dB: brass 31/37, winds 113/142, strings 78/135. Strings are low because many long accents now stand over their neighbours even with no swell, and long notes get no negative step.
- Violins I 62/65/82 measured only 1.9/2.4/0.7 dB over the line before after the capped refit (pass 3-5). They were set by hand over the cap: 5, 5+1 and 5+2. Result: 3.4/3.8/3.2 dB.

A's long-accent measure (peak minus the peaks of the notes in the 2 qn before; control = unaccented long notes), c16 -> c17:

| Family | Excess median | Over 6 dB | In 2-4 dB |
|---|---|---|---|
| Strings | +4.8 -> +3.7 (pass +2..+3.5) | 33 -> 18 (pass under 10) | 27 -> 33 |
| Winds | +4.4 -> +1.6 | | |
| Brass | +4.8 -> +1.8 | 9 -> 1 | |

- Specific notes: celli 342 11.6 -> 7.9; violas 354 10.8 -> 6.9; Violins I 110 10.7 -> 4.0; Violins I 137 15.4 -> 9.1.
- Celli 342 is still the loudest stem there, which is right: it is the fugato subject, 0.7 dB over the basses.
- Strings: a partial pass.

### A #3: syncopated accompaniment
New generic `SYNCO_SHAPE` in `score_to_parts.py` (parts.json `synco_shaped`). It applies to a string note that:
- starts on an off-beat eighth at 100 bpm or faster;
- follows a written rest of at least 0.25 qn;
- is 0.75-2 qn long;
- is not accented, and not slurred from the note before.

The note takes an exact shape:
- +6 dB from -0.12 s to +0.10 s, +3 at +0.25, 0 at +0.45, -3 from +0.60 to the note's end;
- back to 0 by the next moved onset.

It applies to Violins II (14 notes) and violas (8 notes), bars 15-22.

Median profile against the note's maximum, bins -0.12..0 / 0..0.1 / 0.1..0.2 / 0.2..0.3 / 0.3..0.45 / 0.45..0.6 / 0.6..0.8 s:

| | c16 | c17 |
|---|---|---|
| Violins II | -6.6 -7.7 -5.4 -4.0 -3.4 -0.6 0.0 | -0.6 -2.9 -0.7 -1.1 -2.7 -2.3 -3.9 |
| Violas | -6.7 -7.1 -5.0 -3.7 -2.7 -1.8 0.0 | -2.0 -3.1 -0.6 -2.6 -2.4 -4.3 -4.1 |

- Stem mean over bars 15-22: +0.8 / +0.2 dB. Master: -0.4 dB.
- A counted about 59 notes, including the recapitulation violas (525.5-535.5). Those are off-beat eighths of 0.5 qn, outside A's own 0.75-2 qn rule, so they are not shaped.
- The optional `Sus Marc LITE` test was deferred. It loads a row (a full rebuild of Violins II), and it should not share a render with a level shape on the same notes.

### B #1: recapitulation trombone
- `roles.json` Trombone 1 [520,536] +2.5 -> -0.5.
- `accent_fits.json` Trombone 1 "521" [5.0,1.01] -> [3.0,-1.5] and "529" [5.0,3.0] -> 3.0, kept out of the refits.
- Trombone 1 minus celli, median over 520-536: +1.4 -> -2.3 dB. Per half beat over 521-523.5: +6.4..+11.4 -> -1.6..+5.9.

### B #2: fugato entry 3
- Roles: Cor anglais +4 and Violins II +3 at 360.25-372; celli -2, violas -2 and basses -3 (from 358); basses -2 at 104.5-108.
- Subject top minus accompaniment top, median: -3.2 -> +0.6 dB (simulated +1.0).

### B #3: bars 121 and 124-125
- Trombone 1 / Bass trombone cuts held to 484 with a 4 qn end ramp.
- Bar 124: low brass -3.5 and celli -3 at 492.5-496.5; Violins I / Oboe 1 / Flute 1 +2.5. Bassoon 2 -3 at 496-500.
- Melody top minus accompaniment top: bar 121 -1.9 -> -0.1 dB; bar 124 -2.5 -> +1.2.

### B #4: wind mf -> f
- `dyn_trim_db` f raised on Oboes (3.5), Bassoon 1 (3.5), Bassoon 2 (4.0), Bass clarinet (0.5) and Cor anglais (2.5), with mf anchors at the old mf values (soft overrides for the oboes and cor anglais).
- Pitch-matched wind mf -> f: +0.7 -> +1.9 dB (pass +2..+4); f -> ff +6.7 -> +5.7.
- Partial pass. The rest is left for a re-measure.

### B #5: soft timpani rolls
- Roles -3 at 168-176, -3 at 300-304.5, -2 at 244-252.
- Roll minus the quietest held string section: bar 76 +0.5 -> -2.0..-3.2 dB; bars 43-44 about +2.7 -> -4.3..+1.1; bars 62-63 (printed swell) -1.1..+5.6.

### C #1: Horns a2 colour
- `mix.json`: a static high shelf at 1.25 kHz -3 dB, plus a `loud_eq` high shelf at 1.6 kHz -8 dB over the four CC1 >= 108 windows. Restored by roles +1.0 over the windows. The render had +1.7, which put the a2 track 0.6-0.8 dB over c16; the stem fix lowered it.
- a2 2-5 kHz re 500 Hz-2 kHz in the loud windows: -8.4..-10.3 -> -17.8..-19.8 dB. Horns 3-4 there are -16.2..-21.7.
- a2 level per window against c16: -0.36..+0.13 dB.

### C #2: Trumpet 1 climax top
- `loud_eq` high shelf at 5 kHz -14 dB over 633.8-640.05.
- Master 8-16 kHz re 500 Hz-2 kHz at 637-639.5: -24.5 -> -30.4 dB (target -31..-28).
- Trumpet 1's share of the master's top octave there: 74% -> 13%. Its A-flat5: -13.9 -> -27.3 dB re its own 500 Hz-2 kHz.
- Step into 640-642: 7.6 -> 3.5 dB (target 3 or less; close).

### C #3: percussion width
- `groups.perc.width` 0.4 -> 0.7.
- Seats: crash 0.12, sus. cymbal 0.22, tam-tam 0.12.
- Master L/R correlation, c16 -> c17:

  | Band | c16 | c17 | Target |
  |---|---|---|---|
  | above 4 kHz | 0.590 | 0.547 | 0.555 or less |
  | 8-16 kHz | 0.766 | 0.642 | 0.65 or less |
  | 1-2 kHz | 0.556 | 0.545 | within 0.02 of c16 |
  | 2-4 kHz | 0.514 | 0.501 | within 0.02 of c16 |

- Percussion stems: correlation 0.81 -> 0.65 (C simulated 0.49); levels -0.5 dB.
- R-L moved -1.0 / -1.6 / -1.3 dB (crash / sus. cymbal / tam-tam; target within 1). The seat cut was not needed. Open: seats back up by about 0.06 at the next full rebuild of those tracks.

## Rejected or deferred
- **A #1, pickup entry lead:** not added (A's evidence: the plateau, not the rise, is the deficit).
- **A #3, `Sus Marc LITE` test:** deferred (above).
- **The Horns 3-4 a2 routing at bars 80-81:** still deferred.
- **No other finding was rejected.**

## Before / after (c16 -> c17 after the stem fix)

| Measure | c16 | c17 |
|---|---|---|
| Master integrated (float stem sum) | -16.3 LUFS | -16.4 LUFS |
| Master LRA | 22.2 LU | 22.2 LU |
| Master sample peak | 1.541 | 1.538 |
| Master true peak (float) | +3.8 dBFS | +3.7 dBFS |
| Delivered integrated | -19.8 LUFS | -19.8 LUFS |
| Delivered LRA | 14.5 LU | 14.4 LU |
| p10-to-max span | 19.0 dB | 19.1 dB |
| Delivery limiter | 2.0 dB | 2.3 dB |
| Delivered true peak | -1.6 dBTP | -1.7 dBTP |
| Motion (mp3) | 8.82 / 4.56 dB | 8.65 / 4.52 dB |

- First render, before the stem fix: delivered LRA 14.4 LU, span 19.1 dB, limiter 2.3 dB.
- Climax order on delivered S max: 160 -9.99 > 122 -11.17 > 167-170 -12.94 (c16 -10.10 > -11.20 > -12.89).
- Master top peaks:
  - 1.538 at qn 484.53, the fff arrival of bar 122 (the limiter's peak; c16 1.348 there). The sample sums bass trombone 0.175, celli 0.162, timpani 0.148 and Trumpet 2 0.136; in c16 the celli were not among the top six contributors at that sample. The celli stem there is +1.3 dB RMS over c16 with the same sample peak, and no c17 data change touches the celli at 484-485, so this is round-robin variation lining up with the low-brass crest. A 0.16 qn notch like c14's 641.7 would take it down if needed;
  - 1.499 at 636.34;
  - 1.387 at 640.81;
  - 1.313 at 642.86.
- Attack probe: 0 flagged.
- REAPER memory (`metrics/memory.txt`): 26 GiB with 0 compressed when the render started; 45 GiB with 29 compressed after it.
- Delivered mp3: `cycles/c17/mvt1-mockup-c17.mp3`.
