# Cycle 27, critic C: tempo, timing and transitions (render c26)

Lens: the tempo map against the printed tempos and the rit./allargando/animando/largamente steps; the Lento/Allegro changes; attack latency of legato and sustain samples in the fast Allegro figures and lead compensation; keyswitch lead times; note starts between sections; phrase endings, the fermatas and the attacca ending.

## Method

Material: the stem-fixed c26 render (`cycles/c26/render/`) and `cycles/c26/rendered_build/parts.json`. Its notes, keyswitches and tempo map are identical to c25. I ran the same scan on c22 (`cycles/c22/render/`, `cycles/c22/rendered_build/parts.json`) as a control for the c23-c25 timing changes. Score qn were converted to file time on each render's own tempo map. The scratch scripts are deleted (BRIEF rule). They worked as follows:

- **Per-note scan.** Every single-voice note on the wind, brass and string stems (chords and notes after chords skipped). STFT of 2048 points, 5 ms hop, summed L+R power. Own-pitch energy is harmonics 1-4 at ±3% or ±1.2 bins.
  - **Crossover:** the first time from score onset - 0.3 s at which the new pitch's energy, without the harmonics it shares with the old pitch, stays above the old pitch's for 30 ms. Pitch changes with a played gap of 0.25 s or less, both pitches C3 or higher.
  - **Arrival:** the first time own-pitch energy is within 6 dB of its maximum over [-0.25, +0.8] s.
  - Values of -0.2 s or less were dropped as window artefacts.
- **Ensemble deviation.** At every score onset where three or more tracks change pitch: each track's crossover minus the median of the others.
- **Tutti onsets.** Broadband arrival (20 ms frames, peak - 6 dB) at the 40 onsets where 10 or more tracks start a note. For the outliers I also took 50 ms frames around the onset.
- **Phrase endings.** For 425 notes of 0.5 qn or longer followed by at least 1 qn of rest: the time from the played end until the stem falls 10 dB under its last body.
- **Also measured:**
  - the tempo map beat by beat, against `global.ily`;
  - the evaluated `PHRASE_ARCS` / `TEMPO_PUSH` / `BEAT_STRETCH`, by running the head of `score_to_parts.py` and the config in a scratch namespace, set against every printed crescendo span in `build/mockup-events.tsv`;
  - keyswitch-to-note gaps;
  - the master around the end;
  - BRIEF items 7 and 8: `cycles/c25/actor_scripts/loopscan.py`, and my own 2-5 kHz first-80-ms minus body measure on every accented note of 0.5 s or longer.

## Checks that pass (measured)

- **Tempo map.**
  - Total length is 433.48 s.
  - Every printed step is played.
  - Every rit. ramp follows its printed steps within 1-2 bpm:

    | Bars | Ramp |
    |---|---|
    | 45-46 / 145-146 | 125.0 → 113.0 |
    | 66-68 | 117 → 86.5 |
    | 121-122 | 123 → 102, into the sostenuto at 100 |
    | 165-166 | 99 → 79.5 |
    | 177-178 | 71 → 51.5, into Tempo I at 50 |

  - The Lento's last beat is at 44, and the Allegro starts at 126.
  - The c24 arcs give the sostenuto and the largamente their last-beat give: bar 126 runs 98/95, bar 162 runs 98/95.
  - Bar 170 runs 126 / 123.5 / 119.7, then the 2.5 s fermata beat.
- **The c23 lead changes worked.** Allegro crossover medians, c22 → c26:

  | Group | c22 | c26 |
  |---|---|---|
  | Violas Leg | +0.075 | +0.030 |
  | Violas Sus MAX | +0.100 | +0.050 |
  | Violins II Leg | +0.040 | +0.015 |
  | Violins II Sus MAX | +0.080 | +0.040 |
  | Violoncellos Leg | +0.070 | +0.050 |
  | Violoncellos Sus MAX | +0.115 | +0.065 |
  | Clarinet 1 Leg | +0.080 | +0.045 |

  Ensemble deviation by track is now within ±0.03 s for every wind, brass and upper-string group except the two in finding 1.
