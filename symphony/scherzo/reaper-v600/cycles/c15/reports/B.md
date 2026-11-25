# Cycle 15, critic B: balance and levels (on the c14 render)

Measured on `cycles/c14/render/` stems and master, `build/parts.json`, `build/mix.json` and the tables in `build/`. The
volume envelope was split into its layers by running a copy of `tools/score_to_parts.py` in scratch with every
`vol_parts.append` tagged by its call site (output identical to `build/parts.json`: no track differs in `vol_db` or
notes; the layers add up to the written envelope within 0.01 dB), then passing each layer set through
`build_reaper.py` `vol_points`. Levels are mean-square dB. "Measured" and "inferred" are marked per item. Positions are
score quarter notes (qn); bar b starts at qn 3(b-1).

## Manual notes (May 2021 HO manual, PDF pages 123-126: timpani)

| what the manual says | where it applies here | does the render follow it |
|---|---|---|
| p.123, 125: on the long-hit row "Note Velocity also controls dynamics (up to 16 levels)", round robin x2; CC11 and velocity set loudness | every stroke of motive x; the f / ff strokes of bars 101-120, 301-320, 333-339 | Partly. The f strokes play at velocity 85-98 and the level comes from a +6 dB spike in the track envelope on each of 86 strokes (`TIMP_LOUD_ATTACK_DB`); only the summit strokes reach velocity 121-125 (finding 3) |
| p.124: rolls (KS D#0) take their dynamic from CC1 in 8 layers; the recorded crescendos (KS E0, three lengths, two velocity levels) are "the most realism" | rolls of bars 101-103, 129-130, 205-208, 237-240, 285-286, 303, 332, 336 | CC1 map in use (`TIMP_CC1_MAP`); the recorded crescendo row is not used (MANUAL-GAPS #7). No roll is the loudest stem in any bar (best rank 2, bars 207 and 237): Dan's roll rule holds |
| p.124, 126: the Short row gives "more realistic stops and dampening effects than are possible with automation alone" | the 7 printed staccato strokes; the stroke before the G.P. | Followed (`TIMP_STAC_ROW`, `TIMP_DAMP_AT`) |
| p.123-124: left-hand keys C1-A2, right-hand keys C3-A4; hits within 65 ms become double hits | alternated strokes of motive x (eighths are 114 ms apart, so no double hits) | Followed (`TIMP_RH_ALT`, left-hand velocity adds) |
| p.125-126: Timpani Hard KS has the same five rows; hard sticks give "a brighter timbre overall" and clear single hits in rolls | the score prints hard sticks for bars 1-340 and soft sticks from 341 | Not followed: felt throughout (MANUAL-GAPS #6). c14 freed about 2 GB, so one more instance now fits; finding 3 is the cheaper first step |
| p.124: "CC 11 (Expression) and Note Velocity control overall loudness" | the track has no CC11 lane (`score_to_parts.py` line 4487: "the timpani patch has no CC11"; CC7 is used) | Conflict between the manual and the code comment; not tested by me |

Stale lens text, checked against the score: trumpets, trombones and tuba rest in bars 289-324 (`sections/dB.ily`
c428, c033), and the timpani roll before the reprise tutti starts in bar 303. The stems are silent there as printed.
The reprise tutti measures -20.5 dB against -20.1 for bars 105-120 without them.

## 1. The envelope carries balance in some layers and only shape in others; the test in ONE_TIME_c15 must separate them

Where: all tracks; the per-note layers of `parts.json` `vol_db`.

What (measured). Unlike Movement I (0.3 dB or less per track), several scherzo tracks change level by 2-8 dB per
section when every per-note layer is removed, because some per-note layers hold levels, not shapes. Stem level change
when one layer is removed:

| track | layer | sections and change |
|---|---|---|
| Violins I | `SHORT_CC11_PARK` level return | bars 13-56 +2.1, retransition 241-252 +8.2, reprise +1.6 |
| Violins I | `LEVEL_SHAPES` (c13 / c14 theme-head rows, row-level steps) | bars 13-56 +2.3, 57-104 +6.3, reprise +2.1, tutti 301-324 +1.8 |
| Violas | park return | bars 13-56 +2.3, retransition +6.4, reprise +1.3 |
| Violoncellos | park return; `LEVEL_SHAPES` | +1.7 (bars 13-56); tutti 105-120 -2.1, trio 185-208 -2.8 |
| Timpani | stroke spikes (`TIMP_LOUD_ATTACK_DB`) | tutti 105-120 -4.3, tutti 301-324 -3.9, coda -3.1, bars 13-56 -3.1 |
| Flute 1 / Flute 2 | row trim (Stac DblTng +6) | tutti 105-120 -2.7 / -3.5 |
| Oboe 1 | row trim | tutti 105-120 +2.2, tutti 301-324 +1.6 |
| Clarinet 1 | pitch trims | codetta -2.9, trio 209-224 +2.3, tutti 301-324 +1.8 |
| Cor anglais | pitch trim (A4 -3.5) | bars 57-104 +2.1, 121-140 +3.1 |
| Horn 4 / Horn 1 | pitch trims | Horn 4 trio drone and codetta +3.9, bars 57-104 -2.5; Horn 1 codetta -3.5 |
| Horn 3 | `UNI_BOOST` | tutti 105-120 -3.4 (it carries Horn 4's unison; Horn 4's stem is silent there) |
| Double basses | pizz. pitch steps | codetta +2.9 |

Brass (trumpets, trombones, tuba), Harp, Bass clarinet, Bassoon 2, Contrabassoon, the solo and Violas div change by
0.3 dB or less outside the coda's accent swells.

Do the level layers help? Median level step between consecutive long notes at one printed dynamic (CC within 6), with
and without the per-note layers: Clarinet 1 2.6 / 4.2 dB (steps of 6 dB or more 10 / 37), Violas 3.6 / 4.5, Double
basses 2.2 / 2.9, Horn 1 1.5 / 1.9, Bassoon 1 2.5 / 3.0; no gain on Flute 1 3.1 / 3.1, Oboe 1 2.7 / 2.9, Violins II
1.2 / 1.2, Clarinet 2 2.5 / 2.4, Violoncellos 2.2 / 2.1; worse on Violins I 1.4 / 1.1. Clarinet 1's pitch trims
(G#4 +4, B4 +4.5, C#5 +4.5 against A4 -2.5, C5 -2, D#5 -2.5) look alarming in REAPER, a 6.5 dB zigzag between
neighbouring pitches of the trio tune, but they correct sample levels and should stay.

Notes that move without a marking (measured): 1,251 of 5,759 notes (22 %) have more than 3 dB of envelope swing inside
the note; 407 would have it from the slow layers alone (hairpins, trims through long notes). 525 of the 1,251 (42 %)
carry no accent, sf, hairpin or dynamic. By the layer with the largest swing: pitch trims 111, slow layers 104 (role
edges and soft-trim steps under a sounding note), row trims 93, timpani spikes 65, `LEVEL_SHAPES` 33, park and metric
steps 23, note trims 21, early fills 17, wind detach dips 15. Notes of an eighth or less: 527 of 1,949 have more than
0.5 dB of movement inside the note.

`UNI_BOOST` (measured): 74 notes on 7 tracks, +3.0 dB (one +4.8 on Horn 3). It changes level between adjacent notes
of a line at only two joins (Bassoon 1, qn 156 and 161.85). In this movement it is already a phrase level; the finale's
note-to-note switching does not occur here.

Fix (tools; the split ONE_TIME_c15 item 1 asks for, with three classes instead of two):
- `tools/score_to_parts.py`: tag each `vol_parts` item with a class and write three lanes to parts.json.
  *slow*: roles, `hpgain`, timpani `settle` / `flat` / roll trims, held-decrescendo, `ARRIVAL_WEIGHT_AT`, chord, fade.
  *level* (one value per note or per run; carries balance): pitch trims, row trims, note trims, the park return without
  `beat_db`, `UNI_BOOST`, the c14 row-level steps and theme-head rows.
  *shape* (moves inside a note): accent swells / fits / bodies, timpani spikes, early fills, re-bow and loop fills, join
  notches, wind detach dips, slur-pair releases, `beat_db` metric steps, `bloomv`.
- Run the "off" and "capped at 3 dB" tests on the *shape* class only. Switching the *level* class off moves balance by
  the amounts in the table and would need the roles refitted.
- Write the *level* class as one flat value per note: the pitch-trim ramp of 0.25 qn from the moved onset
  (`trim_shape`, the `ramp == 0.25` branch) takes half of an eighth at quarter 264. Use the short crossfade the mirror
  branch already has (`m - 0.05` to `m + 0.03`) for every pitch and row trim, keyed to the next note's score onset.
  Write `UNI_BOOST` and the park return as one row per run of notes, not one shape per note.
- Per-layer verdicts for the shape class are critic A's (stem test on the main lines); from the balance side none of
  them is needed for a section level except the timpani spikes (finding 3).

## 2. Two thirds of the envelope points are slow layers drawn as stairs

Where: `tools/build_reaper.py` `vol_points`; every track.

What (measured). 40,724 points in the score span (146 per second over all tracks; Violins I 19.9 per second, celli
14.4, violas 14.3, Violins II 12.7, Clarinet 1 8.2; the two reference projects 0.01-0.36). 81 % of all points lie on
the 0.125 qn grid and 38 % are collinear with their neighbours within 0.05 dB. With every per-note layer deleted,
27,914 points remain: the slow layers alone are 69 % of what Dan saw. Cause: `val_at` samples `vol_db` (itself a step
lane on a 0.25 qn grid) and the dynamic trim (`trim_at` on the 0.125 qn `dyn_curve`) at every grid point, so each
hairpin gain and each trim change across a hairpin becomes a point every 28-57 ms. Example: Trombone 1, bars 101-103,
one straight +2 dB hairpin gain over 9 qn is written as 36 points 0.055 dB apart. The Violin I solo has 493 points
for 19 notes, all from slow layers.

A Douglas-Peucker pass with a vertical tolerance (computed on the written points):

| | points now | within 0.1 dB | within 0.25 dB |
|---|---|---|---|
| all tracks, full envelope | 40,724 | 19,585 | 14,718 |
| all tracks, slow layers only | 27,914 | 8,555 | |
| Violins I (full / slow only) | 5,538 / 2,567 | 2,280 / 530 | 1,683 |
| Violas | 3,961 / 2,420 | 1,913 / 772 | 1,435 |
| Violoncellos | 3,996 / 2,491 | 2,041 / 780 | 1,507 |
| Clarinet 1 | 2,281 / 1,841 | 1,369 / 691 | 1,009 |
| Bassoon 2 | 1,366 / 1,324 | 422 / 385 | 237 |
| Violin I solo | 493 / 495 | 116 / 107 | 83 |

Fix: in `vol_points`, just before the `out = []` loop, simplify `(grid, vals)`: keep the first and last point, find the
point farthest (in dB) from the straight line between kept neighbours, keep it if the distance is over
`mix.json` `env_simplify_db` (0.1), recurse. Points of fast shapes survive because they deviate by more than the
tolerance. Check with `cycles/c14/actor_scripts/envdiff14.py` that no track differs from the unsimplified build by more
than 0.1 dB. One caution (inferred): REAPER interpolates between points in its own envelope scale
(`ScaleToEnvelopeMode`), not in dB, so test the tolerance on the scaled values or keep a point at least every 2 qn on
ramps of more than 3 dB. This changes nothing audible; it removes the stairs so that what remains visible is what
moves the sound.

## 3. Timpani: the level of every loud stroke is an envelope spike; put it in the velocity

Where: Timpani, 86 strokes printed f or louder (bars 55, 91, 94, 104-120, 129, 131, 200, 209, 285, 287, 304-320, 333-339).

What (measured). `TIMP_LOUD_ATTACK_DB` 6.0 writes +6 dB in 10 ms, held 0.25 qn (57 ms), gone at 0.75 qn (170 ms) on
each of these strokes. It is the largest group of unmarked spikes on one track (52 % of timpani notes have more than
3 dB inside the note; 65 unmarked) and it carries 3.1-4.3 dB of the timpani's tutti level (finding 1). The strokes
themselves play at velocity 85-98. De-enveloped level over 20-170 ms of isolated strokes: B at velocity 98 -37.3 dB,
at 121 -34.2 dB (+3.1 dB for 23 steps); E at 80 -41.2, at 96 -38.7 (+2.5 for 16). The spike adds 2.9 dB over the same
window. So about 22 velocity steps give the same level from the instrument's louder recorded layers (manual p.123:
velocity selects up to 16 dynamic levels), with the stick attack and the ring in their recorded proportion, and before
the hall.

Fix: `build/score_config.py`: `TIMP_LOUD_ATTACK_DB = 0.0`; add 22 to the velocity of Lng and Sht strokes whose printed
level is f or louder, capped at 125 (the `TIMP_VEL` table, or a generic `TIMP_LOUD_VEL_ADD = 22` next to
`TIMP_METRIC_VEL`; the summit strokes at 121-125 stay). Verify on the stem after the render: stroke level over
20-170 ms within 1 dB of c14 (-34.6 to -35.9 dB at f on B), timpani tutti levels within 1 dB (bars 105-120 -36.0),
and the 2-5 kHz share of the first 80 ms (BRIEF item 9) not more than 3 dB over c14; if it is, use +14 and a 2 dB
role. The velocity slope rests on two pitch pairs (measured); the equal result is inferred until rendered.

## 4. Bar 104: the brass f chord is as loud as the whole string section's ff, and louder than the tutti it prepares

Where: bar 104 (qn 309-312), Trumpets 1-2, Trombones 1-2, Bass trombone, Tuba (held f chord after pp <); bars 105-120.

What (measured). Bar 104: Trombone 2 -28.7, Trumpet 1 -29.3, Tuba -29.4, Trombone 1 -30.3, Bass trombone -31.7 dB
and Trumpet 2 -31.8 against Violins I (ff) -28.5, Violins II -27.4, Violas -31.0, celli -31.2 and Double basses -30.2.
The six brass stems sum to -22.3 dB and the five string stems to -22.4 dB. The same players' f at the summit reads -33 to -37 (bars 336-339) and their f quarters in
bar 105 -33.4 to -37.4. The master is -17.0 dB in bar 104 against -19.3 in bar 105 and -20.1 over bars 105-120, so
the bar before the theme is the loudest bar of the first tutti; `RIDE_TRIMS` already holds bars 101-104 back by 1.5 dB
in the delivery. The envelope adds +4 dB there (hairpin gain +2 and the role `[309, 360, 2]` on the four low brass).
Trombone 2 is also 1.6-3.3 dB over Trombone 1 through bars 103-120 (-35.6 against -37.7 over 105-120; `dyn_trim_db` f
+1.9 against -0.9), while the two are equal in the coda.

Fix: `build/roles.json`: start the low-brass role at 312 instead of 309 (Trombone 1, Bass trombone, Tuba
`[312, 360, 2]`), delete Trombone 2's row (no role in 309-360: it then reads -37.6 over bars 105-120 against Trombone
1's -37.7), and add `[309, 312, -1.5]` on Trumpets 1-2. Brass in bar 104 falls 2 dB (low brass) and 1.5 dB (trumpets).
Expected (computed from the stems, returns not counted): brass sum in bar 104 -24.1 dB, master about -17.5 dB. A stem fix can do this without a render. Inferred:
that the brass chord masks the violins' hemiola; the levels are measured.

## 5. Double basses, bars 46-48: two notes of the f bass line are 7-10 dB under their neighbours

Where: Double basses, second idea, qn 134-144 (Leg Slur MAX, printed f, CC11 81-85 throughout).

What (measured, stem level per note, 40-440 ms): G2 -37.9, B1 -39.3, D2 (qn 138) -45.7, E2 (qn 140) -48.6, G#1 -36.6
(with its -6 note trim), A1 -38.7, A2 -38.8. Per half quarter the stem runs -34..-38, -42, -45, -48..-50, then -35.
The same pitches at qn 150 / 152 (CC 96-97) read -38.9 / -38.1, so this is the pair of joins, not the pitch. The
contrabassoon (-41 to -47) and celli hold the line; the low octave drops out for about 0.9 s. Other single joins over
6 dB at one printed level: 639 -> 642 A#1 -14.5 (bars 214-215), 195 -> 198 +8.8, 576 -> 579 +7.5.
After the bell removal the ff arco tutti notes are within 2.8 dB: E1 -32.6 (17 notes, +2 trim), B1 -31.2, A1 -30.8,
D2 -30.9, G1 -29.8 (4 notes: qn 162, 351, 939, 951).

Fix: `build/note_trims.json` Double basses: `"138.0": 6`, `"140.0": 8` (in place of 1.0), flat steps on the score
onset (expected -39.7 and -40.6, computed: the envelope is a gain after the instrument); `"642.0": 6`. G1 at ff: a -2
note trim on 162, 351, 939, 951 closes the E1 / G1 gap to under 1 dB; low priority. These are bass level trims, the
class Movement I's c56 test found necessary; no shape inside the note.

## 6. Delivered span 19.8 dB: take it from the summit, and retire the trio low-mid target

Where: the delivery (`RIDE_TRIMS`, `tools/deliver_master.py`); bars 336-339; bars 169-184.

What (measured on the mp3, ebur128 short-term). Maximum -9.7 LUFS at 242.7 s (bar 337); the two theme tuttis reach
-14.1 and -14.2, the 95th percentile is -14.5, the 10th percentile -29.5. The summit stands 4.4 dB over every other
loud passage and sets both the span (19.8 dB, target 16-19) and the limiter (3.0 dB; the four highest pre-limiter
peaks, +1.5 to -0.3 dBFS, are all at 240.6-242.3 s). The soft end is broad: fourteen separate passages dip under the
10th percentile (bars 10-11, 58-62, 137-142, 290-294, 323-327, 341-343 and others), so lifting one of them does not
move it.

Fix: `build/score_config.py` `RIDE_TRIMS`: add `[(1004.0, 0.0), (1005.0, -1.0), (1016.5, -1.0), (1017.0, 0.0)]`
(delivery only). Expected: span 18.8 dB, limiter about 2 dB, summit still 3.4 dB over the tuttis (inferred from the
measured profile; rerun `deliver_master.py` on the c14 master to confirm before the render).

Trio 169-184 low-mid share (-5.3 dB against the -6.3 I asked for in c14): measured per stem, the 140-355 Hz band of
that passage is the cello tune itself (the celli's band is 1.6 dB under the master's band; next are Bassoon 2 at -9.6,
Horn 3 at -12.2, the string return at -13.3, the basses at -14.7). The target cannot be met without lowering the
melody. Withdraw it; no change.

## Do not touch

Trio tune balances (measured): Clarinet 1 -38.8 over harp -49.2 and horns -50.1 / -53.3 (bars 153-168); celli -39.1
over Violins II -47.6 and basses -46.4 (169-176); Violins I -39.7 level with the celli (177-184); Oboe 1 -41.9 / -41.3
over harp -52.4 and basses -49 to -51 (bars 185-188). The solo (bars 349-356): solo -40.2, Flute 1 -47.3, Violins II
-49.3, Violas div -55.5. Horn 1's tail -37.5 over -45.6 and lower (357-360). Timpani rolls (never the loudest stem).
The summit order (Violins I -21.6 to -24, trumpets f -28.5 to -30.5, low brass -33 to -37). The basses' c14 EQ (bells
removed, 98 Hz halved). Clarinet 1's and the horns' pitch trims as levels. The hall (c14: G.P. drop 20.7 dB, RT60
1.30 s, inside Dan's limits). The brass resting through the reprise as the score prints it.
