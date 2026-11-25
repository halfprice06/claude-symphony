# Cycle 50, critic B: balance and levels (render under review: c49)

## Method

- Stems 01-32 of `cycles/c49/render` (dry tracks, after the volume envelope) and the master. K-weighted and A-weighted power per 10 ms frame (4096-point FFT, 48 kHz). A note's body is the mean over 20-80 % of the played note. A solo's margin is its level over the sum of the other 31 dry stems. The actor's `bcheck_c49.txt` gives the same c49 note bodies as my scripts within 0.2 dB, so every level below can be checked with that tool.
- Data read: `cycles/c49/rendered_build` (`parts.json`, `roles.json`, `note_trims.json`, `pitch_trims.json`, `score_config.py`, `score_to_parts.py`), and `build/mockup-events.tsv` for the printed marks. I compared `roles.json` of c44 with c49 and `note_trims.json` / `pitch_trims.json` of c45 with c49 to list what c45-c49 fitted.
- Terms: a "legato target" is a note whose keyswitch row is a Leg Slur row and which the previous note overlaps. A "slur start" is the first note of a slur on a Leg Slur row. "Not legato" is a note on a Sus row.
- c50 is the legato rebuild cycle, so I propose only rows in `roles.json` and `note_trims.json`, and I say for each whether it sits on a legato note.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 50 (the schedule ends at c47), so no new pages were read. The table lists the manual facts (May 2021 HO manual) and `MANUAL-GAPS.md` items that this report relies on.

| Manual page or gap | Where it applies | Does the render follow it |
|---|---|---|
| p.144: on legato patches velocity sets the transition time; loudness comes from the controllers | Every Leg Slur row: Flute 1 110-122 (velocity 90-95), Cor anglais 124-171, Clarinet 1 283 | Yes. Levels come from CC11/CC1 and the volume envelope. For that reason a level trim on a legato target depends on the loaded legato state (finding 1) |
| p.53: on short articulations velocity sets loudness | Harp harmonics 274-276 (`VEL_SET` 58, 58, 70) | Yes |
| pp.150-151 (with pp.137 and 140): CC7 is the channel ceiling, CC11 shapes the level under it | Clarinet 1 coda: CC7 127 with dips at 282.75 and 291.9-292.35, CC11 31-39 | Yes |
| MANUAL-GAPS 1: clarinet and brass dynamics on CC1 (done in c30) | Clarinet 1 280-297: CC1 constant at 27.5, CC11 31-39 | Yes. The level change inside each coda note comes from CC11, the sample attack and the envelope (finding 2) |
| MANUAL-GAPS 8: half-section divisi patches for div. and 4 soli (never tried; full sections at -3 dB) | Violoncellos div 274-286, Violins II div 108-124, Violas div | By level, yes: each half-section track is within 1.5 dB of its full section at the same printed dynamic (A-weighted medians, pp: Violoncellos div -53.9 against Violoncellos -54.9, Violins II div -52.0 against Violins II -52.3; p: Violas div -49.8 against Violas -49.4). Level gives no reason to change patches |
| MANUAL-GAPS 4, 7, 13: Mid mics on woodwinds and horns, recorded crescendo rolls, Marcato Sustain for the bar 47 fp | Whole movement | Not tried. Not for c50: these are patch or mic changes, and `loop/ONE_TIME.md` keeps new mix changes out of the rebuild cycle |

## Findings

### 1. After the rebuild, refit the c45-c49 trims on legato notes to the c49 levels, not to the c49 trim values

Where: the trims and rows that c45-c49 added or changed on tracks with a Leg Slur row (list below).

What is wrong: these values were fitted on audio from stale legato state. A full rebuild changes the level of a legato target while the data stay the same. Measured case: Trombone 1 at 217.5 (legato target) is -22.2 in c48 and -24.1 in c49 after the full rebuild, a fall of 1.9 dB; every other note of the quotation is identical in both renders (212.5 -25.6, 213 -21.7, 215 -24.1, 217 -22.6). So a trim that was correct in c49 can be up to about 2 dB wrong in c50 (inferred from this one case; the direction on other tracks is not known).

