# Cycle 19, critic A: articulation and phrasing (on the c18 render)

All numbers were measured on `cycles/c18/render/` (stems and master) and on `build/parts.json`, unless marked "inferred". Stems are post-fader; where a level is compared between notes the `vol_db` value at the note was subtracted. Nobody heard the audio.

Limits of this report. Not measured this cycle: the stop of bar 204, the dal niente entries, harp (harmonics, étouffez, glissando), crash cymbals and bass drum, timpani strokes and rolls, tremolo row levels, the divisi / "4 soli" / sul tasto passages, perceived attack centres (S2), the sfp of bar 149. Of the required reading I read BRIEF.md, c18 CHANGES.md and the c18 report A in full; HISTORY.md, MANUAL-GAPS.md, the LEARNINGS files, FINDINGS.md and EW-TEMPLATE-PLAN.md were read by section heading and keyword only. No per-note track volume move is proposed anywhere below.

## Manual notes

Third round, own choice: May 2021 HO manual, PDF pages 100-103 (Hollywood Brass: long and short instrument types), read in full, because the two top problems are brass joins in the chorale and brass accents.

| Manual (PDF page) | Where it applies | Does the render follow it |
|---|---|---|
| p.101, Sustain: loudness is on the Mod Wheel; all four dynamic layers start together | every brass sustain note; the chorale's whole notes (bars 223-234) | Yes (CC1 and CC11 lanes). The measured start of these rows is slow: 60-110 ms from note-on to 3 dB under the body (finding 1). |
| p.101, Portato: each note held "its full length—or close to it—but without tying it to the next note" | the chorale's untied whole notes between the printed breaths (brass print a breath only at qn 892, tuba and bass trombone at 900) | No. Every brass whole note ends 95-155 ms before the bar line and the next starts 50-90 ms before it; the stems have a hole of 60-120 ms, 5-7 dB deep, at every bar line. Finding 1. |
| p.101, Sustain Accent: velocity sets the attack, Mod Wheel the body | brass accents (247-262, 91-92, 277) | Not used, by Dan's rule (weight, not bite). Stays closed. |
| p.101, Sustain Marcato: velocity drives a low-pass filter on the marcato attack | the same | Not used; MANUAL-GAPS item 1 stays as it is. |
| p.102, Short rows have no release trails; some room sound follows the sample | the unaccented eighths of bars 91-92 and 277 on trumpets and tuba | The eighths are played on the sustain rows for 79-109 ms and read 4-7 dB under the accented notes around them (finding 4). "Stac DblTng RRx9" and "Marc Shrt DblTng RRx4" are on the 1TP KS Master (`ks_maps.json`). |
| p.103, Double Tongue; Repetitions at 170 / 145 / 120 bpm, synced to tempo | the same eighths | Not used. The Repetitions patch is not needed for single eighths. |
| p.102, Marcato: round robin of 4 | "Marc Shrt DblTng RRx4" if used for finding 4 | A CC16 reset before the bar is needed for repeatable takes (LEARNINGS c14). |

MANUAL-GAPS items that bear on the findings: item 2 (re-tongue rows) is finding 4; item 9 (portato rows) is the manual's own answer to finding 1, but the KS Masters in use carry no portato row, so finding 1 uses note lengths.

## Findings, ranked

### 1. Chorale bar lines (bars 227-233): all eleven brass players stop and restart inside the same 150 ms; the fix is note lengths (measured; the predicted gain is a simulation)

Where: qn 904-932, Horns 1-4, Trumpets 1-2, Trombones 1-2, Bass trombone, Tuba; then the clarinets and oboes.

