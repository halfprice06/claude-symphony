# Critic B, cycle 56 (render of cycle 55): balance and levels with no per-note volume moves

Data used: the delivered stems `cycles/c55/render/` (01-32 dry, after the stem fix) with `cycles/c55/build_fix/parts.json`
(byte-identical to `build/parts.json`), `build_fix/mix.json`, `roles.json`, `cell_rows_c55.json`; c54 for comparison from
`cycles/c54/render/` and `cycles/c55/acc_c54.json`. `tools/build_reaper.py` was read only up to `ENV_LUA` (through
`cycles/c53/actor_scripts/lib53.py`). Patch files were read (not loaded) to list region key spans.
Scratch folder, left in place (0.5 MB, no audio): `/private/tmp/claude-501/mockup-loop/mvt2-c56-B/`
(`notes.py` per-onset table, `reg.py` / `lines.py` / `sim.py` line fits, `steps.py` envelope steps, `bars.py`, `spans.py`,
`proposal.json` with the tables below in `mix.json` form). No REAPER, no bridge job, nothing written outside this report
and the scratch folder. Nothing below proposes a per-note track volume move; where a volume row is named it covers
three notes or more, a section, or a fade.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 56, so no scheduled page reading. Pages used for the fixes:

| reading (2021 HO manual, PDF page) | where it applies | does the render follow it |
|---|---|---|
| p.137: each row of a KS Master has its own volume knob ("adjust the loudness of each articulation") | Flute 1 "LegRep RRx4" (one note, qn 136), row-level differences in general | No. `tools/build_reaper.py load_articulations()` never sets `layerMatrix.rows[].volume`; the level of a row was held by fader rows that are now off |
| p.53, p.150-151: velocity sets level and layer on short rows and cannot change mid-note; CC11 / CC1 shape longs; CC7 is the track ceiling | violas' pizzicato bars 41-44 (CC11 35-45 and velocity 42-67 both attenuate), Oboe 1 phrase heads at velocity 53 | Partly. Short rows still take a low CC11 as well as a low velocity (FINDINGS section 7: the EastWest template parks the lane high on shorts) |
| `MANUAL-GAPS.md` c37 entry: Flute 1 "LegRep RRx4" body 8-11 dB over "Leg Slur MAX"; "a level shape cuts it" | qn 136 | The level shape is a per-note move and is off in c55; the row is 13 dB over the note before it (finding 2) |

Reference practice (FINDINGS.md of `origin/claude/project-thread-cn1rc0`): no example project corrects a note's level on
the track fader. Sections 51-52 and 91: dynamics are one dense CC lane, flat across legato note changes; section 244:
longs keep one velocity, the lanes carry the dynamics; sections 84-86: shorts take their dynamic from velocity with the
lane parked at 118-127. The stock EastWest patches themselves carry per-region volumes (read from the `.oib` files:
Oboe "Leg Slur MAX" 85 regions at 0.50-0.63, Bass clarinet "Sus Non Vib" 0.50-1.41, Celli "Sus MAX" 890 regions at 1.47,
Basses "Pizz RRx4" 1,420 regions at 1.37-1.82), so a region volume is the library's own way of evening samples.

## Method (measured unless marked)

Per onset: stem level over 20-80 % of the note from the score onset ("heard"), the written envelope at that time, their
difference ("instrument level"), row, velocity, mean CC11 and CC1. Per track a least-squares fit of the instrument level
on row + CC11 (quadratic) + pitch (ridge 0.6) over all single notes of 0.3 s or more. A note's deviation in its line is
its instrument level minus the row + CC11 part of the fit, centred on the line's median; the pitch term says how much of
it recurs on that pitch everywhere in the movement. Limits: pitch terms with one or two notes are weak; some offsets
exist only in one dynamic layer (named where seen); legato transitions and the previous note's tail are inside the
window.

Summary over 24 main lines (364 notes): 171 notes are 2 dB or more out of their line, 101 are 3 dB or more.
The strings' lines are no worse than c54 (Violins I theme 22-30 sd 2.6 dB against 2.7 in c54; Violins II 2.2 / 2.7;
53-60 2.1 / 2.3; A' 1.2 / 1.7). The cost of c55 is on the wind solos, the celli of bars 71-78 and the basses:

