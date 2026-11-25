# Critic C, cycle 58: tempo, timing and transitions (render c57, score v621)

Scripts and tables: `cycles/c58/critic_scripts/C/` (`edges2.py`, `classify.py`, `edges_all.tsv` with all 1312 edges, `entries.py`, `reatt.py`, `shortnotes.py`, `ks.py`, `pairs.py`, the `S_*.txt` outputs of `theme_S.py`). Nobody listened; every figure is measured on the c57 stems, the master, or `build/parts.json` unless marked inferred.

## Manual notes (pages chosen for this lens: 2021 manual PDF pp. 91-92, 94, 98; MANUAL-GAPS.md and DIGEST.md used)

| Manual (PDF page) | What it says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| p.91 | String Sustain: looped, "a good choice for slow-moving lines"; a round robin alternates up and down bows. | Violins II and Violas' repeated quarters in bars 23-25 and 135-137, the basses' repeated notes, all on Sus MAX | The row is used for moving repeated notes. Each new bow reaches 6 dB under its own maximum 130 ms after the beat on Violins II (finding 1). |
| p.91-92 | Marcato Sustain: a marcato sample plus the sustain samples, "extra power at the start of the note". | "Sus Marc LITE" is loaded on Violins I, II, Violas, celli | Used on Violins II 104-127 and 552-576 and Violas 104-127, where the repeats are on the beat (-0 to +31 ms). Not used in bars 23-25 and 135-137. |
| p.94, p.98 | Repetitions: "more realistic than just repeating the same note" because the bow change is in the sample; available for Violas and Basses; CC11 only, no velocity; tempo-synced. | Basses' repeated notes (44 in the theme spans, 15 later than +80 ms) | Not used. Not proposed this cycle (a new row on the basses needs a full rebuild and a range test); listed as an option. |
| p.98 | Trill row: "Play C0 in advance of the trill". The manual gives no minimum time for any keyswitch. | Keyswitch leads (finding 5) | 813 of 1043 changes are under 0.15 s before their note, 13 under 12 ms. No timing fault found from them. |
| MANUAL-GAPS | No new evidence from this lens. | | |

## Method

- Time map: `build/parts.json` `tempo` equals `cycles/c57/rendered_build/parts.json` `tempo`. Violins I's theme reads median S -1 ms in both spans, so the map and the render agree.
- Envelope: `STP_DUMP_VP` dump of `tools/score_to_parts.py` on `build/` (the output is byte-identical to `build/parts.json`), and the written points from `build_reaper.vol_points` (source cut before `ENV_LUA`). An edge is a run of the written envelope at 3 dB/s or more with 1.5 dB or more inside sounding notes. Each edge is split by the rule that wrote it: `role`, `carry`, `hp` (hairpin gain), `shape_slow`, `dyntrim` (the `mix.json` soft / dynamic trim read from the printed dynamic curve), `other` (tail hold, final fade, divisi cut). Timpani left out (its dynamics are in the envelope by design).
- The envelope of `build/` is the one the next build writes. It equals the rendered one for every `dyntrim`, `role`, `hp` and `shape_slow` edge; the carry rows differ (changed by the stem fixes after the render).
- Checked on the stems: Trombone 1 448, Horn 3 144, Tuba 520 (stem level against stem minus envelope in 10 ms steps).

## Findings, ranked by what a listener would gain

### 1. Violins II and Violas play the repeated quarters under the theme a tenth to a quarter of a second late (bars 23-25 and 135-137; measured)

**Answer to the coordinator's question.** Where Violins II and Violas are on Sus Marc LITE (Violins II 77.9-82.1, 104-127, 552-576; Violas 104-127) they are in time with Violins I: same-pitch repeats come within 6 dB of their own maximum at -0 ms (Violins II, n 4) and +31 ms (Violas, n 2), with the maximum at 21 % and 50 % of the note. In bars 23-25 (qn 88-100) and 135-137 (qn 536-548) they are not on that row. They play repeated quarters (mf cresc. to ff, accent on every third) on Sus MAX with lead 0 after a 90 ms gap:

| Track, row, class | n | lead | within 6 dB of own maximum, ms after the beat (quartiles) | later than +80 ms | maximum at |
|---|---|---|---|---|---|
| Violins II, Sus MAX, repeat | 17 | 0 | +130 (+105, +215) | 14 | 93 % of the note |
| Violas, Sus MAX, repeat | 20 | 30 | +67 (+37, +94) | 8 | 68 % |
| Double basses, Sus MAX, repeat | 44 | 0 | +65 (+25, +95) | 15 | 65 % |
| Violins II, Sus Marc LITE, repeat | 4 | 92 | -0 (-5, +10) | 0 | 21 % |
| Violins I theme (S, 79 notes) | | | median -1, robust SD 12 | | |

Violins II bar 23: the stem is at -58 to -60 dB for 110 ms after each beat, reaches -52 dB at +170 to +230 ms and its maximum (-46, -42 dB) at +300 to +380 ms, just before the next beat. The section is heard swelling into each next beat while Violins I play the theme on the beat. `theme_S.py` reads the same notes +115 to +230 ms (Violins II 88, 89, 90, 93, 95, 96, 98, 99, 100; 537, 538, 540, 543, 544, 546) and +76 to +151 ms (Violas 89-99). The c56 readings are within 30 ms of these, so this is not new in c57; the per-note layers did not hide it either.

Cause (read in the tools): `STR_REP_NEW_BOW["sus_min_s"]` is 0.4 s; after `REP_MIN_GAP` the quarters sound 376-386 ms, so they get no re-bow lead.

Celli against Violins I: 21 shared onsets, S difference robust SD 55 ms, 6 over 60 ms (qn 60, 70, 82, 86, 88, 94; all Leg BC MAX joins with a 150 ms lead or the entry at 88). c56 read 46 ms and 4 over 60 with the same MIDI on these notes, so no new fault and no row proposed; the celli's lines here are slurred counter-lines, not the repeated figure.

**Fix** (`build/score_config.py`, no envelope):
- `_C54_STR_SPANS["Violins II"]`: add `(88.0, 100.0)` and `(536.0, 548.0)`; `_C54_STR_SPANS["Violas"]`: add `(88.0, 100.0)` and `(536.0, 548.0)`. They then take the c54 "marc" spec (Sus Marc LITE, `rep_lead_s` 0.085).
- Expected: within 6 dB of own maximum at 0 ± 30 ms (the value of the Marc LITE repeats in this render), from +130 and +67 ms. Range test bars 23-25 first. If the Marc front is too heavy against the theme (front minus tail was 7.5 dB on Violins I), the fallback is Sus MAX with `STR_REP_NEW_BOW["sus_min_s"] = 0.35` so the 0.10 s lead applies; expected +130 -> about +30 ms.
- Basses: give the same-pitch repeats a lead. `RETONGUE_LEAD_S["Double basses"] = 0.06` (they have no entry; `sus_lead_s` does not reach notes under 0.4 s). Expected median +65 -> about +5 ms. The three worst (qn 66, 70, 84: 6 dB under the maximum only at +285 to +350 ms) are low G#1 / G1 / F1 notes that swell for their whole length; they need critic B's region gains, not a lead.

### 2. Envelope edges that land inside sounding notes: 392 of 3 dB or more; the largest class is the dynamic trim stepping during the first 60 ms of an entry (measured)

All edges of 3 dB/s or more with 1.5 dB or more inside sounding notes, timpani left out: 1312. Counting for onset edges only the part after the new note's note-on: 1178 (392 of 3 dB or more, 92 of 6 dB or more). Full list with step size, position and where to key each: `cycles/c58/critic_scripts/C/edges_all.tsv`.

| Class | Position | 1.5 dB+ | 3 dB+ | 6 dB+ | Main rule (3 dB+) | Where it should be keyed |
|---|---|---|---|---|---|---|
| A | onset edge of a note that follows a rest of 0.15 s or more; the step ends at the score onset, the note-on is one lead earlier, so the step lies in the first 50-240 ms of the note | 251 | 125 | 51 | dyntrim 104, shape 6, role 5, other 5, hp 3, carry 2 | wholly in the rest, finished at the moved note-on |
| B | onset edge of a legato target joined to the note before | 136 | 41 | 7 | shape 11, dyntrim 10, carry 9 | leave at the score onset: the lead is the transition time, the pitch changes at the score onset |
| C | onset edge of a new bow or tongued note that follows within 0.15 s (lead 35-120 ms) | 217 | 69 | 11 | dyntrim 21, carry 15, hp 14, shape 10 | centred on the moved note-on (in the 30-140 ms gap) |
| D | no onset near: inside a held note | 574 | 157 | 23 | hp 54, dyntrim 32, shape 28, other 23, carry 11, role 9 | see below, by rule |

