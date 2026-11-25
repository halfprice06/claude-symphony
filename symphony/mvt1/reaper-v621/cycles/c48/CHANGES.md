# Cycle 48 (series 2): changes

## For Dan: what to listen for in c48

Notes now land closer to the beat. About 110 individual notes that came in early or late in both of the last two renders were moved, most of them in the strings. Thirty notes that started on time but reached full volume late now get a short level lift. Their volume now peaks a median 33 ms after the beat instead of 117 ms. In the first fugato (bars 85-96) the accented note at the head of each subject entry is now 1.5-2.5 dB louder than the staccato eighths after it. Before, it was level with them or under them, so the subject read as a run of short notes with no accent. In the soft Lento chords (bars 6-7 and 13-14) the double basses can be heard again under the cellos. In bar 11 the timpani roll stays under the strings' crescendo until the bar-12 stroke. In bar 81 the second violins' tremolo crescendo no longer covers the first violins' and flute's entry. In the coda the basses' repeated C eighths in bars 167-170 no longer limp: the downbeats now carry the weight and sound on time. The coda clarinet solo is 1 dB quieter but still on top. The cello solo's note in bar 172 and the clarinet's B in bar 177 no longer sag after the change of note. The soft bass notes now ring longer through bar 174 but still clear before the next chord.

## Values for the other movements (Movement II, scherzo, finale)

