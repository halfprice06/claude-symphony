# Cycle 37, critic B: balance and levels (on the c36 render)

**Method.**
- Stems and master from `cycles/c36/render/` (no stem fix in c36). `build/parts.json` is identical to `cycles/c36/rendered_build/parts.json`.
- **Level scale.** K-weighted: the BS.1770 response applied to 4096-point Hann spectra, 25 ms hop, both channels summed, ungated. On this scale the master reads about 3 dB under its gated LUFS. Bands: unweighted 20-100, 100-300, 300-2000 and 2000-5000 Hz from the same frames.
- **Note bodies.** From the score onset + 0.15 s to 0.05 s before the played end.
- **Time base.** Score qn mapped on the parts.json tempo map.
- **Simulations.** dB gain applied to the stem frames, with the master re-summed.
- **Labels.** "Measured" means a number from the render, parts.json or a table. "Inferred" means a judgement about what a listener hears, or a reading of an orchestration book.

## Manual notes (B4: May 2021 HO manual pp. 49-52, 202-204, 208; `loop/MANUAL-GAPS.md` read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.49 **Load with Effects off**: drop each instance's convolution reverb and use a DAW reverb instead. | All 32 instances (`mix.json` `reverb`). | Partly, and that is fine. Each instance keeps its Opus reverb slot, but `build_reaper.py` loads one shared hall IR into every slot at one `fx_volume`, with per-mic sends set per group. The result is the same one-room blend that a shared bus gives. Nothing to change for balance. |
| pp.50-51 **Multi-outputs**: route each mic to its own stereo output, and send each mic to an FX-bus reverb. | Mic balance and depth per family. | Not used. Mic levels and sends are set inside Opus (`mix.json` `mics`, `send`), which reaches the same balance without 5x more REAPER tracks. Splitting the outputs would only matter for a post-Opus EQ on one mic. No finding below needs that. |
| p.52 **Multi-timbral**: up to 16 instruments in one instance. | Memory: 32 instances, 45 GB after the c36 render. | Not used. Samples load per instrument either way, so the memory gain is uncertain (inferred). Not a balance tool. |
| p.202 **Level Amp**: compressor with fixed threshold and ratio and automatic make-up gain. p.203 **Limiter / Limiting Amp**: a hard ceiling with release; a threshold with 0.1-10 ms attack. | Every stem; the delivery chain. | Correctly not used. No dynamics processor runs inside Opus. Levels come from CC11/CC1 (layer and volume), CC7 and the volume envelope, so printed hairpins keep their size. The only limiter is `tools/deliver_master.py`: 2.0 dB on c36's loudest peak (225.7 s, bar 61), under the 3 dB ceiling. |
| p.204 **SSL Bus Compressor**: 2:1/4:1/20:1, attack 0.1-30 ms, release 0.1-1.2 s or Auto. | The master. | Not used. It would shrink the master's 23.9 LU range in place of the delivery ride, which already gives LRA 15.3 and span 18.3 dB. Correctly not used. |
| p.208 **SSL Transient Shaper**: Gain sets transient detection, Amount the added attack; **Invert** subtracts the attack ("softer attack ... body"); Speed sets how long the added attack lasts. | Short level spikes at note fronts: findings 1 and 4 (a legato fill and an f arrival), the harp's plucked chords at bar 76, the coda timpani strokes. | Not used. Invert could soften these fronts on a whole track, but it acts on every note of the track. The spikes below come from per-note fills and samples and are fixed exactly with per-note tables. Keep it as an option only for a track whose every attack is too hard (inferred; none measured this cycle). |

## 1. Bar 73 (qn 245.7-246.5): a legato fill on the celli's counter-melody spikes 10 dB over the violins' theme and lifts the master 5.5 dB, in a p passage (measured)

