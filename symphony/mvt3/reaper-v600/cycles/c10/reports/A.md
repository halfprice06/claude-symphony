# Cycle 10, critic A: articulation and phrasing (render c09, score v600)

Method. All numbers come from the c09 render after its stem fix (`cycles/c09/render`: dry stems 01-31, returns 32-35, `00_Master.wav`) and the data that made it (`cycles/c09/rendered_build/parts.json`, `build/mockup-events.tsv`). Times use the parts.json tempo map (`tools/pcx.py` TM). Scripts were in `/private/tmp/claude-501/mockup-loop/mvt3-c10-A/` (deleted after the report). "Measured" means a number from the render, parts.json, the events file, ks_maps.json or a score source. "Inferred" means reasoned but not tested. Measures:
- **Repeat dip (S1):** the note's harmonic band (`pcx.band_env`, 2 ms hop) on the dry stem and on the master: min(peak in -0.2 s..the moved onset, peak in +0.03..+0.25 s) minus the minimum in -0.06..+0.06 s around the onset. A repeat is two same-pitch notes of one track with no other onset of that track between them and a played gap under 0.2 s.
- **Legato join time (S2):** `pcx.attack_pcx` on every join `pcx.legato_joins` returns, relative to the score onset.
- **Brass accent tilt jump:** on the master, once per accented brass onset (98): 2-5 kHz level over the first 80 ms minus the 200 ms before, minus the same jump at 0.25-1.5 kHz (LEARNINGS c08).

## Manual notes (cycle 10, slot A: second reading of 2021 manual PDF pages 108-113, woodwinds, read in full)

The first reading is `cycles/c04/reports/A.md`. Each of its notes is checked against c09. The pages are text only; row facts come from `~/.rpr-bridge/libs/ew_ho/ks_maps.json`.

