# Critic A, cycle 53: articulation and phrasing (review of the c52 render)

Data: `cycles/c52/render/*.wav` (stems and master), `cycles/c52/rendered_build/parts.json`, `cycles/c52/rendered_build_pass2/parts.json`, `build/score_config.py`, `build/*.json`, `build/mockup-events.tsv`, `tools/score_to_parts.py`. "pc" below is the perceived attack centre minus the score onset (BRIEF S2), in ms; positive is late. Bar b starts at qn 4(b-1). Every number is measured on the c52 stems or read from parts.json unless marked inferred.

## Manual notes

Pages are PDF pages of the May 2021 Hollywood Orchestra Opus manual. I chose the pages behind this cycle's open items (flute pair, legato timing, wind shorts, brass sf, string re-bows).

| Manual says | Page | Where it applies here | Does the render follow it |
|---|---|---|---|
| "Flute 2" is a second flautist in another seat; no samples are shared with "Flute", so the two do not behave as one instrument. | 108 | Flute 1 and Flute 2 on the same line: bars 68-72 (qn 271-284) and bars 158-161 (qn 629-644). | Partly. Flute 2 has its own base lead since c52 (0.11 s against 0.03 s), but the two still land 45-155 ms apart on 16 of 18 shared onsets (finding 2). |
| On true-legato patches, velocity sets the length of the transition (about 50-60 longer, 110-127 shorter) and does not change loudness. | 144 | Every legato target. The flutes' long targets in the climax are v60 (qn 634, 640) and v80 (642); strings and brass targets have median v124. | Followed as a rule (`LEG_VEL_STRONG`, `LEG_VEL_SPANS`). The two latest Flute 2 joins are the v60 and v80 targets, which fits the page (inferred, not tested). |
| A slur happens only when there is no significant gap between two notes; legato instruments are monophonic by default. | 99, 112 | All Leg Slur / Leg BC rows. | Yes. parts.json has 0 chords on legato rows, 0 same-pitch overlaps and 0 cases of two notes held into a legato target. |
| Woodwind Staccato, Staccatissimo and Double Tongue are recorded short notes without release trails; hold the MIDI note so the room rings. | 110 | Printed wind staccatos: bar 30 (Flute 1, Oboe 1, Clarinet 1), bars 88-96 (Bassoon 1, Cor anglais, Flute 1). | Bars 88-96 yes (Stac DblTng RRx9 in the second pass). Bar 30 no: slices of Sus rows, 84-133 ms long (finding 5). |
| Brass Sustain takes its dynamics from the Mod Wheel; on Sustain Accent velocity sets the attack; Sustain Marcato has a weaker attack whose velocity sets a low-pass filter. | 101 | The tutti sf at qn 160 (bar 41), where the brass play an eighth on plain sustain rows. | The rows are legal but the result is not an sf: the heavy brass peak 0.15-0.23 s after the mark (finding 3). Marc Sus LITE failed in c47 (MANUAL-GAPS 1), so the fix proposed is a level shape, not a row. |
| String Sustain is looped and alternates up-bow and down-bow samples (round robin). | 91 | Re-bow pieces of long notes; the basses' repeated eighths (`RR_RESET_AT` since c52). | Yes. No held string note is longer than 6.5 s, so the 3.95 s loop fold has nothing to test in this movement. |

## The three items the c52 actor left open

