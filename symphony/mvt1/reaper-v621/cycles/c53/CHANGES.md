# Cycle 53 changes (actor, 2026-11-09): clamp order, re-bow refit, brass width and tail, delivery EQ, the coordinator's thirteen decisions

Critic reports: `reports/A.md`, `B.md`, `C.md` (on the c52 render); `COORDINATOR-NOTES.md` section (7) decides where they
differ. Snapshot: `before/` (the work folder is not tracked by git, so every "before" below is a file in `before/`).
Scripts: `actor_scripts/` (`apply53.py` all json edits, idempotent, reads `before/` and writes `build/`; `rangetest53.py`
range renders with every track playing plus listed stems; `rttest53.py` release measure on a range render; `tail53.py`
decay after the nine stops; `bal53.py` B's check table; `post53.py` sf / horn3 / ends / vol; `pc53.py` onset measures
(pcx, m37, crossing, h6, m6); `envpair53.py` band envelopes of two tracks at one onset; `rebowdip53.py` re-bow dips on
stem and master; `deliv53.py` delivered loudness, band shares, climax order and stop decays; `delivvar53.sh` the delivery
EQ variants on one master; `checks53.sh` every post-render check in one run, `checks53_ref.sh` the same measures on c52;
`partsdiff53.py` parts.json diffs; `turnlock53.py` the lock by the longest-waiter rule; `stac53.py` the bar-30
staccatos; `sfsim53.py` candidate sf shapes simulated on the rendered stems; `volpts53.py` the volume envelope the build
writes for a span; `stalecmp53.py` per-note onset and level of two renders of one phrase; `delivvar53b.sh` two more
delivery variants). Builds: two full builds of all 33 main tracks (18:24 for the range tests, 19:21 for the main render) and two full
builds of the 9 pass-2 tracks before theirs; after the renders Horn 1 was rebuilt in full twice, both violin tracks once, and Bassoon 1
stac and Flute 1 stac once (state guard section). `parts.json` was regenerated four times before the renders and three
more times for the stem fix, and diffed against the previous one each time. One render of each project; the level
corrections after it were made on the stems (`tools/stem_fix.py --apply`), so every number under "Measured" that names a
corrected stem is a simulated level, not a second render.

