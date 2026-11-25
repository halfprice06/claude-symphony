# Cycle 49, critic B: balance and levels (on the c48 render)

The largest balance faults left in the c48 render have one cause. The c44 "EastWest template mix" cycle changed the mic positions and the family EQ, and that changed each pitch of the wind and horn patches by a different amount. The per-pitch and per-note trims fitted before c44 no longer match the samples as they now sound. Three solo lines and one accompaniment line now carry a loud or a weak pitch that the print does not ask for. Findings 1 to 5 correct those pitches with pitch trims, note trims and one role value. No mic, EQ, gain, CC map or soft trim needs to change.

## Method

- I measured the 32 dry stems and the master of `cycles/c48/render/`, and for comparison the stems of c36, c38, c41, c43, c44, c45, c46 and c47. Each render is read on its own `rendered_build/parts.json` tempo map.
- Levels are K-weighted (BS.1770) unless marked A (A-weighted), from 4096-point FFT frames at a 10 ms hop, power of both channels. Note bodies are the mean over 20-80 % of the moved note.
- A solo's margin is its level over the sum of the other 31 dry stems. I give K and A together, because K-weighting hardly discounts low pedal notes and A-weighting discounts them by 19-30 dB. The own-band margin is the same comparison in 1/3-octave bands, weighted by the solo's energy per band.
- Cross-render comparison: for every sustained note (0.9 quarter notes or longer) I read CC1, CC11, CC7 and `vol_db` from each render's parts.json, kept the notes whose CC1 and CC11 agree within 1.5 units, subtracted the `vol_db` change, and compared the body level. A pitch is flagged when its median change differs from the track's median change by 2.5 dB or more.
- Predictions scale the cached per-frame powers of the stems by the proposed trims and re-sum.
- Labels: **measured** (from the render or the data), **predicted** (arithmetic or simulation on measured levels), **inferred** (a judgement about cause or about what a listener hears).
- I changed no audio setting and touched no REAPER, build or tool file. The scratch folder `/private/tmp/claude-501/mockup-loop/mvt2-c49-B/` (436 MB, scripts and cached analyses) is left in place, because the launcher of this run said not to delete files. The per-pitch comparison is `m15.py` there (`m15.py c43 c44 "Horn 1" "Cor anglais" ...`).

## Manual notes

MANUAL-READING.md has no row for cycle 49, so I did no page reading. The table lists the manual facts and MANUAL-GAPS items this report relies on.

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.53: velocity is for short articulations; CCs shape sustained notes. p.144: on true-legato rows velocity sets the transition time, not the loudness. | All five corrected lines are sustained or legato notes (Leg Slur MAX, Sus MAX). | Yes. Their level cannot be corrected with velocity. The fixes act on the volume envelope (`vol_db`), through pitch trims, note trims and roles. |
| MANUAL-GAPS #1 (p.101; 2025 manual p.61-67): brass and clarinet dynamics on CC1, kept since c30. | Horn 1 bars 7-14 and 67-70; Clarinet 1 bars 85-89. | Yes. CC1 is identical in c43 and c44 at every note compared, so the level changes below are not controller changes. |
| p.138-139, p.222, MANUAL-GAPS #4: Close mics capture presence, Main the unified sound of the section; Mid is the alternative to Close. | Woodwinds and horns since c44 (Clarinet 1: Close 0.5 / Main 0.8 became Close 0.782 / Main 0.528), with the woodwind family EQ (447 Hz -5.1 dB, 1000 Hz -3.1, 2200 Hz -4.7). | The c44 setting stands. Its per-pitch consequences were not corrected (findings 1-5). |
| MANUAL-GAPS #5 (p.109): expressive rows for dolce wind solos. | Cor anglais bars 41-50, Clarinet 1 bars 85-89. | Not tried. Not needed for the fixes here. |
| MANUAL-GAPS #7 (p.123, p.125): recorded crescendo rolls. | Timpani at 168, 200, 261. | Not tried. The f rolls sit 18-23 dB under the master ("Also measured"). |
| MANUAL-GAPS #8 (p.89-90, p.222): 4 soli on half-section patches. | Vc div bars 83-86; basses 4 soli bars 65-70 and 87-92. | Levels on target: Vc div pp -48.9 against celli pp -48.3. Only the timbre is open. |

