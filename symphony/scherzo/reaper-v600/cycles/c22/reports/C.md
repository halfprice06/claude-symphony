# Cycle 22, critic C: dynamics over time (lens C2), on the c21 render and its delivered mp3

Sources: `cycles/c21/render/` (master, 31 stems, returns), `cycles/c21/scherzo-mockup-c21.mp3`, `cycles/c21/build_render/` (parts.json, roles.json, mix.json as rendered), `build/mockup-events.tsv`, `build/score_config.py`, `tools/deliver_master.py`, `cycles/c21/CHANGES.md`, c18 stems for comparison. Loudness: EBU momentary (M, 0.4 s) and short-term (S, 3 s), K-weighted, centred, on the c21 tempo map; "mean" is the energy mean of M over the span, "max" its maximum. Stem levels are plain RMS dB. The delivery simulations ran `tools/deliver_master.py` unchanged on `cycles/c21/render/00_Master.wav` with its environment overrides and, where stated, extra `ride_trims` in a scratch copy of parts.json; the baseline run reproduces the delivered file exactly (-14.1 LUFS, LRA 12.1, p10 -21.5, limiter 5.7 dB). "Measured" = a number from the render, the data or a simulation; "inferred" = reasoned, not tested.

## Manual notes

MANUAL-READING.md has no row for cycle 22, so I skipped the page reading. I used MANUAL-GAPS.md:

| item (MANUAL-GAPS) | manual page | where it applies here | does the render follow it? |
|---|---|---|---|
| #7 recorded crescendo rolls | p.123, p.125 | rolls 101-103, 205-208, 301-303 | Not used, and not needed (measured): the CC1 rolls grow -50.8 -> -28.7 dB (300-307.5), -51 -> -36 (612-624), -42 -> -34 (906-908), staying 9-11 dB under the master at their tops. |
| #4 brass and clarinet dynamics on CC1 | p.101 | brass crescendos into 996 and 1005 | In use (measured): horns, trumpets and trombones rise +3.4 to +8.1 dB from 993-995 to 996-998 (CC1 68 -> 81, 91 -> 106). |
| #6 timpani hard sticks | p.123-126 | bars 1-340 | Still pending; it does not affect dynamics (inferred). |

## Checks the cycle note asked for (measured)

