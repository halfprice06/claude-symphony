# Cycle 28, critic B: balance and levels (render c27)

## Method

All numbers come from `cycles/c27/render/`, which holds the stems and master after the c27 stem fix. Notes, dynamics, CC and envelopes come from `build/parts.json`, `build/mix.json`, `build/roles.json` and `build/mockup-events.tsv`.

**Measures.** Each stem has a 10 ms envelope (2048-point STFT, stereo power) in A-weighting, K-weighting and bands. "re M" means a stem minus the master over the same window. Per-note levels are taken on the note body (score onset + 0.12 s to + 1.5 s), or on the front 0.03-0.6 s for doubling comparisons. Simulations add (gain - 1) x stem to the master; this is exact for level-only changes.

**A against K.** At the soft and middle levels in this movement, K-weighting counts the double basses and celli 3-8 dB higher than A. For example, in bars 35-36 the p celli are 1.3 dB under the mf Vln I tune in K but 4-7 dB under it in A. In bars 131-132 the ff basses are top in K and 6 dB lower in A. Below mf I quote A for balance judgements, and K where I give both.

**Score pages checked:** 2-18 (all).

**Scratch.** Scripts were in `/private/tmp/claude-501/mockup-loop/mvt1-c28-B/` (`env.py`, `lib.py`, `notes.py`, `peer.py`, `ladder.py`, `pair.py`, `cmp.py`, `notecmp.py`, `top.py`, `fund.py`, `sim.py`). I deleted the folder at the end.

## What holds (measured)

**Cross-family mapping.** I paired notes of the same flat printed dynamic sounding together (A):
- Horns against single woodwinds: pp -0.5, p -2.1, mp +2.2, mf -1.4 dB (n = 8-31). That is Rimsky-Korsakov's "in piano all wind instruments are of fairly equal balance".
- Single woodwinds against Violins I at f/ff/fff: -6.3 / -5.7 / -3.5 dB (median). Rimsky-Korsakov gives about -3 at forte. Finding 2 covers the worst span.
- Every track's A ladder rises from p to ff.
- I found no family whose p is louder than another family's mp. The exceptions are the role-cut spans (Horn 4 at bars 63-66 and 74).

**Trumpets.** At pp (bars 113-115) the trumpets sit 13-23 dB under the master, rising with the printed cresc. They lead only where printed: bars 82-83 with the tune, bar 116, and the 167-170 theme. Trumpet 1 sits 1-6 dB over Trumpets 2/3 in chords, which is its register. I left this as c27 left it.

**Percussion.** I made no new measurement beyond the bar tops. Tam-tam 484 is the top stem of bar 122 (printed fff, heavy beater). The 696 stroke is not among bar 175's top six. The crash and suspended cymbal are as c27 B measured.

**Melody over accompaniment** holds at these bars: 1-9, 13-18, 23-25, 35-38, 43-52, 56-61, 63-68, 69-72 (dual theme), 77-79, 85-95, 97-110, 116, 122-130, 131-146, 147-152, 156-170, 171-176 and 178-182.

**Dan's checks.**
- Loop pulse and accent attacks: I made no new findings under this lens. The c27 B loop scan and the c27 accent fixes stand, and no render-level change since c27 affects held notes.
- Low end, loud tuttis: master 30-100 Hz re 300-2 kHz is -10.3 to -22.2 dB. Bar 97 is -10.3 and letter G -10.9; the c27 bells hold.
- The narrow boom left is finding 4.

## 1. Bars 19-21 (qn 76-83): the violas' espr. counter-line falls 10-14 dB under Violins I and under the mp second violins (measured; fix simulated)

**Where.** Score p. 2, strings only.
- Violas: mf espr. < at 72, f at 76, decrescendo at 80, mf at 84. This is the A♭4-G4-F4 line in half notes.
- Violins I: the theme, f < to sf at 78, then decrescendo.
- Violins II: mp off-beat eighths, with the sf note at 78.
- Celli: mf bass in half notes.

**Evidence (A, per note, re M).** Violas are compared with the other strings:

