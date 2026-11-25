# Cycle 28, critic A: articulation and phrasing (on the c27 render)

Material: the `cycles/c27/render` stems and `cycles/c27/build_render/parts.json` (the data as rendered), `cycles/c27/records/`, and `cycles/c18/render` with its parts.json as the older comparison. The c18 stems are 3 dB hotter (global gain), so every number below is relative within one render unless it says otherwise. The actor's tools were run read-only: `cycles/c27/actor_scripts/fig27.py` (the pitch-resolved figure measure) and `spic27.py`. My own scripts measured:
- per-pitch bands (harmonics 2-5, ±0.3 semitone, 2048-point STFT, 5 ms hop);
- broadband and 2-5 kHz envelopes in 5 ms and 20 ms frames;
- 70 ms peaks;
- the rows each note plays, read from the `ks` lanes in parts.json.

"Measured" means a number from the render or from parts.json. "Inferred" means reasoned from those numbers.

## Manual notes

`MANUAL-READING.md` has no row for c28. I read group A1 (PDF pages 89-94 of the May 2021 HO manual, Hollywood Strings: sections, divisi, longs, shorts) in full, because three of this cycle's four A items are Violins I articulation choices (Spiccato, Marcato Sustain, Sus MAX). I also used `MANUAL-GAPS.md`.

