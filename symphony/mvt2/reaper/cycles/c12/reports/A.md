# Cycle 12, critic A: articulation and phrasing (on the cycle 11 render)

Scripts are in `/private/tmp/claude-501/mockup-loop/c12-A/`. They are the c11 set plus these new ones:
- `pizz.py`: the peak and attack time of each pizz. note.
- `bccmp.py`: the join dips of Vln II, Vla and Vc in c10 and c11, for the joins whose articulation changed.
- `pitchtrack.py`: energy at chosen MIDI pitches over time (43 ms windows, 10 ms hop).
- `upbeat.py`: pickup-to-downbeat body levels.
- `breath.py`: the level dip at every breath mark.
- `longs.py`: level per second on held notes of 6 s or more.
- `harpoff.py`: harp decay after note-off.
- `gaps.py`: gaps and overlaps between consecutive notes, by articulation.

Run them with `CYC=11 ~/.venvs/claude-composes-reaper/bin/python`. Levels are dB re full scale on the c11 stems after the envelope fix. Onsets are score onsets (`sq`). build/parts.json (16:23) is the data that made this render.

## Checked and working (measured)

- **Chords and slurs:** no chord goes to a legato patch. Every slurred note is on a legato articulation, apart from the intended exceptions:
  - Ob1 208 and CA 157: portato Sus.
  - The viola sextuplets: short_sus.
  - The Vc div. at 51-52 and 63-65.
- **Breath marks:** 26 of 28 breaths make a 12-39 dB dip in their stem. The exceptions are Horn 1 qn 196 (1.2 dB) and qn 265 (7.6 dB). At f, the horn's release and hall tail fill a 0.19-0.25 s gap.
- **Held notes:** "change bow at will" pedals and the final chord hold steady with no loop artefacts. This covers 18-26 s notes in Vln II 286, Cb 220/271/292 and Vc 274: each sits within ±2 dB of its CC11 plan per second.
- **Harp:** note-offs do not damp the harp. Decay after note-off is 2-10 dB/s, the same as before it, so the harp rings through its rests as it should.
- **Con sordino:** the CC15 spans match the score. Vln II/Vla/Vc are muted from the rest before qn 42, Cb before qn 60, and Vln I's tutti from 65. All are off before the "senza sord." at 108; the solo track stays open.
- **Viola triplets:** the slurred triplets in bars 37-40 and 57-58 are clear. Each note's own pitch dominates 78-82% of its slot.

## 1. The pizzicato pitch trims reach full depth a quarter-beat late, so they cut the following note instead of the hot one (Violas, bars 41-44; Vc and Cb pizz., bars 37-44). Measured.

**Where:** the Violas pizz. eighth-note figure under the cor anglais "solo, dolce cantabile" (qn 124-138). `pitch_trims.json` Violas, restricted to `Pizz RRx4`:
- F4 (65) -8
- G flat 4 (66) -2
- C4 (54) +4
- E flat 4 (58) +3

**Evidence (data):** the notes are joined, so `trim_shape` starts each trim at the moved onset and ramps over 0.25 qn. The ramp is then sampled on the 0.125 qn envelope grid, with no `vol_bp`. The envelope value at each pizz. attack (read from parts.json `vol_db`):

| Note | Intended trim | Envelope at the onset | Full trim reached at |
|---|---|---|---|
| F4 at 124.67 / 128.67 / 131.67 | -8 | -1.8 / -2.5 / -2.5 dB | onset + 0.25 qn (124.917 etc.), just before the next note |
| Following note at 125.0 / 129.0 / 132.0 | 0 / +3 / +4 | -3.0 dB | |

**Evidence (audio, `pizz.py`):**
- Peak median over the 42 pizz. notes: -38.8 dB.
- F4 peaks: -30.7 and -29.8, which is 8-9 dB hot.
- The notes after an F4 have a median peak of -44.3, 5.5 dB under the median.
- C4 still has a median of -42.6.
- p10-p90 spread: 8 dB. The largest note-to-note jump is 14.5 dB.
- c10 is identical, so the c08 trims never worked.

The same mechanism hits the other pizz. trims:
- Vc B flat 2 (-5) sits at -2.0/-2.8 at its two onsets, and its peaks are +3/+5 over the line.
- Cb A flat 1 (-5, all articulations) is at +0.2 and +3.0 at the pizz. onsets 130 and 136.

The c10 learning (a 0.6 s ramp does nothing for a percussion stroke) applies to pizz. too.

**What a listener hears (inferred):** in a soft, even accompaniment, two pizz. notes per bar pop out by about 8 dB and the next note drops away.

**Fix (`tools/score_to_parts.py`, the pitch-trim loop after `trim_shape`, about line 1516):** for a note whose articulation contains "izz", replace the ramped shape with a step that is at full value on the attack.
- The shape is `[(qn_before(q0, 0.03), 0), (qn_before(q0, 0.01), dB), (qn_before(next_onset, 0.03), dB), (qn_before(next_onset, 0.01), 0)]`.
  - `next_onset` is the next note's moved onset; with no following note, use the onset + 0.6 s.
  - `q0` is the moved onset; for pizz. it equals the score onset.
