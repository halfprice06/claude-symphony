# Cycle 22, critic C: dynamics over time (on the cycle 21 render)

Lens: the shape of every hairpin and phrase, the loudness arc against the score (climax bars 59-63, return at 65, coda), loudness range, swells and decays on long notes, and comparison with recordings of real orchestras.

Material:
- `cycles/c21/render` (master and 32 stems), `cycles/c21/mvt2-mockup-c21.mp3` and `cycles/c21/metrics`.
- `build/parts.json`, which holds the data of the c21 render. Its tempo map puts bar 92 at 342.2-348.6 s, and that matches the render.
- `build/{roles,note_trims,early_fills,pitch_trims}.json`, `tools/score_to_parts.py`, `build/mockup-events.tsv`.
- Score pages 1 and 4-8.
- References: Dvorak 9/i (Columbia mp3) and the stored Brahms 1/ii and 4/ii loudness series.

Scripts and outputs are in `/private/tmp/claude-501/mockup-loop/c22-C/`:
- `lib.py`: BS.1770 K-weighting as an FFT magnitude filter, and the parts.json tempo map.
- `frames.py`: writes `kE.npy`, K-weighted 50 ms energy for the master and every stem.
- `bars.py`: LUFS per bar, master and mp3.
- `kb.py` and `grp2.py`: per-beat levels for stems and for instrument families.
- `hpgroups.py` and `leadhp.py`: every hairpin, measured as the level of the hairpin's last third minus its first third.
- `need.py`: splits each hairpin's level change into the volume-envelope part and the sample part.
- `a1.py`, `a6s.py` and `checks.py`: statistics and delivery checks against the references.
- `simhp.py`, `sim1.py`, `sim1b.py`, `sim56.py` and `simcoda.py`: simulations. Each one scales stem energy by a proposed gain curve and adds the difference to the master. That ignores interference between stems, which is accurate to within a few tenths of a dB at these levels.

## Delivery, c21 (measured)

| | Master | mp3 |
|---|---|---|
| Integrated loudness | -22.5 LUFS | -19.8 LUFS |
| LRA | 23.6 LU | 16.0 LU |
| True peak | -3.9 dBFS | -1.6 dBTP |
| p10 / max short-term | -39.7 / -13.2 | -27.9 / -9.4 |
| Span | 26.5 dB | 18.5 dB |

- mp3 checks: limiter 1.9 dB, 0 inversions. The median share of 5 s moves kept is 0.83 (p10 0.65).
- All the brief's targets are met. The LRA is at the top of its range.
- The bottom 10% of the mp3's short-term loudness comes from these bars: 10, 14-15, 18, 30, 35-36, 65-66, 70, 83-84, 91-92.
- The top 5% comes only from bars 60-63 and 79-80.

What holds (measured). Keep these:
- The large arc, in K-weighted LUFS per bar:

  | Bar | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60 | 61 | 62 |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | LUFS | -35.2 | -32.8 | -30.0 | -28.4 | -25.7 | -26.5 | -23.1 | -20.8 | -16.6 | -13.7 | -13.8 |

- Bar 61 is 1.7 dB over bar 79 (-15.4). In the mp3 the gap is 1.5 dB (-9.8 / -11.3).
- Bars 61-62 hold -13.0..-14.3 per beat.
- The strings' sf at qn 212 stands 2-3 dB over their last ff beats. They then fall 18 dB through the bar to the p of bar 64.
- The return: bar 64 is -25.1 and bar 65 is -38.3.
- Bars 81-82 fall 8.4 and 5.8 dB.
- Coda: ppp under pp under ppp, and the final chord sits at the level of the opening ppp chord.
- The theme A swell now goes the printed way in both statements:
  - Violins I+II: +1.6/-1.5 dB (qn 68-72) and +1.8/-2.8 dB (240-244).
- Timpani rolls settle under the texture.

Comparison with real orchestras (measured):
- Phrase-scale movement is the standard deviation of momentary loudness after removing a linear trend from each 6 s window.
  - Master: 1.25. Mid-level windows: 1.05.
  - Mid-level windows in the references: Dvorak 2.51, Brahms 1/ii 2.18, Brahms 4/ii 1.73.
- Momentary minus short-term loudness, standard deviation: master 2.21, Brahms 4/ii 2.83, Brahms 1/ii 3.45.
- Absolute change of short-term loudness over 1 s, p90: master 1.86, Brahms 4/ii 2.26, Brahms 1/ii 3.13.
- The mockup moves less than a real orchestra on the scale of a phrase, and less from note to note. These numbers have not changed since c18 (1.24).

