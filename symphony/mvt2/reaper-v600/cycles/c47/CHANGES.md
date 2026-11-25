# Cycle 47 (actor): last cycle before Dan listens; level and timing data only

Rendered 2026-11-09 11:26 (`cycles/c47/mvt2-mockup-c47.mp3`), one render, no stem fix.

Lock and drive. The data work was finished by 08:55. The first turn (lock 10:16:30) came with 25 GiB free, under the 30 GB
rule (other threads' renders since 08:53): REAPER was started and opened, then quit with no build, and the lock released
at 10:20 (`NOTES-interrupted.md`). Resumed on the coordinator's word (31 GiB free): lock 10:59:42-11:35:54 (36 min, plus
3.5 min in the first attempt). Open settled at 44 GB in 11 min; the 22-track `--midi-only` build took 20 s (no full
rebuild; each string track gained the 3 fade points); restart, settled at 43 GB with 0 compressed in 10 min; disk 56 GiB;
`_c47_audio_init.lua` (48000 Hz, 512, no input); `render_cycle.py 47` at once, no `--force-memory`.

## Results (c47 render; c46 in brackets)
- Master -22.9 LUFS (-23.0), LRA 23.4 (23.4), true peak -3.5 (-3.4), no clipping. Delivered -19.8 LUFS, LRA 15.3 (15.4),
  TP -1.6, p10-to-max span 18.8 dB (18.9), limiter 2.0 dB (2.4), length 354.65 s (354.70). Bars 61 / 62 still the
  loudest (-16.7 / -17.6, unchanged); bar 60 -20.6 (-20.9). Attack probe: late or hole 0.
- REAPER memory: 43 GB / 0 compressed before the render; 44 GB / 16 GB compressed after.
- The simulated numbers held in the render, most within 0.5 dB and all within 1.5 dB (the bass clarinet close, where
  CC7 acts before the release; `m47_render.txt`; the simulated values are under "Simulated" below): Oboe 1 joins 143 / 146 / 47 stem holes 8.7 / 7.8 / 6.6 -> 1.2 / 3.2 / 1.8 dB; celli 140 / 240 / 248.5
  12.2 / 9.4 / 7.5 -> 6.4 / 5.5 / 2.7; Flute 1 113.5 7.2 -> 5.1; bass clarinet 92 / 92.5 master dips (C) 8.1 / 6.8 -> 5.1 /
  5.0; Clarinet 1 283 C master 4.0 -> 3.4; Oboe 1 bar 80 -27.1 / -27.6 -> -34.8 / -35.6 K (no longer among bar 80's three
  loudest stems); the bass clarinet close falls -49.7 / -49.9 / -50.5 / -52.2 over 273-273.75 (was -48.5 / -46.9 / -45.0 /
  -43.7); Horn 1 minus Violins I at 196-203 -6.0..-1.4 -> -3.4..+1.1; timpani 277 -44.7 -> -42.2 (level with 278.5 / 279);
  Horn 1 229-232 per beat -39.3 / -43.6 / -46.2 / -47.3 (was -39.4 / -46.2 / -46.2 / -47.3).
- C #2 wind entries (body - 6 dB re the beat, `entries47.txt`): median -38 -> -6 ms (C predicted about -6); entries more
  than 60 ms early 8 -> 0; bar 79 winds -116..-30 -> -20..+18 ms (C predicted -18..+14); Clarinet 1 280 -134 -> +16,
  Bassoon 1 196 / 229 -96 / -118 -> +10 / -10, Flute 2 262 -116 -> +18.
- Final chord (master, check44): time to -20 dB 0.479 -> 0.404 s (guard 0.45; recordings 0.43-0.58), drop at +0.15 / +0.3
  s 0.7 / 9.1 -> 4.0 / 14.1 dB; steepest 50 ms fall 4.9 dB; every string stem's steepest 50 ms fall unchanged (Violins I
  9.1, celli 8.5, violas 8.9, basses 13.3 dB, the samples' own releases). The render is 0.03 s shorter than the simulation
  because the post-fader sends carried the fade into R Strings too.