- Append it as an exact item, `("env", shape, True)`, so the breakpoints go into `vol_bp`.
- Keep the table values. They will now act for the first time. Re-fit them after this render, because Pizz RRx4 round-robin variation is mixed in with pitch.

**Check (`pizz.py Violas`):**
- Each pizz. onset's envelope value equals its table value.
- F4 peaks are within ±2.5 dB of the line median.
- No note after an F4 is more than 3 dB under the median.
- The p10-p90 spread is 5.5 dB or less, and the largest jump is under 9 dB.
- Vc 112/122 are within 2 dB of the Vc pizz. median.

## 2. The c11 bow-change rule (BC_SOFT) helped the violas but left Violins II and the celli with more holes: choose the articulation per join from the two renders. Measured.

**Where:** the soft pp-p unslurred lines in bars 16-22, 46-51 and 71-75. Jointly they are the accompaniment under the solo violin and the cor anglais.

**Evidence (`bccmp.py`):** the same holes metric on c10 (Leg BC MAX, with the old bcsoft dip) and c11 (Leg Slur MAX plus notch) for every join that changed.

| Section | Joins | c11 median | Joins of 7 dB+ in c11 | Note |
|---|---|---|---|---|
| Violins II | 20 | 6.4 | 7 | |
| Violas | 15 | 3.1 | 1 | Long targets 6.5 -> 3.0 |
| Violoncellos | 31 | 5.8 | 11 | |

Joins where Leg BC measured at least 1.5 dB better in c10 (c10 -> c11):

| Track | Joins |
|---|---|
| Violins II | 48 (0.5 -> 3.1), 54 (0.9 -> 5.5), 57 (0.1 -> 3.5), 146 (4.7 -> 9.5), 154 (6.7 -> 10.8), 159 (3.8 -> 7.2), 271 (0.5 -> 2.6) |
| Violas | 159 (4.0 -> 7.9) |
| Violoncellos | 45 (4.1 -> 8.4), 50 (7.1 -> 8.9), 60 (1.1 -> 4.9), 62 (3.8 -> 6.9), 132 (5.7 -> 7.9), 144 (3.8 -> 7.1), 160 (7.5 -> 9.7), 220 (1.5 -> 3.9) |

