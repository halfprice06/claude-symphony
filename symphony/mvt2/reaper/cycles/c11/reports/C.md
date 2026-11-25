# Cycle 11, critic C: tempo, timing and transitions (on the cycle 10 render)

Under review: `cycles/c10/render` (master and 28 stems), `cycles/c10/metrics`, `build/parts.json` (unchanged since the c10 render), `build/entry_leads.json`, `build/early_fills.json`, `build/pitch_trims.json`, `tools/score_to_parts.py`, `v77/global.ily`, `build/mockup-events.tsv`.

Scripts are in `/private/tmp/claude-501/mockup-loop/c11-C/`. Run them with `~/.venvs/claude-composes-reaper/bin/python`. `lib.py`, `entries.py`, `ent2.py`, `leg.py` and `dom.py` are c07-C's; `lib.py` now reads `PARTS=<path>` so that c09 can be measured on `cycles/c10/before/build/parts.json`. New scripts:
- `arrival.py`: at every score onset shared by 4 or more tracks, the time each track's new pitch (3 harmonics) reaches 6 dB under its body. Output is in `arr10.txt` and `arr_10.json`.
- `pitchtrace.py`: old-pitch and new-pitch energy every 40 ms around one transition.
- `look.py`: a note's articulation, velocity, lead and broadband envelope.
- `reatt.py`: re-attacks that abut the previous note.

All times are against the score onset `sq` on the parts.json tempo map, caesuras included. "Crossover" is c07-C's measure: the time the new pitch's harmonic energy overtakes the old pitch's and stays ahead for 40 ms.

## Where c10 stands (measured)

- **Tempo map.** Every bar matches the printed `\mt` steps in `global.ily`:
  - bars 35-36: 49.2 and 45.0 bpm
  - bar 47: 58.0
  - bars 53-59: 60.0 rising to 64.0
  - bar 60: 56.8, including the 0.22 s caesura
  - bars 63-64: 50.3 and 42.6
  - bars 78-82: 50.3, 48.7, 45.5, 45.9, 44.0
  - bars 89-92: 48.4, 44.0, 39.9, then 36.8/35.2 and 20 bpm for the fermata beat

  The final chord lasts 6.3 s. The master holds -45 to -49 dB (0.5 s RMS) until 345.4 s, falls over the last 1.5 s, and the hall tail falls from -66 to -113 dB in 1.5 s after the release. The fermata is not faded early.
- **Keyswitches.** None arrives after the moved start of the note it belongs to. The smallest gap from keyswitch to note is 13 ms (Ob1 207.95, a Sus crossfade inside a sounding chain); the string Leg BC/Slur changes in bars 58-60 leave 28 ms.
- **Entry arrival, body - 6 dB, median (p90):** winds +0.034 (+0.075), brass +0.001 (+0.066), timpani +0.002, harp +0.007, strings +0.032 (+0.108).
- **Legato crossovers, median:**
  - Vln I +0.018, Vln II +0.033, Vla +0.040, Vc +0.028
  - Hn1 +0.030
  - Fl1 +0.038, Ob1 +0.043, CA +0.001, Cl1 +0.043, Bn1 +0.058
  - Pairwise medians between sections that share onsets are within 0.033 s (Vln I/Vln II 0.000, Vln II/Vc -0.005, Fl1/Vln I +0.010).
  - At the 152 onsets where two or more tracks change pitch legato, the spread is median 0.093 s, p90 0.195 s.

The remaining timing errors are specific notes and specific intervals, not table-wide leads. These are the ones a listener hears.

**Delivery (for the record; not my lens):** master -23.6 LUFS, LRA 21.6 LU; mp3 -20.0 LUFS, LRA 14.6 LU (ffmpeg ebur128, re-measured). TP and limiter figures are in c10 CHANGES.md: master -3.6 dBFS, mp3 -1.5 dBTP, limiter 3.6 dB.

## 1. Horn 1 is 0.19-0.31 s late every time it leaves F4 in the climb to bar 61. It doubles the cellos at the octave there, and the cellos are on time (measured)

