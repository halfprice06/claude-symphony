# Cycle 54, critic B: balance and levels (render under review: c53)

## Method

- Stems 01-32, the four return stems and the master of `cycles/c53/render` (the four string stems carry the post-render stem fix), `cycles/c53/render_first` for the unfixed strings, the data of `cycles/c53/rendered_build` (notes, CCs, mix) and `cycles/c53/build_fix` (the delivered envelopes of Violins I, Violins II, Violas, Violoncellos). c47, c51 and c52 from their own `render` and `rendered_build` for comparison.
- K-weighted and A-weighted power per 10 ms frame (4096-point FFT, the c50-c53 B scripts, so numbers compare). Note body = mean over 20-80 % of the note from its score onset. Fine curves are unweighted stem RMS in 30 ms steps. Low-frequency spectra are whole-passage FFTs of the files (the 4096-point frames smear below 100 Hz and are not used there).
- New this cycle: every sounding crescendo measured on its own stem against the envelope and the `soft_trim_db` / `dyn_trim_db` change across it (`trim.py` reimplements `build_reaper.py vol_points`); every slurred line scanned for notes 5 dB or more under or over both neighbours; the double basses' static 80 Hz cut inverted on the stem and summed into the master (exact, the EQ is linear and after Opus).
- I cannot hear the render. "Measured" and "inferred" are marked.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 54 (the schedule ends at c47), so no page range was read. `MANUAL-GAPS.md` was read.

