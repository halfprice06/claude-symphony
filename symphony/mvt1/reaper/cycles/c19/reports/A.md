# Cycle 19, critic A: articulation and phrasing (render c18)

Scope: every wind, brass, string, harp, timpani and percussion note in `build/parts.json` (the c18 build after its stem fix; MIDI identical to c17), measured on the c18 stems and master (`cycles/c18/render/`).

Scratch: `/private/tmp/claude-501/mockup-loop/mvt1-c19-A/`.
- The c18-A battery was rerun on c18. Outputs are `o18_*.txt`; 5 ms feature frames are in `feat_c18/`.
- New scripts:
  - `cand.py`: string join holes with the 30 ms spike check;
  - `a536.py`: the bar-135 accents against the next note;
  - `vtrip.py`: the viola triplets at letter G;
  - `mt.py`: multi-stem traces.

## Checks that passed (measured)

- **Legato.**
  - No chord is sent to a Leg row (`chordleg2`: 0).
  - Wind and brass joins: none at 6 dB or more.
  - Trumpet 1 279: the c18 notch took the join to -0.1 dB, with no spike left (`joins`).
  - Violins I 279/626/720 now dip at most 1.9 dB (`jfill`).
- **Tenuto/portato joins.** -1.5..+1.9 dB on the 200 ms window (`ten200`).
- **Accent fronts (item 8).** 2-5 kHz in the first 80 ms minus the body: brass median -8.1 dB (max +4.3, Horn 3 317/321), winds -5.7 dB. The string outliers, Violas 536 (+15) and celli 536 (+8.4), are the release of the preceding f dyads falling into the front window. See #3.
- **Accent shape** (`accshape`).
  - Brass front-body +1.9 dB, winds +1.0, strings +0.8 (c17: -1.1). The c18 body cuts helped, but strings still miss the +2 target. See #1.
  - String peak minus preceding notes: median +4.5 dB, 28 over 6 dB (c17: 4.7 and 30).
- **Re-bows and loop pulsing (item 7).**
  - No new re-bow step. The largest steps are the printed sf > mf (celli 163.9) and the morendo (727).
  - No held note within 6 dB of the master pulses at the loop period with more than 3 dB of swing (`longloop`). Bass clarinet 11 sits at -4.4 dB re master with 1.4 dB of swing.
  - The harp values in that table are decaying plucks, not loops.
- **Other techniques.**
  - String staccato separation: medians 9.8-14.3 dB.
  - Tremolo joins: median -0.8 dB, 1 of 33 at 4 dB or more.
  - Pizzicato reaches -3 dB of its peak at +0.02..+0.06 s.
  - Detach holes: brass -5.0 dB, winds -5.6 dB.
  - Ties on the timpani and basses are held.
  - The violas' release thump at 526.5-534.5 is gone (`vla`; no post-off burst over the body).
  - Breath marks dip 3-15 dB. The Horn 1/2 rows at 475/636 read 0 only because those notes play on Horns a2, whose stem dips 4-6 dB at both.

## 1. Accented string notes on Leg BC MAX start in the transition sag; the same accents on Sus MAX have weight

**Measured** (`accshape.json`, string accents of 0.75 s or more within 12 dB of the master, front = onset..+0.15 s, body = +0.45..+0.75 s):

| Row of the accented note | n | front-body median | front under body |
|---|---|---|---|
| Sus MAX (fresh stroke) | 15 | +1.6 dB | 5 |
| Leg BC MAX (bow-change legato target, moved 0.11-0.17 s early) | 18 | -0.2 dB | 9 |

Worst Leg BC cases, front-body / mid-body (+0.15..+0.4 s) in dB:

