# Critic C, cycle 47: holistic comparison (render c46, score v621)

Render under review: c46 as delivered (`cycles/c46/render`, 40 stems, master = float stem sum; Violins I / II / Violas are the 350 ms pass-2 test stems, celli / basses spliced from the final chord; `render_first/` = the same notes at 150 ms). Data: `build/parts.json` (describes the delivered stems; REAPER was not rebuilt). Compared with cycle 0 (`cycles/c00/mvt1-mockup-c00.mp3`; v221, no stems), with c41 (five cycles back, the old hall: fx 0.19, full IR, no string caps), with c43 / c44 where a single change needed isolating, and with the reference recordings: the Dvořák 9/i MP3 (audio) and the stored rtk metrics of Brahms 1/i, 4/i, 1/ii and 4/ii (`symphony/render/critics/c00`, `c04`; the Brahms audio is not on this machine). Every reference comparison below uses the same code on both sides: rtk's own `cutoff_decays` / `decay_fit` (copied without scipy) for tails, and one STFT script for modulation, onsets, band shares and stereo. My scripts were in `/private/tmp/claude-501/mockup-loop/mvt1-c47-C/` (deleted at the end, as the brief asks).

## Manual notes (second reading of the c41 slot C row: 2021 manual PDF pp. 44-45 and 134-136, read again in full; MANUAL-GAPS.md and DIGEST.md read)

Open MANUAL-GAPS items first: #1 brass Marc Sus LITE accents (never tried; finding 2), #4 Mid mics on winds (never tried), #5 expressive wind rows, #7 half-section divisi, #9 horn portato rows, #12 Felt Cresc rolls (deferred in c46), #13 bass-trombone low notes. #3 (Solo Cello) is not installed.

