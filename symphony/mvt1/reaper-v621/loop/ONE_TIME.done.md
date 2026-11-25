# One-time task for the cycle 3 actor (delete this file when done)

Cycle 2 measured every volume-envelope change in the stems 0.09-0.25 s before its planned time while note onsets were on time (cycles/c02/CHANGES.md). Fills, accent swells, re-bow shapes and loop profiles all depend on this timing. Before other work, find the cause and fix it in the tools, not per note. First candidate: plugin delay compensation. Read Opus's reported latency (TrackFX_GetNamedConfigParm(tr, 0, "pdc") or the track's I_PDC-related values / the FX chunk) and compare it with the measured lead; if REAPER applies the track volume envelope without the PDC shift, either shift the envelope points in build_reaper.py vol_points by the measured latency, or move level shaping to a post-FX volume (e.g. a JS volume or ReaEQ gain automated as an FX parameter envelope, which REAPER does delay-compensate) and verify on one track in the render. Record the cause and the fix in loop/LEARNINGS.md: it also affects movement II's c17-c26 shapes and belongs in mockup-kit/LEARNINGS.md.
# One-time task for the cycle 7 actor (rename to ONE_TIME.done.md when done)

Dan's standing rule (BRIEF item 8): brass accents are weight, not bite, about 2-4 dB over the surrounding notes with no hard front edge. c06 measured the brass accents at +4.5 to +6.0 dB over the surrounding notes even after the swell was cut from 4.0 to 2.5 dB, and velocity has no effect on the KS Master sustain rows. Find what still lifts them (CC11 shape at the accent, the accent swell stacking on crescendo gain or role lifts, tenuto bumps, DETACH_ACCENTS gaps making the note before quieter, the sample's own attack) and bring every brass accent into 2-4 dB over its neighbours, with 2-5 kHz energy in the first 80 ms no more than about 3 dB over the note's body. Report the per-accent numbers before and after in CHANGES.md.

# One-time task for the cycle 14 actor (done in c14)

Memory: the c13 render ended at 45 GB with 32 GB compressed (33 instances after the new Horns a2 track), at the brief's limit; the Mac froze at about this pressure during movement II. Before adding anything, bring the settled footprint down so the render ends clearly under 45 GB. Candidates, measure each: the three percussion tracks (tam-tam, suspended cymbal, crash: a few notes each) into one Opus instance (several InstrumentZones in one Performance on separate key ranges, or one track per player reusing an instance); unload mic columns a track barely needs (Surround/Mid where loaded); unload articulation rows still loaded but used for one or two notes; the reverted c13 tests (Double basses Detache row) as part of their revert. Record REAPER memory before and after the render in CHANGES.md, and do not add a 34th instance.

Outcome (c14, cycles/c14/CHANGES.md): measured with `footprint` on settled sessions, the three single-note Leg Port MAX rows cost about 0.1 GB together (46.01 -> 46.13 GB) and one percussion instance under 0.01 GB; every track already loads only Close + Main and only the rows it plays. Nothing worth cutting was found; the Detache row was reverted. Settled 43 GiB before the render (0 compressed), 44 GiB with 11 compressed after it (c13 45 / 32).

# One-time task for the cycle 25 actor (done in c25)

1. Dan's item 7 (no audible sample-loop pulsing on held notes) has not been re-measured since the tempo and timing changes of c19-c24. On the c24 render, list every held note of 6 s or more (strings, brass, winds, timpani rolls) and report the 100-300 Hz band level and spectral centroid folded at the loop period (autocorrelation at 3.95 s for Hollywood Strings, the measured period for others), plus the master on the final chord and the Lento. Fix any note at 0.4 or above.
2. Fix the two c24 tempo side effects: Violins I/II at qn 259.5 turned into Leg Slur targets, and Clarinets 1/2 at qn 637 lost their re-tongue lead.

Outcome (c25, cycles/c25/CHANGES.md "ONE_TIME"): #1 measured with cycles/c25/actor_scripts/loopscan.py (lists in cycles/c25/loopscan_c24.txt / loopscan_c25.txt). Strings, timpani rolls and the master (final chord -0.39 / -0.08, Lento bars 5-12 -0.08 / -0.17) under 0.4. Bass clarinet 11/464, Horn 4 289 and Bassoon 2 476 (0.44-0.83) were split with BREATH_SPLIT_AT into 2.1-3.1 s pieces and now read -0.03..+0.23, with level shapes on the exposed re-entries. #2: Violins I/II 259.5 back to Sus MAX (new SHORT_SUS_AT); Clarinets 1/2 637 got their re-tongue lead back (new GATE_BPM_PRE_ARC: tempo gates read the pre-arc map, and no other note changed).

# One-time note for the cycle 30 actor (done in c30)