| page | what it says | where it applies here | does the render follow it |
|---|---|---|---|
| 89-90 | DIV A/B patches have Close mics only; a divisi half is "not much less" loud than the whole section | the solo violin (DIV A, bars 349-356) and Violas div | followed (mix side); not re-measured this cycle |
| 91 | Sustain round robins alternate up and down bow on every note | every slurred pair played as two Sus MAX notes (bar 23 figure, tutti pairs 317/329/353, ...) | partly: each slurred note is a new bow stroke in the samples. The 0.02 qn overlaps keep them joined (pair troughs -4..-13 dB, finding 2). Not a defect at this tempo |
| 91-92 | Marcato Sustain: a marcato sample "ends relatively quickly" over looped sustains, giving "extra power at the start" | the nine soft theme heads and their two slurred eighths on "Sus Marc LITE" | the heads use it as described. Its quick end is the hole after each head (finding 2). Every slurred eighth on this row also starts with a marcato attack, which the slur does not ask for (finding 2) |
| 93 | Spiccato: the bow bounces, so the note is very short | the 72 Violins I staccatos that `STAC_ROW_BY_PITCH` sends to "Spiccato RRx9" by pitch | right for the 40 notes in same-pitch eighth pairs (S1). Wrong for the 32 single notes, which include the slur-end landing at 330 / 930 (finding 1) |
| 94 | Staccato On Bow: the bow stops on the string, "the distinctive sound of the bow stopping" | a staccato quarter that ends a slur (330 / 930, 42 / 54 / 72 ... after the soft heads' eighths) | not used. Stac RRx14 is the tested row (c18); Stac On Bow is an option (finding 1, variant) |
| 93-94 | Staccato / Spiccato Marcato MOD: CC1 crossfades into marcato for single accented shorts | none: the scherzo's accents are on half notes | correctly not used |
| 94 | Repetitions row: a dozen re-bowed repeats with release trails | the theme's repeated eighth pairs | not used. The Spiccato pairs separate by 4.5-6.5 dB (`records/stac.txt`), so not needed |
| MANUAL-GAPS #5, #12 | woodwind staccato rows; round-robin reset | woodwind theme heads; celli heads | in use |

## First check: Dan's figure at every occurrence

- Strings (`records/fig25.txt`, c26 -> c27, my rerun of fig27.py on c27 and c18). Nothing is more than 2 dB worse except one step: Violins I bars 110 / 310, step 79 -> 78, 4.5 / 3.7 -> 2.8 / 2.5 (c18 3.8 / 4.4). Violins II, same notes, is unchanged (4.1 / 4.6), and every other Violins I step is unchanged or better (bar 23 last step 9.1 -> 12.4). Cause and fix: finding 1 (measured).
- The 110 / 310 figure is not Dan's rising figure. It is the descent A5 (accented half) -> G sharp 5 -> G5 (slurred eighths) -> F sharp 5 (staccato quarter, slur end, on the downbeat of bar 111 / 311). Notes, CC11, CC1 and keyswitches from 328.868 to 330.3 are identical in c26 and c27 (parts.json). The only change that reaches these notes is c27's F sharp 5 v90+ region cut on "Spiccato RRx9" (-3 dB), which hits the landing F sharp at 330 / 930 (v95) (measured).
- Woodwinds: not re-measured. The actor's fig27w (CHANGES) has Flute 1, Flute 2 and Oboe 1 within 1.1 dB of c26 and Clarinet 2 better. The c26 woodwind state is unchanged.

## Findings, ranked by what a listener hears

### 1. Violins I plays 32 single staccato notes on "Spiccato RRx9" only because of their pitch. Among them are the slur-end landing of bars 110 / 310 (the 79 -> 78 regression) and the F sharp that now stands over the accented C at 345 / 945 (measured; fix inferred, the rows it returns to are c18's, measured then)

Where:
- Violins I, every printed staccato on D5, D sharp 5 or F sharp 5 that is not part of a same-pitch eighth pair.
- Tutti, at v95: 321, 322, 330, 338, 342, 356, 921, 922, 930, 938, 942, 956.
- Soft statements: 54, 62, 66, 80, 102, 105, 128, 294, 295, 298, 299, 747, 748, 752, 753, 774, 782, 786, 800, 824.
- The 40 notes that are in pairs (55 / 55.5, 64 / 64.5, 79 / 79.5, 103 / 103.5, ..., 331 / 331.5, 940 / 940.5, 955 / 955.5, 988 / 988.5) are what c24's reroute was for: "the same-pitch eighth pairs ... separate by 0.2-2.3 dB on every short row" (score_config c24 #4).

Evidence:
- Bars 110 / 310. Pitch bands around the landing's moved note-on (329.802 / 929.802), in dB under the G5 eighth's own peak:

| | landing F sharp 5 peak | its band at +0.16 s | G5 eighth at +0.06 s (same in both) |
|---|---|---|---|
| c18 (landing on "Stac RRx14") | **+3.2..+4.2** over the eighth, held to +0.16 s | +2.9 / +3.2 | -2.9 / -1.9 |
| c27 (landing on "Spiccato RRx9", v90+ regions -4 and F sharp 5 -3 dB) | **-1.6** (under the eighth before it) | -11.5 / -11.2 | -2.7 / -1.8 |

  The slurred G5 rings the same in both renders: 150 ms Sus MAX cap, -2.7 dB 60 ms after the landing's note-on. What changed is the landing. On Spiccato with 7 dB of region cuts it never rises over the eighth's tail, so the crossover comes while the G is still 2.5-2.8 dB from its peak. A listener hears G sharp - G smear into a faint F sharp, on the downbeat of bar 111 / 311, the bar after the tutti accent.
- 345 / 945 (CHANGES "still open"; `spic27.py`): the single F sharp at 342 is at -33.8 dB against the accented C at 345 at -34.6. In c18, with that F sharp on Stac RRx14, it was -33.5 against -31.3 (c18 scale): 2.2 dB under the C. The F sharp leads into Dan's figure at bar 115 / 315. On Spiccato it rose 2.7 dB against its c18 row, and c27's -3 dB cut did not bring it back under the C.
- The single notes gain nothing from the reroute: Spiccato's reason is a pair's re-attack (manual p.93, bounced bow), and a single note has no partner. 20 of the 32 came from "Staccatissimo RRx9" and 12 from "Stac RRx14" (c18 rows, read from c18 parts.json). c25 measured the c18 rows at -0.7..-1.2 dB over their staccato neighbours, against +2.8..+3.3 on Spiccato before the cuts.
- They also carry the c25/c26 velocity subtractions (-13 / -20 / -33: 54 played at v44, 66 at v44, 748 at v34). Those were made to fit Spiccato's layers and have no reason on the old rows.

Fix:
- `tools/score_to_parts.py`, STAC_ROW_BY_PITCH branch (line ~2728): new generic option `STAC_ROW_BY_PITCH_REP_ONLY = {track: True}`, default {}.
  - When set, a note takes the pitch row only if the previous or next note of the part has the same pitch, both are printed staccatos, and the two score onsets are 0.5 qn or less apart.
  - Otherwise the note falls through to ART_SPANS / STAC_ROW, as before c24.
  - The vel_add loop at ~3683 already keys on `n["stac_pitch_row"]`, so the velocities come back with the row.
- `build/score_config.py`, c28 block: `STAC_ROW_BY_PITCH_REP_ONLY = {"Violins I": True}`.
  - Keep the three-band velocity rows and mix.json's Spiccato region cuts: the pairs still use them.
  - The F sharp 5 -3 dB `vel_min 90` cut then reaches only pair notes at v90+, and there are none (988 / 988.5 are v49), so it can stay or go.
  - 782 / 786 stay on Spiccato through ART_SPANS (780-792), as in c18.
- Variant to range-test alongside: the slur-end landings (330 / 930, and the soft heads' landings 42, 54, 72, 78, ... when single) on "Stac On Bow RRx9" (manual p.94: the bow stops on the string; the row is in the 1st Violins KS Master; its orphan group is already switched off by the c24 rule). Not measured here.
- Range test 312-360 / 912-960 and 36-84 / 756-804 against a same-start control. Acceptance:
  - fig25 bars 110 / 310 step 79 -> 78 at 3.7 or more (c26 / c18 level), every other figure value within 2 dB of c27, bar 23 / 263 included;
  - 342 / 942 F sharp at least 1.5 dB under the accented C at 345 / 945;
  - single-note 70 ms peak over the ±3 qn staccato neighbours (spic27 method, all short rows): median -1..+1, none over +3;
  - the pairs' separation (`records/stac.txt` method) within 0.3 dB of c27.

### 2. The nine soft theme heads: the two slurred eighths are played as two detached marcato strokes, with a 14.6 dB trough between them and a bright front on each. The slur from the half note through the eighths is not heard (measured; the fix is inferred and needs the range test)

Where: Violins I, the eighths at q+2 / q+2.5 after the heads at q = 39, 51, 69, 75, 285, 759, 771, 789, 795 (bars 14, 18, 24, 26, 96, 254, 258, 264, 266). Score: one slur from the accented half note over both eighths to the staccato landing at q+3 (bar 14: slur 39-42, p leggiero).

Evidence (c27 Violins I stem; median of nine; levels against the staccato quarter one beat before the head):

| | head 0.03-0.15 s | 0.21-0.39 s | eighth 1 | eighth 1, 2-5 kHz | trough between the eighths (lowest 20 ms) | landing |
|---|---|---|---|---|---|---|
| c18 | +0.8 | -8.6 | -2.8 | +3.6 | -13.1 | +0.3 |
| c27 | -0.8 | **-9.6** | -1.8 | **+3.1** | **-14.6** | -0.8 |

- The same measure on the slurred eighth pairs played on "Sus MAX" with a 0.02 qn overlap reads -4.5..-12.6 (median -8.3) at 317 / 329 / 353 / 917 / 929 / 953, and -4.0..-6.3 at 343 / 787 / 943. On "Sus Marc LITE" the soft heads' pairs are 0.02 qn *apart* (eighth 1 ends 41.084, eighth 2 starts 41.104), and each starts with the row's marcato overlay at v78-94 (the 66-108 layer, which the vel<66 cut does not reach). So each eighth is a separate accented stroke, 2-5 kHz +3 dB over the staccato. Manual p.91-92: the marcato sample "ends relatively quickly", which leaves the hole.
- c27's head work held: head front -0.8 dB under the staccato before it, 2-5 kHz +3.2 (c26 +6.3). The eighths were not touched (c27 A #1c "eighths at v62" was not run). CC11 from marc_lift falls 65 -> 51 at the first eighth's moved note-on (40.594, as designed), so the eighths sit at CC11 about 50 with an f-layer marcato on each.
- History (score_config c13): "marc" was chosen over Leg Slur MAX targets (uneven: the second eighth heard 2-74 ms late) and over "Slur Runs" (failed). Keeping the eighths on this row keeps their timing; the faults are their gap and their attack layer.

Fix: two variants in one range test on 36-84 and 756-804:
- a) Stay on the row. Join the pair: in `build/score_config.py` give the first eighth's end a 0.02 qn overlap past the second eighth's moved note-on (NOTE_END_AT["Violins I"][q+2] for the nine heads. Both eighths are led 0.396 qn, so check in parts.json that the first eighth's moved end lands 0.02 qn after the second's moved note-on. The second eighth keeps c13's end, NOTE_END_AT[q+2.5] = q+2.52). Velocity v62 on both eighths: VEL_SET["Violins I"] at q+2 and q+2.5. The ART_SPANS `vel_by_cc` for the `_pq` entries must not override it; check the order. At v62 they play the 1-65 marcato layer, which mix.json already cuts 6 dB (row_dyn_db vel<66 -6). c14 showed that velocity sets the layer and not the level on this row.
- b) Eighths on "Sus MAX" (as the tutti pairs): drop the nine `_pq` entries from ART_SPANS["Violins I"] (or ART_AT q+2 / q+2.5 -> "Sus MAX"), with the same 0.02 qn overlap and the tutti pairs' re-attack lead.
- Acceptance:
  - trough between the eighths 8 dB or less (the tutti pairs' median);
  - eighth 1 at 2-5 kHz 0 dB or less over the staccato before;
  - eighths' perceived onset (pcx) within 25 ms of c27;
  - landing within ±2 dB of c27;
  - bar 23 figure (fig25 at 67; the head at 69 follows it) and bar 263 within 2 dB of c27.
  - The hole after the head (-9.6) should not deepen. A partial decay after a p accent is musical, so this is not a target.

### 3. Tutti accent fronts sit 1.0-1.8 dB under their staccato neighbours. On these bars the accented half notes are the downbeats (315, 327, 345, 351 / 915 ...), so this is also the missing tutti downbeat weight. c27's earlier body dip pulls CC11 down inside the first 100-250 ms of a slow-attack sustain (measured; the attribution between the dip and the removed leads is inferred)

Where: Violins I / II, cor anglais, Clarinet 2 and Oboe 1, the accented half notes in 312-360 / 912-960.

Evidence:
- A's measure (first 100 ms over the unaccented notes within ±2 qn, `records/acc_down.txt`, c26 -> c27):

| track | c26 | c27 |
|---|---|---|
| Violins I | +0.1 / -1.4 | -1.2 / -1.5 |
| Violins II | -1.3 / -1.3 | -1.4 / -1.3 |
| cor anglais | +0.9 / +0.2 | -1.4 / -1.8 |
| Oboe 1 | -0.4 / -1.0 | -1.0 / -1.0 |
| Clarinet 2 (got its bump) | -1.2 / -1.3 | -0.6 / -1.0 |

  Dan's target is +1..+2. Master downbeat over beats 2-3, 312-360: +0.3 -> 0.0.
- CC11 under the accents (c27 parts.json): Violins I rises to 115-117 and starts falling at the beat + 0.25 qn (57 ms): 315.25 115 -> 316.23 97, 345.375 116 -> 346.23 96. Violins II peaks at only 108-110 (add_loud 6), falling 0.1 qn after the beat.
- The Sus MAX sample peaks 0.18-0.26 s after the beat, so with Opus's ~120 ms CC11 smoothing the dip (body_s 0.14-0.24 s) lands on the attack's bloom. c27 changed both the dip (0.22 -> 0.14) and the leads (Violins I 0.04, cor anglais 0.05 removed). Violins II had only the dip change and did not move. CHANGES: "the body dip and the violas' cut do not make a downbeat".

Fix (`build/score_config.py`):
- `C27_BODY` off, so body_s goes back to (0.22, 0.36) on the six tracks. The switch exists: run the range test with C27_BODY=0.
- `_ACC_BY["Violins II"]` add_loud 6 -> **10** (top 124; its peak CC11 108-110 has room).
- Violins I add_loud 12 -> **14**.
- Keep c27's lead removals (they put the -6 dB point on time: Violins I +33 ms).
- No envelope change.
- Range test 312-360. Acceptance: A's measure +1..+2 on Violins I / II and cor anglais, none over +3; peak 0.20 s or earlier; 2-5 kHz front minus body 0 dB or less (no bite); master downbeat over beats 2-3 at +1 or more; the soft heads (CC11 under 98, add 3) unchanged.

## Not ranked

- The soft heads' hole after the marcato (0.21-0.39 s mean -9.6 dB; c18 -8.6). The actor's range test found marc_lift +14 "barely helps". It is the marcato sample ending (manual p.91-92). Finding 2's variant a) (the overlap) partly covers the end of it. I propose no larger lift: a decay after a p accent under a slur is what a player does.
- Violins I staccato ring (c26 A #5: Stac RRx14 / Staccatissimo isolated quarters to -20 dB 271-291 ms against 206-251 on the other rows) is still not run. Finding 1 adds 32 notes to those rows. Run the ring test (STAC_MIN_SOUND_S 0.14 on the rest path, a 220 ms any_dyn cap) in the same range pass if lock time allows.
- Not re-measured (no data change since earlier A reports): pizzicato / arco changes, harp, timpani rolls, con sordino, sul A, the re-bows of the held notes, the solo violin.

Do not touch:
- the c26 woodwind figure state (SLUR_END_BEFORE_STAC 35 ms, 120 ms caps, f trails -6 dB, Oboe 1 v118);
- the strings' bar 23 treatment (fig25 bar 23 last step now 12.4);
- the Spiccato rows and their layer cuts for the 40 pair notes (pair separation 4.5-6.5 dB);
- c27's soft-head marcato cut (vel<66 -6) and marc_lift (head 2-5 kHz front +6.3 -> +3.2);
- Clarinet 2's new accent bump (-1.2 -> -0.6 dB, peak 0.16 s in 299-362);
- the soft legato heads' CC11 front (SOFT_LEG_HEAD_CC; -6 dB point 213 -> 131 ms);
- the summit's "Sus Marc LITE" stroke;
- the 150 ms short-row caps on Violins II and the violas.
