# Cycle 02, critic A: articulation and phrasing (render c01)

Material: `cycles/c01/render/` (stems after the stem fix, master), `cycles/c00/render/` for comparison, `build/parts.json` (the c01 data plus the stem-fix roles; tempo map and notes as rendered), `build/mockup-events.tsv`, `build/score_config.py`, `tools/score_to_parts.py`, the row-to-sample tables read from the KS Master `.oib` files with `opus_state.py`, score pages 1, 4 and 5, and May 2021 HO manual PDF pages 95-99 (group A2). Times come from the parts.json tempo map, with qn 0 at 0 s of the rendered files. Levels are RMS in 10 ms frames on the stems unless the text says master. Each judgement is marked **measured**, **read** (code, patch file or score) or **inferred**.

## Manual notes (A2, PDF pages 95-99, read in full; MANUAL-GAPS.md read)

| Page | What the manual says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| 95-96 | Pre-recorded runs: one-octave scales in 1st Violins, Violas and Celli, with direction set by keyswitch, MOD or SPLIT. The Repetitions Runs script picks the slur direction itself, and its samples are repetitions that are heard when a run stops on a note. | The scherzo has no scale runs. | Not applicable. |
| 96-97 | Slur Runs (1st and 2nd Violins only) are built for fast slurred scales: run notes, the slurs between them, and sustains at 3 vibrato levels (CC1) and 5 dynamics (CC11). Velocity is ignored. The minimum speed is sixteenths at about 125 bpm, which is 0.12 s per note. | The scherzo's slurred eighths last 0.114 s at quarter 264, which is inside that speed. 64 Violins I and 91 Violins II slurred eighths (plus 25 viola and 22 celli) are each played as a fresh Sus MAX attack, for example the theme head's F sharp 5-F 5 after the accent. | Not used (finding 5). Movement I c20 measured this row separating slurred sixteenths at 0.119 s where Sus MAX smeared (mvt1 LEARNINGS). |
| 97 | Spiccato Runs (2nd Violins only) play runs with 5 interval samples, at most a whole tone between notes. | None. | Not applicable. |
| 97-98 | Tremolo and measured tremolo (TS, synced to the host tempo) take CC11, not velocity. | No string tremolo in this score. | Not applicable. |
| 98 | Trills, with a keyswitch choice of half or whole tone. | No trills printed. | Not applicable. |
| 98 | Repetitions (the manual names Violas and Basses; every KS Master here has a "Repetitions TS" row) give about a dozen pulses in a little over 1 s, tempo synced, with CC11 crossfades. | The theme head's two repeated eighths, and the repeated quarters. | Correctly not used: a dozen pulses at the sample's own rate does not fit a pair of eighths. |
| 98 | Sul ponticello (violas only) | Not printed. | Not applicable. |
| 98-99 | Legato Slur and Portamento: in portamento the pitch slides through the notes in between, while a slur jumps over most of them. Legato needs no time gap between the notes, so the first note of a phrase has no legato. Legato patches are monophonic, and CC22 64-127 makes them polyphonic. | The "port." at bar 214 (qn 640); every slurred line; the violas' "non div." double stops ("poly" ART_SPANS). | Followed. The port. glides: energy between C sharp 6 and F sharp 6 rises to +1 dB over the two end pitches for about 0.2 s around the beat (c00: -16..-31 dB, no glide). I found no chord on a mono legato row. |
| 99 | **Legato Slur Staccato** adds a slur-staccato attack to every note with no legato connection, so "the first note of each legato phrase" gets "a slightly stronger attack". | The theme head's accented note, which starts a slur (G5 accent, then F sharp 5, F 5, E 5), in every statement and every string section. The KS Masters have it: 1st Violins "StacSl Leg BC + Slur + Port MAX" (key 50; regions read: V1 **StacSl** mp/f/ff attacks + Nv/Vb sustains + LegSl/LegBc/LegPt), 2nd Violins (key 47, V2 StacSs attacks), and Violas / Celli "Stac Leg BC + Slur + Port MAX" (keys 44 / 90, StacHd attacks). | Not used (finding 1). The scherzo's c16 test used the violas' row for fast slurred sextuplets, not for accented first notes. |
| 99 | Legato Bow Change: a bow change inside a legato line, chosen by Opus from the MIDI data. | Leg BC MAX targets throughout. In bars 101-104 and 301-304 it joins **unslurred accented** half notes (finding 2). | Followed as written, but used where the score asks for separate accented strokes. |