| Manual (PDF page) | What it says | Where it applies | Followed now? (first reading in c41 -> c46) |
|---|---|---|---|
| p.44 | MIDI channel modes (Multi, MPE, Omni, 1-16); pan knob = Play-page pan = mixer pan | one instrument per Opus instance, CC lanes on the track's channel | Yes, unchanged (read in parts.json / build_reaper). |
| p.45 | CC1 commonly crossfades dynamic and/or vibrato layers; CC11 sets volume, or the dynamics when CC1 holds vibrato; keyswitches outside the sampled range | CC1_DYN_TRACKS (brass, clarinet), CC11 = printed line, balance in the volume envelope | Yes. c46 A found no keyswitch closer than 9.5 ms to its note and no chord on a legato row (measured in parts.json). |
| p.134 | Purge pill: green = preloaded, yellow = streaming as notes play | 1x offline render from the USB drive | Yes: probe 0 late, no silent notes beyond the two known false alarms; main project 44 GB settled (c46 CHANGES). |
| p.135 | Player window: Mood, Performance, Envelope, Stereo Double, Reverb, mic channels | releases, mics, widths, hall set by the pipeline | Now more fully followed than in c41: the Envelope's release is set per dynamic (150 ms mf-ff / 350 ms pp-p) and per-mic width replaced the Stereo Double option the first reading rejected (`width_by_mic`, c45). Stereo Double still unused (right). |
| p.136 | Moods: Classic = Main mix, hall "3.4 second decay"; Soft = Mid + Surround for "slower, more emotional passages", "definition and depth"; Epic = Close + Main + Surround, 2.8 s. Moods also set the MIDI compressor | no mood applied; Close + Main per group, one shared hall | Partly. New on this reading: the mockup now departs on purpose from Classic's 3.4 s hall (late RT 1.81 s, c46); the recordings support that (1.3-1.6 s rtk RT, see finding 4). Still not followed: the Soft mood's Mid mics for the espr./dolce wind solos (MANUAL-GAPS #4). The MIDI compressor is irrelevant here (velocity matters only on legato / short rows). |

## Where the movement stands (c00 -> c41 -> c46, measured; reference comparisons inferred where the piece differs)

| Measure (same code for every file) | c00 mp3 | c41 mp3 | c46 mp3 | Dvořák 9/i |
|---|---|---|---|---|
| 3-10 Hz modulation of band envelopes, loud 2 s windows (dB SD), 60-200 / 200-500 / 500-1k / 1-2k / 2-5k Hz | 0.98 / 0.75 / 0.73 / 0.84 / 0.72 | 1.17 / 0.85 / 0.86 / 0.93 / 0.71 | 1.27 / 0.94 / 0.94 / 0.92 / 0.72 | 1.35 / 0.91 / 1.11 / 0.91 / 0.92 |
| Same, mid-level windows | 1.11 / 1.04 / 1.08 / 0.88 / 0.68 | 1.03 / 1.17 / 1.13 / 0.93 / 0.74 | 1.23 / 1.13 / 1.16 / 0.97 / 0.76 | 1.44 / 1.20 / 1.33 / 1.18 / 1.06 |
| Salient onsets per active second (log spectral flux) | 0.22 | 0.37 | 0.40 | 0.71 |
| Band shares, loud frames, 100-200 / 2-6k / 6-20k Hz (dB) | -11.1 / -11.4 / -28.8 | -9.5 / -11.4 / -31.0 | -10.0 / -11.2 / -30.5 | -6.6 / -11.2 / -27.8 |
| Side/mid (dB) | -5.0 | -5.6 | -6.2 | -5.3 |

- **Large-scale shape (measured).** Per-bar master levels: c46 minus c41 median -0.7 dB (the hall cut), c46 minus c00 -0.2 dB. Only bar 84 moved more than 3 dB (-7.0: the bar-83 ff chord's hall no longer fills the beat of rest before the sub. p). The dynamic plan is still c00's.
- **What the drier room bought (measured).** Loud low and low-mid definition rose from c41 to c46 (60-200 Hz +0.10, 200-500 +0.09, 500-1k +0.08; mid-level 60-200 +0.20) and now sits at or near the recording in 60-500 Hz.
- **What 46 cycles never moved (measured).** 2-5 kHz modulation: 0.72 in c00, 0.71 in c41, 0.72 in c46, against 0.92 (loud) / 1.06 (mid) in the recording. Mid-level 500 Hz-2 kHz is also 13-18% under. Salient onsets are 57% of the recording's. This is the remaining "mush": attacks without edge, not reverb (findings 2-3).
- **Weakest passages now (measured, by section modulation and onset rate in the c46 mp3).**
  1. Letter G and the stringendo, bars 111-122 (qn 440-488): the lowest 200-500 Hz modulation of any loud section (bars 117-130: 0.84), 2-5 kHz 0.80, 0.21 onsets/s. The violas' and clarinets' triplets are the rhythm here, and the violas' note-rate pulse is weaker than five cycles back (finding 3).
  2. The climax, bars 160-166: 60-200 Hz 0.90 (lowest loud value), 2-5 kHz 0.70, 0.23 onsets/s; the fff is loud but has no attack profile.
  3. The recapitulation's second theme, bars 147-159: 1-2 kHz 0.78, 2-5 kHz 0.67, the lowest of all sections. Dolce, so part of this is right; the rest is the dull attack of every note.
  4. The coda's soft close, bars 171-182: 2-5 kHz 0.72, and the final chord stops too fast (finding 1).
- **What still sounds like a machine (ranked).** (1) Every accent and re-attack is a level change with the plain note's dull front (finding 2). (2) Soft endings and the final chord stop faster than any reference (finding 1). (3) Running string figures and tutti repeated notes do not articulate in the master (finding 3). (4) Tutti cut-offs fall a little faster in their first 0.3 s than a hall (finding 4).
- **Also measured, no finding.** Loud frames have 3.4 dB less 100-200 Hz than the Dvořák and, unlike every recording, less low-mid than soft frames (loud minus soft -1.3 dB; Dvořák +3.3); the top octave is 2.7 dB darker. The image narrowed since c41 (side/mid -5.6 -> -6.2 dB). These belong to the c49 Blend critic.

## Coordinator's questions (measured)

- **2:43 glitch.** 2:43 is bar 62 beat 4 (the sub. p at qn 244 = 161.18 s). c46 master relative to the 0.35-0.05 s before the mark, over 0-0.05 / 0.05-0.1 / 0.1-0.2 / 0.2-0.3 / 0.3-0.5 s: -1.8 / -5.6 / -9.2 / -12.5 / -14.0 dB; the 679 tutti fermata release in the same render -3.0 / -6.3 / -11.4 / -16.7 / -22.2. The mp3 is the same within 0.2 dB (the ride adds no dip). Largest 50 ms frame after 0.1 s: -8.5 dB (no blip over the forte). Bar 62 now decays more slowly than a tutti release. **It stays fixed.**
- **Too dry or still mushy?** Neither, by the references; the room sits slightly on the dry side in the first 0.3 s and is right after that (finding 4). The mush that remains is attack definition (findings 2-3).
- **pp/p cap: 500 ms or none?** No cap at pp; keep 350 ms at p (finding 1).

## Findings, ranked by what a listener would gain

### 1. The final chord and the pp chorale ends still stop in a third of a recording's time: take the cap off the pp groups (no cap), keep 350 ms at p and 150 ms at mf-ff (measured; prediction from a two-cap fit, inferred)

**Where.** The last sound of the movement (qn 728, all five string sections, ppp morendo, attacca); the pp chord ends of the Lento (bars 6-14), the second theme's pp accompaniment (violas / basses bars 42-54) and the coda (175-182).

**What is wrong.** The ppp chord plays on the Sus MAX "pp" groups, which the patches ship at 931 ms (read: `1V pp`, `V2 pp`, `Va pp`, `Vc pp`, `Db pp` all 931 ms; the 430 ms groups in the c46 log are the Sus Marc LITE row; `p` groups ship 524-700 ms). The 350 ms cap removes almost two thirds of that release, and the hall now carries too little to make up for it.

**Evidence (measured, per stem relative to the 0.3 s before its own note-off; master at 728).**

| Final note-off | t to -10 / -20 dB (s) | drop at 0.05-0.1 s |
|---|---|---|
| c41 master (no cap, old hall) | 0.41 / 0.65 | -3.3 |
| c46 master, 150 ms (render_first) | 0.08 / 0.34 | -9.9 |
| c46 master, 350 ms (delivered) | 0.13 / 0.34 | -6.8 |
| References, soft endings (rtk final tails) | Brahms 1/ii 0.40 / 0.79, Brahms 4/ii 0.20 / 0.48 | |
| References, loud endings | Brahms 4/i 0.24 / 0.46, Dvořák 0.31 / 0.61 | |

- The 150 -> 350 step moved -10 dB from 0.08 to 0.13 s and left -20 dB at 0.34 s: past 0.3 s the tail is the hall, and the cap has to reach further than that before -20 dB moves.
- **Prediction (inferred).** Each string stem's tail fitted as hall + release, P_R(t) = H(t) + D·(1 - t/R)^2k, on the c46 150 / 350 pair (fit error 0.4-1.9 dB; k 1-2), then summed with each stem's share of the master just before 728 (basses 45%, violas 27%, celli 12%, Violins II 11%, Violins I 4%):

| pp release | master t to -10 / -20 / -30 dB (s) |
|---|---|
| 350 ms (fit check; measured 0.13 / 0.34 / 0.52) | 0.14 / 0.28 / 0.52 |
| 500 ms | 0.19 / 0.36 / 0.52 |
| 700 ms | 0.25 / 0.48 / 0.69 |
| 931 ms (no cap) | 0.33 / 0.63 / 0.82 |

  The fit reads -20 dB about 0.06 s early at 350 ms, so the no-cap value is about 0.33 / 0.63-0.69 s.
- **500 ms is not enough:** -20 dB at about 0.36 s is short of every reference (0.46-0.79). No cap lands inside the soft-ending range at both points (0.20-0.40 / 0.48-0.79), close to c41's 0.41 / 0.65 without c41's wet hall.

**Risk (measured count, effect inferred).** 117 string Sus MAX notes end at a pp CC11 (40 or less) with another note of the same track within 0.25 s (Violins I 4, Violins II 27, Violas 32, celli 19, basses 35; bars 4-13, 42-54, 72-75, 107-109, 144-145, 173-182). Many are same-pitch re-bow pieces (a longer release fills those dips: good); the rest are pp chord changes, where a 931 ms release puts the old pitch under the new one. The same patches' legato rows already overlap 0.27-0.39 s at -10 dB (c44 C), so the test should hold the chord changes to that.

**Fix.**
1. `build/mix.json`, Violins I, Violins II, Violas, Violoncellos, Double basses and both f62 aliases: `"sus_release_cap_ms": [{"ms": 150, "dyn": ["mf", "f", "ff"], "rows": ["Sus MAX", "Sus Marc LITE"]}, {"ms": 350, "dyn": ["p"], "rows": ["Sus MAX", "Sus Marc LITE"]}]` (the pp entry removed; nothing else in `build_reaper.py` changes).
2. As the c46 do-not-touch rule asks, test first in pass 2: five `TEST_TRACKS` aliases ("<section> ppcap test") over each section's own windows (`tw_own`) on qn 16-56, 168-220 and 680-728, `alias_check.py` OK apart from `sus_release_cap_ms`. A second variant at 700 ms is the fallback.
3. Pass if: master final release -10 dB at 0.20 s or later and -20 dB at 0.48 s or later (after the swap); at the pp chord changes (violas / basses bars 47-54, Lento bars 6-13, coda 175-181) the old pitch is down 10 dB within 0.35 s of the new moved onset (pcx exclusion bands); re-bow steps of 3 dB or more no more than c46's; mf-ff and p ends unchanged. Use 700 ms if no-cap fails only the chord-change test.
4. Then refit the final chord's re-bow fills (c44 rule); c46 measured that a longer soft release makes re-bow dips shallower, so expect cuts, not lifts.

### 2. Accents and attacks have no edge: 2-5 kHz definition is the one measure 46 cycles never moved; try the brass marcato row (MANUAL-GAPS #1) in pass 2 now (measured problem; fix inferred, to be tested)

**Where.** All 200 brass accents (bars 23-26, 32-33, 41, 69-72, 80-83, 131-138, 142-143, 167-170), and through them the tutti climaxes; the same applies to the 663 printed accents of every family.

**What is wrong.** Every accent is a 2-4 dB volume swell on the plain sustain's dull front, so a conductor hears louder notes, not accented ones. The tutti arrivals and the fff have weight but no attack profile.

**Evidence (measured).**
- 2-5 kHz modulation, loud / mid windows: c00 0.72 / 0.68, c41 0.71 / 0.74, c46 0.72 / 0.76; Dvořák 0.92 / 1.06. The climax (160-166) and the recapitulation's second theme are lowest (0.70 / 0.67).
- Brass accents' 2-5 kHz in the first 80 ms minus body: median -16.4 dB, p90 -8.1 (c46 A on c45; c41 -13.9). The real-orchestra value recorded in `build/score_config.py` (line 575) is -4.2 dB; MANUAL-GAPS #1 sets -6..-2 dB with a ceiling of +3. The master's 2-5 kHz jump at accents is -2.5 dB median: accented notes start darker than the texture.
- Salient onsets 0.40 per s against 0.71 in the recording.

**Manual.** p.101: the Sustain Marcato row ("Marc Sus LITE") has a marcato attack "not as forceful" as Sustain Accent, and velocity sets a low-pass filter on the attack, so a moderate velocity gives a controlled, darker front. p.106: Legato Slur Accent MAX (velocity = accent strength) for accents inside slurs. p.62-63: LITE rows have about half the layers. The row is installed and unloaded in the 1FH, 2FH, 1TP, 1TB and 1TU KS Masters (MANUAL-GAPS #1, read).

**Fix (pass 2, main project untouched).**
1. Test aliases (`TEST_TRACKS`, alias_check OK apart from the art) on Trombone 1, Trombone 2, Bass trombone, Horns a2 and Horn 3 / Horn 4 over bars 32-33 (qn 124-132) and 142-143 (564-572): `ART_SPANS` with art "Marc Sus LITE" on the accented notes, velocity from the printed dynamic mapped into 45-75 (filter mostly closed), CC1 from `CC1_DYN_MAP`, the `GENTLE_ACCENT` swell cut to about +1 dB (the sample now supplies the front), no CC11 bump.
2. Measure against the main stems on the same notes: 2-5 kHz first 80 ms minus body (target -6..-2 dB, never over +3); the master's 2-5 kHz jump (under +3 dB); level over same-dynamic neighbours 2-4 dB (`fit_accents.py`); attack-peak time (pcX).
3. If it passes, extend family by family (trumpets on 1TP's row next; Leg Slur Accent MAX for slurred accents), refit `accent_fits.json`, and check Dan's item 8 (no 2-5 kHz burst 7-13 dB over the body).

### 3. Shorter tails cleared the pitch overlap but did not articulate the running figures and tutti repeats: the articulation has to come from the stroke row; make the deferred tools change and run the string row A/B (measured; fix to be tested)

**Where.** The violas' (and clarinets') triplets at letter G, bars 117-120 (qn 464-480), and the stringendo, bars 111-116; the basses' ff eighth pedals in bars 27-32, 131-134, 139-142 and 167-169; the celli's sixteenths in bars 127-130.

**What is wrong.** These figures are the rhythm under the tunes, and in the master they read as held chords or a drone. Each cycle since c44 shortened the strings' tails (150 ms cap, Violas trail -6 dB). That reduced the old pitch under the new one, but it did not give the notes attacks, and at letter G the note-rate pulse got weaker.

**Evidence (measured).**
- **Letter G.** Violas data identical in c41-c46 (notes, Sus MAX short strokes, CC11 88, envelope). Note-rate (6.3 Hz) peak of the 250-1200 Hz envelope over its 3-12 Hz median:
  - Violas stem: c43 7.2, c44 5.5 (cap + hall), c45 main 5.5, c46 4.5 dB (trail -6).
  - Master: c41 8.9 / c43 7.6 -> c46 6.3 dB.
  - In the same render Clarinet 2 reaches 13.7 dB.
  - Inferred: the patch's release trails (shipped at +12 dB on the violas' mf groups) had carried part of each stroke's audible pulse.
- **Bars 97-102.** The violas' eighths pulse at 14.2 dB on the stem but 5.8 dB in the master.
- **S1 in the master** (c46 A on c45, string data unchanged since): strings Sus -> Sus repeats dip 4.2 dB on the stem and 1.6 dB in the master. Basses' pedals stem / master: 4.0 / 2.0, 4.9 / 1.4, 4.0 / 3.2, 7.1 / 3.4 dB. A simulated extra -4 dB dip moved the master only +0.2 dB (A). Level dips cannot separate these notes in a tutti; an attack can.
- Re-attacks raise 2-5 kHz only +0.4-1.1 dB over the 80 ms before (c41 C, same rows).

**Fix.**
1. **Tools (c46 CHANGES "Rejected", A #2).** In `tools/score_to_parts.py`, `STR_REP_NEW_BOW` (and the stroke paths `STR_SHORT_AFTER_SUS` / `REP_SPLIT`) must keep an `ART_SPANS` row when that row is listed in `STR_STROKE_ROWS`, and the next note keeps its own row.
2. **Pass-2 A/B with matched test aliases.**
   - "Sus Marc LITE" (velocity 60-80) against Sus MAX: basses on bars 27-32 and 131-134; celli on bars 127-130.
   - "Stac RRx9" against "Sus Marc LITE": violas' triplets over bars 111-120 (qn 440-480).
3. **Pass criteria.**
   - Master boundary dip of 3 dB or more on the basses' pedals.
   - Violas' note-rate peak at least c43's 7.2 dB on the stem and 7.6 in the master.
   - 2-5 kHz front minus body -6..-2 dB.
   - Old pitch at +70 ms no higher than c46's -8.4 dB.
   - Bar levels within 1 dB.
4. **Do not cut string releases or trails further.** Their measured effect on articulation is now negative.

### 4. The hall is not the mush any more; it is slightly dry in the first 0.3 s and right after that: leave it for Dan's next listen (measured; fallback inferred)

**Where.** Every tutti cut-off (bars 14, 26, 72, 138, the 679 fermata) and rests after loud chords (bar 83 -> 84).

**Evidence (measured, rtk's own detector on renders and recordings).**

| | n | t to -20 dB (s) | RT from the -5..-20 dB slope (s) | drop at 0.3 s from the -2 dB point (dB) |
|---|---|---|---|---|
| c41 master (fx 0.19, full IR) | 1 | 0.62 | 2.62 | -18.3 |
| c44 master | 4 | 0.45-0.55 (med 0.49) | 0.85-1.70 (1.06) | -17.6..-20.8 |
| c46 master | 5 | 0.43-0.53 (0.46; 72's 1.14 is a held note) | 0.87-1.13 (1.03) | -17.0..-22.3 (-19.7) |
| Brahms 1/i (stored rtk, 12 cut-offs) | 12 | 0.43-0.55 (0.485) | 1.13-1.62 (1.33) | (13-17 per c05 / c17) |
| Dvořák 9/i | 1 | 0.49 | 1.32 | -16.0 |

- The time to -20 dB sits at the references' fast end. Between -5 and -20 dB, though, c46 falls about 25% faster than both recordings (1.03 against 1.32-1.33 s), and 3-4 dB further by 0.3 s than the Dvořák.
- The fermata's late RT is 1.81 s (c46 CHANGES), inside the 1.5-2 s target.
- Fermata 679 profile over 0.3-0.5 / 0.5-0.8 / 0.8-1.2 s: c41 -15.9 / -21.2 / -30.1, c46 -22.2 / -30.3 / -42.2 dB.
- Bar 83's cut-off before the sub. p falls -19.3 dB by 0.3-0.5 s (c41 -12.9), so the beat of rest is now an audible gap. That gap is written in the score.
- Definition in 60-500 Hz rose to the recording's (table above). The remaining deficit is at 500 Hz-5 kHz, where the hall is not the cause.

**Recommendation.**
- No hall change in c47. Dan's last note ("too wet") was made against c42, whose drop at 0.3 s was 13-14 dB. c46 is 5-6 dB drier than that and has not been heard.
- Do not raise sends (brief S4).
- **Prepared fallback if Dan calls c47 dry or clipped:** `reverb.fx_volume` 0.095 -> 0.12 (+2 dB on the hall return; envelope, low cut and sends unchanged; full rebuild of both passes). Predicted drop at 0.3 s: about 17.7 dB, still clear of the 13 dB floor. Predicted -5..-20 dB slope about 1.1-1.2 s (inferred).

## Standing checks (BRIEF 5-9, S1-S3)

- **S3 / 2:43.** Fixed (see "Coordinator's questions").
- **S1.** See finding 3. Winds 5-15 dB on the stems and brass 3.8-9.8 dB (c46 A); strings separate on the stems but not in the master.
- **S2.** Probe legato robust SD 51 / 42 / 52 / 50 ms (c46); family medians +11..+17 ms. Strokes are still the late class: median +44 ms, 8 of 15 over 60 ms (A). Finding 3's row test addresses their start too.
- **7. Loop pulse.** Final chord 0.06 / -0.02 and Lento 0.04 / -0.09 at 3.95 s (A, c45). The data and the hall are unchanged in c46. After finding 1, re-check the final chord: longer releases overlap the re-bows.
- **8. Accents.** Dark fronts, no bite (finding 2 is the opposite problem).
- **Timpani rolls (Dan's priority).** c46 lowered bar 174 (+11 -> +7 dB over the bassoons' G2 in 78-196 Hz) and bars 13-14 (-3 dB). The crescendo rolls now grow +3.1 to +4.8 dB. No roll measured here covers a part outside its printed crescendos; not re-measured beyond c46 CHANGES.
- **Delivery.** -19.7 LUFS, LRA 14.9 LU, span 19.3 dB (0.3 over), limiter 1.0 dB. Climax order: 160 -11.3 > 122 -12.1 > 167-170 -13.6 > 26 -14.2.

**Do not touch:**
- the 150 ms mf-ff string cap and the 237 ms horn caps;
- Violas `rt_gain_db` -6 (no further trail or release cuts on strings: finding 3);
- the hall (fx 0.095, low cut 160, `ir_setup` endPos / decayLength 0.5) and every send until Dan has heard it;
- the bar-62 f62 aliases with SUBITO_SILENT_QN, LEADIN_HOLD and their POST_SHAPES_S (2:43 stays fixed);
- `width_by_mic`;
- `alias_dup` / `tw_own` / `alias_check` (every test above depends on them);
- GENTLE_ACCENT and `accent_fits.json` outside the test spans;
- the dynamic plan (per-bar levels within 1 dB of c00 / c41 except bar 84);
- the climax order with the c46 fff lifts.
