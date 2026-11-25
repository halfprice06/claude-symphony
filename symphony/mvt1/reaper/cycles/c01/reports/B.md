# Cycle 1, critic B: balance and levels (render c00)

Method: K-weighted levels (BS.1770 filter applied per FFT frame, 25 ms hop) on every stem and the master, per note body (onset +0.08 s to +1.0 s or note end), compared between tracks at the same score onset and the same printed dynamic (from `parts.json` `dyn_curve`). Scripts and tables are in `/private/tmp/claude-501/mockup-loop/mvt1-c01-B/` (`notes.py`, `brass.py`, `solos.py`, `region.py`, `timp.py`). Balance targets are Rimsky-Korsakov's ratios (Principles, "Comparison of resonance": in loud passages trumpet = trombone = tuba = 2 horns, horn = 2 woodwinds; in piano all winds are about equal and one string section equals one wind; in forte a string section equals two winds), which mockup-kit LEARNINGS section 13 found to work. "Measured" means taken from the c00 render or `parts.json`; "inferred" means reasoned.

## 1. Every "sub. p" in the score is ignored: bar 62 and bar 84 play loud where the score says subito piano

Where: qn 244 (bar 62, poco animando) in Violins I, Violins II, Violas (245), Violoncellos, Double basses, Clarinet 1, Bassoon 2, Horns 2-4 and Harp; qn 332 (bar 84) in Violoncellos and Double basses. 13 marks.

What is wrong (measured): `mockup-events.tsv` writes the mark as the dynamic `sub. p`, and `score_to_parts.py` accepts a dynamic only if `v[0] in DYN` (line 824); `DYN` has no `"sub. p"` key, so the mark is dropped and the line keeps its previous level or crescendo. In `parts.json` the dynamic curve at qn 244.5 is 82 (Violins I/II, still rising from the bar-60 mf crescendo), 62 (Double basses, Clarinet 1), 68 (Harp, mf with velocity 86-98 until qn 262) instead of 46. At qn 332.5 the cellos and basses sit at 114 (ff) instead of 46. On the render: master bars 60-64 are -27.7, -28.4, -27.7, -27.0, -25.9 dB, with no drop at bar 62; Violins I are 2 dB louder in bar 62 than in bar 61 (-33.1 against -35.2); the harp is at -35.8 dB in bar 62, 14 dB over its own p in bars 56-58 (-47.6 to -50.5) and as loud as the violin tune. In bar 84 the cellos are the loudest stem of the whole bar at -23.7 dB, their ff level (cello ff median -29.8, p median -44.6), on a printed sub. p: about 15-20 dB too loud.

Fix: in `build/score_config.py`, after the defaults, add `DYN["sub. p"] = DYN["p"]` (and, for safety, `DYN["sub. pp"] = DYN["pp"]`, `DYN["sub. mp"] = DYN["mp"]`). `level = DYN[data]` (line 897) and the hairpin target lookup (line 901) both read the same dict, so no other change is needed. Check after the rebuild that `dyn_curve` is 46 at qn 244.5 on the 12 tracks and at qn 332.5 on Vc/Cb, and that the bar-62 master falls by at least 4 dB from bar 61 (inferred target: a subito p is heard as a clear drop). The bar-60/61 crescendo `hpgain` holds (HP hold until the first onset after the arrival) must also release at qn 244, or the volume envelope keeps up to +3 dB through the subito; check `vol_db` there.

## 2. Trumpets are 8-12 dB too low against the other brass; trombones and Horn 2 a little high

Where: every f, ff and fff brass passage: bars 26-32, 72, 83, 115-117, 122-123, 131-142, 158-162, 167-170.

