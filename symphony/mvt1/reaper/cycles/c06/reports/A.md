# Cycle 6, critic A: articulation and phrasing (render c05)

Scope: every wind, brass, string, timpani and harp note in `build/parts.json` (the c05 build, unchanged by the stem fix), measured on the c05 stems after the stem fix and on the master. Scripts and 5 ms feature files are in `/private/tmp/claude-501/mockup-loop/mvt1-c06-A/`. The c05-A scripts were rerun on c05 (`acc2.py`, `joins.py`, `rebow.py`, `breath.py`, `rep2.py`, `longloop.py`, `xall.py`). New scripts:
- `bows.py`: notes with printed bow marks.
- `ten2.py`: tenutos.
- `chordleg.py`: chords on legato rows.
- `ownp.py`: own-pitch share and per-note swing, c04 against c05.
- `trace3.py` and `lt.py`: level and brightness traces.
- Inline checks of the bar-160 arrival and of wind and brass repeats.

## Checks that passed (measured)

- **Accents (Dan's item 8).** 2-5 kHz energy in the first 80 ms minus the note body, median per track:

  | Family | Median range |
  |---|---|
  | Strings | -1.6..-5.7 dB |
  | Brass | -2.8..-16.8 dB |
  | Winds | -4.5..-11.2 dB |

  - Only Horn 1 at qn 665 reads +4.7 dB. That reading is level, not brightness: the attack's 2-5 kHz share of the total (-24 dB) is lower than the body's (-21 dB), and the note falls 6 dB after the swell.
  - The qn-536 outliers are the earlier-note artefact noted in c04 and c05.
- **Loop pulsing (Dan's item 7).** Master autocorrelation at 3.95 s (100-300 Hz / centroid):

  | Passage | Autocorrelation |
  |---|---|
  | Final chord, qn 712.5-727.5 | -0.14 / -0.02 |
  | Lento, qn 20-44 | -0.14 / -0.13 |
  | fff span, qn 464-484 | +0.14 / +0.14 |

  - Every string stem in these windows is between -0.30 and +0.18.
  - Re-bows: master dips at re-bows have a median of -2.3 dB, against -2.1 dB at control times in the final chord.
- **Legato structure.**
  - No chord is sent to a Leg row on any track (`chordleg.py`: no overlapping different-pitch notes over 0.12 qn).
  - `ks_clash` is empty.
  - Wind and brass legato joins have a median dip of 0.4-4.2 dB.
- **c05 strokes.** The violas' triplets in bars 117-121 now separate: own-pitch share in mid-note went from 0.20 (c04, Leg BC) to 0.48 (c05, Sus strokes).

## 1. The movement's climax downbeat (bar 160, qn 636, fff after the caesura) lands soft and late: the master dips 1.3 dB on the beat

**Measured, master.** Level relative to the window -0.45..-0.05 s before the beat:

| Downbeat | 0-0.15 s | 0.15-0.5 s | 30 ms peak |
|---|---|---|---|
| **Bar 160 (636)** | **-1.3 dB** | +0.9 dB | +0.9 dB |
| Bar 122 (484) | +0.9 | +3.1 | |
| Bar 26 (100) | +3.4 | +4.6 | |
| Bar 170 (676) | +2.5 | +3.8 | |

Of the 21 tutti downbeats measured, the fff climax has one of the weakest arrivals.

**Measured, per stem.** Two causes, both articulation:

1. **Winds and brass come in late after the caesura breath.** Flute 1/2, Oboe 1, Horn 1/2, Trumpet 1/3, Trombone 1 and Bass trombone have breath marks at 636, with `CAESURA` {636: 0.15}. The note after the breath starts exactly on the score onset (qn +0.000) with no entry lead. The entry-lead rule applies after a caesura breath only when the onset has a listed extra (`cb_` in `score_to_parts.py`, about line 2050), and `build/entry_leads.json` is empty.

   | Track | Reaches body - 3 dB |
   |---|---|
   | Trumpet 3 | **+0.17 s** (trough -17.6 dB) |
   | Oboe 1 | +0.16 s |
   | Trumpet 2 | +0.12 s |
   | Tuba | +0.10 s |
   | Flute 1 | +0.09 s |
   | Trombone 1 | +0.09 s |
   | Bass trombone | +0.08 s |

2. **The strings' fff downbeat is a legato transition.** The printed down-bow on Violins I/II at 636 (and Violins II at 628) is played as a Leg BC MAX join (v124) from the G6 before it. The transition sags at the beat:

   | Track | Trough at the beat |
   |---|---|
   | Violins I | -7.3 dB (stem -16 -> -26 dB from -0.1 to +0.04 s) |
   | Violins II | -6.2 dB |
   | Violoncellos (Leg BC, no mark) | -5.3 dB |

   In `bows.py`, every other down-bow at f or louder that follows a note is a Sus MAX stroke.

Inferred: the bar the whole movement builds to arrives as a dip with a soft front edge. After a printed breath and caesura, a real orchestra attacks together on the beat.

**Fix.**
- **Winds and brass:** `build/entry_leads.json`, extras at 636.0, so that each track's total lead is close to its measured lateness minus 0.02 s:

  | Track | Total lead |
  |---|---|
  | Oboe 1 | 0.12 s |
  | Trumpet 3 | 0.12 s |
  | Flute 1 | 0.07 s |
  | Flute 2 | 0.07 s |
  | Trombone 1 | 0.07 s |
  | Bass trombone | 0.06 s |
  | Horn 1 | 0.03 s |
  | Trumpet 1 | 0.03 s |

  - Brass loud tracks already get 0.05 s from `ENTRY_LEAD_S`, and wind Leg Slur MAX notes get 0.055 s from `ENTRY_LEAD_ART_S`. List only the remainder: for example Trumpet 3 +0.07, Oboe 1 +0.065 if it stays on Leg Slur MAX, Trombone 1 +0.02.
  - `ENTRY_CAP_S` and the `q - pe - 0.02` cap still apply. The caesura gives 0.12 qn of rest (`CAESURA_BREATH_QN`), which is about 0.1 s at the largamente tempo, so leads up to 0.10 s fit.
  - Do the same for the 632 breaths (Trumpet 2, Trombone 2, Tuba) only if they measure late.
- **Strings:** new table `DOWNBOW_STROKE_AT = {"Violins I": [636.0], "Violins II": [628.0, 636.0], "Violoncellos": [636.0]}` in `build/score_config.py`, read in the string articulation pass next to `STR_ACC_AFTER_SUS`. A listed note:
  - plays Sus MAX as a fresh stroke at the `REBOW_VEL_BY_CC` velocity for its level;
  - gets the loud string entry lead (0.06 s);
  - takes its previous note's end 0.02 qn before the moved onset (as the c06 Leg -> Sus entry path does);
  - takes the string `GENTLE_ACCENT` swell (+3 dB, full at +0.07 s, gone by +0.6 s).

  The note after it (the A-flat6 half note, slurred) stays a Leg Slur target. Check its join afterwards: it now joins from a Sus note, as `SHORT_SUS_JOIN` does.

**Pass criteria (c06 render).**
- Master 0-0.15 s after qn 636 at least +1.5 dB over -0.45..-0.05 s (now -1.3).
- Every listed wind and brass stem reaches body - 3 dB by +0.05 s.
- Violins I/II and celli trough at the beat no deeper than -3 dB.
- 2-5 kHz attack minus body at or below 0 dB on the new strokes.
- Climax order 160 > 122 > 169 kept: check with critic B's measure, because the strokes and swell add level.

## 2. Unslurred repeated notes in the winds and brass are not re-articulated: 197 of 228 repeats dip less than 3 dB, so repeated chords and pedals sound tied

**Measured.** Untied, unslurred, same-pitch repeats on wind and brass stems: lowest 30 ms level within -0.12..+0.1 s of the repeat, against the quieter of the 0.2 s before and after.

| Track | Repeats | Dip under 3 dB |
|---|---|---|
| Horn 3 | 29 | 28 |
| Horn 4 | 35 | 33 |
| Contrabassoon | 40 | 36 |
| Bassoon 1 | 18 | 12 |
| Horn 1 | 12 | 11 |
| Horn 2 | 12 | 12 |
| Trombone 1 | 8 | 7 |
| Trombone 2 | 11 | 9 |
| Bass trombone | 9 | 9 |
| Bass clarinet | 6 | 6 |
| Tuba | 4 | 4 |

- The gap in parts.json is 0.03 qn on almost all of them (14 ms at 126 bpm). That comes from `score_to_parts.py` note lengths: `same_pitch` -> `min(0.03, 0.1*dur)` for a Sus note. The release tail and the hall fill it.
- Examples:
  - Horns 3/4, bars 19-22 (p, qn 76-88): Horn 4 at 80/84/86 reads +0.5 / -0.8 / -0.8 dB, so four half notes sound as one.
  - Contrabassoon quarters in bars 27-30 (ff, doubling the basses' repeated eighths, which REP_SPLIT now separates by 4-6 dB): -0.3..-2.9 dB.
  - Trombone 1 at 492 (fff): 0.0 dB.
- Kit section 7: 0.06 qn gave 2-6 dB on bassoon and bass clarinet and only 1-2 dB on horns. A loud breath needed a longer gap and a fall into it (0.5 qn plus 10 CC gave 7.2 dB).

Inferred: in a real orchestra each of these is a new tongue stroke, heard as a light pulse. Here the brass harmony and the contrabassoon pedal lose their rhythm.

**Fix** (generic, `tools/score_to_parts.py` note-length pass, the `elif same_pitch:` branch; `--midi-only`). New `WIND_REP_RETONGUE = {"gap_s": 0.06, "frac": 0.25, "fall_cc": 6, "fall_s": 0.12}`:
- An untied, unslurred, same-pitch wind or brass repeat (not `sost_rep`, not a breath) ends `min(qn(gap_s), frac * dur)` before the next onset, converted with `qn_to_sec` going back from the onset.
- Its CC11 falls by `fall_cc` over its last `fall_s` (`cc_falls` already carries this shape) and returns at the next onset.
- At 126 bpm this is a 0.13 qn gap on a quarter note; in the Lento it stays 0.06 s.
- Keep `REP_RETONGUE_AT` for any per-onset exceptions.
- If the horns still read under 3 dB, raise their `fall_cc` to 10 before lengthening the gap.

The `LegRep RRx4` row in the 1FH/1TB/1TU KS Masters is a short articulation (manual p. 46: listed under SHORT). It is not a substitute for held repeated notes; do not use it here.

**Pass criteria.**
- Median repeat dip 4-7 dB on every listed track, and no repeat deeper than 10 dB.
- Horn 4 at 80-86: at least 3 dB.
- Accent and probe checks unchanged.

## 3. Slurred tenutos (portato) in the winds at f/ff open holes and arrive weaker than the eighth before them, the reverse of a tenuto (bars 69-70 and 98-102)

**Score.** The development theme in bars 98-102 (B minor, ff): `g''2--` tenuto half notes inside long slurs. They are in Oboe 1, Cor anglais and Flute 1 at qn 393/400/405, doubled by Violins I/II. At qn 277 (bar 70) the tenuto is in Flute 1/2, Oboe 1 and Trumpet 1. There is also Bassoon 1 at 413.

**Measured** (`ten2.py`; dip = lowest 40 ms level around the onset against the louder neighbour; body = +0.1..+0.5 s minus the 0.3 s before).

Each wind tenuto is re-tongued on Sus MAX at v83-91 with a 0.07 qn gap (`score_to_parts.py` about line 1367: "a tenuto inside a slur is tongued").

| Note | Dip | Body - before |
|---|---|---|
| **Oboe 1 400** | -10.2 dB | **-6.8 dB** (stem -31 -> -38..-42 dB for 0.3 s after the onset) |
| Flute 2 277 | **-11.6 dB** | |
| Flute 1 393 / 405 | -6.1 / -6.2 dB | |
| Cor anglais 393 / 400 / 405 | -4.8 / -5.0 / -5.3 dB | |
| Oboe 1 277 | -5.1 dB | |
| Trumpet 1 277 | -5.1 dB | |
| Bassoon 1 413 | -5.0 dB | -4.5 dB |

- The string tenutos in the same bars are legato joins. Their bodies sit under the note before: Violins I 393/400 -3.4 dB, Violins II 393 -2.9 dB, Violas 429 -7.2 dB.
- Kit section 6 (c07): a wind tenuto to a new pitch played best as a Leg Slur target (v100, 10 CC notch), with join dips of 4.1-5.2 dB. Horn 1's c04 `PORTATO_JOIN_AT` joins here measure -2.2..-8.1 dB. The worst (189, -8.1) is a 9-semitone leap, as c04 recorded.

Inferred: the stressed half note of the theme falls back each time instead of leaning in.

**Fix** (`build/score_config.py`, `--midi-only`).
1. **Wind tenutos.** `PORTATO_JOIN_AT` += Oboe 1 [277, 393, 400, 405], Cor anglais [393, 400, 405], Flute 1 [277, 393, 400, 405, 436], Flute 2 [277], Bassoon 1 [413], Trumpet 1 [277].
   - All are new pitches within 9 semitones. Most are 8-9-semitone leaps, so check each join.
   - Fallback, for any join that dips 6 dB or more on the render: keep that note on Sus MAX with a 0.05 s lead (`entry_leads.json`) and velocity 105 instead of v91.
2. **String tenutos.** New generic `TENUTO_SWELL_DB = 1.5`: a slurred string tenuto at f or louder gets a volume step of +1.5 dB from its onset to 0.1 qn before its end (the `GENTLE_ACCENT` envelope shape, held for the note), so the note keeps its weight. Do not add a CC11 bump: kit section 6 says level shaping into a legato sag deepens it. Apply it after the join, starting at +0.05 s.

**Pass criteria.**
- Every listed wind tenuto: dip no deeper than 6 dB, and body at least -1 dB against the note before (Oboe 1 400 now -6.8).
- String tenutos in bars 98-102: body - before at least 0 dB.
- No new 2-5 kHz bump.

## 4. a2 horns play one solo-horn sample plus 3 dB in six passages, including both horn pairs at the climax: a better patch exists (2FH KS Master)

**Measured (parts.json `unison_dropped`).**
- Horn 2 has 84 notes dropped into Horn 1, so one Solo French Horn sample plays both players, with +3 dB. The spans (qn):

  | Span | Bars | Notes |
  |---|---|---|
  | 272.5-286 | 69-72 | 19 |
  | 310.5-314 | 78-79 | 7 ("a2" printed at 310.5) |
  | 381.5-404 | 96-102 | 20 |
  | 464-480 | 117-121 | 7 |
  | 628-643.5 | 158-161 (climax, "a2" printed) | 13 |
  | 662-676 | 166-170 | 16 |

- Horn 4 into Horn 3: 628-640 (the second climax a2 pair), 292-300 and 316.5-324.
- Also on single samples: Trumpet 2 into Trumpet 1 at 664.5-676 (16 notes), Trombone 2 into Trombone 1 at 520.5-534 (19), Clarinet 2 at 272.5-286 and 408.5-423.5, Bassoon 2 at 520.5-544.
- At the climax Horn 1 is the loudest brass stem: -9.7 dB re master at qn 636.

Inferred: a solo-horn sample raised 3 dB keeps a solo's narrow tone. Two horns in unison give a broader sound with slight beating, which is how a2 horns sound in a tutti. HO has it recorded: `2 French Horns/06 Keyswitch/2FH KS Master.oib`. Its rows are already in `ks_maps.json`: Sus MAX, Leg Slur MAX, Portato, Marc rows.

**Fix.**
- Add one track "Horns 1-2 a2" on the 2FH KS Master.
- Route Horn 1's notes in the Horn 1/2 unison spans above to it, by score-onset window and only where Horn 2 doubles: the `TRACK_WINDOWS` mechanism of mvt II c18/c19 (kit sections 8 and 17).
- Remove the +3 dB unison boost for those notes.
- Gain: kit c18 measured +4.6 dB over the solo-horn track that it replaced, which had the +3 dB boost. Set it from one render with a role.
- Load only the rows used (Sus MAX, Leg Slur MAX) and its Close + Main mics.
- Memory: c05 settled at 43 GB after the render, against the limit of about 45 GB. Record the post-render figure. If it goes over, keep this track and unload unused mics on the four solo horn tracks.
- If memory allows, a second 2FH track for Horns 3-4 at 628-640 is the next step. Trumpets 1-2 at 664.5-676 could use `2 Trumpets/06 Keyswitch`.

**Pass criteria.**
- The a2 stem within ±1 dB of the c05 Horn 1 level over qn 628-643.5 and 272.5-286.
- Legato join dips of the routed slurs at or under the c05 Horn 1 values (median 1.1 dB).
- REAPER at or under 45 GB after the render.

## 5. Slurred string eighths at 112-126 bpm on Sus MAX change pitch late and dip: Violins I median +0.10 s, 21 of 75 dips of 6 dB or more (test a capped legato lead)

**Measured (`xall.py`, slurred pitch steps).**

| Track | Notes | Sus MAX crossover (p90) | Leg-row crossover | Sus dips of 6 dB or more |
|---|---|---|---|---|
| Violins I | 75 | +0.10 s (+0.148) | +0.065 s | 21 |
| Violins II | 36 | +0.10 s | +0.06 s | |
| Violoncellos | 20 | +0.138 s (+0.22) | +0.06 s | |

- Examples on Violins I: qn 283.5 +0.205 s, 271.0 +0.20, 151.5 +0.185, 67.0 +0.17.
- Bar 16 (qn 61.0, the theme's b'8, exposed): +0.24 s with an 11.8 dB dip.
- The c05 test (0.05 s lead on Sus eighths) moved the crossover only 0.015-0.02 s, because the crossover of two overlapping Sus notes is set by the old note's decay (mvt I LEARNINGS c05).
- Kit section 5 (c19): with `LEG_CAP_FRAC` 0.75 and the normal legato lead, slurred viola triplets on Leg Slur MAX moved from +0.053 to -0.017 s median.

Inferred: the strings blur the chromatic eighths of the main theme and trail the winds that double them.

**Fix (test, Violins I only; Violins II is the control).**
- New `SHORT_SUS_LEG_TRACKS = ("Violins I",)` in the short_sus branch (`score_to_parts.py` about line 1320). A slurred, monophonic, non-first note of 0.20-0.25 s (eighths at 112-126) stays on Leg Slur MAX as an ordinary legato target, with the string lead and v124.
- Set `LEG_CAP_FRAC = {"Violins I": [(56.0, 728.0, 0.75)]}`.
- Notes under 0.20 s (sextuplets, triplets) stay Sus MAX, as the kit requires.
- Keep `short_sus` on any eighth that is followed by its own pitch in the slur, so that `SLUR_REP_MERGE_SUS` still merges it (Violins I 60/108/140/572).
- Revert the c05 `SHORT_SUS_LEAD_TRACKS` in the same pass.

**Pass criteria.**
- Violins I slurred-eighth crossover median at or under +0.06 s.
- Dips of 6 dB or more: 10 or fewer.
- No join spike over +5 dB (kit: one join in ten spikes).
- Bar 16 (qn 61.0) dip under 6 dB.
- If it fails, revert and close this item.

## 6. Smaller items (ranked)

- **Celli whole-note tremolos, bars 117-121 (qn 464-480, f under the fff texture), measured.**
  - Five untied tremolo whole notes are re-attacked each bar. Each one jumps and then decays 5-7 dB within its 1.9 s: stem -26.3 dB at the bar start, -33..-36 dB at the end, in every bar.
  - The stem is 14 dB under the master, so this is a minor issue.
  - Fix: listed tremolo repeats keep one note with a 4 CC notch at each bar line (the slurred-repeat merge path), `TREM_MERGE_AT = {"Violoncellos": [(464, 484)]}`.
- **Horn 3/4 breath-split dips at qn 720 (open from c05).** On the stems the dips are -3.6..-8.9 dB within 0.4 s. Halve the `BREATH_SPLIT` dip (-3 -> -1.5 dB) before moving the split times.
- **Violins I final-chord re-bows, measured.** Stem dips at 711.855 / 722.781 / 724.465 are -5.7 / -4.3 / -3.9 dB, and at 722.781 the master dips -4.0 dB, against a control p10 of -3.8. Refit those three with `fit_rebows.py` on c05; the other sections' re-bows are within -3.8 dB.
- **Harp étouffez (qn 244, 650, 654), measured.** The harp chord at 648 is already 15 dB down by 650, so 650 and 654 need nothing. 244 remains as in c05-A, a low priority.

## Do not touch

- `GENTLE_ACCENT` for brass, winds and strings, `STR_ACC_AFTER_SUS` and `DETACH_ACCENTS`.
- `AUTO_REBOW` with `space_rebows.py` and the fitted shapes: master loop autocorrelations are all at or under 0.14.
- The slurred-repeat merges (`SLUR_REP_MERGE_SUS`, `WIND_SLUR_REP_MERGE`), `STR_SHORT_AFTER_SUS`, `REP_SPLIT`, and the strokes' velocity rule.
- `PORT_TARGETS`, `PORTATO_JOIN_AT` Horn 1, and `META_DB`.
- The timpani re-strike plans (0/48/464/484/720) and `TIMP_DELAY_S`.
- The pizzicato rows, staccato at half the written length, and the Tremolo rows.
- The crash patch and timing, the sus. cymbal lead, and the pre-roll meter fix.
