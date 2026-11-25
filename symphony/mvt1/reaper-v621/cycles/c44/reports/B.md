# Critic B, cycle 44 (render c43): balance and levels

## Manual notes (second reading of the c38 B row: May 2021 HO manual PDF pages 118-120 and 123-126, read in full; MANUAL-GAPS.md and DIGEST.md read)

Open MANUAL-GAPS items for these pages come first, then the c38 B notes checked against the c43 render, then what the first reading missed.

| Source | What the manual says | Where it applies here | Followed in c43? |
|---|---|---|---|
| MANUAL-GAPS #12 (p.123, p.125) | Felt Cresc: recorded crescendo rolls in three lengths, each ending on a hard final stroke; "the most realism" for a roll crescendo. Felt Rolls with CC1 give control over length. | Printed roll crescendos into a stroke (316-324 into bar 82, 556-560). | **Still open, still low priority.** The CC1 roll at 316-324 sits at -10.5 dB K re M and grows into the stroke (measured). A recorded take would not fix a level problem. |
| MANUAL-GAPS #10 (p.123-124) | Felt Long: left-hand hits on C1-A2, right-hand hits on C3-A4; two notes within 65 ms play a damped double hit. | `TIMP_RH_ALT` since c37. | **Followed.** parts.json `timp_rh` lists the alternate strokes (105.5, 107.5, ... 534.5). The shortest gap between two strokes is 0.235 s, so there are no unintended double hits (measured). |
| p.118, 32in Med Tam Tam | Long hit on C1 (key 36), 12 velocity layers, "bassy resonance coupled with its high frequency splash". | fff at 484 (v124, heavy beater); pp at 696 (v60, soft stick). | **Followed, unchanged since c38.** At fff the tam-tam is the loudest stem from 484 to 490, by 1.9 / 4.1 / 3.8 / 6.2 / 4.9 / 4.2 / 1.4 dB K (c38: 0.9-4.0 dB A). At pp its 1-8 kHz band is -21.6 to -38.6 dB re M over 696-704 (c38: 17-42 dB under), so the v60 layer still has almost no splash (measured). |
| p.118, 22in Zildjian K Crash | Long note on C3, 7 velocity layers. | A long note at 636 to supply the top octave under the cymbal's peak. | **Followed.** Its 5-12 kHz band re M is -7.8 / -13.3 / -23.6 / -34.9 dB at 638 / 640 / 642 / 644 (c38: -15 / -25 / -36 at 640 / 642 / 644). Little is left to damp when the printed damp starts at 644 (measured). The hall barely reaches this band (5.5 kHz high cut), so the drier hall will not change it (inferred). |
| p.119-120, 18in Zildjian Sus Cymbal Cresc | Crescendo-sustain takes in four lengths; 2 velocity layers. | Key 64, `lead_s` puts the peak on 636. | **Followed.** At 635.5 / 636 the cymbal is the master's largest 5-12 kHz component (-1.9 / -1.8 dB re M). After the peak it is at -13.5 / -24.5 / -39.5 dB at 637 / 638 / 640 (c38: -15 / -26 / -39) (measured). |
| p.123-124, Felt Long velocity | Up to 16 velocity layers; CC11 and velocity set loudness. | Stroke velocities follow the printed dynamic. | **Followed.** On steady co-sounding beats the timpani sit, against the beat median: pp -1.8, f -0.4, fff +0.1 dB. ff reads -11.8 on 7 beats, because those beats are rolls that have settled under the texture (measured). |
| p.124-125, Felt Rolls | CC1 crossfades 8 dynamic layers for crescendos and decrescendos. | `TIMP_CC1_MAP`, `TIMP_ROLL_TRIM_DB`. | **Followed (Dan's rule holds).** Rolls sit at -15.2 (484-492), -16.8 (556-560) and -12.7 dB K re M (632-636). Only the solo opening is louder (-8.1 over 0-8) (measured). |
| p.124, Felt Short | Quickly damped hits for stops within a beat or two. | Not used. | **Still not needed.** The ff strokes at 328 / 330 ring into the bar-84 sub. p on the celli and basses' own G (c38). With the drier hall the timpani fall about 1.3 dB over 328-332 (model, finding 4). |
| p.125-126, hard-mallet patches | Brighter tone; clear single hits inside rolls. | v621 prints "medium sticks" at bar 26 and "soft sticks" at bar 175. | **Not followed** (felt throughout). Low priority and not a balance problem (unchanged). |
| **New**, p.118 with ONE_TIME item 2 | The 32in tam-tam's strength is its "bassy resonance"; its strongest partials are about 86 and 130 Hz (KIT §20, c38). | The c44 160 Hz low cut on the hall input. | **Not yet applicable.** The model (finding 4) puts the tam-tam's hall part at 23-30% of its level and the hall's 80-160 Hz return 9-15 dB lower. Its 80-160 Hz band then falls 1.2-1.3 dB, and its K level falls 0.4-0.5 dB on the fff stroke and 0.9-1.1 dB on the l.v. ring (496-504) and the pp stroke (696-708). In bars 175-177 that ring is the master's only content in those bins (c38), so check its decay there after c44. |
| **New**, p.123 ("the felt coating ... makes each note quite soft") with the timpani mics | Felt strokes are soft-edged, so in this mix much of their audible level comes from the room. | Timpani on Close 0.2 / Main 0.5 with send 0.45 (factory Close 0.43 / Main 0.24 / Surround 0.46). | **Measured:** the timpani have the largest hall share of any pitched track, 34-36% of their level. They lose the most with the drier hall: 1.1-1.6 dB (finding 4). |

DIGEST 9.1-9.4 agree with the table. No MANUAL-GAPS item on these pages changes state this cycle.

## Method

- **Data.** The c43 render: 40 stems after the stem fix and the second pass (`cycles/c43/render`), plus the pre-fix stems in `render_first` and the c42 render. Build data: `build/` at the end of c43 (parts.json, mix.json, roles.json, score_config.py).
- **Frames.** 2048-point STFT with a 10 ms hop, stereo power. 26 bands from 20 Hz to 24 kHz, plus K and A weighting. Data are binned per 1/4 and 1/8 qn. "re M" means stem minus master over the same window.
- **Summed tracks.** "Violins I" and "Violins II" include the bar 55-61 aliases "Violins I f62" / "Violins II f62" (stems 39 / 40). "Violoncellos" includes "Cello solo". The three "stac" aliases are summed with their source tracks. A unison partner whose part is dropped onto the first player's track (Trombone 2, Clarinet 2, Bassoon 2 in bars 131-133) is counted on that first track.
- **Hall model (finding 4).**
  - *IR.* I read the IR the shared hall uses, "S. Cal Hall Perc TS FR 3.3s", from `/Library/Application Support/East West/ImpulseResponseData/HOP True Stereo.ird` (4 channels of float32, 44.1 kHz). Its T30 is 2.45 s, which matches the 2.5 s measured on renders. I applied the 30 ms pre-delay and the 5.5 kHz high cut (assumed 12 dB/oct); for c44 I also applied the 160 Hz low cut (same slope).
  - *Per-stem fit.* For each stem the dry signal was recovered by power-domain deconvolution: stem = dry + g × (dry ⊛ IR energy per band).
  - *Fitting g.* g was fitted on each stem's own rests, 0.5-2.5 s after every note-off followed by at least 1.2 s of silence.
  - *Check against the sends.* g divided by send² is consistent across the 30 reliable stems: median 0.0087, most within a factor 0.6-1.4 (celli 2.0). This matches build_reaper's pre-fader send, scaled by mic volume, so the wet share depends on the send alone. I used both the per-stem g ("fit") and 0.0087 × send² ("common").
  - *Check against the decay.* Over 0.5-1.5 s after cutoffs the model's tail follows the rendered tails within 1-2 dB (e.g. Trumpet 1, qn 285.9: rendered -19.7 / -24.9 / -31.3 / -42.0 dB at 0.5 / 0.75 / 1.0 / 1.5 s against modelled -18.3 / -24.2 / -30.1 / -39.7). After about 1.7 s the rendered hall falls faster than the IR file, which has a noise floor at -52 dB; that late part carries almost no energy.
  - *Independent check.* Series-1 c09 raised the flute and oboe sends from 0.35 to 0.5 (+3.1 dB of wet). The measured level rise was +0.3 / +0.5 dB; this model predicts +0.37.
- **Simulations.** Proposed level shapes are applied to the 1/4 qn stem powers, and the change is added to the master power.
- **Scratch.** Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c44-B/`, deleted at the end.

## Findings, ranked by what a listener would gain

### 1. The c43 state contours on Horn 1, Trumpet 1 and Violas can be wrong by up to 14.5 dB after c44's full rebuild: check them before anything else (measured; risk inferred)

**What c43 did.**
- c43 sent the CC16 round-robin reset for the first time (`RR_RESET_CC`).
- With identical data, the Leg Slur MAX targets of Horn 1 and Trumpet 1 then rendered louder than in c42. I measured the c43 raw stems against c42, note body from onset + 0.1 s to the next onset - 0.03 s:
  - Horn 1, bars 47-52: -2.3 to +5.1 dB (15 of 17 notes louder);
  - Horn 1, bars 103-106: +0.6 to +8.6 dB (414.75: +8.6);
  - Horn 1, bars 147-154: -0.4 to +6.0 dB;
  - Trumpet 1, bars 69-71: +1.4 to +14.9 dB (283.29: +14.9);
  - Trumpet 1, bars 113-114: +0.7 to +6.6 dB on the contoured notes;
  - Trumpet 1, bar 161: +5.1 / +1.9 dB.
- The stem fix brought every note back to its c42 level: c43 final minus c42 is -2.1 to +0.9 dB, median 0.0.

**Why it matters for c44.**
- Those corrections now live as data: the "c43 stem fix" `LEVEL_SHAPES` rows in `build/score_config.py` (Horn 1 four phrases, Trumpet 1 three phrases, Violas 654.2-654.7 -5.6 dB). The c44 render will apply them through the volume envelope.
- c44 rebuilds every Opus instance in both passes (ONE_TIME item 5). If the fresh instances render the c42 state, every contoured note comes out low by the size of its cut. The largest cuts:
  - Trumpet 1: -14.5 dB on 283.33-283.9, -7.1 / -7.4 dB over 279.9-281.8;
  - Horn 1: -9.3 dB on 195.4-195.8 (the dolce solo of bar 49), -8.6 dB on 414.8-415.8, -7.1 dB on 417.4-417.8, -6.6 dB on 595.3-595.9 (the recap solo).
- The Horn 1 solo and the bars 69-71 trumpet tune would drop out.
- Trumpet 1 rendered in the loud state in both c42 (no reset; spliced back) and c43 (with reset); Horn 1 did only in c43. The state may well repeat, but no render has yet followed a full rebuild with the reset (inferred).

**Fix (c44 actor, before any other level fit).** Use the raw c44 stems of Horn 1, Trumpet 1 and Violas.
- **Measure.** For every note inside the contour rows, take its body level minus the same note in the c43 final stem, then add back the hall change predicted in finding 4 (Horn 1 / Trumpet 1 +0.8 dB, Violas +0.2 dB).
- **Within ±1.5 dB:** the state repeated. Keep the rows.
- **Low by about the row's cut** (the c42 state): delete that track's rows from the "c43 stem fix" block (score_config.py lines 2840-2861) and restore those notes by stem fix (`stem_fix.py` with the rows removed).
- **Mixed result:** handle each note on its own.
- **Not affected.** The Trumpets a2 and Horns a2 aliases carry no contour.
- **Record.** Write the result in MANUAL-GAPS "Results (c44)". Whether the reset makes these instruments repeat is the open question from c43.

### 2. Bar 170 (qn 676-679), the coda's ff fermata chord: a single first trombone on D4 covers the tune's arrival on B in Trumpets a2 (measured; fix simulated)

**Score (p.17).**
- The coda tune (Trumpets 1-2 a2, Horns 1-2 a2, violas unis., ff) arrives at 676 on B (Trumpets B4, Horns B3), accented, under a ff diminished chord with a fermata.
- Trombone 1 holds D4, an inner voice, also accented.

**Evidence (K re M per 1/4 qn; each column starts at the qn shown).**

| | 676.0 | 676.25 | 676.5 | 676.75 | 677.0 | 677.25 | 677.5 | 677.75 | 678.0 | 678.25 | 678.5 | 678.75 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Trumpets a2 | -9.4 | -10.1 | -14.1 | -15.7 | -15.9 | -14.2 | -13.5 | -11.2 | -12.3 | -11.3 | -9.5 | -11.1 |
| Trombone 1 | -11.0 | -8.8 | -7.7 | -8.9 | -8.9 | -8.3 | -9.1 | -9.4 | -8.7 | -8.8 | -11.0 | -9.5 |

- Trombone 1 is the loudest stem of the chord in most quarter-beats; Violins I (top F6) sits at -9.5..-11.3 over 676.5-678.75.
- The trumpets' arrival sits 4.4-7.0 dB under the trombone over 676.5-677.75, and 1.6-3.6 dB under it in four of the five quarter-beats after that. A-weighting agrees (Trombone 1 -7.7..-8.5, Trumpets a2 -10.4..-12.8 per qn over 676-679).
- **Causes, read in parts.json.**
  - The trumpets' fitted accent swell (`acc_fitted` 676) falls from +3.2 to -1.4 dB in the envelope within 0.5 qn of the attack, while the raw sample stays flat (-21..-23.5 dB).
  - Trombone 1's -2.5 dB role [672, 676] ends on the arrival downbeat (KIT §4, c25: a role that ends on a held note's downbeat moves the whole note).
- **Norm.** By RK, a trombone equals two horns. Two trumpets in unison should not sit under one trombone on an inner note of the chord (inferred).

**Fix (level only; `stem_fix.py`, then `--mix-only`), `build/score_config.py`:**
```
LEVEL_SHAPES["Trombone 1"] = LEVEL_SHAPES.get("Trombone 1", []) + [[(676.25, 0.0), (676.5, -3.0), (678.875, -3.0), (679.0, 0.0)]]
LEVEL_SHAPES["Trumpet 1"]  = LEVEL_SHAPES.get("Trumpet 1", [])  + [[(676.375, 0.0), (676.625, 3.0), (677.25, 3.0), (677.75, 1.0), (678.875, 1.0), (679.0, 0.0)]]
```
- The Trumpet 1 row reaches the Trumpets a2 alias in its 664.5-679 window. Check that parts.json "Trumpets a2" `vol_db` shows it. If the alias does not read its source's LEVEL_SHAPES, add the same shape to its alias tables.
- Trombone 1 notes off at 679.0. The tail hold keeps the envelope at the note's level through the fermata rest, so the 0 dB point at 679.0 does not lift the tail. Check this on `vol_db`.

**Simulated.**
- Trumpets a2 minus Trombone 1 per 1/4 qn 676.25-678.75: -1.3 / -6.4 / -6.8 / -7.0 / -5.9 / -4.4 / -1.8 / -3.6 / -2.5 / +1.5 / -1.6 → +0.2 / -0.4 / -0.8 / -1.0 / -0.4 / +0.1 / +2.1 / +0.4 / +1.5 / +5.4 / +2.4 dB.
- Master -0.2 dB over 676-679. The 167-170 short-term maximum stays third (-4.1 dB re bar 160).
- The drier hall lowers the trumpets about 0.3 dB more than the trombone (finding 4). That does not change this result.

### 3. Bar 158 (qn 629-632), the run-up to the climax: Horns a2 swell 4.5 dB on a held E4 while the melody's top octave fades, and end 4-5 dB over Violins I (measured; fix simulated)

**Score (p.16, ff, no hairpin until bar 159).** The G-to-E leap is in three octaves:
- top: Flutes 1-2 and Violins I, E6;
- middle: Trumpet 1, Violins II and Oboe 2, E5;
- bottom: Horns 1-2 a2 and celli, E4.

**Evidence (K, per 1/2 qn, 629.0-631.5).**
- **Horns a2.** Re M: -10.1 / -7.3 / -6.8 / -5.9 / -6.0 / -5.2. The raw sample (stem minus envelope) rises -23.2 → -18.5 dB over a flat envelope (+2.3 → +1.8) at a constant CC1 of 108: the sample blooms.
- **Violins I.** Re M: -11.5 / -9.1 / -9.1 / -10.3 / -11.3 / -10.6. Its raw sample falls -21.5 → -27.0 dB after the leap, and its envelope ramp (+1 → +4.6) recovers only part of that.
- **Top group (Violins I + Flutes 1-2) against Horns a2.** The top group sits at -8.8 / -7.3 / -7.6 / -8.8 / -9.9 / -9.0, so the horns go from 1.3 dB under the top group to 3.9 dB over it within two beats.
- **A-weighting.** It shows the same movement, smaller: the horns end level with Violins II and 3 dB over Violins I.
- **Norm.** By RK, two horns at ff equal about four woodwinds or two string sections, which is about the weight of the top group. A swell in the horns that is not printed, against a fading top voice, is heard as the horns taking over the held E (inferred).

**Fix (level only), `build/score_config.py`:**
```
LEVEL_SHAPES["Horns a2"]  = LEVEL_SHAPES["Horns a2"] + [[(629.25, 0.0), (630.0, -2.5), (630.5, -3.0), (631.75, -3.0), (632.0, 0.0)]]
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES.get("Violins I", []) + [[(629.75, 0.0), (630.5, 1.5), (631.0, 2.5), (632.0, 2.5), (632.25, 0.0)]]
```

**Simulated (per 1/2 qn, 629.5-631.5).**
- Horns a2 minus the top group: 0.0 / +0.8 / +2.9 / +3.9 / +3.8 → -1.8 / -2.6 / -1.6 / -1.0 / -0.3 dB.
- Violins I re M: -9.1 / -9.1 / -10.3 / -11.3 / -10.6 → -8.7 / -7.8 / -8.0 / -8.5 / -7.9.
- Master -0.2..-0.3 dB in bar 158. The step into bars 159-160 grows by that amount, which helps the climax.
- Trumpet 1 and Violins II (the middle octave) are unchanged.

### 4. The drier hall (ONE_TIME items 1-3) lowers each track by 0.15-1.6 dB; no balance point moves by more than about 1 dB except the timpani. Re-check the points below; do not pre-compensate (model, validated; see Method)

**Wet share and predicted change per track.**
- "Wet share" is the hall's part of the track's K level on beats where it plays (within 30 dB of the master).
- The change column is fx 0.19 → 0.095 plus the 160 Hz low cut, with the common fit first and the per-stem fit in brackets.
- A shorter hall (T30 2.45 → 1.75 s, ONE_TIME item 3) adds another -0.03..-0.10 dB on every track.

| Track (send) | Wet share | Level change, dB |
|---|---|---|
| Violins I, Violins II, both f62 aliases (0.25) | 4-5% | -0.14..-0.17 (-0.16..-0.17)* |
| Violas (0.25) | 7-8% | -0.23 (-0.27) |
| Violoncellos (0.25) | 11-19% | -0.40 (-0.72) |
| Double basses (0.25) | 13-15% | -0.54 (-0.62) |
| Harp (0.30) | 13-18% | -0.68 (-0.47) |
| Cor anglais, Clarinets, Bassoons (0.35) | 9-15% | -0.32..-0.40 (-0.30..-0.52) |
| Bass clarinet, Contrabassoon (0.35) | 13-15% | -0.50..-0.54 (-0.46..-0.49) |
| Oboes (0.5) | 10-13% | -0.43..-0.46 (-0.33..-0.44) |
| Flutes (0.5) | 16-21% | -0.55..-0.57 (-0.67..-0.75) |
| Trombones 1-2, Bass trombone (0.45) | 15-20% | -0.52..-0.55 (-0.62..-0.69) |
| Tuba (0.45) | 19-24% | -0.96 (-0.75) |
| Horns 1-4, Horns a2 (0.5) | 17-24% | -0.74..-0.87 (-0.60..-0.88) |
| Trumpets 1-3, Trumpets a2 (0.65) | 15-28% | -0.81..-0.85 (-0.52..-1.03) |
| Timpani (0.45) | 34-36% | -1.47 (-1.57); per passage -1.1..-1.6 |
| Tam-tam (0.45) | 23-30% | -0.92 (-1.22); stroke -0.4, ring -0.9..-1.0 |
| Suspended cymbal, Crash (0.45) | ≤13% | -0.27 / -0.44; the 5-12 kHz peak and ring are dry |
| **Master** | | -0.44 |

\* The f62 aliases' own fits are unreliable: each stem has only 2 s of rests.

**Uncertainty.** Even with a wet share 50% higher than estimated, the brass would lose about 1.3 dB and the violins 0.25 dB.

**What moves relative to the rest.**
- The trumpets and horns lose about 0.65 dB against the violins (0.3-0.4 dB against the master).
- The timpani lose 1.3 dB against the violins.
- The woodwinds lose 0.2-0.4 dB against the violins.
- This answers the coordinator's question: the high sends do lose more, but less than 1 dB.

**Predicted for c44 (K, common fit first, per-stem fit in brackets).**

| Balance point | c43 | Predicted c44 | Target, or why it is listed |
|---|---|---|---|
| Letter F, tune minus brass (388-407) | +5.6 | +5.9 (+6.0); per bar +4.0..+6.7 | B's 5-6 window; at its top edge |
| Bars 70-71, tune minus counter (276-284, per 2 qn) | +4.1 / +3.1 / +4.0 / +1.9 | +4.1 / +3.3 / +4.1 / +1.9 | unchanged (brass on both sides) |
| Bars 56-59, violins incl. f62 minus Clarinet 1 + Horn 2 (220-236) | +3.7 | +4.3 (+3.7) | the tune gains or holds |
| Horn 1 minus Violins I (498.5 / 499.0 / 499.5) | +5.8 / +3.4 / +2.9 | +5.1 / +2.5 / +2.1 (+5.3 / +2.7 / +2.3) | the c41 B #2 point; still positive |
| Coda, Trumpets a2 minus Violins I (664-676, per bar) | +3.8 / +6.7 / +8.6 | -0.6..-0.9 dB on each | still clearly on top |
| Coda, Trumpets a2 minus Horns a2 (664-676, per bar) | +1.2 / +2.0 / +4.5 | 0.0..-0.3 dB on each | still on top |
| Timpani re M (0-8 / 316-324 / 484-492 / 632-636) | -8.1 / -10.5 / -15.2 / -12.7 | -9.0 / -11.4 / -15.9 / -13.3 (-8.3 / -11.2 / -16.2 / -13.6) | rolls further under the texture, as Dan's rule asks |
| Timpani re M, coda pp motto (712-720) | -12.8 | -14.1 (-14.8) | the largest drop; check the strokes stay audible (c38: -1.2..-4.6 K at the stroke peaks re the master's beat level) |
| Tam-tam re M (484-492 / 696-700) | -7.4 / -11.6 | -7.3..-7.8 / -12.0..-12.5 | still the loudest stem for two bars |
| Short-term maxima re bar 160 | 26 -5.1, 122-124 -1.3, 156-159 -1.3, 167-170 -4.2 | each within ±0.2 dB of c43 | climax order unchanged |
| Master p10-to-max span | 30.7 dB | 30.7 dB | delivery unchanged |
| Master 125-160 / 160-200 / 80-125 Hz (density re 1 kHz) | | -1.0 / -0.5 / -0.2 dB | loud-bar 125-200 Hz share -0.9 dB; c43's 125 Hz third-octave was already 3.3 dB under the Dvořák (+3.7 vs +7.0 re 1 kHz) |

**Re-check list after the c44 render.**
1. **Finding 1 first.** Per-track changes beyond the predictions above by more than ±1.5 dB on unchanged data are state changes from the rebuild, not the hall.
2. **Then the table rows**, in their order. Fix only a point that leaves its window, with roles or note trims (stem fix).
3. **The low end.** If the 125 Hz third-octave falls by more than 1 dB, restore the body with the celli and basses' dry bells (mix.json `eq` 125 / 170 / 180 Hz), not by lowering the hall's low cut.
4. **Do not raise any send or `fx_volume`** to win back the brass (S4).
5. **By-product for the actor's tail checks (inferred from the model).** The master's drop 0.3 s after the cutoffs I could detect moves only 0.7-2.4 dB, because most of the first 0.3 s is the samples' own release:
   - bar 62: 12.0 → 12.7 dB;
   - bar 73 (288): 13.4 → 14.8 dB;
   - bar 138 (551): 14.3 → 16.0 dB;
   - bar 170 fermata release: 14.8 → 16.6 dB, and 32.2 → 34.6 dB at 1.0 s.
   - The shorter IR adds 0.1-0.9 dB at 0.3 s and up to 2.9 dB at 1.0 s.
   - Where c44 misses 13 dB at 0.3 s, the remaining early tail is the samples' own release (their recorded room), not the hall (inferred).

### 5. ONE_TIME item 4 (repeated string notes re-attacked on Sus MAX) can put the new strokes 2-6 dB over their legato neighbours at f and ff (inferred from measured row offsets)

**Evidence.**
- **Row offsets at the same CC11.** At CC11 80 and above, Sus MAX sustains sit over the Leg rows by: Violins II +4.7, Violas +5.6, Violoncellos +2.1, Violins I +1.7 dB (c07, the reason for `ROW_TRIM_DB` in score_config.py line 239).
- **The brief's figure.** BRIEF item 7 gives 3-9 dB between Sus MAX and Leg Slur MAX sustains at one CC11 (the re-bow fits).
- **Code.** `tools/score_to_parts.py` (line 4930) leaves `rep_sus` notes out of `ROW_TRIM_DB`: written-out repeated strokes "carry their own fitted levels". It also sets their velocity from `REBOW_VEL_BY_CC` (line 2797).
- **The risk.** If the new re-attacks are flagged `rep_sus`, or are built the same way, they get no row trim. Each repeat inside a loud legato violin or viola line then becomes a 2-6 dB bump. The present merge has the opposite fault (a 1-4 dB notch), so the change can over-correct.

**Fix.**
- **Row trim.** In the new re-attack branch of `score_to_parts.py`, give each stroke its track's `ROW_TRIM_DB` Sus MAX value when the printed level is CC11 80 or above. Do not set `rep_sus` on these strokes, or exempt them from that exclusion.
- **Measure.** After the render, measure every changed repeat: the re-attacked note's body (onset + 0.1 s to its end) minus the previous note's body.
  - Target -1.5..+1.5 dB, outside printed accents and hairpins.
  - Correct outliers with `note_trims.json` rows with a 0.1 s step (`NOTE_TRIM_RAMP_S`), by stem fix.
- **Keep A's check.** The dip itself (S1, 6 dB or more in the master) remains the articulation lens's check. This one only keeps the bodies level.

## Checks with no change proposed (measured on c43)

**c43's balance changes rendered as intended (K).**
- Bars 70-71: the tune leads its counter by +4.1 / +3.1 / +4.0 / +1.9 dB per 2 qn.
- Letter F: the tune leads the brass by +5.6 dB.
- Bars 56-59: the violins (with the f62 aliases) lead Clarinet 1 + Horn 2 by +3.7 dB.

**Dynamic mapping.** Method: on steady co-sounding beats, each track against the beat median.
- Every track is within ±3 dB at every dynamic, apart from:
  - melody roles: Violins I +3.3..+5.8, Clarinet 1 pp +7.2 (coda solo), Trumpet 1 +1.8..+2.9;
  - inner and register parts on the low side: Flute 2 f -4.4, Clarinet 2 f -4.2, Contrabassoon f -4.2 / fff -3.8, Bassoon 1 fff -4.3, Harp mp -4.4 (under a tune).
- **The trumpet tracks.** Trumpets 2-3 sit at 0.0..+0.9.
- **Single tracks that carry a dropped unison** (Trombone 1 in bars 131-133, a2) read +6..+9 dB against the beat median. This is correct, as the theme group is on top there.

**Fugato (bars 85-96).** Each entry leads the loudest continuing voice (A):
- Bassoon 1 + violas by 2.4-9.4 dB at 348-352;
- cor anglais + Violins II by 2.8-7.7 dB at 360-364;
- Violins I by 1.5 / 2.7 dB over Violins II at 372 / 376. Flute 1 is between +1.0 and -2.9 dB of Violins II there.

**Percussion and timpani.** See the Manual notes table; Dan's roll rule holds.

## Do not touch

- **Kept from c43.** The c43 B #1 / #2 / #4 / #5 data: the bars 70-71 shapes, the letter-F brass lift with its `PICKUP_LIFT` values, the bars 56-59 roles, the celli 100 Hz loud EQ.
- **Kept from c41-c42.** The B data: the Horn 1 dolce roles and violas +2, the bar-10 shapes, the cor anglais roles, the single `_all` rows into 636 / 484, the bar-72 brass lift from 283.75.
- **Second-pass tracks.** The f62 aliases with their release fit; the Trumpets a2 coda tune and its alias tables (finding 2 adds to them, it does not replace them).
- **Timpani and percussion.** The timpani roll levels, `TIMP_CC1_MAP` and `TIMP_RH_ALT`; the tam-tam fff and pp; the suspended-cymbal peak with the K Crash ring.
- **The mix.** The soft and dyn trims as a set, and every send (S4).
- **Every earlier do-not-touch item.**
