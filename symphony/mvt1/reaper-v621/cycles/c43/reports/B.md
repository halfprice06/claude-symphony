# Critic B, cycle 43 (render c42): balance and levels

## Manual notes (second reading of the c37 B row: May 2021 HO manual PDF pages 194-200, Chapter 6 "Mix", read in full; the p.196 picture read as an image; MANUAL-GAPS.md and DIGEST.md read)

Open MANUAL-GAPS items first, then the c37 B notes checked against the c42 render, then what the first reading missed.

| Source | What it says | Where it applies here | Followed now? |
|---|---|---|---|
| MANUAL-GAPS #6 (p.34, p.143, p.145; 2025 p.92) | Opus resets round robins on the CC set in Preferences (16); CC36 is the Repetition script's reset. | Both passes still send only CC36 in the pre-roll. | **No; planned for c43.** c42 evidence (measured): Trumpet 1's three Leg Slur phrases rendered 4-10 dB K louder with identical data, with the same 2-5 kHz share (pre-splice minus final at qn 276 / 277 / 280 / 283: +6.2 / +8.5 / +6.8 / +10.4 dB; 2-5 kHz share -11.6 / -15.7 / -12.7 / -13.8 dB pre, -12.5 / -17.8 / -12.8 / -11.4 final). The louder state is therefore more level, not a brighter dynamic layer. Horn 3's C4 at 164 is in its high state for the third render running. See finding 3. |
| MANUAL-GAPS #4 (p.138-139; the Mid channel is one of the sub-mixer channels on p.196) | Mid mics: definition without close-mic proximity. | Woodwinds and horns are still on Close + Main. | Open. It is not a level problem in this render: the marked woodwind solos lead by a median +2 to +11 dB A (checks below). It belongs to the blend lens (c45). |
| MANUAL-GAPS #1, #5, #7, #9, #12, #13 | Accent rows, expressive rows, divisi, portato, crescendo rolls, 3TB. | — | Still open. These belong to the articulation and holistic lenses. None of them sets a level problem found here. |
| p.194, p.196 (picture) | Each instrument has a master channel and one sub-mixer channel per mic (volume, pan, load). Each mic channel has a "Reverb Send" insert into an FX-bus Reverb. | `apply_mix()` writes `mix.json` `mics`: wind Close 0.5 / Main 0.8; horn and trumpet 0.5 / 1.0; timpani 0.2 / 0.5; harp 0.6 / 1.0; perc 0.3 / 1.0; basses 0.6 / 1.0; tuba 0.45 / 1.0. Strings and trombones keep the factory mix. Cello solo is Close 0.65 only. Unused mics are unloaded. | **Followed** (read; unchanged since c37). |
| p.195 | Store Mix / Restore Mix. | Not used; the pipeline writes the state. | Not applicable. |
| p.198 | The Effects Send has a level slider and a Post switch; post-fader is typical for reverb. | `send_pre_fader` true, with the send scaled by the mic volume. All 40 tracks, the pass-2 aliases included, share one hall (S. Cal Hall Perc TS 3.3 s, fx 0.19, wet 2.0, high cut 5.5 kHz). Sends: strings 0.25, harp 0.3, winds 0.35 (Fl/Ob 0.5), low brass / timpani / perc 0.45, horns 0.5, trumpets 0.65, DIV A solo 0.5. | **Followed in effect.** The REAPER volume envelope comes after Opus, so every role and shape moves the dry sound and the hall together, as a post-fader send would. All fixes below are of that kind (inferred from the signal order). |
| p.199-200 | Opus insert EQs: Bass Comp (32-256 Hz), a 3-band Channel EQ and a 6-band Equalizer. | The mockup uses ReaEQ after Opus. c37 B noted that the trumpets' 4 kHz shelf (+2.5 dB) supplies the presence a mic choice would. | Unchanged: Trumpets 1-3 and Trumpets a2 +2.5 dB at 4 kHz, trombones -4 dB. Consistent in effect (inferred). |
| **New**, p.196 picture with p.199 | An insert placed above the Reverb Send on a sub-mixer channel shapes only that dry mic, before the hall. | The low-mid bells on the celli are post-hall ReaEQs: static 125 Hz +3 and 170 Hz +3, plus the loud-span 150 Hz +6 (RBJ response +6 dB at 99 Hz, +10 dB at 125-157 Hz). The basses have 180 Hz +4 and 160 Hz +6. These also raise the hall's low tail. | Not tested (inferred). It matters at bars 82-83 (finding 5). |
| **New**, p.198 (level slider) | The send sets each channel's depth. | The f62 aliases copy Violins I / II's mix exactly. Their stems equal c41's Violins I / II over 219-243.5 (p90 within 0.34 dB, c42check). | **Followed:** the bar 55-61 violins sit in the same space as the rest of the movement. |

