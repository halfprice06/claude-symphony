# Cycle 08, critic B (balance and levels), on the c07 render

Method. I computed K-weighted levels (BS.1770 weighting applied in the frequency domain, 2048-point frames) per bar for every stem and the master of `cycles/c07/render/`, on the c07 tempo map (`cycles/c07/build_render/parts.json`), plus band energies per bar (20-100, 100-250, 250-500, 500-2k, 2-6k, 6-20k Hz). Levels below are K-weighted dB on one common scale, energy-averaged over the bars named. They are comparable with each other, not with LUFS. For c05 against c07 I used the two masters (only c05's master survives). Score marks come from `build/mockup-events.tsv` and the score pages. Bar b starts at qn 3(b-1).

## Manual notes (cycle 8, slot B: group B2, May 2021 HO manual PDF pages 194-200, read in full; MANUAL-GAPS.md read)

| Manual (PDF page) | Where it applies here | Render follows it? |
|---|---|---|
| p.194, 196: every loaded instrument has a master channel and sub-mixer channels, one per mic position, each with its own volume, pan and load button | `mix.json` `mic_db` per track (template levels: string Close -4.5 under Main, woodwinds Close-led, timpani Close -8.4 / Main -6.9 / **Surround 0.0**) | Yes. The timpani's Surround mic at 0 dB, with the 84 Hz bell, is part of finding 1 |
| p.195: Store Mix / Restore Mix saves every channel's settings by name | none (the pipeline writes each Opus state from `mix.json`) | Not needed; the script is the stored mix |
| p.196, 198: an FX bus inside Opus, fed by Effects Send inserts on the sub-mixer channels; a POST switch sets pre- or post-fader; "for reverb, post fader is typically used" | `opus_reverb_off` and the four REAPER Spaces II returns with post-fader sends (c06/c07) | Yes, the same routing outside Opus, post-fader. A result: a role or trim in the volume envelope also changes that track's hall send (LEARNINGS c06), so every role below moves dry and wet together |
| p.198-200: insert EQs (Bass Comp 32-256 Hz; Channel Equalizer, 3 bands; Equalizer, 6 bands, 30 Hz-18 kHz, -60..+24 dB) | the family EQs and per-track bands are REAPER ReaEQ after Opus, not Opus inserts | Yes in function. No Opus insert EQ is needed for the fixes below; ReaEQ already covers the 84 Hz bell (finding 1) and the string shelves (finding 5) |
| MANUAL-GAPS #6 (p.123-126): hard-stick timpani for bars 1-340 | the tutti strokes of finding 1 play the felt Flt KS | No (still open). Hard sticks would give the printed colour, with more attack and less low ring (inferred) |

## Is c07 too dry or thin in my area? (measured)

No. The master's band shares from c05 to c07, by passage (20-100 / 100-250 / 250-500 / 500-2k / 2-6k / 6-20k Hz, dB of the passage total):
- 105-120 tutti: c05 -23.1 / -8.4 / -6.7 / -2.6 / -10.8 / -31.1, c07 **-17.4** / -8.0 / -6.9 / -2.9 / -9.7 / **-26.7**
- 153-168 trio clarinet: c05 -18.8 / -8.8 / -4.6 / -3.2 / -14.7 / -50.0, c07 -18.3 / -9.8 / -5.3 / -2.7 / -13.3 / -42.3
- 349-356 solo: c05 -17.6 / -9.3 / -11.2 / -1.9 / -8.7 / -24.9, c07 -17.1 / -10.2 / -12.0 / -2.5 / -6.1 / **-19.5**
- 364-376 close: c05 -22.9 / -16.2 / -7.2 / -1.6 / -10.8 / -36.7, c07 **-16.3** / -15.6 / -7.5 / -2.2 / -7.9 / -31.0

The body bands (100-500 Hz) moved by less than 1 dB in every passage. What changed is the two ends: more sub-bass in the tuttis and the close (finding 1) and 4-8 dB more 6-20 kHz everywhere (finding 5). The sub. p's keep their hall (S3): the R Strings return falls 8.4 dB from bar 120 to 121 while the master falls 10.2 dB, and 4.0 dB against 3.9 at 276-277. I did not re-measure loop pulsing or repeat dips (other lenses).

## Findings, ranked by what a listener would hear

### 1. In the theme tuttis the timpani supply three quarters of the master's sub-bass: the tutti is 5.7 dB heavier below 100 Hz than in c05. The trio's two f strokes are as loud as the rest of the orchestra (measured)

**Where.** Bars 105-120 (qn 312-360) and 305-320 (qn 912-960), timpani motive x strokes (f, velocity 94-97, Timpani Flt KS Lng). Bars 200 and 209 (qn 597, 624): single f strokes in the trio.

**Measured.**
- Timpani share of the master's 40-100 Hz energy: **75 %** at 105-120, **70 %** at 305-320, 20 % at the summit 333-338, 3 % at 45-56. Over the loudest 10 % of all frames: 48 %.
- Master 40-100 Hz against 250 Hz-2 kHz, loud frames: c07 -16.0 dB (105-120), -15.5 (305-320), -17.0 (loudest 10 % of the piece). The Dvořák 9/i reference reads -22.8 on its loudest 10 %. It is a lossy MP3 (BRIEF), so I use it for direction only. The c05-to-c07 change (above: 20-100 Hz share -23.1 -> -17.4 dB at 105-120, -22.9 -> -16.3 at the close) is the safer number.
- Broadband, the drum does not cover the theme in the tuttis: in the first 0.25 s of each stroke the timpani stem is 9-12.6 dB (RMS) under the rest of the master. The excess is all below 100 Hz. That points at the EQ and mic, not the level.
- The trio strokes are a separate problem. At qn 597 (bar 200, f staccato, v94) the timpani's first 0.25 s is -28.8 dB against -27.1 for everything else (-1.6 dB). At qn 624 (bar 209, the roll's f end, v97) it is -31.8 against -32.6 (+0.7). The tutti strokes at the same velocities sit 10-12 dB under the rest. Each of these two notes is the loudest stem of its bar (K-weighted bar means: bar 200 timpani -30.9 against Clarinet 1 -31.3 and violas -31.8; bar 209 -33.6, level with Violins I -31.6 and the celli -33.6).
- Cause (read): since c06 the timpani carry the template's Surround mic at 0 dB and its 84 Hz bell (+8.58, halved in c07 to +4.3 dB, 1.39 oct). Both feed the felt drum's E2/B1 ring.