**Where.** Violoncellos, the C4 at sq 246 (bar 73 beat 3: the top of the "cantabile, sul D" counter-melody's hairpin). The theme is in Violins I/II (p espr., unison an octave apart: 246 = F5/F4 quarter, then the 247 half note).

**Evidence (measured, 0.1 qn frames).**

| qn | Violins I | Violins II | Violoncellos | Master |
|---|---|---|---|---|
| 245.5 | -39.4 | -39.7 | -38.2 | -32.7 |
| 245.7 | -36.4 | -38.9 | **-29.7** | -27.7 |
| 246.0 | -36.6 | -44.2 | -35.6 | -31.2 |
| 246.3 | -38.7 | -39.9 | **-27.6** | **-25.8** |
| 246.4 | -38.8 | -42.5 | -28.6 | -26.6 |
| 246.7 | -38.3 | -38.5 | -35.6 | -30.7 |
| 247.0 | -37.3 | -41.2 | -37.0 | -31.0 |

- The master-bump scan (0.1 s master level against its ±1.2 s median, whole movement) ranks this event with the largest: +5.5 dB at qn 246.40. Only the bar 28 f arrival (+6.0) and the bar 84 timpani stroke (+6.0) are higher, and those two are printed events.
- The cello spike is 6-7 dB over the cello note's own body. The body itself (246.5-247.5: -34.2..-36.7) is still 2-4 dB over Violins I (-37.3..-38.5). So for about 0.6 s the counter-melody covers the theme.
- **Cause (read, `build/*.json` and parts.json vol_db).** Three tables stack on this one note:
  - `early_fills.json` Violoncellos "246": {db 8.0, pre_s 0.29, hold_s 0.35};
  - `note_trims.json` Violoncellos "246": +4;
  - `hpgain` [244, 246, 2.5].
  - vol_db jumps from -2.34 at 245.72 to +5.69 at 245.75, peaks at +8.08 at 246.30, then falls to +2.17 by 246.5. The +8 fill's pre-time puts the first spike (245.7) on the end of the 244 note. The hold carries the second spike past the sample's own arrival at about 246.2.
  - The `roles` row [245.5, 250, -2] takes back only 2 dB.

**Why it matters (inferred).** In a quiet p phrase a cello note jumps out like a misplaced accent. That is about 0.3 s after the beat, so it also reads as a late, pushed arrival. The theme's beat-3 quarter disappears under it.

**Fix (level only).**
- `build/early_fills.json` Violoncellos "246": db 8.0 → 3.0, pre_s 0.29 → 0.12, hold_s 0.35 → 0.2.
- `build/note_trims.json` Violoncellos "246": +4 → +1.
- Expected (estimated from vol_db): the 245.7 and 246.3 spikes fall to about -35 / -33.5, and the body to about -37.5 / -38.5. That is level with Violins I, and the hairpin peak sits 1-2 dB over the body.
- Master in bar 73 about -0.5 dB, a fall inside a sounding legato line: the fill's fall stays at the note front where the transition sample covers it.
- Check after the render: no 0.1 qn frame from 245.6 to 246.6 more than 2 dB over the following body, and no dip at the join deeper than 5 dB (the reason for the fill).

## 2. Bar 61 (qn 204-210): Clarinet 1's held ff F5 swells 5.4 dB inside the sample and becomes the loudest and brightest wind at the climax, over Horn 1 and the oboe on the same F5 (measured)

**Where.** Clarinet 1, sq 204, F5 held 6 qn on Sus Non Vib (CC1 108, CC11 118-122), printed ff with a tenuto and no hairpin. Oboe 1 plays the same F5 (sq 204, ff).

**Evidence (measured, 0.25 qn frames).**
- Clarinet 1 rises from -24.5 (204.5) through -21.6 (206.0) to -19.1 (207.5), then falls back to -23.3 by 208.75.
  - The controllers explain at most 1.5 dB of that rise: vol_db +2.60 → +3.62 and CC11 119 → 122.
  - The rest, about 4 dB, is the sample swelling. This is the same effect as the bass clarinet's A flat 2 pedal (c28, c35).
- **At the peak (207.0-208.0):**
  - Clarinet 1 -19.1..-19.8 against Oboe 1 -23.0..-25.0 on the same pitch;
  - Horn 1 (ff) -20.7..-25.2; Horn 2 and Horn 3 lower.
  - The clarinet's 2-5 kHz rises from -32.5 to -27.3 dB.
- **Over the whole bar (204.2-207.8):**
  - Clarinet 1 is third in the master's 2-5 kHz band (-11.4 dB under the master's band level), behind only Violins I and II.
  - It is ahead of Oboe 2 (-13.8), the violas (-15.3) and every brass part (-20 or lower).
  - On the K scale it is the loudest wind (-21.7), louder than any horn.
- **Control.** At the bar 79-80 ff (262-268) the same track sits at -26.8..-27.3, with 2-5 kHz at -43.6..-45.9. That is level with Oboe 1 (-24.5..-28.7), as a doubling wind should be.
- **Norm.** Rimsky-Korsakov (`reference-books/text/rimsky-principles.txt` l.1966-1972): in forte, a horn equals two clarinets. A clarinet doubling the wind chord should sit under each horn, not 1-5 dB over Horn 1 (inferred).

