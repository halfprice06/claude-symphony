# Cycle 25, critic A: articulation and phrasing (render c24)

Scope: every wind, brass and string note in `cycles/c24/rendered_build/parts.json`, measured on the c24 stems and master, with c23 as the control (5 ms feature caches for both renders). I reran the c22/c24 battery on both renders: joins, kscheck, ties, rebow, longloop, acchf, accpk2, accshape, pkr3, ssj, sstart, pairs, stacsep, tremj, timp, harp, pz3, breath, ten200, rests2, cutoffs, reltime, relburst2, efchk2, detw2, rrcyc and chordleg2. New scripts: `xall25.py` (pitch crossover on every legato target, harmonics 1-4), `accx25.py` (each accent's 0-0.30 s level against its plain neighbours), `chain.py` (accents whose neighbours are all accented), `accpt.py` (peak time and front-minus-mid on every note), `mjump.py` (the master's 2-5 kHz jump at every accented onset), `rbctl25.py` / `rbcoda.py` (re-bow dips against control times), `corr.py`, `pkw.py`. Score pages 2, 7, 12, 13, 14 and 17, plus `mockup-events.tsv`.

## Checks that passed (measured, no action)

- **Keyswitches and ties.** Shortest keyswitch lead is 14 ms. No chord goes to a legato row. Every keyswitch inside a sounding note is a planned row change. Ties hold.
- **Legato joins.** No wind or brass join is 6 dB or deeper except Clarinet 1 213 (6.2 dB, unchanged).
- **Crossover medians.** Strings +0.007 to +0.055 s, winds +0.02 to +0.07 s, brass +0.01 to +0.06 s.
- **Joins changed by c24.** Clarinet 1 227 went 2.2 -> 5.2 dB, because the c24 B #4 cut replaced a +13 dB spike with a 0.4 s rise. That is acceptable. Vln I/II 259.5 is now a Leg Slur target: Vln I dip -11.5 -> -8.5 dB, Vln II -6.1 -> -7.3, crossovers +0.05/+0.075 s. That is fine.
- **Item 7 (loop pulse).** No string note within 6 dB of the master pulses at the loop period:
  - Final chord: Violins I 720 level acf 0.13, centroid acf 0.19. Violins II 712 -0.11 / 0.17.
  - Bass clarinet 11 (acf 0.58, -6.1 dB re master) is the known exception.
  - The high acf values on Bassoon 2 684, Trombone 1 716 and Horn 4 289 are re-tongued notes or 6-7 s notes with only 1.5 loop cycles. Their 0.2 s traces show no repeating dip larger than 2-3 dB.
- **Re-bows.**
  - Medians: Vln I -3.0 (c23 -4.5, after the 711.855 fill), Vln II -2.1, Vla -2.6, Vc -2.8, Cb -1.4 dB.
  - On the final chord the master dip at the 30 re-bows has a median of -2.5 dB. At control times 0.9 s or more from any re-bow it is -1.15 dB. The worst re-bow dips (-3 to -4 dB) are inside the control's p10 (-3.5).
  - The re-bows add an irregular movement but not a periodic one, so no action.
- **Item 8 (accent bite), stems.** 2-5 kHz first 80 ms minus body: brass median -8.3, winds -3.7, strings -2.7.
- **Item 8, master.** Over 91 accented onsets, the master's 2-5 kHz front minus body has a median of -0.6 dB. The largest jumps are:
  - qn 354: the violas' mf accent, +7.0 front-body, +3.4 front-pre, at -32 dB.
  - qn 568: the bar-143 ff tutti chord, +3.0 / +5.0, which fits an ff accented cut-off.
- **Other articulations.** Staccato separation (6.7-14 dB), pizzicato onsets, tremolo joins (median -1.1 dB), harp rolls (0.067 qn per note, low to high), breath gaps, tenutos and release bursts are all within 1 dB of c23.
- **Pickups on the master.** Wind theme pickups sit 6-11 dB under their targets on their own stems (Oboe 1 146.5 -10.6, Clarinet 1 552.5 -9.7). On the master every theme pickup is within 1 dB of its target body, because the violins carry it. No action.

## 1. The hemiola accents in bars 22-24 and 135-137 are almost flat: the cross-rhythm cannot be heard (measured)