MANUAL-GAPS additions: #2 (repetitions): the manual itself rules the Repetitions row out for pairs (p.98). #11: the port. was rendered in c01 and glides (above). Two new gaps for the table are Legato Slur Staccato for accented slur starts (p.99) and Slur Runs for slurred eighths at quarter 264 (p.96-97).

## Findings, ranked by what a listener would gain

### 1. The theme head's accented slur (accent, then two slurred eighths) is still a hole in every p/mp statement. The c01 strokes did not fix it; the manual's Legato Slur Staccato row is built for this exact case.

- **Where.** Violins I at qn 39, 51, 69, 75 (bars 14-26), 285 (bar 96), 759, 771, 789, 795 and 819 (bars 254-274). In each, the accented G5 (or its transposition) is a half note that starts a slur over two eighths and a staccato quarter (`VlnI 39 accent, slur -1 ... 42 staccato, slur 1`). The same figure is in Violins II (132, 195) and the violas (123, 183, 267, 723, 879).
- **What is wrong (measured, c01 stems).** The figure is the theme's main gesture, and all of it sits under the staccatos around it.
  - The accented note (mean of the first 150 ms, minus the 100 ms peak of the staccato before it) reads -13.5 / -12.7 / -14.9 / -13.9 / -8.9 / -11.8 / -11.1 / -11.8 / -9.9 / -8.8 dB, against c00's -15.0 / -7.3 / -11.7 / -15.2 / -14.8 / -9.6 / -4.3 / -10.4 / -8.5 / -8.2. That is no gain, and 51 and 771 are worse.
  - It reaches its maximum 140-480 ms after the beat (a quarter lasts 227 ms).
  - The two slurred eighths after it (41/41.5 and the like) are fresh Sus MAX attacks at velocity 53. They read -3..-13 dB (first) and -7..-17 dB (second) under the same staccato peak. In the ff statements (111, 123, 207, 891) the gap is smaller (-5..-9 dB accent, -1..-5 dB eighths).
  - 2-5 kHz attack minus body is -4.5 dB median on Violins I accents, so the problem is missing weight, not bite.
- **Why (read).** At p the DOWNBOW_STROKE_AT stroke is Sus MAX at `REBOW_VEL_BY_CC` velocity 52, and that row speaks as slowly as Leg Slur MAX's first-note layer (c01 LEARNINGS; Movement I c20: "a third-leap from a soft (v53) first note still did not speak"). The slurred eighths after it are on Sus MAX because they are under 0.25 s. They re-attack slowly instead of slurring.
- **Fix (manual p.99; one render as an A/B test).**
  - In `build/score_config.py`, remove 39, 69, 759 and 789 from `DOWNBOW_STROKE_AT["Violins I"]`.
  - Add `STACLEG_SPANS = {"Violins I": [(39.0, 41.9, "StacSl Leg BC + Slur + Port MAX"), (69.0, 71.9, "StacSl Leg BC + Slur + Port MAX"), (759.0, 761.9, "StacSl Leg BC + Slur + Port MAX"), (789.0, 791.9, "StacSl Leg BC + Slur + Port MAX")]}`. Each span ends before the slur's last note, which is staccato and stays on its Stac row.
  - Keep 51, 75, 771 and 795 as strokes for the control.
  - The per-span row path exists (`in_stacleg`, Movement I c20). Inside the span the notes overlap by `FAST_LEG_OVERLAP`, with no lead and no same-pitch merge.
  - One code change is needed in `tools/score_to_parts.py`: let a span carry a 4th element, the first note's velocity. A named-row span keeps the LilyPond velocity, here 73 at p. Use 90, inferred to reach the StacSl mp layer (the row's attacks are mp/f/ff only). Leave the slurred targets at the legato velocity 124 (fast transitions for 0.114 s eighths).
  - One more row on Violins I (Leg Port MAX is already loaded).
  - Pass criteria: the accent within -3..+4 dB of the staccato peak before it in the first 150 ms; both eighths within -6 dB; maximum within 150 ms of the beat; 2-5 kHz attack minus body at or under 0 dB. If it passes, extend it to every statement and to the violas' "Stac Leg BC + Slur + Port MAX" (keys 44 / 90) and Violins II's StacSl row for their copies of the figure.