## Method

- **Render and data.** `cycles/c42/render` (40 stems; master = float sum, with the stem fixes and the Trumpet 1 splice) and the end-of-c42 `build/` (parts.json, roles, mix). Envelopes come from `vol_points()` of the c42 `tools/build_reaper.py`, loaded with `cycles/c33/actor_scripts/sim.py`.
- **Frames.** 4096-point FFT, 20 ms hop, stereo power. Per frame: A- and K-weighted power, eight bands and 1/3-octave bands from 20 Hz to 10 kHz.
- **Notation.** "re M" = stem minus master over the same window.
- **Summed tracks.** "Violins I" includes "Violins I f62", "Violins II" includes "Violins II f62", "Violoncellos" includes "Cello solo", and the three "stac" aliases are summed with their sources.
- **Simulations.** Stem frame powers are scaled by the proposed dB shape and the change is added to the master power. Arithmetic, not `stem_fix.py`.
- **Reference.** The Dvořák 9/i reference was analysed the same way (lossy; used above 75 Hz only).
- **Score.** Pages 3, 4, 6, 7, 8, 9, 11, 13, 14, 16, 17 and 18 read. Notes and marks checked in `mockup-events.tsv`.

## Findings, ranked by what a listener would gain

### 1. Bars 70-71 (qn 276-284): the closing theme's melody sinks under its own counter-motif (measured; fix simulated)

