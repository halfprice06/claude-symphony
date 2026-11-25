# Cycle 26, critic A: articulation and phrasing (on the c25 render)

Sources:
- The c25 stems and master (`cycles/c25/render/`) and the c24 stems for a repeat check (`cycles/c24/render/`).
- The data that made them: `cycles/c25/parts_rendered.json`, `build/score_config.py`, `build/mix.json`, `build/mockup-events.tsv`.
- The score (`v600/score.pdf` p.3, 11, 13, 14, 16).
- `ks_maps.json`.
- The May 2021 HO manual, `loop/MANUAL-GAPS.md`.
- `cycles/c25/logs/render/meas25.log`, and `cycles/c19/actor_scripts/stepcheck.py`, which I ran read-only on the c25 parts.

"Measured" means a number from these files. "Inferred" means a conclusion that a render still has to confirm. Every fix below is on the instrument side: rows, round-robin resets, note lengths, leads, velocity, or CC11 / CC1 shapes. None is a per-note move in the track volume envelope.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 26 (the third round ends at c20). I read the pages behind my findings in full instead, and `loop/MANUAL-GAPS.md`.

| Manual (May 2021 HO, PDF page) | What it says | Where it applies here | Does the render follow it |
|---|---|---|---|
| p.91 (Strings, Long) | Détaché notes come to a defined end. The Sustain and Détaché rows have finger positions, and Sustain alternates up- and down-bow samples by round robin. | Celli bass line on "Detache", bars 11-26 and 151-166 (finding 2) | Partly. In the render the Détaché row alternates two takes. On a same-pitch repeat, one take gives no new attack. |
| p.34, p.145 (Round Robin Reset) | A reset sends the cycle back to its first take. Without one, Opus continues the cycle where it stopped. Reset at important points to force a particular order. | `RR_RESET_AT`. The celli already get CC16 resets at 39.868, 103.801, 599.892 and 679.762 | Partly. The resets make the takes repeatable, but they are not placed to choose the take that a repeat gets (finding 2). |
| p.112 (Woodwinds, Slur Runs) | Slur legato for very fast runs. The characteristic sound works only on minor and major seconds. Each note can be held. Dynamics come from the Mod Wheel, not velocity. | Flute 1, Clarinet 1 and Oboe 1 motive-x runs, bars 43-48. Every interval there is a second (finding 1) | Not used. The runs play on "Leg Slur MAX" / "Leg Slur". The row is in the FL / OB / CL KS Masters (keys 37 / 37 / 36) but not in BS. |
| p.144 (Monophonic True Legato) | Velocity sets the transition timing (50-60 slow, 110-127 tight) and does not affect loudness. | Wind legato targets (finding 1) | Followed (targets at v100). MANUAL-GAPS c22 measured that a velocity floor of 96-116 does not change the wind transition holes. |
| MANUAL-GAPS c23 / c25 entries | c23 adopted wind targets "on the sustain row 0.06 s early with no overlap" for early holes: 8 of 8 went under 6 dB. TLeg hold / decay is "still the untested candidate". c25: the celli Détaché row has no velocity layers (groups cover v1-127). | Findings 1 and 2 | The c23 fix covered only the 8 listed held targets. The motive-x runs and the bassoon solo were not in the list. Because the Détaché row has no velocity layers, velocity cannot fix finding 2. |

## Findings, ranked by what a listener would gain

### 1. Notes vanish in the exposed soft wind solos: the motive-x runs (bars 43-48) and the bassoon solo (bars 115-129) (measured; fix to be range-tested)

**Where.**
- Flute 1 at qn 169-174, Clarinet 1 at 177-182 and Oboe 1 at 185-188. Each is a slurred eighth-note run at p over the strings' held pp chord. Each starts on a v53 head, the targets are v100 on "Leg Slur MAX" / "Leg Slur", and the overlap is 0.098 qn.
- Bassoon 1 at 456-470 and 496-516 ("solo, espress.", then "1. dolce").