**Simulated on the c07 stems** (timpani stem re-weighted, master = old master + change):

| change | 105-120: 40-100 re 250-2k / timp share | 305-320 | timpani K level 105-120 |
|---|---|---|---|
| c07 | -16.0 dB / 75 % | -15.5 / 70 % | 0 |
| 84 Hz bell +4.3 -> 0 | -18.7 / 54 % | -18.0 / 48 % | -1.8 dB |
| bell 0 and timpani -3 dB | -20.1 / 37 % | -19.1 / 31 % | -4.8 dB |

**Fix.**
1. `build/mix.json` `family_eqs.timpani`: the 84.43 Hz bell from +4.3 to 0 dB (or delete the band). It is a mix-only change, and the summit (333-338, timpani share 20 -> 9 %) keeps its weight from the strings and basses. This is the measured case against the template item.
2. `build/roles.json` "Timpani": add `[596.9, 597.6, -5]` and `[623.9, 624.6, -4]`, as steps on the attack (kit LEARNINGS section 13: struck-note trims as steps). Target: each stroke 4-6 dB under the rest of the orchestra in its first 0.25 s, about where the tutti strokes sit after the bell change. A velocity cap of 80 on those two notes (`VEL_CAP_SPANS`) would do the same through the layer.
3. Not now: the Surround mic. Re-measure after 1 and 2 and lower it only if the 105-120 share is still over 50 %.
4. Hard sticks (MANUAL-GAPS #6) remain the score's colour for every stroke to bar 340 (inferred: less low ring, more attack).

### 2. Violins II sit 4-7.5 dB under Violins I wherever both play espress. lines at the same printed dynamic. In the trio's f statement they fall under the mf celli (measured)

**Measured** (K-weighted, Violins I / Violins II / gap):
- 45-46 mf espress.: -28.1 / -31.4 / 3.3; 47-48: -30.8 / -37.3 / 6.5; 51-52: -23.8 / -30.8 / 7.0
- 121-124 sub. p espress. (both): -33.3 / -40.8 / **7.5**; 125-128: -29.8 / -35.2 / 5.4
- 209-212 f espress. (both, the tune T with Clarinet 1): -30.4 / -36.3 / 5.9; 213-216: -30.1 / -36.7 / 6.6. Celli (mf) -34.9 / -33.3: **1.4-3.4 dB over Violins II**; Bassoon 2 (mf) -35.8 at 209-212, level with them
- 217-220 ff: -24.6 / -31.1 / 6.5
- 281-284 p espress.: -31.1 / -35.4 / 4.3
- Against this, 105-111 ff unison: -22.4 / -24.0 and -24.0 / -24.1, a 0-1.6 dB gap. So the samples and gains match at ff and the gap opens at p-f.
- Cause (read, `build/mix.json`): Violins I soft trims p +3, mf +1, ff dyn +1.5; Violins II p 0, mf -0.8, f -1, ff +1. Net V2 - V1 from the trims: p -3, mf -1.8, f -1, ff -0.5 dB. The metrics table shows the same slope in plain RMS (gap p 4.4, mp 4.6, mf 4.9, f 6.7, ff 1.3 dB).
- Norm (inferred): HO records 16 first and 11 second violins, so equal dynamics would give about 1-2 dB less on the seconds, not 4-7. Rimsky-Korsakov (rimsky-principles p.77, "Comparison of resonance") treats equal sections at an equal dynamic as equal. The trio statement is printed f espress. for both sections over mf celli, violas, bassoons and basses.

**Judgement (inferred).** The second violins' counter-lines (the second idea, both sub. p entries, the trio's ff T) are heard as background, and at 209-216 the celli's mf counter-melody comes through ahead of them.