Evidence (measured, same score onset and same printed dynamic, note bodies):
- Trumpet 1 minus the mean of Horns 1/3/4: -5.0 dB at f (22 onsets), -5.4 dB at ff/fff (24). Target +3 dB (trumpet = 2 horns), so the trumpets are about 8 dB short.
- Trumpet 1 minus Trombone 1: -12.4 dB at f (14), -9.7 dB at ff/fff (9). Target about 0.
- Trumpet 3 minus Trumpet 1: -1.6 dB at f, -5.7 dB at ff/fff. On the bar-122 fff tutti chord (qn 484) Trumpet 3 is at -43.1 dB against Trumpet 1 -33.2, Trombone 2 -22.1, Horn 2 -24.5 and Violins I -16.3; at bar 160 (the fff climax) Trumpet 1 is at -33.7 against Trombone 1 -20.3. Per-dynamic medians: trumpets at f -40.9 to -42.6 dB, horns -35 to -36, trombones -28.8 to -31.8.
- Trombone 1 minus Horns 1/3/4: +6.5 dB at f, +4.6 at ff (target +3). Trombone 2 equals Trombone 1 (-0.1 / +0.5) although its trims are +6/+8 against Trombone 1's +3/+4; bass trombone is 2.4-3.2 dB under Trombone 1.
- Horn 2 minus Horns 1/3/4: +2.9 dB at f, +4.4 dB at ff/fff, 0.1 dB at p/mp. Its `dyn_trim_db` is f +2 / ff +4 against Horn 1/3's +1 / +2, so most of the loud-only excess is the trim (qn 328: Horn 2 -22.4 against -28.4 to -29.2 for the other three).
- Tuba minus Trombone 1: -5.8 / -5.6 dB. K-weighting under-counts the tuba's lowest octave by a few dB (inferred), so leave the tuba for now.

The trumpets are the instruments that should cut through a brass tutti; with these numbers they are absent from the bar-122 and bar-160 chords (inferred from the levels: 10-17 dB under the loudest stems). The soft trumpet notes are in line with the horns (pp: Trumpet 1 -45.8, Horn 1 -45.5), so the fix belongs in the loud trims, not the gain.

Fix in `build/mix.json` `tracks`:
- Trumpet 1 and 2: `dyn_trim_db` {"f": 0, "ff": 0} -> {"f": 6, "ff": 7}; gain stays -3.
- Trumpet 3: `dyn_trim_db` -> {"f": 7, "ff": 10} (it loses another 4 dB against Trumpet 1 at ff).
- Trombone 1: f 3 -> 1 (ff stays 4). Trombone 2: f 6 -> 4, ff 8 -> 6. Bass trombone unchanged.
- Horn 2: f 2 -> 1, ff 4 -> 1 (same as Horn 1 at f, -3 dB at ff).
Expected (simulated from the measured gaps): Trumpet 1 over the horns +1 to +2 dB, Trumpet 1 about 3-6 dB under Trombone 1 at f and 0-2 dB at ff, Horn 2 within 1.5 dB of the other horns. The master changes by less than 0.5 dB at the climaxes, because the trumpets move from -33 to -26 dB under a -13 dB master. After the render, check that the trumpets' 2-5 kHz attack energy on the accented notes stays inside the GENTLE_ACCENT limits (BRIEF item 8): raising the level with the trim keeps the CC11 layer, so it should.

## 3. The coda cello solo (bars 171-174, mp espr.) climbs to f, and the cor anglais imitation is 11 dB under it

Where: Violoncellos qn 680-696, Cor anglais qn 683-694.

Evidence (measured): the printed cello line is mp with five small untargeted hairpins (< 680, > 683.5, < 685, < 691, > 692; the next printed mark is pp at 696). The untargeted-hairpin rules ratchet the line upward: `dyn_curve` 58 -> 79 at 683.4, back only to 69, then 59 -> 80 at 687, then 85 -> 93 at 692 (CC11 93 is above the f table value 88), with a +2.4 to +3.7 dB `vol_db` swell on top. The cello stem measures -31.4, -36.7, -35.0, -36.6 dB in bars 171-174, its own f level (cello f median -34.6, mp median -43.3), 8-9 dB over a printed mp. The cor anglais enters at qn 683 marked p espr. as an imitation of the cello line and measures -44.9 dB (-49.7 to -44.2 per bar), 10.7 dB under the cellos (median of frames where both sound). One dynamic step (mp against p) should be about 3-4 dB (inferred from the per-dynamic medians: about 1.5-4 dB per step across families).

