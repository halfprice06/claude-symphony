# Cycle 25, critic A: articulation and phrasing (on the c24 render)

Sources:
- The c24 stems and master (`cycles/c24/render/`).
- The data that made them: `cycles/c24/parts_rendered.json`. `build/parts.json` differs from it only in the delivery ride rows written after the render.
- `build/score_config.py` (the c24 block), `build/mix.json`, `build/mockup-events.tsv`, the score (`v600/score.pdf` p.11, bars 199-208).
- The keyswitch maps (`ks_maps.json`, `build/ks_maps_extra.json`) and the installed Solo Trumpet folders.
- The May 2021 HO manual.
- I re-ran the actor's `cycles/c24/actor_scripts/meas24.py` read-only on the c24 render. Its numbers match CHANGES.md.

"Measured" means a number taken from these files. "Inferred" means a conclusion that a render still has to confirm. Every fix is on the instrument side: rows, velocity, note lengths and leads, CC11 / CC1 shapes. The only volume-envelope changes proposed are held passage levels, which the standing rule allows. None is a per-note move.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 25 (its third round ends at c20). I read the pages behind my findings in full instead, plus `loop/MANUAL-GAPS.md`.

| Manual (May 2021 HO, PDF page) | What it says | Where it applies here | Does the render follow it |
|---|---|---|---|
| p.90 (Strings, Long: Détaché) | Détaché notes have no legato connection and "come to a well defined end". Sustain loops and cycles up and down bows by round robin. | The celli's unslurred half-note bass line, bars 11-26 and 151-166 (finding 1) | No. The line plays on "Sus MAX". Each note needs 0.3-0.5 s to reach its body, and same-pitch repeats are not separated. |
| p.90-91 (Marcato Sustain) | A marcato sample on top of the looped sustain gives "extra power at the start of the note". There is one such row per section. | The accented ff string chords at qn 0, 4, 16, 20, 372, 584, 1104 (finding 2) | On Violins I only (c24). The other sections play "Sus MAX" and have no accent front. |
| p.93 (Marcato, Marcato Long) | Short notes with a strong accent. Only the 2nd Violins and the Basses have Marcato Long. | An alternative for the lower strings' chords (finding 2) | Not suitable: these chords are held, and Marcato Long does not sustain. The CC11 route in finding 2 is the one I propose. |
| p.100-101 (Brass, Long) | Sustain volume comes from the Mod Wheel. Sustain Accent: velocity is the attack loudness. Sustain Marcato: a gentler attack, with velocity as the filter cutoff. | Trumpet 3's accents, bars 255-262 (finding 4) | Accents are a CC11 bump on "Sus Non Vib MAX". The bump is held 0.48 s, so it reads as level rather than as an attack. |
| p.106-107 (Brass Mutes) | Mutes are listed as patches to audition. The installed `05 Mutes` folder has Mute Sus, Mute Sus Accent and Mute StacSs, and no muted legato. | Trumpet 1 con sordino, bars 171-182 (finding 5) | The slurred solo plays on "Mute Sus". Four joins inside the slurs dip 4-7 dB. |
| MANUAL-GAPS #1 / c24 entry (string Marcato Sustain) | Lower strings on "Sus Marc LITE" at v92 "started 13-25 dB under their peak" and were rejected. | Finding 2 | The test moved the ff CC11 step to the moved note-on on Violins I only. On the other sections the step still landed at the score onset, after the led chord had started (see `score_config.py` near line 2547: `if _t not in _C24_MARC_TR: continue`), so that rejection may be confounded (inferred). |

## Findings, ranked by what a listener would gain

### 1. The celli's half-note bass line under the first theme (bars 11-26, 151-166) still swells into every note, and its same-pitch repeats are not heard as separate notes (measured; fix partly measured in the c24 range test)

