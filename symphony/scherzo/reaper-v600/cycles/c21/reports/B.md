# Cycle 21, critic B (balance and levels), on the c20 render

Measured on `cycles/c20/render` (stems and master) and `cycles/c20/scherzo-mockup-c20.mp3`, with the data in `cycles/c20/build_render/`. Stems are compared with `cycles/c18/render`, masters with `cycles/c19/render/00_Master.wav`. Positions are score quarter notes (qn); bar b starts at qn 3(b-1).

Terms:
- "Level" is the A-weighted mean power of a stem (mean of the two channels), in dB on an arbitrary common scale, over a window or over a note's first 0.03-0.5 s ("body"). Differences between stems and renders are what matter.
- "Best band" is c20's measure: over 1/6-octave bands 40 Hz-16 kHz, the line's power against every other stem plus the four returns, averaged over the frames where the line sounds; only bands within 10 dB of the line's strongest band. The master file is excluded from "others" (it sits in the render folder).
- "M" is ffmpeg ebur128 momentary loudness on the mp3; a bar's value is its median M.

Each judgement is marked (m) measured or (i) inferred.

## Manual notes

`loop/MANUAL-READING.md` has no row for c21 ("cycles after c20 pick their own pages"). I read B1's pages 137 and 150-151 of the May 2021 HO manual, because three findings below turn on row volume, velocity layers and volume against expression, and used `loop/MANUAL-GAPS.md`.

