# Cycle 32, critic B: balance and levels (on the c31 render)

**How the levels were measured.**
- Source: the final (stem-fixed) stems in `cycles/c31/render/`. Time base: the tempo map and vol_db of `build/parts.json` (the c31 stem-fix version).
- Frames: K-weighted (BS.1770 pre-filter applied in the frequency domain), ungated, both channels summed, 4096-point Hann frames every 50 ms. On this scale the master reads about 3 dB under its gated LUFS.
- Note bodies: from onset + 0.15 s to 0.05 s before the note's end. "Accompaniment" is the power sum of every other stem.
- Band levels (unweighted): 20-100 Hz, 500-2000 Hz and 2-5 kHz.
- Labels: **measured** is a number from the render, parts.json, a table or a patch state. **Inferred** is a judgement about what a listener hears.

## Manual notes (B5: May 2021 HO manual pp. 114-115, 154-155, 158-159; `loop/MANUAL-GAPS.md` read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.114 §3.10.1-3.10.2: percussion instrument categories. Orchestral Perc Basics Kit 1: "CC 11 (Expression), and Note Velocity control overall loudness, and Note Velocity controls dynamics (up to 16 levels)". Timpani Felt Long on C0-E1, alternating LH and RH. | The Timpani track (`Timpani Flt KS`, 16 notes). | Partly, and this is not a problem. In the loaded state, 8 layer rescalers sit on cc 1 and one on cc 11 (read in `jobs/19_Timpani_Flt_KS.b64`). The pipeline sends CC7 for level and CC1 for the roll layers (`TIMP_CC1_MAP`), and no CC11. Rolls and strokes follow BRIEF item 5 (below). The kit patches are not needed: v600 has no same-pitch stroke runs. |
| p.115: Kit 2 (bass drum, snares, cymbals, tam-tam and others). | None (v600 has no percussion other than timpani). | n/a |
| p.154 §4.3.5 Humanizer: random note on/off delay of 0-100 ms, velocity up to 50%, tuning, volume 0-100%, pan. | Any track, if it were on. | Not used. No Humanizer or MIDI-tool block is in any of the 32 Opus states in `jobs/` (read). That is correct: a random volume would undo the per-note trims this lens checks. |
| pp.154-155 §4.3.6 MIDI Compressor: threshold, ratio and makeup on velocity or on a CC. | It could narrow the CC11 or velocity range per track. | Not used (read). Correct. Range compression is done after the mix by `deliver_master.py`, so CC11 keeps choosing each printed dynamic's layer. |
| p.155 §4.3.7 MIDI Echo. | None. | n/a |
| p.158 §4.4.1-4.4.2: Automation parameters and macros. | Track level and mic automation. | Not used. Level automation is REAPER's volume envelope, after the hall. CC7/CC11 act before the hall (S3). |
| p.159 §4.4.3: MIDI Controller Mapping: "re-map existing MIDI CC assignments... Be careful to avoid conflicting MIDI CC messages". | The CCs the pipeline sends: 1, 7, 11, 15, 36, 69, 70. | Yes. Every `controllerMap` in the states keeps the default numbers: controller_1 -> 1, 7 -> 7, 11 -> 11, 15 -> 15, and 22/36/64/65/68/69 (read on Violins I, Horn 1 and Timpani). No remap conflicts with a CC the pipeline sends. The timpani map has no CC1 or CC11 entry, but its layer rescalers still read cc 1 (above). |

**MANUAL-GAPS.** No item in it bears on the findings below, except #8 (half-section patches for the 4 soli), which is behind finding 6. The misplaced loop fills in finding 1 are a pipeline gap, not a manual one.

## 1. Eight stale loop-seam fills from series 1 now land on re-bow pieces or on the next note: 0.2-0.4 s level bumps of 5-14 dB in the opening chord, under the solo violin, under the flute solo and in the bass at the climax (measured)

