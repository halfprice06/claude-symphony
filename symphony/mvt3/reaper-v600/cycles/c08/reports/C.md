# Cycle 8, critic C (holistic comparison), on the c07 render

Lens: listen through the data as a conductor would. I compared c07 with the c00 port baseline, with c02 (five cycles back), with c05 (the last render on the Opus hall and the wetness ceiling), with Movement I's latest finished render on the same tools (symphony/mvt1/reaper-v621/cycles/c49, which still uses the pre-template mix), and with the Dvořák 9/i recording (the only reference audio on disk; Brahms numbers come from the stored metrics). All scripts ran on the c07 stems and masters against each cycle's `rendered_build/parts.json` tempo map (for c02, c03's map). Every number below is measured unless it is marked inferred.

## Manual notes (May 2021 HO manual, PDF p.10-11 and p.61-63: second reading of the c4 C row; cycles/c04/reports/C.md re-checked; MANUAL-GAPS.md read)

| Manual (PDF page) | What it says | Where it applies in the Finale | Does c07 follow it? |
|---|---|---|---|
| p.10-11 | The Opus Edition recorded new ensembles: 18 Violins, 2 Trumpets ("blazing at high velocities"), 2 Trombones ("warm, full, and extremely precise"), and 3 flutes, 3 clarinets and 3 bassoons. | a2 unisons. c07 `unison_dropped`: Horn 2 192 notes, Horn 4 111, Bassoon 2 76, Clarinet 2 52, Oboe 2 50, Trombone 2 50, Trumpet 2 35. | **No, unchanged since c04.** Each unison is still one solo player with +3 dB. The 2FH, 2TP and 2TB KS Masters are installed. HISTORY c04 left "Horns a2" open for memory reasons (pass 2). Not ranked here because memory blocks it. When a pass 2 runs, the horn a2 lines at 205-206, 247-254, 257-268 and 273-276 come first (192 Horn 2 notes). |
| p.61 | All seven libraries were recorded in EastWest Studio 1, as one large studio orchestra. | Every track. | **Partly.** The template returns use three different halls: S. Cal. Hall for strings and brass, San Francisco Hall 3.4 s for winds, and Northwest Hall 2.6 s for percussion and harp. All four are truncated by the same irSetup (endPos 0.5), so the tails are similar (inferred). Brief rule 3 asks for one room. Low priority while the decays meet the ceiling. |
| p.61 / p.135 | Moods (Classic, Soft, Epic) presets. | None. | n/a: the pipeline sets mics and returns itself. |
| p.62-63 | MAX patches have the most dynamic and vibrato layers; LITE patches have about half. | Every sustain and legato row. | Yes. c07 `art_counts` has no LITE row on any track. |
| p.63 | Every instrument fades to silence on CC11 (niente). | Fades into rests, morendo endings. | Yes in effect (CC11/CC1 plus the post-hall envelope). |
| p.63 | Finger position is on CC70. | The printed "sul G" spans: Vln I / Vla bar 169, Vln II bar 255. | No: every `cc70` lane is empty. Low gain, as in c04 (Movement I c38 found the change inaudible under slurs). Not ranked. |

MANUAL-GAPS items still open and relevant: #13 (bass trombone's low notes), #12 (recorded crescendo rolls), #7 (half-section divisi). None of them is among the largest audible problems now.

## Coordinator checks (answers first)

**Wetness ceiling (measured).** I wrote an independent cut-off detector: 7 or more tracks end within 0.12 s with nothing sounding for 0.55 s after, the stop is aligned to the steepest 50 ms fall, the reference level is the 0.25 s before the stop, and the times are to -10 / -20 dB.

| stop (s) | c05 -20 dB / drop at +0.3 s | c06 | c07 |
|---|---|---|---|
| 1.81 (bar 2) | 0.34 s / 18.7 dB | 0.56 / 13.6 | **0.48 / 12.1** |
| 7.5 (bar 6) | 0.31 / 19.7 | 0.56 / 12.5 | 0.33 / 18.9 |
| 36.4 | 0.22 / 23.5 | 0.48 / 11.1 | 0.36 / 18.4 |
| 244.6 | 0.27 / 21.7 | >3 / 13.2 | 0.33 / 18.6 |
| 299.1 | 0.38 / 18.0 | >3 / 13.6 | 0.39 / 18.0 |
| 421.7 (final) | 0.22 / 24.9 | 0.54 / 12.4 | 0.24 / 23.3 |
| median | 0.29 / 20.7 | – | **0.35 / 18.5** |

- c07 meets the numeric ceiling: every tutti stop reaches -20 dB within 0.50 s.
- The actor's other figures also reproduce:
  - RT60 estimate at the final stop is 1.22 s.
  - Late slope is 0.95 s.
  - Return minus dry energy is -12.5 dB.
- The actor's `decay07.py` gives a 0.52 s median only because its nominal times at qn 373 and 661 fall before the real stops: its drop at +0.3 s there is 4.5 and 2.2 dB.
- c07 is about 0.05 s and 2 dB wetter than c05, and at bar 2 clearly so (0.48 against 0.34 s).
- **Too dry or boxy?** c07 is already drier than the recordings at tutti stops:
  - -20 dB in 0.35 s, against Brahms 1/i 0.43-0.55 and Dvořák 0.50-0.58 s.
  - drop at +0.3 s of 18.5 dB, against 13-17 dB.
  - So it is not too dry by decay. Do not cut the returns further, and do not raise them either: the c05 rule binds.
- There is a slight boxiness. In the loudest 10 % of frames, the 250-500 Hz share is -5.5 dB, against c05 -6.9, Dvořák -6.8 and Movement I -6.6. It comes from the template EQ (finding 1), not from the hall.

**Brass accents, the 2-5 kHz jump (measured; the target should change).**
- On the c07 master, 98 brass accents give a jump p90 of 5.2 dB, as reported.
- But the jump compares the first 80 ms with the 200 ms before, so it counts entries and tutti downbeats. At the four largest jumps (qn 816, 104, 524, 72; +13.1 / +11.5 / +10.5 / +6.4 dB) brass is only -9.6 to -30.7 dB of the master's 2-5 kHz in the attack window. The burst comes from other sections.
- On the 71 accents where brass was already sounding, the jump p90 is **+0.4 dB**, under the +2 target.
- The accent's own front against its body (first 80 ms against 150-400 ms) is a median **-8.3 dB**, p90 -3.6 dB. There is no bright attack burst.
- EQ cannot move this metric. In simulation on the stems:
  - the 821 Hz bell -7.8 → -4 gives jump p90 5.4;
  - a 3.2 kHz -3 dB bell gives 4.6;
  - both together give 5.0.
- Recommendation: record in LEARNINGS that the target is met on sounding brass (p90 +0.4 dB, front minus body -8.3 dB median), and replace the check with "front minus body" or "jump on accents where brass already sounds". The brightness that is real is a whole-tutti problem: see finding 1.

**Movement I c50 template corrections (measured).**
- Timpani: no 84 Hz bell and no Surround mic (Close 0.2 / Main 0.5). Its share of the master's 30-150 Hz is 2-10 % in the rolls at bars 5, 147-150, 219-222, 231-238 and 261-262, and 18.5 % at 273-277. It is never the loudest stem: 7-11 dB under the top stem in 200 Hz-5 kHz. **Followed.**
- Harp high-pass at 80 Hz: **followed.**
- Winds -2.9 dB and crash -3.4 dB (c06 stem fix in gain_db): **followed.**
- Per-instrument brass make-up: soft_trim_db exists per track, but at pp it overshoots on the trombones (finding 5).

**Other standing checks.**
- Loop pulsing is absent. Autocorrelation at 3.95 s of the 100-300 Hz band level and of the centroid stays within ±0.24 on the master, the five string stems, Horn 1 and Trombone 1, in both the chorale (qn 888-936) and the end (qn 1080-1112). The kit's failure case was 0.39-0.63.

## Where the render stands against c00, c02, c05, Movement I and the recording

| | c00 | c02 | c05 | c07 | Mvt I c49 | Dvořák 9/i |
|---|---|---|---|---|---|---|
| centroid of the loudest 10 % of frames (Hz) | 1028 | 867 | 878 | **1009** | 882 | 812 (Brahms 818-870) |
| side/mid, 200 Hz-5 kHz (dB) | -5.6 | -7.3 | -6.9 | **-3.2** | -6.5 | -5.6 (refs -4.7..-5.6) |
| envelope modulation 2-16 Hz, louder half (dB) | -19.5 | -19.4 | -18.9 | -19.6 | -19.1 | **-17.2** |

**What has improved since c02:**
- decays and soft ends;
- repeat gaps;
- legato velocity and leads (string joins within ±20 ms);
- the phrase shapes;
- the loudness arc. Section levels relative to the median are within 1.7 dB of c02 everywhere, and 223 and 278 are still the loudest.

**What c06-c07 made worse.** The template mix took the tone colour and the stereo image away from both the recordings and Movement I:
- the tutti is now as bright as the c00 baseline;
- the image is wider than any reference.

**Weakest passages now, in order:**
1. Every brass-led tutti sounds bright and thin in the middle. The brightest sections: the arrival 223 (centroid 1288 Hz), O 211-222 (1181), T 271-279 (1126), J 135-150 (1008).
2. The subito at bar 219 is inaudible, and the sfp at bar 149 is weak.
3. The hammered eighths of the codas (199-210, 247-270) have no metric shape.
4. A pp trombone chord at bar 143 sits at the level of the f melody.

## Findings, ranked by what a listener would hear

### 1. The template EQ scooped the tutti at 500 Hz-1 kHz and lifted 2-8 kHz: the loud passages are brighter and thinner than any reference (measured; fix simulated)

**Where.** Every loud section, worst in the brass-led ones: 135-150, 211-234, 247-279.

**What is wrong.** Octave shares of the loudest 10 % of frames (dB re total):

| | 125-250 | 250-500 | 500-1k | 1-2k | 2-4k | 4-8k |
|---|---|---|---|---|---|---|
| c05 | -10.0 | -6.9 | -5.2 | -5.5 | -12.4 | -22.1 |
| c07 master | -9.9 | **-5.5** | **-7.7** | -5.7 | **-9.4** | **-18.3** |
| Mvt I c49 | -10.6 | -6.6 | -5.4 | -5.4 | -11.3 | -21.9 |
| Dvořák | -6.9 | -6.8 | -5.7 | -7.0 | -11.2 | -21.9 |

- Against c05, Movement I and the recording:
  - 500 Hz-1 kHz is 2.0-2.5 dB low;
  - 2-4 kHz is 1.8-3.0 dB high;
  - 4-8 kHz is 3.6 dB high.
- The same pattern appears in every one of the 20 score sections: c05 → c07, the 500-1k share falls 1.0-2.6 dB and the 2-8 kHz share rises 1.3-4.3 dB.
- The cause is the family EQ cuts at 447-475 Hz and 821-1005 Hz plus the remaining +2 to +2.55 dB shelves.
- With the delivery master_eq applied (the 6 kHz -3 dB shelf), the delivered loud frames are still 500-1k -7.4, 2-4k -9.3 and 4-8k -18.9.
- The Trumpet 1 solo (51-66), marked p dolce, also got brighter: section 2-8 kHz share -16.7 → -12.8 dB, centroid 807 → 868 Hz.

**Fix** (`build/mix.json`, `groups` → `family_eq`; Opus state is unchanged, so a mix-only write should be enough):
- `horn`, `trumpet`, `lowbrass`: change the 821 Hz bell from -7.8 to **-4.0** dB (bw 1.92), and add `{"type": "bell", "hz": 3200, "db": -4.0, "bw": 1.0}`.
- `string`: change the 1005 Hz bell from -5.0 to **-2.5** dB.
- `wind`: change the 1000 Hz bell from -3.1 to **-1.55** dB.

Simulated on the c07 stems with master_eq (delivered loud frames):

| | 500-1k | 2-4k | 4-8k | centroid |
|---|---|---|---|---|
| c07 | -7.4 | -9.3 | -18.9 | – |
| with the fix | -6.2 | -11.3 | -20.6 | down about 80 Hz |
| references | -5.2..-5.7 | -11.2..-12.4 | -21.9..-22.1 | – |

Balance cost (A-weighted), to remove in `gain_db` so finding 1 changes colour and not balance:
- horns +1.7..+2.0 dB. Keep +0.8 of it: the horns are 4.4-4.5 dB under the heavy brass.
- trumpets +0.8 (Trumpet 3 +1.6);
- trombones +1.0;
- tuba +1.7;
- strings +0.3..+0.8;
- winds +0.5..+1.1.

If 4-8 kHz is still more than 1 dB over -21.9 after the render, set the brass and string shelves (+2.0) to 0 before touching master_eq. Check with the loud-frame octave shares above.

### 2. The tutti image is wider than any recording, and its bass is out of phase: L/R correlation at 125-250 Hz is -0.03 (measured; fix simulated)

**Where.** The whole piece, most in loud passages.

**What is wrong.**
- L/R correlation of the loudest 10 % of frames, per octave from 30 Hz to 8 kHz:
  - c07: 0.23, 0.49, **-0.03**, 0.42, 0.35, 0.35, 0.26, 0.32
  - Dvořák: 0.46, 0.67, 0.54, 0.55, 0.57, 0.60, 0.70, 0.47
  - c05: 0.52-0.80
- Side/mid is -3.2 dB, against -4.7..-5.6 in the references and -6.9 in c05.
- Per stem at 125-250 Hz in loud frames:
  - celli -0.05 and basses -0.37: together they carry most of the master's 60-250 Hz;
  - tuba -0.01;
  - R Brass -0.56, R Strings +0.14;
  - the trumpets go to -0.37 at 250-500 Hz.
- This is the full-width Main pair of `pan_by_mic`. Movement I c49 measured the same effect and concluded "copy it only partly" (mvt1 LEARNINGS, "EastWest's template setup").
- On top of this, 22 tracks still carry the c21-era side high shelf at 250 Hz, +1.5 dB, which widens further.
- A bass with near-zero or negative correlation sounds hollow and unanchored on speakers and loses level in mono (inferred from the numbers).

**Fix** (`build/mix.json` track `side_shelf`, list form, existing code in `build_reaper.py set_side_shelf`; mix-only):
1. Remove the `{"band": "highshelf", "hz": 250, "db": 1.5}` side shelf from all 22 tracks that have it (winds, horns, trumpets, trombones).
2. Give Violoncellos, Double basses, Tuba, Bass trombone, Trombones 1-2, Contrabassoon, Timpani and the four returns (`returns` entries take a side shelf too: `r.ss` in returns_job) `"side_shelf": [{"band": "lowshelf", "hz": 400, "db": -8}]`.

Simulated (first-order shelves on the c07 stems):

| | correlation per octave, 30 Hz-8 kHz | side/mid |
|---|---|---|
| with the fix | 0.84, 0.86, 0.56, 0.56, 0.47, 0.47, 0.37, 0.42 | -4.6 dB |

ReaEQ's shelf is steeper than the model, so check on the render. Targets:
- 125-250 Hz correlation 0.45-0.60;
- side/mid -4.7..-5.6 dB;
- no octave below 125 Hz over 0.85 (if it is, use -6 dB).

Seats should hold, since the shelf acts only on the side channel below 400 Hz (Close carries the seat). Check Vln I and Cb R-L against c07.

### 3. The subito p at bar 219 cannot be heard, and the sfp at bar 149 has a late, weak sf (measured)

**Where.** qn 872 (bar 219, "sub. p" in the winds, horns 1-2, trumpets, timpani and violins; p elsewhere) and qn 592 (bar 149, sfp on 26 tracks). Brief S3 names both.

**What is wrong at 872.**
- The master does not change: -33.3 dB in the second before, -33.5 dB at +0.4..+1.2 s.
- Winds go from -43.0 at qn 870 to -38.4 at 871-872. Strings go from -41.2 to -38.5 / -36.4. Brass falls only 5.7 dB from its crescendo peak.
- The CC lanes do drop (Vln I CC11 78 → 56, Fl 1 66 → 43, Cl 1 CC1 59 → 36). The post-hall volume envelope takes the drop back. Twelve tracks step **up** at the mark:
  - Clarinet 1 and Oboe 1 +6 dB;
  - Flute 2, Oboe 2, Violins I, Bassoon 2, contrabassoon, celli and basses +3 dB;
  - timpani +10.7 dB.
- The step is `HELD_DECRESC_DB` (wind 3, string 3; score_to_parts.py near line 4962). The decrescendos at 860-864 and 864-868 lie inside held notes. They put -3 then -6 dB into the envelope and hold it "to the next moved onset (then back to 0)", and that onset is the subito.
- The same rule produces positive steps at the p marks of qn 353 (Horn 1 +5.6) and qn 384 (Violins II +8.4). Check those too.

**What is wrong at 592.** Master per 0.25 qn (about 0.09 s):

| qn | 591 | 591.75 | 592 | 592.5 | 593-593.5 |
|---|---|---|---|---|---|
| master (dB) | -18.5 | -22.7 | **-25.5** | -20.4 | -25.8..-26.4 |
| strings (dB) | -23.1 | – | -30.3 | – | -34.1 |

- So the sf arrives about 0.18 s after the beat and peaks 1.9 dB **under** the preceding ff.
- The p sits only 5.4-6.0 dB under that peak (c02 target: 10 dB).
- The timpani roll never drops: -34.2 dB on the beat, -37.4 / -35.8 at +0.5 / +1.0 qn, against -37.9 dB in the ff before.

**Fix.**
1. Add a generic option to `tools/score_to_parts.py`, `HELD_DECRESC_CARRY = True` (default off).
   - A held-decrescendo level does not return to 0 at a next onset whose printed dynamic is "sub.", fp, sfp, or not louder than the dynamic at the hairpin's end.
   - Instead it is held to the start of the next crescendo hairpin and ramps to 0 across it. Here: held 872-876, released over the cresc 876-880, under the existing `hpgain` 2.5 / 4.0.
   - Turn it on in `build/score_config.py`.
   - Target: master at qn 872-874 at least 5 dB under qn 869-871. Winds and strings must not rise at 872.
2. Timpani at 832 and 872: the +11.2 and +10.7 dB steps are the roll trims answering a CC drop (88 → 65 / 60). Cap the timpani's post-mark envelope step at the fp / sub. so the roll sits at least 6 dB under its pre-mark level for 0.5 s.
3. qn 592:
   - Raise the sf: `SFP_SPIKE_S` (0.12, 0.30) → (0.15, 0.35), `SFP_VEL` 96 → 110.
   - Give the sfp notes on the string Sus rows an extra lead of 0.06 s (via `entry_leads.json` at sq 592) so the sf lands on the beat.
   - Fit the timpani's 592 roll to fall 10 dB in 0.3 s.
   - Targets: the master sf peak within 0.08 s of the beat and at least 1 dB over the preceding ff; the p at least 10 dB under the peak.
   - All falls go in CC11/CC1, never as a volume-envelope drop (S3).

### 4. The hammered eighths have no metric shape: every eighth is the same velocity and nearly the same level (measured; batch 7 not yet adopted)

**Where.** Basses, celli and violas: qn 792-840 (bars 199-210) and 984-1080 (bars 247-270), about 60 s of the piece's two fastest tuttis.

**What is wrong.**
- Basses' velocity by beat position (0, 0.5, 1.0, 1.5 qn in each half note):
  - 87 / 87 / 87 / 88 at 792-840 (88 notes; the first 32 are all 91);
  - 90 / 91 / 91 / 91 at 984-1080 (176 notes).
- Stem level over each eighth's first 120 ms, re the median, by position: +1.0 / -0.2 / +0.4 / -0.3 dB and +0.6 / -0.1 / -0.2 / -0.1 dB.
- The variation that does exist (SD 3.4-4.9 dB) is round-robin scatter, not metre. `METRIC_BOWED_DB` is down 1.0 / mid 0.5 / beat 0 / off -0.5, so it is realised almost one-to-one, but it is too small.
- Research batch 7 (FINDINGS §23) asks for 15-25 velocity steps between the strongest and weakest notes, plus ±5-7 seeded variation.
- The whole render's envelope modulation at 2-16 Hz is -19.6 dB against the recording's -17.2 dB. It has not moved since c00 (-19.5), so the articulation still has less pulse than a real orchestra. These passages are where that is heard most (inferred).

**Fix** (`build/score_config.py`; generic code in score_to_parts.py):
1. `METRIC_BOWED_DB` = {"down": 2.0, "mid": 1.0, "beat": 0.0, "off": -1.5} on the existing spans (Violas, Violoncellos, Double basses at 792-816 and 984-1080). Extend the spans to 816-840, which are hammered as well.
2. Add `METRIC_BOWED_VEL` (generic, default off): velocity offsets {"down": +12, "mid": +6, "beat": 0, "off": -8} around the CC-derived velocity, with seeded ±5 jitter, on the same notes.
   - Movement I c16's `METRIC_VEL` failed on pizzicato (scatter rose), so judge this one on the stems.
   - Targets: downbeat minus off-beat 2.5-3.5 dB on the Cb stem (now 1.3 / 0.7 dB), with per-position SD no larger than c07's.
   - Measure the master's 2-16 Hz modulation over 984-1080 against c07.
3. Do not shorten these notes to the batch-7 spiccato length (50-62 %). They are unmarked ff eighths played détaché, and the detach dips (median 12.7 dB) already separate them.

### 5. Soft trombones are trimmed up to the level of the f melody: pp at bar 143 sits 1 dB under Horn 1's f (measured; c50 B #2's per-dynamic make-up)

**Where.** qn 568-576 (bar 143): Trombones 1-2 and bass trombone hold a pp D4 under Vln I and Horn 1, which play f.

**What is wrong.**
- In 200 Hz-5 kHz:
  - Trombone 1 is +1.8 dB over Violins I and -1.0 dB under Horn 1;
  - Trombone 2 is -3.9 dB and the bass trombone -5.7 dB under Horn 1.
- A pp chord under an f melody should sit about 10 dB lower, and a trombone at f is about +3 dB over a horn (Rimsky-Korsakov's ratio, kit LEARNINGS §13).
- `soft_trim_db` on the trombones is pp 16.6 / 16.2 / 15.1 dB, on top of the c06 +4.2 dB family make-up.
- The stems' median levels by printed dynamic show the result:
  - Trombone 1: pp -43.4, p -43.2, mf -42.2 (pp to mf 1.2 dB);
  - Trombone 2: pp -43.0 against mf -45.5 (inverted);
  - bass trombone: pp -47.1, mf -47.6;
  - by comparison, violas span 16 dB from pp to mf.
- The other soft trombone spots are within reason: p at qn 932 is 2-3.4 dB under the mf celli, p at 872 is 2-3 dB under.

**Fix** (`build/mix.json` tracks):
- Trombone 1, Trombone 2 and Bass trombone `soft_trim_db.pp` 16.6 / 16.2 / 15.1 → **8.0** (ppp the same).
- Leave p and mf as they are.
- Target: at 568-576, the trombones 8-10 dB under Horn 1 and 5-7 dB under Violins I.
- Then re-check the horns' pp trims (13-14 dB): at 264-300, Horn 1 at pp is -3.1 dB under the mf Violins I. A pp accompaniment should be about 6 dB under, so take about 3 dB off Horn 1's pp trim.

## Do not touch

- The return envelope (irSetup 2 / 0.5 / 0.5), the register sends and the return faders. Tutti stops reach -20 dB in 0.24-0.48 s, already drier than the recordings. Do not lower them to fix brightness: that is EQ (finding 1).
- The per-dynamic string release caps.
- Legato velocity by dynamic with its leads (string joins within ±20 ms).
- The repeat gaps (low-brass dips 7.9 / 12.2 dB).
- The timpani's reduced EQ, no Surround mic, and roll levels: never the loudest stem.
- Harp HPF 80 Hz.
- The c06 wind and crash make-ups.
- The phrase shapes and the CAESURA/PHRASE_ARCS tempo map.
- The re-bow layout: no loop pulsing in 223-234 or 271-279.
- Climax order: 278 and 223 are the loudest bars.
- The delivery ride ratio 2.0.
