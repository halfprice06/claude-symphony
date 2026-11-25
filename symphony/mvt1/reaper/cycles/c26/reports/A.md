# Cycle 26, critic A: articulation and phrasing (render c25)

Scope: every wind, brass and string note in `build/parts.json` (c25 after its stem fixes), measured on the c25 stems and master, with c24 (`cycles/c24/rendered_build/parts.json`) as the control. Both renders were measured from 5 ms feature caches. I reran the c22-c25 battery on c25: kscheck, ties, chordleg2, joins, acchf, stacsep, tremj, timp, harp, pz3, breath, ten200, cutoffs, rebow, longloop, reltime, relburst2, rests2, accpk2, accshape, pairs, rrcyc, detw2, efchk2, sstart, ssj, pkr3 and xall (extended to the solo winds and Horn 1). New scripts:
- `bacc.py`: arrival and peak time of every accented and plain note, by family.
- `spike.py`: legato-target bursts over both neighbours.
- `mhole.py`: master holes at legato joins of tracks within 6 dB of the master.
- `arr.py`: legato-target arrival time.
- `hem26.py` / `who539.py`: hemiola steps per stem.
- `hf.py`: 2-5 kHz share per 40 ms.

Score pages 6, 11 and 15 were checked, along with `mockup-events.tsv`. Scratch files are in `/private/tmp/claude-501/mockup-loop/mvt1-c26-A/`.

## Checks that passed (measured, no action)

- **Keyswitches, chords on legato rows, ties.**
  - The shortest keyswitch lead is 14 ms.
  - No chord goes to a legato row.
  - Every keyswitch inside a sounding note is a planned row change.
  - The only tie re-attacks are the timpani re-strikes and the basses' re-bows.
  - All of these are unchanged from c24.
- **Legato joins (stems).**
  - No wind or brass join is 6 dB or deeper, except Clarinet 1 227 (6.2 dB, which c24 accepted).
  - Strings with joins of 6 dB or more: Vln II 2, violas 3, celli 2.
  - Every one of those is masked on the master. Celli 112 dips 8.1 dB on the stem and the master moves under 1 dB. Violas 361.5 is 17 dB under the master. Vln II 637 is the crash arrival.
  - Medians match c24 within 0.3 dB.
- **c25 changes, no side effects.**
  - The Oboe pair extras moved no other Oboe 1 join; Oboe 1's median join dip is 3.2 dB, against 2.7 in c24.
  - The hemiola swells and the breath splits left the joins, cut-offs and rests within 0.5 dB of c24.
- **Brass accent timing (c25 open item), measured closed.**
  - The c25 open note says the peak median is still +0.20 s. The level gets there much sooner: the brass accents reach peak - 3 dB at +0.030 s after the score onset (median; p75 +0.060, n 74).
  - For comparison, plain brass notes reach it at +0.040 s, string accents at 0.000 s and wind accents at +0.010 s.
  - The later peak (median 0.17 s) is a bloom of 3 dB or less on a note that is already at level.
  - Recommendation: stop. A faster row such as `Marc Sus LITE` (in every brass KS Master, never tried on brass) would only add attack brightness. That is Dan's item 8, and Trumpet 1 is already the brightest stem (next point).
- **Item 8, accent bite.**
  - Stem 2-5 kHz first 80 ms minus body: brass median -8.1 dB, winds -3.9, strings -3.3.
  - The flagged outliers are mostly the previous note's tail:
    - Violas 536 (+16.0), celli 536 (+11.7), Bassoon 1 536 (+8.5): the bar-135 accents are mf after f bars; the front window holds the f dyads' release, and the accented notes sit 8-11 dB under it.
    - Clarinet 1 558 (+8.8): the previous note is brighter than the accented one.
  - Trumpet 1 284 is +7.0 on its stem (c24 +7.6), but on the master only +1.6 front-body / +3.5 front-pre. Trumpet 1 670 is +4.7 on its stem and +2.8 on the master.
  - No master accent jumps more than +3.5 dB at 2-5 kHz, except the violas' qn 354 (+7.0 front-body), which was known in c25.
