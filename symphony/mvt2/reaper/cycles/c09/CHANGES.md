# Cycle 9 changes (actor)

Snapshot of tools and build data before the cycle: `before/`. The Opus states changed on every track (pre-fader sends, reverb high cut, widths), so I rebuilt all 27 tracks, then saved, quit and reopened REAPER before rendering. The first render (`pass1_metrics/`, `pass1_mvt2-mockup-c09.mp3`) had regressions that I caused: three new 8-10 dB join holes, a Tbn1 accent 8 dB too strong, Cb hot in bars 83-84, and harmonics too loud. I fixed them as data only (`--midi-only`), restarted REAPER (48 GB compressed) and rendered a second time (`pass2_metrics/`). In pass 2, my `fresh` cut had shortened the Vln I qn 65 tutti note itself to 0.02 qn, because I compared rounded onsets without a tolerance. I fixed that (only Vln I changed), restarted and rendered a third time. The first try at pass 3 stalled with REAPER idle and the bridge unresponsive. Inferred cause: an overwrite prompt, because the render folder still held the pass 2 stems. I stopped it, quit REAPER (SIGTERM; the project had been saved before), emptied `render/`, reopened and rendered. Pass 3 (`metrics/`, `render/`, `mvt2-mockup-c09.mp3`) is the delivered render. All renders passed the attack gate (0 late entries or holes); pass 3 ran at 0 GB compressed. Unless marked otherwise, the numbers below are from pass 2, which differs from pass 3 only in the Vln I track.

Not mine: someone changed `tools/render_cycle.py` at 12:18, after my snapshot. The mp3 is now mastered by a new `tools/deliver_master.py` instead of the ffmpeg chain. I did not touch either file.

## Accepted and implemented

Critic A (articulation):
- A #1 `build/early_fills.json`: Ob1 55.5 / 57 / 271 (7/6/7), CA 99 / 129.5 / 133.5 (6/5/4), Fl1 190 / 252 (5/6), Fl1 256 3 -> 5.
- A #2 `tools/score_to_parts.py`:
  - Role spans: spans that meet (`ROLE_CHAIN` 0.5 qn) crossfade over [B.a - 0.1, B.a + 0.15]. A span that starts on a legato target ramps in over [a, a + 0.25]. Spans with end_ramp are unchanged.
  - Note and pitch trims now end over [next moved onset - 0.05, + 0.03] (`trim_shape`). A pitch trim on a joined note starts at the note's moved onset and ramps in over 0.25 qn.
  - Note trims keep their 0.6 s ramp in from the score onset. In the first render they started at full depth at the moved onset, and that gave the regressions at Ob1 190, CA 152 and Fl1 254.
  - `bcsoft` is skipped where a crescendo starts within 0.25 qn.
- A #3: no Leg BC join across more than 12 semitones, or where the target has a "solo"/"tutti" text.
  - A wide unslurred step plays Sus MAX through the c06 entry path (Vc qn 274; also Vla qn 262, A flat 3 -> B flat 4 at the ff).
  - A "tutti" entry is marked `fresh`: it gets the family entry lead plus `entry_leads.json` Vln I 65 = 0.10 s, and the solo's last note is cut 0.03 qn before it.
- A #4 Horns 3-4 con sord.: `mix.json` `mute_eq` adds a second ReaEQ (low shelf 300 Hz -6, bell 1.8 kHz +3 bw 1, high shelf 4.5 kHz -8). Its Wet parameter (index 17) is automated 0 -> 1 at qn 278. Supported in `build_reaper.py` (`set_mute_eq`, also in `--midi-only` and `--mix-only`). I did not add the extra -2 role, because the EQ already lowers the level.
- A #5: loud accents (f-4 or louder, winds/brass/strings) get +`ACCENT_DB` in the volume envelope (30 ms rise, held to 0.25 s, gone by 0.5 s). I used 2 dB, not 3: at 3 dB, Tbn1 213 was 5.6 dB over its neighbours. `VEL_SET` Tbn1 218 is 110, not 118: at 118 it peaked 8 dB over its neighbours.
- A #6: `HARP_PITCH_VEL` {58: +12, 57: +7, 60: +5, 63: +5, 65: -8, 66: -4} on non-top harp notes.

