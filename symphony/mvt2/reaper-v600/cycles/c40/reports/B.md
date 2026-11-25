# Cycle 40, critic B: balance and levels (on the c39 render)

**Method.** I used the stems and master in `cycles/c39/render/` and the note data in `cycles/c39/rendered_build/parts.json`, with every qn converted to seconds on its tempo map. Each stem was analysed with 4096-point Hann frames (1024 hop), both channels' power summed, in 1/3-octave bands. Levels are approximately K-weighted (a 38 Hz high-pass plus a +4 dB shelf above 1.5 kHz). They carry an arbitrary offset, so only differences between them mean anything; A-weighting is given where low and high instruments are compared. The printed dynamic comes from each track's `dyn_curve`. For the reference I used the Dvořák 9/i MP3 (`symphony/render/assets/refs/`), split into all frames, its loudest 10% and its p10-p50 frames. Simulations scale stem band powers and re-sum the master. They ignore the hall, so trust them to about 1 dB. "Measured" means a number from the render or parts.json. "Inferred" means a judgement about what a listener hears.

## Manual notes (B1: May 2021 HO manual pp. 137, 140, 150-151; `loop/MANUAL-GAPS.md` read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.137: in the Articulations view, each KS Master row has a load button and its own volume knob. | Level differences between rows at the same CC11: Flute 1's LegRep RRx4 at 136 (body 8-11 dB over Leg Slur MAX, c37), the GENTLE_ACCENT Sus MAX notes, and the Sus MAX re-bow pieces against Leg Slur MAX. | Partly. Rows are loaded and unloaded by script (`UNLOAD_UNUSED_ROWS`). The row volume knobs stay at the patch default, and the differences are corrected with per-note level shapes. Inferred: c40 rebuilds every track anyway (ONE_TIME), so a static row volume would cost no extra rebuild, if `opus_state.py` can write that field of the row. |
| p.140: the Master Channel's Pan keeps the relative panning of the mics; its Gain changes the output without changing the mic mix. | Seats and track gains. | Followed in effect. Seats are written into the mic pans (c05), REAPER pan is centred, and gains live in REAPER track volume and envelopes. |
| p.150: Note Velocity Sensitivity curve (linear default, range -100 to +100). On instruments with several dynamic layers, velocity ranges choose the samples. | Harp, timpani and the pizzicati of bars 37-44. | Followed (linear default). Measured: harp per-note peaks are pp 22.8 / p 23.1 K. The printed pp-p step disappears because the p harp of bars 37-44 carries a -2.5 to -4 dB accompaniment role under Flute 1 and the cor anglais. This is intended, and not a fault of the curve. Timpani peaks: ppp 17.3, pp 25.4, f 35.8. |
| p.151: send CC1 and CC11 before the first notes. In strings and woodwinds CC11 sets loudness and dynamics and CC1 sets vibrato. In LITE patches CC1 sets dynamics and vibrato. CC7 is "best used to set the overall upper limit" of a track; CC11 shapes the line. | Pre-roll, CC roles, the use of CC7. | Followed: the 3 qn pre-roll carries CC1/CC11, and no LITE row is used (checked `art_counts` on all 32 tracks). CC7 serves a different purpose here: pre-hall local cuts, so that drops keep the hall ring (S3). Track ceilings live in REAPER gain. The fixes below use CC7 the same way. |

MANUAL-GAPS read. Relevant to balance: #4 (Mid mics on the solo winds and horns) and #8 (half-section patches for the 4 soli) are still open. The fixes below need neither.

## Where the balance stands (measured)