| Item | c52 actor | My measurement on the c52 render | Verdict |
|---|---|---|---|
| Flute 2 late at qn 280, 636, 639.5, 642 | Flute 2 minus Flute 1: 280 +85, 636 +118, 642 +75 ms (639.5 not in its table); 643 -155 | Flute 2 minus Flute 1: 280.0 +85, 636.0 +118, 639.5 +79, 642.0 +75 ms. Also 634.0 +48 and 271.0 +45. In the other direction: Flute 2 is 49-71 ms ahead of Flute 1 at 275.5, 277, 281.5, 283, 283.5 and 629; Flute 1 late at 272.0 (+145 ms) and 643.0 (+129 ms). | Confirmed, and wider than the four onsets: finding 2. |
| Violins I sf at qn 78 peaks at +0.14 s | +0.14 s, 1.1 dB over the first 0.1 s | First 0.1 s -30.0 dB; peak 20 ms frame at +0.15 s, -28.9 dB (1.1 dB higher). | Confirmed and small. No change needed. |
| Celli CC1 macro "fails the join rule" | 8 of 147 joins grew by 2 dB or more; violas (no macro) 3 of 71 | c51 against c52, 261 matched celli joins: median dip 1.50 against 1.57 dB; 6 grew by 2 dB or more (2.3 %), 12 shrank by 2 dB or more. Tracks without the macro: Violas 1 grew and 4 shrank of 129; Violins I 7 grew of 245 (2.9 %); Violins II 4 of 125 (3.2 %). | Not confirmed as an effect of the macro. Joins grow at the same rate on tracks that do not have it, so this is render-to-render variation. The macro is neutral on joins; vibrato depth is unchanged (14 cents). Keeping or dropping it makes no measurable difference to joins. |

## SHARED-TECHNIQUES items 18-23 in Movement I

| Item | Applies | Bars | Measurement |
|---|---|---|---|
| 18 Low-string repeated eighths measured at 30-120 Hz; dip in the gap before each beat | Yes on the basses' stem, low priority | 27-31, 131-134, 140-142 | Stem on-beat / off-beat dips: 4.7 / 6.9, 5.2 / 7.5, 5.1 / 9.8 dB (the stroke before the beat is the weaker one, as in the finale). Master on-beat dips 10.9, 8.3, 7.2 dB; only bars 140-142 lie under the finale's fixed range (7.8-10.6 dB). Bars 167-169 are the reverse case (13.7 / 4.2 dB) and must not get the dip. |
| 19 sf on winds and brass: post-fader bump +3 dB over 0.35 qn | Yes | 41 (qn 160) | Finding 3. There is no sfp in v621; the plain sf at 160 has the same late fronts. |
| 20 Negative lead rows must be added before the clamp | Yes | Onsets listed in finding 4 | `tools/score_to_parts.py` clamps base + row first and adds the extras afterwards. 10 of 16 onsets with negative rows are still 16-60 ms early. |
| 21 Louré chord repeats against new-slur chord repeats | No | none | String chord repeats are almost all in the Violas (54). No tenuto chord repeat inside a slur exists. The two new-slur chord repeats (Violas 48.0, Violoncellos 500.0) are already fresh strokes under `STR_REP_NEW_BOW`. |
| 22 Note trims ramp in over 0.6 s | Partly checked | not enumerated | The default `NOTE_TRIM_RAMP_S` is 0.6 s; many rows in `build/note_trims.json` are already 0.1 s steps (`_steps`, config line 315). I did not list the rows on notes shorter than 0.6 s that still use the default ramp. |
| 23 Delivery ride after a subito | No in practice (inferred) | 61-62 (qn 244/245), 84 (qn 332) | The ride rows are 0.5 dB and none starts at a subito. |

## Findings, ranked

### 1. Three sections change bow together at qn 292 (bar 74), and six Lento re-bows are deeper than the surrounding texture (measured)

Where: bars 72-75, Violins II, Violas, Double basses; bars 4-12, Violoncellos, Double basses, Violas, Violins II.

What is wrong: at qn 292.0 the Violins II (printed repeat of Eb4) and the Violas (printed repeat of C4) start new whole notes and the Double basses' automatic "change bow at will" row sits on the same beat. The master dips 4.1 dB there. In the same four bars the master's dips at moments with no note event within 0.35 s have median 0.4 dB, p95 0.7 dB, maximum 0.8 dB, so the dip is five times the largest dip of the surrounding texture. LEARNINGS asks for re-bows of different sections at least 0.25 s apart. The stems: Double basses 8.2 dB, Violins II 4.8 dB, Violas 4.9 dB at 296.0.