**Score (p.7, Tempo dell'Allegro, everything f).**
- The tune is in Flutes a2, Violins I, Oboe 1 and Trumpet 1.
- The dotted head-motif counter is in Clarinets a2, cor anglais, Horns 1-2 a2 and Violins II.
- There is no hairpin or new dynamic until the bar-72 cadence.

**Evidence (A re M per qn, K in brackets).**

| | 272-275 (bar 69) | 278 | 279 | 280 | 281 | 282 | 283 |
|---|---|---|---|---|---|---|---|
| Tune group | -2.1 .. -3.5 | -4.1 (-4.9) | -4.5 | -4.5 | -5.3 (-7.5) | -5.7 | -6.0 (-7.1) |
| Motif group | | -3.7 | -4.8 | -5.0 | -7.0 | -3.8 | -4.7 |
| Bass group (K) | | | | | -3.6 | -4.2 | -3.7 |

- **Tune against the motif.** In bar 69 the tune leads the motif by 1.2-7.6 dB (median 4.1). In bars 70-71 the motif is over the tune on 278, 282 and 283 (by 0.4 / 1.9 / 1.3 dB) and within 0.5 dB of it on 279-280. The bass group is 3.4-3.9 dB over the tune in K at 281-283.
- **Violins I against Violins II.** Vln I minus Vln II goes +10.7 / +9.3 (272 / 275) → +0.2 / +0.4 (278-279) → -3.6 (283).
- **Violins I against the master.** Violins I falls from -4.1 to -8.5..-11.9 A re M inside a printed f.

**Cause, read in the envelope.**
- **The tune's crescendo gains are released mid-phrase.** They are held to the first onset after the arrival, then released:
  - Violins I: +8.0 → +5.0 dB at 275.5-276.5 (hpgain [270, 272, +3]);
  - Flute 1: -1.3 → -5.3 at 275-277;
  - Oboe 1: +4.2 → -1.8 at 276.
- **The motif keeps its lifts to 284.**
  - Its +2 dB roles stay on to 284: Clarinet 1, Violins II and Horns a2 [272, 284, 2].
  - Violins II also rises +4 dB at 278 (+3.0 → +7.0). Its `ROW_TRIM_DB` Sus MAX trim (-4) applies only over 274.5-277.5 of a run of Sus MAX notes.

**Fix (level only; `stem_fix.py`, then `--mix-only`), `build/score_config.py`:**
```
LEVEL_SHAPES["Violins I"]  = LEVEL_SHAPES.get("Violins I", [])  + [[(275.5, 0.0), (276.5, 2.0), (283.75, 2.0), (284.0, 0.0)]]
LEVEL_SHAPES["Flute 1"]    = LEVEL_SHAPES.get("Flute 1", [])    + [[(275.0, 0.0), (277.0, 2.0), (283.75, 2.0), (284.0, 0.0)]]
LEVEL_SHAPES["Flute 2"]    = LEVEL_SHAPES.get("Flute 2", [])    + [[(275.0, 0.0), (277.0, 2.0), (283.75, 2.0), (284.0, 0.0)]]
LEVEL_SHAPES["Oboe 1"]     = LEVEL_SHAPES.get("Oboe 1", [])     + [[(275.5, 0.0), (276.25, 2.0), (283.75, 2.0), (284.0, 0.0)]]
LEVEL_SHAPES["Violins II"] = LEVEL_SHAPES.get("Violins II", []) + [[(277.625, 0.0), (277.875, -4.0), (283.75, -4.0), (284.0, 0.0)]]
LEVEL_SHAPES["Clarinet 1"] = LEVEL_SHAPES.get("Clarinet 1", []) + [[(276.75, 0.0), (277.25, -2.0), (283.75, -2.0), (284.0, 0.0)]]
LEVEL_SHAPES["Horns a2"]   = LEVEL_SHAPES.get("Horns a2", [])   + [[(276.75, 0.0), (277.25, -2.0), (283.75, -2.0), (284.0, 0.0)]]
```

**Simulated.**
- Tune minus motif per qn 276-283: +2.5 / +2.8 / -0.4 / +0.3 / +0.5 / +1.7 / -1.9 / -1.3 → +3.9 / +5.2 / +3.6 / +4.6 / +4.6 / +5.8 / +2.2 / +1.6 dB A.
- Vln I minus Vln II: +5.4..+8.7 through 282.
- Master K per qn -0.3..+0.6 dB against c42 (+0.4 / +0.6 at 276-277, within ±0.3 after). The step into the bar-72 cadence (whose brass lift starts at 283.75) is unchanged.
- The simulation used the Violins II ramp 0.125 qn later and the tune ramps ending at 283.5. The rows above put the breakpoints on the 0.125 qn envelope grid.
- Do not fit this against a loud-state Trumpet 1 (finding 3).

### 2. Bars 98-102, letter F (qn 388-407): the brass eighth figure under the ff tune cannot be heard (measured; fix simulated)

**Score (p.9).**
- The tune is ff in Flutes a2, Oboes, cor anglais, Violins I, Violins II (sul G) and celli.
- Horns 1-2 a2 and Trombone 1 (the staff is marked "1." from bar 96; Trombone 2 rests), marked f, answer each bar with a half note, then three eighths (390.5-391.5, 394.5-395.5, 398.5-399.5, Tbn also 406.5).

**Evidence (measured).**
- **The brass against the tune.** Horns a2 + Trombone 1 sit at a median -11.1 dB A re M (range -8.3..-16.8). That is 8.9 dB under the tune group per beat (6.2-16.6). Trombone 1 alone sits at -11.5..-18.2 A re M.
- **The first eighth of each figure.** It is 3-6 dB under the next eighth on both stems (Horns a2 -3.7 against +0.3; Trombone 1 -3.0 against +0.4 dB K at 390.5 / 391.0). This is the plateau a pickup after a rest sits on (KIT c16).
- **Those first eighths against the master.**

  | qn | 390.5 | 394.5 | 398.5 | 406.5 |
  |---|---|---|---|---|
  | A re M | -19.6 | -17.1 | -14.1 | -20.4 |
  | 2-5 kHz re M | -21.2 | -26.9 | -21.3 | -26.0 |

- **No role holds them down.** The only role is Horns a2 -0.8; Trombone 1 has only its f trim of -0.9.

**Orchestration norms.**
- RK, "Comparison of resonance": at forte a trombone equals 2 horns equals 4 woodwinds, and a string section equals 2 woodwinds. On that scale two horns plus one trombone count about 8 woodwind units, against about 11 for this tune group (5 winds + 3 string sections), roughly 1.5 dB under it at an equal dynamic. Adler (PDF p.292) warns that the brass can cover everything.
- The printed one-step difference (f under ff) suggests the brass should sit clearly under the tune but still be heard: about 5-6 dB under it, not 9-17 (inferred).

**Fix (level only), `build/score_config.py`:**
```
LEVEL_SHAPES["Horns a2"]   = LEVEL_SHAPES.get("Horns a2", [])   + [[(387.75, 0.0), (388.0, 3.0), (404.25, 3.0), (404.5, 0.0)]]
LEVEL_SHAPES["Trombone 1"] = LEVEL_SHAPES.get("Trombone 1", []) + [[(387.75, 0.0), (388.0, 3.0), (406.25, 3.0), (406.5, 0.0)]]
PICKUP_LIFT["Horns a2"].update({390.5: 6.0, 394.5: 6.0, 398.5: 6.0})
PICKUP_LIFT["Trombone 1"].update({390.5: 6.0, 394.5: 6.0, 398.5: 6.0, 406.5: 6.0})
```

**Simulated.**
- Brass group: median -8.3 dB A re M.
- Tune minus brass: median +5.8 dB (3.2-12.9).
- First eighths: -10.9 / -8.6 / -6.2 / -14.3 A re M; 2-5 kHz -12.4..-19.6.
- Master: +0.36 dB K over 388-408. The tune still leads every beat.

**Check after the render.** If an eighth now stands more than 2 dB over its neighbours, lower its `PICKUP_LIFT` value to the measured excess.

### 3. The CC16 reset (c43) will move the balance points that depend on a render state: re-measure them before fitting anything (measured; cause inferred)

**Trumpet 1, at the three spliced phrases (275.3-284.1, 451.3-456.0, 642.9-644.0).**
- **The loud state (the c42 pre-splice stem) covers the strings.**

  | qn | 276-278 | 278-280 | 280-282 | 282-284 | 454-456 | 643-644 |
  |---|---|---|---|---|---|---|
  | Trumpet 1, loud state | -3.7 | -7.3 | -7.8 | -4.9 | -8.7 | -4.2 |
  | Violins I | -9.4 | -8.9 | -8.9 | -11.3 | | |

  Values are A re M. In bars 70-71 Trumpet 1 is then the loudest stem.
- **The c41 state (now spliced in):** -9.9 / -11.5 / -14.1 / -12.7 at 276-284, -15.1 at 454-456, -6.1 at 643-644.
- **Why a trim would hold.** The 2-5 kHz share is the same in both states (Manual notes, row #6). With the reset on CC16 the state should repeat from render to render. A trim is then a lasting fix and not another splice (inferred).

**Horn 3 at 164-165.**
- Horn 3 carries Horns 3+4 in the four-horn unison call: Horn 4's copy is dropped as a unison.
- Its C4 is +1.1 / +3.7 dB A over Horns a2 (which carries Horns 1+2) at 164.0 / 164.5. Two against two should be level.
- This is the third render in this state.

**Fix: the measurement order for the c43 actor.**
- **Reset.** Send CC16 = 127 next to CC36 in both projects (main and pass 2).
- **Trumpet 1.** Before any refit, compare it per 0.5 qn with the c42 final numbers above.
  - Within 1.5 dB: accept.
  - Loud state: put `note_trims.json` "Trumpet 1" rows on the Leg Slur notes of those phrases, sized from that render, stepped (0.1 s). Do not splice.
- **Horn 3.** If Horn 3 minus Horns a2 still exceeds +2 dB A over 164.0-165.0: `note_trims.json` "Horn 3" "164.0" = minus the excess, with 164.0 in `NOTE_TRIM_RAMP_S["Horn 3"]` at 0.1 s.
- **The c42 balance checks.** Re-run them (`c42check.py 43 b1 b2 b3 c2`, and findings 1, 2 and 4 here) before trusting any per-note fit from c42.

### 4. Bars 56-59 (qn 220-236): the clarinet-horn counter-melody is level with the violins' molto cantabile tune in K (measured; fix simulated)

**Score (p.6).**
- Violins I and II play the tune in unison, p molto cantabile, with < > hairpins.
- Clarinet 1 and Horn 2 play the counter-melody in unison, p espr.

**Evidence (measured, violins summed with the f62 aliases).**
- **Per beat.** Violins minus Clarinet 1 + Horn 2: median +3.4 dB A, but +0.5 dB K.
- **On the downbeats.** The counter is over the tune in K on 7 of 16 beats: -2.6 at 220, -3.5 at 224, -1.8 at 228, -3.1 at 230, -0.9 at 234. These are the beats where the counter enters on a long note as the tune's hairpins dip.
- **The roles.** Clarinet 1 has a +3 dB role [220, 244, 3, 2] and Horn 2 a net +1 ([220, 244, 2] with [220, 244, -1, 2]). These come on top of c37's +5 dB note trims on Horn 2's low notes, which were wanted.
- **Within the counter.** Clarinet 1 minus Horn 2: median +2.7 dB.
- **Norm.** RK at p: one string section equals one wind. The tune (two sections in unison) and the counter (two winds) are therefore equal in weight when every role is 0. The tune, marked molto cantabile, should be on top (inferred).

**Fix (level only), `build/roles.json`:**
- "Clarinet 1" [220, 244, 3, 2] → [220, 244, 0.5, 2];
- "Horn 2" [220, 244, 2] → [220, 244, 1].

**Simulated.**
- Violins minus counter: median A +5.2, K +2.3 dB (minimum K -1.9). Beats with the counter over the tune in K: 7 → 4.
- Clarinet 1 minus Horn 2: +1.2 dB (the unison stays blended).
- Master: -0.5 dB K over 220-236.

### 5. Bars 82-83 (qn 324-332): the celli's A-flat2 / G2 make these the most bass-heavy tutti bars (measured; EQ effect simulated per 1/3 octave)

**Evidence (measured).**
- **The band ratio.** Master 79-125 Hz minus 157-397 Hz per 2 qn: -2.2 / -3.2 / -2.5 / -3.7 dB.
  - Loud-bar median: -8.9 (p75 -6.7).
  - Dvořák reference, loud 2 s blocks: median -11.9, p75 -7.2.
  - Only bar 97 (a low-register ff chord alone) is heavier.
- **Who carries the band.** The celli carry 40-67% of 79-125 Hz here; timpani A-flat2 strokes 18-22% and basses 10-14%.
- **The celli as the loudest stem.** They are the loudest K stem at 324-326 and 328-330 (-7.8 / -8.5 dB re M) while playing bass half notes under the ff motif.
- **The celli's fundamentals.** On G2 the fundamental is +9.5 dB over the mean of harmonics 2-4 (median of 14 notes).
- **The EQ.** At 99 Hz the static bells add about +3.5 dB and the loud-span 150 Hz +6 bell (on from 323.5) about +2.5 dB (RBJ response, computed).

**Fix (EQ; needs the render or an EQ simulation, and `--mix-only`).**
- Add to `build/mix.json` "Violoncellos" a second `loud_eq` spec only for this window: `{"points": [[323.5, 0], [324, 1], [331, 1], [332, 0]], "bands": [{"band": "bell2", "hz": 100, "db": -4, "bw_oct": 0.5}]}`. This matches the basses' 98 Hz -4 band.
- Simulated on the celli's 1/3-octave bands: the master ratio goes to -3.3 / -4.3 / -5.2 / -5.3.
- The 125-200 Hz body stays.
- The gain is modest. Do it only if the EQ simulation agrees.

## Checks with no change proposed (measured)

**Dynamic mapping across families: p sounds like p.** Method: on every beat where four or more tracks hold one steady printed dynamic with no hairpin, each track's K level minus that beat's median.
- **Within ±3 dB.** Every track at every dynamic, apart from:
  - the melody roles: Violins I +2.2..+6.4, Clarinet 1 pp +7.6 (coda solo), Trumpet 1 ff +4.1 (first trumpet);
  - timpani ff +3.4;
  - register and inner parts on the low side: Flute 2 f -3.8, Contrabassoon f -5.3, Bassoons fff -3.5 / -4.3, Clarinet 2 f -6.3. Clarinet 2's case is the letter G triplets, where Clarinets 1+2 and the violas doing the same figure both sit at -18..-26 A re M under the ff tune and brass.
- **The new trumpet tracks.** Trumpet 2 / 3 at f 0.0 / +0.8 and at ff +0.9 / 0.0. In the coda tune, Trumpets a2 is the loudest stem in 167-169 (-5.1..-7.2 A re M), 3.6-5.4 dB over Horns a2.

**Families against RK (K medians at f / ff).**

| pair | render, f / ff | RK |
|---|---|---|
| trombone minus trumpet | -0.1 / -0.3 | 0 |
| horn minus trumpet | -2.1 / -2.5 | -3 |
| horn minus woodwind | +1.4 / +1.3 | +3 |
| string section minus woodwind | +4.3 / +3.7 | +3 |
| trombone minus tuba | -0.7 / +0.7 | 0 |

Brass under the strings by 0..+1.6 dB is lighter than RK; that suits a symphonic tutti and was left alone.

**Melody over accompaniment, the marked solos.** Median margin over the loudest other stem (A / K):
- cor anglais bars 5-8: +10.4 / +6.3;
- Horn 1 bar 13: +8.9 / +10.1;
- Flute 1 bar 73: +10.9 / +9.4;
- bass clarinet bar 77: +2.2 / +5.3;
- Oboe 1 bar 145: +7.3 / +4.2;
- Clarinet 1 bar 175: +4.2 / +3.9.

**Tutti tunes.** Group sums:
- bars 27-31: the theme leads every other group by 4-7 dB;
- bars 139-142: the tune is at -1.5..-3.0 re M, the counter at -6..-11;
- bars 158-161: the tune group leads every non-tune stem by 2.9-7.6 dB;
- bars 167-170: Trumpets a2 leads 2-6 dB over every single chord stem.

**Timpani (Dan's roll rule holds).**
- Rolls sit at a median -9..-19 dB K re M by dynamic. No roll is the loudest stem except the solo opening.
- ff strokes: median -8.1 (-13.8..-5.2). Coda pp strokes: -5.1.

**Percussion.**
- **Tam-tam fff.** -9.4 A re M on the stroke, then -5.6..-6.7 through 485-488 and -6..-8 K to 492. It is the loudest stem by about 6 dB for two bars, which a heavy-beater fff allows (kept, as in c37 / c42).
- **Tam-tam pp at 696.** -14.1 A / -10.3 K re M at the stroke.
- **Suspended-cymbal roll.** 5-12 kHz re M rises -34.6 (634) → -9.9 (635) → -1.9 (635.5); the stroke at 636 is -1.7. The crash ring then holds 5-12 kHz at -4.6..-8.2 dB for 2 s.

**Low end.**
- Long-term 1/3 octaves (metrics.md) against the Dvořák: 63 Hz -6.7 vs -6.2, 125 Hz +3.8 vs +7.0 dB re 1 kHz. The bass is not boomy overall.
- The only outliers are bars 82-83 (finding 5) and the register-driven bar 97.

**Item 7 (loop pulsing).** Master autocorrelation at 3.95 s (100-300 Hz / centroid):

| passage | 100-300 Hz | centroid |
|---|---|---|
| opening | -0.00 | +0.17 |
| Lento chorale | -0.44 | +0.07 |
| tam-tam l.v. | -0.01 | +0.26 |
| coda chorale | -0.06 | -0.00 |
| final chord | -0.20 | +0.18 |

**Item 8 (accent fronts).** 2-5 kHz in the first 80 ms minus the body (+0.25..+0.6 s):

| family | median | p90 | over +3 dB |
|---|---|---|---|
| brass | -8.4 | -2.0 | 3 of 161 |
| strings | -3.2 | +2.3 | 11 of 154 |
| winds | -3.5 | +3.6 | 19 of 143 |

The wind count is for the articulation lens. The largest master jumps are the bar-83 tutti entry after a rest.

**S1.** The c42 actor's re-attack rise: master celli 3.9 dB, basses 3.7 dB (no change since c41).

**S2.** The probe's pcX robust SD is 52 / 46 / 59 / 48 ms (Violins I / Violins II / violas / celli), with 0 late notes.

**S3.** Master K re the forte at 0-0.05 / 0.05-0.1 / 0.1-0.2 / 0.2-0.3 s:

| | 0-0.05 s | 0.05-0.1 s | 0.1-0.2 s | 0.2-0.3 s |
|---|---|---|---|---|
| bar 84 sub. p | -0.0 | -2.4 | -8.0 | -10.0 |
| bar 62 sub. p | -3.0 | -5.7 | -8.7 | -11.8 |
| fermata release (679) | -3.3 | -4.9 | -8.8 | -13.1 |

Neither subito cuts the hall.

**Delivery.** -19.7 LUFS, LRA 14.9 LU, span 19.0 dB, limiter 0.6 dB. Delivered short-term maxima re bar 160:
- 122-124: -0.7;
- 156-159: -1.5;
- 117-121: -1.6;
- 167-170: -1.7;
- 26-32: -2.9;
- 131-134: -4.0;
- 69-72: -4.5;
- 95-102: -4.9.

The development's ff has no trumpets, and its brass are marked f.

## Do not touch

- **Kept from c42 / c41.**
  - The c42 B #1-#3 data: Horn 1 roles and violas +2 in the dolce tune, the bar-10 shapes, the Horn 4 453 / Bassoon 1 364 changes.
  - The c41 B data: cor anglais role and stac shapes, the `_all` fff rows into 636 / 484, the coda cor anglais -2.5.
  - Horn 2's c37 note trims at 220 / 232 / 234.
  - The soft and dyn trims as a set (fix every finding above with roles and shapes).
- **Timpani and percussion.** The timpani roll levels, `TIMP_CC1_MAP` / `TIMP_ROLL_TRIM_DB` and the coda pp strokes; the tam-tam fff and pp; the suspended-cymbal swell with the K Crash ring.
- **Solos and tunes.** The Trumpets a2 coda tune; the DIV A coda solo and `RIDE_TRIMS`; every solo margin listed above.
- **Climaxes and second-pass tracks.** The climax order (160 > 122); the f62 aliases with their release fit; the bar-72 brass lift rows from 283.75.
- **Every earlier do-not-touch item.**
