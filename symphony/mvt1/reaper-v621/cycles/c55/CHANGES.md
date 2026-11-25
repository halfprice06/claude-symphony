# Cycle 55: changes (actor)

Render: `cycles/c55/render/` (main pass, then pass 2; Violoncellos and Cor anglais carry a level fix, originals in
`render_first/`). Delivered: `cycles/c55/mvt1-mockup-c55.mp3`. Data as rendered: `cycles/c55/rendered_build/`; the
current `build/` adds the three stem-fix rows. Measures: `cycles/c55/post_final.txt` (`actor_scripts/post55.sh`).

## Priority 1: the theme's long notes were a stab followed by a body 8-15 dB lower

### Before / after (full renders, each on its own data; `actor_scripts/long55.py` = critic A's measures, `p1q55.py` = critic B's scale, S = `theme_S55.py`)

| | c53 | c54 | c55 | target |
|---|---|---|---|---|
| Violins I 56-127, 33 notes of a quarter or longer: front minus tail, median | 2.8 dB | 9.7 | 1.9 | under 4 |
| the same: sounding under 60 % of the length | 1 | 13 | 1 | at most 2 |
| the same: next note's front minus this tail over 6 dB | 2 of 29 | 21 of 29 | 1 of 29 | at most 3 |
| Violins I 56-127: front minus body, accented / unaccented long notes | 3.8 / 0.9 | 11.2 / 4.7 | 2.8 / -0.2 | 2-5 accented |
| Violins I 536-576 (22): front minus tail / under 60 % / steps over 6 dB | | 7.7 / 4 / 11 of 20 | 1.6 / 0 / 2 of 20 | |
| Violins II 104-127 (10) | | 6.9 / 2 / 5 of 9 | 2.3 / 1 / 1 of 9 | |
| Violins II 552-576 (8) | | 9.4 / 3 / 4 of 6 | 1.8 / 0 / 1 of 6 | |
| Violas 104-127 (10) | | 4.4 / 0 / 1 of 9 | 1.4 / 0 / 0 of 9 | |
| Violoncellos 520-536 (6) | | 4.2 / 3 / 2 of 5 | 0.3 / 1 / 0 of 5 | |
| Violins I minus celli 56-88 per quarter: median / lower quartile / under +3 / under 0 | +6.33 / +4.07 / 5 / 2 | +6.47 / +3.01 / 8 / 3 | +6.30 / +4.95 / 6 / 0 | lower quartile +3.9 or more |
| bar 138, Violins I minus Violins II at 549, 550 | +0.4, -3.2 | -9.3, -9.1 | -0.3, +0.1 | within 3 |
| bar 26, Violins I minus Violins II at 101 | +1.7 | -2.8 | +1.9 | |
| S Violins I 56-87.9 (39): median / robust SD / over 40 ms from the median | +3 / 40 / 13 | +2 / 6 / 1 | +6 / 9 / 2 | robust SD under 15, at most 1 over 40 |
| S Violins I 56-127 (79) | | +2 / 9 / 2 | +6 / 10 / 2 | |
| S Violins I 536-576 (38) | | 0 / 12 / 3 | +2 / 14 / 2 | |
| S Violins II 104-127 / 552-576 | | +4 / 16 / 1; -1 / 16 / 1 | +5 / 16 / 0; +2 / 15 / 1 | |
| S Violas 104-127 | | 0 / 15 / 1 | +7 / 12 / 2 | |
| S Violoncellos 520-536 (19) | | +2 / 28 / 5 | +4 / 24 / 5 | fails as in c54 |
| join holes Violins I 56-127: slurred / bow change, median | 3.7 / 5.3 dB | 4.4 / 5.7 | 4.9 / about 8 (against the lifted body) | |

S "at most 1 note over 40 ms" is missed by one note on Violins I 56-87.9 (72.5 reads +55 ms, c54 -6; pcX only, the note
before a lifted accent; no note-on moved). Over the 79 notes of 56-127 the S change against c54 has a median of 0 ms
on the 30 lifted notes and 0 ms on the other 49; 5 notes moved more than 15 ms (72.5, 73, 108, 112.5, 119.5).

