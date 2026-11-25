# Cycle 15, critic C: tempo, timing and transitions (on the cycle 14 render)

Material: `cycles/c14/render` (master and 29 stems), `cycles/c14/metrics` (attacks.txt), `build/parts.json` (written 19:00:05, before the c14 render at 19:01, so it is the rendered data), `build/{leg_leads,entry_leads}.json`, `tools/score_to_parts.py`, `build/global.ily`, `build/mockup-events.tsv`, score pages 1-8. For comparison, c13 measured on `cycles/c14/before/build/parts.json`.

Scripts are in `/private/tmp/claude-501/mockup-loop/c15-C/`. Run them with `~/.venvs/claude-composes-reaper/bin/python`. These are c11-C's scripts (`lib.py`, `leg.py`, `arrival.py`, `pitchtrace.py`, `look.py`, `entries.py`, `ent2.py`, `reatt.py`) plus these new ones:
- `bars.py`: per-bar and per-beat tempo from the parts.json map.
- `ks.py`: the gap from each keyswitch to the moved start of the note it serves.
- `arrall.py`: for every legato or abutting note, the time its pitch reaches body - 6 dB.
- `chg.py`: dip depth and time to body - 3 dB at chord changes.
- `rel.py`: release times at shared phrase ends.
- `run.py`: which pitch dominates during a fast run.
- `tbn.py`: per-note onsets of one track.

"Crossover" has the c07/c11 meaning: the time the new pitch's harmonic energy overtakes the old pitch's and stays ahead for 40 ms. All times are measured from the score onset `sq` on the parts.json tempo map, caesuras included.

Delivery, for the record (from c14 CHANGES.md; ebur128 re-run): master -23.8 LUFS, LRA 23.5 LU, TP -4.5 dBFS. mp3 -19.8 LUFS, LRA 16.0 LU, TP -1.7 dBTP.

## Where c14 stands (measured)

- **Tempo map.** Every printed step in `global.ily` is realised:
  - bars 35-36: 49.2 and 45.0 bpm
  - bar 47: 60, 60, 57.5, 55
  - bars 48-52: 54
  - bars 53-59: 60.0 rising to 64.5
  - bar 60: 63, 61, 59, then 47.1 including the 0.22 s caesura
  - bars 61-62: 54
  - bars 63-64: 53.0 falling to 38.5
  - bars 78-82: 50.3, 48.7, 45.5, 45.9, 44.0
  - bars 89-92: 48.4, 44.0, 39.9, then 36.8, 35.2 and 20 bpm on the last beat

  The final chord lasts 6.3 s, 1.4 times bar 91. The master holds -46 to -48 dB until 0.75 s before the release. After the release it falls from -60 to -94 dB in 1.25 s. Every final-chord stem ends at qn 304. The fermata is not cut early.
- **Keyswitches.** All 251 come before their note's moved start. The smallest gaps are 13 ms (Ob1 207.95) and 28-29 ms (string Leg BC/Slur changes in bars 58-60). The c14 Tbn1 `Marc Lng RRx4` key comes 0.06 qn before qn 214.5. The timpani stroke keys at 202.94 and 210.94 come before their strokes. No clashes.
- **Entries** (body - 6 dB, median and p90): winds +0.033 (+0.074), brass -0.005 (+0.061), timpani +0.002, harp +0.006, strings +0.029 (+0.114). These match c11.
- **Legato crossovers, median per track** (c14; c13 in brackets):
  - Vln I +0.013 (+0.013), Vln II +0.033 (+0.043), Vla +0.028 (+0.028), Vc +0.038 (+0.028)
  - Hn1 +0.023 (+0.013)
  - Fl1 +0.038, Ob1 +0.043, CA +0.001, Cl1 +0.043, Bn1 +0.058
- **Tbn1 marcato line (bars 63-64).** Each note's own pitch reaches its peak - 6 dB between -0.10 and +0.07 s. The c14 MARCATO change did not make it late.

The table-wide leads are right. The remaining timing errors fall into two groups: systematic biases inside a track (by articulation, by dynamic), and a short list of repeatable single notes.

## 1. The flute solo of bars 37-44 changes notes 0.08-0.23 s after the pizzicato and harp beats under it. Soft flute legato is late as a class (measured)

**Where.** Flute 1, qn 108-140 (Poco più mosso, p, "1." solo). Under it, Vc/Cb pizz. and harp play on the beat; they measure +0.00 to +0.03 s.

**Evidence (measured):**
- Flute 1 legato crossovers by CC11 at the target:
  - CC11 ≤ 50: median +0.093 s (n = 18)
  - CC11 51-75: +0.030 (n = 20)
  - CC11 > 75: +0.028 (n = 18)