Master, lowest 30 ms frame in [-0.25, +0.2] s against the 0.3 s before: 896 -2.3, 900 -0.3, 904 -3.9, 908 -4.5, 912 -1.7, 916 -5.1, 920 -4.3, 924 -4.6, 928 -4.0, 932 -3.1 dB (the actor's numbers within 0.5 dB). The minimum lies 25-85 ms before the bar line at nine of ten.

Floor of the measure: the same window placed 1, 2 and 3 qn after each bar line, where nothing changes, reads +1.6 to -5.0 dB, median -1.8 (tremolo and roll). A 2 dB target is at the floor; 3 dB is the reachable target.

Per stem, the hole (level more than 3 dB under the lower of the levels before and after), in ms against the bar line, medians over 904-928:

| track | row | note-off | note-on | hole from..to | depth | rise (note-on to 3 dB under body) | release (note-off to 3 dB down) |
|---|---|---|---|---|---|---|---|
| Trumpet 1 | Sus Non Vib MAX | -95 | -50 | -33..+32 | -5.8 | 82 | 75 |
| Trumpet 2 | Sus Non Vib MAX | -135 | -80 | -65..+10 | -7.0 | 90 | 70 |
| Trombone 1 | Sus MAX | -130 | -50 | -75..+52 | -5.6 | 102 | 55 |
| Trombone 2 | Sus MAX | -120 | -50 | -40..+35 | -6.3 | 85 | 80 |
| Bass trombone | Sus MAX | -135 | -50 | -70..+50 | -7.3 | 100 | 65 |
| Tuba | Sus MAX | -130 | -70 | -95..+10 | -6.2 | 80 | 35 |
| Horn 1 / 3 / 4 | Sus MAX | -155 / -110 / -110 | -90 / -50 / -50 | -45..-35 / -85..+85 / -50..-10 | -4.6 / -5.5 / -8.2 | 55 / 135 / 40 | 110 / 40 / 60 |
| Clarinet 1 / 2 | Sus Non Vib | -100 / -112 | -35 | -55..+5 / -80..-15 | -8.1 / -9.8 | 40 / 20 | 45 / 32 |
| Oboe 1 / 2 | Sus MAX | -120 / -182 | -70 / -120 | -78..+170 / -140..-33 | -6.0 / -6.4 | 240 / 87 | 42 / 53 |
| Violas, Violins I / II | Leg BC / Leg Slur | (overlap) | -205 to -280 | 3-5 dB for about 100 ms, ending at the bar line | | | |
| Violoncellos, Double basses | Sus MAX | -105 | -100 | -20..+215 / -35..+35 | -4.9 / -5.7 | | |

The brass are the loudest stems before every one of these bar lines except 916 (Trombone 1, Trumpet 1, Trumpet 2, Tuba at -37 to -41 dBFS each; Violas -37 to -39). Their holes all contain the window -40..+10 ms.

Simulation: I filled each stem's hole (gain up to the lower of its level before and after, 20 ms smoothing), summed the 31 stems with the four return stems unchanged, and measured the dip again (the sum of the stems reproduces the master's dips to 0.1 dB).

| bar line | rendered | brass filled | winds filled | upper strings filled | all pitched filled |
|---|---|---|---|---|---|
| 904 | -3.9 | -2.6 | -3.6 | -3.6 | -2.0 |
| 908 | -4.5 | -3.6 | -4.3 | -4.4 | -3.3 |
| 916 | -5.1 | -5.1 | -4.9 | -4.0 | -4.2 |
| 920 | -4.4 | -2.8 | -3.9 | -4.0 | -2.4 |
| 924 | -4.6 | -3.2 | -4.4 | -4.4 | -2.8 |
| 928 | -4.0 | -3.5 | -3.8 | -3.9 | -3.0 |
| 932 | -3.1 | -3.1 | -2.7 | -2.5 | -1.8 |

The returns still carry the holes in this simulation, so a real fix gains a little more. Bar 908 is not a join: Violins I (-30.6 dBFS, 5 dB over the next stem) hold a tied note there and the printed hairpin turns; leave it. Bar 916 is the upper strings (Violas enter on "Leg Slur MAX", Violins I on "Leg BC MAX", both dip 3-5 dB in the 100 ms before the line).

The woodwind hole is not the fast fall of their stems: clarinets and oboes start to fall 32-53 ms after note-off like the brass (35-80 ms); their hole comes from a 65-77 ms gap in front of a 20-40 ms rise. Upper-woodwind and trumpet stems do fall further than the rest once a note has ended (0.2 s after the end of a note followed by a rest: flutes -20 to -28 dB, oboes -24 / -25, clarinets -25 to -28, cor anglais -33, trumpets -40 to -47, horns -12 to -17, trombones -15 to -21, strings -10 to -18), so the other movements' finding applies here and the trumpets are the driest; that matters at phrase ends, not at these joins.

