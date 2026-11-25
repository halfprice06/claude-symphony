# Cycle 19, critic C: tempo, timing and transitions (on the cycle 18 render)

Material: `cycles/c18/render` (master and 32 stems), `cycles/c18/metrics`, `build/parts.json` (23:50, the c18 data after the post-render `--mix-only` fixes; tempo map and notes are the rendered ones; copied to scratch as `parts18.json`), `cycles/c18/before` and `c17/before` (the c17 and c16 data), `build/{leg_leads,entry_leads}.json`, `tools/score_to_parts.py`, `v77/global.ily`, `build/mockup-events.tsv`, score page 2 (bars 15-40).

Scripts are in `/private/tmp/claude-501/mockup-loop/c19-C/` (run with `~/.venvs/claude-composes-reaper/bin/python`, `PARTS=parts18.json`). They are c15-C's set plus:
- `legst.py`: legato crossover (as c07/c11/c15) on stereo power spectra instead of the mono fold.
- `rise.py`: direct-onset proxy. The time the new pitch's harmonics that the old pitch does not share reach the note's body - 6 dB.
- `ens.py`: arrival spread at shared onsets. `ioi.py`: inter-onset ratios inside legato lines. `dom2.py`: dominant-pitch trace. `breath.py`: gaps at printed breaths. `secent.py`: section-sum entries.
- The c16 and c17 runs of the same scripts are in `c16/` and `c17s/`.

Delivery (from c18 CHANGES.md, not re-measured): master -22.5 LUFS, LRA 23.6 LU, TP -4.1 dBFS. mp3 -19.8 LUFS, LRA 16.0 LU, TP -1.6 dBTP.

## Where c18 stands (measured)

- **Tempo map.** It matches `global.ily` bar by bar, as in c15:
  - bars 35-36: 49.2 / 45.0
  - bars 53-59: 60.0 rising to 64.0
  - bar 60: 63, 61, 59, then 47.1 with the caesura
  - bars 61-62: 53.2
  - bars 63-64: 50.3 / 42.6
  - bars 78-82: 50.3, 48.7, 45.5, 45.9, 44.0
  - bars 89-92: 48.4, 44.0, 39.9, then 36.8, 35.2 and 20 bpm on the last beat. The final bar lasts 6.3 s.
- **Final release.** The master holds -43..-46 dB until 1.2 s before the release, then fades to -58 at the release. The tail falls -64, -69, -77, -85 dB at +0.25, +0.5, +0.75, +1.0 s, about 26 dB/s. No stem is cut.
- **Keyswitches.** All 255 come before their note's moved start (smallest gap 13 ms, Ob1 207.95) and there are no clashes.
- **Entries** (body - 6 dB, median / p90): winds +0.029 / +0.068, brass -0.020 / +0.063, strings +0.031 / +0.135, harp +0.006, timpani +0.002. Pizz. +0.00..+0.04 s. The new divisi tracks did not make section entries later: the Vla + Vla div sum at qn 66 reaches body - 6 dB at +0.215 s (c17 Vla alone +0.185), qn 277 +0.095 (+0.060), Vln II + div at qn 108 +0.096 (+0.161).
- **Legato medians** (stereo crossover): Vln I +0.018, Vln II +0.018, Vla +0.026, Vc +0.008, Hn1 +0.036, Fl1 +0.023, Ob1 +0.043, CA +0.008, Cl1 +0.048, BCl +0.078.

**The crossover measurement changed with the c17 hall.** The data in c16 and c17 is identical for these notes. Even so, single crossovers moved by up to ±0.15 s with the true-stereo hall:
- Hn1 qn 26: +0.08 → +0.17
- Hn1 qn 34: -0.03 → -0.16
- Hn1 qn 35: +0.15 → +0.02
- BCl qn 91.5: +0.08 → +0.23

