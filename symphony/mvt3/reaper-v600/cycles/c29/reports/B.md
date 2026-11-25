# Cycle 29, critic B (balance and levels), on the c28 render

Sources: the c28 stems and master (`cycles/c28/render/`), the c27 stems for before/after comparisons, `cycles/c28/parts_rendered.json` (tempo map, notes, CC lanes), `build/mockup-events.tsv`, `build/roles.json`, `build/mix.json`, `build/score_config.py`, the c28 actor logs (`logs/guard28_net.txt`, `logs/stops.log`), the c27 and c28 mp3s, the Dvořák 9/i reference, score pages 3, 15 and 16, and the read-only `.rpp` (volume-envelope points only). Levels are K-weighted power from 40 ms frames at a 10 ms hop. "Rel" means a stem against the sum of the 31 dry stems in the same window. "Lead" means a line against the loudest other stem. mp3 bar levels are K-weighted bar means with the 0.30 s head removed. Scripts were in my scratch folder (deleted).

## Manual notes

MANUAL-READING.md has no row for cycle 29 (third round: pages chosen by the open problem). I read pages 91-92 (string long articulations) and 122-125 (timpani) in full for findings 1 and 6, and used MANUAL-GAPS.md.

| What the manual says (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| Harmonics exist only in the 2nd Violins (all two octaves over the fundamental). In other sections, a Sustain played pp with the Mod Wheel (CC1) at 0 gives a similar breathy, non-vibrato sound to Flautando (p.92). | Violins I printed "harm." B flat 5, pp, bars 43-50 (qn 168-199) | No. It plays on Leg Slur MAX with CC1 39-42 (vibrato layer) and is the second-loudest stem in bar 43 (finding 1). |
| Sustain has three vibrato levels on CC1; CC11 sets dynamics (p.91, p.64) | Every string pad | Yes. CC11 sets the level and CC1 the vibrato. The transition pad sits at the movement's p level even though pp is printed (finding 1). |
| Hard mallets: "brighter timbre overall than ... felt"; rolls with "clear individual hits" (p.124-125). Felt: "blended timbre" (p.122-123). | Printed: hard sticks at 0, soft sticks 680-711, hard 711, medium 856-1016, hard 1016 | Partly. Timpani Hrd KS plays the whole movement. In the medium and soft spans the rolls sit at rank 12-21 and are darker than the hard ff roll (2-5 kHz minus 30-150 Hz: -24 dB against -17.7 at bar 39). No change (check list). |
| CC7 sets the track level inside Opus, before the hall send (p.64, p.151; MANUAL-GAPS "CC7") | Trims and role carries in CC7 (`dyn_trim_to_cc7`, `ROLE_EDGE_IN_REST`) | Yes. The in-note items in finding 5 are CC7 steps at note-ons, not track-envelope cuts. |

## Findings, ranked by what a listener on earbuds would hear

### 1. Transition, bars 43-50: the motive-x solos are level with the pp string pad, and Violins I play their printed harmonic as a normal full-section note (measured)

**Where:** qn 168-199. Flute 1 (bar 43, p), Clarinet 1 (bar 45, p) and Oboe 1 (bar 47, p) pass motive x over held strings marked pp (Violins I "harm.", "change bow at will"), with Horn 4 pp dolce.

**What is wrong:** each solo leads the loudest other stem by only +1.3 / +3.1 / +2.0 dB (median of 2 qn windows; p10 -0.6 / -1.1 / +0.1). Each solo is also 2-4 dB under the accompaniment sum. In the first bar of each solo the solo is under a string stem:
- Flute 1 at 168-172: -0.6 / -0.4 dB against Horn 4 / Violins I.
- Clarinet 1 at 176: -1.9 against Violins I.
- Oboe 1 at 184: -0.7 against the violas.

The string pad is louder than its pp marking. Violins I, Violins II, violas and celli measure -45 to -50 dB each here. That is 4-9 dB over the movement's median for string notes marked pp (-53.8) and level with its median at p (-45.4). This is the only place in the movement with that inconsistency.

Violins I are the worst case. The printed harmonic B flat 5 plays as an ordinary Leg Slur MAX note with CC1 39-42 (the vibrato layer). It measures -44.2..-52.9 dB, with a spectral centroid of 1.5-1.8 kHz. It sits a few semitones over the flute's line and is the flute's main rival in bar 43. A real harmonic at pp is a faint, thin sound, far under a flute at p. The manual (p.92) gives the substitute for sections without a harmonics patch: Sustain at pp with CC1 at 0.

**Fix (`build/roles.json` and `build/score_config.py`; every edge in a rest):**
- roles.json: Violins I [167.9, 199.0, -6.0]; Violins II, Violas, Violoncellos, Double basses [167.9, 199.0, -3.0]; Horn 4 [167.9, 186.5, -2.0].
- Solo rows: Flute 1 [168, 176] 5.0 -> 7.0, Clarinet 1 [176, 184] 4.0 -> 6.0, Oboe 1 [184, 192] 4.0 -> 6.0.
- `INSTR_POST["cc_cap"]["Violins I"]` append `{"lane": "cc1", "pts": [(167.9, 0), (198.9, 0)]}` (non-vibrato, manual p.92). CC1 is not an Opus state change, so no rebuild.
- Delivery: raise the transition's ride row (the 163.95 row in `RIDE_TRIMS`) by +1.0 dB over 168-199, so the passage keeps its level on the mp3 for p10.

**Expected:** simulated on the c28 stems, the per-window leads go from -0.6 / -0.4 / +2.9 / +3.3 (flute), -1.9 / +0.7 / +5.4 / +6.9 (clarinet) and -0.7 / +2.1 / +1.9 / +8.1 (oboe) to +1.4..+11.8; no window stays under +1.4. The passage sum falls 1.5 dB before the ride. The CC1 change is untested on level: it may lower Violins I by a further 1-2 dB (inferred).

### 2. Bar 271: the 1079.5 ride row cancels the crescendo's arrival, and 271-273 stay under bar 255 (measured on the mp3)

**Where:** qn 1072-1096. Timpani, Trumpet 3 and Tuba crescendo through 269-270 into ff at 271 (Trumpets 1-2 and trombones join at ff). Bars 271-272 are the allargando; 273 is the Largamente.

**What is wrong:** on the master, the crescendo arrives: 1078-1080 -21.0 dB, 1080-1082 -18.7 (+2.3). On the mp3 the c28 row steps to -2.0 dB exactly at 1080, so the arrival disappears: 1078 -13.6, 1080 -13.3, 1082 -13.2 (bars 269 / 270 / 271: -13.4 / -13.3 / -13.3). Bars 271 / 272 / 273 measure -3.3 / -1.7 / -2.1 against bar 255 (-9.9). The actor's measure gave -1.9 / -1.4 / -2.4. Either way, the coordinator's target is "within 1.5".

**Fix (`build/score_config.py`, the c28 ride block, the 1079.5 row):**

`[(1079.5, 0.0), (1083.5, 0.0), (1084.0, -1.0), (1096.0, -1.0), (1104.0, -3.0), (1107.8, -3.5), (1107.95, 0.0)]`

(was -2.0 from 1080 to 1096). The 0.5 qn ramp at 1083.5-1084.0 is a delivery ride over a passage, which the rule allows.

**Expected:**
- 271 about -11.3: +2 dB over bar 270, so the arrival is heard again, and -1.4 against bar 255.
- 272 about -10.6 (-0.7 against 255). Its loudest half-bar (1084) goes from -10.6 to -9.6, 1.6 dB under the final chord's -8.0, so delivery item 2 holds.
- 273 about -11.1 (-1.2 against 255).
- Bars 275-276 rise up to +1 dB on the ramp to -3.0.

Re-run the delivery. Revert to -2.0 at 1080-1084 if the final chord's lead over any rival falls under 0.5 LU or limiting goes over 6 dB.

### 3. Oboe 1's solo, bars 95-97, enters level with a held chord that the score gives to the last two desks (measured)

**Where:** qn 376-392. Oboe 1 "solo, espress." mf > p. The held chord is mp > p: Violins II, violas and celli "sul tasto, last 2 desks", basses "last desk", Bassoon 2 mp, Horns 3-4 p. Clarinet 1 pp dolce at 386.

**What is wrong:** in the oboe's first bar it does not lead: -2.9 dB against Bassoon 2 (376-378) and 0.0 against the violas (378-380). It is 8.1 / 3.2 dB under the accompaniment sum, and it leads only in its own 500-2000 Hz band (+2..+4). It then leads by +6 / +8 in 380-384. At 386 Clarinet 1, printed pp, is 1.8 dB over the oboe's printed p.

The strings play full-section patches at an unreduced level. Two desks of a 12-14-player section are about 5 dB softer (10 log10(4/12)); one desk of basses is about 6 dB softer. The score's own note (clos.ily c224) marks the chord one level under the solo so that the solo comes through.

**Fix (`build/roles.json`, edges in the rest after the bar-94 stop and at the 392 tutti re-attack):**
- Violins II, Violas, Violoncellos [375.9, 391.9, -4.0]; Double basses [375.9, 391.9, -6.0].
- Bassoon 2, Horn 3, Horn 4 [375.9, 391.9, -2.0].
- Clarinet 1 [385.9, 391.9, -3.0].

**Expected (simulated):** per-window leads -2.9 / 0.0 / +6.0 / +8.4 / +5.2 / -1.8 -> -0.9 / +4.0 / +10.0 / +12.4 / +7.2 / +1.2. The passage sum falls 1.5 dB. The oboe's level and the 392 tutti are unchanged.

### 4. Trumpet 1 at 989 and the fff trims under ff: verified, with values (measured)

**Trumpet 1 at 989** (Più allegro head, tenuto, printed f). Per-note p90 over 0.05-0.4 s:
- Trumpet 1: 988 -34.3, 989 -34.6, 991 -30.5, 992 -34.2.
- 989 is -2.2 dB against mean(988, 991) by my measure (the actor measured -3.5). The unmarked 991 is still the loudest note of the head, +3.7 dB over 992.
- Trumpet 2 with CC1 -6 at 989 measures +0.7 over its neighbours, inside the 0..+3 target.
- In this span Trumpet 1 changes about 0.4 dB per CC1 unit (987.5: CC1 103 -> 97 gave -2.4 dB from c27 to c28).

Fix (`build/score_config.py` c28 block): Trumpet 1's 989 CC1 offset -12 -> -6 (CC1 86 -> 92, the same offset as Trumpet 2), expected +2.4 dB. Also take Trumpet 1's 991 CC11 cut from -5 to -8 dB (k 20, same window 990.70-991.75), expected 991 about -33.5. Result: 989 about +1.3 over mean(988, 991), and Trumpet 1's range over 984-998 falls from 8.5 to about 6 dB.

**fff trims under ff** (`build/mix.json` `dyn_trim_db`):
- **Trumpet 3** (ff 14.1, fff 12.6). Through the printed crescendo 1040-1048 into the fff of 263, the body level goes 1046 -25.0 -> 1048 -24.3 (+0.7 dB). The note-on step is +0.4 against an accented 1044 at -21.5. The 1.5 dB trim drop is part of why the crescendo does not arrive. Set fff 12.6 -> 14.1. Expected +1.5 dB at 888, 1048 and 1108 (master about +0.1 dB). The trims are in CC7 under the track's largest trim, so the envelope maximum does not change.
- **Horn 1** (ff 2.6, fff 1.9). Horn 1 rises +6..+8 dB into every fff (887 -29.1 -> 888 -20.9; 1047 -30.1 -> 1049 -22.4). No reversal is heard. Leave it.

### 5. In-note net-level items, harp 952 and the +24 dB envelope limit: none is an audible fault on the stems; next steps (measured)

**Net gate (14 / 6 / 8; 10 are timpani roll CC7 shapes, which are allowed as printed roll shapes).** I traced each of the other 18 on its stem (K level in 50 ms steps from -0.3 to +0.6 s):
- **Violins I 892 (-4.2), entry.** This is the printed fff -> mf at a new note. The stem falls 17 dB over 0.1-0.2 s after the 892 note-on, in CC7, before the hall. Keep (printed subito).
- **Flute 1 136 (-1.6), Clarinet 1 135.75 / 135.77 (-3.1), violas 823.5 / 823.55 (+1.7).** Each step lands on the new note's attack; the stem shows the attack, not a step inside a sustained sound. Keep.
- **Violins I 487.5 / 488 (+1.6 / +2.1), violas 15 / 16 (-1.5 / -1.6), Horn 3 564.87 (+1.6 over 1.4 s), Violins I 896-899 (+1.5-1.6 three times, at 3.0-3.2 dB/s).** These are smooth rises of 3-4 dB over 0.6-0.9 s, in crescendos by addition or the carry. They are heard as swells, not steps. Keep. The rate gate (3 dB/s) and the carry rate (2.5 dB/s) disagree only on the short notes at 896-899. If the actor wants the gate clean, set `ROLE_EDGE_IN_REST["carry_rate_db_s"]` to 2.5 for notes over 1.5 s and let the rest of the move fall in the next rest.
- **Violoncellos 951.48 (-4.7), Double basses 951.78 (-4.2), inside_dyn.** These are CC7 trim steps 25-40 ms before the led 952 note-on. On the stems the new note rises +11 dB at that moment, so the old note's last 40 ms are covered. For a clean gate, extend `TRIM_CC7_ONSET_QN` to snap points within 0.1 qn *before* a moved note-on to 0.003 qn before it (now only points after the note-on are snapped).
- **Violas 1088 (-2.1).** A CC7 fall at the tune -> tremolo change (ff -> ff). The stem drops 8 dB, mostly from the row change; the violas in 273 sit 5 dB under Violins II, which is acceptable for an inner tremolo. Keep.
- **Bassoon 1 320 (+2.4, c26 variant C swell).** There is a 6-7 dB hole at the 318 -> 320 join after the printed decrescendo, then the swell. The note sits 25 dB under the master under the violins' F2. Inaudible (inferred). Keep.

**Harp 952** (printed p -> mf at a new chord). The 2.9 dB envelope rise comes with the velocity rise 64 -> 90 (about +6 dB through the Velocity->Volume path). The harp measures -44.4 at 950-952 and -37.4 at 952-954 (+7 dB). Four earlier notes still ring under the new chord's attack, 3-9 dB under it, so the rise is covered (inferred). Leave it. If the actor wants zero step at 952, make it level-neutral in the instrument: roles.json Harp [952, 968] -3.0 -> -5.9 and velocities 952-967.9 x1.17 (cap 127), which gives +2.7 dB through the velocity-squared law measured in c22.

**Envelope at +24 dB.** I read the `.rpp` volume envelopes:
- Horn 3 reaches exactly +24.00 dB at 1018.0 and 1019.0 (two points). Its envelope is 14.0 + vol_db everywhere (1016 +22.0, 1018-1019 +24.0, 1021 +22.09), so the c28 shape is not clipped, but it has zero headroom.
- Trombone 1 peaks at +23.60 (984.35-1015), Tuba at +23.50 (1107.9-1113). No other track is over +22.5.

Fix: none for c28's data. In c29, do not raise any envelope row on Horn 3 at 1016-1021, Trombone 1 at 984-1015 or Tuba at 1108-1113. D_VOL cannot take the excess (build_reaper.py line 740: REAPER ignores it under an envelope). Any lift there must come from CC1 / CC11 / velocity.

## Other checks in this lens

- **Solos (lead / p10, c27 -> c28):**
  - Trumpet 1, bars 51-66: +5.1 / +1.7 -> +9.0 / +5.8 (my K measure; the actor's band measure gave +7.3).
  - Violins F2, bars 67-82: +4.8 / +1.1 -> +7.1 / +3.0.
  - Bassoon 1, bar 115: +9.4 / +5.5.
  - Cor anglais with muted Trumpet 1, bars 171-186: +10.3 / +5.7.
  - Bass theme, bars 27-34: +8.6 / +6.0; violin countersubject +8.0 over the rest.
  - Theme B trumpets, bars 211-218: +6.5.
  - C-major violins, bars 187-198: +6.6 / +3.9.
  - F2 hand-over at 123-130: celli +5.7, violas +1.9 (rival Bassoon 1's counter-line), Clarinet 1 +4.3, Violins I + Flute 1 +5.7.
  - The harp is no longer the soloist at 123-130 (dev.ily c033). Its arpeggios are 10 dB under, which is correct.
  - All measured. No change.
- **Arrival and ending (rel to the dry sum):**
  - Bar 223: Violins I -10.4, Trumpet 1 -10.8, timpani -15.6, bass drum -21.7, crash -13.4.
  - Final chord: timpani -11.8..-12.5 (rank 6-7), bass drum -20, crash -12.3, tuba -14.
  - Crash cymbals: -11.6 / -9.5 / -12.3 rel in their first 0.5 s at 223 / 263 / 278; heard, not dominant.
  - Low brass and timpani do not cover. Measured. No change.
- **Chorales:**
  - 224-234: winds and Violins I lead the f brass, as printed (ff over f).
  - 255-256: the trumpets' held G4 sits level with each stem of the ff espressivo counter-melody (Horns 3-4, Violins II, violas, celli); the tune leads from 257 (-20..-24 against -24..-31).
  - Measured. No change.
- **Dynamic mapping (median note level by printed dynamic):**
  - p: winds -45.5, horns -45.7, trumpets/trombones -43.9, strings -45.4 (within 2 dB).
  - pp: winds and strings -53.7 / -53.8, but horns -45.8, because Horn 1's pp counter-line in 67-77 carries the accepted role +7.
  - The strings' pp pad in 43-50 is the one place where pp sounds like p (finding 1).
- **Accents** (against unaccented notes of the same track within +-2 qn):
  - Median +0.9..+2.2 dB, p90 +5.0..+5.9.
  - 2-5 kHz in the first 80 ms against the body: median -2.4..-11.5 dB.
  - Not overdone and no hard fronts (Dan c17). No change.
- **Timpani sticks:**
  - Timpani Hrd KS (Hrd Lng / Hrd Rls) plays everywhere. The soft-stick motive x at 708-711 (pp, near the rim, 4 notes) and the medium-stick span 856-1016 play on hard sticks.
  - Measured: the medium-span rolls rank 12-21 and are 6 dB darker than the hard ff roll, and 708 ranks 3rd (-12.5 rel) at its motive.
  - A felt instance would add an Opus instance at the memory limit. No change in the last cycle.
- **Low-end check** (scherzo c28: quiet passages too heavy).
  - The quietest quarter of the c28 mp3 has a 20-150 Hz share of -9.8 dB (Dvořák -12.8 by the same method; Movement I c62 -7.9) and 500-2k -3.6 (Dvořák -3.1).
  - The dry stems give -10.8..-13.4 in the solo passages, the basses supplying 61-84%.
  - Applies weakly (3 dB, not 5). No change.
- **Tenuto downbeats on loud tutti chords** (scherzo c28):
  - Does not apply in the same form. Our low-brass tenutos are the tuba's in the counterstatement, and there the tuba's downbeats stand +3.3 dB over beats 2-4.
  - In the recapitulation (600-640) the bass trombone and trombones play half notes on Sus MAX that peak 240-280 ms after the onset (median). The downbeats stand only +0.3..+0.5 dB over the other beats.
  - A swell per half note, outside my lens's safe fixes (a Portato or Marc Lng test needs a range render). Reported, no change.
- **Stops:** bar 113 is 17.3 dB (0.3 over the band; the others 15.8-16.9). 0.3 dB is within render variance. Leave it.
- **Subitos:** the sfp at 592 drops 7 dB in 0.2 s and the sub. p at 872 drops 9 dB over 0.4 s, both in CC11/CC7 with the hall ringing. Fine.
- **Other-movement findings:**
  - Scherzo c24 note_slew: covered by our 2.5 dB/s carries (finding 5).
  - c25 trims on moved time: done in c28 (`TRIM_CC7_ONSET_QN`); finding 5 asks for the before-onset half.
  - c25 / c26 +24 dB envelope: checked, finding 5.
  - c27 fff trims under ff: finding 4.
  - c27 arrival fades after crescendos: the hold rules are in place; no 1-5 dB unprinted fade was found in my traces.
  - The Violins I Spiccato, round-robin, mono-oboe and woodwind release items belong to lens A and are not measured here.

Do not touch: the trumpet solo roles and CC1 cap/targets (lead +9.0); the 67-82 roles; the cor anglais / muted trumpet balance; the counterstatement bass balance; theme B trumpet roles; the chorale tremolo levels; `TIMP_ARRIVAL_RAMP`, the 1108 roll CC7 and the crash / bass-drum levels; the accent levels (median +1-2 dB, no bright fronts); trims in CC7 with the moved-time snap; the ROLE_EDGE_IN_REST carries; the bass clarinet CC7 at 261; Horn 1's counter-line role 7; the room bed and the -14 LUFS delivery with the c28 rows other than the 1079.5 row.
