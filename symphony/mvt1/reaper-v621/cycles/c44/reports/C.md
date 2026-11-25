# Critic C, cycle 44: holistic comparison (render c43, score v621), with "mushy" measured apart from the hall

Render under review: c43 (`cycles/c43/render`, 40 stems, master = float stem sum; data `cycles/c43/rendered_build/`). Compared with cycle 0 (`cycles/c00/mvt1-mockup-c00.mp3`; its stems are gone, and it rendered v221), with c38 (five cycles back, `cycles/c38/render`), with the Dvořák 9/i recording (audio decoded) and with the stored Brahms metrics (`symphony/render/critics/c00|c04/ref_brahms*/metrics.json`, same algorithms as `symphony/render/tools/rtk.py`, which I re-implemented in numpy). Scripts were in my scratch folder (deleted at the end); per-note pitch bands use `tools/pcx.py` (`band_env`, `band_mask`, `legato_joins`).

Following the coordinator's note, I do not spend findings on the hall at `fx_volume` 0.095, the 160 Hz low cut, the shorter IR, or the string same-pitch re-attacks. I measured what else makes the sound mushy.

## Manual notes (second reading of the c38 slot C row: PDF pages 10-11 and 61-63, read again in full; p.142 added; MANUAL-GAPS.md and DIGEST.md read)

| Manual (PDF page) | What it says | Where it applies | c38 status | Now (c43) |
|---|---|---|---|---|
| MANUAL-GAPS open items first | #1 brass accent rows, #4 Mid mics, #5 expressive rows, #7 half-section divisi, #9 horn portato, #12 crescendo rolls, #13 bass trombone low notes | — | open | All still open. #1 bears on my lens: attack colour is the band where the mockup lacks the most definition (below). #4 is one of the levers for S4 (Mid gives "definition without the sound of close proximity", p.138); it is not proposed here because it would change the depth the c41 critics asked for. |
| p.10-11 | The Opus Edition recorded new 18 Violins, 2 Trumpets ("blazing at high velocities"), 2 Trombones and 3-player wind ensembles. | the a2 unisons | partly | Still partly. "Trumpets a2" (2TP) has played in pass 2 since c39, and Horns a2 since c13. "2 Trombones EXP" was rejected in c39: it has no legato row and a 700 ms release, which would add to S4. 18 Violins is still unused because it has no bow-change legato. |
| p.61 | Seven libraries, all recorded in Studio 1; Moods (Classic, Soft, Epic), see 4.2.1. | every track | yes | Yes. The coda solo plays on Celli DIV A in pass 2 (c40), because Solo Cello is not installed. New for S4: the Classic mood is the Main mics plus a 3.4 s hall (DIGEST 4.2, p.136). Each sample's Main mic already carries Studio 1's room, and the pipeline adds a 3.3 s convolution hall on top, so two rooms are stacked. That stacking is why the ONE_TIME hall cut matters. |
| p.62-63 | MAX instruments hold the most dynamic and vibrato layers; LITE about half. | the rows in use | yes | Followed. The only LITE row is still Sus Marc LITE, on 14 strokes (Violins I 6, Violins II 6, celli 2; parts.json `art_counts`). |
| p.63 | Every instrument fades to silence on CC11 (niente). | HP_NIENTE, morendo, subito | in effect | In effect. Bar 62 measures -1.9 / -5.1 / -8.3 / -11.7 dB at 0-0.3 s (c43 CHANGES). With a drier hall, the post-hall envelope cuts less tail, so S3 gets easier. Re-measure it on c44. |
| p.63 | CC70 selects the finger position. | the sul spans | **no** in c38 | Followed since c38: `SUL_SPANS`, FP4 default 127, and Violins I on a fresh instance (c41). |
| p.142 (new on this reading) | Envelope RELEASE "determines how long the sound remains audible after a note is released"; "all instruments are programmed with envelope values to achieve a natural result, so please be careful when changing them". | string and horn note ends | not read in c38 | Not handled as a measured choice. Read from the patch files (opus_state): string sustain groups ship 323-524 ms at mf-ff and 524-931 ms at p-pp, with an instrument envelope of 931 ms. The string release-trail ("RT") groups ship 1245-1741 ms, source volume up to 3.98 (+12 dB) and release damping 0.8-0.93. Woodwinds ship 100-177 ms and damp their RT groups at 0.17-0.29. Horns ship 237-562 ms, plus RT groups up to +12 dB. Only Violas, Violoncellos and Double basses Sus MAX mf/f/ff are capped (250 ms, c21). Findings 1-3. |