Cycle 30 is the last cycle: no later cycle will revert a failed test or fix a regression. Make only changes whose effect you can simulate on the c29 stems or that the c29 render already proves; run no tests, no row or patch swaps, no Opus-state rebuilds and no tempo-map changes. If anything you change measures worse on the render, put it back with a stem fix before delivering. Leave the project, build/ and parts.json in exactly the state of the delivered render. In CHANGES.md add a short "Final state" section: what is open, and the items that need a listener (the widened celli top from c29, the Clarinet 1 bars 104/106 attack cuts, the Sus Marc LITE strokes at bars 83 and 142).

Outcome (c30, cycles/c30/CHANGES.md): all 12 findings were level-only. They were simulated together on the c29 stems with stem_fix.py before REAPER was touched, written with --mix-only, and rendered once. The render matched the simulation within 0.5 dB, and nothing measured worse than c29, so no stem fix was needed. The project, build/ and parts.json are the delivered render's state. The "Final state" section lists the open items and the listener checks.

# One-time step for cycle 44 (coordinator, 2026-11-07; done in c44, see cycles/c44/CHANGES.md)

Dan heard the mockups as too wet and a bit mushy (BRIEF S4) and asked every movement to dial the reverb back. A research pass on orchestral mockup practice (YouTube scoring channels) added the hall filter, the shorter decay and the repeated-note point below. Movement I goes first on items 2 and 4 and the coordinator passes the measured values to the other three movements, so record exact state keys and values in CHANGES.md and LEARNINGS.md.

