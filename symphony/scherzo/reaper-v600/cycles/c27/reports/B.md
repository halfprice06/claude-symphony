# Cycle 27, critic B (balance and levels), on the c26 render

I measured on `cycles/c26/render` (stems and master), the c25 master, and `cycles/c26/build_render/` (identical to `build/`: parts.json, mix.json, roles.json and score_config.py compare equal).
- The lanes REAPER got were rebuilt the way `actor_scripts/net26.py` does it: `tools/build_reaper.py` cut before `ENV_LUA`, then `vol_points` and `cc7_lane` per track. I also wrapped `stretch_cc7` to record its input envelope and offsets, and the CC7 trim lane before it.
- vol_points returns project qn (score + 3); cc7_lane and the stretch offsets are in score qn.
- "Net" means envelope dB + 20 log10(CC7/127). Since c26 the two lanes trade level at the same instants, so only the net level is heard.
- (m) = measured, (i) = inferred.

## Manual notes

`loop/MANUAL-READING.md` has no row for c27, so I chose pages for this cycle's question (CC7 against CC11 for in-note moves). From the May 2021 manual I read pp.53-54 (shaping dynamics), p.64 (3.2.5 realistic performances) and pp.150-151 (velocity sensitivity and MIDI control). I also used `loop/MANUAL-GAPS.md`.