- **Item 7, loop pulse.**
  - Re-bow medians: Vln I -3.0, Vln II -2.1, violas -2.3, celli -2.5, basses -1.4 dB; master median -1.2..-3.0.
  - The two large steps are both printed diminuendos: celli 163.877 is the ff-to-p diminuendo (CC11 114 -> 40), and celli 727.116 is the morendo.
  - The longloop values of 0.5-0.66 (violas 50, celli 11, basses 48) come from 6-8 s spans cut into 2-4 pieces. Too little overlap remains at a lag of 3.95 s, so this is not a loop pulse (the actor's merged-span scan agrees).
- **Other articulations, all within 1 dB or 0.02 s of c24.**
  - Staccato separation: winds 8-11.6 dB, strings 8.8-14.1 dB.
  - Pizzicato: -10 dB point +0.007 s.
  - Tremolo arrivals: stem median -1.1 dB.
  - Breath gaps: the Horns a2 track dips 6-7 dB at 475 and 4-5 dB at 636. breath.py reads "0.0" on Horn 1/2 there because their notes are routed to the a2 track.
  - Tenutos, release bursts and tutti cut-offs (the master at -10 dB by 0.13-0.25 s).
- **Other techniques.**
  - The harp étouffez and arpeggio rolls, the timpani soft-stick strokes (felt sticks, as printed, all movement), and the sul tasto EQ on the Violins II tremolo (bars 147-155) are in place.
  - The two Leg Port MAX joins are also in place: 225 sul A (Vln I -2.1 / Vln II 3.3 dB) and celli 685 (3.0 dB).

## 1. The dolce second theme (bars 49-50 and 149-150, celli + Horn 1): the c24 shapes boost a transition burst and step down into the beat-3 join (measured)

**Where.**
- Violoncellos and Horn 1, the theme's top-note bar.
- Exposition: qn 195.5 -> 196 -> 198.
- Recapitulation: qn 595.5 -> 596 -> 598.
- Score page 15 (and page 6): the celli and Horn 1 are in unison, slurred. There is a `<` into the half note at 196/596 and a `>` across bar 50/150. The half note at 198/598 is in the middle of that diminuendo, under a new slur.
- The celli are the loudest stem here: -0.4 to -3.8 dB re master.

**Evidence (measured).**

(a) The rise into 596 sits on a legato transition burst.
- The c24 C #1 shape reaches +6.0 dB at 595.92: `score_config.py` line 1335, `[(595.65, 0), (595.92, 6.0), …]`.
- The celli's 596 C4 is a Leg Slur target moved to 595.625. Its transition burst falls at 595.69-595.87.
- So the full gain lands on the burst, not on the note. Celli stem level re score 595.5:

  | +0.0 s | +0.10 s | +0.20 s | +0.30 s | +0.40 s |
  |---|---|---|---|---|
  | -36.8 | -27.0 | -24.5 | -32.8 | -33.5 |

- That is an 8.5 dB burst about 0.15 s long over both note bodies (`spike.py`; second-largest of 96 flagged joins). The master rises +3.6 dB with it.
- The 596 body after the burst (-33..-35) is no louder than 595, so the printed `<` peak is not reached either.
- Exposition 195.5 has the same shape (line 1334, full +6.5 at 195.9): the celli burst is +6 dB (-28.6 against -35).

(b) The join into 598/198 steps down 5-7 dB.
- The same shapes return to 0 just before the next join:
  - celli exposition 4.9 dB at 197 -> -0.8 at 197.95;
  - celli recapitulation 6.0 -> 1.2 at 597.98;
  - Horn 1 `[(596.1, 0), (597.9, -4), (598.05, 0)]` (line 565): vol -5.7 at 597.73, and exposition 7.65 -> 2.15 at 197.9.
- The celli's 598/198 target starts 0.22 s early (moved 597.589). The Leg Slur sag (kit LEARNINGS section 6) therefore falls inside that downward ramp.
- The c25 auto fill at 598.0 (+5 dB, from the score onset) starts after the sag has begun. efchk2 lists the celli at 598 as still dipping 6.1 dB at -0.03 s through an existing +5 dB fill. Horn 1 at 198 dips 7.0 dB through its fill.
- Master, 0.05 s frames re the score onset of 598 / 198:

  | | -0.6..-0.2 s | lowest | +0.5 s |
  |---|---|---|---|
  | 598 | -29.6 | -34.0 at +0.25 | -30.6 |
  | 198 | -30.0 | -38.0 at -0.05 | -34.5 |

- This is a hole of about 4.5 dB (recap) and a 5-8 dB step down (exposition) on beat 3 of the theme. The printed diminuendo calls for a gradual fall across the bar.
- kit LEARNINGS section 6: "do not taper or ramp down into a note that the next note joins". The standard joins check passes these joins (celli 198 2.0 dB, 598 4.3 dB) only because its pre-window already sits on the ramp-down.

**Fix.** This is a level-only change on a MIDI-identical build, so the actor can apply it as a stem fix on Violoncellos and Horn 1. Simulate it on the c25 stems first.

In `build/score_config.py`, c24 C #1 block:
- Celli recapitulation: replace `[(595.65, 0.0), (595.92, 6.0), (597.0, 5.0), (597.9, 2.0), (598.1, 0.0)]` with `[(595.65, 0.0), (595.95, 0.0), (596.15, 6.0), (597.0, 5.0), (598.6, 3.0), (599.6, 0.0)]`.
- Celli exposition: replace `[(193.2, 0.0), (193.45, 2.0), (195.6, 2.0), (195.9, 6.5), (196.6, 6.0), (197.6, 4.0), (198.2, 0.0)]` with `[(193.2, 0.0), (193.45, 2.0), (195.6, 2.0), (195.95, 2.0), (196.15, 6.5), (196.6, 6.0), (198.6, 3.0), (199.6, 0.0)]`.
- Add `JOIN_NOTCH["Violoncellos"]` entries `(595.66, 595.92, -5.0)` and `(195.66, 195.92, -4.0)`. These cover the burst. Per kit LEARNINGS section 5, make each notch span the burst positions seen in the last two renders; c24 and c25 are identical here.
- Horn 1: replace `[(596.1, 0.0), (597.9, -4.0), (598.05, 0.0)]` and `[(196.1, 0.0), (197.9, -2.5), (198.05, 0.0)]` with a fall that does not return at the join: `[(596.1, 0.0), (599.5, -4.0), (599.75, 0.0)]` and `[(196.1, 0.0), (199.5, -2.5), (199.75, 0.0)]`.
  - Both returns end before the moved 600/200 onsets (599.845 / 199.845).
  - Lower the c24 C #1 Horn 1 point `(197.6, 4.0)` to `(198.6, 3.0)`, as for the celli.
- Then rerun `tools/auto_fills.py` for Violoncellos and Horn 1 at 198/598 only.
  - Start the fills at the moved onset + 0.10 s (`pre_s`), not at the score onset.
  - Use the overshoot rule against the 30 ms peak (kit LEARNINGS section 6).

**Pass.**
- Celli stem at 595.5 +0.1..+0.25 s no more than 3 dB over the higher of 595 and 596.
- 596 body (+0.3..+0.8 s after 596) at least 1 dB over 595.
- Master minimum from -0.1 to +0.4 s around 598 and 198 no more than 2.5 dB under the mean of the 0.4 s before and the +0.5..+0.8 s after.
- Bar 50/150 master level falling monotonically (0.25 s means) from 596 to 600 within ±1.5 dB.
- Horn 1 and the celli still within 2 dB of each other over each half note.

## 2. Doubled lines still play one sample at +3 dB: Horns 3-4 a2 at bars 79-81 and the trumpets a2 (patch; inferred, carried from c25 A #4)

**Where.**
- Horn 3 + Horn 4 a2: qn 316.5-322.5 (f, two accented pickup figures) and 628-640.
- Trumpets 1-2 a2: 664.5-676 (the coda theme, ff, with Horns a2 and violas) and 520-524.

**Evidence.**
- Measured: `unison_dropped` is Trumpet 2 = 21 and Horn 4 = 18 notes, so each doubled line is one player's sample at +10·log10(2) dB.
- Measured: Horn 3 317 / 321 are the brightest horn accents (stem 2-5 kHz front-body +3.9 / +4.0 dB; master -1.3 / -1.8). Trumpet 1 670 is +4.7 on its stem and +2.8 on the master.
- Measured: the 2FH a2 track is idle from 314.5 to 381.5 (`_A2W`).
- Inferred: a recorded two-player patch gives the width and the small pitch and timing spread of a2 playing, as the horns' 2FH track did (c13). By the same evidence, the solo patch with a dB boost cannot.
- c25 deferred this because both parts needed code and memory. Part (a) needs no new instance.

**Fix.**
- (a) Add per-window staff lists to `TRACK_WINDOWS` in `tools/score_to_parts.py` (`tw_spans`). Then route the Hn3 staff's 316.5-322.5 notes to "Horns a2", with Horn 3 / Horn 4 resting there.
  - Copy Horn 3's accent fits, the 317/321 c24 skips and its dyn trims.
  - Start the window level at the Horn 3 gain + 4.6 dB (the c13 offset), then set it from the render.
  - The Horns a2 track's shelves (static 1.25 kHz -3, loud 1.6 kHz -8) already apply.
- (b) Only if REAPER settles at 45 GB or less before the render: a Trumpets a2 track. Use `2 Trumpets/04 Legato/2TP Leg Slur MAX.oib` (a single articulation, Close + Main), for windows 664.4-676.5 and 520-524.5.
  - A disconnected note on a Leg Slur MAX patch plays its sustain layer (kit LEARNINGS section 5), so no keyswitch rows are needed.
  - Copy Trumpet 1's PICKUP_LIFT (664.5, 672.5), accent fits, ABUT_LEAD, the trumpets' 4 kHz shelf and the climax shelf.
  - Drop it if the settled footprint after the render goes over 47 GB.

**Pass.**
- Window levels within 1 dB of c25.
- Horn 317/321 stem 2-5 kHz front-body at +1 dB or less.
- Trumpet theme joins under 5 dB, with the theme accents at master 2-5 kHz +3 dB or less.
- Dan to compare once against c25 (no level measure separates "two players" from "one louder player").

## 3. Bars 135-137 hemiola: the accents are now on the stems, and what hides them on the master is the Violins I line, not articulation (measured; for the record, no articulation fix)

- After the c25 chain swells, every accented stem steps +1.9..+5.3 dB at 539 and 542:
  - 539: Bassoon 1 +3.0, celli +2.7, basses +5.3, Clarinet 1/2 +3.0/+3.2, Contrabassoon +4.8, Horn 3 +3.0.
  - 542: violas +6.7, Violins II +5.6, Horn 3 +6.9.
- The master moves only +0.5 / +0.7 dB, because the loudest stem, Violins I (-6.9 dB re master), falls 3.3 dB across 539 while those stems rise.
- Further accent swells would push the accents past the 4.5 dB cap without changing the master.
- If the cross-rhythm must be heard, the remaining lever is a balance choice for critic B: about -2 dB on the Violins I 538.5-546 notes. Articulation should leave this passage alone.

## Do not touch

- The c25 brass swell timing and refit: brass accent arrival is now +0.03 s and needs no row change.
- The c25 Oboe pair extras and the 90/498/538/582 fills; the hemiola chainfit swells.
- The c25 breath splits with their re-entry shapes.
- Everything listed under "Checks that passed": keyswitch, legato lead and cap tables, ABUT_LEAD, STAC_LEAD_S, STR_REST_SHORT, the re-bow times with rebow_fills (including the 711.855 fill), the Marc LITE strokes, the c24 accent cuts (`LEVEL_SHAPES_S`), Leg Port 225/685, the timpani, harp, pizzicato, tremolo and MEAS_TREM settings, and the Violins II sul tasto EQ.
- In the c24 C #1 shapes, change only the points named in finding 1. Keep the 193.2-195.6 rise and Horn 1's 193.2-196.6 points.
