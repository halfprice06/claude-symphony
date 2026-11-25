# Critic B, cycle 3: balance and levels (render c02)

Method. All levels are K-weighted (BS.1770 filter, LUFS-style dB) unless marked RMS. Per-note levels run from onset + 80 ms to min(note end, onset + 1.5 s), paired with the CC11 value at the onset. Fits of level against CC11 use notes of 0.9 qn or longer. Per-beat levels come from the stems, using the tempo map in parts.json. Scripts and data are in `/private/tmp/claude-501/mockup-loop/c03-B/`: `an.py` (per-note levels), `fit.py` (dB per CC), `kbars.py` and `top.py` (per-bar levels and the loudest stems in each bar, with printed dynamics), `qlev.py` (per-beat levels for chosen tracks), `spec.py` (band spectra).

What c02 fixed (measured): the celli no longer cover the violin tune in bars 23-28 and 75-77. At p every family lands between -45.6 and -52 (fit at CC46). Bars 53-56 are balanced. The horn solo in bars 7-14 leads by 5-12 dB. At ff the trombone leads the decaying strings in bar 63 with about the Rimsky-Korsakov margin: Tbn1 -26 against tutti ff violins at -29 to -30, where one trombone counts as two horns, which is about +3 dB over a string section.

## 1. The soft timpani rolls sit level with or above the pp strings. In bar 52 the roll is the loudest stem, and in bar 92 it is the loudest at the end (measured)

Where: Timpani in bars 2-3 (qn 3-8, ppp), bar 52 (qn 168-172, pp cresc. to p), bars 67-70 (qn 226-237, ppp under the "1. solo" horn) and bars 89-92 (qn 292-304, ppp). Also the p stroke at qn 271 (bar 82).

What, per beat:
- Bar 2: the ppp roll starts at -46.7 and settles to -50.3. The pp strings it accompanies measure Vln I -51.7, Vln II -50.5, Vla -56.3, Vc -50.8, Cb -54.3. In RMS the roll is -51.2 against violins at -55.9 and -56.5, with its energy at 160-320 Hz (`spec.py`), so the K-weighting is not causing this.
- Bar 52, qn 168-171: the roll measures -42.6, -41.8, -40.4, -40.2. The cor anglais solo (p) measures -46.4, -49.1, -46.4, -45.3, and the strings (pp, decresc.) -39.5 to -55. The roll is the loudest stem in the bar (top.py). Bar 52 is 4 dB louder than bar 51 in the mix, with no cresc. printed for anyone but the timpani.
- qn 233-236: the roll holds -49.9 to -50.6 after its settle, against Horn 1 at -47.4, -49.4, -50.8, -50.3 (mp dim. to pp). The roll is level with the solo or above it. c02's target was 3 dB under.
- qn 292-301: the roll holds -50.2 to -50.6 against Vln II -50.6 to -53.6 and Vla -54 to -60. At qn 301-303 it is the loudest stem (-51.2, -57.6, -65.4 against Vln I -53.7, -59.5, -70.7). All parts are printed ppp with a fermata.
- The p stroke at qn 271 measures -39.4. The strings arriving at p measure -45 to -55. It is the loudest stem in bar 82.
- BRIEF rule 5: a roll starts at its printed dynamic and then settles under the texture. Rimsky-Korsakov treats a ppp roll as a background colour.

Cause (measured from parts.json): the rolls play at CC7 16 and velocity 31 (ppp) or CC7 21-28 and velocity 41 (pp). The vol_db settle (-5 dB over 3 qn) works, measured at -3.6 to -3.9 dB, but it starts from a level that is too high.

Fix:
- `tools/score_to_parts.py`, timpani block (`timp_db` / vol_db): add a flat -6 dB to `vol_db` for every roll whose printed dynamic is p or softer. That covers qn 3, 168, 226 and 292. Keep the existing -5 dB settle on top of it. Do it in vol_db, not in `roll_db`, because the CC7 curve is not documented.
- Strokes: at p, use roll + 12 instead of roll + 16, which brings qn 271 down 4 dB. Leave the pp strokes at roll + 20. qn 277 is now -50.1, which is fine. qn 278.5 and 279 are -58.4 and -56.1, still about 6 dB under qn 277, so raise velocity 56 → 60 on those two notes only.
- Targets: bar 2 roll at or below -52.5 at its onset and about -56 settled. Bar 52 roll at or below -48 at the start and at or below -46 at qn 171, under the cor anglais. qn 229-236 roll at or below -54, at least 3 dB under the horn. Final roll at or below -55 and under Vln I in bar 92.

## 2. Divisi chords and double stops on section patches play two full sections. Violas cover the violins in bars 28 and 61-62, and Vln II covers the flute solo in bars 37-40 (measured)

Where (`poly` scan of parts.json, where two notes sound at once):
- Violas: bars 23-30 (div.), 61-64 (non div. tremolo double stops, ff), 84-86.
- Violins II: bars 37-40 (div., sul tasto, pp) and 63-64 (tremolo double stops).
- Violins I: bar 63 (div.).
- Violoncellos: bars 18 and 22 (div.).

