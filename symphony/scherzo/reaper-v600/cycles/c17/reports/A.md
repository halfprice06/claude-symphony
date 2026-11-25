# Cycle 17, critic A: articulation and phrasing (on the c16 render)

Positions are score quarter notes (qn); bar b starts at qn 3(b-1). Levels are mean-square dB on the stems of `cycles/c16/render/` (after the stem fix), read on `build/parts.json` (identical to `cycles/c16/build_fix/parts.json`); comparisons use `cycles/c15/render/` with `cycles/c15/build_render/parts.json`. Join timing is the actor's measure S (`cycles/c16/records/S_c16.json`, `S_PA.json`, `cycles/c15/records/S_c15.json`). "Measured" = a number from those files; "inferred" = reasoned, not tested. Nobody heard the audio. Every fix is on the instrument side (CC11, CC1, velocity, row, region gain, note length, lead, bow-change position). None is a volume-envelope move.

Not measured this cycle (data unchanged since c14): harp, pizzicato and arco changes, sul A, con sordino, breath marks, tenuto lengths, timpani (critic B has the stroke fronts and the bar 332 roll), loop pulsing on brass and winds.

## Manual notes (May 2021 HO manual, PDF pages 108-113, read in full)

| Manual | Where it applies here | Does the render follow it |
|---|---|---|
| p.108: "Flute 2" is a second player with its own samples; unisons do not collapse | Flute 1 and 2 in unison in the tuttis (bars 105-120, 305-320) | Yes: Flute 2 plays "FL2 KS Master". But the two patches' rows are levelled differently: Flute 2's accented half note is 4.7 dB under its own slurred resolution, Flute 1's is 8.0 dB over (finding 2) |
| p.109: Sustain patches play all dynamic layers and crossfade them by controller (CC11 in Opus; the Mod Wheel text is Play-era) | every "Sus MAX" note; the accents, which are CC11 bumps on that row | Yes. Measured response of the bump: 0.06-0.33 dB per CC11 unit, different per track and dynamic (finding 2 table) |
| p.109: Sus Expressive ("slower attack and a gently increasing vibrato") | Oboe 1 espress. (bars 185-196), the codetta's dolce lines (225-236) | Not used (MANUAL-GAPS #8, c10 tried the slower legato velocity instead). No change asked |
| p.109-110: Legato Repetitions RRx4: a sustain plus a short re-tongued attack, for repeated notes inside a sustained phrase | slurred or tenuto repeats: Clarinet 2 159 and 390, Clarinet 1 402, the bassoons' pp repeats of bars 143-147 | Not used. The clarinets already play "Leg Slur Rep" (p.112), which re-tongues repeats that have no gap; their three weak repeats have a 65 ms gap, which defeats that row (finding 5) |
| p.110: short articulations have no release trails; "hold the MIDI notes long enough to hear the natural reverberation" | every "Stac DblTng RRx9" and string short note | Scherzo: MIDI length 114 ms (the whole eighth) on every track and section: followed. Coda build 329-336 (eighth = 104 ms): the same unison figure is 52 ms on Violins I and Flute 1, 55 on celli, 62 on Violins II, 78 on violas and cor anglais (measured in parts.json). Inferred: make them one length, at least 0.08 s (`short_strokes` / the staccato length rule) |
| p.110: Marcato = short note with a strong accent; Shorts MOD SPEED | accents | Not used, correctly (Dan: weight, not bite). 2-5 kHz share of the first 80 ms against the body on accented notes: -3.5 to +1.0 dB on every track (no bite) |
| p.112: a woodwind slur needs "no significant gap" and an interval of at most an octave | all woodwind legato rows | Yes: 0 joins over an octave on nine woodwind tracks; connected pairs overlap 45 ms (median). 11-14 ms gaps exist on six tracks, on tongued notes |
| p.112: legato rows are monophonic (CC22 0-63 turns it off) | chords on legato rows | Followed (not re-checked) |
| p.112: Legato Slur Repetitions: repeats "without space between the notes" use a re-tongued sample | Clarinet 1 and 2 (whole track on "Leg Slur Rep") | Partly: `REP_GAP_FLOOR_S` wind 0.065 now puts a gap before every clarinet repeat, so the row's own re-tongue sample is never used (finding 5) |
| KS Master row lists (p.113, ks_maps): "Sus Accent MAX" is in every woodwind and horn KS Master | printed accents | Not used and not costed anywhere in the loop files. A candidate only if the CC shape of finding 2 fails; it would need a 2-5 kHz check first |