| Note | Front-body | Mid-body | Stem re master |
|---|---|---|---|
| Violoncellos 321 (bar 81) | -5.9 | -7.0 | -9.6 |
| Violoncellos 91 (23) | -4.9 | -3.6 | -10.6 |
| Violoncellos 539 (135) | -3.3 | -2.3 | -10.4 |
| Violins I 154 (39) | -3.1 | -2.4 | -8.2 |
| Violoncellos 317 (80) | -2.7 | -0.9 | -5.5 |
| Violins I 548 (138) | -2.3 | -1.9 | -11.9 |
| Violins I 533 (134) | -2.2 | -1.4 | -11.6 |
| Violins I 100 (26) | -1.8 | -1.5 | -10.0 |
| Violins I 142 (36) | -0.4 | -1.0 | -6.7 |

- Celli 321's -7.0 mid-body is a 7 dB hole inside the accented note.
- Celli 317/321 double the f horn entry of bars 80-81 and sit 5.5 dB under the master.
- c18's body cuts (accent_bodies.json, Vln I 533/142 at -3) did not fix these. A body cut lowers the late part of the note but cannot fill the transition sag at the front.

**Inferred.** An accent on an unslurred note is a new bow with weight. The bow-change legato transition does the opposite: it hides the change, and the sample sags for 0.15-0.4 s. The c06/c11 strokes (Vln I 57/65/78/113/479) show that the stroke path works in this movement.

**Fix:**
- `build/score_config.py`: `DOWNBOW_STROKE_AT` add:
  - Violoncellos 91.0, 317.0, 321.0, 539.0;
  - Violins I 100.0, 142.0, 154.0, 533.0, 548.0.
  - These become fresh Sus MAX strokes on the Leg -> Sus entry path, and the next note joins from each one as a Leg BC target.
- Remove these notes' rows from `build/accent_fits.json` and Violins I 533/142 from `build/accent_bodies.json`.
- Refit after the render: `fit_accents.py --family string` and `fit_accent_bodies.py`.
- Check that the next note's join holes stay at 5 dB or less (`joins.py`).

**Pass:**
- These nine notes: front-body at least +1.0 dB, and none with mid-body under -2.
- String accent front-body median at least +1.5 dB.
- 2-5 kHz front minus body at most +2 dB on each.

## 2. String legato holes of 6-11.5 dB on joins no fill covers; on celli 365/369 the pair release falls into the sag

**Measured** (`cand.py`; hole = the lower of the two bodies minus the 30 ms minimum; span = where the level is 3 dB or more under, from the moved onset):

| Track, note (bar) | Hole | Span | Min at | 30 ms peak over body | Stem re master |
|---|---|---|---|---|---|
| Violoncellos 365 (92) | 11.5 | +0.14..+0.43 | +0.34 | +1.0 | -12.9 |
| Violoncellos 369 (93) | 9.5 | -0.02..+0.35 | +0.20 | +1.0 | -12.0 |
| Violas 72 (19, espr. phrase start, mf) | 8.5 | +0.04..+0.31 | +0.11 | +2.1 | -10.8 |
| Violas 180 (46) | 8.2 | -0.10..+0.40 | -0.03 | -1.8 | -12.4 |
| Violins II 296 (75) | 7.1 | -0.03..+0.38 | +0.34 | +0.9 | -10.6 |
| Violins II 405 (102) | 6.5 | +0.03..+0.28 | +0.24 | +1.3 | -13.5 |
| Violins II 236 (60) | 6.2 | +0.08..+0.39 | +0.19 | +0.9 | -10.9 |
| Violas 517 (130) | 5.3 | +0.03..+0.29 | +0.19 | +1.2 | -12.8 |

- Violas and Violins II are not in `build/auto_fills.json` `tracks`, so these joins have never been filled. All of them repeat from c17 within 0.7 dB (`o17_joins` / `o18_joins`).
- The celli are listed, but 365 and 369 have no fill. Both are the second notes of two-note sighs (E-flat3 tied -> D-flat3, C3 tied -> B-flat2). `SLUR_PAIR_RELEASE` writes -5.0 -> -7.5 dB from 364.75 to 364.958 (and 368.75-368.957), which is moved onset +0.10 s. That puts the fall inside the transition sag that LEARNINGS section 6 says not to stack into.
- Violas 72 opens the violas' espr. phrase (B3 -> A-flat4 after two tongued B3s). The trace dips from -39 to -47.5 dB just before the beat and reaches the body only at +0.4 s.
- Left out: Violas 612, celli 112/215, Violins I 480, Violins II 637. Their 30 ms spikes sit 2.6-4.7 dB over the body, so a fill would add to the spike (LEARNINGS 6).

