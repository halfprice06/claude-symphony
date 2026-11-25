# c51 critic C: holistic comparison (render under review: c50)

Lens: I listened through the data the way a conductor would. I compared c50 with c49 (the same notes on the old mix, so the pair isolates the template mix), with c45 (five cycles back), with cycle 0 (c00, series 1, delivered mp3 only; c31, the v621 port, for master figures) and with the Dvořák 9/i recording (decoded mp3), plus the stored metrics of Brahms 1/i, 4/i, 1/ii and 4/ii. I also measured the finale's c07 render, the first render with PHRASE_SHAPE and HP_CURVE, before its stems were deleted during this cycle. Every number is measured unless it is marked inferred.

Method, all scripts mine unless named:
- Tone, width and envelope modulation: 0.1 s frames (8192-point FFT) of the master and mp3; band shares and centroid over the loudest 10 % of frames (whole file) or the loudest 25 % (per section); side/mid over 200 Hz-5 kHz; L/R correlation by band; envelope modulation is the 2-16 Hz depth of the 10 ms RMS envelope, the median over 2.56 s windows in the louder half.
- Per-stem band energy as a share of the master's energy in the same frames.
- EQ simulation in the power-spectrum domain on the c50 dry stems and returns, with each changed stem re-levelled to its own K-weighted energy. The incoherent stem sum matches the master within 0.2 dB per band and 12 Hz of centroid.
- Phrase statistics on dry stems: a phrase is notes with played gaps under 0.25 s, at least 2 s long, typed build / drive / lyric with the finale's rule and C c50's lyric spans. "rise08" is the 50 ms RMS level at +0.8 s minus the level at +0.15 s. "taper" is the level 1 s before the last note-off minus the level 0.2 s before it.
- `cycles/c48/actor_scripts/scan48.py` on c50 for perceived attacks (pcX).
- Per-beat K-weighted master levels and a stem-sum simulation for bar 121.

Scratch: `/private/tmp/claude-501/mockup-loop/mvt1-c51-C/` (deleted at the end).

## Manual notes (second round, c48-51 rule: pages behind this lens's top problem, phrase shaping and controller use, plus the tone change)

| Page | What it says | Where it applies | Does c50 follow it? |
|---|---|---|---|
| p.53 (2.5.7) | Shape lines the way a player does, with CCs changing mid-note and over a phrase; velocity for shorts | Every sustained line | **No.** Lanes follow only the printed marks: lyric phrases have 0 units of rise by 0.8 s and 0-1 units of taper (finding 1) |
| p.64, p.151 | In the MAX string and woodwind patches, CC11 sets loudness and dynamics and CC1 sets vibrato. In the LITE string patches, CC1 sets dynamics and vibrato together. CC7 or the fader sets each track's ceiling | The plan's "Mod + Expression Combo" CC1-only test (section 5) | Yes. The string lanes already ride together (r(CC1, CC11) 0.73-0.99 per section; CC1 tops out at 98-99) and keep a deliberate +30 CC1 offset in the espr. windows. The macro would make our MAX patches behave like LITE ones and remove that offset (see "Plan items") |
| p.45 | CC1 and CC11 can be connected to any parameter (this is what the template's macro does) | Same | Information only |
| p.91 | String sustains have three vibrato levels (non vib, vib, molto) and a bow-direction round robin | The espr. CC1 offsets; the basses' strong off-beat stroke | Followed |
| p.101 | Brass sustains play all 4 dynamic layers at once and the Mod Wheel (CC1) crossfades them | Brass phrase shapes | Followed for printed dynamics. On these tracks the printed curve drives CC1 and CC11 together, and the realised change is 0.28 dB per CC1 unit on c50 brass decrescendos. Phrase offsets should drive both lanes the same way (finding 1) |
| p.138-139 | Close mics give presence, Mid gives definition, Main gives the room and a "big, unified sound" | Tone of the tutti after the template | The template EQ and make-up, not the mics, moved the brass to 4 dB more presence and 4 dB less middle (finding 2) |
| p.222 | The recorded room is heard as long as samples sound, release trails included | The returns add to the room the Main mics already carry | Decays still pass (drop at +0.3 s 15.7-20.3 dB on the master) |

MANUAL-GAPS items in this lens: #5 (Sus Exp / Leg Slur Exp rows for the espr. wind solos) is an untested alternative to phrase shapes on the solos. #12 (Felt Cresc) is an alternative for the bar-121 timpani roll. #4 (Mid instead of Close on the winds) bears on wind brightness. None of them is needed in c51.

## EW-TEMPLATE-PLAN: what c50 still does not apply

- Section 5, legato overlap: medians are winds 19 ms, brass 21 ms, strings 20 ms against the plan's 33-58 / 45-80 ms. Not applied (critic A's lens).
- Section 5, legato velocity: strings and brass 124, winds 100. Applied, but not by dynamic.
- Section 5, lane density: 3.1-4.9 points per sounding second against the plan's 7-13. Not applied; PHRASE_SHAPE `step_s` 0.1 would meet it inside shaped phrases.
- Section 5 / 6, CC1-only test: not applied (see "Plan items").
- Sections 6-8, phrase shape per phrase: not applied (finding 1).
- Section 8, repeat gaps: winds 60 ms and brass 100 ms medians, so applied there. Strings are not: the median is 14 ms on 417 same-pitch repeats, and separation comes from volume dips instead (finding 5).
- Section 8, tutti spread, room-noise bed and tempo breaths: not applied (see "Plan items").
- Section 9, hairpin curves: not applied (finding 4).
- Section 10, shape by character: not applied (finding 1). Doublings already share one printed curve.
- Sections 1-4 were applied in c50. Section 3's brass and woodwind bands overshoot the references (finding 2).

