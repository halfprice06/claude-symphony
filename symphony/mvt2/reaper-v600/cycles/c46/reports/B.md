# Cycle 46, critic B: balance and levels (on the c45 render)

## Method

I measured the 32 dry stems and the master of `cycles/c45/render/`, with c43 and c44 for comparison and the Dvořák 9/i reference for the loud tutti spectrum. Frames are 8192 points with a 43 ms hop. Levels are K-weighted (BS.1770) or A-weighted, as stated. Band shares use 1/6-octave bands of the mid signal. Positions come from the c45 `rendered_build/parts.json` tempo map. EQ changes are simulated in the power domain on the c45 stems, with each changed stem re-levelled to its own K-weighted energy.

Labels:
- **measured**: a number taken from the render or the data.
- **predicted**: arithmetic on measured spectra or levels.
- **inferred**: a judgement about what a listener hears.

I changed no audio settings and touched no REAPER, build or tool file. Scratch files were in `/private/tmp/claude-501/mockup-loop/mvt2-c46-B/` and have been deleted.

## Manual notes (row c46/B: group B1, May 2021 HO manual PDF pp. 137, 140, 150-151, read in full; MANUAL-GAPS.md read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.137: Articulations view. Each row has a load button and a **volume knob** that sets that articulation's loudness inside a KS Master. | Rows whose level differs from the row next to them in the same line: Flute 1 LegRep at 136 (8-11 dB over Leg Slur MAX, MANUAL-GAPS #2), Trombone 1 Sus MAX at 216/218 inside Leg Slur MAX lines, the string tremolo rows at bars 61-64, and the Violas Detache portato. | **Followed by another route.** Row levels are matched in the volume envelope (per-onset shapes; the generic `ROW_TRIM_DB` is empty in movement II), not with the Opus knob. The knob would be a static per-row offset that `opus_state.py` does not write. No change needed. |
| p.140: Master channel. Pan moves the instrument "while preserving the relative panning of the individual microphones"; the gain fader changes output level without changing the mic mix. | Seating (c44 template layout: panned Close mic, full-width Main, small REAPER pan). | **Followed.** Seats come from `pan_by_mic` and the REAPER track pan, and levels from track gain. The Opus gain fader is not used. |
| p.150: Note velocity sensitivity curve. The default is linear (0, on a -100 to +100 range). Velocity picks the sample layer, using example ranges (p 1-25, mp 26-45). | Every velocity table: the legato-target `LEG_VEL_BY_CC`, the timpani strokes, the harp, the pizzicato. | **Followed.** No state writes a sensitivity value, so every patch is linear, and the measured layer edges (timpani v56/64, harp 42/43, 57/58, 70/71; LEARNINGS §9-10) are the ones in force. Keep the curve at 0: every velocity table was fitted on it. |
| p.151: "Prepping MIDI CCs": send CC1 and CC11 before the first note. | Each track's first CC values. | **Followed.** The silent 3 qn pre-roll carries the first CC1, CC11 and keyswitch values and the CC16 reset. |
| p.151: CC7 "is best used to set the overall upper limit on the volume of each track", **not** for shaping a line; CC11 shapes swells and phrases; velocity, CC11 and volume are three ways to make a note louder. | CC7 is used for shaping in five places: Trombone 1's accents (213 and 215 windows at 110 / 120), the timpani roll shapes, the Violins II dip at 264-265.75, the bar 66 niente, and the CC7 term in the re-bow plan. | **Partly.** Most CC7 shaping is deliberate: CC7 acts before the hall, so a fall there keeps the tail ringing (S3). The exception is Trombone 1's 213 window: the CC7 dip to 110 sits exactly on the accent and works against it. Its original purpose (taming brightness) is better served by the brass EQ (findings 2 and 4). |