Fix in `build/score_config.py`: `HP_TARGET_AT["Vc"] = {680.0: "mf", 683.5: "mp", 685.0: "mf", 691.0: "mf", 692.0: "mp"}` so each swell peaks at mf (72) and returns to mp (58). Then in `build/roles.json` add `"Cor anglais": [[683, 695, 2.5]]` (the imitation should be 3-5 dB under the cello, not 11). Check after the render: cello bars 171-174 at about -40 to -42 dB, cor anglais 3-5 dB under it, and the bar-175 pp entry (trombones dolce, low strings) still under bar 174.

## 4. Percussion: the suspended-cymbal roll peaks 1.2 s before the crash; the tam-tam is buried at fff and almost inaudible at pp

Where: Suspended cymbal qn 632-636 (bar 159), Crash cymbals qn 636, Tam-tam qn 484 (bar 122, fff heavy beater, l.v. to bar 126) and qn 696 (bar 175, pp soft stick).

Evidence (measured):
- Suspended cymbal: the stroke at qn 632 (key 60, velocity 105, the f take) reaches its peak 0.84 s after note-on, at qn 633.6, while the crash is 1.98 s after note-on (qn 636). Above 4 kHz the roll's peak is only 2.7 dB under the fff crash (-3.4 against -0.7 dB, 0.05 s frames) and is the brightest event in the master at qn 633.7; by the crash it has fallen 16-18 dB. So a printed pp < into the fff crash plays as a near-fortissimo swell that dies away before the climax.
- Crash cymbals: at qn 636 the crash leads the master above 4 kHz (-4.2 against a master of -3.5 dB in 4-12 kHz) and decays 12 dB in 0.75 s. Its level is right; keep it.
- Tam-tam fff (qn 484): -24.7 dB K-weighted in the first second against a master of -10.5 dB (14 dB under), and 14 dB under the master in 2-5 kHz. While it rings alone after the brass release (qn 497-501) it is still 15-17 dB under a master of -28 to -32 dB. A fff heavy-beater tam-tam at the development's climax should be one of the loudest sounds there for its first seconds and audible through its ring (inferred).
- Tam-tam pp (qn 696): -54 to -58 dB against a master of -34 to -37 dB (about 20 dB under) and no energy above 2 kHz (-112 dB): at velocity 40 the soft layer is dark and very quiet. The percussion tracks are in `soft_trim_db._except`, so it also misses the +3 dB that every other pp line gets.

Fix:
- `build/score_config.py` `PERC_MAP["Suspended cymbal"]`: the roll's peak must land on qn 636. Either use a longer crescendo key (62 or 64; measure its peak time first: the patch notes say four lengths, shortest first) whose peak falls about 2.0 s after note-on, or keep key 60 and start it 0.85 s before qn 636 (needs a later start than the written beat; `lead_s` only moves notes earlier, so add a `delay_s` or an explicit start qn to `build_perc_track`). Lower the velocity from 105 to about 80 (the p take, 1-89) so the roll starts pp, or keep 105 and lower `Suspended cymbal` `gain_db` from -6 to -9; target: roll peak 4-6 dB under the crash above 4 kHz, at the crash and not before it.
- `build/mix.json` `Tam-tam` `gain_db` -4 -> +2 (+6 dB), which brings the fff strike to about 8 dB under the master and lets the ring be heard after the brass release. For the pp stroke at qn 696 raise the velocity from 40 to about 60 (`PERC_VEL` or a per-stroke `vel`), so a layer with some upper partials plays, and aim at 10-12 dB under the master (now 20).

## 5. The opening: the solo timpani ppp roll is 12 dB under the strings that join it, and the first cello and bass note blooms 7-10 dB

Where: Timpani qn 0-16 (bars 1-4), Violoncellos/Double basses/Bass clarinet qn 2.9-8.

