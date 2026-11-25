# Cycle 28, critic B (balance and levels), on the c27 render

I measured on `cycles/c27/render` (stems and master), `cycles/c18/render` (stems, allowing for the -3 dB global gain since c26), the c26 master and `cycles/c27/build_render/` (identical to `build/`: parts.json, mix.json, roles.json and score_config.py compare equal).
- The lanes REAPER got were rebuilt with the actor's `net27.py` method (`tools/build_reaper.py` cut before `ENV_LUA`, then `vol_points` and `cc7_lane`). My `--netmoves` run reproduces `records/netmoves_c27.txt` exactly: 398 / 350 / 48.
- "Net" means envelope dB + 20 log10(CC7/127).
- Inner lines: the inner23 measure (a line's power over all other stems plus the returns, in its best 1/6-octave band, doublers joined). I ran it on every one of the 61 printed espress. / dolce / leggiero / scherz. entries, on c27 and on c18.
- (m) = measured, (i) = inferred.

## Manual notes

`loop/MANUAL-READING.md` has no row for c28, so I chose pages for this cycle's questions: divisi loudness, row and master volume, and CC7 against CC11. From the May 2021 manual I read pp.89-90, 137, 140, 150 and 151 in full. I also used `loop/MANUAL-GAPS.md` (#9, #12, the c15 / c25 results).

| what the manual says (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| The divisi patches are Close-only, one chair per stand. "The loudness of a divisi part is not much less than if the whole section were playing" (p.89-90) | Violas div (DIV B, upper third) against Violas (full section, lower third), bars 209-224 | Roughly. The upper voice averages 2.3 dB under the lower over 32 note pairs at qn 625-672 (m), but the pairs range from -10.2 to +7.0 dB. Fixing finding 1 removes the largest part of that spread. |
| Each articulation row has its own volume knob (p.137) | `region_gain_db` / `row_dyn_db` (Sus Marc LITE vel<66 -6 dB, Spiccato F sharp v90+ -3 dB) | Yes. These are instrument-side levels, as Dan's rule asks. |
| The master GAIN changes the output without changing the mic mix (p.140) | `global_gain_db` -3 | Yes. |
| Velocity "cannot be changed mid-note" and selects the dynamic layer (p.150) | the violas' slurred tenuto pairs, bars 209-216: v112 where the pair changes pitch (626, 632), v66 where it repeats a pitch (629, 635-647) | Mechanically yes. But the same printed figure (mf, tenuto, slurred) gets two layers, and this adds to the fall in finding 1 (i). |
| CC7 is "best used to set the overall upper limit ... relative to each of the other tracks, as opposed to shaping an individual musical line" (p.151) | the CC7 trim lane; the cap release on the celli at 631.6-635.1; the summit arrival-weight tails | Mostly yes: the lane holds passage levels. Two exceptions shape a line in CC7: the celli's 5.3 dB CC7 ramp inside legato notes (finding 1) and the 1.1-1.2 dB tails inside the summit notes (finding 3). |
| LITE string rows: CC1 sets dynamics and vibrato, CC11 only loudness (p.151) | Violins I "Sus Marc LITE" soft heads | Outside my lens; noted for critic A. |

## Findings, ranked by what a listener would hear

### 1. Trio climax, bars 210-216 (qn 627-648): the violas and celli accompaniment drops 4-13 dB under an unchanged printed mf. This is the "632 step" (m)

**Print (m).** Violins I / II have the tune f espress., with short swells at 632-634, 639-642 and 644-646. The celli are mf from 624 and the violas mf div. from 625. All of them have the same figure in every bar (the violas play slurred tenuto pairs). There is no new mark until the crescendo at 648 / 649 into the ff of 653.

**What the lanes do (net, dB).**

| track | 624-627 | 628-633 | after the step | mechanism |
|---|---|---|---|---|
| Violoncellos | +2.6 | +2.6 | falls to -2.8 between 631.6 and 635.1 | `cresc_trim_hold` reaches its 8 qn cap (624 + 8 = 632). The celli are legato and every note overlaps the next, so there is no re-attack for a cap step. The release becomes a 5.3 dB CC7 ramp through notes 632, 634 and 635 (CC7 101 -> 55) |
| Violas | +6.75 | +4.75 | +1.27 from 633.5 | (a) the HP gain (+2.0, cresc 618-625) is released at 627.0-628.4, in the 0.5 qn gap between two slurred pairs (the hold's "first rest of 0.5 qn" stop); (b) the trim-hold cap is a 3.5 dB step at 633.1-633.5 before the moved note-on 633.544 |
| Violas div | +7.9 | +5.9 | +3.3 from 633.5 | same, 2.0 + 2.6 dB |

**What the stems do (m).**
- Violas pair heads, first 250 ms: 625 -40.3, 631 -40.7, then 634 -48.5, 637 -54.1, 640 / 643 -51.6, 646 -48.3 dB.
- Violas per bar (209-216): -40.5 / -41.4 / -42.2 / -45.9 / -50.0 / -49.7 / -50.1 / -46.9 dB.
- Celli per bar: -39.1 / -35.9 / -40.5 / -41.6 / -43.1 / -43.4 / -43.5 / -42.3 dB.
- Master per bar 209-217: -31.5 / -30.9 / -31.1 / -31.8 / -33.3 / -33.8 / -35.4 / -33.6 / -31.2. That is a 4.5 dB sag into bar 215 before the crescendo, with nothing printed.
- c27 against c26: bars 210 / 211 are +1.9 / +2.0 dB, because the new hold restored them to the c18 level. The fall after them is the release. CHANGES.md filed these two bars under "crescendo holds before bar 72", but they are qn 627-633, this passage.
- The violas' velocity layers (p.150 row above) add a few dB to the fall from 634 on (i).

**Tune margin (m).** Holding the accompaniment up costs the tune nothing measurable here.
- The Violins I line (Flute 1, Clarinet 1 and Violins II join it as doublers) is +14.8 to +17.2 dB over all others in its best band (2.3-4 kHz), in every 3 qn window from 624 to 651.
- The celli line lives in 160-570 Hz. It falls from +9.1 / +11.8 dB over all others (bars 210-211) to +2.9 / +3.7 (bars 213-216).
- So the actor's objection to a long hold (c27: "celli +5.4 dB for 13 qn") holds the inner lines up, which is what Dan asked for on 11-17. It does not cover the tune.

**Fix (generic, off by default).**
- `tools/build_reaper.py` `vol_points`, cresc_trim_hold: add mix.json keys `"hold_to_dec_qn": 32` and `"rest_min_qn": 2.0`.
  - When the track keeps playing with no rest of 2 qn or more, and no softer printed mark comes before a printed decrescendo starting within 32 qn of the arrival, the held trim stays until that decrescendo.
  - It is then released linearly across the decrescendo (a printed move): celli to 654-660, violas to 655-661.
  - The 8 qn cap with its rest / re-attack release stays for every other case.
- `tools/score_to_parts.py` `_keep()`: add the same two keys to HP_GAIN_TO_CC11 (`hold_to_dec_qn` 32, `hold_rest_min_qn` 2.0 in the c27 block at score_config.py line 2290). A gap under 2 qn between slurred pairs or staccatos then no longer ends the hold. This removes the violas' 627 release.

**Expected (i).**
- Celli +5.4 dB and violas +3.5 to +5.5 dB over 633-648.
- Master bars 213-216 about +1.5 dB, so the plateau before the 648 crescendo is flat.
- No in-note ramp on the celli.

**Check after the build.**
- The 648-653 crescendo still rises at least 3 dB on the master. It is CC11 75 -> 84+ plus the strings' own crescendo gains.
- The Violins I line stays 12 dB or more over all others at 633-651.

### 2. Crescendo arrivals still sag 3-6 dB within 1-3 qn on 40 track-arrivals. The c27 hold misses two cases (m)

**Measure.** For every printed crescendo, the net level from its end to the first of: the next hairpin, a falling dynamic curve, a rest of 0.5 qn, or 8 qn later. I counted only frames where the track sounds. 55 arrivals fall 1.5 dB or more. Leaving out the summit weight (finding 3) and the brass at 996 leaves 40.

**The repeating ones.**
- 120 (bar 41): Oboe 1 7.0, Flute 1 4.0, Violins I / II and violas 3.0.
- 156 (bar 53): Flute 1 4.1, cor anglais 4.1, Violins I / II 2.9 / 3.0.
- 309 / 310 (bar 104, the ff of the tutti): Flute 2 5.8, Oboe 1 6.2, Clarinet 2 4.1, cor anglais 3.6, Violins I / II 3.0.
- 384 / 852 (bars 129 / 285): Flute 1 4.1, Oboe 1 4.6, Violins I / II 2.9-3.0.
- 909 / 910 (bar 304): Flute 2 4.0, Oboe 1 5.7, Clarinet 2 4.1, Violins I 4.5, Violins II 3.0.
- 204 / 888: violas and celli 3.0-3.1.
- 588 / 816: Violins I 2.1 / 3.0.

**Two mechanisms (m).**
1. **Short arrival notes skip `_keep()`.** In `score_to_parts.py`'s HP_GAIN_TO_CC11 loop (about line 5760), a gain with no note sounding at least `min_s` (0.25 s) past its release point hits a bare `continue`. That gain never reaches `_keep()`, so `hold_until_mark_qn` does not apply. It keeps the old HP_REL release, which `note_slew` and `stretch_cc7` then spread into a ramp.
   - Example, Flute 1 at 156: vol_db is held only to 157.09 and back to 0 by 158. In CC7 this becomes a 4.2 dB fall from 156.04 to 159.6 (CC7 65 -> 40) under the printed f, with nothing printed until the crescendo of 159.
   - The cor anglais at 156 is the same case.
2. **Short gaps end the hold.** The hold's "first rest of 0.5 qn" stop fires on the gap after the first staccato quarter.
   - Violins I's +3.0 dB gain of the 300-310 crescendo is released at 312.6-313.5, inside the first bar of the ff tutti theme. Violins II is the same (-2.8), and so are the strings at 120, 384 and 852.

**What a listener hears.**
- The master falls 4.2 dB from bar 104 to bar 106 (-19.8 -> -24.0 RMS). Most of that is the writing: the held brass chord of bar 104 gives way to the trumpets' repeated quarters, Horns 1 / 2 / 4, Oboe 2 and Clarinet 1 rest, and the basses' stem falls 9 dB (m).
- The mixing part is the strings' and winds' 3-6 dB. Their stems fall 3.1-4.9 dB (Violins II -3.2, violas -3.1, Oboe 1 -4.9, Clarinet 2 -4.8). On the mp3 this makes the "105 -0.5 / 305 -0.4" reversed arrivals in CHANGES.md (BRIEF item 6) (i).

**Fix.**
- (a) `score_to_parts.py`: replace that bare `continue` with `_keep(it, r0_, g_); continue`. Short arrival notes then hold like the others.
- (b) The `hold_rest_min_qn` 2.0 from finding 1.
- (c) For the two tutti arrivals, do not hold the overshoot, because the hold would lift the whole ff tutti and narrow the summit's lead (105-120 is only 1.2 LU under the summit on the mp3). Instead add 309.0 / 310.0 / 909.0 / 910.0 to `drop_ends` in `_hp18w` and the strings' HP_GAIN_TO_CC11 entry (score_config.py lines 1620-1624, where 213 / 897 already are). Those crescendos then rise on CC11 (89 -> 114) and the brass entries alone, and arrive at the tutti level with no release.

**Expected (i).**
- After (a) and (b), the arrivals at 120 / 156 / 384 / 852 hold to the next printed change or the 8 qn cap.
- After (c), bars 104 / 304 are about 1-2 dB lower, and the ff tutti is not lowered.

**Check after the build.** The mp3 arrival list: 105 and 305 should become positive. Summit lead at least +0.5 LU, f -> ff at least 2 LU, LRA at least 10.5.

### 3. The summit stroke at 1005 is a single-note fader row on 15 tracks, and it is why the summit leads by only +0.57 LU (m)

**What it is.** `ARRIVAL_WEIGHT_AT` {1005: (-2.0, 3.0, 1.0)} with ARRIVAL_WEIGHT_HOLD_CAP 1.5 adds +3 dB to the fff stroke on all woodwinds and strings for 1.5 qn. It then takes the 3 dB back as a step at the next note-on 1007.5.
- Double basses: net 5.0 -> 2.0. Clarinet 1: 9.5 -> 6.5. Violins I: 15.5 -> 14.5, sliding over 1008-1010.
- Inside the notes it also leaves CC7 tails of 1.1-1.2 dB (Clarinet 1 / 2 and Bassoon 2 at 1005, three of the 48).
- By Dan's 11-11 rule this is "a fader row for a single note".

**Print (m).** fff at 1005 on strings and woodwinds, and accents on every stroke at 1008, 1010, 1012 and 1014. The brass decrescendo starts at 1014. Bars 336-339 are one fff passage.

**Master (m).** 1005 / 1006: -16.1 / -15.4 dB, then 1007-1014: -17.4, -17.5, -16.8, -16.4, -16.5, -17.3, -17.2, -17.4.
- The first stroke stands 1.5-2 dB over the rest of the printed fff.
- A 0.3 s weight barely moves the 3 s short-term window that decides the summit's lead. That is consistent with the lead staying at +0.57 LU (+1.2 over the next loudest passage) while the 0.5 qn step measure rose (i).

**Fix (instrument side for the stroke, passage level for the dynamic).**
- Remove `ARRIVAL_WEIGHT_AT` 1005 in both places in score_config.py (lines 288 and 2219).
- Add a passage row in `build/roles.json` on the same 15 tracks: [1005, 1017, +2.5] for strings and woodwinds; brass unchanged, their decrescendo from 1014 stays. Start it at the moved onset of the 1005 stroke less 0.02 s, which is the CC7 trim-lane rule. It is a step at a printed fff mark, held to the G.P.
- The downbeat bite stays where c26 put it: the Sus Marc LITE stroke (v92) and its CC11 counter-shape.

**Expected (i).**
- Bars 336-339 +2 dB on the master.
- Mp3 summit lead +0.57 -> about +1.5 to +2 LU.
- The 0.5 qn downbeat step measure falls by about 0.5 dB.
- Check the delivery limiter on the summit (3.3 dB now, limit 6) and LRA (10.6).

### 4. The 48 net in-note moves left outside hairpins: classes, audibility, where each belongs (m)

I printed each note's net level, envelope and CC7, and its largest change within any 0.5 s window.

| class | notes | size (largest 0.5 s change) | heard? | where it belongs |
|---|---|---|---|---|
| Final fermata fades: Horn 1 1101, Violins I 1111, solo 1120 | 3 | 8-10.5 dB in total, 1.9-2.0 per 0.5 s, all in the last 1.5 s (1125-1128) | yes, as the printed fermata's end | a fade, allowed by the rule. Keep |
| Harp 238 (one chord, counted three times) | 3 | 3.9 dB over 238.3-240.3 | barely: it lies on let-ring notes that are decaying anyway (i) | The envelope carries the role [240, 264, -2] plus the pp at 240 as a ramp over chords plucked at 237-238 (the harp has no CC7 lane). Move the role start into the printed decrescendo, `roles.json` Harp [236, 264, -2], so the move sits inside the hairpin 236-237. Or give the harp notes from 240 velocity -6 and drop the row |
| Summit weight tails: Clarinet 1, Clarinet 2, Bassoon 2 at 1005 | 3 | 1.1-1.2 dB | no | finding 3 |
| HP gains that skip the hold: Flute 1 156 / 384, cor anglais 156 | 3 | 1.1-1.4 dB inside the note, 4.1 dB over the passage | the passage fall, yes | finding 2 (a) |
| Trio climax cap release: celli 632 / 634, Bassoon 2 632 | 3 | 1.1-2.2 dB inside the note; 5.3 dB ramp over 3.5 qn on the celli | yes | finding 1 |
| Slow trim / hold / unison ramps on held tutti notes: Horn 3 ×5, Horn 4 ×4, Trombone 1 / Bass trombone / Tuba 309, celli 312 / 317 / 321 / 329 / 897 ×2 / 912 / 917 / 921 / 929, violas 897 ×2 / 999, Violins II 360 / 999, Bassoon 1 324 / 924, Bassoon 2 897, Oboe 1 996, Contrabassoon 996, Clarinet 2 261 | 33 | 1.0-1.6 dB at 1.5-3 dB/s, inside f / ff tutti chords | no: under the level difference a listener notices inside a thick tutti (i) | No change. Add a rate test to the guard, so that only 1.5 dB or more at over 3 dB/s counts as heard: this class is not note-by-note shaping. |

So 9 of the 48 are heard, and all 9 are covered by findings 1-3 and the harp row. The other 39 are 3 printed fades and 36 moves at or under threshold.

### 5. Inner lines (Dan, 11-17): the printed espress. / dolce lines lead; three entries are still level with the texture (m)

**Overall.** Of the 61 marked entries, every one leads its texture by +2 dB or more in its band except the following:
- the tenor countermelody head at the ff tuttis (Bassoon 1 / Horn 3 / celli espress., bars 105 and 305): -0.4 and -2.6 dB in their first 6 qn, +2.0 / +1.2 in the next;
- Hn 3 dolce, bar 73: -2.4. This is a held chord tone under the harp's espress. tune, so not a hidden line;
- Bassoon 1 / Clarinet 1 dolce, bars 345-348: -0.8 / -0.2;
- Clarinet 1 dolce, bar 81: +0.2;
- Flute 1 1. dolce, bar 172: +0.5;
- Oboe 1 leggiero, bar 31: +0.3;
- Flute 1 leggiero, bar 263: -0.5.

**Against c18.** 14 of the 19 entries under +3.5 dB improved, for example the countermelody's second bar -1.4 -> +2.0 and the reprise second idea at 277 -1.0 -> +2.7. Oboe 1 bar 31 (-2.0), Flute 1 bar 172 (-1.7) and Flute 1 bar 263 (-1.1) lost ground; Hn 3 bar 261 and Clarinet 1 bar 345 are within 0.2 dB.

**Countermelody head (m).** The +2 dB roles of Horn 3 / Horn 4 start at 313 / 913, one beat after the head at 312 / 912. Horn 3's net level climbs -1.0 (309.5) -> +0.3 (311.5) -> +1.9 (312.2) -> +3.5 (318), so the head sits under the line's own level.

**Fix.**
- `roles.json` Horn 3 and Horn 4: [313, 360, 2] -> [311.5, 360, 2] and [913, 960, 2] -> [911.5, 960, 2]. The edge falls in the 0.3 qn rest after the held note that ends at 311.48 / 911.48 (Horn 3's notes: 308.78-311.48, next at 311.78).
- The celli line of bars 212-216 is finding 1.

### 6. Per-bar master, c27 against c26 and c18 (m)

**c27 against c26.** Median 0.0 dB, p10 / p90 -0.18 / +0.45. Changes:
- bar 56 +1.7;
- bar 58 -3.4 (the celli fugato entry's round robin; it is +1.2 over c18, so c26 was the outlier);
- bar 192 +1.6;
- bars 210 / 211 +1.9 / +2.0 (finding 1).

**c27 against c18 (after the -3.0 dB global).** p10 / p90 -0.97 / +1.19.
- Theme A, bars 14-28: -1.5 to -2.8 dB. Violins I's stem is -1.8 dB relative to the master's -3.0 global: the c25 Spiccato velocity -13 and layer cuts, and the c27 soft-head marcato cut. The theme still leads by +12 to +15 dB (inner23), so this is loudness relative to the loud passages, not balance.
- The counterstatement's crescendo, bars 38-43: -1.8 to -3.5.
- The sfp, bars 302 / 303: -3.3 / -3.5 (intended).
- The coda build and summit, bars 325-337: +1.7 to +3.5 (intended).
- Dan's 11-17 note is about exactly these quiet passages. But the delivery's LRA is 10.6 against a 10.5 floor, so a theme A row of about +1.5 dB (`cc7_spans_db` Violins I [36, 84] / [756, 804]) costs about 0.2-0.4 LU of LRA (i). I report it and do not propose it this cycle. Findings 1-3 raise loud passages and the summit, which gives some LRA back. Measure it with them if the actor wants to try it.

**Do not touch:**
- the c27 arrival holds where they work (Bassoon 1 156, contrabassoon 993, Horn 4 912), and the 8 qn cap for the cases findings 1 and 2 do not cover;
- `stretch_cc7` and the CC7 trim lane with its moved-time warp;
- `note_slew` onset_step_s and skip_hairpins;
- the woodwind summit rows from 984 and fff = ff on Clarinet 2 / Bassoon 1;
- the Sus Marc LITE summit stroke;
- every inner-line level listed in finding 5 that leads;
- the Violins I theme lead (+12 to +15 dB);
- the trio tunes (Clarinet 1 +12 to +16, celli +14, Oboe 1 +10 to +14, solo / Flute 1 +13 to +15, Hn 1 motto +12 to +14);
- the delivery chain plus bed, the fugato ride +0.5, and the -3 dB global gain.
