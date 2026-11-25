# Cycle 21 changes (actor)

Snapshot of the c20 tools and data: `cycles/c21/before/`. All 32 tracks were updated with `build_reaper.py build/parts.json jobs --midi-only`. No Opus state changed, so no track was fully rebuilt. Then save, quit (the quit job timed out, but REAPER exited), `-new` restart and `Main_openProject` (32 tracks). One render: 21 GB and 0 GB compressed at the start. During the render REAPER reached 63 GB, with 51 GB compressed, and the Mac had 0.5 GB free. The render finished. Attack gate 18 of 20: Vln II and Vc at qn 212 dipped 6.7 and 7.6 dB, the same values as c20 (known threshold noise). No post-render fixes.

## Accepted

### Critic A
- **A #1 transition spikes (tools/score_to_parts.py `JOIN_NOTCH`).** I added the 16 notches as given (Vln I 68/72/73.5/75/80, Vc 68.5/182/240.5, Vln II 177.5/243/245.5/270.5, solo violin 53, Horn 1 30, Violas 162). The Vln I 207.80 entry is kept.
- **A #2 fills on transition peaks (build/early_fills.json).** I set these by hand and noted them in `_auto` as "c21 lowered by hand":
  - Ob1 145: 6.8 -> 2.0.
  - Vln I 80: 4 -> 2. Vln I 68: 3 -> 1.5.
  - Vc 256: 3.4 -> 1.0. Vc 156: 4.0 -> 1.5.
  - Fl1 193: 6.0 -> 3.0. Fl1 194: 4.6 -> 2.0. Fl1 129.5: 4.8 -> 2.5.
- **A #3:** `ACCENT_DB_AT` Trombone 1 218: 3.0 -> 4.5.
- **A #4:** early fill Violins II 172.0 `{"db": 4, "pre_s": 0, "hold_s": 0.35}`.
- **Routine `auto_fills.py 20`** on the c21/before parts.json. It changed 8 entries: raised Ob1 143, Cl1 178 and Hn1 202 (6.5 -> 8.0); lowered Cl1 266, BCl 92.5 and Vc 259; removed Fl1 193.5 and Vc 210.
  - I excluded the hand-set notes above, plus CA 132/134 and Fl1 257.5/258.5.
  - I also excluded Vc 203 and Fl1 200. auto_fills removed both in c20 and wanted to add them back, so they would keep switching on and off.

### Critic B (build/roles.json, note_trims.json, pitch_trims.json)
- **B #1 bars 56-58.**
  - Violoncellos `[188,204,-6,4]` -> -3. Double basses `[188,204,-3,4]` -> -1.
  - Vc note trims: 190 -4 -> -1.5, new 193 -3.
  - Bassoon 2 pitch-trim `_skip_onsets` += 193, 198.
- **B #2 bar 58 flute.** Flute 1 `[191.5,196,-3]`. Fills 193/194 as in A #2. I used the lower of the two critics' values for 194 (2.0).
- **B #3 bars 37-40 flute.** Flute 1 `[112,124,2]`, and note trims +4 on 110, 110.5, 113, 113.5, 117, 117.333 and 117.667.
- **B #4 bars 54-56 horn.** Horn 1 `[176,188,-3]` -> 0.5, and note trim 180 -2.
- **B #5 harp dyad at qn 26.** note_trims Harp `{"26": -5}`. The note-trim code (`score_to_parts.py`) now gives plucked notes (the harp, and any pizz. articulation) the c12 step shape: full value on the attack, held to the next onset (at most 1.5 s), applied once per onset.

### Critic C (build/mix.json, tools/build_reaper.py)
- **C #1:** `side_shelf` {200 Hz, -2 dB} on Cb, Vc, Tuba, BTbn, Cbn and Timp (was -6). The harp shelves are unchanged.
- **C #2:** the Cb `loud_eq` low shelf is 100 Hz -6 dB (was 80 Hz -3). The wet points are [[190,0],[200,1],[214,1],[216,0],[254,0],[259,1],[269,1],[271,0]]. The 150 Hz +4 bell is kept.
- **C #3:** `loud_eq` may now be a list of specs, with one wet-automated ReaEQ per spec (`mute_lua`). The Cb has a second spec: a 90 Hz -5 dB low shelf, wet over qn 108-140.
- **C #4:** `side_shelf` may now be a list of ReaEQ bands (`side_lua` passes `{bands=...}`, and `set_side_shelf` takes `spec.bands`).
  - Every wind and brass track, plus Horns 1-2 a2: `[{"band": "highshelf", "hz": 250, "db": 1.5}]`.
  - Cbn, BTbn and Tuba: a low shelf at 200 Hz -2 plus the same high shelf.
  - Vln II div, Vla div and Vc div: high shelf 250 Hz +3.