MANUAL-GAPS #8 (the "4 soli" on half-section patches) and #10 (CC16 round-robin reset) also bear on this lens:
- **#8:** the soli levels are on target (finding 6). Only the timbre is open.
- **#10:** c46 changes the tempo map, which moves every MIDI event. So c46 cannot test whether two renders of unchanged data now match. Run `state_check.py` in the first cycle after c46 that leaves some tracks unchanged.

## The ONE_TIME carry-overs in my area

- **Brass bells (Movement I c51 item c): apply them.** Measured and simulated; see finding 2.
- **Soft timpani roll shelf (item d): not needed.** Measured:
  - The soft rolls take less of the 30-150 Hz band than in c43, not more: ppp roll bars 2-3 11.0% (c43 11.8%); pp crescendo roll into 172 27.7% (28.8%); ppp roll under Horn 1 at bars 67-70 7.3% (8.0%); coda strokes 15.1% (17.4%).
  - The drum's own tone is a little darker (centroid 155 Hz against 169 Hz), but its share of the bass band fell.
  - The only roll above c43 is the pp crescendo roll into the f at 203 (20.4% against 14.5%). That crescendo is printed, which rule 5 allows, and the roll stays 14.7 dB K under the master.
  - Leave the 160 Hz shelf and the +1 dB out.
- **Trombone 1 qn 213:** finding 4.
- **Hairpin curves and the timpani roll lanes:** finding 3.
- **Violas 87 and the Oboe 1 join timing:** these belong to the articulation and tempo lenses. I measured nothing there that changes their advice.

## Findings, ranked by what a listener would hear

### 1. The double basses lost 4-5 dB in the loud tuttis, and the bass trombone and bass clarinet now carry the bottom (measured; fix predicted)

**Where:** Double basses and bass clarinet, bars 61-62 (qn 204-212) and bars 79-81 (qn 262-271). Both passages are printed ff, "molto sostenuto, change bow at will".

**Evidence (measured, K-weighted):**
- The basses' own level, c43 -> c45: bar 61 41.0 -> 35.5 dB; bars 79-80 37.1 -> 32.0. The loss runs from the fundamental (60-80 Hz band -4.2 dB at bar 61) through 160-500 Hz (-6 to -8 dB). It is a level loss from the c44 template mix (basses `gain_db` -5.62, Duc's 228 Hz cut, HPF 53 Hz), not a change of notes.
- Share of the 30-150 Hz band, c43 -> c45:

  | Passage | Basses | Bass trombone | Bass clarinet |
  |---|---|---|---|
  | Bar 61 | 45% -> **18%** | 21% -> **37%** | 12% -> 19% |
  | Bars 79-80 | 63% -> 51% | | 25% -> 37% |
  | Bar 81 | 27% -> 15% | | 48% -> **69%** |

- At bar 61 the bass clarinet alone (41.8 dB) is 6.3 dB louder than the whole bass section (35.5 dB). In c43 the two were level (41.2 / 41.0).
- c45 B #2 contributed: the wind f +1.5 / ff +2 make-up was meant for the melody winds, and it also raised the bass clarinet, which doubles the basses an octave up.
- Basses minus celli: bars 61-62 -5.1 (c43) -> -6.1 dB; bars 79-81 -4.5 -> -6.3.
- Kit LEARNINGS §13-14 and Rimsky-Korsakov (Principles, p.33, "Comparison of resonance") support the basses as the foundation of a string-led ff tutti. A single bass clarinet in its middle register should not cover them.

**Fix (`build/mix.json`):**
- `tracks["Double basses"].dyn_trim_db`: **{f 0 -> 2.5, ff 1 -> 4.0}**. Leave the soft trims, the `loud_eq` rows and the pp/p release cap.
- `tracks["Bass clarinet"].dyn_trim_db`: **{f 0.0 -> -1.0, ff -1.0 -> -3.0}**. ff goes back to c44's value; f goes half way. The other ten winds keep c45's make-up.

