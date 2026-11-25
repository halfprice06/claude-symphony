# Critic C, cycle 61: holistic (render c60, delivered at -14 LUFS, against c56, c53, c0 and a recording; score v621)

Scripts and outputs: `cycles/c61/critic_scripts/C/` (`lib61.py`; `bars61.py` per-bar momentary loudness, master and mp3; `xbars.py` per-bar comparison c53 / c56 / c60; `cresc61.py` every printed crescendo on the delivered file; `limgr.py` limiter gain reduction per bar, aligned for the limiter's 240-sample look-ahead; `mp3cmp61.py`, `mascmp61.py` spectrum, width and moment-to-moment level against Dvořák 9/i; `stemdiff.py`, `trace.py`, `pitchrow.py` stem checks; `deliver_copy.py` / `deliver_copy2.py`, copies of `tools/deliver_master.py` with a gain dump and env overrides for the top ride; `mkvar.py` and `var/v1`-`v8` the delivery variants, each an mp3 and a log). `out/c60_redeliver.mp3` reproduces the shipped c60 mp3 exactly (I -14.0, LRA 11.2, limiter 6.7 dB); `out/c56_at14.mp3` is the c56 master through today's delivery, so c56 and c60 can be compared at the same delivered level. Nobody listened. Figures are measured unless marked inferred. Loudness is EBU momentary (0.4 s) or short-term (3 s) from ffmpeg, 10 Hz, centred.

## Manual notes (pages chosen for this lens; MANUAL-GAPS.md and DIGEST.md read)

| Manual (2021 PDF page) | What it says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| p.109 | Woodwind sustains play all 3 dynamic layers at once; the controller crossfades them (Play-era text says Mod Wheel; DIGEST: CC11 on Opus woodwinds). | Oboe 1, bar 145-146 (finding 3): the soft layer at CC11 54 on E5 plays 7-10 dB over E-flat 5 / F5 at the same CC11. | The layer is followed, but the per-pitch region gain that corrects E5 is filtered to the `f` layer only, so the p E5 is uncorrected. |
| p.112 | Woodwind legato: slur only with no gap and within an octave; Leg Slur patches start 3 sustain samples plus the slur sample. | Oboe 1 578-584 G4 -> E5 (a sixth, slurred) | Followed; the transition is within an octave. The level jump is the E5 sample layer, not the slur. |
| p.208 | SSL Transient Shaper adds or (Invert) softens attacks; "it can increase the peak level of a signal significantly". | The ff stabs of bars 40-41, 82-83 and 170 take 5-7 dB of delivery limiting (finding 1). | No transient shaping in use. Not proposed: the stabs' attacks are what the limiter takes; adding attack would add limiting. |
| DIGEST, CC11 row (p.63-64, p.151) | CC11 shapes loudness over time and crossfades layers. | Second-theme lanes (finding 4) | Followed; sizes below use the track's own slope. |
| MANUAL-GAPS #8 | Legato velocity 50-75 for longer slides on cantabile lines; never tried. | Second theme, Oboe 1 145-146 | Still open. Not proposed this cycle. |

EW-TEMPLATE-PLAN sections this lens touched: section 3 master EQ is applied in a changed form (the template's +0.8 dB shelf at 8 kHz was replaced in c53 by a -1.0 / now -1.3 dB shelf at 3 kHz; the delivered 6-14 kHz share is 2.2 dB under the recording, see finding 6); sections 6-8 ("long notes keep moving") were measured in c59 and c60 and are not repeated here.

## How c60 compares with c56, c53 and c0 (delivered files)

Measured on the mp3s (`mp3cmp61.py`; band shares in dB of 40 Hz-14 kHz; "level change" is the SD of the change between neighbouring 0.4 s frames in the louder half):

| | c0 (v221) | c53 | c56 | c56 through today's delivery | c60 | Dvořák 9/i (lossy) |
|---|---|---|---|---|---|---|
| 2-6 kHz share | -12.2 | -10.0 | -9.9 | -10.1 | -10.2 | -10.4 |
| 6-14 kHz share | -30.9 | -30.2 | -30.2 | -30.8 | -30.8 | -28.6 |
| centroid of loud frames, Hz | 722 | 861 | 840 | 834 | 845 | 835 |
| LR correlation 2-8 kHz | 0.49 | 0.42 | 0.42 | 0.41 | 0.43 | 0.66 |
| 3 s level p10-p95, dB | 17.1 | 14.1 | 13.7 | 11.1 | 10.4 | 23.8 |
| level change, dB | 1.94 | 1.74 | 1.76 | 1.57 | 1.59 | 2.64 |

The tone and width have matched the recording since c53 and still do. At the same delivery, c60 and c56 have the same moment-to-moment movement (1.59 / 1.57). On the masters it is 2.05 (c60) against 2.19 (c56), so removing the per-note shaping cost 0.14 dB there, and the -14 delivery takes another 0.46 (ride 0.30, limiter 0.17: pre-limiter file 1.75). The 3 s spread fell from 13.7 to 10.4 dB, almost all of it the -14 target (c56 through today's delivery 11.1).

Per bar, c60 against c56 at the same delivery (`xbars.py`, each bar's mean loudness relative to the file's mean): down 2-3.6 dB in the second theme (bars 47, 49, 50, 147, 148; celli and Horn 1 stems -3 to -5 dB, accompaniment unchanged) and bar 144 (-2.5, Violins I -3.5); up 6.2 dB in bar 146 (Oboe 1 +10.9, finding 3), +2.8 / +3.4 in bars 86-87 (the fugato rows deleted, intended), +2 to +4.5 in the coda 176-182 (the ride trims; what Dan asked for). Against c53 the same pattern, plus the fugato and the coda louder by 5-8 dB.

The climaxes over the file's mean (momentary max per bar, LU): c53 122 +9.9, 160 +9.8, 170 +9.0, 26 +8.8 (delivered at -19.8, wrong order); c56 through today's delivery 160 +7.2, 122 +7.1, 170 +6.8, 26 +6.1 (printed order); c60 160 +7.1, 170 +6.6, 26 +6.4, 122 +6.4 (wrong order). The c60 ff trims took 0.7 dB off bar 122 at delivery and 0.2 off bar 170.

## Findings, ranked by what a listener would gain

### 1. At -14 LUFS the top of the movement is flat and in the wrong order: bar 170's ff chord is the second-loudest moment, and seven bars lie within 1.2 LU (measured; fix simulated)

**Where.** Bars 26, 82-83, 122, 160-161, 170 on the delivered mp3.

**What is wrong.** Loudest 0.4 s per bar on `mvt1-mockup-c60.mp3` (LUFS momentary): 160 -7.1, 170 -7.7, 26 -7.9, 122 -7.9, 161 -7.9, 83 -8.0, 82 -8.1. The printed order is 160 (fff) > 122 > 26 > 170. On the master the gaps are healthy (160 -10.0, 122 -11.5, 26 -13.0, 170 -13.6: 3.6 dB from summit to bar 170); the delivery closes them to 0.6 dB. The gain the delivery adds at each bar's loudest moment: 160 +2.9, 122 +3.6, 26 +5.2, 170 +6.0, 82 +8.4. Two stages do it. The top ride (`TOP_ABOVE, TOP_RATIO = -10.0, 3.0`: 3:1 on everything above 10 dB under the 95th percentile, 3 s smoothing) pulls 160 and 122 down 4-5 dB and bar 170 only 2.0-2.2 dB (ride at 378 s, `gdb_c60.npy`), because bar 170 is one half-note chord before a fermata rest and its 3 s loudness is low. Then the limiter takes the chord's peaks (bar 170: 5.3 dB, more than 3 dB over 13 % of the bar; bar 160 3.5 dB; `limgr.py`). Bar 170 is not lifted by the quiet-passage ride or by the cello-solo trim (that row starts at qn 680, after the chord).

**What I tried** (`var/`, each the full delivery with the loudness loop; order is by loudest 0.4 s):

| variant | 26 | 122 | 160 | 170 | 169 -> 170 rise | order | LRA | limiter |
|---|---|---|---|---|---|---|---|---|
| c60 as shipped | -7.9 | -7.9 | -7.1 | -7.7 | +1.6 | 160 170 26 122 | 11.2 | 6.7 |
| v1 row -2.5 dB on the chord | -7.9 | -7.9 | -7.1 | -8.3 | +1.2 | 160 26 122 170 | 11.2 | 6.7 |
| v2 row -3.5 dB | -7.9 | -7.9 | -7.1 | -8.8 | +0.6 | 160 26 122 170 | 11.2 | 6.7 |
| v5 top ride 2:1, no row | -7.8 | -7.6 | -6.9 | -7.7 | +1.6 | 160 122 170 26 | 11.8 | 6.3 |
| **v4 top ride 2:1 + row -2.5** | -7.8 | -7.6 | -6.9 | -8.3 | +1.1 | **160 122 26 170** | 11.7 | 6.4 |
| v8 = v7 + row -2 on bars 82-83 | -7.8 | -7.6 | -6.9 | -8.3 | +1.1 | 160 122 26 170 | 11.7 | 5.3 |

A row on the chord alone gains only a quarter of its size after the limiter (-2.5 dB in, -0.6 out) and cannot put 122 over 26. The 2:1 top ride (the finale's c21 value) restores 122 over 26 and with the chord row gives the printed order. v8 is a negative result: a row on the bars 82-83 stabs moves the limiting onto bars 122 and 160-161 (more than 1 dB over 79 % of those bars) and starts at the ff arrival of bar 82, which halves that crescendo (80-82: master +5.3, delivered +2.2). Do not use it.

**Fix.**
- `tools/deliver_master.py`, the -14 line: `TOP_ABOVE, TOP_RATIO = -10.0, 3.0` -> `-10.0, 2.0`.
- `build/score_config.py`, append to `RIDE_TRIMS` (score qn, dB): `[(675.8, 0.0), (676.0, -2.5), (679.0, -2.5), (679.9, 0.0)]`. The row comes in on the chord's attack and goes out in the hall tail under the fermata (the tail is 30-40 dB down by 379.5 s), before the cello-solo row at 679.95.
- Expected (simulated, v4 / v7): 160 -6.9 > 122 -7.6 > 26 -7.8 > 170 -8.3; margins 0.7, 0.2, 0.5 LU; I -14.0, LRA 11.2 -> 11.7, true peak -1.2, limiter 6.7 -> 6.4 dB; short-term p10 -21.5 -> -22.0 (the quiet passages 0.5 dB softer: the cost). The crescendo into bar 170 shrinks from +1.6 to +1.1 dB at delivery (master +2.9).
- Check after the render: the same table on the delivered file; the margin 122 over 26 is only 0.2 LU, so if c61's mix changes move bar 122 or 26, re-run `varcmp.py`.

### 2. The delivery inverts one crescendo and halves seven, among them the development's six-bar crescendo to ff and the run-up to the summit (measured; fix simulated)

**Where.** Every printed crescendo carried by two or more parts, 1.5 qn or longer (54 spans, `cresc61.py`); level rise = mean momentary loudness over the last quarter of the span and the arrival's first half-beat, minus the first quarter.

**What is wrong.** Median rise master +4.5 dB, delivered +3.6. Inverted by the delivery: bars 95-97 (qn 376-387 into ff; ten parts start a crescendo at 376, two of them run to 387): master +2.2, delivered -0.4. Rise halved or worse: bars 111-117 (qn 440-464, 17 parts, p to ff) master +13.9, delivered +5.7; 113-117 +7.9 -> +3.4; 156-158 (qn 620-628, 11 parts, into the ff before the summit) +6.5 -> +2.4; 40-41 (qn 156-160, low brass and timpani) +4.7 -> +2.1. The quiet-passage lift (5 s smoothing) raises the soft start of a long crescendo by 5-8 dB and the top ride lowers its arrival; over 10 s the two meet halfway. Seven spans have a master rise under 1 dB (bars 57, 99, 103, 116-117, 148, 151, and bars 7-8, where the span runs into a diminuendo and my window includes it): those are mix questions, not delivery, and are left to critics A and B.

**Fix.**
- With finding 1's 2:1 top ride the inversion at 95-97 is gone and the halved spans fall from 7 to 5 (simulated v4).
- `RIDE_TRIMS`, two rows that hold the lift back at the soft start of the two long crescendos and give it back during the crescendo (no step at the arrival; the `--fit-flat` rows printed for these spans end in a 2.3 dB drop on the ff arrival and must not be used): `[(436.0, 0.0), (440.0, -3.0), (448.0, -2.0), (456.0, 0.0)]` and `[(616.0, 0.0), (620.0, -2.0), (624.0, -1.0), (627.0, 0.0)]`.
- Expected (simulated, v7 = 2:1 + the bar-170 row + these two rows): bars 111 -> 117 delivered rise 5.5 -> 9.4 dB (bar means -19.6 -> -10.2); 156 -> 160 7.6 -> 9.5 dB; 0 inversions, 1 halved (bars 40-41, +4.7 -> +2.2, a 4-qn crescendo the ride cannot follow without a fitted row); bars 110-112 2.5 dB softer than now (p and mp, still about 5 LU over the file's p10). Climax order as in finding 1.

### 3. Bars 145-146: the p dolce oboe link is now the loudest line from bar 140 to the second theme, 11 dB over c56 (measured)

**Where.** Oboe 1, qn 578-584 (G4, slurred to a held E5 with a printed diminuendo, then D5; p dolce), over celli pp.

**What is wrong.** Oboe 1 stem per half-beat, c56 / c60 (dB): the E5 at 579.5-581 -43 / -45 / -46 against **-33 / -32 / -32**; the bar-146 master rose 5.3 dB (delivered +6.2 against c56 at the same delivery: bar 146 is now 1.2 dB under the mf entry of the second theme at bar 147). CC11 there is 53-60. By pitch on Leg Slur MAX (`pitchrow.py`, body level, CC11 at the onset): E5 at 54 -33.2 and at 107 -33.9, against E-flat 5 at 72-86 -39.7 to -43.7 and F5 at 63-94 -39.5 to -44.2. So E5 plays 7-10 dB over its neighbours at a soft CC11. `build/mix.json` Oboe 1 `region_gain_db` has `{"rows": ["Leg Slur MAX"], "pitch_db": {"76": -5, ...}, "dyn": ["f"]}`: the E5 cut acts on the f layer only, while `soft_trim_db.p` +9.5 lifts the soft layer. c56 hid it with a -5 dB per-note shape (LEVEL_SHAPES at 579.2-581.7), dropped with the other per-note rows.

**Fix.** `build/mix.json` Oboe 1 `region_gain_db`: add `{"rows": ["Leg Slur MAX"], "pitch_db": {"76": -8.0}, "dyn": ["p", "pp", "mp"]}` (first check which dynamic group sounds at CC11 54 on key 76 in the Opus state; c59 found a dyn filter that did not act on Horn 4). Expected: 579.5-581 about -41 dB, 2-3 dB over the G4 before it, the diminuendo audible; bar 146 back within 1.5 dB of c56. The E5 at 395.9 (CC11 107, -33.9) is in the same group if the filter takes the mid layer; check it after.

### 4. The second theme lost 3-5 dB of melody against its accompaniment (measured; sizes inferred from the track slopes)

**Where.** Violoncellos and Horn 1 (unison melody, dolce), bars 47-50 and 147-148.

**What is wrong.** Stem change c56 -> c60 per bar: bar 47 celli -4.9, Horn 1 -4.1; bar 49 celli -3.8, Horn 1 -1.1; bar 50 -3.8 / -4.0; bar 148 -2.1 / -2.8; harp and violas unchanged (0.0 to +1.4). In bar 49 the harp is now -40.6 against celli -38.4: 2.2 dB under the melody. This is the c60 `region_gain_db` Leg BC MAX -4 on every celli region plus the c60 lanes, which took the hot Leg BC notes down (as asked) but also the whole line. Critic B owns the celli; this is what the holistic comparison shows.

**Fix.** Keep the Leg BC cut; raise the line instead: `build/score_config.py` `CC11_LANE["Violoncellos"]` over 184-216 and 584-616, every point +6 units (0.41 dB per unit at 72-88 on this track: about +2.5 dB), and `CC11_LANE["Horn 1"]` over the same spans +4 units (0.51 dB per unit: +2 dB; its CC1 follows by `CC11_LANE_CC1`). Expected: melody back to within about 1.5 dB of c56, harp 4-5 dB under it in bar 49. If critic B's measured inner-line pass gives other values for these spans, use B's.

### 5. What still sounds like a machine (measured; no new fix beyond findings 1-3)

- The ff stabs are limited hardest: bars 82-83 6.7 dB (over 3 dB for 19 % of bar 83), 41 5.6, 170 5.3, 40 5.1; the fff summit only 3.5. The single highest pre-limiter peak (202.7 s, qn 328.3) is the sum crest of the accented Violins I double stop B4 / A-flat 5 with tuba, timpani and violas (master -5.5 dBFS, Violins I stem -10.0). At -14 the stabs lose the front of their attack. Finding 1 lowers the global figure only from 6.7 to 6.4 dB; a ride row on the stabs moves the limiting elsewhere (v8). Inferred: this stays until the delivered target is lower or the ff stab attacks are softened at the source, which Dan's accent rule (+1.5 to +2 dB) already limits. Left audible.
- Moment-to-moment movement is 1.59 dB against 2.64 for the recording; c60 C measured where (ff tuttis do not move with the beat) and showed long-note decay is not the lever. The delivery takes 0.46 of the master's 2.05. Nothing more to propose within the rules.
- Hot single samples left after the per-note rows went: Oboe 1 E5 (finding 3) is the largest found on the comparison; Oboe 1 F5 at 552.9 reads -31.2 at CC11 102 against -39.9 to -40.6 for its other F5s at 81-102 (8 dB; not checked further: in a tutti).

### 6. The top band is 2.2 dB under the recording (measured; low priority; A/B only)

Delivered 6-14 kHz share -30.8 against -28.6 for Dvořák 9/i (c0 -30.9). On the master it is -29.1; the delivery's `master_eq` high shelf (3 kHz, -1.3 dB) takes 1.7 dB of it. c53 chose this shelf over the template's +0.8 dB at 8 kHz to cut 6-20 kHz by 0.9 dB. The reference is a lossy mp3, which usually loses top, so the real gap may be larger. Fix (A/B on the delivery only, no render): `build/mix.json` `master_eq` highshelf 3000 Hz -1.3 -> -0.5 dB; expected 6-14 kHz about -30.0. Listen before adopting; do not combine with finding 1 in the same A/B.

## Not measured

c0's bars (different score version v221, no tempo map aligned; compared on whole-file measures only); per-note faults (critic A); inner lines bar by bar (critic B).

## Do not touch

The envelope state (0 per-note items, 0 fitted rows); the -14 loudness loop and the true-peak loop in `deliver_master.py` (reproduced exactly: I -14.0, TP -1.2); the cello-solo ride trim and the +0.5 dB coda rows (the coda is now 2-4.5 dB louder than c56 at the same delivery, which is what Dan asked for); the fugato rows' removal (bars 86-87 +3 dB); the master tone and width (equal to the recording since c53); the c60 master climax order (160 > 122 > 26 > 170 by bar level and loudest 0.4 s): fix the delivered order in the delivery, not by moving mix levels again.