| line | sd c54 -> c55 (dB) | out by 2 dB+ / 3 dB+ (c55) | after the pitch term |
|---|---|---|---|
| Horn 1 theme 7-14 | 1.5 -> 3.0 | 14 / 8 of 22 | 1.6 |
| Oboe 1 15-22 | 2.7 -> 4.2 | 6 / 5 of 11 | 2.8 |
| Violin I solo 17-22 | 1.3 -> 2.2 | 3 / 1 of 11 | 0.8 |
| Bass clarinet 31-36 | 1.9 -> 2.7 | 4 / 3 of 12 | 1.1 |
| Flute 1 theme B 37-44 | 2.6 -> 3.1 | 20 / 11 of 30 | 2.1 |
| Cor anglais 41-44 / 47-50 | 1.6 -> 3.0 / 1.9 -> 2.5 | 8 / 4 of 14; 3 / 2 of 6 | 1.5 / 0.9 |
| Violoncellos 71-78 | 1.8 -> 3.5 | 10 / 6 of 18 | 2.4 |
| Bassoon 1 71-78 | 1.8 -> 4.0 | 7 / 5 of 9 | 1.8 |
| Double basses 23-30 (same in c54) | 4.4 | 11 / 8 of 14 | 2.1 |

## Findings, ranked by audibility

### 1. Per-pitch sample levels on the solo winds, Horn 1, the celli and the basses: move the old pitch trims into Opus as region volumes

Where: Horn 1 bars 7-14 and 65-70; Flute 1 bars 37-44 and 79-82; Cor anglais bars 41-44 and 47-52; Bass clarinet bars
31-36; Bassoon 1 and Violoncellos bars 71-78; Double basses bars 23-30, 30, 71-75; the pickup into bar 53.

What (measured, c55 stems):
- Horn 1, bar 12: B flat 4 -35.1, A flat 4 -42.5, G 4 -41.7, E flat 4 -36.6 dB heard, with CC11 only 57.6 -> 52.9. The
  top of the theme falls 7 dB for two notes. Over the movement at CC11 40-60: A flat 3 -4.6 dB (5 notes), F 3 -3.6 (2),
  D 4 +8.5 (2: bars 8 and 68), E flat 4 +4.3 (3; -2.9 above CC11 85, so only the soft layers), F sharp 4 -2.9, A flat 4
  -3.8 / -7.2. The signs agree with the c06-c54 `pitch_trims.json` entries (56 +3, 62 -3, 66 +4, 68 +5).
- Double basses on "Sus MAX": bars 23-26 at CC11 45-50 read A flat 2 -40.7, F 2 -43.7, B flat 2 -47.0, E flat 3 -50.1,
  A flat 2 -39.7, D flat 3 -49.0, E flat 3 -51.3: 10 dB between neighbouring notes of one line (unchanged from c54, never
  corrected). A flat 1 is +2.4 dB over the track at CC11 under 40 (19 notes), +4.8 / +6.8 above. With its c54 trim off
  it is 6.9-7.8 dB louder than in c54 at qn 87, 238, 244, 250 and is the loudest stem of bars 30, 71 and 73.
- Master bars (c54 -> c55): 30 +3.2 (basses A flat 1 +6.9), 35 +3.9 (Bass clarinet A flat 2 held 4.9 s, +3.8; A flat 2 is
  +2.6 to +7.3 over the track on 12 notes), 48 +3.0 (Cor anglais A 4, 3.8 s, +4.9; pitch +4), 71 +3.2 and 73 +2.7
  (basses A flat 1 +7.8; celli E flat 3 +6.9 and A flat 3 +6.6), 11 +3.0 / 12 -1.7 (Horn 1).
- Violins I and II: C 5 is +3.2 / +3.5 dB (16 and 8 notes) and F 4 -3.1 / -2.9 (3 and 9). The C 5 pickup at qn 171 stands
  2.8 dB (Violins I) and 4.2 dB (Violins II) over the bar 53 downbeat it leads to.

