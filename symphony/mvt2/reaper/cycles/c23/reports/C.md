# Cycle 23, critic C: tempo, timing and transitions (on the cycle 22 render)

Material: `cycles/c22/render` (master and 32 stems), `cycles/c22/mvt2-mockup-c22.mp3`, `cycles/c22/metrics`, `build/parts.json` (03:51; the render is from 04:16, so this is the rendered data), `cycles/c22/before/parts.json` (the c21 data, used to measure the c21 render), `build/{entry_leads,leg_leads}.json`, `tools/score_to_parts.py`, `tools/build_reaper.py`, `v77/global.ily`, `build/mockup-events.tsv`, and score pages 2 and 5.

Scripts are in `/private/tmp/claude-501/mockup-loop/c23-C/`. They are the c19-C set, run on c22 and, with `PARTS=cycles/c22/before/parts.json`, on c21. New scripts:
- `both.py`: legato joins where the stereo crossover and the new pitch's rise agree. It also lists the c21 and c18 values.
- `cmp.py`: stereo-power stem levels around an onset, c21 against c22.
- `fin.py`: per-stem levels around a release or onset.
- `pt.py`: per-pitch harmonic energy trace.
- `secent.py`: section-sum entries.

Run them with `~/.venvs/claude-composes-reaper/bin/python`. Times are measured from the score onset (`sq`). "body - 6 dB" is the entry metric used since c07.

Delivery (measured with ffmpeg ebur128 and from metrics.md):
- Master: -22.5 LUFS, LRA 23.6 LU, TP -3.9 dBFS.
- mp3: -19.8 LUFS, LRA 16.0 LU, TP -1.6 dBTP, p10-to-max span 18.5 dB, limiter about 1.8 dB.

## Where c22 stands (measured)

- **Tempo map.** It matches `global.ily` bar by bar, the same as on c19. Bar means:
  - bars 35-36: 49.2 / 45.0
  - bars 53-59: 60.0 rising to 64.0
  - bar 60: 63, 61, 59, then 47.1 with the 0.22 s caesura
  - bars 61-62: 53.2 (the downbeats at 50.8)
  - bars 63-64: 50.3 / 42.6
  - bars 78-82: 50.3, 48.7, 45.5, 45.9, 44.0
  - bars 89-92: 48.4, 44.0, 39.9, then 36.8, 35.2 and 20 on the fermata beat (final bar 6.3 s)
  - total 348.6 s
- **Keyswitches.** All 255 come before their note's moved start (the smallest gap is 13 ms, Ob1 qn 207.95). There are no clashes.
- **Entries, body - 6 dB, median / p90** (c21 → c22):
  - winds +0.026 / +0.061 → +0.026 / +0.067
  - brass -0.021 / +0.076 → -0.022 / +0.021
  - strings +0.032 / +0.135 → +0.016 / +0.116
  - harp and timpani +0.003..+0.004
- **What the c22 CC-pull fix changed.** Soft string entries that already had leads arrived 0.08-0.14 s earlier at the same lead:
  - Vla 42: +0.101 → -0.009
  - Vc 42: +0.136 → +0.056
  - Violin I solo 48: +0.048 → -0.077
  - Vln I 65: +0.126 → +0.016
  - Vln I 237: +0.089 → -0.041

  This is the cause behind LEARNINGS 27 ("extra lead did not help soft entries"): before c22, the moved note started on the previous phrase's CC11. Entry leads on soft string notes now act, and that changes finding 1.
- **Legato.** Stereo-crossover medians: Vln I +0.018, Vln II +0.018, Vla +0.003, Vc +0.008, Hn1 +0.038, Fl1 +0.018, Ob1 +0.040, CA +0.013, Cl1 +0.048. The rise metric is identical on c21 and c22, to 0.005 s on every listed note.
- **Tutti arrivals.**
  - qn 204 (bar 61 ff): brass, contrabassoon and timpani -0.02..+0.07; strings +0.06..+0.12 (crossover).
  - qn 262: everything within -0.02..+0.10.
  - The caesura breath gaps are 0.19-0.23 s at 204 and 0.09-0.23 s at 268.