**Where.** The accented dotted halves at qn 88, 91, 94 and 97 (exposition) and 536, 539, 542 and 545 (recapitulation). They are in Clarinet 1-2, Bassoon 1-2, Violoncellos and Horns. They make 3-beat units across the 4/4 barline under mf (mp) < to ff (bar 25) or f (bar 138). See score pages 3 and 13: every note is accented, unslurred, and tied over the barline.

**Evidence (measured).** Step = 0-0.30 s after the score onset minus the 0.30 s before it, on each stem.

| Track | 91 | 94 | 97 | 539 | 542 | 545 |
|---|---|---|---|---|---|---|
| Clarinet 1 | -1.3 | +1.2 | +4.5 | -0.4 | +0.5 | +1.4 |
| Violoncellos | +0.9 | -1.4 | +3.1 | +0.5 | -1.1 | +1.4 |
| Bassoon 1 | +6.2 | +1.5 | +1.4 | +2.4 | +1.7 | +0.9 |
| Master | +2.4 | +1.1 | +3.8 | -0.3 | +0.5 | +2.2 |

- In the recapitulation the off-beat accents at 539 and 542 add nothing on the master. The passage sounds like a smooth crescendo of held notes, not a syncopation.
- Elsewhere, accents sit at a median of +3.0 dB over their plain neighbours (winds and strings, `accx25.py`).
- The cause is in the data. `fit_accents.py` only fits an accent that has same-dynamic plain neighbours, and here every neighbour is accented. `build/accent_fits.json` has no entry for Clarinet 1/2, Bassoon 1 or Violoncellos at these onsets (only Vc 536 2.0 and Bn2 545/548). So the notes get only the default mf swell:
  - Clarinet 1 539: vol 1.27 -> 3.02 dB, so +1.75.
  - Violoncellos 539: -3.48 -> -1.74 dB, so +1.74.
  - Both ride the CC11 crescendo, 72 -> 85.
- `chain.py` finds 43 accents with only accented neighbours. Eleven step less than 1.5 dB, and none is fitted.