## "Mushy", measured on c43 apart from the hall (the coordinator's four questions)

**1. The 200-500 Hz share is at the references; the excess is at 100-200 Hz in the soft passages (measured).** Band shares of the master (dB of total energy). Loud = top 10% of active frames by K-weighted momentary loudness; soft = bottom 30%. The Dvořák is measured the same way.

| | 100-200 | 200-500 | 500-2k | 2-6k |
|---|---|---|---|---|
| c43 loud / tutti bars | -10.2 / -9.7 | -6.5 / -6.3 | -2.4 / -2.5 | -11.0 / -11.3 |
| Dvořák loud | -7.1 | -6.1 | -3.3 | -10.6 |
| c43 soft / soft bars | -7.4 / -8.0 | -4.6 / -4.0 | -3.8 / -4.1 | -14.9 / -15.1 |
| Dvořák soft | -10.1 | -4.8 | -3.0 | -13.6 |

- **200-500 Hz.** It sits within 0.4 dB of the recording in tutti and within 0.2-0.8 dB in soft passages. In the Brahms files, 315-400 Hz re 1 kHz is -1.5..+5.1 dB; c43 is -0.2..+0.5 (loud) and +2.0..+2.7 (soft). A cut at 200-500 Hz would thin the orchestra, not clarify it.
- **The deviation is a tilt.**
  - Soft passages carry +2.6 dB more 100-200 Hz than the recording, and 2.5-5 kHz is about 2 dB darker (157 / 198 Hz re 1 kHz: +0.4 / +1.3 against -1.8 / -1.4).
  - Loud passages have 3.2 dB less 100-200 Hz than the recording.
  - Loud minus soft at 157 Hz: -3.5 dB in c43, against +4.1 in the Dvořák and +2.8 / +4.2 / -0.4 / +5.1 in the four Brahms files. In recordings, loud passages gain low-mid relative to soft ones; in the mockup it is the other way round.