Fix (`build/score_config.py`, `INSTR_POST` `gap_set` / `note_end` / `onset_lead`; no fader, no second instance):
- Brass, qn 892-932, notes of 3 qn or longer whose next note has a different pitch and no printed breath between: end the old note 0.03 s after the new note's moved note-on (the sustain rows are polyphonic; the old note's 55-80 ms release then covers the new note's 80-100 ms rise). Key, for example, `"gap_set": {"brass": [{"from": 892.0, "to": 932.5, "min_qn": 3.0, "gap_s": -0.03, "diff_pitch": True}]}`.
- Same-pitch whole notes (Bass trombone and Tuba C at 916-928, Trombone 1 C4 at 920-928, Horn 2 C4 at 916-928; an overlap would stop the new note): gap 0.02 s, and move the two pedal players apart so their holes do not coincide: Tuba note-on 0.12 s before the bar line, Bass trombone 0.03 s before it (`onset_lead`). S1 is kept: a 0.02 s gap in front of an 80-100 ms rise still gives a dip of about 3 dB on the stem.
- Printed breaths (892 on horns, trumpets, trombones; 900 on tuba and bass trombone; 920 on the upper woodwinds; 900 and 912 on the bassoons) keep their present gaps.
- Clarinets 904-928 (not 920): gap 0.02 s (predicted hole 0: rise 20-40 ms, release 32-45 ms). Oboe 2: end the old note 0.03 s after the new note-on. Oboe 1 (rise 240 ms on C5-range notes): note-on 0.20 s before the bar line and the old note held to 0.05 s before the bar line.
- 916: Violas' first note of the phrase (sq 915-916, "Leg Slur MAX") and Violins I at 916: CC11 +8 units from 0.25 s before the bar line to 0.30 s after it, return over 0.55 s (the lift shape of Movement II c57; no pre-fall).
- Check with the table above: brass holes under 3 dB at the different-pitch joins, master dips at 904 / 920 / 924 / 928 at 3 dB or less. If the brass joins then sound slurred on the stem (no dip at all at more than half of them), shorten the overlap to 0.

### 2. Brass accents are below audibility; string accents at f are the outliers; woodwinds are close (measured)

Measure: each accented note against unaccented notes on the same track, same pitch, same row, same chord size, resting CC11 within 3 units and CC1 within 4, first 0.3 s, fader removed. 557 accents have such a match.

| family | n | median | quartiles | isolated n | isolated median | isolated quartiles |
|---|---|---|---|---|---|---|
| woodwinds | 182 | +0.8 | +0.3 / +1.2 | 53 | +0.8 | +0.3 / +1.5 |
| brass | 196 | +0.5 | +0.2 / +0.9 | 34 | +0.4 | -0.1 / +0.9 |
| strings | 179 | +1.6 | +0.3 / +2.8 | 74 | +1.9 | +0.2 / +2.8 |

Per track: Trumpets 1 / 2 / 3 +0.2 / +0.3 / +0.3 (quartiles +0.0 to +0.6), Trombone 2 +0.4, Tuba +0.4, Horns +0.6 to +0.8, Trombone 1 +0.7, Bass trombone +0.8; woodwinds +0.2 (Clarinet 1) to +1.0; Violins I / II +2.0 / +1.9 (14 and 11 notes over +3 dB of 49 and 46), Violas +1.6, Violoncellos +1.5 (isolated +2.8), Double basses +0.6.

