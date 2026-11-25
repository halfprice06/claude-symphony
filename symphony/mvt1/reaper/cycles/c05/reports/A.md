# Cycle 5, critic A: articulation and phrasing (render c04)

Scope: every string, wind, brass, timpani and harp note in `build/parts.json` (the c04 build), measured on the c04 stems (after the stem fix) and the master. Scripts and 5 ms feature files are in `/private/tmp/claude-501/mockup-loop/mvt1-c05-A/`. The new scripts are:
- `xover.py`, `xall.py`, `legafter.py`: pitch crossover. This is the time after the score onset at which the new note's first five harmonics (±35 cents) carry more energy than the old note's. "Dip" is the lowest 30 ms level within -0.1..+0.2 s, against the louder of the two note bodies.
- `samep.py`: same-pitch arrivals.
- `timpacc.py`, `rep2.py`, `rel.py`, `short.py`, `trem.py`, `stac.py`.

The c04-A scripts (`acc2.py`, `joins.py`, `rebow.py`, `longloop.py`, `breath.py`) were rerun on c04.

## Checks that passed (measured)

- **Accents, weight not bite.** I measured 2-5 kHz energy in the first 80 ms against the note body, median per track:

  | Family | Median range |
  |---|---|
  | Strings | -1.6..-5.7 dB |
  | Brass | -2.8..-16.8 dB |
  | Winds | -4.5..-11.2 dB |

  Only two notes are positive and real:
  - Horn 1 qn 665: +4.7 (ff, bar 167), the same as in c03.
  - Horn 4 qn 91: +4.7.

  The qn 536 outliers are earlier-note artefacts, as in c04-A.

  Timpani accents (v121 against v110 neighbours) peak 4-6 dB over the unaccented strokes. That is weight, as printed.
- **Legato structure.**
  - `ks_clash` is empty on every track.
  - No keyswitch has a lead under 4 ms.
  - The Leg BC/Leg Slur switches during held notes are the known working exception.
  - Wind and brass joins: median dip 0.6-4.1 dB.
- **Staccato.** Every staccato note is at half its written length (0.119 s at 126 bpm), with 5-20 dB between notes. Isolated short brass and wind notes reach peak - 6 dB at +0.02..+0.08 s.
- **Tremolo.** All 99 Tremolo notes reach body - 6 dB within 0.15 s.
- **Pizzicato.** Basses start at +0.02 s (median).
- **Releases.** Phrase-final notes fall 10 dB in 0.09-0.28 s and 20 dB in 0.24-0.57 s. No note is clipped.
- **The c04 changes work.**
  - REP_SPLIT strokes: per-note swing 4.2-6.5 dB in bars 23-25, 88-100, 111-116 and 135-139.
  - Horn 1 portato joins: worst join 3.5 dB.
  - Timpani re-strikes at qn 0, 48 and 720: centroid autocorrelation 0.26, 0.46 and 0.39.
- **Re-bows.**
  - Median dip per section: -0.9..-3.6 dB.
  - Master median dip: -1.8..-2.3 dB.
  - The residuals are listed under "Smaller items".

## 1. The theme's chromatic descent loses its arrival note: a same-pitch note at the end of the slur dies away or drops 7-17 dB (strings), or opens with an 8-12 dB hole (winds)

**Score.** The main motif ends `d''8( des''8 c''8 | c''4)`: the last eighth and the note after it are the same pitch, under one slur, with no tie. Its occurrences:
- Vln I: bars 15, 27, 35, 143.
- Vln II and Vla: bar 27 (tutti ff).
- Vla: bars 34, 167.
- Vc: bars 79, 131.
- In winds, the same figure: Ob 1 and Cl 1 bar 27; Cl 1 bars 78, 104, 128, 131; Ob 2 bar 104.

**Measured (parts.json).** Strings:
- The eighth is `short_sus`: Sus MAX, because it is a slurred note under 0.25 s.
- The arrival note is a new **Leg Slur MAX** note 0.03 qn after it.
- The merge loop in `score_to_parts.py` (about lines 1414-1444) merges same-pitch notes only when the first one is on a Leg row, so this pair is never merged.
- A Leg Slur MAX note with nothing sounding before it plays the slow first-note layer (kit section 6).

Winds: the arrival note is re-tongued on Leg Slur MAX after a 0.06 qn gap.

**Measured (stems, `samep.py`).** Level of the arrival note against the eighth before it:

| Track (qn) | +0.05..0.2 s | +0.2..0.5 s |
|---|---|---|
| Vln II 108 | -7.9 | **-16.9** |
| Vla 668 | -4.5 | **-14.9** |
| Vla 108 | -4.2 | **-14.7** |
| Vln I 108 | -4.2 | **-13.8** |
| Vc 314 | -4.2 | **-11.5** |
| Vln I 140 | -1.0 | **-10.9** |
| Vln I 60 | -2.1 | -8.6 |
| Vc 524 | -2.2 | -8.3 |
| Vla 136 | -0.6 | -8.0 |
| Vln I 572 | -1.1 | -7.5 |
| Cl 1 412 / 508 / 524 | -10.5 / -10.0 / -7.5 | -6.0 / -3.2 / -4.0 |
| Ob 1 108, Cl 1 108, Ob 2 412 | -8.5 / -9.3 / -7.1 | -0.7 / -1.8 / +6.9 |
| Cl 1 310 (half note) | -7.3 | -5.9 (end -6.9) |

**Bar 16 (qn 60), where Vln I is the only melody.**
- Vln I falls from -34.5 dB on the eighth to -44.3 dB in the second half of the quarter.
- The master falls from -30.7 to -35.9 dB.
- The c''4 dies inside its own length, and the next slur starts from near silence: b'8 at qn 61.0 dips 16.7 dB, and at qn 109.0 it dips 19.4 dB.

The c03 render shows the same thing (Vln I 108: -11.3 dB), so this is not new.

Inferred: the note on which each statement of the theme comes to rest fades as if released. At the downbeat of bar 28 the whole string section does this together.

**Fix** (`tools/score_to_parts.py`, generic, `--midi-only`):
1. **Strings.** In the c03 merge loop, also merge when `n.get("short_sus")` and the next note is the same pitch in the same slur (`o["slur"] == n["slur"]`) on a Leg row.
   - Keep `n` on Sus MAX.
   - Set `n["end"] = o["end"]` and drop `o`.
   - Write a 6 CC notch at `o["qn"]` (8 CC above CC11 90): a slurred repeat is a light pulse in one bow, not a bow change.
   - The merged notes are 0.6-1.2 s long, so no re-bow is created.
   - New flag `SLUR_REP_MERGE_SUS = True`.
2. **Winds.** New `WIND_SLUR_REP_MERGE = True`: a same-pitch note inside the same slur, after a Leg Slur note, with no tenuto and no breath, merges into the previous note with an 8 CC notch. Slurred tenutos keep the c07/c04 portato paths.
3. Re-run `auto_fills.py` for these onsets afterwards: the next note of the slur now joins from a sounding note.

**Pass criteria (c05 render).**
- Every listed string arrival is within -3 dB of the eighth before it over +0.2..+0.5 s.
- The listed wind arrivals have no dip deeper than 4 dB in the first 0.2 s.
- Master over qn 60.5-60.9 is within 2 dB of qn 59.5-59.95 (now -5.2).
- Vln I 61.0 and 109.0 dips are under 8 dB (now 16.7 and 19.4).

## 2. Unslurred short string notes that follow a Sus MAX note play as slow legato transitions: the pitch arrives at or after the end of the note (median +0.205 s on notes of 0.15-0.24 s). Part of this is a c04 regression from REP_SPLIT

**Score and parts.** An unslurred note in a monophonic string line stays on Leg Slur MAX (c02 rule). When the previous note abuts it on Sus MAX, the KS Master plays a legato transition from that Sus note at the note's own velocity (v73-91, so a slow transition; HO manual p. 91: velocity sets the legato transition time).

c04's REP_SPLIT turned the repeated notes around such neighbour notes into Sus MAX strokes, so every neighbour note now takes this path. Example: the violas' f/ff ostinato in bars 139-142, `c'8 c'8 b8 c'8 f'8 f'8 e'8 f'8 ...` (recOne.ily line 149), plays its lower neighbours (b, e, d, g, f-sharp, c-sharp) on Leg Slur MAX at v85-91.

The theme's `aes'4.-> g'8` (bars 16, 28, 36, 132, 168) has the same structure: the g'8 is unslurred after an accented Sus MAX note.

**Measured (`legafter.py`, `xover.py`).** All unslurred Leg-row string notes shorter than 0.35 s whose predecessor abuts on Sus MAX: 22 notes.
- Pitch crossover: median **+0.205 s**; 20 of 22 at +0.15 s or later.
- The violas, qn 553-567:

  | | Crossovers | Velocity |
  |---|---|---|
  | c04 | +0.155..+0.22 s (one never crosses) | v85-91 |
  | c03 render (c03 parts) | -0.005..+0.03 s | v124 Leg BC |

  So this is a regression.
