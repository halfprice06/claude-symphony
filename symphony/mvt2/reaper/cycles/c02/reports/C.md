# Critic C, cycle 2: dynamics over time

Under review: the cycle 1 render (`cycles/c01/render`, `metrics/`), `build/parts.json`, `tools/score_to_parts.py`. Scratch scripts are in `/private/tmp/claude-501/mockup-loop/c02-C/`:
- `a1_arc.py`: K-weighted loudness per bar, from the ffmpeg ebur128 momentary log.
- `a3_hp.py`: the level change across every hairpin, per stem.
- `a4_clim.py`: per-beat stem levels next to the CC values.
- `a5_dynbar.py`: master loudness grouped by printed dynamic.
- `a2_cal.py`, `a6_within.py`: how CC11 maps to level.
- `a7_long.py`: long notes.

Bars in this report: bar 59 = qn 196, bar 61 = 204, bar 63 = 212, bar 65 = 220, bar 79 = 262, bar 92 = 301.

Master loudness per bar (LUFS, mean momentary), the overall shape:

| Section | LUFS |
|---|---|
| Opening, bars 1-36 | -48 to -33 |
| Bar 59 (f) | -23.4 |
| Bar 61 (ff) | -19.7 |
| Bar 63 | -22.9 |
| Bar 64 | -32.4 |
| Bar 65 (return, pp) | -42.7 |
| Bars 79-80 (second ff) | -20.0 / -19.6 |
| Bar 84 | -46.7 |
| Bars 89-90 | -38.1 / -38.5 |
| Bar 92 (ppp, morendo) | -41.8 |

The overall range is right: LRA 23.5 LU, against 21.8 for the Dvorak reference. The shape inside that range is wrong in five places, ranked below.

## 1. The movement does not die away: the final ppp morendo is flat for 8 seconds, then stops (measured)

**Where:** bars 91-92 (qn 298-304), all tracks sounding; the timpani roll from qn 292.

**What is wrong:** the score has a decrescendo at 298, *morendo* in Clarinet 2, ppp at 301, and the tempo falls to 20 for the last beat, so the final chord is held about 6 seconds. A real orchestra fades that chord to almost nothing. In the render it holds its level and then cuts off.

**Evidence:**
- Master RMS in 0.25 s windows from 338.0 to 345.75 s stays between -43.4 and -47.1 dB, with no downward trend.
- At note-off (345.9 s) the level falls from -43.4 to -73 dB in 1.25 s, which you hear as a cut-off with a short reverb tail.
- Bar 92 measures -41.8 LUFS. That is louder than the pp return (bar 65, -42.7), than bar 84 (-46.7) and than the quietest bar (36, -47.6). It is only 1.2 LU under bar 91.
- The printed decrescendo 298-301 (CC11 34→22) moves Violins I by -2.3 dB, Violins II -2.5, violas -1.6 and celli -3.5. The string patches barely respond below CC 40 (finding 3).
- The timpani ppp roll (CC7 13) measures -49.0 dB through the whole final bar. It is the loudest stem there: Violins I -51.8, Violins II -57.4, violas -59.9. This breaks Dan's rule 5.

**Fix,** in `tools/score_to_parts.py`, a final-bar rule in `build_track()` after the CC11 sampling:
1. For every track with a note that ends at `END`, add CC7 points: 127 up to qn 301.5, then a ramp to 40 at qn 304. CC7 is channel volume; with the 40·log law the tools use for the timpani, 40 is -20 dB. Put a CC7 127 point at qn 0 on those tracks so earlier passages are unchanged.
2. Ramp CC11 for the same notes from 22 to 8 over qn 302-304.
3. For the timpani, scale the existing CC7 roll values by the same fade factor.

Targets:
- The last 2 s of the chord at least 12 dB below bar 91.
- Bar 92 the quietest bar of the movement (-48 LUFS or lower).
- No hard drop at note-off: the level falls less than 10 dB in the first 0.5 s after the note ends.

## 2. The main climax (bars 59-63) barely grows, sags on arrival, loses its sf, and is matched by bar 79 (measured)

**Where:** bars 59-63, all strings and winds; bars 75-81, Violins I and celli.

**What is wrong:** printed f at bar 59, crescendo in bar 60, ff at bar 61 with brass and timpani, then sf at bar 63 into a diminuendo. This should be the loudest point of the movement.