| Note | Violas re M | Violins I over violas | Violins II over violas | Celli over violas |
|---|---|---|---|---|
| 76 | -8.0 | +5.6 | -3.4 | -4.3 |
| 78 (A♭4, at the f peak) | -11.5 | +10.3 | +3.3 | -5.1 |
| 81 | -14.0 | +12.8 | +1.9 | +3.4 |
| 82 | -13.6 | +13.0 | -3.2 | -1.0 |

- In K the gaps to Violins I are 8.2 / 10.2 / 8.6 dB at 78 / 80 / 82.
- So the printed f espr. line sits under a printed mp accompaniment (Violins II) and, at 81, under the mf bass.
- Before 78 and after 83 the violas sit 3-6 dB under Violins I, which is right for a counter-line.
- The dip is specific to the A♭4 at 78 (velocity 83, Leg Slur MAX) and the 81/82 notes. The envelope there is only +0.75..+2.8 dB.

**Fix.**
- `build/roles.json` Violas: add `[77.5, 82.75, 5.0, 0.5]`. Level only, so it can be applied by stem fix.
- Simulated (A, re M), c27 -> fix:
  - violas 78-82: -11.3/-12.0/-11.7/-13.9/-14.4 -> -7.0/-7.6/-7.3/-9.3/-11.4;
  - Violins I stays 5-8 dB over them;
  - violas now 1-4 dB over Violins II;
  - master +0.3..+0.7 dB A over 77-81;
  - 83-86 unchanged.
- Do not extend the row past 83. A +5 over 76-85.5 simulated the violas level with Violins I at 84 (-1.8 vs -6.1).

## 2. Letter G, bars 117-120 (qn 464-480): Flute 1 and Oboe 1 doubling the ff violin tune sit 8 dB under Violins I and 4-5 dB under the held horn/trombone harmony (measured; fix simulated)

**Where.** Score p. 10.
- Fl 1-2 and Ob 1 play the accented tune ff with Violins I/II. The flute track carries it; Flute 2 holds the sustained line.
- Horns a2 and Trombones a2 hold ff harmony.

**Evidence (A, per note on the front 0.03-0.6 s, median over 21 notes).**
- Against Violins I: Flute 1 -7.9, Oboe 1 -8.0, Violins II -2.1, Horns a2 -3.4, Trombone 1 -2.7 dB.
- The same Flute 1 / Oboe 1 medians in the other ff/f doublings of the tune:

| Bars | Flute 1 | Oboe 1 |
|---|---|---|
| 26-31 | -1.5 | -6.3 |
| 98-102 | -2.5 | -4.6 |
| 138-142 | -4.1 | -4.8 |
| 158-161 | -3.2 | -5.4 |
| 167-170 | -3.3 | -2.6 |
| Letter G | -7.9 | -8.0 |

- Letter G is the outlier by about 4-5 dB.
- Per 2 qn re M, Flute 1 sits at -10.3..-17.2 and Oboe 1 at -11.4..-17.3, against Violins I at -5.1..-7.6.
- Rimsky-Korsakov (Principles, "Comparison of resonance") says that in forte one violin section equals two woodwinds, so a single doubling wind sits about 3 dB under it. Here the wind colour on the tune is close to gone (inferred).
- No role touches these two tracks between 464 and 484.
- Bar 12 (qn 43-48) shows the same thing on a smaller scale: the f Flute 1 tune sits 7.9 dB under Violins I and 2-3 dB under the mf Trombone 1. Flute 1's `dyn_trim_db` f -4 against `soft_trim_db` mf +2.5 makes its mf-to-f step in the envelope -6.5 dB (inferred contributor). I do not ask for a change there.

**Fix.**
- `build/roles.json`: add Flute 1 `[463.5, 479.5, 4.0, 1.5]` and Oboe 1 `[463.5, 479.5, 4.0, 1.5]`.
- They should end by 481, so bar 121 (where both already rise to -10..-12 re M) and the 484 arrival with Flute 1's `[484, 492, -3]` are untouched.
- Simulated:

| | c27 | After fix |
|---|---|---|
| Flute 1 re M | -10.9..-17.2 | -7.7..-13.4 |
| Oboe 1 re M | -12.2..-17.3 | -9.0..-13.6 |
| Fl/Ob gap to Violins I | 8 dB | 4-5 dB |
| Violins I re M | | -0.2..-0.4 dB |
| Master change, 464-476 | | +0.2..+0.5 dB A (+0.1..+0.4 K) |

- If the ramp is left running to 484, the master gains +0.8..+0.9 dB at 478-484; that is why the row ends at 479.5. Bar 122 and the climax order are unaffected. Check delivered S over 117-120 after the stem fix.

## 3. Second-theme phrase ends, bars 54-55 (qn 212-218.5) and 153-155 (qn 610-618): the pp second-violin chord rises to the level of the p/mp lines (measured; fix simulated)

**Where.** Score pp. 5 and 14.
- Violins II hold pp chords: metà until "tutti, div." at 216, and pp div. sul tasto tremolo in the recapitulation.
- They sit under the theme in celli/violas/Horn 1, the Clarinet 1 mp solo (bar 53-54 / 153) and the cor anglais p answers (bars 153-155).

**Evidence (A, re M, per 1 qn).**

Recapitulation:

| qn | Violins II | Cor anglais (p) | Horn 1 | Violas | Celli |
|---|---|---|---|---|---|
| 612-615 | -7.3..-8.8 | -8.3..-11.3 | -5.7..-8.3 | | |
| 616-618 | -5.2..-6.7 | -9.2..-17.8 | -10.4..-13.2 | -3.9..-7.1 | -5.0..-5.8 |

- Violins II hold a flat -16 dB A absolute from 584 to 619 (CC11 34-38, Tremolo row, the c03 +2 role [584, 619] for the sul tasto EQ).
- The melody decrescendos into bar 155 around them. So the pp chord ends level with the p melody and 4-8 dB over the cor anglais and Horn 1.

Exposition:
- Violins II at 213-215: -8.5 / -6.9 / -5.2, against the mp Clarinet 1 solo at -6.7 / -6.2 / -9.5. So at 215 they are 4.3 dB over it.
- At 217-218 they are -5.4 / -5.4, against the p celli tune at -3.6 / -4.4.

**Fix.**
- `build/roles.json` Violins II:
  - add `[610.5, 618.0, -4.5, 0.5]`;
  - add `[211.5, 218.25, -4.0, 0.5]`.
- Both end before the 619 and 219 molto cantabile entries and their leads.
- Simulated:

| Span | Violins II re M | Cor anglais / Clarinet 1 | Master |
|---|---|---|---|
| 612-618 | -9.3..-13.0 | cor anglais within ±2 dB | -0.4..-0.8 dB A |
| 213-218 | -7.8..-12.1 | Clarinet 1 1.4-2.3 dB over them | -0.4..-1.1 dB A |

- In 612-618 they also sit 3-7 dB under the melody.
- The delivery ride lifts these soft bars, so the delivered span should not move. Check it.

## 4. Double basses G2 and A♭2 (98/104 Hz): a near-sine fundamental that booms in bars 12-14 and 89-90 (measured; audibility inferred)

**Where.** Double basses:
- A♭2 at qn 44/46 (bar 12, Lento f) and 356 (bar 90);
- G2 at 48-55 (bars 13-14, under the Horn 1 solo), 358 (bar 90) and 20/22 (bar 6, pp).

**Evidence (measured).**

Cb stem, fundamental minus harmonics 2-4, per-pitch median:

| Pitch | dB |
|---|---|
| C2 | -11.8 |
| D2 | -6.4 |
| E♭2 | -12.0 |
| F2 | -0.2 |
| **G2** | **+4.6** (max +8.1) |
| **A♭2** | **+6.3** (max +9.6) |

- The c27 bells (61.7/73.4 Hz) and the 87.3 Hz bell2 do not reach these two pitches.

Master 85-120 Hz minus 300-2 kHz:

| Bars | dB |
|---|---|
| Bar 12 | -4.8 |
| Bar 14 | -6.6 |
| Bar 90 (356-358) | -5.2 |
| Bar 90 (358-360) | +3.3 |
| Other tuttis and soft passages | -11.4 (letter G) to -31.5 |

