# Critic A, cycle 49: articulation and phrasing

Render under review: `cycles/c48/render/` (master and stems), with `cycles/c48/rendered_build/parts.json`,
`build/score_config.py` and `tools/`. Positions are score quarter notes (qn) on the c46 tempo map unless marked "s".
"Printed onset" is the score onset; "lead" is how far the note-on sits before it. Every judgement is marked
**measured** or **inferred**. Three findings; the rest of the lens was measured and passed (list at the end).

## Manual notes

The reading schedule has no row for cycle 49. Pages consulted for the findings (Opus Edition User Manual 2021):

| Page | Content | Used in |
|---|---|---|
| p.91 | Détaché: separated notes, each with a clear attack whatever precedes it. A row named "RR" holds two recorded takes per note, played in turn. | Finding 1 (the Violas' Detache row, keyswitch 30) |
| p.92 | Flautando exists only in the 2nd Violins. For other sections the manual suggests Sustain played pp with the Mod Wheel fully down as a similar sound. | Finding 3 |
| p.143, p.145 | Round Robin Reset: Opus remembers which take comes next; the manual lists CC36 (any value) and advises a reset at the start and "at important positions throughout the sequence". | Finding 1. DIGEST.md: this machine's Opus resets on the controller in Preferences (`RoundRobinResetCC: 16`); a CC36 inside the music did not reset a Stac RRx9 cycle (Movement I c14). |

## Findings

### 1. Violas, sotto voce portato eighths, bars 48-51 (qn 152.5-167.5): the two Detache takes changed places between c47 and c48, so the fitted leads now sit on the wrong takes

**Where.** Violas, 15 off-beat eighths on the Detache row (`ART_SPANS["Violas"]`, 152.5-168.0), pp. Worst in bar 51
(E flat 4 at 164.5, 165.5, 166.5, 167.5; 188.2-193.0 s).

**What is wrong (measured).** The data in qn 152-168 is identical in the c47 and c48 `rendered_build/parts.json`,
and the c46 and c47 stems are identical there. In c48 every pitch plays the other take of its pair. The per-note leads
in `build/entry_leads.json` were fitted to the c47 order (a long lead on the slow take, a short lead on the fast one),
so in c48 the fast take gets the long lead and the slow take the short one.

Stem envelope, 30 ms window, ms relative to the printed onset; "length" is the time between the -10 dB points:

| qn | pitch | lead | c47 t(-6 dB) | c47 peak | c47 length | c48 t(-6 dB) | c48 peak | c48 length |
|---|---|---|---|---|---|---|---|---|
| 152.5 | A3 | 290 | 0 | +170 | 470 | -10 | +250 | 830 |
| 153.5 | A3 | 280 | +10 | +260 | 625 | -150 | +185 | 490 |
| 154.5 | A3 | 290 | 0 | +170 | 490 | -95 | +250 | 680 |
| 156.5 | A3 | 280 | +10 | +260 | 625 | -150 | +185 | 490 |
| 157.5 | A3 | 290 | 0 | +175 | 490 | -95 | +255 | 695 |
| 158.5 | B3 | 120 | -40 | +215 | 630 | -60 | +145 | 655 |
| 159.5 | A flat 3 | 120 | +30 | +295 | 625 | +15 | +170 | 645 |
| 160.5 | A3 | 280 | +10 | +260 | 640 | -150 | +185 | 710 |
| 161.5 | A3 | 290 | 0 | +180 | 490 | -95 | +245 | 675 |
| 162.5 | D4 | 120 | -30 | +220 | 690 | -65 | +95 | 715 |
| 163.5 | B3 | 120 | -55 | +150 | 720 | -40 | +215 | 705 |
| 164.5 | E flat 4 | 300 | -135 | +140 | 695 | -185 | -130 | 685 |
| 165.5 | E flat 4 | 120 | -5 | +50 | 525 | +30 | +320 | 550 |
| 166.5 | E flat 4 | 300 | -135 | +135 | 705 | -190 | -125 | 725 |
| 167.5 | E flat 4 | 120 | -5 | +55 | 580 | +30 | +315 | 860 |

- E flat 4: one take peaks about 170 ms after its note-on, the other about 440 ms. c47 peaks at +140 / +50 / +135 /
  +55 ms; c48 at -130 / +320 / -125 / +315 ms. The printed spacing of these four notes is 1.13, 1.15, 1.26 s. The peaks
  are 1.04, 1.24, 1.18 s apart in c47 and **1.58, 0.71, 1.70 s** apart in c48.
- All 15 notes: t(-6 dB) median 0 ms (SD 49) in c47, -95 ms (SD 73) in c48; t(-3 dB) SD 36 ms in c47, 104 ms in c48
  (range -160 to +285 ms). `tools/pcx.py` attack centre: median -64 ms (SD 41) in c47, -124 ms (SD 69) in c48.
- The first note (152.5) sounds for 830 ms in c48 (470 ms in c47); an eighth is 556-661 ms there.
- Audibility: in bar 51 the Violas stem is the only source in the E flat 4 fundamental band (296-327 Hz): Violas
  -57.4 dB, next stem (Double basses) -76.3 dB. Whole-band levels in bar 51: Master -39.1, Cor anglais -40.8,
  Violins II -47.1, Double basses -47.7, Violoncellos -49.0, Violas -54.1 dB.
- `cycles/c48/state_check.txt` reported it ("timing run Violas: qn 156.50-168.00, 6 notes ... pcX median -40 ms";
  156.5 -106 ms, 160.5 +51, 164.5 -32, 166.5 -49, 167.5 +31). `cycles/c48/CHANGES.md` does not mention it. The tool's
  own text calls timing runs informational, which is right for unfitted rows and wrong for this one.

**Cause (inferred).** All five pitches changed take at once, including A flat 3 and D4, which are played once each.
A per-note counter with no reset would also have changed those two between the c46 and c47 full renders, and those
stems are identical. So one event before bar 48 shifted the take order of the whole instance. The c48 Violas data before bar 48 differs from
c47 in one place: the note at 148 became a fresh Sus MAX stroke with a new keyswitch at 147.93 (it was a slur
transition), and the build was `--midi-only`. Two range renders of qn 143-153 also ran before the full render; each
plays the first Detache note without passing the pre-roll reset at qn 0.1. I cannot separate these causes without
REAPER. Either way, an edit earlier in the Violas part can swap the takes again.

**Fix.**
1. `tools/build_reaper.py`, `item_lua()`, the lane tuple at line 886: send the in-music reset lane on the controller
   Opus is set to, `(RR_RESET_CC, tr.get("cc36", []))` instead of `(36, tr.get("cc36", []))`. No track in the c48
   `parts.json` has a point in that lane, so nothing else changes (measured).
2. `tools/score_to_parts.py`, line 5077 (where `cc36` is built from `rr_start` notes): append the points of a new
   table, default `RR_RESET_AT = {}`, and set `RR_RESET_AT = {"Violas": [152.06]}` in `build/score_config.py`. Slot:
   the Sus MAX note ends at 152.0 (174.354 s), the Detache keyswitch is at 152.125 (174.499 s), the first Detache
   note-on at 152.249.
3. Test under the lock before the full render, because a mid-score reset on CC16 has not been tried (only CC36 was,
   Movement I c14): range-render qn 150-160 twice in a row. That range holds 7 Detache notes (5 of them A3), an odd
   count. If the two Violas stems match note for note, the reset works.
4. If it works: after the full render, re-fit the nine Violas entries of `build/entry_leads.json` (152.5-166.5) on
   that render to the c47 targets (peak +50 to +260 ms, t(-6 dB) within about ±50 ms of the group median).
5. If it does not work: drop step 2 and fit the leads to the c48 order. For E flat 4 that is: remove `"164.5": 0.18`
   and `"166.5": 0.18`, add `"165.5": 0.18` and `"167.5": 0.18` (expected peaks +50 and +140 ms, from the c47
   measurements of the same takes with those leads). The A3 entries differ by 0.01 s and the B3 notes have none, so
   they stay.
6. `tools/state_check.py`: for a row with two takes (Detache) print a "take swap" line when two notes of the same
   pitch inside a timing run moved by more than `--ms` in opposite directions (here A3 156.5 -106 ms against 160.5
   +51 ms, E flat 4 164.5 -32 and 166.5 -49 against 167.5 +31). The actor then swaps or re-fits in the same cycle.

**Pass.** The four E flat 4 peaks within 100 ms of each other relative to their printed onsets; t(-3 dB) SD at or
under 40 ms over the 15 notes; no Violas timing run in qn 152-168 in the next state check.

### 2. Double basses, pedal G sharp 1, bars 84-85 (qn 278.35-282.17, 318.24-322.65 s): the level swings 12-13 dB in the last 2 s of a 4.4 s piece, and the master moves 5.9 dB with it

**Where.** Double basses, Sus MAX, velocity 38, CC11 20-22, no printed dynamic change. The same passage on
Violoncellos div (the 4 soli pedal, bars 83-86) to a smaller degree.

**What is wrong (measured).** 50 ms envelope of the stem: -50.5 ±1.5 dB for the first 2.4 s, then -57.0 dB at
320.78 s, -44.4 at 321.13, -53.5 at 321.48, -49.2 at 321.63, -57.8 at 321.98, -46.1 at 322.58, and the re-bow dip
-54.6 at 322.83 (13.4 dB from peak to trough). With a 150 ms window the stem moves 4.0 dB in the first 2.4 s and
12.7 dB after it (-55.4 to -44.8 dB within 0.3 s at 320.8-321.1 s). The master (150 ms window) goes from -48.5 to
-42.6 dB in the same 0.3 s (qn 280.6-280.8, bar 85) and is back at -47.9 dB by 321.4 s: 5.9 dB. The basses are the
loudest stem there (Master -45.1, Double basses -49.4, Clarinet 1 -51.1, Violoncellos div -51.3 dB), so this is heard
as a slow pulse on a note printed as held. A second master rise at 322.45-322.6 s (to -42.1 dB) is partly
Clarinet 1's entry and is not counted. The c47 stem is identical; this is not new in c48.

**Cause (measured).** `build/rebow_fills.json`, "Double basses", key "278.351": 70 points, the last at 2.6 s
(-1.95 dB), then the value holds. `build/rebow_moves.json` moved the automatic re-bow from 280.990 to 282.203, so the
piece lasts 4.4 s: longer than the 2.6 s fit window (c34) and than the sample's 3.95 s loop period. Peak-to-trough on
the stem is 8.5 dB inside the fit window and 13.4 dB after it.

**Fix.** Refit this one piece over its whole length; keep the hand-set `rebow_moves.json` entry.
`~/.venvs/claude-composes-reaper/bin/python tools/fit_rebows.py cycles/c48 cycles/c48/rendered_build/parts.json --tracks "Double basses" --window "Double basses:4.1"`
without `--write`, then copy only the new list for key "278.351" into `build/rebow_fills.json` (W = min(4.1, piece
length - 0.3 s) = 4.1 s; the other basses keys keep their c34 fits). The needed correction is +6.5 to -6 dB, at the
edge of the tool's clamp (-6, +9). If the fitted list still leaves more than 6 dB on a simulated stem
(`tools/stem_fix.py --out`), only then move "280.990" in `rebow_moves.json` to about 280.9 so the piece is shorter
than the loop, after checking 0.6 s spacing against Violoncellos div 279.67 / 281.716 and Violas div 280.439.

Same class, lower weight: Violoncellos div pedal pieces of 2.29-2.82 s carry fits that end at 1.48 s. Stem
peak-to-trough after the fit window: 9.8 dB (key 275.527), 6.7 (277.599), 10.2 (279.67), 7.4 (281.716); the stem goes
from -58.1 to -48.2 dB at 321.5-321.9 s. Refit those four keys with `--window "Violoncellos div:2.5"` in the same way.

**Pass.** 150 ms window: Double basses stem at or under 6 dB peak to trough over 318.3-322.6 s; master at or under
4 dB over 318.3-322.3 s (before Clarinet 1's entry).

### 3. Violins II and Violins II div, sul tasto pad (Flautando), bars 37-40 (qn 108-124, 128.8-145.5 s): each change of harmony is heard 0.4-1.0 s after the beat

**Where.** Both tracks, pp, "senza sord., div., sul tasto": half notes, and quarter notes at 118 and 119. Each track
is one voice there.

**What is wrong (measured).** `tools/score_to_parts.py` lines 431-438: `FLAUT_LEAD_S, FLAUT_OVERLAP_QN = 0.45, 0.7`.
The new pitch starts 0.45 s early and the old pitch is held 0.7 qn (about 0.7 s) past the printed onset. The Flautando
attack is slow: relative to the note's body, -6 to -7 dB at +0.45 s after the note-on, still -5 to -8 dB at +0.85 s,
-3 dB at about +1.15 s. So the old pitch stays the louder one until it is released. Time at which the new pitch's band
passes the old one's, relative to the printed onset, and how long both are within 6 dB of each other (pitch names
from the MIDI numbers):

| Track | qn | interval | new pitch leads from | both within 6 dB for |
|---|---|---|---|---|
| Violins II | 114 | F sharp 4 after C sharp 4 | +1.00 s | 0.33 s |
| Violins II | 116 | C sharp 4 after F sharp 4 | +0.68 s | 0.83 s |
| Violins II | 118 | C4 after C sharp 4 | +0.75 s | 0.43 s |
| Violins II | 119 | E flat 4 after C4 | +0.82 s | 0.43 s |
| Violins II | 122 | C sharp 4 after E flat 4 | +0.70 s | 0.70 s |
| Violins II div | 112 | B flat 4 after A flat 4 | +0.38 s | 0.55 s |
| Violins II div | 118 | F sharp 4 after B flat 4 | +0.85 s | 0.75 s |
| Violins II div | 122 | F4 after F sharp 4 | +0.97 s | 0.80 s |

A beat is about 1.0 s. Seven of the eight changes are heard 0.68 s or more late; the quarter-note C4 at 118 leads for
about 0.25 s before the next change; the semitone pairs (118, and 122 on the div track) sound together for 0.4-0.8 s.
Levels over qn 112-120: Master -37.9, Flute 1 -40.3, Violins II -47.4, Violas -49.3, Harp -49.3, Double basses -49.4,
Violins II div -50.6 dB. The c15/c16 values were chosen for the level trough at each change (9-11 dB before them);
the time of the pitch change was not measured then.

**Fix.**
1. `tools/score_to_parts.py`: `FLAUT_LEAD_S` 0.45 to 0.75 and `FLAUT_OVERLAP_QN` 0.7 to 0.15. The lead stays capped
   at 0.45 of the previous note's length (lines 3346-3360), so the two quarter notes keep 0.45 s.
2. Add a fitted `vol_db` fill after each of the 8 joins so the shorter overlap does not reopen the trough: about
   +5 dB at the old note's note-off, falling to 0 by 1.2 s after the new note's note-on. Each track is one voice, so
   after the old note-off the fill acts on the new note only. Fit the values on a range render of qn 106-126.
3. Only if the trough cannot be held at or under 6 dB that way: test the moving voices on Sus MAX with CC1 at 0
   (manual p.92) for one range render and compare the same two numbers.

The re-bow points of the pad's held notes on Violins II div are not part of this.

**Pass.** At all 8 changes the new pitch's band passes the old one's within ±0.3 s of the printed onset, and the pad's
level trough (sum of both tracks, 150 ms window) is at or under 6 dB.

## Measured and passed (no finding)

- Legato: overlap medians 40-46 ms (strings 43-46, minimum 37); no chord on a legato row.
- Keyswitches: no note on a wrong row. String section keyswitches lead their notes by 33-34 ms (median; minimum
  20-22 ms; 28 of 254 under 25 ms), under the research default of 40 ms. The render is offline and the state check
  shows no level runs on these tracks, so I recommend no change (inferred).
- Tenutos, bars 61-62: brass re-tongue gaps 22-44 ms, string and woodwind overlaps 44-75 ms; no stem more than 6 dB
  down for over 70 ms except the printed breaths (Bass trombone and Tuba at 208, 333 ms; Contrabassoon at 210,
  293 ms).
- Tremolo, bars 61-64: dips at the changes 0-4.7 dB on stems, under 3.2 dB on the master.
- Pizzicato, bars 37-44: Double basses (Pizz RRx4, 21 notes) t(-6 dB) median +20 ms (0 to +58, SD 17), peak level SD
  1.8 dB; Violas from 124 +6 to +48 ms.
- Trombone 1's accents (the delivered stem is the c47 splice): 2-5 kHz share in the first 80 ms against the body,
  213: -19.1 against -15.5 dB (attack 3.6 dB darker); 218: -11.6 against -6.9 dB (4.7 dB darker); peaks at +160 and
  +232 ms. Weight, not bite. Repeat this after the full rebuild that c48's CHANGES schedules.
- Re-bows of the opening chord, bar 66 and the final chord: master dips under 3 dB except Violins I 298 (4.1 dB),
  Double basses 235.66 (3.9), Violins II 165.86 (3.4). The 4.2-4.4 dB at 289 is the printed new attack of bar 88.
- Mutes: every CC15 change sits in a rest (strings 9.5, 66.5, 90.5, 268.5-274.5; Horns 3-4 271.5) and matches the
  printed marks. Harp: rolled chords start on the beat and spread 40-120 ms; 3 harmonics on the Harmonics patch.
- Timpani: rolls on Flt Rls, strokes on Flt Lng; rolls steady within 2-4 dB after the attack.
- Patches: no patch change recommended this cycle. MANUAL-GAPS items 7, 8, 9 and 11 were not measured.

**Do not touch:** every standing item in `loop/HISTORY.md` and the earlier reports' lists, and from this cycle's
measurements: the Violas' Detache levels (per-note CC7, `VEL_SET["Violas"]`) and the Detache row itself; legato
overlaps and row choices; the tenuto gaps and printed breaths of bars 61-62; the tremolo joins of bars 61-64; the
pizzicato rows and leads of bars 37-44; Trombone 1's accent data (velocities, CC7 lanes, Sus MAX accents); the re-bow
points and fills of the opening chord, bar 66 and the final chord; the hand-set `rebow_moves.json` entries (including
Double basses 280.990 to 282.203 unless Finding 2's refit fails its test); the re-bow points of the Violins II div
Flautando pad; CC15 mute placement; the harp rolls; the timpani rows; `KS_LEAD`.