The pitch trace at Hn1 26 shows why. In c16 the old pitch fell 15 dB by +0.10 s. In c17/c18 it stays within 3-5 dB of its body until +0.10 s and fades over 0.3 s. That is the hall tail of the old note, not a later new note. The new note's own rise (`rise.py`) did not move: c16 against c18 differ by a median 0.005 s and a p90 of 0.066 s over 349 notes.

**Rule used below.** A note counts as late or early only when the crossover and the rise agree, and only when it was the same on c16. Single-note leads from the crossover alone would now follow the hall. Examples to leave alone:
- Horn 1 qn 18, 26, 30 and 39 (Ab3 targets): crossover +0.14..+0.19, rise +0.07, +0.07 and -0.02.
- BCl 91.5.
- Vln II 164: crossover +0.19, rise -0.015.

## 1. Exposed solo notes are off the beat by 0.12-0.18 s (measured)

Each item gives crossover / rise in c18, then c16 in brackets.

- **Horn 1 lands early on F4 → B flat4.**
  - qn 34 (bar 12 beat 2), the crest of the horn theme, alone over the reeds: -0.16 / -0.15 s (c16 rise -0.175).
  - qn 178 (bar 54.5): -0.13 / -0.135.
  - Cause: `LEG_EXTRA_S["Horn 1"] = {65: 0.15}` adds 0.15 s to every departure from F4. The downward departures arrive on time (184 rise +0.09; 193 crossover 0.00). The upward fourth gets too much.
  - Fix: `LEG_PAIR_EXTRA_S["Horn 1"] = {(65, 70): -0.12}`. Total lead goes 0.25 → 0.13 s at 34 and 0.224 → 0.104 at 178. Expected arrival -0.03..0.
  - Qn 34 carries the c18 loop fill at moved + 0.825 s. It moves with the note, so check the probe's "Horn 1 qn 34 sustain dip".
- **Horn 1 qn 201 (bar 60.25, E flat4 → F4) is late**, in the climb where the cellos and violins are on time: +0.18 / +0.235 (c16 +0.08 / +0.28). Add `"201": 0.10` to `build/leg_leads.json` "Horn 1". The cap allows 0.43 s.
- **Oboe 1 is late on its falling steps** under Vln II's quarter-note beats:
  - qn 47 (bar 16.67, F5 → E flat5): +0.15 / +0.165
  - qn 55.5 (bar 19.5, D flat5 → C5): +0.15 / +0.165
  - qn 143 (bar 45.75, D flat5 → C5): +0.16 / +0.18
  - qn 270 (bar 81.67, D flat5 → C5): crossover +0.13
  - All are the same on c16. Every D flat5 → C5 is late, and the oboe's other joins are +0.00..+0.07. Against Vln II at the same onset the oboe is 0.16 / 0.33 s behind at qn 47.
  - Fix: `LEG_PAIR_EXTRA_S["Oboe 1"] = {(73, 72): 0.10, (77, 75): 0.10}`. The lead goes 0.06 → 0.16 s. Caps: 0.23-0.30 s at 55.5/143/270, 1.0 s at 47. Expected +0.03..+0.07.
  - The ff qn 210 (bar 62.5, F5 → E5) has a rise of +0.305 on both renders with no lead, because it is on the Largamente portato path. If a lead can be applied there, add 0.10. Otherwise leave it.
- **The bass clarinet solo (bars 31-36)** is late at:
  - qn 92.5 (A flat3 → C4, the third note of the opening "es f aes c"): +0.14 / +0.125 (c16 +0.10 / +0.11)
  - qn 106 (bar 36.33): +0.12 / +0.235

  This makes the first eighths uneven: inter-onset ratios 0.64-1.19 of the written length. Add to `leg_leads.json`: `"Bass clarinet": {"92.5": 0.07, "106": 0.08}`. Do not add 91.5 (a hall artefact, see above).
