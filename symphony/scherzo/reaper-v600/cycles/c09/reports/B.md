# Cycle 09, critic B (balance and levels), on the c08 render

Method. I computed K-weighted levels (the BS.1770 weighting applied in the frequency domain, 2048-point frames, hop 1024) for every stem, return and the master of `cycles/c08/render/`, on the `build/parts.json` tempo map. Levels are energy means over the qn spans named. "Note body" means the level over the note's own first 0.4-1.0 qn. Values are on one common scale and can be compared with each other, not with LUFS. For c07 and earlier I used the per-bar stem levels in `cycles/cNN/metrics/metrics.json` (plain RMS) and c07's surviving `00_Master.wav`. Score marks come from `build/mockup-events.tsv`; data come from `build/parts.json` and its c07 copy in `cycles/c08/before/parts.json`. Bar b starts at qn 3(b-1).

## Manual notes (cycle 9, slot B: group B3, May 2021 HO manual PDF pages 123-126, read in full; MANUAL-GAPS.md read)

| Manual (PDF page) | Where it applies here | Render follows it? |
|---|---|---|
| p.123 Timpani Felt Long (= KS row C0): velocity sets up to 16 layers, round robin x2; left-hand variations on C1-A2 and right-hand on C3-A4; two notes within 65 ms play a damped double hit | motive x strokes (Lng row, v80-98 in the tuttis); `TIMP_RH_ALT` sends repeated strokes alternately to pitch 47 (left-hand range) and 71 (right-hand range), e.g. qn 298 / 298.5, 310 / 310.5 | Yes. Strokes at quarter 264 are 114 ms apart, so the 65 ms double-hit rule never triggers |
| p.124 Felt Rolls (KS D#0): CC1 sets the dynamic over 8 layers; CC11 and velocity set loudness | rolls 101-103, 129-130, 205-208, 237-240, 285-286, 303, 332, 336 on "Flt Rls" with CC1 ramps (e.g. 60 -> 79 over 300-307) and the level in vol_db (+18 dB on the roll) | Yes. CC1 shapes the crescendo and the envelope sets the level. Rolls rank 5th-14th of 31 stems in their bars and never lead (Dan's rule 5 holds) |
| p.124 Felt Short (KS C#0): muted hits for stops "within a beat or two" | `TIMP_STAC_ROW` plays the 7 printed staccato strokes on Sht; the G.P. after the summit uses the CC7 damp (`TIMP_DAMP_AT`) | Yes |
| p.123, p.125 Felt / Hard Cresc (KS E0): recorded crescendos in three speed ranges, 2 velocity layers | the printed crescendo rolls (101-103, 205-208, 303) | No (MANUAL-GAPS #7). Not a balance problem: the CC1 rolls already sit under the texture |
| p.125 Hard Long: "a brighter timbre overall than in the case of felt mallets"; Hard KS has the same five rows on C0-E0 (p.125-126) | the score prints "hard sticks" for bars 1-340 and "soft sticks" from 341 | No (MANUAL-GAPS #6). Through my lens: the felt drum blends and does not cover (tutti 105-120 timpani -33.5 against Violins I -22.5). Hard sticks would give the strokes more presence at the same level (inferred). Swap the rows only, then re-fit `TIMP_ROLL_TRIM_DB` |
| p.123-126 all timpani patches: "CC 11 and Note Velocity control overall loudness" | the Timpani track has no CC11 lane; every level is in vol_db or velocity | Yes. Level corrections belong in vol_db or velocity, as now |

## Is c08 too dry, thin or dull in my passages? (measured: master band shares, c07 -> c08)

No. The body bands (100-2000 Hz) moved by 1 dB or less in every passage: theme 13-28, second idea 45-56, tutti 105-120, trio 153-168 and 209-224, codetta, solo, close and summit. Only the ends changed: 6-20 kHz dropped 3-4 dB (theme -24.1 -> -28.4, tutti -26.6 -> -30.4, trio ff -23.7 -> -27.5, summit -22.9 -> -27.1; references -28.8..-32.2), and 20-100 Hz dropped 1-2.7 dB in the tuttis and the close. The trio clarinet and the codetta were already dark in c07 (6-20 kHz -42) and are unchanged. The solo (349-356) is still the brightest passage (6-20 kHz -22.5), which is for the blend lens. The sub. p's keep their hall: R Strings falls 4.8 dB over the first 0.25 qn of bar 121 while the master falls 3.6 dB.

## Findings, ranked by what a listener would hear

### 1. Violas: the open legato SPREAD and the "3 dB louder" stem come from the build mode, not the data. Every render in which the Violas track got a MIDI-only rewrite came out in a second state, 1.5-2 dB louder in its legato passages, with joins 20-40 ms early (measured over nine renders; mechanism inferred)

**Where.** Violas legato passages: second idea 45-56 (qn 132-168), 129-132 (387-396), trio f 194-205 (579-615), 286-288 (855-864). These are the four passages the probe flags.

**Measured.** The Violas notes, keyswitches, CC1, CC11 and vol_db are identical to c07's over 132-161 and 575-615. I diffed `cycles/c08/before/parts.json` against `build/parts.json`. Only 129-132 differs, because of the new `SHORT_CC11_PARK` on the shorts before it. Over the same bars the stem and the probe still differ. Violas per-bar levels from each cycle's metrics.json (energy mean of bars 45-56 / 194-205, plain RMS dB) against the probe's legato window:

| cycle | 45-56 | 194-205 | window median (limit 90) | how the Violas track was built |
|---|---|---|---|---|
| c03 | -36.7 | -40.0 | 92 ms | full build of all 31 tracks (ir_setup) |
| c04 | **-35.3** | **-38.5** | **116 ms SPREAD** | `--midi-only`, Opus state not reloaded (CHANGES c04 line 33) |
| c05 | -36.4 | -40.0 | 92 ms | full rebuild (ir_setup 0.7) |
| c06 | -37.0 | -41.3 | 88 ms | full rebuild (template mix) |
| c07 | -37.1 | -40.2 | 88 ms | strings fully rebuilt (mics, release caps) |
| c08 | **-35.4** | **-38.6** | **115 ms SPREAD** | `--midi-only`, Violas state not reloaded (only V1, V2, horns and Tp2 were rebuilt) |

The match is exact in both directions. Both MIDI-only renders show +1.5-2 dB in exactly these passages, with the probe's pcX median at -22 and -37 ms. Every full-build render is in the normal state. The violas' theme-A accompaniment (13-28: -50.3..-51.0 in every cycle) and their staccato passages do not move, so the effect is in the legato rows. The c04 entry in loop/LEARNINGS ("flip ... between renders with identical data") is this same effect.

**Judgement (inferred).** Opus keeps some state in the saved instance (README: "Opus stores start-mode controller values in the saved state") that the save after one render carries into the next whenever the instance is not reloaded. The legato script then plays the violas' joins earlier and louder: an inner voice 2 dB forward in the second idea and the trio's f, with smeared joins. I could not tell from the stem which parameter it is. The old pitch's partials after a join decay about as fast as in the other string sections, so the stem does not show an obvious mono/poly flip.

**Fix.**
1. In c09, after the `--midi-only` build, fully rebuild the Violas track: `build_reaper.py build/parts.json jobs Violas` (no `--midi-only`; the ONLY list reloads the Opus state from the patch). Do the same for any other string track that is not already rebuilt this cycle. Celli and basses were also MIDI-only in c08; they show no flag, but they share the same risk.
2. Before the rebuild, copy the Violas FX state chunk out of the saved `.rpp`. After the rebuild, diff it against the new one. The parameter that differs is the cause, and it should go into LEARNINGS.
3. Generic option (tools/build_reaper.py): a `--midi-only` rule that also fully rebuilds every track using a "Leg" row, or a check after each render that compares each legato track's level in its legato windows with the last full-build render.
4. Expected: Violas 45-56 about -36.5..-37 (plain RMS), 194-205 about -40..-41, probe window at most 90 ms, with no data change.

### 2. The woodwinds' f staccato plays softer than their p staccato: Flute 1 sits 8.4 dB under Oboe 1 on 34 unison f staccatos, and the theme's flute disappears at every f arrival of the counterstatement (measured)

**Where.** Flute 1 (and Flute 2 and the cor anglais where they double) at the f staccato theme heads: qn 114-129 (bars 39-43), 204-212 (69-71), 393 (132), 816-825 (273-275), 861 (288), 888-896 (297-299).

**Measured.**
- Median note body of the staccato notes by printed dynamic: **Flute 1 p -41.7, mf -35.0, f -43.0, ff -28.0**. The f is 1.3 dB under its own p. Cor anglais: p -40.9, f -42.3, ff -35.5. Oboe 1 is ordered correctly (p -44.3, mf -37.9, f -36.3, ff -32.4), as are Violins I (p -37.0, f -30.2, ff -21.4).
- The same pitch on the same row: Flute 1 E5 at p (qn 84, v64, CC11 46) -39.2 against E5 at f (qn 205, v96, CC11 82) -45.6. A5 at f -42.5..-44.3.
- Unison Flute 1 / Oboe 1 (same onset and pitch): f staccato Oboe 1 over Flute 1 by median **+8.4 dB** (n 34; 13.1 dB at qn 120, 11.0 at 204, 13.7 at 816). The same pairs differ by -0.2 at p staccato, +0.8 at f legato and -3.5 at ff staccato.
- Bar 41 (the f arrival): Flute 1 -43.1, Oboe 1 -29.8, Violins I -27.8.
- Cause (read, `tools/build_reaper.py` vol_points and `build/mix.json`): the trim table interpolates p +5 (CC46), mf +2.5 (CC72), **f -4 (CC88)**, ff -1 (CC114) for both flutes. The f anchor is a 6.5 dB notch between mf and ff. The legato f notes are matched to the oboe at that trim, but the staccato row (level by velocity, `_WSTAC` f 96) does not gain the 6-9 dB the trim takes away. The cor anglais has no notch (f 0); its f staccatos sit low on the row itself.

**Judgement (inferred).** At each f arrival of theme A's counterstatement, the flute half of the flute-oboe unison drops out, and the line turns into a solo oboe. The theme's top colour changes exactly where the score asks for more.

**Fix.** Raise the f staccato and its Sus pickup without touching the f legato notes, which are balanced.
- `build/roles.json` "Flute 1": add `[114.9, 124.9, 6]`, `[125.9, 130, 6]`, `[203.9, 208.9, 6]`, `[209.9, 213, 6]`, `[392.9, 393.9, 6]`, `[815.9, 820.9, 6]`, `[821.9, 826, 6]`, `[860.9, 861.9, 6]`, `[887.9, 892.9, 6]`, `[893.9, 897, 6]`. These windows leave out the Leg pairs at 125, 209, 821 and 893. Use steps, as for struck shorts.
- "Flute 2": add `[119.9, 124.9, 5]`, `[125.9, 130, 5]`, `[815.9, 820.9, 5]`, `[821.9, 826, 5]`. "Cor anglais": add `[119.9, 124.9, 4]`, `[125.9, 130, 4]`, `[815.9, 820.9, 4]`, `[821.9, 826, 4]`.
- Targets: Flute 1 f staccato median about -37 (above its p, under its ff), 2-3 dB under Oboe 1 in unison, still 7+ dB under Violins I.
- Check the existing Flute 1 roles, which do not overlap these windows (`[132, 150, -3]`, `[828, 840, -3.5]`).
- Generic note for later: in vol_points the f anchor should not dip below both its neighbours on a track whose staccato row has no CC11 level.

### 3. Theme tuttis 105-120 and 305-320: the violas' ff "non div." chords sit 10.6 dB under Violins I and 6-7 dB under Violins II's shorts at the same velocity, which leaves the middle of the ff chord hollow (measured; norm inferred)

**Where.** Violas qn 313-360 and 913-960: 54 double-stop quarters on "Staccatissimo RRx16" at v95, CC11 parked 120, plus 6 Sus MAX notes.

**Measured.**
- Note bodies: Violas -33.0 (105-120) / -33.2 (305-320), Violins II Spiccato / Stac -25.8..-27.1, Violins I -22.4, celli -30.5, basses -34.3.
- Section means: Violas -34.3 / -34.9 against celli -28.1 / -27.7. In the f hemiola just before (101-104) the violas sit at -28.0, and in the coda build 333-338 at -26.3 / -21.2 (6 dB under Violins I).
- The row is weak at this velocity. Its ROW_TRIM_DB entry (-4) is not applied here (`row_trimmed` is empty over 312-360, since there is no Leg neighbour), so the cause is the row, not a trim.
- Unchanged since c07, so this is a standing balance, not a regression.
- Norm (inferred): the double stops fill the harmony between the celli's tenor countermelody and Violins II. In the ff tutti a 12-player viola section on double stops should sit near the celli, as the violas do at 333-338.

**Fix.** `build/roles.json` "Violas": add `[312.5, 360, 4]` and `[912.5, 960, 4]`. No violas legato notes fall in these windows. Target: note bodies about -29, level with the celli and 6-7 dB under Violins I. Check after the render that the master's 250-500 Hz share at 105-120 stays within 0.5 dB of now (-6.4 dB).

### 4. Trio f, bars 197-203: Clarinet 2's held accompaniment E4 is the loudest stem of bar 197, 7 dB over Clarinet 1's espress. tune, and its p chord tones lead the p strings in 201-203 because of a pitch trim (measured)

**Score.** qn 588: Clarinet 1 f espress. (the tune, 9 notes); Clarinet 2 f, held chord tones (E4 for 5.8 qn, then D4, C4); at 600 Clarinet 2, bassoons and strings p.

**Measured.**
- Bar 197: Clarinet 2 -28.6, Clarinet 1 -35.8, violas -32.4, Violins II -32.6.
- Per note: Clarinet 2 E4 at 588 -28.6, against Clarinet 1's tune notes 588-596 at -33.2..-38.4. Both are on Leg Slur Rep at the same CC1 / CC11, with vol +4.0 (Cl2) and +5.6..+6.5 (Cl1). E4 has no pitch trim, so this is the sample.
- 600-606 (p): Clarinet 2 -33.3 / -35.3 / -35.9 against violas -37.9..-41.0, celli -40.6..-41.8, Bassoon 1 -40.0..-46.4. Clarinet 2 is the loudest stem of bars 202-203.
- The C sharp 4 at 600 gets `pitch_trims.json` "Clarinet 2" `"61": 4.0`: the same pattern as c08's Clarinet 1 108 (a trim fitted on line notes, landing on a held chord tone).

**Fix.**
- `build/note_trims.json` "Clarinet 2": `"588.0": -6`. Target: 3-4 dB under Clarinet 1's tune.
- `build/pitch_trims.json` "Clarinet 2": add `"_skip_onsets": [600.0]`, and `build/note_trims.json` "Clarinet 2" `"603.0": -2`, `"606.0": -2`. Target: Clarinet 2 at 600-608 about level with the p violas (-38..-40).

### 5. Counterstatement crescendo, bar 39: one celli G2 staccato is the loudest event of bars 37-40, 2.5 dB over Violins I's theme and 8 dB over the flute and oboe carrying it (measured)

**Where.** Violoncellos qn 111 and 114 (bars 38-39), G2 (pitch 43) downbeat staccatos on Stac RRx9 in the p < f bass of the counterstatement.

**Measured.**
- Celli note bodies along the crescendo: 108 v57 -38.9, **111 v64 -31.9, 114 v72 -25.8**, 117 v80 (D3) -34.9, 120 v87 (D3) -38.9. The level should rise steadily; instead the G2 notes jump 7 and 13 dB over the first one and then fall 9 dB at the next pitch.
- Bar 39 K levels: celli -30.3, Violins I -32.7, Flute 1 -37.8, Oboe 1 -39.7, Clarinet 1 -34.8.
- The step 64 -> 72 is a layer boundary on the HO short rows (velocity switches the layer, about 10 dB: Movement I c51), on the open G string.

**Fix.** `build/note_trims.json` "Violoncellos": `"111.0": -3`, `"114.0": -8` (steps). Target: a smooth rise of about 2 dB per bar, about -36 / -34 / -35 / -33 at 111 / 114 / 117 / 120, with the bass under Violins I. The alternative is `VEL_SET` 114 -> v66, which stays on the lower layer.

### 6. Tutti flutes: Flute 2 plays E6-A6 2-5 dB over Flute 1 on the same notes, so in bars 108-110 the second flute is the loudest stem (measured)

**Where.** Flutes 1-2 in unison an octave over Violins I in the ff theme tuttis, qn 312-360 and 912-960.

**Measured.**
- Flute 2 minus Flute 1 on identical onsets by pitch: 87-93 (D sharp 6-A6) +2.0..+4.9 dB (912-960) and +0.9..+4.3 (312-360). 75-84 -1.2..-8.0 dB.
- Bar 110: Flute 2 -20.4 against Violins I -21.8 and Flute 1 -23.4. Bar 108: Flute 2 -23.4 against Flute 1 -29.2.
- Same rows and velocities on both tracks (Stac DblTng v112, Leg Slur v100). Flute 2 is a different player's sample set (manual p.108), so the difference follows the register.

**Fix.** `build/pitch_trims.json` "Flute 2": `{"87": -2.5, "88": -3, "89": -3.5, "90": -2.5, "91": -2.5, "92": -4, "93": -4}`. These pitches occur only in the f/ff passages. Target: Flute 2 within 1 dB of Flute 1 per note, and the flute pair at or under Violins I in every tutti bar. Keep c05's G6 roles on Flute 1.

## Measured and in balance (for the record)

- Theme A 13-28: Violins I 12-15 dB over the pizz. basses, celli and violas, and 24 dB over the timpani.
- Counterstatement call and response 29-36: Violins I -43.3, Flute 1 -43.7, Oboe 1 -44.8.
- Sub. p 121-124: Violins I -33.7, Violins II -38.5 (the c07 gap of 7.5 dB is now 4.8), clarinets -44.
- Trio:
  - Clarinet 1 8 dB over the harp and 12-16 dB over the horns' drone (153-168).
  - Celli 8.4 dB over the con sord. Violins II (169-176); Violins I 3.6 dB over the celli (177-184).
  - Oboe 1, then celli, over the harp (185-192).
  - ff T 209-216: Violins I -30.5, Violins II -32.3 (c08's fix: V2 now 4 dB over the celli), Violas div within 1 dB of the violas.
- Codetta: Oboe 1, Clarinet 1 and Bassoon 1 each -33..-36 in turn.
- Trumpets at 105-120: Trumpet 1 -34.6 / Trumpet 2 -36.0, 12 dB under Violins I.
- Timpani rolls: never the loudest stem.
- Summit 336-338: strings -13.1, woodwinds -16.2, horns -24.8, trumpets / trombones / tuba -24.5, timpani -29.9. The brass weigh in under the fff without accents, and the summit is the master's loudest passage.
- Solo 349-352: 6 dB over Flute 1 and 9.5 dB over Violins II "la metà".
- Hn 1's motto: 8.4 dB over the violas. The close 368-371 is now +2.9 dB over 364-367 (was +5.7).

Do not touch: c08's Violins II trims and the celli roles at 624-672; the Horn 1 close role (+6); the Trumpet 2 StacSs row; the contrabassoon and low-brass roles at 309-360; the timpani 84 Hz bell off and its trio stroke steps; the summit's string-over-brass order with no brass accents; the subito roles at 121 and 277; the harp caps under the trio tune; the solo / flute / celli roles at 349-356.
