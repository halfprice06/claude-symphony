# Cycle 3, critic C: tempo, timing and transitions (on the cycle 2 render)

Under review: `cycles/c02/render`, `build/parts.json` (unchanged since the c02 render), `tools/score_to_parts.py`, `tools/build_reaper.py`. Scratch scripts are in `/private/tmp/claude-501/mockup-loop/c03-C/`. Set `CYCLE=03` to run them on the next render.
- `entries.py`, `ent2.py`: entry onsets (notes after at least 0.5 qn of silence). "First sound" is the time from the MIDI onset until the 5 ms envelope comes within 20 dB of the note's early peak. "Arrival" is the time until it comes within 6 dB.
- `leg.py`: the legato arrival time. It is the time after the MIDI onset when the energy at the new pitch's harmonics 1-4 exceeds the old pitch's (the same method as c02-A `xover.py`).
- `sync.py`: note starts compared across tracks at every common onset.
- `det.py`: the same entries measured in the c02 pass1, pass2 and final renders, to test whether the delays repeat.
- `f0trace.py`: the dominant pitch every 20 ms against a list of candidate pitches.
- `ks.py`: keyswitch lead times. `ramp.py`: tempo-ramp durations.

Method floor: the winds measure 50-150 ms with the same crossover method. A crossover marks the middle of a transition, so the lag a listener hears is about 40 ms less than the measured figure.

## 1. Every string legato note sounds 220-290 ms late, and the strings trail the winds they double by 150-190 ms (measured)

**Where:** all slurred and Leg BC string notes, Vln I, Vln II, Vla and Vc. It is worst in the doubled melodic passages: bars 53-60 (qn 172-204), 71-82 (qn 238-274) and 87-92.

**Evidence:** median crossover lag by track (`leg.py`, c02 render):

| Track | n | median (ms) | p75 (ms) | Leg Slur / Leg BC (ms) |
|---|---|---|---|---|
| Vln I | 96 | 250 | 290 | 232 / 285 |
| Vln II | 98 | 275 | 324 | 280 / 265 |
| Vla | 185 | 220 | 295 | 250 / 270 |
| Vc | 92 | 260 | 318 | 290 / 252 |
| Hn 1 | 50 | 202 | 286 | |
| Hn 2 | 11 | 190 | | |
| Ob 1 | 35 | 155 | | |
| Bn 1 | 12 | 155 | | |
| BCl | 11 | 140 | | |
| Fl 1 | 56 | 88 | | |
| Cl 1 | 25 | 90 | | |
| CA | 25 | 90 | | |

- **Velocity has only a small effect.** At velocity 120 against 105 the lag is Vln I 225 against 265 ms and Vla 210 against 298 ms. The HO manual (p. 98, True Legato) says 110-127 gives the shortest transition.
- **Wind-to-string offsets.** At onsets the parts share, the median string lag after the wind is:
  - Fl 1 against Vln I / Vln II / Vc: 150 / 190 / 130 ms;
  - Cl 1 against the same: 160 / 190 / 160 ms;
  - Ob 1 against the same: 90 / 115 / 90 ms.
- **Examples** (`sync.py`): bar 77 beat 1, Fl 70, Cl 130, Vln II 260, Vln I 295, Vla 340 ms. Bar 54 beat 3, Cl 85, Hn 120, Vc 265, Vln I 295, Vln II 335 ms.
- At 52-64 bpm, 250 ms is a sixteenth note. A listener hears every string melody note as a dragged, smeared arrival behind the beat, and hears winds and strings in unison as two attacks.
- **The lag is deterministic.** The c01 objection, that start delays are not deterministic, applies to streamed entries after a rebuild (finding 5). It does not apply to legato transitions. The interquartile range is ±40 ms, and the c02 pass2 and final renders give the same values note for note (`det.py`).

