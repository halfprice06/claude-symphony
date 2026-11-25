# Cycle 22, critic A: articulation and phrasing (render c21)

Scope: every wind, brass, string, harp, timpani and percussion note in `build/parts.json` (the stem-fixed c21 build; note, CC and keyswitch data in the horn and string tracks checked identical to `cycles/c21/rendered_build/parts.json` where compared), measured on the c21 stems and master (`cycles/c21/render/`), with c20 as the control (`/private/tmp/claude-501/mockup-loop/mvt1-c21-A/feat_c20`). Scratch: `/private/tmp/claude-501/mockup-loop/mvt1-c22-A/`. I reran the c21-A battery on c21 (outputs `o21_*.txt`, features `feat_c21/`). New scripts: `efold.py` (band envelopes folded on the eighth grid), `repscan.py` (every run of 4+ repeated unslurred Sus eighths, folded), `cbsim.py` (stem/master simulation of a detach dip on the basses), `relsus.py` (release after the last note before a rest, Sus MAX strings, c20 against c21), and `rb_c20.json`/`rb_c21.json` (re-bow dips per render). The patch data was read from the `.oib` files with `opus_state.load_oib`.

## Checks that passed (measured)

- **Legato.** No chord goes to a legato row (`chordleg2`: none). Wind and brass joins at 6 dB or more: none. String joins at 6 dB or more: 5, the same as c21's actor count (Vc 112 7.8, Vc 689.5 6.7, Vc 215 6.3, Vla 612 6.6, Vln II 637 7.2). None of them shows on the master.
- **Accents (item 8).** 2-5 kHz energy in the first 80 ms minus the note body: brass median -8.4 dB, winds -6.0, strings -3.5. These are c20's values within 0.5 dB. The outliers are the same notes as before: Vla/Vc 536 (+12.9/+10.9) are the release of the ff eighth before a subito mf, and Trumpet 1 284 (+7.6) sits 15 dB under the master.
- **Loop pulsing (item 7).** No held note within 6 dB of the master pulses at the loop period. The bass clarinet's C3 at qn 11 (6.1 s, -4.3 dB re master, deferred to this lens in c21) has a flat level: ±0.3 dB in 0.25 s bins. Its centroid drifts once, 350 -> 250 -> 340 Hz, over the whole note, so there is no 3.95 s cycle. No change needed.
- **Keyswitches.** The shortest lead to a note is 14 ms, and none is under 4 ms. Every keyswitch that falls inside a sounding note is a planned legato-row switch, a slur-start join or a timpani row change.
- **Other techniques.**
  - Pizzicato is on time (-10 dB point median +0.005 s).
  - Tremolo joins: median -1.1 dB.
  - Staccato separation (strings): median 9.8-14.2 dB.
  - Tenuto portato joins: 3 dB or less.
  - Ties are held.
  - Harp étouffez at 244/650/654 is unchanged.
  - Timpani strokes and rolls are unchanged.
  - The breath marks dip 3-15 dB. Horns 1-2 at 475 and 636 read 0 only because those notes play on Horns a2. There the breath gaps are 0.30 qn at 474.6 and 0.09 qn at 635.88, which is the caesura breath.
- **c21 partial passes, unchanged on this render:**
  - 607 F leads -0.07/+0.01 s.
  - Celli arpeggio crossover median +0.070 s.
  - Vln I 270.25 still +0.167 s.
  - Celli 239.0 still +0.245 s.
  
  I do not repeat these as findings. Their next steps are in c21-A #2-#4.

## 1. The basses' ff repeated-eighth pedals in bars 27-31, 131-134 and 140-142 play as one held note: no stroke on the eighths (measured; fix simulated)

**Where.** Double basses:
- bars 27-31, qn 104.5-124: ff C2/D2/E♭2 eighths under the celli's ff tune and the timpani (score p. 2);
- bars 131-134, qn 520-536;
- bars 140-142, qn 556-567.5.

The basses play each eighth as a Sus MAX note of 0.47 qn (gap 0.03 qn), v91. These eighths are the rhythmic bass of the first theme's tutti.

**Evidence (measured).**
- I folded the band envelopes on the eighth grid (`efold.py`; peak-to-trough of the mean profile over all eighths, in dB):

  | Span | 30-150 Hz | 150-600 Hz | 1-4 kHz |
  |---|---|---|---|
  | Basses 104.5-124 | 2.8 | 2.8 | 1.7 |
  | Basses 520-536 | 2.7 | 3.5 | 2.5 |
  | Basses 556-567.5 | 3.1 | 4.3 | 2.5 |
  | Basses 324-328 (control) | 7.0 | 8.9 | 6.6 |
  | Basses 664-676 (coda control, the c20 steps) | 7.7 | 4.3 | 3.4 |

  The celli's measured tremolo passed at 4.0 dB (c13).