Fix (instrument side; the scherzo c15-c16 and finale c17 tool, not yet in this folder):
1. Port `region_gain()` from `symphony/scherzo/reaper-v600/tools/build_reaper.py` (lines 355-398, the c16 version with
   case-insensitive row names) into `tools/build_reaper.py` and call it in the state builder after
   `load_articulations()` when `mix.json` tracks[...] has `region_gain_db`. It multiplies `regionMap.regions[].volume`
   of every region whose key span holds the pitch.
2. `build/mix.json`, per track `"region_gain_db": {"rows": null, "pitch_db": {...}}`, starting values (dB, minus the
   measured offset, rounded; `proposal.json` in the scratch folder holds them in this form):
   - Horn 1: 53 +3, 55 +2, 56 +4, 60 -1.5, 62 -5, 63 -2, 66 +3, 67 +2, 68 +5
   - Flute 1: 72 +3, 73 +5, 75 +2, 78 +2.5, 84 -3, 85 -3, 89 -3, 90 -5, 91 -6
   - Cor anglais: 56 -2.5, 61 +2.5, 65 +4, 69 -4
   - Bass clarinet: 39 +4, 44 -4
   - Bassoon 1: 56 +3.5, 61 -3.5; Bassoon 2: 48 +4, 51 +2.5
   - Clarinet 1: 68 +3, 73 +3, 79 -3; Clarinet 2: 68 +3
   - Violins I: 65 +3, 72 -3; Violins II: 61 -3, 65 +3, 72 -3
   - Violoncellos: 51 -2.5, 53 -2, 55 +2, 56 -2.5, 60 +3.5
   - Double basses: 32 -4, 39 +4, 46 +2, 48 +5, 49 +5, 51 +6
3. Shared regions, checked in the patch files (`spans.py`): every listed pitch has its own regions on the rows these
   tracks play, except 5 regions each for Cor anglais F 4 (with F sharp 4), Bassoon 1 A flat 3 (with G 3), and the
   tremolo rows of Violins I (F 4 / E flat 4, C 5 / D flat 5) and Violoncellos (E flat 3 / D 3, G 3 / F sharp 3). Use
   `"rows"` to leave "Tremolo" out on the strings.
4. Layer-specific cases the plain table cannot hold: Horn 1 E flat 4 (+4.3 soft, -2.9 loud), Flute 1 C 6 (+9.4 at CC11
   60-85 on 2 notes, -0.7 above 85), Bassoon 1 F 3 (+4.4 soft, -2.5 loud). Start with the smaller value (as listed) and
   fit the rest after the pass; if needed add a per-pitch form of the scherzo's `row_dyn_db` (groups whose name ends in
   pp / mf / f / ff).
5. After the gains are in, rerun `cycles/c55/actor_scripts/comp55.py`: the section rows of `cell_rows_c55.json` were
   derived with the uneven pitches in (Double basses [238, 262, +2.2] lifts the hot A flat 1 further).

Expected (simulated on the per-note table, `sim.py`, as a plain gain per pitch): notes out by 2 dB or more 171 -> 109,
by 3 dB or more 101 -> 50; Horn 1 theme sd 3.0 -> 1.6 dB (14 -> 4 notes out), Double basses 23-30 4.4 -> 2.1,
Bass clarinet 2.7 -> 1.3, Cor anglais 3.0 -> 1.5, Bassoon 1 71-78 4.0 -> 2.3, Horn 1 65-70 2.0 -> 0.3; master bars 30,
35, 48, 71, 73 back within about 1 dB of their neighbours' trend (inferred from the stem changes).
Verify: needs a pass (the scherzo verified on one whole-piece pass; its misses were a row-name case mismatch on the cor
anglais and legato-joined horn notes 2-5 dB under target). Before the pass the tables can be previewed offline as
stem times gain per note (`lib53.Render` with a per-note gain; simulation only). After: rerun `notes.py`, `lines.py`.

### 2. Flute 1 "LegRep RRx4" at qn 136 (bar 44) is 13 dB over the note it repeats: set the row's volume in the patch

