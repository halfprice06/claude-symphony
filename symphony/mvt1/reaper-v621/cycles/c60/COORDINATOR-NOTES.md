# Cycle 60: coordinator notes (read before anything else)

## Dan's rules (no exceptions)
- 2026-11-11: "yeah i want to nuke all the volume adjustments per note i think they are very not helpful, there has to be other ways to fix our problem". The track volume envelope carries slow balance only (gain, roles, section dynamics, hairpin gain, divisi cuts, timpani dynamics, fades), as ramps. No per-note level or shape on it, no level rows fitted to earlier renders. Faults are fixed in the instrument (CC11/CC1 per phrase, velocity, patch or row, region volume, note lengths, gaps, overlaps, leads, keyswitch timing) or left audible and listed. Per-note bumps rebuilt as CC11 shapes inside notes are not a fix.
- 2026-11-11, on the finale: "The accents are little bit over done now". Target: isolated accents +1.5 to +2 dB, no track over +3; flat CC11 value for the note's length.
- Reference practice: mockup-kit/EW-TEMPLATE-FINDINGS.md sections 5-8 and 12.

## State after c59 (cycles/c59/CHANGES.md, envelope_table.md, faults_table.md, accent_table.md)
- Per-note envelope items 0, fitted rows 0. Points 3951. Strings 0.41-0.61 points/s, winds and brass 0.15-0.47, timpani 1.28.
- Guards: Violins I 56-90 S robust SD 9 ms, front minus tail -1.8 dB; 56-127 12 ms; 536-576 18 ms. Theme over celli lower quartile +4.3.
- Faults c58 -> c59: join holes 30 -> 25; repeats under 3 dB 49 of 260; re-bow holes 14 of 52; sags 61; pulses 13; pitches out 6.
- Isolated accents (n 151): median +1.7, quartiles +1.3 / +2.6, max +9.6; 20 under +1, 32 over +3 (single accents of +5 to +9.6 on six tracks: likely sample level by pitch); Bass trombone +3.2; under +1.5: Flute 2, Trombone 2, Trumpet 1, Horns a2.
- Cello solo 171-174: crest C5 loudest, range 8.4 dB; short notes at 689.5 and 691 4-6 dB under neighbours.
- Horn 4: layer follows CC1; F3 over G3 at p 1.7 dB; bar 111 Horn 4 still 2.2 dB over Horn 1.
- Left audible: 14 re-bow holes of 8-16 dB (Violas 36: 13.3); loop pulse on the Violins I last note (SD 3.2 dB on Sus MAX); Violas tremolo step at 168 (17.8 dB); Horn 1 498 / 587.5, Horn 3 165, Trumpet 3 456 short by 1.5-2.5 dB; Cor anglais bar 7 crest; join holes Flute 1 47, Flute 2 560, Oboe 1 168 (10.4), Bassoon 2 268 (11.5); notes after the sf at 78 3-3.5 dB under c58; Trumpet 1 fff bar 122; Clarinet 1 576-582 went -9.5 dB (5 asked); celli shorts bar 87 -2.7 (further than asked); 28 short role rows still dropped.
- Not done: alias instances for the seven printed bow changes; hairpin gains into CC11 (gains are built after the CC11 lane); Cor anglais Main-mic test; legato velocity test; Stac On Bow on the basses' eighths; brass soft entry lead.
- Not verified: basses' fp at 128; the 32 held bow changes; tone change from CC1 moving with CC11 offsets on brass and clarinets; new per-pitch gains for A-flat 4 and bass clarinet C2-D2.
- Deleted to free disk: WAV stems of cycles 29-40, 49 and 52-55. c0 and c56-c59 remain.

## What this cycle is for (critic C lens: dynamics over time)
1. Critic C: the shape of every hairpin and phrase, the loudness arc of the movement against the score (sostenuto climax with the tam-tam at bars 123-126, fff at bar 160 after the cymbal roll, recapitulation at 131, ppp coda), loudness range, swells and loop pulsing on long notes, decays. Under the rule: is each printed hairpin now carried by CC11 (the instrument) and how much is still fader gain; long notes with static CC11 (31-41 % against 0-13 % in the expert files): which exposed ones need a phrase lane. Less moment-to-moment level change than the recording (1.89 against 2.64 dB): where.
2. Critic A: the 14 re-bow holes one by one with the alias-instance option (copy on Sus MAX, changes 3 s apart, new bow led 0.15-0.2 s) and the Adagio's loop facts (sustain loop 1.93-5.90 s); the tremolo step at Violas 168; the four join holes; the single accents of +5 to +9.6 dB (row or pitch sample level?); the basses' eighths (finale: length 70 % of the slot, lead 0.075 s); sustained tutti bar-line dips (finale: old note ends 0.03-0.05 s after the new note-on on polyphonic sustain rows).
3. Critic B: the list under "Left audible" that is balance (Horn 1 / Horn 3 / Trumpet 3 short rows, Clarinet 1 576-582, celli bar 87, notes after the sf at 78, Trumpet 1 bar 122, Horn 4 bar 111), the 28 dropped short role rows (which matter), tutti entry spread per track at chords of 8+ entries (half-rise per track), and a full check of the dynamic mapping per track after c58-c59 (p / mp / mf / f steps in order on every track).

