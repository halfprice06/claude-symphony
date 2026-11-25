# Cycle 7, critic A: articulation and phrasing (render c06, score v600)

Method. All numbers come from the c06 render (`cycles/c06/render`, after the stem fix) and the data that produced it (`cycles/c06/rendered_build/parts.json`, identical to `build/parts.json`). c06 moved to the EastWest template mix, so the instrument stems 01-31 are now dry and the hall lives in the four return stems 32-35. Articulation is measured on the dry stems. Where the hall matters (repeated notes), I also measured each dry stem plus its whole family return ("dry+return"). That figure is pessimistic, because the return also carries the family's other tracks, but it is closer to what reaches the master than the dry stem alone. Times are placed on the tempo map with `tools/pcx.py`. Velocity layers and controller routings were read from the installed `.oib` patch files with `opus_state.load_oib`.

Measures, as in c06 A:
- **Repeat dip (S1).** Broadband 10 ms RMS: min(peak before, peak after) minus the minimum around the moved onset.
- **pc (S2).** `pcx.attack_pcx`, relative to the score onset. For per-track timing I used detached attacks only: no note of the track sounding at the onset, top note of a chord, re-bow pieces left out.
- **Accent front (item 4).** 2-5 kHz over the first 80 ms minus 2-5 kHz over +0.15..+0.6 s.

This report builds on `cycles/c06/reports/A.md`. Its PHRASE_SHAPE proposal (finding 2) was not built in c06 and stands unchanged, so I do not repeat it. The caller asked for concrete c07 values for repeat gaps, legato velocity by dynamic, short notes and early shifts per track. They are findings 1-4, with a summary table at the end.

## Manual notes (cycle 7, slot A: second reading of 2021 manual PDF pages 89-94, strings, read in full)

The first reading is `cycles/c01/reports/A.md`. Each of its notes is checked here against c06, and one note is new.