What:
- Fit residuals for 2-note chords against single notes on the same track: Vla Sus MAX +1.8, Vla Tremolo +2.0, Vln II Flautando +2.0, Vln II Tremolo +8.2 (4 notes; the tremolo patch adds more). Each chord note fires a sample recorded by the full section. A real divisi gives each note half the players, so the pair should sum to about one section's level.
- Bar 28 (qn 81-83), all instruments printed mf: Violas (div. chords) -40.4, -39.9, -41.3 and Basses -41.1, -39.8, -41.2, against the melody in Vln I -47.0, -41.5, -43.8 and Vln II -50.1, -46.9, -42.6. The tune falls under its accompaniment at the top of the phrase.
- Bars 61-62 (qn 204-212, all ff, "molto sostenuto"): the violas' tremolo double stops measure -25.3 to -28.1. The violin melody in octaves measures -28.3 to -30.9 (Vln I) and -30.9 to -38.0 (Vln II). The violas are the loudest stem at the climax (bars 61 and 62 in top.py).
- Bars 37-40 (qn 108-123): Vln II "pp, div., sul tasto" measures -42.6 to -50.3. The "1. p" flute solo measures -42.5 to -51.6, so the pp accompaniment is level with the solo.
- qn 212 (bar 63, sf): Vln II double stops reach -23.4, the loudest string moment in the piece. qn 216-217 (bar 64, p tremolo): Vln II -36.2 and -35.3, 7-10 dB over Vln I (-43.4) and the violas (-46.5), all printed p. The per-note residual there is +12.3.

Fix: in `score_to_parts.py`, where vol_db is assembled, for string-family tracks:
- Over every span where k ≥ 2 notes sound together, add -10·log10(k) dB (-3 for pairs) when the governing staff text is "div.". For "non div." double stops, use -1.5 dB. This is inferred: each player bows two strings with less weight on each. Ramp it in over 0.1 qn before the chord onset and out 0.1 qn after it. The text spans are already parsed for "unis." and "sul" in the CC70 block, so reuse that parsing.
- For 2-note tremolo chords, add a further -3 dB (measured: Vln II tremolo chords +8.2 over the fit, violas +2.0).
- Targets: bar 28 melody (louder violin section) at least 2 dB over the violas. Bars 61-62 violas at least 2 dB under Vln I. Bars 37-40 Vln II at least 5 dB under the flute. Bar 64 Vln II within 2 dB of the other p strings.

## 3. Violas and bassoons rise too steeply with CC11: soft at p, the loudest of their families at f and ff (measured; targets from Rimsky-Korsakov)

Fitted level at each CC11 value, from notes of 0.9 qn or longer:

| track | dB/CC | pp 34 | p 46 | mf 72 | f 88 | ff 114 |
|---|---|---|---|---|---|---|
| Violins I | 0.231 | -48.4 | -45.6 | -39.6 | -35.9 | -29.9 |
| Violins II | 0.254 | -51.5 | -48.5 | -41.8 | -37.8 | -31.2 |
| Violas | 0.325 | -54.1 | -50.2 | -41.7 | -36.5 | -28.1 |
| Violoncellos | 0.252 | -53.5 | -50.5 | -43.9 | -39.9 | -33.4 |
| Bassoon 1 | 0.302 | -54.6 | -51.0 | -43.1 | -38.3 | -30.5 |
| Bassoon 2 | 0.296 | -55.7 | -52.1 | -44.4 | -39.7 | -32.0 |
| median single woodwind (Ob1, CA, Cl1, BCl, Bn2) | | | | | -39.5 | -33.0 |

What:
- The viola section goes from 4.6 dB under Vln I at p to 1.8 dB over at ff. A viola section has fewer players than either violin section and should sit about 1 dB under Vln II at every dynamic.
- In bars 59-60 (all printed f, violins carrying the tune in octaves) the violas' accompanying arpeggios measure -35.2, -35.2, -36.8, -33.9, -34.8, -34.0, -32.9, -31.1, level with or above Vln I (-31.6 to -36.2).
- The bassoons go from 3-5 dB under the other winds at pp/p to the loudest woodwind at ff. Bn1 at ff is -30.5, level with the first violins. Rimsky-Korsakov (Principles, "Comparison of resonance") puts one woodwind at about half a string section in forte, which is about -3 dB.
- Where you hear it:
  - Bar 59: Bn1 -34.4 and Bn2 -34.6 are the loudest stems, over the violin tune at -35.2.
  - Bar 62: Bn1 is second loudest (-28.4).
  - qn 208-209: Bn1 -26.2 against Vln I -30.9.
  - Bars 79 and 81: Bn1 is in the top two.
- c02 raised the bassoon f/ff trims to +2.5/+4, which was more than my c02 table asked for (+1.5/+2).

Fix (`build/mix.json`):
- Violas: `dyn_trim_db` f 0.5 → -2, ff 1 → -3. Remove the viola `soft_trim_db` pp -2 (set pp 0, keep ppp -4). Expected result: Vla at Vln II -1 ±1 dB at pp, f and ff.
- Bassoon 1: `dyn_trim_db` f 2.5 → 1.5, ff 4 → 1.5. Bassoon 2: f 2.5 → 2, ff 4 → 3. Contrabassoon unchanged.
- Check after the render: re-run `fit.py`. Violas between Vln II -2 and Vln II at every column. Both bassoons within ±1 dB of the woodwind median at f and ff.

