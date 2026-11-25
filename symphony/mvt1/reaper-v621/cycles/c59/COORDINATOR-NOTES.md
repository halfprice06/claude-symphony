# Cycle 59: coordinator notes (read before anything else)

## Dan's rules (no exceptions)
- 2026-11-11: "yeah i want to nuke all the volume adjustments per note i think they are very not helpful, there has to be other ways to fix our problem". The track volume envelope carries slow balance only (gain, roles, section dynamics, hairpin gain, divisi cuts, timpani dynamics, fades), as ramps. No per-note level or shape on it, no level rows fitted to earlier renders. Faults are fixed in the instrument (CC11/CC1 per phrase, velocity, patch or row, region or row volume, note lengths, gaps, overlaps, leads, keyswitch timing) or left audible and listed. Per-note bumps rebuilt as CC11 shapes inside notes are not a fix.
- 2026-11-11, on the finale: "The accents are little bit over done now" (they were +2.1 to +4.1 dB). Target here: isolated accents +1.5 to +2 dB over unaccented notes, no track over +3. An accent is a flat CC11 value for the note's length.
- Reference practice: mockup-kit/EW-TEMPLATE-FINDINGS.md sections 5-8 and 12.

## State after c58 (cycles/c58/CHANGES.md, envelope_table.md, faults_table.md, faults_c58.txt)
- Per-note envelope items 0, fitted level rows 0. Points 4515. Strings 0.49-0.73 points/s (aim 0.4), winds and brass 0.18-0.55, timpani 1.34.
- Guards: Violins I 56-90 S robust SD 9 ms, front minus tail -2.1 dB. 56-127: 13 ms, 7 over 40. 536-576: 17 ms, 7 over 40. Theme over celli bars 15-22 median +9.3, lower quartile +5.9 (target 3.9: now perhaps too far; check the celli are not lost).
- Faults c57 -> c58: join holes 25 -> 30; re-bow holes 16 -> 17 (of 62 re-bows); sags 62 -> 62; pulses 17 -> 13; pitches 4 dB out 23 -> 7. The repeat count skips led repeats and is not comparable.
- Master bars against c57: 23 more than 1.5 dB over (172 +4.7, 74 +4.4, 179 +4.2), 17 under (7 -7.8, 47 -4.0, 21 -3.2).
- Accents f / ff: strings +2.6 / +1.7, winds +1.2 / +0.9, brass +0.9 / +0.5. Violins I +3.3 (over), celli -0.8, most winds and brass +0.5 to +0.8 (under). sf / sfp do not take the rule. Measured as a mixed median, not isolated accents.
- Failed in c58: re-bow overlap on MIDI channel 2 (silent in Opus); CC16 reset per beat on the basses' eighths (no change); Horn 4 soft-layer gain (F3 still 12 dB over G3 at p, bars 19-22).
- Left audible: 17 re-bow holes of 7-13 dB; Cor anglais bar 7 -8.4 dB against c57; Horn 1 bar 111 -9.4; basses' pedal bars 125-129 +5.3; Violins I recap theme bars 136-139 +3.7; string shorts 4-5 dB over c56; bars 171-174 and 179-180 +3 to +4.7 (Cello solo lost its shapes, no CC11 phrase shape written); capped bassoon swells 2-3 dB short.
- Not done: alias-instance re-bows, Marc rows for string accents, legato velocity test (124 -> 96), Stac On Bow on the basses, brass soft entry lead, keyswitch lead 0.15 s, per-track accent refit.
- Deviation: Violins II theme doubling stays on Sus Marc LITE with a -4 dB row gain.
- Not verified: pulsing on notes no longer split; levels of the CC11 offsets that replaced roles and shapes; brass entry timing after onset keying.
- theme_S.py now imports onsets from cycles/c55/actor_scripts/S; run from ROOT: `~/.venvs/claude-composes-reaper/bin/python cycles/c54/coordinator_scripts/theme_S.py c58 "Violins I" 56 90`. It reads cycles/cNN/rendered_build/parts.json.

