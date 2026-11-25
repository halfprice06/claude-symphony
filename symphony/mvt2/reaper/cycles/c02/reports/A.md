# Cycle 2, critic A: articulation and phrasing (on the cycle 1 render)

Scripts and outputs are in `/private/tmp/claude-501/mockup-loop/c02-A/`:
- `arts.py` rebuilds each note's articulation from `parts.json` keyswitches and writes `arts.json`.
- `xover.py` measures legato arrival: the time after the MIDI onset when energy at the new pitch's first four harmonics exceeds energy at the old pitch's.
- `dip2.py` and `dip.py` measure level dips at note joins.
- `pz.py` and `peak.py` give time-to-peak and decay per note.

Bars are converted from qn as 1-36 = qn/3, 37-64 = (qn-108)/4, 65-92 = (qn-220)/3.

## 1. Pizzicato, tremolo and flautando are not played. Those keyswitches point at articulations that are not loaded (Vc, Cb, Vla, Vln II, Vln I)

**Measured.**
- **Double basses and celli, bars 37-44 (pizz.).** No note has a pizzicato envelope.
  - Cb qn 108: the level rises from -70 to -47 dB over 350 ms. It then holds flat (±1 dB) until the MIDI note-off at 1.0 s and only then decays.
  - Over all 17 Cb "pizz" notes, the median time to peak is 600 ms and the median drop from peak to note end is 1.7 dB. Vc pizz notes: 720 ms and 1.0 dB. The same tracks' Sus MAX notes give 80-320 ms and 3-4 dB.
  - So these notes are bowed sustains. A plucked note peaks within about 30 ms and decays at once.

**Cause (measured in the patch files).** Every string KS Master `.oib` has `loaded: true` only on its first six `layerMatrix.rows`, for example Sus MAX, Sus Marc LITE, Leg Slur MAX, Staccatissimo, Stac On Bow, Marc Shrt.
- The other articulations have `loaded: false`, `active: false`. Their `articulations.trigger` entries also have no `useKey` and `triggerName: "None"`.
- The HO manual (p. 98, Articulations sub-page) says the 1st Violins KS Master has 6 active articulations by default.
- `build_reaper.py state_for()` loads mic columns but never rows. Opus ignores a keyswitch to an unloaded articulation and keeps playing the current one.

These articulations are used but not loaded:
- Pizz RRx4 / Pizzicato RRx4 in Vla, Vc and Cb.
- Tremolo in Vln I, Vln II, Vla and Vc.
- Flautando in Vln II.

What the listener hears instead:
- Bars 37-44: the "pizz." basses and celli are bowed.
- Bars 41-44: the viola's pizz. eighths are detached arco notes from Leg Slur MAX.
- Bars 37-40: Vln II plays plain Sus MAX where the score has div. sul tasto pp.
- At the climax (Vla bars 61-64; Vln I, Vln II and Vc bars 63-64), every string tremolo is a plain sustain. This is inferred from the same mechanism; the stems give no clear amplitude-modulation difference for tremolo with 16 players.
- c01's "pizzicato onsets are clean" note was wrong.

**Fix in `tools/build_reaper.py`, `state_for(tr)`.**
- Build the set of articulations the track uses: `tr["art_counts"]` keys plus `tr["first_art"]`, plus any articulation adopted in finding 3.
- For each one, match case-insensitively (the cor anglais row is "Sus Max", not "Sus MAX"). Then set:
  - `row["loaded"] = True` and `row["active"] = True` in `inst["layerMatrix"]["rows"]`;
  - `trig["useKey"] = True` on the matching `inst["articulations"]["trigger"]` entry. Keep its `key`, and copy a `triggerName` pattern from a loaded row if Opus needs one.
- Leave unused rows unloaded, to save RAM and streaming.
- Render, then check with `pz.py`. Pizz notes should peak within 60 ms and drop at least 6 dB within 400 ms.
- If Opus still ignores the keyswitch, move the pizz and tremolo notes to tracks with the single-articulation patches, for example `Basses/02 Short/...Pizz...oib`.

## 2. Legato transitions in strings and horns arrive 270-350 ms late, with a 4-6 dB hole after each slurred join

**Measured with `xover.py`.** Median time from the MIDI onset to the new pitch winning:

| Track | Median lag (ms) | p25-p75 |
|---|---|---|
| Vln I | 285 | 221-460 |
| Vln II | 275 | |
| Vla | 222 | |
| Vc | 310 | |
| Hn 1 | 310 | |
| Hn 2 | 385 | |
| Ob 1 | 150 | |
| Fl 1 | 112 | |
| CA | 100 | |
| Cl 1 | 115 | |
| BCl | 150 | |
| Bn 1 | 135 | |

