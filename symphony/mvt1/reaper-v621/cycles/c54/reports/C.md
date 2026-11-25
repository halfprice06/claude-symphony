# Critic C, cycle 54: tempo, timing and transitions (render c53, score v621)

## Manual notes (third round: pages chosen for this lens; 2021 manual PDF pp. 94-97 and 108-110 read in full; MANUAL-GAPS.md and DIGEST.md used)

| Manual (PDF page) | What it says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| p.109 | Woodwind Sustain: "all 3 dynamic layers start to play simultaneously"; the Mod Wheel sets the level. Only "Sus Expressive" has "a slower attack". | Every wind entry on Sus MAX / Sus Non Vib | The patch has no slow attack to compensate, and the stems agree: Bassoon 1, Bassoon 2 and Contrabassoon entries reach body level 5-20 ms after note-on. The entry leads of 0.04-0.18 s on Bassoon 1, Oboe 2, Flute 2, Bassoon 2 and Contrabassoon therefore play the notes early by about the lead (finding 3; measured). |
| p.109-110 | Legato Repetitions (LegRep RRx4) for repeated notes inside a legato phrase; shorts have no release trails. | Wind repeats (MANUAL-GAPS #2) | No change proposed by this lens. |
| p.95 | Violas and Celli have a playable "Rep Runs Script" patch (slur from the lower note upward, from the higher note downward; loudness on CC11, velocity ignored). Pre-recorded runs are whole octaves. | The violas' and celli's 32nd-note run at qn 606.5-606.875 (bar 152), now four 82 ms notes on Sus MAX | Not used. The run sounds 66-102 ms early and 3-7 dB under its neighbours (finding 4; measured). `Violas Rep Runs Script.oib` and `Celli Rep Runs Script.oib` exist in `03 Effects`. |
| p.96 | Slur Runs exist only for 1st and 2nd Violins; "A minimum speed is sixteenth notes at about 125 beats per minute"; sustained notes inside the patch on CC11. | Violins I runs at 127, 158 and 270 (126 bpm sixteenths: at the stated minimum) | Used. The arrival notes after the runs at 160 and 272 are fresh Sus MAX strokes (c-series fix); the arrival at 128 is still a Leg BC target and arrives 0.2 s late (finding 2; measured). |
| p.99 (re-read from c48) | "The first note of a phrase has no legato effect." | A legato-row note whose predecessor is on another row | This is the mechanism behind findings 1 and 5: the target after a Sus-row note is a phrase-first note to the legato row, so the lead that compensates a transition does not apply. |
| MANUAL-GAPS #6 | RR reset on CC16 | Coda bass pedal | Still open; no new evidence from this lens. |

## Method (measured)

- Time map: `cycles/c53/rendered_build/parts.json` (`tempo`, each note's `qn` = moved note-on and `sq` = score onset), read with `tools/pcx.py` `TM`. It is identical to `build/parts.json` and to c52's map. Check against the audio: 88 timpani strokes sit at +18 ms (robust SD 3 ms), 106 harp notes at +4 ms (9 ms). The map matches the render.
- 4884 score note groups on all 42 instrument stems (re-bow and split pieces left out by matching `mockup-events.tsv` onsets), 4754 usable. Each has two measures: `pcx.attack_pcx` (t50, h10 in harmonic bands with the previous pitch excluded) and a broadband stem envelope (2 ms hop) with the same t50 / h10 rule. The same scan was run on c52 with its own parts.json.
- Every item below over 100 ms was checked a second way on the stem: the broadband envelope from digital silence for entries, the two pitch bands in 20-40 ms steps for joins, and a 4096-point spectrum (harmonics 1-3) for finding 2.
- The estimator gave false readings in three situations, and those rows are not reported: a same-pitch re-attack right after a staccato (celli 340: the staccato was read as the onset), a short pickup before a much louder note (Horns a2 310.5, celli 583, Bass clarinet 432.5: the reference level came from the next note), and joins where the new note swells (Cor anglais 26, Clarinet 1 224).

State of S2 (exposed notes, stem within 10 dB of the master; pcx against each beat's median): per-beat robust SD 15-52 ms by section, 34-39 ms in the Allegro, development and second theme; identical in c52 within 5 ms. By track in the fast music: strings 43-56 ms with 21-28 % of notes more than 60 ms off, winds 16-39 ms, brass 20-36 ms, timpani 19 ms. The string figures are where c47 stood (46-53 ms); the per-note rows of c48 did not reduce the spread over the whole movement. Findings 1, 3 and 5 name three mechanisms that produce stable errors by rule, not by note.

## Findings, ranked by what a listener would gain

### 1. Wind and brass slurs that start on a Sus-row note: the second note enters early and the first rings on, so two pitches sound together for about 0.14 s (measured; 79 joins)

**Where.** Every `slur_start_joins` onset on wind and brass tracks (`SLUR_START_SUS`, `tools/score_to_parts.py` line 3798): 79 joins. The most exposed are in the transition motive (eighth, dotted quarter, slurred eighths): Bassoon 1 131 and 133.5 (bar 33, "espr.", f, stem 0.6 and 2.5 dB under the master), Bassoon 1 stac 353.5 (1.5 dB under), Bass clarinet 307 (2.7), Clarinet 1 507 and 509.5 (4.1 and 2.4), Oboe 2 419 (4.2), Bassoon 1 362.5 (5.9), Clarinet 1 531 (6.5), Horns a2 667 (6.7).

**What is wrong.** The slur's first note plays on the Sus row and is held to the score onset of the second note plus 0.04 qn (note-off +19 ms). The second note plays on the legato row with a lead of 0.107 s (`SOST_JOIN_LEAD_S` 0.12 s capped at 0.45 of the eighth). The legato row gets no transition from a Sus-row note (p.99), and the Sus row is polyphonic, so both notes sound.
- New pitch reaches 10 dB under its body a median 46 ms before the beat (quartiles -74 and -26; 36 of 79 more than 50 ms early), and 4 dB under its body at -18 ms.
- Old pitch is 8 dB down only at a median +96 ms.
- Both pitches sound for a median 140 ms. At 126 bpm an eighth is 238 ms.
- The slur's first eighth is heard alone for a median 82 % of its written length, and for 47-65 % at Clarinet 1 507, Bassoon 1 131, 362.5, 525.5 and Trombone 1 525.5 / 533.5.
- Same values in c52. The c53 note "Trombone 1 525.5 139 ms earlier than c52 on unchanged data" is one of these joins: the estimator switches between the two overlapping pitches.

**The cor anglais at qn 275 is the same join and shows the fix.** c52: lead 106 ms, first note held to +19 ms; the new pitch was 10 dB under the old one until +60 ms and crossed it at about +65 ms (read as +158 late). c53: lead 166 ms, first note ended at -41 ms; the new pitch reaches 10 dB under body at -104 ms and crosses the old pitch at -45 ms (confirmed early: band crossing -45, pcx -84). In both renders the crossing falls 0-45 ms after the first note's note-off, and the new pitch needs about 60 ms from its note-on to reach 10 dB under body. So the first note's end sets where the change is heard.

**Fix.** In `tools/score_to_parts.py` (generic, off by default) add `SLUR_START_SUS["head_end_s"]`: when set, a `slur_start_sus` note ends that many seconds before the score onset of the note that joins from it, instead of at that onset + `LEG_OVERLAP`. In `build/score_config.py`:
- `SLUR_START_SUS = dict(SLUR_START_SUS, head_end_s=0.03)`;
- `SOST_JOIN_LEAD_S = {"default": 0.12, "wind": 0.07, "brass": 0.07}` (the per-track dict form already exists, c52 A #4), so the new pitch is 10 dB under body at about -10 ms and the two pitches overlap by about 40-60 ms;
- delete `retongue_leads.json` Cor anglais 275.0 (+0.06) so that note follows the rule (its lead falls from 0.166 to 0.07 s). This replaces the coordinator's proposal of +0.02, which would leave a 0.126 s lead with the first note still ending at -41 ms;
- re-check the existing rows on these onsets after the change (`leg_leads.json` Flute 2 275.5 / 277 / 281.5 / 283 / 283.5, Bassoon 1 413 / 531.5 / 575.5, Clarinet 1 421.5).
The size of the effect is inferred from the two cor anglais renders; run a range test on bars 33-34 (Bassoon 1) and 127-128 (Clarinet 1) first. Target on the full render: new pitch 10 dB under body within ±25 ms of the beat, old pitch 8 dB down by +40 ms, on at least 60 of the 79.

### 2. Bar 33 downbeat (qn 128): the Violins I play B5 on the ff downbeat and reach the printed C6 only 0.2 s later, 35 ms before the note ends (measured two ways, both renders)

**Where.** Violins I qn 127-128.5: the sixteenth run on Slur Runs into the accented, down-bow ff C6 eighth that ends the first theme (tutti stop at 128.5). Stem 7.4 dB under the master.

**What is wrong.** The C6 is a Leg BC MAX target with a 64 ms lead (0.32 s was asked; `lead_short` cut it because the run's last sixteenth is short). 4096-point spectrum, harmonics 1-3:
- B5 (the run's last note, note-off at -44 ms) is at 35-41 dB from -30 ms to +150 ms and still at 33 dB at +240 ms;
- C6 is at 10-18 dB until +150 ms, 27.7 dB at +180 ms and reaches B5's level at +210 ms; its note-off is at +245 ms.
pcx reads +175 ms in c53 and +174 ms in c52. The listener hears the leading note on the downbeat and a short C at the cut-off.

**Fix.** `build/score_config.py`: add 128.0 to `DOWNBOW_STROKE_AT["Violins I"]`, as c-series critic C #2 did for 160 and 272 (line 1797: "as Leg BC targets the new pitch dominated only at +0.21..+0.23 s"). The score prints a down-bow and an accent there. Check on the render: C6 over B5 by +30 ms, and the run's last note 10 dB down by +60 ms; if B5 still rings, end the 127.75 note at the stroke's moved onset.

### 3. Wind entries with long entry leads start early by about the lead: Bassoon 1 by 0.1 s on 14 of 14 loud entries (measured from digital silence, both renders)

**Where and what.** Clean entries (0.3 s or more of rest before, broadband rise 20 dB or more; n = 625 over all tracks). Time of the broadband stem envelope, ms against the score onset:

| Track, row, lead | n | 10 dB under body | half amplitude | Read |
|---|---|---|---|---|
| Bassoon 1, Sus MAX / Leg Slur MAX, 120 ms | 14 | -108 | -100 | 14 of 14 start 91-115 ms early: 72, 104, 128.5, 272, 320.5, 324.5, 330, 381.5, 388, 464, 552, 644, 664, and Bassoon 1 stac 348.5 |
| Bassoon 1, Sus MAX, 60 ms | 6 | -42 | -16 | early by 20-40 ms |
| Bassoon 2, Sus MAX, 60 ms | 23 | -49 | -35 | early |
| Contrabassoon, Sus MAX, 40 ms | 19 | -35 | -26 | all 19 between -27 and -39 |
| Oboe 2, Sus MAX, 180 ms | 9 | -145 | -15 | 44, 520, 664 start 145-160 ms early and are at half amplitude by -115..-155; 552 at -55; 408.5 (Leg Slur, 115 ms) at -96 |
| Flute 2, Sus MAX, 100 ms | 10 | -66 | -10 | 104, 160, 548, 552 at -61..-67; 628 (Leg Slur, 115 ms) at -82; Flute 1 has lead 0 on the same onsets |
| Horn 2, Sus MAX, 80 ms | 8 | -51 | -25 | 104 and 324 at -51 / -61 |
| Horn 1, Sus MAX, 90 ms | 8 | -53 | +29 | swelling attacks, on time except 520 (-79 / -75) |
| Clarinets, Flute 1, Oboe 1, trumpets, trombones, tuba, Horn 3 / 4, timpani, harp | | -30..+5 | -10..+20 | on time; keep |

The eighth pickups show it most: Bassoon 1 stac 348.5 (stem 2.6 dB under the master) starts at -120 ms and is at body level by -100 ms, so the pickup lasts 330 ms against 238 written. Bassoon 1 72 and 320.5 are 9 dB under the master. Most of the others are tutti downbeats 12-23 dB under the master, where the early fronts widen the attack: Bassoon 1, Oboe 2, Horn 1 / 2, Contrabassoon and Flute 2 are the earliest tracks at 272, 464, 520, 548 and 644 (10-90 % spread of those onsets 84-121 ms).

The loud leads date from series 1 (c07 C #3: loud entries "reached body - 3 dB at +0.12..+0.23 s"). The c53 stems no longer show that slow attack on these tracks, and the manual gives the Sustain rows none (p.109).

**Fix** (`build/score_config.py`; tuples are soft, loud, mid):
- `ENTRY_LEAD_S["Bassoon 1"] = (0.03, 0.02, 0.02)` (was (0.06, 0.12, 0.06));
- `ENTRY_LEAD_S["Bassoon"] = (0.025, 0.02)` (Bassoon 2; was (0.06, 0.06));
- `ENTRY_LEAD_S["Contrabassoon"] = (0.01, 0.01)` (was (0.04, 0.04));
- `ENTRY_LEAD_S["Flute 2"] = (0.0, 0.0, 0.0)` (was (0.0, 0.06, 0.0); the 0.04 s Sus MAX articulation lead stays). This also closes the Flute 2 against Flute 1 item: of 81 shared onsets, 100, 160 and 548 are early on both measures (-73 / -60 / -107 ms) and they are these entries; the other pcx differences over 50 ms are swell readings (h10 within 40 ms);
- Oboe 2: the loud lead is right for 100 and 128 and wrong for the others, so use rows in `build/entry_leads.json`: 44.0, 520.0, 664.0 at -0.13; 552.0 at -0.10; 408.5 at -0.165 (now -0.08);
- `build/entry_leads.json` Horn 2 104.0 and 324.0 at -0.05, Horn 1 520.0 at -0.07;
- then remove or re-fit the c48 Bassoon 1 rows that were fitted on the old leads (entry 316.5 / 360 / 516 / 406.5).
Target: these entries' half-amplitude point within ±30 ms of the beat median. The transfer is close to 1:1 because the attacks are fast (inferred from the two lead groups of Bassoon 1: 60 ms lead gives -42 / -16, 120 ms gives -108 / -100).

### 4. Bar 152 (qn 606.5-607): the violas' and celli's 32nd-note run is early, not together and under its neighbours (measured, both renders)

**Where.** Violas and Violoncellos, B-C-D-E in 32nds into the F at 607, under a crescendo, in octaves; celli stem 1.7-4.1 dB under the master, violas 5.9-7.7.

**What is wrong.** Four 82 ms notes on Sus MAX at v72 with a 0.12 s group lead (`GROUP_LEAD_AT`). A 32nd lasts 67 ms at 112 bpm.
- Violas: -90, -102, -87, -76 ms against the score onsets, more than one note early (c52 the same within 12 ms).
- Celli: -66, -10, -29, -98 ms, so the two sections are 24-92 ms apart on three of the four notes.
- The celli stem sits at -41 to -45 dB through the run, against -38 dB on the note before and -30 dB on the arrival.
The c48 rows (-0.06 s) are in the build; the values did not carry.

**Fix.** One range test, bars 151-153, two options:
- (a) Alias tracks on `03 Effects/Violas Rep Runs Script.oib` and `Celli Rep Runs Script.oib` for 606.5-606.875 (p.95: slurs chosen by direction, loudness on CC11), CC11 following the crescendo, group lead fitted from the test.
- (b) Without a new patch: the four notes on the loaded short rows (`Stac On Bow RRx9` on the celli, `Stac RRx9` on the violas), velocities rising 70 / 78 / 86 / 94, `GROUP_LEAD_AT` (606.5, 606.875) at 0.03 s for both tracks, 607.0 kept as its down-bow stroke.
Keep whichever puts all eight notes within ±30 ms of the score onsets with the two sections within 30 ms of each other, and the run within 3 dB of the note before it.

### 5. String legato notes after a Sus-row note are the least reliable class; a short list of exposed late notes (measured)

**What.** 93 string notes on a legato row whose overlapping predecessor is on Sus MAX or Tremolo (mostly after `short_sus` notes): robust SD 82 ms against the beat median, 28 % late by more than 60 ms and 14 % early. True legato joins: 46 ms, 11 %, 9 % (n 658). More lead does not help these: Violas 428 already leads by 226 ms and is +129 ms in both renders; its new pitch sits 9 dB under the previous note's ring until +100 ms.

Exposed rows, late by more than 60 ms in c53 and c52 (ms against the beat median; stem re master): Violas 428 +129 (-1.9 dB), 436 +81 (-2.5), 434 +74 (-3.8), 368 +115 (-7.1), 76 +147 (-9.0), 168 +148 (-9.3, after Tremolo); Violoncellos 356 +85 (-4.6); Violins II 400 +123 (-6.7), 290 +146 (-8.3).

**Fix.** `build/score_config.py` `SHORT_SUS_AT`: add these onsets for their tracks (the note stays on Sus MAX like its predecessor, with the re-attack lead), except Violas 168, which needs an `early_fills.json` row of +3 dB from the moved onset to +0.15 s. Inferred; verify each row on the render and drop the ones that do not land within ±40 ms.

One wind entry belongs here: **Oboe 1 578** (p, bar 145, stem 5.4 dB under the master) is +95 / +117 ms late on both measures in both renders. The stem holds -53 dB from -40 to +60 ms and then rises 12 dB by +130 ms; the track's `vol_db` has its first breakpoint after the note-on at +100 ms (9.6 dB, then 12 dB at +246 ms). Start that level row at the moved onset (qn 577.8) instead of after the beat.

### 6. Open items, cut-offs, tempo map, fermatas and the ending (measured)

- **Oboe 1 582: no row.** The pitch crossing is at about -30 ms. The measures disagree because the broadband stem sags 8-12 dB for about 80 ms around the join (-39 dB before, -51 dB at -20..0 ms, -45 dB after). If anything is done, it is a 3 dB fill over -0.06..+0.04 s, not a lead.
- **Cor anglais 275:** confirmed early; fix in finding 1.
- **Bar-14 horn ending:** not too long. The master is under -56 dB from 1.25 s and under -70 dB from 1.0 s before the Allegro downbeat; the rest lasts 1.36 s (44 bpm).
- **Cut-offs at the 17 stops with 8 or more parts:** the stems' -12 dB points fall a median 90-130 ms after the printed end, with a 10-90 % spread of 54-181 ms. Flute 2 is among the last at five tutti stops (+213, +242, +277, +262, +272 ms against a wind median of 104-123 ms), Horn 2 at four (+188..+262), Horn 1 at three. Flute 2 is 17-25 dB under the master, so this is a low-priority range test: `sus_release_cap_ms` 180 on Flute 2's Sus MAX.
- **Tempo map against `global.ily`:** every printed step is played within 0.6 % (poco rit. 176-184; animando 244-252; rit. 260-270 at 116 / 111 / 104 / 98 / 90; stringendo 448-464 at 128.6 / 132 / 135 / 138; allargando 480-488 at 120.7 / 114.1 / 105.9; sostenuto 99.5; rit. 656-664; Più lento 71.6; rit. 704-712; Tempo I 49.7). The exceptions are intended: 252-260 at 119.4 (printed 118), 628-636 at 115.7 (the 0.15 s caesura), the fermata beat 679 at 24 bpm (2.5 s; master under -60 dB for 1.2 s before the solo) and the last bar at 30 bpm (8 s).
- **Ending:** the last chord holds -48 to -52 dB for 6 s, tapers to -63 dB by the note end, and the master is at -88 dB 0.5 s after it. The mp3 ends 1.45 s after the score end, so the attacca has no long silence.
- **Keyswitches:** 1146 changes, none at or after its note; lead 9.5 ms minimum, 18 ms median.
- **Tutti arrivals** (10-90 % spread of pcx, parts within 22 dB of the master): 664 58 ms, 628 62, 160 64, 636 66, 484 68, 100 70, 488 78, 272 84, 464 93, 548 98, 520 107, 644 121, 440 122 ms. Finding 3 removes the earliest parts at 272, 464, 520, 548 and 644.

## EW-TEMPLATE-PLAN sections this lens touches that are not applied

- Section 5, legato overlap 45-80 ms (strings) / 33-58 ms (winds, brass): `LEG_OVERLAP` is 0.04 qn (19-21 ms). Finding 1 shows that a long overlap is harmful where the previous note is on a polyphonic Sus row, so any test of this section should cover legato-row to legato-row joins only.
- Section 6, keyswitches 40-800 ms before the note: ours are 9.5-18 ms. No failure measured (none late, probe 0).
- Section 7, fixed early shift per wind track: ours are per-note leads. The measured attacks do not support the 40-85 ms bassoon shift of that library (finding 3).
- Section 8, tutti entry spread 36-55 ms first to last: not applied as a seeded offset; the measured 10-90 % spread is already 58-122 ms, wider than the target, so the work is to remove outliers, not to add spread.
- Section 8 / 9, breath rule for tempo: applied in part (Lento agogics 44-51.5 bpm, `PHRASE_ARCS`, caesura 636, fermata 679). No change proposed.

**Do not touch:** the tempo map, `RAMP_SPANS`, `CAESURA` 636, `BEAT_STRETCH` 679, the 30 bpm last bar and `PHRASE_ARCS`; the delivery tail trim; `KS_LEAD` and keyswitch placement; the entry leads of the clarinets, Flute 1, Oboe 1, trumpets, trombones, tuba, Horn 3 / 4 and the timpani and harp timing (all within ±30 ms on clean entries); `DOWNBOW_STROKE_AT` 160 and 272; the Oboe 1 582 and Flute pair rows from c53; the c48 coda bass pedal shapes and cello solo fills.
