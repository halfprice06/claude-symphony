# Cycle 41, critic A: articulation and phrasing (on the c40 render)

## Inputs and methods

- **Render and data.** `cycles/c40/render/` (master and 32 stems), compared with `cycles/c39/render/`. Data: `cycles/c40/rendered_build/` (parts.json, mix.json, score_config.py) and the c39 equivalents. Also read: `cycles/c40/CHANGES.md`, `cycles/c40/reports/A.md`, `build/mockup-events.tsv`, and `tools/build_reaper.py` (`cap_release`). In `tools/score_to_parts.py` I read the re-bow split (`REBOW_GAP_QN`, about lines 4940-5010).
- **Release times shipped in the patches.** Read from the .oib files: each used row and dynamic group's AHDSR release, by a dry read with opus_state. Nothing was written.
- **Manual.** May 2021 HO manual PDF pp.160-162 and 188-190 (row A7, cycle 41), read in full. Also `loop/MANUAL-GAPS.md`.
- **References.** The stored rtk tails in `symphony/render/critics/c00|c04/ref_*/metrics.json`.
- **Measurement conventions.**
  - Levels are stereo-power RMS on the stems, 20 ms windows every 5 ms (30 ms for the re-bows), in dB.
  - Positions are score qn. Times are on each cycle's own tempo map (the c39 and c40 maps are identical).
  - **t10:** the time from MIDI note-off until the stem first falls 10 dB under its mean over the 0.15 s before the note-off.
  - **Phrase end:** a note-off followed by at least 0.6 s with no note on that track.

## Manual notes (A7, PDF pp.160-162, 188-190: articulation window, trigger options, zones)