| Source | Where it applies | Does the render follow it |
|---|---|---|
| May 2021 HO manual p.144 (true legato: a velocity around 50-60 gives a longer transition, 110-127 a shorter one); `MANUAL-GAPS.md` 6 | every string legato target plays at v124 | Not tried. At soft dynamics the v124 transition is 5-12 dB louder than the body it leads into (Violoncellos 77: transition about -35 dB before the notch, body -47 to -52). The notches of c53 removed the peaks; the weak bodies remain (finding 1). A lower legato velocity on the p cantabile lines is the untested alternative to per-note rows |
| `MANUAL-GAPS.md` 8 (DIV A / DIV B half sections, Close mics only) | Violas div bars 23-30, 80-81, 84-92; Violoncellos div bars 21-22, 83-86 | In use. The two viola halves differ by 5-7 dB in opposite directions inside one crescendo (finding 3) |
| `mockup-kit/LEARNINGS.md` section 5 (string joins: notch of peak minus 2 dB) | Violins I 65.5, Violins II 177, Violins I 86.5 | Two of the three are not transitions (finding 4) |
| `EW-TEMPLATE-PLAN.md` section 8 (basses: Duc's -3 dB at 228 Hz) | Double basses family EQ | Present. The older static cut at 80 Hz on the same track is the larger effect on the bass register (finding 2) |

## Slot questions from the loop lead

- **Do `soft_trim_db` / `dyn_trim_db` take back single-instrument crescendos here?** No, not as in the scherzo (measured). Of 169 crescendo rows in parts.json, 115 sound on their track. The trim falls across 109 of the 169 (by 3 dB or more in 37, by 5 dB or more in 8: Tuba 200, Violoncellos 78, Violas 146, Double basses 146 and 250, the divisi copies). On the stems 109 of the 115 still rise by 1 dB or more inside the hairpin or at its arrival; 6 do not (Bass clarinet 105-108, Bassoon 1 200-204, Horn 4 267-268, Harp 250-256, Violins I 68-69, Violoncellos 180-184). Violins I 68-69 is a false alarm (the crescendo is played as a +5.6 dB step onto the E flat 5 at 68). In the others the trim's share is 0.3-2.1 dB; the rest comes from role and note rows (finding 3). The families do not drift apart: woodwinds against strings (K) go -10.8 dB at qn 188, -5.3 at 196, -3.2 at 204; in the second build -8.8 at 250, -4.5 at 259, +0.1 at 262. Brass against strings -9.4 at 188, -6.4 at 196, -1.3 at 204. The winds gain on the strings in every crescendo into f and ff, so no change to the trim tables is proposed.
- **Remaining transition peaks.** Finding 4.
- **Horn 1 breath at 196.** Finding 5: the gap is deep enough; the pickup before it is too soft.
- **Violoncellos 68 reading -65 ms and 77 reading -49 ms.** 77 is real and is a level problem: the G3 sounds at -42 to -43 dB for 200 ms before the beat (its transition, already notched by 7.9 dB) and at -47 to -52 dB after the beat (finding 1). 68 is the measure: a 1-2 dB bump 270 ms before the beat, a dip to -43 / -44, then the A flat 3 at -40 on the beat and steady (measured curve, inferred reading).
- **Low-mid weight.** Finding 2. The 140-355 Hz share is high partly because the octave below it is thin.

Routine checks (measured, K; same script on c52 in brackets): solo margins Horn 1 bars 7-14 +8.4 (+7.5); Oboe 1 15-16 +3.5 (+3.1); Violin I solo 17-18 +7.6 (+7.1); bass clarinet 31-36 +5.3 (+5.3); Flute 1 37-40 +4.7 (+4.3); cor anglais 41-44 +2.7 (+1.9) and 48-50 +2.8 (+2.5); Horn 1 67-70 +7.0 (+7.0); Clarinet 1 85-89 +0.8 K / +3.3 A (+0.7 K). The rises come from the Harp's new 200 Hz bell (the harp accompanies each of these solos). Climaxes: bar 61 strings -16.7, brass -17.9 (low brass -19.8), woodwinds -19.8, timpani -32.0; bar 79 strings -22.4, woodwinds -22.2, brass -27.2, timpani -37.7: as c52, nothing covers. Dynamic mapping (A-weighted medians of note bodies of 0.6 s or longer): pp woodwinds -55.4, horns -54.6, strings -53.9, divisi and solo -54.7; p -45.7 / -45.8 / -47.3 / -48.0; f woodwinds -39.2, horns -34.3, strings -34.2; ff -35.6 / -30.1 / -29.7. Violoncellos against all other stems in bars 22-27: -4.6 -> -6.4 dB (c52 -> c53).

## Findings

### 1. Eleven notes inside slurred lines sit 5-13 dB under both neighbours; they have done so since c47 at least

Where and evidence (measured; body of the note before / the note / the note after, dB; c47, c51 and c52 read within 0.7 dB of these values, so they are stable and not a c53 effect):

| Track, qn (bar) | Pitch, printed level | Before / note / after | Fine curve |
|---|---|---|---|
| Flute 1 133.5 (43) | A flat 5, dim. toward pp | -44.5 / **-57.5** / -45.4 | falls from -48 at the beat to -62 at +0.24 s |
| Flute 1 135 (43) | E flat 5 | -45.4 / **-53.2** / -48.4 | |
| Flute 1 199 (59) | B flat 5, f | -33.5 / **-42.3** / -35.5 | -42 to -47 for the whole quarter |
| Violins II 47 (16) | G4, pp, A flat-G-A flat | -45.1 / **-57.7** / -48.0 | -57 to -60 from the beat on |
| Violoncellos div 63 (22) | G3, pp, the answer to the solo violin | -44.4 / **-55.1** / -47.0 | -54 to -58; `level_fits.json` carries a -4.6 dB row on this note |
| Violoncellos 68.5 (23) | G3, p cantabile | -40.5 / **-44.9** / -37.1 | -39 before the beat (transition), -44 to -48 after |
| Violoncellos 240.5 (71) | G3, the same figure | -41.6 / **-48.1** / -40.6 | -40 to -43 before the beat, -47 to -51 after |
| Violoncellos 249 (73) | G3 | -43.0 / **-47.3** / -40.5 | |
| Violoncellos 77 (26) | G3 | -44.5 / **-47.0** / -39.6 | -42 / -43 before the beat, -47 to -52 after |
| Violoncellos 199 (59) | E3, f | -31.4 / **-37.0** / -30.8 | |
| Bassoon 1 201 (59) | F3, f, doubling the celli | -37.1 / **-42.5** / -33.9 | |

What is wrong: each of these is a note of a melody or counter-melody that drops to the level of a dynamic one or two steps lower and comes back on the next note. In the cello counter-melody the c53 notches (correctly) removed the transition peaks at 68.5, 240.5 and 77, and what is left is a transition at the line's level followed by a body 5-8 dB under it: the loudest part of the note now lies before the beat. That is also why S reads 77 early. Seven of the eleven are the lower neighbour in a semitone or whole-tone figure (A flat-G-A flat or A flat-G-F); cause not established (inferred: the legato target's sustain layer at CC11 33-49).

