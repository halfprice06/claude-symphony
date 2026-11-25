# Critic A, cycle 54: articulation and phrasing (review of the c53 render)

Data: `cycles/c53/render/*.wav` (stems after the stem fix, master), `cycles/c53/render_first/` where a corrected stem matters, `cycles/c53/rendered_build/parts.json` and `rendered_build_pass2/parts.json` (notes, keyswitches, CC lanes as rendered), the c49-c52 renders for comparison, `build/score_config.py`, `build/*.json`, `build/mockup-events.tsv`. Times come from `pcx.TM(parts["tempo"]).sec(qn)` without the pre-roll (coordinator fact 4). Onsets are band envelopes of the note's own harmonics with the neighbouring pitch's harmonics excluded (fact 5); pcx was not used alone. Bar b starts at qn 4(b-1). Every number is measured on the c53 files unless marked inferred.

## Manual notes

Third round: own choice of pages (May 2021 manual, PDF pages), taken from this cycle's findings.

| Manual says | Page | Where it applies here | Does the render follow it |
|---|---|---|---|
| String Sustain has a bow-direction round robin that alternates up-bow and down-bow samples on each note. | 91 | Every re-bow piece of a held string note; the Double basses' final C (qn 712-728). | No at the final chord: the two bow samples differ by 3-5 dB, the fills in `rebow_fills.json` were fitted to the other phase, and the pieces now step by 6-10 dB (finding 2). |
| "Opus remembers which sample should be played the next time a note sounds"; RR Reset exists so that playback is the same every time. | 145 | `RR_RESET_AT` (CC16) on the Double basses since c52; the pre-roll reset on every track. | Partly. The resets at 104-664 changed which sample every later bass note of that pitch gets; nothing after 664 was re-fitted (finding 2). The Violins I Staccatissimo stroke at 116.0 plays another sample than in c50/c51 with unchanged data (finding 3). |
| Staccato and Staccatissimo are round-robin instruments with 9-16 sample sets. | 94 | Violins I bar 30 (4 strokes), bars 94-96; Stac RRx9 on the other strings. | Yes for the row choice. One of the sets has a much faster start than the others (finding 3). |
| On true-legato instruments velocity sets the transition time (50-60 longer, 110-127 shorter) and not loudness. | 144 | Cor anglais solo bars 5-8 (targets v80-90); every legato target. | Followed. The hole at qn 26 is not a velocity effect: the same v80 target had no hole in c50/c51 at CC11 73 and has one at CC11 87 (finding 1). |
| A slur is played only when there is no significant gap between the notes; legato instruments are monophonic. | 99, 112 | All Leg rows. | Yes: 0 chords on legato rows on all 42 tracks, every legato target overlaps its predecessor (median 19-21 ms). |
| Tam-tam: C1 = long, 12 velocity layers; velocity and CC11 set loudness. | 118 | Tam-tam qn 484 (fff) and 696 (pp, l.v.). | Yes for key and velocity. The pp note ends at qn 709.7, before the printed "damp" at 724 (minor, listed under "Checked"). |

## The coordinator's open items in this lens