Fix: after the full rebuild and before the full render, measure the notes below on the range renders with the bcheck method and compare with the c49 body levels given here. These levels are the targets, because critics accepted them or asked for them. Change a trim by the measured difference when the difference is 1.0 dB or more; leave smaller differences. Where one pitch trim covers both legato targets and other notes, and only the legato targets move, change the pitch trim and hold the other notes with note trims.

Legato targets on tracks that were not fully rebuilt in c49 (K-weighted body, dB):

- Cor anglais, `pitch_trims.json` `"65": 3, "66": 3`: 126 F4 -38.1; 127.5 F sharp 4 -38.8; 130 -38.9 (also `note_trims.json` `"130": 1`); 131.5 -40.2; 133.5 -42.3; 156 -39.0; 166 -39.6; 168 -43.3; 171 -42.8. `note_trims.json` `"152": -1`: A4 -42.3. Role `[98.5, 102, -7.5]`: 99 -47.7. The same pitch trim also acts on 172 F4 (Sus MAX, not legato, -46.9) and 286 F4 (slur start, -47.2).
- Horn 1, `pitch_trims.json` `"62": -3`: D4 at 22 -35.0 and at 229 -34.6. Roles `[188, 203.9, 2, 0.1]` and `[198.0, 203.9, 2.5]`: 190 -31.8; 192 -36.9; 193 -29.8; 195.5 -37.2; 198 -30.9; 199 -26.6; 200 -28.9; 201 -27.5; 202 -24.3 (188 is a slur start at -36.7; 196 is on Sus MAX at -27.2).
- Bassoon 1, `pitch_trims.json` `"56": 5`: A flat 3 legato targets 24 -55.2; 39 -55.6; 231 -51.0; 238 -52.4; 253 -43.5. Not legato (Sus MAX, tenuto): 21 -51.3; 22 -51.1; 32 -51.6; 33 -54.0. Slur start: 265 -36.3. Role `[231.5, 237, -4.5, 1.5]`: 232 -52.6 (legato target), 235 -51.6 (slur start).
- Bassoon 1, a difference to remove if it remains after the rebuild (measured): at 24 and 39 the legato-target A flat 3 is 4 dB under the tenuto A flat 3 at 21, 22 and 32, at the same printed pp and in the same slur. Target for 24 and 39: -52.5 ± 1, with `note_trims.json` Bassoon 1 `"24"` and `"39"`. This is an accompaniment line under Horn 1, so the gain for a listener is small (inferred).
- Clarinet 1, roles `[280, 286, 0.5, 0.5]` and `[279.9, 292.0, 1.5, 0.5]`, `note_trims.json` `"286": 1.5`: 280 E flat 5 -46.6 (slur start); 283 D5 -43.5 (legato target); 286 C sharp 5 -41.7 (slur start); 289 -41.9 (re-tongued on Sus Non Vib, not legato); 292 C5 -44.1 (legato target).
- Flute 1, role `[125.75, 131.5, 1, 0.5]` (the flute under the cor anglais): 126 -45.0 (slur start); 127.5 -44.5; 128 -40.5; 129 -43.7; 129.5 -44.8; 130 -44.3 (legato targets).
- Violoncellos, role `[152.0, 164.0, -3.0, 0.5]`: 152 -48.0 (slur start); 156 -49.8; 158 -50.0; 160 -45.9; 162 -49.1 (legato targets).
- Bass clarinet, `note_trims.json` `"24": -4`: -51.7 (slur start). `"18": -4` and `"39": -4` are on Sus Non Vib (not legato): -52.6 and -52.6.

Fully rebuilt in c49, so fitted on fresh state; verify only:

- Oboe 1 `note_trims.json`: `"44": 2` -39.0 (legato target); `"139": 6` -44.2 (slur start); `"145": 5` -41.9 (legato target); `"266": -8` -34.6 (legato target).
- Trombone 1 rows `[212.4, 212.9, 1.5]` and `[212.91, 213.6, 3.5]`: 212.5 -25.6; 213 -21.7. The note at 217.5 (-24.1) needs no compensation for balance: it is 1.5 dB under 217, and the quotation's margin in bars 63-64 is +6.0 K / +7.0 A (measured).