## Answers to the coordinator

### c49 against c50: what the template mix gained and lost (same notes)

Whole movement, master, loudest 10 % of frames (band shares in dB re total):

| | 30-125 | 125-250 | 250-500 | 500-1k | 1-2k | 2-4k | 4-8k | 8-16k | centroid Hz | side/mid dB | corr 250-5k | env. mod dB |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| c31 (v621 port) | -13.6 | -10.7 | -7.0 | -5.1 | -5.5 | -11.3 | -22.3 | -35.7 | 947 | -5.6 | 0.57 | -17.5 |
| c45 | -15.2 | -10.4 | -6.4 | -5.5 | -5.5 | -11.2 | -21.9 | -36.8 | 943 | -6.7 | 0.65 | -17.4 |
| c49 | -15.3 | -10.4 | -6.5 | -5.5 | -5.3 | -11.3 | -22.0 | -36.8 | 952 | -6.7 | 0.65 | -17.5 |
| **c50** | -12.7 | -9.0 | -6.5 | **-7.6** | -5.2 | **-9.5** | **-19.3** | -33.6 | **1035** | -4.6 | 0.48 | -17.8 |
| Dvořák 9/i | -14.3 | -6.9 | -6.5 | -5.9 | -7.1 | -11.2 | -21.9 | -33.4 | 824 | -5.7 | 0.58 | -15.9 |

The Brahms references (rtk) have a loudest-10 % centroid of 818-870 Hz and side/mid of -4.7 / -5.4 dB.