- Wetness (check44 family stops): strings / winds / brass t20 0.381 / 0.304 / 0.253 s, unchanged.
- Solo margins (check44): cor anglais bars 41-44 1.2 -> 2.5 dB (C's target about 2.5), Oboe 1 bars 15-16 7.2 -> 8.1, Oboe
  1 bars 45-47 5.5 -> 5.8, Horn 1 bars 7-14 7.2 -> 7.8, Horn 1 bars 67-70 8.0 -> 8.4, Clarinet 1 bars 85-89 3.2 -> 3.7;
  cor anglais minus Flute 1 per 2 beats from 126: +2.5 +4.6 +0.5 +3.6 +5.3 +3.5 -0.4 (c46 +0.5 +2.6 -1.2 +2.8 +3.2 +3.5
  -0.4; the linear flute hairpin added 0.8-2.1 dB at 132-134 over the simulation).
- S1 (s1check44, 49 points): own-band median 8.2 -> 7.4 dB, under 3 dB 7 -> 8, master median 3.7 -> 3.8. Changed: the bar
  80 repeats at 265 in the master 2.4 -> 3.8 dB (the oboe trim); bass clarinet 265 own-band 12.8 -> 1.5 dB with its
  broadband stem dip unchanged (5.8 -> 5.5) and its note data unchanged apart from the 262 entry starting 25 ms later;
  Bassoon 2 21 master 2.6 -> -1.0 (the bass clarinet's -4 trim on its 18 note lowers the master's reference; the
  bassoon's own dip 8.0 -> 6.7).
- S2: pcX joins (median) Violins I +15 ms (+16), Violins II +14 (+15), Violas +3 (+7), Oboe 1 +39 (+45).
- State check (c46 -> c47, same tempo map): no level runs; flagged unchanged notes within ±0.7 dB except Violins II 218
  +3.2 dB; one Violas "timing run" (251-258, 6 notes) whose pcX values alternate -109..+98 ms with levels +0.0..+0.6 dB:
  estimator spread (robust SD 61 ms), not a state flip (the violas' data changed only after qn 304).
- Master: band shares within 0.1 dB of c46 (100-250 Hz -7.39, 2-6 kHz -10.01, 6-20 kHz -29.48); side/mid -5.45 dB, L/R
  correlation under 250 Hz 0.63.

## Changes (files and parameters)

All changes are data (volume envelope, CC7, CC11 shape, note leads). No Opus state changed (no articulation row added or
dropped, no mic, hall, seat or mix.json change), so every changed track took `build_reaper.py --midi-only`. Each level
change was simulated on the c46 stems before the render (`actor_scripts/sim47.py`: the volume-envelope difference through
build_reaper's own `vol_points()`, as stem_fix does, plus the CC7 difference as a gain; the returns not re-simulated) and
measured with the critics' own methods (`actor_scripts/m47.py`; critic A's lower-body join hole and 200 ms overshoot,
critic C's join dip against the previous note, 50 ms pre-onset peak over the previous body).

Tools (generic):
- `tools/score_to_parts.py`: an `env` shape that starts at or after END (a LEVEL_SHAPES fade over the last release) is
  kept after END on top of the held level and holds its last value; parts.json `post_end_shapes` lists such shapes.
- `tools/build_reaper.py` `vol_points()`: `post_end_shapes` are added on top of the last-rest tail hold (c19), which had
  dropped any envelope change after a track's last note. Without this, C #4's fade never reached REAPER (simulated: no
  change at all).

Per-note tables (`build/`):
- `early_fills.json` (critic A #1, hand entries marked in `_auto`): Oboe 1 47 {4.0, pre_s 0.14, hold 0.08}, 142 {4.0,
  0.06, 0.08}, 142.5 {3.0, 0, 0.15}, 143 {6.0, 0.12, 0.10}, 146 {4.6, 0.09, 0.10}; Violoncellos 140 {8.0, **0.10**, 0.32},
  240 {6.6, **0.12**, 0.19}, 248.5 {4.8, 0.13, 0.14}; Flute 1 113.5 {4.2, 0, 0.17}; Bass clarinet 92 {4.0, 0.09, 0.10}.
  The two celli pre_s values are shorter than A's 0.18 / 0.26 (see Deviations). C #1 (auto_fills on the bass clarinet,
  Horn 1 and Clarinet 1, kept where the simulation was better): Bass clarinet 92.5 {3.5, 0, 0.10}.
- `note_trims.json`: Oboe 1 139 2 -> 6, 145 +5 (A #2), 266 -8 (B #1); Bass clarinet 18 / 24 / 39 -4 (B #2, its optional
  part).
- `roles.json`: Horn 1 + [198.0, 203.9, 2.5] (B #4); Flute 1 [125.75, 131.5, 3, 0.5] -> 1 dB (C #3); Horn 4 [86, 90, -5.5]
  deleted (C #5, replaced by a LEVEL_SHAPES fall).
- `entry_leads.json`: Clarinet 1 280, Flute 2 262, Bassoon 1 196 and 229 deleted (C #2).

Config (`build/score_config.py`, c47 block at the end):
- `NOTE_TRIM_RAMP_S["Oboe 1"]` 139 / 145 / 266: 0.1 s (steps).
- `CC7_POINTS["Bass clarinet"]` (272.75, 127), (273.0, 101), (273.25, 82), (273.5, 57), (273.75, 40), (275.5, 40), (276.0,
  127) (B #2).
- `HP_CURVE["linear"]` (B #3): Violins II and Violins II div (42, 47), Flute 1 (131, 136), Violoncellos (124, 132),
  Violoncellos div, Double basses and Violas div (283, 286). parts.json `hp_curved` lost exactly these 10 hairpins.
- `LEVEL_SHAPES["Timpani"]` + [(276.96, 0), (276.99, 2.5), (278.3, 2.5), (278.45, 0)] (B #5).
- C #2 wind entry leads: `ENTRY_LEAD_S["Bassoon"]` (0.03, 0.03), `["Contrabassoon"]` (0.02, 0.02); `ENTRY_LEAD_ART_S`
  wind Leg Slur MAX 0.03, Leg Slur 0.04, Sus Non Vib 0.04, Sus MAX 0.02, Flute 1 keeps 0.06 / 0.11 / 0.07 / 0.05. 54
  wind onsets moved later, median 30 ms (Clarinet 1 70 ms on its Leg Slur row, 130 ms at 280; Flute 2 262 130 ms;
  Bassoon 1 196 / 229 90 / 130 ms).
- `LEVEL_SHAPES["Horn 4"]` + [(84.5, 0), (86.5, -5.5), (90.0, -5.5), (90.5, 0)] (C #5).
- `LEVEL_SHAPES` on Violins I, Violins II, Violas, Violas div, Violoncellos, Double basses: [(304.0, 0), (304.1, -4.0)]
  (C #4, the final-chord fade; held to the end).
- `LEVEL_SHAPES["Horn 1"]` + [(229.95, 0), (230.1, 3.0), (230.85, 3.0), (231.0, 0)] (C #1c).
- `CC7_POINTS["Clarinet 1"]`: the c38 dip (85 from 282.75) now ends at 283.0 instead of 283.3 (C #1b, see Deviations).

## Simulated before the render (c46 stems; c46 -> c47 data; the render confirmed these)

Joins (A: stem hole below the lower body, 200 ms overshoot | master hole; C: stem | master dip re the previous note):

| join | A c46 | A sim | C c46 | C sim |
|---|---|---|---|---|
| Oboe 1 47 | 6.6 +0.6 / 2.6 | 1.8 +0.7 / 1.6 | 3.8 / 3.5 | 3.4 / 3.1 |
| Oboe 1 142 | 6.4 +0.3 / 1.1 | 3.4 +0.9 / 0.3 | 7.0 / 2.1 | 4.8 / 1.7 |
| Oboe 1 142.5 | 4.3 +0.2 / 1.9 | 4.3 +0.3 / 2.3 | 5.2 / 2.4 | 4.8 / 2.2 |
| Oboe 1 143 | 8.7 +3.1 / 2.3 | 1.2 +0.5 / 1.3 | 14.2 / 5.1 | 6.2 / 3.3 |
| Oboe 1 146 | 7.8 0.0 / 4.1 | 3.2 0.0 / 3.1 | 9.3 / 4.2 | 4.5 / 3.0 |
| celli 140 | 12.2 0.0 / 4.3 | 6.4 +0.8 / 5.0 | 13.1 / 4.7 | 6.6 / 5.9 |
| celli 240 | 9.4 +0.4 / 3.0 | 5.5 +0.3 / 1.1 | 5.6 / 3.7 | -0.6 / 1.9 |
| celli 248.5 | 7.5 +0.1 / 2.0 | 2.7 +0.4 / 1.4 | 9.7 / 2.7 | 5.1 / 2.1 |
| Flute 1 113.5 | 7.2 +0.7 / 1.3 | 5.1 +0.5 / 1.8 | 9.6 / 3.2 | 5.4 / 2.6 |
| bass clarinet 92 | 5.9 +1.1 / 5.6 | 2.1 +1.8 / 3.2 | 10.8 / 8.1 | 6.9 / 5.9 |
| bass clarinet 92.5 | 4.7 -1.7 / 3.3 | 2.3 -1.8 / 1.9 | 7.2 / 6.8 | 4.9 / 5.5 |
| Horn 1 230 | 0.1 / 0.3 | 0.1 / 0.3 | 10.0 / 7.1 | 8.5 / 6.0 |
| Clarinet 1 283 | 5.3 0.0 / 0.5 | 3.7 0.0 / -0.4 | 10.0 / 4.0 | 6.5 / 2.9 |

The celli 140 master hole reads larger (4.3 -> 5.0) only because A #2 raised Oboe 1's 139 pickup, the reference; the
master's minimum rose 1 dB (-52.7 -> -51.7 dB).

Other simulated checks (c46 -> sim):
- A #2 Oboe 1 bodies: 139 -53.2 -> -48.9 (140 -44.1: a pickup 4.8 dB under), 145 -51.4 -> -46.4 (neighbours -45.6 / -46.5).
- B #1 bar 80, K per qn 266 / 267: Oboe 1 -27.1 / -27.6 -> -34.8 / -35.6 (Violins I -29.9 / -31.4, Clarinet 1 -34.6 /
  -34.9); master -0.6 dB.
- B #2 bass clarinet 272.5-274.25 (K per 0.25 qn): -49.1 -48.5 -48.5 -46.9 -45.0 -43.7 -49.4 -> -49.1 -48.5 -50.5 -50.7
  -51.9 -53.7 -59.4; master -37.7 -40.2 -40.0 -39.8 -> -38.0 -41.0 -41.7 -42.4 over 273.0-273.75. A flat 2 bodies 18 / 24
  / 39 -51.7 / -50.8 / -51.6 -> -55.7 / -54.8 / -55.6 (its notes at 21 / 29: -56.0 / -53.2).
- B #4 Horn 1 minus Violins I per beat 196-203 (K): 0.2 -2.2 -6.0 -1.4 -5.3 -1.9 -3.0 -7.1 -> 0.2 -1.9 -3.5 +1.1 -2.8
  +0.6 -0.5 -4.7; master bar 60 +0.2 dB, bar 61 unchanged and still the loudest.
- B #5 timpani 277 / 278.5 / 279 peaks -44.7 / -42.0 / -42.4 -> -42.2 / -42.0 / -42.4.
- C #3 cor anglais minus Flute 1 (A-weighted, per 2 beats from 126): +0.5 +2.6 -1.2 +2.8 +3.2 +3.5 -0.4 -> +2.5 +4.6 +0.5
  +2.8 +3.2 +3.5 -0.4 (the linear flute hairpin at 131-136, CC11, not simulated).
- C #5 Horn 4 84: largest 1 s swing 12.2 -> 9.3 dB (C's keep rule was under 5 dB; the rest is the sample's own loop dip
  at +1.8..+2.7 s; the master is unchanged there, the horn 10-17 dB under it).
- C #1c Horn 1 A-weighted per beat 228-235: -42.1 -39.4 -46.2 -46.2 -47.3 -49.5 -51.5 -52.7 -> -42.1 -39.3 -43.6 -46.2 -47.3
  -49.5 -51.5 -52.7 (the printed 229-235 decrescendo now falls every beat).
- Final chord (master, 50 ms RMS): t20 0.475 -> 0.430 s, drop at +0.15 / +0.3 s 0.8 / 9.1 -> 2.7 / 13.0 dB, steepest 50
  ms fall 5.2 -> 4.8 dB; every string stem's steepest 50 ms fall unchanged (the fade is 0.67 dB per 50 ms), so the release
  is not clipped.
- Delivery (deliver_master on the simulated master): LRA 15.4 -> 15.3, span 18.9 -> 18.8, limiter 2.4 -> 2.4 dB.

## Deviations from the coordinator's notes, with the measurement
- Violoncellos 140 / 240 fills: pre_s 0.10 / 0.12 instead of A's 0.18 / 0.26. With A's values the fill reached full level
  while the old note was still sounding (the Hollywood Strings transition keeps the old pitch about 0.1 s past the moved
  onset): the old note's tail rose +6.9 / +5.9 dB on the stem and +3.5 / +4.4 dB on the master just before the beat (50 ms
  peak over the previous body; c46 -0.6 / -1.1 and +0.4 / +1.4). With the shorter pre_s the pre-onset peaks are +1.4 / -1.1
  (stem) and 0.0 / +1.4 (master) and the holes are filled the same (140: A hole 6.4 both; 240: master 1.1 both).
- Clarinet 1 283: C's change deletes the c38 CC7 dip. Simulated, deleting it lifted the 280 note's last 0.3 s by 3.5 dB
  (A-weighted quarter beats 282.5-283.75: -48.3 / -44.9 / -49.3 / -53.2 with C's fill raise, against -48.3 / -48.5 / -54.7
  / -52.2 in c46): the dip still cuts that note's end swell. Ending the dip at 283.0 instead of 283.3 gave -48.3 / -48.5 /
  -51.2 / -51.5 with no overshoot; auto_fills' raise of the 283 fill (3 -> 6 dB) then overshot (+2.3 dB) and was not kept.
- Horn theme 23 / 35 / 37.5: auto_fills proposed nothing there. 23 and 35 are level steps into the printed decrescendos
  (A's lower-body hole 0.5 / 1.1 dB; C's measure reads the step as a dip); 37.5 has a 5.0 dB hole under its existing fill
  that auto_fills does not flag. No change.
- Oboe 1 142 / 142.5 (kept as given): A's shorter holds (0.08 / 0.15 s against 0.35 / 0.28) leave the two eighths' bodies
  2.5-3 dB lower than in c46 (quarter beats 142.25 / 142.75 -40.6 / -40.5 -> -43.6 / -42.3; master -39.2 / -39.0 -> -41.1 /
  -40.2), as A's own simulation showed for 142's master dip (1.7 -> 3.0). Open.

## Rejected / left
- The string lifts (CAESURA_LIFT), Violas 249.5 and the basses' f trim (coordinator; B's bar 59 check did not ask for a
  change).
- MANUAL-GAPS: none tried (the last cycle allows no Opus state change).