- **Solo margins over the summed accompaniment (K, per bar).** Horn 1 bars 7-14 +0.5..+4.6; Oboe 1 15-21 +2.5..+5.6; solo violin 17-21 +3.3..+6.9; bass clarinet 31-36 +1.5..+6.2; Flute 1 37-40 +1.7..+4.0; cor anglais 41-44 +2.5..+4.7 and 48-50 +1.3..+4.5; Oboe 1 45-47 +0.3..+1.6, with no single part closer than 6.7 dB; Clarinet 1 85-86 +3.2/+4.2.
- **Dynamic mapping between families (median K of 0.25 qn frames at a steady printed mark).** The ratio Rimsky-Korsakov gives (*Principles*, PDF p.51: in piano all winds are "of fairly equal balance", and a whole string department equals one wind) holds:
  - p: Flute 1 27.0, Oboe 1 26.1, cor anglais 25.4, bass clarinet 26.0, Horn 1 23.8, Violins I 26.4, Violins II 25.2, celli 24.4.
  - pp: winds and horns 15.3-21.7, upper strings and celli 18.0-19.3.
  - The basses at pp sit 3.3 dB under the celli (14.9 against 18.2).
- **Divisi and soli tracks.** The viola halves are within 2.5 dB of each other on every 2 qn in bars 23-30, 80-81 and the coda. Violins II div and Violins II are within 3 dB in bars 37-40. The Violin I solo at p is 24.8, against the Violins I section at 26.4. The exception is finding 5.
- **Climaxes.** Timpani are never above rank 9 in bars 61-64 or 79-82, and sit 14-24 dB under the master. Violins I is the loudest stem at most half beats from 204 to 212, except as in finding 3. Bars 79-82 have no low brass.
- **Spectrum over the whole movement.** It matches the references in the low mids. 250-500 Hz share: mix -5.6, Dvořák -6.3, Brahms -6.0/-6.3. 315-500 Hz relative to 500-2000 Hz: -2.8 for Dvořák against -2.0 to -5.6 per passage here. A master or bus cut at 200-500 Hz is therefore not justified. The low-mid excess is local (finding 1), and the band below it is light (finding 2).
- **S3 scan.** I scanned for vol_db falls of 4 dB or more within 0.15 qn under a note sounding for 0.4 qn or longer. Every hit is a fill or accent-body shape near an attack, as in c39. No role or trim step was found under a held chord.

## 1. The horn-solo passages are the low-mid centre of the movement, and Horn 1's presence band sits under the bass clarinet's pp bass line (measured; "mushy" inferred)

**Where.** Bars 1-14 (qn 0-42): Horn 3's C-D flat-C, then Horn 1's "dolce espr." theme at p over bassoons a2, bass clarinet and harp, all pp. Also bars 66-70 (qn 226-238), Horn 1 alone at p-mp.

**Evidence (measured).**
- 200-500 Hz relative to 630-1600 Hz in the master:
  - bars 1-6: +8.0; bars 7-14: +11.0; bars 65-70: +12.2; coda: +5.7;
  - every other section: -2.2..+1.7; Dvořák -1.5.
- Horn 1 supplies 70% of the band in bars 7-14 and 86% in 66-69. Horn 3 supplies 24% in bars 1-6.
- Horn 1's own spectrum in bars 7-14: the 315 Hz band (its fundamental) is 13 dB over 630-1600 and 30 dB over 2 kHz. Its 1-5 kHz share is -17.8 dB, inside the -19..-21 dB range that c30 measured for the real soft layers. So the horn's colour is right, and a treble lift on it would be wrong.
- What is wrong is the mix around it. In bars 7-14 the bass clarinet's pp bass line (A flat 2 - B flat 1) supplies 73% of the master's 2-4 kHz and 27% of its 1-2 kHz.
  - Horn 1 against the accompaniment: 2-4 kHz -5.2 dB (bars 7, 11, 12: -7 to -8), 1-2 kHz +0.4, 250-1000 Hz +1.5..+7.
  - In K, Horn 1 is only +0.5 (bar 9), +0.8 (13) and +0.6 (14) over the summed accompaniment.
- The theme is carried by its 250-500 Hz fundamental, while its definition band belongs to the bass line (inferred). The movement opens with this.