## What this cycle is for (critic C lens: holistic)
1. The passages that lost a shape and got nothing in its place: write the phrase in CC11 as the references do (one lane per phrase, flat across joins): Cor anglais bar 7, Horn 1 bar 111 and bars 44/48/103, Cello solo 171-180, bassoon swells, basses' pedal 125-129, recap theme 136-139. Critic B: list every passage where a solo or melody now sits wrong against its accompaniment, with the CC11 phrase values that fix it.
2. Accents per track, measured on isolated accents (critic A): sizes per track from the CC11-to-dB table so every track lands at +1.5 to +2; Violins I down; celli up; sf / sfp included; scale 0.75 / 0.6 for 9+ / 16+ accented staves.
3. Re-bows (critic A): 17 holes. The second-channel route failed. Left: a separate alias track / instance on Sus MAX with interleaved bow changes spaced 3 s apart (scherzo: 12.4-13.5 -> 4.1-6.5 dB); no re-bow on exposed notes; raising REBOW_MAX_S further where pulse measurements allow.
4. String shorts 4-5 dB over c56 (velocity-mapped levels after SHORT_CC11_PARK = None).
5. Envelope points on strings: hairpin gain is the next source. Which hairpin gains can move into CC11 (critic B)?
6. Critic C, holistic: compare c58 with c53 and c0 and with real recordings; the weakest passages now; what still sounds like a machine; three to six changes across any area. Include the checks other movements found useful: per-note L/R correlation on exposed held horn notes; tutti note ends falling together 20-50 ms before bar lines; upper-woodwind stems with no stage sound after note ends.

## Notes from the other movements under the same rules
## Finale c17 (symphony/mvt3/reaper-v600/cycles/c17/CHANGES.md), instrument-side only
- Accents by lower resting CC11 plus CC bump: +2.1 to +4.1 dB over neighbours on 19 of 28 tracks (not oboes, Horn 3, Trumpet 2, basses).
- Tongued wind/brass joins separate by 3.8-6.4 dB (was 0.5-2.9), except Horn 3, Bassoon 1, fast eighths.
- Bass pitch spread 12.2 -> 8.8 dB by Opus region volumes.
- Timpani strokes +4 dB. Fader steps of 2 dB in 60 ms inside notes 75 -> 0.
- Still audible: bar-line dips 2.6-5.5 dB in the chorale, uneven cello/bass pizzicato.
- Finale items 70-75 (symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md, tools/instr_post.py): accent bump to 124 from 0.02 s before note-on, held 0.15 s, back by 0.45 s; envelope guard post-pass (fader moves of 2 dB in 60 ms inside a note moved to 0.03 s before the moved note-on); timpani envelope folded into CC7, right-hand keys 4 dB louder; gap floors 0.09 trumpets/tuba, 0.12 horns/trombones, 0.068 woodwinds, 0.085 oboes; Stac On Bow RRx9 no velocity response, use CC11 offset; no-gap bow change with CC11 swell does not close re-bow holes; move keyswitch and CC16 reset with the note-on.

## Finale c18 critics (symphony/mvt3/reaper-v600/cycles/c18/reports/)
- Dan: finale c17 accents "a little bit over done". Target +1.5 to +2 dB median, no track over +3; scale 0.75 / 0.6 for 9+ / 16+ accented staves. Medians hide a quarter of accents at +5 to +8 dB: report the upper quartile and maximum. A held-then-released CC bump puts the level 60-450 ms after the onset (bulge).
- Lower resting CC11 did not flatten ff against f.
- Guard by slope, not "2 dB in 60 ms": 3 dB/s and 1.5 dB or more inside a sounding note (hairpin-gain releases, stretched role steps, old stem-fix rows).
- sf / sfp needs the accent rule.
- Bar-line dips in tutti come from about 15 tracks ending together 20-50 ms before the bar line: stagger note ends and breaths; offset bow changes between celli and basses.
- Pizzicato velocity crosses a sample layer near 47 (8-13 dB step): keep under the edge, level pitches by region gains.
- Basses Stac On Bow: half amplitude at 95 ms, peak at 140 ms; round-robin positions differ 33-113 ms; onset detectors on running eighths give noise.
- Timpani right-hand keys 4-5 dB louder than left.

## Scherzo c16 (symphony/scherzo/reaper-v600/cycles/c16/CHANGES.md)
- Same-track overlap of old and new bow is impossible. DIV doubling with interleaved bow changes and CC11 lifts: dips 12.4-13.5 -> 4.1-6.5 dB.
- note_move_guard post-pass in build_reaper.py: no unprinted envelope move over 1.9 dB inside a sounding note; 55 one-note role rows removed. Cost: held crescendo arrivals raise basses, violas, bassoons 1.1-2.2 dB.
- Accents with ff at CC11 104: median +0.7 to +1.4 dB but uneven per track (Flute 1 +3.6, Clarinet 1 +5.0, strings at ff +0.8). Size per track.
- Region gains: match row names without case ("Sus Max" on cor anglais); per dynamic layer works.
- Brass gap floor 0.09 s: trumpets' repeated chords separate 6.4-9.3 dB (was 1.5-2.0).
- Keyswitch 0.15 s ahead plus row-change leads: late joins fewer, but celli joins outside 25 ms got worse after one refit pass (28 -> 43): refit twice.
- Timpani velocity +8 capped at 104, CC1 118: roll holds -30 to -34 dB.

