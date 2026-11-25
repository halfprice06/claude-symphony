# Cycle 19, critic B (balance and levels), on the c18 render

Everything here is measured on `cycles/c18/render` (stems and master) and the delivered `scherzo-mockup-c18.mp3`, against `cycles/c16/render` and `cycles/c17/render`, using the data in `cycles/c18/build_render/`. Positions are score quarter notes (qn); bar b starts at qn 3(b-1).

Terms:
- "Level" is the mean power of a stem while its notes sound, averaged over both channels.
- "Best band" is the highest ratio, over 1/6-octave bands, of a line's power to the power of every other stem plus the returns. Only bands within 10 dB of the line's own strongest band count. The ratio is averaged over the frames where the line's notes sound. A line under 0 dB in its best band is covered in every band where it has energy.
- "Frames over" is the share of 21 ms frames in which the line beats everything else in that band.
- "M" and "S" are ffmpeg ebur128 momentary (400 ms) and short-term (3 s) loudness.

Each judgement is marked (m) measured or (i) inferred.

## Manual notes (slot B1: May 2021 HO manual PDF p.137, 140, 150-151; MANUAL-GAPS.md)

| reading (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| Each KS Master row has a load button and a volume knob (p.137) | Rows a track does not use are unloaded (`UNLOAD_UNUSED_ROWS`). Row levels: Violins I "Sus Marc LITE" -8, Flute 1 / Flute 2 / cor anglais "Stac DblTng" ±2.5-3 | Yes. Loading follows (43 GB settled). Levels are set as region volumes (`row_db`), because the knob itself does not act (finale technique 83). |
| The master channel's gain fader changes the instrument's output without changing the mic sub-mix; pan keeps the relative mic panning (p.140) | Track gains (`mix.json gain_db`), `mic_db` per track, Horn 3 `channel_map` 2 | Yes. Levels are set in REAPER and as mic dB. The Opus gain fader is not automated. |
| Note Velocity Sensitivity curve (linear by default, -100 to +100); velocity selects the dynamic samples on shorts (p.150) | Pizzicato, staccato, harp and timpani velocities: celli pizzicato 52 across the 50/51 layer edge, timpani summit at 114 | Yes, the curve is left at 0. Not used: a convex or concave curve on a pizzicato track could narrow a per-key spread without per-key tables (i). |
| Send CC1 and CC11 before the first notes (p.151) | The 3 qn silent pre-roll carries every first CC value | Yes. |
| CC7 sets a track's upper limit; CC11 shapes a line (swells, phrase dynamics) (p.151) | Balance lives in the REAPER envelope (after the hall). Shaping is in CC11 / CC1 (before the hall, S3). CC7 is used only on the timpani. | Yes in spirit. Finding 1's fix uses CC11, which is the manual's tool for raising a line inside the instrument. |
| On HS / HW Opus patches CC11 = loudness and dynamics and CC1 = vibrato; on LITE articulations CC1 does the dynamics (p.151) | Violins I "Sus Marc LITE" (36 notes: the theme head's half notes, the hemiola strokes 300-310 / 902-910) | Yes (m). On those 36 notes the pipeline's CC1 follows CC11 within 8 units (300: 90 / 88; 310: 95 / 104), so the dynamic layer follows the printed dynamic. Any future CC11-only change on that row must move CC1 too. |
| MANUAL-GAPS #9 half-section patches; #13 Mid mics on woodwinds and horns | Violins II "la metà", woodwind and horn depth | Unchanged. Not needed for any finding below. |

## Answers to the cycle 19 questions (m unless marked)

- **Hidden inner lines.** I scanned the whole movement in 2-bar windows: every track that plays at least 3 pitches and is not doubled by another track (pitch class and onset), plus the doubled groups as groups.
  - Every doubled group is audible: best band 0 dB or more in every window except Clarinet 1 + Oboe 2 in bar 335 (-3.4).
  - The tutti countermelody (celli, Bassoon 1, Horns 3-4) now sits 2.9 / 3.6 dB under the theme group, with best band +3.1 / +3.8. The theme keeps +10.7 / +12.9. c18's rows did what Dan asked.
  - The celli's espress. line in 281-288 went from -4.0 to -0.5 in its best band.
  - Among the undoubled lines, only one line marked or written as a line is covered in a quiet passage: Violins II's con sord. arpeggios (finding 1).
  - The other low windows are printed-softer inner voices inside f-ff tuttis. Examples: Clarinet 1 / 2 at mf under the f-ff second idea, bars 49-55 (-5 to -7); Horn 2's held chord tones at 119, 127-129, 319 (-7 to -11); violas' repeated B at 125 (-8). These are covered as a real orchestra would cover them, so I propose no change.
- **f arrivals 1.8-2.2 dB under c16.** The cause is known and the shortfall should be kept (finding 2).
- **Horn 3 after "Mono From Left".**
  - Per pitch against c17 (same data otherwise): median +0.7 dB, range -3.7 to +3.6. Horn 4 (unchanged) reads 0.0.
  - The +3.6 dB G sharp 4 at 1092 is a hand-off from Horn 1. The Horn 1 + Horn 3 sum per 2 qn over 1084-1104 now reads -47, -49, -48, -47, -45, -45, -45, -47, -45, -44. c17's sum dipped to -51 at the hand-off. Keep it.
  - Only E4 needs a small fix (finding 5).
- **The 17 bars more than 1.5 dB from c17** (top stem contributions per bar):
  - Intended:
    - 62 / 294: violas fugato +14, +3.7 dB;
    - 71 / 299 / 300: the bar 72 / 300 woodwinds, +1.9 to +7.5;
    - 110: Flute 2's A6 -9.4;
    - 137 / 138: the low-group rows deleted, celli and basses -1.5 / -2.0 at printed p;
    - 288: the celli's -3 row now ends at 840, +4.7.
  - Already fixed in build/:
    - 18 / 258: Violins I "Sus MAX", -8.0 / -7.2 on the stem;
    - 66: Violins II +30, +14.5.
  - 184: Bassoon 2 +2.8 and celli +2.3, from the crescendo gains that stay in the envelope (the bar 184 crescendo). Acceptable.
  - 290: celli -2.6 with identical CC11, rows, keyswitches and envelope in c17 and c18 at 864-871. Inferred: a different round-robin or legato take (finale c21 #8). Do not fit to it.
  - 328: a side effect of the c18 trim-hold skip (finding 2).
  - 365 / 366: Horn 3 +3.1 / +4.2 (the hand-off above). In 365 the master is 1.8 dB under the power sum of its stems: Horn 1 and Horn 3 partly cancel on the same G sharp 4 (finding 5).
- **Bar 300 against the tuttis.**
  - Print: bar 300 is a wind, string and four-horn ff chord (18 tracks). The 305-320 tutti adds timpani and cor anglais; the 105-120 tutti adds full brass (24 tracks).
  - Delivered mp3, S max: bar 300 -10.5, 105-120 -8.9, 305-320 -9.4. Bar 300 is 1.1-1.6 LU under both tuttis. On M max it ties 105-120 (-8.3) and is 0.3 under 305-320.
  - Bar 300 now stands where the print puts it. No further change.
  - One small inversion on M: bar 304 (the ff arrival of the sfp crescendo) reads -8.5 against bar 300's -8.3. On S, 304 leads (-9.6 against -10.5), so leave it.
- **Delivered order of the printed dynamics** (context, not a fault of the mix):
  - On the mp3 the f bars 41-44 / 129-131 read M -9.2 / -9.0 against the ff tuttis' -8.3 / -8.0. That is 0.9-1.2 LU, where the master has 6.6 LU (-20.4 against -13.8).
  - On M, bar 72 (-7.8) and bar 53 (-7.9) are above the first tutti (-8.3). On S they are at or under it (-10.5 / -8.9 against -8.9).
  - I tested the delivery offline (`deliver_master.py` into scratch). Top ride from 5 dB under p95 with lift 1.8, or from 6 dB at 2:1, gained only 0.2-0.6 LU of f/ff spacing. It raised the limiter on the tuttis to 4.3-4.4 dB and LRA to 13.2-13.3.
  - The squeeze comes from the -14 LUFS target with about 5 dB of limiting, not from the ride. Keep the delivery as it is. Do not add level to the f bars in the mix (finding 2).

## Findings, ranked by what a listener would hear

### 1. Trio, bars 168-184 (qn 501.5-551.5): Violins II's con sord. arpeggios are covered in every band (m)

**Print.** Violins II, pp con sord. dolce, play quaver arpeggios. Above them are the celli's tune (mp arco espress.), then Violins I (p dolce espress., from 528) and Flute 1 (p dolce, from 514).

**Measured.**
- Violins II level: 8.6 dB under the celli in 169-176 and 9.8 dB under in 177-184.
- Best band -7.4 dB (508 Hz). Violins II beat the rest of the orchestra there in only 23 % of frames.
- c16 and c17 read the same (-7.2 / -6.6), so this is an old fault.
- This is the only line in a soft passage that the scan finds covered. It is the case Dan described: a moving inner line hidden behind the melody in a quiet part.

**Data.**
- Violins II play "Sus MAX" with CC11 47-50, CC1 95-105, CC15 127 and the role [501.5, 588, +4].
- The celli play CC11 49-69 with the role [504, 552, +2].

**Fix** (instrument side, `build/score_config.py` `CC11_ADD_SPANS`):
- Add Violins II (501.3, 551.4) +9.
- At the measured Violins II "Sus MAX" slope at p (0.48 dB per unit at CC11 41-55; c18 LEARNINGS) that is about +4.3 dB.
- That slope was measured senza sord.: check the con sord. stem and stop at the value that puts the arpeggios 4-5 dB under the celli.
- Targets:
  - Violins II about 4.5 dB under the celli and under Violins I from 528;
  - best band 0 dB or more;
  - the celli's tune still on top (its best band is now +10.4).
- Keep the +4 role. Do not add a fader row.

### 2. The trim-hold skip spans: keep them at the four f arrivals, but make the bar 328 one per track (m)

**Cause of the f arrivals (bars 41 / 129 / 197 / 285).**
- At the arrival beats CC11, CC1 and `vol_db` are identical in c16 and c18 for Clarinet 1 / 2, violas, cor anglais and the others that lose.
- The difference is `mix.json` `cresc_trim_hold.skip`: c17 added [108, 120], [372, 384], [576, 588] and [840, 852] when it moved the crescendo gains into CC11.
- c18 put the gains back in the envelope on every track except Flute 1, cor anglais and Violins I / II, but the skip spans are global. So the non-converted tracks lose the hold: min(0.7 x (p trim - f trim), 3.5) dB.
- That predicts the measured losses against c16:

| track | measured loss against c16 (dB) |
|---|---|
| Clarinet 1 / 2 | -4.3 / -4.5 (bar 41) |
| violas | -3.1 to -3.4 |
| double basses | -3.2 / -3.4 |
| contrabassoon | -3.4 |
| Bassoon 2 | -2.8 / -3.7 |

- Simulated on the stems, giving the hold back to these tracks raises the master at the arrival beat by +2.2 / +1.8 / +2.6 / +2.0 dB, which is c16's level.

**Do not give it back at these four spans.**
- The c18 rise into each arrival is already as large as c16's or larger at 129, 197 and 285 (master, arrival beat against the bar before):

| bar | c16 | c18 |
|---|---|---|
| 129 | +2.5 dB | +2.6 dB |
| 197 | +1.5 dB | +2.1 dB |
| 285 | +3.2 dB | +4.2 dB |
| 41 | +6.1 dB | +4.4 dB |

- After the arrival the f continues as printed: c18's arrival bar and the next bar are level (41 / 42: -24.6 / -24.9). c15 and c16 peaked and fell 1.5-3 dB, which the print does not ask for.
- On the delivered file these f bars already sit only 0.9-1.2 LU (M) under the ff tuttis. Another 2 dB on the master would bring f level with ff on the mp3.
- Close the "1.8-2.2 dB under c16" item.

**Bar 328 (qn 981-984), crescendo pp -> mf into the coda build.**
- c18 added [981, 984] to the same global skip list for Violins II (c18 critic C #4). It also took the hold off the violas (-2.7 dB against c17, -3.8 against c16), celli (-2.7) and Violins I (-1.5).
- The master in bar 328 is -1.9 dB against c17 and -2.6 against c16. The crescendo now gains less of its rise before bar 329.

**Fix** (`build/mix.json`): `build_reaper.py` reads `cresc_trim_hold` from the track before the top level.
- Remove [981, 984] from the top-level `skip`.
- Give Violins II its own `cresc_trim_hold`: a copy of the top-level dict with [981, 984] added.
- Expected: bar 328 back to about c17 (-36.9), with Violins II's own fix kept.

### 3. Clarinet 1 is the loudest stem in f-ff bars where it doubles or accompanies the violins (m)

**Where.** Clarinet 1 against Violins I, per bar (c18):

| bar | Clarinet 1 over Violins I | what Clarinet 1 plays |
|---|---|---|
| 41-44 | +1.5 dB | holds C5 for 6 qn under the theme, f |
| 300 | +2.3 | C sharp 6, ff accented |
| 302 | +1.6 | |
| 334 | +3.9 | G5, the theme an octave under Violins I, ff |
| 214 | +3.9 | trio ff, doubling the tune |

Clarinet 1 is the loudest stem in bars 214, 223, 300, 301, 302, 329 and 334 (metrics "loudest three stems").

**Evidence.**
- One clarinet over sixteen first violins at ff is against the orchestration norm. Rimsky-Korsakov, cited in the score's own c021 note: the clarinet is weak in its middle compass and blends rather than leads in a tutti (i).
- The theme is still audible: best band +2.8 to +16 dB. The lowest is bar 334 at +2.8, where Clarinet 1 sits an octave under the tune.
- Clarinet 1's ff median is -33.5 dB, and its p median -40.8 is the loudest p of any woodwind. Its range from p to ff is 7 dB, against 14 dB for Violins I.

**Fix** (instrument side). The clarinet's dynamics are on CC1 (`CC1_DYN_TRACKS`), and its "Leg Slur Rep" row has no per-dynamic regions, so a region gain cannot select ff.
- In `score_config.py`, set `CC1_DYN_MAP_BY["Clarinet 1"]` = [(22, 18), (34, 28), (46, 42), (58, 54), (72, 68), (88, 80), (114, 98), (124, 110)]. That is the default map with f / ff / fff 6-10 units lower: a less bright layer in the tuttis.
- Read the change on the stem. Finale c21 #2 found CC1 changes can land on a layer plateau.
- If the stem moves less than 1.5 dB at ff, use `mix.json` Clarinet 1 `dyn_trim_db` ff +1.2 -> -1.0 instead. This is a per-dynamic mapping trim, not a note move.
- Target: Clarinet 1 1-2 dB under Violins I in bars 300, 302 and 334, and no clarinet as the loudest stem in a tutti bar. The trio ff (209-224) prints the tune in Clarinet 1 with both violin sections, so there a level with Violins I is enough.

### 4. Fugato entries (bars 57-68): the build/ fixes are right; the first entry is now the soft one (m, sizes i)

**Print.** Celli at 168, violas at 180 and Violins II at 192 all enter at p.

**c18 held-note levels.**
- Celli 171: -45.0. Violas 183: -40.9. Violins II 195: -36.5.

**build/ changes.**
- Violins II CC11 +30 -> +24 (CC11 72 -> 66 at 194.46).
  - At the 0.48 dB per unit that the +30 produced (+14.3 dB), this is -2.9 dB, to about -39.4. That is 1.5 dB over the violas. Right in direction.
  - +20 would put Violins II level with the violas (about -41.3). I would take +20.
- Violins I at 49.812 and 769.812 back on "Sus Marc LITE", with CC11 and CC1 at their c17 values.
  - This restores bars 18 / 258, which were -8.0 / -7.2 on the stem. c15-c17 read -35.9 / -35.6 there.
  - Right. The accent size in those bars is critic A's.

**The celli's first entry is 4.1 dB under the violas' at the same printed p.**
- The celli carry [168, 180, +5] already.
- Fix: `CC11_ADD_SPANS` Violoncellos (170.9, 174.0) +8. Size it on the stem from the celli's own slope; c18 LEARNINGS gives 0.27-0.48 dB per unit at p for other sections.
- Target: the three held fugato notes within 2 dB of each other, rising no more than the print's p allows.

### 5. Horn 3 after "Mono From Left": re-level E4 only; the bar 365 hand-off partly cancels (m)

**Per-pitch shifts against c17.** Between -1.8 and +2.4 dB for every pitch with three or more notes, except E4 (MIDI 64): median -1.8, range -3.7 to +0.7.
- In the trio, where Horn 3 doubles the celli's tune, E4 at 509 reads -50 dB between -45 and -44 on its neighbours. That is a 5 dB hole in the line.
- In the 1020 dolce solo, E4 reads -44 between -41 and -45.

**Fix.** `mix.json` Horn 3 `region_gain_db` {"rows": [], "pitch_db": {"64": 2.0}}, applied to every row that plays E4. Horn legato transitions are not keyed by target pitch alone (c15 LEARNINGS), so check the trio notes on the stem.

**Hand-off at qn 1092-1095.**
- Horn 3's new G sharp 4 meets Horn 1's decaying G sharp 4. The coherent sum of the two stems is 1.1 dB under their power sum, and the master is 1.8 dB under the power sum of all stems (c17: +0.8).
- The master per 2 qn dips to -46 there, between -44 and -43. Inferred: a thin, slightly phasey moment at the start of the ppp close.
- Instrument-side options:
  - a different round-robin start on Horn 3 at 1092 (a CC16 / CC36 reset value that selects another take);
  - Horn 3's note-on 0.1-0.15 s after the beat, while Horn 1 is still at its pp.
- If neither helps, leave it. The level fault it replaced was worse.

### 6. Role rows by cause (164 in `build/roles.json`, was 177) (m)

- **Single-note or single-figure fader rows, against Dan's rule.** Replace each on the instrument side:
  - Timpani [300.0, 300.5, -12]: the first half-beat of the bar 101 p roll. Use the roll's own start value (the roll's CC1 or its first-stroke velocity) and delete the row.
  - Trumpets [994, 995.5, -4 / -5]: the pp eighths 994-995. Lower CC1 on those notes (brass dynamics are on CC1).
  - Horns 3-4 [990, 995.8, -4]: their pp-to-ff approach. Lower CC1 by the same amount over 990-995.8.
  - Oboe 1 [672, 676.5, +4]: the codetta's first notes G sharp 5 / A5. Use a CC11 offset or region gain on those pitches.
  - Horn 1 [0, 5.9, +4] is a phrase row: keep it.
- **9 rows under 1 dB: delete.**
  - Harp [216, 240, 0];
  - celli [648, 672, +0.5];
  - Violins II, violas and celli [168, 312] and [864, 912] at -0.7 / -0.8.
  - Keep Violins I [1089, 1128, -0.5], a pair with the solo.
- **14 overlapping pairs: merge each into one row.** For example:
  - celli [552, 624, +3.2] with [576, 612, -7];
  - contrabassoon [168, 312, +3] with [309, 360, -3];
  - cor anglais [168, 312, +2] with [306, 312, -2.5];
  - Violins I [1004.75, 1017, +2.5] with [1008, 1014, +2];
  - Violins II [996, 1016, -2] with [996, 1004.75, -3].
- **60 rows on the tutti and summit spans.** These are mapping rows. Move one into `dyn_trim_db` only where the same track has the same sign at its other ff passages; otherwise keep it as a slow row.

## Do not touch

- The tutti countermelody rows (celli +4.5, Bassoon 1 +3, Horn 4 +2): 2.9 / 3.6 dB under the theme group, theme best band +10.7 / +12.9.
- The celli's -3 row ending at 840.
- The trio tune margins: Clarinet 1 +10.4 over the harp and drone; celli +8.5; Oboe 1 +10.5.
- The solo's +7.7 over Flute 1, with Violins II "la metà" and violas div 7.6-8.5 under.
- Horn 1's motto (+8.1) and last G sharp.
- Horn 3's G sharp 4 hand-off level.
- The summit: strings and woodwinds 6.7 dB over the brass, timpani 16.5 under.
- The first tutti: theme 5.3 dB over the low brass and timpani; trumpets 9.9 under the theme (best band -4.1, present on their attacks only, 25 % of frames: at the lower edge of "present").
- Bar 300 under the tuttis on the delivered file.
- The delivery chain at -14 LUFS.
- The two sub. p's: melody 1.8 dB apart, accompaniment as printed (p / pp).
