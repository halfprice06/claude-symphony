# Cycle 10, critic C: dynamics over time (lens C2), on the c09 render

Sources: `cycles/c09/render/` (master, 31 stems, 4 return stems), `cycles/c09/scherzo-mockup-c09.mp3`, `cycles/c09/build_render/parts.json`, `build/score_config.py`, `build/roles.json`, `build/accent_fits.json`, `tools/score_to_parts.py`, `tools/deliver_master.py`, `build/mockup-events.tsv`, score pages 6 and 12, and the masters of c00-c08 for comparison. Levels are plain RMS dB on the parts.json tempo map, in windows of 0.25-1 qn, unless marked LUFS (EBU momentary or short-term, from ffmpeg ebur128). Bar b starts at qn 3(b-1). I re-ran `deliver_master.py` on the c09 master into my scratch folder only. It reproduced the delivered figures exactly (LRA 14.7, span 19.6). I used that to test ride-trim variants.

## Manual notes (cycle 10, slot C: group D3, May 2021 HO manual PDF pages 68-71, read for levels; MANUAL-GAPS.md read)

| Page | What the manual says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| p.68 | Hollywood Harp uses a solo-instrument mic set: close and mid, each with a vintage alternative, and no surround. | Harp and Harp harmonics tracks. | Yes. Template mics with Mid added (c06). This page has nothing on levels. |
| p.68-69, Angels / Maestro | Velocity switches the articulation: nail picks at 103-127 (Maestro) or 123-127 (Angels). | Not used. The harp plays "Harp Sus RR". | Not applicable. |
| p.69, Sustain RR | Pluck Long and Thumb Pick alternate by round robin at velocity 1-123, with 5 dynamic levels each. Velocity 124-127 plays the Nail Pick. "CC 11 (Expression) and Note Velocity control overall loudness." | The Harp track's 346 notes. The pp off-beat chords of the trio and the Meno mosso; the p espress. line of the F major episode (bars 73-80, qn 216-240). | Velocity part: yes. The velocity is 40-56 (pp median 42, p 52-56) and never reaches the Nail Pick. The harp's stem medians are pp -49.5 and p -37.9 dB, so pp and p differ in level and in layer (measured). CC11 part: no. CC11 is fixed at 110 for the whole movement, and the episode's velocities are capped at 56 (`VEL_CAP_SPANS`), so the harp's printed hairpins have no way to sound (finding 4, measured). |
| p.69, Bisbigliando (CC1) | CC1 fades in the fingered tremolo. | Nothing printed needs it. | Not used, which is correct. |
| p.70, Harmonics | Separate patch, 2 velocity layers. It "blends well with pizzicato strings". CC11 and velocity set loudness. | Harp harmonics track, bars 149, 151 and 375 (all 9 notes at v58, CC11 110). | Yes. The p harmonics measure -47.0 dB (stem median) at 445 and 451, and -48.9 dB at 1122-1125, where they enter with the celli and basses pizz. Measured. |
| p.70, Repetition Rep, Double Hit, Pres de la table, Gliss | Repeated notes ring through; the others are effect articulations. | The trio's repeated off-beat chords could use Repetition Rep. | Not used. Sus RR's round robin covers the repeats, and this is not a dynamics issue. |
| p.71 | Glissando key map. | The scherzo has no harp glissando. | Not applicable. |

MANUAL-GAPS #7 (recorded crescendo rolls, "Crs" row) gives an alternative fix for finding 5.

ONE_TIME item 6 (finale: no positive PHRASE_SHAPE offset on a phrase that starts on a sub. p), checked in parts.json:
- No positive offset is written at either sub. p.
- At qn 828 the lyric arch's -12 CC start puts the celli and Bassoon 2 on CC11 34 (the pp value) for the printed sub. p, and Oboe 1 on 42. The celli measure -56.4 dB there, against a p median of -45.6 dB with their -3 role.
- At qn 360 the strings start at CC11 49-50.
- Both sub. p's follow a played rest, so the hall of the tutti decays under them. At 360 R Strings falls from -39.8 dB at -0.3 s to -46.6 dB at the onset, with no cut. S3 holds (measured).
- The "drop" type is not needed. If the celli at 828 should read as p rather than pp, give the arch's start offset a floor at a subito (inferred, small).