**Why it matters (inferred).** In the movement's climax a single clarinet tone grows out of the chord on a note with no printed hairpin. Over bar 61 the chord's colour moves from strings-and-horns to a bright reed.

**Fix (pre-hall, so no tail is cut).** `build/score_config.py`:
`CC7_POINTS["Clarinet 1"] = CC7_POINTS.get("Clarinet 1", []) + [(205.0, 127), (205.75, 106), (206.5, 90), (207.0, 80), (208.0, 80), (208.75, 101), (209.5, 113), (209.9, 127)]`
- CC7 is linear amplitude on these KS Masters (series 2 LEARNINGS c29). 106/90/80 are -1.6/-3.0/-4.0 dB, and 101/113 are -2.0/-1.0.
- Expected: Clarinet 1 holds -23.5..-24.5 across 205-209.5, level with Oboe 1 and Horn 1. Its 2-5 kHz share of the master falls about 4 dB at 207-208.
- Master K -0.1 dB, 2-5 kHz -0.6 dB at 207-208. The limiter can only go down.
- Keep c29's role [204, 210, -4] as it is. The new lane flattens the swell; it does not change the note's start level.

## 3. Bars 61-62 (qn 204-212): the brass chord sits 6-8 dB under the string sections, although the horns print ff; at the bar 79 ff the horns sit level with the violins (measured levels; the judgement is inferred)

