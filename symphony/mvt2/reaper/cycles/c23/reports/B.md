# Critic B, cycle 23: balance and levels (render c22)

Method. I computed K-weighted (BS.1770) 10 ms frames and A-weighted 50 ms frames for every c22 stem and the master, and put them on score qn with the parts.json tempo map. I also took per-stem 30-120 / 120-250 / 250-2000 Hz band energies in 0.1 s frames, and narrow-band energies at each double-bass note's harmonics. Printed marks come from `build/mockup-events.tsv` and score pages 1-8. Control data comes from parts.json (`cc11`, `vol_db`, notes, hairpins), roles.json, mix.json and the trims files. Patch layer tables are read from the `.oib` files (`BS KS Master.oib`, `BC KS Master.oib`) with the same zlib load that `opus_state.load_oib` uses. I simulated each fix by applying its dB shape to the stem frames. Scripts are in `/private/tmp/claude-501/mockup-loop/c23-B/` (the c22-B set re-pointed at c22, plus `viol.py`, `swellscan.py`, `rise.py`, `simsw.py`, `sim78.py`, `mvc.py`, `lowpass.py`, `lowbar.py`, `f0.py`, `famacc.py`, `oib2.py`).

## Delivery, c22 (from metrics.md, measured)

| | Master | mp3 |
|---|---|---|
| Integrated | -22.5 LUFS | -19.8 LUFS |
| LRA | 23.6 LU | 16.0 LU (target 14-16) |
| True peak | -3.9 dBFS | -1.6 dBTP |
| p10-to-max short-term span | | 18.5 dB (target 16-19) |
| Limiter | | 1.8 dB |

None of the fixes below touches bars 61-62 or 79-80. Findings 1, 3 and 4 lower short bumps of 2-10 dB in pp/p passages. I infer that p10 moves by less than 0.2 dB, so all targets stay met.

## What holds (measured)

- **Same dynamic, same level in every family.** Accompaniment notes only (melody and countermelody lines excluded), median K by printed dynamic:
  - pp: winds -46.4, brass -47.4, strings -46.9.
  - p: winds -42.3, brass -39.9 (n=6), strings -43.8.
  - Each step pp -> p -> mp is 3-5 dB in every family.
- **Climaxes.** At bars 61-62 and 79-80 the melody group (Vln I, Fl, Ob, Vln II) leads every other stem by 2-12 dB K. Horns (f), trombones and tuba (mf), and the timpani stay 5-13 dB under it.
- **Tuba at bar 61.** It is K-loud (-24.9), but it puts only 2-10% of the 30-120 Hz energy into the master. The basses give 75-113%; the shares add to more than 100% because the stems partly cancel.
- **Bass balance overall.** The 20-100 Hz share is -17.1 dB. That lies between the Dvorak reference (-21.7) and the Brahms 1/ii and 4/ii references (-8.5 and -7.9), so the bass is not boomy overall.
  - The double basses' low band changes from note to note because the pitches differ. Ab1, the most frequent pitch, carries its energy at 104 Hz (H2); its fundamental is 18.5 dB under the note total, which is how real basses sound.
  - I found no pitch-specific boom worth an EQ change. The E flat 2 notches from c22 stay.
- **Solo margins.** The melody minus each single accompanying stem (A-weighted) is +4 to +13 dB in almost every soft solo: horn bars 7-14, oboe, solo violin, flute bars 37-40, CA, horn bars 67-70, clarinet bars 85-86.

## 1. Bassoons and bass clarinet: pp long notes swell 4-13 dB, because the swell crosses the patch's next dynamic layer. The swells reach the horn, oboe and bass clarinet solos (measured; layer cause read from the patch files)

**Where.** Every pp long note in Bassoon 1, Bassoon 2 and Bass clarinet whose CC11 swell starts at CC 40 or lower: 29 notes. The worst ones fall under solos:
- bar 3 (BCl, qn 6)
- bar 7 (BCl/Bn2, qn 18)
- bar 9 (Bn1 and BCl, qn 24)
- bar 10 (Bn2, qn 27)
- bar 31 (Bn2, qn 90)
- bar 37 (Bn1, qn 108)
- bar 45 (Bn2, qn 140)
- bar 69 (Bn2, qn 232)