- **Final fermata and tail.**
  - The morendo falls evenly across the strings (bar 91 beat 1 → 303.5: -9.4 to -12.3 dB on every string stem).
  - After the release the mp3 falls -40.5 → -57.6 → -73.2 dB at +0.5 / +1.0 s, about 32 dB/s. The final cutoff of the Dvořák reference falls about 30-35 dB/s (-9 → -45 dB in 1.2 s).
  - The tail hold keeps every track's envelope flat after the release.

## 1. Soft string entries: the violas come in 0.2-0.26 s after the other strings at bars 1, 23, 71 and 84, and the low half of the bar 37 sul tasto chord 0.25 s after the high half (measured)

Measurements are body - 6 / body - 3 dB on each stem (`ent2.py`), with the section sum where a div track exists (`secent.py`). All values are the same on c21 and c22, except Vla 277 (c21 +0.187, c22 +0.257). No viola entry has an `entry_leads.json` extra, so each plays only the family soft lead (0.12 s).

- **Bar 1, qn 0, the ppp chord that opens the movement.**
  - Vln I +0.015 / +0.040, Vc +0.010, Hn3 +0.055.
  - Vln II +0.110 / +0.210.
  - Vla +0.195 / +0.350 (stereo sum +0.260).
  - So the chord fills in from the top and bottom, and the violas arrive last.
- **Bar 23, qn 66, theme C, "div." p chord C4/E flat4.** Vln I -0.03 and Vln II +0.02 (legato), Cb -0.075, Vla div +0.135, Vla +0.245 / +0.305. The Vla + Vla div sum is +0.215 / +0.280.
  - Levels (stereo power) from the beat: -58.8 at 0, -53.5 at +0.1, -51.9 at +0.2, -46.4 at +0.3, -42.4 at +0.4. The body is -42.
  - The viola harmony of the theme's first downbeat reaches its level a third of a beat late.
- **Bar 71, qn 238 (J).** Vla +0.113 / +0.268, against Vln I/II, Vc and the harp at -0.08..+0.03.
- **Bar 84, qn 277 (coda).** Vla +0.257 / +0.272, Vla div -0.028, timpani 0.00. The section sum is +0.147 / +0.247.
- **Bar 37, qn 108 (Poco più mosso, Vln II "div., sul tasto" pp).** The low note D flat4 on Violins II is at +0.197 / +0.327. The high note F4 on Violins II div is at -0.048. Both have the same 0.24 s lead.

**Fix** (`build/entry_leads.json`; the total stays under `ENTRY_CAP_S` 0.30):
- `"Violas": {"0": 0.12, "66": 0.12, "238": 0.08, "277": 0.10}`. These are new; the existing 54 and 140 stay.
- `"Violas div": {"66": 0.06}` (new track key).
- `"Violins II": "0": 0.06`, and `"108"` 0.12 → 0.18. The cap holds the 108 total at 0.30, so it gains 0.06.
- `"Violins II div": "108"` 0.12 → 0.06.

The rests before these notes are 3.8-14 s, so `prev_end` does not limit the lead. Expected:
- every viola entry at body - 6 dB +0.05..+0.13
- the bar 1 chord within about 0.08 s top to bottom
- the bar 37 halves within about 0.13 s (was 0.245)

Re-measure with `ent2.py` and `secent.py`. If a soft entry moves less than its added lead, record it as the sample's slow bloom (LEARNINGS 27) and leave it.

## 2. Bassoon 1's pp entry at bar 68 is late again since the c22 pull fix, and its f entry at bar 59 is late too (measured)

