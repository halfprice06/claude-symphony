# Cycle 26, critic C: dynamics over time (lens C2), on the c25 render and its delivered mp3

Sources: `cycles/c25/render/` (master, 31 stems, returns), `cycles/c25/scherzo-mockup-c25.mp3` (second delivery), `cycles/c25/build_render/` (parts.json, roles.json, mix.json as rendered), c18 stems and parts.json for comparison (c24's stems are deleted), the c19-c24 `build_render/parts.json` files, `build/mockup-events.tsv`, `build/score_config.py`, `tools/score_to_parts.py` (read only), `tools/deliver_master.py`.

Method:
- Loudness is EBU momentary (M, 0.4 s) and short-term (S, 3 s) from ffmpeg ebur128, centred, on the parts.json tempo map. The mp3 and the master line up at lag 0.
- "Mean" is the energy mean of M over a span. Stem and family levels are plain RMS dB, in 25 ms frames summed over the window.
- I ran the delivery simulations with `tools/deliver_master.py`, unchanged, on the c25 master, using a scratch copy of parts.json with extra `ride_trims`. The baseline run reproduces the delivered file exactly: -14.0 LUFS, LRA 10.5, p10 -20.3, limiter 3.7 dB.
- "Measured" means a number from the render, the data or a simulation. "Inferred" means reasoned, not tested.

## Manual notes

MANUAL-READING.md has no row for cycle 26 ("cycles after c20 pick their own pages"). I read group D1 (p.53-54, p.63-64) because it covers this lens, and p.91-92 (the Marcato Sustain text) for finding 1. I used MANUAL-GAPS.md for the rest.

| reading (PDF page) | where it applies here | does the render follow it? |
|---|---|---|
| p.53: note velocity sets loudness on short articulations and cannot change mid-note; CCs shape sustained notes | the fff summit strokes at 1005 (strings Sus MAX v112) | Partly. On the KS Master sustain rows, velocity does nothing (DIGEST, measured M1 c06). The summit's v112 cannot give the attack weight, and CC11 already starts at 119. Finding 1 (measured). |
| p.63-64: CC7 sets an instrument's level against the others; CC11 shapes its dynamics over time | c25's trims in a CC7 lane | Yes. Hairpin depths per family are unchanged from c18 (below), so the move to CC7 did not flatten shapes. The exception is finding 3, which comes from a hold rule, not from CC7 (measured). |
| p.91-92: Marcato Sustain plays a marcato sample with the looped sustains for "extra power at the start of the note" | the fff downbeat at 1005 in Violins I/II, violas, celli (all have a "Sus Marc LITE" row; Violins I's row is loaded and used at the sf of 900) | Not used at 1005. Finding 1 (problem measured, gain inferred). |
| MANUAL-GAPS #7, recorded crescendo rolls (p.123, 125) | rolls 101-103, 205-208, 301-303 | Not needed (measured). The CC1 rolls grow +11.6 (300-309), +15.0 (612-624) and +12.6 dB (906-910) and stay 7.5-11 dB under the master at their tops. |
| MANUAL-GAPS #4, brass and clarinet dynamics on CC1 (p.101) | brass into 996 / 1005 | In use. Brass is 3 dB lower at the summit downbeat than over the beat before (finding 1). The cause is the c25 removal of brass arrival weight, which is intended (printed f/ff). |

## Checks the cycle note asked for (measured)

**Hairpins per family, now that trims move in CC7 on moved time.**
- Method: stem level over the first quarter of each hairpin of 2 qn or more (at most 1.5 qn) against its last quarter. Harp and timpani are left out.

| | c25: crescendos median / under +1 dB | c18: crescendos | c25: decrescendos median / not falling 1 dB | c18: decrescendos |
|---|---|---|---|---|
| winds | +5.3 / 31 of 122 | +5.5 / 32 | -5.6 / 11 of 67 | -6.1 / 9 |
| brass | +8.2 / 3 of 43 | +8.3 / 3 | -4.5 / 6 of 32 | -3.8 / 7 |
| strings | +5.8 / 16 of 94 | +5.5 / 14 | -4.0 / 16 of 52 | -4.1 / 12 |

- The CC7 move kept the shapes. 22 hairpins improved by more than 2.5 dB against c18 and 23 got worse.
- The worse ones are dominated by one c25 rule (finding 3) and by two older faults (finding 5).
- The "crescendos" at 900 that read as falling are the sfp's sf in the first window (finding 2).

**The summit's 0.56 LU lead.**
- mp3 M max: 336 -7.18; 335 -7.49; 337 -7.53; 338 -7.56; 339 -8.17; next 110 -8.29, 300 -8.33, 104 -8.44.
- Spec item 2 holds. The lead over 335 rests on its last beat, which is in effect the summit's own onset: see finding 1.
- f to ff on the mp3 (passage means):
  - f: 41-44 -11.7, 128-131 -10.8, 197-200 -12.1, 273-276 -11.7, 284-287 -11.1;
  - ff: 53-55 -10.2, 72 -9.4, 105-120 -9.8, 304 -8.9, 305-320 -10.1, 333-335 -9.3.

**Quiet passages (Dan's AirPods note).**
- mp3 means: ppp intro bars 1-2 -17.7; horn call 3-6 -14.3; timpani 9-12 -21.7; theme A 13-28 -16.7; counterstatement -18.3; fugato -20.0 / -19.8; F major pp -17.6; ritmo -19.9; link ppp -17.7; trio dolce -15.9; codetta -17.2; reprise -15.9; stretto pp -21.2; Meno pp -19.2; solo -15.6; close ppp -19.0.
- S p10 is -20.3, 2.7 LU above the spec floor of -23. Nothing is buried. The cost is order: finding 4.

**LRA.** Master 22.1, mp3 10.5: exactly at the spec floor (finding 4).

**S3 at both sub. p's.**
- 360: R Strings falls -35.1 / -41.5 / -46.9 / -48.0 / -50.1 / -51.1 dB at -0.6 / -0.3 / -0.05 / +0.05 / +0.1 / +0.2 s, with no step. f 105-120 to sub. p 121-127 is -11.8 dB on the master and -6.1 LU on the mp3.
- 828: smooth too. 273-276 to 277-283 is -5.4 dB on the master and -3.5 LU on the mp3; the tutti before it ends in a rest.
- Both keep the hall.

**G.P. (bar 340).**
- Master falls from -16.6 (-0.6 s) to -36.4 at the cut-off, then -50.0 at +0.3 s and -69 at +0.8 s.
- R Strings: -40 -> -51 -> -60 -> -74 dB. The hall rings into the silence and is gone before 341.

**Timpani rolls.**
- Growth only under the printed crescendos (above).
- 129-130 and 285-286 start at -38.7 / -38.9 and settle to -44 / -45 under the texture.
- Open: the 237-240 roll (finding 5).

**Loop pulsing** (100-300 Hz band and spectral centroid, autocorrelation at 3.95 s after a 2 s detrend):
- Violins I G sharp 364-376 +0.18 / +0.10; bars 1-8 +0.02 / -0.18; Horn 1's last G sharp -0.03 / +0.20; the master over 1110-1128 -0.10 / -0.18.
- Nothing pulses audibly. The other held notes are shorter than two loop periods at these tempos.

**Arc against the print.**
- In order everywhere except findings 1-4.
- Trio: 197 is printed f in eight parts, but 209 is f only in the violins (Clarinet 1, violas and celli mf), and ff comes at 653. So the master's 209-217 (-25.5) under 197-200 (-23.9) follows the print, and the A6 bars 218-220 are the trio's loudest (-20.5).
- Codetta fade, accelerando growth (249 -> 252 +7.9 dB), held-chord fade 361-364 (-36.5 / -39.1 / -43.7 / -44.6) and the ppp close are all in order.

## Findings, ranked by what a listener would gain

### 1. The fff summit (bar 336, qn 1005) has no arrival. The downbeat lands at the crescendo's level, the extra fff energy blooms 0.3-0.5 s later, and the delivery takes the bloom away. On the mp3, bar 336's downbeat is 0.1 LU over the last beat of 335 (measured; fix partly inferred)

**Where.** qn 1003.5-1008, all families; Violins I, Violins II and violas above all.

**Master, 0.25 qn windows (measured).**
- The master goes -16.6 (1004.5), -17.2, **-16.7 (1005.0)**, -15.4, -15.2, -15.0, -14.2, -13.1, **-12.6 (1006.5)**, -11.8 (1007.0).
- Over the first 0.5 qn (0.1 s) after the fff the master is +0.9 dB over the beat before. The peak comes 0.35-0.45 s later, +4.4 dB higher.
- Families, 1002-1005 against the first 0.5 qn after 1005:
  - strings: Violins I +4.5, Violins II +9.0 (both bloom a further +3.7 / +1.0 dB over the bar); celli +0.6; basses -0.5;
  - winds: Flute 1 (the top fff voice) -0.8; cor anglais -1.2;
  - brass: -1 to -5.6 (horns and trombones lost their arrival weight in c25, as intended);
  - timpani: +2.4.
- Violins I's fff note (Sus MAX, v112, CC11 119 falling to 107) reads -29.3 over its first 0.25 qn, then -23.5, then -19.2 at 1006.5 (c18: -32.5 / -27.1 / -23.0, the same shape). The sample swells for 0.4 s after the attack.
- The pre-limiter peak of the delivery at 240.93 s (qn 1006.6) is Violins I at -6.2 dBFS inside that swell.
- Velocity cannot fix this on a KS Master sustain row (DIGEST, p.101-102; measured in M1 c06).

**mp3 (measured).**
- RMS per 0.5 qn: 1003.5 -12.8, 1004.0 -12.8, 1004.5 -12.7, **1005.0 -12.1**, 1005.5 -13.0, 1006.0 -13.1, 1006.5 -13.4, 1007.0 -11.4.
- The delivery's gain falls from +3.9 dB at the downbeat to -0.4 dB at 1006.5: the peak compressor, top ride and limiter take the bloom.
- M max: 335's third beat -7.49 against 336's first beat -7.37.

**What the delivery cannot do (simulated).**
- Ending the 990-1005.1 ride row (-4.5 dB) at 1004.85 instead of 1004.6 changes nothing: summit lead and beat levels are identical to 0.03 LU, because the ride is smoothed.
- A -3 dB dip on the master over 1005.4-1007.55 (a stand-in for flattening the bloom) lowers the limiter from 3.7 to 3.2 dB, but the downbeat is still -12.1 and the lead is unchanged.
- So the step has to be in the master's first 0.1 s.

**Fix (instrument side; range-test first).**
- `build/score_config.py` `ART_SPANS`: play the 1005 stroke on the loaded "Sus Marc LITE" row, the row the sf of 900 uses for Violins I (line 622 pattern). The row adds a marcato sample to the sustain for "extra power at the start of the note" (manual p.91-92).
  - Violins I: `{"from": 1004.9, "to": 1005.1, "art": "Sus Marc LITE", ...}` with the f-layer velocity the 900 span uses.
  - Violins II and violas: the same, but only after a range test. c22 rejected their Marc rows at the hemiola. The finale's technique 140 (Violins II "Sus Marc LITE" at v92, lead 0.085 s, CC11 ff step 0.06 s before the moved note-on) is the recipe to copy.
  - Celli: optional. They are not the bloom.
- `CC11_ADD_SPANS`, Violins I / Violins II / violas: a counter-shape on the held fff notes, so that the level holds instead of swelling (the c24 celli 516 / 526 mechanism, a shape on the instrument, not a fader move): (1005.35, 1006.0, 0, -10), (1006.0, 1007.3, -10, -10), (1007.3, 1007.5, -10, 0).
- Targets on the next render:
  - master over the first 0.5 qn after 1005 at least +3 dB over 1004.0-1005.0 (now +0.9);
  - the master's peak in 1005-1008 within 0.15 s of the onset (now +0.4 s);
  - on the mp3, the first beat of 336 at least 1.0 LU over 335's third beat (now 0.1), and the limiter at the summit 3.7 dB or less.
- Do not raise brass at the summit; it is printed f/ff.

### 2. The tutti sfp < at bar 301 (qn 900) is heard as a one-beat hiccup. The p lasts about 1 qn, the crescendo is finished by bar 302, the accents at 902 put the strings back at f at once, and on the mp3 the dip is 2.5 LU deep (measured)

**Where.** qn 900-912: woodwinds and strings with an sfp, horns p, cresc to ff at 909-910.

**Master and mp3, M max per qn (measured).**
- ff 897 -13.4; sf 900 -15.7; 901 -18.3; **902 -21.6**; 903 -19.8; 904 -18.5; 905 -17.7; ...; 909 -14.9; 910 -13.6.
- The p trough is 5.9 dB under the sf and 8.2 dB under the ff before it.
- On the mp3 the same run reads -9.5 / -10.9 / **-12.0** / -10.9 / -10.1: a 2.5 LU dip. The delivery gain rises from +6.2 at the sf to +9.7 dB at the trough.
- The ride row [(895.5, 0), (896.5, -2), (900, -2), (901, 0)] lowers the ff and the sf by 2 dB and releases into the p. It works against the sfp.

**Causes in the data (measured, parts.json).**
- `dyn_curve` falls from 114 to 46 by 900.9 (FP_SPIKE ("f", 0.45, 0.9)), then climbs on the default `HP_CURVE` "cresc" (0.4, 0.7): 55 at 901.5, 63 at 902, 78 at 903, **94 at 904**, 100 at 906, 114 at 910.
- 70% of the rise is done at bar 302 beat 2. The 9-10 qn sfp hairpins were left out of `cresc_long` on purpose in c10 (comment at line 727).
- `ACCENT_CC_AT` (22, 0.5) at 902 on Violins II, violas and celli puts CC11 at 87-97 on the first accented note after the sfp.
- Stems from 901.5 to 902.25: celli -41.9 -> -31.2 (+10.7 dB), Violins I -44.0 -> -34.9 (+9.1), Flute 1 -37.3 -> -31.4 (+5.9). That is three to five times Dan's accent target of +1 to +2 dB, on a note whose printed level is p in a crescendo.
- The celli are at -31.7 at 902.5, above their own printed-f median (-39.8).

**Fix.**
- `tools/score_to_parts.py` / `build/score_config.py`:
  - a generic `HP_CURVE` kind `"cresc_after_fp"` (default off) for a crescendo that starts on an fp / sfp mark; scherzo `{"pt": (0.6, 0.3)}`, holding the p point until 1 qn after the mark;
  - or extend `cresc_long` with `min_qn` 9.0 for these two hairpins (300 has no sfp, so only 900 changes there).
- `ACCENT_CC_AT` 902: (22, 0.5) -> (12, 0.5) for Violins II, violas and celli. c11 measured that strokes under CC11 75 speak late, so keep their 902 leads (`REATTACK_LEAD_AT`). With the slower curve the stroke starts near CC11 52 + 12 = 64. If pcx then reads them more than 60 ms late, give the stroke velocity instead of CC (inferred).
- `RIDE_TRIMS`: change [(895.5, 0), (896.5, -2), (900, -2), (901, 0)] to end at (899.6, -2), (900.0, 0). Keep the -2 dB on bar 300 and let the sf through at full level. Simulate the summit lead first: the sf reads -9.5 M on the mp3 now, so +2 dB would bring it near -7.5. If the lead drops under 0.5 LU, keep the row.
- Targets:
  - master p trough at least 10 dB under the sf, held until 902;
  - monotonic rise 902-909 with at least +4 dB from 904 to 909 (now +3.6);
  - mp3 dip at least 4 LU;
  - accents at 902 / 904 at most +3 dB over the curve's level on each stem.

### 3. c25's HP_HOLD_TO_NOTE_END holds the crescendo gain through printed decrescendos. The winds' ff > into the F major pp (bar 72, qn 213-216) lost 3-9 dB of its fall, and Clarinet 1 now rises (measured)

**Where.** Bar 72, qn 213-216: Clarinet 1, Clarinet 2, Bassoon 1, Bassoon 2, contrabassoon (ff accent, decresc into bar 73's pp episode). Also Flute 1 at 549-551.

**What is wrong.**
- The +4 dB hpgain of the 210-213 crescendo used to release across the decrescendo note (c18 vol_db on Clarinet 2: 3.75 at 212.9, falling to 0.17 at 215.9).
- With `HP_HOLD_TO_NOTE_END = 3.0` the hold runs to the note's end, because a rest follows. parts.json `hp_held_end` lists [213.0, 216.0] for all five winds and [549.0, 551.0] for Flute 1. The c25 vol_db on Clarinet 2 holds 3.75 to 216.0.
- Decrescendo depth, stem start against end, c18 -> c25:

| track | c18 | c25 |
|---|---|---|
| Clarinet 1 | -6.6 | **+2.0** |
| Clarinet 2 | -6.6 | -3.0 |
| Bassoon 2 | -7.0 | -3.8 |
| contrabassoon | -7.5 | -4.2 |
| Bassoon 1 | -16.3 | -14.5 |
| Flute 1, 549-551 | -1.3 | +0.3 |

- Clarinet 1's stem bumps to -27.4 at 215.5 (c18 -33.9), in the last beat before the pp.
- Of the 32 holds the rule made, these 6 are the only ones on a note under a printed decrescendo. The other 26 are arrivals into rests, which is the rule's purpose.

**Fix.**
- `tools/score_to_parts.py`, in the HP_HOLD_TO_NOTE_END loop (about line 5630): skip a hold when a printed decrescendo of the track overlaps the held span, i.e. `any(k == "decresc" and a < e_ and b > nx_ for a, b, k in track hairpins)`. The gain then releases across the decrescendo as in c18.
- Generic, default on whenever the rule is on.
- Target: those six decrescendos within 1 dB of c18's depth. Clarinet 1 falling at least 5 dB over 213-216.

### 4. On the mp3 the printed ppp passages are as loud as mp, and p solos reach the level of the f tutti. The LRA sits exactly on the 10.5 floor, so nothing else can be lifted without failing spec 6. The delivery has 2.7 LU of p10 headroom to spend on order (measured, simulated)

**Where.** Bars 1-12 (ppp / pp, Horn 1's call p), 141-148 (link ppp), 364-376 (close ppp). Also Clarinet 1's p swell at bar 247.

**What is wrong (mp3).**
- Passage means: ppp intro -17.7 and link ppp -17.7, against theme A (p / mp) -16.7, counterstatement p -18.3, trio dolce -15.9. The close ppp is -19.0, against the Meno pp -19.2.
- Horn 1's p arrival in bar 4 peaks at M -10.0. The f at bar 41-42 peaks at -9.8 (master -29.4 against -22.3).
- Clarinet 1's p swell in bar 247 reaches -12.2, at the level of the f passage means (-11.7).
- The master is in order. The 5 s quiet-passage lift raises a solo p line as much as a soft tutti: the delivery gain is +19 to +20 dB in the intro and +12 to +13 at bar 41.

**Simulation on the c25 master.**
- Extra `RIDE_TRIMS` rows: [(0, -2.5), (33, -2.5), (36, 0)], [(418, 0), (420, -2.5), (444, -2.5), (447, 0)], [(1087, 0), (1089, -2.5), (1130, -2.5)].
- Result:
  - I -14.1 LUFS (inside ±0.5), TP -1.3, limiter 3.7 (unchanged), summit and every rival unchanged;
  - **LRA 10.5 -> 11.5**; p10 -20.3 -> -21.3 (floor -23);
  - intro -17.0 -> -19.1, link -17.7 -> -20.0, close -19.0 -> -21.5; Horn 1's bar 4 peak -10.0 -> -11.6.
- Theme A, counterstatement, trio, Meno and stretto are unchanged.

**Fix.**
- `build/score_config.py` `RIDE_TRIMS`: add the three rows above. This is a delivery-only change, needs no REAPER work, and can be checked on the c25 master in a minute.
- This lowers the softest passages by about 2.3 LU against Dan's AirPods note. They stay above every quieter passage the mp3 already has: stretto -21.2, fugato -20.0, timpani 9-12 -21.7. The ppp passages would then sit 2-3 LU under the p / mp ones, as printed.
- If Dan prefers loudness to order here, use -1.5 dB: about LRA 11.0 by interpolation (inferred).
- Either way the LRA leaves the floor, which the next balance change needs.

### 5. Three older dynamic faults inside phrases (measured)

**a. Violins I, bar 200 (qn 597-600, printed decrescendo into p).**
- The 597 note (G sharp 5, 3 qn, under the slur from 596.5) has played since c19 as a Sus MAX re-attack at v66 (`reattack_leads` [597.0, 0.323]; Leg Slur only from 598.537). c18 joined it as a Leg Slur transition at v112.
- Stem per 0.5 qn: 595.5 -40.5, 596.5 -50.4, **597.0 -52.1**, 597.5 -49.3, 598.0 -44.8. It dips 11 dB and swells back +7 inside the decrescendo; c18 fell evenly from -45.4 to -47.9.
- Fix: move the "Leg Slur MAX" keyswitch before 596.5 (`ART_SPANS` or the re-attack exception that sends 597 to Sus MAX), so 596.5 -> 597 is a slurred join as printed.
- Target: 597-600 falling at least 3 dB, with no 0.5 qn window more than 2 dB under the next.

**b. Flute 2, bar 72 (qn 213, ff accent, decrescendo).**
- Since c22 the note plays the accent row at v90 with no lead. It enters at -43.1 and swells to -32.1 by 214.5: +11 dB inside a printed ff > (c18 -31.0, falling).
- Fix: v110 or more on this note (`VEL_SET` "Flute 2" 213.0; the row's velocity is the attack, p.101), or Sus MAX as in c18.
- Target: the first 0.5 qn within 3 dB of the note's maximum.

**c. Timpani roll, bars 237-240 (qn 708-718, pp, no crescendo printed).**
- It settles to -55 / -56 (711-713), then rises to -51.8 / -50.3 at 715-716 with the envelope flat at 12 dB from 711 to 718.
- It is one 10 qn note, so this is the roll sample, not the data (inferred).
- Fix: `TIMP_CC1_AT`-style hold, CC1 -6 over 714-718 on that roll, or a restrike at 714.
- Target: no rise over 1.5 dB inside the roll.

### 6. The ff tutti theme (bars 105 / 305) lands 1.8 dB under the top of the crescendo into it (measured; low priority)

- Master M max per beat: 104 -13.7 / -12.8 / -12.9, then **105 -14.6** / -16.9 / -17.9; 304 -14.9 / -13.6 / -13.3, then **305 -15.1**.
- On the mp3: 104 -8.4, 105 -9.0.
- Most of the drop is texture. The sustained hemiola chords become the staccato theme head, and the first bar of 105 is 3-5 dB lower in 15 of 18 stems.
- The downbeat itself (first quarter, a printed ff) is under the chord before it in Violins II (-29.6 against -27.7), violas (-36.9 against -30.2) and celli (-40.4 against -29.7). The celli's -40 is a rest or a late entry in the countermelody, not a fault.
- No change proposed this cycle. If finding 1's Sus Marc LITE stroke works, the same row on the strings' 312 / 912 downbeat quarters is the candidate (inferred).

## Do not touch

- The CC7 trim lane on moved time: hairpin depths per family match c18.
- S3 at both sub. p's (the hall decays under them); the G.P. hall.
- The timpani crescendo rolls (101-103, 205-208, 301-303) and the settling of the unprinted rolls 129-130 / 285-286.
- No loop pulsing on any held note (keep the re-bows and HELD_DOUBLE).
- The trio's arc as printed: 197 f wider than 209 f, the A6 at 218 the trio's loudest.
- The codetta fade, the accelerando growth, the held chord's fade 361-364 and the ppp close.
- The delivery chain and bed; the fugato ride lifts (+1.5).
- Bar 23's state.
