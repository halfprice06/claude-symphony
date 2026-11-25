# Critic B, cycle 42 (render c41): balance and levels

## Manual notes (second reading of the c36 B row: May 2021 HO manual PDF pages 137, 140, 150-151, read in full; MANUAL-GAPS.md and DIGEST.md read)

Open MANUAL-GAPS items first, then the c36 B notes checked against the c41 render.

| Source | What it says | Where it applies here | Followed now? |
|---|---|---|---|
| MANUAL-GAPS #6 (p.34; 2025 p.92) | Opus resets round robins on the CC set in Preferences (`RoundRobinResetCC` 16). CC36 is the Repetition script's reset. | `build_reaper.py` sends only CC36 = 127 in the pre-roll. | **No, still open.** Measured c40 → c41 on 1-qn windows where notes, keyswitches, CC1/11/7/70 and the envelope are identical: 27 of 38 stems repeat within 0.5 dB in 98-100% of windows, Violins II 92%, Oboe 1 92%, Violins I 87% (that figure includes the bars 56-59 sul window, where c40's audio came from a stale-state instance). With identical data, 14 windows moved by 3 dB or more, 12 of them outside that sul window. The largest is Violins II's held A5 at 160, which fell 4.3-6.1 dB at 162-164 (A re M -7.1 → -12.2 at 162). Horn 3's C4 at 164 stayed in the "high" state c40 found (-2.2 A re M, 2.5 dB over Horns a2). See finding 4. |
| MANUAL-GAPS #7 (p.89-90) | DIV A/B half sections for soft div. passages. | Violas div. pp in bars 47-60; Violins II div. sul tasto pp in bars 147-155. | Not used, and not needed for balance. The viola chords sit 12.7-18.5 dB K under the master at 184-206, and the Vln II tremolo 13.7-22 dB under at 584-618 (measured). |
| MANUAL-GAPS #1, #4, #5, #9, #12, #13 | Accent rows, Mid mics, expressive rows, portato, crescendo rolls, 3TB. | — | These belong to the articulation, blend and holistic lenses. None of them is a level problem in this render. |
| p.137 | Every KS Master row has a load button and its own volume knob. | `load_articulations()` loads only the rows in use. Row offsets are corrected in the envelope (`ROW_TRIM_DB`, fitted row shapes). | **Followed.** Read from the `.oib` LayerRow entries this cycle: every row the 34 pitched tracks use ships at volume 1.0 (Tuba Sus MAX 1.016). That includes the rows added since c36: LegRep RRx4 (Contrabassoon, Bassoon 1, Bass clarinet, Horn 1, Horn 4, Trumpet 2), Leg Slur Rep (Clarinet 1), Stac DblTng RRx9 (the three pass-2 stac aliases), Staccatissimo RRx9 (Violins I), and the 2TP and DIV A patches. The c41 LegRep body excess is trimmed in the envelope (Horn 1 452 -2, Trumpet 2 456 -1.5). **New note:** an AUTO_REBOW piece on Sus MAX inside a Leg Slur line plays hotter than the legato note it continues. Celli 37.377 (Sus MAX keyswitch at 37.357): stem minus envelope is -2..-3 dB before the re-bow and 0..+1.7 dB 1.2-1.5 s after it, inside a crescendo (measured; that the row is the cause is inferred). Finding 2. |
| p.140 | Master channel gain changes the output without changing the mic mix. Pan keeps the mics' relative pans. | Main gain and pan are left at the patch values. Track gains are in the REAPER envelope. The pass-2 project uses the same `build_reaper.py` / `mix.json`. | **Followed** (read). |
| p.150 | Velocity sensitivity defaults to 0 (linear). Velocity picks the layer and is mostly used for short notes. | Read this cycle: `velocitySensitivity` 0.0 in the 1FH, 1st Violins, 2TP, BS and Celli DIV A patches. Velocity sets the level on timpani, harp, pizz. and stac. | **Followed.** c36's coda pp timpani strokes (712-718) now sit -5.0..-6.9 dB K re M over their first 0.15 s, on c36's -5..-7 target (measured). |
| p.151 | Send CC1/CC11 before the first note. CC7 sets each track's ceiling, and CC11 shapes the line. Volume can be changed mid-note. | 3-qn pre-roll. Gains, dyn and soft trims are in the volume envelope. The timpani use CC7 per stroke. | **Followed.** The bar-141 ff stroke (560) is -7.1 dB K re M over 0.25 s (c36 fix -7.0), inside the -5.6..-13.9 spread of the other ff strokes (measured). **New note:** the volume-by-dynamic trims are largest on the horns: Horn 1 soft_trim mp +7.2, p +10.6, pp 13.0; Horn 3 mp +8.4. The strings get +0.7..+2 at mf. With the c09 role, this puts Horn 1's mp above the mf strings it doubles. Finding 1. |