- The eighth's own shape (20 ms bins from the moved onset, 104-124): -17.9, -18.3, -17.8, -17.7, -16.9, -16.0, -16.0, -16.5 ... dB re the peak.
  - Each eighth is quietest at its start and peaks at +0.10-0.12 s, half way through the note. The pedal swells on every eighth and has no stroke at the start.
  - The c21 release cap made the basses' re-attack dip only 0.5 -> 0.9 dB (c21 CHANGES; pass 2).
- `repscan.py` finds no other run of four or more repeated unslurred Sus eighths in any string, wind or brass track with a fold under 4 dB. Winds and brass already have WIND_DETACH.
- Rows tried before: Marc Shrt (c03) and Detache (c13) separated no better. Both are in LEARNINGS. The row approach is used up. A level dip at the end of each eighth is not.

**Simulation (measured on the c21 stems; `cbsim.py`).** A volume dip of -5 dB over the last 0.08 s before each next eighth's moved onset (0.02 s ramps, back at the onset + 0.025 s), on the three spans:

| Measure | c21 | Simulated |
|---|---|---|
| Basses fold 30-150 / 150-600 / 1-4k, 104.5-124 | 2.6 / 1.8 / 1.8 | 6.5 / 6.3 / 5.7 |
| Basses fold, 520-535 | 2.8 / 3.5 / 2.5 | 7.8 / 8.5 / 6.9 |
| Basses fold, 556-567.5 | 3.1 / 4.3 / 2.5 | 7.5 / 8.8 / 5.6 |
| Master fold 30-150 Hz, 104-124 / 520-535 | 2.5 / 3.8 | 3.9 / 5.3 |
| Basses RMS / master RMS over the span | | -1.6 / -0.09 dB |

- -4 dB gave 5.6/5.3/4.7 on the stem.
- -6 dB gave 7.5/7.3/6.7, with a stem RMS of -1.8.

**Fix.**
- `tools/score_to_parts.py`: extend the WIND_DETACH dip (brass: dip -5, dip_min_cc 84) to unslurred same-pitch string eighths of 0.5 qn or less on Sus MAX at CC11 84 or more. As a generic rule, a new `STR_REP_DETACH = {"tracks": ["Double basses"], "dip_db": -5, "dip_s": 0.08, "ramp_s": 0.02, "min_cc": 84}` with an `at` span list in `build/score_config.py`: [104.5, 124], [520, 536], [556, 567.5].
- Write the breakpoints exactly (LEARNINGS 15).
- Add a +1.5 dB role on the same spans in `build/roles.json` to restore the bar RMS.
- It is level-only. It can be built with `--midi-only` on the basses, and checked or tuned on the stem with `stem_fix.py` before it is kept.

**Pass.**
- Basses 1-4 kHz fold ≥ 4.5 dB on all three spans; 30-150 Hz ≥ 5.
- Basses bar RMS within ±0.7 dB of c21.
- Master 30-150 Hz fold up at 104-124 and 520-535.
- No new 6 dB join hole on the basses at the span edges (124, 536, 567.5).

## 2. The celli's Lento re-bows at qn 39.879, 41.38 and 49.683 lost their fit when the release cap went in: the 39.879 hole is now 10 dB on the stem, at the bar-10 breath (measured)

**Evidence (measured, `rb_c20/c21.json`, lowest 80 ms level in -0.1..+0.6 s minus the 0.4 s before).**

| Re-bow | c20 stem | c21 stem | c21 master | Celli re master |
|---|---|---|---|---|
| 39.879 | -5.7 | -10.4 | -2.4 | -5.6 |
| 41.38 | -2.6 | -4.2 | 0.0 | -8.3 |
| 49.683 | -6.0 | -8.2 | -1.2 | -14.4 |

No other string re-bow deepened by more than 1.5 dB.

**The trace at 39.879 (0.1 s bins).**
- Celli: -35.5 before; -44.6 / -45.1 at +0.0..+0.2 s; -40.2 at +0.3 s; back at +0.5 s.
- The fitted shape (`rebow_fills.json` Violoncellos "39.879") sits at -0.7..-1.9 dB over +0.0..+0.24 s and reaches +7 only at +0.40 s.
- The fill therefore comes after the hole. The c21 Sus MAX release cap (Vc mf/f/ff 524 -> 250 ms) makes the old piece end sooner, so the hole is earlier and deeper.
- The re-bow falls on the bassoons' breath (qn 40; Bn1 -8 dB, Bn2 -5.7 dB in +0..+0.3 s). The master drops 1.8 dB over those 0.3 s, so the celli add a hole where the phrase already breathes.