**Fix.**
- `build/mix.json` "Violins II": `soft_trim_db` p 0 -> +2, mf -0.8 -> +1.2; `dyn_trim_db` f -1 -> +1 (ff +1 unchanged). Expected gap at p-f: about 3-4 dB, leaving Violins I on top.
- `build/roles.json` "Violins II": add `[624, 660, 2]` (bars 209-220). "Violoncellos": replace `[624, 672, -1]` with `[624, 648, -3]` and `[648, 672, -1]`. Target at 209-216: Violins II 2-3 dB over the celli.
- Check after: the accompaniment spans where a +2 dB rise must not lift Violins II into the foreground. At 13-28 (p staccato chords) they sit at -50..-52, under the violas at -47 and Violins I at -36. At 169-196 (con sord., existing role +4) they sit 9 dB under the celli's tune. At 349-356 ("la metà") they sit 11 dB under the solo. All keep their place after +2.

### 3. Counterstatement crescendo, bars 37-40: Clarinet 1's held B4 is the loudest stem, 4-6 dB over the melody, because of a +4.5 dB pitch trim (measured)

**Score.** qn 108-120: every part crescendos to f at bar 41. Flute 1, Oboe 1 and Violins I carry the theme (from p). Clarinets 1-2 hold a pp chord (Cl 1 B4 for 8.8 qn, Cl 2 G4).

**Measured.** Bars 37-38 / 39-40: **Clarinet 1 -33.0 / -31.8**, Clarinet 2 -38.3 / -35.3, Flute 1 -38.8 / -39.5, Oboe 1 -39.3 / -35.8, Violins I -36.8 / -33.7. The clarinets share one chord, dynamic and CC1/CC11 curve, yet Clarinet 1 is 4.4-5.3 dB over Clarinet 2. parts.json shows its volume envelope at +4.7..+7.4 dB through 108-117 against +0.3..+2.8 on Clarinet 2. The difference is `build/pitch_trims.json` "Clarinet 1" `"71": 4.5` (the c06 B4 trim, fitted on soft legato notes) applied to this held accompaniment note. No role covers 108-120 (the c01-c07 rows stop at 108). This is the case kit LEARNINGS section 13 warns about: a pitch trim set at one dynamic or texture can be wrong inside a chord.