In the Lento the same comparison gives control dips of median 0.7, p95 3.1 dB. Six re-bows are over the p95 (1.7 expected by chance): qn 12.16 (3.3 dB, celli stem 4.3), 21.44 (3.4, celli stem 6.8), 26.0 and 26.52 (4.9 each; basses row 26.003, celli row 26.516, celli stem 9.0), 40.0 (3.1, Violas stem 5.4), 47.0 (3.3; Violins II stem 4.2, basses stem 5.5). The fills in `build/rebow_fills.json` for these rows were fitted before the c50 mix change, and LEARNINGS says to refit after any mic or hall change.

Fix:
- `build/score_config.py`, `_REBOW_FROZEN` (line 436): move the Double basses' row 292.0 to 290.9. The basses hold one pitch from 286 to 304; at 126 bpm the new point is 0.52 s before the printed changes at 292.0, 0.84 s after the celli's 289.145 row and 0.43 s after the note changes of Violins II and Violas at 290.0. Re-key its fill in `build/rebow_fills.json` ("Double basses", key "292") and refit it with `tools/fit_rebows.py`. Leave the printed re-articulations of Violins II (292.0) and Violas (296.0) as they are; they are in the score.
- Refit, without redesign, the fills of Violoncellos 12.163, 21.442, 26.516, Double basses 26.003, Violas 40.0 and the two rows at 47.0 against the c52 stems. Target: stem dip at most 3 dB and master dip under the Lento control p95 (3.1 dB). Several of these are on earlier do-not-touch lists (the bar-12 re-bow, the 26.516 caps): keep their positions and velocities and change only the fill points.
- Check after the render: master dip at 292.0 at most 2 dB; no new dip over 2 dB at 290.9.

### 2. The two flutes land 45-155 ms apart on 16 of 18 shared onsets (measured)

Where: Flute 1 and Flute 2, bars 68-72 and 158-161.

What is wrong: c52 raised Flute 2's base legato lead to 0.11 s. That fixed 633 and 640 (difference +3 and +28 ms), but soft and medium joins are now early and the loud climax joins are still late. Flute 2 is another player's samples (manual p.108), so one base value cannot fit both.

| qn (bar) | Flute 1 pc (lead) | Flute 2 pc (lead) | Fl2 - Fl1 | Change |
|---|---|---|---|---|
| 271.0 (68) | +23 (55) | +68 (55) | +45 | Flute 2 entry +0.04 s |
| 272.0 (69) | +145 (35) | +29 (36) | -116 | Flute 1 +0.11 s |
| 275.5, 277.0, 281.5, 283.0, 283.5 (69-71) | +21, +28, +8, +7, +4 | -45, -43, -48, -42, -62 (110) | -49 to -71 | Flute 2 -0.045 s on each |
| 280.0 (71) | -1 (35) | +84 (70) | +85 | Flute 2 +0.07 s |
| 284.0 (72) | +35 | -21 | -56 | Flute 2 -0.03 s |
| 629.0 (158) | +24 | -43 | -67 | Flute 2 -0.04 s |
| 634.0 (159) | +36 (130) | +84 (150) | +48 | Flute 2 +0.06 s, Flute 1 +0.03 s |
| 636.0 (160) | -5 (70) | +113 (130) | +118 | Flute 2 +0.09 s |
| 639.5 (160) | -16 (50) | +63 (120) | +79 | Flute 2 +0.05 s |
| 642.0 (161) | +48 (30) | +123 (110) | +75 | Flute 2 +0.10 s, Flute 1 +0.04 s |
| 643.0 (161) | +129 (50) | -26 (110) | -155 | Flute 1 +0.10 s (its row is +0.02 now) |

Keep 633.0 and 640.0 (difference +3 and +28 ms) and 643.5 (48 ms apart, but each flute within 35 ms of the beat).