**Why the c21 celli refit was rejected (c21 CHANGES).** It lowered bars 73-77 by 2.4-3.6 dB. That was a whole-track refit.

**Fix.**
- `tools/fit_rebows.py 21 --tracks Violoncellos`, keeping only the rows 39.879, 41.38 and 49.683. Merge them into a copy of the old table (LEARNINGS c10: `--write` drops skipped rows). All other celli rows are unchanged, so bars 73-77 keep their level.
- Hold-max as in c21.
- The fix is level-only, so `stem_fix.py` can apply it to the c21 stems first.

**Pass.**
- Celli dip at 39.879 -5 dB or shallower.
- 41.38 / 49.683 at their c20 values (-2.6 / -6.0) or better.
- Celli level 36-52 within 1 dB of c21.
- Master at 39.879 no deeper than -2.0 dB.

## 3. Accents on the three release-capped tracks have not been refit, and some moved by 2-4 dB (measured)

**Evidence (measured; `accpk2`: long accents, peak minus the peak of the unaccented notes in the 2 qn before; c20 -> c21).**
- String accents over the preceding notes by more than 6 dB: 27 -> 31.
- The moves of more than 1.5 dB are mostly on the capped tracks:

  | Track | Accent (qn) | c20 | c21 |
  |---|---|---|---|
  | Violoncellos | 311 | +1.9 | +6.3 |
  | Violoncellos | 317 | +2.8 | -1.8 |
  | Violoncellos | 526 | +5.3 | +7.3 |
  | Violoncellos | 124 | -2.8 | -0.9 |
  | Double basses | 88 | +4.6 | +2.5 |
  | Double basses | 97 | +3.0 | +0.1 |
  | Double basses | 542 | +3.1 | +1.5 |
  | Violas | 147 | +5.3 | +7.4 |

- On uncapped tracks: Violins II 124 +3.7 -> +6.6, 479 +5.5 -> +7.7 and 564 +3.5 -> +1.3 (render variation or neighbours).
- Shorter tails lower the "preceding notes" peaks, so the accents read higher. On the basses the accents fall, because their own tails no longer swell.
- The 2-5 kHz fronts are unchanged (string median -3.5), so this is weight, not bite.
- The actor listed the refit as open for c22 (c21 CHANGES).

**Fix.**
- `tools/fit_accents.py` on c21 for Violas, Violoncellos and Double basses, with the c17 options (`--peak-long-qn`, `--max-total`, strings cap 4.5). Use `--skip` for the hand values: Vc 321 DOWNBOW, the 536 subito notes, Vla/Vc 607 strokes.
- Then refit `fit_accent_bodies.py` on the same three tracks.
- Add Violins II 124 and 479 only if the fitter's own measure agrees: past cycles found that the fitter and this measure disagree on long accents.

**Pass.**
- Fitter's string accent excess median ≤ +3.5 dB.
- Celli 311/526 and Vla 147 within 2-4 dB on its measure.
- Basses 97/542 back to ≥ +2 dB.
- 2-5 kHz front minus body not raised (string median ≤ -3.0).

## 4. The release cap left the release-trail samples alone, and on the violas and Violins I those trails are 1.2-1.7 s long (patch data measured; audible effect inferred; test)

**Patch data (measured, `opus_state.load_oib`, Sus MAX row groups; AHDSR release).**

| Patch | Sustain groups | Release-trail ("RT") groups |
|---|---|---|
| Violas KS Master | 333-931 ms | 1660 ms (all dynamics) |
| 1st Violins KS Master | 323-931 ms | 1245 ms |
| Celli KS Master | 524-931 ms | 131-166 ms |
| Basses KS Master | 524-931 ms | 131-166 ms |

- The RT groups have `releaseTrail: true` and `releaseDamping 0.8`. They are triggered at the note-off, so their AHDSR release is how long the recorded release plays.
- The legato rows have no RT groups. This fits the c20 finding that the same stems stop 2-3 times faster on Leg Slur MAX.
- `cap_release()` skips every group whose name ends in "RT", by design.

**What the render shows (measured, `relsus.py`, Sus MAX strings, time to -10 dB after the last note before a rest of 0.6 s or more).**
- Basses, c20 -> c21: 0.51 -> 0.34, 0.31 -> 0.19, 0.35 -> 0.26, 0.36 -> 0.26 s (short RT). The cap worked.
- Violas: 0.43 -> 0.38, 0.26 -> 0.25, 0.24 -> 0.18, 0.27 -> 0.15, 0.20 -> 0.20 s. This is mixed.
- The violas' off-beat dyads in bars 131-134 still drop only 5.8 dB in their 0.18 s rests (`rests2`; c21 pass target 7).
- Violins I (not capped): 0.20-0.26 s at f-ff.
- Celli: still 0.29-0.40 s at CC11 114 (125, 128). Their RT is short, so the rest of their tail has another cause, not found here.

