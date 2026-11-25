# Critic C, cycle 41: holistic comparison (render c40, score v621)

Render under review: c40 final (`cycles/c40/render`, 38 stems, master = float stem sum; data `cycles/c40/rendered_build/`). Compared with cycle 0 (`cycles/c00/mvt1-mockup-c00.mp3` and its metrics.json; its stems are gone, and it rendered v221), with c35 (five cycles back, `cycles/c35/render` and `rendered_build`), and with the Dvořák 9/i recording plus the stored Brahms metrics. Scripts are in my scratch folder (deleted at the end); the per-note measures reuse `cycles/c37/actor_scripts/m37.py` (pc = perceived attack, dip, front minus body).

## Manual notes (cycle 41, slot C: PDF pages 44-45 and 134-136, read in full; MANUAL-GAPS.md and DIGEST.md read)

| Manual (PDF page) | What it says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| p.44 | Each instrument has a pan knob, solo/mute, an output selector and a MIDI channel mode: Multi (per-note CC1/CC11/pitch bend, for MIDI guitars), MPE, Omni (CC1/CC11 apply to notes on every channel, for stacked sections) or 1-16 (discrete channels for multi-timbral use). | One instrument per Opus instance on every track (DIGEST §3), CC lanes on the track's own channel. | Yes. With one instrument per instance the mode cannot route a controller to the wrong notes. The master pan is centred in the pipeline (KIT §12), which matches the p.44 note that the pan knob, the Play-page master pan and the mixer pan are one control. |
| p.45 | Virtual keyboard: white = sampled range, blue = keyswitches outside it. CC1 "commonly" crossfades dynamic and/or vibrato layers, sets volume or selects articulations (MOD patches). CC11 sets overall volume, or the dynamics when CC1 holds vibrato. | CC1 = dynamics on the brass and clarinets (`CC1_DYN_TRACKS`), vibrato layer on winds and strings; CC11 = the printed line; balance in the volume envelope. Low instruments put their keyswitches above the played range (Contrabassoon, Tuba, celli, basses, read in parts.json). | Yes. No keyswitch clashes in parts.json (`ks_clash` empty on all 38 tracks); every string note is inside its sampled range (DIGEST §5.5). |
| p.134 | Play page: the purge pill (green = loaded at the preload size, red = purged, yellow = streaming as notes play). | A 1x offline render from the USB drive. | Yes: no purge; render_cycle waits for the samples; the attack probe found 0 late notes in both passes. |
| p.135 | Player window: Mood; Performance scripts; Sensitivity & MIDI control; Envelope; Stereo Double; convolution Reverb; mic channels; master channel (tuning, routing). | The pipeline sets mics, one shared hall, per-mic pans (width), envelope releases (harp `env_sustain`, string release caps) itself. | Yes, as designed. Stereo Double is not used. It would widen the narrow winds and brass (Finding 3), but as an effect on the whole signal. Restoring the Main pair's own spaced image with per-mic width is the better route (inferred). |
| p.136 | Moods. Classic (default): the Main mic mix (Decca tree + outriggers), "well-balanced, unified sound", large hall 3.4 s. Soft: Mid + Surround/Vintage through Abravanel Hall, "for slower, more emotional passages", "definition and depth". Epic: Close + Main + Surround, cathedral 2.8 s. | No mood is applied; each group loads Close + Main and one shared 3.3 s IR. Winds Close 0.5 / Main 0.8, but the woodwind Main samples sit 11-40 dB under Close (KIT §12), so the winds are close-mic sounds. | Partly. The strings, trombones and tuba follow the Classic (Main-led) model. The woodwinds do not: they have the driest early tail of any family (c39 C: -9.1..-13.6 dB at 0.15-0.25 s against horns -5.5..-8.2), and the exposed soft espr./dolce wind solos never use the Mid mics the Soft mood pairs with such passages (MANUAL-GAPS #4, still untried). |

Engine and mood facts from these pages that the render does not need: Multi/MPE modes, snapshots, the virtual keyboard's pitch-bend slider.

## Where the movement stands after the first block (c32-c41)

### Against cycle 0 and c35 (measured)

| Measure | c00 | c35 | c40 | Reference |
|---|---|---|---|---|
| Bar level vs the bar's loudest printed dynamic: r / slope | 0.785 / 3.7 dB per step | 0.803 / 3.8 | 0.807 / 3.8 | none |
| Delivered LRA (LU) | 17.3 | 14.8 | 15.0 | target 14-16 |
| Delivered loudness motion, dS4 p90 / 1 s-20 s (dB) | 9.55 / 5.00 | 8.63 / 4.61 | 8.94 / 4.84 | Brahms slow movements 8.55 / 4.56, 6.29 / 3.92 |
| Salient onsets per second (spectral flux, same detector, delivered mp3s, active frames) | 0.21 | 0.26 | 0.30 | Dvořák 0.53 |
| 3-10 Hz modulation of the 60-400 Hz envelope, loud frames (dB) | 2.23 | 2.58 | 2.65 | Dvořák 2.78 |
| Master L/R correlation 4-8 / 8-16 kHz | n/a | 0.539 / 0.701 | 0.538 / 0.617 | above 4 kHz 0.38-0.48 (Brahms, Dvořák); Dvořák 8-16 kHz 0.295 |
| Per-beat attack spread, Allegro tempi (robust SD; share > 60 ms off the beat median) | n/a | 36-44 ms; 20-26% | 33-40 ms; 19-22% | none |

- **Large-scale shape (measured).** Section power means of the master are within 1 dB of c00 everywhere except the second theme (+0.9 dB) and the recapitulation's second theme (+2.0 dB, where v621 changed the dynamics). From c35 to c40 no bar moved more than 1.5 dB except bars 158-159 (-2.2 dB, the c36 climax set). The 41 cycles changed detail, not the movement's dynamic plan, which was right from c00. Keep it.
- **Delivery (measured).** The c40 mp3 is still a little less mobile than c00's (8.94 / 4.84 against 9.55 / 5.00), the price of the headphone ride Dan asked for; it is above both Brahms references.
- **Rhythmic definition (measured; the reference comparison is inferred, since it is a different piece).** Salient attacks rose from 0.21 to 0.30 per second over 41 cycles, but this is still about half the Dvořák's 0.53 with the same detector. The low band's rhythmic modulation is now close to the recording's (2.65 against 2.78).

### Weakest passages now (ranked by what a listener would notice)

1. **The celli and horn dolce tune, bars 47-55, and its return, bars 147-155** (measured). This is the movement's main lyrical line. On the celli, both pitches sound within 6 dB of each other for a median 196 ms at each slur (p75 600 ms), against 112-126 ms for the violins. In bars 147-155, 15 of 25 celli attacks and 11 of 27 viola attacks lie more than 60 ms from the beat median (per-beat spread 60 ms; c35 61 ms). The movement has 64 exposed attacks (within 8 dB of the master) that sit more than 0.12 s late or 0.15 s early. 27 of them are celli notes, and 12 of those belong to these two tunes (pc mostly -0.17..-0.29 s). Ten of the 12 have the same pc as in c35: nothing in this block touched them.
2. **The slow string chorales: Lento bars 6-14 and Più lento / Tempo I bars 171-182** (measured). With bars 147-155, bars 6-14 have the widest attack spread of any well-populated passage: 61 ms, 34% more than 60 ms off (c35 65 ms / 38%). Bar 12's downbeat, the first forte of the piece, has celli at -306 ms, Violins II at -163, Violins I at +104 and Bassoon 1 at +93. Many of these are legato targets inside a crescendo (rises of only 8-12 dB), where the estimator is noisy. The coda improved, from 55 to 38 ms, but the chord changes at qn 704 and 708 still spread over 0.4 s (Violins II -311, celli -255 and -219, Bass trombone +168).
3. **The development, bars 97-116** (measured). Per-beat spread 42-43 ms, 26% off. The violas account for 19 of 45 attacks off, Violins II 19 of 29 and the celli 18 of 34.
4. **The recapitulation's first theme and the climax approach, bars 123-138 and 156-170** (measured). Exposed string repeats separate on the stems but not in the master (S1 below), and every accent is a level swell with an unchanged attack colour (Finding 2).

### What still sounds like a machine (ranked)

1. Every viola and cello slur sounds as a slide, about twice as long as the violins' (Finding 1).
2. Accents and repeated-note re-attacks differ from plain notes only in level, never in attack colour (Finding 2).
3. The winds and brass sound like dry spot-miked point sources laid over a roomy string section (Finding 3).
4. About half the salient attacks per second of a recording; this follows from 1 and 2 (inferred).

## Dan's listening notes after the block (BRIEF 7-9, S1-S3)

| Note | Met? | Evidence (c40; c35 in brackets) |
|---|---|---|
| 7. No loop pulsing on held notes | **Met** (measured) | None of the 33 held notes of 6 s or more reaches 0.4 autocorrelation at 3.95 s, in the 100-300 Hz band or the centroid. The highest is the Timpani at qn 464 (centroid 0.33, band 0.06, -14.7 dB re master); timpani rolls are also clean at 3.4 s. Master: Lento 0-12 0.18 / 0.16 (control lags -0.26..-0.01), final 704-728 0.00 / 0.02, sostenuto 484-504 -0.18 / -0.15. |
| 8. Brass accents soft, weight not bite | **Met** (measured) | 177 brass accents. 2-5 kHz first 80 ms minus body: median -13.9 dB, p90 -7.6, max +3.2 (Trumpet 1 qn 284) [c35 -14.0 / -7.2 / +1.4]. The master's 2-5 kHz jump at the attack: median -3.2, p90 +0.7, max +3.8 dB. The harsh case Dan heard was +7..+13. The open problem is now the opposite one (Finding 2). |
| 9. REAPER under about 45 GB | **At the limit, not met with margin** (measured) | Main project 45 GB settled and 45 GB after the c40 render (14 GB compressed). It was 46-47 GB after the c35-c39 renders. The second pass (17-18 GB) runs in its own session. There is no room for any instance in the main session, so new tests belong in pass 2. |
| S1. Repeated notes heard as separate notes | **Met for winds and brass; strings met on the stems but not in the master** (measured) | Exposed repeats (voice within 10 dB of the master). Stem broadband dip: winds 6.2 dB, brass 6.5, none under 3 dB [5.3 / 4.0]; strings 4.4, 29% under 3 dB [3.5, 47%]. Master harmonic-band dip (pitches C3 and up): winds 3.3 [2.1], brass 4.3 [3.6], strings 2.1 with 61% under 3 dB [1.7, 73%]. The low-string pulses (bars 127-138, 167-170) cannot be read with a harmonic comb at this window length. |
| S2. Perceived attack centre on the beat | **Centres met; spread not** (measured) | Family medians re the beat median: brass -1, winds +2, strings -1, timpani 0, harp 0 ms. Spread: Allegro 33-40 ms with 19-22% more than 60 ms off [36-44, 20-26%]; Lento 62 ms / 37% [62 / 39%]; Più lento 38 / 28% [49 / 34%]. By family: strings 57 ms / 33%, winds 28 / 17%, brass 32 / 14%. Legato string targets: 38% more than 60 ms off (violas 48%, celli 45%). |
| S3. A subito must not cut the hall | **Partly met; not yet heard by Dan** (measured) | Bar 62 master re the 0.35-0.05 s before the beat, over 0-0.05 / 0.05-0.1 / 0.1-0.2 / 0.2-0.3 s: -8.6 / -10.6 / -13.3 / -15.9 dB [c35 -11.3 / -13.4 / -16.2 / -15.5]. Bar 84: +0.7 / -1.8 / -7.3 / -9.2. The tutti fermata release at qn 679 by the same window: -3.1 / -4.5 / -8.1 / -12.8. The c36 fix stopped the glitch: the hall now decays rather than cuts off. In its first 0.2 s, though, bar 62 still falls 2-5 dB faster than a release. Some of that may come from the strings' drier send (inferred). The rest is a post-hall envelope fall of 13-16 dB within 0.35 s on the violins (measured, Finding 4). |

Also measured: Dan's priority 5 (timpani rolls) is met. Over all 11 rolls of 3.5 s or more, the timpani sit 9-16 dB under the master after the first second and rank 3rd-9th among the stems. Only the opening ppp roll is the master for its first second, because it plays alone. Priority 6 (delivery) is met: LRA 15.0 LU, span 19.2 dB (0.2 over the target), limiter 0.5 dB, climaxes in order (160 > 122 > 167-170 > 26).

## Findings, ranked by what a listener would gain

### 1. Viola and cello slurs are slides twice as long as the violins': the dolce tunes and slow chorales smear, and these legato joins are the largest source of the S2 spread (measured problem; patch read; fix inferred)

**Where.**
- The celli dolce tune, bars 47-55 (qn 184-220), and its return, bars 147-155 (584-620).
- The Lento chorale, bars 6-14 (qn 20-56).
- The Più lento / Tempo I chorale, bars 171-182 (680-728).
- Every celli and viola slur in the Allegro.

**What is wrong (measured, c40; c35 in brackets).** Both-within-6-dB window: the time around the crossover during which the new and old pitches' harmonic bands are within 6 dB of each other.

| Section and passage | Joins | Window median | p75 | p90 |
|---|---|---|---|---|
| Celli, dolce tunes | 47 | 196 ms [204] | 600 | 674 |
| Celli, Allegro | 71 | 236 [236] | 388 | 604 |
| Violas, slow passages | 36 | 174 [164] | 546 | 822 |
| Violins I, molto cantabile bars 56-61 | 14 | 114 | 171 | 325 |
| Violins I, Allegro | 71 | 112 | 138 | 332 |
| Violins II, molto cantabile | 14 | 126 | 188 | 217 |
| Cello solo (DIV A) | 8 | 150 | 244 | 378 |

- **Crossovers.** Medians: celli +56 ms, violas +34, Violins I +58-60, Violins II +72. My detector reads about 24 ms late by construction, so the true values are roughly +10..+50 ms.
- **Perceived attack.** Legato targets: violas robust SD 101 ms (48% more than 60 ms off), celli 82 ms (45%), against Violins I 58 (31%) and Violins II 56 (33%).
- **Unchanged since c35.** Nothing in the block changed these joins. Of the 12 exposed dolce-tune celli notes more than 0.12-0.15 s off the beat, 10 have the same pc in c35 and c40. The celli make up 27 of the movement's 64 exposed off-beat attacks.

**Cause (patch, read by c38 critic C and the c38 actor).** In the LegatoSpeed script, velocity maps to a start offset into the transition sample, up to START_MAX:

| Patch | START_MAX (samples) | BUMPRED | RELEASE |
|---|---|---|---|
| 1st Violins | 4800 | 4760 | 450 ms |
| Violas | 2173 | 3890 | 510 ms |
| Celli | 2709 | 3130 | 443 ms |

At v124, therefore, the violas and celli skip only 44-55 ms of each recorded slide, against about 97 ms for the violins. The manual says velocity 110-127 gives the "shorter" transition (p.144; DIGEST §2.1), but these START_MAX values cap how short the lower sections can go. The c38 actor deferred the test because an offset beyond BUMPRED is untested and a START_MAX change also acts as a lead change. They proposed "one section, leads unchanged, both estimators, RELEASE as a second variable". The second pass, built in c39, now allows exactly that without touching the main project.

**Fix (A/B in the second pass, main project unchanged).**
1. **Tool.** `tools/build_reaper.py apply_mix()`: a per-track mix.json key `"legato_speed": {"START_MAX": n, "RELEASE": ms}`, written into the Opus state's LegatoSpeed EventFilterScript parameters (the same kind of state edit as `env_release_ms`).
2. **Test aliases.** Four test aliases in `ALIAS_TRACKS` / `PASS2_TRACKS`, rendered and then left out of the sum like c40's "Violins I test". Each plays its section's own notes, lanes and leads (no "drop", leads unchanged):
   - "Vc test A": Violoncellos over 182-220 and 584-620, START_MAX 3130 (= BUMPRED).
   - "Vc test B": the same windows, START_MAX 4800 and RELEASE 300.
   - "Vla test A": Violas over 20-56 and 680-728, START_MAX 3890.
   - "Vla test B": the same windows, START_MAX 4800 and RELEASE 300.
   Memory is about 5 GB per section instance in pass 2 (c40 measured).
3. **Measure each variant against the main render's stem on the same notes:**
   - the both-within-6-dB window;
   - crossover and pc (both estimators);
   - join dips of 5 dB or more, and bursts of 3 dB or more (c40 joinchk method);
   - 2-5 kHz front.
4. **Pass if:**
   - window median ≤ 130 ms and p75 ≤ 200 ms (the violins' values);
   - crossover and pc agree within 30 ms;
   - no new dips over 5 dB.
5. **If a variant passes,** adopt it on the main Violas and Violoncellos in the next render: a full rebuild of both tracks; leads lowered by the measured shift (expect about 0.04 s, a lead change, as the actor noted); rebow_fills, early_fills, loop_fills and the c40 join notches refitted. Then refit the per-onset chorale leads (bars 6-14, 171-182). Until then the two estimators disagree too much to fit them.

### 2. Accents and repeated-note re-attacks change only in level, never in attack colour (measured; fix inferred)

**Where.** All 663 printed accents, most densely in bars 23-33, 69-72, 80-83, 117-122, 131-143, 156-170. Also the re-attacks of every repeated note.

**What is wrong (measured, c40).** 2-5 kHz energy in the first 80 ms from the moved onset, minus the note's body (0.15-0.45 s), on non-legato notes of 0.75 qn or longer:

| Family | Accented: n, median (p25/p75) | Unaccented: n, median |
|---|---|---|
| Brass | 142, -14.4 dB (-19.5/-10.8) | 573, -12.5 |
| Strings | 51, -8.5 | 322, -6.1 |
| Winds | 202, -11.2 | 641, -10.8 |

- **Accents.** An accented note starts 0.4-2.4 dB duller than an unaccented one, so the accent is only the fitted 2-4 dB volume swell. The brass median is -13.9 over 177 accents in c40, -14.0 in c35 and -14.5 in c12. The c12 note in `build/score_config.py` measured -4.2 dB on a real orchestra, and MANUAL-GAPS #1 sets a target of -6..-2 dB with a ceiling of +3.
- **Re-attacks.** At repeated-note re-attacks the 2-5 kHz energy in the first 60 ms rises only +0.4 (winds), +0.8 (strings) and +1.1 dB (brass) over the 80 ms before. The separation therefore rests on the level dip alone. In the master, other parts doubling the pitch and the hall fill that dip, which is why exposed string repeats keep a master dip of 2.1 dB while their stems dip 4.4 (S1). The causal link is inferred.
- **Item 8 still has room** (measured): brass front max +3.2, master 2-5 kHz jump p90 +0.7 dB.

**Manual.**
- p.101: the "Marc Sus LITE" row (Sustain Marcato) gives a marcato attack "not as forceful" as Sustain Accent, with velocity setting a low-pass cutoff on the attack, so a soft velocity gives a darker front.
- p.106: Legato Slur Accent MAX, where velocity sets the accent's strength.
- p.62-63: LITE rows have about half the layers.

**Fix (MANUAL-GAPS #1 as written, in the second pass).**
1. **Test aliases** (left out of the sum), on "Marc Sus LITE" over bars 32-33 (qn 124-132) and 142-143 (564-572):
   - Trombones 1-2, Bass trombone and Horns 1-4 (or Horns a2 where they play a2);
   - velocity 45-70 from the printed dynamic (filter mostly closed; avoid the top velocities, p.102);
   - CC1 from `CC1_DYN_MAP`, no CC11 bump;
   - the GENTLE_ACCENT swell cut to about +1 dB;
   - `fit_accents.py` refit on the test stems.
2. **Pass criteria per accent:**
   - 2-5 kHz front minus body -6..-2 dB, never over +3;
   - the master's 2-5 kHz jump under +3 dB with the test stem substituted;
   - level over same-dynamic neighbours 2-4 dB.
3. **Then.** If it passes, extend family by family, with accents inside slurs on "Leg Slur Accent MAX" at low velocity. Run the same A/B for the string accented quarter strokes of bars 131-138 on "Sus Marc LITE", taking its level step from the body (KIT §20, c23-c24). Keep GENTLE_ACCENT as the fallback: Dan has not heard an accent with a front yet, and the harsh limit (+7..+13 dB) must stay far away.

### 3. Winds and brass are dry point sources in a roomy hall; the solos never use the Mid mics the manual's Soft mood pairs with such passages (measured symptom; fix inferred)

**Where.**
- Every passage with winds or brass.
- Most audible in the exposed solos: Cor anglais espr. bars 5-8, Bassoon 1 bars 33-35, Clarinet 1 dolce bars 45-46, Flute 1 espr. bars 73-76, Bass clarinet bars 77 and 107, Oboe 1 bar 145, Cor anglais bars 171-174, Clarinet 1 bar 175.

**What is wrong (measured).**
- **Top-octave width.** Master L/R correlation 4-8 kHz 0.538 and 8-16 kHz 0.617 in c40, against 0.38-0.48 above 4 kHz in the references (Dvořák 8-16 kHz 0.295).
- **Point-source stems.** At width 0.05 the wind, Horn 1-4 and Trumpet 1 stems correlate 0.75-0.90 in 1-4 kHz and 0.99-1.00 in 8-16 kHz. `apply_mix()` gives the spaced Main pair the same pan as the Close mic, so it collapses to a point (c39 C #3, measured on c38; widths unchanged since).
- **Close-mic sound.** The winds have the driest early tail of any family: -9.1..-13.6 dB at 0.15-0.25 s after a phrase end, against horns -5.5..-8.2 (c39 C). The woodwind Main samples sit 11-40 dB under Close (KIT §12), so Close 0.5 / Main 0.8 is still a close-mic sound.

**Manual.**
- p.136: Classic = the Main mix, "well-balanced, unified"; Soft = Mid + Surround "for slower, more emotional passages", "definition and depth".
- p.138: Mid gives "definition without the sound of close proximity".

**Fix (one rebuild cycle in c42-c45, both sessions; memory neutral).**
1. **Per-mic width.** c39 C #3's `width_by_mic` in `apply_mix()`: `w = m.get("width_by_mic", {}).get(label, m["width"])`, with `{"Close": 0.05, "Main": 0.35}` on the wind, horn, trumpet and lowbrass groups, the a2 tracks, Clarinet 2, Contrabassoon, Bass clarinet and Trumpets 2-3 (so pairs match).
2. **Mid swap test.** The same render tests the swap on Flute 1, Oboe 1, Clarinet 1 and Cor anglais as aliases in pass 2: `"mics": {"Mid": 0.5, "Main": 0.8}`, `width_by_mic` Mid 0.15 / Main 0.35, gains re-matched to the same K-weighted level. Optionally the Cor anglais coda solo (683-695) can also be played on "Leg Slur Exp" (MANUAL-GAPS #5, p.109).
3. **Targets:**
   - stem correlation 1-8 kHz 0.6-0.8, master above 4 kHz ≤ 0.50;
   - per-note R-L SD ≤ 1.2 dB (c35 method);
   - wind early tail toward -7..-9 dB;
   - the solos' 2-5 kHz level against the strings within 2 dB of c40;
   - K-weighted track levels within ±0.5 dB.
4. **Hall envelope (c39 C #4).** Leave it out unless its decay is re-measured first. My cut-off method reads t-20 at 0.52-0.54 s at qn 55 and 679 in c40, close to the Brahms 0.485 s that c39's method measured (c39 measured 0.62 / 0.74 s on the same stops). The two methods disagree, so run one method on the mockup and the references before changing the IR.

### 4. Bar 62's sub. p still cuts the forte's hall: the post-hall envelope falls 13-16 dB within 0.35 s on the violins (measured; fix inferred)

**Where.** Bar 62 (qn 244), on Violins I/II, Horns 2-3, Clarinet 1 and the celli/basses (parts.json `subito_falls`). Bar 84 (qn 332) has smaller drops on the celli and basses.

**What is wrong (measured).**
- **The fall is still faster than a release.** The master falls -8.6 / -10.6 / -13.3 dB over 0-0.05 / 0.05-0.1 / 0.1-0.2 s, against -3.1 / -4.5 / -8.1 at the tutti fermata release at qn 679 (S3 table).
- **Why.** The track envelope, which acts after the Opus hall, sits at +12.2 dB (Violins I), +13.3 (Violins II), +8.4 / +8.9 (Horns 2 / 3) and +7.4 (Clarinet 1) at qn 243.7. This is the crescendo's hpgain (2-3 dB) plus roles and trims. At 245 it is at -3.0 / 0.0 / -3.0 / -2.05 / -3.0 dB. SUBITO_TAIL (`build_reaper.py`, at_once 4 dB, ramp 0.35 s) splits that 13-16 dB drop but still completes it in 0.35 s. The hall return of the forte notes therefore falls 13-16 dB in 0.35 s, where the hall itself would fall about 5-8 dB (the fermata profile).
- **Dan's criterion.** His note asked for the forte's ring to decay under the p (cycles/c36/reports/DAN.md). It now decays, but about twice as fast as a release.

**Fix.**
1. **Move the subito drop before the hall.** In `build_reaper.py vol_points()`, for each `subito_falls` entry:
   - write the drop (pre minus post, in dB) as a CC7 step at the fall qn (CC7 is pre-hall and leaves the hall tail alone: Results c36, measured);
   - keep the post-hall envelope at its pre-mark value, then ramp it down to the post value over 1.5 s;
   - ramp CC7 back up over the same 1.5 s, so the new p notes' direct level stays as now from their onset.
2. **Check.** At bar 84 first (two tracks), then bar 62. Bar 62 profile: 0-0.2 s within 2 dB of the fermata release. The new p notes within 1 dB of c40 from +0.3 s. The c36 blip (243.4-244.0) no higher than +4.2 dB re the forte.
3. **CC7 curve.** Read it from the c36 CC7 test (-12 dB at a known value), or measure it once on a held note.

The fall itself can be simulated first, as a level-only change on the c40 stems. The CC7 half needs the render.

## Order of work for the next block (inferred)

The main session has no memory left (item 9), so Findings 1-3 test new states, rows and mics as aliases in the second pass. Each alias is an A/B against the main render's own stem on the same notes, and is left out of the sum until adopted.

1. With c41's Violins I rebuild: the aliases for Findings 1 and 2.
2. In the next render: adopt what passed, with the main-track rebuilds and refits.
3. A later cycle: the space rebuild (Finding 3) in both sessions at once.
4. Finding 4 is independent and small; it can go into any cycle.

## Do not touch

- The movement's dynamic plan (bar level r 0.81 against the printed dynamics, unchanged in shape since c00).
- AUTO_REBOW with the fitted re-bow, breath and restrike shapes (no held note loops).
- GENTLE_ACCENT as the default and the fallback for Finding 2.
- REP_ROW with REP_ROW_GAP_S (0.06, 0.15) and the wind/brass re-tongue settings (S1 met for winds and brass).
- SUBITO_FRESH / SUBITO_TAIL.
- The timpani roll levels and TIMP_CC1_MAP (rolls 9-16 dB under the master).
- The delivery ride with RIDE_TRIMS and the climax order (160 > 122 > 167-170 > 26).
- The DIV A coda solo as fitted.
- The c36-c40 climax set.
- Every per-onset table on notes the findings above do not change.