- Almost all of the soft group is this solo. Across qn 108-140 the median is +0.083 and p75 +0.118 (n = 24).
- The latest are the v60 steps onto beats that a pizz. or harp note also starts:
  - 111: +0.163
  - 112: +0.118
  - 118: +0.233
  - 119: +0.143
  - 122: +0.113
  - 132: +0.118
  - 134: +0.143
- The v80 notes in the same solo have a median of +0.068.
- c13 gave the same values (111 +0.163, 118 +0.183, 134 +0.153), so the lag is repeatable.
- The flute's lead is 0.03 s (`LEG_LEAD_S["Flute"]`). The cor anglais solo that follows (qn 124-172) crosses at a median of -0.002 on its 0.08 s lead. So the flute is the outlier.
- Inferred: a 0.1-0.2 s lag against plucked beats is the most exposed timing error left in the movement. Pizz. and harp mark the beat exactly, and the flute is alone on top.

**Fix.** In `tools/score_to_parts.py`, add a soft-dynamic legato extra:

```
LEG_SOFT_EXTRA_S = {"Flute 1": (50, 0.06)}   # c15 (C #1): (CC11 at the target <=, extra s)
```

In the `pv is not None` branch next to `LEG_EXTRA_S`, add:

```
ex += LEG_SOFT_EXTRA_S.get(tname, (0, 0))[1] if cc11_at_target <= LEG_SOFT_EXTRA_S.get(tname, (0, 0))[0] else 0
```

Here `cc11_at_target` is the same `final(q)`/base CC11 that the entry branch reads.

Expected: soft flute median about +0.03 s. The listed onsets come to +0.05..+0.17, with 118 the latest.

The 0.45 x previous-length cap does not bind. The shortest previous note in the solo is 0.33 qn, which allows 0.15 qn, about 0.15 s. Do not raise the flute's v60 legato velocity instead, because velocity changes the character of the transition.

## 2. The strings' slurred joins cross 0.05-0.08 s later than their bow-change joins on the same lead. Octave-doubled lines smear by up to 0.2 s (measured)

**Where.** Violins II, Violas and Violoncellos, throughout. It is most audible where Vln I and Vln II double the theme at the octave (bars 23-30 and 71-77) and where the cellos double the violins in the climb (bars 54-60).

**Evidence (measured).** Crossover median by articulation, c14 (c13 in brackets):

| Track | Leg Slur MAX | Leg BC MAX | Difference |
|---|---|---|---|
| Vln I | +0.028 (+0.023), n=56 | +0.010 (+0.010), n=30 | 0.02 |
| Vln II | +0.063 (+0.063), n=73 | -0.017 (-0.012), n=35 | 0.08 |
| Vla | +0.043 (+0.038), n=111 | -0.007 (+0.003), n=13 | 0.05 |
| Vc | +0.068 (+0.058), n=61 | -0.007 (-0.007), n=35 | 0.075 |

