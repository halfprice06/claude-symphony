# Cycle 6, critic A: articulation and phrasing (render c05, score v600)

Method. All numbers come from the c05 stems and master (`cycles/c05/render`, after the crash / bass-drum stem fix) and from the data as rendered (`cycles/c05/rendered_build/parts.json`). Notes are placed on the tempo map with `tools/pcx.py` (TM). As the caller asked, this report also measures the c05 data against the EastWest template MIDI rules (`mockup-kit/EW-TEMPLATE-PLAN.md` sections 5-8, BRIEF "EastWest template mix") and proposes values for c07.

Measures used:
- **Repeat dip (S1).** Two methods. Harmonic band: `pcx.band_env`, min(peak before, peak after) minus the minimum around the onset. Broadband: 10 ms RMS of the stem, same formula. The harmonic band smears low notes because it uses nfft 8192, so for the basses, celli and low brass I quote the broadband figure.
- **pc (S2).** `pcx.attack_pcx` relative to the score onset. For the percussion and tutti arrivals I also measured the -10 / -6 / -3 dB points of a 2-5 ms RMS envelope relative to the beat.
- **Accent front (item 4).** 2-5 kHz over the first 80 ms minus 2-5 kHz over +0.15..+0.6 s.
- **Phrase shapes (EW sections 6-8).** A phrase is a run of notes on one track with gaps under 0.3 s, at least 2 s long. Measured on the dynamic lane: CC11, or CC1 on `CC1_DYN_TRACKS`. Figures: rise at +0.4 / +0.8 s, taper (value 1 s before the end minus the value at the end), peak position, range, and points per second. Hairpin phrases are reported separately.

"Measured" means a number from the render, parts.json, the score or a patch. "Inferred" means reasoned, not tested.

## Manual notes (cycle 6, slot A: 2021 manual PDF pages 72-74, 116-117, 121-122, read in full; also p.70-71 for the harp's harmonics and Maestro Gliss)

| Manual (PDF page) | Where it applies in the Finale | Does the render follow it? |
|---|---|---|
| p.71-73: Maestro "Gliss" and "Gliss Angelic" slow/fast. One recorded glissando per white key, each with a fixed root and scale (major, minor and modes). | Harp glissando at bar 277: qn 1106-1108, G3 to G6 on C D E G A (B♯ = C, F♭ = E), f < into the ff of 278 | **Follows, by a better route (measured).** No key in the maps has the printed pentatonic tuning. The nearest, E3 "A minor", plays the B and F that the score's tuning removes. `GLISS_SPANS` plays 15 Sus RR notes from 55 to 88, 53-56 ms apart, at v90 -> 112 (the crescendo, under the nail-pick zone at 124). G6 lands at 1108 with the chord, and the notes ring l.v. Keep. |
| p.74: Gliss Angelic descriptions (ethereal, overlapping); keyswitch use of KS Masters | Nothing in the Finale | Not applicable. |
| p.116: crash pairs, three lengths (long / short / even shorter on consecutive white keys from C3), RR x3, velocity selects 7 layers, CC11 and velocity set loudness | Crash at 888 (fff), 1048 (fff, accent), 1108 (fff, accent, tied into the fermata quarter at 1112) | **Partly.** Key 60 (long) at v124 (the top layer) suits the l.v. whole notes. The final stroke is damped after the cut-off (c05 stem fix, kept). But every stroke starts 0.05 s late because of `PERC_MAP` `delay_s` (finding 1). |
| p.117: 22in Zildjian K, "grandiose quality" | Same | The patch choice fits fff arrivals. |
| p.121-122: bass drums. C1 felt short, D1 felt long, E1 felt roll, F1 roll with DXF, G1-E2 felt crescendos, C3-E4 hard-mallet crescendos. 36in Ludwig: "deep, rumbling ... strong woody hit". Velocity up to 12 layers (the patch file: 7). | Bass drum at 888 (ff) and 1108 (ff, accent, tied to 1112). v600 prints no beater. | **Follows** in row and beater: key 38 (felt long), v114. No roll or crescendo is printed, so leaving those rows unused is correct. Same 0.05 s delay (finding 1). |
| p.70: harp "Harmonics" individual patch: fundamental missing, hollow and floating, velocity selects 2 levels | Harp harmonic B♭4 at bar 43 (qn 168, pp) | **No (measured).** `HARM_ON_TRACK = {"Harp": 0}` plays it as an ordinary Sus RR pluck at v46 (finding 6). |

