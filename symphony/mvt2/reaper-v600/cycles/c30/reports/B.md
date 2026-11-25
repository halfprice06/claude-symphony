# Cycle 30, critic B: balance and levels (on the c29 render)

**How the levels were measured**
- Frames: K-weighted, ungated, summed over both channels, from 4096-point Hann frames every 50 ms on `cycles/c29/render/`. These are the stem-fixed stems. The master's integrated level measures -24.0 on this scale, against -21.3 LUFS gated.
- Time base: the frames are averaged per qn on the tempo map of `cycles/c29/rendered_build/parts.json`.
- Note bodies: the level from onset + 0.15-0.2 s to 0.05 s before the note's end.
- Band levels: 20-100, 100-250, 250-500, 500-2k and 2-6k Hz, from the same frames.
- Tables: per-onset tables were read in `build/` (unchanged since the c29 render).
- Labels: "measured" means a number from the render, parts.json or a table. "Inferred" means a judgement about what a listener hears.

## Manual notes (B3: May 2021 HO manual pp. 123-126; `loop/MANUAL-GAPS.md` read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.123: **Timpani Felt Long.** Long hits, with left-hand variations at C1-A2 (EW; MIDI 36-57) and right-hand variations at C3-A4. Two notes closer than 65 ms play a double hit that damps the first. Velocity selects up to 16 layers. | The strokes at 172, 203, 209.5, 277, 278.5 and 279 (MIDI 44-51, Lng row, KS C0 = 24). | Yes. No two strokes are closer than 0.5 qn (about 0.55 s), so no stroke turns into a double hit by accident. The right-hand variations are never used. Nothing in v600 needs them: there are no same-pitch stroke runs (MANUAL-GAPS, "checked"). |
| p.123, p.125: **Timpani Felt Cresc.** Live-recorded crescendo rolls ending on a strong stroke, in three key ranges of different lengths, with 2 velocity layers. The manual calls it "the most realism" for a roll crescendo. | The pp < p roll into the 172 stroke (4 qn, bar 52), the pp < f roll into 203 (3 qn, bars 60-61), and the pp < f roll at 261 (1 qn). | No. All three are played on the Rls row with a CC1 ramp, CC7 and the volume envelope (MANUAL-GAPS #7, never tried). The bar 52 roll's own shape is finding 4. |
| p.123, p.125: **Felt Flam.** Soft double hits, 2 layers. | None: v600 prints no flams. | Not applicable. |
| p.124: **Felt Rolls.** CC11 and velocity set overall loudness; CC1 sets the dynamic in 8 layers, for crescendos and decrescendos of any length. | Every roll: ppp at 3 and 226, pp < at 168/200/261, f at 204/262, and the bar 81 decrescendo at 268-271. | Yes for CC1: `TIMP_CC1_MAP` gives 56 at ppp/pp, 60 at p and 88-104 at f/ff, so the rolls cross layers. No for CC11: the Timpani Flt KS patch has no CC11 entry (DIGEST §9.1, patch check; KIT §10), so loudness is CC7 plus the envelope. The bar 81 decrescendo falls 16 dB (268: -33.4, 271: -49.2), and the 200-203 crescendo rises 10 dB into the f stroke. |
| p.124: **Felt Short.** For stops "within a beat or two", "more realistic … than … automation alone". | The printed "damp" at 173 (after the p stroke at 172) and at 210 (after the 209.5 stroke). | Partly. The Lng stroke is cut by its note-off: 172 falls 13.5 dB within 0.5 qn, and 209.5 falls from -32.9 to -57.4 dB by 211. The manual's row is not used, but the damping is audible in the measurements. |
| p.124: **Felt KS.** C0 long, C#0 short, D0 flam, D#0 roll, E0 cresc. | parts.json `ks`: 24 (Lng) and 27 (Rls) only. | Yes. The keyswitches land 0.06-0.5 qn before each change. |
| p.125-126: **Hard-mallet versions.** Brighter, with clear individual hits in rolls. | The score asks for "soft sticks" (Timp text at qn 0). | Yes: the Felt patch is the right one. |

## 1. Bassoon 1's D flat 4 is 5-8 dB louder than its neighbouring notes at every dynamic. It is the loudest stem over the violin theme in bar 76 and level with the tune at the bar 61 climax (measured)

**Where.** Bassoon 1 (stem 09), every D flat 4 (MIDI 61). Note bodies:
- qn 140: p, -42.8
- qn 146: -41.3
- qn 148: -38.6. These are bars 45-47, under Oboe 1's B flat minor head.
- qn 206: ff, -23.3
- qn 255: mp <, -28.6
- qn 258: -28.4
- qn 262: ff, -23.1
- qn 269: -30.4

**Evidence (measured).**
- **Residual scan.** Note body against the median of its ±2 neighbours: 206 +7.5 dB, 255 +5.7, 262 +5.6, 140 +4.7. No other Bassoon 1 pitch is flagged.
- **Neighbours at 206.** F3 at 204 measures -32.3 and F4 at 208 -28.1. The vol_db difference is only about 2 dB, so about 6-8 dB of the excess comes from the sample.
- **Bar 76, qn 255-256.**
  - Bassoon 1 measures -29.6 / -28.3 (0.5 qn means).
  - The violin theme (Violins I, mp <) measures -34.8 / -35.1, so the bassoon is 5-7 dB over it.
  - Bassoon 1 doubles the celli here (-32.7 / -35.3) and stands 3-7 dB over them as well.
- **Bar 61, qn 206.** Bassoon 1 measures -22.3, Violins I -22.4. It is the second-loudest stem of the ff tutti.
- **Bars 45-47.** Bassoon 1 is the loudest accompanying stem (-43.1, -41.1, -37.4).
- **Not in the tables.** `pitch_trims.json` Bassoon 1 trims only 51 (+6) and 55 (+4). KIT §13 lists the bassoon's D flat 3 as hot, not D flat 4.

**Fix.**
- In `build/pitch_trims.json` Bassoon 1, add `"61": -5`. `_all_arts` is already true. Keep the c29 role [262,265.5,2].
- Simulated on the c29 stems:
  - qn 255-256: Bassoon 1 drops to -34.0, under Violins I (-34.7), and the master drops 1.5-1.9 dB there. The bassoon was carrying the bar.
  - qn 206-208: Bassoon 1 drops to -28.4, 6.7 dB under the tune.
  - Bars 45-47: the Oboe 1 margin over the whole accompaniment improves by 0.9-1.3 dB.
  - The master changes by at most -0.5 dB anywhere else. Bars 61-62 stay the loudest bars.
- This is a level-only change, so it can be done with `stem_fix.py`.
- Same method, optional: the bass clarinet's A flat 2 (44) at qn 18, 24 and 39 (bars 7-14) is +9/+9/+5 dB over its neighbours. The c28 fix covered bars 3-6 and 35 only. Horn 1's solo still stays 4.9-5.2 dB over it, so this can wait.

## 2. Bars 61-62 (qn 204-212): the ff tune in Violins I is still not on top in four of eight beats (measured)

**Where.**
- The tune: Violins I (D flat 6 - D flat 6 - F6 - E6/A flat 6, ff molto sostenuto).
- Against it: Violins II, Horn 3, the celli and Trombone 2.

**Evidence (measured, 1-qn means).**

| qn | 204 | 205 | 206 | 207 | 208 | 209 | 210 | 211 |
|---|---|---|---|---|---|---|---|---|
| Violins I | -19.8 | -22.9 | -22.4 | -20.9 | -20.0 | -23.2 | -19.5 | -17.6 |
| loudest other stem | Vc -22.3 | Vc -23.1 | **Vln II -20.4** | Vln II -21.7 | Bn2 -22.1 | **Hn3 -22.3** | Cb -22.3 | Hn3 -20.7 |
| Horn 3 (f, two horns) | -24.9 | -28.1 | -24.5 | -23.4 | -24.7 | -22.3 | -23.1 | -20.7 |
| Horn 1 (ff) | -24.6 | -28.2 | -27.6 | -28.3 | -24.3 | -27.2 | -23.9 | -27.4 |

**Causes (read in the tables).**
- **Violins II.** The role [204,212,2] is a series 1 carry-over. Violins II carry vol_db +4.3 to +6.6 dB here, while the Violins I re-bow fill at 205.949 holds -2.1 to -4.4 dB from 206.06 to 207.86. c29 critic B flagged this fill; the actor did not refit it.
- **Horn 3.**
  - The role [204,212,5] stacks on the unison boost: Horn 4's A flat 4 is dropped into Horn 3 (`UNI_BOOST` +3.01 dB, which is right for two players) and on the A flat 4 pitch trim (+3). That puts vol_db at +10.6 to +13.1 dB on a CC11 of 93-96 (f).
  - So the printed-f pair sits 0 to +6.7 dB over Horn 1's ff (mean +2.5). For balance, two horns at f should sit 1-3 dB under one horn at ff (inferred, Rimsky-Korsakov's resonance table: horn f to ff is a larger step than one player to two).
  - Horn 4's role [204,212,5] does nothing: its notes are dropped into Horn 3.
