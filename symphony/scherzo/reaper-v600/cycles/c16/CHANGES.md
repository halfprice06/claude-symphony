# Cycle 16: changes (actor, on the c15 render)

Snapshot before this cycle: `cycles/c16/before/`. Scripts: `cycles/c16/actor_scripts/` (README, "Cycle 16"). Data as
rendered: `cycles/c16/build_render/`; data after the stem fix (equal to `build/` and to the saved REAPER project):
`cycles/c16/build_fix/`. Records: `cycles/c16/records/`. Positions are score quarter notes (qn); bar b starts at qn
3(b-1). Levels are mean-square dB (mean of the channels' powers).

STATUS: rendered once on 2026-11-15 (15:20-15:26 CST, freshly restarted REAPER), one stem fix (section roles on the
five string tracks), second delivery. mp3: `cycles/c16/scherzo-mockup-c16.mp3`.
Lock held 2026-11-11 17:25:18 to 2026-11-15 15:29:47. Working time under it was about 55 minutes (11 Nov 17:25-17:51:
open, full build, restart, one whole-piece pass; 15 Nov 15:02-15:30: measurement, rebuild, restart, render, mix-only
write, quit). In between the actor was stopped on a usage limit for four days with the lock held and REAPER open; the
finale's c18 waited behind it.

**For c17, first thing under the lock:** the project saved after the render holds 6 stale Opus states (Contrabassoon,
Horn 4, Violins I, Violas, Violoncellos, Violin I solo: `records/state_guard_final_save.txt`); run `tools/state_guard.py`
and rebuild them. `build/` and the saved project already contain the stem fix's roles.
**Not deleted (refused by the session's permission check, not retried):** c15's stems, `cycles/c16/render_first/`
(6 files, the pre-fix copies). `cycles/c16/rangetest/PA` (my pass) is deleted. 39 GB free.

## Result in numbers

| | c15 | c16 |
|---|---|---|
| master | -21.0 LUFS, LRA 22.7, TP -1.4, sample peak 0.840 | -20.6 LUFS, LRA 22.9, TP -2.1, sample peak 0.778 (first render -20.4, 22.7) |
| delivered mp3 | -19.8 LUFS, LRA 14.8, TP -1.6, limiter 2.4 dB, span 19.1 | -19.8 LUFS, LRA 14.9, TP -1.6, limiter 2.4 dB, span 20.2 |
| attack probe | late or hole 0 | late or hole 0 (both deliveries) |
| volume envelope: points / per note / per second (31 tracks) | 4,545 / 0.8 / 16.4 | 4,371 / 0.8 / 15.7 |
| notes with over 3 dB inside (moved note-on to note end) | 6 % | 3 % |
| notes with over 3 dB strictly inside; of these without accent, hairpin or dynamic change (`envstats15.py`) | 156; 57 | 97; 9 (timpani rolls 4, celli 3, Violins I 1, Horn 3 1: roll shapes and the final fade) |
| out-and-back excursions of 3 dB within 0.25 s | 67 | 27 |
| unprinted envelope moves inside a sounding note (`guard16.py`, the guard's own definition): notes over 2 dB | 123 (60 over 3 dB), first definition | 0 left by the guard; cross-check 1 note at 2.0 dB (Double basses 294, at a printed mark), 0 over 3 dB |
| critic B's count (2 dB within 0.5 qn under a sounding note, outside printed hairpins) | 89 | 8 (all at a printed dynamic mark on a joined note) |
| accents: level over the mean of the two neighbours, median, 274 accents (`meas16.py acc`) | +0.7 dB, 150 under +1 dB | +1.4 dB, 119 under +1 dB |
| re-bow dips of the last G sharp (lowest 40 ms frame against the 0.5 s before) | -12.5 / -12.4 / -13.5 dB (Violins I alone) | -4.1 / -5.1 / -4.1 / -4.1 / -6.5 dB (sum of the two instances, five bow changes); lowest 0.1 s frame 4.4 dB under the median |
| legato joins outside 25 / 60 ms (`s14.py`): Violins I, Violins II, Violas, Violoncellos | 10 / 3 of 100, 41 / 11 of 104, 32 / 3 of 67, 28 / 7 of 200 | 12 / 3 of 98, 31 / 4 of 104, 20 / 2 of 71, 43 / 4 of 198 |
| measure S, `timing13.py`, outside 25 / 60 ms | 26 % / 5 % (702 / 145 of 2,676) | 25 % / 5 % (682 / 123 of 2,677) |
| master per section against c15 (15 sections) | | -0.4 .. +0.9 dB (bars 121-140 +0.9, 325-340 +0.6) |
| delivered: bars 337 / 338 against bar 300 | -13.6 / -13.6 against -14.6 (1.0 dB) | -12.7 / -12.3 against -14.1 (1.4-1.8 dB) |
| hall: G.P. drop at +0.3 s, 20 dB fall, RT60; final chord | 20.8 dB, 0.24 s, 1.30 s; 20.7, 0.25, 1.32 | 21.3 dB, 0.28 s, 1.36 s; 20.6 dB, 0.30 s, 1.24 s |
| soft ends (`hall14.py`) | 0.06-0.22 s | 0.07, 0.19, 0.16 s |
| returns re dry | -12.74 dB | -12.42 dB |
| REAPER memory | 43-44 GB, 0 compressed before; 50 / 32 after | 43 GB settled with 27 GB compressed before the render (other processes held about 50 GB; rendered with `--force-memory`), 44 / 25 after |

## What was done, in the coordinator's order

| item | change (files, parameters) | measured on the c16 render |
|---|---|---|
| 1. Re-bows of exposed held notes (A #1, C #1) | `AUTO_REBOW_SKIP` Violins I 0.0 and Violins II 420.0 (one bow each; their stale `rebow_fills.json` keys removed). The last note: `REBOW_AT` 1103.814 / 1116.299 (the re-bow on the fermata bar is gone), all pieces on "Sus MAX" (new generic `ART_AT`), and new generic `HELD_DOUBLE`: the idle "Violin I solo" instance (DIV A, "Leg Slur MAX", no new row, no memory) plays the same G sharp with bow changes at 1096.14 / 1110.66 / 1121.0; the holding track lifts CC11 by 7 for 0.15 + 0.45 + 1.0 s over the other's new bow. Roles: Violins I 1089-1128 +2.5 -> -0.5, solo +5.5 (the DIV A copy read 8.5 dB under Violins I on the pass) | bars 1-8 and the harmonic: no dip (0.5 s levels -47..-51 and -47..-54 dB, one slow arc). Last note: sum of the two stems -48.6 dB (c15 -48.6 on Violins I alone), each instance -51.6; dips at the five bow changes 4.1-6.5 dB (c15 12.4-13.5); per second -51 -47 -48 -48 -49 -49 -48 -49 -48 -50 -50 -49 -50 -50. C's overlap of old and new bow on one track was not built: a same-pitch overlap on one instance stops the new note (kit LEARNINGS), and the finale measured that a CC swell does not close such a hole. The celli's points at 1074 / 1077 / 1080 and 609-618 are printed repeated notes (`rep_rebows`), not automatic re-bows: left |
| 2. Moves inside sounding notes (B #2, A #4) | new generic `tools/build_reaper.py` `note_move_guard` (mix.json; max 1.9 dB per note outside printed hairpins, marks, subito tails, the fade and timpani rolls): a move at a note's start is finished before its note-on (after a rest) or on the score onset (a join); any other is held to the note's end and returns in the next rest, across the next printed zone, or at 2 dB/s under the following notes. 101 snaps and 130 holds. A note entering after a rest is checked from its moved note-on, and a printed mark on its own entry is moved before the note-on (Movement II c56 #4, Movement I c58 #2). 30 role rows that covered one note or figure removed or merged in a first pass, then 25 more that cover one or two notes and less than two bars (coordinator, Movement II's ROLE_NOTE_MIN; list in roles.json `_c16_dropped_note_rows`); Flute 1's "col Vl. solo" step moved from 1049.5 to 1044; `TIMP_SETTLE_SKIP` | counts in the table above. Bars 129-131: master at qn 383 / 387-389 -21.9 / -24.1 dB (c15 -21.4 / -26.1: the cadence sinks 2.2 dB instead of 4.7). Cost: held crescendo arrivals raise sections: Double basses bars 121-140 +2.2, 253-288 +1.7, 153-208 +1.1; violas 121-140 +1.8, 253-288 +2.0; Bassoon 1 253-288 +2.2, Bassoon 2 13-56 +1.8 |
| 3. Accents (A #2, C #4; Dan on the finale: "a little bit over done") | new generic `CC11_REST_MAP` (strings and woodwinds: printed 114 plays 104, 127 plays 108; knee 96) with `dyn_trim_db` ff +1.6 strings (Violins I / II +0.8, basses +2.4) and +1.2 woodwinds; new generic `ACCENT_CC`: strings +12 (+20 from CC 98, ceiling 124) held 0.15 s, back over 0.3 s; woodwinds +12 (+10 from CC 98, ceiling 116) held 0.08 s, back over 0.22 s (halved after the pass, where their ff accents read +4.0 dB); `ACCENT_SUS_MIN_CC` woodwinds 44 (8 accented slur heads per track on "Sus MAX"). The lead, row and velocity rules read CC11 as before. No range test on bars 105-120 alone: one whole-piece pass of 16 tracks instead | per track, accent over neighbours (median; c15 in brackets): Flute 1 +3.6 (+1.6), Flute 2 -0.8 (-3.7), Oboe 1 +1.2 (-1.1), cor anglais +2.8 (+2.2), Clarinet 1 +5.0 (+3.8), Clarinet 2 +0.8 (+0.9), Bassoon 1 +3.1 (+1.0), Bassoon 2 +1.3, Contrabassoon +0.4, Violins I +2.0 (+0.7), Violins II +1.4 (+0.7), violas +0.5 (-0.8), celli +0.9 (+0.6), basses +0.4 (+0.7). By class: strings ff +0.8, mf-f +1.6, p-mp +2.2; woodwinds ff +2.7, mf-f +1.4, p-mp +0.8. Over Dan's +3 limit: Flute 1, Clarinet 1, Bassoon 1 (c17: bring down). Still without weight: strings at ff, violas, basses, Flute 2. Section levels bars 105-120 against c15: within 1.0 dB except Oboe 1 -1.5 |
| 4. The sf of the tutti sfp (B #4, C #3) | `ART_AT` Violins I 900 "Sus MAX"; the sfp's attack keeps its printed CC11 + 8 (`CC11_REST_SFP_ADD`: 122-127) over an ff upbeat resting at 99 (899 skipped by `ACCENT_CC`); `RIDE_TRIMS`: c15's -1 dB row over 1004-1017 removed, the 897 row starts at 894; roles 1004.75-1017 Violins I +2.5, violas +1.5 | Violins I sf -27.4 dB against its upbeat -28.5 (c15 -29.0 against -26.7). Master 50 ms frames from 898.5: -14 -15 -14 -18 -22 -23 **-16 -19 -20 -22** -18 (c15 -16 -16 -15 -19 -22 -24 **-17 -20 -21 -21**): the sf is 1 dB higher but still 2 dB under the upbeat chord. Summit margin in the delivery 1.4-1.8 dB (c15 1.0; c14 2.4) |
| 5. Timpani (B #1) | `TIMP_LOUD_VEL_ADD` (8, 104, 0.0); roles +2.5 on 312-360, 912-960, 996-1004.9 and +2.0 on 264-312, 864-912 (after the pass: -1.7 / -2.2 dB there); new generic `TIMP_CC1_AT`: roll 336 CC1 118, roll 332 CC1 62 -> 104; `TIMP_SETTLE_SKIP` 1005; the -4 role from 1008.5; the two single-stroke fader rows (597, 624) as velocity 96 / 103 | roll 336, 50 ms frames: -30 -32 -31 -32 -32 -33 -32 -32 -33 -34 -34 -33 -34 (c15 -29 ... -45). Roll 332: first / last 0.2 s -41.1 / -38.8 (+2.3 dB; c15 -0.8; target 4 not met: the "Crs" row is the next step). Sections against c15: within 1.0 dB except bars 13-56 -1.2. 2-5 kHz share of the stroke fronts: not measured this cycle |
| 6. Legato after a row change (C #2) | `KS_MIN_LEAD_S` 0.15 on Violins II and Violas (and Violas div); new generic `ROW_CHANGE_LEAD_S` (0.235 / 0.245 / 0.20 / 0.21 s, at most the previous slot less 20 ms); `ART_AT` Violas 579 / 585 "Sus MAX"; strokes Violins I 372, Violins II 372 / 385.5, celli 524; then one refit step on the single pass (new generic `LEAD_SET_AT`, `build/lead_set.json`: 74 joins with a reading over 40 ms, gain 0.85). Two passes of identical data were planned; only one was made | joins over 60 ms late or early: Violins I 3, Violins II 11 -> 4, violas 3 -> 2, celli 7 -> 4. Outside 25 ms: Violins II 41 -> 31, violas 32 -> 20, celli 28 -> 43 (worse: the refit moved 30 cello joins on one reading). Violas 579 / 585 and render-to-render stability: not checked (one render) |
| 7. Row levels (A #3) | `region_gain_db` extended (list of specs, row names without case, `row_dyn_db` by dynamic layer or velocity range): Flute 2 staccato row -4; Flute 1 staccato velocity 75+ +4 (its ten +5 fader rows and three tutti roles removed or lowered); Oboe 1 staccato velocity 75+ -3; Violins II "Leg Slur MAX" f / ff +2; celli and violas "Sus MAX" pp / p +2. Cor anglais A4: the patch names the row "Sus Max", so c15's gain never reached it: -4.5 on "Sus Max", -3.5 on "Leg Slur MAX" (first values after the critics, then lowered after the pass: -6 / -5 / +4 / +4 and A4 -7 moved sections by 2-6 dB) | cor anglais A4 at 310 +6.9 dB over the B4 before it (c15 +11.7); its sections 121-140 -3.9, 289-304 -2.7 against c15. Flute 2 bars 13-56 -2.0, 253-288 -1.5. Row-pair table (`meas16.py rows`): not run on the final render |
| 8. Balances (B #3, #5; C #5-6) | new generic `CC11_ADD_SPANS`: Oboe 1 827.95-840 +11..14 (role -4 -> -1.5); celli 503-506 +10 -> 0. Basses: div. octaves 756-801 velocity 53 -> 42; pizzicato region gains F sharp 1 -4, C sharp 2 -3.5, E2 +2.5, E1 +1.5, A2 -4, G sharp 2 -3; "Sus MAX" G1 -3, G sharp 1 -2.5, A1 -1.5, E2 +2. Celli pizzicato A2 -5, D3 +5 | Oboe 1 at 828 / 829 / 830: -52.7 / -48.8 / -53.1 dB (c15 -60.1 / -60.0 / -57.9); bars 277-280 oboe 3.2 dB under Flute 1 (c15 6.7). Basses bars 253-268 -45.6 dB (c15 -44.7), 6.9 dB under Violins I. Celli 504: -50.2 / -41.3 / -39.6 / -33.1 at 0 / +90 / +200 / +400 ms: still a 17 dB swell, not fixed. Pitch residuals: not re-measured |
| 9. Repeats (A #5) | new generic `REP_GAP_FLOOR_S` brass 0.09, woodwinds 0.065 s; Horn 1's re-tongue gap 0.035 -> 0.065, fall 8 | separation median, repeats under 3 dB (c15): Horn 1 10.4 dB, 4 of 43 (5.9, 11); Horn 2 9.6, 6 (10.1, 6); Horn 3 8.6, 2 (8.1, 5); Horn 4 6.6, 3 (5.1, 5); trumpets 9.3 / 6.4, 0 (2.0 / 1.5, 2 and 3) |
| 10. Heads and join bumps (A #6) | celli 570 / 764 / 800 velocity 80; `ACCENT_CC_AT` celli 794 / 542, Bassoon 1 353 / 953, Clarinet 1 576; Violas div 1044 entry extra 0.20 | not measured |

## Coordinator messages during the cycle

- Movement II c55 (role rows over one or two notes): 25 rows dropped (above). Kept: role rows on held notes of two bars or more.
- Movement II c56 / Movement I c58 (CC + envelope pairs): `SHORT_CC11_PARK` is off and no track carries `cc11_park` or `vol_post`; the sfp at 900 lost its c12 fader bumps in c15 and has its attack in CC11 now. Other fitted pairs were not audited.
- Movement I c57 / c58 (slow rows fitted to old layers): the envelope still holds 172 role rows (207 before), 14 one-level rows of a bar or more and 26 unison spans. Of the roles, c15 wrote about 25 passage constants from the old per-note levels (roles.json `_c15`); this cycle moved Flute 1's (13 rows) into a row gain and added 21 section rows (timpani 5, the strings' two development sections 10, summit 2, the doubled G sharp 2, Flute 1 2). They are not sorted by cause yet (sample level / mapping / bar means / phrase decisions): c17.
- Movement I c57 #5 (a "drive" phrase shape sinking held horn notes): not checked.
- Movement II c56 #7 (legato velocity 124): 76 legato-row string notes play velocity 120 or more (celli 43); not changed, their leads are fitted to it.
- Finale c17 / c18 and Dan's note on accents: taken into item 3.

## Faults left audible (no instrument-side fix found or built this cycle)

| line, bars | fault, measured |
|---|---|
| strings at ff, violas, basses, Flute 2: printed accents | +0.8 dB (strings ff), +0.5, +0.4, -0.8 over the neighbours |
| Flute 1, Clarinet 1, Bassoon 1: accents | +3.6, +5.0, +3.1 dB: over Dan's limit |
| tutti sfp, bar 301 | the sf is 2 dB under the ff upbeat chord in the master |
| Violins I + solo, bars 364-376 | 4-6.5 dB dips at five bow changes (c14 with fills: 1-4 dB) |
| celli, bar 169 (qn 504) | 17 dB swell through the first note of the trio tune |
| timpani roll, bar 332 | grows 2.3 dB (printed mf < f) |
| cor anglais A4 at f / ff | 6.9 dB over its neighbour; with the gain its sections are 2.7-3.9 dB under c15 |
| Horn 1, qn 598 | 8 dB fall inside a slur (not touched) |
| bar 332, brass | the six rows that held the brass back in the printed crescendo are gone (rows inside one note): they reach f earlier again (c11 B #4) |
| Clarinet 1, bars 72 and 300 | its rows of -5 dB are gone: sections 57-104 +3.1, 289-304 +3.6 dB against c15 |
| crescendo arrivals | held through the arrival note; basses, violas and bassoons 1.1-2.2 dB over c15 in four sections |
| celli legato joins | 43 of 198 outside 25 ms (c15 28) |

## Rejected, deferred, not done

- C's overlap of old and new bow on one track (not possible on one instance); the "18 Violins KS Master" test; Horn 1 598; the per-pitch fits after the region gains; a second pass and a two-pass refit; the 2-5 kHz check of the timpani fronts; the hall of the first sub. p; MANUAL-GAPS items other than the dynamic-layer gains (recorded there).
- A stem fix for Clarinet 1, cor anglais and the held arrivals was not made (they are single bars, one pitch, or the intended effect of item 2).

## Research items

| item | status |
|---|---|
| EW template mix, returns, EQ set, seats, wind send, return pans | adopted (unchanged) |
| "no volume automation per note; reference projects 0.01-0.36 points per second" | adopted: 15.7 points per second over 31 tracks; unprinted moves inside notes 0 by the guard |
| accents by controller, not fader (finale technique 70) | adopted, reduced on the woodwinds after Dan's note |
| one legato row per string line, keyswitch 0.15 s ahead | adopted on all five sections now; refit on one pass only |
| per-region / per-row volume in the Opus state | adopted and extended to dynamic layers |
| unprinted tempo, Slur Runs, Close + Main on divisi | rejected earlier, stays out |
| CC16 resets everywhere, delivery rise delay, separate legato tracks, timpani hard sticks, recorded crescendo rolls | pending |