Not on legato notes; no state reason to re-check: Flute 1 `[204, 208, -1.5]`, Clarinet 1 `[204, 210, -2]`, Bass clarinet `[204, 208.5, -2]`, Bass trombone `[200, 214, 2, 1]`, Tuba `[200, 214, 1, 1]`, Double basses `[139.9, 146.0, -3]` (all on Sus rows), and the Harp and Timpani rows.

The two c49 open items of this kind are within tolerance now: Cor anglais 127.5 is -38.8 against a predicted -37.2, and Bassoon 1 231 is -51.0 against -50.1. Both are legato targets, so decide after the rebuild.

### 2. Clarinet 1, coda solo entry, bar 87 (qn 286.0-287.0): the solo is under its accompaniment for the first beat

Where: Clarinet 1, C sharp 5 at qn 286 (printed "1." pp, slur 286-295, after the breath). Tempo about 51 bpm, so one beat lasts about 1.15 s.

What is wrong (measured): the note needs 1.25 beats to reach its body level, and half of that rise is in the volume envelope. Quarter-beat levels from 286.0 (K): -50.2, -48.7, -45.4, -43.7, -41.9, -40.4, -40.4; the body is -41.7. The sum of the other stems over the same quarter beats is -44.3, -42.1, -42.6, -41.7, -41.8, -40.9, -41.5. Margins K: -5.9, -6.6, -2.8, -2.1, -0.1, +0.5, +1.1. Margins A: -2.9, -3.1, -0.2, +0.5, +2.1, +3.2, +4.0. No hairpin is printed on this note.

