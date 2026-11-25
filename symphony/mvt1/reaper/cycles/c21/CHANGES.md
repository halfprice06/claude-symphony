# Cycle 21: changes (actor)

This cycle ran two patch-state tests: a shorter Sus MAX release on three string tracks and a narrower horn width. It also made two timing changes, played one note as a new stroke, and made level and EQ changes.

REAPER steps:
1. Fresh start, project opened (33 tracks).
2. `build_reaper.py build/parts.json jobs --midi-only` on Oboe 1, Cor anglais, Clarinet 1, Horns 1-4, Trumpets 1-3, Trombones 1-2, Bass trombone, Timpani, Tam-tam, Violins I/II, Violas, Violoncellos, Double basses and Horns a2. Seven tracks were fully rebuilt because their Opus state changed: Horns 1-4 (width and seats) and Violas, Violoncellos and Double basses (release cap).
3. Save. The quit job timed out, so REAPER was killed after the save. Fresh start, open, render (`render_cycle.py 21`).
4. One level-only stem fix (`stem_fix.py 21 cycles/c21/rendered_build build --apply Violas Violoncellos "Double basses"`; originals in `cycles/c21/render_first/`), then `render_cycle.py 21 --measure-only`. Then `build_reaper.py --mix-only` on the same three tracks so the project matches `build/`. Save. The quit timed out and REAPER was killed after the save.

Files:
- `cycles/c21/before/`: the c20 tools and data.
- `cycles/c21/rendered_build/`: the data and code the render was made from.
- Scratch: `/private/tmp/claude-501/mockup-loop/mvt1-c21-actor/`. It holds `pdiff.py`, `f607.py`, `bchk.py`, `cchk.py`, `clim.py`, `bardiff.py` and `peak.py`, plus copies of the critics' scripts in `A/`, `B/` and `C/`.

## Code

- `tools/build_reaper.py`: new mix key `sus_release_cap_ms` (`cap_release()`).
  - It caps the AHDSR release of the sustain groups of the listed rows (default Sus MAX) whose names end in a listed dynamic (default mf/f/ff).
  - A group belongs to a row when all of its regions sit on that layerMatrix row.
  - RT release trails, TLeg transitions and the softer layers are not changed.
  - The matched groups are printed:
    - Violas: Va f 333/394, ff 323/394, mf 394/650/653 ms.
    - Celli: Vc mf/f/ff 524 ms.
    - Basses: Db f/ff 524, mf 700 ms.
- `tools/score_to_parts.py` (all generic):
  - `LEG_MIN_GAP_S`: a legato target never starts closer than this to the previous note's moved onset.
  - `LEG_CAP_FRAC` entries can take a 4th element "listed". The raised cap then applies only to onsets listed in `leg_leads.json`.
  - Per-onset `leg_leads.json` leads now also act on fast_leg / Slur Runs targets, capped at `FAST_LEG_LEAD_CAP` 0.75 of the previous note.
  - `GROUP_LEAD_AT` group notes now end at most 0.03 qn after the next group note's moved onset. Without this, the run's E overlapped the new F stroke by 0.26 qn.

## Accepted

### A #1 (test, partial pass): Sus MAX release cap 250 ms on Violas, Violoncellos and Double basses (`mix.json`)

Measured c20 -> c21:

| Measure | c20 | c21 | Pass |
|---|---|---|---|
| Basses Sus MAX, -10 dB after the note-off | 0.35 s | 0.26 s | ≤ 0.22 s |
| Celli Sus MAX, -10 dB after the note-off | 0.47 s | 0.47 s | ≤ 0.22 s |
| Violas Sus MAX, -10 dB after the note-off | 0.30 s | 0.30 s | ≤ 0.22 s |
| Master cut-off, qn 103 / 126 / 551 | 0.20 / 0.28 / 0.27 s | 0.13 / 0.24 / 0.23 s | ≤ 0.20 s at 126 and 551 |
| Celli cut-off, qn 103 / 126 / 551 | 0.34 / 0.47 / 0.47 s | 0.17 / 0.41 / 0.37 s | |
| Basses cut-off, qn 103 / 126 / 551 | 0.23 / 0.31 / 0.44 s | 0.14 / 0.19 / 0.35 s | |
| String Sus short rests, median drop | 4.1 dB | 5.8 dB | |
| String Sus short rests under 6 dB | 36 of 41 | 25 of 41 | |
| Violas' rest drop | 4.3 dB | 5.8 dB | ≥ 7 dB |
| Basses' repeated eighths, re-attack dip, bars 27-31 | 0.5 dB | 0.9 dB | ≥ 2 dB |
| Basses' repeated eighths, re-attack dip, bars 131-134 | 1.8 dB | 1.7 dB | |

