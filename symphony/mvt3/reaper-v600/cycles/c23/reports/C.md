# Critic C, cycle 23 (tempo, timing and transitions), on the c22 render

Data: `cycles/c22/render/` (31 dry stems, 4 return stems, `00_Master.wav`), `cycles/c22/mvt3-mockup-c22.mp3` (decoded to 48 kHz; per-100 ms momentary loudness from ffmpeg `ebur128`), `cycles/c21/` and `cycles/c19/` / `c20/` renders for comparison, `build/parts.json` (only the ride rows changed after the render), `build/mockup.midi` (the printed tempo steps), `build/score_config.py`, `build/mix.json`, and the installed `.oib` patch files. I decompressed the patch files myself (gzip at byte 20, JSON inside) and did not use the bridge library. Score pages 12, 13 and 15 were read as images.

My measures (scratch scripts, deleted after this report):
- **pcx entries.** `tools/pcx.py attack_pcx` on every note that starts after at least 0.15 s of silence on its track (1,418 notes on 29 tracks).
- **Fold.** A band envelope (150-3000 Hz, or 30-150 Hz on the master) resampled to score time, one quarter per row, averaged over a span. On the fold I read the half-rise (amplitude halfway from the floor to the peak) and the peak. This works through the accelerando.
- **Frames.** 20 ms and 50 ms RMS frames on stems, the master and the mp3, around bar lines, repeats and stops.
- **Harmonic bands.** For legato-target holes, the level of harmonics 1-4 of the new pitch in 4096-point frames every 25 ms.

I cannot hear. "Measured" means a number from the files. "Inferred" means a conclusion from those numbers or from the data.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 23, so I did not do the page reading. I used `loop/MANUAL-GAPS.md` (items 2, 5, 6, 8 and the c21/c22 results) and the installed patch files. Page numbers are PDF pages of the May 2021 HO manual.