## Findings, ranked by what a listener would gain

### 1. Short soft swells on the wind and horn solos rise 6-11 dB in one beat, to the instrument's own fff level (measured)

**Where.**
- Horn 1, bars 147-148 (qn 440-442), the link.
- Clarinet 1's trio tune, bars 155, 158 and 159 (qn 464-466, 471-474, 476-478).
- Horn 3's dolce tune, bar 343 (qn 1028-1030).
- Violins I, bar 181 (qn 542).

Each is a one-beat < (with a > after it) printed inside a p or dolce line, with no target dynamic.

**What a listener hears.**
- **Horn 1, bar 147 (the ppp link).** The horn's p < > jumps from -39.6 dB (qn 439) to -31.8 dB (qn 441): +7.8 dB in one beat. Its ff in the coda measures -31.2..-34.0 dB per qn (996-1014). The master rises from -38.3 to -31.4 dB at 441, the loudest point between bar 131 and the trio, in a passage marked ppp/pp. In the delivered mp3, bars 147-148 reach -18.3 LUFS momentary max. The trio's f bars 197-200 deliver at -20.2 LUFS median. The same peak is in every render since c00 (master at 441: -31.4..-33.1 dB).
- **Clarinet 1, bar 158 (the dolce trio tune).** It reaches -31.8..-32.7 dB at 472-473, +11.4 dB over the line before it. That equals Clarinet 1 at the fff summit (-30.4..-34.5 dB per 2 qn). The master's bar 158 is the loudest of bars 153-168 (473: -30.4 dB against about -37.5 dB around it).
- **The others.** Bars 155 and 159 rise +5.8 / +5.2 dB, Horn 3 at 1028 +8.1 dB (to -36.6, within 3 dB of its coda ff), Violins I at 542 +6.1 dB.

**Cause (read in parts.json and the code).**
- An untargeted crescendo that starts at mp or softer moves `HP_STEP_SOFT` = 22 CC. For Horn 1 at 440 that is CC11 46 -> 68; for Clarinet 1 at 471, CC11 49 -> 70 and CC1 42 -> 64 (both are CC1 dynamic tracks).
- The soft-hairpin dB ramp (`HP_GAIN_SOFT_DB` / `HP_GAIN_SOFT_ACC_DB`, +2.5..3 dB) is added on top. So are the roles (Horn 1 +3 over 420-444) and, on Horn 1, the legato target at v106 with vol +9.2 dB at 442.
- The tool already treats a hairpin of `HP_SHORT_S` (0.6 s) or less as a nuance and caps it at `HP_STEP_SHORT` (6 CC). `HP_SHORT_KINDS` = ("decresc",) applies that cap to decrescendos only. Its comment, "short crescendos keep the full step (no lurch was measured on them)", comes from Movement I. Here the lurch is measured. At quarter 228-264, one quarter lasts 0.23-0.26 s, so every one-beat hairpin is short.

**Fix.**
- In `build/score_config.py`, set `HP_SHORT_KINDS = ("decresc", "cresc")`. This keeps `HP_STEP_SHORT` 6 and the dB ramps. It affects only untargeted hairpins of 0.6 s or less. 83 crescendos of that length exist, and those with a printed target (211 -> 213 ff, 895 -> 897 ff) are unchanged.
- If Horn 1's crest is still above target after the render, add `HP_TARGET_AT["Hn1"][440.0] = "mp"` (the table already holds 618 "mf-") and end its `roles.json` +3 at 438 instead of 444.

**Targets (stems, 0.5 qn windows).**
- Each swell's crest 3-5 dB over the note before it.
- Horn 1 at 441 at or under -35.5 dB, and the master's bar 148 at or under -36 dB.
- Clarinet 1 at 472 at or under -36 dB.
- Horn 3 at 1029.5 at or under -40.5 dB.