**Fix.** `build/pitch_trims.json` "Clarinet 1": add `"_skip_onsets": [108.0]` (read by score_to_parts.py line 4655). Expected: Clarinet 1 about -37.5 / -36.3, 1-3 dB under the melody and level with Clarinet 2. Fallback: `build/roles.json` "Clarinet 1" `[108, 117, -5]`, released over the arrival at 120. Also list the other onsets where this B4 is a held chord tone rather than a tune note before the next refit.

### 4. Tutti 101-120: Trumpet 2 plays 5 dB under Trumpet 1 on the same quarters, and the trumpet pair sits under every single woodwind (measured; norm inferred)

**Score.** Trumpets 1-2 share one staff and one rhythm, f repeated quarters and eighths (bars 101-120, qn 300-360; there are no trumpets or trombones in the reprise tutti 305-320, page 11, so BRIEF's "301-320" does not apply). Woodwinds and strings play ff, trombones and tuba f tenuto strokes.

**Measured.** Trumpet 1 / Trumpet 2: 105-108 -34.6 / -39.1, 109-112 -34.7 / -40.1, 113-116 -34.2 / -39.4, 117-120 -33.9 / -36.7; the coda 333-335 -31.2 / -36.7 (equal at 336-338). Cause (read): Trumpet 1 plays its staccatos on "StacSs DblTng RRx9" (56 notes) and Trumpet 2 on "Sus Non Vib MAX" slices (63 notes, v87). c04 measured StacSs at about the level of the slice at v96, so the 5 dB comes from the slice's slow front at quarter 264. Against the texture: Violins I -22.4..-24.0, Oboe 1 -30.4..-32.1, Clarinet 2 -27.3..-29.9, Trombone 1 -36.8..-38.0, Tuba -35.8..-37.6, **Contrabassoon -31.8..-35.5** (ff). Rimsky-Korsakov (p.77) gives trumpet = trombone = tuba = 2 horns = 4 woodwinds. Here the trumpets sit 4-10 dB under one woodwind, the trombones and tuba 5-8 dB under, and the contrabassoon 3-5 dB over the tuba.

**Judgement (inferred).** "Present but not on top" is met for Trumpet 1. Trumpet 2 is barely there, so the repeated quarters sound like one trumpet. The brass bass (trombone and tuba strokes) is weaker than the contrabassoon, which reverses the orchestral order. Dan's rule that low brass must not cover the theme leaves room for 2-3 dB here: the trombones are 13-15 dB under Violins I.

**Fix.**
- `build/roles.json` "Trumpet 2": `[[300, 360, 4], [984, 1005, 4]]` (ramp in over the pp start at 300). Target: within 1.5 dB of Trumpet 1. The StacSs row stays the better fix when memory allows (MANUAL-GAPS #17).
- `build/roles.json` "Contrabassoon": add `[309, 360, -3]` (it already has `[996, 1017, -3]`). It would then sit about level with the tuba. Optionally Trombones 1-2, bass trombone and tuba `[309, 360, 2]`, leaving them 11-13 dB under Violins I.

### 5. Brightness (scheduled in ONE_TIME_c08 item 1): Violins I carry 55-86 % of the 6-20 kHz band in my passages. Movement I's values reach the target, but they cost the violins 0.9 dB of loudness (measured; simulated on the c07 stems)

**Measured.** Share of the master's 6-20 kHz energy: Violins I 55 % and Violins II 29 % at 105-120, 66 % / 27 % at 333-338, 77 % at 45-56, 86 % at 209-224. The brass carry about 1 % (Movement I had 35 %). The solo (349-356) gained 5.4 dB of 6-20 kHz share and 2.6 dB of 2-6 kHz from c05 to c07.

**Simulated** (strings family 4.73 kHz +4 dB shelf removed on all string tracks, Violins I 5 kHz shelf -4 -> -6, Violins II new 5 kHz -4): master 6-20 kHz share -24.8 -> **-28.8 dB** (target -28 or lower; references -28.8..-32.2), 2-6 kHz -8.9 -> -9.7 (references -10.5..-12.4). K-weighted loudness change per stem: **Violins I -0.85, Violins II -0.90**, violas -0.08, celli and basses 0.0, solo -0.45, Violas div -0.04 dB.

**How to tune it.**
- Apply Movement I's values as scheduled. Give the two violin sections their loss back in `gain_db` (Violins I 6.2 -> 7.05, Violins II 7.66 -> 8.55, on top of finding 2's trims), as c06 did for the family EQs. Otherwise the theme's margin over the woodwinds (Violins I over Flute 1 at 105-120: +3.4 dB) shrinks by about 1 dB.
- Keep the Violin I solo's own 2.5 kHz -5.5 shelf. It was matched to the section with both carrying the family shelf. After the change the section loses 2 dB more at 5 kHz than the solo, so measure the solo's 2-8 kHz re 0.5-2 kHz tilt against Violins I at 345-348/364-367 and lower the solo shelf to about -6.5 only if it reads more than 1.5 dB brighter.
- Do not take treble from the woodwinds or brass for this: they do not carry the band.

### 6. The close: Horn 1's pp at bars 368-372 (qn 1101-1116) is 7-8 dB louder than its own pp at 361-363, so the master rises 5.7 dB into a pp/ppp ending (measured; judgement inferred)

**Score.** Hn 1 pp at 1080 (bar 361) and again at 1101 (bar 368), ppp at 1122 (bar 375); Violins I ppp "tutti, change bow freely" from 1089; rit. 370-375.

**Measured.** Horn 1: 361-363 -44.9, 364-367 -47.4, **368-371 -37.0**, 372-375 -39.4, 376 -42.3. Violins I ppp -43.9..-45.2. Master: 364-367 -41.6, **368-371 -35.9**, 372-375 -37.8, a louder bar range than the Meno mosso's pp opening (341-344 -35.7). Cause: `build/roles.json` "Horn 1" `[1100.25, 1128, 10]` (c06 C #2).

**Judgement (inferred).** The pivot G sharp should be heard over the ppp violins, but a 10 dB lift makes the horn's second pp a step up in the last ten bars of a movement that is printed to fade.

**Fix.** `build/roles.json` "Horn 1": `[1100.25, 1128, 10]` -> `[1100.25, 1128, 6]`. Expected: Horn 1 about -41 at 368-371, 3-4 dB over Violins I and 4 dB over its pp at 361-363; the master at 368-371 about 2-3 dB over 364-367 instead of 5.7.

## Measured and in balance (for the record)

- Theme A 13-28: Violins I 11-14 dB over the pizz. basses and celli and 17-27 dB over the timpani.
- Trio: Clarinet 1 8-12 dB over the harp and 12-16 over the drone (153-168). The celli's T 9 dB over the con sord. Violins II (169-176). Violins I 2.5 dB over the celli an octave below (177-184). Oboe 1 10 dB over the harp (185-188).
- Codetta: Oboe 1 / Clarinet 1 / Bassoon 1 at -35.0 / -36.3 / -35.8.
- Solo 349-352: 6 dB over Flute 1 and 11 over Violins II "la metà".
- Hn 1 motto 357-360: 8.8 dB over the violas.
- Summit 336-338: Violins I -16.4 over horns -28.6..-29.7, trumpets -31.5, trombones and tuba -30.8..-34.1, timpani -28.8.
- Violas div against violas: within -2.3..+1.2 dB at 209-220.

Do not touch: the c07 subito roles (Violins I 6.7-6.9 dB over the clarinets at 121), the harp caps under the trio tunes, the solo / flute / celli roles at 349-356, the Violas div gain and width, the trio horn roles, the returns and sends as built in c07 (the body bands did not thin), and the summit's string-over-brass order with no brass accents.