**Where.** Violoncellos, qn 40-104 and 600-664. The notes are unslurred half notes, printed f and then ff. In c24 they play on "Sus MAX" at v83 / v91, with gaps of 30-50 ms and leads of 0.04 s. The CC11 lane holds 84-87 (f) and 100-105 (ff).

**Evidence.**
- **Swell.** Back (0.6-0.9 of the slot) minus front (0.1-0.4), median **+2.9 dB**; 11 of 42 notes are over +4. Worst notes: 52 +8.1, 54 +6.0, 62 +6.8, 612 +8.1, 624 +5.7 (meas24 on c24).
- **Shape inside a note**, 25 ms frames from the moved note-on:
  - The first 0.1 s is the old note's release at full level.
  - Then a 6-10 dB dip from about +0.15 to +0.35 s.
  - The new note reaches its body only at +0.4..+0.5 s, in the back half of a 0.71 s note. At 606: -1 0 -1 -2 -2 -4 -3 -6 -10 -10 -10 -10 -9 -6 -5 -5 -3 dB. The ff statement does this as well as the f one, so the CC11 layer is not the cause.
- **Repeats (S1).** On the celli stem, the new note's peak in its first 0.17 s minus the floor in the 0.1 s before it:
  - 604 **1.7**, 606 **1.1**, 608 **1.6**, 630 **1.0**, 658 **1.7**, 70 **1.0**, 98 2.9 dB.
  - Celli: 20 of the 56 repeats in the movement are under 3 dB. The basses: 5 of 345.
  - The basses double this line on "Sus MAX" and separate the same notes.
  - The chorale's celli repeats (892-932) are printed "change bow at will", so low separation is correct there.
- **In the master.** The 100-400 Hz back-front is still +4.1 / +4.3 / +3.6 / +6.3 dB at 614 / 618 / 622 / 624, and +4.4 / +4.0 at 62 / 64.

**Why.** This is the Sus MAX attack of the celli: about 0.4 s to body at every dynamic (measured). The scherzo's c21 note says capping the legato sustain attack does not fix string swell, so a cap is not the fix.

**Fix** (`build/score_config.py`, the c24 celli bass-line spans):
- Play both statements on **"Detache"** (key 30, manual p.90) at **velocity 91**, not v83:
  - `ART_SPANS["Violoncellos"]` rows `(40.0, 104.0)` and `(600.0, 664.0)`, art "Detache".
  - `vel_cap {"row": "Detache", "min": 91, "max": 91, "from": 39.9, "to": 664.1}`.
- Why v91 on both: c24's range T1 played both statements on Detache. The ff statement at v91 was flat (median -0.4 dB, every note -3.8..+1.6). The f statement at v83 swelled 9-23 dB on three notes, so v83 is the bad velocity layer (inferred).
- Bring the f statement to its level with a held passage level on the celli for 40-104 (slow balance, allowed). Fit its value on the range render against the basses (c24 celli-minus-basses in 40-104 as the target).
- Keep the T1 release caps on the celli Detache groups ("1V mp" / "1V ff", 700 / 528 ms shipped): 300 ms at f, 150 ms at ff. Put them in `mix.json sus_release_cap_ms` as a celli row on "Detache". The scherzo's c21 caution about an unmatched 5 s release applies here.
- Same-pitch repeats keep a gap of 0.05 s (`rep_gap_s`). Other joins keep 0.03 s.
- Stop the span at 664 so the slurs of 668-676 stay on the legato rows.

**Pass:**
- Celli back-front median at most +2 dB, with no note over +4.
- Every repeat at 602-608, 628-630, 656-658 separated by 4 dB or more.
- Master 100-400 Hz back-front at most +3 dB on every half note of 612-628.
- The -3 dB point of each note within ±30 ms of the basses'.

### 2. The lower strings play the accented ff chords of bars 5 and 147 with no accent front, and reach their body late (measured; fix inferred)