**What.**
- Peak minus early body over these 29 notes: median **+4.1 dB**, max +12.1. For comparison, pp/p long notes without hairpins in other winds rise much less (`rise.py`): Cl1 +0.7, Fl1 +1.9, Cl2 +2.0, Hn3/Hn4 +1.4/+1.8, CA +2.5. The intended shape is SWELL_DB 1.5 plus +4 CC, about 2 dB.
- Bar 9, qn 24-26. Bn1 Ab3 rises from -48.7 to -41.7 K (CC 34 -> 37/38, vol_db +1.2) while the horn solo sits at -41.4..-41.7 on its low C-Bb-Ab. Bn1 is +0.7 K / -0.2 A against the horn at qn 25. The BCl Ab2 rises from -49.1 to -43.4 at the same time.
- Bar 45, qn 140-143. The c22 cap at CC 36 did not work. Bn2 B flat 2 still goes from -54.8 (CC 34) to **-41.8 at qn 141.75** (CC 36, vol +1.4). That is 13 dB, and it comes within 4.5 dB K of the oboe solo.
- Bar 10, qn 27-29: Bn2 -50.5 -> -42.1 (CC 36).
- Bar 69, qn 232-234: Bn2 Db3 -50.7 -> -41.9, 2.6 dB K under the horn solo.
- Bars 3 and 7 (BCl, qn 6 and 18): -49.9 -> -43.2, and +5.6. The pp chord under the first horn entry bulges every bar.

**Cause** (patch tables, read with `oib2.py`; the CC index is the table position).
- `BS KS Master`: there is no pp layer. "Bs mp" is 1.0 up to CC 40. "Bs f" fades in from 0 at CC 32 to 0.37 at 36 and 0.62 at 40.
- `BC KS Master`: "BC p" is at 1.0 up to 40. "BC mp" fades in from 0.23 at 32 to 0.51 at 36 and 0.64 at 40.
- So the printed pp (CC 34) sits exactly where the next layer enters. The +4 CC swell adds that louder layer instead of a small CC move.
- The c22 actor measured part of this already: a cap at 36 left "0.37 of the f layer".

**Fix** (`tools/score_to_parts.py`).
- Extend `SWELL_CC_CAP` to a track-wide form: a `"*"` key means "cap at the note's own starting CC while that CC is 40 or lower":
  `SWELL_CC_CAP = {"Bassoon 1": {"*": 0}, "Bassoon 2": {"*": 0, 46: 34}, "Bass clarinet": {"*": 0}}`
  The value 0 means "no CC rise"; you could also write the cap as start CC + 0.
- In the swell_caps code (near line 1549, `if n["pitch"] in swell_cap_tab`), accept `"*"`. When it matches, use the note's CC11 at its start as the ceiling.
- Keep `SWELL_DB` 1.5 dB for these notes, so they still breathe through the volume envelope.
- Check the Contrabassoon (qn 87: +3.4, CC 28-38) and Clarinet 2 (qn 238/244/286: +3.0..+4.4, CC 32-38) with the same reading of `CB KS Master` and `CL KS Master`. Add them only if their tables show the same crossfade.