**Fix,** in `tools/score_to_parts.py`, `build_track()`, after the velocity loop and before the keyswitch loop:
- Add `LEG_LEAD_S = {"string": 0.20, "brass": 0.15, "Oboe": 0.08, "Bassoon": 0.08, "Bass clarinet": 0.08, "wind": 0.04}`. Look up the instrument name first, then the family.
- For each note with `leg_target` (slur and Leg BC targets), compute `lead_qn = LEG_LEAD_S * bpm(q) / 60`, where bpm is the local tempo. Cap it at 0.45 × the previous note's duration.
- Move `n["qn"] -= lead_qn` and keep `n["end"]`.
- Set the previous note's end to `max(prev_end, new_qn + LEG_OVERLAP)` so the overlap survives.
- Compute the keyswitches (`early_time`) from the moved onsets so that every keyswitch stays at least 0.03 qn before its note. CC11, CC1 and vol_db stay on score time.
- String legato velocity: `LEG_VEL_STRONG["string"] = (127, 118)`. Horns stay at (120, 105).

**Target:** string median crossover 60-110 ms, and every wind-string median offset under 50 ms. Check with `CYCLE=03 python leg.py` and `sync.py`.

## 2. The after-grace run into the second ff (bar 78 to bar 79, qn 261.58-262) arrives early and leaves a 15-19 dB hole just before the ff downbeat (measured)

**Where:** Vln I, Vln II and Fl 1. The source is `aTwo.ily` lines 13, 18 and 23: `\afterGrace c4 { f16( g aes }` into the B flat on bar 79.

**What is wrong:**
- The MIDI places the three grace notes at qn 261.581, 261.635 and 261.693, each about 0.05 qn (60 ms) long. They end at 261.75, a quarter of a beat (about 310 ms at 48 bpm) before the downbeat they lead into.
- Nothing sounds in the gap. In the score the run connects straight to the ff note.
- The main note C is also cut early: in Vln I it ends at 261.53.

**Evidence** (`f0trace.py`):
- **Vln I.** Pitch 89 is heard 261.65-261.73, 91 at 261.77-261.83, and 92 never wins. From 261.83 to 262.0 the release of 89 sounds at -52 to -57 dB, against -40 dB during the run. The ff 94 wins only at 262.03, and its level reaches -41 dB at 262.13.
- **Vln II.** The run sounds 261.65-261.78. Then the tail of 72 sounds at -50 to -53 dB until 262.0, against -36 dB before the run.
- **Fl 1.** Same pattern: -50 to -55 dB from 261.85 to 262.02.
- **Keyswitches.** The articulation toggles Leg Slur, Leg BC, Leg Slur inside the run. One Leg BC keyswitch, at 261.6327, lands 3 ms before its note (`ks.py`). That is the only keyswitch in the piece with less than 55 ms of lead.
- **Result:** the climax downbeat at bar 79 arrives after a dip, about 80-130 ms late.

**Fix,** in `tools/score_to_parts.py`. Add an after-grace rule in the note loading or in `build_track()`. Detect grace notes in `mockup-events.tsv` as rows with a non-zero third column, followed by a main note.
- **Grace placement.** Re-place the grace notes so that they end on the next main note: at `q_next - k * g` for k = 3, 2, 1, with g = 0.09 s converted at the local tempo. Each note lasts g + LEG_OVERLAP.
- **Main note.** Hold the main note (C) until the first grace note starts, overlapping it by LEG_OVERLAP. Do not apply the breath or slur-end shortening to it. Fl 1 has a printed breath before the C (line 23), which stays.
- **Articulation.** Play the run and its target with one articulation, so there is no keyswitch inside the run:
  - Vln I and Vln II: "Slur Runs" (1st Violins KS Master key 42, 2nd Violins KS Master key 43). The row must be loaded with `load_articulations()` in `build_reaper.py`, as for pizz. in c02.
  - Flute: "Leg Slur Runs" (FL KS Master key 37).
  - If the runs rows will not load, use Leg Slur MAX at velocity 127, with no Leg BC on any grace note.
- **Target note.** The ff target (94 Vln I, 82 Vln II, 94 Fl 1) gets the finding-1 legato lead.