Fix (level only, can go in by `stem_fix.py`; rows in the c53 form, rising from -0.06 s to the beat and held to the note end, so they do not move S):
- `build/level_fits.json` "Violoncellos": "68.500" +4.0, "240.500" +6.0, "249.000" +4.0, "77.000" +4.0, "199.000" +4.5 (predicted bodies -40.9, -42.1, -43.3, -43.0, -32.5).
- `build/level_fits.json` "Violoncellos div" "63.000": replace the -4.6 dB row by +3.5 (predicted -47.0).
- `build/level_fits.json` "Violins II" "47.000": +7.0 (predicted -50.7, between the note before and the dim. it stands in).
- `build/note_trims.json` "Flute 1": "199" +7.0, "135" +4.0; "Bassoon 1": "201" +6.0 (0.1 s ramps).
- Flute 1 133.5 as a `LEVEL_SHAPES_S` row because the note decays inside itself: seconds from the note-on, (0.0, 0) (0.08, 4) (0.20, 10) (to the note-off, 10), then 0 in 60 ms (predicted -47 to -51 throughout).

Acceptance: none of the eleven more than 3 dB under the mean of its neighbours; `s_onsets.py` on Violoncellos 77 and 68.5 within 25 ms; celli against the other stems in bars 22-27 back near -5 dB.

Judgement: levels measured on four renders; the cause inferred; the predictions assume the envelope is linear in dB.

### 2. The double basses' static 80 Hz cut sits on this movement's dominant and takes 3.5 dB off the tonic's strongest partial; the master's 63-100 Hz bands are 5-11 dB under the Brahms references

Where: `build/mix.json` "Double basses" `eq` band `bell2` (80 Hz, -6 dB, 1 octave; series 1 c25). The basses supply 75 % of the master's 56-112 Hz energy over the whole movement and 84-99 % in bars 23-30, 61-62, 71-78 and 79-81.

Evidence (measured):
- What the basses play: A flat 1 (51.9 Hz) for 71 s, E flat 2 (77.8 Hz) for 42 s, D flat 2 (69.3 Hz) for 28 s, B flat 1 for 21 s. On every A flat 1 the fundamental is 10-20 dB under the octave, so the tonic's weight is at 104 Hz; on E flat 2 the fundamental is now 2-6 dB under its octave, on D flat 2 level with it. The bell is centred between E flat 2 and D flat 2 (-6 and about -5 dB) and still gives about -3.5 dB at 104 Hz.
- Master third-octave bands relative to the total, whole movement, against Brahms 1/ii and 4/ii (`symphony/render/critics/c04/ref_*/metrics.json`): 63 Hz -20.2 (Brahms -11.5 / -11.3), 79 Hz -23.7 (-13.4 / -12.2), 99 Hz -18.0 (-13.2 / -12.9), 125 Hz -13.2 (-14.4 / -11.8), 198 Hz -12.3 (-16.1 / -15.1), 315 Hz -9.0 (-14.3 / -13.8). The 20-100 Hz share is -17.3 dB against -8.5 / -7.9. So the low-mid excess that c53 worked on stands beside a larger shortage one octave lower. (The Brahms 63 Hz band rises 17 dB over its 50 Hz neighbour in both recordings and may hold hum; the 79 and 99 Hz bands are the safer comparison.)
- Simulation on the c53 basses stem and master, bell2 at -2 dB instead of -6: bands 63 / 79 / 99 Hz whole movement -20.2 / -23.7 / -18.0 -> -17.1 / -21.1 / -16.1; 20-100 Hz share -17.3 -> -14.5; 140-355 Hz share -5.81 -> -5.93. Bars 71-78: 79 Hz -16.8 -> -13.1. Bars 65-70 (the E flat pedal under Horn 1): 79 Hz -18.7 -> -14.9. K-weighted master level per bar rises by 0.85 dB at most (bars 83-84, the coda pedal), under 0.5 dB in every other bar; master sample peak 0.581 -> 0.592. With the bell removed: 63 / 79 / 99 Hz -15.6 / -19.6 / -15.0, share -13.1, K rise 1.4 dB in bars 83-84, peak 0.599; the 99 Hz band in the coda goes from -8.6 to -6.5 dB of the total, which is why I stop at -2.

