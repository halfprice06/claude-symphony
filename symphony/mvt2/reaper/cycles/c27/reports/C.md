# Cycle 27, critic C: tempo, timing and transitions (on the cycle 26 render)

Material: `cycles/c26/render` (master and 32 stems), `cycles/c26/metrics`, `build/parts.json` (08:20:52; it already holds the post-render gain fixes), `cycles/c26/before/parts.json` (the c25 data, used to measure the c25 render), `build/{entry_leads,leg_leads,early_fills}.json`, `tools/score_to_parts.py`, `v77/global.ily`, `build/mockup-events.tsv`, `sections/coda.ily`, and score page 6 (bars 71-78).

Scripts: `/private/tmp/claude-501/mockup-loop/c27-C/`. This is the c23-C set run on c26, and on c25 with `PARTS=cycles/c26/before/parts.json`. New scripts:
- `trace.py`: stem level in 50 ms steps from -0.2 to +0.8 s around a score onset, relative to the body (+0.4 to +0.9 s).
- `fillsim.py`: applies an `early_fills.json` shape to the measured envelope and re-measures the arrival and the peak over the body (50 ms).
- `onsets.py`: arrival of every track at one onset.
- `rebow.py` and `rbmaster.py`: the final-chord re-bows, measured on the stems and on the master by band.
- `relq.py`: releases.

All times are measured from the score onset (`sq`). "b-6" means the stem reaches its body level minus 6 dB.

Delivery (from metrics.md):
- Master: -22.6 LUFS, LRA 23.6 LU, TP -4.1 dBFS.
- mp3: -19.8 LUFS, LRA 16.0 LU, TP -1.7 dBTP, p10-to-max span 18.5 dB, limiter about 1.7 dB. Motion of the mp3: 5.19 / 2.87.

## Where c26 stands (measured)

- **Tempo map.** It matches `global.ily` bar by bar, the same as c22. Examples:
  - bars 35-36: 49.2 / 45.0
  - bar 60: 63, 61, 59, then 47.1 (caesura)
  - bars 63-64: 50.3 / 42.6
  - bars 78-82: 50.3 to 44.0
  - bars 89-92: 48.4, 44.0, 39.9, then 36.8, 35.2, 20 (6.3 s final bar)
  - total 348.9 s
- **Keyswitches.** All of them come before their notes. The smallest gap is 13 ms (Ob1 207.95). The re-bow keyswitches are 23-26 ms before their notes. There are no clashes.
- **Entries, b-6 median / p90.**
  - winds +0.024 / +0.062
  - brass -0.023 / +0.028
  - strings +0.015 / +0.116
  - harp and timpani +0.003..+0.004
  - These are identical to c25 except Tbn1 212.5 (below).
- **Legato.** Stereo-crossover medians are +0.00..+0.05 on every track. Only the joins listed in findings 3 and 5 are late on both metrics.
- **Breaths.**
  - The caesura gaps at 204 are 0.19-0.23 s and at 268 0.09-0.23 s.
  - Wind breaths elsewhere are 0.23-0.42 s.
- **Releases.**
  - The tutti cutoffs at qn 9, 90 and 212 fall 15 dB within 0.1-0.4 s on every stem.
  - The final release is as recorded in c23.
- **Final-chord re-bows.**
  - In the 200 Hz-2 kHz band of the master, the dip at each re-bow is 0.8-4.7 dB, about the same as the chord's own movement.
  - The 30-200 Hz band moves 2-15 dB with no relation to the re-bow times. That is the irregular low-string beating the actor noted, not a timing effect.
  - One stem dip stands out: Cb 297.2, -9 dB for 0.1 s at +0.05..+0.10 s. In the master it is 4.5 dB in the 200 Hz-2 kHz band.

## 1. The violas, and in three places the second violins, enter late on soft entries; the extra lead added in c23 moved the attack but not the slow rise to full level (measured)

The violas have the latest entries of any track: b-6 median +0.130 s across their 7 entries, against +0.00..+0.03 for the other strings. The trace values below are stem level in dB relative to the body, per 50 ms from the onset.
- **Bar 1, qn 0** (the opening ppp chord).
  - Vla: b-6 +0.235, b-3 +0.36. Trace -15, -11, -10, -11, -8, -7, -8, -4, -2: full level only at +0.45 s.
  - Vln I, Vln II, Vc and Hn3 are at -6 or higher by +0.05.
  - The c23 extra lead did act: the c22 → c23 stems show the viola attack moved about 0.08 s earlier. But the sample's 18 dB, 0.5 s rise at CC22 / v31 is unchanged. The lead is now 0.24 s, near `ENTRY_CAP_S`.
