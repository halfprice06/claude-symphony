# Cycle 18: changes (actor, on the c17 render)

STATUS: **rendered once**, on 2026-11-17 at about 06:40 CST, from a freshly restarted REAPER.
- Delivered at the shared target (-14 LUFS).
- mp3: `cycles/c18/scherzo-mockup-c18.mp3`, 279.75 s, md5 f976607e01693e56dd1ab0e36f90366a.
- Data as rendered: `cycles/c18/build_render/`.
- After the render: ride rows for the delivery (`cycles/c18/build_fix/`), then two data fixes for c19 that are not rendered (end of `score_config.py`). `build/` is therefore one step ahead of the render.

Lock and queue:
- The first attempt queued from 16 Nov 21:05 and stopped at 04:48 with the work prepared. The finale's c20 actor held the lock idle from 22:55 to 05:22.
- Resumed at 05:23 behind Movement II. Lock held 06:12:11-06:45:30 (33 min): open, settle, full build, restart, settle, guard (0 stale), audio_init, render. No range tests (not enough lock time).
- After quit, the saved project holds 5 stale Opus states (`records/state_guard_final.txt`). c19 must rebuild them first.
- REAPER memory: 43 GB settled with 0 compressed; 43 GB with 11 GB compressed after the render.
- Leads: Movement II c57 found that a full correction overshoots, so critic A's 14 lead values were each moved by half the S error before the build.

## Result

| | c17 | c18 |
|---|---|---|
| master | -21.7 LUFS, LRA 22.5, TP -3.0 | -21.5 LUFS, LRA 22.6, TP -2.7, sample peak 0.731, no clipping |
| attack probe | late or hole 0 | late or hole 0 |
| delivered loudness | -19.8 LUFS, LRA 14.3, TP -1.6 | -14.1 LUFS, LRA 12.0, TP -1.3 dBTP (measured on the mp3) |
| delivered short-term | p10 -29.0 LUFS, span 19.4 dB | p10 -21.7 LUFS, span 14.2 dB |
| delivery limiter | 1.6 dB | 5.5 dB (the summit) |
| limiter per passage (max gain reduction, look-ahead aligned) | | summit 5.5, tutti 105-120 3.9, tutti 305-320 2.8, bar 72 2.8, bar 300 2.4, final chord 0.1 dB |
| climax order, master (momentary max per bar span, `order18.py`) | summit 0.2 LU over the tutti | summit -11.5, bar 304 -13.2, bar 300 -13.7, tutti 105-120 -13.8, tutti 305-320 -13.9, bar 72 -15.3, bar 333 -15.4, bar 53 -16.2, trio ff -17.2: the summit leads by 1.6 LU |
| climax order, delivered mp3 | (c17 at the new target: summit -0.0 LU, tied with the first tutti) | summit -7.1, bar 72 -7.8, bar 53 -7.9, tutti 305-320 -8.0, trio ff -8.0, bar 333 -8.0, tutti 105-120 -8.3, bar 300 -8.3, bar 304 -8.5: the summit leads by 0.7 LU. Without the new ride rows it led by 0.1 LU (bar 72 -7.4, trio ff -7.1) |
| bar 72 / 300 over the bar before (master) | -2.9 / -3.9 dB | +2.4 / +4.0 dB; bar 300 is level with the tuttis on the master (-13.7 against -13.8 / -13.9), bar 72 1.5 dB under |
| f arrivals, master bars 41 / 129 / 197 / 285 | c16 -22.8 / -22.5 / -24.1 / -22.8; c17 -25.9 / -24.4 / -26.7 / -25.2 | -24.6 / -24.5 / -26.3 / -24.6: +1.3 / -0.1 / +0.4 / +0.6 dB on c17, still 1.8-2.2 dB under c16. The 1 dB target is not met |
| Bassoon 1 into the bar 72 / 300 chords (stem, 209 -> 213 / 893 -> 897) | -8.3 / -7.9 dB | -2.3 / -1.5 dB |
| Flute 1 at 213 against its f eighth | -7.9 dB | -2.3 dB |
| Flute 2 minus Flute 1 at the A6 of 327 | +13.6 dB | +3.7 dB |
| timpani ff strokes 1008 / 1014 against the f strokes 996-1004 (peak, 100 ms) | -33.9 against -30.1 | -29.9 against -32.6 |
| isolated accents (median / p90 / over +3) | +1.4 / +4.9 / 33 | +1.5 / +5.0 / 36 (Violins II +2.8, Clarinet 1 +3.2, Violas +2.0) |
| string legato join excess (`legx18.py`) | median +3.2, 87 of 430 over 6 dB | median +3.1, 91 of 429 over 6 dB; celli 504-552 +3.6 -> +3.9. LEG_TRANS_CC did not work |
| Horn 1 hole at 1077.75-1078.25 against 1076.75 | -15.9 dB | -16.2 dB: velocity 72 did not help |
| Horn 3 G sharp 4, 263.9-266 s | correlation -0.70, mono loss -8.3 dB | +0.99, -0.2 dB; level +3.7 dB, L-R +4.1 dB, the stem nearly mono (broadband correlation 1.00) |
| fugato held notes: celli 171, violas 183, Violins II 195 | -44.0 / -44.7 / -50.8 | -45.0 / -40.9 / -36.5: in order, but Violins II is 4.4 dB over the violas (+30 units gave +14.3 dB); +24 for c19 |
| hall (`hall17.py`) | G.P. drop at +0.3 s 20.1 dB, 20 dB fall 0.30 s, RT60 1.36 s | 18.4 dB, 0.33 s, RT60 1.38 s (late slope 1.53 s): inside Dan's limit |
| envelope points / per note / per second; slope guard | 4,865 / 0.84 / 17.5; 8 notes | 4,852 / 0.84 / 17.5; 9 notes |
| master per bar against c17 (`records/bars_c18_vs_c17.txt`) | | 9 bars over +1.5 dB (62, 66, 71, 184, 288, 294, 299, 300, 366), 8 under -1.5 dB (18 -6.9, 110, 137, 138, 258 -4.8, 290, 328, 365). Bars 18 and 258: Violins I's accented theme notes on "Sus MAX" fell 7-8 dB. That row change is reverted for c19 |
| master per bar against c16 | | 12 up, 23 down (`records/bars_c18_vs_c16.txt`) |