- Inferred: at 52 bpm these are 11-15% of a beat, on the most exposed lines of the piece (horn theme, oboe dialogue, B.cl. solo), against pizz./harp/tenuto beats that are on time to 0.04 s.

## 2. Before both tutti arrivals the woodwinds stop for 0.45-0.54 s while the strings play through. The master dips 3 dB just before the ff (gaps and dips measured, musical effect inferred)

**Where.** The printed wind breaths at qn 204 (into bar 61 ff, Largamente) and qn 268 (bar 81). Seven woodwinds at each: Fl1, Ob1, Cl1, Cl2, BCl, Bn1, Bn2 at 204; Fl1, Ob1, Cl1, Cl2, BCl, Bn2 at 268.

**Evidence** (`breath.py`):
- Every one of these notes ends 0.3 qn early: the c13 loud-breath rule, `n["end"] = e0 - min(0.3, 0.5 * dur)`. That point falls inside the `CAESURA` span: the 0.25 qn before 204 lasts 0.487 s, and before 268 0.47 s. So the gaps are 0.540 s (204) and 0.535 s (268).
- Each stem is 25-33 dB down for 0.40-0.49 s.
- The strings have no breath, so they sustain the crescendo through it. Vln I is -25..-30 dB throughout.
- Master per 0.1 s at 204: -14.0 at -0.7 s, -17.2 at -0.4, -14.0 at 0.0, peak -12.8 at +0.2. So the ff downbeat is only 1.2 dB over the pre-breath crescendo.
- At 268 the master goes -16.8 → -19.9 before the beat.
- The caesura already gives the whole orchestra its pause. Inferred: the extra 0.3 qn turns a wind breath into a half-second hole at the moment the crescendo should peak. Players breathe in about 0.2-0.25 s at an arrival like this.

**Fix.** In `tools/score_to_parts.py` (note lengths, the `near(orig_end, breath_q)` branch), use a shorter loud gap when the breath has a caesura. Add the constant `CAESURA_BREATH_QN = 0.12`, and in the `elif family in ("wind", "brass") and base(e0 - 0.01) >= DYN["mf"]` branch:

```
gap_ = CAESURA_BREATH_QN if any(abs(e0 - c_) < 0.01 for c_ in CAESURA) else 0.3
n["end"] = e0 - min(gap_, 0.5 * dur)
```

- Expected gaps: about 0.23 s at 204 and 0.23 s at 268. The master dip should be about 1 dB.
- The c13/c15 solo-horn breaths (196, `BREATH_GAP_AT`) are not in `CAESURA` and keep 0.3/0.5 qn. LEARNINGS 124/153 were measured on those.
- Re-check the limiter. The winds now sound up to 0.3 s longer into the climax, so peaks may move (LEARNINGS 99/167).

## 3. The violas' accompaniment triplets in bars 37-40 limp: every rise from the bottom note is 0.10-0.22 s late (measured)

**Where.** Violas, qn 108-124 ("senza sord., unis.", pp, slurred triplet eighths under the flute solo, against Vc/Cb pizz. and harp on the beats). Also bar 57 (qn 188-190).

**Evidence:**
- Dominant-pitch trace (`dom2.py`, bar 38, qn 112-114):
  - B flat3 → D flat4 takes over at +0.15 and +0.10 s.
  - The other steps take over at +0.02..+0.05.
  - So each triplet plays about 0.45 / 0.24 / 0.33 s instead of 0.33 × 3.
- Crossovers, all the same on c17:
  - 58 → 61 (B flat3 → D flat4) at 112.333, 113.667, 116.333, 117.667, 118.333, 119.667, 122.333: +0.13 each
  - 57 → 60 at 120.333 / 121.667: +0.19..+0.22
  - 60 → 63 at 120.667: +0.20
  - 65 → 61 at 109, 111, 119, 189: +0.16..+0.22, despite the existing +0.12 pair extra
