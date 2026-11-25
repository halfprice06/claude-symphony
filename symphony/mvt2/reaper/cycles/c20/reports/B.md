# Critic B, cycle 20: balance and levels (render c19)

Method. I computed K-weighted (BS.1770) 10 ms frames and A-weighted 50 ms frames for the c19 master and all 32 stems, and placed them on score qn with the parts.json tempo map (parts.json 00:17, render 00:44, so they match). Printed marks come from `build/mockup-events.tsv` and score pages 1-7. Gains come from parts.json `cc11`/`vol_db`/`hpgain`, roles.json, mix.json, pitch_trims.json and early_fills.json. I compare instruments in the same register with K-weighting, and a melody against accompaniment in other registers with A-weighting. I simulated the proposed role changes by applying the `score_to_parts.py` role shapes (0.5 qn ramp in and release) to the stem frames. For the delivery check, I applied them to the stem audio, summed the stems and ran `deliver_master.py`. Scripts are in `/private/tmp/claude-501/mockup-loop/c20-B/`: `lib.py`, `beatsA.py` (per beat, K and A), `sgrp.py` (section sums per bar), `famdyn.py`/`trkdyn2.py`/`outl2.py` (dynamic map), `inv3.py` (printed-softer-but-louder scan), `lowb.py` (low bands), `sA.py`-`sE.py` (role simulations) and `simdel.py` (delivery simulation).

## Delivery, c19 (measured)

| | Master | mp3 | With findings 1-3 (simulated) |
|---|---|---|---|
| Integrated | -22.4 LUFS | -19.8 LUFS | -19.8 |
| LRA | 23.7 LU | 16.1 LU (target 14-16) | 16.0 |
| True peak | -3.8 dBFS | -1.6 dBTP | -1.5 |
| p10-to-max short-term span | 26.6 dB | 18.5 dB | 18.6 |
| Climax rise over the 15-20 s before | 13.6 dB | 11.7 dB | |
| Limiter | | 2.0 dB | 2.1 |
| 5 s moves reversed by the ride | | 0 | |

## What holds (measured)

The CC11 map is consistent across families. The table gives note medians in K.

| | pp | p | mp | f |
|---|---|---|---|---|
| Winds | -46.5 | -39.7 | -37.6 | -32.2 |
| Brass | -48.0 | -40.3 | -37.9 | -30.6 |
| Strings | -47.0 | -41.4 | -37.8 | -32.8 |

This matches Rimsky-Korsakov (rimsky-principles.txt p51): in piano, woodwind and brass are of about equal strength.

Other balances are in good shape:
- The solo margins over the loudest other stem, A-weighted median: oboe bars 15-16 +10.7, CA bars 47-51 +7.5, clarinet bars 85-86 +13.8.
- The c19 horn and a2 roles hold.
- No timpani roll is the loudest stem.
- In bars 61-62 the printed-mf low brass do not cover the bass. `lowb.py` puts the double basses at 0 dB of the master's 25-125 Hz band, the tuba at -18 dB and the bass trombone at -18 dB. The tuba is -6 dB of the 125-250 Hz band. Leave them.

The problems below are four passages where a section is far from the level its printed dynamic and role imply.

## 1. Bars 23-30 (theme A): the violas, the only harmony voice between the violin tune and the cello counter-line, are 6-9 dB under the violins at the same printed p < mf > (measured)

**Where.** Violas and Violas div, qn 66-87. The score (p. 2): Vln I and II play the tune in unison, the violas play div. dyads, and the Vc plays "unis., cantabile". All parts are p, with < mf > in bars 27-29.

**What.** Section sums per bar (`sgrp.py`), K:

| bar | Vln I | Vln II | Vla + div | Vc | Cb |
|---|---|---|---|---|---|
| 23 | -35.3 | -37.2 | -42.4 | -38.1 | -41.6 |
| 24 | -34.2 | -38.5 | -42.5 | -39.0 | -42.3 |
| 25 | -36.8 | -38.0 | -45.5 | -38.2 | -41.6 |
| 27 | -34.4 | -37.1 | -44.7 | -39.0 | -39.9 |
| 28 (mf) | -34.4 | -36.0 | -42.0 | -38.9 | -38.4 |
| 29 | -40.2 | -40.2 | -48.0 | -44.6 | -39.6 |

