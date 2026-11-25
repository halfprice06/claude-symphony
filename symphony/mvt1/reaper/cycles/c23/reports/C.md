# Cycle 23, critic C: tempo, timing and transitions (render c22)

Lens: the tempo map against the printed tempos and the rit./allargando/animando/largamente steps; the Lento/Allegro changes; attack latency of legato and sustain samples in the fast Allegro figures and lead compensation; keyswitch lead times; note starts between sections; phrase endings, the fermatas and the attacca ending.

## Method

Material: the stem-fixed c22 render (`cycles/c22/render/`), `mvt1-mockup-c22.mp3`, and `build/parts.json` (same notes, keyswitches and tempo map as the render). Score qn were converted to file time on the parts.json tempo map. The scripts were throwaway and the scratch folder has been deleted (BRIEF rule). They worked as follows, so the actor can repeat them:

- **Per-note timing.** For every single-voice note in the Allegro tempi (105 bpm or faster; chords skipped), the stem's mono sum was analysed with a 2048-point STFT at a 5 ms hop.
  - Own-pitch energy is harmonics 1-4, ±3% or ±1.2 bins.
  - **Crossover:** the first time from the score onset - 0.25 s at which the new pitch's energy exceeds the old pitch's for 30 ms. Used for pitch changes with no rest.
  - **Arrival:** the first time the own-pitch level is within 6 dB of its maximum over the note's first 0.8 s. Used for entries after at least 0.2 qn of rest.
  - Values of -0.2 s or less are window-start artefacts (repeats, sustained crescendos) and were dropped. Below about C3 the pitch resolution is too coarse, so bass values are not used.
- **Ensemble deviation.** At every score onset where three or more tracks start a note, each track's value minus the median of the others.
- **Tutti onsets.** Broadband arrival (peak - 6 dB over 20 ms frames) for each stem at the 60 onsets that have 14 or more note events.
- **Phrase endings.** For 560 notes of 0.5 qn or longer followed by a rest of 1 qn or more, the time at which the stem falls 10 dB under the note's last body.
- **Also measured:**
  - the tempo map beat by beat, against `build/mockup.midi`;
  - keyswitch-to-note gaps;
  - the master around the fermatas and at the end;
  - BRIEF items 7 and 8.

## Checks that pass (measured)

- **Tempo map.** It plays every printed tempo. The total is 433.34 s, against 430.78 s for the printed steps; the difference is the arcs, the caesura and the bar-170 fermata.
  - **Ramps.** Every ramp follows its printed steps within 1-2 bpm:
    - the poco rit. of bars 45-46 and 145-146 run identically, 125.0 → 113.0;
    - the rit. of bars 66-68 falls 117 → 86.5;
    - the allargando of bars 121-122 falls 123 → 102, into the sostenuto at 100;
    - the rit. of bars 165-166 falls 99 → 79.5;
    - the rit. of bars 177-178 falls 71 → 51.5, into Tempo I at 50.
  - **Lento → Allegro.** The Lento's last arc slows beat 56 to 44 bpm, and the Allegro starts at 126.
- **Bar-170 fermata.**
  - The ff chord stops at qn 679 (380.20 s).
  - The master falls from -13 to -38 dB by +0.8 s and to -65 dB by +2.1 s.
  - The cello's Più lento starts at 382.7 s (qn 680), so the fermata holds 2.5 s of silence.
- **Attacca ending.**
  - Over the 8 s of bar 182 the morendo falls steadily, -39 → -50 dB.
  - The master is at -60 dB at 433.0 s and -85 dB at 434.0 s.
  - The mp3 is 434.85 s long, a 1.5 s tail. Nothing hangs over the attacca.