## Notes from the other movements under the same rules
## Adagio c56 render (symphony/mvt2/reaper-v600/cycles/c56/CHANGES.md)
- DIV-instance doubling with interleaved bow changes: re-bow dip medians Violins I 6.2 -> 2.3 dB, Violins II 8.1 -> 4.6, celli 5.5 -> 1.5. CC11 lift at the new bow: small help on upper strings, worse on basses.
- Opus row volume knob has no effect; use region volumes over the row (arrive within 0.3 dB).
- Per-pitch region gains made lines worse where hot notes were long notes, not pitches.
- Envelope edge slew 3 dB/s while the track sounds, printed sudden steps moved to the led note-on: moves of 1.5 dB in 0.25 s inside a note 140 -> 14.
- Velocity does nothing on oboe sustain heads. Trombone 1: CC11 barely acts near the top, CC1 carries accents.
- sf: remove CC7 half-pairs left from the old envelope; tremolo row level as region volume.
- REAPER 55 GB after 17 full rebuilds, bridge stopped answering: restart between batches.

## Adagio c57 critics (symphony/mvt2/reaper-v600/cycles/c57/reports/)
- String sustain patch loops from 1.93 to 5.90 s: a bow up to about 5.5 s cannot pulse. Split limits 5.6 / 5.0 s removed 46 of 97 bow changes.
- CC11 lift at a new bow: hold 0.30 s, return 0.55 s, no pre-fall (else the hole deepens).
- A CC shape keyed to the moved note-on is half gone at the beat when the lead is 120-300 ms: hold soft-entry shapes to score onset + 0.15 s.
- Legato velocity 84-108 fits the references but delays transitions (violins 25-45 ms, violas 13-22, celli 15-27) unless leads are corrected. Bursts do not depend on velocity.
- Short slurred notes read 2-4.6 dB low: a 6-12 dB dip for 0.25-0.4 s after each slurred note-on, independent of CC11.
- Timpani: fold the whole envelope into one CC7 lane (split between CC7 and fader caused moves inside notes).
- Fitted rows by cause: unexplained ff cells with one sign per track belong in the ff dynamic trim.
- A sustained bass pedal (A flat 1) pulses every 1.3 s inside the sample, 11-12 dB; no fix yet.
- DIV copies used for doubling are Close-only and mono: pairs 1.7-3.0 dB narrower.
- Horn 1 and 3 B flat 4 and A flat 4: L/R correlation 0.14 and 0.01.

## Finale c18 techniques (symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md items 76-80)
- Accents halved: strings +8 / +10 CC11 units at f / ff, woodwinds +7 / +10, brass 6-10 % of resting; medians +1.0 to +1.3 dB. The 11-16 % still 5 dB out are sample level by pitch.
- Fader guard at 3 dB/s: slow hairpin-gain release at the source (2.8 dB/s); a passage level whose edge falls on a held note with no rest goes into CC11. Role rows 267 -> 137.
- sfp on sustain rows: start the fall 0.22 s after the mark (0.10 s leaves no sf), CC11 +10 from 0.03 s before the note-on, hold the p with a ceiling on the dynamic lane.
- Region volumes by row group: oboe Sus MAX C5 / E5 / F5 -4 / +9 / +11 dB out -> within 2 dB.
- Negative: Sus MAX strings lose 0.7 dB per CC11 unit under 100 and are flat above 103. Chorale bar-line dips are each new whole note's slow start. Pizzicato celli: 5 dB between round-robin samples of one pitch.

