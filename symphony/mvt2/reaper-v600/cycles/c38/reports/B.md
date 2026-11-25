# Cycle 38, critic B: balance and levels (on the c37 render)

**Method.**
- Stems and master from `cycles/c37/render/` (after the c37 Flute 1 stem fix). Note data from `cycles/c37/rendered_build/parts.json`.
- **Level scale.** Approximately K-weighted (4th-order 38 Hz high-pass plus a +4 dB shelf above 1.5 kHz), 4096-point Hann spectra, 25 ms hop, both channels summed, ungated. Plain bands 20-100, 100-300, 300-2000 and 2000-5000 Hz come from the same frames. The absolute offset differs from c37 B's scale, so only differences between numbers are meaningful. Cross-check: Violins I over 204.1-211.9 reads -8.7 dB against the master here, and c37 B's simulation predicted -8.6.
- **Note bodies.** From the score onset + 0.15 s to 0.05 s before the played end. Time base: score qn on the parts.json tempo map.
- **Simulations.** dB gains applied to the stem frames, with the master re-summed. They ignore hall smear, so treat them as accurate to about 1 dB.
- **Labels.** "Measured" means a number from the render, parts.json or a table. "Inferred" means a judgement about what a listener hears, or a reading of a book or manual.

## Manual notes (B5: May 2021 HO manual pp. 114-115, 154-155, 158-159; `loop/MANUAL-GAPS.md` read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| pp.114-115 **Orchestral Perc Basics Kits 1/2**: CC11 and velocity set loudness; velocity selects the dynamic (up to 16 levels in Kit 1, 12 in Kit 2); Kit 1 maps Timpani Felt Long to C0-E1 with alternating hands. | Timpani: strokes at 172 (p), 203/208/209.5 (f), 277/278.5/279 (pp, coda). | Not applicable as written: the track uses `Timpani Flt KS.oib` with CC1 layers (c28), not a kit. Velocity against printed dynamic is consistent (measured stroke peaks): pp 56-60 → -38.6..-41.0, p 72 → -33.5, f 96 → -15.5. That is about 5-7 dB per printed step, near the 4.8 dB/step of the other families. Rolls follow Dan's rule (finding list below). |
| p.154 **Humanizer**: random note-on/off delay 0-100 ms, velocity up to 50 %, tuning, volume and pan. | All tracks. | Correctly not used. The 1FH KS Master's filter list (read with `opus_state.load_oib`) has no Humanizer. c37's unchanged tracks were sample-exact against c36, which also rules out any random variation. The per-onset tables need that determinism. |
| pp.154-155 **MIDI Compressor**: threshold/ratio/makeup on velocity or a CC; notes under the threshold are not played. | CC11/CC1 dynamics on every track. | Correctly not used. It would compress the printed dynamics, which `deliver_master.py` already handles after the mix. No patch read has it as a filter. Every note in parts.json sounds on its stem. |
| p.158 **Automation window**: automatable parameters and macros. | Opus mixer, mics, reverb. | Not used. Opus parameters are fixed per track in the generated state (`jobs/*.b64`). Time-varying level is done in MIDI (CC1/CC11/CC7, pre-hall) and in REAPER's volume envelope (post-hall). That keeps every level change in `parts.json`/`mix.json`. This matches the BRIEF rule that everything is rebuilt from files. |
| p.159 **MIDI Controller Mapping**: remap a patch's CCs; "avoid conflicting MIDI CC messages". | The CCs the pipeline sends (measured in parts.json): CC1 on 30 tracks, CC11 on 31, CC15 on 11 (strings and Horns 3/4), CC7 on 8, CC70 on the four string sections, CC36 on none (pre-roll reset only), plus CC69 in the pre-roll. | Followed for the CCs used for balance. CC15 on Horns 3/4 drives the 1FH patch's ConSordino filter: the filter is present in the .oib, so it is a real mapping, not a stray CC. CC7 acts as linear pre-hall gain (series 2 LEARNINGS c29), which findings 2-4 below rely on. The one known mismatch is MANUAL-GAPS #10 (round-robin reset on CC36 instead of Opus's CC16). It is not a balance issue and is not re-tested here. |

