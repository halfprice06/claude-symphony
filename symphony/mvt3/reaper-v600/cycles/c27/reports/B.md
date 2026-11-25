# Cycle 27, critic B (balance and levels), on the c26 render

All levels come from the c26 stems and master (`cycles/c26/render/`), timed on `cycles/c26/parts_rendered.json`.
- "K" is K-like weighting: a 60 Hz high-pass and +4 dB above 1.5 kHz, on the mono sum, in 10 ms frames.
- "Best band" uses Movement I c61's method (`symphony/mvt1/reaper-v621/cycles/c61/reports/B.md`): the 1/3-octave band from 100 Hz to 6.3 kHz, among the line's own bands, where the line's power over everything else (master minus line) is highest. Its targets: middleground lines (countermelodies, counter-lines) 2-6 dB K under the tune and 0 dB or better in the best band; background figures 6-10 dB under, best band -6 dB or better (Adler p.116; Rimsky-Korsakov, "Comparison of resonance").
- Doubling tracks count as part of their line.
- "Simulated" values scale each stem's band power over the span (power sum, no cross terms). They are inferred, not rendered.
- The mp3 figures come from `mvt3-mockup-c26.mp3` (ffmpeg ebur128, 0.30 s head allowed for).
- Envelope figures for the dynamic trims are my own reconstruction from parts.json (`vol_db`, `dyn_curve`, `hairpins`) and the mix.json trim tables, with the decrescendo holds of `vol_points`. I did not run build_reaper.py.
- The scratch scripts were deleted with the scratch folder.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 27: the table stops at cycle 20, and the third round sets no pages. So I skipped the full reading. I read `loop/MANUAL-GAPS.md` and the pages behind my findings.

| What the manual says (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| Volume (CC7) sets a track's level against the other tracks; Expression (CC11) shapes the line (p.64, and p.151: CC7 "is best used to set the overall upper limit on the volume of each track"). | Passage levels in findings 1-3 and the dynamic trims in finding 5. | Partly. CC7 is used on the timpani and, since c26, for Violins I (632-660) and the violas (839-848), where it measured as 20 log10 (MANUAL-GAPS, Finale c26). The dynamic trims, roles and hairpin gains are still in the track envelope. |
| Stopped horn: the 06 Mutes folder; "see the descriptions of the unmuted versions of these instruments for details about Mod Wheel usage" (p.106), so CC1 should crossfade the dynamic layers as on the open rows (p.101). | Horns' "Stop Sus" notes at 548-552 (sf >) and 668-672 (f > p). | No. On "Stop Sus", CC1 falling 89 -> 54 left the stem flat or rising (finding 4). That is measured, so the row does not answer CC1 the way the open rows do (the patch's groups were not read; inferred). |
| MANUAL-GAPS #7, half-section divisi patches (p.89-90). | Violins I div. octaves at 632-660 (finding 2). | Still unused for memory reasons. The CC7 80 passage level from c26 stands in for it; the remaining masking at 159-165 comes from Horn 1 and the violas, not Violins I. |
| MANUAL-GAPS, Finale c26: CC7 behaves as 20 log10 on the string patches. | The new CC7 rows proposed here (basses, horns, celli). | The CC7 law on the woodwind KS Masters is not measured yet. Range-test it before moving any woodwind trim into CC7 (finding 5). |

## 1. Bars 259-262 (qn 1032-1048): the celli's held notes and Horns 3-4 cover the running figure, and they also take the step out of the fff arrival at 263 (measured; fix simulated)

**What happens.** Under the last chorale statement, Violins II and Clarinets 1-2 play the slurred running figure (ff), the violas play quarters, and the celli hold whole notes. The figure is the passage's motion.

**Evidence (K, 1036-1048):**
- Running figure (Violins II + Clarinets 1-2): best band -7.7 dB (1.6 kHz), 8.4 dB under the chorale (Trumpets 1 / 3, Horns 1-2, Trombone 1, Flute 1, Oboe 1). The background target is -6 or better. Violas' quarters: best band -8.1 dB.
- Maskers in the figure's band: Horn 3 -6.1, Horn 4 -8.2, Horn 1 -9.2 dB re the rest. Horns 3-4 carry the role `roles.json` [1032, 1048, 3.0] plus hairpin gain, so +3 to +5 dB in the envelope.
- The celli's whole notes are the second-loudest stem of the orchestra in bar 262 (1044-1048):

  | stem | K level |
  |---|---|
  | Trumpet 1 | -21.5 |
  | celli | -24.7 |
  | Horn 3 | -25.0 |
  | Trombone 1 | -27.0 |
  | Violins I | -27.3 |

  The celli sit 7-9 dB over Violins II (-33.1) and the violas (-33.7). Their level comes from CC11 109-115, hairpin gain rising to +3 dB, and the `loud_eq` 160 Hz +3 dB bell, which switches on at 1030-1032.
