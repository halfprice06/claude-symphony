# Cycle 30, critic A: articulation and phrasing (render c29)

Scope: the c29 render after its stem fix (`cycles/c29/render/`) against `build/parts.json`. Controls for repeatability: c27, c26, c24, c20. Levels are plain stereo power on 20-50 ms frames unless stated. "Crossover" means the first frame where the new pitch's harmonics 1-4 carry more energy than the old pitch's (4096-point FFT, 10 ms hop). Every fix below was simulated by applying the volume change to the c29 stem and adding the difference to the master; c29 found that this method matches a render to 0.1 dB. All four fixes are level-only, so a stem fix plus `--mix-only` on the affected tracks is enough. Score pages 1, 2, 4, 11, 16 and 17 were checked (bars 1-30, 39-46, 121-130, 163-182).

## Checks that passed (measured, no action)

- **Item 8, accents.** I scanned 584 accents for 2-5 kHz energy over the first 80 ms against the note body. Only 3 stems read over +4 dB: Violas 536 (+11.8), Clarinet 1 558 (+5.8), celli 536 (+5.0). At all three the master falls 5-7 dB at the accent, because the front is the previous ff chord's release before a printed mf. The largest master jump is +3.7 dB, at the tutti ff arrival at 128.
- **Item 7.** `loopscan.py 29`: the master reads +0.40 (Lento), -0.38 (final chord) and -0.45 (bars 160-164) at 3.95 s. One stem is over 0.4 on a window long enough to trust: celli 504 (0.53 on the centroid), which is a run of 40 short repeated notes, not one held note. Celli 11.0 also reads over 0.4, but its window is flagged too short.
- **Re-bows.** 92 re-bows, median dip 2.5 dB. The deepest ones in the master are the Violins I final-chord pieces (722.781: stem swing -44..-56). This is the sample's 3 Hz swing recorded at c24, and the master stays within -41..-46.
- **Keyswitches.** No keyswitch lands 0-0.03 qn after the note that needs it.
- **Legato rows.** No chords on legato rows (c29 check still holds).
- **Tremolo.** Every tremolo entry and chord change dips 4.4 dB or less in the stem, except Vln II 304 (7 dB in the stem, master flat).
- **Breath marks.** All 24 have gaps of 0.14-0.30 s.
- **Pizzicato.** Basses and celli pizzicato onsets are on time.
- **Tam-tam pp at 696.** It sits 10-13 dB under the master below 800 Hz, which is audible as a low wash.

## 1. Early fills that now start on the old note: a 4-8 dB swell just before ten string legato joins. Worst case: the coda cello solo at bar 172 (measured; fix simulated)

**Where (main case).** Violoncellos, coda Più lento, bar 172 (qn 684-688). This is the mp espr. cello solo with the cor anglais. The slur runs C4 - A-flat4 (tenuto, the Leg Port target at 685) - G4 (687). A printed < runs from beat 2 to the G4.

**What is wrong.** `early_fills.json` Violoncellos `687` is {db 3.5, pre_s 0.17, hold_s 0.35}. It raises the envelope from +1.0 dB at 686.68 to +7.7 at 686.79, which is 0.20 s before the score onset. The G4 takes over only at the beat: the own-pitch crossover is at +0.00 s. Until -0.04 s the A-flat4's harmonics read 34-37 dB and the G4's 23-27. So the fill lifts the tail of the A-flat4, not the G4's sag. In 40 ms frames:
- **Stem.** A-flat4 body -33..-36. Then a burst of -27 -27 -28 -29 over -0.20..-0.04 s. Then the G4 at -34..-39 for 0.44 s.
- **Master.** -27 at the burst, then -34..-36 on the G4.

The < therefore peaks before its arrival note, and the arrival comes in 7-9 dB lower.