Fix: per-onset rows, in the table the tool reads for each kind of onset. The values in the last column are 0.8 times the measured error, in seconds, positive = earlier.
- True legato joins (634.0, 642.0, 643.0, 275.5-284.0, 629.0): `build/leg_leads.json`. Flute 2's only row now is 633.0.
- 639.5 is a slur-start join from a Sus MAX note (`SOST_JOIN_LEG_LEADS`, config line 3668): a `leg_leads.json` row on Flute 2 works there since c52.
- 636.0 is an entry after the breath: `build/entry_leads.json` has 0.015 for both flutes; set Flute 2 to 0.105. The note before ends at 635.78 and the new note-on would move to about 635.73, so check that the note before still ends 40-60 ms before it.
- 271.0, 272.0 and 280.0 are tongued starts on the Leg Slur MAX row (the note before ends 0.04-0.05 qn earlier, or there is a rest). The c52 actor found `leg_leads.json` rows without effect on such onsets, so use `entry_leads.json` or `retongue_leads.json`, whichever the build log shows as applied.
- If a row at 634.0 or 642.0 does not move the landing, raise those two targets from v60 and v80 to v105 with `LEG_VEL_SPANS` (tools line 962; manual p.144: higher velocity shortens the transition). Inferred, not tested.
- Check after the render: Flute 2 minus Flute 1 within ±35 ms on the changed onsets and within ±50 ms on all 18.

### 3. The sf at qn 160 (bar 41) has no weight in the brass: their eighth swells instead of striking (measured)

Where: bar 41 beat 1, tutti sf. Trumpets 1-3, Tuba, Bass trombone, Horns 3 and 4; less so Oboe 1, Flute 2, Clarinet 1.

What is wrong: the strings and Flute 1 peak within 0.05 s of the mark, and the master peaks at +0.04 s. The trumpets, tuba and bass trombone play a 0.6 qn note (0.29 s at 126 bpm) on plain sustain rows and their level is still rising when the note ends. Horns 3 and 4 and the three winds hold longer notes whose first 0.1 s is weak.

| Track | First 0.1 s (dB) | Peak time | Peak (dB) |
|---|---|---|---|
| Trumpet 1 | -30.9 | +0.22 s | -27.0 |
| Trumpet 2 | -32.2 | +0.21 s | -28.1 |
| Trumpet 3 | -35.7 | +0.19 s | -29.2 |
| Tuba | -29.8 | +0.15 s | -26.1 |
| Bass trombone | -34.8 | +0.23 s | -32.8 |
| Horn 3 | -40.7 (6.2 dB under its f before) | +0.37 s | -35.2 |
| Horn 4 | -40.7 | +0.19 s | -34.9 |
| Oboe 1, Flute 2, Clarinet 1 | | +0.37, +0.35, +0.18 s | |

Trombones 1 and 2 are in time (+0.13, +0.07 s). The finale measured that more lead does not help winds and brass (item 13) and that a post-fader bump does (item 19). Movement I already has such bumps at 160 on Violins I, Violoncellos and Double basses (`POST_SHAPES_S`, config lines 3623-3627) but none on the brass.

Fix: `build/score_config.py`, `POST_SHAPES_S`, a row at 160.0 on each track, in the form already used for Violins I at 78: `(160.0, [(-0.07, 0.0), (-0.06, 3.0), (0.17, 3.0), (0.25, 0.0)])` for Tuba, Bass trombone, Horn 3, Horn 4, Oboe 1, Flute 2, Clarinet 1, and the same with 4.0 dB for Trumpets 1-3 (0.17 s is 0.35 qn at 126 bpm). Start each row at that track's own moved note-on if it is earlier than -0.07 s (Horn 3 starts at 159.88, Trumpet 3 at 159.86). Check after the render: each stem's first 0.1 s within 2 dB of its peak, and brass minus strings in the first 0.1 s of bar 41 up by 2-3 dB. Do not go back to Marc Sus LITE (c47).

One accent with bite, same beat: Flute 1's G6 at 160.0 has a 2-5 kHz front 8.6 dB over its body and a tilt jump of +16.3 dB (c51: +9.1 dB). Every other accented track has a negative front-minus-body value (medians -7.6 to -29.1 dB). The note is an unled Sus MAX at v98. A candidate fix (inferred): a `POST_SHAPES_S["Flute 1"]` row `(160.0, [(-0.01, 0.0), (0.0, -3.0), (0.07, -3.0), (0.15, 0.0)])`. It is low priority because the flute's first 80 ms sits under the trumpets once their front is raised.

