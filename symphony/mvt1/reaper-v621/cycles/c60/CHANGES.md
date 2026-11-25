# Cycle 60 (Movement I): CHANGES

Render: cycles/c60/mvt1-mockup-c60.mp3 (main render and pass 2, 17 Nov 07:35-08:19). Built from build/ as listed
below; rendered_build/ holds parts.json, mix.json, roles.json and score_config.py as rendered. Two actors: the first
applied every change and was stopped before the lock came; the second checked the build (parts.json regenerated
identically, apply60.py reproduces the four JSON files), ran the REAPER phases and wrote this file.

## What changed, in the coordinator's order (files: `build/score_config.py` c60 block, `build/mix.json`, `build/roles.json`, `build/entry_leads.json`, `build/retongue_leads.json` through `cycles/c60/actor_scripts/apply60.py`; `tools/score_to_parts.py`, `tools/build_reaper.py`)

1. **Rule breaches on the envelope.**
   - Deleted: the two `LEVEL_SHAPES["Violoncellos"]` rows fitted to the c26 and c47 renders over the strokes 345-347
     (-4.0 and -3.5 dB), the +1 dB row on the celli's one tremolo note at 484.25-488, the +2.5 dB row on three Cor
     anglais staccato strokes (alias table, 367.3-371.7).
   - Bass clarinet 424.4-432.2 (+2.5 dB over nine notes): deleted from the envelope, written as `CC11_ADD` +6 units
     (0.39 dB per unit on its own curve at 34-46).
   - Violas 244.1-248.7 (critic B: -8.7 dB): not a fitted row. It is the end of two crescendo ramps (+4, +3 dB) at
     the printed subito and the -3 dB row `LEVEL_SHAPES["_all"]` that every track carries over the printed sub. p bar.
     Kept as section dynamics on a printed dynamic.
   - Fugato subject, celli alone, bars 85-87: `CC11_LANE` flat at 72 over 336.4-347.7 (the lane fell 72 -> 62 with
     nothing printed), the accent at 342 one flat value of 77; stroke velocities by `VEL_SET` (variant in
     `build/fug60.txt`).
   - Timpani: `TIMP_LOUD_ATTACK_DB` 6 -> 0 (the +6 dB shape on each f / ff stroke is gone); stroke weight by velocity,
     `TIMP_STROKE_VEL` (new key): f 96 -> 112, ff 110 -> 127 before the metric offsets.
   - Search of `LEVEL_SHAPES` and the rule dump (`rows60.py`: every envelope item under 5 s or on fewer than 5 onsets):
     5 found and removed (the four deleted rows above and the Bass clarinet row); 267 short rows listed and read (349 before), the rest kept as section dynamics with edges in rests or on printed dynamics. Kept after reading each: bar-long rows whose edges lie in rests or on printed
     dynamics (Trumpet 1 324.2-329.5 +4, celli 324-329.5 -3, Oboe 1 455.7-462.3 +4), the ramps into and out of
     printed arrivals (236-244, 478-484, 627.9-636), unison rows.
2. **Climax order.** `mix.json` `dyn_trim_db.ff`: -2.5 on Violins I, Violins II, Violas, Violoncellos, Double basses
   and their aliases, -1.5 on every wind and brass track with an `fff` anchor; Horn 1 ff 1.5 -> -0.5 and f -0.8 -> 0.7,
   Horn 2 ff 0.4 -> -1.6; `fff` unchanged. `roles.json`: Trumpet 1 `[484, 492.5, 3, 1]`, Trumpets 2 / 3
   `[484, 492.5, 2, 1]` added as slow rows on the envelope (`LEVEL_TO_CC` new key `keep_env`); the c59 rows stay: they
   are played as CC11 109 -> 124 with the top CC1 layer (critic B read them as not played; taking them out put the
   trumpets back at 109). `_all [484, 504]` -1.6 -> -0.6. Violins I tremolo 484-492: `CC11_ADD` +13 (98 -> 111).
   Timpani roll 632-636: CC7 end 76 -> 83 (`TIMP_ROLL_DB_ADD`, new key, +1.8 dB on the roll, back before the stroke).
