# Cycle 19, critic C: tempo, timing and transitions (render c18)

## Method

I measured the stem-fixed c18 render (`cycles/c18/render/`) against `build/parts.json`. Its notes, keyswitches and tempo map are identical to `cycles/c18/rendered_build/parts.json`; only the Bassoon 1 volume envelope differs (the stem fix). Score qn was converted to file time on that tempo map. Levels are stereo power in 20 ms windows at a 5 ms hop. Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c19-C/` (the c15 critic C set, pointed at c18, plus new ones):

- `shortn.py`: re-attack arrival for every note at 100 bpm or faster, from the local minimum before the onset to the 0.25 s peak - 3 dB.
- `shortn2.py`: the same with the track's `vol_db` envelope subtracted, so it measures the sample alone. This takes the GENTLE_ACCENT swell out of the accent measurements.
- `shsum*.py`, `shlist.py`: summaries split into led and unled notes, and lists of single notes.
- `accl.py`, `accl2.py`: accented notes (from `mockup-events.tsv`) split into led and unled notes, with a table per onset.
- `tutti.py`, `timp.py`, `xover2.py` + `xsum3.py`, `entries.py`, `front.py`, `slowent.py`, `ks.py`, `loopacc.py`, `acc_one.py`, `tempo.py`.

## Checks that pass (measured)

- **Printed tempos.**
  - Lento 50, Allegro 126, Poco meno mosso 112, sostenuto 100 (bars 123-126), largamente 100 (bars 160-164), Più lento 72, Tempo I 50 and the final bar at 30 all play as printed.
  - The rit., allargando and animando ramps end on their printed steps: bar 46 at 113, bar 68 at 86.5, bar 122 at 102, bar 166 at 79.5, bar 178 at 51.5. The animandos reach 120.1 (bar 65) and 120.9 (bar 159).
  - The total length is 433.44 s, the same as c15.
- **Bar-170 fermata.** qn 679 is at 380.31 s. The master falls from -13.1 to -63.6 dB by +2.0 s, and the cello's sound starts 0.1 s before qn 680 (382.81 s).
- **Attacca ending.** The master is at -49.6 dB at 432.5 s and -61 dB at qn 728 + 0.06 s. The mp3 is 434.95 s long, so the tail is 1.5 s.
- **Keyswitches.** All 1025 used keyswitches come at least 9.5 ms before their note.
- **String entries after rests** (c15 finding 1, fixed in c15). t-6 is now -0.07..+0.12 s for the 19 listed entries (c14: +0.16..+0.48). The worst is Cb 696 at +0.20 (`slowent.py`).
- **Legato crossovers in the Allegro.** Medians, in seconds:

  | Track | Leg Slur | Leg BC |
  |---|---|---|
  | Violins I | +0.025 | +0.065 |
  | Violins II | +0.015 | +0.045 |
  | Violas | +0.040 | +0.035 |
  | Celli | +0.040 | +0.060 |

  Horn 1 Leg Slur +0.033, Flute 1 +0.020, Oboe 1 +0.030, Horns a2 0.000. Flute 2 at +0.080 is the only one over +0.07.
- **Led re-attacks.** The c15 RETONGUE_LEAD_S and loud entry leads hold:
  - led brass +0.040 s (n 534) and led winds +0.046 (n 649), against strings +0.000 (n 807);
  - timpani strokes are at +0.042, the brass at the same strokes +0.020 by `timp.py`'s -6 dB measure. TIMP_DELAY_S 0.045 is right.
- **Brief item 7.** Master autocorrelation at 3.95 s, 100-300 Hz band / centroid (`loopacc.py`):

  | Passage | Band | Centroid |
  |---|---|---|
  | Lento 5-12 | -0.07 | -0.03 |
  | sostenuto 123-126 | -0.17 | -0.02 |
  | coda 175-178 | -0.09 | +0.08 |
  | Tempo I 179-182 | -0.27 | -0.20 |

  No loop pulse.
- **Brief item 8.** 2-5 kHz in the first 80 ms minus the body: brass median -14.2 dB (max +2.0), winds -13.6 (max +1.5), strings -9.4. The one string value over +3 is Violas 536 (+10.5), the ringing f double stop already explained in c15.

## 1. Every loud wind and brass accent plays from the score onset with no lead and lands a sixteenth behind the orchestra, on the movement's main hammer chords (measured)

**Where.** Wind and brass accents at f or louder that take the GENTLE_ACCENT branch (`n["acc_art"] = True`, plain Sus rows). The tutti chords where they cluster:
- bar 26 (qn 100);
- bars 32-33 (124, 125, 128);
- bar 41 (160);
- bar 72 (284, 285, 286, the three hammer strokes);
- bar 83 (328, 330);
- bar 138 (548);
- bar 143 (568);
- bar 170 (676, the ff chord before the fermata).

There are also the recapitulation wind accents at 521-566.

**What is wrong.** `tools/score_to_parts.py` line 2499 (`elif n.get("acc_art"): pass`, comment "c26: listed accent articulations keep the score onset (no lead, as Sus Accent had)") skips every lead rule for these notes. The rule was written for the Sus Accent samples, which attack fast. GENTLE_ACCENT replaced those samples with plain Sus rows, which have the same attack latency as any other Sus note, and those notes now get no lead.

Sample-only arrival (`shortn2.py`, envelope removed; s after the score onset):

| Notes | Unled accents | Led notes of the same family |
|---|---|---|
| brass | +0.107 (n 102, p75 +0.133) | +0.045 (n 531) |
| winds | +0.095 (n 128, p75 +0.131) | +0.046 (n 632) |

Per onset (`accl.py`, envelope included):

| Onset | Unled wind and brass arrivals |
|---|---|
| bar 26 (100) | Oboe 2 +0.19, Trumpet 1/2 +0.17/+0.15, Horn 2 +0.14, Tuba +0.11; strings median -0.03 |
| bar 83 (330) | Horn 1/2 +0.16/+0.15, Oboe 2 +0.17, Contrabassoon +0.14, Trumpet 2 +0.13; timpani and the trombones +0.06 |
| bar 138 (548) | Oboe 2 and Flute 1 +0.20, Tuba +0.13, trumpets +0.10..+0.12; timpani +0.06 |
| bar 170 (676) | Oboes +0.21/+0.20, Flute 2 +0.19, Trombone 1 +0.19, Trumpet 3 +0.16, Bassoon +0.15 |

At 126 bpm a sixteenth note lasts 0.119 s. Inferred effect: on the accented tutti chords the timpani and the led parts strike first and the upper winds and brass arrive a sixteenth later, so the chords that should hit hardest are spread out.

**Fix.**
- **Code.** In `tools/score_to_parts.py`, line 2499, skip only real accent samples, so GENTLE_ACCENT notes fall through to RETONGUE_LEAD_S (gap under 0.5 qn) or the entry branch:

  ```
  elif n.get("acc_art") and ("Accent" in (n.get("art") or "") or not ACC_ART_LEAD):
  ```

  with a new generic `ACC_ART_LEAD = True` in `score_to_parts.py`.
- **Values.** No new numbers are needed. These notes then take the existing RETONGUE_LEAD_S values and the c15 loud ENTRY_LEAD_S tuples.
- **Controllers.** The volume-envelope swell (`swell_s`) and CC11 stay on score time; the lead adds the span to `pulls`, as for any led note.
- **After the render.**
  - Refit the accents: `fit_accents.py --family brass` and `--family wind`, with `--keep-long-qn 1.4` and the existing `--skip` hand values.
  - Re-check item 8 (2-5 kHz front minus body under +3 dB).
- **Checks.**
  - Unled-accent sample-only medians within 0.02 s of the led medians (brass ≤ +0.065, winds ≤ +0.065).
  - At 100, 284-286, 330, 548 and 676 no wind or brass track over +0.10.
  - No new repeat hole of 6 dB or more (same-pitch accents such as Oboe 2 285, Tuba 330 and Oboe 1 672/676 follow short gaps).

## 2. Unled string strokes, the bar-72 hammer strokes above all, land 0.12-0.23 s late (measured)

**Where.**
- **Bar 72, beats 2-3 (285, 286).** Down-bow accented quarters (score p. 7, "change bow at will" in the low strings).
- **Other Sus MAX notes with no lead.** They follow a slur or a short gap under 0.5 qn, at 100 bpm or faster:
  - Violins I: 59.5, 77.5, 127.25, 127.75, 159.5, 571.5;
  - Violins II: 128, 554.5;
  - Violas: 100 (f accent), 115.5, 279.5, 675.5.

**What is wrong.**
- Sample-only arrival of unled Sus MAX notes: Violins I +0.120 (n 27, p75 +0.166), Violins II +0.094 (n 18). Led string notes: +0.004 (n 772).
- **Bar 72.** The rendered arrivals are:

  | Onset | Strings | Timpani | Brass |
  |---|---|---|---|
  | 285 | Violins I +0.228, Violins II +0.173, Violas +0.143 | +0.05 | Tuba +0.12, Trombones +0.09..+0.11 |
  | 286 | Violins II +0.192, Violas +0.202 | +0.06 | |

  The strokes are 0.476 s apart (c11 BEAT_STRETCH), so the strings lose about 40% of each stroke's beat.
- **Violas 100** (f accent with the brass): +0.189.
- None of these notes is reached by ABUT_LEAD (not listed), STR_SHORT_AFTER_SUS (no lead) or the entry branch (gap under 0.5 qn).

**Fix.**
- **Rule.** Extend RETONGUE_LEAD_S to strings: a `"string": 0.10` entry in `build/score_config.py`, and allow `family == "string"` in `retongue_ok()` for Sus MAX notes only.
  - The previous note's end moves with the lead, as for winds.
  - Exclude notes listed in `_REBOW_FROZEN`/REBOW_AT, REP_SPLIT/MEAS_TREM strokes and Stac rows (their medians are +0.055..+0.085).
- **If a generic rule is too wide this cycle,** list the onsets instead: `ABUT_LEAD["Violins I"]`, `["Violins II"]` and `["Violas"]` with `"lead_s": 0.10, "at": [...]`, the onsets above plus 284-286 for all upper strings.
- **Checks.**
  - Bar 72 strings within 0.04 s of the timpani on each stroke.
  - Unled Violins I/II Sus medians ≤ +0.05.
  - Re-measure the violas' bar-72 roles and the c06 DOWNBOW_STROKE_AT level shapes, which are keyed to these onsets.

## 3. The first-theme Violins I slur heads play as a 0.07 s flick, not an eighth (measured from the data; heard effect inferred)

**Where.** Violins I, 23 notes, all the first eighth of a slur followed by a led legato target:
- bars 15-21: 58.5, 61.0, 66.5, 69.0, 74.5, 80.5, 84.0;
- bars 27-29: 106.5, 109.0, 114.5;
- bars 35-39: 138.5, 141, 146.5, 150.5, 152, 156;
- 259.5, 314.5, 377, 455.5, 554.5;
- bar 143: 570.5, 573.

These are the theme's "D-D♭-C" figures (score p. 2, bar 15: dotted quarter E♭, then a slurred D-D♭-C).

**What is wrong.**
- In parts.json each head starts at its score onset on Sus MAX. The next note, a Leg Slur target, starts 0.17 s early.
- So the written eighth (0.238 s) sounds 0.065-0.080 s before the next pitch takes over.
- With string attack latency, the head reaches -3 dB of its peak only at +0.12..+0.18 s: 66.5 +0.165, 84 +0.167, 138.5 +0.177, 146.5 +0.166, 152 +0.167. By then the next pitch has already started.
- Inferred effect: the first note of each slur in the main theme is reduced to a grace-note smear, and the figure's rhythm is uneven.

**Fix.** In `tools/score_to_parts.py`, a string Sus MAX slur head shorter than 0.5 qn whose next note is a led legato target gets the same lead as that target:
- new generic `SLUR_HEAD_LEAD = {"string": True}`;
- the shift is `lead_qn(q, leg_s)`, capped so the head keeps at least 0.8 of its written length before the target's moved onset;
- add the span to `pulls`.

Check: each listed head sounds at least 0.19 s before the next moved onset and reaches -3 dB by +0.06 s. Re-check `PICKUP_LIFT` and `SYNCO_SHAPE` only where they touch these onsets (bars 15-22).

## 4. Oboe 2 is the latest wind on every loud entry, even with its leads (measured)

**Where.** Oboe 2 at 100 bpm or faster.

**What is wrong.**
- Led Oboe 2 notes arrive at +0.104 s (n 26, p75 +0.128), against +0.046 for the other led winds. Unled ones arrive at +0.130.
- Examples, all with the c15 loud lead (0.08-0.12 s):
  - 116 +0.166;
  - 160 +0.113;
  - 409 +0.171;
  - 413.5 +0.164;
  - 488 +0.129;
  - 664 +0.138;
  - 668 +0.168.
- Oboe 1's unled Leg Slur re-attacks also run late: 92 +0.233, 105 +0.208, 540 +0.233, 579 +0.212 (Leg Slur leads of only 0.03-0.08 s).

**Fix.** In `build/score_config.py`:
- `ENTRY_LEAD_S["Oboe 2"] = (0.0, 0.14, 0.0)`;
- `RETONGUE_LEAD_S["Oboe 2"] = 0.12`;
- `ENTRY_LEAD_ART_S["Oboe 2"]["Leg Slur MAX"] = 0.16`;
- for Oboe 1's Leg Slur re-attacks after a slur break, `ENTRY_LEAD_ART_S["Oboe 1"] = dict(ENTRY_LEAD_ART_S["wind"], **{"Leg Slur MAX": 0.16})`.

Put the track keys before "Oboe" and "wind" (`by_name` takes the first match). Keep ENTRY_CAP_S at 0.30.

Check: Oboe 2 led median ≤ +0.06, first sound (peak - 20 dB) no earlier than -0.15 s.

## 5. The recapitulation's poco rit. (bars 145-146) starts a bar early and stalls (measured; small)

**What is wrong.** Printed: bars 145-146 at 124, 121, 118, 114 (half bars), the same as bars 45-46. Beat tempos (`tempo.py`):

| Bar | Beat tempos |
|---|---|
| 45 | 125.0, 123.2, 121.7, 120.2 |
| 46 | 118.7, 117.0, 115.0, 113.0 |
| 144 | 126, 126, 123.5, 119.7 |
| 145 | 120, 120, 120, 119.5 |
| 146 | 118.5, 117.0, 115.0, 113.0 |

The "sub" arc (568, 576) slows bar 144, and the ramp then holds 120 through bar 145. The result slows, stops slowing, then slows again, where the exposition makes one gradual rit.

**Fix.** In `build/score_config.py`:
- set `(568, 576, "open")` in PHRASE_ARCS (push only, as c11 did for 272, 232 and 600);
- set the RAMP_SPANS entry `(576, 584, 126)`, as bar 45 has (176, 184, 126).

Re-bows are frozen in qn, so they do not move.

Check: bar 145 beats 125 → 120 falling and bar 146 equal to bar 46 within 1 bpm, with no speed-up inside 572-584.

## Do not touch

- The RAMP_SPANS realisation of the other printed steps, the rit. clamp in `smooth_tempo` and the arcs with their "open"/"sub" depths (apart from 568-576).
- BEAT_STRETCH 284/285/679, CAESURA {636: 0.15} with the suspended-cymbal key 64 / lead 0.25, and the 30 bpm final bar with the 1.0 s mp3 tail.
- TIMP_DELAY_S 0.045 (it matches the led brass).
- Keyswitch placement.
- The string Leg Slur/Leg BC leads and the c15 string entry leads and fills.
- RETONGUE_LEAD_S and the c15 loud ENTRY_LEAD_S values for the other tracks.
- The Horn 1 leg leads, ABUT_LEAD lists and UNI_DELAY overlap with its fade.
- `_REBOW_FROZEN` and the fitted re-bow shapes.
- GENTLE_ACCENT's swell and CC11 on score time (only the note-on moves in finding 1).