**Where.** `build/loop_fills.json`, which holds series 1's c16 fills, fitted on the v77 c15 stems.

| Track | Score onset | Fill (s after start) | Note length now (s) | Lands on | Bump in the stem |
|---|---|---|---|---|---|
| Double basses | 3 (bars 2-3, the opening chord) | 5.99, 6.49 | 3.84 | the re-bow at sq 6.25 | +4.2 / +2.2 dB |
| Double basses | 168 (bar 52) | 4.04 | 2.24 | the re-bow at sq 170.05 | +5.3 dB (stem -50.6 -> -42.4) |
| Double basses | 204 (bar 61, ff) | 3.58 | 4.65 | inside the note, where no dip is left | +5.4 dB, qn 206.9-207.2 |
| Violins II | 108 (bar 37) | 4.40 | 3.48 | the next note, sq 111.2 | +5.9 dB (-44.7 -> -37.2) |
| Violins II | 116 (bar 39) | 4.40 | 3.15 | the note after 118 | +6.3 dB |
| Violoncellos | 3 (bars 2-3) | 5.59, 6.71 | 4.57 | the re-bow at sq 6.8 | +5.3 / +3.6 dB |
| Violoncellos | 63 (bar 22) | 4.20 | 2.36 | the next note, sq 64.84 | +10-14 dB (-47 -> -32.8) |

- The ones that are still right: Horn 1 34 (+1.3), Violas div 87 (-0.1, -0.3) and Violoncellos 3's 2.77 s (-0.5). These measure flat.

**Evidence (measured).**
- **Fill windows against the 0.5 s either side.** Measured with `lf.py`: the in-window level over the neighbouring 0.5 s is the "bump" column above.
- **Why the fills are stale.** Since c27, `AUTO_REBOW` and the v600 port shortened these notes or split them into re-bow pieces. A fill is timed in seconds from the original note's start, so it now falls after the note's end, on a fresh sample start with no seam.
- **Cb 204, 50 ms frames from the note start (203.908).**
  - 2.9-3.15 s: -29.1..-29.8 dB. This is the real seam dip, about 3 dB.
  - 3.5-3.8 s: -20.2..-22.0 dB. This is the fill.
  - From 3.95 s: -26..-27.6 dB.
  - On the master, 20-100 Hz jumps from -36 to -24.5 dB for 0.3 s at qn 207, the middle of the held ff D flat in bar 61. The c30 render shows the same bump, so the fill was already stale before c31.
- **Vc 63.** The bump sits on qn 64.6-65, the solo violin's phrase end. There the solo measures 3.1 dB under its accompaniment (1-qn margin at 64, celli loudest), against +1.5..+5.6 over the rest of bars 21-22.

**Why it matters (inferred).** These are short swells inside sustained pp/ppp chords, the kind of periodic "bowing" movement Dan heard in series 1 (BRIEF item 8). At the climax the bump reads as a bass thump in the middle of a held note.

**Fix.**
- Delete these entries from `build/loop_fills.json`:
  - Double basses "3", "168" and "204".
  - Violins II "108" and "116".
  - Violoncellos "63", and the 5.59 and 6.71 lifts of Violoncellos "3". Its 2.77 s lift is neutral and may also go.
- The remaining real seams belong to `fit_loops.py` / `fit_rebows.py` on the re-bow pieces, if any still measure over 4 dB.
- Generic guard in `tools/score_to_parts.py`, next to c29's stale REBOW_FILLS / LOOP_PROFILES warnings: print a WARNING for any LOOP_FILLS lift whose t_s + width exceeds the moved note's length in seconds (the note keyed by sq).
- Expected result: each bump falls to the surrounding level. These are level-only changes, so `stem_fix.py` can simulate them.

## 2. Bars 57-60 (qn 188-204): Bassoon 2's p bass line is level with the violins' theme and 6-10 dB over Horn 1's mp counter-melody. The horn line is buried through bars 54-60 (measured)