## 1. Bar 81 (qn 268-271): the cadence roles end where the printed decrescendo starts, so the whole orchestra gets a +1.5 to +3 dB envelope lift into the diminuendo, and the inner voices pass the melody (measured)

**Where.**
- All parts decrescendo from ff at 268 to p at 271.
- The melody descends in octaves: Violins I, Violins II, Flute 1, Oboe 1 and Clarinet 1 (268 A flat, then eighths 269-270.5).
- The violas (G4 at 268, then E flat 4) and the celli (D flat 4 tenuto at 269) are inner and bass voices.

**Evidence (measured).**
- **Roles and shapes ending at 268.**
  - `LEVEL_SHAPES["_all"]` (score_config.py l.660) is -1.5 until 267.75 and back to 0 at 268.25.
  - `roles.json` [262, 268, -1.5] on Violins I/II, violas, celli and basses also ends at 268.
  - So at 268 every track rises 1.5 dB and every string track 3 dB.
- **vol_db, 268 → 269.**
  - Violas -4.8 → 0.0.
  - Violins I -3.2 → 0.0.
  - Celli -2.2 → +2.4 (the +2.4 at 269 is `early_fills.json` Violoncellos "269" {3.4, pre 0.04, hold 0.1}).
- **Master (0.5 qn).** 266.5 -16.2, 267.0 -16.6, 267.5 -17.3, **268.0 -16.6**, 268.5 -18.2, 269.0 -20.7. The diminuendo starts with a 0.7 dB rise, a reversed diminuendo in Dan's sense (BRIEF rule 6).
- **Inner voices against Violins I (melody).**
  - Violas 268.0 -25.4 against -26.2; 268.5 -25.9 against -28.9 (+3.0 dB).
  - Celli 269.0 -27.2 against -33.1 (+5.9 dB). The cello 269 note blooms 10 dB over its own median, the largest in-note swell on any string note outside the bar 63 sf.
  - The cor anglais E flat 4 at 269 (-31.5) also sits over Violins I.

**Why it matters (inferred).** The listener hears the end of the second climax swell again on the first beat of the diminuendo. Then a viola note and a cello tenuto stand out of the texture while the melody's falling eighths, the line that leads into the full close of bar 82, drop under them.

**Fix.**
- `build/score_config.py`, keep the melody tracks as they are. For every other track sounding in bar 81, add a shape that mirrors the `_all` ramp so their level stays at -1.5 through the diminuendo:
  - tracks: Flute 2, Oboe 2, Cor anglais, Clarinet 2, Bass clarinet, Bassoon 1, Bassoon 2, Contrabassoon, Horn 3, Horn 4, Horns 1-2 a2, Timpani, Violas, Violoncellos, Double basses;
  - shape: `LEVEL_SHAPES[t] = LEVEL_SHAPES.get(t, []) + [[(267.75, 0.0), (268.25, -1.5), (270.75, -1.5), (271.0, 0.0)]]`.
  - The rise back to 0 lands on the p chord at 271, a new onset in every part, so no tail is cut (S3).
- `build/roles.json`: Violas, Violoncellos and Double basses `[262, 268, -1.5]` → `[262, 270.9, -1.5]`.
- `build/early_fills.json` Violoncellos "269": db 3.4 → 1.0, keeping pre 0.04 and hold 0.1.
- **Simulated.**
  - Master 266.5-269.0: -16.2, -16.6, -17.3, **-17.6**, -19.5, -22.3. The fall is now monotone.
  - Violas at 268.5 -28.9, level with Violins I (was +3.0).
  - Celli at 269.0 -30.9, +2.2 over Violins I (was +5.9).
  - Bars 79-80 are unchanged, so the climax order holds. The limiter peak is in bar 61, so the limiter is unchanged.
- **Check after the render.**
  - No 0.5 qn master frame from 267.5 to 271 louder than the one before it.
  - Violas and celli no more than 2 dB over Violins I from 268 to 270.5.