## Findings

### 1. Eight joins of the second idea speak 128-151 ms late: the c16 lead cap cut their leads to 94 ms (measured)

Where: the figure "eighth, then a long slurred note" of the second idea (hemiola, espress.): Violins I 146 (bar 49) and 374 (bar 125); Violins II 134 (bar 45), 146, 374, 840 (bar 281); celli 842 and 144. An eighth lasts 114 ms here, so these notes arrive more than an eighth late.

Evidence (S = lateness of the new pitch, ms; lead = note-on before the score onset, ms):

| join | c15 S / lead | c16 S / lead | `lead_set.json` asked |
|---|---|---|---|
| Violins I 146 | +7 / 134 | +150 / 94 | 210 |
| Violins I 374 | +34 / 124 | +144 / 94 | 215 |
| Violins II 134 | +77 / 173 | +144 / 94 | 230 |
| Violins II 146 | +72 / 160 | +136 / 94 | 220 |
| Violins II 374 | +98 / 162 | +151 / 94 | 245 |
| Violins II 840 | +66 / 134 | +128 / 94 | 195 |
| Violoncellos 842 | +73 / 159 | +140 / 94 | 205 |
| Violoncellos 144 | - / 34 | +71 / 94 | 155 |

Also capped: Violins I 591 and 597 (112 ms, S +44 and +109), celli 536 (112, +41), violas 726 (127, +79), Violins II 387 and 855 (207, +51), celli 768 (207, +55). Violins I's five refit joins read a median of +109 ms.

Cause: `tools/score_to_parts.py`, the `LEAD_SET_AT` block (and the `ROW_CHANGE_LEAD_S` block above it): `want_ = min(want_, (q - p_["qn"]) - lead_qn(q, ROW_CHANGE_LEAD_GAP_S))`. The cap is the previous note's score slot less 20 ms and ignores that the previous note itself starts early. At 145.5 the eighth now starts 235 ms early (row-change lead), so the note at 146 could start up to 114 + 235 ms after it; the cap allows 94 ms. c15 had 124-173 ms there.

Fix: in both blocks cap against the previous note's moved note-on: `want_ <= (q - p_["qn"]) + shift.get(id(p_), 0.0) - lead_qn(q, PREV_MIN_SOUND_S)` with a new generic `PREV_MIN_SOUND_S = 0.06` (the previous note sounds at least 60 ms alone). With that every value in `lead_set.json` above is reached (146: room 289 ms for 210). No new measurements are needed for these joins: the set values come from the pass. Target: no join of these four tracks over 60 ms late (c16: Violins I 3, Violins II 4, violas 2, celli 4).

### 2. Accents: the per-track medians mix two cases. Accents with plain neighbours are already over the limit on eight tracks (+3.1 median, 75 of 144 over +3 dB); the other 130 stand in runs where every note is accented and read 0 by construction. Most of the excess is row and pitch level, not the CC bump (measured)

Evidence 1, the statistic. Of the 274 measurable accents, 130 have an accented neighbour (the hemiolas of bars 101-104 and 301-304, bars 337-338). Their "level over the neighbours" is +0.3 dB (median), which says nothing about weight. The 144 with plain neighbours:

| track | isolated n | median | p90 | over +3 dB | in runs n | median |
|---|---|---|---|---|---|---|
| Flute 1 | 18 | +4.3 | +8.9 | 15 | 14 | -0.3 |
| Flute 2 | 7 | -0.8 | +3.3 | 1 | 0 | |
| Oboe 1 | 22 | +1.2 | +3.7 | 7 | 2 | -1.3 |
| Cor anglais | 13 | +3.1 | +6.3 | 10 | 15 | +0.8 |
| Clarinet 1 | 5 | +5.0 | +8.0 | 4 | 4 | +2.2 |
| Clarinet 2 | 10 | +5.2 | +6.4 | 6 | 6 | +0.6 |
| Bassoon 1 | 3 | +4.0 | +6.0 | 2 | 3 | -0.1 |
| Violins I | 28 | +3.1 | +5.0 | 15 | 17 | +0.3 |
| Violins II | 18 | +2.6 | +7.4 | 7 | 16 | +0.4 |
| Violas | 12 | +2.2 | +5.5 | 6 | 16 | -0.4 |
| Violoncellos | 6 | +1.3 | +2.7 | 1 | 15 | +0.5 |
| Double basses | 0 | | | | 15 | +0.4 |

So "strings at ff, violas and basses have almost no accent" is the run dilution: Violins I's isolated ff accents read +1.6, Violins II's +2.5. Do not raise the string bump.

Evidence 2, what the CC bump adds. Same accents in c15 (no accent CC) and c16, the neighbours' own change subtracted:

| track, dynamic | c15 (no bump) | bump adds | c16 | dB per CC11 unit |
|---|---|---|---|---|
| Flute 1 p-mp / mf-f / ff | +1.2 / +4.8 / +5.5 | +3.4 / -0.4 / +1.5 | +3.4 / +4.3 / +7.9 | 0.28 / 0 / 0.15 |
| Flute 2 ff | -4.8 | +2.3 | -0.5 | 0.23 |
| Oboe 1 p-mp / mf-f / ff | -5.1 / -3.0 / +1.6 | +1.8 / +3.4 / +2.1 | +0.5 / -0.3 / +3.3 | 0.15 / 0.28 / 0.21 |
| Cor anglais mf-f / ff | +2.6 / +2.4 | +0.7 / +0.7 | +2.7 / +3.1 | 0.06 |
| Clarinet 1 (all) | +3.8 | +1.6 | +5.0 | 0.13 |
| Clarinet 2 ff | +4.0 | +0.6 | +4.6 | 0.06 |
| Violins I p-mp / mf-f / ff | +2.1 / +0.9 / +0.4 | +1.1 / +2.1 / +1.4 | +3.6 / +2.8 / +1.6 | 0.10 / 0.17 / 0.07 |
| Violins II p-mp / mf-f / ff | -2.3 / +3.4 / +1.1 | +4.2 / +1.8 / +1.1 | +2.5 / +5.0 / +2.5 | 0.30 / 0.14 / 0.06 |
| Violas p-mp / mf-f | -4.8 / +1.6 | +3.0 / +2.9 | -2.0 / +4.5 | 0.25 / 0.23 |
| Violoncellos p-mp | -2.9 | +4.0 | +1.3 | 0.33 |

The bump itself adds +0.6 to +4.2 dB. Flute 1, Clarinet 1, Clarinet 2 and the cor anglais were already +2.4 to +5.5 dB over their neighbours without any bump; Flute 2, Oboe 1 and the violas at p were 3-5 dB under. That part is row and pitch level:
- Flute 1 "Sus MAX" at ff (CC11 100 or more, notes of a quarter or longer): G6 -24.9 dB, E6 -26.2, A6 -31.9, C6 -34.7; its "Leg Slur MAX" on G6 -29.8. The accents on G6 (315, 351, 999) read +9.4, +9.5, +8.6; on C6 (345) +4.1.
- Clarinet 2 "Leg Slur Rep" at ff: A4 -26.7, C5 -29.0, G4 -34.6, F sharp 4 -32.4. Accents on A4 / C5 (327, 345, 927, 945): +4.6 to +6.8; on G4 (315, 351, 915, 951): -1.7 to -2.1.
- Clarinet 1 C sharp 6 at ff -20.4 against -31.6 / -31.9 on E flat 5 / A5 (n 2; qn 897 reads +9.0).
- Flute 2: accent +4.0 over the staccato before it and -4.7 under the slurred note after it ("Leg Slur MAX" over "Sus MAX" at ff +2.7, n 14).
- Oboe 1 at p to f: accent 2.1-2.9 dB under the staccato before it (c16 trimmed the staccato row only from velocity 75).
- Violas at p-mp: accent 5.5 dB under the "Stac RRx9" note before it (723: -6.5, 978: -3.9).
- Violins I at p-mp: the appoggiaturas on "Sus Marc LITE" (51, 285, 771) read +5.3 to +7.0; that row has its own accent and gets the bump on top.

