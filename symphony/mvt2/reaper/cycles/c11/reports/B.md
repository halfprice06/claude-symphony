# Critic B, cycle 11: balance and levels (render c10)

Method. I computed K-weighted levels (BS.1770 filter) in 10 ms frames from the c10 stems, which include the remixed solo stem. Positions use the parts.json tempo map, which matches the c10 render. Where I compare instruments in different registers, I also use A-weighted 50 ms frames. Delivery numbers come from ffmpeg ebur128 and from running `tools/deliver_master.py` unchanged on the masters.

Level changes were simulated in `sim.py`. The stems sum exactly to the master, so I scaled each stem by a dB envelope on the score-qn grid, using the role semantics with 0.25 qn ramps, summed the stems, and ran deliver_master. On the unchanged stems this reproduces c10 exactly: mp3 -20.0 LUFS, LRA 14.6, span 19.5, limiter 3.6.

Scripts and outputs are in `/private/tmp/claude-501/mockup-loop/c11-B/`: `prep.py`, `lib.py`, `dyn.py`, `rms.py`, `beats.py`, `sumlev.py`, `vol.py` (the build_reaper envelope recomputed per track), `crest.py`, `lowband.py`, `overshoot.py`, `tatt.py`, `melA.py`, `cbvc.py`, `sim.py`, `simcheck.py`.

Delivery, c10 (measured):
- Master: -23.6 LUFS, LRA 21.6 LU, TP -3.6 dBFS. Short-term p10 -40.4, max -13.0, span 27.3 dB.
- mp3: -20.0 LUFS, LRA 14.6 LU, TP -1.5 dBTP. Span 19.5 dB (target 16-19). Limiter 3.6 dB (target about 3). Climax rise 12.8 dB. 0 inversions. 81% of 5 s moves kept.
- The limiter now acts only in the bar 61 tutti (3.6-4.1 dB at qn 206.4-207.9) and lightly at qn 212.1 and 263.7. The Trombone 1 attacks no longer drive it.

What holds (measured):
- Printed dynamics map consistently across families. Per-note medians:
  - pp: winds -46.9, brass -47.0, strings -47.5
  - p: winds -40.3, brass -40.8, strings -41.9
- Melody margins (A-weighted, melody minus the loudest other stem, medians):

  | Passage | Margin (dB) |
  |---|---|
  | Hn1 solo, bars 7-14 | +5.2 |
  | Fl theme B | +4.8 |
  | CA, bars 41-51 | +3.0 / +6.2 |
  | Ob, bars 45-46 | +6.9 |
  | Violin I solo, bars 17-22 | +6.9 |
  | Ob answers, bars 19-20 | +8.5 |
  | Cl1, bars 85-86 | +10.8 |
  | Violins I+II, theme A / theme B / bars 71-74 / bars 79-81 | +8.0 / +6.2 / +7.6 / +5.8 |

- Cb is under Vc A-weighted in every bar where both play, apart from bars 31 and 40 (+0.7 and +1.6).
- The bar 84 timpani figure is now 2-6 dB over the violas and cellos at each attack (A-weighted).

## 1. The bar 61-62 wind chord spreads 14 dB between voices of equal weight, and the 1st players fall 5-7 dB into bar 62 under "ff molto sostenuto" (measured; fix simulated)

Where: Fl1/Fl2, Ob1/Ob2, Cl2 and BCl, qn 204-212 (Largamente, every wind marked ff). Code: the `hpgain` arrival in `tools/score_to_parts.py` and `build/roles.json`.

What:
- Only the tracks that played the bars 57-60 crescendo arrive with the crescendo gain. Envelope at qn 205 (gain + vol_db + dyn trim, from `vol.py`):

  | Track | dB |
  |---|---|
  | Fl1 | +3.5 |
  | Ob1 | +2.9 |
  | Cl1 | +4.1 |
  | Cl2 | +3.9 |
  | BCl | +5.9 |
  | Fl2 (enters at the ff, plus its role -3) | -3.9 |
  | Ob2 (enters at the ff) | -4.1 |

