# Critic B, cycle 27: balance and levels (render c26)

Method. I used the c26 stems and master: K-weighted (BS.1770) 10 ms frames, A-weighted 50 ms frames, and band energies from FFTs. I mapped them to score qn with the parts.json tempo map. I compared them with the printed marks (`build/mockup-events.tsv`, score pages 1-8) and with the control data in parts.json (notes, cc11, vol_db) and `build/*.json`. Fixes were simulated by applying their dB to the stem frames. The scripts are in `/private/tmp/claude-501/mockup-loop/c27-B/`: the c26-B set, re-pointed at c26, plus `mbar.py` (master K per bar), `ccmap.py` (CC11 and velocity per printed dynamic), `outl2.py` (note outliers by dynamic), `pitchhot.py` (per-pitch residuals), `timp.py` and `lomid.py` (30-100 Hz against 100-400 Hz, mix and Dvorak reference).

## Delivery, c26 (ffmpeg ebur128 agrees with metrics.md)

| | Master | mp3 |
|---|---|---|
| Integrated | -22.6 LUFS | -19.8 LUFS |
| LRA | 23.6 LU | 16.0 LU (target 14-16) |
| True peak | -4.1 dBFS | -1.7 dBTP |
| p10-to-max span | | 18.5 dB |
| Limiter | | 1.7 dB |

Findings 1-3 lower or reshape single lines and do not touch the climax peak. Finding 4 adds about 0.4 dB at the two climaxes. That is inferred to raise the limiter by 0.3-0.4 dB, and the LRA by under 0.2 LU.

## What holds (measured)

**The dynamic map agrees across families.** Median K of accompaniment notes by printed dynamic:

| | winds | brass | strings |
|---|---|---|---|
| pp | -47.5 | -47.9 | -47.3 |
| p | -42.3 | -40.3 (n 6) | -44.2 |

CC11 per printed dynamic is consistent in every family: pp 34-38, p 43-63, f 84-93, ff 111-119. The only exceptions are the timpani, which run on CC7 by design.

**The climax proportions in bars 61-62 (qn 204-208, K sums):**

| strings ff | winds ff | low brass mf | horns f |
|---|---|---|---|
| -17.8 | -18.7 | -22.4 | -24.6 |

**The bass is in order.**
- No Cb pitch is hot after the c25 trims. For example, the Ab1 notes in theme A come within 1 dB of their neighbours (-43.3 against -44.4..-45.1 K).
- The timpani are the loudest stem only in their printed pp solo in bar 84.
- Mix 30-100 Hz against 100-400 Hz is -16.0 / -15.5 / -14.1 dB (soft / mid / loud windows). The Dvorak reference is -11.4 / -13.5 / -19.2, so the loud passages carry about 5 dB more low end than the reference. I traced no single stem or pitch that causes this, so no fix is proposed.

**The c26 B fixes landed.**
- Bar 81: Horns 3-4 fall 4-5 dB across the bar.
- Bar 30: the horns are 2.5 dB lower.
- Cl1 292 now falls through bar 89.

## 1. Bar 78: Clarinet 1's held A flat 4 (an inner f harmony note) gets the +6 dB A flat 4 pitch trim and swells over the flute melody (measured)

**Where.** Clarinet 1, A flat 4 at qn 259-261 (bar 78, f, poco allargando, p. 6). Fl1 and Vln I carry the tune. Cl1 holds a half note of the wind harmony.

**What.** K per 0.25 qn:

| qn | 259.0 | 259.5 | 260.0 | 260.25 | 260.5 | 260.75 |
|---|---|---|---|---|---|---|
| Clarinet 1 | -34.8 | -33.1 | -30.7 | -28.3 | -27.7 | -27.5 |
| Flute 1 (melody) | -30.8 | -33.7 | -31.7 | -32.5 | -31.7 | -41.7 |
| Violins II | -36.9 | -33.2 | -30.9 | -31.7 | -30.9 | -32.5 |

- From qn 260.25 to 260.75, Cl1 is 4-5 dB over the flute and the second-loudest stem after Vln I. `clim.py` at qn 260 gives "Clarinet (f) -28.4" over Vln II, Vc and Fl1 in both K and A (A 26.7 against Fl1 22.9).
- It rises 7 dB through a held note that has no hairpin of its own.

**Cause, in parts.json.** Cl1 vol_db at this note is +9.6 -> +14.5 -> +17.0 dB, the highest value on the track.
- The A flat 4 entry in `build/pitch_trims.json` ("Clarinet 1": `"68": 6`, `_all_arts_pitches` [68, 70]) applies to every articulation. It was fitted for a weak soft legato sample.
- At ff the same trim was already found to overshoot. c15 put qn 204 into `_skip_onsets`, and that ff A flat 4 now measures -31.8 K. The f A flat 4 at 259 measures -32.0 over its first 1.5 s even before the swell, so the trim is not needed here either.
- I checked that `_skip_onsets` matches against `n["qn"]`, which holds the score onset at that point (`sq` is written from it at output), so "259" matches.

