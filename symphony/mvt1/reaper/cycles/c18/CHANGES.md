# Cycle 18: changes (actor)

Every change this cycle was level-only (volume envelope) or a ReaEQ change, so parts.json notes, keyswitches and CC lanes are identical to c17 (checked track by track). REAPER: fresh start, project opened, `build_reaper.py build/parts.json jobs --mix-only` (all tracks), save, quit, fresh start, open, render. One stem fix after the render (Bassoon 1, below), then `render_cycle.py 18 --measure-only` and `--mix-only "Bassoon 1"` into REAPER; saved and quit. The quit job timed out at 60 s both times and REAPER had exited.

Before the render all changes were simulated on the c17 stems: `stem_fix.py 17 cycles/c18/before build --out <scratch>/sim` plus an FFT-magnitude version of the basses' EQ change (`eqsim.py`). The simulation gave delivered LRA 14.4 / span 19.1 / limiter 2.2 dB. The render measured 14.4 / 19.0 / 1.9 and matched the simulation within 0.2 dB on every check below, except Bassoon 1.

Where things are: `cycles/c18/before/` (c17 tools and data), `cycles/c18/rendered_build/` (the data and code the render was made from), `cycles/c18/render_first/` (the first-render Bassoon 1 stem and master). Scratch: `/private/tmp/claude-501/mockup-loop/mvt1-c18-actor/` (`lib18.py`, `holes.py`, `chk.py`, `mbeat.py`, `lowband.py`, `eqsim.py`, `eqvar.py`).

## Accepted