Inner lines in the render (`records/inner_c18.txt`; level while the track sounds, against the loudest track):

| line | c17 | c18 |
|---|---|---|
| celli countermelody, bars 105-111 / 305-320 | -5.5 / -4.7 | -2.9 / -2.2 |
| Bassoon 1, bars 305-320 | -12.6 | -7.5 |
| Horn 4, bars 305-320 | -7.4 | -6.3 |
| celli espress. from 840 | -6.2 | -2.5 |
| melody over the low group, bars 125-128 | basses louder than Violins I | Violins I on top, basses -0.8 |
| Violins II's p fugato entry | -2.4 under the celli | +4.5 over the celli (too much; +24 units for c19) |

The rest of this file is the preparation text of the first attempt; numbers marked "simulated" are replaced by the table above.

## Changes made (files, parameters)

### Generic options in `tools/score_to_parts.py` (all off by default)
- `HP_GAIN_TO_CC11` gains four new keys:
  - `convert` (False: never move the gain into CC11);
  - `keep_rel_db_s`: a gain left in the envelope is released by one of these rules:
    - across a printed decrescendo that starts between the arrival and the hold's end;
    - by the next softer printed mark;
    - inside the next rest of 0.5 qn or more: held to it when the rest starts within 1 qn, otherwise ended in it,
      over at most `rest_rel_s` 0.6 s;
    - otherwise at this rate (2.8 dB/s here);
  - `drop_keep_chain`: a dropped gain that continues a chain holds the earlier gain;
  - `drop_only_chained`: at `drop_ends` only the chained rise is removed.
- `HP_SUBITO_SFP_DELAY_S` / `_REL_S`: a crescendo gain that meets an sfp is held through the sf. It is released
  0.22 s after the mark over 0.3 s (finale technique 78). Before, it was cut at the mark.
