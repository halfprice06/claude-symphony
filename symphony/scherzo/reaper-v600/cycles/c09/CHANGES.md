# Cycle 09: changes (actor, on the c08 render)

Snapshot in `before/`. Scripts in `actor_scripts/`: `apply09.py` (roles, note trims, pitch trims, entry leads, early
fills), `mix09.py` (mix.json sends; run after `mix08.py` when regenerating mix.json), `retsim09.py` (return-send
simulator, the c07 method, kept this time), `check09.py N` (the c09 checks; `check_c08.txt` / `check_c09.txt`). The
Violas state experiment is in `exp/`. The data that rendered is in `build_render/` (before the Flute 2 stem fix).

STATUS: rendered 2026-11-09 10:38-10:45, checked, one stem fix. Lock held 10:20:25-10:59:19 (38.9 min, including a
5 min one-track experiment render). mp3: `cycles/c09/scherzo-mockup-c09.mp3`.

## 1. Violas legato state (orchestrator item; critics A #3, B #1, C #5): cause found

Diff of the Violas Opus state saved in the .rpp after the c08 render against the state build_reaper writes
(`jobs/25_Violas_KS_Master.b64`), decoded JSON leaves (`exp/violas_saved_c08.json.gz` keeps the saved state):

| leaf (count) | written by build_reaper | saved after a render |
|---|---|---|
| AHDSR `attack` of the legato sustain groups "V1s pp..ff" (52) | 841-1501 ms | 20 ms |
| EWSO filter `legato_speed_active` (1) | true | false |
| `Controller 1` processor `value` (833) | 127 | 0 |
| start-mode `default` of CC11 groups (about 140) and CC1 groups (8) | 127 | 11 / 38 / 41 / 124, 47 |
| `sampleMarked` (2440), layer pan/volume defaults (105), labels, tempo 120 -> 60, tsNumerator 4 -> 3 | | |

The same categories differ on every instance that has played (Violins I, rebuilt in c08, too), so the Violas instance
of c08 loaded all of them from the state saved after the c07 render, while Violins I loaded the written state.

Experiment (after the main render, same project, `exp/`): the written Violas state with only the 52 AHDSR attacks set to
the saved 20 ms (`make_exp_state.py`, `exp_set.lua`), one-track render (`exp_render.lua`, 5 min), pcX
(`exp_analyze.py`):

| Violas | joins v112+ pcX / window | v96-111 | v0-95 | all: window median, robust SD | stem 133-162 / 579-615 |
|---|---|---|---|---|---|
| c08 (saved state, MIDI-only) | -86 ms / 122 | +14 / 90 | +13 / 103 | 115 ms, 93 ms (SPREAD) | -35.1 / -38.6 dB |
| c09 experiment (attacks 20 ms only) | -83 / 122 | +14 / 90 | +13 / 94 | 114, 82 | -35.1 / -38.6 |
| c09 render (written state, full build) | -3 / 88 | +21 / 76 | +13 / 108 | 91, 78 (ok) | -36.7 / -39.9 |

The 52 attack values alone reproduce the c08 flip exactly: the saved 20 ms attack of the legato sustain groups (Opus
writes the attack its legato script last set) makes loud joins arrive about 0.08 s early and the legato passages
1.3-1.6 dB louder. Violas was then rebuilt again from the written state before the save.

Changes:
- Full rebuild of all 31 tracks this cycle (no `--midi-only`).
- `tools/build_reaper.py`: `LEGATO_MONO_CC22 = 127` sends CC22 127 in the pre-roll on every track that plays a "Leg"
  row (20 tracks; every legato KS Master maps controller_22 "True Legato: Mono", read from the states). Mono is the
  default, so this only pins it; the cause was the attack values. `MIDI_ONLY_REBUILD_LEGATO = True`: `--midi-only`
  fully rebuilds every track with a "Leg" row (its state reloads from jobs/NN_*.b64).
- C #5 (SHORT_CC11_PARK un-park step) not changed: the attack experiment explains the flip with the parked data unchanged.

## 2. Critics' findings