3. **Dynamic trim across printed hairpins.** `tools/build_reaper.py` `vol_points`, `mix.json` `decresc_ramp`
   `{"min_step_db": 3, "rest_s": 0.1, "max_db_s": 3}`: where a diminuendo runs into its arrival note with no rest and
   the held trim would step up 3 dB or more at that note-on, the trim ramps over the hairpin (at most 3 dB/s; what is
   left stays a step). 19 hairpins (list: `ramps60.py`). The c59 floor on the violas' tremolo is replaced by the value
   in `build/vafl60.txt`. `CC11_FLOOR` at the arrival value: Oboe 1 166-168 34, Bassoon 2 262-268 43, Contrabassoon
   164-168 46, Bassoon 1 496-500 50, Double basses 28-32 40.
4. **Second theme, bars 47-54 and 147-154.** `mix.json` Violoncellos `region_gain_db` Leg BC MAX -4 (every region of
   the row); `CC11_LANE` for the celli and Horn 1 over 184-216 and 584-616 (critic C's points); on Horn 1 the CC1 layer
   moves with the lane (`CC11_LANE_CC1`, new key).
5. **Other hairpins and balance items.** `CC11_ADD`: basses 357.7-359.7 start 80 -> 72 (the printed mf; C asked for the
   end at 100, which would overshoot the f it arrives at); Horn 1 bars 103-104 each hairpin 6 units lower at its start
   and 6 / 9 higher at its arrival, B-flat 4 Sus MAX region gain +3 -> +1; Horn 1 bar 111 52 -> 64 -> 70; Horn 3 165
   84 -> 78; Trumpet 3 456-464 80 -> 73; Clarinet 1 576-582 12 -> 17. `CC11_LANE`: Clarinet 2 576-582 15 -> 19 -> 16
   (was 25 -> 34 -> 22), Violas 368 88 -> 94 -> 86, celli 295-304 34 -> 28. Cello solo: lane point 683.35 70 -> 64; the
   Port note at 685 led 0.15 s more (alias `LEG_LEADS` 0.07 -> 0.22) in place of critic C's CC11 rise inside the note.
6. **Dynamic mapping.** `mix.json`: Horn 4 `soft_trim_db` p 5 -> 7.5, mp 5 -> 6, mf 4 -> 5.5, F3 soft layers -6 -> -8.5;
   Oboe 1 region gains per layer (the E5 / F5 cuts on the f layer only; E-flat 5 +7 and F5 +2 on the pp and mf layers);
   Violas `soft_trim_db` p 5 -> 3; Oboe 2 `dyn_trim_db` f 3.5 -> 6.0.
7. **Sustained tutti chord changes.** `WIND_DETACH["long"]` (new, `tools/score_to_parts.py`): a tongued join between two
   notes of 0.8 s or more on one plain sustain row, the second without accent, staccato, sf or breath: the old note ends
   0.04 s (brass) / 0.03 s (winds) after the new note-on at a pitch change, 0.025 s before it at the same pitch. 558
   joins on 22 tracks. A keyswitch between the two notes or a different row excludes the join, so no legato row gets
   an overlap.
8. **Re-bows.** `REBOW_AT` re-listed so pieces run up to 5.3 s (`REBOW_MAX_S` / `REBOW_SKIP_UNDER_S` 5.3, `REBOW_SEG_S`
   4.6): celli bars 7-14 none, bars 3-4 one, final chord four; basses bars 12-14 one, 286-304 one at 293.6, pedal
   463.7-520 five, final chord four (`REBOW_NONE` removed); violas final chord three. Re-bow rows 70 -> 52.
   `REP_MIN_GAP["held_lead_s"]` (new): the new bow of a printed same-pitch change on a held pitch starts 0.20 s early
   under CC11 60 and 0.12 s above (51 notes, re-bow pieces on printed bow marks included).
9. **Timing.** `RETONGUE_LEAD_S` basses 0.06 -> 0.12; `ENTRY_LEAD_S` Oboe 2 0.14 -> 0.05 with its `entry_leads.json`
   extras re-based so no entry leads more than 0.06 s (`ob2leads60.py`, `build/ob2_extra60.json`); Trumpet 2 0.06 ->
   0.08; `entry_leads.json` Horn 1 / Horn 2 484 +0.06, Trumpet 1 484 +0.04, Bassoon 2 620 +0.10;
   `retongue_leads.json` Flute 1 47 +0.07 (the old note now ends 0.05 s before it, was 0.087); tam-tam `delay_s`
   0.05 -> -0.08.
10. **Small CC11 items.** Bass clarinet 704-708 34 -> 27; Clarinet 1 706 start 48 -> 54; Violas tremolo into bar 82
    78 -> 96 in place of 84 -> 102 (a slower rise from 319); Trumpet 3 456 (item 5). Horn 1 587.5: superseded by the
    second-theme lane.

## REAPER turns
- Turn 1 (16 Nov 21:00-22:36): state guard 0 stale at the start; main build --midi-only (Oboe 1, Horn 1, Horn 4 rebuilt
  in full: Opus state); range renders, each twice, second kept; post-save guard 4 stale (Cor anglais, Horn 4, Violas,
  Horns a2) rebuilt in full. The main render was refused by render_cycle's memory gate (23 GB compressed, limit 6) and
  the chain went on to unlock with no render (actor error: the shell chain did not stop on failure).
- Turn 2 (17 Nov 07:33-08:35, cycles/c60/actor_scripts/p5.sh, which stops and keeps the lock on any failure): fresh
  restart, 0 GB compressed, main render without --force-memory; pass 2 (9 tracks); post-save stale tracks rebuilt in
  full in both projects (pass 2: Bassoon 1 stac, Cor anglais stac, Flute 1 stac); quit; unlock.
- Memory: main REAPER 43 GB before (0.0 GB compressed), 44 GB after (28 GB compressed); pass 2 19-20 GB. Disk 59 GB free.

## Range tests (second passes, cycles/c60/rangetest/*B; first passes deleted)
- Fugato bars 85-87, celli alone: B (critic B's velocities) shipped. Bar levels B 85 / 86 / 87: -38.6 / -37.3 / -41.9 dB;
  C: bar 87 -42.1. Neither keeps bar 87 within 3 dB of bar 86 (bar 86 holds the 342 accent); B is louder in 87.
- Long joins (decision 7) adopted: wind-and-brass sum dip c59 -> c60 at 484 / 488 / 492 / 496: 6.5 / 6.0 / 2.0 / 3.9 ->
  3.6 / 1.8 / 1.2 / 3.2 dB; at 664 / 668 / 670 / 672 / 676: 4.5 / 7.0 / 1.5 / 7.5 / 6.3 -> 3.4 / 3.5 / 0.9 / 1.8 / 6.3.
  4 of 9 under 2 dB. Fronts +4 to +5 dB at 484, 488, 670 (Flute 2, Oboe 1, Bassoon 1, Clarinet 1, Horn 4): doubled
  attacks not checked.
- Bar 122: Trumpet 1 +3.8 / +4.3 dB, Trumpets 2 / 3 +2.3-2.8, Horns 1-2 +0.8-1.2, Violins I +2.5-3.3, tam-tam +0.3.
- Timpani bars 27-28: without the attack shape, f/ff strokes 0.4-4.8 dB under c59 (velocity already 117-127).
- Basses' eighths 104-108: peaks 10 ms earlier (+54 to +85 ms), 2.0-3.6 dB lower (ff trim). The finale's 70 % / 0.075 s
  form was not tested (needs a tool key).
- Violas 160-168: step into 168 +4.4 dB (c59 +9.0), still over 3. Oboe 1 166-169 +8-10 dB over c59 (CC11 floor 34).
  Horn 3 164 -6.7 dB as asked.
- Second theme 184-216: celli Leg BC notes -4.2 to -4.8 dB, Horn 1 within 2 dB of c59.

## Measured, c60 render against c59
- Envelope: per-note items 0 on every track; points 3951 -> 3437; timpani 1.28 -> 0.40 points/s; strings 0.37-0.61,
  winds and brass 0.19-0.38 (envelope_table.md).
- Guards: Violins I 56-87.9 S robust SD 9 ms, front minus tail -1.5 dB; 56-127 12 ms; 536-576 18 ms (-2.6). Theme over
  celli 56-88 lower quartile +7.4 (c59 +4.3).
- Climax order. Master bar level: 160 -16.0, 161 -16.4, 122 -17.1, 26 -19.2, 170 -22.7 dB (c59: 160 -16.0, 26 -16.9,
  122 -18.1, 170 -20.7): printed order holds by bar level and by loudest 0.4 s (160 -15.1, 122 -16.5, 26 -17.4, 170
  -17.9). Delivered mp3: by bar level 160/161 -13.0, 122 -13.3, 26 -13.9, 170 -16.7 (holds); by loudest 0.4 s 170 and
  160 both -12.2, 26 -12.5, 122 -12.8: the delivery ride lifts bar 170's quieter bar and its first chord with it.
- Delivery (tools/deliver_master.py as changed by the coordinator): loudness pass 1 I -14.5 LUFS (lift +11.80 dB),
  pass 2 I -14.0 (lift +12.35); delivered I -14.0 LUFS, LRA 11.2 LU, TP -1.2 dBTP, ride max +10.5 / min -7.0 dB,
  limiter about 6.7 dB on the loudest peak (ceiling 0.870), p10-to-max short-term span 13.5 dB. Pre-limiter peaks:
  202.7 s (bar 83, Violins I) +5.5 dBFS = 6.7 dB of limiting, the only passage over 6 dB; 203.8 s (bar 83) 5.9;
  117.0 s (bar 40) 5.6; 378.8 s and 377.9 s (bar 170) 5.3 / 4.9. Master: -21.1 LUFS, LRA 22.1, TP -2.0 dBFS.
- Attack probe: late or hole 0; string join windows inside their limits.
- Faults c59 -> c60: faults_table.md (re-bow holes 14 -> 8; repeats 49 -> 114 from the long-join same-pitch gap).
- Isolated accents (accent_table.md): n 152, median +1.8, quartiles +1.2 / +2.6, max +9.6; 29 inside +1.5-2.0, 32
  over +3, 22 under +1 (c59: n 151, +1.7, 30 / 32 / 20). Accent values untouched.
- Master bars more than 1.5 dB off c59: up 86 +6.5, 87 +5.0 (the fitted -7.5 dB celli rows deleted), 146 +3.0, 145 +2.3
  (Clarinet 1 12 -> 17 and the lanes of bar 145), 125 +2.3 (Bassoon 1 floor 50 and the trim ramp); down 29 bars, -1.5
  to -3.0, all in ff passages (25-32, 82-85, 97, 134, 140, 158, 170): the ff trims of decision 2. Median -0.21.
- Inner lines (coordinator note 3): the celli under the theme, bars 15-22, -41.7 -> -45.6 dB (row gain Leg BC MAX -4);
  the celli's Leg BC notes in the second theme -4.5 dB. Both bury the celli further; c61's inner-line pass should
  check them.
- A/B clips c59 then c60 (ab/): bars 15-23, 85-87 and 121-124, master and lead stem, one gain per clip.

## Left audible / not done / not verified
- Left audible: bar 87 5.4 dB under bar 86 (master); timpani f/ff strokes softer; Violas step into 168 +4.4 dB;
  join dips 3.2-6.3 dB at 484, 496, 664, 668, 676; 8 re-bow holes of 8-14 dB; join holes Flute 2 560 (11.9), Oboe 1
  166 (9.5), celli 286 (16.5), basses 310 (10.3).
- Not done: final-chord alias Sus MAX copies (decision 8); the basses' 70 % / 0.075 s variant.
- Not verified: doubled attacks at the long joins; whether the 92 new same-pitch repeats are audible; the tam-tam
  delay -0.08 s against the beat (no range measure of its start); the Cello solo 685 lead by ear.
