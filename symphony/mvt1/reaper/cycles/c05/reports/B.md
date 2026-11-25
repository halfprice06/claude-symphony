# Cycle 5, critic B: balance and levels (render c04)

## Method

Measured on the stem-fixed c04 render (`cycles/c04/render/`); score qn maps to file time through the parts.json tempo map with no shift. Levels are K-weighted stereo power on 25 ms hops. "Margin" is the lead's level minus the loudest other stem in the same 1- or 2-qn window. Note bodies run from onset +0.08 s to min(end, +1.5 s); "raw" is the body minus the parts.json `vol_db` at the onset. Simulations apply role, mix and pitch changes to the stems with build_reaper's `vol_points` and deliver with `tools/deliver_master.py` (`sim3.py`/`sim4.py`; with no change they reproduce c04 exactly: LRA 15.5 LU, span 20.2 dB, limiter 2.8 dB, peak 1.440). Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c05-B/` (`lead.py`, `leadscan.py`, `simm.py`, `trem.py`, `artdyn.py`, `pairs.py`, `invscan.py`, `s_all.json`).

## Does p sound like p in every family? (measured)

Heard body medians per printed dynamic (dB K):

| | pp | p | mf | f | ff |
|---|---|---|---|---|---|
| Single winds | -42.3..-46.5 | -41.1..-46.2 | -38.0..-42.3 | -35.0..-39.8 | -30.6..-35.1 |
| Horns | -41.3..-45.5 | -41.5..-43.3 | -35.4..-39.7 | -34.9..-35.8 | -29.1..-29.6 |
| Trumpets | -41.9..-45.4 | | | -33.5..-34.7 | -26.8..-29.2 |
| Trombones, tuba | -42.8..-46.3 | | | -31.0..-32.1 | -25.3..-30.0 |
| Vln I / Vla / Vc / Cb | -43.4..-47.6 | -40.1..-44.5 | -37.3..-40.9 | -33.3..-38.9 | -25.9..-34.2 |
| Violins II | -43.1 | **-38.5** | -38.5 | -35.1 | -30.8 |

The families agree within 2-4 dB at pp and p, and from f up they follow Rimsky-Korsakov's ratios (trumpet = trombone > horn > single woodwind). At the same onsets Trumpet 1 is +2.9 dB over Horn 1 at f and +2.3 at ff, and 1.8 / 0.7 dB under Trombone 1. The new trumpets fit.

The one family outlier at the soft dynamics is Violins II at p:

- Same onsets, same printed p: +7.4 dB over the violas (n=11), +4.5 over the celli (n=11), +5.7 over the basses.
- At pp it is level with them: +0.2 / -1.2.

The percussion is as c04 B measured it, with the stems unchanged since then:

- The tam-tam fff is the loudest stem for 0.5 s, then 9 dB under the master at 1-6 kHz.
- The crash carries the master's 6-16 kHz band for 0.3 s.
- The suspended cymbal is inaudible until its last 0.3-0.5 s.
- The tam-tam pp is a low hum, 10 dB under the strings.

The printed-dynamic inversion scan (`invscan.py`) looked for every 2-qn window in which a track printed two or more levels softer plays 3 dB or more louder than another track. Violins II has the most cases (bars 37, 46, 77-80). The rest are single bars that roles already cover.

## 1. The Violins II tremolo row plays 6-10 dB hot, and at p it covers the melody (bars 37-40) and the wind solos (bars 77-81)

**Where:** Violins II, the single-note tremolos at qn 144-160 (bars 37-40, p < f) and qn 304-324 (bars 77-81, p, then < to the ff of bar 82).

**What is wrong (measured):**

- The Violins II KS Master's Tremolo row is far louder than its Sus/Leg rows at the same CC11. Raw medians:

  | Dynamic | Tremolo | Leg Slur MAX | Sus MAX |
  |---|---|---|---|
  | pp | -37.8 | -43.3 | -43.8 |
  | p | -36.4 | -39.4 | -44.5 |
  | mf | -30.3 | -39.6 | -39.3 |
  | f | -25.0 | -40.3 | -35.1 |

- The violas' Tremolo row is not hot (p -44.8 against Sus -43.6). The divisi rule's extra -3 dB cut for tremolo chords hides this wherever the chord has two notes, but the single-note tremolos get no cut.
- Bars 77-80: the Violins II p tremolo is -36.3 to -38.1 dB, and the violas' p tremolo on the same chord is -44.7 to -45.6 (+7.0 to +8.5 dB).
- In those bars Violins II is the loudest stem:
  - over the bass clarinet's mf espr. "Solo" by 4.2 dB (median per beat, bars 77-78);
  - over the a2 horn entry in bar 78 by 5.8 dB.
- Bars 37-40: the Violins I mf melody sits a median 3.1 dB under the loudest other stem (8 of 12 half-bars more than 1 dB under). The p tremolo is 6-7.6 dB over the melody at 37.3, 38.3 and 39.1.
- Cause: the Tremolo row, plus Violins II's +6 gain (against +2 on the violas), plus the global p soft trim of +5. The non-tremolo Violins II is also 4 dB over the violas and celli at p (pairs at bars 8, 13, 56, 62, 68, 110, 126; median +4.2).

**Fix:**

1. `build/mix.json` Violins II: add `"soft_trim_db": {"ppp": 7, "pp": 7, "p": 2}`. This takes 3 dB off at p, about 1.5 at mp, 0 at pp and from f up. pp is unchanged, so the bar 147-155 sul tasto tremolo and the Cor anglais role keyed to it are untouched.
2. `build/roles.json` Violins II: `[144, 156, -3, 4]` and `[304, 320, -3, 4]`. Both open over 4 qn into the printed crescendos, so the arrivals at bars 40 and 82 keep their level.
3. Optional, the generic version: a `TREMOLO_DB = {"Violins II": -3}` in `score_to_parts.py`, applied in the volume envelope to single-note tremolos only (chords already get -3). It would cover future tremolos too; the roles above cover all single-note tremolos at p/mp in this score.

**Simulated with findings 2-5:**

- Bass clarinet solo margin -3.7 -> +1.9 dB (0 of 6 beats under).
- Horn 1 bars 78-79: -1.4 -> +1.1.
- Bars 37-40 melody: -3.1 -> +0.5 (2 of 12 half-bars still under, both against the celli's crescendo into bar 40).
- Delivered LRA 15.5 -> 15.4 LU, span 20.2, limiter 2.8, peak 1.440 (unchanged).

## 2. Bars 37-40: Bassoon 1's held G-flat 3 on Sus MAX plays 7.6 dB hot over the Violins I melody

**Where:** Bassoon 1, qn 144 (bar 37, Gb3, mf <, Sus MAX), and qn 280 (bar 71, Db4, f, Sus MAX).

**What is wrong (measured):**

- The bassoon's mf held note at qn 144 measures -32.9 dB. The track's other mf notes have a median of -40.5, so this note is a +7.6 dB residual.
- Bar 37.1 is 4.4 dB over the Violins I mf melody.
- `pitch_trims.json` has Bassoon 1 54 -5 and 61 -5, but only on legato notes, so the Sus MAX notes keep the hot pitch.
- The qn 280 Db4 Sus is a +6.3 dB residual at f. It is level with the Violins I melody in bar 71 (margin -1.1).

**Fix:**

- `build/note_trims.json` Bassoon 1: `{"144.0": -5, "280.0": -4}`. A note trim rather than `_all_arts_pitches`, because the 54/61 staccato and short notes at qn 382-407 were not measured hot.
- `build/roles.json` Violins I: `[144, 160, 2, 2]`. The melody across the p-to-f crescendo is not in `LEAD_SPANS`; adding (136, 160) to `LEAD_SPANS["Violins I"]` would also give its slurs the phrase-top rule.

Simulated together with finding 1: bars 35-40 melody margin -3.1 -> +0.5 dB, under by more than 1 dB in 8 -> 2 of 12 half-bars.

## 3. Bars 73-78: the flute's p espr. solo and the bass clarinet's mf "Solo" sit under the pp/p string accompaniment

**Where:** Flute 1, qn 291-300 (bars 73-75, "1." p espr. > pp, over a pp string chord and the Horn 4 pp pedal). Bass clarinet, qn 304.5-310 (bars 77-78, "Solo" mf espr., over the p tremolo chord).

**What is wrong (measured):**

- Flute 1's margin per beat is -1.2 to -4.5 dB; it is under the loudest pp stem on all 9 beats.
  - Its level is -43.2 to -46.2 dB, against celli -39.4 to -43.4, Violins II -41.4 to -44.4 and violas -40.7 (all pp).
  - Its envelope runs -0.2 -> -2.5 dB over the phrase. That is the printed decrescendo's soft ramp (`HP_SOFT_DEC_DB`), applied to a solo that starts under the accompaniment.
- Bass clarinet: see finding 1. Without the Violins II cut it is a median 4.2 dB under; with it, +0.2.
- A printed p solo over a pp accompaniment should sit about 3 dB over it (kit LEARNINGS 13: one wind equals one string section at the same p; here the solo is printed one level louder).

**Fix: `build/roles.json`.**

- Flute 1 `[291, 300, 3]`.
- Bass clarinet `[304.5, 310, 2]`.

Simulated: flute margin -2.4 -> +1.1 dB (under by more than 1 dB 9 -> 2 of 9 beats); bass clarinet +1.9 with finding 1. Delivery unchanged (both are soft passages under the ride's knee). Either one also lowers the p10 span slightly (inferred).

## 4. Bars 56-61: the c01 Horn 2 lift has gone stale; Horn 2 now covers the molto cantabile Violins I melody

**Where:** Horn 2 (with Clarinet 1, the espr. counterline in unison), qn 220-244; Violins I p "molto cantabile".

**What is wrong (measured):**

- c01 gave Horn 2 `[220, 244, 2, 2]` when it was 10.6 dB under the texture. Since then the soft trims, `HP_SOFT_EXTRA_SPANS` (Horn 2 [220,244]) and the c04 lead rules have raised it.
- Horn 2 is now:
  - -36.7 dB over the span, 4.3 dB over its unison partner Clarinet 1 (-41.0);
  - 2.9 dB under the melody on average, but over it at 57.1 (+3.1 dB) and 61.1 (+1.2 dB);
  - the loudest other stem in 7 of 13 half-bars.
- Violins I's median margin over the span is +0.1 dB.
- Horn 2's mf median over the movement is -35.4 dB, the loudest horn by 2-4 dB.

**Fix:**

- `build/roles.json` Horn 2: `[220, 244, -1, 2]` (from +2).
- With finding 1's Violins II p trim, this also takes about 2.8 dB off the Violins II chord at bar 56.1, where it is 3.1 dB over the melody.

Simulated: Violins I margin +0.1 -> +1.6 dB median (+1.9 with the Violins II trim), under by more than 1 dB 3 -> 0 of 13 half-bars. The counterline stays 4-5 dB under the melody, and Horn 2 stays its loudest voice.

## 5. Bar 175: the celli's pp G2 plays 5-8 dB over the pp chorale and its dolce trombone top

**Where:** Violoncellos qn 696 (G2, pp, 3.8 qn, Leg Slur MAX), under the Trombone 1 "pp dolce" chorale (bars 175-178, with the bass clarinet, Clarinet 1 and the pp strings).

**What is wrong (measured):**

- The note measures -36.4 / -35.0 dB at beats 2-3, against Violins II -40.7, basses -41.1 and violas -43.8. It is 5-8 dB over the other pp strings and over Trombone 1 (-43.4 to -44.2).
- Bar 175 is the one bar of the chorale where the celli lead the mix (bar level -36.5 against -42.4 to -44.0 for bars 176-178).
- It already carries the pitch trim G2 (43) -5, all articulations. The CC11 swell 37 -> 41 on the note adds the rest (inferred: kit LEARNINGS 13 notes the cello's low pitches are uneven at one layer).

**Fix: `build/note_trims.json`.** Violoncellos `"696.0": -6`; the default 0.6 s ramp suits a pp entry.

Simulated: Trombone 1 margin at bar 175 -6.2 -> -2.8 dB. The celli are no longer the loudest; Violins II is, by 2.5-3.2 dB.

## 6. At ff the oboes sit 3 dB under the flutes and clarinets at the same onsets

**Where:** Oboe 1/2, every ff tutti (bars 26-32, 82-83, 116-123, 131-142, 160-161).

**What is wrong (measured):**

| Oboe 1 minus | f | ff | fff |
|---|---|---|---|
| Flute 1 | -0.1 dB (n=38) | -3.1 (n=98) | -2.7 (n=9) |
| Clarinet 1 | -1.0 (n=24) | -2.8 (n=58) | |

- Oboe 1's ff median is -35.1 dB, against Flute 1 -31.4 and Clarinet 1 -31.2. The step from f to ff is 1.8 dB on the oboe and 5.6 dB on the flute.
- The c01 trims (f 2 / ff 4) fixed the f level but not ff. Rimsky-Korsakov's forte table puts the oboe level with the flute and clarinet. In the ff wind chords the oboe colour is lost under the flutes (inferred).

**Fix: `build/mix.json`.** Oboe 1 and Oboe 2 `dyn_trim_db` ff 4 -> 6 (f stays 2).

Simulated alone: master peak 1.440 -> 1.455; delivered LRA 15.5, span 20.3, limiter 2.8 dB (unchanged). If it is combined with other loud changes, check the bar 160 peak list.

## Dan's two checks (measured)

**Loop pulsing.** Autocorrelation at 3.95 s of the 100-300 Hz level / the spectral centroid:

| Passage | Stem | 100-300 Hz | Centroid |
|---|---|---|---|
| Final chord, qn 712-728 | Master | -0.10 | -0.03 |
| Final chord, qn 712-728 | Each string stem | -0.10..+0.13 | -0.11..+0.12 |
| Opening roll, qn 0-16 | Timpani | -0.04 | -0.06 |
| Final roll, qn 720-728 | Timpani | -0.11 | -0.18 |
| Tam-tam fff | Tam-tam | -0.08 | -0.36 |
| Coda chorale, qn 696-712 | Celli | +0.12 | +0.17 |
| Coda chorale, qn 696-712 | Trombone 1 | +0.04 | +0.17 |
| qn 720-728 | Horn 4 | +0.93 | +0.70 |

Horn 4's ppp G3 is the only stem that still pulses, and it sits about 15 dB under the master in that band. That is critic A's to judge.

**Accents.** 2-5 kHz energy in the first 80 ms minus the body, median (p90):

| Stems | Median (p90), dB |
|---|---|
| Trumpets 1/2/3 | -6.0 (-4.3) / -11.5 / -13.5 |
| Trombones | -9.6 to -12.4, p90 at most -5.1 |
| Horns 1/3 | -4.7 (+3.6) / -0.1 (+2.6) |
| Strings | -2.7 to -2.8 |
| Woodwinds | -4.2 to -5.1, p90 at most +2.1 |

No accent comes near a 7-13 dB burst.

## Checked and not proposed (measured)

- **Low end at the loud tutti.** 100-250 Hz is 4-5 dB light against the Dvořák reference (loud frames 100-160 Hz -15.5 against -10.8). Bass-octave roles of +2-2.5 dB at bars 82, 122 and 160 simulated only +0.7 dB there, raised 20-100 Hz by 0.8 and the limiter 2.8 -> 3.0. Not worth it against one lossy reference.
- **Lowering pp toward p everywhere.** The global soft trims put pp +2 dB over p (7 against 5); global pp 7 -> 5 simulated span 20.2 -> 20.7 dB, the wrong way. Solo roles (findings 3-4) are the better route.
- **The bars 167-170 theme** (Trumpets/Horns a2 + violas ff): its three stems are the top three in every half-bar of 167-168.

**Combined simulation of findings 1-5** (`s_all.json`): delivered LRA 15.4 LU, span 20.2 dB, limiter 2.8 dB, peak 1.440; climax order unchanged (no change after qn 320 except bars 175 and 56-61).

**Do not touch:** the trumpet `dyn_trim_db` (f/ff ratios with horns and trombones are right); the c04 fff brass roles and the climax order (160 > 122 > 169); the percussion gains, keys and timing; the global soft trims 7/7/5 and the per-track pp overrides of violas, basses and bassoons (at pp the violas sit level with Violins II and the celli, and the basses 4.9 dB under them); the Cor anglais [586,620,+4] and Violins II [584,619,+2] roles (pp, untouched by finding 1); the bars 127-130 Clarinet 1 roles; brass, wind and string GENTLE_ACCENT; the basses' EQ and loud_eq.