- **Who makes the soft low-mid (per-stem share of the master's band energy, soft bars).**
  - The celli: 68% of 140-225 Hz and 51% of 225-280 Hz (-1.7 / -2.9 dB).
  - The basses: 31% of 90-140 Hz.
  - The celli carry static bells (170 Hz +3 dB / 1.5 oct and 125 Hz +3 / 1 oct; +5.2 dB at 125-150 Hz together, +3.8 at 200 Hz) at every dynamic. The basses carry a static 180 Hz +4 bell. All three were added in series 1 for the loud tutti, which the separate `loud_eq` now covers. Finding 4.
- **Tutti low-mid.** Basses 31-40% and timpani 21-22% of 90-225 Hz. The timpani share is the rolls under the tutti; Dan's roll rule is met, so I leave them.

**2. Note releases and overlaps (measured): the strings and horns keep sounding after their notes end.** Per note, the old pitch's harmonic band was measured with the next pitches' harmonics excluded (the pcx exclusion bands), against the note's own body.

| Family (row) | Phrase end, stem drop at 0.15 s | Legato: old pitch at -10 dB, after the new moved onset | Detached: old pitch -10 dB after its note-off | Hall send |
|---|---|---|---|---|
| woodwinds (Sus / Leg) | -5.2..-11.6 dB (median -9.5) | 0.15-0.27 s | 0.13-0.20 s | 0.35-0.5 |
| trumpets | -5.8..-8.6 | — | 0.19-0.22 | 0.65 |
| trombones, tuba | -5.4..-7.3 | 0.22-0.24 | 0.21-0.23 | 0.45 |
| horns | -3.4..-5.5 | 0.25-0.33 | 0.25-0.35 | 0.5 |
| strings | Vln I -10.2, Vln II -3.1, Vla -5.7, Vc -1.3, Cb -7.8 | 0.27-0.39 (Leg Slur / Leg BC) | Vln II 0.34, Vla 0.33, Vln I 0.19, Cb 0.20 (Sus MAX) | 0.25 |

- **Running figures (violas).** In the eighths and triplets of bars 97-102, 117-122 and 139-142 (Sus MAX strokes, IOI 0.159 s, n = 111), each old pitch is still -4.1 dB under its peak 70 ms into the next note, and -13.2 dB 70 ms into the note after. Three pitches of the arpeggio sound within a few dB of each other, so the figure reads as a held chord.
- **The strings have the lowest hall send of any family (0.25), yet the slowest note ends.**
  - Model (inferred from the stems' own late decay, 2.2 s, and their hall level extrapolated to the note-off: -8..-10 dB re body on Violins I / II and violas, median about -6 dB on the winds): the hall part of the violas' old pitch at that moment is about -13 dB, while the measured total is -4.1 dB. About nine tenths of what blurs the figure is the sample's own release and release trail, not the hall.
  - Halving the hall moves this by about 0.2 dB (inferred).
  - On the woodwinds the reverse holds: their -10 dB point (0.13-0.27 s) is close to what the hall alone predicts, so the hall cut will shorten their tails.
- **Played gaps.** Detached string notes on Sus MAX play their full written length into the next note: median gap 0-16 ms, and 27-81% of changes abut or overlap (Violins I 81%). Tongued winds keep 50 ms and brass 90 ms (`WIND_DETACH`). With 323-931 ms releases and RT trails on every note-off, each détaché note leaves its pitch under the next one.

**3. The master's drop after tutti cut-offs (measured; prediction inferred).** Drop at 0.15 / 0.3 / 0.6 s, measured from the first frame 2 dB under the 0.3 s pre-level:

| Cut-off (qn) | Drop at 0.15 / 0.3 / 0.6 s |
|---|---|
| 103 | -11.5 / -13.9 / (next entry) |
| 125.9 | -7.2 / -12.6 / -16.3 |
| 244 (bar 62) | -7.9 / -12.7 / -11.9 |
| 288 | -7.8 / -13.2 / -14.3 |
| 332 | -8.8 / -14.9 / -13.3 |
| 551 | -9.8 / -13.9 / (next entry) |
| 568.6 | -8.7 / -11.7 / -13.0 |
| 679 fermata | -8.1 / -14.2 / -20.8 |

- **What decides the tails at cut-offs.** The 679 fermata decays at 26-28 dB/s from 0.15 s on, a straight line in dB, with a late RT of 2.13 s (c38 2.10 s). From about 0.1 s after the cut-off the tail is the hall alone. The remaining dry part is -11 dB at 0.05 s and below the hall by 0.1 s, so `CUTOFF_EARLY_S` works.
- **Against the references.** With the stored references' own detector (rtk `cutoff_decays`), c38's fermata gives t to -20 dB 0.65 s and RT60 (-5..-20 dB) 2.36 s, and the Lento cut at qn 55 gives 0.60 s / 1.84 s (the same in c43; c43's fermata falls just short of the detector's 15 dB-in-0.4 s gate). My method gives 0.56 s for c43's fermata (c38 0.57). References: Brahms 1/i 0.485 s (0.43-0.55, 12 cut-offs) with RT60 1.13-1.62 s; Dvořák 0.50 s / 1.32 s.
- **Prediction for the fermata at hall -6 dB (inferred).** Drop at 0.3 s 16-19 dB (target 13); t to -20 dB 0.42-0.45 s, a little faster than the Brahms; the late slope unchanged. Finding 5.

**4. Inner-voice clarity (measured).**
- **Own-bin share.** This is each note's share of the master's energy in its own harmonic bins (h1-6) over its body. In tutti it is low for the violas (median -11.3 dB, 59% under -10 dB), Horn 4 (-10.5), Oboe 2 (-12.1), the bassoons (-10.1..-10.9) and Flute 2 (-10.8). In the development figures it is -12.2..-12.9 dB for the violas, where Bassoon 2, Horn 3, Horns a2 and Oboe 1 hold the same pitches.
- **Tails from tracks that have stopped are not the cause.** Tracks with no note sounding supply only 3-4% (tutti) and 2% (soft) of the master's energy in each band, almost all of it in the first 0.15 s after their note-off.
- **Where the blur comes from.** Inside each track, old pitches sound under new ones (question 2). The hall does the same at the level of the whole orchestra.

## Where the movement stands

| Measure | c00 | c38 | c43 | Reference |
|---|---|---|---|---|
| Delivered LRA / p10-max span | 17.3 / — | 15.0 / 19.1 | 14.9 / 18.9 | 14-16 / 16-19 |
| 3-10 Hz modulation of band envelopes, loud windows (dB SD), 60-200 / 200-500 / 500-1k / 1-2k / 2-5k Hz | 1.15 / 1.07 / 0.98 / 0.97 / 0.74 | 1.43 / 1.08 / 1.11 / 1.14 / 0.81 | 1.41 / 1.13 / 1.12 / 1.12 / 0.77 | Dvořák 1.84 / 1.30 / 1.38 / 1.22 / 1.18 |
| Same, mid-level windows | 1.25 / 1.29 / 1.27 / 0.96 / 0.76 | 1.28 / 1.36 / 1.27 / 1.04 / 0.83 | 1.29 / 1.35 / 1.32 / 1.03 / 0.82 | 1.85 / 1.42 / 1.50 / 1.28 / 1.11 |
| Band shares, loud and soft | within about 1 dB of c43 | within 0.3 dB of c43 | (table above) | (table above) |
| Fermata 679 t to -20 dB / late RT (my method) | — | 0.57 s / 2.10 s | 0.56 s / 2.13 s | Brahms 1/i 0.485 s / 1.13-1.62 s |

- **Against c00 (measured).** Over 43 cycles the envelope modulation (temporal definition) rose in the loud low band (+0.26) and at 500 Hz-2 kHz (+0.14..+0.15). It is still under the recording in every band. The largest gaps are 2-5 kHz (0.77-0.82 against 1.11-1.18, about a third less) and the loud low band. The comparison with the recording is inferred, since it is a different piece. Spectra and space did not change from c00 to c43; the cycles changed timing, articulation and balance.
- **Against c38 (measured).** Nothing in space or spectrum moved (band shares ±0.3 dB, identical cut-off tails), as expected: c39-c43 worked on timing, joins and balance.

**Weakest passages now (measured, by modulation and the per-note measures).**
1. **The development's stringendo and letter G, bars 113-122.**
   - The lowest definition in the movement: 200-500 Hz 0.93, 500 Hz-1 kHz 0.95, 2-5 kHz 0.71.
   - The violas' triplets, the rhythmic engine here, read as a held diminished chord: old pitch -4 dB into the next note, own-bin share -12 dB.
2. **The climax, bars 160-166.** 60-200 Hz 0.93, 200 Hz-1 kHz 1.08-1.09.
3. **The recapitulation's second theme (bars 147-159) and the coda tutti (bars 167-170).** 2-5 kHz 0.70-0.72; the attacks carry no edge.
4. **The development's eighths, bars 97-102.** These are the violas' figures under the ff tune: own-bin share -12.9 dB, notes overlapping.

**What still sounds like a machine.**
1. String notes do not stop: every détaché and legato string note leaves its pitch sounding 0.19-0.39 s into the next one (Findings 1-2).
2. The hall, which the ONE_TIME step addresses.
3. Attacks have little 2-5 kHz edge: accents are level swells with the plain note's front (MANUAL-GAPS #1 still open; c43 A #4 not done).
4. String same-pitch repeats, which c44 addresses.

**Dan's standing checks.**
- **7. Loop pulsing.** Met (measured). Master 100-300 Hz / centroid autocorrelation at 3.95 s: final chord +0.07 / -0.04, Lento 0-12 +0.20 / +0.10, sostenuto 484-500 -0.23 / -0.07 (controls at 2.6 / 3.3 s, same order: +0.00 / +0.07, +0.06 / -0.24, -0.21 / -0.01).
- **8. Brass accents.** Accent data unchanged since c41 (2-5 kHz front median -13.9 dB, max +3.2); not re-measured.
- **S1.** Re-attack work is in c44.
- **S2.** c43 probe legato robust SD 43 / 40 / 50 / 48 ms (c43 CHANGES).
- **S3.** See p.63 above.

## Findings, ranked by what a listener would gain

### 1. String notes ring on under the next note: cap the release of every string Sus MAX group, all dynamics, Violins I and II included (measured problem, patch read, effect inferred)

- **Where.** Every unslurred string note. Most exposed: the violas' eighths and triplets (bars 97-102, 117-122, 139-142), Violins II détaché (132 Sus MAX notes), the basses' pedals (325 Sus MAX notes), the celli strokes, and string phrase ends in soft passages.
- **What.** The Sus MAX sustain groups release over 323-524 ms at mf-ff and 524-931 ms at p-pp (patch; manual p.142). Violins I and II are not capped at all. The violas, celli and basses are capped only at mf/f/ff, and only to 250 ms (c21).
- **Evidence (measured).**
  - The violas' figures: old pitch -4.1 dB 70 ms into the next note.
  - Violins II detached: -10 dB only 0.34 s after the note-off. Violins I 0.19 s; woodwinds 0.13-0.20 s with more hall.
  - The hall part of that blur is about -13 dB (inferred, question 2), so halving the hall leaves it in place.
  - c21 measured what a release cap does on this library: basses -10 dB time 0.35 -> 0.26 s; string short-rest drop 4.1 -> 5.8 dB; master cut-offs 0.20-0.28 -> 0.13-0.24 s.
  - The same patches ship 133 ms on their own slur sustain groups (1st Violins "V1s f/mf/ff", read). 150 ms is a value the patch itself uses.
- **Fix (`build/mix.json`; full rebuild of these tracks, which c44 does anyway; this replaces the c21 entries on Violas, Violoncellos and Double basses).**
  - On Violins I, Violins II, Violas, Violoncellos, Double basses, Violins I f62 and Violins II f62: `"sus_release_cap_ms": {"ms": 150, "dyn": ["pp", "p", "mf", "f", "ff"], "rows": ["Sus MAX", "Sus Marc LITE"]}`.
  - Legato rows untouched (Finding 2). Cello solo untouched (fitted DIV A).
  - `build_reaper.cap_release` already handles these rows and dynamic names. It skips TLeg and RT groups and the "Marc Shrt" groups.
- **Refits afterwards (all level-only, by stem fix).** c21 showed that a release change moves re-bow joins (basses' re-bow dips -1.5 -> -3.2 dB). Refit:
  - `build/rebow_fills.json` (`tools/fit_rebows.py`);
  - the violas' stroke and `STR_REP_DETACH` levels;
  - the string accent fits on Sus rows (`fit_accents.py --family string`).
- **Pass criteria.**
  - Violas' running figures: old pitch at the next moved onset + 70 ms at -8 dB or lower (from -4.1; inferred about -8). Measure on the pitch band with the neighbours' harmonics excluded.
  - Violins II détaché: -10 dB within 0.22 s of the note-off.
  - No string phrase end falling more than 10 dB in its first 0.05 s, so no ends sound clipped.
  - Re-bow dips back in the c43 range after the refit.
- **If an end sounds clipped:** 200 ms.

### 2. Test the legato rows and the release trails on two sections in pass 2 before touching them (measured problem; fix to be tested)

- **What (measured).**
  - In legato the old pitch of a string section stays above -10 dB for 0.27-0.39 s after the new note's moved onset, and above -6 dB for 0.17-0.31 s. Winds: 0.15-0.27 s / 0.07-0.17 s.
  - The 6 dB transition window itself is only 82-98 ms (c42), so the excess comes after the transition.
  - The legato rows share the long sustain-group releases (323-524 ms at mf-ff).
  - The string RT groups play at up to +12 dB (source volume 3.98) with damping 0.8-0.93 (woodwinds 0.17-0.29).
  - c41's LegatoSpeed RELEASE 300 ms test moved this tail only 20-40 ms. I re-measured c41's test stems: violas t-10 0.344 -> 0.310 s, celli 0.281 -> 0.260 s. So the script's RELEASE is not the lever; the group envelopes and the trails are.
- **Fix (a test).** Two `TEST_TRACKS` aliases in pass 2, as c41 built "Vla test A/B": "Vla rel test" (all of Violas' notes) and "Vc rel test".
  - mix.json for both: `"sus_release_cap_ms": {"ms": 200, "dyn": ["pp", "p", "mf", "f", "ff"], "rows": ["Leg Slur MAX", "Leg BC MAX"]}`.
  - A new `build_reaper.py` mix key, e.g. `"rt_gain_db": -6`: multiply `SourceProcessor.volume` of every group with `releaseTrail: true` by 10^(-6/20). The instrument's `releaseTrails` key (true in every patch) would switch the trails off entirely, as a third variant.
- **Measure with `tools/pcx.py`.**
  - Old-pitch t-10 after the new moved onset (target 0.08 s shorter or more).
  - The count of joins with 5 dB dips or more against the main stems; c41 had violas 9 and celli 24. Adopt only with no more dips than main.
  - Phrase ends into rests.
- **Why only a test.** The joins have fitted leads, fills and notches (c42-c43), and c41's variant B raised the 5 dB dips.

### 3. Horns have the slowest note ends in the orchestra: cap their soft-layer releases at the patch's own ff value (measured problem, patch read, effect inferred)

- **Where.** Horns 1-4 and Horns a2 everywhere, most audibly in the tutti chords and the repeated pedals (bars 20-22, 69-72, 117-126, 131-142, 157-170).
- **What (measured).**
  - After a horn phrase end the stem is only -3.4..-5.5 dB down at 0.15 s. Trumpets: -5.8..-8.6. Winds: -5.2..-11.6 (median -9.5).
  - Old pitch at -10 dB 0.25-0.35 s after detached and legato changes.
  - Predicted with the hall at -6 dB: still -3.4..-6.8 dB at 0.15 s (inferred). The horn tail is the sample, not the hall.
- **Patch (read).** 1FH Sus MAX / Leg Slur MAX releases are pp 562, mf 394, f 316, ff 237 ms; RT groups up to +12 dB with damping 0.7-0.8. The horn mics are Close 0.5 / Main 1.0 against the factory 1.35 / 0.44, room-heavy (p.138-139).
- **Earlier lessons.** Repeat dips were hard to reach on horns for the same reason (c06: "the Solo French Horn release and hall tail fill a 0.06 s gap"; Horn 4 repeats 2.8 dB in c07).
- **Fix.** `build/mix.json` on Horn 1-4 and Horns a2: `"sus_release_cap_ms": {"ms": 237, "dyn": ["pp", "mf", "f"], "rows": ["Sus MAX", "LegRep RRx4"]}`. The Leg Slur MAX groups stay as they are until Finding 2's test reports. Check the group list that `cap_release` prints for Horns a2 (2FH), whose group names I did not read.
- **Afterwards.**
  - Re-measure the horn gap dips and breath rows (c41) and the Horn 1 portato shapes, and refit by stem fix any that move.
  - Target: phrase-end drop at 0.15 s of -6 dB or lower; horn same-pitch repeat dips in the master of 6 dB or more.
- **The mic balance** is a second lever, left for a later cycle.

### 4. Soft passages are bottom-heavy at 100-200 Hz: move the celli's and basses' static low-mid bells into their loud EQ (measured; fix simulated)

- **Where.** Every soft passage: Lento, the celli dolce tune (bars 47-55, 147-155), bars 73-90 and the coda.
- **Evidence (measured).** Question 1: soft 100-200 Hz +2.6 dB over the recording; loud minus soft at 157 Hz -3.5 dB (recordings mostly +2.8..+5.1); the celli make 68% of the soft passages' 140-225 Hz. The loud passages, by contrast, are 3.2 dB short at 100-200 Hz, so the loud bells must stay.
- **Fix (`build/mix.json`).**
  - "Violoncellos": remove `bell` 170 Hz +3 / 1.5 oct and `bell2` 125 Hz +3 / 1.0 oct from `eq` (keep the 30 Hz high-pass). Add a second `loud_eq` spec with the same points as its first spec and bands `[{"band": "bell", "hz": 170, "db": 3, "bw_oct": 1.5}, {"band": "bell2", "hz": 125, "db": 3, "bw_oct": 1.0}]`. A track takes one ReaEQ per loud_eq spec (KIT §14).
  - "Double basses": move `bell` 180 Hz +4 / 1.0 oct the same way. Keep `bell2` 87.3 Hz -10 static.
  - Leave "Cello solo" as fitted.
- **Simulated on the c43 stems** (complex-STFT EQ outside the loud spans, master rebuilt).
  - Loud frames: unchanged within 0.02 dB.
  - Soft frames: 100-200 Hz share -7.3 -> -8.8 dB; 157 / 198 Hz re 1 kHz +0.8 / +1.8 -> -1.3 / -0.3 (Dvořák soft -1.8 / -1.4); 500 Hz-2 kHz +0.4 dB; 2-6 kHz +0.4 dB; loud minus soft at 157 Hz -3.5 -> -2.0.
- **Level.** The move lowers the soft passages' K-weighted level by 1.7 dB (celli) and 2.0 dB (basses).
  - With both restored by `soft_trim_db` (celli +1.7, basses +2.0 at pp/p), the simulation still gives soft 100-200 Hz -1.0 dB and 157 Hz -1.8 dB re 1 kHz. The basses' restoration, though, raises the soft 20-100 Hz share by 0.9 dB.
  - So restore the celli only, and leave the basses 2 dB lower in soft passages: c16 found them the loudest stem in held soft chords.
  - Check B's soft balance points with `cycles/c33/actor_scripts/sim.py` before rendering.
- **What not to do.** Do not cut 200-500 Hz: it sits at the references in both loud and soft passages.

### 5. The hall cut alone meets the cut-off target: do not lower sends or add other tail cuts, and judge the IR envelope by the late slope (measured; prediction inferred)

- **Evidence.**
  - At tutti cut-offs the tail from about 0.1 s on is the hall alone (the 679 fermata decays on one straight line, 26-28 dB/s).
  - The dry part is already 11 dB down at 0.05 s, which `CUTOFF_EARLY_S` gives.
  - At `fx_volume` 0.095: drop at 0.3 s 16-19 dB against the target 13 (now 11.7-14.9 by my method); t to -20 dB 0.42-0.45 s, faster than Brahms 1/i's 0.485 s (now 0.56 s).
  - What stays different from a recording is the late slope: RT 2.1-2.4 s against 1.13-1.62 (Brahms) and 1.32 (Dvořák).
- **Fix.**
  - Keep every send.
  - Do not use Findings 1-3 to win back depth or the other way round: they act on the first 0.3 s inside phrases, the hall on the tail after cut-offs.
  - For the IR envelope test (ONE_TIME #3), choose the Decay setting by the late slope (-20..-35 dB), not by the 0.3 s drop: target an RT of 1.5-1.9 s.
- **Check on c44** (inferred risk). With the hall no longer covering them, the 0.04-0.05 s early ends (`CUTOFF_EARLY_S` strings 0.05, brass 0.04) and the f62 aliases' fitted release shapes (`POST_SHAPES_S`) are more exposed. Re-measure bar 62 and the 679 fermata at 0-0.05 / 0.05-0.1 / 0.1-0.2 s, and halve `CUTOFF_EARLY_S` if the first 0.05 s falls more than 9 dB.

Do not touch: the 200-500 Hz band (it matches the references; no cut); the loud `loud_eq` low-mid bells on celli, basses and low brass (the loud tutti is still 3.2 dB short at 100-200 Hz); the climax order and delivery settings (LRA 14.9, span 18.9, RIDE_TRIMS, limiter 0.5 dB); AUTO_REBOW with its spacing and fills (loop autocorrelation 0.07 / -0.04 on the final chord), refit only where the release caps move them; the true-stereo hall IR, seats and widths; the pcX lead tables of c42-c43; `CUTOFF_EARLY_S` (it makes the cut-offs' dry part fast; re-check it after the hall cut, do not remove it); GENTLE_ACCENT; the woodwinds' release settings (their tails are the hall and will shorten with it).
