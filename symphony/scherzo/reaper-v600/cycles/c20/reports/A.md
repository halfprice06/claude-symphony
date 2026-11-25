# Cycle 20, critic A: articulation and phrasing (on the c19 render)

Data judged: `cycles/c19/render` (stems and master) and `cycles/c19/build_render/parts.json`. c17 and c18 renders are the comparisons. Scripts and numbers are my own, from scratch files (deleted after this report). "Measured" means read off the stems or parts.json; "inferred" means reasoned from the manual, patch files or earlier cycles and not checked on audio.

## Manual notes (May 2021 HO manual, PDF p.160-162 and p.188-190; MANUAL-READING row 20, slot A7)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| Articulations window: each row has a load switch, and a row that is switched off is unloaded from RAM (p.160) | `UNLOAD_UNUSED_ROWS`; per-track row sets | Yes. Rows a track does not use are unloaded (memory 43-44 GB). |
| Trigger option "Keyswitch": an articulation is selected by a MIDI note outside the playable range; the active row is shown in yellow (p.161, p.189) | every KS Master track; 1135 row changes in parts.json | Yes, measured. Keyswitch to next note-on: median 45 ms, p10 6.8 ms, minimum 5.3 ms, none after its note. The attack probe reports 0 late notes or holes. |
| "Keyswitch Range" with pass-through and offset (p.161, p.189) | none | Not used, and not needed. |
| Trigger option "Velocity": a short accent row set to velocity 110-127 sounds together with a sustain, so hard notes get an accent attack (p.162, p.190) | the accented half notes after staccato eighths in the theme head (Flute 1, Oboe 1, cor anglais, Violins I; bars 42-49, 106-118, 274, 306-334) | Not used. Inside a KS Master the rows are exclusive (only the triggered row plays). Layering would need a second instance or a zone set up for it in the Opus state. Finding 2 measures the weak accent fronts this feature is meant to fix. |
| Zones "Group": only the triggered instrument in a group plays (p.188) | the same exclusivity | Followed implicitly; no zone layering. |
| "Voice Limit": voices are stolen at the limit; raise it if voices drop (p.188) | the "non div." chords (bars 72, 105-120, 300, 305-320, 339) | Followed, measured. The Violas KS Master's voiceLimit is 350. Parts.json has at most 4 simultaneous notes on any string track (Violins II at qn 1014), so no voices are stolen. No chord reaches a monophonic legato row (0 cases on any track). |
| Octave and Key Range for splits (p.188-189) | none | Not used, and not needed. |

## Findings, ranked by what a listener would hear

### 1. The string legato swell is the start of the transition sample at the old pitch, and it repeats exactly from render to render. The c19 range test was compared against the wrong control

**Where.** Leg Slur MAX joins on Violins II, Violas, Violoncellos, Violin I solo and Violas div. The worst joins (peak over the louder of the two notes, dB):
- Violas: 726 (bar 243) +13.1; 582 +9.8; 363 +8.6; 387 +8.4; 725.5 +8.1; 375 +7.7; 632 +7.4; 162 +6.8; 693 +6.6; 136 +6.6.
- Violins II: 373.5 / 374 (bar 125) +11.3 / +10.3; 361.5 +8.4; 841.5 +6.6; 163 +6.3.
- Celli: 516 (bar 173) +11.0; 572 +8.1; 792 +8.0; 506 +7.2; 944 / 344 +7.1 / +6.8; 637 +6.4; 800 +6.1.
- Solo: 1065 +9.6; 1049 +7.9; 1054 +6.1.
- Violas div: 1047 +9.1; 635 +9.0.

They cluster in the second idea (bars 45-55, 121-130, 277-283), the trio tune (169-198, 211-219), bars 241-243 and the solo (349-358). These are the espressivo lines, so each slurred note swells into the next.