## 2. Bar 56 (qn 184-188): the celli swell 5 dB inside their half notes, and Horn 1's D flat 4 is a hot pitch; together they cover the mf violin theme and make a +3.7 dB master bump (measured)

**Where.**
- Violins I/II: the theme, mf at 184.
- Celli: a half-note bass line at mf (A2 at 184, B flat 2 at 186).
- Horn 1: the counter-melody, printed mp (C4 at 184, D flat 4 at 186).

**Evidence (measured, 0.25 qn).**
- **Celli in-note swell.**
  - 184.0 -35.0, 184.5 -27.7, **184.75 -25.2**, 185.25 -34.9; 186.0 -35.5, **186.75 -29.4**, 187.0 -35.3.
  - Each half note peaks 4.6-4.9 dB over its own median at +0.75 qn. At 184.75 that is 5.5 dB over Violins I (-30.7).
  - The controllers explain about 1 dB: CC11 arcs 71 → 76 → 71 on every half note and vol_db +0.4..+1.0. The rest is the sample, probably a layer crossfade near the edge of a dynamic layer; MANUAL-READING D1 notes "swells near a layer edge jump 8-11 dB" (inferred).
- **Horn 1 at 186.**
  - D flat 4 body -31.9 against Violins I -31.7 (-0.2 dB) and Violins I+II -2.8 dB. The neighbouring counter-melody notes sit 4.8-7.5 dB under Violins I (182: -4.9, 184: -6.4, 188: -7.5).
  - At the same CC11 (67), the D flat 4 is 4.4 dB over the C4 at 184; the C4 is itself trimmed -2, so the D flat 4 is about 2.4 dB over the untrimmed C4. `pitch_trims.json` Horn 1 has no entry for 61.
  - The same pitch is hot on Horn 3 (same 1FH KS Master) in bar 5: D flat 4 at 12 has body -42.9 against its C4 at 6 and 15 (-46.9/-46.2) at CC11 35. At 12.0 Horn 3 is 1.5 dB under the whole master.
  - In the bars 7-14 solo the D flat 4 sits within 2 dB of its neighbours (23.0: -38.7 against -40.1/-40.4; 37.5: -38.7).
- **Master.** The bump scan (0.1 s master against its ±1.2 s median) ranks 186.79 at +3.7 dB, contributed by the celli (+5.9) and Horn 1 (+4.8). The melody scan flags 184.5 (celli +3.8 over Violins I) and 186.0 (Horn 1 +2.3).

**Why it matters (inferred).** The bass line and the mp counter-melody push forward on beats 2 and 4 of the bar in which the violins reach mf. The theme sounds as if it stepped back, and the counter-melody's D flat sounds accented.

**Fix.**
- `build/score_config.py`: `CC7_POINTS["Violoncellos"] = CC7_POINTS["Violoncellos"] + [(184.35, 127), (184.55, 71), (185.0, 71), (185.2, 127), (186.35, 127), (186.55, 71), (187.0, 71), (187.2, 127)]`.
  - 71 is -5 dB, applied pre-hall. Keep the c31 bar-63 lane that is already in the list.
- `build/pitch_trims.json`:
  - "Horn 1": add `"61": -2.5`, and add 23.0 and 37.5 to its `_skip_onsets` (keep 32, 182, 210).
  - "Horn 3": add `"61": -2.5`.
- **Simulated.**
  - Celli at 184.75 -30.2 (under Violins I) and at 186.75 -34.4.
  - Horn 1 at 186.0-186.75 -34.0..-31.9, 2.7 dB under Violins I and 5.3 under the two sections together.
  - Master at 186.75 -24.3 → about -25.9, at 184.75 -23.2 → about -25.5.
  - Horn 3 at 12.0 -41.7, still 1.2 dB over its C4 (the neighbour note keeps a slight lean).
- **Check.** Horn 1 at 230 (D flat 4, mp) goes -33.9 → -36.4, between its 229 (-33.7) and 231 (-39.1) neighbours.

## 3. Coda (bars 85-89): Clarinet 1's pp dolce solo has two 4-5 dB bumps, and the second lands on the violins' pp entry on the same C5 (measured)