| Manual (PDF page) | Where it applies | c04 status | c09 status |
|---|---|---|---|
| p.108: Flute 2 is a different player in another seat; no samples shared with Flute | Flute 2 doubles Flute 1 through the F1 theme (bars 27-34, 151-164) and the Più allegro | own patch (FL2) | **Patch yes; timing no (measured, finding 2).** Flute 2 takes Flute 1's leads. On the same 122 doubled joins Flute 2 lands a median 7 ms later, IQR -18..+60 ms, 31 joins more than 60 ms apart. |
| p.108: one oboe, clarinet and bassoon player; 3 Clarinets / 3 Bassoons are new ensembles | Oboe 2, Clarinet 2 and Bassoon 2 unisons | unisons dropped, +3 dB (UNI_BOOST) | Unchanged: Oboe 2 50, Clarinet 2 52, Bassoon 2 76 notes dropped. A level question (B); not ranked. |
| p.109: sustain dynamics on the Mod Wheel; all three layers sound together | every wind sustain | follows (CC11 dynamics, CC1 Non Vib/Vib; CC1 dynamics on CL/BC) | Follows. |
| p.109: **Sus Expressive**: slower attack, vibrato that grows | the exposed solos: Oboe 1 "solo, espress." bar 95 (376), Bassoon 1 "solo, espress." bars 115-125 (456-500), Cor anglais "dolce cantabile" bars 171-186 (680-744), Oboe 1 / Bassoon 1 bar 187 (744) | not used (Bassoon 1 CC1 ramp instead) | **Still not used (MANUAL-GAPS #5, never tried in any movement).** All these solos play Leg Slur MAX. Rows present: "Leg Slur Exp" OB 35, EH 35, BS 77; "Sus Exp Vib" OB/EH/BS 30. Finding 4. |
| p.109-110: Legato Repetitions (LegRep RRx4) | wind repeats | not used; S1 passes | **Not needed (measured).** Wind and brass repeats: stem medians 6.0-13.6 dB, master 3.4-9.8 dB. Lowest on the master: Contrabassoon 3.4 (9 of 27 under 3 dB), under the basses' eighths. |
| p.110: shorts have no release trails; hold the notes so the room rings | 776 printed staccatos | only Bassoon 1 on the staccato row | **Follows since c04 (measured).** Flute 1 45, Flute 2 22, Oboe 1 38, Clarinet 1 26, Bassoon 1 55 staccatos on "Stac DblTng RRx9"; horns on Marc Shrt; trumpets on Stac DblTng. Played length 0.50 of the slot (0.35 at the shortest); the batch-7 research says 0.50-0.62. Still on Sus/Leg slices: Bassoon 2 14, Clarinet 2 6, Bass clarinet 6, Contrabassoon 6, Cor anglais 6, Oboe 2 3. Too few to rank. |
| p.110: Shorts MOD SPEED | none | n/a | n/a |
| p.111: runs, trills, flutter, repetition patches (Rep Med 145 / Slw 120 on OB, BS) | no fast wind repeats or runs; the grace run into bar 35 | n/a; violin grace notes missing | **Fixed:** Violins I and II now play all three grace notes at 135.244 / 135.496 / 135.748, as the winds do. |
| p.112: legato only with no gap and within an octave; mono unless CC22 0-63 | every wind and brass legato row | follows | **Follows (measured).** 0 chords on a legato row, 0 legato joins over 12 semitones, no CC22. |
| p.112: Legato Slur Repetitions | slurred wind repeats | not used, not needed | Not needed (S1 above). |
| p.112-113: Slur Runs; KS Masters | no runs; every row change | n/a; follows | Keyswitch leads 7-12 ms; the 40-800 ms research default was rejected with numbers in c09 (LEARNINGS). No wrong-row note found in this render either. |
| Not on these pages, but it decides how slurs sound: velocity sets transition speed | wind legato targets | v80/v90 targets 100-190 ms late | **Mostly fixed by c07's velocity-by-dynamic (floor 100).** Wind v100 medians -8..+28 ms. But 158 of 1562 wind, horn and trumpet joins are still later than +80 ms or earlier than -60 ms (finding 2). |

## Standing checks and the coordinator's items

- **Wetness (measured; the claims hold, and the mix is not too dry).**
  - Tutti cut-offs at qn 5 / 21 / 661 / 1113, measured from the last point within 3 dB of the held level: -20 dB in 0.39 / 0.39 / 0.35 / 0.36 s.
  - Measured from the written cut-off: 0.47 / 0.46 / (661 is held past the beat) / 0.42 s.
  - Final chord RT60 from the -10..-30 dB slope: 1.23 s (claimed 1.26).
  - This is inside the ceiling (0.50 s, 1.5 s). Measured from the written end it sits at the dry end of the recordings (Brahms 1/i 0.43-0.55, Dvořák 0.50-0.58 s). Drier than that would be too dry; this is not.
- **The c09 "plain" 90 ms string gaps, stem against master (measured).** In the master the hall and the other parts fill the gaps on violas and Violins II, as Movement I c51 found:

  | section | stem median | master median | repeats |
  |---|---|---|---|
  | Violas | 5.3 | 3.8 | 36 |
  | Violins II | 5.7 | 5.0 | 6 |
  | Violins I | 5.4 | 8.7 | 4 |
  | Violoncellos | 1.8 | 6.7 | 3 |

  - The violas' chorale repeats at 888-984 dip 11.2 dB on the stem and 3.7 dB on the master.
  - The gaps do separate on the master where a section is exposed. Where it is not, the next gain in S1 is in the basses (finding 1), not in longer gaps on the upper strings.
- **Inner held notes under a tune (measured).** Held wind and brass notes of 1.5 qn or more under a printed diminuendo, level re master:
  - None sits within 4 dB of the master except Horn 1 at 971-973 (-1.7 dB) and Bassoon 1 at 484 (+0.4). Both carry the line there: Horn 1 in bars 243-245, Bassoon 1 in its solo.
  - I found no case like Movement I's Horn 3.
- **Horns' soft passages, weighted (measured, B's lens).** A-weighting widens the gap; it does not close it. The 315 Hz bell left the soft horns too low.
  - Horn 1 pp at 264-300 (bars 67-75): A-weighted -59.4 dB. That is 17.3 dB under Violins I (-42.1) and 20.8 dB under the master (plain RMS 10.9 under Violins I).
  - At 744-760 Horn 1 (dolce) is 3.2 dB A under Oboe 1. That is fine.
  - I did not measure the 315 Hz hump (C's lens).
- **Brass accents, tilt jump (measured).** Median -0.2 dB, p90 +3.1, maximum +6.2 (qn 56). That is at the +3 target. Front minus body at 2-5 kHz on the master: median -1.7, p90 +1.3. No accent bites.
- **Item 7, loops (measured).** Master fold at 3.95 s (100-300 Hz band / centroid): chorale 888-936 -0.01 / -0.07, final bars 1088-1112 0.17 / 0.08. Stems all under 0.25, except the tuba's band at 1088-1112 (0.58 on the stem, 0.17 on the master). No pulsing.

## 1. The basses' hammered eighths run together in the master: half of them dip under 3 dB (S1, S2; measured, fix measured on Movement I)

**Where.** Double basses, the hammered eighths:
- coda bars 199-210 (qn 792-840);
- Più allegro bars 247-270 (984-1088);
- Largamente bars 273-277 (1088-1108).

All are Sus MAX at f-ff inside the `STR_REP_DETACH` spans.

**What is wrong.**
- Each eighth plays 0.47 qn, so the gap before the next eighth is 8-12 ms. Separation comes only from the -5 dB / 0.08 s volume dip.
- The c09 `STR_REP_NEW_BOW["plain"]` 90 ms gap excludes the detach spans, so the basses never got a real gap.
- On the stem the eighths separate. In the master the basses' own harmonic band hardly moves, because the celli, timpani, tuba and the returns fill the dip. In the 30-140 Hz band the basses carry only 20-41 % of the energy in these spans; the celli carry 15-50 % and the timpani 5-36 %.

**Evidence.** Repeat dips in the basses' harmonic band:

| span | repeats | stem median | master median | master under 3 dB |
|---|---|---|---|---|
| 792-840 | 82 | 7.3 | 2.7 | 47 |
| 984-1088 | 177 | 5.7 | 3.1 | 86 |
| 1088-1108 | 39 | 3.9 | 2.2 | 26 |

- Before on-beat eighths the stem dips only 2.6-5.0 dB. Before off-beat eighths it dips 6.9-13.8 dB.
  - 816-840: 2.7 on the beat, 11.1 off it.
  - 1088-1108: 2.6 on the beat, 13.8 off it.
- So the off-beat eighth runs into the next downbeat. That is the long-short lilt the c09 actor measured as an attack-time swing: -68 ms at 1088-1108 and -30 ms at 816-840, which the CC16 resets did not remove.
- Movement I c51 had the same patch, the same dip and the same 14-19 ms gaps (`symphony/mvt1/reaper-v621/cycles/c51/CHANGES.md`). It gave the strokes real gaps of 77-80 ms and cut the dip to -3 dB:
  - the basses' master band dips went 2.7 -> 3.5, 4.2 -> 8.3 and 2.8 -> 3.0 dB;
  - the downbeat fronts went from 1.5-6.6 dB under the off-beats to 0.8-4.0 dB over them;
  - "the REP_SPLIT gaps and the -3 dB detach dip, not a layer change, fixed the weak downbeats" (Movement I LEARNINGS c51).
- Movement I also found that no other row articulates these eighths: Detache, Marc Shrt and Marc Sus LITE all failed (LEARNINGS c13, c22, c50).

**Fix.**
1. Port Movement I c51's `REP_SPLIT` gap keys into `tools/score_to_parts.py`: the branch at mvt1 lines 2852-2861, the `rep_split_gaps` output, and the comment block at mvt1 631-635. Let it act inside `STR_REP_DETACH` spans as it does on Movement I's basses.
2. `build/score_config.py`: `REP_SPLIT = dict(REP_SPLIT, gap_s=0.08, frac=0.35, gap_min_s=0.06, gap_min_cc=DYN["mp"])`.
   - The Finale's eighths then end 0.063 s early at 168 qpm (slot 0.179 s), 0.060 s at 176 qpm, and 0.073 s in the Largamente (144 qpm).
3. Set the basses' detach dip to -3 dB on the spans (792, 840.25) and (984, 1108.25): a per-span `{"dip_db": -3.0}` in `STR_REP_DETACH["at"]["Double basses"]`, as Movement I did.
4. Movement I c51's gaps cost 0.3-0.65 dB per slot. Add +0.5 dB `LEVEL_SHAPES` rows over the same spans (Movement I's `_lv51`).
5. Refit the basses' `METRIC_BOWED_DB_SPANS` tables after the render. This is a new stroke layout, which is the case the c09 lesson ("do not refit without a new reset layout") allows.
6. Leave the Contrabassoon's quarters (master dip 3.4) alone until this is measured. They double the same band.