Findings 1 and 4 are the parts of this gap that the printed hairpins account for.

## 1. Soft hairpins in six exposed solos do not move, because per-note trims cancel the +3 dB ramp (measured; fix partly simulated)

Where:
- Violin I solo, bar 17 (qn 48-51, p <) and bar 21 (60-62).
- Horn 1 solo, bar 11 (32-34, p < mp, rising to the crest Bb4).
- Horn 1, bar 54 (176-180, p < mp, with Clarinet 1).
- Flute 1, bar 41 (126-128, < mp).
- Oboe 1, bar 20 (57-59, >).

Evidence (measured): the level of the stem's last third of the hairpin minus its first third (K-weighted, 50 ms frames, medians), split by `need.py` into the volume-envelope and sample parts.

| Line | Printed | Change | Volume envelope | CC11 | Sample part |
|---|---|---|---|---|---|
| Violin I solo 48-51 | < | -0.8 | +1.0 | +13 | -1.8 |
| Violin I solo 60-62 | < | +2.0 | +1.3 | +8 | +0.7 |
| Horn 1 32-34 | < | -1.6 | **-3.1** | +8 | +1.6 |
| Horn 1 176-180 | < | +1.1 | -0.5 | +8 | +1.5 |
| Flute 1 126-128 | < | -2.1 | +2.4 | +8 | -4.4 |
| Oboe 1 57-59 | > | -1.0 | -3.1 | -15 | +2.0 |

For comparison, the solo hairpins that work are +4..+10 dB:
- Oboe 1 42-45 and 54-57: +7.8 / +9.9.
- Bass clarinet 93-108: +5.2 / -4.0 / -3.3 / +7.0.
- Cor anglais 157-171: +5.2 / -5.7.
- Horn 1 226-235: +4.1 / -7.4.
- Clarinet 1 280-282: +5.0.

Causes, read from the build data:
- **Horn 1, qn 32.**
  - `pitch_trims.json` gives F4 `{"early": 1, "body": -5}` with `_all_arts`.
  - `note_trims` 32 is +2.5.
  - So the F4 that carries the crescendo starts at +3.5 dB and drops to -2.5 dB after the early part. The +3 dB `hp_soft` ramp cannot overcome that.
  - Per 100 ms the note goes -34.5, -37.0, -35.4, -32.8, -30.1, -29.9, -31.6, -33.6, -33.2, -32.0. It peaks just after the attack, which works against the crescendo.
- **Violin I solo, qn 48.**
  - The line falls from Bb5 to Eb5 through the crescendo.
  - The c18 phrase-top rule (`PT_DB_PER_ST` 0.3) gives the slur's onsets +1.3 (Bb5), +0.4, -0.2 and -0.8 dB (Eb5). That is -2.1 dB across the crescendo (inferred from the formula).
  - `note_trims` 48.5 is -2. The sample also loses 1.8 dB going down the line.
- **Horn 1, 176-180.**
  - It is not in `LEAD_SPANS` (Horn 1 has (17,40) and (226,236) only), so this hairpin gets no `hp_soft` ramp.
  - Its early fill at 176 (5 dB) and note trim 180 (-2) make the envelope fall 0.5 dB across a printed crescendo.
  - The clarinet in unison rises 4.7 dB, so the pair rises only part of the way.
- **Flute 1, qn 126.** The sustained F5 sags (-38.5 to -41.6 to -39.3), so the +2.4 dB envelope ramp is lost.
- **Oboe 1, qn 57.**
  - The decrescendo has the default `HP_SOFT_DEC_DB` 2.
  - Most of the envelope fall (vol 8.2 to 4.4) happens in the first 0.5 qn, where the note-start fill ends.
  - The rest of the held Ab is flat (-36.4..-37.5).

Fix (`tools/score_to_parts.py` and the build JSON):
- (a) Add a per-onset table, `HP_SOFT_GAIN_AT = {"Violin I solo": {48.0: 6.0, 60.0: 4.5}, "Horn 1": {32.0: 4.0, 176.0: 5.0}, "Flute 1": {126.0: 6.0}}`.
  - In the `hp_soft` crescendo branch, use it in place of `HP_GAIN_SOFT_DB[family]`, in both the messa-di-voce and the held cases.
  - Extend `HP_SOFT_DEC_AT` with `"Oboe 1": {57.0: 5.0}`.