**Fix (`build/mix.json`).** This is c39 B #5's bell, which was not applied, here quantified and paired with a cut on the bass clarinet.
- Horn 1 and Horn 3 `loud_eq`: add `{"band": "bell", "hz": 300, "db": -3, "bw_oct": 1.0}` to the existing `bands` list. The 800 Hz -8 shelf and the points stay, so the bell is wet exactly where the soft shelf is.
- Horn 1 `soft_trim_db`: pp 4.0 -> 5.5, p 4.5 -> 6.0, mp 2.8 -> 4.3. The bell alone costs about 1.4 dB K, and these trims restore it.
- Bass clarinet: new `loud_eq` `{"points": [[0, 1], [42, 1], [44, 0], [304, 0]], "bands": [{"band": "highshelf", "hz": 1200, "db": -3}]}`. Its solo (bars 31-36) and its ff passages keep their present EQ.

**Simulated.**
- Bars 7-14: master 200-500 re 630-1600 +11.0 -> +9.6; Horn 1 over the accompaniment at 1-2 kHz +0.4 -> +3.4 and at 2-4 kHz -5.2 -> -0.9; K margin unchanged (+2.3 -> +2.4); master K level unchanged.
- Bar 9: 1-2 kHz +0.9 -> +4.3.
- Bars 66-70: +12.5 -> +11.1.

**Check.**
- Horn 1 at least 0 dB over the accompaniment at 1-2 kHz in every bar 7-14.
- Horn 1 1-5 kHz share still -17..-21 dB.
- Horn 1 bar levels within 0.5 dB of c39.

**ONE_TIME interaction.** The hall (160 Hz low cut) carries a large share of these passages' 200-500 Hz. Measure bars 7-14 after the shorter IR first. If the ratio is already under +9.5, use a -2 dB bell. Horn release caps do not reach the solo: Horn 1 plays 47 of its 51 notes on Leg Slur MAX, which is not in the cap list.

## 2. The loud passages have no bass fundamental: bars 61-62 and 76-79 are 3-8 dB light at 56-125 Hz, while the celli fill 160-500 Hz (measured; "not solid" inferred)

**Evidence (measured; band relative to 500-2000 Hz).**

| | 56-125 Hz | 160-250 Hz | 315-500 Hz |
|---|---|---|---|
| Dvořák 9/i, loudest 10% | -8.9 | -4.1 | -3.0 |
| bars 61-62 (qn 204-212) | -12.0 | -8.3 | -5.7 |
| bars 76-79 (qn 256-265) | -16.7 | -8.5 | -4.4 |

- At 256-262 the basses' E flat 2 / E2 fundamental (79 Hz band) is 7.8 dB under their own second harmonic (157 Hz).
- Three things stack on it:
  - the static bell2 at 80 Hz -6 dB (series 1, for soft D2/F2 boom);
  - the loud-span lowshelf at 100 Hz -3 (`loud_eq`, windows 190-216 and 254-271);
  - the Basses KS Master's weak recorded fundamentals (kit LEARNINGS 14).
- The celli (static 170 Hz +3 bell, 1.5 oct wide, plus a 150 Hz +4 loud bell) supply 66-75% of 160-250 Hz in bars 53-60 and 79-81.
- A floor that is light, under normal low mids, makes the low mids stand in for the bass (inferred).
- c39 B #3 left this open for limiter headroom. The version below keeps the master's peak level.

**Fix (`build/mix.json`, loud windows only; the static bell2, the 160 Hz bell and every soft span stay).**
- Double basses `loud_eq` bands: replace `{"band": "lowshelf", "hz": 100, "db": -3}` with `{"band": "bell", "hz": 78, "db": 4, "bw_oct": 0.8}`. Keep the 150 Hz +4 bell. This changes series 1's "climax shelf -3" from the do-not-touch list; the reason for it (basses 7.5 dB over Dvořák below 100 Hz) no longer holds.
- Violoncellos `loud_eq`: 150 Hz bell +4 -> +2, and add `{"band": "bell", "hz": 350, "db": -2, "bw_oct": 1.0}`. This is the 200-500 Hz cut Dan's note asks for, placed where the celli are the largest contributor.