- **Tutti onsets.** The median stem arrival is -0.06..+0.06 s at all 40 onsets, including the section changes at 128, 272, 330, 440, 464, 484, 520, 548, 636 and 664.
  - The late outliers are not latency. Bassoon 2 at 272, Oboe 1 at 664 and Flute 2 at 664 sound within 0.05 s of the onset in 50 ms frames, and the -6 dB arrival is late only because the line grows louder over the next notes.
  - Oboe 2 at 628 is the UNI_DELAY hand-over.
  - Tam-tam 484, crash 636 and tam-tam 696 first sound at +0.05 s (delay_s), as set.
- **Keyswitches.** All 1061 come 10 ms or more before the note they serve.
  - The three that follow a note-on by 16-23 ms (Violins I 127.782, 159.782, 271.783) belong to the next, moved note.
  - The 10 ms gaps are the frozen celli re-bows.
- **Phrase endings.** Per-track release medians are 0.11-0.30 s. The six tails over 0.6 s are all soft (body -34..-59 dB): Cor anglais 371, Horn 3 264, Tuba 160, Oboe 2 568, basses 216, Trumpet 3 160.
- **Attacca.**
  - The master falls -44 → -52 dB over bar 182, reaches -61 dB at 433.0 s and -82 dB at 434.0 s.
  - The mp3 is 434.95 s long. Nothing hangs over the attacca.
- **BRIEF item 7** (loop autocorrelation at 3.95 s, band / centroid).
  - Master: final chord -0.39 / -0.08; bars 175-178 -0.12 / +0.08; bars 160-164 -0.47 / -0.18; Lento bars 5-12 -0.08 / -0.18.
  - Of the 47 held spans of 6 s or more, only two reach 0.5:
    - Violoncellos 11: 0.69 / 0.53 on a 6.3 s "short" window, inferred to be the c26 bar-3 swell plus the printed decrescendo;
    - Violoncellos 504: centroid 0.52 on 40 tremolo pieces, not a loop.
- **BRIEF item 8** (2-5 kHz, first 80 ms minus body). Medians: brass -14.7 dB (max -2.5), winds -11.8, strings -10.1. Only three accents are over +3:
  - Violoncellos 536 (+8.3, the known ringing double stop);
  - Bassoon 1 536 (+7.1);
  - Clarinet 1 414 (+5.4).

## 1. Violins I legato and celli Leg BC targets are the late strings now: 0.04-0.05 s behind the other sections (measured)

**Where.**
- Violins I Leg BC MAX targets throughout the Allegro (84 targets; bars 16-43, 58-65, 80-82, 94-102, 112-141, 156-164).
- Violins I Leg Slur MAX targets after an eighth (slot under 0.3 s): the first theme bars 15-22 and 27-40, bars 57-71, and the recapitulation 139-164.
- Violoncellos Leg BC MAX targets (78), mostly after notes of 0.5 s or longer: bars 15-31 and 88-116, and the recapitulation 135-149.

**What is wrong.** The c23 fixes gave Violins II and violas leads of 0.20-0.25 s, and the c15/c03 extras gave celli Leg Slur 0.20-0.22 s. Violins I is still on the 0.17 s string default, and celli Leg BC on 0.11 s (`LEG_ART_EXTRA_S["Violoncellos"]["Leg BC MAX"] = -0.06`, set in c03 on the time-shifted c02 render).

| Group | n | Crossover median | Arrival median | Deviation from the others |
|---|---|---|---|---|
| Violins I Leg BC (lead 0.17) | 84 | +0.065 | +0.062 | +0.046 (n 78) |
| Violins I Leg Slur after an eighth (lead 0.17, at the 0.75 cap of 0.179 s) | 54 | +0.075 | | |
| Violins I Leg Slur after longer notes | 47 | -0.015 | | +0.003 overall |
| Violoncellos Leg BC (lead 0.11) | 78 | +0.080 | +0.015 | +0.040 (n 59) |
| Violoncellos Leg Slur (lead 0.20-0.22) | 105 | +0.035 | -0.055 | -0.005 |
| Violins II Leg BC / Leg Slur | | +0.007 / +0.020 | +0.033 / +0.038 | |
| Violas Leg BC / Leg Slur | | +0.010 / +0.033 | +0.030 / +0.018 | |

