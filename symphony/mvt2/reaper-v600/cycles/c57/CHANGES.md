# Cycle 57 (actor): instrument-side fixes after the c56 render; last cycle of the run

Owner's rule (Dan, 11 Nov; lead_c57.md): no per-note track volume move in any form. Fixes are on the instrument side
(CC11, CC1, CC7, velocity, row, region volume, note lengths, gaps, leads, doubling). A fault that cannot be fixed that
way stays audible and is listed below. Nothing in this cycle adds a per-note volume move.

The first actor did all the offline work on 15 Nov (19:22-22:19), took the lock at 22:17, found 21 GB free (under the
30 GB render limit), released it without starting REAPER, and stopped on a usage limit while waiting again. A second
actor took over on 16 Nov at 20:24. It checked the build against `before/` and `cycles/c56/build_fix/` (parts.json
regenerated at 22:19:38, identical to `build_pre/` from 20:01; no score_to_parts WARNING; the lead's three later notes
were already handled, see 1.1 / 1.7 / 2.3 below) and restarted the waiter.

To reverse: `cycles/c57/before/` holds every tool and build file as it was. `MVT2_C57_OFF=1` builds without the c57
block of `build/score_config.py` (with `cell_rows_c56.json` and the `before/` tables that gives the c56 parts.json);
switches `MVT2_C57_SHORT`, `_BURST`, `_ROWCC`, `_SF`. Table edits: `actor_scripts/edits57.py` (idempotent, from
`before/`), `actor_scripts/gen_cc57.py` (build/cc_shapes_c57.json).

## What was done (lead_c57.md numbering)
1.1 **Bow changes.** `REBOW_MAX_S, REBOW_SEG_S = 5.6, 5.0` (the Sus MAX / Leg Slur MAX loops run 1.93-5.90 s; basses
   1.81-5.78 s). Listed points removed or replaced (rebow_plan57.py: long pedals and the final chord in pieces of 3.1-5.4 s,
   staggered at least 0.25 s between sections). String bow pieces 97 -> 67 (the lead's estimate was 51; the final chord
   keeps 31 changes so no piece is longer than 5.4 s). Every printed bow change stays (checked in parts.json: Violins I
   295 / 298 / 301 / 302.75, Violins II 51 / 112 / 120 / 144 / 223 / 289 / 292, the Violas and celli 223, Violas div 79,
   Violins II div 114-120). Printed same-pitch repeats on held soft notes: `soft_gap_s_at` 0.04-0.05 s.
   `REBOW_CC_LIFT` hold 0.30 s, return 0.55 s, no pre-fall. The Violins II div double runs 286-304.
1.2 **Coda and final chord.** CC11 "set" lanes 33 -> 17 -> 8 from 298.3 on the violins, celli and copies (basses
   33 -> 22 -> 13 -> 8); CC7 span lanes on the doubled pairs and the basses (Violins I pair 127 over the first bow, 100,
   75 from 300.4; Violins II pair 115 / 90 / 68; celli 113 -> 68; basses 127 / 101 / 80); Clarinet 2 CC11 -5 from 300.5.
1.3 **Timpani.** Its whole volume envelope is folded into one CC7 lane (`ENV_TO_CC7`, 222 points, CC7 21-122), track
   gain +4 dB in mix.json, its six section rows become note levels inside the lane; velocities 64 / 60 / 60 in bar 84.
1.4 **Leads.** Bar 79 group leads Violins I 190 -> 225 ms, Violins II 150 -> 190 ms (not the critic's +75 ms: the run's
   last note would be cut to 54 ms); Violins II 252 -65 ms, Violoncellos 253 -30 ms; bar 47 fp: Violins II 148
   0.06 -> 0.20 s, Violas 0.13 s, basses re-attack lead 0.29 s. `SOFT_ENTRY_CC` holds to the score onset + 0.15 s and
   covers Sus MAX. Violas 168 and Violas div 79 are not fresh entries for the lead rules and keep their lifts.
