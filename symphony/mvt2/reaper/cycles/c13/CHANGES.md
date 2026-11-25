# Cycle 13 changes (actor)

Snapshot of the c12 tools and build/*.json: `before/`. Scratch and analysis: `/private/tmp/claude-501/mockup-loop/c13-actor/` (`check.py` compares the c12 and c13 stems for every accepted finding; `statecheck.py` lists which Opus states a build would change; `orig/` holds the render's own master, cello-div stem, mp3 and metrics before the gain fix below).

## Process

1. Edited `tools/score_to_parts.py`, `tools/build_reaper.py` and the build JSON files; regenerated parts.json and diffed it against `before/build/parts.json`. Checked offline that only the intended Opus states change (Bass clarinet, Double basses, Harp harmonics, Violin I solo, and the new Violoncellos div).
2. `build_reaper.py build/parts.json jobs --midi-only`: 24 tracks updated in place, the 5 tracks above fully built (29 tracks). Saved, quit and reopened REAPER (`open -a REAPER --args -new`, project opened by a bridge job; 17 GB, 0 GB compressed).
3. One render (`render_cycle.py 13`). Attack gate 18 of 19: the one failure is Violoncellos qn 212 at 6.6 dB, the same value as c12 (the known marginal tremolo probe), so it was not re-rendered. Other work on the Mac compressed 37 of REAPER's 56 GB by the end of the render.
4. After the render the cello answer measured 10-12 dB under the solo violin. I raised the track's gain from -2 to +4 dB in mix.json, applied it in REAPER (`--mix-only "Violoncellos div"`, saved), scaled that stem by +6 dB and rebuilt the master as the stem sum. Before the change the stems summed to the master within -121.6 dBFS, so the rebuilt master is exact. measure.py, the probe and deliver_master.py were then run again. The track plays only in bars 17-22.

## Accepted

**A #1: cello divisi answers on their own track** (`score_to_parts.py` `TRACK_SPLITS`, new track "Violoncellos div", stem 29)
- Patch: `Celli Divisi/06 Keyswitch/Celli KS Master DIV A.oib`, a half section with only the Close mic. Its keyswitch map was dumped into `build/ks_maps_extra.json`.
- Violoncellos notes with a score onset in [51, 54) or [63, 66) and pitch 55 or higher (60/63/60/61 and 55/56/58/55) move to the new track. Both answers now play Leg Slur MAX with the string leads.
- The Violoncellos track keeps the lower voice as a single line (49 -> 48 -> 46 -> 53 joins; 51 at qn 63 merges with the unison E flat at 66, with a bow-change notch). The split-off notes still count for its divisi cut (-3 dB), because a full-section patch is playing a half section's line.
- mix.json: seat 0.35, width 0.2, send 0.5, Vc's EQ; gain +4 (set after the render, see Process 4).

**A #2: soft bow-change joins** (`score_to_parts.py`)
- `VLA_BC_SOFT["notch"]` 8 -> 4, `BC_SOFT["notch_soft"]` 6 -> 3.
- New `joined_next(n)`. A slur's last note whose next note joins it (bow-change target or overlapped legato target) is not a phrase end, so it gets "swell" instead of "swell_taper". bloomv skips such a note: only Vc qn 124 now. Vc 54 and 66 lost bloomv for another reason: 54 became a legato target and 66 was merged, both because of A #1.
- `early_fills.json` Violoncellos 68: 4, 78: {db 3, hold_s 0.3}. These are smaller than A's 5/5, because removing the plan dip (4.0 and 5.2 dB) already takes part of each hole.

**A #3: timpani roll hairpins** (`score_to_parts.py`, `TIMP_HP_DB_FACTOR` 1.0)
- Rolls with a hairpin get the half of the planned dB change that CC7 does not deliver, in the volume envelope, relative to the roll's start. It is held to the roll's end and released by the next onset. qn 168 +2.4, qn 200 +5.0, qn 268 -4.8.
- roles.json Timpani [200, 203.5, -3] deleted.

**A #4:** early fills BCl 92/93/98/99, Ob1 143 4 -> 8 and 145, CA 97/126/128/129/131.5, Cl1 176/178, as A proposed.

**A #5:** a wind or brass note at CC11 72 or above ends min(0.3 qn, half its length) before a breath (was min(0.25, 0.2 x length)). This shortens Hn1 195 and the loud wind and brass notes before the qn 204 and 268 breaths by 0.05-0.1 qn.

**B #1-#4, #6 pitch trims** (`pitch_trims.json`): Clarinet 2 {68: +6, `_all_arts`}; Clarinet 1 68 +6 (`_all_arts_pitches` [68]); Bassoon 1 {51: +6, 55: +4, `_all_arts`}; Bassoon 2 51 +6, 55 +4; Double basses {32: -5, 37: -2, 39: +4, `_arts` ["Sus MAX"]} (the pizz. notes no longer take the trims); Cor anglais 61 +4.

**B #2** (`note_trims.json`): Oboe 1 42 +5, 54 +5; Violas 54 -7, 48 -4.

**B #5:** roles.json Harp [172, 188, -4] deleted.

**C #1:** `apply_mix` centres every Opus state's main (Master) channel. The DIV A patches ship it panned: 1st Violins DIV A -0.74, Celli DIV A +0.33. Every other state already had it at 0, so their states are unchanged. Violin I solo seat -0.55 -> -0.4.

**C #3** (mix.json Double basses): 90 Hz -5 dB low shelf removed, 160 Hz bell +6 -> +3, Close 0.4 -> 0.6, gain -7 -> -8. I added a 25 Hz high pass (lowest note E1, 41 Hz) so the sub-bass does not rise with the shelf gone.

**C #4:** Bass clarinet seat -0.25 -> -0.05. **C #5:** Harp harmonics seat -0.35 -> -0.65.

## Rejected or deferred

- **C #2 (true-stereo hall IR): deferred.** It needs a full rebuild of all 29 tracks and a test render before the full render. With one render per cycle, and several level changes riding on this one, I could not test it without confounding them. It is the best candidate for a cycle that does only this: rebuild, restart, render, and compare tails against c13.
- **A #2 fills at A's sizes (5/5): reduced** to 4/3 (see above).
- Still open from c12: the viola sextuplet articulation test and the bar 53 pickup.

## Measured, c12 -> c13 (plain RMS on stems unless noted; `check.py`)

**Delivery**

| | c12 | c13 |
|---|---|---|
| Master integrated | -23.6 LUFS | -23.3 LUFS |
| Master LRA | 23.9 LU | 23.9 LU |
| Master true peak | -3.9 dBFS | -3.6 dBFS |
| mp3 integrated | -19.8 LUFS | -19.8 LUFS |
| mp3 LRA | 15.7 LU | 15.8 LU |
| mp3 true peak | -1.6 dBTP | -1.6 dBTP |
| mp3 span (p10 to max) | 18.4 dB | 18.2 dB |
| Limiter | 3.0 dB | 3.2 dB |

**Findings**
- A #1, answer body: Vc div at -52.0 dB (bar 18) and -50.3 (bar 22), against the solo violin's -45.8/-46.4. That is 6.2 and 3.9 dB under (target 3-6). In c12 the answer had no stem of its own.
  - Summed Vc + Vc div at the entry: the deepest frame is 6.6 dB under the frame before at qn 51 (c12 about 10) and 4.6 at qn 63 (c12 about 10). The target of 4 is met at 63, not at 51.
- A #2, Vc counter-melody, per quarter: qn 67/68 -46.6/-47.7 -> -44.1/-44.2 and qn 78 -47.2 -> -45.7. The other joins are within 0.5 dB of c12.
- A #3, qn 200 roll: -43.7 at qn 200 -> -33.8 at 203, +9.9 dB (c12 +5.3; target 9 or more). At qn 202-203 it is 4.7 dB under Vln I (target 6-9: about 1.5 dB hot) and never the loudest stem. The qn 268 roll falls 8.4 dB by qn 271 (c12 4.5; target 6-8).
- A #5: Hn1's minimum before qn 196 goes from -44.5 to -45.4 dB (10.3 dB under the note body). The gain is small: the hall tail fills most of the gap.
- B #1, Cl2 Ab4: +5.4 to +5.8 dB. qn 253/254 -42.9/-42.3, then Bb4 at 255 -38.9: a 4 dB step inside the crescendo (c12 10 dB).
- B #2: Ob1 at qn 42.5 -54.8 -> -49.8 and qn 54.5 -54.6 -> -50.1. Vla at 54.5 -40.1 -> -47.1. Plain RMS: the oboe now leads at 42.5 and trails the viola by 3 dB at 54.5. Critic B's check is A-weighted and was not repeated.
- B #3: Bn1 Eb3 notes in bars 7-11 +4.5 to +5.6 dB (qn 18 -57.0 -> -51.5, qn 27 -55.1 -> -49.7).
- B #4: Cb qn 84 -50.1 -> -44.9 and qn 193 -48.7 -> -42.2. Cb minus Vc per bar in bars 83-92 stays within -3.5..+3.2 dB (c12 -3.3..+4.2).
- B #5: harp at qn 172-188 -46.8 -> -42.8.
- C #1: solo violin R-L -21.1 -> -5.1 dB (target -7..-4); level -45.4 -> -45.8.
- C #3: 20-100 Hz share -16.3 -> -15.1 (target -14.5..-12.5, not reached; the -1 dB gain and the B #4 Ab1 -5 hold it down); 63 Hz third vs 1 kHz +2.0.
- C #4: BCl R-L -5.3 -> -2.5 (target -4..-2). C #5: harmonics R-L -3.9 -> -5.0, the harp -6.0 (within 2 dB).

## Open
- C #2 true-stereo hall (see above).
- The qn 200 timpani crescendo ends about 1.5 dB hot against Vln I. Try roles Timpani [200, 203.5, -1.5] or `TIMP_HP_DB_FACTOR` 0.8.
- Cello answer entry at qn 51 is still a 6.6 dB dip (the DIV A Leg Slur first note's attack). Try an entry fill or an extra entry lead on the div track.
- Cb sub-bass share still 0.6 dB short of C's range. Next step: Cb gain -8 -> -7, or the low shelf at -2.
- C #2's coherence and tail checks were not measured this cycle (no reverb change).