**Evidence (measured).**
- The "join excess" metric overstates the swell. It reads +3.2 median, with 96 of 429 joins over 6 dB, but it compares the peak with the *next* note's body only. Measured against the louder of the old note (level 30-150 ms before the moved note-on) and the new note's body, the excess is:
  - +1.9 dB median, p80 +4.0, 29 joins over 6 dB;
  - on next notes held 0.5 s or more: +1.4 median, against +4.5 on the old metric.
  - So about 1.3 dB of the "+3.2" is the previous note simply being louder than the next note's body.
- What the swell is, measured on harmonic bands of the old and new pitch (50 ms window, 30 ms hop):
  - In every bad join examined, the energy rises on the **old** pitch's harmonics, 30-180 ms after the moved note-on.
  - Celli 572: old pitch 24 -> 35 dB; celli 344: 30 -> 39; violas 363: 16 -> 24; violas 582: 25 -> 31; Violins II 163: 32 -> 37.
  - The new pitch takes over only around the beat.
  - So the sample that plays the start of the slur, still on the old pitch, is 6-12 dB louder than the old note's sustain was. It is not an overlap of two sustains.
- Per-join behaviour is deterministic.
  - The same joins in c17, c18 and c19 correlate 0.97 on this excess, with a median per-join change of 0.1-0.2 dB.
  - All 29 joins over 6 dB in c19 were within about 2 dB of the same value in c18 and c17.
  - So the "round-robin scatter of ±2 dB" in the c19 celli range test (CHANGES.md: TLeg -2 dB, median +3.9 -> +3.5, single joins ±2 dB) came from comparing a range render that started at qn 504 with the full render. A different start position gives different round-robin positions.
  - That test does not show that the TLeg gain has no effect. A -2 dB gain against ±2 dB of start-position scatter could not show anything.
- Velocity is not the lever. The legato speed start offset, (vel - VELO_MIN) / (127 - VELO_MIN) x START_MAX, correlates 0.01 with the excess. Per-section velocity-to-excess correlation is -0.14..+0.09.
- Manual p.144: velocity sets only the transition timing, not loudness.

**Fix (one change per line, each with a control render from the same start).**
- (a) Violas, one range from bar 240 to 246 (qn 717-738):
  - render it twice from the same start, once without and once with `region_gain_db` layer "group:TLeg" at **-6 dB**, not -2 (`build/mix.json`, Violas; the c19 tool form);
  - measure the old-pitch harmonic bump at 726 / 725.5 / 735, and the dip after the transition.
  - Adopt it if the bump falls by 3 dB or more with no new dip over 5 dB. Then try it on the celli (the 506 / 516 / 572 range, bars 168-191).
- (b) Celli only, a separate test: `"legato_speed": {"RELEASE": 200}` in `build/mix.json` (patch value 443 ms; `tools/build_reaper.py` already supports the key, from mvt1 c41).
  - Mvt1 c41 measured RELEASE 300 for timing and dips (more 5 dB dips together with START_MAX 4800), not for the peak.
  - Whether RELEASE also shapes the old note under the transition head is inferred. Test it alone, on the same range and with a same-start control.
