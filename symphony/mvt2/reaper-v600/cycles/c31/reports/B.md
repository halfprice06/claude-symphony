# Cycle 31, critic B: balance and levels (on the c30 render)

**How the levels were measured**
- Frames: K-weighted (BS.1770 pre-filter applied in the frequency domain), ungated, summed over both channels, 4096-point Hann frames every 50 ms, on the final (stem-fixed) stems in `cycles/c30/render/`. On this scale the master's integrated level is -24.1, against -21.4 LUFS gated. The same frames were computed for `cycles/c29/render/` to compare before and after the c30 CC1 change.
- Time base: frames averaged per qn (or 0.25 qn) on the tempo map of `cycles/c30/rendered_build/parts.json`. CC lanes were read there; vol_db was read in `build/parts.json` (it holds the stem-fix note trims).
- Note bodies: from onset + 0.12-0.18 s to 0.05 s before the note's end. "Accompaniment" means the power sum of every other stem.
- Tilt: the 2-5 kHz band level minus the 500-2000 Hz band level.
- Labels: "measured" means a number from the render, parts.json or a table. "Inferred" means a judgement about what a listener hears.

## Manual notes (B4: May 2021 HO manual pp. 49-52, 202-204, 208; `loop/MANUAL-GAPS.md` read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.49 §2.5.2: output configurations (Stereo, 5.1, multi-output 16 x stereo). | All 32 tracks: one Opus instance each, stereo out, mics mixed inside Opus (`mix.json` `mics`). | Yes. Per-mic balance is set inside Opus. No balance problem below needs separate mic outputs. |
| p.49 §2.5.3: "Load with Effects off", so the reverb can be replaced by one shared reverb on an FX bus. | The shared true-stereo hall: each patch's reverb is replaced by `reverb.from_patch`, with pre-fader per-mic sends (`send_pre_fader`). | Yes in effect: one hall for every track, fed inside each instance. As a result, CC7/CC11 act before the hall and the REAPER envelope acts after it (S3). Every fix below is either a slow ramp or a step on an onset. |
| pp.50-51 §2.5.5: multi-outputs that route each mic to its own DAW channel, with sends to a reverb bus. | Would allow per-mic automation (for example less Close on a solo in a tutti). | Not used. No finding here needs it. It is memory-neutral, but it would add 4-5 REAPER channels per track. |
| p.52 §2.5.6: multi-timbral instances, up to 16 parts per instance. | None. | Not used (one instance per track). This has no effect on balance. |
| p.202: Dynamics inserts (De-Esser; Level Amp: fixed-ratio compression with automatic make-up gain). | Per-track dynamics. | Not used, which is correct. A Level Amp on a track would flatten the printed pp/p/mf steps that this lens checks. The delivery compression is in `tools/deliver_master.py` (ratio 2.2, limiter 1.3 dB in c30). |
| p.203: Limiter (ceiling -24..0 dB, release 1-400 ms) and Limiting Amp. | Track and bus peaks. | Not used per track. No stem clips: the master's sample peak is 0.766. |
| p.204: SSL Bus Compressor (2:1/4:1/20:1, attack 0.1-30 ms, release 0.1-1.2 s or Auto). | The master bus. | Not used. The delivery master's slow ride does the bus work. Correct for a mockup whose levels must follow the printed dynamics. |
| p.208: SSL Transient Shaper. "Invert" softens an attack: it "subtracts" the attack, "Good for getting body (sustain)". | Accent fronts (BRIEF item 9). | Not used. The accents use `GENTLE_ACCENT` volume swells, and Trombone 1's ff fronts measure 2-5 kHz -4..-17 dB under the body (c30). No balance finding below is a transient problem. |

The B4 question was whether a level problem would be better solved by a mic, row or controller change than by envelope trims. Finding 1 is a case for a controller change (the CC1 path). Findings 2-6 are pitch- or sample-specific levels, where trims and shapes are the right tool.

## 1. Horn 1, bars 54-55 and 69: a slow CC1 sweep through 30-50 inside a held note makes a 5-14 dB hole. In bar 69 the solo horn sinks under the bassoons and the 4-soli bass pedal (measured)

**Where.**
- Horn 1, B flat 3 at qn 232-238 (bar 69). The score: mp > pp tied, "1. solo, dolce", against Bassoon 1-2 pp.
- Horn 1, B flat 4 at qn 178-182 (bars 54-55). The score: the pp < mp "espr." counter-melody.