## Finale c19 critics (symphony/mvt3/reaper-v600/cycles/c19/reports/)
- Bar-line dips in sustained tutti (2.3-5.3 dB): every wind and brass whole note has a 35-90 ms silence in the same window before the bar line. Plan: old note ends 0.03-0.05 s after the new note-on at pitch-changing joins on polyphonic sustain rows; 0.02-0.03 s gap staggered at same-pitch joins; leads sized to each track's rise time (oboes 0.18-0.20 s, Trombone 1 0.19, Horn 1 0.13, basses 0.18).
- Tutti entries after a rest spread over a median 148 ms because the same tracks always speak first: measure half-rise per track at chords of 8+ entries.
- Horn Main pair anti-phase on B flat 4: test Opus Channel Routing "Mono From Left" or Close 0.85 / Main 0.55.
- A switch with no effect: check the rule's tag name.
- Basses' hammered eighths sound as one late pulse per quarter: the 80 ms note is released 30 ms before the stroke's peak; test length 70 % of the slot and lead 0.075 s.

## Instructions to the critics
- SAFETY: read-only. Never run tools/build_reaper.py or tools/render_cycle.py, never exec build_reaper.py whole (cut the source before ENV_LUA if you need its functions), never touch REAPER, ~/.rpr-bridge or another movement's folder. Scratch files and scripts only under cycles/c60/critic_scripts/<SLOT>/. No subagents. No cache over 1 GB.
- Propose instrument-side fixes only. Any proposal that puts a per-note value or a fitted row on the track volume envelope will be discarded.
- Do not count a fault the reference projects also leave (legato-join sags of 2-3 dB; S shifts with identical MIDI).
- Every proposal: measured size now, expected size after, file and key to change. Size CC11 changes from the track's own curve, not a family slope.
- Hand-back at most 40 lines; full report to cycles/c60/reports/<SLOT>.md.

## Coordinator decisions on the c60 critic reports (actor: this is the work order; tables and values in reports/A.md, B.md, C.md)

Priority order. Range-test what a critic marks as inferred. Drop from the bottom if time runs short and list what was dropped. Do not touch: the 0 per-note envelope state, the theme leads on Violins I, the fff trims and bars 160-161, the delivery chain, the Cello solo lane apart from C's two points, the tam-tam level, pp/ppp levels of bars 175-182, celli change at 295.0, Violins II's one bow in the last chord, accent CC11 values, harp and pizzicato settings, TIMP_DELAY_S.