| finding | status | change | measured (c08 -> c09, plain RMS dB, check09.py) |
|---|---|---|---|
| A #1 head tails | adopted | new generic `SHORT_SUS_LEG_AT` (listed slurred short notes stay Leg Slur MAX targets) plus a join from a Sus / Marc head (overlap, leg_target, legato lead): Violins I 18 tail onsets | tails vs half-note body: 69 -16.2/-13.3 -> -7.6/-5.5, 789 -13.6/-11.2 -> -6.0/-3.2; all 18 within 8 dB; vs the next quarter 7 of 9 heads within 6 dB (51 -11.1, 75 -9.8 still under) |
| A #2 celli fills | adopted | `auto_fills.py 8 --write` (26 new incl. 17 celli, 3 raised, 1 retimed, 2 removed, 2 lowered, 2 held). c04 recorded no reason for dropping its celli fills | celli join dips 542 11.1 -> 5.1, 576 10.5 -> 5.3; 645 4.9 -> 7.6 (my 30 ms measure; check on the next pass) |
| A #3 violas | adopted | section 1 | probe ok |
| A #4 soft entries | adopted, **failed** | celli 504 entry lead 0.12 + early fill 4 dB; basses 504 / 1071 lead 0.06 and v53 | pcX celli 504 +285 -> +367 ms, basses +146 / +144 -> +166 / +164: worse. Revert in c10 (lead plus fill does not move a slow p attack here) |
| A #5 celli spikes | adopted | `JOIN_NOTCH` celli 763.05-763.55 -4, 799.05-799.6 -4.5 | master pair dips 763.5 / 799.5: 2.5 / 1.6 -> 4.7 / 4.4 |
| A #6 Horn 1 breath | adopted | `NOTE_END_AT` Horn 1 646 -> 647.35 (gap 88 ms) | stem dip at 648 2.5 -> 7.5 dB |
| B #1 rebuild | adopted | section 1 | |
| B #2 flute f staccato | adopted (+5, not +6) | roles Flute 1 +5, Flute 2 +5, cor anglais +4 on the f staccato windows (+6 simulated level with the oboe in plain RMS) | unison f stac Ob1 - Fl1 +6.2 -> +1.2 dB; bar 41 Fl1 -46.8 -> -41.8 (V1 -33.6) |
| B #3 violas tutti | adopted | roles +4 over 312.5-360, 912.5-960 | Violas -38.0 -> -34.0 (celli -30.9, V1 -27.8) |
| B #4 Clarinet 2 | adopted, deeper | note trims 588 -9 (B: -6; simulated level with Cl1), 600 -2, 603 / 606 -4, as steps; pitch-trim skip 600 | Cl2 588-594 -34.0 -> -42.2 (Cl1 -39.2); 600-608 -37.8 -> -42.2 (violas -46.2) |
| B #5 celli 111 / 114 | adopted | note trims -3 / -8 as steps (`NOTE_TRIM_RAMP_S` 0.02; the 0.6 s default ramp reached only 0.2-0.7 dB) | 111 / 114: -33.8 / -28.0 -> -36.8 / -35.8 (117 -37.7) |
| B #6 Flute 2 high notes | adopted, halved by stem fix | pitch trims 87-93 (`_all_arts`); B's values gave Fl2 - Fl1 -2.8 dB, halved | Fl2 - Fl1 +2.6 -> -1.6 dB after the stem fix |
| C #1a wind send | adopted (simulated) | wind group `send_offset_db` R Winds +3 | |
| C #1b wind Main mics | deferred | inferred, changes tone; needs a stem test | |
| C #2 brass / bassoon sends | adopted (simulated) | trumpets R Brass offset 0, trombones / tuba -11.77, bassoons R Winds -11.36 (+3) | |
| C #3 DIV sends | adopted (simulated) | solo R Strings +3.6, Violas div +4.0 | |
| C #4 harp harmonics hall | adopted (simulated) | Harp harmonics to R Strings -8.77, R Perc off | see soft ends below |
| soft string end 0.31 s | fixed | `LEVEL_SHAPES` Violins I 1127.75-1128 0 -> -6 dB (the end is the dry ppp sample's own fall; `NOTE_END_AT` would have moved the fitted re-bows) | 0.31 -> 0.14 s |

Return simulation (`retsim09.py`, fit residuals -21..-28 dB) for C #1a-#4 together, against the render:

| | G.P. 1016 drop +0.3/+0.6/+1.0 s, t20, RT60 | final chord 1128, RT60 | returns re dry |
|---|---|---|---|
| c08 rendered | 21.1 / 32.1 / 46.9, 0.30, 1.30 | 21.4 / 32.8 / 41.7, 1.28 | -12.94 dB |
| simulated | 20.6 / 31.3 / 40.2, 0.30, 1.34 | 21.4 / 32.2 / 41.4, 1.28 | -11.73 |
| c09 rendered | 20.5 / 31.4 / 46.6, 0.30, 1.34 | 20.2 / 31.5 / 40.4, 1.42 | -11.64 |

Soft ends (stem + R Strings, -10 dB): V1 23.0 0.13, V1 1128 0.14, solo 1066.8 0.16 s. The Violins II harmonic end at
444.5 reads 0.71 s (c08 0.29) because the harp harmonics now ring in R Strings from 445 (C #4): the simulation without
the harp's share of R Strings gives 0.29 s, so the strings' own end is unchanged and the 0.71 is the handover, not a
wetter string end.

## 3. Orchestrator notes received during the cycle

- Movement I c51 lessons (mockup-kit README): item 1 (brass bells) already in our mix; item 2 (winds' phrase-shape
  offsets x1.4) not adopted: our PHRASE_SHAPE has no per-family scale and the critics balanced the winds per bar this
  cycle; items 3-5 used as checks (inner held notes: Horns 3-4 under Clarinet 1 at 456-504 -53.5 / -50.2, unchanged
  from c08 to 0.0 dB). All carried into `loop/ONE_TIME.md` for c10.
- Finale SHARED-TECHNIQUES (arrived after the render): item 2 checked, our `FP_SPIKE_FROM_ONSET` is not overwritten by
  the bar-301 crescendo (sf values at the moved note-on in parts.json); item 9 does not apply (harp velocity at most 56);
  items 1, 3-8, 10-12 not adopted this cycle (the render was done) and written into `loop/ONE_TIME.md` for c10.

## 4. Not done

- MANUAL-GAPS: no gap tried (the state investigation took the room); #6 hard sticks remains the next candidate.
- Disk rule: deleting cycles/c08's non-master WAVs and render_first was refused by the session's permission
  classifier, so they are still there (2.9 GB); the orchestrator or Dan should delete them. Disk had 25 GB free at the
  render (other threads' files), under the 30 GB rule; 55 GB free at the end.

## Research items

| item | status |
|---|---|
| EW template mix (c06), returns and sends (c07), c08 EQ set | adopted, unchanged |
| register sends (no hall send from low brass, bassoons) | partly rejected with numbers (critic C #2, simulated): trombones / tuba and bassoons back in the hall 3 dB under their families (180 Hz return high-pass); G.P. +0.3 s 21.1 -> 20.5 dB, 250-500 Hz share unchanged within 0.04 dB (C). Contrabassoon and basses stay dry |
| woodwind Close as the main mic | kept (C #1b deferred); the wind send raised 3 dB instead |
| batch 6 #3 shared curves, CC11 -> CC1 pass 2, separate legato tracks | pending (memory / pass 2) |
| finale techniques (SHARED-TECHNIQUES) | pending, `loop/ONE_TIME.md` |

## Render

Steps: lock (no waiter; mvt2 c47 queued only later), start, open (Opus log clean: 0 "Interrupted system call"),
full build of 31 tracks plus returns (73 s, all states set), restart (reopen 2.5 min), 45 GB settled by 10:37 with
28 GB compressed (other processes held the rest), audio_init (48000 / 512, no input), `render_cycle.py 9
--force-memory` (7 min). Stem fix: Flute 2 pitch trims halved (`stem_fix.py 9 build_render build "Flute 2"
--apply`, originals in `render_first/`), `--mix-only` written to REAPER, `render_cycle.py 9 --measure-only`. Then
the experiment (section 1) and the Violas rebuild, quit, unlock.

Memory: 45 GB settled (28 GB compressed) before the render, 46 GB (28 compressed) after it, 47 / 27 after the
experiment.

Master -20.8 LUFS, LRA 23.2 LU, true peak -1.6 dBFS (sample peak 0.828). Delivered -19.8 LUFS, LRA 14.7 LU, TP -1.5
dBTP, limiter about 2.7 dB, span 19.6 dB (c08: -19.8 / 14.9 / -1.6 / 2.6 / 19.6). Band shares 2-6 kHz -9.56, 6-20 kHz
-28.81 dB (c08 -9.5 / -28.9). Attack probe: all ok, no late or hole; legato windows / robust SD Violins I 66 / 44,
Violins II 81 / 44, Violas 91 / 78 (limit 90 on the SD; c08 SPREAD 93), celli 66 / 53 ms. Unchanged tracks render
the same to 0.0 dB (Horns 3-4, Clarinet 1, Horn 1 close).
