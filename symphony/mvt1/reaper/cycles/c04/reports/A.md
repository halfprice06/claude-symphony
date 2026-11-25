# Cycle 4, critic A: articulation and phrasing (render c03)

Scope: every wind, brass, string, timpani, harp and percussion note in `build/parts.json` (the c03 build, roles after the stem fix), measured on the c03 post-fader stems and master. c03 is the first render on a correct time map, so `q2s()` from parts.json is used directly. Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c04-A/`:
- `feat.py`: per-stem 5 ms frames with power, 100-300 Hz, 2-5 kHz, 1-8 kHz and spectral centroid.
- `acc2.py`: accents, with the 2-5 kHz band normalised per second. c03-A's `accs.py` divided band energy by window length once too few times, which biased an 80 ms attack about 9 dB low against a 600 ms body.
- `longloop.py`, `cfold.py`: loop pulse.
- `rebow.py`, `joins.py`, `ten.py`, `merged.py`, `pulse2.py`, `breath.py`, `slurs.py`, `trace.py`.

## Checks that passed (measured)

- **Accents, weight not bite.** 2-5 kHz energy in the first 80 ms minus the note body, median per track:
  - strings -1.4..-5.3 dB;
  - brass -3.3..-17.6 dB;
  - winds -4.4..-11.2 dB.

  The positive outliers are artefacts: a brighter previous note was still sounding in the attack window (Bassoon 1 536 +14.3, Violas 536 +12.2). The only real one is Horn 1 qn 665 at +4.5 dB, an ff accent on Sus MAX inside a slur in bar 167; it is minor.
- **Accent level.** The accent sits over the note before it by a median +1.7..+4.8 dB. At accents, the master's 2-5 kHz jump over the 0.3 s before has a median of 0.0..+1.6 dB per track. The 4-7 dB cases are all tutti entries after rests.
- **Legato structure.**
  - `ks_clash` is empty on every track.
  - No legato-row note overlaps another pitch by more than 0.12 qn.
  - Every wind and brass slur target is on a legato row, except the slurred tenutos (finding 2).
  - Median join dip per track is 1.0-4.1 dB.
- **Pizzicato.** Basses (36 notes) and celli (3) start at -0.007 / +0.010 s against the score and decay 11-13 dB in 0.4 s.
- **Re-bows.**
  - Median 80 ms dip per section is -1.1..-3.3 dB.
  - The master's median dip at re-bows is -1.7..-2.1 dB, against control times at -1.6..-2.2 dB.
  - The worst cases are listed in finding 4.

## 1. Unslurred repeated string notes are merged into one held note: the cellos' written-out accelerando before the recapitulation plays as a sustained G (bars 127-130, and about 100 notes elsewhere)

**Score.** At qn 504-520 (dev.ily line 367-368) the celli play repeated G2s: quarters at pp, then eighths, then triplets at mf, then sixteenths at f with a crescendo, into the recapitulation at bar 131. The timpani and basses hold G under it, so this written acceleration is the only rhythmic motor of the retransition.

**Measured (parts.json).** The 48 written notes became 3 notes: 504.0 (4.13 qn, Leg Slur MAX), 508.157 (5.30 qn, Sus MAX) and 513.49 (6.51 qn, Sus MAX).
- The cause is the c03 (A #1) merge loop in `tools/score_to_parts.py` (about lines 1354-1385). Each unslurred note is put on a legato row (Leg BC/Leg Slur), so the merge treats it as a "repeated pitch in a legato string line".
- The merged note then gets automatic re-bows at 508.157 and 513.49, unrelated to the rhythm.
- The written notes survive only as a CC11 sawtooth (about 12 CC per sixteenth).
- In bar 130, a re-bow hold also pulls the crescendo down: `vol_db` is -8 to -9 dB across 516.5-520.

**Measured (stems, per-note level max minus min).**

| Bar | Written notes | Celli | Comparison |
|---|---|---|---|
| 128 | eighths | 4.3 dB | |
| 129 | triplets | 3.4 dB (p25 1.7) | |
| 130 | sixteenths, f | 1.1 dB (p25 0.7) | the basses' held G1 in the same bar: 0.9 dB |

- So the sixteenths are not distinguishable from a held note.
- The celli are the loudest stem in bar 130 (-6.3 dB under the master), so this is exposed.
- For contrast, the basses' separately played Sus MAX quarters in bars 23-25 measure 7.4 dB per note.

**The same merge also applies elsewhere (measured).** Written unslurred repeats of 1.5 qn or less merged into longer notes:

| Track | Notes | Bars |
|---|---|---|
| Violins I | 2 | 62, 158 |
| Violins II | 18 | 23-25, 62, 135-137 |
| Violas | 43 | 21, 23-25, 98-100, 111-116, 126, 135-142 |
| Violoncellos | 41 | 12, 127-130, 165 |

Where the notes are quarters or eighths at mf, the 14 CC notches still give 6-7 dB per note (bars 23-25). The loss is in the fast notes and in the accents' re-articulation, for example Violas 536-538 (three E♭ quarters, the first accented).

**Fix** (`tools/score_to_parts.py`, the merge loop):
1. Do not merge when both notes are unslurred (`n["slur"] is None and o["slur"] is None`), the written note is 1.5 qn or shorter, and the tempo is 100 bpm or faster.
   - Keep the merge for slurred repeats, ties, printed bow marks and the slow Lento whole notes (the kit's 7-15 dB Leg Slur re-attack holes).
2. Articulation for these split notes:
   - **Notes of 0.4 s or longer:** Sus MAX fresh strokes (the c02 `STR_ACC_AFTER_SUS` path).
     - End each note `min(0.04 qn, 10%)` early.
     - Velocity from `REBOW_VEL_BY_CC` at the printed level.
   - **Notes under 0.3 s (triplets, sixteenths):** the Stac row the track already loads (Violoncellos/Violas/Violins II `Stac RRx9`, Violins I `Stac RRx14`).
     - Play at the written length minus 0.02 qn.
     - Velocity by the dynamic curve (mf about 80, f about 96, rising through the hairpin).
     - Keep CC11 as the dynamic.
     - Write no notches.
   - No new rows are loaded, so this is `--midi-only`.
3. Short notes are no longer re-bowed, so the re-bow shapes keyed at Violoncellos 508.157 and 513.49 in `build/rebow_fills.json` must be dropped. Their -9 dB hold goes with them.
4. Optional, same rule: Violoncellos `g,1:16` at bars 117-121 (qn 464-484) is a measured sixteenth tremolo printed f, played on the unmeasured `Tremolo` row.
   - The celli sit 14-16 dB under the master there, so this is inferred to matter much less.
   - Expand `:16` (tremolo value 16 or larger at 100 bpm or faster) into written sixteenths with the same treatment.
   - Do not use `Meas Trem TS`: it is recorded at 145 bpm (read from the .oib), and the manual (p. 52) advises staying within ±10 bpm.

**Pass criteria (c04 render).**
- Celli, bar 130: per-sixteenth max-min of 4 dB or more (c03 1.1).
- Celli, bar 129: per-triplet max-min of 5 dB or more (c03 3.4).
- Bar RMS within ±2 dB of c03 for bars 127-130 (-43.1 / -46.8 / -40.7 / -31.0).
- 2-5 kHz attack minus body of the new short notes at 0 dB or lower.
- Violins II/Violas bars 23-25 per-quarter max-min stays at 6 dB or more.

## 2. Horn 1's slurred tenutos in the dolce second-theme solo are re-tongued on Sus MAX and jump 8-9 dB (bars 48, 51, 148, 151)

**Score.** tTwo.ily line 36, `aes4\! f'2--\< es'4\!)`: the F4 is a tenuto inside the slur, a leaning portato at the top of the phrase. The cellos play the same melody an octave below (Hn 1/Vc melody).

**Measured** (`ten.py`; body at +0.1..+0.5 s minus the last 0.2 s of the previous note):

| Onset | Horn 1 | Celli on the same note (Leg Slur MAX) |
|---|---|---|
| qn 189 | **+9.4 dB** | -0.4 dB |
| qn 589 (recapitulation) | **+8.1 dB** | +6.0 dB |
| qn 201 | +3.9 dB | |
| qn 601 | +1.7 dB | |

- The rule at `score_to_parts.py` lines 1276-1278 (c04 A #4, "a tenuto inside a slur is tongued") plays every slurred tenuto on Sus MAX at velocity 63, with a 0.07 qn break before it.
- The c07 joined-portato path exists but only for `family == "wind"` inside `SOSTENUTO_SPANS`, which is empty for movement I.
- Inferred: most of the jump is the level difference between the two rows (Sus MAX against the Leg Slur MAX sustain at one CC11; kit section 6: 3-9 dB). Only about 1.5 dB comes from the +5 CC tenuto bump.
- Inferred: heard as a tongued accent at the expressive leap of a dolce horn solo, sticking out of the horn/cello unison. A horn leaning on a slurred tenuto rises about 2-4 dB.

**Fix.**
- Add `PORTATO_JOIN_AT = {"Horn 1": [189.0, 201.0, 589.0, 601.0]}` to `build/score_config.py`.
- In the slurred-tenuto branch of `score_to_parts.py`, let a listed onset take the c07 joined path for brass as well as winds:
  - Leg Slur MAX target, velocity `SOST_VEL` (100);
  - `SOST_NOTCH` (10 CC) portato notch;
  - the normal legato lead and overlap, no break.
- Keep the +5 CC tenuto bump. This is `--midi-only`.

**Pass criteria.**
- Horn 1 at 189 and 589: +1..+4 dB over the end of the previous note.
- No join dip over 5 dB at these four onsets (80 ms window).
- Horn 1 stays within 2 dB of its c03 level over bars 47-52.

## 3. The long timpani rolls cycle in tone colour at their loop period; the opening roll is the movement's first sound (qn 0-16, 48-56, 720-728)

**Measured** (`longloop.py`, `cfold.py`, timpani stem; 0.25 s frames over the 19.2 s opening roll):
- The level is flat: -48.2 ±0.3 dB from 4 s on. The c03 loop profile works for level (swing 1.6-1.9 dB).
- The spectral centroid dips from about 400 to 335-345 Hz every 3.48 s (minima at 3.25, 6.75, 10.25, 13.75 and 17.25 s), about 250 cents.
- The 1-8 kHz share falls 3 dB (-13.5 to -16.8) at the same moments.
- Autocorrelation at the period:

  | Roll | Centroid | 100-300 Hz |
  |---|---|---|
  | qn 0 | 0.95 | 0.89 |
  | qn 48 | 0.89 | 0.90 |
  | qn 720 | 0.92 | 0.63 |

- Exposure: in bar 1 the timpani (-46.2 dB) sit level with the celli (-45.4 dB), and the roll is 9.7 dB under the master. Bars 1-4 have little else.
- Inferred: a slow, regular darkening every 3.5 s on a ppp roll at the opening of the movement: Dan's "bowing" effect, on the timpani. A level profile cannot remove it (kit LEARNINGS 6).

**Fix as a test** (`score_to_parts.py`, timpani branch; new `TIMP_ROLL_RESTRIKE = {"min_s": 6.0, "seg_s": (2.5, 3.3)}`):
- Split rolls longer than 6 s into abutting same-pitch Timpani Flt Rls notes. Each piece is 2.5-3.3 s, drawn at irregular lengths so no piece completes a 3.48 s loop.
- Each old piece ends exactly at the next onset (no same-pitch overlap). Velocity and CC7 stay unchanged.
- Remove the `build/loop_profiles.json` entries for Timpani 0 and 48 on the test notes.
- Apply to qn 0 and 48; qn 720 stays as the control.
- If a re-strike bump shows, put a -1.5 dB, 0.15 s dip in the volume envelope at each new piece.
- Fallback if the same-key retrigger misbehaves: alternate the pieces onto an appended "Timpani roll B" track on the same patch, with 0.3 s volume crossfades.

**Pass criteria.**
- Centroid autocorrelation at 3.2-3.8 s under 0.4 on rolls 0 and 48.
- Folded 1-8 kHz share swing 1.5 dB or less.
- Level step at each new piece within ±1.5 dB.
- No 2-5 kHz attack over the roll body at the new pieces.

## 4. The remaining legato and re-bow holes to target in the planned refits (all families)

**Measured.** Legato joins with a dip of 6 dB or more (`joins.py`, 80 ms window, against the lower of the two bodies):

| Track | Onset (dip) |
|---|---|
| Horn 2 | 453 (9.8 dB), 266 (6.5) |
| Violas | 440 (7.8, Leg BC), 180, 378, 517 (6.0) |
| Violoncellos | 365 (7.7), 685 (7.5, the coda solo), 8.0 (7.3, Lento), 112 (6.8) |
| Violins I | 720 (7.5, final chord), 636 (7.2, the fff arrival), 279 (7.0) |
| Violins II | 234 (6.3), 245 (6.2), 637 (6.0) |
| Clarinet 1 | 213 (7.2, bar 54) |
| Flute 2 | 633 (6.2) |
| Oboe 1 | 540 (6.0) |

**Measured.** Worst re-bows (`rebow.py`):

| Track | Re-bow qn | Stem dip | Step 1-2 s after | Master dip | Note |
|---|---|---|---|---|---|
| Double basses | 297.045 | -9.0 dB | | | |
| Violoncellos | 163.877 | -8.0 dB | -7.4 dB | | |
| Violas | 725.52 | -7.6 dB | | -3.9 dB | final chord |
| Violins II | 28.878 | -7.3 dB | | -4.7 dB | bar 8, Violins II the loudest stem; Lento control master dip median -1.8, p10 -4.4 |
| Violoncellos | 39.879 | | +9.3 dB | | |
| Violoncellos | 727.116 | | -8.3 dB | | |

**Fix.**
- The planned `auto_fills.py 3` and `fit_rebows.py 3` passes should cover these. After the run, check this list by name.
- Horn 2 453 and Violins I 636/637 are loud arrivals: check the 30 ms peak (kit section 5 spike rule) before filling.
- Run both passes after finding 1's change, because it removes the re-bows at Violoncellos 508.157 and 513.49.

**Pass criterion.** Every listed join under 5 dB, and every listed re-bow dip under 5 dB with its step within ±3 dB.

## 5. a2 unisons are played by one solo-horn sample plus 3 dB; Hollywood Brass has a recorded a2 horn patch (bars 96-102, 117-121, 158-161, 166-170)

**Measured (parts.json, `unison_dropped`).** The unison copy is dropped and the kept note gets +10·log10(2) dB:

| Track | Notes dropped | Bars |
|---|---|---|
| Horn 2 | 97 | 24-25, 28, 41-42, 62-64, 66-67, 69-72, 78-79, 96-102, 114, 117-121, 133, 137, 156, 158-161, 166-170 |
| Clarinet 2 | 65 | |
| Bassoon 2 | 47 | |
| Trombone 2 | 32 | |
| Trumpet 2 | 23 | |
| Horn 4 | 30 | |

This is the right fix for the 0.999-correlation problem (kit section 8).

**Inferred.** Through the development climaxes and the main fff, the horn line in unison has one player's timbre, louder. A real a2 has two players' small pitch and timing differences, which thicken the tone.

**Fix.**
- Append a track "Horns 1+2 a2" on `.../2 French Horns/06 Keyswitch/2FH KS Master.oib`, with only Sus MAX and Leg Slur MAX loaded (`UNLOAD_UNUSED_ROWS`).
- Route Horn 1's notes in the Horn 1/Horn 2 unison spans to it with `TRACK_WINDOWS`. Use the dropped notes' onsets, so the 3 dB unison boost is not applied there.
- Starting gain: Horn 1 gain +4.6 dB (kit c18 measurement). Set the final gain from this render, with a role.
- Memory: c03 settled at 42 GB after the render. Measure the new instance's settled footprint before rendering and drop the test if REAPER would pass 45 GB.
- Lower priority, same method: Violins II "metà" at qn 184-196 on the 2nd Violins DIV A KS Master, deferred since c01 for memory.

**Pass criterion.** The a2 track's level matches the solo track's c03 level ±1.5 dB per bar in the listed spans, with the accents' 2-5 kHz attack minus body still at 0 dB or lower.

## 6. Harp étouffez is still not implemented (qn 244, 650/654, 727)

**Measured (harp stem).**
- At qn 244 (bar 62, sub. p) the f chord of qn 242 rings at -37.5..-38.6 dB through qn 244.1. It falls to -45 dB only by qn 245.1.
- The new p arpeggio (from -45 dB) sits under that ring for its first beat.
- No rule reads the étouffez text (c03-A smaller item, deferred in c03 because a track-wide dip would cut the new arpeggio).

**Fix.**
- Route the notes sounding before each étouffez mark onto an appended track "Harp (damped)" with `TRACK_WINDOWS`: qn 240-243.99 for the mark at 244, the chord before 650/654, and the final note before 727. Use the same patch file and seat.
- Give that track a volume step of -30 dB over 0.06 s at the mark. The main harp track keeps the new arpeggio untouched.
- Harp Sus RR is a small instance.

**Pass criterion.** At qn 244.0-244.6 the old chord's ring is at least 15 dB under the new arpeggio's notes.

## Smaller items (not ranked)

- **Breaths (measured, `breath.py`).** All marked breaths dip 2.5-19 dB except Horn 1 qn 475 (-2.7 dB, gap 0.143 s, at ff). By kit section 7 this is acceptable at ff; leave it.
- **Wind staccato.** It still speaks later than the strings (c03 test failed). No change proposed.

Do not touch: brass, wind and string `GENTLE_ACCENT` (accent 2-5 kHz attack minus body medians all negative); `STR_ACC_AFTER_SUS`; `DETACH_ACCENTS`; the legato structure, overlaps and keyswitch placement (no clashes, no chords on legato rows); the pizz. rows and timing; the c03 pre-roll meter fix; `TIMP_DELAY_S`; the suspended-cymbal timing; `AUTO_REBOW` and `space_rebows.py` spacing (master re-bow dips equal control); the merge of slurred and tied repeats (keep it; finding 1 only removes it for unslurred fast notes).
