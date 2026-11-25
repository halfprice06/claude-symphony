# Cycle 57: changes (actor)

Render: `cycles/c57/render/` (main pass, pass 2, then three level-only stem fixes; originals of the master and the
changed stems in `render_first/`). Delivered: `cycles/c57/mvt1-mockup-c57.mp3`. Data as rendered:
`cycles/c57/rendered_build/`; `build/` is that plus the level-only balance rows described under "After the render".
Nobody listened. Every figure is measured on dry stems or the master; simulated figures are marked.

## Work order
The coordinator changed the method during the cycle (Dan, 2026-11-11: "i want to nuke all the volume adjustments per
note"). Decision 1 (1a-1f) of `COORDINATOR-NOTES.md` was replaced: the track volume envelope carries slow balance only,
on every track, with no exceptions; faults are fixed on the instrument side or left audible and listed. Decisions 2-7
stand, on the instrument side. The code and tables written for 1a-1e before the change (scaled theme levels, the
`NOTE_LEVEL` "edges" pass and `build/shape_edges57.json`, `EARLY_FILL_SCALE`, Violins II row trims at half, removed
Violas note trims, re-bow residual refits, Oboe 1 fills, celli loop cut) are still in the tools and tables but have no
effect: their rules no longer reach the envelope.

## 1. The envelope: slow balance only
- `tools/score_to_parts.py` `VOL_SLOW_ONLY` (new, generic; values in `build/score_config.py`): the items of 33 per-note
  rules are left out on every family (accent swells and bodies, join fills, crescendo fronts, syncopation / pair /
  tenuto shapes, repeated-note dips, theme body lifts and level steps, re-bow and loop fills, notches, breath dips,
  long-note swells, held-note diminuendo, bloom cuts, pitch trims, note trims, metric steps, pickup lifts, row trims,
  phrase tops, unison fade, arrival weight, parked-CC returns, timpani re-strike dips). `NOTE_LEVEL` is off.
- Config level shapes (`LEVEL_SHAPES`) stay only as phrase-level rows: 2 s or more over two or more onsets (263 of
  1347 items; tag `shape_slow`). The three percussion tracks (tam-tam, cymbals) are built by their own code and keep
  their stroke shapes (59 / 1 / 49 envelope values); the timpani patch has no CC11, so its printed dynamics and roll
  settle stay in the envelope.
- Balance rows ("carry", `build/balance57.json`, `cycles/c57/actor_scripts/balance57.py`): per track and bar, the mean
  level the dropped layers gave that bar on the c56 stem, where it is 2 dB or more; neighbouring bars within 1 dB are
  merged; 1 qn ramps. 375 rows on 32 tracks. They are level rows of a bar or more, not per-note moves. Without them the
  theme stood 14 dB over the celli (simulated) and single tracks moved 5-11 dB in single bars.
- `tools/build_reaper.py` `ENV_THIN` 0.1 dB -> 0.5 dB (steps up to 3 dB, 16 qn).
- Table (`cycles/c57/envelope_table.md`, per track): points 32712 -> 6962; points per second on the strings 5.0-9.6 ->
  0.9-1.35, winds and brass 1.0-4.5 -> 0.2-0.8 (references 0.01-0.4); notes with 3 dB or more inside (moved note-on to
  note end) 2137 -> 720, 6 dB or more 795 -> 209, strictly inside the note 1063 -> 424; **envelope items from a
  per-note rule: 0 on every track of the table** (read from a dump of the shipped build by rule name). What still moves
  inside notes is hairpin gain, dynamic trims through hairpins, role edges, the bar rows' ramps and the timpani's
  dynamics. CC11 / CC1 points per second per track are in the table; 504 notes have 12 or more CC11 units of movement
  inside (hairpins, phrase shapes, wind re-tongue falls; none of it added this cycle).

## 2. Instrument-side changes
- Theme (Violins I 56-127, 128.4-158, 536-576): Sus MAX on every note in place of Sus Marc LITE with body lifts
  (`build/theme_row57.txt`), class leads fitted in one step (`build/steady_leads57.json`: slurred 80, new bow 62, after
  a rest 29, repeat 50 ms), then per-note leads on 103 notes (`build/steady57_at.json`, lead + 0.8 x S where S was 12 ms
  or more off). Range renders, each twice, second kept:
  | bars 15-22 | S robust SD / over 40 ms | long notes front minus tail |
  |---|---|---|
  | Sus Marc LITE, no lifts | 7 ms / 0 | 7.5 dB (fails 3) |
  | Sus MAX, one lead per class | 27 ms / 4 (fails 12) | -2.9 dB |
  | Sus MAX, per-note leads (shipped) | 10 ms / 1 | -1.6 dB |
  Full render: 9 ms / 1 and -1.9 dB: both guards pass. Other spans on the full render: 56-127 10 ms / 5 over 40;
  536-576 17 ms / 7 over 40 (not at the guard). Violins II, Violas and celli keep Sus Marc LITE without lifts.
- Repeated notes: `REP_MIN_GAP` (new, generic): every same-pitch repeat gets a real note-off gap (strings 90 ms, winds
  65, brass 100; at most 40 % of the slot; not on short, tremolo or plucked rows or re-bow pieces): 395 repeats
  shortened (basses 152, Violas 139). Basses' Sus MAX release at mf-ff 150 -> 80 ms.
- Per-pitch levels: `mix.json` `region_gain_db` (port of the scherzo's c15 tool): the pitch trims of
  `build/pitch_trims.json` are region volumes inside Opus on 13 tracks (the "_skip_onsets" and the horns' F4 shape
  cannot be carried). This carries decision 2.
- Decision 6: `PHRASE_SHAPE["types"]["drive_max_mean_qn"] = 2.0`: 103 held phrases take no "drive" shape (list with
  levels: `cycles/c57/checks57.txt`); Horn 3 / Horn 4 `soft_trim_db` p +2.0. Horn 3 note trims at 652 / 654: dropped
  (per-note volume).
- Decision 7: `SHORT_SUS_AT` celli 408.0, Violins II 404.5. The other items of 7 were per-note volume and are dropped.

## 3. Faults at audible size, c56 render -> c57 render (`faults57.py`, `faults_c56.txt`, `faults_c57.txt`)
| | c56 | all per-note layers off, c56 MIDI (simulated) | c57 render |
|---|---|---|---|
| join holes (6 dB or more for 80 ms or more) | 44 | 45 | 25 |
| same-pitch repeats under 3 dB of separation | 83 of 425 | 158 of 425 | 82 of 406 |
| re-bow holes (6 dB for 80 ms) | 1 of 87 | 12 of 86 | 16 of 87 |
| long notes sagging 6 dB or more | 84 | 70 | 62 |
| pulse on a held note (6 dB) | 13 | 17 | 17 |
| pitches 4 dB or more out of their line | 18 | 25 | 23 |
Left audible (not patched with volume):
- Re-bows, 16: Violins I 44 (14.0 dB); Violas 36 (11.9), 296 (8.4), 725.5 (10.6); celli 26.5 (13.8), 180 (9.6), 289.1
  (8.0), 298.4 (11.1), 717.6 (9.9), 721.9 (8.5); basses 38.0 (13.9), 47 (9.6), 50.3 (7.1), 297.0 (16.2), 714.7 (8.6),
  720.0 (7.8). Cause: our own split of the long note (a new Sus MAX piece after a 0.03 qn gap; the new attack is slow).
  Tried: nothing that works; same-pitch pieces cannot overlap on one track. Not tried: the scherzo's proposals (a second
  instance with interleaved re-bows; no re-bow on exposed notes).
- Basses' repeated eighths: 26 of 139 repeats under 3 dB (c56 18 of 141); bars 27-30 read 2.4-3.0 dB with the 90 ms
  gap (range test: 16 of 33 under 3 dB at the 150 ms release, 13 of 33 at 80 ms). Violas 7 of 85 (c56 16 of 87).
- Pitches 4 dB or more out (winds mostly; the region gains follow the old trim table, which did not hold them all):
  Flute 2 Eb6 +11.0, F6 +7.9, Db6 -6.8, C6 -6.6; Flute 1 D6 -8.8; Bassoon 1 Ab3 -7.7; Horn 1 D4 +6.8; Violins II D4
  +6.7; basses Ab1 -5.7; the rest in `faults_c57.txt`.
- Accents: no envelope swell any more and nothing put in its place (velocity does nothing on sustain rows; the
  finale's fix, a lower resting CC11, was not tried). Not measured on the render.
- Theme over the celli, bars 15-22 (Violins I minus celli per quarter): median +4.4, lower quartile **+1.7** (target
  3.9; c56 +3.56): fails. The per-note levels that evened the quarters are gone; the bar rows hold the bar means only.
- 15 bars of the master are more than 1.5 dB over c56 (bar 21 +5.5: Violins II's bars 20-21 lost a -12 dB note shape;
  bar 182 +5.4; bar 85 +4.3; bar 7 +3.1), 1 bar more than 1.5 dB under.

## 4. Decisions 2-6, measured on the render
- 2 (basses): F2 notes -4.0 to -5.8 dB against c56 (bars 10, 38, 68, 111), Db2 bar 44 -1.1; Horn 1 solo minus basses
  in bar 44 -3.4 -> +2.9 dB. The 172.0 / 42.0 note trims were dropped (per-note). Not re-run: critic B's per-pitch
  residual table.
- 3: roles celli `[56, 88, -2]` is in; the target is not met (above).
- 4: Cello solo R-L +6.0 -> +2.7 dB (target 2.5-4: pass), stem correlation 1.00 (target 0.85 or less: **fails**, the
  DIV A patch is one close microphone pair summed; the Main-mic alias track was not built); master bars 171-174 R-L
  +5.6 -> +3.0 (pass), correlation 0.90 (fails 0.80). Clarinet 2 correlation 0.48 -> 0.85, R-L -3.6 -> -2.7;
  Contrabassoon 0.28 -> 0.68, R-L +6.8 -> +3.8, gain +0.4 dB after a range render (Clarinet 2's gain not re-matched: the
  range reading, +2.35 dB, included its region gain). R Brass +1.5 dB whole file (Trumpets 1-3 send +6); R Perc -3.7 dB
  (timpani -6, harp -4). Trumpet `rt_gain_db` +18 range test: not done.
- 5: basses `loud_eq` half step and `master_eq` 3b are in. Master share in the loudest 10 % of frames: 56-90 Hz -20.1 ->
  -18.4, 90-180 Hz -11.1 -> -10.9; whole file 70-112 Hz -13.6 -> -13.2. Delivery loudness and peak inside the guard
  (below). The "no bar up more than 1.5 dB" guard fails for the reason in section 3, not from the EQ (not separated).
- 6: Horns 3-4 bars 19-22, last 30 % minus first 30 % of the phrase: Horn 3 -7.5 -> +0.5 dB, Horn 4 -11.9 -> -4.7
  (target within 3: Horn 4 fails by 1.7), Bassoon 1 72-88 -4.7 -> 0.0, celli 136-183 -15.8 -> -8.5.

## After the render (level only, `tools/stem_fix.py`, in the main REAPER project)
1. Violins I: ten 16 qn rows for the Sus MAX spans (the c56-minus-c57 stem level, +1.1 to +5.6 dB; the first balance
   rows were fitted for the Marc row). 2. Bar rows in place of the first 16 qn rows on 31 tracks. 3. Basses' bar rows
   refitted against the c56 trims (the first fit had cancelled decision 2). The return stems were summed unchanged, so
   the hall share of the changed tracks is as rendered. The pass-2 project holds the 16 qn rows of its tracks (only
   Violins I f62 was rewritten); the next pass-2 build writes the bar rows.

## Render conditions
- Lock: waiter from 10:13; held 13:32-15:59 (build 13:33-13:55 with 14 full rebuilds, range renders to 14:40, a first
  render attempt refused by the state guard, main render 15:03-15:15, pass 2 to 15:39, data and saves to 15:59).
  Nothing taken by hand. `p6.sh` and one run of `p7.sh` were stopped by me while they waited for the project to settle
  (before any bridge job), to write all tracks instead of one.
- State guard: 0 stale at the start and after the build; 4 stale before the first render attempt (Double basses,
  Trumpet 2, Violas, Violins II, after the range renders), rebuilt in full; 0 before and after the main render; pass 2
  0 before, 2 after its save (Bassoon 1 stac, Flute 1 stac), rebuilt; 0 at both quits.
- Memory: REAPER 43 GB before, 44 GB after the main render; pass 2 19-20 GB. Attack probe: late or hole 0. Disk 50 GB free.

## Delivery
-19.7 LUFS integrated, LRA 14.3 LU, true peak -2.0 dBTP, limiter 0.0 dB, p10-to-max span 18.6 dB, 433.65 s.
Master: -20.8 LUFS, LRA 22.7 LU, true peak -1.3 dBFS. Bar 160 -14.6, bar 122 -15.5, bar 26 -18.2 dB (master RMS).

## For Dan
- `cycles/c57/ab3/`: three states of c56 (as rendered / shape class off / all per-note layers off), four passages, mix
  and leading string stem, made offline from the c56 stems (README.txt there).
- `cycles/c57/ab/`: bars 15-23, c56 then c57, master and Violins I stem, one gain for both halves.

## Tools
`tools/score_to_parts.py`: `VOL_SLOW_ONLY` (drop, slow_tags, carry), `REP_MIN_GAP`, `PHRASE_SHAPE` types
`drive_max_mean_qn` (kind "flat"), `NOTE_LEVEL` "edges", `EARLY_FILL_SCALE`, tag `timp_restrike`, debug `STP_DROP_TAGS`.
With none set parts.json is byte-identical to c56 (checked before the method change; not re-checked after
`VOL_SLOW_ONLY`, `REP_MIN_GAP` and the tag rename were added). `tools/build_reaper.py`: `region_gain`, `ENV_THIN`
values. `cycles/c57/actor_scripts/`: `lib57.py`, `faults57.py`, `balance57.py`, `carryfix57.py`, `table57.py`,
`checks57.py`, `ab3_57.py`, `abclips57.py`, `fitleads57.py`, `fitat57.py`, `susiter57.sh`, `rt57.sh`, `edits57.py`,
`edges57.py`, `rebowres57.py`, `widthgain57.py`, `p1.sh`-`p7.sh`, `wait_lock.py`.

## Not done
Legato overlap 45-80 ms and legato velocity; accents by velocity or a lower resting CC11; per-row levels in the Opus
state; note-on CC11 or velocity for the pitches still out; re-bow cause removal; Cello solo Main-mic alias; trumpet
release gain test; MANUAL-GAPS (none tried); EW-TEMPLATE-PLAN sections 5 (overlap), 6, 7, 10 still not applied, section 8
repeat gaps now applied.

## Not verified
Accent levels and their 2-5 kHz fronts; timpani stroke decays after the R Perc change and the timpani without re-strike
dips; tutti-stop decays; the trumpet tails after the send change; loop pulsing folded at 3.95 s; the theme's S outside
Violins I after the row change of the neighbours' balance; Clarinet 2's level after narrowing; whether the note-off gaps
are heard as separation on winds and brass (only the fault count was read); the three-state clips and the mp3 by ear.
