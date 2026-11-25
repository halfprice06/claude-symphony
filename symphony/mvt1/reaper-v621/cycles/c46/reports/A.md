# Cycle 46, critic A: articulation and phrasing (render c45, score v621)

## Method

All measurements are on the final c45 stems and master (`cycles/c45/render`, 40 stems, stem-fixed), placed with `build/parts.json` (written 15:25, one minute before the final stems; it is the state the stems carry). Comparisons with c44 use `cycles/c44/render` with `cycles/c45/before/parts.json`.

Measures (scratch scripts deleted after the run, as the brief asks):
- **pcX**: `tools/pcx.py attack_pcx`, ms after the score onset. Legato targets exclude the previous pitch; repeats use no exclusion. 0..+15 ms is "on the beat" for this estimator (harp +5, staccato rows +1..+13).
- **Crossover**: `pcx.pair_window`. Synthetic instant-switch error per join: `pcx.synth_switch`.
- **Join dip / burst**: 30 ms stereo power. Dip = lower body minus the minimum in [moved onset - 0.03, score onset + 0.15 s]. Burst = maximum in that window minus the louder body. 779 monophonic legato joins (`pcx.legato_joins`).
- **"Time under body"**: how long the pitch band stays more than 6 dB under the note's body (+0.3..+0.6 s) inside [moved onset - 0.1, score onset + 0.3 s].
- **rel**: stem minus master over the note's first 0.3 s.
- **Envelope simulations**: scale the stem by a volume-envelope difference. The envelope sits after the Opus hall, so these are exact for level-only changes.

Labels: **measured** (render or parts.json), **read** (code, config or patch file), **inferred** (reasoned, not tested).

## Manual notes (second round: c40 slot A's pages, 2021 manual PDF pp. 82-88, Hollywood Solo Cello, read again in full; MANUAL-GAPS.md and DIGEST.md read)

**MANUAL-GAPS items still open in this lens:**
- **#3 Solo Cello:** still not installed (`ls "/Volumes/MAC DRIVE/"`: no Solo library).
- **#5 expressive wind rows:** untried.
- **#9 horn portato rows:** untried.
- **#1 brass accents on Marc Sus LITE:** not needed. Brass accent fronts are dark: 2-5 kHz in the first 80 ms minus the body, median -16.4 dB, p90 -8.1, n 146 (measured).

On this reading I also used p.91-92 (Détaché, Marcato Sustain) and p.99 (Legato Slur Staccato) for finding 2.

| Manual (PDF page) | c40 A's note | Now (c45 render) |
|---|---|---|
| p.82: Solo Cello mics are made for one instrument (vintage Close/Mid instead of Surround/Vintage) | No: the section KS Master played the solo; image corr 0.74 | **Partly followed** (measured). Since c40 the solo plays on Celli KS Master DIV A, Close only (pass 2). L/R correlation over 680-696 is now 0.96 (cor anglais 0.79, celli section 0.77): a single-player image. Solo Cello is still not installed. |
| p.82: on Solo Cello CC1 sets dynamics and vibrato together | Matters only for a Solo Cello track | **n/a, correct for the patch in use** (read). DIV A takes CC1 70 -> 105 over the first phrase (vibrato) and CC11 61-74 (dynamics). A Solo Cello track would need CC1 from the printed dynamic. |
| p.82-84: Long Solo legato script | n/a | n/a |
| p.83-85: Lyrical Vibrato, Sus Exp, NV/VB types | Not available | Not available |
| p.86: Legato Bow Change accents the second note; p.87: BC Smooth gives a soft non-slurred attack | Partly: 684 / 688 / 692 on Leg BC MAX v124 | **Followed as far as HS allows** (measured). The bow changes now play at v70. Dips 3.6 / 4.8 / 1.7 dB, bursts -0.2 / +1.1 / +2.3 dB: no accented bow changes. |
| p.87: Legato Slur suits slow-medium tempos; velocity sets transition timing | No: every target at v124 | **Velocity followed** (v70 since c40, `LEG_VEL_SPANS`). **Timing not followed.** The per-onset leads were fitted in c40 with the old m37 estimator and never refit on pcX: 690 / 694 / 687 / 684 sound +156 / +153 / +89 / +63 ms late, 685 / 691 / 680 -93 / -62 / -93 ms early. See **finding 1**. |
| p.86-87: Solo Cello has no portamento patch | 685 would be a slow Legato Slur | 685 is still on Leg Port MAX at v100. The glide lands early (pcX -93 ms, crossover -132 ms). Finding 1. |
| p.87-88: LegSus Slur reads CC1 at note start | n/a | n/a |
| p.88: KS Master | n/a | n/a |
| p.91-92 (new on this reading): Marcato Sustain plays a marcato sample over the sustain samples, "extra power at the start of the note"; Détaché is separated, has a defined end, is not loopable, and may be cut short | | Read in the patches: see finding 2. |
| p.99 (new): Legato Slur Staccato adds a slur-staccato accent to notes with no legato connection: "the first note of each legato phrase" gets "a slightly stronger attack" | | The library's own answer to the late strokes (finding 2) and the weak slur heads (finding 5). Never tried for this. |

