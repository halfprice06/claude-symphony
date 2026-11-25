# Cycle 10, critic B (balance and levels), on the c09 render

Method. All levels are K-weighted (BS.1770 shelf and high-pass applied in the frequency domain) on the stems and master in `cycles/c09/render/`, placed on the score with the `build/parts.json` tempo map (`tools/pcx.py` TM). Levels are energy means over the qn spans named. "Note level" is the first 0.10-0.15 s after the score onset for short notes, and +0.15 s to the note end (at most 0.7 s) for held notes. Values share one scale: compare them with each other, not with LUFS. Plain-RMS history comes from each cycle's `metrics/metrics.json`. Marks come from `build/mockup-events.tsv` and the score pages (pdftoppm). Bar b starts at qn 3(b-1). Scripts and scratch files were in `/private/tmp/claude-501/mockup-loop/scherzo-c10-B/` (deleted).

## Manual notes (cycle 10, slot B: group B4, May 2021 HO manual PDF pages 49-52, 202-204 and 208, read in full; MANUAL-GAPS.md read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.49 output configurations (Stereo: every mic summed to outputs 1/2) and "Load with Effects off" (drop the Opus convolution reverb and use the DAW's reverb on an FX bus) | every track: `mix.json` `opus_reverb_off`, four Spaces II returns since c06 | Yes. Opus reverb is off, each instance outputs stereo, and the hall comes from the returns |
| p.50-51 multi-outputs: each mic on its own DAW channel, each mic sent to the reverb bus by its own amount | depth against presence per family (the c09 wind send +3, the DIV sends +3.6 / +4) | No. Mics are mixed inside Opus (Close / Main levels in `mix.json`), and each track sends one post-fader stereo signal. Per-mic sends (Main to the hall, Close dry) would add depth without moving the dry balance. That is a blend-lens option, and I found no level fault that it would fix |
| p.52 multi-timbral instances (up to 16 instruments per instance) | 31 instances, one per track | Not used. Only memory is affected, not balance |
| p.202-203 Level Amp, Limiter, Limiting Amp (fixed-ratio levelling and hard ceilings) | none per track; the delivery master uses `tools/deliver_master.py` (ride plus about 2.7 dB of limiting in c09) | Correct not to use them per track: a leveller would flatten the printed dynamics, which the balance relies on (p against mf against ff). The findings below are fixed in the envelope or the trim tables, before any processor |
| p.204 SSL Bus Compressor (ratios 2:1 / 4:1 / 20:1, attack 0.1-30 ms, release 0.1-1.2 s or Auto) | could glue the tuttis | Not used. Not needed for balance: the summit is already the loudest passage and the delivered LRA is 14.7 LU |
| p.208 SSL Transient Shaper; "Invert" subtracts the attack ("getting body") | accent bite (Dan: weight, not bite) | Not used. The level faults found below are in sustained bodies, not transients, so the shaper does not apply to them |

## Findings, ranked by what a listener would hear

### 1. Coda build, bars 329-332 (qn 984-996): the winds' p sustained chord and the horns' pp crescendo peak a bar early. A single Oboe 2 is the loudest stem of bar 331, 4 dB over all the first violins carrying the theme, and the winds then drop 4-8 dB at their ff in bar 333 (measured; cause read in the code)

**Score (p.12).** Bars 329-332: strings play the staccato theme, mf with a crescendo to f at 332 and ff at 333. Oboe 2 (alone, "2."), cor anglais, clarinets, bass clarinet and bassoons hold a p chord with a four-bar crescendo to ff at 333. Horns 3-4 enter pp at 331 and Horns 1-2, trumpets and trombones pp at 332, each with a crescendo to ff/f at 333. The theme should stay on top until the ff.

**Measured (K, per bar):**