| Item | Measurement | Verdict |
|---|---|---|
| Cor anglais 275: +158 ms (c52), -84 ms (c53) | Note-on 166 ms before the beat. A-flat band within 3 dB of its plateau at -60 ms; A-flat passes the B-flat at -20 ms; t50 -65 ms, 10 dB point -110 ms. The B-flat eighth before it (Sus MAX, 235 ms written) sounds alone for about 145 ms. | Confirmed early, by 40-65 ms on three measures (not 84). Reduce `retongue_leads` 275.0 from +0.06 to +0.02 as proposed (finding 4). |
| Oboe 1 582: -52 ms by pcx | D5 passes the E5 at -30 ms and reaches its body at +60 ms; t50 +25 ms. The 10 dB point (-125 ms) reads the old note's fade. | Rejected. No row. |
| Four Lento re-bow rows over the limits | Violoncellos 21.442 and Double basses 26.003 pass on their own stems; the master dips there belong to the cor anglais solo, which is 15-20 dB over every string stem in bars 6-7: at 21.4 the held B-flat wavers 2-4 dB, at 26.0 its legato join has a 7 dB hole (finding 1). Violoncellos 12.163 and Double basses 47: master 2.7 dB on my measure (limit 3.1). | Close all four as string re-bow items. Fix the cor anglais join instead. |
| Bar-14 horn ending, 0.48 s to -20 dB: too long? | The master is 15.4 dB down at 0.3-0.6 s (BRIEF S4 asks at least 13). A hall with a 1.5-2 s decay reaches -20 dB after 0.5-0.67 s. | Not too long (inferred from the decay arithmetic; the level is measured). No change. |
| Trumpets 1-3 release | No new measurement. The note lengths and note-offs are as printed; nothing on the MIDI side shortens the release. | No articulation proposal. The patch-side candidates of c53 (releaseDamping 0.8, sustain release 178 -> 237 ms) need the range test. |
| Oboe 1's front at 160, 3 dB lower than c52 on unchanged notes | First 150 ms of the G5 on three renders of identical notes: c51 -41 to -43 dB, c52 -36 to -37, c53 as rendered (with the +3 dB bump) -36 to -38. The underlying note moved +6 dB (c51 -> c52) and -3 dB (c52 -> c53). | Single-note sampler variation (fact 3). Do not fit this front closer than ±3 dB. |
| Double basses at 704-712 differ from c50, equal c52 | It is a run: 708 -4.4, 712 -2.6, 714.67 +3.2, 718.17 -2.8, 720.0 +3.5, 722.67 -1.7, 724.8 +1.2, 726.08 -1.2 dB against c51, alternating in sign. | A state change, not variation: the bow-direction round robin is in the other phase since c52's CC16 resets (finding 2). |
| First bar-30 staccato against Violins I | Winds: first staccato lands like their other three (t50 +20 to +35 ms). Violins I: stroke 1 is 60-80 ms earlier than strokes 2-4. | The winds are right; the violins' first stroke is early (finding 3). Flute 1's 115.5 note covers the first wind staccato (finding 5). |
| Finale item 18 on the basses | Not concluded. On my front measure (160 ms from the beat) the downbeat-minus-off-beat difference is +0.4 / -0.2 / +0.4 / -0.5 dB at 104 / 112 / 520 / 528 and -2.2 dB at 664-676, where c52 aimed at +2.0. The measure is not the one c52 fitted with, so I give no row. | Open; re-measure 664-676 with c52's own script before changing anything. |

## Findings, ranked

### 1. Cor anglais solo, bar 7: the peak note of the hairpin has a 7 dB hole for its first 340 ms (measured)

Where: Cor anglais, qn 26.0 (G4 to A-flat4, slurred; printed crescendo 24-26, diminuendo from 26, "espr."). The cor anglais is the master here: its stem is within 0.3 dB of the master and 15-20 dB over every string stem.

What is wrong: the G4 before the join sits at -31 dB (harmonic band 33-34 dB). The A-flat arrives at -20 ms at 27 dB and stays at 25-28 dB until +320 ms; it reaches 35.7 dB only at +370 ms. Broadband: -31 dB before, -38.6 dB at +50 ms, -38.7 dB at +200 ms, -29.3 dB at +350 ms. Master dip 5.6 dB. The printed peak of the phrase is therefore its softest moment. The hole came with c52 and is the same in c53 (stems equal to 0.1 dB): c52 raised CC11 at the top of this crescendo from 73 to 87 (`dyn_curve`), with the notes, velocities, CC1 and volume lane unchanged. In c50/c51 the same join rose without a dip (-40 -> -37.6 -> -34.5 dB). At CC11 87 the sustain before the join plays a louder layer and the legato target does not follow for a third of a second (cause inferred; the levels are measured). The volume lane adds to it: it falls from +7.40 dB at 25.93 to +3.23 dB at 26.18, inside the hole.

This is also what c53 carried as "Double basses 26.003, master 4.8 dB".

Fix:
- `build/early_fills.json`, "Cor anglais": add `"26": {"db": 5.0, "pre_s": 0.0, "hold_s": 0.33}` (the form of its rows at 612, 684, 687.5).
- Keep the volume lane from falling during the join: the ramp that starts at 25.93 should start at 26.30 (0.36 s after the beat at 50 bpm). The +7.4 dB there is the `hpgain` [24, 26, 3.0] plus the `LEVEL_SHAPES["Cor anglais"]` row at config line 2712; move the end point of whichever ends at 25.9.
- If the fill needs more than 6 dB, lower the CC11 top for this one hairpin to about 80 instead (the layer step is the cause).
- Check after the render: stem dip at 26.0 at most 3 dB (median over -0.4..-0.2 s against the minimum in -0.2..+0.25 s, 40 ms RMS); master dip at most 2.5 dB; A-flat band within 3 dB of the G band by +100 ms.

