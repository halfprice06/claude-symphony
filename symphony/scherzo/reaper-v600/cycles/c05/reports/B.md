# Cycle 05, critic B (balance and levels), on the c04 render

Material: `cycles/c04/render/` (the final stems after c04's Trumpet 1 stem fix, and the master), `cycles/c04/metrics/`, and `cycles/c03/render/` for comparison. Build data: `build/parts.json`, `build/mix.json`, `build/roles.json`, `build/score_config.py`, `build/mockup-events.tsv`, and the saved Opus states in `jobs/*.b64`. Score pages 5 and 9 were read, along with `sections/*.ily`.

Method:
- Levels are K-weighted power: the BS.1770 filter's response applied to 2048-point spectra every 10 ms, both channels summed, and averaged over qn windows on the parts.json tempo map. These are the same kind of numbers as the c03 and c04 B reports, not the plain RMS in metrics.md.
- "Peak" means the highest 50 ms mean within a note.
- "X over Y" means X's level minus Y's in the same window.
- A simulation scales a stem's frame powers and adds the change to the master as power.
- Each judgement is marked **measured**, **read** (data, code, score or manual) or **inferred**.

## Manual notes (cycle 5, slot B: group B5, PDF pages 114-115, 154-155, 158-159, read in full; MANUAL-GAPS.md read)

| PDF page | What it says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| 114-115 | Percussion categories. In the Basics kits, CC11 and velocity set loudness, velocity selects the dynamic layer ("up to 16 levels", Kit 2 "up to 12"), and the timpani felt long hits alternate hands. | Timpani on `Timpani Flt KS` (the same 16-layer long hits, manual p.123-124), not a kit. | **Yes (read).** Timpani velocities in parts.json span v41-125: pp 52-56, p 64, f 88-98, accents and ff 121-125. The track receives CC1 (roll layers) and CC7 (the c04 damp) but no CC11, so loudness comes from velocity and the envelope. The f motive x heard alone at bars 91 and 94 reads -27 dB K, in proportion to the f tutti at bar 101 (master -20). |
| 154 | Humanizer: random note-on/off delay, velocity, tuning, volume, pan. | Every track. | **Yes, correctly not used (read).** None of the 31 saved states in `jobs/` has a state-level MIDI-tool filter. The instrument filters are the patch scripts only (ConSordino, FingerPosition, EWSO, Legato3, Portamento3, Repetition3, LegatoSpeed, RTKiller). Renders stay deterministic, which the per-onset tables need. |
| 154-155 | MIDI Compressor on velocity or one CC; notes under the threshold are not played. | Every track. | **Yes, correctly not used (read).** Level compression is left to `deliver_master.py` after the mix. |
| 158 | Automation window: automatable parameters and macros. | Opus mixer, mics, reverb. | **Not used, by design (read).** Every level lives in parts.json and mix.json: CC1/CC7/CC11 before the hall, the REAPER volume envelope after it. |
| 159 | MIDI Controller Mapping: remap a patch's CCs, and "avoid conflicting MIDI CC messages". | Every CC the pipeline sends. | **Yes (read).** Every state maps each controller to its own number, with no remap: CC1 (28 states), 5, 7, 10, 11 (30), 15 (28), 22, 36, 64, 65, 68, 69 and 70 (6). parts.json sends CC1 on 29 tracks, CC11 on 30, CC15 on 7, CC7 on 1 (Timpani) and CC70 on 2, plus the CC36 reset and the CC69 "off" in the pre-roll (build_reaper RR_RESET_QN). The only CC sent that a map does not list is CC1 to the Timpani. It drives the Rls layers through the layer groups (DIGEST §9.1, measured in Movement I c12), so it is not a conflict. CC16 is in no map and is never sent (MANUAL-GAPS #12, still open, not a balance item). |

## Standing checks (Dan's ears), measured on c04

- **Loop pulsing (item 8): none.** Autocorrelation at 3.95 s of the detrended level / 100-300 Hz band / spectral centroid:

  | span | level | band | centroid |
  |---|---|---|---|
  | Violins I 0-23 | -0.04 | -0.16 | -0.07 |
  | Violins I 1089-1128 | -0.01 | -0.22 | -0.01 |
  | Horn 1 1110-1128 | -0.34 | -0.31 | -0.13 |
  | celli 605-624 | -0.07 | -0.08 | +0.17 |
  | celli 1070-1091 | -0.54 | -0.47 | -0.41 |
  | Horn 4 drone 456-504 | -0.05 | +0.10 | -0.05 |
  | master 1089-1128 | -0.20 | +0.19 | -0.22 |

  Violins I 420-445 reads band +0.42, as in c03, but that band holds the bassoon and bass clarinet pad; the violins' own level and centroid are +0.07 and -0.05.
- **S3 (measured).** Master in 50 ms frames from 0.2 s before the bar line: qn 360 -28.1, -27.4, -30.0, -32.0, -31.1, -29.6 ...; qn 828 -29.7, -32.8, -35.6, -36.9, -36.0, -33.4 .... No step to silence at either. The sfp at 900 is finding 5.
- **Accent fronts.** The flute accents in finding 1 are loud, not harsh. Their 2-5 kHz energy in the first 100 ms sits under the note body: Flute 1 at 315/351/999 -3.8 dB, at 915/951 -14.5 dB; Flute 2 at 315 -7.4 dB. The problem is level, not bite.
- **c04 B fixes hold (measured).**
  - Harp in bars 74-79 at -38.5..-40.4, over the horns at -40.6..-45.3 and no longer the loudest soft passage.
  - Bassoon 2 at 630 2.8 dB under the celli it doubles.
  - Bassoon 1 at 1032-1044 under Oboe 1 (but see finding 3).
  - Violins II's con sord. arpeggios 10-15 dB under the celli's tune.
  - Timpani at the G.P. silent.

## Findings, ranked by what a listener would hear

### 1. In the ff tutti theme the flutes vanish on the staccato head and burst out on the long top notes: the accented G6 is 16-20 dB over the flute's own staccatos and 5-8 dB over Violins I (bars 105-106, 117-118, 305-306, 317-318, 334; also 110 and 310)

**Where:** Flute 1 and Flute 2 (a2, an octave over Violins I+II) at qn 312-318, 348-354, 912-918, 948-954, 996-1001.

**Measured.**
- First statement, Flute 1, 50 ms peaks:
  - Staccato head (Stac DblTng RRx9, v112, CC11 114): 312 -23.7, 313 -33.6, 313.5 -34.6, 314 -31.7.
  - Accented G6 half note at 315 (Sus MAX): -14.5. That is 17-20 dB over the three staccatos before it.
  - Violins I's accent on the same beat: -22.1. The flute is 7.6 dB over it.
- Over each note's window (312-360), the flute's staccatos sit 7.9-17.7 dB under Violins I. The G6 at 315 and 351 sits +6.7 dB over Violins I, and the F sharp 6 at 317 / 353 sits +2.3.
- The flute is the loudest stem in bars 106 and 118 (-17.2 against Violins I -22.1). In bar 110 Flute 2 (-19.7) is over everything but Violins I.
- Second statement (912-960): Flute 1's G6 at 915 and 951 is -17.4 / -17.6, +5.7 over Violins I and 16 dB over its staccato neighbours. In the coda, 999 jumps +18 dB over the staccatos and is +5 over Violins I.
- Flute 2 plays the same G6 at -20.6 (+0.8 over Violins I). The burst is mostly Flute 1, but both flutes show the 10-13 dB row jump.

**Read.**
- At ff the woodwind "Stac DblTng RRx9" row plays far under the track's Sus MAX at the same CC11 and velocity. scherzo LEARNINGS c02: the row barely follows velocity.
- The accented notes get `GENTLE_ACCENT`'s +3.5 dB envelope swell on top (vol_db 315.13 +3.5 on both flutes).
- Flute rows have no `ROW_TRIM_DB` entry. Only Oboe 1's stac row has one (-5 from CC11 72).

**Judgement (inferred).**
- In the four loudest statements of the theme, the flute octave does not double the head. The listener hears a flute shriek on each long note instead, louder than the tune.
- An accent should be 2-4 dB of weight (BRIEF rule 4); here it is 16-20 dB.

**Fix.**
1. `build/score_config.py`: `ROW_TRIM_DB["Flute 1"] = {"Stac DblTng RRx9": (6.0, 100)}` and the same for "Flute 2" (ff only; `ROW_TRIM_WINDS` is already True). The f and softer flute staccatos (counterstatement, reprise) stay as they are.
2. `build/roles.json`, cuts on the Sus/Leg top notes:
   - "Flute 1": `[315, 317.4, -7]`, `[351, 353.4, -7]`, `[915, 917.4, -6]`, `[951, 953.4, -6]`, `[999, 1000.9, -4]`. The last one adds to the existing `[996, 1017, -4]`.
   - "Flute 2": `[315, 317.4, -3]`, `[351, 353.4, -3]`.
   - The roles' 0.5 qn ramp-in ends on the beat, so the moved onset (314.82) gets about -6 dB.

**Target (simulated from the c04 peaks).**
- Flute 1's G6 at about -22, level with or 1 dB under Violins I.
- G6 about 4 dB over the raised staccato median (about -26.7): a 2-4 dB accent.
- The staccato head 2-5 dB under each violin section instead of 8-15.
- Check S1 on the flute pairs (313/313.5) after the change. A level trim does not change the dip.

### 2. Coda build, bars 329-332 (qn 984-996): since c04, Violins II's motive x is 3-10 dB over Violins I's rising outer line and has buried the violas' entries (measured, caused by c04's A #3)

**Score (read, coda.ily header and c033).** In bars 325-332 the strings enter with motive x a bar apart, from the bottom up (Vc, Vla, Vln II, Vln I). In 329-332 Violins I rises G5-A5-C6-D sharp 6 against the falling bass ("a diverging progression"): it is the top line of the crescendo. Violins I and II are both mf < (Violins I f at 993); the theme head is ff at 996.

**Measured (3 qn windows):**

| qn | 984 | 987 | 990 | 993 |
|---|---|---|---|---|
| Violins I, c04 | -27.4 | -27.9 | -29.1 | -30.5 |
| Violins II, c04 | -30.8 | -25.3 | -21.9 | -20.5 |
| violas, c04 | -40.3 | -40.4 | -38.7 | -33.0 |
| Violins II, c03 | -37.5 | -35.9 | -34.2 | -25.8 |
| violas, c03 | -36.0 | -37.7 | -34.6 | -34.0 |
| master, c04 | -23.1 | -21.6 | -19.5 | -17.0 |
| master, c03 | -24.4 | -22.5 | -21.3 | -17.7 |

- Violins II rose 7-12 dB from c03 to c04 and is now the loudest stem of bars 330-332.
- Violins I is 3-10 dB under it at 987-993.
- The violas fell 2-4 dB and are 12-17 dB under Violins II.
- The build is 0.7-1.8 dB louder than in c03 bar by bar, which takes margin from the summit.

**Read.**
- c04 moved the coda pairs onto "Spiccato RRx9" (Violins II), "Stac RRx14" (Violins I) and "Staccatissimo RRx16" (violas) (`score_config.py` lines 381-386).
- parts.json `row_trimmed` is empty for all three sections over 980-1006. `ROW_TRIM_DB`'s string branch trims only notes with a Leg-row note within 3 qn, and these all-staccato bars have none. So Violins II's Spiccato plays at full level. It already played 2-6 dB over the Stac row at one velocity in c01 (LEARNINGS).

**Judgement (inferred).** The listener hears the inner ostinato on top and loses the rising violin line and the stretto's entries. The c04 S1 gain (Violins II pair dips 3.1 -> 5.5 dB) can be kept with a level correction.

**Fix.** `build/roles.json`:
- "Violins II": `[984, 995.5, -7]`.
- "Violas": `[984, 995.5, 3]`.
- "Violins I": `[987, 995.5, 2]`.

All three ramp back to 0 by 996, the ff head. The alternative is `ROW_TRIM_SKIP`-style logic in reverse: let `ROW_TRIM_DB` apply to string rows with no Leg neighbour inside `ART_SPANS` that carry `"mark": "staccato"`. That would be a generic tool change, and the role is enough here.

**Target (simulated).**

| qn | 984 | 987 | 990 | 993 |
|---|---|---|---|---|
| Violins I over Violins II | +10.4 | +6.4 | +1.8 | -1.0 |
| violas | -37.3 | -37.4 | -35.7 | -30.0 |
| master | -23.7 | -22.6 | -21.6 | -18.6 |

The violas return to c03 levels, and the master falls 0.6-2.1 dB in the build, below c03, which restores part of the summit margin. Re-measure the Violins II pair dips (should be unchanged: a flat level).

### 3. Oboe 1's soft espress. and dolce lines sit under the instruments they lead (bars 277-280, 345-347, 225) (measured)

**Measured.**
- **Bars 277-280 (qn 828-840), the reprise's second idea after the sub. p.** Flute 1 and Oboe 1 play it in octaves, both "sub. p espress." (score page 9). The clarinets, horns and violas are pp; the celli and Bassoon 2 sub. p. 1.5 qn windows:

  | qn | 828 | 829.5 | 831 | 832.5 | 834 | 835.5 | 837 | 838.5 |
  |---|---|---|---|---|---|---|---|---|
  | Flute 1 | -35.7 | -37.8 | -35.4 | -30.6 | -28.7 | -34.7 | -38.8 | -35.2 |
  | Oboe 1 | -48.1 | -45.2 | -40.3 | -32.0 | -40.4 | -43.1 | -42.0 | -43.2 |
  | pp violas | -50.4 | -45.8 | -44.5 | -43.3 | -42.7 | -40.7 | -43.3 | -44.7 |
  | celli | -47.0 | -46.5 | -41.9 | -40.7 | -43.1 | -40.2 | -35.7 | -36.1 |

  - Per note, Oboe 1 is 6.5-12 dB under Flute 1.
  - Oboe 1 is level with or under the pp violas and the celli, except at the hairpin peak (832.5).
- **Bars 345-347 (qn 1032-1041).** Ob 1, Cl 1 and Bn 1 are all "p dolce", with T on top in the oboe. Oboe 1 reads -44.4, -40.1, -38.2, -38.9, -38.1 against Clarinet 1 -38.5, -39.0, -38.1, -38.0, -38.3 (and the harp at -38.4..-42). The tune enters 6 dB under the clarinet below it and stays level with it until the crescendo of bar 348.
- **Bar 225 (qn 672-675), the codetta.** Oboe 1 "p dolce" leads. It reads -46.0 / -43.2 against the pp Violins II's -47.5 / -39.6 and the violas' -44.0.
- In each case the oboe's first notes are the weakest. That is the slow Leg Slur first-note layer at p, plus a p level that is low for a leading voice. The oboe's solo at 185 (-42, harp 3-5 dB under) is fine only because nothing else plays.

**Read.** Oboe 1 `gain_db` -5.3, `soft_trim_db` p 5. Flute 1 `gain_db` -1.3, p 5.

**Judgement (inferred).** At bar 277 the second idea sounds like a flute solo, not a flute-oboe octave. At 345 the listener hears the clarinet's inner part as the tune.

**Fix.**
- `build/score_config.py` `LEVEL_SHAPES["Oboe 1"] = [[(827.5, 0), (828, 7), (831.5, 7), (832.3, 2), (833.5, 4), (840, 4), (840.5, 0)]]`. This is a shape rather than a role so the hairpin peak at 832 does not jump over the flute.
- `build/roles.json`:
  - "Oboe 1": `[1032, 1041, 4]`, `[672, 676.5, 4]`.
  - "Clarinet 1": `[1032, 1041, -2]`.
  - "Flute 1": `[834, 836, -3]`. The D sharp 6 at 834 is the flute's hot note.

**Target (simulated).**
- 828-840: Oboe 1 3-5 dB under Flute 1 on most beats and level at 829.5, over the pp violas and celli everywhere.
- 1032-1041: Oboe 1 level with Clarinet 1 on the first beat, then 4-6 dB over it.
- 672-675: Oboe 1 at -42.0 / -39.2 / -38.6, over Violins II and the violas.

Do not raise Oboe 1's `soft_trim_db` p globally. Its p leggiero staccatos in the counterstatement (84-108) are level with Flute 1 already.

### 4. Retransition, bars 245-252 (qn 732-756): the bass clarinet's pp B pedal is the loudest stem, level with Clarinet 1's head entry and over Violins I's (measured)

**Score (read, retr.ily header).** Theme A's head passes viola (241) -> Cl 1 (245) -> Vln I (249), pp, over the pizzicato B. The bass clarinet holds B2 pp from 245 (dotted halves), < to p at 253.

**Measured (3 qn windows):**

| qn | 732 | 735 | 738 | 741 | 744 | 747 | 750 | 753 |
|---|---|---|---|---|---|---|---|---|
| bass clarinet | -42.0 | -42.1 | -45.4 | -43.3 | -40.6 | -37.1 | -36.0 | -39.9 |
| Clarinet 1 | -42.8 | -36.0 | -41.2 | -38.1 | -45.0 | -40.0 | -37.6 | -36.5 |
| Violins I | | | | | -41.8 | -38.1 | -36.2 | -38.3 |
| pizz. celli / basses | -53..-56 | | | | -46..-49 | | | |

- The bass clarinet is the loudest stem in bars 249-251.
- It is 1.0-1.2 dB over Violins I's entry, and 0.8 dB over Clarinet 1 on the clarinet's first beat.

**Read.** Bass clarinet `soft_trim_db` pp 5, gain +1. Its only roles are at 240-264 (bars 81-88) and 624-672. Nothing covers 732-756.

**Judgement (inferred).** The canon's entries, the point of the retransition, come through a held low drone that is louder than they are.

**Fix.** `build/roles.json` "Bass clarinet": `[732, 756, -5]`.

**Target (simulated).**
- The pedal at -47..-41: 4-5 dB under the Vln I entry at 744-750.
- 4.2 dB under Cl 1's first beat (732) and 11 dB under its second.
- Still over the pizzicato bass, so it keeps the harmony.

### 5. The tutti sfp of bar 301 (qn 900-906): in the trough after the sf the held Flute 2 and the p horn chord sit 8-13 dB over Violins I's melody, while Oboe 1 on the same held note drops as printed (measured)

**Score (read, events and dC).**
- Violins I (with Fl 1 and Vc) have the accented hemiola melody: B5, C6 accent, F6 accent, ....
- Fl 2 and Ob 1 hold B5 tenuto, 3 qn each, sfp.
- Horns 1-4 play a p tenuto chord, cresc.

**Measured (1 qn windows):**

| qn | 900 | 901 | 902 | 903 | 904 |
|---|---|---|---|---|---|
| Flute 2 | -31.1 | -31.5 | -32.3 | -31.3 | -31.7 |
| Oboe 1 | -35.2 | -41.7 | -39.3 | -41.3 | -36.5 |
| Horn 1 | -33.0 | -35.7 | -37.1 | -32.7 | -32.4 |
| Horn 2 | -35.1 | -37.1 | -34.3 | -31.5 | -33.2 |
| Violins I | -26.6 | -40.7 | -40.3 | -34.1 | -38.0 |

- Flute 2 and Oboe 1 have identical MIDI: B5, CC11 spike 119, then 46-54, and vol_db within 0.2 dB from 900.5. Yet the flute holds 8-10 dB over the oboe.
- At 901-902 Flute 2 is 9-10 dB over the melody, and the horns 3-6 dB over it.
- The master falls only 6 dB into the trough (-17.4 -> -23.7) while the strings fall 15-20 dB, so the sfp reads as a thinning, not a drop.

**Read.** Flute 2 plays the sf note on Leg Slur MAX's first note (ks 899.25), and the flute's p CC11 46 sits higher in level than the oboe's. The horns' p is CC1 64 on Movement II's soft map, which sounds near mf. In the exposition (300-306) that does no harm because the strings are f there.

**Judgement (inferred).** In the reprise's one tutti sfp, the listener hears a held flute B5 and a horn chord where the violins' melody should come through the drop.

**Fix.** `build/roles.json`:
- "Flute 2": `[900, 906, -6]`. The ramp ends on the note-on, so the whole note, sf included, is lower and no fall acts on the hall tail (S3).
- "Horn 1" and "Horn 2": `[900, 906, -3]` (same reason).

The flute's sf attack then sits level with the oboe's (-34) instead of 1.7 dB over it.

**Target (simulated).**
- Flute 2 at -38..-39, level with Oboe 1 and Violins I at 901-902.
- Horns 1-2 at -35..-40.
- If the melody still sits under the horns, a rise (not a fall) on Violins I and celli `[901, 904, 3]` is S3-safe.

### 6. Exposition second idea, bars 45-52 (qn 132-156): the celli bass is level with or over Violins I's tune (measured)

**Score (read, sA.ily c419/c432).** The second idea is f espress. in three octaves (Vln I; Vln II with Ob 1; violas with Cl 2). The celli carry the bass f with Bsn 1, Cbsn and Cb.

**Measured (3 qn windows):**

| qn | 132 | 135 | 138 | 141 | 144 | 147 | 150 | 153 |
|---|---|---|---|---|---|---|---|---|
| celli | -32.4 | -28.4 | -27.7 | -33.4 | -28.8 | -30.4 | -26.5 | -25.0 |
| Violins I | -28.8 | -28.4 | -30.4 | -32.7 | -28.9 | -29.3 | -25.1 | -20.3 |

- The celli are the loudest stem in bars 46-47, at +0.0 and +2.7 dB over Violins I.
- Bar 49 is level, and bars 48 and 50 are 0.7-1.4 under.
- The basses are 5-10 dB under the celli, so the bass octave is carried by the celli.

**Read.** c03 B's celli roles fixed the same relation at 362-396 and 828-864 (the E minor statements), but the G major statement at 132-156 has none.

**Judgement (inferred).** Same as c03/c04 finding 3: a low-mid-heavy forte with the tune second.

**Fix.** `build/roles.json` "Violoncellos": `[132, 156, -3]`. It ends before the ff hemiola at 156, where the celli and basses together are the cadence's bass.

**Target (simulated).**
- The celli 0.4-5 dB under Violins I through 132-156 (bar 47: -30.7 against -30.4).
- The master about 0.3-0.6 dB lower in those bars.

## Other observations (not ranked)

- **Violins I's ppp harmonic E6 (420-445)** is level with Hn 1's pp line: -42.6 against -43.0 at bar 143, and it is over the horn in bars 143-145. The mockup plays an ordinary ppp sustain (MANUAL-GAPS #14), which is fuller than a real harmonic. Violins I `[420, 445, -3]` would leave Hn 1 the line. This is inferred; check by ear.
- **Flute 1's p leggiero over the mp theme (bars 261-263, 267):** -33.4 / -35.7 / -29.9 / -34.1 against Violins I -34.0 / -36.0 / -32.2 / -34.1, level or 2 dB over. If the flute sounds like the tune, use Flute 1 `[780, 804, -2]`.
- **Hn 1's last G sharp (374-376)** is 1.8-2.7 dB under Violins I's ppp G sharp 5. Both are printed ppp, and the horn's decrescendo to ppp arrives at 1122, so this is consistent with the print. Leave it unless Dan wants the horn as the last sound.
- **Trio's forte return (624-672):** Violins I's tune is 1-5 dB over the celli's countermelody and 3-5 dB over Clarinet 1. Flute 1's mf at 648-660 is 2-3 dB under the ff violins, present but not on top. These are fine.
- **Summit (1005-1014):** brass f/ff at -24..-33 against the fff strings at -15..-22. The brass are under the strings, as printed.

## Do not touch

- The c04 balance fixes, all measured holding on this render:
  - the harp's episode caps and roles;
  - the bassoon gains -5 and their roles;
  - the bass clarinet roles at 240-264 and 624-672;
  - Violins II's roles at 192-198 and 501.5-588;
  - the doubling-wind roles at 132-150 and 372-384;
  - the celli `loud_eq` +2;
  - `TIMP_DAMP_AT` and the Timpani role at 1007.9-1020.
- Theme A's Violins I over the pizzicato bass (10 dB margin at 36-84).
- The reprise's arco espress. celli countermelody, 1-4 dB under the theme at 756-804, as printed.
- The Violin I solo over Flute 1 and Violins II "la metà" (349-356).
- Hn 1's motto tail over the violas (357-360).
- Clarinet 1's trio tune over the harp and drone (153-168).
- The sub. p transitions at 360 and 828.
- No loop pulsing on any held note.
- Every patch's controller map: no remaps. Do not use Opus MIDI tools; keep the pipeline deterministic.
- The hall settings.