**Predicted:**
- Basses minus celli: bars 61-62 about -3.1, bars 79-81 about -3.5.
- Basses' share of 30-150 Hz: bar 61 about 37%, bars 79-81 about 45-50%.
- Bass clarinet 2 dB under its c45 level in bars 53-64 and 75-82.
- Master at bar 61 +0.3 dB or less: check the limiter and the climax order.

**Inferred:** the climaxes get a bowed bass under them instead of a low reed and a bass trombone.

### 2. The brass family EQ made the loud brass thin and bright. Halve the template bells, add the 3.2 kHz bell, and re-level (measured; simulated)

**Where:** the four horns, Horns 1-2 a2, Trombones 1-2, bass trombone, tuba. Most audible at bars 63-64 (Trombone 1's quotation), then bars 61-62 and 79-81.

**Evidence (measured, master):**

| | Loudest 10% of frames, centroid | 500 Hz-1 kHz | 2-4 kHz | 4-8 kHz | Bars 63-64 centroid |
|---|---|---|---|---|---|
| c45 | 933 Hz | -7.1 | -9.6 | -20.0 | **1337 Hz** |
| c43 | 889 Hz | -5.9 | -10.8 | -21.4 | 1100 Hz |
| Dvořák | 850 Hz | -5.9 | -11.0 | -22.2 | |

- Brass 2-5 kHz minus 0.5-2 kHz (the bite against the body), c43 -> c45:
  - horns at bars 61-62: -12.7 -> -4.4 dB;
  - low brass at bars 63-64: -10.3 -> -4.8 dB.
  This is the template's -5.4 dB bell at 475 Hz and -7.8 dB bell at 821 Hz, followed by make-up gain. It is the same overshoot Movement I c51 C and the finale's c08 measured. Three movements now agree.
- The soft horn solos are affected in the other direction. In bars 7-14 and 67-70 the horn centroid fell 458 -> 354 Hz and 402 -> 322 Hz. Their 400-900 Hz share fell 4-6 dB while 250-500 Hz stayed. That is the "heavy at 250-500 Hz" sound critic C measured in c45. Halving the bells gives the horns back some 500-1000 Hz, so it eases that problem rather than adding to it.

**Fix (`build/mix.json`, `groups.horn.family_eq` and `groups.lowbrass.family_eq`, both alike):**
- bell 475 Hz -5.4 -> **-2.7 dB** (bw 1.92);
- bell 821 Hz -7.8 -> **-3.9 dB** (bw 1.92);
- add `{"type": "bell", "hz": 3200.0, "db": -3.0, "bw": 1.0}`;
- keep the 41 Hz HPF and the +2 dB 7.49 kHz shelf.

`gain_db` deltas hold each stem's K-weighted energy, so all balance tables stay put:

| Track | Delta (dB) | New `gain_db` |
|---|---|---|
| Horn 1 | **-3.4** | 0.1 |
| Horn 2 | **-2.8** | -0.9 |
| Horn 3 | **-3.9** | 0.7 |
| Horn 4 | **-3.9** | 0.6 |
| Horns 1-2 a2 | **-3.5** | 4.5 |
| Trombone 1 | **-2.0** | 4.18 |
| Trombone 2 | **-3.2** | 5.0 |
| Bass trombone | **-2.7** | 5.5 |
| Tuba | **-2.35** | 7.95 |

**Simulated:**
- Loudest 10%: centroid 933 -> 904 Hz; 500 Hz-1 kHz -7.1 -> -6.5; 2-4 kHz -9.6 -> -10.1; 4-8 kHz -20.0 -> -20.6.
- Bars 63-64 centroid 1337 -> 1172 Hz (c43 1100).
- Bars 61-62 centroid 926 -> 892.
- Brass 2-5 kHz minus 0.5-2 kHz at bars 61-64: Horn 1 -3.7 -> -9.3, Trombone 1 -4.5 -> -8.9, Trombone 2 -8.9 -> -13.5, bass trombone -8.2 -> -12.9.
- Soft horn solos: centroid 349 -> 371 Hz (bars 7-14) and 362 -> 379 (bars 67-70), with 500 Hz-1 kHz +1.3 to +1.5 dB. The horns' 800 Hz soft shelf stays.

**Check after the render:**
- loud-frame centroid at or under 910 Hz;
- 2-4 kHz share at or under -10 dB;
- bars 63-64 centroid at or under 1200 Hz;
- climax order unchanged;
- the Trombone 1 accent numbers in finding 4.

### 3. Every curved hairpin raises its track by 1-6 dB in the middle of the hairpin. Under Trombone 1's quotation and the bar 47-48 solo handover, that covers the lead (predicted from the parts data)

**Where:** the c46 port of plan section 9:
- crescendos: control point at 34% of the time and 88% of the rise;
- diminuendos: control point at 72% of the time and 0% of the drop.

**Evidence (predicted):** I applied both curves to all 336 hairpins in the c45 parts. I took each hairpin's CC11 (or CC7) end values and converted them to dB with the measured CC11 response (0.57 / 0.35 / 0.25 / 0.12 dB per CC over 0-30 / 30-60 / 60-88 / 88-128). Both shapes only add level against the linear ramp:
- a crescendo gets loud early;
- a diminuendo stays loud late.

Where it matters for balance:
- **Bars 63-64, strings' ff -> p diminuendo, qn 212-216**, on Violins I and II, violas, celli and every div track (CC 122 -> 47), plus the bass trombone's 212-216. These tracks hold **+3.1 dB on average and up to +5.9 dB** longer, right under Trombone 1's accented quotation. Today Trombone 1 leads its accompaniment by +4.5 / +6.2 / +4.3 / +6.9 / +7.9 dB K at qn 213 / 213.5 / 214 / 214.5 / 215. With the curve that margin falls to about +1.5 to +4. The 213 accent would then be no louder than the strings' tremolo.
- **Bar 47-48, qn 146-152.5**: the decrescendo after the fp on Violins II (CC 84 -> 34), violas and Violas div (to 152.5), basses and Violins II div (88 -> 34), celli and celli div. Mean +3.0 to +3.6 dB, up to +5.7. It lands on Oboe 1's tail (149-151) and the cor anglais's entry at 151. That entry already loses to the accompaniment at 152-154: margin -0.6 / -1.6 / -3.4 dB K (finding 5c).
- **Under solos, small (+0.7 to +2.1 dB mean):**
  - Violins II and Violins II div pairs under Oboe 1 at 42-47 and 54-57;
  - Violins I under the solo violin at 48-53;
  - the bass clarinet decrescendo under Flute 1 at 108-110;
  - Horns 1-2 a2 lanes at 229-235 (silent there, no effect).
- **Timpani:** curved, the crescendo rolls at 168, 200 and 261 would gain +2.0 to +3.0 dB on average, up to +4.7. ONE_TIME already says to keep the timpani lanes linear; these numbers support it.
- **Tutti diminuendos** at 268-271 (bar 81) and 295-297 (morendo): +2.4 to +3.6 dB mean, all tracks alike. There is no balance problem, but the post-climax decay becomes 1-3 dB louder, so the delivered span and the S3 tails need a check.

**Fix (`build/score_config.py`, in the c46 hairpin-curve rule):**
- Curve the CC11 lane only. Keep the `vol_db` hairpin ramps (`hpgain`, the HP dB swells) linear, or each curve counts twice.
- Linear (skip list) for:
  - `Timpani` (all);
  - the qn 212-216 diminuendo on Violins I, Violins II, Violas, Violoncellos, Double basses, Violin I solo, Violoncellos div, Violins II div, Violas div and Bass trombone;
  - the qn 146-152.5 hairpins on Violins II, Violins II div, Violas, Violas div, Violoncellos, Violoncellos div and Double basses.
- A generic rule that does the same: no curve on a track that is not the lead inside a lead window. Windows: Trombone 1 212.4-220, Oboe 1 139-151, cor anglais 151-168, plus the solo windows in BRIEF.

**Check after the render:**
- Trombone 1 over its accompaniment at 213-215.5 at least +4 dB K (it is +4.3 to +7.9 now);
- the cor anglais at 151-154 not lower than in c45.

### 4. Trombone 1's 213 accent: start the role at the accent, and lift the CC7 dip that cancels it (measured; fix predicted)

**Where:** Trombone 1, qn 212.5-215 (bars 63-64, ff marcato quotation).

**Evidence (measured, peak of the 50 ms energy in the first 0.35 s of each note, stem dBFS):**

| | 212.5 | 213 | 214.5 | 215 | 218 |
|---|---|---|---|---|---|
| c43 | -26.7 | -18.5 | -24.6 | -22.0 | -23.0 |
| c45 | -30.0 | -26.2 | -28.6 | -29.8 | -25.1 |

- In c45, 213 is only +3.8 over the pickup and +2.4 over 214.5, and it is **1.1 dB quieter than 218**.
- Three things hold it down:
  1. The role row [212.4, 213.6, +3] starts on the pickup and lifts it by as much as the accent. In the volume envelope the pickup is +5.0 dB at 212.4, against +5.7 to +9.0 at 213.
  2. `CC7_POINTS["Trombone 1"]` drops to 110 (about -1.2 dB) from 212.9 to 213.35, exactly on the accent. This is a c33 leftover from when the accent was too bright. Manual p.151 reserves CC7 for the track's upper limit.
  3. The brass bells removed the note's 475-821 Hz weight (finding 2).
- There is a lot of room on the bite: 2-5 kHz attack minus body -10.1 dB, master 2-5 kHz jump -6.5 dB (rule 9 limit +2).

**How roles ramp:** `score_to_parts.py` (role code near line 3860) ramps a role over [a, a+0.25] when a falls within 0.02 qn of a legato-target onset, and over [a-0.5, a] otherwise. The 213 note is a legato target with its note-on at qn 212.91 (parts.json). So a row that starts at 213.0 would still ramp over the pickup from 212.5. It has to start at 212.91.

**Fix:**
- `build/roles.json` Trombone 1: replace [212.4, 213.6, 3] with **[212.4, 212.9, 1.5] and [212.91, 213.6, 3.5]**. The two rows meet, so the pickup's +1.5 crossfades to +3.5 over 212.81-213.06, and the accent is at full lift from 213.06. The 214.1 ramp-out is unchanged.
- `build/score_config.py`: in the c38 `CC7_POINTS["Trombone 1"]` remap, set the 213 window (212.9, 213.35) to **127** instead of 110. Keep 215's 120.
  - This is pre-hall, so the tail keeps ringing (S3).
  - Do this together with finding 2's 3.2 kHz bell, which takes about 4 dB off this note's 2-5 kHz share (simulated -4.5 -> -8.9 dB, 2-5 kHz minus 0.5-2 kHz over bars 61-64).
- Include Trombone 1 in `--midi-only` (ONE_TIME).

**Predicted:**
- pickup -31.5;
- 213 about -24.5: +7 over the pickup (c43 +8.2), +4 over 214.5, +0.6 over 218;
- 2-5 kHz attack minus body about -12 dB; master jump well under +2.

If critic A finds +7 over the pickup too heavy, use [212.91, 213.6, 2.5] instead (predicted +6 / +3 / -0.4).

### 5. Four wind solos lose to one accompanying line in places (measured; fixes predicted)

Margins are the lead minus one accompanying stem, per quarter note.

**(a) Horn 1, bars 69-70 (qn 232-236).**
- Horn 1 holds B flat 3 under a printed decrescendo from mp, reaching pp at 235. Bassoon 1 holds G3 just under it at pp.
- Horn minus Bassoon 1 (A): +2.8 / +2.3 / +1.2 / +0.5 / +0.9 dB at qn 232-236. c44 was about 0.5 dB better.
- Bassoon 1's phrase (228.86-240) got c45's lyrical arch, peaking at 0.44 of the phrase (about qn 233.8). Its legato targets at 231 and 232 went from v60 to v88 (`LEG_VEL_BY_CC`). Its volume envelope reads +3.6 to +4.8 dB at 232.5-234 even with the -2 role.
- **Fix:** `build/roles.json` Bassoon 1 [231.5, 237, -2, 0.5] -> **[231.5, 237, -4.5, 1.5]**. The cut holds to 235.5, then opens linearly to 237 inside Bassoon 1's printed crescendo.
- **Predicted:** horn over Bassoon 1 +5.3 / +4.8 / +3.7 / +3.0 / about +2.5 at 232-236.

**(b) Bass clarinet solo, bars 31-34 (qn 93-101).**
- The cor anglais's p "dolce" holds C5 against the bass clarinet's crescendo to mf (93-96), then its A flat 4 against the bass clarinet's mp line (99-101).
- Bass clarinet minus cor anglais (K): +3.9 / +3.2 at 93 / 94, and +4.6 / +3.1 at 99 / 100. A-weighted: +3.6 / +2.5 and +2.6 / +0.9.
- c45's -5.5 role at 98.5-102 moved the cor anglais only about 2 dB. Its volume envelope there is already -4 dB, so the level comes from the v90 legato targets.
- **Fix:** `build/roles.json` cor anglais [93, 96.0, 2, 0.5] -> **delete** (or 0), and [98.5, 102, -5.5] -> **[98.5, 102, -7.5]**.
- **Predicted:** bass clarinet over the cor anglais about +5 to +6.6 dB K at 93-94 and 99-100.

**(c) Cor anglais, bars 48-51 (qn 151-164, "solo, espr.", p).**
- The pp celli sit 1-3 dB under it: margin over the whole accompaniment -0.6 / -1.6 / -3.4 dB K at 152-154 and -0.3 / -1.8 at 160-161. The celli (C sharp 3, then the moving pp bass line) are the strongest accompanying stem: 20.5 to 23.7 dB K against the cor anglais's 22 to 25.
- The held A4 still sags about 2 dB at 154 (22.2 against 24.0 / 24.8 on either side).
- **Fix:**
  - `build/roles.json` Violoncellos: add **[152.0, 164.0, -3.0, 0.5]**;
  - `build/note_trims.json` cor anglais "152": **-3 -> -1**.
- **Predicted:** margin about +1 to +2 dB at 152-154 and +0 to +1.5 at 160-161.
- Finding 3's skip list stops the curved 146-152.5 diminuendo from undoing this.

**(d) Clarinet 1, coda bars 87-89 (qn 286-292).**
- Both Clarinet 1 and the cor anglais are printed pp. The cor anglais is the "dolce" inner voice; Clarinet 1 has the motto tail.
- Clarinet 1 minus cor anglais (A): +1.8 / +1.1 / +3.8 at 289.5 / 290 / 290.5. Clarinet 1's median margin over everything is +3.9 dB, with 39% of frames under +3.
- The cor anglais carries a role [285.9, 292.5, +2, 0.5], and its lyrical arch peaks at about 289.5.
- **Fix:** `build/roles.json` cor anglais [285.9, 292.5, 2, 0.5] -> **delete**.
- **Predicted:** Clarinet 1 over the cor anglais +3.8 / +3.1 / +5.8 at those points; median margin over everything about +4.6.

### 6. Soft strings: the basses' pp pedal equals the celli under the oboe solo, and the divided violas' upper half is 2.5-6 dB over its lower half (measured)

**(a) Basses, bars 45-46 (qn 140-146, pp arco B flat 1 under Oboe 1's "dolce espr." p and the celli's co-melody).**
- Basses minus celli: -0.5 dB K over bars 45-47. In bars 23-30 at the same pp it is -6.4. Oboe 1 is only +2.5 to +6.6 dB K over the basses at qn 140-143, and its margin over the accompaniment is -0.6 at 141 and -1.1 at 145.
- Part of this comes from c45 B #3's +2 dB on the basses' pp trim, which was meant for the pedals at bars 23-30, 65-70 and the coda.
- **Fix:** `build/roles.json` Double basses: add **[139.9, 146.0, -3]**. It meets the existing [146, 151, -3], so the cut runs continuously to 151.
- **Predicted:** basses minus celli about -3.5; Oboe 1 over the basses +5.5 to +9.6 dB K.

**(b) Violas div (DIV B half section, the upper voice by `TRACK_SPLITS` "rank") against Violas (the full patch playing the lower half).**
- Violas div minus Violas (K, while both sound): +2.5 at bars 23-26 (qn 66-80); **+6.0 at bars 27-29 (80-87)**; +4.3 at 279-292; +4.4 at 292-304.
- In the coda the lower voice carries the chromatic descent (F, E, E flat under the held A flat 3). At +4 dB under the upper voice it disappears (inferred).
- The other divisi pairs are in range (half section against full patch): Violins II div minus Violins II -1.3 dB at bars 37-40; celli 4 soli (div) level with the basses at 274-286; basses' 4 soli 2.9-4.3 dB under the celli.
- **Fix:** `build/mix.json` `tracks["Violas div"].gain_db` 5.48 -> **2.98**.
- **Predicted:** +0.0 (66-80), +3.5 (80-87), +1.8 (coda).
- Then check the final chord: if the A flat 3 falls under the chord's balance target, raise Violas div's [297.9, 304, 2.5, 1] row to 5.

## Also measured, no change

- **Solo margins** (A, lead over all other dry stems, median / p10): Horn 1 bars 7-14 +5.2 / +1.6; Oboe 1 bars 15-16 +6.5 / +2.6 and 19-20 +7.8 / +0.8; solo violin bars 17-18 +9.0 / +4.1 and 21-22 +7.6 / +2.4; Flute 1 bars 37-40 +6.2 / +1.4; cor anglais bars 41-44 +9.6 / +3.2; Oboe 1 bars 45-47 +5.3 / -0.4 (finding 6a). In range, except where findings 5-6 apply.
- **Dynamic mapping at pp** (K, notes only):
  - strings: Violins I 14.4, Violas 14.4, basses 15.0, Violins II 17.0, celli 18.5;
  - accompanying winds: 14.3-18.4;
  - Horns 3-4: 15.1-15.2;
  - timpani: 14.4.
  pp means about the same in every family, within about 4 dB. The celli sit at the top of that range, but they carry counter-melodies at pp.
- **Climax families against the strings** (K): winds -1.8 / -1.3 at bars 61 / 62 and +1.0 to +1.5 at bars 79-81; horns -4.1 to -5.4; low brass -3.2 / -4.4 at bars 61 / 62. Timpani -14.7 to -21.4 dB, 6-8% of 30-150 Hz. Neither the timpani nor the low brass covers anything at bars 61-64 or 79-82 apart from the bass-band shift in finding 1.

**Do not touch:**
- the c44/c45 return levels, hp 160 and the IR envelope;
- the c45 string brightness set (string shelf 0, 1 kHz -2.5, Violins I -6 / Violins II -4 at 5 kHz);
- the horns' 800 Hz soft shelf (finding 2 needs it);
- Horn 1's roles at 16.5-42 and 226-238;
- the -1.5 dB on the bassoons and bass clarinet in bars 7-14;
- the timpani CC7 roll shapes, TIMP_CC1_MAP, the +3 role at 204.25-209.5, and linear timpani lanes;
- the basses' soft trims {ppp 6, pp 8, p 8.5} outside 140-151, their `loud_eq` rows and the 400 ms pp/p cap;
- the c45 wind f/ff make-up on the ten melody winds;
- the celli coda role [291.9, 300.9, -2.5];
- Clarinet 1's coda roles and the harp's c45 stem-fix level;
- the velocity sensitivity at 0 (manual p.150).