## 1. The coda "Solo espr." cello is the most exposed string line, and four of its notes sound 63-156 ms late and three 62-93 ms early. Its leads were fitted with the old estimator and never refit on pcX (S2; measured)

**Where.** "Cello solo" (pass 2, Celli KS Master DIV A), bars 171-174, qn 680-694. The line sits 0.5-1.7 dB under the whole master (rel), so nothing covers it.

**What is wrong (measured, c45 stem).** Per note: pcX / crossover (the two agree), with the realized lead.

| Note | Step | Lead (s) | pcX (ms) | Crossover (ms) |
|---|---|---|---|---|
| 680 | entry | 0.30 | -93 | |
| 683.5 | | 0.12 | -12 | -10 |
| 684 | | 0.05 | **+63** | +108 |
| 685 (Leg Port MAX) | | 0.27 | **-93** | -132 |
| 687 | | 0.155 | **+89** | +93 |
| 688 | | 0.065 | +49 | +59 |
| 689.5 | | 0.20 | -16 | -50 |
| 690 | E-flat4 -> C-sharp4 | 0.03 | **+156** | +164 |
| 691 | | 0.25 | **-62** | -70 |
| 691.5 | | 0.12 | +16 | -2 |
| 692 | | 0.12 | +1 | -8 |
| 694 | C5 -> B4 | 0.03 | **+153** | +204 |