**Why it got worse (measured).** The burst over the larger body was +4.5 dB in c24 and c26 and +7.6 dB in c29. Two other joins grew in the same way: 650 went +2.5 -> +6.6 and 712 went -1.1 -> +4.2. c27 moved the celli fills with their targets and changed the Leg BC/Leg Slur leads, and the crossovers now arrive on the beat. As a result, every fill with pre_s 0.09-0.17 s now acts on the old note.

**The other joins.** The same scan over all 81 fills with pre_s over 0.05 s found nine more. In each, the old pitch swells over both bodies in the pre_s window while the crossover is at -0.04..+0.04 s. Simulated with pre_s = 0, keeping each fill's db and hold_s:

| track, onset (bar) | fill db/pre/hold | stem bump over bodies | stem dip | master bump |
|---|---|---|---|---|
| Vc 650 (163) | 3.3/0.14/0.35 | +6.5 -> +3.2 | 1.7 -> 2.3 | +0.4 -> +0.1 |
| Vc 422 (106) | 4.1/0.14/0.35 | +6.0 -> +5.2 | -1.2 -> 2.2 | +1.3 -> +0.3 |
| Vc 266 (67) | 4.1/0.14/0.35 | +5.2 -> +2.0 | 4.8 -> 4.8 | 0.0 -> -0.1 |
| Vc 66 (17) | 6.0/0.13/0.27 | +4.8 -> -0.4 | 5.9 -> 5.9 | +2.9 -> -0.1 |
| Vla 429 (108) | 2.5/0.10/0.30 | +4.5 -> +2.0 | 2.8 -> 2.8 | +3.6 -> +1.4 |
| Vc 712 (179) | 3.3/0.14/0.35 | +4.2 -> +0.9 | 4.2 -> 4.2 | +1.5 -> +1.3 |
| Vc 10 (3, Lento) | 1.4/0.09/0.10 | +3.6 -> +3.1 | -2.0 -> -2.0 | +3.0 -> +2.2 |
| Vc 4 (2, Lento) | 3.9/0.10/0.10 | +2.5 -> -0.1 | -0.5 -> -0.5 | +3.7 -> +1.3 |
| Vc 694 (174, solo) | 4.3/0.14/0.35 | +2.2 -> -2.1 | 1.9 -> 2.7 | +2.7 -> -0.5 |

For 687, pre_s 0 alone leaves the master burst at +2.4 dB, and the G4 is still 3 dB under the A-flat4.

**Fix.**
1. In `build/early_fills.json`, set `"pre_s": 0.0` on these nine entries and keep their db and hold_s: Violoncellos 650, 422, 266, 66, 712, 10, 4, 694, and Violas 429.
2. Delete the Violoncellos `687` early fill.
3. Add this exact shape to `build/score_config.py`:

```
LEVEL_SHAPES_S["Violoncellos"] = LEVEL_SHAPES_S.get("Violoncellos", []) + [
    (687.0, [(-0.25, 0.0), (-0.20, -2.0), (-0.03, -2.0), (0.0, 7.0), (0.36, 7.0), (0.52, 0.0)])]
```

**Simulated, bar 172, 40 ms frames.**

| | old | new |
|---|---|---|
| Stem, A-flat4 tail | -27..-29 | -32..-34 |
| Stem, G4 | -34..-39 | -33..-35, then rising into 688 |
| Master, before the beat | -27 | -31 |
| Master, G4 | -34..-36 | -32..-34 |

The A-flat4 body and bars 173-174 are unchanged.

**Pass.**
- At each listed join, the 40 ms peak in the pre_s window is at most 3 dB over the larger body.
- No join dip grows by more than 1.5 dB.
- At 687, the G4's first 0.4 s on the master is within 2 dB of the A-flat4 body or above it.

## 2. Bars 43-44 (qn 168-176), the p horn duet: Horn 2's G4 dies away, then both horns jump 15-20 dB against the printed diminuendo (measured; fix simulated)