- The celli and violas did not change on the critic's few long-rest notes (n 5 and n 2). Those may be softer notes, or the instrument-level `envelope.releaseTime` (931 ms) may still act. Not tested.
- String joins of 6 dB or more: 4 -> 5. The new one is Violins II 637 (5.8 -> 7.2), a track this cycle did not change, so it is render variation.
- Re-bows. The basses' re-bow dips deepened (median -1.5 -> -3.2 dB) and the violas' a little (-2.3 -> -2.7). The Double basses and Violas `rebow_fills.json` rows were refit on c21 (`fit_rebows.py 21 --hold-max-after 720:0`) and applied by the stem fix. Median dip after the fix:
  - basses -1.2;
  - violas -2.2;
  - celli -2.8 (c20 -2.6).
  
  The celli refit was simulated and not kept: it lowered the held bars 73-77 by 2.4-3.6 dB.
- The basses' loud bars are 1-2 dB lower in plain RMS: less tail energy between notes.
- pp/p groups were not changed. Celli bar 13 is -1.4 dB and violas bars 164-165 are -2..-2.7 dB, which are the B #1 shape.
- Not done: refits of the accents, auto_fills, ABUT_LEAD and the coda basses steps for these tracks. Open for c22.

### A #2: bar 152 F (607) as a fresh Sus MAX stroke on violas and celli (`DOWNBOW_STROKE_AT`, with the GROUP_LEAD 0.12 s)

| Section | F first dominant from 607, c20 -> c21 | F body minus run, c20 -> render -> stem fix | Largest 30 ms dip, 606-608, c20 -> c21 |
|---|---|---|---|
| Violas | +0.11 -> -0.07 s | -1.9 -> +0.6 -> +1.3 dB | 7.4 -> 6.2 dB |
| Celli | +0.21 -> +0.01 s | +4.6 -> -0.1 -> +3.1 dB | 8.9 -> 8.1 dB |

- The stroke plays at v105. The celli's F body fell 6.6 dB, so the stem fix added +5 dB on the celli and +1 dB on the violas over the F.
- The dips stay over the 5 dB limit. They are at the run.

### A #3 (partial pass): celli second-theme arpeggios
- `LEG_CAP_FRAC` 0.75 "listed" over 219-252 and 616-632, `leg_leads.json` +0.06 s on the 18 rising steps of 5 semitones or more, and `LEG_MIN_GAP_S` 0.10 s.
- Crossover on the 36 steps, c20 -> c21:

  | Measure | c20 | c21 | Pass |
  |---|---|---|---|
  | Median | +0.083 s | +0.070 s | ≤ +0.07 s |
  | p75 | +0.140 s | +0.116 s | |
  | Over +0.15 s | 7 | 2 (239.0 +0.245, 626.0 +0.155) | |
  | xall dips of 6 dB or more | 12 | 16 | not more than c20 |
  | joins.py celli joins of 6 dB or more | 3 | 3 | |

- The master dips at these steps are unchanged (-1.5..-4.6 dB).

### A #4 (partial): Violins I bar 68
- 270.25 (the Slur Runs target a major third from the head) has a 0.10 s per-onset lead. It was capped to 0.072 s.
- First dominance +0.217 -> +0.167 s, dominance share 0.00 -> 0.12. The pass is +0.08 s and 0.4.
- 160 was not changed: its lead is already at the 0.75 cap of the 0.25 qn run note before it.

### B (level only; plain RMS)

| Item | Change | Measure | c20 | c21 |
|---|---|---|---|---|
| #1 | Oboe 1 hairpin target mf at 648; Violins I +3, violas -2 and Clarinet 1 -2 over 652-662 | Oboe 1 re master, 650-651.9 | -7.1 | -11.6 |
| | | Violins I re master, 650-651.9 | -8.8 | -8.3 |
| | | Violins I minus Clarinet 1, 652-662, median | +1.3 | +6.9 |
| | | Violins I minus violas, 652-662, median | -0.9 | +4.1 |
| | | Master bars 163/164/165 | | -27.1 / -29.4 / -32.4 |
| #2 | Cor anglais role [586, 605, 4, 0.5] and -2 at 608 | Melody (violas + celli) minus cor anglais, 602-620, median | +4.8 | +8.6 |
| | | Half beats under 0 | 4 | 0 |
| #3 | Cor anglais -2.5 at 687.3-694.8, celli +3.5 at the crest | Celli crest | -38.0 | -35.0 (bar 172: -33.4) |
| | | Celli minus cor anglais at the crest | -1.6 | +3.9 |
| | | Celli minus cor anglais, 683-695, median | +3.0 | +5.1 |
| | | Half beats under 0, 683-695 | 4 | 0 |
| #4 (test) | +3 dB on the timpani rolls over 464-492, 628-644 and 664-676 | Rolls re master | -15.4..-18.8 | -12.6..-15.9 |
| #5 | Violins II -3 at 452.8-456.2; Horns a2 -1.5 at 310.5-311.5 | Violins I minus Violins II, 453.5-454.5 | -5.6 | -2.6 |
| | | Bars 78/79 | -32.1 / -32.2 | -32.5 / -32.1 |