## Rejected or deferred
- A #1b (`auto_notches.py`, a measured notch pass) and A #2b (an overshoot test on the 30 ms peak in `auto_fills.py`) are deferred. The hand entries cover the joins they listed. Both tools are worth building before the hand lists grow.
- Nothing was rejected.

## Measured (c20 -> c21)

| | c20 | c21 |
|---|---|---|
| Master integrated / LRA / TP | -22.6 LUFS / 23.6 LU / -3.8 dBFS | -22.5 LUFS / 23.6 LU / -3.9 dBFS |
| mp3 integrated / LRA / TP | -19.8 LUFS / 16.0 LU / -1.6 dBTP | -19.8 LUFS / 16.0 LU / -1.6 dBTP |
| mp3 span / limiter | 18.5 dB / 2.2 dB | 18.5 dB / 1.9 dB |

- **A #1/#2** (critic A's `spikescan.py 5`; scripts in `/private/tmp/claude-501/mockup-loop/c21-A/`, results in `c21-actor/spike2*.txt`):
  - Spiking joins went from 62 to 47.
  - Every listed join is now under the 5 dB threshold, except Vln I 72 (7.9 -> 5.9, master +4.1) and Ob1 145 (5.9 -> 5.8).
  - The Ob1 145 spike is at -0.17..-0.09 s, before the fill, so it comes from the transition sample. A notch is needed there, not a lower fill.
  - New spikes: Hn1 180 +5.0 (fill 4.2 plus the B #4 lift), Hn1 202 +5.4 (the auto_fills raise to 8.0 overshoots), Vln I 249.5 +5.2 and Vln II 83.
- **A #3:** Tbn1 218 peak -22.5 -> -20.8 dB. That is +3.2 over the 214.5-217.5 eighths (mean about -24.0), and 1.7 under the 213 accent. Target met.
- **B #1** (plain RMS):
  - Vc - Vln I per beat, qn 188-195: -7.5..+2.7 -> -4.8..+3.9. The Vc no longer falls under the line, but in plain RMS it is now level with Vln I from qn 190. This measure weights the Vc's low register; the critic's K-weighted target was 2-5 dB under.
  - Bn2 qn 193: -32.1 -> -37.3, now under its neighbours.
  - Master bar 56 -> 57: -28.6/-30.5 -> -28.1/-29.8. The step is still 1.7 dB, because bar 56 also rose (the B #4 horn lift).
- **B #2:** Fl1 - Vln I per 0.5 qn in bar 58: -5.6..+2.3 (median +1.2) -> -8.4..-0.5 (median -1.4).
- **B #3:** Fl1 short notes 110-117.67 rose 1.0-3.6 dB; the long notes rose 0.2-2.4.
- **B #4:** Horn 1 - Vln I per 2 qn, 176-188: -11.6..-0.1 -> -7.6..+2.2. Horn - harp: -5.0..+0.2 -> -1.0..+3.9.
- **B #5:** the harp qn 26 peak -38.2 -> -43.2, inside the harp's range (-42.7..-44.3). The horn is not covered.
- **C #1** (critic C's `bands.py`): master correlation at 25-60 / 60-120 / 120-250 Hz went from 0.90/0.88/0.71 to 0.71/0.75/0.56. Target met.
- **C #2** (`lowpow.py`, 60-100 Hz relative to 250 Hz-2 kHz): loudest 10% -13.4 -> -15.9 (target -15.5..-17.5); 100-250 Hz -6.5 -> -6.6 (limit -7.0); loud third 30-60 Hz -30.4 -> -32.1.
- **C #3:** master 60-100 Hz relative to 250 Hz-2 kHz over bars 37-44 went from -10.6 to -13.8. The Cb's 120-400 Hz band relative to 250 Hz-2 kHz changed by -0.3 dB. The soft third overall went -15.9 -> -18.5 at 60-100 Hz, because this window is part of it.
- **C #4:** master correlation at 250-500 Hz / 500 Hz-2 kHz / 2-6 kHz went from 0.63/0.62/0.51 to 0.56/0.56/0.50. Per stem at 500 Hz-2 kHz: Fl1 0.74 -> 0.66, Ob1 0.76 -> 0.67, Horn 1 0.67 -> 0.55, Vln II div 0.88 -> 0.77. R-L moved by 0.1-1.1 dB; Vln II div moved -0.9/-1.1, a little over the 0.7 limit.

## Open
- Hn1 202: lower the fill back to 6.5. Hn1 180: lower the fill 4.2 -> 2.5. Add notches for Ob1 145 and Vln I 249.5. Vln I 72 needs a wider or deeper notch.
- Bar 56 -> 57 still steps down 1.7 dB in RMS. Check it K-weighted before changing anything.
- The Vc in bars 57-58 may now be too loud (level with Vln I in RMS). Check it K-weighted.
- Build `auto_notches.py` (A #1b) and the 30 ms overshoot test in `auto_fills.py` (A #2b).