**Targets.**
- Master harmonic-band dip median 4 dB or more in each span, with fewer than a quarter of repeats under 3 dB.
- Stem on-beat dips of 5 dB or more.
- On-beat minus off-beat attack within ±12 ms.
- Down minus off level +2..+4 dB after the refit.

## 2. Flute 2 lands up to 190 ms behind Flute 1 on the doubled theme; the slur-start joins carry one lead for two players (S2; measured; manual p.108)

**Where.**
- Flute 1 and Flute 2 in octave/unison doubling: the counterstatement bars 27-34 (qn 104-134); the recapitulated F1 heads bars 151, 155, 159, 163 (602, 618, 634, 650); the Più allegro 1007, 1059, 1067, 1070-1074.
- Isolated late joins in Bassoon 1, Oboe 1, Horn 1 and the cor anglais.

**Evidence.**
- Flute 2 legato joins: median +32 ms (Flute 1 +8); 28 of 128 later than +80 ms.
- On the 122 joins the two flutes share, Flute 2 minus Flute 1 has median +7 ms and IQR -18..+60 ms; 31 joins differ by more than 60 ms.
- The worst are the **slur-start joins**: the second note of a slur whose head was tongued on Sus. `tools/score_to_parts.py` gives every track the same `SOST_JOIN_LEAD_S` 0.12 s for these (branch at about line 3793; `leg_leads.json` rows do not reach it).
  - Flute 1: 35 such joins, median **-36 ms**.
  - Flute 2: 26 joins, median **+45 ms**.
  - At 602 / 618 / 634 / 650 / 1007 / 1074, Flute 1 lands -70 / -22 / -70 / -65 / -63 / -70 ms and Flute 2 +89 / +192 / +105 / +192 / +136 / +89 ms. On the held head notes of the ff F1 recap that is a flam of 160-260 ms between the flutes.