Same kind, smaller, same solo: qn 24.0 (A4 to G4) dips 5.7 dB for 170 ms.

### 2. Final chord: the Double basses' re-bow pieces step by 6-10 dB where a diminuendo is printed (measured)

Where: Double basses, C2, qn 712-728 (bars 179-182, "change bow at will", diminuendo from 720 to ppp at 724, fermata). Re-bow pieces start at 714.671, 718.171, 720.004, 722.671, 724.803, 726.078.

What is wrong: level of each piece (0.4 s after its start to 0.1 s before its end), stem, dB:

| piece | 712.0 | 714.67 | 718.17 | 720.00 | 722.67 | 724.80 | 726.08 |
|---|---|---|---|---|---|---|---|
| c50 / c51 | -58.4 | -58.2 | -53.7 | -55.0 / -54.0 | -59.9 / -59.5 | -59.7 | -60.0 |
| c52 = c53 | -61.0 | -55.0 | -56.8 | -50.5 | -61.2 | -58.5 | -61.2 |

Steps in c53: +6.0, -1.8, +6.3, -10.7, +2.7, -2.7 dB. The C2 band alone: 11.7, 17.6, 15.7, 22.4, 12.0, 14.8, 12.0 dB. The master at 40-160 Hz was monotonic in c49-c51 (-53.2, -56.1, -56.4, -56.5, -60.2, -60.3, -63.6 dB in c51) and in c53 reads -53.5, -55.0, -59.5, -53.7, -60.5, -61.6, -63.4: a 5.8 dB rise at bar 181, where the diminuendo starts, and a 6.8 dB drop 3.2 s later. The other four string sections fall smoothly there (Violins II 14.8, 14.7, 15.3, 16.1, 12.6, 11.4, 8.3 dB).

Cause (measured as the alternating run in the table above; mechanism from manual p.91 and p.145): c52 added CC16 round-robin resets on the basses, the last at 664. Each later C2 gets the other bow sample than before. The six fills in `build/rebow_fills.json` ("714.671" to "726.078", up to +9 and +15 dB) were fitted before c52 to the other sample of each piece, so each fill now adds to the difference it was made to remove. The same flip shows at 568 and 570 (-5.9, -6.3 dB against c51), 676 (-3.0), 172 and 180 (+2.9, +5.7).