**qn 229 (bar 68), "1." pp, under the horn solo.**
- In c21 the moved note started on the previous phrase's CC11 and spiked (+14.8 dB over its body).
- In c22 it starts on its own CC11 34. It reads -53.6 at 0, -52.2 at +0.1, -51.7 at +0.2, -47.5 at +0.3 and -46.3 at +0.4, with the body about -44.
- Body - 6 dB comes at +0.127 and - 3 dB at +0.242. Horn 1, on its legato note at the same onset, is at +0.06 / +0.025.
- The note has only the family lead of 0.06 s. LEARNINGS 245 says to look at the lead tables after a bug fix; this is the case where a lead is now missing, not one that is now extra.

**qn 196 (bar 59, Sus MAX, f).** Body - 6 dB at +0.104 and -3 dB at +0.129 on both renders. Fl1, Ob1 and Vln I/II there are at -0.07..+0.01.

**Fix:** `build/entry_leads.json` `"Bassoon 1": {"229": 0.10, "196": 0.06}`. Totals are 0.16 / 0.12 s. Expected: 229 at about +0.03 / +0.14, and 196 at about +0.05.

Check with `cmp.py "Bassoon 1:229"` that the attack does not spike. It should not: the pull now holds CC11 34 from the moved onset.

## 3. Oboe 1's ff E5 at bar 62 beat 3 (qn 210) speaks 0.10 s late and reaches its level 0.35 s late (measured)

**Score.** Page 5, bar 62: the winds' ff tutti chord moves from F to F flat (E5 on the oboe) on beat 3, under "Largamente". The oboe has a portato pair: 208 F5 tenuto, then 210 E5 tenuto, the last note of the slur from 204.

**Data.** parts.json:
- 208 is Sus MAX, a re-tongued repeat (`sost_rep`, 0.04 s lead), ending at 210.03.
- 210 is Leg Slur MAX (`sost`, velocity 91) with a lead of 0.000. The shift loop gives a lead only to `leg_target`, `sost_rep`, `fresh` or entry notes. This note is none of them: it follows an overlapping Sus note.

**Measured** (`pt.py 22 "Oboe 1" 210 77,76`, 3-harmonic energy):
- E5 is absent until +0.05 s, crosses F5 at about +0.12 s, and reaches its body (37-40) only at +0.35..+0.45 s.
- Stem level: -33.7 dB from -0.1 to +0.2 s, then -27.0 at +0.3 and -23.1 at +0.4. That is 10 dB under the note's body for the first 0.3 s.
- The rise is +0.305 on c16, c18, c21 and c22 alike (crossover +0.12).
- Vln I's note change on the same beat crosses at +0.05.

**Inferred.** The KS Master joins the overlapping Sus F5 into the Leg Slur E5 like a legato transition. It does this with no lead, at the slow first-note layer.

**Fix** (`tools/score_to_parts.py`, the shift loop, before the `fresh` branch). For a wind note with `n.get("sost")` that is not a `leg_target`, and whose previous note in the track is a `sost_rep` or `sost_sus` note ending within 0.05 qn of it:
- Shift it by `lead_qn(q, SOST_JOIN_LEAD_S)` with `SOST_JOIN_LEAD_S = 0.12`.
- Give it `SOST_VEL` (100), the "firm, quick" join velocity.
- Leave the previous note's end at its present `e0 + 0.03`. It then overlaps the moved onset by about 0.14 qn, which is the legato-overlap condition.

As far as I can see in parts.json, only Ob1 210 matches. Fl2 and the clarinets repeat their pitch at 208/210, and their crossovers are at +0.03..+0.04.

Expected: crossover about 0.0, and body - 6 dB at about +0.2 instead of +0.33.

Related, for critic A/B: the re-tongued F5 at 208 drops from -24 to -31 dB and stays at -29..-33 for 2 qn. So the oboe's ff line steps down 5-7 dB at bar 62 before this late E5.

## 4. Four legato joins are still late on both metrics, and the same on c21 (measured)

Each item gives crossover / rise, then the c21 rise. The rule is the c19 one: change a lead only when both metrics agree.

- **Violins II qn 206** (bar 61.5, Largamente ff, A flat4 → C sharp5, Leg BC).
  - +0.103 / +0.290 (c21 +0.29).
  - The stem sits at -28 dB from 0 to +0.15 s between the -24 dB note before and the -19 dB note body at +0.4. The cellos at the same onset are at +0.05 / +0.03.
  - Lead now 0.17 s.