- **Bar 159 → 160.** The caesura makes the master dip 3.4 dB at 355.6 s. The suspended cymbal peaks 0.03 s after qn 636. The fff arrives with a tutti median of +0.02 s.
- **Keyswitches.** Every keyswitch comes 14 ms or more before the note it serves. The seven that follow a note-on by 16-65 ms (Clarinet 1 152.6, Violins I 127.78/159.78/259.63/271.78/455.61, Violas 152.86) are meant for the next, moved note, which is correct.
- **Tutti onsets.** At 100, 104, 160, 284, 324-330, 484, 520, 548, 636 and 664 the median stem arrival is -0.01..+0.04 s. The brass and timpani sit within ±0.05 s of the ensemble. Measured against the other tracks at the same onsets, the brass median deviation is -0.03..+0.00 s. The c19 ACC_ART_LEAD, RETONGUE_LEAD_S and TIMP_DELAY_S work.
- **Phrase endings.** Releases fall 10 dB a median 0.11-0.30 s after the written end on every track. There are no clipped endings; the apparent early ones are accented notes falling inside their own swell. There are no hanging tails over 0.5 s except basses 430 (+1.09 s, pp) and Horn 4 406 (+0.70 s).
- **BRIEF item 7.** Master 100-300 Hz / centroid autocorrelation at 3.95 s:

  | Passage | Band | Centroid |
  |---|---|---|
  | Lento 5-12 | -0.11 | 0.00 |
  | second theme 47-61 | 0.04 | -0.03 |
  | Tempo I 179-182 | -0.32 | -0.12 |
  | largamente 160-164 | -0.08 | 0.37 |
  | coda 175-178 | -0.05 | 0.34 |

  None of these is a loop pulse; the last two centroid values are inferred to be harmonic rhythm.
- **BRIEF item 8.** 2-5 kHz in the first 80 ms minus the body on accented notes:
  - brass medians -7.7..-12.3 dB, strings -7.5;
  - the only values over +3 are the known Horn 2 665 (+6.5, the 16th pickup) and Violas 536 (+10.8, the ringing double stop), plus Horn 3 91 (+4.8) and Oboe 1 113 (+4.9).

The sections below are what remains. All of it is in the strings and Clarinet 1, where the lead rules do not reach.

## 1. Legato targets after an eighth are held at the 0.45 lead cap on Violins II, violas and celli: 141 notes cross 0.09-0.16 s late (measured)

