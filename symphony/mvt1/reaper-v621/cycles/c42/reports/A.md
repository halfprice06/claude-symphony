# Cycle 42, critic A: articulation and phrasing (render c41, score v621)

Method. All levels are stereo power in dB on the final c41 stems (38 stems, master = their float sum), placed with `cycles/c41/rendered_build/parts.json`. Joins are legtest.py's selection (`cycles/c41/actor_scripts/legtest.py`: a note on a Leg row whose moved onset falls inside exactly one other sounding note of another pitch): 245 Violins I, 142 Violins II, 124 Violas, 263 celli joins. Every timing or window estimator was also run on a synthetic instant switch between the same two pitches (harmonics 1-40 at k^-0.8, three chorus voices ±6 cents with 5.5-6.2 Hz ±12-cent vibrato, 5 ms crossfade, placed on the score onset with the join's own lead), which gives each estimator's error for that pitch pair. "Exclusion bands" means a pitch's harmonic bands with every bin within 2 FFT bins of any harmonic of the other pitch left out. Scripts were in `/private/tmp/claude-501/mockup-loop/mvt1-c42-A/` (deleted at the end). Coordinator's two questions are findings 1 and 2.

## Manual notes (second round: c36 slot A's pages, 2021 manual PDF pp. 89-94, read again in full; MANUAL-GAPS.md and DIGEST.md read)

MANUAL-GAPS items still open in this lens, first: #1 brass accents on Marc Sus LITE (c41 C #2's pass-2 test is written and deferred; still the only route to an accent with attack colour), #7 half-section divisi (finding 3), #8 slower legato on cantabile section lines (its c41 premise, that the viola and cello slides are too long, does not hold: finding 1), #5 expressive wind rows, #9 horn portato, #13 3TB for the bass trombone's three lowest notes. Untested and now relevant: the strings' Repetitions TS row (p.94, finding 2).