- A-weighted, the violas are 4.2-8.6 dB under Vln II and 7-11 dB under Vln I.
- The double basses, an octave or more lower, are louder than the violas in every bar.
- In the pp chorale of bars 15-21, the same viola stem is within 0-3 dB of Vln II. So the problem is specific to this passage.
- Rimsky (p28): the five string groups "produce a fairly even balance of tone". The c05 target for this passage was "Vln I at least 2 dB over Vla and Vc". The current gap is three to four times that.
- **Cause.** Violas get CC11 46 at p and vol_db -3 (curve.py at qn 66-78). The violins get the melody's CC11 58 and vol_db 0 to +5. On top of that, the c05 role `[80, 90, -3]` (copied to Violas div in c18) was set when the violas were level with Vln I. Since then the divisi split (c18) and the melody lifts have moved them 6-9 dB down.

The same thing happens on a smaller scale in bars 37-40 (qn 108-124). The violas' pp triplets are the moving inner line under the flute. They are 5-6 dB K and 3-5 dB A under the sustained Vln II sul tasto pad (Vln II + div) at the same pp. The c04 role Violas `[108, 124, -4]` caused this.

**Fix** (`build/roles.json`):
- Violas: replace `[80, 90, -3]` with `[87, 90, -3]`. Add `[66, 80, 3]` and `[80, 87, 3]`. The second row restores the 80-87 level; ROLE_CHAIN joins the two rows.
- Violas div: the same three rows.
- Violas: change `[108, 124, -4]` to `[108, 124, -1.5]`.

**Predicted** (`sE.py`; inferred for the sound):
- Bars 23-29: violas 3.5-5 dB K under Vln I and 1-3 dB under Vln II, about level with the celli. A-weighted, 3-6 dB under the violins. The tune still leads.
- Bar 30 (p > pp, the -3 kept): unchanged.
- Bars 37-40: violas 2-3 dB under the Vln II pad. The flute stays 6-10 dB A over every accompaniment stem.
- Mix bars 23-29: +0.3-0.5 dB.

## 2. Bar 60 (allargando, f < ff): the woodwind chord is upside down; bass clarinet, bassoons and Clarinet 2 are 3-5 dB A and 5-8 dB K over the flute and oboe on the top (measured)

**Where.** qn 200-204. Fl1, Ob1, Cl1-2, BCl and Bn1-2 all hold whole notes at f with < into the ff of bar 61 (score p. 4). Fl1 (E flat 6) and Ob1 (E flat 5) double the Vln I melody note.

**What** (per beat, A / K, `beatsA.py`):

| qn | Fl1 | Ob1 | Cl2 | BCl | Bn1 | Bn2 |
|---|---|---|---|---|---|---|
| 201 | 22.2 / -33.8 | 23.9 / -31.9 | 24.5 / -30.1 | 22.7 / -28.6 | 25.8 / -28.2 | 24.5 / -30.0 |
| 202 | 25.2 / -31.3 | 24.7 / -31.3 | 26.8 / -27.6 | 25.5 / -25.9 | 27.3 / -26.6 | 26.7 / -27.6 |
| 203 | 24.3 / -32.2 | 22.9 / -32.9 | 26.2 / -27.9 | 27.2 / -24.3 | 27.7 / -26.1 | 27.1 / -27.0 |

- BCl at -24.3 K is louder than any woodwind at ff in bars 61-62 (-25.1 to -35).
- The flute and oboe fall 4-6 dB at the barline (qn 198 Fl1 28.0 A) and never get back over the bass of the chord.
- Rimsky (p51): at f, the woodwinds are of about equal strength. A bassoon in its middle register does not outweigh a high flute and an oboe.

**Cause:**
- Every wind has the same chained `hpgain` +7 here. On top of that, the low reeds get the c16 climax low-octave roles: BCl `[188, 204, -5, 4]` opening over this bar plus `[200, 214, 2, 1]`, and Bn2 `[200, 214, 3, 1]`.
- Bassoon 1 plays E flat 3 at qn 200, which carries `pitch_trims.json` Bassoon 1 `"51": 6` with `_all_arts`. That trim was set for soft notes (c13) and now applies at f.
- Flute 1 E flat 6 (pitch 84) carries the -3 pitch trim.

**Fix** (`build/roles.json`):
- Bass clarinet and Bassoon 1: add `[200, 204, -4]`.
- Bassoon 2: add `[200, 204, -3]`.
- Clarinet 2: add `[200, 204, -2]`.
- Flute 1 and Oboe 1: add `[200, 204, 2]`.
- They nest under the existing rows and release into the ff on the 0.5 qn ramp. The bar 61 rows are unchanged.

**Predicted** (`sB.py`):
- qn 202-203: Fl1 26.3-27.2 A and Ob1 24.9-26.7, against BCl 21.5-23.2, Bn1 23.3-23.7 and Bn2 23.7-24.1.
- K: reeds -28.3 to -30.6, about level with Fl1 (-29.3 / -30.2).
- Bar 60 mix -16.4 -> -16.9, so the step into bar 61 grows by 0.5 dB.
- Delivery unchanged (table above).