Evidence (measured): the movement opens with the timpani roll alone for 2.9 qn (3.5 s). Its `vol_db` already settles from -6 to -11 dB over qn 0-3, before any other instrument plays, so the opening roll measures -56 to -60 dB and the whole bar-1 master is the timpani at about -58 dB. Once the low strings enter, the roll is 12 dB under the quietest string section (timpani -59.7 against double basses -47.9 over the note); the target that worked in movement II is 3-5 dB under the quietest sustained string section (LEARNINGS section 13). The other ppp rolls agree: bar 76 timpani -58.0 against violas -49.5 (8.5 dB under). Per printed dynamic the timpani's pp median (-60.6 dB) is lower than its ppp median (-56.5 dB). Separately, the first string note swells far over its printed pp: the cellos' pickup G2 (score qn 3, moved to 2.9, Leg Slur MAX first note, velocity 41) rises about 10 dB over the body of the following note within 0.4 s (0.25 s windows: cello stem -36.4 dB at qn 3.25-3.5 against -44 dB from qn 3.75; 0.05 s windows: a 10-11 dB fall at the join into qn 4), and the double basses' pickup does the same by about 7 dB (-43.1 against -50). The master reaches -33.4 dB there, the loudest moment of bars 1-4.

Fix:
- Hold the timpani roll's settle until the first entry of another instrument (qn 2.9) instead of starting at qn 0, and settle only 3-4 dB. If the settle logic is not easy to change for one roll, add `"Timpani": [[0, 16, 7]]` to `build/roles.json` (this offsets the settle: about -52 dB, 4 dB under the basses) and `[300, 304, 4]` for bar 76.
- Trim the pickup blooms in `build/note_trims.json`: `"Violoncellos": {"3.0": -8}`, `"Double basses": {"3.0": -6}` (0.1 s ramp, `NOTE_TRIM_RAMP_S`). Check that the pickup then sits within 2-3 dB of the following note's body, so the printed pp < > of bar 2 grows from the pickup instead of falling from it.

## 6. Oboes do not grow from f to ff, and the bar 56-61 espressivo countermelody is 10-15 dB under the tune

Where: Oboe 1/2 at every ff (e.g. bars 98-102, where flute, oboe and Violins I carry the ff melody in octaves); Clarinet 1 and Horn 2, qn 220-244 (bars 56-61, "espr." p, against Violins I/II "molto cantabile" p).

Evidence (measured): Oboe 1's note median is -38.3 dB at f and -38.7 at ff (102 notes, CC11 104-122): no growth, where flutes grow 6 dB, clarinets 2.9, Violins I 7.1. At the same onsets and the same printed dynamic, Oboe 1 is 6.0 dB under Flute 1 and 3.7 dB under Clarinet 1 at ff (1.3 and 3.3 dB at f). In bars 98-102 Oboe 1 is 4-14 dB under Flute 1 and 8-12 dB under Violins I. Rimsky's ratio is about equal woodwinds in forte. In bars 56-61, Clarinet 1 (-45.2 dB) and Horn 2 (-40.7 dB), playing the printed espr. countermelody in unison, are 14.6 and 10.6 dB under the rest of the texture (medians of frames) and under the p harp arpeggios (-36.8 dB before the sub. p fix); together they are about 7 dB under the two violin sections. A countermelody marked espr. should be 3-5 dB under the tune (inferred from movement II's role cuts, LEARNINGS section 13).

Fix: `build/mix.json` Oboe 1 and Oboe 2 `dyn_trim_db` {"f": 1, "ff": 0} -> {"f": 2, "ff": 4} (expected: Oboe 1 about 2 dB under Flute 1 and level with Clarinet 1 at ff). `build/roles.json`: `"Clarinet 1": [[220, 244, 3]]`, `"Horn 2": [[220, 244, 2]]`, and `"Harp": [[220, 244, -2]]`, released over the last 2 qn into the bar-62 subito (after finding 1 is fixed, re-measure the harp first: it may already drop by itself).

Do not touch: the crash-cymbal level at qn 636; the string section balance by dynamic (Violins I f -32.9 / ff -25.8, about 3-4 dB over a single wind at f as Rimsky's ratio asks); the double basses' level and EQ (20-100 Hz share -14.6 dB, inside the -14.5 to -12.5 target, no boom measured); the global `soft_trim_db` {ppp 3, pp 3, p 3.5} (pp and p medians agree across winds, horns and strings within about 4 dB); the horn-solo and cello unison of bars 47-53 (both at about -35 dB, harp and divisi strings 8-12 dB under); the oboe solo at bars 145-147 (4.8 dB over everything else).