| Manual (PDF page) | c36 A's note | Now (c41 render) |
|---|---|---|
| p.89-90: DIV A/B = left or right chair of each stand, Close only; a divisi part is "not much less" loud than the whole section | Partly: div. passages as chords on the section patch with -10·log10(k) dB; half-section colour missing; memory | **Still not followed** (read: parts.json `div_entries` Violas 51, Violins I 15, Violins II 10, celli 21). Memory is no longer the reason: the second pass (c39) took 9 instances at 19 GB in c41. DIV A is used once, for the coda solo (c40). Finding 3 |
| p.90 (new on this reading): mix the divisi Close mics with the non-divisi section's other mics, same articulation, loudness adjusted | n/a | The coda "Cello solo" (DIV A) has Close only with send 0.5 and Violoncellos resting, so no section Main under it. Image correlation 0.85 (c40). Followed in spirit through the send; no change (inferred) |
| p.91: Détaché, a defined end, no legato connection; use staccato rows for staccato-length notes | No: never used | **Still never used** (art_counts, all five sections). Not the answer for repeats: Detache ran together on the basses' ff eighths (mvt1 c22) |
| p.91: Sustain alternates up/down bow by round robin | RR never reset (CC36 sent, Opus resets on CC16) | **Still not reset** (MANUAL-GAPS #6, deferred again in c41). Which bow direction a printed down-bow or a repeated Sus MAX stroke plays depends on the history, and c41 shows identical data rendering up to 4 dB apart (Oboe 1 315.5). It also limits every per-note fit, including finding 1's leads (inferred) |
| p.91: three vibrato levels | At f / melody CC1 two sample sets sound together | Unchanged (no string CC1 change since c36) |
| p.91-92: Marcato Sustain = marcato sample plus sustain, "extra power at the start" | Yes, 14 strokes | **Followed**: 14 Sus Marc LITE notes (Vln I 6, Vln II 6, Vc 2), unchanged; string accent fronts median -8.6 dB 2-5 kHz re body (c41 A on c40) |
| p.92: Flautando only in 2nd Violins | Yes | Followed (v621's only sul tasto passage is a tremolo) |
| p.92: Pizzicato RRx2/x4 | Yes | Followed (Cb 33, Vc 3; recap levels fixed in c36) |
| p.94: staccato, staccato on bow, staccatissimo ("even shorter") | No for Violins I (row names swapped) | **Followed since c36** (`STAC_ROW` Violins I "Staccatissimo RRx9" = the V1 Stac samples, 11 notes); the V1 staccato is still 0.17 s at -10 dB against 0.28-0.29 s for the other sections, which is the recording |
| p.94: Repetitions: the same note about a dozen times, "more realistic than just playing the same staccato note multiple times because you get the sound of the bow changing direction"; release trails; end the note early for fewer repeats | Untested | **Still untested.** Read from the patches: "Repetitions TS" is in every section KS Master (Basses key 87); Basses samples 2.50 s at a recorded tempo of 120 bpm (`tempoSync` on), three CC11 layers (mf/f/ff), 0.88 s release trails. 2.5 s at 120 bpm holds about ten eighths. v621 has 16 same-pitch eighth runs on the basses (152 notes at 122-128 bpm). Finding 2 |
| MANUAL-GAPS "checked and consistent" (short rows carry their own envelopes) | Corrected in c36 | Unchanged |

Standing checks (measured, c41 parts.json and stems): no chord on any legato row; no same-pitch overlap; shortest keyswitch lead 9.5 ms (Violas 294.195, celli 152.441), none on or after its note. Re-bows: no string data changed in c41 apart from local notches, and Violins I's rebuild matched c40 (median 0.00 dB), so c41 C's loop result (no held note at 0.4 autocorrelation at 3.95 s) and c41 A's re-bow dips (median 2.1-3.6 dB per section, steps within ±0.6 dB) stand. Accents: no bite (brass 2-5 kHz front minus body median -13.9 dB, c41 C).

## 1. The viola and cello "slides" are an artefact of the band estimator, and so is most of their S2 spread; the real outliers are 37 lower-string joins (68 with the violins), several in the opposite direction from the one the old estimator gives (measured; fix partly inferred)

**Where.** Every monophonic legato join of Violins I/II, Violas and celli, especially the celli dolce tunes (bars 47-55, 147-155), the Lento (bars 3-14) and the second themes.

**What c41 C reported.** Both pitches within 6 dB for 174-236 ms on violas and celli against 112-126 ms on the violins, and legato-target attack spreads of 82-101 ms (violas 48%, celli 45% more than 60 ms off). The c41 START_MAX test changed nothing, because there is nothing to shorten.

**Evidence (measured).**

| | Violins I | Violins II | Violas | Celli |
|---|---|---|---|---|
| Window, C's bands (m37 `harm_env` per pitch, no exclusion): real median | 94 ms | 114 (cantabile) | 164 | 204-219 |
| The same method on a synthetic instant switch: median / p75 | 8 / 10 | 10 / 14 | 15 / 252 | 36-70 / 302-310 |
| Window, exclusion bands, legtest nfft (L) / fixed 2048 (F): real median | 86 / 82 | 101 / 96 | 98 / 92 | 108 / 76 |
| Synthetic floor of L / F | 8 / 8 | 8 / 8 | 8 / 8 | 16 / 7 |
| m37 pc on the synthetic switch: share more than 60 ms off (true value 0) | 10% | 24% | 32% | 29% |
| m37 pc on the stems: robust SD / share > 60 ms off the median | 62 / 35% | 87 / 49% | 114 / 61% | 95 / 53% |
| Corrected pc ("pcX", exclusion bands): robust SD / share > 60 ms off | 51 / 23% | 43 / 26% | 67 / 39% | 58 / 29% |
| pcX on the synthetic switch: robust SD / share > 60 ms off | 3 / 0% | 3 / 1% | 3 / 2% | 4 / 3% |

- **Cause of the artefact (read in `cycles/c37/actor_scripts/m37.py`).** `harm_env` takes each harmonic ±max(1.5%, 1 FFT bin) with nfft 4096 under 220 Hz and 8192 under 110 Hz. One bin there is ±9% of the fundamental, wider than a semitone or a whole tone. At any nfft, harmonics in small-number ratios (9:8, 4:3, 3:2) fall inside each other's ±1.5%. So each pitch's band holds the other pitch's partials. With C's method a perfect instant switch reads as up to 0.6 s of "both pitches sounding" on violas and celli, and only 8-14 ms on the violins. The same overlap makes `attack()` read the old note as the new note's floor or rise.
- **The real transitions are the same length in all four sections.** With exclusion bands they last 76-108 ms (violins 82-101) over a floor of 7-16 ms, by two methods. Arrival of the new pitch within 6 dB of its body (notes of 0.45 s or longer): median -10 / +14 / -17 / +13 ms and p90 71 / 84 / 80 / 94 ms (Violins I / II, Violas, celli).
- **The S2 spread of the lower strings is about half what was reported.** Celli dolce tunes: m37 robust SD 96 ms with 53% more than 60 ms off; pcX 52 ms with 29%. The violas stay the widest section (67 ms).
- **m37 points the wrong way on many joins.** Of the 131 celli joins m37 puts more than 60 ms off, pcX puts 51 on the other side of the median (violas 13 of 67, Violins II 27 of 71, Violins I 15 of 86).
- **The c27/c37 per-onset leads were fitted on m37 pc**, so some moved the wrong way (inferred from the fit notes in `build/leg_leads.json`). All values here are relative to the section median. Example: celli 10.0 (C3 to C-sharp3, bar 3; the celli are the master there, rel -0.2 dB). It carries a -0.09 s extra and m37 reads -89 ms (early). pcX reads +89 ms and the relative crossover +136 ms: late. The same holds for celli 60, 72, 270, 280, 440 and 596 (m37 -87..-185 ms early, pcX +61..+212 late) and, the other way round, Violas 81 (m37 +121, pcX -113).

**Fix.**
1. **No section-wide legato change.** Drop the START_MAX / RELEASE route (c41) and the slide premise of MANUAL-GAPS #8.
2. **Measure with exclusion bands.** Before any lead is fitted, measure legato targets (and any string note that follows another pitch within 0.5 s) with exclusion bands, in the actor's copy of `m37.py` (`harm_env` / `attack`):
   - drop every bin within 2 bins of a harmonic of the previous pitch;
   - use nfft 2048 if at least 2 harmonics of the new pitch survive, else 4096, else 8192;
   - keep the t50/h10 rule unchanged;
   - also replace m37 pc in legtest.py's pc column.
   Synthetic error with this estimator: robust SD 3-4 ms.
3. **Refit the outliers, in `build/leg_leads.json`.** The candidates are exposed joins (target within 10 dB of the master over its first 0.3 s) more than 60 ms off their section's pcX median (+13..+23 ms), where a relative crossover on the same bands agrees in sign and by more than 30 ms. The new value is old + 0.6 x (pcX - section median), with the change clamped at ±0.12 s. Celli and violas first (37 joins); the violins can follow (31). Values (new totals; current value is 0 where the onset has no entry):
   ```
   "Violoncellos": {"10.0": -0.04, "11.0": -0.04, "60.0": 0.04, "72.0": 0.12, "91.0": 0.04, "144.0": -0.08, "183.0": 0.08, "184.0": 0.07,
     "211.5": -0.05, "213.0": -0.04, "266.0": 0.1, "270.0": 0.07, "280.0": 0.04, "356.0": 0.1, "372.0": 0.05, "415.0": -0.04, "418.0": -0.04,
     "422.0": -0.05, "438.0": 0.1, "440.0": 0.04, "572.0": -0.04, "592.0": -0.04, "596.0": 0.05, "601.0": 0.09, "613.0": -0.07, "658.0": 0.04}
   "Violas": {"81.0": -0.07, "147.0": 0.08, "182.0": -0.09, "368.0": 0.12, "436.0": 0.04, "584.0": 0.11, "589.0": -0.1, "601.0": -0.04,
     "604.0": -0.05, "613.0": 0.07, "673.0": -0.07}
   "Violins II": {"180.0": -0.04, "230.0": 0.06, "256.0": -0.04, "400.0": 0.09, "404.0": -0.05, "650.0": 0.06}
   "Violins I": {"47.0": 0.01, "89.0": -0.05, "91.0": 0.11, "98.0": -0.04, "137.0": -0.08, "224.0": 0.09, "236.0": 0.07, "245.0": -0.05,
     "249.0": -0.04, "260.0": -0.05, "268.0": -0.07, "280.0": -0.11, "313.0": -0.04, "395.0": 0.08, "400.0": 0.04, "402.0": -0.05,
     "444.0": 0.14, "452.0": 0.04, "456.0": 0.05, "471.5": 0.04, "496.0": -0.06, "537.0": -0.04, "545.0": -0.05, "562.0": 0.05, "654.0": -0.04}
   ```
4. **Before the render.** Diff the moved onsets (`cycles/c33/actor_scripts/pdiff.py`): a new key can raise the lead cap where a `LEG_CAP_FRAC` "listed" entry covers the onset, and nothing else may move.
5. **After the render, re-measure what keys off these joins (kit c30).**
   - 13 of the celli joins and Violins I 236 carry `early_fills.json` rows (celli 10, 144, 601 and 658 with pre_s 0.21-0.28 s).
   - Celli 596 has the c26 notch at 595.66-595.92.
   - Violas 613 has the c41 notch at 612.75-613.0.
6. **Pass.**
   - pcX robust SD: violas ≤ 50 ms, celli ≤ 45 ms;
   - none of the moved joins further from its median than now;
   - no new dips ≥ 5 dB or bursts ≥ 3 dB (legtest metrics).

## 2. String repeats: the master dip is small because other parts hold notes in the repeating section's own band, not because the stems fail to separate; what is left to change is the attack, and the basses' eighth pedals can try the library's recorded repetitions (measured; gain inferred)

**Where.** 84 exposed same-pitch string repeats (stem broadband body within 10 dB of the master; re-bow pieces left out):
- the celli's G2 pedal pp < f, bars 127-130 (504-520), 31 repeats;
- the basses' eighth pedals, bars 27-31, 82, 131-134, 140-142, 167-169 (104-124, 324-328, 520-536, 556-568, 664-676), 23 repeats;
- 18 more on the basses;
- 12 on the upper strings.

**What is wrong (measured).**
- **The two c41 numbers measure different things.** 4.4 dB is a broadband stem dip; 2.1 dB is a master harmonic-band dip. In the same harmonic band (h1-8 of the repeated pitch, 30 ms) the stems dip a median 3.1 dB, the sum of all five string stems 2.4 dB, and the master 1.5 dB.
- **Other parts fill the band.** In 68 of the 84 repeats, the other stems carry 3 dB or more than the repeating section in that band at the note body. Median excess:
  - +5.6 dB at the celli pedal: Clarinet 1's motif (its G3/G4/D notes are harmonics of G2), with the basses holding G and the timpani roll;
  - +4.8 dB at the basses' pedals: the celli theme, tuba, timpani.
- **These maskers are held notes in the score, not misaligned repeats.** No case is a doubled section re-attacking out of step with the repeating one. A real orchestra would show the same small dip.
- **The re-attack does show in the master.** The band rises from the dip minimum to the attack peak by a median 3.9-4.0 dB in the master (stem 5.8-9.0).
- **Under a held note in the same band, a repeat can only be heard through its attack colour** (inferred), and c41 C measured only +0.8 dB of 2-5 kHz at string re-attacks.
- **The basses' pedals now (eighth-grid fold, detrended, p95-p5 in dB, stem / master):**

  | Run | 30-150 Hz | 1-4 kHz |
  |---|---|---|
  | 104-124 | 5.8 / 4.2 | 4.8 / 1.1 |
  | 520-536 | 7.0 / 6.4 | 6.6 / 0.8 |
  | 556-568 | 5.4 / 2.4 | 4.8 / 1.3 |
  | 664-676 | 5.1 / 3.2 | 4.8 / 0.8 |

  At 664-676 the stem dips 13.2 dB at 30-150 Hz before each downbeat, but only 0.7 dB before each off-beat (master 5.4 / 2.8). The off-beat runs into the downbeat (c41 A's observation). This is the known c13-c22 compromise; Detache and Marc Shrt failed there.

**Fix.**
1. **Leave STR_REP_DETACH and the `_cb24` shapes as they are.** A deeper post-hall dip cannot uncover a note under a louder held voice, and it cuts the section's own hall.
2. **Measure S1 differently where others hold.** For string repeats where the other stems are 3 dB or more over the repeating section in its band, use the master re-attack rise in the band (now 3.9-4.0 dB) and the 2-5 kHz rise, not the master dip.
3. **A/B the basses' eighth pedals on "Repetitions TS" in the second pass** (manual p.94):
   - **Track.** A TEST_TRACKS alias of Double basses ("Cb rep test", Basses KS Master), over the 16 runs. Its alias tables drop STR_REP_DETACH, the `_cb24` level shape and the per-eighth note trims.
   - **Tool.** One generic rule in `tools/score_to_parts.py`, e.g. `REP_TS = {"at": {track: [(a, b)]}, "row": "Repetitions TS", "max_qn": 4.0, "lead_s": 0.03}`. Inside a span, each same-pitch run becomes one note per 4 qn or less (8 eighths; the sample holds about 10), on the row's keyswitch. CC11 stays at the printed level (the row has mf/f/ff layers). The note starts 0.03 s early instead of the 0.12-0.16 s abut lead, because the sample's own grid then follows the host tempo.
   - **Memory.** One Basses KS Master with one row loaded, in pass 2.
4. **Check first.** Before judging, check on the test stem that the internal repeats fall on the eighths: inter-onset 0.5 qn ±15 ms at 122-128 bpm. The rate is inferred from the sample length.
5. **Pass:**
   - per-eighth dips before off-beats ≥ 4 dB at 30-150 Hz on the stem (664-676 now 0.7);
   - master 30-150 Hz eighth fold ≥ now in every run, with the test stem substituted;
   - 2-5 kHz rise at each re-attack ≥ +3 dB, front minus body ≤ +3 dB (no bite);
   - bar levels within ±1 dB K of the main stem;
   - perceived attacks within ±25 ms of the run's median.

   Adopt it run by run; keep the current pedal where it fails.

## 3. Viola divisi, bars 47-60 and 62-68, as half-section patches in the second pass (MANUAL-GAPS #7; p.89-90) (inferred)

**Where.** Violas div. 184-236.5 and 245-272 (unslurred whole-note dyads at p under the celli dolce tune). Also Violins II div. 424-464.

**What is wrong.**
- **How it is played (read).** Each dyad note is a full-section sample cut 3 dB (`div_entries`), so two full sections play at half power each.
- **What the manual says (p.89-90).** The DIV patches are the two chairs of each stand, recorded at the same time as the section's other mics. The real texture is two half-sections of different colour. Their loudness is "not much less" than the full section.
- **What is new.** The second pass removes the memory reason that deferred this in mvt1 c01. The DIV A route worked for the coda solo (c40) and for mvt II's divisi (kit §8).

**Fix.**
1. **Tracks.** "Vla div A" / "Vla div B" aliases of Violas on Violas KS Master DIV A / DIV B, Close only, send 0.5, main channel pan 0 (kit §1: DIV A ships panned).
2. **Routing.** The upper note to A and the lower to B by the rank rule (kit §17), over 183.9-236.6 and 244.9-272. Violas rest there (`TRACK_WINDOWS`), with no -3 dB div cut on the aliases.
3. **First render as TEST_TRACKS.** Measure:
   - per-note level against the section render (match within 1 dB with alias gains);
   - centroid and 2-5 kHz share;
   - loop pulsing on the whole notes (DIV patches loop too);
   - the entry and hand-over at 184 and 236.5.

Adopt if the levels match and the two voices read as separate lines. Rank it after findings 1-2: the gain is colour, not timing.

Do not touch: AUTO_REBOW with the fitted re-bow shapes; the legato overlaps and keyswitch placement (no chords on legato rows, no keyswitch under 9.5 ms); START_MAX / RELEASE at the patch defaults (c41 test); STR_REP_DETACH, the basses' `_cb24` shapes and the celli 504-520 hold (keep them as the fallback for finding 2); REP_ROW with REP_ROW_GAP_S (0.06, 0.15) and the wind/brass re-tongue settings; GENTLE_ACCENT and the accent fits; STAC_ROW Violins I; the 14 Sus Marc LITE strokes; the DIV A coda solo as fitted; every per-onset lead in leg_leads.json not listed in finding 1.