- The g'8 after `aes'4.->`:
  - Vln I 63.5 / 111.5 / 143.5: +0.28 / +0.175 / +0.305 s.
  - Vln II 111.5: +0.295 s.
  - Vla 111.5 / 671.5: +0.22 / +0.22 s.
  - Vc 527.5: +0.205 s.
- Others:
  - Vln II 279.5 / 283.5 / 561.5: +0.26 / +0.20 / +0.205 s.
  - Vla 388.5 / 396.5: +0.27 / +0.165 s.
  - Vln I 83.5 / 561.5: +0.365 / +0.155 s.
- For comparison, short Sus MAX strokes on the same tracks cross at a median +0.068 s (Vla) to +0.12 s (Vln I).

Inferred: in bars 139-142 the violas' neighbour-note figure is heard as a repeated note; in the theme, the eighth that leads into the next bar is missing.

**Fix** (`tools/score_to_parts.py`, articulation pass, next to `STR_ACC_AFTER_SUS`; `--midi-only`, no new rows):
- New `STR_SHORT_AFTER_SUS = {"max_s": 0.3}`. A string note that meets all of the following plays Sus MAX as a fresh stroke:
  - not in a slur and not polyphonic;
  - written length under 0.3 s on `TEMPO_NC`;
  - its predecessor ends within 0.06 qn of its onset on a non-legato row (Sus MAX, a `rep_sus`/`rep_stac` stroke, Stac).
- Velocity: `REBOW_VEL_BY_CC` at the printed level, as for `rep_sus`.
- End: `min(0.04 qn, 10%)` early.
- Process notes in order, so that the note after one that was changed (the violas' upper-neighbour return at 553.5, 557.5 and so on, now Leg BC v124 after a Sus stroke) is checked again and also becomes a stroke.
- Keep the c06 Leg -> Sus entry path untouched.

**Pass criteria.**
- These 22 notes, plus the Violas 553.5-567.5 returns: median crossover at or under +0.08 s, and none over +0.15 s.
- Violas bars 139-142 per-eighth swing at least 4 dB.
- 2-5 kHz attack minus body of the new strokes at or below 0 dB.

## 3. Slurred string eighths at 126 bpm (`short_sus`, Sus MAX) cross 0.12 s late, about twice as late as the winds that double them

**Measured (`xall.py`).** Slurred string notes on Sus MAX (pitch steps):

| Track | Notes | Median crossover | p75 |
|---|---|---|---|
| Violins I | 75 | +0.12 s | +0.165 s |
| Violins II | 35 | +0.12 s | +0.14 s |
| Violoncellos | 19 | +0.095 s | |
| Violas | 58 | +0.068 s | |

For comparison, Violins I on a Leg row cross at +0.05..+0.065 s.

Bar 27 (qn 106.5-107.5), the theme in unison at ff:

| Instrument | Crossover |
|---|---|
| Fl 1 | +0.035..+0.05 s |
| Ob 1 | -0.05..+0.06 s |
| Cl 1 | +0.06..+0.095 s |
| Vln II | +0.01 / +0.12 / +0.14 s |
| Vla | +0.05 / +0.085 / +0.14 s |

An eighth lasts 0.238 s.

Inferred: on every chromatic eighth of the theme the strings change pitch 0.06-0.1 s after the winds, so the doubled line blurs. Kit section 5 lists a 90-120 ms lag left after the c03 change to Sus MAX; no lead on these notes was tried.

**Fix (test).**
- New `SHORT_SUS_LEAD_S = 0.05` in `score_to_parts.py`: every `short_sus` note that is not the first of its slur starts 0.05 s early, converted with `qn_to_sec` going back from the onset. The previous note's end does not move, so the 0.03 qn crossfade overlap grows by the lead.
- Apply it to Violins I and II only (`SHORT_SUS_LEAD_TRACKS`); Violas and Violoncellos are the control.
- No velocity or CC change.

**Pass criteria.**
- Vln I/II `short_sus` median crossover at or under +0.07 s.
- No new dip of 6 dB or more.
- Accent 2-5 kHz medians unchanged within 1 dB.

## 4. Portamento on the two expressive leaps that HO can play with Leg Port MAX: the coda cello solo (qn 685) and the "sul A" sixth of the violins' cantabile tune (qn 225)

**Measured.**
- **Violoncellos 685.0** (bar 172, the "espr." coda solo, C4 -> A-flat4, a slurred minor sixth up, v124 Leg Slur MAX):
  - The join dips 7.4 dB (`joins.py`), from -41 to -52 dB for 0.1 s.
  - The A-flat then needs 0.4 s to reach -38 dB.
  - The celli are the loudest stem here, 2.7 dB under the master (qn 680-696).
  - The next joins also dip: 687.0 by 5.4 dB and 691.0 by 5.2 dB.
- **Violins I/II 225.0** (bar 57, `aes'4 f''2--` under the "sul A" spanner):
  - Joins are fine (1.0 / 0.3 dB).
  - The whole tune is played with the fastest transitions (all string legato targets above CC11 40 are v124).
  - "Sul A" asks for the shift on one string, which a player makes audible.