**Evidence.**
- **Each note's own-pitch peak** (harmonics 1-4, 20 ms frames), against its neighbours:
  - Clarinet 1: 177.0 -44, **177.5 -55**, 178.0 -46, 178.5 -44 dB.
  - Flute 1: 169.0 -46, 169.5 -52, **170.0 -55**, 170.5 -48.
  - Oboe 1: 185.0 -50, **185.5 -54**, 186.0 -46, **187.5 -53**, 188.0 -45.
  - Bassoon 1: 498 -48, **499 -54**, 500 -49 and 506 -49, **507 -56**, 508 -48. Also 459 / 460 -53 after the -44 head at 456.
  - In every run, the first one or two transitions after the soft head are the weak notes.
- **Holes at the joins** (200-6000 Hz, 20 ms; minimum around the join against the lower neighbouring body):
  - Clarinet 1 at 178: **19.8 dB**.
  - Bassoon 1 at 508: 11.5, at 462: 9.2, at 500: 6.3, at 512: 6.2.
  - Flute 1 at 170: 8.8. Oboe 1 at 188: 8.8.
- **In the master** (solo stem against the master minus that stem, 40 ms frames):
  - Clarinet 1 sits level with the accompaniment (-45 against -46..-47 dB). It then falls to -58 / -59 / -64 for about 0.15 s across 177.5-178, **13-18 dB under the accompaniment**.
  - Bassoon 1 falls from -53 to -60 / -64 at 507-508 against -43..-44.
- **The holes repeat exactly.** The c24 render gives every one of these numbers to the dB, so the holes are deterministic sample behaviour, not render variance.
- **Cause: two parts** (part a inferred, part b measured).
  - (a) The weak notes are the transitions straight after a v53 head. MANUAL-GAPS c22 says the holes are in the sample crossfade, and a velocity floor on the targets did not help. Nobody has tried the head's own velocity.
  - (b) In the bassoon solo, the quarter notes 499 and 507 come before half notes at v80 that lead by **0.42 qn** (the other targets lead by 0.168). The quarter therefore sounds for about 0.25 s between its own transition and the next one, and it never reaches its body.

**Fix** (`build/score_config.py`). One range render, three variants on the same four spans (Fl1 168.8-174.1, Cl1 176.8-182.1, Ob1 184.8-188.1, Bn1 455.9-516):
- **A.** Run heads at v90 instead of v53 (169.0, 177.0, 185.0, 456.0, 496.0). Use `INSTR_POST["vel_cap"]` rows `{"row": "Leg Slur MAX" / "Leg Slur", "min": 90, "max": 90, "from": head - 0.2, "to": head + 0.1}`. Nothing else changes.
- **B.** Flute, oboe and clarinet runs on **"Leg Slur Runs"** (p.112: seconds only, which these runs are throughout). `ART_SPANS` rows `{"from": 168.8, "to": 174.1, "art": "Leg Slur Runs"}` on Flute 1, the same for Clarinet 1 (176.8-182.1) and Oboe 1 (184.8-188.1).
  - Dynamics on this row come from CC1. Copy each run's CC11 shape into CC1 at the same values over the span.
  - The row name contains "Leg", so the pipeline already treats it as legato.
  - It loads one row per track, so these three tracks need a full rebuild.