Judgement by family:
- Brass: under. +0.2 to +0.5 dB is not heard as an accent (inferred: a level step under about 1 dB is not noticed). The cause is the shape, not the amount. On brass CC11 is volume at 40 log10, so the c18 amounts would give +1.65 dB (10 %), +1.0 (6 %), +0.85 (5 %) if they were sounding; the bump is back at 0.22 s and the rows need 80-135 ms to speak (finding 1), so most of it is spent before the note has its body. Windows against matched plain notes (relative to each note's own body at 0.45-0.7 s): trumpets -0.6 dB at 0-80 ms, +0.2 at 80-200 ms; trombones -1.7 / -0.3; horns +0.2 / +0.7. The 2-5 kHz front over body is the same as on plain notes or lower (trumpets -11.2 against -11.0 dB, trombones -7.5 against -5.1, horns -20.4 against -14.5): no bite.
- Woodwinds: slightly under, acceptable. +0.7 dB at 80-200 ms, 0.0 at 0-80 ms; slope 0.09-0.10 dB per CC11 unit.
- Strings: the median is right (+1.6 to +2.0, in the first 80 ms +2.6, at 80-200 ms +1.9, at 200-400 ms +0.7: a front, not a bulge). The upper quartile is over. Slope 0.19-0.24 dB per unit in the first 0.3 s.

The "Sus MAX is flat above 103" question: for accents it is not. "Sus MAX" accents with resting CC11 104 or more and a 10-unit bump read a median +1.7 dB (n 49, quartiles +0.2 / +2.6), the same as at 96-103 (+1.9, n 51) and at 80-95 with 8 units (+1.9, n 42). The flat part applies to held bodies (the range test of bars 1-2), not to the first 0.3 s.

Outliers over +4 dB (26 of 557, all but 4 on strings):
- String "Sus MAX" notes at printed f, resting CC11 82-89 (the steep part of the row): Violins I qn 40 (+6.5), 15 (+4.3), 88, 68, 525, 527 (+3.4 to +3.8); Violins II 88 (+6.4), 56 (+6.3), 14 (+5.3). 7-8 units there are worth up to 6 dB.
- Top-register and stop-bar notes at ff: Violins I G6 at 806 (+8.0) and 998 (+4.0), B5 at 813, A5 at 990; Violas and Violins at 660 and 813 (+4.3 to +5.4; these are the notes before the stops of bars 166 and 204, so part of it is the stop's own CC11 shape).
- Violoncellos on "Leg Slur MAX" in 1073-1084 (E3 +7.9 / +8.0, C3 +5.2 / +4.9; 1-2 matches each, so low confidence).
- Horn 1: E flat 4 at 56 (+9.9, one match), A flat 4 at 84 and 816 (+5.2, +4.7; A flat 4 is one of the pitches reported in anti-phase between L and R, and I measure on the mono sum, so these two are unreliable).

Trumpet 3's "+3.1" in the actor's table is not its accents (+0.3 here, 30 matched). It is pitch level on "Sus Non Vib MAX": normalised to CC11 100 and against the track median, C4 -3.7 dB (3 notes, 2 accented), G4 +1.9 (10), B flat 4 +4.0 (2). Trumpet 2: B4 +4.6 (3 notes, all accented), C sharp 5 +4.5 (1), A flat 4 -2.3. Horn 1: C5 +5.1 (4, at CC1 119), F4 +3.8 (3), F sharp 4 -4.6 (1).

Fix (`build/score_config.py`, the c18 accent block; `mix.json` `region_gain_db`):
- Brass shape only: from 0.03 s before the moved note-on, held 0.18 s, back by 0.40 s (c18: 0.06 / 0.22). Amounts unchanged except trumpets and tuba 6 % -> 9 %, Trumpet 3 5 % -> 9 %. No CC1 part on any brass track. Expected +1.0 to +1.5 dB in the first 0.3 s. This is longer than c18 but shorter than c17's 0.15 / 0.45 that Dan called overdone, and c17 also had twice the amount.
- Strings: at printed f (resting under 96) bump +8 / +7 -> +4 on Violins I / II and Violas, +5 on Violoncellos; at ff unchanged; step cap unchanged. Top register (pitch 88 or higher on Violins I): +6 at ff.
- Woodwinds: unchanged amounts; hold 0.06 -> 0.10 s.
- Region gains, "Sus Non Vib MAX" / "Sus MAX": Trumpet 3 C4 +3, B flat 4 -3; Trumpet 2 B4 -4, C sharp 5 -3.5; Horn 1 C5 -4, F4 -3. Range-test first (the counts are small).
- Check with the matched measure above (not with neighbours at other pitches): brass isolated median +1.0 to +1.5, strings' upper quartile under +2.5, no track over +2.

### 3. Pizzicato celli: the unevenness is fixed per pluck and repeatable, so it can be removed pluck by pluck in CC11 (measured)

Where: Violoncellos, bars 51-66, 115-122, 171-186 (62 plucks on "Pizzicato RRx4", velocity 41, CC11 34 throughout).

Peak range per passage 10.9 / 8.4 / 10.4 dB (actor: 11.8 / 7.3 / 11.0). Within one pitch the level follows the round-robin position (counted from the CC16 reset of the passage): C3 reads -53 dBFS at positions 0, 4, 8, 16 and -43 at position 2; B flat 2 reads -48 at positions 10, 18, 22, -40 at 7 and -43 at 21; F2 -45 at 6, 18, 22 and -51 at 4; B2 -50 at positions 1 and 9, -45 / -46 at 3, 7, 15, 19. Between-pitch spread of the medians is 2.2 dB, within-pitch SD 2.4 dB: the per-pitch region gains did their half; one gain per pitch cannot do the other half (C3's gain of +5.8 leaves four plucks 5 dB low and one 5 dB high). Plucks are repeatable to 0.00 dB with the section resets (LEARNINGS c14).

Plucks more than 2.5 dB from their passage median (dB): 220 B flat 2 +6.5, 226 B2 -2.9, 254 B flat 2 +3.8, 260 E flat 3 -4.4, 464 E flat 3 -4.2, 468 C3 -5.8, 472 A3 +2.6, 680 C3 -4.8, 686 C3 +5.4, 692 F2 -2.9, 700 B2 +2.9, 704 C3 -4.7, 709.5 G2 +2.8, 716 B2 +2.9, 718 C3 -5.1, 722 F2 +3.6, 732 F2 +3.6. Other pizzicato tracks for comparison: Double basses 3.7-6.4 dB (within-pitch SD 1.5), Violas p5-p95 7.0 dB (B3 and A flat 3 have a 7.5 dB range), Violins II 7.6 dB (D4 7.6).

Fix:
- `INSTR_POST["note_cc"]`: a CC11 value per listed pluck, set in the rest before it (at least 0.05 s before the note-on) and held to the next pluck: 34 + round(-residual / k). k is not known for the pizzicato row at CC11 34. Measure it on one range (bars 115-122 with the track at CC11 34 and again at 44), then write the 17 values. Velocity stays 41 (the layer step is at 48-56).
- Not recommended: a CC16 reset before every pluck. It would make every pitch one sample (seven immediate same-pitch repeats at 242, 254, 708, 709, 709.5, 722, 734 would play the identical sample), and the basses' resets on eighths failed in Movement I.
- Target: peak range per passage 6 dB or less.

### 4. Bars 91-92 and 277: the unaccented eighth between two accents is half-swallowed on trumpets and tuba (measured); calibration plan for the basses' eighths

Where: qn 361.5, 365.5 (bars 91-92) and 1105.5 (bar 277); Trumpets 1-3, Tuba; the figure is accented dotted quarter, eighth, accented half.

The eighth is played on the sustain row for 79-109 ms (bars 91-92) and 106-142 ms (bar 277), cut short by the 90 ms brass gap in front of a same-pitch note. Peak of the eighth against the accented notes on either side (20 ms frames, fader removed): Trumpet 1 -36 against -30 dBFS, Trumpet 2 -36 against -29 / -31, Trumpet 3 -39 against -32 / -33, Tuba -36 against -31 / -30; at 277 Trumpets -36 / -34 / -38 against -32 / -29 / -32. Trombones (-37 / -38 against -34 to -35), woodwinds and strings are within 3 dB. The trumpet rows need 82-90 ms to come within 3 dB of their body (finding 1), which is the whole note.

Fix:
- Trumpets 1-3 and Tuba at 361.5, 365.5, 1105.5: play the eighth on the double-tongue short row ("Stac DblTng RRx9" on the 1TP KS Master, key 28; on the 2TP / 3TP masters the nearest row is "Marc Shrt DblTng RRx4"; the tuba's short row from its map), velocity 95 (research batch 2: brass shorts 62-95), CC16 reset before bar 91 and before bar 277, keyswitch 0.15 s ahead (short rows take the early keyswitch: LEARNINGS c15). Level by region volume on that row against the neighbouring sustain notes, target 2-3 dB under the accents.
- If the row cannot be loaded within memory: keep the sustain row, start the eighth 0.05 s earlier and take the same-pitch gap down to 0.05 s for these three notes (note 130-140 ms).

Double basses' eighths (bars 199-210, 247-277) are unchanged: separation between strokes on "Stac On Bow RRx9" median -5.7 / -6.2 / -4.8 / -6.0 dB in 792-840 / 984-1056 / 1056-1088 / 1104-1108, with 9 / 12 / 13 / 1 joins under 3 dB (the other strings' repeats read -6 to -10). Whether `row_volume_db` -1.5 acted cannot be read from this render (no unchanged reference). Calibration range, as the c18 report asked, with one addition: Double basses alone, after bar 279 or in pass 2; rows "Stac On Bow RRx9", "Marc Shrt RRx4", "Staccatissimo RRx9", "Spiccato RRx9"; per row a CC16 reset, then nine strokes 1 s apart on A flat 1, C2, D2, F2 at velocity 100, CC11 105, note length 0.08 s; then the same nine on "Stac On Bow RRx9" with `row_volume_db` 0 and -6. Read per stroke: first sample over -60 dB, time to half amplitude, time to peak, peak level. Choose the row whose median half-rise is under 50 ms with the nine samples within 25 ms; the two volume passes say in one step whether the row knob acts (Movement II: it did not; region volumes do).

### 5. Two faults from c18, causes found (measured)

- Horn 3, bars 27-38: the +3.5 dB is the held unison level. `score_to_parts.py` line 6086 sets `vol_parts.rule = "uni_hold"` when `UNI_BOOST_HOLD_QN` is set, and `VOL_RULE_OFF` is keyed `"uni_boost"`, so it matched nothing. The envelope reads +3.5 dB from qn 104.5 to 151.5 (47 qn, twelve bars, well past the unison). Fix: `VOL_RULE_OFF["Horn 3"] = {"uni_hold": [(103.0, 152.0)]}` (or accept both tags in `dropped()`), and if the level is wanted, give it as `cc_scale` on CC11 (exact on brass). Note for B: Horn 3 at -33.8 dBFS stands 13-16 dB over Horns 1, 2 and 4 (-46.7, -47.8, -50.1) at the same CC11 100 / CC1 108 as Horn 4; 3.5 dB of that is the row, the rest is not the fader.
- Muted Trumpet 1, bar 182: the G5 at qn 724 reads -43.2 dBFS (fader removed) against D5 -48.3 one quarter before and F5 -48.7 one quarter after, with CC1 56 on the G5 and 59 on the D5 before it. CC1 is not higher on the loud note, so the excess is the G5 sample of "Mute Sus" (and velocity 73, the highest of the solo). Fix: region gain "Mute Sus" G5 -4 dB, remove the +4 CC1 units on G4 / A flat 4 as ruled, and leave the CC1 ceiling (lowering it to 52 would also take 2-3 dB off the D5 and F5, which are in line).
- For the record, the muted solo's slurs (680-694, 712-728) are on a sustain row with joins of 0 to -5.8 dB (median -1.9); the cor anglais that doubles it reads median -1.4 on "Leg Slur MAX". The two lines match; no change.

### 6. Checked and in order (measured)

- No chord is sent to a legato row on any wind or brass track, and no pair of legato notes overlaps by more than 150 ms.
- No note is held longer than 6.5 s (the longest: Horn 4 at 168, 6.5 s; Horn 2 at 152, 5.8 s; Clarinet 2 at 184 and Contrabassoon at 568, 5.6 s), and no string note over 5.2 s, so the 3.95 s loop has nothing to pulse on outside the timpani rolls (not measured).
- Repeated notes outside the basses separate by 6 dB or more on the stems, except Trombone 1 in 984-1056 (three repeats, -2.7 to -2.9 dB, gap 77 ms; give it the 90 ms gap of the trumpets) and Violas at 361.5-362 / 365.5-366 (-2.0 / -2.4 dB, gap 54 ms; gap 0.08 s).

Do not touch: the string accent fronts at ff (shape 0.03 / 0.06 / 0.22 and +10 units); the oboe and bass region gains of c18; the pizzicato basses (3.7-6.4 dB); the legato rows and overlaps of the open trumpet solo (bars 51-66) and the cor anglais; the printed breaths in the chorale; the 0.04 s lead of "Stac On Bow RRx9" until the calibration range has run; the no-split limit (nothing over 6.5 s).