- B #4: climax windows unchanged. The master's top sample peak rose from 1.480 to 1.534 at 636.19 (Timpani -0.129 of it, in phase with the trombones and tuba), and the limiter went from 1.7 to 2.0 dB.

### C (mix.json)

**#1: brass 4 kHz high shelves.** Trombones -4 dB, trumpets +2.5 dB, and the Trumpet 1 climax shelf -14 -> -6 dB. Share of the master's 5-10 kHz:

| Span | Trumpets c20 -> c21 | Trombones c20 -> c21 | Master 5-10 kHz | Master 10-17 kHz |
|---|---|---|---|---|
| qn 634-640 | 5.6% -> 21.0% | 19.3% -> 7.8% | +0.4 dB | +0.2 dB |
| qn 464-492 | 13.6% -> 27.0% | 45.3% -> 23.8% | -0.7 dB | -1.5 dB (target ±0.5) |

**#2: tam-tam 86 Hz bell2, -9 dB, 0.3 oct.** Its 71-89 Hz excess over the rest of the orchestra:

| Bars | c20 | c21 | Target |
|---|---|---|---|
| 122-123 | +10.2 | +3.9 | at most +9 |
| 124-126 | +12.6 | +5.9 | at most +9 |
| 175-176 | +12.2 | +3.6 | at most +4 |

- Master bar totals are within 0.2 dB.
- The pp stroke stem is 4-6 dB lower in plain RMS in bars 175-178 (the critic simulated 2.5-3.2).

**#3 (test FAILED on its aim): Horns 1-4 width 0.15, Horn 3/4 seats -0.38/-0.40.**
- Per-pitch R-L is unchanged within about 1 dB (F4 -10.1/-11.2/-10.4 -> -10.2/-11.1/-10.7; Horn 1 Eb4 -9.2 -> -10.4). The offsets are not from the mic-pair pan spread.
- Horn 4 moved left (G3 0.0 -> -1.6 dB R-L).
- Horn levels are within 0.3 dB of c20 by dynamic, except Horn 3 ff -1.0 and Horn 4 bars 104-105 -1.6..-2.0.
- Kept, because a rebuild is needed to change it back. Revert the width with the next horn rebuild.

## Rejected or deferred
- A #1 fallback (MIDI early ends, or Marc Lng for the basses' eighths): deferred until the release cap is fully understood. The next step is the instrument-level `envelope.releaseTime` on these three tracks.
- A #4 160: not changed (at the cap).
- B #5 bass clarinet 11.0 loop: deferred to A's lens.
- C's alternative trumpet mic change: not needed.

## Before / after (c20 -> c21, after the stem fix)

| Measure | c20 | c21 |
|---|---|---|
| Master integrated (float stem sum) | -16.4 LUFS | -16.4 LUFS |
| Master LRA | 22.5 LU | 22.6 LU |
| Master sample peak | 1.480 | 1.534 (qn 636.19) |
| Master true peak | +3.4 dBFS | +3.7 dBFS |
| Delivered integrated | -19.8 LUFS | -19.8 LUFS |
| Delivered LRA | 14.4 LU | 14.4 LU |
| p10-to-max span | 18.9 dB | 19.0 dB |
| Delivery limiter | 1.7 dB | 2.0 dB |
| Delivered true peak | -1.6 dBTP | -1.7 dBTP |
| Motion (mp3) | 8.62 / 4.47 dB | 8.58 / 4.48 dB |

- Climax order (delivered S max): 160 -10.00 > 122 -11.50 > 167-170 -13.10.
- Attack probe: 0 flagged.
- REAPER memory: 26 GB with 0 compressed at the render start; 46 GB with 29 GB compressed after it (31 GB compressed at the final save).
- Delivered mp3: `cycles/c21/mvt1-mockup-c21.mp3`.

## Open for c22
- A #1: the celli and violas Sus MAX releases mostly did not shorten. Test `envelope.releaseTime`, and refit the accents, auto_fills, ABUT_LEAD and the coda basses steps on these tracks.
- Revert the horn width 0.15 at the next horn rebuild (no effect).
- Violins I 270.25 is still late (+0.167 s).
- Celli 239.0 is still +0.245 s.
- The 607 run holes are 6-8 dB.
- Delivery limiter is 2.0 dB (timpani at the 636 peak).
- Basses loud bars are 1-2 dB lower.
- Tam-tam pp stroke is 4-6 dB lower.
