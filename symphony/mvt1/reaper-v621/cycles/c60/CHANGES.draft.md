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
     see "Rule" above for the count. Kept after reading each: bar-long rows whose edges lie in rests or on printed
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
