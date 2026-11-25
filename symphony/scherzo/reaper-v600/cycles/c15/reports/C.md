# Cycle 15, critic C: tempo, timing and transitions (lens C3), on the c14 render

Material: `cycles/c14/render/` (31 stems, master), `cycles/c14/build_render/` (parts.json, mix.json, tables), `build/score_config.py`, `build/leg_leads.json`, `cycles/c14/records/` (S_c13 / S_c14, timing13_c13 / _c14), `cycles/c14/actor_scripts/` (themefit14.py, s14.py), `cycles/c13/actor_scripts/timing13.py`, `tools/pcx.py`, `tools/build_reaper.py` (`vol_points`), the c11 C report (this lens on c10).

Methods. "pc" is `pcx.attack_pcx` (perceived attack on the note's harmonic bands, the previous pitch excluded on joins), "xr" is the robust crossover of the old and new pitch bands (`robust_cross` of timing13.py / s14.py), both in ms from the score onset on the render's tempo map. Measure S is the smaller of the two. I ran both on 23 tracks over the whole movement (4,230 readings), once on the stems and once on the stems with the written volume envelope divided out (`vol_points` of the c14 build, interpolated linearly between points; valid because the envelope is a gain after the instrument). pc and xr disagree by 50 ms or more on many single notes, so I call a join late or early only where both agree in sign and both pass 60 ms ("agreed"), or where one estimator is the only one that applies and a second fact supports it. Entries have pc only; pc over-reads soft notes that swell.

## Manual notes (T2: May 2021 HO manual, PDF pages 147-149 and 99, read in full, 147 and 149 as images; MANUAL-GAPS.md read)

| Manual (PDF page) | Where it applies here | Render follows it? |
|---|---|---|
| p.99: a legato transition needs two notes with no significant gap, and "the first note of a phrase has no legato effect" | every legato-row note whose predecessor plays on another row (the keyswitch falls between them): 51 such joins on Violins I, Violins II, violas, celli and Flute 1, among them the downbeats after a Sus MAX pickup eighth (159, 372, 387, 597, 855) and the notes after c14's new Sus MAX strokes | No. These notes are first notes on the legato row and take the legato lead of a transition. 9 of 51 are agreed late by more than 60 ms, against 18 of 570 joins inside one row (findings 1 and 4) |
| p.99: legato instruments are monophonic by default; CC22 switches | every legato track | Yes: CC22 127 in the pre-roll (the polarity of p.99 is reversed, 2025 p.91; c09 checked the patches) |
| p.99: Legato Slur Staccato rows give the first note of each legato phrase a stronger attack | the soft phrase heads that read late (finding 6); the row "StacSl Leg BC + Slur + Port MAX" is in every string KS Master | Not used: 54 thousand regions on Violins I (MANUAL-GAPS section 16), memory. No change proposed |
| p.99: keyswitches select the row for the notes that follow | keyswitch lead: Violins I and celli median 150 / 130 ms (c14 `KS_MIN_LEAD_S`), Violins II, violas, Flute 1, Oboe 1, Horn 3 median 7-8 ms, 5th percentile 5-7 ms, none under 3 ms | Yes |
| p.147 violin finger positions (EastWest note names are an octave down): G sharp 5 is on the A string only at FP4; C sharp 5 to D sharp 5 on the A string at FP1-3; B4 at FP1-2; A4 at FP1; A5 and above on the E string at every FP | `SUL_SPANS`: Violins I 0-23, 528-538, 1089-1125; Violins II 364-383.5, 839.5-851.5, 1044-1054 | Yes on Violins I (G sharp 5 at CC70 127, C sharp 5 / D sharp 5 / E5 at 90, B4 at 55; A5 at 533 marked string 4). Violins II: D sharp 5 at 366 is sent at 127, which p.147 puts on the D string; the tool reads the patch's own string tags (c07 C), unchanged since. No note outside a "sul" span sounds at a CC70 other than 127 (checked every note-on of the three tracks) |
| p.148-149 viola and celli tables | no "sul" span on violas or celli; lanes rest at 127 | n/a |

## The actor's open timing list: which readings are real

| reading in c14 CHANGES | pc / xr on the stem | without the envelope | verdict |
|---|---|---|---|
| Violas 828, +261 | +386 / +261 | same | real. A v41 legato-row note after a leap of 13 semitones (no transition sample over an octave); finding 4 |
| Violins I 144, +76 | +112 / +76 | +119 / +76 | real (Sus MAX stroke, 60 ms lead); finding 4 |
| Violins I 372, +105 | +105 / +136 | +120 / +136 | real (legato-row downbeat after the Sus MAX pickup 371.5); finding 1. Violins II plays the same note at +209 / +180 |
| Violins I 855, -61 | +12 / -61 | -64 / -61 | real as a pitch change 61 ms before the beat; the envelope's level shape hides it in pc. Lead 209 ms is 50 ms too long; finding 4 |
| Violins II 123, +62 | +62 (entry) | +61 | real but small; the class of 60 ms strokes reads +25 (finding 4) |
| Violas 855, +68 | +68 / +92 | same | real; finding 4 |
| celli 840, +56 | +148 / +56 | +150 / +56 | real; with 648 (+165 / +118) the two leaps onto a Sus MAX stroke; finding 4 |
| Flute 2 912-960 | five joins agreed late: 921.5 +82 / +99, 922.5 +79 / +61, 931.5 +79 / +61, 943.5 +113 / +129, 954.5 +79 / +71; 955 (-137 / +69) is not a valid reading (neighbouring same pitch) | same | real on five eighths in an ff tutti; finding 5 |
| Violins I landing staccatos 42, 288, 774, 798, -61..-130 | as an "entry" (no pitch excluded, timing13.py's class) -61..-130; with the second eighth's pitch excluded +4, +4, +8, +4 | entry class -19..-54; excluded +9..+15 | the measure. The notes are on time. xr reads +39..+51: the ringing second eighth stays the stronger pitch for 40-50 ms after the beat, as in c13 |

Across all 4,230 readings the per-note envelope does not carry the timing: S is outside 25 ms on 1,253 notes with the envelope and 1,291 without it. 188 readings move by more than 25 ms when the envelope is divided out (115 earlier with the envelope, 73 later; 42 by more than 60 ms), most on violas (26), Violins I (28), celli (21), timpani (21: the tutti strokes read -1..-20 ms with their shapes and +40..+53 without).

## Findings, ranked by what a listener would gain

### 1. A row change inside a slurred line makes the notes after it late; c14's stroke at qn 144 put Violins II 60-110 ms behind Violins I for four bars (measured; mechanism read in the MIDI)

Where: Violins II and violas, bars 49-52 (qn 145.5-154), after the new Sus MAX stroke at 144 (`_c14_strokes`); the downbeats after a Sus MAX pickup eighth in both violin sections and the celli (qn 159, 372, 374, 387, 597, 792, 882).

Evidence:
- Violins II, S on c13 -> c14 with the same leads on these notes (`records/timing13_c13.json` / `_c14.json`): 146 -36 -> +72, 148 -5 -> +91, 150 +20 -> +114, 152 +13 -> +58, 154 -29 -> +73. My reading of c14: pc / xr 146 +100 / +72, 148 +100 / +91, 150 +116 / +114, 152 +109 / +58, 154 +73 / +152. Violas: 146 +7 -> +50, 148 +1 -> +43, 150 -11 -> +33, 152 -16 -> +50.
- Violins I, which got the same stroke and was then refitted, plays the same notes at pc / xr +7 / +14, +43 / +22, +21 / +29, +1 / +61, +11 / +28, with leads 60-70 ms longer than Violins II's on 148-154 (210, 185, 225, 210 against 173, 140, 148, 138 ms). So the two violin sections, in octaves on the second idea, are 60-110 ms apart on five consecutive notes. In c13 they were within 40 ms.
- The MIDI: in c13 the keyswitch to Leg Slur MAX stood at 143.82, before the note at 144, so 144-154 was one legato chain. In c14 the 144 note is a Sus MAX stroke that sounds until 145.12, the keyswitch stands at 144.83 (7 ms before the next note-on, under the sounding stroke) and the legato row starts with 145.5 as a first note (manual p.99).
- The same class elsewhere, legato-row notes that overlap a note on another row: Violins I 159 +113 / +57 (lead 209), 372 +105 / +136, 387 +119 / +27, 597 +92 / +92; Violins II 159 +108 / +76, 372 +209 / +180 (lead 74), 387 +164 / +88; celli 792 +82 / +59, 882 +142 / +57, 312 +220 / +93, 321 +98 / +106, 912 +214 / +77. Over five tracks, 9 of 51 row-change joins are agreed late by more than 60 ms and 14 by more than 45 ms; of 570 joins inside one row, 18 and 32. On the three refitted tracks this class holds most of what the refit left: 4 of Violins I's 6 joins outside 45 ms in `S_c14.json` (159, 372, 597, 855) and 5 of the celli's 11 (312, 321, 792, 882, 912).
- Violins II also has agreed-late joins inside the legato row that the refit would catch: 134 +100 / +77, 374 +159 / +98, 840 +91 / +66, 846 +78 / +69. Its count stays at 43 / 13 of 104 outside 25 / 60 ms against Violins I's 9 / 3 of 100.

Fix:
- Best: give Violins II and violas what c14 gave Violins I (`build/score_config.py`: `ROW_REMAP` Leg BC MAX -> Leg Slur MAX is not needed, they already use one legato row; add both to `KS_MIN_LEAD_S` 0.15 and run `refit14.py` on two agreeing whole-piece passes, gain 1.0 then 0.8). Include the row-change joins in the refit. Target: Violins II and violas at 15 or fewer of about 100 joins outside 25 ms, and every doubled note of 132-160, 360-392 and 840-856 within 40 ms of Violins I.
- If the lock time is short, per-onset rows in `build/leg_leads.json` (seconds, added to the present values, 0.8 x S): Violins II 146 +0.058, 148 +0.073, 150 +0.091, 152 +0.046, 154 +0.058, 134 +0.06, 374 +0.08, 840 +0.05, 846 +0.055; violas 146 +0.04, 152 +0.04. Print the realised lead next to the requested one (c13 lesson: the cap or the minimum gap may bind).
- The downbeats after a Sus MAX pickup (Violins I and II 159, 372, 387, Violins I 597, celli 792, 882): they are first notes on the legato row, so a longer transition lead does little (Violins I 159 and 387 already have 209 ms). Make them Sus MAX strokes as c14 did for 157.5 / 385.5 / 853.5 (`DOWNBOW_STROKE_AT`, `REATTACK_LEAD_AT` 0.085 s on the violins, 0.15 s on the celli, `REATTACK_KEEP_END`), and refit the joins that follow each new stroke to the end of its slur in the same passes. A stroke added without that refit repeats the bars 49-52 fault.
- Fallback for bars 49-52 alone: take 144.0 out of `_c14_strokes["Violins II"]` and `["Violas"]` (c13 state: 144 at +105 / +139, the five joins after it within 40 ms).

### 2. The trio tune in the celli and Horn 3 (bars 169-184) limps: the long notes at qn 510, 512 and 524 arrive 110-170 ms late (measured)

Where: celli arco espress. with Horn 3, qn 504-552; again 567 and 572; Horn 3's recall of the tune at bars 341-344 (qn 1020-1030).

Evidence (pc / xr; a quarter at 228 lasts 263 ms, an eighth 132 ms):
- Celli: 510 +154 / +117 (lead 65 ms), 512 +110 / +113 (lead 147), 524 +158 / +168 (lead 102), 567 +106 / +115, 572 +96 / +99. The other 28 joins of 504-552 are agreed late nowhere; their leads are 115-265 ms.
- Horn 3 on the same notes: 510 +188 / +124, 516 +77 / +138, 519 +107 / +124, 523.5 +78 / +84, 524 +72 / +117. In bars 341-344: 1022 +100 / +124, 1023 +68 / +60, 1025 +110 / +78. Its legato lead is 60 ms at v100 and 50 ms on the re-tongued v53 heads (510, 516, 519, 522 start 13 ms after the previous note's end).
- Clarinet 1 plays the same tune in bars 153-168 at +6..+31 ms on every note (462 +9 / +22, 464 +31 / +28, 476 +28 / +16), and the harp's off-beat chords stand at -1 ms median. So the clarinet statement is in time and the cello statement is not.
- Causes read in the data: celli 510 carries a refit offset of -0.115 s in `leg_leads.json` (lead 180 -> 65 ms); 512 and 524 follow the pickup eighths 511.5 / 523.5, and `LEG_MIN_GAP_S` (celli 0.1 s between note-ons) holds their leads at 147 and 102 ms although `leg_leads.json` asks +0.09 and +0.295. On this row at v80 the new pitch passes the old about 250 ms after the note-on (147 + 110, 102 + 158). In bars 209-224 the celli play the same figure at v112-118 and 656 lands at +38 / +57 with lead 157: the faster transition of high velocities (manual p.144) is worth about 60 ms here.

Fix:
- `build/leg_leads.json` Violoncellos: "510" -0.115 -> 0.0.
- `build/score_config.py`: legato velocity 112 on the celli notes after a pickup eighth, 512, 524, 536, 567, 572 (`VEL_SET`; p.144: velocity sets the transition time, not the loudness; the rest of the tune keeps c10's v80), and `LEG_MIN_GAP_S["Violoncellos"]` 0.06 inside 504-576 (Violins I's value), which frees 40 ms of lead on 512 and 524.
- Horn 3: legato lead 0.06 -> 0.11 s over 504-552 and 1020-1032 (kit: 0.10 s worked on brass legato), and 0.12 s on the four re-tongued heads 510, 516, 519, 522 (the per-onset re-tongue lead table).
- Target: celli 510, 512, 524, 567, 572 and Horn 3's listed notes within +60 ms on both estimators, celli and Horn 3 within 40 ms of each other. Measure with `s14.py`; if 524 stays over +80, accept it and say so (the row's limit after an eighth).

### 3. The theme head in Violins I: the envelope jumps 8-15 dB in the 27 ms before the first slurred eighth's beat and falls 9-13 dB across the beat (measured; this is one of the shapes Dan saw)

Where: seven of the nine soft statements (qn 41, 53, 77, 287, 761, 773, 797; 71 and 791 by 1.5-2 dB), the `_c14_lv` rows of `build/score_config.py` (line 1159).

Evidence:
- Written envelope at 41: 5.2 dB at 40.90, 13.0 at 40.98, 8.5 at 41.00, 4.0 at 41.02. At 53: -0.5, 14.5, 7.8, 2.3. At 287: -1.0, 7.4 at the peak, -0.5 after. The same form at 77, 761, 773, 797.
- Cause: the half note's body row returns to 0 dB over q - 0.24 .. q - 0.02 and the eighths' step to `a` (-7 to -11.5 dB) starts at q - 0.02 (c14 moved it to the score onset). The first eighth's note-on is at q - 0.396 (lead 90 ms), so for the 50 ms before its beat it plays with no cut and with the tail lift `u` on top.
- Stem, 20 ms frames around the beat (-40..-20, -20..0, 0..+20 ms, then the eighth's body +20..+110 ms): 41: -44.1, -36.0, -40.7, body -37.2; 53: -49.6, -37.2, -40.8, body -41.0; 287: -51.0, -39.5, -45.4, body -42.5; 773: -48.0, -36.3, -40.1, body -39.4. The frame before the beat is 5-12 dB over the frame before it, 3-5 dB over the frame after it and 1-4 dB over the eighth's own body. With the envelope divided out the level rises evenly (287: -41.5, -38.3, -37.2).
- c14's check "the half note's last 140 ms raised from -7..-15 to -5..-8 dB under its start" measured this bump: the half note's MIDI ends at q - 0.416, and what sounds in that window is the first eighth.
- Timing: the first eighth reads pc -20..-24 ms with the envelope and -3..-20 without it. The pair and the landing staccato are on time (table above).

Fix, with the before / after stem measurement (simulated on the c14 stem; the envelope is post-fader): in the nine rows, replace the points (q - 0.55, u), (q - 0.02, u), (q + 0.02, a) by one crossfade from the level at the eighth's note-on to `a`: (q - 0.40, level before), (q - 0.20, a), and take the half note's body row to its end at q - 0.40 instead of q - 0.24; drop `u`. Simulated result, frames -40..-20 / -20..0 / 0..+20 ms and body: 41: -45.5 / -42.5 / -41.4 / -37.2; 53: -47.0 / -45.8 / -41.5 / -41.0; 287: -50.7 / -47.5 / -46.5 / -42.5; 773: -45.9 / -44.5 / -40.9 / -39.4 (a steady rise into the body at all nine); first eighth pc -3..-22 ms, xr unchanged (-30..-44); the half note's last 100 ms before the eighth's note-on unchanged (-34.2..-47.3 dB). This removes two points per figure.

General rule for the c15 envelope work (inferred from this case): a level step "on the score onset" is right only for a note with little lead. A note with 45-250 ms of lead has been sounding at the previous level for that long. Key the step to the moved note-on when the previous note has ended, and to the crossover (score onset + S) when it still sounds, and move every row that changes at that join at the same instant.

### 4. Sus MAX strokes with 60 ms of lead speak 25 ms late as a class and up to 110 ms late singly; two cello leaps are 120-165 ms late; Violas 828 is 260-390 ms late (measured)

Evidence:
- Long Sus MAX notes (0.3 s or more) by lead, pc median: Violins I 45-75 ms lead +23 (n 13), 75-115 ms +3 (n 7); Violins II +25 (n 13) and +5 (n 13); violas 0 (n 10) and -9 (n 11).
- Singles: Violins I 144 +112 / +76; Violins II 123 +62, 897 +69; Violas 855 +68 / +92; celli 648 +165 / +118 and 840 +148 / +56 (leaps of 14 and 16 semitones up, v105, lead 120 ms).
- Violas 828: +386 / +261 with c14's entry extra (+187 before it). It is a v41 Leg Slur MAX note a 13th above the note before; lead alone moves the quiet part of a soft first-note sample earlier (kit section 6).
- Violins I 855: the pitch changes 61 ms before the beat (xr -61; pc -64 without the envelope) at 209 ms of lead.

Fix (`build/score_config.py`):
- `REATTACK_LEAD_AT` for the c14 violin strokes 0.06 -> 0.085 s; Violins I 144 0.13 s (the value of its hemiola strokes at 300-310, which land within 50 ms); Violas 855 0.11 s; celli 648 and 840 0.12 -> 0.18 s. Entry strokes Violins II 123 and 897: entry lead 0.085 s.
- Violas 828: remove c14's +0.13 s entry extra, put the note on a Sus MAX stroke with a CC11 lift at the note-on (+22, back to the curve 0.5 qn later, lead 0.09 s; c11 lesson: this moved soft re-attacks from +31..+177 to -47..+50 ms where a volume swell did not). No envelope row.
- Violins I 855: `leg_leads.json` -0.05 s.
- Target: every listed note within 45 ms on both estimators; Violas 828 within +100 ms on pc.

### 5. Flute 2 in the reprise tutti (bars 305-320): five slurred eighths 60-130 ms late against Flute 1 (measured; small in an ff tutti, inferred)

Evidence: 921.5 +82 / +99, 922.5 +79 / +61, 931.5 +79 / +61, 943.5 +113 / +129, 954.5 +79 / +71; Flute 1 on 921.5 and 930.5 -12 / +71 and -17 / +55. 922.5 and 931.5 already have the listed cap (85 ms of lead); the other three have 51 ms. Whole track: 8 of 49 legato joins over 60 ms, median +20 against Flute 1's +5.

Fix: add 921.5, 943.5 and 954.5 to Flute 2's listed rows in `build/leg_leads.json` (value 0.0; they then take the 0.75 cap). Do no more: 85 ms of lead left 922.5 and 931.5 at +61..+79, so the rest is the patch's transition (c11: 0.04 s more lead moved this flute by 7 ms).

### 6. Soft phrase heads still read 100-200 ms late; the ff return of the trio tune starts 70-120 ms after the clarinet in Violins I (measured with pc only, which over-reads swelling notes; carried from c11 C #2)

Evidence (pc; entries, no xr): Violins I 528 +146, 576 +204, 603 +160, 1089 +171; Violins II 672 +193 (c10 +281), 708 +138 (+272), 1068 +170, 360 +118; celli 504 +140 (+243 with the envelope divided out, so the early fill is worth 100 ms here), 1071 +144; violas 1020 +109 (+261), 708 +100; solo 1044 +127 (+228); Flute 1 1044 +67 (+324); Oboe 1 672 +194 (+220); Horn 1 6 +97. The c11 fills and leads halved most of them.
- Bar 209 (qn 624), the trio tune's return, espress. ff: Violins I +99 (v83, lead 120 ms), Violins II +32 (lead 180), Clarinet 1 -21. This one is a loud entry and can be fixed with lead.
- Flute 1 132 (bar 45, the second idea's entry) reads +148 where c13 read +16 with the same lead (55 ms); +142 with the envelope divided out. c13's stems are gone, so I could not find the cause. Check it on the next render before changing anything.

Fix: Violins I 624 entry lead 0.12 -> 0.18 s (`build/entry_leads.json`, Violins II's value). For the soft heads no new envelope rows: where a head is still over +150 (Violins I 576 and 603, Violins II 672 and 1068, Oboe 1 672), a CC11 lift at the note-on (+10..+15 for 0.5 qn, as in finding 4) is the tool to test on a range render; adopt it only with a before / after pc.

## Do not touch

- The tempo map. Bar averages against the print: bar 2 at 88 (2.045 s); 149-152 at 253.4 / 240.5 / 232.5 / 228.0 (print 252 / 240 / 232 / 228); 237-240 at 222.5 / 214.0 / 206.5 / 202.0 and 241-252 from 199 to 256.5, one curve, Tempo I 264 at 253; Più mosso 288; G.P. 96 (1.875 s); Meno mosso 228; 370-375 at 212.5 / 195.7 / 179.3 / 160.7 / 146.6 / 140.0 (print 210 / 196 / 180 / 160 / 140 / 140; the c11 overshoot to 133 is gone); bar 376 at 50 (3.6 s). No `BEAT_STRETCH`, `CAESURA`, `PHRASE_ARCS` or `TEMPO_PUSH` (c13 removed the unprinted steps: keep it so).
- Staccato and pizzicato timing in the theme statements and tuttis: S medians by track for short notes after a rest: Violins I +1, Violins II -9, violas -4, celli +1, basses' pizz. +8, Flute 1 +10, Flute 2 +15, Oboe 1 -6, cor anglais -6, Clarinet 2 -10, trumpets -10 / -9, Horn 1 -14, timpani +15, harp -1. The whole spread is 29 ms, a quarter of an eighth.
- "Ritmo di tre battute": the basses' pizz. heads at -45.0 dB against -47.3 and -50.4 in the second and third bars of each group, the master's head bars 5-8 dB over the second bars, the timpani on the third. The groups are marked; the c11 finding is closed.
- Clarinet 1's trio tune (bars 153-168: every join +6..+31 ms) and the harp's off-beat chords with no lead.
- Violins I's, the celli's and the solo's refitted joins inside the legato row (Violins I: no same-row join agreed late or early by more than 60 ms of 92; solo 0 of 18).
- The landing staccatos of the theme head at 42, 288, 774, 798: on time (+4..+8 ms); do not move their note-ons to answer the S reading.
- Keyswitch placement (none under 3 ms before its note), CC70 lanes, CC22, `RR_RESET_AT`, the hall and the G.P. (c14: drop 20.7 dB at +0.3 s, RT60 1.30 s).