Where: Flute 1, the slurred E flat 5 repeat, qn 135 -> 136, held 3.0 s; master bar 44.
What (measured): E flat 5 on "Leg Slur MAX" at qn 135 -51.8 dB heard (instrument -58.2), the repeat on "LegRep RRx4" at
qn 136 -38.8 (instrument -44.9) at the same CC11 (35.5 / 34.0). In c54 a level shape held it at -48.4. The Flute 1 stem
of bar 44 is +8.1 dB against c54 and the master +3.3; the pp close of theme B is its loudest flute bar.
Fix: the row volume knob (manual p.137). Port `row_volume_db` from `symphony/mvt3/reaper-v600/tools/build_reaper.py`
(lines 287-291: `row["volume"] = 10 ** (dB / 20)` inside `load_articulations`, called with
`MIX.get("row_volume_db", {}).get(track)`); `build/mix.json` `"row_volume_db": {"Flute 1": {"LegRep RRx4": -9.5}}`.
The row is used by this one note (`art_counts` "LegRep RRx4": 1), so nothing else moves.
Expected: qn 136 at about -48.3 dB, bar 44 master back to about -41.5. Offline as a gain on the note; confirm on a
range pass of bars 43-44 (the re-attack against the end of 135 should stay about 5 dB, MANUAL-GAPS c37).

### 3. Oboe 1 phrase heads at velocity 53 enter 5 dB under their line

Where: Oboe 1 qn 42 (bar 15), 54 (bar 19), 139, 144 (bar 46), 188.
What (measured): on "Leg Slur MAX" the four heads at velocity 53 sit 4.8-5.5 dB under the fit of row, CC11 and pitch
(144, a re-tongued B flat 4 at velocity 53, 4.9 under its line); the three heads at velocity 83-91 sit at -2.4 to +0.4.
Heard: bar 15 C 5 -51.6 dB for 1.65 s against -42.5 / -42.2 on the next two notes; bar 19 C 5 -53.5 against -43.8.
c54 covered them with fills (deviation -1.3 and -3.0 there). No other wind track shows it (heads minus joined notes:
Cor anglais +0.9, Clarinet 1 +1.1, Bassoon 1 +0.6, Horn 1 -0.7; Flute 1 +3.3).
Fix: velocity, not level: `build/score_config.py` `VEL_SET["Oboe 1"] = {42.0: 86, 54.0: 86, 139.0: 86, 144.0: 86,
188.0: 86}` (the value `LEG_VEL_BY_CC` gives wind legato targets at this CC11).
Expected +3.5 to +5 dB on those notes (inferred from the velocity 83-91 heads). Needs a range pass (bars 15-20 and
45-47): check the level, the 2-5 kHz share of the first 80 ms (a harder attack is possible) and S for the head.
Until this is done do not fit Oboe 1 pitch gains: its C 5 and A flat 4 offsets (-4.1, -2.7) are mostly these heads.

### 4. Role, section-row and hairpin-gain edges that step inside sounding notes (leftover per-note steps)