**Where.** Clarinet 1, the motto tail:
- 280 E flat 5 (pp cresc. at the start);
- 283 D5 (slurred; moved onset 282.974);
- 286 D flat 5, then 289 D flat 5;
- 292 C5, held into the morendo.

Violins I enter at 292 on C5, pp, con sord. (the pitch movement I ended on).

**Evidence (measured, 0.25 qn).**
- **283.** 282.5 -40.8, **282.75 -36.9**, 283.0 -38.0, 283.25 -42.8, 283.5 -43.3. That is 4-6 dB over both sides, on the legato transition into the D5 plus the 283 early fill (+1 dB, hold 0.35 s). Master bump +4.7 dB at 282.97, ranked third in the movement.
- **292.** 291.75 -41.3, **292.0 -36.0**, 292.25 -36.7, 292.5 -40.8. That is 4.8-5.3 dB over both sides.
  - vol_db rises 7.4 → 9.0 over 291.5-291.9: the c35 role [279.9, 291.9, -2, 0.5] ends with its ramp back to 0.
  - Then the 292 note trim (-4) ramps in only from the moved onset, reaching +1.0 at 292.47.
  - Master bump +4.4 dB at 292.11 (fifth in the movement). At 292.0 the clarinet is 12 dB over the entering Violins I (-48.3).

**Why it matters (inferred).** A pp dolce line gets two pushed notes. The second covers the moment the violins take over the C5, which is the movement's link back to movement I. It should sound like a handover, not a swell.

