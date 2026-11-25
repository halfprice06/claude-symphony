# Cycle 62 (Movement I): CHANGES

Narrow cycle on Dan's rule (no per-note level or shape on the track volume envelope), no critics. Render:
cycles/c62/mvt1-mockup-c62.mp3 (second REAPER turn, lock 23:01-00:18; mp3 re-delivered on the
same master after the bar-122 ride row went -1 -> -2). rendered_build/ = the build as rendered (parts.json differs from the
rendered one only in ride_trims). The first turn's render (19:53-21:16) carried a faulty guard and is in first/ (mp3,
metrics, logs) only. Scripts: cycles/c62/actor_scripts/. Edge tables: edges_c61.md (tagged), edges_c62.md; envelope_table.md;
inner_line_table.md; A/B clips ab/ (c61 then c62, masters, bars 12-16 and 85-91).

## What changed, in the coordinator's order
1. **Tagging** (`tag62.py`, `edges_c61.md`): the 354 c61 edges by rule: dynamic trims at printed marks 94, role-row edges
   64, phrase / level-shape rows 64, hairpin gain 31, POST_SHAPES_S per-note shapes 25, timpani levels 25, divisi chord
   cuts 18, percussion ring shapes 18, final fade 8, others 7. (Held / new split with my window: 102 / 252; the
   coordinator's 137 / 217 used another window.)
2. **Source fixes and the guard.**
   - `build/score_config.py` c62 block: `POST_SHAPES_S = {}` and the f62 aliases' POST tables removed (bar-41 sf bumps on
     13 tracks, Violins I 78, the f62 hall-cut shapes at 244).
   - `tools/score_to_parts.py` `VOL_TO_CC7` (generic, the finale's vol_to_cc7): Timpani (shift 12 dB; 4 peak points
     clipped), Crash cymbals and Tam-tam ("auto", 12 / 9 dB) have their vol_db in CC7; the shift goes to the track gain
     (`vol_shift_db`, added in build_reaper). Their strokes' dynamics and ring shapes are now CC7 shapes inside notes:
     in the instrument, but still per-note shapes (crash ring fade-in, tam-tam ring hold): flagged for Dan.
   - `tools/build_reaper.py` `note_slope_guard` (generic; mix.json `note_slope_guard`): written from scratch rather than
     ported (the scherzo guard skips printed zones; the coordinator's c24 note says not to). Acts everywhere; no window is
     skipped. Printed sudden dynamics: 20 dB/s ramp ending 0.03 s before the moved note-on. Other steps at a new note: in
     the rest before it, or the step added as a 2.4 dB/s ramp ending at the moved note-on (at most 2 s, three times per
     note-on). Held notes: hairpin moves ramp from the hairpin's start, others are held and return at 2.4 dB/s or in the
     next rest. Runs longer than 0.4 s are ramps (from the hairpin start when one covers them).
   - **Departure:** `mark_steps`: a printed dynamic that changes the level on a note with no hairpin arriving there (ff ...
     pp, p ... f) counts as sudden. Without it the 2.4 dB/s ramps carried the pp trim 4 s back into the ff: celli marcato
     strokes at 284-286 +9 dB, and a divisi chord +13 dB through its decrescendo before 504.
   - Not done: hairpin-gain release, held-decrescendo and role-edge fixes at the source (the guard does them); the
     finale's c26 rest-release options (the guard already gives 0 inside held notes).
3. **Result** (edges62.py, the env61 measure unchanged, on rendered_build): 354 -> 30. Inside held notes 102 -> 0. At new
   notes 30: printed sudden marks 9 (sf 160, sub. p 244 and 332), printed dynamic steps 20, one other (Violas 574.3, 3.2
   dB/s). Brass 6, strings 19, winds 4, harp 1; 6 dB+ 4. Notes with 1.5 dB+ envelope movement in their first 0.35 s:
   164 -> 8 of 5124. Envelope points 3449 -> 2692; notes with 3 / 6 dB inside 279 / 62 -> 142 / 14.
   Master bars more than 1.5 dB off c61: one, bar 62 +4.4 dB (Violins I / II f62 +8 / +12: their forte's hall tail rings
   into the sub. p now that the POST_SHAPES cuts are gone). Median +0.02 dB.
4. **Delivery** (`tools/deliver_master.py`): TOP_ABOVE -10 -> -6, TOP_RATIO 2.0 -> 1.5, quiet lift 3.0:1 kept with its cap
   10 -> 15 dB (2.1:1 gave p10 -24.0 on the c61 master; the lift sat at its cap); RIDE_TRIMS bar 122 -2 dB. Grid of 13
   deliveries on the c61 and c62 masters in the scratch folder.
5. **Guards:** Violins I theme 56-90 S robust SD 9 ms (c61 9). Theme over celli lower quartile +3.93 (c61 +3.96). Inner
   lines (67, B's measure): median -0.1 dB, **six lower by more than 1 dB: 37-39 Vla -2.6, 56-63 Cl1+Hn2 counter -1.8,
   56-61 harp -1.5, 60-61 Vla -1.8, 107-110 Vln II -2.3, 162-166 Vln II -1.8: guard failed, cause not traced** (probably
   role-row edges the guard moved or ramped).
7. **Room bed** (`tools/deliver_master.py` `room_bed`, env `DELIVER_ROOM_BED_LUFS`, default -60, "off"): as specified,
   after the limiter, before the encode, seeds 6201-6203. With the bed: I -14.1, LRA 13.3, TP -1.1; without: I -14.1, LRA
   13.3, TP -1.2 (the integrated figure does not move at ffmpeg's 0.1 resolution).

## Measured (c62 against c61)
- Delivered (bed on): I -14.1 LUFS, LRA 13.3 (c61 11.9), TP -1.1 dBTP, short-term p10 -22.9 (c61 -22.2), limiter 5.7 dB on
  the loudest sample peak, no bar with 6 dB+ over 0.5 s. Loudest 0.4 s: 160 -6.9 > 122 -7.5 > 26 -7.6 > 170 -8.3; summit
  lead 0.61 / 0.70 / 1.34 LU (c61 0.25 / 0.50 / 1.03). f -> ff passage medians +1.18 LU (c61 +0.95; spec 2): **not met**
  (master +3.3; every ride setting tried gave 1.0-1.7).
- Master -21.0 LUFS, LRA 22.5, TP -1.9. Attack probe: 0 late or hole (main and pass 2). Memory 42 GB before the main
  render, 44 GB after, 0 compressed. Disk 47 GB free after the turn.
- Phrase entries (coordinator's note): 474 entries, 81 more than 6 dB under the next note; lyric 19 of 106 (c61 20),
  build 46 of 189 (expected), drive 11 of 83, flat 5 of 96. PHRASE_SHAPE start (winds -8 x 1.4) not changed.
- Against printed hairpins (U-shaped trims): notes moving 3 dB+ against their hairpin 67 -> 37 (worst Horns 1-3 at 40,
  a crescendo, -8 dB; Clarinet 1 242 -6.9).

## Left audible / not done / not verified
- Left audible: bar 62 f62 tails into the sub. p (+4.4 dB master); the sf at bar 41 without its bumps (brass front weaker,
  not measured); timpani, crash and tam-tam shapes now in CC7 (not compared by ear; CC7 response on the cymbal patches not
  verified beyond the stems sounding).
- Coordinator's correction after the render: a hairpin's move should ramp over its printed length however steep; the
  guard limits hairpin ramps to 2.85 dB/s, so 45 of 277 hairpin ramps start before the printed hairpin (median 0.37 s,
  max 2.1 s). One-line change for c63: `hairpin_db_s` very large, and count those edges as "printed hairpin".
- Not done: the six inner lines; f -> ff step; PHRASE_SHAPE start; source fixes for the U-shaped trims.
- Not verified: nothing was listened to; the guard's ramps at joins (up to 2 s before a note) by ear.