- Bars 27-34: Flute 2's ordinary v100 joins land +100..+124 ms at 106.5, 107, 107.5, 117, 120.5, 127, 131.5, 133.5 and 134. Flute 1's land at -32..+64 ms on the same notes.
- Manual p.108: Flute 2 was recorded by a different flautist. The leads were fitted on other players and carried over unchanged.
- Other outliers (later than +80 ms):
  - Bassoon 1: 748 +350, 756 +188, 845 +147, 466 +129 ms.
  - Oboe 1: 188 +189, 758 +185, 749 +168, 1014 +162 ms.
  - Horn 1: 51 +223, 87 +189, 970 +162 ms.
  - Cor anglais: 692 +115, 702 +134, 738 +118 ms.
- Across winds, horn and trumpet, 158 of 1562 joins fall outside -60..+80 ms.

**Fix.**
1. `tools/score_to_parts.py`: let `SOST_JOIN_LEAD_S` be a per-track dict through `by_name`, so the slur-start branch reads the track's value. Keep the 0.45 × first-note cap.
2. Also let `leg_leads.json` rows apply in that branch. Today they are read only for legato targets (c48 lesson: route each row to the path its note takes).
3. `build/score_config.py`:
   - `SOST_JOIN_LEAD_S = {"Flute 1": 0.085, "Flute 2": 0.16, "default": 0.12}`. These are the medians -36 / +45 ms moved to 0; the cap holds Flute 2 under 0.45 of a quarter.
   - Add a Flute 2 legato lead of +0.02 s (its v100 median +25 against Flute 1's +8) through `LEG_VEL_EXTRA_S["Flute 2"]` as `[(100, 0.02), (80, 0.06), (60, 0.10)]`.
4. `build/leg_leads.json`: rows for every wind or horn join outside -60..+80 ms in this render (the list is above).
   - Size each at 0.8 × the error, clamped to ±0.08 s (Movement I c48: median |error| 71 -> 30 ms on 108 rows).
   - Check each row's realised shift in parts.json before rendering.

**Targets.**
- Flute 2 minus Flute 1 on shared joins: IQR within ±30 ms.
- Slur-start join medians within ±20 ms on both flutes.
- No join in the listed solos beyond +80 ms.

## 3. The timpani play the soft-stick and medium-stick passages on the hard-stick patch; the score's stick changes never reach the events file (measured in the data; audible effect partly measured)

**Where.** Timpani:
- 680-712: "soft sticks" in the rest at bar 171; the pp "near the rim" motive x at 708-711.
- 856-1016: "muta D♭ in C / medium sticks" in the rest at bar 215, then "hard sticks" in the rest at bar 255. This covers the sub. p roll into the arrival (872-888), the arrival roll (888), the chorale strokes and roll (912-933), the p < f roll (970-984) and the Più allegro strokes (984-1012).

36 notes in all (4 + 32).

**What is wrong.**
- `symphony/mvt3/v600/sections/recS.ily` line 170 prints "soft sticks", and `codaTwo.ily` line 64 prints "medium sticks" (the comment in `intro.ily` line 54 explains the plan).
- `build/mockup-events.tsv` has neither: the extraction drops text attached to a full-bar rest. It keeps only "near the rim" (708) and "hard sticks" (711).
- So BRIEF's "4 timpani (hard sticks ...)" and every events-based check miss the changes. All 179 timpani notes play `Timpani Hrd KS`.
- c01 added a darker switched EQ (`mix.json` Timpani `loud_eq`: 1.5 kHz shelf -6 dB at 707.5-711.5 and 871.5-985) as an interim. It stops at 985, not 1016.
- c01 C #6 and c05 A #2 asked for a felt pass; both were deferred for memory.

**Evidence (c09 timpani stem, 1-8 kHz share of the stem).**

| passage | stick printed | 1-8 kHz share | level |
|---|---|---|---|
| sub. p roll 872-888 | medium | -12.9 dB | -38.8 dB |
| 223 roll | medium | -13.8 dB | -35.0 dB |
| p < f rolls 968-984 | medium | -16.4 dB | |
| f rolls 1040-1048 | hard | -10.3 dB | |
| fff rolls 1088-1100 | hard | -13.9 dB | |

- With the interim EQ, the "medium" rolls are as bright as the hard-stick fff rolls.
- Movement I's felt rolls measured -38 (ppp) to -22 (f) dB on the same share (Movement I LEARNINGS c12).
- Manual p.123: felt rolls have a blended timbre because the individual attacks are less strong.
- Inferred: the soft rolls under the chorale and before the arrival sound like a hard-mallet rumble with audible strokes, which is what Dan's rule about rolls is aimed at.

**Fix.**
1. Preferred: a "Timpani felt" alias in the second pass on `Timpani Flt KS.oib`. Movement I's `ALIAS_TRACKS` / `PASS2_TRACKS` / `build_reaper.py --pass2` / `render_cycle.py N --pass2` are already in tools/.
   - `TRACK_WINDOWS = {"Timpani felt": [(679.9, 711.9), (855.9, 1015.9)]}`. Both windows start and end in the timpani's full-bar rests (Movement I c49 lesson). The main Timpani rests inside them.
   - Use Movement I's felt `TIMP_CC1_MAP` / `TIMP_ROLL_TRIM_DB` for the alias, `TIMP_ROW` with the Flt row names, and `HP_CURVE` skip_staves as now.
   - Diff the alias's parts.json against the source first (mockup-kit `pipeline/alias_check.py`).
2. Until then, extend the switched EQ's second window from 985 to 1016.
3. Teach `build/mockup.ly`'s event dump to keep text on multi-measure rests, so stick, mute and "muta" changes appear in mockup-events.tsv. Check the trumpets' "togli sord." at bar 185 the same way; it is also in a rest.

**Targets.**
- 1-8 kHz share in the medium windows at least 6 dB under the hard f rolls.
- Level per roll within ±1.5 dB of c09: the B balance and Dan's settle rule stay as they are.

## 4. The exposed espressivo wind solos have no expressive attack or growing vibrato; the library's Exp rows were never tried (inferred; manual p.109, MANUAL-GAPS #5)

**Where.**
- Bassoon 1 "solo, espress." bars 115-125 (qn 456-500, pp strings only): 23 notes.
- Cor anglais "dolce cantabile" bars 171-186 (680-744, the duet with the muted Trumpet 1): 41 notes.
- Oboe 1 "solo, espress." bar 95 (376-392, over the last desks' sul tasto) and "1. dolce" bar 187 (744-760).

**What is wrong.**
- All of them play Leg Slur MAX, with vibrato only from the CC1 Non Vib / Vib crossfade.
- Manual p.109: Sus Expressive "adds an expressive feel to the notes with a slower attack and a gently increasing vibrato".
- The KS Masters hold "Leg Slur Exp" (OB key 35, EH 35, BS 77) and "Sus Exp Vib" (OB, EH, BS key 30). All are unloaded.
- No movement has tried them (MANUAL-GAPS #5, "Tried: never"). These are the three most exposed wind solos in the Finale, and the reading row for this cycle is these pages.

**Fix (A/B, one row per track).**
- `build/score_config.py` `ART_SPANS`:
  - Bassoon 1 `{"from": 455.9, "to": 500.0, "art": "Leg Slur Exp"}`;
  - Cor anglais `{"from": 679.9, "to": 744.0, "art": "Leg Slur Exp"}`;
  - Oboe 1 `{"from": 375.9, "to": 392.0, "art": "Leg Slur Exp"}` and `{"from": 743.9, "to": 760.0, ...}`.
- Hold CC1 at the current shape.
- Each track loads one more row: about 0.1-0.3 GB each (inferred), three tracks, with a full rebuild.
- If memory blocks it, render the three windows as one pass-2 alias each.

**Measure.**
- Vibrato modulation depth (pitch band, 4-7.5 Hz share) over the first 1 s of each held note against c09.
- Attack rise to -6 dB of the body.
- Join times with `pcx` (the slower attack may need +0.03-0.05 s more lead, with the finding 2 tables).
- Level against the accompaniment within ±1 dB.

Keep the row only if joins stay within ±40 ms and the level is unchanged.

## 5. Slurred tenuto (louré) chord repeats keep a 25 ms gap: violas bars 211-218 dip 2-4 dB on half the notes (S1; measured)

**Where.**
- Violas div. chords, Largamente bars 211-218 (qn 842-866): 16 slurred pairs, each pair two tenuto half notes under one slur, ff then f.
- Also Violoncellos 980-983 and Violas / Violins II 362 / 366.

**What is wrong.**
- The second note of each slurred pair plays after a 0.06 qn (25 ms) gap. The `STR_REP_NEW_BOW["portato"]` 0.09 s gap and CC fall do not apply, because the repeats are two-note chords on Sus MAX, not merged notes.
- The slur-boundary repeats (844, 856, 860, 864, 868) do get the "plain" 90 ms gap.

**Evidence.**
- In-slur repeats: stem dips 2.3-8.4 dB, median 3.8; master 1.5-8.8, median 2.5.
  - 842 (C♯4): 3.2 / 1.9; 850 (F♯4): 2.3 / 1.5; 854 (A♭4): 2.4 / 2.5; 858: 3.4 dB on the stem.
- The plain-gap repeats beside them dip 8.4-13.9 dB on the stem.
- The louré pulse is the printed figure; a 2 dB dip on the master is not heard as a pulse.

**Fix.**
- `tools/score_to_parts.py`: let `STR_REP_NEW_BOW["portato"]` (gap 0.09 s, fall_cc 10 / 12, fall_s 0.06) also act on same-pitch chord repeats under one slur whose notes carry tenuto. The "chord" option already does this for non-legato next rows; extend it to the portato case.
- Keep the "change bow at will" skip spans (864-884 on Vln I/II, Vc, Cb).

**Target.** In-slur louré dips of 5 dB or more on the stem and 3 dB or more on the master, with each pair's second note within 1.5 dB of its first.

## 6. "div. a 3" at the final chord is still read as three full sections per staff (measured in the data; level effect inferred; carried from c09 A #6)

**Where.** Violins I, Violins II and Violas at qn 1108 (bar 278, fff tremolo, "div. a 3").

**What is wrong.**
- `div_entries` lists nothing at 1108. The last entries are Violins I 968, Violins II 968 and Violas 1085.
- Violins I plays 84 / 88 / 91 at velocity 127 on Tremolo: three full-section tremolos instead of three thirds.
- c09 neither took nor rejected this (HISTORY c09).

**Fix.**
1. Make the div parser in `tools/score_to_parts.py` read "div. a N" and take -10·log10(N) (-4.8 dB) per voice, as it does for "div.".
2. Move the family difference into `roles.json` at 1108 so that the climax order (278 loudest, then 223) and FINAL_RING's fall are unchanged.
3. Check the final chord's string-to-brass balance against c09 (B's lens).

Low cost; the gain is texture (inferred).

**Do not touch:**
- The legato rules: mono, no wide joins, no CC22, the overlap floors, velocity by dynamic with floor 100.
- The wind and brass staccato rows at 0.50 of the slot.
- The wind / brass re-tongue repeats (stem medians 6.0-13.6 dB).
- The c09 "plain" 90 ms gaps on the upper strings.
- The muted Trumpet 1 on Mute Sus (cor anglais minus trumpet median -12 ms) and the open solo.
- The stopped horns on Stop Sus.
- The grace runs into bar 35 (now complete on all four staves).
- The brass accent swell (tilt jump p90 +3.1, no bite).
- The re-bow layout (no loop fold over 0.25 on the master).
- The tremolo rows.
- FP_SPIKE_AT_MARK.
- The returns and envelope: tutti -20 dB in 0.35-0.39 s from the last held point, 0.42-0.47 s from the written cut-off; RT60 1.23 s.
