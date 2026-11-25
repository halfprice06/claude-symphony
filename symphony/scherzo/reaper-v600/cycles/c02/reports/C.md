# Cycle 02, critic C: dynamics over time (lens C2), on the c01 render

Sources: `cycles/c01/render/` stems and master, the delivered `scherzo-mockup-c01.mp3`, `cycles/c01/build_render/parts.json` and `mix.json`, `build/roles.json`, `build/score_config.py`, `tools/score_to_parts.py`, `tools/build_reaper.py`, the c00 render for comparison, and the latest metrics of Movement I (c43) and Movement II (c37). Levels are plain RMS dB on the parts.json tempo map unless marked LUFS. Bar b starts at qn 3(b-1). My scripts ran from a scratch folder that has since been deleted.

## Manual notes (D1, May 2021 HO manual, PDF pages 53-54 and 64)

| Page | What the manual says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| p.53 (2.5.7) | Velocity is set once, at the start of a note. It suits short articulations. CCs shape sustained notes, because they can change in the middle of a note. | The string strokes on the fff downbeat (qn 1005) and the harp's p espress. hairpins (bars 73-80) | Partly. The fff strokes get their velocity from `REBOW_VEL_BY_CC`, whose top entry is 96, so at fff they speak 9-10 dB under the v119 staccatissimo quarter just before them (finding 2). The harp turns its printed p < > into velocities up to 98 (finding 5). |
| p.54 | Velocity is a single value per note. CC1 and CC11 are curves, so they can shape a note or phrase as it plays. | The sfp at bar 301 and the crescendo after it | The CCs are right: CC11 goes 119 -> 46 in 0.5 qn and then rises. The volume envelope is not: it keeps the previous crescendo's +3..+7 dB through the p (finding 3). |
| p.64 (3.2.5) | In the HO Strings and Woodwinds, CC11 sets loudness and dynamics and CC1 sets vibrato. In other instruments CC1 handles dynamics. CC7 sets a track's level against the others, and CC11 shapes its changing dynamics. | The horns, whose dynamics are on CC1 (`CC1_DYN_TRACKS`; Movement II c30 read the layer groups in the 1FH/2FH .oib files), and the timpani rolls (CC1 layers, CC7 shaping) | No. In the volume envelope, the horns' soft trims (+10-14 dB at pp/p) cancel most of what CC1 and CC11 do between p and ff (finding 1). On the timpani, the roll trim table falls 11 dB from p to f and cancels the CC1/CC7 crescendo (finding 4). |

MANUAL-GAPS items used below: #7 (recorded crescendo rolls) is the alternative for finding 4.

## Findings, ranked by what a listener would gain

### 1. Horns: printed pp and p play as loud as f and ff. In most soft passages a soft horn is the loudest voice (measured; cause read in the configs)