**Target:** no window under -46 dB between qn 261.6 and 262.0 in Vln I and Vln II, and the target pitch winning by qn 262.0 + 0.05.

## 3. The viola sextuplet figure in bars 59-60 (qn 196-204, f into ff) is smeared by more than one note (measured)

**Where:** Violas, 48 notes, each 0.167 qn: 156 ms at 64 bpm, 161 ms at 62 bpm.

**Evidence:**
- Leg Slur / Leg BC transitions take 160-320 ms in this passage. In 23 of 47 cases the crossover test finds the new pitch already louder before its onset (-100 ms in `leg.py`), because the previous pitch never took over.
- `f0trace.py`, written ges-bes-es'-bes at 196.0, 196.167, 196.333 and 196.5:
  - 58 (bes) is heard 196.0-196.24, 54 (ges) 196.26-196.34, 58 at 196.36-196.58 and 63 (es') at 196.60-196.68;
  - so the figure runs about 0.25 qn (230 ms) behind, more than one note;
  - the note lengths are uneven, 80-230 ms, and the top note E flat is only about 80 ms long each time.
- This is the motor of the animando climax, and it sounds blurred and behind the violins and flutes.

**Fix,** in `tools/score_to_parts.py`. The Violas KS Master has no runs articulation (checked in `ks_maps.json`; the Violas folder has no Slur Runs patch). Add a rule: slurred string notes shorter than 0.25 s use the Sus MAX keyswitch, not Leg Slur / Leg BC. Each note overlaps the next by 0.03 qn, which Sus MAX allows because it is polyphonic, so the slur still sounds connected. Keep the CC11 crescendo as it is.
- The actor should compare this with the alternative: Leg Slur MAX at velocity 127, with the finding-1 lead capped at 0.45 × 0.167 qn.
- Pick the one where `f0trace.py "Violas" 196 198 54,58,63` shows each pitch within 40 ms of its MIDI onset and every note at least 100 ms long.
- Vln I and Vln II should use their KS Master "Slur Runs" for any string note under 0.25 s. In this score that is only the bar 78 grace run (finding 2).

## 4. Every rit., allargando and animando is a set of tempo steps, so the tempo jumps by 4-8 bpm at bar lines (measured and inferred)

**Where:**
- bars 35-36 (49, 45);
- bar 47 beats 3-4 (57, 55);
- bars 53-60 (60, 61, 62, 64, then 62, 58);
- bars 63-64 (50, 46, 40);
- bars 78-82 (50, 48, 46, 44);
- bars 89-92 (48, 44, 40, 36, 20).

**Evidence (measured):**
- `parts.json` `tempo` matches the `\mt` steps in `global.ily` exactly. The tempo map is correct against the score.
- `build_reaper.py tempo_job()` writes square markers (`lineartempo=false`). Each step is a sudden 4-13% change on a beat, for example 62 → 58 in the middle of bar 60 and 46 → 40 at beat 3 of bar 64.
- The `\mt` comment in `global.ily` calls them "MIDI-only tempo step[s]" that realise the printed rit. and allargando. A printed rit. is a gradual slowing; the step version is only an approximation of it.
- *Animando* (bar 53) is a gradual push in the same way.
- The breath marks (comma) at qn 204 (9 winds, before Largamente, bar 61) and qn 268 (7 winds, bar 81) get no time at all. The strings are marked molto sostenuto at 204. *Inferred:* real players take a small lift there.

**Fix,** in `tools/score_to_parts.py`, after `tempo` is read. Keep the step tempo model, so `qn_to_sec`, `measure.py` and every analysis stay valid, and make the steps fine:
- Inside each span from a rit./allargando/animando text to the next "a tempo" / "Tempo I" / "Largamente" point, put each printed step value at the midpoint of its own span. Interpolate linearly between those points, starting from the tempo in force when the span begins, and write a tempo point every 0.25 qn.
- This keeps each span's length within about 2% of the printed steps (`ramp.py`). For example:
  - bars 35-36: 52 → 42 at qn 107.75 (7.67 s, the same as the steps);
  - bars 63-64: 54 → 39 (10.4 s);
  - bars 78-82: 52 → 42.5 (19.1 s);
  - bars 53-58 animando: 60 → 64 by qn 196, held through bar 59, then 64 → 56 over qn 200-204 into Largamente 54.
- Leave the final step (36 → 20 at qn 303, the fermata) as it is.
- Optional: put a short caesura before the two breath arrivals, with a tempo point of 40 bpm at qn 203.75 and at 267.75 (about +100 ms each), restored at the next point.
- `build_reaper.py tempo_job()` needs no change; it writes more square markers.

## 5. Soft sustained entries in strings, horns and low brass bloom in 300-650 ms; the delay is repeatable (measured)

**Where:** non-legato first notes of phrases at pp-p, for example:

| Entry | Track and qn | Arrival (ms) | First sound (ms) |
|---|---|---|---|
| Bar 15 | Vln II 42 | 775 | |
| | Vla 42 | 650 | |
| Bar 37 | Vln II Flautando 108 | 1010 | 190 |
| Bar 45 | Vla 140 | 490 | |
| | Vln II 140 | 425 | |
| | Cb 140 | 800 | 250 |
| Bar 48 | Vc 152 | 730 | |
| Bar 71 | Vc 238 | 675 | 205 |
| | Vla 238 | 400 | |
| Bar 87 | Vln II 286 | 795 | 285 |
| | Hn 3 286 | 435 | |
| Bar 60 | Tuba 200 | 475 | |
| | B. Tbn 200 | 495 | |
| | Hn 4 200 | 440 | |
| Bar 61 | Hn 3 204 | 355 | |

Winds entering at the same moments arrive in 60-150 ms, so the spread between tracks at an entry is 600-1000 ms: bar 15 Ob 95 against Vln II 775; bar 37 Harp 20 against Vln II 1010; bar 87 Hn 4 115 against Vln II 795.

**Evidence:**
- `det.py`: the c02 pass2 and final renders give identical first-sound and arrival times for every one of these entries. The delays are therefore sample attack, not streaming, and can be compensated.
- The exceptions are qn 0 and Vln I at 48 and 60. At qn 0 pass2 started Vln II, Vla and Vc 460-555 ms late and the final render 10-20 ms late. Those differences come from streaming.
- The bloom at pp is partly real: a pp section entry is soft-edged. But an arrival two-thirds of a beat after the beat reads as late.

**Fix,** in `tools/score_to_parts.py`, in the same pass as finding 1. Notes that start after at least 0.5 qn of silence in that track, in a sustained articulation (Sus MAX, Leg Slur MAX first note, Flautando, Sus Non Vib, Tremolo; not pizz., harp, timpani or shorts), move earlier by:
- strings: 120 ms when CC11 at the onset is 50 or less, 60 ms above;
- horns, trombones and tuba: 100 ms at 50 or less, 50 ms above;
- bassoons and contrabassoon: 60 ms;
- other winds: 0.

Never move a note before qn 0. Recompute the keyswitch time from the moved onset.

**Target:** median arrival at soft entries under 300 ms in Vln I, Vln II, Vla, Vc, Hn 3 and Hn 4; entry spreads at bars 15, 45 and 87 under 400 ms.

For qn 0 only: `render_cycle.py` could play the project once from qn 0 for 5 s before the render, so the first notes are already in memory. That is a transport action, not a render setting.

## Do not touch

- The tempo values themselves: `parts.json` tempo equals `global.ily` `\mt` exactly. Finding 4 only smooths between them.
- The final fermata: 6.3 s with the -20 dB fade from 301.5, and a tail that decays from -68 to -100 dB over 1.25 s after note-off with no cut-off.
- Keyswitch placement in rests (median lead 69 ms, minimum 55 ms, except the one grace-run toggle in finding 2).
- The 1x render and the three-reading load wait.
- Pizzicato, harp and timpani onsets (first sound 0-25 ms, arrival 25-125 ms): do not shift them.
