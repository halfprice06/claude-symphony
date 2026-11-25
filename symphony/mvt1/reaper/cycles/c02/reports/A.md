# Cycle 2, critic A: articulation and phrasing (render c01)

Scope: every wind, brass, string, timpani and harp note in `build/parts.json`. Each note's articulation is read from its track's keyswitch lane and measured on the c01 post-fader stems (stereo power) and the master, at score onsets (`sq`) on the parts.json tempo map. Where it helps, c00 is shown for comparison. The scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c02-A/`: lib.py, accs.py, sus2leg.py, sus2leg2.py, downbow.py, timproll.py, loopdet.py, longloop.py, stac.py, rebow2.py, rebow3.py, masteracf.py and env.py.

## Checks that passed (measured)

- **Legato structure.** No chord and no simultaneous note reaches a legato row on any track. There are no same-pitch overlaps.
- **Brass and wind accents (`GENTLE_ACCENT`).**
  - Energy at 2-5 kHz over the first 80 ms minus the note body has a median of -5..-12 dB per track.
  - In the master, 2-5 kHz over the first 80 ms is -2..-7 dB under the body at every accent checked.
  - Accent weight over the note before is +2..+6 dB.
- **Final chord.** No loop pulse: the master's 100-300 Hz and spectral-centroid autocorrelations at 3.95 s are -0.02 and 0.03.
- **Pizzicato.** Basses and celli decay 7-17 dB within 400 ms. Peaks fall within 0.00-0.14 s.

## 1. Repeated accented down-bow strokes are played as one connected chord (bars 32, 72, 142; whole orchestra)

**Where.** Bar 32 (qn 124-125), bar 72 (qn 284-286) and bar 142 (qn 564-566). The bass's bar 83 strokes have their own fix below.
- The strings play accented notes, each marked down-bow: `c'''4->\downbow b''4->\downbow`, `aes'4->\downbow c''4->\downbow aes'4->\downbow`, `c''2->\downbow b'2->\downbow`.
- At bars 32 and 72, 17-18 wind and brass tracks play the same accented, unslurred notes. At bar 142, Fl/Ob/Cl join the violins.
- A down-bow after a down-bow means the player lifts and retakes the bow, so the strokes are separate and heavy.

**What is wrong (measured).**
- The strings join these notes as bow-change legato. Violins I/II and celli are on `Leg BC MAX` with the 0.04 qn overlap and the legato lead.
- The violas and basses play abutting Sus MAX notes.
- Every wind and brass note is held to its full written value (0.97-1.0 qn), so it abuts the next one.
- Break depth between strokes (`downbow.py`; lower of the two bodies minus the minimum within ±0.15 s of the second onset):

  | Bars | Strings | Master |
  |---|---|---|
  | 32 | -1.1..4.7 dB | 2.1 dB |
  | 72 | 2.2..4.1 dB | 2.7 dB and 0.1 dB |
  | 142 | 1.7 and 4.8 dB | 0.0 dB |

- For comparison, the bar 83 bass strokes, which have rests between them, give a 9.6 dB master break.

**As heard (inferred).** Each cadential hammer-stroke figure sounds as one sustained chord with a pitch change, not as two or three separate blows.

**Fix**, in `tools/score_to_parts.py`, a new generic rule `DETACH_ACCENTS = {"min_gap_qn": 0.25, "frac": 0.75}`:
- **Trigger.** Wind, brass and string tracks. The rule applies to an unslurred onset in `accent_q` whose next onset (no rest between) is also an unslurred accent.
  - For strings, also require a `downbow` mark on both notes. Add `downbow_q` next to `ten_q` at line 1056.
- **Note length.** Cut the note to `min(frac × written length, written length - min_gap_qn)`. Kit LEARNINGS 7: an end 0.25 qn early gave a 13 dB break, 0.1 qn gave none.
- **Strings.**
  - Play both notes on Sus MAX: a fresh stroke, `n["detach"] = True`.
  - Exclude them from the Leg BC loop (line 1222: `continue` when both `n` and `o` carry `detach`).
  - Give them no legato lead.
- **Accent weight.** Keep the gentle swell; no CC11 bump (see finding 2).
- **Pass criterion.** Master break of at least 6 dB at qn 125, 285, 286 and 566, with each stroke's 2-5 kHz energy over its first 80 ms still under its body.
- **Optional test.** Inside the same render, play Violins I at bar 72 only on the string KS Master's `Sus Marc LITE` row (key 25, one of the six rows a KS Master loads by default, unloaded here by `UNLOAD_UNUSED_ROWS`). Bar 32 is the control. Loading the row means a full rebuild of that track.

## 2. Accented string notes reached from Sus MAX eighths fall 4-10 dB under the eighths before them (theme, bars 28, 70-71, 135, 140, 168)

**Where (measured).** The second half of the head motif, `c''4) b'8( c''8) aes'4.-> g'8`, and its variants. The accented dotted quarter follows Sus MAX eighths (a two-note slur on `short_sus`, or an unslurred eighth run). It is unslurred, so it plays as a disconnected `Leg Slur MAX` note.

Accented target body (0.15-0.5 s) minus the body of the note before (`sus2leg.py`):

| Track | qn | dB |
|---|---|---|
| Violas | 536 | -10.5 |
| Violins II | 110 | -9.2 |
| Violins II | 278 | -8.4 |
| Violins II | 558 | -6.5 |
| Violins II | 282 | -6.3 |
| Violins I | 110 | -5.8 |
| Violas | 110 | -5.7 |
| Violas | 670 | -4.6 |
| Violins I | 154 | -3.9 |
| Violins I | 378 | -3.2 |

By join type (accented targets):

| Join | Cases | Median |
|---|---|---|
| Sus MAX -> Leg Slur MAX | 18 | -3.5 dB |
| Leg -> Leg BC | 66 | +2.4 dB |
| Sus -> Sus | 22 | -0.2 dB |

The 54 unaccented Sus -> Leg Slur joins sit at -4.1 dB. On notes of 1 s or more the deficit stays at -2.4 dB from 0.6 to 1.0 s, so this is a lower sustain level, not only a slow attack.

The shapes:
- **Violins II qn 110:** -22 dB at the onset, then -34..-39 dB for the rest of the note. Its 10 ms peak is 14.5 dB over the body. The 2-5 kHz energy over the first 80 ms equals the body (-0.2 dB, against -8.7 dB for the section's other accents): the +8 CC11 accent bump reaches the fff layer (CC 122) for the first 0.3 qn.
- **Violins II qn 278:** -36 -> -45 dB at +0.2..+0.6 s, back to -35 dB only at +1.0 s.
- c00 and c01 envelopes at qn 110 and 278 are identical to 1 dB. This was the open c01 item "Vln II 110/278/282 accents under their eighths".

**As heard (inferred).** Each time the theme answers itself, the accented downbeat sounds weaker than the upbeat eighths: a short bright tick and then a hollow note.

**Fix**, in `tools/score_to_parts.py`, string branch (around line 1130):
- **Articulation.** An accented note that is not slurred to its predecessor, and whose predecessor (abutting, within 0.06 qn) is on Sus MAX, a Stac row or Tremolo, plays Sus MAX, a fresh bow stroke. It keeps the entry lead of a Sus note after a Leg note (kit LEARNINGS 6, c06).
- **Accent weight.** Give strings the gentle-accent treatment:
  - Add `GENTLE_ACCENT["string"] = {"arts": ("Sus MAX",), "db": 3.0, "soft_db": 2.0, "swell_s": (0.07, 0.25, 0.6), "keep_legato": True}`.
  - Route the string branch's accent handling through it. Currently strings take `ACCENT_BUMP` 8 CC, +10 velocity and `ACCENT_DB` 2 dB, because `family not in GENTLE_ACCENT`; the gentle treatment drops the bump and the velocity.
  - `keep_legato` keeps accents inside a slur on their legato row, as for winds.
- **Pass criterion.** On the 18 listed onsets, the median body minus predecessor is at least +1 dB, none is under -2 dB, and 2-5 kHz first-80 ms minus body is -3 dB or lower on all of them.

## 3. Timpani rolls that end on a tied stroke have no stroke (7 places; `TIMP_TIE_STROKES` is empty)

**Where (score).** The part writes rolls that end on a tied, unrolled note. The score's own comments say so: "rolls end on a tied stroke" (intro.ily c166) and "the crescendo ends on a tied stroke on the A♭" (dev.ily c166). The MIDI merges the tie into the roll. The tied notes are at:

| qn | Bar and beat | Dynamic |
|---|---|---|
| 46 | 12.3 | f |
| 54 | 14.3 | pp |
| 249 | 63.2 | dim. |
| 460 | 116.1 | f arrival |
| 561 | 141.2 | ff |
| 581 | 146.2 | pp |
| 641 | 161.2 | dim. from fff |

**Measured.** At 46, 460, 561 and 641 the timpani stem is flat through the tied note (±1 dB of the roll in the 0.3 s around it). The roll simply stops at its end: at 460, -36 dB steady, then a fade from +0.45 s. There is no attack anywhere.

The kit's rule exists: `TIMP_TIE_STROKES` / `TIMP_TIE_STROKE_DB` in score_to_parts.py line 232, from mvt II c14, where a stroke peaked 6.4 dB over the roll. In movement I the list is empty.

**Fix.**
- In `build/score_config.py`, set `TIMP_TIE_STROKES = [46.0, 460.0, 561.0, 641.0]`.
- Leave 54, 249 and 581 as rolls ending in their diminuendo. These are the pp ends; the kit leaves pp/ppp tied ends alone, because felt strokes below v53 are near silent.
- Check that the velocity rule gives about v96 at 46 and 460, v110 at 561, and about v80 at 641.
- **Pass criterion.** Each stroke peaks 3-7 dB over the roll's last half beat, in the 50-250 Hz band, within 0.03 s of its score onset.

## 4. Long timpani rolls pulse at their sample loop (3.3-3.5 s): the opening ppp solo roll is the most exposed

**Measured** (`timproll.py`). The timpani stem's 60-250 Hz level and spectral centroid, detrended, have a clear period:

| Roll | Length | Level | Centroid | Swing (p95-p5) |
|---|---|---|---|---|
| Opening, qn 0-16, bars 1-4 | 19.2 s | autocorrelation 0.82 at 3.50 s | 0.88 | 5.8 dB |
| qn 48, bars 13-14 | 8.4 s | 0.94 at 3.30 s | — | 5.4 dB |
| qn 160, bar 41 | — | 0.88 at 2.95 s | — | 9.1 dB |
| qn 464, bars 117-121 | — | 0.71 at 3.30 s | — | 6.2 dB |
| qn 484, bars 122-130 | — | — | 0.98 at 3.30 s | — |
| qn 720, final roll | — | — | 0.91 at 3.50 s | 6.4 dB |

- In the opening, the roll is the only sustained sound in the movement's first 3 beats, and it runs under the pp cello, bass and bass-clarinet phrases.
- c01 raised it +12 dB (timpani role), so it is now -45.7 dB, 4 dB under the basses, and exposed.
- In the master's 60-250 Hz band the period does not show (autocorrelation 0.02 on the opening), because the moving bass lines dominate that band's statistics.

**As heard (inferred).** A slow throb about every 3.5 s, heard as a pulse in the roll.

**Fix.**
- Fit periodic inverse profiles on the c01 timpani stem into `build/loop_profiles.json` "Timpani". This is the kit method, LEARNINGS 6 and 10 (c26: 4.2 -> 1.0 dB and 2.6 -> 1.1 dB).
  - Keys are the moved onsets 0.0, 48.0, 160.0, 464.0, 484.0 and 720.0.
  - Use `period_s` as measured per roll, because each pitch has its own loop: 3.50, 3.30, 2.95, 3.30, 3.30, 3.50.
  - Clamp `corr_db` to ±3 dB, and remove `vol_db` before folding.
- **Pass criterion.** Each roll's 60-250 Hz detrended swing is at most 2.5 dB, and its autocorrelation at its period is under 0.3.

## 5. Woodwind staccato speaks 0.1 s after the string staccato it doubles (development, bars 85-96, 30)

**Where.** The development's staccato motif is passed between instruments: Bn1 + Vla at qn 350-359, CA + Vln II at 362-371, Fl1 + Vln I at 374-383; also bar 30.

**Measured** (`stac.py`, `env.py`).
- Winds play printed staccato as Sus MAX at half length.
  - CA qn 368 peaks at +0.10..+0.14 s, against +0.02 s for Violins II on the same note.
  - Bn1 qn 356 peaks at +0.14 s, against +0.02..+0.06 s for the violas.
- Median peak times: CA 0.128 s, Bn1 0.103 s, Cl1 0.245 s (the next note's attack), Ob1 0.068 s. The strings' Stac rows peak at 0.022-0.055 s.
- The wind note reaches its level just as the string note dies, so each doubled staccato has a soft second onset (inferred: a smeared, two-part attack). This was c01's deferred A6.2.

**Fix** (`score_to_parts.py`, the wind branch at `elif q in stacc_q`):
- Use `ks_lookup(stem, "Stac DblTng RRx9")`. The row is key 28 in the FL, OB, EH, CL and BS KS Masters (ks_maps.json).
- Velocity sets the level, as on other short articulations: start from the Sus note's velocity and trim per track after the render.
- This loads one row, so it is a full rebuild of Flute 1, Oboe 1, Cor anglais, Clarinet 1 and Bassoon 1.
- **Pass criterion.** Wind staccato peak time is within 0.04 s of its string doubling (median), and the level is within ±2 dB of the c01 Sus notes.

## 6. Re-bow seams: Lento celli and the final bars still dip; the fitted shapes hit their +9 dB cap

**Measured** (`rebow2.py`, `rebow3.py`, 80 ms envelope). Median stem dip at the re-bows against unsplit control notes:

| Section | c00 | c01 | Control |
|---|---|---|---|
| Violoncellos | 6.9 | 5.9 | 4.2 |
| Violins I | 4.7 | 8.0 | 4.6 |
| Violins II | 6.4 | 6.0 | 3.2 |
| Violas | 4.1 | 5.3 | 4.4 |
| Double basses | 3.9 | 3.5 | 4.5 |

Level steps of 3 dB or more fell from 17 to 5 (celli) and 12 to 7 (basses), so the c01 fit fixed the steps but not the dips.

Worst seams:
- **Celli qn 37.37 (bar 10, the loudest stem there):** the stem falls from -36 to -47 dB over -0.16..+0.36 s and then overshoots to -29 dB at +0.5 s. The master dips 3.6 dB.
  - The fitted shape in `rebow_fills.json` sits at its +9 dB clamp from 0 to 0.32 s, and the hole starts 0.16 s before the re-bow.
- **Celli 25.39 (bar 7):** 11.7 dB, master 2.4.
- **Final bars 178-182 (30 re-bows):** median master dip 3.1 dB (p90 5.1) against 2.1 (p90 3.4) at random control times in the same bars.
- **Intro bars 6-14:** the master at the 38 re-bows is no worse than at control times (2.4 against 2.7 dB), so only the outliers above matter there.

**Fix.**
- **Re-bow lead.** At soft levels the new Sus MAX piece speaks slowly (kit LEARNINGS 6, soft entries).
  - Give each re-bow piece at CC11 ≤ 50 a lead of 0.10 s, with the old piece ending at the moved start (no same-pitch overlap). Add `REBOW_LEAD_S = 0.10` in `score_to_parts.py`'s re-bow split.
  - Then refit with `tools/fit_rebows.py` at 0.04 s smoothing instead of 0.12 s. Allow up to +12 dB for the first 0.4 s only, and keep the -6..+9 dB clamp for the hold.
  - Refitting needs a render with the new lead first, so refit in the cycle after the lead change.
- **Pass criterion.** Celli intro re-bow dips at most 4 dB median, none over 7 dB. Master dip in bars 178-182 at the re-bows within 0.5 dB of the control.

## Smaller items still open (not ranked)

- **Harp étouffez at qn 244 (bar 62, sub. p).** The f chord of qn 242 is still -35 dB at the subito and decays only 8 dB in 0.4 s. It sits over the p harp arpeggio, and the master falls only 3-4 dB into bar 62.
- **Unison and a2 passages.** Horn 2's 97 dropped unison notes, and Violins II's "metà" at bars 47-54 on the full section, are unchanged from c01's A #5. They are worth doing when REAPER's 42 GB footprint allows another Opus instance.

Do not touch: `GENTLE_ACCENT` for brass and winds (2-5 kHz attack minus body -5..-12 dB median, no 2-5 kHz bursts in the master, +2..+6 dB weight), the c01 pickup rule (`SHORT_SUS_TO_LONG`), `AUTO_REBOW` stagger and times (final chord master 100-300 Hz and centroid autocorrelations -0.02 and 0.03), legato structure (no chords on legato rows, no same-pitch overlaps), the string Stac rows, the pizzicato rows, and the suspended-cymbal timing.