1.5 **Section rows by cause.** 117 -> 39 (rows_log.txt): 33 under 1 dB deleted; the ff cells into `dyn_trim_db` "ff"
   (Oboe 1 -2, Flute 2 -2, Bassoon 1 -1, Bassoon 2 -3, Bass clarinet -1.6, Horn 1 -2.4, basses -2); four phrase
   decisions moved to roles.json (Violins II [274, 304] and [220, 238], Cor anglais [90, 108], Horn 2 [204, 220]);
   one- and two-note rows became flat CC11 offsets (Violins I 171 -8 and 237 -4, Violas 0 +3 and 220 +7, celli 0 -6,
   Bassoon 2 232 -8, Horn 1 17 -2), region gains, or went; Oboe 1's +4.7 row at 139 deleted; Flute 1 [262, 274]
   -6.1 -> -3.0 with the region gains; 11 rows refitted on the simulation on the c56 stems; Clarinet 1's row edge moved
   into its rest (261.5).
1.6 **Trombone 1.** Region volume row "Sus MAX" +2.5 dB; 213 CC11 head 124 -> 118, pickup 104 -> 110; 219.5 CC11 -4.
1.7 **Horn 1 bars 11-12** CC11 +4 on 34 and -2 on 32: half the critic's +8 / -3, because Movement I measured +6.5 dB for
   +8 units on Horn 1 (0.8 dB per unit, not the family 0.34). **Bar 62:** Violins I 208 on Sus MAX (`ART_SPANS`) with
   re-attack leads 208 / 210; basses G flat 1 +4 dB region volume on Sus MAX (196, 208; the pp G flat 1 at 146 is on Leg Slur MAX and is not touched).
2.1 **Short slurred notes** (critic B short57.json): flat CC11 offsets over each note, half the fitted size (celli +4,
   Oboe 1 +7, Cor anglais +5, Bassoon 1 +4, Flute 1 +4), consecutive notes sharing one plateau. One value per note for
   its whole length: a CC11 level, not a move.
2.2 **Region gains round two** (70 % of the c56 fit, pitches of 2 dB or more with one sign on c55 and c56): Flute 1
   eleven pitches, Violins I C5 -2 (legato rows), Violins II 61 -2.5, basses E flat 2 +3 / E flat 3 +3.5, Bassoon 1 56 +3,
   Bassoon 2 48 +3 / 51 +2, Cor anglais 56 -1.5 / 61 +2 / 65 +2, Clarinet 1 79 -2, Clarinet 2 68 +2, Bass clarinet 39
   +2.5. Not written (the simulation made the lines rougher): Violins II 65 / 72 and the celli 51 / 56 / 60. Every note
   each gain touches: region_gain_usage.txt.
2.3 **Bursts:** CC11 notches at the 11 legato transitions that burst 6 dB or more and were under 4 dB in c54 (critic A's
   table). All sit at CC11 35-92, under the 100-105 zone where Sus MAX is flat (finale note), so none is a deep cut there.
2.4 **Bar 63:** Bass trombone sf head by CC7 headroom (90 from the rest before 204, 127 on the head, a fall back over
   212.15-212.75) with a +3 dB slow row that switches in the same rest. Not on the Violas (no rest to switch the pair in).
2.5 `env_simplify_db` not changed.