## Scherzo c17 critics (symphony/scherzo/reaper-v600/cycles/c17/reports/)
- Horn 1 G#4 in anti-phase between L and R in the 1FH Main pair (correlation -0.72 to -0.86; mono loses 8-11 dB). Check exposed held horn notes with per-note L/R correlation.
- Guard side effects: hairpin gains and crescendo holds that can no longer release stay on held notes (up to +7.4 dB); a role rising inside a solo's first note now ramps over the entry (7-8 dB low). Carry hairpin gain in CC11; start solo roles in the rest before.
- Accent statistics: measure isolated accents separately from runs of accents (runs read +0.3 by construction). Their isolated median +3.1 against a mixed +1.4. Most excess is row and pitch sample level. A bump gives a louder whole note, not a weighted start.
- Lead caps: cap a legato lead against the previous note's moved note-on, not its score slot (eight joins 128-151 ms late).
- Second instance for interleaved re-bows: copy on Sus MAX, not Leg Slur MAX (7 dB weaker fundamental, 4 dB brighter). Bow changes need 1.0-2.2 s to recover: space 3 s apart.
- Old per-note level lines survive a "slow" filter if they hold one level for 3 qn.
- Upper-woodwind stems fall 28-41 dB within 0.2 s of a note end against 15-22 dB for strings and brass: test raising Main mics on one woodwind.
- Two hall scripts read the late slope differently (1.36 s against 1.54 s).

## Instructions to the critics
- SAFETY: read-only. Never run tools/build_reaper.py or tools/render_cycle.py, never exec build_reaper.py whole (cut the source before ENV_LUA if you need its functions), never touch REAPER, ~/.rpr-bridge or another movement's folder. Scratch files only under cycles/c59/critic_scripts/<SLOT>/, and keep scripts there, not in the temp folder. No subagents. Disk is short (27 GB free): no caches over 1 GB.
- Propose instrument-side fixes only. Any proposal that puts a per-note value or a fitted row on the track volume envelope will be discarded.
- Do not count a fault the reference projects also leave (legato-join sags of 2-3 dB; S shifts with identical MIDI).
- Every proposal: measured size now, expected size after, file and key to change.
- Hand-back at most 40 lines; full report to cycles/c59/reports/<SLOT>.md.

## Coordinator decisions on the c59 critic reports (actor: this is the work order; tables and values in reports/A.md, B.md, C.md)

Priority order. Range-test what a critic marks as inferred. Drop from the bottom if time runs short and list what was dropped. Do not touch (C, A): the c58 envelope state, the theme leads on Violins I, the Marc spans 88-100 and 536-548, EQs, returns, sends, the delivery chain, REBOW_MAX_S 5.2, SHORT_CC11_PARK = None, the brass accent ceiling 118.