**Fix.** `build/pitch_trims.json`, "Clarinet 1": `"_skip_onsets": [204]` -> `[204, 259]`.

**Predicted (stem minus 6 dB):**
- Cl1 at qn 260-260.75 comes to about -36.7 / -34.3 / -33.7 / -33.5 K, 1.5-2.5 dB under the flute and 6-8 dB under Vln I.
- It still sounds as part of the f wind chord, level with Vln II.

## 2. Bars 85-88: the pp dolce clarinet solo plays louder than the same player's p solos, and bars 86-87 swell to the coda's loudest point where nothing is printed (measured; the judgement of the target level is inferred)

**Where.** Clarinet 1, qn 280-292 (p. 7-8):
- Bar 85: niente < pp, dolce.
- Bar 86: the pp held on.
- Bars 87-88: pp after the breath.
- Under it, the violas and celli are ppp and the Cb ppp, then everyone is pp from bar 87.

**What.**
- Cl1 notes (K over the first 1.5 s): 283 -38.1, 286 -38.9, 289 -41.5. Its own p solos are 1-6 dB softer:
  - bars 54-56: 180 -42.0, 182 -41.6, 184 -42.6, 186 -45.2
  - bar 76: 252 -39.9
- The pp arrival of the bar 85 hairpin (qn 282) is at -40.3. The line then keeps rising with no printed mark: 283.75 -37.6, 284.0 -36.3, 284.25 **-35.8**. It falls to -43.3 by 285.5, then rises again to **-36.8** at 287.25.
- These two peaks are the master's loudest K frames of bars 83-92 (-35.5 and -34.8). At those peaks the solo is 13-15 dB over the ppp accompaniment and 9-10 dB over Vln II, the horns and the violas in bar 87.
- The other exposed soft solos sit 6-8 dB over their accompaniment (`melA.py`): Hn1 bars 7-14 +6.0, Ob1 bars 15-20 +6.4..+8.3. Bars 85-86 sit at +12.9.

**Cause, in `build/roles.json`.** The "Clarinet 1" rows stack:
- [280,297,3,2]
- [286,297,2.5,2]
- [283,297,1.5,2]
- [284.25,285.75,3]
- [287.4,289.0,2.5]

The two short rows put +3 and +2.5 dB on top of the +4.5 to +7 dB the long rows give at those points. vol_db reaches +8.5 at 283, +6.9 at 284.25 and +8.75 at 287.4. The c24 row [284.25, 285.75, 3] filled a dip that the c25 long rows (held to 297) have since covered. The bar 87 row dates from c23, when Cl1 sat under Cl2 at 287.5. It is now 10 dB over Cl2.

**Fix.** `build/roles.json`, "Clarinet 1": delete `[284.25, 285.75, 3]` and `[287.4, 289.0, 2.5]`. Keep the long rows held to 297.

**Predicted (stem frames minus the row shapes):**
- Bar 86 peak about -38.8 K, bar 87 peak about -39.3.
- The line then holds within about 1.5 dB from the pp arrival through bar 87, then falls into bar 88.
- The solo stays 4-6 dB over the pp tutti of bars 87-88, and about 10 dB over the ppp strings of bars 85-86.
- Its pp notes land 1-2 dB under its p solos instead of 1-3 dB over them.
- The mp3 ride lifts this whole passage, so the solo stays clearly audible. That is inferred from the deliver_master ride, which works on the master and does not change stem ratios.

## 3. Bar 64: Trombone 1's last accent (qn 218) has no weight left. Its body is level with the eighths around it (measured)