- The synthetic instant switch reads -4..+4 ms on every one of these joins, so the estimator is not the cause.
- **Robust SD 70 ms**, against 42-55 ms for the string sections' legato.
- The values agree within 13 ms in every render from c40 to c45 (measured on each cycle's stem). They were never right on pcX.
- **Why.** The c40 actor fitted the leads on the m37 "pc" ("targets within -0.04..+0.09 s"). c42 showed that m37 shares partials between the two pitches (read: `build/score_config.py` c40 comment; HISTORY c42-c43: "Cello solo leads (DIV A fit kept)").

**Fix** (`build/score_config.py`, `ALIAS_TRACKS["Cello solo"]["tables"]`). New lead = realized lead + 0.9 x (pcX - 0.015 s), the c45 stroke rule. `LEG_LEADS` is relative to the alias's `LEG_LEAD_S` 0.12:

| Onset | Now | New |
|---|---|---|
| 684.0 | -0.07 | -0.03 |
| 685.0 | +0.15 | +0.07 (the full rule says +0.05; keep some anticipation for the glide) |
| 687.0 | +0.035 | +0.10 |
| 688.0 | -0.055 | -0.02 |
| 689.5 | +0.08 | +0.05 |
| 690.0 | -0.11 | +0.04 |
| 691.0 | +0.13 | +0.06 |
| 694.0 | -0.09 | +0.03 |

- `ENTRY_LEADS` 680.0: 0.24 -> 0.14.
- Leave 683.5, 691.5 and 692.
- **Caps.** 690's lead (0.16 s) stays under 0.45 of 689.5's 0.42 s slot.
- **Level shapes must move with their notes** (read). `_DIVA_CONTOUR` and `_DIVA_JOINS` carry crossfade points at the old moved onsets, e.g. 689.964 = 690's moved onset and 693.964 = 694's. Move each by its lead change in qn (q = 72: 0.1 s = 0.12 qn), and check the `LEG_RAMP_WARN` and `LEAD WARNING` lines.

**Targets.**
- Every solo note's pcX within ±40 ms of +15 ms; robust SD under 45 ms.
- Join dips still ≤ 5 dB and bursts ≤ 3 dB on the pass-2 stem.
- 687's burst (+3.2 dB now) not raised.

## 2. Celli 152 / 156 and Violas 372 stay late for two reasons: a note-trim step anchored at the score onset (an envelope cause, fixable by stem fix), and a slow mf Sus MAX bow start. The KS Masters have two rows built for a faster re-articulated start (S1, S2; measured and read)

**Where (strokes, `rep_strokes` class "stroke").**
- **Violoncellos:** 47, 84, 88, 152, 156, 164, 448, 456 (bars 12, 22, 23, 39, 40, 42, 113, 115).
- **Violas:** 372 (bar 94).

These are long notes: whole notes in a crescendo (celli 148-156), a dotted half (Violas 372). Celli 374 and 668, which are mf-f, are fine.

**What is wrong (measured, c45 stems).**
- **pcX.** Celli 152 +118, 156 +82, 448 +63, 47 +60, 164 +58 ms; Violas 372 +88. The time under body is 225 / 300 / 185 ms for celli 152 / 156 / 448 and 165 ms for Violas 372.
- **The band at the beat.** At celli 152 the band is still 10 dB under the body at -0.02..+0.06 s, -6 dB at +0.10 s and -2 dB at +0.18 s. The note-on is 0.19 s before the beat.

**Cause A (envelope; read and measured).** `tools/score_to_parts.py` `trim_shape`, last branch: a note trim that is not a legato pitch trim starts at `q0`, the score onset (`a0, a1 = q0, q0 + ramp`). The stroke trims in `build/note_trims.json` are positive with 0.1 s ramps (`NOTE_TRIM_RAMP_S`, c44 B #5): celli 84 +2.4, 88 +2.8, 152 +5.0, 156 +5.5, 448 +1.8. So each stroke plays its first 0.2-0.3 s at the previous note's level.
- **Celli 152** (`vol_db`): +2.0 dB to 152.0, then +7.0 at 152.21.
- **Celli 156** is worse. The 152 trim ends at 156's moved onset (155.551-155.631: -6.5 dB). 156's own trim only starts at 156.0. So 156's lead window sits in a 6.5 dB envelope hole: 5.9 at 155.55, -0.6 at 155.63, +0.5 at 156.0, +6.8 at 156.21.

This is why "more lead did not move it" in c45.

**Cause B (samples; measured and read).** The Celli and Violas Sus MAX mf layer (CC11 under about 94) starts slowly, and lead cannot shorten that. Time from note-on to -6 dB of the peak:

| Section | mf entries (CC11 72) | f entries (CC11 88-114) |
|---|---|---|
| Celli | 0.20 s (56) | 0.05 s (128) |
| Violas | 0.21-0.24 s (65.5, 253, 257, 261) | 0.03-0.11 s (521.5-535.5, 552) |

The AHDSR attack is only 6-43 ms, so the slow start is in the recording (patch).

**Simulation of a fix for cause A** (level only, on the c45 stem): start each positive stroke trim at its moved onset.

| Celli stroke | Time under body (ms) | Front re body (dB) |
|---|---|---|
| 152 | 225 -> 45 | -7.0 -> -3.6 |
| 84 | 140 -> 70 | |
| 88 | 80 -> 0 | |
| 448 | 185 -> 130 | |
| 156 | 300 -> 285 | (cause B dominates) |

Violas 372's trim is negative (-1.5), so cause B alone acts there.

**What the library offers (read: patches and manual).**

| Row (KS Master) | What plays | Measured in this render | Fit for an unaccented re-bow |
|---|---|---|---|
| **"Stac Leg BC + Slur + Port MAX"** (Celli, Violas; p.99 Legato Slur Staccato) | Notes with no legato connection play the same Non Vib / Sus Vib / Molto Vib samples as Sus MAX at their normal 12-23 ms AHDSR. A "Stac Hrd" group is layered on top: velocity -> volume intensity 1.0, A 20-26 ms, D 489 ms, S 0. Connected notes play the BC / Slur / Port transitions. | Never used for strokes. c16 used it on viola sextuplets (clarity only). | **Best candidate** (inferred). A front scaled down to nothing by velocity fills the slow bow start, and the body is the MAX sustain the neighbours use. |
| **"Sus Marc LITE"** (p.91-92; already in `STR_STROKE_ROWS`) | A marcato short (Celli velocity intensity 0.6, so the front can only drop about 8 dB; Violas 1.0) over LITE sustains faded in over 240 ms (Celli) / 260 ms (Violas). | Speaks on the beat (Violins I / II 328-566 at v111: pcX -41..+47 ms, -6 dB 26-113 ms after note-on). But the front is 7-14 dB over the body at v103-111 (celli 284 / 285 +7..+11 dB at +0.06..+0.18 s; Violins I 328 +14). | Second candidate, at low velocity. Bite risk on the celli. |
| "Detache" (p.91) | Celli and Violas: mp and ff only, RR x2, sample start trimmed 1935-3808 samples. Basses: mp only. Not loopable. | Not used. | Not for whole notes. Maybe for quarter-note portatos. |

**Fix.**
1. **Generic, level only (stem-fixable; simulate first).** In `tools/score_to_parts.py` `trim_shape`, start a note trim at the moved onset when all of these hold:
   - the trim is positive;
   - its ramp is 0.15 s or less (`NOTE_TRIM_RAMP_S`);
   - the note is not `joined_in`;
   - `new_on(n) < n["qn"] - EPS`.

   Use `a0 = new_on(n) - 0.01`, `a1 = a0 + ramp`, behind a new option, e.g. `NOTE_TRIM_FROM_MOVED = True`. Leave negative trims and 0.6 s bloom ramps as they are: they must let the attack through. On the main tracks this changes only celli 84 / 88 / 152 / 156 / 448 (plus Violoncellos 340 +3.0 and Horn 1 413 +5.0; check those two). Apply with `stem_fix.py`.
2. **A/B in pass 2** (one render, `TEST_TRACKS`, as in c41 / c45): "Vc stroke A" / "Vla stroke A" are aliases of Violoncellos / Violas over (0, 730).
   - Rows: `ART_SPANS` on the stroke onsets (celli 47, 84, 88, 152, 156, 164, 448, 456; Violas 372, its span covering the slur to 378) to "Stac Leg BC + Slur + Port MAX".
   - Velocity: `vel_by_cc` [(60, 40), (90, 50), (120, 60)].
   - Add the row to `STR_STROKE_ROWS`, so the strokes keep their timing and leads.
   - Optionally "Vc stroke B": "Sus Marc LITE" with `vel_by_cc` [(60, 25), (90, 35), (120, 45)].
   - Run it with the step-1 envelope.
   - Watch the c05 keyswitch guard: the row is a legato row by name (`_lg`).

**Pass criteria.**
- Time under body ≤ 90 ms.
- Front (moved onset..+0.10 s) within -3..+2 dB of the body.
- 2-5 kHz in the first 80 ms minus the body ≤ -3 dB (Dan: weight, not bite).
- Stem dip before the stroke still ≥ 6 dB.
- pcX within ±40 ms of the section's legato median (+6 celli, +12 violas).

Keep the variant only where all pass. It costs one row per instance in the main project (inferred 0.1-0.3 GB).

## 3. Exposed legato transition spikes: one new in c45 (the only c45 fill that overshoots), one old and unnotched in the f theme (measured)

**Check of the c45 fills (coordinator).** I measured all 33 changed `early_fills.json` entries and Clarinet 1 224's shape on both renders: dip, 200 ms and 30 ms overshoot over the louder body (`fillsim45`'s definitions).
- **One overshoots: Bassoon 1 375** (bar 94; F3 -> A-flat3, Leg Slur MAX v60).
  - c44: dip 5.4 dB, over200 +1.2, over30 +2.9.
  - c45: dip 1.9, over200 **+5.6**, over30 **+7.4**.
  - rel -12.8 -> **-5.3 dB**: the bassoon jumps out of the texture for 0.2 s.
  - Cause. The stem is 9-11 dB louder than c44 at +0.05..+0.15 s, against a +1.5 dB envelope change. So most of the burst is a new transition state after the c45 full rebuild of the wind tracks (`width_by_mic`). The fill raise (2.6 -> 4.1 dB) adds 1.5 dB on top.
- **Bass clarinet 700** (new 2.3 dB fill): over200 +3.1 (+2.6 without it in c44). Marginal.
- Every other changed fill is at or under +2.4 dB (200 ms). The fills worked: Oboe 1 582 dip 5.0 -> 3.2, Clarinet 1 517 6.1 -> 2.3, celli 413 6.4 -> 1.5, Clarinet 1 224 5.8 -> 2.9 with its overshoot gone.
- Joins with removed fills still burst from the sample itself: Oboe 1 579 (+2.4 / +5.5), celli 358 (+3.7 / +5.6), celli 672 (+4.0 / +7.0, with a 7.6 dB dip after it).

**The exposed unaccented spikes in c45.** Bursts at accented targets are the gentle-accent swells and are left out.

| Join | Burst (dB) | rel (dB) | Mark | Since |
|---|---|---|---|---|
| Violins I 70 (bar 18, G4 half note after slurred eighths, f) | **+8.0** | -2.8 | none | c44 and earlier, identical audio |
| Violas 78 | +6.9 | -4.8 | slur end, f | |
| Violas 290 | +4.4 | -2.8 | pp | |
| Violoncellos 416 | +7.5 | -5.2 | | |
| Violas 81 | +6.2 | -7.9 | | new in c45: -0.4 dB dip -> +6.2 burst |
| Violins I 496 | +7.4 | -7.6 | | new in c45: +3.2 -> +7.4 |

Violins I 70's spike lasts 30-50 ms at 0.03 s after its moved onset (-26.3 dB against -33..-36 around it). No `JOIN_NOTCH` or shape covers it (read in parts.json `vol_db`).

**Fix** (`build/score_config.py` `JOIN_NOTCH`, (qn from, qn to, dB); level only). Spans are measured on the c45 frames as the core of each burst (frames within 4 dB of the peak), depth = peak - 2 dB:
- **Violins I** (69.604, 69.793, -5.9): peak +7.9 dB at -0.149 s. Its audio repeats exactly between renders.
- **Bassoon 1** (375.011, 375.437, -4.5): peak +6.5 dB at +0.125 s. Also put the 375 fill back to `{"db": 2.6, "pre_s": 0.0, "hold_s": 0.18}` (`early_fills.json`).
- **Violas** (77.723, 78.112, -4.9) and (290.010, 290.147, -2.4).
- **Violas 81:** replace the existing (80.72, 80.88, -2.5) with (80.590, 80.842, -4.2). The c45 burst peaks at -0.155 s, ahead of the old notch.
- **Violoncellos** (415.511, 415.850, -5.5).
- **Violins I** (495.675, 496.167, -5.4). This core is wide, so check it does not cut the fff body.

Simulate each on the c45 stem with the `stem_fix.py` path before writing. After the render, re-list joins with burst ≥ 5 dB and rel > -8 dB.

**Target.** No unaccented exposed join (rel > -8 dB) bursts more than 4 dB.

## 4. Violins I entries after rests speak late at mf and f, while Violins II with longer leads land on the beat (S2; measured)

**What is wrong (measured, pcX median by CC11 band).**

| | mf (CC11 51-80) | f (CC11 81-127) |
|---|---|---|
| Violins I | **+52 ms**, lead 0.12, n 9 | **+35 ms**, lead 0.06, n 27 |
| Violins II | -8 ms, lead 0.18 | +5 ms, lead 0.12 |

The same pattern holds for the violas at mf (+16) and the celli at f (+24).

The late Violins I entries (pcX ms, rel dB):
- **mf:** 88 (+72, -11), **136.5 (+68, rel -4: exposed)**, 286 (+89), 536 (+105), 619 (+79).
- **f:** 112.5 (+39), 127 (+45), 322.5 (+47), 472.5 (+68), 474.5 (+70), 521 (+55).

A few f entries are early: 56.5 -45, 568.5 -43 (the downbow pickups of bars 15 and 143).

**Fix** (`build/entry_leads.json`, per onset, extra s = 0.9 x (pcX - 0.015), the c45 rule).
- **Violins I, add:** 88 +0.05, 136.5 +0.05, 286 +0.07, 536 +0.08, 619 +0.06, 112.5 +0.02, 127 +0.03, 322.5 +0.03, 472.5 +0.05, 474.5 +0.05, 521 +0.04, 529 +0.02.
- **Violins I, remove lead:** 56.5 -0.05, 568.5 -0.05.
- **Leave** 707 (pp, +153 ms: check its first 0.3 s shape before adding lead, KIT §6).
- **Do not raise `ENTRY_LEAD_S` for the whole section.** The f entries straddle zero (56.5 / 552.5 / 568.5 are early).
- **Check the `LEAD WARNING` lines.** Every listed onset must take its lead.

**Target.** Violins I entry median within ±20 ms of +15, none of the listed ones beyond ±50 ms.

## 5. Short Sus MAX slur heads are weak: the first note of a slurred pair or group drops 5-10 dB under the note it leads into (articulation, S2; measured)

**Where and how much.** String notes on Sus MAX of 0.08-0.30 s that a legato note of another pitch follows (slur heads, `SLUR_START_SUS` / short_sus). Broadband level of the head minus the next note's first 0.3 s, stem:

| Section | n | Median |
|---|---|---|
| Violins I | 15 | **-3.9 dB** |
| Violoncellos | 8 | **-4.9 dB** (band -7.5) |
| Violins II / Violas | | about 0 |

The worst (dB under the next note, rel dB):
- **Violins I:** 259.5 (bar 65) -9.2 / rel -7.7; 146.5 (bar 37) -8.9; 377 (bar 95) -7.4; 66.5 (bar 17) -5.6 / rel -8.4; **61 (bar 16, the theme's upbow B4) -4.6 / rel -3.6**.
- **Celli:** 419.5 (bar 105) -9.8; 355.5 (bar 89) -8.8; 533.5 (bar 134) -6.3.

An upbeat a little lighter than its downbeat is normal (about -2..-3 dB). Five to ten decibels under it means the note is barely heard.

**Why (inferred).** The same slow mf Sus MAX start as finding 2: a 0.09-0.12 s note ends before the sample reaches its body. Violins I's 58.5 D5 at f measures -39.8 dB against -33.0 / -33.8 for the notes on either side.

**Fix.**
- **Level only (stem-fixable).** `PICKUP_LIFT` per onset (exact lift from the pickup's moved onset to its target's moved onset), aiming at -2..-3 dB under the next note:
  - Violins I 259.5 +6, 146.5 +5, 377 +4, 66.5 +2.5, 61 +2, 58.5 +3;
  - Violoncellos 419.5 +6, 355.5 +5, 533.5 +3.5.
- **Better, if finding 2's A/B passes.** Play these heads on "Stac Leg BC + Slur + Port MAX". The manual describes it for exactly this case ("the first note of each legato phrase ... a slightly stronger attack", p.99), and the slur's next note then joins on the same row. Then the lifts are not needed.

## 6. The Violins I portato tenutos (bars 16, 144): the c45 measure included the next note's attack; on the corrected window only 60, 140 and 108 are still over target (coordinator's open item; measured)

**What changed in the measure.** c45's body window (+0.15..+0.42 s from the tenuto) contains the front of the next note: Violins I 61 is a Sus MAX upbow with a 0.10 s lead, starting 0.376 s after 60's score onset. The "body peak at +410 ms" is that note. I measured again with:
- the body over [moved onset + 0.10 s, next moved onset - 0.02 s];
- the next pitch excluded from the band.

**Now (c45; tenuto body re its eighth's peak / median, front re the eighth's median).**

| Tenuto | Body re eighth peak / median | Front re eighth median |
|---|---|---|
| Violins I 60 | **+3.4 / +4.0 dB** | +0.6 |
| Violins I 572 | **+2.0 / +3.8 dB** (on target) | +0.5 |
| Violins I 140 | **+3.9 / +3.7 dB** | +0.9 |
| Violins I 108 | **+2.9 / +3.8 dB** | +0.3 |
| Violins II 108, Violas 108 / 668, celli 524 | within -0.8..+2.2 dB | |

c44 had Violins I 60 at +8.0 and 140 at +8.8, so the c45 shapes did most of the work. The fronts now open at the eighth's level (+0.3..+0.9 dB), so the remaining excess is the sample's rise within the first 0.1-0.3 s.

**Fix** (`build/score_config.py` `LEVEL_SHAPES_S`, body part of the c45 `_portato` rows, from +0.14 s to the next moved onset; level only):
- Violins I 60: -3.0 -> -4.5.
- Violins I 140: -2.0 -> -4.0.
- Violins I 108: add a body of -1.0.
- Leave 572.

**Target.** Body within -1..+2 dB of the eighth's peak.

## Standing checks (measured)

**S1, repeated notes.** 881 written repeats (gap ≤ 0.5 qn, not tied), pitch-band dip, stem / master medians:

| Family | Repeats | Stem dip (dB) | Master dip (dB) |
|---|---|---|---|
| Strings Sus -> Sus | 395 | 4.2 | 1.6 |
| Winds | 164 | 5.0-15 | 1.4-5.5 |
| Brass | 210 | 3.8-9.8 | 2.7-5.4 |

- **Exposed repeats (rel > -8 dB) with a master dip under 3 dB: 19.** Most are on the repetition rows with the same pitch doubled in the master (Bass clarinet 308, Bassoon 1 stac 352: stem 5.2 / 7.5 dB).
- **The basses' ff eighth pedals** (`REP_SPLIT` strokes with 14 ms gaps), stem / master boundary depth:
  - bars 27-32: 4.0 / 2.0 dB;
  - bars 139-142: 4.9 / 1.4;
  - bars 167-169: 4.0 / 3.2;
  - bars 131-134: 7.1 / 3.4.
- **The celli's sixteenths in bars 127-130:** 4.6 / 2.1 dB.
- **A simulated extra -4 dB `STR_REP_DETACH` dip** (0.09 s) takes the basses' stems to 7.2-8.4 dB but the master only +0.2 dB. Contrabassoon, tuba, horns and the timpani roll sound the same pitch classes in those tuttis. I do not recommend it unless Dan names these passages.

**S2, perceived attack** (pcX median / robust SD / share more than 60 ms late):

| Family | Class | Median (ms) | Robust SD (ms) | > 60 ms late |
|---|---|---|---|---|
| Strings | legato | +14 | 51 | 17% |
| Strings | entries | +11 | 41 | 14% |
| Strings | re-attacks | +12 | 64 | 24% |
| Winds | legato | +17 | 32 | 16% |
| Winds | re-attacks | +14 | 33 | 16% |
| Brass | all classes | -9..+7 | 22-33 | 2-9% |
| Timpani | strokes | +14 | 7 | |
| Harp | | +5 | 7 | |

- **The outliers that matter:** findings 1, 2 and 4.
- **Bassoon 1** legato at f is +42 ms (n 27) and Bassoon 2 re-attacks +40 ms. Both are buried (rel -7..-20 dB), so lower priority.

**Strokes and sus-gap repeats** (c45's leads). Strokes median +44 ms, 8 of 15 more than 60 ms late (finding 2). Sus-gap repeats +25 ms, 5 of 23 late.

**Item 8 (accents).** 2-5 kHz in the first 80 ms minus the body:
- winds -11.5 dB median (p90 -4.5);
- brass -16.4 (p90 -8.1);
- strings -9.5 (p90 -3.0).

Five accents in all are over +3 dB, all buried. The master's 2-5 kHz jump at accents is -2.5 dB median (p90 +2.5). Weight, no bite.

**Item 7 (loop pulse).** Master 100-300 Hz / centroid autocorrelation at 3.95 s:
- final chord 712-728: 0.06 / -0.02;
- Lento 0-40: 0.04 / -0.09.

No loop pulse.

**Legato joins overall** (c44 -> c45):

| Family | Median dip | Joins ≥ 6 dB | Bursts ≥ 5 dB |
|---|---|---|---|
| Strings | 2.6 -> 2.6 | 28 -> 23 | 58 -> 57 |
| Winds | 2.5 -> 2.5 | 25 -> 19 | 24 -> 22 |
| Brass | 1.4 -> 1.4 | 2 -> 3 | 4 -> 2 |

19 joins worsened by 3 dB or more and 13 improved (finding 3 lists the exposed ones).

**Keyswitches and chords** (parts.json). No keyswitch lands less than 9.5 ms before its note, and no chord is sent to a legato row on any track.

**S3.** Bar 62 is unchanged from c44 (c45 CHANGES); not re-measured.

## Do not touch

- The pcX tooling and the probe's legato check.
- `REP_ROW` repetition rows with the c38 gap rules.
- `STR_REP_NEW_BOW`'s classification and gaps.
- The c45 retongue_leads rows: refit only the stroke onsets named in finding 2 after its test.
- `GENTLE_ACCENT` and `accent_fits.json` (fronts dark, no bite).
- The pass-2 wind staccato windows.
- `TIMP_RH_ALT`, the harp ring and damp settings, and the timpani roll settings (struck attacks within ±7 ms robust SD).
- The c45 fills other than Bassoon 1 375: Oboe 1 582, Clarinet 1 517 / 178 / 224, celli 413 / 372 / 402 measured with no overshoot.
- The Violas `rt_gain_db` -6.
- The 150 / 237 ms release caps.
- The hall values and every send.
- The Cello solo's DIV A patch, v70 legato velocity and level contour: move the contour points with the new leads, do not refit the levels.
- Every c45 and earlier do-not-touch item.
