# Cycle 26, critic B (balance and levels), on the c25 render

I measured on `cycles/c25/render` (stems, returns, the float master), on the delivered `cycles/c25/scherzo-mockup-c25.mp3` and on `cycles/c25/build_render/` (parts.json, roles.json, mix.json; these are identical to `build/`).
- Stems are compared with `cycles/c18/render`; the mp3 is compared with c24 and c18.
- Positions are score quarter notes (qn); bar b starts at qn 3(b-1).
- (m) means measured, (i) means inferred.

How I read the lanes REAPER gets:
- I ran `tools/build_reaper.py` only up to `ENV_LUA` (the guard25 method), then called `vol_points` and `cc7_lane` on every track.
- `vol_points` returns project qn (score + 3, the pre-roll). `cc7_lane` and `TRIM_CC7` return score qn; `item_lua` adds the pre-roll later. Anyone reusing guard25's harness for CC7 must not subtract the pre-roll from the CC7 lane. My first pass did, and every CC7 position came out 3 qn early.

Measures:
- **Stem level.** Mean power over 5 ms frames above -70 dB in a window, in dB on the common scale.
- **inner23.** `cycles/c23/actor_scripts/inner23.py`: a line's best band against every other stem plus the returns.
- **mp3 bar loudness.** ffmpeg ebur128 momentary loudness; a bar's value is its median.

## Manual notes

`loop/MANUAL-READING.md` has no row for c26, so I chose pages myself: B1, PDF pp.137, 140, 150-151 of the May 2021 manual (CC7 against CC11, velocity, row and master gain), because this cycle's questions are about the CC7 lane. I also used `loop/MANUAL-GAPS.md`.