MANUAL-GAPS items in this lens that are still open: #2 (repetition rows: finding 3, Horn 2), #8 (legato velocity on cantabile lines: finding 4), #13 (the bass trombone's B♭1), #12 (felt crescendo rolls). The timpani are on hard sticks throughout, although bar 215 prints "medium sticks" (c05 A #2, deferred). These pages add no new gap.

## Standing checks (c05)

- **Item 4, accents (measured): pass.** Brass 2-5 kHz front minus body, median per span. Più allegro 984-1080: Horn 1 -21, Horn 3 -20, Trumpets 1/3 -16 / -13, Trombone 1 -10, Tuba -15 dB. Final bars: -8..-26 dB. The few positive readings (Horn 3 +18, Trombone 2 +12) are short notes whose body window falls in the decay, not bites.
- **S1, repeats (measured, broadband).** Passing:
  - Basses 7.2 / 7.9 / 8.8 / 8.8 dB median (before the coda, coda, 984-1048, 1048-1080).
  - Contrabassoon 7.6-10.5, Tuba 7.6-10.9, bassoons 7.9-8.8 (harmonic band).
  - Winds 6-9 dB, trumpets 7.0-8.6, Violas 6.2-6.6 in the chorale and 1033-1047.

  Failing: the **celli** (median 3.0 dB before bar 199, 10 of 20 under 3 dB) and **Horn 2 at ff** (finding 3).
- **S2 (measured).** The percussion arrivals are late (finding 1). The celli repeats are still +75 ms median, with 606, 608, 630, 668, 828, 880 and 972 at +116..+250 ms (finding 3). Brass, timpani and tuba at the three climaxes reach -3 dB at +13..+47 ms.
- **Item 7, loops.** No change from c05's critics: the strings are re-bowed, and nothing else is held 6 s or more apart from the crashes.
- **Tremolo (measured).** Every string tremolo mark from 888 on and in 1088-1112 sits on the Tremolo row.

## 1. Crash cymbals and bass drum arrive 50-80 ms after the orchestra at all three climaxes (bars 223, 263, 278; S2; measured)

**Where.** Crash at qn 888, 1048 and 1108; bass drum at 888 and 1108.

**Evidence.**
- In parts.json the strokes sit at 888.0933, 1048.1467 and 1108.12. That is exactly 50 ms after the beat at each tempo, from `PERC_MAP[...]["delay_s"] = 0.05`.
- On the stems the crash starts at +50 ms. It reaches -10 dB of its peak at +95..+98 ms and -6 dB at +98..+104 ms, with its first-150 ms energy centroid at +153..+156 ms. The bass drum reaches -10 dB at +74 ms and -6 dB at +75 ms.
- In the same chords the orchestra reaches -3 dB at:
  - 888: Trumpet 1 +13, Violins I -11, Horn 1 +32, Tuba +25 ms.
  - 1108: Trumpet 1 +18, Violins I +14, Horn 1 +47, Tuba +46, timpani +31 ms.
- So the cymbal lands about 55-85 ms after the brass and strings, and the bass drum about 30-60 ms after. At 112-176 qpm, 40 ms is already audible (S2). These are the three loudest moments of the piece, so the clash reaches the listener as a flam after the chord.
- The delay came from Movement I c03, by analogy with felt timpani ("Delay the crash and tam-tam too"). It was never measured on the crash. This sample needs about 45 ms by itself to rise to -10 dB. The EW research (plan section 7) puts percussion exactly on the grid.