Fix:
- `build/score_config.py`, `RR_RESET_AT["Double basses"]`: add 712.0, so the phase of the final chord no longer depends on what was played before it.
- Refit the six fills with `tools/fit_rebows.py --only "Double basses:714.671"` (and the other five) `--fine` on a primed range render taken 45 s after the build, then verify on the full render (c53's cor anglais row showed that a range fit can fail to carry over).
- Check after the render: stem pieces from 712 to 720 within 2 dB of each other, each piece from 720 on at or under the one before; master 40-160 Hz never rising by more than 1 dB from 712 to 728.
- State check for c55: compare the basses against c51 as well as c53, pitch by pitch, to find other notes whose per-note trims were fitted to the other bow sample (568, 570, 676, 172, 180 are the candidates).

### 3. Violins I, bar 30: the first of the four staccatissimo eighths is 60-80 ms ahead of the other three (measured)

Where: Violins I, qn 116.0 (B-flat5), Staccatissimo RRx9, f. Strokes at 116.0, 116.5, 117.0, 117.5, all with a 45 ms lead and v95.

What is wrong: time from note-on to 10 dB under the peak / to the peak, in ms: stroke 1: 5 / 15; strokes 2-4: 75 / 120, 55 / 150, 60 / 130. Against the beat, stroke 1 reaches -10 dB at -40 ms and peaks at -30 ms; the others reach -10 dB at +10 to +30 ms and peak at +75 to +105 ms. The spacing of the four strokes is about 320, 240 and 215 ms where the tempo gives 238. The other seven Staccatissimo strokes of the track (bars 94-96) all read 40-55 ms to -10 dB, and the stroke at 117.5 on the same pitch reads 60 ms. In c50 and c51 stroke 1 rose over 80 ms and peaked at +35 ms; in c52 and c53 (identical to each other) it starts within 10 ms. The MIDI is identical in all four cycles, so this pitch now gets another sample of the round robin, one with a much shorter start (inferred; the pre-roll reset moved to CC16 in c52). The winds' first staccato is at +20 to +35 ms (t50), so the violins lead the doubling by about 65 ms on the first note and are with it on the next three. In the master's 1.5-8 kHz band the bump before the beat is 2-4 dB over c51.

Fix: `tools/score_to_parts.py` near line 3716 has only the per-track `STAC_LEAD_S`. Add a per-onset override (for example `STAC_LEAD_AT = {"Violins I": {116.0: -0.015}}`, seconds, read before `STAC_LEAD_S`), so this note-on falls 15 ms after the score time instead of 45 ms before it. Since the reset now works, the sample is the same on every render and the row will hold. Check after the render: the four strokes' -10 dB points within 25 ms of each other against their beats, and stroke 1 within 30 ms of the Flute 1 stac note.

### 4. Cor anglais 275: confirmed early; lower the row to +0.02 (measured)

Where: Cor anglais, qn 275.0 (A-flat4 after a tongued B-flat4 eighth), `retongue_leads` 275.0 = +0.06 (lead 166 ms).

What is wrong: see the open-items table. The keyswitch changes from Sus MAX to Leg Slur MAX inside the B-flat (274.617), so the A-flat is not a sampled transition but the legato row's first-note layer, which starts slowly; that is why it needs a long lead, and why the fit depends on the exact state. The A-flat is at plateau level 60 ms before the beat and overlaps the B-flat for about 80 ms.

Fix: `build/retongue_leads.json`, "Cor anglais" "275.0": 0.06 -> 0.02 (lead about 126 ms). Fit on the full render, not on a range. Accept when the A-flat passes the B-flat between -20 and +20 ms and its t50 is within ±35 ms.

### 5. Flute 1, bar 30: the slurred C6 rings over the first staccato (measured)

Where: Flute 1 main track, note at qn 115.5 (C6, Leg Slur MAX), ends at 116.000; "Flute 1 stac" starts its B-flat5 at 116.000.

What is wrong: the C6 is at -34 dB at the beat and -38 dB at +60 ms; the staccato B-flat5 peaks at -39 dB at +60 ms. For the first 60 ms the released note is 0-5 dB over the staccato a tone below it. Oboe 1's main note is 6 dB under its staccato at +60 ms and Clarinet 1's 13 dB under, so only the flute is affected. This is the item c53 deferred.

Fix: `build/score_config.py`, `BREATH_GAP_AT["Flute 1"]`: add `115.5: 0.10` (the note then ends near 115.80, about 48 ms before the staccato; the C6 written as an eighth keeps 0.36 qn). Check: Flute 1 main at least 6 dB under the staccato's peak at +60 ms, and no gap over 60 ms between the two notes on the summed pair.

### 6. Three legato joins with holes of 9-14 dB lasting 150-285 ms (measured; master dips 3-4 dB)

Sweep of 613 legato joins on all tracks (stem, 40 ms RMS; dip = lower of the levels 0.2-0.4 s before and 0.25-0.5 s after, minus the minimum between). Medians per track are 0.7-4.0 dB. Outliers that also show in the master:

| Track, qn (bar) | Notes | Stem dip | Width under -3 dB | Master dip | Fill now |
|---|---|---|---|---|---|
| Violoncellos 672.0 (169) | F4 -> E-flat4, Leg BC MAX v124, ff | 13.7 dB | 285 ms | 4.0 dB | none |
| Horn 1 415.0 (104) | B-flat4 -> A4, v100 | 12.3 dB | 145 ms | 3.0 dB | none |
| Oboe 1 95.0 and 99.0 (24, 25) | G5 -> F5, v80, CC11 96 / 110 | 12.1 / 10.8 dB | 180 / 160 ms | 3.4 / 0.6 dB | none |

On the celli the F4 fades from 75 ms before the beat and the E-flat4 reaches its level only at +285 ms. On the oboe the F5 arrives at -35 ms at full level, falls 12 dB from +45 to +165 ms and returns by +250 ms, the same shape at both places, so it belongs to that transition sample. Flute 1 and Flute 2 at 634.0 (10.8 and 7.6 dB) are 16-18 dB under the master and need nothing.

Fix: `build/early_fills.json` rows, hold-shaped like the existing ones: Violoncellos "672": `{"db": 6.0, "pre_s": 0.05, "hold_s": 0.28}`; Horn 1 "415": `{"db": 5.0, "pre_s": 0.0, "hold_s": 0.15}`; Oboe 1 "95" and "99": `{"db": 5.0, "pre_s": -0.04, "hold_s": 0.13}` (the fill must start 40 ms after the beat, after the transition's own peak; if `pre_s` cannot be negative, use a `LEVEL_SHAPES_S` row from +0.04 to +0.17 s). Check: stem dips at most 6 dB and master dips at most 2 dB at the four places. Lower priority than findings 1-5.

## Checked and in order (no change needed)

- Keyswitches: every keyswitch is 9.5-46 ms ahead of its note on all 42 tracks, none within 5 ms. No chords on legato rows.
- Slurs: of 1,274 slurred note pairs, the pairs not played as an overlapped legato target are the documented cases (same-pitch repeats, slurred shorts on Sus MAX with overlap, Slur Runs, printed down-bows after a slurred upbeat). Violins I 59.5 (a 37 ms Sus MAX note before the tenuto C5) sounds as a C5 from +50 ms with a 5-8 dB re-articulation before 60.0: as intended.
- Accents (Dan: weight, not bite): the 2-5 kHz level of every accented or sf front on a single stem is at least 6 dB under the master's 2-5 kHz level at that moment. Flute 1 at 160 still has the brightest front against its own body (+18 dB at 2-5 kHz, +7 dB full band) and is 20 dB under the master there.
- Shorts: wind Stac DblTng strokes reach -10 dB at +5 to +30 ms; bass pizzicato +5 ms (one at 592.0, +55 ms); string Stac RRx9 +10 ms median.
- Harp: the étouffez marks at 650, 658 and 727 silence the stem within 0.3 s; 224, 243, 244, 251, 268 damp one hand while the other plays. Rolled chords: the three right-hand notes are 30-40 ms apart, the left-hand octave is on the beat, as the arpeggio mark stands on the right-hand staff only. Velocities 46-112 (cap 123).
- Timpani: rolls on the roll row with restrikes, single strokes on the long row, alternate-hand keys on 18 repeated strokes. No technique finding.
- Tam-tam and cymbals: fff stroke -24 dB at 485, -35 dB at 492 ("damp gradually"), -64 dB at 504 ("damp"), -80 dB at 505. Suspended-cymbal roll peaks at 636, -79 dB at 644, silent at 650. The pp tam-tam note ends at qn 709.7 where the score lets it ring to the "damp" at 724; it is -67 dB at 708, 10-15 dB under each string section, so the cut is inaudible (inferred). If wanted: a 28 qn length for that note in `PERC_MAP`.
- Same-pitch repeats (S1): winds and brass separate by 5-18 dB in the median. Bassoon 2's long pedal repeats (476-491, 628-632, 672-676) re-attack by only 2-3 dB; they are doubled pedals under a tutti and were left.

## EW-TEMPLATE-PLAN sections this lens touches that are not applied

- Section 5, legato overlap: median 19 ms (winds), 21 ms (brass), 20 ms (strings) against 45-80 ms and 33-58 ms in the study. Legato target velocity: strings 93 % at v120 or more, brass 87 %, winds median v100.
- Section 6 (two tracks per string section), section 7 (per-note lean-off as a rule), section 8 (tutti entry spread), section 10 (beat-position velocity outside the listed spans): as in c53, not applied.
- MANUAL-GAPS still open in this lens: #5 expressive rows for the wind solos (the cor anglais solo of finding 1 is the first candidate if the fill does not hold), #9 horn portato rows, #12 recorded crescendo rolls.

## Not checked this cycle

Tremolo joins, the loop fold at 3.95 s (no held note is long enough since the re-bows), accent weight against unaccented neighbours, the reference recordings, `metrics.md`. The finale item 18 rows were measured but not concluded (table above).

Do not touch: keyswitch placement; the legato rows' note handling; the wind staccato rows and their alias level shapes in bar 30 and bars 88-96; the Violins I strokes 2-4 in bar 30 and the per-track `STAC_LEAD_S` values; the re-bow rows and refitted fills in the Lento and at 290.9 / 297 (all four open rows are closed above); the other four sections' final-chord fills; the front-weighted sf shapes at 160; the kept Flute 2 rows; Oboe 1 at 582 (on time); the harp damping rule and the roll spacing; the timpani rows; the percussion rings at 484-504 and 632-652; accent settings; the R Brass half step as far as the bar-14 horn ending is concerned.