Evidence 3, the shape. Median level over the neighbours by time after the onset: 0-60 ms -1.9 to +0.6 on 12 of 15 tracks, 60-300 ms +1.0 to +6.4. Inside the accented note, level at 30-180 ms against 250-400 ms: isolated accents -3.1 to +2.1 dB, plain sustained notes of the same length -2.9 to +0.7. The accented note has the same shape as a plain note: it is a louder note, not a weighted start. On the strings the bump covers the whole half note and the start of the next: Violins I 327: CC11 127 from qn 326.55 (the moved note-on, 100 ms before the beat) to 327.75, back at 328.98, which is 0.55 s for a 0.45 s note; the configured 0.15 + 0.3 s is counted from the score onset, the lead is added in front.

Summed accents (staves accented together, plain neighbours): woodwind sum +3.3 (3-4 staves) and +3.4 (5 or more), string sum +2.3 and +3.9; master +1.5 to +2.9 median, p90 +3.6 to +5.8. Bar 300 (qn 897, 16 staves): master +5.4.

Fix (`build/score_config.py`, `tools/score_to_parts.py`, `build/mix.json`):
- Report and tune on isolated accents only; for runs report the within-note measure (30-180 ms over 250-400 ms).
- Shape, all tracks: `ACCENT_CC` `hold_s` 0.06, `rel_s` 0.20, both counted from the later of the moved note-on and (score onset - 0.03 s), so the tail of the note is back on its resting CC. Target inside the note: first 180 ms +1.5 to +2.5 dB over 250-400 ms.
- Amounts, as a new per-track override `ACCENT_CC_BY = {track: {"add": .., "add_loud": ..}}` (bump adds about 1.5 dB less the c15 baseline, by the measured dB per unit): Flute 1 add 2, add_loud 0; Cor anglais 0 / 0; Clarinet 1 0 / 0; Clarinet 2 12 / 0; Bassoon 1 12 / 0; Oboe 1 add 12, add_loud 4; Flute 2 12 / 10 (unchanged); Violins I add 6, add_loud 20; Violins II add 8, add_loud 14; Violas add 5; Violoncellos, Double basses unchanged. No CC bump on a note whose row is "Sus Marc LITE".
- 9 or more staves accented together: scale the bump by 0.75, 16 or more by 0.6 (finale c18), which covers qn 897.
- Baselines, in `region_gain_db` (the c15 / c16 mechanism): Flute 1 "Sus MAX" ff layer E6 and G6 -5; Flute 2 "Sus MAX" f and ff layers +3; Clarinet 2 "Leg Slur Rep" A4 -4 and G4 +2 at the ff layer; Oboe 1 "Stac DblTng RRx9" velocity under 75 -3; Violas "Stac RRx9" p layer -4. Clarinet 1 C sharp 6 and the cor anglais pitches (Sus Max at ff: B4 -37.6, G4 -35.5, C5 -34.9, A4 -31.6, F sharp 4 -30.5) go to critic B's per-pitch fit; I measured them on post-fader stems, so the passage roles are in these numbers (inferred that the pitch is the cause).
- Pass: isolated accents median +1.0 to +2.0 per track, p90 under +3.5, none of the 15 tracks over +3.