- Measured K levels over qn 204-212:

  | Group | Tracks and levels |
  |---|---|
  | Loudest winds | Fl1 -24.1, Ob1 -24.4, Cl2 -26.7, BCl -26.9 |
  | Other winds | Cl1 -29.3, Fl2 -30.8, Bn1 -30.9, Bn2 -31.3, Cbn -33.7, Ob2 -37.5 |
  | Brass | Hn2-4 -31.1 to -33.0, Tbn2 -30.3, BTbn -33.5, Tuba -34.1 |

- Ob2 is 13 dB under Ob1 on the same ff chord.
- Rimsky (rimsky-principles p33): in forte the woodwinds are equal to each other, and Horn = 2 woodwinds. The score marks horns f and trombones and tuba mf so that the chord balances. The mockup puts single wind 1sts 6-7 dB over the horns and leaves the 2nds 3-6 dB under them.
- The hpgain is released at the first onset after the arrival, so the 1sts drop inside the sostenuto. Per beat:
  - Fl1: -21.7, -22.9, -22.6, -22.2, then -24.5, -28.3, -29.0, -29.4.
  - Ob1 falls to -30.1 at qn 209.
- This is most of the open item "bar 62 falls 2.4 dB from bar 61". It is also the Fl1 +11 dB step from qn 203 to 204, the open item "Fl1/Ob1 +6..+9 dB into bar 61".

Fix in `build/roles.json`:
- Flute 1: [204, 208, -4], [208, 212, 1.5]
- Oboe 1: [204, 208, -3], [208, 212, -1]
- Oboe 2: [204, 210.1, 8]
- Flute 2: [204, 212, -3] becomes [204, 212, 1]
- Clarinet 2: [204, 208, -2.5]
- Bass clarinet: see finding 2.

A general rule could do the same: give a track that enters on an hpgain arrival the arrival gain of its family's crescendo, and cap the arrival's held gain inside SOSTENUTO_SPANS at +3. Simulate it before rendering, because it adds level where the roles take it away.

Simulated (findings 1+2 together, stems scaled):
- Wind and brass spread: bar 61 14 to 7 dB, bar 62 14 to 8 dB.
- Bar 61 / bar 62 master RMS: -13.7 / -16.1 becomes -14.4 / -15.8. The fall is 1.4 dB, which meets the c10 target of 1.5.
- Bar 61 stays 4.7 dB over bar 79.
- Master peak: -3.6 to -4.1 dBFS.
- mp3: limiter 3.6 to 3.3 dB, span 19.5 to 19.1, LRA 14.6.

Check after the render: every wind in qn 204-212 between -24 and -31 K, Ob2 within 4 dB of Ob1, and Fl1 bar 62 within 2 dB of bar 61.

## 2. The bass of the bar 61-62 climax is carried by the bass clarinet: it gives 25% of the master's 90-180 Hz, while tuba, bass trombone, contrabassoon and bassoons together give 12% (measured; fix simulated)

Where: qn 204-212. Tracks: BCl, Tuba, Bass trombone, Contrabassoon.

What (FFT band energy by stem, qn 204-212):
- 90-180 Hz: Cb 53%, BCl 25%, Timp 11%, Tuba 4%, BTbn 3%, Cbn 3%, Bn2 1%.
- 30-90 Hz: Cb 94%, BCl 3%, Tuba 2%, Cbn 1%.
- The master's 90-180 Hz band is 7.6 dB under its 180-350 Hz band in the tutti, against 0.7 dB in bars 37-52. The low brass the score adds at bar 61 does not fill the low register.
- BCl level: -26.9 K, level with Vc (-25.2) and Cb (-28.6), and 4-7 dB over Bn1/Bn2/Cbn. Its peak is -13.1 dBFS at qn 208.0, with a crest of 11.8 dB. It is the third-largest stem in the master's bar 61 sample peaks, after Vln I/II.
- Per Rimsky (p33), tuba = trombone = 2 horns in forte. Even at mf, two degrees under the winds' ff, the tuba should weigh at least as much as one bass clarinet at ff.
- The cause: BCl gets +7.9 dB of hpgain/chain at the arrival (envelope +5.9 dB at qn 205). The low brass get only the c06 role +2 and come from pp.

Fix in `build/roles.json`:
- Bass clarinet: add [204, 208.5, -4]. Its [188, 204, -5, 4] row stays.
- Tuba: [204, 212, 2] becomes [204, 212, 5].
- Bass trombone: [204, 212, 2] becomes [204, 212, 4].
- Contrabassoon: add [204, 212, 3].