- (c) Only if (a) and (b) fail: "Sus MAX" on the arrival notes that are held 0.5 s or more and still swell (the finale's #98).
  - The arrival is then re-bowed, so it is no longer slurred.
  - Use it only on the 9 long-arrival joins over 6 dB: Violas 726 / 632 / 387 / 375, celli 516 / 637, solo 1065 / 1049, Violas div 1047.
- Report the swell with the both-neighbours metric from now on: median +1.9, 29 joins over 6 dB in c19.

### 2. The accented half notes after the staccato eighths come in under the eighths. The weight arrives 150-250 ms late (Flute 1, Oboe 1, cor anglais, Violins I)

**Where.** The theme head's accented half note, after two staccato eighths:
- the counterstatement, bars 42, 45, 49, 70 (qn 123, 132, 144, 207);
- the tuttis, bars 106-118 and 306-318 (qn 315-351, 915-951);
- bars 274, 298, 334 (qn 819, 891, 999).

**Evidence (measured).**
- First 100 ms of each isolated accent against its two neighbours (c19 `records/acc_c19.txt`, which I re-checked per note):
  - cor anglais -4.8 dB median (13 accents);
  - Flute 1 -1.7, Violins I -1.6, Flute 2 -1.2, Oboe 1 -1.1;
  - target +1.0 to +2.0.
- Level of the accented Sus MAX note in 50 ms windows from the beat, against the first 100 ms of the staccato eighth before it (median per track):

| Track | 0 ms | +50 ms | +100 ms | +150 ms | +200 ms |
|---|---|---|---|---|---|
| Flute 1 | -6.5 | -3.1 | -2.4 | -2.5 | -0.7 |
| Oboe 1 | -3.5 | -2.6 | -2.5 | -1.4 | -1.3 |
| Violins I | -4.1 | -2.0 | -1.6 | -0.6 | -1.2 |
| Violins II | -2.6 | -2.1 | -0.3 | 0.0 | +1.5 |
| Violas | -0.4 | -0.1 | +1.9 | +1.9 | +1.4 |

- On the winds and Violins I the accented note is never louder than the staccato eighth before it in its first 200 ms. At quarter 264 that is nearly a full beat, so the stress is heard on the eighths and the accented note swells in afterwards.
- With the 0.35 s window that c17-c18 used, the same notes read +0.5..+1.8. That window measured the late swell, not the accent.
- Cause in the data:
  - The cor anglais and Flute 1 have `_ACC_BY` (0, 0, 116) and (2, 0, 116), so their accents get no CC11 bump (`build/score_config.py` c17 block, `_ACC_BY`).
  - The eighths before the accents are louder rows at higher velocity: Stac DblTng v122 against Sus MAX v111 at ff, v96 against v93-103 at mf.
  - The accented notes' lead is 35-40 ms on the winds, which play the staccato before them with no lead.
- The Violins II per-note +3.1..+3.6 (123, 819, 840, 144) are row-change steps after the quieter "Stac RRx9". The track median is +0.3, inside Dan's limit (no track median over +3), so they are low priority.

**Fix.**
- `ROW_CHANGE_LEAD_S` (`tools/score_to_parts.py` l.434; its scherzo value goes in `build/score_config.py`): +0.04 s for Flute 1, Oboe 1 and cor anglais on a staccato-to-"Sus MAX" change at an accent.
- `_ACC_BY`:
  - cor anglais (0, 0) -> (6, 6, 116);
  - Flute 1 (2, 0) -> (6, 6, 116).
- Range-test bars 104-120 and check:
  - the first-100 ms isolated median reaches +1.0..+2.0, with no track over +3;
  - the 2-5 kHz energy over the first 80 ms stays within 2 dB of the note body (weight, not bite);
  - the perceived attack (S2, `tools/pcx.py`) stays within 25 ms of the beat.
- Do not raise velocity on the accented Sus MAX note (velocity does not change Hollywood Strings sustain level, `loop/LEARNINGS.md` c18).

### 3. Horn 1's "Sus MAX" G sharps fill the hole, but the note is 10-15 dB brighter than the slurred A4 before it, under a printed diminuendo

**Where.** Horn 1 at 442 (bar 148), 598 (bar 200) and 1077 (bar 360). Each is the end of a slurred A4 -> G sharp 4 sigh under the hairpin that starts at 441 / 597 / 1071 (events.tsv).

**Evidence (measured).**
- Brightness, measured as 1.5-5 kHz against 0.3-1.5 kHz over the body:

| | A4 (Leg Slur MAX) | G sharp 4 (Sus MAX) | slurred G sharp in c18 |
|---|---|---|---|
| 442 | -27.4 dB | -12.3 dB | -22.6 dB |
| 598 | -23.0 dB | -12.3 dB | -23.3 dB |
| 1077 | -26.4 dB | -12.7 dB | -15.4 dB |

- Spectral centroid of the G sharp body: 703 / 758 / 723 Hz in c19, against 468 / 491 / 730 Hz in c18.
- The G sharp's body sits 9.6 / 9.3 / 4.6 dB under the A4. That is acceptable under the printed diminuendo.
- The hole is now 1.6-3.4 dB, which is good.
- The colour is not right: the end of the sigh sounds like a new, brassier horn tone instead of the same breath fading.
- CC1 is 65 / 69 / 67 on the G sharps. The Solo French Horn Sus MAX layers sit at CC1 0 / 50 / 82 / 118, pp / mf / f / ff (mvt1 c46, read from the patch), so these notes fade in part of the f layer.

**Fix (inferred, one range test).**
- In `build/score_config.py`, set CC1 on the three G sharps to 50-52 at their moved note-on: the printed diminuendo reaching its end, on the mf layer alone. Use the CC1 per-note form the horns already use, or a `CC1_SPANS`-style ramp from the A4's value.
- Keep `ART_AT` "Sus MAX" and the 0.05 s lead.
- Accept the change if the G sharp's 1.5-5 kHz ratio comes within 5 dB of the A4's and the hole stays under 4 dB.

### 4. The repeated staccato eighths in the strings run together: dips of 1.2-4.4 dB, against 4.3-8.2 dB in the winds (S1)

**Where.** The B-B / E-E eighth pairs of the theme head.

**Evidence (measured).** Median dip at the second onset against the lower of the two 60 ms peaks; the MIDI eighths are 57 ms long:

| Track and row | Bars: median dip |
|---|---|
| Violins II, "Stac RRx9" | 57-72: 1.2 dB; 289-300: 1.0; 305-320: 1.7; 329-336: 2.4 |
| Violins I | 29-44: 1.5; 105-120: 2.5 |
| Violas | 2.4-3.5 |
| Celli | 2.4-3.1 |
| Woodwinds | Oboe 1 6.1-10.5; Clarinet 2 8.2; Flute 1 4.6-7.2 |

- The patch files explain it: the short rows' sample groups release slowly after note-off.

| Row | Release |
|---|---|
| 2nd Violins "Stac RRx9" | 749 ms |
| Violas "Stac RRx9" | 489 ms |
| Celli "Stac RRx9" | 372 ms |
| 1st Violins "Staccatissimo RRx9" | 524 ms |

- With eighths 114 ms apart, each eighth still sounds under the next one. Violins II, with the longest release, separates least.
- `cap_release` in `tools/build_reaper.py` skips these groups. It caps only groups whose name ends in a dynamic word ("V2 Stac rrx1" has none), so adding "Stac RRx9" to `sus_release_cap_ms` does nothing now.

**Fix.**
- Add a generic option to `cap_release` (default off), e.g. `"any_dyn": true`, which caps every non-RT group of the listed rows.
- In `build/mix.json`, give Violins II `{"ms": 150, "rows": ["Stac RRx9"], "any_dyn": true}`, then the violas and celli.
- Range-test bars 104-120 against a same-start control. Accept if:
  - the dips reach 3 dB or more;
  - the master's 20 dB fall after a tutti cut-off does not shorten below about 0.25 s (Dan: not too dry);
  - the eighths' 60 ms peaks stay within 1 dB.
- Movement I (`mvt1` LEARNINGS c23) separated eighths on Sus MAX by cutting the note to 0.6 of its slot. The release cap is the equivalent for one-shot short rows (inferred).

### 5. Timpani coda: the printed crescendo of bars 335 into the ff roll is flat

**Where.** Timpani strokes 1002, 1003, 1003.5, 1004 (bar 335). The crescendo is marked at 1002, ff at 1005; f was marked at 996.

**Evidence (measured).**
- Velocity is 104 on all four strokes. Their peaks are -28.7 / -26.3 / -27.4 / -27.4 dB: no rise into the ff.
- The f strokes of bar 333 (996-998) are -28.3 / -26.4 / -27.4 / -30.1, about the same level.
- The ff accented strokes at 1008-1014 (v114) are -24.3..-26.3.
- c19's timpani stem matches c18's to within 0.1 dB on these strokes, and both are 2.5 dB under c17, as intended after the role row was deleted. The deletion left no crescendo inside the bar.

**Fix.** `VEL_SET["Timpani"]` in `build/score_config.py`: 1002 -> 100, 1003 -> 104, 1003.5 -> 108, 1004 -> 112. Velocity is the stroke's dynamic layer, so this is an instrument-side fix. Check that the four strokes rise monotonically by about 3 dB in total and stay under the 1008 accent.

### 6. Cor anglais hemiola notes 302 / 306 / 902 / 906: the start is on time, but the samples bloom and wobble

**Evidence (measured).**
- On the cor anglais' own harmonics, the note reaches -6 dB of its body at:
  - 306: -10 ms; 906: -10 ms; 304: +10; 308: +20; 310: +20 ms.
  - So the start is not late. The pc readings of +68 / +58 ms come from the shape of the note.
- The D sharp 5 at 306 / 906 sits 6-7 dB under its body for 125 ms, then swings: +3 dB at +175 ms, -4..-5 at +250 ms, +2..+4 at +375 ms.
- The A4 at 302 (accented, p) sits 9-12 dB under its body for 200 ms. This is the A4 bloom that `mockup-kit/LEARNINGS.md` section 6 records.
- CC1 is 93 there, which is fully on the vibrato layer.

**Fix (inferred).** A lead will not help: the start is already on the beat.
- Try CC1 45 (the non-vibrato layer) on 302 / 306 / 902 / 906 in `build/score_config.py`, back to the running value at the next note, to see whether the wobble belongs to the vibrato layer.
- The `_ACC_BY` cor anglais bump from finding 2 also lifts the first 0.15 s of these accented notes.
- Measure the swing (peak-to-trough from +100 to +400 ms) before and after.

## Other checks

- **Tutti downbeats (measured).** On the master, beat 1 over beats 2 and 3 (first 100 ms of each beat) is -0.2 / +0.3 dB median in bars 105-120 and +0.5 / +0.5 in 305-320. In the theme statements it is +3.2 / +2.2 (13-28) and +1.0 / +1.2 (253-268), so the tutti bars have no downbeat stress. METRIC_VEL gave only 0.5-1.2 dB in c16 and METRIC_DB is a per-note envelope (forbidden). The +6 cor anglais / Flute 1 bumps in finding 2 fall on downbeats in the tuttis and help a little. I propose nothing more.
- **The unrendered Clarinet 1 `dyn_trim_db` ff +1.2 -> -1.0.**
  - Right in direction for bar 334 (ff from 996; +3.0 dB over Violins I -> about +0.8).
  - Bar 214 has printed mf at 624, reached by hairpin, and bar 302 follows the sfp crescendo. The trim may not reach either one. Check which dynamic label those notes carry before counting on it for their +3.6 / +3.1.
  - This is a slow per-dynamic balance setting, allowed under Dan's rule.

## Do not touch

- Horn 1's "Sus MAX" G sharps with the 0.05 s lead (the hole at 1.6-3.4 dB); change only their CC1.
- The clarinets off the overlap and on "Leg Slur Rep", and the 0.6 s woodwind overlap minimum: the hemiola notes start within 20 ms.
- Keyswitch timing: none under 5 ms, none after its note.
- No chords on monophonic legato rows, and no stolen voices in the "non div." stops.
- The woodwinds' "Stac DblTng" rows: dips of 4.3-10.5 dB.
- The Violas' accent shape: +1.9 dB at 100-150 ms.
- REP_GAP_FLOOR_LONG_S.
- The Violins II trio +9.
- RTKiller and legato_speed_active on the legato rows.