**Simulated.**
- Bars 76-79: 56-125 Hz -16.7 -> -12.4; bars 61-62: -12.0 -> -9.5. 315-500 Hz is unchanged within 0.1 dB.
- K mean +0.03 dB, K p99 +0.0/+0.1 dB, so the delivery limiter should not move.

**Check.**
- 56-125 Hz at bars 61-62 between -10 and -8.
- 63 Hz third-octave no more than 2 dB over Dvořák's loud frames.
- Limiter at or under 2.5 dB.

**ONE_TIME interaction.** The 150 ms caps on string Sus MAX shorten every bass and cello note end in these tuttis. That makes the low end more intermittent, so this fix becomes more useful, not less.

## 3. Bars 62 beats 1-2 (qn 208-210): Trombone 2, printed f, reaches the ff Violins I melody and passes it at 209 (measured)

**Evidence (K re master per 0.5 qn).**
- Violins I against Trombone 2: 208.0 -7.5/-8.9, 208.5 -7.8/-9.2, **209.0 -9.5/-8.8, 209.5 -11.1/-10.2**, then 210.0 -8.1/-11.6.
- A-weighted over 208-210: Violins I -7.7, Trombone 2 -8.5.
- Trombone 2 prints f, a tenor counter-line, against the strings' and Horns 1-2's ff. It carries `dyn_trim_db` f +4.4 plus c37's brass +3. Rimsky-Korsakov (PDF p.41) puts one trombone f equal to two horns, so a printed f trombone level with the ff melody is too loud by about one step.

**Fix (`build/score_config.py`).** `CC7_POINTS["Trombone 2"] = CC7_POINTS.get("Trombone 2", []) + [(207.90, 127), (207.97, 95), (209.90, 95), (209.97, 127)]`.
- This is -2.5 dB pre-hall on the 208 note only.
- It falls during the 206 note's last 0.03 qn, before the new onset, so no hall tail is cut (S3).
- Simulated: Violins I over Trombone 2 by +3.9 at 208.5 and +1.8 at 209. Master -0.1 dB.

**Check.** Violins I is the loudest stem (K and A) on every 0.5 qn from 204 to 212.

**ONE_TIME interaction.** STR_REP_NEW_BOW will turn the ff tenuto repeat at 206 into a fresh stroke. The c39 Violins I +3 at 205-207.6 was fitted on the old merged re-attack, so re-measure 204-210 as a whole before adding anything.

## 4. Coda bars 87-90 (qn 286-295): Horn 4 sits 2-5 dB over Horn 3 at the same printed pp con sord., and 3 dB under Clarinet 1's dolce solo (measured)

**Evidence.**
- Horn 4 minus Horn 3 per qn, 286-295: +3.9, +3.0, +4.6, +1.6, +2.4, +0.3, -1.0, +2.4, -0.2, +2.3.
- Horn 4 is rank 3-4 in the master and stands 2.7 / 4.7 dB under Clarinet 1 in bars 87 / 88.
- The score prints both horns pp under one "con sord." (Hn 3-4 staff, bar 87). The solo sits over a pp chord in which Horn 4's low line (F3 - E3 - E flat 3) stands out (inferred).

**Fix.** `CC7_POINTS["Horn 4"] = CC7_POINTS.get("Horn 4", []) + [(280.0, 127), (280.1, 90)]` (-3 dB, set while Horn 4 rests, 271.1-286).

**Expected.** Horn 4 within ±1.5 dB of Horn 3 and 5.5-7.5 dB under Clarinet 1 in bars 87-88.

**ONE_TIME interaction.** The horn caps (237 ms on Sus MAX) shorten Horn 4's note ends at 289 and 292 but not its level. Keep this fix.