## Method

- **Render.** `cycles/c41/render` (38 stems, master = float sum) with `cycles/c41/rendered_build/` (parts.json, roles, fills, mix). c40 render and build used for repeatability.
- **Analysis frames.** 4096-point FFT, 20 ms hop, stereo power. Per frame: A- and K-weighted levels, six bands and the centroid.
- **Notation.** "re M" = stem minus master over the same window.
- **Simulations.** Stem powers are scaled by the proposed dB shapes, and the change is added to the master power. This is approximate on correlated low-end stems; `stem_fix.py` gives the exact figure.
- **Delivered levels.** RMS per beat from the decoded `mvt1-mockup-c41.mp3`.
- **Score.** Pages 2, 5, 6, 8-11, 15, 17, 18 read; marks checked in `build/mockup-events.tsv`.
- **K and A.** K under-weights nothing below 1.5 kHz except the sub-bass, while A cuts 200 Hz by 11 dB. At the soft levels discussed here the ear lies between the two (inferred), so both are quoted.

## Coordinator's checks

**c41 B #1-#5 hold** (measured, `c41check.py 40 41 bal climax`):
- **#1.** Cor anglais third answer, A re M at 603 / 604: -7.2 / -8.4.
- **#2.** Horn 1 minus Violins I at 498.0-499.5: +1.8 / +2.9 / +2.4 / +0.8 A. Horn 1 minus Oboe 1 at 499 / 499.5: +4.3 / +3.3.
- **#3.** Master K steps into 636: +1.8 / +0.5 / +3.3 / +2.5; into 484: +1.3 / +0.8 / +3.4. The delivered mp3 grows evenly into 636 (RMS per beat 632-636: -20.5 / -19.4 / -18.5 / -17.4 / -14.2). Into 484 it rises to beat 3 and holds (-19.0 / -18.4 / -18.6 / -15.0). No change needed.
- **#4.** Coda solo minus cor anglais: median +3.8 dB A, 3 of 12 half-beats under 3 dB.
- **#5.** Cor anglais stac minus Violins II: -6.3..+3.1.