### 2. The f hemiola "ritmo di quattro battute" (bars 101-104 and 301-304) loses its accents: 31 printed accented strokes are played legato or merged into one held note.

- **Where (read: score p.4 and the event list; parts.json).** Bars 101-104 (qn 300-312) and 301-304 (qn 900-912). The strings play unslurred, accented half notes on every second beat, f < ff (p.4: every string staff carries ">" on each half note, with no slur).
  - Violins II and violas at 302, 304, 306, 308 and 310 (and 902-910) are Leg BC MAX targets: bow-change legato, started 0.88-1.1 qn early.
  - Violins I at 902-910 are also Leg BC MAX targets.
  - V2, violas and celli at 300 start on Leg Slur MAX's slow first-note layer.
  - The celli's repeated accented B2s at 302-310 are merged into **one 11.6 qn Leg Slur MAX note** at qn 299.74 with 14 CC notches. The same happens at 902, 904, 908 and 910 (the same-pitch merge in `score_to_parts.py`, "c03 (A #1)").
  - Only the basses (Sus MAX) and Violins I's 300-310 (strokes via STR_ACC_AFTER_SUS) re-attack.
- **Evidence (measured).** Each accent's first 150 ms minus the 50-250 ms before it:
  - Master: 302 / 304 / 306 / 308 / 310 = +1.7 / -1.1 / +0.5 / +2.8 / +1.4 dB (c01) and -0.6 / -0.6 / -0.8 / +3.4 / -0.2 dB at 902-910. The hemiola that names the passage is not heard on the first three accents of each statement.
  - Stems: Violins II +5.9 / -5.9 / -0.1 / +0.4 / -0.7; violas -0.9 / -3.6 / -4.1 / +5.3 / -6.6; celli +0.7 / -1.2 / +0.3 / +3.0 / +2.0 dB. The negative values are the legato voice moving off the beat.
  - The target is +2..+4 dB of weight on each.