### 4. Negative lead rows lose part of their value to the clamp (read in the code; effect measured)

Where: `tools/score_to_parts.py`, about lines 3743-3768. Affected onsets: Flute 1 at qn 115, 296, 299.5, 397.5, 555, 633, 639.5, 640 (base 0.03 s, so every negative row); Oboe 1 at 407, 579, 582; Cor anglais 275; Clarinet 1 180; Horn 1 411.5.

What is wrong: the code computes `ls_ = clamp(leg_s + row)` and then `tot = clamp(ls_ + extras)`. When base plus row is under 0.03 s it is raised to 0.03 s before the velocity and articulation extras are added, so the row removes less than its value. This is the finale's item 20 (-0.07 s realised -0.03 s there). Measured pc at onsets with negative rows, with the realised lead in brackets: Flute 1 296 -40 (70), 299.5 -60 (90), 397.5 -22 (70), 555 -23 (80), 640 -28 (70); Oboe 1 407 -35 (120), 579 -32 (80), 582 -53 (200); Horn 1 411.5 -36 (180); Bassoon 1 523 -36 (107). Ten of sixteen are still 16-60 ms early. The largest are in Oboe 1 bar 146, Flute 1 bar 75 and Horn 1 bar 103.

Fix: one line. Replace the two clamps with `tot = max(LEG_LEAD_CLAMP[0], min(LEG_LEAD_CLAMP[1], leg_s + ex + lx))` when a row exists. Then rebuild with `--midi-only`, list the lead of every onset that has a row before and after, and re-check the rows that were fitted against the old behaviour: Flute 1 633 (-0.09) and 639.5 (-0.07) were set in c52 and now land at +6 and -16 ms, so halve them if the new leads fall under 0.03 s. Cor anglais 275 measured +158 ms late with a 106 ms lead and a -0.04 row. Either my measure failed on that note or the row has the wrong sign; listen to bar 69 before changing it. Check after the render: the ten early onsets within ±25 ms.

### 5. The bar 30 wind staccatos are slices of sustain samples and are uneven by 8-15 dB from note to note (measured; the patch remedy is inferred from bars 88-96)

Where: bar 30, qn 116.0-117.5, four staccato eighths in Flute 1, Oboe 1 (Sus MAX) and Clarinet 1 (Sus Non Vib), doubling Violins I.

What is wrong: the notes are 84-133 ms long at CC11 119 and v95, with a volume envelope that moves less than 1.8 dB across the four notes. Peak levels: Flute 1 -34.0, -35.6, -38.2, -42.3 dB; Oboe 1 -32.6, -47.4, -44.1, -36.9 dB; Clarinet 1 -34.2, -34.4, -44.4, -34.8 dB. Nothing printed asks for these differences. A sustain sample cut this short has not reached its level when the note ends, and how far it gets depends on the pitch's sample. The notes do separate (12-22 dB between peak and the minimum before the next onset), so this is a level and tone defect, not a legato one. The same doubling in the fugato (bars 88-96) was moved to the recorded "Stac DblTng RRx9" row in an earlier cycle and kept (MANUAL-GAPS 11: "Oboe 1 / Clarinet 1 bar 30 not tried"; manual p.110).

Fix: `build/score_config.py`, `ART_SPANS` (pattern at lines 2321-2327): add `{"from": 116.0, "to": 118.0, "art": "Stac DblTng RRx9", "mark": "staccato", "vel_by_cc": _WSTAC}` for Flute 1 and Oboe 1, and the Clarinet KS Master's staccato row ("Stac" in DIGEST 7.3; take the exact name from the KS map) for Clarinet 1, on second-pass "... stac" instances as for the fugato windows. Give the notes the lengths the fugato spans use, so the recorded short and the room are not cut (manual p.110: the shorts have no release trail). Check after the render: the four peaks of each instrument within 4 dB, and pc within 30 ms of Violins I. If the row's level is over the Sus slices by more than 3 dB, lower `_WSTAC`'s top value for these spans rather than the track level.

