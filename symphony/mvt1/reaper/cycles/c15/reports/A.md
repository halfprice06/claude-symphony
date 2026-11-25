# Cycle 15, critic A: articulation and phrasing (render c14)

Scope: every wind, brass, string, harp, timpani and percussion note in `build/parts.json` (the c14 build after its stem fix; note timing identical to `cycles/c14/rendered_build/parts.json`), measured on the c14 stems and master (`cycles/c14/render/`), with c13 (`cycles/c13/render/`, `cycles/c13/rendered_build/parts.json`) as a reproducibility check. Patch tables were read from the `.oib` files with `opus_state.load_oib`.

Scripts, 5 ms feature files and outputs are in `/private/tmp/claude-501/mockup-loop/mvt1-c15-A/`. The c14-A battery was rerun on c14 (`out_*.txt`). New scripts:
- `efchk2.py`: every existing early fill against the hole it is meant to fill (auto_fills.py definitions);
- `sstart.py`, `tongued.py`: first notes of slurs against the note before, and tongued notes for comparison;
- `simdip.py`, `simdip2.py`: a volume-envelope dip at brass note changes, simulated on the stems and the master;
- `negacc.py`, `acchole.py`: accent fits with negative steps, and accents whose body falls under their pickup;
- `oibf.py`, `oibkeys.py`: the Celli KS Master's scripts and RR settings;
- `rbctl2.py`, `who.py`: re-bow dips against control times.

## Checks that passed (measured)