**Where.** Horn 2 holds G4 p for bar 43 (168-172; Leg Slur MAX first note, v53). Horn 1 enters at 170 (E-flat4 - C5 tied over the bar - B-flat4 at 174). In bar 44, Horn 2 has E-flat4 (172-176). Both horns have a printed > over bar 44. The horns are the exposed voices over pp strings: Horn 1 is -1 dB and Horn 2 -4 dB re master in bar 44.

**Evidence (measured, 0.2 s frames from 167.6).**

| frame (qn) | 168.0-171.4 | 171.8 | 172.2-173.5 | 173.9-174.7 | 175.2-176.0 |
|---|---|---|---|---|---|
| Horn 2 | -49..-51, then **-54..-57** | -45 | **-38 / -40**, then -46..-47 | -45 | -46..-48 |
| Horn 1 | (enters 170: -42, C5 -38) | -38 | -45 / -49 / -52 / -52 | **-39 / -36** / -41 | -49..-57 |
| master | -34..-39 | -36 | -35 / -36 / -38 / -39 | **-37 / -36** / -38 | -38..-40 |

- **Horn 2.** Its held p G4 falls 7 dB at flat CC11, from the first half of the note to the second. It sits 13-18 dB under Horn 1's entry, so the bar-43 horn chord is heard as Horn 1 alone. Its E-flat4 then arrives 17 dB over the G4's end.
- **Horn 1.** Its C5 falls 15 dB during the first half of the printed > (vol_db goes from -2.2 to -5.3 over 172.0-172.5, with CC11 46 -> 35). Then vol_db steps +4.95 dB at 173.824 -> 173.904, and the B-flat4 comes in 17 dB over the C5's end, louder than the C5's peak.
- **On the master,** the diminuendo bar plays as a fall (-35 -> -39) and then a 3 dB swell on its last note (-36).
- **Repeatability.** c28 and c29 are identical. Horn 1 and 2 were not changed in c29.

**Fix.** Add these exact shapes to `build/score_config.py` (qn polylines):

```
LEVEL_SHAPES["Horn 2"] = LEVEL_SHAPES.get("Horn 2", []) + [[(168.3, 0.0), (168.9, 1.5), (169.6, 3.0), (170.3, 6.0),
    (170.8, 8.0), (171.8, 8.0), (171.9, -4.0), (172.4, -6.0), (172.9, -3.0), (173.5, 0.0)]]
LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES.get("Horn 1", []) + [[(172.0, 0.0), (172.315, 2.0), (172.63, 3.5), (173.05, 4.5),
    (173.47, 6.0), (173.806, 6.0), (173.89, -4.0), (174.1, -7.0), (174.73, -7.0), (175.15, -4.0), (175.675, -1.5), (175.99, 0.0)]]
```

**Simulated (both together), same frames.**
- **Horn 2:** G4 -46..-49, E-flat4 -43/-44 -> -47.
- **Horn 1:** C5 -38/-43/-45/-46/-48, B-flat4 -45/-43/-47/-51. It stays 1-3 dB over Horn 2.
- **Master:** -35.9 -36.5 -37.2 -38.0 -38.5 -39.2 -39.8 -39.0 -38.0, which is a continuous fall through bar 44. The old master read -35.7 ... -38.9 -36.6 -35.7.

**Pass.**
- Horn 2's G4 frames over 168.4-171.8 are within 4 dB of each other, and at most 6 dB under Horn 1 from 170.
- No 0.2 s master frame in 172-176 is more than 1 dB over the one before it.
- Run `envdiff.py` before rendering: the new Horn 2 breakpoints at 171.8/171.9 sit 0.03 qn either side of the E-flat4's moved onset 171.874.

## 3. Recapitulation second theme, bar 153 (qn 611): the celli's slur-end A3 swells 7 dB into the next bow, a 4.6 dB bump on the master at a phrase end (measured; deterministic; fix simulated)

**Where.** Violoncellos with Clarinet 1 in unison, mp. The celli lead (-2.8 re master, clarinet -7). The slur runs 607-611 and ends on the A3 quarter at 611. A new slur with a printed decresc starts at 612.

