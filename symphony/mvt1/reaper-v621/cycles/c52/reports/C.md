# c52 critic C: dynamics over time (render under review: c51)

Lens: the shape of every hairpin and phrase, the loudness arc against the score, master and delivered loudness range (BRIEF 6), swells and loop pulsing on long notes (BRIEF 7), decays, subitos (S3), against real recordings. The coordinator gave this lens finale items 3 (sub. p), 2 (sfp / fp, dynamics side), 7 (FINAL_RING) and 4 (low-end side EQ), plus the c51 open items.

Method. c51 and c50 masters, dry stems, return stems and delivered mp3s; the c51 `build/parts.json` (identical to `rendered_build_pass2/parts.json`) and c50's `rendered_build/parts.json`. Levels are stereo power on 20 ms or 50 ms frames, or K-weighted where marked. Phrase rise is measured on each phrase's first note from its moved onset (K-weighted 100 ms windows at +0.15 s and +0.8 s). Hairpin shares come from `cycles/c51/actor_scripts/post51.py hairpins` (run read-only), plus my own list of reversed hairpins on the same measure. The loop scan is the c25 `loopscan.py` with its path set to reaper-v621. Width is `width49.py`'s measure, with the side-EQ variants simulated on the c51 stems. That simulation applies the complex RBJ biquad ratio new/old to each stem's side channel and re-sums the master; the c51 baseline reproduces the actor's 0.563 / 0.483 / 0.404 / -4.66 dB exactly. Decays use rtk's `decay_fit` and the recordings' automatic cut-off rule. References: Brahms 1/i, 4/i, 1/ii, 4/ii (stored rtk metrics) and Dvořák 9/i (decoded lossy mp3). Scratch was in `/private/tmp/claude-501/mockup-loop/mvt1-c52-C/` and has been deleted.

## Manual notes (third round: pages chosen for this lens's open problems)