**Fix:** `build/early_fills.json` hand entries (times from the moved onset; dB = hole - 3, cap 6). List them in auto_fills `--exclude`.
- Violoncellos:
  - `"365": {"db": 6.0, "pre_s": -0.10, "hold_s": 0.43}`
  - `"369": {"db": 6.0, "pre_s": 0.0, "hold_s": 0.35}`
  - plus `SLUR_PAIR_RELEASE_DB_AT` `{"Violoncellos": {365.0: -1.0, 369.0: -1.0}}`.
- Violas:
  - `"72": {"db": 5.0, "pre_s": 0.0, "hold_s": 0.31}`
  - `"180": {"db": 5.0, "pre_s": 0.10, "hold_s": 0.40}`
  - `"517": {"db": 2.5, "pre_s": 0.0, "hold_s": 0.29}`
- Violins II:
  - `"296": {"db": 4.0, "pre_s": 0.03, "hold_s": 0.38}`
  - `"405": {"db": 3.5, "pre_s": 0.0, "hold_s": 0.28}`
  - `"236": {"db": 3.2, "pre_s": 0.0, "hold_s": 0.39}`

All of these are level-only, so `stem_fix.py` can apply them.

**Pass:** each listed hole at 4.5 dB or less, and no 30 ms peak from the fill's start to +0.6 s more than 2 dB over the louder body.

## 3. Bar 135 (recapitulation, qn 536): the mf accent that starts the crescendo is no louder than the next note on the violas and 3.5 dB under it on the contrabassoon

**Measured** (`a536.py`; body +0.15..+0.40 s of the accented note minus the same window on the unaccented same-pitch note at 537):

| Track | 536 minus 537 | accent_fits row |
|---|---|---|
| Violas | +0.2 | [0.0, -3.91] |
| Contrabassoon | -3.5 | [0.0, -4.34] |
| Violoncellos | +5.9 | 4.5 |
| Violins II | +2.9 | 4.5 |
| Double basses | +1.3 | 4.5 |
| Bassoon 1 | +1.2 | none |

- The score (page 13, bars 135-136) prints accent, mf, cresc. on all six, and the same figure again at 539 and 542.
- The fitter put negative steps on Violas and Contrabassoon 536. The violas' f dyads end exactly at 536.0, and their release is in the accent's front window: the stem falls from -30.5 at 535.98 to -43 by 536.22. The same release gives the false +15 dB 2-5 kHz front (inferred).
- The fitter therefore read the accent as too loud and cut it. The accent's volume now drops to -5.9 dB while 537 sits at -1.7.

**Fix:** `build/accent_fits.json`:
- `Violas "536": 3.0`
- `Contrabassoon "536": 3.0`
- `Violoncellos "536": 2.5`
- Add all three to the `fit_accents.py --skip` list.

Level only (`stem_fix.py`).

**Pass:** 536 minus 537 at +2..+4 dB on Violas, Contrabassoon and Violoncellos, with Violins II, Basses and Bassoon 1 unchanged.

## 4. Horns a2, bars 78-79 (the a2 lead line, mf): an 8 dB hole on the F-sharp4 eighth, and a fill that starts after the hole before the accent

**Measured** (`trace.py`, `mt.py`, `efchk2`; Horns a2 is the loudest stem here, at -2..-8 dB re master):
- **312.5.** The F-sharp4 starts a new slur after the tied G4. It plays the Sus row (`SLUR_START_SUS`, v73) and sags:
  - G4 tail -34.0 dB;
  - F-sharp4 minimum -42.5 at 312.59 (0.13 s after its moved onset 312.393);
  - F4 -33.0.
  - The master dips 2.6 dB (32.2 -> 34.8) inside one mf line.
  - `ssj`: the second note's body is 8.6 dB over the first, the worst brass slur start.
