# Critic B, cycle 19: balance and levels (render c18)

Method. I computed K-weighted 10 ms frames and A-weighted 50 ms frames for the c18 master and all 32 stems (the stems as delivered, after the actor's post-render fixes) and placed them on score qn with the parts.json tempo map. Printed marks come from `build/mockup-events.tsv` and score pages 1-8. Gains come from parts.json `vol_db`/`cc11`/`hpgain`, mix.json and roles.json. I simulated the proposed role changes by applying the role shapes of `score_to_parts.py` (0.5 qn ramp-in, end_ramp or 0.5 qn release) to the stem frames. Scripts: `/private/tmp/claude-501/mockup-loop/c19-B/` (`lib.py`, `melA.py`, `beatsA.py` per-beat K and A, `trkdyn2.py` per track and dynamic, `outl2.py` outliers against the family map, `vlabal.py` inner strings, `simB.py`/`simmix.py` predictions, `deliv.py`).

## Delivery, c18 (measured)

| | Master | mp3 |
|---|---|---|
| Integrated | -22.5 LUFS | -19.8 LUFS |
| LRA | 23.6 LU | 16.0 LU (target 14-16) |
| True peak | -4.1 dBFS | -1.6 dBTP |
| p10-to-max short-term span | 26.5 dB | 18.6 dB |
| Climax rise over the 15-20 s before | 13.6 dB | 11.7 dB |
| Limiter | | 1.7 dB |
| 5 s moves reversed by the ride | | 0 |

## What holds (measured)

- **The CC11 map is consistent across families.** Note medians (K): pp winds -46.5, brass -48.0, strings -47.0; p -39.7 / -40.3 / -41.4; mp -37.3 / -37.9 / -37.8. Rimsky (rimsky-principles.txt p51, book p. 33) says that in piano all winds, woodwind or brass, are of about equal strength, and one string section equals one wind. The map does that.
- **Horns at both climaxes (the c17 B #1 roles).** At qn 204-212 the horns are 25.6-27.7 A against single winds at 27.1-30.5. At 262-268 the a2 track is 27.2 A against Flute 1 at 30.3. Each horn is now within 2-5 dB of one ff wind, as Rimsky's "Horn = 2 Clarinets = 2 Oboes" implies for horns at f under winds at ff.
- **Timpani.** No roll is the loudest stem. The bar 60 p< roll arrives level with its f stroke at qn 203 (-26.9 K). The coda ppp roll sits at -59.5 K, 10-14 dB under the strings.
- **Lower solos.** Over the loudest other stem, per qn, A-weighted, median:

| Passage | Margin |
|---|---|
| Oboe, bars 15-16 | +11.0 |
| Solo violin | +8.9 |
| CA, bars 47-51 | +7.5 |
| Clarinet, bars 85-86 | +13.8 |
| Clarinet, bars 87-88 | +6.5 |

The problems below are the opposite case: solos and accompaniment notes printed p or mp that play at the level of f.

## 1. Bars 31-33: the bass clarinet's mf crest is at the woodwinds' f-ff level and buries the cor anglais's dolce entry, the upper voice of the duet (measured)

**Where.** Bass clarinet and Cor anglais, qn 91-99. The BCl (solo, espr., mp, then < to mf at qn 96 and >) and the CA (dolce, p, entering at qn 93) play the same chromatic descent, C-B-Bb-A over Eb-D-Db-C, a sixth apart. The CA is the top voice.

**What** (K per qn, `beatsA.py`):

| qn | 93 | 94 | 95 | 96 | 97 | 98 |
|---|---|---|---|---|---|---|
| BCl | -31.6 | -29.5 | -27.5 | **-26.7** | -31.6 | -33.8 |
| CA | -43.1 | -41.0 | -43.1 | -44.0 | -41.0 | -43.3 |

- A-weighted, the BCl is 9.0 / 7.6 / 11.4 / 13.4 dB over the CA at qn 93-96.
- The BCl's mf peak of -26.7 K is louder than the woodwinds' f median (-32.2) and ff median (-30.5), and louder than its own ff notes in bars 61-62 (-29.6).
- Rimsky (p51) puts winds in piano at about equal strength. With the BCl printed one to two levels over the CA, the CA should be about 4-6 dB under, not 12-17 dB K.
- **Cause** (parts.json): CC11 reaches 76 at qn 95.9 (mf 72 plus the solo boost), and `vol_db` adds about +1.4 dB on top of the roles [90,108,2], the BCl p soft trim (+3.5) and gain +1.

**Fix** (`build/roles.json`):
- Bass clarinet: add `[93.5, 99, -6, 2.5]`. The cut starts at the held Eb and opens over the decrescendo.
- Cor anglais: add `[93, 98.5, 2]`. It chains into the existing `[98.5, 102, -3]`.

**Predicted** (`simB.py`, K):
- BCl -35.1 / -35.5 / -33.5 / -32.4 / -35.3 at qn 93-97. It still swells about 3 dB to the mf.
- CA -41.1 / -39.0 / -41.1 / -42.0 / -39.0.
- The gap is 6-9 dB K and 0-5 dB A, with the BCl still on top.
- Bars 32-33 mix: -28.8/-29.3 -> -33.0/-32.9 K.

## 2. Bar 12 (horn) and bar 42 (cor anglais): two p<mp solo crests are 3.5-4 dB louder than the other solos with the same marking, at the instrument's own f level (measured)

**Where.**
- Horn 1, qn 32-37. The "dolce espr." solo is p < mp >.
- Cor anglais, qn 127-131. The "solo, dolce cantabile" is p < mp >, with the Flute 1 counter-line also p < mp > on the same beats.

**What.** Peak K per 0.5 qn (`simB.py`/`beatsA.py`):

| Solo | Marking | Peak K |
|---|---|---|
| Horn, bar 12 | p<mp | **-28.5** |
| Horn, bars 67-70 (same player, same marking, same register) | p<mp | -32.0 |
| Horn 1 at f, bars 59-60 | f | -29.4 |
| CA, bar 42 | p<mp | **-28.7** |
| CA, bars 47-51 | p, mp | -32.3 |
| Oboe, bars 15-16 | | -32.9 |
| Solo violin | | -35.3 |

- The bar 12 crest is as loud as the same horn's f, and the bar-12 mix (-30.8 K) is the loudest bar before bar 23.
- At qn 128-129 the CA is 11 dB K and 11-12 dB A over the flute that plays the same mp hairpin with it. In bars 47-51 the CA margin is +7.5.
- **Causes:**
  - CA: `vol_db` reaches +10 to +12.7 at 128-129.5. That is the roles [124,137,2], hpgain +3, the soft trim, and early fills 128/129/129.5 of 3.9-7 dB.
  - Horn: +9 to +12.7 at 34-35.5. That is roles [16.5,42,2.5] + [33.5,38.5,1.5,1], hpgain +3, PT +2, and the C #2 lift.
- Inferred: the mp of these two solos sounds like a forte, and the dynamic scale between the opening solos and the tutti flattens.

**Fix** (`build/roles.json`):
- Horn 1: change `[33.5, 38.5, 1.5, 1.0]` to `[33.5, 38.5, -1.5, 1.0]`. That is -3 dB over the crest and releases with the same end ramp. The c18 qn 34 loop-dip lift (`loop_fills.json`) stays as it is.
- Cor anglais: add `[127.5, 133.5, -3.5, 2.5]`.

**Predicted** (K):
- Horn peak -32.1 at qn 34, which matches bars 67-70. Its margin over the bassoons and bass clarinet is still +9..+13 dB A.
- CA peak -32.9 at 128-129, which matches bars 47-51. It stays 8 dB A over the flute.
- Mix: bar 12 -30.8 -> -33.3, bar 13 -34.2 -> -35.8, bar 42 -30.0 -> -32.4 K.

## 3. Bar 37: the bass clarinet's last p note covers the first two beats of the flute's theme B (measured)

**Where.**
- The BCl's pp < p ends on Db4 at qn 108 (2 qn) as Flute 1 enters with theme B, p, on F6.
- Accompaniment: Vln II pp, violas pp, harp p, Bn1 pp.

**What** (per 0.5 qn):

| qn | 108.0 | 108.5 | 109.0 | 109.5 |
|---|---|---|---|---|
| BCl (K) | -36.1 | -32.8 | -33.2 | -35.5 |
| Flute 1 (K) | -39.5 | -39.4 | -38.5 | -42.1 |
| BCl (A) | 17.6 | 21.1 | 20.2 | 17.0 |
| Flute 1 (A) | 16.7 | 16.4 | 17.6 | 13.9 |

- The BCl is the loudest stem at qn 108-109 (`loudest.py`: +3.1 and +2.7 dB A over the flute). Its p arrival is 7-8 dB over the p median (-41.0).
- **Cause.** At 108 `vol_db` is +5.6: the [105,108,3] crescendo gain plus the role [90,108,2] and its release, on top of the BCl's p trim of +3.5.
- Rimsky p54 (book): "melody should always stand out in relief from the accompaniment."

**Fix** (`build/roles.json`):
- Bass clarinet: add `[105, 110.5, -4]`. It ramps in over the end of the pp decrescendo at 104.5-105, so the pp < p crescendo keeps its full shape, about -48 -> -37 K.
- Flute 1: add `[108, 112, 2]`. This is the first phrase of theme B.

**Predicted.**
- qn 108.5: BCl about -36.8 K / 17.1 A, flute -37.4 K / 18.4 A. Flute lead about +1.3 A, where it was -4.7.
- Bar 36 mix -39.8 -> about -42.5, bar 37 -34.0 -> about -35. The mp3 ride lifts this range, so I expect no LRA change (inferred).

## 4. Bars 81-82: the a2 horns are the loudest stem in the p bar 82 and level with the melody in the bar 81 decrescendo (measured)

**Where.** "Horns 1-2 a2", qn 269-273. Hn 1-2 a2 play Db4 (269, 2 qn) and C4 (271, 2 qn, p >). The melody in Fl1/Ob1/Cl1 and Vln I goes f > p > pp, and everything is marked p at qn 271.

**What** (A / K):
- At qn 271: horns **21.7 / -32.3**. Vln I 16.4 / -38.3, Ob1 15.0, Cl1 15.3, Fl1 11.6 / -44.2. The horns are 5.3 dB A and 6 dB K over the top of the p chord.
- At qn 269-270.5: horns 16.8-22.3 A against Vln I 19.3-21.4 and Ob1 19.2-27.2.
- The a2 p note measures -35.0 K (first 1.5 s). The family p median is -41.0, and one horn at p is -39.9; two horns in unison should be about -37.
- **Cause.** The c18 post-render gain change on this track (gain -4 -> +0.6, +4.6 dB to match Horn 1 at f) applies at p too, and the track's only role [262,268,4,0.5] covers f only.

**Fix** (`build/roles.json`): Horns 1-2 a2, add `[269, 278, -5]`. The span runs past the hall tail of the last note (273.1). The track has no tail hold after its last note (c18 open item), so a role that ended at about 273.5 would move the tail.

**Predicted.**
- qn 271: 16.7 A / -37.3 K, level with Vln I at the attack and under it after.
- qn 269-270.5: 11.8-17.3 A, under the melody.
- Bar 82 mix -32.0 -> -32.7. Bars 79-80 unchanged.

## 5. Bars 61-62: the violas, the only inner chord voice in the string ff, are 5-6 dB under the second violins and celli (measured)

**Where.** Violas, qn 204-212, ff non div., molto sostenuto.

**What** (`vlabal.py`, per qn):
- Vla (plus div) against Vln II: median -5.4 K / -6.9 A. Against Vc: -6.0 K / -5.3 A.
- Elsewhere the gap is smaller:

| Passage | Dynamic | Vla minus Vln II (K) |
|---|---|---|
| Bars 79-80 | ff | -1.1 |
| Bars 41-80 | pp | -1.8 |
| Bars 41-80 | p | -1.0 |
| Bars 41-80 | f | -1.6 |

- **Cause** (mix.json `dyn_trim_db`): violas ff -3, against Vln I +1.5, Vln II -1.5 and Vc -2.5.
- Rimsky (p28): the five string sections "produce a fairly even balance of tone," with any surplus on the first violins.
- Inferred: the inner third of the climax chord is thin, and the ff string sound is violins plus bass.

**Fix** (`build/roles.json`): Violas, add `[204, 212, 2.5]`. It nests under `_all` [204,212,-1.4,3.5].

**Predicted.** Vla 25.0-26.7 A / -26.8..-29.0 K. That is 2-4 dB under Vln II and 1-3 dB under Vc. Bars 61-62 mix +0.1 dB, so the limiter is unchanged (inferred: the viola is not in the qn 207.87 peak sum's top contributors).

## 6. Two small inner-voice fixes: Horn 3 over the strings' cadence in bar 30, and the double basses falling away in the final ppp chord (measured)

**Bar 30, qn 87-89.**
- Horn 3 (pp, held) is the loudest stem: 8.0 / 8.7 / 6.6 A. Vln I is 6.8 / 2.8 / 2.0 and Vln II 6.0 / 6.6 / 3.9, with the strings printed p > pp.
- c17 B #6 cut Horn 4 here. Horn 3 has no cut.
- **Fix:** roles.json Horn 3, add `[86, 90, -3]`.
- **Predicted:** Horn 3 5.0 / 5.7 / 3.6 A, under the top strings.

**Bars 91-92, qn 292-304.**
- From bar 89 to the final chord (qn 301), each part falls by this much (K):

| Part | From | To | Fall |
|---|---|---|---|
| Vln I | -46.2 | -49.0 | 2.8 dB |
| Vc | -46.8 | -52.6 | 5.8 dB |
| Cb | -47.4 | -55.7 | 8.3 dB |

- All strings are printed > to ppp.
- The bass of the final chord ends 6.7 dB K under the top (Cb minus Vc goes from -0.6 to -3.1). In bars 83-86 (ppp) the Cb is 3.3-3.4 dB under the Vc, where elsewhere in the soft bars it is about level with them.
- **Cause.** mix.json Double basses `soft_trim_db` {ppp 1, pp 6, p 6.5}: a printed ppp costs the basses 5 dB more trim than pp. The celli and violins have no such step (global ppp 3, pp 3).
- **Fix:** Double basses `soft_trim_db` ppp 1 -> 4. This changes only bars 83-86 and 92.
- **Predicted:** Cb about -52.7 at qn 301, 1.6 dB under the Vc. Bars 83-84 Cb about level with the Vc.

## Do not touch

- The CC11 dynamic map and the family soft trims, which are consistent across winds, brass and strings at pp-mp.
- The c17 B #1 horn roles at 204-212 and the a2 track's f level at 262-268.
- The strings-to-winds ff balance at the climaxes.
- Timpani levels, `TIMP_HP_DB_FACTOR` and the coda roll.
- The solo margins of the oboe, the solo violin, CA bars 47-51 and clarinet bars 85-88.
- The Horn 1 qn 34 lift in `loop_fills.json` (finding 2 changes only the role around it).
- The Tbn1 bar 63 marcato line.
- `deliver_master.py`.