- `ioi.py`: 17 viola intervals off by more than 30% of their written length (ratios 0.32-1.63). Every other track has 0-7.
- Cause: the lead cap `0.45 * (q - pv["qn"])` (`score_to_parts.py` line 1594) is 0.15 qn = 0.148-0.156 s for every note here, and the leads sit exactly at it. LEARNINGS 89 records that extra leads do nothing on these figures because of this cap.

**Fix.**
- In `tools/score_to_parts.py`, add:

  ```
  LEG_CAP_FRAC = {"Violas": [(108.0, 124.0, 0.75), (186.0, 192.0, 0.75)]}
  ```

  At line 1594, replace 0.45 with the window's fraction when the note's score onset lies inside one.
- Add `LEG_PAIR_EXTRA_S["Violas"]` entries `(58, 61): 0.10` and `(57, 60): 0.10`. The existing `(60, 63): 0.10` and `(65, 61): 0.12` then take effect.
- Expected:
  - leads 0.25-0.27 s, which the 0.75 cap allows (0.25 qn)
  - rising-step takeovers +0.02..+0.08
  - note-on spacing never under 0.22 s
- This is a lead change on the same patch and articulation. It does not reopen the closed articulation tests.
- Check with `dom2.py 19 Violas 112 114` that every pitch dominates part of its slot.

## 4. The violin octaves come apart by 0.12-0.2 s at a few joins of the theme and the climb (measured)

At 6 of the 53 legato onsets that Vln I and Vln II share, both metrics put them more than 0.1 s apart. Each item gives crossover / rise, the same on c16.

- **Vln II late:**
  - qn 68 (bar 23.67, theme C, Leg BC, C5 → E flat5): +0.17 / +0.18; Vln I -0.03 there
  - qn 80 (bar 27.67, C5 → F5, BC): +0.27 / +0.275; Vln I +0.15
  - qn 254 (bar 76.33, F5 → B flat5, BC): +0.12 / +0.22
- **Vln II early** on D5 → C sharp5 in both theme statements:
  - qn 71 (bar 24.67): -0.15 / -0.15
  - qn 243 (bar 72.67): -0.13 / -0.15
- **Vln I late in the climb:**
  - qn 192 (bar 58): +0.12 / +0.125
  - qn 196 (bar 59): +0.13 / +0.12
  - qn 200 (bar 60): +0.12 / +0.16. Vln II is 0.21 / 0.18 s ahead and Fl1 0.12 / 0.17 ahead.
  - qn 247 (bar 74): +0.14 / +0.135
- **Celli late:**
  - qn 54 (bar 19): +0.12 / +0.14
  - qn 180 (bar 55): +0.15 / +0.12

**Fix**, in `build/leg_leads.json`. Caps were checked against the previous note lengths, and all values fit.
- `"Violins II"`: add `"68": 0.10, "80": 0.08, "254": 0.08, "71": -0.10, "243": -0.10`. At 80 the cap is 0.25 s, so expect only +0.19 there.
- `"Violins I"`: add `"192": 0.04, "196": 0.04, "200": 0.08, "247": 0.08`. The caps are 0.21-0.22 s at 192/196.
- `"Violoncellos"`: add `"54": 0.08, "180": 0.08`.
- Leave Vln II 182 alone: it is a triplet at its cap.
- LEARNINGS 144 says one BC join moved 0.29 s for 0.10 s of lead. Re-measure 80 and 254, which are BC leaps, with both metrics.

## 5. After a track's last note the volume envelope still moves, so hall tails swell or drop (measured)

The open c18 item, measured.
- `build_reaper.py` `tail_hold` holds the envelope only through rests between notes.
- **The final chord.** The fade reaches its lowest value at the release (qn 304), and then the roles that end at 304 lift it back toward -10 dB inside the hall tail:
  - Double basses -17 → -11.6 dB by +0.3 s, -10 by +1.5 s
  - Violoncellos and Violins I -16 → -13 → -10
  - Violins II -12 → -10
  - Violas -7 → -10

  The Cb stem rises from -65 to -62 dB 0.25 s after the release, then decays. The master tail is still monotonic, but the low strings' tail blooms 5-6 dB over its natural decay.
