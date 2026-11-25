# Cycle 8 changes (actor)

Snapshot of the tools and build/*.json before this cycle: `cycles/c08/before/`.

## ONE_TIME.md (Opus PreloadSize 0): skipped

The c07 actor sent the PreloadSize change back to Dan with new evidence (the HDD preload uses more RAM, and the c06 lateness came from memory compression). Dan has not answered in the thread since, so, as the note at the top of ONE_TIME.md says, this cycle skipped it. PreloadSize is still 1 and the file stays.

## Render health

- All changes are data changes. `build_reaper.py --midi-only --tempo` (new `--tempo` flag: write the tempo map first, then recreate every track's MIDI item and envelopes on it) updated all 27 tracks without reloading a patch; no Opus state changed.
- Then the project was saved, REAPER quit and reopened (the session had 50 GB with 14 GB compressed before the restart).
- The reload after this morning's reset was slow: memory grew about 1 GB a minute from the external drive (30-70 MB/s), and settled at 49 GB after about 25 minutes. The first `render_cycle.py` run would have hit its 1500 s wait cap and rendered half-loaded patches, so it was stopped before rendering. `render_cycle.py` now waits up to 2700 s and refuses to render while memory is still growing (`--force` overrides).
- Other work on the Mac (a 5-6 GB Python job, Godot, Spotlight indexing, about 30 GB of file cache; load average 30) pushed macOS to compress REAPER's idle samples: 22 GB compressed when loading finished, 36 GB ten minutes later and still rising. Waiting or restarting would not have cleared it, so the render ran with `--force` at 49 GB / 36 GB compressed.
- Attack gate: **0 of 19 checks failed**, despite the compression (c06 failed 10 of 19 at 42 of 57 GB compressed). No clipping (true peak -4.0 dBFS, sample peak 0.631); all 27 stems and the master present.
- One render.

## Accepted

**A #1, early fills on sagging legato targets.** New `build/early_fills.json` {track: {onset: dB}}, read by `score_to_parts.py` into a new vol_db item `env` (a piecewise-linear dB shape): 0 at onset - 0.02 qn, +dB at onset + 0.05 s, held to + 0.35 s, 0 by + 0.6 s. Values as critic A proposed (sag - 2, cap 8): Fl1 8 notes, Ob1 8, CA 4, Cl1 1, Bn1 2, Hn1 5 (182 left out: it is an F4, covered below), Hn2 2.
- Horn F4: `pitch_trims.json` values may now be `{"early": dB, "body": dB}`; Horns 1-4 F4 = `{"early": 1, "body": -5}` (+1 dB to onset + 0.35 s, -5 by + 0.6 s).

**A #2, viola soft slur-to-slur joins.** `VLA_BC_SOFT`: on Violas, a slur-to-slur join whose target is shorter than 0.8 s at CC11 52 or less stays on Leg Slur MAX, still joined (overlap, legato lead, v124), with an 8 CC bow-change notch. 15 of 45 viola Leg BC notes moved to Leg Slur MAX. Other sections unchanged.

**A #3, pizz. pitch trims.** `pitch_trims.json` `"_arts": [...]` restricts a track's trims to those articulations (exclusively; critic A's condition would also have applied the pizz. F4 -8 to legato F4s, which were never measured hot). Violas Pizz RRx4 F4 -8, Gb4 -2, Gb3 +4, Bb3 +3; Violoncellos Pizzicato RRx4 Bb2 -5.

**A #4 / C #5, Vln I solo (bars 17-22): interim version.** `SOLO_NO_BOOST = ("Violins I",)`: the "solo" text gives no CC11 boost on Vln I (was +8 CC); CC1 is +10 over the span (`SOLO_VIB`, 105). roles.json Violins I [48, 65, -3]. The DIV A solo track was deferred again: it adds a 28th Opus instance, and this cycle's restart already started from a session at 50 GB with 14 GB compressed; one more variable on a render after the Mac's reset was not worth it.

**B #1, Flute 1 top octave.** `pitch_trims.json` Flute 1 84 -3, 89 -2, 90 -3, 91 -4, 92 -2, 93 -2, 94 -4 with `"_all_arts_pitches"` (these pitches on every articulation; 78 +4 stays legato-only). note_trims Fl1 262 -3 removed, 254 -8 -> -4.

**B #2.** Vc roles [238, 250] -3 -> 0; note trim Vc 238 -10 -> -6.

**B #3.** note_trims Clarinet 1 266 -5 (cancels the A flat 5 +5 pitch trim on this ff note).

**B #4, harp harmonics.** The harmonics track reads the dynamics of both harp staves (`dyn_staves`), and its velocity is 6 under the harp's (`HARM_VEL_CUT`): v76 -> v58.

**B #5.** Pitch trims on notes longer than 4 qn end at onset + 3 qn (the coda Cb A flat 1 pedals at 271 and 292 keep only the attack cut).

**B #6.** Violas roles [42, 48, -3] and [140, 146, -4] under the oboe entries.

**C #1, crescendo arrivals.** `hpgain` is now held to the first onset after the arrival note (cap 4 qn; `HP_HOLD_CAP`), then released over HP_REL = 1 qn as before. Where no note lands on the arrival, the old rule (release at the next onset, at most 2 qn after the hairpin end) is kept. Tenuto arrivals at f or louder inside `SOSTENUTO_SPANS` keep their tenuto bump at 4 CC to the note end (`holds`), so Vln I qn 204 holds CC11 119-122 instead of falling to 114.

**C #2, crescendo goals (fallback).** note_trims Vln I 80 +3 / 82 +2, Vln II 80 +3, Ob1 57 +4 / 148 +5, Fl1 129 / 129.5 +3. `VEL_SET` Oboe 1 qn 148 velocity 100 (the same-pitch Sus MAX re-attack was v73). (a), (b), (d) as code were not done.

**C #3, breaths.** `CAESURA` adds the solo breath marks 29 (0.12 s), 124 (0.12), 164 (0.10), 286 (0.10) and phrase seams 42 (0.08), 48 (0.10), 66 (0.10), 140 (0.08), 171 (0.10), 237 (0.10): about 1 s in all. Tempo map 303 -> 323 points.

**C #4, coda.** `CODA_SOFT`: from qn 280, soft (CC11 40 or less) string legato targets take velocity 90, not 124 (Vc 292, Vla 289/292). roles Vc [292, 304, -4], Vln I [292, 304, -3], Vla [289, 304, -2].

**C #6, low-mid weight.** mix.json Violoncellos dyn_trim_db f -3 -> -2, ff -4.5 -> -2.5; roles Vc [250, 262] -5 -> -3.

## Rejected or deferred

- A #1.3 (flute legato velocity test): needs a range render; deferred.
- A #4 full fix (DIV A solo violin track): deferred (memory; see above).
- C #2 (a), (b), (d) as general rules: the per-note fallback was used instead; the general rules touch every hairpin and want their own cycle.
- C #3 optional cadence-bar slowing (3% on bars 14, 22, 30): not done.

## Measured (plain RMS dB from the stems, each render on its own tempo map; script `/private/tmp/claude-501/mockup-loop/c08-actor/chk.py`)

Mix: **-23.9 LUFS integrated, LRA 23.6 LU, true peak -4.0 dBFS** (c07 -25.3 / 23.7 / -5.4). The loudness rise is mostly bar 61 (-20.3 -> -17.9 dB): the held hpgain and tenuto hold at the climax.

| Check | c07 | c08 | Target |
|---|---|---|---|
| A #1 body minus early, Fl1 111 / 118 / 132 | 9.8 / 8.3 / 9.0 | 3.3 / 3.6 / 2.9 | < 5 |
| A #1 Ob1 56 / 140, CA 136 | 8.6 / 8.0 / 6.7 | 3.3 / 2.4 / 2.0 | < 5 |
| A #1 Hn1 176 / Hn2 258 | 7.1 / 7.8 | 2.9 / 3.4 | < 5 |
| A #1 Hn1 F4 195 / 201 | 9.8 / 12.1 | 6.6 / 7.7 | < 5 (not met) |
| A #2 the 15 moved viola joins, median dip | 10.2 | 6.2 | <= 6 (241, 244, 245.5 still 10-12) |
| A #3 Vla pizz. F4 first 0.12 s (124.67 / 128.67) | -38.9 / -37.8 | -43.2 / -42.0 | about -49 median |
| B #1 Fl1 minus Vln I, beats 193 / 194 / 195 | +2.8 / +1.1 / +3.3 | -1.3 / -1.7 / +0.1 | -2 to -4 |
| B #1 same at 262 / 268 | +0.4 / +4.7 | -1.7 / +1.0 | -2 to -4 |
| B #2 Vc minus Vln II, bars 71-74 | -6.1 / -4.5 / -5.0 / -4.9 | -0.7 / -1.5 / -2.0 / -1.9 | within 2 |
| B #3 Cl1 minus Ob1, qn 266-268; Vln I minus Cl1 | +3.6; +3.1 | -0.4; +7.1 | within 2; >= 5 |
| B #4 harp harmonics qn 273-277 | -47.7 | **-57.7** | -47 to -50 (overshot) |
| B #5 Cb minus Vc, qn 274-286 / 292-304 | -4.6 / -3.5 | +0.4 / **+4.5** | -3 to +1 (292-304 overshot, with the C #4 Vc cut) |
| B #6 Ob1 minus Vla, beats 43 / 44 / 141 / 142 / 143 | -3.7 / +3.6 / +2.7 / -2.8 / -3.2 | -0.7 / +6.6 / +6.7 / +1.3 / +2.3 | >= 3 (43 and 142 not met) |
| C #1 fall over the arrival note: Vln I 204 / Fl1 204 / Vla 204 / Vln II 196 / Vc 259 | 4.0 / 5.3 / 4.0 / 6.0 / 4.7 | 0.9 / 2.8 / 1.4 / 3.6 / 2.3 | <= 1.5 |
| C #2 goal minus beat before: Vln I 80 / Ob1 148 / Ob1 57; Vln I 82 minus 78 | -5.0 / -5.0 / -3.8; +0.3 | -2.7 / -1.5 / -2.4; +2.0 | >= 0; >= 3 |
| C #4 master bars 88 / 89 / 90 / 91 / 92 | -45.4 / -41.7 / -42.1 / -44.5 / -48.4 | -45.7 / -43.3 / -42.6 / -45.3 / -49.5 | 89-92 at or under 88 (not met) |
| C #5 Vln I bars 17-18 minus Ob1 bars 19-20 | +5.6 | -1.9 | within 1.5 |
| C #6 loud-frame master 125 / 250 Hz (re 1 kHz) | -10.3 / -6.1 | -10.4 / -6.3 | +2 dB (no effect) |
| C #6 Vln I minus Vc, qn 204-212 / 262-268 | +5.8 / +5.5 | +4.6 / +4.4 | >= 3 |

## Open for the next cycle

- Harmonics too soft now: play them at about v72 (B #4's premise held at v76 = -47.7; v58 measured -57.7, about 0.55 dB per velocity step).
- Cb over Vc by 4.5 dB in bars 89-92: ease the Vc [292, 304, -4] role or add Cb [292, 304, -3].
- Horn F4 still sags 6.6-7.7 dB: raise the F4 `early` from +1 to about +4.
- Coda bar 89 still 2.4 dB over bar 88; bar 89's Vln I entry at qn 292 is the next suspect.
- C #6: the cello trims did not move the loud-frame low-mid bands; the deficit is in voicing or in the Cb/timpani octave.
- Viola joins at 241, 244, 245.5 still dip 10-12 dB; Oboe over violas at beats 43 and 142 still short of +3.