**Gained (measured):**
- Width is now inside the references. Side/mid in loud frames went from -6.7 to -4.6 dB, and every section moved +1.2 to +2.8 dB. c49 was narrower than every reference.
- Across the whole file, the 500 Hz-2 kHz share is now at the reference level: -3.5 dB, against -3.5 to -4.4 dB for the references and -2.6 for c49 (`metrics.md`).
- The 24-bit master no longer clips (sample peak 0.957, was 1.469), and the delivery limiter went from 1.3 to 0.2 dB.
- Decays held. On the delivered mp3, the drop 0.3 s after the stops at qn 103 / 125.9 / 288 / 551 / 679 is 18.5 / 21.9 / 18.5 / 21.6 / 19.7 dB (c49 18.9 / 22.7 / 16.9 / 22.8 / 20.8; c00 17.4 / 12.6 / 12.9 / 14.2 / 15.3).
- The climax order and the loudness range held (actor's figures).

**Lost, by passage (measured, loudest 25 % of frames per section, c49 to c50):**
- The tutti lost middle and gained presence in every section: 500 Hz-1 kHz fell 1.2-3.5 dB, 2-4 kHz rose 1.1-2.2 dB and 4-8 kHz rose 1.0-3.4 dB. The worst passages:

  | Passage | Centroid (Hz) | 500 Hz-1 kHz | 4-8 kHz |
  |---|---|---|---|
  | Climax, bars 121-126 | 1071 -> 1192 | -1.8 dB | +2.6 dB |
  | Climax, bars 160-166 | 1071 -> 1206 | -2.4 dB | +2.2 dB |
  | Coda tutti, bars 167-170 | 891 -> 1012 | -3.5 dB | +3.4 dB |
  | Recapitulation second theme, bars 147-159 | 1027 -> 1105 | | |
- Which family causes it (loud frames, energy re the master total):
  - brass: 500 Hz-1 kHz -4.0 dB, 2-4 kHz +3.8, 4-8 kHz +4.8, 30-125 Hz +4.9;
  - winds: 4-8 kHz +4.5 and 8-16 kHz +8.2 (the +5.1 dB shelf at 7.6 kHz);
  - strings: 500 Hz-1 kHz -1.7, 2-4 kHz +1.2.
- Envelope modulation, a proxy for articulation clarity, fell 0.3 dB on the master and 0.5 dB on the mp3. By section it fell in the second theme (-1.0 dB), at the climax of bars 160-166 (-0.7), in the coda tutti (-0.5) and in bars 107-120, the transition and the closing (-0.4 each). It rose in bars 127-130 (+1.3), 147-159 (+0.7) and 131-146 (+0.4). The returns sit 11.9-15.5 dB under the dry stems by section; the second theme is the wettest at -11.9.
- The delivered mp3 changed the same way (loud frames): 500 Hz-1 kHz -2.1 dB, 2-4 kHz +2.4, 4-8 kHz +3.6, centroid 898 -> 982 Hz.

**Against c45 and c00 (measured).** c45 and c49 agree within 0.2 dB in every band, within 9 Hz of centroid and within 0.1 dB of modulation. The per-note work of c45-c49 does not show at the whole-movement level; the template is the only large change in five cycles. Against c00 (delivered):
- the tails are 1-9 dB drier;
- the delivery now fits one headphone level (LRA 17.3 -> 14.7 LU, span 21.7 -> 19.1 dB);
- width is back where c00 had it (side/mid -4.95 -> -4.82 dB);
- the loud tutti is brighter than any earlier render (centroid 894 -> 982 Hz);
- modulation is 0.6 dB better than c00 (-18.6 -> -18.0) but 0.5 dB worse than c49.

**Weakest passages now:**
1. The climaxes (bars 121-126, 160-166) and the coda tutti (167-170). They are the brightest and thinnest, and bar 121 hardly grows into the fff (findings 2, 3).
2. The espr. solos and the lyrical second-theme lines. Their phrases start at the top, do not taper, and sometimes get louder into their last second (finding 1). Examples:
   - Flute 1 bars 11-13 (qn 42-50): taper -3.0 dB;
   - Horn 1 espr. bars 13-14 (49-55): -0.7;
   - Oboe 1 bar 12 (44-48): -0.7;
   - Clarinet 1 bars 52-54 (207-216): -1.9;
   - Flute 1 bars 64-65 (252-260): -3.1;
   - Cor anglais bars 153-155 (608-618): -3.3.
3. Two drops to digital silence, at qn 55.4-55.9 and 679.5-679.9 (finding 6).

What still sounds like a machine: the phrasing (finding 1), and string repeats in the upper strings and celli that still run together on the master (finding 5). Entries are not too tight: perceived spread at tutti onsets is already wide (below).

### What the finale's c07 measured (PHRASE_SHAPE by type, HP_CURVE, CAESURA)

- The finale's actor reported:
  - the Trumpet 1 solo phrases now fall 1.1 / 0.5 / -1.8 dB over their last second (c06 rose 0.4 / 2.6 / 5.8);
  - the rise from 0.15 to 0.8 s is +6.4..+7.0 dB;
  - string legato joins stay within ±20 ms;
  - beats with a tempo change went from 8.4 % to 21.1 % (seven caesuras of 0.05-0.10 s plus phrase arcs).
- Its c08 critics raised no problem with the shapes. B noted that caesura points inflate the accent-jump metric.
- My measurement on the c07 stems:
  - Lyric shapes work where they apply. Where a phrase's lane taper is 8 units or more, the stems taper a median 3.2 dB (winds, n 43) and 2.9 dB (brass, n 31).
  - Across all phrases the realised change is 0.26 dB per lane unit on winds, 0.30 on brass (CC1) and 0.39 on strings. On c50's printed lane changes (no shapes) the figures are 0.21 / 0.28 / 0.26.
  - The drive type did almost nothing: its lane taper is a median 1-1.5 units, because the f / ff scales (0.6 / 0.35) and the hairpin fades remove it, and its stem taper is 0.1 dB.
  - So the plan's depth needs 12-16 units at p-mf to reach a 3-4 dB taper, and the drive type will stay small at f / ff.
- I could not measure HP_CURVE on the finale: its stems were deleted mid-cycle.

### Open items from c50

- **60-250 Hz share of the tails: not a listener problem (measured).**
  - I measured each stop's 60-250 Hz band in 0.1-0.6 s after the cut against the same band in the 0.25 s before. Its decay changed by a median +0.6 dB, ranging from -2.9 dB (faster) to +2.9 dB (slower): qn 55 +2.5, 103 +0.4, 125.9 +0.9, 244 -2.9, 288 -2.5, 551 +2.9, 679 +0.8, 728 0.0.
  - The share rose mainly because the spectrum before the cut has less middle, and because the 2.3 kHz low-pass removes the tail's highs.
  - The two slower tails are each one instrument's soft release. At qn 55, Horn 1's own release carries the tail at -63 dBFS, with R Brass 6.8 dB under it. At 551, Horn 4's release carries it. No action.
- **Soft timpani rolls: unchanged within 1 dB of c49 (measured, K-weighted, timpani re master).**
  - Bar 11: -12.5 -> -12.3. Bars 13-14: -19.3 -> -19.1. Bars 40-43: -14.1 -> -13.2. Bars 181-182: -14.2 -> -15.2.
  - The master's 30-150 Hz share rose 2.2 dB in bars 40-43 and 1.2 dB in bar 11. Optional: a -1 dB timpani role over qn 156-172. Otherwise no action.
- **Trumpets a2 against Horns a2, bars 167-170.** Both play the theme in octaves at ff (Horn 1 G3 against Trumpet 1 G4), and the trumpets on top are idiomatic. B measured +2.8 dB against a limit of 2.5. A -0.5 dB role on Trumpets a2 over 664.5-679.6 meets the limit. Finding 2 re-levels each brass stem to its own K-weighted energy, so it leaves this difference where it is.
- **S3 (measured).** The bar-62 subito falls 14.0 dB by +0.3 s, and its largest 0.2 s fall is 8.8 dB against a limit of 9. I withdraw critic C's c50 suggestion to shorten `SUBITO_TAIL` ramp_s: it would push the fall past the limit.
- **Loops (actor's scan, checked).** Bass clarinet 480 and Trombone 1 716 reach 0.56 at 3.95 s on their dry stems. Those are 6.0-6.1 s notes, so the window covers barely 1.5 loop periods. The master passages stay under 0.40. No action.

### Plan items not yet applied: do they belong in c51?

- **Tutti entry spread: no (measured).**
  - At 237 score onsets where 7 or more tracks start, the MIDI note-on spread is already a median 179 ms (IQR 150-220), because the lead tables compensate each patch's attack.
  - The perceived spread (pcX, 194 onsets) is a median 137 ms first to last (IQR 95-179), 76 ms p10-p90 and 40 ms IQR.
  - The experts' 36-55 ms is a note-on spread that partly compensates attacks. Ours is already wider, and S2 asks for the opposite.
  - The finale dropped it in c07 for the same reason (142 / 85 ms).
- **Tempo breaths: no (measured map, risk inferred).**
  - The c50 map has 548 events: 36 % of beats change tempo, the median beat deviation from the 4-bar median is 0 %, p90 4 %, and 11 beats are more than 15 % slower (rits at qn 265-269 and 659-663, the caesura at 635, the fermata at 679, the end).
  - A wider breath rule would move every seconds-based fit (lead tables, LEVEL_SHAPES_S, swell fills) in the last cycle of the round, with no cycle left to refit them.
  - If the coordinator wants one, the safe form is the finale's `CAESURA`: 0.06-0.08 s at a lyrical section join that already has breath marks, e.g. qn 584 (recapitulation second theme). Measure it with the probe.
- **Room-noise bed: optional, after everything else.** See finding 6. No free room recording is in the repo; a synthetic bed is free of rights but is not a recording, so it is Dan's call.
- **Split legato and KS string tracks: no (inferred from memory and data).**
  - The main project settles at 43-44 GB.
  - Five more string instances would have to live in pass 2.
  - Every string lead, join and re-bow table was fitted on the KS Master Leg Slur rows.
  - c42 measured 82-98 ms transitions in all sections, so there is no slide problem for a legato-only patch to fix.
- **CC1-only "Mod + Expression Combo" test (plan section 5): skip in c51 and record the reason in LEARNINGS (measured lanes, manual p.64).**
  - Our string lanes already ride together (r 0.73-0.99).
  - The macro would raise vibrato above CC1 98 at ff and take away the +30 CC1 espr. offset (Cello solo and the f62 aliases have r 0.38-0.55 because of it).
  - It changes the representation more than the sound, and it costs a pass-2 slot.

## Findings, ranked by what a listener would hear

### 1. No phrase breathes: lyrical lines start at their loudest and do not taper (c51 plan item; measured; values from the finale's measured response)

**Where:** every lyrical line.
- The Lento solos: bars 5-14.
- The second theme: 47-68, including Clarinet 1 207-216 and Flute 1 252-260.
- Flute 1 and Bass clarinet espr.: 73-83.
- Bars 107-112.
- 123-130.
- The recapitulation's second theme: 145-157, including Cor anglais 608-618.
- The coda from 171.

**What is wrong (c50 stems, my phrase scan; the lanes are identical to c49's):**
- Lyric winds (n 41):
  - rise +1.1 dB by 0.8 s;
  - taper +1.4 dB;
  - peak at 0.30 of the phrase;
  - lane rise 0 / 0 units at 0.4 / 0.8 s, lane taper median 1 unit.
- Lyric brass (n 30): rise +1.5 dB, taper +1.5 dB, peak at 0.23.
- Lyric strings (n 14): peak 0.51, taper 3.5 dB. They rise +8 dB in their first 0.8 s, but that is the sample attack.
- By section, a quarter to two thirds of lyric phrases get louder into their last second:
  - Lento: 24 %;
  - second theme: 33 %;
  - 73-83: 69 %;
  - 123-130: 50 %;
  - recapitulation second theme: 22 %.
- Peaks sit at 0.18-0.30 in the second themes and the coda.
- The plan's lyric target is a centred arch: peak at about 0.44, start about 35 and end about 32 units under it. C c50 found 34 % of long notes flat, against the experts' 0-13 %.

**Fix (`tools/score_to_parts.py` plus `build/score_config.py`).** Port the finale's PHRASE_SHAPE as C c50 described:
- the option block;
- the grouping, type and offset code after the contours (`phrase_shapes`, `ps_scale`, `ps_weight`, `phrase_off`, dropping the per-note swell / swell_taper / taper contours inside a shaped phrase);
- its use in the CC11 value;
- the CC1 value on `CC1_DYN_TRACKS` with `cc1_floor`.

Three movement I changes:
- (a) On `CC1_DYN_TRACKS` (brass, Clarinets 1-2) put the offset into **both** CC1 and CC11. This is how the printed dynamics already drive these tracks; the measured response is 0.28 dB per CC1 unit, about the same as the winds' CC11 (0.21) and the finale's CC1-only brass (0.30). So the same values give about the same dB on every family.
- (b) Group phrases on score onsets and written ends (`sq`), so that doublings share one curve. Break string phrases at written rests of 0.5 qn or more and at printed dynamics that are not hairpin targets.
- (c) Make `start` a per-family value.

Values (lane units added to the printed level; C c50's values):
```
PHRASE_SHAPE = {"families": ("string", "wind", "brass"), "min_s": 2.0, "gap_s": 0.25,
    "start": {"string": 0, "wind": -8, "brass": -8}, "rise": [(0.4, 2), (0.8, 6)], "peak": (10, 0.44),
    "pre_end": (1.0, 4), "end": -12,
    "scale": {"ppp": 0.6, "pp": 0.8, "p": 1.0, "mp": 1.0, "mf": 1.0, "f": 0.6, "ff": 0.35, "fff": 0.2},
    "floor": 8, "cap": {"brass": 108}, "cc1_floor": 36, "hp_fade_s": 0.25, "step_s": 0.1,
    "types": {"build_cc": 10, "drive": (6, (10, 0.15), -10), "drive_min_bpm": 105,
              "lyric_spans": [(0, 56), (176, 272), (288, 332), (424, 448), (488, 520), (576, 628), (680, 728)]}}
```
Keep the finale's rule of no taper on an accented or crescendo-arrival last note.

Expected effect (inferred from 0.21-0.30 dB per unit):
- At p-mf, lyric winds and brass rise about +2.5-3.5 dB by 0.8 s.
- The arch is about 4 dB from start to peak.
- The last second tapers 16 units, about 3.5-4.5 dB.
- The drive type adds 1 dB or less at f / ff, as in the finale.

**Why the swell-in is safe for S2 (measured, scan48 on c50):** the first notes of lyric phrases are already perceived early, relative to the beat reference:
- winds: median -29 ms (p25 -48, p75 -1);
- brass: -13 ms;
- strings: +6 ms, and they get no dip (start 0).
A -8 unit start moves wind and brass attacks later by an inferred 5-20 ms, toward the beat.

**Order:**
1. Range-render the Lento (qn 0-56) and the second theme (184-272) with `cycles/c50/actor_scripts/rangetest50.py` before the full build.
2. Then the full render.
3. Then refit accents (`fit_accents.py`, 2-4 dB rule) and the c48 swell fills only where the scan says they moved.

**Pass criteria (stems, same phrase rule):**
- Lyric winds and brass:
  - median rise by 0.8 s of 3 dB or more (c50 1.1 / 1.5);
  - taper of 3 dB or more (c50 1.4 / 1.5);
  - peak at 0.35-0.55 (c50 0.30 / 0.23).
- Each named phrase above tapers 2 dB or more.
- Phrase-first pcX:
  - winds -30..+15 ms of the beat reference;
  - brass -25..+15 ms;
  - strings within ±20 ms of c50.
- The climax order and margins are unchanged, and the delivered LRA stays 14-16 LU.

### 2. The template made the loud tutti brighter and thinner than every reference: brass mids -4 dB, brass presence +4 dB (c50 mix; measured; fix simulated)

**Where:** every forte. Worst at the climaxes 121-126 (centroid 1192 Hz) and 160-166 (1206 Hz), and in the coda tutti 167-170 (1012 Hz); the Dvořák recording's loud frames sit at 824 Hz.

**What is wrong:** see the table above. In loud frames c50 sits 1.7 dB under Dvořák at 500 Hz-1 kHz, and 1.7 and 2.6 dB over it at 2-4 kHz and 4-8 kHz; c49 was within 0.4 dB of it in those bands.

The cause is the brass family EQ:
- bells of -5.4 dB at 475 Hz and -7.8 dB at 821 Hz, each 1.92 octaves wide;
- followed by +4.5 to +6.5 dB of make-up gain, which raised the brass's 2-5 kHz with everything else;
- the brass sum's 2-5 kHz minus 0.5-2 kHz went from -10.7 dB in c49 to -4.9 dB in c50.

The finale's c08 critic C measured the same overshoot on its first template render (500 Hz-1 kHz 2.0-2.5 dB low, 2-8 kHz 1.8-3.6 dB high). Two movements agree, so the cause is the template's EQ values, not one movement's mix.

**Fix (`build/mix.json`, a mix-only change applied before the c51 build):**
- `family_eqs.brass`:
  - bell 475 Hz: -5.4 -> **-2.7 dB** (bw 1.92);
  - bell 821 Hz: -7.8 -> **-3.9 dB** (bw 1.92);
  - add `{"band": "bell", "hz": 3200, "db": -3.0, "bw_oct": 1.0}`;
  - keep the 41 Hz HPF and the +1 dB shelf at 7.49 kHz.
- Brass `gain_db` deltas, which hold each stem's K-weighted level so B's balance checks stay put:

  | Track | Delta (dB) | Track | Delta (dB) |
  |---|---|---|---|
  | Horn 1 | -3.7 | Trumpet 1 | -2.0 |
  | Horn 2 | -3.6 | Trumpet 2 | -2.1 |
  | Horn 3 | -3.6 | Trumpet 3 | -2.2 |
  | Horn 4 | -4.0 | Trumpets a2 | -1.8 |
  | Horns a2 | -4.0 | Trombone 1 | -2.5 |
  | | | Trombone 2 | -2.2 |
  | | | Bass trombone | -2.3 |
  | | | Tuba | -2.7 |

**Simulated on the c50 stems:**
- Loud frames:
  - 500 Hz-1 kHz -7.6 -> -6.8 dB;
  - 2-4 kHz -9.1 -> -10.2;
  - 4-8 kHz -19.1 -> -20.3;
  - centroid 1062 -> 990 Hz on this method.
- Centroid at 121-126: 1189 -> 1085 Hz. At 160-166: 1189 -> 1112. At 167-170: 982 -> 912.
- Brass sum 2-5 kHz minus 0.5-2 kHz: -4.9 -> -9.3 dB (c49 -10.7).
- On the delivered chain the loud-frame centroid falls about 86 Hz.
- Removing the master EQ's 1.18 kHz bell would not help: it raises the centroid by 38 Hz. Keep the master EQ.

Optional second step:
- strings 1005 Hz bell -5 -> -2.5 dB;
- string `gain_db` deltas: Violins I -0.8, Violins II -0.7, Violas -0.5, Violoncellos -0.3, Double basses -0.1 (also the f62 aliases -0.8 / -0.7);
- simulated: loud 500 Hz-1 kHz -6.6, 2-4 kHz -10.5, centroid 982.

Accents gain too: less brass 2-5 kHz means softer accent fronts (BRIEF item 8).

**Check after the render:**
- re-run `bal50.py` (K-weighted; expect within 0.5 dB of c50);
- loud-frame centroid 1000 Hz or lower;
- 2-4 kHz share -10 dB or lower;
- climax order unchanged.

### 3. Bar 121 grows only 1.1 dB into the first fff; bar 159 grows 4.0 dB (c51; measured; fix simulated)

**Where:** bars 121-122 (qn 480-488). The whole orchestra plays a one-bar crescendo from ff into the fff at 484 (tam-tam, heavy beater), with an allargando.

**What is wrong:** K-weighted master per beat.

| Beats | c50 levels | Growth | Step into the next downbeat |
|---|---|---|---|
| 480-483 | -18.0 / -16.6 / -16.8 / -16.9 | +1.1 dB (c49 +1.2) | +3.8 dB at 484 |
| 632-635 | -19.0 / -17.7 / -16.4 / -15.0 | +4.0 dB | +3.0 dB at 636 |

Inside bar 121 the volume envelopes are flat or falling:
- Violins I 3.5 -> 3.7 dB;
- Violas 3.4 -> 1.5 dB;
- celli flat.
CC11 moves 115 -> 124 at the top of its range, where it gives about 1 dB. C c50's causes (the 484 roles) still apply.

**Fix: `LEVEL_SHAPES` rows (qn, dB).** Back off at the start of the crescendo and leave the arrival where it is.
- Violins I, Violins II, Violas, Violoncellos, Double basses, Flutes 1-2, Oboes 1-2, Clarinets 1-2, Bass clarinet, Bassoons 1-2: `[(479.75, 0.0), (480.0, -1.5), (483.9, 1.5), (484.4, 0.0)]`.
- Horns 1-4, Trombones 1-2, Bass trombone, Tuba, Timpani: `[(479.75, 0.0), (480.0, -1.5), (483.9, 0.5), (484.4, 0.0)]`.

**Simulated on the c50 stems (returns held):**
- bar 121 grows +2.9 dB;
- the step at 484 is +3.1 dB;
- bar 122 is unchanged (mean -13.5, momentary maximum -9.7 against bar 160's -8.3), so 160 stays the loudest.
- For comparison, C c50's version (+2 dB ramp held to 486 plus arrival lifts) gave only +2.0 dB of growth, and raised bar 122 by 0.6-0.8 dB, which would cut the delivered 160-over-122 margin (0.7 dB) to about 0.

Bar 121's crescendo is 4 qn into fff, so under finding 4 it stays linear. Under finding 1 it is a build phrase at ff, scaled 0.35, which adds about +0.4 dB at its end (inferred).

**Pass:**
- bar 121 grows 2.5 dB or more;
- the step at 484 is 3 dB or more;
- bar 122 stays within ±0.3 dB of c50;
- delivered S max 160 over 122 is 0.5 dB or more.

### 4. Hairpins are linear: diminuendos fade from their start, short crescendos arrive late (c51; measured)

**Where:** all hairpins of 2 qn or more over sounding notes.

**What is wrong (c50 stems, share of each hairpin's own dB change at 34 / 50 / 72 % of its length):**

| Family | Diminuendos | Crescendos |
|---|---|---|
| Winds | 0.25 / 0.40 / 0.69 (n 35) | 0.39 / 0.54 / 0.81 (n 58) |
| Brass | 0.28 / 0.43 / 0.59 (n 37) | 0.45 / 0.65 / 0.92 (n 30) |
| Strings | 0.43 / 0.58 / 0.72 (n 28) | 0.37 / 0.62 / 0.74 (n 52) |

Plan section 9's curves give 0.07 / 0.16 / 0.38 for diminuendos and 0.60 / 0.76 / 0.91 for crescendos. A printed diminuendo in c50 has done 40-58 % of its fall at the half-way point, where it should have held.

**Fix (C c50's values):**
- Port `HP_CURVE` from the finale's hairpin builder: `HP_CURVE = {"cresc": (0.4, 0.65), "decresc_last": 0.35, "min_qn": 1.0}`.
- Crescendos of 4 qn or more that end on f or louder stay linear: builds peak at the end (section 10).
- A diminuendo over one held note gets a point at 60 % of its length with 20 % of the fall.
- Keep the `HP_GAIN_DB` ramps held to the arrival.

**Pass:**
- diminuendos 0.30 or less of their fall at 50 % and 0.55 or less at 72 %;
- short crescendos 0.50-0.65 of their rise at 34 %;
- no more reversed hairpins than c50.

### 5. String repeats still run together on the master, and the returns filled the dips (S1, Dan's standing note; measured; owner critic A)

**Where:** the five spans where master dips stay under 2 dB:

| Span | Dip, stem / master band (dB) |
|---|---|
| Celli 464-484 | 1.4 / 1.4 |
| Celli 504-520 | 3.1 / 1.4 |
| Violas 440-468 | 3.9 / 1.5 |
| Violas 552-568 | 3.4 / 1.6 |
| Violins II 536-548 | 3.6 / 1.5 |

The actor's `dips50.py` measured these. The master dips fell 0-1.4 dB from c49 because the returns now fill them.

**What is wrong:** the strings separate repeats with volume dips (`STR_REP_DETACH`), not gaps. On 417 same-pitch string repeats on new score onsets (re-bow pieces left out):
- the MIDI gap is a median 14 ms;
- 79 % are under 40 ms;
- the celli median is 10 ms and the basses' 14 ms.
The plan's default is 90 ms for strings (section 8). In the finale's c07, `STR_REP_NEW_BOW` at 0.09 s / frac 0.3 together with the basses' detach dip on the celli took the celli's dry dips from 1.7-3.9 to 3.8-9.5 dB.

**Fix (A to set the exact rows):**
- `STR_REP_NEW_BOW` gap_s 0.06 -> 0.09 and frac 0.25 -> 0.30 (the finale's values).
- In the five spans above, `STR_REP_DETACH` dip_s 0.08 -> 0.10, keeping the string re-tongue lead so attacks stay on the beat.
- Measure with `dips50.py`.
- Target: master dips of 2.5 dB or more in those spans (inferred target: the spans that pass today sit at 2.2-4.5 dB).

### 6. Two drops to digital silence: before the Allegro and after the coda fermata (measured; low priority, cheap)

**Where:**
- qn 55.4-55.9 (66.6-67.3 s): the master falls to -95..-106 dBFS for 0.3 s and the mp3 to -90..-93. The Horn 1 stem goes from -79 dBFS to digital zero in one 50 ms frame at 67.05 s; the timpani stem reaches zero at 66.4 s.
- qn 679.5-679.9: the master sits at -68..-75 dBFS for 0.5 s.
- c49 was the same.
In a recording the room is always heard. The quietest 1 % of 100 ms frames in the Brahms recordings sits 27.5-32 dB under the integrated loudness; ours (mp3) sits 28.8 dB under, so this happens only in these two gaps.

**Fix (optional; no REAPER needed):**
- Add a steady synthetic room bed as an extra stem, summed into `00_Master.wav` before `deliver_master.py`:
  - pink noise;
  - high-pass at 84 Hz, as in Duc's bed;
  - low-pass at about 5 kHz;
  - -70 dBFS RMS on the master.
- That is 13 dB under the master's quietest 1 % (-57 dBFS), so it is inaudible under the music (inferred). It fills only the two gaps and the final decay.
- The plan asks for a recording. A synthetic bed is free of rights but is not one, so do it only if the coordinator or Dan agrees.

## Do not touch

- **The rest of the template mix:**
  - the returns' IR envelope, faders and 2.3 kHz low-pass;
  - the register and Duc sends;
  - Main at the seat ±0.8 with the side-only 200 Hz shelf, which put the width inside the references;
  - the family EQs other than the brass bands in finding 2;
  - the timpani and harp mics.
- **Delivery and loudness:**
  - the decay figures;
  - the climax order 160 > 122 > 167-170 > 26 and its margins;
  - `deliver_master.py` settings, the master EQ and `RIDE_TRIMS`.
- **Fitted tables:**
  - the S1 / S2 lead and dip tables;
  - `SUBITO_FRESH` and `SUBITO_TAIL` as they are;
  - the string release caps;
  - the basses' 600 ms pp cap;
  - `swell_fills48.json`: refit it, do not delete it.
- **Plus every c50 and earlier do-not-touch item.**