Balance norms: Rimsky-Korsakov, Principles of Orchestration, chapter I, "Comparison of resonance in orchestral groups" (`reference-books/text/rimsky-principles.txt` lines 1960-1989): in piano all winds are of fairly equal balance and one string department equals one wind instrument; in forte the horns are half as strong as trumpets and trombones and the woodwinds half as strong as the horns. Adler, The Study of Orchestration, p.116, "Foreground-Middleground-Background" (`reference-books/text/adler1.txt` lines 6165-6195).

## The common cause: each pitch moved by a different amount at c44 (measured)

Between c43 and c44 the controllers of the notes below did not change, and I subtracted every `vol_db` change. The table gives each pitch's median level change minus the track's median change.

| Track (median change c43 to c44) | Pitches that moved against the rest of the track |
|---|---|
| Horn 1 (-1.7 dB) | D4 +4.0 (qn 22 and 229, both +4.0); E flat 4 +2.0 (4 notes); every other pitch within 1.6 |
| Cor anglais (-4.4) | F4 -1.4 (4 notes, -1.9 to -0.8) and F sharp 4 -1.4 (4 notes) against A flat 3 +2.3, C sharp 4 +1.8, E flat 4 +1.9, E4 +2.2: F4 and F sharp 4 fell 3.2-3.7 dB against their neighbours; A4 -5.9 (qn 152) |
| Clarinet 1 (-3.4) | E flat 5 -5.1 (280), D5 -4.9 (283), G5 -3.7, B flat 5 -3.7, B flat 4 -2.7, C sharp 4 +3.9; D flat 5 +0.7, C5 +1.6 |
| Clarinet 2 (-3.1) | C sharp 4 +3.9, B flat 4 -3.9: the same pitches as Clarinet 1 on the same patch |
| Bassoon 1 (-4.7) | A flat 3 -5.1 (10 notes), E flat 3 +4.3 (8 notes), E4 +4.8 |
| Oboe 1 (-3.5) | E flat 5 -2.5 (44, 47, 196), E5 -3.5, B flat 5 -2.8, A flat 5 +2.8 |
| Flute 1, bass clarinet, Violin I solo, Trombone 1, Horn 4, Flute 2 | Nothing over 2.5 dB |

The shift repeats at every occurrence of a pitch and is the same on two tracks that use the same patch, so it belongs to the patch and the c44 settings, not to a note's context. The band levels show that it is not the EQ alone: on the cor anglais F4 at qn 126 the 1000 Hz band (the third harmonic, the strongest band in c43) fell 12.6 dB while the fundamental fell 1.8 dB, and a static -3.1 dB bell cannot do that. The mic mix against the EQ is my reading of the mechanism (**inferred**); the stems do not let me separate the two. The per-pitch shift itself is **measured**.

Later cycles corrected some of the consequences one note at a time without naming the cause. c47 raised Horn 1's C sharp 4 at 230 by 3 dB because it sat 8.5 dB under the D4 before it; the D4 was the note that had moved.

## Findings

### 1. Horn 1, the theme: the D4 at qn 22 (bar 8) and qn 229 (bar 68) is 3-5 dB too loud

**Where.** Horn 1, bar 8 beat 2 (qn 22) and bar 68 beat 1 (qn 229). These are the only two D4 notes on the track.

**What is wrong (measured).** In bar 8 the print has a crescendo over qn 20-21 and a decrescendo over 21-24 (dyn_curve 46, 58 at 21, 46 at 23.88). The peak is at qn 21, inside the E flat 4 that sounds from 20 to 22. The render has a second, higher peak one beat late, on the D4, and then drops 7-8 dB in one beat where the print spreads one dynamic step over three beats. In bars 67-68 the D4 is the printed peak of the crescendo (58 at 229), but it stands 4-5 dB over the end of the E flat 4 before it and 5.5 dB over the C sharp 4 after it.

**Evidence.**