- On Violins I the crossover and the new pitch's own arrival agree (+0.06/+0.07), so this is real lateness, not the hall tail (LEARNINGS section 5).
- In the theme's eighths a +0.075 s crossover is a third of the note. The melody now sounds after the accompaniment that doubles it, since Violins II and violas are on time.
- On the celli, crossover and arrival are both 0.045-0.07 s later than the celli's own Leg Slur targets.

**Fix.** All in `build/score_config.py` and `build/leg_leads.json`:

- **Violins I Leg BC:** `LEG_ART_EXTRA_S["Violins I"] = {"Leg BC MAX": 0.05}`.
- **Violins I Leg Slur after eighths.** Add these 30 onsets to `leg_leads.json` "Violins I" at +0.05 (crossover ≥ +0.05 and arrival ≥ +0.04 on both measures; 118 left out, it has its entry_leads extra):

  ```
  59.0, 67.5, 69.5, 75.5, 81.0, 84.5, 85.0, 107.0, 147.5, 151.0, 153.0, 156.5, 157.0, 230.0, 231.5, 240.0, 243.5,
  265.5, 276.0, 282.0, 315.0, 398.0, 399.5, 407.5, 454.0, 555.5, 556.5, 571.0, 627.5, 643.5
  ```

  With them:

  ```
  LEG_CAP_FRAC["Violins I"] = [(56.0, 728.0, 0.95, "listed"), (56.0, 728.0, 0.75)]
  LEG_MIN_GAP_S["Violins I"] = 0.10
  ```

  The listed cap must come first, because `next()` takes the first matching entry. At 0.75 the 0.22 s lead is capped at 0.179 s on a 126-bpm eighth. LEG_MIN_GAP_S keeps 0.10 s of every eighth after its own moved onset.
- **Violins I Leg BC targets already early on both measures:** `leg_leads.json` "Violins I" 228.0, 373.0, 477.0, 523.0 at -0.05, which cancels the new extra.
- **Celli Leg BC:** `LEG_ART_EXTRA_S["Violoncellos"]["Leg BC MAX"]` -0.06 → -0.02 (lead 0.15). I take 0.04 rather than the full crossover gap because the arrival is already +0.015. The four celli Leg BC targets already early (192, 568, 600, 628 at -0.035..-0.045) get `leg_leads.json` -0.04. Celli 628 is next to the Violins I/II 628 stroke; check it.

**Cautions.**
- A lead change moves each transition spike and sag by the same amount. Move every Violins I / celli `JOIN_NOTCH` and hand fill on a changed Leg BC or listed target 0.04-0.05 s earlier, or refit them. That includes the Violins I (637.6, 638.1) notch, the c26 celli (595.66, 595.92) notch if 596 is Leg BC, and the 711.855 fill.
- After the render, rerun `auto_fills.py --guard-existing` for these two tracks.
- Diff parts.json `art_counts`: nothing should change.

**Check (pass criteria):**
- Violins I Leg BC crossover median ≤ +0.03 s and deviation within ±0.02;
- the 30 listed Leg Slur targets median ≤ +0.04;
- celli Leg BC deviation within ±0.02;
- no new target before -0.08 s;
- string join dips of 6 dB or more on these two tracks no more than c26.

## 2. In the development, the phrase arcs slow down inside the crescendo to letter G and inside the ff letter-F phrase (measured tempo; effect inferred)

**Where.** Arcs `(384, 396)`, `(432, 440, "main")` and `(440, 452, "sub")`, bars 99, 110 and 113.

**What is measured.** Beat tempos on the parts.json map:

| Bar | Beats | Context |
|---|---|---|
| 99 | 126 / 126 / 121.0 / 115.9, then bar 100 at 122.2 / 127.9 | The middle of the 6-bar ff phrase of letter F (bars 97-102, score p. 9). The violas' unbroken eighths stretch from 0.238 to 0.259 s and then snap back. |
| 110 | 126 / 126 / 119.7 / 110.9 (a "main" 12% slowing) | 8 of the 9 sounding staves are inside a printed crescendo (Vln II, Vc, Bn p <, Hn 3 pp <, into bar 111). |
| 113 | 121.0 / 126 / 123.5 / 119.7, then +1% push 114-116 | 22 of 22 sounding staves are in the printed mp cresc. of bars 111-116 to the ff of bar 117 (score p. 10). |

