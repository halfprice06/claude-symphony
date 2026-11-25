# Cycle 54, critic A: articulation and phrasing (render of cycle 53)

Data used: `cycles/c53/render/` (delivered stems, with the stem fix), `cycles/c53/render_first/` (as rendered),
`cycles/c53/build_fix/parts.json` (delivered rows) and `cycles/c53/rendered_build/`; comparisons against
`cycles/c51/render` and `cycles/c52/render` with their own `rendered_build`. S is `tools/pcx.py s_start` as
`tools/s_onsets.py` calls it (values below are S / pcX / crossover in ms). Scratch scripts are left in
`/private/tmp/claude-501/mockup-loop/mvt2-c54-A/` (40 kB, no audio; not deleted, by the lead's rule).
All simulations are level-only gains on the delivered stem, master = rendered master + stem difference.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 54, so no page range was read in full. Points used from
`loop/MANUAL-GAPS.md` and the digest:

| What the manual says | Where it applies | Does the render follow it |
|---|---|---|
| Woodwind "Legato Slur Repetitions": same-pitch notes played without space use a re-tongued sample instead of a slur (2021 manual p.112; MANUAL-GAPS item 2) | Clarinet 1 qn 289, a tenuto repeat inside a slur | No. The repeat is a note-off gap (81 ms of silence) on Sus Non Vib; finding 1 |
| String legato: velocity sets the transition timing; joins up to an octave (p.99) | Violins II 152 -> 154, an octave join at velocity 124 | The join plays, but the octave transition is slow at pp; finding 3 |
| String legato transitions only with no gap between notes; monophonic (p.99) | The four "start sag" notes: all four are overlapped joins on Leg Slur MAX, though the score starts a new bow on each | Followed as data; the slur row has no bow-change swell, which is the "sag" against c51's Leg BC MAX; finding 2 |

## Findings, ranked

### 1. Clarinet 1, bar 88 (qn 289): the slurred tenuto repeat is a 7.5 dB hole in the master, deeper than the printed breath before it (measured)

The score slurs Clarinet 1's D flat 5 at 286 to the D flat 5 at 289 and marks 289 tenuto: a soft re-articulation with
no break. The breath is printed at 286, not at 289. Rendered: the 286 note ends 81 ms before 289 and the clarinet
stem falls from -43 to -52 dB (9 dB) for about 100 ms. Clarinet 1 is the loudest stem there (-43 dB; the next is
Violoncellos at -49), and Horn 3 (-8 dB), Violins II (-5 dB) and Violas div re-attack at the same moment, so the
master falls from -41.5 to -49 dB (7.5 dB) between -75 and +25 ms around the beat (25 ms steps). At the printed
breath at 286 the master dips 2.8 dB (`check46_c53_fix.txt`). The wind stems ring little (t20 0.28 s, 16-20 dB down
0.3 s after a stop, `check52_c53_fix.txt`), so nothing fills the gap. `s1_c53_fix.txt` lists this point with a master
dip of 8.2 dB; c45 reduced Horn 3's part in it (`WIND_REP_RETONGUE_AT`), but the clarinet's gap, which sets the
master, was not changed.

Fix (`build/score_config.py`): `WIND_REP_RETONGUE_AT["Clarinet 1"] = {289.0: {"gap_s": 0.03, "fall_cc": 3}}`
(now the default 0.06 s and 6). Accept when the clarinet's own-band dip is 4-6 dB (S1 still needs 3 dB or more) and
the master dip at 289 is 4 dB or less (the limit already used at 204). If the dip stays over 6 dB at a 30 ms gap, the
second step is the Clarinet KS Master's "Leg Slur Rep" row for 286-289 (manual p.112; it is in `ks_maps.json`; the
track's row set changes, so it is a full rebuild of Clarinet 1). The expected master value is inferred, not simulated.

### 2. Start sags on Violoncellos 253 and Violins I 80: a lift that is level from the beat to +0.45 s does not move S (measured by simulation)

Why the c53 shapes moved S: pcX takes its reference from the highest 30 ms level between the note-on and +0.45 s.
A shape that keeps rising after the beat raises that reference against the attack, so the reading goes late. A lift
that is fully up at the beat and stays at one level until +0.45 s raises attack and reference by the same amount.
After +0.45 s the shape is free. The reading is a threshold: on Violoncellos 253 a rise of 2 dB inside the window
leaves S at -4 ms, a rise of 3 dB makes pcX read +73 ms (the note itself is unchanged), so the rise inside the
window must stay at 2 dB or less.

Both notes are new bows in the score (253 starts a slur after the 250-252 slur; Violins I 80 follows the slur that
ends on 79.5 and is the tied arrival at the top of the crescendo to f at 82), and both are played as overlapped joins
on Leg Slur MAX.

- **Violoncellos 253** (A flat 3, counter-melody bar 76). Delivered: S -14 / -14 / +72; stem under c51 by
  1.7 / 2.0 / 5.1 / 8.3 / 8.5 / 8.1 / 5.2 dB in 100 ms steps from the beat; master under c51 by up to 3.0 dB at
  +0.3 to +0.5 s. In c53 the note is level at the previous note's tail (-39.5 dB) and then dips to -46.4 dB at
  +0.5 s; c51's bow-change row swelled to -32 dB at +0.3 s. Shape in seconds from the score onset:
  `[[-0.06, 0], [0, 5], [0.10, 5], [0.30, 7], [0.45, 7], [0.55, 8], [0.65, 8], [0.90, 0]]`.
  Simulated: S -4 / -4 / +72 (previous join unchanged at +4), stem -34.9 / -33.8 / -33.0 / -33.3 / -35.3 / -38.5 dB,
  master against c51 +0.6 / +0.3 / +0.2 / -1.2 / -1.9 / -0.4 dB (worst step 3.0 -> 1.9 dB). A fully level
  `[[-0.06, 0], [0, 4.5], [0.50, 4.5], [0.80, 0]]` reads S -11 and leaves the master 2.5 dB under.
- **Violins I 80** (F6). Delivered: S -5 / -5 / +34; stem 2.6-4.1 dB under c51 from +0.1 to +0.6 s. The line has the
  eighth C6 before it at -31.3 dB (200 ms before the beat, 7.5 dB over c51), then -39.9 dB on the beat, then a
  slow rise to -32 dB at +0.6 s: the arrival is the weakest point of the bar. Shape:
  `[[-0.30, 0], [-0.26, -3], [-0.13, -3], [-0.06, 0], [0, 3], [0.50, 3], [0.80, 0]]` (a 3 dB notch on the C6's peak and
  a level +3 dB lift). Simulated: S +1 / +1 / +34, the C6 at 79.5 reads -1 (was 0); stem -36.9 / -34.1 / -36.4 |
  -36.9 / -34.4 / -32.5 / -32.3 / -31.7 dB (100 ms steps from -0.3 s), so the dip on the beat is 2.8 dB, was 8.6;
  master against c51 within -0.5 / +1.1 dB.

Where: `build/level_fits.json`, rows "253.000" under Violoncellos and "80.000" under Violins I (merge with any body
row as `start53.py --fit` does). Generic rule for the actor's fitter (`cycles/c53/actor_scripts/start53.py`): a
start shape is at its first level on the beat, changes by at most 2 dB up to +0.45 s, and carries the rest of the
deficit after +0.45 s. Check with `tools/s_onsets.py`; accept at 25 ms or less of S movement.

Velocity is not a cure: all four notes are at velocity 124 already, and on the legato rows velocity sets the
transition timing, not the level (p.99). Going back to Leg BC MAX for single notes brings back the row changes inside
a line that c52 removed for steady rhythm; the level shape costs nothing in timing.

### 3. Violins II 154 arrives late and pcX cannot see it; Violins II 146 does not reach the master (measured)

- **154** (F sharp 4 -> F sharp 5, the only octave join in the movement besides Violas 195). Every harmonic of the
  new pitch is a harmonic of the old one, so the band pcX measures before the note is the old note (-20 dB re the
  body from -300 ms on) and the reading of -1 ms is not a reading of the new note. The crossover reads +396 ms
  (c51: +146). The old note's odd harmonics, which only the old pitch has, fall 6 dB below their level at about
  +135 ms (c51: +65 ms), and the stem has a hole from +0.1 to +0.5 s (-52.7 / -56.9 / -53.5 / -53.7 dB against
  -49.5 before and -48 after). The c53 start shape did not make this note late: it raised the reference above the old
  note's leakage, and pcX then read the real rise (+135 ms). So the open item is a lead, not a shape.
  Fix: `build/leg_leads.json` "Violins II" 154: +0.12 s (played lead 160 -> 280 ms), then the level lift
  `[[-0.06, 0], [0, 4], [0.50, 4], [0.80, 0]]` in `build/level_fits.json`. Judge it by the old pitch's odd-harmonic
  band (`pcx.band_env(x, t0, t1, 66, 78)`) falling 6 dB within 40 ms of the beat and by the crossover, not by S.
  The note is pp and 10-12 dB under the master (master against c51 0.5-0.9 dB down), so the gain is small; it is
  worth one row because the fault is a late note, which is Dan's S2.
  Tool note for `tools/s_onsets.py`: when the interval is 12 or 24 semitones, report the crossover and the old
  pitch's fall, and mark pcX as not valid.
- **146** (F4 -> G flat 4, pp accompaniment). Stem 3-7 dB under c51 from +0.1 to +0.5 s, but the stem is 16-23 dB
  under the master there; the master differs from c51 by -1.9 to +2.4 dB with no pattern and moves by 0.3 dB or less
  per step under any simulated shape. Close this item without a shape. If the lead wants the stem matched anyway,
  `[[-0.12, 0], [-0.06, 4.5], [0.50, 4.5], [0.80, 0]]` reads S -2 / -2 / +55 (delivered -1 / -1 / +55).

### 4. Violoncellos 68 is early in c52 and c53 alike; Violoncellos 77 is an effect of the measure (measured)

- **68** (E flat 3 -> A flat 3, a new bow: the slur starts on 68). The new pitch's band before the beat is the same
  in c52 and c53 within 2 dB at every 30 ms step from -400 to +200 ms: it appears 220 ms before the beat (-14 dB re
  its body), is at -10 dB at -84 ms and at half amplitude at -46 ms. What changed is the reference. In c52 the
  transition peak into 68.5 (13 dB over the body, at +0.23 to +0.38 s) was the highest level inside pcX's window, so
  pcX read +261 ms and S fell back to the crossover (+38). With the peak notched, the reference is the note's body and
  pcX reads -65. The crossover moved from +38 to -8 ms because the new band is 2 dB higher around the beat while
  both bands run almost level there (the old note is a release tail falling 10 dB in 250 ms): it is not a firm
  reading at this join. So: the note is 45-65 ms early, and it was in c52 too.
  Fix: the note-on is 350 ms before the beat, the clamp's maximum. `build/leg_leads.json` "Violoncellos" 68:
  -0.05 s (played lead 350 -> 300 ms); move the early fill with it. Expected pcX about -15 ms (inferred: a shift of
  the note-on shifts the rise).
- **77** (A flat 3 -> G3 under a printed crescendo). The new pitch sits 11-15 dB under its later level from -100 to
  +200 ms and then grows with the crescendo, so pcX's thresholds (reference -10 dB and half amplitude) lie on a
  level stretch: c53 is 3 dB higher than c52 from -130 to -40 ms (the notch shape before it ends there) and h10
  moved from -14 to -90 ms, t50 from +98 to -8 ms. The crossover is -4 ms in c52 and -2 ms in c53. No change to the
  note. Tool note: where the new band changes by less than 6 dB over the 100 ms around the t50 crossing, report the
  crossover and flag pcX.

### 5. Horn 2 208 re-attack: not audible in the master; close the item (measured)

Horn 2's stem dips from -27 to -36 dB at -20 ms and is back at -30 dB at +80 ms. In the
band of its D flat 4 harmonics the master reads 43-45 dB (arbitrary reference) through the re-attack, and the master
with the Horn 2 stem subtracted reads 41-45 dB: Horn 2 is 8-17 dB under the other parts in its own band (Violas,
Bassoon 1 and Violoncellos hold the same D flat 4; the timpani strike D flat at 208), and removing it changes the
master's band level by 1 dB or less at every 20 ms step. No lead or gap value will be heard. Keep the c53 values
(`REP_GAP_AT` 0.12 s, `REATTACK_LEAD_AT` 0.04) and take it off the open list.

### 6. Bars 89-92: master dips of 2.4-3.8 dB that are not re-bows (measured; cause inferred)

100 ms windows against a 1.2 s median, qn 291-304: nine master dips of 2.0-3.8 dB. Three (qn 293.15, 293.83,
294.42; 3.8 / 3.1 / 2.6 dB, 125-350 ms long) have no stem dipping by more than 1.3 dB. Clarinet 1 (tied C5, -43.5 dB)
and Violins I (C5 con sord., -46 dB) hold the same pitch at near-equal level there, so the inferred cause is the two
sources cancelling in part. At qn 297.90 the master dips 3.6 dB with the Violoncellos, the loudest stem, 5.1 dB down
for 75 ms (their re-bows are at 296.3 and 298.6, so this is not a re-bow). No fix proposed without a test: the
actor can confirm the first three by measuring the master with the Clarinet 1 stem subtracted; if they go, 2 dB off
Violins I's level over 292-295 (a volume-envelope row, not CC11) is the smallest change. The per-stem re-bow check
(`rebow_c53_fix.txt`, 17 of 37 over 3 dB) overstates the final chord: on the sum of the string stems only 301.09
(3.2 dB) and 297.91 (3.6 dB) exceed 3 dB.

## Do not touch

The c53 Violins II leads at 66-78 and Violins I 80 / 262; the `JOIN_NOTCH_S` shapes (Violoncellos 68.5 and the
others); the Horn 2 208 values; Horn 3's `WIND_REP_RETONGUE_AT` row at 289; the printed breath at 286 and the
breath gaps at 196 / 204; Violoncellos 77 and its lead; the rule that body rows and start shapes are up on the beat;
one legato row per string line (no Leg BC MAX for single notes).