The mechanism already exists and was kept to the end of movement II: `PORT_TARGETS` (mvt II `Violins I {82: 100, 172: 100}`, Vln II and Vc added in c12). There, the join had no hole (3 dB), and a cello fourth rose 4-6 dB at the intermediate semitones (kit section 7).

**Fix** (`build/score_config.py`):
- `PORT_TARGETS = {"Violoncellos": {685.0: 100}, "Violins I": {225.0: 100}, "Violins II": {225.0: 100}}`.
- These three tracks need a full rebuild to load the Leg Port MAX row; it is a small row.
- Leave 687/691 to the normal `auto_fills.py` pass.

**Pass criteria.**
- Vc 685 dip under 5 dB.
- An f0 glide of 0.08-0.25 s, seen as energy at the intermediate semitones, on all three.
- No crossover later than +0.15 s.

## 5. Violins II "metà" (bars 47-54) plays a full section on one note against the violas' divided pair: the A-flat4 sits 4.7 dB over each viola voice, where the score's c114 note asks for equal weight

**Score.** tTwo.ily lines 100-102: `aes'1\pp^"metà"` for 8 bars, then "tutti, div." at qn 216. The violas play `<c' es'>1^"div."` underneath. The composer's comment: one undivided note against the divided pair makes A-flat4 twice as strong, so ease it by reducing players.

**Measured (stems, qn 184-200).**
- Violins II: -42.3 dB.
- Violas (two notes, each already cut -3 dB by the c03 divisi rule): -44.0 dB.
- So the single A-flat is 1.7 dB over the pair, which puts it about 4.7 dB over each viola voice.
- No rule reads "metà": `div_state()` in the chord-cut code (about line 2882) knows only "div." / "non div." / "unis.".

The same span in the recap (qn 584-600) is a "div. sul tasto" tremolo and is not affected.

**Fix.** Pick one:
- **Level only.** `div_state()` returns "half" after a text containing "metà", until "tutti" or "unis.". `chord_db()` applies -3 dB to single notes in "half" spans. Level only, so it can go into the stem fix.
- **Timbre as well.** Route Violins II qn 184-216 to a "Violins II div" track on `2nd Violins KS Master DIV B` (already in `build/ks_maps_extra.json`).
  - Starting gain: the kit's +2.5 dB over the section at pp.
  - Then set a role from this render.
  - It is one more instance, so check REAPER memory (41 GB after the c04 render).

**Pass criterion.** Violins II over qn 184-212 at the violas' per-voice level ±1.5 dB, which is about 3 dB under the violas' stem.

## 6. The two long timpani rolls left as the control (qn 464 and 484, bars 117-130) cycle in tone colour like the opening roll did before c04

**Measured.**
- Timpani stem, centroid autocorrelation (detrended, best lag 2.8-4.3 s, which is 3.31 s in every window):

  | Window (qn) | Centroid | Level |
  |---|---|---|
  | 464-484 | 0.92 | 0.53 |
  | 488-504 | 0.96 | |
  | 500-520 | 0.96 | |

- Folded centroid swing over qn 496-520: 350-375 cents. The opening roll measured about 250 cents before its re-strikes.
- The roll is 16-17 dB under the master in the fff bars 117-126. In the retransition, bars 127-130 (qn 504-520), it is -10.5 dB, and -8.7 dB in 100-300 Hz: there the timpani G pedal is the floor under the celli's written-out accelerando and the Cl 1 theme.
- The c04 re-strikes passed every criterion on the rolls at 0, 48 and 720 (centroid 0.95/0.89/0.92 -> 0.26/0.46/0.39, level steps -1.5..+0.8 dB).

**Fix.**
- `build/score_config.py`: `TIMP_ROLL_RESTRIKE["at"]` += [464.0, 484.0], with the same seed rule, `seg_s` (2.5, 3.3) and the -1.5 dB re-strike dip. CC7 and the volume envelope stay those of the whole roll, so the fff hairpins and the c04 bar-122 roles are unchanged.
- Keep 0, 48 and 720 as they are; their dips are keyed to the seeded plan.