### What was changed
a. `STEADY_LINE` `own_front` (tools/score_to_parts.py): notes of the spans on a row named "...Marc..." take no accent
   swell, no fitted accent (build/accent_fits.json swell and step trim) and no accent body cut. On its own (simulated on
   the c54 stems): Violins I 56-127 front minus tail 9.7 -> 7.8 dB.
b. Cure shipped: the per-note body lift on the Marc row (`body_db`, `tail_db`, `body_off_s`; `build/steady_body55.json`,
   body rows Violins I 49, Violins II 13, Violas 2, celli 2; tail rows 25, 9, 3, 3; fitted by `actor_scripts/fit55.py` on the c54 stems through the
   lane difference, then checked on range renders), and notes of a quarter or longer end at the next note-on
   (`C55_LONGEND`, per-onset `end_s` 0.0).
c. `build/steady_levels54.json` refitted on the simulated stems with `actor_scripts/levels55.py` (front steps; the body
   window is printed beside them): front residual SD 56-88 1.2, 88-104 0.4, 104-128 0.9, 536-552 0.3, 552-576 0.9 dB
   (Violins I), Violins II 1.2 / 0.9, Violas 1.3, celli 1.4. Celli 526: the accent shapes are gone with (a); its level
   step +2.5 after the render (accent 3.4 dB over its neighbours, c54 2.9).
d. Slur test, not adopted (below).

### Range test, Violins I bars 15-22 (39 notes, qn 55.5-90), each variant rendered three times, the first discarded, the pair identical in every case

| variant | S median / robust SD / over 40 ms | front minus tail | under 60 % | steps over 6 dB | holes slurred / bow change |
|---|---|---|---|---|---|
| base (c54 data) | 0 / 9 / 1 | 12.1 dB | 7 of 10 | 6 of 8 | 4.0 / 5.4 dB |
| lift (lift ends 0 / 0.03 s after the next note-on) | +2 / 9 / 2 | 3.5 | 1 | 0 | 4.4 / 10.2 |
| liftb (0.02 / 0.06 s) | +3 / 7 / 2 | 3.2 | 1 | 0 | 4.4 / 9.5 |
| liftc = liftb + long notes end at the next note-on (shipped) | +8 / 9 / 2 | 2.7 | 1 | 0 | 4.3 / 8.2 |
| susmax (1.5 qn or longer on Sus MAX, keyswitch 0.15 s early, lead 60 ms) | +4 / 10 / 8 (max +156) | 7.9 | 0 | 2 | 4.7 / 10.6 |
| vel (long notes at velocity 45) | 0 / 9 / 3 | 10.6 | 6 | 2 | 4.4 / 9.4 |
| slur1 (lift + overlap 0.04 s on slurred notes) | +6 / 12 / 2 | 3.4 | 1 | 0 | 4.1 / 10.2 |
| slur2 (slur1 + velocity 60 on slurred targets) | +2 / 12 / 2, 1 note unread | 4.1 | 2 | 0 | 3.1 / 10.3; 10 of 36 neighbour body steps over 6 dB |

Cure (ii) (Sus MAX for long notes) lost on both counts without a lead refit; (d) is not adopted: the overlap alone gains
0.3 dB, and with velocity 60 the eighths' levels break and S robust SD goes 9 -> 12 ms. Slurred and bow-change holes
already differ by 3-4 dB in the shipped state.

## Coordinator decisions