**Evidence:**
- **f to ff is only +2.5 LU in the master.** In 2-qn windows: qn 196 -22.3, 198 -25.0, 200 -21.8, 202 -21.3, 204 -19.8, 206 -19.6.
- **The bar 60 crescendo (qn 200-204, CC 88→104) does not grow in most winds and low strings.** Measured change: Flute 1 -1.7 dB, Oboe 1 -0.1, Clarinet 1 -2.2, Bass clarinet -1.4, Bassoon 1 +1.5, Horn 1 +0.6, violas +1.2, celli -1.3, basses +1.9. The upper strings do grow: Violins I +7.2, Violins II +5.9.
- **Cause of the small f-to-ff step:** ff is CC 104, but the patches' top dynamic layer runs up to 127. In FL KS Master the CC11 layer ranges are 0-55, 56-93 and 94-127, read from the .oib. HO manual p. 51: CC11 "controls overall volume, and ... crossfades between multiple dynamic layers". Measured level hardly changes above CC 88: Flute 1 is -38.8 dB in the CC 80-96 bin and -37.1 in 96-112; Horn 1 moves +1.0 dB from CC 88 to 102.
- **The celli peak before the arrival.** The espr. boost from qn 190 plus the crescendo takes their CC11 to 112 at qn 203.9; the boost ends at the "molto sostenuto" text, so the ff downbeat drops to 104. Celli measure -28.2 dB at qn 200, -31.7 at 204 and -33.5 at 206: they get quieter as the climax arrives.
- **The sf at bar 63 is not played.** In `base_points()` the sf adds (212, 100), but the decrescendo starting at the same qn adds (212, 104), which wins. CC11 holds 104 until 212.875 and then falls; sf (100) is below ff anyway. Violins I measure -34.8 dB at qn 210-212 and -34.0 at 212-214: no accent. The sf notes have velocity 83-90.
- **The second ff at bar 79 is as loud or louder.** Bars 79-80 measure -20.0 / -19.6 LUFS against -19.7 / -20.6 for bars 61-62. The loudest 2-qn window is -18.8 at qn 266, against -19.6 at 206. The cause is that the espr. boost (qn 237) and cantabile boost (238) are still on: Violins I are at CC 112 at ff in bar 79 against 104 in bar 61, and the celli at 96 for a printed f.

**Fix,** all in `tools/score_to_parts.py`:
- (a) In `final()`, fade the solo boost out at loud dynamics: `v += SOLO_BOOST * max(0.0, min(1.0, (88 - base(q)) / 30))`. That gives the full boost at mp and below and none at f and above.
- (b) In `base_points()`, when an sf or sfz falls where a hairpin starts:
  - write `(q, level)`, `(q + 0.02, min(124, level + 12))`, `(q + 0.5, level)`;
  - start the hairpin at `q + 0.5`;
  - add +15 velocity to notes at the sf;
  - keep the sf relative to the current level, not the absolute 100.
- (c) Set `DYN["ff"] = 114` and `DYN["fff"] = 124`, and update `DYN_NAMES` in `tools/measure.py` to match.

Targets:
- Bars 61-63 at least 2 LU louder than bars 79-80.
- Bar 59 to bar 61 at least +5 LU.
- The strings show a 3-4 dB rise for about 0.5 qn at qn 212.

## 3. The soft end is compressed: ppp, pp and p are only about 3 LU apart, and the steps between dynamics are uneven (measured)

**Where:** the whole movement, most of all the string-led pp passages: bars 1-14, 42-51, 65-74, 83-92.

**What is wrong:**
- Master loudness by the median printed dynamic of the bar: ppp -44.8, pp -42.1, p -39.0, mp -34.0, mf -27.8, f -25.6, ff -20.6.
- ppp to p is only 5.8 LU, and mf to f only 2.2. Between p and mf the steps are much larger.
- In the Dvorak reference introduction, the 5th percentile of short-term loudness is 39 dB below the 99th and 19.6 dB below the median. In the mix those gaps are 26 and 5.8 dB.

**Evidence:**
- **Strings barely respond to CC11 below 40.** Within single notes, the median is 1.1 dB per 14 CC (n=19, wide spread). Violins I measure -53.6 dB in the CC 10-30 bin and -52.0 in 40-52. Basses at ppp (-53.6) measure louder than at pp (-55.1).
- **Some patches jump in the middle of the range.** From the CC 52-64 bin to the 64-80 bin: bass clarinet +10.9 dB, Flute 1 +7.6, Clarinet 2 +7.6, celli +7.3.
- So `DYN` is linear in CC, but the patches' CC-to-level curves are not.

**Fix:**
1. Measure each patch's curve once. The actor renders a scratch project with one sustained mid-range note per KS Master patch and CC11 swept 1→127 over 16 s, then stores dB against CC as `build/cc_curves.json`. The exact pitch is not critical.
2. In `score_to_parts.py`, give each printed dynamic a target level in dB relative to f: ppp -22, pp -17, p -12, mp -8, mf -4, f 0, ff +4.
3. Convert each target to CC11 per patch by inverting that patch's curve. Where the patch cannot go low enough at CC 1, use CC7 for the rest.
4. Keep the mix.json gains as they are.