Fix: `build/mix.json` "Double basses" `eq` `bell2` db -6 -> **-2** (`--mix-only`; level-only, so it can be previewed on the stem with a +4 dB bell at 80 Hz, 1 octave). Leave the climax `loud_eq` (100 Hz shelf -3 at qn 199-215 and 257-270) as the guard for the D flat 2 at 204 and 262. The c41 `loud_eq` bell (80 Hz +4 dB, 0.5 oct, qn 254-261.9) was added to undo bell2 there; reduce it to +2 so bars 76-78 do not move twice.

Acceptance: 79 Hz band over the whole movement at -21.5 dB or higher; bars 83-84 K level up by no more than 1 dB; master 56-71 Hz at qn 262-268 not above -13 dB of the total (simulated -13.5; if it is, deepen the second `loud_eq` window's shelf to -4.5). Not checked here: the low shelves at 70 Hz -4 dB on Contrabassoon and Tuba (the contrabassoon's A flat 1 pedal of bars 31-36 lies under the shelf); they carry 1-2 % of the band.

Judgement: spectra, pitch table and simulation measured; that more weight at 63-100 Hz reduces the "mushy" impression is inferred.

### 3. Two crescendos fall at their top: Violas bars 27-28 and Bassoon 1 into bar 61

Where: Violas qn 78-82 (p, cresc. to the mf at 82; lower half on Violas, upper half on Violas div); Bassoon 1 qn 196-212 (f, cresc. from 200 to the ff at 204).