Offline simulation on the c56 stems (sim.log, cmp_sim2.txt, deliver_sim.txt): no master bar more than 1.0 dB further
from c54 than c56; bars 2 dB or more off c54 4 -> 2 (bar 20 -2.3, 31 -2.3); delivered -19.8 LUFS, LRA 15.1, span 18.2,
limiter 1.9 dB. Envelope check on build/ (steps57.py): moves of 1.5 dB within 0.25 s inside a note 14 -> 3 (all three at
the final chord's morendo role end 303.7-303.8, -1.6 dB per 0.25 s); 2,244 points.

## Delivery at the shared loudness target (owner direction during the run)
Dan (16-17 Nov): "overall the tracks are too soft", then "-14 goal please". Shared spec (mockup-kit/README.md, "Shared
delivery loudness target"): -14 LUFS +-0.5, -1.0 dBTP (limiter ceiling 0.87), LRA about 12, short-term p10 -23 LUFS or
higher, printed climax order on the delivered file. `tools/deliver_master.py` now takes its target, ceiling, lift ratio,
knee, cap, top ride and momentary cap from build/mix.json "deliver" (or `DELIVER_*` environment overrides;
`DELIVER_OLD=1` gives the c56 delivery), prints the limiter load (50 ms windows over the ceiling by 1 / 3 dB) and the
momentary / short-term 10th percentiles, and can save the per-window load (`DELIVER_LOAD_OUT`) for a per-bar report
(`actor_scripts/limload57.py`). Climax order per bar: `actor_scripts/order57.py`.
Settings (mix.json "deliver"; written by edits57.py): target_i -13.6, tp_db -1.2 (ceiling 0.871), ratio 2.2, knee 7 dB
under p95 short-term, cap 10 dB, top ride 10 dB under p95 at 2:1, momentary cap 3, rise delay 0.6 s. Movement I's top
ride at 3:1 gave LRA 10.6 here and lifted bar 28 (the theme's f) level with the climax and over bar 79, so 2:1.
Limiter figures are pre-limiter sample peaks over the ceiling (what the limiter must take off that sample), so the
look-ahead alignment note does not apply to them. True peak is read on the encoded mp3.

| delivered file (same master: c57 render after the stem fix) | I LUFS | LRA LU | TP dBTP | limiter (loudest peak) | span p10-max S | short-term p10 | momentary p10 / quietest 10 % mean |
|---|---|---|---|---|---|---|---|
| mvt2-mockup-c57.mp3 (new target) | -14.3 | 12.0 | -1.1 | 6.6 dB | 13.2 dB | -21.0 | -22.0 / -25.5 |
| mvt2-mockup-c57-oldlevel.mp3 (c56 settings) | -19.8 | 14.8 | -1.6 | 2.1 dB | 18.0 dB | -28.3 | -29.2 / -32.8 |

Limiter load on the new file, per bar (dB over the ceiling, max; seconds over 1 / 3 dB): bars 61 6.0 (4.0 / 1.6 s),
62 6.0 (3.5 / 1.4), 63 6.6 (0.7 / 0.4), 60 3.9 (1.3 / 0.2), 79 4.3 (1.7 / 0.2), 47 4.8 (0.2 / 0.1, the fp), 64 3.0,
78 3.1, 28 3.0; everything else under 2 dB; the final chord 7.7 dB under the ceiling (untouched). 4.0 s of the file are
limited by more than 3 dB, all in the climax (bars 60-64) and three single peaks. Climax order (momentary max per
bar): new b63 -7.3 > b61 -7.4 > b62 -7.5 > b79 -7.9 > b60 -8.1 > b80 -8.4; old b63 -9.0 > b62 -9.1 > b61 -9.3 > b79
-10.7: the printed order holds (climax bars 61-64, then the ff cadence 79-80), but the climax now stands only 0.6 dB
over bar 79 (1.7 dB at the old level). Quiet passages come up 6.3-7.3 dB, the climax 1.5-1.8 dB.

## Session
Lock (shared turn rule): the first actor's waits on 15 Nov (2 h 10 min, then a 2-minute hold at 22:17-22:19 released for
lack of disk); the takeover's waiter 16 Nov 20:27 -> killed with the session tasks after mvt1 c60 took its turn
(21:00); restarted 17 Nov 04:51 with the finale's c19 waiter (start-time comparison), detached. **Held 05:22:33-06:12:08
(49.6 min).** s1: guard (0 stale), start / open / settle (37 GB), audio init, `--midi-only` on 21 tracks (11 full
rebuilds), `--mix-only` on all, save, guard 0 stale. s3: restart, settle; render_cycle.py refused (29 GB compressed,
limit 6). The `--force-memory` rerun was not allowed by the permission system, so REAPER was restarted again
(39-40 GB, 0 compressed) and the render ran without an override (05:59-06:07, probe 0). Stem fix (two basses rows,
below), `--mix-only` on every track, save, guard 0 stale, quit, unlock. REAPER after the render 40 GB, 0 compressed.
Disk 57 GB free before, 53 GB after. Every bridge job's .lua is in this folder.

## Measured (c57 render after the stem fix, against c56 / c54)
- Master: -23.5 LUFS, LRA 23.5, TP -4.2 dBFS (c56 -23.3 / 24.2 / -4.1). Attack probe 0.
- Master bars 2 dB or more off c54: 4 -> 2 (bar 20 -2.2, 31 -2.3; bars 84 and 92 fixed); no bar 1.0 dB further from c54
  than c56. Bar 92 -2.9 dB against c56 (c56 was +2.1 over c54).
- Coda (half beats, master): falls 298-301.5, one 1.1 dB rise at 302.0 (c54 has one at 301.5), then -53.1 / -54.3 / -58.2;
  the last beat 2.3 dB under c54 (the target was within 0.5 dB: overshot by the CC7 / CC11 lanes plus the basses' refit).
- Envelope: 2,245 points; moves of 1.5 dB within 0.25 s inside a note 14 -> 3 (the three are the final chord's morendo
  role end on basses / violas / Violas div, -1.6 dB per 0.25 s); section rows 117 -> 38.
- Bow changes (string pieces) 97 -> 67. rebow53: re-bows over the 3 dB "after" limit 28 of 37 -> 23 of 24. With the
  doubles (chk57): Violins I median 6.4 -> 4.1 dB, Violins II 7.8 -> 3.6, celli pair 0.9; Violas 5.4 -> 4.2; the new
  coda pieces of Violas div (7.4 / 6.2 at 293 / 296), basses (4.1-7.7; 276.97 7.7) and Violoncellos div (5.2-9.7;
  282.14 9.7) dip more than c56 did at those times (they had no change there), medians 4.4-6.2 dB.
- Joins: holes of 6 dB or more 360 -> 351 (9 dB: 126 -> 130), peaks of 3 dB or more 213 -> 199 (6 dB: 40 -> 36), soft
  starts 294 -> 278, dips in unmarked long notes 235 -> 216; joins with a master bump 25.
- S within 60 ms: 707 -> 702 of 727 (did not hold). Bar 79 B flat: Violins I +80 -> -75 ms, Violins II +81 -> -70 ms
  (the lead overshot: 35 / 40 ms of lead moved S by 150 ms); celli 156-202 now read 40-70 ms early (they were within
  25 ms; cause not found: their leads did not change; the 153 / 165 re-bows went).
- Timpani: bar 84 back on c54 (277 / 278.5 / 279: -0.3 / 0.0 / +0.2 dB against c54); 172 stroke +4.1 over c54 front.
- Trombone 1: 213 +2.6 dB over its pickup (target 1.5-2.5); 216 within 0.1 dB of c54; 218 front +4.5 over 217.5
  (target 1.5-2.5: hot).
- Horn 1 bars 11-12: 34 +0.6 dB, 32 -0.3 dB against c56 (aim +2.7 / -1): CC11 +4 / -2 is too small here; 34 still
  1.1 dB under c54.
- Bar 62: Violins I 208 -25.3 (c56 -28.7, c54 -25.4); basses 196 / 208 +5.4 / +4.0 against c56 (+3.6 / +1.3 over c54);
  master 208-209 still 1.4-1.5 dB under c54.
- Bar 47 fp: the fronts now start 0.1-0.2 qn before the beat (Violas -36 dB at 147.8 against -47 in c56) and the join
  peaks rose (Violins II 148 12.2 -> 18.7 dB, Violas 12 -> 17, basses 11.9 -> 15.6): the new leads (0.20 / 0.13 /
  0.29 s) are too long.
- Short notes: Flute 1 129-133.5 +1.5 to +2.9 dB, Cor anglais 131.5 / 133.5 / 134 +2 to +3 dB, celli 240 / 248 +0.9 / +2.0;
  Cor anglais 131.5 still 4.6 dB under c54.
- Row replacements by CC11: Bassoon 2 232 / 235 +2.1 dB against c56 (the -8 CC11 gave about -2.3 dB of the -4.4 row),
  Violas 220 -1.4 dB (+7 CC11 gave less than the +3.7 row), Violins I 171 +0.5.
- Line steps worse by more than 0.4 dB: Violoncellos 45-47 3.55 -> 4.60, Violins I tutti 61-64 1.98 -> 4.13, Bassoon 1
  71-78 4.12 -> 5.24, Flute 1 79-82 3.04 -> 4.50, basses coda 1.96 -> 3.10, Violas div coda 5.51 -> 6.66.
- Wetness and band shares: unchanged within 0.1 dB except the basses' octaves (56-112 Hz share -11.1 -> -10.6).
- Stem fix after the render (`fix57.sh`, refit57.py on the render's cells): basses [274, 286] -1.9 -> -2.7, basses
  [286, 304] +1.4 deleted (under 1 dB after the refit); written to REAPER with `--mix-only` inside the session.

## Hidden inner lines (for the next run's critics; not changed this cycle)
Dry stems, 150 Hz-6 kHz, mean power while the line sounds, against the loudest stem of the bar (`inner57.py`; full list
`inner_c57.txt`, the lines the critics name `inner_named_c57.txt`):
- Violas' pizzicato triplets, bars 37-44: 9-14 dB under Flute 1 / cor anglais (12 onsets per bar).
- Harp arpeggios under the horn theme, bars 7-14: 12-19 dB under Horn 1; bars 37-43 13-21 dB under the flute.
- Bassoons and bass clarinet, bars 8 and 11: 14-20 dB under Horn 1.
- Double basses' pizzicato, bars 41-43: 24-27 dB under the cor anglais (bars 24, 27, 72, 75 arco: 12-14 dB under the line).
- Violas bars 16, 49, 51 (12-15 dB under Oboe 1 / cor anglais); Violins II / Violins II div bar 39 (15 dB under Flute 1).
- Clarinet 1 bar 54 (12 dB under Violins I); Flute 1 bar 58 (14.5 dB under Horn 1).
- Strings and Bass trombone under Trombone 1's quotation, bar 64 (18-25 dB).
- Not buried: the celli's counter-melody (bars 23-30, 71-78: 0.3-2.9 dB under the violins) and Horn 1's counter-melody
  (bars 53-60: 2-3 dB under), though Horn 1 53-60 reads -6.9 dB as a solo margin.
The fix is a balance job (roles over a phrase, CC11 phrase lanes, region volumes), not the delivery.

## Rejected or deferred
- 2.5 `env_simplify_db` 0.2 -> 0.5: not done (last in the drop order).
- Critic A #2 leads for Violas 168 and Violas div 79 (not fresh entries for the lead rules).
- Region gains Violins II 65 / 72 and celli 51 / 56 / 60 (simulated rougher, as in c56).
- Bar 63 Violas sf by CC7 (no rest to switch the pair in).
- Inner-line rows: no session time after the render, and the named counter-melodies are not buried.
- Section 3 of lead_c57.md (basses' pulse lane, horn L/R phase, mono copies, legato velocity, CC68, `leg_sus_attack_scale`,
  violas' pizzicato): not this cycle.

## Faults left audible (no per-note volume move goes back)
| fault | where | size | instrument-side fix to test |
|---|---|---|---|
| bar 79 B flat early | Violins I / II 262 | S -75 / -70 ms (c56 +80 / +81) | leads about 205 / 170 ms (half way back) |
| bar 47 fp early and hot | Violins II, Violas, basses 148 | fronts 0.1-0.2 qn early; join peaks +4 to +6.5 dB | leads 0.12 / 0.08 / 0.18 s |
| celli early | Violoncellos 156-202 | S 40-70 ms early | find the cause (no lead changed) before refitting |
| Trombone 1 218 hot | bar 64 | +4.5 dB over 217.5 (aim +1.5 to +2.5) | 218 CC11 head down 6-8 units, or 217.5 CC11 up |
| Horn 1 bar 12 crescendo flat | 32-34 | 34 +0.6 dB of the aimed +2.7 | Horn 1 own CC11 curve at 40-60 measured on a range pass |
| new coda re-bow dips | Violas div 293 / 296, basses 276.97, Violoncellos div 282.14 | 6.2-9.7 dB | stagger against the doubles, or no split under 5.6 s on the copies |
| re-bows without a double | Violas, basses, Violas div | medians 4.2-6.2 dB | a second basses instance; CC68 Legato script |
| coda end too low | bar 92 last beat | 2.3 dB under c54 | CC7 floors 75 / 68 -> about 85 / 78 from 300.4 |
| climax close to bar 79 on the delivered file | bars 61-63 vs 79 | 0.6 dB (old level 1.7) | dynamic trims: ff cadence down 1 dB in the mix |
| delivery limiter on the climax | bars 60-64 | up to 6.6 dB on peaks, 4 s over 3 dB | find the crests (pre-limiter peaks at 224.8, 231.0, 231.5, 232.6 s) and lower them in the mix |
| line steps | Violins I tutti 61-64, celli 45-47, Bassoon 1 71-78, Flute 1 79-82 | +1 to +2 dB median step | per-note reading on the c57 stems |
| soft starts of 6 dB or more | 60 | | `leg_sus_attack_scale`, longer entry lifts |
| hidden inner lines | list above | 9-27 dB under the leading line | roles / CC11 lanes / region volumes |
| Horn 1 / Horn 3 L/R phase | B flat 4, A flat 4 (bars 12, 57) | mono loss 2.4-8.2 dB | Opus Channel Routing "Mono From Left" or Close / Main balance |
| basses' A flat 1 pedal pulse | inside the sample | | CC11 counter-lane on a basses-only range pass |

## State at the end of the run
- **Envelope:** 2,245 points over 32 tracks; one class only ("slow": roles over three notes or more, 38 section rows in
  build/cell_rows_c57.json, hairpin gains, dynamic trims with `env_edge_slew` 3 dB/s, fade). No per-note item, no level or
  shape class. Three fast moves inside notes remain (final-chord morendo role end at 304).
- **Instrument-side mechanisms in the tools** (tools/score_to_parts.py, tools/build_reaper.py; values in build/):
  `REBOW_MAX_S` / `REBOW_SEG_S` and `REBOW_AT` lists (bow split), `STR_REP_NEW_BOW` `soft_gap_s_at` (printed repeats),
  `REBOW_CC_LIFT`, `SOFT_ENTRY_CC`, `TRACK_DOUBLES` (interleaved re-bows on idle divisi instances, per-span CC7),
  `CC_SHAPES` / `CC_SHAPES_S` (CC lanes in qn / seconds from the moved note-on; build/cc_shapes_c57.json for row
  replacements, short-note lifts, burst notches), `ENV_TO_CC7` (timpani envelope as CC7), `ART_SPANS`, `GROUP_LEAD_AT`,
  `REATTACK_LEAD_AT`, leg_leads.json / entry_leads.json, `VEL_SET` / `TIMP_VEL`, `region_gain_db` (pitch and row levels
  as Opus region volumes, build/mix.json; usage per note in region_gain_usage.txt), `dyn_trim_db` per dynamic,
  `env_edge_slew`, the delivery settings in mix.json "deliver".
- **Open tests, in priority order:** (1) bar 79 and bar 47 leads (halve the c57 change); (2) the celli's early S at 156-202;
  (3) Trombone 1 218 and Horn 1 32-34 CC11 sizes from each track's own curve on one range pass; (4) the new coda re-bow
  pieces on Violas div / basses / Violoncellos div; (5) coda floor (CC7 75 / 68 up about 10 units); (6) climax against bar
  79 and the limiter load at the climax on the delivered file (dynamic trims, climax crests); (7) hidden inner lines,
  starting with the violas' pizzicato triplets 37-44 and the harp 7-14 (slow roles or CC11 phrase lanes); (8) section
  3 items of lead_c57.md.
- Files: `tools/deliver_master.py` (delivery settings, limiter load); build/: score_config.py (c57 block), mix.json,
  roles.json, leg_leads.json, entry_leads.json, rebow_fills.json, cell_rows_c57.json, cc_shapes_c57.json, parts.json.
  Session scripts `actor_scripts/` (wait_lock.py from the finale c19, run57.sh, session57.sh, s1/s3/s4, rerender57.sh,
  tail57.sh, fix57.sh, edits57.py, gen_cc57.py, inner57.py, order57.py, limload57.py). Logs: s1.log, s3.log,
  rerender.log, render.log, s4.log, session_status.txt, lock_wait.log, fix57.log, post_fix_full.log, chk_final.txt.
  `render_first/` holds the stems the stem fix replaced.
