# Cycle 21, critic A: articulation and phrasing (on the c20 render)

Every number below comes from `cycles/c20/render/` (stems and master), the c19 and c18 stems for comparison, `build/parts.json` (the c20 data), `cycles/c20/before/parts.json` (the c19 data), and the installed `.oib` patch files, which I read as JSON and did not change. "Measured" means a number taken from these files. "Inferred" means a conclusion that needs a render to check. Nobody heard the audio. Nothing below proposes a per-note move in the track volume envelope. Every fix is in CC11 / CC1, region gains, release times, rows, note lengths, or a held phrase level.

Two notes on the brief. First, the coordinator's list "Findings from the other movements. Check each against our render ..." ends with the colon in my task file, and no items follow it, so I could not check them. Second, `loop/MANUAL-READING.md` has no row for cycle 21 (its third round covers c13-c20). As the task says, I skipped the fixed reading and read the pages behind my findings instead.

## Manual notes

| Manual (May 2021 HO, PDF page) / patch file | Where it applies | Does the render follow it |
|---|---|---|
| p.70, Harp individual articulations: "Harmonics ... hollow, transparent ... the fundamental is completely missing"; "Gliss Technique ... the fingers slide gently over each string to produce a glissando ... individual notes". The Harp KS Master has both as rows ("Harmonics", "Gliss Technique", plus "Sus RR"). | Harp: the printed harmonics at qn 168 / 176 / 184 (bars 43-47, "harm. (sound 8va)"); the glissando at qn 1106-1108 (bar 277) | **No.** The track loads "Harp Sus RR", so the harmonics play as ordinary plucks and the glissando plays as 16 ordinary plucks (finding 4). |
| p.69, Harp Sustain RR: alternates pluck and thumb by round-robin, with nail at velocity 124-127 | the whole harp part | Followed. Every velocity is 116 or less. |
| p.89-90, Divisi: DIV A / DIV B patches are one chair of each stand, Close mic only; "the loudness of a divisi part is not much less than if the whole section were playing the part" | the div. chords at 888 and 1088-1116, Violins I "4 soli" at 473-488 | Not used (MANUAL-GAPS #7, memory). Since c16, `CHORD_CUTS = False`, so 2- and 3-note div. chords play at 2-3 full sections. See "Other checks" for why I do not propose restoring the cuts now. |
| p.96-97, Strings: the sustain and tremolo rows do not respond to velocity; CC11 sets loudness | the celli's re-bowed repeats (finding 5), tremolo | Followed. Velocity is not used for string re-attacks. |
| p.101, Brass Sustain: "all 4 dynamic layers start to play simultaneously ... controlled by the Mod Wheel"; Sustain Accent: velocity sets the attack | the trombones' and horns' CC1 lifts in c20 (finding 6) | The CC1 lane behaves as the manual says, but the patch tables (below) show that a CC1 offset inside one layer's plateau changes the level very little. |
| `1TP KS Master.oib`, "Sus Non Vib MAX" / "Leg Slur MAX" / "Mute Sus": sustain groups release 178 ms at f / ff and 237 ms at p / mf; the RT groups have a 148 ms attack and source volume 0.47-0.95. `1TB` "Sus MAX": 237 ms at every dynamic, RT 1.22-1.76. `1FH`: capped at 237 ms (mix.json). | trumpet note ends (finding 3) | The trumpets are the only brass that stop dead (finding 3). |
| `EH KS Master.oib` "Leg Slur MAX": the "TLeg" transition groups have attack 54 ms, hold 412 ms, then decay 177 ms to sustain 0. The "EHs" sustain groups under a legato target have **attack 465 ms**. The first-note "EH" groups have attack 8 ms. | cor anglais legato targets (finding 2) | This patch design is the cause of the bloom (finding 2). |
| `CL KS Master.oib` "Leg Slur" / "Sus Non Vib": CC1 crossfades three layers. The mp layer covers CC1 52-76 alone, and its amplitude rises only from 0.77 to 0.98 over that range. | clarinets 151-170 (finding 6) | It explains why CC1 +6 did nothing there. |

MANUAL-GAPS: the harp's Harmonics and Gliss Technique rows are a new gap (the list has no harp item). Item 7 (DIV A / B) is still deferred.

## Findings, ranked by what a listener would gain

### 1. The basses' hammered eighths now separate, but they lost 3-9 dB of level, not 2.5 (measured; the fix values are partly inferred)

Where: Double basses, "Stac On Bow RRx9", qn 792-840 (bars 199-210) and 984-1088 (bars 247-270). The note data is identical in c19 and c20 except the length (0.35 -> 0.30 qn). CC11 medians are also the same in both: 107 / 88 / 97.5 / 84 over the four spans.

Measured on the stems, c19 -> c20. I give the RMS of the span and the 90th percentile of 20 ms frames (the stroke peaks):

| span | printed | CC11 | RMS | stroke p90 |
|---|---|---|---|---|
| 792-816 | ff | 107 | -33.5 -> -38.1 (-4.6) | -29.7 -> -33.9 (-4.2) |
| 816-840 (accel.) | f | 88 | -35.8 -> -45.0 (-9.2) | -31.7 -> -41.0 (-9.3) |
| 984-1056 | ff | 97.5 | -32.5 -> -36.2 (-3.7) | -28.8 -> -31.7 (-2.9) |
| 1056-1088 | | 84 | -36.7 -> -42.6 (-5.9) | -34.1 -> -38.8 (-4.7) |

In 205-210 the basses went from 3.4 dB over the celli to 5.8 dB under them. Separation is excellent now: true same-pitch repeats dip 18.5 / 13.3 / 17.1 / 16.6 dB, and none of 322 dips under 3 dB. So the c20 change itself is right; only the level is missing. The loss is largest where the strokes are shortest: in the accelerando, the extension used to supply most of the level.

Fix (Opus state, so a full rebuild of Double basses):
- `build/mix.json`, Double basses `region_gain_db`: change the entry `{"rows": ["Stac On Bow"], "all_db": -1.5}` to `+2.5` (+4 dB). The row volume knob does not act (c19 learning). Leave the release-extension entry at -60 dB and the 90 ms cap.
- `build/score_config.py`, c20 block: add `_sc20.setdefault("Double basses", []).append({"lane": "cc11", "k": 47.0, "pts": [(815.7, 0.0), (815.73, 5.0), (839.7, 5.0), (839.73, 0.0)]})`, which takes the lane from 88 to about 113. The k value is the c20 actor's soft-string value; its slope on this short row is inferred, so check it.
- Pass: in each span the stroke p90 within 1.5 dB of c19, and the dips still 10 dB or more.

### 2. Cor anglais solo (bars 171-186): every legato target still blooms about 5 dB, because the patch fades the sustain in over 465 ms under a transition sample that sits about 5 dB lower (measured; fix inferred)

Where: Cor anglais, "Leg Slur MAX", qn 680-744. Trumpet 1's "Mute Sus" doubles the line.

Measure: level from 0.05 s before the beat to 0.10 s after it, against the peak over +0.2..+0.6 s (100 ms windows).
- Cor anglais legato targets at velocity 80-90: +4.5 to +6.9 dB (692 +6.5, 704 +6.9, 706 +5.5, 708 +5.0, 720 +5.5, 728 +4.5, 736 +6.4, 738 +6.5). The median over the passage is +4.9 dB (c19 +5.3).
- Slur first notes at velocity 53 (680, 712): +0.7 / +0.8 dB.
- The muted trumpet on the same notes: median +0.6 dB.

The median target shape, from the moved note-on, relative to the body at 0.5-0.7 s: -2.1 dB at 0.00 s, -5.2 at 0.10, -5.4 at 0.15, -4.4 at 0.20, -2.7 at 0.30, 0.0 at 0.40.

Cause, from the patch file: on this row the legato target is a "TLeg" transition sample (54 ms attack, 412 ms hold, gone by about 0.64 s) plus the "EHs" sustain, which fades in over 465 ms. The transition is about 5 dB under the sustain body, so the note swells for 0.4 s. A first note uses the "EH" groups, with an 8 ms attack, and does not bloom. This also explains why c19's CC11 dip of 10 units removed only 0.9 dB: CC11 scales both samples together.

Fix (Opus state, one track; range test 676-748):
- Variant A, existing tool: in `build/mix.json`, add to Cor anglais `region_gain_db` the entry `{"rows": ["Leg Slur MAX"], "groups": ["TLeg"], "all_db": 4.0}` (`region_gain()` matches group names by substring).
- Variant B, only if A makes the slur sound too heavy: a new mix.json key `attack_set_ms` in `tools/build_reaper.py`, modelled on `cap_release()`, that sets the "EHs" groups' AHDSR attack from 465 to 180 ms.
- In both variants, remove the `INSTR_POST["note_shape"]` "Cor anglais" entry (score_config.py near line 1810, the -10 units over 680-744).
- Keep a variant only if the targets' rise falls to 2.5 dB or less and the join dip stays at 4 dB or less.

Extension: the same row design gives Oboe 1, Clarinet 2 and Bassoon 1 targets a median bloom of +3.1 / +3.5 / +3.5 dB (all passages, crescendos included; measured). If variant A holds, try TLeg +2 dB on those tracks.

### 3. Trumpet note ends are cut off because their f / ff sustain release is 178 ms, not because the trails are weak (measured; the target values come from the measured trombone and horn curves)

Measured: median level after the note-off, relative to the last 0.1 s of the note, for notes followed by 0.6 s or more of rest (25 ms windows):

| track, row | n | +0.10 s | +0.15 | +0.20 | +0.25 | +0.30 |
|---|---|---|---|---|---|---|
| Trumpet 1 / 2 / 3, "Sus Non Vib MAX" | 8 / 8 / 10 | -10.2 / -12.6 / -11.9 | -22 / -24 / -24 | -39 / -40 / -41 | -45 / -44 / -46 | -49 / -48 / -50 |
| Trumpet 1, "Leg Slur MAX" | 3 | -9.0 | -16.2 | -35.1 | -45.8 | -48.3 |
| Trumpet 1, "Mute Sus" | 2 | -5.3 | -11.7 | -22.7 | -52.4 | -64.3 |
| Trombone 1 / 2, "Sus MAX" (release 237 ms) | 16 / 19 | -5.8 / -6.4 | -9 / -11 | -15 / -17 | -19 / -21 | -23 / -25 |
| Horn 1 / 3, "Sus MAX" (capped at 237 ms) | 19 / 22 | -6.9 | -11 / -12 | -19 / -16 | -25 / -19 | -27 / -21 |
| Tuba, "Sus MAX" (163-183 ms) | 21 | -9.1 | -15.7 | -19.4 | -23.7 | -30.3 |

The trumpets fall off a cliff between +0.15 and +0.20 s, which is where the 178 ms release ends. The trombones and horns are still at -15..-19 dB at +0.2 s because their 237 ms release is still running. What remains of the trumpets after +0.25 s, at -45 dB, is the trail: c20's +6 dB on the RT groups moved it by exactly 6 dB. Raising the trails again therefore cannot fix the first 0.25 s. The muted solo has the same edge at +0.25 s (237 ms at p). The tuba keeps its tail with a release as short as the trumpet's because its RT groups are 1.0-3.98 in source volume, against the trumpet's 0.58-0.91.

Fix (Opus state, so full rebuilds of Trumpets 1-3):
- `tools/build_reaper.py cap_release()`: add a spec key `"set": true`, so that `pr_["release"] < ms_` is also written. Today the function only lowers.
- `build/mix.json`, Trumpets 1-3: `sus_release_cap_ms` `{"ms": {"p": 300, "mf": 300, "f": 300, "ff": 300}, "rows": ["Sus Non Vib MAX", "Leg Slur MAX", "Mute Sus"], "set": true}` (Mute Sus on Trumpet 1 only). This sets the "1V" and "1Tps" sustain groups; pp keeps its 316 ms, and RT and TLeg groups are skipped as they are now.
- Expected (inferred from the trombone curve with the release scaled from 237 to 300 ms): -12..-15 dB at +0.2 s and -18..-22 at +0.25 s, then the trail.
- Range test: Trumpet 2 alone, 792-816. Pass if the median at +0.2 s is -14..-20 dB and the master stop at 814 (+0.3 s) stays at 14.4 dB or more. Keep c20's RT +6 dB; it is harmless.

### 4. The harp's printed harmonics (bars 43-47) play as ordinary plucks, and the glissando (bar 277) as 16 thumb / finger plucks (measured in the data; the improvement is inferred)

Where: Harp, notes at qn 168 / 176 / 184 (B flat 4 sounding, velocity 46, 6.6 qn each, printed "harm. (sound 8va)" with flageolet circles, p, solo over the pp strings at the transition). The glissando is 16 notes at qn 1106.0-1107.77 (G3 to E6, velocity 90-112, each held 4.8 qn) into the final chord. The track loads "Harp Sus RR" (`art_counts` "null": no rows at all).

Manual p.70: Harmonics is "hollow, transparent ... the fundamental is completely missing", and Gliss Technique is built for exactly these written-out glissandi. Both are rows of `Hollywood Harp Opus Instruments/04 Keyswitch/Harp KS Master.oib`, next to "Sus RR". The Harmonics samples cover keys 48-96, and they "produce the same pitch", so the sounding pitch 70 that the extraction already writes (`\harmOctF`) is the right key.

Fix (patch change, so a full rebuild of Harp; with `UNLOAD_UNUSED_ROWS` only 3 rows load, so the memory cost should be small; check the settled footprint):
- In `build/score_config.py` TRACKS, set the Harp patch to `Harp KS Master.oib` with the default row "Sus RR".
- Add `ART_SPANS["Harp"]`: "Harmonics" for score onsets 168-188, and "Gliss Technique" for 1106.0-1107.9. The keyswitches come from `ks_maps.json` / `ks_maps_extra.json`; run `dump_ks.py` if the KS Master is missing from them.
- Keep the velocities: the Harmonics row has 2 velocity layers and Gliss Technique has 3 (p.70).
- Check: the 168 note's spectrum should lose its fundamental (B flat 4 band 10 dB or more under the 2nd partial). Also check the harp's level at 168-190 against c20 (-50 dB median at p); set a region gain if the Harmonics row comes out more than 3 dB away.

### 5. The celli's re-bowed same-pitch repeats do not separate: median dip 2.2 dB, 15 of 26 under 3 dB (measured; fix inferred)

Measure: true same-pitch repeats only (no other note of the track sounding in the gap), 150-3000 Hz band, the new note's peak in its first 0.15 s against the floor 30 ms before to 20 ms after its moved note-on. On the same measure:

| track | n | median dip | under 3 dB |
|---|---|---|---|
| Violoncellos | 26 | 2.2 | 15 |
| Violas | 99 | 7.4 | 12 |
| Clarinet 1 / 2 | 20 / 13 | 9.2 / 12.2 | 0 |
| Trombone 1 | 10 | 7.2 | 0 |
| Double basses | 322 | 16.8 | 6 |

Where in the celli: 70 and 98 (G2, F1's bass line, "Leg BC MAX" -> "Sus MAX", 90 ms gap, dips 0.6 / 1.0 dB), 325, 361.5, 365.5 (1.5-1.9 dB), 437 (21 ms gap, 0.5 dB), 564, 604. These are the `STR_REP_NEW_BOW` "stroke" and "sus_min_s" classes. They get a 90 ms gap (c16 research) but no CC fall, so the old note's 150 ms capped release is still sounding when the new "Sus MAX" note starts (c17 learning: its slow start).

Fix (score_to_parts.py plus config; no envelope):
- Give the "stroke" and "sus_min_s" new bows the same CC11 fall that the "portato" class already has.
- `build/score_config.py`: `STR_REP_NEW_BOW["stroke_fall"] = {"fall_cc": 10, "fall_cc_loud": 12, "fall_s": 0.06}`. In `tools/score_to_parts.py`, apply the portato fall code (the `fall_cc` / `fall_s` path of `STR_REP_NEW_BOW["portato"]`) to these classes when `stroke_fall` is set.
- The lane must return to its value by the new note-on, so the new attack is not lowered.
- Expected (inferred): about 7 dB off the tail. Hollywood Strings loses about 0.7 dB per unit under CC11 100 (c18). Pass if the celli median dip is 5 dB or more, with no new hole over 6 dB in the master at these onsets.

### 6. Three of c20's level lifts used CC1 inside a layer's plateau, where the patch barely changes level. Do them in CC11 (measured from the patch tables and the render)

Read from the patch tables (layer amplitudes by CC1):

- **Clarinets** (`CL KS Master`, "Leg Slur" / "Sus Non Vib"): the mp layer alone covers CC1 52-76 (0.77 -> 0.98). In 600-680 the lane moved 61.5 -> 68 (+6.5), which is about +0.4 dB in the table. Measured: Clarinet 1 -45.0 -> -45.1 dB over 600-680. In 40-104 the stem rose 3.0 dB (-48.8 -> -45.8), but that rise matches the deleted -2.5 dB role row; CC1 added about 0.4.
  - Fix: in the c20 block, replace the clarinets' `_nc20` cc1 `add 6` at 600-680 with `_sc20` `{"lane": "cc11", "k": 40.0, "pts": [(599.7, 0.0), (599.73, 3.0), (679.7, 3.0), (679.73, 0.0)]}`. CC11 is the volume on this patch at 40 log10 (c18 learning), and the lane goes from a median of 72 (max 97) to 86 (115).
  - Expected (inferred): Clarinet 1 / 2 at -6.5 / -5.8 dB under Violins I there.
- **Horns 3 / 4** at 844-857: the lane moved CC1 86-90 -> 92-96. In the `1FH` table f + ff sum to 1.29 at 86 and 1.26 at 92: no change.
  - Fix: remove that `_nc20` cc1 add. Add `_sc20` cc11 k 40, +6 dB over 843.9-857 (CC11 83 median / 88 max -> 117 / 124; the lane has room).
- **Bassoon 1 and celli**, same counter-line: their lanes are near their tops (Bassoon 1 CC11 87-92: +3.9 dB at most at k 33; celli 93.5 on "Sus MAX", which is flat above about 103). Give them the remaining lift as held phrase levels (role rows over 844-857, allowed by the standing rule): Bassoon 1 +2.5 dB on top of its current +4; celli +2 dB on top of their +5. Target: 5 dB under the trumpets (now 11-12).
- **Trombones 1 / 2** at 792-816: CC1 99 -> 105 sits in the f / ff crossfade (0.59 / 0.60 -> 0.44 / 0.73), and it bought +0.8 dB (3.1-3.8 -> 2.3-3.0 dB under the trumpets).
  - Fix: keep it, and add `_sc20` cc11 k 40, +1.5 dB over 791.9-816 (CC11 100 -> 109, max 111 -> 121). Target: within 2 dB.

## Coordinator's c20 items, through this lens

- **Climax crests: what makes the peaks (measured).** In the master's peak sample, the stems' signed values are:
  - qn 890.5 (bar 223, 1.4 s into the fff chord, not the attack): Bass trombone +0.172, Trombone 2 +0.178, Trumpet 2 +0.101, Violins II +0.083, and smaller ones. The master is -0.15 dBFS.
  - qn 1109.5 (final chord, 0.66 s in): Violins II +0.173, Trombone 1 +0.148, Violas +0.146, Violins I +0.068.
  - qn 1049.8: Bass trombone and celli.
  - The peaks are chance sums in the body of dense chords, not attacks, and no stem dominates. Simulated on the stems (the stem sum equals the master to 0.01 dB), cutting one family lowers the peak by no more than the loudness: Bass trombone -3 dB gives momentary -0.05 / peak -0.04 at 223; low brass -2 dB gives -0.21 / -0.13; Violins I + II -2 dB gives -0.28 / -0.14 at 223 and -0.54 / -0.10 at the final chord; crash -3 dB gives -0.20 / -0.02 at the final chord.
  - So **no instrument-side crest reduction exists here**. Every cut costs more loudness than it saves in limiting. The limiter load is a delivery-stage question (a slower pre-limiter compressor). Do not lower the climaxes' instruments for it.
- **Tremolo region gains (deferred in c20): do not do them now (measured).** The tremolo chords are the strings at 888 and 1108. A -2 dB violin cut takes 0.54 dB of momentary loudness off the final chord and only 0.10 dB off its peak, against a final-over-223 margin of 0.1 dB.
  - Restoring the div. chord counts as CC7 (-10 log10 k) would be more faithful to p.89-90. Simulated, it takes the final chord -1.37 dB momentary and -0.84 dB peak, against -0.18 / -0.06 at 223, which reverses the climax order.
  - Revisit both only together with a brass or percussion lift at the final chord.
- **Violins / violas 1-2 dB louder in bars 1-10: a round-robin take, not variance in level (measured).** Over qn 0-40, c20's Violins I stem correlates 0.998 with c18's (difference -24 dB re the signal), and c19's correlates 0.016 with both. Violins II: 0.997 / 0.039. So c19 played the other take of the opening "Sus MAX" chords, and c20 is back on c18's. The per-bar changes mirror exactly (bar 1 -2.9 / +2.9, bar 2 -3.1 / +3.1, bar 9 +1.6 / -1.6). Treat c20's level as the normal one and fit nothing on c19's bars 1-10.
- **Cor anglais qn 600, -1.5 dB over 0.5 s.** This is the bar-150 `vol_set` point (599.0 -> 600.0, `_b150`) moving inside the cor anglais note that joins into 600. Fix: drop "Cor anglais" from that loop's track list, or end its ramp at the note-on 599.95. The cor anglais has no bar-150 gain in `_b150`, so the point only returns to 0.
- **Trumpet trails:** finding 3. **Basses' level:** finding 1. **Clarinets 151-170, counter-line 212-215, trombones 199-204:** finding 6. **Cor anglais "Leg Slur MAX":** finding 2. That finding replaces the deferred row-change design, because the cause is the patch's 465 ms sustain attack, not the row.
- **Master LRA 22.8:** a balance and dynamics question, not this lens. Nothing above changes the pp-ff span by more than 1 dB.

## Other checks (measured unless marked)

- **Tremolo rows:** all 43 printed tremolo onsets (888-1112, all five sections) are on the "Tremolo" row.
- **Loop pulsing:** no string or wind note lasts 5.6 s or more (the re-bows split them). The longest are Horn 4 at 168 (6.5 s), Horn 2 at 152 (5.8 s), and timpani rolls of 5.7-7.0 s. The four long rolls show no periodicity: the residual autocorrelation peaks at 0.16-0.29, at 0.8-2.6 s lags.
- **Brass accents, 247-262 (984-1048):** 2-5 kHz over the first 80 ms against 120-300 ms. Accented: median -10.6 dB (n 20). Unaccented: -11.9 (n 124). No family burst. One outlier: Trombone 1 at 985, "Leg Slur MAX" velocity 118, +8.3 dB (+2.4 on the beat-aligned window). The other three velocity-118 heads (993 / 1001 / 1009) read -5.7..+0.5. Not worth a rule.
- **S2, detached brass onsets** (-3 dB point against the beat, notes with no note sounding 60 ms before): in 984-1080 the brass sit at -10..+52 ms and the timpani at +26. The outlier is the Tuba at 792-840: +95 ms (IQR +45..+129), on whole notes at velocity 83 with a 0.07 s lead; in 984-1080 it reads +37. Proposed: Tuba lead 0.07 -> 0.14 s on 792-840 in `entry_leads.json`. Inferred: the low "Sus MAX" notes speak slowly at velocity 83.
- **S1 elsewhere:** trumpets dip 7.5-11.4 dB, Bass trombone 10.3 and Contrabassoon 10.1 (0 under 3 dB). The violas' 12 weak repeats are div. Sus-to-Sus chords at 50-60 ms gaps (826, 850); they are chords, outside `STR_REP_NEW_BOW`'s monophonic rule, so finding 5's fall would reach them only if the rule is extended to chords.
- **Violins I "4 soli" (473-488):** octave pairs on the full-section "Sus MAX" at velocity 41 with the -7 dB player-count level. A DIV A track (p.89-90) would be closer to four players, but it needs the second pass (MANUAL-GAPS #7). Not ranked.

Do not touch: the basses' muted release extension and 90 ms cap (separation 13-18 dB); the CC16 reset before each celli pluck and the celli pizzicato table; the chorale overlaps and staggered same-pitch gaps; "Mono From Left" on Horns 1 / 3; the entry lead cuts; the fff caps, steps and holds at 888 / 1048; the brass and woodwind accent amounts (no family burst, Dan: no general raise); every tremolo on its row; the open Trumpet 1 solo's legato rows; the muted "Mute Sus" line (flat against the cor anglais).