1. Cello solo bars 171-174 (B, C agree): mix.json region_gain_db Cello solo: Leg Port MAX all -8; C5 +5, B4 +3, E-flat 4 legato -4; one CC11 lane for the phrase (B: 62 / 78 / 76 / 82 / 88 at the crest / 64 / 50; C: 56 -> 70 -> 76 -> 96 at 692 -> 58: range render 679-696 and take the one whose crest is the loudest note with the least range elsewhere). Fallback: all notes on Leg Slur MAX.
2. Horn 4 soft layer (B): CC11_REMAP["Horn 4"] p 46 -> 56 (pp 50, mp 62), soft trims p 14.4 -> 5.0, pp 8.0, mp 5.0, F3 Sus MAX -2; remove the pp region entry that did nothing. Range render bars 19-22 and 104-111 first; target F3 within 3 dB of G3 and Horn 4 not over Horn 1 in bar 111. Horn 1 soft A-flat 4 +5, G4 +4 (C). Bassoon 1 A-flat 3 gains halved (C).
3. Solo and melody shapes in CC11 (B finding 4 table, C item 4): Horn 1 412-416 +8 units and B-flat 4 Sus MAX +3, crescendo at bar 111 from 52; Clarinet 1 bars 45-46, 105, 127 and 504.4-508 +8; Bass clarinet bars 77-78, 109 and its A-flat 2 gain limited to Sus Non Vib / Leg Slur rows, C2-E-flat 2 region gains; Horn 1 at 171, 498, 587.5; Cor anglais hairpin start CC11 66 -> 74 (no role); Flute 1 A-flat 5 +5 only on Sus MAX, +2 on Leg Slur MAX; low-brass under the melody bars 124-126 as CC11 values. LEVEL_TO_CC min_s 0.5 for rows starting after a rest, with per-track slopes from B's cccurve.json, not the family values.
4. Oboe 1 dynamic mapping (B): soft_trim_db mf 3.1 -> 7.0, p 5 -> 9.5, mp 8.5. Check bars 79 and 145.
5. Theme (C 3, B): celli role [56, 88] -3.5 -> -2.0; CC11 floor on the Violins I theme row so the diminuendo at 82-89 ends at 84, not 73. Guards as before (Violins I 56-90 S robust SD at or under 12 ms, front minus tail within 3 dB; theme over celli lower quartile 3.9 or more).
6. Accents (A 1): per-track CC11 targets from A's table (f from 88 / ff from the resting value), ceilings 120 strings, 122 winds, 118 brass; tutti_scale off; the 78 accents of 0.3 s or more with no rise get one; sf tops strings 96, winds 110, brass 102 with no ACCENT_FLAT on an sf note; FP_SPIKE ("f", 0.5, 0.9). Report isolated accents per track: median, quartiles, maximum. Target median +1.5 to +2, no track over +3.
7. Re-bows (A 2), config only: REBOW_NONE Violas (28, 42); REBOW_AT["Violoncellos"] = [295.0]; REBOW_NONE basses (722.7, 729); REBOW_NONE Violins I (707.5, 715.5) with the piece at 711.86 on Leg Slur MAX (B) unless the single bow pulses; SUS_ENTRY_AT["Violins I"] = [720.0] for the last note. Alias track on Sus MAX for the seven printed bow changes only if the rest is done and the lock time allows; else list.
8. String shorts (A 3): region_gain_db Violins I Staccatissimo RRx9 all -3.5; Violas Stac RRx9 all -2.5; celli bars 85-87 velocity 77 -> 68.
9. Held same-pitch repeats on strings (C 5): a held-note class in REP_MIN_GAP at 0.03 s (32 joins, dips 9.5 dB median).
10. Join holes (A 4): WIND_DETACH soft gap 0.015 s under CC11 60; Flute 1 634.0 target velocity 100; end the Violins II Marc doubling at 572; CC11 floor 45 on the Violas tremolo diminuendo into 168.0.
11. Basses' pedal 500.5-516: role -3 as one phrase span with slow ramps (B asked -5, C warns it is still 10 dB under the rest).
12. Envelope points: ENV_THIN tol_db 0.5 -> 0.75; the 57 + 38 movable hairpin gains into CC11 only if cheap. Report points per second.
13. Range test only, adopt if clearly better: Cor anglais Main mic -11.6 -> -4 dB (woodwind tails).

Report in the hand-back: per-note envelope items per track (0), fitted rows (0), points per second, guards, faults table c58 -> c59, isolated-accent table, master bars more than 1.5 dB off c58 with cause, faults left audible, what was dropped, what is not verified. A/B clips c58 then c59 in cycles/c59/ab/: bars 15-23 and bars 171-174, master and lead stem.

## Actor constraints
- Shared REAPER lock: wait_lock.py with a running waiter; never take or break the lock by hand; tie rule: the folder path that sorts first goes first.
- Disk: 27 GB free. Before the render delete WAVs only inside cycles/c58/rangetest, cycles/c58/variants, cycles/c57/render_pass2, cycles/c57/rangetest and your own c59 scratch if needed; keep c0 and the main render folders of c52-c58. Keep a 10 GB floor after the render.
- First range render after a rebuild is unusable: render each variant twice, keep the second. State guard at the start, after range renders and before the full render; rebuild stale tracks in full. Wait 45 s after each range pass.
- Keep scripts under cycles/c59/actor_scripts/, not in the temp folder. Write cycles/c59/rendered_build/parts.json as rendered.
- No score change. No commit. Nothing published. No REAPER preference changed. Nothing in ~/.rpr-bridge modified. No subagents.
- Update HISTORY.md, LEARNINGS.md, cycles/c59/CHANGES.md. Hand-back at most 40 lines.