- Bar 8 at quarter-beat steps (c48): 20.0 -37.0, 20.5 -37.3, 20.75 -34.8, 21.0 -33.5, 21.25 -32.8 (the hairpin's peak), 21.5 -34.0, 21.75 -36.3, 22.0 -33.4, 22.25 -31.6, 22.5 -32.3, 22.75 -34.0, 23.0 -39.6, 23.25 -40.0, 23.5 -38.5, 24.0 -39.7.
- Bars 67-68 at half-beat steps (c48): 226 -40.6, -37.8, 227 -35.0, -37.0, 228 -37.9, -36.2, 229 -32.1, -32.7, 230 -38.2, -37.8, 231 -40.2, -41.6.
- Note bodies in c43 / c44 / c48: 20 E flat 4 -38.2 / -35.0 / -34.7; 22 D4 -38.2 / -33.4 / -32.1; 23 C sharp 4 -38.6 / -41.3 / -39.3; 24 C4 -38.5 / -40.8 / -39.4. Reprise: 226 E flat 4 -37.2 / -36.2 / -36.7; 229 D4 -33.8 / -31.5 / -31.7; 230 C sharp 4 -38.1 / -41.1 / -37.6 (c48 includes c47's +3 shape); 231 C4 -38.7 / -40.4 / -40.2.
- Per-bar margin of the horn over the other stems (A): bar 7 +8.3, bar 8 +12.1, bar 9 +8.5; bars 67-68 +16.6 and +14.2. The horn does not need the extra level.
- Cause: the +4.0 dB shift of D4 at c44 (table above). At bar 8, c44 also removed the role `[20.5, 23.5, -2.5]` (c44 C #2, so that the crescendo into bar 8 rises); that was right for the crescendo and left the D4 uncorrected.

**Fix.** `build/pitch_trims.json`, "Horn 1": add `"62": -3` (the table already has `_all_arts: true`, and 22 and 229 are not in `_skip_onsets`). The trim starts at the D4's moved onset, so the crescendo over qn 20-21.25 is untouched. **Predicted:** qn 22 body -35.1, which is 0.4 under the E flat 4's body and about 2 under the hairpin's peak; qn 229 body -34.7, which is level with the E flat 4's loudest point (-35.0 at 227), 1.5 over its last half beat and 2.9 over the C sharp 4. A value of -4 would undo the measured shift exactly, but then the D4 at 229 would not exceed the end of the E flat 4, and the print puts the peak on it. Optional: `build/note_trims.json`, "Horn 1": add `"23": 1.5` (the C sharp 4 goes from -39.3 to -37.8, between the D4 and the C4 at -39.4; 23.0 is in the pitch table's `_skip_onsets`, so a note trim is the way). After the D4 trim, re-measure 229-231 (predicted -34.7 / -37.6 / -40.2) before deciding whether c47's +3 shape at 230 should stay at 3.

### 2. Cor anglais solo, bars 41-44: F4 and F sharp 4 are 3-6 dB under the line, and the solo does not lead on those beats

**Where.** Cor anglais, qn 124-140 ("solo, dolce cantabile", p, crescendo 124-128 to mp, decrescendo 131-136). The weak pitches are F4 and F sharp 4, at 126, 127.5, 130, 131.5 and 133.5, and again at 156, 166, 168, 171, 172 and 286.

**What is wrong (measured).** The line should rise through the crescendo. Since c44 it dips at 126 and falls 5-6 dB at 130, at the top of the printed mp. This solo has the smallest lead of any solo in the movement, and on the F4 and F sharp 4 beats it is level with or under the other stems, with Flute 1's counter-line (printed one dynamic lower) within 1 dB of it.

**Evidence.**

- Note bodies c48 (pitch, printed level on the dyn_curve): 124 A flat 3 -38.1 (47); 125 C sharp 4 -38.1 (50); 126 F4 -41.1 (54); 127.5 F sharp 4 -40.2 (57); 128 A flat 4 -36.8 (58); 129 B flat 4 -36.6; 129.5 A flat 4 -37.7; 130 F sharp 4 -43.0 (58); 131.5 F4 -43.6 (56); 132 E flat 4 -39.8 (54); 133.5 F4 -44.9 (51); 134 C sharp 4 -40.4 (50).
- The same notes in c43 with the same controllers: 124 -36.9, 125 -36.2, 126 -35.6, 128 -32.8, 130 -37.2, 132 -37.0, 134 -39.1. The line rose to the mp and came down evenly.
- Margin over the other 31 stems per bar (K / own-band / A): bar 41 -0.7 / +4.9 / +3.9; bar 42 -0.8 / +7.9 / +2.4; bar 43 +0.2 / +11.8 / +3.2; bar 44 -2.0 / +12.0 / -0.2. The actor's check44 reads 2.5 for bars 41-44 against 3.5 to 8.7 for the other wind and horn solos.
- Per beat, A / K: 126 +1.1 / -3.2; 127 -1.4 / -2.9; 130 -1.2 / -3.4; 131 -0.5 / -3.0; 133 +2.5 / 0.0; against 124 +9.4 / +0.9, 125 +8.6 / +1.9, 129 +4.8 / +0.2, 135 +7.3 / +3.3.
- Cor anglais minus Flute 1 (A) per beat from 126: +5.0, +0.8, +3.0, +6.7, +0.2, +1.0, +3.8, +3.4.
- Cause: F4 and F sharp 4 fell 5.7-6.3 dB at c44 while E flat 4, C sharp 4 and A flat 3 fell 1.5-3.5 dB (table above).

**Fix.** `build/pitch_trims.json`, "Cor anglais": add `"65": 3, "66": 3` and `"_all_arts_pitches": [65, 66]` (ten of the eleven notes are on Leg Slur MAX; the F4 at 172 is on Sus MAX and needs the key). `build/note_trims.json`, "Cor anglais": add `"130": 1`, because the c19 role `[127.5, 133.5, -3.5, 2.5]` is at full depth there. Keep that role. Do not change Flute 1.

**Predicted (simulation on the c48 stems).** Line: 124 -38.1, 125 -38.1, 126 -38.1, 127.5 -37.2, 128 -36.8, 129 -36.6, 129.5 -37.7, 130 -39.0, 131.5 -40.6, 132 -39.8, 133.5 -41.9, 134 -40.4. Per beat, A / K: 126 +4.1 / -0.2; 127 +1.5 / -0.1; 130 +2.8 / +0.6; 131 +2.7 / +0.3; 133 +3.8 / +1.4. Cor anglais minus Flute 1 (A): 126 +8.0, 127 +3.6, 130 +4.2, 131 +4.3, 133 +4.6. Per bar (K / own-band / A): bar 41 +0.6 / +6.2 / +5.1; bar 42 +0.3 / +8.8 / +3.3; bar 43 +0.6 / +11.9 / +3.5; bar 44 unchanged. Second solo: 156 -38.9, 166 -39.7, 168 -43.4, 171 -42.7; the margins of bars 48-50 (A +4.0 / +7.8 / +3.4) hardly change. If the actor wants the opening two notes one step under the mp, `"124": -1.5, "125": -1.5` in note_trims is optional; I do not ask for it.

### 3. Coda, Clarinet 1 bars 85-89: the first phrase is 6-7 dB under the second at one printed pp

**Where.** Clarinet 1, qn 280-297 ("dolce", niente to pp over 280-282; E flat 5 at 280, D5 at 283 with a breath mark, D flat 5 at 286 and 289, C5 at 292). The cor anglais ("dolce", pp) is the lower voice of the duet from bar 87.

**What is wrong (measured).** Both phrases are printed pp. The E flat 5 and the D5 sound at -49.5 and -46.7, the two D flat 5 at -40.7 and -41.9. The whole dry sum rises 5.2 dB from bars 85-86 to bars 87-88 for a printed change from ppp to pp in the accompaniment, under a solo that stays at pp. In bars 87-88 the clarinet is 7 to 10 dB over the cor anglais, which is more than a duet of two pp voices marked dolce asks for (c35 B judged 7.5 too much; c46 B aimed at 4 to 6).

**Evidence.**

- Clarinet 1 per bar, bars 85-89: c36 -42.9 -40.8 -41.6 -42.4 -40.2; c43 -44.7 -42.9 -43.8 -44.8 -42.7; c44 -50.9 -49.6 -43.4 -44.6 -44.1; c48 -49.3 -48.0 -41.7 -42.4 -43.7. In c43 the five bars were within 2.1 dB.
- Per note, c43 to c44, with CC1 (20.5-28), CC11 (28-39) and the keyswitches unchanged: 280 -45.1 to -51.6; 283 -41.7 to -48.0; 286 -43.2 to -42.4; 289 -45.0 to -44.2; 292 -43.4 to -44.5. The fundamental band of the D5 (630 Hz) fell 7.6 dB; that of the D flat 5 rose 0.7 dB.
- The `vol_db` already carried bars 87-88 about 6-7 dB over bars 85-86 in c43 (286.5 +6.0, 287.5 +9.1, 289.5 +6.9 against 280.5 -0.8, 283.5 +0.4). Those trims were fitted when D flat 5 was the weak pitch (c31 B #2). Since c44, E flat 5 and D5 are the weak pitches and D flat 5 is not, so the same trims now produce the step.
- Margins as rendered (K / own-band / A): bar 85 -1.6 / +13.8 / +6.4; bar 86 -0.8 / +16.7 / +6.8; bar 87 +1.4 / +9.2 / +4.4; bar 88 +2.1 / +8.9 / +3.7. Clarinet over cor anglais by bar mean: bar 87 +9.8, bar 88 +7.3 (check44: 7.8 for bars 87-88, by its own method).
- Cor anglais bodies: 286 F4 -50.3, 289 E4 -48.0. The F4 is the pitch of finding 2.

**Fix.** `build/roles.json`, "Clarinet 1": change `[280, 286, -2.5, 0.5]` to `[280, 286, 0.5, 0.5]` (+3 on the first phrase). `build/note_trims.json`, "Clarinet 1": change `"286": 2.5` to `1.5`. Leave `"289": 4`, `"292": -4` and the c23 row `[287.4, 289.0, 2.5]`. For the duet, let finding 2's F4 pitch trim apply at 286 (do not add 286 to the cor anglais `_skip_onsets`); optional: `note_trims.json`, "Cor anglais": add `"289": 1.5`. I rejected lowering bars 87-88 to meet the first phrase: it would leave the solo with the smallest A-weighted lead of the movement.

**Predicted (simulation).** Clarinet bodies 280 -46.5, 283 -43.7, 286 -41.7, 289 -41.9, 292 -44.1. The step from the D5 to the D flat 5 falls from 6.0 dB to 2.0 dB; per bar the first phrase sits 2.3-3.9 dB under the second in place of 5.6-7.6. Bars 85-86 at -46.3 / -45.0 stay under the -45.5 / -43.5 that c32 C and c35 B last set on purpose. Bar 85 K +1.4, own-band +16.8, A +9.4; bar 86 +2.2, +19.7, +9.8; bar 87 -0.2, +7.8, A +2.5, and A +4.6 against the stems without the cor anglais; bar 88 +1.6, +8.7, A +2.9 (+6.1 without the cor anglais). Clarinet over cor anglais +5.8 in both bars. The dry sum rises 3.6 dB from bars 85-86 to bars 87-88 in place of 5.2. A lighter version, +2 on the role and nothing else, gives 280 -47.5 and 283 -44.7.

### 4. Bassoon 1 under the horn theme: every A flat 3 is 5-10 dB under the rest of its line

**Where.** Bassoon 1, bars 7-14 (qn 18-42) and bars 68-70; A flat 3 at 21, 22, 24, 32, 33, 39, 231, 238, and at 253 and 265 in the tutti.

**What is wrong (measured).** Bassoon 1 is the top voice of the wind accompaniment under the horn (E flat 3 and A flat 3 over Bassoon 2's C3 and the bass clarinet's A flat 2), printed at one dynamic throughout. On E flat 3 it is the loudest accompaniment voice (-50.8); on A flat 3, the tonic, it is the quietest (-55.8 to -60.6), 1.5 to 10 dB under the harp, the bass clarinet and Bassoon 2. Adler's point about the background (p.116) is that it should be even in itself so that it does not draw attention; here one voice of the chord comes and goes with the pitch.

**Evidence.**

- Note bodies in c43 / c48, with CC1 41-42 and CC11 33-34 in both: 18 E flat 3 -50.7 / -50.8; 21 A flat 3 -46.7 / -56.1; 22 A flat 3 -46.7 / -55.8; 23 G3 -50.4 / -54.3; 24 A flat 3 -50.4 / -60.2; 26 F3 -51.6 / -54.4; 27 E flat 3 -52.9 / -52.5; 30 E flat 3 -50.6 / -50.4; 32 A flat 3 -46.7 / -56.4; 33 A flat 3 -48.9 / -58.9; 36 B flat 3 -46.3 / -52.4; 38 G3 -48.7 / -50.0; 39 A flat 3 -49.7 / -60.6; 231 A flat 3 -49.5 / -55.1; 238 A flat 3 -47.0 / -57.3; 253 -40.6 / -48.5; 265 -33.9 / -41.3.
- A flat 3 is 5.6-10.9 dB lower in c48 than in c43, and the whole drop happened at c44 (qn 21: -46.7, -56.6, -56.1 in c43, c44, c48); E flat 3 at soft dynamics did not move; the track's median fell 4.7 dB.
- The accompaniment at qn 39-42 (c48): harp -51.2, bass clarinet -52.7, Bassoon 2 -55.9, Bassoon 1 -60.7, under Horn 1 at -41.8.

**Fix.** `build/pitch_trims.json`, "Bassoon 1": add `"56": 5` (the table has `_all_arts: true`). **Predicted (arithmetic):** A flat 3 at 21 -51.1, 22 -50.8, 24 -55.2, 32 -51.4, 33 -53.9, 39 -55.6, 231 -50.1, 238 -52.3; the line under the horn then spans -50.0 to -55.6 in place of -50.0 to -60.6. The sum of the accompaniment at 39-42 rises 0.5 dB (-47.9 to -47.4), so the horn's lead in bar 14 falls by about 0.5 dB (from +7.8 A, +5.8 K). The pre-c44 `"51": 6` on E flat 3 now puts the soft E flat 3 about 4 dB over the track's median change; lowering it to 4 is optional, and I did not check its effect on the loud E flat 3 at 198 and 200, which did fall with the rest.

That the uneven voice is audible under the horn is **inferred**; the levels are measured.

### 5. Oboe 1, bar 15: the E flat 5 at the top of the crescendo is under the notes around it

**Where.** Oboe 1, qn 42-48 (p, crescendo 42-45 from 46 to 68, decrescendo 45-47); the E flat 5 at qn 44.

**What is wrong (measured).** The crescendo dips at the E flat 5: 42 C5 -43.2; 43.5 C sharp 5 -38.7; 44 E flat 5 -40.2 (CC11 69.7, the highest of the phrase); 45 F5 -38.5; 47 E flat 5 -42.7. In c43 the same notes read -40.9, -38.7, -35.4, -34.9, -35.7: the line rose 3.3 dB into the E flat 5 where it now falls 1.5 dB. The oboe's E flat 5 fell 2.5 dB more than the rest of the track at c44. The second phrase (54-60) is even (-46.2, -40.3, -38.3, -39.1, -38.5, -41.8).

**Fix.** `build/note_trims.json`, "Oboe 1": add `"44": 2`. **Predicted:** -38.2, so the line reads -43.2, -38.7, -38.2, -38.5 and no longer dips. The F5 at 45, the printed top of the crescendo, is then level with the E flat 5 within 0.3 dB; in c43 it was 0.5 dB over it. The F5 carries an older note trim `"45": -7` and sits 2.5 dB under what the CC11 rise from 46 to 68 gives from the C5. Changing that trim to -6 (F5 at -37.5) would put the top of the crescendo on the F5; this is optional, and the actor should first check why 45 was set to -7. I do not propose a pitch trim on 75: the E flat 5 at 47 already sits at the p level it returns to, and the oboe's notes around 142 are an open item of another critic.

### 6. Re-check the per-pitch trims after any change of mics or family EQ

**Where.** Every wind and horn track; the tables `build/pitch_trims.json` and `build/note_trims.json`.

**What is wrong (measured for c44, inferred as a rule).** A change of mic mix or of an EQ bell near the harmonics of a patch changes pitches unequally, by up to 10 dB (Bassoon 1 A flat 3). The loop's checks compare families, solos and shares, and none of them compares one pitch of a track with its neighbours across renders, so the c44 shifts went unseen for four cycles and were patched note by note.

**Fix.** Add a per-pitch comparison to the actor's cycle check (for example in `tools/measure.py`, or the cycle's own check script): for each track, each sustained note of 0.9 quarter notes or longer, body level in the new render minus the previous render, minus the `vol_db` change, only for notes whose CC1 and CC11 agree within 1.5; group by pitch; print every pitch whose median differs from the track's median by 2.5 dB or more. Run it whenever `mics`, the family EQ or a patch changes. After findings 1-5, these pitches from the c43-to-c44 table remain flagged and uncorrected; all of them sound in a tutti or in an accompaniment, so I propose no value now: Clarinet 1 G5 and B flat 5 (256, 262, 268), C sharp 4 (176, 186) and B flat 4 (178); Clarinet 2 C sharp 4 and B flat 4; Oboe 1 E5 (210), B flat 5 (262) and A flat 5 (192; 266 already carries a note trim); Bassoon 1 B flat 3 (36, 229: about 2-3 dB more than the track) and E4 (210); Horn 3 B flat 4 (208); cor anglais A4 (152).

## Also measured, no change

- **Solo margins per bar (A / K).** Horn 1: bar 7 +8.3 / +8.0, bar 9 +8.5 / +6.4, bar 10 +6.7 / +3.8, bar 11 +8.3 / +8.1, bar 12 +10.0 / +8.9, bar 13 +5.2 / +4.5, bar 14 +7.8 / +5.8. Oboe 1: bar 15 +5.1 / +2.6, bar 16 +7.0 / +2.9, bar 19 +5.5 / +2.3, bar 20 +8.4 / +4.3. Violin I solo: bar 17 +10.2 / +6.4, bar 18 +10.5 / +8.1, bar 21 +7.5 / +4.0; bar 22 -0.2 / -2.3 as the tutti enters, which is right. Bass clarinet: bars 31-36 +7.6, +6.0, +5.4, +2.5, +6.0, +1.7 (A). Flute 1: bars 37-40 +7.1, +4.0, +7.7, +5.0 (A). Oboe 1 bars 45-46 +3.6 / +3.8 (A). Cor anglais bars 48-50 +4.0, +7.8, +3.4 (A). Horn 1 bar 69 +3.8 / +3.9.
- **Bars 61-64.** Bar 61: master -12.8; strings -16.5, brass -17.9, winds -19.8, timpani -32.0; Violins I -20.2, celli -23.2, Trombone 2 -23.8, bass trombone -24.1, tuba -26.4, basses -28.1. Bar 62: master -13.6; strings -17.2, brass -19.1, winds -19.9, timpani -39.6. The low brass are 3.6-6.2 dB under Violins I and the brass family 1.4 dB under the strings; nothing is covered. Summed winds against strings -0.3 dB at bars 61-62 (check44), which agrees with Rimsky-Korsakov's forte proportions for a doubled tutti. Bars 63-64: Trombone 1 -23.9 / -25.1 leads Violins I at -26.6.
- **Bars 79-80.** Master -18.3 / -19.5; strings -22.1 / -23.0, winds -22.2 / -24.2, brass -27.2 / -27.6, timpani -37.7 / -39.6. The celli counter-line equals Violins I at 262 and 265 in K-weighting, but the tune (Violins I with Flute 1) leads in A-weighting. No finding.
- **Timpani.** The f rolls sit 19-23.5 dB under the master at bars 61-62 (6.7 % of the 30-150 Hz energy) and 18.4-21.2 dB under at bars 79-80 (5.6 %). They cover nothing. They are low for a printed f, but the roll shapes are settled and I leave them. The ppp roll in bars 2-3 is 4.4 and 2.6 dB under the basses.
- **Dynamic mapping, note-body medians.** Winds ppp -52.5, pp -50.6, p -45.4, mp -41.3, mf -39.5, f -36.4, ff -33.8. Brass pp -49.3, p -48.1, mp -38.8, mf -35.4, f -29.7, ff -26.7. Strings ppp -54.8, pp -49.6, p -42.9, mp -40.6, mf -36.1, f -31.6, ff -30.5. Harp pp -48.9, p -47.4. Timpani ppp -57.4, pp -51.0, f -39.4. pp agrees across families within 1.3 dB. p spreads 5 dB because the brass p notes are horn accompaniment held under solos by roles. This matches Rimsky-Korsakov's statement that winds and one string department balance in piano.
- **Half sections.** Vc div pp -48.9 against celli pp -48.3. Opening chord: Violins I -48.2, Violins II -50.6, celli -51.2, violas -51.6.
- **String-led passages (A).** Bars 23-28: Violins I/II lead the celli by 4-8 dB and the violas by 8-11. Bars 53-56: Horn 1's counter-melody is 3-9 dB under Violins I. Bars 71-78: Violins I lead Violins II by 1-3 dB, the celli by 3-6, the violas by 6-8.
- **Bass.** The basses' full-section ppp pedal in bars 83-86 is -50.5 to -51.1 (K) and -66.5 (A); the 4 soli pp from bar 87 is -55.5. The 20-100 Hz share of the master in bars 83-86 is 42 % against 7-11 % in the other soft passages. The pedal shape and the coda rows are settled (c42 A #2); I note the number for critic C and propose nothing.
- **Dan's checks, from the actor's c48 files.** check44.txt: release medians strings 0.376 s, winds 0.304, brass 0.253; final stop d06 28.4 dB, t20 0.444 s; winds -1.9 and brass -2.2 against strings over the whole movement; side/mid -5.64 dB; correlation under 250 Hz 0.634. s1_c48.txt: repeat steps at Violas 271 (2.9), Violins II 289 (1.9), basses 253 (2.4). pcx_c48.txt: Violins I join timing median +20 ms. None of these is changed by the fixes above, which move single notes by 1 to 5 dB on four wind tracks and one horn track.
- **Two candidates dropped.** A K-weighted reading suggested the celli covered the clarinet in bar 89 and the basses covered the cor anglais in bar 84. A-weighted, neither holds (Violins I double the clarinet's C5 in bar 89; the bass energy is under 100 Hz).

**Do not touch:** the c44 mic positions and family EQs (correct their per-pitch consequences with pitch and note trims only); the hall and returns at their c44/c45 faders; the c30 CC1 map and horn CC1 57-72; c44 C #2's horn hairpin gain (`HP_SOFT_GAIN_AT["Horn 1"][20.0] = 3.0`) and the crescendo into bar 8; Horn 1's note trims at 24, 25.5 and 26, its c46/c47 roles and `[198, 203.9, 2.5]`, and the soft-horn loud_eq; the cor anglais c19 role `[127.5, 133.5, -3.5, 2.5]`; Flute 1's 136 note and its level shape; Oboe 1's +4.2 step at 148 and its 139, 145 and 266 trims; Clarinet 1's c23 row `[287.4, 289.0, 2.5]` and its `"289": 4` and `"292": -4` note trims; the coda balance rows and the basses' coda pedal shape; the bar 61-62 string holds, brass +3 and balance; the bar 63 CC7 lanes and Trombone 1's rows; the timpani roll shapes and the 277 step; the basses' f/ff trims and 35 Hz high-pass; the c46 tempo map, caesuras, brass bells and gains; the c47 fills and wind entry leads; the c48 fp chain, 315 Hz string bell and horn width 0.8; the harp level; the PHRASE_SHAPE floors; the final-chord re-bows.