## 3. Bars 55-56: the harp's mp arpeggios are as loud as the violin melody in K and sit over the horn and clarinet counter-line (measured)

**Where.** Harp, qn 180-188. The harp right hand plays sextuplets at mp. Vln I and II (unison tune) go mp < mf. Hn1 "1. espr." (p < mp) and Cl1 (pp < p) play a counter-line in unison (score p. 4).

**What** (per beat, `beatsA.py`):
- Harp: -33.3 to -36.0 K, 12.6-15.5 A.
- Vln I: -38.3, -35.6, -34.7, -31.5 K at qn 180-183. The harp is louder than each violin section at qn 180-182, and it is the loudest stem of bar 55 in metrics.md.
- Hn1: 9.7-13.1 A, except one 18.4 peak at qn 180.
- Cl1: 8.5-13.4 A. The counter-line sits 2-4 dB A under the harp figure.
- Over its whole part, the harp at mp measures -35.0 K. That is 2.5 dB over the family mp (-37.5) and only 1.8 dB under its own mf (-33.2).
- c13 removed Harp `[172, 188, -4]` because the p sextuplets at qn 172-179 were 3-8 dB under the celli. That was right for qn 172-179, where the harp is still 7.8-9.8 A. From the mp at qn 180, the figure is now on top.

**Fix** (`build/roles.json`): Harp, add `[180, 188, -3]`. The row covers only the mp bars, so the c13 lift at qn 172-179 stays.

**Predicted** (`sD.py`, scaled to -3):
- Harp about -36.5 to -39 K and 10-12.5 A. That is 2-7 dB under the violins and about level with the horn line.
- Bar 55 mix -27.8 -> -28.4.

## 4. Bar 77 beat 3: the p flute's eighth notes jump 5-7 dB over the mp violins it doubles, then drop 5-6 dB at the printed f (measured)

**Where.** Flute 1, qn 257.5-259. Fl1 (p) plays the Vln I (mp) tune in unison, cresc. to f at qn 259 "poco allargando".

**What** (A per 0.25 qn):

| qn | 257.5 | 257.75 | 258.0 | 258.25 | 258.5 | 258.75 | 259.0 (f) |
|---|---|---|---|---|---|---|---|
| Fl1 | 25.4 | 24.8 | 29.9 | 26.5 | 29.0 | 29.4 | 23.5 |
| Vln I | 26.1 | 25.7 | 22.9 | 23.2 | 23.8 | 28.3 | 22.3 |

- Over bars 75-77 before this point, the flute sits 1-6 dB under Vln I. That is right for a doubling printed one level softer.
- On the last beat, the flute is up to 7 dB over the violins, and its f arrival is 5-6 dB under the beat before. This is a reversed crescendo in the most exposed wind.
- In K: Fl1 -27.0 at 258.0 and -32.8 at 259.0.
- **Cause.** vol_db +8.2 at 257.5 and +9.65 at 258.5 (`curve.py`), from early_fills `"257.5": {db 4.9}` and `"258.5": {db 6.0, hold_s 0.23}` (c16/c17) plus the crescendo's hpgain 4. The 258.0 eighth (pitch 84) also rises 5 dB with no fill. Inferred: a loop seam or round robin.

**Fix:**
- `build/early_fills.json` Flute 1: `"257.5"` db 4.9 -> 2.0, `"258.5"` db 6.0 -> 2.5 (hold_s unchanged). Note them under `_auto` so `auto_fills.py` does not raise them again.
- `build/note_trims.json` Flute 1: add `"258": -3`. Note trims end at the next note's moved onset, so the qn 259 arrival is untouched.

**Predicted** (inferred from the vol_db steps): Fl1 at 258-258.75 about 24-26 A, within 1-2 dB of Vln I. The f arrival is about level with the last eighth, not 5 dB under it.

## Do not touch

- The CC11 dynamic map and the family soft trims, which are consistent across winds, brass and strings at pp to f.
- The c19 roles: the BCl/CA bars 31-33, the Hn1 crest at -1.0, the a2 horns `[269, 278, -5]`, Violas `[204, 212, 2.5]`, Horn 3 `[86, 90, -3]` and the Cb ppp soft trim 4.
- The low brass at bars 61-62: the basses own the low band.
- The violas' bar 30 cut (`[87, 90, -3]` stays).
- The harp lift at qn 172-179.
- Timpani levels and `TIMP_HP_DB_FACTOR`, including the bar 84 pp strokes.
- The Tbn1 bar 63 marcato line.
- The solo margins (oboe, solo violin, CA bars 47-51, clarinet bars 85-88).
- `deliver_master.py`.