**Where.** Every Leg Slur MAX / Leg BC MAX target that follows an eighth. Worst stretches:
- **Celli:** second-theme arpeggios, bars 48-67 and 148-157 (195.5, 196, 209.5, 210, 221.5, 231, 255-257.5, 260.5-261.5, 264.5, 594, 595.5, 606, 609.5, 610, 623.5, 626), plus bars 72, 78, 104-105 and 131-134.
- **Violas:** theme and counter-lines, bars 20, 27-39, 55-61, 73, 82-97, 108-109, 148-157 and 167-169.
- **Violins II:** bars 27-31, 41-44, 57-73, 82-121 (the development's Leg BC lines) and 139-157.

**What is wrong.** The lead these targets actually got is 0.107 s at 126 bpm and 0.116-0.121 s at 112 bpm. Those are exactly 0.45 × an eighth: the LEG_CAP_FRAC default binds. The tracks' own leads are 0.20-0.24 s. Crossover, by group:

| Track | Capped targets (lead < 0.15 s): n, median, p75 | Cap-free targets: median |
|---|---|---|
| Violins II Leg Slur | 18, +0.163, +0.246 | -0.014 (n 36) |
| Violins II Leg BC | 21, +0.089, +0.142 | +0.034 (n 26) |
| Violas Leg Slur | 34, +0.119, +0.161 | -0.019 (n 33) |
| Violas Leg BC | 13, +0.110, +0.149 | +0.043 (n 15) |
| Celli Leg Slur | 56, +0.112, +0.154 | +0.042 (n 64) |

Own-pitch arrival agrees, so this is not the hall tail of the old note. Celli capped Leg Slur targets arrive at +0.095 against +0.041 for cap-free ones; violas +0.140 against +0.022.

These lines play an eighth of 0.24-0.27 s, so a +0.12..+0.16 s crossover means the new pitch sounds for only the second half of its slot. In the second theme the celli's slurred arpeggios lag the harp and the horn by half an eighth. The c21 fix reached only the 18 listed rising leaps; the other capped celli steps there are still +0.14..+0.17.

Violins I, which has had LEG_CAP_FRAC 0.75 over 56-728 since c06, has no capped targets: its legato median is +0.060 with p90 +0.107.

**Fix.** In `build/score_config.py`:
- LEG_CAP_FRAC 0.75 over the whole movement for the three tracks, unconditional:

  ```
  LEG_CAP_FRAC = dict(LEG_CAP_FRAC, **{t_: [(0.0, 728.0, 0.75)] for t_ in ("Violins II", "Violas", "Violoncellos")})
  ```

  This replaces the celli's two "listed" spans; keep the celli's `leg_leads.json` +0.06 s extras.
- `LEG_MIN_GAP_S = {"Violoncellos": 0.10, "Violas": 0.10, "Violins II": 0.10}`, so every eighth keeps at least 0.10 s after its own moved onset, including unled slur heads.

LEARNINGS section 5 records the precedent: the viola triplets with cap 0.75 went from +0.053 to -0.017 s.

**Check (pass criteria set before the render):**
- capped-group medians ≤ +0.05 s on each track, with no target earlier than -0.08 s;
- no eighth sounding less than 0.10 s before the next moved onset (diff parts.json);
- join dips of 6 dB or more on these three tracks not above c22. c21 saw celli dips go 12 → 16 with the listed cap, so run `auto_fills.py` after.

## 2. Abutting Sus MAX string notes get no lead: 94 viola notes cross +0.108 s, and the violas trail the brass by 0.08 s in the theme (measured)

**Where.**
- **Violas**, unslurred and pair-slurred Sus MAX eighths and quarters that follow another note with no gap:
  - bars 27-29 and 34-38;
  - bars 69-71: the f eighth pairs under the horn/trumpet theme, score p. 6;
  - bars 88-121: the development strokes, including 398-407, 441-463 and the triplets 464.33-483.33;
  - bars 138-142;
  - bars 167-169: the violas double the brass theme ff, score p. 16.
- **Celli:** bars 78-79, 85-89, 104-105 and 131-134.
- **Violins II:** bars 21, 27-28, 70-71, 92 and 139-141.

**What is wrong.** These notes take none of the lead branches:
- RETONGUE needs a gap;
- the entry branch needs a 0.5 qn rest;
- SHORT_SUS_LEAD covers only Violins II's slurred notes;
- ABUT_LEAD reaches the violas only at the seven listed hemiola onsets.

Crossover:

| Notes | n | Median | Arrival median |
|---|---|---|---|
| Violas, unled | 94 | +0.108 s | +0.063 s |
| Violas, led | 11 | +0.016 s | |
| Celli, unled | 22 | +0.119 s | |
| Violins II, unled | 17 | +0.099 s | |
| Violins II, slurred Sus MAX with the 0.06 s SHORT_SUS_LEAD | 41 | +0.084 s | |

At the 21 shared onsets of bars 69-71 and 167-169, violas minus Horns a2 / Trumpet 1 has a median of +0.08 s: half of a 126 bpm eighth. Examples:

| Onset | Violas | Brass |
|---|---|---|
| 279 | +0.19 | +0.05 |
| 280 | +0.155 | +0.05 |
| 671.5 | +0.14 | +0.01 |
| 674.5 | +0.145 | +0.045 |

Measured against all tracks at the same onsets, unled viola Sus MAX notes run +0.052 behind, celli +0.091.

The basses' version of this problem was fixed in c07/c20: ABUT_LEAD ends the old note at the moved start, and the median went from +0.155 to +0.07 s.

**Fix.** In `build/score_config.py`, list the measured onsets. A generic rule would also capture Leg → Sus notes that now take the c06 entry path.

```
ABUT_LEAD["Violas"]["at"] += [107.0, 107.5, 110.0, 111.5, 114.5, 134.5, 135.0, 135.5, 137.0, 148.5, 149.0, 149.5, 152.75,
  272.5, 273.5, 275.0, 276.0, 278.0, 278.5, 279.0, 280.0, 281.0, 282.0, 283.0, 353.0, 366.0, 388.5, 394.0, 397.0,
  398.0, 399.0, 401.0, 402.0, 403.0, 405.0, 406.0, 407.0, 427.5, 435.5, 441.0, 443.0, 449.0, 453.0, 454.0, 460.0,
  461.0, 463.0, 464.3333, 469.3333, 471.3333, 481.3333, 483.3333, 553.0, 555.0, 557.0, 558.0, 559.0, 561.0, 563.0,
  564.0, 567.0, 667.0, 667.5, 670.0, 671.5, 674.5]
ABUT_LEAD["Violoncellos"] = dict(ABUT_LEAD["Violins II"], at=[312.5, 313.0, 341.0, 350.0, 350.5, 355.0, 417.5, 419.0,
  522.5, 523.0, 523.5, 525.0, 527.5, 530.5, 531.0, 531.5, 533.0])
ABUT_LEAD["Violins II"]["at"] += [80.5, 109.0, 110.0, 111.5, 278.0, 279.5, 282.0, 283.5, 365.0, 554.5, 558.0, 561.5]
SHORT_SUS_LEAD_S = 0.10   # Violins II only; KEEP_OVERLAP 0.03 stays
```

The values are lead_s 0.10, overlap 0 and skip_next_same False, as for the hemiola entries. Not listed: celli 484 (the DOWNBOW stroke) and violas 536 (the ringing double stop).

**Cautions.**
- The violas' 388.5-408 and 464-484 strokes carry the c05 roles (ROW_TRIM_SKIP). A lead does not change their level, but re-check those roles.
- Check the repeated notes next to each moved note for new holes (LEARNINGS section 6).

**Check:**
- listed medians ≤ +0.04 s on each track;
- violas minus brass at the 21 theme onsets ≤ +0.03 s;
- no new trough of 6 dB or more of 0.05 s or longer.

## 3. Clarinet 1's legato has no lead and is the latest wind line (measured)

**Where.** Clarinet 1 Leg Slur targets throughout. The clarinets' a2 theme in bars 69-71 doubles the horns. Others: the second-theme counter-lines (bars 52-65, 152-156), bars 26-29, 102-105 and 131-140.

**What is wrong.** `LEG_LEAD_S["Clarinet"] = 0.0` since c03, set from the time-shifted c02 render. Measured now:
- Clarinet 1 Leg Slur crossover median +0.076 s (n 98), Allegro eighths +0.052, p90 +0.122.
- Against the other tracks at the same onsets: +0.045 s (n 55).
- Flute 1 and Oboe 1, with 0.03 s leads, cross +0.030 / +0.028, and deviate -0.010 / -0.007.
- Examples: 115.5 +0.15, 246 +0.17, 249 +0.14, 276.5 +0.14, 277.5 +0.16, 411.5 +0.20, 419.5 +0.12, 532 +0.28.

**Fix.** In `build/score_config.py`: `LEG_LEAD_S["Clarinet"] = 0.05`. The Clarinet KS Master's "Leg Slur" row takes it like the other winds.

**Check:** Clarinet 1 Leg Slur median ≤ +0.04 s and deviation from the others within ±0.02 s; no Leg Slur target before -0.06 s.

## 4. Upper-string Leg BC targets cross 0.05-0.06 s after Leg Slur targets at the same lead (measured)

**Where.** Leg BC MAX joins (connected unslurred notes and slur-to-slur joins) on Violins II and violas. The worst are the development's Leg BC lines (bars 82-101, 117-121) and Violins II 392 (+0.25) and 471.5 (+0.33).

**What is wrong.** On cap-free targets, so independent of finding 1:

| Track | Leg BC (lead) | Leg Slur (lead) |
|---|---|---|
| Violins II | +0.034 (0.17 s: 0.20 - 0.03 from LEG_ART_EXTRA_S) | -0.014 (0.24 s) |
| Violas | +0.043 (0.20 s) | -0.019 (0.225 s) |

Measured against the other tracks at the same onsets, Leg BC targets run +0.035 (Violins I), +0.045 (Violins II) and +0.046 (violas) behind, while Leg Slur targets run -0.02 / -0.03 / +0.026.

Movement II's c15 per-articulation offsets set Leg BC 0.03 s *later* than Leg Slur. In this movement's Allegro the sign is reversed.

**Fix.** In `build/score_config.py` LEG_ART_EXTRA_S:
- Violins II `"Leg BC MAX": -0.03 → +0.03`;
- Violas add `"Leg BC MAX": +0.05`;
- celli unchanged: Leg BC +0.072 against Leg Slur +0.067 overall is already level.

Apply this after finding 1 in the same build. Both act through the lead, and the 0.75 cap leaves room.

**Check:** cap-free Leg BC medians within 0.02 s of Leg Slur on both tracks, and no Leg BC target before -0.08 s.

## 5. Three string re-attacks on Leg Slur MAX get no lead (measured; small)

**Where.**
- Bar 30, qn 118: Violins I/II and violas, f, after a short gap.
- Bar 96, qn 383: Violins II, f.

**What is wrong.**
- RETONGUE_LEAD_S strings apply to Sus MAX only, and the entry branch needs a 0.5 qn rest, so these play from the score onset.
- Arrivals:

  | Onset | Violins I | Violins II | Violas |
  |---|---|---|---|
  | 118 | +0.20 | +0.20 | +0.09 |
  | 383 | | +0.25 | |

  The winds at 118 are at +0.01..+0.08.
- The other Violins II Leg Slur entries with the 0.06 s mid lead arrive at a median +0.138 (n 16), +0.099 behind the others. Examples: 324.5 +0.14, 516 +0.16, 521 +0.17, 529 +0.14, 568.5 +0.15.

**Fix.**
- `build/entry_leads.json`: Violins I 118 +0.10, Violins II 118 +0.10 and 383 +0.10, Violas 118 +0.05. These are extras, which let the entry branch take a gap of 0.2 qn or more.
- For the Violins II Leg Slur entries: ENTRY_LEAD_ART_S for Violins II with `"Leg Slur MAX": 0.06`, so the mid-entry total is 0.12 s, under ENTRY_CAP_S.

**Check:** these onsets within ±0.05 s of the winds; first sound no earlier than -0.15 s.

## 6. Tempo shaping at the two broad climaxes and the animando tops (inferred; small)

**What is measured.**
- The sostenuto (bars 123-126) and the largamente (bars 160-164) are the only long stretches with no tempo shaping at all: 36 beats at exactly 100.0 bpm, 21.6 s.
- The animando ramps extrapolate past their printed last step: bar 65 ends at 120.1 (printed 118) and bar 159 at 120.9 (printed 120). The rit. of bar 66 then starts 2.6% slower, 120.1 → 117.0 at the barline.

**What is inferred.** At the climax, a broad tempo with no give on the arrival bars sounds mechanical next to the shaped Allegro. The bar-65 step is a small hitch inside one gesture: an animando, then a rit.

**Fix.** In `build/score_config.py`:
- PHRASE_ARCS add `(636, 648, "sub")` (bars 160-162, the fff bars falling to bar 163's mp) and `(488, 504, "sub")` (the sostenuto into the a tempo). Re-bows are frozen in qn, so they do not move. Both arcs keep ARRIVAL_WEIGHT_AT 636/484 and the caesura.
- RAMP_SPANS `(244, 260, 115)` → `(244, 252, 115)` and `(620, 632, 115)` → `(620, 628, 115)`, so bars 64-65 and 158-159 hold the printed 118/120.

**Check:**
- bars 160-162 and 123-126 slow 2-5% only on their last two beats;
- bar 65 → 66 drops by no more than 1.5%;
- no beat inside 576-584 or 656-664 faster than the beat before;
- the 636 arrival, the limiter and the climax order are re-measured.

## Do not touch

Keep:
- the RAMP_SPANS realisation of the printed steps and the rit. clamp in `smooth_tempo`;
- the arcs with their "open"/"sub" depths, the bar 145-146 tempo, and BEAT_STRETCH 284/285/679;
- CAESURA {636: 0.15} with the suspended-cymbal key 64 / lead 0.25;
- the 30 bpm final bar and the mp3 tail;
- TIMP_DELAY_S 0.045;
- keyswitch placement;
- ACC_ART_LEAD, RETONGUE_LEAD_S (winds, brass, upper strings Sus) and the brass/wind entry and ABUT leads, since brass and winds sit within ±0.03 s of the ensemble;
- Violins I's LEG_CAP_FRAC 0.75 and leads, SLUR_HEAD_LEAD 0.10 and the Slur Runs spans;
- the basses' ABUT_LEAD 0.12 and STR_REP_DETACH;
- the UNI_DELAY hand-overs (Oboe 2 628, Horn 3 418 start 0.75 qn late by design);
- `_REBOW_FROZEN` with its fitted shapes.