Evidence (measured):
- Violas, lower half: C4 at 78 -45.6; A flat 3 at 79 -38.0; D flat 4 at 81 **-44.8** and at 82 (the mf) **-45.6**. Upper half (Violas div): -50.3, -45.5, -39.8, -40.1. The halves differ by +4.7, +7.5, -5.0, -5.5 dB. Both together: -44.3, -37.3, -38.6, -39.0, so the section peaks one quarter into the hairpin and is 1.7 dB lower at its mf, while Violins I go -37.3 -> -34.3, Violins II -38.5 -> -31.8 and the celli -39.6 -> -33.9. The D flat 4 on Sus MAX at CC11 71 plays at the level of the C4 at CC11 52; after the re-attack at 81 the stem falls from -38 to -46 in 0.2 s. Unchanged since c47.
- Bassoon 1: f bodies 196 / 198 -32.8 / -33.0; then 199 -36.1, 200 -36.9, 201 -42.3 (finding 1), 202 -33.8; ff bodies 204-210 -33.8, -33.5, -33.9, -33.6. Its ff is 1 dB under its f; the envelope steps from +6.0 dB at 198 to between -3.2 and +3.8 dB in bars 61-62 (role [200, 204, -4] plus the trim's -1.5 dB from f to ff). Every other woodwind rises 3-8 dB from bar 59 to bar 61.

Fix:
- `build/level_fits.json` "Violas": "81.000" +5.0 from +0.05 s (the A flat 3 ends 35 ms after the beat) to the note end, "82.000" +5.0 (predicted -39.8, -40.6; both halves together -36.8 and -37.3, a rise of 7 dB from p to mf). Keep the -5 dB gap shape at 81.
- `build/roles.json` "Bassoon 1": [200, 204, -4] -> [200, 204, -1], and `mix.json` Bassoon 1 `dyn_trim_db` ff 1.5 -> 3.0 (predicted bars 61-62 -32.3, the level of its f; woodwinds in bar 61 +0.1 dB).

Judgement: measured; predictions linear in dB.

### 4. The three listed peaks: two are swells inside the note before, one is a transition over a weak body

Evidence (measured, 30 ms steps, time from the beat):
- **Violins II 177** (bar 54): D flat 5 (176) at -35 to -37 dB, a burst of -31 / -30 at -0.33 to -0.27 s, back to -35; the note-on of 177 is at -0.23 s, so the burst is 40-100 ms before it. Spectrum of the burst: the D flat 5 fundamental +6 dB, its harmonics +3 / -3, the C5 absent. It is the old note swelling, not the new note. Half of it is the c52 body row on 176 (+2.3 dB to -0.25 s); in c51 the same place read -34. Master -28 against -30.
- **Violins I 65.5** (bar 22): E flat 5 (65, the entry, v63) at -40 / -41, then -37 / -36 at -0.27 to -0.21 s; note-on of 65.5 at -0.14 s. Again on the old note, 0.47 s into it. Identical in c50-c53.
- **Violins I 86.5** (bar 29, dim.): transition -41 / -42 from -0.24 to -0.09 s under the existing -4.1 dB notch, then the B flat 4 body at -46 on the beat falling to -51 at +0.18 s. The peak is 3.5 dB over the note before and 5-9 dB over its own body.

Fix (`build/score_config.py` `JOIN_NOTCH_S`, seconds from the target's moved note-on; negative starts are already in use at 86.5):
- "Violins II" 177.0: (-0.12, -0.02, -4.5).
- "Violins I" 65.5: (-0.14, -0.05, -3.0).
- "Violins I" 86.5: depth -4.1 -> -6.0 on the same window, and a body row in `level_fits.json` "86.500" +2.5 from the beat to the note end (predicted peak over body 5-9 -> under 3 dB).
The first two windows end before the new note's note-on, so they do not touch the level `s_onsets.py` takes its reference from.

Judgement: curves and spectrum measured; "swell of the sample" inferred.

### 5. Horn 1 breath at 196: leave the gap, raise the pickup

Evidence (measured): E flat 4 (193) -30 dB to -0.48 s; pickup F4 (195.5) -33 to -37, mean -35 (K body -35.5, c52 -36.4); gap floor -42 at -0.12 s; F sharp 4 from -0.06 s at -31 rising to -28. The floor is 12 dB under the note before and 14 dB under the note after, but only 7 dB under the pickup, because the pickup is 5.7 dB under the E flat and 8.3 dB under the F sharp. From -0.45 to -0.06 s the stem is 5-12 dB under the line: pickup and breath together read as one 390 ms hole. The +4 dB shape of c53 raised the pickup by 0.9 dB only (the F4 pitch trim's -5 dB body part still applies at CC11 86).

Fix: `LEVEL_SHAPES_S` Horn 1 195.5: +4 -> **+7.5 dB**, still ending at the note-off (predicted pickup -32, breath dip against it 10 dB, against the E flat 12, gap floor unchanged). Do not deepen or lengthen the gap: its floor is the horn's release in the hall (S3). The master shows no dip at 196 in 30 ms steps (-25 / -24 / -22), the strings play through; the breath is a matter of the horn line only.

Judgement: measured; prediction linear in dB.

## Checked, no change proposed

- Trim tables (`soft_trim_db`, `dyn_trim_db`): see the slot answer. The per-family levels at each printed dynamic agree within 1.6 dB from pp to p and the families converge through both crescendos.
- Horn 1 bars 7-14 margin +8.4 K: 0.9 dB more than c52 through the harp bell; the accompaniment stems sit 12 dB under the horn. In order for "dolce espr." over pp (inferred); do not widen it further.
- Bass clarinet 105-108 (pp cresc. to p under the flute's entry): 106 / 107 read -46.0 / -44.9 after the long A flat 2 at -41.6. A 4 dB step down, then +1.1; small, left.
- Timpani and low brass at bars 61-64 and 79-82: as c52.

## Do not touch

Everything on the c50-c53 B lists; the c53 `JOIN_NOTCH_S` rows (the peaks they removed must stay removed: finding 1 lifts the bodies after the beat, not the transitions); `soft_trim_db` / `dyn_trim_db` tables other than Bassoon 1 ff; the Violoncellos 170 Hz bell at +1.5 and the Harp 200 Hz bell; the basses' 140 Hz bell, 228 Hz cut and climax `loud_eq` shelf; the breath gaps at 196 and 204; the Violas 81 gap shape; the Horn 1 rows at 190 / 192 / 198; hall, sends and `deliver` settings.

Scratch folder: `/private/tmp/claude-501/mockup-loop/mvt2-c54-B/` (175 MB: frame-level caches of the c53 stems, no audio; `lib.py`, `trim.py` and `c1.py` crescendos against envelope and trims, `c2.py` family levels, `nb.py` note bodies, `m1.py` margins, mapping and line outliers, `h1.py` notes across cycles, `j1.py`-`j3.py` fine curves and the 177 spectrum, `e1.py`-`e3.py` bass spectra and the 80 Hz simulation). Left in place, as the loop lead's notes ask.