- (b) `LEAD_SPANS["Horn 1"]`: add (174, 184).
- (c) Horn 1 qn 32:
  - In `pitch_trims.json` add `"_skip_onsets": [32.0]` to Horn 1. Keep the F4 trim everywhere else.
  - In `note_trims.json` set Horn 1 "32" from 2.5 to -2.0. The F4 then starts low and the ramp carries it up into the Bb4 crest, which keeps its +6.5 and the qn 34 lift.
- (d) Phrase tops: in the PT block (`pt_slurs`), do not apply PT values to onsets inside an `hp_soft` crescendo or decrescendo span of the same track. The printed hairpin then sets the shape there, not the pitch contour.
- (e) Flute 1 qn 126: the F5 body sag is a sustain problem. It is critic A's area (loop seam or fill). The +6 above covers the level, but say so in CHANGES.

Simulated:
- `sim1b.py` adds these ramps as extra gain on the stems, without the structural changes c and d:
  - Violin solo 48-51: -0.8 -> +2.8.
  - Horn 1 32-34: -1.6 -> +1.3. This one also needs (c), because the hump at the attack is in the trims, not the ramp.
  - Horn 1 176-180: +1.1 -> +4.9.
  - Flute 126-128: -2.1 -> +1.4.
  - Oboe 57-59: -1.0 -> -2.9.
  - In the master these hairpins go from -1.2/-1.2/+0.4/-1.2/-1.3 to +1.5/+0.8/+1.8/-0.1/-2.6.
- With (c) and (d) the envelope parts of the first two rows rise by about 4.5 and 2 dB more (inferred from the trim values).

Check on the render:
- Each listed hairpin rises at least +3 dB (stem, last third minus first third).
- The bar 18 solo peak stays within 3 dB of the oboe's bar 20 peak.
- The Bb4 at qn 34 stays Horn 1's loudest note in bars 11-13.

## 2. The mf of bar 56 sags 5.8 dB before the strings' printed crescendo in bar 57 starts (measured; partly simulated)

Where: Violins I, Violins II, Violoncellos and Double basses, qn 184-190. The score (page 4) has strings mf at 56. Bar 57 has no new string dynamic (Violas enter mp) and a crescendo to f at 59.

Evidence (measured):

| qn | 184.5 | 185.5 | 186.5 | 187.0 | 187.5 | 188.0 | 188.5 | 189.5 |
|---|---|---|---|---|---|---|---|---|
| Master | -24.2 | -25.4 | -24.5 | -27.7 | -30.0 | -28.8 | -27.1 | -25.8 |

- The strings' sum goes from -25.0 (184.5) to -31.7 (187.5).
- The listener hears bar 56 swell and fade, and then a new crescendo begins from below. The printed shape is mf continuing into a crescendo. This is the open c21 item "bar 56 -> 57 -1.7 dB". K-weighted per half beat, the sag is 5.8 dB.

Causes (build data):
- The mf-arrival `hpgain` [180,184] (+2 dB, strings) is held only to the next note, by `nx` in the hold. That next note is qn 186 for Violins I. The gain is then released over `HP_REL`: Violins II vol goes 3.12 (185), 2.0 (186), 1.12 (187), 0.19 (187.5), 0.0 (188).
- The new crescendo's gain [188,196] starts from 0 at 188.
- The Violoncellos role [188,204,-3,4] is a step at 188. The envelope goes from 3.0 at 188.0 to -2.81 at 188.5, so the Violoncellos lose 5.8 dB in half a beat.
- Violins II at qn 188 (Ab4, the "ord." phrase) also starts 7 dB under its previous note (-41.2 against -33.5..-35).

Fix (`tools/score_to_parts.py`, `build/roles.json`):
- (a) In the hpgain hold, when the same track's next hairpin is a crescendo that starts within `HP_CHAIN` qn after the arrival, and no softer dynamic is printed in between, set `hold_end` to that crescendo's start. Release the held gain linearly over the crescendo's first 1.5 qn while its own ramp rises.
  - This is a hold only. The gains do not add, so the c16 "mf arrivals do not chain" decision stands.
  - In this movement it applies at qn 184 -> 188 only (inferred from the marks list; check `hp_chained`).
