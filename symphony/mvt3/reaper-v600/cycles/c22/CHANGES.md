# Cycle 22 (2026-11-17): harp velocity, crescendos into 263 and the final chord, ride rows, trumpet repeats, chorale repeats, wind legato holes, balances

Critics' reports: `reports/A.md`, `B.md`, `C.md` (on the c21 render), plus the coordinator's rulings 1-8 and its later notes (Movement I c60-c61, scherzo c19-c20). Snapshot before this cycle: `before/`. Scripts: `actor_scripts/` (`data22.py --write` makes the mix.json edits; `statechk22.py` checks Opus state edits offline; `holes22.py` is critic A's legato-hole measure; `harp22.py`, `meas22.py`, `barcheck.py`, `deliv_meas.py`, `simdeliv.sh` measure; `p1.sh`, `pb.sh`, `pc.sh`, `p2.sh`, `auto1.sh`, `wait_lock.py`, `rr.py` drove the lock phase). Logs: `logs/`, `phase.log`, `pdiff.txt` (parts.json diff against `before/`).

Standing rule (Dan): the track volume envelope holds slow balance only. Every fix below is on the instrument side (CC11 / CC1, velocity, note lengths, Opus state), a printed hairpin as a dB ramp, a held phrase level, or a delivery ride. One fader row was removed (Horn 1's -3.5 dB step inside a note at 1104).

## For Dan

- **Loudness unchanged:** -14.0 LUFS, quiet passages about -22.6 LUFS. The limiter takes 6.0 dB off the final chord (c21: 5.7).
- **The harp follows its dynamics again.** In c21 the harp patch ignored how hard each string was plucked, so soft harp was 8-9 dB too loud and the harp sat over the violins' tune in bar 235. The soft harp solo (bars 123-128) is now 9.6 dB quieter, back to c20's level. In bar 235 the harp is now 8 dB under the violins. The harmonics in bars 43-47 are unchanged.
- **The crescendo into bar 263 now grows.** The brass no longer get softer inside it. On the mp3 the last four bars before 263 rise 1.5 dB (c21: they were flat). Bar 263 is still the same level.
- **The crescendo into the final chord grows more:** +4.0 dB over bars 275-277 on the mix (c21: +2.7). On the mp3 the growth is about the same as before (+2.1 dB), because the limiter takes the top off.
- **The opening ff is now louder than the crescendo of bar 10** (by 2.2 dB on the mp3; c21: 0.2). The ff bars no longer reach the fff level: every ff bar is at least 0.9 dB under bars 223 / 263 / the final chord.
- **Bar 131 is still quieter than bar 130 on the mp3** (by 1.3 dB). The mix itself rises there; the delivery's smoothing flattens it.
- **Trumpet repeated notes are clearer.** The repeated notes separate by 5-6 dB now (c21: 4 dB). The hammered half notes of bars 257-262 are still not fully separated (1.6-6.4 dB).
- **Muted trumpet and cor anglais (bars 171-183)** are now 1.5 dB apart (c21: 2.7). Both colours should be heard.
- **Violas and celli under the violins' tune (bars 73-79)** are now under the tune in every bar; before, they rose over it in bars 74 and 76.
- **Horn 1's three legato notes with a hole (bars 23, 72, 218)** now play without a hole. They are not brighter.
- **Horn 4's long soft note in bars 43-47** still wobbles, a little less (7 dB instead of 10).
- **Not fixed:**
  - the chorale's repeated brass whole notes (bars 224-234) still join with only a 1-1.5 dB dip;
  - the woodwind legato notes still have a dip just after the note change on about a third of the joins;
  - Trumpet 3's accents in bars 257-262 are only 1 dB over its plain notes;
  - the trumpets' soft off-beats in bars 159-166 overshot: they are now 9-11 dB under Horn 3 (target 3).

## Results (main render 09:51-10:01)

- **Delivered (`mvt3-mockup-c22.mp3`, re-delivered after the render with the adjusted rides, `logs/deliv_c22.log`):**
  - -14.0 LUFS, LRA 11.9 LU, true peak -1.1 dBTP, p10 short-term -22.6 LUFS.
  - Limiter: 6.0 dB on the final chord, 4.3 at 223, 4.7 at 263, 5.6 at 262.
  - Momentary max: final -7.4, bar 223 -7.7, bar 263 -7.7, loudest ff bar -8.6 (bars 1 / 5). The loudest non-climax bar over the whole movement is 222 at -8.0 (Movement I c60 check).
  - Each fff arrival rises over the bar before it on the mp3: 223 over 222 +0.3, 263 over 262 +0.5, final over 277 +0.6 dB (scherzo c19 check).
- **First delivery** (`mvt3-mockup-c22-first.mp3`, from `render_cycle.py` with the ruled rides): -14.0 LUFS, LRA 12.0, TP -1.1, p10 -22.7. Limiter 6.4 dB on the final chord, 5.7 at 262. 263 over 262 +0.4. The mp3 rose only 0.7 dB from 1032-1039 to 1040-1047.
  - Fix, simulated on the c22 master: final row -3.5 -> -4.0 dB, and a row over the crescendo's earlier bars (-1.5 dB at 1032, -1.0 at 1040, -0.5 at 1046, 0 at 1047.8). The scherzo c20 note suggested this: ride the crescendo's earlier bars, not its last.
  - Result: limiter 6.0, rise +1.5 dB, 263 over 262 +0.5. Variant A (the final row only) gave limiter 5.9 but rise +0.7.
- **Master:** -19.5 LUFS, LRA 22.5, sample peak 1.072. `render_cycle.py` now always writes `00_Master.wav` as the float stem sum (the 24-bit file peaked at 1.0).
- **Checks:**
  - Attack probe: 0 late or holes.
  - Pre-roll messages: master and the five string stems, as in c18-c21.
  - parts.json rebuilds from the config identically (checked before and after the ride edit); score_to_parts.py printed no WARNING.
  - State guard: 3 stale tracks after the final `--midi-only` build (Trombone 2, Violins I, Violoncellos: stale legato attack times, as in c21). They were rebuilt in full, then the guard read 0 stale.
- **REAPER memory:** 45 GB before the render (0 compressed), 46 GB after (4.5 compressed).
- **Lock:** taken 09:12:23 (after waiting 27 min for the scherzo), released 10:02:45: 50 minutes.
  - start and settle: 13 min;
  - build and range R1: 5 min;
  - variant build and range R2: 4 min;
  - final build, state-guard rebuild, restart and settle: 17 min;
  - render: 11 min.

| target (ruling) | c21 | c22 | goal |
|---|---|---|---|
| harp p solo 488-512 RMS (R1) / bar 235 harp minus Violins I | -42.7 / +0.5 | -52.3 / -8.4 | c20 level (-53.6..-48.4) / under the tune |
| harp harmonics 168-184 / ff 1104-1112 (R1) | -59.1 / -37.1 | -59.3 / -36.3 | unchanged / +3.5 |
| brass family RMS 1032 -> lowest in 1036-1046 (master) | -21.2 -> -23.5 | -21.2 -> -22.4 | no fall (not met) |
| mp3 mean M 1040-1047 over 1032-1039 (2) | -0.4 | +1.5 | +1.5 |
| 263 over 262 on the mp3 (2) | +1.7 (first c21 rides) | +0.5 | 0.5 or more |
| master bar 277 over 275 / 278 over 277 (2) | +2.7 / +4.6 | +4.0 / +4.1 | 4 or more / 2.5 or more |
| mp3 bar 277 over 275 (2) | +1.8 | +2.1 | 1.2 or more |
| mp3 bar 1 over bar 10 (3) | +0.2 | +2.2 | over |
| mp3 bars 130 / 131 / 132 (3) | -10.0 / -12.9 / -12.7 | -9.8 / -11.1 / -10.2 | 132 over 130 (not met) |
| ff bars 147 / 148 / 199 / 272 on the mp3 (3) | -9.0 / -8.9 / -9.1 / -8.1 | -10.1 / -10.1 / -9.7 / -11.4 | 1.5 dB under fff (met but bars 1 / 5 at 0.9) |
| trumpet repeat dips, median (under 3 dB), my measure (4) | 3.7 (5) / 4.3 (1) / 4.0 (9) | 5.3 (4) / 6.1 (0) / 5.1 (3) | 6 or more |
| Trumpet 3 half notes 1016-1048 (4) | (A: 1.3-4.8) | 1.6-6.4 | 5 or more (not met) |
| chorale repeat dips Horn 1 / Trombone 1 / Bass trombone (5) | 0.6-2.6 / 1.5 / 0.6-0.7 | 0.5-2.8 / 1.2-1.3 / 0.4-0.5 | 4 or more (not met) |
| master chorale bar-line holes 60-500 Hz (5) | 0.7-4.2 | 0.7-3.3 | not reopened |
| wind legato holes of 6 dB or more, whole piece, Fl1 / Fl2 / Ob1 / CA / Cl1 / Bn1 (6) | 4 / 9 / 6 / 6 / 6 / 7 | 5 / 9 / 6 / 6 / 6 / 6 | halved (not met) |
| Horn 1 legato holes of 6 dB or more (6) | 2 of 22 | 0 of 19 | |
| Horn 1 2-5 kHz front at 90 / 286 / 868 re previous body | -1.8 / +11.0 / -0.6 | -3.1 / +7.2 / -0.7 | not brighter |
| Trumpet 1 minus cor anglais, unison bodies (7) | -2.7 | -1.5 | within 1.5 |
| violas / celli vs Violins I+II, bars 74 / 76 (7) | +2.0 / +3.8 | -1.9 / -0.8 | under the tune |
| trumpet off-beats 636-664 note peaks re Horn 3, Trumpet 1 / 2 (7) | -2.2 / -3.3 | -8.8 / -11.2 | about -3 (overshot) |
| Horn 4 held A flat, 0.25 s level range over 0.5-5.5 s (7) | 9.8 | 7.2 | 5 |
| Trumpet 3 accented minus plain peaks 1016-1048 (8) | +0.8 | +1.1 | 2-3 (not met) |
| basses stroke p90 816-840 (8; c19 -31.7) | -34.8 | -33.9 | -33.2 or louder (not met) |

## Range passes (under the lock)

These test the floor against the attack cap in the same pass (coordinator, after Movement I c61).

- **R1** (`build/parts.json` with the wind legato velocity floor; Harp KS Master with the velocity path):
  - Harp: the p solo, bar 235, the harmonics and the final chord as in the table. Velocity now sets the level: peaks against c21 were v69 -4.3, v78 -3.6, v90 -4.0 and v116 +1.9 dB. The harmonics (v46) changed by -0.2 dB.
  - The harmonics play the Harmonics row's 1-71 velocity layer. The +8.5 dB region gain is on every region of that row, so it reaches the layer that sounds (coordinator's check).
- **R2** (variant vB: no velocity floor, plus `attack_cap_ms` 200 ms on the legato-target sustain groups "1Fls", "Fl2s", "OBs", "EHs", "Cls", "Bss").
- **Holes of 6 dB or more over qn 320-392 and 836-1016:**

  | | Flute 1 | Flute 2 | Oboe 1 | Clarinet 1 |
  |---|---|---|---|---|
  | c21 | 3 | 4 | 6 | 4 |
  | R1 (floor) | 3 | 4 | 7 | 5 |
  | R2 (cap) | 4 | 4 | 6 | 11 |

  - In R2 the cor anglais' two targets read 57 dB holes, so the cap probably silenced the start of a sustain.
  - Neither variant closed the holes, so both were dropped. The main render has no floor (`C22_WFLOOR=1` turns it on) and no cap. Movement I c61 also found the floor did nothing.
  - Caveat (scherzo c20): R1 and R2 were compared with the c21 full render, not with a control range render. The whole-piece comparison of the c22 full render (no floor) against c21 gives the same counts within one hole per track.

## Changes (files and values)

- **Ruling 1 (harp, B #1):**
  - `tools/build_reaper.py` `vel_volume()`, mix.json `"vel_volume": {"from": Harp Sus RR.oib}`. It copies the Global Group's MidiVelocity processor and its "Amount Velocity->Volume" connection (square-law table) into the Harp KS Master. Sus RR itself has both the velocity and CC11 connections on Source/volume, so two modulations into one destination are the library's own setup.
  - Harp gain_db -7.6 -> -3.6; Harmonics region gain -5 -> +8.5 dB.
- **Ruling 2 (crescendos, C #1 / #3):**
  - The 1048 caps became ramps: strings CC11 108 -> 112, woodwinds 107 -> 110, brass / clarinets CC11 102 -> 106, brass CC1 108 -> 116 over 1040-1047.9. The 888 caps are unchanged.
  - The brass hairpin gain is held at its 1032 value to 1048 (`vol_set`) on Horns 1-2, Trombones 1-2 and Trumpet 3. It equals the arrival value, so bar 263 is unchanged.
  - New generic `HP_GAIN_AT_DB` (`tools/score_to_parts.py`): the arrival gain of the hairpins starting at a given qn. The 1096 crescendo uses brass 4 dB and woodwinds 5 dB.
  - Horn 1's -3.5 dB role row at 1104-1113.5 is deleted (`build/roles.json`): it stepped inside the note at 1104. The same -3.5 dB is now in CC11 (k 40) from the rest before the final chord (1107.0-1107.4).
  - New generic `INSTR_POST["cresc_mono"]` (`tools/instr_post.py`): inside a printed crescendo, a note's resting level (lane plus note_cc, read in the note's body) does not fall under the previous note's on the same sustained row. At most 8 units; Trombone 1's crest cut at 1104-1106 is skipped.
    - PHRASE_SHAPE and the per-note contours already skip hairpins (read in the code). C's Oboe 1 fall was the "Leg" row's note_cc offset.
    - The rule acts on 1 note in the final data (Violas 720.5, +3 units).
  - Delivery rows:
    - the 1043.5 row is deleted;
    - the 1045.5 row now starts at 1047.8;
    - the final row steps at the downbeat at -4.0 dB (C ruled -3.5; adjusted after the render);
    - a new row over 1032-1047.8 (after the render).
- **Ruling 3 (ride rows):**
  - Deleted: the -1.5 dB rows on bars 1-2 and 5-6, and the 519.75-528.25 row.
  - Added: -2 dB over 31.5-48; -2.5 at 1080-1088; -1.5 at 584-596; -1.5 at 792-840.
- **Ruling 4 (trumpet repeats):** `WIND_REP_RETONGUE_BY["Trumpet"]` fall 10 -> 12 units (gap 0.1 s was already set in c03). mix.json `sus_release_cap_ms` f / ff 300 -> 240 ms on Trumpets 1-3 (Opus state: full rebuild).
- **Ruling 5 (chorale):** onset_lead `"move_fall"` (`tools/instr_post.py`): when a "set" row moves a note-on earlier, the same-pitch note's re-tongue fall moves with it, so the lane is back 0.01 qn before the moved note-on.
  - The fall is written as a 6-step staircase each way.
  - It is 18 units deep on horns, trombones, bass trombone and tuba, on the c19 chorale rows.
  - 18 moves in total.
- **Ruling 6 (legato holes):**
  - Wind velocity floor tested and dropped (above).
  - Horn 1 at 90 / 286 / 868 plays on "Sus MAX" (ART_SPANS), lead 0.06 s, no overlap (gap_set gap 0, "only_at"). The scherzo's fix, at 0.05 s, gave the same kind of result.
  - Flute 2's legato overlaps at 602 / 634 / 842 / 1074 are capped at 0.035 s (gap_set `"allow_leg"`, new key).
  - New generic mix.json `attack_cap_ms` (`tools/build_reaper.py` `cap_attack()`); not used.
- **Ruling 7 (balances):**
  - Trumpet 1 CC11 +2.5 dB (k 40) over 679.7-731.
  - Violas CC11 -3 dB (k 47) at 287.7-296.3 and 299.7-304.3; celli at 299.7-304.3 and 311.7-316.3.
  - Trumpets 1-2 off-beats velocity add +8 -> +4 at 632.9-662.5.
  - Horn 4 CC11 fill (C's points) at 171.4-182.9.
- **Ruling 8:**
  - Trumpet 3's accent rule over 1016-1048 is the trombones' (CC11 0.10 x rest, CC1 +3). Accent rules now take "from" / "to".
  - Basses' "Stac On Bow" 816-840 at 0.66 of the slot (0.33 qn).
  - `tools/render_cycle.py` always writes `00_Master.wav` as the float stem sum (`MASTER_SUM_ALWAYS=0` restores the old rule). No REAPER master fader change, so the master still equals the stem sum for `stem_fix.py`.
- **Opus state changes (full rebuilds):** Harp, Trumpets 1-3. The 11 wind tracks were built twice for R2 and back.
- `tools/score_to_parts.py` passes each hairpin's kind to instr_post (`ctx["hairpins"]`).

## Rejected or deferred

- **Wind legato velocity floor (A #3a):** no change in the holes (R1, and the whole piece). Rejected with numbers above; recorded in LEARNINGS.
- **Attack cap 200 ms on the legato-target sustain groups (A #3b):** worse (Clarinet 1 4 -> 11 holes; cor anglais silent fronts). Rejected.
- **Refitting `LEG_VEL_EXTRA_S` with pcx:** not needed without the floor.
- **Harp `soft_trim_db` p +2:** not added. The p solo is at c20's level; B's condition (more than 5 dB under the other p solos) was not measured on the same measure.
- **C's loud_eq test:** not this cycle (coordinator). Kept for c23.
- **Stem fixes:** none. The faults left are not level-only.

## Faults introduced or left

- Trumpets 1-2 off-beats at 636-664 are now 8.8 / 11.2 dB under Horn 3. Velocity +4 instead of +8 cost about 6.6 dB, far more than B's estimate of 0.5 dB per step. For c23: +7 (untested).
- The chorale's `move_fall` did not change the dips (1-1.5 dB; target 4). The fall now ends inside the old note's last 0.1 s. Opus smooths CC11 over 120 ms (MidiController fadeTime 120 in the patch), which probably absorbs it. Candidates for c23: the re-tongue rows (MANUAL-GAPS #2) or a longer gap.
- Wind legato holes unchanged (Flute 2 9 of 10 targets; the 0.035 s overlap cap did not help there).
- The crescendo into 263 still has a brass dip at 1036-1040 (-22.4 against -21.2 at 1032). The hairpin hold removed only part of it; the rest is the patches (CC flat at ff).
- On the mp3, bar 131 is 1.3 dB under bar 130.
- Trumpet 3's accents +1.1 dB (target 2-3); basses at 816-840 still 2.2 dB under c19; Horn 4's held note still ripples 7 dB.
- The limiter takes 6.0 dB on the final chord and 5.6 at bar 262.