| # | Decision | Done | Measured on the c55 render |
|---|---|---|---|
| 1 | Tempo map | yes (`_C55_FLAT`, BEAT_STRETCH 284 / 285 deleted, six second-theme arcs "sub" with APEX_SKIP) | parts.json tempo is the printed tempo on every beat of 128-176, 270-448, 464-480, 664-679; 184-244 and 584-620 slow only the last two beats of a phrase (x0.98, x0.95) and take the first beat of the next at x0.97; duration 424.18 -> 424.02 s. Breath gaps: all 18 are equal in ms on the c53, c54 and c55 maps. Re-bow pieces that changed length: Violins II 188 (+32 ms) and 208 (+16 ms) only; none in bars 15-32 or 131-144 on either map |
| 2 | One row on fast marked lines | part: Violins I 128.4-158 shipped with (a)-(c) (per-onset rows, steps matched note by note to the c54 render with `match55.py`, 6 body lifts) | S robust SD 33 -> 15 ms, over 40 ms 5 -> 2; front minus tail 3.5 -> 2.9 dB, 0 under 60 %. Not shipped: Violins I / II 448-480 and the development 304-384 (range test before any fit: Violins I 304-384 robust SD 30 -> 15, Violas 47 -> 34, celli 36 -> 26, Violins I 448-480 34 -> 27, Violins II 448-480 32 -> 57): their long notes carry hairpins and the lift fit would flatten a printed diminuendo. Violas 438.0: Sus MAX with 0.09 s lead (SHORT_SUS_AT), not measured |
| 3 | Lyrical lines | range test only, celli 184-204 (15 notes), first pass with one lead per class | as played S robust SD 43 ms, slurred holes 4.8 dB; Leg Slur MAX only 71 ms / 3.1 dB (6 notes kept Leg BC through another rule); Sus MAX + 0.06 s overlap 46 ms / 2.2 dB; Sus Marc LITE 27 ms / 1.3 dB but front minus tail 6.4 dB with 3 of 11 under 60 %. None meets "under 25 ms, none over 60"; nothing shipped. Violas / celli 584-636 and Violins I 636-664 not tested |
| 4 | Winds | reduced form: 36 per-onset rows from S on the c54 render (`windrows55.py`: both estimators of one sign, moved by the smaller; entries on pcX), rows that a rule absorbed moved to retongue_leads.json. No per-track row lead, no pitch-pair table | S robust SD / over 40 ms, c54 -> c55: Clarinet 1 520-536 14 / 4 -> 9 / 1; Bassoon 1 15 / 3 -> 12 / 2; Trombone 1 30 / 6 -> 16 / 2; Oboe 1 88-104 32 / 6 -> 27 / 3; Oboe 1 536-552 37 / 4 -> 16 / 1; cor anglais 272-284 18 / 5 -> 8 / 1 (275: S +42 -> within the line). Spread per onset between the four lines of 131-134 not re-measured |
| 5 | B #2 bar 30 staccatos | yes | Violins I 116-117.5 per eighth 20.6 21.9 20.7 21.0 -> 18.4 18.4 17.2 17.5; Violins II 17.7 17.3 15.0 13.5 -> 13.9 13.0 15.0 13.6; Violas 12.1 13.5 11.9 10.8 -> 11.3 10.5 8.9 7.8 |
| 5 | A #4 Flute 1 115.5 | yes (NOTE_END_AT 115.8) | main track at 116 +60 ms -37.6 -> -50.4 dB |
| 5 | A #5 join holes | Oboe 1 95 / 99 fills 8 dB; cor anglais 24 fill (after the render: from 0.25 s before the onset, by stem fix) | stem dip Oboe 1 95 6.8 -> 4.3 dB, 99 9.9 -> 5.9; Violins II 576 10.9 -> 2.4 (no refit needed); cor anglais 24 6.7 -> 6.2 before the stem fix, not re-measured after it; Horn 1 415 5.7 -> 10.9 dB on one 50 ms window (unchanged data; the late A4, open) |
| 5 | B #4 Oboe 1 trims | yes | Oboe 1 minus Violins I on the 22 onsets: median -5.5, max -2.0, 0 over -2 (c54: 4) |
| 6 | Tutti entries | band envelope first: Double basses 552 confirmed (+128 ms; lead 60 -> 150 ms); 272, 464, 664, 676 and Flute 2 488 are not clean entries (the pitch band is within 7 dB of the body before the beat): no change. Also Oboe 2 104 / 128 (-144 / -156 ms; leads 180 -> 80 / 100 ms) and Bassoon 1 636 (+100 ms; 35 -> 90 ms) | not re-measured on the c55 render |
| - | Delivery rise delay (finale item 35) | not tested | |
| - | Stem-fix rows of c53 / c54 in REAPER | every main and pass-2 track rebuilt with `--midi-only --tempo` | timpani under the theme group 532-535 7.1 6.4 6.9 7.2 (c54 fixed stems 7.0 6.1 6.2 6.0); Oboe 1 minus Violins I 496-503 -4.3 -3.4 -3.5 -4.1 -4.5 -3.4 -5.1 -4.3; quarter 159 melody group minus celli +1.8 as rendered (c54 +3.8), +2.8 after this cycle's stem fix (target 4: fails); basses' final chord not re-measured |