- **Violins I sags in its held bows.** The tune sags 3.1 dB from 204 to 205 and 3.2 dB from 208 to 209, inside held notes, with the envelope flat. Inferred: sample decay inside the first bow.

**Fix.**
- `build/roles.json`:
  - Violins II [204,212,2] -> [204,212,0].
  - Horn 3 [204,212,5] -> [204,212,1].
  - Delete Horn 4's [204,212,5].
- `build/rebow_fills.json` Violins I "205.949": +2 dB on the hold values, so the hold sits near -0.5..-2.
- `build/score_config.py`: `LEVEL_SHAPES["Violins I"]` += [(204.5,0),(204.9,2),(205.8,2),(205.95,0)] and [(208.5,0),(208.9,2),(209.8,2),(209.95,0)]. These are slow ramps inside held notes, so the hall tail is unaffected (S3).
- Simulated on the c29 stems (all but the Violins I swells, together with finding 1):
  - The tune's margin over the next stem at qn 206, 207, 209 and 211 goes from -2.0 / +0.7 / -1.0 / +3.1 dB to +2.0 / +3.7 / +0.3 / +4.0 dB.
  - The +2 dB swells then lift 205 and 209 to about +2 dB.
  - The master falls 0.2-0.4 dB at bars 61-62, which stay 2.4-3 dB over bars 79-80.