Where: all tracks; worst at the section boundaries qn 204, 262, 292, 108, 226, 87.
What (measured on `vol_points()` of `build_fix`, `steps.py`): 155 notes move 3 dB or more inside the note (58 with no
hairpin or dynamic change; the actor's count 157 / 47 uses a slightly different span rule). 140 notes hold a move of
1.5 dB or more within 0.25 s, 58 of them unmarked. Nearest table edge: role start 47, role end 36, section row 20,
hairpin or hairpin-gain end 16, none within 0.8 qn 20. 90 of the 228 edges of `cell_rows_c55.json` fall inside a
sounding note. The cause is the lead: the edges are keyed to the score onset and the note-on is 0.03-0.25 qn before it,
so the step lands 50-300 ms into the note. Largest:
- Horn 1 qn 226 (bar 67, the solo alone): +5.3 dB between qn 225.9 and 226.0, note-on 225.861 (role [226, 238, +2] and
  the dynamic trim together).
- Horn 3 qn 204 (bar 61 downbeat): points 6.7 dB at 203.875, 2.13 at 204.0, 5.52 at 204.125: a 4.6 dB notch 0.25 qn
  wide on the head of the ff chord (hairpin gain released at 204, role and section row start at 204, not chained).
  Horn 2, Tuba, Trombone 2, Bass trombone, Violins II and Violas carry 2.3-3.3 dB of the same at 204.11.
- Violoncellos qn 87 (bar 30 final note) +5.2 dB in 0.25 s and qn 81 -5.1; Flute 1 qn 262.6 +4.9; Violas and Violas
  div qn 292 +4.3 (ppp coda, exposed); Violins II qn 108 -4.1; Clarinet 1 qn 262 -3.4; Oboe 2 / Horn 2 qn 210-212
  -3.5; falls of 3-5 dB in 0.25 s after the hall are also S3 cases (Violoncellos 273.8 -4.8, Violins I 262.05 -3.9).
Fix (slow rows only; nothing per note): in `tools/score_to_parts.py` where roles, `_all` rows and
`cell_rows_c55.json` rows are added (`vol_add("slow:role", ...)`, about line 4104, and the cell-row block), key each
edge to the track's moved note-on instead of the score onset: for an edge at e with an onset of the track at sq within
0.02 qn, end the ramp at that note's `qn` minus 0.02 and start it min(0.5 qn, the gap or the previous note's last
0.5 qn) earlier; for an edge with no onset within 0.3 qn (inside a held note) ramp over 2 qn or more, at most 1.5 dB
per second. Extend `ROLE_CHAIN` to section rows and hairpin-gain releases so rows that meet at one qn crossfade
instead of summing a release and an entry (the 204 notch). New defaults `ROW_EDGE_TO_NOTE_ON = True`,
`ROW_EDGE_MAX_DB_S = 1.5`.
Expected: fast moves inside notes 140 -> under 30 (the rest are printed hairpins, dynamic changes and the timpani roll
rules), unmarked 58 -> under 10; section levels unchanged within 0.3 dB. Decided offline: rerun `steps.py` (or
`tools/env_stats.py`) on the new build, simulate on the stems with `lib53.Render(render, old, new)`, and check that
`acc55.py` cells and S (`tools/s_onsets.py`) do not move (c55 found that level steps on the beat move S readings; this
removes such steps, so S within 25 ms should rise from 613 toward 640).

### 5. Coda: Clarinet 1's motto tail lost its middle, the last note stands out, the basses dropped, the final chord fades less

Where: bars 85-92 (qn 280-304); master bars 86-88 -2.3 / -1.8 / -1.7, 89 +2.0, 91 +1.8, 92 +3.1 against c54.
What (measured): Clarinet 1 heard E flat 5 -48.2, D 5 -47.7, D flat 5 -46.7, D flat 5 -46.6, C 5 -40.5 dB (c54: -48.3,
-44.5, -41.7, -42.6, -44.4). The three middle notes are 3-5 dB lower and the resolution C 5 is 6 dB over them
(instrument level -50.3 at CC11 33 against -55.8 / -56.4 at CC11 34-36: D flat 5 is -3.3 dB on 6 notes, C 5 +1.0).
Double basses qn 282-292 are 3.9 / 3.4 / 5.7 / 2.8 dB under c54 (F 1 at 286 -57.2). Final chord, last re-bows (qn
299.8-303.4): Violins I +2.4 / +4.6, Violins II +5.1 / +3.4, Violoncellos +4.7, Double basses +4.6 / +4.7 / +3.6 over
c54, so the morendo of bar 91 into the ppp chord falls about 3 dB less.
Fix:
- Clarinet 1: the region gain 73 +3 of finding 1 (rows "Leg Slur" and "Sus Non Vib"), and one phrase row over the three
  middle notes in `build/roles.json`: Clarinet 1 [282.9, 291.9, 2.0, 0.5] (qn 283, 286, 289; three notes, 10 s), ending
  in the change to the C 5. The short rows [287.4, 289], [284.25, 285.75], [286, 286.9] stay off.
- Double basses: `cell_rows_c55.json` has [274, 304, -4.8] over a passage whose own levels differ by section; replace
  it by two rows, [274, 286, -4.8] and [286, 304, -1.5] (each several notes; values from the c54 levels), or raise the
  basses' `role` [285.9, 299.75, 2, 0.5] to 5.