By family at 3 dB or more: class A brass 67, strings 32, winds 26; class D strings 74, brass 42, winds 40.

**Class A, the 14 largest (all 125 are in the TSV).** Step, time re note-on, cause:

| Track | qn (bar) | Step | Lies | Lead | Cause |
|---|---|---|---|---|---|
| Trombone 1 | 448 (113) | +15.5 dB in 60 ms | 0 to +60 ms after note-on | 60 | dyntrim |
| Trombone 1 | 156 (40) | +13.3 / 60 ms | 0 to +60 | 60 | dyntrim |
| Horn 3 | 144 (37) | +12.9 / 60 ms | 0 to +60 | 60 | dyntrim |
| Tuba | 520 (131) | -15.1 / 60 ms (12.7 inside) | -10 to +50 | 50 | dyntrim |
| Horn 3 | 578 (145) | +12.4 / 61 ms | -1 to +60 | 60 | dyntrim |
| Horns a2 | 272.5 (69) | -12.0 / 60 ms | +10 to +70 | 70 | dyntrim |
| Horn 4 | 144, 289, 576 | +11.9, +11.6, +11.6 / 60 ms | 0 to +60 | 60 | dyntrim |
| Horn 1 | 170, 497, 440 | +12.2, +11.8, +16.5 (10.8-11.7 inside) | -49..-119 to +60..+70 | 60-70 | dyntrim (440: carry +3.7) |
| Trombone 2 | 448 (113) | +11.4 / 60 ms | +20 to +80 | 80 | dyntrim |
| Horn 2 | 620, 440 | +11.2, +10.1 / 60-70 ms | 0..+10 to +60..+80 | 60-80 | dyntrim |
| Tuba | 440 (111) | +11.0 / 60 ms | 0 to +60 | 60 | dyntrim |
| Flute 1 | 291 (73) | +11.5 / 60 ms (10.6 inside) | -5 to +55 | 55 | dyntrim, role +1.2 |
| Bass trombone | 452, 156 | +10.6, +10.0 / 60 ms | 0 to +60 | 60 | dyntrim |
| Violoncellos | 332, 136 | +8.6, +8.2 / 60 ms | +60 to +120, +180 to +240 | 120, 240 | dyntrim |

Mechanism (read in `tools/build_reaper.py` `vol_points`): the dynamic trim is read from the printed dynamic curve at score time on a 0.125 qn grid, so it steps on [score onset - 0.125 qn, score onset]. The tail hold keeps the old level through the rest and stops 0.35 s before the moved note-on, but the values after it still come from the old dynamic until the score onset. The note-on is one lead before the score onset.

What it does to the sound (stems): Trombone 1 448: the instrument (stem minus envelope) is within 3 dB of its body 20 ms after note-on; the stem gets there at +50 ms because the envelope climbs 15.5 dB under it. Horn entries with an upward step (26 entries on Horns 1-4, median step +9.2 to +11.4 dB): the stem reaches 10 dB under body 19 ms before the beat, the instrument 31-37 ms before. Downward steps do the opposite: Tuba 520 starts with the envelope 15 dB too high, so the first 40 ms of the attack are raised by up to 11 dB; Horn 4 273 and Horns a2 272.5 the same (-10 to -12 dB in the first 50-70 ms).

