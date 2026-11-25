# Cycle 45, critic B: balance and levels (on the c44 render, the first EastWest template mix)

## Method

I measured all 36 stems of `cycles/c44/render/`: the 32 dry stems after the stem fix, plus the four returns. I used 8192-point frames (hop 43 ms) in 1/6-octave bands, mid and side, on the parts.json tempo map. Balance numbers come from the dry stems, as the c44 README asks. A means A-weighted and K means BS.1770 K-weighting. I use K when comparing low instruments and plucked notes.

For comparison:
- c43's 32 stems, which still carried their own Opus hall.
- The Dvořák 9/i reference, measured with the same code.

Labels:
- **measured**: a number taken from the render or the data.
- **predicted**: arithmetic on measured spectra or measured CC lanes.
- **inferred**: a judgement about what a listener hears.

I changed no audio settings and touched no REAPER, build or tool file.

## Manual notes (row c45/B: group B6, May 2021 HO manual PDF pp. 32-34, 43, 46, 191-192, read in full; MANUAL-GAPS.md read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.32-33: preload size by drive type (HDD / SSD SATA / SSD PCIe), "Never Preload", multi-threaded voice renderer | REAPER's memory: 44 GB settled and after the render, 26 GB compressed (c44 CHANGES) | **Yes.** `Preferences.json` has `PreloadSize` 1 and `NeverPreload` false. The c44 mic change loads Close + Main on every string and brass track, and memory still held at 44 GB. No change needed. |
| p.34: Round Robin "Reset Controller": the CC that resets the round-robin cycle is the one entered in Preferences | Every track's pre-roll reset (`build_reaper.py` `RR_RESET_QN` sends CC36) | **No.** `/Library/Application Support/East West/Opus/Preferences.json` has `"RoundRobinResetCC": 16` and `"RoundRobinResetNote": -1`. The pipeline sends CC36, which in the KS Masters is the Repetition script's "Reset RR", not the engine reset. c44's state check found one level run on unchanged data (Bassoon 1 near qn 21: 3 notes, -3.9 dB). Takes that change between renders make level tables unrepeatable. MANUAL-GAPS #10 says to switch in a cycle that refits per-note shapes. **c45 refits everything for the performance data, so this is the cycle to do it:** send CC16 = 127 at `RR_RESET_QN` next to CC36. |
| p.43: Purge (red / yellow / green states); the instrument volume slider is the same control as the Play page and Mix page faders | Opus instrument volume on every track | **Followed.** Level work is done in REAPER (track gain, volume envelope, CC7 / CC11), not in the Opus slider. No purge is used: a purged instrument loads its samples while playing, which would make an offline render depend on load timing. |
| p.46: system usage (voices, CPU, RAM, disk) | the render | Nothing to apply in an offline render. |
| p.191: All Instances window: purge per instrument and per articulation | `UNLOAD_UNUSED_ROWS` does the same job by script | **Followed.** |
| p.192: voice limit per instrument. Each mic position counts as a voice, and dropped voices mean the limit was reached | c44 doubled the mic voices on the strings and brass (Close + Main). The densest spot is bars 61-64 (tremolo on all strings) | **No sign of voice stealing.** The c43 -> c44 state check showed no flips and no holes in bars 61-64. The attack probe found 0 late notes or holes. Keep watching this if any row or mic is added. |

MANUAL-GAPS #8 (4 soli on DIV A) is relevant to finding 3: the basses' 4 soli still play the full section at -3 dB.

## Extra 1: the c44 carry-overs in my area (measured, then predicted)

### Too bright

Master 6-20 kHz share (my band edges) is -23.7 dB; metrics.md reports -24.5. Where it comes from:
- 85% of the top octave comes from the strings (Violins I 62%, Violins II 15%) and 12% from the brass (mostly Trombone 1 in bars 63-64).
- 90% of it falls in bars 53-64 and 71-82, the loud violin passages. The soft passages are already dark: -39 to -46 dB in bars 1-14, 31-44 and 83-92.