**Where.** Trombone 1, the accented F3 at qn 218 (ff, accent, decrescendo to mf at 219.5; BRIEF item 9, Dan's rule of 2-4 dB with no hard edge).

**What.** Tbn1 body K (0.06-0.4 s after the onset) and the rise time to within 3 dB of the body:

| qn | 212.5 acc | 213 acc | 214.5 | 215 | 215.5 | 216 | 217 | 217.5 | 218 acc |
|---|---|---|---|---|---|---|---|---|---|
| body K | -20.1 | -18.6 | -21.7 | -20.5 | -23.2 | -23.8 | -21.9 | -24.2 | **-21.8** |
| rise to -3 dB | 100 ms | 10 ms | 70 | 30 | 30 | 30 | 90 | 70 | 70 |

- The marcato eighths average -22.5 K. The accents at 212.5 and 213 are +2.4 and +3.9 dB over that, inside Dan's range.
- The accent at 218 is +0.7 dB over the eighths and level with the 217 eighth (-21.9). It reads as one more note of the line, not an accent.
- Its harshness is gone. The c26 CHANGES figures show its 2-5 kHz attack 9.4 dB under its body.
- The weight is missing because the decrescendo CC11 ramp starts at 218 and takes back most of the `ACCENT_DB_AT` swell (+6.0, held only to +0.25 s).
- Side note for critic A: the 212.5 entry takes 100 ms to come within 3 dB of its body, the slowest attack of the solo. That is a front edge question, not a level one.

**Fix.** `tools/score_to_parts.py`:
- `ACCENT_DB_AT["Trombone 1"][218.0]`: 6.0 -> 8.0.
- `ACCENT_SWELL_S_AT["Trombone 1"][218.0]`: (0.07, 0.25, 0.6) -> (0.07, 0.35, 0.8), so the weight lasts through the first beat of the decrescendo.

Do not touch the articulation (Sus MAX), the velocity (92) or the no-bump CC11. Those keep the timbre soft.

**Predicted.** Body about +2.5..+3 dB over the eighths. That is level only, so the 2-5 kHz attack-to-body ratio does not change. Check after the render that the master 2-5 kHz jump at 218 stays under +4 dB (it is +2.1 now).

## 4. The horn chords at both climaxes sit 5-6 dB under the woodwinds. Per player, a horn at f is level with one woodwind at ff, where Rimsky-Korsakov's ratio is one horn = two woodwinds (levels measured; the target is inferred)

**Where.**
- Bars 61-62 (qn 204-212): Horns 2-4, f.
- Bars 79-80 (qn 262-268): Horns 1-2 a2 and Horns 3-4, f.
- In both places the winds and strings are ff.

**What, in K:**

| | horns sum | winds sum | strings sum |
|---|---|---|---|
| bars 61-62 | -23.4 | -18.6 | -18.0 |
| bars 79-80 | -24.1 | -18.7 | -19.5 |

| per player | horns | Flute 1 | Oboe 1 | Clarinet 1 / Bassoon 1 |
|---|---|---|---|---|
| bars 61-62 | Hn2 -28.3, Hn3 -27.9, Hn4 -28.5 | -26.7 | -27.2 | -31.2 / -31.4 |
| bars 79-80 | a2 -26.8, Hn3 -32.6, Hn4 -30.0 | -25.3 | -28.0 | -28.3 / -31.5 |

- A-weighted, the horn sum is 6.5-7 dB under the winds.
- `reference-books/text/rimsky-principles.txt` (lines 1965-1975): "Horn = 2 Clarinets = 2 Oboes = 2 Flutes = 2 Bassoons" in loud passages. A horn should then sit about 3 dB over a single wind. Four horns should be about 1 dB under ten winds, not 5 dB.
- The composer already marked the horns one step lower (f) for that reason. The horns carry the harmonic core of both climaxes, and they are thin here.

**Fix.** `build/roles.json`, +2.5 dB on the existing climax rows:
- Horn 2: [204, 212, 5] -> 7.5, and [262, 268, 2] -> 4.5.
- Horn 3: [204, 212, 5] -> 7.5, and [261.5, 268, 2, 0.5] -> 4.5.
- Horn 4: [204, 212, 5] -> 7.5, and [262, 268, 5, 0.5] -> 7.5.
- Horns 1-2 a2: [262, 268, 4, 0.5] -> 6.5.

**Alternative.** If the actor prefers colour over level, raise the horns' f CC11 at these two spans from about 89 to 100 (brighter f layer) and add only +1 dB. That needs a `dyn_curve` override; I did not check the HO horn layer table for where the ff layer starts.

**Predicted (stem sum).**
- The horns come to about -21 / -21.6 K, 2.5-3 dB under the woodwinds.
- Master +0.36 dB at qn 204-212 and +0.43 dB at qn 262-268.
- Limiter about 2.0 dB (inferred). The climax stays the loudest.

**Condition.** If the mp3 limiter goes over 2.5 dB, keep +1.5 instead of +2.5.

## Smaller items (measured, no change proposed)

- **Bar 55, qn 180-180.5.** The melody's Gb5 comes after the bar 54 decrescendo to mp. The Vln I+II sum there (-35.2 K) is 1 dB under the Vc half note (-34.2) and 1-2 dB over the horn counter. In A-weighting the melody is 3-6 dB over both. This is a printed mp start of the next crescendo, so I left it.
- **Bars 37-40 and 284-292.** Violins II div and Violins II carry 41-62% of the master's 25-50 Hz energy. That is sub-sonic noise in the flautando and Sus samples, about -30 to -42 dB of the total. It is inaudible, but a 40 Hz highpass on the two Vln II tracks in `mix.json` `eq` would remove it.
- **Climax low brass.** The tuba at mf (-25 K) is 2 dB over the ff basses in bar 61. That matches Rimsky's f tuba = two string sections, so I left it.

## Do not touch

- The cross-family CC11 map, `soft_trim_db` and the family trims (pp agrees within 0.6 dB across the three families).
- The c26 B fixes: `HP_TARGET_AT` Hn3/Hn4 268, Hn3/Hn4 [86,90,-5.5], and the Cl1 292 trim removal.
- The Clarinet 1 long coda rows held to 297.
- The Cb pitch trims (32 -5, 37 -2, 39 +4) and the Cb EQ set.
- The bar 61-63 low-brass levels.
- The Timpani [277, 280, 10] row and the ppp roll rows.
- `deliver_master.py`.
