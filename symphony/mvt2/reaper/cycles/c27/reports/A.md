# Cycle 27, critic A: articulation and phrasing (on the cycle 26 render)

Render under review: c26, with c25 and the first c26 render (`c26-actor/render1/`, before the post-render fills) as controls. Scripts are in `/private/tmp/claude-501/mockup-loop/c27-A/`: `rb.py`, `rbb.py`, `rbb2.py`, `rbb3.py`, `rbb4.py` (final-chord re-bows), `flux.py` (master onsets in the chord), `mbump.py` (scan of short master bumps), `spk.py` (spike windows), `tbn.py` (trombone speech), `uni.py`, `br.py`, `pizz.py`, `ends.py`, plus the c25/c26 critic-A kit copied into `kit/` (`spikescan.py`, `holes.py`, `tbn.py`). All qn values are on the parts.json timeline (moved onsets), which is the timeline `JOIN_NOTCH` uses.

Reproducibility: the Violins I/II, Violas and Violoncellos stems give the same spike numbers in c23, c24, c25 and c26 at every join I checked (to 0.1 dB, for example Vc 139.85, Vln I/II 72, 74, 172, 240, 252, 268). The c25 reset works, so the backlog of string notches deferred since c24 can now be fitted on one render.

## 1. Final chord (qn 289-304): every Sus MAX re-bow piece in Violins I, Violins II and Violas swells 4-6 dB about 2.4 s after it starts. Measured; cause inferred.

**What is wrong.** The c26 re-bows replaced the 4 s loop cycle, but the Sus MAX v41 sample has its own bump: a 100-180 ms swell, 2.3-2.5 s after each new piece starts. 13 of 16 upper-string pieces have it (stem excess over a ±0.25 s running median):

| track | re-bow | bump | at | master excess |
|---|---|---|---|---|
| Violins I | 295.0 | +5.3 | 2.50 s | +2.0 |
| Violins I | 298.0 | +3.9 | 1.91 s | +1.5 |
| Violins I | 301.0 | **+6.0** | 2.49 s | **+4.0** |
| Violins I | 302.75 | +4.4 | 2.60 s | +2.5 |
| Violins II | 293.0 / 297.6 / 302.2 | +5.7 / +5.9 / +5.8 | 2.35-2.38 s | +1.4 / 0.0 / 0.0 |
| Violas | 294.1 / 296.9 / 299.2 / 301.5 / 303.1 | +4.4 / +3.7 / +4.3 / +4.7 / +4.0 | 1.95-2.42 s | +0.7 / +1.2 / +1.3 / 0.0 / +0.2 |

**Evidence.**
- The first c26 render (no re-bow fills) shows the same bumps at the same times and sizes (Vln I 301 +6.0 at 2.49 s; Vla 299.2 +4.3 at 2.42 s). So they come from the sample, not from `rebow_fills.json`.
- c25 held one sample per section. Its bumps fall at no fixed offset (Vln I at 0.97 / 3.45 / 3.37 s), as expected for a loop.
- Celli and basses re-bow pieces stay under 2.5 dB. Sus MAX notes of 3 s or more elsewhere in the piece (Cb 22 notes, Hn4 12, Bn2 15) show no 2.4 s bump. The bump belongs to the upper-string Sus MAX at pp.
- My scan of the whole master for short bumps (3.5 dB or more, 200 ms or less, away from percussive onsets) finds one in the final chord: qn 302.52, +4.2 dB at -42 dB. That is the Vln I 301 piece. In the quietest held chord of the piece, a 100 ms rise of 4 dB reads as a blip in the morendo, in the passage Dan flagged (inferred).
- The re-bows themselves are clean on the master. Spectral-flux onsets at the 27 re-bow times have a median z of 2.8, against 3.1 at the same times in c25 with no re-bows. Keep them.

