# Critic B, cycle 15: balance and levels (render c14)

Method. I computed K-weighted (BS.1770) 10 ms frames for the c14 master and all 29 stems, and A-weighted 50 ms frames for melody-against-accompaniment comparisons across registers, all placed on score qn with the parts.json tempo map. Pizzicato notes are compared by their peak frame within the first 0.15 s, because the sustain-window level of a pizz. note depends on its decay. Harmonic levels (H1..H4) are FFT bins at the note's fundamental and its multiples, measured 0.3-2.3 s into each note of 1 qn or longer. I simulated the proposed changes by scaling the stem frames. Scripts are in `/private/tmp/claude-501/mockup-loop/c15-B/`: `prep.py`, `trkdyn.py`, `famdyn.py`, `passacc.py`, `melA.py`, `melgrp.py`, `bardyn.py`, `seq.py`, `abeats.py`, `simswell.py`, `harm.py`, `loudspec.py`, `stemspec.py` and `cbvc.py`. `build/parts.json` (19:00) is the c14 data after the A #3 revert, which matches the delivered stems.

## Delivery, c14 (measured)

| | Master | mp3 |
|---|---|---|
| Integrated | -23.8 LUFS | -19.8 LUFS |
| LRA | 23.5 LU | 16.0 LU |
| True peak | -4.5 dBFS | -1.7 dBTP |
| p10-to-max short-term span | 26.2 dB | 18.2 dB |
| Limiter | | 2.0 dB |
| Climax rise over the 15-20 s before | 12.6 dB | 10.9 dB |
| 5 s level moves reversed by the ride | | 0 |

Every delivery target is met. None of the fixes below changes the loudest passages.

## What holds (measured)

- **Dynamic mapping across families**, per-note medians (K). Every family's pp falls within 1 dB of the others, and p within 2.6 dB:

| | pp | p | mf | f |
|---|---|---|---|---|
| Winds | -46.9 | -39.2 | | -32.5 |
| Brass | -47.9 | -38.7 | -32.5 | -32.4 |
| Strings | -47.4 | -41.3 | -37.4 | -33.1 |

  The wind and brass p medians are dominated by the exposed solos, which carry +2 to +2.5 solo roles.
- **pp accompaniment in eight passages** sits between -44.4 and -51.5 K per voice, whatever the family:
  - Bars 3-6: Cl2, BCl, Hn3 and Hn4 at -47.0 / -47.6 / -46.5 / -50.0.
  - Bars 87-91: Cl2, Hn3, Hn4, Vln II, Vla, Vc and Cb at -47.3 to -50.0.
  - pp sounds like pp in every family.
- **Melody over its loudest other stem**, A-weighted median per beat:

| Passage | Margin |
|---|---|
| Horn, bars 7-14 | +9.2 |
| Oboe, bars 15-16 | +10.2 |
| Oboe, bars 19-20 | +13.1 |
| Solo violin | +8.6 |
| Theme A, Vln I+II | +9.5 / +9.0 |
| BCl | +6.5 |
| CA, bars 41-44 | +5.1 |
| CA, bars 47-51 | +7.6 |
| Theme B, bars 53-56 | +8.4 |
| Bars 70-74 | +9.2 |
| Cl1, bars 85-86 | +11.6 |

- **Bars 61-62**: winds are 36-41% of the energy, strings 39-47%, brass 15-18% and timpani 1%. Brass printed f/mf sits 3.7 dB K under woodwinds printed ff, which is consistent with Rimsky's equivalences (Principles p. 33).
- **Timpani rolls** are 15-23 dB K under the master at ppp/pp and 18-19 dB under at f/ff. No roll is the loudest stem anywhere.

## 1. Unmarked swells peak as loud as the printed high point of their phrase (measured; simulated)

**Where.**
- Horn 1, bars 7-12: the swell in bar 8 (qn 20-24, p < > with no mark) against the printed mp at qn 34.
- Violins I+II, theme A: the bar 24 swell (qn 68-72, inside mp) against the printed mf at qn 82.
- The same figure at bar 72 (qn 240-244, inside p) against the mp at qn 250.

**What.** K level per qn of the lead line:

| Phrase | Unmarked swell top | Printed peak |
|---|---|---|
| Horn | qn 21-22: -32.2 / -31.2 | mp, qn 32-35: -31.2 / -31.6 / -32.8 / -32.0 |
| Theme A | qn 69-71: -32.2 (bar 28 mean -32.0) | mf, qn 82: -29.7 |
| Bar 72 | qn 241-242: -31.8 / -30.5 | mp, qn 250-251: -31.7 / -30.5 |

- The horn's ornamental swell reaches the phrase's printed mp, and in bar 72 a p swell reaches the next mp. In theme A, the printed mf is one beat 2.5 dB over the bar 24 swell, and the bar as a whole is level with it.
- Master momentary loudness confirms this. In theme A, bar 23 (p/mp) is -32.0 LUFS, bars 24-27 are -32.3 and the mf bars 28-29 are -31.4: three printed levels within 1 dB.

**Cause.**
- `base_points` sends an untargeted crescendo from p up to the CC of the next printed mark, because of the c11 "cap at the mark itself" rule. The horn swell goes 54 -> 66, the same CC as the mp at qn 34.
- The c14 `LEAD_SPANS` block in `build_track` then adds `HP_GAIN_SOFT_DB` +3 dB to that swell. The horn's vol_db at qn 22 is +5.5 (role 2.5 + 3), and +7.0 at the mp (role 2.5 + crest 1.5 + 3).
- In theme A, the bar 24 notes also carry the note trims Vln I 68 +4 / Vln II 68 +6 and the early fill at 68.

**Fix.** In `tools/score_to_parts.py` `build_track`, c14 soft-hairpin block (about line 1668), messa-di-voce branch: skip the soft gain when both of these hold:
- the crescendo has no printed dynamic within 1 qn of its end;
- a louder mark than `base(a)` is printed later in the same phrase, using the same look-ahead as `base_points`' `nm2` (up to the next 2 qn rest, at most 16 qn).

This affects Horn 1 qn 20, Violins I/II qn 68 and qn 240, and nothing else in the current `LEAD_SPANS`. The explicit fallback is `SWELL_NO_SOFT_GAIN = {"Horn 1": [20], "Violins I": [68, 240], "Violins II": [68, 240]}`. Leave `HP_GAIN_SOFT_DB` 3 and every other lead hairpin unchanged.

**Predicted** (`simswell.py`, the 3 dB shape removed from the stems):
- Horn swell top -31.2 -> -33.5. The mp crest is then 0.7-2.3 dB over it.
- Theme A swell -32.2 -> -34.4. The mf at qn 82 is then 4.7 dB over it, and the bar 27 crescendo (qn 79-81: -33.0, -31.5) rises out of the swell level.
- Bar 72 swell -30.5 -> -32.8. The mp at qn 250-251 is then 1.1-2.3 dB over it.
- The soft-passage loudness targets barely move: the change only lowers three 4-qn swells.

**Check after the render.** In each of the three phrases, the printed peak is at least 1.5 dB K over the swell top.

## 2. Bass pizzicato in bars 37-44 is the loudest event in the texture (measured; boominess inferred)

**Where.** Double basses pizz. p, qn 108-137.5 (bars 37-44), under the Flute 1 theme (bars 37-40) and the CA solo (bars 41-44). Celli play the same pizz. notes an octave higher in bars 37-40.

**What.**
- Peak frame of each pizz. note (K):
  - Cb -31.4 to -38.3, Vc -36.5 to -42.7.
  - Cb minus Vc: median +5.2 dB (+10.4 at qn 108, +9.4 at qn 120).
  - A-weighted, the Cb is -1.2 dB under the Vc. The excess sits in the low band.
- Against the melody (K):
  - Bars 37-40: the Cb pizz. peaks are 6-15 dB over the flute's level at the same moment (qn 120: -32.3 against -47.2).
  - Bars 41-44: they are level with or over the CA solo (qn 124 -34.9 against -39.3; qn 134 -35.0 against -37.7).
- Plain-RMS bar levels list the Cb as the loudest stem in bars 39 and 40, ahead of the flute melody.
- The F2 pizz. notes (87 Hz) have a fundamental 11-25 dB over their second harmonic. Each pluck is therefore a low-frequency thump. Dan listens with the volume turned up to hear the soft parts, which is when this thump is most exposed (inferred).
- **Cause.** Two lifts stack on these notes:
  - roles.json Double basses [108, 137.5, 5], added in c06 when the Cb sat 8 dB under the Vc;
  - the Cb `soft_trim_db` p, raised to 6.5 in c10 (global 3.5).

  Together that is +11.5 dB at p.