**Evidence (measured).**
- **Bar 69, 0.25-qn means.** The level falls through the decrescendo, then climbs back while the printed level is flat:

  | qn | CC1 | c29 (dB) | c30 (dB) |
  |---|---|---|---|
  | 232.0 | 42 | -39.1 | -38.8 |
  | 233.0 | 37 | -40.2 | -45.4 |
  | 234.0 | 33 | -41.8 | -53.5 |
  | 235.0 | 28 (held) | -43.8 | -49.5 |
  | 236.0 | 28 | -42.8 | -43.8 |

  - From 235 on, CC11 holds 37 and CC1 holds 28, yet the level climbs back 10 dB.
  - vol_db falls only smoothly over this span (3.5 -> 2.0 dB), and the soft trim rises toward pp. The hole comes from the sample crossfade.
  - It is new in c30: c29 (CC1 61-65) fell a smooth 4.7 dB.
- **Bar 69, against the other stems (1-qn means).**
  - Horn 1 measures -47.8 / -52.2 at 233 / 234.
  - Bassoon 1 (pp) measures -43.2 / -44.4, and Bassoon 2 -44.6 / -46.2.
  - Over 2 qn the Cb 4-soli pedal measures -47.5 against Horn 1's -49.3.
  - Horn 1 is 8-11 dB under its accompaniment for two beats.
- **Bars 54-55.** In a crescendo (CC1 37 -> 54) the level falls from -36.4 (178.25) to -40.9 (180.5), then rises to -31.4 at 182. That is a reversed crescendo for two beats. c29 rose steadily from -39.2 to -30.6.
- **Scan of every held CC1_DYN note.** Of all held notes whose CC1 path crosses 30-50, only these two dip by more than 4 dB. The next is Horns 1-2 a2 at 271 (3.6 dB). Notes that sit at one CC1 value inside the band show no dip.
- **Manual.** p.101 says all four layers play at once and the Mod Wheel crossfades them, "to create a realistic crescendo and/or decrescendo during a held note". On 1FH the slow pp/mf crossfade loses level in the middle.

**Fix.**
- Do not sweep CC1 slowly through the pp/mf crossfade inside one held note. Carry that part of the hairpin in CC11 and the volume envelope instead.
- New generic option in `tools/score_to_parts.py`, default empty: `CC1_SPANS = {track: [(from_qn, to_qn, cc1)]}`. It overrides `CC1_DYN_MAP` inside the span, with CC1 stepping at the span's start, which must be a note onset.
- Movement II values in `build/score_config.py`:
  - `CC1_SPANS = {"Horn 1": [(232.0, 238.3, 28), (178.0, 182.0, 54)]}`.
  - The B flat 3 then plays the pp layer from its onset, and the decrescendo is CC11 49 -> 37 plus the envelope.
  - The B flat 4 plays the mf layer from its onset, and its crescendo is CC11 50 -> 66 plus the envelope.
- Bar 69 level: `LEVEL_SHAPES["Horn 1"] += [[(232.0, 0.0), (232.3, 2.5), (234.5, 2.0), (236.0, 0.0)]]`. This is a slow ramp inside the note, so the hall tail is unaffected (S3). It keeps the horn over the pp bassoons until the pp arrival.
- Note trim 178 (+3.5): fitted against the dip in c30. Set it to 0 and re-measure; the crescendo must rise by at least 3 dB from 178.25 to 181.75.
- Pass checks:
  - No dip over 2 dB inside either note.
  - Horn 1 at least 1 dB over Bassoon 1 from 232 to 235, and level with it from 236.
- Inferred: the hole is audible as the solo horn dropping out in mid-note. It is the only exposed horn solo in the retransition.

## 2. Coda, bars 87-89 (qn 286-292): Clarinet 1's second phrase lost 4 dB in c30 and is now under its accompaniment, while the held C5 at 292 rose 5 dB over it. Horn 4 is the loudest note of the con sord. chord (measured)

**Where.**
- Clarinet 1, "1." pp after the breath: D flat 5 at 286, D flat 5 tenuto at 289, C5 at 292 (tied, into the morendo).
- The other lines: cor anglais pp dolce (the co-line in bars 87-88); Horns 3-4 con sord. pp; strings pp.