- `LEG_TRANS_CC`: a per-join CC11 dip over string legato transitions on "Leg" rows, from a table. The dip starts at
  the moved note-on + 0.03 s and falls over 0.03 s. It is held to the beat - 0.02 s and is back by the beat + 0.10 s.
  It applies only to joins with a lead of 0.12 s or more, with no pre-fall.
- `WIND_DETACH` `overlap_s` / `overlap_min_s`: at a pitch change between two held notes (0.4 s or more) on the same
  non-legato row, the old note ends `overlap_s` after the new note's moved note-on. This happens in the output
  stage; the gap stays in the first pass so the lead rules still lead the new note. A first version that removed
  the gap lost the leads (Flute 1 1008 and 902), so I changed it.
- `REP_GAP_FLOOR_LONG_S`: a same-pitch repeat between notes of `min_s` or longer takes `gap_s` instead of the
  `REP_GAP_FLOOR_S` floor.

### `build/score_config.py` (c18 block at the end)
- `HP_GAIN_TO_CC11`:
  - Four tracks keep the c17 conversion: Flute 1, cor anglais, Violins I and II. Their c17 arrivals came within
    0.5 dB of c16, at 0.16-0.23 dB per unit (`actor_scripts/slope18.py`, `records/slope18.json`).
  - Every other track keeps its gain in the envelope with `keep_rel_db_s` 2.8. On those tracks the c17 slope was
    0.14 dB per unit or less, and negative on the bassoons at CC11 88-98: the arrivals lost 1.3-6.5 dB.
  - `drop_ends` [213, 897]:
    - strings: dropped, as in c17;
    - winds and brass: `drop_only_chained`, so Flute 1, Oboe 1 and the clarinets keep their crescendo gains into
      bars 72 / 300, while the bassoons and contrabassoon hold their earlier +4 dB without the rise to +7.
  - `HP_SUBITO_SFP_DELAY_S` 0.22.
- Accents:
  - `ACCENT_CC` `add_at` at 213 / 897 is now 8 on every woodwind (it was `min(8, add_loud)`, which gave 0 on five
    tracks);
  - Flute 2 `_ACC_BY` (12, 10) -> (5, 4).
- `CHORD_CC11`: (1005, 1017) removed from every span list.
- Timpani: `VEL_SET` 1008 / 1010 / 1012 / 1014 104 -> 114.
- `LEG_TRANS_CC`:
  - applies to Violins I and II, violas, celli, the solo and Violas div (`C18_LTC` lists them for tests);
  - the table `build/leg_trans.json` is written by `actor_scripts/legx18.py` from the c17 render: excess 2.5-4 dB
    gives 3 units, 4-6 gives 6, 6-9 gives 9, 9+ gives 12;
  - 255 joins on 6 tracks;
  - the c17 celli dip at 504.95-505.6 is removed.
- Horn 1 1071 / 1074 / 1077 at velocity 72 (`VEL_SET`; checked in parts.json).
- `WIND_DETACH` `overlap_s` 0.04, `overlap_min_s` 0.4 for both families: 146 pitch changes. The finale used
  0.04-0.05 s and never on legato rows. Also `REP_GAP_FLOOR_LONG_S` {0.6 s, 0.025 s}. The trumpets' half-note chords
  at 1008-1012 are 0.42 s long, so they keep the 0.09 s floor (their notes are unchanged in parts.json).
- Fugato, `CC11_ADD_SPANS`: violas +14 over 182.9-185 and 878.9-881, Violins II +30 over 194.9-197. Sizes come from
  these notes' own c16 -> c17 slopes: violas 0.14 dB per unit, Violins II 0.25. The Violins II value is a guess for a
  range test.
- Violins I `ART_AT` 51 / 771 "Sus MAX".
- Celli pp pizzicato heads 264 / 273 / 282 / 291 at velocity 56.
- Violas `CC11_ADD_SPANS` (974.8, 978) extended to 979.4.