- **Fix.**
  - Config, now: in `build/score_config.py` add to `DOWNBOW_STROKE_AT` `[300.0, 302.0, 304.0, 306.0, 308.0, 310.0, 902.0, 904.0, 906.0, 908.0, 910.0]` for Violins II, Violas and Violoncellos, and `[902.0, 904.0, 906.0, 908.0, 910.0]` for Violins I. (Celli 906 is a pitch change; the rest are repeats.)
  - Read: the art choice (line ~2148) runs before the same-pitch merge (line ~2430), and the merge needs both notes on a legato row. So listing the celli onsets also stops the merge.
  - At f-ff these strokes take `REBOW_VEL_BY_CC` 80-96, which is fast enough at that level (Violins I's strokes at 300-310 already read +0.9..+3.3 dB).
  - Generic, in `tools/score_to_parts.py`: (a) an accented, unslurred string note of 1 qn or more after a legato-row note becomes a Sus MAX stroke (the same path as `STR_ACC_AFTER_SUS`, which today fires only after Sus/Stac notes); (b) the same-pitch merge skips a next note that carries an accent.
  - After the render: master +2..+4 dB at each of the ten accents; celli 302-310 as five separate attacks on the stem.

### 3. The woodwind staccato row's single velocity table made Oboe 1's staccatos louder than its accents and left the cor anglais' staccatos too soft (c01 open item, now measured against the accents).

- **Where.** The theme-head accents after staccatos: Oboe 1 and cor anglais at qn 123, 207, 315, 327, 345, 351, 819, 891, 915, 927, 945 and 951.
- **Evidence (measured; accent's 150 ms peak minus the peak of the staccato before it).**
  - Oboe 1: median **+0.4 dB at c00, -5.6 dB at c01** (123 -6.4, 207 -7.8, 819 -8.8, 891 -7.8, 915 -5.6, 951 -5.7).
  - Cor anglais: +5.7 to +8.3 dB median (315 / 915 +14.8 / +15.0). Its staccatos sank by 4.5 dB in c01 (actor's measure).
  - Flute 1: +2.5 to +3.0 dB, which is right.
  - The separation is fine: every woodwind stem's same-pitch eighth pairs dip 4.0-8.5 dB at the median (Oboe 1 5.2, cor anglais 5.1).
- **Fix.** In `build/score_config.py`, give Oboe 1 and the cor anglais their own `vel_by_cc` tables in the "Stac DblTng RRx9" ART_SPANS entry, in place of the shared `_WSTAC`.
  - Oboe 1: every velocity 12 lower: (22,32) (34,42) (46,52) (58,60) (72,70) (88,84) (114,100) (124,106).
  - Cor anglais: every velocity 10 higher: (22,54) (34,64) (46,74) (58,82) (72,92) (88,106) (114,120) (124,127).
  - The step size is inferred (the row's layers are velocity-switched; c01 measured +4.9 / -4.5 dB at the shared table). Check: Oboe 1 accents +2..+4 dB over its staccatos, cor anglais accents under +6 dB, the pair dips unchanged.

### 4. In the ff tuttis the master still blurs several repeated eighth pairs (S1). Violins II's staccatissimo row does not separate the pair and plays loud.

- **Where.** Bars 105-120 and 305-320, the theme head's repeated eighths at 313, 319, 325, 331, 340, 349, 355 and 913 ... 955.
- **Evidence (measured, peak-to-trough between the two eighths' peaks, 10 ms frames).**
  - Master median 2.5 dB (c00 2.2). The pairs at 325, 349, 925, 940 and 949 stay at 0-2.2 dB.
  - On the stems, Violins II (V2 "Stac Slur RRx6" = V2 StacSs samples, read) reads 0.1 / 0.7 / 0.1 / 0.7 / 0.8 dB at 313, 325, 913, 925 and 949. At 313 its level rises steadily through both eighths, with no trough in 20 ms frames.
  - Violins I (Stac RRx14) reaches 7-10 dB at most pairs.
  - In the master's trough at 313 and 913, Violins II carries the largest share of energy (more than half of the stems' energy in that frame).
  - c01 measured the row at +2..+6 dB over the Stac row it replaced.
- **Fix.** Change Violins II's tutti `ART_SPANS` row from "Stac Slur RRx6" to "Spiccato RRx9" (V2 Spic pp/mp/f/ff, read; the manual p.93 says it is shorter than staccato), and set `ROW_TRIM_DB["Violins II"]["Spiccato RRx9"] = (-3.0, 80)` as a starting level.
  - Inferred: the row should separate like Violins I's StacSs. Measure it on the stem.
  - If it does not separate either, return to "Stac RRx9" for the tutti (c00 stem dips 0-5 dB) at -3 dB.
  - Target: master trough of at least 3.5 dB at every pair.

### 5. About 200 slurred eighths in the strings are played as separate Sus MAX attacks, so the slurs are not heard as slurs (manual p.96-97, Slur Runs).

- **Where (read in parts.json).** Notes of 0.5 qn or less inside a printed slur, other than the slur's last note: Violins I 64 (the theme head's 41/41.5, 53/53.5, 71/71.5, 77/77.5 ...), Violins II 91 (125/125.5, 133.5, 145.5, 157.5, 197/197.5, 317 ...), violas 25, celli 22. All are on Sus MAX, following the kit rule "fast slurred notes under 0.25 s smear on legato patches".
- **Evidence.** At p each one is a fresh slow attack: -3..-17 dB under the staccato before the figure in the theme head (finding 1, measured). Whether the pitch is clear was not measured.
- **Fix (test after finding 1, or with it on different bars).** The 1st and 2nd Violins KS Masters have "Slur Runs" (V1 key 42, V2 key 43). The manual gives it for slurred notes at sixteenths at 125 bpm or faster (0.12 s per note; these are 0.114 s). Movement I c20 measured it on slurred sixteenths at 0.119 s: own-pitch share 0.52 -> 0.68 and 0.36 -> 0.83, level within 1.4 dB, at v127 with a 0.02 qn overlap and no lead.
  - Use the same form: `STACLEG_SPANS["Violins II"] = [(125.0, 126.0, "Slur Runs"), (197.0, 198.0, "Slur Runs")]` (two slurred eighth pairs in the second idea and the fugato) against untouched copies elsewhere.
  - The row ignores velocity and takes its level from CC11, so check the level step against the Sus MAX neighbours (inferred risk).
  - One more row on Violins II.

### 6. The violas' div. tenuto pairs under slurs (portato, bars 209-224) have no audible pulse.

- **Where.** Violas and Violas div at qn 629, 638, 641 ... 671: the second of each slurred same-pitch tenuto pair, merged with a 10 CC notch (read).
- **Evidence (measured).** Each pair's second onset, minimum over -60..+100 ms minus the 120-40 ms before:
  - Violas div: -1.9 / -0.2 / -1.6 / -1.6 / +2.9 / -2.1 / -3.2 / -1.9 / -1.7 / -2.0 / -0.4 / -2.1 / -1.0 dB, so no dip.
  - Violas: median about 0 dB, with three of 13 pairs at 3.6-8.5 dB.
  - The rising CC11 of the hairpins covers the 10 CC notch.
- **Fix.** `MERGE_NOTCH_AT = {"Violas": {q: 18 for q in (629.0, 638.0, 641.0, 644.0, 647.0, 650.0, 653.0, 656.0, 659.0, 662.0, 665.0, 668.0, 671.0)}, "Violas div": {...same...}}` in `build/score_config.py`. Target: a 2-3 dB pulse at each, with no level loss across the bar. This is low priority: it is an inner voice under the ff tune.

## Also measured (not ranked)

- **Accent bite (BRIEF item 9), measured.** 2-5 kHz energy in the first 100 ms against the body (250-500 ms), median per track: strings -2.6..-4.5 dB (basses +0.8), woodwinds -1.2..-7.9 dB, timpani +3.7 (4 strokes). No family is harsh. Across the board the accents lack weight rather than having too much bite.
- **Repeated quarters (S1), measured.** Trumpet 1 / 2 quarter repeats dip 9.3 / 6.5 dB at the median (2 of 15 Trumpet 2 pairs under 3 dB: 330, 999). Horns 3.8-8.0 dB. String pizz./stac quarters 10-12 dB. These are fine.
- **Woodwind and string eighth pairs (stems), measured.** Medians 4.0-8.5 dB on every woodwind and string stem; Clarinet 1 has 3 of 9 under 3 dB (208, 241, 892).
- **Port. bar 214, measured.** See the table above. The glide is long (about 0.2-0.25 s at quarter 228) but centred on the beat.

## Do not touch

- `PORT_TARGETS` 640 (the glide works).
- The wind "Stac DblTng RRx9" rows and their 0.02-0.03 s leads (separation is good: change only the velocity tables).
- Violins I's "Stac RRx14" in the tuttis (7-10 dB troughs) and the Stac rows of the soft statements.
- The re-bow fills.
- GENTLE_ACCENT's no-bite rule.
- Violins I's strokes at 300-310 and the basses' Sus MAX strokes in the hemiola.
- The trio legato settings and the solo/Flute 1 legato at bars 349-356.
- CC70 and CC15 lanes.