**Fix for classes A and C** (`tools/build_reaper.py` `vol_points`, generic, default off; one rule, no per-note data): `ONSET_KEY = {"min_rest_s": 0.03, "ramp_s": 0.06}`. For every note that is not a legato target and whose moved note-on m is before its score onset s: the written value on [m, s] is `val_at(s + 0.001)`; the ramp to it ends at m and starts `ramp_s` before m, or at the end of the previous note's release when the rest is shorter. The tail hold then ends at that ramp instead of 0.35 s before m. Legato targets (class B) keep the present timing. Add m and m - ramp to the envelope grid (`vol_bp`).
- Expected: class A 251 -> 0 edges inside the note (125 of 3 dB or more); class C 217 -> the part after the note-on becomes 0 and the step sits in the gap before the new bow.
- Side effect to handle in the same build: brass entries with an upward step will speak 12-18 ms earlier (they are at -19 ms now). `ENTRY_LEAD_S` soft values for Horn 1-4 0.06 -> 0.045, Trombone 1-2 and Bass trombone the same step; check on the render with `entries.py` (target 10 dB under body at -20 ± 15 ms).

**Class D, by rule, with the largest of each:**
- `hp` (131 edges, 54 of 3 dB or more): the hairpin-gain release, `HP_REL` 1.0 qn after the arrival (0.48 s at 126). Bassoon 2 104 and 388, Clarinet 2 104, Flute 2 488 and 558, Bass clarinet 560: -4.0 dB in 0.42-0.53 s starting 80-145 ms after the note-on of the arrival note. Bars 115-116 (qn 460-464) Flute 1 +7.3, Flute 2 +6.7, Oboe 2 +6.1, Oboe 1 +5.3 dB over 1.3-1.6 s inside the held note (hairpin gain 2.2-3.6 plus the trim). Fix: `build/score_config.py` `HP_REL = 4.0` (qn; `tools/score_to_parts.py` line 220), so a 3-4 dB release takes 1.9 s at 126 (1.6-2.1 dB/s, under the 3 dB/s limit). Expected: 131 -> under 20. Check that no release runs into the next hairpin's start (the chained form `hp_chained` already holds).
- `carry` (91, 11 of 3 dB or more) and carry onset edges (class B/C 147): 1 qn ramps centred on bar lines whatever sounds there. Trumpet 2 451.6-452.6 -4.8 dB 1.8 s into a held note; Violins II 319.6-320.25 -4.7; Oboe 2 163.6-164.5 -4.0; Double basses 167.6-168.5 +3.6; celli 91.6-92.6 and 207.6-208.5 -3.4. These go with the carry rows (this cycle's item 1). Any row kept as a role row: start and end it in the rest named in the TSV column `key_to`, or at the phrase's first moved note-on.
- `role` (82, 9 of 3 dB or more): 0.5 qn span ramps. Celli 348.6-349 -4.5 dB 0.42 s into a 0.83 s note (rest at 346.45-346.95); Tuba 495.4-496.75 +4.2 dB 4.5 s into a held note; Trumpets a2 677.1-678 +4.0 (rest 672.0-672.35); Bassoon 2 499.1-500.1 +3.5; Bass trombone 495-495.9 +3.3. Fix: `build/roles.json`: move each row's edge to the rest in `key_to`; where the note is held with no rest (Tuba 488-499, Bassoon 2 496-500) lengthen the ramp to 4 qn (fourth value of the row).
- `shape_slow` (67 in D, 28 of 3 dB or more; 49 more on onsets): several kept "slow" shapes have per-note edges inside them. Violins II 80.38-80.60 +11.4 dB in 107 ms inside the note at 80.5, and 78.0-78.55 -7.5 dB; Violas 76.95-77.05 -6.5 dB and 77.65-77.75 +6.5 dB (a 0.7 qn hole); Cello solo 686.9-687.3 +13.0 dB in 378 ms, 685.1-685.7 -9.8, 680.05-680.6 -8.8, 689.4-689.55 +5.7; celli 343.44-343.48 -7.5 dB in 19 ms, 456.1-459.1 -8.3; Double basses 675.97-676.1 -3.8 dB in 62 ms. These are per-note level moves under Dan's rule. Fix: `VOL_SLOW_ONLY` gets `"slow_max_db_s": 3.0`; a `shape` item with any segment steeper than that is dropped, not kept (`tools/score_to_parts.py` line 6049). Cost to list in CHANGES: the Cello solo's bars 171-174 lose about ±9 dB of shaping, to be replaced by CC11 per phrase.
- `dyntrim` inside held notes (51, 32 of 3 dB or more): the trim following a printed hairpin at 4-7 dB/s (Horn 3 620.1-623.1 -10.3 dB in 1.56 s; Horn 4 662-663 -9.8; Horn 2 662.25-663 -9.7; Horn 4 505.5-507.25 -8.3). These are ramps on printed hairpins and belong to the dynamics mapping (critics A / B); not counted as timing faults. Bar 41 is different: Violins I 160.12-160.63 -8.1 dB, Tuba -6.5, Horn 3 -6.0, Trumpet 3 -5.1, celli -4.5, Trumpet 1 -4.5, Oboe 1 -4.3 dB, all 100-360 ms after the fff note-on at 160: the trim follows the printed drop after the arrival and cuts the attack's body. `ONSET_KEY` does not cover it; if the drop is a printed fp-like mark, move it into CC11.
- `other`: the final fade (-5 dB at 727.62-727.75 on all strings) is in finding 4.

### 3. Violins I theme: the per-note leads ate two pickup notes and left two phrase starts late (measured)

`theme_S.py c57 "Violins I"`: 56-127 n 79, median -1, robust SD 12 ms, 6 more than 40 ms from the median, 3 more than 60. 536-576 n 38, median -1, robust SD 18 ms, 9 more than 40, 4 more than 60. (c56, Marc row: 12 ms / 2 and 12 ms / 4.) The outliers are these notes, not noise:

- **qn 59.5 -> 60 (bar 15 beat 4.5 -> bar 16) and 571.5 -> 572 (bar 143 -> 144): C5 eighth, then C5 again.** The repeat's lead was fitted to 152 ms (`steady57_at.json` "60.000" and "572.000"; the class value is 50). With the 90 ms repeat gap the pickup eighth sounds 80 ms of its 238 ms. On the stem the pickup's slot is at -43 to -46 dB against -35 dB before and -38 dB after: the pickup does not speak. The downbeat still comes within 6 dB of its maximum only at +303 ms (60) and +183 ms (572). S reads +167 / +165 on both, as it did before the fit: the estimator cannot see a same-pitch repeat, so the fit moved the lead without moving the reading.
  Fix: `build/steady57_at.json` delete "60.000" and "572.000" (back to the 50 ms class lead), and "59.500" / "571.500" stay. Give the theme's repeats a 60 ms gap: `STEADY_LINE["Violins I"]` `rep_gap_s` 0.09 -> 0.06 (`build/score_config.py` line 4258). Expected: pickup sounds about 128 ms and reaches the level of its neighbours within 4 dB; downbeat within 6 dB of its maximum by +100 ms. Range test bars 15-16.
- **qn 88 (bar 23) and 536 (bar 135): first note of the phrase, Eb5, lead 160 ms, CC11 72.** Stem 10 dB under body at the beat, within 6 dB of the maximum at +165 / +155 ms, maximum at +350 ms. S +109 / +104. Fix: `steady57_at.json` "88.000" and "536.000" `lead_s` 0.16 -> 0.245 (lead + 0.8 x S); there is a 366 ms rest before both. Expected S +20 ± 20 ms.
- **Leads fitted to 0 that now read late:** 573.0 (bar 144 beat 2, lead 0: S +65, crossover +76, dominant +61) and 570.5 (bar 143 beat 3.5, lead 0: S +44). Fix: "573.000" 0.062, "570.500" 0.03.
- **Early by more than 40 ms with two estimators agreeing:** 539.0 (lead 107: S -63, dominant -84), 558.0 (lead 124: -46 / -76), 574.0 (lead 99: -41 / -40), 76.5 (lead 80: -42 / -42). Fix: `lead_s` 0.06, 0.08, 0.06, 0.04.
- Left alone: 561.5 (estimators disagree, -55 / +57), 114.0 and 123.0 (entries after rests, pcx only), the Staccatissimo at 113.5.
Expected after these rows: 536-576 robust SD 18 -> about 12 ms, notes over 40 ms 9 -> 3 or fewer; 56-127 6 -> 3.

Three more notes cut the same way on other tracks (`shortnotes.py`): Violas 135.5 sounds 81 ms of 238 (next note leads 207 ms; slot at -46 to -50 dB, next note -39), celli 313.5 100 ms of 238, Violins I 455.5 78 ms of 225 (next note leads 165 ms). Fix: cap the following note's lead at 45 % of the slot for these onsets (`retongue_leads.json` / `leg_leads.json` rows: Violas 136.0 -> 0.10 s, Violins I 456.0 -> 0.10 s).

### 4. The last chord does not die away: three new bows surge in the top voice and the level rises 4 dB inside the ppp fermata (bars 181-182; measured)

Printed: diminuendo from 720, "morendo", ppp fermata at 724, 8 s at 30 bpm.
- Master, 1 s steps from qn 724: -48.8, -48.7, -46.1, -44.5, -46.8, -47.2, -46.1, -51.8 dB. The chord is 4.3 dB louder in its fourth second than in its first, and its seventh second is louder than its first. After the end: -61 dB, -90 dB at +0.75 s (the attacca gap is clean; mp3 ends 1.63 s after the score end).
- Violins I (C5, top voice): re-bow pieces at 722.78, 724.47 and 726.51. Stem -50 dB before; -64.6 dB at the first re-bow; -62.0 dB at the second; then up to -44.0 and -43.4 dB (qn 725.2-725.8, 2.3-3.5 s into the fermata), down to -58.8 dB at the third re-bow, back to -50.3 dB. Range 21 dB on a held ppp note. Stem minus envelope swings -70.8 to -52.9 dB, so it is the instrument: each Sus MAX piece at CC11 22, velocity 38 takes about 1.4 s to speak.
- The envelope adds to it: carry rows for bar 182 are +3.8 (Violins I), +3.7 (Violins II), +7.7 (celli), +5.0 dB (basses), after +6.0 / +10.2 dB in bar 181 on Violins II / basses; on Violins I the written envelope rises from +5.3 to +11.3 dB between 723.6 and 726. CC11 is flat at 22 from 724.0 to 727.6 on all five string tracks.
- c54 measured this chord at -48 to -52 dB for 6 s with a taper to -63 dB (per-note re-bow fills were in place).

**Fix** (instrument side):
- `build/score_config.py`: no automatic re-bow inside the last chord on Violins I and Violins II (`REBOW_AT` for the two tracks with their bar 180-182 points removed, or `AUTO_REBOW` off from qn 720): one bow from 720 / 720.5 to the end. The loop period is 3.95 s; with the level falling under a morendo the loop is less exposed than three holes of 12-14 dB. Violas, celli and basses keep theirs but staggered against each other as now.
- CC11 carries the morendo: all strings 22 at 724.0 falling to 14 at 727.0 (then the existing fall to 8), in the rule that writes the final `fade` (`tools/score_to_parts.py` line 3694 writes the CC part of it).
- Delete the bar 181-182 carry rows (`build/balance57.json` Violins I [724, 728], Violins II [720, 724] and [724, 728], Violoncellos [724, 728], Double basses [720, 724] and [724, 728]); if the chord's balance needs it, one role row from 712 that is level through 728.
- Expected: master falls monotonically from about -47 to -55 dB over the fermata; no step of more than 3 dB in the Violins I stem. Range test bars 179-182.

Other endings checked (no fault): the bar-14 rest before the Allegro (master under -70 dB from 1.0 s before the downbeat); the fermata at 679 (2.5 s; -50 dB at +0.5 s, -76 dB at +2.0 s; the solo enters 0.25 s before 680 by its lead); the tutti stop at 128.5 (-21.6 -> -39 dB in 0.3 s). The caesura at 636 dips the master only 3.5 dB for 150 ms (the cymbal roll and timpani ring through by design).

### 5. Keyswitch leads (measured; no fault found)

1043 row changes after the pre-roll. Lead to the first note-on after them: minimum 9.5 ms, median 23 ms; 13 under 12 ms (less than one 512-sample block), 560 under 25 ms, 813 under 0.15 s. Of the 813: 425 go into a legato row inside a line, 279 leave a legato row inside a line, 97 are between non-legato rows, 12 have a rest of 0.2 s or more before the note.
- The 13 under 12 ms: Violas 576.0, 292.0, 300.0; celli 289.14, 180.0, 182.0; Violins II 176.0, 180.0, 188.0, 196.0, 208.0, 212.0, 580.0. Eight are re-bow pieces (Leg Slur MAX -> Sus MAX on the same pitch, in a 14-16 ms gap); five go into Leg Slur MAX with the old note still sounding.
- The scherzo's failure (a keyswitch 7 ms before a legato note, the note silent in some renders) does not show here: the five into-legato joins read the same in c56 and c57 (Violins II 180 +18 / +28 ms, 196 +8 / +10, 212 +40 / +18; Violas 300 -55 / -55; celli 182 +27 / +45, crossover).
- Of the 16 re-bow holes in c57's list, 5 have a keyswitch 9.5-40 ms before the piece (Violins I 44, Violas 725.5, celli 26.5, 180, 289.1); 11 have none. The keyswitch is not their cause.
- Proposal, low priority: `tools/score_to_parts.py` `early_time`: a seconds rule `KS_ROWCHANGE_LEAD_S = 0.15` for changes whose target is not a legato row (376 changes) and for the 12 with a rest; never earlier than 20 ms after the previous note-on. Leave the 425 into-legato changes (the Finale measured joins 36-45 ms later with early keyswitches on legato lines).

### 6. Smaller items (measured)

- **Tempo map against `global.ily`:** every printed step is played within 1.5 % per half bar except the intended ones: Lento agogics (bars 4, 9-12, 14: 45.7-51.5 against 50), second-theme and closing arcs (bars 50, 55, 58, 61, 150, 155: 108.1 against 112), bar 122 (the smoothed allargando, ±2.5 %), bar 126 and 162 (96.5 against 100), the caesura at 636, bar 174 (65.8 against 72, the solo's phrase end), bar 181 (48.2), the fermata beat 679 (24 against the 40 used for the MIDI) and the last bar (30). No unprinted step inside 56-128 or 520-576. No change proposed.
- **Tutti arrivals** (clean entries, time of 10 dB under body): 10-90 % spread 28-81 ms at 18 arrivals (median of the parts -9 to -39 ms). Oboe 2 is the earliest part at 100, 128, 160, 324, 484 and 548 (-75 to -153 ms; its 0.18 s loud lead). Its body-3 dB point is on the beat at 100, 324 and 548 (slow front), but 160 is early on both measures (-153 / -99 ms). Fix: `build/entry_leads.json` Oboe 2 "160.0": -0.10. Trumpet 2 leads 90 ms and starts -45 to -69 ms at seven arrivals; `ENTRY_LEAD_S["Trumpet 2"]` loud 0.11 -> 0.08 (inferred, 1:1 on a fast attack).
- **Violins II / Violas held accompaniment notes in bars 15-20** (Leg Slur MAX entries at 57.5, 65.5, 73.5, 76.5): within 6 dB of their maximum only at +165 to +350 ms, maximum at 70 % of the note. They are long notes under the theme and this reads as a swell, not as a late entry; if critic A wants them flat, start them on Sus MAX (coordinator item 3).

## EW-TEMPLATE-PLAN sections this lens touches that are not applied

- Section 5, legato overlap 45-80 ms strings / 33-58 ms winds and brass: `LEG_OVERLAP` is still 0.04 qn (19 ms at 126). Not tested this cycle by me.
- Section 6, keyswitches 40-800 ms before the note: ours 9.5-23 ms (finding 5; no fault measured).
- Section 7, one fixed early shift per track: ours are class leads plus per-note rows; finding 3 shows two per-note rows that chased an unmeasurable reading.
- Section 8, repeated-note gap 60-100 ms: applied (`REP_MIN_GAP`), but together with long leads it cut four notes to 78-81 ms (finding 3).
- Sections 5-8 of EW-TEMPLATE-FINDINGS on volume automation (none in the templates): finding 2 lists what still moves inside notes.

**Do not touch:** the tempo map, `RAMP_SPANS`, `CAESURA` 636, `BEAT_STRETCH` 679, the 30 bpm last bar, `_C54_FLAT`; Violins I's theme row (Sus MAX) and its class leads in `steady_leads57.json`; every `steady57_at.json` row not named in finding 3; the Marc LITE spans of Violins II 104-127 / 552-576 and Violas 104-127; legato-target envelope edges (class B: they sit on the audible join); keyswitch placement before legato targets; the tail hold in rests (`TAIL_HOLD_*`) apart from where `ONSET_KEY` shortens it; the fermata at 679 and the delivery tail trim.