- Final chord: a fade, on the instrument side first: lower the CC11 targets of the last two re-bows of each string
  track (qn 299.8-303.4) from 22-24 to about 14 (CC11 is before the hall, S3-safe); if a range pass of bars 89-92 shows
  CC11 has no effect that low, deepen the existing `_all` morendo row [300.5, 303.5] from -3 to -5.5 (a fade over all
  tracks and several notes, allowed by the rule).
Expected: bars 86-88 back within 1 dB of c54, bar 89 -2, bar 92 -3; delivered span 19.1 -> about 18.7 dB (inferred: the
10th-percentile short-term loudness rises when bars 86-88 do). Clarinet and basses rows offline (`lib53`); the CC11
morendo needs the range pass.

### 6. Violas' pizzicato triplets bars 41-44: 14 dB between pitches; park CC11 and fit the pitches in the patch

Where: Violas "Pizz RRx4", qn 124-140 (42 notes).
What (measured, note peaks against the passage median): E flat 3 -8.2 dB (4 notes), D flat 3 -4.6, F 3 -3.2, F sharp 3
-3.0 (with +16 velocity already), A flat 3 +1.3, D flat 4 +3.2, E flat 4 +3.4, F sharp 4 +6.3; sd 4.2 dB, median step
2.37 dB (actor: 2.32; c54 1.78). CC11 sits at 35-45 under velocities 42-67, so the row is attenuated twice.
Fix: (a) FINDINGS sections 84-86: hold CC11 at 110 on the pizzicato spans of Violas, Violoncellos and Double basses
(as the harp does since series 1) and carry the printed pp < p > pp in velocity; (b) region gains on the row,
`mix.json` Violas `"region_gain_db": {"rows": ["Pizz RRx4"], "pitch_db": {"49": 4, "51": 6, "53": 3, "54": 3, "61": -3,
"66": -5}}` with the c55 velocity offsets for 54 and 58 taken out again. Shared regions on this row: F 3 with E 3 and
F sharp 3 (10 regions of 80), D flat 4 with C 4 and D 4 (20 of 80), F sharp 4 with F 4 and G 4 (20 of 80); keep F 3
and F sharp 3 equal for that reason.
Expected: sd 4.2 -> about 2 dB, median step under 1.8 dB. Needs a range pass (bars 41-44) because parking CC11 changes
the layer; the Double basses' pizzicato (sd 1.8 dB, all velocity 53) needs nothing.

## Smaller measured points (no finding)

- Climaxes: the Double basses are the loudest dry stem in bars 61-64 (-25.4 dB, Violins I -26.1, trombones -28.0 to
  -28.6, timpani not in the first twelve) and in bars 79-82 (-29.4, Violins I and celli -31.6), +1.2 / +1.4 dB against
  c54 (`loud_eq`). The 56-112 Hz share is still under the Brahms references, so no change proposed; do not add to it.
- Solo margins are unchanged against c54 as section means (actor's figures confirmed on per-bar stems); the losses are
  inside the lines (findings 1-3, 5).
- Phrase heads on "Leg Slur MAX" are louder than joined notes on Violins I (+5.4 dB, 5 heads), Violoncellos (+2.7) and
  Flute 1 (+3.3); the celli's bar 71 head (E flat 3, +6.9 dB against c54) is partly this. Slot A's CC11-over-the-join
  work decides it; no level proposal here.
- Span 19.1 dB and LRA 15.4 LU: no separate change; finding 5 raises the soft end and findings 1-2 remove +3 dB bars
  in soft sections, both of which narrow the span (inferred).

## Do not touch

The slow layers as rendered (hairpin gains, roles over three notes or more, the timpani roll rules, the final fade);
the c55 ramp writing (`VOL_GRID_QN`, `env_simplify_db` 0.1); the violins' and violas' lines of bars 22-30, 53-60 and
71-78, which are as even as in c54 without any trim; the bars 61-64 and 79-82 balance; the timpani stroke velocities
of c55; the basses' pizzicato velocity; `ENV_CLASS` level and shape off. No per-note fader move goes back.