- **Tuba at bar 63.** After its last note (qn 210-212, ff), the envelope falls 8.5 → 3.1 dB within 0.57 s. The tuba tail drops 16 dB in 0.3 s (-38.6 → -55.2), about twice the hall's 25-30 dB/s.
- Smaller cases in the tail's first 1.5 s:
  - Fl1 after 274: -3 dB at +0.12 s
  - Fl2 after 267: +3
  - Ob1 after 273: +6 at +1.4 s
  - Tbn2 after 212: -2.5
  - Vln II div after 124: +2.5..+5
  - Violin I solo after 65: -1.7

**Fix.**
- In `tools/build_reaper.py` `vol_points`, extend `tail_hold` to the final rest. After the track's last note (moved end), hold the envelope at its value at that end to the end of the project.
- Remove the `fade` rise after 304 in `score_to_parts.py`, which now becomes redundant. The c09 intent of "not fading the hall tail" is kept, because the tail is held at the release level instead of rising.
- Then update every track with `--midi-only`.
- Expected: the final tails decay smoothly from their release level (-58 dB master), and the tuba's tail at bar 63 decays at the hall rate.

## 6. Bassoon 1's chord changes under the horn solo are still 0.15-0.3 s late. A per-onset version of c15's abutting lead avoids the c15 failure (measured)

**Where.** Bassoon 1, Sus MAX v41, CC11 34, bars 10-14, under the horn theme. These notes abut the previous note at a new pitch.

**Evidence** (`chg.py`, `arrall.py`):
- body - 3 dB at qn 27 +0.245, qn 35 +0.315
- own-pitch arrival at qn 35 +0.275, qn 36 +0.28, qn 38 +0.145
- The bass clarinet, playing the same chords, arrives at +0.00..+0.06.

c15's `ABUT_LEAD` was emptied because it made 9-15 dB holes on the same-pitch repeats that followed a led note (Bn1 22, 32; Bn2 21). None of 27, 35, 36 and 38 is followed by a same-pitch repeat: 27 → rest at 30, then 35 D flat4 → 36 B flat3 → 38 G3 → 39 A flat3.

**Fix.**
- In `tools/score_to_parts.py`, give `ABUT_LEAD` an `"at"` list and require the onset to be in it (`any(abs(q - a) < 0.02 for a in abut_["at"])`) in the condition at line 1636:

  ```
  ABUT_LEAD = {"Bassoon 1": {"lead_s": 0.10, "max_cc": 50, "overlap_qn": 0.0, "at": [27.0, 35.0, 36.0, 38.0]}}
  ```

- Expected body - 3 dB at about +0.15..+0.2 s.
- Check the qn 22/32/33 repeats on the Bn1 stem, which should be unchanged.

Do not touch:
- The tempo map: `RAMP_SPANS`, the printed steps, `PHRASE_ARCS`, `TEMPO_PUSH`, `APEX_AGOGIC`, `BEAT_STRETCH`, the caesura amounts, the 20 bpm final beat and the fermata length.
- Keyswitch placement and the pre-roll.
- The family legato and entry lead tables, whose medians are +0.00..+0.08.
- The existing `leg_leads.json` values: the c15 Horn 1 193/202 and Vln II 164/252 leads read early or late on one metric only.
- The divisi and a2 entry leads: section sums are within 0.06 s of c17.
- Pizz., harp, timpani and Tbn1 marcato timing (+0.00..+0.04 s).
- The solo-horn breath gaps (`BREATH_GAP_AT` 195).
- Do not add leads from crossover numbers alone after the c17 hall, for example to the Horn 1 Ab3 targets or BCl 91.5.
