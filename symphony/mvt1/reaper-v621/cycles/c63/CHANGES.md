# Cycle 63 (Movement I): CHANGES

Narrow fix cycle, no critics (coordinator notes; Dan: "yeah do c62 that fixes that why not"). Goal: c61's levels
everywhere, minus the fast fader moves inside sounding notes. Scripts: cycles/c63/actor_scripts/. Snapshot: before/.

## Why c62 moved phrase levels
`ENV_NO_GUARD=1` on the c62 build against c61 (gate63.py): 0 spans over 1.5 dB outside the notes of removed c61 edges
(15 inside: POST_SHAPES_S removal and the percussion CC7 fold). So every phrase shift came from c62's note_slope_guard:
held moves were held at their start level and returned at 2.4 dB/s or "in the next rest" (seconds later, across
notes); join steps were spread up to 2 s back, three times per note-on; merged runs were rewritten with their slow
stretches; hairpin ramps were slowed to 2.85 dB/s and started before the hairpin.

## What changed
1. `tools/build_reaper.py`: new guard mode `_nsg_relocate` (mix.json `note_slope_guard` `"mode": "relocate"`; the c62
   function stays as the default mode). Each fast move (runs over 2.6 dB/s moving 1.2 dB or more inside sounding notes)
   is taken out of the written course as a unit (its steep samples only) and the same size is added back at its new
   place, so nothing outside the move's own note changes. A move is split at the track's rests (gaps of 10 ms or more);
   parts in a rest stay. Placement:
   - printed sudden dynamic at a new note (sf, sfz, fp, sfp, sub. p/pp, subito_falls, and c62's mark_steps): a step of at
     most 60 ms ending 0.03 s before the moved note-on (c62's 20 dB/s made a 0.44 s ramp that lifted the celli's ff
     stroke before the pp at 286 by 8.8 dB);
   - printed hairpin move: a ramp inside the printed hairpin and inside the note it lies in (hairpin start or the
     note-on before, to its note-on or the hairpin end), however steep; at a note-on after a rest, in that rest;
   - any other move: whichever option moves the least level (dB x s off the written course, level outside the move's
     own note weighted x6): the rest before or after its note (no note-on crossed; a move at a joined note-on may go
     to the rest before the note it joins), placed in the last 0.35 s before the next note-on; a ramp across its note;
     the move slowed about its centre; for moves 0.4 s or longer, slowed inside the sounding segment, or split between
     a slow ramp and the rest. A ramp counts only if the written course with it stays under 2.9 dB/s inside sounding
     notes (0.25 s windows). Otherwise the least steep in-note ramp (listed).
   **Departures from the work order:** item 3's "nearest rest" became "least level moved" among rests and slow in-note
   ramps (a slow ramp moves less level than a rest 2 s away); item 4's "ramp over the hairpin's printed length" is
   limited to the note the move lies in (spreading a c61 arrival step over a 24 qn hairpin moved 8 tracks by 2-3 dB
   over bars 112-116, which the gate forbids).
2. `build/mix.json` `note_slope_guard`: mode relocate, max_db_s 2.9, detect 2.6, min_db 1.2, rest_min_s 0.01,
   sudden_max_s 0.06, out_weight 6, mix_ramp_rest, passes 1 (removed c62's join_max_s, hairpin_db_s).
3. Unchanged from c62: score_config (POST_SHAPES_S off, VOL_TO_CC7 for timpani / crash / tam-tam), parts.json
   (identical to c62's rendered one), delivery settings (TOP_ABOVE -6, TOP_RATIO 1.5, lift 3:1 cap 15, bar-122 ride -2,
   room bed -60).

## Net-level gate (before the render)
gate63.py: net level = fader dB + CC7 dB, mean per 1-qn span where the track sounds, c63 minus c61, 8944 spans.
- Exception (a) from the moves the guard took out of c61's course (`--guard`): **0 spans over 1.5 dB outside those
  notes** (NET-LEVEL-GATE-c61.md). Inside them: 200 spans over 1.5 dB, 65 over 3, 6 over 6 (largest: Horn 1 / Horn 2
  bar 166 +9.3 / +9.1, Horn 2 bar 68 -8.3, celli bar 83 +8.3).
- Strict exception (only notes holding an env61 edges() edge of c61, 3 dB/s and 1.5 dB): 25 spans fail, all inside
  notes whose c61 move was between 2.6 and 3 dB/s or under 1.5 dB inside (net_level_gate_c61_strict.md).
- c62 -> c63 (net_level_gate_c62.md): 111 spans over 1.5 dB outside the exception (c62's phrase shifts undone).
- Percussion (CC7) passes in both.

## Edges (edges63.py, env61 edges(), no skipped windows; edges_c63.md)
c61 354 (held 75, new 182, hairpin 97) -> c62 30 -> c63 71: **inside held notes 0**; printed hairpin 36 (median 830 ms;
item 4 asks for these however steep); printed sudden / printed step 26; other at new notes 9 (steep in-note ramps
where no slow placement fits: Flute 1 139, Horn 2 165, Harp 59, Violins I 163, Violins II 121 (-15.9 dB in the 20 ms gap
before the bar-122 chord), Violas 155, celli 68 and 138, basses 2). Notes with 1.5 dB+ fader change in their first
0.35 s: 29 (c62 8, c61 174).

## Render (cycles/c63/mvt1-mockup-c63.mp3; one main render + pass 2, lock 13:04-14:34)
- Master -20.9 LUFS, LRA 22.2, TP -2.0. Attack probe: 0 late or hole (main and pass 2). REAPER 42 GB before the main
  render, 44 GB (27 GB compressed) after. Disk dropped to 15 GB free during the build (other threads), 28 GB after the turn. Lock 13:04-14:34 (main stale Trumpet 2 and pass-2 stale Bassoon 1 stac, Flute 1 stac rebuilt after the renders and saved).
- Master bars more than 1.5 dB off c61: one, bar 62 +4.5 dB (Violins I / II f62 tails into the sub. p, as c62: exception
  (b), left audible). Median +0.01 dB. (c62 had the same bar only, but its stems moved whole phrases.)
- Inner lines (B63/measure_lines.py, inner_line_table.md): **0 of 67 lines more than 1.0 dB from c61** (c62: six 1.5-2.6
  dB lower).
- Theme guards: Violins I 56-90 S robust SD 9 ms (limit 12); theme over celli lower quartile +3.99 (limit 3.9).
- Delivery (deliv63.py; settings unchanged from c62): I -14.1 LUFS, LRA 13.2, TP -1.2 dBTP, short-term p10 -22.8,
  limiter 6.4 dB on the loudest sample peak (bars 89-90); summit lead 160 over 122 / 26 / 170: 1.3 / 1.1 / 1.83 LU;
  f -> ff passage medians +1.16 LU (spec 2: **not met**, as c61 0.95 / c62 1.18).
- Exposed solos (coordinator relay, scherzo critics; solo63.py, loudest 0.4 s on the mp3): cor anglais bar 7 -12.8 LUFS
  against f bars 12-13 -9.3 (3.5 LU under); cello solo 171-174 -12.0 against f bars 167-168 -9.8 (2.2 LU under). c61:
  -11.5 / -9.1 and -10.7 / -9.9.
- A/B clips (c61 then c63, masters, one gain for both): ab/bars110-124_master_c61_then_c63.mp3,
  ab/bars160-168_master_c61_then_c63.mp3 (RMS equal to 0.1 dB in both).
- state_check: celli qn 504-507 moved on unchanged MIDI (+3.5 dB against c62, the envelope change; pcX +30 ms, a render
  flip not traced).

## Coordinator relay (scherzo c30 critics)
1. Role edges after a moved note-on: non-printed steps at a note-on go to the rest before it when that moves the least
   level; 29 notes still have 1.5 dB+ of fader change in their first 0.35 s (edges_c63.md lists them; c62 8).
2. No 0.04 s rest needed: the guard counts gaps of 10 ms as rests, so no notes were shortened.
3. One-note volume roles: 39 roles.json rows of 1 dB or more cover a single note onset (Timpani 300 / 692, the a2 brass
   rows 567.75-572.5, the 672-676 -2.5 rows, Cl1 575.75-582 -5, Double basses 336-358 +3, Violins I 720-729 -2.5, ...).
   Kept: their edges lie in rests, and removing any of them moves its note by 2-8 dB (gate fails).
4. Solos: above.

## Left audible / not done / not verified
- Left audible: bar 62 f62 tails (+4.5 dB master); 9 steep in-note ramps at new notes (list above); 36 printed hairpin
  ramps steeper than 3 dB/s (by item 4); in-note level changes where a move went to a rest (6 spans over 6 dB: Horn 1
  / 2 bar 166 +9, Horn 2 bar 68 -8, celli bar 83 +8, Horn 3 bar 112 -7, Trombone 1 bar 114 -7): mostly the U-shaped soft
  trims (a 10 dB step up into an entry inside a crescendo, then a 3 dB/s fall); timpani / crash / tam-tam CC7 shapes as
  c62 (pass the gate).
- Not done: source fix for the U-shaped soft trims; f -> ff step; the sf at bar 41 without its bumps (c62).
- Not verified: nothing listened to; the 30 ms celli timing flip at 504; the strict gate (25 spans) relies on the guard's
  own move list for its exception.