- **311.** The accented G4 after the B3 pickup dips to -40.2 at 310.88 (pickup -35.0, accent -31). The existing fill (+2.7 dB, pre_s -0.079) starts 0.08 s after its moved onset. `efchk2` puts the minimum at -0.04 s, before the fill.

**Fix:** `build/early_fills.json`, Horns a2 (hand entries, `--exclude`):
- `"312.5": {"db": 5.0, "pre_s": 0.0, "hold_s": 0.22}`. The 30 ms peak after it, at 312.93, is +0.2 dB over the F4 body, so there is no spike.
- `"311": {"db": 3.5, "pre_s": 0.05, "hold_s": 0.18}`.

**Pass:**
- F-sharp4 minimum within 4 dB of the G4/F4 bodies.
- The 311 transition within 3 dB of the pickup.
- The accent's front-body unchanged (±1 dB).

## 5. Test: viola triplets at letter G (bars 117-121, qn 464-484) blur into a wash

**Measured** (`vtrip.py`).
- What is played: 60 unslurred f triplet eighths (0.159 s each), all on Sus MAX, 0.3 qn, v80.
- Each onset's 20 ms peak minus the trough before the next onset:
  - median 3.7 dB, p10 1.1, p90 6.2;
  - the string staccato elsewhere separates by 9.8-14.3 dB.
- The violas sit 17.9 dB under the master here, so this is an inner motor figure under a ff tutti.

**Inferred.** In a hall these triplets would be heard as détaché rhythm. Here they read as a sustained buzz, which flattens the drive of letter G. The effect is modest because the figure is under the tutti.

**Fix (test, one track):**
- `ART_SPANS` Violas 464-484 -> `Stac On Bow RRx9` at the written length. It is a row load, so a full Violas rebuild. Stac On Bow passed on the celli measured tremolo in c15.
- Keep the level with a role, so that the violas over 464-480 stay within 1 dB of c18.

**Pass:** onset separation median at least 6 dB, and 2-5 kHz front minus body at most +2 dB. If not, revert.

## Patches

- One new test: `Stac On Bow` for the letter-G viola triplets (#5).
- The deferred Marc Sus LITE test for string accents is replaced by #1. The Sus MAX stroke already gives +1.6 dB of front weight with no extra row.
- No other patch change is indicated. Tuba and contrabassoon have no slurs. The trumpets' Sus Non Vib / Leg Slur rows and the Horns a2 patch are measured correct above.

Do not touch:
- brass and wind `GENTLE_ACCENT` swells (front-body +1.9/+1.0 dB, 2-5 kHz fronts -8.1/-5.7);
- `accent_bodies.json` except the two Leg BC rows named in #1;
- the c18 Violins I fills at 279/626/720, the Trumpet 1 279 notch and the violas' release notches;
- `PORTATO_JOIN_AT`/`PORTATO_JOIN_NOTCH`; `SYNCO_SHAPE`; `PICKUP_LIFT`;
- `_REBOW_FROZEN`/`REBOW_AT` with `rebow_fills.json`;
- `MEAS_TREM` alt_row; `TREM_JOIN`/`TREM_SPLIT`;
- `WIND_DETACH` with the brass dip; `SLUR_START_SUS` and `RETONGUE_LEAD_S` (only the one fill in #4);
- the staccato, pizzicato and tremolo rows;
- harp `env_release_ms` with `HARP_RING_S`/étouffez;
- `PORT_TARGETS`; `TIMP_CC1_MAP` with `TIMP_ROLL_TRIM_DB`;
- the percussion keys and timing;
- the Horns a2 windows, roles and shelves;
- the climax order (160 > 122 > 169).