| what the manual says (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| CC7 "is best used to set the overall upper limit on the volume of each track ... as opposed to shaping an individual musical line" with CC11 (p.151) | `dyn_trim_to_cc7` and `cc7_spans_db` (c25) | Mostly. 315 of the 335 notes whose CC7 moves 1 dB or more inside the note sit in printed hairpins (dynamics, which Dan's rule allows). 20 are passage edges drawn inside notes (finding 4). The fixes I propose put only passage-level falls into CC7. |
| CC11 makes "swells in the middle of a note ... crescendos" on sustained instruments (p.151) | printed short hairpins on held notes: Clarinet 2 210 / 894, Bassoon 1 1001, Horn 1 442, Horn 3 1028, Oboe 1 1002 | No. Their dB gain is still in the post-hall envelope (finding 3). |
| Velocity selects the recorded dynamic samples and cannot change mid-note, so it suits shorts (p.150) | Violins I's rerouted Spiccato notes moved into the v1-54 layer (c25); the trumpets' staccato quarters before the summit | Yes |
| Each KS Master row has its own volume knob (p.137) | row level (`row_dyn_db`, region gains) | Yes. The Spiccato layer cuts use it. A trumpet Sus row trim would be the instrument-side alternative to finding 2. |
| The instrument's master Gain changes the output without changing the mic mix (p.140) | headroom (finding 6) | Not needed: the render's float stem sum already avoids clipping. |
| MANUAL-GAPS #9: half-section patch for Violins II "la metà" (bars 349-356) | the solo passage | Not used. The solo still leads by 12.8-15.2 dB (inner23), so nothing to fix for balance. |

## Answers to the cycle 26 questions

**Does any CC7 lane move note by note? (m) No.**
- Outside printed marks there is no alternating per-note pattern.
- The notes whose CC7 differs from both neighbours by 0.5 dB or more are 4-9 per track. All of them sit on a printed mark: the sf of the sfp at 900, the accents at 1068, the f of 300, the pp of 840, the sub. p.
- 335 notes have 1 dB or more of CC7 movement inside them. 315 of these are inside printed hairpins (±0.6 qn). The 20 that are not are listed in finding 4.

**Per-bar mp3 against c24 (m).**
- Median -0.10 dB; p10 -0.40, p90 +0.10.
- Bars that moved 1 dB or more:
  - 19 / 21 / 22 / 27 / 35: -1.3..-2.3 (the Violins I Spiccato cut);
  - 259 / 267: -1.7 / -1.2;
  - 99, 225: -1.2, -1.0;
  - 277-279: +1.1 / +1.6 / +2.0 (the reprise tune row removed);
  - 349: +1.0.
- All of these are intended. Theme A still leads by +8.7..+15.0 dB over every other stem (inner23, bars 13-28).
- Against c18 the mp3 is +0.85 dB (median), and the quiet sections are +1.0..+2.0. Section medians on c25:

  | passage (bars) | bar-median momentary loudness |
  |---|---|
  | retransition (89-100) | -20.6 |
  | intro (1-12) | -20.0 |
  | link (141-152) | -19.8 |
  | 341-348 | -19.2 |
  | fugato (57-72) | -18.8 |
  | end (364-376) | -18.3 |
  | codetta (225-240) | -18.2 |

  The bar p10 is -22.2. With the -14 delivery met, Dan's AirPods note is now about inner lines, and those all lead (below).

**Master clipping (m).**
- The float stem sum peaks at 1.048 at qn 1007.52 (bar 336, the summit), left channel.
- The contributions at that sample:

  | track | value |
  |---|---|
  | Violins I | -0.626 |
  | Violins II | -0.213 |
  | Clarinet 2 | -0.072 |
  | Flute 2 | -0.068 |
  | R Strings | -0.055 |
  | Violas | -0.047 |

- Only 6 samples are over 0.95, and 2 over 1.0.
- The cause is the strings' summit rise. At 1005-1011 the strings are 2.5-4.2 dB louder than c18 (Violins I -24.4 -> -21.2, Violins II -26.0 -> -21.6, violas -25.3 -> -22.8, celli -31.0 -> -26.8). The Violins I stem peak went 0.422 (c18) -> 0.608 (c24) -> 0.647 (-3.8 dBFS).
- The mp3 is made from the float sum, so nothing is audible. Fix in finding 6.

**Trumpet 1 at the summit (m).** The cause is two role rows, not CC1 or velocity (finding 2).

**Inner lines (inner23, 6 qn windows) (m).** Every tune leads:
- theme A: +8.7..+15.0;
- counterstatement: +4.6..+12.3 where the winds have it (bars 29-36). At 108-132 Flute 1 / Oboe 1 double Violins I in unison at -3..-6, which is correct for a doubling;
- second idea: +7.3..+12.8, reprise +2.4..+10.3;
- Clarinet 1 trio: +8.6..+15.7;
- celli trio: +5.1..+14.3;
- Oboe 1 middle part: +10.3 / +14.3;
- trio ff tune: +10.2..+16.2;
- the bar 197 espress. tune (Clarinet 1, Violins II, violas): +3.5..+10.4, over the mf counterline (+2.3..+5.1);
- codetta: Oboe 1 +0.5 / +4.1, Clarinet 1 +9.6 / +10.3, Bassoon 1 +6.0 / +19.1;
- solo violin: +12.8..+15.2;
- Hn 1 motto tail: +13.3 / +13.9; last G sharp: +16.8..+22.8;
- the tutti tenor countermelody (Bassoon 1, Horns 3-4, celli): -1.1..+5.9 at 105-120 and +3.5..+7.0 at 305-320.

The weakest window is the codetta oboe's first bar (+0.5), and even there it is 7 dB over every single other stem. Bar 221 is in finding 5.

## Findings, ranked by what a listener would hear

### 1. Six guard notes are passage-level falls inside joined notes. CC7 can carry every one of them, because a fall needs no CC7 headroom (m)

**The c25 reason does not hold.** CHANGES.md left the positive role ends in the envelope because "the lane has no headroom at those dynamics". The end of a positive role is a fall. CC7 can always go down. Only the envelope edge has to move, into the next rest.

**What the envelope does now:**

| note | envelope (post-hall) | CC7 there |
|---|---|---|
| Violoncellos 876 (pp legato head, moved onset 875.472) | role [864, 876, +5] ends with 12.0 -> 8.95 dB just before the onset, then 8.95 -> 7.0 by 876.3: 2 dB in the note's first 0.19 s. The stem also drops into a 19 dB hole at qn 876.0 (-47 -> -66 -> -49 dB, an articulation item for A). | 0.0 dB (127) |
| Violins I 1012 (accented, 1011.616-1014.0) | role [1008, 1014, +4.5] -> [1014, 1017, +2.5]: 19.5 -> 16.7 dB across the note's second half | -2.0 dB |
| Horn 3 1028 (p dolce, 1027.775) | role [1020, 1032, +3] plus a hairpin gain (finding 3) | -0.1 dB |
| Flute 1 156, cor anglais 156 (f arrival of the crescendo 144-156, moved onset 155.85) | the hairpin gain +4 is held to 156 and released 10.8 -> 6.8 dB (cor anglais 14.5 -> 10.5) over 156-158. That is 4 dB in 0.45 s (8.8 dB/s) across the arrival note and the two joined notes after it: an unprinted fade right after the f. | Flute 1 -5.8..-7.8, cor anglais -5.3 |
| Flute 1 384 (the same in the tutti, 372-384) | the same release, 10.8 -> 6.8 over 384-386 | -8.5 |

Flute 1's `HP_GAIN_TO_CC11` entry sets `keep_rel_db_s` 2.8, but these releases run at 8.8 dB/s. My guess is that these first gains of a chain take a path that skips the rate limit (i). The tuple after `hpgain` [144, 156, 4.0] / [371.67, 384, 4.0] in parts.json would show which path wrote them.

**Fix: finale technique 136, in `tools/build_reaper.py` `vol_points`.**
- After the `cc7_spans_db` block, add an option, e.g. mix.json `dyn_trim_to_cc7.edge_falls: true`.
- For each fall of 1 dB or more in gain + vol_db that lands inside a sounding note:
  - hold the envelope at the higher level until the end of the phrase (the next rest, at most 16 qn ahead);
  - write the fall into the CC7 lane: a step at the moved note-on less 0.02 s for a role end, or the release rate for a hairpin-gain release;
  - in that rest, step the envelope down and let CC7 return.
- Rests found in parts.json:

  | note | rest the envelope steps down in | CC7 part |
  |---|---|---|
  | celli 876 | 888.39-888.89 | -5 dB from 875.45 |
  | Violins I 1012 | 1015.0 (G.P.) | -2 dB from 1014.0; the lane goes -2 -> -4 dB, CC7 101 -> 80 |
  | Horn 3 1028 | 1031.85 | the role's -3 at 1032 |
  | Flute 1 156, cor anglais 156 | 164.6-164.9 | the 4 dB release at 2.8 dB/s from the arrival's moved onset + 0.35 s |
  | Flute 1 384 | 392.63-392.91 | the same |

  Flute 1 and the cor anglais have 5.3-8.5 dB of CC7 below 127 there, so the hold-and-release also fits as a rise if the actor prefers to write the gain itself in CC7.

**Expected (i).**
- No envelope step inside those six notes. That clears 6 of the 15 guard notes (Violoncellos 876, Violins I 1012, Horn 3 1028, Flute 1 156 / 384, cor anglais 156).
- The falls happen before the hall, so the hall of the higher level keeps ringing (S3).
- The f arrivals at 156 / 384 no longer fade over 0.45 s.
- The levels the notes reach are unchanged.

### 2. At the summit, Trumpet 1 (printed f) plays its unison B4 3 dB over Horn 1 (printed ff), because roles.json lifts the trumpets and cuts Horn 1 (m)

**Print and data.** At 1005 Trumpet 1 and Horn 1 both hold B4 (dotted half), trumpet f, horn ff. roles.json has:
- Trumpet 1 [1005, 1016.5, +2] and Trumpet 2 [1005, 1016.5, +2] (c13 B #5);
- Horn 1 [1004.75, 1014, -1.5] (c06 / c22 summit cuts).

The trumpets' envelope steps +1.74 dB at 1004.625-1004.75, before their moved onset (1004.76). Trumpet 1's CC1 (86-88) and CC11 (93 -> 88) do not change across the summit.

**Stem levels, c25:**

| window | Trumpet 1 | Horn 1 | Trumpet 2 | Violins I |
|---|---|---|---|---|
| 1002-1005 | -34.7 | -31.2 | -35.2 | -28.0 |
| 1005-1008 | **-29.1** | **-32.1** | -31.3 | -19.8 |
| 1008-1011 | -31.4 | -29.7 | -32.6 | -23.4 |

Trumpet 1 rises 5.6 dB into a note with no printed change, while Horn 1 falls 0.9. The brass stay 9-10 dB under the strings, so the summit order is safe either way.

**Fix: `build/roles.json`.**
- Delete Trumpet 1 [1005, 1016.5, 2] and Trumpet 2 [1005, 1016.5, 2].
- Delete Horn 1 [1004.75, 1014, -1.5].
- These are slow role rows (allowed), and deleting them removes three envelope edges.

**Expected (i).**
- At 1005-1008: Trumpet 1 about -31.1, Horn 1 about -30.6, so the horn is level with or 0.5 dB over the trumpet, as printed.
- At 1008-1011: Horn 1 about 3-5 dB over the trumpets.
- The summit's loudness changes by under 0.05 LU, because the brass are 9-10 dB under the strings. Check the summit lead (+0.56 LU) after the build anyway.

### 3. The other nine guard notes are printed short hairpins on held notes, and one unison boost. They are legal as ramps, but they belong before the hall and in the right lane (m)

**Printed hairpins** (Dan's rule allows them as envelope ramps; the guard counts them because they run faster than 6 dB/s). For each, whether CC7 has room for the rise:

| note | print | gain in the envelope | CC7 below 127 there |
|---|---|---|---|
| Clarinet 2 210 / 894 (held 209.85-212.6) | cresc 211-213 into ff | +4 dB (3.2 dB in 0.4 s). The stem rises 6 dB smoothly (-36.8 -> -27.8), as a real crescendo would. | 6.0-8.3 dB: room |
| Bassoon 1 1001 | cresc 1002-1005 | +4 | 4.0 dB: room |
| Horn 1 442 | cresc 440-441, decresc 441-444 | +2.5, then -2.9 | 0.4-0.9 dB: the fall fits, the rise does not |
| Horn 3 1028 | cresc 1028-1029, decresc 1029-1032 | +2.5 | 0.1 dB |
| Oboe 1 1002 | cresc into fff, plus the summit's arrival weight (+3 at 1004.69-1004.75, inside the legato overlap of the 1002 note) | | 0 |
| Violin I solo 1064, Violins II 1057 / 1064 | -2.5 hairpin gains | -2.5 | falls |

**Fix (generic, `tools/build_reaper.py` `vol_points`).** With `dyn_trim_to_cc7` on, write a printed hairpin's dB gain (`hpgain`) into the CC7 lane wherever the lane is at or below 127 x 10^(-gain/20) over the hairpin. Falls always fit. Otherwise leave it in the envelope.
- This moves Clarinet 2 210 / 894, Bassoon 1 1001, the decrescendo halves of Horn 1 442 / Horn 3 1028, and the solo-passage -2.5 gains before the hall.
- Oboe 1 1002 and the rising halves of the horn hairpins stay in the envelope as printed ramps.
- In `cycles/c25/actor_scripts/guard25.py`, exempt a printed hairpin's ramp whose rate is at or under its gain divided by its printed length. That way the guard lists only moves that are not printed.

**Horn 3 950 (not explained in c25).**
- The envelope rises 6.8 -> 9.8 dB at 949.5-950.0, then falls 9.8 -> 6.8 over 951.1-953.09, inside the held E4 (949.736-952.94).
- This is `UNI_BOOST_AS_ROLE` (the slow:uni_role layer): +3 dB while Horn 4's unison is dropped. Its end is fixed 0.5 qn after the run.
- c24 B #2 proposed snapping these edges; that was not done.
- Fix: in `tools/score_to_parts.py`, in the `UNI_BOOST_AS_ROLE` block, end the role in the first rest after the run (here 958.0-989.6) and start it at the run's first moved note-on.
- Separately, the stem rises 8.5 dB across the held note (-37.1 -> -28.5) with nothing printed. That looks like the sustain sample's own swell; I pass it to A.

### 4. Twenty notes carry CC7 moves outside printed hairpins. The largest are c25's own Oboe 1 spans, drawn as 0.5 qn ramps inside notes (m)

- **Oboe 1 `cc7_spans_db` [386.3, 393, -4.5, 0.5, 0.5] and [854.3, 861, -4.5, 0.5, 0.5].**
  - The ramp in falls 4.6 dB (-4.1 -> -8.3) over 386.35-386.8, inside the last 0.1 s of the f note 386 (385.78-386.98).
  - The ramp out rises 3.7 dB over 393.0-393.5, across the whole staccato 393 (392.912, 0.5 qn).
  - The same happens at 854 / 861.
  - Fix in `build/mix.json` Oboe 1: [386.76, 392.89, -4.5, 0, 0] and [854.76, 860.89, -4.5, 0, 0]. These are steps at the moved note-ons of 387 and 393, before the hall.
- **Flute 1 140 / 142.** After the printed decrescendo 136-141, the soft-decrescendo hold releases +2.8 dB (-7.3 -> -4.5) across the tied 140 note, with nothing printed.
  - Fix: end that hold (`SOFT_DECRESC_KEEP` holds in `vol_points`) in the rest after the tie, or skip holds whose release falls inside a tie.
- **The rest are 1.0-2.0 dB:** Flute 1 780 / 836 / 838, Contrabassoon 993, Horn 1 612, violas 626 / 681 / 839 / 1020 / 1065, celli 179 / 413 / 626 / 875.
  - Most are span or role edges within 0.3 qn of a moved onset.
  - violas 681: the codetta span ends at 683.27 inside the note.
  - violas 839: the span ends at 839.1, 16 ms before the 840 head. Harmless.
  - Moving each edge to the nearest moved note-on removes them.

None of these is a note-by-note shape. They are passage edges a few tenths of a qn out of place.

### 5. Violas' div. thirds, bar 221: the -2.6 dB is the lower voice against the bass line's octave. The upper voice is heard (m), so stop lifting it

**inner23 on c25:**

| line | window | over all others | band |
|---|---|---|---|
| Violas + Violas div | 660-666 (6 qn) | -2.6 dB | 226 Hz |
| Violas div (upper voice) | bar 221 | +1.0 dB | 320 Hz |
| Violas div (upper voice) | bar 222 | -0.9 dB | 320 Hz |
| Violas + Violas div | bar 221 (3 qn) | +1.1 dB | |
| Violas + Violas div | bar 222 (3 qn) | -0.9 dB | |
| Violas + Violas div | bar 223 (3 qn) | -2.7 dB | |

**Why the pair reads -2.6.** The pair measure picks the full section's lower voice: B3 at 661-662, A3 at 664-665. The full section is 6-10 dB stronger than the half-section DIV B, so the 320 Hz band falls outside "within 10 dB of the line's strongest band". In that band the lower voice sits an octave over the bass line B2-C3-A2-B2, played by the celli (vel 112), Bassoon 2 and Horn 4. Horn 4 also carries the c22 role [648, 669, +3].

**Also:** c25's lifts (violas +2, Violas div +2.5, 636.5-672) were cut at CC7 127 on 5 + 6 points (build warnings), so part of them was never written.

**Fix.**
- Accept the line as it is. The upper voice of the thirds is level with or over every other stem in its band, and the lower voice under the bass's octave is a normal inner voice.
- Measure this passage with the upper voice alone from now on.
- If the actor still wants the lower third clearer, the cause to reduce is the doubling, not the violas: shorten Horn 4 [648, 669, +3] to [648, 660, +3] in roles.json. Over 660-669 Horn 4 plays the bass line an octave under the violas' lower voice. Test on the stems first: expect about +1 dB on the pair at 226 Hz (i).
- Remove the violas' / Violas div lifts above CC7 127 from `cc7_spans_db`, or lower the lane under them first, so the data matches what plays.

### 6. Headroom: the summit strings push the master over full scale and leave Violins I's 24-bit stem 3.8 dB from clipping (m)

- c25's 00_Master.wav from REAPER clipped and was replaced by the float stem sum (`render.log`: "master clipped: replaced by the float stem sum, peak 1.0485"). The stems are PCM_24.
- Violins I's stem peak is -3.8 dBFS at the summit, 3.7 dB higher than in c18.
- The summit has been climbing every cycle (arrival weight 2.5 -> 3.0, roles +2.5 / +4.5, CC11 119-125). If it climbs another 4 dB, the Violins I stem clips inside REAPER, and the float sum cannot repair that.
- Fix: in `tools/build_reaper.py` (the track gains from mix.json), lower every track gain by the same 3 dB through a top-level mix.json key, e.g. `"global_gain_db": -3`. `deliver_master.py` normalises to -14 LUFS, so the delivered mp3 does not change. Alternatively, render the stems as 32-bit float in `render.lua` / `render_cycle.py`.
- Also make `render_cycle.py` warn when any stem passes -1 dBFS.

## Do not touch

- the CC7 trim lane and its moved-time warp;
- the inner-line levels listed above (every tune leads; Flute 1 col Vl. solo at -45.9 with the solo at -40.1);
- the Violins I Spiccato layer cuts and velocity -13;
- the bar 23 state (none of these fixes touch Violins I before qn 1008);
- the summit order (bar 336 leads by +0.56 LU) and the delivery chain with its room bed;
- `RIDE_TRIMS` fugato +1.5;
- the trombone / tuba soft head at 993 in CC7.