**Evidence (measured, 40 ms frames from 610.9).**
- **Stem.** The A3 rises -42 -> -36 -> -33.6 at 611.6-611.75, then -40 by 612.0. The Leg BC join into 612 (moved onset 611.72) lands on top of the A3's swell.
- **Master.** -35..-37 around it, -31.1 at the peak.
- **Repeatability.** c27 and c29 are identical. The exposition statement (bar 53, different notes) has no such swell.

**Fix.**

```
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(611.1, 0.0), (611.2, -3.5), (611.45, -4.5), (611.85, -4.5), (611.97, 0.0)]]
```

**Simulated.**
- **Stem:** -42..-38 over the A3, and 612.0 unchanged (-40).
- **Master:** -35.6 -35.9 -36.4 -36.3 -36.4 -35.2 -33.6 -33.3 -34.7 -36.7. The peak is now 2.4 dB over the phrase instead of 4.6.

**Pass.** The master over 611.1-612.0 is at most 2.5 dB over its 610.0-611.0 median, and the 612 entry is unchanged within 0.5 dB.

## 4. Fugato, bar 89 (qn 352-354): the celli's countersubject half note jumps 6-7 dB over its own line, to the level of the mf subject (measured; small; fix simulated)

**Where.** The violas and Bassoon 1 carry the subject from 348.5 (mf, accent at 349, staccatos). The celli countersubject is mp: short Sus MAX notes over 349.5-351, then the E-flat4 half note at 352 on Leg BC MAX (v124).

**Evidence (measured, per note, onset + 0.05 s to the note end, at most 0.8 s).**
- **Celli:** 349.5 / 350 / 350.5 / 351 / 352 read -51.0 / -48.2 / -52.0 / -44.9 / **-38.3**.
- **0.5 qn windows at 352.5-353.0:** celli -36.9 / -38.3, violas -40.2 / -38.1, Bassoon 1 -36.8 / -36.7.
- So the mp countersubject is level with the mf subject for a beat, and the master rises 2-3 dB at 352.5-353 (-33.1 / -32.4, against -35..-36 before it).
- **Cause (inferred).** The level difference between the soft Sus MAX short notes and the Leg BC sustain at the same CC11.

**Fix.**

```
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(351.9, 0.0), (352.2, -4.0), (353.8, -4.0), (353.95, 0.0)]]
```

It starts after the 351.685 join, so the join's sag is not deepened.

**Simulated.**
- **Celli:** -42.6 / -40.6 / -44.4 / -42.5 over 352.15-353.7, 2-4 dB under the violas.
- **Master:** -35.0 / -33.9 / -34.0 / -34.3.
- 354 onward is unchanged.

**Pass.** Over 352.2-353.8, the celli are at least 1.5 dB under the violas in each 0.5 qn window.

## Patches

I recommend no patch change for the final render.
- **a2 tracks.** The brass a2 tracks (2TP Leg Slur MAX, 2TB Sus MAX) are still the one patch upgrade left in my lens. They need new Opus instances at the memory limit, full rebuilds and refits, and no later render could check them.
- **Bar 172.** The Leg Port MAX on the cello's 685 sixth is correct and should stay. The swell in finding 1 is from the fill, not from the portamento row.

## Do not touch

- The c29 shapes (CA 23.5-25 stem-fix shape, bar-52 Horn 1/celli, Clarinet 1 212.72, Oboe 1 578.96, celli 723.921 re-bow row).
- The c28 coda cello/cor anglais steps 689.18-693.8. Finding 1's 687 shape and the 694 pre_s change sit outside them.
- GENTLE_ACCENT with the current accent fits, bodies and the c24 cuts.
- The c27 legato leads. Finding 1 corrects the fills, not the leads.
- The re-bow times and every other `rebow_fills.json` row.
- The breath splits, the Leg Port rows at 225/685, and the Stac RRx9/RRx14 and shortened-Sus staccato.
- The harp étouffez damps.