**Fix.** `build/roles.json` Double basses: [108, 137.5, 5] -> [108, 137.5, 2].

**Predicted.**
- Cb minus Vc pizz. peaks in bars 37-40: median +2.2 K, -4.2 A.
- Cb pizz. peaks 0-3 dB under the CA in bars 41-44.
- Bars 37-44 then match the soft-bar Cb-Vc balance accepted in c06-c09: Cb at or slightly under the Vc in A, and within 2-3 dB over it in K.

## 3. Flute 1 theme B (bars 37-40) has the weakest margin of any solo; its low notes sag (measured; simulated)

**Where.** Flute 1 "1." p, qn 108-124. The notes that fall away are C5 (72), Db5 (73) and Bb4 (70) at qn 112-113.5 and 119-123.5.

**What.**
- The flute's median margin over the loudest other stem is +4.7 dB A per half beat. Every other solo is +6.5 to +13.1. Ten of 32 half beats are under +3 dB.
- The weak beats fall on the low notes:
  - qn 113.5 +1.0, qn 120 +1.9, qn 123 +2.2 and qn 123.5 -3.8 (Vln II pp div. sul tasto over the flute's Bb4).
  - Over the same beats, the A-weighted flute level falls from 17-19 on F5 to 7-9 on C5/Db5/Bb4.
- Sample residuals (`pgroup.py`, level minus envelope minus 0.25 dB per CC):
  - F5 +2.4, Eb5 -1.0, Db5 -3.7, C5 -3.7, Bb4 -6.5.
  - That is a 9 dB fall over a sixth. The low register is weaker on a real flute too (Rimsky, Principles), but the line then needs light accompaniment. Here the Vln II already carries [108, 124, -5].
- At qn 108-109.5 the flute is level with the BCl's last held note (-2.0..+0.9). That is the printed hand-over and is not a fault.

**Fix.** `build/pitch_trims.json`, Flute 1: add `"70": 4, "72": 3, "73": 3`. These are legato notes, so `_all_arts_pitches` is not needed. The trims stop at onset + 3 qn and do not reach the high register.

**Predicted** (simulated by note). Median margin +4.7 -> +6.3, minimum -3.8 -> -2.0, beats under +3: 10 -> 7. The remaining low beats are the qn 110 Vln II swell and the BCl hand-over.

## 4. Bar 30 cadence: the celli drop out of the pp chord, and the basses sit on top (measured)

**Where.** Bar 30, qn 87-90. All five string parts are printed p > pp, with Hn3-4 pp and Cbn pp entering.

**What.** K per half qn, qn 88-89.5:

| Part | K level |
|---|---|
| Vln I | -45.3..-50.4 |
| Vln II | -45.1..-48.9 |
| Vla | -48.8..-49.9 |
| Hn3 | -44.9..-50.4 |
| Hn4 | -45.8..-48.3 |
| Cbn | -47.3..-48.4 |
| Cb | -45.9..-49.0 |
| **Vc** | **-53.2..-58.6** |

- The celli are 5-9 dB under every other voice in the chord. In the bar as a whole they are 8.0 dB K under the Cb (`cbvc.py`).
- **Cause.** roles.json Violoncellos [78, 90, -6]. It was set to keep the celli under the violins in the mf bars 27-29, and it still applies at the cadence, where everyone is pp.

**Fix.** `build/roles.json` Violoncellos: replace [78, 90, -6] with [78, 87, -6] and [87, 90, -2, 0.5] (end_ramp 0.5 qn into the cadence). Optionally add Double basses [87, 90, -2] on top of the existing [66, 90, -1].

**Predicted.** Vc -49..-54.6 at qn 88-89.5, within 1-4 dB of the violas, and the Cb about 1 dB under the violins.

## 5. Bar 79: the celli/bassoon moving line is 3-5 dB K (6-9 A) under the sustained violas and second violins (measured; musical weight inferred)

**Where.** qn 262-264.5 (bar 79). Vc f, doubled by Bn1 ff, plays the only moving line of the bar (Db4-C4-Bb3). Vla and Vln II hold ff notes.

**What.**
- K per qn, 262 / 263 / 264:
  - Vc+Bn1: -28.8 / -30.7 / -29.4.
  - Vla: -26.8 / -25.1 / -25.8.
  - Vln II: -27.5 / -25.1 / -24.2.
- A-weighted, the Vc is at 21.8-22.0 against the Vla at 28.3-30.0.
- The celli come up only on the Ab3 at qn 265 (-25.2 K). The roles already give Vc +2 and Vla +2.5 over [262, 268] (the c12 lift).
- Inferred: in a real tutti, celli at f in the Db4 register with a bassoon doubling are clearly heard as the moving voice under sustained harmony. Here the line reads as an inner murmur.

**Fix.** `build/roles.json` Violoncellos: add [262, 265, 2, 0.25] on top of the existing [262, 268, 2]. Leave the violas' c12 lift alone.

**Predicted.** Vc+Bn1 at -27..-28.5 K, within 1-3 dB of the sustained voices. The bar 79 master level rises by less than 0.3 dB (the celli are about 5% of the bar's energy), so the climax and limiter numbers do not change.

## 6. Low end at the climaxes: a 63 Hz band 18 dB over the Dvorak reference and a 100-200 Hz hole (measured; the remedy is not established)

**Where.** The loudest 10% of frames (bars 59-62 and 78-80).

**What.**
- 1/3-octave levels re 1 kHz (`loudspec.py`):

| Hz | 63 | 126 | 159 |
|---|---|---|---|
| mix | -7.1 | -10.2 | -11.1 |
| Dvorak, loud frames | -25.6 | -1.1 | +1.7 |

- Whole-movement Brahms references, re 1 kHz:

| Hz | 125 | 157 |
|---|---|---|
| Brahms 1/ii | -1.1 | -2.2 |
| Brahms 4/ii | +2.9 | +0.5 |

- In soft frames (10-30%) the mix tracks the reference at 126-159 Hz within 2.4 dB. The 100-200 Hz hole appears only in the tutti.
- The Double basses supply 94-99% of 30-90 Hz everywhere (`lowband.py`).
- Per-pitch harmonic balance of the Cb:
  - B1-D2 (pitches 35-38, 62-73 Hz) have a fundamental 5-12 dB over H2. Db2, n17, is +9.5.
  - Ab1 and lower are 13-22 dB under H2.
  - Db2 is the Cb note of both climaxes (qn 195, 204, 262, 265) and of the coda pedal (qn 286, 289).
- The climax 126-159 Hz band should come from BTbn, Bn2 and the timpani on Db3, and from the second harmonics of Cb, Cbn and Tuba. The celli play above it in these bars.

**Why not a firm fix.**
- The three references disagree by 27 dB at 63 Hz. The Brahms spectra are key-specific: both movements are in E, with B1 pedals at 62 Hz.
- A real double bass also radiates most strongly at 60-100 Hz.

**Suggested test, if the actor has a spare range render.** A Double basses ReaEQ bell at 69 Hz, -3 dB, bw 0.5 oct (mix.json `eq`), which touches only the B1-D2 fundamentals. Compare the climax 63/126 Hz levels and the Cb-Vc K balance in bars 83-92 (currently -0.4..-4.0) before keeping it. Do not change the Cb gain or its pitch trims for this.

## Do not touch

- The soft-trim table and its per-track overrides (pp and p consistent across families). `deliver_master.py` and TARGET_I. `LEAD_SPANS` soft gain 3/-2 on every hairpin except the three swells in finding 1.
- The bar 61-62 wind and low-brass roles. The `_all` [204, 212, -1] and the bars 79-81 lift (climax gap and limiter at target).
- `TIMP_HP_DB_FACTOR` 1.0, `TIMP_TIE_STROKES` and the timpani roll levels.
- The c14 soft solo roles: horn, Ob1, solo violin, BCl, CA, and the coda `_all` -2.
- The Vc div gain +4. The Tbn1 marcato velocities and its +2/+2 shape.
- The viola pizz. pitch trims in bars 41-44: by peak frame the notes are within 2.5 dB of each other (F4 -38.2, Gb3 -40.7). The sustain-window spread is decay, not level.
