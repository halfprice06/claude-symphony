# Cycle 44, critic A (articulation and phrasing), on the c43 render

Every number comes from the c43 render (`cycles/c43/render/`, stems and master) and from `cycles/c43/rendered_build/parts.json`, which is the same file as `build/parts.json`. The comparison figures come from c42 (`cycles/c42/render`, `rendered_build`). My scripts ran in `/private/tmp/claude-501/mockup-loop/mvt2-c44-A/`, which I deleted when I finished. Their methods are described at the end.

This cycle changes the mix (loop/ONE_TIME.md). Cycle 45 adopts the performance data in EW-TEMPLATE-PLAN.md sections 5-9. Finding 2 gives the baseline that c45 asked for. Findings 1, 3 and 4 can go into c44 or c45.

## Manual notes (MANUAL-READING row c44 / A: group A4, May 2021 HO manual PDF pages 108-113, read in full; MANUAL-GAPS.md read)

| Manual (PDF page) | Where in this mockup | Does the render follow it? |
|---|---|---|
| "Flute 2" was played by a different flautist and shares no samples with "Flute", so the two do not merge in unison (p.108) | Flute 2 (bars 79-82, 268) | Yes. Flute 2 loads `FL2 KS Master.oib` and Flute 1 loads `FL KS Master.oib`. |
| Sustain: all 3 dynamic layers start together and the controller crossfades them (p.109). The "Mod Wheel" wording is Play-era; 2025 p.52 and the patch files win | Every woodwind Sus/Leg note. Dynamics are on CC11 (clarinets on CC1, `CC1_DYN_TRACKS`); CC1 is the vibrato crossfade on flutes, oboes, cor anglais and bassoons | Yes. It matters for c45: a phrase swell drawn in CC11 crosses the layer boundaries (LEARNINGS section 4: woodwind boundaries at CC 30-36, +8-11 dB jumps). See finding 2. |
| Sus Expressive gives a slower attack and gently increasing vibrato (p.109) | The espr./dolce wind solos (MANUAL-GAPS #5) | Not used. It is still the library's built-in version of the "swell after the onset" that finding 2 measures as missing on winds. |
| Legato Repetitions RRx4: a re-tongued repeat inside a sustained phrase, with a 4-way round robin on the attack (p.109-110) | Flute 1 136 (since c37) | Yes at 136: own-band dip 6.0 dB, master 2.8. The bass clarinet's slurred repeat at 33 does not use it; it dips only 3.1 dB own-band (finding 1). |
| Shorts have no release trails; hold the last note so the hall rings (p.110) | v600 prints no wind staccato | n/a |
| Repetitions and runs effects (p.111-113) | none in v600 | n/a, correctly not used |
| Legato needs no gap and an interval of at most an octave. Legato patches are monophonic unless CC22 is 0-63 (p.112) | Every wind/brass Leg row | Yes. Scan: no wind or brass legato join wider than 12 semitones (`wide_leg` is empty on every track), and no simultaneous onsets on any Leg row on any of the 32 tracks. |
| Legato Slur Repetitions: separate re-tongued samples for same-pitch notes inside a slur (p.112) | Merged slurred wind repeats: Cor anglais 271 (merged into 269 in the bar 81-82 slur) and bass clarinet 33 | Not used (it was untried in c37 too). It is the row to try for the bass clarinet at 33 (finding 1). |
| KS Masters switch articulations with keyswitches (p.113) | All woodwind tracks | Yes. No keyswitch arrives within 0.02 qn after a note-on on any track. |

## Findings, ranked by what a listener would hear

### 1. Soft printed string repeats still run together. Their gap is 29-36 ms, against 60-100 ms where repeats do separate (S1)

**Where.** These are the printed same-pitch repeats that STR_REP_NEW_BOW plays as "soft" re-bow points:
- Violins II 51, 120, 144, 289, 292;
- Violins II div 114, 116, 119 (sul tasto, Flautando);
- Violas 50, 62, 71, 81, 87, 198, 271, 283;
- Violas div 70, 79, 289;
- Double basses 81.

Three loud repeats run together for a different reason (gap too short or release too long): Double basses 265 (f, bar 80), Horn 2 208 (ff tenuto) and Violas 81.

**What is wrong (measured).** I took all 66 printed contiguous repeats in mockup-events.tsv (not tied, pizz. and tremolo excluded). For each I measured the MIDI gap in parts.json and the dip at the repeat. The dip is measured three ways: the stem broadband, the stem's own band (harmonics 1-4 of the pitch, 60 ms frames), and the master.

| MIDI gap | n | median stem dip | median own-band dip | own-band under 3 dB | median master dip |
|---|---|---|---|---|---|
| under 60 ms | 27 | 3.7 dB | 3.3 dB | **13** | 3.1 dB |
| 60-100 ms | 31 | 7.3 | 7.1 | 2 | 3.1 |
| over 100 ms | 8 | 11.4 | 14.7 | 0 | 3.6 |

The string repeats sit in the first row. Their median gap is 35 ms (IQR 33-60), against 86 ms on the winds and 100 on the brass. The cause is `REBOW_GAP_QN` = 0.03 qn: the "soft" STR_REP_NEW_BOW path reuses the loop re-bow machinery, and its gap is meant to be inaudible. The worst own-band dips are:
- Violins II 289: 0.3 dB;
- Violins II 120: -1.8;
- Violins II div 114 / 116 / 119: 0.0 / 1.7 / 0.9;
- Violas 271: 0.6;
- Violas div 79: 0.7;
- Violas 81 and 87: 2.2 each. At 81 the gap is only 6 ms, because the next note's lead eats it.
- Violas 198: 2.9 (16 ms gap).

The loud repeats:
- Double basses 265 has a 60 ms gap and dips -0.8 dB. Its `sus_fall` only applies at p or softer, so at f the release fills the gap.
- Horn 2 208 dips 2.7 dB. Its REP_RETONGUE_AT gap is 33 ms, the frac limit on a short note.

The 60-100 ms repeats show that the samples do separate when they are given the gap: basses 156 and 168 dip 4.2 and 7.9 dB, celli 148 dips 7.3, violas 253 dips 8.7. EW-TEMPLATE-PLAN section 8 makes 60-100 ms the default for this reason.

**Fix.**
- (a) Generic, in `tools/score_to_parts.py`: a new key `STR_REP_NEW_BOW["soft_gap_s"]`, default 0.08. It is the gap before a printed "soft" repeat's re-bow piece, i.e. a point that comes from `rep_rebows`, not from AUTO_REBOW or a listed loop point in REBOW_AT. Loop re-bows keep `REBOW_GAP_QN` 0.03 qn. Give those pieces the `sus_lead_s` 0.10 s lead (the note before gives way so the gap is kept, as on the sus_min_s path). Extend `sus_fall` to every string track for them: `{"cc": 6, "s": 0.06, "max_cc": DYN["mp"]}` (8 CC on the basses as now).
- (b) For loud repeats, add a `"loud_gap_s": 0.10` with a 6 CC `sus_fall` and no max_cc, used at CC 72 or louder. This covers Double basses 265 and the violas' f repeats.
- (c) `build/score_config.py`, `REP_RETONGUE_AT["Horn 2"]` 208: gap 0.08 s instead of the frac-limited 33 ms (a per-onset `gap_s`, or the `WIND_REP_RETONGUE` frac 0.25 -> 0.4 for brass).
- (d) Bass clarinet 33 (a slurred repeat, own-band 3.1 dB): put it on "LegRep RRx4" with `WIND_SLUR_REP_MERGE_SKIP`, as Flute 1 136 is, and re-level its body by about -8 dB (c37 measured the row 8-11 dB hotter).
- After the render, re-run `fit_rebows.py`. The soft pieces' fills were fitted for the 0.03 qn gap, and c44 also changes the hall.
- Target: an own-band dip of 4-8 dB at every printed repeat, and none under 3.

Judgement: measured (gaps, dips). That the fix closes the gap is inferred from the 60-100 ms row.

### 2. Baseline for c45 (plan sections 5-9): legato and repeat timing is close to the plan, but phrase shape in the controllers is flat

Measured on all 32 tracks in parts.json (harp and timpani excluded). The dynamic lane is CC1 on `CC1_DYN_TRACKS` and CC11 elsewhere. A phrase starts after at least 0.3 s with no note sounding and must last at least 1.5 s; "hairpin" marks a printed hairpin inside the measured window. The audio figures come from the stems: 100 ms RMS against the level at +0.10-0.25 s.

| Plan item | Plan target | c43 measured (strings / winds / brass) |
|---|---|---|
| Legato overlap (old note end minus new moved onset) | strings 45-80 ms, winds and brass 33-58 ms | median 45 / 45 / 45 ms (IQR 40-46). `LEG_OVERLAP` = 0.04 qn, which is 41-49 ms at 49-60 bpm. Strings sit at the bottom of their range; winds and brass are inside theirs. |
| Repeated-note gap | 60-100 ms | 35 / 86 / 100 ms (printed repeats; finding 1) |
| Legato velocity | 90 or more, following the dynamic (r about 0.35) | strings and brass 124 on every target (`LEG_VEL_STRONG`; coda 90, sostenuto 108). Winds median 60 (IQR 60-80): `score_to_parts.py` gives v100 / 80 / 60 by note length (< 0.45 s / < 0.9 s / longer), not by dynamic. |
| Phrase swell after the first onset | about +15 by 0.4 s, +25 by 0.8 s, nothing before the onset | Lane: +0 / +0 / +0 at 0.4 s and +1 / +0 / +0 at 0.8 s on phrases without a hairpin. None reaches +10 by 0.8 s except 17% of wind phrases in CC1 (the delayed-vibrato rule). The vol_db envelope adds -2.2 / +0.2 / +0.2 dB by 0.8 s; the strings fall because the entry fills decay. **Audio: +2.8 / +0.7 / +0.7 dB by 0.8 s.** The strings get theirs from the sample's own bloom; winds and brass have none. |
| Before the onset | flat | 24 / 42 / 15% of phrase starts rise more than 2 CC in the 0.25 s before the score onset. These are the entry leads, which hold the entry level from the moved onset: correct, keep them. |
| Taper over the last second | about -20 (CC1 19 higher 1 s before the end, 8 higher at 0.5 s) | Lane: +3 / +1 / 0 (no hairpin), +5 / +6 / +2.5 (hairpin). vol_db: +1.9 / +1.4 / +1.5 dB. **Audio: +2.6 / +0.9 / +2.5 dB.** Winds hardly taper. |
| Phrase arch (phrases of 4 s or more) | peak at 33-62% of the phrase, range 30-60 units | Lane peak at 39% / 25% / 24% (only 16-18% of phrases inside 33-62%); range 23 / 22 / 4 units (brass CC1 nearly flat). Audio peak 46% / 46% / 50%, but only 40 / 32 / 21% inside 33-62%; audio range 16.9 / 11.8 / 12.8 dB (it includes the printed dynamics). |
| In-slur lean-off | about -2 per note by 0.4-0.8 s | Lane +1.3 / 0 / 0 (strings rise slightly). vol_db -0.5 / -1.1 / -0.2 dB: the legato fills already lean off a little. |
| CC point density inside phrases | 7-13 points/s | CC1 2.0 / 1.4 / 0.6, CC11 3.3 / 2.9 / 3.0 points/s |

**What a listener hears (inferred from the table).** Winds and brass phrases start at their level and end at it, and the first second of each phrase is flat. The strings move a little because of the sample bloom. This is the "machine" quality the expert files do not have.

**Rules in `tools/score_to_parts.py` that would need to change for c45:**
- Overlap: `LEG_OVERLAP` = 0.04 qn (line 59) becomes a per-family value in seconds, converted on the tempo map at the target note. For example `LEG_OVERLAP_S = {"string": 0.065, "wind": 0.045, "brass": 0.045}`. Keep `FAST_LEG_OVERLAP`, the lead cap (`LEG_CAP_FRAC`) that moves the previous note's end with it, and the rule against overlapping into the same pitch (LEARNINGS section 5).
- Repeat gaps: `REBOW_GAP_QN` on the soft printed-repeat path (finding 1); `STR_REP_NEW_BOW` `gap_s` 0.06 -> 0.08; `STR_REP_NEW_BOW["portato"]` `gap_s` 0.03. c41 cut it from 0.05 because 0.05 opened 12-18 dB holes at Violins II 44/50, so test 0.06 with `sus_fall` rather than adopting it blind. `WIND_REP_RETONGUE` (gap 0.06, frac 0.25) is already at 86 ms; only raise frac.
- Legato velocity: the `leg_target` branch at about line 2705. Strings and brass: velocity from the printed level, at least 90 (for example `value_at([(22, 90), (46, 98), (72, 110), (114, 124)], base(q))`), keeping `CODA_SOFT` and `SOST_STR_LEG_VEL`. Winds: replace the length rule with the same map (floor 90; Cor anglais keeps its c04 values or more). Velocity sets the transition speed on the string and brass scripts (manual p.144, p.104-105). Re-measure every legato lead afterwards, because LEARNINGS section 5 says velocity changes moved crossovers by 0-80 ms.
- Phrase swell, taper and arch: a new generic `PHRASE_SHAPE` applied after the printed dynamic curve, overridden inside printed hairpins (the plan's rule): rise from the first onset, peak in the middle third, taper over the last second.
  - Write it mostly in dB in `vol_db` (for example +2.5 dB by 0.4 s, +4 dB by 0.8 s, -4 dB over the last second, scaled by 0.5 at pp and 1.0 from mf), and only the part that stays inside one layer in CC11 or CC1. With c44's post-fader sends to the returns, a volume-envelope taper no longer cuts the hall return's tail (inferred; check S3 on the c44 render).
  - The plan's +25 CC is a CC1 macro value that moves vibrato and the layers together. On our patches CC11 is the layer crossfade, and 25 CC at p crosses a woodwind boundary (+8-11 dB; manual p.109 and LEARNINGS section 4). Clarinets and brass on CC1 need the same caution with `CC1_DYN_MAP`.
  - Winds and brass first: they measure +0.7 dB of swell against the strings' +2.8.
- Lean-off: leave it out. The vol_db fills already give -0.5 to -1.1 dB, and -2 CC is about 0.5 dB.
- Density: `sample()` (line 1691) uses a 0.125 qn grid, at most about 7 points/s at 52 bpm, and writes a point only where the value changes. A 0.0625 qn grid is enough. Density follows from the shapes above; on its own it changes nothing.
- The CC1-only pass-2 test: our KS Masters map CC1 to the vibrato crossfade (strings and most woodwinds) or to the layers (brass, clarinets), not to EW's "Mod + Expression Combo" macro. The test needs that macro in the Opus state (`build_reaper.py` / `opus_state.py`), not only new lanes from score_to_parts.

Judgement: the table is measured; what is heard is inferred.

### 3. Wind legato arrivals are 20-40 ms late and their legato velocity is 60. Bass clarinet per-onset leads; Clarinet 1 194 is not late

**Where and what (measured, `tools/pcx.py` on the c43 stems).** Legato pcX medians:
- winds late: Oboe 1 +36 ms, Bassoon 1 +39, Bass clarinet +33, Cor anglais +26, Flute 1 +19, Clarinet 1 +12;
- strings: Violins I +23, Violins II +18, violas +2, celli +1;
- Horn 1: -19.

The winds' long legato targets play at v60 (the length rule; finding 2). LEARNINGS section 5 records the cor anglais at v60/v80 with 150-185 ms transitions.

- **Bass clarinet (open item, +33 ms).** I only want to move the joins where the crossover and pcX agree. Values are pcX / crossover in ms:
  - 22: +45 / +54;
  - 31: +63 / +68;
  - 92.5: +32 / +58;
  - 97: +28 / +86;
  - 98: +62 / +44;
  - 99: +44 / +28;
  - 106: +18 / +80.

  The large pcX readings at 32 (+78) and 108 (+58) have early crossovers (-66, -92). Their extra leads are already enough, so leave them.
- **Clarinet 1 194 (open item, +120 ms).** It is not late. In 60 ms frames the C6 band overtakes the D flat 6 band between -0.05 and 0.00 s (crossover -2 ms, window 34 ms). The note then sags about 3 dB at +0.15 s and grows 4 dB to +0.55 s. pcX takes that later peak as its reference.

**Fix.**
- `build/leg_leads.json` "Bass clarinet": add +0.04 s at 22, 31, 98 and +0.03 at 92.5, 97, 99, 106. Leave the family `LEG_LEAD_S` at 0.09.
- No lead for Clarinet 1 194. Close the item.
- For c45, use the plan's wind legato velocity of 90 or more (finding 2). Expect the wind medians to move earlier, then refit `LEG_LEAD_S` for the winds from the next render rather than raising them now.

Judgement: measured. The velocity effect on winds is inferred.

### 4. Violas' sotto voce portato eighths (bars 48-51): two identical samples alternate, and every second A3 peaks 0.15 s late

**Where.** Violas qn 152.5-167.5, Detache row (key 30). Every note is at velocity 37 with the same CC11 shape (39 at the moved onset, falling to 34).

**What is wrong (measured, stem).**
- On the repeated A3s the peaks alternate exactly between two takes: -47.4 dB at +0.15 s with a 412 Hz centroid (152.5, 154.5, 157.5, 161.5) and -47.8 dB at +0.30 s with a 565 Hz centroid (153.5, 156.5, 160.5). The four "down" notes match each other within 0.1 dB and 4 Hz.
- This is the bow-direction round robin, which cycles per pitch (manual p.91-92: "a Round Robin (RR) cycle that alternates between up and down bow").
- With a deterministic RR reset, the same two takes come back note after note. The late take puts the perceived attack 0.30 s after the eighth's onset, 0.15 s later than its partner (S2).
- The D sharp 4s (164.5-167.5) show the same pairing: +0.12 s / 926 Hz against +0.03 s / 463 Hz.

**Fix.** `build/score_config.py`:
- (a) Velocity alternation with a small seeded jitter on these 15 notes, for example 37, 33, 39, 34, 38, 33, ... (a `VEL_SET["Violas"]` entry per onset). Detache follows velocity as well as CC11, so the takes stop being identical copies.
- (b) Extra entry leads in `build/entry_leads.json` on the late-take A3s: 153.5, 156.5, 160.5 get +0.10 s (total under the 0.30 s cap). This needs the RR order to stay as now: CC36 reset at the pre-roll, and the same note count on the Violas track before bar 48. Re-measure after the render, because any change upstream can swap the two takes.
- Target: the A3 peaks spread 0.5-1.5 dB, and every peak lands by +0.18 s.

Judgement: measured (peaks, timing, identity). The velocity response of Detache is inferred from the manual.

### 5. Violins I timing run at 261.8-266 is render variation, not data. Re-check it on the c44 render

**Where.** Violins I legato joins 257, 262 and 266 (bars 78-80).

**What (measured, pcX c42 -> c43, same data).**
- 257: -47 -> +57 ms;
- 262: +101 -> -3 ms;
- 266: -49 -> +36 ms.

Every other join from 255 to 270 is identical to the millisecond. Crossovers move the same way (257: -42 -> +58; 262: +113 -> +9; 266: -4 -> +56). This is a state difference: the actor rebuilt Violins I after the render. The c44 full rebuild is the real re-test.

**Fix.** No data change now. After the c44 render, run `tools/state_check.py` against c43 and `pcx.py --tracks "Violins I"`. If 257 and 266 stay at +40 ms or later in two renders running, add -0.04 s to each in `build/leg_leads.json`. 262 (now -3 ms) needs nothing.

Judgement: measured.

### 6. Articulation checks that passed on c43; repeat them after c44's mix change

These all measured correct, and c44's new returns and EQ can change some of them:
- **Trombone 1's quotation (bars 63-64).** 2-5 kHz over the first 80 ms minus the body: 213 accent +1.0 dB, 218 accent -7.6. The master's 2-5 kHz jump is +1.2 at 213 and -1.7 at 218. Levels over the neighbours: 213 is 7 dB over the 212.5 pickup, 218 is 2.3 dB over 217. This is weight, not bite. The c44 brass make-up of +4-6 dB after the family EQ (+4 dB shelf at 7.5 kHz) raises the 2-5 kHz attack too. Re-measure 213 and 218 and keep attack minus body at +2 dB or less.
- **Loop pulsing on held notes.** Autocorrelation at 3.95 s of the 100-300 Hz band and of the centroid:
  - opening chord (master): -0.12 / -0.09;
  - Violins I 0-9: +0.05 / -0.04;
  - basses' 4-soli pedals: -0.08 / -0.11 and +0.04 / -0.05;
  - celli div coda: +0.04 / -0.11;
  - bass clarinet pedal: -0.03 / +0.16.

  None show the loop period. The final chord is too short above -25 dB (5.8 s) to compute.
- **S3.** The master's fastest 50 ms fall is -3.0 dB at the fp of bar 47 (qn 148), -2.3 dB at the 195-196 dip, and -3.7 dB in the bar 66 niente. The niente's stems fade over two beats (Violins II -46 -> -61 dB by 225.5), with no cut tails.
- **Mutes.** CC15 sits in the rests before each muted entry and matches the score (Violins II, violas and celli from 42; Violins I "gli altri" from 65; off before 108/124/171; coda 273.5/274.5; Violas div 268.5). It never falls on a note-on.
- **Keyswitches.** No keyswitch on any track arrives within 0.02 qn after a note it governs, and no chord reaches a legato row.
- After c44, re-fit the re-bow fills (`fit_rebows.py`, relevel41 rules for the basses), because they were fitted under the old Opus hall.

Judgement: measured.

## Do not touch

- Trombone 1's two accents (Sus MAX, swell shapes, v124 at 215).
- Clarinet 1's legato lead 0.07 (median +12 ms).
- The basses' c43 items (400 ms pp/p cap, coda re-bow points with the c41 fills, force_at 286).
- Flute 1 136 on LegRep RRx4.
- The entry leads that hold the entry level from the moved onset.
- The release caps (strings 600 ms at pp/p, basses 400).
- The CC15 mute placement.

## Methods

- Overlaps, velocities and gaps were read from parts.json, converted on its tempo map. Legato joins are notes on a Leg row (not LegRep) starting while exactly one other-pitch note sounds.
- Printed repeats are taken from mockup-events.tsv: the same staff and pitch, the next onset equal to the previous onset plus its printed length, and not tied.
- S1 dips: the minimum 30 ms RMS in [t - 0.12, t + 0.10] s against the mean over [t - 0.45, t - 0.15] s. The own-band version uses harmonics 1-4 within ±3% in 60 ms frames.
- Phrase shapes: the controller lanes sampled as written (steps). Audio uses 100 ms RMS on the stems.
- Legato timing: `tools/pcx.py`.
- Accents: 2-5 kHz energy in [0, 80 ms] against [250, 600 ms].
- Loop: 50 ms frames, slow trend removed, autocorrelation at the 3.95 s lag.