| bar (qn) | Oboe 2 | Clarinet 1 | Clarinet 2 | Cor anglais | Violins I | Violins II | Horn 4 | master |
|---|---|---|---|---|---|---|---|---|
| 329 (984) p / mf | -40.4 | **-33.3** | -40.1 | -43.6 | -31.6 | -39.3 | - | -27.1 |
| 330 (987) | -36.2 | **-32.3** | -38.2 | -34.6 | -33.0 | -34.1 | - | -25.0 |
| 331 (990) | **-26.0** | -29.1 | -40.0 | -37.3 | -30.3 | -31.9 | -33.0 (pp, at 992) | -21.9 |
| 332 (993) f | -32.6 | -30.6 | -34.3 | -34.5 | -29.8 | -32.1 | -32.7 | -21.1 |
| 333 (996) ff | -34.0 | -35.4 | -33.6 | -39.1 | -23.1 | -28.0 | -30.4 | -18.1 |

- Plain-RMS history for bar 331 (metrics.json), Oboe 2 against Violins I: c00 -35.4 / -32.4, c05 -35.6 / -32.6, **c07 -28.7 / -33.5**, c09 -28.7 / -33.1. The fault arrived in c07.
- Cause (read, `tools/score_to_parts.py` hairpin points and `build/score_config.py` HP_CURVE). c07's `HP_CURVE = {"cresc": (0.4, 0.7)}` puts 70 % of a crescendo's rise at 40 % of its length, and only the timpani are skipped. On this 12-qn crescendo the winds' CC11 reaches 94 at qn 988.8 (bar 330) and 100 at 991 (Oboe 2 and Clarinet 1 CC11 lanes in parts.json), about f, two bars before the ff. `HP_GAIN_DB` adds +2..+3.8 dB in the envelope over the same span.
- The early peak makes a reversed crescendo. Every wind is softer in bar 333 (ff) than in bar 331 or 332. The bar-333 notes are the staccato theme head, and from 996 the summit roles (-3..-5 dB) apply.
- Horns 3-4 (pp at 990) reach -33.0 at 992, 2 dB under Violins I (f). Horn 1 (p at 993) reaches -30.8 at 995, over Violins I between its notes (-38.5).
- Oboe 2's F5 at 990 adds about 8 dB of its own (finding 2). Clarinet 1 sits within 0-2 dB of the theme in bars 329-330 without any hot pitch.