## 4. The c02 note trims landed on the climax notes and missed the swelling soft notes; other hot notes remain (measured)

Where and what: `note_trims.json` keys on pitch and a minimum length in seconds, with no condition on dynamic or position.
- Oboe 1 F5: the -7 dB trim hit the ff tenuto notes at qn 204 and 208 (bars 61-62). Their residuals are now -4.6 and -5.0, so the oboe drops out of the climax. It missed qn 190, 1.49 s at 62 bpm, under the 1.5 s cutoff. In bar 57 that note measures -38.4 then -35.1, louder than the violins at mf (-39.6 to -40.0), with the oboe printed p cresc. The residual is +9.9. qn 194 has a residual of +6.4.
- Flute 1 B♭6: the -4 dB trim hit the ff note at qn 262 and missed qn 254 (1.04 qn, 1.2 s). In bar 77 that note measures -32.8, 8 dB over the mf violin melody (-41.0). The residual is +10.0.
- The qn 45 oboe note and the qn 152 cor anglais note are now fine (+1.5, +1.9).
- Other notes 5-10 dB over their CC prediction at mp or softer, from the per-pitch residual scan:
  - Bass clarinet E♭4 at qn 93 (bar 32): +7.3. It peaks at -33.6, 12-15 dB over the cor anglais "p dolce" counterline (-47 to -49). Its median at mp is the hottest wind on the chart.
  - Bassoon 2: D♭3 at qn 172, 182, 252 and 253 (+9.1, +9.1, +8.6, +7.7), and G♭3 at qn 190 and 196 (+10.1, +7.9). In bar 57 Bn2 measures -37.5/-36.1, louder than both violin sections.
  - Bassoon 1: G♭3 at qn 184 and 196 (+8.2, +6.6).
  - Clarinet 1: G5 at qn 256 (+7.2).
  - Violoncellos: qn 139, 164, 180 and 238 (+8.2, +7.5, +10.0, +7.6).

Fix:
- Change `note_trims.json` to explicit onsets: `{track: {"qn": dB}}`. Change `score_to_parts.py` to match a note by onset within 0.02 qn, with no length cutoff. Keep the existing ramp (0 dB at onset → full trim at onset + 0.6 s, held to note end, back to 0 at note end).
- Values:
  - Oboe 1 {45: -7, 190: -8, 194: -5}
  - Cor anglais {152: -8}
  - Flute 1 {254: -8}
  - Clarinet 1 {256: -5}
  - Bass clarinet {93: -6}
  - Bassoon 1 {184: -6, 196: -5}
  - Bassoon 2 {172: -7, 182: -7, 190: -8, 196: -6, 252: -6, 253: -6}
  - Violoncellos {139: -6, 164: -5, 180: -7, 238: -6}
- This removes the trims at Oboe 1 qn 204/208 and Flute 1 qn 262.
- Check after the render: no note of 0.9 qn or longer more than +5 dB over its track's CC fit, and the ff oboe notes at 204/208 back within ±2 dB.

## 5. The harp chords still match or beat the cor anglais solo in bars 41-43 (measured)

Where: Harp against Cor anglais, qn 124-136. The cor anglais is printed "solo, dolce cantabile" p<mp>p. The harp chords are printed p.

What: the harp chord beats measure -45.9 (qn 124), -41.9 (126) and -41.9 (132). The cor anglais at the same beats measures -45.4, -45.8 and -46.3. Each chord comes in 2-4 dB over the solo, even with the c02 roles cut of -3 dB. The bar medians are harp -46.0 against CA -45.9 in bar 41, and -45.9 against -45.4 in bar 43.

Fix: in `build/roles.json`, change Harp [124, 140, -3] to [124, 140, -7]. Alternatively, keep -3 and lower the harp velocity in that span by 12, because the harp's dynamics come from velocity (Sus RR). Target: harp chord beats at least 3 dB under the cor anglais.

## 6. Mix-level note: at the soft end, the melody's lead depends on these fixes more than on gains (inferred)

Track gains need no general change. At p the families match within about 6 dB, and the remaining leads are correct in bars 7-20, 45-50 and 71-74. Most of the balance faults above are local: rolls, chords, hot notes and harp. Fixing findings 1-5 in vol_db is better than moving any track's `gain_db`, which would disturb the matched p levels.

Do not touch: the matched p levels across families; the c02 celli roles cuts (the celli now sit 1-5 dB under the violin tune in bars 27, 57 and 75); the horn solo lead in bars 7-14 and 67-69; the f/ff timpani rolls 2-6 dB under the strings (qn 200-212); Trombone 1's ff marcato lead in bars 63-64; the timpani roll settle mechanism in vol_db; the volume-envelope scheme (gain in the envelope, CC11 choosing the layer); the Flute 1 f/ff trims (the flute is now within 1 dB of the woodwind median at ff).