Targets: master medians ppp -50 or lower, pp about -46, p about -42; mf and f at least 3 LU apart.

## 4. One-step hairpins (the many small swells) are too small to hear (measured)

**Where:** the 95 hairpins that move about 11-14 CC (`HP_STEP` or one dynamic step). Most are the phrase swells in solos and strings, for example:
- Horn 1 solo, bars 7-13 and 67;
- Oboe and cor anglais solos, bars 15-20 and 41-51;
- Violins I/II, bars 17-24 and 71-72;
- the pp string swells in bars 66 and 86.

**What is wrong:** across their span these hairpins measure a median of +2.6 dB in the printed direction. 38 of 95 move less than 1.5 dB or the wrong way, for example:
- Flute 1, 126-128: -1.4 dB;
- cor anglais, 124-128: +0.1;
- Horn 1, 176-180: +0.5; Horn 1, 226-229: +0.4;
- Violins I, 70-72: 0.0; Violins I, 242-244: -0.5;
- celli, 124-128: -1.9;
- basses, 283-286: -0.8.

Hairpins with a printed target and more than 16 CC of travel work well: median 7.0 dB, and only 3 of 66 fail. That part of the parser should stay. In soft music a printed swell is normally played at about 4-6 dB (inferred).

**Fix,** in `base_points()`:
- Make the untargeted step depend on level: 22 CC when the starting level is mp or softer, 14 above that.
- For a cresc that ends where a decresc begins (the printed swell shape), let the decresc return to the level before the crescendo, as now.

After finding 3, define the step in dB instead: +5 dB at p and below. Target: at least 85 of 95 of these hairpins measure 2.5 dB or more in the printed direction.

## 5. Long notes are static (measured: no shape; benefit inferred)

**Where:** all sustained lines, most of all:
- the slow string pads (violas 33 of 52 notes of 2 s or more, celli 34 of 59);
- the woodwind and horn chorales (bassoons 38 of 55, Horns 3-4 20 of 32);
- the cor anglais solo (6 of 10).

**What is wrong:** 255 of the 476 notes of 2 s or longer have a completely flat CC11. In most wind stems the second half of these notes is within ±1 dB of the first half. There is no swell on long notes, and phrase ends are not tapered unless a hairpin is printed. Real players shape both. The brief allows "a slight swell on a long note".

**Fix,** in `final()` (or a pass after it) in `score_to_parts.py`, for families wind, horn and string:
- **Long-note swell.** For a note of 1.8 s or more in seconds (`qn_to_sec`) whose base curve is flat (no hairpin over it), add +4 CC rising to 40% of the note and falling to -2 CC at its end.
- **Phrase-end taper.** For the last note of a slur, or a note before a breath mark or a rest of 1 qn or more, add -6 CC over the last 50% of the note.
- **Where not to apply it:**
  - notes inside printed hairpins;
  - repeated-note accompaniment (the same pitch as the previous note);
  - the timpani;
  - the final bar (finding 1).

Both effects are about 1-2 dB, inside "small liberties".

## 6. Timpani ppp/pp rolls sit above the strings in the opening and the coda (measured)

**Where:** Timpani, bars 2-3 (qn 3-9, ppp) and bars 89-92 (qn 292-304, ppp).

**What is wrong:**
- **Opening:** in bars 2-3 the roll measures -48.5 to -48.8 dB. The pp strings are lower: Violins I -51 to -53, Violins II and violas -53 to -60, basses -51 to -54. Only the celli are above it (-45 to -49).
- **Coda:** in bars 89-92 the roll is flat at -48.1 to -49.6 dB and is the loudest stem in bar 92.
- **Settle:** the 4 dB settle moves CC7 only from 15 to 13, which measures 1.5 dB.
- A ppp roll should be felt under the strings, not heard above them (rule 5).

**Fix,** in `score_to_parts.py`, `roll_db`:
- ppp from -36 to -42 dB, pp from -31 to -35 dB; p and above unchanged.
- At ppp and pp, settle 6 dB instead of 4.
- Coda: apply the CC7 fade from finding 1.

Target: at ppp/pp the roll is 3-5 dB under the quietest sustained string section.

**Do not touch:**
- the hairpin parser and level holds: targeted hairpins measure a median of 7 dB, 63 of 66 in the right direction;
- the big diminuendos:
  - bar 63: Violins I -9.7, violas -16.5, celli -14.4 dB;
  - bar 81: Flute 1 and Clarinet 1 -14.2, violas -12.6;
- the crescendo into bar 59 (strings and winds +7 to +19 dB);
- the timpani roll table at p and above;
- the 1x render;
- mix.json.