Expected 90-180 Hz shares: BCl about 10%, low brass plus Cbn about 19% (inferred from the dB changes). Tuba and BTbn come to about -31 K, level with the horns. Included in the simulation in finding 1 (limiter 3.3, master peak -4.1).

## 3. Theme A's phrase arch does not climb: the printed mf goal in bar 28 is no louder than the mp start, and an unprinted swell in bar 24 overshoots it (measured; fix inferred)

Where: Violins I and II, bars 22-30 (qn 65-90). Printed: tutti mp at qn 65, a small < > in bars 23-24 (qn 68-72), a long < in bars 27-28 to mf at qn 82, then > p (qn 87) and pp (qn 89). Code: `base_points()` in `tools/score_to_parts.py`.

What:
- Violins I+II per bar (3 qn): bar 23 -34.2, 24 -34.2, 25 -32.8, 26 -37.1, 27 -34.9, 28 -35.1, 29 -35.9, 30 -42.7.
- All strings: bar 23 -32.7, bar 25 -31.1, bar 28 -32.3.
- The mf arrival is 0.4-0.9 dB under the phrase's mp start and 1.2-2.3 dB under bar 25.
- In the bar 53-56 theme B (p, mp, mf) the mix rises 6 dB. In bars 70-81 the strings rise steadily. Bars 23-28 are the one phrase whose printed peak sounds flat.

Causes, from parts.json:
- (a) The untargeted < at qn 68 takes `HP_STEP_SOFT` = 22 CC from 58 to CC 80 at qn 70. The next-mark cap looks only 1-6 qn past the hairpin's stop, so it misses the mf at qn 82. The swell peaks 8 CC over the printed goal, which itself gets CC 71-72.
- (b) The soft-trim taper (p +3.5, falling to the f trim) removes 1.7 dB between CC 58 and CC 72 on Vln I and 2.0 dB on Vln II. A 14 CC crescendo (about +3.5 dB of sample, LEARNINGS 2.5 dB per 10 CC) nets about +1.5 dB.
- (c) hpgain applies only to arrivals at f or louder.

Fix in `tools/score_to_parts.py`:
- `base_points()`: for an untargeted crescendo, look ahead for the next printed louder mark up to the next rest of 2 qn or more, or 16 qn, not just 1-6 qn. Cap `tgt` at that mark minus 8 CC. Here: 58 -> 64 instead of 80.
- Extend `hpgain` to crescendos that arrive on a printed mf: `HP_GAIN_MF_DB = {"string": 2.0, "wind": 2.0, "brass": 1.0}`, same hold and release as hpgain.
  - Condition: `DYN["mf"] - 2 <= base(b2 - 0.01) < DYN["f"] - 2`.
  - This affects 16 crescendos (Vln I/II 82 and 184, Vla/Vc/Cb 82, Vc 148 and 184, Cb 184, BCl 96, Ob1 148, Hn2 258, and Tbn2/BTbn/Tuba 204).
  - Tbn2/BTbn/Tuba 204 also take finding 2's roles, so check those three together.

Target: Violins I+II at qn 81-84 at least 2.5 dB over qn 66-69 and at least 1 dB over the bar 24-25 peak. No change in bars 52-56 beyond +2 dB.

## 4. The mp3 is still 0.5 dB over the span target and the ride sits at its cap in the ppp bars (measured; fix simulated)

Where: ppp bars 1, 83-85, 92 and the bar 61 limiter. Config: `build/mix.json` `soft_trim_db`.

What:
- Ride gain per bar: bar 1 +9.6, bar 84 +8.7, bar 92 +9.5, reaching +10 dB. Span 19.5 dB.
- After c10 the soft table is {ppp +1, pp +3, p +3.5}. ppp is still 2 dB under the pp lift, and the brief allows a further +2 to +4 on ppp.

Fix: in `mix.json`, global `soft_trim_db.ppp` goes from 1 to 3. pp and p stay, and so do the per-track overrides. CC11 stays as it is, so ppp keeps its layer, and the CC step still leaves ppp about 6-7 dB under pp.

