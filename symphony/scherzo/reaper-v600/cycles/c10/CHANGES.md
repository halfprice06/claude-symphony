# Cycle 10: changes (actor, on the c09 render)

Snapshot in `before/` (tools, score_config, build JSONs, and the previous `parts.json`). Scripts in `actor_scripts/`:
`apply10.py` (per-note tables: roles, note trims, pitch trims, accent fits, entry leads, the A #4 revert), `mix10.py`
(mix.json; run after `mix09.py` when regenerating mix.json), `check10.py N [parts.json]` (one block per c10 change;
`check_c09.txt` / `check_c10.txt`), `tone10.py` (correlation, side/mid and band shares of a master), `ndiff10.py`
(note-level parts.json diff). The data that rendered is in `build_render/` (before the stem fix).

STATUS: rendered 2026-11-09 12:48-12:57, checked, one stem fix. Lock held 12:13:58-13:02:51 (48.9 min; about 25 min of
it waiting for REAPER to settle from a cold cache). mp3: `cycles/c10/scherzo-mockup-c10.mp3`.

## 1. Critics' findings

Numbers are c09 -> c10 (after the stem fix), from `check10.py` on both renders. Plain RMS unless "K".

| finding | status | change | measured c09 -> c10 |
|---|---|---|---|
| orchestrator: revert c09 A #4 | done | entry_leads celli 504 0.12 -> 0.06, basses 504 / 1071 removed, celli early fill 504 removed, VEL_SET basses 53 removed | celli 504 pcX +367 -> +263 ms, basses 504 / 1071 +166 / +164 -> +144 / +144 (back to c08) |
| B #4 celli spike at 506 | adopted | note trim 506 -3 as a step, with the revert | spike over body +14.7 -> +9.0 dB; master bar 169 -28.8 -> -34.7 (bars 170-172 -36.0; target within 2 dB: met) |
| B #1 coda build (329-333) | adopted | new generic HP_CURVE `cresc_long` {min_qn 10.5, pt (0.6, 0.35)}: crescendos of more than 3.5 bars rise late (the 9 qn sfp < hemiolas at 300 / 900 are left on the old curve: with min_qn 9 they changed legato velocities, leads and lengths in the tutti hemiola); roles Horns 3-4 -4 over 990-995.8, Horns 1-2 -3 over 993-995.8 | K bar 331: Oboe 2 -27.0 -> -39.2, Clarinet 1 -30.2 -> -36.0, V1 -30.4; Horn 3/4 bar 332 -33.8/-33.7 -> -37.9/-37.7 (V1 -30.0). Master 329-333 -27.3 / -26.7 / -25.6 / -22.0 / -18.5, rising. Wind bar 333 >= bar 332: Oboe 2 and Clarinet 2 yes, Clarinet 1 / cor anglais 2.4 / 3.2 dB under (summit roles from 996, left) |
| C #1 one-beat swells | adopted + stem fix | `HP_SHORT_KINDS = ("decresc", "cresc")` (CC step capped at 6); the CC cap moved the stems only 0.3-2 dB, so the stem fix added LEVEL_SHAPES over each crest: Horn 1 440.2-442.3 -2.5, Clarinet 1 471-474.3 -3.5, Horn 3 1028.2-1030.5 -3 | rise over the note before: Horn 1 +9.3 -> +4.8 dB (441 -36.1, target <= -35.5), Clarinet 1 +9.3 -> +5.2 (-36.4, target <= -36), Horn 3 +8.9 -> +5.0 (-40.5, target <= -40.5), V1 542 +4.8 -> +4.5; master bar 148 -33.2 -> -36.0 (target <= -36) |
| C #2 second idea's < on the accent | adopted | accent_fits 4.5 -> 1.0 at V1 / V2 132 and 360, violas and celli 132; LEVEL_SHAPES on the four string sections 133-141 (0 / +2 at 136-137 / 0) | V1 arrival minus accented note: 132 -3.9 -> +1.6 dB, 360 -0.2 -> +3.3; master < at bar 45 -0.3 -> +2.7 dB, bar 121 -1.8 -> -0.3 |
| C #3 Horn 1's last G sharp | adopted | new generic `HP_DEC_HOLD_HELD` (a decrescendo arriving inside a sounding note holds its gain to the note's end); LEVEL_SHAPES -2.5 dB over 1123.5-1126 for the sample's own swell | Horn 1 1122 -> 1126 +4.6 -> +2.1 dB; master bar 376 -46.1 -> -47.0 (bar 375 -44.2, target 1 dB under: met) |
| C #4 harp hairpins (manual p.69) | adopted | HP_GAIN_SOFT_DB harp 3.0, HP_SOFT_EXTRA_SPANS Harp 216-240, HP_SOFT_GAIN_AT 216 / 228 +4 | harp per bar 216-240: -40.7 -41.5 -39.6 -37.9 -37.4 -39.5 -40.6 -37.7 -> -38.4 -39.5 -39.6 -37.9 -36.7 -37.3 -37.4 -37.7: the > bars now hold instead of rising, the crests are 1-2 dB, under the 2.5-4 dB target (velocity cap 56 kept) |
| C #5 timpani roll 205-208 | adopted | the c02 -3 dB over 621-624 removed; -3 dB ramp over 612.5-617.5 against the roll's own build | 612-617 -51.3..-47.9 (+3.4) -> -51.4..-50.3 (within 1.1 dB); 618-623 +2.2 -> +5.2 dB, still 2.4 dB under the violas at 622-623 |
| B #2 hot wind pitches | adopted | pitch trims Oboe 2 F5 -4 (all arts), cor anglais A4 -3.5 (Sus / Leg Slur), Oboe 1 A5 -3 (Stac DblTng) | K: Oboe 2 990 -26.4 -> -42.3 (987 -44.2, 993 -35.6); 903 Oboe 2 -27.9 -> -31.9 (Oboe 1 -36.0: still 4 dB over); CA 327 -28.6 -> -31.3 (7.3 under V1); bar 41 Oboe 1 - Flute 1 +8.3 -> +6.5 (open) |
| B #3 Trio 221-223 | adopted | roles Horn 1 -5, Horn 2 -2 over 660-669.5, Flute 1 -2 over 660-669 | K bar 221 Horn 1 -35.9 -> -41.4 (V1 -34.8); bar 222 Flute 1 -33.1 -> -36.9 (V1 -33.2) |
| B #5 reprise violas pizz. | adopted | roles Violas +4 over 756.5-810, note trims +3 on the beat-2 onsets (steps) | K beat-2 note level Violas -59.7 -> -52.7 (Violins II -51.2) |
| A #1 flute staccato note-off | partly | new generic 4-tuple STAC_LEN_SPANS (lengthen, reading the written value from the event list, ending STAC_LEN_NEXT_GAP_QN 0.5 before the next onset), flutes (0, end, 0.85, 1 qn). With a 0.02 qn margin the following notes lost 0.09 qn of lead (WIND_DETACH gap), so only quarters before a rest lengthen (Flute 1 18, Flute 2 5) | median note-off step Flute 1 7.6 -> 5.8 dB, Flute 2 7.3 -> 7.3 (target 3.5 not met; the quarters followed by a note are unchanged) |
| A #2 Flute 1 sfp 900 | adopted, no effect | VEL_SET 900 118; +0.03 s entry lead (entry_leads.json; REATTACK_LEAD_AT does not apply after a rest) | Flute 1 sf-to-p drop 6.9 -> 7.1 dB (target 8). Finale item 13 (post-fader sf bump) carried to c11 |
| A #3 horn tenuto repeats 624-666 | adopted, short of target | NOTE_END_AT Horn 1 627 / 630 / 660 (63 ms before the Port Lng re-attack), Horn 2 624 / 639 / 648 (0.10 s gap) | dips Horn 1 630 / 633 / 663 -1.8 / -1.5 / -2.7 -> 1.6 / 1.7 / 1.7 dB; Horn 2 627 / 642 / 651 1.3 / 1.1 / 0.2 -> 2.6 / 3.6 / 1.9 (657 6.0 both); target 3-6 |
| A #4 celli trio tune velocity (MANUAL-GAPS #8) | adopted | LEG_VEL_SPANS celli 504.5-552 v80; LEG_VEL_EXTRA_S celli (85, 0.03 s) | celli 506-552 pcX median -63 -> -19 ms (IQR -139..+46); probe celli window 66 -> 65 ms, robust SD 53 -> 49 |
| A #5 Flute 2 low unison eighths | adopted | note trims -5 at 121 / 121.5 / 127 / 127.5 / 817 / 817.5 / 823 / 823.5 (steps); RR_RESET_AT Flute 2 817 | Flute 1+2 sum pair dips 2.3 / 12.5 / 6.8 / 5.9 -> 4.3 / 4.1 / 5.6 / 7.6 dB (all >= 3) |
| A #6 V1 heads 51 / 75 | adopted + stem fix | VEL_SET 53 / 77 100; note trims +3, raised to +5.5 in the stem fix | first eighth vs the next quarter 51 -11.1 -> -6.0, 75 -9.8 -> -6.5 dB (target -6); 39 / 285 / 759 unchanged |
| orchestrator: hall at 444.5 | done | Harp harmonics back to R Perc -8.77 (the harp profile's level; R Strings off) | soft end V2 444.5 0.71 -> 0.29 s; G.P. +0.3 / +0.6 / +1.0 s 20.4 / 31.3 / 46.7 dB, RT60 1.34 s; final chord 20.6 dB, RT60 1.44 s; other soft ends 0.13 / 0.14 / 0.16 s |

Rejected or deferred: none of the critics' findings were rejected; A #1, A #2, A #3, C #4 and B #2's Oboe 1 A5 and
Oboe 2 at 903 remain short of their targets (above).

## 2. ONE_TIME (finale SHARED-TECHNIQUES items 1-12, Movement I c51)

Measured on the c09 master with `tone10.py` (Dvořák 9/i reference in brackets): correlation below 250 Hz 0.63 (0.56),
250 Hz-5 kHz 0.53 (0.56), side/mid -5.2 dB (-5.3); shares 40-100 Hz -18.9 (-21.8), 250-500 -6.3 (-6.2), 280-355 -11.8
(-12.3), 500 Hz-1 kHz -6.5 (-5.9), 1-2 kHz -5.9 (-7.2).

| item | result |
|---|---|
| 1 low-end width (side 60 Hz shelf + 180 Hz bell) | rejected: our low end is already as narrow as the references (0.63 against 0.54-0.62); more side cut would make it narrower |
| 2 brass track_width | adopted: `track_width` ported into `tools/build_reaper.py` (D_WIDTH, default 1.0, full build and --mix-only); trumpets 0.5, trombones 0.6, reaper_pan raised by 0.075-0.155 so each stem keeps its balance (simulated on the c09 stems). Measured: stem R/L balance within 0.05-0.6 dB of c09, L-R correlation 0.50-0.64 -> 0.81-0.89 |
| 3 low-mid cuts (horns / violas 315 Hz) | rejected: our 280-355 Hz share is 0.5 dB over the Dvořák (the finale's excess was 5.8 dB) |
| 4 FINAL_RING | skipped: our close is Horn 1 alone; ringing 0.45 s past the end would break the 0.30 s soft-end limit (final chord drop 20.6 dB at +0.3 s, RT60 1.44 s) |
| 5 RR reset before ostinatos | skipped: a reset at both tutti statements (312, 912) would replay the first statement's samples in the second, which c08 removed (identical attacks 29 -> 2 of 38) |
| 6 sub. p "drop" / HELD_DECRESC_CARRY | not needed: critic C checked no positive phrase offset at 360 / 828 and the hall decays under both |
| 7 template EQ tone (1 kHz cuts) | rejected: 500 Hz-1 kHz is already 0.6 dB under the reference; a 1 kHz cut would deepen it |
| 8 basses' high-pass 53 -> 35 Hz | rejected: 40-100 Hz share already 3 dB over the reference (critic B: tuttis 20-100 Hz -20.2 / -18.9 against -21.7) |
| 9 hall | no change beyond the harp harmonics routing |
| 10 wind phrase shapes x1.4 | adopted: new PHRASE_SHAPE `family_scale` (off by default), winds 1.4; not measured separately (moves a wind's rise about 0.4 dB, Movement I c51) |
| 11 checks | inner held notes Horns 3-4 under Clarinet 1 456-504 -53.5 / -50.2 against -38.8 (unchanged); string repeat dips on the master: A #5 above |

Finale items 13-17 arrived during the render (the build was already in REAPER): written to `loop/ONE_TIME_c11.md`.

## Research items

| item | status |
|---|---|
| EW template mix (c06), returns and sends (c07-c09), c08 EQ set | adopted, unchanged |
| finale SHARED-TECHNIQUES 1-12 | 2 and 10 adopted; 1, 3, 7, 8 rejected with numbers (above); 4, 5 skipped with reasons; 6, 9, 11 checked |
| finale SHARED-TECHNIQUES 13-17 | pending, `loop/ONE_TIME_c11.md` |
| batch 6 #3 shared curves, CC11 -> CC1 pass 2, separate legato tracks | pending (memory / pass 2) |

## MANUAL-GAPS

#8 (slower legato velocity for cantabile lines) tried on the celli trio tune: see A #4 above; result recorded in
`loop/MANUAL-GAPS.md`.

## Tool changes (generic, off by default unless noted)

- `tools/score_to_parts.py`: HP_CURVE `cresc_long`; `HP_DEC_HOLD_HELD`; 4-tuple `STAC_LEN_SPANS` (lengthen, written
  value from the event list) with `STAC_LEN_NEXT_GAP_QN` 0.5; PHRASE_SHAPE `family_scale`.
- `tools/build_reaper.py`: mix.json `track_width` (D_WIDTH; default 1.0).

## Render

Steps: lock at 12:13:58 (no other waiter; mvt3 c10 had just released), start, open (Opus log
`Opus.g3log.20261109-121553.log`: 0 "Interrupted system call"), full build of all 31 tracks plus returns (64 s, all
states set), restart (open 2.5 min), cold-cache load to 45 GB settled by 12:46 (38 GB compressed; other processes:
CrashRestartHelper 6.4 GB, Steam 7.8 GB, java 3.6 GB), audio_init (48000 / 512, no input), `render_cycle.py 10
--force-memory`. Stem fix (C #1 shapes, A #6 trims) with `stem_fix.py 10 build_render build --apply` on Horn 1,
Clarinet 1, Horn 3, Violins I; the same data written to REAPER with `--mix-only`; save; `render_cycle.py 10
--measure-only`; quit; unlock 13:02:51.

Memory: 45 GB settled (38 GB compressed) before the render, 45 GB (32 GB compressed) after.

Master -21.0 LUFS, LRA 23.1 LU, true peak -1.2 dBFS (sample peak 0.874; c09 -20.8 / 23.2 / -1.6, 0.828). Delivered
-19.8 LUFS, LRA 14.8 LU, TP -1.6 dBTP, limiter about 3.3 dB, span 19.6 dB (c09 -19.8 / 14.7 / -1.5 / 2.7 / 19.6). The
loudest master sample is at the same summit moment (241.5 s) with the same stem peaks as c09; the rise is in the sum
(inferred: the narrowed brass add more in phase). Limiter 0.3 dB over the brief's "about 3 dB": open. Band shares 2-6
kHz -9.56, 6-20 kHz -28.8 dB (unchanged). Attack probe: no late or hole; legato windows / robust SD Violins I 64 / 44,
Violins II 80 / 45, Violas 88 / 76, celli 65 / 49 ms, all ok.

Disk: deleted `cycles/c10/render_first`, `cycles/c09/render_first`, cycles/c09's stems and return stems (kept its
00_Master.wav and mp3) and `Backups/`. cycles/c08/render still holds its stems (2.8 GB; c09's deletion was refused and
this cycle was not asked to delete it). 54 GB free after.