- **Legato.** No chord sits on a Leg row. Join dips by track: medians 1.8-2.6 dB on strings, 0.2-3.2 dB on winds and brass. Joins of 6 dB or more: Violins I 2, Violins II 4, Violas 2, celli 5 (but see #1). Keyswitches sent while a Leg note sounds are all Leg Slur / Leg BC / Leg Port row changes, as designed.
- **Re-bows (item 7).** Master dip at the 62 re-bows before qn 700: median -1.77 dB, against -1.80 dB at 35 control times in the same held notes. Final chords (708-728): longest notes (22.5-22.7 s) have autocorrelation at the loop period of 0.18 or less in level, 100-300 Hz and centroid. Violins I's 6 re-bows dip -5.3 dB on the stem (ppp, 7.5-8.3 dB under the master) and -2.1..-3.6 on the master. The -4.9 dB master dip at 48.6 is the printed phrase end in every section, not a re-bow.
- **Accents (item 8).** 2-5 kHz first 80 ms minus body: brass median -7.8 dB (max +2.6, none over +3), winds -5.8 (max +3.7: Clarinet 1 422, Bassoon 1 382, Oboe 1 113), strings -4.3. The string readings over +3 dB are Violas/celli 536 (ff into sub. mf) and Violas 120, where the body collapses (#5).
- **Other articulations.** Staccato separates 7.0-14.1 dB per track (medians). Breath marks dip 3.8-16 dB; the Horns a2 breath at 475 dips 5 dB, the 636 caesura 4 dB on the master. Tremolo joins: median -0.9 dB, 1 of 33 at 4 dB or more. Pizzicato reaches -3 dB of its peak in a median 0.003-0.055 s. Harp étouffez at 650 still damps the old pitches. Timpani strokes and tie strokes unchanged from c13.

## 1. Existing early fills start after the hole they fill: exposed cello lead joins still drop 7-13 dB (Lento bars 2-17, second theme bars 50-56 and 150, coda bars 172-174)

**Measured** (`efchk2.py`, using the `auto_fills.py` definitions: reference = the lower of the two bodies, minimum between the moved onset - 0.05 s and the score onset + 0.4 s, times relative to the score onset).

Of the 131 existing entries in `build/early_fills.json`, 29 still dip 5 dB or more on c14, and in 17 of them the hole's minimum comes before the fill reaches full level. The same joins read the same on c13 (18 cases; celli 8 10.2 dB at +0.115 s, 694 7.4 dB at +0.10 s).

| Track | Onset (bar) | Dip | Minimum at | Fill | Stem re master |
|---|---|---|---|---|---|
| Violoncellos | 8 (3) | 12.9 dB | +0.13 s | +6 dB from +0.16 s | -3.1 dB |
| Violoncellos | 694 (174) | 7.9 | +0.10 | +3 from +0.14 | -1.1 |
| Violoncellos | 198 (50) | 6.5 | +0.05 | +5 from +0.09 | -3.2 |
| Violoncellos | 598 (150) | 6.7 | +0.05 | +5 from +0.09 | -4.0 |
| Violoncellos | 66 (17) | 7.0 | +0.04 | +6 from +0.08 | -4.9 |
| Violoncellos | 712 (179) | 7.8 | +0.14 | +4 from +0.17 | -6.6 |
| Violoncellos | 122 (31) | 7.8 | +0.01 | +6 from +0.08 | -7.0 |
| Violoncellos | 658 (165) | 8.1 | -0.18 | +2 from +0.11 | -7.7 |
| Horn 1 | 422 (106) | 11.5 | -0.11 | +6 from +0.08 | -7.9 |
| Bassoon 1 | 415, 420, 422, 453 | 5.6-7.3 | -0.03..0.00 | from 0.00..+0.08 | -7.2..-13.5 |
| Clarinet 1 | 140, 515 | 5.3 | +0.04 | from +0.08 | -7.8..-11.5 |

On 40 ms frames, celli 8 falls from -39..-41 to -47..-49 dB for 0.2 s (moved onset + 0.18..+0.34 s) while the fill only rises from moved onset + 0.35 s. Celli 690 and 687 (bar 173) dip 4.7-6.3 dB with fills that start at +0.14 s.

Cause:
- These entries carry the negative `pre_s` of c03's 1/6 qn shift (fill starts 0.08-0.17 s after the score onset).
- Since then the celli's legato targets move 0.11-0.22 s early (`moved` column in `efchk2.py`), and their sags begin at the moved onset.
- `tools/auto_fills.py` never retimes an existing entry. Its "raised" branch copies the old `pre_s` (`pre = old.get("pre_s", 0.0)`), and the celli are in `TRACKS` but not `RAISE_TRACKS`, so their old entries are not touched at all.
- A plan-only run on c14 (no `--write`) would raise Horn 1 422 to +8 dB, still from +0.079 s, behind a hole at -0.107 s.

**Inferred.** The cello line leads the Lento and the second theme (1-5 dB under the whole orchestra). A 0.2-0.3 s drop of 7-13 dB at a slurred step sounds like a bow lifting off or a missing note, and it happens at the first cello phrase of the piece.

**Fix:** `tools/auto_fills.py`, new branch "retimed" before the raise:
- An existing entry with dip at least `mind` and `t_min < -pre_s + 0.02` (the minimum lies before the fill is full) gets:
  - `{"db": min(8.0, max(db0, dip - 3)), "pre_s": round(max(0.0, -t_min), 2), "hold_s": clamp(t_min + 0.05, 0.10, 0.35)}`
  - It applies on every track in `TRACKS`, not only `RAISE_TRACKS`, and is listed in `_auto` as "retimed".
- Also add "Bassoon 1" to `TRACKS` and `RAISE_TRACKS`.
- Then run `auto_fills.py 14 cycles/c14/rendered_build/parts.json --write` (the plan also adds 15 new entries, 9 of them celli joins of 5-9 dB: 48, 58, 112, 189, 392, 545, 566, 570, 664).
- Do not edit the decrescendo guard or the overshoot rule; they run as they are on c15.

**Pass:**
- The 15 joins in the table plus celli 687 and 690 under 5 dB on c15 (auto_fills measure).
- No fill over +2 dB above the louder body (the tool's 200 ms overshoot measure).
- Celli stem level 0.5 s after each join within ±1 dB of c14.

## 2. A slur's short first note after a tongued note plays the legato row's slow layer: 2-10 dB under the note before (50 wind and brass notes)

**Measured** (`sstart.py`, `tongued.py`). Set: the first note of a slur, at most 0.6 qn written, that follows another note of the same track within 2 qn, where the slur's second note is not accented or tenuto. Body = moved onset + 0.05 s to the next moved onset.

| Notes | n | Note minus the note before (median) | Share at -4 dB or lower |
|---|---|---|---|
| Wind slur starts on Leg Slur (clarinets) | 23 | -2.2 dB | |
| Wind slur starts on Leg Slur MAX | 21 | -3.3 dB | |
| Wind and brass slur starts, all | 50 | -2.2 dB | 36% (18) |
| Tongued unslurred short notes after a note, Sus rows (same tracks) | 64 | +0.8 dB | 8% |

Worst cases, the slur's first note minus the note before:

| Track | Onset (bar) | First note minus note before | Stem re master |
|---|---|---|---|
| Clarinet 1 | 509 (128) | -7.9 dB | -3.2 dB |
| Clarinet 1 | 506.5 (127) | -4.3 | -2.3 |
| Bassoon 1 | 130.5 (33, espr.) | -7.0 | -3.8 |
| Bass clarinet | 306.5 (77, Solo espr.) | -5.4 | -4.9 |
| Oboe 1 | 314.5 (79) | -9.0 | -7.1 |
| Clarinet 1 | 374, 410.5, 413 | -5.4, -8.2, -8.2 | -12..-15 |
| Oboe 2 | 410.5, 413, 418.5 | -5.5, -10.2, -6.4 | -8..-15 |

Clarinet 1 509: the C4 quarter (end of a slur) sits at -32 dB, the slurred B3 eighth (Leg Slur, v65) at -38..-42 dB for its whole 0.24 s, then the C4 eighth returns to -34, all inside a printed crescendo (CC11 62-65, volume +10 dB flat).

Cause: `score_to_parts.py` puts every wind/brass slurred note on Leg Slur (`elif n["slur"] is not None: n["art"] = ks_lookup(stem, "Leg Slur MAX", "Leg Slur")`). A slur's first note is disconnected, so the row plays its sustain layer, which rises slowly (kit section 5; the c04 portato rule already moved slurred tenutos to Sus for this reason).

This is also why two-note eighth slurs read "second louder" after the c14 release (Clarinet 1 374 +3.2, 413 +2.9 dB): the first note is weak, not the second loud.

**Inferred.** Wind players tongue the first note of a slur at the line's level. A dropped first note breaks the two-note figures in the clarinet's development crescendo (bars 127-128) and in the espressivo bassoon and bass clarinet solos.

**Fix:** `tools/score_to_parts.py`, wind/brass articulation chain, a new branch before the plain slur branch. Defaults go in `build/score_config.py`:

`SLUR_START_SUS = {"families": ("wind", "brass"), "max_qn": 0.6, "after_qn": 0.15}`

Conditions:
- `n` is the first note of its slur;
- `n["end"] - q <= max_qn`;
- another note of the track ends within `after_qn` before `q`;
- not polyphonic, not accented, not tenuto.

Then:
- `n["art"] = ks_lookup(stem, "Sus MAX", "Sus Max", "Sus Non Vib", "Sus Non Vib MAX")[0]`, with `n["slur_start_sus"] = True`.
- The slur's second note stays on Leg Slur and joins from it the way the kit's c23 `SOST_JOIN_LEAD_S` path does: overlap 0.04 qn, lead `SOST_JOIN_LEAD_S` (0.12 s), velocity 100, keyswitch to Leg Slur while the Sus note sounds. The guard concerns sounding legato notes only.
- Apply it once per onset, and leave `SLUR_PAIR_RELEASE` as it is.

Fallback if the join fails on the render: a level-only lift on those first notes (exact shape from the moved onset to the next moved onset, `+min(6, before - first - 1)` dB), as a stem fix.

**Pass:**
- On the same set, median first note minus note before -0.5 dB or higher, and under 15% at -4 dB or lower.
- Join dip into the second note at most 4 dB (median).
- Clarinet 1 509 within 2 dB of the C4 before it.
- Two-note eighth slurs (winds) median second minus first between -1 and -3.5 dB.

## 3. Tongued brass changes with short gaps are still as smooth as slurs (87 changes, ff tutti themes): put the separation in the volume envelope

**Measured** (`detw2.py`, `detbin.py` on c14). Hole = the lowest 20 ms frame within ±0.08 s of the score onset, minus the louder of the two bodies.

| Brass change | n | Hole median |
|---|---|---|
| Gap under 0.06 s | 87 | -3.5 dB |
| Gap 0.08-0.095 s | 252 | -5.0 dB |
| Gap 0.095-0.2 s | 23 | -5.3 dB |
| Slurred | 150 | -3.6 dB |

- Winds pass: tongued -5.6, slurred -4.1 dB.
- The c14 CC11 fall (`WIND_DETACH["by"]["brass"]["fall_cc"] = 10`) changed nothing (c13 -3.1 dB).
- Short gaps by track: Horns a2 23, Trombone 1 21, Trumpet 1 15, Horn 2 9, Horn 1 8, Horn 3 5. Many are slur ends into the next tongued note (Horns a2 277.5 -> 278, Trumpet 1 669.5 -> 670, Trombone 1 525.5 -> 526) and eighths whose detach gap the entry lead shortened to 0.04 s.

**Simulated** on the c14 stems (`simdip2.py`). The volume envelope acts after Opus, on the plugin's output including its hall, so multiplying the stems is exact. Shape at every one of the 87 changes: 0 dB at the old note's end - 0.05 s, D at its end, held to the next moved onset - 0.005 s, back to 0 at + 0.005 s.

| D | Stem hole median | Master dip median at the same changes |
|---|---|---|
| 0 dB (c14) | -3.6 dB | -2.39 dB |
| -3 dB | -4.8 | -2.49 |
| -4 dB | -5.5 | -2.48 |
| -6 dB | -7.2 | -2.54 |

The master barely moves, because the strings carry the rhythm there.

**Inferred.** In the four ff tutti themes the brass eighths still run together on their own stems. Tongued separation at -5..-6 dB, like the wider-gap changes and the winds, makes the brass rhythm audible without making it staccato.

**Fix:**
1. In the `WIND_DETACH` branch of `tools/score_to_parts.py`, replace the CC11 fall (the c14 test, which failed) with a volume dip. For a brass note followed by a different pitch that is not in the same slur, when the played gap (next moved onset minus the note's end) is under 0.07 s, write the exact level shape above.
2. Set `WIND_DETACH["by"]["brass"] = {"gap_s": 0.09, "frac": 0.18, "dip_db": -4.0, "dip_fall_s": 0.05}` in `build/score_config.py`. Same-pitch repeats stay with `WIND_REP_RETONGUE`.
3. Apply it once per onset when unisons are merged. The new note's accent swell starts after the dip ends, so the two do not overlap.
4. Refit the brass accents afterwards (`fit_accents.py`, brass only).

**Pass:**
- Brass changes with gaps under 0.07 s: hole median -5.0 dB or deeper.
- Slurred brass within ±0.3 dB of -3.6.
- Master dip at those changes no more than 0.3 dB deeper than c14.
- No new 2-5 kHz front over +3 dB on the following notes.

## 4. The celli's measured tremolo (bars 117-121) still repeats its 9-stroke round robin: alternate two short rows instead of CC36

**Measured** (`rrcyc.py` on c14). The 80 strokes (G2, Stac RRx9, v96, 0.119 s apart) have this autocorrelation:

| Value | Lag 9 | Lag 18 | c13 lag 9 |
|---|---|---|---|
| Peak level | 0.73 | 0.67 | 0.71 |
| 1-8 kHz share | 0.85 | 0.85 | 0.82 |
| Centroid | 0.92 | 0.87 | 0.93 |

- By position in the cycle, takes 5-6 are 2.0-2.3 dB weaker and 2.6-3.8 dB brighter in 1-8 kHz share, and takes 7-9 are darker (centroid 138-153 Hz against 169-198 Hz).
- The celli are 16.2 dB under the master there.
- The c14 CC36 resets did nothing. The patch state shows why the round robin cannot be steered from MIDI: the Repetition3 script (`RESET_RANDOM_TIME` 60, `RESET_REPEAT_COUNT` 5, `DETUNE_INTENSITY` 50) is off with CC69 0, and nothing else in the state selects the take order (`oibf.py`).

**Inferred.** A pattern that repeats exactly every 1.07 s under the build to bar 122 sounds mechanical, like a loop.

**Fix** (a memory-cheap row: c14 measured one-note rows at about 0.04 GB each):
1. Load the Celli KS Master's `Stac On Bow RRx9` row (key 28, on-the-string staccato, the closer stroke for a measured tremolo). This is a full rebuild of the celli.
2. In the `MEAS_TREM` expansion of `tools/score_to_parts.py`, give each stroke a row from a fixed irregular sequence, about 55% Stac RRx9 and 45% Stac On Bow. No row plays more than 3 strokes in a row, and the pattern is not periodic under 30 strokes, for example a seeded `random.Random(464)` draw. Each row's round robin advances only on its own strokes, so the combined order no longer repeats at 9.
3. Send each keyswitch 0.012 qn before its stroke (stroke rows are not legato).
4. Remove `MEAS_TREM["rr_runs"]` and the `cc36` lane (c14 test); keep the pre-roll reset.
5. Match the rows' levels with `ROW_TRIM_DB["Violoncellos"]["Stac On Bow RRx9"]`, set from the c15 render: median stroke peak per row within 1 dB.

**Pass:**
- Stroke autocorrelation under 0.3 at lags 9 and 18 and under 0.4 at every lag 4-18, for peak, 1-8 kHz share and centroid.
- Sixteenth-grid fold 3.5 dB or more.
- Celli level per bar within ±1 dB of c14.

## 5. Violas bar 31: an accented dotted quarter sits 9.7 dB under its own eighth pickup, from a fitted -6 dB step on a legato target

**Measured** (`negacc.py`, `acchole.py`, `v120.py`). Score: `Vla` 118 G4 dotted quarter (accent), 119.5 F4 eighth, 120 A-flat4 dotted quarter (accent), unslurred. In the render:
- F4 (Leg BC, moved to 119.101) plays at -29.7 dB.
- A-flat4 (Leg BC target, moved to 119.775) falls to -38..-41 dB from 0.1 s after its moved onset to the end of the note: body -39.5 dB, 9.7 dB under the pickup, 24 dB under the master.
- The 2-5 kHz front-minus-body reading of +9.4 dB comes from this collapse, not from a bright attack.
- The volume envelope holds +2.0..+2.5 dB on the F4 (the 118 swell of +5 dB lasts to 119.75), then -4.5..-6.0 dB from 120.2 to 121.05. That is `accent_fits.json` Violas `"120": [0.0, -6.0]`.
- The fit read the Leg BC transition peak (-25 dB at moved onset + 0.03 s) as the accent and cut the whole note.
- c13 measured the same shape.
- No other accent of the 324 checked falls 4 dB or more under its pickup except at the printed sub. mf (536).

**Inferred.** The violas' second accent of the figure disappears in the middle of the first-theme tutti.

**Fix:**
- `build/accent_fits.json` Violas `"120"` -> `[0.0, 0.0]`, and `build/note_trims.json` Violas `"120.0": 3.0` with `NOTE_TRIM_RAMP_S["Violas"][120.0] = 0.1`.
- In `tools/fit_accents.py`, skip negative steps on accents played as Leg targets whose moved onset is more than 0.05 s before the score onset (the measured front then includes the transition); measure those from the moved onset.
- Refit only this track's accents 118-125 afterwards.

**Pass:**
- Violas 120 body (+0.15..+0.5 s) 2-4 dB over the F4 pickup.
- 2-5 kHz front minus body under +3 dB.
- Violas 118/124/125 within 1 dB of c14.

## 6. Smaller items

- **Horns 3-4 a2, bars 80-81** (316.5-328: G3 -> E-flat4 accented pickups twice, then C4 whole note, every onset the same pitch). These play on one solo horn sample, 7.4-9.9 dB under the master. The Horns a2 track is free there.
  - Fix: let `TRACK_WINDOWS` take notes from a second staff, `"Horns a2": (_A2W, True, {"Hn3": [(316.4, 328.0)]})`. Horn 3 and Horn 4 rest in that window.
  - Set the window's role from the first render, as for the other a2 windows (LEARNINGS c13).
  - No new instance is needed.
- **Two-note slur release on short notes.** After #2, re-measure before changing it. If eighth pairs still read over -1 dB, scale the shape on second notes under 0.35 s: `from_s = min(0.10, 0.3 * dur_s)`, `full_s = min(0.20, 0.6 * dur_s)`. Strings pass now (-3.0 dB, 30% at -1 or louder), so leave them.
- **Clarinet 1 422 / Bassoon 1 382 / Oboe 1 113 accents:** 2-5 kHz front minus body +3.5..+3.7 dB, the only wind readings over +3. Bassoon 1 382 carries a -5.7 dB fitted step that lowers the body under its front. Recheck after the brass and wind refit; no action now.

Do not touch:
- `SLUR_PAIR_RELEASE` for strings;
- the Horns a2 track, its windows and per-window roles;
- `MEAS_TREM` strokes (only the row choice changes);
- `REP_SPLIT`; `TREM_JOIN` / `TREM_SPLIT`;
- `WIND_DETACH` for winds;
- `GENTLE_ACCENT` with `swell_s_leg`;
- the c13 pickup `LEVEL_SHAPES`;
- `_REBOW_FROZEN` / `REBOW_AT` with `rebow_fills.json` and `NOTCH_SKIP`;
- `TIMP_CC1_MAP` with `TIMP_ROLL_TRIM_DB` and the re-strike plans;
- `PORTATO_JOIN_AT`; `DOWNBOW_STROKE_AT` with its `LEVEL_SHAPES`; `ROW_TRIM_DB`;
- harp `env_release_ms` 200 with `HARP_RING_S`;
- the pizz., staccato and tremolo rows;
- `PORT_TARGETS`;
- the sus. cymbal key 64 / lead 0.25;
- the climax order (160 > 122 > 169).