In the 68 beats of bars 97-113 the tempo slows at seven arc ends. This is the every-two-bars hitch that c15/c16 removed from bars 15-22.

Of every non-open arc in the movement, these two are the only ones whose slowing falls where 30% or more of the sounding staves are inside a crescendo. The others are bar 9 in the Lento (48 → 46) and bar 90 (2 of 4 staves).

**What is inferred.** The build to letter G is one gesture, six bars of crescendo by the whole orchestra. Easing off at bar 113 and then pushing works against it. The bar-99 slowing breaks a phrase that runs on through bar 102.

**Fix.** In `build/score_config.py`, a PHRASE_ARCS map after the c24 block:

```
PHRASE_ARCS = [(384, 396, "open") if x_[:2] == (384, 396) else (432, 440, "sub") if x_[:2] == (432, 440)
               else (440, 452, "open") if x_[:2] == (440, 452) else x_ for x_ in PHRASE_ARCS]
```

Keep `(396, 408, "main")` (the section end at bar 102 → 103), `(408, 416, "sub")`, `(416, 424)`, `(424, 432, "sub")` and the 452-464 push.

**Cautions.**
- Re-bows are frozen in qn and LEVEL_SHAPES_S convert on the new map, so neither moves.
- Diff parts.json `art_counts`. In c11, an arc change turned short slurred notes into legato targets.
- Re-measure the letter-G arrival at 464 and the 484.53 limiter peak.

**Check:**
- bars 110-116: no beat more than 2% slower than the beat before;
- bar 99 → 100 changes by no more than 2%;
- the arcs' seconds over 384-464 within 0.3 s of c26;
- `art_counts` unchanged.

## 3. 24 string legato targets sound 0.08-0.19 s early, on both measures (measured)

**Where and what.** Targets whose crossover and own-pitch arrival are both -0.05 s or earlier, almost all on the full 0.20-0.25 s leads (Leg Slur extras and the c23 Leg BC extras). Values are crossover / arrival in seconds.

| Track | Onsets |
|---|---|
| Violins II | 39.0 -0.12/-0.125, 119.5 -0.095/-0.09, 262.0 -0.10/-0.10, 500.0 -0.095/-0.095, 523.0 -0.105/-0.065, 654.0 -0.095/-0.10 |
| Violas | 42.0 -0.085/-0.065, 119.5 -0.185/-0.165, 178.0 -0.155/-0.155, 496.0 -0.115/-0.22, 501.0 -0.10/-0.22, 589.0 -0.10/-0.085, 600.0 -0.085/-0.08, 647.0 -0.08/-0.085, 682.0 -0.10/-0.23 |
| Violoncellos | 10.0 -0.125/-0.125, 225.5 -0.085/-0.095, 369.0 -0.10/-0.25, 555.0 -0.11/-0.195, 562.0 -0.125/-0.12, 593.5 -0.09/-0.25, 616.0 -0.155/-0.18, 643.0 -0.14/-0.15, 646.0 -0.08/-0.05 |

- Violas 589/600 and celli 562/616 were already on the c23 open list.
- At 119.5, Violins II and violas both land 0.1-0.18 s ahead of Violins I and the winds (deviation -0.18 for violas).
- These are the c23-era leads applied to transitions that were already fast. LEARNINGS section 5 says the lag depends on the source pitch and the interval.

**Fix.** `build/leg_leads.json`, negative per-onset extras of (|earlier of the two values| - 0.03), rounded:

```
Violins II: {"39.0": -0.09, "119.5": -0.06, "262.0": -0.07, "500.0": -0.06, "523.0": -0.05, "654.0": -0.07}
Violas: {"42.0": -0.04, "119.5": -0.15, "178.0": -0.12, "496.0": -0.08, "501.0": -0.07, "589.0": -0.06,
         "600.0": -0.05, "647.0": -0.05, "682.0": -0.07}
Violoncellos (add to the existing 18): {"10.0": -0.09, "225.5": -0.06, "555.0": -0.08, "562.0": -0.09,
         "593.5": -0.06, "616.0": -0.12, "643.0": -0.11, "646.0": -0.03}
```