**Predicted** (`simsw.py`: each note's 30-100% section capped at body + 2 dB). Accompaniment minus melody, worst 0.25 qn frame, K:
- Bar 9: Bn1 +0.7 -> -0.5. BCl -0.9 -> -3.5. The horn's low notes stay quiet; that is the shape of the phrase.
- Bar 45: Bn2 -4.5 -> **-10.0** under the oboe.
- Bars 31-33: Bn2 -1.8 -> -6.1 under the bass clarinet solo.
- Bar 69: Bn2 -2.6 -> -4.8. Bar 7: BCl -4.0 -> -7.0.

The pp pad keeps its level (body unchanged) and loses its periodic bulge.

## 2. Bar 78 (f, poco allargando): the bar 79 low-octave rows start a bar early, so the bass voices reach ff weight and the bassoon covers the violins on the downbeat (measured)

**Where.** qn 258-261.5. Rows in `build/roles.json` with `[258, 269, dB, 1]`:
- Bassoon 2 +3, Double basses +3, Contrabassoon +3, Bass trombone +3, Tuba +3
- Bass clarinet +2, Timpani +2, Violoncellos +1
- **Violins I -1**, Violins II -0.5

These rows come from c16 C #1, which proposed them for the ff tutti of bar 79. The score has the crescendo in bars 75-77, f at bar 78 and ff at bar 79 (p. 6-7).

**What.**
- Bar 77 crescendo, per 1.5 qn, from bar 75 to bar 78:
  - Vln I rises 8 dB (-35.1 -> -27.0 K).
  - Cb rises 12 dB (-43.1 -> -31.1). Inside its E flat 2 (qn 256) alone it rises 13.7 dB (-40.5 -> -26.8 at qn 258.75), with vol_db +2.9 -> +10.7.
  - Bn2 rises 20 dB from its pp (-49.2 -> -29.4).
- At qn 259.0 (bar 78 downbeat) Bn2 is **+0.4 K / +0.6 A over Vln I**. Over the bar it stays within 2-5 dB K.
- In bar 78 Bn2 (24.5 A) is 3 dB over the Fl1 melody doubling (21.6 A) and over Cl1 (23.2), although all of them are printed f.
- Rimsky-Korsakov places the weight of the low octave in the tutti. Bar 78 is the f bar before it, and the melody should still lead.

**Fix.** `build/roles.json`: change the start of these ten rows from 258 to **261.5**: `[261.5, 269, dB, 1]`. The default 0.5 qn ramp then finishes on the bar 79 downbeat.

**Predicted** (`sim78.py`). Bar 78, Bn2 minus Vln I:
- K: +0.4 / -3.3 / -4.6 / -2.8 / -2.1 -> **-3.6 / -7.3 / -8.6 / -6.8 / -5.5**.
- A: +0.6 -> -3.4.

The Cb goes 4 dB under its bar 78 level, and its bar 77 peak at qn 258.5-259 goes 2-4 dB lower. The sum of all stems in bar 78 falls 0.2 dB (-21.2 -> -21.4), so the step from bar 78 to bar 79 grows by 0.2 dB. Bar 79 itself does not change.

## 3. Theme A, bars 25-26 and 73-74: on the melody's low notes, the cantabile cellos come level with the two violin sections (measured)

**Where.** Violoncellos, qn 73.5-78 (bar 25 beat 3 to the end of bar 26) and qn 245.5-250 (bars 73-74). The violins are mp espr. in unison, the Vc p cantabile (p. 2 and 6).

**What.** Vc minus (Vln I + Vln II), per beat:

| qn | 74 | 75 | 76 | 77 | 246 | 247 | 248 | 249 |
|---|---|---|---|---|---|---|---|---|
| K | -1.5 | -1.5 | -3.1 | -3.0 | -0.9 | -2.6 | -3.4 | -2.0 |
| A | -1.9 | -1.9 | -3.5 | -5.1 | -2.2 | -3.6 | -4.6 | -4.4 |

- In the rest of the theme the gap is -4..-8 K and -7..-12 A.
- The melody falls from -33 K (bars 23-24) to -37..-38 on its low Ab4/Eb4/Fb4, while the Vc on its high C4/Bb3 holds.
- The violins are marked mp and the cellos p, so the violins should stay on top. In the hall the violins outnumber the celli about 3:1.

**Fix.** `build/roles.json` Violoncellos: add `[73.5, 78, -2]` and `[245.5, 250, -2]`. They add to the existing `[66, 78, -1]` and `[237.5, 250, -2.5, 0.5]`.

**Predicted:** Vc minus melody -1.5 -> -3.5 K and -1.9 -> -3.9 A at the worst beats. The countermelody is still 4-5 dB over the violas and basses.

## 4. Coda bar 87: the Cl1 melody's D flat 5 sags 6 dB in its second half, and the muted horns and violas reach its level (measured; cause partly inferred)

**Where.** Clarinet 1, qn 287.5-289 (bar 87 beat 3; the note starts at 286). Accompaniment: Horn 4 and Violas (pp), Hn 3-4 con sord.

**What.**
- Cl1 goes -40.3 K (qn 287) -> -41.8 -> -43.8 -> **-46.4** (qn 288.5). In the same frames CC11 falls 40 -> 37 and vol_db +4.8 -> +3.5. That is the swell contour's fall plus the sample's decay.
- Horn 4 minus Cl1 at 288.0/288.5: 0.0/+0.2 K, -1.5/-0.3 A. Violas: -2.8/+0.5 K, -5.7/-1.1 A.
- Over the rest of bars 87-88 the clarinet leads each stem by 4-8 dB.

**Fix.** `build/roles.json` Clarinet 1: add `[287.4, 289.0, 2.5]`. It adds to `[280, 292, 3]`, with the default ramps.

**Predicted** (inferred from the stem levels): Cl1 at qn 288-289 is 2.5 dB higher. Horn 4 and Violas are -2.3..-2.5 K under it at the worst frame instead of level. Bar 88's own entry (qn 289) does not change.

## 5. Smaller items, measured, for the actor's judgement

- **Bars 15 and 19, oboe entries.**
  - The first 0.3-0.4 qn of the oboe's entry note (qn 42.0-42.4 and 54.0-54.4) is under the pp con sord. strings: Vln II +4.2 K / +2.2 A at qn 54.0. The pp strings then swell under the oboe's first beat (Violas qn 42 +10.3, Vc +4.7, Vln II +4.6 rise).
  - note_trims already give the oboe +6/+5, but they ramp in over 0.6 s. A shorter ramp for these two onsets would let the solo speak first. This belongs to critic A's attack area, so I leave it to them.
- **Contrabassoon and Clarinet 2.** These are the swell checks named in finding 1. Do not change them until the patch tables are read.

## Do not touch

- The CC11 dynamic map and the family soft trims (pp/p/mp consistent across families).
- The climax balance at bars 61-62 and 79-81. The tuba's +5 at bar 61 adds weight in 120-500 Hz, not boom.
- The c22 Cb E flat 2 and Vc bar 60 notches, `HP_GAIN_SOFT_ACC_DB`, and the morendo rows.
- Harp `[238, 262, 4]`.
- The Cb EQ chain (low band between the Dvorak and Brahms references).
- `deliver_master.py` and the `_all` soft lifts.
