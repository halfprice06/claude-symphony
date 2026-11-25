# Critic A, cycle 57 (render of cycle 56): articulation, joins, attacks

Measured on `cycles/c56/render` (delivered stems after the stem fix) with `build/` (`parts.json` and `mix.json` are byte-identical to `cycles/c56/build_fix/`). c54 and c55 renders used for comparison. Patch data read from the `.oib` files with `opus_state.load_oib` (read only). No REAPER, no audio settings, nothing deleted. Scratch: `/private/tmp/claude-501/mockup-loop/mvt2-c57-A/` (23 MB, scripts and 5 ms power frames, no audio), left in place.

No proposal below moves the track volume envelope. Every control is CC11, a note length or gap, a lead, a region gain, or the bow-split rule.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 57, so no page range was read. Two manual facts from `loop/MANUAL-GAPS.md` are used below, and three facts read from the patch files.

| Source | What it says | Where it applies | Does the render follow it |
|---|---|---|---|
| HO manual p.144 (MANUAL-GAPS #6) | True-legato velocity about 50-60 gives a longer transition, 110-127 a shorter one | String legato targets, all at 124 | No. See finding 3 for why 84-108 needs a lead correction |
| HO manual p.89-90 (MANUAL-GAPS #8) | DIV A / DIV B are half sections, Close mics only | The three doubled spans of c56 | Yes, with a side effect: the copy's stem is mono (L/R correlation 1.00 against 0.46-0.57 for the full section) |
| Patch files, Sus MAX and Leg Slur MAX regions (Violins I/II, Violas, Celli, Basses KS Masters) | Loop start 85,000, loop end 260,000 samples at 44.1 kHz (basses 80,000 / 255,000), no loop crossfade | Every held string note | A bow shorter than 5.9 s (basses 5.78 s) never reaches the loop end, so it cannot pulse. The split limit of 4.5 s and piece length of 3.1 s are tighter than the patch requires |
| Patch files, `LegatoSpeed` filter | `USE_VELO_SPEED` true; velocity `VELO_MIN`..127 maps to a sample start of 0..`START_MAX`: Violins I 30 / 4800, Violins II 40 / 4800, Violas 41 / 2173, Celli 40 / 2709 samples | String legato velocity | Velocity 124 to 90 starts the transition sample 38 ms later on violins, 19 ms on violas, 23 ms on celli |
| Patch file, Celli KS Master, groups `TLeg <source note>` | Transition regions are keyed by target pitch inside a group named for the source pitch. A flat 3 to G 3 is group `TLeg G#2`, key 55, layers p / mf / ff. EastWest trimmed the ff region itself (volume 0.83, later start) and left p and mf untrimmed | Celli 68.5, 77, 240.5, 249 | The four worst bursts of the movement are this one transition at CC11 49-56 (p / mf layers) |

## Findings, ranked

### 1. MUST DO. Held string notes: 97 bow changes where 51 are enough, and each one dips 4-8 dB (bars 1-3, 46-52, 61, 65-70, 79-92)

Measured (dip = mean of the 0.5 s windows before and after, minus the lowest 150 ms level within -0.3..+0.6 s of the bow change; "control" = the same statistic at instants at least 0.95 s from any note-on in the same held notes):

| | bow changes | median dip | control median |
|---|---|---|---|
| Violins I alone, final chord | 4 | 7.2 dB | 3.9 |
| Violins II alone, final chord | 5 | 7.4 | 2.8 |
| Violas alone, final chord | 5 | 4.6 | 2.2 |
| Violas div, 286-304 | 6 | 5.8 | 3.3 |
| Double basses, 220-238 | 6 | 4.3 | 2.0 |
| Double basses, final chord | 5 | 7.9 | 3.0 |
| Violins I + Violin I solo (sum), final chord | 9 | 6.4 | 2.5 |
| Violins II + div (sum), final chord | 10 | 4.2 | 1.5 |
| Violoncellos + div (sum), final chord | 10 | 4.3 | 2.8 (single stem) |

On the master, bow changes dip a median 3.5 dB in bars 83-88 (c54 2.0; 9 of 13 over 3 dB; control median 0.5) and 3.5 dB in bars 65-70 (worst 8.9 dB, basses). The final chord has 43 bow changes in about 20 s, median 1.9 dB (c54 1.9), worst 5.9 (Violins II div) and 5.7 (Violas div).

Three causes, each with its own control:

a) **Too many bows.** `REBOW_MAX_S` 4.5 and `REBOW_SEG_S` 3.1 (`tools/score_to_parts.py` line 673) split every chain over 4.5 s into 3 s pieces. The patch loops only from 1.93 s to 5.90 s, so a bow of 5.5 s plays no repeated material. In the c57 block of `build/score_config.py`: `REBOW_MAX_S, REBOW_SEG_S = 5.6, 5.0`, then re-run `tools/space_rebows.py` and thin `REBOW_AT` for the final chord to pieces of 4.6-5.4 s. Counted offline from `parts.json` `rebows`: 97 bow changes become 51. 21 chains lose their only bow change, among them:
   - Violins I 264.42 and Violins II 263.92 (bar 79, the ff B flat): the second piece plays Sus MAX after a Leg Slur MAX piece and stands **+4.7 / +4.3 dB** over it for the rest of the note (Violins II 264-265.8 is +3.8 dB over c54). Violins I 205.95 (bar 61): +2.5 dB.
   - Violoncellos 153.37 and 165.29 (9.5 and 9.2 dB dips on single-stem 50 ms levels), Violins II 165.86 (8.3), Violas 169.5 (7.3), basses 170.0 (6.2).
   - Basses pedal 220-238: 6 changes become 4. Final chord: 5 become 3 per instance, 43 become about 27.
   Decidable offline (the count). Pulse risk: none from the loop below 5.9 s (patch data); Movement I c59 saw no pulse at 5.2 s.

b) **Printed same-pitch repeats on held soft notes take the 80-150 ms repeat gap.** These are not ties: Violins II 51, 112, 120, 144, 289, 292; Violas 50, 62, 71, 271, 283; Violas div 70, 79, 289; Violins II div 114, 116, 119, 120. The score prints "change bow at will" at Violins II 292 and Violas 279. Single-stem dips (50 ms levels): Violas median 10.9 dB at these against 6.3 at 33-50 ms splits; Violas div 12.8 against 7.4; Violins II 112 15.5, 289 11.7, 292 11.9. Control: `STR_REP_NEW_BOW["soft_gap_s_at"]`, 0.05 s at the three points c49-c56 set to 0.12-0.15 (Violins II 289 and 120, Violas 271, Violins II div 120) and 0.04 s at the others. Expected: 2-4 dB shallower on the viola tracks, little on Violins II (its splits dip as deep as its repeats); S1 is kept by the new bow's attack. Needs the render to confirm.