1. **Basses' soft release (critic A #3).** With no pp cap, the basses' old pitch hung 8-17 dB under its body 0.35 s after soft chord changes. At 600 ms on the pp sample groups (Movement II's value), all 5 coda changes pass the -12 dB check. The basses' final release to -20 dB takes 0.35 s, the master's 0.53 s (references 0.48-0.79). At 450 ms the bars 1-174 changes improve, with 4 failures against 7 at 600 ms, but the final release to -20 dB shortens to 0.30 s. **Use 600 ms at pp on the basses; the other sections stay uncapped at pp.**
2. **Per-note leads: check where each row actually lands.** Of C's 150 rows, about 30 never reached their note:
   - 20 entry rows sat on notes that are re-attacks to the pipeline: a gap under 0.2 qn, an abutting note or a stac row. Some printed no warning. They moved to `retongue_leads.json`, which adds to the lead the note already has.
   - 7 legato rows were fully absorbed by the lead caps.
   - 6 rows asked for less lead on notes that had none. A lead is never negative.
   - Moving a 32nd-note run later while its target kept its lead squeezed one note to 0.039 qn, so those 10 rows were dropped.
   - `cycles/c48/actor_scripts/realised48.py` compares the requested and realised change of every row. Run it after any lead table edit.
   - Result: on the 108 rows that could be measured, the median |pcX - reference| went 71 -> 30 ms. 96 moved closer and 65 now sit within 40 ms (4 before). Fast-tempo string robust SD against the beat median: Violins I 49 -> 40 ms, Violins II 56 -> 36, violas 50 -> 47, celli 42 -> 41, basses 39 -> 32. Notes over 60 ms off: 27 / 33 / 25 / 31 / 14% -> 20 / 9 / 21 / 29 / 4%.
3. **Swell notes take level, not lead.** These are notes whose -10 dB point is on time but whose half-amplitude point (t50) comes 80 ms or more late. Each fill is 2-4 dB from the score onset, held 0.06-0.15 s, and back to 0 before the next note. Fit each fill on the previous stems against at most +2 dB overshoot. Simulate with the envelope that will actually be written: build_reaper's vol_points from both builds, as in `simenv48.py`. One fill did nothing once the written envelope was used. Result: 29 notes, median t50 117 -> 33 ms after the reference, 22 of 29 within 60 ms.
4. **New shape breakpoints can change the written envelope around them.** Removing a role row that chained a ramp onto a pickup made the pickup up to 4.4 dB louder. A shape breakpoint placed between grid points read the base envelope's step value (kit LEARNINGS c26). List the new-minus-old envelope extremes per track before every render (`cycles/c45/actor_scripts/pdiff45.py OLD NEW --min-db=0.5`).
5. **Sus Marc LITE strokes need their own lead.** Celli 456 at 0.05 s extra passes: time 6 dB under the body 364 -> 84 ms, pcX +85 -> +2 ms. Celli 156 at 0.02 s lost its swell (222 -> 46 ms) but is perceived +77 ms late, and at 0.055 s it swelled again (134 ms). Violas 372 on the same row failed: 338 ms under, +138 ms. Fit the row per note. It is not a drop-in fix.
6. **A full rebuild of a flipped Solo Horn instance works.** Horn 1 (fully rebuilt) matches c46 on 108 unchanged notes with no state run. Trumpet 1 stayed in its c45 / c47 state on a MIDI-only build.

## Run

- **Disk.** 33 GB free when I queued for the lock. When the lock came at 08:49 it was 29 GB. I deleted my own 1.3 GB scratch (simulated stems) and got back to 30-31 GB. 27 GB free at the end. The cycle folder holds 5.6 GB.
- **Lock.** Movement II held it, then the scherzo from 08:20; nobody else was waiting. Mine from 08:49 to 09:45, released with REAPER quit.
- **Main pass.** `start`, `open`, `build_reaper.py build/parts.json jobs --midi-only` (Violins II, Violas, Violoncellos and Double basses fully rebuilt: Opus state changed), full build of "Horn 1", `restart` (33 tracks, 48000 / 512, no input), `render_cycle.py 48`: probe 0 late or holes, state check 0 runs.
- **Pass 2.** `quit`, `start`, `--pass2 open`, `--pass2 --midi-only`. Vla stroke B was built. After the main render's checks I added "Cb pp450 test" and "Vc stroke 156 test" and built them, then `--pass2 restart` (10 tracks) and `render_cycle.py 48 --pass2`. Memory 15 / 28 / 29 GB.
- **Decisions.** `swap48.py`: basses from the 450 ms test stem up to qn 695.8. The alias check was OK, and the test stem matched the main stem within 1 dB on every active 0.5 s frame. Original in `render_first/`. Then `render_cycle.py 48 --measure-only`.
- **Clean-up.** Test tracks deleted from the pass-2 project (`del_tracks.lua`), saved with 7 tracks, `--pass2 quit`, `unlock`. Test stems and `render_pass2/` deleted after measuring (2.0 GB). The test aliases and their mix entries were removed from the data. parts.json is otherwise byte-identical to the rendered one (`rendered_build/`), so REAPER needs no rebuild for c49.

## Accepted

All json edits are in `cycles/c48/actor_scripts/apply48.py`, which re-applies them from `before/`. The score_config c48 block holds the rest.

- **Coordinator, Horn 1:** full rebuild. Against c46: 108 unchanged notes, 3 flagged, 0 runs (metrics/state_check_horn1_c46.txt). Against c47: 0 runs on every track.
- **B #1, basses bars 6-7 / 13-14:** roles `[16, 28, -2]` -> `[16, 19.9, -2, 0.25]`, note_trims +3 at 20 / 22.003 / 24 / 26.003, the G2 pitch trim skipped at 48 / 52.92, roles `[48, 56, -2]` -> -4. Basses minus celli (RMS) 20-28: -9.5 -> -4.8 dB; 48-56: -5.9 -> -2.4 dB. Bar-5 C2 re master unchanged (-0.5).
- **B #2, coda Clarinet 1:** -2 dB over 700.0-706.4 as a LEVEL_SHAPES row. Removing the roles row `[699, 712, 2]`, as B proposed, also removed the ramp on the 699 pickup, which then played up to 4.4 dB louder, so the row stays. Clarinet 1 re master at 700-706: -2.7 -> -3.7 dB.
- **B #3, bar-11 roll:** Timpani `[40.5, 43.95, -3.5, 0.25]`. Roll re master at 41-43: -9.2 -> -12.4 dB.
- **B #4, bar-81 tremolo:** Violins II `[320.5, 324.25, -3, 0.25]`, Violas -1.5. Violins II re master at 321-323.5: -5.5 -> -7.8 dB.
- **A #1, fugato heads:** C's and A's shapes as proposed (celli, violas, Bassoon 1 stac alias, Violins I). Accent minus the loudest following staccato, simulated with the written envelope: Vc 337 -0.1 -> +2.4, Vc 342 -4.9 -> +2.2, Vla 349 -2.6 -> +1.4, Vla 354 -4.1 -> +1.6, Bn1 stac 349 -3.4 -> +2.0, Vln I 373 +0.1 -> +2.6 dB. This matches A's simulation exactly.
- **A #3 + B #1, basses pp cap:** 600 ms at pp (mix.json). It does not overlap B #1: the cap acts on release-trail length and B #1 on level, and A's old-pitch-re-body check is level-independent. In bars 6-7 both the old and the new note got the same +3 dB trim, so the tail between them stays consistent. Results are in Measured and Values 1. The delivered bars 1-174 take the 450 ms test audio (see Open).
- **C #2, coda basses pedal:** +3 dB downbeat / -1.5 dB off-beat shapes on 664-675. Downbeat pcX +58 -> +18 ms (off-beat -38 -> -42). C's inferred off-beat lead was not made.
- **C #3 / C #4 fills:**
  - Cello solo 688 as C proposed: pcX +69 -> +13 ms.
  - Clarinet 1 706: +2 dB, fitted (`cl706_48.py`). Level across the change against the C5 went -2.0 -> 0.0 dB. +3 dB reached C's +2 dB overshoot limit. pcX is unchanged (+99 ms), as expected for a level fill on an on-time crossover.
- **C #1 (a), per-note leads:** 112 rows (116 changed rows in three tables, 51 leg, 18 entry and 47 retongue, some re-routed; the other four are the 472.5 / 474.5 and 156 / 456 leads; Values 2). Every row was clamped to ±0.08 s.
  - 18 rows keyed to these notes (6 early fills, 6 seconds shapes, 2 qn shapes, 4 join notches) moved with them by the realised change (c43's rule; `near48.py`).
  - The basses' 332 sub. p notch and the body rows at Violins I 707 / Violins II 388 stay where they are.
  - Violins I 472.5 / 474.5 entry leads 0.075 / 0.065 (coordinator): pcX +68 / +70 -> +5 / +52 ms (references +28 / -6).
- **C #1 (b):** ENTRY_LEAD_S Horn 3 (0.06, 0.03, 0.03), Contrabassoon (0.04, 0.04). Horn 3 317 also through retongue_leads (-0.04 s; its 0.06 comes from another path).
- **C #1 (c), swell fills:** 29 LEVEL_SHAPES_S rows (`build/swell_fills48.json`, `swellfit48.py`). Selection: 90 swell notes in both renders. 22 are left to their lead changes, existing fills or aliases, 38 had no room before the next note or no body reference, and Violins I 88 / 536 are left alone (coordinator). Measured on c48: median t50 117 -> 33 ms after the reference, 0 -> 22 within 60 ms.
- **A #2, strokes:** celli 156 / 456 on Sus Marc LITE with retongue leads 0.02 / 0.05.
  - 456 passes A's criteria: time 6 dB under the body 364 -> 84 ms, 2-5 kHz front -10.9 dB, pcX +85 -> +2 ms.
  - 156: 222 -> 46 ms under, but pcX +32 -> +77. A pass-2 retry at 0.055 s gave 134 ms / +61. The main render was kept (see Open).
- **A #4 vs C #1 (coordinator):** I chose C #1's per-note table. A #4's +0.015 s family shift on Violins I / II / violas would move the same joins a second time (16 / 6 / 12 legato rows are in C's table). After C #1 the upper strings' robust SD fell 49 / 56 / 50 -> 40 / 36 / 47 ms.

## Rejected or deferred

- **A #2, Violas 372 on Sus Marc LITE at 0.04 s (pass-2 test "Vla stroke B"):** worse: 162 -> 338 ms under, pcX +88 -> +138 ms, no dip before it. It stays on Sus MAX.
- **A #4:** not made (see above).
- **C #2 off-beat lead (-0.03 s):** C inferred it and did not simulate it. Not made.
- **C #6 arrival onsets:** deferred, as C asked, until finding 1's transfer is confirmed (it is: see Measured).
- **A's optional pass-2 tests** (celli 342 / Violas 354 on Sus Marc LITE, fugato Spiccato RRx9) and **B's Felt Cresc alternative (MANUAL-GAPS #12):** not run; the level shapes met the targets.
- **C #1 rows that could not act:** celli 504 / 514-518.75 (the notes have no lead to remove), Horn 1 416 / 418 (moved the wrong way), Violas 428 / 434 / 153 / 76 / 436 / 595.5, Violins II 657, celli 265.5 / 266 (absorbed by the caps), Flute 1 296 / 299 / 299.5, Violins I 44 / 270.25 / 270.75 / 271 (no lead path), and the bar-152 run into 607 (Violas / celli 606.5-606.875).

## Open for c49

- **The basses' delivered audio is the 450 ms pp cap up to qn 695.8 and 600 ms after it; mix.json says 600 everywhere.** A rebuild plays 600 throughout. That differs only at the bars 1-174 pp chord changes (176 / 180 / 224 / 230 at -9.8..-11.7 dB re the new note, against -11.7..-15.4 at 450). Options: a coda-only alias at 600 with the main basses at 450, or accept 600.
- **Celli 156:** pcX +77 ms with Sus Marc LITE at 0.02 s. Fit its lead from these two renders (0.02 s -> +77 ms; 0.055 s -> +61 ms with more swell). The row's round robins vary.
- **Clarinet 1 706:** pcX +99 ms. A level fill cannot move a timbre-led reading, so check it by ear or with a crossover measure.
- **C #6:** the widest tutti arrival onsets (272, 464, 484, 488, 520, 584, 636, 664).
- **Basses 3 -> 4 and 17.95 -> 20, 182 -> 184 pp changes** read over -12 dB re the new note at every cap. The new note's band loses the shared harmonics (fourths and fifths), so the check is unreliable there.

## Measured

- **Master** (float sum of 40 stems): -17.4 LUFS, LRA 23.3 LU, true peak +2.6 dBFS, sample peak 1.347. c47: -17.3 / 23.4 / +2.5 / 1.339.
- **Delivered** `cycles/c48/mvt1-mockup-c48.mp3`: -19.8 LUFS, LRA 14.8 LU, TP -1.8 dBTP, p10-to-max span 19.0 dB, limiter about 0.6 dB. c47: -19.8 / 14.7 / -1.7 / 18.9 / 0.5.
- **Delivered S max:** 160 -11.4 > 122 -12.1 > 167-170 -13.5 > 26 -14.2. Climax order unchanged.
- **Attack probe:** 0 late or holes. **State check:** 0 runs against c47 on every track. Horn 1 against c46: 0 runs.
- **Basses pp chord changes** (old pitch at +0.35 s, re its body / re the new note; -12 / -12 to pass):
  - coda at 600 ms: 0 of 5 fail (no cap in c47: 3 failed);
  - bars 1-174: 350 ms (c47) 3, 600 ms 7, 450 ms (delivered) 4 fail.
- **Final release, to -10 / -20 / -30 dB:** basses 0.16 / 0.35 / 0.61 s (c47 no cap 0.22 / 0.63 / 0.81); master 0.19 / 0.53 / 0.82 s (c47 0.21 / 0.61 / 0.82). The master's -20 dB point is inside the references' 0.48-0.79 s.
- **Timing:** see Values 2 and 3.
- **REAPER memory:** main 24 GB at start, 44 GB settled (1 GB compressed), 45 GB (19 GB compressed) after the render. Pass 2 (10 instances): 15 / 28 / 29 GB.
