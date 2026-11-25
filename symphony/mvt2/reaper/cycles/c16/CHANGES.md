# Cycle 16 changes (actor)

Snapshot of the c15 tools and build/*.json: `before/`. Scratch and analysis: `/private/tmp/claude-501/mockup-loop/c16-actor/`.
- `sim.py`: the level simulation on the c15 stems, including the loud EQ.
- `spec.py`, `win.py`, `checks.py`, `count_joins.py`, `overshoot2.py`: the checks below.
- `A/`: critic A's scripts, with `lib.py` reading `PARTS`.
- `splice.py`: the post-render viola fix.

## Process

1. Edited the following, then regenerated parts.json:
   - `tools/score_to_parts.py` and `tools/build_reaper.py`;
   - the new `tools/auto_fills.py` and `build/loop_fills.json`;
   - `build/{roles,note_trims,early_fills,pitch_trims,mix}.json`.
2. Simulated the level changes on the c15 stems (`sim.py` plus `deliver_master.py`): mp3 LRA 16.1 LU, limiter 2.3 dB.
   - Following C's own rule (LRA over 16), I took the Bassoon 2 and Contrabassoon climax lifts from +4 to +3.
   - Simulated again: LRA 16.0, limiter 2.2, span 18.8.
3. `build_reaper.py build/parts.json jobs --midi-only --tempo`:
   - Violas were fully rebuilt: the Detache row was unloaded and the Stac Leg row loaded.
   - The other 28 tracks were updated in place.
4. Saved and quit REAPER (it had 56 GB, 29 GB of it compressed), started it with `-new`, and opened the project with a bridge job. The load settled at 55 GB with 0 compressed.
5. One render (`render_cycle.py 16`). Attack gate 19 of 19, with no late notes or holes.
6. After the render, I found one regression from A #4 and fixed it without a second render.
   - **The regression.** Setting the slur of the violas' qn 262 note (an unslurred ff entry, 14 semitones above the previous note) made it a first Leg Slur MAX note instead of Sus MAX. It played 6-9 dB under c15 in bars 79-80.
   - **The tool fix.** The tied-slur rule now sets only the outgoing join (`slur_out`). Regenerating parts.json changed only Violas, which are now c15's data at 262-268 apart from the 6 CC bow notch.
   - **REAPER.** Violas were updated with `--midi-only Violas` and the project was saved.
   - **The stem splice.** In the rendered stem, qn 261.6-267.85 was replaced by the c15 Violas stem for that span, with the new-minus-old envelope applied (the B #3 -2.5 dB role) and 30 ms crossfades. The tempo offset there is a constant -0.0789 s. The master was rebuilt as the stem sum (the residual before the splice was -121.6 dBFS). Then measure, probe and delivery were rerun.
   - Like the c14 splice, this is a valid render of the data, not a sample-identical one. The 265 notch in the splice is c15's 14 CC, not the new 6 CC.

## Accepted

- **Reverts (c15 plan, A #6).** `DETACHE_SPANS = {}` and `ABUT_LEAD = {}`.
- **A #1, loop-seam fills.** New `build/loop_fills.json` (`{track: {onset: [[t_s, dB, width_s]]}}`, critic A's values).
  - `score_to_parts.py` adds a raised-cosine lift at each seam: t_s seconds after the note's moved start, on the real tempo map (`sec_to_qn`).
  - Overlapping lifts take the larger value, not the sum. The lifts are exact `vol_bp` breakpoints.
  - Applied to Cb 220/271/292, Vc 164/274/292, Vln I 0/292 and Vla 292 (43 lifts).
- **A #2, fix A.** `FLAUT_LEAD_S` 0.15 -> 0.45 s, `FLAUT_OVERLAP_QN` 0.35 -> 0.7, and roles Violins II [114,116,3].
- **A #3, test.** `STACLEG_SPANS = {"Violas": [(196, 200)]}`. Bar 59 plays the KS Master's "Stac Leg BC + Slur + Port MAX" row (key 44): v110, 0.02 qn overlap inside each slur, no lead. Bar 60 stays on Sus MAX as the control.
  - I checked the patch file: the KS row exists, and the standalone "Violas Stac Leg Slur + Port MAX" has rows Sus, legato slur and stac on bow RRx4.
- **A #4, bar 80 bow change.**
  - A slur that starts on a tied continuation is the merged note's outgoing slur (`slur_out`, `same_slur()`), so Vln I/II 266 joins on Leg Slur MAX instead of Leg BC MAX.
  - The notch for a printed bow mark inside a held note at f or louder is 6 CC (was 14).
  - There is no CC1 delayed-vibrato dip on a legato target at f or louder that is slurred to the previous note.
- **A #5.** `SOST_NOTCH` is not applied while `SOST_HOLD_THROUGH` is on (Flute 2 had 3 such notches).
- **B #1.** early_fills Oboe 1 "271" 7 -> 3; roles Oboe 1 [271,274,-4]; note_trims Flute 1 "271" +3.
- **B #2.** note_trims Oboe 1 "144" +7, "145.5" +3.
- **B #3.**
  - roles: Horn 1 [262,265.5,3], Bassoon 1 [262,265.5,2], Violas and Violins II [262.5,265,-2.5,0.25].
  - note_trims: Horn 1 "264" +2.
- **B #4.** roles: Violins I [244,262,2] -> [250,262,2], plus [237.5,250,-2.5,0.5] on Violins I, Violins II and Violoncellos.
- **B #5.** The Bassoon 2 peak at 268.18 came from the Eb3 +6 pitch trim plus the tail of roles [262,268,4]. pitch_trims Bassoon 2 `_skip_onsets` [268].
- **B #6, merged into C #1.** An 80 Hz -3 dB low shelf on the basses. It is not static as B proposed: it sits in the basses' level-dependent EQ (see C #1).
- **C #1, low octave at the ff tutti.**
  - roles `[200,214,dB,1]` and `[258,269,dB,1]`: Cb +3, Cbn +3, Bn2 +3, Tuba +3, BTbn +3, BCl +2, Timp +2, Vc +1, Vln I -1, Vln II -0.5. The second span ends at 269, not 272, so the bar 81 decrescendo is not lifted (B #5).
  - `build_reaper.py`: `set_mute_eq` now takes a list of wet points and an envelope shape. mix.json `loud_eq` {points, bands} adds a ReaEQ whose Wet follows the points linearly.
  - Vc and Cb get a 150 Hz +4 dB bell (1 oct), and Cb also the 80 Hz -3 dB shelf. Wet points: [199,0],[201,1],[213,1],[215,0],[257,0],[259,1],[268,1],[270,0].
- **C #2, measured fills.** New `tools/auto_fills.py PREV PARTS [--write] [--exclude Track:onset]`, run on c15. It wrote 110 entries to early_fills.json (88 new, 22 raised), each listed in its track's `_auto` key.
  - Excluded: Ob1 271 (B #1), and Fl1 271 and Ob1 145.5, which have note trims from B #1/#2.
  - Existing Vc entries were not raised (do-not-touch).
- **C #3, tempo.**
  - `PHRASE_ARCS` loses (42,48) and (54,60).
  - `TEMPO_PUSH`: (21,24,1.015), (78,84,1.02) and (250,259,1.025), each starting one beat in. C wrote 244-253 for bars 75-77, but bars 75-77 are qn 250-259.
  - `APEX_AGOGIC` 0.96 on the beat of the lead line's highest note. The lead line is the `LEAD_SPANS` track whose span started last, or `APEX_LEAD` {108: Flute 1}. The arc's first beat and its last two beats are excluded. This applied to 10 arcs.
  - `BEAT_STRETCH` {204: 0.94, 208: 0.94}.
  - Total length +0.23 s. Bars 75-77 now run at 53.3 bpm, and then the poco allargando ramp starts at 51.2.
- **C #4.** `METRIC_VEL` {downbeat +6, mid +3, weak -3} on pizz. notes and the harp. Not applied to accents or sf, inside LEAD_SPANS, or to the inner notes of rolled chords.

## Rejected or deferred

- **A #2 fix B** (Vln II divisi tracks): deferred. Fix A cleared two of the three troughs.
- **C #5** (wind vibrato shaping): deferred. It needs a CC1 response test first.
- **B #6 as a static shelf**: not done. Critic C's do-not-touch keeps the soft-passage spectrum, so the shelf is only in the loud EQ.
- **A #3 failed.**

  | Bar | Own-pitch share | First dominance | RMS |
  |---|---|---|---|
  | 59 (Stac Leg) | 0.39 | +0.020 s | -36.1 |
  | 60 (Sus MAX control) | 0.30 | | -32.8 |

  The pass needed a share of 0.5 and an RMS within 1.5 dB of bar 60. The test stays in this render and in the tools. Next cycle: set `STACLEG_SPANS = {}` (full Violas rebuild) and close the item. No HO viola patch plays these sextuplets clearly.
- **C #4 failed.**
  - The beat-1 lean is Cb +0.8, Vc -0.5, Harp +1.2 / -0.2 dB (target 1.5-3).
  - The Cb pizz. peak std rose from 1.7 to 3.3 dB (limit 3).
  - Next cycle: set `METRIC_VEL = {}`. The pizz. round robins dominate the velocity steps.
- **A #1 only partly worked.**
  - The lifts land where planned. For example, Cb 292 at +4.0 s went from -58.9 to -52.9 dB.
  - The detrended pulse barely moved:

    | Note | c15 p95-p5 | c16 p95-p5 |
    |---|---|---|
    | Cb 292 | 11.8 | 9.7 |
    | Vc 292 | 9.9 | 7.7 |
    | Cb 271 | 12.4 | 11.7 |
    | Vln I 292 | 10.5 | 10.2 |

  - The master's 30-200 Hz pulse in bars 89-92 is 14.1 dB (c15 13.9).
  - The real seam dips are wider than the fitted widths, and the lifted spots now leave the neighbouring frames as the new minima.
  - Refit next cycle from the c16 stems: a wider lift (about 2x the width) and depth from the local maxima, not 80% of the detrended dip.

## Measured, c15 -> c16

Each render is measured on its own tempo map.

**Delivery**

| | c15 | c16 |
|---|---|---|
| Master integrated | -23.6 LUFS | -23.0 LUFS |
| Master LRA | 23.2 LU | 23.6 LU |
| Master true peak | -4.5 dBFS | -2.9 dBFS |
| mp3 integrated | -19.8 LUFS | -19.8 LUFS |
| mp3 LRA | 15.9 LU | 16.1 LU |
| mp3 true peak | -1.6 dBTP | -1.6 dBTP |
| mp3 span | 18.7 dB | 18.9 dB |
| Limiter | 1.9 dB | 3.2 dB |

No clipping. All 29 stems are present.

- **The limiter.** The 3.2 dB is set by one peak: Violins II at qn 207.94 (the bar 62 legato join after the stretched 208 beat), 1.5 dB over the next master peak (-4.4 dBFS at 204.1). The other climax peaks match c15 (-4.4..-4.7). The simulation had predicted 2.2.
- **mp3 sections** (RMS dB, c15 -> c16):

  | Passage | c15 | c16 |
  |---|---|---|
  | Intro | -26.9 | -27.0 |
  | Horn solo | -24.5 | -24.6 |
  | Theme A | -23.8 | -23.9 |
  | Reprise | -24.3 | -25.3 |
  | Bars 61-62 | -11.5 | -10.9 |
  | Bars 79-80 | -13.6 | -13.0 |
  | Coda | -27.5 | -27.3 |

**Findings**

- **C #1, loud-frame spectrum** (my method: 0.4 s frames, re 1 kHz):

  | | c15 | c16 |
  |---|---|---|
  | Centroid of the loudest 10% | 1010 Hz | 853 Hz |
  | 125 Hz | -9.6 | -5.7 |
  | 160 Hz | -11.5 | -7.3 |
  | 63 Hz | -6.9 | -5.8 |
  | 157 Hz loud minus soft | -6.9 | -3.0 |
  | 100-250 Hz share | -10.1 | -8.1 |

  The 63 Hz band rose only 1.1 dB against 4 dB at 125 Hz, so the shelf offsets the Cb role there.
- **C #2.**
  - Lead-line joins dipping 5 dB or more (wind and horn lines): 73 -> 22 (Fl1 24 -> 12, Ob1 17 -> 6, CA 12 -> 2, Hn1 12 -> 0, Cl1 6 -> 2, BCl 2 -> 0).
  - Vc 45 -> 25.
  - Overshoot: 9 of 110 filled joins now rise more than 2 dB over their body at +0.3..+0.6 s, and more than 2 dB above c15:
    - Fl1 135/194/200
    - Ob1 190
    - CA 152/163
    - Vc 71/140/263
  - Next cycle: shorten the hold or lower the dB on these.
- **A #2.** Vln II re-attack troughs of 3 dB or more (`rebow.py`): 114 and 120 are gone. 112 is still 7.0 dB at +0.16 s (c15 7.1).
- **A #4.** Bar 80, 265.1-265.8 against 264.3-264.95: Vln I -1.4 dB (was -1.7), Vln II -1.3 (was -4.2). There is no rise at 266.
- **A #5.** The Fl2 steps at 206/208/210 are -0.2/-3.3/-6.4 dB (c15 -0.4/-3.7/-6.7). The falls are the sample's, as A said. Closed.
- **A #6.** Bn1 22: 10.3 -> 3.1 dB; Bn1 32: 15.1 -> 3.1. Bn2 21 (9.7) and Bn1 21 (7.8) remain open.
- **B #1.** Bar 82, Ob1 minus (Fl1 + Vln I): +4.3 -> -3.5 dB.
- **B #2.** Ob1 143/144/145: -41.3/-49.3/-43.0 -> -43.4/-43.5/-43.0. The Vc at 144 is 2.6 dB under the oboe (was +2.7 over it).
- **B #3.** The tenor line (Hn1+Vc+Bn1) is now 2-6 dB (plain RMS) over the held Vla/Vln II (was 2-5 under). This is above B's target of about -1..+1 A-weighted.
- **B #4.** The reprise sits under the first statement: Vln I -41.9 -> -45.3, master -36.3 -> -38.2 (first statement -36.4), and the mp3 1.4 dB under theme A.
- **B #5.** Bn2 268.5-269.5: -33.2 -> -38.7, now under Fl1 (-35.3) and Ob1 (-34.8).
- **C #3.** The attack gate passed 19 of 19, with no caesura exit and +0.23 s in total.