| Manual (PDF page) | Where it applies | c01 status | c06 status |
|---|---|---|---|
| p.89-90: DIV A/B patches are one chair per stand, Close mics only. "The loudness of a divisi part is not much less than if the whole section were playing the part". | Vla, Vln I and Vln II div. passages; "div. a 3" at 1108; Vln I "4 soli" 473-488 | Chords on the section patches; half-section colour missing (MANUAL-GAPS #7) | **Unchanged (measured from parts.json).** REAPER sits at 44 GB, so #7 stays deferred. The "4 soli" line is still octave chords on Sus MAX. |
| p.91: Détaché ends cleanly with no legato connection. | Unslurred running notes (Vla, Vln II) | Not used | **Unchanged.** Not used, no change proposed. |
| p.91: Sustain has bow-direction RR, finger position and 3 vibrato levels on CC1. | Every Sus/Leg string note; the sul tasto spans | Sul tasto played with full vibrato | **Followed since c01** (TASTO_CC1 0, LAST_DESK_DB -4). Bow-direction RR reset is still CC36 (MANUAL-GAPS #6). |
| p.91-92: Marcato Sustain adds "extra power at the start". | String accents | Not used; accents had weight without bite | **Still not needed (measured).** String accents 984-1080: front minus body Vln I -10.5 dB median (max -3.9), Vc -10.9 (max -5.5). |
| p.92: Flautando exists in the 2nd Violins only. | "sul tasto, last 2 desks" bar 95 | The Vln II Flautando note lost the row at its hidden re-bow (383.3) | **Followed (measured).** The 383.323 piece now plays on Flautando (REBOW_KEEP_ARTS). Its re-bow dip is 1.3 dB, which is right for a hidden re-bow. |
| p.92: Harmonics exist in the 2nd Violins only, lowest note G4. | Vln I "harm." B♭5, qn 168, pp | Played on Leg Slur MAX, an ordinary vibrato tone | **Unchanged (measured).** Still Leg Slur MAX at v41, 11.5 qn long (finding 6). |
| p.92: Pizzicato is RRx4. | Bars 51-66, 115-122, 171-186 | v41 in each patch's softest layer | **Unchanged.** v41 with CC11 34 is still the double attenuation of c06 A #5 (finding 3). |
| p.93: Bartók, ricochet, col legno, Marcato short, spiccato, MOD combos | None printed | n/a | n/a |
| p.94: Staccato types: plain, on the bow, Marcato MOD, staccatissimo. "All the staccato patches are Round Robin instruments with ... 9–16 sets". | Printed string staccatos | Rows correct; lengths 0.27-0.33 s | **New note (measured, read from the .oib region maps).** Each staccato row has 4 velocity layers (celli 6). The f and ff staccatos at v87 / v95 never reach the top layer (finding 3). |
| p.94: Repetitions are "more realistic than just playing the same staccato note multiple times", with release trails. | The basses' hammered eighths | Not used | **Not needed (measured).** Bass repeats dip 10.4 dB dry and 6.9 dB dry+return (median, 348 repeats). The Violas KS Master holds a "Repetitions TS" row if one is ever needed. |

MANUAL-GAPS items open in this lens: #2 (repetition rows; finding 1 handles the repeats by gap instead), #7 (divisi), #8 (legato velocity: finding 2), #13 (the bass trombone's B♭1). This reading adds one gap: the unused top velocity layers of the string staccato rows (finding 3).

## Standing checks (c06)

- **Item 4, accents (measured): pass.** Brass 2-5 kHz front minus body at printed accents, 984-1080 (dry stems with the new FAMILY EQ):
  - Horn 1 -38.0, Horn 3 -17.8, Trumpet 1 -25.3, Trumpet 3 -23.5, Tuba -23.7 dB.
  - Trombone 1 -6.2 dB, max -0.7. That is the brightest, but still under its body.

  The template's +4..+5 dB family shelves did not turn the accents into bites.
- **S1 and S2:** findings 1 and 4.
- **Tremolo (measured):** unchanged since c05. Every string tremolo mark from 888 on is on the Tremolo row.
- **Item 7:** not re-measured. Nothing in this lens changed the re-bows.

## 1. Repeated notes: the template returns roughly halve the wind and brass repeat dips; low brass and trumpets need the brass gap, the celli still merge (S1; measured)

**Evidence, c06 MIDI gaps and dips (median per track).** "dry+ret" is the dry stem plus its family return.

| track (rows) | c06 gap ms | dry dip | dry+ret dip | under 3 dB (dry+ret) | expert median |
|---|---|---|---|---|---|
| Flutes 1-2 | 89-123 | 8.0-10.3 | 4.3-5.5 | 2-3 | winds 63 |
| Oboes 1-2, bass clarinet | 60 | 6.6-10.6 | 4.6-7.1 | 1-2 | winds 63 |
| Clarinets 1-2 | 123-164 | 5.1-7.0 | 5.4-5.6 | 4-7 | winds 63 |
| Bassoons, contrabassoon | 100 | 9.5-11.7 | 5.3-6.5 | 1-4 | winds 63 |
| Horns 1-3 / Horn 4 | 100 / 140 | 7.1-9.0 / 10.9 | 5.1-6.6 | 0-5 | brass 98 |
| Trumpets 1-3 | 80-89 | 9.5-11.7 | 4.9-5.4 | 1 / 2 / **9** | brass 98 |
| Trombones 1-2 | 80 | 7.2-8.4 | 5.7 | 1-2 | brass 98 |
| **Bass trombone, Tuba** | **60** | 7.0 / 10.7 | 5.8 / 5.7 | **6 / 5** | brass 98 |
| Violins I, II, Violas (Sus) | 92-114 (new-bow strokes 60) | 5.6-7.6 | 6.3-6.6 | 4-11 | strings 90 |
| **Violoncellos** | 50 (new-bow strokes 60) | 6.2 | 6.4 | **9 of 65** | strings 90 |
| Double basses (10 ms + detach dip) | 10 | 10.4 | 6.9 | 11 of 348 | strings 90 |
| String short rows (staccato repeats) | 96-182 | 7.6-15.1 | - | 0-1 | shorts 116 |

- **Winds and brass.** The return takes 3-6 dB off every dip, more than off the strings (their dips hardly move, because the other string sections in the return already fill around them).
  - Trumpet 3's under-3 dB repeats are all in the Più allegro and final bars: 986, 1028, 1038, 1057.5, 1065.5, 1086. So are the low brass's: 832, 860, 892 for both, plus 630 for the bass trombone. Those are the passages where Dan hears whether the brass repeats separate.
  - 588 / 592 show up on every track, but that is the sfp chord, so they are not repeat failures.
- **Celli.** The f-ff Sus MAX strokes at 604, 606, 630, 658 and 828 dip 1.7-3.9 dB dry. Their pc is +121, +170, +178, +155 and +123 ms, plus +144 / +204 ms at 880 / 972, although each has a 170 ms lead. c05 measured the same thing (+116..+250 ms). The attack does not stand out from the release that fills the 60 ms gap, so the estimator, and the ear, find it late. More lead has not helped: c05's +0.07 s moved the median about 10 ms.
- **Horn 2's ff repeats** (c06 A #3.4) are no longer a dry-stem problem. 442 / 444 / 810 / 812 have pc -14..-19 ms, and the ff median dip is 6.7 dB dry.

**Fix (c07 values).**
1. `build/score_config.py` `WIND_REP_RETONGUE_BY`:
   - "Trumpet": `{"gap_s": 0.10, "frac": 0.3, "fall_cc": 10, "fall_s": 0.15}`.
   - "Trombone": gap_s 0.08 -> 0.10 (Trombone 1 already has 0.10).
   - "Bass trombone" and "Tuba": `{"gap_s": 0.10, "frac": 0.3, "fall_cc": 10, "fall_s": 0.15}`. `by_name` is case-sensitive, so "Trombone" does not match "Bass trombone"; give both keys.

   This is EW's 98 ms. The 100 ms gap measured 9.5-11.7 dB dry on the bassoons and horns, against 7.0 dB on the 60 ms bass trombone.
2. `STR_REP_NEW_BOW` (EW strings 90):
   - gap_s 0.06 -> 0.09, frac 0.25 -> 0.3.
   - "tenuto" gap_s 0.07 -> 0.09.
   - "portato" gap_s 0.08 -> 0.09.
3. **Celli.** Adopt c06 A #3.1 as written: `STR_REP_DETACH["at"]["Violoncellos"]` on the f-ff spans (64-104, 320-330, 432-440, 560-580, 596-672, 704-712, 824-836, 876-884, 968-984; `max_qn` 2.0, `same_pitch_only`). That is the basses' -5 dB / 0.08 s post-hall dip, which gives them 10.4 dB dry.

   Also remove `RETONGUE_LEAD_ART_S["Violoncellos"]["Sus MAX"] = 0.07` (back to 0.10 s total). It bought about 10 ms, and once the dip makes the attack visible, a 170 ms lead may put it early (inferred). Refit per onset from the c07 pcX.
4. **Keep:**
   - the winds' 60 ms default (dry+ret 4.6-7.1 dB; EW 63);
   - the clarinets' and flutes' short re-tongue (WIND_REP_RETONGUE_SHORT);
   - the bassoons' and horns' 100 ms, Horn 4's 140 ms;
   - the basses' 10 ms plus dip;
   - the short rows.
5. **Targets on the c07 stems:**
   - brass dry+ret median 6 dB or more, under-3 dB counts halved on Trumpet 3, the bass trombone and the tuba;
   - celli dry dip 6 dB or more at 604-658 / 828, pc median under +60 ms there;
   - the Vln / Vla repeat medians within 0.5 dB of c06 or better.

## 2. Legato velocity is flat (strings and horns 124, winds 100) at every dynamic; EW and the experts follow the dynamic (EW plan sections 5, 8; velocity measured, effect inferred)

**Evidence (legato targets from `pcx.legato_joins`, velocity against the dynamic lane at the target).**

| track | pp | p | mp | mf | f | ff | r(vel, dyn) |
|---|---|---|---|---|---|---|---|
| Violins I | - | 124 (3) | 124 (2) | 124 (54) | 124 (81) | 124 (72) | 0.11 |
| Violins II | 124 (5) | 124 (4) | 124 (3) | 124 (52) | 124 (75) | 124 (61) | 0.20 |
| Violas | 124 (5) | 124 (16) | 124 (38) | 124 (42) | 124 (30) | 124 (75) | 0.22 |
| Violoncellos | 90 (10) | 124 (16) | 124 (27) | 124 (46) | 124 (102) | 124 (85) | 0.44 |
| Horn 1 | 124 (19) | 124 (18) | 124 (11) | 124 (15) | 124 (23) | 124 (55) | -0.22 |
| Trumpet 1 | - | 96 (32) | 96 (3) | 96 (2) | 124 (13) | 124 (26) | 0.86 |
| Flute 1, Oboe 1, Clarinet 1, Bassoon 1 | 100 | 100 | 100 | 100 | 100 | 100 | -0.02..0.29 |

- Overlap: 14 ms median at every join on every track (`LEG_OVERLAP` 0.04 qn). EW uses 45-80 ms on strings and 33-58 ms on winds and brass.
- What velocity does on these patches:
  - Strings: the LegatoSpeed table maps v30-127 to a sample start offset of 0-4800 samples, so about 1.1 ms per step at 44.1 kHz (c06 A, read from the patch; manual p.144).
  - Brass: velocity is the transition speed (manual p.106). The horn script spans about 50 ms (kit section 20). Trumpet 1's v96 solo measured on time with 35 ms less lead (c03).
  - Woodwinds: v80-90 need 20-110 ms extra lead (c04).

**Fix (c07 values).**
- `tools/score_to_parts.py`, the legato-target velocity block near line 3008: let `LEG_VEL_STRONG` take a list of (dynamic-lane value at or below, velocity), read on the target's dynamic lane (CC11, or CC1 on `CC1_DYN_TRACKS`).
  - It currently takes (short, long) = (124, 124).
  - `LEG_VEL_SPANS` (Trumpet 1's 96), `CODA_SOFT` and the sost rules keep priority.
  - The table's floor is 100, because that block's c02 note records strings and horns 220-385 ms late at v60-100.
- Values in `build/score_config.py`:
  - "string": `[(52, 100), (65, 106), (80, 112), (100, 118), (127, 124)]`. About 300 targets change: Vla 21 + 38 at pp-mp, Vc 26 + 27, Vln II 12, Vln I 5, plus every mf / f target to 112 / 118.
  - "brass": the same table. Horn 1's soft lines change most (48 targets at pp-mp).
  - Winds already follow note length (100 under 0.45 s, 80 under 0.9 s, 60 longer; the Cor anglais 100 / 90 / 80), with fitted `LEG_VEL_EXTRA_S` lists. Add only a dynamic term: +8 (to 108) on targets at ff, so loud wind lines change notes cleanly. That is 258 targets across Fl1 91, Fl2 76, Ob1 84, Cl1 82, Bn1 66 and the others.
- Lead compensation in `LEG_VEL_EXTRA_S` (list form, velocity at or below):
  - Strings `[(100, 0.027), (106, 0.020), (112, 0.013), (118, 0.007)]` (1.1 ms per step).
  - Brass `[(100, 0.010), (106, 0.007), (112, 0.005), (118, 0.002)]`.
  - At wind v108 no extra: faster than the v100 the leads were fitted on, so check for early joins.
- **Overlap:** adopt EW's values as a seconds floor: `LEG_OVERLAP` at least 0.045 s on strings and 0.035 s on winds and brass. No onset moves. Check that no overlap runs into a same-pitch note (kit section 5) or into a poly row, and that the join dips stay within 0.5 dB.
- **Measure on c07:**
  - pcX median per section and dynamic: refit the per-onset leads in `leg_leads.json` at 0.6 x the error in c08.
  - `pcx.pair_window` on the changed targets.
  - The join dips. Movement I measured v108 and v124 identical on Vln I, but v105 against v120 25-80 ms apart, so expect the change to show mostly as timing.

## 3. Short notes: velocity does not carry the dynamic (f and ff share a layer, the top layer is never used), and the brass shorts have no lead (EW plan section 6; layers read from the patches, timing measured)

**Evidence.**
- **Velocity layers** of the rows in use, read from each KS Master's region map:

  | row | layers |
  |---|---|
  | Vln I Staccatissimo RRx9 | 1-54 / 55-89 / 90-114 / 115-127 |
  | Vln II Stac RRx9 | 1-55 / 56-91 / 92-115 / 116-127 |
  | Va Stac RRx9 | 1-60 / 61-94 / 95-115 / 116-127 |
  | Vc Stac RRx9 | 1-36 / 37-68 / 69-89 / 90-104 / 105-117 / 118-127 |
  | Cb Staccato RRx9 | 1-54 / 55-85 / 86-116 / 117-127 |
  | 1TP Stac DblTng | 1-54 / 55-75 / 76-94 / 95-127 |
  | 1FH Marc Shrt | 1-62 / 63-109 / 110-127 |
  | FL, OB Stac DblTng | 1-74 / 75-114 / 115-127 |
  | CL, BS Stac DblTng | 1-74 / 75-109 / 110-127 |

  On the string staccato groups velocity drives the source volume and selects the layer. CC11 acts only at instrument level, as volume (Va stac group connections: AHDSR and MIDI velocity to Source/volume).
- **What c06 plays.** String staccatos take v87 at f (CC11 88) and v95 at ff (CC11 114); range 73-113.
  - The basses' f and ff staccatos therefore fall in the same layer (86-116), and the violins' ff ones in the third layer of four.
  - Not one string staccato reaches the top layer.
  - Horn Marc Shrt v77 / 87 / 99 at mf / f / ff all play layer 63-109.
  - Wind staccatos v82 / 96 / 104 all play layer 75-109/114.
  - EW parks CC at 118-127 on string shorts, sets the dynamic by velocity, and uses velocity 62-95 on brass and wind shorts.
- **Lengths.** 179 ms (0.5 qn) against EW's 60-90 ms. c06 A measured no audible difference: the rows play out their samples, and the -10 dB lengths moved 0-90 ms. Still measured, still not worth changing.
- **Timing (pc of detached attacks):**
  - String shorts +2..+13 ms, wind shorts -7..-30 ms (all with STAC_LEAD_S).
  - Trumpet Stac DblTng +29 / +33 / +28 ms, horn Marc Shrt +9..+11 ms, all with no lead. STAC_LEAD_S applies only to the string and wind families (`score_to_parts.py` near line 3425).

**Fix (c07 values).**
- **String staccato velocity by printed dynamic.** Today the velocities are the MIDI source's (f 87, ff 95). Give each string track an `ART_SPANS` entry over 0-SCORE_END on its staccato row (Vln I "Staccatissimo RRx9", Vln II / Va / Vc "Stac RRx9", Cb "Staccato RRx9"), with `"mark": "staccato"` and `"vel_by_cc": [(58, 66), (72, 80), (88, 100), (114, 118), (124, 124)]`. That is the pattern of the winds' `_ww_stac_vel` in the score_config c04 block.
  - Vln I, Vln II and Va: f -> layer 3, ff -> layer 4.
  - Vc: f -> 90-104, ff -> 118-127.
  - Cb: f -> 86-116, ff -> 117-127.
  - Keep CC11 as it is in c07, so the CC1-macro test decides the lane separately. Take the level back with `ROW_TRIM_DB` at ff: start at -3 dB on every string staccato row at CC 100 and above (inferred: the velocity volume scaling is about +1.9 dB for 95 -> 118, plus the louder layer). Refit by stem fix.
  - Measure 2-5 kHz front minus body against the c06 staccatos (no new bite: within +3 dB) and the -10 dB length.
- **Brass and wind shorts:**
  - Leave the horns' Marc Shrt (the top layer 110-127 is the hard marcato; Dan wants weight, not bite).
  - Leave the trumpets' v88 (inside EW's 62-95).
  - Leave the wind staccatos, but cap ff at 104. They already sit inside EW's range except ff, and the top wind layers (110/115+) are untested here.
- **Brass short lead:** allow `STAC_LEAD_S` for the brass family in `tools/score_to_parts.py` (the condition at about line 3425: `family in ("string", "wind", "brass")`), with `STAC_LEAD_S` "Trumpet 1"/"Trumpet 2"/"Trumpet 3" 0.02. Target pc within ±15 ms.
- **Pizzicato** (c06 A #5, optional, unchanged): v41 is right for p (softest layer on every section). The CC11 34 under it is a second attenuation. If tested, hold CC11 at 110 over the pizz spans and take the level in `roles.json` with a stem fix.

## 4. Early shifts per track: the per-note lead tables already put 24 of 28 tracks within ±25 ms; a fixed EW / Polar shift on top would make them early; four tracks and the string slur heads need trims (EW plan sections 7-8; measured)

**Evidence: pc of detached attacks on the c06 dry stems (median, robust SD) against the track's median lead.**

| track | n | pc ms | rSD | lead ms | Polar fixed shift |
|---|---|---|---|---|---|
| Flute 1 / 2 | 211 / 150 | +4 / +4 | 21 / 53 | 35 / 70 | flute -75 |
| Oboe 1 / **Oboe 2** | 182 / 70 | -16 / **-44** (Sus -40) | 35 / 66 | 55 / **120** | oboe -27 |
| Cor anglais | 32 | -10 | 50 | 55 | - |
| Clarinet 1 / 2 | 257 / 170 | -1 / -4 | 30 / 24 | 35 | -38 / -46 |
| Bass clarinet | 56 | -8 | 22 | 35 | -17 |
| Bassoon 1 / 2 | 317 / 212 | -16 / -14 | 28 / 35 | 35 | -40 / -85 |
| **Contrabassoon** | 129 | **-30** | 16 | 35 | - |
| Horn 1 / **Horn 2** | 211 / 103 | -5 / **-25** (Sus -31) | 46 / 43 | 90 | brass -20..-120 |
| Horn 3 / 4 | 173 / 149 | +8 / +10 | 21 / 16 | 50 | |
| **Trumpet 1** / 2 / 3 | 124 / 78 / 115 | **+24** (Sus +25, shorts +29) / +13 / +11 | 26-30 | 50-80 | |
| Trombones 1-2, bass trombone, tuba | 99-138 | +1..+10 | 19-28 | 50-70 | |
| Timpani | 150 | +12 | 6 | -20 (delay) | percussion on the grid |
| Violins I / II | 226 / 287 | +6 / +7 (**slur heads on Leg rows +38 / +26**) | 33 | 35-54 | strings -20..-120 |
| Violas | 289 | +12 | 44 | 40 | |
| **Violoncellos** | 271 | +17 (Sus +24, **slur heads +50**) | 50 | 35 | |
| Double basses | 435 | -1 | 40 | 0 | |

- Our leads (35-55 ms on the winds, 50-90 ms on the brass) are already the size of the Polar shifts. They are fitted per note to the measured attacks, and the result sits on the beat.
- Adding Polar's fixed shifts on top would put the flutes 75 ms and the bassoons 40-85 ms early. **Reject the fixed per-track shift with these numbers.** Compare our median leads with Polar's (oboe 55 vs 27, clarinets 35 vs 38-46, bass clarinet 35 vs 17, bassoons 35 vs 40-85), as the plan asks: they are the same order.
- **Tutti entry spread (Movement I's new default, 36-55 ms seeded).** At the 83 onsets where 14 or more tracks attack together, the pc spread across tracks is already 80 ms from p10 to p90 (median) and 167 ms from first to last. That is wider than the experts' 36-55 ms from first to last.
  - A seeded offset on top would widen it further.
  - **Do not add it on this score.** Record in LEARNINGS that the per-note leads already produce more spread than the expert files.
  - Caveat (inferred): pc measures where each sample's envelope rises, and across families that is not exactly where the ear places the attack. It does not explain away a 2-3x larger spread.

**Fix (c07 values; 0.6 x the error, the loop's usual step).**
- `ENTRY_LEAD_S`:
  - "Oboe 2" (0.0, 0.14, 0.0) -> (0.0, 0.11, 0.0).
  - "Contrabassoon" (0.06, 0.06) -> (0.04, 0.04).
  - "Horn 2" (0.06, 0.08, 0.05) -> (0.04, 0.06, 0.03).
  - "Trumpet 1" (brass default (0.10, 0.05)) -> (0.10, 0.065).
- String slur heads on Leg Slur MAX (first note of a slur, after a rest): `ENTRY_LEAD_ART_S` per track, on top of the string 0.06:
  - "Violoncellos" {"Leg Slur MAX": 0.09}.
  - Violins I +0.02. `by_name` matches by substring, so "Violins I" would also hit "Violins II". Put it under a key that matches only Violins I, or add Violins II at +0.015 too (its heads are +26).
- Trumpet shorts: finding 3 (0.02 s).
- Leave every other lead table as it is. Re-measure this table on c07, because finding 2 changes the legato velocities and finding 1 the repeat gaps.

## 5. Repeated common tones inside div. chords and slur heads after a held note merge with 10-16 ms gaps (S1; measured)

**Where.**
- Violins I / II at 972, 973, 976: Poco più mosso, mf <, div. chords whose G4 / G3 / C4 repeats unslurred while the other voice moves.
- Violins I / II 876: p <, chord repeated.
- Violins I 884: Leg Slur MAX.
- Violins I 896: Tremolo.
- Violoncellos 828 -> 832: the held G♯2 whole note, then the head of the slurred run on the same pitch.

**Evidence.**
- Gaps 10-16 ms, dips 1.6-3.8 dB dry: Vln II 973 1.9, 976 1.6; Vln I 972 3.8, 976 3.5, 884 2.9, 896 2.7; Vc 828 / 832 1.7 / 1.9.
- They sit at mf or above (CC 72-85 at 972-976), so `STR_REP_NEW_BOW` should give them a stroke (stroke_cc mf).
- They keep the 11-16 ms re-bow gap. That suggests the rule skips chord voices, or notes whose chord partner changes pitch (inferred from the data; I did not trace the code path).
- None of these is under a slur in `mockup-events.tsv`.

**Fix.**
- In `tools/score_to_parts.py` `STR_REP_NEW_BOW`, treat a same-pitch repeat inside a chord track as a repeat when that voice is not slurred, whatever the other voice does. Check how `UNI_CHORD_SPLIT` / div handling feeds the rule.
- A slur head that repeats the pitch of the held note before it is a new bow (Vc 832). Same gap as finding 1 (0.09 s, frac 0.3) and the same fall.
- Target: the dips at these onsets of 4 dB or more, with no change at pp-p re-bow points (the hidden re-bows must stay at 11 ms).

## 6. The Violins I harmonic at bar 43 (and the harp's) still play as ordinary tones (manual p.92 and p.70; measured; low priority)

**Where.**
- Violins I B♭5, qn 168 (bar 43, pp, "harm."), 11.5 qn on Leg Slur MAX at v41.
- Harp B♭4 at the same onset (c06 A #6, deferred).

**Evidence.** The manual (p.92) offers harmonics only in the 2nd Violins KS Master, two octaves above the fundamental and no lower than G4, so B♭5 is available. The note is exposed at the start of the transition over the B♭ pedal. Violins II play their own legato note at the same time, so it cannot go to the Vln II instance's row.

**Fix.** One pass-2 track (`build_reaper.py --pass2`) with the 2nd Violins "Harmonics" individual patch, holding the Vln I note at 168 and, if that patch's key map allows, nothing else. Add the harp harmonic as the harp "Harmonics" patch on a second small pass-2 instance. Memory: a one-row instance is about 0.01-0.7 GB (mvt1 LEARNINGS c14), so check the 45 GB ceiling first. Level: the c06 note -3 dB, refit by stem fix. Do it only after findings 1-5.

## c07 values summary

| item | c06 measured | c07 value |
|---|---|---|
| Repeat gaps | winds 60-164, bassoons and horns 100, trumpets 80-89, trombones 80, B.tbn / tuba 60, string strokes 60, Vc 50, Cb 10 + dip; dry+ret dips 4.3-7.1 | trumpets, trombones, B.tbn, tuba 0.10 s / frac 0.3 / fall 10 CC; STR_REP_NEW_BOW 0.09 s / frac 0.3 (tenuto, portato 0.09); celli detach dip spans + Vc Sus MAX extra lead off; keep winds 0.06, bassoons / horns 0.10, Hn4 0.14, Cb 10 ms + dip |
| Legato velocity | strings / horns 124, Tpt1 solo 96, winds 100 at every dynamic | strings and brass (52:100, 65:106, 80:112, 100:118, 127:124), floor 100; winds keep the length rule, ff targets +8 (108); lead extras strings 1.1 ms / step, brass 0.4 ms / step |
| Legato overlap | 14 ms everywhere | floor 0.045 s strings, 0.035 s winds / brass |
| Short notes | strings v87 f / v95 ff (top layer unused), 179 ms, string / wind leads 25-45 ms; trumpets +28..+33 ms with no lead | string staccato velocity (58:66, 72:80, 88:100, 114:118, 124:124), ROW_TRIM_DB -3 dB at CC 100+, refit by stem fix; lengths unchanged; brass STAC_LEAD_S (Trumpets 0.02); winds and horns unchanged |
| Early shifts | 24 of 28 tracks within ±25 ms; tutti spread already 80 ms p10-p90 | no fixed per-track shift and no seeded tutti spread (measured rejection); Oboe 2, Cbn, Horn 2, Trumpet 1 entry leads and string slur-head leads trimmed as in finding 4; percussion stays on the grid |

**Do not touch:**
- The basses' 10 ms gap plus detach dip (10.4 dB dry, 6.9 dry+return).
- The bassoon, contrabassoon and horn re-tongue at 100 ms (Horn 4 140).
- The wind staccato rows and their 0.03 s leads.
- The string staccato rows and leads (+2..+13 ms).
- The brass accents (front -6..-38 dB under the body).
- The hidden re-bow gaps (11 ms, Flautando kept at 383.3).
- Every tremolo assignment from 888 on.
- The harp glissando at 277.
- Percussion on the grid with the crash's 0.02 s lead.
- The per-onset string legato leads (refit them, do not discard them).
