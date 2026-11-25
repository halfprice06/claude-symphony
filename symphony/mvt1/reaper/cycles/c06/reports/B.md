# Cycle 6, critic B: balance and levels (render c05)

## Method

All measurements are on the stem-fixed c05 render (`cycles/c05/render/`). Score qn maps to file time through the parts.json tempo map.

- **Levels:** K-weighted stereo power on 25 ms hops. Note bodies run from onset +0.05 s to +0.35 s for accents, and from +0.08 s to min(end, +1.5 s) otherwise.
- **Raw level:** the body level minus the full track envelope at the onset (build_reaper `vol_points`: gain, trims and `vol_db`).
- **Margin:** the lead's level minus the loudest other stem in the same 1- or 2-qn window.
- **Simulations:** roles, note trims and mix changes are applied to the stems, and the result is delivered with `tools/deliver_master.py`. Climax maxima are delivered short-term LUFS. With no change, the simulation reproduces c05 exactly: LRA 15.6 LU, span 20.3 dB, limiter 3.0 dB, bar 160 -9.56, bar 122 -10.29, bars 167-170 -12.11.

Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c06-B/`:

- `notes.py`, `samedyn.py`, `rawuni.py`, `dbl.py`: per-dynamic and unison comparisons.
- `acclev.py`, `rowgap.py`, `notetr.py`: accent level against neighbours.
- `leadscan.py`, `topcover.py`, `clim.py`: lead margins and covering stems.
- `sim5.py` + `marg.py` with `s_acc3.json` / `s_all.json`: simulations.
- `loopscan.py`, `fold.py`, `acc.py`: Dan's two checks.

## What holds (measured)

**Families at each printed dynamic.** At p and pp the single winds, horns and string sections fall within 3-4 dB of each other:

| Dynamic | Single winds (dB) | Horns (dB) | Strings (dB) |
|---|---|---|---|
| p | -40..-46 | -42..-43 | -42.7..-44.5 |
| pp | -41.7..-46.5 | -43..-45 | -43.4..-47.6 |

**Trumpets at f/ff, at the same onsets:**

| Trumpet 1 against | f (dB) | ff (dB) |
|---|---|---|
| Horn 1 | +2.9 | +2.3 |
| Horn 3 | +2.9 | +3.3 |
| Trombone 1 | -2.1 | +0.7 |

This is Rimsky-Korsakov's order: trumpet = trombone > horn.

**Previous cycle's balance fixes.**

- The printed-dynamic inversion scan finds only single bars, against 7-12 pairs per track in c04.
- The c05 B fixes hold:
  - flute solo bars 73-75: margin +0.7;
  - bass clarinet solo bars 77-78: +3.3;
  - molto cantabile melody bars 56-61: +2.3, never under;
  - Violins I bars 35-40: +1.5.

## 1. Every accented note plays 20 velocity steps hot. With the accent swell on top, brass accents stand 5-13 dB over their neighbours, and the brass themes of bars 69-72 and 167-170 break into loud accents with gaps between them

**Where:** every accented Sus note in brass, winds and strings. Worst in the Horn 1 theme (bars 69-72), the Horns/Trumpets a2 theme (bars 167-170), Trombone 1 in bars 80-81, and the Tuba in bars 41 and 138.

**What is wrong (measured):**

- `GENTLE_ACCENT` is meant to give an accent no extra velocity. Every accented note in parts.json carries the source MIDI's accent velocity anyway:

  | Printed dynamic | Plain Sus | Accented Sus | Notes |
  |---|---|---|---|
  | f | v83 | v103 | n = 74 brass, 68 wind, 39 string |
  | ff | v91 | v111 | |
  | mf | v72-73 | v91-96 | |

  - In `score_to_parts.py` only the `+10` for non-GENTLE families is skipped (line 1734). The LilyPond accent velocity is never removed.
  - The HO manual (ch. 2, p. 51) says velocity "influences overall volume".
- Accented minus unaccented Sus at the same dynamic, raw (envelope removed):

  | Track | Raw gap (dB) |
  |---|---|
  | Horn 1 | +3.6 |
  | Trumpet 1 | +6.1 |
  | Trombone 1 | +3.7 |

  The +4 dB brass swell is added on top of this.
- Legato notes on Leg Slur MAX sit another 2.5-3.3 dB under plain Sus at f/ff (Horn 1 -35.1 / -31.8, Trumpet 1 -39.4 / -37.0, Trombone 1 -35.8 / -33.3 raw).
- Accent body (+0.05-0.35 s) minus the median of unaccented notes of the same track within 6 qn at the same printed dynamic, at f/ff:

  | Family | Median (dB) | p90 (dB) | Max (dB) |
  |---|---|---|---|
  | Brass | +4.9 | +9.4 | +13.1 |
  | Winds | +3.8 | +8.3 | |
  | Strings | +2.5 | +8.5 | |

  The brief's target is about 2-4 dB.
- In the themes, the slurred running notes after each accent fall 8-14 dB:
  - Horn 1, bars 69-71: accents -25.6..-31.6, the slurred eighths -36..-42.
  - Horn 1, bars 167-169: accents -18.0..-22.6, the notes after them -29.7..-34.
  - Trumpet 1, bars 167-169: accents -20.0..-22.7, the notes after them -24.8..-34.2.
  - Accented minus other notes (median): Horn 1 bars 69-72 +7.4, Horn 1 bars 167-170 +8.1, Trumpet 1 bars 167-170 +8.9 dB.
- The accents also cover the texture:
  - Trombone 1's Eb4 at 81.2 is the loudest stem by +4.0 dB (body -25.0; the same figure's Eb3 at 80.2 is -31.8).
  - The Tuba's accented sf at 41.1 is the loudest stem by +2.8 dB, and its accented f at 138.1 by +2.5. Its unaccented f notes right after are 12 dB lower.
  - Horn 1 F4 at 169.2 is +13.1 over its neighbours.
- The 2-5 kHz attack check passes (see Dan's checks). This is a level problem, not bite.

**Fix:**

1. **`tools/score_to_parts.py`, velocity block (lines 1733-1735).** For families in `GENTLE_ACCENT`, play an accented note at the velocity of a plain note at the same dynamic plus a small fixed weight.
   - New config `GENTLE_ACCENT[family]["vel_add"] = 5`. Movement II c26 used v96 at ff, base 91: +5.
   - Implementation: `n["vel"] = min(127, plain_vel + vel_add)`, where `plain_vel` is the velocity an unaccented note at that onset would get. In practice, subtract the source accent increment: `n["vel"] -= 20 - vel_add` when `n["qn"] in accent_q` and the note is not a legato target.
   - Keep the swells at brass 4.0, wind 3.5, string 3.0 dB for this render, and re-measure before touching them.
2. **`build/note_trims.json`.** Brass legato notes inside the two themes, so the run is not 8 dB under its accents:
   - +3 dB on every Leg Slur MAX note shorter than 1 qn in Horn 1 [268, 288] and in Horn 1 and Trumpet 1 [664, 680].
   - Use a step (0.1 s ramp).

**Simulated (inferred for the velocity part):**

- I simulated the velocity change as -3.5 dB on each of the 145 accented brass Sus notes, with fix 2 added.
  - Accented minus other notes: Horn 1 bars 69-72 +7.4 -> +2.5, bars 167-170 +8.1 -> +3.8; Trumpet 1 +8.9 -> +3.7 dB.
  - Delivered LRA 15.6 -> 15.4 LU, span 20.5 dB, limiter 3.0 -> 3.2 dB.
  - Climax order kept: bar 160 -9.41 > 122 -10.12 > 167-170 -12.91.
- With winds and strings included (-3 dB on 272 more accents), the limiter rises to 3.5 dB and bars 26-28 fall 1.9 dB.
  - So apply the wind and string part only after the brass part is measured, or with `vel_add` around 10 for those families.

## 2. The oboe's p solos that lead into both second themes are buried or uneven (bars 45-46 and 145-146)

**Where:** Oboe 1, qn 176-184 ("1." p, the descending poco rit. figure over pp strings) and qn 578-582 (recapitulation, p dolce).

**What is wrong (measured):**

- **Bars 45-46.** The oboe sits under the loudest pp string stem on every beat.

  | Beat | Oboe 1 (dB) | Loudest string stem (dB) | Margin (dB) |
  |---|---|---|---|
  | 45.2 | -47.0 | celli -37.1 | -9.9 |
  | 45.3 | -44.8 | celli -39.4 | -5.4 |
  | 46.1 | -42.3 | Violins II -38.2 | -4.1 |
  | 46.3 | -39.4 | Violins II -34.5 | -4.9 |

  - Median margin over qn 176-184: -5.2 dB, under in 4 of 4 two-qn windows.
  - The pp strings there run 4-6 dB over their own pp medians:
    - Violins II has an envelope of +13 to +14 dB (gain 6 plus pp soft trim 7).
    - The celli have +7 to +8.
    - The Oboe 1 envelope is 0 (gain -5, p trim +5).
  - A printed p solo over pp accompaniment should sit about 3 dB over it (kit LEARNINGS 13).
- **Bar 145.** The pickup G4 at qn 578 measures -51.7 dB, 11 dB under the pp strings around it. The next note, E5 at 579 (with the current -5 to -6.9 dB envelope there), reaches -35.4 at 146.1. So the phrase starts inaudible and then jumps 16 dB.

**Fix:**

- `build/roles.json`: Oboe 1 `[176, 184, 4]`; Violins II `[176, 183, -2]`; Violoncellos `[176, 182.5, -2, 0.25]`. The last must end before the celli's mf pickup at 183.
- `build/note_trims.json`: Oboe 1 `"578.0": 8` (step).

**Simulated:**

- Bars 45-46 margin -5.2 -> +0.6 dB median, under by more than 1 dB in 1 of 4 windows (was 4 of 4).
- Bar 145-146 margin +1.4 -> +2.2 dB, and the pickup is no longer 11 dB under.
- Delivery unchanged (soft passages under the ride).

## 3. The tam-tam's tail is the loudest stem through the p music of bars 125-127, then cuts at qn 512

**Where:** Tam-tam, qn 484-512. The fff heavy-beater stroke is printed l.v. to bar 126 (the note ends at qn 504.3). The c05 roles are `[484, 512, 2]` and `[487, 512, 4]`.

**What is wrong (measured):**

- The +6 dB lift that critic C wanted for the bloom at +0.5-4 s holds until bar 128.
  - At bar 125-126 the orchestra is p/pp: bar 126 is marked p/pp, and Clarinet 1 enters p at 504.5.
  - Tam-tam re master: bar 126.1 -6.6, 126.3 -7.3, 127.1 -6.2 dB. It is the loudest stem by 2.2-2.8 dB at qn 500-503.
  - At 504 it is level with the Clarinet 1 entry: -41.0 against -39.1.
- At qn 512, the role's release (+6 -> 0 over 0.25 qn) and the end of the ring take the stem from -47.5 to -65.6 dB within 2 qn. That is an audible stop in the Clarinet 1 solo (inferred: the tail is 12 dB under the master at 508).
- The stroke itself (bar 122) is right: loudest stem by 1.4-2.3 dB at the fff.

**Fix: `build/roles.json` Tam-tam.**

- `[484, 512, 2]` -> `[484, 500, 2, 4]`.
- `[487, 512, 4]` -> `[487, 496, 4, 4]`.

This keeps C's +6 dB over the first 5 s and returns to 0 by bar 126.

**Simulated:** bars 126-127 tam-tam -4 dB, under Violins II and Clarinet 1. Bar 122 unchanged.

## 4. The coda's timpani motif (bars 179-180, pp soft sticks) is still 12.5-15.8 dB under the master at its own attacks

**Where:** Timpani, qn 712-719.5 (C3-G2-C3 strokes, v62, Tempo I). It recalls the movement's opening over the pp string chord.

**What is wrong (measured):**

| | Stroke peak (25 ms, dB) | Master in the same frame (dB) | Loudest other stem (dB) |
|---|---|---|---|
| Range over the six strokes | -48.0 .. -51.1 | -34.9 .. -36.9 | -36.9 .. -43.0 |

- Each stroke is 12.5-15.8 dB under the master and 6-10 dB under the loudest string stem.
- The c04 stem fix `[711.5, 719.5, 5]` was not enough. For comparison, the bar-12 p strokes sit 5-7.6 dB under the master, and the bar-72 f strokes 3.7-6.4.
- A pp stroke as the only rhythmic event over a held pp chord should be heard (inferred). The brief's settle rule applies to rolls, not strokes.

**Fix: `build/roles.json` Timpani.** `[711.5, 719.5, 5]` -> `[711.5, 719.5, 10]`. Keep v62: it is the soft-stick colour.

**Simulated:** stroke peaks about -43..-46 dB, 8-11 dB under the master and 0-6 dB under the loudest string stem.

## 5. Violins II plays 4-8 dB under Violins I wherever it doubles the tune at f/ff, in unison or an octave below

**Where:** Violins II at ff in bars 25-32, 81-83, 97-104, 117-124, 129-144 and 157-164 (e.g. bars 117-120: "unis.", the tune an octave under Violins I, with Flute and Oboe).

**What is wrong (measured):**

- Violins I minus Violins II on notes at the same onset an octave apart, at ff, per 4 bars: +3.3 to +9.6 dB (e.g. bars 117-120 +7.3, n = 18).
- On notes of the same pitch and onset, at ff: +6.6 dB (n = 7; fff +5.7, p +4.6).
  - Of this, 2.0 dB is the envelope: gain 5 / 6, ff trim +1.5 / -1.5.
  - The other 3.7-4.6 dB at f/ff is the patches' own raw gap.
- Over all same-onset ff notes: Violins I +6.3 dB over Violins II (n = 103), against +1.4 at f.
- In bars 117-120 Violins I stands -5.5 dB re master and Violins II -13.3. The octave doubling that gives the tune its body is barely there, and the tune is one section wide (inferred).

**Fix: `build/mix.json` Violins II.** `dyn_trim_db` ff -1.5 -> +1.0 (f stays -2.5). The existing accompaniment cuts `[440, 464, -4]` and `[664, 680, -4]` keep the ff chords under the tunes there.

**Simulated:**

- Delivered LRA 15.6 -> 15.7 LU, limiter 3.0 -> 2.8 dB, span 20.4 dB.
- Melody margins at bars 117-120 and 156-161 unchanged (+3.4 / +3.5). Bars 138-142 +3.0 -> +1.1, because the loudest other stem there is now Violins II in unison on the same line.
- Climax order kept (160 -9.61 > 122 -10.21 > 167-170 -12.15).

## 6. Second theme: at the start of each bar-49/149 slur, Horn 1 drops 8-12 dB under its celli unison

**Where:** Horn 1 ("1. dolce", mp) and celli ("dolce", mf), in unison at qn 184-216 and 584-616.

**What is wrong (measured):**

- The printed mp against mf makes the celli the upper partner. The horn's median 3.4 / 2.1 dB under the celli matches that, and the horn colour is there in most of the phrase.
- At the re-attacked note that starts each slur the horn falls out:
  - qn 192 (Db4, v82, no lead): horn -40.0 against celli -31.6 (-8.4 dB). At 192.25-192.5 the horn is at -44.5, a 6 dB hole, while the celli rise 4 dB into the crescendo.
  - qn 592 (F4): -12.3 dB.
  - Smaller holes at 204 (-8.0) and 595.5 (-7.7).
- Inferred cause: the re-tongued note on Leg Slur MAX plays its slow first-note layer (kit LEARNINGS 5). Critic A may prefer a join.

**Fix:**

- The level fix is `build/note_trims.json` Horn 1 `"192.0": 4, "592.0": 5` (step).
- The better one, if A agrees, is `PORTATO_JOIN_AT["Horn 1"] += [192, 592]` (as at 189/201/589/601).

**Simulated (note trims):** the worst window 149.1 goes -9.7 -> -7.2 dB. A join would close the hole itself.

## Combined simulation of findings 1 (brass part) to 6

Spec: `s_all.json` (brass accents -3.5, theme legato +3, Oboe/Vln II/Vc roles and the 578 trim, Tam-tam -4 over [496, 512], Timpani +5, Horn 1 trims, Violins II ff +1).

- Delivered: LRA 15.6 -> 15.5 LU, span 20.3 -> 20.5 dB, limiter 3.0 dB, TP -1.6 dBTP.
- Climaxes: bar 160 -9.45 > bar 122 -10.03 > bars 167-170 -12.91.
  - The margin of bar 160 over bar 122 narrows 0.73 -> 0.58 dB.
  - If the render confirms that, `"_all": [[484, 492, -0.5, 2]]` in roles.json restores it (inferred).

## Dan's two checks (measured)

**Loop pulsing.** Notes over 6 s now exist only on winds, brass, the harp and percussion. Strings and timpani rolls are re-bowed or re-struck.

- Cor anglais G4, qn 27 (9.4 s, the intro solo): centroid autocorrelation +0.73 at 3.95 s (best lag 4.0 s, 0.69), folded centroid swing 228 Hz. Its level does not pulse (K level autocorrelation -0.09 at 3.95 s). It sits inside a printed decrescendo.
- Horn 4, qn 289 (6.9 s, pp pedal): 100-300 Hz autocorrelation +0.76, centroid -0.15. The stem is 9.8 dB under the master.
- Tuba, qn 488 (6.4 s): 100-300 Hz +0.92, centroid -0.48. The stem is 16.8 dB under the master.
- The 6-7 s windows give only 2-3 s of overlap at the 3.95 s lag, so treat the Horn 4 and Tuba values as indicative.
- These belong to A's and C's lenses. Nothing here affects balance.

**Accents.** 2-5 kHz in the first 80 ms minus the body, median (p90):

| Track(s) | Median (p90), dB |
|---|---|
| Trumpet 1 | -5.1 (-2.5) |
| Trumpet 2 | -11.5 |
| Trumpet 3 | -13.5 |
| Horn 1 | -4.5 (+3.6) |
| Horn 3 | -0.1 (+2.6) |
| Trombones, Bass trombone, Tuba | -8.2..-12.4 |
| Violins I, celli | -2.7 |
| Oboe 1, Clarinet 1, Flute 1 | -4.2..-5.1 |

No bite anywhere. The problem in finding 1 is body level, not attack.

## Do not touch

- The trumpet `dyn_trim_db` (f/ff ratios against horns and trombones are right).
- The c04 fff brass roles and the climax order (160 > 122 > 169).
- The global soft trims 7/7/5 and the per-track pp overrides.
- The c05 B roles (Violins II tremolo cuts, Flute 1 / Bass clarinet solo lifts, Horn 2 [220, 244, -1], Violins I [144, 160, 2]) and the oboe ff trim 6.
- The tam-tam stroke level and timing at qn 484 (only the tail rows change).
- Brass, wind and string `GENTLE_ACCENT` swell shapes and articulations (no accent samples, no CC11 bump).
- The percussion patches and the sus. cymbal timing.