**Where.** Violins II, Violas and Violoncellos at qn 16 (bar 5). The celli also at qn 584 (bar 147). The chords are printed ff with accents in every string part. Violins I plays them on "Sus Marc LITE" since c24.

**Evidence.**
- **Body at -3 dB, against the score onset** (150-6000 Hz, 10 ms frames; body is the median of 0.25-0.6 s):
  - qn 16: Violins I +25 ms, Violins II +0, Violas **+40**, celli +0, basses **+90**.
  - qn 584: celli **+150 ms**, Violins II +30.
- **Front: the peak in the first 0.3 s minus the body.**
  - qn 16: Violins I **+3.2**, Violins II +4.9, Violas **+0.1**, celli **-1.4**, basses -0.2 dB.
  - qn 584: Violins I +4.8, Violins II +2.1, Violas +2.7, celli **+0.1** dB.
  - The lower strings have no accent. Their level grows into the chord instead.
- **CC data.**
  - At qn 16 the lower strings' CC11 steps from 82-83 to 99-100 exactly at 16.0. The chord also starts at 16.0 (lead 0). Opus smooths CC, so the chord starts on the lower layer.
  - c24 moved this step to 0.06 s before the note-on for Violins I only.
  - The lower strings get no accent bump: `skip_rows` exempts only the marcato row, but none of the CC11 lanes holds a bump at 16.0.
  - At 584 the celli step 88 to 106 at 584.0, with the note-on also at 584.0.
- **Master.** The peak comes +225 ms after the beat at qn 16 and +325 ms at qn 584 (the c24 target was about 150).

