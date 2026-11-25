# Cycle 10 changes (actor)

Snapshot of the c09 tools and build/*.json: `before/`. Scratch and analysis scripts: `/private/tmp/claude-501/mockup-loop/c10-actor/` (`sim.py` envelope simulation on the c09 stems, `checks.py` post-render checks, `A/` critic A's join scripts made cycle-configurable).

## Process

1. Edited the tools and config, regenerated parts.json, and diffed it against `before/build/parts.json`.
2. Simulated every level-only change on the c09 stems before rendering. The stems sum to the master, so I applied the new-minus-old volume envelope to each c09 stem, summed them, and ran `deliver_master.py`. The first version of C #4b (cuts starting after the sf) simulated a master peak of +2.1 dBFS, and the full sostenuto hold plus a string chain rise simulated a 4.9 dB limiter. Both were changed before the render; see below.
3. `build_reaper.py --midi-only` updated all 27 tracks, which needed no patch reload. It also did a full build of the new track.
4. REAPER was at 51 GB, so I saved, quit and reopened it. It reloaded to 52 GB with 0 GB compressed.
5. Rendered once. The attack gate passed 19 of 19.
6. The new solo track measured 12 dB over its accompaniment because its gain was a guess. Instead of rendering again, I set its gain from +6 to -1 dB in mix.json and in REAPER (`--midi-only "Violin I solo"`, then saved). I then rebuilt the master as the stem sum with stem 28 at -7 dB (`remix_solo_gain.py`). The rendered stems sum to the rendered master to -122 dBFS peak, so this equals a render. The original master, the original solo stem and the first mp3 are in `render_pre_gainfix/`, and the metrics from before the fix are in `metrics_pre_gainfix/`. I then re-ran `measure.py`, `probe_attacks.py` (19/19) and `deliver_master.py`.

## Accepted

**A #1: Violin I solo on its own track**
- New track 28, "Violin I solo", on `1st Violins Divisi/06 Keyswitch/1st Violins KS Master DIV A.oib` (the half section). I used the KS Master DIV A rather than the single Leg Slur patch, so the existing keyswitch code applies. Its key map is the same as the section's (dumped with `dump_ks.py` into the new `build/ks_maps_extra.json`, which `score_to_parts.py` merges).
- The patch file has only a Close mic channel, so the track uses send 0.5 for more hall, seat -0.55, width 0.2 and gain -1 dB.
- `TRACK_WINDOWS` routes Violin I notes with score onsets from 48 to 65 to the solo track. Violins I rests there. The solo's last note keeps its full length to 65.0, so it overlaps the tutti entry, and the `fresh` cut no longer applies.
- The solo gets SOLO_BOOST over the whole window. CC15 stays at 0 (senza sord.); two CC15 changes at the same time now keep the last one.
- Entry leads: Violin I solo 48 +0.13 s (moved from Violins I) and 60 +0.10 s. The roles.json entry Violins I [48, 65, -3] is removed.

**A #2 and A #4: early fills**
- `early_fills.json` now accepts `{"db", "pre_s"}`. The fill is 0 at onset - pre_s - 0.03 s, reaches +db at onset - pre_s, holds to onset + 0.10 s, and is back to 0 by + 0.35 s.
- The breakpoints are written exactly: parts.json `vol_bp`, which `build_reaper.py` adds to the envelope's 0.125 qn grid.
- New fills:
  - Cl1 266 {6, 0.10}, Fl1 270.5 {5, 0.06}, Hn1 203 {4, 0.10}
  - BCl 92.5 5; Ob1 270 4 and 142 4; CA 132 4; CA 133.5 4 -> 6
  - Vla 244 {6, 0.06}, 245.5 4, 254.5 {5, 0.04}
  - Vln II 59 5 and 60 5; Vc 77 5 and 86 4; Vln I 67.5 5
- `note_trims.json`: Bn1 231 +4.

**B #1 and C #1: soft trims**
- `soft_trim_db` global {ppp -2, pp 0, p +2} -> {+1, +3, +3.5}.
- Every per-track override +3/+3/+1.5: Cl1 {-1, 0, 0.5}, Cl2 {-0.5, 1.5, 3.5}, Bn1 {4, 6, 5.5}, Bn2 {5, 8, 6.5}, Vla {1, 5, 3.5}, Cb {1, 6, 6.5}.
- Roles: Oboe 1 [139, 151, 2.5], Clarinet 1 [280, 292, 3], Clarinet 2 [286, 292, -2] (also B #5).

**B #2: timpani loud attacks**
- `TIMP_LOUD_ATTACK_DB` 6: rolls and strokes printed f or louder get +6 dB from the onset (10 ms rise), held 0.25 qn, gone by 0.75 qn. The roll table and the settle are unchanged.

**B #3 and C #2: Trombone 1 marcato attacks**
- `VEL_SET` Tbn1 212.5 -> 108 and 213 -> 105. ACCENT_DB is kept.
- `deliver_master.py` TARGET_I -19.0 -> -19.5 (both critics' fallback, inside the -18 to -20 range).

**B #4: timpani bar 84**
- The +3 note trims at 277, 278.5 and 279 were replaced by the role Timpani [277, 280, 10]. A note trim ramps in over 0.6 s, so it lifted the ring and not the stroke.

**C #3: the bar 60 crescendo**
- A chained second crescendo now rises: `HP_CHAIN_RISE` {wind: 0.75}, so winds go from 4 to 7 dB.
- Winds only: a string rise simulated the bar 61 downbeat 2 dB over c09's peak, and the strings and brass already grew 5-15 dB across bar 60.

**C #4: the Largamente ff (bars 61-62)**
- (a) An hpgain arrival inside SOSTENUTO_SPANS holds `SOST_HOLD_SHARE` (0.5) x HP_GAIN_DB to qn 212, then releases over 1 qn. A full hold simulated a 4.9 dB limiter.
- (b) At a printed sf, the chord cut starts at the sf, not 0.1 qn before it. A role span that starts at an sf crossfades over [sf, sf + 0.25].
  - The first version started the cuts at sf + 0.25/0.35. In simulation that put the Vln I/II tremolo chord 10-14 dB over c09 and the master at +2.1 dBFS, so I rejected it.
- (c) A loud sf gets the ACCENT_DB envelope accent. Accents are now applied once per chord; before, each chord note added its own +2 dB.
- (d) String legato targets inside SOSTENUTO_SPANS use velocity 108 (`SOST_STR_LEG_VEL`).

**C #5: the coda arrival**
- No `bloomv` on a crescendo's arrival note.
- Vc, Vla and Cb at qn 286 play at velocity 60.

## Rejected or deferred

- **A #3 (portamento on 3-4 leaps): deferred.** It needs the Leg Port MAX row loaded, which means a patch reload of Vln I, Vln II and Vc, plus an f0 test of the slide length. With one render per cycle, a too-long slide could not be corrected this cycle. Do it with a short range check first.
- **B #3 "skip ACCENT_DB at velocity 115 or more": not needed.** Neither note is at 115 or more any more.
- **C #6 (swell held through crescendos, phrase-peak shaping): deferred.** It is lower priority. Also, C's example (Vln I qn 79.85-81.88) is a note trim ending at the next moved onset, not `swell_db`: notes inside a hairpin get no swell contour.
- **C #4a full hold and C #4b after-attack cuts:** changed to the versions above because of the simulated peaks.

## Measured, c09 -> c10

**Delivery**

| | c09 | c10 |
|---|---|---|
| Master integrated | -23.7 LUFS | -23.6 LUFS |
| Master LRA | 23.8 LU | 21.6 LU |
| Master true peak | -3.9 dBFS | -3.6 dBFS |
| mp3 integrated | -19.5 LUFS | -20.0 LUFS |
| mp3 LRA | 16.0 LU | 14.6 LU |
| mp3 true peak | -1.6 dBTP | -1.5 dBTP |
| mp3 p10-to-max span | 19.8 dB | 19.5 dB (target 16-19) |
| Limiter | 4.5 dB | 3.6 dB |

The ride still reaches its +10 dB cap.

**Solo (A #1)**
- Entries reach body - 3.8 dB (qn 48) and - 0.7 dB (qn 60) by +0.25 s. In c09, qn 48 sat at -60 against a body of -49 at that point.
- Hand-over at qn 65: the solo + section minimum in [-0.1, +0.35] s is 1.3 dB under the qn 64.5 level. c09 had a 6-7 dB hole.
- Level 5 dB over Vln II (-45.6 / -46.1 against -50.8 / -50.9).

**Joins (wjoin2 post-dip, dB)**

| Join | c09 | c10 |
|---|---|---|
| Cl1 266 | 10.5 | 4.4 |
| BCl 92.5 | 7.9 | 4.0 |
| Ob1 142 | 7.1 | 4.2 |
| Ob1 270 | 7.4 | 6.2 |
| CA 132 | 7.2 | 3.3 |
| CA 133.5 | 7.3 | 6.3 |
| Hn1 203 | 7.6 | 7.3 (not fixed) |
| Vla 244 | 9.4 | under 6 |
| Vla 245.5 | 7.5 | 4.1 |
| Vla 254.5 | 8.8 | under 6 |
| Vln II 59 | 8.3 | 7.0 |
| Vln II 60 | 8.2 | 6.1 |
| Vc 77 | 8.2 | 6.3 |
| Vc 86 | 7.0 | 6.1 |
| Vln I 67.5 | 8.5 | 4.8 |

Track medians are unchanged within 0.3 dB.

**Timpani attacks (timp minus mix, 50-250 Hz)**

| qn | c09 | c10 |
|---|---|---|
| 204 | -11.1 | -6.4 |
| 208 | -8.8 | -5.1 |
| 262 | -3.2 | -1.3 |
| 265 | -5.0 | -1.4 |
| 268 | -8.9 | -8.9 |

The roll bodies are unchanged (qn 205: -35.9, qn 263: -38.7).

**Trombone 1**

| Note | c09 peak / body | c10 peak / body |
|---|---|---|
| 212.5 | -7.5 / -25.7 | -15.6 / -26.7 |
| 213.0 | -9.5 / -23.6 | -12.5 / -24.9 |

The master's loudest sample is now the bar 61 tutti (qn 204.4).

**Bar 60 (C #3)**
- Slopes now: Fl1 +3.4, Ob1 +1.9, Cl1 +2.7 dB (c09 +1.1, -0.3, +0.5).
- The step into qn 204 is still +9.0 (Fl1) and +6.1 (Ob1).

**Bars 61-63 (C #4)**
- Bar 61 / 62: -17.7 / -20.1 (c09 -19.0 / -21.5). The 2.4 dB fall is not reduced; the target was 1.5 dB.
- The sf beat at 212: -21.6 (c09 -22.7).
- Bar 61 is now 5.3 dB over bar 79 (c09 4.1).

**Coda (C #5)**
- Vc / Cb at qn 286-289: -48.6 / -47.9 (c09 -55.2 / -50.9).
- Master qn 286 -> 289: -39.5 -> -42.2 (c09 -42.3 -> -45.7).

**Solos**

| Check | c09 | c10 |
|---|---|---|
| Cl1 minus Cl2, qn 286 | -5.4 | +0.4 |
| Cl1 minus Cl2, qn 287.5 | -6.6 | -1.6 |
| Cl1 minus Cl2, qn 289 | -1.9 | +3.1 |
| Ob1 minus Vc, qn 144 | -3.8 | -1.3 |
| Ob1 minus Vc, qn 146 | -0.3 | +2.2 |

**Timpani bar 84, A-weighted against the violas**

| qn | c09 | c10 |
|---|---|---|
| 277 | -8.0 | -1.8 |
| 278.5 | -9.0 | -2.8 |
| 279 | -11.6 | -5.7 |

The qn 280 ring is 19 dB under Cl1.

## Open
- Span 19.5 dB, 0.5 over the target. The ride is still at its cap in the ppp bars.
- Bar 62 still falls 2.4 dB from bar 61.
- Fl1/Ob1 step +6..+9 dB into bar 61.
- Hn1 203 join 7.3 dB: the hole starts more than 0.10 s before the onset.
- Cl1 is still 1.6 dB under Cl2 at qn 287.5.
- Timpani 279 is 5.7 dB under the violas.
- The solo patch has no Main mic. Check the solo's room against the section's.