- At the arrival, stem by stem (1048-1050 minus 1046-1047.9): celli -2.7, Violins I -3.6, Trumpet 1 -1.0; the master steps only +0.7. On the mp3, bar 263 is +0.8 dB over bar 262. The two loudest strings of bar 262 get softer at the fff.

**Fix (no per-note envelope move):**
- `build/roles.json`: Horn 3 and Horn 4 [1032, 1048, 3.0] -> [1032, 1048, 0.0] (the edges stay where they are). Violins II [1032, 1048, 2.0] -> [1032, 1048, 4.0] (the [984, 1056, -2.5] row stays, so the net is +1.5).
- Clarinets 1-2: a role of +2 dB from 1031.85 to 1047.85, with both edges in the common rests (Cl1 1031.8-1032.0 / 1047.75-1047.94, Cl2 1031.6-1031.9 / 1047.81-1047.94). CC11 is already at 102-104 here, so it cannot carry the change.
- Violoncellos:
  - CC7 95 (-2.5 dB) from 1032 to the 1047.78-1047.89 gap. Ramp it in over 1032-1033 in CC7 (instrument side), and return it to 127 inside the gap.
  - Move the `loud_eq` points [1030, 0], [1032, 1] to [1046, 0], [1047.85, 1], so the bell opens in the same gap with the fff note.

**Expected (simulated):** figure best band -7.7 -> -5.2 dB, figure 6.4 dB under the chorale (from 8.4), master over 1036-1048 -0.3 dB. The stem-sum step into 263 goes +0.64 -> +1.25 dB (celli -3 dB alone: +0.89). Bar 262 is 0.55 dB lower, so the delivery's final-chord lead does not shrink.

## 2. Two middleground lines in the f/ff tuttis are still hidden: the Horn 1 counter-line at 67-74 and the Violins II / clarinet countersubject at 159-165 (measured; fixes simulated)

These are the lines behind Dan's "inner lines hidden".

**Horn 1 dolce counter-line, qn 264-296 (bars 67-74), under the violins' F2:**
- K 10.2 dB under the violins; best band -4.3 dB (252 Hz). The middleground target is 2-6 under and 0 or better.
- Maskers in that band: celli -3.2 and double basses -3.6 dB re the rest. The celli carry their own counter-melody (best band +3.1, so it is heard). The basses (mp) play bass notes only.
- c25's role [263.72, 295.75, 4.0, 0.2] was not enough.

**Fix for 67-74:**
- Horn 1 role 4.0 -> 7.0 (same edges, in the breaths at 263.72 and 296).
- Double basses: a new row of -3 dB from 263.73 (their rest 261.0-263.73) to their first rest at or after 296. As CC7 90 it is a passage level in the instrument.
- Simulated: best band -4.3 -> -0.8 dB, K 7.2 dB under the violins, master +0.1 dB.

**Countersubject, qn 632-660 (bars 159-165):** Violins II f espress. with Clarinets 1-2 mf espress., under the tune in Flutes, Oboes, Violins I div., violas and Horn 1.
- Best band -4.7 dB (252 Hz); K 7.2 dB under the tune.
- Maskers: Horn 1 -5.3 and violas -6.5 dB, both doubling the tune. Violins I is no longer the masker after c26's CC7 80.
- c25's "+2 dB at k 20" (`cc_scale`) on the clarinets did not reach the stems: Clarinet 1's CC11 at 640 is 127, the ceiling.

**Fix for 159-165:**
- Clarinets 1-2: a role of +2 dB from 631.0 to 659.9. Both edges lie in Clarinet 1's rests (630.0-631.87 and the 659.81-660.0 gap). Drop the ineffective `cc_scale` on these tracks.
- Horn 1: CC7 90 (-3 dB) from its rest at 630.89-631.79 to its first rest at or after 659.8.
- Violas: CC7 101 (-2 dB) from their rest at 630.86-631.78 to the same point.
- The tune stays doubled by six tracks.
- Simulated: best band -4.7 -> -1.6 dB, K 4.5 dB under the tune (inside 2-6), master -0.3 dB.

## 3. Bars 235-237 (qn 936-948): the basses' p pedal sits 3-8 dB over the celli's moving p bass line (measured; fix inferred)