**Fix (test, Violas only).**
- `tools/build_reaper.py cap_release()`: a new spec key `"rt_ms"`. When it is set, cap the release of the listed rows' "RT" groups of the listed dynamics as well.
- `build/mix.json` Violas: `"sus_release_cap_ms": {"ms": 250, "rt_ms": 400}`.
- This needs a full Violas rebuild and no new rows, so memory is unchanged.
- Leave Violins I until the violas result is known: its Sus MAX notes are few (54).

**Pass.**
- Violas' rest drop in bars 131-134 ≥ 7 dB.
- Violas Sus MAX -10 dB median ≤ 0.20 s.
- No change of more than 0.5 dB in violas held-note levels.
- Re-bow dips not deeper than c21; refit the violas `rebow_fills` if they are.

## 5. Horn 4 legato joins at qn 415 and 453 opened after the c21 horn rebuild (measured; low priority)

**Evidence (measured).**
- Horn 4's MIDI, CC11, CC1 and keyswitches over 410-456 are identical in the c20 and c21 rendered builds.
- Joins (`joins.py`), c20 -> c21:
  - 415 (E3 -> D3, bar 104): 2.0 -> 5.9 dB.
  - 453 (bar 114): 0.1 -> 5.2 dB.
  - Track median 0.2 -> 1.5.
- Traces at 415:
  - c20 rises straight to -35.4 at +0.05 s.
  - c21 holds -42.7..-43.1 to +0.15 s, then falls to -51.5 at +0.25 s, and is back only at +0.6 s.
- At 453 c21 sags 6.5 dB over +0.05..+0.5 s, where c20 was flat.
- Horn 4 sits 12.5-13.5 dB under the master, so the master does not show it. It is the bottom of the horn chord in bars 104 and 114.
- Horn 3 165 went 2.8 -> 3.9 dB. The rebuild (width 0.15, seats) changed legato behaviour that the data did not.

**Fix.**
- Rerun `tools/auto_fills.py 21` for Horns 1-4 only and accept new fills on Horn 4 415 and 453 (about +4 dB, held to +0.35 / +0.45 s).
- If the width is reverted at the next horn rebuild (c21 C #3), re-measure these two joins before keeping the fills.

**Pass.** Horn 4 joins 415 and 453 at 3 dB or less, with no overshoot over the body of more than 2 dB.

## Patches

- The basses' repeated-eighth problem (#1) does not need a new row. Marc Shrt (c03) and Detache (c13) failed. The untried rows also look unpromising:
  - Stac On Bow RRx9 has a 749 ms release;
  - Staccato RRx9 has a 1330 ms release.
  
  Their tails would fill the eighth gaps in the same way. `Repetitions TS` is tempo-synced and not suited to a pedal that changes pitch every bar. The level dip is the cheaper test.
- #4 is a patch-state change, not a patch swap.
- I found no other Hollywood Orchestra patch to recommend this cycle. The legato, staccato, pizzicato, tremolo, flautando and a2 horn choices all pass on this render.
- HB has 2- and 3-trumpet ensemble patches (`Hollywood Brass Instruments/2 Trumpets`, `3 Trumpets`). The trumpet parts here are mostly in thirds, so they are not unison doublings. Not recommended.

**Do not touch:**
- GENTLE_ACCENT, ACC_ART_LEAD and the brass/wind accent fits (brass 2-5 kHz front -8.4 dB);
- sus_release_cap_ms on the basses (it works) with the c21 basses/violas rebow_fills;
- the c21 607 strokes, LEG_CAP_FRAC "listed" with the celli leg_leads, and LEG_MIN_GAP_S;
- the Slur Runs spans, `_lg()`, SLUR_HEAD_LEAD 0.10 and GROUP_LEAD_AT;
- the coda basses steps (fold 7.7 dB);
- MEAS_TREM alt_row; TREM_JOIN/TREM_SPLIT;
- WIND_DETACH, RETONGUE_LEAD_S and WIND_REP_RETONGUE;
- breath splits and CAESURA_BREATH_QN (Horns a2 gaps 0.30/0.09 qn);
- harp env_release_ms 200 with HARP_RING_S;
- TIMP_CC1_MAP / TIMP_ROLL_TRIM_DB and the re-strike plans;
- _REBOW_FROZEN and every re-bow row except the three in #2;
- sus. cymbal key 64 / lead 0.25.