**Judgement.** For a listener, the four-bar build loses its theme in bar 331: a held wind chord, topped by one oboe, covers the strings' staccato head. The wind chord then thins out at the downbeat that should be the arrival (measured). The norm is the scherzo's own texture: a sustained harmony that crescendos under a theme should stay under it until the target (inferred, Rimsky-Korsakov's "sustained harmony in the middle parts").

**Fix.**
1. Generic, in `tools/score_to_parts.py` (the HP_CURVE branch at the `if hk == "cresc" and HP_CURVE.get("cresc")` line): a long-crescendo shape, off by default. In `build/score_config.py`: `HP_CURVE = {**HP_CURVE, "cresc_long": {"min_qn": 9.0, "pt": (0.6, 0.35)}}`, so a crescendo of three bars or more ("poco a poco") reaches 35 % of its rise at 60 % of its length. With this, the winds' CC11 at 990 is about 66 instead of 99.
2. If you would rather not change the curve this cycle, use `build/roles.json` (0.5 qn ramps, all ending before the ff): "Oboe 2" `[987, 995.5, -4]`, "Clarinet 1" `[984, 995.5, -4]`, "Clarinet 2" `[987, 995.5, -3]`, "Cor anglais" `[987, 995.5, -3]`, "Horn 3" and "Horn 4" `[990, 995.8, -4]`, "Horn 1" and "Horn 2" `[993, 995.8, -3]`.
3. Targets (K, per bar): every wind and horn at least 3 dB under Violins I in bars 329-331 and at least 1 dB under in bar 332. Each wind's bar-333 level at least equal to its bar-332 level. Master bars 329-333 rising monotonically, as now (-27.1 / -25.0 / -21.9 / -21.1 / -18.1). If bar 333 still falls after the curve change, start the winds' summit roles at 999 instead of 996 for the staccato head only (Oboe 2, cor anglais, clarinets: `[996, 998.9, +3]`).
4. Check the other long wind and brass crescendos that the new curve would touch (300-309, 372-387, 900-909) for unchanged arrivals.

### 2. Three wind samples are 6-10 dB hot on one pitch each: Oboe 2's F5, the cor anglais' A4 on its sustain rows, and Oboe 1's A5 on its staccato row. Each one pops out of the chord or unison it belongs to (measured)

Method: I compared each note against same-track notes with the same CC11 and vol_db, and against a doubling track with identical controller data.

- **Oboe 2, F5 (pitch 77), Sus MAX (its only row).**
  - qn 990: -26.6 dB after removing vol_db, against -37.3 (F sharp 5 at 987) and -35.0 (D sharp 5 at 993) on the same crescendo. Clarinet 1 on the identical CC11 and vol lanes rises only 3.5 dB from 987 to 990.
  - qn 903 (bar 302, sfp crescendo): Oboe 2 -27.1 against Oboe 1 -37.1 on an identical CC11 lane. The next F5-free note (E flat 5 at 906, with higher CC11) is -32.5.
  - In bars 302-303 (903-906) Oboe 2 is the loudest wind, -25.5..-28 against Violins I at -24..-31.
  - Estimate: about +8 dB. F5 occurs only at 900, 903 and 990.
- **Cor anglais, A4 (pitch 69), Sus MAX / Leg Slur MAX.**
  - Residual over the track's CC11 fit: median +6.8 dB over 9 held notes (148, 302, 310, 327, 399, 402, 900, 910, 927).
  - Examples: 310 -26.6 against 308 -38.0 and 315 -32.7 (CC11 110-116); 327 -25.4 against 315 / 345 / 351 at -32.7..-32.9; 900 -34.7 at CC11 56 against 902 -42.4 at CC11 76.
  - In the ff tuttis the cor anglais' A4 at 327 and 927 is level with Violins I (-25.5 against -25).
- **Oboe 1, A5 (pitch 81), Stac DblTng RRx9.**
  - In the unison f staccatos with Flute 1 (114-130, 204-213, 816-826, 888-897), Oboe 1 minus Flute 1 is +4.2 dB on A5 (n 13) and -1.7 dB on the other pitches (n 31).
  - Bar 41 (qn 120): Oboe 1 -27.6, Flute 1 -34.1, Violins I -26.0. The c09 flute fix (B #2) reads as solved except on this one pitch.

**Fix.** In `build/pitch_trims.json`, with values halved per LEARNINGS c09 ("`_all_arts` trims moved the stem about twice the value"). Simulate them first with `tools/stem_fix.py --out` and measure with the K-weighted note level:
- "Oboe 2": `{"77": -4, "_all_arts": true}`
- "Cor anglais": `{"69": -3.5, "_arts": ["Sus MAX", "Leg Slur MAX"]}`
- "Oboe 1": `{"81": -3, "_arts": ["Stac DblTng RRx9"]}`

Targets: each pitch within 2 dB of its neighbours after vol_db; Oboe 2 under Oboe 1 at 903; the cor anglais at least 4 dB under Violins I at 327 / 927; Oboe 1 A5 within 2 dB of Flute 1 in the unison f staccatos.

### 3. Trio, bars 221-224 (qn 660-672): Horn 1's p tenuto chord tone is level with Violins I's f tune and 2-4 dB over Violins II's. Flute 1's mf doubling sits over Violins I in bar 222 (measured; standing since c00)

**Score (p.8).** Bar 221: violins f (falling from the ff of 218), with <> hairpins. Flute 1 mf doubles the tune. Horns 1-2 p, held tenuto chord tones with a decrescendo. Clarinet 1, violas and celli mf.

**Measured (K, per bar):**

| bar | Horn 1 | Violins I | Violins II | Flute 1 |
|---|---|---|---|---|
| 221 | **-34.7** | -34.2 | -38.0 | -38.4 |
| 222 | **-34.7** | -32.7 | -36.1 | **-31.9** |
| 223 | -40.6 | -33.7 | -36.6 | -35.8 |

- Plain RMS for bar 221, Horn 1 against Violins I: c00 -34.6 / -36.4, c09 -36.0 / -36.9. The fault has been there since the port.
- Horn 1's p at 660 (-34.7) is only 1.1 dB under its mf at 654 (-33.6). Its CC1 (the horns' dynamic layer, soft map) moves only from 70-72 to 64-67 between the two marks. CC11 54-59 and vol 0 to +3.5 at 665.9 (parts.json).
- In the metrics table Horn 1's p and mf medians are only 2.5 dB apart (-40.4 / -37.9; inferred to be the same narrow CC1 range).

**Fix.** In `build/roles.json`: "Horn 1" `[660, 669.5, -5]`, "Horn 2" `[660, 669.5, -2]`, "Flute 1" `[660, 669, -2]`. Targets: Horn 1 about -40 (6 dB under Violins I) in bars 221-222, and Flute 1 2-3 dB under Violins I. For later: with the horns' CC1 floor (57), a horn p needs an envelope offset rather than CC1. Check Horn 1's other p chord tones under a tune with the same comparison (I found no other case over 2 dB).

### 4. Trio entry, bar 169 (qn 504-506): the celli's mp tune starts with a 10 dB spike at the first legato join. Reverting c09's A #4 (planned for c10) removes only part of it (measured)

- **c09:** celli -27.0 at 505.5-506.0, against -36.5..-39.9 for the body that follows (506-509.5). The master in bar 169 is -28.8 plain RMS, the loudest bar between 154 and 196.
- **c08 (before A #4):** the same frame was -33.4 against a body of -38.8, so a 5.4 dB spike remains after the revert.
- Data (parts.json): the second note (506, A3) is a v106 legato target moved to 505.44. It plays under the first note's envelope rise (vol +3.65 at 505.67 in c08, +6.9 in c09 with the 4 dB early fill). The envelope then falls 3-7 dB at 506.0-506.3 under the transition. The loud v106 transition lands at the top of the rise.
- **Fix.** After the revert, add `build/note_trims.json` "Violoncellos": `{"506.0": -3}` with `NOTE_TRIM_RAMP_S` 0.02, or end the first note's swell at 505.3. Target: the 505.4-506.0 frame within 2 dB of the 506.5-508 body, and bar 169 in the master within 2 dB of bars 170-172 (plain RMS -35..-38).

### 5. Reprise, bars 253-272 (qn 756-816): the violas' pizzicato pp off-beats sit 6.4 dB under Violins II's pizzicato pp on the same beats, and their beat 2 is 3.5 dB under beat 3 (measured)

**Score.** Bar 253: Violins II and violas pizz. pp, off-beat quarters on beats 2 and 3 under Violins I's mp leggiero theme. Same velocity (v41) and similar CC11 (34-39) on both tracks.

**Measured (note level, first 0.1 s):**
- Violins II median -50.2 (beat 2 -50.7, beat 3 -49.1, n 26).
- Violas median -56.6 (beat 2 **-57.5**, beat 3 -54.0, n 28).
- Neither track has a role here. With `RR_RESET_AT` "Violas" [756.0], beat 2 always draws the same weaker round robins of the four.
- At theme A (bars 13-28, arco staccato pp) the two sections are within 1.2 dB of each other (-49.5 / -48.3), so the pizz row is the difference.

**Fix.**
- In `build/roles.json`: "Violas" `[756.5, 810, 4]`.
- In `build/note_trims.json` "Violas": +3 on each beat-2 onset (757, 760, 763, 766, 769, 772, 775, 781, 784, 787, 790, 793, 796, 799), as steps (`NOTE_TRIM_RAMP_S` 0.02).

Target: violas within 2 dB of Violins II, and beat 2 within 1 dB of beat 3. Violins I stays 13+ dB over both.

## Measured and in balance (for the record)

- **Theme A 13-28.** Violins I (p leggiero) -38.4 note level. Violins II / violas (pp) -49.5 / -48.3. Celli / basses pizz. (p) -54.8 / -57.0. Timpani -57.9. The tune is clearly on top. The pizz. bass is quiet in K but carries the master's 20-100 Hz share (-15.5 dB here, against -18.7 for the whole piece).
- **Counterstatement 29-36.** Violins I -45.0, Flute 1 -45.0, Oboe 1 -47.1 in call and response.
- **Second idea 45-56.** Violins I -31.8 / -26.0 over Oboe 1, Violins II and Flute 1 (-32..-34.7). The c09 tutti violas fix holds: 105-120 violas -33.6 against celli -32.6.
- **Sub. p, bars 121 and 277.** At 121-124: Violins I -36.6, Violins II -40.8, violas -42.8, horns -44.6 / -46.6, clarinets -46.5 / -47.4. At 277-280: Flute 1 -38.8 and Oboe 1 -40.4 over violas -45.5 and clarinets -47+.
- **Tutti sfp, bar 301 (ONE_TIME note).** Each part's own drop from the sf to the p trough within 0.5-1.5 qn: Violins I about 14 dB, Oboe 1 10, Oboe 2 20, Clarinet 1 18, violas 23, celli 17. All are 10 dB or more.
- **Trio.**
  - Clarinet 1 -36.4 over the harp (-47.9) and the drone (Horn 4 -49.7, Horn 3 -53.5).
  - Celli -38.3 over the con sord. Violins II (-46.2).
  - Violins I (p) 4 dB over the celli (mp) at 177-184. The octave doubling leads, which is acceptable.
  - Oboe 1 -42.1 over the celli (-44.5) at 185-192.
  - At 209-216, Violas div. within 0.2 dB of the violas.
- **Codetta.** Oboe 1, Clarinet 1 and Bassoon 1 lead in turn (-39..-44) over violas, Violins II and the harp.
- **Tuttis 105-120 / 305-320.** Trumpets -36.8 / -38.2, 11-13 dB under Violins I and 3 dB under the horns: present, not on top. Timpani -40.7. Low brass -35.7..-39.3. Basses -42.5. 20-100 Hz share -20.2 / -18.9 dB (Dvořák -21.7): not boomy.
- **Timpani rolls.** Ranked 5th-20th in their bars, never the loudest stem.
- **Summit 336-339.** Violins I -20.7, Violins II -23.0, violas -24.6, woodwinds -27..-32, horns -31.4..-32.8, trumpets -34, trombones / tuba -35..-37, timpani -35.1. Horn 3's F sharp 4 is dropped as a unison with Horn 2, with the +3 dB `UNI_BOOST`. The master's loudest passage.
- **Solo 349-352.** Solo -36.1, Flute 1 -41.3, Violins II "la metà" -44.9.
- **Hn 1's motto 357-360.** -36.1, 9 dB over the violas.
- **Last G sharp, 372-376.** Horn 1 -46.1 against Violins I -46.8.

Do not touch: the c09 tutti violas +4 and flute / cor anglais f staccato roles; c08's Violins II trims and the celli roles at 624-672; the summit's string-over-woodwind-over-brass order with no brass accents and its `UNI_BOOST`; the subito and sfp CC11 drops (each part 10 dB or more at bar 301); the harp caps under the trio tune; the solo / flute / celli roles at 349-356; Horn 1's close role; the timpani roll trims and `TIMP_DAMP_AT`.