## 3. Bar 55-56, qn 182-183: Horn 1's G flat 4 is the loudest stem, 5.7 dB over the violin theme. Its pitch trim is wrong at mp (measured)

**Where.** Horn 1, G flat 4 (66) at qn 182 (2 qn, legato from the B flat 4 at 178). The score marks it as the counter-melody: "espr.", pp < mp at 182. The violins carry the theme: "sul A, cantabile", p < mp (178) < mf (184).

**Evidence (measured, 0.25-qn means).**
- Horn 1: 181.5 -33.2, 182.0 -30.6, 182.5 -27.7, 182.75 -28.0, 183.25 -34.5.
- Violins I over the same span: -34.4 / -34.9 / -33.4 / -33.7 / -30.6.
- The note body is +5.2 dB over its neighbours (residual scan).
- vol_db steps from +3.8 to +9.1 at 182.0, then to +11.0 at 182.15. The +4 comes from `pitch_trims.json` Horn 1 `"66": 4`.
- KIT §13 records G flat 4 as weak (-5) on soft notes. Here, at CC11 66-69, the note is not weak. This is KIT's "a pitch trim set at soft dynamics can be wrong at ff" case.
- The other G flat 4s are in range: 190 (-37.2, under the violins), 196 f and 208 ff (-24.3, level with Horn 1's F4 at 204).

**Fix.**
- `build/pitch_trims.json` Horn 1: add 182.0 to `_skip_onsets`.
- `build/note_trims.json` Horn 1: add `"182": -2` (joined note: the 0.25 qn ramp-in from KIT §13).
- Simulated: Horn 1 at 182.5 is about -33.7, level with to 0.3 dB under Violins I. It stays on top of the accompaniment. Inferred: still heard as the "espr." counter-line.

## 4. Timpani rolls: the ppp roll of bars 2-3 never settles under the pp strings, and the bar 52 crescendo roll falls in its last beat (measured)

**(a) Bars 2-3, qn 3-8.55.**
- The score: Timpani A flat 2 ppp roll, decrescendo 6-8. The strings are pp in Vln II/Vla/Vc/Cb, ppp in Vln I, all decrescendo 6-9.
- 0.5-qn means, timpani against the quietest string section:
  - 3.25: -47.0 against Cb -47.9
  - 4.25: -46.4 against Cb -48.1
  - 5.25: -46.3 against Vc -44.0 / Cb -43.3
  - 6.75: -46.7 against Cb -53.6, Vc -49.3
  - 7.75: -47.5. Every string section is quieter: Vln I -48.5, Vln II -50.6, Vla -50.3, Vc -50.7, Cb -52.6.
  - 8.25: -50.8
- KIT §13 puts a pp/ppp roll 3-5 dB under the quietest sustained string section. The roll is instead 1-2 dB over the basses for its first 3 qn, and over every string section by bar 3.
- Rule 5 (settle under the texture) also fails:
  - vol_db falls from +15.6 to +10.6 over 3-6.
  - The stem rises from -47.3 to -46.5 over the same 3 qn (the sample grows).
  - The printed decrescendo falls 2.8 dB (6-8.5), while the strings fall 4-6 dB.
- The roll supplies about a third of the master's 100-250 Hz band here: -46.7 against the master's -41.8.

**(b) Bar 52, qn 168-172.**
- The score: pp < roll into the p stroke at 172.
- 0.25-qn means: 170.5 -42.6, 171.0 -45.8, 171.25 -47.6, 171.5 -45.1, 171.75 -43.6, stroke 172 -42.1 (99th-percentile peak -39.7).
- The roll falls 5 dB in its last beat. That is a reversed crescendo, against brief item 6.
- Cause:
  - c29's cap `LEVEL_SHAPES["Timpani"]` [(170.5,0),(171.6,-4),...] ramps down across the whole last beat.
  - The raw roll also sags about 2.3 dB from 170.5 to 171.25. That is the measured level with the cap's own dB taken out.
  - The stroke ends only 2.4 dB over the roll's peak.

**Fix (`build/score_config.py`, `LEVEL_SHAPES["Timpani"]`).**
- (a) Add [(3.0,0),(4.5,-3),(6.0,-3),(8.4,-6),(9.2,-6),(9.5,0)]. These are slow ramps under a sounding roll; the roll has ended by 8.55, so the hall tail is unaffected. CC7 is unchanged.
  - Simulated: the roll sits 1 dB under the basses and 3-5 dB under the other sections in bar 2. At 7.75 it falls to about -53, under every string section.
  - It is still about 13 dB under the master, well above the c25 overshoot (14-23 dB under the orchestra).
- (b) Replace the cap [(170.5,0),(171.6,-4),(171.94,-4),(171.95,0)] with [(168.0,0),(168.5,-2.5),(170.75,-2.5),(171.5,-0.5),(171.94,-0.5),(171.95,0)]. That is a flat cut that opens over the last beat, against the sample's sag. Then raise the 172 stroke shape (`LEVEL_SHAPES_S`) from +4 to +6.
  - Inferred result: the roll rises steadily to about -44, and the stroke peaks about 5 dB over it.
  - The manual's alternative is the Felt Cresc row (E0, p.123/125; MANUAL-GAPS #7). A recorded 4-beat crescendo ending on the stroke would replace both the CC1 ramp and these shapes. Read the take lengths from the `.ews` headers first.

## 5. Horns (and the low brass) have one tone colour from pp to f, because CC1 never leaves the middle layers. A printed p horn is a quieter mf (measured; MANUAL-GAPS #1, deferred three times)

**Evidence (measured).**
- The measure: the high-band tilt (2-6 kHz minus 500-2000 Hz, median per note body) by printed dynamic, with the median CC1 at those notes.

  | Track | pp | p | mp | mf | f | ff |
  |---|---|---|---|---|---|---|
  | Horn 1 tilt (dB) | -26.1 | -25.9 | -25.4 | -24.0 | -26.7 | -13.7 |
  | Horn 1 CC1 | 63 | 64 | 67 | 72 | 77 | 86 |
  | Bass trombone tilt (dB) | -24.5 | -26.1 | | | -16.0 | |

- Horn 1's tilt stays within 2.7 dB from pp to f, and jumps only at ff.
- For comparison, Violins I, whose CC11 crossfades the layers, spans about 13 dB between pp and p alone.
- The Hollywood Brass KS Masters crossfade their dynamic layers on CC1, not CC11 (p.101; DIGEST; M1 c09 read the patch). `CC1_DYN_TRACKS` is empty in this config, so every brass note gets CC1 53-87 from the vibrato rule.
- Consequence for this lens:
  - Horn 1's p solos (bars 7-14, 67-70), its pp counter-melody (finding 3) and the p/pp chords of Horns 3-4 get their dynamic from volume only.
  - Horn 1's pp/p/mp body levels measure -42.7 / -39.2 / -35.1: the printed order holds in volume, but not in colour.
  - Inferred: the soft horn passages sound like a distant mf rather than a soft horn.

**Fix.**
- `build/score_config.py`: `CC1_DYN_TRACKS = ("Horn", "Trombone", "Bass trombone", "Tuba")`. "Horn" also matches "Horns 1-2 a2". Leave the clarinets for a later cycle, so that one family changes at a time.
- Keep `CC1_DYN_MAP` generic.
- Expect to refit:
  - the horn pitch trims (`"65"` early/body, `"66"`, `"68"`; finding 3);
  - Horn 1's roles;
  - Trombone 1's per-onset accent shapes. Movement I c09 needed two cycles to settle.
- Pass check: Horn 1's tilt spreads at least 6 dB between p and f, and the pp/p notes get darker. Re-measure the solo margins listed under "Checks asked for in this lens" below; Horn 1 must still sit 2-5 dB over the bars 7-14 accompaniment.
- If the actor defers this again, record the tilt table above as the baseline.

## 6. Soft trims set pp at or above p on the violas and Bassoon 2, so pp and p sound alike on those tracks (measured levels; audibility inferred, small)

**Evidence (measured).**
- Median note-body level by printed dynamic:

  | Track | pp | p | gap |
  |---|---|---|---|
  | Violas | -46.3 (66 notes) | -44.6 (17) | 1.7 dB |
  | Bassoon 2 | -46.8 (25) | -44.6 (5) | 2.2 dB |
  | Double basses | -48.3 (40) | -47.4 (38) | 0.9 dB |
  | Violins II | | | 5.7 dB |
  | Violoncellos | | | 5.3 dB |
  | Violins I | | | 8.4 dB |
  | Bassoon 1 | | | 5.6 dB |

- `build/mix.json` `soft_trim_db`:
  - Violas and Violas div: pp +5, p +3.5.
  - Bassoon 2: pp +8, p +6.5.
  - Double basses: pp +6, p +6.5.
- So on the violas and Bassoon 2 the trim adds 1.5 dB more at pp than at p, which takes back part of the CC11 step.
- The delivery master's slow lift (ride up to +10 dB) already raises the soft passages for headphones, so the mix does not need to flatten pp into p as well.

**Fix.**
- `build/mix.json` `soft_trim_db`: Violas and Violas div pp 5 -> 3.5; Bassoon 2 pp 8 -> 6.5. Leave the Double basses: their pp 4-soli pedals were refitted in c29.
- This is level-only, so it can be done by stem fix.
- Check:
  - the violas' pp entries in bars 15-22 and 41-44 against the oboe and cor anglais (they must not disappear: target 6-9 dB under the solo);
  - the delivered LRA and span.

## Checks asked for in this lens

- **Solos over their accompaniment** (margin over the whole accompaniment, then over the loudest single stem). All measured, all hold:

  | Solo | Bars | Over whole accompaniment | Over loudest stem |
  |---|---|---|---|
  | Horn 1 | 7-14 | +1.7 to +4.9 dB (one dip at qn 24, between phrases) | 5-11 dB |
  | Oboe 1 / solo violin | 15-22 | +1.0 to +8.0 dB | 4-12 dB |
  | Bass clarinet | 31-36 | +1.6 to +7.2 dB | |
  | Flute 1 | 37-40 | +2.5 to +5.6 dB | |
  | Cor anglais | 41-44 | +0.8 to +4.8 dB; Flute 1 is its co-line | |
  | Cor anglais | 47-50 | +0.3 to +8.1 dB | 4-11 dB |
  | Clarinet 1 | coda | +3.6 to +9.2 dB at 280-285, +0.7 to +1.9 at 286-292 | 6-8 dB |

  Oboe 1 in bars 45-47 sits -0.3 to +0.6 dB against the whole accompaniment and 4.6-5.5 dB over its loudest stem; finding 1 lifts it.
- **Low brass at bars 61-64 (measured).**
  - Trombone 2, bass trombone and tuba (f) measure -22.6 to -25.5 against Violins I at -19.5 to -23.2.
  - By band: Violins I owns 2-6 kHz, where the low brass sum is 13-14 dB under it. In 500-2000 Hz the low brass sum is about 4 dB over Violins I.
  - Rimsky-Korsakov's resonance ratios (a trombone at f about 3 dB over a string section) would allow more.
  - Not covering. Keep as is.
- **Timpani at bars 61-64 and 79-82 (measured).**
  - Bars 61-64: the f roll measures -30.3 to -37.1, 8-17 dB under every string section. The f stroke at 203 is -26.0.
  - Bars 79-82: the roll is -28.6 to -33.4 against the master at -13 to -16. There are no low brass in these bars.
  - The bar 81 decrescendo falls 16 dB.
  - Not covering.
- **Bass (measured).**
  - Over the whole movement, the master's 20-100 Hz share is -19.7 dB, between the Dvořák (-21.7) and Brahms (-8.5/-7.9) references.
  - The most bass-heavy bars are 83-84 (-9.6/-9.0, the coda's ppp pedal with the timpani strokes) and 31/35 (-9.7, the contrabassoon pedal). These are low-level passages, comparable with the Brahms average share.
  - At the climaxes the 20-100 Hz share is -12 to -20 dB.
  - Solid, not boomy. No change.
- **Divisi and soli tracks against their sections (measured).**
  - Violas div is within ±2 dB of the Violas in bars 23-28, 80-81 and 84-92. The exceptions are bars 29-30 (+8.8 dB, -48.1 against -56.9) and 283-286 (+5.2), both short and quiet.
  - Violins II div is 3.5-7 dB under the Violins II in bars 37-40 (the c29 shelf).
  - Violoncellos div is level with the celli.
  - The Cb 4 soli are 4-8 dB over the ppp roll in bars 67-70, and the Vc 4 soli are over the Cb from 277.
- **S3 (measured).** No volume-envelope fall of 3 dB or more within 0.2 s under a sounding note away from an onset, apart from the end points of early fills. Every fix above is a slow ramp, a hold value, a pitch or note trim on an onset, or a role change.

**Do not touch:**
- The solo margins listed above, including Horn 1 in bars 7-14, the solo violin and Oboe 1 in bars 15-22, and Clarinet 1's coda.
- Trombone 1's quotation level, and the low brass and timpani levels at both climaxes.
- The bars 67-70 pedal-over-roll balance and the roll's decrescendo (c29).
- The bar 81 roll decrescendo.
- The coda timpani strokes. They are 4-7 dB over the ppp pedal as the E flat-C-A flat answer, and ring out 14 dB under Clarinet 1's entry.
- The climax order (bars 61-62 louder than 79-80).
- The Cb EQ set and climax loud_eq.
- The Violas Detache level on CC7.
- The c29 Clarinet 1 / Flute 2 / Bassoon 2 / Oboe 1 climax roles.