## 5. Coda bars 83-86 (qn 274-286): the celli's 4-soli ppp pedal is louder than the full section's ppp and covers the timpani's pp answer (measured)

**Evidence.**
- Violoncellos div (half-section patch, A flat 2 pedal) at ppp: median K 13.8, against the full celli's ppp 11.3, so 2.5 dB louder with fewer players.
- At 277-280 (the timpani's E flat-C-A flat answer, pp, thematic) the pedal is the loudest stem: A-weighted -4.0 re master, timpani -5.3. K: pedal -5.3, timpani -4.1.
- At 274-277 the harp harmonics (p dolce) stay clear of it in A-weighting (-1.6 against -10.0).

**Fix.** `CC7_POINTS["Violoncellos div"] = CC7_POINTS.get("Violoncellos div", []) + [(272.0, 127), (272.1, 95)]` (-2.5 dB).
- It is set in silence (the track's previous window ends at 66) and holds to the end.
- This is on the half-section track. It does not change the viola halves, which the "coda divisi balance" do-not-touch protects.

**Check.** The timpani are at least 1.5 dB over the pedal (A) at 277-280. The 286 handoff to the tutti celli is not louder than the div pedal before it by more than about 6 dB.

**ONE_TIME interaction.** The pedal plays Sus MAX (ART_SPANS), so the 150 ms cap applies to its five re-bow joins (275.53-284.14). Refit them with `fit_rebows.py` first, then confirm the level, since deeper join dips lower the pedal by themselves.

## 6. Balance settings that the shorter tails and release caps may make unnecessary or wrong (inferred, from the c38/c39 measurements and Movement I c44)

- **Solo levels: do not add any solo lift in c40.**
  - The wind and horn phrase ends already drop 16-23 dB at +0.3 s (c39 B #6), against 13-17 in recordings.
  - The new IR envelope shortens every tail, and the 150 ms caps shorten the string accompaniment's sustain. The winds get no caps, so legato solos over strings will gain relative level.
  - Re-measure the solo margins above (bass clarinet 31-36, cor anglais 41-50, Oboe 1 45-47) after the render. Cut, rather than lift, if any margin grows past +6.
- **c39 bars 79-80 (Violins II CC7 -4.5 at 264-265.75; Violins I fill 264.417 +2.5).** Both were fitted on uncapped releases. Refit the fill with `fit_rebows.py`, then check Violins I at least 1 dB over Violins II at every 0.25 qn from 262 to 265.75 before keeping the CC7 depth.
- **c39 B #4: basses +3 at 226-238 under Horn 1.** The pedal's re-bows (225.215, 227.775, 230.393, 233.038) are Sus MAX. Movement I's caps deepened re-bow dips by 2-3 dB before the refit, so re-measure the pedal against Horn 1 after the refit, not before.
- **Coda short-term loudness.** The coda sits at -41..-52 dB per bar. With less hall bed, its short-term loudness may fall 0.5-1 dB, and the delivered span (19.0 now, target at most 19) may cross the limit. Check the delivered span. Fix it with `soft_trim_db`, not CC11.
- **Finding 1's bell depth** depends on the hall change (above). **Finding 2** is made more necessary by the caps.

**Do not touch:**
- fx_volume 0.095 and the 160 Hz hall low cut; no master or bus EQ at 200-500 Hz (the global share matches the references);
- the c39 bars 61-62 balance (Violins I +3, Horn 1 lift 5.5, Violins II CC7), except as re-measured after STR_REP_NEW_BOW;
- the bars 79-80 Violins II CC7 (refit only);
- Horn 1's 800 Hz -8 soft shelf (its 1-5 kHz share is on target);
- the solo margins listed above;
- the timpani levels at bars 61-64, 67-70 and 79-82;
- the viola-half and Violins II div balances;
- the Violin I solo level;
- Clarinet 1's coda CC7;
- Flute 1's bars 41-44 counter-line level;
- the static Cb bell2 80 Hz and 160 Hz bells.