**Where.**
- Score (p.4): violins p/mp theme, doubled by Flute 1 and Oboe 1 (p).
- Horn 1 "1." counter-melody: pp < mp (bars 53-56, doubled by Clarinet 1 and Bassoon 1), then mp < f (bars 57-60).
- Bass line: Bassoon 2 "2." p <, bass clarinet p, double basses mf.

**Evidence (measured, note bodies).**
- **Bassoon 2.**
  - G flat 3 at 190: -30.3 dB. A flat 2 at 194: -30.2. Its other notes: -34.6..-35.7.
  - Its printed f arrival at 196 measures -30.9, so Bassoon 2 has no crescendo: p sounds as loud as f.
  - Violins I's 1-qn means at 190-194 are -30.6..-29.2. Bassoon 2 is level with the theme.
  - The bass clarinet measures -39.4..-32.5 under its role [188,204,-5,4], and the basses -38..-40.
- **Horn 1.**
  - Bars 57-58: -40.1 / -38.2 / -38.3 at 188/190/192, 7-11 dB under Violins I. It is the 7th to 9th loudest stem.
  - Its role `[188, 204, -2, 4]` pushes it down further.
  - Bars 54-56 (176-187): -35..-40 against Violins I -29..-35, 4-8 dB under one violin section and about 7 dB under the theme as a whole.
