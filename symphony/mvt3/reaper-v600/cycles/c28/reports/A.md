# Cycle 28, critic A: articulation and phrasing (on the c27 render)

Sources: the c27 stems and master (`cycles/c27/render/`), `cycles/c27/parts_rendered.json`, `role_moves_over_1qn.txt`, `logs/guard27_final.txt`, the c26 stems and parts for before/after, the c16 and c22 masters (tempo maps from `c17/before/parts.json` and `c23/before/parts.json`), `build/mockup-events.tsv`, `build/score_config.py`, `build/mix.json`, the score PDF (pages 11, 14, 15, 16), `~/.rpr-bridge/libs/ew_ho/ks_maps.json`, the May 2021 HO manual and `loop/MANUAL-GAPS.md`. All numbers come from my own scripts on the stems (200-6000 Hz unless stated; 10-40 ms frames). "Measured" means a number from these files. "Inferred" means a cause or a fix that a render still has to confirm. Every fix is on the instrument side (CC1 / CC7 / CC11, rows, velocity, note ends) or in a tool rule. None is a per-note move in the track volume envelope.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 28, so there was no assigned reading. I read the pages behind my findings and `loop/MANUAL-GAPS.md`.

| Manual (May 2021 HO, PDF page) | What it says | Where it applies here | Does the render follow it |
|---|---|---|---|
| p.105, brass Legato | A slur needs no gap between the notes and an interval of an octave or less. Legato patches are monophonic. | Every brass slur; Trumpets 1-2 at 970 (E5 to C6, a minor sixth: legal) | Partly. When the head of a slur is accented, `ACC_HEAD_JOIN` plays the head on the Sus row. The second note is then the first note on the legato row, not a transition, and it speaks late (finding 3). |
| p.106, Legato Slur | "MIDI Velocity is used to control the speed of the legato transitions." | Legato targets at v96-124. The join notes after a Sus head use `SOST_VEL` 100. | Yes for ordinary targets. For the join notes the c27 leads (0.16-0.20 s at 970) did not move them (finding 3). |
| p.106, Legato Slur Accent | The patch "includes an accent at the attack". The Mod Wheel sets the volume and velocity sets the accent strength. | Accented slur heads: 968 (Trumpets 1-2, Horn 1), 816 (Horn 1, Trombone 1), 576 (Horn 3) | Not used. MANUAL-GAPS #1 (lines 45 and 313): "Leg Slur Accent MAX" is installed in all five brass KS Masters and has never been tried. It is the candidate for finding 3. |
| p.64 and p.151 (CC7), MANUAL-GAPS c26 / c27 | CC7 is 20 log10(CC7 / 127) on the string, wind and brass patches. | `ROLE_EDGE_IN_REST` CC7 carries and `dyn_trim_to_cc7` | The law holds. The carry is applied at the wrong note when the edge falls inside a legato-connected span (finding 1). |
| p.69 (harp), MANUAL-GAPS c22 | CC11 and note velocity set the harp's loudness. The KS Master has the copied Velocity->Volume path. | Harp gate items 951.5 / 951.9 (finding 6) | It can be used. The harp is excluded from CC7, so velocity is its instrument-side lever. |

## Findings, ranked by what a listener on earbuds would notice

### 1. Six of the CC7-carried role moves are not compensated. The level change lands up to 4 qn early, and Horn 2's f note at bar 167 is 8 dB too loud (measured; cause inferred)

**Where:** `ROLE_EDGE_IN_REST` moves with a CC7 carry (`cycles/c27/role_moves_over_1qn.txt`).

**What is wrong:**
- The rule moves the envelope edge into a rest and is meant to hold the difference in CC7 until the original edge.
- On these tracks CC7 only dips for 0.3-0.5 qn around the note-on after the moved edge. It is back at 127 before the note sounds.
- So the role step plays from the moved edge, not from the printed place.

**Evidence (measured).** I compared c27 with c26 inside each carried window, from the moved edge to the original edge, per 0.5 qn. Where the carry works, c27 minus c26 is 0 ± 0.7 dB (Violins I 477 / 488 / 892 / 1024, Violins II 328 / 856 / 900 / 936, violas 720 / 1088, trombones 1020, Trumpet 1 932 / 1054, Clarinet 2 1031.85). The failures:

| track | original edge | moved to | carry | window (qn) | c27 - c26 |
|---|---|---|---|---|---|
| Horn 2 | 668.0 | 663.37-663.87 | +8.5 | 663.9-668.0 | **+8.2 dB** |
| Horn 1 | 863.77 | 859.49-859.78 | +2.0 | 859.8-863.8 | +2.0 |
| Horn 3 | 568.0 | 563.53-563.86 | +4.0 | 563.9-568.0 | +2.1 |
| Violins I | 899.9 | 895.97-896.00 | +6.0 | 896.0-899.9 | +2.9 |
| Violins II | 788.0 | 792.00-792.30 | -3.0 | 788.0-792.0 | -3.4 |
| Flute 1 | 1113.5 | 1107.43-1107.93 | +2.5 | 1107.9-1113.5 | +2.5 |

- **Horn 2's lanes, bar 167.**
  - CC7 falls 119 -> 49 over 663.41-663.86, which is in the rest.
  - It climbs back to 127 by 664.20, while the envelope already holds +8.5 from 663.87.
  - The f note at 664-667.9 therefore plays at +8.5 dB.
  - Horn 2 over 664.2-667.5: c26 1.8, c27 **10.1** (my band units). Horn 1 is 5.2 in both.
  - Horn 2 went from 3.4 dB under Horn 1 to 4.9 dB over it, on a held f chord just before the stopped notes.
- **Horn 1 at 860.** CC7 dips only to 103 over 859.51-860.09. The 860 note then plays +2 dB from the start.

**Cause (inferred).**
- In each failure the original edge sits on a note joined to the one before it with no rest (Horn 2 664 -> 668 is a slurred change onto "Stop Sus"; Violins I 896 -> 900).
- The CC7 return ramp is centred on the first note of the played span (from `STP_ROLE_SPANS`), not on the note at the original edge.

**Fix (`tools/score_to_parts.py`, `ROLE_EDGE_IN_REST`):**
- Take the "edge's note" from the notes list: the note whose onset is nearest the original edge. Do not take the start of the played span.
- Hold CC7 at 127 x 10^(-carry/20) from the moved envelope edge to that note's onset (for falls, the mirror).
- Place the 0.25 s return ramp centred on that onset (`carry_ramp_s` unchanged).
- Add a check to the gate: per carried move, the planned envelope + CC7 sum must equal the c26 envelope within 0.3 dB at every note-on inside the window.

**Pass (on the render):**
- c28 minus c26 within ±0.7 dB in the six windows above.
- Horn 2 at 664-667.5 at 1.8 ± 1 dB again (3-4 dB under Horn 1).

### 2. Trumpet 1's open solo (bars 51-66): every phrase swells on its first note and then drops 6-8 dB (measured; fix values inferred)

**Where:** Trumpet 1, qn 200-262, "solo, dolce cantabile", p. Slurs 200-214, 216-228, 232-248 and 251-260. This is the trumpets' first entry, alone over pizzicato strings.