Critic B (balance):
- B #1: `HP_CHAIN` 6 qn. Consecutive crescendos to f+ chain their hpgain when no softer mark and no decrescendo comes between them: the first holds without a release, and the second starts from it. It applied at qn 200 on 13 tracks.
- B #2: removed the c08 pitch-trim cut at onset + 3 qn. Added roles.json Cb [274, 286, 2]. I used 2, not 4, because the new Cb EQ made 4 measure +1 to +2 dB over Vc in bars 83-84.
- B #3: an untargeted hairpin of the opposite direction within 0.3 qn of the previous untargeted one returns to that hairpin's starting level (messa di voce).
  - The c06 next-mark limit is skipped in this case. Without that, Vln I bar 73 stayed at CC 58 because of the mp in bar 75.
  - Printed marks reset the rule.
- B #4: roles Vln I [204, 208, -1.5] (the critic's alternative, which keeps Vln I at least 3 dB over Vc) and Vln II [204, 212, 2].
- B #5: Harp harmonics gain_db -2 -> +3. +6 measured -40 to -42 at the attacks.
- B #6: note_trims Bn2 259 -5.

Critic C (blend):
- C #1:
  - Vc bell 170 Hz +3 bw 1.5. I used +3, not +4, to protect the Vc countermelody balance.
  - Cb low shelf -7 -> -5, bell 150 +3 -> 160 Hz +6 bw 1.4.
  - Vln I high shelf 5 kHz -4. This needed a new `highshelf` band type (ReaEQ band 3) in `build_reaper.py`.
  - `measure.py` now prints band shares against the Dvorak and both Brahms references.
- C #2: `reverb.send_pre_fader`: each mic channel's Reverb Send is pre-fader (`post: false`), level = send x channel volume.
- C #3: width 0.3 for harp (seat -0.6 -> -0.65), horns, BCl, CA, Tbn1-2, BTbn and Tuba; Vc and Cb 0.35.
- C #4: `reverb.high_cut_hz` 5500: the hall's `filterActive` true, with `highFilterFreq` and `highCutFreq` both 5500 (the state has both keys).
- C #5: the final fade holds -10 dB from qn 304 (it no longer goes to -20 by 304.5). A timpani roll that ends the piece keeps its settle through the tail.
- C #6: high-pass Harp 30, Tuba 25, BTbn 30 -> 40, Timp 45 Hz.

## Measured (c08 -> c09 final render; scripts are the critics', copied to `/private/tmp/claude-501/mockup-loop/c09-actor/v{A,B,C}`)

- Master (pass 3): -23.9 -> -23.7 LUFS, LRA 23.6 -> 23.8 LU, true peak -4.0 -> -3.9 dBFS. Delivered mp3: -19.5 LUFS, LRA 16.0 LU, -1.6 dBTP.
- A #1 join dips (post envelope):
  - Ob1 55.5: 10.1 -> 4.4. Ob1 57: 12.1 -> 6.4 (2.7 in pass 1, where the +4 note trim came in fast). Ob1 271: 10.6 -> 5.2.
  - CA 99: 9.4 -> 4.2. Fl1 252: 9.3 -> 3.7. Fl1 255: 7.3 -> 2.2.
  - Not met: CA 129.5 8.8 -> 7.6, CA 133.5 7.7 -> 7.3, Fl1 190 7.2 -> 6.9, Fl1 256 8.7 -> 6.4, Fl1 270.5 10.7 -> 8.8.
  - Ob1 190 / CA 152 / Fl1 254 are back to c08 or better: 3.3 / 3.9 / 2.1.
- A #2:
  - vol_db at the shared role boundaries now lies between the two role values: Vla 298 +9.0 -> +3.2, Vln II 216 -18.5 -> -11.3, Vc 262 -12.0 -> -2.2, Harp 124 -11 -> -5.2.
  - Vla at qn 146 still falls about 9 dB in the 0.15 s after the bow change (c08 about 12). Not met (target 3).