**Where.** Horns 1-4, every soft passage. The pp/p horn is the loudest stem in:
- bars 1-2 and 141-148 (Hn 1, pp);
- 73-88 (Hn 3-4 pp dolce chords);
- 149-152 (Hn 3-4 pp, above the harp harmonics' p);
- 241-244 (Hn 1 pp);
- 281-282 (Hn 2 p);
- 364-369 (Hn 3 pp, Hn 1).

**What is wrong.**
- Per-bar stem medians by printed dynamic: Horn 3 runs pp -42.2, p -38.7, f -37.3, ff -35.5 dB, so p to ff is 3.2 dB. Horn 1's p (-37.4) is louder than its f (-39.0). Horn 2 has p -41.7 against f -41.5.
- The same table in the other movements, same library: Movement I c43 Horn 3 p -46.2 / ff -31.2 (15 dB); Movement II c37 Horn 1 p -43.0 / ff -26.0 (17 dB).
- Per note, with roles taken out (stem level minus parts.json vol_db): on Leg Slur MAX, Horn 3's ff notes (CC11 100+, n=30) measure -39.7 dB and its pp-mp notes (n=33) -38.7 dB.
- Horn 1's p note at qn 900 (A4) measures -32.5 dB. Its ff note three beats earlier (897, C sharp 5) measures -35.2 dB.
- Bars 81-88: Cl 1's "p dolce" tune (-40..-49) sits 2-6 dB under the Hn 3-4 pp chords (-37..-39), the same masking c01 had to fix with roles in the trio.
- The hairpin census (stem level at the start of each hairpin of 2 qn or more against its end or arrival): 7 of 13 Horn 1 crescendos and 8 of 10 Horn 1 decrescendos come out flat or reversed. For the strings it is 3 of 24 (Violins I crescendos).

**Cause (read).**
- The scherzo uses Movement II's soft horn CC1 map: `CC1_DYN_MAP_BY["Horn"]` puts CC1 57-64 at pp-p. The generic map puts CC1 18-42 there.
- But it keeps Movement I's horn soft trims in mix.json: Horn 1 ppp 14 / pp 13 / p 10.6 / mp 7.2, Horn 3 14 / 13 / 12 / 8.4, Horn 4 10 / 9.5 / 12 / 6.7.
- Movement I fitted those trims on the quiet low-CC1 layers. When Movement II c31 moved to the soft map, it set the trims back to ppp 4 / pp 4 / p 4.5 / mp 2.8 / mf 2.0 (mvt2 mix.json; mvt2 score_config c31 comment).
- So the soft horns are compensated twice: about +9 dB too hot at pp, +6..+7.5 at p and +4.4..+5.6 at mp.

**Fix.**
1. In `build/mix.json`, set Horns 1-4 `soft_trim_db` to Movement II's values: {"ppp": 4, "pp": 4, "p": 4.5, "mp": 2.8, "mf": 2.0}. Keep each horn's own mf where it is higher (Horn 2 2.4, Horn 4 3.3). This is the mix only, so `build_reaper.py --mix-only` is enough with no row change.
2. Where a horn carries the line, give it a solo role in `build/roles.json`, so the drones and chords drop and the solos stay in front:
   - Horn 1: [0, 18, +4] (the pp G sharp and the p espress. call), [420, 444, +3], [1068, 1080, +3], [1089, 1128, +4];
   - Horn 3: [1020, 1032, +3].

   My stem simulation of step 1 alone dropped bars 1-6 by 4.8-5.3 dB and bars 364-376 by 3.2 dB. Without the solo roles, the delivery ride, already at its +10 dB cap in the quietest passages, would have to make that up.
3. Remove the c01 trio roles that only existed to push the drone down (Horn 3 [456,504,-3], Horn 4 [456,504,-2]), or halve them, after checking Clarinet 1 against Horn 4 per two bars (c01: +0.8..+8.7 dB).
4. Recheck at the sfp of bar 301: Horns 1-2 should then measure under their bar-300 ff.

This should also raise the delivered LRA, which is now under target (13.6 LU against 14-16), because the soft passages lose a voice that plays at f level (inferred).

### 2. The fff summit arrives as a dip: the last quarter of the bar-335 crescendo is the movement's loudest moment, and bar 336 sits 4-6 dB under it (measured)

**Where.** Bars 333-338 (qn 996-1014), all strings and woodwinds.

**What is wrong.** Master per quarter (0.25 qn windows, c01):

| qn | 1004.25 | 1004.75 | 1005.0 | rest of bar 336 |
|---|---|---|---|---|
| dB | -10.7 | -17.2 | -16.9 | -12.8 at best |

Per 1.5 qn:
- c01: 1003.5 -13.5, 1005 -15.1, 1006.5 -14.2, bar 337's first half -12.0.
- c00: 1003.5 -13.3, 1005 -12.2, so the arrival rose 1.1 dB.

In the delivered mp3, bar 333 got louder (996-999: -16.0 / -14.7 / -13.7, against c00 -17.8 / -17.8 / -15.3). The fff plateau (1005-1014: -12.6..-14.3) is only about 1 dB over bars 333-334. In c00 it was 2-5 dB over them. The short-term LUFS margin over bar 104 is still 3.6 LU, so "loudest" passes, but the arrival does not read as an arrival.

**Causes.**
- **(a)** Violins I's fff downbeat is a `DOWNBOW_STROKE_AT` Sus MAX stroke at v96. That is `REBOW_VEL_BY_CC`'s cap at CC 114+, and the stroke measures -29 dB on the stem. The staccatissimo quarter before it is v119 and measures -18.7 dB.
- **(b)** The summit roles start inside the crescendo or on the arrival:
  - winds [1002,1017,-1.5..-5] and Violas [1002,1016,-3] start on the hairpin's first beat and cancel its 4-7 dB `hpgain`;
  - the stem-fix cuts Violoncellos [1005,1016,-6] and Violins II [1005,1016,-2] land on the downbeat.
- **(c)** Bars 333-334 gained +2..+6 dB in the strings and +3.4 dB in Clarinet 1 against c00. That comes from c01's Sus MAX strokes on the accented half notes at 999 and the new wind staccato row.

**Fix.**
1. Use `ARRIVAL_WEIGHT_AT` (score_to_parts.py, Movement I c06, written for exactly this fff case): `ARRIVAL_WEIGHT_AT = {1005.0: (-2.0, 2.5, 1.0)}` in score_config.py. That holds back 2 dB over the last beat and adds +2.5 dB at the arrival, held 0.5 qn.
2. Raise the strings' fff stroke velocity: either add (124, 112) to `REBOW_VEL_BY_CC`, or `VEL_SET` {1005.0: 112} for Violins I, Violins II, Violas and Violoncellos (it is one stroke). Cap Violins I's v119 quarter at 1004 at about 105 (`VEL_SET`), so the crescendo's last note does not outweigh its target.
3. Move every summit role's start to qn 996 (the ff entry of bar 333) at the same depth, so that no cut falls inside the bar-335 hairpin or on the downbeat:
   - winds [996,1017,x];
   - Violas [996,1016,-3];
   - Violoncellos [996,1016,-6] and Violins II [996,1016,-2] (from the stem fix, now in roles.json).

**Expected effect.**
- My stem simulation of step 3 alone lowered bars 333-334 by 1.7-2.9 dB and left the summit unchanged. The downbeat still came out 0.3 dB under the beat before, so steps 1-2 are needed.
- The master's peak (bar 337, 1008-1012) is not raised. The last beat of bar 335 is lowered, so the delivery limiter should stay at or under c01's 3.1 dB (inferred).

### 3. The sfp at bar 301 keeps the previous crescendo's volume gain through the p, so the dip after the sf is shallow and the bassoons and horns take over the p (measured; code bug read)

**Where.** Bar 301 on (qn 900-909), 13 tracks: Oboe 1, Clarinets 1-2, Bassoons 1-2, Contrabassoon, Horns 1-2, Violins I, Violins II, Violas, Violoncellos, Violas div.

**What is wrong.**
- In parts.json, the vol_db at qn 900.5, at the p just after the sf, is: Bassoon 1/2 and Contrabassoon +7.2 dB, Oboe 1 and Clarinets 1-2 +4.2, strings +3.7, Horns 1-2 +2.0. These gains then keep rising to +10 / +7 / +6 at 909.
- That is the `hpgain` of the bar 299-300 crescendo to ff, chained into the 900-909 crescendo by the HP_CHAIN rule.
- The chain test in `tools/score_to_parts.py` (the `hpi` loop after "c09 (B #1): chain consecutive crescendos") only looks for softer marks strictly between the first arrival and the second start (`b1 + EPS < mq < a2 - EPS`). The sfp/p printed exactly at a2 = 900 is not seen. 900 is the only place in the score where a chained hairpin starts on a softer printed mark (checked on all tracks).

**Measured result.**
- The master falls only from -14.3..-15.0 (bar 300) to -22.6..-24.2 (qn 901-903). The strings themselves fall 15-17 dB (Violins I -26.7 -> -43).
- At qn 901-903 the loudest stems are Bassoon 2 -31.0, Horn 2 -32.1, Horn 1 -33.5, Bassoon 1 -34.7. Bassoon 2's p here is 8 dB above its own f median (-39.3).
- The census finds the 900-909 crescendo flat on Bassoon 2 (0.0 dB) and falling on Horns 1-2 (-3.9 / -6.2 dB).

**Fix.** In that chain test, also end the chain when a printed dynamic at the second hairpin's start (within EPS of a2) is softer than the first arrival. sfp and fp count as their p, the way score_to_parts reads them. Then the first gain releases over HP_REL from the first onset at or after 900, which is under the sfp's own CC11 fall (900.25-900.5), and the new crescendo starts from 0 dB.

S3: the release does cut the bar-300 tail by at most the 2-7 dB it removes. If the actor wants none of that cut in the volume envelope, put the same step into CC7 on these tracks (`CC7_POINTS`, Movement II c30's form) over 900.25-901.0.

Expected result (inferred from the vol_db numbers): the master's p at 901-903 about 4-6 dB lower (about -28), strings and winds back on top of the bassoons, and a crescendo of about 14 dB into bar 304 instead of 9.

### 4. The timpani crescendo rolls do not grow, and the codetta's pp roll is inaudible (measured)

**Where.** Timpani, rolls at bars 101-103, 237-240 and 205-208.

**Bars 101-103 (qn 300-309, p < into f; Dan's priority 5 allows growth here).** The roll measures -35.1 / -40.4 / -36.9 / -35.4 / -37.1 / -34.9 dB per 1.5 qn (c00 also flat). Meanwhile the master rises from -24.8 to -17.3. The CCs rise: CC1 60 -> 88, CC7 28 -> 50. But `TIMP_ROLL_TRIM_DB` (score_config.py) is read from the printed level as the crescendo moves, so the envelope falls from +16.9 to +13.6 dB across the roll (p +18.6 down to f +7.3 in the table) and cancels the crescendo.

**Bars 237-240 (qn 708-718, pp, the codetta's E pedal).** The roll sits at -56..-59 dB, 12-19 dB under the loudest other stem. Mockup-kit LEARNINGS found that rolls 14-23 dB under the orchestra needed +3-4 dB to be heard.

**Bars 205-208 (pp < into f at 209).** The roll grows by 11.6 dB. In its last 1.5 qn it is the loudest stem, +2.8 dB over Horn 1 (-32.7 against -35.5), before the f stroke at 624.

**Fix.**
- Add a generic rule in score_to_parts.py where the roll trim is applied (the `TIMP_ROLL_TRIM_DB` block, around line 3812): under a printed crescendo, hold the trim at its value at the hairpin's start for the rest of the roll. Then the CC1/CC7 growth is heard.
- Plus `LEVEL_SHAPES["Timpani"]` in score_config.py:
  - [(301.0, 0), (308.8, 4.0), (308.95, 0)], aiming for +6..+8 dB of growth, still at least 6 dB under the celli (-24..-28 there);
  - [(707.9, 0), (708.0, 5.0), (717.9, 5.0), (718.0, 0)];
  - [(620.0, 0), (621.0, -3.0), (623.9, -3.0), (624.0, 0)].
- If the trim hold is not enough, MANUAL-GAPS #7 (the recorded "Crs" row, p.123/125) is the alternative for 101-103 (about 2.0 s at quarter 264).

### 5. The pp F-major episode (bars 73-88) is louder than the mp theme and close to the f passages (measured)

**Where.** qn 216-264: Harp, Horns 3-4, Clarinet 1.

**What is wrong.**
- Master momentary median (LUFS): bars 73-88 -29.0, theme A at mp (13-28) -36.8, the ritmo's pp (89-100) -35.6. The f hemiola (45-56) is -21.7.
- Delivered: -23.0 against -26.0 for the theme, so the order of the dynamics is reversed for a listener.
- The harp is printed p espress. with < > hairpins and the loudest stem through most of the episode (-31..-38 dB). It plays velocities up to 98 on its hairpins (14 notes at v80-98 in 216-237; its other p/pp passages stay at v40-64).
- The Hn 3-4 pp chords (-37..-43) come next, and finding 1 covers them.

**Fix.**
- After finding 1, cap the harp's hairpin velocities in this episode at about 78 (`VEL_SET["Harp"]` for the 14 onsets listed in parts.json at v80+, or a cap in the harp hairpin-velocity code). The aim is the episode's master median at or under the theme's.
- If the harp leads, keep it 3-4 dB over Clarinet 1 from bar 81, where Cl 1 p dolce takes the tune.
- My simulation of finding 1 alone lowered this episode by only 1.7 dB, so the harp is the larger part.

### 6. S3 at bar 121 and the loop check (measured; small)

**Bar 121.** The sub. p comes after a caesura, and the master drops 12 dB from bar 120 (better than c00's 9-10 dB). But c01's Horn 2 and Horn 4 roles [360,381,-4] ramp down in the volume envelope at 359.75-360.0, under the ring of their ff. Start the role at 360.05 with its ramp after the p note's onset, or move the -4 dB into CC7 (`CC7_POINTS`).

**Bar 277.** The sub. p falls 7 dB (825: -30.9 -> 828: -37.7) with no volume-envelope step (fine). But the master is back at -31 by bar 278, because Flute 1's espress. boost (+2 dB vol, CC11 54-57) puts its p at -38.5..-40.5 dB, its mf level. That is acceptable for an espress. lead.

**Loop pulsing (BRIEF item 8).** No held sample is longer than about 6 s at this tempo except Hn 1's last G sharp (11.7 s; stem 100-300 Hz and centroid autocorrelation at 3.95 s: -0.06 / -0.12). The stems over the re-bowed spans (Violins I 1089-1128, Horns 3-4 456-504) show autocorrelation -0.19..+0.13. The master's +0.25..+0.53 there follows the harp's and pizzicato's bar pattern (5 bars at quarter 228 = 3.95 s), not a sample loop. Nothing to fix.

**Do not touch:**
- c01's re-bow fills (Violins I dips -1.1..-2.3 dB);
- the hall settings (fx 0.095, low cut 160) and the tutti cut-off drops (13.9-16.2 dB);
- the sub. p at bar 121 as a CC11 fall (12 dB, no tail cut except the horn roles above);
- the summit as the loudest short-term moment (keep the bar 337 peak where it is: fix the approach, not the peak);
- the codetta's and coda's fades (bars 361-364 fall 9 dB into Hn 1's G sharp);
- the accelerando crescendo (bars 241-251, +5 dB);
- the trio's arc (dolce -36, f at 197 -25.7, ff at 218 -23.3).