**Where.** Horn 1, bars 54-60, qn 184 (F4→C4), 193 (F4→Eb4) and 202 (F4→Gb4). Also 178 and 34, less late. In bars 56-60 Horn 1 plays the cello line an octave up, note for note: Vc 53/51/53/54 against Hn1 65/63/65/66 at the same onsets.

**Evidence (measured):**

| qn | Hn1 crossover | Vc crossover |
|---|---|---|
| 184 | +0.193 | -0.047 |
| 193 | +0.283 | -0.017 |
| 202 | +0.308 | +0.043 |

- Horn 1 legato departures from F4: median +0.193 s (n = 5). All other Horn 1 transitions: median +0.028 (n = 45).
- `pitchtrace.py` at qn 193: the new Eb4 is present from -0.06 s, but the old F4 stays stronger until +0.30 s. It decays only 12 dB in that time while Eb4 rises from +10 to +18 dB.
- The same notes were late in c05 (+0.20/+0.28/+0.31; c07-C #3), before any pitch trim existed. c07 raised brass legato velocity to v124, and that did not move them. So the cause is the F4 legato sample itself. This is consistent with F4 being the hot note in that patch (pitch_trims `_doc`: +5 dB residual).
- Inferred, secondary: the F4 `body -5` trim ends at the next note's moved onset (192.85 → 192.93: -5.8 → -0.8 dB). That lifts the departing F4 by 5 dB while its transition tail is still sounding.

**Fix.** In `tools/score_to_parts.py`, set `LEG_EXTRA_S = {"Violas": {60: 0.10}, "Horn 1": {65: 0.15}}`. The code looks it up with `.get(tname)`, an exact match, so only Horn 1 is affected. Expected crossovers: 184 about +0.04, 193 about +0.13, 202 about +0.16, 178 about -0.03, 34 about -0.06. The `0.45 * (q - pv["qn"])` cap does not bind (the previous notes are 1-2 qn).

Do not move the F4 trim end first. Keeping -5 dB past the onset would also cut the new note's start.

## 2. On the bar 61 downbeat, Horn 3's Ab4 swells in over 0.45 s. It is 18-20 dB under Horn 2 for the first 0.3 s (measured)

**Where.** Horn 3, qn 204: Ab4, f, tenuto, Sus MAX, v83, CC11 93. It is the top of the horn chord on the climax downbeat. The same slow sample affects Horn 2 at qn 210 (Ab4, Sus re-attack from Gb4).

**Evidence (measured).** 10 ms RMS of the stems every 0.05 s from the score onset (`look.py`):

| | +0.00 | +0.05 | +0.10 | +0.15 | +0.20 | +0.25 | +0.30 | +0.35 | +0.40 | +0.45 s |
|---|---|---|---|---|---|---|---|---|---|---|
| Horn 3 | -55 | -52 | -50 | -47 | -48 | -45 | -43 | -40 | -36 | -33 |
| Horn 2 | -37 | -33 | -32 | -30 | -32 | -30 | -30 | -30 | -30 | -30 |

- Horn 3 reaches body - 6 dB at +0.34 s. Every other track at qn 204 reaches it between -0.06 and +0.11 s: winds +0.005..+0.11, timpani 0.00, Hn2 -0.01, Vln II -0.025.
- The c08, c09 and c10 stems are identical to the dB at this note, so the attack is deterministic.
- Horn 3 has no CC15 change near the note and no negative pitch trim (Ab4 +3). Horn 2 at qn 210, same pitch and velocity, rises -40 → -30 dB over 0.5 s (arrival +0.175).

**Fix.** Both are data only.
- `build/entry_leads.json`: `"Horn 3": {"204": 0.10}`. The total lead becomes 0.15 s with the brass 0.05. Horn 3 rests before this note, so the earlier start falls inside the 0.22 s caesura, where the winds breathe.
- `build/early_fills.json`: `"Horn 3": {"204": 8}` and `"Horn 2": {"210": 6}`. Use the plain-number form: +dB from onset + 0.05 s to + 0.35 s, gone by + 0.6 s. That covers the measured rise.
- Check after the render: Horn 3 at 204 should be within 6 dB of its body by +0.10 s, and the bar 61 master peak should not rise (Horn 3 is about 12 dB under the master there).

## 3. In the Largamente (bars 61-62), the first violins' melody changes notes 0.1-0.2 s after the cellos. The c10 velocity change to v108 had no measurable effect (measured)

**Where.** Vln I and Vc legato targets at qn 204, 208 and 210, inside `SOSTENUTO_SPANS` (204-212).

**Evidence (measured).** Crossovers:

| qn | Vln I | Vc | Vln II |
|---|---|---|---|
| 204 | +0.138 | -0.057 | +0.073 |
| 208 | +0.068 | -0.032 | +0.148 |
| 210 | +0.103 | -0.007 | -0.017 |

- At 204 (`pitchtrace.py`), the cellos' new pitch leads from -0.06 s and is at body by -0.02 s, inside the caesura. Vln I's Db6 overtakes the C6 only at about +0.10 s.
- c09 (v124) and c10 (v108, `SOST_STR_LEG_VEL`) give the same crossovers to the millisecond at all seven of these transitions. The Vln I stems for qn 204-212 correlate 0.997, and their difference is 20 dB under the signal, which is the vol_db changes only.
- So velocity between 108 and 124 does not change the legato timing in this patch. The C #4d change can stay for its intended level effect, but it does not change the timing.

**Fix.** Add per-onset legato lead offsets.
- New file `build/leg_leads.json`, `{track: {score onset: seconds}}`. Read it next to `ENTRY_LEADS`. In the legato branch, where `leg_s` and `LEG_EXTRA_S` are added (around line 1059), add the matched value, matched within 0.02 qn. Negative values are allowed. Clamp the total lead to the range 0.03 to 0.35 s.
- Values:
  - Violins I: {204: 0.07, 208: 0.05, 210: 0.05}
  - Violoncellos: {204: -0.07}
- Expected: Vln I +0.03..+0.07 and Vc about 0.0 at 204, which puts the cellos on the beat after the caesura rather than in it.
- Keep the Vc lead change to 204 only. The cellos are on time everywhere else (median +0.028).

## 4. The new solo violin enters late at bar 17 and anticipates its slurred changes by up to 0.1 s; its patch speaks differently from the section's (measured)

**Where.** Track 28 "Violin I solo", qn 48-65 (bars 17-22).

**Evidence (measured):**
- **Entry at qn 48** (v53, CC11 54, lead 0.19 s = 0.06 family + 0.13 extra): it is 20 dB under body at +0.05 s and reaches body - 6 dB only at +0.185 s. At the same onset the violas arrive at +0.05 and Vln II at -0.15 (a legato continuation). The entry at qn 60 (lead 0.16) arrives at +0.03 and is fine.
- **Legato targets** (Leg Slur MAX on `1st Violins KS Master DIV A`, v124, 0.17 s string lead): median crossover -0.027 s against the full section's +0.018 on the same lead.
  - The two latest are 51.0 (-0.082) and 53.0 (-0.102), the downbeats of bar 18 and bar 18.67.
  - The cellos (51) and Vln II/Vc (53) change harmony on those beats. The solo moves about 0.1 s ahead of the harmony change, a rush in a 52 bpm adagio.
  - Range of the nine targets: -0.102 to +0.038.

**Fix:**
- `score_to_parts.py` `LEG_LEAD_S`: add `"Violin I solo": 0.12`. The name match comes before the family default, and no existing key is a substring of "Violin I solo". Expected median about +0.02 s, matching the section.
- `build/entry_leads.json`: `"Violin I solo": {"48": 0.20, "60": 0.10}`. The total at 48 is 0.26 s, under the 0.30 cap. The first 0.2 s sounds at -65 to -80 dB, which is under the accompaniment.

## 5. Three string intervals cross 0.15-0.23 s late every time they occur, including the cello countermelody's rising third in bars 25 and 73 (measured)

**Where and evidence (measured).** Crossovers, compared with each track's median for all other transitions:

| Track and interval | Onsets (qn) | Crossovers (s) | Track median, other transitions |
|---|---|---|---|
| Vc Ab3→C4 (56→60), Leg Slur | 74 (bar 25.67), 246 (bar 73.67) | +0.233 both | +0.026 |
| Vla C4→Eb4 (60→63), Leg Slur | 120.67, 194.67, 238.5, 244.5, 246, 250.5 (bars 40-75) | +0.10 to +0.21, median +0.16 | +0.043 |
| Vla F4→Db4 (65→61), Leg Slur | 109, 111, 119, 189 | +0.183 to +0.218 | +0.043 |

- The cello notes are the exposed countermelody under the bar 23-30 and bar 71-76 tune (global.ily: "theme in the violins, cello counter-melody"). Vln I is on time at both onsets.
- The violas' C4→Eb4 is already late after `LEG_EXTRA_S` {60: 0.10}. Every other departure from C4 now crosses at -0.08 to +0.04, so the existing extra is right for those and too small for Eb4 alone.

**Fix.** Add a pair table in `score_to_parts.py` next to `LEG_EXTRA_S`:

```
LEG_PAIR_EXTRA_S = {"Violoncellos": {(56, 60): 0.15}, "Violas": {(60, 63): 0.10, (65, 61): 0.12}}
```

Add it where `ex` is computed: `ex += LEG_PAIR_EXTRA_S.get(tname, {}).get((pv["pitch"], n["pitch"]), 0.0)`. The viola F4→Db4 notes at 109-119 are 0.33 s triplets, so check that the `0.45 * (q - pv["qn"])` cap allows the total; the previous note is 0.33-1 qn, which gives at least 0.15 qn.

## 6. The violas' slurred sextuplets in bars 59-60 lose their rhythm: most notes are never the strongest pitch in their own 0.16 s slot (share measured; cause inferred)

**Where.** Violas, qn 196-204: sextuplet 16ths, slurred in groups of 12, f, on Sus MAX through the `short_sus` rule. Each note is 0.197 qn long, so it overlaps the next by about 0.03 qn.

**Evidence:**
- Measured (`dom.py Violas 186 204 10`): the share of each note's own slot in which its pitch dominates the other pitches of the figure has a median of 0.26 in qn 196-204. 18 of the 48 notes have 0.10 or less, including every Gb3 (54) and nearly every Eb4 (63) from 199 to 203.33. In bars 37-40 (0.33 s triplets) the median is 0.82.
- Inferred: overlapping polyphonic Sus samples with slow attacks, at 0.157 s per note, blur into a chord. The rhythmic drive of the animando under the climb is lost. Some of the low share for Gb3 may be the measure, because its harmonics are shared with Bb3 and Eb4.

**Fix (test first on a short range render, qn 194-204).** In the `short_sus` branch, for string notes shorter than 0.2 s at CC11 ≥ 90:
- end each note 0.01 qn before the next onset (no overlap), and
- use velocity 100 (now 83), so each sample's attack is quicker.

If the share stays under 0.5, try the Violas KS Master's `Detache` row (key 30). It is in the patch but not loaded; `build_reaper.py` loads any row a track uses. Score fidelity is a concern: Detache plays separate bows under a printed slur, so use it only if the non-overlap version fails.

**Do not touch:**
- The tempo map: `RAMP_SPANS`, the caesura amounts and the 20 bpm fermata beat. Every span matches its printed steps.
- The final-bar fade (0 to 303, -2/-10, held after the release). The fermata now holds at -45 to -49 dB.
- Keyswitch placement and the pre-roll first-keyswitch scheme.
- The family legato lead tables for strings and winds. Section-to-section medians are within 0.03 s; change only the specific notes and intervals above.
- `qn_before` lead conversion.
- The existing `entry_leads.json` values. Pizzicato, harp and timpani attacks are 0.00-0.01 s.