**Evidence (measured).**
- **Note bodies, c29 -> c30.**
  - 286: -37.9 -> -41.8.
  - 289: -40.1 -> -44.2.
  - 292: -43.3 -> -38.6.
  - CC1 is 28 on all three (the Clarinet KS Master's p layer), and CC11 and vol_db are unchanged. The p layer is weak on D flat 5 and strong on C5. The first phrase (280-285, E flat 5 / D5) kept its c29 level.
- **1-qn margins at 286-291.** Clarinet 1 is 1.1-4.8 dB under the whole accompaniment (c29: +0.3..+2.8). It is only -0.3..+3.2 dB over the loudest single stem: the cor anglais -44.1 at 287 and -44.5 at 290.
- **Shape.** The phrase now rises 5-8 dB into its tied last note instead of leading to it.
- **Horn 4 against Horn 3.** In the pp chord, Horn 4 (F3 / F flat 3 / E flat 3) measures -46.7 / -48.8 / -49.6 against Horn 3's A flat 3 at -52.7 / -52.8. Horn 4 is 4-6 dB over Horn 3, and is the second or third loudest stem in bars 87-90. In c30 the pp layer moved both horns, and the low pitches came out louder.

**Fix.**
- `build/note_trims.json` Clarinet 1: add `"286": 4, "289": 4, "292": -4`. The coda roles stay.
- `build/roles.json` Horn 4: change [286,298,-1] to [286,298,-4].
- Level only, so `stem_fix.py` can do it.
- Simulated on the c30 stems:
  - Clarinet 1 at 286-291 measures -37.0..-40.9. That is -0.4..+4.9 dB over the whole accompaniment and +3.7..+11.2 dB over the loudest stem.
  - 292 measures -40.1, just under the phrase.
  - The first phrase is unchanged (+5..+11 dB).

## 3. Horn 1, bars 9-10 and 13-14: on the new layers the low phrase-end notes sit 4-6 dB under their neighbours. The p solo is 2-4 dB under its pp accompaniment at qn 24-26 and 39-41 (measured)

**Where.** Horn 1's theme ("dolce espr.", p, mp crest at bar 12). The accompaniment: bass clarinet, Bassoons 1-2 (pp) and harp (pp).

**Evidence (measured).**
- **Residuals.** Note body against the median of its ±2 neighbours, c30 (c29 in brackets):

  | qn | pitch | c30 | c29 |
  |---|---|---|---|
  | 18 | A flat 3 | -5.8 | -2.9 |
  | 24 | C4 | -4.9 | -1.7 |
  | 26 | A flat 3 | -3.8 | -0.7 |
  | 30 | A flat 3 | -5.6 | -2.1 |
  | 36 | G4 | -5.4 | -0.7 |
  | 38 | C4 | -4.6 | -1.4 |

  The c30 trims at 27 and 39 (+4) and 37.5 (-4) were applied; E flat 4 / D flat 4 at 37-37.5 remain +4.1 / +5.5.
- **Margins (1 qn).**

  | qn | Horn 1 | Nearest stem | Over that stem | Over whole accompaniment |
  |---|---|---|---|---|
  | 24 | -44.5 | Bassoon 1 -44.8 | +0.3 | -4.2 |
  | 25 | -43.5 | bass clarinet -44.8 | +1.3 | -2.4 |
  | 26 | -45.0 | harp -44.8 | -0.1 | -3.6 |
  | 40 | -42.6 | bass clarinet -44.2 | +1.6 | -2.2 |
  | 41 | -42.8 | bass clarinet -44.3 | +1.5 | -0.8 |

  c29 had +2.3 over the accompaniment at 40 and -0.3 at 26.
- **Stale trim.** `pitch_trims.json` Horn 1 `"60": -2` (C4) dates from the old layers.

**Fix.**
- `build/note_trims.json` Horn 1: add `"18": 3, "24": 3, "26": 3, "30": 4, "36": 3, "38": 3` (joined notes: the 0.25 qn ramp-in).
- `build/roles.json`: add Bassoon 1 [23.5, 28.5, -2] and Bass clarinet [38.5, 42, -2]. Following the kit rule, the accompaniment is lowered rather than the crest raised.
- Simulated with the note trims alone: Horn 1 is +2.3..+3.6 dB over the loudest stem at 24-27 and +1.5..+3.9 at 39-41. With the two roles it is about +3.5..+5 dB over the loudest stem, back to c29's shape.
- Level only, so it can be done by stem fix.

## 4. Bar 77, qn 257: Bassoon 2's E flat 3 swells 8-10 dB inside the note and is the loudest stem under the violins' top note (measured; the same in c29)

**Where.** Bassoon 2, E flat 3 at 256-258 (p < f into bar 78) under Violins I's E flat 6 at 257, the top of the A' theme. Bassoon 1 doubles the celli's cantabile in bars 75-77.

**Evidence (measured).**
- **Bassoon 2, 0.25-qn means.**
  - First half of the note: 256.25 -35.6, 256.5 -35.4, 256.75 -37.8.
  - The swell: 257.25 -28.4 and 257.5 -27.7.
  - Over the same span vol_db rises only 1.0 dB (2.0 -> 3.0) and CC11 rises 79 -> 82. The swell is in the sample. The c29 values are identical.
- **Against Violins I.** Violins I's 1-qn mean at 257 is -29.8, so Bassoon 2 is up to 2 dB over the theme's crest.
- **The pitch trim does not cause it.** The +6 E flat 3 pitch trim already skips 256 (`_skip_onsets`).
- **Bassoon 1 (optional).** It sits 0.5-2.3 dB over the celli it doubles at 255-256 (-33.3 / -32.9 against -33.8 / -35.2).

**Fix.**
- `build/score_config.py`: `LEVEL_SHAPES["Bassoon 2"] = LEVEL_SHAPES.get("Bassoon 2", []) + [[(256.9, 0.0), (257.15, -7.0), (257.85, -7.0), (258.05, 0.0)]]`. These are 0.3 s ramps inside the note, so the hall tail is unaffected.
- Inferred result: Bassoon 2 at about -35 through the note, 5 dB under the violins' crest. The f arrival at 259 (-28.9) then grows out of it.
- Optional: Bassoon 1 role [252.5, 257, -2], so the doubling sits inside the cello line.

## 5. Bars 3-6: Clarinet 2 lost 4-8 dB in c30. Its F flat 3 at bar 5 is 11-13 dB under the chord, and the bass clarinet pedal is again the loudest stem (measured)

**Where.**
- Clarinet 2 pp: E flat 3 (6), F flat 3 (12), E flat 3 (15).
- The rest of the chord: bass clarinet pp pedal; Horns 3-4 pp, with Horn 3's C-D flat-C.

**Evidence (measured).**
- **Note bodies, c29 -> c30.** 6: -41.3 -> -46.1; 12: -45.3 -> -53.3; 15: -41.6 -> -45.7. CC1 went from 60 to 28.
- **At qn 12-15.** Clarinet 2 measures -52.6..-53.6, Horn 3's D flat -39.8..-41.7, and the bass clarinet -41.8..-43.3.
  - The F flat is the colour note of the bar (with Horn 3's D flat), and it disappears.
- **Master.** Bars 3-5 are 1.0-2.4 dB softer than c29. The bass clarinet is the loudest stem at qn 6-11 and 15-16, although it already carries roles of -1 to -7 dB here.

**Fix.**
- `build/note_trims.json`: new entry Clarinet 2 `{"6": 3, "12": 7, "15": 3}`.
- Simulated (with +4 instead of +3 on 6 and 15): Clarinet 2 measures -40.8..-44.4 against the bass clarinet's -42.6..-46.4. With +3 it sits about level with the bass clarinet, as in c29. At 12-15 the F flat measures about -46, under Horn 3's motif and audible in the chord.
- Level only.

## 6. Bars 61-62: Violins II still covers the ff tune at qn 206, and Horn 1's A flat 4 at 210 rose 3.4 dB in c30 (measured; the Violins II part was deferred by c30)

**Evidence (measured, 1-qn means).**
- **qn 206.** Violins II measures -20.4 against Violins I -22.4. The Violins II role [204,212,2] is still in place.
- **qn 210.** Horn 1 measures -20.8 against Violins I -19.1. On the c29 render it was -23.9.
  - Horn 1's ff layer (CC1 108) carries the `"68": 3` pitch trim, which was set on the soft layers.
- **Not covering.**
  - The low brass (Trombone 2 -22.5..-25.1, bass trombone, tuba) stay 10-15 dB under Violins I in 2-5 kHz.
  - The timpani measure -30..-37, 8-17 dB under every string section.
  - The climax order holds: master bars 61-62 -12.0 / -11.9 against bars 79-80 -14.2 / -14.9.

**Fix.**
- `build/roles.json` Violins II: change [204,212,2] to [204,212,0].
- `build/pitch_trims.json` Horn 1: add 210 to `_skip_onsets`.
- Simulated: Violins I is level with Violins II at 206 and 4.7 dB over Horn 1 at 210. At 210 the next stem is then the basses (-22.3, so +3.2).
- c30 B #2's Violins I fill (+2 on 205.949) is still the way to put the tune on top at 206.

## Checks asked for in this lens

- **Solos over their accompaniment** (1-qn margins over the whole accompaniment, then over the loudest single stem; measured):
  - Horn 1, bars 7-14: -4.2..+7.9 / -0.1..+12.0. See finding 3.
  - Oboe 1, bars 15-16: +0.4..+6.7 / +4.7..+8.8.
  - Solo violin, bars 17-18: +2.3..+9.9 / +5.5..+14.5.
  - Oboe 1, bars 19-20: -2.1..+9.2 / +1.7..+11.9.
  - Solo violin, bars 21-22: -3.5..+6.2 / +0.8..+10.1. The low end of both ranges is at the phrase end, qn 64.
  - Bass clarinet, bars 31-36: -2.1..+9.4. Its entry and the cor anglais answer at 98 are the low points.
  - Flute 1, bars 37-40: +2.3..+7.6.
  - Cor anglais, bars 41-44: +2.2..+10.3.
  - Oboe 1, bars 45-47: -0.4..+4.8 / +5.1..+10.9.
  - Cor anglais, bars 47-50: +0.1..+8.9 / +3.3..+13.9.
  - Clarinet 1, coda: +1.3..+11.3 at 280-285, and see finding 2 for 286-291.
- **Dynamic mapping between families (measured).** Median note body at printed pp:
  - Clarinet 2 -45.8, bass clarinet -46.6, Bassoon 1 -45.4, Bassoon 2 -46.8, contrabassoon -47.6.
  - Horn 3 -47.1, Horn 4 -48.8, timpani -47.2, harp -47.2.
  - Violins I -46.8, Violins II -45.3, violas -46.1, celli -45.9, basses -48.2.
  - So pp is within about ±1.5 dB across families. The pp -> p step is 5-9 dB on the strings and bassoons and 4.6 dB on the violas. c30 B #6's concern (1.7 dB) does not hold on this measure, so no action.
  - At ppp, Violins II and violas (-56 / -60) sit 7-10 dB under Violins I and the celli (-47.5 / -49). This is mostly the final chord, where those two sections are muted and the violas divided. Not acted on.
- **Divisi and soli tracks (measured).**
  - Violins II div: 4-7 dB under the Violins II in bars 37-40. Both are pp sul tasto under Flute 1, which stays 9-11 dB over them.
  - Violas div: level with the violas in bars 23-28, 80-81 and the coda.
  - Violoncellos div: level with the celli.
  - The Cb 4 soli (bars 65-70, -46.5..-49) sit under Horn 1 except in bar 69 (finding 1).
  - In the coda the muted, divided violas sit 5-8 dB under the unmuted celli. This is acceptable.
- **Bass (measured).**
  - The 20-100 Hz share of the master is -12..-38 dB per bar. The highest values are in bars 31 / 35 (contrabassoon pedal, -9.7 / -9.5) and bars 83-84 (-9.6 / -9.0, the ppp pedal with the timpani strokes). These are quiet bars, and the share is comparable with the Brahms references.
  - At the climaxes the share is -17..-24 dB.
  - Solid, not boomy.
- **Timpani and low brass at the climaxes (measured).**
  - Bars 79-82: the roll is 6-11 dB under the Flute 1 / Violins I tune.
  - Bars 61-64: see finding 6.
  - Neither covers.
- **S3 (measured on `build/parts.json`).** Every fast vol_db fall of 3 dB or more under a sounding note lies on a fill end point near an onset. All the fixes above are onset steps, slow ramps, or a CC1/CC11 change.

**Do not touch:**
- Trombone 1's quotation level and accents.
- The low brass and timpani levels at both climaxes, and the climax order.
- The bar 81 roll decrescendo, the bars 2-3 and bar 52 roll shapes, and the coda timpani strokes.
- The solo levels of Oboe 1, the solo violin, Flute 1, the cor anglais, and Clarinet 1's first coda phrase (280-285).
- The c30 CC1 layer map itself (the darker soft horns and clarinets). Fix the two within-note crossings and the pitch residuals, not the map.
- The Cb EQ set and loud_eq.
- The Violas Detache level on CC7.
- The niente CC7 lanes.
