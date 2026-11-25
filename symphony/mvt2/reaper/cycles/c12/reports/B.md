# Critic B, cycle 12: balance and levels (render c11)

Method. I computed K-weighted levels (BS.1770 filter) in 10 ms frames from the c11 stems (after the actor's envelope fix), with positions taken from the parts.json tempo map. I used A-weighted 50 ms frames only to compare instruments in the same register. Delivery numbers come from ffmpeg ebur128 and from running `tools/deliver_master.py` unchanged. Level changes were simulated by scaling stems with dB spans on the score-qn grid, summing them and delivering the result. On the unchanged stems the simulation reproduces c11 exactly (mp3 LRA 14.4, span 18.9, limiter 3.5). Scripts are in `/private/tmp/claude-501/mockup-loop/c12-B/`: `prep.py`, `lib.py`, `dyn2.py`, `win.py`, `vol.py`, `melgrp.py`, `arch.py`, `pitchres.py`, `lowshare.py`, `lim.py`, `sim2.py`, `simchk.py`.

## Delivery, c11 (measured)

| | Master | mp3 |
|---|---|---|
| Integrated | -23.7 LUFS | -19.9 LUFS |
| LRA | 21.5 LU | 14.4 LU |
| True peak | -3.6 dBFS | -1.6 dBTP |
| Span | | 18.9 dB |
| Limiter | | 3.5 dB |
| Climax rise | | 12.0 dB |
| Inversions | | 0 |

- The ride sits at its +10 dB cap in bars 1, 84 and 92.
- The limiter acts only in bars 60-63 (1-4 dB at qn 203.4-212.1) and at 1.2 dB at qn 263.7.

## What holds (measured)

**Cross-family mapping is consistent at the soft end.** Per-note medians:

| Dynamic | Winds | Brass | Strings |
|---|---|---|---|
| pp | -46.9 | -46.9 | -47.4 |
| p | -40.3 | -41.2 | -41.9 |

The exposed p solos are within 2.5 dB of each other: Hn1 -40.9, Ob1 -38.4, CA -40.8, Fl1 -39.4, Cl1 -40.3, solo violin -38.8.

**Melody group minus the loudest accompanying stem** (A-weighted, median):

| Passage | Margin (dB) |
|---|---|
| Hn1, bars 7-14 | +5.2 |
| Theme A | +7.9 / +8.4 |
| Theme B, bars 53-56 | +9.2 |
| Bars 57-60 | +7.9 |
| Bars 70-74 | +7.8 |
| Bars 75-78 | +9.4 |
| Bars 79-81 | +2.8 |
| Cl1, bars 85-86 | +10.7 |

**The c11 targets are met:**
- Bar 61 winds are between -26.3 and -31.5 K, and Ob2 is within 1.7 dB of Ob1.
- Fl1 bar 62 is level with bar 61.
- The bar 61 low brass and contrabassoon are at -28..-31 K.

**The low end is within the references' spread.** At 63 Hz the mix is -0.2 dB relative to 1 kHz. Dvorak 9/i is -6.2 and the two Brahms slow movements are about +2. At the climaxes the Cb's Db2 fundamental, 2nd and 3rd harmonics are within 3 dB of each other, so nothing is boomy.

## 1. Theme A (bars 23-28): pitch-dependent sample levels reverse the printed phrase shape (measured; fix simulated)

**Where.** Violins I and II, in unison, sul D, qn 65-87. Printed: mp at qn 65, < > over qn 68-72, < from qn 78 to mf at qn 82, then > to p.

**What.** Vln I+II K level per beat:

| qn | 65 | 66 | 67 | 68 | 69 | 70 | 71 | 72 | 73 | 78 | 79 | 80 | 81 | 82 | 83 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| dB | -36.1 | -34.6 | -31.9 | -37.2 | -37.9 | -34.8 | -33.1 | -30.6 | -32.8 | -35.0 | -32.7 | -34.2 | -36.2 | -32.1 | -34.7 |

- The top of the printed swell (Eb5, qn 68-70) is the quietest point of the first phrase. It sits 5-6 dB under the C5 on either side of it, although CC11 is higher there (64-66 against 61).
- Inside the crescendo, the F5 at qn 80-81 falls 1.5-3.5 dB.
- The mf arrival at qn 82 (-32.1) ends up 1.5 dB under the unmarked qn 72. This is why c11's B #3 changes gained only about 1 dB.

**Cause** (`pitchres.py`: level minus envelope minus 0.25 dB per CC, on notes of 0.9 qn or longer):
- Vln I's C5 (72) runs 3-4 dB hot on all 5 notes: -54.0..-55.7, against -57..-59 for its neighbours.
- F5 (77) is 4-5 dB weak in both sections: Vln I -63.3/-61.5, Vln II -68.8 at qn 80.
- The Eb5 at qn 68 is 3-6 dB weaker than the same pitch elsewhere: Vln I -61.7 against -58.2, Vln II -67.0 against -60.6.
- In these spots Vln II is 5-7 dB under Vln I on the same unison notes. Elsewhere the gap is about 2 dB.

**Fix** in `build/note_trims.json` (these add to the existing values):
- Violins I: add `"68": 4` and `"72": -3`; change `"80"` from 3 to 6 and `"82"` from 2 to 3.5.
- Violins II: add `"68": 6` and `"70": 3`; change `"80"` from 3 to 8; add `"82": 2`.
- Leave the existing early fills (67.5, 71, 80) as they are.

**Simulated per beat:** the swell becomes -32.6/-33.3/-33.4 at qn 68-70 and qn 72 becomes -33.0. The crescendo runs -35.0, -32.0, -29.8, -31.3, and the mf at qn 82 reaches -29.9, about 4 dB over the mp start. In the mp3, bar 28 becomes the phrase's loudest bar (-20.4 against -22.4 for bar 25; it was 0.3 dB over bar 25 before).

**Check after the render:**
- qn 68-70 within 1.5 dB of the qn 65-67 mean, or above it.
- qn 82 at least 2.5 dB over that mean and at least 1 dB over qn 72.

## 2. Opening and closing chords: the Violins I top note at ppp/pp stands 3-9 dB over the rest of the chord (measured; fix simulated)

**Where.** Bars 1-3 (qn 0-9.2): Vln I holds C5 ppp. In bar 2 the others move to pp, except the horns, which stay ppp. Bars 89-92 (qn 292-304): the whole chord is pp, falling to ppp.

**What** (K):

| Bars | Vln I | Others |
|---|---|---|
| 1 | -41.6 (ppp) | Vln II -47.7, Vla -50.1, Vc -51.0, Hn3 -51.5, Hn4 -51.9 (all ppp) |
| 2-3 | -40.8..-43.7 (ppp) | the pp chord at -44.5..-47.1 |
| 89-90 | -41.7, even with the c08 role -3 | Vln II -44.5, Vc -45.7, Cb -45.7, Vla -47.7 |

- The printed hierarchy is reversed: the one part marked softer (ppp against pp) is the loudest stem. In bar 1, Vln I carries 58% of the master's energy.
- Cause: the hot C5 from finding 1. Vln I's envelope is the same as Vln II's (+8 against +9.6 dB, CC11 22 against 24).
- Pitch trims stop at onset + 3 qn on notes over 4 qn, so these 9- and 12-qn holds need roles.

**Fix** in `build/roles.json`:
- Violins I: add `[0, 9.2, -5]`.
- Violins I: change `[292, 304, -3]` to `[292, 304, -6]`.

**Simulated:**
- Bar 1: Vln I -46.6, 1 dB over Vln II.
- Bars 2-3: Vln I -47.0, against the pp chord at -45.8..-48.0.
- Bars 89-90: Vln I -44.7, level with Vln II (-44.5).
- mp3: bar 1 goes from -24.2 to -26.4 RMS, so the ppp opening is now 2.4 dB under the p horn solo of bar 8. It was level with it.

## 3. Bars 79-81, the second climax: the wind chord spreads 12 dB, and Oboe 1 is 6 dB under Clarinet 1 on the same ff B flat 5 (measured; fix simulated)

**Where.** qn 262-271. All the winds are marked ff; in bar 81 Fl1, Ob1 and Cl1 play the "1." line with Vln I. This is the same entry-without-hpgain pattern that c11 B #1 fixed at bar 61, but here it was not touched.

**What** (per note, K, qn 262):

| Instrument | Level |
|---|---|
| Fl1 (Bb6) | -27.3 |
| Cl1 (Bb5) | -29.3 |
| Fl2 | -31.6 |
| Bn1 | -33.2 |
| Cbn | -33.8 |
| BCl | -33.9 |
| Ob2 | -35.5 |
| Ob1 (Bb5) | -35.6 |
| Cl2 | -38.9 |
| Bn2 | -39.2 |

- At qn 268, on the melody: Ob1 -35.7, Cl1 -32.4, Fl1 -26.3.
- Causes:
  - Ob1 enters fresh at ff with gain -5 and gets no crescendo gain.
  - Ob2 carries the c05 note trim 262 -4.
  - Bn2 is at -4.4 and Cl2 at -3 envelope.
- In bar 61 the same oboe is level with the flute (-26.5 against -26.3).
- Rimsky (rimsky-principles p33): in forte the woodwinds are equal to each other.

**Fix:**
- `build/roles.json`:
  - Oboe 1 `[262, 268, 4]`, `[268, 271, 3]`
  - Clarinet 2 `[262, 268, 3]`
  - Bassoon 2 `[262, 268, 3]`
- `build/note_trims.json`: Oboe 2 `"262"` from -4 to -2. My simulation used 0, which put Ob2 1.4 dB over Ob1.

**Simulated:**
- Bar 79 spread 9.5 -> 6.5 dB (qn 262-265 means: Fl1 -29.4 .. Bn2 -35.9). Ob1 -32.0, level with Fl2 and Cl2.
- At qn 268, Ob1 -32.4, level with Cl1 (-32.5).
- The melody margin (Vln I+Fl1 over Vln II) is unchanged, because the added energy is about 15 dB under the master.

## 4. Coda, bars 87-91: the muted horns are 5-11 dB under the pp chord (measured; audibility inferred)

**Where.** Horns 3-4 con sord. pp, qn 286-298. The rest of the chord (clarinets, strings) is pp too.

**What** (K):

| Bars | Hn3 | Hn4 | Strings | Clarinets |
|---|---|---|---|---|
| 87-88 | -52.0 | -49.4 | -44.9..-47.1 | -44.0 / -46.1 |
| 89-90 | -54.9 | -53.0 | -44.5..-47.7 (Vln I -41.7) | |

- Hn4 (F3) doubles the violas' F3 in unison and is 4-7 dB under it. Hn3, the upper horn, is 2.6 dB under Hn4.
- The horns lose level in four places:
  - The c05 role `[286, 298, -4]`, set before the c09 `mute_eq` existed.
  - The mute EQ itself.
  - Hn4's note trims 286 -5 / 289 -3.
  - The +3 pp soft trim, which they share with everyone.
- With this much cut, the muted-horn colour in the final chord is gone (inferred).

**Fix** in `build/roles.json`:
- Horn 3: `[286, 298, -4]` becomes `[286, 298, 1]`.
- Horn 4: `[286, 298, -4]` becomes `[286, 298, -1]`.
- Hn4's note trims stay.

**Simulated:**
- Bars 87-88: Hn3 -47.0, Hn4 -46.4, level with Vla (-45.7) and Vc (-47.1).
- Bars 89-90: -49.9/-50.0, 2-5 dB under the strings. That is a reasonable place for muted horns at pp.

## 5. Bar 34: the cor anglais (p dolce) covers the bass clarinet solo (p, "solo, espr.") (measured)

**Where.** qn 98.5-102.

**What** (K per beat): at qn 99/100/101, CA -39.1/-37.7/-41.1 against BCl -40.7/-40.8/-43.3. The CA is 1.6-3.1 dB on top for a full bar. In bar 33 the BCl (mf) is 7-9 dB over the CA, which is correct.

**Fix** in `build/roles.json`: Cor anglais `[98.5, 102, -3]` (new track entry). Simulated: CA -42.1/-40.7/-44.1, so the BCl is level or 1 dB on top.

## 6. The mp-to-mf step is the weakest step of the dynamic mapping (measured; part of finding 1, no separate fix proposed)

Per-note family medians, step to the next louder dynamic:

| Step | Strings | Winds |
|---|---|---|
| pp -> p | +5.5 | +6.6 |
| p -> mp | +3.2 | +2.1 |
| mp -> mf | +1.4 | +2.2 |
| mf -> f | +3.7 | +2.2 |
| f -> ff | +4.4 | +1.4 |

- The soft trims taper linearly from +3.5 dB at CC 46 to the f trim at CC 88. Over mp-mf (CC 58-72) they take away 1.5-2 dB of the 3.5 dB the samples gain.
- Finding 1's pitch effect explains theme A better than this does, so I do not propose a table change.
- If a later critic wants one: an `mf` anchor in the build_reaper/vol trim table (CC 72, value equal to p) moves the taper to mf-f. It must be simulated first, because it adds about 1.5 dB to every mf passage before the ride.

## All fixes together (simulated, findings 1-5)

| | Master | mp3 |
|---|---|---|
| Peak | -3.56 dBFS (unchanged) | |
| LRA | | 14.7 LU |
| Span | | 18.8 dB |
| Limiter | | 3.4 dB |
| Integrated | | -19.9 LUFS |

- Climax unchanged (bar 61 mp3 -9.4 RMS).
- Bar 1 is 2.2 dB softer in the mp3.

Do not touch:
- The soft-trim table and its per-track overrides (cross-family pp/p within 1.5 dB).
- The bar 61-62 wind and low-brass roles from c11.
- The Violin I solo track and its gain.
- The Tbn1 accent overrides and the bar 63 roles.
- The timpani p strokes (+16) and the bar 84 role.
- The Cb EQ and the Cb/Vc balance.
- The Hn1 solo and Cl1 coda roles (margins +5 to +11 dB).
- deliver_master's ride and TARGET_I -19.5.