Against the Dvořák reference at the same level relative to each file's loudest moment:
- Loudest 6 dB of frames: ours -24.4, Dvořák -27.0.
- -6 to -12 dB: ours -22.5, Dvořák -28.6.
- -12 to -20 dB: ours -24.2, Dvořák -31.9.

The 2-6 kHz band is also about 2 dB over the reference, and 500-2000 Hz is at -4.6, the low edge of the references.

The c43 -> c44 change on the Violins I stem in the same bars: +2.5 to +3.2 dB at 7-15 kHz and -4 to -6.6 dB at 0.5-1.4 kHz. So about half of the brightness comes from the string shelf and half from the 1 kHz body cut, which raises the top's share.

Halving the strings and brass shelves (ONE_TIME's suggestion) gets only to **-25.1** (predicted). Removing the string shelf entirely gets to -26.0.

**Exact values (predicted -26.7 for the whole piece, -27.1 in the loudest frames, 2-6 kHz -9.2, 500-2000 Hz -4.2):**
- `build/mix.json` `groups.string.family_eq` and `tracks["Double basses"].family_eq`:
  - hshelf 4730 Hz **+4.0 -> 0.0 dB** (or delete the band);
  - bell 1005 Hz **-5.0 -> -2.5 dB** (bw 0.945).
- `groups.horn.family_eq` and `groups.lowbrass.family_eq`: hshelf 7490 Hz **+4.0 -> +2.0 dB**.
- `tracks["Violins II"].eq` and `tracks["Violins II div"].eq`: add `{"band": "highshelf", "hz": 5000, "db": -4}`, the same as Violins I has.
- Level make-up so the A-weighted balance does not move (`gain_db` change):
  - Violins I -0.1, Violin I solo -0.2, Violins II -0.2;
  - Violas -0.5, Violas div -0.5;
  - Violoncellos -0.5, Violoncellos div -0.5;
  - Violins II div -0.4;
  - Double basses -0.3;
  - brass 0.
- If the render still measures above -27, also take Violins I and Violin I solo's 5 kHz shelf from -4 to -6 (predicted -27.4, loudest frames -27.8).

Keep the woodwind shelf (winds carry only 3.7% of the top) and the harp shelf (0%). Check the brass 2-5 kHz accent jump again after the change: the shelf sits above 5 kHz, so it should not move.

### Timpani +1 dB stem fix: keep it

Measured: no timpani roll is the loudest stem anywhere.
- Rolls sit 18-24 dB A under the master in bars 1-3, 21-30 dB in bars 67-70 and 22-26 dB in bars 79-81.
- The only window over the finale's 18% cap on the 30-150 Hz share is the printed crescendo roll into the p stroke at qn 172: 28% at qn 170 and 59% at qn 171. The texture there has almost no bass, and rule 5 allows a printed crescendo to grow.
- The f roll at bars 61-62 has the opposite problem (finding 5).

### Trombone 1 at qn 213

Its accent is now 3.6 dB over the pickup (peak over 0-0.35 s; c43 8.3 dB) and only 2.3 dB over the next note. The second accent at 218 is now louder than 213. See finding 5.

## Extra 2: what c45's performance data will do to the balance (predicted)

I applied ONE_TIME's lyrical arch to every phrase of 1.5 s or longer on all 29 sustaining tracks:
- start 33 units under the peak, peak at 0.44 of the phrase, end 32 under;
- on CC11, or CC1 on the `CC1_DYN_TRACKS`;
- converted to dB with the measured CC11 response (kit LEARNINGS §4: 0.57 / 0.35 / 0.25 / 0.12 dB per CC over 0-30 / 30-60 / 60-88 / 88-128);
- then recomputed the solo margins frame by frame.

| | Mix change by section | Solo margins, p10 frames |
|---|---|---|
| Arch with the peak at the printed level (it only subtracts) | Soft passages -3.5 to -4.9 dB, loud passages -1.8 to -2.3 dB. The quiet parts fall 2-3 dB more than the loud ones, so the mix's dynamic span widens, and deliver_master and every soft trim would have to be refit. | Solo violin +1.8 -> -2.6 dB; Clarinet 1 coda +0.5 -> -4.0; Horn 1 bars 67-70 -3.8 -> -5.2; Violins I bars 53-60 -4.3 -> -8.9. Entries and phrase ends drop into the accompaniment. |
| The same arch centred (+16, mean zero) | Level kept (+0.4 to +1.5 dB) | p10 still -2.4 (solo violin), -4.0 (Clarinet 1), -7.3 (Horn 1 bars 67-70) |
| Depth 16 / 16, centred (+8) | Level kept (0 to +0.6 dB) | Every margin within about 1 dB of now; worst: solo violin p10 -1.9, Horn 1 bars 67-70 -1.8, Clarinet 1 -1.0 |

The lead tracks get no additional advantage from the arch: they and their accompaniment arch alike. A's c44 baseline also shows the audio already moves 12-17 dB per phrase, because printed dynamics and samples contribute. The phrase swell (+25 by 0.8 s) works the same way: started from the printed level it adds 6-9 dB at p.

So, for c45:
- **On the level lanes, specify the arch in dB, not CC units:** about ±3-4 dB, which is 16 CC at mid-range.
- **Keep each phrase's mean on its printed dynamic:** peak at the printed CC + 8, start and end at - 8.
- Put the full 33-unit shape on CC1 where CC1 is only vibrato (strings, flutes, oboes, cor anglais, bassoons). There it changes colour, not balance. "Same shape" is then kept; only the depth differs.
- Where CC11 is at 40 or less (pp phrases), keep CC11 flat and draw the arch in the volume envelope. The woodwind and low-wind layer boundaries at CC 30-36 jump 8-11 dB (LEARNINGS §4; `SWELL_CC_CAP` exists for this reason).
- After the render, check that every lead entry keeps its p10 margin of at least +1 dB, at:
  - qn 48-66 (solo violin);
  - 226-238 (Horn 1);
  - 280-292 (Clarinet 1).

**Short-note rules (predicted, partly measured):**
- **"CC parked high for shorts"** on the viola pizz. (qn 124-137, CC11 34-46 now) and the basses' pizz. (108-137, CC11 46) raises them by **+14 to +20 dB** at the same velocity (G(118) - G(34..46)). Velocity cannot take that back. If CC11 is parked at 110-127, add a vol_db offset over those spans equal to -(G(new) - G(old)): -15 dB at 108-137 for the basses, and -15 to -20 dB following the hairpin for the violas. Then measure.
- **Beat-position velocity with ±5-7 random:**
  - Timpani strokes (v56-96): the felt strokes have an 8-16 dB step between v56 and v64 (LEARNINGS §10). Leave the timpani out.
  - Harp: Harp Sus RR has layer edges at 57/58 (Pluck) and 42/43, 70/71 (Thumb), with 10-12 dB between the RR groups (LEARNINGS §9). Our pp 52 / p 64 straddle the 57/58 edge, so ±12 would cross a layer on every other note.
  - Measured evidence from series 1 c16: +6/+3/-3 by beat on pizz. and harp gave only 0.5-1.2 dB more on downbeats and doubled the basses' pizz. peak spread (1.7 -> 3.3 dB), and was reverted. By the ONE_TIME rule, this is evidence for dropping the beat pattern on the harp and pizz. rows. Where the pattern is kept (viola pizz. triplets, bars 41-44), centre it on the current velocity (first note +8, last -8), so the group's mean level and its balance under the cor anglais (+7.5 dB now) stay put.
- **Doublings sharing one curve** (Flute 1 and Violins I at bars 61 and 79): no balance change if each track's trims and roles stay on top, as the plan says. Check bars 61-62 and 79-81 against finding 2 after the render.

## Findings, ranked by what a listener would hear

### 1. The loud violins are 3-6 dB too bright in the top octave (measured; fix predicted)

- **Where:** Violins I and II (and the brass shelf) over bars 53-64 and 71-82 (qn 172-220, 238-274). These bars hold 90% of the piece's 6-20 kHz energy.
- **Evidence:**
  - At the same relative level, the master's 6-20 kHz share is 2.6-7.7 dB over the Dvořák reference (Extra 1); 2-6 kHz is about 2 dB over.
  - Violins I alone supplies 62% of the top octave even with its own 5 kHz -4 shelf.
  - The c43 -> c44 stem difference shows the cause: the template's +4 dB 4.73 kHz shelf adds about +3 dB at 7-15 kHz, and the -5 dB 1 kHz bell takes 4-6.6 dB of body.
  - Halving the shelves, as ONE_TIME suggested, gains only 1.4 dB.
- **Fix:** the exact values in Extra 1, `build/mix.json`:
  - string shelf 0 dB (`groups.string` and the basses' own family_eq);
  - string 1 kHz bell -2.5 dB;
  - brass shelves +2 dB;
  - Violins II and Violins II div highshelf 5 kHz -4;
  - string `gain_db` make-ups -0.1 to -0.5 dB.
- **Check:** master 6-20 kHz share -26.5 to -28 dB, loudest 6 dB of frames at -27 or lower, 2-6 kHz -9 to -11, 500-2000 Hz no lower than -4.6.
- **Inferred:** the loud string passages will sound like a section in a hall rather than close-miked violins.

### 2. The woodwinds lost 1-2 dB against the strings in c44, and in the ff tuttis they now add almost nothing (measured)

- **Where:** all 11 wind tracks; most of all bars 61-62 (qn 204-212) and 79-81 (262-271), also bars 53-60 and 71-78.
- **Evidence:**
  - Wind family minus strings (K), c43 -> c44:
    - bars 61-62 -4.1 -> **-5.6**;
    - 79-81 -0.6 -> -2.2;
    - 57-60 -6.3 -> -7.3;
    - 71-78 -5.9 -> -7.1;
    - 45-52 +1.8 -> +0.4;
    - 15-22 -3.4 -> -5.3.
  - Per track against Violins I at 61-62 (all printed ff): Flute 1 -8.6 -> **-10.7**, Oboe 1 -10.2 -> -13.2, Flute 2 -9.1 -> -11.9, Clarinet 1 -9.7 -> -10.5, Bassoon 1 -12.9 -> -14.7.
  - At 79-81: Flute 1 (the B flat 6 melody with Violins I) -2.6 -> -4.7; Clarinet 1 -5.6 -> -9.4; Bassoons -6.3 / -7.6 -> -10.6 / -10.4.
  - Rimsky-Korsakov (Principles, "Comparison of resonance", p.33): in forte one string section equals two wind instruments, so a single wind sits about 3 dB under its section. Here the ff winds sit 7-15 dB under Violins I.
  - The causes:
    - c44's make-up was fitted on whole-piece A-weighted level, which the soft wind solos dominate.
    - The c44 stem fix lowered Flute 1 by 1 dB and Oboe 1 by 1.5 dB.
    - Series 1's roles still cut the winds at the climax: Flute 1 [204, 208, -4], Oboe 1 [204, 208, -3], Clarinet 1 [204, 210, -4], Clarinet 2 [204, 208, -2.5], Bass clarinet [204, 208.5, -4].
- **Fix:**
  - `build/mix.json`: every wind track's `dyn_trim_db` gets **f +1.5, ff +2.0** on top of the current values (0 at p, so the solos and soft passages do not move). For example Flute 1 {f -2.5, ff +1}, Oboe 1 {f 2.5, ff 2}, Clarinet 1 {f -3.1, ff -1.3}, Bassoon 1 {f 3, ff 1.5}, Contrabassoon {f 2, ff -0.8}.
  - `build/roles.json`: Flute 1 [204, 208, -4] -> **-1.5**; Clarinet 1 [204, 210, -4] -> -2; Bass clarinet [204, 208.5, -4] -> -2.
- **Predicted:** winds minus strings at bars 61-62 about -3 K, at 79-81 about -0.2 (the c43 values). The master rises about 0.5 dB at bars 61-62, so check the limiter.
- **Check:** Flute 1 within 3-6 dB K of Violins I at 61-62 and within 3 dB at 79-81; Violins I still the loudest stem in both.

### 3. The basses fell 2-3.5 dB against the celli in soft passages; the bass pedals under the horn solo and in the coda are thin (measured)

- **Where:**
  - Double basses: bars 23-30 (pp), the 4 soli E flat 2 pedal at bars 65-70 under Horn 1 (qn 220-238), the coda pedal (274-304), and the final chord's root.
- **Evidence (K, Double basses minus the reference stem, c43 -> c44):**
  - vs Violoncellos: 66-90 -7.3 -> **-9.4**; 286-301 -6.4 -> -8.5; 238-262 -4.0 -> -5.6; 204-212 -5.4 -> -6.7.
  - vs Horn 1 at 226-238: -10.8 -> **-14.3**.
  - The celli 4 soli (on Vc div) now sit +2.1 dB K over the tutti basses at 274-286; both are printed ppp.
  - Causes:
    - the string HPF 53 Hz plus the master HPF 42 Hz;
    - Duc's -3 dB at 228 Hz;
    - the basses' return send turned off.
  - Kit LEARNINGS §4 (c06): at pp-p the Basses KS Master needs +3 to +5 dB to stand with the celli; c06 took Cb - Vc from -8.1 to -2.6.
  - The 20-100 Hz share of the master (-19.7) is still between the references, so the loud passages are not short of bass. Bars 61-62: basses 43% of 30-150 Hz.
- **Fix:** `build/mix.json` `tracks["Double basses"].soft_trim_db` {ppp 4, pp 6, p 6.5} -> **{ppp 6, pp 8, p 8.5}**. Leave f/ff, the loud_eq rows and the 400 ms pp/p cap as they are.
- **Predicted:**
  - Cb - Vc at 66-90 -7.4 K and at 286-301 -6.5 (c43 levels);
  - basses vs Horn 1 at 226-238 -12.3 (Horn 1 still leads by 12 dB);
  - basses level with the celli div at 274-286 (+0.1).
- **Later:** MANUAL-GAPS #8 (a DIV A track for the 4 soli) would let the soli sound like four players instead of a quieter tutti.

### 4. Two wind solos are covered in places: the cor anglais's held A4 at bar 48, and the bass clarinet at bars 33-34 (measured)

**(a) Cor anglais, bar 48, qn 152-155.4 ("solo, espr.", p; Violins II pp).**
- The held A4 falls from 23.3 dB A (qn 151) to 20.0 / 17.8 / 16.0 at qn 152 / 153 / 154.
- At 153-154 the celli and Violins II are +1.5 and +3.6 dB over it (margin over the accompaniment -3.7 and -6.1).
- Across bars 47-50, 52% of the solo's frames are under +3 dB of margin.
- The note carries `note_trims.json` `"Cor anglais": {"152": -8}` on top of the A4 pitch trim -5. Its volume envelope reads -9.6 to -10.9 dB over the whole note, while the next notes are back at +1 to +2 dB.
- This is the stale negative trim that LEARNINGS §4 (c25) warns about.
- **Fix:** `build/note_trims.json` Cor anglais "152": **-8 -> -3**. Predicted: the note at 21-23 dB, level with its neighbours, and the margin at 153-154 about +1 to +2 dB over Violins II.

**(b) Bass clarinet solo, bars 33-34, qn 99-101.**
- The bass clarinet is printed mp; the cor anglais's dolce line is printed p.
- Measured margin at qn 99 / 100: -0.7 / -2.5 dB, with the cor anglais +1.8 dB over the solo at 100.
- Over all of bars 31-36 the solo leads its accompaniment by only +3.0 dB, and half its frames are under +3.
- **Fix:** `build/roles.json` Cor anglais [98.5, 102, -3] -> **[98.5, 102, -5.5]**.
- **Check:** bass clarinet at least +3 dB over the cor anglais at qn 99-101.

### 5. Bars 61-64: the low brass gained 1-2 dB over c43, the f timpani roll vanishes, and Trombone 1's accent lost its weight (measured)

**(a) Low brass, bars 61-62 (qn 204-212).** Measured:
- Trombone 2 (one player, printed f under the ff tutti) is the second-loudest stem: 42.6 dB A, against Violins I at 45.5. It is louder than Violins II, the celli and the ff Horn 1 (39.6).
- Trombone 2 + bass trombone + tuba together sit only 0.4 dB under Violins I, while the four horns sum to 5.3 dB under the strings.
- Against Violins I (K), c43 -> c44: Trombone 2 -3.8 -> -3.0, bass trombone -5.0 -> -3.9, tuba -7.3 -> -5.4. Horns are unchanged (Horn 1 -5.0 -> -5.1).
- The low brass also send nothing to the hall now, which makes them sound closer than their level alone suggests (inferred).

Fix, restoring c43's relation:
- `build/mix.json` Trombone 2 `dyn_trim_db.f` 4.4 -> **3.6**;
- `build/roles.json` Bass trombone [200, 214, 3, 1] -> **[200, 214, 2, 1]** and Tuba [200, 214, 3, 1] -> **[200, 214, 1, 1]**.
- Bass trombone and tuba together hold 44% of the 30-150 Hz band there (basses 43%), so the cut also clears the bass.

**(b) Timpani f roll, qn 204-209.5.** It settles to 28-31 dB A under the master, with 1-3% of the 30-150 Hz band. Bars 79-81's f roll sits 22-26 dB under, and c43 had the timpani 22.2 dB under the strings at bars 61-62 (now -25.4). Kit LEARNINGS §10 (c25) records the same overshoot on soft rolls.
- **Fix:** `build/roles.json` Timpani add **[204.25, 209.5, 3, 0.25]**.
- **Check:** 30-150 Hz share at 6-15%, the timpani still 20 dB or more under the master, and no change at the 209.5 stroke.

**(c) Trombone 1's accent at qn 213 (ff marcato quotation).**
- Peak over the first 0.35 s per note, c43 -> c44:
  - 212.5 pickup -26.8 -> -31.1;
  - 213 -18.5 -> -27.5;
  - 214.5 -24.6 -> -29.8;
  - 218 -23.0 -> -26.0.
- The accent is now +3.6 over the pickup and +2.3 over the next note, and quieter than the 218 accent.
- The 2-5 kHz bite measure has a lot of room left: first 80 ms minus body -10.0 dB; master jump at 213 -5.8 dB against the +2 limit.
- The accent shelf `loud_eq` 2 kHz -4 at 212.9-213.4 and CC7 110 were set in series 1, before the brass family EQ removed 5-8 dB at 475-821 Hz, which is where this note's weight is.
- **Fix:** `build/mix.json` Trombone 1 `loud_eq` points for the 213 window set to 0. Keep the 215 window. `build/roles.json` Trombone 1 [212.4, 213.6, 3] -> **[212.4, 213.6, 5]**.
- **Predicted:** 213 about 6 dB over the pickup and 3-4 dB over 214.5-217.5; master 2-5 kHz jump at 213 about -2 dB. Re-check against rule 9 after the render.

### 6. The harp is 6-10 dB under the rest of the accompaniment at its own attacks, except in bars 7-14 (measured)

- **Where:** Harp in bars 37-44 (qn 108-140, printed p while the strings are pp), bars 53-56 (172-188) and bars 71-78 (238-262).
- **Evidence (K, the frame starting at each harp onset, against the sum of all other non-lead stems):**
  - 108-124: median -7.6 dB (p10 -10.6);
  - 124-140: -10.0;
  - 172-188: -9.5;
  - 238-262: -6.0;
  - bars 7-14: +1.2, which matches c43 B's target of the harp level with the bassoons.
- At 108-124 the harp is 6.0 dB K under the pp Violins II div (sul tasto) and 4.9 under the pp violas.
- Roles still cut it by 4 and 7 dB there ([108, 124, -4], [124, 140, -7]).
- c44 gave the harp +2.2 dB of make-up for a template EQ that took 4.9 dB A.
- Rimsky-Korsakov (p.33): sustained groups "easily overpower" plucked instruments. The score asks for the harp a level above the strings here.
- **Fix:**
  - `build/mix.json` Harp `gain_db` -1.8 -> **+1.2**;
  - `build/roles.json` Harp: add **[17.9, 42.0, -3.0, 0.5]** (bars 7-14 stay as they are) and change [124, 140, -7] -> **[124, 140, -5]**.
- **Predicted:** harp attacks -4.6 dB (108-124), -5 (124-140), -6.5 (172-188) and -3 (238-262) against the accompaniment, still 5 dB or more under every lead.
- **Inferred:** the harp's chords become audible as a part rather than a faint click.

## Also measured, no change

- **Solo margins** (A, lead over the sum of all other dry stems):
  - Horn 1 bars 7-14 +8.0;
  - Oboe 1 bars 15-16 +5.7;
  - solo violin bars 17-18 +9.9 and bars 21-22 +3.1 (over its accompaniment, excluding the oboe);
  - Flute 1 bars 37-40 +5.8;
  - cor anglais bars 41-44 +7.5;
  - Oboe 1 bars 45-47 +4.5;
  - Horn 1 bars 67-70 +5.6;
  - Clarinet 1 coda +4.5 (+6.3 over the cor anglais);
  - Violins I over the celli at 292-301 +5.9.
  All are in the c44 B target ranges.
- **Divisi and soli:**
  - Violins II div against Violins II (bars 37-40): -0.3 dB A.
  - Violas div against Violas: +2-3 dB when both play (bars 23-30, coda), unchanged from c43 (+0.5 -> +0.6 K over the window).
  - Horns 1-2 a2 over Horn 3 at bars 79-81: +2.3 dB (two horns against one).
  - Harp harmonics over the celli div at 274-283: +3.1 A, a printed p over ppp. Keep the +2 role.
- **Dynamic mapping:** at pp the string sections (12.5-14.8 dB A), the accompanying winds (8.9-13.7) and the horns (12.1-14.9) agree within about 2 dB. The exceptions are the harp (finding 6) and the ff winds (finding 2).

**Do not touch:**
- the c44 return levels and IR envelope (my numbers are on the dry stems);
- Horn 1's bars 7-14 role and the -1.5 dB on the bassoons and bass clarinet;
- c42's +3 on Horn 1 at 184.1-195.35;
- the coda Clarinet 1 / cor anglais levels;
- Violins I's 5 kHz -4 shelf (finding 1 adds to it, never removes it);
- the horns' soft 800 Hz shelf;
- TIMP_CC1_MAP and the timpani CC7 roll shapes;
- the bar 66 niente in CC7;
- the basses' loud_eq rows and pp/p release cap;
- the celli coda role [291.9, 300.9, -2.5] that keeps Violins I on top;
- the timpani +1 dB stem fix.