### 2. The second idea's crescendos (bars 45 and 121) peak on their accented first note, so the printed < runs flat or backwards (measured)

**Where.** All in the first beat of each phrase, with the arrival one bar later:
- bar 45, qn 132-136-141 (strings f / winds mf, espress., < >);
- bar 121, qn 360-364-369, the sub. p phrase (Violins I and II, espress., < >).

**What a listener hears.** Stem and master level, from the first beat after the onset (+0.1 to +1.1 qn) to the last beat of the hairpin, and to its arrival note:

| | Violins I | Violins II | Violas | Violoncellos | master |
|---|---|---|---|---|---|
| bar 45, end / arrival | -3.2 / -2.8 dB | +0.4 / -3.7 | -3.0 / -5.2 | -3.7 / -3.5 | +0.3 / -0.2 |
| bar 121, end / arrival | -0.5 / +1.4 | -2.9 / -3.6 | | | -1.8 / -0.7 |

At bar 45, Violins I's accented B5 sits at -31.2 / -30.8 dB (132.5-133), and the top of the phrase, the D6 at 136, at -35.1 dB. The winds there do grow (Oboe 1 +9.8, Flute 1 +5.5 dB), so the master stays flat. At bar 121 the phrase after the sub. p falls 1.8 dB across a printed crescendo.

**Cause (parts.json).**
- `accent_fits.json` gives each of these accents the fitter's full 4.5 dB swell: Violins I, Violins II, Violas and celli at 132; Violins I and II at 360.
- In the volume envelope that swell reaches +5.1 dB at 360.97 and decays to +1.4 dB by 362.2. The hairpin's own gain is smaller: `HP_GAIN_SOFT_ACC_DB` 2.5 at 360, and `HP_LOUD_SWELL_DB` 1.5 for strings at 132.
- `ACCENT_MINUS_HPGAIN` already stops an accent from stacking on a crescendo's arrival. Nothing does the same for an accent on the crescendo's first note.

**Fix.**
- Set `build/accent_fits.json` to 1.0 at Violins I 132 and 360, Violins II 132 and 360, Violas 132 and Violoncellos 132. A generic alternative is a new option in `score_to_parts.py`, off by default, that caps a fitted accent swell on a crescendo's first note at that hairpin's dB gain minus 1.
- Give bar 45's strings the shape the winds already have: `LEVEL_SHAPES` on Violins I, Violins II, Violas and Violoncellos `[(133.0, 0.0), (136.0, 2.0), (137.0, 2.0), (141.0, 0.0)]`.
- Re-check the accent's weight against the staccato before it with `fit_accents.py`. The bar-45 accents follow a rest, so their weight comes from the attack, not from a swell.

**Targets.** The arrival notes (136, 364) 2-4 dB over the accented note's body on the lead stems, and the master's < +1.5..+3 dB at both bars.

### 3. The close: Horn 1's last G sharp swells 5 dB after its decrescendo has reached ppp (measured)

**Where.** Horn 1, bars 375-376 (qn 1122-1128). This is one tied note from qn 1101: pp, decrescendo 1113 -> 1122 to ppp, then the fermata alone. This is the pivot note the finale takes up.

**What a listener hears.**
- The decrescendo works: Horn 1 falls from -43.0 dB (1113) to -53.8 dB (1122).
- Then it rises -52.9 (1123), -51.4 (1124), -49.4 (1125), -48.7 (1126): +5.1 dB into the fermata, while the score asks for ppp.
- On the master, bar 376 (-46.1 dB) is held up by the horn alone. c08 is identical.

**Cause.**
- The volume envelope rises +2.5 dB at 1123.25-1124 (7.0 -> 9.5 dB). This is the soft decrescendo's -2.5 dB gain being released. Its release point is `nx = ... default=b2 + 1.0` in the lone-decrescendo branch of `score_to_parts.py`: no onset follows inside the held note, so the release falls one qn after the arrival, in the middle of the note.
- The other +2.7 dB (1124 -> 1126) comes at constant CC1 57, CC11 22 and vol, so it is the sample's own swell.