- **Inferred.** A real horn at mp against violins at p-mp is about level with the pair (Rimsky-Korsakov's ratio: a horn equals about two woodwinds, and one woodwind equals one string section at piano). Measured, the counter-melody falls below the bass line.

**Fix.**
- `build/roles.json` Bassoon 2: add `[187.5, 195.5, -6, 0.5]`, released over 195.5-196.
  - This gives a 6 dB crescendo into the f at 196 and puts the bass line at about -36..-41, under the bass clarinet and basses.
  - The release is a ramp under a crescendo, not a fall, so S3 does not apply.
- `build/roles.json` Horn 1:
  - Change `[188, 204, -2, 4]` to `[188, 204, 2, 4]`, which is +4 dB.
  - Change `[176, 188, 0.5]` to `[176, 188, 2.5]`.
- Simulated (arithmetic on the bodies):
  - Horn 1 at 188-193: -36.1 / -34.2 / -34.3 / -31.8. That is 4-7 dB under Violins I and 2-6 dB over Bassoon 2.
  - Bars 54-56: about 3-6 dB under Violins I.
  - The f bars 59-60 keep the 4 dB ramp and are still under the f strings: Horn 1 measures -26.8..-32 against Violins I -22..-28.
- Level only, so `stem_fix.py` can do it.

## 3. Bars 25-26 (qn 72-78): the celli's p cantabile swell covers the violins' mp theme by 4-8 dB, and the violins fall 5-7 dB from bars 23-24 with no printed decrescendo (measured)

**Where.**
- Score (p.2, rehearsal C): Violins I/II mp "espr., sul D", with no hairpin in bars 25-26. Violins I is "tutti, con sord." at 72.
- Violoncellos p "cantabile, sul D", with < > over 72-75 (top at C4, 74).

**Evidence (measured).**
- **1-qn means at 73-74.** Violoncellos -32.5 / -32.6. Violins I -38.0 / -39.3. Violins II -38.2 / -39.3.
- **Note bodies.**
  - Celli: C4 at 74 -32.2 (vol_db +8.0), then -37.8 at 75.
  - Violins I: 72 -40.7 (vol_db -6.9), 74 -40.1, 77 -41.5.
  - Violins II: 73.5 -42.0, 77 -42.7.
  - In bars 23-24 the same violins measured -32.7..-36.2.
- **Tables behind it.**
  - `note_trims.json` Violoncellos `"74": 4` on top of the soft-hairpin gain.
  - `note_trims.json` Violins I `"72": -3`, which is stale. The note now sits 3.7 dB under the median of its neighbours (68 -32.7, 70 -36.2, 73.5 -37.0), so untrimmed it would be in line.
  - Violins I CC1 also drops from 100 to 62 at 71.94. On the string KS Masters the Molto Vib set is the louder one (BRIEF facts).

**Fix.**
- `build/note_trims.json`: Violoncellos `"74": 4` -> remove. Violins I `"72": -3` -> remove.
- `build/roles.json`:
  - Violoncellos: add `[72, 77, -2, 0.5]`.
  - Violins I and Violins II: add `[71.9, 78, 2, 0.5]`. It joins the existing 78-82 crescendo gain, so nothing steps at 78.
- Simulated: celli at 74 about -38.2, Violins I/II about -35..-38 through bars 25-26. The theme leads by about 2-3 dB per section (5 dB for the pair), and the cello swell stays audible as a swell.
- Optionally, hold Violins I's CC1 near 90 through 72-78 (CC1_SPANS) instead of the 2 dB on Violins I. That keeps the timbre change out of the theme. Inferred.

## 4. Bars 37-40 (qn 108-124): the upper voice of the Violins II divisi (the DIV B track) sits 4-7 dB under the lower voice (measured)

**Where.** Violins II "senza sord., div., sul tasto" pp. The upper voice (A flat 4 - B flat 4) is on Violins II div (DIV B, Flautando). The lower voice (D flat 4 - E flat 4) is on the Violins II section track. Both carry the role `[108, 124, -5]`.

**Evidence (measured).**
- **Note bodies.** Violins II div measures -46.6..-51.8 (median -49.9). Violins II measures -43.3..-45.9 (median -44.8). The upper voice is 5.1 dB under.
- **Comparisons.**
  - The c31 B report measured the same 4-7 dB gap and accepted it.
  - Under this lens, two halves of one section at one printed dynamic should be level. Kit rule: summed main + div stays within ±0.8 dB of the chord version (LEARNINGS 8). With an upper voice this quiet, the chord loses its top.
- **Flute 1.** It stays 7.6-11.7 dB over the loudest single stem.

**Fix.**
- `build/roles.json` Violins II div: change `[108, 124, -5]` to `[108, 124, -1]`. Keep its `[114, 116, 3]`.
- Simulated:
  - Violins II div about -45..-48, level with the lower voice.
  - The flute's margin over the accompaniment sum falls about 1.5 dB (median +4.3 -> about +2.9), and over the loudest stem it stays +6..+10.
  - If that margin is wanted back, Violas `[108, 124, -1.5]` -> `-3` (the violas' pp triplets are the busiest layer at -45..-46).
- Level only, so `stem_fix.py` can do it.

## 5. Horn 1's p solo, bars 9-10 (qn 24-30) and bar 69 (qn 232-236), is only 1.5-3 dB over the nearest pp accompaniment stem (measured)

**Evidence (measured, 1-qn means).**
- **qn 24-26.** Horn 1 -42.3 / -42.9 / -41.8. Bassoon 1 -44.9 / -46.1 / -47.3. Bass clarinet -46.3 / -44.7. Margin over the loudest stem +2.6 / +1.8 / +3.1. Over the whole accompaniment -1.8 / -1.9 / -0.4.
- **Note bodies.**
  - C4 at 24: -42.8. B flat 3 at 25.5: -42.3. A flat 3 at 26: -42.0.
  - Neighbours: 22-23 at -38.9..-40.1, and 27 at -38.8.
  - The same C4 at 19.5 and 31.5 measures -37.6 / -38.5. This is a note residual, not a pitch one, so a pitch-trim change would be wrong.
- **qn 232-236 (bar 69, "1. solo, dolce" mp > pp against Bassoon 1 pp).** Horn 1 -39.8..-43.9. Bassoon 1 -42.3..-45.0. Margin +0.4..+2.6.
- c31 dropped c30 B #3's trims as superseded by the CC1 map return. The margins came back only partly: c29 had +2.3 over the accompaniment at 40, and c31 has +1.0 at 41.

**Fix.**
- `build/note_trims.json` Horn 1: add `"24": 3, "25.5": 2, "26": 2`.
- `build/roles.json` Bassoon 1: add `[23.5, 28.5, -2]` and `[231.5, 237, -2, 0.5]`.
- Simulated:
  - Horn 1 +4..+5.5 dB over the loudest stem at 24-26, and about +1 over the accompaniment sum.
  - Bar 69: +2.5..+4.5 over Bassoon 1, which still sits with Bassoon 2 (-46..-48).
- Level only.

## 6. The "4 soli" passages play at tutti level: the basses in bars 65-70 and the celli in bars 83-86 are as loud as their full sections at the same or a louder printed dynamic (measured levels; the target is inferred)

**Evidence (measured, note bodies).**
- **Basses 4 soli pp, bars 65-70 (220-238).** -47.3..-47.5 on every piece. The full section at pp: -46.9 / -48.1 / -50.3 in bars 47-49 and -47.3 in bar 2.
- **Celli 4 soli ppp, bars 83-86 (274-286).** -49.0..-49.4. The full section at pp: median -45.7. At ppp in bars 1-2 it measures about -49.
- So the four soloists at ppp equal the tutti at ppp. `SOLI_AS_META`'s -3 dB is cancelled by the soft trims and the re-bow fill offsets.
- **Effect on other lines.** The bars 65-70 pedal does not cover Horn 1, which is 9-15 dB over it except in bar 69 (finding 5).
- **Coda.** In bar 83 the pedal is level with the harp harmonics in K-weighted level: -49.5 against -49.6..-51.3. The harmonics still lead by about 10 dB in 500-2000 Hz, so they are heard (measured).
- **Inferred.** Four soloists sound thinner and softer than a section. A ppp 4-soli pedal 3-4 dB under the tutti would match the score's intent and the dynamic map of the other families (pp within ±1.5 dB across families, c31 B).

**Fix.**
- `build/roles.json`:
  - Double basses: add `[220, 238, -3]`. The 238 tutti pp entry stays at full level.
  - Violoncellos: add `[273.9, 286, -3, 0.5]`. 286 is the printed pp and the end of the soli.
- Low priority. Do it after finding 1, because removing the Cb fills changes these pieces' levels.
- MANUAL-GAPS #8 (Basses/Celli Divisi DIV A for the soli) is the timbral answer, but it costs memory.

## Checks asked for in this lens (measured unless marked)

- **Solos over their accompaniment** (1-qn margins over the whole accompaniment / over the loudest single stem).
  - Horn 1, bars 7-14: -1.9..+7.1 / +1.8..+11.5 (finding 5).
  - Oboe 1, bars 15-16: +0.5..+6.7 / +5.0..+8.8.
  - Solo violin, bars 17-18: +2.5..+9.8 / +5.6..+13.9.
  - Oboe 1, bars 19-20: -2.5..+9.4 / +1.4..+12.0. The low point is the entry at 54, under the celli.
  - Solo violin, bars 21-22: -3.1..+5.6 / +0.8..+9.5. The low point is 64, the Vc 63 fill (finding 1).
  - Bass clarinet, bars 31-36: -2.1..+9.6 / -0.1..+11.3. The low points are its entry at 91 and the cor anglais answers at 98 and 101, which are answers and correct.
  - Flute 1, bars 37-40: +1.9..+8.4 / +5.9..+11.7.
  - Cor anglais, bars 41-44: +0.2..+7.1 / +3.0..+12.6 (139 is its phrase end).
  - Oboe 1, bars 45-47: -1.1..+4.9 / +4.5..+11.2.
  - Cor anglais, bars 47-50: +0.1..+8.8 / +3.3..+13.7.
  - Clarinet 1, coda: +1.0..+11.8 at 280-285, and -2.5..+3.7 / +3.0..+9.3 at 286-292. The low point is the 286 entry. The c31 trims worked (c30: 1.1-4.8 under).
- **Dynamic mapping (median note bodies at pp).**
  - Winds: Clarinet 1 -42.3, Clarinet 2 -44.1, bass clarinet -46.6, Bassoon 1 -45.4, Bassoon 2 -46.8, contrabassoon -47.6, cor anglais -46.6.
  - Horns 3/4: -48.7 / -46.8.
  - Strings: Violins I -46.8, Violins II -45.3, violas -45.9, celli -45.7, basses -48.2.
  - Timpani -46.9, harp -47.2.
  - So pp sounds like pp in every family, within about ±2 dB. At ff: Violins I -24.1, celli -24.9, violas -27.8, Violins II -28.6. Single winds -29..-32 (Flute 1 -30.5 with its bar 79 cut). So a string section sits 3-6 dB over one wind, the Rimsky-Korsakov forte ratio (+3 dB).
  - Divisi and soli tracks: findings 4 and 6. Violas div and violas are level in bars 23-28, 80-81 and the coda (within 1-3 dB). Violoncellos div against the celli: -47.2 against -45.7.
- **Bars 61-64 climax.**
  - Master -11.8..-12.9 (bars 61-62) against bars 79-80 -13.5..-15.5. The climax order holds.
  - The ff tune leads: Violins I -18..-23, with Flute 1, Oboe 1 and Clarinet 1 doubling.
  - The f low brass sit 1-6 dB under Violins I in K-weighted level: Trombone 2 -22.4..-25.0, bass trombone -23.4..-26.8, tuba -24.4..-30.2.
  - In 2-5 kHz the brass are 9-20 dB under Violins I. So they add weight without covering, which fits Rimsky-Korsakov's forte ratios (a trombone at f equals about a string section at ff).
  - Timpani: the f stroke at 203 is 6.7 dB under the loudest stem, then the roll is 11-17 dB under (rank 21-22 of 32).
  - Bars 63-64: Trombone 1's quotation leads (-17.1 at 213), and the strings' sf > p falls under it.
- **Bars 79-82.**
  - Violins I and Flute 1 lead: -22..-24.5.
  - Horns 1-2 a2 (f) sit at -24.6..-27.9, level with Violins II and violas.
  - The timpani roll is 6-9 dB under the tune (rank 12-20). No trombones or tuba play here.
- **Timpani rolls (BRIEF 5).**
  - Bars 2-3: rank 5-6. Bar 52: rank 5, 7-13 dB under the top. Bars 67-70 ppp: rank 3-5, 12-20 dB under Horn 1. Bar 81: rank 16-20.
  - No long roll is the loudest stem. The coda strokes (bars 84-85) are the loudest stem by design: they are the printed "answer" over a ppp pedal.
- **Bass.** Long-term 20-100 Hz share -19.6 dB (Dvořák -21.7, Brahms -7.9..-8.5), so solid, not boomy. The one boom is the Cb 204 fill at qn 207 (finding 1).
- **S1-S3.** Every fix above is a role or trim step on an onset, a slow ramp under a crescendo, or the removal of a lift. None is a fast fall in the envelope under a sounding note.

**Do not touch:**
- The climax order and the bars 61-64 levels: the f brass weight, Trombone 1's quotation, the timpani at both climaxes.
- The bar 63 CC7 lanes.
- The solo levels of Oboe 1, the solo violin (bars 17-18), Flute 1, the cor anglais, and Clarinet 1's coda trims from c31.
- The c31 horn CC1 map (soft 57-72) and the Horn 1 early fills.
- The bass clarinet's [188,204,-5,4] role.
- The coda violas / Violas div balance.
- The roll shapes (bars 2-3, 52, 81).
- The Cb EQ set and loud_eq.
- The still-valid loop fills: Horn 1 34, Violas div 87, Vc 3 at 2.77 s.
