# Cycle 28, critic A: articulation and phrasing (on the c27 render)

Sources: `cycles/c27/render` stems and master, `build/parts.json`, `build/score_config.py`, `build/mockup-events.tsv`, `sections/bSec.ily`, score page 5, `tools/score_to_parts.py`, `tools/fit_rebows.py`, `tools/auto_fills.py`, May 2021 HO manual pp. 89-94 (row A1 of `loop/MANUAL-READING.md`), `loop/MANUAL-GAPS.md`. All times are score qn unless marked s. Levels are stem or master RMS: 30 ms windows for joins and attacks, 0.12 s for re-bows.

## Manual notes (A1, PDF pp. 89-94)

| Manual (PDF page) | Where it applies | Does the render follow it? |
|---|---|---|
| Divisi patches (DIV A/B) record one chair per stand, Close mics only; "the loudness of a divisi part is not much less than if the whole section were playing" (p.89) | Violin I solo (bars 17-22) on 1st Violins DIV A; Violins II div, Violas div, Violoncellos div | Partly. The div tracks are used the way the manual intends. For the solo, the DIV A patch is still half a section (about 8 players), so it cannot sound like one violin (gap #3). Its 9 legato joins all dip under 6 dB (measured), so the patch, not the joins, is the limit. |
| Divisi patches have Close mics only; for the other mics, add the non-divisi articulation and match the loudness (p.90) | Every div track (sends 0.5 in mix.json) | Uses the send alternative. That is acceptable. |
| Sustain patches cycle up and down bows as round robins, and offer finger position and three vibrato levels. Détaché "do not have a legato connection to the following note... come to a well defined end" (p.91) | Violas' sotto voce portato eighths, bars 48-51 (qn 152.5-167.5) | **No.** They play the Leg Slur MAX first-note layer, which has no round robin. Detache (Violas KS Master key 30) is not loaded. Finding 6. |
| Marcato Sustain adds a marcato sample to the looped sustain for "extra power at the start of the note" (pp.91-92) | The ff tutti arrivals at 204 and 262 (strings "molto sostenuto") | Not used (Sus Marc LITE exists, key 25). Not ranked: the tenuto joins in bars 61-62 already sound right (Do not touch). |
| Flautando is in the 2nd Violins only; elsewhere use a pp Sustain with CC1 at its lowest (p.92) | Violins II div sul tasto, bars 37-40 | Yes. Both Violins II tracks play Flautando, re-bowed on Flautando. The master dips at those re-bows are 0-3.2 dB. |
| Pizzicato is a round-robin patch with 2 or 4 samples per note (p.92) | Violas 124-140, basses 108-140 and 212 | Yes, Pizz RRx4. Onsets are on time: median half-rise +0.02 s for the violas and +0.00 s for the basses (measured). |
| Staccato On Bow: "the bow does not lift off the string ... comes to a full stop" (p.94) | A candidate for the portato eighths, bars 48-51 | Not used. Finding 6 names it as the second choice after Detache. |
| Repetitions: about a dozen repeated notes per sample, not round robin (p.94) | No fast repeated strokes in v600 | Not applicable. |
| MANUAL-GAPS #8 (4 soli on DIV patches) and #9 (horn/trombone portato rows) | Basses 220-238 and 286-304, celli 274-286; tutti tenutos 204-212 | Not used. Gap #8 still applies. Gap #9 is low priority, because the tenutos of bars 61-62 measure well. |

## Findings, ranked by what a listener would hear

### 1. Trombone 1's quotation (bars 63-64, qn 212.5-219.5): v600's slurs play as detached marcato strokes, and the slurred accent lands 0.5 s late

- **Where.** Trombone 1, qn 212.5-219.5. It is the loudest stem in bar 63 (-24.9 dB).
- **What is wrong.** v600 slurs almost the whole line: `e8( c'4.->) b8( bes8 a8 | a4--) gis8( a8) f4.-> e8`. The composer's comment (c240) calls it "falling B-B flat-A slurred into the repeated A, portato on it". v77 printed no slurs (`symphony/mvt2/reaper/build/sections/bSec.ily`: `r8 e8-> c'4.-> b8 bes8 a8 | a4 gis8 a8`), and series 1's `MARCATO_SPANS = {"Trombone 1": [(212.5, 219.0)]}` was written for that version. `in_marc()` in `score_to_parts.py` comes before every slur rule. As a result, each unaccented note plays Marc Lng RRx4 at 0.75 of its written length, and the accented C4 (213) is cut 0.25 qn short as a fresh Sus MAX (`ACCENT_ART_AT`, `MARC_ACC_CUT_AT`).
- **Evidence (measured).**
  - The parts.json gaps between slurred notes are 0.139-0.165 s.
  - Trombone 1 stem, drop from each note's peak to the gap: 9.7 dB (212.5 into 213), 7.8 / 11.3 / 12.8 dB (B-B flat-A-A), 10.6 / 11.4 dB (G sharp-A, A into F).
  - The master's 150-1500 Hz band shows the same breaks at 6.6-12.2 dB, because the strings are in their sf decrescendo there.
  - The slurred accent at 213 peaks at +0.48 s after the beat, with its first 80 ms 5.2 dB under its body. The emphasis lands almost half a beat late.
  - The unaccented Marc Lng A3 at 217.5 has the brightest attack in the line: 2-5 kHz front minus body +6.5 dB, against -6.3 and -1.2 dB on the two accents. So an unaccented note bites harder than the accented ones.
  - The two accents are not harsh (BRIEF item 9 is answered).
- **Fix.** In `build/score_config.py`:
  - Delete Trombone 1 from `MARCATO_SPANS`, from `MARC_ACC_CUT_AT`, and 213.0 from `ACCENT_ART_AT` and `ACCENT_SWELL_S_AT`. Keep 218.0 (unslurred, accented) as Sus MAX with its swell.
  - Set `GENTLE_ACCENT["brass"]["keep_legato"] = True`, so the slurred accent at 213 stays a Leg Slur MAX target with the swell. Kit LEARNINGS 20 (c07) measured this: slurred brass accents re-tongued on Sus stood +2.6..+9.5 dB over their slur.
  - Set `WIND_REP_PORTATO = True`, so the slurred tenuto A at 216 is re-tongued with the WIND_REP_RETONGUE gap and fall. Movement I c13-c15 found that the Hollywood Brass KS Masters need about a -4 dB volume dip to separate a repeat, so check that 216 dips 3-6 dB.
  - In `VEL_SET`, give the legato targets 214.5-217.5 velocities 110-115 for firm, fast ff transitions.
  - Keep the marcato character as weight, not separation: a +1.5..+2 dB swell (`ACCENT_SWELL_S_AT`-style, 0.04/0.15/0.35 s) on the first note of each slur (214.5, 217.0).
- **Check after the render.**
  - Join dips 2-4 dB inside the slurs.
  - 213's peak within +0.25 s of the beat.
  - 2-5 kHz front minus body at or under 0 dB on every note.

### 2. Re-bows in the final chord, bar 66 and the opening chord: the series 1 shapes no longer fit, the ppp fermata swells 3-5 dB, and bar 66 has a 10 dB hole

- **Final chord (qn 292-304).** In v600 the final chord is morendo (298-301) into a ppp fermata (301-304).
  - **Measured.** The master falls to -51 dB at 301.4-301.7, then rises to -48/-47/-46 dB at 302.0-302.9, a +3-5 dB swell inside the ppp fermata. Each stem steps at its re-bows:
    - Violoncellos: -3.9 (293.6), -9.1 (298.6), +7.2 (300.6), -8.0 dB (302.35). The dip at 298.6 is 14 dB.
    - Violins I: dip 10.9 dB at 301, step +4.1 at 302.75. The stem goes from -61 to -51 dB at 303.1.
    - Violas: +3.3 (301.5). Double basses: +4.0 (302.0). Violins II: +2.4 (302.2).
  - **Cause.** The shapes in `build/rebow_fills.json` were fitted on series 1's c26 stems. Since c27, REBOW_VEL, the CC11 curve and the volume rows differ, and the shapes carry swings of up to 15 dB (Violins I vol_db -15.0 at 301.72 and -0.5 at 302.83; Violoncellos -14.7 at 300.57 and -0.4 at 302.9).
  - The new "Violas div" points (287.3-302.95) have no shapes at all. Their stem dips are 4.5-7.6 dB.
- **Bar 66 (qn 222.45-223.4).**
  - **Measured.** The master falls from -41 to -50 dB at 223.2. That is a 9.7 dB hole about 0.3 s long, followed by a -4.1 dB step.
  - **Cause.** Violins II, violas and celli re-bow on the printed down-bow at 223.0 together (Sus MAX, v45, no shape). Their stem dips are 11.7, 8.3 and 9.6 dB. The basses' automatic re-bow at 222.45 adds a 6.4 dB dip 0.55 s earlier.
- **Opening chord (qn 0-9).**
  - **Measured.** Stem dips are 7.4-11.9 dB (Violins I 2.4/4.6/7.35, Violins II 5.15, violas 5.7, celli 6.8), with no shapes. The master dips 1.2-4.6 dB because the points are staggered.
- **Fix.**
  - Run `tools/fit_rebows.py 27 build/parts.json --write --hold-max-after 301:0`. That option is movement I's fix for the same morendo swell. It refits every listed and automatic re-bow, including Violas div and the opening chord.
  - In `REBOW_AT["Double basses"]`, move the basses' bar 66 point away from 223 (for example to 221.8, so it is at least 0.6 s from the three printed re-bows) and refit.
  - Keep the printed down-bow at 223 for the three upper sections. A real bow change there is a soft re-articulation (2-3 dB), not a 10 dB gap.
- **Check after the render.**
  - Master at qn 301-304 never above its level at 301.
  - Master dip at 223 at most 3 dB.
  - Median stem re-bow dip at most 3 dB, as kit LEARNINGS 6 measured for c26.

### 3. Timpani: every roll plays the loudest dynamic layer, so the ppp soft-stick rolls have the ff colour

- **Where.** Timpani rolls at 3 (ppp, bars 2-3), 168 and 200 (pp <), 204/208 (ff), 226-237 (ppp "near the rim", bars 67-70, 13.5 s), 261 (pp <), 262-270 (ff/f).
- **What is wrong (measured).** parts.json has no CC1 lane on the Timpani track: `TIMP_CC1_MAP = []`, the port left movement I's map out. Movement I c12 read the Timpani Flt KS Rls row in the patch: it crossfades eight recorded dynamic layers on CC1, and with no CC1 lane every roll played V8, the fff layer. This render shows the same thing. The rolls' 1-8 kHz share of energy is:

  | roll | printed | 1-8 kHz share |
  |---|---|---|
  | qn 3 | ppp | -11.5 dB |
  | qn 226 | ppp | -12.7 dB |
  | qn 168, 200 | pp | -11.5 / -11.4 dB |
  | qn 204 | ff | -13.7 dB |
  | qn 262-268 | f | -13.1..-13.8 dB |

  So the ppp rolls are as bright as, or brighter than, the ff ones. Movement I measured V8 at about -13 dB and V4 at about -31 dB. The soft rolls are loud samples turned down in CC7. That is the hard-stick, "on top of the orchestra" colour that Dan's roll rule (BRIEF item 5) is about.
- **Fix.** In `build/score_config.py`, take movement I's final values (`symphony/mvt1/reaper-v621/build/score_config.py`, c12):
  - `TIMP_CC1_MAP = [(22, 56), (34, 56), (46, 60), (58, 66), (72, 72), (88, 88), (114, 104), (124, 122)]`
  - `TIMP_ROLL_TRIM_DB = [(22, 17.6), (34, 19.0), (46, 18.6), (58, 12.7), (72, 9.5), (88, 7.3), (114, 3.7), (124, 0.0)]`

  The layers are recorded at their own levels, so the trims put the level back. Then refit the roll levels by stem fix against c27's per-roll levels (-54.4 / -54.7 / -33.0 / -37.1 / -55.0 / -32.9 dB at qn 3 / 168 / 200 / 204 / 226 / 261). With CC1 following the printed curve, the crescendo rolls at 168, 200 and 261 also cross the layers as they grow. That is the cheap first step before gap #7 (Felt Cresc).
- **Check after the render.** The 1-8 kHz share in dynamic order (ppp/pp about -25..-31 dB, ff about -16 dB), and BRIEF item 5 level checks unchanged.

### 4. Legato joins: 69 of 735 dip 6 dB or more on the stems; Bassoon 1 is the worst (11 of 32)

- **Where.** The measure covers each target on a Leg row that a different pitch sounds into. The dip is the lower of the 0.3 s before and the 0.35-0.7 s after, minus the minimum between moved onset - 0.05 s and onset + 0.35 s. The counts at 6 dB or more are:

  | track | joins of 6 dB or more | all joins |
  |---|---|---|
  | Violoncellos | 12 | 107 |
  | Violas | 12 | 138 |
  | Bassoon 1 | 11 | 32 |
  | Violins I | 7 | 85 |
  | Violins II | 6 | 116 |
  | Flute 1 | 4 | 52 |

  Every other track has 0-2.
- **Worst joins (measured).**
  - Violoncellos: 246.0 (10.4 dB), 50.0 (8.6), 195.5 (8.6).
  - Violins I: 73.5 (9.3), 67.5 (9.2), 251.5 (8.2).
  - Bassoon 1: 199.0 (8.8), 256.0 (8.5), 261.0 (8.1), 255.0 (7.2). In bars 76-77 Bassoon 1 is the second-loudest stem (-37.1/-36.3 dB), so these holes are exposed.
  - Violoncellos div 63.0 (8.4), Clarinet 2 246.0 (8.1), Violas 56.0 (8.1) and 266.0 (7.9), Cor anglais 152.0 (7.6).
- **Cause (inferred).** Most of these are in qn 117-270, where v600 changed notes and the port dropped 89 per-note entries. The early fills there were fitted on v77's notes or are missing.
- **Fix.**
  - Run `tools/auto_fills.py 27 build/parts.json --write`, with its overshoot rule. Exclude the hand-set entries the port kept, and the re-bow pieces.
  - Re-measure with a 200 ms window on Flute 1, Oboe 1 and Cor anglais before acting on their counts (vibrato).
  - For Bassoon 1 (no family lead extra: `ENTRY_LEAD_ART_S["Bassoon"] = {}`), also check the crossover times at 199, 255, 256 and 261 before adding fills (kit LEARNINGS 6: hold a fill only to the sag minimum).

### 5. Violins II bars 15-21: the slurred portato repeats sound in the wrong places (S1)

- **Where.** Violins II, qn 42-56. The score has `aes'2--( aes'4--)` pairs on one pitch, followed by a new slur on the same pitch: A flat at 42, 44, 45 and at 48, 50, 51.
- **What is wrong (read and measured).**
  - The three A flats merge into one note of 4.8 qn (5.5 s). AUTO_REBOW then splits it at 44.34 and 50.35, a third of a beat after the printed notes.
  - **Violins II stem:**

    | point | what is printed there | dip |
    |---|---|---|
    | 44.0 | portato | 3.0 dB (a CC11 notch) |
    | 44.34 | nothing (automatic re-bow) | 9.5 dB, minimum at qn 44.5 |
    | 45.0 | new slur, new bow | 1.0 dB |
    | 50.0 | portato | none |
    | 50.35 | nothing (automatic re-bow) | 9.1 dB, minimum at qn 50.6 |
    | 51.0 | new slur, new bow | none |

  - The re-articulation a listener hears falls between beats. At the printed bow changes on 45 and 51 the repeat is not heard at all. Violins II is the second-loudest stem in bars 15-16 (-44.7 / -43.8 dB).
- **Fix.**
  - In `build/score_config.py`, add `REBOW_AT["Violins II"] += [45.0, 51.0]` (the printed new bows, which take over from the automatic points 44.34 and 50.35), and `NOTCH_SKIP["Violins II"] += [45.0, 51.0]`. The pieces are then 42-45 (3.5 s) and 45-47, both under REBOW_MAX_S, so no automatic point remains.
  - Keep a gentle CC11 notch (4-6 CC at pp) for the portato at 44.0 and 50.0.
  - Fit the new re-bows with `fit_rebows.py` (finding 2) to a 2-4 dB re-articulation.
- **Check after the render.** S1: dips of 3-6 dB at 44, 45, 50 and 51 (30 ms), and nothing between the beats.

### 6. Violas' sotto voce portato eighths, bars 48-51 (qn 152.5-167.5): slow first-note samples that bloom on the following beat (S2)

- **Where.** Violas, 15 off-beat eighths, pp, each followed by a rest, under the cor anglais quotation.
- **What is wrong (measured).** Every eighth plays Leg Slur MAX at v37, 0.54 s long, led 0.11 qn. On that patch an isolated note is the first-note layer, and it has no round robin.
  - The eight A3 eighths reach -6 dB of their peak at +0.25-0.26 s and peak at +0.34-0.38 s after the score onset. The eighth lasts 0.556 s at 54 bpm. So each swells into the next beat instead of being placed on the "and".
  - All eight A3s peak at -48.0 ± 0.2 dB with the same timing to 0.01 s: the same sample every time.
  - The E flat 4 eighths (164.5-167.5) reach level at +0.07 s, so the slow rise depends on pitch.
- **Fix.** In `build/score_config.py`, `ART_SPANS` (or a per-onset articulation table) for Violas 152.5-168.0. Use Detache (Violas KS Master key 30), which the manual describes as notes with no legato connection that "come to a well defined end" (p.91). Keep each note at its written length minus 0.05 qn, at the pp level of CC11, with the string entry lead (0.06-0.12 s from the c27 rise times). The second choice is Stac On Bow RRx9 (key 28, "the bow ... comes to a full stop", p.94) at 0.5 qn. A row change rebuilds the Violas track: the row costs about 0.1-0.3 GB, and its own new rows need a check.
- **Check after the render.**
  - Each eighth reaches body - 3 dB by +0.12 s.
  - Successive A3s differ by 0.5-2 dB (round robins).
  - The stem level stays at about -48 dB.

## Smaller observations (not ranked)

- The violas' pizz triplets open 16-17 dB under the bar after them: qn 124-125.67 at -58..-49 dB, against -41..-40 dB at 126-128. The printed marks are pp < p, and velocities 41-46 sit under a layer edge (measured). Raising the velocity floor of the first beat to about 47 (`TIMP_VEL`-style `VEL_SET` entries) would make the figure's start audible. This is for critic B.
- The bass clarinet's tied pp A flat 2 (qn 6-17) rises +11 dB inside one sample (-51 to -40 dB) while CC11 stays flat at 34. This is the baseline's open item and a level question for critic B. If it is fixed as articulation, a staggered BREATH_SPLIT (movement I c05/c25) would also break the swell.
- Double basses' 4 soli pedal (220-238): the 0.5 s window level swings 5.4 dB (p10-p90) at about 0.7 Hz, with no 3.95 s periodicity (autocorrelation -0.0). It sounds as an uneven bow, not a loop. MANUAL-GAPS #8 (Basses DIV A for the 4 soli) would also suit it better than the full section at -3 dB, if memory allows one more Close-only instance (about 0.7 GiB).

## Do not touch

Keep these; they measure well:
- **Bars 61-62 molto sostenuto tenutos.** Strings on Leg BC MAX, winds and brass crossfaded. The master dips at 206, 208 and 210 are 0.6, 0.8 and 2.2 dB.
- **Tremolos.** The tremolo entries at 204/212, and no re-bows inside the held tremolos. The 212 entry dips -0.4..+1.1 dB on Violins I, Violins II and the celli; the violas re-enter louder, at -4.9 dB.
- **Pizzicato.** Rows and timing on the violas and basses.
- **Harp.** Rolled chords from the bottom, 40 ms per note.
- **Mutes.** CC15 placement: every mute change falls in a rest.
- **Trombone 1's accent at 218.** Sus MAX with its swell (2-5 kHz front minus body -1.2 dB).
- **Violins II div Flautando.** Re-bowed on Flautando.
- **Violin I solo legato joins.** All under 6 dB.