Evidence for the cause (measured in `parts.json`): `vol_db` is +4.8 at 286.0, +6.4 at 286.5, +7.2 at 286.9, +7.8 at 287.0 and +9.9 at 287.4, a rise of 5.1 dB. The first 2.4 dB (286.0-286.9) is the opening of the lyrical phrase shape for the phrase 286-297; the next 2.7 dB (286.9-287.4) is the half-beat ramp-in of the c23 row `[287.4, 289.0, 2.5]`. The stem minus the envelope rises 5.3 dB over the same beat (the sample's pp attack plus CC11 34 to 38).

Fix: `roles.json`, Clarinet 1, add the row `[286.0, 286.9, 2.5]`. A row ramps in over the half beat before its start and out over the half beat after its end, so this row's ramp-out (286.9-287.4) cancels the c23 row's ramp-in and the two rows sum to a constant +2.5 dB from 286.0 to 289.0. The c23 row, the note trims `"286": 1.5`, `"289": 4`, `"292": -4` and the phrase shape stay as they are. Check in the built `parts.json`: `vol_db` about +7.3 at 286.0, +8.9 at 286.5, +9.7 at 286.9, +9.9 at 287.4, unchanged from 287.4 on.

Predicted (arithmetic on the c49 stems): quarter-beat levels from 286.0: -47.7, -46.2, -42.9, -41.3, -40.5, -40.2, -40.4. Margins K: -3.4, -4.1, -0.3, +0.3, +1.3, +0.8, +1.1. Margins A: -0.4, -0.6, +2.3, +2.9, +3.5, +3.5, +4.0. The solo then reaches the level of its accompaniment after half a beat instead of a full beat. The row's ramp-in also raises the last quarter beat of the D5 (285.5-285.75) by 0 to 1.25 dB, which is not audible (inferred).

Legato status: 286 is a slur start on the Leg Slur row, not a legato target. Clarinet 1 is a legato track, so re-check the seven quarter-beat levels after the rebuild before fitting the row.

Not proposed: the remaining deficit in the first half beat is the sample's attack. An entry lead for this note (`entry_leads.json` has none for Clarinet 1) is a timing change in critic A's area; I did not measure the attack centre.

### 3. Flute 1, bars 37-39 (qn 108-122): the notes at the top of the printed hairpin are 3-5 dB under the phrase's first note, and C sharp 5 at 121 is 3-7 dB under its neighbours

Where: Flute 1 solo over the sul tasto Violins II. Printed: p at 108, crescendo 108-111, decrescendo 112-114, crescendo 114-116, decrescendo from 118, p at 120. The dynamic curve in `parts.json` peaks at 68 (between mp and mf) over 110.9-112.1.

What is wrong (measured): note bodies K: 108 F5 -36.6; 110 F sharp 5 -36.3; 110.5 F5 -35.8; 111 E flat 5 -39.4; 112 C sharp 5 -41.1; 113 C5 -42.2; 113.5 C sharp 5 -41.1; 114 E flat 5 -39.6; then 120 C5 -39.8; 121 C sharp 5 -44.4; 121.5 C5 -41.3; 122 B flat 4 -37.2. The loudest note is 110.5; at 111-112, where the hairpin peaks, the line is 3.6-5.3 dB below it and 2.8-4.5 dB below the opening p. Half-beat margins K over the other stems: 110.5 +6.0; 111.0 +2.8; 112.0 +0.4; 113.0 +1.4; 113.5 +0.6; 121.0 -1.9 (bar 37 before the peak: +4.4 to +6.6).

Evidence for the cause (measured): at equal CC11 the patch is weaker on these pitches. Stem minus envelope at the note middle: F5 -39.4 (CC11 67); E flat 5 -43.9 (CC11 72); C sharp 5 -47.4 (72); C5 -48.7 (69); C sharp 5 at 121 -51.3 (55) against C5 at 120 -46.6 (54). The existing pitch trims `"72": 3` and `"73": 3` and the note trims of +4 at 110, 110.5, 113 and 113.5 cover part of it; 111, 112 and 121 have no note trim.

Fix: `note_trims.json`, Flute 1: add `"111": 2.5`, `"112": 3`, `"121": 3`; change `"113": 4` to `5.5` and `"113.5": 4` to `5`. I use note trims and not the pitch trim `"73"`, because C sharp 5 at 119 (-41.3, in the decrescendo between 118 at -39.3 and 120 at -39.8) is at the right level.

Predicted (arithmetic on the c49 stem): 110.5 -35.8; 111 -36.9; 112 -38.1; 113 -40.7; 113.5 -40.1; 114 -39.6; 120 -39.8; 121 -41.4; 121.5 -41.3. Margins K: 111.0 +5.3; 112.0 +3.4; 113.0 +2.9; 113.5 +1.6; 121.0 +1.1. The crescendo still ends in a plateau and not a rise (108 -36.6 to 111 -36.9); lowering the opening note would cost margin in bar 37, so I leave it.

Legato status: all five notes are legato targets (Leg Slur MAX, velocity 90-95). Fit them after the rebuild against the new stem, with these targets: 111 -37 ± 1; 112 -38 ± 1; 113 -40.7 ± 1; 113.5 -40 ± 1; 121 -41.5 ± 1.

## Also measured, no change proposed

- Solo margins in c49 (K / own-band / A, dB): Horn 1 bars 7-14 +7.4 / +9.4 / +8.2; Oboe 1 bars 15-16 +3.0 / +12.5 / +6.3; Violin I solo bars 17-18 +7.0 / +15.1 / +10.3; bass clarinet bars 31-36 +5.8 / +8.7 / +5.1; Flute 1 bars 37-40 +3.4 / +7.8 / +6.4; cor anglais bars 41-44 +0.1 / +5.5 / +3.3 and bars 47-50 +2.5 / +8.2 / +5.5; Oboe 1 bars 45-47 +1.3 / +6.8 / +3.9; Trombone 1 bars 63-64 +6.0 / +8.8 / +7.0; Horn 1 bars 65-70 +4.4 / +9.8 / +3.2; Clarinet 1 bars 85-89 +1.2 / +8.6 / +4.5. c49 differs from c48 by less than 0.3 dB outside the intended changes.
- Cor anglais bars 41-44: c49's trims gave the levels the previous report asked for (126 -41.1 to -38.1; 130 -42.7 to -38.9; 133.5 -44.7 to -42.3). The last note, C4 at 136, tapers to the level of the flute's held E flat 5 on its last beat; it is printed p after a decrescendo in a duet, so this is correct.
- Climax, bar 61 (K): strings -16.5, brass -17.9, woodwinds -19.8, timpani -32.0; Trombone 2 -23.8, bass trombone -24.1, tuba -26.4, Horn 1 and Horn 3 about -27. A trombone is 3.5 dB over a horn, which agrees with Rimsky-Korsakov's forte proportion (one trombone balances two horns). Bar 79: woodwinds -22.2, strings -22.1, brass -27.2 (horns printed f against ff), timpani -37.7. Timpani and low brass do not cover in either passage.
- Bar 60 (qn 200-204): the low brass enter at -48 to -56 and rise to -31 to -35 before the step to f at 204; the timpani roll rises from -40.5 to -26.4 and stays 12-20 dB under the master. No change.
- Dynamic mapping, A-weighted medians of note bodies (notes of one beat or longer): pp woodwinds -54.7, horns -54.6, strings -54.9, divisi and solo strings -53.9; p -49.4 / -48.8 / -47.2 / -45.8; mf -42.3 / -42.0 / -39.4 / -41.0; f woodwinds -39.1, horns -34.3, strings -35.5, low brass -28.0. pp and p agree across families within 2 dB up to the solo tracks, and the forte steps follow Rimsky-Korsakov's proportions (one horn about 5 dB over one woodwind).
- Opening chord, bar 1 (all ppp, K): Violins I -48.2, Violins II -50.6, Violas -51.6, Violoncellos -51.2, Horn 3 -54.0, Horn 4 -54.3. The top voice is 2.4-3.4 dB over the other strings. No change.
- Harp harmonics, bar 83 (first half beat, K): 274 -49.0; 275.5 -49.3; 276 -44.6. The arrival is 4.5 dB over the first two. Critic A set this shape in earlier cycles (`VEL_SET` and `LEVEL_SHAPES_S` in `score_config.py`), and the A-weighted margins over the pedal are +3.5, +7.6 and +11.4, so I propose no level trim. The per-pitch spreads in `gain_c49.txt` (Harp harmonics 3.8 dB, Oboe 1 1.9 dB) are left-right image values and need no level pitch trims: Oboe 1 at 42-45 is within 0.7 dB of the previous predictions.
- The pitch_check flags at Violins II 120 and Violins II div 122 are not level problems: the stems at those notes are within 1.5 dB of c48 (-50.0 against -49.7; -47.0 against -45.5).
- Clarinet 1 over the cor anglais in bars 87-88 (c49 open item, 7.8 to 6.3 dB): keep. Finding 2 raises the clarinet's first beat, which is where the two are closest.

## Do not touch

The c44 mic positions and family EQs; the hall and returns at their c44/c45 faders; the c30 CC1 map and horn CC1 57-72; `HP_SOFT_GAIN_AT["Horn 1"][20.0] = 3.0` and the crescendo into bar 8; Horn 1's note trims at 24, 25.5, 26 and its role `[198, 203.9, 2.5]`; the cor anglais role `[127.5, 133.5, -3.5, 2.5]` and its c49 F4 / F sharp 4 levels (as targets, see finding 1); Flute 1's note at 136 and its level shape, and its trims at 110, 110.5, 117-117.667; Oboe 1's step at 148 and its trims at 42-45, 139, 145, 266 with Main 0.24; Clarinet 1's c23 row `[287.4, 289.0, 2.5]`, `"289": 4`, `"292": -4` and the body levels 280 -46.6, 283 -43.5, 286 -41.7; the coda balance rows, the basses' pedal shape and the 4.1 s pedal fills; the bar 61-62 string holds and brass balance; the bar 63 CC7 lanes and Trombone 1's rows (no compensation at 217.5); the timpani roll shapes and the step at 277; the basses' f/ff trims and 35 Hz high-pass; the harp and harp harmonics levels; the PHRASE_SHAPE values; the c46 tempo map; the c47 fills and wind entry leads; the c48 fp chain; the c49 Violas reset at 152.06 and its nine entry leads.

Scratch folder: `/private/tmp/claude-501/mockup-loop/mvt2-c50-B/` (179 MB: scripts m1.py-m7.py and cached frame levels) is left in place, because the launcher's instruction for this run was not to delete files.