### 3. The last G sharp (bars 364-376): the five bow changes follow each other every 1.9 s, and each instance needs 1.0-2.2 s to come back, so one of the two is always down (measured)

Evidence: the note sounds from 263.0 to 277.9 s. Bow changes at 265.0 (solo), 267.0 (Violins I), 268.9 (solo), 270.7 (Violins I), 272.6 s (solo). After its own change each instance is 6-18 dB down for 0.4 s and back within 2 dB only after 2.2, 1.45, 1.1, 1.0 and 1.1 s. The holding instance's CC11 lift (22 to 29) gives +3.0, +3.7 and +3.3 dB at 1103.8, 1110.66 and 1116.3, but +0.9 dB at 1096.14 (Violins I is 2 s into its first bow) and +0.8 dB at 1121.0 (Violins I changed 1.9 s earlier and is still at -53 to -54 against -50): that is the 6.5 dB dip. The lift starts 0.02-0.08 qn after the other's change (1103.89 for 1103.814) and takes 0.15 s, so the hole comes first: the sum is 3 dB down for 0.2 s even where the lift works. Sum, 0.1 s frames over 1091-1126: standard deviation 1.4 dB, range 7.2 dB (c14 with fader fills 1.3 / 6.1; c15 3.4 / 17.3); autocorrelation at 3.9 s 0.31.

Fix (`build/score_config.py`, `HELD_DOUBLE` and `REBOW_AT`):
- Three changes instead of five, 3.0 s apart, so the holder is always at least 3 s past its own change: solo at 266.0 s (qn about 1100.0), Violins I at 269.0 s (about 1111.0), solo at 272.0 s (about 1119.5, before bar 375); none later. `REBOW_AT` Violins I [1111.0]; `rebow_at` solo [1100.0, 1119.5]. Take the exact qn from the tempo map.
- `lift`: start 0.3 s before the other instance's change and be at +7 on it (a new first element, lead 0.3 s); hold and release as now.
- The pieces become 6.0-8.9 s, so each passes the 3.95 s loop point once or twice. Inferred that two offset instances hide it; check after the render: no 0.1 s frame of the two-stem sum more than 3 dB under the median, no 40 ms dip over 4 dB, autocorrelation at 3.95 s under 0.3.

### 4. Celli, bars 169-184: the "17 dB swell" at qn 504 is the slur into the second note, which starts 265 ms early; and the refit left 13 of 30 joins outside 25 ms (measured; the remedies partly inferred)

Evidence, 504: the G sharp 3 enters at -50 dB on the beat and sits at -42 to -43 from 50 to 200 ms. The A3 of qn 506 has its note-on 265 ms before its beat, which is 0.26 s after the G sharp's beat (a half note is 0.526 s at quarter 228). From there the stem rises to -36 (300-350 ms) and -33 dB (400 ms), then the A3 settles at -41 to -43. The peak is the slur transition, 8-9 dB over both bodies. Peak in c14 / c15 / c16: -37 / -34 / -33 dB. Removing the +10 CC11 at 503-506 changed nothing because the burst is in the transition sample. Other cello slurs with a burst of 4 dB or more: 789 (+6.1), 520, 516, 834, 163, 374 (7 of 105; median +0.4, so it is not general).