- (b) Split the Violoncellos role [188,204,-3,4] into [188,190,-1.5] and [190,204,-3,4]. With `ROLE_CHAIN` the cut then comes in over two beats.
- (c) Look at Violins II's 188 onset; no trim at 188 is listed in the JSON files. If it is the sample, a `note_trims` +3 at "188" brings it to the level of its neighbours.

Simulated (`sim56.py`, a and b only):

| qn | 184.5 | 185.5 | 186.5 | 187.0 | 187.5 | 188.0 | 188.5 |
|---|---|---|---|---|---|---|---|
| Master | -24.2 | -24.6 | -24.0 | -26.4 | -28.0 | -26.7 | -26.0 |

- The sag is 3.8 dB instead of 5.8.
- The rest comes from the Violins I slur end at 186-188, the -1.5 dB phrase taper of `swell_db`. A breath there is musical; with (c), the dip would be about 3 dB.
- The bar 58-61 rise is unchanged, because the 188-196 hpgain still starts at 0.

## 3. Coda bars 86-87: the strings' ppp < pp comes in the last beat, and the pp chord attacks and then decays 5 dB (measured; partly simulated)

Where: Violas (and the Violas div voice), Violoncellos and Double basses, qn 283-288 (page 7-8). The printed mark is < from ppp to the pp of bar 87, and the new chord arrives at 286 with Clarinets, Horns 3-4 con sord. and Violins II.

Evidence (measured, string sum per half beat, K):

| qn | 283 | 283.5 | 284 | 284.5 | 285 | 285.5 | 286 | 286.5 | 287 | 287.5 | 288 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Strings | -45.2 | -45.0 | -45.1 | -44.2 | -43.1 | -40.6 | **-38.6** | -41.4 | -43.2 | -43.8 | -43.5 |
| Master | | | | | | | -35.6 (-35.2 per 0.25 qn) | | -37.0..-39.8 | | |

- The crescendo is flat for 1.5 beats. The strings then overshoot at the arrival and fall 5 dB into the held pp.
- Per stem, from the arrival (286.0) to 287:
  - Violoncellos: -40.9 to -46.9..-49.0.
  - Violas: -46.4/-42.6 to -50.
  - Double basses: -43.9 to -47..-53.
- The causes are `VEL_SET` {286.0: 60} for Vla/Vc/Cb, set in c10 because the v41-53 re-attacks decayed 5-11 dB, and the Double basses' CC11, which goes 33 -> 40 at 286 and falls back to 32 by 287.
- The re-attacks still decay; they now start from a stronger attack.
- In the mp3 the ride is +12.4..+13.0 dB here, so the bump and the decay are as exposed as anything in the piece.

Fix (`tools/score_to_parts.py`):
- (a) `JOIN_NOTCH` entries over the arrival attacks: "Violoncellos" (285.75, 286.30, -3.0), "Violas" (286.00, 286.40, -3.0), "Double basses" (285.95, 286.30, -3.0).
- (b) Find the source of the Double basses' CC11 +7 at 286 and cap that note's CC11 at the printed pp (34).
- (c) Give bar 86's < a level ramp (finding 4's rule, or a role chain) of +2.5 dB over 283-286, released over 1 qn.

Simulated (`simcoda.py`, a and c):
- The strings rise -45.0, -44.4, -44.1, -42.9, -41.3, -38.9 into the arrival, so the crescendo is spread over the bar.
- The arrival block is 0.5 dB lower.
- The decay after the arrival is a sample effect. A notch alone does not fix it. If the render still shows a fall of more than 3 dB from 286.5 to 287.5, add `note_trims` shapes (+2 to +3 over 286.5-288) for these three tracks.

## 4. Soft hairpins outside the lead lines change only through CC11 (about 2 dB). Give them a smaller dB ramp (measured; simulated)

Where:
- Every soft hairpin, starting at CC11 66 or lower, in a track or span outside `LEAD_SPANS` that has no hpgain of its own: 131 hairpins.
- Examples, as the hairpin group's level (last third minus first third) and the master's:

| Span | Lines | Printed | Group | Master |
|---|---|---|---|---|
| qn 124-128 | Cor anglais, Violas, Violoncellos | < | +1.8 | +1.0 |
| qn 168-172 | Timpani, Violas, Violoncellos, Double basses | < | +2.2 | |
| qn 168-171 | Violins II | < | +0.9 | -0.5 |
| qn 223-226 | Violins II, Violas, Violoncellos | > (bar 66, the return) | -3.1 | -0.5 |
| qn 283-286 | coda | < | | -2.4 (the clarinet's phrase end dominates) |
| qn 298-301 | morendo | > | -2.4 | |

- CC11 moves 0.11-0.19 dB per step at p (c14), so a 12-step hairpin is worth 1.3-2.3 dB. A section playing p < mp in an orchestra changes by about 4-6 dB (inferred).
- This is the accompaniment half of the phrase-scale gap: 1.25 here against 1.73-2.51 in the references.

Fix (`tools/score_to_parts.py`, `hp_soft` block):
- Add a branch for tracks (string, wind and brass families) and spans not in `LEAD_SPANS`, under the same conditions: CC11 66 or lower at the start, no hpgain of the same span, not in `SWELL_NO_SOFT_GAIN`.
- Use a new constant `HP_GAIN_SOFT_ACC_DB = 2.5`: crescendo ramp to +2.5 held to the arrival and released over `HP_REL`, and decrescendo -2.5. A < > pair works as in the lead branch (messa di voce).
- Exclude the harp, the timpani (their rolls have their own hairpin factor) and the theme A swells already in `SWELL_SOFT_GAIN_AT`.

Simulated (`simhp.py`):
- Phrase-scale movement 1.253 -> 1.306 with this rule alone, about 1.34 with finding 1 added.
- Master LRA (estimated from 3 s windows of the K-weighted frames) 23.62 -> 23.73. The mp3 LRA should move by under 0.1 (inferred), because these moves are a few seconds long and the gain ride smooths over 3 s.
- At +3/-3 on every soft hairpin, including the lead lines, it reaches 1.48. So the depth can be raised later if the render sounds right.

## 5. The morendo of bar 91 falls only 3.7 dB, and the final ppp chord does not decay under its fermata (measured; target inferred)

Where: every string line, qn 298-304 (page 8: strings ">" marked "morendo" in bar 91, ppp with fermata in bar 92). The Clarinets and Horns finish their > at 297.

Evidence (measured):
- Strings' sum per half beat: 298 -40.3, 299 -41.2, 300 -42.6, 301 -44.0, 302 -43.7, 302.5 -43.5, 303 -44.6, then the release from 303.5.
- The master in the fermata (343-347 s) holds -43..-45.8. It then falls about 45 dB over 1.5 s of hall tail, after which there is silence.
- The morendo is the smallest diminuendo among the coda's full-ensemble hairpins: bar 81 -8.4, bar 82 -5.8, bar 91 -2.4 (group, last third minus first third).
- `roles.json` Violas [298,304,7] lifts the violas through it. That is a balance choice (c05 B #4), and the violas still fall 5.5 dB.
- In the mp3 the ride rises from +12.9 (bar 90) to +14.0 (bar 92), which takes another 1.1 dB off the fall. The mp3 bars 90/91/92 are -26.3/-27.7/-30.5.

Fix (`build/roles.json` `_all`): add [298.5,299.5,-1], [299.5,300.5,-2], [300.5,303.5,-3].
- With `ROLE_CHAIN` this becomes a stepped ramp of 1 dB per beat across bar 91. It holds -3 through the fermata until the existing final fade takes over at the release.
- Keep [283.5,304,-2] and the violas' +7.
- Expected (inferred from the role values): a morendo of about 6.5 dB, and a final chord about 3 dB under the opening ppp chord.
- The mp3 LRA should not move, because bars 91-92 are already in the bottom 10% of short-term loudness (63 frames). Check it on the delivery.
- If the closing ppp must stay equal to the opening ppp, use only [298.5,299.5,-1] / [299.5,301,-2] and stop at 301.

## Do not touch

Keep these unchanged:
- `deliver_master.py` constants: mp3 LRA 16.0, limiter 1.9, 0 inversions, 83% kept.
- The bars 52-61 rise, and bar 61 over bar 79 (1.7 dB master, 1.5 dB mp3).
- The bar 61-62 hold and the qn 212 sf with its fall into bar 64.
- The 64 -> 65 return drop.
- The bars 81-82 decrescendos.
- The theme A messa di voce (`SWELL_SOFT_GAIN_AT`), which now goes the right way.
- The working solo hairpins: Oboe 1 42/54, Bass clarinet 93-108, Cor anglais 157-171, Horn 1 226-235, Clarinet 1 280.
- The timpani roll settle.
- The coda's ppp-pp-ppp order.
- The tail hold.
- The final release and the hall tail.