- **Violoncellos qn 255** (bar 76.67, A flat3 → D flat4, Leg Slur, the reprise climb).
  - +0.168 / +0.185 (c21 +0.185; c18 +0.008 / +0.12).
  - Vln I/II and Vla at the next onsets are within ±0.03.
  - Lead now 0.22 s.
- **Bassoon 1 qn 100** (bar 34.33, F3 → E flat3, pp, under the bass clarinet solo).
  - +0.133 / +0.225 (c21 +0.225).
  - Lead 0.06 s.
- **Oboe 1 qn 200** (bar 60 downbeat, B flat4 → C5, f, poco allargando).
  - +0.108 / +0.170 (c21 +0.17).
  - Vln I/II at the same onset are at -0.06 / -0.09.
  - Lead 0.06 s.

**Fix** (`build/leg_leads.json`): `"Violins II": "206": 0.08`, `"Violoncellos": "255": 0.08`, `"Bassoon 1": {"100": 0.08}` (new key), `"Oboe 1": {"200": 0.06}` (new key).
- The caps (0.45 × the previous note) allow 1.0-1.6 s at 206/255/100 and 0.42 s at 200.
- The totals stay under `LEG_LEAD_CLAMP` 0.35.

Expected arrivals are +0.03..+0.10 on both metrics. Vln II 80 also reads late (+0.19 / +0.26), but it sits at its 0.225 qn cap; leave it (LEARNINGS 144).

## 5. Viola falling steps from C4 and two other falling semitones arrive 0.07-0.17 s early (measured, low audibility)

Each item gives crossover / rise. All are identical on c18.

- C4 → B flat3 at qn 47, 59 (lead 0.26 s): -0.072 / -0.105.
- C4 → B flat3 at qn 70, 75 (lead 0.325 s): -0.127 / -0.160 and -0.137 / -0.160.
- F4 → E4 at qn 56: -0.097 / -0.170.
- E3 → E flat3 at qn 292 (coda, bar 89): -0.092 / -0.175.

**Cause.** `LEG_EXTRA_S["Violas"] = {60: 0.10}` adds 0.10 s to every departure from C4. It was set for rising steps (LEARNINGS 8). This is the same two-direction problem as Horn 1 F4 in c19 (LEARNINGS 204).

**Fix:** `LEG_PAIR_EXTRA_S["Violas"]` add `(60, 58): -0.10`, `(65, 64): -0.08` and `(52, 51): -0.08`. Expected: -0.05..+0.03. Re-check the rising C4 joins, which should be unchanged: 58 (C4 → D flat4) -0.03, and the `(60, 63)` triplets.

## Not changed, recorded

The final chord releases in two steps. Violins, violas, clarinet and timpani fall 10 dB within +0.05..+0.25 s of the release. The cellos and basses hold -59..-62 dB to +0.2 s and fall 10 dB by +0.35..+0.4. All notes end at qn 304 in parts.json, so this is the low strings' release samples and their resonance (inferred). A real section's basses ring a little longer too, and the master release is smooth (-53, -55, -58, -61, -70 dB at 0, +0.1, +0.2, +0.3, +0.5 s). Leave it.

Do not touch:
- The tempo map: `RAMP_SPANS`, the printed steps, `PHRASE_ARCS`, `TEMPO_PUSH`, `APEX_AGOGIC`, `BEAT_STRETCH` and the caesura amounts.
- The 20 bpm final beat and the fermata length, and the final tail hold and decay.
- Keyswitch placement and the pre-roll.
- `CAESURA_BREATH_QN` and the breath gaps.
- The c22 pull pad: it is what makes entry leads work on soft notes now.
- The family legato and entry lead tables, and the existing `leg_leads.json` and `entry_leads.json` values.
- The Cb `ABUT_LEAD`.
- Pizz., harp and timpani timing (+0.00..+0.04 s).