**Fix (`tools/score_to_parts.py` `JOIN_NOTCH`; level only, `--midi-only`).** These windows are measured from the stems (qn, parts.json timeline), and each depth is the bump minus 1.5 dB:
- Violins I: (296.80, 296.90, -3.8), (299.27, 299.39, -2.4), (302.46, 302.55, -4.5), (303.70, 303.74, -2.9).
- Violins II: (292.68, 292.81, -2.6), (294.81, 294.94, -4.2), (299.18, 299.29, -4.4), (303.31, 303.36, -4.3).
- Violas: (295.89, 296.01, -2.9), (298.48, 298.57, -2.2), (300.74, 300.82, -2.8), (302.81, 302.92, -3.2), (303.72, 303.77, -2.5).

The JOIN_NOTCH ramps are 0.04 qn. That is about 70 ms at 1.7 s/qn and 120 ms in the fermata bar (3 s/qn), wider than these bumps. Give the tuple an optional fourth value for the ramp (0.015 qn for these entries) in the loop at line 2517.

Alternative (inferred, test only if the notches leave a bump): the c26 critic's deferred CC1 56 from 292 on Vln I/II/Vla. That plays Sus Vib alone instead of Non Vib + Sus Vib. If the bump is one layer leaving its attack, it would go, but the chord would get more vibrato than a niente ending wants.

Checks with `rbb.py` and `mbump.py`:
- Every upper-string piece's bump under 2.5 dB on its stem.
- No master bump of 3 dB or more in 292-304.
- Flux z at the re-bows unchanged.
- `rebow_fills.json` untouched (the notches add on top of it).

## 2. Bars 44-45, Violoncellos into qn 140, and Oboe 1 into 146: a note-trim release ramps up into the legato transition. The loudest short bumps on the master. Measured.

**Where and what.**
- **Vc 139 -> 140** (A flat 3 -> D flat 4, Leg Slur MAX v124, p, the start of the oboe-cello duet):
  - The Vc stem rises +7.9 dB over 139.75-139.90 (230 ms). The master rises +7.0 dB over 210 ms at -38.8 dB.
  - The values are identical in c23, c24, c25 and c26.
  - Of the 41 bumps my scan finds on the master, this is the largest.
- **Ob1 145.5 -> 146** (dolce espr., p): the Ob1 stem is +8.1 dB over 145.86-146.01 and the master +5.6 dB over 150 ms.

**Cause (measured in parts.json).**
- `note_trims.json` Violoncellos "139": -6 releases as a ramp in vol_db, from -6.0 at 139.514 to 0.0 at 139.874. It lifts the end of the A flat 3 by 6 dB just as the transition burst begins (moved onset 139.844).
- After that, the early fill (+4.3) steps in at 140.0.
- Ob1: the "145.5": +3 trim ramps up to +4.33 at 145.889, under the 146 transition burst.

**Fix.**
- `JOIN_NOTCH` Violoncellos (139.74, 139.91, -6.0) and Oboe 1 (145.86, 146.01, -5.5).
- If the Vc note still swells after the notch, end the 139 trim with a 0.05 qn release that finishes at 139.84, instead of the ramp from 139.51. The trim was there for the A flat 3's body (measured as the note's own level, not the join).
- Check: master bump at 139.85 under +2.5 dB and at 145.94 under +2.5 dB, with no new trough deeper than 4 dB on either stem.

## 3. Bar 29 (qn 86) and bar 28 (qn 82): Violins I and II unison joins tick on the master. Measured.

**qn 86.0** (descending eighths into C5, Leg Slur MAX v124):
- **Two bursts.**
  - Both sections' transition samples peak at 85.87-85.92: Vln II +6.0 dB over 85.854-85.932, Vln I about +5.
  - About 20 ms later, Vln I steps again: +6.8 dB at 86.018, over 86.001-86.062. That second step is `early_fills.json` Violins I "86" (db 4, pre_s 0, hold 0.35). vol_db goes from -2.61 at 85.98 to +1.22 at 86.00, which is +3.8 dB in about 23 ms, and it lands right after the burst it was meant to support.