1. `build/mix.json` `reverb.fx_volume` 0.19 -> 0.095 (-6 dB on the shared hall return; Opus mixer volumes are linear amplitude). Keep every send, the IR, `wet`, true stereo.
2. Hall input low cut: add `reverb.low_cut_hz` support to `tools/build_reaper.py` exactly as in `mockup-kit/pipeline/build_reaper.py` (after the high-cut block: `filterActive` true, `lowFilterFreq` = `lowCutFreq` = the value), and set `low_cut_hz` 160 in `build/mix.json`. Keep `high_cut_hz` 5500.
3. Shorter hall: the target is a late decay of 1.5-2 s, as in real recordings (the true-stereo 3.3 s IR measured about 2.5 s). The Opus convolution reverb has an IR envelope (Opus manual p.133-134: Simple = one Decay slider that sets length and fade-out together; Full = start, end, fade-in and fade-out times and curves). Find its keys in the state (the shared insert prints `"decay": 0.0`; dump the whole ConvolutionReverb dict, nested keys included, and compare with a patch whose reverb uses an envelope if one exists). Test before the full build: one short pass-2 render of a few staccato tutti chords or a single track at two or three settings, and measure the decay (the master's drop at 0.15 / 0.3 / 0.6 / 1.0 s after a cutoff, and the late slope). Adopt the setting that gives 1.5-2 s. If no key works, say so and keep the full IR.
4. Repeated notes (Dan's S1): `score_to_parts.py` merges a same-pitch string repeat on a legato row into the note before with a CC11 notch of 6-14 CC (about 1-4 dB), so in the mix many repeats do not separate (c40: strings 2.1 dB in the master, 61% under 3 dB). Change this generically: a same-pitch repeat that is not under the same slur as the note before (and not a printed portato or tie) is a new bow stroke, re-attacked after a gap of min(0.06 s, 25% of the note) on a row with a real attack (Sus MAX, or the repetition rows in MANUAL-GAPS #2), never as a new unled Leg Slur MAX note (the c05 7-17 dB hole). Keep the merge for repeats inside one slur. Measure every changed repeat's dip in the stem and the master (target 6 dB or more in the master, as for winds and brass) and its attack timing with pcX.
5. All of 1-3 are Opus state changes: fully rebuild every track in both passes (`build_reaper.py build/parts.json jobs` with every track listed, then the same with `--pass2`), not `--midi-only`.
6. After the render, measure and record in CHANGES.md: the master's drop 0.15 / 0.3 / 0.6 s after the tutti cutoffs (bars 61-62, 122, 160, the final chord) against c43 (target at 0.3 s: 13 dB or more); the late slope; each family's early tail; the 60-250 Hz share of the tails; the repeated-note dips (S1) and the join notches against c43. Refit only the per-note fills, notches and breath gaps that the drier tail moved; fix levels by stem fix. The drier hall lowers the high-send tracks (trumpets, horns) slightly: re-check B's balance points.
7. Rename this file to ONE_TIME.done.md when done.

---
# c52 (2026-11-09): the c52 ONE_TIME.md, done

# One-time task for the c52 actor (written by the c51 actor, 2026-11-09)

The c51 render's stems carry two roles rows that REAPER does not hold yet (REAPER was released to the other threads before
they were measured): `build/roles.json` Horn 3 [163.75, 168.0, -4.0] and Cor anglais [584.0, 608.0, +1.5]
(cycles/c51/CHANGES.md, "Corrections after the render"). After locking and opening the main project, before any other
REAPER work, run

    ~/.venvs/claude-composes-reaper/bin/python tools/build_reaper.py build/parts.json cycles/c52/jobs-onetime --mix-only "Horn 3" "Cor anglais"

then save (`reaper_ctl.py save`). Everything else in build/ matches the main and pass-2 projects. Append this file to ONE_TIME.done.md and delete it when done.

# Finale techniques to adopt in c52 (added 2026-11-09 by the Movement I thread)

Dan asked that the Finale's techniques reach every movement. Source with exact settings and results:
`symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md` (code in that folder's tools/score_to_parts.py and tools/build_reaper.py).
Movement I already has items 1 (irSetup and dry hall), 12 (basses 35 Hz high-pass) and most of 11 (brass bells). Critics
should treat the rest as defaults for c52, tested against c51 and dropped only with measured evidence:
- 2 sfp / fp: FP_SPIKE_AT_MARK (spike at the moved note-on, not overwritten by a crescendo on the same onset), FP_VEL 96, per-part p roles. Judge each part's own drop.
- 3 sub. p: PHRASE_SHAPE type "drop" and HELD_DECRESC_CARRY (c51's PHRASE_SHAPE has no drop type yet).
- 4 low-end width: Finale uses a side-only 60 Hz -3 dB shelf plus a 180 Hz -5.5 dB bell; Movement I's c50 200 Hz -6 dB side shelf is already inside the references (0.563), so compare, do not swap blindly.
- 5 track_width for narrow trumpets (0.5) and trombones (0.6).
- 6 315 Hz cuts: horn family -5 dB (+1.0 make-up), violas -3 dB (+0.8). Check against Dan's "mushy" note.
- 7 FINAL_RING on the last chord.
- 8 CC16 round-robin reset before ostinato spans, then a per-span accent table (relevant to the coda bass pedal's uneven off-beats).
- 9 HARP_VEL_MAX 123 (124+ triggers the Nail Pick layer).
- 10 use the tilt jump (2-5 kHz minus 0.5-2 kHz) for brass accents, not the 2-5 kHz jump.
- 11 the rest: strings 1 kHz -2.5 dB, winds 1 kHz -1.55 dB, with make-up.

# Scherzo finding for c52 (added 2026-11-09)
After an Opus instance has played, the saved project keeps 52 legato sustain-group envelope attacks at 20 ms instead of
841-1501 ms, so any `--midi-only` build reloads that state and loud legato joins come about 85 ms early. A full track
rebuild fixes it (symphony/scherzo/reaper-v600/loop/LEARNINGS.md). Movement I's c51 was a --midi-only build for every
track except the 11 winds and the celli: check the legato joins of the other tracks on pcX against c50, and fully rebuild
any track whose joins came early.

# Finale items 13-17 (added 2026-11-09 after finale c10; same SHARED-TECHNIQUES.md)
- 13 string sf of an sfp: 0.35 qn post-fader bump (+3 dB violins and violas, +5 dB celli and basses) plus a 0.08 s lead on unled sections.
- 14 two players on one line need separate join leads (per-track SOST_JOIN_LEAD_S).
- 15 delivery ride: never end a ride trim with a step inside a printed crescendo; --fit-flat rows at +1.5 dB for soft passages after loud ones.
- 16 add the LilyPond multi-measure-text-event listener to the event dump (text on full-bar rests was missing).
- 17 confirms c51: REP_SPLIT gaps on doubled bass eighths do not deepen master repeat dips; refit metric tables after adding gaps.

## Done by the c52 actor (2026-11-09)
- The two roles rows (Horn 3 [163.75, 168, -4], Cor anglais [584, 608, +1.5]) were **not** written into REAPER and are
  removed from build/roles.json: critic A #1 showed they were fitted on the stale legato state of Horn 1 / Horn 3
  (coordinator's decision). They are re-measured on the clean c52 render (Horns a2 over the loudest other at bars 41-42,
  cor anglais minus Horn 1 at 147-152) and a row is added back only if the problem is still there (cycles/c52/CHANGES.md).
- Scherzo legato-state check: tools/state_guard.py found Horn 1, Horn 3, Trumpet 1, Trumpet 2 (main) and Bassoon 1 stac
  (pass 2) stale; build_reaper.py --midi-only now rebuilds stale tracks (STALE_GUARD) and render_cycle.py refuses a stale
  project. The c51 Horn 1 mf -3.4 and Horn 3 mp -1.7 soft trims fitted on that audio are reverted.
- Finale items 2-17: decided per item by the coordinator from critics A, B, C (cycles/c52/CHANGES.md lists each: adopted 2,
  3 (ps_drops, subito marks only), 4 (bell -4.5 dB), 5, 6 (per-track make-up), 8, 9, 13, 14, 15 (656-664 row), 16;
  not adopted 7 (FINAL_RING off: C #6), 10 (measurement note), 11 (B #6), 12 already applied; 17 is a measurement).