**Fix.**
- `build/score_config.py` `PERC_MAP`:
  - "Crash cymbals": `delay_s` 0.05 -> 0.0, and `lead_s` 0.02 (the crash's -6 dB point then lands at about +30 ms, inside the brass range).
  - "Bass drum": `delay_s` 0.05 -> 0.0 (-6 dB at about +25 ms).
- Keep `PERC_END_AT` and the `_damp` at 1113.2. The note-offs move with the strokes, so they must stay at 1113.2.
- MIDI-only change on two tracks. Afterwards, check the -6 dB point of each stroke against the trumpets' -3 dB point (target within ±25 ms), and check that the master peak at 888 / 1048 / 1108 does not rise (the earlier hit coincides with the brass attack, so check the limiter).

## 2. No phrase shape: the dynamic lanes are flat steps between printed marks (EW plan sections 6-8; measured)

**Where.** Every sustained and legato line. It is worst on the brass (CC1) and clarinets.

**Evidence (parts.json dynamic lanes, 491 phrases of 2 s or more).** In the 150 phrases with no printed hairpin:

| measure | c05 | EW / expert reference |
|---|---|---|
| rise by +0.4 / +0.8 s after the first onset | median 0 / 0 on every track; 0 % of phrases rise 10 or more | about +15 / +25 (CC1 macro scale) |
| taper over the last second | median 0..+5; 0 % taper 10 or more | 13-37 units over the last 0.25-1 s on a quarter to a half of phrase ends (EW); about 20 (hand-played) |
| peak in the middle third (33-62 %) | 0-25 % of phrases (celli 50 %) | 18 of 20 files |
| range within the phrase | median 0 on brass, Clarinets 1-2, Violins I-II; 4-21 on others | 30-60 units on long phrases |
| CC points per second inside phrases | 1.2-6.1 (Clarinet 2 and Trumpet 2 at 0) | 7-13 (EW), 13-44 (hand-played) |
| long notes (1.5 s or more) with a flat dynamic lane | brass 70 %, winds 33 %, strings 26 % (with the volume envelope also flat within 1 dB: 23 / 14 / 11 %) | 0-13 % flat in 15 of 20 files |

The volume envelope gives some level motion, but it acts after the instrument and changes no timbre. On the brass and clarinets the dynamic layer does not move on 70 % of long notes.

**Inferred effect.** Lines sound "programmed": each note sits at its printed level with no push into the middle of a phrase and no release at the end. This is the clearest difference between our data and every expert file. Dan's "mushy" note may come partly from it, because a line with no arch has no clear phrase ends.

**Fix for c07 (new generic option; Movement I's tools have no phrase shaping yet, so the kit has nothing to port).**
- Add `PHRASE_SHAPE` to `tools/score_to_parts.py`. It writes into the dynamic lane (CC11, or CC1 on `CC1_DYN_TRACKS`), or into whichever lane the c07 CC1-macro pass-2 test uses.
- Default None. Finale values in `build/score_config.py`, scaled by `step` = the CC distance from the printed level to the next dynamic up (mf 72 -> f 88: 16):
  - Phrase: notes joined by a slur or by gaps under 0.3 s, at least 2.0 s long. Skip a phrase that overlaps a printed hairpin, fp / sfp / subito or role step. Printed shapes win.
  - Rise: +0.4 step by 0.4 s and +0.7 step by 0.8 s after the first onset (mf: +6 / +11 CC, about +1.5 / +2.8 dB at 0.25 dB/CC). Nothing before the onset.
  - Arch: on phrases over 4 s, the peak at 45 % of the phrase, at +1.0 step at most.
  - Taper: -0.7 step over the last 1.0 s, but never below the printed level minus 0.5 step.
  - Inside slurs: a lean-off of -2 CC per note between 0.4 and 0.8 s after its onset, except on the first 0.15 s of a legato target.
  - Long notes of 1.5 s or more keep moving: a late-peak swell of +0.4 step peaking at 40-60 % of the note when the phrase rule leaves it flat.
  - CC resolution 0.1 s (10 points per second).
- Caps:
  - Brass CC1 at most 108 (above that CC1 brightens fast: kit section 20).
  - Respect `SWELL_CC_CAP`. At CC 40 or below, put the rise in the volume envelope instead, because of the layer boundaries at CC 30-36 (kit section 4).
  - Never above the next printed louder mark minus 8 CC (the existing look-ahead rule).
- Start with half of EW's size measured in dynamic levels (EW's +25 is about 1.5 of our levels). Raise it in c08 if the arches measure under 1.5 dB.
- **Measure in c07:**
  - Per unmarked phrase on the stems, K-weighted level from start to peak 1.5-3 dB, peak at 33-62 %, last second falling 2 dB or more.
  - Join dips and repeat dips unchanged (within 0.5 dB median).
  - 0 WARNING.
  - No new layer jumps: per-note level steps over 4 dB inside a slur.

## 3. Repeated-note gaps against the expert defaults: celli and ff horns merge, the low brass are short of the 98 ms brass median (S1; measured)

**Evidence: c05 MIDI gaps (median ms) and broadband dips.**

| track / row | c05 gap | expert median | dip (median) | under 3 dB |
|---|---|---|---|---|
| Flutes, oboes, clarinets, bass clarinet (Sus) | 60 | winds 63 | 6.2-9.7 | 0-3 per track |
| Bassoons, contrabassoon | 100 | 63 | 7.0-8.8 | 0 |
| Horns 1-3 / Horn 4 | 100 / 140 | brass 98 | 4.9-8.5 | Horn 2: 4 of 22 |
| Trumpets 1-3 | 81-89 | 98 | 7.0-8.6 | 0 |
| Trombones 1-2 | 80 | 98 | 5.8-6.8 | 2 |
| Bass trombone, Tuba | 60 | 98 | 5.5 / 6.8 (harmonic) | 2 / 2 (836, 892, 932) |
| Violins I / II, Violas (Sus) | 45 / 80 / 60 | strings 90 | 5.6 / 7.9 / 7.6 | 1 / 4 / 4 |
| **Violoncellos (Sus MAX)** | **60** | 90 | **3.0** before bar 199 (broadband) | **10 of 20** |
| Double basses (10 ms gap + -5 dB / 0.08 s detach dip) | 10 | 90 | 7.2-8.8 (broadband) | 1-2 per span |

- The **celli** are the weak section. Their f-ff repeats fall at 70, 98, 325, 437, 568-575, 604-608, 630, 658, 668, 710, 828-832, 880 and 972-978. Dips there are 0.9-2.7 dB, and pc runs to +116..+250 ms on 606, 608, 630, 668, 828, 880 and 972, although each has a 170 ms lead. c05's +0.07 s re-tongue lead moved the median by only about 10 ms.
- The basses beside them, with the post-hall detach dip, measure 7-9 dB. Movement I and this loop measured the same thing (LEARNINGS c02): the 150 ms release cap fills a 60 ms gap at low pitch, and the dip does the work.
- **Horn 2** at ff, with a 100 ms gap: 810 / 812 dip 1.3 / 1.0 dB, 442 / 444 1.0 / 1.5 dB, 896 1.5 dB. As c03 measured, the gap is not the answer at ff, because the shipped 237 ms release and the hall fill it. The Trombone 1 repeats at 988 / 996 (1.4 / 3.0 dB) are the same case.

**Fix for c07.**
1. **Celli (generic option exists).** In `build/score_config.py`, add `STR_REP_DETACH["at"]["Violoncellos"] = [(a, b, {"max_qn": 2.0, "same_pitch_only": True}) for a, b in ((64.0, 104.0), (320.0, 330.0), (432.0, 440.0), (560.0, 580.0), (596.0, 672.0), (704.0, 712.0), (824.0, 836.0), (876.0, 884.0), (968.0, 984.0))]`. That is the basses' -5 dB / 0.08 s dip with min_cc 72, so f and louder only. Also raise `STR_REP_NEW_BOW["gap_s"]` to 0.09 on the celli: `"by": {"Violoncellos": {"gap_s": 0.09, "frac": 0.35}}`, which needs a per-track override in `tools/score_to_parts.py` next to `sus_min_s`. Targets: broadband dip median 6 dB or more and pc median under +40 ms on these onsets.
2. **Strings generally (EW strings 90).** Violins I's unslurred Sus repeats (45 ms, 1 of 8 under 3 dB) and Violins II's soft repeats (174.49 and 383.32: 2.1 / 2.8 dB at a 11 ms re-bow gap) are small sets. Leave them unless item 1 shows that the longer gap helps the celli without the dip.
3. **Brass.** In `WIND_REP_RETONGUE_BY`, set the Trumpets, Trombones, Bass trombone and Tuba to `{"gap_s": 0.10, "frac": 0.3, "fall_cc": 10, "fall_s": 0.15}` (EW 98 ms). That moves the low brass from 60 to 100 ms, the size that measured 7 dB on the bassoons in c02.
4. **Horn 2 ff repeats (and Trombone 1 at 988 / 996).** Either the post-hall dip that `WIND_DETACH["by"]["brass"]` already uses (dip_db -5, dip_fall_s 0.05), allowed on re-tongued repeats with a `"dip_db"` key in `WIND_REP_RETONGUE_BY` (a small tool change: the same block as line ~4889), or `REP_ROW` "LegRep RRx4" on Horn 2 at 440-446, 808-814 and 894-898 (MANUAL-GAPS #2; costs a row, and memory is at the limit). Prefer the dip.
5. **Keep** the winds' 60 ms and the bassoons' 100 ms. They are at or above EW's 63, with no dip under 3 dB.

## 4. Legato velocity does not follow the dynamic; the legato overlap is 14 ms against EW's 45-80 (EW plan sections 5, 8; velocity measured, effect inferred)

**Evidence.**
- Legato targets: strings 124 on 899 of 913 targets (correlation with the dynamic 0.11-0.44, all from the 14 exceptions); Horns, Trombones and Trumpets 2-3 at 124; winds 80-100 (Flutes, Oboes, Clarinets p10 80, median 100); Trumpet 1's soft solo 96 (`LEG_VEL_SPANS`).
- Targets at p and below on 124: Violas 18, Violoncellos 17, Violins II 6, Horn 1 35. At mp-mf: Violas 66, Violoncellos 48, Violins II 13, Horn 1 28.
- The experts' legato velocity follows the dynamic (r about 0.35) around a median of 90 or more.
- The string KS Masters' LegatoSpeed maps v30-127 to a sample start offset of 0-4800 samples, so 49.5 samples (1.0 ms) per velocity step (MANUAL-GAPS #8, read from the patch; manual p.144 "allowing the melody to breathe"). v124 -> 96 plays 29 ms more of the recorded transition, and v124 -> 110 plays 14 ms more (inferred arithmetic).
- Overlap: every legato join in the piece overlaps 14 ms (median, all families; `LEG_OVERLAP` 0.04 qn at 168 qpm). Only the p90 of some winds and brass reach 80-134 ms, from caps.
- The joins are on time with this overlap: c05 pcX medians are Violins I +24, Violins II +8, Violas -6, celli +19 ms, with join dips unchanged since c03. HO's legato script crossfades at the new note-on, so the overlap only has to trigger the transition (kit section 5: "0.04 qn worked"). No measured problem comes from the 14 ms.

**Fix for c07.**
- In `tools/score_to_parts.py`, let `LEG_VEL_STRONG` take a dynamic table, e.g. `{"string": [(46, 100), (72, 112), (127, 124)], "brass": [(46, 100), (72, 112), (127, 124)]}`, applied to the target's dynamic-lane value (Trumpet 1's `LEG_VEL_SPANS` 96 stays).
- Compensate with `LEG_VEL_EXTRA_S` string `[(100, 0.025), (112, 0.012)]` and brass `[(100, 0.012), (112, 0.006)]` (the horn script's range is about 50 ms, kit section 20).
- Then refit the per-onset string leads from pcX on the c07 render, because Movement I measured v108 against v124 as identical on Violins I and v105 against v120 as 25-80 ms apart.
- Affects about 300 targets (listed above), mostly the soft viola, celli and Horn 1 lines.
- Measure the transition window (`pcx.pair_window`), pcX and the join dips on those targets.
- **Overlap:** do not adopt EW's 45-80 ms as a rule change. If c07 wants conformance, set a floor of 0.045 s (strings) and 0.035 s (winds, brass) on `LEG_OVERLAP` in seconds. That cannot move any onset, but check for notes overlapping into the same pitch (kit section 5) and for rows where the old note still sounds through a poly row.

## 5. Short notes: the expert lengths (60-90 ms) make no audible difference on HO short rows; velocities are in range; pizzicato is attenuated twice (EW plan section 6; measured)

**Evidence.**
- 558 notes on short rows (Stac DblTng, Staccatissimo, Stac, Marc Shrt, Staccato) are 179 ms long in the MIDI (median; 0.5 qn at 168 qpm), against EW's 60-90 ms.
- In the same render, notes of 89-100 ms and 179 ms on the same row fall to -10 dB at about the same time:
  - Violins I Staccatissimo: 205 against 251 ms.
  - Violins II Stac: 214 against 252 ms.
  - Flute 1: 186 against 170 ms.
  - Oboe 1: 158 against 254 ms.

  The rows play out their samples. The shortening would gain 0-90 ms of -10 dB length, mostly in the hall.
- Brass shorts take v77-88 and wind shorts v82-104 (EW 62-95). Only the wind ff staccatos at v104 sit above it.
- String staccatos (all f-ff here) take v87-95 with CC11 at the printed 88-114. EW parks CC at 118-127 and sets the dynamic by velocity. Velocity selects the layer on HO shorts and CC11 sets volume (DIGEST: p.53, p.64, p.150), so f and ff staccatos share one layer at v87-95.
- Pizzicato at p: v41 with CC11 at 34 (Violins II, Violas, celli, basses, bars 51-66). That is the double attenuation the kit found on the harp (section 3).

**Fix for c07.**
- Leave the short-note lengths. They are not audible, and the stac leads (25-45 ms) are measured, so do not quantize the shorts back onto the grid.
- Optional, low priority: hold CC11 at 110 over the pizzicato spans with velocity unchanged, and take the level back in the volume envelope (`roles.json` pizz rows about -6..-8 dB, refit by stem fix). This is the harp's fix. Measure the pizz attack-to-body ratio and the noise floor in bars 51-66.
- Do not move the string staccatos to velocity-only dynamics until the CC1-macro test settles which lane carries dynamics.

## 6. The harp harmonic at bar 43 plays as an ordinary pluck (manual p.70; measured)

**Where.** Harp, qn 168 (bar 43, pp, the start of the transition over the B♭ pedal): B♭4 (70), v46, 6.6 qn l.v.

**Evidence.** `HARM_ON_TRACK = {"Harp": 0}` keeps the note on the Sus RR track at its sounding pitch. The manual (p.70) describes the Harmonics patch as "hollow, transparent ... the fundamental is completely missing ... a float-like quality". The note is the harp's only harmonic, it is exposed, and c05 deferred it (C #4).

**Fix.**
- Load "Harmonics" (Hollywood Harp, Individual Articulations) as a row of the harp instance if the Sus RR patch can take it, or as a pass-2 track holding this one note. A percussion-size instance costs almost nothing (mvt1 LEARNINGS c14: about 0.01 GB).
- Velocity 60-70 (2 layers), CC11 110. Set the level in the volume envelope to the c05 note's level -3 dB. Pitch: keep the sounding B♭4 if the patch maps harmonics at sounding pitch; check the key map in the .oib first.
- Measure 2-5 kHz minus f0 against the c05 pluck (the harmonic should show a weaker fundamental and a softer attack).

## Proposed c07 values (summary of the EW measurements above)

| EW rule | c05 measured | c07 proposal |
|---|---|---|
| Legato overlap 45-80 ms (strings), 33-58 (winds, brass) | 14 ms everywhere; joins on time | Keep (optional seconds floor 0.045 / 0.035 s) |
| Repeat gaps 60-100 ms (winds 63, strings 90, brass 98, shorts 116) | winds 60, bassoons 100, horns 100-140, trumpets 81-89, trombones 80, B.tbn / tuba 60, strings 10-80 | celli 0.09 s plus the basses' detach dip; trumpets, trombones, B.tbn, tuba 0.10 s; Horn 2 / Tbn 1 ff repeats a -5 dB post-hall dip; keep the winds and bassoons |
| Legato velocity 90 or more, following the dynamic | strings and brass 124 everywhere, winds 80-100 | strings / brass 100 / 112 / 124 at p / mf / f, with velocity lead extras, then refit leads |
| Shorts 60-90 ms, on the grid | 179 ms; leads 25-45 ms | Keep (no audible length change; leads are measured) |
| Short velocities 62-95; string shorts CC parked 118-127 | brass 77-88, winds 82-104, strings v87-95 at CC 88-114; pizz v41 at CC 34 | Pizz CC11 110 test (optional); nothing else |
| Phrase swell +15 / +25 by 0.4 / 0.8 s, taper about 20, arch at 33-62 %, long notes moving, 7-13 points/s | all zero; 1-6 points/s; brass long notes 70 % flat | `PHRASE_SHAPE` at about half of EW's size in dynamic levels (finding 2) |
| Early shift per wind track (-17..-85 ms), percussion on the grid | wind leads 30-50 ms median (measured per note); percussion +50 ms late | Keep the wind leads; percussion delay 0 (finding 1) |

**Do not touch:**
- Wind repeat gaps (60 ms) and the bassoon / contrabassoon re-tongue (100 ms, dips 7-9 dB).
- The basses' detach dips (7-9 dB broadband).
- The brass accents (2-5 kHz front -8..-24 dB under the body).
- The harp glissando route at 277 (`GLISS_SPANS`, v90 -> 112).
- The crash / bass-drum damp at 1113.2.
- The string per-onset legato leads and the per-dynamic release caps.
- The wind "Stac DblTng RRx9" rows and their 0.03 s leads.
- Every tremolo assignment from 888 on.