- **C.** The c23 sustain-row fix applied to the weak targets: 169.5, 170.0, 177.5, 178.0, 185.5, 187.5 (and the bassoon's 459, 460, 499, 507) on "Sus MAX" / "Sus Non Vib", 0.06 s early, with 0.03 qn overlap.
- In every variant, for Bassoon 1, set the targets after a quarter note (500, 503, 508, 510, 512) to the same lead as the others: 0.168 qn in place of 0.42, at v100 in place of v80. The `leg_leads` / velocity-by-dynamic rows that make them v80 with long leads should skip a target whose previous note is 1 qn or shorter.
- If none of A-C passes, try the untested TLeg hold / decay (`mix.json tleg_env`, hold 550 / decay 250 ms; MANUAL-GAPS c23).

**Pass:**
- Every run note's own-pitch peak within 4 dB of the mean of its two neighbours.
- No join dip over 5 dB.
- Clarinet 1 never more than 6 dB under the accompaniment across 177-182.
- Per-note arrival (pcX) still within 40 ms of the beat.

### 2. The celli's Détaché bass line: every other same-pitch repeat is not re-articulated. The round-robin take decides it (measured; fix partly measured)

**Where.** Violoncellos, "Detache" at v91, qn 40-104 and 600-664. The repeated G2 half notes are at 70, 96-98, 600-608 (five in a row, ff), 628-630 and 656-658. They are unslurred half notes, printed f and then ff, doubled by the basses.

**Evidence.** I counted takes per key from each CC16 reset (39.868 and 599.892).
- **First-take repeats.** Every repeat on the first take after a reset (98, 604, 608, 658) rises only **1.4 / 1.8 / 1.7 / 1.7 dB**. This is the new note's peak in its first 0.2 s against the floor around the note-on, on G2's harmonics.
- **Second-take repeats.** Every repeat on the second take (70, 602, 606, 630) rises **9.3 / 8.9 / 9.1 / 10.3 dB**.
- **The pattern holds for all 8 repeats.** The 1.5-6.5 dB alternation in meas25 is the same effect.
- **The same sample each time.** The 1.5-6 kHz band of the first-take repeats is frame-for-frame identical across 604, 608 and 658.
- **Shape of a first-take repeat** (20 ms frames, from 0.2 s before the note-on): -39 -37 -34 -33 -32 -31 -31 -31 -31 -31 | -32 -33 -34 -35 -35 -36 ...
  - The previous take's tail rises into the gap, and the new note has no attack. Its body also sits about 4 dB under the second-take notes (-35..-37 against -31..-33).
  - In the ff recapitulation the line therefore pulses on every other half note instead of re-bowing each one.
- **Velocity cannot fix it.** The c25 patch reading found no velocity layers on this row (MANUAL-GAPS c25).
- Cause: the row's two-take cycle (bow direction, p.91) (inferred).

**Fix** (`build/score_config.py`):
- **Pairs.** For a pair, reset just before the first note, so that the first note takes the first take and the repeat takes the second.
  - `RR_RESET_AT["Violoncellos"]` add **95.85** (the 96-98 pair) and **655.85** (the 656-658 pair).
  - The existing resets at 103.801 and 679.762 limit the knock-on to 96-103.8 and 656-679.76. MANUAL-GAPS c13 says a reset moves every later take on the track, so compare those spans against c25.
  - 628-630 is already right.
- **The five-note chain 600-608.** Resets cannot avoid a first-take repeat in a chain of five. Use the note end and CC11 instead:
  - On the Détaché same-pitch repeats, set the gap to **0.28 qn (0.10 s)** in place of 0.14 qn. Use `rep_gap_s` 0.10 for celli Détaché repeats, within the research's 60-100 ms default.
  - Add a CC11 notch on the old note: `INSTR_POST["cc_shape"]` lane cc11, rows ("Detache",), `from_note` True, at 602 / 604 / 606 / 608, `pts [(-0.18, 0), (-0.06, -12), (0.0, 0)]`.
  - CC11 crossfades the row's mp and ff groups, so the notch takes the old tail toward the mp group before the new stroke.

**Pass:**
- Every same-pitch repeat in 96-98, 600-608, 628-630 and 656-658 rises 4 dB or more (meas25 measure).
- Bodies of the repeated notes within 2 dB of each other.
- Back-minus-front medians stay at or under +2 dB (c25: -0.5 / -0.9).

### 3. Più allegro, bars 247-250: the trumpets' tenuto is 12-15 dB over the rest of their slur, and the next note is lost under its tail (measured; fix inferred)

**Where.** Trumpets 1-2, a2, qn 984-1000, printed f under one slur: E (tied) D C | **A (tenuto)** G | F E D F A | C B. They double the oboes, clarinets, horns 1-2 and violas.

**Evidence** (each note's p90 level, 200-6000 Hz, 20 ms):
- **Trumpet 1:** 984 -32 | 987.5 -37, 988 -44 | **989 -30** | 991 -32 | 992 -40, 993.5 -41, 994 -44, 995 -45, 995.5 -42, 996 -40, 998 -38.
- **Trumpet 2:** 989 **-28** against -43..-44 for every other legato note.
- The tenuto 989 is the only "Sus Non Vib MAX" note in the slur (keyswitch 988.94). It ends at 991.04, after 991's moved start (990.648).
- **Under 991:**
  - The old A5 stays at -31..-38 until about 0.2 s after the moved start, while the new G5 rises -54, -46, -42, -44. The old pitch covers the new one for 8-23 dB until about 0.1 s after the beat.
  - Trumpet 2 (old F5, new E5): 12-20 dB.
- **In the master,** the 2-5 kHz band moves 3-5 dB with this (989 -33, 991 -36, 992 -38), so the effect is moderate.
- **Horn 1 and Oboe 2 do not show it.** They play the same figure and the same row change, and stay within 4 dB.
- The trumpets' legato targets at CC1 81-90 sit 9-12 dB under their slur head. At 840 and 1056, with CC1 108-115, they match it.
  - So the f layer of "Leg Slur MAX" is the weak part (inferred). The PHRASE_SHAPE "drive" fall (-10 CC1 across the phrase) takes CC1 from 89 to 81 here.

**Fix** (`build/score_config.py`):
- Play the tenuto 989 on **"Leg Slur MAX" as a target** on Trumpets 1-2. This is Movement I's c07 rule: a tenuto to a new pitch goes on the legato row as a target at v100, not as a re-tongued Sus note.
  - Give it its weight in CC11: +2 dB (×1.26, brass CC11 is 20 log10), rising 0.03 s after the note-on, held to +0.40 s, gone by +0.70 s.
  - 991 then becomes an ordinary target (v118 like its neighbours).
- Hold the trumpets' CC1 at the head's value over 984-999.9 (no drive fall on Trumpets 1-2 in this span; `PHRASE_SHAPE` skip span).

**Pass:**
- Trumpets 1-2 per-note p90 over 984-998 within a 6 dB range.
- 989 at most +3 dB over its neighbours.
- G5 / E5 at 991 dominant within 60 ms of the beat.

### 4. Two c25 shapes did not act: Horn 1's CC1 taper before bar 223, and the muted trumpet's slurred joins (measured; values from the measured lanes)

**Horn 1, the dip before 888.**
- The taper is on the lane as written: CC1 107 -> 92 over 887.375-887.68.
- Through it, the stem holds -32 / -33 dB in every 20 ms frame. The only dip is the 0.13 qn gap: -36, which is **3.7 dB** (target 5).
- Horn 2 has the same gap and the same rows and dips 8.3 dB.
- Horn CC1 is a layer crossfade, and at ff it sits on a plateau. c21 critic A #6 already measured that a CC1 move inside a plateau barely changes level.
- **Fix:** replace the CC1 taper on Horn 1 with a CC11 taper.
  - `cc_shape` lane cc11, at 888.0, `from_note` True, `pts [(-0.40, 0), (-0.16, -44), (-0.006, -44), (-0.005, 0)]` in units on the lane value 100, so 100 -> 56, which is -5.0 dB.
  - Keep the 887.879 step to 112-118 at the note-on.
  - Keep Trumpet 1's CC1 taper: its dip is 3.2 dB and meets its target.

**Trumpet 1 con sordino, the slurred joins** ("Mute Sus" at CC11 53-62, 0.168 qn overlap since c25).
- The joins at 685 / 688 / 717 / 726 dip **4.5 / 4.0 / 4.5 / 4.3 dB**.
- They are not holes. They are 0.3 s sags: the new note's own pitch rises from -60 to -55 over 0.25 s while the old one fades.
- **Fix:** a CC11 lift over each sag. `cc_shape` lane cc11, rows ("Mute",), `from_note` True, at 685, 688, 717 and 726, `pts [(-0.02, 0), (0.03, +33%), (0.25, +33%), (0.40, 0)]`.
  - +2.5 dB in the linear brass law: 62 -> 82, 53 -> 71, 60 -> 80.
  - It also raises the old note's last 0.06 s, which is the point of a crossfade fill.

**Pass:**
- Horn 1 dips 5 dB or more before 888, and its 888 peak time stays within 20 ms of c25.
- Every slurred join in 680-728 dips 3 dB or less, with no bump over +2 dB at +0.1..+0.4 s.

### 5. The 30 fader steps inside notes: none is a printed fp / sfp, and one is a harp jump of +8 dB (measured)

I ran `stepcheck.py` on the c25 parts: moves of 2 dB or more within 60 ms, strictly inside a sounding note. Its count of 30 matches CHANGES. None falls at the printed fp (qn 832) or sfp (592). Every one breaks the standing rule. By kind:
- **22 hairpin snap-backs (+2.5..+2.9 dB) at a score onset inside a led note.** A decrescendo's dB ramp returns to 0 at the written onset, but the note there started 0.12-0.27 s earlier:
  - Oboe 1 909.9 / 931.9, Oboe 2 913.9 / 931.9.
  - Violins I 295.9 / 775.9 / 909.9 / 913.9 / 949.9.
  - Violins II 295.9 / 531.9 / 775.9 / 909.9 / 913.9 / 949.9.
  - Violas 775.9 / 931.9.
  - Celli 383.9 / 551.9 / 931.9 / 967.9.
  - Basses 931.9.
  - On the stems these steps fall inside the legato transition's own 9-16 dB rise (Violins I 910: lead 0.25 s; Violins II 532: 0.27 s), so each adds a small late bulge, not an audible click.
- **3 front weights:** celli 15.5 (+6 dB inside the last quarter of the turn figure), celli 1032 (+6), Trombone 2 152 (+3.5).
- **4 role edges inside led notes:** Violins II / Violas / Celli 375.9 (-4, "sul tasto, last 2 desks"), Violins I 484.9 (-3, "4 soli").
- **1 role end on ringing notes:** Harp 512. The [488, 512] -10 dB role from c25 returns to 0 over 512-512.5 while the arpeggio notes of 506.5-511.5 (6 qn long) are still ringing. The harp stem jumps **-53 -> -45 dB within about 0.2 s**. This is the one step a listener will hear.

**Fixes:**
- **Harp.** Take the 488-512 cut into the instrument: harp velocity and CC11 both set loudness (p.69; the KS Master has the Velocity->Volume path since c22). Use a `vel_cap` scale or a CC11 lane -10 dB over 488-511.9, then follow the printed crescendo 512-520 as a ramp in CC11. Remove the role.
- **Snap-backs** (`tools/score_to_parts.py`, generic, default off; Finale on): when a hairpin's dB ramp ends at a score onset whose note is led (qn < sq), end the ramp at the moved note-on and return to 0 over 0.25 s from there, not in one step at sq.
- **Front weights and role edges.** Move the three front weights into CC11 shapes (`cc_shape` from_note, the same dB through each track's CC11 law). Put the role edges in the rests before the led notes (`ROLE_EDGE_XF`, as c25 did for Violins II).

**Pass:** stepcheck inside-note count 30 -> 0 or near it, and the harp's level at 512-512.5 within 3 dB of its level at 511.5.

## The coordinator's c25 list, through this lens

- **Celli bass line on Détaché.** The swell is gone (meas25 back-front -0.5 / -0.9). The repeats are finding 2: the take order, not the row.
- **Basses' pp re-bows (rises 2.6 / 1.6 / 4.1 dB).** Only 190.533 is over the +3 target.
  - The c25 range slope (-10 -> -14 units took the rise from 5.7 to 4.1 dB, about 0.4 dB per unit) gives **-18 units** on that bow alone: about +2.5 dB.
  - I did not measure the master's 30-150 Hz range (8.9 dB) for its causes. The pedal is only one of them.
- **Violins I marcato fronts, 5 dB over Violins II.**
  - This is the marcato sample of "Sus Marc LITE" at v92. Removing the region gain lowered only the sustain body (front -27.5 / body -32.3 at qn 0).
  - Try velocity **80** on the Violins I chords at 0 / 16 / 372 / 584 / 1104 in a range pass, on the assumption that the marcato layer follows velocity (inferred; not measured).
  - Pass: front within 3 dB of Violins II, and the -3 dB point still within 30 ms of the beat.
- **Inner lines, Violins II countersubject (9-13 dB under Violins I).** On the HS Sus MAX row, CC1 is the vibrato crossfade.
  - The scherzo's c23 critics measured a CC1 floor lifting soft legato notes +3 to +16 dB on Violins I without touching the notes before.
  - Try a CC1 floor of **100** on Violins II over 631.9-659.9 instead of more CC11, which would cross the bright layer at 94 (inferred).
  - Pass: the c25 table's Violins II minus Violins I at -5..-7.
- **Muted Trumpet 1 joins and Horn 1 before 888.** Finding 4.
- **Thirty fader steps inside notes.** Finding 5.
- **Not measured here** (other lenses):
  - Stops after bars 94 / 113, the 223 / 263 in-bar steps and ties, the timpani at 223, loud_eq.
  - Horns 2 / 4 per-pitch levels after "Mono From Left".
- **Other movements' findings:**
  - Scherzo Woodwind Sus Accent MAX on flute accents: does not apply. Our flute accents play on Sus MAX / Leg Slur MAX, and no Finale track uses a "Sus Accent" row.
  - Scherzo CC11 lift on soft slurred string pairs starting after the previous release: applies to the Violins II note_cc offsets. Their 0.02 s pad means the old tail rises for 20 ms only, so nothing to change.
  - Scherzo Sus Marc LITE failing on Violins II / viola accents: consistent with ours. Only Violins I uses that row here.
  - Scherzo Violins I staccato peaks at 81-98 ms: not measured here.
  - Scherzo: delivery compression costs 2-5 kHz beat contrast. The brass accents below have room for it.

## Other checks that passed (measured)

- **Accents, 2-5 kHz first 80 ms minus body, brass, 880-1090.** Medians -16 to -2 dB on every brass track, the worst +4.1 (Trombone 2, 1081). No accent bites, and Dan's "a little overdone" needs no general raise.
- **Pizzicato, 200-264 / 456-488.**
  - Onsets 2-10 ms after the score onset (-10 dB point). -3 dB points 25-58 ms.
  - Peak SD 1.1-2.2 dB on Violins II, Violas and Celli.
  - The basses spread more (SD 3.5-4.3, four plucks 8-10 dB under their neighbours: 206, 238, 476, 484). This is round-robin dependent, the celli double the line, and the gain is small.
- **Tremolo arrivals** at 888 / 1088 / 1108: every string section reaches -3 dB of its body within 20 ms of the beat. Nothing is held over 6 s at the end.
- **Harp étouffez** at 326 / 520 / 968 / 1112: stems fall to silence within 0.2 s (returns keep the ring).
- **Chorale violas' portato** (892-911) and Violins II (924-931): re-articulated, 5-9 dB dips at f.
- **Repeats elsewhere.** Winds, brass and upper strings: 0-2 repeats per track under 3 dB. The chorale's re-tongued brass whole notes separate 7-15 dB.

**Do not touch:**
- The GENTLE brass accents and Trumpet 3's c25 accent bump (all under +4 dB of 2-5 kHz front).
- The basses' "Stac On Bow" hammered eighths and their metric velocities (81-102).
- The chorale's brass re-tongue gaps.
- The celli on "Detache" (the row, the v91 and the release caps).
- The harp's Harmonics / Gliss Technique rows and the étouffez cuts.
- The strings' tremolo rows at 888 / 1088 / 1108.
- The c23 sustain-row fix on the 8 wind targets.
- Trumpet 1's CC1 taper before 888.
- Violins I "Sus Marc LITE" as the row for the ff chords.
