# Cycle 14, critic B: balance and levels (render c13)

## Method

All numbers come from the stem-fixed c13 render (`cycles/c13/render/`, 33 stems). They are mapped through `build/parts.json`, which is dated 14:40 and matches the stem fix. Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c14-B/`: the c13-B set plus these:
- `fam.py`, `xfam.py`, `xdyn.py`: per-dynamic levels and cross-family pairs.
- `uniq.py`: undoubled lines.
- `cbp.py`, `cbb.py`, `lowcmp.py`: basses and low bands.
- `swell.py`: notes that swell by themselves.
- `wend.py`: Horns a2 window ends.
- `simsoft.py`, `simaud.py`, `stl.py`, `spots.py`: simulations.

Definitions:
- **Level:** K-weighted power in 10 ms hops, as in c13-B.
- **re master:** the stem minus the master over the same window.
- **Pairs:** two stems that both hold a note through a 1 qn window.
- **Audio simulation (`simaud.py`):** the stems are post-fader and sum to the master, so the simulated master is the c13 master plus Σ stem × (gain - 1), sample-exact. The result is run through `tools/deliver_master.py`. Baseline on the c13 master: LRA 14.2 LU, span 18.5 dB, limiter 2.3 dB.

## What holds (measured)

**Section balance at f and louder matches Rimsky-Korsakov's resonance table (Principles, "Comparison of resonance").** Pair medians, same printed dynamic:

| Pair | Measured (f / ff / fff) | RK |
|---|---|---|
| Horn - single woodwind | +2.3 / +2.8 / +3.6 | Horn = 2 woodwinds, +3 |
| Trumpet - woodwind | +6.0 / +4.3 / +5.0 | +6 |
| Trombone/tuba - woodwind | +6.2 / +5.4 / +5.7 | +6 |
| Trumpet - horn | +2.8 / +2.7 / +1.7 | +3 |
| Low brass - horn | +2.4 / +2.0 / +2.3 | +3 |
| Trumpet - trombone | about 0 | 0 |
| String section - woodwind | +4.8 / +4.6 / +5.2 | +3 |

The strings run about 2 dB over RK at f and louder; that is acceptable, since they carry most of the melody.

**The new trumpet tracks** (trumpet pairs, f / ff / fff):

| Pair | f | ff | fff |
|---|---|---|---|
| Trumpet 1 - Trombone 1 | -0.5 | +2.2 | -0.5 |
| Trumpet 2 - Trombone 2 | 0.0 | -0.2 | -1.1 |
| Trumpet 3 - Bass trombone | +0.2 | -0.6 | -0.9 |
| Trumpet 1 - Oboe 1 | +2.6 | +3.3 | +1.8 |

Same-dynamic medians are +0.8..+2.9. Their only soft notes (bars 113-114, pp cresc.) sit 15-26 dB under the master, as an entry under an mp crescendo should.

**Percussion:** unchanged from c13-B and still in proportion:
- Tam-tam fff (bar 122): perc group -8.7 re master.
- Crash at 636: -13.9 re master in bar 160.
- Sus. cymbal pp roll in bar 159: -23.8.

**Climax order** (delivered 3 s maxima): 160 -10.2 > 122 -10.8 > 167-170 -12.9.

**Dan's checks for this lens:**
- *Accent attacks* (2-5 kHz, first 80 ms minus the body, all printed accents):

  | Family | Median | Notes over +3 dB |
  |---|---|---|
  | Brass | -7.2 | 2 of 145 (Tpt1 284 +4.7, Tpt1 676 +4.6) |
  | Winds | -6.1 | 6 of 220 |
  | Strings | -4.1 | 7 of 192 |

  The +6..+16 outliers at qn 536 are the ff-to-mf tail artefact noted in c13-B.
- *Loop pulsing:* 8 unsplit notes are 6 s or longer. The worst is Bass clarinet 11.0 (100-300 Hz autocorrelation 0.81), with only 1.9 s of overlap at the 3.95 s lag, so the reading is unreliable. The master over 464-500 / 696-728 / 712-728 reads band -0.22 / -0.34 / -0.55, centroid -0.13 / -0.10 / -0.02. Nothing here is a balance problem.

## 1. String pp sits above string p in the soft trims, so pp string accompaniment is level with or over p solos (measured; fix simulated)

**Where.** Every soft passage. The worst spots:
- Bars 43-45: the Horn 1/2 p phrase and the Oboe 1 p solo.
- Bars 53-54.
- Bar 107.
- Bars 153-155: recap second theme.
- Bars 175-178: the pp dolce trombone chorale.

**What is wrong.** RK: "in piano passages" one string department equals one wind instrument. Measured, string section minus wind/brass:

| Dynamics compared | Median | Windows where the string is louder |
|---|---|---|
| String pp vs wind pp | +1.9 dB (418 windows) | 71% |
| String p vs wind p | +2.1..+2.6 | |
| String pp vs wind/brass p (one level louder) | -0.7 dB (118 windows) | 46% |

Horns minus strings at p is -3.3, at mp -3.5.

**Cause** (`build/mix.json`): the soft trims lift pp more than p.

| Track | pp | p |
|---|---|---|
| Global (Violins I and Violoncellos use it) | +7 | +5 |
| Violas | +9 | +5 |
| Violins II | +7 | +2 |

On Violins II this adds to the c03 stem-fix role `[584,619,+2]` over the recap's pp sul tasto tremolo. There the melody group's margin over Violins II falls to 3.5-6 dB in bars 153-155, against 7-15 dB in the exposition (bars 47-55).

**Fix:**
- `build/mix.json` tracks, `soft_trim_db` overrides:
  - Violins I: `{"ppp": 6, "pp": 6, "p": 5}`.
  - Violoncellos: `{"ppp": 6, "pp": 6, "p": 5}`.
  - Violins II: `{"ppp": 6, "pp": 5, "p": 2}`.
  - Violas: `{"ppp": 5, "pp": 6, "p": 5}`.
- `build/roles.json` Violins II: delete `[584, 619, 2]`.
- Double basses stay as they are (pp -2.1 under the celli already).

**Simulated** (`simaud.py`, audio-exact):
- String pp minus wind pp: +1.9 -> -0.1 dB.
- String pp minus wind p: -0.7 -> -3.2 dB; louder share 0.46 -> 0.35.

Solo minus the loudest string, per qn median (minimum):

| Spot | c13 | Simulated |
|---|---|---|
| Bars 43-44 horns | -4.9 (-8.1) | -2.9 (-6.8) |
| Bar 45 oboe | -0.5 (-4.4) | +0.5 (-2.4) |
| Bar 54 Cl1/Vc | +4.5 (-1.2) | +5.9 (+0.8) |
| Chorale 175-178 | +1.0 | +2.0 |

Delivered file: LRA 14.2 -> 14.7 LU, span 18.5 -> 18.9 dB, limiter 2.3 dB (unchanged), climax maxima unchanged to 0.1 dB. The soft passages' 3 s maxima move 0.0..-0.2 LU; only bars 179-182 move -0.7, which suits the printed morendo.

## 2. Bar 43: a Violins II pp note swells 12 dB by itself and covers the horns' p phrase (measured; fix inferred)

**Where.** Violins II C#4 (sq 168, moved onset 167.748, Sus MAX), qn 168-172. Horns 1/2 p, bars 43-44.

**Evidence:**
- CC11 falls to 32-34 (pp) and stays there; vol_db is flat at 0.
- The stem nevertheless rises from -45.8 dB (abs, qn 168) through -41.9 (169) and -39.0 (170.5) to -33.7 (171.5).
- At 171-171.5 Violins II is the loudest stem: -2.6 / -1.4 re master. Horn 1's p phrase sits at -42.2..-42.8 abs, so it is 5-8.5 dB under the pp chord.
- The violas' B-flat3 in the same chord bumps +5 dB at 169.5 (-38.3 against -43 around it).
- This is a sample bloom at a flat controller (kit LEARNINGS section 4, "Some samples swell by themselves").

**Fix:** `build/score_config.py` `LEVEL_SHAPES["Violins II"]`, moved-onset times, holding the note at about its qn-169 level. Add the shape `[(169.25, 0), (169.75, -2.5), (170.5, -3.5), (171.0, -5.5), (171.4, -9), (171.9, -9), (172.0, 0)]`. The next note starts at 172.0 on Leg Slur (keyswitch at 171.94), so the release must not start before 171.95.

Optional: Violas `[(169.25, 0), (169.5, -4), (169.9, -4), (170.2, 0)]`.

**Target:** Horn 1 2-3 dB over the chord through bars 43-44. Measure the stem against this table after the render.

## 3. Exposition ff tutti (bars 27-32): the basses' eighths are 6-9 dB under the same bars in the recapitulation (measured; fix simulated)

**Where.** Double basses, qn 104-128, against bars 131-134 (qn 520-536), which have the same ff C2 eighths under the same theme.

**Evidence.** Same pitch C2, ff, first 0.2 s of each eighth:

| Bars | c13 | c12 (Sus MAX) |
|---|---|---|
| 27-28 (exposition) | -35.2 dB | -34.9 dB |
| 131 (recapitulation) | -26.6 dB | -29.0 dB |

Bars 28-31 (D2/E-flat2/E2/F2) read -34.2..-39.4.

Per bar in the exposition:
- Cb re master -18.0 / -21.5 / -19.6 / -22.9 / -18.9, against -9.4..-15.1 in bars 131-134.
- Cb minus celli -2.2 / -7.5 / -7.0 / -8.7 / -10.4.
- Master 60-100 Hz re K -21.5, against -18.2 in bars 131-134; 160-300 Hz -10.4 against -7.8.

Causes:
- The recap's basses carry the crescendo hold gain into 131 (vol_db +3.5..+7 against +0.5..+1 in 104-124). Bar 27 is a ff arrival with no hairpin into it (kit section 4: "Check every ff arrival that has no hairpin into it").
- The basses' `loud_eq` (160 Hz +6) is off in bar 27: points `[103,1],[104,0],[108,0],[110,1]`.
- The c13 Detache test cost another 1.5-3 dB.

**Fix:**
- After the planned Detache revert, `build/roles.json` Double basses: add `[104, 128, 3, 1]`.
- `build/mix.json` Double basses `loud_eq.points`: delete `[104, 0]` and `[108, 0]`, so the wet stays 1 from 94 to 127.

**Simulated** (+4 dB on c13, close to +3 with the revert):
- Cb re master per bar +3.9.
- Cb minus celli +1.8 / -3.5 / -3.0 / -4.7.
- Master K +0.03..+0.10 dB.
- Master 60-100 Hz re K +3.5 dB in bars 27-29 and 31.

**Target:** Cb within 3 dB of bars 131-134 re master, and Cb minus celli -1..-3 in bars 28-31.

## 4. Horns a2: the c13 per-window roles end in the middle of held notes; at 314.5 the phrase-end half note jumps 5 dB over the next entry (measured)

**Where.** Horns a2. Measured step across each window end (0.25 s before/after):

| Window end | Note it cuts | Step |
|---|---|---|
| 314.5 | E4 314-316 | +5.1 dB |
| 404.5 | 404-406.1 | +3.0 |
| 480.5 | 479-484.1 | +2.4 |
| 676.5 | fermata | +1.6 |

**What is wrong at 314.5 (bar 79).** The horns' mf phrase ends on a slurred half note E4 that follows a same-pitch E4 eighth. The -1.3 dB window role releases at 314.5, and the note blooms besides:
- It reads -33.9 / -30.2 / -29.8 / -30.0 dB abs at 314 / 314.5 / 315 / 315.5.
- It is the loudest note of the horns' phrase (the phrase peak at 311 is -31.9).
- At 314.5-316 it is the loudest stem (-1.6..-2.2 re master).
- It sits 6-8 dB over Oboe 1 and Violins I, whose mf phrase enters at 312.5 (-38.0..-38.7 / -36.4..-37.8 abs).

The other three steps are inside f/ff tutti, 10-11 dB under the master, and inaudible.

**Fix:**
- `build/roles.json` Horns a2: end each window row at the end of the note it cuts. Change `[272.5, 314.5, -1.3, 0.25]` -> `[272.5, 316.1, -1.3, 0.25]`, `[381.5, 404.5, -0.8, 0.25]` -> `[381.5, 406.2, -0.8, 0.25]`, `[464, 480.5, -2.4, 0.25]` -> `[464, 484.1, -2.4, 0.25]`.
- `build/score_config.py` `LEVEL_SHAPES["Horns a2"]`: add `[(314.0, 0), (314.3, -2.5), (316.0, -5), (316.2, 0)]` so the phrase end tapers under the entry.

**Target:** Horns a2 at 314.5-316 at least 2 dB under Violins I.

## 5. Coda tutti (bars 167-170): the bass has no fundamental; 60-100 Hz is 6-9 dB under every other tutti (measured band; cause inferred)

**Where.** qn 664-680: Cb f eighths on C2, tuba C2, contrabassoon C1.

**Evidence.** Master 60-100 Hz re K by tutti:

| Bars | 60-100 Hz re K |
|---|---|
| 167-169 | -27.5 |
| 170 | -26.6 |
| 27-31 | -21.5 |
| 69-72 | -20.0 |
| 131-134 | -18.2 |
| 139-142 | -18.6 |
| 158-161 | -17.9 |

- The basses supply that band: their share is -0.7 dB, and the tuba's share is -12.
- Bass C2 eighths in the 60-100 Hz band:

  | Bars | 60-100 Hz | K | Fundamental re K |
  |---|---|---|---|
  | 167-169 (f) | -45.8 dB | -31.4 | -14.4 |
  | 131-134 (ff, same pitch) | -36.4 | -27.0 | -9.4 |

- The c13 row `[664,680,1.5,0.5]` lifted the whole stem (63-250 Hz re 500-2000 Hz met critic C's -8.1 target at -7.1), but the fundamental is missing. Inferred: it is the f layer's spectrum.
- A listener hears the final Allegro tutti as lighter in the bass than the climaxes before it, though only the theme is ff.

**Fix (inferred; check against critic C's low-band numbers):** `build/mix.json` Double basses: add a second `loud_eq` spec, `{"points": [[662, 0], [664, 1], [679, 1], [680, 0]], "bands": [{"band": "bell", "hz": 66, "db": 4, "bw_oct": 0.6}]}`. The kit (section 14) supports a separate wet-automated EQ per spec.

**Target:** master 60-100 Hz re K about -21 in bars 167-170. The 63 Hz third-octave of the whole file should not rise more than 0.3 dB.

## Do not touch

- Brass, wind and string ratios at f/ff/fff (the RK table above).
- The trumpet f/ff/fff anchors and the c13 fff trims of Trumpets 2-3 and Horns 3-4.
- Percussion gains, patches, roles and timing (tam-tam fff and pp, crash, sus. cymbal).
- The climax order (160 > 122 > 169) with `FAST_CAP_ABOVE` 4 and top ride 1.6.
- `accent_fits.json` (accent fronts are within the rules).
- `TIMP_CC1_MAP` with `TIMP_ROLL_TRIM_DB`.
- The second-theme `HP_TARGET_AT` set and the bars 23-25 / 135-137 roles.
- The c13 coda 672-676 rows and final-chord rows.
- `_REBOW_FROZEN` / `rebow_fills.json`.
- The Double basses' soft trims.
