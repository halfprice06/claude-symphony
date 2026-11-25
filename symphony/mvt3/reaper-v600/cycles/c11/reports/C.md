# Critic C, cycle 11 (tempo, timing and transitions), on the c10 render

Data: `cycles/c10/render/` (render-time stems, returns 32-35), `cycles/c10/rendered_build/parts.json` (tempo map and note data), `cycles/c10/mvt3-mockup-c10.mp3`, the c09 master. Scratch scripts were in `/private/tmp/claude-501/mockup-loop/mvt3-c11-C/` (deleted). Times are on the render's score clock (`pcx.TM` on parts.json's tempo map). Levels are 30 ms RMS on a 10 ms hop unless named; "band" levels are FFT band-pass envelopes on the named pitch's harmonics.

## Manual notes

MANUAL-READING gives c11 C no fixed row ("c11 (tempo) picks its own pages"). I read the pages behind this lens's open problems in full: p.100-103 and p.106 (Hollywood Brass long and short articulations, legato), p.109-111 (woodwind long, short and effects rows), p.93-94 (string shorts and Repetitions), p.144 (true-legato velocity). MANUAL-GAPS.md items that are still open come first.

| Manual (PDF page) | What it says | Where it applies here | Followed? |
|---|---|---|---|
| p.101 (MANUAL-GAPS #1) | Sustain Accent: velocity sets the loudness of the attack and CC1 the loudness of the sustained note. | The sfp at bar 149 (qn 592) on all 11 brass tracks. "Sus Accent MAX" is a default row of 1FH, 1TP, 1TB and 1TU (key 25 / tuba 61), but no brass track uses it, so `UNLOAD_UNUSED_ROWS` unloads it. | No. The sf is a CC1 hold on Sus MAX, and the brass peak 0.23-0.28 s late (finding 1). |
| p.103 (MANUAL-GAPS c09 note) | Sforzando Crescendo (Solo Horn, Solo Tuba; the 1TB KS Master also has a "Sfz Cres" row): an accented attack followed by a strong crescendo. Velocity sets the attack and the crescendo. | The brass "sfp <" at qn 592. | No. MANUAL-GAPS c09 set the test condition as "the brass sf more than 1 dB under the ff before". Measured on c10 at +0.10 s: Horn 1 -2.9, Horn 3 -2.9, Trumpet 1 -5.1, Trombone 1 -4.0 dB. The condition is met (finding 1). |
| p.103 | Brass Repetitions are tempo-synced, recorded at 170 / 145 / 120 bpm, and have release trails. | The Più allegro (176 qn bpm) brass repeats. | Not used. Not ranked: this is A's lens. |
| p.94; M1 LEARNINGS c42 | String Repetitions: about a dozen repeats with bow changes; release trails; not round robin; the Basses "Repetitions TS" row is time-stretched to the host tempo. | The basses' hammered eighths (792-840, 984-1108). | Not used. The basses' own stem already separates 5-7 dB (finding 4), so the row would not fix the master. Read only. |
| p.106, p.144 | True legato: velocity sets the transition speed. 50-60 gives a longer transition and 110-127 a tighter one; it does not change loudness. | Flute 2's late joins at 618 / 650 (v100) (finding 3). Bassoon 1's Exp row (finding 2). | Partly. Flute 2 still plays v100 on its two slow joins. |
| p.109 (MANUAL-GAPS #5) | Sus Expressive: a slower attack and a gently increasing vibrato. | Bassoon 1's solo 455.9-496 on "Leg Slur Exp". | Yes. Attack to -6 dB of the body 20 → 35 ms. The joins are faster than Leg Slur MAX's, though, so the old leads now land early (finding 2). |
| p.102, p.110 | Shorts have no release trails; hold the last short note so the room rings. | Wind and brass staccato rows. | Read only, not measured. Out of scope for timing. |

## State through this lens (measured)

- **Wetness (the coordinator's check).** On the master, nine tutti stops fall 20 dB in 0.45, 0.43, 0.33, 0.41, 0.30, 0.40, 0.43, 0.28 s (qn 5, 21, 102, 374, 450, 662, 814, ring end) and 0.44 s for the final chord measured from its written end (qn 1113). Drop at +0.3 s: 13.5-20.7 dB. RT60 on the final chord is 1.35 s (-5..-25 dB) and 1.32 s (-20..-35 dB). c09 and c10 match to 0.01 s, as expected with unchanged returns. Violin soft ends (Vln I plus R Strings) fall -10 dB in 0.27 s (qn 199), 0.14 (418) and 0.27 (477). **Every number is inside Dan's ceiling** (tutti -20 dB ≤ 0.50 s, RT60 ≤ 1.5 s, soft ends ≤ 0.30 s). **The mix is not too dry.** The median of 0.41 s sits at the dry edge of the references (0.43-0.58 s). Only two stops (qn 102 and 450, 0.30-0.33 s) are drier than any reference. Keep the returns. If Dan ever calls it dry, raise the return faders 1.5 dB and leave the sends alone.
- **Tempo map.** It matches every printed step and the eight RAMP_SPANS. The ramps reach 145.3 (rit. into 200 and 792), 132.5 (rit. into 600), 185.9 (accel. into 840), 112 (allargando, flat from 886), 170.4 (stringendo into 984) and 146.4 (allargando into 1088). CAESURA x7 and the lyric PHRASE_ARCS are in place. The caesura at 1107.75 falls in the printed quarter rest before the final crash chord: only the basses' last eighth and the top of the harp glissando cross it.
- **Hammered tutti (S2).** Median pcX against the score per section, on the timpani beats. Coda N 792-816: timpani +16, Trumpet 1 -8, Vln I 0, Vln II +16, Vla +30, Vc +8 ms. Più allegro 984-1056: timpani +13, Trumpet 1 +5, Trombone 1 +6, Horn 1 +38, Vln I +10, Vln II +27, Vla +34, Vc +23 ms. Everything is within ±40 ms. Not ranked.
- **Loop pulsing (item 7).** No sustained note longer than 6 s except Horn 4 at qn 168 (6.5 s). The re-bows split everything else. Nothing to measure at 3.95 s.

## Findings, ranked by what a listener would hear

### 1. The sfp at bar 149 arrives in two steps 0.3 s apart. The strings fall at +0.10 s; the brass hold a plateau and fall at +0.35-0.40 s, and their sf is 3-5 dB under the ff before it. Fix: Sus Accent MAX on the brass at 592 (measured; the row choice is inferred from p.101)

Where: qn 592 (bar 149, 219.62 s). Horns 1-4, Trumpets 1-3, Trombones 1-2, Bass trombone and Tuba; the strings and timpani for comparison.

Evidence. Each stem's level is given relative to the ff peak in the 0.4 s before the mark:

| stem | +0.00 | +0.10 | +0.20 | +0.30 | +0.40 s | peak time |
|---|---|---|---|---|---|---|
| Violins I | -0.9 | -6.4 | -7.1 | -9.7 | -14.8 | -0.01 |
| Violoncellos | -3.4 | -2.2 | -1.0 | -3.4 | -17.0 | +0.21 |
| Horn 1 | -6.3 | -2.9 | -3.3 | -2.5 | -14.3 | +0.27 |
| Trumpet 1 | -9.7 | -5.1 | -3.1 | -3.1 | -5.6 | +0.24 |
| Trombone 1 | -8.4 | -4.0 | -4.7 | -2.2 | -12.2 | +0.28 |
| master | -2.0 | -1.8 | -1.8 | -2.1 | -9.0 | +0.25 |

- The brass note-ons are already led 0.05-0.09 s (parts.json).
- Their CC1 holds 98 until 592.375 (+0.135 s) and reaches 42 at 592.827 (+0.30 s).
- The audio follows about 0.1 s behind the CC (the CC1 layer crossfade, M1 c12), so the brass fall lands at +0.30-0.40 s.
- On a Sus MAX sample the attack itself is a rise, not an accent: at +0.10 s the brass are still 3-5 dB under the ff they interrupt.
- Result: the master holds a 0.3 s plateau at -2 dB and then drops 7 dB. Violins I have already fallen by +0.10 s, so the listener hears the strings' p and then the brass's p a beat later.
- More lead cannot fix this (c10 rejected that with numbers). Moving the CC1 fall earlier would cut the brass's only source of sf weight.

Fix (`build/score_config.py`, new c11 block; tools as named):
- Play the 11 brass notes that start at the 592 sfp mark on "Sus Accent MAX" through `ART_SPANS`, span (591.6, 592.1), art "Sus Accent MAX" for each brass track. This is the manual's model of an sfp (p.101): velocity sets the attack, CC1 the sustained note.
  - Velocity 100 (SFP_VEL stays 110 for the other tracks; this needs a per-family override, e.g. `SFP_VEL_BY = {"brass": 100}`).
  - CC1 reaches the p value (`DYN["sfp"]`) by +0.05 s: set brass `SFP_SPIKE_S` to (0.0, 0.05). This needs a per-family form in `score_to_parts.py` near line 1859, like `SOST_JOIN_LEAD_S`'s `by_name`.
  - No CC11 bump, and no `ACCENT_SWELL` on these notes.
  - The printed crescendo then rises from that p as now.
- Cost: one loaded row on each of the 11 brass tracks, 1-3 GB in all (0.1-0.3 GB per row, inferred), plus a full rebuild of those tracks. REAPER is at 45 GB. If memory forces a choice, do the 8 horn, trombone and tuba tracks first; they carry the weight of the chord.
- Lighter alternative if memory blocks the row: brass `SFP_SPIKE_S` (0.0, 0.12) alone. That moves the brass fall to about +0.2 s, beside the strings, but leaves the sf 4-6 dB under the ff (inferred).
- Optional A/B for the "sfp <" (MANUAL-GAPS c09): "Sfz Cres" on Horn 1, Trombone 1 and Tuba only (rows in 1FH / 1TB / 1TU), against Sus Accent on the others.
- Check after the render:
  - each brass stem's peak within +0.12 s of the mark;
  - the level at +0.30 s at least 8 dB under the peak;
  - the master's -6 dB point by +0.20 s;
  - the brass-accent tilt jump (LEARNINGS c08) at 592 no worse than the c10 accents at ff. Dan's harshness came from the accent sample at v105-110 with an 8 CC11 bump into the fff layer; this uses v100 with no bump.

### 2. Bassoon 1's Leg Slur Exp row: keep it, but five led joins now land 53-128 ms early because the Leg Slur MAX leads are too large for the faster Exp transitions. Fix: trim those leads (measured)

Where: Bassoon 1 solo "solo, espress.", qn 455.9-496 (bars 114-124), on "Leg Slur Exp" since c10.

Evidence (pcx legato joins, c10 stem; synthetic estimator error rSD 2 ms):
- Exp solo, 18 joins: median +10 ms, IQR -42..+20, rSD 33 ms, crossover window median 49 ms.
- Bassoon 1's 139 Leg Slur MAX joins elsewhere: median +14, IQR +5..+41, rSD 26, window 48 ms. The overlap of the two pitches is the same, so the Exp row does not smear the legato.
- The spread comes from the joins with large leads:
  - every join with the 0.06 s lead lands +7..+49 ms (11 joins);
  - the joins led 0.14-0.22 s land early: 466 (lead 0.14 s) -53 ms; 468 -77, 470 -77 and 482 -69 (0.15 s each); 484 (0.22 s) -128 ms.
- These leads were fitted on Leg Slur MAX (466 carries c10's +0.08 s leg_leads row). The Exp transitions speak sooner.
- An early join on an exposed espressivo solo is heard as rushing into the long notes.

Judgement on keep or revert: keep the Exp row. The timing problem is in the leads, not the row. Joins with the base lead are on time, the crossover window is unchanged, and the slower attack (20 → 35 ms to -6 dB of the body, c10) is what p.109 promises. A judges the vibrato (AM share 0.46 → 0.18).

Fix (`build/leg_leads.json`, rows keyed to Bassoon 1):
- 466.0: remove c10's +0.08 (net -0.08 s).
- 468.0 -0.07, 470.0 -0.07, 482.0 -0.06, 484.0 -0.11 s.
- Leave 464 (+59 ms) and 480 (+50 ms). They are slightly late, but they are upward leaps on the slow-attack row.
- Print each row's realised lead after the build (`LEAD_WARN_S`; M1 c48: a fifth of lead rows never act).
- Target: every solo join within ±50 ms, rSD at or under 26 ms.

### 3. Flute 2's legato joins out of D#6 land late: +152 ms at qn 618 and +275 ms at 650. More lead made 650 later, and the cap does not bind. Fix: a faster transition by velocity, or a re-attack (measured; the cause is inferred)

Where: Flute 2 at qn 618 (87 → 82, bar 155) and 650 (87 → 85, bar 163), the F1 heads of the recapitulation K, doubling Flute 1 in unison at 650.

Evidence (pcx and band envelope re the score onset):
- Flute 1, led 0.085 s: -42 / +10 / -45 / -30 / -34 / -42 ms at 602 / 618 / 634 / 650 / 1007 / 1074.
- Flute 2, led 0.16 s: +48 / **+152** / +49 / **+275** / -38 / +49 ms.
- Flute 2's 650 band sits at -14 dB at the beat, -17 at +0.10 s, -7 at +0.20, -12 at +0.30 and -4 at +0.40: a slow transition that wavers.
- The lead is applied in full: parts.json moves 650 to 649.552 = 0.16 s. The 0.45 cap allows 0.9 qn after the 2-qn note at 648, so the cap is not what binds.
- c09 (less lead) read +192 ms; c10 (more lead) reads +275. The two late joins are the only ones that leave D#6 (87); the 84 → 79 joins are +48/49 ms and 93 → 91 is -38. So this is how that patch handles these intervals, not a lead shortfall.
- Against Flute 1 (-30 ms at 650) this is a 305 ms flam on the theme's head.

Fix (`build/score_config.py`):
- Give Flute 2 velocity 122 at sq 618 and 650 (manual p.144: 110-127 tightens the transition). Use `LEG_VEL_EXTRA_S` in its list form, or a per-onset velocity row if the tool has one.
- Take the leads at those two onsets back to 0.12 s with leg_leads rows of -0.04.
- If 650 still measures more than +80 ms, play Flute 2's 618 and 650 as unslurred Sus MAX re-attacks with the 0.06 s entry lead. Flute 1 carries the slur in the unison, and Flute 2's own 602/634 entries land at +48 ms.
- Target: Flute 2 within 60 ms of Flute 1 at all six F1 heads.

### 4. The basses' eighths cannot reach a 4 dB repeat dip in the master where the tuba and contrabassoon hold the same pitch in printed whole notes. Where nothing holds that pitch, the master already gets 5.9 dB. Do not put per-stroke dips on the whole notes (measured; one option simulated)

Where: Double basses 792-816 (34 repeats measured), 984-1056 (114), 1056-1088 (63), 1088-1108 (37).

Evidence. Median dip and gap level per stroke in the band of each eighth's fundamental (±6 %), 10 ms windows:

| span | master dip | basses stem dip | basses gap | tuba gap / dip | Cbn gap / dip | celli gap | R Strings gap |
|---|---|---|---|---|---|---|---|
| 792-816 | 4.1 | 6.4 | -54.0 | -56.3 / 2.6 | -62.7 / 3.1 | -97 | -108 |
| 984-1056 | 3.4 | 7.0 | -61.1 | -64.8 / 1.2 | -61.8 / 1.0 | -97 | -109 |
| 1056-1088 | **5.9** | 5.7 | -54.8 | -87.5 | -115 | -101 | -112 |
| 1088-1108 | 3.2 | 5.1 | -58.0 | **-54.0** / 1.1 | -58.1 / 1.1 | -99 | -112 |

- Gap levels are in dB on the stems' scale.
- What fills the gaps is the tuba and the contrabassoon. Their printed whole notes sit on the basses' pitch (984/988/992/996 and 1088/1092: C, D, F, G and C under the eighths), with no dip of their own.
- The celli and the returns are 35-55 dB under the basses' gap in this band. This corrects c10's attribution (CHANGES: "celli / timpani / returns").
- In 1088-1108 the tuba's sustained C2 is 4 dB louder than the basses' gap.
- In 1056-1088, where neither holds the pitch, the master's dip equals the stem's (5.9 vs 5.7 dB): the 63 ms REP_SPLIT gaps do their job.
- A real orchestra with a tuba holding the same C sounds the same way. Separation there is heard in the basses' bow attacks, not in a gap.
- Per-stroke dips on the tuba and contrabassoon whole notes would make printed sustained notes pulse eight times a bar, the pulsing BRIEF item 7 forbids.

Fix:
1. Keep REP_SPLIT as it is, and do not add dips to doublers.
2. Measure S1 for the basses on the master in 1056-1088 (the only span without a sustained same-pitch doubler; target 4 dB, met). In the other spans, measure it on the stem (target 5 dB, met).
3. One option, a balance choice for B: tuba and contrabassoon -3 dB in 984-1056 only (`roles.json`, rows [984, 1056, -3] on both, with the usual 0.5 qn ramp). Simulated from the band energies above: master dip 3.4 → 4.4 dB. In 1088-1108 the same cut buys only 3.2 → 3.7 dB, and -6 dB on the tuba 4.2 dB, which would thin the final ff bass. Do not cut there.

### 5. The delivery ride lifts the mp3 by 1.5 dB exactly at the subito p of bar 42, and by 2.1 dB more at bar 43, so the mp3's f-to-p is 6.8 dB against the master's 9.2 (measured)

Where: the delivery ride row 164-200 (`build/score_config.py`, the c10 `_FIT10` loop: offset -1.0 before 168, ramp to +1.5 by 172).

Evidence:
- Every string section, the flutes, the bassoons and Trombone 1 print p at qn 164 (bar 42). It is a subito after the ff counterstatement.
- The ride row in parts.json is (163.95, 0.0), (164.0, 1.48), (166, 1.52), (168, 3.58), (170, 3.63): a 1.5 dB step on the mark, then a 2.1 dB step at 168.
- Per-bar plain RMS, master / mp3 (aligned, lag 10 ms): bar 41 -32.0 / -26.1; bar 42 -41.2 / -32.9; bar 43 -43.9 / -33.1.
  - 41 → 42: master 9.2 dB, mp3 6.8.
  - 41 → 43: master 11.9 dB, mp3 7.0.
- The ride acts on the whole master, returns included, so the step on the mark also raises the ringing ff tail. The subito loses its contrast in the one place a listener notices it.

Fix: start the 164 row's rise after the drop.
- Points (163.95, 0), (166.0, 0.0), (168.0, 1.5), (172.0, 3.7), then the fitted values. In code: offset -1.48 for q < 166 and a ramp from 166 to 172, in place of `-(1.0 if q_ < 168.0 else 0.0)`.
- Predicted mp3 41 → 42: about 8.3 dB. Bar 43 then sits about 1 dB over bar 42; the master has 42 → 43 at -2.7, so check that it does not read as a crescendo in a slow ride.
- 277 → 278 is fine: master +2.1, mp3 +1.5 dB, and bar 278 is the mp3's loudest bar.

### 6. The 315 Hz hump in J comes from Horn 3's D4 in the stop chord (584-600), not from 552-564 (measured; balance, outside this lens, answered for the coordinator's open item)

Evidence:
- Over qn 536-600, the master's 282-355 Hz band stands 6.7 dB over the mean of 224-282 and 355-447 Hz.
- Horn 3 carries 38.5 % of that band's energy across the stems. Its own band stands +23.4 dB over its neighbours. Next come the bass clarinet 8.4 %, the violas 7.9 % and Trombone 2 7.8 %.
- 93 % of Horn 3's band energy in J is its D4 (MIDI 62, 294 Hz) on the ff chord and the sfp: qn 584 33 %, 588 19 %, 592 41 %.
- The c10 cut (552-564) touched 0.7 %, which is why the hump moved only 8.5 → 8.4.

Fix:
- `build/note_trims.json` Horn 3 584.0, 588.0 and 592.0 at -3 dB, or a pitch_trims row for pitch 62 over 584-600.
- If finding 1 puts 592 on Sus Accent, refit 592's trim on the next render.
- Target: J hump at 5 dB or less, Horn 3 under 25 % of the band, and the stop chord's horn level against Trombone 1 within 1 dB of c10.

Do not touch: the tempo map, the eight RAMP_SPANS, CAESURA x7 and the lyric PHRASE_ARCS (all match the print); the returns, faders, envelope and register sends (tutti -20 dB 0.28-0.45 s, RT60 1.32-1.35 s, final chord -20 dB 0.44 s from 1113; not too dry); FINAL_RING; REP_SPLIT's 63 ms basses gaps (master dip 5.9 dB where no doubler holds the pitch); the string sf bump and FP_SPIKE_AT_MARK on the strings at 592 (Vln I at -6.4 dB by +0.10 s); the hammered-tutti alignment and percussion on the grid; the Bassoon 1 Exp row itself; the per-dynamic string release caps.
