# Critic B, cycle 41 (render c40): balance and levels

## Manual notes (May 2021 HO manual, PDF pages 32-34, 43, 46, 191-192; MANUAL-GAPS.md and DIGEST.md read)

| Page | What the manual says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| p.32 | Default preload size: HDD keeps the most of each sample in RAM, SSD (SATA) less, SSD (PCIe) least; "Never Preload" streams everything and needs RAID 0 PCIe drives. | The samples stream from a USB desktop hard drive; Opus `Preferences.json` has `PreloadSize: 1` (SSD SATA), `NeverPreload: false` (read). | Partly. The manual's setting for this drive is HDD, but KIT section 11 keeps 1 on purpose (memory), and the c40 attack probe found 0 late entries in both passes (measured). No change. |
| p.33 | Multi-threaded reverb and voice renderer, voice-render threads; plugin stereo outputs 1-16. | `UseMultiThreadedReverb` false, `RenderMultiThreaded2` false, 1 voice-render thread, 9 plugin outputs (read). | Consistent. The render is offline at 1x, and every stem is a separate track, so outputs do not matter. |
| p.33-34 | Audio-drive types: slower drives need more RAM. A 7200 rpm USB 3.0 drive is the minimum. | The same drive. | Nothing to change. The render gate waits for three quiet RSS readings before it renders. |
| p.34 (picture) | Round Robin: Reset Controller is a CC number set in Preferences (16 in the manual's own screenshot), and Reset Note is optional. | Preferences hold `RoundRobinResetCC: 16`, `RoundRobinResetNote: -1` (read). `build_reaper.py` sends CC36 = 127 at `RR_RESET_QN` (patches map CC36 to "Repetition: Reset RR") and never sends CC16 (read). | No. MANUAL-GAPS #6 is still open. Repeatability on unchanged data, measured c39 against c40 with every frame within 1 qn of a volume-envelope change masked out: 25 of 31 unchanged stems have 94-100% of 20 ms frames within 0.5 dB. Seven notes moved by more than 3 dB with identical MIDI: Horn 3 164 +6.4 K (+6.9 A), Violins II 160 +4.1 / 262 +3.7 / 119.5 -3.6, Bass clarinet 429.5 +4.3, Bassoon 1 523 -3.5, Flute 1 109.5 +3.5. Finding 6. |
| p.34 | Program change to articulation (optional). | Off in Preferences; keyswitches only. | Consistent. |
| p.43 | Purge: a purged instrument loads samples as notes play (yellow state) and is green only when fully loaded. | The render must start with every instance green. `render_cycle.py` waits for REAPER's RSS to settle. | The audio follows it (probe 0). The record does not: `metrics/memory.txt` says "before render: REAPER 23G", while `top_before_render.txt` and CHANGES say 45 GB settled. `render_cycle.py` writes the `top` reading it takes before the settle wait (lines 41-42 and 198 of the render-time copy). Fix: call `cmprs_gb()` again after the wait loop and write that value as "before render". |
| p.46 | System usage: voices, CPU, RAM, disk. | GUI only. | Not applicable. The pipeline reads memory with `top` and `footprint`. |
| p.191 | All Instances window: purge state and articulation selector per instance. | GUI only. | Not applicable. Rows the pipeline does not use are unloaded by `UNLOAD_UNUSED_ROWS`. |
| p.192 | Voice limit per instrument: when it is too low, voices drop; one note uses one voice per mic and per layer. | The patches ship limits of 250 (winds, brass, timpani) and 350 (strings) (DIGEST 2.3); `InstrumentVoiceLimitMax` is 1024 (read). | No drops are likely (inferred). The densest string chords are 4 notes on 2 mics with crossfaded layers and release tails, which is far under 350. The silent-note check lists only its two known false alarms (Trombone 1 552, Timpani 727). |
| p.192 | Octave and key range per instrument. | Not used. | Consistent (no transposition). |
| DIGEST 3 / MANUAL-GAPS #6-#7 | Engine settings table; CC16 reset; half-section divisi for soft div. passages. | As above; divisi: the violas' bars 47-60 div. pp chords sit 12-18 dB K under the cello tune (measured), with no balance problem. | #6 open (finding 6); #7 not needed for balance. |

## Method

- Render analysed: `cycles/c40/render`, all 38 stems.
- Data: `cycles/c40/rendered_build/` (parts.json, roles.json, score_config.py, mix.json).
- Comparison: c39 with its rendered_build. The tempo maps are identical.
- Analysis frames: 4096-point FFT, 20 ms hop, stereo power, with A- and K-weighting and six bands computed per frame.
- "re M" means stem minus master over the same window.
- Printed dynamics come from each track's `dyn_curve`.
- Simulations scale stem or master frame powers by the proposed envelope change (`_all` rows act on every non-percussion track).
- Score pages read: 2, 4-9, 11-18.
- Every judgement below is marked measured or inferred.

## The coordinator's checks (c40 changes)

- **Cello solo (stem 38), 680-696.**
  - **Level.** The solo is the master in bars 171-174: -0.2..-3.1 A re M per beat. The pp accompaniment (violas, Bassoon 2) sits 13-23 dB under it, and the bar-174 pp roll 13.5-17.4 dB K under the master (measured).
  - **Against the cor anglais.** The solo's margin over the p espr. cor anglais fell: per half-beat median +3.8 → +2.7 dB A (K +5.3 → +5.2), and 11 of 20 half-beats are under 3 dB (measured). Finding 4.
  - **Timbre.** The DIV A is a little darker than the section it replaced: 2-5 kHz share -1.1 dB and 5-20 kHz share -1.8 dB at the same broadband level (measured).
- **Brass lift kept at the tutti chords (bars 26, 32, 72, 143).**
  - **Where the lift was removed.** The master fell 0.4-0.8 dB A over bars 27-31, 69-71 and 131-142, as planned (measured).
  - **Recap theme.** Trombone 1 (a2, f) minus the ff cellos, per 2 qn in bars 131-134: c39 +5.3 / +4.9 / +2.0 / +0.6 / +2.4 / +4.6 / +5.1 / -0.9 → c40 +3.3 / +3.4 / +0.4 / -0.8 / +0.3 / +2.6 / +2.4 / -3.3 (measured).
  - **Inversions** (a softer-printed track more than 3 dB K over a louder-printed one on steady beats): fewer and smaller (measured). Trombone 1 over Flute 2: 17 beats at median +6.4 → 14 at +5.3. Tuba over Flute 2: 19 → 9. Tuba over Bassoon 1: 13 at +6.1 → 10 at +6.5.
  - **Bar 72.** The trombones lead the f chord by about 3 dB over the Violins I top line (A). That is what RK's forte ratio gives (one trombone ≈ two string sections), so I leave it.
- **Trumpet 2 roles.** Trumpet 2 minus Trumpet 1 on co-sounding beats (A, measured):
  - bars 27-31: c39 -0.2 / -0.9 / +1.3 / -2.6 / +1.5 → c40 -2.2 / -2.9 / -0.7 / -4.6 / -0.5;
  - bars 69-72: c39 +0.1 / +0.3 / +0.8 / +1.4 → c40 -1.9 / -1.7 / -1.2 / -0.5.
  - Bar 32 is +2.8, on two short accented ff chords. That is not worth a change.
- **Fugato staccato levels.** Per-note 0.2 s peaks, wind minus the string section it doubles (A, measured):
  - Bassoon 1 stac: -10.5..+7.8 → -3.5..+4.6.
  - Flute 1 stac: median -7.7 → -4.2 (RK -3). Its last two notes are -8.1 / -10.8, under the Violins I's ff crescendo.
  - Cor anglais stac is unchanged at -7.8..+6.0. Finding 5.
- **fff arrivals at 122 and 160.** The steps are there: master K +3.7 dB into 160 and +3.0 into 122 (measured). But the crescendos now stall on their last beat. Finding 3.
- **Long timpani rolls (Dan's standing note): no roll drowns anything (measured).** In both A and K, no long roll is the loudest stem. Ranks among 38 stems (A / K):

  | roll | rank (A / K) | K re M |
  |---|---|---|
  | opening ppp | 4 / 4 | -9.7 |
  | bar 41 ff | 21 / 10 | |
  | bars 117-121 | 19 / 18 | |
  | bars 124-125 ff > mf | 10 / 4 | -10.7 |
  | bars 126-130 under the clarinet solo | 7 / 5 | 9-14 dB under the solo |
  | bar 144 mp | 9 / 7 | |
  | bars 166-169 | 21 / 9 | |
  | bar 174 pp | 6 / 3 | -16.4 |
  | final ppp | 9 / 7 | |

  The rolls lead only the 100-250 Hz band, at bars 62, 124-125 and 158-159 and under the bar-174 solo. There they double the bass pedal. Keep them as they are.
- **New trumpet and percussion tracks against the rest (measured).**
  - Trumpets a2 minus Trumpet 3, same f rhythm in bars 131-132: +3.1..+5.3 dB A. RK gives two trumpets +3.
  - Trumpets a2 minus Horns a2 in the ff coda theme: +0.6..+2.7 K in bars 167-168 and +5.1 at 169.1.
  - The tam-tam fff is the loudest stem in bars 122-123 (-6.6..-7.1 A re M), as printed (heavy beater).
  - The pp tam-tam at 175 sits at -14.8 K / -19.8 A re M.
  - The sus.-cymbal stroke and the K Crash ring sit at -15.7..-29.6 A re M from 636.5 and cover nothing.
- **Does p sound like p in every family (measured, K).** On beats where at least four tracks share one steady printed dynamic, each track's deviation from that beat's median:
  - At pp/p the families lie within ±3 dB, except the melodic roles (Clarinet 1 coda solo +7.4, Violins I +6.3) and Horn 4 at -2.8.
  - At f/ff the winds sit at -4.4..+0.8 (Flute 2 and Contrabassoon the lowest, as their register gives) and the brass at -1.6..+3.4.
  - Same-pitch steps per printed level: winds 3.4-8.1 dB from f to ff, brass 5.3-8.9, strings 1.8-4.7.
  - None of this is a mapping fault that needs a change. The remaining issues are local and role-based, and they are listed below.

## 1. The cor anglais's p dolce answers stand level with or over the recap tune they answer (bars 148-152) (measured)

**Where.** Cor anglais, qn 586.5-590, 594.5-598 and 602.4-606 (bars 147.3-148, 149.3-150, 151.3-152).

**The score (p.15).** The tune is in the violas and cellos (mf dolce, swelling toward f) with Horn 1 (mp). The cor anglais answers it, marked p dolce with small < > swells.

**Evidence.**
- The answers are lifted three ways:
  - The swells read as untargeted hairpins: CC from 46 (p) up to 68 (mf) and back.
  - The volume envelope reaches +6.5 dB at each swell top: the c04 role `["Cor anglais", [586, 605, 4, 0.5]]` (c04 B #3, set when the answers were 2.6 dB under a pp Violins II tremolo) plus the soft-hairpin ramp.
  - The Violins II tremolo now sits 13-17 dB A under the master, so the role's reason has gone (LEARNINGS 13: old cuts and lifts go stale).
- Per beat, A re M, at the swell tops:

  | qn | cor anglais | celli | violas | Horn 1 |
  |---|---|---|---|---|
  | 594 | -6.6 | -5.9 | -5.4 | |
  | 595 | -5.7 | -5.9 | -4.7 | |
  | 603 | -5.0 | -6.7 | -9.2 | -5.7 |
  | 604 | -4.2 | -5.8 | -8.6 | -8.2 |

- In A, the cor anglais is the loudest voice at 603-604.
- In K it is level with the celli (-6.5 / -6.0 against -6.3 / -4.7) and 3.4-3.7 dB over the violas.
- RK at piano: one wind equals one string section. A p answer should therefore sit about 3-5 dB under the mf/f tune it answers.
- The first answer (586-590) is fine: 4.5 dB under Horn 1, which leads there.

**Fix.** In `build/roles.json`, end the c04 lift after the second answer: `["Cor anglais", [586, 605, 4, 0.5]]` → `["Cor anglais", [586, 598.5, 4, 0.5]]`.
- The cor anglais rests from 598.1 to 602.4, so the change acts only on the third answer (-4 dB).
- Simulated, cor anglais minus the loudest tune voice at 603 / 604: A +0.7 / +1.6 → -3.3 / -2.4; K -3.0 / -1.3 → -7.0 / -5.3.
- If the second answer (594-596, -1.0..-1.6 A, -3.9..-7.2 K) still reads as too forward on the next render, its part of the row can go from 4 to 3.
- Level only, so it can go in by stem fix.

## 2. Horn 1's mp espr. answer in bar 125 is covered by the violins' and oboe's C5, which swells against its printed decrescendo (measured)

**Where.** qn 498-500.
- Horn 1 holds C4 (498.0, 3 qn, mp espr., Leg Slur MAX).
- Violins I hold C5 (497.72-499.68, Leg Slur MAX) and Oboe 1 holds C5 (497.78-499.88). Both are printed mf > p into bar 126.

**Evidence.**
- Violins I, A per half-beat: 25.3 at 496.0, 22.1 at 497.0, then 24.3 / 26.3 at 498.5 / 499.0. In quarter beats the C5 swells from 20.7 at 498.25 to 27.0 at 499.0, which is +6.3 dB inside the decrescendo.
- The printed mf > p (CC 72 → 46, 26 CC at the measured 0.23-0.25 dB per CC) asks for a fall of about 6 dB.
- Meanwhile Horn 1's C4 sags from 25.5 at 498.75 to 20.2 at 499.25.
- Horn 1 minus Violins I per half-beat, 498.0 / 498.5 / 499.0 / 499.5: A -0.8 / +0.6 / -4.1 / -1.4; K +1.8 / +1.3 / -3.6 / -0.8.
- Horn 1 minus Oboe 1 at 499.0 / 499.5: +0.6 / -1.3 A. Oboe 1's join fill (+3.8 dB at 498) lifts its C5 just as the horn enters.
- c33 B #4 gave Horn 1 +2 here (`[496.5, 501, 2, 0.5]`). The violins' swell, measured at the same values in c39, undoes it.

**Fix (level only), in `build/score_config.py`:**
- `LEVEL_SHAPES["Violins I"] += [[(498.25, 0.0), (498.75, -3.0), (499.0, -5.0), (499.5, -5.0), (499.6, 0.0)]]`. This is back to 0 before the 499.63 transition into the p D5.
- `LEVEL_SHAPES["Oboe 1"] += [[(498.6, 0.0), (499.0, -3.0), (499.8, -3.0), (499.9, 0.0)]]`. This acts after the join fill's 0.23 s hold.
- `LEVEL_SHAPES["Horn 1"] += [[(498.9, 0.0), (499.25, 3.0), (500.0, 3.0), (500.75, 0.0)]]`. This holds the sagging C4 into its own printed > p at 500-501.
- Expected Horn 1 minus Violins I at 499.0 / 499.25 / 499.5: A about +3 / +3 / +7 (inferred from the stem powers).

## 3. The c40 hold-back makes the crescendos into the fff downbeats stall on their last beat (measured)

**Where.** Bar 159 (the ff < fff crescendo in every part, with the sus. cymbal pp < fff) and the last beat of bar 121 (allargando, < fff). The cause is the `_all` rows of c40 C #1 added to the older rows.

**Evidence: master K per beat, and steps.**

| | beats | c39 | c40 |
|---|---|---|---|
| bar 159 into 636 | 633 → 634 → 635 → 636 | +1.5 / +1.8 / +0.7 | +0.8 / +0.6 / +3.6 |
| bar 121 into 484 | 482 → 483 → 484 | +0.2 / +1.5 | -0.7 / +3.0 |

- In the delivered mp3 (RMS per beat):
  - bar 159: -18.8 / -18.2 / -18.0 then -14.1 at 636 (c39 -18.8 / -17.6 / -16.1 / -15.2);
  - bar 121: -17.7 / -18.4 then -15.0.
- So the crescendo stops growing for a beat and a half and then jumps. Into 122 the last beat even falls.
- The two rows work against each other:
  - The bar-158 row `[(627.875, 0.0), (628.375, -2.0), (632.0, -2.0), (635.375, 0.0)]` rises toward 0 while C #1's `[(634.0, 0.0), (635.0, -1.5), (635.9, -2.5), (636.0, 0.0)]` falls.
  - Into 122, the old `[(467.0, 0.0), (468.5, 0.8), (482.0, 0.8), (483.5, 0.0)]` already ramps out over 482-483.5 under C #1's -2. The low brass's printed eighth rest before 122 lowers beat 4 as well.

**Fix: `LEVEL_SHAPES["_all"]` in `build/score_config.py` (level only).**
- **Bar 160.**
  - Replace the bar-158 row with `[(627.875, 0.0), (628.375, -2.0), (632.0, -2.0), (635.9, -1.2), (636.0, 0.0)]`.
  - Delete `[(634.0, 0.0), (635.0, -1.5), (635.9, -2.5), (636.0, 0.0)]`.
  - Keep the 636 arrival lift.
  - Simulated: steps +1.0 / +1.2 / +1.5, then +2.9 into 636.
- **Bar 122.**
  - Replace both rows with `[(467.0, 0.0), (468.5, 0.8), (481.0, 0.8), (483.95, -1.8), (484.05, 0.0)]`.
  - Simulated: steps +0.7 / +0.7 / -0.1, then +3.0 into 484.
- Both downbeats keep a step of about 3 dB, and the crescendos grow up to them.
- The downbeat levels are unchanged. Bar 159's end rises 0.8 dB and bar 121's third beat falls about 0.6, so the delivered margin of 160 over 122 can only grow (inferred). Re-check it with `smax.py`.

## 4. Coda: the cor anglais's counter-line is level with the DIV A solo in bars 171-172 (measured)

**Where.** qn 683-688. Cor anglais "p espr." against the solo ("Solo espr.", mp).

**Evidence.**
- Solo minus cor anglais per half-beat (A), 683.0-688.5: +1.1, -1.6, +0.6, +2.6, +0.7, -0.3, +1.4, +3.7, +5.3, +1.2, +0.9.
- The cor anglais is louder than the solo at 683.5 and 686.0. With the section patch (c39) the median was +3.8.
- In K the margins are +0.8..+7.6.
- The DIV A is 1.1-1.8 dB darker above 2 kHz than the section (measured), which costs it presence against the brighter cor anglais (inferred).
- The cor anglais carries +6 dB of coda lifts (roles `[683, 695, 2.5]`, `[683, 696, 1.5]`, `[683.0, 694.0, 2.0]`) and one -4 shape at 684. The c01 target was 3-5 dB under the solo.

**Fix.** In `build/roles.json`, add `["Cor anglais", [682.75, 689.0, -2.5, 0.5]]`.
- Simulated solo minus cor anglais over 683-688.5: +3.6, +0.9, +3.1, +5.1, +3.2, +2.2, +3.9, +6.2, +7.8, +3.7, +3.4 (A).
- The master moves under 0.5 dB, so the c40 `RIDE_TRIMS` stay valid (inferred). Do not raise the solo instead: that would move the ride fit.

## 5. Fugato entry 2 (bars 91-92): the cor anglais doubling swells on its long notes and drops out on its staccatos (measured)

**Where.** "Cor anglais stac" (stem 36), qn 360.5-371, doubling Violins II (f).

**Evidence.**
- Per-note 0.2 s peak minus Violins II (A):

  | 360.5 | 361.0 | 362.5 | 363.0 | 363.5 | 364.0 | 365.0 | 365.5 | 366.0 | 367.5 | 368-371 |
  |---|---|---|---|---|---|---|---|---|---|---|
  | -6.1 | +0.2 | +6.0 | -2.2 | -7.8 | -2.6 | +2.9 | +4.7 | -4.5 | -7.3 | -2.2..+0.3 |

- That spread of 13.8 dB is the widest of the three fugato doublings (Bassoon 8.1, Flute 12.5 including its ff tail).
- The long G-sharp4 at 361 (Sus MAX) grows from 25 at its attack to 33-35 A at 362.2-362.5, against a flat Violins II at 29-30. The 362.5 reading is that tail.
- The next staccato eighths fall to 23.7 and 17-20 A, 8-15 dB under the long note.
- The whole entry still carries the c17 +4 role `[360.25, 372, 4, 0.5]`, set when every note was on Sus rows. The staccato row is quieter and has only +2.5 more.

**Fix.** In `build/score_config.py`, extend `ALIAS_TRACKS["Cor anglais stac"]["tables"]` (level only, stem fix on the pass-2 stem):
- `LEVEL_SHAPES` += `[(361.3, 0.0), (361.8, -3.0), (362.3, -5.0), (362.4, 0.0)]` (the long note's swell);
- `LEVEL_SHAPES` += `[(364.85, 0.0), (364.95, -4.0), (365.88, -4.0), (365.95, 0.0)]` (the Sus / legato quarters);
- a new `"LEVEL_SHAPES_S"` with `(363.5, [(-0.05, 0.0), (0.0, 4.0), (0.2, 4.0), (0.25, 0.0)])` and `(367.5, [(-0.05, 0.0), (0.0, 4.0), (0.25, 4.0), (0.3, 0.0)])`.
- Expected per note against Violins II: about -6..+1 dB (inferred from the per-note readings).

## 6. Identical data, different level: Horn 3's C4 at 164 jumped 6.9 dB and now tops the bar-42 horn call (measured; cause inferred)

**Where.** Horn 3 qn 164 (C4, ff molto espr., Leg Slur MAX target, v124), bars 41-42. Here Horn 3 carries the Horns 3-4 a2 line, and "Horns a2" carries Horns 1-2.

**Evidence.**
- The MIDI and mix are identical to c39. The note body is 28.0 A in c39 and 34.9 in c40 (+6.9), and the 165 B-flat3 is +2.6.
- It is now the loudest stem at 164: -3.0 A re M against Horns a2 -4.3. In c39 it was 5.5 dB under the a2 pair.
- c35 recorded the same note moving -6.5 dB in the other direction, so it flips between two states.
- Six more notes moved by more than 3 dB with identical data (see the manual table).
- Every other unchanged stem repeated to within 0.5 dB in 94-100% of frames.
- Pre-roll resets: only CC36, which the patches map to the Repetition script. The reset controller Opus itself uses is CC16 (p.34, `Preferences.json`). Whether a CC16 reset fixes these flips is untested (inferred).

**Fix.**
- In `tools/build_reaper.py` at the `RR_RESET_QN` block (lines 706-711), also append `{"qn": RR_RESET_QN, "cc": 16, "v": 127}` for every track, and keep CC36. Do the same in `score_to_parts.py`'s `MEAS_TREM["rr_runs"]` lane if it is kept.
- Then compare the seven listed notes with c39 and c40.
- If Horn 3 164 still flips, judge it per render. Do not fit a level to one state.
- MANUAL-GAPS #6 notes that a reset can move other per-note fits once. Schedule it in a cycle that refits, and record the comparison in CHANGES.

**Do not touch:**
- the timpani roll levels, settles, `TIMP_CC1_MAP` / `TIMP_ROLL_TRIM_DB` and `TIMP_RH_ALT` (no roll covers anything);
- the c40 brass-lift removal and its kept tutti-chord rows (bars 26, 32, 72, 143);
- the Trumpet 2 roles;
- the Flute 1 stac and Bassoon 1 stac level fixes;
- the DIV A solo's contour, leads and join rows, and the solo's level (change the cor anglais, not the solo);
- `RIDE_TRIMS`;
- the 636 arrival lift and the Trumpet 1 shelf ramp;
- the tam-tam fff level and damp, the pp tam-tam, the sus.-cymbal stroke with the K Crash ring;
- Trumpets a2's fit;
- every solo margin c40 B listed (cor anglais bars 5-8, Horn 1 bars 13-14, Flute 1 bars 73-76, Clarinet 1 bars 127-130, Oboe 1 bar 145);
- the climax order (160 over 122);
- plus every c40 and earlier do-not-touch item.
