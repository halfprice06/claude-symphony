# Cycle 20, critic A: articulation and phrasing (on the cycle 19 render)

Scripts are in `/private/tmp/claude-501/mockup-loop/c20-A/`: the c19-A set, plus `xover.py` and `xover2.py` (pitch-change crossover), `rise.py`, `cbv.py`, `seams.py` (single loop-seam dips), `entries.py`, `trem.py`, `wam.py` and `bnhole.py`. Run them with `CYC=19 ~/.venvs/claude-composes-reaper/bin/python`. Levels are stereo power. Times are measured from the score onset (`sq`).

## Checked and working (measured, c19)

- **Chords, ties, slurs, keyswitches.**
  - No chord goes to a legato patch.
  - All 104 ties are held. The only re-attacks are the timpani tie strokes at 203 and 211.
  - Every keyswitch is at least 20 ms ahead of its note, except the known Ob1 207.952 (13 ms).
  - CC15 matches every printed con/senza sord., including Vln I "gli altri con sord." at 65.
- **Pitch-change timing on every legato line** (crossover of the new pitch's partials over the old one's, `xover2.py`, 8192-point window, harmonics 2-8):
  - Vln I, Vln II, Vla, Vc: median +0.00 to +0.03 s.
  - Solo violin, Vc div, Vla div, a2 horns: -0.00 to +0.04 s.
  - Winds and horns on legato: +0.02 to +0.06 s.
  - Wind and horn Sus re-attacks: +0.07 to +0.08 s.
  - Cbn +0.05 s, Tuba +0.08 s, BTbn +0.05 s.