**Fix.**
- Generic: in that branch, when the decrescendo's arrival lies inside a note that is still sounding, hold the gain to that note's end (no release inside a held note).
- Config fallback: `LEVEL_SHAPES["Horn 1"] = [[(1123.0, 0.0), (1124.0, -2.5), (1126.0, -4.5), (1128.0, -4.5)]]`. The existing end fade, 1127.25 -> 1128, stays.

**Target.** Horn 1 over 1123-1127 within ±1 dB of its 1122 level (-53.8 dB). The master's bar 376 at or under bar 375 minus 1 dB.

**Secondary point, same passage.**
- Horn 1's pp re-entry at bar 368 (qn 1101) lifts the delivered close by +4.3 LU, from -30.3 at bars 364-367 to -26.0 at bars 368-369. The horn there sits 4.3 dB over the Violins I ppp, with role +6 over 1100.25-1128.
- Lowering that role to +3 would leave the horn about 1.3 dB over the violins, the printed pp over ppp. The effect on the master is inferred.
- Critic B owns that balance. I give the arc's side: the ppp close should not rise at bar 368.

### 4. The harp's p espress. line in the F major episode has no hairpins: every note is at velocity 56 and CC11 never moves (measured; manual p.69)

**Where.** Harp (right hand), bars 73-80 (qn 216-240), p espress. The printed hairpins are < 216-219, > 219-222, < 228-236 and > 236-237. Here the harp is the lead over the winds' and horns' pp.

**What is wrong.**
- All 53 notes in 216-240 play at v52-56, at the `VEL_CAP_SPANS` cap of 56 (c04, to keep the harp under the theme).
- CC11 is 110 for the whole movement, and the volume envelope is a constant -3 dB.
- The manual says CC11 and velocity set the Sus RR patch's loudness (p.69). The pipeline uses neither in this span.
- Measured, harp stem per beat: the < 216-219 does rise (-49.9 -> -40.4 dB). The > 219-222 then rises 2.7 dB (-44.0 -> -40.9) and the < 228-236 falls 2.5 dB (-39.1 -> -39.6/-41.2). These are sample differences, not dynamics.