**Long timpani rolls (Dan's note): none drowns anything** (measured, all 12 rolls of 3.4 s or more, from 1 s after the start). No roll is the loudest stem.

| Roll | K rank | K re M (dB) | A rank |
|---|---|---|---|
| opening ppp (0-16) | 4 | -10.3 | 4 |
| bar 11 pp < f (40-47) | 3 | -11.0 | 13 |
| bars 80-82 p < ff (316-329) | 3 | -9.4 | 7 |
| letter G / sostenuto (464-521) | 14 | -14.9 | 25 |
| bar 159 (628-642) | 6 | -13.2 | 18 |
| bar 174 pp | 6 | -14.9 | 6 |
| final ppp (720-728) | 8 | -11.9 | 8 |

**Dynamic mapping across families** (measured). Method: on every beat where four or more tracks hold one steady printed dynamic, each track's K level minus that beat's median.
- **Within ±3 dB.** Every wind, brass and string track at every dynamic, apart from:
  - the melodic roles: Violins I +3.0..+5.1, Violins II f +3.7, Clarinet 1 pp +6.8 (its coda solo), Horn 1 ff +3.0;
  - register and inner second parts, on the low side: Flute 2 f -4.7 / ff -3.6, Clarinet 2 f -3.8, Oboe 2 f -3.2, Contrabassoon f -3.6 / fff -4.2, Bassoon 1 fff -4.1.
- **New trumpet tracks.** Trumpet 1 f / ff / fff +1.9 / +2.8 / +2.5, Trumpet 2 and 3 within ±1.1.
- **Percussion.** Tam-tam, suspended cymbal and the Crash ring repeat c40 within 0.5 dB on every compared window, so c41 B's percussion readings stand.
- **Verdict.** p sounds like p in every family. No global trim change.

**Weakest passages named by C.**
- **Bars 47-55 and 147-155:** finding 1.
- **Lento chorale, bars 6-14:** finding 2. The cor anglais solo leads the pp strings by 6+ dB.
- **Coda, bars 171-182.** Balanced: Clarinet 1's pp espr. solo leads by 4-6 dB K; Vln I leads bars 179-180; the pp tam-tam sits at -10.9 K / -15.0 A re M in its first 2 qn. In the final ppp chord the violas are the loudest voice (-5.0 K at 726), but they carry the major third (E-natural, 724 on) under their +2 role [720, 729], so that is right.
- **Development, bars 97-116.**
  - Letter F: the ff tune leads, with Vln I at -5.8..-9.9 K re M and the f brass at -10..-19.
  - Bars 103-106: the printed f counter-motif (Oboe 2 + Clarinet 1) sits over the mf Horn 1 / celli tune, as printed.
  - Bars 107-110: the two p espr. lines (bass clarinet, violas) are level.
  - The one fault is a stale fill at bar 114 (finding 3).

**Brass or percussion as the loudest stem** (A, beats 56-680, margin of 2 dB or more over the next stem):
- **Expected:** the tam-tam fff (485-492, as printed), the coda Trumpets a2 tune (665-675), Trombone 1 in the last coda chords, and Horn 1's p line in bars 43-44 (the only melodic voice).
- **Not expected:** Horn 1 under the dolce tune (finding 1).

## Findings, ranked by what a listener would gain

### 1. Horn 1 (mp) is louder than the mf strings it doubles in the second theme's dolce tune, bars 46-52 and above all 147-152 (measured; fix simulated)

**Where.**
- Horn 1 against Violoncellos (bars 46-52, unison, celli "mf dolce", horn "mp, 1. dolce").
- Horn 1 against Violas and Violoncellos (bars 147-152). Violas and celli play mf dolce in octaves; the horn doubles the violas to 598 and the celli from 600.

**Evidence (measured).**
- **Recap, per 2 qn, re M:**

  | qn | Horn 1 A | Violas A | Celli A | Horn 1 K | Violas K | Celli K |
  |---|---|---|---|---|---|---|
  | 586 | -3.1 | -8.2 | -6.2 | -4.2 | -8.8 | -3.9 |
  | 588 | -3.9 | -6.5 | -8.7 | -4.0 | -7.6 | -5.5 |
  | 590 | -3.4 | -7.7 | -5.5 | -3.6 | -9.5 | -4.3 |
  | 598 | -4.4 | -7.6 | -4.3 | -4.6 | -9.1 | -3.6 |
  | 602 | -5.3 | -7.6 | -4.3 | -4.3 | -9.4 | -3.9 |

- **Horn as loudest stem.** Horn 1 is the loudest stem of the whole texture at 587, 588, 590 and 599, by 3.1-4.4 dB A. The violas, which carry the tune's upper octave, are the weakest of the three voices in K (3-6 dB under the celli).
- **Exposition.** Horn minus celli per 2 qn, 184-206:
  - K: median -1.0, peaks +2.8 (202, the C5) and +0.5 (200);
  - A: median -1.9;
  - Horn 1 is the loudest stem at 183-184 and 203 (+2.7..+4.7 A).
- **Why: the envelope.** At the swell tops Horn 1's envelope is +9..+12.5 dB (586-587, 591). That is the mp soft trim (+7.2), the c09 role `["Horn 1", [583, 607, 2.5]]` (and `[183, 207, 2.5]`), the soft-hairpin ramps and note trim 591 +4.5. Over 584-607 the violas' envelope runs -1.7..+5.5 dB and the celli's -2.5..+7.4.
- **Why the c09 role is stale.** c09 (series 1) set the role when the horn was 1.9-2.6 dB under the celli and aimed for level. The horn has since risen past them (LEARNINGS 13: old lifts go stale).
- **Orchestration norms.** By RK's piano ratios (one horn ≈ one wind ≈ one string section), a horn marked a level softer than its string partners should sit 2-3 dB under them, not 3-5 dB over (inferred).

**Fix (level only; stem fix possible), `build/roles.json`:**
- `["Horn 1", [583, 607, 2.5]]` → `[583, 607, -1.0]`;
- `["Horn 1", [183, 207, 2.5]]` → `[183, 207, 0.5]`;
- add `["Violas", [584.0, 606.0, 2.0, 0.5]]`.

**Simulated results.**
- **Recap, A at 586 / 588 / 590.** Horn -5.7 / -6.9 / -6.1, violas -5.4 / -4.0 / -5.0, celli -5.3 / -8.3 / -4.8. The three voices come within 3 dB, with the strings on top; the horn is the loudest stem nowhere in 584-606.
- **Recap, K.** Horn -6.3..-13.4, violas -3.7..-6.8, celli -2.7..-5.0.
- **Exposition.** Horn minus celli: median K -3.0 (peak +0.8 at 202), A -3.9.
- **Master.** Falls 0.36 dB K over 584-606. The cor anglais answers (c41 #1) keep or gain margin.

### 2. Bar 10 (Lento, qn 36-39.5): the Vln I's mp espr. melody is covered by the celli's pp crescendo, and the master dips inside the bars 9-12 crescendo (measured; fix simulated)

**Score.** Bar 9: Vln I "mp" sul D, with one long crescendo to f at bar 12. Vln II, violas, celli and basses are marked "pp" with the same crescendo.

**Evidence (measured).**
- **Vln I minus celli per half qn, 36.0-38.5:**
  - K: -3.0 / -2.8 / -2.5 / -3.4 / -5.4 / -8.7;
  - A: +3.5 / +3.8 / +4.3 / +2.2 / +0.7 / -1.3.
  - At 38.5 the celli are the loudest stem (-2.0 K re M, Vln I -10.7).
- **The violins stay flat.** Vln I's held E-flat5 (35.87-39.02) stays flat in absolute level (-6.1 / -5.7 / -6.4 dB K per qn) while everything else crescendos, so it falls 4 dB re M inside a printed crescendo.
- **The celli bloom.** The celli's automatic re-bow at 37.377 plays on Sus MAX (keyswitch 37.357, velocity 59). Its fitted re-bow fill matches the hole (stem minus envelope -15..-19 dB under the +10 dB fill). From +1.2 s the Sus MAX piece blooms to 3-4 dB over the legato note before it (manual-notes row p.137).
- **The listener's result.** Delivered RMS per beat 37 / 38 / 39 / 40: -26.1 / -24.9 / -26.3 / -25.4. That is a 1.4 dB fall at qn 39 in the middle of a four-bar crescendo (BRIEF item 6: no reversed crescendos). Master K per qn 36-40: 0.9 / 2.3 / 3.7 / 2.9 / 4.2.

**Fix (level only), `build/score_config.py`:**
```
LEVEL_SHAPES["Violins I"] = LEVEL_SHAPES["Violins I"] + [[(36.3, 0.0), (37.6, 2.0), (38.6, 4.0), (38.95, 4.0), (39.45, 0.0)]]
LEVEL_SHAPES["Violoncellos"] = LEVEL_SHAPES["Violoncellos"] + [[(35.9, 0.0), (36.3, -2.5), (38.1, -2.5), (38.35, -4.0),
                                                               (38.9, -4.0), (39.3, -1.5), (39.9, 0.0)]]
```
- **Timing.** The Vln I shape releases across its bow-change join into 39 (moved onset 38.854). The celli shape is back to 0 before the 39.879 re-bow and the printed bow change at 40 (NOTCH_SKIP).
- **Simulated, Vln I minus celli 36.0-39.5:** K -1.0..+5.3 (one half beat -0.9); A +5.4..+8.3.
- **Simulated master K per qn 35-40:** -0.4 / 0.3 / 2.0 / 2.8 / 2.9 / 4.2, which now rises every beat.
- **Celli.** They still grow from pp to f across bars 9-12.

### 3. Two stale join fills make inner voices swell over the line: Horn 4 at qn 453 (bar 114) and Bassoon 1 at 364 (bar 92) (measured)

**Scan.** All 131 early fills of 2 dB or more on c41: stem level in the fill window against the 0.25 s before it and 0.3-0.7 s after it, plus stem minus envelope. Only these two make a bump on both sides without a dip in the stem minus envelope; every other ≥2 dB fill is followed by a body decay or covers a real dip. The celli re-bow fills of finding 2 fit their holes.

**Horn 4, 453 (F3, p cresc., poco a poco stringendo).**
- **The fill.** `early_fills.json` `"453": {"db": 4.2, "pre_s": 0.0, "hold_s": 0.45}`, from c22 (`auto_fills.py` on c21, "dip 7.2 dB at +0.33 s").
- **There is no hole to fill.** Stem minus envelope is -0.8..-1.5 dB over 0-0.3 s after the onset against -0.7..-2.5 before it. The fill raises the stem +4.9 dB at the onset and holds +4..+5.6 for 0.5 s.
- **Balance result.** Per half qn 453.0-454.0, K re M: Horn 4 -9.0 / -8.4 / -7.5, against Violins I (the tune) -8.8 / -9.5 / -9.9, Horn 3 -16.9 / -16.0 / -14.9 and Horn 1 -14.6 / -15.2 / -14.1.
- **Against its neighbours.** The F3's body is -8.8 K re M, against -13.6..-21.3 for Horn 4's other notes in bars 111-117 and -15.6 for Horn 3 on the same beats.

**Bassoon 1, 364 (A-flat3, f, countersubject under the Violins II / cor anglais subject entry).**
- **The fill.** `"364": {"db": 5.1, "pre_s": -0.079, "hold_s": 0.359}`, from series 1 c02.
- **There is no hole to fill.** Stem minus envelope does not dip (fill window minus body -0.1 dB).
- **Balance result.** Bassoon 1 is -4.2..-4.5 K re M at 364.0-364.5, 1.6-4.3 dB over the Violins II subject (-5.9 / -8.5 / -6.5).

**Fix (level only; stem fix possible).**
- In `build/early_fills.json`, delete Horn 4 `"453"` and Bassoon 1 `"364"`, with their `_auto` notes.
- In `build/note_trims.json`, add Horn 4 `"453.0": -2`, and put 453.0 in the 0.1 s list of `NOTE_TRIM_RAMP_S["Horn 4"]` (`build/score_config.py` line 499, the block headed "Horn 4's C3-F3 notes play 10 dB hot at p/mp").

**Simulated.**
- **Horn 4, 453.0-455.5, K re M:** -15.8 / -15.1 / -12.3 / -14.2 / -15.8 (with Horn 3 -14.3..-16.4), with Vln I 5-7 dB on top.
- **Bassoon 1, 364.0-364.5:** -8.3 / -7.3 / -6.2 against Vln II -4.7 / -7.3 / -5.5.
- **Re-check.** After the render, check that no join hole reopens: the stem-minus-envelope dip should stay under 3 dB.

### 4. Identical data still renders at different levels (MANUAL-GAPS #6): Violins II at bars 41-42 fell 4-6 dB, and Horn 3's C4 at 164 still tops the horn call (measured; cause inferred)

**Where.** Bars 41-42 (qn 160-166), plus single notes elsewhere.

**Evidence (measured).**
- **Repeatability, c40 → c41.** Only windows with identical notes, keyswitches, CC lanes and envelope were compared. 27 of 38 stems repeat within 0.5 dB in 98-100% of 1-qn windows, but Violins II 92%, Oboe 1 92% and Horns a2 93%. Violins I is at 87%, but that includes the c40 stale-state sul window.
- **Moves of 3 dB or more, outside that window:**
  - Violins II 162 / 163 / 164: -5.7 / -6.1 / -4.3 dB. This is one held A5 from 160, v98, Leg Slur MAX. A re M at 163 went -4.7 → -8.9.
  - Violins II 648: -3.4; Violins II 173: +3.0.
  - Trumpet 2 453: -3.9.
  - Clarinet 1 152: +3.5; Clarinet 1 422: -3.0.
  - Violas 375: +3.3.
  - Violoncellos 350: +3.1.
  - Oboe 2 411: -3.0.
  - Violins I 96: +3.0.
- **Horn 3, 164.** Horn 3's C4 at 164 (c41 B #6) kept its c40 level: -2.2 dB A re M against Horns a2 -4.8, the loudest stem at bar 42 by 2.5 dB. c39 had it 5.5 dB under.
- **Consequence.** A per-note level fitted on one render can be wrong on the next, so per-note fits on these tracks cannot be trusted.

**Fix (tool, as c41 B #6; schedule it in a refit cycle).**
- In `tools/build_reaper.py`, in the `RR_RESET_QN` block, append `{"qn": RR_RESET_QN, "cc": 16, "v": 127}` for every track next to the CC36 reset. Do the same at the `MEAS_TREM["rr_runs"]` lane starts in `score_to_parts.py`.
- Render once. Compare the listed notes and the per-stem repeat shares above with c41 and the following render (two renders with the reset, no data change between them, if the cycle allows).
- If the Violins II A5 and Horn 3 C4 still flip, leave them unfitted and judge per render. Do not fit a level to one state.

## Do not touch

- The timpani roll levels, settles, `TIMP_CC1_MAP` / `TIMP_ROLL_TRIM_DB` (no roll is the loudest stem; ranks 3-14 in K).
- The coda pp timpani strokes and the bar-141 step.
- The c41 B #1-#5 changes:
  - the Cor anglais role [586, 598.5];
  - the bar-125 shapes;
  - the `_all` fff rows (the delivered crescendo into 636 now grows every beat);
  - the coda cor anglais -2.5;
  - the Cor anglais stac shapes.
- The violas' +2 role [720, 729] (the final chord's E-natural).
- The celli re-bow fills at 21.442 / 26.516 / 37.377 / 39.879 (they fill real holes).
- The soft and dyn trims as a set (p sounds like p in every family; fix finding 1 with roles, not the horn mp trim, which the bar-13 solo and bars 43-44 rely on).
- The Trumpets a2 fit; the tam-tam fff and pp; the sus.-cymbal stroke with the K Crash ring.
- `RIDE_TRIMS`, the DIV A coda solo and its contour, and the climax order (160 > 122).
- Every solo margin c40 / c41 B protected (cor anglais bars 5-8, Horn 1 bars 13-14, Flute 1 bars 73-76, Clarinet 1 bars 127-130 and 175-178, Oboe 1 bar 145).
- Every earlier do-not-touch item.