| what the manual says (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| Velocity "cannot be changed mid-note", so it suits shorts. CCs change loudness "in the middle of a note or phrase" (p.53) | every in-note level move below | Yes, mechanically: in-note moves are CCs, not velocity. But 54 of the 61 real in-note moves are unprinted shapes (finding 1). |
| CC7 sets "a loudness level relative to other instruments". CC11 shapes "the continually changing dynamics" (p.64) | roles, cc7_spans and dynamic trims (relative levels) against the post-arrival releases and slewed role ramps (shapes) | Partly. Roles and trims are relative levels in CC7, which is right. The 38 post-arrival releases and 9 slewed role ramps are shapes inside notes written in CC7. By the manual they are either CC11's job or should not be there at all. |
| CC7 "is best used to set the overall upper limit ... as opposed to shaping an individual musical line" (p.151) | `stretch_cc7` (c26) | Mixed. The lane carries passage levels correctly (91 of the 152 counted moves are join steps). The rest are ramps that existed in the c25 envelope and have only been relabelled. |
| Velocity layers are mapped to velocity ranges. "Volume can be adjusted mid-note", which gives a held crescendo (pp.150-151) | printed hairpins on held notes | Yes. The hairpin moves are printed and stay. |
| MANUAL-GAPS #4: clarinet and brass dynamics on CC1 (in use) | Clarinet 2's crescendo into the summit (finding 2) | CC1 rises with the crescendo (84 -> 89 over 993, still rising after). The level falls anyway, because of the trim table (finding 2). |

## Answer to the coordinator's question: the 152 CC7 moves (m)

**The counter overstates the problem.** `net26.py --cc7moves` reads CC7 alone up to each note's written end. The heard quantity is the net level, and it should be read only up to the next moved note-on, which includes legato overlaps.

I recounted the same 152 notes on the net level, from 60 ms after the moved note-on to 25 ms before the next moved note-on (the dynamic-trim lead is 0.02 s):
- **91 have less than 1 dB of net movement inside the note body.** They fall into two groups:
  - At stretch ends, CC7 and the envelope swap level at the same qn, for example Clarinet 2 at 89.56: envelope -6.0 dB, CC7 +6.0 dB, net 0.
  - Dynamic-trim or span steps placed 17-27 ms before the next moved note-on, for example violas 681 / 1020 / 1065 and celli 413. These are a level change at a note-on.
  - Neither group is heard inside a note.
- **61 are real moves of 1.0-3.3 dB inside a note body.** All 61 were already in the c25 envelope. c26's net level matches c25 (p99 0.1-0.3 dB), so c26 created none and fixed none.
- Size: median 1.2 dB, median largest change within 0.5 s 1.1 dB. Only 8 move 2 dB or more within 0.5 s (one of them printed).
- None is a note-by-note pattern. Each is one shape per phrase.

| class | notes | what it is | heard inside the note? | where it belongs |
|---|---|---|---|---|
| A. join or stretch-end steps | 91 | net 0 in the body | no | stays. Fix the counter (finding 5). |
| B. crescendo gain or trim-hold released after the arrival | 38 | `hpgain` (keep_rel_db_s 2.8) and `cresc_trim_hold` (release_s 1.0) give back 1-5 dB over 1-3 s after an f/ff arrival, inside the arrival note and the notes joined to it | mostly at threshold (1.0-1.4 dB per 0.5 s). Audible on Bassoon 1 156 (2.1), Bassoon 2 626 (2.2), Contrabassoon 993 (3.2), celli 626 (3.0) | held as a passage level until the next printed mark (finding 1) |
| C. role row starting at the ff arrival of bar 333 | 4 | Clarinet 2, Bassoon 1 / 2, Contrabassoon at 996 | yes, as a fall at a printed ff (finding 2) | the start of the crescendo |
| D. role edges ramped backward into joined notes by `note_slew` | 9 | Flute 2, Trombone 1, Bass trombone, Tuba 309; celli 312 / 912; Violins I 1012; Violins II 360; Clarinet 1 1042 | Violins I 1012 audible (2.1); the rest at threshold (1.0-1.6) | a step at the next moved note-on (finding 3) |
| E. `UNI_BOOST_AS_ROLE` +3 dB edges inside held notes | 4 | Horn 3 350 / 353 / 933 / 950 | 950 audible (2.3) | the run's first moved note-on and the first rest after it (finding 4) |
| F. `note_slew` pre-ramps of short printed hairpins, and a decrescendo gain restored inside a later note | 4 | Bassoon 2 327 / 927, Clarinet 1 1034, Clarinet 2 261 | at threshold (1.1-1.6) | inside the printed hairpin (finding 4) |
| G. trim-lane fall with nothing printed | 1 | Violas div 1044: CC7 -1.25 -> -3.5 dB over 1042.82-1045.6, on the "dolce, solo" entry | at threshold (1.6) | a level at the moved note-on (finding 4) |
| H. printed decrescendo | 1 | Violins II 420 (harmonic, decresc 438-444, 5.6 dB) | printed | keep |

## Findings, ranked by what a listener would hear

### 1. After nearly every printed crescendo the arrival note fades 1-5 dB over 1-3 s. This is 38 of the 61 real in-note moves (m)

**Mechanisms (m).**
- `score_to_parts.py`, `_keep()` in the HP_GAIN_TO_CC11 block: when no rest starts within 1 qn, the hairpin's dB gain is released at keep_rel_db_s 2.8 (`_hp18`, `_hp18_cc`).
- `build_reaper.py` `vol_points`, `cresc_trim_hold`: the trim held at 70 % (keep 0.3) is released over release_s 1.0 s from the arrival's onset.
- Both act inside the f/ff note the crescendo arrives on, and inside the notes joined to it.

**Examples (net level from the lanes).**

| track, arrival | print | what happens after the arrival |
|---|---|---|
| Bassoon 1, 156 (f, cresc 144-156) | f held | vol_db 7.0 -> 1.1 dB over 160-164.5. CC7 carries 2.4 dB of it inside the held note (159.6-162.0); note_move_guard pushes the rest into the 164.56 rest. Stem: -33.4 dB at 158 -> -34.9 at 159.5-160.5 -> -36.5 at 161 |
| Contrabassoon, 993 (f, cresc 987-993) | ff at 996, then cresc 1002-1005 | net 7.3 (993.5) -> 5.7 (996.3) -> 4.1 (998) -> 3.6 (1000.5-1001.7): -3.7 dB through printed f < ff. Stem bars 333 / 334 / 335: -35.4 / -36.3 / -39.1 |
| Violoncellos, 626 (bar 209, cresc 618-624) | f arrival | CC7 -1.6 -> -5.3 over 622.75-626.9, plus vol_db 0.5 -> -1.5: 3.0 dB inside 0.5 s of note 626 |
| Bassoon 2, 626; Bassoon 1, 624 | same arrival | -2.2 and -2.1 dB |
| low strings and bassoons at 384 / 852 (the tutti statements), the celli at 594, violas at 159 / 387 / 626 / 855, Horn 2 387 / 591, Horn 4 915 / 918 | f arrivals | -1.0 to -1.5 dB, at about 2.4 dB/s |

**Why it matters (i).** The print keeps the arrival dynamic until the next mark. The render plays "crescendo, arrive, sag". Each sag is small. Together they make the f arrivals of every bass and inner line deflate right after they land, and they are part of why the coda's woodwind bass falls under its printed ff (finding 2).

**Fix (generic, off by default).**
- `tools/score_to_parts.py` `_keep()`: add a HP_GAIN_TO_CC11 key `hold_until_mark_qn` (scherzo value 16 in `_hp18` and `_hp18_cc`). With it, the gain left in the envelope holds from the arrival until the first of:
  - (a) a printed decrescendo start or a softer printed mark: release there, as now;
  - (b) a louder printed mark: the held gain shrinks by the table's rise, so the level never falls at a louder mark (net level = max(held level, new table level));
  - (c) 16 qn: the current slow release, ending in a rest if one comes.
- `tools/build_reaper.py` `vol_points`, cresc_trim_hold: the same option, mix.json `"cresc_trim_hold": {..., "release_at": "mark", "max_hold_qn": 16}`. The held amount stays until the next printed mark or decrescendo start, then releases over release_s from that mark's moved onset.
- `stretch_cc7` needs no change: the held level then simply has no moves inside the stretch.

**Expected (i).**
- The 38 notes lose their in-note fades, and the arrival levels last through the phrase.
- The affected bass and inner lines play about 1-4 dB louder for 1-3 s after each arrival.
- Check the delivery after the build: f -> ff step (2.23 LU), summit lead (+0.68 LU), LRA (10.5). Most of these arrivals sit 6 dB or more under the tune.

### 2. Coda build, bars 331-335 (qn 990-1005): Clarinet 2 and the bassoons fall at the ff of bar 333 and through the printed crescendo into the summit (m)

**Net level (envelope + CC7) and CC11:**

| qn | 993.5 (f) | 996.3 (ff) | 1000.5 | 1003.5 (inside cresc 1002-1005) | 1005.5 (fff) |
|---|---|---|---|---|---|
| Clarinet 2 | 4.3 | 3.8 | 0.9 | 0.7 | 4.4 |
| Bassoon 1 | 4.1 | 2.7 | 1.0 | 0.5 | 3.7 |
| Bassoon 2 | 2.3 | 2.7 | -0.1 | 2.3 | 5.3 |
| Contrabassoon | 7.3 | 5.7 | 3.6 | 7.7 | 10.6 |
| CC11 (all four) | 87-91 | 103-104 | 104 | 106 | 107 |

**Stems, bars 333 / 334 / 335.**
- Bassoon 1: -38.8 / -41.2 / -39.8.
- Bassoon 2: -36.1 / -38.2 / -37.7.
- Contrabassoon: -35.4 / -36.3 / -39.1.
- Clarinet 2: flat (-34.1 / -34.7 / -34.5).
- Meanwhile the master rises (-22.1 / -21.8 / -20.5). The woodwind bass does not take part in the build. Its fff level comes only from the arrival weight at 1005.

**Three causes.**
1. Finding 1's releases after the 993 / 996 arrivals.
2. The role rows [996, 1017, x] start on the printed ff arrival: Clarinet 2 -2.5, Bassoon 1 -2.35, Bassoon 2 -0.75, Contrabassoon -1.5, cor anglais -1.5, Clarinet 1 -1.0. On Clarinet 2 the -2.5 lands at 995.75-995.83, the moved onset of the ff note: net 6.6 at 995.5 -> 4.1 at 995.9.
3. The mix.json trim tables put fff under ff: Clarinet 2 ff +1.2 / fff -1.18 (-2.4 dB), Bassoon 1 ff +4.0 / fff +0.72 (-3.3 dB). cresc_trim_hold skips [1002, 1005], and woodwind CC11 is nearly flat above 104, so CC11 104 -> 107 adds little. The trim's fall wins inside the printed crescendo.

**Fix.**
- `build/mix.json` tracks: Clarinet 2 `dyn_trim_db.fff` -1.18 -> +1.2; Bassoon 1 `dyn_trim_db.fff` 0.72 -> 4.0 (fff = ff). The summit balance stays with the existing role rows.
- `build/roles.json`: start the six woodwind summit rows at their crescendo instead of at 996, in the last rest before it (Clarinet 2, Bassoon 1 / 2, cor anglais, Clarinet 1 at 984; Contrabassoon at 987). Keep their end (1017) and dB. They stay slow role rows, now with no edge on a printed arrival.
- Finding 1's hold removes the remaining sag.

**Expected (i).**
- No fall at the ff of bar 333.
- Clarinet 2 and Bassoon 1 rise about 2.4-3.3 dB across 1002-1005 instead of falling 0.5-2.5.
- The woodwind bass grows with the tutti through bars 333-335.
- These four tracks are 4-8 dB under the strings there, so the summit lead (+0.68 LU) should move by under 0.1 LU. Check it.

### 3. `note_slew` turns role edges at joins into ramps across the note before them: 9 notes, Violins I 1012 audible (m)

**The rule.** When a role edge falls where two of a track's notes join (gap under 5 ms), `note_slew` (4 dB/s, max_ramp_qn 2) ramps the step backward across the earlier note. stretch_cc7 then copies that ramp into CC7.

**Notes.**
- **Violins I 1012** (accented, 1011.616-1014.0): role [1008, 1014, +4.5] -> [1014, 1017, +2.5]. CC7 goes -3.1 -> -5.1 dB across the note (2.1 dB in 0.5 s) after the summit. Critic B c26 #1 named this note. It is still a fade, now before the hall instead of after it.
- **Trombone 1, Bass trombone, Tuba 309** (bar 104, the held f note into the ff at 105): role [312, 360, +2] rises 1.2-1.4 dB over the note's last 0.4 s.
- **Flute 2 309**: role [312, 360, -1.8] falls 1.6 dB.
- **Celli 312 / 912**: role starts at 310.6 / 910.6, 1.3 dB.
- **Violins II 360**: role [336, 359.2, -3] ends inside the sub. p head, 1.0 dB.
- **Clarinet 1 1042**: role [1032, 1041, -2] ends inside the held note, 1.0 dB.

**Fix (generic).**
- `tools/build_reaper.py` `note_slew`: add a key `onset_step_s` (mix.json `note_slew.onset_step_s` 0.03).
- A move whose unslewed step lies within that many seconds of a moved note-on, where the track's previous note ends within 0.03 s of that note-on (a re-attack join, not a legato overlap), stays a step 0.02 s before the note-on. stretch_cc7 then places it in CC7 at the new attack.
- Legato overlaps keep the ramp.
- The level change becomes the new note's dynamic. Dan's rule allows that, because it is a passage level at a note-on.

**Expected (i).** No in-note ramp on these 9 notes. Violins I 1012 holds its level and the 1014 stroke takes the -2 dB.

### 4. Three small generic leftovers (m)

1. **Horn 3 350 / 353 / 933 / 950: `UNI_BOOST_AS_ROLE`'s +3 dB span.**
   - It starts and ends inside held notes. 950 falls 2.3 dB over its last 0.4 s (vol_db 2.9 -> 5.0 -> ...).
   - Critic B c26 #3 gave the fix and it was not done: in `tools/score_to_parts.py`'s `UNI_BOOST_AS_ROLE` block, start the span at the run's first moved note-on and end it in the first rest after the run (958.0-989.6 for 950).
2. **Short printed hairpins pre-ramped by `note_slew`.**
   - Bassoon 2 327 / 927 rises 1.2 dB from 0.38 s before the printed cresc 329-330. Clarinet 1 1034 rises 1.6 dB before cresc 1035-1036.
   - The code already has the finale's option: set mix.json `note_slew.skip_hairpins: true`. Printed hairpin spans are then free of the rate limit, and the ramp stays inside the hairpin.
   - Clarinet 2 261 is the same pattern after a decrescendo: the gain of decresc 254.8-258 is restored by +1.3 dB inside the next phrase. Finding 1's hold covers it.
3. **Violas div 1044.**
   - CC7 falls -1.25 -> -3.5 dB over 1042.82-1045.6 on the "dolce, solo" entry. Nothing is printed and vol_db is flat at 9.0.
   - The fall is in the trim lane. I did not find the source, but `dyn_warp` interpolating between moved anchors is the likely one (i).
   - Fix: find which trim-lane input ramps there (print `tv_` around 1042-1046 in `vol_points`). If it is the warp, add a `dyn_warp` option that holds each anchor's value to the next anchor, so the trim lane changes only at moved note-ons.

### 5. The CC7-move counter: count the net level inside the note body (m)

As it stands, `net26.py --cc7moves` adds 91 join swaps to the 61 real moves, and it would hide a real move written as CC7 + envelope.

Fix in the actor's guard script for c27:
- For each note, take the net level (envelope + CC7 dB) from 60 ms after the moved note-on to 25 ms before the next moved note-on of the same track (or the written end, whichever comes first).
- Count notes with 1 dB or more, split into inside / outside printed hairpins (±0.6 qn), as now.
- With findings 1-4 done, the expected count outside hairpins is about 0-5, not 152.

## Other checks (m)

**Inner lines (inner23 on c26, line over all other stems plus returns in its best band, 6 qn windows).**
- Every tune leads by the margins c26 B listed, within 0.3 dB: Clarinet 1 trio, celli trio, Oboe 1 +10.4 / +14.2, solo violin, Hn 1 motto tail +13.2 / +13.9.
- The bar 197 espress. tune (Clarinet 1, Violins II, violas): +2.7..+7.6.
- The tutti tenor countermelody (Bassoon 1, Horns 3-4, celli): -0.9 / +0.7 at bars 105-107, +1.9..+5.9 after; +3.5..+6.9 at 305-320. That is level with or over the whole rest of the tutti in its band.
- Violins II's con sord. arpeggios (169-184): -0.2..-4.9 under all others, but over every single other stem except the celli tune at 169 (-1.9) and Violins I at 181 (-1.1). This is accompaniment under the tune.
- The violas' div. thirds of 209-224 measure -1.5..-5.7 dB (upper voice alone) since the c26 lift removal. They are printed mf under the ff tune, so this is the printed balance, not a hidden line. No change proposed.

**Per-bar master c26 against c25.**
- Median -3.01 dB (the global -3); p10 / p90 -0.28 / +0.21 after removing it.
- Bars that moved 1 dB or more: 58 +3.5 (celli fugato entry, round robin), 73 -1.4 (the bar 72 hold no longer runs under the decrescendo), 172 +1.1, 302 / 303 -3.7 / -3.4 (the sfp's held p). All are intended or round robin.

**Do not touch:**
- `stretch_cc7` and the CC7 trim lane, with its moved-time warp;
- the summit stroke on Sus Marc LITE and its CC11 counter-shape, and the deleted trumpet / Horn 1 summit rows;
- the woodwind figure state (slur ends, release caps, f trails, Oboe 1 v118) and the bar 23 state;
- the Spiccato three-row split;
- the delivery chain with the room bed, and the fugato ride +0.5;
- every inner-line level listed above;
- the -3 dB global gain.
