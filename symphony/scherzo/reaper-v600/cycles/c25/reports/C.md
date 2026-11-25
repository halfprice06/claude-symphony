# Cycle 25, critic C: blend and space (lens C1), on the c24 render and its delivered mp3

Measured on `cycles/c24/render/` (31 stems, returns 91-94, master), the delivered `cycles/c24/scherzo-mockup-c24.mp3` (decoded at 48 kHz, aligned to the master at +239 samples), `cycles/c24/build_render/` (parts.json, mix.json, roles.json, score_config.py), the c18 stems, and the c23 master. Note positions are the moved note-ons from parts.json, mapped to time with the parts.json tempo map. Bar b starts at qn 3(b-1). Levels are mean-square dB. "Correlation" is the L/R correlation at 300 Hz-8 kHz. "Side/mid" is the side level against the mid level at 300 Hz-8 kHz. "L-R" is the left level minus the right level. Scratch scripts were in `/private/tmp/claude-501/mockup-loop/scherzo-c25-C/` (deleted).

## Manual notes

MANUAL-READING.md has no row for c25. c21 (the last blend cycle) read L2 (pp. 219-223), so I read group L1: May 2021 HO manual PDF pp. 138-142, in full. MANUAL-GAPS.md was read, #13 in particular.

| manual (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| p.138: Close mics capture "the sound coming directly from the instruments". Main mics are in the fifth row and capture "more room reflections than direct sound". Surround "lacks definition" but adds depth. | The woodwinds are Close-led. Oboe 1/2 Main is 20.6 dB under Close, cor anglais 11.6 dB under. The strings and brass are Main-led. The timpani are Surround-led (template: Close -8.4 / Main -6.9 / Surround 0). | Partly. The oboes and cor anglais carry almost none of the recorded room, while the strings around them carry a lot (finding 2). The timpani follow the template, and the tutti numbers give no reason to change them. |
| p.139: the mixes can be set on the Play page or the Mix page. Each mic position has its own volume, pan and load state. | `mix.json` `mic_db` and `pan_by_mic`, written into the Opus state | Yes. |
| p.140: Master Channel Pan keeps the relative panning of the mics. Gain does not change the mic mix. | seats (`seat`, `reaper_pan`) and `gain_db` | Yes. The section positions are stable from row to row (Violins I's rows sit at L-R +6.0..+6.9 dB). |
| p.141: Channel Routing (Stereo, Mono, Mono From Left/Right, Swap). Stereo Double works only when the routing is Stereo. | Horn 3 `channel_map` 2 (Mono From Left, since c18); Violas div and Violin I solo `stereo_double` | Yes. Violas div with spread 0.6 now reads correlation 0.78 / 0.63 at 624-672 / 1044-1068 (c18: 1.00 / 1.00). Horn 3 is still 1.00 (Mid and Horn 1's mix were range-tested in c21 and rejected). |
| p.141-142: the Opus convolution reverb (preset, pre-delay, volume, Master). | Off on every track (`opus_reverb_off`). The hall is the four Spaces II returns. | Yes. The returns carry -12.75 dB of the dry energy (c18 -12.68). |
| p.142: the amplitude envelope (attack, hold, decay, sustain, release). "All instruments are programmed with envelope values to achieve a natural result, so please be careful when changing them." | The release caps: Violins II "Stac RRx9" / "Spiccato RRx9" 150 ms, Violins I short rows 100 ms, and c24 switched off the Violins I short rows' groups with no start mode | Changed with care, and the master shows no cost. The Violins II staccato stems fall to digital silence (-150 to -170 dB) 0.25 s after each peak, and Violins I "Stac RRx14" tails fall 11.5 dB further at +0.25 s than in c18. On the master the drops after isolated notes match c18 / c23 within 1 dB at all but two of 32 notes (pass list below). |

MANUAL-GAPS #13 (Mid instead of Close on the winds) has not been tried on any wind. c21 tried it on Horn 3 only (correlation 0.97, rejected). Finding 2 uses Main, which the c21 offline test measured.

## What passes on c24 (measured; keep)

- **Hall on the mp3.** For the G.P. after the fff (cut-off qn 1015.3, 242.74 s), I measured the drop from the peak of the last 0.2 s:
  - master: 18.3 dB at +0.3 s, 20 dB fall in 0.29 s;
  - mp3: 15.6 dB at +0.3 s, 20 dB fall in 0.39 s.
  - The c21 ride row holds the delivery gain flat through the tail (+6.3 to +7.5 dB from +0.1 to +1.0 s), so the limiter no longer releases into the silence.
  - Both files are inside Dan's limit (at least 13 dB, 20 dB fall within 0.50 s).
  - Wet/dry ratio stable since c18: -12.68 / -12.69 / -12.73 / -12.72 / -12.75 dB for c18 / c21 / c22 / c23 / c24.
- **The switched-off short-row groups did not make Violins I dry or thin.** On the same 76 "Stac RRx14" and 114 "Staccatissimo RRx9" notes, c24 against c18 (medians):
  - first-100 ms level -0.35 / -0.15 dB;
  - ring at 100-200 ms against the first 100 ms -0.24 / -0.14 dB;
  - harmonic brightness -0.08 / +0.33 dB;
  - body (200-700 Hz against 0.7-4 kHz) +0.03 / -0.11 dB.
  - Only the stem's far tail changed: "Stac RRx14" at +0.25 s after the peak went from -23.6 to -35.1 dB.
  - On the master, isolated Violins I notes drop by the same amount as in c18 / c23 at +0.3 s (qn 81: 20.4 / 20.2 / 21.1; 801: 12.1 / 12.1 / 12.7; 957: 13.3 / 12.0 / 12.2 dB). Only 57 (12.8 -> 10.8) and 357 (9.3 -> 13.2) moved by more than 1 dB.
  - Violins I's short notes still ring longer on the stem than Violins II's: 100-200 ms ring +0.5 against -1.3 dB.
- **Spiccato and Staccatissimo sit in the same place.** Spiccato against its neighbours in the same line:
  - L-R -0.0 dB (median), so the same seat;
  - 5-12 kHz air +1.0 dB more than the same notes had on Staccatissimo / Stac in c18.
  - Only the level stands out (finding 1).
- **Tone matches between sample sets:**
  - Violin I solo (DIV A) against the Violins I section at the same pitches (83-93): harmonic brightness -1.7 dB, air -1.0 dB (median), L-R +5.5 against +6.1. The solo's correlation is 0.94, a point source, which suits a soloist.
  - Violins II con sordino (504-552) against open (588-624): brightness -13.0 against -2.7 dB. The mute is audible.
  - Handover from the borrowed harmonic to the harp harmonics: Violins II-track E6 -49.6 / -49.4 dB, harp harmonics -46.4 / -46.5 (L-R +4.5 / +4.5), the same as c18.
- **Brass in one hall.** Trumpet 1 and Horn 1 in 312-360: correlation 0.87 / 0.91, L-R -3.6 / +4.1, both on R Brass with Main-led mics. The timpani in the tuttis: correlation 0.34-0.39, L-R -1.5 dB.
- **Low end (master share, 101-120 / 301-320 / 329-339):**
  - 100-250 Hz -8.5 / -8.5 / -10.1 dB;
  - 250-500 Hz -5.3 / -6.3 / -6.8 dB;
  - references: Dvořák -6.6 / -6.3, Brahms -7.6..-8.8 / -5.95..-6.3;
  - basses' div. pizz. 253-268: -9.2 / -9.1 dB.
  - No build-up. Same as c21.
- **S3.** The R Strings return falls smoothly through the sub. p at 360 / 828 and the sfp at 900: the largest 10 ms steps are 4.0-5.0 dB, inside the frame scatter.
- **Loop pulsing (BRIEF 8).** Autocorrelation at 3.95 s of the 100-300 Hz band, the 0.7-5 kHz band and the centroid, all equal to c18 within 0.06:
  - Violins I ppp G sharp 0.5-23: +0.17 / +0.25 / +0.26;
  - Violins I ppp G sharp 1092-1124: +0.04 / +0.10 / +0.10;
  - harmonic E6: +0.14 / +0.14 / +0.04;
  - Horns 3-4 drone 456-504: -0.13 to +0.00;
  - Horn 1 1100-1127: +0.14 / -0.32 / -0.02.
  - No pulse.
- **Measured but not proposed: the cut-off at bar 72 into bar 73 on the mp3.** The delivery gain rises from +7.8 to +14.0 dB within 0.3 s of the cut-off (qn 215.9), so the ff chord's hall tail drops 13.1 dB at +0.3 s on the master but only 6.6 dB on the mp3. The pp entries of bar 73 start on the cut-off. A ride row would either swell the held pp chord or not reach the tail, so as in c21, I propose no row.

## Findings, ranked by what a listener would hear

### 1. Violins I's Spiccato notes (D5, D sharp 5, F sharp 5) stand 2.8 dB over the staccato notes around them, so the theme line is uneven by pitch (measured)

Where: every Violins I staccato statement. The 90 "Spiccato RRx9" notes include the 68 that c24's `STAC_ROW_BY_PITCH` moved off "Staccatissimo RRx9" / "Stac RRx14". Examples: qn 54-66 (bars 19-23), 102-128 (the counterstatement strings), 294-356 (the hemiola and the ff tutti), 747-800 (the reprise), 330-356 / 930-956.

What is wrong: the c24 row change brought the shorter decay the separation needed, but it also made each of those pitches louder and a little brighter than its neighbours. Inferred: in a leggiero staccato line, every D, D sharp and F sharp now sounds lightly accented, and no printed mark asks for that. Dan asked for fewer accents (2026-11-11: median accent +1..+2 dB, nothing over +3). These notes carry no accent mark, yet 30 of the 68 stand more than 3 dB over their neighbours.

Evidence: the first-80 ms peak (10 ms windows), set against the median of the non-Spiccato short notes within 4 qn. The c18 column is the same notes (paired by score onset) when they still played Staccatissimo / Stac, measured the same way:

| measure (median, 68 notes) | c18 (other rows) | c24 (Spiccato) |
|---|---|---|
| peak over neighbours | -0.7 dB | **+2.8 dB** |
| notes over +3 dB | 14 | **30** |
| harmonics 3-8 against 1-2, over neighbours | +0.4 dB | +2.0 dB |
| 5-12 kHz against fundamental, over neighbours | +3.1 dB | +4.1 dB |

- Across all 78 Spiccato notes with neighbours: +2.6 dB median, p90 +5.7.
- The worst are in the ff tutti: 321 +8.6, 355 / 355.5 +6.0 / +5.7, 356 +7.2, 342 +5.5, and the reprise 753 +7.3.
- The stereo position matches (L-R -0.0 dB median), so this is a level and colour step, not a seat step.

Fix (instrument side; a row volume in the Opus state, as Dan's rule allows):
- `build/mix.json`, track "Violins I", append to `region_gain_db`: `{"rows": [], "row_db": {"Spiccato RRx9": -2.5}, "_c25": "critic C #1: Spiccato pitches +2.8 dB over their staccato neighbours"}`.
- A uniform row gain leaves each note's own decay ratio unchanged, so c24's separation figures (D5 4.7, D sharp 5 7.6, F sharp 5 6.0 dB) should hold. The trough before a non-Spiccato next note gets 2.5 dB deeper, which helps.
- Measure after the build:
  - Spiccato over neighbours, median within -0.5..+1.0 dB and no more than 8 notes over +3;
  - the bar 23 figure at every occurrence (its F sharp 5 at qn 66 is a Spiccato note): nothing worse than c23 (Dan's first check);
  - the Spiccato notes' 60 ms peaks still within 1 dB of the c23 levels of the same notes, so the c24 gain in presence over c23 is not lost.
- If critic A's fix for bars 115 / 315 moves the tutti F sharp 5 (342 / 346 / 942 / 946) back to "Stac RRx14", this gain does not conflict: it then acts on fewer notes.

### 2. The oboes and cor anglais are still dry mono points beside a string section with its own stage. The counterstatement's picture narrows every time the winds call (measured; the benefit for the listener is inferred)

Where:
- the counterstatement, bars 29-44 (winds' calls qn 84-90 and 96-102, strings' answers 90.4-96 and 102.4-108);
- Oboe 1's trio middle part, 185-196 (qn 552-588);
- the cor anglais' pp staccato arpeggio, 95-100, and every theme head the cor anglais doubles.

What is wrong: c24 changed nothing here, and the c21 numbers still hold on this render:
- master, winds' calls: correlation 0.84 / 0.88, side/mid -10.5 / -11.7 dB;
- master, strings' answers: 0.39 / 0.40, -3.5 / -3.2 dB, at equal level (-41.2 / -39.5 against -41.1 / -40.0 dB);
- Oboe 1 stem in 552-588: 0.99, side/mid -17.2 dB, unchanged since c18;
- Violins I and violas beside it: 0.42-0.46, -3.3 to -3.9 dB.

The oboes take Main 20.6 dB under Close, and the cor anglais 11.6 dB under (the EW template's values; p.138: Main is where the room reflections are). Their only room is the R Winds return, which the "too wet" cuts lowered and Dan's rule keeps there. Inferred: a dry centre point among wide strings sounds nearer and separate, not in the same hall. Dan's "not too dry, thin or dull" applies here.

The research item (RESEARCH-FINDINGS part 1, line 61: winds "Close 1.0 / Main about 0.35 (-9 dB), with Oboe Main lower still"; EW-TEMPLATE-PLAN 1) sets Oboe Main under -9 dB. I reject the "Oboe lower still" part, on these numbers:
- at -20.6 the oboe's stem correlation is 0.99, against 0.42-0.46 for the strings around it;
- c21's offline mix of Close-only and Main-only range renders (`cycles/c21/CHANGES.md`, "Woodwind stage") gave Oboe 1 0.97 / 0.94 / 0.90 / 0.82 at Main -12 / -9 / -6 / -3 under Close, and cor anglais 0.94 / 0.90 / 0.84 / 0.75. At -6 the oboe's note-end drop at +0.15 s went from -23.0 to -21.6 dB, inside the -18..-24 target. Only the 250-500 Hz share was not measured, and that is why nothing was adopted.

Fix: finish the c21 test. There is no new tool work.
1. Range-render Oboe 1, Oboe 2 and cor anglais over qn 81-110 and 549-590, once with Close 0 / Main -150 and once with Close -150 / Main 0. Use one start for all passes, before each track's last keyswitch, and allow c24's settle time after the rebuild (renders made right after a rebuild lost notes).
2. Mix offline at Main -9 and -6 dB under Close. Adopt the lower Main level that meets all of these:
   - Oboe 1 stem correlation 0.92 or less in 552-588;
   - 250-500 Hz share of the stem up by less than 1.5 dB;
   - note-end drop at +0.15 s between -18 and -24 dB;
   - master correlation in the winds' calls 0.80 or less, with the c24 stems and returns summed (the sends are linear).
3. Set `build/mix.json` `mic_db` Main on Oboe 1 and Oboe 2 together (expected -9 or -6) and on the cor anglais (expected -9). Re-fit `gain_db` so each track's K-weighted level matches c24: about -0.5 dB at Main -9 on the oboes, -0.2 dB on the cor anglais.
4. Leave the flutes (Main -4.7, stem 0.91), the clarinets (-3.4, 0.77) and the bassoons alone. Do not raise the R Winds send or fader.
5. If the oboe turns thick at both levels, report it and keep -20.6.

Pass on the render: the G.P. after the fff within 1 dB of c24 on the master (18.3 dB at +0.3 s), and the winds' 20 dB fall at the G.P. 0.30 s or less.

### 3. Flute 1 "col Vl. solo" (bars 349-356) sits 8.4 dB under the solo violin it doubles in unison, so the printed doubling colour does not reach the listener (measured levels; audibility inferred)

Where: qn 1044-1068. The printed dynamics are Violin I solo pp, Flute 1 pp "col Vl. solo", Violins II "la metà" pp an octave below, violas ppp, celli pp.

What is wrong: the passage levels on the c24 stems:

| track | level |
|---|---|
| Violin I solo | -40.6 dB |
| Flute 1 | -49.0 dB |
| Violins II | -48.9 dB |
| violas | -50.0 dB |
| Violas div | -55.4 dB |
| celli | -50.7 dB |

- The flute plays the solo's notes at the same pitch (pitch median 88 in both). In roles.json the solo has [1040, 1068, +8] and Flute 1 has [1044, 1068, -9.5], a 17.5 dB difference between the two envelopes.
- The c01 row was meant to put the solo over its doubling (critic B #2 + C #1). It now buries the flute: inferred, a unison partner 8 dB down at the same pitch is masked and adds no colour.
- The flute's own CC11 already sits low (39-47).
- The solo's place in the hall, its tone against the section and the harp cap (B, c24) are fine and stay.

Fix (slow balance, a whole-passage role, as the rule allows): `build/roles.json` "Flute 1" [1044, 1068, -9.5] -> **[1044, 1068, -6.5]**. Keep the start edge where it is (in the rest before the flute's moved note-on at 1043.02) and keep the end edge, so note_slew draws no new move inside a note.

Pass on the render:
- Flute 1 at 1044-1068 between -46.5 and -45.5 dB, 5 dB under the solo;
- the solo's own level within 0.5 dB of c24;
- master level in bars 349-356 up by 0.5 dB or less.

## Do not touch

- The returns, their faders, filters, pans, IR envelopes and every send (wet/dry -12.75 dB, G.P. 18.3 dB at +0.3 s on the master, 15.6 on the mp3).
- The c21 G.P. ride row and the delivery chain.
- The release caps and the switched-off Violins I short-row groups (no measured cost on the master).
- Violins I's Spiccato row choice by pitch (only its level, finding 1).
- Violas div stereo double 0.6, the Violin I solo's mic, EQ and stereo settings.
- The borrowed harmonic and the harp harmonics at the handover, the Violins II con sordino lane.
- The trumpets' and horns' mics and seats, Horn 3's routing, the timpani's template mics, and the low end at 100-500 Hz.