Other rows of critic B's c54 table hold: celli minus Violins I 97-99 -1.7 -1.6 -2.5; 557.0 / 557.5 -2.0 / -3.5; bass
clarinet minus tuba -6.8..-1.0; basses pizzicato spread 3.3 / 5.8 dB.

## Stem fix after the render (level only; `tools/stem_fix.py 55 cycles/c55/rendered_build cycles/c55/variants/fix --apply`)
Violoncellos: -2.2 dB over quarter 159, level step +2.5 on 526. Cor anglais: the fill at 24 from 0.25 s before the onset.
The rows are in `build/` and reach REAPER with the next build.

## Tools
`tools/score_to_parts.py`: `STEADY_LINE` keys `own_front`, `body_db` / `body_s` / `body_off_s`, `tail_db` / `tail_s`,
`max_len_qn`, `ks_pre_s`, `slur_vel` (parts.json `steady_no_accent`, `steady_body`). With none set parts.json is
unchanged. `cycles/c55/actor_scripts/`: see README.md (c55 line).

## Render conditions
- Lock held 19:43-21:58 on 10 Nov (range tests 19:43-20:55, main render 21:19-21:30, pass 2 to 21:55). Turn rule: waited
  from 11:45 behind mvt2 and the scherzo; a deadlock with the finale's waiter (both started 16:48:40) was resolved by
  the coordinator; nothing was taken by hand.
- State guard: 0 stale at the first open; 2 after the full `--midi-only --tempo` build and restart (Bass clarinet,
  Trumpet 2), rebuilt in full, 0 before the main render; 2 in the post-render save (Horn 1, Trumpet 1), rebuilt, 0 at
  quit. Pass 2: 0 before, 2 after (Bassoon 1 stac, Flute 1 stac), rebuilt, 0 at quit.
- Memory: REAPER 44 GB with 3.0 GB compressed before the main render (limit 6; no --force-memory, no waiting needed),
  44 GB after it; pass 2 19 GB, 0 compressed. Attack probe: late or hole 0 in both passes. Disk 72-93 GB free.
- `metrics/state_check.txt` compares with c54 across the changed tempo map: its runs are not state changes.

## Delivery (`master_eq` unchanged)
-19.8 LUFS integrated, LRA 14.4 LU, true peak -1.7 dBTP, limiter about 0.9 dB, p10-to-max span 18.9 dB, 433.45 s.
Master before delivery: -20.8 LUFS, LRA 23.2 LU, true peak -0.7 dBFS (c54: -21.0, 23.1, -1.2).

## Not done, not verified
- Decision 2 beyond bars 33-40; decision 3 beyond the range test; decision 4's row-lead and pitch-pair table; the
  delivery rise delay; MANUAL-GAPS: only the velocity test on the Marc row (recorded under #8).
- Violoncellos 520-536 still fails S (robust SD 24 ms, 5 notes over 40 ms); its eighth-to-eighth body steps were not
  re-counted (neighbour body steps over 6 dB: 5 of 17, c54 7 of 17).
- Not re-measured on the c55 render: tutti-entry rows (basses 552, Oboe 2 104 / 128, Bassoon 1 636), Violas 438, the
  per-onset spread of bars 131-134, tutti-stop decays, the basses' final chord, the 2-5 kHz front of the accented
  theme notes, the master's pitch-band front minus tail, climax order and band shares of the delivery.
- Level rows keyed in fixed quarter notes near moved note-ons (`notchcheck55.py`: 61 breakpoints, at the new wind lead
  rows of 520-548 and 272-284 and at the removed arc ends 331-332 and 406-407) were listed, not checked one by one.
- The bow-change hole on the theme's long notes reads about 8 dB against the lifted body (c53 5.3 dB); the two
  re-bow pieces whose length changed (Violins II 188, 208) were not refitted.
- The stem-fix effects on cor anglais 24 and quarter 159 beyond the table; no listening.
- EW-TEMPLATE-PLAN sections still not applied: 5 (legato overlap; tested on the theme and not adopted), 6 (two tracks
  per string section), 7 (lean-off inside slurs), 8 (tutti entry spread), 10 (beat-position velocity).