- **f against ff on the mp3.** Passage means: f 41-44 -11.2, 129-131 -9.6, 197-200 -11.1, 273-276 -10.7, 285-288 -10.5 (average -10.6); ff 72 -8.5, 104 -8.1, 105-120 -9.6, 300 -8.6, 304 -8.6, 305-320 -10.0 (average -8.9). So f to ff is 1.7 LU on the mp3, against 5.5-6 dB on the master. Finale c24's suggestion (top ride 6 dB under p95, quiet-lift ratio 2.1), simulated on the c21 master: gap 2.5 LU, summit lead 0.38 LU (worse), limiter 5.7 dB, LRA 12.2, p10 -21.6. On its own it does not fix the top (finding 1).
- **The summit's 0.4 LU lead.** Loudest bars of the mp3 by M max: 338 -7.1, 339 -7.2, 336 -7.2, 337 -7.3; then 318 -7.5, 300 -7.8, 104 -7.8, 218 -7.9, 53 -7.9, 335 -7.9, 72 -8.0. On the master the summit leads 104 by 1.4 dB, 300/304 by 2.1, 318 by 3.5, and 218 and 53 by 5.5 and 4.8. The delivery gain per bar (mp3 minus master M mean) is +4.5 at the summit, +5.6 at 104, +6.0 at 300, +8.0 at 318, +9.3 at 218, +9.4 at 53 and +19 in the soft passages.
- **Quiet passages (Dan's AirPods note).** mp3 means: ppp intro -18.8, theme A p -17.7, counterstatement p -21.5, fugato p -21.0, ritmo pp -19.4, link ppp -19.2, trio dolce -17.3, codetta -18.2, stretto pp -23.8, Meno pp -20.0, close ppp -20.3. p10 short-term -21.7, which meets the -23 floor.
- **S3.** Both sub. p's keep the hall. At 360 R Strings falls -35.0 / -41.1 / -43.2 / -47.0 / -48.7 / -51.9 dB at -0.6 / -0.3 / -0.1 / 0 / +0.1 / +0.2 s from the bar line, with no step; the master falls 11 dB from the tutti to the sub. p. At 828 the fall is smooth too.
- **Timpani rolls.** They grow only under the printed crescendos (above). The unprinted rolls settle: 129-130 and 285-286 start at -38, settle to -45, then the stroke; 237-240 stay at -50 to -56. The roll into 909 dips 4 dB at its ff stroke (-34.2 -> -38.3), then -32.6. That is small, so I have not ranked it.
- **Loop pulsing** (band level and centroid, detrended, autocorrelation at 3.95 s): Violins I G sharp 1089-1122 +0.03 / +0.05; the master over the last note -0.02 / -0.02; Horn 1 1101-1122 +0.04 / -0.01; Violins I bars 1-8 +0.18 / +0.30; Violins II harmonic +0.09 / +0.24; celli 605-624 -0.14 / +0.02. Nothing pulses audibly.
- **Hairpin audit** (stem, first note's body against the arrival note's, hairpins of 2 qn or more): 257 crescendos, median +7.3 dB, 43 under +1 (winds 27 of 116). 90 decrescendos, median -4.4, 20 not falling. The worst cases that are not artefacts of the sf at 900 are findings 2 and 3.
- **Arc against the print, master:** in order except findings 2-4. ppp intro -40.5; theme A p -35.6; f at 41 -23.1; second idea -20.8, with ff at 53; F major pp -33.1; ritmo -32.5; f hemiola -15.9; ff tutti -17.7; sub. p -28.5; link ppp -36.7; trio dolce -34.1, f (197) -23.5, ff (209-224) -23.8 with the A6 at 218 the trio's loudest (-17.0 max); codetta -34.4 to -38.5; accelerando -35.3; reprise sub. p -29.1; sfp 301-303 -17.5; ff 304 -14.4; build -18.1; summit -12.6; Meno pp -35.1; fade 361-364 -36.4 / -39.1 / -43.6 / -44.4; close -40.3.

## Findings, ranked by what a listener would gain

### 1. On the delivered mp3 every loud passage sits within about 1 LU of the fff summit, and the limiter takes 5.7 dB at the summit (BRIEF: at most about 3). The trio's ff and the second idea's ff come out as loud as the full-orchestra tuttis (measured, simulated)

**Where.** The summit, bars 336-339 (qn 1005-1017), against bar 318, bar 300, bars 104-120, bar 218 (the trio's A6, qn 651, strings and Clarinet 1 only) and bar 53 (the second idea's ff).

**What is wrong.**
- The mp3 maxima are listed above: the summit -7.1 and seven bars at -7.5 to -8.0.
- The summit's M is pinned by the limiter. In all ten delivery variants I ran, the summit's M max stayed between -7.0 and -7.4.
- The pre-limiter peaks are at qn 1011.4, 1015.0, 1006.6 and 1009.0, at +2.4 to +4.3 dBFS against a -1.4 dBFS ceiling. They come from the summed strings with the hall: the master peaks at -3.6 dBFS while the loudest stems there peak at -10 to -12 (Violins I, Violins II, violas).
- So raising the summit in the delivery cannot help. Only lowering the limiter's share (the crest), or the bars that compete with the summit, can.
- The 2:1 top ride starts 10 dB under p95 (master S -27.1). That puts every f, ff and fff passage above its threshold and halves the differences between them.

**Simulations on the c21 master** (all -14.0/-14.1 LUFS, TP -1.2 to -1.4 dBTP):

| variant | limiter at the summit | summit lead (M max) | f -> ff (mean) | bar 218 / bar 53 | p10 S | LRA |
|---|---|---|---|---|---|---|
| delivered (c21) | 5.7 | 0.44 over 318 | 1.7 | -7.9 / -7.9 | -21.7 | 12.1 |
| top 6 dB under p95, lift 2.1 (finale c24) | 5.7 | 0.38 | 2.5 | -8.1 / -7.9 | -21.6 | 12.2 |
| top 6 dB under p95, top ratio 1.5, lift 2.1 | 5.7 | 0.29 | 2.7 | -8.2 / -7.9 | -21.7 | 12.5 |
| peak compressor -9 dB 3:1 only | 3.0 | 0.81 | 1.6 | -8.6 / -8.3 | -20.6 | 10.7 |
| **peak compressor -9 dB 3:1, top 6 dB under p95, lift 2.1** | **3.0** | **0.72** | **2.2** | -8.7 / -8.3 | **-20.5** | 11.0 |
| the same + the three ride rows below | 3.0 | 0.72 over 318 | 2.2 | **-9.5 / -8.7** | -20.3 | 10.6 |

**Fix (delivery only; the stems and the master keep their levels).**
- `tools/deliver_master.py`:
  - `PEAK_COMP` `acompressor=threshold=-9dB:ratio=3:attack=2:release=60:knee=4:makeup=1` (was -6 dB 2:1);
  - `TOP_ABOVE` -6.0 (was -10);
  - `RATIO` (the quiet lift) 2.1 (was 1.6).
- `build/score_config.py` `RIDE_TRIMS`, add:
  - `[(154.0, 0.0), (156.0, -1.5), (164.0, -1.5), (166.0, 0.0)]` (bar 53);
  - `[(645.0, 0.0), (647.0, -1.5), (656.0, -1.5), (659.0, 0.0)]` (the trio's A6, on top of the -2 row there);
  - the counterstatement row of finding 4.
- Result (last row of the table): the limiter meets BRIEF item 6 (5.7 -> 3.0 dB); f -> ff +0.5 LU; the trio's A6 2.1 LU under the summit instead of 0.8; soft passages +0.8 to +1.5 LU (Dan's AirPods note).
- The cost is LRA 10.6, against the shared target of about 12. I would accept it for the limiter, the order and the soft passages, but the coordinator should decide (inferred).
- The summit's lead stays under 1 LU until the master itself has more fff than ff. That is finding 2.
- After the delivery change, check the 2-5 kHz front of the timpani strokes and the string accents on the mp3. A -9 dB threshold acts on crests (inferred).

### 2. At the coda's ff (bar 333, qn 996) twelve tracks step down at the arrival, and the woodwinds and celli do not grow from ff to fff into the summit (measured)

**Where.** qn 993-1010. Tracks: Violoncellos, Clarinet 1, Clarinet 2, Bassoon 1, Bassoon 2, cor anglais, Oboe 1, Oboe 2, Flute 1, Flute 2, Contrabassoon, Horn 1.

**What is wrong.**
- `roles.json` has summit cuts that all start at 996: Violoncellos [996, 1016, -6], Clarinet 2 -5, Bassoon 1 -4.7, Flute 1 / Flute 2 / Oboe 2 -4, cor anglais / Contrabassoon / Horn 1 -3, Clarinet 1 -2, Bassoon 2 -1.5, Oboe 1 -1. They date from c01-c03, when the summit's Sus MAX strokes were 8-11 dB hot.
- At the same point the crescendo gains of 984-996 are released. Celli vol_db goes +2.9 -> -3.0 in 0.13 qn (27 ms) at 995.75-995.88. That is in the rest before 996, so it also cuts that note's hall tail (S3).
- Stems, 993.0-995.4 against 996.0-998.4 (the printed f, or the end of the crescendo, to ff): celli **-6.8 dB**, Clarinet 1 -3.2, Bassoon 1 -1.8, cor anglais -1.2, violas 0.0. Against these, the strings and brass that have no cut rise +5 to +10.6.
- From the ff (996-1002) to the fff (1005-1010) the woodwinds that should grow do not: Oboe 1 0.0, Clarinet 1 -0.6, Bassoon 2 -0.1, Contrabassoon -2.5.
- Celli per printed dynamic (metrics): ff -31.0, fff -32.0. At the summit the celli are the weakest string section (-32.4 against -26.0 / -25.9 / -27.9).
- The master's ff plateau 996-1002 is flat at -20.1 to -20.8 dB RMS, then the summit only reaches -18.2 / -16.4. On the master the summit leads bars 333-335 by 2.0 dB, and 104 by 1.4.

**Fix (`build/roles.json`, slow role rows; no per-note moves).**
- Move every 996 start to 1004.75, the start the Violins II and violas rows already use, so that the ff of 996-1002 sounds at the printed level.
- Halve the cuts at the summit:
  - Violoncellos [1004.75, 1016, -3];
  - Clarinet 2 -2.5; Bassoon 1 -2.5;
  - Flute 1, Flute 2, Oboe 2 -2;
  - cor anglais, Contrabassoon, Horn 1 -1.5;
  - Clarinet 1 -1; Bassoon 2 -0.5; Oboe 1 0 (delete the row).
- The c01 reason for the cuts (strokes 8-11 dB hot on Sus MAX) no longer holds as measured: today the celli are 4-6 dB under the upper strings at the summit.
- In `tools/score_to_parts.py`, the crescendo gain on the celli (hpgain [984, 996, 3]) should release after the ff note, not in the rest before it (HP_HOLD_CAP is already 4 qn; the release here comes from the role row's edge at 996).
- Targets:
  - every listed track rises at least +2 dB from 993-995 to 996-998, and at least +1.5 dB from 996-1002 to 1005-1010 (woodwinds) or holds (brass, printed f/ff);
  - celli fff over celli ff;
  - master summit at least 3 dB over 996-1002 and at least 2 dB over bar 104 (now 2.0 / 1.4);
  - on the mp3 with finding 1's chain, check the limiter stays at 3.5 dB or less (inferred: about +0.3 dB more limiting).

### 3. Flute 1's crescendos into both ff tuttis (qn 300-310 and 900-910) stay at mp, then step +46 CC11 units at the ff downbeat, and two balance rows cut Clarinet 1 inside the bar-301 crescendo (measured)

**Where.**
- Flute 1, bars 101-104 into 105 (qn 300-312) and bars 301-304 into 305 (qn 900-912).
- Clarinet 1, bars 302-304 (qn 905.75-912).
- The same pattern on the chained crescendos of the bassoons and contrabassoon into bars 72 and 300 (210-213, 894-897).

**What is wrong.**
- Flute 1's part prints the crescendo to 910 and its ff on the next downbeat, 912 (the same at 310 / 312).
- With no mark at the hairpin end, `dyn_curve` climbs only 46 -> 68 (at 900-909.6), then jumps to 114 at 912. CC11 at 909: 68 (Flute 2, whose ff falls at the hairpin end, reaches 114).
- Flute 1 stem per quarter 900-912: -33.2 -33.7 -35.0 -36.7 -41.4 -36.9 -38.7 -41.8 **-44.7** -40.9 -40.7 -39.0, then **-29.5** at 912. It falls 6.2 dB through a printed crescendo, then steps up 11 dB.
- At 300-312: -39.9 ... -43.0 ... -38.3 / -37.7 / -36.1, then **-26.1** at 312 (+10 dB step).
- Flute 1 is the top of the woodwind chord in both tuttis. A scan of every crescendo of 1.5 qn or more found the same "end short of the next mark" only here and in the chained bassoon / contrabassoon crescendos: curve held at 88 through 210-213 and 894-897, then 114. Bassoon 1's stem falls 2.7 dB from 210 to 213 (c18 #1's chain, still open).
- Clarinet 1 has the role row [906, 912, -5] inside the printed crescendo. Its slow class steps +2.5 -> -2.4 dB at 905.75-905.85. The stem reads 904 -30.6, 906 -35.9, 909 -34.5, 910 -38.8, below its own sf at 900 (-27.2).

**Fix.**
- `tools/score_to_parts.py`, where a crescendo's target dynamic is chosen: add a generic option `HP_TARGET_LOOKAHEAD_QN` (default 0 = off; scherzo 2.5). When a crescendo has no printed dynamic at its end and the track's next printed dynamic lies within that many qn after it, the crescendo takes that dynamic as its target. The curve reaches it at the hairpin end and holds to the mark.
- Apply the same rule to the second hairpin of a chain (210-213, 894-897), so that its curve rises 88 -> 114 across the hairpin instead of stepping at 213 / 897.
- Clarinet 1: move the role row to start at 900.5, after the sf, so the -5 balance holds from the p and the crescendo keeps its shape. Or ramp it in over the hairpin (start 900.5 at 0, -5 at 903).
- Targets:
  - Flute 1 rising at least +6 dB from 901.5-902.5 to 909-910.5, and from 300.5-301.5 to 309-310.5;
  - its step at 912 / 312 at most 3 dB;
  - Clarinet 1 rising monotonically (quarter medians) 901.5-910;
  - Bassoon 1 / 2 rising at least +2 dB from 210 to 213 and from 894 to 897.

### 4. On the mp3 the counterstatement (bars 29-36, p) is the softest p passage, 2.7 LU under the ppp introduction. Horn 1's p peak in the horn call is as loud as the first f (measured, simulated)

**Where.** Bars 29-36 (qn 84-108): Flute 1 and Oboe 1 leggiero with the strings. Bars 3-5 (qn 9-12): Horn 1's p arrival.

**What is wrong.**
- mp3 means: counterstatement -21.5 against theme A (p) -17.7, ppp intro -18.8, Meno pp -20.0 and link ppp -19.2.
- The delivery gave the counterstatement +15.9 dB and its neighbours +19. The 5 s lift dips there because the momentary cap (MOM_CAP_ABOVE 3) reads the wind calls' accented quarters, and the crescendo of 37-40 lies inside the lift's smoothing.
- The master is in order (counterstatement -37.4, intro -40.5); only the delivery inverts it.
- `deliver_master.py --fit-flat 84 108` gives a steady lift of 4.66 dB against the ride's 3.64 -> 2.11.
- Horn 1's horn call peaks at M -10.6 on the mp3 (qn 11-12, printed p) against -10.3 for the f at bar 41. On the master it is 7 dB under. The quiet lift's 19 dB applies to a solo line as fully as to a soft tutti. I do not propose to lower it, given Dan's AirPods note. I record it as the place where p and f meet on the delivered file.

**Fix.** `build/score_config.py` `RIDE_TRIMS`, add `[(83.5, 0.0), (84.5, 1.5), (104.0, 2.0), (108.0, 2.0), (116.0, 0.0)]`. This is not the fit's row, which steps 2.55 dB down at 108: this one returns to 0 across the printed crescendo of 37-40. Simulated with finding 1's chain: counterstatement -21.5 -> -18.7. The crescendo into 41 still rises 7 LU on the mp3 (inferred from the -13.2 -> -11.2 passage means, less the 2 dB row).

### 5. The second idea in E minor after the sub. p and the trio's middle part are in order, but the fugato still barely grows: bars 57-66 within 3.4 dB, bar 61 the softest (measured; c18 #3, partly fixed)

**Where.** Bars 57-66 (qn 168-198; celli p, violas p at 180, Violins II p at 192) and 289-294 (qn 864-882).

**What is wrong.**
- Master per bar 57-66: -42.3 -41.2 -42.6 -41.7 | **-45.5** -39.1 -41.1 -40.9 | -41.6 -36.6. Averages: 57-60 -42.0, 61-64 -41.7, 65-66 -39.1.
- The violas' entry bar 61 is 3.5 dB under the bar before. Stem: violas -47.2 against the celli's -41.7 in bar 58.
- Reprise 289-294: -43.3 -44.0 -42.8 -41.7 **-45.7** -38.5. Again the entry bar (293) is the low point.
- The c18 targets were +1 to +1.5 dB per entry. Entry 2 adds +0.3, entry 3 +2.6.

**Fix.**
- CC11 only, on the violas' first two bars of each entry: `CC11_ADD_SPANS` Violas (180.0, 183.0, +8) and (876.0, 879.0, +8). The head's staccatos at CC11 41-50 sit in the steep part of the strings' range (c18 measured about 0.7 dB per unit under 100).
- If the staccato row's soft layer caps it, raise the violas' entry velocities one layer at 180-183 / 876-879 (`VEL_SET`) instead.
- Target: bar 61 and bar 293 not under the bar before; bars 61-64 at least 1 dB over 57-60.

### 6. Smaller dynamic-order faults per track (measured)

- **Cor anglais:** per-bar medians mp -37.4, mf -38.8, f -40.4 (mp over f by 3 dB).
- **Horn 2:** mf -40.4, f -43.5. **Horn 4:** p -46.3, mp -48.7.
- **Violas div:** f -38.0 against the Violas track's -39.4, while its mp is -55.7.
- These per-bar figures mix rows and textures. Before any change, check the cor anglais' f notes, which are mainly the tutti hemiola 300-309 and 897-910 at CC1 45 (c20 set CC1 45 on the hemiola notes): with CC1 45 the f notes lose the vibrato layer and about 2-3 dB (inferred, Opus CC1 layer crossfade).
- **Fix to test:** cor anglais CC1 45 only on the hemiola's mp/mf notes (c20's swing problem), back to the resting CC1 on the f / ff notes (`CC1_SPANS` or the c20 switch in score_config.py).
- **Target:** each adjacent printed step on held notes at least +1 dB.

## Do not touch

- S3 at both sub. p's (CC11 falls, the hall decaying under them).
- The timpani rolls: they grow only under printed crescendos and settle elsewhere.
- No loop pulsing on any held note (keep the re-bows and HELD_DOUBLE).
- The G.P. ride row.
- The stretto role rows of c21.
- The trio's arc (dolce, f at 197, the A6 at 218 as its loudest on the master) and the codetta's fade.
- The brass crescendos on CC1.
- The held chord's fade 361-364 into Horn 1's G sharp and the ppp close.
- Bar 23's Sus MAX pairs: not touched by any fix here.
