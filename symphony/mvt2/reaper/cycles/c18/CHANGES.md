# Cycle 18 changes (actor)

Snapshot of the c17 tools and build/*.json: `before/` (its `parts.json` is the data of the c17 render). Scratch and analysis: `/private/tmp/claude-501/mockup-loop/c18-actor/`:
- `diffparts.py OLD NEW`: per-track differences between two parts.json files (notes, CCs, vol_db spans).
- `chk.py`: divisi window levels, a2 horn level, climax per beat, theme A per beat, Oboe 1 decrescendo, master peaks (c17 against c18).
- `cC/`: critic C's `peaks.py` re-pointed at c17 and c18.
- `orig_render/`: the rendered stems that were changed after the render, as rendered.

## Process

1. Edited `tools/score_to_parts.py` and `tools/probe_attacks.py`, and `build/{roles,mix,early_fills,entry_leads,loop_fills,loop_profiles,ks_maps_extra}.json`. Reran `auto_fills.py 17` on the c17 render (excluding Oboe 1 140/189/271). Regenerated parts.json; the tempo map is unchanged.
2. `build_reaper.py --midi-only`. Five tracks were fully rebuilt: Violoncellos and Double basses (width) and the three new tracks. The other 27 were updated with `--midi-only`.
3. Saved and quit. The quit (command 40004) stopped at a modal dialog (`sample` showed `runModalForWindow` under `Main_OnCommand`), probably a save prompt. The project had been saved just before, so I killed REAPER, started it with `-new` and opened the project with a bridge job. The open took 8 minutes and did not deadlock.
4. One render (`render_cycle.py 18`). It started at 0 GB compressed. REAPER finished loading at 56 GB, about 10 GB more than c17, because of the three new tracks. After the render it was at 63 GB with 43 GB compressed. Attack gate 19 of 20: the known Vln I 171 artefact again, at +0.34 s as in c17.
5. Post-render fixes. Each one is a pure gain or volume-envelope change, so I applied it to the stem and rebuilt the master as the stem sum. Before the change the stem sum matched the rendered master to 8e-7. REAPER was then updated with `--mix-only` and saved, so the project matches the tools.
   - **Horns 1-2 a2:** measured 4.6 dB under c17's Horn 1 over 262-268. Gain -4 -> +0.6; stem +4.6 dB.
   - **Violins II div:** gain 10 -> 8.5; stem -1.5 dB.
   - **Violas div:** roles [276.5,304,-5]; stem -5 dB from qn 276. At 277-280 the DIV B ppp Eb4 was 7.6 dB over the main track's C4.
   - **Horn 1 qn 34 fill:** replaced (see C #2 below). I computed the stem correction from `build_reaper.vol_points` of both parts.json files: -8..0 dB over 39.86-40.88 s.

## Accepted

- **A #1. `WIND_VIB_CAP = None`.** The `cc1_fn` condition is guarded. Flute 1 1.5-4 kHz modulation at 204.5-211.5: 15.5 -> 8.1 dB p95-p5 (4.3 Hz, autocorrelation 0.66). That is better than c16's 10.1.
- **A #2. Divisi tracks**, appended as stems 30-31. Both use DIV B KS Masters; their maps, dumped with `dump_ks.py`, are identical to the full sections' maps and are in `ks_maps_extra.json`.
  - "Violins II div" (2nd Violins KS Master DIV B, Flautando row) at 108-124. Split at pitch 64. It is in `FLAUT_JOIN_TRACKS`, and the Vln II roles [108,124,-5] / [114,116,3] and entry lead 108 are copied to it.
  - "Violas div" (Violas KS Master DIV B) at 66-90 and 277-289. `TRACK_SPLITS` has a new `"rank"` mode: a note goes to the split track when another source note starts with it at a lower pitch. The viola roles [80,90,-3] and [286,292,-1] are copied.
  - mix.json: section seat, width 0.3, send 0.5 (Close mic only, like the Vc div).
  - Both main tracks keep the -3 dB chord cut through `split_away`. Each viola voice is now a single line, so it plays Leg Slur / Leg BC instead of Sus MAX dyads (Violas Sus MAX 79 -> 49 notes).
- **A #3. Loop profiles:** the critic's c17 refit of Vln I 0/292, Vc 164 and Cb 220. The Vc 164 profile is capped at +7 dB (7 points).
- **A #4. "Horns 1-2 a2"** (2FH KS Master, stem 32): `TRACK_WINDOWS` 261-272, with Horn 1 and Horn 2 excluded there. The Horn 1 role [262,268,4,0.5] moved to the new track, and entry lead 261 0.08 was copied.
- **A #5. Wind fills.** `auto_fills.py` rerun on c17 (31 entries: 14 new, 4 raised, the rest lowered or removed). Then the critic's lower values by hand: Fl1 252 2.1, CA 132 3.1, CA 134 1.7, CA 97 1.1, Cl1 258.5 0.5. Cl1 256 and Cl1 178 were removed.
- **C #1. Theme A swell and soft decrescendos.**
  - `SWELL_SOFT_GAIN_AT` (Vln I/II 68 and 240): a +2.5 dB messa di voce, released across the paired decrescendo to -1 dB, back to 0 over 1 qn.
  - A decrescendo is now skipped only when it is in `used_dec`. A decrescendo that starts within 0.3 qn of an hpgain (mf) crescendo's end passes the CC11 66 filter (`after_mf_`); without this, Oboe 1 148 (mf) would still have been skipped.
  - `HP_SOFT_DEC_AT` Oboe 1 148: 4 dB. Violins I early fill 71: 5 -> 2.
  - New soft decrescendo ramps: Oboe 1 148, Bass clarinet 96, Horn 1 22, Vln I/II 82.
- **C #2. Horn 1 crest at qn 34: accepted in changed form.**
  - The critic's 10-11 dB collapse was measured on the mono fold. L and R are anti-correlated there: corr -0.7 to -0.86 from s+0.5 to s+1.0 s. In stereo power the dip is 7 dB for one 50 ms frame at s+0.55 s.
  - The proposed lifts (+8 at moved+0.9 s, +4 at +1.25) rendered as a +6..9 dB bump: bar 12 +3.8 dB, beat 34 -28.4 against -34.0.
  - Replaced by one lift, `loop_fills.json` Horn 1 34 [[0.825, 4, 0.12]], and the stem was corrected. The probe now measures stereo power.
  - Result: dip 7.3 dB (c17) -> 3.3 dB, and beat 34 -34.0 -> -31.5 (+2 of this is the phrase-top shaping).
- **C #3. Climax.**
  - (a) `JOIN_NOTCH` Violins I (207.80, 207.97, -4 dB), exact breakpoints.
  - (b) `_all` [204,212,-1.4] -> [204,212,-1.4,3.5].
  - (c) Strings [211.75,213,1.5,0.5].
- **C #4. Phrase tops.** In `LEAD_SPANS` slurs of 4 or more onsets, each onset gets clip(0.3 x (top pitch - slur mean), -1.5, +2) dB, stepped at the moved onsets, as exact breakpoints. This shaped 29 slurs.
- **C #5. pp lifts:** `_all` [9,17,2], [220,226,2], [274,280,2].
- **c17 deferred C #4.** Violoncellos and Double basses width 0.35 -> 0.28 (full rebuilds).

## Rejected or deferred

- **A #2 memory note.** REAPER loaded to 56 GB with 32 tracks, and the render ran normally. The 277-289 viola window was kept.
- **C #5 extras** ([35,36.9,1.5] and the morendo [298,304,1]): not added. The LRA reached 16.0 without them.
- **Open:**
  - The final rest after a track's last note has no tail hold. A role that ends after the last note moves the hall tail (Violas [286,292,-1] ends at 292.5, after the last viola note). Add the final rest to `tail_hold` next cycle, then rebuild all tracks with `--midi-only`.
  - Three wind joins have deeper 200 ms dips after the lowered fills: Ob1 143 4.1 -> 6.7, CA 132 5.1 -> 7.2, CA 134 4.3 -> 6.4 dB. Their overshoot is now at most +2.4 dB. Rerun `auto_fills.py 18`.
  - Vc 164 loop pulse 7.2 dB, over the 6 dB target (capped profile).

## Measured, c17 -> c18 (after the post-render fixes)

| | c17 | c18 |
|---|---|---|
| Master integrated | -22.5 LUFS | -22.5 LUFS |
| Master LRA | 24.3 LU | 23.6 LU |
| Master true peak | -2.3 dBFS | -4.1 dBFS |
| mp3 integrated | -19.9 LUFS | -19.8 LUFS |
| mp3 LRA | 16.3 LU | 16.0 LU (target 14-16) |
| mp3 true peak | -1.6 dBTP | -1.6 dBTP |
| mp3 span | 18.9 dB | 18.6 dB |
| Limiter | 3.4 dB | 1.7 dB |

- **Clipping and stems.** No clipping, and all 32 stems are present.
- **Master peaks.** The top peak at 207.87 went from -2.26 to -4.06 dBFS. The next peaks are 206.72 (-4.16) and 263.66 (-4.53).
- **Climax, master RMS per beat.**
  - qn 208-211: c17 -16.6, -17.8, -18.1, -18.2; c18 -16.8, -17.6, -17.4, -17.0.
  - The sf at 212: -19.9 -> -18.7.
  - Bar 61 is 2.2 dB over bar 79 (c17 1.8).
- **Theme A, Vln I+II per beat.**
  - Qn 68-71: c17 -36.4, -37.9, -36.2, -35.9; c18 -35.7, -36.0, -34.6, -36.9. The < now rises 1.1 dB and the > falls.
  - Reprise qn 240-244: c18 -41.0, -39.0, -37.6, -39.7. That is +3.4 dB up the <, then down.
- **Oboe 1 148-151 per 0.5 qn.** c17 -39.6..-41.0; c18 -40.6 -> -44.5.
- **Phrase tops (critic C's `peaks.py`).** The top note over the rest of its slur: median +1.3 -> +3.7 dB. It is the loudest note in 13 of 23 slurs (c17: 9 of 25; two Horn 1 slurs moved to the a2 track).
- **Loop pulse, p95-p5:**
  - Vln I 0: 8.6 -> 5.7
  - Vln I 292: 7.5 -> 5.8
  - Vc 164: 9.0 -> 7.2
  - Cb 220: 3.7 -> 1.9
  - The other six are unchanged.
- **Wind joins, over at 200 ms:**
  - Fl1 252 +4.9 -> +1.5
  - Ob1 143 +3.1 -> +2.4
  - CA 132 +3.1 -> +1.9
  - CA 134 +3.3 -> +1.4
  - Cl1 258.5 +2.9 -> +2.6
- **Divisi, main + div RMS against c17:**
  - Violas 66-90: -0.8 dB.
  - Violas 277-289: +0.5 dB. The `_all` +2 covers 277-280.
  - Violins II 108-124: +0.8 dB.
  - The detrended 0.25 qn troughs are unchanged: 5th percentile -2.4 against -2.2 at 66-90, -1.6 against -1.9 at 108-124.
- **Horns a2.** 262-268 is within 0.0 dB of c17's Horn 1, and 268-272 is +1.0.
- **Bars that changed by 0.8 dB or more:**
  - pp lifts: bars 4-5 +2.0, bar 65-66 +2.0/+2.1, bars 83-84 +1.9/+2.1.
  - Horn crest: bar 12 +1.9.
  - Bar 32 +1.3, bar 82 +1.0.
  - Bars 29/31/47 -0.8..-1.0 (phrase-top cuts and the lowered fills).