**Evidence:**
- Celli minus basses (K, per 4 qn): -4.4 / -7.8 / -2.9 dB.
- The celli now play CC11 46-48 (DYN p, after c26's +12) with CC1 42-45. Their line moves: C3 C3 D3 F2 G2, "change bow at will".
- The basses hold C (pitch 36) for 8 qn, twice (935.79, 943.84), at CC11 46-50 with CC1 55-57. They also carry the soft trim p +8 dB, against the celli's +3.5.
- Both are printed p. The moving line is the middleground and the pedal is background, so the celli should be at least level with the basses.
- More celli CC11 would move them toward the mf layer.

**Fix:** Double basses CC7 80 (-4.0 dB, 20 log10 as measured on the string patches) from the rest at 934.91-935.79 to the end of the 943.84 note (951.85), back to 127 after it.

**Expected:** celli minus basses about -0.4 / -3.8 / +1.1 dB (inferred: the shift as written, as for c26's CC7 rows).

## 4. The stopped-horn decrescendos run the wrong way (548-552) or barely fall (668-672) (measured; cause partly inferred)

**Horns 3-4, qn 548-552 (bar 138):** printed "+" sf with a decrescendo; the winds have a sub. p.
- The row is "Stop Sus". CC1 falls 89 -> 54, CC11 stays at 127, and the envelope trim rises.
- Stem, per 0.5 qn from 548:
  - Horn 3: -43.9, -46.7, -46.2, -46.3, -45.1, -44.3, -43.8.
  - Horn 4: -47.0, -48.7, -46.0, -43.7, -44.1, -43.1, -42.5.
- So Horn 4 grows 6 dB through the printed decrescendo, while the master falls from -25.6 to -37.0. Horn 4 comes out of the sub. p texture: at 551 it is 5.5 dB under the master. The sf front is weak too, only 2 dB over the body.

**Horns 1-2, qn 668-672 (bar 168):** stopped f > p, tied into the p note.
- They fall only 3.9 / 4.4 dB over the bar, where f to p should give about 10 dB.
- CC11 falls 87 -> 64 here (-2.7 dB at 20 log10). The trims rise +5.4 to +6.3 dB under the decrescendo hold (my reconstruction). CC1 adds nothing.

**Fix (instrument side; `build/score_config.py` `note_cc` / `cc_shape` on the "Stop Sus" notes):**
- Horns 3-4 548: CC11 127 at 548.25 (after the sf front), falling to 50 at 551.9: -8.1 dB at 20 log10.
- Horns 1-2 668: CC11 from 87 to 35 by 671.9 (-7.9 dB), not to 64.
- Hold the dynamic trim at its start value inside these two hairpins. In `vol_points`, a per-span `SOFT_DECRESC_KEEP` of 0 for notes on "Stop Sus" (now 0.5).
- **Target:** each stopped decrescendo falls 7-10 dB, and no stopped note rises inside a printed decrescendo.

## 5. The 73 "printed-hairpin ramps inside held notes": a rate limit is the wrong fix; move the dynamic trims into CC7 (measured, with my reconstruction of the envelope)

**What the ramps are.** They are the mix.json dynamic trims (`dyn_trim_db` and `soft_trim_db`) read from the printed dynamic curve. In my reconstruction of the 1058 held-note spans under a printed hairpin, the envelope moves 1.5 dB or more in the hairpin's direction on 317 spans and against it on 118. "Against" is built into the trim tables: Horn 1 is p +10.6, mf +2.0, f -2.0, ff +2.6, and Trombone 1 is p +12.6, f -0.9. So a p -> f crescendo lowers the envelope by up to 12 dB while CC1 and CC11 rise.

**Are they audible as per-note moves?** Mostly not, measured on the stems:
- The 85 crescendos whose trim falls still rise a median +7.1 dB.
- The 33 decrescendos whose trim rises still fall a median -7.1 dB.
- The audible exceptions are the stopped horns in finding 4.

**Why a rate limit would hurt.** At 3 dB/s, a 2 qn hairpin at 168 qn/min (0.71 s) could move only 2.1 dB. That flattens the printed crescendo gains (+2 brass, +3 strings, +4 winds) and moves arrival levels after their marks. Do not add one.

**The fastest moves are not on the guard's list.** The guard exempts 1.5 s after an fp / sfp. There the trims jump inside held notes within 0.17 s (0.5 qn), while CC11 falls:

| mark | track | trim jump |
|---|---|---|
| sfp 592 | Trombone 1 | +10.5 dB |
| sfp 592 | Horn 3 | +9.7 dB |
| sfp 592 | Tuba | +8.9 dB |
| sfp 592 | Flute 1 | +8.8 dB |
| fp 832 | Horn 1 | +11.3 dB |
| fp 832 | Trombone 1 | +11.2 dB |
| fp 832 | Horn 2 | +9.7 dB |

That is about 60 dB/s inside the note. The p after the mark still lands on the track's usual p level (Horn 1 falls 19.6 dB and Trombone 1 24 dB from the 592 peak), so the levels are consistent. Only the place where the move happens breaks the rule.

**Fix (generic, `tools/build_reaper.py` vol_points and `tools/score_to_parts.py`; default off, Finale on):** `DYN_TRIM_TO_CC7`.
- Per track, the envelope keeps a constant: gain_db plus the table's maximum trim.
- CC7 carries the rest: CC7 = round(127 · 10^((trim(q) − max)/20)), on the same 0.125 qn grid and dynamic curve, with the same holds.
- Multiply it into the existing CC7 rows (timpani, Violins I 80, violas 90, and those proposed above).
- Example, Trombone 1: envelope +16.6 dB (4.0 + 12.6). CC7 is 127 at p and 27 at f (-13.5 dB; 0.3 dB per step there).
- First range-test CC7's law on one woodwind KS Master (Flute 1, Oboe 1), because only the string patches are measured.
- **Expected:** the envelope holds no trim movement inside any note (guard `inside_hp` 73 -> 0, and the fp / sfp jumps leave the envelope), with stem levels unchanged within CC7 quantization (0.1-0.3 dB).

The five `inside_dyn` steps and the celli step at 870.4 (`--strict`) come from the same trims and go into CC7 with them.

## 6. The first violins' accented chord fronts: the gap to Violins II is a row mismatch, not a hot Violins I (measured)

**Evidence (K, front from -0.03 to +0.08 s against the body at +0.2 to +0.5 s, at qn 16 / 584 / 1104):**

| section | row | front minus its own body |
|---|---|---|
| Violins I | "Sus Marc LITE" (v92 / v108) | -0.8 / -1.0 / -1.7 dB |
| Violins II | "Sus MAX" (v111 / v127) | -7.6 / -4.8 / -9.0 dB |
| Violas | "Sus MAX" | -4.4 / +0.4 / -1.0 dB |
| Violoncellos | "Sus MAX" | -8.1 / -4.5 / +0.6 dB |

- The bodies are balanced: Violins I minus Violins II is +2.6 / +4.3 / +3.6 dB. The "7-10 dB" is Violins II's slow Sus MAX attack: their body arrives 0.2-0.3 s late.
- c25's CC11 front shape (+17 ahead) did not fix it at 16 (Violins II still 7.6 under its body). c26's v80 test on Violins I lowered the wrong section.

**Fix:**
- Play Violins II's accented ff chords at 0, 16, 584 and 1104 on "Sus Marc LITE", with Violins I's lead (0.085 s) and velocity (v92 at 0 / 16 / 584, v108 at 1104).
- Add the celli at 16 and 1104 if memory allows. Each is a new row: a full rebuild, about 0.1-0.3 GB per track.
- Keep Violins I as it is.
- **Target:** every section's front within 3 dB of its own body, and Violins I minus Violins II within 3 dB at the front.

## Coordinator's checks (measured unless marked)

- **73 hairpin ramps, 5 legato-overlap steps, celli 870.4:** finding 5. No rate limit. Move the trims into CC7, after a woodwind CC7 range test. Only the stopped horns are heard as wrong-way moves (finding 4).
- **Bars 223 and 263:**
  - EBU momentary maximum on the mp3: 278 -7.67, 263 -8.33, 277 -8.39, 223 -8.41, 212 -8.53 LUFS. The final leads by 0.66 LU or more.
  - Both 223 and 263 are printed fff. In the score, 223 is a single tutti stroke falling to f at 224, while 263 is a sustained tutti chord with crash. A tie meets the printed order, so do not spend a ride on it.
  - The weak step at 263 (+0.8) is the celli and Violins I falling at the arrival, and the fix is finding 1.
  - The 259-262 crescendo is back-loaded: master bars -18.2, -18.1, -17.0, -14.8. That is critic C's area.
- **Violins I chord fronts:** finding 6.
- **Basses' pp re-bow swells (170.859 / 181.676 / 190.533):**
  - The CC11 counter-shape is in the lane: 32 -> 18 from +0.45 to +0.9 s. Yet the stem still peaks at +1.0 s (170.859: -52.8, against -56..-58 before and after).
  - So the Basses Sus MAX hardly answers CC11 at 18-32, and the swell is the sample's bow bloom.
  - Fix: put the counter-shape in CC7 (instrument side, 20 log10) over +0.6 to +1.4 s: 127 -> 74 (-4.7 dB) at 170.859, 93 (-2.7 dB) at 181.676, 60 (-6.5 dB) at 190.533.
- **Muted Trumpet 1 joins:** my measure is the minimum within -80 to +150 ms against the lower of the two bodies, K. It gives 3.7 / 7.1 / 3.9 / 5.1 dB at 685 / 688 / 717 / 726, so 688 is the one left. That is critic A's area; I did not re-test overlaps.
- **Trumpet 1 at 989:** by note body (+0.06 s to the end), 989 is the second-loudest note of the slur, -34.5 against a slur median of -40.2 dB. I cannot confirm "softest" with this measure. No change.
- **Bassoon 1 at 514:** the new note's body sits 7.2 dB under the note before (-47.6 -> -54.8); it is not a dip inside the join. A woodwind CC11 offset on that note, about +6 units, would raise it about 3 dB (inferred; at the layer slope of section 4 of the kit LEARNINGS).
- **Flute 1 run holes:** not re-measured (critic A's area).
- **Violas against Trumpet 1, 840-842:**
  - Violas minus the melody per 0.5 qn: -7.2 / -5.1 / -4.7 / -6.5 dB, counting the doubled melody (Trumpets 1-2, Flute 1, Oboe 1, Clarinet 1, per the doubling rule).
  - Against Trumpet 1 alone: -1.0 / -0.2 / +1.3 / -2.1 dB.
  - Close the item as met.
- **Celli 235-237 under the basses:** finding 3.
- **Listening on earbuds (inferred from the measures):**
  1. From bar 199 on, every ff and fff peaks within 1.4 LU on the mp3 (199 -9.2, 211 -8.9, 212 -8.5, 223 -8.4, 255 -8.9, 263 -8.3). The ff of theme B at 212 sits only 0.12 LU under the fff of 223. That comes from delivery at -14 (Movement I c62). A `RIDE_TRIMS` row of -1 dB over 840-856 would put 212 about 1 LU under 223.
  2. In the Più allegro (265-268), Trumpet 1 alone is 3-7 dB under the master. The a2 is on one track, with a +3 dB role over 1054-1071.5. Strings (f) and winds (ff) sit 6-10 dB under it, 2-4 dB more than Rimsky-Korsakov's resonance ratios give. Worth -2 dB on that role after findings 1-2.
  3. The inner lines of findings 1-2 are what an earbud listener misses.

## Findings from the other movements

- **Room-noise bed:** applies and is in place. It measures -60 LUFS, about 38 dB under the mp3's 10th percentile (-21.7).
- **Slope guard with no skipped windows (scherzo c24):** applies. guard26 still exempts 1.5 s after fp / sfp, where the trims move 60 dB/s (finding 5).
- **Phrase-shape start -12 burying lyrical entries (scherzo c24):** partly applies. Trumpet 1's solo entry at 200 starts 8.3 dB under its level at 0.8-1.6 s: CC1 36 -> 50 crosses the 30-36 layer boundary. The cor anglais at 680 starts 5.8 dB under. Both stay over their accompaniment (pizzicato -55..-65 dB), so they are not buried. A start of -4 in `PHRASE_SHAPE` "lyric_spans" (the scherzo's value) would take about 3 dB off the swell (inferred).
- **Pizzicato basses over celli at the same p (scherzo c24):** applies. In bars 51-66 the basses are 3.1-8.5 dB over the celli (K, per 2 bars), even with the role [200, 264, -4]. That role -4 -> -7 would bring them within about 1-5 dB (inferred). Low priority.
- **Not checked (other lenses):** the scherzo's soft slurred pairs and CC1 floor, the Violins I short-row round-robin ring, and late celli leaps. The crescendo ramp under a rest map is handled in c26's CHANGES (`instr_post` order).

**Do not touch:**
- the c26 CC7 passage levels (Violins I 80 at 632-660, violas 90 at 839-848);
- Trumpet 1's open-solo role [200, 264, +3.2] and the cor anglais / muted trumpet roles 680-744 (solos 12-18 dB over their accompaniment);
- the bassoon solo (10-14 dB over the strings);
- the theme-B melody balance counted with its doublings;
- `TIMP_ARRIVAL_RAMP` 888 / 1048 / 1108 (timpani 11.7 / 12.5 dB under the master);
- crash and bass drum at 223 / 263 / 278 (12-14 dB under the master, never the top stem);
- the chorale brass over the string tremolo at 224-225;
- Horns 2 / 4 "Mono From Left";
- k 20 on brass and clarinet `cc_scale`;
- the -14 LUFS delivery chain with the room bed and the 0.30 s head;
- the c26 stop fixes at bars 94 / 113.
