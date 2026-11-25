# Cycle 42, critic B: balance and levels (on the c41 render)

**Method.** I analysed every stem and the master of `cycles/c41/render/` (the final stems, after both stem fixes) and of `cycles/c40/render/` for comparison. Both renders use the same tempo map from `build/parts.json`. Frames were 4096 points with a 1024 hop on the mid (L+R)/2 signal. Each frame was weighted three ways: approximately K (38 Hz high-pass plus a +4 dB shelf above 1.5 kHz), A, and octave bands, plus a 2-5 kHz band. Levels carry an arbitrary offset, so only differences are meaningful. I measured stereo seat and width from L and R directly, above 150 Hz.

Other sources:
- Printed marks: `build/mockup-events.tsv`.
- Note, CC and volume data: `build/parts.json` and `build/roles.json`.
- Timpani layer tables: read from `Timpani Flt KS.oib` with `mockup-kit/opus/opus_state.py`.

Simulations scale stem powers and re-sum. They ignore the hall, so trust them to about 1 dB. "Measured" means a number from the render or the data. "Inferred" means a judgement about what a listener hears.

## Manual notes (B3: May 2021 HO manual pp. 123-126; `loop/MANUAL-GAPS.md` read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.124 (Felt Rolls; KS row D#0): CC1 "controls dynamics (8 levels)", for crescendos and decrescendos. | Every roll (Rls row, key 27): ppp bars 2-3, 67-70; crescendo rolls 168, 200, 261; f rolls 204-209, 262-271. | **Followed.** `TIMP_CC1_MAP`: ppp/pp 56, p 60, f 88, ff 104. The .oib tables put the layer peaks at V1 0, V2 23, V3 39, V4 55, V5 71, V6 87, V7 103, V8 119. So pp rolls play V4 at full, f rolls V6 and ff V7. The `score_config.py` comment ("V1 at CC1 0-9 ... V8 at 118-127") describes the tables wrongly but changes nothing. Measured: the 1-8 kHz share of the ppp rolls is -21..-24 dB against -16 for the f rolls, so the soft rolls sound darker. |
| p.123-125 (Felt Cresc; KS E0): live-recorded crescendos in three lengths, two velocity layers; "the most realism" for a crescendo roll. | Crescendo rolls 168-172 (pp < into a p stroke), 200-203 (pp < f), 261-262. | **Not used** (MANUAL-GAPS #7, untried). The Rls crescendos grow 11 dB (168 to 171.5), 11 dB (200 to 202.5) and 17 dB (261 to 262) in K (measured), so the dynamic shape is right. The gain from Felt Cresc would be realism, not balance. |
| p.123-124 (Felt Long, KS C0): strokes more than 65 ms apart play long hits, closer ones double hits; velocity sets the dynamic (16 levels). | Strokes at 172, 203, 209.5 and the coda answer 277 / 278.5 / 279 (v56/60/60). | **Followed.** All strokes are more than 0.5 s apart, so all play long hits. Coda strokes sit 3 dB under the master (A) and are the answer the score asks for. |
| p.124 (Felt Short): use it for strokes that must stop within a beat or two. | The printed "damp" at qn 210 after the 209.5 stroke. | **Followed in effect.** The 209.5 stroke ends at 210 and has fallen 16 dB by 210.0 (measured). |
| p.124: in the Felt KS patch, CC11 and velocity control overall loudness. | The roll level. | **Not tested.** The render uses CC7 (LEARNINGS §10 says the patch has no CC11). The .oib's Global Group does have a "Controller 11" processor wired to Source/volume, labelled "Amount Controller 1->Volume". CC7 works and gives the levels below, so this needs no change. |
| p.124-125: KS map C0-E0 (Lng, Sht, Flm, Rls, Crs). | `ks` lane: keys 24 (Lng) and 27 (Rls). | **Followed** (Opus C0 = MIDI 24). |

MANUAL-GAPS read: #7 (Felt Cresc) stays open. #8 (basses 4 soli on DIV A) is still timbre only, because the 4-soli levels are now consistent (section D below). #4 (Mid mics on the solo winds) is not needed for any finding here.

## Extra check 1: did c41's width_by_mic move any solo's margin or seat? (measured)

**No solo's level against its accompaniment moved by more than 0.3 dB.** Per-bar solo-minus-rest margins, c40 -> c41, A and K:
- Horn 1, bars 7-14: +0.2..+0.3.
- Oboe 1, bars 15-20: -0.1..-0.3, except bar 15 at -1.0 A / -0.8 K. That comes from the longer string releases under it; the oboe's own level moved only -0.3.
- Solo violin, bars 17-22: ±0.1.
- Bass clarinet, bars 31-36: ±0.2.
- Flute 1, bars 37-44: -0.1..-0.6 (bar 40 -0.6 A).
- Cor anglais, bars 41-50: -0.1..-0.4.
- Clarinet 1, bars 85-89: ±0.3.

**Seats (R-L above 150 Hz) moved by at most 0.8 dB, but the solo winds' images are wider:**

| Stem | R-L | side/mid | correlation | mid level |
|---|---|---|---|---|
| Oboe 1 | +2.1 -> +1.3 dB | -11.8 -> -9.1 | 0.90 -> 0.79 | -0.2 dB |
| Cor anglais | +4.0 -> +4.2 | -9.1 -> -6.8 | 0.87 -> 0.73 | -0.3 |
| Flute 1 | -0.8 -> -0.9 | -14.0 -> -12.5 | 0.93 -> 0.90 | |
| Bass clarinet | -2.5 -> -3.3 | -8.8 -> -7.7 | | |
| Clarinet 1 | -1.9 -> -2.0 | (unchanged) | | |
| Violoncellos, bars 23-28 | | -7.6 -> -4.8 | 0.82 -> 0.60 | |

- The solo violin (corr 0.92) and Horn 1 did not change.
- **Horn 1's `width_by_mic {"Main": 0.2}` has no effect.** `build_reaper.py` line 136 takes `max(track width, mic width)`, and the horn group width is 0.3, so Horn 1's Main stays at seat ±0.3. Only Clarinet 1's 0.2 (track width 0.05) acts.
- Inferred: the oboe and cor anglais solos are now a little less focused than the solo violin, but their levels, seats and margins are intact. I propose no change. If a listener finds the solos diffuse, give Oboe 1, Cor anglais and Flute 1 the same per-track `"width_by_mic": {"Main": 0.2}` as Clarinet 1 (mix only).

## Extra check 2: Horn 1's counter-melody, bars 56-58 (qn 182-196): see finding 1

From qn 186 the horn now sits -2.0..-12.7 dB under Violins I (A, per 0.5 qn). In c40 it was -5..-15.
- **c41 did lift it where it acted:** +2.3..+2.6 dB at 184-189.5 and +1.2..+1.8 at 189.5-191.5, from the shelf ramping out by 182 instead of 194. It had no effect from 192 on. CHANGES.md says "from 186 on unchanged"; my measurement disagrees for 186-191.5.
- **Two problems remain:**
  - the 182 note now overshoots;
  - 184-195.5 is still mostly 7-13 dB under.

## 1. Bars 56-58: Horn 1's mp counter-melody bulges on the 182 note (as loud as its own f), then sinks 7-13 dB under the violins (measured; audibility inferred)

**Where.** Horn 1, qn 182-195.9. The marks are mp at 182 and again at 188 with a crescendo to f at 196, "1., espr." from 175. Violins I/II have the theme: mf at 184, crescendo 188-196, f at 196.

**Evidence (measured, c41).**
- **The 182 head (G flat 4) is too loud.**
  - A 30.9 / K 33.3 over 182.4-183.0. The same pitch at the printed f at 196 measures A 30.6 / K 32.6, so the mp note is as loud as the f.
  - Its 2-5 kHz energy (+15.6, relative) equals the f note's (+17.1).
  - Against Violins I it is +4.4 at 182.5 and +5.8 at 182.75 (per 0.125 qn), above the melody.
  - Causes: the c41 +5 dB shape inside the note (`score_config.py` line 951) stacks on 9.5-11.7 dB of existing envelope there (roles, hairpin, early fill), and the shelf is now out.
- **From 184 the horn sinks under the theme.** Horn 1 minus Violins I (A, per 0.5 qn), 184-195.5:

  -9.6, -5.3, -7.1, -9.7, -5.0, -7.7, -8.3, -12.7, -9.9, -8.8, -10.6, -10.4, -5.2, -3.5, -8.6, -7.0, -8.4, -5.6, -7.6, -9.0, -8.6, -8.3, -6.6, -11.9

  The median is -8.4. The horn's own level stays flat at A 20-25 through its printed crescendo 188-195.5.
- **The target.** One printed step under the theme is about -4..-6 dB on this mockup's scale (c39/c41 B). Adler, *Study of Orchestration* (PDF p.132), puts the counterpoint (middleground) between the foreground line and the background. Here it sinks to the background level for most of the phrase. Bassoon 1 + Clarinet 1 (p/mp under it) are only +0.3..+2.8 dB under the horn at 191.5-194, and above it at 194.5-195.5 (-0.9..-5.1).

**Fix (`build/score_config.py`).**
- Line 951: change the 182 shape to `[(182.6, 0.0), (182.95, 2.0), (183.8, 2.0), (183.9, 0.0)]`, i.e. +5 -> +2.
- Add `LEVEL_SHAPES["Horn 1"] = LEVEL_SHAPES["Horn 1"] + [[(183.95, 0.0), (184.1, 3.0), (195.35, 3.0), (195.5, 0.0)]]`.
  - It rises at the 184 legato target and falls at the 195.5 pickup onset, so both ramps are covered by new attacks.
  - The 196 f stays as it is (it is already -5.0 / +0.9 at 196 / 196.5).
- This is a stem-level change. It can be applied by `stem_fix.py` if no other Horn 1 change forces a render.

**Expected (simulated).**
- Horn 1 minus Violins I, 184-195.5: median -5.3, range -0.5..-9.8.
- The 182 head about +3 over Violins I at 182.5, and about 2 dB under the 196 f.
- 183.5 stays near -10, where the violins move.
- Bassoon 1 + Clarinet 1 at least 3 dB under the horn at 188-195.5.

**Check.**
- The Horn 1 1-5 kHz share at 175-181 is unchanged.
- The 182 head is at least 1.5 dB under the f note at 196 (same pitch, A).
- Violins I is the top stem (A) on every 0.5 qn 184-195.5 except at most two.

## 2. Bars 7-14: Horn 1's p "dolce espr." theme is only 0-1 dB (K) over its pp accompaniment in five of eight bars, and 4-6 dB softer than every other p solo (measured; "the theme does not stand out" inferred)

**Where.** Horn 1, qn 17-41 (p from 17, mp at 34, p at 39). The accompaniment is Bassoons 1-2, bass clarinet and harp, all pp from 18. Roles now: Horn 1 `[16.5, 42, 2.5]`.

**Evidence (measured, c41).**
- **Horn 1 over the summed accompaniment, per bar 7-14.**

  | | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
  |---|---|---|---|---|---|---|---|---|
  | K | +0.7 | +0.9 | -0.3 | +1.6 | +3.8 | +2.9 | +0.3 | +0.3 |
  | A | +1.7 | +0.9 | +1.7 | +4.9 | +4.0 | +3.6 | +1.4 | +2.2 |

  Unchanged since c40 (±0.3).
- **In octave bands the horn is not above its accompaniment in its own register.**
  - 500 Hz: -3.7 in bar 8, -1.0 in bar 13.
  - 2 kHz: -0.3..-4.1 in six of eight bars.
- **The other solos clear their accompaniment by much more:**

  | Solo | K | A |
  |---|---|---|
  | Oboe 1, bars 15-20 | +2.6..+4.4 | +5.8..+8.3 |
  | Solo violin, bars 17-21 | +3.4..+6.1 | |
  | Bass clarinet, bars 31-36 | +1.8..+6.8 | |
  | Cor anglais, bars 41-44 | +1.9..+3.7 | +7.9..+10.8 |
  | Clarinet 1, bars 85-86 | +2.8..+3.3 | +9.9..+10.1 |

- **Median K of note bodies at printed p (the same p in every family):**

  | Instrument | K at p |
  |---|---|
  | Horn 1 | 20.8 |
  | Bass clarinet | 20.8 |
  | Cor anglais | 23.1 |
  | Oboe 1 | 24.3 |
  | Flute 1 | 24.4 |
  | Violin I solo | 25.7 |
  | Violins I (tutti) | 22.3 |

- **Rimsky-Korsakov, *Principles* (text, "Comparison of resonance", PDF p.51):** "in piano passages, all wind-instruments, wood or brass are of fairly equal balance". A p horn solo should therefore weigh as much as a p oboe or flute solo, not 4 dB less. Over pp woodwinds it should sit a clear step above them.
- The colour is a deliberate choice and should stay: the soft-horn 800 Hz -8 shelf (c37 do-not-touch) keeps the p horn dark. So the fix is level only.

**Fix (`build/roles.json`).**
- Horn 1: `[16.5, 42, 2.5]` -> `[16.5, 42, 4.5]`.
- Bassoon 1, Bassoon 2 and Bass clarinet: add `[17.5, 41.9, -1.5, 0.5]`.
- Both are slow 1.5-2 dB moves under sounding chords, so no audible tail cut (S3).
- After the render, re-check Horn 1's p soft trim (`mix.json` 5.5) only if Horn 1's p bucket moves more than 2.5 dB.

**Expected (simulated).** Margins in bars 7-14:

| | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|
| K | +4.0 | +3.8 | +2.6 | +4.3 | +6.9 | +6.1 | +3.3 | +3.4 |
| A | +5.1 | +4.2 | +5.0 | +8.1 | +7.4 | +7.0 | +4.7 | +5.5 |

Horn 1 at p about K 22.8, still at or under the other p wind solos. Soft passages get louder, so the delivered span narrows slightly. The limiter is not affected.

**Check.**
- Horn 1 is at least +2.5 K over the summed accompaniment in every bar 7-14.
- The bassoons and bass clarinet stay at least 3 dB over their own ppp level elsewhere.
- Bar 15 (Oboe 1's entry) is unchanged.

## 3. Bar 40 (qn 120-124): Flute 1's p phrase end is level with the Violins II pp accompaniment (measured; inferred: the theme blurs into the sul tasto chord before the cor anglais takes over)

**Where.** Flute 1, theme B, "dolce cantabile". It is p at 120 after the 118 decrescendo, holding B flat 4 from 122 to the breath at 124. Underneath are Violins II and Violins II div at pp sul tasto, violas, basses pizz. and harp.

**Evidence (measured, c41).**
- **Flute 1 over all other stems, per 0.5 qn 120-123.5:**

  | | 120 | 120.5 | 121 | 121.5 | 122 | 122.5 | 123 | 123.5 |
  |---|---|---|---|---|---|---|---|---|
  | K | -0.1 | +1.5 | -0.7 | -0.7 | -1.3 | +3.6 | +4.6 | -1.1 |
  | A | +5.8 | +4.0 | +1.0 | +1.9 | +1.3 | +5.9 | +7.0 | +0.8 |

  Bars 37-39 margins are +3.8 / +2.5 / +3.9 K. The bar 40 margin fell from +1.4 (c40) to +0.9 K, the largest drop among the solos.
- **The closest voice is Violins II at -1.8..-3.8 K at 121-122,** printed pp, one step under the flute.

**Fix.**
- `build/roles.json` Flute 1: add `[120.4, 123.95, 2, 0.4]`. It rises inside the 120 note and ends at the printed breath before 124, so no tail cut.
- The c37 role `[125.75, 131.5, 3, 0.5]` and the cor anglais handover at 124 are untouched.

**Expected (simulated).**
- K margin at 120-123.5: +0.7..+6.6 (none under 0).
- A margin at 121-122: +3.0..+3.9.

**Check.**
- Flute 1 at 120-124 stays at least 2 dB under its own bar 37 level (A). The printed decrescendo to p must still be heard.
- The cor anglais entry at 124 stays at least 2 dB over Flute 1.

## 4. The bar 61-64 and 79-82 climaxes: no covering; no change (measured)

**Climax order.**
- c41's `_all` -0.4 dB lowered the master 0.4-0.5 dB (A) over 204-211.5 and nothing else.
- Bars 61-62 still lead the piece: master A 45.6-48.6 per 0.5 qn, against 41.1-44.1 in bars 79-80.

**Bars 61-62 (qn 204-212), against Violins I (ff) per 0.5 qn.**
- Trombone 2 (f) is -0.4..-5.2 K / -1.1..-5.5 A under.
- Bass trombone (f) is -0.7..-8.4 K, except 209.5 at +0.4 K / +0.6 A.
  - Its envelope rises 6.4 -> 8.8 dB over 208.8-209.75 inside the tenuto F sharp 2, then steps back at 210.
  - No role row in `roles.json` makes this rise. It is one half beat at parity in a molto sostenuto tutti and is not audible as covering (inferred).
  - Optional: hold the bass trombone's vol at the 208.8 value to 210.
- Tuba is -2.9..-11.6 K under.
- Timpani (f roll) is -17..-22 A under Violins I and ranks 18-22 of 32. Its 125 Hz octave is -7..-15 dB re master, so it is heard as the low floor without covering anything. Dan's rule 5 is met: the 203 stroke is -4 K re the rest, then the roll settles.

**Bars 63-64.** Trombone 1's ff quotation is +4.4..+15.8 dB over Violins I (the p tremolo strings), as the marks ask.

**Bars 79-82.** Timpani -14..-24 dB under the master (rank 12-21). There are no low brass. Violins I is the top stem in 9 of 16 half beats. The others are Flute 1's B flat 6 (+3.3..+4.2 at 262/266/268, printed ff) and Violins II / celli / oboe within 0.2-2.6 dB.

**The bass at the climax is solid, not boomy.**
- 63 Hz octave re 500-2000 Hz: -17.1 (61-62), -16.1 (76-78), -15.4 (79-80). Soft passages: -19.6..-23.4.
- The 125 Hz octave is thinner at the climaxes (-9.8 / -11.9 / -10.0) than at bars 53-58 (-4.8). That is the voicing issue described in LEARNINGS §14, not a mix fault.

## 5. Dynamic mapping across families, divisi and soli tracks (measured; no change beyond findings 2-3)

**Median K of note bodies by printed dynamic (c41).**

| Printed | Instrument | K |
|---|---|---|
| p | Flute 1 | 24.4 |
| p | Oboe 1 | 24.3 |
| p | cor anglais | 23.1 |
| p | bass clarinet | 20.8 |
| p | bassoons | 19.4-19.7 |
| p | Horn 1 | 20.8 |
| p | Violins I | 22.3 |
| p | Violins II | 22.2 |
| p | celli | 22.4 |
| p | violas | 17.6 |
| pp | winds | 13.8-19.3 |
| pp | horns 3-4 | 11.5-12.1 |
| pp | strings | 12.1-16.7 |
| ppp | strings | 3.9-12.3 |

Every family steps up from pp to p to mp. The only wind solo off its family's p is Horn 1 (finding 2).

**Half-section and soli tracks against their sections at the same mark (K).**
- Violoncellos div: pp 15.5 against celli pp 16.7.
- Violins II div: pp 16.3 against Violins II pp 15.6.
- Violas div: pp 9.1 / p 21.3 against violas pp 12.9 / p 17.6. In the coda the two viola tracks are within 2 dB bar by bar.
- Violin I solo: p 25.7 against Violins I p 22.3 (its +2 solo role).
- **Basses 4 soli now fit the tutti.** After c41's removal of the +3 and the refit:
  - 4 soli pp at 226-238: K 11.2 (c40 15.6).
  - Tutti pp at 238-250: 14.8.
  - Coda 4 soli pp at 286-298: 9.3.
  - Horn 1 over the basses at 226-237: +8.2..+17.1 A, +4.1..+15.2 K. c41 B's target of at least 6 A is met everywhere.
- **Small inversion.** The coda tutti ppp pedal (274-286, K 11.4) is 2 dB over the 4 soli pp (286-298). Inaudible under the harp harmonics and the clarinet (inferred).

**Final chord.** Violins I's C5 leads the strings, with the basses 5.7 K under the celli. Unchanged.

**Do not touch:**
- c41's width settings for the strings and low winds (the bass seat holds R-L +0.8 dB at 35-63 Hz);
- the c39/c41 bars 61-62 balance (Violins I +3, Horn 1 lift 5.5, Violins II CC7) and `_all` -0.4 at 204-212;
- Trombone 1's level and CC7 110/120;
- the timpani levels and `TIMP_CC1_MAP` at every roll and stroke (start at the printed level, settle 12-22 dB under the rest; ppp rolls 5-8 dB darker than f rolls);
- the basses' c41 pedal re-levelling (Horn 1 8-17 dB A over it);
- the celli counter-melodies (-4..-6 K under the violin pair in bars 23-28 and 71-74);
- Clarinet 1 and the cor anglais as an equal pp duet in bars 87-89;
- the solo levels of Oboe 1, the solo violin, the bass clarinet and the cor anglais;
- the divisi/soli track levels;
- fx_volume 0.095, the 160 Hz hall low cut, ir_setup 0.7;
- the soft-horn 800 Hz shelf (findings 1-2 change level, not colour).
