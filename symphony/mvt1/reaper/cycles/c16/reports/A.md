# Cycle 16, critic A: articulation and phrasing (render c15)

Scope: every wind, brass, string, harp, timpani and percussion note in `build/parts.json` (the c15 build after its stem fixes), measured on the c15 stems and master (`cycles/c15/render/`), with c14 (`cycles/c14/render/`, `cycles/c14/rendered_build/parts.json`) for before/after checks. Scripts and outputs are in `/private/tmp/claude-501/mockup-loop/mvt1-c16-A/`. The c15-A battery was rerun on c15 (`out_*.txt`). New scripts:
- `pkr.py`, `pkr2.py`, `pkr3.py`: short notes after a rest leading into a new pitch (pickups), by row. `pkr2` windows the pickup on its own sounding time (moved onset to the target's moved onset). `pkr3` uses score-onset windows (pickup score onset - 0.15 s to target score onset - 0.03 s), so it stays valid after a timing change; it is the pass measure.
- `acclate.py`: time after the score onset at which each accent reaches its peak - 3 dB, by row.
- `ssj.py`: SLUR_START_SUS pairs, second note against first.
- `volrise.py`: volume-envelope rises after a moved onset. `joinlen.py`: join dip against the length of the held note before it. `pairs.py`: two-note slurs. `tr2.py`: multi-track 40 ms traces.

## Checks that passed (measured)

- **Legato.** No chord on a Leg row. No keyswitch is sent after a note-on it belongs to. String join dips: median 1.7 dB whatever the length of the note before (308 joins after notes under 1 s, 33 after 3-6 s held notes, median 0.7). Joins of 6 dB or more: 14 string joins, all but two 9-15 dB under the master.
- **Re-bows (item 7).** Master dip at the 62 re-bows before qn 700 is -1.82 dB, against -1.72 dB at 35 control times. Final chords: the longest notes (22.5-22.7 s) have autocorrelation at the loop period of 0.16 or less. No wind, brass or timpani note over 6 s pulses: Bass clarinet 11 and Bassoon 2 684 traced flat within 1-2 dB over 5-7 s.
- **Accents (item 8).** 2-5 kHz in the first 80 ms minus the body: brass median -8.2 dB, winds -6.3, strings -4.6.
  - Readings over +3 dB: Clarinet 1 558 (+6.3) is a timbre change, not an attack. The slurred run into it is bright and the held Sus Non Vib A-flat5 goes 10 dB darker 0.12 s in, with no level peak; it sits 14 dB under the ff master.
  - Horn 3 317/321 read +3.4, and Violas 536 is the printed sub. mf.
- **Other articulations.**
  - Staccato separation: 6.7-14.6 dB median per track. Tremolo joins: median -0.8 dB, 1 of 33 at 4 dB or more. Breath marks: 3.1-15 dB. Pizzicato reaches -3 dB of its peak in 0.015-0.065 s.
  - Celli measured tremolo autocorrelation at lag 9: peak -0.08, 1-8 kHz +0.03, centroid +0.10.
  - The harp étouffez at 650 still damps the old pitches.
  - Timpani accent fronts: +1.1..+4.7 dB.
  - Tam-tam: the fff stroke at 484 rings 12 s. The pp soft-stick stroke at 696 has its 2-5 kHz band 46 dB under the master's, so it reads as a dark hum, as printed.
- **Patches.** I found no better Hollywood Orchestra patch to recommend this cycle.
  - The Vln II sul tasto passage (584-619) is a tremolo, and Flautando has no tremolo.
  - Celli `Meas Trem TS` is recorded at 145 bpm (c13 A).
  - The divisi KS Masters would not help tremolo chords whose level is already cut by voice count.
  - Timpani Flt (soft sticks) and Trumpet Sus Non Vib MAX are as printed.
  - The Sus rows that the fixes below need are already loaded on every track concerned.

## 1. Pickups after a rest play the legato row's slow first-note layer: the motive's upbeat is 9-21 dB under its note, and the accent behind it arrives late (transition, development, recapitulation)

**Measured** (`pkr.py`, `pkr2.py`, `pkr3.py`, `acclate.py`). The movement's main motive (eighth rest, eighth pickup slurred into an accented dotted quarter) enters again and again:
- the transition, bars 33-38 (Bn1, Vla, Vln I, Ob1, Cl1, Vln I);
- the development entries at letter E, bars 77-81 (BCl Solo, Cl1, Horns a2, Ob1 + Vln I, Vc);
- bars 94-96 and 109;
- the recapitulation, bar 139;
- the coda trumpets.

In the render the pickup is missing or nearly missing. A pickup is a note of at most 0.62 qn, with nothing sounding 0.2 qn before it, leading into a new pitch. "Peak" is the pickup's highest 40 ms level; "target body" is the next note from +0.1 to +0.4 s.

| Pickups on stems within 14 dB of the master | n | Own sounding time: pickup peak minus target body | Score windows (`pkr3`) | At -8 dB or lower |
|---|---|---|---|---|
| Winds, Leg row (slurred) | 11 | -8.0 dB | -8.6 dB | 6 |
| Winds, Sus row (tongued) | 8 | -3.0 | -3.3 | 1 |
| Strings, Leg row, slurred | 15 | -5.9 | -3.1 (all 43 Leg) | 4 |
| Strings, Leg row, unslurred | 28 | -3.0 | | 3 |
| Strings, Sus row | 11 | -1.6 | -0.4 | 0 |
| Brass, Leg row | 2 | -7.3 | -6.7 | 1 |
| Brass, Sus row | 4 | -0.7 | -0.7 | 0 |

Worst cases (own window / score window; stem against master at the target):

| Track | Pickup (bar) | Dynamic | Pickup minus target | Stem re master | Accent at peak - 3 dB |
|---|---|---|---|---|---|
| Violins I | 136.5 (35) | mf | -21.3 / -10.6 dB | -1.7 | +0.29 s |
| Oboe 1 | 312.5 (79) | mf | -14.0 / -14.5 | -7.6 | +0.32 |
| Bass clarinet | 432.5 (109) | | -13.6 / -12.1 | -1.7 | |
| Violins I | 380.5 (96), 372.5 (94) | | -13.8 / -5.5, -11.1 / -4.9 | -4.5, -5.6 | +0.23 |
| Bass clarinet | 304.5 (77, Solo espr.) | mf | -9.3 / -9.3 | -1.6 | +0.26 |
| Horns a2 | 310.5 (78) | mf | -8.9 (own) | -0.9 | |
| Violins I | 104.5 (27), 312.5 (79) | | -9.9 / -6.7, -9.7 / -5.1 | -6.8, -4.6 | |
| Flute 1, Oboe 1 | 552.5 (139) | | -8.9, -8.0 | -7.0, -11.5 | |
| Trumpet 1 | 664.5, 672.5 (167-169) | | -8.1 / -7.1, -6.6 / -6.3 | -4.9, -6.3 | |

Trace of Violins I bar 35 (40 ms frames):
- The F4 pickup (Leg Slur MAX, v73) rises from -63 to -51 dB over its 0.19 s. The master there is -32.
- The D-flat5 then starts at -43 dB at its moved onset (0.17 s early) and reaches -30 dB only 0.12 s after the beat.

Oboe 1 bar 79:
- The pickup lies at -58..-54 dB, the accent body at -38..-33 dB.
- The accent reaches its body 0.4 s after its moved onset.

Accent arrival (`acclate.py`):
- Accents on legato targets reach peak - 3 dB at a median +0.10 s (strings) and +0.13 s (winds), against +0.07 and +0.06 s on Sus rows.
- Of the 68 accents within 8 dB of the master, 15 arrive at +0.20 s or later. 12 of them are the targets of these pickups: Vln I 110, 137, 142, 149, 325, 381, 569; BCl 305; Cl1 307; Vc 382; Fl1 553; Bn1 129.

Cause:
- `score_to_parts.py` keeps these pickups on the Leg row:
  - for strings, a slurred note through `short_into_long` or the plain slur branch, and an unslurred note through the c02 "unslurred notes stay on Leg Slur MAX" branch;
  - for winds and brass, the plain slur branch, because `SLUR_START_SUS` requires another note ending just before.
- After a rest, the Leg row plays its sustain layer, which grows over 0.3-0.4 s (kit LEARNINGS line 138). An eighth at 112-126 bpm sounds only 0.12-0.27 s, because the target's legato lead cuts it, so it never reaches its level.
- The target's legato transition then starts from that quiet note, which is why the accent arrives late.
- c01 kept such pickups on Leg because on Sus MAX they sat 2.3 dB over their targets. Since then the targets carry accent swells and fitted steps (+3..+6 dB in the volume envelope at the targets above), and Sus-row pickups now measure -0.4..-3.3 dB under their targets.

**Inferred.**
- The motive is the movement's main cell. With its upbeat missing it starts on the accent, and the accent swells in instead of landing.
- This is most audible where the motive is exposed: Violins I bar 35, the bass clarinet solo at bar 77, the horns a2 at bar 78, the violins at bars 94-96.

**Fix** (generic, `tools/score_to_parts.py`; the values go in `build/score_config.py`):
1. Add `PICKUP_SUS = {"families": ("wind", "brass", "string"), "max_qn": 0.62, "rest_qn": 0.2, "level_db": {"string": -2.5, "wind": 0.0, "brass": 0.0}}`.
2. A note qualifies when:
   - it is monophonic, its written length is at most `max_qn`, and it is not tenuto or accented;
   - no note of the track sounds (by score) within `rest_qn` before it;
   - the next note starts at its written end (±0.02 qn) at a new pitch, is monophonic, and would play a Leg row (slurred, or a Leg BC/Leg Slur target).
   The target may be accented.
3. Then:
   - `n["art"]` = the Sus row, through the same `ks_lookup` chain as `SLUR_START_SUS`; mark it `pickup_sus`.
   - The test must run before `short_into_long`, the string slur branch and the c02 unslurred-Leg branch.
4. Extend the c15 `slur_start_joins` branch to `o.get("slur_start_sus") or o.get("pickup_sus")`. The target is led by min(`SOST_JOIN_LEAD_S`, 0.45 x the pickup) at `SOST_VEL`, as for `SLUR_START_SUS`.
5. Write the `level_db` as an exact level shape from the pickup's moved onset to the target's moved onset, not as a note trim (LEARNINGS c13: score-keyed trims miss early notes). New parts.json key: `pickup_sus`.
6. About 61 notes. Refit the accents of the targets afterwards (`fit_accents.py`, all three families; the pickups are neighbours).

**Pass** (`pkr3.py`, score windows, stems within 14 dB of the master):
- Pickups moved from Leg to Sus: pickup peak minus target body median between -2 and -5 dB in each family. None under -8, and none over -1 (the c01 risk of an accented upbeat).
- Violins I 136.5, Bass clarinet 304.5 and 432.5, Oboe 1 312.5: each between -6 and -1.
- Join dip into the targets (`joins.py`): median 4 dB or less.
- `acclate.py`: the 12 late targets at +0.15 s or earlier (median +0.10 or earlier).
- 2-5 kHz first 80 ms minus body on the targets under +3 dB.

## 2. Bar 51: the second theme's tenuto C5 (Horn 1 + celli) opens with a 10 dB hole on the beat, since the c15 Horn 1 lead

**Measured** (`tr2.py`, `efchk2.py`, c14 and c15).

Score: Hn1 200 E-flat4 slurred to 201 C5 (tenuto, the phrase's top, cresc 201-203), doubled by the celli. c15 put `leg_leads.json` Horn 1 "201.0" at 0.14 s (C #4); the note now moves 0.373 qn (0.20 s) early.

| | c14 | c15 |
|---|---|---|
| Horn 1 E-flat4 before the change | -37.7 dB | -35.7 dB |
| Horn 1 lowest point at the change | -41.2 (at -0.04 s) | -45.9 (-0.08..+0.00 s) |
| Horn 1 at +0.04..+0.08 s | -33.6 | -39.8 |
| Celli lowest at the change | -38.0 | -38.8 |
| Master at the beat (+0.04 s) | -29.5 | -33.1 (-36.2 at -0.06 s, from -28.6) |

The Horn 1 stem is 1.3 dB under the master there.
- `early_fills.json` Horn 1 "201.0" is still `{"db": 9.0, "pre_s": -0.06, "hold_s": 0.45}`, set for c14's 0.06 s lead. The fill starts 0.06 s after a hole that ends at +0.03 s. The c15 retime pass skipped this note on purpose.
- The volume envelope also steps to -2.5 dB at 200.877 qn (0.25 qn after the new moved onset) and holds to 201.055. In c14 it was -1.0 dB at 201.0-201.05.
- The recapitulation's notes (589, 601) have no hole (-35.8 / -32.2 dB through the change).

**Inferred.** The tenuto at the top of the dolce phrase sounds like a dropped note, in the horn solo's first phrase.

**Fix:**
- `build/early_fills.json` Horn 1 "201.0" -> `{"db": 7.0, "pre_s": 0.12, "hold_s": 0.35}`, so the fill is full from 0.12 s before the score onset (0.08 s after the moved onset).
- Find the source of the -2.5 dB point at 200.877 in `build_reaper.py vol_points` (it moved with the lead) and end it at the moved onset 200.627.
- Keep the 0.14 s lead (the horn-celli crossover passed).
- The celli dip into 201 (-33.2 -> -38.8 dB, from -0.16 to -0.04 s) is also partly ahead of its fill (`{"db": 6.0, "pre_s": 0.081, "hold_s": 0.189}`): set pre_s to 0.16.

**Pass:**
- Horn 1 dip at 201 under 4 dB against the E-flat.
- Horn 1 at +0.04..+0.3 s within -2..+1 dB of the E-flat.
- Master at the beat within 1 dB of c14 (-29.5).
- No overshoot over 2 dB (auto_fills measure).

## 3. SLUR_START_SUS: the joined second note of a two-note slur bumps 3-3.5 dB over the tongued first note (66 notes)

**Measured** (`ssj.py`, score windows). The c15 test (A #2) fixed the first notes. But the second note, joined at `SOST_VEL` 100 with the 0.12 s lead, peaks over the first note's body.

| SLUR_START_SUS pairs (all second notes 0.12-0.26 s) | n | Second body minus first | Second peak minus first body | Peak at +3 dB or more |
|---|---|---|---|---|
| Winds | 51 | -0.2 dB | +3.0 dB | 49% |
| Brass | 15 | +0.6 | +3.5 | 60% |

Exposed cases:
- Bassoon 1 130.5 -> 131 (bar 33, 1. Solo f espr., 3.7 dB under the master): +6.3 peak.
- Bass clarinet 434.5 (solo): +4.1.
- Bass clarinet 306.5 (bar 77 Solo): +3.3.
- Horns a2 312.5 -> 313: +9.5 peak, +8.8 body (6.8 dB under the master).
- Trombone 1 533.5: the second note at -21.6 against the first at -27..-29.

Two-note slurs measured with `pairs.py`:
- Brass: second minus first +2.4 dB (5 of 5 at -1 or louder).
- Winds and strings with short second notes: -1.0 / -1.1, half at -1 or louder.
- So the open c14 item (pair release too late on short notes) is still open, and the join makes it worse.

**Inferred.**
- A two-note slur is played strong-weak: the second note lighter, 2-4 dB.
- The v100 transition puts a push on the weak note, which inverts the figure in the espressivo solos.
- Where the second note is accented, the push is welcome; those are excluded from this fix.

**Fix** (`tools/score_to_parts.py`, `SLUR_PAIR_RELEASE`):
- For a second note under 0.35 s (written), start the release at the second note's moved onset: `from_s = 0.0` from the moved onset, full at `min(0.12, 0.5 x dur_s)`.
- Depth -3 dB on notes listed in `slur_start_joins` (the v100 push), the existing depth elsewhere.
- Skip accented and tenuto second notes.
- Keep `SOST_VEL` and the lead, which make the join arrive on time (LEARNINGS c15).

**Pass** (`ssj.py`, `pairs.py`):
- SLUR_START_SUS pairs: second peak minus first body median +0.5 dB or lower (share at +3 under 15%); second body minus first between -1.5 and -3.5.
- Short two-note slurs: median second minus first between -1.5 and -3.5 in each family.
- Join dip into the second note 4 dB or less.
- Bassoon 1 131 and the bass clarinet solos within those ranges.

## 4. Exposed celli joins: four fills still start after their holes (Lento bar 3, coda bars 164 and 172-174)

**Measured** (`efchk2.py` on c15). Of the 140 existing fills, 26 still dip 5 dB or more, and in 10 the hole's minimum comes before the fill is full. The ones in exposed lines:

| Track | Onset (bar) | Dip | Minimum at | Fill | Lead | Stem re master |
|---|---|---|---|---|---|---|
| Violoncellos | 694 (174) | 7.7 dB | -0.04 s | +4 from 0.00 s | 0.22 s | -1.0 |
| Violoncellos | 687 (172) | 5.2 | -0.12 | +6 from 0.00 | 0.22 | -1.1 |
| Violoncellos | 8 (3) | 5.8 | -0.075 | +6 from 0.00 | 0.22 | -1.7 |
| Violoncellos | 654 (164) | 5.9 | -0.08 | +4 from 0.00 | 0.11 | -7.4 |
| Oboe 1 | 182 (46) | 5.2 | +0.05 | +5 from +0.086 | 0.03 | -2.3 |

- The c15 "retimed" branch sets `pre_s = max(0, -t_min)` from one render. The fill becomes full exactly at that render's minimum.
- The celli holes move 0.05-0.1 s between renders (c15 CHANGES: 694 7.9 -> 7.7, 122 7.8 -> 8.6 after retiming).
- Celli 658 (minimum at -0.19 s, before its moved onset) belongs to the join before it. Celli 122 (8.6 dB in c15 CHANGES) is 7 dB under the master.

**Inferred.** In the coda and the Lento the celli carry the line 1-2 dB under the whole orchestra, so a 5-8 dB sag reads as a bow lifting.

**Fix:**
1. `tools/auto_fills.py` "retimed" branch, for Leg targets with a lead of at least 0.1 s: `pre_s = max(-t_min + 0.05, lead_s - 0.08)`. The fill is then full from 0.08 s after the moved onset, whichever render's minimum comes.
2. Hold to +0.35 s; db as now (at least dip - 3, cap 8).
3. Rerun on c15 with `--write`, keeping Horn 1 201 from #2.

**Pass:**
- The five rows under 5 dB on c16.
- No overshoot over 2 dB (the tool's 200 ms measure).
- Celli 0.5 s after each join within ±1 dB of c15.

## 5. Smaller items

- **Oboe 1 314.5 (bar 79, mf).** The slur after the accented B-flat5 plays at -45..-41 dB, 8-12 dB under the accent's body (-33). The accent's volume step is +4 dB and the following notes are at the same printed mf.
  - Measured on the stem (7.6 dB under the master); the Violins I doubling falls 4-5 dB.
  - Fix after #1 (the accent there is refit): `note_trims.json` Oboe 1 "314.5" +3 as a level shape from the moved onset 314.393 to 316.0.
  - Pass: 314.5-315.5 between 3 and 6 dB under the accent body.
- **Basses bar 72 (284 -> 285), hammer strokes** (accent + downbow on both). The bass entry lead moved 285 to 284.761, so the 0.25 qn `DETACH_ACCENTS` gap is gone: gap 0.011 qn, no dip on the stem (measured). Bar 32 and bar 83 keep theirs (master 8 dB at 124.96).
  - Fix: in the entry-lead pass of `score_to_parts.py`, do not lead a note in `det_str` by more than its detach gap minus 0.05 qn.
  - Pass: Cb 284/285 gap at least 0.15 qn; stem dip 4 dB or more.
- **Horns 3-4 a2, bars 80-81** (f pickup + accent, twice): still one solo horn sample (A #6 c15, deferred twice). The `TRACK_WINDOWS` second-staff routing is still the fix; it needs `build_track` to read the Hn3 staff's dynamics and articulations for that window.
- **Violins I 279 (bar 70)** join 9.4 dB and **Violins I 720** 8.6 dB: 13.6 and 8.9 dB under the master; leave them.

Do not touch:
- `SLUR_START_SUS` first-note rule;
- `RETONGUE_LEAD_S`;
- `WIND_DETACH` (brass dip -5 / dip_min_cc 84; tongued holes brass -5.1, winds -5.6, slurred -3.4/-4.0);
- `MEAS_TREM` alt_row with seed 464;
- `_REBOW_FROZEN` / `REBOW_AT` with `rebow_fills.json`;
- `GENTLE_ACCENT` (brass/wind/string accent fronts -8.2/-6.3/-4.6 dB);
- `TIMP_CC1_MAP` with `TIMP_ROLL_TRIM_DB`;
- the tremolo, staccato and pizzicato rows;
- harp `env_release_ms` 200 with `HARP_RING_S`;
- `PORT_TARGETS`;
- the Horns a2 windows and roles;
- the Horn 1 second-theme leads other than the 201 fill;
- tam-tam and sus. cymbal keys and timing;
- the climax order (160 > 122 > 169).