- The basses supply 89-100% of that band in these bars.
- In bar 12, in K, the basses are the top stem of the printed-f tutti (-7.8 re M, over the Violins I tune at -9.6).
- In bar 90 (mf under the mp celli fugato) they are second in K (-4.8).

**Fix.**
- `build/pitch_trims.json` Double basses: add `"43": -6` and `"44": -6`. The track already has `_all_arts`.
- Add 20.0 and 22.003 to its `_skip_onsets` so that the pp G2 of bar 6 keeps its level. Level only.
- Simulated (-5 dB on the stem), master 85-120 re 300-2k:

| Where | c27 | After -5 dB |
|---|---|---|
| Bar 12 | -4.8 | -9.0 |
| Bar 14 | -6.6 | -10.2 |
| Bar 90 (356-358) | -5.2 | -10.0 |
| Bar 90 (358-360) | +3.3 | -1.5 |

- With -6 dB, expect about 1 dB more.
- Bar 12 Cb K re M -7.8 -> about -13, under the tune. Master A change ≤ 0.1 dB, K -0.3..-0.6 dB.
- Do not do this with a static EQ bell at 100 Hz. That cuts the second harmonic of G1/A♭1, which carries the pitch of the letter-G G1 pedal and the A♭1s at qn 132, 220, 224, 272, 286 and 292 (their fundamentals sit 21 dB under).

## 5. Bass clarinet over the melody: bars 111-113 (qn 440-452) and bar 177 (qn 704-707) (measured; fix simulated)

**Bars 111-113.** Score p. 10.
- The Violins I mp cresc. tune sits over a five-instrument bass line: bass clarinet, Bassoon 2, contrabassoon, celli and basses, all mp cresc.
- In K the bass clarinet is level with Violins I. Re M at 440 / 442 / 448 / 450: BCl -7.8 / -7.6 / -6.7 / -8.4 against Vln I -7.8 / -6.9 / -6.8 / -8.6.
- In A the tune leads by only 0.6-2.6 dB, and the bass clarinet stands 4-6 dB over its own bass-line partners.
- Causes:
  - its envelope adds +2.6..+3.2 dB over 440-444 (soft trim at mp + hairpin gain);
  - CC11 crosses 67 -> 82 over 440-450, the patch's mid-range jump (kit LEARNINGS 4: bass clarinet +10.9 dB from the 52-64 to the 64-80 bin).

**Bar 177.** Score p. 17, pp chorale.
- The bass clarinet's D3 (704, under its c07 +2 role [696, 712]) sits at -7.2 / -6.4 / -5.3 A re M at 704 / 705 / 706.
- The Clarinet 1 pp tune ending (C5-B4) sits at -6.3 / -7.9 / -9.4. So the chorale's bass voice is 1.5-4 dB over the melody at 705-706.

**Fix.** `build/roles.json`:
- Bass clarinet `[439.5, 456.0, -3.5, 2.0]`. This ends before the crescendo's ff arrival at 464.
- Bass clarinet `[703.5, 707.5, -3.0, 0.5]`. It adds to the +2 row.
- Clarinet 1 `[705.75, 707.75, 2.5, 0.25]`.

**Expected (simulated).**

| Span | Bass clarinet re M | Tune | Bass line | Master |
|---|---|---|---|---|
| 440-452 | -9.7..-12.3 | 3.5-6 dB under Vln I | still its loudest member | -0.3..-0.5 dB |
| 704-707 | -7.6..-9.7 | Clarinet 1 level or over with its +2.5 | | -0.5 dB |

## Do not touch

- The c27 bells (61.7/73.4 Hz) and the 87.3 bell2 on the basses.
- The letter-G brass roles (Horn 3/4, Tuba) and the c27 bars 27-31 brass roles.
- The bar-40 timpani shape.
- The trumpet trims and roles.
- The percussion gains and shapes.
- The coda soft solos and the `_coda26` cut.
- The second-theme shapes of c24/c26.
- The CA [586, 605, +4] row and the Violins II [584, 619, +2] sul tasto row. Finding 3 adds a cut at the phrase end only.
- The climax order 160 > 122 > 167-170 > bar 26. None of the fixes above touches 484-496 or 628-648.