### A #1: weight at the start of long string accents (new tool, new rule)
- New `tools/fit_accent_bodies.py PREV RENDERED_PARTS [--front-min 2] [--max-cut 4] [--skip T:q] [--write]`. It takes string accents written (or tied) 1 qn or longer that sound at least 0.75 s, excluding notes inside or arriving at a printed crescendo and sf/fp notes. For each it measures front (score onset to +0.15 s) minus body (+0.45 to min(+0.75, end - 0.05) s), takes out the rendered envelope's share, and writes a body cut `clip(pred - 2, -max_cut, 0)` to the new `build/accent_bodies.json`.
- New generic `ACCENT_BODIES` / `ACCENT_BODY_S` in `score_to_parts.py`: the cut is 0 at score onset +0.25 s, full at +0.45 s, held to the next moved onset - 0.02 qn. parts.json key `accent_body`. A separate table was used instead of a third value in `accent_fits.json`, so `fit_accents.py` refits leave it alone.
- Run with `--max-cut 3` (not the critic's 4) and the hand values Violins I 62/65/82 skipped. 18 cuts on 19 eligible notes: Violins I 142/286/521-533/558-566, Violins II 525-566, violas and basses 676, basses 328.
- Measured on the c18 render: front-body median on those 19 went from -1.3 to +1.2 dB, with 16 -> 8 notes under 0. This is a partial pass against A's +2 / at most 6 under 0. Only 19 of A's 30 notes qualify: the rest are crescendo arrivals (Vln I/II 100, 548, celli 91/539, Vln I 154) or 1 qn notes followed by a rest (celli 321, Vln I 330), where A's body window measured the release.
- The cap is 3 dB because 521-533 is the recapitulation theme under the trumpets. Violins I minus the louder trumpet over 520-536 per half beat went from median +0.5 (15/32 under 0) to +1.6 (7/32), with B #3 included.
- The `Marc Sus LITE` test was deferred: it needs a row load and must not share notes with the body cut.

### A #2: bar 70 and the Violins I holes
- Trumpet 1 `JOIN_NOTCH` (278.45, 279.0, -6). The critic's end of 278.92 simulated the spike's last frames 3.5 dB over the F5. Result: peak 30 ms in the 0.3 s before 279 minus the F5 body, +8.0 -> +2.5 dB.
- New generic `SLUR_PAIR_RELEASE_DB_AT`, set to Violins I 279: -1. The -2.5 dB on 279.0-279.643 came from SLUR_PAIR_RELEASE.
- Exact `LEVEL_SHAPES` fills on Violins I, in seconds from the moved onset, rather than early_fills.json:
  - 279: +5 dB 0.17-0.42 s;
  - 626: +5 dB 0.04-0.09 s, then +2 to 0.40 s;
  - 720: +7 dB 0.27-0.37 s.
- Holes against the lower body: 279 6.6 -> 0.6 dB; 626 6.2 -> 2.1; 720 8.0 -> 4.1 (the 0.72-0.82 s tail of the old hole is left). No 30 ms peak more than 2.1 dB over the body, apart from the existing +7.1 at the next note's transition (626, +0.51 s).
- Master, half note's last 0.25 s against beat 4: -2.4 -> -1.7 dB (pass 2).
- Violins I was not added to `auto_fills.json` tracks. That is open: the hand shapes would need `--exclude`.

### A #3: recapitulation viola release bursts
- `LEVEL_SHAPES` Violas: -6 dB from each note-off at 527/529/531/533/535 - 0.01 qn to +0.22 qn. The critic's -5 dB / +0.20 simulated 526.5 and 534.5 still at +1.5 / +2.2.
- Post-off 30 ms peak minus body peak: +4.0/+3.3/+3.1/+3.0/+4.6 -> -0.7/-1.0/-1.2/-1.4/+0.2 dB. The dyads in between are unchanged (+1.8/+1.7).

### B #1: harp under the bar 53-55 celli
- roles Harp [206, 220, -3, 1].
- Harp minus celli over 208-220 (plain power): -1.1 -> -4.0 dB.

### B #2: Trumpet 2 at f
- `mix.json` Trumpet 2 f trim 6.2 -> 4.7 (its soft_trim mf anchor 4.7 was already there).
- roles: [272, 288, -3, 1], plus [279.75, 284, -1.5, 0.25], and 551.5-557 on Trumpets 2/3.
- Trumpet 1 minus Trumpet 2 (plain power, +0.03..+0.6 s): 280 -4.7 -> -1.7; 284 -2.5 -> +1.6; 285 -4.4 -> +0.1; 456 -1.4 -> -0.1; 554 -2.5 -> +0.4; 556 -2.3 -> -0.6.

### B #3: recapitulation trumpets
- roles Trumpets 1-3 [520, 536, -2.5, 0.5].
- Trumpet 1 re master over 520-536: -13.6 -> -15.8 dB. Violins I over the louder trumpet: as in A #1.

### B #4: double-bass F2 boom
- `mix.json` Double basses bell2 100 Hz -2 dB / 0.8 oct -> 87 Hz -6 dB / 0.25 oct (ReaEQ shows 0.24). `pitch_trims.json` Double basses "41" -2 -> 0.
- The critic's 0.35 oct simulated the master's loud-frame 20-100 Hz re 300 Hz-2 kHz 0.9 dB under c17, outside B's 0.5 dB guard. 0.25 oct keeps -4.4 dB at 87 Hz and cuts less at 78-82 Hz (E2 -2.9 instead of -3.6).
- Rendered: loud frames -12.80 -> -13.10 dB (all frames -12.23 -> -12.62).

### C #1: letter G arrival
- The `_lg_new` hold on the ten held ff parts now starts at the arrival (463.9 -> +3 at 464.05) and is +4 dB over 468.6-483.5; the critic proposed +3.5. The 484 end is unchanged.
- Master M per bar: 116 beats 2-4 -12.4; 117 -11.8 (c17 -13.6); 118 -13.1; 119 -13.9; 120 -12.9; 121 -11.2; 122 beat 1 -7.1.
- Bar 117 is +0.6 over 116 (pass 0.5); bar 119 2.1 under 117 (target 2.0); 122 is 4 dB over 121.

### C #2: bars 127-129
- Clarinet 1: start shape -3 -> 0 over 505-512; the c06 shape replaced by +3 at 512, +4.5 over 514-519.5, 0 at 520.3.
- Celli: +2 -> +4 over 508-511.7.
- Master 505-508 / 508-512 / 512-516 / 516-520: -31.2/-29.8/-27.9/-19.6 -> -32.3/-30.1/-26.9/-19.5. The rise into 512-516 is +5.4 dB (pass 4.5).
- Clarinet 1 after 512: the 516-517 window is 3.2 dB under 512-513; c17 was 7.3.

### C #3: Lento bar 3
- Exact fills: celli +7 dB over 8.82-9.2, basses +3.5, bass clarinet +3. Celli loop fill "8.0" 5 -> 3 dB.
- Master eighth-qn steps: the 3.7 dB step at 8.75 -> 2.2 dB max. Celli 8.75-9.5: -42.2..-48.9 -> -39.5..-42.1 dB (within 5 dB of 8.5-8.75).

### C #4: Bassoon 1 bar 34
- `LEVEL_SHAPES` -4.5 dB over 131.55-131.75. After the stem fix it is -6.5/-6.0: the render's 131.5 quarter stood 2.2 dB over 131.0-131.5, where the simulation gave -0.2. The sample differs between renders.
- 131.5 quarter: -32.6 -> -37.9 dB, against -38.4 for 131.0-131.5. That is 0.5 dB over the critic's criterion; the phrase now falls from 131.75.

## Rejected or deferred
- C #5: no change, as the critic proposed.
- A #1 `Marc Sus LITE`: deferred (above).
- The c17 open item on percussion seats (+0.06 at the next perc rebuild): no perc rebuild this cycle.
- Violins I in auto_fills: deferred.

## Before / after (c17 -> c18, after stem fixes)

| Measure | c17 | c18 |
|---|---|---|
| Master integrated (float stem sum) | -16.4 LUFS | -16.3 LUFS |
| Master LRA | 22.2 LU | 22.5 LU |
| Master sample peak | 1.538 | 1.509 |
| Master true peak | +3.7 dBFS | +3.6 dBFS |
| Delivered integrated | -19.8 LUFS | -19.8 LUFS |
| Delivered LRA | 14.4 LU | 14.4 LU |
| p10-to-max span | 19.1 dB | 19.0 dB |
| Delivery limiter | 2.3 dB | 1.9 dB |
| Delivered true peak | -1.7 dBTP | -1.6 dBTP |
| Motion (mp3) | 8.65 / 4.52 dB | 8.59 / 4.50 dB |

- Climax order, delivered S max: 160 -10.10 > 122 -11.31 > 167-170 -13.11 (c17 -9.99 > -11.17 > -12.94).
- Attack probe: 0 flagged.
- REAPER memory: 18 GiB with 0 compressed at the render start; 45 GiB with 29 compressed after it.
- Delivered mp3: `cycles/c18/mvt1-mockup-c18.mp3`.
