# Cycle 13: changes (actor, on the c12 render)

Snapshot before this cycle: `cycles/c13/before/`. Scripts: `cycles/c13/actor_scripts/` (`apply13.py` table and mix edits;
`timing13.py` measure S; `pairs13.py` the theme head's two slurred eighths; `check13.py CYCLE [block]` blocks `hem pick
timp ob tpt ww seat wet pairs`; `pdiff13.py` parts.json diff; `rr13.py` range-render jobs; `vcjoin13.py`, `kscmp13.py`,
`sd13.py` range-test measures; `phase1.sh` / `phase2.sh` the lock phases). Data as rendered: `cycles/c13/build_render/`.
Records: `cycles/c13/records/` (`*_c12.*` = the same script on the c12 render). Range tests: `cycles/c13/rangetest/`.
The first c13 render's metrics, mp3 and data are in `cycles/c13/first/` (its WAVs are deleted).

STATUS: rendered twice on 2026-11-10 (17:50 and 18:27 CST, both from a freshly restarted REAPER, 0 GB compressed). The
second render is the cycle's render: `cycles/c13/scherzo-mockup-c13.mp3`. Reason for the second render: the first one
had the new theme-head rows with the second eighth ringing over the staccato after it in all nine statements (below, A #1).
Lock held 17:09:45-18:37:49 CST (88 min; the wait for it lasted from 07:50 to 17:09 behind Movement II, Movement I,
the finale and Movement II again). No stem fix, no splice.

Positions are score quarter notes (qn); bar b starts at qn 3(b-1). "S" is critic A's measure (the earlier of pcX and
the robust band crossover; entries pcX), ms against the score onset, positive = late; my implementation is
`timing13.py` (16 tracks, qn 36-216, 264-420, 756-1017, same-pitch repeats left out).

## Result in numbers

| | c12 | c13 |
|---|---|---|
| master | -20.8 LUFS, LRA 23.4, TP -1.5 | -21.0 LUFS, LRA 23.4, TP -1.6, sample peak 0.832 |
| delivered mp3 | -19.8 LUFS, LRA 14.8, TP -1.5, limiter 2.8 dB | -19.8 LUFS, LRA 15.0, TP -1.6, limiter 2.8 dB, span 19.8 dB |
| attack probe | late or hole 0 | late or hole 0 |
| S outside 25 ms / 60 ms (my measure; critic A's on c12: 27 % / 6 %) | 836 of 2681 (31 %) / 188 (7 %) | 749 of 2679 (28 %) / 154 (6 %) |
| hall: G.P. drop at +0.3 s, 20 dB fall, RT60 | 20.5 dB, 0.30 s, 1.32 s | 20.7 dB, 0.27 s, 1.30 s (final chord 20.6 dB, 0.29 s, 1.32 s) |
| soft ends | 0.14-0.29 s | 0.14, 0.18, 0.31 (Violins II 444.5), 0.33 s (solo 1066.8): two over the 0.30 s limit by 0.01-0.03 s |
| returns re dry | -11.67 dB | -12.71 dB (R Strings -14.82, R Brass -25.03, R Winds -17.95, R Perc -27.79) |
| REAPER memory | 45 GB settled, 45 / 32 after | 45 GB settled; 49 GB during the second render (two instances rebuilt just before it), 50 GB / 27 compressed after |

S by track, share outside 25 ms / 60 ms, c12 -> c13: Violins I 34 -> 25 % / 6 -> 3 %; Violins II 31 -> 27 / 9 -> 10;
Violas 29 -> 29 / 5 -> 4; Violoncellos 44 -> 41 / 11 -> 9; Flute 1 18 -> 16 / 2 -> 3; Flute 2 38 -> 36 / 13 -> 12;
Oboe 1 22 -> 19 / 6 -> 2; Cor anglais 30 -> 25 / 9 -> 7; Clarinet 2 24 -> 19 / 4 -> 3; Clarinet 1, bassoons, horns and
trumpets within 2 points (`records/timing_notes_c12_c13.txt`, `timing13_c1*.txt`). The 25 ms goal is not reached: the
gain is 3 points. No printed note is silent; tempo: no unprinted change is left.

## Timing (critic A)

| finding | status | change | measured c12 -> c13 |
|---|---|---|---|
| A #4 unprinted tempo | accepted | `BEAT_STRETCH = {}` (22 beats, +0.53 s). Full build of every track on the new map. Re-bow points did not move (none lies in a stretched beat); per-onset tables are keyed by score onset; delivery rows are in qn | tempo map 364 -> 321 points; only printed tempos and the three `RAMP_SPANS` remain. Violins I re-bow dips 1.3 / 3.4 / 4.3 dB (c12 1.7 / 4.1 / 4.3) |
| A #1 theme head, two slurred eighths (Violins I, nine soft statements) | accepted in another form after a range test | three variants on one-track range renders of bars 13-28 (`rangetest/`): Leg Slur MAX targets (c12), "Slur Runs" (A's proposal), Sus Marc LITE (Movement I c54's one-row cure; only the eighths, the half note was on that row already). Adopted: Sus Marc LITE via `ART_SPANS` with 0.09 s `REATTACK_LEAD_AT`, level steps per pair, the second eighth ending 60 ms earlier (`NOTE_END_AT`), `_C13_V1_PAIRS = "marc"` | first eighth heard (dominant pitch) 180 -> 140 ms, second eighth 0 (0-44) -> 164 ms (124-176); second eighth's start +62 -> -2 ms (two at +28 / +30); two renders identical. Slur Runs failed: first eighth +55..+103 ms late and heard 0-70 ms, second 0-100 ms, and two renders of the same data differed. Open: the staccato quarter after the pair becomes the dominant pitch 40-62 ms after its beat (c12: 12-48 ms before it): the Marc LITE eighth rings under it; the second eighth still 7-11 dB over the half note's body at 53.5, 287.5, 773.5 |
| A #1 (4) celli fugato pairs 173 / 869 | accepted | `SHORT_SUS_LEG_AT` 173 / 869, `SHORT_SUS_LEAD_AT` 0.16 s at 173.5 / 869.5, +4 dB shape | S 173 +11 -> -76, 173.5 +101 -> -36, 869 -4 -> -52, 869.5 +102 -> -30: now early; halve the leads in c14 |
| A #1 (5) tutti pairs | accepted | `SHORT_SUS_LEAD_AT` 0.03 s (Violins I) / 0.045 s (Violins II) on the v100 pairs | median S Violins I -36 -> -6, Violins II -33 -> -17 |
| A #2 legato-row notes after another row | accepted as a generic rule | `LEG_HEAD_AFTER_ROW_LEAD_S` (new): strings A's per-onset values, default 0.10 s, capped at 0.3 of the previous note's written length; winds one value per track (Flute 1 0.035, Oboe 1 0.055, Cor anglais 0.05, Clarinet 2 0.055, Flute 2 0.05) with a 32 ms gap. 75 notes | winds, median S of the first slurred eighth: Flute 1 +36 -> 0, Cor anglais +54 -> -17, Clarinet 2 +58 -> -14, Flute 2 +69 -> -19, Oboe 1 +64 -> -43 (too early: 0.055 -> about 0.02 in c14). Strings: Violas 382 +181 -> +72, 387 +120 -> +78, 850 +186 -> -18, 855 +143 -> +55; bar 49 beat 1 (after an eighth pickup, lead capped at 34 ms): Violins I +143 -> +116, Violins II +135 -> +105, Violas +142 -> +139, celli +48 -> +22; Violins I 385.5 +45 -> +80 (worse). The bar-49 class needs the finale's cure (a Sus MAX stroke 0.06 s early, technique 49) |
| A #3 string joins | in part | `leg_leads.json` rows (`apply13.py`); caps lifted at Violins II 372 and the solo's 1052 / 1061.5; Flute 2 `LEG_ART_EXTRA_S` 0.03 | negative rows worked: celli 345 / 945 -69 -> -11, 844 -70 -> -11, 350 +60 -> 0, 880 +82 -> +12; Violas 150 -91 -> -11, 831 +97 -> +12; Violins II 848 -98 -> -28; Violins I 146 +66 -> -46. Positive rows held by the lead cap or the 100 ms minimum gap did nothing: Violins II 134, 159, 374, 387, 819, 840, 855, 372 and celli 171, 180, 207, 891 unchanged (+66..+180). Flute 2's joins in 912-960: median +29 -> +37, over 60 ms 11 -> 14 of 42 (0.03 s more lead did not help; a pitch-pair table is the next step). Celli trio tune: see the range test below |
| A #5 shorter staccatos | applied, no effect | `STAC_LEN_SPANS` 0.7 on trumpets, celli 972-1008, Violins II 984-996 | pair dips: Trumpet 1 median 2.2 -> 2.2, Trumpet 2 1.9 -> 1.8, celli 2.5 -> 2.3, Violins II 5.0 -> 4.9 dB. The short rows do not end at the note-off. Leave or remove in c14 |
| A #6 keyswitch lead | tested on one track, not adopted | new generic `KS_MIN_LEAD_S` (off). Celli trio tune (qn 504-552), paired range renders: data as is (A), keyswitch 0.15 s early (B), one legato row (C) | second render of each pair: A 14 of 30 joins outside 25 ms, 5 outside 60; B 16 / 6, and 10 of 30 joins differ from A by 25-70 ms; C all 30 joins 120-260 ms early (every lead on the line would need a refit). No gain from the early keyswitch on this passage. The first range render after each rebuild was useless (27-29 of 30 joins off by up to 400 ms) although it started 50 s after the build |

Not done from A: Flute 1's 120 ms lead at 1061 (it comes from the slur-start join rule, not a table), Violoncellos 840
(a re-attack on the legato row after a legato note: no rule reaches it), the four +3 dB second-eighth rows.

## Balance (critic B)

| finding | change | measured c12 -> c13 (K-weighted note levels) |
|---|---|---|
| B #1 hemiola | `LEVEL_SHAPES` Violins I -5 -> -8 (299.4-311.9), -2 -> -6.5 (901.05-911.9); delivery rows -2 -> -1.5 and -2 -> -0.5 | Violins I over Violins II at 300-310: 6.9..4.1 -> 3.9..1.0 dB; 906-910: 6.2 / 6.7 / 4.9 -> 1.7 / 2.4 / 0.4 dB. Master 100 ms peak at 908.5 -12.6 -> -15.4 (summit -12.0..-12.4). Master bars 303 / 304 -15.9 / -16.0 -> -17.8 / -17.3 (bar 305 -18.0) |
| B #2 pickups and heads | 155.5 -8; 204 / 888 -4.5; 383.5 / 851.5 -6 -> -3 (Violins II -9.5 -> -7.5) | pickup minus the note after: 155.5 +8.3 -> -1.3 (master +5.3 -> -0.5); 204 +5.7 -> +1.1; 888 +8.1 -> +3.7; Violins I 383.5 -0.9 -> +5.9 (its downbeat now starts a legato head 34 ms early and reads 2.3 dB lower; open), 851.5 -0.8 -> +0.1; master 383.5 +1.6, 851.5 +0.2 |
| B #3 timpani | `roles.json` `[23.5, 35.5, 7]`; first-stroke steps 288 +2, 291 +4.5, 294 +6, 297 +3, 720 +3, 738 +4, 744 +5 | strokes of bars 9-12 -50.8..-46.3 -> -43.8..-39.3; master bars 9-12 -52.0 / -55.4 / -50.6 / -50.8 -> -45.1 / -48.4 / -43.6 / -45.9 (bars 1-2 -44.4 / -42.8, bar 13 -39.1). First stroke against the next three: 291 -4.9 -> -0.3, 294 -6.5 -> -0.5, 297 -3.7 -> -0.7, 720 -2.9 -> +0.1, 738 -4.1 -> -0.1, 744 -6.4 -> -1.4 |
| B #4 Oboe 1 | roles `[386.8, 393, -4.5]`, `[854.8, 861, -4.5]`, `[147.8, 155.4, -3]` | Oboe 1 against Violins I at 387 / 389 / 391: 0.0 / -4.0 / +0.8 -> -4.7 / -8.6 / -3.8; over Flute 1 by 2.3-3.7 dB; step 386.5 -> 387 8.9 -> 8.2 dB (the quick notes are short; open) |
| B #5 trumpets | gains +2; roles `[1005, 1016.5, 2]`; Trumpet 1 A4 +3 on the sustain row | odd bars 105-111: Trumpet 1 10.3..9.5 -> 8.4..8.3 dB under Violins I; bar 337: Trumpet 1 14.7 -> 7.9 under, Trumpet 2 13.5 -> 9.5. Families at 1005-1014: strings -17.9, winds -20.3, brass -24.6 -> -23.2 (order holds); 300-312 brass -24.4, winds -26.5. Trumpets at 994-995.5 stay 5-6 dB under their 996-999. Fronts unchanged |
| B #6 | Flute 1 / Oboe 1 `[897, 900, -2 / -1.5]`; summit rows Oboe 1 -3 -> -1, Clarinet 1 -4 -> -2 | bar 300: Flute 1 -24.1 -> -26.4, Oboe 1 -26.3 -> -27.8; bars 336-338: Oboe 1 +1.9..+2.0, Clarinet 1 +1.9..+2.0 (now 1-3 dB over / under their seconds) |

## Blend (critic C)

| finding | change | measured c12 -> c13 |
|---|---|---|
| C #1a woodwind seats | `mix.json` seats (apply13.py) | stem L-R: Flute 1 +4.6 -> +2.2, Flute 2 +3.3 -> +1.5, Oboe 1 -5.2 -> -2.1, Oboe 2 -6.5 -> -2.9, Clarinet 1 +3.0 -> +1.8; K level of every wind stem within 0.3 dB of c12, so no make-up gain |
| C #1b oboe Main mics | deferred | no time left under the lock for a third one-track test |
| C #2 Stereo Double | adopted on the solo only | `build_reaper.py` `"stereo_double"`; range test: correlation 1.00 -> 0.93, L-R +5.9 -> +5.5 dB, level -2.5 dB (given back in the gain), bands within 0.4 dB, deepest 1/3-octave notch of the mono sum 3.1 dB. C's 0.60-0.90 is not reached at spread 0.4; 0.6 and Violas div are for c14. Solo soft end 0.33 s (limit 0.30) |
| C #3 wind send | `send_offset_db` R Winds 3.0 -> 1.5 | R Winds re its dry senders: -7.5..-10.6 -> -9.9..-13.0 (strings -11.2..-12.0): the winds are now 0.5-1 dB drier than the strings in the tutti and equal in the trio tune (-11.2) |
| C #4 return pans, harp seat | return pans 0.17 / 0.06 / 0.07 / 0.05; harp seats -0.45 | return L-R minus dry L-R, median: R Winds +1.40 -> -0.14, R Strings +0.34 -> -0.28, R Brass +0.40 -> -0.51, R Perc +0.31 -> -0.15 dB; master L-R +1.24 -> +0.98. Harp 216-240 L-R +5.7 -> +3.3 (500-1000 Hz +8.8 -> +5.7), its hall +11.1 -> +8.2 |

## ONE_TIME_c13 and coordinator notes

- Item 2 / 5: done above (S on 16 tracks; one value per track on the winds; tempo). Item 6: `END_LEG_KS = {}`.
- State guard: 0 stale at the start and after the full build; 6 stale after the first render (Bassoon 2, Contrabassoon,
  Horn 4, Violins I, Violas, Violoncellos), rebuilt; 2 stale after range renders (Flute 1, Violins I), rebuilt before the
  second render; 3 stale after it (Horn 4, Violins I, Violoncellos), rebuilt without playback; final save 0 stale.
- Horn 1 around bar 56 against the data with the removed note (`cycles/c12/before/parts.json`): no trim runs on, the
  next entry at 210 has the same velocity, lanes and lead; the note at 163 now ends 4.5 ms before the staccato at 165.
- Finale 46, 49, 43, 35-36 and Movement II's one-row method with a full lead refit: not used; first items for c14.
- Join notches (celli 506 / 570, Clarinet 1 459): their notes' leads did not change; peaks +4.5 / -1.6 / +3.4 dB as c12.
- Disk: deleting c12's stems and `Backups/` was refused by the session's safety check (a compound command with a
  relative glob); not retried. `cycles/c12/render/` still holds 2.8 GB of stems. Free space 96 GB.

## Research items

| item | status |
|---|---|
| EW template mix, returns, c08 EQ set, brass widths | adopted; changed with numbers: woodwind and harp Close seats (L-R table above), wind send +3 -> +1.5, return pans |
| unprinted tempo (batch 5 item 5, c07) | rejected: removed (Movement I / II: Dan heard the themes as out of time) |
| keyswitch lead as in EW's template (40-800 ms) | tested on one line, no gain; pending a paired test on row-change joins with resets (finale 46) |
| one row per string line (Movement I c54, Movement II c52) | adopted for Violins I's theme-head eighths (Sus Marc LITE); legato lines pending (needs a refit of every lead) |
| Slur Runs (MANUAL-GAPS, HO manual p.96-97) | rejected for eighths at quarter 264: late, weak, not repeatable |
| Stereo Double (HO manual p.141) | adopted on the solo at spread 0.4 |
| batch 6 #3, CC11 -> CC1 pass 2, separate legato tracks, timpani hard sticks | pending (memory) |
