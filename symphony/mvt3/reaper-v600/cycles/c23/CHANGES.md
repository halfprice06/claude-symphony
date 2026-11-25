# Cycle 23 (2026-11-17): fff arrivals, chorale repeats, trumpet off-beats, inner lines, wind legato holes, basses' timing, opening chord

Critics' reports: `reports/A.md`, `B.md`, `C.md` (on the c22 render), the coordinator's rulings 1-8 and its later notes (scherzo c20 / c21). Snapshot before this cycle: `before/`. Scripts: `actor_scripts/` (`meas23.py` the ruled targets on a full render or a range folder, `holes23.py` legato holes with `--w200` / `--force`, `op23.py` opening chord, `deliv23.py` delivered-file checks with `DM_HEAD_S`, `stops23.py`, `chk23.py` / `pd23.py` data checks, `mix23.py` mix variants, `simdeliv.sh`; lock phase `auto1.sh`, `p1.sh`, `pa.sh`, `ana.sh`, `p2.sh`, `p3.sh`, `wait_lock.py`, `rr.py`). Logs: `logs/`, `phase.log`, `p12.log`.

Standing rule (Dan): no per-note move in the track volume envelope. Every change below is on the instrument side, a passage role level, a tempo change or a delivery ride. The data check (`stepcheck.py`) finds 31 fader moves inside notes against 32 in c22 (no new one; the end of Violins II's -7 dB row inside a note at 936 is gone).

## For Dan

- **Loudness unchanged:** -14.0 LUFS, quiet passages about -22.4 LUFS. The limiter now takes 5.9 dB off the final chord (c22: 6.0).
- **The three big arrivals now step up.** The bars before bar 223, bar 263 and the final chord are turned down a little in the delivery, so each arrival is louder than the bar before it: bar 223 by 3.4 dB (c22: 1.7), bar 263 by 1.2 dB (0.5), the final chord by 1.1 dB (0.6). The crescendos into them still grow, and the final chord is as loud as bar 223.
- **The final chord's ring no longer swells in the mp3.** The delivery had been lifting the hall tail after the last chord (it fell only 8 dB in 0.3 s); now it falls 16 dB, like the other stops.
- **The chorale's repeated brass notes (bars 224-234) are now heard as separate notes.** A short break before each repeated whole note (0.12 s brass, 0.08 s winds) instead of 0.025 s: they dip 5-11 dB (c22: 0.4-4 dB). The chord at each bar line does not open a hole (3.7 dB at most).
- **The trumpets' soft off-beats in bars 159-166 are back at the right level:** 2.4 / 3.5 dB under Horn 3 (c22: 9-11 dB under).
- **Inner lines:** the second violins' moving line in bars 230-233 is now 2-7 dB under the violas (c22: 8-13), and they join the first violins' tune in 226-229 at nearly equal level. Horn 3's soft upper note in bars 235-237 is 5.5 dB closer to Horn 4 (still 8.5 dB under). Oboe 1's held F in bars 143-144 is now as loud as the clarinet's D (c22: 12.6 dB under; this overshot the aim of 5 dB under).
- **Woodwind legato notes:** the eight notes with the worst early dip (oboe, cor anglais, clarinet) now play without it. Two other ideas for the remaining dips did not help or could not be tested.
- **The basses' hammered eighths are now on the beat:** their attack moved 40 ms later, peaking with the timpani.
- **The opening chord:** the mp3 now starts 0.3 s before the first beat, so the strings' attacks are no longer cut off, and Horn 1 and the tuba enter with the chord (they were 0.1 s late).
- **Not fixed:** no real breath before bars 223 and 263 (the strings lift, but winds and brass hold through); Trumpet 3's accents in bars 257-262 still only 1.3 dB; Horn 4's long soft note in bars 43-47 still wobbles (6.6 dB); the cellos still hang over three tutti stops.

## Results (main render 14:21-14:31)

- **Delivered (`mvt3-mockup-c23.mp3`, re-delivered after the render with the refitted rides, `logs/deliv_c23.log`; the file starts 0.30 s before qn 0):** -14.0 LUFS, LRA 11.6 LU, true peak -1.1 dBTP, p10 short-term -22.4 LUFS, limiter 5.9 dB (final chord), 4.8 (223), 3.8 (263). In-bar momentary maxima: final -7.5, 223 -7.5, 263 -7.8, loudest ff bar -8.3 (bar 5). First delivery (`mvt3-mockup-c23-first.mp3`, the pre-render rows): same loudness, limiter 6.4 dB, final-chord tail drop 7.8 dB.
- **Master:** -19.5 LUFS, LRA 22.6, sample peak 1.218 (float stem sum, the final chord; c22 1.072).
- **Attack probe:** 0 late or holes. State guard 0 stale. score_to_parts.py printed no WARNING.
- **REAPER memory:** 45 GB before the render (0 compressed), 46 GB after (0 compressed).
- **Lock:** 13:22:47-14:32:26, 70 min (waited 2 h 26 min for Movement I and the scherzo). Start and settle 12 min; control range 4 min; T1 build and range 5 min; the vB build deadlocked REAPER (13:44, killed 13:54); restart and cold reload 12 min; final build, state guard, restart and settle 13 min; render 10 min.

| target (ruling) | c22 | c23 | goal |
|---|---|---|---|
| mp3 in-bar step 223 / 263 / final (1) | +1.7 / +0.5 / +0.6 | +3.4 / +1.2 / +1.1 | +1 or more each, final at or over 223 (met: tie) |
| bars 219-223 / 256-263 / 273-277 on the mp3 (1) | rising / rising / 273 > 274 | rising / rising (257 0.3 under 256) / rising | no inverted printed crescendo |
| bar 130 / 131 / 132 on the mp3 | -9.8 / -11.1 / -10.2 | -11.1 / -10.9 / -10.0 | rising |
| master dip in the 150 ms before 888 / 1048 (1) | 0.3 / 4.0 | 2.4 / 3.1 | 6 or more (not met) |
| chorale repeat dips median, under 4 dB (2) | 2.8, 24 of 35 | 5.5, 4 of 35 | 4 or more |
| master bar-line holes 60-500 Hz 896-932 (2) | 0.7-3.3 | 0.7-3.7 | 3 or less (4 of 10 over 3; none over 6) |
| trumpet off-beats re Horn 3, Tpt 1 / 2 (3) | -8.8 / -11.2 | -2.4 / -3.5 | -2 to -4 |
| Vln II - violas bars 230-233 (4) | -7.6..-13.3 | -1.6..-7.3 | 2-4 under (mostly) |
| Horn 3 - Horn 4 bodies 936-948 (4) | -14.0 | -8.5 | within 1-3 (not met) |
| Oboe 1 - Clarinet 1 568-576 (4) | -12.6 | -0.7 | about -5 (overshot) |
| wind legato holes of 6 dB or more, Fl1 / Fl2 / Ob1 / CA (200 ms) / Cl1 / Bn1 (30 ms) (5) | 2 / 2 / 3 / 2 / 6 / 6 | 2 / 2 / 1 / 1 / 3 / 10 | halved; Bassoon 1: render variance (unchanged data; four notes crossed 6 dB by 0.6-1.1 dB) |
| basses half-rise / peak re beat, timpani half / peak (6) | -68 / -13, +22 / +32 | -27 / +27, +22 / +32 | half within ±20 and 30 of timpani; peak within 15 (peak met, half 7 ms short) |
| basses 816-840 p90 / separation (6) | -33.9 / 14.9 | -32.2 / 11.4 | -32.2 or louder / 7 or more |
| opening chord pcx median / spread (7) | +44 / 117 ms | +32 / 126 ms | ±15 / under 80 (not met: celli +117, Violins II +77, Horn 4 +66); Horn 1 +131 -> +26, Tuba +78 -> -2 |
| mp3 first 10 ms (7) | (cut attack) | silent (fade-in) | -60 dBFS or lower |
| Trumpet 3 accented - plain peaks 1016-1048 (8) | +0.8 | +1.3 | +2 to +3 (not met) |
| Horn 4 held note 0.25 s range (8) | 6.4 | 6.6 | 5 (not met) |
| celli -10 dB after the stops 374 / 450 / 814; master +0.3 s at 814 (8) | +385 / +235 / +315 ms; 12.5 | identical | 180 ms; 15 (not met; rt_ms rejected) |
| mp3 stops bars 2 / 6 / 94 / 113 / 166 / 204 / final (coordinator) | 15.2 / 15.1 / 15.0 / 15.5 / 15.0 / 16.1 / 7.9 | 15.3 / 15.3 / 14.9 / 14.8 / 16.1 / 16.1 / 15.6 | 14.5-17 |

## Range pass (under the lock; control range CTRL = the c22 project as saved, T1 = the c23 data, same starts 296 / 598 / 790)

- Range starts chosen where the measured tracks have a keyswitch before their first note (coordinator, `cycles/c19/actor_scripts/rangechk.py`); 446-454 dropped (no keyswitch on most tracks), Bassoon 1 in 296-394 has none (its counts there are unreliable).
- T1 = c23 data with mix variant (a) LegatoSpeed SSOFFSET 11025 on the six wind tracks and celli `rt_ms` 80. Per-note levels T1 against CTRL (`rr.py eq`, `logs/T1_eq.log`): 2144 of 2561 notes within 0.5 dB; tracks with no data or state change in these spans (Bass clarinet, Contrabassoon, Bass trombone, Tuba, Bassoon 2) all within 0.5 dB; the celli (state change) 52 of 195 over 1 dB. CTRL's chorale dips equal the c22 full render within 0.6 dB.
- (a): on the legato targets that stayed legato, 6 dB holes 4 -> 6 (Flute 1 330 and Flute 2 602 / 650 better; cor anglais 650, Clarinet 330 / 940, Bassoon 850 worse). Rejected.
- (c) Sus row 0.06 s early: all 8 targets under 6 dB. Adopted.
- Celli rt_ms 80: celli fall times identical (385 / 315 ms). Rejected. (The coordinator's any_dyn note does not apply: every celli group on these rows has a dynamic word in its name.)
- Basses lead 0.06 s: as in the table. Adopted.
- Chorale gaps: as in the table (T1 equal to the full render within 0.5 dB). Adopted.
- vB (TLeg hold 550 / decay 250 ms): REAPER deadlocked during the vB build (bridge heartbeat stopped at 13:44 while Flute 1 loaded its new state); killed at 13:54 and dropped. The final mix.json is c22's (neither (a) nor rt), so the six wind tracks and the celli were rebuilt in full back to their c22 states.

## Changes (files and values)

- **Ruling 1 (fff arrivals; C #1, B #1):**
  - `build/score_config.py` c23 block: `CAESURA` 888.0 0.06 s (112 -> 77 bpm over 887.75-888) and 1048.0 0.05 s (176 -> 111 bpm over 1047.75-1048); `PHRASE_ARCS` (888, 912) -> (892, 912), so bar 223 starts at 112 without the arc's push. Tempo points changed at 889, 893, 900, 902, 1047.75, 1048 (`--midi-only --tempo` on every track).
  - String lift before 1048: `INSTR_POST["note_end"]` rows `{"end": 1048.0, "tol": 0.3, "gap_next_s": 0.06}` on Violins I, Violins II, Violas, Violoncellos (new generic key `gap_next_s` in `tools/instr_post.py`: the note sounding into the arrival ends 0.06 s before the track's moved 1048 note-on). Violins I's 34 ms overlap became a 60 ms gap; no CC11 fall.
  - Delivery rows (`RIDE_TRIMS`, replacing the c21 / c22 rows that start at 883.5, 1031.5 and 1079.5): bar 223 `[879.5 0, 880 -3.5, 884 -5.0, 887.9 -5.0, 888 -4.5, 891.5 -4.5, 892 0]`; into 263 `[1023.5 0, 1024 -2.5, 1032 -3.5, 1040 -3.0, 1046 -2.5, 1047.8 -2.5, 1047.95 0]`; into the final `[1079.5 0, 1080 -3.5, 1088 -3.5, 1092 -2.5, 1096 -2.0, 1104 -3.0, 1107.8 -3.5, 1107.95 0]`; bar 130 `[511.5 0, 512 -1.5, 519.5 -1.5, 520 0]`.
- **Ruling 2 (chorale same-pitch repeats; A #1, B #4, C #3):** the c19 chorale rows (896-932): same-pitch `gap_set` and `onset_lead` gaps 0.025 s -> 0.12 s on Horns 1-4, Trombones 1-2, Bass trombone, Tuba; 0.08 s on Oboes 1-2 and Clarinets 1-2 (Trumpets and Flutes keep 0.025 s). The c22 `move_fall` rows are gone; those rows now carry `no_fall` (new `onset_lead` key in `tools/instr_post.py`): the re-tongue CC11 fall before the repeat is removed, also on notes the row does not move (Horns 2-4 kept a 12-unit fall on the first build because their lead was unchanged).
- **Ruling 3:** Trumpets 1-2 `vel_add` at 632.9-662.5: +4 -> +7 (velocity 95, the top layer of "Stac DblTng RRx9").
- **Ruling 4:**
  - `build/roles.json` Violins II `[888, 936, -7]` -> `[888, 899.9, -7]` + `[899.9, 936, -1]`; the crossfade runs over 899.848-899.866 (new score_config `ROLE_EDGE_XF`, read in `tools/score_to_parts.py`), between the tremolo's end (899.847) and the moved note-on of 900 (899.867).
  - `cc_scale` (CC11): Horn 3 +8 dB, Horn 4 -3 dB, k 40, over 935.6-947.75 (Horn 3 CC11 34-46 -> 54-73); Oboe 1 +5 dB, k 33, over 567.5-575.75 (CC11 61-69 -> 86-98).
- **Ruling 5 (wind legato holes):**
  - (c) data: Oboe 1 384 / 964 / 1014, Cor anglais 708 / 738, Clarinet 1 606 / 998 / 1014 on the sustain row ("Sus MAX"; the clarinet's "Sus Non Vib"), 0.06 s early, no overlap (`ART_SPANS`, `onset_lead`, `gap_set` `only_at`).
  - (a) / (b): range-test only, not in the render: mix.json variants (`cycles/c23/actor_scripts/mix23.py`): (a) LegatoSpeed `SSOFFSET` 11025 with `SUS_GROUP_SUBSTRING` "OBs" / "Cls" on the oboe / clarinet; (b) new mix.json key `tleg_env` (`tools/build_reaper.py tleg_env()`): TLeg hold 550 ms, decay 250 ms. Both on Flute 1, Flute 2, Oboe 1, Cor anglais, Clarinet 1, Bassoon 1.
- **Ruling 6 (basses):** `row_onset` lead 0.10 -> 0.06 s (all spans); 816-840 length 0.33 -> 0.37 qn (`len_frac` 0.74); `roles.json` `[820, 840, -4]` -> -2.5.
- **Ruling 7 (opening chord):** `tools/render_cycle.py` keeps the last 0.30 s of pre-roll (`render_head/`), `tools/deliver_master.py` `DELIVER_HEAD` puts it before the mp3 (10 ms fade-in); `build/entry_leads.json` Horn 1 0.0 +0.03 s, Tuba 0.0 +0.01 s (total entry leads 0.12 / 0.08 s).
- **Ruling 8:** Trumpet 3 accents 1016-1048 `amt_rel` 0.10 -> 0.20, hold 0.15 s, back by 0.45 s, `max_step` 12 -> 20; Horn 4 CC11 fill points shifted / narrowed (A's values); celli `rt_ms` 80 at mf-ff tested in the range pass and rejected (mix.json unchanged from c22).
- Delivery rows refitted after the render (re-delivered on the c23 master): bar 223's arrival -4.5 -> -5.0; the final row -4.0 -> -4.5 at the chord and -8 dB over its tail from 1113.3 to 1120.
- Tools: `tools/build_reaper.py` `tleg_env()`; `tools/instr_post.py` `note_end` `gap_next_s`, `onset_lead` `no_fall`; `tools/score_to_parts.py` `ROLE_EDGE_XF`; `tools/render_cycle.py` pre-roll head (`render_head/`, env `RENDER_HEAD_S`); `tools/deliver_master.py` `DELIVER_HEAD`. README "c23 pipeline notes".

## Rejected or deferred

- LegatoSpeed SSOFFSET (5a): range test, holes 4 -> 6 on untreated targets. Rejected (LEARNINGS, MANUAL-GAPS).
- TLeg hold / decay (5b): not measured (REAPER deadlock). Open for c24.
- Celli rt_ms 80 (8): no change. Rejected. CC11 taper before the three cut-offs (C's fallback) not done.
- LegRep RRx4 fallback for the chorale: not needed (no hole over 6 dB).
- A full breath before 223 / 263: the string lift and caesuras alone do not dip the master; a lift on winds and brass is the next step.
- Stem fixes: none (Oboe 1's overshoot at 568-576 found after the lock was released; for c24: +5 -> about 0 dB, or -5 dB from here).

## Faults introduced or left

- Oboe 1 bars 143-144 overshot: level with Clarinet 1 (aim 5 dB under).
- Bassoon 1 legato holes 6 -> 10 over 6 dB by the 30 ms measure, with unchanged data (render variance; four notes crossed 6 dB by 0.6-1.1 dB).
- The mp3 now starts 0.30 s before qn 0: anyone measuring the mp3 on the tempo map must add 0.30 s (deliv23.py / stops23.py take `DM_HEAD_S=0.30`).
- Master sample peak 1.218 on the final chord (float sum; the delivery limiter takes 5.9 dB there).