- **Bar 23, qn 66** (theme C, the viola harmony). Vla +0.130 / +0.185; Vla div +0.080 / +0.180. The violins and basses are at -0.08..+0.02.
- **Bar 71, qn 238** (J, "unis., ord." pp eighth figure, page 6). Vla +0.182 / +0.242.
  - The first note is an eighth of 0.58 s, so it reaches its level a third of the way through.
  - Vln I/II, Vc and the harp at the same onset are at -0.08..+0.03.
- **Bar 84, qn 277** (coda). Vla +0.161 / +0.181.
- **Second violins.**
  - Bar 15 (qn 42): +0.116 / +0.141.
  - Bar 37 (qn 108, sul tasto): +0.142 / +0.267, while Vln II div is at -0.118. The two halves of the chord are still 0.26 s apart.
  - Bar 87 (qn 286, coda pp): +0.084 / +0.229, with a trace of -17, -14, -7, -9, -5, -3.

The fix that worked before is an entry fill. The c23 recipe on Vla 42 (fill 4 dB, hold 0.4) took that entry from +0.101 to -0.019.

**Fix** (`build/early_fills.json`, dict form). Short holds give arrival without overshoot. Simulated b-6 / b-3 and the peak over the body in 50 ms windows are in brackets:
- `"Violas"`:
  - `"0": {"db": 6, "pre_s": 0, "hold_s": 0.10}` (+0.060 / +0.080, peak -2.7)
  - `"66": {"db": 5, "pre_s": 0, "hold_s": 0.10}` (-0.005 / +0.085, +3.0)
  - `"238": {"db": 5, "pre_s": 0, "hold_s": 0.10}` (+0.002 / +0.182, +1.5)
  - `"277": {"db": 5, "pre_s": 0, "hold_s": 0.10}` (-0.009 / +0.076, +2.9)
- `"Violas div"`: `"66": {"db": 3, "pre_s": 0, "hold_s": 0.15}` (-0.010 / +0.080, +3.0)
- `"Violins II"`:
  - `"42": {"db": 5, "pre_s": 0, "hold_s": 0.10}` (+0.006 / +0.091, +1.4)
  - `"286": {"db": 6, "pre_s": 0, "hold_s": 0.10}` (+0.019 / +0.059, +0.8)
  - replace `"108"` with `{"db": 7, "pre_s": 0, "hold_s": 0.10}`. That is the existing 4 dB plus 3; simulated +0.04 / +0.14, peak about +1.8. It brings the bar 37 halves within about 0.16 s.

Keep all leads as they are. Make sure the qn 0 fill is written: the envelope must accept a point inside the pre-roll, as the Vln I qn 0 `vol_db` already does. Re-measure with `ent2.py` and `trace.py`. A peak over +3 dB in the first 0.35 s means the fill is too large.

## 2. Two pickups into new sections speak late, at the lead cap (measured)

- **Vc qn 139** (bar 44.75, the pickup into E at bar 45; Leg Slur first note, v53, lead 0.12).
  - Trace -8, -11, -11, -9, -7, -4, -2, and at body only from +0.35 s. The note is 1.0 s long.
  - b-6 +0.061, b-3 +0.301.
- **Vln I qn 171** (bar 52.75, the pickup into F at bar 53 "a tempo, poco a poco animando"; lead 0.30, which is the cap).
  - Trace -9, -9, -5, -4, -6, -12, -7, -3, and at body from +0.4 s. The note is 1.0 s long.
  - `probe_attacks.py` has flagged this note LATE (+0.34) in every cycle since c24.

So for most of their length these pickups sit 7-12 dB under their own level. The downbeats of E and F then arrive without an audible upbeat.

**Fix** (`early_fills.json`):
- `"Violoncellos"`: `"139": {"db": 5, "pre_s": 0, "hold_s": 0.25}` (simulated +0.021 / +0.041, peak +3.6)
- `"Violins I"`: `"171": {"db": 5, "pre_s": 0, "hold_s": 0.20}` (simulated -0.017 / +0.038, peak +2.9)

Optional: `"Violoncellos"` `"152": {"db": 4, "pre_s": 0, "hold_s": 0.15}`. This is bar 48 "poco sostenuto", now at +0.105 / +0.140; simulated +0.055 / +0.090.

## 3. In the Largamente climax, the second violins change notes 0.10-0.17 s after the first violins (measured)