| Manual says (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| Each articulation cell has a load switch that loads the row into RAM or unloads it (p.160). | Every KS Master track. `build_reaper.py` loads the rows a track uses and unloads the rest (`UNLOAD_UNUSED_ROWS`). | Yes (read). The c40 memory was 44-45 GB with all 32 tracks rebuilt. |
| Keyswitch trigger notes lie outside the playable range (C-2 to G8), and a keyswitch selects the articulation used from then on (p.161). | All keyswitch lanes in parts.json. | Yes (measured in parts.json). No note's keyswitch arrives later than its note-on, and none lands less than 5 ms before it. There are 1-53 keyswitches per string track that fall while an earlier legato note still sounds (for example Violins II 46.762 and 47.796). These are the deliberate switches before the next legato target. The manual pages do not say what a mid-note switch does to the sounding note; the joins measured below show no hole caused by one. |
| Keyswitch Range with pass-thru, Program Change, and Controller triggers by CC value range (pp.161-162, 189-190). | Not used. The pipeline drives everything by keyswitch. | Not applicable. CC1 and CC11 already carry layers inside the rows, so a CC-range trigger would collide with them. |
| Velocity trigger: layer a short articulation on a sustain at v110-127 to get an accent (pp.162, 189-190). | The only printed brass accents are Trombone 1's at 213 and 218. | Correctly not used: Dan wants weight, not bite (BRIEF item 9). Measured on c40: 2-5 kHz energy over the first 80 ms is 11.2 dB (213) and 17.3 dB (218) under the note body, and the level is +2.5 / +3.4 dB over the pickup. Unchanged from c39. |
| Group: instruments switched in tandem; only the triggered one in a group plays (p.188). | Not used. One instrument per Opus instance. | Not applicable. |
| Voice limit per instrument; raise it if voices drop (p.188). | Divisi chords on the KS Masters, the final chord, overlapping re-bow pieces. | Read: the Violas KS Master ships `voiceLimit` 350 with a 10 ms steal fade. The largest chord here (3 notes × 2 mics × release voices) is far under that. No dropped voices are expected (inferred). |
| Octave and Key Range split instruments on one channel (pp.188-189). | Not used. Divisi go to separate tracks (Violas div, Violins II div, Violoncellos div, Violin I solo). | Not applicable. The one key-range issue is the bass trombone's D2 at 218, under the 1TB roots E2-C5 (MANUAL-GAPS #12, open). |

## Findings, ranked by what a listener would hear

### 1. The 150 ms release cap makes soft string endings stop 2-3 times faster than c39 and the references. The final chord loses its last 0.2 s, soft re-bows dip deeper, and soft legato joins dip more. Lengthen the cap at pp/p (measured; fix value inferred)

**Shipped releases (read in the patches).** `cap_release` caps groups by sample-layer name, not by printed dynamic. In c40 the same 150 ms applies to the pp, p, mf, f and ff groups of Sus MAX, Leg Slur MAX, Leg BC MAX, Leg Port MAX and Flautando on all nine string tracks. What the patches ship:

| Patch | Groups | Shipped release |
|---|---|---|
| Violins II, Violas, Violoncellos, Double basses | pp | 931 ms on Sus MAX and Leg BC MAX |
| Violins I | Sus MAX pp | 931 ms |
| Violins I | Leg Slur MAX pp | 562 ms |
| All of the above | p | 524-700 ms |
| Flautando | pp | 645 ms |
| Horns | pp | 562 ms (capped to 237 in c40) |

**Phrase ends at pp/p** (38 string phrase ends with CC11 ≤ 52, same MIDI in both cycles).

| | c39 | c40 |
|---|---|---|
| t10 median | 0.20 s | 0.12 s |
| Ends with t10 of 0.20 s or more | 50% | 16% |
| Median drop in the first 0.05 s | 2.3 dB | 4.4 dB |

Ends that got more than 0.08 s faster:

| Track | Onset (qn) | t10 c39 → c40 (s) |
|---|---|---|
| Double basses | 72 | 0.45 → 0.09 |
| Double basses | 87 | 0.60 → 0.11 |
| Violins II | 56 | 0.29 → 0.09 |
| Violins II | 87 | 0.27 → 0.07 |
| Violins II | 122 | 0.26 → 0.09 |
| Violins II | 271 | 0.34 → 0.07 |
| Violas | 5.7 | 0.39 → 0.12 |
| Violas | 169.5 | 0.29 → 0.10 |
| Violas div | 72 | 0.36 → 0.12 |
| Violins I | 7.35 | 0.34 → 0.05 |
| Violoncellos div | 284.14 | 0.28 → 0.09 |

Three ends fall more than 10 dB in their first 0.05 s, which is the brief's limit:
- Violins I 7.35, the end of the opening C5: 11.0 dB.
- Violoncellos 87 (bar 30, end of section A): 12.1 dB.
- Violins I's final-chord C5: 10.1 dB.

**Final chord, ppp, ending at qn 304.**

| Signal | t10 c39 → c40 | t20 c39 → c40 | Drop at +0.2 s c39 → c40 |
|---|---|---|---|
| Master | 0.31 → 0.11 s | 0.62 → 0.23 s | 7.1 → 17.8 dB |
| String stems | 0.23-0.35 → 0.05-0.10 s | | |

**References** (rtk final tails; inferred comparison, since rtk measures from the last frame within 12 dB of the final maximum rather than from a note-off):

| Recording | t10 | t20 |
|---|---|---|
| Brahms 1/ii | 0.40 s | 0.79 s |
| Brahms 4/ii | 0.20 s | 0.48 s |
| Brahms 4/i | 0.24 s | 0.46 s |
| Dvořák 9/i | 0.31 s | 0.61 s |

- c39 sat inside the range of soft endings. c40's final chord is 2-4 times faster at both -10 and -20 dB, the same result Movement I measured (0.40 → 0.07 s).
- In the master, most mid-movement soft ends are covered by the next entry: drops of 0.5-5 dB at +0.3 s, nearly unchanged from c39. So the audible cases are the final chord and section ends where little else sounds: bar 30 into the bass clarinet solo, where the master drop at +0.3 s went from 4.4 to 5.2 dB.

**Same cause at soft re-bows (measured).** A re-bow ends the old piece 0.03 qn before the new Sus MAX note (`REBOW_GAP_QN`). With the shipped 524-931 ms releases, the old voice bridged the slow soft attack of the new one. With 150 ms it does not.

| Re-bows | Stem dip median c39 → c40 | Other numbers |
|---|---|---|
| All 86 | 4.2 → 6.0 dB | p90 6.0 → 10.2 dB |
| Final chord, 292-304 (29 points) | 3.9 → 7.0 dB | Celli 296.3-302.4: 8.4-11.0 dB, against 1.3-2.6 in c39. Basses 297-303: 6.8-10.2 dB. |
| Coda basses 273.2 / 282.2 / 283.6 | 12.3 / 11.3 / 12.7 dB | |

- The master dips much less, because the sections are staggered. Final-chord master dip median 2.2 → 2.7 dB. The master's 50 ms level wobble around its 1 s mean over 292-301 went from 1.19 to 1.32 dB standard deviation. Inferred: a slightly more restless chord, not a new pulse.
- Bar 66 and the basses' 4 soli pedal: the master dip at Cb 225.2 went from 5.2 to 7.3 dB.

**Same cause at soft legato joins (measured).** Dip = median over -0.3..-0.08 s minus the minimum over -0.05..+0.2 s at each legato target.

| Track | Joins dipping 6 dB or more, c39 → c40 | Median change |
|---|---|---|
| Violins II | 7 → 20 | 3.0 → 3.5 dB |
| Violins I | 9 → 13 | |
| Violoncellos | 20 → 23 | |
| Violas div | 1 → 4 | |

- Medians changed by 0-0.5 dB.
- Joins that got at least 3 dB deeper, almost all at pp-mp: Violins II 47, 53, 71, 154, 156, 168, 172; Violoncellos 68, 140, 240; Violas div 71, 283.
- Legato lines are still connected (no hole at any join), but the soft ones now dip.

**Fix.**
- `tools/build_reaper.py` `state_for`: accept a list of specs. Replace `cap_release(inst, m_["sus_release_cap_ms"], tr["name"])` with a loop over `spec if isinstance(spec, list) else [spec]`. `cap_release` only lowers releases, so the order of specs does not matter.
- `build/mix.json`, the nine string tracks' `sus_release_cap_ms`, same rows as now:
  `[{"ms": 150, "dyn": ["mf", "f", "ff"], "rows": [...]}, {"ms": 350, "dyn": ["pp", "p"], "rows": [...]}]`
- Horns 1-4 and Horns 1-2 a2: the pp groups (562 ms shipped) from 237 to 350 ms.
- Horn soft phrase ends also got faster (t10 median 0.21 → 0.15 s). Horn 1 232, the exposed end of the bar 69 solo: 0.17 → 0.13 s.

**Targets.**
- Final-chord master t10 0.20-0.40 s and t20 0.45-0.8 s.
- pp/p string phrase ends t10 median at least 0.18 s, with none over 10 dB in the first 0.05 s.
- Soft re-bow stem dips at a median of 5 dB or less. Final-chord celli and basses at 6 dB or less.
- Violins II joins of 6 dB or more back to 10 or fewer.

**If 350 ms leaves the final chord under 0.20 s:** go to the shipped value at pp (no cap on the pp groups). c39 showed the shipped values give 0.31 s.

**What to watch.** The basses' pp sus-gap repeats at 156 and 168 currently separate by 9-11 dB in the stem, because the cap empties their 0.06 s gap. Re-measure them after the change. If either dip falls under 4 dB, add a CC11 fall of about 12 CC over the last 0.06 s before the gap, returning at the new onset. CC11 is the instrument's volume and acts on the releasing voice, before the hall (inferred). Do not use CC7 or the volume envelope: c39 measured no effect from a CC7 fall.

**Check before keeping it (inferred until rendered).** Movement I is testing the same 350 / 150 split. Compare its result before the c41 render if it is available.

### 2. Trombone 1, bar 63: the slur from 214.5 to 215 in the ff marcato quotation dips 8 dB in the stem and 6 dB in the master for about 0.15 s (measured)

**Evidence (c40, 20 ms windows, around 215 at t = 237.517 s).**
- Stem: -21.0 dB at -0.25 s, falling from -0.20 s to -29.3 dB at -0.04 s, back to -24.1 at 0.00 s and -22.5 at +0.10 s.
- Master: -20.5, falling to -26.6 at -0.04 s, back to -22.9 at +0.02 s. Trombone 1 is the loudest part of the master here, so its dip is the master's dip.
- In 0.125 qn windows this is the 4.3 dB step the c40 actor left open.
- MIDI (read): 214.5 v106, ending 214.95; 215 v112, starting 214.91 on Leg Slur (0.04 qn overlap). The score slurs 214.5-216.
- The volume envelope makes the notch worse (read in parts.json `vol_db`). The 214.5 shape holds +2.5 dB to 0.40 s and falls to 0 at 0.50 s. The 215 shape starts from 0 dB at -0.02 s and reaches +2.5 dB at +0.03 s. Together they make a V of 2.5 dB exactly at the transition. The CC7 floor 127 → 120 at 214.86-214.9 adds about 1 dB more.

**Simulation on the stems (master = master - stem + stem × gain).**
- A flat +2.5 dB over -0.14..-0.02 s, which removes the V, lifts the master minimum from -26.6 to -25.1 dB.
- +4 dB lifts it to -24.1 dB.
- The rest is the legato transition sample itself: a 30-40 ms notch.

**Fix (`build/score_config.py`, the c40 "A #4" block, about line 928).**
- 214.5 shape: `[(-0.01, 0.0), (0.04, 2.5), (0.60, 2.5)]` (no fall to 0).
- 215 shape: `[(-0.02, 2.5), (0.03, 2.5), (0.50, 2.5), (0.60, 0.0)]`.
  Together these hold +2.5 dB continuously from 214.54 through the end of 215. This is post-hall volume, so `stem_fix.py` can apply it and verify it exactly.
- Raise the legato velocity of 215 (`VEL_SET["Trombone 1"][215.0]`, now 112) to 124. Brass legato velocity sets the transition speed (manual p.104-105, row A5). The faster transition should shorten the notch (inferred). Test on the render.

**Target.** Master minimum at the 214.9 transition no more than 3 dB under the mean of the 0.2 s before it. Trombone 1 2-5 kHz energy over the first 80 ms of 215 not above its body (c40: -4.1 dB, so keep it under 0).

### 3. Some of the new fresh strokes and printed re-bows sound like holes, and two like bumps (measured; causes read; fix values inferred)

**Measures.** Stem dip = median over -0.45..-0.15 s minus the minimum over -0.15..+0.15 s. "Below" = the time spent in ±0.25 s under the pre-level minus 6 or minus 10 dB. Peak = maximum over 0..0.35 s minus the body at +0.4..+0.9 s.

**Most of the c40 strokes work as bow changes.** These dip 5-9 dB in the stem with no time below -10 dB, and 1.4-5 dB in the master: Violins II 45, 51, 144, 289, 292; Violas 50, 62, 253; Violoncellos 66; Violas div 70, 82, 289; basses 156, 253, 265. Keep these.

**Holes:**

| Repeat | Printed | Stem dip | Time below -6 / -10 dB | Master dip | Notes |
|---|---|---|---|---|---|
| Violins II 44 (A flat 4) | portato quarter inside the slur 42-44, pp cresc. into 45 | 17.6 dB, falling to -59 dB | 0.37 / 0.23 s | 4.2 dB | The portato note itself plays 7 dB (44.0-44.5) and 4 dB (44.5-45.0) under c39, where the score asks for the cresc. A louré inside one bow should dip a few dB, not stop. |
| Violoncellos 128 | p slur head after the 4-beat pp upbow 124 | 13.8 dB | 0.32 / 0.175 s | | |
| Violas 69 | unslurred repeat, soft re-bow | 14.2 dB | -10: 0.125 s | | |
| Violas 248.5 | slurred eighth repeat 248-248.5 | 12.4 dB | -10: 0.10 s | | |

Cause for all four (read; measured on the envelopes): a short gap, plus a fresh Sus MAX note whose soft attack reaches body only after 0.15-0.35 s. Before c40, the old note's release (524-931 ms) filled that time. Finding 1 restores most of it at pp/p.

**Bumps:**

| Repeat | Measured |
|---|---|
| Double basses 144, the pp `DOWNBOW_STROKE_AT` slur head | Peaks +7.2 dB over its body at +0.08..+0.26 s, then falls 9 dB by +0.6 s. An accent shape on a pp note; c39 fell smoothly. |
| Double basses 168, pp sus gap | +6.2 dB over the body |
| Violas 71 | +5.6 dB |

**Fix (`build/score_config.py`, the c40 STR_REP_NEW_BOW block).**
- (a) After finding 1, re-measure these seven before changing anything else.
- (b) Portato: the gap 0.05 s → 0.03 s, and drop the CC fall from 6/8 to 3/4 CC. Then lift the portato note to the slur's level: the cresc. should carry 44 at least level with 42's end. Use a note trim, `note_trims.json` "Violins II" 44.0: +4 dB, or a CC11 start at the slur's current value rather than the stroke value. Target: 3-6 dB dip, no time below -10 dB, and 44 at or above 43.5's level within 0.3 s. Apply the same rule to Violins II 50 (stem dip 12.2 dB, 45 ms below -10).
- (c) Strokes and soft re-bows at p and below: scale the stroke gap to 0.03 s (`gap` 0.06 s → a per-dynamic value, or `STR_REP_NEW_BOW["gap_by_cc"]` = {46: 0.03}). Target at Violoncellos 128, Violas 69 and Violas 248.5: dip 6-9 dB, under 0.05 s below -10 dB.
- (d) Basses 144: take it out of `DOWNBOW_STROKE_AT`, keeping only the 0.06 qn gap (`rep_sus_gaps` already has it), or give it the soft velocity of its neighbours. 144 is pp under the oboe/celli B flat minor head, so it should not swell. Target: peak no more than 3 dB over the body.

### 4. Violins II sul tasto, bars 37-40: the printed re-bows now make the pp accompaniment uneven by about ±5 dB in the stem (measured; small in the master)

**Score.** Violins II div., sul tasto, pp: lower voice C sharp 4 at 108/112, F sharp 4 114, C sharp 4 116, then 118/119/120.

**Per half-qn levels, Violins II stem, 110.0-114.0.**

| Cycle | 110.0 | 110.5 | 111.0 | 111.5 | 112.0 | 112.5 | 113.0 | 113.5 |
|---|---|---|---|---|---|---|---|---|
| c39 | -45.0 | -46.1 | -45.4 | -46.9 | -46.0 | -43.4 | -42.5 | -44.5 |
| c40 | -44.2 | -41.1 | -50.2 | -43.3 | -42.3 | -41.4 | -37.9 | -40.6 |

- c40 has a 9 dB hole at the printed bow 112 (the stem dip by the re-bow measure is 16.9 dB with a -6.0 dB step). That measure's window and the half-qn grid are offset, so the hole sits in the 111.0 column.
- 113.0-113.5 is +4.6 dB over c39.
- The master moves at most 1.2 dB, because Flute 1's theme and the harp cover it.
- `fit_rebows.py` clamped the 112 piece (c40 CHANGES).

**Fix.** Refit only the Violins II 112 piece with the printed-bow rule from c40 critic A #2: `--skip "Violins II:112"`, then a hold-only row `[[-0.04, 0], [0.25, 0], [0.45, H]]`, with H = the previous body minus the new body, measured at +0.5..+1.5 s. Then trim the 113-114 swell. It comes from the lower voice's 112 piece overlapping the 113.543 note on Flautando, a polyphonic row (read). Set `vol_db` -3 dB over 112.8-114.0 via `LEVEL_SHAPES`. Finding 1 will also soften the 112 dip.

**Target.** Stem per half qn within ±2.5 dB of a smooth line through 108-124, and 3-5 dB dips at the printed bows.

### 5. Patch choices still open (inferred; no new measurement)

- **Basses "4 soli", bars 65-70 and 87-92 (MANUAL-GAPS #8).** `Basses Divisi/05 Keyswitch/Basses KS Master DIV A.oib` is installed and still unused. The full section at -3 dB plays a soli passage that the score marks for four players. After finding 1 the pedal's re-bows are the most exposed string sound in bars 65-70 (master dip at 225.2: 7.3 dB). A half section would also halve the ensemble size that the slow attack represents.
  - Cost: one Close-only instance, about 0.7 GiB, against 45 GB settled in c40. That is at the cap, so it needs either a second-pass render (MANUAL-GAPS memory plan) or unloading a row elsewhere.
  - Lower priority than findings 1-3.
- **Horn portato rows for the molto sostenuto tenutos, bars 61-62 (MANUAL-GAPS #9).** Still untried. c40's Horn 2 208 re-tongue had no measured effect under the ff tutti, so the gain is small there. Bars 80-81 (Horns 1-2 tenutos at 267 and 269) are more exposed and are a better first test.
- **Hollywood Solo Violin for bars 17-22:** still not installed (MANUAL-GAPS #3). Violin I solo phrase ends are unchanged by the cap (53: 0.10 → 0.09 s; 63: 0.18 → 0.17 s).

## Checked and fine (measured)

- **No legato chords.** No simultaneous onsets on any Leg row.
- **Keyswitches.** All arrive before their notes (Manual notes).
- **Pizzicato (bars 37-44), viola Detache portato (bars 48-51), harp, timpani, the bars 61-64 tremolos.** Same MIDI as c39 and uncapped rows. Violas per-qn level over 152-168 is within 0.2 dB of c39; Violins I over 204-220 within 0.4 dB.
- **Trombone 1's accents** are weight, not bite (Manual notes).
- **Mutes (CC15)** unchanged from c39.
- **The opening chord's re-bows.** Master dips 2.0-4.0 dB, no change in wobble (std 1.18 dB in both cycles).
- **Basses' 4 soli pedal 226-238.** Master wobble improved (std 1.05 → 0.85 dB).
- **Horn legato joins** unchanged: Horn 1 median 2.9 → 2.8 dB over 42 joins.

## Do not touch

- The 150 ms cap at mf/f/ff on the string rows, and its effect on the loud phrase ends and on the bass repeats at 253 and 265.
- The hall `ir_setup` (endPos 0.7).
- The working c40 strokes and soft re-bows listed in finding 3.
- `BC_NEWP_KEEP` at Violins I 72.
- The Violins II div sul tasto points at 114, 116, 119 and 120.
- Trombone 1's accents (213, 218), velocities 106/112/92 and CC7 floors. Change only the 214.5/215 shapes and the 215 velocity.
- The harp setup, the viola Detache portato and the tremolo rows.