- A #3:
  - Vc qn 274 is now at -55 dB by +0.2 s; c08 sat at -76 for 0.8 s.
  - Vln I 65 (pass 3, with the 0.10 s extra lead): -49 to -50 at +0.06 to +0.12 s, -45 by +0.14 s, about -42 at +0.5 s (c08: -56 to -52 for 0.25 s). Better, but the critic's 4 dB check is not met.
- A #4: Horn 3 muted A flat 3, 2-8 kHz minus f0..4f0: -17.7 -> -25.8 dB. The open Horn 4 at qn 9 measures -17.7.
- A #5: Tbn1 213 is +3.8 dB over the eighths around it and 218 is +2.2; peak minus body at 218 is 4.9.
- A #6 (my own measure, attack energy over the ring): harp p10-p90 spread 8.1 -> 5.7 dB (bars 53-54) and 9.2 -> 5.1 dB (55-58).
- B #1:
  - Wind section at qn 199: -30.8 -> -27.8 (196: -24.3). Mix 196 -> 199 fall: 4.6 -> 2.1 dB.
  - Fl1/Ob1 at 199-201: -33.9 / -34.5. Partly met: the critic's target was -33 or louder.
- B #2: Cb minus Vc, bars 83-86: 0.0 / -1.0 / -1.6 / -2.2; bars 89-92: +0.1 / +0.3 / -0.9 / -2.5. c08 had +4.7 / +3.5 in bars 90-91.
- B #3: Vln I 244-249 is -36.5 (c08 -32.8 to -35.8). That is 3 dB over qn 238-239; the target was 1.5. Bar 75 (mp) is 3.7 dB over bar 74.
- B #4: Vln I share of bar 61 is 37% -> 26%. Vln I is 3.2 dB over Vln II and 4.3 dB over Vc. Bar 61 is 4.5 dB over bar 79 (c08 4.9).
- B #5: harmonics at -43.6 to -48.9 per half beat on the attacks; Vc/Cb are at -54.
- B #6: Bn2 259 is -33.3 (c08 -29.8); Fl1 is -34.2.
- C #1:
  - Band shares: 100-250 Hz -11.2 -> -9.6 (target -8.8, not met). 20-100 Hz -18.9 -> -16.7. 2-6 kHz -9.25 -> -10.06. 6-20 kHz -25.9 -> -29.2.
  - The melody margins at bars 57-60 and 75-81 are within 0.7 dB of c08.
- C #2: no effect. The tails still sit at the seat: Vln I sustain -7.7 / tail -7.6 dB R-L, Cb +7.4 / +7.3.
  - Inferred: the Opus channel pan is applied before the send's tap point, or the patch recordings already carry the seat. Pre-fader sends do not unpan the hall.
- C #4: the stem-tail darkening is still small (median 2-8 kHz change -1.15 dB; target -4). The darker top end of the master comes mostly from the Vln I shelf.
- C #5: master -10 to -40 dB after the last release: 0.9 -> 1.05 s (target 1.2).
- C #6: master 8-16 Hz -38.5 -> -50.2 and 16-25 Hz -40.0 -> -45.7 dB re 400-1000 Hz.

## Rejected or deferred

- C #2 fallback (a REAPER Hall bus with ReaVerb and post-fader track sends, Opus reverb off): deferred to the next cycle.
  - The pre-fader send is left in place: it is harmless and keeps the reverb input level.
  - A Hall bus needs a full rebuild and a new IR choice. It is the remaining route to unpanned tails and real tail darkening.
- A #4 extra -2 role on Horns 3-4: not needed (the EQ lowers the level; Hn3/Hn4 now sit 3-5 dB under Cl1 in bars 87-89).
- A, unranked: the flute vibrato CC1 test is deferred.
- Open: CA 129.5 / 133.5 and Fl1 190 / 256 / 270.5 joins (6-9 dB). Vla 146 bow-change fall. Vln I 65 early body still 7-8 dB under at +0.1 s. 100-250 Hz still 0.8-2 dB short of the references.

## Machine note

- render_cycle.py renders into an existing `cycles/cNN/render/` folder. When that folder already holds stems, REAPER appears to wait on an overwrite prompt, which the bridge cannot answer. Empty the folder before rendering again (inferred from this cycle's stall; not changed in render_cycle.py, which someone else is editing).