c) **The re-bow lift ends before the new bow has spoken.** `REBOW_CC_LIFT` is +7 at the note-on, back to the lane by 0.45 s, after a 4-unit fall over the last 0.15 s of the old bow. The lowest level comes 0.1-0.6 s after the bow change (Sus MAX bloom), so half the lift is spent before the hole, and the pre-fall adds about 2 dB to it (it is also what deepened the basses' dips on pass a1). Change in `score_to_parts.py` at the `RL` block (about line 6379): add a `hold` key, `pts_ = [(sec_to_qn(t0_ - 0.005), 0.0), (q_, cc), (sec_to_qn(t0_ + RL.get("hold", 0)), cc), (sec_to_qn(t0_ + RL.get("hold", 0) + RL["s"]), 0.0)]`; config `{"cc": 8, "hold": 0.30, "s": 0.55, "max_cc": 46, "pre_fall": 0}`. Keep the basses out (`skip_tracks`). Expected 2-3 dB shallower (0.6 dB per unit at soft CC11); verify on the render, and check that no bow change now bumps by more than 2 dB.

d) **Doubling.** Extend `TRACK_DOUBLES["Violins II div"]["spans"]` to `[(286.0, 304.0)]` so the printed repeats at 289 and 292 fall inside a doubled span (the copy is idle from 123). Violas, Violas div and basses have no idle instance of their section in the coda; a) to c) are all that is available for them. With a), the alternating changes of source and copy are 2.3-2.7 s apart instead of 1.5-2.2 s (the scherzo measured 1.0-2.2 s for a bow to recover).

Doubled spans, the check asked for: no constant-lag correlation between source and copy (cross-correlation over ±100 ms in 1 s windows: scattered lags, median |r| 0.37-0.41, the value two tonal signals of one pitch give), no level bump at the span starts, and the sum's deviation from a 2 s median is no larger than the single section's (sd 1.8-2.3 dB against 1.9-2.4). Fundamental-band modulation 1-12 Hz is the same for the sum and for each instance (strongest line 1.4-2.0 dB). What does differ is the image: the copy is Close-only and mono, so the sum's L/R correlation rises from 0.48-0.57 to 0.71-0.78 over the doubled spans (measured; whether that is heard as a narrowing is for slot C).