- Each track uses one lead for both articulations. Vln II and Vla use 0.20 s, Vc 0.17 s.
- Across the string pairs that share legato onsets (269 shared onsets), 80 differ by more than 0.10 s. The median difference is 0.065 s and p90 0.165.
- Examples, Vln I against Vln II at the same onset:
  - qn 66 (the theme's first change): -0.012 / +0.133
  - qn 72 (Vln II on BC): +0.013 / -0.132
  - qn 86.5: +0.053 / +0.198
- Vln II against Vc at qn 54: -0.092 / +0.153.
- Simulated with the fix below (crossovers shifted by the lead change, 1:1 as LEARNINGS records for leads): 80 → 64 pairs over 0.10 s, median 0.065 → 0.055. The track medians become Vln II +0.018, Vla +0.018, Vc +0.008.

**Fix.** In `tools/score_to_parts.py`, add an articulation adjustment in the same `pv` branch: `ex += LEG_ART_EXTRA_S.get(tname, {}).get(n["art"], 0.0)`.

```
LEG_ART_EXTRA_S = {"Violins II": {"Leg Slur MAX": 0.04, "Leg BC MAX": -0.03},
                   "Violoncellos": {"Leg Slur MAX": 0.05},
                   "Violas": {"Leg Slur MAX": 0.025}}
```

Use the exact track names. `by_name` substring matching would make "Violins I" catch "Violins II", as the `LEG_LEAD_S` comment warns. BC_SOFT joins play Leg Slur MAX and were measured as Slur, so they take the Slur value.

Interactions:
- `leg_leads.json` totals are still clamped to 0.03-0.35. Vc qn 204 (-0.07) is a BC join and is unaffected.
- The Vc (56, 60) pair extra (0.15) already brings its two notes to +0.25..+0.30 arrival. With +0.05 they reach the 0.45 x cap only if the previous note is shorter than 1 qn. Check those two in the diff.

## 3. A dozen repeatable single legato notes are still 0.15-0.27 s late, including Horn 1 against the cellos it doubles in bars 58-60 (measured)

All values below were the same in c13 and c14 within 0.03 s, except where noted. LEARNINGS records that a per-onset lead moves a crossover 1:1.

| Track, qn (bar) | Interval, art | Crossover c14 (c13) | Context |
|---|---|---|---|
| Horn 1, 193 (58.25) | F4→Eb4, lead 0.25 | +0.183 (+0.203) | Vc same onset -0.017 |
| Horn 1, 195 (58.75) | Eb4→F4, lead 0.10 | +0.173 (+0.123) | Vc +0.158 |
| Horn 1, 200 (60) | E4→Eb4, lead 0.10 | +0.153 (+0.143) | Vc -0.092 |
| Horn 1, 202 (60.5) | F4→Gb4, lead 0.25 | +0.178 (+0.173) | Vc +0.043 |
| Vln II, 164 (51) | D5→Eb5, Slur | +0.268 (+0.273) | just after the qn 164 caesura |
| Vln II, 252 (75.67) | C5→F5, BC | +0.243 (+0.243) | Vla +0.043 |
| Vln II, 60 (21) | E4→F4, Slur | +0.183 (+0.188) | Vla -0.012 |
| Vln II, 245.5 (73.5) | C5→Bb4, Slur | +0.193 (+0.153) | |
| Vln I, 75 (26) | Ab5→G5, Slur | +0.208 (+0.208) | Vln II +0.043 |
| Flute 1, 200 (60) | Bb5→C6, v60 | +0.218 (+0.213) | Vln I +0.008, Ob1 +0.068 |
| Cor anglais, 131.5 (42.9) | Gb4→F4 | +0.183 (+0.183) | solo |

- Horn 1 plays the cello line an octave higher in bars 56-60. Of its five transitions at 193-202, four are 0.15-0.18 s behind, while the cellos average +0.02.
- Two climax entries without a wind entry lead also arrive late:
  - Flute 2 at qn 262 (Sus v91, after 59 qn of rest): body - 6 dB at +0.17 s
  - Bassoon 2 at qn 268 (Sus v91): +0.186 s

**Fix** (data only):
- `build/leg_leads.json`:
  - `"Horn 1": {"193": 0.10, "195": 0.08, "200": 0.07, "202": 0.10}` (193 and 202 reach the 0.35 clamp)
  - `"Violins II": {"164": 0.10, "252": 0.10, "60": 0.07, "245.5": 0.07}` (if #2 is adopted, subtract its +0.04 from the Slur ones: 164 0.06, 60 0.03, 245.5 0.03)
  - add `"75": 0.08` to the existing `"Violins I"` entry
  - `"Flute 1": {"200": 0.10}` (#1 does not cover it, because CC11 is 88 there)
  - `"Cor anglais": {"131.5": 0.08}`
- `build/entry_leads.json`: `"Flute 2": {"262": 0.10}` and `"Bassoon 2": {"268": 0.08}`.
- Expected: every listed note within +0.03..+0.10 s.
- Check 262 on the master afterwards. It is the bar 79 ff downbeat, and earlier starts move peaks. Leave limiter margin, as LEARNINGS says.

## 4. Under the horn solo (bars 8-14), the bassoons' quarter-note chord changes take 0.17-0.32 s to sound (measured; audibility inferred)

**Where.** Bassoon 1 (and Bassoon 2) at qn 21-39. Sus MAX, v41, CC11 34, pp. Each note abuts the previous one (gap 0.000 qn) and gets no lead. `ENTRY_LEAD_S["Bassoon"]` applies only after a rest of 0.5 qn or more.

**Evidence (measured)** (`chg.py`, broadband 20 ms frames, body = +0.35..+0.8 s):

| Bassoon 1 onset | Body - 3 dB at |
|---|---|
| 21 | +0.175 s |
| 27 | +0.250 s |
| 31 | +0.170 s |
| 39 | +0.320 s |

- The new pitch's harmonics reach body - 6 dB at:
  - qn 27: +0.215 s
  - qn 35: +0.270 s
  - qn 36: +0.19 s
- The dips at these changes are 4-9 dB.
- The bass clarinet, playing the same chords on Sus Non Vib, reaches body - 3 dB by +0.00..+0.10 at the same onsets. The bassoon's harmony therefore changes after the rest of the chord.
- The same pattern shows in Bn2 at 180, 193 and 261 (+0.18..+0.20) and Bn1 at 198 (+0.175), at louder levels.

**Fix.** In `tools/score_to_parts.py`, add a rule for abutting wind re-attacks. It applies to a non-legato Sus note in the Bassoon family whose previous note in the track ends within 0.05 qn of its onset and whose pitch differs. Such a note gets lead `ENTRY_LEAD_S` (0.06 s) + 0.04 = 0.10 s, and the previous note is ended at the moved start (the existing note-end guard does this for same-pitch notes; apply it here too). Only an overlap that the guard removes would join; Sus is polyphonic, so a 0.02 qn overlap is harmless and avoids a gap.

Expected: body - 3 dB at +0.07..+0.22 s, and smaller dips. Limit the rule to CC11 ≤ 60 first, and check bars 8-14 on the Bassoon 1/2 stems.

## 5. The phrase arcs give every phrase the same ending, including 2-bar sub-phrases. The tempo then jumps 8-17% back up on the next downbeat (tempo measured, musical effect inferred)

**Where.** `PHRASE_ARCS`, especially (42,48), (48,54), (54,60), (60,66) in bars 15-22, and (220,226).

**Evidence:**
- Measured (`bars.py`), last beat of each bar → next downbeat:
  - bar 16: 44.3 → 52.0
  - bar 18: 47.8 → 52.0
  - bar 20: 47.8 → 52.0
  - bar 22: 44.3 → 52.0
- So bars 15-22 slow down every 2 bars. The pulse runs through all of them: Vln II has a tenuto on every beat, and the score has no seam in the accompaniment.
- The section cadences get the same x0.96/x0.92 as these sub-phrases: qn 42 (end of the horn theme), 66 (into C), 90 (end of C, p > pp) and 238.
- The arcs add only 0.03-0.11 s per phrase (LEARNINGS). So the effect is a small hesitation every two bars, with no larger breath at the section ends.
- Inferred: in performance, phrase-final lengthening scales with the level of the boundary, and the tempo comes back over a beat or two rather than in one step. As set now, the arcs give a regular hitch at the sub-phrases and no extra weight at the cadences.

**Fix** (one render, then judge by listening or by the bar table). In `score_to_parts.py`:
1. Give PHRASE_ARCS entries an optional depth: `(a, e, depth)` with `depth` in {"sub", "main"}.
   - `"sub"` uses `PHRASE_SLOW` (0.98, 0.95) and no push. Use it for (42,48), (48,54), (54,60) and (220,226).
   - `"main"` uses (0.95, 0.88). Use it for (30,42), (60,66), (78,90) and (226,238).
   - Leave the others as they are.
2. When an arc's start follows another arc's end within 0.01 qn, make its first beat x0.97 instead of x1.0, so the tempo returns over one beat.

Both stay on whole-qn steps, so `add_caesuras` will not exit. The total length changes by less than +0.3 s. If the seams in bars 15-22 are wanted as written, change only step 2.

## 6. Smaller items (measured)

- **Violas C4→Eb4** (238.5, 244.5, 246, 250.5): +0.15..+0.20 s on a 0.26 s lead.
  - The `0.45 * (q - pv["qn"])` cap binds, because the previous C4 is 0.5 qn long.
  - Only a cap exception can fix these. In the pair-extra case, allow 0.6 x the previous length when the previous note is 0.5 qn or longer.
  - This is an inner voice, so it has low priority.
- **Release spread at qn 90** (end of bar 30, p > pp, strings and horns): the stems fall 15 dB under their body between +0.17 s (Vln I) and +0.70 s (Cb). At the final chord the spread is +0.12 (Cl2) to +0.67 (Cb).
  - This is the low strings' longer sample release and room. It is consistent with a real hall, and I do not recommend a change.

## Do not touch

- The tempo map: `RAMP_SPANS`, the printed steps, the caesura amounts, the 20 bpm fermata beat, and the final-bar fade and hold.
- Keyswitch placement, and the pre-roll first-keyswitch scheme.
- The family legato and entry lead tables. The medians are +0.00..+0.06; change only the classes and notes above.
- `qn_before` lead conversion, and the existing `leg_leads.json` and `entry_leads.json` values.
- The Tbn1 marcato timing (on time).
- `TIMP_TIE_STROKES` timing: the strokes at 203 and 211 start rising at +0.00..+0.02 s and peak at +0.06 and +0.035 s.