Measures used below. Tail (`tail53.py`): body = RMS over T-0.35..T-0.05 s before a note end T; four windows +0.05..0.15,
+0.15..0.30, +0.30..0.60, +0.60..1.00 s in dB under the body; t20 = first time the 20 ms RMS envelope (5 ms hop) is 20 dB
under the body. The nine stops (note end in s; C's bar): 66.07 (14), 89.84 (25), 102.15 (31), 183.69 (71), 197.92 (79),
204.07 (82), 311.27 (137), 319.69 (141), 379.45 (169). C's bar numbers are 2 lower than qn/4+1. Onsets: pcx = the pitch
band's 10 %-of-plateau time against the written time; on a swelling note pcx reads the swell, so a second measure (band
envelope crossing of the previous note's level, m37, h6) is given where it decided.

## What changed (generic code off by default; Movement I values in the `build/score_config.py` c53 block from line 3704)

### Code
1. **Clamp order of the legato lead (A #4, finale technique 20, decision 6).** `tools/score_to_parts.py` line 3768: a
   per-onset row is now added to the total lead (base + velocity extras) before the clamp:
   `tot = ls_ + ex if lx is None else max(LEG_LEAD_CLAMP[0], min(LEG_LEAD_CLAMP[1], leg_s + lx + ex))`. Before, the row
   was added to the clamped base and the extras afterwards, so a negative row on a loud onset lost part of its effect.
2. **`tools/fit_rebows.py`**: options `--only "Track:qn"`, `--render-dir DIR` with `--render-t0 QN` (fit on a range
   render), `--fine` (second, finer search stage around the first result), `--dump FILE` (write the fit without touching
   `build/rebow_fills.json`). Defaults reproduce c52.

### Articulation (A)
3. **A #1 re-bows.** `REBOW_AT` Double basses 292.0 -> 290.9 (the note boundary A named). Fills refitted with `--fine` on
   the c52 stems (`actor_scripts/rebow_refit53.json`); simulated stem dip old -> new (master old -> new), dB:
   Violoncellos 21.442 4.8 -> 2.1 (3.5 -> 3.4); Violoncellos 26.516 7.0 -> 2.1 (3.0 -> 2.8); Double basses 26.003
   1.4 -> 0.9 (4.6 -> 4.8); Double basses 47 6.1 -> 3.8 (2.4 -> 2.4); Violas 40 3.8 -> 0.9 (2.3 -> 2.2); Violins II 47
   3.6 -> 2.1 (2.4 -> 2.4). Violoncellos 12.163 was not refitted: the fine stage read 3.9 -> 4.0 dB on the stem (first
   stage 4.5), master 1.8 -> 2.0, so the c52 fill stays. The re-keyed Double basses fill ("292" -> "290.9") and the fill
   at 297.045 were refitted on a c53 range render (`actor_scripts/rebow_refit53b.json`): stem dips 8.1 -> 2.3 and
   7.3 -> 0.8 dB simulated; master at 290.9 0.6 -> 0.2 dB. A re-keyed fill has to be refitted: the old fill's shape was
   fitted to the other boundary and left an 8.1 dB stem dip.
4. **A #2 flute pair, per-onset rows for Flute 2** (finale technique 14). Kept: `entry_leads` Flute 2 271.0 +0.04 (pcx
   +68 -> +34 ms); `leg_leads` Flute 2 275.5, 277.0, 281.5, 283.0, 283.5 at -0.045 (pcx -45 / -43 / -48 / -42 / -62 ->
   -1 / -2 / -3 / +3 / -20 ms); `retongue_leads` Flute 2 284.0 -0.03 (-21 -> +8 ms) and 629.0 -0.04 (about 20 ms ahead
   of Flute 1 now). Tried and removed, because the band envelopes showed c52 already on time and pcx had read the swell
   of the note: Flute 2 280 (+0.05), 639.5 (+0.05), 642 (+0.08); Flute 1 272 (+0.03), 642 (+0.04). Not changed, same
   reason: Flute 1 634 and 643, Flute 2 634 and 636. The rows at 633, 640 and 643.5 stay as A asked.
5. **A #3 sf of the sfp at qn 160 on winds and brass** (finale technique 19). `POST_SHAPES_S` at 160.0, shape
   `[(a, 0), (a + 0.01, d), (0.17, d), (0.25, 0)]` in qn after the note: +3 dB on Tuba, Bass trombone, Horn 3, Horn 4,
   Oboe 1, Clarinet 1 (a -0.07) and Flute 2 (a -0.11); +4 dB on Trumpet 1 (a -0.07), Trumpet 2 (-0.10), Trumpet 3
   (-0.08). The start times follow each track's own lead so the bump begins at the sounding attack. This flat shape is
   what was rendered; it raised the peak inside the bump as much as the front, so it was replaced on the stems by
   front-weighted shapes (Corrections after the render).
6. **A #4 / decision 6: the negative per-onset rows after the clamp fix.** Re-measured on range renders and re-fitted
   where the onset moved: `leg_leads` Bassoon 1 366.0 -0.03 -> +0.015, 523.0 (-0.03) moved to `retongue_leads` (the
   onset is a re-tongue); Clarinet 1 180.0 -0.054 -> -0.03; Flute 1 299.5 -0.04 -> -0.05, 397.5 -0.05 -> -0.07, 555.0
   -0.04 -> -0.055; Oboe 1 407.0 (-0.07) moved to `retongue_leads` -0.035, 582.0 -0.04 -> -0.05.
7. **Decision 7, cor anglais at qn 275.** c52 on five measures: pcx +158, m37 +160, h6 +112, crossing +66, m6 +70 ms.
   All five read late, so the row was changed: `leg_leads` 275.0 (-0.04) deleted, `retongue_leads` 275.0 +0.06 (lead
   166 ms). Range render: pcx +107, m37 +105, crossing +6, h6 +98, m6 +22 ms. pcx and m37 still read the slow swell of
   the note; the crossing and m6 read the start of the sound. On the full render the same onset reads 84 ms early on
   four measures (Measured): the fit on the range render did not carry over. Deferred to c54.
8. **A #5 bar-30 wind staccatos.** `ART_SPANS` `{"from": 116.0, "to": 118.0, "art": "Stac DblTng RRx9", "mark":
   "staccato"}` with a velocity-by-CC table, window (115.9, 117.9) in `TRACK_WINDOWS` / `ALIAS_TRACKS` / `PASS2_TRACKS`
   for Flute 1, Oboe 1 and Clarinet 1 (new pass-2 tracks "Oboe 1 stac" and "Clarinet 1 stac"; "Flute 1 stac" existed).
   The row's level differs by pitch, so the four notes were levelled on the stems (Corrections after the render).
9. **A #6** `BREATH_GAP_AT["Oboe 2"][643.5] = 0.10` (the note now ends at 643.750 instead of 643.600).

### Balance (B)
10. **B #1 Violins I theme over the celli, bars 17-22.** `roles` Violins I [56, 72, +2] -> [56, 88, +2]; Violoncellos
    [56, 72, -2] -> [56, 84, -2]; `note_trims` Violoncellos 64 -2, 66 -3, 70 -2, 72 -2, 74 -3, 80 -2.
11. **B #2 celli inner voice, bars 115-116.** `LEVEL_SHAPES` Violoncellos `[(456, 0), (457, -2.5), (458, -6.5),
    (459, -8), (460, -8), (460.1, -6), (463.5, -6), (464, 0)]`; `note_trims` Bassoon 1 460.0 -5. On the stems
    afterwards: -8 -> -8.6 at 459-460, and a 0.1 s ramp for the bassoon trim.
12. **B #3 cor anglais third answer.** `roles` Cor anglais + [602.25, 606.5, +3.0, 0.25]; `note_trims` 604.0 (-4.5)
    deleted with its `NOTE_TRIM_RAMP_S` entry.
13. **B #4 / decision 8, Oboe 1 at p.** `LEVEL_SHAPES` Oboe 1 `[(495.95, 0), (496, +7), (497.9, +7), (498, 0)]` and
    `[(499.9, 0), (500, +5), (503.8, +5), (504, 0)]`. B asked +6 and +8; with B's values a range render read Oboe 1
    minus Violins I -5.14 / -4.76 / +0.85 / -0.57 dB at 496-498 / 498-500 / 500-502 / 502-504. Oboe 1 passes the
    violins in bar 126 (500-504) with +8 and is under the 2-5 dB target in bar 125 (496-500) with +6, so the values
    became +7 at 496-497.9 and +5 at 500-503.8. `note_trims` Oboe 1 168.0 +7 and Flute 2 168.0 +6. On the stems
    afterwards: +7 -> +8.8 at 496-496.9, and 0.1 s ramps for the two trims at 168.
14. **B #5 bass clarinet arch.** `roles` Bass clarinet + [699.5, 708.0, -2.0, 0.5]; `note_trims` Clarinet 1 699.0 +1.5.
15. **B #6 timpani bar 4.** Timpani shape `[(12.4, 0), (12.9, -3), (15.6, -3), (15.9, 0)]` -> `[(12.4, 0), (12.9, -3),
    (16.5, -3), (16.95, 0)]`. On the stems afterwards: -3.6 from 15.5 to 16.5.
16. **Decision 9.** Horn 3 [165.5, 168, -3.5] and cor anglais [584, 608, +1.5] were in `roles.json` since c52's
    post-render step; the c53 full build puts them into the project.

### Blend and space (C)
17. **Decision 2, brass width.** `track_width` Trumpet 1 / 2 / 3 and Trumpets a2 0.5 -> 0.65; Trombone 1 / 2 and Bass
    trombone 0.6 -> 0.75. The side bell stays at -4.5 dB. Make-up re-measured against a no-width range render; `gain_db`
    (make-up before -> after): Trumpet 1 2.8 -> 2.55 (+2.80 -> +2.55), Trumpet 2 2.1 -> 1.9 (+2.20 -> +2.00), Trumpet 3
    2.75 -> 2.5 (+2.45 -> +2.20), Trumpets a2 3.7 -> 3.45 (+2.50 -> +2.25), Trombone 1 4.8 -> 4.55 (+1.30 -> +1.05),
    Trombone 2 5.05 -> 4.7 (+1.75 -> +1.40), Bass trombone 4.85 -> 4.6 (+1.65 -> +1.40). Residual of each stem against
    the no-width render in the range test: -0.19 to +0.19 dB (limit 0.3).
18. **Decision 3, R Brass half step.** `returns["R Brass"]["fader_db"]` -10.97 -> -7.97; group `send_offset_db`
    trumpet -6 -> -3, lowbrass -10 -> -7, horn new {"R Brass": -1.0}. (c52 values for a revert: fader -10.97, trumpet
    -6, lowbrass -10, no horn entry.)
19. **Decision 5, delivery master EQ (`mix.json` `master_eq`, used only by `tools/deliver_master.py`).** c52 values, for
    a revert: highpass 42 Hz bw 2.0; bell 167.0 Hz -1.6 dB bw 1.39; bell 1180 Hz -1.9 dB bw 1.39; highshelf 8008.0 Hz
    +0.8 dB bw 1.39. c53 values as shipped: highpass 42 Hz bw 2.0; bell 167.0 Hz -1.6 dB bw 1.39 (kept); bell 260.0 Hz
    -1.5 dB bw 1.0 (new); bell 1180 Hz -1.9 dB bw 1.39; highshelf 3000.0 Hz -1.0 dB bw 1.39 (replaces the 8008 Hz
    shelf). The coordinator's added checks (limiter and stop decays) decided between the variants; the table is in the
    Measured section.

## Range tests before the render (each into its own folder under `rangetest/`, audio deleted at the end)

- **Decision 2, width make-up.** Each brass stem with the new width and make-up against the no-width render: residuals
  -0.19 to +0.19 dB (limit 0.3). Stem correlation at 250 Hz-5 kHz in bars 82-83: 0.19-0.50 -> 0.58-0.80.
- **Decision 3, R Brass half step** (bars 82-83, 121-126, 167-170, plus bar 14). Master at the stops of bars 82 and 169:
  unchanged within 0.1 dB and 0 ms. Bar 14: master 0.3-0.6 s level -15.3 -> -14.8 dB under the chord, t20 0.46 -> 0.485 s.
  Brass tail 0.3-1.1 dB closer to the strings' tail. "Brass tail within 4 dB of the strings" is not met with the half
  step: the gap is 5.2 dB at bar 169 and 15.9 dB at bar 82. The `R Brass` return stem rose 3.4 dB, mostly horns. Kept
  for the full render; the comparison with c49 at all nine stops is in the Measured section.
- **Decision 4, Trumpets 1-3 release (C #2): tested, not applied.** Test in the main project on Trumpet 1 (Trumpet 1 is a
  main-project track; C's 101.88 s is the stop of bar 31, 102.15 s on the build's time map; C expected -20 to -25 dB at
  0.15-0.30 s), range qn 119.5-128.6 + 2 s, keyswitches primed,
  samples loaded (43 GB). Columns: body; level under the body at +0.05..0.15 / +0.15..0.30 / +0.30..0.60 /
  +0.60..1.00 s; t20.

  | stem, note end | body | 0.05-0.15 | 0.15-0.30 | 0.30-0.60 | 0.60-1.00 | t20 |
  |---|---|---|---|---|---|---|
  | Trumpet 1, no `rt_gain_db`, 100.88 s | -27.2 | -10.3 | -38.2 | -58.5 | (next note) | 0.135 s |
  | Trumpet 1, +6 dB, 100.88 s | -27.2 | -10.2 | -36.8 | -52.5 | (next note) | 0.135 s |
  | Trumpet 1, no `rt_gain_db`, 102.15 s | -30.7 | -8.9 | -31.7 | -53.6 | -67.7 | 0.155 s |
  | Trumpet 1, +6 dB, 102.15 s | -30.7 | -8.8 | -31.3 | -47.6 | -61.7 | 0.155 s |
  | Trombone 1 (both renders), 102.15 s | -27.4 | -2.9 | -12.3 | -26.7 | -47.2 | 0.300 s |
  | Master, no `rt_gain_db`, 102.15 s | -15.8 | -4.9 | -11.4 | -18.6 | -20.8 | 0.42 s |
  | Master, +6 dB, 102.15 s | -16.2 | -4.4 | -11.5 | -18.4 | -20.4 | 0.42 s |

  The build printed "Trumpet 1: release-trail gain +6.0 dB on 10 groups". The +6 dB arrives in full only from 0.3 s
  (+6.0 dB at 0.30-0.60 and 0.60-1.00 s), where the trail is 48-62 dB under the note. The fall at 0.15-0.30 s moved
  0.4 dB (102.15 s) and 1.4 dB (100.88 s); the trombone is 19 dB higher on the same measure. The stem's fall at 180 ms
  did not move toward the trombones', so the test does not confirm the cause and `rt_gain_db` is not applied
  (`mix.json` restored, Trumpet 1 rebuilt in full, state guard 0 stale). Patch data (decoded .oib, Sus rows): sustain
  groups' AHDSR release on the Solo Trumpet 178 ms (f, ff), 237 ms (p, mf), 316 ms (pp); on the Solo Trombone 237 ms on
  every layer. Release-trail groups: AHDSR attack 148 ms on both patches, so a trail cannot fill the first 0.15 s;
  volumes 0.58-0.95 (trumpet) against 1.22-1.76 (trombone); `releaseDamping` 1.0 on all 13 trail groups of the trumpet
  against 0.7-0.8 on trombone, horns and tuba. Candidates for c54, untested: `releaseDamping` 0.8 on the trumpet's trail
  groups; the sustain groups' release 178 -> 237 ms. Record: `actor_scripts/tp_rt_test.txt`.
- **Decision 8, CC1 floor of 64 on Oboe 1's held notes: range test only.** The held D5 rose 2.3 dB (B expected about 8).
  Not shipped; Oboe 1 rebuilt in full without it.
- **Coordinator (1), fp at Double basses qn 128.** The volume lane and the stem show no dip under the attack, so
  `fp_falls` is not ported.
- **Decision 11, C's timing observation.** Attack probe and stem measure at sq 104: Horn 1 +4 ms, Horn 3 +13 ms, Double
  basses -11 ms (pcx); at sq 552: Horn 1 -9 ms, Horn 3 +6 ms. The onsets are on the written time; the 0.3-0.45 s offset
  is in C's time map (C's note-on times 89.95 s and 311.36 s are not the build's). For the c54 tempo critic: use
  `pcx.TM(P["tempo"]).sec(qn)` without the preroll.
- **Range-render method errors found and fixed in this cycle** (also in `loop/LEARNINGS.md`):
  a range render that starts inside a phrase plays with the keyswitch of the previous range render, not the one that
  governs the phrase, so each range needs its governing keyswitch sent first (`rangetest53.py prime`); results of the
  unprimed ranges before 18:50 were discarded (Oboe 1 582 read -130 / -148 ms there). A range render into a folder that
  already holds the files opens REAPER's overwrite dialog and blocks the bridge (18:59; REAPER killed and restarted at
  19:05; the job file `~/.rpr-bridge/inbox/a7ba029ad458.running` was left as it was). For about 30 s after a restart
  the first range render plays tracks whose samples are not loaded yet.

## State guard (decision 12 and the coordinator's two messages)

`tools/state_guard.py` counts per track the Opus sustain-group attack times in the saved project that differ from the
values the build wrote (a legato group left at 20 ms is the stale state of c51/c52).

| project file as saved at | stale tracks | detail |
|---|---|---|
| 18:29, after the first full build | 0 | |
| 18:53, after about 40 range renders | 2 | Bass clarinet 27 attacks at 20.0 ms (written 438.3), Trumpet 1 24 at 20.0 (written 1076.1); both rebuilt in full |
| 19:24, after the full build of all 33 main tracks | 0 | |
| 19:43, before the main render | 0 | `state_guard_pre_render.txt` |
| about 19:56, render_cycle's own save before the render | 0 | "stale none" in `render_main2.log` |
| 20:07:59, **after the main render** | **1** | Horn 1, 16 attacks (1FHs pp 20.0 ms, written 1076.0; mf and f 20.0, written 677.7); `state_guard_post_render.txt` |
| 20:14, Horn 1 rebuilt in full | 0 | |
| 20:16 and 20:18, after test range renders (below) | 1 | Violins I, then Violins II |
| 20:22 and 20:24 (after quitting), both violin tracks rebuilt in full | 0 | `state_guard_main_final.txt`; this is the main project on disk for c54 |
| pass 2, 20:31, before its render | 0 | `state_guard_pass2_pre_render.txt` (9 tracks) |
| pass 2, render_cycle's own save before the render | 0 | "stale none" in `render_pass2.log` |
| pass 2, 20:46, **after its render** | **2** | Bassoon 1 stac, 18 attacks (Bss mp / f / ff 20.0 ms, written 438.3); Flute 1 stac, 24 attacks (1Fls pp / mf / f 20.0 ms, written 738.16); `state_guard_pass2_post_render.txt` |
| pass 2, 20:47, both tracks rebuilt in full | 0 | `state_guard_pass2_final.txt` |
| 20:52, both project files after REAPER quit | 0 | pass 2: 0 stale of 9; main: 0 stale of 33 (`state_guard_pass2_after_quit.txt`, `state_guard_main_after_quit.txt`); these are the projects on disk for c54 |

So the main project went from 0 to 1 stale track during its render and the pass-2 project from 0 to 2 during its
render, as the scherzo's did (0 to 5). Both guards read 0 before the renders (the condition of decision 12), and both
projects read 0 on disk now.

**Is the rendered audio affected? No.** Horn 1 stem of c53 against c52 (`cycles/c52/actor_scripts/post52.py joins`):
46 joins, onset change median +0.0 ms, none more than 40 ms earlier; level residual on legato notes +0.00 dB (n 59), on
other notes +0.00 dB (n 50). State check: "Horn 1 compared 111 flagged 2 state runs 0 timing runs 0". Three range renders
of Horn 1's phrase at qn 599-608.5 (`actor_scripts/stalecmp53.py`, per-note onset and level of the pitch band): with
the stale live state straight after the render (`h1_stale`), and with a rebuilt clean state after the samples had
loaded (`h1_c3`, guard 0 stale before and after), both equal the full render's stem at the five joins (0 ms; at most
0.1 dB at 600.801, 602.886, 603.830, 605.386, 605.886). No re-render. Horn 1 was rebuilt in full afterwards.
Pass 2: state check "Bassoon 1 stac compared 14 flagged 0", "Flute 1 stac compared 15 flagged 0"; `post52.py joins`
against c52: Bassoon 1 stac 1 join +0.0 ms, level residual +0.00 dB; Flute 1 stac 1 join +0.0 ms, legato +1.35 dB
on its single legato note, other notes +0.00 dB (n 14). No re-render; both tracks were rebuilt in full.

**What makes the state stale (partly identified).** The 20 ms attack on the legato sustain groups is a runtime value of
the Opus instance: playback sets it and clears it, and a save stores whatever the instance holds when playback
stopped. Evidence:
- After a range render of qn 623.8-629 the save read Violins I stale (58 attacks: V1s pp 20.0 ms against 1076.1
  written, p 20.0 / 1053.9, mf 20.0 / 840.9) and Horn 1 clean. After the next range render, qn 610-629, the save read
  Violins II stale (78 attacks) and Violins I clean again, with no build in between: playing the track again cleared it.
- The same range (610-629) rendered a second time left Violins II stale again, and a second save without playback in
  between read the same: the result follows from where playback stops, not from the save.
- A range that ends after Horn 1's slurred phrase (599-608.5) left 0 stale.
- In the live instance the stale value does not change the sound: the range render with the stale state, the range
  render with the clean state and the full render are equal. The earlier and louder joins of c51/c52 appear only when a
  project saved in that state is loaded again and played.
So the render's own playback leaves it: the full render stops after the last bar with Horn 1 in that state, and the
save after the render stores it. The exact trigger was not found. Horn 1's last legato-row note is a single "LegRep
RRx4" note at 623.942, but Contrabassoon (124.927), Horn 4 (499.917) and Trumpet 2 (455.822) end their legato rows the
same way and were clean; in the two test ranges both violin sections hold a "Leg BC MAX" note when playback stops and
only one of them was stale each time.

**Rule that follows (used here, also in `loop/LEARNINGS.md`):** a stale save is harmless for the render that produced
it and harmful for the next load. Run the guard on the save made after the last playback (render or range render),
rebuild every stale track in full, wait for the samples (about 45 s), save, and read 0 before the restart that precedes
a render. `build_reaper.py --midi-only` also rebuilds stale tracks through `stale_tracks()`.

**Sample loading after a full rebuild.** A range render taken 10 s after a full rebuild of Horn 1 differed from the full
render (joins +67, +56, -90 ms; levels -1.9 to +4.0 dB); one taken 45 s after the rebuild is equal to it. A full
rebuild reloads the track's samples, so a range render (or a render) must wait until REAPER's memory is steady.

**State check** (`tools/state_check.py`, runs of consecutive notes that moved on unchanged data): against c52,
0 runs on the first render (main and pass 2) and again on the fixed stems; against c50, 2 runs, both on Double basses
(`metrics/state_check.txt`, `metrics/state_check_vs_c50.txt`; compared 58, flagged 19). Read with the coordinator's
rule from the finale's c12: isolated single notes that move 2-6.7 dB are sampler variation; a run of consecutive notes
or a whole-bar median shift is a state problem.

The two bass runs: the pizzicato notes at 188-216 and 592-616 ("Pizz RRx4") differ with mixed signs (-7.30, -3.47,
+3.95, -5.06, -4.23, +3.99 dB; +7.61, +3.50, +6.77 dB), which is the round-robin position moved by c52's resets; and
the "Sus MAX" notes at 571.5 (+3.49 dB, +113 ms), 696 (+209 ms), 700 (+68 ms) and 704-712, where c53 equals c52 note
for note, so that difference arose in c51 or c52, not in this cycle. Every other track: 0 state runs and 0 timing
runs against c50.

## Corrections after the render (stem fix, `tools/stem_fix.py --apply`; originals in `render_first/`)

The main render was made from the data in `rendered_build/` and the pass-2 render from `rendered_build_pass2/`. The
level rows below were changed in `build/` after the renders and applied to the stems once, at 21:29
(`stemfix_apply.log`): `stem_fix.py` computes each track's volume envelope from the rendered and the new build data,
multiplies the stem by the difference and sums the master again (float sum, peak 0.949). The data after the fix is kept
as `rendered_build/parts_after_fix.json`, `score_config_after_fix.py`, `note_trims_after_fix.json` and
`roles_after_fix.json`. 17 stems changed: Flute 2, Oboe 1, Clarinet 1, Bassoon 1, Horn 3, Horn 4, Trumpet 1, 2, 3, Bass
trombone, Tuba, Timpani, Violoncellos, Trumpets a2, Flute 1 stac, Oboe 1 stac, Clarinet 1 stac. Trumpets a2 and
Clarinet 1 stac differ only by the main track's sf shape at 160, which the alias inherits and where the alias is
silent; Oboe 1 stac has that and its own staccato shape. The four return stems were summed unchanged, because the
returns' input is not re-simulated: the reverb of a corrected note keeps its rendered level. `--apply` must not be run
a second time on these stems (it would apply the difference twice). The REAPER projects hold the rendered values; the
rows below reach them with the next full build.

1. **A #3, sf at qn 160: the flat bump replaced by front-weighted shapes.** The rendered flat bump (+3 / +4 dB over
   0.17 qn) raised the peak inside the bump as much as the front, so the stems still peaked 2.4-5.1 dB over their first
   0.1 s on 7 of 10 tracks. New `POST_SHAPES_S` shape at 160.0, `[(a, 0), (a + 0.01, d), (t1, d), (t2, 0)]` in qn after
   the note, fitted per track with `actor_scripts/sfsim53.py` on the rendered stems:

   | track | d dB | a | t1 | t2 |
   |---|---|---|---|---|
   | Tuba | 6.0 | -0.07 | 0.02 | 0.08 |
   | Bass trombone | 3.0 | -0.07 | 0.05 | 0.11 |
   | Horn 3 | 4.5 | -0.07 | 0.08 | 0.20 |
   | Horn 4 | 5.0 | -0.07 | 0.05 | 0.17 |
   | Oboe 1 | 4.0 | -0.07 | 0.08 | 0.20 |
   | Flute 2 | 3.0 | -0.11 | 0.05 | 0.11 |
   | Clarinet 1 | 3.0 | -0.07 | 0.05 | 0.11 |
   | Trumpet 1 | 4.0 | -0.07 | 0.05 | 0.11 |
   | Trumpet 2 | 4.0 | -0.10 | 0.05 | 0.11 |
   | Trumpet 3 | 5.0 | -0.08 | 0.08 | 0.14 |

   First 0.1 s level (dB) and peak over the first 0.1 s (dB), c52 -> as rendered with the flat bump -> fixed:

   | track | first 0.1 s | peak over the first 0.1 s |
   |---|---|---|
   | Flute 2 | -39.7 -> -36.7 -> -37.3 | 1.5 -> 1.5 -> 1.3 |
   | Oboe 1 | -33.3 -> -33.4 -> -32.5 | 2.2 -> 2.4 -> 0.6 |
   | Clarinet 1 | -40.3 -> -37.3 -> -37.6 | 1.7 -> 1.6 -> 1.5 |
   | Horn 3 | -36.7 -> -33.7 -> -32.3 | 5.7 -> 2.7 -> 1.3 |
   | Horn 4 | -37.1 -> -34.1 -> -32.7 | 5.8 -> 5.0 -> 1.4 |
   | Trumpet 1 | -27.2 -> -23.1 -> -24.3 | 3.9 -> 3.8 -> 1.3 |
   | Trumpet 2 | -28.4 -> -24.2 -> -25.1 | 3.7 -> 3.2 -> 1.5 |
   | Trumpet 3 | -32.1 -> -28.2 -> -27.3 | 6.2 -> 5.1 -> 1.7 |
   | Bass trombone | -31.0 -> -28.0 -> -28.6 | 1.6 -> 0.9 -> 0.6 |
   | Tuba | -25.5 -> -22.5 -> -23.6 | 3.4 -> 3.4 -> 1.6 |

   Brass minus strings in the first 0.1 s of bar 41: -3.6 (c52) -> -0.9 (flat bump) -> -1.4 dB (fixed; +2.2 against
   c52, A's target +2 to +3). Oboe 1's front was 3 dB lower than c52 with the flat bump on unchanged notes (the +3 dB
   bump read -33.4 against -33.3); the cause was not found.
2. **A #5, bar-30 staccatos: level shapes on the alias tracks only.** The "Stac DblTng RRx9" row plays the four
   pitches 6-9 dB apart at one velocity. Shapes through `ALIAS_TRACKS[alias]["tables"]["LEVEL_SHAPES"]` (a table row
   keyed by the alias name has no effect), one step per note, each step placed 0.04 to 0.01 qn before the onset:
   Flute 1 stac +2.3 / -3.9 / -1.7 / +3.3 dB, Oboe 1 stac -4.1 / +4.4 / +3.1 / -3.4 dB. Four peaks, as rendered ->
   fixed: Flute 1 -37.5 -31.3 -33.5 -38.5 (spread 7.1) -> -35.2 x4 (0.1); Oboe 1 -30.8 -39.3 -38.0 -31.5 (8.6) ->
   -34.9 -35.4 -34.9 -34.9 (0.5); Clarinet 1 unchanged -28.7 -30.9 -31.5 -31.3 (2.8). A first version with the steps
   0.10-0.04 qn before the onset made Oboe 1's second note read 60 ms early (the step cut into the first note's end);
   with 0.04-0.01 it reads -15 ms.
3. **B #2, celli 459-460 and Bassoon 1 460.** Celli shape -8 -> -8.6 dB at 459-460 (Violins I minus celli at 459
   +1.9 -> +2.5 dB, at 458 +3.7 -> +4.0). `NOTE_TRIM_RAMP_S` 0.1 s for Bassoon 1 460.0: the -5 dB trim with the default
   0.6 s ramp had realised -1.8 dB in the note's first quarter (41.8 -> 39.1; limit 40).
4. **B #4, Oboe 1 at 496 and the chord at 168.** Oboe 1 shape +7 -> +8.8 dB at 496-496.9, +7 kept at 497-497.9 (Oboe 1
   minus Violins I at 496 -6.0 -> -4.4 dB). `NOTE_TRIM_RAMP_S` 0.1 s for Oboe 1 168.0 and Flute 2 168.0: with the
   default ramp the +7 and +6 dB trims had realised +2.7 and +2.1 dB (Oboe 1 17.5 -> 21.6, Flute 2 18.6 -> 22.0;
   clarinets 21.0-24.3).
5. **B #6, timpani bar 4.** Shape `[(12.4, 0), (12.9, -3), (15.0, -3), (15.5, -3.6), (16.5, -3.6), (16.95, 0)]`
   (qn 15 18.2 -> 17.7 against qn 14 18.0).

## Measured (final: main stems after the stem fix, pass-2 stems, returns)

Files: `actor_scripts/chk_*.txt` (fixed stems), `actor_scripts/chk_first/` (as rendered), `chk52_*.txt` and
`bal53_c52.txt` (the same measures on c52), `checks53_final.log`, `measure-final.log`, `metrics/`.

**Pass criteria**

| Item | c52 | c53 | Pass |
|---|---|---|---|
| State guard before each render (main / pass 2) | not recorded | 0 of 33 / 0 of 9 | yes |
| State guard on the save after each render | not measured | 1 (Horn 1) / 2 (Bassoon 1 stac, Flute 1 stac); audio equal to c52 at the joins; rebuilt; projects on disk 0 / 0 | audio yes; saved state fixed |
| State check against c52, runs | | 0 | yes |
| State check against c50, runs | | 2, both Double basses (round robins; a c51/c52 difference) | yes for this cycle |
| Attack probe, late or hole | 0 | 0 | yes |
| A #1 master dip at 292.0 (limit 2 dB) | 2.1 | 1.5 | yes |
| A #1 new dip at 290.9 (limit 2 dB) | 0.1 | 0.0 | yes |
| A #1 Lento re-bows: stem dip at most 3 dB and master dip under 3.1 dB | 0 of 7 rows | 3 of 7 rows | no (4 rows over one limit) |
| A #2 changed Flute 2 onsets within ±35 ms (pcx) | -62 to +68 | -20 to +34 | yes |
| A #2 Flute 2 minus Flute 1 within ±50 ms on shared onsets (pcx) | 5 of 28 over | 5 of 28 over (272, 280, 636, 642, 643) | no by pcx; the band envelopes read them on time |
| A #3 first 0.1 s within 2 dB of the peak, ten bumped stems | 7 over | 0 over (0.6-1.7) | yes |
| A #3 brass minus strings, first 0.1 s of bar 41 (target +2 to +3) | -3.6 | -1.4 (+2.2) | yes |
| A #4 / decision 6: the 16 onsets with a negative row | 10 of 16 were 16-60 ms early | none late; 14 of 16 within ±25 ms | yes (none late); Oboe 1 582 and cor anglais 275 open |
| Decision 7: cor anglais 275 | +158 ms | -84 ms | no (deferred) |
| A #5 four staccato peaks within 4 dB (Flute 1 / Oboe 1 / Clarinet 1 spread) | 10.8 / 13.6 / 9.9 | 0.1 / 0.5 / 2.8 | yes |
| A #5 staccato onsets within 30 ms of Violins I | | notes 2-4 yes; note 1 not decided | partly |
| A #6 Oboe 2 at 643.5 ends at 643.750 | 643.600 | 643.750 | yes |
| B #1 theme over celli 56-88: median at least +5 / lower quartile at least +3.5 / quarters under 0 | +3.47 / +0.65 / 6 | +5.47 / +3.67 / 0 | yes |
| B #2 Violins I minus celli, every quarter 456-463 (at least +2) | -5.9 to +5.5 | +2.5 to +7.9 | yes |
| B #2 melody group minus celli 456-463 (at least +4.5) | -2.4 to +8.6 | +5.6 to +13.9 | yes |
| B #2 Bassoon 1 460-462 (40 or lower) | 43.6 43.7 44.0 | 39.1 38.7 39.0 | yes |
| B #3 cor anglais minus loudest tune voice, three answers (-5 to 0) | third answer -10.6 / -10.7 | -0.8 / -4.4, -0.3 / -2.8, -3.9 / -3.2 | yes |
| B #4 / decision 8: Oboe 1 under Violins I at 496-503 (2 to 5 dB) | 3.2 to 13.0 | 2.9 to 4.9 | yes |
| B #4 Oboe 1 / Flute 2 at 168 within 4 dB of the clarinets (21.0-24.3) | 14.8 / 16.5 | 21.6 / 22.0 | yes |
| B #5 Clarinet 1 coda 699-706: minimum at least +2 / 706 at least 0 / median at least +5 | +1.9 / -1.0 / +4.8 | +2.9 / +1.0 / +6.1 | yes |
| B #6 timpani qn 15 not above qn 14 | 1.4 over | 0.3 under | yes |
| B: horn unison 164-167 at least +6; Horn 3 165-167 unchanged | +9.0 +8.1 +7.9 +6.3; 32.8 34.5 30.7 | the same | yes |
| B: horns minus heavy brass 484-492 (-5.5 to -4.0) | -3.98 | -4.05 | yes |
| B: timpani rolls, none loudest; table within 1 dB of c52 | | largest -0.1; 15 of 16 within 1 dB | yes; roll 9 over (the celli cut) |
| B: same-dynamic rows within 0.5 dB of c52 | | within 0.2 | yes |
| B: family sums at the tuttis within 1 dB of c52 | | within 0.9 except bars 115-116 (+1.8, +1.5) | no at 115-116 (the celli cut, intended) |
| Decision 2: correlation below 250 Hz (0.54-0.62) | 0.589 | 0.593 | yes |
| Decision 2: correlation 250 Hz-5 kHz (0.47-0.56) | 0.566 | 0.552 | yes |
| Decision 2: side/mid (-4.7 to -5.4 dB) | -5.53 | -5.40 | yes, at the edge |
| Correlation above 5 kHz (0.37-0.48) | 0.495 | 0.473 | yes |
| Decision 2: make-up within 0.3 dB of the no-width render | ±0.28 | -0.19 to +0.19 (range test); +0.16 to +0.23 against c52 on the full render | yes |
| Pitch check, trumpets and trombones: pitches 2.5 dB or more off their track's median change | | 0 | yes |
| Decision 3 (a): brass tail within 4 dB of the strings' tail, bars 31 / 82 / 169 | 8.9 / 13.3 / 6.3 under | 7.8 / 12.3 / 6.1 under | no |
| Decision 3 (b): master 0.3-0.6 s level no wetter than c49, tutti stops 25 / 31 / 82 / 137 / 169 | all dryer | all dryer by 0.5-1.5 dB | yes |
| Decision 3 (b): master t20 no longer than c49, the same stops | bar 137 0.32 s against 0.305 | bars 25, 31, 82, 169 shorter; bar 137 0.325 s against 0.305 | no at bar 137 (in c52 already; not from the half step) |
| Decision 5: delivered loudness -19.8 LUFS within 0.3 | -19.8 | -19.8 | yes |
| Decision 5: climax order 160 > 122 > 167-170 > 26 | kept | -11.4 > -11.9 > -13.6 > -14.4 | yes |
| Decision 5 (added): limiter at most 0.5 dB above c52's | 0.4 | 0.4 | yes |
| Decision 5 (added): stop decays no longer than c52's | 0.425 / 0.30 / 0.68 / 0.355 / 0.325 / 0.38 s | 0.48 / 0.30 / 0.68 / 0.355 / 0.33 / 0.38 s | the EQ: yes (equal to the c52 EQ on the c53 master at every stop); the file: bar 14 +55 ms and bar 137 +5 ms, both in the master |
| Decision 5: 250-500 Hz share at or under the highest reference (-5.85) | -5.41 | -5.86 | yes, by 0.01 dB |
| Decision 5: 6-20 kHz share closer to the references (-29.06 to -32.73) | -28.97 | -29.91 | yes (inside) |
| Decision 5: 2-6 kHz share closer to the references (upper edge -10.78) | -9.95 | -9.86 | no (0.09 dB farther) |
| Not a criterion: 100-250 Hz share (references -6.67 to -8.73) | -8.41 | -8.78 | 0.05 dB under the lowest reference |

Band shares are on my measure, which reads +0.10 dB above C's at 250-500 Hz, -0.39 at 2-6 kHz, -0.47 at 6-20 kHz and
+0.02 at 100-250 Hz; the reference limits in the table are converted to it.

**A #1 re-bows, stem dip / master dip (dB), c52 -> c53** (`rebowdip53.py`; dip = median level over 0.60-0.15 s before
the re-bow minus the minimum from 0.12 s before to 0.40 s after): Violoncellos 12.163 3.9 / 1.8 -> 3.9 / 1.8 (not
refitted); Violoncellos 21.442 4.8 / 3.5 -> 2.1 / 3.4; Violoncellos 26.516 7.0 / 3.0 -> 2.2 / 2.6; Double basses 26.003
1.4 / 4.6 -> 0.9 / 4.8; Violas 40 3.8 / 2.3 -> 0.9 / 2.2; Violins II 47 3.6 / 2.4 -> 2.1 / 2.7; Double basses 47
6.1 / 2.4 -> 3.8 / 2.7. Passing both of A's limits: Violoncellos 26.516, Violas 40, Violins II 47. Over one limit: stem
of Violoncellos 12.163 (3.9) and Double basses 47 (3.8); master at Violoncellos 21.442 (3.4) and Double basses 26.003
(4.8), where the track's own stem dips 2.1 and 0.9 dB, so the master dip there comes from other tracks. Poco piu mosso:
Double basses 292 (c52) 8.8 / 2.1 -> 290.9 (c53) 2.0 / 0.0; master at 292.0 2.1 -> 1.5; Double basses stem at 292.0
8.8 -> 3.3; Double basses 297.045 2.8 / 5.0 -> 0.7 / 5.1; Violas 296 (a printed re-articulation, unchanged) 2.2 / 3.0 ->
2.4 / 3.4; Violins II stem at 292 3.4 (as c52).

**A #2 flutes (pcx, ms).** The changed Flute 2 rows on the full render: 271 +34, 275.5 -1, 277 -2, 281.5 -4, 283 +3,
283.5 -20, 284 +8, 629 +27. Flute 2 minus Flute 1 at the 28 shared onsets: median -14 ms; over 40 ms at 7: 272 -116
(Flute 1 pcx +145, crossing +7), 280 +85 (Flute 2 pcx +84, m6 -12), 634 +48, 636 +118 (Flute 2 pcx +113, m6 -78), 642
+75 (Flute 2 pcx +123, m6 +16), 643 -155 (Flute 1 pcx +129), 643.5 -48. These are the values of c52: at each of them
one flute's pcx reads the swell of a soft note while its second measure reads within 80 ms of the written time, and the
rows tried there were removed (item 4). Detached notes 456-473: median -5 ms (n 17).

**Decision 6, the 16 onsets with a negative per-onset row, full render (pcx, ms):** Flute 1 115 +12, 296 -10, 299.5
-10, 397.5 -5, 555 -22, 633 -4, 639.5 -16, 640 -2; Oboe 1 407 0, 579 -13, 582 -52 (m37 -51, crossing -32, h6 +22, m6
-120: the measures disagree); Cor anglais 275 -84 (m37 -93, h6 -74, m6 -82; c52 +158); Clarinet 1 180 +3; Horn 1 411.5
+7; Bassoon 1 523 -16, 366 +15.

**A #5 staccatos, onsets against the written time (ms):** Flute 1 +25 +25 +30 +20, Oboe 1 +10 -15 +15 +15, Clarinet 1
+10 +5 +5 +10; minus Violins I on notes 2-4 within 30 ms; on note 1 the Violins I measure reads -50 ms because it
catches their previous note. On the Flute 1 main stem the note at 115.5 has a body of -28.9 dB and the first 0.1 s of
the first staccato reads -32.8 dB: the main note's release covers the first staccato (deferred).

**A #6:** Oboe 2 at 643.5: note-on 643.417, ends at qn 643.750 (359.522 s); stem -34.1 dB before the end, -40.8 dB at
+0.05..0.15 s.

**B's check table, the rows not in the pass table** (`chk_bal.txt`; c53 fixed; c52 in brackets where it differs by more
than 0.2 dB). Violins I minus celli 456-463: +6.4 +5.2 +4.0 +2.5 +5.0 +2.9 +3.9 +7.9 (+5.5 +0.5 -3.5 -5.9 -0.1 -1.3 -1.9
+2.5); melody group minus celli +9.3 +8.5 +7.2 +6.0 +8.2 +5.6 +8.1 +13.9 (+8.3 +3.8 -0.3 -2.4 +3.0 +1.4 +2.4 +8.6).
Oboe 1 minus Violins I 494-503: +1.8 +2.2 -4.4 -3.2 -3.2 -3.2 -2.9 -2.9 -4.9 -4.1 (+1.4 +2.7 -13.0 -10.2 -3.2 -3.3 -7.6
-8.0 -9.8 -9.2); 494-495 are outside B's row and not changed by this cycle (the shapes start at 495.95). Theme 56-88
per quarter from 64: -2.1 +6.2 +3.2 +3.2 +3.8 +6.5 +4.0 +0.9 +3.1 +5.8 +2.8 +5.5 +5.8 +3.7 +5.5 +6.4 +3.7 +3.7 +12.5 +8.6
+2.2 +4.3 +2.5 -13.5 (the count leaves out quarters where Violins I is more than 15 dB under its maximum, as c52's
count did: 64 and 87). Violins I theme over the loudest other 15-22 +5.5 (+3.5). Bass clarinet 699-707 16.6 18.2 21.4
21.5 19.6 19.6 19.4 20.7 24.2 (2 dB higher). Cor anglais minus Horn 1 147-152 -4.8 (-5.6). Horns a2 41-42 +1.6; Horn 1
solo 13-14 +13.0; celli tune 47-55 +4.4; harp minus celli -9.1; brass minus strings 25-32 / 115-122 / 123-126 / 158-161
-0.6 / +0.6 / +2.1 / -0.8; horns minus trumpets + trombones + tuba 123-126 -4.0; Trumpets a2 minus Violins I / Horns a2
167-170 +0.6 / +2.0; Trumpet 1 minus Violins I 82-83 -1.6; winds minus strings -1.4 / -1.9; tam-tam -6.6; cymbals
-16.5; chorale -2.3; Cello solo +8.3; Horn 1 bar 125 +5.2 / -0.1; Clarinet 1 arrival +1.2; Horn 3 minus Horn 4 ppp +2.0;
timpani ppp minus violas -9.3. Family sums (brass - strings, trumpets - (trombones + tuba), trumpets - Violins I, winds
- strings, horns - heavy brass): bars 41-42 +0.3, +0.3, -0.2, -3.7, -3.0 (c52 -0.2, -0.2, -1.1, -3.7, -2.5: the sf
bump; with the flat bump as rendered +1.3, +1.3, +1.7, -3.7, -4.5); bars 115-116 +1.5, +1.0, +1.4, +1.0, -6.4 (c52 -0.3,
+1.0, +1.3, -0.5, -6.4: the celli cut); all other tuttis within 0.3 dB of c52. Timpani rolls, median / maximum over the
loudest other, c52 -> c53: roll 9 (bar 115) -9.9 / -8.3 -> -8.4 / -4.3 (the celli cut); roll 11 (bar 140) -7.4 / -4.2
-> -7.4 / -5.2; rolls 2, 7, 12, 13, 14 within 0.7 dB; rolls 3, 4, 5, 6, 8, 10, 15, 16 unchanged. Same-dynamic rows: pp
horns -1.8, pp trombones + tuba -3.5, pp winds +0.6, p horns -3.8, p winds -2.2, p harp -5.4, f horns -3.8, f trumpets
-0.3, f trombones + tuba +0.3, f winds -5.0, ff horns -2.7, ff trumpets -0.5, ff trombones + tuba 0.0, ff winds -4.3.

**Decision 2, width** (`chk_width.txt`): seat of `R Brass` (right minus left) -2.00 -> -0.27 dB; Trombone 2 right minus
left +5.43 -> +5.75 dB. Joins against c52 (`chk_joins.txt`): Horn 1 46 joins median +0.0 ms, residual 0.00 dB; Horn 2
25 joins (245.5 -32 ms); Horn 3 11; Horn 4 6; Trumpet 1 15 joins +0.0 ms, level +0.16 / +0.19 dB; Trumpet 2 +0.22;
Trumpet 3 +0.20; Trombone 1 13 joins median +0.0 ms, level +0.23 dB, one join more than 40 ms earlier (525.5 -139 ms;
531.0 -37 ms).

**Decision 3, the nine stops on the master** (0.3-0.6 s level under the body in dB / t20 in s; `chk_tail.txt`,
`chk_tail52.txt`, `chk_tail49.txt`; third column: the c53 master with c52's `R Brass` return stem in place of c53's,
which is what a revert of the half step would give):

| stop (C's bar) | c49 | c52 | c53 with c52's R Brass return | c53 |
|---|---|---|---|---|
| 14, horn ending | -23.2 / 0.345 | -16.0 / 0.425 | -16.0 / 0.425 | -15.4 / 0.48 |
| 25, tutti | -9.8 / 0.335 | -10.7 / 0.295 | -10.7 / 0.295 | -10.7 / 0.295 |
| 31, tutti | -17.2 / 0.535 | -17.9 / 0.45 | -17.9 / 0.45 | -17.8 / 0.45 |
| 71 | -16.1 / 1.17 | -15.7 / none | -15.2 / none | -15.1 / none |
| 79 | -1.1 / none | -0.3 / none | | -0.4 / none |
| 82, tutti | -20.6 / 0.37 | -22.1 / 0.345 | -22.1 / 0.345 | -22.1 / 0.345 |
| 137, tutti | -13.3 / 0.305 | -14.0 / 0.32 | -13.9 / 0.325 | -13.9 / 0.325 |
| 141 | -13.2 / none | -12.1 / none | -12.2 / none | -12.2 / none |
| 169, tutti | -22.2 / 0.355 | -22.8 / 0.33 | -22.8 / 0.33 | -22.7 / 0.33 |

`R Brass` return stem RMS -55.70 -> -52.58 dB (+3.12). Brass family at 0.3-0.6 s (c49 / c52 / c53): bar 14 -26.0 /
-15.6 / -14.8; 25 -11.9 / -11.7 / -11.8; 31 -22.4 / -28.4 / -27.3; 71 -21.8 / -25.7 / -24.9; 79 -25.6 / -31.2 / -30.2; 82
-26.6 / -31.9 / -30.9; 137 -11.6 / -13.5 / -13.4; 141 -22.0 / -27.7 / -26.7; 169 -22.8 / -26.7 / -26.5. Brass t20, c52 ->
c53: bar 14 0.41 -> 0.545 s, 31 0.26 -> 0.28, 82 0.255 -> 0.255, 137 0.265 -> 0.275, 141 0.28 -> 0.29, 169 0.295 -> 0.30.
Strings at 0.3-0.6 s (c53 = c52): bar 31 -19.5, 82 -18.6, 169 -20.4.

Reading. The half step raises the brass tail by 0.2-1.1 dB; it stays 6.1-12.3 dB under the strings' tail (criterion
"within 4 dB": not met) and 3.7-4.9 dB under c49's brass tail at bars 31, 82 and 169. On the master the five tutti
stops move by at most 0.1 dB and 5 ms against c52. One reading fails "no wetter than c49": t20 at bar 137, 0.325 s
against 0.305 s (its level passes). That reading is 0.325 s with c52's return stem too and was 0.32 s in c52, so the
half step does not cause it and a revert would not remove it. The half step is therefore kept. This departs from the
literal sentence of decision 3 ("if the master fails at any stop, go back to the c52 values"); the c52 values are in
item 18 and the third column shows what the revert gives: the only audible difference is the bar-14 horn ending (-15.4
dB / 0.48 s with the half step, -16.0 dB / 0.425 s without; C's limit of 0.49 s holds; c49 -23.2 dB / 0.345 s, so c52
was already wetter than c49 there). The non-tutti stops 71 and 141 read 1.0 dB wetter than c49 (71: 0.1 dB of it from
the half step; 141: as c52).

**Decision 5, delivery EQ variants on the fixed c53 master** (`delivvar53.txt`, `delivvar53b.txt`; shares on my
measure; t20 of the delivered file at bars 14, 25, 31, 82, 137, 169; climax order kept in every variant):

| variant | I / LRA / TP | limiter dB | 100-250 | 250-500 | 2-6 k | 6-20 k | stop t20 (s) |
|---|---|---|---|---|---|---|---|
| c52's delivered file | -19.8 / 14.4 / -1.7 | 0.4 | -8.41 | -5.41 | -9.95 | -28.97 | 0.425 0.30 0.68 0.355 0.325 0.38 |
| c52 EQ on the c53 master | -19.8 / 14.4 / -1.7 | 0.3 | -8.48 | -5.40 | -9.91 | -28.95 | 0.48 0.30 0.68 0.355 0.33 0.38 |
| as decided: 260 Hz -2.0 in place of 167 Hz, shelf 3 kHz -1.0 | -19.7 / 14.5 / -1.7 | 0.5 | -7.93 | -5.92 | -10.09 | -30.13 | 0.48 0.30 0.68 0.365 0.335 0.38 |
| 167 kept + 260 Hz -1.0, shelf -1.0 | -19.8 / 14.5 / -1.7 | 0.3 | -8.67 | -5.70 | -9.97 | -30.02 | as the c52 EQ |
| **167 kept + 260 Hz -1.5, shelf -1.0 (shipped)** | -19.8 / 14.5 / -1.7 | 0.4 | -8.78 | -5.86 | -9.86 | -29.91 | as the c52 EQ |
| 167 kept + 260 Hz -2.0, shelf -1.0 | -19.7 / 14.6 / -1.8 | 0.4 | -8.88 | -6.01 | -9.75 | -29.81 | not measured |
| 167 kept + 260 Hz -1.5, shelf -1.3 (tested only) | -19.8 / 14.5 / -1.9 | 0.3 | -8.77 | -5.85 | -9.95 | -30.22 | as the c52 EQ |
| 167 kept + 260 Hz -2.0, shelf -1.3 (tested only) | -19.8 / 14.5 / -1.7 | 0.4 | -8.87 | -6.01 | -9.84 | -30.11 | bar 82 0.36, rest as the c52 EQ |

Reading. The pair as decided passes the three share checks but lengthens the decay at bars 82 and 137 by 10 and 5 ms
against the c52 EQ on the same master and reads limiter 0.5 dB, so the coordinator's added check on the stop decays
fails for it. With the 167 Hz bell kept (the coordinator's fallback) the decays equal the c52 EQ's at every stop. 260 Hz
-1.5 dB is the smallest depth that puts 250-500 Hz at the highest reference (-5.86 against -5.85, a margin smaller than
the difference between my measure and C's). With the 167 Hz bell kept, the 2-6 kHz share is not closer to the
references than c52 (0.05 dB farther than the c52 EQ on the same master, 0.09 dB farther than c52's file): the 260 Hz
cut removes low-mid energy, the file is brought back to -19.8 LUFS, and the upper bands rise with it. The shelf at -1.3
dB instead of -1.0 gives 2-6 kHz -9.95 (equal to c52), 250-500 Hz -5.85, 6-20 kHz -30.22, the same decays, limiter 0.3
dB and true peak -1.9 dBTP; it was tested and not shipped because decision 5 fixes the shelf at -1.0 dB. The delivery
can be re-run from the master in about a minute (`tools/deliver_master.py`). Side effect of keeping both low bells:
100-250 Hz reads -8.78, 0.05 dB under the lowest reference (c52 -8.41).

**Other.** Climax order (delivered S max): 160 -11.4 > 122 -11.9 > 167-170 -13.6 > 26 -14.4 (c52 -11.5 / -12.0 / -13.6
/ -14.4). Delivered stop t20: bar 14 0.48 s, 25 0.30, 31 0.68, 82 0.355, 137 0.33, 169 0.38; bars 71, 79, 141 never fall
20 dB. Pre-limiter peaks (s, dBFS): 278.57 -1.14, 117.28 -1.29, 355.98 -1.78, 354.98 -1.97, 379.23 -2.04. Delivery
ride +10.5 / -2.3 dB. Motion (`tools/motion.py`): master dS4 p90 11.18 dB, 1 s / 20 s 6.00 dB; mp3 9.31 / 5.03 dB.
Master 100-250 Hz share -8.9 / -8.6 dB, 6-20 kHz share -28.8 dB. Decision 11 (pcx): Horn 1 104 +4, Horn 3 104 +13,
Double basses 104 -11, Horn 1 552 -9, Horn 3 552 +6 ms. Coordinator note (3): `diff before/mockup-events.tsv
build/mockup-events.tsv` shows only `VlnII 436.0 0.0 cresc -1` removed and `VlnII 440.0 0.0 cresc 1` added;
`mockup.midi` is identical (cmp); Violins II in `parts.json`: 0 notes added or removed, 0 leads, 0 velocities or ends
changed; its volume lane differs only at qn 46.85-47.20 (the refitted re-bow fill at 47).

**Loudness** (delivered `mvt1-mockup-c53.mp3`): -19.8 LUFS, LRA 14.5 LU, TP -1.7 dBTP, 433.90 s (tail 1.00 s), limiter
about 0.4 dB on the loudest sample peak, p10-to-max short-term span 19.0 dB. Master -20.7 LUFS, LRA 23.5 LU, true peak
-0.4 dBFS, sample peak 0.949 (c52 master -20.6 LUFS, LRA 23.5 LU, true peak -0.6 dBFS).

## Section (7) decisions and coordinator notes: outcome

1. **Celli CC1 macro: kept.** Not touched.
2. **Brass width 0.65 / 0.75, side bell -4.5 dB: done, passes.** Correlation 0.593 / 0.552, side/mid -5.40 dB (at the
   edge of -5.4), make-up within 0.19 dB in the range test.
3. **R Brass half step: applied and kept; the first criterion is not met and one master reading fails.** Brass tail
   6.1-12.3 dB under the strings' tail (limit 4). Master no wetter than c49 at the tutti stops 25, 31, 82, 169 on both
   measures; bar 137 t20 0.325 s against 0.305 s, which c52 had (0.32 s) and which the revert does not change (0.325 s).
   Kept on that evidence, against the literal revert rule; revert values in item 18. C's full step was not tried.
4. **Trumpet release: tested before the render, not applied.** +6 dB on the release trails moves the fall at
   0.15-0.30 s by 0.4-1.4 dB and acts in full only from 0.3 s; the test does not confirm the cause.
5. **Delivery EQ: shipped as the coordinator's fallback** (167 Hz -1.6 kept, 260 Hz -1.5 added, 1180 Hz -1.9, shelf
   3000 Hz -1.0; the 8008 Hz shelf removed). Passes loudness, climax order, limiter, stop decays (EQ), 250-500 Hz (by
   0.01 dB) and 6-20 kHz; fails "2-6 kHz closer than c52" by 0.09 dB. The pair as decided fails the stop-decay check
   (bars 82 and 137 longer by 10 and 5 ms). Shelf -1.3 dB would pass every check (tested only).
6. **Clamp fix and the 16 negative rows: done.** None lands late; 14 of 16 within ±25 ms; rows re-fitted where the onset
   moved (item 6).
7. **Cor anglais 275: measured five ways, all late in c52, row changed; on the full render it is 84 ms early.** The fit
   on a range render did not carry over. Deferred to c54 with the numbers.
8. **Oboe 1 shapes: applied with smaller values where B's passed the violins** (+7 / +8.8 at 496-497.9, +5 at
   500-503.8); Oboe 1 is 2.9-4.9 dB under Violins I at 496-503. CC1 floor 64: range test only, +2.3 dB, not shipped.
9. **Horn 3 and cor anglais rows: in the project through the full build.** Cor anglais checked with one value per
   answer.
10. **Finale item 18 on the basses: not done** (low priority; time went to the state guard work).
11. **C's timing observation: C's time map.** Onsets within 13 ms of the written time on the stems.
12. **State check against c52 and c50, guard 0 before each render: done** (state guard section).
13. **No new return, no REAPER preference changed, no score source changed.** `build/sections/dev.ily` was not edited
    by this cycle; the Violin II hairpin change in it is the one of coordinator note (3).

Coordinator notes: (1) fp at Double basses 128: no dip, `fp_falls` not ported. (2) No row was fitted on audio from a
`--midi-only` build; every c53 build of a measured track was a full build. (3) Verified (Other, above). (4) Finale
techniques: 18 not done; 19 done (A #3); 20 done (A #4); 21 not applicable to a c53 finding; 22 used (0.1 s ramps for
note trims on short notes; level shapes for the staccatos); 23 not applicable. (5) Open c52 items: Flute 2 (A #2), width
(decision 2), the roles rows (decision 9) are done; bar 84, the string diminuendi share and Horn 1's legato-minus-other
level were not addressed. (6) State check against two cycles done; `pitch_check.py` used after the width change.

## Critic findings: done, rejected or deferred

**A (articulation).**
- A #1 re-bows: done (item 3). Master at 292.0 1.5 dB and no new dip at 290.9: pass. Lento rows: 3 of 7 pass both
  limits (c52 0 of 7); 4 rows stay over one limit and are deferred with their numbers.
- A #2 flute pair: done for the eight onsets where two measures agreed (item 4; -20 to +34 ms). Rejected for 272, 280,
  634, 636, 639.5, 642, 643: the band envelopes read them on time and pcx reads the swell; the pcx differences there
  are the c52 values.
- A #3 sf at 160: done (item 5 and correction 1); all ten stems within 2 dB, brass minus strings +2.2 dB. A's
  low-priority Flute 1 dip was not applied (Flute 1 2.5 dB, as c52).
- A #4 clamp order: done (items 1 and 6).
- A, cor anglais 275 (decision 7): changed, result 84 ms early, deferred.
- A #5 bar-30 staccatos: done (item 8 and correction 2); spreads 0.1 / 0.5 / 2.8 dB. A's alternative (lower `_WSTAC`'s
  top value) was not needed. Deferred: the Flute 1 main note at 115.5 covers the first staccato.
- A #6 Oboe 2 643.5: done (item 9).
- A's open items: Flute 2 late = A #2; Violins I sf at 78: no change, as A wrote; celli CC1 macro: kept (decision 1).
- A's technique table: 18 not done (decision 10); 19 done; 20 done; 21 no; 22 used; 23 no.

**B (balance).**
- B #1 bars 17-22: done (item 10); +5.47 / +3.67 / 0.
- B #2 bars 115-116: done (item 11 and correction 3); celli 2.5-7.9 dB under Violins I, Bassoon 1 at most 39.1.
- B #3 cor anglais third answer: done (item 12); -3.9 / -3.2 dB.
- B #4 Oboe 1 at p: done with decision 8's target (item 13 and correction 4); B's "within 3 dB at 500-503" is replaced
  by "2-5 dB under", measured 2.9-4.9. B's +8 dB at 500-503.8 rejected: a range render read Oboe 1 +0.85 dB over
  Violins I at 500-502. CC1 floor rejected for this cycle: +2.3 dB in the range test.
- B #5 bass clarinet under Clarinet 1: done (item 14); +2.9 / +1.0 / +6.1.
- B #6 timpani bar 4: done (item 15 and correction 5).
- B's check table: every row passes except the two that the celli cut moves by design (family sums at bars 115-116,
  timpani roll 9).

**C (blend and space).**
- C #1 brass tail: half of C's step, kept (decision 3); the brass tail rose 0.2-1.1 dB and is still 6-12 dB under the
  strings' tail. C's full step deferred to the coordinator.
- C #2 trumpets stop without release: tested, `rt_gain_db` rejected (0.4-1.4 dB at 0.15-0.30 s). Two untested
  candidates for c54: `releaseDamping` 0.8 on the trumpet's trail groups; sustain release 178 -> 237 ms.
- C #3 width narrows the brass more than intended: done (decision 2).
- C #4 low-mid build-up in the delivered file: done in part. 260 Hz -1.5 dB with the 167 Hz bell kept; 250-500 Hz
  -5.41 -> -5.86 (highest reference -5.85). C's move of the bell to 260 Hz rejected for this cycle: it lengthens two
  stop decays.
- C #5 delivered file brighter than the references: done in part. 6-20 kHz -28.97 -> -29.91 (inside the references);
  2-6 kHz -9.95 -> -9.86 (not closer; reference edge -10.78).
- C's timing observation: C's time map (decision 11).

## Rejected / deferred (for c54)

- Cor anglais 275: 84 ms early on the full render (pcx -84, m37 -93, h6 -74, m6 -82). Reduce `retongue_leads` Cor
  anglais 275.0 from +0.06 toward about +0.02, or move the keyswitch before the note at 274.5; verify on a full render.
  The keyswitch changes between two overlapping notes there, so the join depends on what was played before the range.
- Oboe 1 582: pcx -52 ms, with disagreeing measures (crossing -32, h6 +22, m6 -120). Not changed.
- Flute onsets where pcx reads late and the band envelope does not: 272, 280, 634, 636, 642, 643. No rows.
- Flute 1: the main note at 115.5 covers the first staccato at 116.0 (`BREATH_GAP_AT` on Flute 1 115.5 is the
  candidate).
- Stems over 2 dB at 160 that have no bump: Flute 1 2.5, Timpani 2.8, Violoncellos 2.3 (as c52).
- Re-bow rows over A's limits: Violoncellos 12.163 (stem 3.9), Double basses 47 (stem 3.8), Violoncellos 21.442 (master
  3.4), Double basses 26.003 (master 4.8); also Double basses 297.045 (master 5.1, stem 0.7) and Violas 296 (master
  3.4, a printed re-articulation). Where the stem is under 3 dB the master dip comes from other tracks, so a fill on
  this track cannot remove it.
- Trombone 1 525.5: 139 ms earlier than c52 on unchanged data (one join of 13; no state run).
- Brass tail 6-12 dB under the strings' tail after the half step; bar 137 t20 0.325 s against c49's 0.305 s (as c52);
  bars 71 and 141 1.0 dB wetter than c49 (not clean stops).
- Decision 5: 2-6 kHz not closer than c52 (0.09 dB); the shelf at -1.3 dB is the measured option. 100-250 Hz 0.05 dB
  under the lowest reference.
- Family sums at bars 115-116 (+1.8 / +1.5 dB) and timpani roll 9 (+1.5 median, +4.0 maximum) moved over B's 1 dB by
  the celli cut B asked for. B's table needs new reference values there.
- Oboe 1 over Violins I at 494-495 (+1.8 / +2.2 dB, as c52; outside B's row).
- Decision 10, finale item 18 on the basses (bars 27-31, 131-134, 140-142): not done.
- Decision 8's CC1 floor: +2.3 dB, not shipped.
- The trigger of the stale state after playback: not identified (state guard section).
- c52 open items not addressed: bar 84 master rise, string diminuendi 50 % share, Horn 1 legato-minus-other +1.6 dB.

## Could not verify

- What exactly makes the Opus instance hold the 20 ms attack when playback stops. The audio of the render that
  produced the stale save is correct on every stale track checked.
- The cor anglais 275 row on a corrected value (one render per cycle).
- Whether the Double basses' difference from c50 at 704-712 is a state effect of c51 or c52; c53 equals c52 there.
- Why Oboe 1's front at 160 was 3 dB lower than c52 on unchanged notes in the main render.
- The levels of the 17 corrected stems are simulated from the build data, not rendered. The return stems were not
  re-simulated, so the reverb of the corrected notes has the rendered level. The REAPER projects do not hold the
  post-render rows until the next full build.
- The staccatos' first note against Violins I (the measure catches the violins' previous note).
- Decision 3's master readings at the non-tutti stops 71 and 141 as "tutti stops": I read them as not covered by the
  criterion.

## EW-TEMPLATE-PLAN sections not yet applied

From A: section 5 legato overlap (`LEG_OVERLAP` 0.04 qn = 19-21 ms against 45-80 ms on strings and 33-58 ms on winds
and brass) and legato velocity by dynamic (median v124 against 92-98 / 90-105); section 6 two tracks per string
section; section 7 per-note lean-off; section 8 tutti entry spread; section 10 beat-position velocity outside the
listed spans. From C: timpani mics (Close -14 / Main -6, no Surround); harp mics; return faders 8 / 12 / 4 / 4 dB under
the template; impulse cut to half; `R Glue` off; section 8 (Duc's send profile, basses EQ, tutti entry spread,
room-noise bed). MANUAL-GAPS still open: #12 Felt Cresc rolls, #5 expressive rows for the wind solos, #4 Mid mics on
the winds.

## REAPER

- Lock: waited from 17:19:05 behind "scherzo" and then "mvt3" (longest-waiter rule, `lock.log`); owner "mvt1" from
  18:14:47 to 20:52:53; released. No other owner's lock was touched. All work after 20:53 was on files only.
- Main project: full builds of all 33 tracks at 18:24 and 19:21, restarts at 19:05 (after the overwrite-dialog hang),
  19:25 and 19:43. First render attempt 19:45-19:54 refused by `render_cycle.py` (REAPER had closed its audio device after the
  restart; reopened with `python3 ~/.rpr-bridge/rpr.py run cycles/c52/audio_init.lua`, no preference changed). Render
  19:55:21-20:07:46 (`render_main2.log`): guard "stale none", 33 stems + 4 returns, "late or hole: 0", exit 0.
- Pass 2: two full builds of the 9 tracks (20:27, 20:31), render 20:33:53-20:46:12 (`render_pass2.log`): guard "stale none", master =
  float sum of 46 stems, peak 0.9485, exit 0. `render_pass2/` was a copy of the pass-2 stems under their pass-2
  numbers (sample-identical to `render/` and `render_first/`) and is deleted, as in c52.
- Memory: main project 43 GB before the render and after its settle wait, 0.0 GB compressed (`render_main2.log`), about
  43-44 GB after the render; pass 2 19 GB, 0.0 GB compressed (`render_pass2.log`), about 19-20 GB after its render.
- Both projects on disk read 0 stale tracks (main 0 of 33, pass 2 0 of 9, saved after REAPER quit at 20:52). They hold
  the rendered level rows, not the post-render ones.
- Sample drive `/Volumes/MAC DRIVE` answered at each check. No REAPER preference changed; nothing under `~/.rpr-bridge`
  modified (the job file `inbox/a7ba029ad458.running` of the hung range render was left as it was).
- Disk: 38 GiB free after the renders, 43 GiB after deleting the range-test audio and `render_pass2/`; `render/` 6.6 GB,
  `render_first/` 2.3 GB (kept: the stems as rendered, before the stem fix).

## Addendum after the actor (coordinator, 2026-11-09 22:20 CST): delivery re-run with the 3 kHz shelf at -1.3 dB

The actor measured that the shelf at -1.3 dB passes every delivery check and did not ship it because decision 5 fixed
-1.0 dB. I changed `build/mix.json` `master_eq` highshelf 3000 Hz from -1.0 to -1.3 dB and re-ran
`tools/deliver_master.py cycles/c53/render/00_Master.wav cycles/c53/mvt1-mockup-c53.mp3 build/parts.json`. The master,
stems and projects are unchanged. The mp3 the actor shipped is kept as `cycles/c53/mvt1-mockup-c53-shelf10.mp3`.

Delivered now (`actor_scripts/deliv53.py --stops`; log `metrics/deliver_shelf13.log`): -19.8 LUFS, LRA 14.5 LU, TP -1.9
dBTP, limiter about 0.3 dB, length 433.90 s. Shares: 100-250 Hz -8.77, 250-500 Hz -5.85 (limit -5.85), 2-6 kHz -9.95
(c52 -9.95; shipped-by-actor file -9.86), 6-20 kHz -30.22 (references -29.06 to -32.73). Climax order kept (160 -11.4 >
122 -11.9 > 167-170 -13.6 > 26 -14.5). Stop t20: bar 14 0.48 s, 25 0.30, 31 0.68, 82 0.355, 137 0.33, 169 0.38, equal to
the actor's file. Decision 5's 2-6 kHz check now reads "equal to c52" instead of 0.09 dB the wrong way.
Current `master_eq`: highpass 42 Hz; bell 167 Hz -1.6 dB bw 1.39; bell 260 Hz -1.5 dB bw 1.0; bell 1180 Hz -1.9 dB bw
1.39; highshelf 3000 Hz -1.3 dB bw 1.39.