- At 52 bpm an eighth is 577 ms, so the slurred string and horn melodies sound about half an eighth behind the harp, pizz. and winds.
- Lag by legato velocity:
  - Vln I: v60 355 ms, v80 270 ms, v100 205 ms.
  - Vla: v80 310 ms, v100 195 ms.
  - The bar 37-40 viola triplets (333 ms notes) still arrive about 195 ms late.
- `dip2.py`, median level of Vln I legato joins relative to the 200 ms before the join:
  - 0 dB up to +100 ms;
  - -4 to -6 dB from +125 to +300 ms;
  - back by +350 ms.
- Vc stays at -4 dB from +250 ms. Fl 1 shows -2 to -3 dB.
- So each slurred violin note has a short hole before the new pitch fills in.

**Inferred from the patch files.**
- The KS Masters' `EWSO` filter has `legato_speed_active: false` and `RTKiller` has `active: false`. The dedicated `1st Violins Leg Slur MAX.oib` and `1FH Leg Slur Accent MAX.oib` have both `true`.
- `LegatoSpeed` maps velocity 30-127 to a sample start offset of 0-4800 samples (`START_MIN`/`START_MAX`). The highest velocities skip the most transition, about 100 ms.
- HO manual pp. 90-91: velocity 110-127 gives the shortest transition, and in True Legato velocity does not change loudness.

**Fix.**
- **(a) `build_reaper.py state_for()`.** For KS Masters with a Leg row, set `EWSO.legato_speed_active = True` and `RTKiller.active = True`, as in the dedicated Leg Slur MAX patches.
- **(b) `score_to_parts.py`, velocities block.** Set legato-target velocity for strings and horns:
  - 120 for notes under 0.9 s;
  - 105 for longer notes.
  - Winds keep the c01 table.
- **(c) New step after the note-length loop.** Move every `leg_target` note earlier by `lag - 60 ms`, using the lag re-measured after (a) and (b).
  - Starting values: strings 0.14 s, horns 0.20 s, winds 0.05 s.
  - Convert to qn with the local tempo: `s * bpm / 60`.
  - Also pull back the previous note's end so the 0.04 qn overlap is kept.
  - Never move a note earlier than the previous onset plus 50% of the previous note's length.
  - Do not move the first note of a slur.
- Then rerun `xover.py` and `dip2.py`. Target: string and horn median lag 60-120 ms, and the Vln I join dip no deeper than -2 dB.

## 3. Slur boundaries and unslurred connected string lines break the line; Leg BC MAX is in every upper-string KS Master and unused

**Measured with `dip.py`.**
- Strings where one slur ends and the next begins (the note is cut 0.05 qn and re-attacked): median dips are Vln I -12.1, Vln II -8.7, Vla -8.0 and Vc -9.5 dB.
- Unslurred notes that join with no gap: Vln I -8.0, Vla -9.4, Vc -4.0 dB.
- Number of such joins:

  | Track | Unslurred, connected | Slur boundaries | Leg/Sus keyswitch flips mid-line |
  |---|---|---|---|
  | Vc | 40 | 15 | 10 |
  | Vln II | 17 | 24 | 16 |
  | Vla | 12 | 30 | 6 |
  | Vln I | 6 | 17 | 13 |

- Examples:
  - Vc bars 15-23 and 49-55, the con sord. pp quarter-and-half lines;
  - Vln II, Vla and Vc bars 46-51;
  - the cantabile phrases at 54-59 and 73-81.
- The Leg/Sus flips switch an unslurred note in a melody to Sus MAX: Vln I/II at 23.67, 24.33, 27.67, 28.33, 71.67, 72.33, 75.67, 76.33.
- The score asks for slurred groups joined by bow changes, and for connected separate bows in "change bow at will" / "molto sostenuto" passages. It never asks for gaps.
- HO manual section 2.1.4 (Articulations) lists Legato Bow Change for these sections. The keys are Leg BC MAX: Vln I 48, Vln II 45, Vla 42, Vc 88.

**Fix in `score_to_parts.py build_track()`, family == "string".**
- A monophonic note that joins the next note (gap under 0.1 qn, different pitch) gets `Leg BC MAX` with the 0.04 qn overlap when:
  - it is unslurred, or
  - it ends a slur and the next note starts another one.
- Keep `Leg Slur MAX` inside slurs.
- Stop sending Sus MAX for single unslurred notes in a monophonic line. Leg Slur MAX already plays its sustain layer for disconnected notes (manual section 2.1.3, the Leg Slur MAX description: disconnected notes select the sustain articulation).
- The keyswitch between Leg Slur and Leg BC then falls on the overlap note. Place it at `q - 0.02` qn.
- Leg BC must be loaded (finding 1).
- Basses have no Leg BC. Leave Cb as it is: its unslurred join dip is only -2.8 dB.
- Check with `dip.py`. Target: boundary dips of -3 to -5 dB, which should still read as a bow change.