**Pass criteria.**
- Centroid autocorrelation under 0.45 in all three windows.
- Level step at each re-strike within ±1.5 dB.
- No 2-5 kHz bump over the roll body at the re-strikes.

## Smaller items (not ranked)

- **Unslurred brass repeats are hardly re-tongued (measured, `rep2.py`).** Median dip at the repeat:

  | Track | Median dip | Share under 3 dB |
  |---|---|---|
  | Horn 1 | -1.0 dB | 79% |
  | Horn 2 | -0.8 dB | 92% |
  | Horn 3 | -0.9 dB | 85% |
  | Horn 4 | -0.3 dB | 97% |
  | Trombone 1 | -0.6 dB | 90% |
  | Trombone 2 | -2.0 dB | 83% |

  Examples are Hn 4 `aes2 aes2` in bar 31 (-0.1 dB) and the p `f1 | f1` of bars 19-20 (+0.3 dB). Inferred: repeated brass chords read as ties.

  Kit section 7: 0.06 qn gives only 1-2 dB on soft horns. A test with `REP_RETONGUE_AT` on Horns 3/4 at bars 19-22 and 31 (0.1 qn early at mf and louder) would tell whether a generic rule is worth it. The accented quarters of bar 32 are already re-articulated (dip -1..-7 dB with a +4..+11 dB rise).
- **Breath marks that do not show (measured, `breath.py`).**

  | Track (qn) | Dip | Gap |
  |---|---|---|
  | Horn 3 536 | -0.3 dB | 0.15 s |
  | Horn 4 512 | -2.6 dB | 0.12 s |
  | Horn 1 475 | -3.0 dB | |
  | Trombone 1 636 | -3.0 dB | |

  All are loud inner voices (kit: a loud breath needs about 0.5 qn and a fall). They are low priority, except Hn 3 536, which is not visible at all.
- **Re-bow residuals (measured, `rebow.py`).**
  - Vc 163.877: dip -6.4 dB, step -9.3 dB (includes the bar-41 sf decrescendo).
  - Vc 37.377: -6.2 / +5.1 dB.
  - Vc 49.683: -5.8 dB.
  - Vln I 711.855: -5.7 dB.
  - Cb 166.01: -5.3 / -4.2 dB.
  - Steps of 3 dB or more: Vc 4, Cb 7.

  These are for the next `fit_rebows.py` pass. Master dips at re-bows equal the control.
- **Remaining legato holes of 6 dB or more (measured, `joins.py`).**
  - Horn 2: 453 (9.7 dB), 266 (6.7).
  - Vc: 112 (8.1), 365 (7.6), 8.0 (7.3).
  - Vln I: 636 / 720 (7.4).
  - Vln II: 296 (6.9), 234 / 245 (6.2).
  - Vla: 378 / 517 / 612 (6.0-6.1).
  - Fl 2: 633 (6.0).

  For `auto_fills.py`. Check Vln I 636/720 for a 30 ms spike first.
- **Harp étouffez (qn 244) is still not implemented.**
  - Measured: the f chord of qn 242 rings at -39..-43 dB through 244.6, while the new p arpeggio sits at -45 dB.
  - The harp is 6-10 dB under the master there, so the gain is small; c04-A #6 still applies.
  - The qn 727 étouffez needs nothing: the ppp chord is already at -81 dB by 726.
- **a2 horns (c04-A #5)** are still on one solo-horn sample plus 3 dB. The recorded 2FH a2 patch remains the right test when a cycle has memory to spare (41 GB settled after c04).
- **Soft string legato velocity (inferred).** 79-91% of string legato targets at CC11 41-70, including the "molto cantabile" tune (219-272) and the "dolce" celli (184-216), play at v124, the tightest transition. Kit c08 used v90 only at CC11 40 or below. A test at v100 on the bars 55-59 violin tune would show whether the slower transition still crosses within +0.10 s.

Do not touch:
- brass, wind and string `GENTLE_ACCENT` (all accent 2-5 kHz medians negative);
- `STR_ACC_AFTER_SUS`, `DETACH_ACCENTS`, `REP_SPLIT` strokes and `stac_s` 0.2 (finding 2 only changes the neighbour notes around them);
- `PORTATO_JOIN_AT` Horn 1;
- the timpani re-strikes at qn 0/48/720 and their dips;
- `TIMP_DELAY_S` and the timpani accent velocities (v121 against v110);
- the pizzicato rows;
- staccato at half the written length;
- the Tremolo rows and the keyswitch guard;
- `AUTO_REBOW` with `space_rebows.py` and the fitted shapes (refit only);
- the merge of slurred and tied repeats on Leg rows (finding 1 extends it, it does not replace it);
- the pre-roll meter fix.