- **Pizzicato and harp onsets.** Vc, Cb and Vla pizz. land within +-0.01 s of the score (median). Harp minus Vc pizz. is +0.00 s.
- **Breaths.** Every printed breath dips 9.6-34 dB.
- **Legato joins.** Every track's median join dip is 0.9-3.7 dB. Only Ob1 142.5/143, Vln I 67.5 and Vc 240 reach 8 dB or more after the envelope, and the routine `auto_fills` rerun covers them. Vc 124 is a false positive: its previous note is pizz.
- **Bn1 abut lead (c19 C #6), same metric on c18 and c19:**
  - It works: the crossovers at 27/35/36/38 went from +0.05/+0.12/+0.15/+0.13 s to -0.04/-0.01/-0.02/+0.01 s.
  - The dips did not deepen: 36 went from 7.5 to 7.4 dB and 38 from 4.5 to 5.0 dB (`bnhole.py`, 50 ms smoothing).
  - The "8.1 -> 11.5" in CHANGES.md is not confirmed. Keep the entry as it is.
- **Tremolo (bars 61-64).** It sounds, with an 8-30 Hz modulation share of 0.5-0.7 on Tremolo against 0.36-0.49 on the legato before it. No finding.

## 1. The double basses reach every new pitch about 0.2 s after the celli. They play on Sus MAX with no lead, and the old note rings into the new one. Measured.

**Where:** every arco Cb pitch change: bars 22-30, 49-60, 61-62 (Largamente), 64-65, 72-82 and 87-89. 65 changes were measured.

**Evidence** (`xover2.py "Violoncellos,Double basses" 8192 -v`):

| | median | p25 | p75 |
|---|---|---|---|
| Cb crossover | +0.200 s | +0.100 | +0.270 |
| Vc crossover (same tool, control) | -0.000 s | -0.023 | +0.050 |
| Cb - Vc, 46 shared changes | +0.165 s | +0.100 | +0.277 |

- Cb is behind the celli at 42 of the 46 shared changes. Examples:
  - 63 +0.37, 84 +0.35, 160 +0.32, 172 +0.47, 176 +0.36.
  - 196 +0.39, 200 +0.32, 208 +0.20 (bar 62 ff), 241 +0.30, 256 +0.34.
- With a 4096 window and harmonics 1-4, the lag is the same or larger: +0.27 s median. It does not depend on dynamics (CC11 0-60: +0.265; 60-85: +0.280; 85+: +0.270) or on velocity (r = -0.09).
- Every other non-legato part is at +0.05 to +0.08 s, so this is not how Sus MAX behaves in general.
- Cause:
  - parts.json starts all 77 arco notes on the score onset (lead 0.000). The previous note ends at the same instant.
  - The old pitch's partials take a median +0.46 s to fall 10 dB (`rise.py`). The celli's old pitch takes +0.12 s.
  - At ♩ = 52-60, a quarter-note bass line (bars 72-73, qn 241-247) spends a quarter of each beat on the old harmony.
- Why the c19 measurement was noisy: below about 100 Hz a ±2% band around harmonics 1-4 holds 0-1 FFT bins at 4096 points. Using harmonics 2-8 with at least ±1 bin at 8192 points brings the Vc control down to a p25-p75 spread of 0.07 s.
- The same mechanism already works on Bn1: lead 0.10 s, crossover 0.09-0.16 s earlier, no deeper dips. See "Checked" above.

**Fix:**
1. Add a Double basses entry to `ABUT_LEAD` in `tools/score_to_parts.py`:

   ```python
   ABUT_LEAD = {"Bassoon 1": {"lead_s": 0.10, "max_cc": 50, "overlap_qn": 0.0, "at": [27.0, 35.0, 36.0, 38.0]},
                "Double basses": {"lead_s": 0.16, "max_cc": 127, "overlap_qn": 0.0, "skip_next_same": True}}
   ```

   - There is no `at` list: every arco Sus note that abuts a note of another pitch is led.
   - Pizz. notes are already excluded by the `n["art"].startswith("Sus")` test.
2. In the abut branch of `build_track` (the `elif abut_ and n["art"].startswith("Sus") ...` condition, around line 1652), add this guard against the c15 failure (holes on same-pitch repeats after a led note):

   ```python
   and not (abut_.get("skip_next_same") and any(o["qn"] > q + EPS and abs(o["qn"] - orig_end[id(n)]) < 0.05
                                                and o["pitch"] == n["pitch"] for o in ns))
   ```

   - This skips Cb 252 (followed by 253 at the same pitch) and 262 (followed by 265).
   - The existing previous-same-pitch test already skips 253 and 265.
3. Run `--midi-only`. No state change is needed.

The note-on and the old note-off move together, so the shape of each change is unchanged; only its timing moves. No new hole is expected (inferred).

**Check:**
- Rerun `xover2.py "Violoncellos,Double basses" 8192`. Cb median at most +0.06 s; Cb - Vc median at most +0.05 s.
- `rebow.py`: no new Double basses trough of 6 dB or more. c19 has 84, 144, 152, 168, 174, 190, 216, 247 and 252.
- If it fails, set the Cb entry's `lead_s` to 0.08.

## 2. Single loop-seam dips of 8-11 dB in medium-length string notes that the c17 loop profiles do not cover. Measured in the stems. Mostly masked in the master.

**Where and how much** (`seams.py`, vol_db removed, 1.2 s running-median detrend):
- The dips are the same in c18 and c19 to 0.1 dB and 0.01 s, so they come from the samples.
- `t` is seconds after the note's moved start, which is the same base `loop_fills` uses.

| Track, note | t (s) | dip | width (s) | stem - master | master dip |
|---|---|---|---|---|---|
| Double basses 168 (bar 52, p) | 4.04 | 11.1 | 0.18 | -5.8 | none |
| Double basses 204 (bar 61, ff) | 3.58 | 9.7 | 0.23 | -9.4 | 1.9 |
| Violins II 108 (bar 37, pp sul tasto) | 4.40 | 9.2 | 0.14 | -4.6 | none |
| Violins II 116 (bar 39, pp sul tasto) | 4.40 | 8.7 | 0.14 | -4.1 | up to 5.4 (coincides with a gap in the pizz./harp) |
| Double basses 3 (bar 2, opening chord) | 5.99 / 6.49 | 9.5 / 7.7 | 0.14 / 0.18 | -10 | none |
| Violoncellos 3 (opening chord) | 2.77 / 5.59 / 6.71 | 7.2 / 7.1 / 8.4 | 0.25 / 0.16 / 0.16 | -8 | up to 2.3 at 5.59 |
| Violoncellos 63 (bar 22) | 4.20 | 8.0 | 0.13 | -4.2 | 1.9 |
| Violas div 87 (bar 30, p > pp) | 1.77 / 3.00 | 8.4 / 7.9 | 0.20 / 0.20 | -8 | 1.6 / 1.2 |

- The notes under `build/loop_profiles.json` now show no seam over 6 dB after the envelope.
- Exposure:
  - The sul tasto pad (bars 37-40) is exposed under the flute solo, so it is the most audible case.
  - The opening chord is the first thing heard.
  - The others sit 6-10 dB under the master, so they mostly read as a brief loss of bass weight (inferred).

**Fix:** add `build/loop_fills.json` entries, `[t_s, dB, width_s]`, using the file's own rule (dB = 80% of the dip, cap 6; width = the measured width):

```json
"Double basses": {"3": [[5.99, 6, 0.14], [6.49, 6, 0.18]], "168": [[4.04, 6, 0.18]], "204": [[3.58, 6, 0.23]]},
"Violins II": {"108": [[4.40, 6, 0.14]], "116": [[4.40, 6, 0.14]]},
"Violoncellos": {"3": [[2.77, 5.8, 0.25], [5.59, 5.7, 0.16], [6.71, 6, 0.16]], "63": [[4.20, 6, 0.13]]},
"Violas div": {"87": [[1.77, 6, 0.20], [3.00, 6, 0.20]]}
```

- Keep the existing Horn 1 34 entry.
- These are single raised-cosine lifts of the kind that worked for Horn 1 qn 34 in c18. They are not periodic profiles.
- If the Double basses get the #1 lead, their moved starts shift by 0.16 s and the seams shift with them. `t` is measured from the moved start, so the values stay valid.

**Check:** `seams.py <track> -post` on c20 shows each listed dip at 4 dB or less, with no bump over +2.5 dB.

## Not findings, checked

- **Legato transition speed.** Strings and horns play legato targets at velocity 124, the shortest transition (HO manual, p. 91: 50-60 gives a longer, "breathing" transition). A slower setting on the slow espressivo lines might sound more vocal. That is inferred only, and it would undo the lead tables measured since c03, so I do not propose it without a range test.
- **Wind vibrato in bars 61-62.**
  - The 4-8 Hz modulation is 10.2 dB peak-to-peak on Ob1 at 210-212 and 11.2 dB on Fl2 at 204-208.
  - Vibrato was closed in c18 after the `WIND_VIB_CAP` test made the flute worse. Not reopened.
- **Bass trombone on the tenor trombone patch.** The 1TB Sus MAX lowest region is 36-40, so the D2 notes are stretched by at most 2 semitones. The exposed BTbn notes in bar 63 change pitch on time (+0.05 s). No patch change.
- **Soft string entries** (Vla 42, Vln II 108, Vla 66). They take 0.3-0.5 s to reach body - 6 dB, but they start at -55..-78 dB at the onset. This is the printed pp/crescendo shape, not lateness.

**Do not touch:**
- **Leads and joins.**
  - The `ABUT_LEAD` Bassoon 1 entry (measured to work).
  - `LEG_CAP_FRAC`, the c19 leg_leads and pair leads.
  - `slur_out`, `BC_SOFT`/`BC_SOFT_SKIP`, `SOST_HOLD_THROUGH`, `JOIN_NOTCH`.
- **Loop seams.** The loop profiles. Their notes show no seam over 6 dB.
- **Ties, keyswitches, mutes.** Tie handling, keyswitch placement, CC15/`mute_eq`.
- **Pizzicato, harp, timpani.** Pizz. timing and steps, the harp rolls, the timpani tie strokes.
- **Breaths.** The caesura breaths.