The c10 Leg BC values on targets of 1.4 s or more include the old bcsoft dip, which made them worse (c11 A #1). Leg BC with `BCSOFT` depth 0 should therefore measure at or below them (inferred).

Taking the better articulation per join gives:
- Violins II: median 6.4 -> 5.0, joins of 7 dB+ 7 -> 4.
- Violoncellos: median 5.8 -> 4.6, joins of 7 dB+ 11 -> 8.

**Fix (`tools/score_to_parts.py`, the BC_SOFT test in the Leg BC block):**
- Add `BC_SOFT_SKIP = {"Violins II": [48, 54, 57, 146, 154, 159, 271], "Violas": [159], "Violoncellos": [45, 50, 60, 62, 132, 144, 160, 220]}`. These are target score onsets, matched within 0.01 qn.
- A listed join stays Leg BC MAX, with `BCSOFT` depth still 0.
- Do not list Vc 87/172/271. Leg BC made a bump there (-2.2/-0.7/-1.7).
- Do not change the viola joins that improved.

**Check (`TH=6 holes.py "Violins II,Violoncellos"`):**
- Each listed join is at or under its c10 value.
- No new join of 7 dB or more appears in bars 16-22 or 46-51.
- `bump.py`: after-minus-before is +3 dB or less on the reverted joins.

## 3. The portamento trial works: extend it to the other strings at the same two leaps. Measured (glide); inferred (musical gain).

**Evidence (`pitchtrack.py`, energy at the intermediate semitones within 0.25-0.5 s of the leap):**

| Join | Intermediate pitches | c10 (Leg BC/Slur) | c11 (Leg Port) |
|---|---|---|---|
| Vln I qn 82, F5 -> B flat 5 | G5 / A flat 5 | -11 / -18 | +2 / +2 |
| Vln I qn 172, C5 -> F5 | D5 / E flat 5 / E5 | -13 / -19 / -11 | -6 / -4 / -1 |

- At qn 82 the glide occupies about 0.30-0.44 s after the measurement start: it begins at the moved onset and ends at the score onset. That is a 0.12-0.15 s slide about 12-15 dB under the source note, which is a discreet, idiomatic shift.
- Violins II plays the same F5 -> B flat 5 at qn 82 on Leg BC, and its intermediate pitches stay at -15 to -35 (no slide). The two sections now play the same "sul D" shift differently.
- The port joins have no hole (82: 3.0 dB).

**Fix (`score_to_parts.py` `PORT_TARGETS`):**
- Add Violins II [82.0, 172.0]: the same leaps in unison with Vln I, "sul D" and "sul A".
- Add Violoncellos [83.0]: A flat 3 -> D flat 4 in the cantabile.
- Use target velocity 100, as for Vln I.
- Vln II and Vc need a full track rebuild, so their Leg Port rows load (key 46 for Vln II, 89 for Vc).
- Do not add any more leaps this cycle.

**Check (`pitchtrack.py`):**
- At Vln II 82, the intermediate pitches rise by 10 dB or more over c11.
- At Vc 83, a B flat 3 / B 3 / C 4 rise within 0.2 s before the score onset.
- `holes.py` dips at these joins are 5 dB or less.

## 4. The violins' pickup into bar 53 is louder than the downbeat it leads to (qn 171 -> 172). Measured.

**Score:** bar 52 beat 4, Vln I and Vln II "p, senza sord., sul A" enter with a C5 pickup slurred to F5. The F5 starts a < > hairpin to mp.

**Measured (`upbeat.py`):**
- Downbeat body minus pickup body:
  - Vln I: -5.5 dB (c11), -5.1 (c10), -5.0 (c09).
  - Vln II: -3.1 dB.
- The CC11 is the same on both notes (46), and there is no vol_db shaping there.
- So the C5 pickup sample (with its 0.19 s entry lead) is simply hotter than the F5. The phrase arrives on a weaker note and then crescendos from below where it started.

The other pickup-downbeat inversions found (bars 30, 82) sit inside printed diminuendos and are left alone.

**Fix (`build/roles.json`):**
- Violins I [170.4, 171.9, -4] and Violins II [170.4, 171.9, -2.5]. Each starts in the preceding rest, so it is at full value on the pickup's attack, and must be released before the leg-port target's moved onset (171.85).
- If the role ramp does not allow that, use a 0.2 qn ramp out, or lower the pickup's CC11 by 5 to 41 on these two tracks.

**Check:** `upbeat.py "Violins I,Violins II" 0` gives a downbeat-minus-pickup of 0 to +2 dB on both tracks at 172.

## 5. The viola sextuplets in bars 59-60 are still a blur: test a different articulation on a short range. Measured problem; the fix is a test.

**Measured (`dom.py Violas 196 204 11`):**
- Each sextuplet note's pitch dominates only 26% of its own slot (median).
- The triplets of bars 57-58 on Leg Slur MAX reach 78%.
- c11 C #6 (detaching the Sus MAX notes) changed nothing (0.27 -> 0.26).

The notes are 0.16 s long, and Sus MAX attacks take about 0.1-0.2 s to reach body, so no note is fully established before the next one starts (inferred).

**Fix (test first):**
- Render qn 194-204 on the Violas track three ways, in one restart, from the existing KS Master rows:
  - (a) the current short_sus.
  - (b) Detache (key 30, separate bows; it is designed for fast détaché attacks) at v100, notes ending 0.01 qn before the next.
  - (c) Leg Slur MAX at v127 with no lead (`LEG_LEAD_S` off for notes under 0.2 s), one slur per beat.
- Keep whichever gives the highest `dom.py` own share.
- Detache plays every note on a new bow while the score slurs each group of six. At f in a tutti that is acceptable if it is the only way to make the pitches heard.

**Check:** median own share of 0.5 or more, and the bar 59-60 viola stem level within 1.5 dB of c11.

## 6. Violins I reach the bar 79 ff downbeat late after the three-note grace run (qn 262). Measured, minor.

**Measured (`dom.py`, first sustained dominance of B flat 6 after the run):**

| Track | Target dominates at |
|---|---|
| Violins I | +0.105 s |
| Violins II | +0.025 s |
| Flute 1 | +0.030 s |

The three tracks play the same after-grace run into the climax arrival.

- Vln I's target starts at 261.860, a 0.14 qn lead. Vln II's starts at 261.835, a 0.165 qn lead (`LEG_LEAD_S` 0.17 against 0.20 s).
- In 50 ms frames, Vln I rises from -38 to its ff body (-31) only by about +0.35 s.

**Fix:**
- `build/leg_leads.json` Violins I {"262": 0.05}.
- Check in parts.json that the three grace notes (261.638/261.712/261.786) move with the target. If they do not, move them by the same 0.04 qn in the grace placement.

**Check:** Vln I target dominance at +0.05 s or earlier, and the grace notes still each dominate 80% or more of their slots.

## Do not touch

- Leg Port on Vln I 82/172: the glide is audible and has no hole.
- The `BC_SOFT` viola joins. Long viola targets went from 6.5 to 3.0 dB.
- The breath gaps: 26 of 28 make clear dips.
- Harp note handling: it rings through its rests. Also the harp rolls and the harmonics octave.
- The CC15 sordino spans.
- The same-pitch merges and notches, the tie handling, and the held-note sustains.
- The viola triplet legato.
- The Tbn1 accent shapes.
- `hold_s` early fills.
- No chords on legato patches, and keyswitches in the preceding note or rest.