### `build/roles.json`, `build/mix.json`, `build/lead_set.json` (`actor_scripts/apply18.py`, rerunnable from `before/`)
- Roles:
  - Flute 2 [312, 360, 3.5] -> -1.8 (Flute 1's value) and [912, 960, 1.9] deleted;
  - Timpani [996, 1004.9, 2.5] deleted;
  - the 15 c17 rows of B #3 deleted;
  - Violins II [984, 995.5, -7] -> [985, 995.5, -7] (its edge now falls in the rest before 985).
- Inner lines (Dan, 2026-11-17):
  - celli [312, 360] and [912, 960] +2.5 -> +4.5;
  - Bassoon 1 +3 and Horn 4 +2 over the same spans;
  - celli [180, 198, 2.5] -> [180, 192, 2.5];
  - celli [828, 864, -3] -> [828, 840, -3].
- Mix:
  - Flute 1 "Sus MAX" f layer E6 -5 -> -2;
  - Flute 2 "Sus MAX" A6 a further -4 (total -6);
  - celli "Leg Slur MAX" f / ff +1.5 -> +4.5;
  - Bassoon 1 `dyn_trim_db` f 0 -> +2, ff 1.2 -> +4;
  - Horn 3 `channel_map` 2 ("Mono From Left", finale c19). Horn 1's Close-led mix was not copied.
  - `cresc_trim_hold` skip + [981, 984].
- Leads (A #3): Violins II 134 0.14, 133.5 0.10, 373.5 0.15; Violins I 145.5 0.17, 373.5 0.17, 597 0.22, 361.5 0.14;
  celli 348 0.09, 933 0.165, 948 0.09, 333 0.15; violas 594 0.195, 1056 0.31.

### Delivery (`tools/deliver_master.py`; Dan 2026-11-17, shared spec in `mockup-kit/README.md`)
- Loudness and limiter:
  - -14 LUFS (was -19.5);
  - limiter ceiling 0.87 (-1.2 dBFS);
  - quiet-lift knee 7 dB under p95 short-term;
  - top ride from 10 dB under p95 at 3:1 (Movement I's values).
- Lift and peak control:
  - lift ratio 1.6;
  - a fast peak compressor before the limiter (threshold -6 dB, ratio 2, 2 / 60 ms; `DELIVER_PEAK_COMP`);
  - the gain is corrected after the compressor.
- New reports:
  - the limiter's gain reduction per passage, with the output moved back by the 5 ms look-ahead;
  - the short-term p10 / max;
  - environment overrides for every new value.

## Measured offline

| | c17 | c18 (prepared, simulated where noted) |
|---|---|---|
| envelope points / per note / per second (`slope17.py`) | 4,865 / 0.84 / 17.5 | 4,869 / 0.85 / 17.5 |
| slope guard (1.5 dB in 0.5 s inside a note) | 8 notes | 9 notes: celli 362 / 312 / 912, Horn 2 1005, Horn 3 953 / 936, Harp 708, Oboe 1 1005, Violas 197 |
| crescendo arrivals, dry-stem sum (envelope only, `sim18.py`) | | 41 +0.7, 129 +0.6, 197 +1.4, 285 +0.6 dB; bar 72 +1.0, bar 300 +1.5 |
| 0.4 s maxima, dry-stem sum (envelope only) | summit -15.5, tutti 312-360 -16.9, 912-960 -18.7, bar 72 -20.5, bar 300 -19.1 | summit -15.6, tutti -18.1 / -18.2, bar 72 -19.2, bar 300 -17.6. Flute 2's A6 no longer leads the first tutti. Bar 300 may come out over the second tutti; the render has to show it (the accent and sfp shapes are not in this simulation) |
| string legato join excess (`legx18.py`, c17) | median +3.2 dB, 87 of 430 over 6 dB | not rendered |

c17 master under the new delivery (`records/c17_at_shared_target.mp3`):

| | |
|---|---|
| loudness | I -14.4 LUFS, LRA 12.3 LU, TP -1.0 dBTP |
| short-term | p10 -22.3 LUFS (c17 delivered: -29.0); p10-to-max span 14.8 dB |
| limiter (gain reduction) | summit 4.9 dB, tutti 105-120 3.1, tutti 305-320 2.2, bar 72 2.5, bar 300 1.0, final chord 0.1 |
| momentary maximum (`order18.py`) | summit -7.0, tutti 105-120 -6.9: the summit no longer leads (c17 mp3: +1.4 LU). At -14 LUFS the top ride and limiter flatten the summit against the first tutti. The c18 mix lowers that tutti (Flute 2) and keeps the summit's chords at full CC11; the c18 render has to show whether that is enough |

Inner lines (c17 stems, `inner18.py`, level while the track sounds, against the loudest track):

| line | bars | before (c17) | after |
|---|---|---|---|
| tutti countermelody (espress.) | 105-111 / 305-320 | celli -5.5 / -4.7, Bassoon 1 -12.9 / -12.6, Horn 4 -7.4 | roles +2 / +3 / +2 (not rendered) |
| Violins II's p fugato entry under the celli's pp | 65-67 | -2.4 under the celli | celli row ends at 192; Violins II CC11 +30 |
| celli espress. from 840 | 281-288 | -6.2 (under the basses), -5.6 under Violins I | -3 row ends at 840 |
| second idea, melody against the low group | 121-128 / 277-284 | basses loudest | low-group rows removed (item 3) |

## Rejected, deferred, not done
- Range tests were planned and not run: celli LEG_TRANS_CC, Horn 1 1071-1077, timpani 114, celli "Leg Slur MAX"
  layers, and Horn 3 per pitch with Mono From Left. The finale saw shifts of up to 7 dB on single pitches; re-level
  after the render.
- Clarinet crescendos on CC1 were not tested; they stay in the envelope.
- The celli countermelody region gain (B #6): the transition groups set the level of short legato notes and carry no
  dynamic suffix, so f / ff +4.5 acts on the long notes only. The phrase row (+4.5) carries the line.
- Not done:
  - Bassoon 2 trims;
  - celli f under mf (C #4) beyond the f-layer gain;
  - CC16 resets before each pizzicato pluck;
  - per-track tutti entry-lead cuts;
  - Flute 1's accent at 264.
- The region-gain tool applies only the first listed pitch when one sample serves two keys (finale c20 #4). This was
  not checked on our celli pizzicato table.
- c17's WAV files: not deleted (the coordinator's c18 notes: do not delete c16's or c17's stems or render_first).
- Range tests: none were run, for lack of lock time.
- Faults still audible:
  - the f arrivals are 1.8-2.2 dB under c16;
  - the string legato join swell (LEG_TRANS_CC had no effect);
  - Horn 1's motto-tail hole;
  - bars 18 / 258 (fixed in the data for c19);
  - the fugato Violins II overshoot (fixed in the data for c19);
  - bar 300 is level with the tuttis on the master (the delivery ride holds it 0.3 dB under the second tutti);
  - Horn 3 is +3.7 dB and narrow after Mono From Left: re-level it per pitch in c19.
- Delivery: two new data changes:
  - ride rows (`RIDE_TRIMS`, end of `score_config.py`): trio ff 624-672 -2, bar 72 -1.5, bar 300 -2, tutti 912-960 -1 dB;
  - `tools/deliver_master.py`: top ride 2.5:1 (3:1 gave LRA 11.7), ceiling 0.85 (0.87 gave -0.9 dBTP after the mp3 encode), pre-limiter aim +0.6 LU.

## Research items

| item | status |
|---|---|
| EW template mix, returns, EQ set, seats, wind send, return pans | adopted (unchanged) |
| no volume automation per note | adopted; slope guard 9 notes |
| accents by controller | adopted, per track |
| one legato row per string line, keyswitch 0.15 s ahead | adopted |
| per-region / per-row volume in the Opus state | adopted |
| unprinted tempo, Slur Runs, Close + Main on divisi | rejected earlier |
| CC16 resets everywhere, delivery rise delay, separate legato tracks, timpani hard sticks, recorded crescendo rolls | pending |