### 6. Oboe 2's eighth before the breath in bar 161 sounds for 109 ms of a written 300 ms (measured in the MIDI)

Where: Oboe 2, score onset 643.5, note-on 643.417, note-off 643.600, v100; next note-on 643.850 (score 644.0, with a printed breath mark).

What is wrong: the default breath rule in `tools/score_to_parts.py` (about lines 2788-2806) ends a loud wind note 0.3 qn before the breath, at most half the note, and counts back from the next note's led onset (643.850, a lead of 0.15 qn). The eighth is left 0.183 qn long with a silence of 0.25 qn (150 ms) after it. On the same eighth Flute 1 sounds 370 ms, Flute 2 409 ms, Horns a2 360 ms and Trumpet 1 250 ms. Across all 58 notes that end at a breath mark the median sounding-to-written ratio is 0.92; this note is at 0.20 and the next lowest is 0.77.

Fix: `build/score_config.py`, `BREATH_GAP_AT["Oboe 2"]`: add `643.5: 0.10` (the key is the onset of the note that ends at the breath; the value is in qn). By the rule's formula the note then ends at 643.750: 0.333 qn long (200 ms) with a 60 ms gap. Check both values in parts.json. This is one doubled note in a tutti ff, so its audible weight is small.

## EW-TEMPLATE-PLAN sections this lens touches that are not applied

- Section 5, legato overlap: `LEG_OVERLAP = 0.04` is in quarter notes (tools line 83), which gives a median of 19-21 ms in the Allegro on nearly every track, against 45-80 ms (strings) and 33-58 ms (winds, brass) in the study. I measured no audible consequence: legato joins dip 1.4-2.1 dB in the median and none failed to connect. Legato velocity: strings and brass targets have median v124 against the study's 92-98 and 90-105; winds are 60-100.
- Section 6, two tracks per string section: not applied (one track and one KS Master per section).
- Section 7, per-note lean-off: not applied as a rule; release shapes exist only where a row was written.
- Section 8, tutti entry spread: not applied as a rule; leads are fitted per onset toward a common landing.
- Section 10, beat-position velocity on shorts: partly. The repeated-eighth spans have metric tables (parts.json `metric_db`, `metric_vel`) and the basses have `RR_RESET_AT`; there is no general rule for other short-note runs.

## Not checked this cycle

Harp, timpani and percussion technique were not measured (MANUAL-GAPS lists harp velocities, the tam-tam key and the cymbal rows as checked and consistent). I did not read `cycles/c52/metrics/metrics.md`, did not compare with the reference recordings, and did not enumerate the item 22 rows. The lists of string same-pitch repeats with dips under 1 dB that my first script produced are not reported: the window missed dips that fall at the score beat. On the Violas' half-plus-quarter chord repeats in bars 62-67 a second measurement showed dips of 4-8 dB.

Do not touch: the legato rows' note handling (no chords, no same-pitch overlaps); keyswitch placement (about 14 ms before the note-on); the slurred short string notes on Sus MAX (join dips 0.4 dB); `REP_SPLIT` gaps and `RR_RESET_AT`; pizzicato, tremolo and string staccato rows; `HARP_VEL_MAX` 123; the celli CC1 map (neutral on joins); the Violins I sf at 78; the Clarinet 1 accent fix at 414 and 422 (front minus body now -9.8 and -13.8 dB); accent settings in general (no track has a brighter front than body except Flute 1 at 160); the breath before 636 (master dip 3.9 dB, audible); wind and brass repeated-note separation (3.6-13.4 dB); the fugato staccato rows in bars 88-96; the Violas' chord repeats in bars 62-67; the positions and velocities of the protected re-bow rows and the final-chord fills; the Flute 1 and Flute 2 landings at 633, 640 and 643.5.