**Fix.**
- In `tools/fit_accents.py`, add a `--chain` mode. For an accent whose plain-neighbour list is empty, the reference is the 0.30 s before its score onset on the same track (the previous accented note's tail). The target is +3.0 dB over that reference, with the usual caps (winds 4.5, strings 4.5) and `--front-s 0.18`.
- Run it on c24 for the two passages only. Tracks: Clarinet 1, Clarinet 2, Bassoon 1, Bassoon 2, Violoncellos, Horn 1-3. Onsets: 88-97 and 536-545.
- Hand-start values if the tool is not ready, as `[swell, step]` in `build/accent_fits.json`, with the step held to the note end:
  - Clarinet 1 91 / 94 / 539 / 542 / 545: [4.0, 0.5], [3.0, 0.5], [3.5, 0.5], [3.0, 0.5], [2.0, 0].
  - Violoncellos 91 / 94 / 539 / 542 / 545: [3.0, 0.5], [4.0, 0.5], [3.0, 0.5], [4.0, 0.5], [2.0, 0].
  - Bassoon 1 94 / 97 / 542 / 545: [2.0, 0], [2.0, 0], [1.5, 0], [2.5, 0].
- The small step trims keep each note's body above the one before it, so the crescendo still rises through the bar.
- These are level-only changes, so a stem fix is possible.

**Pass.** Every listed onset steps +2..+4 dB on its stem. Master steps at 539 and 542 are +1.5 dB or more, and 91/94 rise to +2.5 or more. 2-5 kHz front minus body stays at +3 or under. Bars 22-25 and 135-138 still rise overall: bar 25 and bar 138 stay the loudest bars of each passage.

## 2. Brass accents peak 0.2-0.5 s after the beat: the weight arrives mid-note (measured; audibility inferred)

**Where.** All accents on the brass tracks played as GENTLE_ACCENT on plain Sus rows. Clearest examples:
- the bar-72 tutti accented quarters (Trombones, Tuba, qn 284-286);
- the bar-131 trombone theme (521, 529);
- the coda trumpet theme (665, 673);
- the bar-135 horns (542, 545, 548);
- Horn 1 100 and 328/330.

**Evidence (measured, `accpt.py`).** Notes at least 0.35 s long within 14 dB of the master; peak = loudest 30 ms frame in score onset +0..+0.6 s; front = 0-0.12 s; mid = 0.15-0.40 s.

| | n | peak time median | p75 | peak after 0.2 s | front - mid |
|---|---|---|---|---|---|
| brass accents | 89 | 0.21 s | 0.28 | 53% | -1.3 dB |
| brass plain | 357 | 0.27 | 0.45 | 62% | -1.5 |
| wind accents | 79 | 0.14 | 0.22 | 27% | -0.1 |
| string accents | 126 | 0.17 | 0.30 | 41% | +0.2 |

- Since c23 (A #1, swell (0.03, 0.15, 0.40)), wind and string accents carry their weight in the front. Brass still uses `swell_s` (0.04, 0.25, 0.6) from c12 (`score_config.py` line 577).
- A brass accent therefore has the same shape as a plain brass note: it swells to a peak in the middle of the note.
- Trombone 1 284 (f, quarter, moved 0.11 s early by ACC_ART_LEAD): the level is -34.7 dB at the beat, -32.1 at +0.1 s and peaks at -30.1 at +0.29 s, then falls 7-9 dB into the next quarter. 285 and 286 have the same shape.
- Latest peaks: Trombone 2 676 0.56 s, Trombone 1 521 0.53, Trumpet 1 673 0.47, Horn 1 100 0.42, Trombone 1 286 0.41, Trumpet 1 665 0.37.
- Brass accents also sit only +1.6 dB (median) over their next plain notes (7 of 18 in 2-4.5 dB).
- Inferred: the bar-72 chords and the coda theme sound like small swells ("bwah") rather than accents.
- The front can get more level without more bite. 2-5 kHz front minus body is -8.3 dB (median), the most headroom of any family, because the Sus MAX attack is dark.

**Fix (test).**
- In `build/score_config.py` (c25 block), give brass the c23 timing: `GENTLE_ACCENT["brass"]` `swell_s=(0.03, 0.15, 0.40)`, `swell_s_leg=(0.03, 0.22, 0.50)`.
- Keep `db` / `soft_db`, plain Sus, no accent sample and no CC11 bump.
- After the render, refit the brass with `tools/fit_accents.py --front-s 0.18 --line-max 5` (skip Tbn1 521/529, as in c17).
- This is MIDI-identical, so a stem fix of the envelope is possible.

**Pass.**
- Brass accent peak time median 0.15 s or earlier, with 30% or fewer peaking after 0.2 s.
- Front minus mid 0 dB or more.
- Accents 2-4.5 dB over their next plain notes for at least 12 of 18.
- 2-5 kHz front minus body median -6 dB or lower, no new brass accent over +3 dB, and the master's 2-5 kHz jump at 568 at +3 dB or less.

## 3. Oboe 1 falling whole steps cross over 0.14-0.26 s late, including the exposed solo in bar 146 (measured)

**Where.** Oboe 1, Leg Slur MAX targets:
- E5 -> D5 at qn 397.5 and 582;
- D5 -> C5 at qn 90, 498, 538 and 555.5.

**Evidence (measured, `xall25.py` / `xdet.py`).**
- Crossovers: 0.14, 0.26, 0.155, 0.23, 0.23 and 0.165 s. They are identical in c23 within 0.005 s, so the lag is deterministic.
- The Oboe 1 median is +0.04 s over 73 joins. These six are the latest, and the two pitch pairs average 0.20 s.
- 582 is the end of the "dolce" oboe solo (bars 145-146; Oboe 1 is the loudest stem there at -2.5 dB re master):
  - the E5 holds until +0.21 s;
  - the D5's harmonics reach their level only at +0.42 s;
  - the stem dips 8 dB at +0.12 s, despite the +5 dB fill at 582.17.
- `LEG_PAIR_EXTRA_S["Oboe 1"]` (line 108) has (73, 72): 0.10 and (77, 75): 0.05 from c19. It has no entry for these two falling whole steps.
- This matches kit LEARNINGS section 5: oboe falling steps are late every time and need pair extras.

**Fix.**
- In `build/score_config.py`: `LEG_PAIR_EXTRA_S["Oboe 1"].update({(76, 74): 0.12, (74, 72): 0.10})`.
- 555.5 follows an eighth, so `LEG_CAP_FRAC` limits its lead to about 0.11 s. Leave it capped.
- After the render, rerun `auto_fills.py` for Oboe 1. Exclude or lower the 582 fill if it overshoots the earlier body.

**Pass.**
- All six crossovers at +0.10 s or earlier, with none earlier than -0.05 s.
- The 582 dip 5 dB or less.
- Other Oboe 1 joins unchanged within 0.02 s.

## 4. Two trumpets as one: the coda theme and the bar-131 a2 on one solo sample +3 dB; Horns 3-4 a2 the same (patch; inferred, memory to check)

**Where.**
- Trumpets 1-2 a2 at 664.5-676 (bars 167-169, ff, the coda theme together with Horns a2 and violas, score page 17). Trumpet 1 sits at -8.6 dB re master there.
- Trumpets 1-2 a2 also at 520-524 (5 notes), 276 and 628.
- Horns 3-4 a2 at 316.5-322 (f, two accented pickup figures) and 628-640.

**Evidence.**
- Measured: `unison_dropped` is Trumpet 2 = 21 and Horn 4 = 18. The kept note gets +10·log10(2) dB, so a doubled line sounds like one louder player.
- Measured: Horn 3 317 and 321 have 2-5 kHz front minus body of +3.9 and +4.0 dB. They are the brightest brass accents after Trumpet 1 284.
- Measured: the Horns a2 track's shelves took 2-5 kHz re mid from -9 to -18.5 dB (c17).
- Measured: the Horns a2 track is idle from 314.5 to 381.5 (`_A2W`).
- Inferred: a recorded two-player sample adds the width and small pitch and timing spread of two players, as it did for the horns (c13).
- My stereo-correlation and partial-width measures did not separate the patches clearly, because the hall dominates. Judge this by ear.

**Fix (test, in this order).**
- (a) No new instance. Route the Hn3 staff's notes at 316.5-322.5 to the existing "Horns a2" track. `TRACK_WINDOWS` needs a per-window staff list, for example `"Horns a2": ([(…), (316.5, 322.5, "Hn3")], True)`, with Horn 3 / Horn 4 excluded in that window. Copy Horn 3's accent fits and trims there, and set the window's level from the render (start: the Horn 3 gain + 4.6 dB, the c13 offset).
- (b) If memory allows, use a lighter variant of the c24 A #3 Trumpets a2 track. Load `2 Trumpets/04 Legato/2TP Leg Slur MAX.oib` alone, not the KS Master. One articulation: disconnected notes play its sustain layer (kit LEARNINGS 5, HO manual 2.1.3), so no keyswitch rows. Use Close + Main mics only, windows 664.4-676.5 and 520-524.5, and Trumpet 1 / Trumpet 2 resting there.
- Copy Trumpet 1's `PICKUP_LIFT` (664.5 6.9, 672.5 6.4), accent fits, `ABUT_LEAD`, the 4 kHz shelf and the climax `loud_eq`.
- Record the footprint. Drop (b) if REAPER settles over 47 GB after the render (c24: 46 GB, 21 compressed).

**Pass.**
- Window levels within 1 dB of c24.
- Horn 3-4 317/321 2-5 kHz front minus body at +1 dB or less.
- Trumpet theme joins under 5 dB.
- 2-5 kHz front minus body on 665/670/673/676 at -1 dB or less.
- Listen once against c24.

## Do not touch

- **Legato and timing:** `LEG_CAP_FRAC` / `LEG_MIN_GAP_S`, the ABUT_LEAD lists, SHORT_SUS_LEAD, `STAC_LEAD_S`, `STR_REST_SHORT`, and the Slur Runs spans. String crossover medians are +0.01..+0.06 s and the joins are clean.
- **Accents:** the c23 wind/string swell shapes and the c24 `LEVEL_SHAPES_S` accent cuts (the 12 cut accents now sit +1.9..+5.6 dB over their next notes). Also brass plain Sus with no accent sample and no CC11 bump: change only the swell timing (finding 2).
- **Re-bows:** AUTO_REBOW times and the re-bow fills, including the 711.855 fill.
- **Other techniques:** the timpani, harp, pizzicato, tremolo, MEAS_TREM and STR_REP_DETACH settings.
- **Patches:** the Horns a2 windows and shelves.