**Evidence (measured):**
- **The heads swell.** Each head (v53, a dotted half) rises 9 dB over its own length. At 200 it goes -19 -> -10 at +1.1 s. Its CC1 rises 36 -> 50.
- **The phrase then falls.** The first legato targets (v96, CC1 51-52) sit at -16..-22.
- **Targets minus head** (median of the next three notes against the head's body):
  - Trumpet 1: **-7.9 dB at 200, -7.3 at 232**, -4 at 216.
  - Other lines measured the same way: Horn 1 median +1.1, Oboe 1 +3.7, Violins I +0.8.
- **In the master** (1-4 kHz), bars 201.5-203 minus 203.2-207.8: c16 3.8, c22 3.8, **c27 3.7 dB**. The fault has been present since the per-note volume removal.
- **The score** has no hairpin in 200-238. The first printed shape is the crescendo 239 -> mf 244 -> decrescendo.
- So the phrase should arch toward its long notes (208, 240-244). Instead it peaks at the end of its first note (15-20 % of the phrase).
- The research default for lyrical lines is a centred arch peaking at 33-62 % of the phrase (EW-TEMPLATE-PLAN section 8).

**Fix (`build/score_config.py`, Trumpet 1 only, over 199.8-262):**
- **(a) Smaller head swell.** Cap the onset swell on the slur heads 200 / 216 / 232 at +6 CC1 units over the head's start value: 36 -> 42, not 36 -> 50. Use the `INSTR_POST cc_cap` lane cc1 over 199.8-202.9, 215.9-218.9 and 231.9-234.9.
- **(b) Lift the targets.** Add CC1 +4 on the legato targets (`note_cc` cc1 +4 over 202.5-215, 218.5-231 and 234.5-248, ceiling 60).
- Expected change: the head peak -5 dB, the targets +2.5 dB. On these KS Masters CC1 is the dynamic layer; the c27 +12 units moved the f targets 7-9 dB, about 0.65 dB per unit.
- Leave the printed crescendo 239-244 as it is.

**Pass:**
- Targets minus head between -2 and +1 dB at 200 / 216 / 232.
- Master 1-4 kHz 201.5-203 minus 203.2-207.8 under 1.5 dB (now 3.7).
- The loudest stretch of the 232 phrase lands in 240-245.

### 3. The second note of an accented slur speaks late. Trumpets 1-2 at 970 are +170 / +200 ms, Horn 1 at 818 +160 ms, and leads do not move them (measured; cause inferred)

**Where:** every `ACC_HEAD_JOIN` join (`slur_start_joins`): Trumpets 1-2 at 970 (bar 243, "molto espr." f), Horn 1 at 74 / 634 / 818 / 970, Horn 3 at 106 / 146 / 578, Trombone 1 at 818.

**Evidence (measured).** My measure is the time at which the new pitch reaches -6 dB of its later level, from harmonic bands that the two pitches do not share, relative to the beat:
- Trumpet 1 at 970: **+170 ms**. Trumpet 2 at 970: **+200 ms**.
- Horn 1: 818 **+160**, 74 +90, 970 +80, 634 +70.
- Horn 3: 578 **+140**, 146 +80, 106 +70.
- The old pitch falls 10 dB at +100..+180 ms on these joins and on ordinary legato joins alike. So the fault is the new note's slow start, not an old note left ringing.
- **Ordinary legato joins on the same tracks** (legato row to legato row) reach -6 dB before the beat: Trumpet 1 median -30 ms, Horn 1 earlier still.
- **On the head joins the medians are later:** Trumpet 1 +10 ms, Horn 3 +40, Trumpet 2 +120.
- **Why the leads did not work.** All the join notes are v100 (`SOST_VEL`). In c27 the leads at 970 were raised to 0.16 s (Trumpet 1) and 0.20 s (Horn 1) with no gain: c27 CHANGES gives +152 / +130 ms. A larger lead cannot fix a note that is not a transition.
- **Cause (inferred).** The accented head plays the Sus row (`ACC_HEAD_JOIN`). The legato row therefore has no sounding note to slur from. The second note starts as that row's first note, on its slow sustain layer (mvt1 c15 note in `score_to_parts.py`; p.105-106).

**Fix (range test under the lock; starts 963.75 and 811.75):**
- **Variant A: "Leg Slur Accent MAX"** (p.106; installed in all five brass KS Masters, MANUAL-GAPS #1). Play the whole slur on this row with no keyswitch inside the slur.
  - The head carries the accent at v72-85 (weight, not bite). The targets stay at v100-110 (transition speed).
  - CC1 as now. Drop the head's gentle-accent swell on these heads.
  - Where: Trumpets 1-2 968-982, Horn 1 968-982 and 816-823.5, Trombone 1 816-823.5, Horn 3 576-583.
  - Code: `ART_SPANS` in `build/score_config.py`, and `ACC_HEAD_JOIN` off for those onsets.
  - This adds one row on 4 tracks, an Opus state change, so rebuild those tracks fully. Unload "Marc Shrt RRx4" on Horn 3 if memory needs it; it is used only 4 times.
- **Variant B** (if A brings a bite or breaks the legato): keep the Sus head, but play the join note itself on the Sus row as a target 0.08 s early, crossfaded with the head (the head ends 0.08 s after the new onset; CC flat over the join).
  - This is the technique of Horn 1 c22 and the woodwind targets of c23 (8 of 8 holes closed), and it is close to the cor anglais variant b of c27.
  - At 970 the slur's later notes (973, 978) are long, so the whole slur can stay on the Sus row with the same crossfades.

**Pass:**
- New pitch at -6 dB within +50 ms of the beat at 970 (Trumpets 1-2, Horn 1), 818 (Horn 1, Trombone 1) and 578 (Horn 3).
- The head's 2-5 kHz front (first 80 ms minus body) at most +2 dB (now -16 at 968).
- No join dip over 4 dB.

### 4. Più allegro (bar 248): the trumpets' tenuto at 989 is now 5-8 dB over its neighbours and over the head (measured)

**Where:** Trumpets 1-2, qn 984-998 (f, slurred). 989 is A5 (Trumpet 1), a half note with a tenuto.

**Evidence** (per-note p90 level, Trumpet 1):

| qn | 984 head | 987.5 | 988 | **989** | 991 | 992 | 994 | 996 |
|---|---|---|---|---|---|---|---|---|
| c26 | -3.2 | -13.7 | -15.3 | -5.3 | -10.4 | -11.8 | -14.7 | -11.9 |
| c27 | -3.2 | -6.6 | -7.4 | **+2.6** | -3.6 | -8.2 | -7.3 | -5.2 |

- The c27 CC1 +12 lifted every target 7-8 dB, and 989 with them. 989 still stands 10 dB over 988, as in c26, and is now 5.8 dB over the head.
- Against the mean of 988 / 991: Trumpet 1 **+8.1 dB**, Trumpet 2 **+5.3 dB** (-2.2 against -8.9 / -6.2).
- A tenuto means full length and a little weight, not the loudest note of the phrase.
- Horn 1 plays the same line with its 989 on "Sus MAX" at -2.1, only 1.5 dB over the head.

**Fix (`build/score_config.py`):**
- Remove 989's CC11 bump (+12 -> 0).
- Add CC1 `note_cc` on 989 only: Trumpet 1 **-12 units**, Trumpet 2 **-6 units** (about 0.65 dB per unit), returning to the line's lane at the 991 transition.
- Keep the 0.45 qn lead (its crossover is +65 ms) and the CC1 +12 on the rest of the slur.

**Pass:**
- 989 0-3 dB over the mean of 988 / 991 on each trumpet.
- The per-note range over 984-998 is 8 dB or less on Trumpet 1 (now 12).

### 5. Più allegro: Trombone 1's accented dotted quarters are cut to a quarter, while the bassoons and celli play the same figure at full length (measured)

**Where:** Trombone 1 (a2: Trombone 2 is dropped as unison), qn 985, 990, 993, 1001, 1006, 1014-1046 (the F1 head motive, ff). Bassoons 1-2 and celli double the figure.

**Evidence (measured):**
- **Length.** The written 1.5 qn notes play **1.00 qn** (985: note-off at 986.00; the next note is led to 986.35).
- **Cause in the data.** The trombones' tongued-join floor `_C17_GAP` (floor_s 0.12) and the next note's 0.147 qn lead take 0.5 qn off the note.
- **Stem.** The trombone falls 8.5-9 dB for about 0.15 s at every one of these joins: 985 -5 -> -14, 990 -6 -> -16, 993 -4 -> -13, 1001 -5 -> -14, 1006 -4 -> -12.
- **The doubling.** The bassoon plays the same notes for 1.40 qn and the celli for 1.47 qn.
- So the doubled line has two articulations: a held accent in the strings and bassoons, and a clipped quarter in the trombone.
- The c17 floor was set to separate tongued joins that ran together. These joins change pitch and follow an accented long note, where a 0.05 s break is enough.

**Fix (`build/score_config.py`):**
- `INSTR_POST["gap_set"]["Trombone 1"] = [{"from": 984.0, "to": 1080.0, "min_qn": 1.4, "gap_s": 0.05}]` (the same mechanism as the chorale's brass `gap_set`).
- Keep the 0.12 s floor elsewhere and on same-pitch repeats.

**Pass:**
- Dips at these joins 5 dB or less, with separation still 3 dB or more.
- The notes end within 0.15 qn of the bassoons' note-offs.

### 6. The nine gate items: an instrument-side fix for each (measured on the lanes)

- **Oboe 1, 851.46-851.69:** the envelope rises +1.5 -> +4.5 dB at the led onset of 852 inside a slur (`role_edge_join`; no rest within 16 qn). Carry it in CC7: envelope held at +4.5 from the rest before 846.9, CC7 90 -> 127 centred on 851.71.
- **Violas, 775.26-775.95:** the envelope rises -5.0 -> -2.5 on the "Leg BC" note that enters mp. Hold the envelope at -2.5 from the rest before 775.26 and put the -2.5 dB under the decrescendo in CC7 (106 -> 127 by 775.95).
- **Celli, 494.9-495.9:** 3 -> 0 dB over a legato note. Same CC7 carry (127 -> 90 over 494.9-495.9, envelope flat).
- **Celli, 15.64-15.66:** a 6 dB step in the 0.03 qn gap between the lifted quarter and the bar-5 chord, under the quarter's release. Put the -6 dB in CC7 from 15.66, ramped up 0.06 s ahead with `no_pre_cap` as on the Violins II chord, and keep the envelope flat.
- **Bassoons 1-2 and contrabassoon, 600.0-601.65:** a 1.7 -> 0 dB envelope fall inside the ff note after the sfp. It comes from an `INSTR_POST vol_set` row ([596, 600, ...]), which `dyn_trim_to_cc7` does not convert. Fix: extend `dyn_trim_to_cc7` to `vol_set` rows (generic), or end that row at 599.90.
- **Harp, 951.5 and 951.9-952.15 (-2 -> -3 dB at chord onsets):** the harp has no CC7 path. Lower the velocities of the 951.5 and 952.0 notes by the equivalent of 3 dB through the KS Master's Velocity->Volume path (p.69, c22 `vel_volume`), and remove the envelope step.
- **Generic (after finding 1 is fixed):** any role edge left as `role_edge_join` gets a CC7 carry centred on the onset of the note at the edge. Then the gate should read 0 / 0 / 0.

## The coordinator's list, through this lens

- **guard27's nine items:** finding 6.
- **Trumpets 989 / 991:** finding 4. 991 is 1.9 dB over the mean of its neighbours and is not a fault. 989 is the fault.
- **Trumpet 1 at 970 and Horn 1 at 818:** finding 3. The cause is the Sus-row head, not the lead.
- **Horn 3's stopped decrescendo (548):**
  - Measured from the body after the sf front, the note falls 9 dB (-21 at +0.1 s to -30 at the end of the note), inside 7-10. The 14 dB in CHANGES counts from the sf front (-12).
  - Horn 4 falls 8 dB (-17 -> -25) before its next note.
  - Keep the ceilings.
- **Stops 17.3-17.7 dB:** in my lens the c27 celli stop ceilings (ruling 8) are the likely reason the bar-6 and bar-204 stops are drier (celli stem drop 10 -> 14-19 dB).
  - 0.3-0.7 dB over the band is not audible as a change of articulation.
  - Leave them; if one is touched, the celli ceiling ramp at bar 204 is the place.
- **Basses' pp re-bows (170.9 / 181.7 / 190.5):**
  - The stem still falls 18-20 dB at 170.9 (-18 -> -38 in 30-150 Hz) and recovers by +1.2 s.
  - In the master the 30-150 Hz band dips 5 dB (-24 -> -29), and the 150-6000 Hz band does not move (-10 ± 1).
  - Earbuds reproduce little under 100 Hz. With two cycles left, record it as accepted and spend the cycle elsewhere (inferred: not audible on earbuds).
- **Role edges moved (18 over 1 qn):** finding 1. The plain moves within 1 qn are in rests, and their following notes match c26 within 0.5 dB at the note.
- **Holistic, c16 -> c22 -> c27, on master measures:**
  - Bar-5 chord, front minus body: -9.6 / -10.0 / **-5.7 dB**. Better: Violins II marcato and the lower-string leads.
  - Muted theme joins (cor anglais onsets 681-730) dipping 3 dB or more: 8/32 / 7/32 / **3/32**, largest 6.1 / 6.3 / 4.6. Better.
  - Hammered eighths, master 40-150 Hz separation: coda 10.6 / 15.8 / **18.4 dB**, Più allegro 12.6 / 15.3 / **17.2**. Better.
  - Chorale bar-line dips: 5.1 / 2.1 / 2.2. Unchanged since c22.
  - Trumpet solo head minus targets: 3.8 / 3.8 / 3.7. Never addressed (finding 2).
  - Worse in c27 only: Horn 2 at bar 167 (+8 dB, finding 1), and the smaller early level steps of finding 1.

## Other movements' findings

- **Movement I c62 room bed:** unified in c27. Applies; no articulation effect.
- **Movement I c62 limit on how far a guard may move a ramp:** applies, in a new form.
  - `ROLE_EDGE_IN_REST` limits uncompensated moves to 1 qn, and the CC7 carries reach 16 qn.
  - But the carry fails at legato-connected edges (finding 1), so up to 4.4 qn (Horn 2, 1.5 s) of uncompensated move got through.
  - The gate check in finding 1 is the guard against this.
- **Movement I c62 f-to-ff step only +1.2 on the mp3:** does not apply. Here it is +3.5 (CHANGES).

## Other checks that passed (measured)

- **Repeated notes (S1), median separation:**
  - Basses 792-840: 12.7 dB (min 6.9). Basses 984-1080: 16.7 (min 8.0).
  - Contrabassoon 10.7. Violas' quarters 1032-1047: 10.6. Trumpet 3 at 984-1048: 8.5-10.4.
  - Chorale brass 888-936: Horn 1 11.8, Trombone 1 9.3, Tuba 14.9.
  - Only one repeat is under 3 dB: Trumpet 1 at 794 (2.0 dB).
  - The basses' metric velocities follow the research pattern (102 / 84 / 95 / 84 / 90 / 83 / 98 / 86, 18 steps), and their eighths play 0.30 qn of a 0.5 qn slot (60 %).
- **Accents:** 2-5 kHz front minus body is negative on every accented note in 984-1048 (Trumpet 3 -11.2, Trombone 1 -7.7, Violins I -9.4, Flute 1 -4.4 median). No bite. Dan's "a little overdone" (c17) is not visible in timbre.
- **Pizzicato, bars 51-66:** "Pizz RRx4" / "Pizzicato RRx4" on every printed pizz. Onsets at -6 dB of the peak, +12..+22 ms after the beat (median). Arco returns at 264 on the legato rows.
- **Tremolo:**
  - The rows are used for every printed tremolo at 888-899, 1016-1047 and 1088-1112, and Violins I has its div. a 3 chord at 1108.
  - No string note is longer than 4.4 s (the re-bow rule holds), so no tremolo or sustain loop cycle is audible.
  - Horn 4's 6.5 s pp note at 168 still shows a 5 dB dip near +4.5 s (c22's 7.2 ripple, known).
- **Percussion:** the crash and bass drum at 1108 are tied into the 1112 quarter (score page 16 confirms the tie), so there is correctly no restrike. The crash at 888 / 1048 decays smoothly.
- **Harp:**
  - Harmonics row at 168 / 176 / 184.
  - The 277 glissando: 15 notes G3-E6 on "Gliss Technique" over 2 qn into the ff chord.
  - The étouffez at 326 and 1113 end the notes on the mark.
- **Not ranked (inferred):**
  - The timpani's "soft sticks" (680-711: four pp strokes "near the rim", 708-710) and "medium sticks" (856) play on the hard-stick patch.
  - "Timpani Flt KS" would need another instance. Four pp strokes are not worth the memory now.

Do not touch: the basses' "Stac On Bow" hammered eighths with metric velocities; the chorale's re-tongue gaps; the cor anglais crossfades over the muted theme; the Violins II "Sus Marc LITE" chords and lower-string leads at 16 / 584 / 1104; Trumpet 1 on "Mute Sus"; the stopped-horn CC11 ceilings; the CC7 carries that measured within 0.7 dB (list in finding 1); the pizzicato rows; the harp Harmonics / Gliss Technique rows and étouffez cuts; the tied percussion strokes at 1108-1112; the CC1 +12 on the trumpets' Più allegro slur (only 989 changes).
