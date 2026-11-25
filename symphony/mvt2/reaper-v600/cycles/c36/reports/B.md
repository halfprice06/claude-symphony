# Cycle 36, critic B: balance and levels (on the c35 render)

**Method.**
- Stems and master from `cycles/c35/render/`. These are the stem-fixed stems; `build/parts.json` matches them, including the two fills lowered after the render.
- **Level scale.** K-weighted: the BS.1770 response applied to 4096-point Hann spectra, 25 ms hop, both channels summed, ungated. On this scale the master reads about 3 dB under its gated LUFS.
- **Bands.** Unweighted 20-100, 100-300, 300-2000 and 2000-5000 Hz from the same frames.
- **Note bodies.** From the score onset + 0.15 s to 0.05 s before the played end.
- **Time base.** Score qn mapped on the parts.json tempo map.
- **Simulations.** dB gain applied to the stem frames, with the master re-summed (stem power out, new stem power in).
- **Labels.** "Measured" means a number from the render, parts.json or a table. "Inferred" means a judgement about what a listener hears.

## Manual notes (B3: May 2021 HO manual pp. 123-126, timpani; `loop/MANUAL-GAPS.md` read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.123 **Timpani Felt Long**. Long hits; left-hand variations at C1-A2, right-hand at C3-A4. Two notes closer than 65 ms play a double hit. Velocity selects up to 16 levels. | The strokes at 172, 203, 209.5, 277, 278.5 and 279, on the Lng row (KS 24). | Yes. No two strokes are closer than 0.5 qn. The coda's pp strokes (v56/60/60) are the loudest stem in bar 84 (-47.9 / -46.8 against the celli 4 soli at -48.6), which suits an answering phrase. The f stroke at 203 reaches -3 dB of the master in 100-300 Hz (measured). |
| p.123, p.125 **Felt Cresc**. Live-recorded crescendo rolls in three key ranges of different lengths, ending on a hit, 2 velocity layers ("the most realism"). | The pp < rolls at 168-172, 200-203 and 261-262. | No. They are still played on the Rls row with a CC1 ramp plus CC7 and the envelope (MANUAL-GAPS #7). Their levels are not wrong: the 200-203 roll rises 10 dB, rank 14 → 6 of 23. |
| p.124 **Felt Rolls**. CC11 and velocity set loudness; CC1 sets the dynamic in 8 layers. | Every roll. | Partly. CC1 follows `TIMP_CC1_MAP`. Both f rolls (204-209.5 and 262-268) sit on CC1 88, the same layer, so the 10 dB difference between them in finding 2 is in the envelope, not the layer (read, parts.json). The KS patch has no CC11 (KIT §10). Loudness comes from CC7 plus the envelope. |
| p.124 **Felt Short**. Hits damped "within a beat or two", more realistic than automation. | "damp" at 210, after the 209.5 stroke. | Damping is done by note-off on the Lng row: -32.1 → -43.3 dB by 210 and -55.9 by 211 (measured). This is audible as a damp. The Short row is not used. |
| p.124 **Felt KS**. C0 long, C#0 short, D0 flam, D#0 roll, E0 cresc. | parts.json `ks`. | Yes. Only 24 (Lng) and 27 (Rls) are used. The keyswitches land 0.06 qn before each stroke (171.94, 202.94, 209.44, 271.5). |
| p.123, p.125-126 **Flam; the hard-mallet set**. | The score asks for soft sticks and prints no flams. | Yes: the Felt patch is the right one. |

## 1. Bar 28 (the f peak of section A, qn 81-83): the celli's A flat 3 is 8 dB louder than their printed f arrival, and the main viola half drops out for 0.8 s (measured)

**Where.**
- Violoncellos, qn 81 (A flat 3, inside the crescendo) and 82 (F3, printed f, then decrescendo; `aOneVc` bar 28). The violins reach their f B flat 5 at 82.
- Violas (main half), qn 81 (D flat 4 of the `<des' f'>4 <des' f'>4\mf` chords). The upper F4 is on Violas div.

**Celli: the counter-melody's crescendo reverses at its f arrival (measured).**
- Note bodies:
  - 81 A flat 3 (mf, in the crescendo): -28.5 dB.
  - 82 F3 (printed f): -36.3 dB.
  - The f arrival is 7.8 dB *under* the note before it.
- 0.1 qn frames:
  - The celli peak at -27.0..-27.5 over 81.3-81.6. That is 3-4 dB over Violins I (-30.9..-32.6) and Violins II (-29.4..-30.8), right as the violins climb to their peak.
  - At 82.0-82.4, while the violins peak (Vln II -23.3, Vln I -28.0), the celli are at -37..-38.6.
- Causes (read):
  - Volume envelope: the c28 early fill `early_fills.json` Violoncellos "81" {6 dB, pre 0.11 s, hold 0.35 s} sits on top of the series 1 role `[78, 87, -6]`. vol_db is +2.2..+2.5 over 81.0-81.31 and -3.0 at 82. That makes 5.2 dB of the difference.
  - The sample: the Leg BC A flat 3 swells by itself at 81.4-81.6. The level holds at -27.0 after vol_db has fallen 5 dB. That is the remaining 2-3 dB.
  - The other celli A flat 3s are not hot at their own dynamics (204: +1.5 dB over neighbours; 265: +2), so this one note at CC11 79-87 is the outlier. LEARNINGS §13 reports the same pitch hot at f.

**Violas main: a same-pitch re-attack on Leg Slur MAX (measured).**
- The D flat 4 at 80 plays Sus MAX (v63). The D flat 4 at 81 starts 0.03 qn after it on Leg Slur MAX (v68, KS at 80.94), with no gap.
- The stem falls from -37.4 (80 body) to -50..-56 dB over 81.2-81.7. That is a 13-19 dB hole for about 0.8 s, while Violas div's F4 holds at -35..-37.
- This is the established case "a same-pitch re-attack on Leg Slur MAX plays the slow first-note layer" (BRIEF, facts).
- The printed beat-2 repeat at 82 is merged into the 81 note on both viola tracks (81 lasts 1.87 qn on the main track, 2.05 on div). That repeat is S1's concern, for critic A.

**Why it matters (inferred).** Bar 28 is the loudest bar of section A. In it the alto chord thins to one note, and the cello line swells on the wrong note. Its f peak then sounds like a fall, so the climax reads as violins over a sagging middle.

**Fix.**
- **Celli** (level only). In `build/score_config.py`:
  `LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(80.95, 0.0), (81.05, -5.0), (81.65, -5.0), (81.9, 4.0), (82.85, 4.0), (83.0, 0.0)]]`.
  The rise at 81.65-81.9 happens inside a sounding legato line, so no tail is cut.
  - Simulated: celli 81 body -28.7 → -33.4 and 82 body -36.4 → -32.4. The f arrival is now 1 dB over its approach.
  - The celli now sit about 2 dB under each violin section at 81 and 3-6 dB under them at 82, where they peak.
  - Master: bar 28 -0.1 dB; 81.1-81.6 -1.4 dB inside a crescendo that still rises 4 dB to 82.3.
- **Violas main** (row only; Sus MAX is already loaded on the track). `ART_SPANS["Violas"] = ART_SPANS.get("Violas", []) + [{"from": 80.95, "to": 81.5, "art": "Sus MAX"}]`. The 81 chord tone then starts as a fresh stroke, like the 80 note before it.
  - Measure it after the render. Target: the 81.1-81.8 level within 3 dB of the 80 body (-37.4).
  - LEARNINGS mvt1 c07: Sus MAX can sit 2-6 dB over Leg Slur at f. If it lands more than 2 dB over Violas div's F4 (-35.5 body), add a step trim on the 81 note.

## 2. The timpani's printed f roll in bars 61-62 is masked from its first beat: 13-18 dB under the tutti in its own band, against 8-10 dB for the same printed f roll in bars 79-80 (measured)

**Where.** Timpani, qn 204-209.5: f roll on D flat 3, CC1 88, then the 209.5 stroke and the damp at 210. The control is the f roll at 262-268 (A flat 2 / D flat 3, same CC1 88).

**Evidence (measured; timpani minus master per band).**

| | 100-300 Hz | 20-100 Hz | K-weighted | rank (K) |
|---|---|---|---|---|
| 204.0-204.25, the roll's start | -12.6 | -21.4 | -18.0 | 21 of 23 |
| 204-206 | -15.4 | -23.9 | -21.8 | 21-22 of 22 |
| 206-208 | -18.5 | -33.2 | -26.3 | 22 of 22 |
| 208-209.5 | -16.6 | -26.6 | -26.5 | 22 of 22 |
| control 262.0-262.25 | -4.5 | -6.6 | -13.3 | 14 of 21 |
| control 262-265 / 265-268 | -8.4 / -9.9 | | -16.1 / -18.8 | 18-20 of 21 |

- In 100-300 Hz the celli (-20.5..-25.3) and the basses sit 12-15 dB over the roll for the whole of bars 61-62.
- Cause (read, parts.json vol_db):
  - The bar 61 roll settles from +14.9 at 204.01 to +3.9 by 207 and holds there to 209.5.
  - The bar 79 roll settles from +15.8 to +7.8 and holds there.
  - The bars 61-62 tutti is also about 5 dB louder than bars 79-80 (master -10.4 against -15.1).
- So the same printed f sits 4 dB lower in the envelope under a louder orchestra.
- The 203 f stroke (-3.1 dB in band) and the 209.5 stroke (-9.6) are heard. The roll between them is not.

**Why it matters (inferred).** Dan's rule is that a roll starts at its printed dynamic and then settles under the texture. Here it starts already under the texture, and the movement's climax has no timpani between two strokes. The rule against a roll covering the orchestra stays met after the fix (rank 21-22 of 22 on the K scale).

**Fix (level only; a rise, so no hall tail is cut).** In `build/score_config.py`:
`LEVEL_SHAPES["Timpani"] = LEVEL_SHAPES["Timpani"] + [[(203.98, 0.0), (204.05, 5.0), (209.4, 5.0), (209.47, 0.0)]]`.
The release ends before the 209.5 stroke, which keeps its own shape.
- Simulated with +4: 100-300 Hz share -15.4 / -18.5 / -16.6 → -11.6 / -14.6 / -12.9 per window. +5 brings it to about -10.6 / -13.6 / -11.9, close to the bars 79-80 roll.
- Master +0.1..+0.2 dB in 100-300 Hz and +0.04 dB K-weighted, so the limiter and the climax order do not move. The roll stays under every string section and every low brass part.

## 3. Clarinet 2's pp plays 3-6 dB over the other parts marked pp: it is the loudest stem in the introduction's wind chord, over Horn 3's C-D flat-C, and stands out of the pp accompaniment in bars 71-73 (measured)

**Where.** Clarinet 2 at:
- qn 6-18 (bars 3-6, pp, the wind chord);
- qn 238-250 (bars 71-74, pp, under the violins' p theme);
- qn 292-304 (bars 89-92, niente < pp > ppp, the morendo).

**Evidence.**
- **Note bodies against the other parts at the same printed dynamic, same window:**
  - bar 3: -43.1 against a median -45.8;
  - bar 5: -43.6 against -46.1;
  - bar 6: -42.9 against -46.3;
  - qn 238: -41.0 against -47.0;
  - qn 246: -41.0 against -45.6.
- **Clarinet 2's pp median against other families' pp:**
  - Clarinet 2 -43.6 (9 notes);
  - bass clarinet -46.9, Bassoon 1/2 -45.7/-46.8, Horns 3/4 -48.5/-46.8;
  - string sections -45.0..-47.2.
- **Bars 3-4.** Clarinet 2 is the loudest stem (-44.1 / -42.4), over Horn 4 (-46.4 / -44.4), the bass clarinet (-45.9) and Horn 3 (-47.3 / -46.5).
- **Bar 5.** Horn 3's D flat, the only moving voice the introduction gives the winds, comes out level with it (-43.6 against -43.8).
- **Bar 71.** Clarinet 2 sits only 4 dB under the violins' p theme. The other pp accompaniment (violas -44.0, Bassoon 1 -46.8, basses -47.4) sits 7-10 dB under.
- **Bars 89-92.** In bar 90 it is the loudest stem (-44.3, over the celli at -45.7 and Violins I at -46.8). In the final ppp chord it is level with Violins I's closing C5 (-54.4 against -55.1).
- **Cause (read, `mix.json`).** Clarinet 2 `soft_trim_db` is pp +5.1 and ppp +2.3, against p +4.4. Clarinet 1 has the same shape (pp +5.4, p +1.4). c30 set these to hold the c29 levels after CC1 moved the clarinets onto their soft layers.
- **Norm.**
  - Rimsky-Korsakov (`reference-books/text/rimsky-principles.txt` l.1316-1318): the clarinet "can reduce volume of tone to a mere breath".
  - Adler (`adler1/p0210.txt`): the clarinet has the full range "from the faintest pianissimo".
  - So a pp clarinet should sit at or under the other winds' pp, not over them. The darker CC1 layer gives the right colour, but the trim then lifts the level back to mp.

**Why it matters (inferred).**
- In the introduction the clarinet's low E flat covers the horn's chromatic turn.
- In bar 71 a pp inner part competes with the cello counter-melody.
- At the end the clarinet, not Violins I's C5, is the top of the final chord.

**Fix (level only).** `build/mix.json` "Clarinet 2" `soft_trim_db`: pp 5.1 → 2.6, ppp 2.3 → 1.0; p, mp and mf unchanged.

**Simulated (per bar, Clarinet 2 → new; next loudest stem in brackets).**
- Bars 3-6: -44.1/-42.4/-43.8/-44.7 → -46.6/-44.9/-46.3/-47.2, now level with the bass clarinet and Horn 4. Horn 3's D flat in bar 5 leads by 2.7 dB.
- Bar 71: -41.2 → -43.7, 6.5 dB under the theme.
- Bar 90: -44.3 → -46.5 (celli -45.7).
- Bar 92: -54.4 → -55.7 (Violins I -55.1).
- Master: bars 3-6 -0.4..-0.9 dB, bars 71-74 -0.1..-0.3, coda -0.2..-0.5.
  - The introduction sits at the delivery ride's cap, so expect most of that 0.4-0.9 dB to reach the mp3.
  - Check the delivered p10 span after the render. If it widens past 19 dB, give the intro +0.5 dB on its string `soft_trim` ppp instead of keeping the clarinet up.
- Leave Clarinet 1's trims alone: its pp is the coda solo, and c35 set its level against the cor anglais.

## 4. The harp's p chord at qn 253 (bar 76) is plucked 7.6 dB over the violins' mf theme at its attack, and 4-5 dB over the harp's chords on either side (measured)

**Where.** Harp, qn 253: D flat 2-A flat 2-D flat 4-F4 rolled, p inside the harp's crescendo to mp at 256, under Violins I's mf theme.

**Evidence.**
- Harp peak in the first 200 ms: -26.1, against Violins I -33.7 and all other stems together -29.0.
- In 300-2000 Hz the harp's attack (-26.3) is 2.3 dB over the whole master's mean (-28.6).
- The harp's neighbouring chords measure, over 0.5 qn: 251 (p) -35.5, 253 -30.4, 257 (mp, the crescendo's goal) -33.9.
- Causes (read):
  - Velocities: v70-76. D flat 4 takes `HARP_PITCH_VEL` 61: +6 (c33) and the top of the roll +4.
  - Envelope: the series 1 harp role `[238, 256, 4]` adds +4 dB.
  - The rest comes from the Sus RR take (LEARNINGS c28: two RR groups 10-12 dB apart at one pitch and velocity).
- No other harp onset in the movement stands more than 4 dB over the loudest other stem.

**Why it matters (inferred).** One p arpeggio pings out of a soft string phrase, in a passage where the harp only fills the harmony.

**Fix.** `build/note_trims.json` "Harp": add `"253": -4.5`. Plucked notes take the step trim shape by default (LEARNINGS §13).
- Expected: 0.5 qn level about -34.9, between 251 and 257, so the crescendo to 256 reads in order.
- Peak about 3 dB over Violins I at the pluck only. Master under 0.3 dB.

## Checks asked for in this lens

All measured unless marked inferred.

**Solos over their accompaniment (note bodies).** Each entry gives the median and minimum over the accompaniment sum, then over the loudest single stem.

| Solo | Over accompaniment (median / min) | Over loudest stem (median / min) | Notes |
|---|---|---|---|
| Horn 1, bars 7-14 | +1.9 / -1.4 | +5.3 / +3.1 | |
| Oboe 1, bars 15-16 | +4.7 / +0.6 | +6.3 / +4.5 | |
| Solo violin, bars 17-18 | +4.6 / -1.3 | +8.3 / +3.1 | |
| Oboe 1, bars 19-20 | +4.5 / -2.0 | +6.6 / +1.9 | |
| Solo violin, bars 21-22 | +2.8 / -2.8 | +6.6 / +1.0 | 60: the celli |
| Bass clarinet, bars 31-36 | +2.5 / -0.9 | +4.3 / +1.2 | 98: the cor anglais' p entry |
| Flute 1, bars 37-40 | +3.6 / +2.3 | +8.2 / +5.4 | |
| Cor anglais, bars 41-44 | +2.5 / 0.0 | +6.4 / +2.8 | |
| Oboe 1, bars 45-47 | +1.7 / -4.8 | +6.6 / +0.5 | The 145 eighth dips 5 dB inside the oboe's own line; the celli double the line an octave lower |
| Cor anglais, bars 47-50 | +3.8 / +1.1 | +6.7 / +4.0 | |
| Horn 1, bars 65-70 | +8.5 / -2.3 | +9.6 / +2.8 | |
| Clarinet 1, coda | +1.1 / -2.3 | +4.8 / +1.9 | Leads the cor anglais by 1.9-2.2 dB, as c35 intended |

Only the bar 28 cello note (finding 1) puts an accompanying part over a melody for more than a beat.

**Climaxes.**
- **Bars 61-62.** Strings -17.3..-23.7 per section. Winds -24..-30, horns -22.6..-28, low brass -23..-26 (f). The timpani roll is too low (finding 2).
- **Bars 63-64.** Trombone 1 -20.9 / -22.4 (ff) leads the strings' sf → p by 2.7 dB in bar 63 and by 15-20 dB in bar 64.
- **Bars 79-82.** No trombones play. The timpani roll is at rank 14-20 and falls with its decrescendo, 268 → 271: -34.1 → -49.1.
- **Low brass.** Nothing covers anywhere. The bar 60 pp < f crescendo of tuba, bass trombone and Trombone 2 rises from -45..-52 to -23..-25 under strings at -15..-20.
- **Climax order.** Bars 61/62 -14.3/-15.0 against 79/80 -19.3/-19.9 (plain RMS, metrics.md). Findings 1-4 move either by at most 0.2 dB.

**Dynamic mapping (median note bodies of notes of 0.75 qn or more).**
- Macro dynamics: bar level against the bar's 90th-percentile printed dynamic gives a correlation of 0.93 and a slope of 4.8 dB per step. Outliers:
  - bars 61-62: +6.5, the full tutti;
  - bar 1: +5.5, the ppp opening; it is only about 2 dB under bar 2's pp;
  - bars 83-84: -7, the harmonics' p over a ppp pedal.
- Strings are consistent: basses 4-6 dB under the celli at every dynamic from ppp to ff on the K scale (arco only).
- Single winds at ff: -26.9..-30.7. String sections at ff: -18.8..-25.3. That fits Rimsky's forte ratio.
- The exceptions are Clarinet 2 (finding 3) and Clarinet 1, whose pp (-42.2) is above its p (-43.2): the coda solo is its only pp passage.

**Half-section and 4 soli tracks.**
- Violins II div (Flautando, pp) is within 1 dB of the Violins II half: -45.9 against -45.0.
- Violoncellos div sits 3 dB over the celli where it answers the solo violin (bars 18, 21-22), as the score's roles ask.
- Celli 4 soli (bars 83-86, ppp): -49.8, about level with the tutti basses' ppp.
- Basses 4 soli: bars 65-70 -50..-52, about 1-2 dB under their tutti pp (-49.4); coda -53..-55, 4-5 dB under.
- Violas div runs 2-3 dB over the main half in bars 23-30 and the coda, except at 81 (finding 1) and 87. At 87 the printed p > pp makes the main half fall 9.6 dB against div's -48.1.

**Bass (inferred, from metrics.md).** Band shares: 20-100 Hz -20.4, 100-250 Hz -8.8 dB, within the references' range. No stem booms. The coda pedal and the bass clarinet's chalumeau make the heaviest bars, as in c35. No change.

**Gains, soft trims, CC11/velocity.**
- The largest soft trims are Bassoon 2 pp +8, the low brass p +7.8, and the basses p +6.5.
- Bassoon 2 pp +8: the bassoons' pp (-45.7/-46.8) matches the other winds, so it is not over.
- Low brass p +7.8: few p notes (bar 64 under the quotation, -43..-49); not over.
- Basses p +6.5: within the basses' consistent 4-6 dB under the celli.
- Only the clarinets' pp trims produce a level out of family order (finding 3).

**Standing checks inside this lens.**
- S3 (cut tails): I scanned every track's vol_db for falls of 4 dB or more within 0.13 qn under a sounding note (not at an onset). There is one, Double basses 274.25-274.38 (-4.6 dB), where the stem rises 3.9 dB anyway, so nothing audible is cut.
- Items 8-9, S1 and S2 are outside balance; I did not re-measure them.

**Do not touch:**
- the climax order and the bar 61-62 string holds;
- Trombone 1's quotation levels, shapes and CC7 lanes;
- the bar 79-82 timpani roll and its decrescendo;
- the coda clarinet / cor anglais balance (c35);
- the celli 4 soli on the div track and the basses' coda 4 soli level;
- the solo levels in the table above;
- the timpani mic volumes (Close 0.2 / Main 0.5) and gain -7;
- the Cb and timpani side shelves;
- the horn CC1 map and soft-horn loud_eq;
- harp env_sustain 1.0;
- the violas' f/ff trims and c35 roles;
- Clarinet 1's soft trims.