| Manual / patch (PDF page) | What it says | Where it applies here | Does the c22 render follow it? |
|---|---|---|---|
| p.101, 106, 109-110 Legato Repetitions / Legato Slur Repetitions (MANUAL-GAPS #2) | Re-tongued samples for repeated notes inside a legato or sustained line | The chorale's same-pitch whole notes, bars 224-234 (qn 896-932): Horns 1-4, Trumpet 2, Trombone 1, Bass trombone, Tuba | Not used; no track loads a Rep row (parts.json). These notes play as Sus MAX with a 25 ms gap. Finding 3. Measured. |
| Patch read: every KS Master's Global Group has a CC11 `MidiController` with `fadeTime` 120 ms (1FH, 1TP, 1TB, 1TU, FL, Celli; the TLeg groups too). The manual (p.150-151) describes CC11 as expression but does not mention the smoothing. | Any CC11 move shorter than about 0.12 s is smoothed away | The c22 `move_fall` (18 units in about 0.1 s) and every short CC11 notch | Confirms the actor's suspicion: the fall cannot reach depth. Finding 3. Measured in the patch. |
| p.112 (woodwinds) / p.105 (brass) Legato: a slur plays only with no significant gap between the notes; the instruments are monophonic | The woodwind legato targets with holes (Flute 1/2, Oboe 1, cor anglais, Clarinet 1, Bassoon 1) | The render follows it (the targets overlap). The holes come from the patch's crossfade, not from the gap. Finding 4. Measured in the patch and on the stems. |
| Patch read, Leg Slur MAX row: TLeg groups A 54-92 ms, H 264-300 ms, D 177-237 ms to sustain 0.001. Legato-target sustain groups ("Fl2s", "OBs", "Cls") attack 440-553 ms, start mode VoiceTimer start 30 ms | The transition sample fades out from 0.32-0.39 s while the target's sustain is still rising | Same targets | Not addressed. Finding 4. |
| p.94 Staccato On Bow: the bow comes to a full stop at the end of the note | Double basses' hammered eighths 792-840, 984-1108 | The row is right and separation is good. The strokes are timed early: finding 2. Measured. |
| p.145 CC16 round-robin reset | Repeatability between renders | Followed: pre-roll and section resets. Keep. |

## State through this lens (measured)

- **Tempo map.** Unchanged since c15. Rendered length 423.76 s against 423.11 s printed. 125 of 558 half-note beats change tempo (22 %, which meets the research default of about 20 %). 23 beats differ 3 % or more from the printed step. Every printed tempo word is realised.
- **Entries (S2).** Class medians are centred: winds -19..+5 ms (cor anglais +30), brass -21..+16, strings -2..+13, timpani +14. This is the result of the c19 lead cuts.
  - At the 37 chords where 8 or more tracks enter after a rest, the median first-to-last spread is 97 ms (c18: 148; target under 100).
  - The outliers are the strings' printed swells at 744 and 1016, and the opening chord (finding 5).
- **Keyswitches.** 2,001 keyswitches. Median 20 ms before the note-on; 188 come less than one audio block (10.7 ms) before it; probe 0 late. No action.
- **Per-bar momentary maxima on the mp3** (Movement I c60 check):
  - 278 -7.4, 279 -7.6, 223 -7.7, 263 -7.7.
  - Below them: 277 -8.0, 262 -8.2, 264 -8.5, bars 1 / 5 -8.6, 132 -9.1, 222 -9.4.
  - No non-climax bar is above a climax. The check passes, but the bars just before 263 and 278 are within 0.3-0.5 dB of them (finding 1).
- **Final fermata.** The final chord rings to -10 dB at about 0.6 s on the mp3 and to -58 dB at 2.0 s. The file ends 2.9 s after the chord. Correct as printed (the fermata is on the rest).

## Findings

### 1. The fff arrivals at bars 263 and 223 come with no time and no air before them; bar 263 hardly steps even on the mix (measured; fix inferred)

**Where:** qn 1048 (bar 263, crash, all brass fff) and qn 888 (bar 223, Maestoso). Bar 278 (qn 1108) is the comparison.

**Evidence, mp3 momentary loudness** (step = maximum in the first 0.6 s minus the maximum over the bar before):

| arrival | c21 | c22 |
|---|---|---|
| 888 | +1.7 | +1.7 |
| 1048 | +1.7 | +0.5 |
| 1108 | +1.0 | +0.3 |

The c22 crescendo row lifted bar 262 (from -9.6 to -8.2) while bar 263 stayed at -7.7.

**Evidence, master and mp3 in 50 ms frames around the downbeat:**
- **1048.** The master is at -15..-16 dB, dips only to -18.3 / -19.1 in the 100 ms before the beat, and comes back to -15..-14. On the mix itself that is a step of about +1 dB, and on the mp3 +0.5..+2 dB.
- **888.** The master steps from -18 to -12 (+6 dB), but the mp3 only from -15.6 to -11.7.
- **Comparison with breaths.** Where the orchestra does breathe, the arrival is clear: at 840 (Largamente, general rest) the master dips 9 dB, and at 1108 (rest plus `CAESURA` 0.04) it dips 18 dB.

**Why the arrivals have no air:**
- At 1048 every string track joins straight through (Violins I overlap 34 ms, violas and Violins II 30 ms gaps, celli 14 ms), and the timpani roll continues. The wind and brass gaps of 68-120 ms are filled.
- **Tempo at 1048:** strict 176 through the downbeat.
- **Tempo at 888:** the allargando ramp reaches 112 one beat early (beat 886 at 112.0). Bar 223 then runs faster than that beat (112.8, 113.7) because of the +1.5 % push of `PHRASE_ARCS` (888, 912).
- This is my c19 finding 6; it was never tried.

**Score support:**
- The allargando of 221-222 is printed. The flutes and Violins I have a rest and a rising pick-up in the second half of bar 222 (page 12).
- At 263 the violins start a new fff eighth figure and the celli a new whole note ("non div.").
- Breaths are printed at 1040 and 1044.

**Answer to the coordinator:**
- +0.3 / +0.5 / +0.6 dB is not enough to hear an arrival by level. The limiter (4.3-6 dB on these bars) will not allow more.
- What is left is articulation: a short silence and a slightly late downbeat, as a real orchestra plays it.
- The scherzo's -2 to -4.5 dB ride over the 4 beats before an arrival works against our crescendo target (the mp3 rise of +1.5 dB over 1032-1047). Use it only as a small fallback.

**Fix:**
1. **Tempo** (`build/score_config.py`):
   - `CAESURA[1048.0] = 0.05` (about 7 % on the last half-note beat at 176).
   - `CAESURA[888.0] = 0.06` (the last beat of the allargando 112 -> about 106).
   - `PHRASE_ARCS` (888, 912) -> (892, 912), so bar 223 starts at 112 without the push.
   - Then `--midi-only --tempo` on all tracks, and check the re-bow fill keys against the built positions (Movement I LEARNINGS c11).
2. **A lift before 263** (`INSTR_POST["note_end"]`, instrument side, no fader):
   - Violins I, Violins II, Violas, Violoncellos: the note sounding into 1048 ends 0.06 s before that track's moved 1048 note-on. Use `end` 1048.0, `tol` 0.3, with `early_s` sized so that the gap is 0.06 s; the Violins I overlap of 34 ms becomes a 60 ms gap.
   - The basses already leave 168 ms.
   - Timpani unchanged.
   - No CC11 fall, so the cut stays a gap and not a subito (S3).
3. **Fallback, delivery only** (if the targets are missed): a ride row of -1.0 dB over 1046.0-1047.95, back to 0 at 1048.0.

**Targets:**
- Master 50 ms frames: a dip of 6 dB or more in the 150 ms before 1048, and the first frame after 1048 at least +3 dB over the frame at -0.3 s (now +0.4).
- mp3 step at 1048 of +1.2 dB or more; 888 kept at +1.7 or more.
- Climax order unchanged.

### 2. The basses' hammered eighths speak 60-80 ms before the timpani (S2; measured)

**Where:** Double basses, "Stac On Bow RRx9", 792-840, 984-1080, 1088-1104; timpani on the same beats.

**Evidence** (fold, 150-3000 Hz; half-rise / peak against the beat):

| span | basses on-beat | basses off-beat | timpani |
|---|---|---|---|
| 792-816 | -62 / -15 ms | -62 ms | +23 / +35 ms |
| 816-840 | -50 / +25 ms | -45 ms | +23 / +38 ms |
| 984-1016 | -55 / -15 ms | -62 / -10 ms | +23 / +35 ms |
| 1056-1080 | -47 / 0 ms | -47 / 0 ms | +23 / +35 ms |
| 1088-1104 | -47 / +15 ms | -45 / 0 ms | (not in this span) |

- Separation is good: on/off bumps 13-30 dB, both eighths present.
- The master's 30-150 Hz band half-rises at -35 to -65 ms.
- **Cause.** c20 set `INSTR_POST["row_onset"]["Double basses"]` `lead_s` 0.10 to put the *peak* on the beat. pcx defines the perceived attack as the mean of the half-rise and the -10 dB point, and for these 13-17 dB rises that falls before the peak. So by the project's S2 measure the bass pulse is about 55 ms early, and the timpani strokes (about +20 ms) come about 75 ms after it. At this tempo 40 ms is already audible. c22 and c21 are equal here; c19 (lead 0.075 s, 70 %) had peaks at +43..+49.

**Fix:**
- `build/score_config.py`, the c20 ruling-5 block: `INSTR_POST["row_onset"]["Double basses"]` `lead_s` 0.10 -> 0.06 on all three spans. Keep the 60 % / 66 % lengths and the muted release extension.
- The expected shift is +40 ms: half-rise -55 -> about -15 ms, peak 0 -> about +40 ms, which is the timpani's peak.
- Range test 790:820 and 982:1000 against a control range render.

**Targets** (fold):
- Bass half-rise between -20 and +20 ms, and within 30 ms of the timpani's.
- Bass peak within 15 ms of the timpani's peak.
- On/off bump heights within 2 dB of now.

### 3. The chorale's same-pitch repeats: a 25 ms gap and a smoothed CC11 fall cannot separate them (S1; measured)

**Where:** bars 224-234, from the c19 chorale block in `build/score_config.py` (`INSTR_POST["gap_set"]` rows `{"from": 894.0, "to": 936.5, "gap_s": 0.025, "pitch": "same"}` and the `onset_lead` rows with `gap_s` 0.025). Every same-pitch whole note in the chorale has a 25 ms gap at 112 bpm (a whole note lasts 2.14 s).

**Evidence:**
- **Dips per repeat** (20 ms frames, deepest frame against the lower of the body levels before and after):
  - Horn 2 at 920 / 924 / 928: -0.7 / -0.7 / -0.6 dB, so no dip at all.
  - Horn 1 at 896 / 900 / 908: 4.8 / 6.6 / -1.4 dB.
  - Horn 3: 0.0 / 3.2 dB; Horn 4: 3.2 / 1.4 dB.
  - Trombone 1 at 920-932: 3.1-3.9 dB.
  - Bass trombone: 3.1-5.3 dB.
  - Tuba: 3.0-4.2 dB.
  - Each dip lasts one or two 20 ms frames. The actor's broader window reads 1-1.5 dB.
- **Wider gaps work.** The woodwinds with the same 25 ms gap dip 2-7 dB (their release is shorter). At the printed breath of 920, where the gap is 100 ms, Flute 2 and Oboe 2 dip 14.4 / 10.5 dB.
- **The fall is smoothed.** The patches' Global Group CC11 `fadeTime` is 120 ms, so the c22 fall of about 0.1 s is smoothed to a fraction of its depth.
- **Research default.** The repeat gap for brass is 60-100 ms (median 98 ms, FINDINGS section 8). 25 ms is far under it.

**Fix** (range test 884:940, two variants, against a control range render):
- **Variant A (data only).**
  - Same-pitch `gap_s` 0.025 -> 0.07 on the brass: Horns 1-4, Trumpet 2, Trombone 1, Bass trombone, Tuba. Move the old note-off earlier and keep the new note-on, so the c19 stagger and leads stay.
  - Woodwinds and bassoons: 0.025 -> 0.05.
- **Variant B (Opus state, full rebuild of the 8 brass tracks).** Variant A plus the brass KS Masters' Global Group CC11 `fadeTime` 120 -> 40 ms. This would need a small generic `build_reaper.py` option beside `cap_release`, for example mix.json `"cc_fade_ms": {"cc": 11, "ms": 40}`. It lets the existing `move_fall` act. Listen-check risk: zipper steps on dense CC11 lanes; measure 1-4 kHz noise in the steady notes against now.
- **If neither reaches the target:** the "LegRep RRx4" row on Tuba and Trombone 1 for these notes (MANUAL-GAPS #2).

**Targets:**
- Every brass same-pitch repeat dips 4 dB or more on the actor's measure, and stays at least 6 dB down for 50 ms or more.
- The master's bar-line holes at 896-932 stay at 4 dB or less (now 0.7-3.3).

### 4. Wind legato holes: the transition sample fades out before the target's sustain has risen (measured in the patch and on the stems; fix inferred)

**Where:** the targets listed by `holes22.py`: Flute 2 9 of 10 targets; Flute 1 5, Oboe 1 6, cor anglais 6, Clarinet 1 6, Bassoon 1 6.

**What the patch does** (Leg Slur MAX row of FL2, OB, CL; same layout on EH and BS):
- A legato target starts two voices.
  - The transition group "TLeg <pitch>": AHDSR attack 72 / 54 / 92 ms, hold 300 / 264 / 299 ms, decay 237 / 177 / 177 ms to sustain 0.001. It is silent by about 0.5-0.6 s.
  - The target sustain group "Fl2s / OBs / Cls <dyn>": start mode VoiceTimer, starting 30 ms after the other voice. Attack 525 / 440 / 553 ms.
- So the transition starts to fall at 0.32-0.39 s, while the sustain is still in its attack.
- The c22 attack cap (200 ms on the sustain) made Clarinet 1 worse (4 -> 11 holes). This fits two recordings of the same pitch summed at similar levels for longer, which cancel at some harmonics (inferred).

**What the stems show** (harmonics of the new pitch):
- **Flute 2 (618, 842, 602, 1074).** The holes sit at 0.37-0.45 s, in the TLeg decay. The dips differ by harmonic: at 618, h1 is -14 at 0.45 s while h2 is -1. This points to interference during the crossfade.
- **Oboe 1 384, cor anglais 738, Clarinet 1 606.** The new pitch's h1-h2 are 6-20 dB under the body for 0.1-0.3 s while the transition plays, then rise with the sustain. The transition sample is simply quieter than the body.
- c21 showed that a +4 dB TLeg region gain does not move the cor anglais' rise.

**Fix:**
- **(a) Holes at 0.3-0.45 s** (most of Flute 1 / Flute 2, Clarinet 1 at 0.43 s, Bassoon 1 at 0.37-0.40 s): a new generic Opus-state option beside `cap_attack()`, for example mix.json `"tleg_env": {"rows": ["Leg Slur MAX", "Leg Slur"], "hold_ms": 550, "decay_ms": 250}`, on the FL, FL2, CL and BS KS Masters. It sets the TLeg groups' hold to 550 ms (the target sustain attack is 440-553 ms) and their decay to 250 ms. The transition then lasts until the sustain is up. This is the opposite direction from the failed cap, and untested. Range test 320:392 and 836:1016 against a control range render; measure `holes22.py` plus the harmonic-band check.
- **(b) Holes at 0.1-0.25 s** (Oboe 1 384 / 844 / 848 / 1014, cor anglais 638-740, Clarinet 1 998 / 1014): play those targets on "Sus MAX" through `ART_SPANS`. This is the route already measured on the cor anglais (c21) and Horn 1 (c22: holes 2 -> 0).

**Target:** holes of 6 dB or more halved per track, with no new holes on non-target notes.

### 5. The opening chord: strings start inside the pre-roll cut, brass 40-130 ms late (measured)

**Where:** qn 0, bar 1. This is the first sound of the movement (ff tutti, German sixth).

**Evidence:**
- The master's first sample is 0.026 (-32 dBFS). Violins I are at -40 dB in the first 5 ms, so the strings' led attacks are cut off by the pre-roll trim (noted at c00 and never fixed).
- The brass start from zero at the beat, with no lead possible. pcx: Horn 1 +129 ms, Tuba +77; chord spread 124 ms, median +29 ms.
- On the stems, Horn 1 reaches its body at about 140 ms and Tuba at 100-120 ms, while the strings are already at their body level at 0 ms. So the movement's first chord is smeared and begins with a cut string attack.

**Fix** (`tools/render_cycle.py`, generic):
- Render from 0.30 s before qn 0, and trim that 0.30 s from the stems and the float master used for metrics, so every measurement stays on score time.
- Deliver the mp3 from the untrimmed sum, with a 10 ms fade-in at its first sample.
- In `score_to_parts.py`, let leads at qn 0 go down to -0.30 s, so bar 1 takes the normal entry leads (Horn 1 0.09 s, brass 0.05-0.09).

**Target:** bar 1 chord spread under 80 ms, median within ±15 ms; the master at -60 dBFS or lower in the first 10 ms of the delivered file.

### 6. Celli hang 150-300 ms over the tutti cut-offs (measured; cause inferred)

**Where:** the cut-offs at 374 (bar 94), 450 (113) and 814 (204); bars 2 / 6 in c21.

**Evidence:**
- **Time to -10 dB after the common end:** most stems take 100-130 ms (median).
- **Celli:** +410 ms at 374, +250 at 450, +240 at 814. At 374 the celli sit at a plateau 7 dB under their body from +130 to +330 ms. At 814 the celli are at -37..-42 dB for 0.3 s while the basses fall 30 dB in 0.12 s.
- The notes themselves end 30-50 ms early (Sus MAX / Leg BC MAX, release cap 150 ms at f/ff). What hangs over is inferred to be the celli's release-trail groups ("Vc f RT", "Vc ff RT"), which `cap_release` leaves alone unless `rt_ms` is set.
- **Master drop at +0.3 s:** 13.9-15.1 dB at these stops (stable c19-c22). At 204 it is 13.9 dB, under the 15 dB floor.

**Fix:**
- Range test 370:378 and 810:818: mix.json Violoncellos `sus_release_cap_ms` with `"rt_ms": 80` (Opus state, full rebuild of the celli).
- If the plateau does not move, the release-trail voices ignore their AHDSR release. Then, instead, write CC11 down by 20 units over the last 0.12 s before these three note-offs. CC11 picks the RT layer (start mode Controller 11), so the release plays the softer "mf RT" layer. That is instrument side, not a fader move.

**Target:** celli -10 dB within 180 ms of the common end; the master at 15 dB or more at +0.3 s at 204.

## Coordinator's items through this lens

- **fff arrival steps:** finding 1. +0.3 to +0.6 dB is not enough, and on the mix itself 1048 steps only about 1 dB.
- **Chorale repeats / CC11 smoothing:** verified. Global Group CC11 `fadeTime` 120 ms in the brass, flute and celli KS Masters. Gap and variants in finding 3.
- **Wind legato holes:** finding 4. Cause: the TLeg hold/decay against a 440-553 ms target attack, plus a quiet transition on Oboe 1 and the cor anglais. The velocity floor could not act on either.
- **Basses' eighths 816-840:** the 2.2 dB level gap to c19 is a level question (lens B). The timing of these eighths is finding 2: both spans are early, the same as 792-816. A later note-on does not change their level.
- **Trumpet off-beats 159-166:**
  - Trumpets 1-2 play "Stac DblTng RRx9" at velocity 92 in c22. That row's layers in the 1TP KS Master are 1-54, 55-75, 76-94 and 95-127.
  - c21's velocity 96 sat in the top layer and measured -2.2 / -3.3 dB under Horn 3, which is the target. The c22 drop of 6.6-7.9 dB is that layer change, not 0.5 dB per step.
  - So velocity add +8 (v96) restores the measured c21 level. +7 (v95) gives the same layer.
- **Movement I c60 per-bar momentary check:** passes (section "State").
- **Trumpet repeats (Più allegro):** Trumpet 3's same-pitch re-attacks at 984-1080 sit at pcx median -8 ms (p10 -30, p90 +44). Timing is fine; the dips are lens A.
- **Not measured here (lenses A and B):** harp level in bar 235, bar 131 against 130, the brass dip at 1036-1040, Horn 4's held-note wobble, Trumpet 3 accents.

**Do not touch:**
- The printed tempo ramps, `RAMP_END_CLAMP`, the caesuras at 72, 104, 392, 632, 664, 816 and 1108, and the lyrical arcs. Only 888 changes (finding 1).
- The c19 entry-lead cuts: class medians within ±20 ms, chord spread median 97 ms.
- `TIMP_DELAY_S` 0.02, and percussion on the grid.
- The chorale's pitch-change overlaps and staggered leads (only the same-pitch gap changes).
- The basses' 60 % / 66 % lengths and muted release extension (separation 13-30 dB).
- CC16 resets.
- `FINAL_RING` and the final fermata length.
- The stops of bars 2 / 6 / 150 (15.1 / 14.8 / 17.4 dB).
- The 840 general breath (9 dB master dip).
- No per-note move in the track envelope.