**Fix.**
- In `build/score_config.py`, add the harp family to the soft-hairpin dB ramps: `HP_GAIN_SOFT_DB = {**HP_GAIN_SOFT_DB, "harp": 3.0}`. Every harp hairpin then gets ±2.5 dB (`HP_GAIN_SOFT_ACC_DB`, messa di voce release) in the volume envelope.
- Better for this lead line: list it as `HP_SOFT_EXTRA_SPANS = {"Harp": [(216.0, 240.0)]}` with `HP_SOFT_GAIN_AT = {"Harp": {216.0: 4.0, 228.0: 4.0}}`.
- Keep the velocity cap: it keeps the episode in the p layer, which is right for p.
- Check that the code path accepts family "harp" (it requires `base(a + 0.01) <= 66`, and the harp's lane is 46 here).

**Target (inferred).** On the harp stem, bars 74 and 79 (the crests) 2.5-4 dB over bars 73 and 77, and the > bars falling 2-3 dB.

### 5. The timpani roll of bars 205-208 grows only 2 dB under its printed pp < f, after rising 3 dB with no crescendo printed (measured)

**Where.** Timpani, qn 612-624: a pp roll with a crescendo from 618 into the f stroke at 624, which leads into the trio tune's return at bar 209. Dan's priority 5 is that only a printed crescendo makes a roll grow.

**What is wrong.**

| Timpani stem, per qn | Level |
|---|---|
| 612 -> 617 (no crescendo printed) | -51.3 -> -48.0 dB (+3.3) |
| 618 -> 623 (the printed crescendo) | -43.4 -> -41.2 dB (+2.2) |
| 624, f stroke | -38.7 dB |

- The rolls of bars 101-103 (+6.2 dB), 303 (+7.1) and 332 (+7.0) grow as printed.
- Here the roll trim table falls from pp (+19.0) to f (+7.3) with no hold, because `TIMP_ROLL_TRIM_HOLD_SKIP` = [618]. On top, `LEVEL_SHAPES` cuts a further -3 dB over 621-623.9. Together they cancel the CC1 rise from 56 to 88.
- Both were set in c02, when this roll measured +11.6 dB. The mix and the hall have changed since.
- The rise before 618 comes at constant CC1 56 and vol +16, so it is the roll sample's own build.

**Fix.**
- In `build/score_config.py`, remove `[(620.0, 0.0), (621.0, -3.0), (623.9, -3.0), (624.0, 0.0)]` from `LEVEL_SHAPES["Timpani"]`. Arithmetic on the c09 envelope predicts about +5.2 dB over 618-623.
- Add `[(612.5, 0.0), (617.5, -3.0), (618.5, 0.0)]` to flatten the pp part.
- Alternative: MANUAL-GAPS #7, the recorded crescendo roll row ("Crs") for this one roll.

**Target.** The roll within ±1 dB over 612-617.9, +5..+7 dB over 618-623.9, and at least 2 dB under the loudest string stem until the stroke at 624. The celli and violas measure -36..-38 dB at 622-623.

## Measured and in order (do not touch)

- **Summit.** The fff summit is the loudest moment: master short-term max -12.3 LUFS at bars 336-338, against -14.6..-14.9 for every ff tutti. Delivered -9.9 against -13.9..-14.4, a 4.0 LU margin. The coda builds bar by bar from -28.2 dB (bar 329) to -14.8 dB (bar 337).
- **The tutti sfp at bar 301.** The sf is level with bar 300 (900.0: -15.9 dB), the trough reaches -27.2 at 901.5, and the crescendo rises to -15.8..-14.8 by 908-910.
- **Both sub. p's (360, 828).** They follow a rest, and the hall decays under them with no cut (S3).
- **G.P. and final decay.** Within Dan's limits as rendered in c09.
- **Timpani rolls without a printed crescendo.** The rolls at 384-390 and 852-858 start f and settle 10 dB under the texture. The pp rolls at 708-717 stay flat.
- **Loop pulsing.** No pulsing at the 3.95 s loop period on the held notes. Autocorrelation of level, 100-300 Hz band and spectral centroid at that lag is -0.13..+0.07 on Violins I's G sharp at bars 1-8 and 364-376, the borrowed harmonic E6, Horn 1 at bars 368-376 and the trio horn drone. The re-bow fills work.
- **Delivery.**
  - Delivered -19.8 LUFS, LRA 14.7 LU, span 19.6 dB, limiter 2.7 dB. The master's LRA is 23.2 LU, inside the 21.8-23.5 LU of the recordings in loop/DYNAMICS-RESEARCH.md.
  - Inversions: 0 among 331 five-second moves of 3 dB or more. A median 84% of each move is kept.
  - Long ppp/pp stretches get +11..+13 dB of lift and short p stretches between loud ones +5..+7 dB. So the ppp opening (-28.3 LUFS) delivers louder than the p counterstatement (-29.4) and the p fugato entry (-35.5).
  - I simulated ride trims that undo this (fugato +3, ritmo +2.5, intro -2, close -1.5). They pushed LRA to 15.2 and the span to 20.1 dB, past the brief's 16-19. So I propose no change there.

Do not touch: the summit chain (arrival weight, `RIDE_TRIMS`, `TIMP_DAMP_AT` 1014.5), `FP_SPIKE_FROM_ONSET` and the sfp roles at bar 301, the timpani roll trims and holds on every roll except bars 205-208, the re-bow fills on the held Violins I G sharp, the delivery settings (2.2 / 5.5, lift smoothing 5 s), and the c09 sends and hall.