**Where.** Horns 1-2 (ff), Horn 3 (the "a2 f" line; Horn 4 has no notes here, C #3 of c36), Trombone 2, bass trombone and tuba (all f). Strings ff molto sostenuto.

**Evidence (measured, K scale, 204.2-207.8 / 208.2-211.8).**
- Strings: Violins I -16.6 / -16.1, Violins II -16.1 / -19.2, violas -19.6 / -21.8, celli -18.0 / -18.4.
- Horns: Horn 1 -23.2 / -23.0, Horn 2 -24.2 / -21.3, Horn 3 -26.3 / -24.8.
- Low brass: Trombone 2 -22.1 / -22.3, bass trombone -22.5 / -23.9, tuba -23.4 / -27.3.
- Family sums against the master over 204.1-211.9:
  - strings -2.8, woodwinds -5.8, horns -10.1, low brass -9.9 dB;
  - in 2-5 kHz: strings -0.9, horns -16.9, low brass -16.4.
  - The brass (seven parts) carries about 20% of the climax's energy, the five string sections about 52%.
- **Control: the bar 79-80 ff (262.2-267.8).** Horns 1-2 a2 (printed f) -25.5 against Violins I -24.1 (-1.4 dB). At bar 61, Horn 1 at ff sits 6.6 dB under Violins I.
  - The quieter printed dynamic is therefore placed relatively louder than the louder one.
  - Cause (read): c34 raised the strings +3/+3.5 dB over 204-212 (LEVEL_SHAPES) for the climax order. c36 then kept Horn 1's lift off the front.
- **Norm.**
  - Rimsky-Korsakov (l.1966-1977): in forte a trombone or tuba equals two horns, a horn equals two woodwinds, and one string section equals two woodwinds. So one horn about equals one string section, and a trombone about equals two sections.
  - The composer already prints the trombones and tuba one step under the strings. Rimsky's balance rule (l.1510-1517) is to mark brass one degree differently to balance it.
  - So at f against ff the low brass should sit about level with a string section, not 4-7 dB under it (inferred).
- **Dan's concern (low brass and timpani covering).** It stays met with room to spare. The timpani roll is rank 21-22 of 22, and the loudest brass part would still be 5 dB under Violins I after the fix.

**Why it matters (inferred).** The movement's one Largamente ff sounds like a string climax with a thin brass halo. A listener expects the horn chord and trombones to fill the middle under the violins, as they do (relatively) at bar 79.

**Fix (rises only, so no hall tail is cut).** `build/score_config.py`:
- `LEVEL_SHAPES["Horn 2"]`, `["Horn 3"]`, `["Trombone 2"]`, `["Bass trombone"]`, `["Tuba"]`: each `+ [[(204.0, 0.0), (204.15, 3.0), (211.6, 3.0), (211.9, 0.0)]]`.
  - The bass trombone's sf at 212 (bar 63) is outside the span, which closes before it.
- Horn 1: keep the c36 front shape (do-not-touch) and add +3 only on its lift. In `LEVEL_SHAPES["Horn 1"]` 205.0: +4.5 → +7.5 and 207.75: +4.5 → +7.5, and add the same +3 from 208.0 to 211.6 as a new shape ending at 211.9.
- Take 1 dB back from the c34 string holds: `LEVEL_SHAPES` Violins I and Violins II 3.0 → 2.0, Violoncellos 3.5 → 2.5 (the `[(204.0, 0.0), (204.2, ...), (211.6, ...), (211.9, 0.0)]` rows). The violins stay the loudest stems.
- **Simulated (204.1-211.9).**
  - Master K +0.47 dB mean and +0.36 dB on the loudest frame (limiter about 2.0 → 2.4 dB, under the 3 dB ceiling); 2-5 kHz -0.55 dB; 100-300 Hz +0.8 dB.
  - Relative to the master: Violins I -8.6, Violins II -9.8, celli -10.5, violas -11.7, Horn 1 -11.4, Horn 2 -10.9, Horn 3 -13.7, Trombone 2 -10.5, bass trombone -11.5, tuba -13.4.
  - The climax order improves: bars 61/62 move further over 79/80.
- If the limiter passes 2.7 dB in the stem-fix simulation, use +2.5 on the brass instead of +3.

## 4. Bar 28-29 (qn 82-84): at the f peak of section A, Violins II spike 6-8 dB over the unison Violins I, then the violas' F4 at 83 sits 6-9 dB over both violin sections inside the printed decrescendo (measured)

**Where.**
- Violins I and II in unison: B flat 5 at sq 82 (f, decrescendo), A flat 5 at 83, G5 at 84.
- Violas main half: F4 at sq 83 (printed mf at 82 with a decrescendo), on Leg Slur MAX v69 with c36's `REATTACK_LEAD_AT` 0.12. Then the legato move to E flat 4 at 84 on Leg BC MAX.

**Evidence (measured, 0.1 qn frames).**
- **82.2-82.4.** Violins II -21.4..-22.9 against Violins I -26.7..-30.2.
  - vol_db Violins II +5.7..+5.8 against Violins I +2.9..+3.0. The 2.8 dB difference is `early_fills.json` Violins II "82" {2.8, pre 0.23, hold 0.35}; Violins I has no fill at 82. The rest is the sample.
  - This is the master's largest bump in the movement (+6.0 dB at qn 82.33 against its ±1.2 s median), from one violin section only.
- **Violas 83 F4.** Body -31.3. In 0.1 qn frames: 83.0-83.3 -32.2..-33.9, then 83.4-83.8 -30.1, -29.9, -32.4, -29.8, -27.4 (the peak is the legato transition into 84).
  - Violins I sit at -34.8..-43.7 and Violins II at -29.2..-40.3 over the same frames.
  - The violas' 82 note before it measured -35.0..-41.1, and the 84 target -41.8. So the decrescendo goes up 4-8 dB on beat 2 and then falls 10-14 dB into bar 29.
  - Violas div is silent here: its F4 ends at 83.

**Why it matters (inferred).** The f arrival of section A comes from one section as a bump rather than from both violin sections together. On the next beat an inner viola note covers the melody's falling line, so bar 28's decrescendo reads as a crescendo of the middle voice.

**Fix.**
- `build/early_fills.json` Violins II "82": remove it (or db 2.8 → 0).
  - Expected: Violins II at 82.2-82.4 about -24.2..-25.7, still 2-4 dB over Violins I from the sample, and the master bump about +3.5 dB.
  - Leave Violins I's 83/84 fills alone.
- Violas 83, pre-hall: `CC7_POINTS["Violas"] = CC7_POINTS["Violas"] + [(82.93, 127), (82.98, 64), (83.95, 64), (84.05, 127)]` (64 = -6 dB).
  - The drop falls at the new note's onset (82.90 moved), so the 82 note's tail is not cut after the hall.
  - The return to 127 comes after the 84 target's start, where that note's early fill (+2.4) covers it.
  - Expected: 83 body about -37.3 and transition peak about -33.4, 1-3 dB under Violins II and level with Violins I. 84 unchanged.
  - Check: the Violas CC7 list already holds the c29 Detache lane (152-168); keep both.

## 5. Bars 42-44 (qn 126-136): Flute 1's printed counter-line sits 4-10 dB under the cor anglais and level with the pp accompaniment, so the dialogue the score gives the two winds is mostly lost (measured; judgement inferred)

**Where.** Flute 1 "1." from 126 (pp cresc. → p at 128, decresc. from 131, pp at 136), an octave above the cor anglais' "solo, dolce cantabile" (p → mp at 128). BRIEF: "then cor anglais and flute (41-44) over viola triplets (pizz.)".

**Evidence (note bodies, measured).**
- Flute 1 minus cor anglais: median -5.5, range -2.0 (130) to -10.2 (129).
- Flute 1 against the sum of everything except the cor anglais: median -1.0, range -4.3 to +2.1. Against the loudest other stem (pizz. violas or pp celli): median +1.5, minimum -1.9 (129.5).
- The flute at its printed p (-35.6..-45.6) is 6-11 dB under its own p in bars 37-40 (-31.9..-34.3). That earlier span is a solo with roles, but the dynamic is the same.
- This is after c35's +5 dB on bars 43-44 (B #4). The notes of bar 42 (126-131) did not get it and are the weakest: 129 -10.2, 129.5 -7.0 under the cor anglais.

**Why it matters (inferred).** One printed step under the cor anglais (about 4-5 dB on this mockup's 4.8 dB/step mapping, c36 B) is right. But at 129-129.5 and 133.5 the flute drops into the accompaniment, so the answering line breaks off mid-phrase.

**Fix.** `build/roles.json` "Flute 1": add `[125.75, 131.5, 3, 0.5]`. That covers bar 42 up to the decrescendo; c35's lift already covers 132-136.
- Expected: Flute 1 against the cor anglais about -3 median (129: -7). Against the other accompaniment +2 median, never under the pizz. violas.
- Master under +0.2 dB in bars 42-43.

## Checks asked for in this lens (all measured unless marked inferred)

**Solos over their accompaniment (note bodies).** Each entry gives the median and minimum over the accompaniment sum, then over the loudest single stem.

| Solo | Over accompaniment (median / min) | Over loudest stem (median / min) | Notes |
|---|---|---|---|
| Horn 1, bars 7-14 | +1.6 / -2.1 | +4.9 / +2.1 | One printed step (p over pp) over four parts; lowest at 30 (the harp) |
| Oboe 1, bars 15-16 | +4.8 / +1.1 | +6.6 / +4.7 | |
| Solo violin, bars 17-18 | +4.6 / -1.0 | +8.0 / +3.3 | |
| Oboe 1, bars 19-20 | +4.9 / -1.4 | +7.2 / +2.8 | |
| Solo violin, bars 21-22 | +3.1 / -1.7 | +7.2 / +0.8 | 60: the celli |
| Bass clarinet, bars 31-36 | +3.7 / 0.0 | +5.1 / +2.0 | 98: the cor anglais' entry |
| Flute 1, bars 37-40 | +4.0 / +2.3 | +8.4 / +6.4 | |
| Cor anglais, bars 41-44 | +1.9 / 0.0 | +5.8 / +2.1 | Flute's counter-line: finding 5 |
| Oboe 1, bars 45-47 | +1.9 / -4.5 | +7.1 / +0.1 | 145: the eighth inside the oboe's own line (as in c36) |
| Cor anglais, bars 47-50 | +3.5 / +0.3 | +6.8 / +3.1 | |
| Horn 1, bars 65-70 | +7.9 / -2.5 | +8.8 / +3.2 | |
| Clarinet 1, coda | +0.4 / -2.9 | +4.4 / +1.4 | 286/289: the cor anglais' own pp dolce line, 1.4-1.9 dB under, as c35 set |

- **Melody scan.** I checked the designated melody against every other stem in 0.5 qn windows. Beyond findings 1 and 4, the places where another stem leads by more than 2 dB are all printed or harmonic:
  - the celli moving under held violins in bar 60 and bar 81;
  - Violins II's octave line at 206 (the c09 role);
  - Violins II at 264.5-265.5 (bar 80);
  - the sf at 212;
  - the pickup at 237.

**Climaxes.**
- **Bars 61-62.** Timpani roll rank 21-22 (-19..-22.5 under the master) after its 203 stroke. The low brass is at rank 5-11 and the horns 7-13. Nothing covers. The brass is light (finding 3) and Clarinet 1 swells (finding 2).
- **Bars 63-64.** Trombone 1 leads the next stem by 11-13 dB in bar 63 and 15-20 dB in bar 64 (ff against strings p). The bass trombone's sf → p is 15.6 dB under the master at 213 and 22-25 dB under from 214.
- **Bars 79-82.** No trombones. The timpani roll is at rank 12-20, -16..-19 under the master, falling with its decrescendo. Flute 1 and Violins I lead bar 79 beat 1. Horns 1-2 a2 (f) are 1.4 dB under Violins I, 4-5 dB over Horn 3/4.
- **Climax order (plain RMS, metrics.md).** Bars 61/62 -14.3/-15.0 against 79/80 -19.4/-19.9. Finding 3 widens the gap by about 0.4 dB; findings 1, 2, 4 and 5 move it by under 0.1 dB.

**Dynamic mapping (median note bodies, notes of 0.9 qn or more).**
- pp is consistent across families: winds -43.9..-45.8, Horns 3/4 -46.7/-44.9, strings -43.1..-47.3, harp -43.8.
- p is consistent except:
  - the basses, whose arco p median is about -43, 6 dB under the celli (4-6 dB at every level on this scale, as in c36: K-weighting takes 1-5 dB off their 40-100 Hz fundamentals);
  - the harp under the bars 37-44 solos (-43..-47, the c04 cut).
- The two inversions in the table are explained:
  - Clarinet 1's pp is above its p because the coda solo is its only pp passage.
  - The violas' "mf" bucket is bar 28-29, where finding 4 applies.

**Half-section and 4 soli tracks.**
- Violins II div (Flautando pp) -43.6 against the Violins II half -43.1.
- Violas div against the main half: +1.3 dB median in bars 23-30 and +0.4 dB in the coda (279-304, range -2.4..+5.9). Both are fine.
- Celli 4 soli on the div track (274-286): -46..-50, level with the tutti basses' ppp (-48..-49), as in c36.
- Basses 4 soli in bars 87-92: 5-8 dB under the tutti celli at pp (4 players against a section, an octave lower; inferred right).

**Bass.**
- 40-100 Hz is 77-80% basses. 25-40 Hz is negligible (-43.9 dB of the total).
- The heaviest bars for sub-bass share are:
  - bars 83-84 (-8.2/-8.4 dB against a median of -19), the basses' ppp A flat 1 pedal;
  - bars 31 and 35, the bass clarinet's E flat 2 / F2 fundamentals.
- Neither is a resonance or a mic boom: the bass clarinet's 20-100 Hz is its fundamental, and the pedal is a printed ppp tutti.
- The harmonics' three notes (274-276) reach -45 at the pluck, 5 dB over the pedal, then decay under it within half a beat. That is the harp's physics, and they own the 300-2000 Hz band throughout.
- No change (inferred).

**Gains, soft trims, CC11/velocity.**
- No track's trims produce a family-order error this cycle. The largest remain Bassoon 2 pp +8, the low brass p +7.8 and the basses p +6.5, all checked in c36.
- The level errors found are all per-note tables (fills and trims stacking: findings 1 and 4) or a sample swell (finding 2). None comes from the CC11 map.

**Standing checks inside this lens.**
- **S3.** I scanned every track's vol_db for falls of 3 dB or more within 0.15 qn, under a note sounding for more than 0.4 qn. They fall into three kinds:
  - re-bow fill shapes, where the stem re-attacks;
  - the timpani roll ends before strokes (171.9, 209.4), which the stroke masks;
  - the roll's slow settle (207-208, 1 qn).
- None cuts an audible tail. The fixes above put every new fall in CC7.
- Items 8-9, S1 and S2 are outside balance and were not re-measured.

**Do not touch:**
- the bar 61-62 timpani roll (+5, c36) and its 209.4 release;
- Horn 1's bar 61 front shape (finding 3 adds only on the lift);
- Trombone 1's quotation levels, shapes and CC7 lanes;
- the bar 79-82 timpani roll and its decrescendo;
- the Horns 1-2 a2 level at bars 79-80;
- the coda Clarinet 1 / cor anglais balance (c35);
- the celli 4 soli on the div track and the basses' coda 4 soli level;
- the solo levels in the table above;
- harp env_sustain 1.0 and the harp 253 trim;
- the Cb and timpani side shelves;
- the horn CC1 map and soft-horn loud_eq;
- Clarinet 2's c36 pp/ppp trims;
- the violas' Sus MAX at 81-82 (finding 4 acts only on 83);
- the c29 Violas Detache CC7 lane.
