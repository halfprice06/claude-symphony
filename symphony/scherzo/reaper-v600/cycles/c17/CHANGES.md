# Cycle 17: changes (actor, on the c16 render)

STATUS: rendered twice on 2026-11-15 / 16 (first render 23:38, second 23:57 CST, each from a freshly restarted REAPER),
then one stem fix (Horn 1 roles) and a second delivery. mp3: `cycles/c17/scherzo-mockup-c17.mp3` (279.5 s, md5
2ceecf713c3f62dfd6d142527453067b). The work was prepared on 15 Nov 16:02-18:05 and stopped then (disk under 30 GB, lock
not reached); it was resumed at 22:19 with 54 GB free. Lock held 22:25:44 to 00:06:12 (100 minutes: full build, Horn 1
and last-note range tests, five restarts, two renders). The lock was free from 22:16 while the Movement II and finale
waiters each listed the other as ahead; scherzo, queued since 16:17, took it (`lock_wait.log`).

Snapshot: `cycles/c17/before/`. Data as rendered (second render): `cycles/c17/build_render/`; first render's data:
`build_render1/`; after the stem fix (equal to `build/` and the saved project): `build_fix/`. Scripts:
`cycles/c17/actor_scripts/`. Records: `cycles/c17/records/`. `render_first/` holds the first render (its Horn 1 stem and
master were overwritten by the stem fix's originals of the second render). Positions are score quarter notes.

**For c18, first thing under the lock:** the saved project holds 4 stale Opus states (Horn 2, Horn 4, Violins I,
Violoncellos: `records/state_guard_final_save.txt`). `build/` equals the saved project's data.
**Second render, why:** the first render confirmed the predicted drops (low winds, basses, celli 3.0-4.8 dB under c16
in bars 121-140 and 253-288), Violas' bar 326 fell 8.6 dB, Horn 1 read 1.3-2.8 dB low after its mic change, and
Violins I / II accents read +2.6 / +3.6. Fixes are in the table (marked "second render").

## Result in numbers

| | c16 | c17 |
|---|---|---|
| master | -20.6 LUFS, LRA 22.9, TP -2.1, sample peak 0.778 | -21.7 LUFS, LRA 22.5, TP -3.0, sample peak 0.705 (first render -22.0, 22.7) |
| delivered mp3 | -19.8 LUFS, LRA 14.9, TP -1.6, limiter 2.4 dB, span 20.2 | -19.8 LUFS, LRA 14.3, TP -1.6, limiter 1.6 dB, span 19.4 |
| attack probe | late or hole 0 | late or hole 0 (both renders, and after the fix) |
| envelope: points / per note / per second (`slope17.py`) | 4,433 / 0.77 / 16.0 | 4,857 / 0.84 / 17.5 (more points: role edges and held gains are ramps drawn by the guard) |
| slope guard (unprinted 1.5 dB within 0.5 s inside a sounding note) | 42 notes (B: 44) | 8 notes: celli 312 / 912 / 362, Horn 2 1005, Horn 3 953 / 936, Horn 4 915, Harp 708 |
| notes with over 3 dB strictly inside; unprinted | 97; 9 | not re-counted (`envstats15.py` not run) |
| role rows | 172 | 177 (17 removed or merged by B's sorting, 22 section rows added after the first render, see item 7) |
| isolated accents, all tracks (144): median / p90 / over +3 dB | +3.1 / +6.5 / 75 | +1.4 / +4.9 / 33 |
| last G sharp: dips of the two-instance sum at the bow changes (40 ms frame against the 0.5 s before) | 5.0 / 4.3 / 5.4 / 4.5 / 8.2 dB (five changes, this script) | 3.5 / 2.3 / 1.6 dB (three changes); sum level -48.5 dB (c16 -48.5) |
| last G sharp: 4-8 kHz against 0.5-1.5 kHz of the sum, per second | -4.6 .. -16.2 dB | -8.4 .. -16.4 dB on the range test (copy alone -8.7 .. -14.2; c16 -1.2 .. -5) |
| last G sharp: L/R correlation of the sum / Violins I alone / L-R | 0.65 / 0.40 / +5.7 | 0.64 / 0.38 / +5.6 (the Close-only copy narrows the pair as before) |
| Horn 1 G sharp 4, 400-430 Hz: L/R correlation, mono loss (bars 1-2; last note) | -0.69, -8.1 dB; -0.81, -10.3 dB | +0.65, -0.9 dB; +0.45, -1.5 dB. Stem L-R +1.5 / +2.2 (c16 +0.1 / -0.3) |
| Horn 3 G sharp 4 at qn 1092 | -0.71, -8.4 dB | unchanged (not treated) |
| sf of bar 301, master 20-200 ms after qn 897 / 898 / 899 / 900 (first render) | -15.2 / -14.3 / -19.6 / -19.7 | -21.0 / -20.1 / -23.8 / -20.8: the sf is 3.0 dB over its upbeat and within 0.7 dB of bar 300, which itself fell 4.6 dB |
| climax order (first render): bars 105-120, 305-320; bars 336-338 | -20.6, -20.5; -15.5 / -15.1 / -14.6 | -20.9, -21.3; -16.6 / -15.9 / -15.4: the summit stays 4.3-5.9 dB over the tuttis |
| measure S (`timing13.py`) outside 25 / 60 ms | 25 % / 5 % (682 / 123 of 2,677) | 25 % / 5 % (675 / 133 of 2,679). The eight joins were not read one by one (`s14.py` not run); their leads are 174-245 ms (c16: 94) |
| master per section against c16 (15 sections) | | +1.5 (bars 1-12, Horn 1) .. -1.2 (289-304); against c15 the first render read -1.4 .. +0.6 |
| master per bar against c16 (`records/bars_c17_vs_c16.txt`) | | 10 bars over +1.5 dB (67, 90, 93, 97, 137, 138, 290, 349, 374, 376), 20 under -1.5 dB (41, 42, 72, 73, 129, 130, 184, 195-198, 264, 284-286, 300, 312, 326, 364, 365) |
| hall: G.P. drop at +0.3 s, 20 dB fall, RT60 (`hall14.py`); late slope (C's reading) | 21.3 dB, 0.28 s, 1.36 s; 1.54 s | 20.1 dB, 0.30 s, 1.36 s; 1.53 s. Soft ends 0.07 / 0.19 / 0.10 / 0.12 s. Returns re dry -12.83 dB |
| REAPER memory | 43 GB settled, 44 / 25 after | 43 GB settled with 0 compressed before each render, 43 / 18 after. 56 GB (35 compressed) after 33 full rebuilds in one run; restarted |

Section balance against c16 after the second render and the fix (`records/bal_c17_vs_c16.txt`; over 1.5 dB): Flute 1
57-104 -2.5 and 289-304 -4.1 (bars 72 / 300 and the dropped gains), Flute 2 +2.0..+2.8 in four loud sections ("Sus MAX"
f layer +3), cor anglais 253-288 -3.5, Clarinet 1 57-104 -4.2 and 289-304 -4.7 (its C sharp 6, intended), Clarinet 2
-1.5..-3.2 (intended in the tuttis), Bassoon 1 253-288 -2.3, Contrabassoon 325-340 -2.0, Violas 121-140 -2.1 and
253-288 -2.2, basses -2.0 in three sections, Violins II 325-340 -2.3. In bars 121-140 and 253-288 c16 stood 1.1-2.2 dB
over c15 (held arrival gains), so these land near c15.

## What was done, in the coordinator's order

The table is the preparation of 18:05 ("not rendered" in its last column means not rendered then). Values changed later are in the notes under it and win: Horn 1 CC11 +14 / +8 (not +11), lift (10, 0, 0.30, 0.55, 0.3), accent hold 0.08 s with `pre_s` 0, Violins I 3 / 12, Violins II 2 / 6, Bassoon 1 0 / 0, 59 gains in CC11 (not 84), roles 177 (not 155), short-row gains -1.5 (not -3), Flute 2 staccato -2.5.



| item | change (files, parameters) | as prepared on the data (measured results: table above and the notes below) |
|---|---|---|
| 1. Closing solos (B #1) | `roles.json` Violin I solo [1044, 1068, 8] -> [1040, 1068, 8]; `CC11_ADD_SPANS` Horn 1 (1100.7, 1128, +11): CC11 34 -> 45 from the note-on | data checked (`chk17.txt`); not rendered |
| 2. Horn 1 G sharp 4 in anti-phase (C #1) | `tools/build_reaper.py`: mix.json track key `channel_map` (the instrument's `channelMap`). No setting chosen | range test not run; the fault stays in the data |
| 3. Last violin G sharp (A #3, C #2) | `REBOW_AT` Violins I [1110.963] (269.0 s); `HELD_DOUBLE` copy re-bows at 1099.912 / 1119.618 (266.0 / 272.0 s), `art` "Sus MAX" (keyswitch at 1087.544, row now in the solo's `art_counts`), `lift` (7, 0.15, 0.45, 1.0, 0.3): complete on the other's change | range test not run; the solo's role +5.5 is unfitted for the new row |
| 4. Accents (A #2) | `ACCENT_CC` per track: add / add_loud Flute 1 2 / 0, Flute 2 12 / 10, Oboe 1 12 / 4, cor anglais 0 / 0, Clarinet 1 0 / 0, Clarinet 2 12 / 0, Bassoon 1 12 / 0, Violins I 6 / 20, Violins II 8 / 14, Violas 5 / 20, others as c16; shape 0.06 s + 0.20 s from the later of the moved note-on and score onset - 0.03 s (`from_moved`); none on "Sus Marc LITE"; 213 / 897 at +8. Stave scaling written (`scale_staves`) and left off (Movement I c59: the sum rises as each track does). Baselines in `region_gain_db`: Flute 1 "Sus MAX" f layer E6 / G6 -5 (the patch has layers pp / mf / f, no ff), staccato row +3; Flute 2 staccato -4 -> -1, "Sus MAX" f +3; Clarinet 2 A4 -2.5 / G4 +1.5 (its row has no dynamic layers, so half of A's ff values on all); Oboe 1 staccato under velocity 75 -3; Violas "Stac RRx9" under velocity 61 -3; Clarinet 1 C sharp 6 -5.5 | Violins I 327: CC11 127 for 0.1 s after the beat, 110 at +0.2 s, 107 at +0.35 (c16: 127 / 124 / 114). Not rendered; the per-track table of isolated and in-run accents cannot be given |
| 5. sf of bar 301, gains on held notes (B #2, #3) | `HP_GAIN_TO_CC11` (new): a crescendo gain released inside a note that sounds 0.25 s past the release start leaves the envelope and goes into CC11 at 0.22 dB per unit, at most the arrival's played CC11 + 10, back over 0.6 s: 84 gains on 22 tracks; the gains into 213 and 897 dropped (28). `CHORD_CC11` (new): -7 / -11 units on double / triple stops at 213-216, 897-900, 1005-1017: 3 chords each on Violins II, Violas, celli. `cresc_trim_hold` skip + [840, 852], [372, 384], [108, 120], [576, 588], [1002, 1005]. `ROLE_EDGE_MOVED` 0.03 s (new) and `note_move_guard` max_db 1.9 -> 1.4 | slope guard 42 -> 9 notes. Violins II 897: CC11 124 -> 103, sf at 900 127. Violins I's sf stays on "Sus MAX": "Sus Marc LITE" has velocity-split regions only for its attack overlay (1-65 / 66-108 / 109-127), its sustain layers are 1-127, so B's velocity-limited row gain cannot work |
| 6. Legato lead cap (A #1) | `PREV_MIN_SOUND_S` 0.06 (new) in both cap blocks; `lead_set.json` celli 321 0.17, 921 0.175, 933 0.18, 570 0.275, 350 0.255, 526 0.27, 506 0.24; `CC11_ADD_SPANS` celli -14 across 504.95-505.6 (the +10 at 503-506 removed). Fix found on the way: `KS_MIN_LEAD_S` took a note's own rounded note-on for the previous one and left the keyswitch 7 ms before the note (three new cases, and Violins II 386 and Violas 725 from c16) | leads in the table above. Not rendered |
| 7. Leftover lines and role rows (B #4) | the two one-level c14 celli lines (333-341.4, 933-941.4, +6 dB) unwritten; celli "Leg Slur MAX" f / ff +1.5 in the Opus state. Roles 172 -> 155: 7 bar-mean coda rows deleted, Violas' cancelling pair deleted, 4 overlapping pairs merged (Bassoon 1 996-1017 -4.7 and 696-711 +6, Flute 1 1044-1068 -9.5, celli 624-648 -1.5 / 648-672 +0.5), 4 f-staccato rows (Flute 2, cor anglais) into row gains, Violas 975-978 (one bar) and the timpani summit cut deleted, solo start moved, Clarinet 2 -3 added in both tuttis. Kept as section rows: the mapping rows of the two tuttis and the summit (moving them into `dyn_trim_db` would move every other ff passage of those tracks by 2-4 dB, unmeasured); Violas 624-672 -3.7 and 360-420 -1.8 (no chord in the data there); all phrase rows | not rendered. Rows under two bars still present: Trumpet 1 / 2 [994, 995.5], Oboe 1 [672, 676.5], Timpani [300, 300.5] |
| 8. Sample levels (B #5, A #6) | cor anglais: staccato A4 -4.5, staccato row +3, "Sus Max" A4 -4.5 plus -2.5 in the f layer, B4 +2.5 and D sharp 5 +3 on the sustain and legato rows; basses pizzicato G sharp 1 -5 -> +1; celli pp pizzicato of bars 89-98 velocity 41 -> 52 (the patch's layer edge is 50 / 51); Violins I "Stac RRx14" velocity 90+ -3; Violins II "Spiccato RRx9" velocity 80+ -3 (layers 80-109 / 110-127); Clarinet 2 -3 in the tuttis | not rendered |
| 9. Timpani (B #6) | the five summit strokes at velocity 104 (`VEL_SET`), role [1008.5, 1020, -4] deleted | data checked |
| 10. Optional | Horn 1 630 / 633 / 663 on "Sus MAX" (`ART_AT`); Violas div 1047 and solo 1065 at velocity 64; the dead `ACCENT_CC_AT` lifts on Bassoon 1 and Clarinet 1 removed | not rendered. Not done: woodwind Main mics, Violas div spread, woodwind join holes, Horn 1 598, string repeat gaps |


Changes made after the 18:05 stop (resume, range tests, second render):
- Item 1 / 2, Horn 1: mix.json `mic_db` Close -1.4 / Main -5.2 dB (the coordinator's 0.85 / 0.55), `gain_db` 1.13 -> -1.17. Range test (qn -3..20, two equal passes): fundamental correlation -0.69 -> +0.65, the horn call's stem correlation 0.82 -> 0.98 (drier and narrower: the cost). Levels by passage moved unequally (call +4.7, soft G sharp +1.2 before the gain), so `CC11_ADD_SPANS` Horn 1 +8 on bars 1-2 and +14 on the last note (0.22 dB per unit at CC11 about 35, measured: +5 units = +1.1 dB), and after the second render roles [0, 18, 4] -> [0, 5.9, 4] + [6, 18, 1.6], [756, 864, -1.5], [1020, 1068, -2.5] by stem fix. `channel_map` was not needed and stays untested. B flat 4 not checked. Last note: -44..-47 dB in its first six seconds (c15 -43..-46, c16 -46..-48).
- Item 3: `lift` (10, 0, 0.30, 0.55, 0.3) after the range test (7 gave dips 6.9 / 3.6 / 1.5 dB); solo role +5.5 -> +4.5.
- Item 4, second render: Violins I 3 / 12, Violins II 2 / 6, Bassoon 1 0 / 0; hold 0.08 s from the score onset on led notes (`pre_s` 0); bars 72 / 300 +12 on the strings. Per track, isolated accents (n, median, p90) and accents in runs (n, median): Flute 1 18 +1.1 +2.4, 14 -0.2; Flute 2 7 +1.4 +5.4; Oboe 1 22 +1.6 +3.7, 2 -1.5; cor anglais 13 +0.5 +2.6, 15 +0.9; Clarinet 1 5 +3.2 +5.3, 4 +2.2 (no bump left: sample level); Clarinet 2 10 +1.6 +6.5, 6 +0.8; Bassoon 1 3 -1.2 +3.8, 3 -0.1; Violins I 28 +1.8 +4.9, 17 -0.2; Violins II 18 +2.5 +5.9, 16 +0.5; Violas 12 +1.4 +3.7, 16 +0.3; celli 6 +0.5 +2.5, 15 +0.5; basses 0, 15 +0.5 (`records/acc17.txt`). Medians: every track at +3 or under except Clarinet 1; inside +1.0..+2.0 on Flute 1, Flute 2, Oboe 1, Clarinet 2, Violins I, Violas. The 90th percentile is over +3.5 on eight tracks (pitch and row level, not the bump). The measure is A's; accents carrying a new dynamic or inside a hairpin are not excluded.
- Item 5: `HP_GAIN_TO_CC11` `max_arrival_cc` 100: 16 gains into ff arrivals lost 1.5-4 dB because CC11 is flat above 104 (`records/hp_to_cc11_clipped.txt`); they stay in the envelope. Final count: 59 gains in CC11, 28 dropped, 25 kept. 13 f arrivals still lose 1.8 dB (asked 18 units, written 10).
- Item 7, second render and fix: section rows added where the first render stood over 1.5 dB under c15: bassoons, contrabassoon, basses, celli +1.5..+3.0 over 360-420 and 828-864; clarinets and Bassoon 2 +2.5 over 108-132; clarinets and Bassoon 1 +2.0 over 576-600; cor anglais +2 and contrabassoon +3 over 168-312 and 864-912; Flute 2's two f-staccato rows back at +4 (row -2.5); the c16 stem-fix rows of the strings over 168-312 and 864-912 removed (Violins I) or cut to -0.7 / -0.8. Roles 155 -> 177.
- Item 8: Violas "Stac RRx9" soft layer -3 -> -1.5, Violins I / II short rows -3 -> -1.5 (first render: soft viola passages -2.2..-2.7, tuttis -1.7 / -2.2). Celli pp pizzicato at velocity 52: the stem over bars 89-98 rose 9.2 dB (-61.4 -> -52.2), now at the basses' -48..-52; the spread of the three-note cycle was not re-measured. Row levels are written as region volumes (not the row knob) and arrive: Flute 2 +2.0..+2.8 for +3 on one layer.
- Violas bar 326: `CC11_ADD_SPANS` +14 over 974.8-978.

## Hall: the two readings (on c05, c15, c16 masters, `hall17.py`)

`hall14.py` reads "RT60" as 2 x (time from -5 to -35 dB) after the G.P. cut-off: the first 0.1-0.8 s, which holds the
direct sound's own fall and the early hall. Critic C fits the slope between -25 and -55 dB: 0.4-1.3 s after the
cut-off, the late tail. Same frames (10 ms, broadband) and same reference, c16: 1.42 s and 1.54 s; c05: 1.38-1.80 s
(by cut-off frame) and 1.92-2.10 s. The first reading moves by about 0.1 s when the cut-off frame moves by 0.1 s; the
second does not. Dan's 1.5 s limit was set with the hall14 reading of c05, so it refers to that reading; on C's late
slope the same limit is c05's 2.0-2.1 s. By both methods c16 is not wetter than c05 (1.36-1.42 against 1.5; 1.54
against 2.0-2.1). No hall change.

## Faults left audible

| line, bars | fault, measured |
|---|---|
| master, bars 72 and 300 | 4.7 / 4.6 dB under c16 (about 3 under c15): accent, chord rule, Clarinet 1's pitch gain and the dropped gains together are more than B asked |
| Violas, bar 326 | master 4.3 dB under c16 after CC11 +14 (first render -6.4) |
| master, bars 41-42, 195-198, 284-286, 129-130 | 1.8-3.2 dB under c16: arrivals whose gain went to CC11 capped at +10 units |
| master, bars 364-365 | -2.1 / -2.3 dB: not examined |
| celli, bars 112-114 and 312-314 | 2.2 dB under the bars before (first render: -35.0 against -32.8) with the +6 lines gone; the legato row's f / ff gain of +1.5 gave 0.2 dB |
| Horn 1 | drier and narrower than Horns 2-4 (stem correlation 0.98 in the call); +2.9 / +1.7 dB in bars 374 / 376 against c16 |
| Horn 3, qn 1092 | G sharp 4 still in anti-phase (-0.71) |
| accents | Clarinet 1 median +3.2; 33 of 144 isolated accents over +3 dB |
| slope guard | 8 notes (table) |

## Rejected, deferred, not done

- B's velocity-limited row gain for Violins I's sf (the row's sustain layers are not velocity-split).
- Mapping rows into `dyn_trim_db`; timpani roles into CC7; staff-count scaling of accents (coordinator).
- Not done: `channel_map` test, B flat 4 check, Violas div spread, woodwind Main mics, woodwind join holes, Horn 1 598, string repeat gaps, the per-join S readings, the 2 dB / 3 dB inside-note counts, brass accents (none printed here), MANUAL-GAPS items.
- Not deleted: nothing of c16 or earlier (as instructed); `cycles/c17/render_first/` (2.9 GB, first render) is kept; my range-test WAVs and scratch are deleted. 48 GB free at 00:15.

## Research items

| item | status |
|---|---|
| EW template mix, returns, EQ set, seats, wind send, return pans | adopted (unchanged) |
| no volume automation per note | adopted; slope guard 42 -> 9 notes in the data |
| accents by controller | adopted, per track and shorter |
| one legato row per string line, keyswitch 0.15 s ahead | adopted; rounding fault fixed |
| per-region / per-row volume in the Opus state | adopted, extended (velocity-below, pitch in one layer) |
| unprinted tempo, Slur Runs, Close + Main on divisi | rejected earlier |
| CC16 resets everywhere, delivery rise delay, separate legato tracks, timpani hard sticks, recorded crescendo rolls | pending |
