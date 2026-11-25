# Critic C, cycle 42: dynamics over time (render c41, score v621)

Render under review: c41 final (`cycles/c41/render`, 38 stems, master = float stem sum), the delivered `mvt1-mockup-c41.mp3`, and `build/` as it stands after the c41 stem fix (parts.json 03:12, the data the final stems carry). Score pages 2, 4, 6, 7, 12, 13, 16 and 18 were rendered and read. Envelopes come from `build_reaper.vol_points()` loaded the way `stem_fix.py` loads it, so "Opus output" below means stem minus post-hall envelope (exact, since the envelope is a pure gain after the instance). Levels are stereo power. Scratch scripts were in `/private/tmp/claude-501/mockup-loop/mvt1-c42-C/` and are deleted.

## Manual notes (second reading of the c36 C row: PDF pages 53-54 and 63-64, 101-102, read in full; MANUAL-GAPS.md and DIGEST.md read)

Open MANUAL-GAPS items that touch this lens come first.

| Manual (PDF page) | What it says | Where it applies here | Does the render follow it now? |
|---|---|---|---|
| p.123, p.125 (MANUAL-GAPS #12, open) | Felt Cresc: recorded crescendo rolls ending on a stroke, "the most realism" | the 13 timpani crescendo hairpins | Not tried. The rolls on CC1 grow a median +6.2 dB, 2 of 13 under 1.5 dB (measured). The gain stays low. Keep it open. |
| p.109 (MANUAL-GAPS #5, open) | Sus Exp / Leg Slur Exp: slower attack and a gently increasing vibrato | espr. wind solos | Not tried. The cor anglais' espr. solo in bars 5-8 is the place to test it (Finding 2). |
| p.104-105 (brass crescendo rows, ranked low in MANUAL-GAPS) | Cres Fst/Med/Slw are "often more realistic than using MIDI volume" | held brass crescendos | Not tried. No brass crescendo fails within 8 dB of the master (see p.101 below), so there is no reason to try them now. |
| p.101 (MANUAL-GAPS #1, open) | Sustain Marcato: velocity sets a low-pass on the attack | brass accents | Still GENTLE_ACCENT by design. Item 8 is met: 150 brass accents of 0.75 qn or longer measure 2-5 kHz in the first 80 ms minus body at a median of -15.7 dB, p90 -8.0, max +2.9 (measured). |
| p.53 (c36: partly followed) | Shape sustained lines with CCs. Velocity is fixed per note. | every held note that starts a hairpin | Now mostly followed. 159 held notes (1.2 s or longer) start a crescendo: median growth +5.4 dB (strings +5.9, winds +5.8, brass +4.8). 34 of them (21%) end under the peak of their first 0.4 s; c36 counted 20 of 36. Almost all are 10 dB or more under the master. The exposed exceptions are cor anglais qn 24 (+1.6 dB, Finding 2), celli 440 (-4.9 dB, the first note of the 24-qn crescendo into the stringendo, -8.3 dB re master) and Horn 1 408 (-2.7 dB, -8.6 re master). Measured. |
| p.54 (c36: yes) | Velocity is one node per note; CC1/CC11 are curves through the notes | all lanes | Yes, unchanged. |
| p.63-64 (c36: yes, but the envelope is after the hall) | CCs crossfade simultaneous layers. CC7 sets a track's level against the others; CC11 shapes the line. | balance in the post-hall envelope; CC11/CC1 per printed dynamic | Still yes, and bar 62 still pays for the post-hall envelope (Finding 1). What the second reading adds: (a) The crossfade explains the subito. In Opus output, Violins II's forte-to-sub.-p step is only 5.5 dB (CC11 86 to 49). The other 12.8 dB is post-hall envelope (measured). (b) CC7 is a voice-stage gain. It moves sounding timpani rolls (score_to_parts c13: slopes 0.79-1.10 against 20·log10 CC7) and left a hall tail untouched (MANUAL-GAPS Results c36). A CC7 step at a subito therefore also cuts the forte's release voices, which carry the first 0.15 s of a violin release here (Finding 1; inferred from those two measurements). (c) The c36 test lane `CC7_POINTS["Trombone 1"]` (679.32-679.97) is still in `build/score_config.py`. It does nothing, because the trombone rests from 679 to 695.9; remove it when touching CC7. |
| p.64 (c36: yes) | LITE string patches: CC1 sets dynamics and vibrato together | Sus Marc LITE strokes | Still 14 notes on the row (parts.json art_counts). Not re-measured. |
| p.101 (c36: crescendos +3.0 dB, 14% wrong way) | Brass Sustain: all 4 layers sound; CC1 picks 1-2, so a held note can crescendo | held brass hairpins (`CC1_DYN_MAP`) | Followed. Held brass crescendos grow a median +4.8 dB, 8 of 54 the wrong way (15%). 16 end under their attack peak, all but one 10 dB or more under the master. Held decrescendos fall a median -8.2 dB, 1 of 34 the wrong way. Measured. |
| p.101 (c36: met) | Sustains loop | BRIEF item 7 | Met. 48 held notes of 6 s or more were scanned (c25 loopscan). None reaches 0.4 at 3.95 s except Bass clarinet qn 492: band 0.84, centroid 0.71, -12.3 dB re master. That reading comes from its two breath-split dips 4.8 and 4.1 qn apart (17 dB deep at 496.8), not from a loop. The Lento master over bars 5-12 reads -0.11 / -0.19 and the final chord -0.13 / +0.14 (band / centroid). Measured. |
| p.101 (new) | Legato Repetitions: retongued repeats inside a legato phrase | S1 | Now in use: LegRep RRx4 on 11 brass and 26 wind notes, Leg Slur Rep on 12 (parts.json art_counts). MANUAL-GAPS #2 is done in part. |
| p.102 (c36: cut-offs like the reference) | Shorts have no release trails; let the last note ring; brass staccato at top velocity overblows | cut-offs | Unchanged. No brass track plays a short row (art_counts), so the overblow warning does not apply. The tutti fermata release at qn 679 falls -3.3 / -4.9 / -8.8 / -13.2 / -16.1 / -21.6 dB over 0-0.05 / 0.05-0.1 / 0.1-0.2 / 0.2-0.3 / 0.3-0.5 / 0.5-0.8 s, and the final release decays about 28 dB/s. Measured. |

## State through this lens (measured unless marked)

- **Arc.** Bar level against the bar's loudest printed dynamic: r 0.89, slope 4.6 dB per step (plain RMS).
- **Sostenuto climax.** The bar-122 fff (tam-tam) arrives +3.3 dB over bar 121's last beat. The master then falls 22 dB from bar 122 to bar 126, in the printed order (fff, decrescendo, f, mp, p). The tam-tam sits 7-10 dB under the master in bars 122-123 and 19-21 dB under by bar 126, and is damped at 505.
  - Bar 121's crescendo looks stalled on its last beat (-0.2 dB), but that is the printed eighth rest in Trombones 1-2, Bass trombone and Tuba before the fff. It is a breath, not a defect.
- **Main climax.** Bar 159 grows +3.6 dB over four beats, starting 1.4 dB under bar 158's peak (the printed breath). Bar 160 arrives +3.3 dB over 159's last beat.
  - The cymbal roll is inaudible until beat 3 of bar 159 (4-12 kHz 26 dB under the master), then reaches -5 dB at the stroke. With the K Crash ring, the cymbals stay within 3-8 dB of the master's 4-12 kHz for 2 s.
- **Recapitulation.** Bars 127-131 rise +5.2 / +6.2 / +4.7 dB (pp to mf, to f, to ff).
- **Coda.** Bars 175-180 hold at pp (-40.5..-41.3 dB). The morendo takes bar 181 down 5 dB and bar 182 a further 4 dB, then the release.
- **Delivery (item 6).** mp3 -19.8 LUFS, LRA 14.9 LU, span 19.2 dB (0.2 over the target), limiter about 0.5 dB. Of 2758 five-second moves of 3 dB or more, 2 are inverted; the median share kept is 0.81. Climax order 160 > 122 > 167-170 > 26. Master LRA 23.6 LU (Dvořák 9/i 21.8).
- **Hairpins.**
  - Crescendos grow a median +4.8 (strings), +5.2 (winds), +4.8 (brass) and +6.2 dB (timpani), 4-8% the wrong way.
  - Decrescendos fall -5.7, -5.1, -6.5 and -5.4 dB, 4-12% the wrong way.
  - The exposed short swells of the celli/horn dolce tune (bars 48-51, 148-151) follow their < > within a note or two.
- **Dan's notes.**
  - Item 5 (timpani rolls) holds: the bar-62 pp roll sits 10 dB under the master.
  - S1 and S2 were not re-measured. c41 left the string joins and repeats as in c40 (Violins I was rebuilt to match c40 at 0.00 dB median), so c41 C's numbers on c40 still describe the strings. c41's brass repeat changes are in its CHANGES.md.
  - S3: bar 84 now decays like a release: +0.5 / -2.1 / -7.4 / -9.4 / -13.7 dB at 0-0.05 / 0.05-0.1 / 0.1-0.2 / 0.2-0.3 / 0.3-0.5 s. Bar 62 does not (Finding 1).
- **Real recording (inferred, different piece).** In the Dvořák reference the loudest 5% of short-term loudness lies within 1.6 dB of its maximum. In this master it lies within 5.7 dB (mp3 4.3). The climaxes here are narrower peaks than a real tutti plateau. The score has two fff bars against several ff passages, so this is context, not a fault to fix.

## Findings, ranked by what a listener would gain

### 1. Bar 62's sub. p (Dan's S3): the forte is cut 0.13 s before the beat with a +4.5 dB burst, then falls 3-5 dB faster than a release, and dips 3 dB under the p level that follows. A CC7 step would not fix it. Ending the forte on its own instance would. (Problem measured; variants simulated with a model, inferred.)

**Where.** Bar 62, qn 243.7-245. Violins I and II carry 75% of the forte's power in the 0.3 s before the mark. Horn 3 (-16.5 dB re master), Clarinet 1 (-19.1), the celli (-13.2) and the basses (-16.7) carry the rest.

**What is wrong (measured).**

Master level per window, relative to its mean over -0.35..-0.15 s before the beat at 244.0:

| s re beat | -0.15..-0.10 | -0.10..-0.05 | -0.05..0 | 0..0.05 | 0.05..0.1 | 0.1..0.2 | 0.2..0.3 | 0.3..0.5 | 0.5..0.8 | 0.8..1.2 |
|---|---|---|---|---|---|---|---|---|---|---|
| bar 62, c41 | +3.1 | -1.9 | -4.7 | -8.4 | -10.5 | -13.3 | -15.3 | -15.3 | -12.9 | -11.9 |
| fermata release, qn 679 | -0.6 | -0.5 | -1.8 | -3.3 | -4.9 | -8.8 | -13.2 | -16.1 | -21.6 | -30.5 |

Four things make that row:

- **(a) Timing.** The fall starts 0.12-0.13 s before the beat. The violins' forte note ends at 243.746. The p note starts at 243.776 (the fresh-entry lead of `SUBITO_FRESH`). `SUBITO_TAIL` starts its fall at that moved onset.
- **(b) A burst.** At the note-off, Violins II's Opus output jumps 7-8 dB for 40 ms (from -23 to -15 dB re the master reference), a release burst. The envelope there is still at the forte value (+18.8 dB), so the master's 20 ms peak is +4.5 dB over the forte, just before the subito.
- **(c) The fall is mostly post-hall.** The violins' post-hall envelope falls 12.8 dB (Violins I +17.8 to +5.0 dB, Violins II +18.8 to +6.0, gain included): 4 dB at 243.776, the rest by 244.43. Of that crescendo top, about +12 dB is vol_db built up over bars 60-61 (hairpin gain and level shapes such as `_hp236`; Violins I vol_db -1.1 dB at 235.5, +13.0 dB at 243.9). Opus output falls only 5.5 dB. So 70% of the subito is a post-hall cut, and it takes the forte's hall tail with it.
- **(d) A hole.** At 0.2-0.5 s the master is 2.4-3.4 dB under the p level it settles at from 0.5 s. The first p note (E-flat) is also about 3 dB softer than the C that follows at +0.35 s.

Aligned on its own start, the bar-62 fall is 3-5 dB faster than the fermata release over 0.08-0.22 s. Relative to the beat it is 5-6 dB lower at 0-0.1 s.

**The CC7 proposal (c41 C Finding 4), checked.**

What the evidence says:
- CC7 is a voice-stage gain. It moves sounding timpani rolls (c13 slopes) and did not touch a hall tail (c36). So a CC7 step at 243.766 cuts the forte's release voices at once.
- On this render, string releases measure a median -4.6 dB at +0.1 s.
- The hall's own share is small. The late-slope fits of 12 Violins I/II cut-offs extrapolate the hall tail to a median -7.8 dB under the sustain at the cut-off, decaying 20-33 dB/s. The strings' send is 0.25.
- So the first 0.15 s of a violin release is mostly release voices, and CC7 would remove them as fast as the envelope does now.

The model:
- Opus output is split into a hall tail (sustain -8 dB, -27 dB/s) and the rest.
- The natural release shape is the measured Violins I/II release at qn 678.9.
- Applied to the violins only, CC7 gives -6.1 / -7.8 / -10.1 / -11.2 / -12.9 / -14.7 dB over -0.10..0.3 s.
  - That is 3-4 dB lower than now before the beat, and only 0.4-2.4 dB higher after it.
  - With the hall share at -4 dB the gain is at most +2.4 dB; at -11 dB it is about +1 dB.
- It also leaves (a) and (b) unchanged. Not recommended.
- If the actor wants it as a side test anyway:
  - `CC7_POINTS = {"Violins I": [(243.766, 29), (244.239, 37), (244.718, 48), (245.197, 61), (245.676, 78), (246.156, 99), (246.636, 127)]}`, and the same for "Violins II". This is CC7 = round(127·10^(-Δ/20)) for a remaining drop Δ falling 12.8 dB to 0 over 1.5 s.
  - It needs a per-track SUBITO_TAIL override (`{"at_once_db": 0, "ramp_s": 1.5}`) in `build_reaper.vol_points()`, so that the envelope and CC7 multiply to the post level at every moment.
  - Run it as a TEST_TRACKS alias of Violins I over 236-252 in pass 2.

**Fix (recommended): let the forte end on its own instance, as a real section would, and start the p notes fresh on the main track.**

1. **`build/score_config.py`, new c42 block.**
   - `_SUB62 = [(218.5, 243.9)]`. This window covers the phrase from the bar-55 pickup, Violins I/II score onsets 219-243.5. The previous notes end by 217.91, so the window starts after a rest.
   - `TRACK_WINDOWS = {**TRACK_WINDOWS, "Violins I": (_SUB62, False), "Violins II": (_SUB62, False)}`.
   - `ALIAS_TRACKS["Violins I f62"] = {"source": "Violins I", "windows": _SUB62}` and the same for "Violins II f62".
   - Add both to `PASS2_TRACKS`.
   - In `build/mix.json`, copy each source's track entry (gain, seat, width, send, mics, EQ, loud_eq, side shelves, trims).
   - The aliases inherit the sources' per-onset tables: leg_leads, join notches, the bar 55-59 sul spans and the bars 60-61 crescendo shapes.
   - Memory: two string KS Master instances in pass 2 (c40: about 5 GB each). The main project is unchanged.
2. **`tools/build_reaper.py vol_points()`, SUBITO_TAIL loop (generic).**
   - When the track has no note whose score onset lies within 0.05 qn of the mark (`not any(abs(n.get("sq", n["qn"]) - s_) < 0.05 for n in tr["notes"])`), do not fall.
   - Instead, hold `pre` (the value at fs_ - 0.002) from fs_ until TAIL_HOLD_LEAD_S before the track's next moved onset (or the end), then `continue`.
   - Without this the alias's tail would still be cut. Its subito_falls entry falls back to the mark itself (score_to_parts: "else the mark itself"), and the vol_db shapes ending at 243.94 would be held at their fallen value by the tail hold.
3. **`tools/score_to_parts.py` (generic, for ALIAS_TRACKS).** Drop CC11/CC1 points after the alias's last note-off, so each lane holds its last value. CC11 is voice-stage: a drop to 46-49 at 244 would cut the forte's release voices about 5 dB. Check in parts.json that "Violins I f62" cc11 stays at 86 after 243.6.
4. **The forte's end.** On the alias, the last note (sq 243.5) has no following note. It should end at its written end, 244.0: check parts.json (between 243.95 and 244.0; `NOTE_END_AT` alias table if not). The main Violins I/II keep their p notes (moved onset 243.776, CC11 49). They are silent before them, so SUBITO_TAIL moves their whole drop to the fall qn and they start at the post level.
5. **Burst check.** On the alias stems, if the 20 ms peak in [note-off - 0.02, + 0.08 s] exceeds the note's body by more than 2 dB (Violins II did by +6.8), add an alias `LEVEL_SHAPES_S` row at 244.0: `[(-0.03, 0.0), (-0.01, -5.0), (0.06, -5.0), (0.09, 0.0)]`.

**Expected (model, inferred):** -0.3 / -1.8 / -2.1 / -5.6 / -8.3 / -11.4 / -14.2 dB over -0.10..0.5 s. That is within 0.2-1.9 dB of the fermata release from -0.10 to +0.3 s, with the p level unchanged from +0.5 s. The violins hold to the beat and their ring bridges into the p, which removes (a) and (d).

**Pass criteria (measured on the render):**
- Master over 0-0.05 / 0.05-0.1 / 0.1-0.2 / 0.2-0.3 s within 2 dB of -3.3 / -4.9 / -8.8 / -13.2 (same reference window).
- No 20 ms frame in -0.3..+0.05 s more than 2 dB over the reference (now +4.5).
- From +0.5 s, the master within 1 dB of c41 (-12.9 / -11.9 / -13.6 at 0.5-0.8 / 0.8-1.2 / 1.2-1.6 s).
- The alias stems within 1 dB of c41's Violins I/II per 1 s frame (median) over 219-243.5, as c41's test aliases matched their sources.

**Fallback if the aliases cannot go into c42 (level only, so it can be done by stem fix with `--old-src`).**
- A Violins II notch, `LEVEL_SHAPES["Violins II"] += [[(243.72, 0.0), (243.73, -6.0), (243.80, -6.0), (243.81, 0.0)]]`.
- `SUBITO_TAIL` `at_once_db` 4.0 -> 2.0 and `ramp_s` 0.35 -> 0.6. This changes the bar-62 falls of Violins I/II (12.8 dB), Horn 3 (8.0), Clarinet 1 (5.9), Horn 2 (5.3) and the basses (4.6). Bar 84 has no positive fall (the envelopes rise there), so nothing changes there.
- Simulated on the c41 stems: +1.9 / 0.0 / -2.5 / -6.0 / -8.1 / -11.0 / -12.7 / -14.3 dB over -0.15..0.5 s. That is 2.3-2.6 dB nearer the release at 0-0.3 s, and the 20 ms peak goes from +4.5 to about +2 dB.
- The timing (a) remains.

### 2. The cor anglais' opening espr. solo: the bar-7 swell grows only 1.6 dB, against 5.4-6 dB for the falls around it (measured problem; fix values inferred)

**Where.** Cor anglais, bar 7, qn 24-26 crescendo and 26-28 decrescendo, the first wind solo of the movement. The cor anglais is the loudest voice there (-1.3 dB re master).

**What is wrong (measured).**
- The stem rises -37.2 to -35.6 dB over 24.1-25.8.
- Around it, the bar-6 decrescendo falls 5.4 dB (20.5 to 23.0) and the bar-7 decrescendo 6.0 dB (26.4 to 28.1).
- The printed hairpins are alike: dyn curve tops 68 at 20 and at 26, from 46-55.

**Cause (measured).**
- CC11 adds about 3 dB (55 to 73; Opus output -45.3 to -42.2).
- The envelope falls 8.1 to 6.4 dB through the crescendo:
  - the soft trim tapers from p (+5) toward mf (+2.5) as the CC rises (mix.json Cor anglais `soft_trim_db`);
  - a 1.4 dB dip at 24.75-25.0 in vol_db.
- Together these cancel the +3 dB hpgain (`hpgain [24, 26, 3.0]`).

**Fix.**
- Add `LEVEL_SHAPES["Cor anglais"] += [[(24.1, 0.0), (25.9, 2.5), (26.25, 2.5), (27.75, 0.0)]]` in `build/score_config.py`. This is level only, so it can be stem-fixed.
- Targets (inferred):
  - the stem over 25.6-26.0 at least 4 dB over 24.1-24.5;
  - the decrescendo to 28 at least -6 dB;
  - the swell's peak no more than 1.5 dB over the bar-6 peak (-34.6 dB), since both hairpins top at the same printed level.
- Alternative for the listener: MANUAL-GAPS #5 as a pass-2 test alias, Cor anglais 19-31 on "Leg Slur Exp" (p.109: slower attack, gently increasing vibrato), which may give this solo its swells from the samples.

## Do not touch

- The movement's dynamic plan (r 0.89).
- The c36-c41 climax set:
  - the `_all` rows into 484 and 636 with the 636 arrival lift and CAESURA;
  - bar 121's brass breath (the printed eighth rest);
  - the tam-tam and cymbal/K-crash ring shapes and damps.
- The delivery ride with RIDE_TRIMS (2 inversions in 2758 moves).
- `SUBITO_FRESH` (the p note as a fresh entry stays in every variant above).
- HP_NIENTE / HELD_DECRESC_DB, CRESC_FRONTS, the soft hairpin gains.
- TIMP_CC1_MAP with the roll trims.
- AUTO_REBOW and the breath splits with their fitted shapes (no held note loops).
- GENTLE_ACCENT (item 8 met).
- The coda morendo and the final release.