### 2. MUST DO. Soft entries: the entry lift is spent before the beat (12 entries, 6-10 dB under their own level 0.35 s later)

The count of 71 mixes three things. Re-measured against a local body (the level over 0.35-0.85 s after the score onset, so crescendo hairpins do not count): **29 of the 71 are 6 dB or more soft**; 30 of the 71 sit under a printed crescendo and 13 are same-pitch re-bows (finding 1). Of the 29, 12 are fresh entries, 8 pitch-change joins, 8 level steps.

Cause of the entries (read from `parts.json`): `SOFT_ENTRY_CC` adds +8 at the **moved note-on** and returns over 0.5 s, but the note-on is 120-300 ms before the beat. Violins II 108 (lead 300 ms): CC11 42 at the note-on, 38 at the beat, 34 by +0.19 s; the stem reaches its level minus 3 dB only at +0.27 s. Double basses 140 (Sus MAX, lead 270 ms): no lift at all (the row list is Leg Slur MAX and Flautando), -3 dB at +0.49 s. Entries with no lead and no lift: Violas 168, Violas div 79, Violins II div 292 (the copy's first bow, 9.9 dB soft).

Fix, `score_to_parts.py` line 6406: key the hold to the score onset. `ts_ = qn_to_sec(max(n["sq"] for n in p["notes"] if abs(n["qn"] - q_) < 1e-3))`, then `[(sec_to_qn(t0_ - 0.005), 0.0), (q_, cc), (sec_to_qn(ts_ + SE_.get("hold", 0.15)), cc), (sec_to_qn(ts_ + SE_.get("hold", 0.15) + SE_["s"]), 0.0)]`. Config: `"rows": ("Leg Slur MAX", "Flautando", "Sus MAX")`, `"cc": 8, "hold": 0.15, "s": 0.5`. In `entry_leads.json` give Violas 168.0 and Violas div 79.0 a 0.12 s lead, and give each `TRACK_DOUBLES` copy its source's lead on the first piece (Violins II div 292.0).

Worst entries now (soft against local body, time to -3 dB): Violoncellos 139 9.5 dB / +0.34 s; Double basses 140 9.2 / +0.49; Violoncellos div 274 8.3 / +0.52; Violins I 171 7.9 / +0.35; Violoncellos div 292 7.9 / +0.51; Violas 0 7.8; Violas div 79 7.4; Violoncellos 238 7.1 / +0.53; Violas 78 6.9; Violoncellos 286 6.3; Violins I 0 6.3. Expected: +3 to +4.5 dB over the first 0.35 s at these, about 8 of the 12 under 4 dB. Not decidable offline; no range pass needed, read it on the render. The c54 fronts at these notes were 1-10 dB higher (fills), so nothing here exceeds what c54 had.

### 3. MUST DO. Transition bursts: a CC11 notch per join, and the answer on legato velocity

24 joins peak 5-13.7 dB over both bodies with a master bump of 2 dB or more. 11 of them were under +3 dB in c54 at the same instant, where a volume notch stood (celli 240.5 **+13.7** now, +1.6 in c54; 249.0 +10.9 / +2.6; 68.5 +8.9; 77.0 +7.1; Violins II 245.5 +6.8; Violins I 75 +6.7, 80 +6.2, 65.5 +6.0). The other 13 are unchanged from c54.

Velocity is not the cause (measured): 52 of 430 joins at velocity 124 burst (12 %), 4 of 30 at 60-108 (13 %); series 1 c21 found the same.

Fix: the same notch on CC11, before the hall. `CC_SHAPES_S[track]` rows `(11, score onset, [(s from the moved note-on, units), ...])`, spans from `cycles/c56/joinpeak_c56_fix.json`, depth (excess - 2 dB) at 0.6 / 0.5 / 0.45 dB per unit for CC11 up to 50 / 70 / above:

```
Violins I:    (11, 65.5,  [(-0.157,0),(-0.107,-8),(0.093,-8),(0.173,0)]),  (11, 75.0, [(0.002,0),(0.052,-9),(0.122,-9),(0.202,0)]),
              (11, 80.0,  [(-0.098,0),(-0.048,-9),(0.112,-9),(0.192,0)]), (11, 85.0, [(0.033,0),(0.083,-8),(0.153,-8),(0.233,0)]),
              (11, 249.5, [(-0.097,0),(-0.047,-6),(0.073,-6),(0.153,0)]), (11, 252.0,[(-0.067,0),(-0.017,-6),(0.013,-6),(0.093,0)]),
              (11, 271.0, [(-0.008,0),(0.042,-7),(0.072,-7),(0.152,0)])
Violins II:   (11, 56.0,  [(-0.025,0),(0.025,-8),(0.225,-8),(0.305,0)]),  (11, 190.0,[(-0.075,0),(-0.025,-9),(0.145,-9),(0.225,0)]),
              (11, 245.5, [(-0.012,0),(0.038,-8),(0.098,-8),(0.178,0)])
Violas:       (11, 144.0, [(0.032,0),(0.082,-5),(0.172,-5),(0.252,0)]),   (11, 220.0,[(0.031,0),(0.081,-8),(0.191,-8),(0.271,0)]),
              (11, 255.0, [(-0.008,0),(0.042,-7),(0.162,-7),(0.242,0)]),  (11, 286.0,[(0.224,0),(0.274,-6),(0.444,-6),(0.524,0)])
Violoncellos: (11, 48.0,  [(-0.025,0),(0.025,-6),(0.155,-6),(0.235,0)]),  (11, 68.5, [(-0.068,0),(-0.018,-11),(0.192,-11),(0.272,0)]),
              (11, 77.0,  [(0.004,0),(0.054,-10),(0.154,-10),(0.234,0)]), (11, 142.5,[(-0.008,0),(0.042,-9),(0.142,-9),(0.222,0)]),
              (11, 143.0, [(0.007,0),(0.057,-6),(0.137,-6),(0.217,0)]),   (11, 174.0,[(0.02,0),(0.07,-7),(0.15,-7),(0.23,0)]),
              (11, 240.5, [(-0.103,0),(-0.053,-16),(0.177,-16),(0.257,0)]),(11, 249.0,[(-0.175,0),(-0.125,-16),(0.135,-16),(0.215,0)])
```

Not listed: Violas 111.0 and 116.333 (arco triplets of 0.15-0.23 s, unchanged from c54). Expected: the 11 new bursts back to +2..+4 dB, the count from 24 to about 8. Not decidable offline; a range pass over qn 64-90 and 236-256 would settle the depths, otherwise read the render. An alternative for the four celli A flat 3 to G 3 joins, if `region_gain()` gets a group-name match: -6 dB on group `TLeg G#2`, key 55, row Leg Slur MAX (then halve the notch at 240.5 and 249.0 and drop it at 68.5 and 77).

**Legato velocity (`build_legvel/`, 84-108 by dynamic).** The values agree with the references (EastWest demos 57-124, median 92-98; manual p.144) but the build is wrong as it stands: by the patch's `LegatoSpeed` table it starts every violin transition 25-45 ms later than velocity 124 (violas 13-22 ms, celli 15-27 ms) and changes no lead. It would undo the 613 / 707 of 727 S result, and it does not remove bursts. Recommendation: do not render it in c57. If one range pass is free (range V, qn 64-90), build it with each string legato lead lengthened by `(124 - vel) / (127 - VELO_MIN) * START_MAX / 44100` s (table in the manual notes) and compare S and transition peaks with pass a1.

### 4. MUST DO. Four late or early arrivals (leads only; decidable offline)

From `cycles/c56/S_c56_fix.json` (S = perceived start against the beat; 20 of 727 joins are outside 60 ms, 10 of them viola triplets and inner parts):

| join | S now | lead now | change in `build/leg_leads.json` |
|---|---|---|---|
| Violins I 262.0 (bar 79, ff B flat 6) | +80 ms | 190 ms | 265 ms |
| Violins II 262.0 (same arrival, B flat 5) | +81 ms | 150 ms | 225 ms |
| Violins II 252.0 | -79 ms (Violins I +4: an 83 ms split between the sections on the theme) | 260 ms | 185 ms |
| Violoncellos 253.0 | -89 ms (crossover -36); c56 raised the lead 150 to 200 and overshot | 200 ms | 165 ms |

Both violin sections reach the loudest note of A' 80 ms late together. Leads have mapped about 1:1 here (LEARNINGS c11). Also outside 45 ms between the two violin sections: 86.5 (-73 ms, Violins II +62 at a 260 ms lead; leave), 73.5, 196, 269 (50-55 ms; leave). Violas 220.0 (-68 ms) reads early because of its +6.6 dB burst; the notch in finding 3 should return it.

### 5. MUST DO (small). Trombone 1 quotation, bars 63-64: the Sus MAX row is 3-5 dB under the legato row

Measured fronts (first 0.35 s): 212.5 -30.1, **213 (accent) -26.7**, 214.5 -30.0, 215 -29.0, 215.5 -27.5, **216 (tenuto) -32.3**, 217 -29.3, 217.5 -28.6, **218 (accent) -28.9**, body of 218 -34.8 (printed diminuendo to p). The track plays Sus MAX on exactly three notes: 216, 218 and 219.5. The same pitch (A 3) reads -27.5 on Leg Slur MAX at 215.5 and -32.3 on Sus MAX at 216, so the tenuto note is the softest of the phrase and the second accent cannot rise.

- `build/mix.json`, Trombone 1: `"region_gain_db": {"rows": [], "pitch_db": {}, "row_db": {"Sus MAX": 2.5}}`. Expected: 216 -29.8 (level with 217), 218 front -26.4, **+2.2 dB over 217.5** (aim +1.5 to +2). Take CC11 -4 over 219.5-220 so the p note stays where it is. Row gains arrived within 0.3 dB on pass a1, so this is decidable offline.
- 213 is +3.4 over its pickup: CC11 head 124 to 118 and the pickup 212.5 from 104 to 110 (0.1 dB per unit at the top) gives about +2.2.
- Bite (Dan's note 9): 2-5 kHz over the first 80 ms against the body is -9.6 dB at 213 and -0.8..+2.1 on the plain notes. At 218 it reads +9.9, of which 7.1 is the broadband fall of the diminuendo; no hard attack measured. Keep the plain-sustain accents.

### 6. Smaller items checked (none is a must)

- **Old CC7 lanes with lost envelope partners.** Level over each lane against c54: Cor anglais 266-268 +1.7 dB, Clarinet 1 205.75-209.9 -1.0 and 291.9-292.5 -0.1, Trombone 2 208-210 -0.9, Trombone 1 214.9-215.4 -0.1, Violoncellos 184.5 / 186.5 -0.7 / +1.1, strings 212-218 +0.9 to +1.8. The niente lanes 223.6-236.5 differ by -3.0 (Violins II), -1.7 (Violas), +3.6 (Violoncellos) at stem levels of -59 to -70 dB. Bass clarinet 273-276 is 3.9 dB under c54, but so are the 2 s before the lane (a level matter for slot B, not the lane). Violins II 264-265.8 (+3.8) is the row step of finding 1a. No lane needs deleting; the cor anglais lane could go to 97 (from 90).
- **Basses 144** (repeat of B flat 1 after a 4 s note, gap 60 ms): no dip, but the new note rises 4.4 dB over the old one within 0.25 s (own band h1-4: -56.1 before, -51.8 after). The repeat is marked by the swell. Leave it.
- **Divisi copies are mono.** Violin I solo, Violins II div, Violoncellos div and Violas div are Close-only with L/R correlation 0.998-1.000. For the bars 17-22 solo that is right. For Violas div (bars 23-30 and the whole coda) it is a section played as a point; a Main or Mid share on Violas div would match the tutti violas. Inferred, not tested; not for the last cycle.
- **Soft starts under hairpins and at joins** (17 of the 29): 8 are level steps of the line (celli 72, 78, 3; Violins II 54; basses 146, 210) where the front is the old note's level. They belong to slot B's line levels, not to attacks.
- Not re-measured this cycle for lack of time: harp arpeggios and harmonics, timpani strokes, the viola portato of bars 48-51 (c56's own figure: median step 1.42 dB, unchanged), pizzicato bars 41-44, tremolo bars 61-64.

## Order for the one session

All of 1a, 1b, 4 and 5 are data edits whose result is known before the render. 1c, 2 and 3 are lane shapes read on the render; if one range pass is affordable, spend it on finding 3 (qn 64-90 and 236-256), which carries the largest single faults (+13.7 and +10.9 dB on the celli's counter-melody). After 1a re-run the state guard on every string track (their re-bow pieces change) and re-fit the ten doubled CC7 values only if the sum level moves by more than 1 dB.

## Do not touch

The plain-sustain accents (no bite measured on Trombone 1); the leads of the 707 joins inside 60 ms other than the four in finding 4; the doubling of Violins I bars 1-3 and of the final chord (no comb, no bump, no added pulse measured); the single bow of bars 2-3 on Violins II, Violas, Violoncellos and basses; region gains and row gains as c56 set them; string legato velocity 124 until a lead-corrected test exists; the basses' exclusion from the re-bow lift.