| PDF page | What it says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| p.53 (2.5.7) | Shape lines the way a player does. Velocity is for short notes (it cannot change mid-note); CCs are for sustained notes, mid-note or over a phrase. | PHRASE_SHAPE, hairpins | Partly. Phrase arches exist since c51, but they switch off at every printed hairpin, so the arch and the printed swell work against each other (finding 1). Five low-wind tracks never rise above their printed level (finding 3). |
| p.63 | Every instrument fades to silence on CC11 (the Ni patches are gone). | Final ppp chord, morendo, HP_NIENTE | Yes. From the written end the final chord falls 20 dB in 0.665 s, between the soft-ending references (finding 6). |
| p.64, p.151 | CC7 or the fader sets a track's ceiling. CC11 carries the line's changing dynamics and swells "over the course of a phrase". On strings and winds CC1 is vibrato. | Level work in the volume envelope; CC11 lanes | The split is followed. SWELL_CC_CAP keeps CC11 off a layer boundary, but it throws the phrase swell away instead of moving it into the envelope (finding 3). |
| p.91-92 | String Sustain loops, with bow-direction round robins and 3 vibrato levels. Marcato Sustain adds a marcato sample at the start for "extra power". | The basses' fp at bar 33 (Sus MAX); the sub. p re-attacks at bar 84 | fp: Sus MAX with the CC11 spike already gives a 13.7 dB drop of the part's own level (finding 6). Velocity does nothing on Sus MAX (DIGEST 2.1, measured M1 c06), so FP_VEL 96 changes nothing. Marc Sus LITE would be the sampled fp attack; it is not needed. |
| p.101 | Brass Sustain: CC1 crossfades 4 dynamic layers that all play at once. Portato: each note is held to nearly its full length without being tied. | Horn 1's dolce theme (CC1 carries the phrase offset); its tenutos at 189 / 201 / 589 / 601 are legato-row portato joins (PORTATO_JOIN_AT) | Partly. Where the offset fades out at each hairpin start, CC1 moves 7-10 units at the portato note-on: the note gets a front bump and then falls (finding 1). The KS Master's own portato row (MANUAL-GAPS #9) has not been tried. |
| p.222 | The recorded room is heard as long as samples play, release trails included. | Final-chord ring, tutti stops, S3 | Yes. Tutti stops fall 20 dB in 0.46-0.50 s (references 0.43-0.55). At bar 62 the hall return is still within 6.9 dB of its forte level 0.3-0.6 s after the subito (finding 2). |

MANUAL-GAPS items in this lens: #12 (Felt Cresc rolls) is still untried and not needed (no roll problem measured). #9 (horn portato rows) is an alternative for the Horn 1 tenutos in finding 1.

## EW-TEMPLATE-PLAN sections in this lens, and what is not yet applied

- Sections 7, 8, 10 (phrase shapes): applied in c51, with three gaps.
  - The arch is suspended at every printed hairpin (finding 1).
  - SWELL_CC_CAP cuts it on Bassoons 1-2, Bass clarinet, Contrabassoon and Clarinet 2 (finding 3).
  - Long notes that stay flat (1.2 s or longer, lane within 2 units of its onset value) fell from 36 % to 28 % overall: brass 63 → 42 %, winds 24 → 21 %, strings 20 → 22 %. The plan asks for 0-13 % (measured).
  - The slur lean-off is not applied. Keep it off: about 0.5 dB, against the fitted legato fills (C c50).
- Section 9 (hairpin curves): applied. Diminuendos still fall early on strings and brass (finding 4).
- Section 10, "doublings share one curve": phrases are grouped on score onsets, but the family "start" differs (brass -8, strings 0). The Horn 1 / celli doubling of the dolce theme therefore does not share one curve (measured on the lanes; minor).
- Section 8 tutti spread and room bed: not applied. C c51 measured the spread as unnecessary; the bed stays optional.
- Section 2 delivery refit: not needed (LRA 14.6 LU, limiter 0.0 dB).

## Answers to the coordinator (details in the findings)

- **Finale item 3 (sub. p): finding 2.**
  - There are only two subitos in v621: qn 244 (bar 62; Vla 245) and qn 332 (bar 84, Vc / Cb).
  - HELD_DECRESC_CARRY has nothing to act on: no decrescendo ends at 128, 244, 245 or 332 (parts.json hairpins).
  - The drive phrase type "drop" has no target: 0 drive phrases start on a printed drop of 6 CC or more.
  - The finale's other half of the rule does have a target. The positive phrase offset is not allowed from a subito to the next hairpin (`ps_drops`). In c51 the phrase offset left Bassoon 2 and Horn 4 5 dB louder in the bar-62 p than in c50.
- **Finale item 2 (fp): finding 6.** There is one fp (Cb, bar 33) and no sfp. The part's own drop is 13.7 dB, inside the finale's 10-17. FP_SPIKE_AT_MARK and FP_VEL change nothing here.
- **Finale item 7 (FINAL_RING): finding 6.** Drop it on measured evidence: c51's final chord already falls slower than the finale's result and lies between the soft-ending recordings. The finale's ring points would make it faster.
- **Finale item 4 (side EQ): finding 5.** Switch to the finale's form with the bell at -4.5 dB instead of -5.5, on the tracks that now carry the 200 Hz shelf, and not on the returns. The finale's exact values overshoot below 250 Hz (0.632).
- **Bar 122, 0.5 dB under c50.** The order and margins still hold: 160 over 122 by 1.0 dB (limit 0.5), 122 over 167-170 by 1.0 (limit 1.0, at the limit), 167-170 over 26 by 0.8 (limit 0.3). Nothing below touches bar 122. Re-check the 122 over 167-170 margin after the render (measured).
- **Bar-14 Horn 1 ending (qn 55): keep c51.** It drops 14.1 dB at +0.3 s, 25.4 dB at +0.6 s, so -20 dB at about 0.46 s, inside the references (0.43-0.55 s). c50's 19.2 dB at +0.3 s was faster than any reference (measured).
- **Wind phrase rise: finding 3.**
  - On first notes from the moved onset, wind lyric phrases now rise a median +3.6 dB from +0.15 to +0.8 s (c50 +1.5), brass +2.9 (c50 +0.5). The realised dB per lane unit is 0.22-0.24 for winds and 0.40 for brass (CC1 + CC11). So the winds are not the smallest on this measure.
  - What is missing is the arch on the five SWELL_CC_CAP tracks.
- **Bars 160-166 centroid:** tone, not this lens; untouched.

## Findings, ranked by what a listener would hear

### 1. The phrase shape switches off at every printed hairpin, and that inverts the small swells of the dolce second theme (Horn 1, celli, violas; bars 48-51 and 148-151) (tools; measured, fix effect inferred)

**Where.** The second theme's tune, Horn 1 "1. dolce" with the celli (qn 184-216) and its recapitulation (584-616): the one-bar `<` hairpins at 189, 195, 201, 589, 595 and 601. Also the Cello solo at 685 / 691.

**What.** In `score_to_parts.py` (`ps_hp` near line 3276, `ps_weight` near line 3369), every printed hairpin enters `ps_hp`. The phrase offset fades to 0 over `hp_fade_s` (0.25 s) before the hairpin and comes back after it. In a lyric phrase the offset is +7..+10 units at those points (arch peak +10, family scale). Each printed crescendo therefore starts with a drop of 7-10 units and only climbs back to where the line already was; these hairpins move only 3-7 CC (Horn 1 dyn 59 → 65, 66 → 68). The old Horn 1 portato fits on the tenutos at the hairpin starts were tuned on c09-c46 lanes and now stack on the new CC at the moved note-on: note_trims 189 -6 / 201 -1 / 601 -4; LEVEL_SHAPES 200.81-201.07 +6 / +8, 189.9-190.95 -2.5, 196.1-198.05 -2.5, 596.1-598.05 -4; PORTATO_JOIN_AT 189 / 201 / 589 / 601.

**Evidence (measured).**
- Lanes:
  - 217 crescendos lie inside shaped phrases with the line sounding 0.35 s before. In 19 of them the lane at the hairpin's end is at or below the lane 0.35 s before its start.
  - 7 of the 19 sit at printed drops or subitos (Clarinet 1 / Horn 2 236; Clarinet 1, Bassoon 1, celli and basses 536; celli 405).
  - The other 12 are the dolce theme and the coda solo: Horn 1 195 / 201 / 595 / 601, celli 195 / 201 / 595 / 601, violas 595 / 601, Cello solo 685 / 691.
  - Example, Horn 1 at 189: CC1 62 at 188.5 (c50 54), 54 at 189.0, 61 at 191.0, then 66-70 after the hairpin.
- Stems, Horn 1's six dolce crescendos, end minus the level 0.3 s before the hairpin:
  - c50: +6.2 / +3.8 / -1.6 / +3.5 / -7.5 / +1.3 dB (median +2.4).
  - c51: -0.1 / +2.5 / -2.6 / -3.1 / -4.4 / -2.6 (median -2.6).
- Start to end of the hairpin:
  - c50: +3.1 / +6.1 / -0.4 / +8.2 / -2.8 / -0.7.
  - c51: -4.2 / +6.0 / -7.7 / +1.0 / +0.6 / -3.8.
- Celli, the same six, end minus before: median c50 +1.1, c51 -1.05 dB.
- Front bump. At 189 the c51 Horn 1 note starts 3.7-6.4 dB over its next 0.3 s (c50 rises through the hairpin). At 201 it starts at -3.2 and falls to -10.6..-14.1 by +0.85 s: a 7-11 dB fall inside a printed crescendo (c50 flat, -10.2 → -6.4..-8.3).
- `post51.py hairpins`: brass crescendos under 4 qn reversed 0 → 3 of 8, and these are those three (Horn 1 189, 201, 601). Their 34 % share is 0.45; the plan range is 0.50-0.65.

**Fix.**
- In `tools/score_to_parts.py`, add a PHRASE_SHAPE key `"hp_fade_min_qn"` and append to `ps_hp` only hairpins at least that long: `for a_, b_, k_ in hps: if b_ - a_ >= PS_.get("hp_fade_min_qn", 0.0) - EPS: ps_hp.append((a_, b_))`. Set `PHRASE_SHAPE["hp_fade_min_qn"] = 4.0` in `build/score_config.py`.
  - Shorter hairpins then ride on top of the arch.
  - Long builds keep the fade, as HP_CURVE's `build_min_qn` 4.0 does.
  - Keep the fp / sf entries in `ps_hp`.
- Alternative with the same effect: inside a hairpin under 4 qn, freeze the offset at its value at the hairpin start, then resume.
- Then refit the Horn 1 portato rows (note trims 189 / 201 / 601 and the LEVEL_SHAPES rows above) on the c52 stems, or before the render by envelope simulation (`cycles/c48/actor_scripts/simenv48.py`). Do not delete them blind: they were fitted against a measured bloom.
- If the tenutos still bump: MANUAL-GAPS #9, the 1FH portato row, as a pass-2 test.

**Pass criteria.**
- In 184-216, 584-616 and the Cello solo 680-696, no crescendo whose lane at its end is at or below the lane 0.35 s before it (c51: 12).
- Each of Horn 1's six dolce crescendos rises at least +1.5 dB (end minus 0.3 s before); celli and violas the same at least 0 dB.
- Brass short crescendos: 0 reversed.
- Phrase rise and taper statistics elsewhere within 0.5 dB of c51.

### 2. Sub. p: bar 62 now falls like a natural stop, but the held winds and horns stay 5 dB too loud in the p, and bar 84's p notes swell in late (S3; measured, effect of the fixes inferred)

**Bar 62 (qn 244), master: the S3 shape passes (measured).**

| Measure | c35 (glitch) | c36 | c50 | c51 | This render's tutti stops (qn 125.9 / 288 / 551 / 679) |
|---|---|---|---|---|---|
| First 50 ms frame (20 ms frames, re the 0.35-0.1 s before) | -11.6 | -8.6 | -5.2 | -5.1 | -2.9..-4.9 |
| Steepest 0.2 s fall | 18.3 | 15.1 | 11.2 | 11.0 | 12.8-14.9 |
| -10 dB reached at | — | — | — | +0.20 s | +0.10-0.15 s |
| Level 0.5-1.0 s after | — | — | — | -12.7 dB | — |

- The hall rings under the p. The returns are 14.3 dB under the master before the mark and fall only 3.2 / 6.9 / 7.5 dB at 0.1-0.3 / 0.3-0.6 / 0.6-1.0 s.
- The fall comes in two steps:
  - -5.4 dB in the first 50 ms;
  - a hold at -8 dB for 0.1 s;
  - a further 3.5 dB at +0.2 s, when the forte violins' release (f62 aliases, 150 ms cap) ends.
- Critic C c50's limit "no 0.2 s fall over 9 dB" is stricter than this render's own natural stops, which match the recordings. Replace it with the limits below.

**Bar 62, each part's own drop (measured).**
- Method: K-weighted, -0.5..-0.1 s against +0.3..+1.2 s.
- Strings, c51 (c50):
  - Violins I (main + f62): -17.7 (-17.8).
  - Violins II: -13.7.
  - Celli: -18.5 (-18.7).
  - Basses: -12.0 (-10.4).
- Winds and horns holding into the p:
  - Bassoon 2: -7.3 (-12.5).
  - Horn 4: -4.8 (-10.8).
  - Clarinet 1: -7.2 (-7.3).
  - Horn 2: -8.5 (-8.2).
  - Horn 3: -8.8 (-7.7).
- So Bassoon 2 and Horn 4 sit about 5 dB louder in the p than in c50 (post level -52.7 → -47.6 and -55.4 → -50.5). The master drop is 13.3 dB (c50 13.8).
- Cause: over 244-248 (to the next hairpin start, 248) these parts' lanes sit over the printed p (46):
  - Bassoon 2: +11.9 units (lyric phrase 236-247, the arch carried across the subito).
  - Clarinet 1: +9.0.
  - Horn 2: +8.9.
  - Horn 4: +7.6 (build phrases 238.5-254 and 232-247).
  - Violins I / II: +3.4 / +3.6.
- These offsets times the measured dB per unit (0.22-0.40) account for 2-3.6 dB of it (inferred). This is the finale's bar-219 failure in a smaller form.

**Fix, bar 62.**
- Port the finale's `ps_drops`: `symphony/mvt3/reaper-v600/tools/score_to_parts.py`, the block after `ps_weight` (lines ~3496-3504) and the `o_ > 0` test in `phrase_off`. Port the drive "drop" kind with it for parity (lines ~3437-3455); it will find nothing here.
- Set `PHRASE_SHAPE["types"]["drop"] = {"cc": 6}`. Expected effect: Bassoon 2 / Clarinet 1 / Horn 2 / Horn 4 -2..-3.5 dB over 244-248, the master post level about -0.3 dB.
- The 6-CC test also zeroes positive offsets after printed drops inside continuing lines elsewhere (many marks: every non-hairpin drop of a dynamic step or more inside a shaped phrase). Guard: if post51's lyric or build rise or taper falls by more than 0.5 dB against c51 for any family, restrict the rule to subito and fp marks (a `"subito_only": True` key: only `sub_soft_q`).
- HELD_DECRESC_CARRY: port it with the value off (`None`); it has no target in v621.
- No "-4 dB fresh brass entry" roles are needed. Horn 2's entry at 245 is covered by `ps_drops`.

**Pass limits for bar 62 (master on 20 ms frames re the 0.35-0.1 s before the mark; parts K-weighted -0.5..-0.1 s against +0.3..+1.2 s).**
- First 50 ms 5.5 dB or less (c51 5.1). If the new drop pushes it over, lower `SUBITO_TAIL` `at_once_db` 4 → 3.
- Steepest 0.2 s fall 13 dB or less (c51 11.0).
- Level at 0.5-1.0 s between -12 and -15 dB (c51 -12.7).
- Summed returns at 0.3-0.6 s within 8 dB of their own pre level (c51 -6.9).
- Strings' drops at least 12 dB.
- Clarinet 1, Bassoon 2, Horn 2 and Horn 4 at least 9 dB, and no part's drop more than 1 dB smaller than in c50.

**Bar 84 (qn 332, Vc / Cb sub. p re-attacks after the bar-83 ff): a late swell, then a fall (measured).**
- Master, 50 ms frames re 332-0.35 s:
  - -10.7 / -12.7 at +0.05 / +0.15 s;
  - then up to -8.2 / -6.1 at +0.25 / +0.35;
  - then down to -10.3 at +0.85 and -11.5 at +1.35.
  So there is a 6.6 dB re-swell 0.35 s after the beat.
- The basses' stem rises 10 dB between +0.15 and +0.35 s, then falls 10-15 dB over the next 0.8 s. The Vc + Cb sum falls 5-6 dB from +0.35 to +1.15 s.
- The basses' envelope does this:
  - LEVEL_SHAPES `[(331.45, 0), (331.6, -8), (332.25, -8), (332.4, 0)]` (score_config.py ~line 1740, set for the ff release) holds the new p note at -10 dB until 331.99 and lifts it 8 dB by 332.4 (+0.20 s);
  - `[(332.9, 0), (333.15, -3.5), (334.3, -3.5), (334.8, 0)]` (~line 1322) and CC11 52 → 44 over 331.73-333.0 then pull it down.
- Celli: their bloom shapes (332.5-334.6: -3 / -5 / -2; lines ~1317 and ~1976-1979) take the envelope from -2.0 at 332.0 to -8.1 at 333.0.
- Unchanged c49-c51, so it is old: these shapes were fitted on series-1 renders.

**Fix, bar 84.**
- End the basses' ff note earlier: `NOTE_END_AT["Double basses"] = {330.0: 331.45}`. Then return the -8 dB cut to 0 by 331.80 instead of 332.4.
- Remove the celli and basses bloom shapes at 332.5-334.8.
- Simulate with `simenv48.py` on the c51 stems before rendering. Refit a flat shape only if the render shows a bloom over 2 dB.

**Pass limits for bar 84.**
- The master rises 2 dB or less from +0.15 to +0.35 s (c51 +6.6).
- The Vc + Cb sum stays within ±2 dB from +0.3 to +1.2 s (c51 falls 5-6 dB).
- The master at +0.3..+1.2 s is at least 12 dB under the bar-83 chord (c51 14.0, K-weighted).

### 3. The five SWELL_CC_CAP winds never arch: their soft lyric phrases peak only 2 units over the printed level, against 11 on the other winds (tools; measured, effect inferred)

**Where.** Bassoons 1-2, Bass clarinet, Contrabassoon and Clarinet 2 in their soft lyric phrases:
- Bassoon 2 at 48 (bar 13) and 600 (bar 151, recapitulation second theme);
- Bassoon 1 at 584 and 692;
- Bassoon 2 at 680;
- Bass clarinet at 696 (coda pp);
- Clarinet 2 at 576.

**What.** `SWELL_CC_CAP` (tools/score_to_parts.py line 536: `"*": 0` on these five tracks, with `SWELL_CAP_MAX_CC` 40) clamps CC11 at the note's starting value on soft long notes. It exists so a pp swell does not fade in the next layer, whose crossfade starts at CC 33-38 (kit section 4). The clamp now also removes the c51 phrase arch: the lane can only climb back from the phrase's start offset (-9) to the printed level and stops there. Nothing replaces it in the volume envelope.

**Evidence (measured).**
- Soft wind lyric phrases (printed p or softer), median peak offset over the printed level:
  - capped tracks: +2.1 units (n 8);
  - the other winds: +11.3 (n 10).
- Example, Bassoon 2 at 600: CC11 25 → 34 by 600.8, then held at 34 (the printed pp) for 3.9 qn.
- The rise from +0.15 to +0.8 s is similar (capped +3.6 dB, others +3.1 dB, median) because it is the return from the start offset. The middle of the phrase is flat, and the taper starts from the printed level instead of from a peak.
- This, not the wind dB response, is why the actor's wind lyric figure stays the smallest.
- Measured dB per lane unit on winds is 0.22-0.24 (c50 → c51, 32 phrases with a lane change of 4 units or more).

**Fix.**
- In `tools/score_to_parts.py`, where `swell_caps` clamps CC11 (near line 3456), add the clamped amount of the phrase offset (only inside `phrase_shapes`, so the per-note SWELL_DB behaviour of c22 / c23 stays) to the volume envelope in dB.
- Use a new table `SWELL_CAP_TO_VOL_DB_PER_CC = {"Bassoon 1": 0.32, "Bassoon 2": 0.32, "Bass clarinet": 0.26, "Contrabassoon": 0.21, "Clarinet 2": 0.20}` (kit LEARNINGS section 4 per-patch fits), set in `build/score_config.py`.
- Expected: +2.3-2.9 dB at the arch peak (about 9 units), with CC11 still never over the cap, so no layer crossing (inferred).

**Pass criteria.**
- On those phrases, stem level at the arch peak (0.33-0.62 of the phrase) at least 2 dB over both the level at +0.15 s and the level 1 s before the end.
- The phrase's first and last 0.3 s within 0.5 dB of c51 (no louder entries).
- Coda pp bars 175-181 in the mp3 still at least 5 dB under the 171-174 solo bars (c51 6.9).

### 4. Diminuendos still lose their level early on strings and brass (HP_CURVE value; measured, effect of the values inferred)

**Where.** All diminuendos of 2 qn or more over a continuous line (string n 48, brass n 37, wind n 45).

**Evidence (measured, `post51.py hairpins`).** Share of each hairpin's own dB change reached at 34 / 50 / 72 % of its length, c50 → c51:

| Hairpins | c50 | c51 | Plan limit (C c50, from plan section 9) |
|---|---|---|---|
| String diminuendos | 0.26 / 0.49 / 0.70 | 0.21 / 0.40 / 0.57 | 0.30 or less at 50 %, 0.55 or less at 72 % |
| Brass diminuendos | 0.22 / 0.41 / 0.62 | 0.17 / 0.36 / 0.48 | as above |
| Wind diminuendos | 0.19 / 0.34 / 0.73 | 0.17 / 0.22 / 0.57 | as above |
| Short crescendos (under 4 qn), 34 % share: winds / strings / brass | — | 0.65 / 0.55 / 0.45 | 0.50-0.65 |

- So c51 moved the diminuendos in the right direction, but strings miss both limits and brass misses at 50 %. Winds are just over at 72 %.
- Short crescendos: winds and strings pass; brass is low because of finding 1.
- Reversed hairpins: crescendos 17 → 17, diminuendos 4 → 5.
- The large "reversed" brass crescendos (Horn 3 440-464, Horn 4 536-548 and 88-100, Bass trombone 452-464, Trombone 2 448-464) are measurement artefacts: their last note ends before the hairpin's end.

**Why.** HP_CURVE `"decresc_last": 0.35` lets 35 % of the fall happen before the last inner onset. The volume-envelope falls are linear in time: `HELD_DECRESC_DB` (wind / string 3 dB, from start + 0.2 s to the end) and the soft-hairpin dB ramps.

**Fix (in `build/score_config.py` and the `held_decresc` envelope in score_to_parts.py).**
- `HP_CURVE["decresc_last"]` 0.35 → 0.20.
- Give the held-decrescendo envelope the lane's held shape: a point at 60 % of the time with 20 % of the dB fall, as `decresc_held` (0.6, 0.2) does for the lane.

**Pass.** String and brass diminuendos 0.30 or less at 50 % and 0.55 or less at 72 %; no more reversed diminuendos than c51's 5.

### 5. Low-end width (finale item 4): switch to the finale's side EQ form, with the bell at -4.5 dB, on the tracks that carry the 200 Hz shelf now, and not on the returns (mix.json; simulated on the c51 stems)

**Evidence (simulated, except the c51 row and the references, which are measured).** Correlation by band; side/mid over all active frames. References: below 250 Hz 0.54-0.62 (Brahms 0.541 / 0.583 / 0.601 / 0.624); 250 Hz-5 kHz 0.47-0.56; side/mid -4.7..-5.4 dB.

| Variant | Below 250 Hz | 31-62 / 62-125 / 125-250 Hz | 250 Hz-5 kHz | Side/mid (dB) |
|---|---|---|---|---|
| c51 (200 Hz -6 side shelf on strings, brass, timpani) | 0.563 | 0.854 / 0.843 / 0.478 | 0.483 | -4.66 |
| Finale's exact EQ (60 Hz -3 shelf + 180 Hz -5.5 bell, 1.5 oct) on the same tracks | 0.632 (over) | 0.718 / 0.790 / 0.583 | 0.517 | -5.11 |
| Same with the bell at -4.5 | 0.592 | 0.702 / 0.773 / 0.534 | 0.509 | -4.95 |
| Same with the bell at -3.5 | 0.543 | 0.684 / 0.754 / 0.477 | 0.500 | -4.77 |
| Finale's track set (Vc, Cb, trombones, tuba, timpani, harp, Cbn) + the 4 returns | 0.704 (over) | — | 0.505 | -5.12 |
| Finale's EQ on the 4 returns only | 0.617 | — | 0.489 | -4.82 |
| Dvořák 9/i (lossy mp3; low end not to be tuned on it alone) | 0.560 | 0.491 / 0.616 / 0.552 | 0.561 | -5.33 |

**Reading.**
- c51 is near-mono below 125 Hz (0.84-0.85) and wide at 125-250 Hz, and its side/mid is 0.04 dB outside the references.
- The -4.5 dB variant puts all three aggregate figures inside the references and makes the band profile more even (deep bass less mono, low-mids narrower), closer to the one recording measured by band.
- The finale's exact -5.5 dB overshoots, and its track-plus-returns layout overshoots further, because Movement I's Mains already sit at the seat ±0.8.

**Fix.**
- In `build/mix.json`, replace `{"band": "lowshelf", "hz": 200, "db": -6.0}` with `{"band": "lowshelf", "hz": 60, "db": -3.0}, {"band": "bell", "hz": 180, "db": -4.5, "bw_oct": 1.5}` on every track that has it:
  - Horns 1-4, Horns a2;
  - Trumpets 1-3, Trumpets a2;
  - Trombones 1-2, Bass trombone, Tuba;
  - Timpani;
  - Violins I / II, Violas, Violoncellos, Double basses.
- On the celli and basses this bell replaces the 0 dB 170 Hz placeholder. Keep the brass 250 Hz +1.5 high shelf and the harp's 300 Hz -8 shelf. No side EQ on the returns. This is a `--mix-only` change.
- The ReaEQ shelf slope at default bandwidth is not exactly the RBJ shelf used in the simulation, so check the render. Pass: below 250 Hz 0.54-0.62, 250 Hz-5 kHz 0.47-0.56, side/mid -4.7..-5.4 dB. If below 250 Hz reads over 0.62, use the -3.5 dB bell.

### 6. Finale items 2 (fp) and 7 (FINAL_RING): measured, nothing to change in the sound; port the code with values that keep c51's result (measured)

**fp (the only one: Double basses, bar 33, qn 128; v621 has no sfp).**
- The basses' stem peaks at +0.12-0.17 s, is 9.8 dB down at +0.32 s and 13.7 dB down at +0.52 s, then holds 13-18 dB under the peak. That is inside the finale's 10-17 dB per-part drop.
- During the attack the tutti ff eighth is 18 dB over the basses. Under the bassoon solo the basses sit 5-12 dB below it.
- CC11 at the moved note-on (127.88) is already the ff level (111, held to 128.125, at the p 46 by 128.25), because the level before the fp is ff and no hairpin starts at the mark. So FP_SPIKE_AT_MARK changes nothing.
- FP_VEL 96 changes nothing on Sus MAX (velocity ignored on KS Master sustain rows: DIGEST 2.1, manual p.53 / p.64, M1 c06).
- Port both for parity (`FP_SPIKE_AT_MARK = True`, `FP_SPIKE_S, FP_VEL = (0.10, 0.30), 96`) and check the basses' stem over 127.5-130 within 0.5 dB of c51. At 126 bpm (0.10, 0.30) s is about 0.21 / 0.63 qn, against FP_SPIKE's 0.12 / 0.25 qn. That lengthens the attack, so if the basses' drop by +0.5 s falls under 10 dB, keep `FP_SPIKE_S = None`.
- The master drop at the fp is the tutti stop (peak +12.2 to -7.9 dB at +0.62 s) followed by the bassoon solo. No issue.

**FINAL_RING.**
- c51 final chord, master / mp3:
  - from the written end (qn 728): -10 / -20 / -30 dB at 0.405 / 0.665 / 0.865 s and 0.413 / 0.663 / 0.873 s;
  - by the recordings' automatic rule, the chord's fade starts 2.24 s before the end (morendo plus the final fade from 727.5).
- Soft-ending references (rtk, same detector): Brahms 4/ii 0.20 / 0.48 s, Brahms 1/ii 0.40 / 0.79 s to -10 / -20 dB. The finale's FINAL_RING took its loud chord to 0.42 s.
- The finale's ring points (-8 / -16 / -24 dB at 0.15 / 0.30 / 0.45 s) would reach -20 dB at about 0.37 s (inferred from the envelope alone): faster than c51 and faster than both soft references.
- Keep `FINAL_RING = None` in Movement I (port the code, value off).
- The final ppp chord in the mp3 is 5.7 dB under bar 181 and 13.5 dB under the 171-174 solo bars; the loop scan reads +0.06 (band) / +0.25 (centroid) at 3.95 s on the master, under 0.40. Nothing to fix.

## Loudness arc, delivery, loops and decays (measured; no change asked)

**Delivered mp3.**
- -19.8 LUFS, LRA 14.6 LU, p10-to-max 18.8 dB, true peak -1.8 dBTP, limiter 0.0 dB.
- Short-term max over integrated: mp3 +8.4, master +10.0; references +5.1..+7.6 (the score has two fff; do not let it grow).
- Climax order (short-term max): 160 -11.4 > 122 -12.4 > 167-170 -13.4 > 26 -14.2.

**Sostenuto decrescendo, bars 122-126 (master, K-weighted bar levels).** -11.5 / -15.3 / -22.3 / -28.5 / -35.1, steps -3.8 / -7.0 / -6.2 / -6.6 dB. c50: -5.0 / -8.4 / -8.2 / -1.9. It now falls evenly from the fff to the p over the tam-tam's damp; c51's best dynamic change.

**Builds.**
- Bars 113-116: +10.0 dB.
- Bars 127-131: +15.8 dB.
- Bars 155-160: +18.9 dB in the mp3, with bar 159 crescendoing inside the bar.

**Coda (mp3).**
- 171-174: -22.8 / -22.6 / -21.5 / -25.1.
- 175-181 pp: -31.3..-28.7.
- 182 ppp: -36.3.

**Loudness motion.** mp3 dS4 p90 8.95 → 8.71 dB (just past the c24 regression line of 0.2), 1 s / 20 s 4.97 → 4.95. Master 10.68 / 5.99 (Dvořák 9.7 / 5.6, Brahms 1/ii 8.55 / 4.56). Finding 1's fix should give some motion back (inferred).

**Decays.**
- Tutti stops fall 20 dB in 0.46-0.50 s (references 0.43-0.55).
- Drops at +0.3 s: 16.0-20.6 dB.
- Fermata late decay (RT -20..-35): 1.89 s.

**Loops.**
- Master: Lento +0.27 / -0.11 (band / centroid at 3.95 s), 175-178 +0.03 / -0.06, 160-164 -0.37 / -0.10.
- Stems at 0.40 or more: Bass clarinet 464 / 480 / 492 (band +0.54 / +0.78 / +0.84), Tuba 488 (centroid +0.65) and Violins II 184 (centroid +0.47). These are 6-7 s notes in breath-split pieces of 2.6-2.9 s or single short windows, 10.5-19.3 dB under the master. They are not loop pulsing (inferred; as in c50 / c51).

## Do not touch

- The bar-62 machinery: SUBITO_FRESH, SUBITO_TAIL and the f62 aliases. Only add `ps_drops`, and lower `at_once_db` only if the first-50-ms limit fails.
- The bar-121 back-off rows and the even 122-126 decrescendo.
- The climax order and margins (160 > 122 > 167-170 > 26) and the fff lifts at 636.
- HP_CURVE's crescendo point (0.4, 0.65) and its linear long builds and timpani.
- PHRASE_SHAPE values, the wind `family_gain` 1.4 and `both_lanes`. Change only the two places in findings 1 and 3.
- The returns' IR envelope, faders and 2.3 kHz low-pass; Main at seat ±0.8. Change only the side-EQ curve.
- `deliver_master.py` settings, the master EQ and RIDE_TRIMS.
- The string release caps (150 ms mf-ff / 350 ms p; basses 600 ms pp) and the final-chord morendo and fade.
- `swell_fills48.json` and the S1 / S2 lead and dip tables.
- Every c51 and earlier do-not-touch item.