- **Master:** +5.7 dB for 80 ms at -29 dB. Spikescan reports +8.8 for this join (c25: +7.7).

**qn 82.0** (the Leg Port MAX targets, both sections): Vln I +6.0 at 82.305 and Vln II +6.1 at 82.322 land in the same 20 ms, so the master gets the sum, +4.7 dB for 40 ms.

**Fix.**
- `early_fills.json` Violins I "86": db 4 -> 1.5, pre_s 0 -> 0.03, so it rises before the burst instead of after it.
- `JOIN_NOTCH`:
  - Violins II (85.85, 85.93, -4.0) and Violins I (85.86, 85.92, -3.0).
  - Violins I (82.28, 82.33, -4.0) and Violins II (82.30, 82.34, -4.0). The existing 86.38-86.51 entries stay.
- Check: master bumps at 85.9 and 82.31 under +2.5 dB, and no 86 dip deeper than the c24 notched joins (4 dB).

## 4. Trombone 1, bars 63-64: after the c26 fix the accents no longer bite, and the ff marcato pickup speaks late. Measured (c26 vs c25); the musical judgement is inferred.

**What.** The c26 change removed the 2-5 kHz burst, as Dan asked. But the ff marcato eighth at 212.5, the exposed entry of the movement I call-back after the strings' sf, now swells in instead of speaking:

| qn | articulation | first 60 ms vs body | -3 dB point after the score onset | 2-5 kHz attack minus body |
|---|---|---|---|---|
| 212.5, c25 | Sus Accent MAX v108 | +1.3 dB | +16 ms | +6.9 (c26 actor's figure) |
| **212.5, c26** | **Sus MAX v96** | **-9.8 dB** | **+96 ms** (body -1 dB at +150 ms) | -0.8 |
| 218, c26 | Sus MAX v92 | -6.0 dB | +67 ms | -9.4 |
| 214.5-217.5 | Marc Lng RRx4, v94-106 | -0.2 .. -5.2 dB | +16 .. +85 ms (median about +25) | -6.3 .. +4.1 |

The eighth lasts 0.57 s, so its first 100 ms is a soft, late front on a note printed ff with an accent. 218 also takes 67 ms to reach -3 dB and is now darker at the attack than in its body (-9.4 dB): no weight on the front at all.

The Marc Lng eighths of the same line show that a firm front without a 2-5 kHz burst is possible on this patch. They speak in 16-85 ms with a 2-5 kHz tilt of -6..+4 dB (c26 critic A: "clean").

**Fix (Marc Lng RRx4 is already loaded on Trombone 1, so `--midi-only`):**
- `ACCENT_ART_AT` Trombone 1 212.5: "Sus MAX" -> "Marc Lng RRx4" (an accented eighth inside the printed marcato line). `VEL_SET` 212.5: 96 -> 104, one step under the line's first eighth (106). `ACCENT_SWELL_S_AT` 212.5 swell 4.5 -> 2.5 dB, because the Marc Lng body is level with the eighths.
- 218: keep Sus MAX, v92 and the swell. Add `build/entry_leads.json` "Trombone 1": {"218.0": 0.05}, so the -3 dB point falls at about +20 ms. The 217.5 eighth ends at 217.875, which leaves room.
- 213 is unchanged. It starts from 212.5's release, at -3 dB 50 ms before its onset.
- Checks with `tbn.py`:
  - 212.5 first 60 ms within -4 dB of body, -3 dB point within +40 ms, 2-5 kHz attack minus body at most +4 dB, master 2-5 kHz jump under +3 dB.
  - 218 -3 dB point within +30 ms.
  - Bodies 2-4 dB over the eighths, as the c26 checks required.

## 5. The remaining legato-transition spikes are now stable from render to render: notch the string backlog. Measured.

Stem spike windows (excess over the window median, 10 ms frames), identical in c25 and c26. The master figure is the rise at the peak:

| join (score qn) | Vln I | Vln II | Vc | master |
|---|---|---|---|---|
| 72 | +5.3 over 72.13-72.22 | +4.6 over 71.97-72.11 | | +2.5 |
| 74 | +4.6 over 74.16-74.26 | +4.4 over 73.85-73.91 | | +3.8 |
| 172 | +6.0 over 171.90-171.99 | +5.9 over 171.81-171.86 | +5.4 over 171.81-172.01 | +3.7 |
| 174 | | | +7.2 over 173.82-173.95 | +3.8 |
| 240 | +6.3 over 239.98-240.03 (fill db 4 at 240) | +6.3 over 239.66-239.84 | | +1.9 |
| 252 | +7.0 over 251.88-251.95 | +8.6 over 251.64-251.92 | | +3.0 |

- The existing Vln I notch (71.90, 72.08, -4.5) now misses its spike, which sits 0.05-0.14 qn later.
- In every unison join above, Vln II's burst comes 0.10-0.31 qn before Vln I's. Vln II has a 0.20 s lead against Vln I's 0.17 s, and its transitions are faster. A unison melody gets two small ticks instead of one.

**Fix: `JOIN_NOTCH` (depth = spike - 2, cap 6, the c21 rule):**
- Violins I: (72.12, 72.22, -3.3), (74.15, 74.26, -2.6), (171.90, 171.99, -4.0), (239.97, 240.03, -4.3), (251.88, 251.95, -5.0). Replace (71.90, 72.08, -4.5) with the 72 entry.
- Violins II: (71.97, 72.11, -2.6), (73.85, 73.91, -2.4), (171.81, 171.86, -3.9), (239.66, 239.84, -4.3), (251.64, 251.92, -6.0).
- Violoncellos: (171.81, 172.01, -3.4), (173.82, 173.95, -5.2).
- Lower `early_fills.json` Violins I "240" from 4.0 to 2.0 before adding its notch, because the fill sits on the spike.

Check with `kit/spikescan.py 5` (c26: 36 of 606 joins at +5 or more). The listed joins should be under +3 on the stems and under +2 on the master, and `holes.py` should not report a new hole of 6 dB or more at these joins (c26: 111 joins at 6 dB or more, c25: 110).

## Also checked, no finding

- **Chords on monophonic legato patches:** none. The Tbn1 marcato eighths, Vla tremolo double stops (Tremolo patch, polyphonic) and Vln I div. tremolo are on non-legato rows.
- **Breath marks:** all 29 breath marks leave a gap of 0.09-0.42 s that dips the stem 10-25 dB (the median is about 15). They read as breaths.
- **Pizzicato lengths:** Cb/Vc quarter-note pizz. cut at the note-off are already 15-27 dB under the peak by then. The 2-qn pizz. notes decay the same way (Cb 120: -27 dB at 1.1 s), so the note-off removes nothing audible. Violas pizz. triplets at 124-138 spread 6.6 dB p10-p90, with no pitch or beat pattern.
- **Timpani:** the tied roll at 210 ends on a Flt Lng stroke at 211, 3.6 dB over the roll and inside the ff tutti. Roll and stroke assignment matches the score everywhere.
- **Unison crossovers, Vln I vs Vln II (39 joins):** median difference -0.020 s. 10 joins differ by more than 0.06 s, the largest 0.145 s at 178. This is minor; the bursts in finding 5 matter more than the crossovers.

Do not touch:
- The `REBOW_AT` points and `rebow_fills.json` (no master onsets at the re-bows; the bump in finding 1 is the sample's, so notch it on top).
- The Marc Lng eighths and `MARCATO_SPANS` / `MARC_ATTACK_S`. Finding 4 copies them for 212.5.
- The Tbn1 no-bump CC11 (`ACCENT_BUMP_AT` 0).
- `BC_SOFT` and the legato lead tables.
- The c23 breath gaps.
- The pre-roll CC36/CC69 reset. It is what makes these notches safe to fit.