| reading (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| Each articulation row has its own volume knob (p.137) | `mix.json` `region_gain_db`: Violins I "Sus Marc LITE" -8 dB (c15), Oboe 1 "Stac DblTng RRx9" vel<75 +3 (c20), Clarinet 1 pitch table | Yes. But a row-wide gain follows any note moved onto that row: Violins I's 999 took the LITE row's -8 dB in c20 (finding 2). |
| Velocity selects the recorded dynamic layer on short instruments; layers sit in fixed velocity ranges (p.150) | Oboe 1 staccato layer 1-74 (the p calls play 42-55) | Yes. The c20 +6 dB on that layer moved its staccatos past the oboe's own sustained notes (finding 4). |
| Volume can raise a softly played section without changing its timbre ("violas played softly can be cranked up"); CC11 shapes the line, CC7 sets each track's ceiling (p.151) | The coda's pp stretto, bars 325-328 | Not done. The entries play at CC11 24-45 with no role, the quietest music in the movement (finding 1). A role row is the volume move the manual describes. |
| MANUAL-GAPS #8, expressive rows for the cantabile lines | The trio tune, Oboe 1's middle part | Not used. No finding needs it this cycle. |
| MANUAL-GAPS #9, half-section patches for Violins II "la metà" | Bars 349-356 | Not needed: the solo leads Flute 1 by 9-10 dB and Violins II by 9-12 dB (m). |

## Answers to the cycle 21 questions (m unless marked)

- **Violins II, bars 179-183.** Closed. Their level rose 5.3-8.2 dB from c18 (bar 177: 9.3 -> 16.0; 179: 8.5 -> 15.8; 181: 7.5 -> 14.9; 183: 5.4 -> 13.6). They now sit 4.8 / 3.0 dB under Violins I and 4.0 / 1.3 dB under the celli in bars 179 / 181, and over both in 183. Their best band is -3.4 / -5.2 / -5.9 in 179 / 181 / 183, because Violins I's doubling lies in the same register. For pp con sord. arpeggios under a p tune, that is the right order. Do not lift them further.
- **Clarinet 1 at beat 640.** Over one-quarter windows, Clarinet 1 reads 22.2 against Violins II 19.9 and Violins I 18.9 (+2.3 / +3.3). In every other beat of bars 209-222 it is 2-10 dB under both. The cause that is left is a hot pitch, F sharp 5 (finding 6).
- **Violas' div. thirds, bars 209-224** (both viola tracks summed). Up 2.5-3.5 dB from c18. They are still 8-11 dB under Violins I (A-weighted), with best band -0.9 / -3.5 / -2.6 / -1.2 / -6.3 in bars 211 / 213 / 215 / 219 / 221. The celli are level with them in their own band. This is acceptable for mf off-beat tenutos under an f tune. Optional: CC11 +6 on Violas and Violas div over 630-648 and 660-672 (`CC11_ADD_SPANS`), which at the violas' measured 0.27 dB per unit gives about +1.6 dB (i).
- **Oboe 1 after the +6 dB layer.** The gain reaches only 25 notes (bars 29-40 and the pp head entry at 273-275).
  - In the unison calls the oboe's staccatos are now a median 2.4 dB under Flute 1's (target about 2). It is not hot anywhere else.
  - Two side effects (finding 4): its accented sustained notes are now far under its own staccatos, and its pp head entry (staccatos 12.3-14.9) sits 5-6 dB over the violas' pp entry at 264 (3.5-9.3) and about level with Violins I's p entry at 282 (13.5-20.5).
- **Per-bar master against c19.** Median 0.0 dB.
  - Over +1.5 dB: bars 23 +4.4, 58 +3.0, 263 +1.8.
  - Under -1.5 dB: 364 -2.5, 290 -2.1, 21 -2.0, 363 -1.8.
  - Also 360 -1.4 and 148 -1.2: Horn 1's CC1 cap on 1077 and 442. It is removed in build/, so these return.
  - Bars 23 and 263 are the Detache pairs (finding 5). Bars 58 and 290 are round robins on unchanged celli data.
- **Role rows by cause** (151 rows).
  - No row is stale under a line with its own role.
  - Two Horn 1 rows do nothing:
    - [756, 864, -1.5] covers only four held doubling notes (816-825);
    - [1020, 1068, -2.5] covers no Horn 1 note.

    Leave or delete them; neither is audible.
  - The coda's pp stretto (972-984) is the only fugato texture without entry rows. The fugato at bar 57 has +5 on each entry (celli [168, 180], violas [180, 192], Violins II [192, 198]); see finding 1.
- **The rest of the lens.**
  - Theme A keeps a best band of +11 to +14 dB over the pizzicato bass and timpani (bars 13-28).
  - In the tuttis the trumpets sit 13-16 dB under the total, the timpani 20-24 and the tuba 21-22. The tenor countermelody (Bassoon 1, Horns 3-4, celli summed) has best band -1.2 / -1.7 in bars 105-108 and +0.9..+4.6 after. At 305-320 it reads +2.1..+6.0.
  - At the summit (qn 1005) Violins I read 36.4 against horns 27.4, trumpets 30.5 and low brass 28.4: 6-9 dB of fff over f/ff, as printed.
  - Solo margins (349-356): Flute 1 -9 to -10, Violins II -9 to -12.
  - Horn 1's motto (357-360) leads by 8.5 dB in its best band, and its last G sharp by 18.0.

## Findings, ranked by what a listener would hear

### 1. Coda, bars 325-328 (qn 972-984): the pp stretto on the theme head is the quietest music in the movement on the mp3 (m)

**Print.** Più mosso. The theme head enters pp in four voices: celli 972, violas 975, Violins II 978, Violins I 981. The crescendo starts at 981, mf at 984, and the build to the fff summit follows.

**Measured.**
- On the mp3, bars 325 / 326 / 327 read -32.9 / -34.5 / -30.1 LUFS M. That is 10 dB under the movement's 10th-percentile bar (-23.7) and 19-20 dB under the integrated -14.1. Only the G.P. (bar 340) is quieter.
- The fugato entries of bars 57-64 read -19.4 to -25.3. The delivery ride is at its +10 dB cap here ("ride max +10.0 dB", metrics.md), so the master's gap passes straight to the mp3. On the master, bars 325-327 read -46.8 / -48.7 / -44.8 against -38.3 to -44.3 for bars 57-64.
- The data:
  - CC11 is celli 27-34, violas 38-45, Violins II 24-36, Violins I 34, with no role on any entry;
  - the fugato's entries play at CC11 37-52 with a +5 dB role each.
- Inside the stretto, the celli's accented half note (975, "Sus MAX", CC11 34) reads -2.4, against 2.1-8.8 for its own staccatos. Its slurred pair 977 / 977.5 reads -3.4 / -3.3. So the subject's crest drops out of the first entry. Violas (978) and Violins II (981) carry the same Sus MAX half note at CC11 45 / 36.
- This is where Dan's note bites ("turn the volume ... to almost max ... especially in quiet parts").

**Fix** (`build/roles.json`, slow class, phrase-length rows like the fugato's; the printed pp stays in CC11, as p.151 describes):
- Violoncellos [972, 981, +4];
- Violas [975, 981, +4];
- Violins II [978, 981, +4];
- each opening to 0 over the printed crescendo 981-984 (the c06 rule for role edges). Violins II's existing [985, 995.5, -7] then starts from 0, not +4.

Instrument-side companion: `CC11_ADD_SPANS` +8 on the three Sus MAX half notes of the stretto (celli 974.9-977.0, violas 977.9-980.0, Violins II 980.9-983.0). That is about +2-4 dB at 0.27-0.48 dB per unit (c18 slopes, i), and it keeps the pp layer (CC11 under 52).

**Expected** (i): master 325-327 about -42..-45, mp3 about -29..-30 M (the ride stays at its cap), the celli's half note level with its staccatos. The build from 981 keeps its range, since its arrival rows at 984+ are unchanged. Check that the summit still leads by at least 0.5 LU.

### 2. Coda build, bar 333 (qn 999): Violins I's accented G6 took the "Sus Marc LITE" row's -8 dB, and the theme is now level with the horns and trumpets (m)

**Measured.**
- c20 moved 999 to "Sus Marc LITE" (`ART_SPANS`, C20_V999 "marc"). `mix.json` gives that row `row_db` -8.0 for every note (c15, set for the soft theme-head halves), so this ff note lost 8 dB at the row.
- Body 26.7 at CC11 101. The fff Sus MAX note at 1010 (same register) reads 35.4.
- Violins I per bar: 332 32.9, **333 27.1**, 334 33.3.
- In bar 333 the horns read 28.0 and the trumpets 27.9, level with the theme. The woodwinds read 33.7.
- c20's own reading: 999 against its staccatos -2.6 (c19, Sus MAX) -> -4.9 (c20, LITE).
- 999 is the only Violins I note at pitch 91 on either row (data checked).

**Fix** (`build/score_config.py`, `build/mix.json`):
- Put 999 back on "Sus MAX": set `_C20_V999` to "none", or delete the ART_SPANS entry.
- Add a Violins I `region_gain_db` entry {"rows": ["Sus MAX"], "pitch_db": {"91": 4.0}}. It touches only this note, and region volumes above 1.0 already work (Oboe 1's +3 layer).
- Target: 999 +1 to +2 dB over its staccatos (c19 -2.6, +4 gives about +1.4, i), and Violins I's bar 333 within 2 dB of bars 332 / 334, 4-6 dB over the brass.
- Do not use velocity: the 1st Violins Sus MAX groups follow CC11, not velocity (c20 `records/velocity_paths.txt`).

### 3. Trio, bars 181-184 (qn 540-551): Bassoon 2's p bass note swells about 10 dB, with no hairpin, over the end of the tune (m)

**Print.** Bassoon 2 doubles the basses: pp tenutos from 504, a crescendo 528-540, then **p** held F sharp 2 (540) and B2 (546) to 551. Over it, the celli's tune and Violins I end with a decrescendo (546, 549.5), and Flute 1 answers p (547-549).

**Measured** (per quarter):
- Bassoon 2 rises 7.8 -> 16.7 over 542-544 and 8.6 -> 18.4 over 546-550.
- At 549 / 550 it reads 17.8 / 18.4, against celli 10.7 / 6.0 and Violins I 4.2 / 1.9: the loudest stem with Flute 1, 7-16 dB over the tune it accompanies.
- c18 reads the same to 0.1 dB, so it is not a round robin.
- Over 544-551 the envelope falls (vol 2.5 -> 0), so the rise comes from CC11 46 -> 60 (540.6-549.5, then 46 at 551) and CC1 56 -> 63.

**Cause** (m on the data, `tools/score_to_parts.py` PHRASE_SHAPE):
- Bassoon 2's notes 504-551 form one phrase (no gap over 0.25 s), about 12 s long.
- It passes both "build" tests: the printed level rises pp -> p (10 units or more), and the 528-540 crescendo ends after 75 % of the phrase.
- The type test runs before the lyric-span test, so the trio's span does not protect it. A build enters at -12, peaks at +10 x 1.4 (wind scale) at 0.95 of the phrase, with no taper. Inside the hairpin the shape is faded out (ps_weight), so the whole climb happens after the arrival, on the held notes.

**Fix** (generic option in `tools/score_to_parts.py`, value in `build/score_config.py` PHRASE_SHAPE["types"]):
- add `"build_end_s": 1.5`: a phrase is a build only if its crescendo's arrival lies within 1.5 s of the phrase end;
- with `"build_rise_lyric": False`, the printed-rise test does not apply inside `lyric_spans`.

Bassoon 2's trio phrase then takes the lyric arch at p (+10 x 1.4 at 0.45 of the phrase, tapering to -12 at the end). Print the per-track `ps_kinds` before and after, and list every phrase that changes type. Other long accompaniment phrases in the trio and the second idea may have the same build, and this scan found only this one swell over 6 dB outside the soft string attacks.

**Expected** (i): Bassoon 2 at 546-550 about 8-11, 3-6 dB under the celli's last notes. No envelope change.

### 4. Counterstatement and retransition: Oboe 1's accented sustained notes now sit 7-15 dB under its own staccatos (m)

**Measured** (bodies; c18 -> c20):
- Bars 37-38: staccato 110 16.4 -> 22.4; the accented B5 at 111 ("Sus MAX", CC11 51) 7.8 -> 7.6. The accent is now **14.8 dB under** the staccato before it, and 10.1 dB under Flute 1's unison B5 (17.7). Per half-quarter the B5 stays 4.2-9.3 for its whole length.
- Bars 92-93, pp head entry: staccatos 12.3-14.9; the accented D5 at 276 (head of a "Leg Slur MAX" slur, CC11 46) 6.6, falling to 3.5; the slurred pair 278 / 278.5 2.2 / 2.7.
- The same figure's accented notes on "Sus MAX" at 87 and 99 (CC11 46) read 14.4 and 12.3, level with their staccatos.
- B5 at fff (1005, Sus MAX) reads 28.0, level with its neighbours. So the B5 is weak only in the p layer.

**Fix** (instrument side):
- 276: `ART_AT` Oboe 1 276.0 -> "Sus MAX", as on 87 and 99 (the slurred 278 / 278.5 follow on Leg Slur MAX).
- 111: `CC11_ADD_SPANS` Oboe 1 (110.95, 112.9, +10, +10). Measure the stem: if the oboe's p-layer slope is under 0.3 dB per unit, move 111 to "Leg Slur MAX" as the head of the 111-113.5 slur instead.
- Optional, for the pp entry: `VEL_SET` Oboe 1 273-275 velocity 42 -> 34 (same 1-74 layer), to put the pp entry under Violins I's p entry. Measure it, since the layer's velocity curve has not been read.
- Target: each accented sustained note within 0 to +2 dB of the staccato before it (Dan's accent range).

### 5. Theme head, every Violins I Detache pair: the notes after the pair rose 2-12 dB, so the crest arrives a beat early (m; cause i)

**Measured** (first 0.25 s, c18 -> c20). Notes before the pair are unchanged; the pair itself rose as intended. The landing staccato after the pair rose in all 18 pairs:
- 68: 24 -> 29;
- 114: 21 -> 27;
- 318: 28 -> 33;
- 788: 30 -> 32;
- 1002: 33 -> 35;
- median about +4.

The note after that rose too:
- 115: 14 -> 23;
- 127: 15 -> 27;
- 349: 22 -> 29;
- 823: 14 -> 24.

In bar 23 (crescendo 66-69 onto the accented 69), the landing 68 now reads 30.4 against 25.3 for the accent (c18: 27.3 / 27.4). In bar 263, 788 reads 32 against 26 for 789. The master's +4.4 / +1.8 in bars 23 / 263 comes from this.

**Cause** (i): the Detache notes are written 0.52-0.55 qn, over their 0.5 qn slot, and Violins I's `sus_release_cap_ms` covers "Sus MAX" and "Sus Marc LITE" but not "Detache". The pair's release trails therefore ring under the next two notes, as Violins II's 749 ms "Stac RRx9" trails did before c20.

**Fix** (`build/mix.json` Violins I `sus_release_cap_ms`, and `build/score_config.py`):
- add {"ms": 150, "rows": ["Detache"], "any_dyn": true};
- end the Detache pair notes at their written length (no overlap into the landing note).
- Target: the landing notes back within 1 dB of c18, and in bars 23 / 263 the accented note at or above the landing note.
- Critic A owns the pairs' articulation; this is their level effect on the line.

### 6. Clarinet 1's F sharp 5 is a hot pitch (+2 to +6 dB at p-mf), the main cause left at beat 640 (m)

**Measured** (bodies against the neighbouring notes, Clarinet 1 "Leg Slur Rep"):
- 472 (p, trio tune) 21.7 against 19.3 / 17.8;
- 488 (p) 21.4 against 22.3 / 18.9;
- 640 (mf) 22.9 against 19.4 / 16.5;
- 656 (mf) 20.2 against 20.9 / 17.7;
- 987 (p) 24.0 against 23.4 / 25.1;
- 210 (f) 18.4 against 20.7 / 13.9;
- median about +2.

At 640 the CC11 crest of the one-beat hairpin is 4 units (76 -> 80) and CC1 is 72, flat against the bar. `mix.json`'s Clarinet 1 `pitch_db` table has no entry for 78. LEARNINGS section 13 lists the clarinet's G5 as +10, the next semitone up.

**Fix** (`build/mix.json` Clarinet 1 `region_gain_db` pitch_db): add "78": -2.5. Expected: beat 640 about level with Violins II and 1 dB over Violins I (i). Bar 214 then comes down to Violins I's own weak portamento arrival (640: 20.4 against 25-27 for its neighbours), which is critic A's. At f/ff (210, 894, 1001) the note loses 2.5 dB inside tuttis where it doubles.

## Do not touch

- The -14 LUFS delivery with its ride rows: summit leads by 0.7 LU, LRA 12.3, crescendo arrivals unchanged.
- Violins II's trio CC11 lift (169-184).
- The deleted violas rows (209-224).
- Oboe 1's staccato layer gain for the unison calls (median now 2.4 dB under Flute 1).
- Theme A's margins.
- The fugato entry rows.
- The tutti countermelody rows.
- The summit's string-over-brass order.
- The solo's and Horn 1's margins in 349-376.
- The timpani's levels in the tuttis and the coda.