## 4. "sul D / sul A / sul G / sul C" are not rendered; HO has a Finger Position control for exactly this (CC70)

**Measured / from the manual.** The HO manual (pp. 92-95, tables read from the PDF page images) says CC70 picks the string:

| CC70 value | Finger position |
|---|---|
| 0-38 | FP1 |
| 39-76 | FP2 |
| 77-114 | FP3 |
| 115-127 | FP4 |

- Higher FPs move a note to a lower string, and the manual calls FP4 "warmer, more emotional".
- Every string KS Master has the `FingerPosition` filter at 0 (FP1), mapped to CC70.

The printed passages:
- Vln I and Vln II sul D, bars 22.67-26 (qn 65-78), pitches 63-75. FP4 keeps all of them on the D string, which goes up to MIDI 75 at FP4.
- Vln I and Vln II sul A, bars 52.75-56 (qn 171-188), pitches 70-78. For the A string:
  - FP1 for pitches ≤ 74, because at FP2-4 the pitches 70-72 move to the D string;
  - FP4 for 76-80.
- Vln II sul G, qn 218-220 (pitches 61-62): FP4.
- Vln II sul D, bars 70.67-74 (qn 237-250), pitches 63-75: FP4.
- Vla sul C, bars 65-70 (qn 220-238) and from bar 87 (qn 286), pitches 51-55: FP4. The viola's G 55 is on the C string at FP2-4.

**Fix in `score_to_parts.py`.**
- Add a `cc70` lane for strings: 127 while a `sul D|G|C` text is in force, until `ord.` or `unis., ord.`.
- For sul A use per-note values: 20 for pitch ≤ 74, 127 for 75-80.
- Send each change at the note's keyswitch time (`early_time`).
- `build_reaper.py` writes it like cc15.
- The effect on sound is inferred; there is no stem difference to measure yet.

## 5. Divisi lines are played as full-section chords, which takes the upper line off legato

**Measured in parts.json.**
- Vc div. bar 18 (qn 51-54) and bar 22 (qn 63-66): the slurred upper cello answer and the held lower note are simultaneous notes. So both go to Sus MAX: the polyphony check is correct, but the upper slur loses its legato.
- Vla div. bars 23-36 and Vln II div. bars 37-44 also go to Sus MAX or Flautando chords. Each line sounds with the full section, so the div. passage is twice as thick as written (inferred).

**Fix.**
- Add a second track per divided section that loads the DIV B KS Master. The files exist:
  - `Celli Divisi/06 Keyswitch/Celli KS Master DIV B.oib`;
  - `Violas KS Master DIV B.oib`;
  - `2nd Violins KS Master DIV B.oib`.
- Switch the main track to DIV A for the div. spans only (bars 18, 22 for Vc; 23-36 for Vla; 37-44 for Vln II).
- Split notes in `score_to_parts.py`: at each onset inside a span, the highest note goes to B and the rest to A. Each part then runs its own Leg Slur logic.
- Give DIV A/B the parent's mix.json entry with gain -3 dB each.
- Lower priority than findings 1-4. Cello bars 18 and 22 gain the most.
- The same 1st Violins DIV A patch, a half section, is the closest thing on the drive to the Vln I solo at bars 17-22 (qn 48-65). This is inferred and optional.

## 6. Horn 3 con sord. (bar 87, qn 286): the 1FH KS Master has an Opus Con Sordino script

**Measured in the patch file.** `1FH KS Master.oib` has the `ConSordino` filter (`conSordino: false`), mapped to CC15, the same script the strings use. c01 left the mute out because there is no muted-horn sample set.

**Fix.** Send CC15 = 127 on Horn 3 in the rest before qn 286, and 0 at the next senza or at the end. Extend the `cc15` block in `score_to_parts.py` to family "brass", keyed on the "con sord." text.
- This is an emulation (inferred: a filter, as for the strings). It is still closer to the printed colour than an open horn.
- Do not substitute Stop Sus (agreeing with c01).

## Do not touch

- The slur-scoped 0.04 qn legato overlap, and the polyphony check: 0 chord onsets on legato patches, no slurred leap over an octave.
- Breath shortening, the tenuto separation and +5 bump, and the accent handling. Tbn1 at f/ff uses Sus Accent MAX, which is loaded.
- Repeated-pitch re-attacks.
- Timpani: the felt-stick KS patch, all five articulations loaded, rolls on Rls, ties merged into single roll notes.
- Harp Sus RR with velocity dynamics and the separate harmonics track.
- Clarinets on Sus Non Vib.
- Keyswitches placed in rests.