**Fix** (`INSTR_POST["cc_shape"]` with `"from_note": True`, CC11, in the c24 block next to the Violins I rows; the strings' Sus MAX is flat above about 103 and loses about 0.7 dB per unit under 100, `loop/LEARNINGS.md` c18):
- **qn 16**, on Violins II, Violas and Violoncellos: `pts [(-0.06, 17), (0.0, 22), (0.12, 22), (0.30, 0)]`.
  - This moves the ff step 0.06 s ahead of the note-on.
  - It adds a front at 104-105 (the knee) for 0.12 s, about +3 dB, and settles back to the printed ff by 0.3 s. That is weight, not bite, and the bump stays under the knee, so it cannot overshoot.
- **qn 584**, on Violoncellos: `pts [(-0.06, 18), (0.0, 18), (0.01, 0)]` plus `onset_lead` 0.04 s ("set", rows "Sus"). Violins II and Violas already step and lead at 584.
- Leave the basses alone. Their lane is 115 at the note-on, so CC11 cannot help, and the slow attack is the sample.
- Second option, as an A/B on the same range render: "Sus Marc LITE" on the celli only at 16 / 584 / 1104, with the c24 step move applied to the celli as well (it was not applied in the c24 test) and the top marcato layer (v111). The celli's 2-5 kHz content is low, so the top layer's brightness matters less there than on Violins I.

**Pass:**
- Every lower-string section within +30 ms of the score onset at its -3 dB point, at 16 and 584.
- Front minus body +2 to +4 dB.
- 2-5 kHz in the first 80 ms no more than +3 dB over the body.
- Master peak at qn 16 at +175 ms or earlier.

### 3. Each new bow of the basses' pp pedal (bars 43-50) blooms 5-10 dB and then sags: the master's low band pulses with it (measured; fix inferred)

**Where.** Double basses, B flat 1 pedal 164-199, split into bows at 170.859 / 181.676 / 190.533. All bows are on "Sus MAX", with gaps of 30 ms and a CC11 lane of 33 falling to 27.

**Evidence.**
- **Per bow**, 0.5 s frames from 0.5 s before the note-on:
  - 170.86: -54 -59 -54 **-49** -53 -52 -57 -59
  - 181.68: -61 -60 -63 -62 **-54** -56 -58
  - 190.53: -59 -62 -55 **-51** -55 -55 -58
- Each bow peaks 5-10 dB over the level at its start, 0.75-1.5 s in, then loses 4-8 dB by its end. So every re-bow is heard as a swell after a fade. meas24 gives +9.8 / +7.5 / +10.2 dB.
- **In the master**, the 30-150 Hz band over 168-200 runs -59 -52 **-48** -53 -55 ... -58 **-53** -57 **-50** -56: steps of 5-9 dB under the soft motive x solos.

**Fix.** The coordinator notes the interleaved-divisi pedal is not in the tools, so this is the instrument-side fix: a CC11 counter-shape on each bow.
- `INSTR_POST["cc_shape"]["Double basses"]` rows with `from_note: True` at 170.859, 181.676 and 190.533. The `at` keys match the split notes' `sq` in parts.json.
- `pts [(0.0, 0), (0.35, -8), (1.6, -8), (2.6, 0)]` takes out the bloom.
- Add `(2.6, 0), (3.1, 4)` on the 3.9 s bow (170.86) to hold up its tail.
- About 0.55 dB per unit, estimated from the 164-168 hairpin: CC11 52 to 32 with a -3 dB ramp gave -14 dB.
- Range-test -8 and -14 units against a control from the same start.
- A generic version: let `tools/fit_rebows.py` write its fitted rebow fills as CC11 shapes (INSTR_POST) rather than volume fills, which the standing rule now forbids.

**Pass:**
- Each bow's maximum (0.15-1.5 s) minus its level at the note-on at most +3 dB.
- The level at each bow's end within 3 dB of its body.
- Master 30-150 Hz range over 168-199 at most 4 dB.

### 4. Trumpet 3's accents in bars 255-262 are a held level bump, not an attack, and the one at 1044 is missing (measured; fix inferred)

**Where.** Trumpet 3, qn 1016-1046: accented half notes alternate with plain ones, printed f, then ff from 1032, then a crescendo into the fff at 1048. All play on "Sus Non Vib MAX". Brass CC11 is linear volume here (`cc_scale_k` 20).

**Evidence.**
- **Lane.** Accented notes get CC11 108-120 from 0.09 s before the note-on, held 0.48 s. Plain notes rest at 87-103.
  - 20 log10(117 / 88) is +2.5 dB at 1016, but only +1.4 dB at 1040 (120 / 102), because the ff lane already sits near the ceiling.
  - At **1044** the lane has no event between 1043.5 and 1044.6, so the accent is not played at all.
- **Stem.** Accented peak (first 0.24 s) minus the mean of the two plain neighbours' peaks: +1.9, +1.75, +1.3, +3.1, +1.4, **-0.65**, **+0.35** dB. The median is +1.4. meas24's +0.5 mixes in the crescendo.
- **Front minus body on the accented notes** (first 0.24 s against 0.3-0.5 s): +3.5, -0.7, +1.5, +0.5, +3.0, +3.1, +0.3, **-2.7**. Because the bump is held as long as the body, half the accents have no front at all.
- **2-5 kHz.** Every Trumpet 3 accent is 6-16 dB under its body (median -10.3), so there is room for weight with no bite.

**Fix** (`build/score_config.py`):
- Lower Trumpet 3's resting lane over 1015.5-1047.9 with `cc_scale` -3 dB (k 20, so resting values become about 0.71x). Restore the level with a held passage level of +3 dB over the same span (allowed).
- On Trumpet 3, change the accent row to `hold_s` 0.20 and `end_s` 0.35 (now 0.48), `max` 127. That gives about +4 dB of room above the resting lane, and the bump becomes a front.
- Find out why 1044 has no bump: a hairpin skip (`hp_soft_acc`?) or the `max_step` cap. Accents inside a crescendo must still be played.

**Pass:**
- Accented peak minus the mean of its neighbours +2 to +3 dB on all eight, including 1044.
- Front minus body +1 to +3 dB.
- 2-5 kHz front minus body at 0 dB or less.

### 5. Trumpet 1's muted solo is slurred in the score but re-attacked in the render at four joins (bars 172, 179, 182) (measured; fix inferred)

**Where.** Trumpet 1, "Mute Sus" row (the 1TP KS Master has no muted legato row, and the installed `05 Mutes` folder has none either). The score prints a slur over 680-694 and another over 712-728, p dolce cantabile, doubled by the cor anglais.

**Evidence.**
- Dip at each join: the minimum from -0.1 to +0.15 s against the lower of the bodies before and after, 200-6000 Hz.
- **688: 5.5 dB** (50 ms gap). **715: 4.1** (no gap). **726: 6.6** (60 ms overlap). **727: 4.8** (51 ms gap).
- The other 18 joins are under 4 dB.
- Even at 726, with a 60 ms overlap, the new note's attack comes too late to cover the join.

**Fix.**
- Make every join inside the two slurs overlap by 0.06 s: `gap_set` on Trumpet 1, rows `("Mute",)`, from 680 to 729, `gap_s` -0.06, `allow_leg` False. "Mute Sus" is a sustain row and plays polyphonically, so the two notes crossfade.
- Add an `onset_lead` of 0.04 s on the slur-internal targets at 688, 715, 726 and 727, so the new attack reaches its body as the old note fades.
- Do not put the solo on "Leg Slur MAX". It would lose the mute.

**Pass:**
- Every slurred join in 680-728 dips 3 dB or less.
- At +0.15 s the old pitch sits at least 10 dB under the new body (no smear).
- The breath at 696 and the rest before 712 are kept.

### 6. Before the fff at bar 223, Horn 1 and Trumpet 1 still barely lift: their releases fill the 100 / 90 ms gaps (measured; fix inferred)

**Evidence.**
- Dips before 888: Horn 1 **3.1**, Trumpet 1 **1.6** dB. The others: Horn 2 6.8, Horn 4 4.5, Trumpets 2-3 7.2 / 6.9, Trombones 4.3 / 4.1, Tuba 6.4.
- Horn 1's envelope (20 ms frames, 150-6000 Hz) holds at -11 dB and only reaches -14 in the gap. The release covers it.
- **Horn 3 and the Bass trombone are not faults.** At 884 they play the same pitches as Horn 2 (D4) and Trombone 2 (B2), and those unisons are dropped. Those two parts lift 6.8 / 4.1 dB.

**Fix.**
- A CC1 taper on the last 0.25 s of the 884 note: `cc_shape` lane "cc1", `at` 888.0, `from_note` True, `pts [(-0.38, 0), (-0.14, -15), (-0.006, -15), (-0.005, 0)]`.
  - Horn 1 and Trumpet 1 only.
  - Brass CC1 is the dynamic layer, smoothed over 120 ms, so the taper has to begin before the gap.
  - The 888 CC1 step to 120 stays at the note-on.
- Keep Trumpet 1's 0.08 s gap (the leading-tone B to C).

**Pass:**
- Horn 1 dips 5 dB or more and Trumpet 1 3 dB or more.
- The 888 attack's peak time on both within ±20 ms of c24.
- The master's in-bar step at 223 still +3 dB or more on the mp3.

## The coordinator's c24 list, through this lens

- **"Sus Marc LITE" on Violins I.** The ff chords do strike now:
  - Violins I front minus body is +3.2 / +4.8 / +6.2 at 16 / 584 / 1104, and its -3 dB point is +25..+35 ms after the score onset. Master peak at bar 5 is +225 ms (c23 +375).
  - The lower strings are the rest of the problem (finding 2).
  - Another row for them: Violins II's "Marc Lng RRx4" (p.93) is a short note and cannot hold these chords. Violas and celli have only "Marc Shrt RRx4" besides "Sus Marc LITE".
  - The CC11 front is the route I propose, with a celli-only "Sus Marc LITE" A/B as the second option.
- **Celli bass line.** Finding 1. "Detache" at v91 on both statements, with release caps. The celli legato sags at 286 / 860 are not re-measured here.
- **Basses' pp re-bows.** Finding 3. A CC11 counter-shape per bow is the instrument-side fix that the standing rule leaves open.
- **Dips before 888.** Finding 6. Horn 3 and the Bass trombone are unison drops at 884, not faults.
- **Oboe 1, bars 143-144: why the range result did not transfer.**
  - The final render did not play T1's lane. T1 had CC11 74-79. The final has 82-88 (+3.5 instead of +5 at k 33). c23 had 91-98.
  - On the stem, Oboe 1 over 568-576 is -43.3 dB in c23 and **-43.5** in c24. So 91 to 82 changed nothing, while T1's 74-79 gave about -6.6 dB.
  - The oboe's CC11 response is flat from about 82 up and steep below it: a layer boundary between 79 and 82 (measured on two points, inferred between).
  - The c24 note "woodwinds switch dynamic layers with CC11" is exactly what breaks a smooth k law here.
  - Fix: write T1's lane (+5 at k 33, CC11 74-79), which puts the oboe in the softer mf layer. Bring it from -7.8 back to the -4 to -5 target with a held passage level of +3 dB on Oboe 1 over 567.5-576.
- **Trumpet 3 accents.** Finding 4. The +0.5 dB is partly a measurement artefact (the crescendo); the true median is +1.4. 1044 has no bump at all.
- **Bar 113 stop at 14.4 dB.** A hall and delivery item, not measured here.
- **Horn 3 under Horn 4 and Trombone 1 accents.** Trombone 1's accents measure -1.3 / -4.7 / -6.2 dB (2-5 kHz front minus body), so the fix holds.
- **Listening pass, other items.**
  - Brass accents across the movement: 2-5 kHz front minus body medians are -7 to -16 dB on every brass track, with no accent over +3 dB apart from Horn 1 at 56 (+6.2, on Leg Slur) and Trombone 2 at 1081 (+4.1, on Leg Slur). Dan's "overdone" note is not about brightness: no general raise is needed or wanted.
  - Slurred lines inside slurs: no gap over 60 ms between different pitches on any string or wind track.
  - The only gap of that kind is on Horn 2 at 1004, and it is not a hole. Horn 2 doubles Horn 1 in unison over 1000-1011, and the unison drop leaves Horn 2 only two isolated notes, 1004 and 1008, both on "Leg Slur" at v124. That is likely a small doubling bump on two notes of Horn 1's line (inferred, not measured). Worth checking: drop those two fragments as well, or keep the whole line doubled.
  - The harp's harmonics (qn 168) and the glissando at 1106-1108 play on their rows.
  - Hammered eighths: the basses are on "Stac On Bow", and same-pitch repeats are not separated by under 3 dB anywhere except 5 of 345.
- **Other movements' findings.**
  - Scherzo c21, Detache release: applies to finding 1 (the celli Detache groups need the cap).
  - Scherzo c21, the 150 ms cap on staccatos: does not apply. Our caps cover only the "Sus MAX" and "Sus Marc LITE" rows.
  - Scherzo c21, a legato attack cap does not fix swell: consistent with finding 1, so do not try it.
  - Scherzo c22, Sus Marc LITE at about 130 ms: Violins I peaks +125-225 ms here, consistent.

**Do not touch:**
- Violins I "Sus Marc LITE" at v92 on the ff chords.
- Trombone 1's tongued accents at 985 / 993 / 1001.
- The 888 gaps of 0.08 / 0.10 s and the 1048 lift.
- The basses' "Stac On Bow" hammered eighths.
- The chorale's re-tongued wind and brass repeats, and the celli and basses' "change bow at will" pedals (low separation is correct there).
- The harp's Harmonics and Gliss Technique rows.
- The GENTLE brass accents: no accent bites.