**Fix (pre-hall, so no tail is cut).** `build/score_config.py`:
`CC7_POINTS["Clarinet 1"] = CC7_POINTS["Clarinet 1"] + [(282.6, 127), (282.75, 85), (283.1, 85), (283.3, 127), (291.4, 127), (291.9, 85), (292.1, 80), (292.35, 95), (292.5, 127)]`
- 85/80/95 are -3.5/-4.0/-2.5 dB. Keep the c37 lane at 205-209.9.
- **Simulated.** 282.75-283.0 -40.4/-41.0 (body -41..-43); 292.0-292.25 -39.6/-38.8 (body -40.8). Master bumps about +2 dB at both places.
- Leave the c35 coda balance against the cor anglais as it is (clarinet median +4.6 dB over the loudest other stem; the cor anglais' own pp dolce line within 2 dB at 286/289).

## 4. Bar 80 (qn 266-268): the cor anglais' inner A flat 4 is the loudest wind and louder than the melody, even after its -3 dB trim (measured)

**Where.**
- Cor anglais A flat 4 at 266 (ff, inner voice of the wind chord).
- The melody at 266 is Violins I (G flat 6), Flute 1, Oboe 1 and Clarinet 1.

**Evidence (measured, 0.5 qn).**
- Cor anglais 266.0 -25.9, 266.5 **-24.1**, 267.0 -26.5, against:
  - Violins I -27.7/-27.4/-28.9;
  - Oboe 1 -27.1/-27.8/-28.8;
  - Flute 1 -26.3/-29.2/-34.6.
- The cor anglais' own 262 note (B flat 4, same ff) measures -29.8..-31.8, so the A flat 4 is 5-6 dB hotter than the note before it. `note_trims.json` "266": -3 is already applied.
- Over 266-268 its 2-5 kHz band sits 14.7 dB under the master's band level. Flute 1 is at 24.5 dB under and Clarinet 1 at 16.3. Only Oboe 1 (12.3) and the violins (5.0-5.2) are brighter.
- The melody scan flags 266.5 (+3.3 over Violins I) and 267.0 (+2.4).

**Why it matters (inferred).** In the ff cadential bar a reed colour from the middle of the chord comes out over the tune, which the strings and upper winds carry in octaves.

**Fix (pre-hall).** `build/score_config.py`: `CC7_POINTS["Cor anglais"] = [(265.95, 127), (266.05, 90), (267.9, 90), (268.0, 127)]` (-3 dB, on top of the -3 note trim).
- Simulated: cor anglais -28.9/-27.1/-29.5, at or under the melody instruments. Master under -0.4 dB.

## 5. Bars 29-30 (qn 87-90): the violas' main half drops 7 dB at its re-bow and sits 6-10 dB under the divisi half in the final A flat chord of section A (measured)

**Where.** The full close of section A, p decrescendo to pp. In the chord:
- the violas' main half holds E flat 4 (re-bowed at 86.861 onto Sus MAX by AUTO_REBOW; `rebow_fills.json` Violas "86.861");
- the divisi half holds A flat 4;
- Violins I/II A flat 4, celli C4, basses A flat 1.

**Evidence (measured, 0.25-0.5 qn).**
- **Main violas.** 86.75 -48.8, then **87.0 -55.7** at the re-bow piece, then -55..-57 to 89.0 and -57..-60 to 90.
- **Over the same frames.** Violas div -45.1..-51.4; Violins I -44.2..-51.4; celli -45.9..-56.3. The div half does not step at 87 (-45.9 → -46.9).
- vol_db: main half -2.0 at 87.0 → -8.1 at 87.07 → -12.2 by 89.0. Div half -0.9 → -5.5 over the same span. Both halves share the roles [87, 90, -3] and [80, 87, 0.5], so the extra 5-7 dB on the main half comes from the re-bow piece's own level (its fill tail is -3.7).
- Median over bars 29-30: div minus main is +7..+9 dB per qn (88-90).

**Why it matters (inferred).** In the cadence chord, the only string E flat (the fifth) drops out at the re-bow, a 7 dB step that a listener hears as a section stopping. The chord thins to roots and thirds, with Horn 4's pp E flat 3 an octave lower.

**Fix (rises only).** `build/score_config.py`:
`LEVEL_SHAPES["Violas"] = LEVEL_SHAPES["Violas"] + [[(86.95, 0.0), (87.1, 6.0), (89.0, 6.0), (90.0, 2.0), (90.3, 0.0)]]`
- The 89-90 fall stays inside the printed decrescendo to pp. Only 2 dB falls after the release, and the next viola note is at 108.
- Simulated (constant +6): main half -48.6..-51.8, 0-4 dB under the div half, no step at 87. Master +0.1 dB.
- Alternative with the same result: raise the "86.861" fill points from 0.2 s on by +6 dB and move its last point (3.86, 0.0) to (4.4, 0.0).

## Checks asked for in this lens (measured unless marked)

**Solos over their accompaniment (note bodies, median / minimum).**

| Solo | Over accompaniment sum | Over loudest stem |
|---|---|---|
| Horn 1, bars 7-14 | +1.8 / -1.4 | +4.9 / +2.9 |
| Oboe 1, bars 15-16 | +4.5 / +0.4 | +5.9 / +4.4 |
| Solo violin, bars 17-18 | +4.4 / -1.5 | +8.0 / +2.8 |
| Oboe 1, bars 19-20 | +4.1 / -2.4 | +6.3 / +1.3 |
| Solo violin, bars 21-22 | +2.2 / -3.3 | +5.9 / +0.5 |
| Bass clarinet, bars 31-36 | +2.6 / -0.9 | +4.5 / +1.2 |
| Flute 1, bars 37-40 | +3.6 / +2.3 | +8.4 / +5.4 |
| Cor anglais, bars 41-44 | +4.2 / +2.8 | +7.8 / +4.3 |
| Flute 1 counter-line, bars 41-44 (cor anglais excluded) | +0.4 / -3.4 | +3.5 / -0.4 |
| Oboe 1, bars 45-47 | +1.4 / -4.8 | +6.6 / +0.3 |
| Cor anglais, bars 47-50 | +3.9 / +1.4 | +7.0 / +4.2 |
| Horn 1, bars 65-70 | +8.3 / -2.3 | +9.3 / +2.6 |
| Clarinet 1, coda | +0.7 / -2.7 | +4.6 / +1.9 |

- All solos lead their accompaniment.
- The minima are single notes under a cello entry (solo violin at 60, oboe at 54) or inside the solo's own phrase (oboe at 145). No action.
- Flute 1's bar 42 note rose with c37's role: 129 is now +0.8 over the loudest stem.

**Climaxes and Dan's timpani and low-brass rule.**
- **Bars 61-62 (family sum against master).**
  - Strings -3.9/-4.2, woodwinds -7.4/-6.8, horns -8.1/-6.7, low brass -6.5/-7.4, timpani -19.2/-25.5.
  - The timpani roll ranks 21-22 of 22 after its 203 stroke. No brass part is louder than Violins I (-8.7). c37 B #3 landed: Horn 1 -11.5, Trombone 2 -10.2.
- **Bars 63-64.** Trombone 1 leads (ff against strings sf>p, then p).
- **Bars 79-81.**
  - Timpani rank 14-20, -16..-19 under the master, falling with its decrescendo. No trombones.
  - Woodwinds -3.4/-3.9 and strings -4.2/-4.0 against the master. Rimsky's forte ratio (one section is worth two winds; 11 winds against 5 sections) predicts about this (inferred).
- **Climax order (metrics.md).** Bars 61/62 -13.8/-14.3 against 79/80 -19.4/-20.0.
- **Long rolls.** The ppp roll of bars 67-70 is -14..-21 under the master, under Horn 1's solo.

**Dynamic mapping (median note bodies of 0.9 qn or more, by printed dynamic).**
- pp is consistent across families: winds -41.9..-47.2, Horns 3/4 -47.6/-46.3, strings -44.9..-46.6, harp -45.8.
- p and mp steps are 3-6 dB in every family. The visible inversions are context, not mapping:
  - Clarinet 1's pp is its coda solo;
  - the violas' mf is bar 28 after c37's 83 cut;
  - Oboe 1's f bucket is the bar 59-60 crescendo start;
  - the harp's p is the c04 cut under the bars 37-44 solos.
- The basses read 6-8 dB under the celli at p on this K scale; c36 and c37 B judged this right for their 40-100 Hz fundamentals.
- No soft trim or CC11 map produces a family-order error. Every error found this cycle is local: role ends, fills, in-note sample swells and hot pitches.

**Half-section and 4 soli tracks.**
- Violins II div minus the Violins II half: -1.3 dB median (108-120).
- Violas div minus main: +1.5 (bars 23-28), +0.2 (coda 279-304). Bars 29-30 are finding 5.
- Celli 4 soli (div track) minus tutti basses, 274-286: +1.2.
- Basses 4 soli against tutti celli, 286-304: -5.7.
- The solo violin over Violins I is as in c37. No other change.

**Bass.** In the arco sections the basses carry most of 20-100 Hz: their band level is 0.1-1.7 dB under the master's (68-98 %), and 5.7 dB under in bars 1-6. 100-300 Hz share by section: -4.5 (bars 1-6) to -8.4 dB (bars 79-80); the loud sections run -7.1 to -8.4. No boom, and no section where the bass drops out. No change (inferred against c36/c37 B).

**Standing checks inside this lens.**
- S3: every fix above is either pre-hall CC7 or a rise in the volume envelope, except finding 5's last 2 dB after the release.
- Items 8-9, S1 and S2 are outside balance and were not re-measured.

**Do not touch:**
- c37's Clarinet 1 CC7 at 205-209.9 (now flat, -24.7..-28.1);
- the bars 61-62 brass +3 and strings 2/2.5;
- Horn 1's bar 61 front shape;
- the timpani bar 61-62 roll (+5) and the bar 79-82 roll decrescendo;
- Trombone 1's quotation levels, shapes and CC7 lanes;
- the violas' 83 CC7 dip and the Violins II 82 fill removal;
- the Vc 246 fill as lowered in c37 (peak now 3 dB over Violins I);
- Flute 1's roles at bars 42-44;
- the coda clarinet/cor anglais balance and the celli 4 soli on the div track;
- the final chord's balance (Violins I on top, -53..-56);
- the Cb and timpani side shelves and the soft-horn loud_eq;
- harp env_sustain 1.0;
- the solo levels in the table above.
