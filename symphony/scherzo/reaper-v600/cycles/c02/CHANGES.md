# Cycle 02 (actor), on the c01 render and the critics' reports A, B, C

Render: `cycles/c02/scherzo-mockup-c02.mp3` (one render, 12 tracks fully rebuilt, the rest MIDI/envelope only; one stem fix on Violins I afterwards). Snapshot before the cycle: `cycles/c02/before/`; the data the render was made from: `cycles/c02/build_render/`. Scripts: `cycles/c02/actor_scripts/` (`rowcost.py` sample regions per loaded row, `loaded.py` rows loaded in the generated Opus states, `rownotes.py` / `notes_at.py` notes per row, `sim.py` envelope simulation on the c01 stems, `post.py` before/after checks; output in `cycles/c02/post_c01_c02.txt`).

Hall (BRIEF S4, mockup-kit README item 7, mockup-kit LEARNINGS "Too wet and mushy"): no newer shared values since c01. Item 7 still reads fx_volume 0.095, low cut 160 Hz, high cut 5.5 kHz; the IR-envelope shortening is "values to follow" (Movement I's mix.json is still at 0.19 in its c44). Nothing changed.

## ONE_TIME: memory back under the cap (BRIEF item 7)

- Checked first: `UNLOAD_UNUSED_ROWS` still unloads every row a track does not play. In every generated state (`jobs/NN_*.b64`) the loaded rows equal the track's `art_counts` plus `first_art`. The only exceptions are the single-row harp patches and a case difference ("Sus Max") on the cor anglais.
- Cost measure: sample regions per row read from each `.oib` (`rowcost.py`). c01's 13 new rows were about 92 thousand regions for +4 GB (45 -> 49 GB settled). The legato rows are the expensive ones (10-27 thousand regions each); "StacSl Leg BC + Slur + Port MAX" is 54 thousand.
- New generic option `ROW_REMAP` (`tools/score_to_parts.py`, default `{}`): `{track: {row: row}}` moves every note the rules put on a row to a row the track already loads. A legato row remapped to a Sus row plays tongued Sus notes. "Leg BC MAX" -> "Leg Slur MAX" keeps the join as a slur transition with `VLA_BC_SOFT`'s 4 CC bow-change notch (the BC_SOFT path). parts.json gets a `row_remapped` list per track.
- Changes per track (`build/score_config.py`, c02 block):

  | track | dropped row | notes moved | thousand regions |
  |---|---|---|---|
  | Trombone 1, Trombone 2, Bass trombone, Tuba | Leg Slur MAX -> Sus MAX | 2 each (slur heads at 300 and 996, nothing joined to them) | 10.5-10.7 each, 42.6 total |
  | Oboe 2 | Leg Slur MAX -> Sus MAX; Stac DblTng -> Sus slices | 3 heads (300, 900, 1005); 16 staccatos | 11.9 + 4.4 |
  | Bass clarinet | Leg Slur -> Sus Non Vib | 11 (2 joins lost: 237, 264, pp inner voice) | 14.0 |
  | Bassoon 1, Clarinet 1 | Stac DblTng -> Sus slices | 20, 35 (tutti, doubled) | 4.8 + 5.6 |
  | Violas | Leg BC MAX -> Leg Slur MAX + notch | 17 | 20.7 |
  | Violins II | Leg BC MAX -> Leg Slur MAX + notch; Stac Slur RRx6 -> Spiccato RRx9 | 25; 76 | 27.2; +2.8 |
  | Violas div | Leg BC MAX -> Leg Slur MAX + notch | 2 | 4.1 |
  | Violins I | + Sus Marc LITE (finding A #1) | 9 | +8.5 |

  Total loaded regions: 700.7 thousand (c01) -> 576.5 thousand (c00 had about 609).
- Kept on purpose: Leg Port MAX on Violins I (1 note, 22.4 thousand regions; the printed "port." glides, critic A); Violins I and celli Leg BC MAX; the contrabassoon's slurred line.
- **Settled memory: 45 GB with 25 GB compressed** after the restart (c01: 49 GB with 16 compressed, 50 / 32 after its render). The footprint is 4-5 GB lower, at the cap but not clearly under it. After the render: 45 GB (22 compressed); after the save: 46 GB (27 compressed). The render passed the attack probe with `--force-memory` (the gate refuses at more than 6 GB compressed).

## Accepted and made

- **A #1 theme-head accents (p / mp)**. The manual's Legato Slur Staccato row was rejected for memory (54 thousand regions). Instead, Movement I c23's "Sus Marc LITE" row plays the nine p/mp Violins I heads (39, 51, 69, 75, 285, 759, 771, 789, 795) via `ART_SPANS` with `vel_by_cc` (34,70) (46,78) (58,86) (72,94). `STR_STROKE_ROWS` keeps the stroke lead. The f heads and 819 stay Sus MAX strokes as the control.
  - Rendered: accent minus the staccato before it went from -14.1..-8.5 dB to **+4.4..+14.6 dB**. That overshoots, and theme A's master rose 5.5 dB.
  - Stem fix: exact `LEVEL_SHAPES` steps per head (-2.4..-12 dB, from the moved onset to just before the slurred eighths). Result: **+2.0..+2.6 dB** (target -3..+4). Theme A master -39.1 (c01) -> -37.3 dB.
  - 2-5 kHz first 80 ms minus body: **+2.3..+7.1 dB** (c01 -10.6..-13.3). A level step does not change this. **Open**: the row's front is brighter than the body; check by ear and trim the first 0.1 s if it bites.
- **A #2 hemiola strokes**: `DOWNBOW_STROKE_AT` 300-310 / 902-910 for Violins II, Violas and celli, and 902-910 for Violins I. The celli's 11.6 qn merged note is now six strokes.
  - Weight (first 150 ms minus the 50-250 ms before), master: 302/304/306/308/310 went from +1.9/-1.0/+0.5/+3.0/+0.9 to **+2.9/+2.0/+2.6/+3.2/-0.9 dB**; 902-910 from -0.8/-0.7/-0.5/+2.9/-0.3 to -0.6/0.0/+2.5/+1.8/+0.5.
  - Violins II: +2.1..+5.6 on 7 of 10 (c01 4 negative). Violas: 7 of 10 positive. Celli: mixed (906/910 -3.8/-4.0).
- **A #3 wind stac velocities** (Oboe 1 -12, cor anglais +10 on every entry): **no measurable effect**. Oboe 1 accent minus staccato went from -8.7..-11.1 to -6.8..-10.6; cor anglais from +1.4/+8.3 to +1.1/+8.0. **Open**: shape it in level (row trim or note trims), not velocity.
- **A #4 Violins II tutti on Spiccato RRx9** (trim -3 dB): the stem's pair dips did not improve (c01 0.0-5.9, c02 1.3-6.2). The master pair dips at 313-355 / 913-955 went from 0.6-4.6 to 0.6-3.9, a little worse at 319/331/919. **Open**: try "Stac RRx9" at -3 dB in the tutti, or a shorter note length.
- **A #6**: `MERGE_NOTCH_AT` 18 CC on the violas' portato pairs 629-671 (Violas, Violas div). Not measured.
- **B #1 harp** `soft_trim_db` pp 7 -> 2. Trio harp minus Clarinet 1 went from +0.4..+3.9 to **-1.1..-5.3 dB** in the bars where both play; 185-188 harp minus Oboe 1 from +5.6 to +0.6..+0.8.
- **C #5**: new generic `VEL_CAP_SPANS`; Harp capped at v78 over 216-240. Master in bars 73-88 went from -30.7 to -33.2 dB (the theme is -33.6 here and -37.3 after the stem fix).
- **C #1 horns**: `soft_trim_db` -> Movement II's soft-map values (ppp 4, pp 4, p 4.5, mp 2.8, own mf). The c01 drone/pedal/sub. p roles were removed (Horn 2 360-381, Horn 3 456-504 and 708-720, Horn 4 360-381, 456-504, 684-720).
  - Solo roles: Horn 1 0-18 +4, 420-444 +3, 1068-1080 +3, 1089-1128 +10; Horn 3 1020-1032 +3, 501-528 +2. B #4: Violins I 1116-1128 -2.5.
  - Simulated on the c01 stems first (`sim.py`).
  - Rendered: Horn 1 minus Violins I at 1116/1119/1122 went from -1.3/-3.4/-4.0 to **+2.0/-0.4/-1.3 dB**. Horn 3 under the celli's trio tune went from -0.7..+0.9 to -4.9..-8.2 dB (a little more than B's 2-4 dB target). Hn 3-4 under Clarinet 1 at 81-88.
  - This also covers C #6: the sub. p horn roles are gone, so no envelope ramp falls under the ff ring at 360.
- **C #2 + B #2 summit**:
  - `ARRIVAL_WEIGHT_AT {1005: (-2, 2.5, 1.0)}`; `VEL_SET` 1005 v112 on the four string sections; Violins I 1004 v105.
  - Every summit role now starts at 996. Violins I 1004.75-1008 +3 and 1008-1014 +2; cor anglais 1008-1010 -4; Bassoon 1 1005-1017 -3 more.
  - Master first 0.15 s of 1005 minus 1004: **-3.3 -> +1.0 dB**. Bars 333/334/335/336/337: -15.7/-15.1/-14.2/-13.8/-12.1 -> **-18.1/-17.9/-16.2/-13.1/-12.3**.
  - Bar 337 over bar 304: 1.2 -> 2.1 dB.
  - Violins I 1005-1014 -24.3 -> -21.9 (Violins II -20.8); cor anglais / Bassoon 1 -25.5 / -25.0 -> -28.3 / -28.1.
- **B #3 timpani**: `TIMP_LOUD_ATTACK_DB` applied once per onset (generic). The 1014 double stop went from +12 to +6 dB. Timpani at 1014 -15.4 -> **-21.0** against Violins I -23.5.
- **C #3 sfp chain** (generic fix in the `HP_CHAIN` test: a softer mark at the second hairpin's start ends the chain):
  - Master 901-903 went from -22.6 to **-26.2 dB**. Bassoon 2 / Horn 2 / Horn 1 there went from -30.6/-31.1/-32.7 to -37.4/-38.0/-38.6.
  - The crescendo into bar 304 grew from 6.9 to 8.8 dB.
- **C #4 timpani rolls**: new generic `TIMP_ROLL_TRIM_HOLD_CRESC` (share of the trim's fall held under a printed crescendo; default 0, scherzo 0.6) with `TIMP_ROLL_TRIM_HOLD_SKIP` [618].
  - Bar 101-103 roll per 1.5 qn went from -34.4..-39.5 (flat) to **-33.5 -> -28.1** (+5.4 dB growth), 7 dB under the celli.
  - `LEVEL_SHAPES`: codetta pp roll +4 (708-718: -57.9 -> -53.9 dB); 621-624 -3 (-34.1 -> -37.0, now 2.3 dB over Horn 1 instead of 2.4).
- **B #5 counterstatement roles** (Clarinet 1 -4/-9/-4, Clarinet 2 and Bassoons -4 over 84-108): Clarinet 1's A4 at bars 33-34 went from -39.7 to -48.6 dB. Master pair dips at 85/97 went from 0.9/1.7 to 1.3/2.5 dB (target 3).
- **B #6 celli pizz.**: pitch trims G2 / F sharp 2 / D sharp 2 -6, G sharp 2 -4, B2 -3; role 36-84 -2. Not measured separately.

## Rejected or deferred

- A #1's Legato Slur Staccato row and A #5's Slur Runs: 54 and 15-21 thousand regions per track, over the memory cap. Deferred until memory allows.
- B #4's horn cuts (Horn 3 -4 ×2, Horn 2 -5): superseded by C #1's trim change, which lowered them 6-9 dB.
- Timpani staccatos on the Sht row (B #3 articulation): deferred (one more row; the envelope fix met the target).

## Measured summary

- Master (after the stem fix): -19.3 LUFS integrated, LRA 23.8 LU, true peak +0.4 dBFS. The float master peak 1.051 is at the summit (sample-peak clip; the master was replaced by the float stem sum).
- Delivered mp3: **-19.9 LUFS, LRA 15.0 LU** (c01 13.6; target 14-16), **TP -1.6 dBTP, limiter 3.2 dB**. The p10-to-max span is 20.2 dB (target 16-19; c01 19.0).
- Attack probe: all attacks ok. The only failures are the pre-existing string legato spread: Violins I SD 88 ms, Violins II 90 ms (c01 89 / 93; limit 75).
- Every stem present and sounding.
- REAPER memory: settled 45 GB / 25 compressed before the render; 45 / 22 after the render; 46 / 27 after the save.
- Lock held 10:50:51-11:18:16 (27.4 min), after a 50 min wait behind Movement II. The build with 12 full rebuilds took 60 s; the render with measurement about 7 min.
