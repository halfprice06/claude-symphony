# Movement IV (Finale) mockup in REAPER (EastWest Hollywood Orchestra Opus Edition)

Mockup of `symphony/mvt3/v600` (Symphony No. 1, IV. Finale: Allegro con fuoco, C minor to C major), built by script through the REAPER file bridge and improved by the actor-critic loop in `loop/`. This folder is local and kept out of git (`.git/info/exclude`). The method and tools come from `mockup-kit/` (read its README and LEARNINGS first); the tools here are Movement I series 2's pipeline at its c42 (`symphony/mvt1/reaper-v621/tools/`) plus the port's edits below.

## Files

- `mvt3-v600-mockup.rpp`: the REAPER project (Movement I's project header with no tracks, `RENDER_1X 1`; the first build writes every track, the tempo map and the pre-roll). 31 tracks, one Opus instance each, stems 01-31 in `build/score_config.py` `TRACKS` order.
- `build/`: `mockup.ly` (Movement I's extraction, unchanged: one staff per player plus a DrumStaff; dumps `mockup.midi` and `mockup-events.tsv`), the score sources copied from v600 (`global.ily`, `parts.ily`, `sections/`, run through `convert-ly` to LilyPond 2.26; `score-defs.ily` = v600's `score.ly` from its `sec` definitions to its last `\addQuote`, without the layout and the MIDI-only timpani roll function, which the pipeline does not need), `score_config.py`, `parts.json`, `mix.json`, `probe.json`, `ks_maps_extra.json` (Movement I's), and the per-note tables (`roles`, `note_trims`, `pitch_trims`, `entry_leads`, `early_fills`, `leg_leads`, `loop_fills`, `loop_profiles`, `rebow_fills`, `rebow_moves`, `accent_fits`, `accent_bodies`, `cresc_fronts`, `auto_fills`; all empty at c00).
- `tools/`: the pipeline (score_to_parts, space_rebows, build_reaper, reaper_ctl with owner "mvt3", render_cycle, measure, probe_attacks, pcx, deliver_master, motion, auto_fills, fit_rebows, fit_loops, fit_accents, fit_accent_bodies, stem_fix, rendermap, state_guard). `mockup-kit/README.md` and Movement I's README ("Tools added in later cycles") describe each.
- `loop/`: `BRIEF.md` (read by every agent), `critic_prompt.md`, `actor_prompt.md`, `workflow.js` (one cycle per call: args {start, end, prev}), `HISTORY.md`, `LEARNINGS.md`, `MANUAL-READING.md`, `MANUAL-GAPS.md`, `DYNAMICS-RESEARCH.md`.
- `cycles/`: per cycle the critics' `reports/`, `before/`, `render/`, `metrics/`, `CHANGES.md` and the delivered `mvt3-mockup-cNN.mp3`. `cycles/c00/PORT.md` records the port.
- `jobs/`: the Lua jobs and generated Opus states (`NN_<patch>.b64`).

## Rebuild from scratch

```
cd build && lilypond -o mockup mockup.ly
~/.venvs/claude-composes-reaper/bin/python ../tools/score_to_parts.py . ~/.rpr-bridge/libs/ew_ho/ks_maps.json parts.json
~/.venvs/claude-composes-reaper/bin/python ../tools/space_rebows.py parts.json --write   # when re-bows changed
~/.venvs/claude-composes-reaper/bin/python ../tools/score_to_parts.py . ~/.rpr-bridge/libs/ew_ho/ks_maps.json parts.json
cd ..
# REAPER is shared with the Movement I, Movement II and scherzo threads: take the lock first, keep job files in this folder
~/.venvs/claude-composes-reaper/bin/python tools/reaper_ctl.py lock "mvt3 cNN actor"
~/.venvs/claude-composes-reaper/bin/python tools/reaper_ctl.py start && ~/.venvs/claude-composes-reaper/bin/python tools/reaper_ctl.py open
~/.venvs/claude-composes-reaper/bin/python tools/build_reaper.py build/parts.json jobs
~/.venvs/claude-composes-reaper/bin/python tools/reaper_ctl.py restart
# after a --midi-only build: save, then check the saved project for stale Opus legato state (read-only; rebuild in full any track it lists)
~/.venvs/claude-composes-reaper/bin/python tools/state_guard.py mvt3-v600-mockup.rpp build/parts.json jobs
# reopen the audio device (reaper.Audio_Init() job), then:
~/.venvs/claude-composes-reaper/bin/python tools/render_cycle.py N
~/.venvs/claude-composes-reaper/bin/python tools/reaper_ctl.py quit && ~/.venvs/claude-composes-reaper/bin/python tools/reaper_ctl.py unlock
```

`score_to_parts.py` must print no WARNING (each one is a printed dynamic the CC11 curve misses).

## Port to v600 (cycle 0; details in `cycles/c00/PORT.md`)

- Config: `build/score_config.py` holds the Finale's tables (tracks, percussion map, Trumpet 1's mute span, tempo ramps) and Movement I series 2's generic settings at its c42 (every value in its config that names no score onset: CC1 dynamics on brass and clarinets, leads, legato caps, repeat and detach rules, row trims, the gentle accents, timpani maps, harp velocities). No per-onset entry of Movement I is carried over.
- Tracks: Movement I's 33 minus the tam-tam and suspended cymbal, plus a bass drum (36in Ludwig, Felt Long key 38). Timpani on `Timpani Hrd KS` (v600 prints hard sticks; Movement I used felt, and its timpani maps were fitted on felt). Trumpet 1's con sordino solo (qn 680-792) on the 1TP KS Master's "Mute Sus" row (`ART_SPANS`), no extra instance.
- Mix: Movement I's c42 `mix.json` with its score-timed EQ automation (`loud_eq`, `side_shelf_switched`) and its alias/test/pass-2 tracks removed; Bass drum added to the perc group.
- New generic options in `tools/score_to_parts.py` (comments "mvt3 port"): `SOLI_AS_META` ("N soli" reads like "metà", from Movement II c27), `sfp` read as an fp with an sf attack (`SFP_SPIKE_HI`), timpani rows by patch (`TIMP_ROW`: the Hrd KS rows), and a tempo ramp returns to the stepped tempo at its end when no step marks it (allargando 124-112 into Maestoso 112). `tools/stem_fix.py` scratch paths are `mvt3-stemfix-*`. `tools/reaper_ctl.py` takes the lock as owner "mvt3".
- Known open at c00: the bass trombone's B flat 1 (one note, below the 1TB KS Master's lowest key 36; MANUAL-GAPS #13); timpani CC1/roll maps fitted on felt; no Finale per-onset tables yet.

## Delivery

`tools/deliver_master.py` is Movement I's c42 version (lift ratio 3.0, knee 5 dB, 5 s lift smoothing, top ride ratio 2.5, `RIDE_TRIMS` from parts.json when present).

## Tool options added in later cycles

- c01: `score_to_parts.py` ROW_GAIN_DB, LAST_DESK_DB, TASTO_CC1, REBOW_KEEP_ARTS, HARM_ON_TRACK, GLISS_SPANS, UNI_CHORD_SPLIT; `build_reaper.py` mix.json "bandpass" (Opus Bandpass Filter per row) and reverb "low_cut_hz". The hall return is fx_volume 0.095 from c01 (Dan: too wet).
- c02: `score_to_parts.py` STR_REP_NEW_BOW (ported from Movement I c44, plus a "skip" span list and down-bow strokes as predecessors), SFP_SPIKE_S / SFP_VEL (an sfp attack in seconds and a minimum attack velocity); `build/score_config.py` RIDE_TRIMS (delivery-ride trims, refit on the render).
- c03: `build_reaper.py` reverb "ir_setup" (the IR envelope, from mockup-kit / Movement I c44); `score_to_parts.py` HP_DIM_RESTATE, HP_SWELL_AT_MARK and the fp/sfp check point (no WARNING), ACC_HEAD_JOIN, SHORT_SUS_DETACH_JOIN_LEG, RAMP_END_CLAMP, TIMP_SETTLE_SKIP, ABUT_LEAD "min_qn", STR_REP_NEW_BOW "tenuto"; mix.json string / horn `sus_release_cap_ms` (Movement I c44); `space_rebows.py --write` run for the first time (build/rebow_moves.json).
- c04: `score_to_parts.py` LEG_VEL_EXTRA_S list form [(velocity at or below, extra s), ...], REBOW_FILL_END_S (from Movement I c45), STR_REP_NEW_BOW "sus_min_s" repeats take the re-tongue lead (`rt_for`, "sus_lead_s"); `build_reaper.py` mix.json `width_by_mic` (from Movement I c45 / mockup-kit). The string release cap now also lists the legato and tremolo rows; `build/rebow_fills.json` is fitted (c03 render).
- c05: `build_reaper.py` `cap_release` "ms" may be a dict keyed by dynamic word (mix.json string caps pp/p 500, mf 300, f/ff 150 ms); `score_to_parts.py` PERC_END_AT (per-stroke percussion end), PIZZ_LEAD_S (per-track pizzicato lead), ROW_LEAD_S (per-track, per-row lead); the final crash / bass drum use PERC_MAP `_damp` (the crash does not damp at its note-off).
- c06 (EastWest template mix, mockup-kit/EW-TEMPLATE-PLAN.md items 1-4; no kit code existed, written here): `build_reaper.py` mix.json `pan_by_mic` (Close at the seat with the track width, Main / Surround full width; replaces `width_by_mic`), `track_pan` (REAPER pan), reverb `opus_off` (Opus hall off: sends 0, fx:0 0, ConvolutionReverb removed), `returns` (four return tracks "R Strings", "R Brass", "R Winds", "R Perc" after the 31 instruments, FX chains pasted verbatim from `symphony/mockup-research/ew-template-2026-11-08/ho-mix-chunks/*_VERB.txt`, faders from the template) with group `return` {to, db} post-fader sends, and `family_eq` (a second ReaEQ named "FAMILY EQ", built from a band list on the template's ReaEQ chunk layout and loaded with vst_chunk; `set_eq` leaves it alone; each build reads the bands back). `deliver_master.py` applies mix.json `master_eq` (the template's master ReaEQ) before the ride, so `00_Master.wav` stays the plain sum of the stems. The project now has 35 tracks; `render_cycle.py` renders the returns as stems 32-35, so the master = dry stems + return stems. Measure balance on the dry stems (01-31) and decays / soft ends on the master or on a stem plus its return.
- c07 (`cycles/c07/CHANGES.md`):
  - `tools/fxchunk.py`: Movement I's Spaces II `spaces_set`, ported. It lets a mix.json return carry `"set"` (Spaces II
    JSON, e.g. `irSetup`) and `"hp_hz"` (band 0 of the return's ReaEQ). `returns_job` reads both back from REAPER.
  - `score_to_parts.py` options:
    - legato and velocity: `LEG_VEL_STRONG` list form, `LEG_VEL_DYN_ADD`, `LEG_OVERLAP_MIN_S`, `ROW_VEL_BY_CC`;
    - leads: `ROW_LEAD_S` span form (with `ROW_LEAD_CAP_FRAC`), `TREM_ENTRY_LEAD_SPANS`, `STAC_LEAD_S` for brass;
    - repeats: `STR_REP_NEW_BOW["chord"]`;
    - shaping: `PHRASE_SHAPE` (typed build / drive / lyric; on `CC1_DYN_TRACKS` in CC1) and `HP_CURVE`.
  - `deliver_master.py`: mix.json `"deliver": {"ratio"}`.
- c08 (`cycles/c08/CHANGES.md`): `score_to_parts.py` `FINAL_RING`, `METRIC_BOWED_DB_SPANS` (and the 2/2 half bar as
  "mid"), `RR_RESET_AT` / `RR_RESET_CC` (CC16 round-robin resets, lane `cc16`), `UNI_OUTLAST_PLAY`, `HELD_DECRESC_CARRY`;
  `build_reaper.py` writes the `cc16` lane and a mix.json return's `side_shelf`; `stem_fix.py` runs again with the
  fxchunk import.
- c09 (`cycles/c09/CHANGES.md`): `score_to_parts.py` `FP_SPIKE_AT_MARK` (an fp / sfp attack as a step at the mark; a
  hairpin on the same onset starts after the attack's fall), `FP_SPIKE_S` / `FP_VEL`, `HP_CURVE["skip_staves"]`,
  `PHRASE_SHAPE["types"]["drop"]`, `ACCENT_SWELL_FROM_MOVED`, `STR_REP_NEW_BOW["plain"]` (parts.json `plain_gaps`),
  `HARP_VEL_MAX`; `build_reaper.py` mix.json `track_width` (REAPER D_WIDTH, also written by `--mix-only`).
- c10 (`cycles/c10/CHANGES.md`): `score_to_parts.py` `REP_SPLIT` gap keys (Movement I c51 port, also the basses' plain
  Sus MAX repeats; parts.json `rep_split_gaps`), `SOST_JOIN_LEAD_S` per-track dict and `leg_leads.json` rows on slur-start
  joins; `build/mockup.ly` dumps text on multi-measure rests (stick changes, "muta", "metti / togli sord.").
- c11 (`cycles/c11/CHANGES.md`): `score_to_parts.py` `STR_REP_DETACH` per-span `beat_gap_db` (a gap-only dip before beat
  strokes; the span's metric steps start at the onset; parts.json `beat_gaps`), `STR_REP_NEW_BOW["chord"]` tested before
  the generic string tenuto rule, with `head_gap_s` / `loure_gap_s` (parts.json `chord_head_gaps`, `chord_loure_gaps`);
  `leg_leads.json` rows add to the base lead plus extras before `LEG_LEAD_CLAMP`.
- c12 (`cycles/c12/CHANGES.md`): `score_to_parts.py` `ROW_SLUR_OVERLAP_S` {track: {row: seconds}} (at a `ROW_LEAD_S`
  join under one printed slur the note before ends this long after the moved onset; parts.json `row_slur_overlaps`),
  `ROW_LEAD_KEEP_END` {track: {row: [(from_qn, to_qn)]}} (a led stroke keeps its note end, so the played gap before
  the next stroke does not grow by the lead), `STR_REP_NEW_BOW["plain"]["force"]` {track: [score onsets]} (listed
  same-pitch repeats take the new-bow gap at any dynamic and under a slur; a WARNING if one cannot). `tools/state_guard.py`
  (Movement I's c52 tool, copied unchanged): `state_guard.py RPP PARTS JOBS` reads the saved .rpp and lists tracks whose
  Opus legato state is stale after `--midi-only` builds. A tempo-map change (`PHRASE_ARCS`) needs `--midi-only --tempo`
  on all tracks, and the seconds-spaced re-bow keys in `rebow_fills.json` move with it.
- c13 (`cycles/c13/CHANGES.md`): `score_to_parts.py` `KS_LEAD_S` (seconds; a keyswitch that is not placed in a rest
  goes this long before its note's moved note-on and at least `KS_AFTER_PREV_ON_S` after the track's previous note-on;
  None keeps the old 0.06 qn), `RR_RESET_AT` also on percussion tracks, `ROW_SLUR_OVERLAP_S` values as a list of
  `(from_qn, to_qn, seconds)` spans, `LEG_RAMP_OK` {track: [score onsets]} (level-shape rows meant to act inside a
  listed legato transition are not reported). `deliver_master.py` mix.json `"deliver": {"rise_delay_s"}` (ride gain
  rises run this late, falls stay on time; default 0). The REAPER lock keeps no queue: `cycles/c13/actor_scripts/wait_lock.py`
  waits by the turn rule and takes the lock only when no folder that waited before it is still ahead.
- c13 lock period (`cycles/c13/actor_scripts/`): `phase1.sh` (lock, start, open, settle, range renders, `--midi-only` build, range renders, comparison) and `phase2.sh [--force-memory]` (save, `state_guard.py`, restart, settle, 45 s wait, audio device, `render_cycle.py`, `after_render.sh`); `phase2.sh` stops when the state guard finds a stale track, which is then rebuilt in full. `KS_LEAD_S` is None in the rendered build (range test failed).
- c14 (`cycles/c14/CHANGES.md`): `build_reaper.py` `PRE_RR_RESET` (CC16 127, parts.json `rr_reset_cc`, in the pre-roll of
  every track next to the CC36 reset). `score_to_parts.py` `RR_RESET_ALL_AT` / `RR_RESET_ALL_SKIP` (a CC16 reset on every
  pitched track before its first note at or after each listed score qn: the section starts), `RR_RESET_KS_RESTATE` (the
  keyswitch in force is sent again before such a reset when it lies in a rest; parts.json `ks` entries with
  `"restate": true`), `HP_CURVE` keys `decresc_last_max_qn` / `decresc_last_min_s`, a negative `ROW_SLUR_OVERLAP_S`
  value as a gap. `build/pluck_trims.json` (seconds-keyed level shapes per pizzicato note, read by `score_config.py`
  into `LEVEL_SHAPES_S`; fitted by `cycles/c14/actor_scripts/pluckfit.py`).
- c14 lock period (`cycles/c14/actor_scripts/`): `wait_lock.py`, then `p1.sh` (start, open, settle, `--midi-only --tempo`
  build, two range renders `rr.py render Ra|Rb RANGES`, `p1_analyse.sh`: `rr.py eq` the equality test, `smeas.py` measure
  S per line, `refit2.py`, `pluckfit.py`), then `p2.sh [--force-memory]` (save, state guard, restart, settle, audio
  device, `render_cycle.py 14`, `after.sh`). Each range starts before the last keyswitch that precedes its notes.
- c15 (`cycles/c15/CHANGES.md`): `score_to_parts.py` `STEADY_LINE` (Movement I c54's one-row line, ported by
  `cycles/c15/actor_scripts/port_steady.py`: a span of a track on one row with one lead per class; here also
  `level_default` {row: dB} and `level_all`, so the per-note `level_db` steps reach the span's staccato notes; parts.json
  `steady_line` rows end with the class), `SHORT_SUS_LEG_SPANS`, `RETONGUE_LEAD_SPANS`, `ROW_LEAD_KEEP_GAP`, a track key in
  `LEG_VEL_STRONG`, phrase-arc depth `"light"`. `build/steady_leads.json` (class leads per track and span) and
  `build/steady_levels.json` (per-note level steps) are read by `score_config.py` and fitted by
  `cycles/c15/actor_scripts/fit15.py LABEL S.json --write` on a range render.
- c15 lock period (`cycles/c15/actor_scripts/`): `wait_lock.py`, `p1.sh` (start, open, wait until REAPER's footprint is
  43 GB or more and steady, `--midi-only --tempo` build, range render R1, `analyse`: `smeas.py`, `fit15.py`, `chk15.py`),
  `p1b.sh LABEL` (build of the refitted parts.json, range render, analyses), `p2.sh [--build] [--force-memory]` (save,
  state guard, restart, footprint wait, audio device, `render_cycle.py 15`, `after.sh`). Ranges and segments are in
  `common.sh`; each range starts 2 qn before a `RR_RESET_ALL_AT` point, where the keyswitches are restated.
- c16 (`cycles/c16/CHANGES.md`; the per-note volume automation):
  - `score_to_parts.py`: every volume-envelope item is tagged with the rule that wrote it (`vol_parts.rule`).
    `VOL_PER_NOTE` "on" / "cap3" / "off" (env `STP_VOL_PER_NOTE`; `VOL_PER_NOTE_RULES`, `VOL_PER_NOTE_KEEP`,
    `VOL_RULE_OFF`, env `STP_VOL_OFF=rule,rule`) builds the envelope with the per-note rules on, capped at 3 dB or off.
    `VOL_LIN` (parts.json `vol_lin`: `vol_db` is a piecewise-linear lane), `LEVEL_STEP_AT_SCORE` (level steps cross over
    30 ms centred on the next note's score onset), `ACCENT_FRONT` / `ACCENT_NO_STACK` / `ACCENT_CAP_DB` /
    `ACCENT_SHORT_FLAT_QN`, `SHORT_ONE_LEVEL_QN`, `UNI_BOOST_HOLD_QN`, `ROW_VEL_SPANS`, and the `ART_SPANS` keys
    `max_qn`, `unslurred`, `len_frac`, `vel_metric`, `vel_jit`.
  - `build_reaper.py`: `THIN_DB` (collinear envelope points dropped; env `BUILD_THIN=0` writes every point),
    `DYN_LIN_IN_HAIRPINS`, `CRESC_TRIM_KEEP` with mix.json `cresc_trim_hold` {track: [[from, to]]}, mix.json
    `return_rides` (rows `{"stop": qn, "db": dB}` or `{"pts": [[qn, dB], ...]}`: a volume envelope on the four return
    tracks that carries the fader level plus the ride; removing the key leaves the last written envelope on the
    returns, so write a flat one or delete it in REAPER).
  - `build/steady_rows.json` (one level per row and span group of the one-row theme; `cycles/c16/actor_scripts/
    reduce_levels.py` made it and the reduced `steady_levels.json` from the c15 table; `rowfit.py LABEL --write` refits
    the rows on a range render).
  - Scripts in `cycles/c16/actor_scripts/`: `envstats.py` and `inote.py` (points, points per second, notes moving 3 dB
    or more inside the note), `stepmed.py` (step medians per line, accents), `envsim.py` / `simstates.sh` (an envelope
    change simulated on rendered stems: exact for the dry stems, so on / cap3 / off need no range render),
    `bassband.py` (`sim`, `measure RENDER_DIR`), `stopsim.py`, `crescsim.py`, `bodydiff.py`, `cbtest.py`, `envdump.py`
    (REAPER evaluates an envelope every 5 ms: the thinning check), and the lock phases `p1.sh`, `p1r.sh LABEL
    [--build]`, `p1cb.sh`, `p2.sh`, `after.sh`.
- c17 (`cycles/c17/CHANGES.md`; every per-note level on the instrument side):
  - `tools/instr_post.py` (new; `score_to_parts.py` calls it at the end of each track when `INSTR_POST` is set in
    `build/score_config.py`): `rest_map`, `accent`, `note_cc` (pitch / row by dynamic / chord / beat offsets), `cc_shape`,
    `cc_cap`, `gap_floor`, `gap_set`, `row_onset` (with the keyswitch and CC16 reset moved along), `note_end`,
    `rebow_join`, `vel_pitch`, `vel_db`, `vol_to_cc7`, `vol_guard`, `dyn_step_on`; parts.json `instr_post` per track.
  - `score_to_parts.py` `UNI_BOOST_MIN_QN`, `UNI_BOOST_ONE_LEVEL`; `build_reaper.py` mix.json `region_gain_db`
    {"rows": [prefixes], "pitch_db": {midi: dB}} (per-region volume in the Opus state: a state change).
  - `build/mix.json` is written from `cycles/c17/before/mix.json` by `cycles/c17/actor_scripts/mixfit.py
    cycles/c17/fit_final.json` (dyn_trim make-ups, Timpani gain, basses' region gains and bell).
  - Checks: `cycles/c17/actor_scripts/stepcheck.py build/parts.json` must report 0 moves inside notes; `c17meas.py`
    (`sep`, `sites`, `cb`, `cbp`, `lev`, `stop`, `dip`), `timpmeas.py`, `pluckvel.py`. Range labels must be new names
    (not used in an earlier cycle's range folder). Lock phases: `p1.sh`, `p1r.sh LABEL [--build]`, `p1mic.sh`,
    `p2.sh [--build] [--force-memory]`, `p3.sh`, `after.sh`.
- c18 (`cycles/c18/CHANGES.md`; accents halved, the fader guard at 3 dB/s, subito levels in CC11):
  - `tools/instr_post.py`: `accent` keys `tutti_scale` (scale by the number of staves accenting one onset; `score_to_parts.py`
    passes `accent_staves`), `max_step`, and the bump ends before the note does; `note_cc` `add` (a span offset);
    `cc_shape` `from_note`; `cc_scale` (a passage level in dB as a factor on a lane); `note_merge` (a note tied to the
    same-pitch note before it); `onset_lead` (listed notes start earlier and keep their end); `note_end` `pitch`;
    `gap_floor` `skip_long`; `vel_cap`; `vol_guard` keys `hairpin_ok`, `max_iter`, `rate_short_db_s` / `short_s`, `skip`.
  - `score_to_parts.py` `HP_REL_MAX_DB_S` (the fastest release of a hairpin's dB gain); `build_reaper.py` mix.json
    `region_gain_db` may be a list of specs (one per row group).
  - `build/roles.json` and `build/mix.json` are written from `cycles/c18/before/` by `cycles/c18/actor_scripts/data18.py
    --write` (role rows 267 -> 137, dyn_trim_db in place of the bass instruments' tutti rows, region gains, row volume).
  - Checks: `cycles/c18/actor_scripts/guard18.py build/parts.json` (unprinted moves of 1.5 dB or more steeper than 3 dB/s
    inside a sounding note, on the envelope `build_reaper.py` writes), `envdiff18.py` (the written envelope of two builds
    per track and bar), `meas18.py RENDER_DIR PARTS` (the c18 targets: accents, sfp, chorale bar lines, bar 222,
    pizzicato, introduction, pitch levels; also on one range folder). Lock phases: `autostart.sh`, `p1.sh` (with the
    range round I1), `p2.sh [--build] [--force-memory]`, `p3.sh`, `after.sh`.
- c20 (Dan 17 Nov: too soft on headphones; shared delivery target, mockup-kit/README.md):
  - `deliver_master.py`: -14 LUFS target (`DELIVER_TARGET_I` overrides), knee 7 dB, top ride 10 dB under p95 at 3:1;
    the quiet-lift ratio is still mix.json "deliver" 2.0. Sample ceiling 0.87, and after the mp3 encode the true
    peak is measured: if it is over -1.0 dBTP the ceiling is lowered by the excess and the limiter and encode run
    again. `DELIVER_KEEP_DIR` keeps pre.wav / lim.wav for a per-bar limiter measure
    (`cycles/c20/actor_scripts/deliv_meas.py PARTS MP3 KEEPDIR`: loudness, p10, momentary max per bar, printed
    climax order, limiter gain reduction aligned for the 5 ms look-ahead).
  - `instr_post.py`: `cc_cap` "to_note" (the ceiling ends at the moved note-on of a printed onset), `cc_shape`
    "hold_to" (a step held to a score qn), `vol_set` (the envelope follows a line over a span: held phrase levels,
    hairpin gains kept through an fff arrival), `vel_add` (a velocity offset in a span).
  - `score_to_parts.py`: `PERC_VEL_ADD` (velocity offsets on percussion strokes in a span).
  - `build_reaper.py`: region_gain() reports keys sharing one region with unequal values ("shared": "first" by
    default, "mean" opt-in); `sus_release_cap_ms` may be a list of specs, and a spec with "any_dyn" caps every
    non-RT, non-TLeg group of its rows.
- c21 (`cycles/c21/CHANGES.md`):
  - `deliver_master.py`: loudness loop after the limiter (`DELIVER_LOUD_PASSES`, default 3), top ride 2:1 (`DELIVER_TOP_RATIO`).
  - `instr_post.py`: `short_cc_park` {track: [{"rows", "cc11", "cc1_min", "pre_s", "from", "to"}]} (short-row notes hold CC11 / CC1).
  - `score_to_parts.py`: `STR_REP_NEW_BOW["stroke_fall"]` (CC11 fall on "stroke" / "sus_min_s" new bows; parts.json `stroke_falls`), ART_SPANS on harp tracks.
  - `build_reaper.py`: `sus_release_cap_ms` spec `"set": true` (raise as well as lower), mix.json `ks_keys` / `ks_unused_off` (move KS Master triggers to other keys; the same keys go in `build/ks_maps_extra.json`). A variant parts.json for a range test needs mix.json beside it.


## c22 pipeline notes
- `tools/render_cycle.py` always replaces `render/00_Master.wav` with the 32-bit float sum of the rendered stems (the master has no FX; `MASTER_SUM_ALWAYS=0` keeps the 24-bit file unless it clips).
- New generic keys: mix.json `vel_volume` {"from": patch} (copy a Velocity->Volume path into a KS Master's state) and `attack_cap_ms` (cap sustain-group attacks; tested, unused); score_config `HP_GAIN_AT_DB`; INSTR_POST `cresc_mono`, onset_lead `move_fall` / `fall_cc`, gap_set `allow_leg`, accent rule `from` / `to`.

## c23 pipeline notes
- **The delivered mp3 now starts 0.30 s before score qn 0** (ruling 7: the opening chord's led string attacks were cut by the pre-roll trim). `tools/render_cycle.py` keeps the last `RENDER_HEAD_S` (default 0.30) seconds of pre-roll of every stem in `cycles/cNN/render_head/` (per stem, plus their sum `00_Master_head.wav`); the stems and `render/00_Master.wav` stay on score time. `tools/deliver_master.py` puts env `DELIVER_HEAD` (the head wav) before the file at the first frame's ride gain with a 10 ms fade-in. Anyone measuring the mp3 on the score's tempo map must add 0.30 s (`cycles/c23/actor_scripts/deliv23.py` takes env `DM_HEAD_S=0.30`).
- New generic keys: mix.json `tleg_env` {"rows", "hold_ms", "decay_ms"} (`build_reaper.py tleg_env()`: the AHDSR of the legato-transition groups); INSTR_POST `note_end` key `gap_next_s` (end a note this long before the track's next note-on near `end`), INSTR_POST `onset_lead` key `no_fall` (remove the re-tongue CC11 fall before the listed notes, moved or not); score_config `ROLE_EDGE_XF` {track: {edge qn: (x0, x1)}} (the crossfade window of two chained roles.json rows).

## c24 pipeline notes
- **CC11 law:** on the brass and clarinet KS Masters CC11 is linear volume (20 log10). New INSTR_POST key `cc_scale_k` {track/family: k} sets the k of `cc_scale` rows that give none; score_config sets 20 on brass and clarinets and rewrites every k-40 row there (list in `cycles/c24/CHANGES.md`). Woodwind / string rows keep their fitted k.
- New generic keys: INSTR_POST `accent` `skip_rows` (no CC bump on rows with these prefixes, e.g. "Sus Marc"); `HP_SOFT_ACC_SKIP` entries may be `(qn, track)`; mix.json `deliver` `top_above` (top-ride start re the 95th percentile; env `DELIVER_TOP_ABOVE`).
- score_config c24 env toggles for range tests: `C24_OFF`, `C24_MARC` (on / ab / off), `C24_MARC_VEL`, `C24_MARC_TR`, `C24_VC` (sus / det / off), `C24_AIRPODS`.

## c25 pipeline notes
- New generic options in `tools/score_to_parts.py`: `HP_END_AT_TARGET` {"spans", "within_qn", "max_dyn"} (a crescendo's dB gain gone by the printed mark it ends on, falling at `HP_REL_MAX_DB_S` at most; parts.json `hp_end_tgt`) and `TIMP_ARRIVAL_RAMP` [(at, to)] (a timpani roll at a printed arrival: one dB-linear CC7 ramp from the level before it to the target mark's level; parts.json `timp_arrival`).
- New INSTR_POST keys (`tools/instr_post.py`): `cc_cap` `acc_free` (the ceiling holds the resting lane, accent bumps go on top); `cc_shape` `no_pre_cap` (the accent's pre-note ceiling does not clip the shape).
- `tools/fit_rebows.py --cc11 DB_PER_UNIT` writes fitted re-bow shapes as CC11 offsets into `build/rebow_cc11.json`, which score_config reads into `cc_shape` (the volume-envelope fills are off under Dan's no-per-note rule).
- score_config c25 env toggles: `C25`, `C25_OFF`, `C25_RBC` (basses' re-bow CC11 depth), `C25_V1CC` (the withdrawn Violins I chord CC11 scale), `C25_BD` (36in / 40in bass drum); `C24_VC` now defaults to "det".

## c26 pipeline notes
- New generic options in `tools/score_to_parts.py` (defaults off): `HELD_DECRESC_LED_RELEASE` (True or {track/family: release s}: a held decrescendo's level is reached at the led next note's moved onset and released from there, or in a rest of 0.15 qn or more before it; parts.json `held_decresc_led`), `UNI_HOLD_END_REST` (a held unison level released in the rest before a led note), `CHORD_SEG_EDGE_REST` (a printed player-count level steps in the rest before its led note); `TIMP_ARRIVAL_RAMP` rows may be (at, to, cc7_start, cc7_end).
- `CC7_POINTS` (mvt1 c36 test lane) is used for passage levels inside the patch (manual p.64 / p.151), edges in rests.
- `tools/deliver_master.py`: the room-noise bed (`DELIVER_ROOM_BED_LUFS`, default -60, "off"; mockup-kit/README.md "Room-noise bed in the delivery"), added after the limiter and before the encode.
- Pre-render gate: `cycles/c26/actor_scripts/stepcheck.py` and `guard26.py` (exit 1 on an unprinted move of 1.5 dB steeper than 3 dB/s inside a note; `--strict` drops the edge window; printed hairpin ramps and printed dynamic steps are listed).
- score_config c26 env toggles: `C26`, `C26_OFF`, `C26_WIND` (wind-solo variant per track: A / B / C / 0), `C26_MARC_VEL` (0 = c24's v92), `C26_BRASSCAP` (the withdrawn 1043.8-1047.85 brass CC11 ceiling).

## c27 pipeline notes
- `tools/score_to_parts.py` `ROLE_EDGE_IN_REST` (default on: {"min_gap_s": 0.012, "max_ramp_qn": 0.5, "carry_qn": 64, "carry_ramp_s": 0.25}): every roles.json edge ramp that overlaps a sounding note moves into the rest before the note nearest the edge; with no rest there, the envelope edge moves to the nearest rest (before a rise, after a fall) and CC7 carries the change between that rest and the edge (parts.json `role_edge_moved`, `role_edge_join`). It reads the played note spans of the previous run's parts.json (env `STP_ROLE_SPANS`, default `build/parts.json`), so **after any change of notes run score_to_parts.py twice**. A `ROLE_EDGE_XF` window is taken as given. c28: a note starting at the edge (up to `edge_note_qn` 0.05 after the ramp) is the edge's note; the CC7 carry ramp sits on that note-on only when it starts within `carry_at_edge_qn` 0.5 of the edge, else on the row's own edge ramp, no faster than `carry_rate_db_s` 2.5 inside a held note. c29: `step_at_note_on` (on): instead of a ramp inside a held note, the change is a step just before the note-on of a note starting up to `step_next_qn` 0.25 after the edge; a rise whose held note starts within `step_held_max_qn` 4.5 before the edge moves into the rest before that note; a held note that ends at the edge followed by a rest takes the edge in that rest (parts.json `role_edge_moved` "step" / "rest_after"). End-ramp rows ([a, b, dB, end_ramp]) become shapes: the slow end ramp stays when it moves 2.5 dB/s or less.
- `tools/build_reaper.py`: mix.json `dyn_trim_to_cc7` {"tracks": "all" | [names], "except", "families_except"} moves the dynamic trims (dyn_trim_db / soft_trim_db with their holds) out of the volume envelope into CC7 (`TRIM_CC7`, `cc7_lane()`): the envelope holds gain + vol_db + the track's largest trim, CC7 = the lane's CC7 x 10^((trim - largest) / 20), held in rests like the envelope. c28: a trim-lane change point within `TRIM_CC7_ONSET_QN` 0.15 qn after a moved note-on moves to `TRIM_CC7_ONSET_PRE` 0.003 qn before it (trims on moved time). c29: a trim step of 1 dB or more up to `TRIM_CC7_LEG_PRE_QN` 0.1 qn before a moved note-on while an earlier note still sounds across it (a legato overlap ending within `TRIM_CC7_LEG_MAX_OV` 0.12 qn after the note-on) moves to `TRIM_CC7_LEG_POST` 0.003 qn after the note-on; `ENV_MAX_DB` 23.5: with trims in CC7 the excess over it comes off the envelope and goes into the CC7 trim lane (level-neutral; logged in `ENV_SHIFTED`), any envelope still above it fails the build (REAPER stops at +24 dB). A `--mix-only` build does not rewrite CC7: after a trim change use `--midi-only`. `SOFT_DECRESC_KEEP` is 0 (env `BUILD_DECRESC_KEEP`).
- Gate before the render: `cycles/c27/actor_scripts/guard27.py PARTS` (entry window: 1.5 dB in the first 0.35 s of a note; inside moves steeper than 3 dB/s with no edge window; only fp / sfp falls exempt; printed-hairpin moves listed as `entry_hp` / `inside_hp`).
- score_config c27 env toggles: `C27`, `C27_OFF`, `C27_CA` (a / b / 0: cor anglais bars 171-186), `C27_V2` (marc / sus: Violins II's accented chords), `C27_CB` (lead / cc7: the basses' pp re-bows).