Leave celli 369 out: its arrival is a window artefact. LEG_LEAD_CLAMP (0.03 s minimum) limits the largest cuts. Move any JOIN_NOTCH / fill on these onsets with them (finding 1 caution).

**Check:** the listed onsets within -0.04..+0.04 s on both measures, and none of their neighbours moved.

## 4. The Più lento cello solo changes tempo direction five times in 12 beats (measured map; effect inferred)

**Where.** Bars 171-174 (qn 680-696), arcs `(680, 688, "sub")` and `(688, 696, "main")` with their apex holds.

**What is measured.** Beat tempos:

| Bar | Beats |
|---|---|
| 171 | 72 / 72 / 72 / 72 |
| 172 | 72 / 69.1 / 70.6 / 68.4 |
| 173 | 69.8 / 73.1 / 73.1 / 73.1 |
| 174 | 69.1 / 72 / 68.4 / 63.4 |
| 175 | 72 (the chorale and tam-tam pp) |

Each change is 2-7%, and the fastest beats (73.1) come straight after the slowest (68.4). The printed phrase is one 4-bar cello line, mp espr., with < > hairpins and the cor anglais against it (score p. 17). Two 2-bar arcs plus two apex holds make it lurch.

**Fix.** Replace the two arcs with one:

```
PHRASE_ARCS = [x_ for x_ in PHRASE_ARCS if x_[:2] not in ((680, 688), (688, 696))] + [(680, 696, "main")]
```

This keeps the push to the middle of the line, one apex hold on its top note, and the 0.95/0.88 phrase end into bar 175. The violas' two frozen re-bow points (686.694, 699.507) stay in qn.

**Small item on the same lens:** bars 64-65 are played at 119.4 against the printed 118 (c24 open item). The (244, 252, 115) ramp extrapolates past the last step, and the bar-66 rit. then starts 2% lower (117). It is under 1.5%, so leave it unless `smooth_tempo` gets a generic option to end an animando ramp on its last printed step when the score holds that step afterwards.

**Check:** bars 171-174 change direction no more than twice; bar 174 → 175 unchanged; the cello solo's seconds within 0.2 s of c26.

## 5. Not a finding: horn and Bassoon 1 legato crossovers read late but arrive on time (measured)

Allegro Leg Slur crossovers:

| Track | Crossover |
|---|---|
| Horn 1 | +0.045 |
| Horn 2 | +0.070 |
| Horns a2 | +0.065 (the theme of bars 69-71/167-169: 275 +0.21, 281 +0.18, 675.5 +0.17) |
| Bassoon 1 | +0.073 |

The new pitch's own arrival is -0.003 / +0.015 / -0.003 / +0.018. That is the legato overlap and the hall tail of the old note, not a late new note (LEARNINGS section 5: change a lead only when both measures agree). Do not raise the Horn/Bassoon leg leads on this evidence.

## Do not touch

Keep these as they are:
- **Tempo map:**
  - the RAMP_SPANS realisation, with the rit. clamp in `smooth_tempo`;
  - the c24 arcs (184-200, 488-504, 636-648, 664-679 with APEX_SKIP 664);
  - CAESURA 636 0.15 with the suspended-cymbal key 64 / lead 0.25;
  - BEAT_STRETCH 284/285/679 (the 2.5 s bar-170 fermata);
  - the 30 bpm final bar and the mp3 tail.
- **Lead rules:**
  - the c23 string leads: LEG_CAP_FRAC 0.75 and LEG_MIN_GAP_S 0.10 on Violins II/violas/celli, the ABUT_LEAD lists with cap_frac, SHORT_SUS_LEAD 0.10, the Violins II/violas Leg BC extras, and STAC_LEAD_S;
  - Clarinet leg lead 0.05;
  - ACC_ART_LEAD, RETONGUE_LEAD_S, and the brass/wind entry leads (tutti medians -0.06..+0.06 s);
  - TIMP_DELAY_S 0.045 and the perc delay_s 0.05;
  - the Horn and Bassoon leg leads (finding 5).
- **Notes and keyswitches:**
  - keyswitch placement;
  - the UNI_DELAY hand-overs;
  - `_REBOW_FROZEN` with its fitted shapes;
  - the sus_release_cap_ms release timing.