Bars 61-62 (qn 204, 208), Leg BC MAX, ff. Each item gives crossover / pitch rise, with Vln I at the same onset after the semicolon:
- **Vln II 204** (C5 → A flat4): +0.103 / +0.140; Vln I +0.053 / -0.035.
- **Vln II 208** (C sharp5 → F5): +0.168 / +0.180; Vln I +0.028 / +0.030.

Both metrics agree, and the values are the same on c21 through c26. Vln I already has `leg_leads` 204 0.07 and 208 0.05; Vln II has only 206 (0.08), which now crosses at -0.047 / +0.21. At 54 bpm this smears the inner harmony at each half-bar change of the climax.

**Fix** (`build/leg_leads.json`, `"Violins II"`): add `"204": 0.05` and `"208": 0.08`. The totals are 0.22 / 0.25 s, under `LEG_LEAD_CLAMP` 0.35. The previous notes are 2 qn long, so the 0.45 cap allows about 1 s. Expected arrivals are +0.03..+0.08 on both metrics. Leave Vc 204: its two metrics disagree (+0.12 / +0.005).

## 4. Trombone 1's accents at bar 63 are 40-60 ms later than in c25, and behind the strings at qn 218 (measured)

In c26 the three accents moved from Sus Accent MAX to Sus MAX, which speaks more slowly. `score_to_parts.py` gives every `acc_art` note no lead ("keep the score onset, as Sus Accent had").

Measured on the Tbn1 stem (b-6, with the trace to body in dB per 50 ms from the onset):
- **212.5** (solo entry after a rest).
  - c25 Sus Accent: +0.021, trace +2, +5.
  - c26 Sus MAX: +0.086, trace -17, -4, -1, 0.
- **218.** c25 +0.0 (trace +4, +6); c26 +0.062 (trace -6, 0, +2).
  - On the same beat, Vln II, Vla, Vc and BTbn arrive at -0.023. So the trombone sits 85 ms behind the strings, at 42.6 bpm.
- **213** is a direct follow-on from 212.5 and is on time (-0.021).

Inferred: the swell now carries the weight, as item 9 asked, but the note front is late. A late trombone line in an ff tutti sounds heavy and behind the beat. That was not the aim of the change.

**Fix** (`tools/score_to_parts.py`):
- Add `ACC_ART_LEAD_S = {"Trombone 1": {212.5: 0.05, 218.0: 0.05}}`.
- In the shift loop's `elif n.get("acc_art"):` branch, set `shift[id(n)] = lead_qn(q, s)` for a listed onset, instead of `pass`.
- 217.5 ends at 217.875, so the 0.035 qn lead leaves a 0.09 qn gap. No overlap guard is needed.
- `ACCENT_SWELL_S_AT` matches onsets within 0.02 qn, and 0.05 s is 0.044 qn. Check with `STP_DEBUG_VOL="Trombone 1:212.5,218"` that the swell still attaches to these notes (keyed on the score onset). If it does, it then starts 0.05 s after the note-on, which keeps the no-front-edge shape.
- Expected: b-6 at about +0.035 (212.5) and +0.01 (218). Re-measure the 2-5 kHz attack minus body; it should stay at or under the c26 values (-0.8 / -9.4 dB).

## 5. The cor anglais falling semitone at bar 48.88 still arrives late (measured, low audibility)

- **Cor anglais qn 155.5** (A4 → A flat4, Leg Slur, lead 0.08 s): crossover +0.203, rise +0.265. c18 measured +0.113 / +0.035.
- It is the last solo join before bar 49.

**Fix** (`leg_leads.json`): `"Cor anglais"` add `"155.5": 0.08` (total 0.16 s, under the cap of 0.45 × the previous note). Expected about +0.05..+0.10.

Do not touch:
- The tempo map: `RAMP_SPANS`, the printed steps, `PHRASE_ARCS`, `TEMPO_PUSH`, `APEX_AGOGIC`, `BEAT_STRETCH`, `CAESURA` and `CAESURA_BREATH_QN`.
- The final bar (36.8 / 35.2 / 20 bpm), the fermata length and the tail hold.
- Keyswitch placement and the pre-roll CC36/CC69.
- The `REBOW_AT` points and `rebow_fills.json`: re-bow dips in the master's 200 Hz-2 kHz band are within the chord's own movement.
- All existing entry and legato leads, including the Vla 42 fill and the Cb `ABUT_LEAD`.
- Pizz., harp and timpani timing (+0.00..+0.05 s).
- The breath gaps.