1. Rule breaches still on the envelope (B 2, B 5, C 4):
   - Delete the two fitted LEVEL_SHAPES rows on the celli (score_config.py lines 1498 and 3277, qn 343.5-347.7). Fugato subject bars 85-87: flat CC11 (remove the unprinted 72 -> 62 fall), stroke velocities per B (345, 346: 62; 347: 52; 338.5, 339: 60) or C (56 / 56 / 50): range render 336-349, take the one with the smaller range and bar 87 not under bar 86 by more than 3 dB.
   - Step-shaped phrase rows Violas 244.1-248.7 (-8.7 dB) and Bass clarinet 424.4-432.1 (+4.5 dB): move to CC11 on the track's own curve, or delete and list.
   - TIMP_LOUD_ATTACK_DB (+6 dB on each f/ff stroke, removed over 0.75 qn) is a shape inside each note: remove it; stroke weight by velocity (B's table). Report the timpani's points per second after.
   - Search LEVEL_SHAPES and the rule dump once more for any fitted or one-figure row; the hand-back states the count found and removed.
2. Climax order (C 1, B 1). The printed order must hold: bar 160 (fff) and bar 122 (fff) over bars 170 and 26 (ff).
   - mix.json dyn_trim_db ff -2.5 on the five string tracks, -1.5 on winds and brass (a per-dynamic track trim is slow balance); fff unchanged. Horns 1 / 2: B's values stand in place of the -1.5 (Horn 1 ff 1.5 -> -0.5 and f -0.8 -> 0.7; Horn 2 ff 0.4 -> -1.6).
   - Bar 122: roles.json Trumpet 1 [484, 492.5, +3], Trumpets 2 / 3 [484, 492.5, +2] as slow rows with edges in rests (their CC11 is at 124, an offset cannot play); _all [484, 504] -1.6 -> -0.6; Violins I 484-492 at CC11 112 in place of the 125 -> 99 conversion; timpani roll 632-636 CC7 end 76 -> 84.
   - Check by level-only stem sum before the render: momentary order 160, 122, 170, 26. Report the four bar levels.
3. Dynamic trim across printed hairpins (A 3): the trim ramps over the hairpin instead of stepping at its end (build_reaper.py vol_points); remove the c59 CC11 floor on Violas 160-168; Violas 164-168 and 500 must not step up more than 3 dB at the arrival. CC11_FLOOR rows at the arrival value for the 26 diminuendo ends that undershoot (basses 32, Bassoon 2 268, Contrabassoon 168, Bassoon 1 500, Oboe 1 168 first).
4. Second theme bars 47-54 and 147-154 (C 2): celli region_gain_db Leg BC MAX -4; CC11 lanes for celli and Horn 1 over 184-216 and 584-616 from C's report. Range render one of the two spans. The theme-over-celli guard in bars 15-22 must still hold after the row gain (re-measure; adjust the celli role there if it moves).
5. Other hairpins (C 3) and balance items (B list): basses 356-360 and 28-32, Horn 1 bars 103-104 and crescendo 444: 64 / 448: 70, Flute 2 160-164; Clarinet 1 576-582 CC11 12 -> 17; Horn 3 165 84 -> 78; Clarinet 2 bar 145 21 -> 16; lanes for Violas 368, celli 295 and 539, Clarinet 2 576; Cello solo 685 hole (C's two points).
6. Dynamic mapping (B 3): Horn 4 soft_trim p 5 -> 7.5, mp 5 -> 6, mf 4 -> 5.5, F3 soft-layer gain -6 -> -8.5; Oboe 1 per-layer region gains (E-flat 5 +7, F5 +2, no E5 cut on soft layers); Violas soft_trim p 5 -> 3; Oboe 2 dyn_trim f 3.5 -> 6.0.
7. Sustained tutti chord changes (A 2): long-note form of WIND_DETACH (both notes 0.8 s or more, no accent): old note ends 0.03-0.04 s after the new note-on at a pitch change if the row is polyphonic (check: a legato row must not get an overlap that triggers a transition it did not have), 0.025 s gap at same pitch. Range render bars 122-124 and 167-169; adopt if the wind-and-brass sum dip falls under 2 dB with no doubled attacks.
8. Re-bows (A 1): re-list REBOW_AT so pieces run up to 5.3 s (43 -> 29 changes; celli bars 7-14 none); remove REBOW_NONE basses (722.7, 729); REP_MIN_GAP held_lead_s 0.20 s under CC11 60, 0.12 s above, for the 23 printed same-pitch changes. Final chord 711.8-728 ("change bow at will"): alias Sus MAX copies of Violins I, Violas, celli, basses in pass 2 with interleaved changes, each instance -3 dB, only if lock time allows; else list.
9. Timing: RETONGUE_LEAD_S basses 0.06 -> 0.12; ENTRY_LEAD_S Oboe 2 mid 0.14 -> 0.05 with entry_leads.json totals capped at 0.06 s; Trumpet 2 0.06 -> 0.08; per-onset extras at 484 and 620 (B 4); Flute 1 47: 0.03 s gap, 0.07 s lead; tam-tam delay so the fff starts on the beat (range test).
10. Small CC11 items from B for Bass clarinet 704, Clarinet 1 706, Violas 320.5, Trumpet 3 456, Horn 1 587.5.

Report in the hand-back: per-note envelope items per track (0), fitted rows found and removed, points per second (timpani too), guards, the four climax bar levels and their order, faults table c59 -> c60, isolated-accent table, master bars more than 1.5 dB off c59 with cause, faults left audible, what was dropped, what is not verified. A/B clips c59 then c60 in cycles/c60/ab/: bars 15-23, bars 85-87, bars 121-124, master and lead stem.

## Actor constraints
- Shared REAPER lock: wait_lock.py with a running waiter; never take or break the lock by hand; tie rule: the folder path that sorts first goes first.
- Disk: 54 GB free at the start. Keep a 10 GB floor after the render; delete WAVs only inside cycles/c58 and cycles/c59 rangetest / variants folders and your own c60 scratch.
- First range render after a rebuild is unusable: render each variant twice, keep the second. State guard at the start, after range renders and before the full render; rebuild stale tracks in full. Wait 45 s after each range pass. Restart REAPER between batches of rebuilds.
- Keep scripts under cycles/c60/actor_scripts/. Write cycles/c60/rendered_build/parts.json as rendered.
- No score change. No commit. Nothing published. No REAPER preference changed. Nothing in ~/.rpr-bridge modified. No subagents.
- Update HISTORY.md, LEARNINGS.md, cycles/c60/CHANGES.md. Hand-back at most 40 lines.