Evidence, joins: the count outside 25 ms rose 28 to 43 for two reasons.
- 19 joins that nobody touched (same lead in c15, on the pass and in c16; reading identical on pass and render to 1 ms) moved from about 0 to +25..+47 ms, 11 of them in the tune itself (528-546: +26 to +32, c15 -10 to +9). Violins I, which double the tune an octave higher from 528, did not move (-20 to +22, as in c15). The notes did not move; the reading did (inferred: the envelope guard's snaps changed where the level onset is read, as Movement II c56 found). Not a fault to fix by leads.
- Of the 30 refit joins 17 are inside 25 ms now. Six did not move because of the cap of finding 1 or a floor (144, 536, 768, 842; 566.5 and 571.5 stay at -46 and -38 with leads of 90 and 100 ms). Five jumped across zero: 321 (-86 to +44), 921 (-78 to +42), 933 (-63 to +37), 570 (-61 to +33), 350 (+44 to -36). On those the reading has two states (the earlier of two detectors), so one reading is not a slope.

Fix:
- `build/lead_set.json` Violoncellos: 321 0.17, 921 0.175, 933 0.18 (midway between the two leads that read -86..-63 and +37..+44); 570 0.275 and 350 0.255 (the c15 leads, which read -1 and +1); 526 0.27. Refit thresholds: keep 40 ms; do not refit the 19 joins that read 25-47 ms.
- 504-506: `build/lead_set.json` Violoncellos 506 0.24 (S is -25 ms now, so the slur can start 25 ms later). For the burst itself, in this order: (a) `CC11_ADD_SPANS` Violoncellos (504.95, 505.25, 0, -14), (505.25, 505.6, -14, 0): at CC11 56-62 the celli give 0.33 dB per unit, so about -4.5 dB at the transition, inside Opus, with the hall tail intact; the same at 789. (b) If the patch file shows the slur transitions as their own groups in "Leg Slur MAX", a `region_gain_db` of -4 on those groups' p and mp layers is the general form (inferred; read the patch first). Pass: no 50 ms frame between 504 and 506 more than 4 dB over the following body.

### 5. Repeats after the gap floor: brass and woodwinds separate; what is left is Horn 1's "Port Lng" repeats, three clarinet repeats, and the strings' printed pp repeats (measured)

Evidence (peak of the second note's first 120 ms over the lowest 15 ms frame before it):
- Brass: Horn 1 median 10.4 dB (c15 5.9), trumpets at 1008-1012 9.3 and 6.4 (c15 0.0-0.1), trombones and tuba 5.6-8.3; none under 3 dB except Horn 1 630, 633, 663 (1.2-1.4 dB, on "Port Lng" with a 90 ms gap), Horn 2 999 (1.9) and 1011 (2.0), Horn 3 219 (1.9) and 603 (1.3).
- Woodwinds: sustained repeats median 6.2-11.1 dB; under 2 dB only Clarinet 2 159 (0.4) and 390 (1.2), Clarinet 1 402 (1.7), Oboe 1 165 (1.9). All four have the 65 ms floor gap.
- Staccato pairs of the theme head: strings 10.1-12.0 dB, flutes 15.8-16.4, oboe 11.6, cor anglais 15.5, trumpets 8.6-11.3. Good.
- Strings, printed repeats of long notes at pp-p with an 8 ms gap (`rep_rebows`): violas 675, 687, 1041, 1047, 1053, 1080 (0.5-2.8 dB), celli 609 (1.9), 1074 (1.1), basses 609, 1074, 1077, 1080 (1.5-2.8). With an 8 ms gap: median 2.7-3.6 dB; with 60-90 ms: 6.4-8.3 dB.

Fix (`build/score_config.py`): Horn 1 630, 633, 663 on "Sus MAX" through `ART_AT` (the row its other tenuto repeats use; they separate by 5.3 dB median). Clarinets: exempt "Leg Slur Rep" from `REP_GAP_FLOOR_S` for repeats under a slur, so the row's own re-tongue sample plays (manual p.112: it needs the notes "without space"); keep the floor for tongued repeats (inferred; check the three notes after the render). Strings: gap of min(0.05 s, 15 % of the first note) on the printed repeats listed in `rep_rebows` (not on automatic re-bows), new generic `REP_REBOW_GAP_S = 0.05`. Target 3-6 dB.

### 6. Rows of one line still 3-9 dB apart, and the measured results of c16's unmeasured item 10 (measured)

Row pairs (adjacent notes on different rows, CC11 within 8; median, n), `meas16.py rows` on the final render, which c16 did not run:

| track | pair | dynamic | dB |
|---|---|---|---|
| Flute 1 | "Leg Slur MAX" over "Stac DblTng RRx9" | ff / mf-f / p | +6.1 (16) / +3.7 (6) / +5.4 (5) |
| Flute 2 | "Leg Slur MAX" over "Stac DblTng RRx9" | ff | +6.3 (14) |
| Oboe 1 | "Leg Slur MAX" over "Stac DblTng RRx9" | ff / p | +3.5 (12) / +5.6 (4) |
| Cor anglais | "Leg Slur MAX" over "Stac DblTng RRx9" | ff / mf-f | +3.8 (13) / +8.9 (3) |
| Violins I | "Stac RRx14" over "Sus MAX" | ff | +5.8 (14) |
| Violins II | "Spiccato RRx9" over "Sus MAX" / over "Stac RRx9" | ff / mf-f | +5.9 (13) / +6.8 (6) |
| Violas | "Leg Slur MAX" against "Sus MAX" | mf-f / p | -2.8 (29) / +3.1 (19) |
| Violoncellos | "Stac RRx9" against "Sus MAX" | mf-f / p | -5.3 (3) / +6.8 (3) |

The flute and cor anglais pairs are the slurred resolution followed by the next head's staccato: the staccato row is 4-6 dB soft against the legato row on three woodwinds. Violins I and II at ff are the reverse (short row 6 dB hot against the sustain), which is why their ff accents after a staccato read low.

Fix (`build/mix.json` `region_gain_db`, `row_dyn_db`): Flute 1 "Stac DblTng RRx9" all velocities +3 more (velocity 75 up is at +4 now); Flute 2 "Stac DblTng RRx9" -4 back to -1; Cor anglais "Stac DblTng RRx9" +3; Violins I "Stac RRx14" velocity 90 up -3; Violins II "Spiccato RRx9" velocity 90 up -4. Then re-run the row table and the accent table of finding 2 (the two interact: do the row gains first).

Item 10 of c16, measured:
- Violas div 1044: the -6 dB point is at -20 ms (c15 +10): fixed. Its join at 1047 bumps +7.5 dB, and the solo violin's join at 1065 +7.9 dB (both exposed, bars 349-356; unchanged from c15). Lower the two targets' velocity (90 and 82) to 64 (`NOTE_VEL_AT` or the legato velocity span; upper strings gain 0.45-0.85 dB per 10).
- Celli 506 / 764 / 800: bumps +0.5 / +1.6 / +1.7 dB (c15 +1.1 / -0.8 / +2.4): fine. Celli 794: front +1.8 over the body: fine. Celli 542 and 570: holes of 8.1 and 10.5 dB at the join (570: c14 7.9, c15 9.8): open; 570 gets its c15 lead back in finding 4.
- Bassoon 1 353 / 953 and Clarinet 1 576: the CC11 lift of 8 did nothing (front under body -3.6 to -3.5, -2.9 to -2.7, -4.1 to -3.8): at ff the bassoon's CC11 response is 0 dB per unit. Remove the three `ACCENT_CC_AT` entries. Clarinet 1 576 is a join hole of 11.4 dB; the same shape at 382 (11.9) and 850 (10.6), Oboe 1 380 (11.2) and 848 (10.8), Flute 1 154 (11.0). For these six: overlap 45 ms to 80 ms on the join (legato overlap in seconds, Movement I c58) and re-measure.

## Do not touch

Brass re-tongue gaps (`REP_GAP_FLOOR_S` brass 0.09, Horn 1 gap 0.065); the staccato pairs of the theme head on every track; `AUTO_REBOW_SKIP` on bars 1-8 and the harmonic (one bow, no dip); the two-instance G sharp as a method; `CC11_REST_MAP` and the string `add_loud` 20 at ff; `ACCENT_SUS_MIN_CC`; the 2-5 kHz fronts (no bite anywhere); the 17 cello and 14 viola refit leads that now read inside 25 ms; woodwind legato overlaps and the octave rule; Flute 2 on its own patch; `note_move_guard`.