Simulated mp3 results:

| Change | LRA | Span | Limiter |
|---|---|---|---|
| ppp change alone | 14.4 | 19.3 | 3.6 |
| Findings 1+2+4 | 14.4 | 18.9 | 3.3 |
| Findings 1+2+4+6 | 14.5 | 19.0 | 3.2 |

With findings 1+2+4+6 the master is -23.7 LUFS, LRA 21.5, peak -4.0 dBFS. TARGET_I stays at -19.5.

## 5. The two single timpani strokes printed p (bar 53 qn 172, bar 82 qn 271) are 6-11 dB under the p strings and oboe at the attack (measured; audibility inferred)

Where: Timpani qn 172 (A flat, the downbeat of F "a tempo") and qn 271 (bar 82). Code: `timp_db` in `tools/score_to_parts.py`, and `roles.json`.

What:
- A-weighted level of the first 150 ms:
  - qn 172: the timpani is 10.7 dB under Vln I and 9.3 dB under Vln II, both printed p.
  - qn 271: 7.3 dB under Ob1 and 6 dB under Hn4/Vln I.
- K-weighted per 1 qn: -55.0 and -54.5, against -38.5..-44 for the p strings and bassoon at qn 172.
- Causes:
  - The c10 soft trims (+3.5 at p) exclude the timpani (`_except`).
  - c03 cut p strokes from +16 to +12 when qn 271 was the loudest stem in bar 82.
  - The role Timpani [168, 172, -4] ramps out over [172, 172.5], so the qn 172 stroke starts 4 dB down.

Fix:
- `timp_db`: p strokes `12` -> `16`.
- roles.json Timpani [168, 172, -4] -> [168, 171.5, -4].

Target: each stroke's 150 ms A-weighted attack 2-4 dB under the loudest p instrument, and not the loudest stem in its bar.

## 6. Bar 63: Trombone 1's ff marcato motto enters under the strings' sf chord, and the Violin II sf spikes 10 dB (measured; fix simulated)

Where: qn 212-214. Strings print sf > to p; Tbn1 "1." ff marcato enters at qn 212.5.

What:
- K levels per 0.25 qn, Tbn1 against all strings summed:

  | qn | Tbn1 | Strings | Difference |
  |---|---|---|---|
  | 212.5 | -23.9 | -21.0 | -2.9 |
  | 213.0 | -22.0 | -23.2 | +1.2 |

  Only from qn 213.5 is the trombone 3.7-7 dB on top. The first two notes of the quotation sit inside the string chord's decay.
- Per Rimsky (p33), one trombone in forte equals two horns, or four woodwinds, or two violin sections.
- At the sf the string sections spike unevenly, measured from 0.5 qn before:
  - Vln II +10.2 dB (to -16.9; its stem peaks at -7.7 dBFS, the master's bar 63 peak, limiter 2.3 dB)
  - Vln I +5.2, Vla +4.2, Cb +1.5, Vc +0.4

Fix in `roles.json`:
- Trombone 1: [212.4, 213.6, 3]
- Violins I, Violins II, Violas, Violoncellos, Double basses: each [212.35, 213.6, -2], after the sf so the attack keeps its weight. It chains with the existing Vln II [212, 216, -6].
- Optionally, to even the sf, Violins II [212, 212.3, -3]. This needs a sim check against C #4b's peak finding.

Simulated with findings 1, 2 and 4: master peak -4.0 dBFS, limiter 3.2, span 19.0. Tbn1 comes to about +2 dB over the strings at qn 212.5 and +6 at qn 213 (inferred from the dB changes).

Do not touch:
- The soft-trim pp and p values and the per-track overrides. Cross-family pp/p levels are consistent within 1.6 dB.
- The Violin I solo track, its -1 dB gain and window. It is +6.9 dB over the accompaniment and balanced with the oboe answers.
- The bar 84 timpani role [277, 280, 10].
- The horn/trombone/tuba relation at bar 61 (horns f level with trombones mf, raised together in finding 2).
- The theme B and bars 70-81 rises.
- The Cb/Vc balance, A-weighted.
- `TIMP_LOUD_ATTACK_DB` 6; Tbn1 v108/105.
- deliver_master's ride and TARGET_I -19.5.
