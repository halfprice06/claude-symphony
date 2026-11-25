# Cycle 9, critic A: articulation and phrasing (render c08)

Scope: every wind, brass, string, timpani and harp note in `build/parts.json` (the c08 build after its stem fix, which is what `cycles/c08/render/` carries), measured on the c08 stems and master. Scripts and 5 ms feature files are in `/private/tmp/claude-501/mockup-loop/mvt1-c09-A/`: the c08-A scripts rerun on c08 (`accfam.py`, `joins.py`, `tremj.py`, `rebow.py`, `longloop.py`, `breath.py`, `hrep.py`, `stacsep.py`, `ten2.py`, `susbloom.py`, `timp.py`, `chordleg2.py`, `ties.py`, `notelv.py`, `trace.py`), plus new `hp.py` / `hp2.py` (CC11 and level across short untargeted hairpins) and `harp.py` (per-pitch ring of harp chords after an étouffez). Nothing under `build/` or `tools/` was written; `tools/fit_rebows.py` was run without `--write` to read its summary.

## Checks that passed (measured)

- **Accents, Dan's item 8.** `fit_accents.py`'s measure on the fixed c08 stems: strings 112 of 137 in 2-4 dB over their neighbours (median +3.05, 3 under 1 dB), winds 114 of 146 (median +3.04), brass 33 of 36. The remaining highs are the slur-pickup artefact the fit now skips (Oboe 1 / Flute 1 / Clarinet 1 553). 2-5 kHz first 80 ms minus body: medians string -10.2, wind -11.4, brass -14.3 dB; the only positive readings are the known window artefacts (Violas/Bassoon 1 536, Horn 1 124/665).
- **Legato.** No chord or held overlap on a Leg row. Join dips: median 0.4-3.5 dB on winds and brass, 1.6-2.7 dB on strings; 6 dB or more on 2-4 joins per string section and the three known wind/brass holes (below).
- **Staccato** separates 8.4-15 dB per note on every track; **ties** re-attacked only at the planned timpani tie strokes and the basses' "change bow at will"; **breaths** dip 4.8-19 dB everywhere (Flute 1 636 now -4.8, Horn 4 512 -9.3, Horn 3 256/536 -6.0/-7.1); **timpani** metric weight holds (off-beats in bars 131-134 2-9 dB under the next downbeat); pizzicato and the harp's rolled chords unchanged.
- **Dan's item 7.** No wind or brass note of 9 s or more loops above 0.6 at the period. String re-bow dips are a median 0.9-3.8 dB per section and 1.4-2.3 dB on the master, unchanged from c07. The largest remaining re-bow "steps" (celli 163.877 -9.3 dB, 727.116 -7.9 dB) fall inside printed decrescendos (sf > mf > pp at bar 41, the morendo), so they are mostly the printed fall, not a re-bow fault.

## 1. The second theme's signature figure collapses on its quarter note and then surges on the tenuto (Horn 1, celli, violas; bars 47-48, 147-148, 171-172)

**Measured.** The theme (Horn 1 "1. dolce" with the celli in bars 47-48, Horn 1 + violas + celli "dolce" in bars 147-148, celli "espr." in bars 171-172) is a held note with a long `<`, a `>` over the last eighth, a quarter, and a slurred tenuto half note under a new `<`. The `>` is half a beat long (0.27 s at q=112) and has no printed target. Its CC11 drop and the level of the quarter that follows:

| Track, quarter at qn | CC11 at the eighth -> quarter | Quarter (0.05-0.35 s) minus the eighth before | Tenuto peak minus quarter |
|---|---|---|---|
| Horn 1, 188 (bar 48) | 81 -> 61, then 56 at the tenuto (10 CC portato notch) | -9.6 dB (body -48.7 against -40.0) | +15.8 dB (-48.6 -> -32.8 at qn 190) |
| Horn 1, 588 (bar 148) | 80 -> 61 -> 56 | -8.9 dB | +11.8 dB |
| Violoncellos, 684 (bar 172) | 74 -> 61 (`HP_TARGET_AT` 683.5 "mp") | -9.0 dB (body -42.8 against -35.4 on the held note) | +8.0 dB |
| Violoncellos, 588 | 86 -> 74 | -6.9 dB | +7 dB |
| Violas, 588 | 86 -> 74 | -6.2 dB | |
| Violoncellos, 188 | 84 -> 74 | -4.8 dB | |

On the master, beat 1 of bar 48 falls 3.5 dB under the beat before (qn 187 -32.5, 188 -36.0 dB) and then rises 6.8 dB to qn 190 (-29.2). Horn 1, the melody, goes from 5 dB to 12-15 dB under the master for that beat, so the tune passes to the celli for one note and comes back loud.

Cause (from `hairpins_and_marks()` in `tools/score_to_parts.py`): an untargeted `>` right after an untargeted `<` returns to the level where the `<` started (the c09 "mdv" rule), so a 3.5-qn swell is undone inside half a beat; the next `<` then starts from that floor, and the `PORTATO_JOIN_AT` notch (`SOST_NOTCH` 10 CC) on Horn 1's tenuto at 189/589 deepens it. Of the 16 short untargeted hairpins in the score with a 12 CC or larger move, every decrescendo lowers the next note 2.7-9.6 dB and every crescendo raises it -2.7..+4.7 dB.

**Inferred.** A hairpin over one eighth is a nuance of 1-3 dB, not a change of dynamic level. This is the most exposed melody of the movement after the first theme, and the lurch comes back in all three statements.

**Fix.**
1. `tools/score_to_parts.py` `hairpins_and_marks()`: new `HP_SHORT_S = 0.6` and `HP_STEP_SHORT = 6`. An untargeted hairpin lasting `HP_SHORT_S` seconds or less (tempo-aware, so the 1-qn hairpins of the Lento at q=50 are not caught) moves at most `HP_STEP_SHORT` CC; in the mdv branch, a short decrescendo's target is `max(last_un[1], level - HP_STEP_SHORT)`, and the line returns to the `<`'s starting level only over the next hairpin or note.
2. `build/score_config.py`: drop `HP_TARGET_AT["Vc"][683.5]` ("mp"), so the celli's bar-171 `>` follows the same short rule (or set it to "mf-" if the dictionary needs an entry).
3. `PORTATO_JOIN_AT` notch: add `PORTATO_JOIN_NOTCH = 4` and use it at the `portato_join` line of the notch pass (`notches.append((n["qn"], SOST_NOTCH))` near line 1820) instead of `SOST_NOTCH`. That keeps the c04 attack fix and removes 6 CC from the hole at 189/589.
4. Then refit Horn 1's and the celli's accents only if `fit_accents.py` lists one inside qn 184-205, 584-605 or 680-696 (none are accented now).

**Pass.** On Horn 1, celli and violas at 188, 588 and 684, the quarter (0.05-0.35 s) sits within 3 dB of the eighth before it and still 1 dB or more under it. The tenuto's peak is 5 dB or less over the quarter. On the master, beat 1 of bars 48/148 is within 1.5 dB of the beat before. Re-bow rows are unchanged.

## 2. Violins I's theme heads still carry no accent (bars 17, 29, 120; 3 of the first theme's 5 statements)

**Measured.** The accent fit is at its caps (+5 dB swell, +5 dB step) on Violins I 57, 65, 113 and 479, and the measured accents still sit under or level with the notes around them:

| qn | Measured over the neighbours | Residual (samples and row, without the envelope) |
|---|---|---|
| 57 | +2.2 | -4.1 |
| 65 | **-0.2** | **-6.6** |
| 113 | **+0.3** | **-6.2** |
| 479 | **-0.3** | -5.0 |
| 521 / 529 (control, ff) | +3.0 / +3.0 | -4.5 / -3.9 |

Each of these notes is an eighth pickup (down-bow) slurred to an accented dotted quarter 8-12 semitones up, on Leg Slur MAX (479 on Leg BC MAX). The pickup sounds only 0.13 s before the legato target starts (the 0.17 s lead), and the target reaches its body 0.3-0.4 s after its onset: at 65 the window reads -32.8 dB and the body -29.4 dB. The weight comes a quarter-beat late, inside the transition sample. LEARNINGS c08 records the same limit.

**Inferred.** In bars 17, 29 and 120 the leading voice of the first theme starts without its accent. The listener hears the accent on bars 15, 19 and 131 and not on these.

**Fix (test, revertible).** Play these four accents as fresh Sus MAX strokes. That is the c02 rule for accents after Sus eighths (`acc_sus`), extended to a listed slur target. The Sus rows sit 2-6 dB over Leg at the same CC11 (LEARNINGS c05/c07), which is the size of the missing residual.
- `build/score_config.py`: `ACC_SUS_AT = {"Violins I": [57.0, 65.0, 113.0, 479.0]}`.
- In `score_to_parts.py`: the pickup ends at the accent's score onset + 0.02 qn and keeps its row. The accent takes Sus MAX at the string mid entry lead (0.12 s), without the legato lead.
- Drop the four entries from `accent_fits.json`. `fit_accents.py` marks them invalid when the row changes, and the next refit starts from the default swell.

**Pass:**
- 57, 65, 113 and 479 each +2..+4 dB over their neighbours.
- 2-5 kHz first 80 ms minus body 0 dB or less.
- The pickup no louder than the accent's first 0.35 s.
- Onset (body - 6 dB) within 0.06 s of the score.

Revert any note that fails, and keep the others.

## 3. The doubled horn and trumpet lines are still one solo sample +3 dB (closing theme, climax, coda)

**Measured.** `find_unisons()` drops 84 Horn 2 notes and 21 Trumpet 2 notes; the kept Horn 1 / Trumpet 1 notes play them at +3 dB on the solo patch. The spans are 272.5-286 (bars 69-72, the closing theme in horns a2), 381.5-404, 628-643.5 (the climax) and 664.5-676 (bars 167-169, "a2" horns and trumpets ff). Horn 1 sits 8.4-13.4 dB under the master there and Trumpet 1 9.2-14.7 dB under. Kit section 8 measured identical-patch unisons at 0.999 correlation: one player made louder, not two.

**Inferred.** At the two loud statements of the closing theme the horns sound like one strong solo horn, without the width and slight beating of two. This is the only place left in the movement where a dedicated recorded patch would change the instrument's colour rather than its level.

**Fix.** As c08-A #3: track `"Horns 1-2 a2"` on `2 French Horns/06 Keyswitch/2FH KS Master.oib`, with Sus MAX and Leg Slur MAX rows only, Close 0.5 / Main 1.0, and gain Horn 1 + 4.6 dB (kit c18). Add an `A2_ROUTE` that moves only the unison-dropped notes inside the spans (Horn 2's own notes at 276.0 and 668.0 stay put). Do the trumpets (`2TP KS Master`, map via `dump_ks.py`) in a later cycle.

**Memory.** The deferral reason was memory. c08 ended at 43 GB with 3.6 GB compressed. Movement II ran 32 instances including this a2 horn track at 44 GB after the row cut (kit section 11, c24-c26), and one instance with two rows is about 1 GB. A new track needs the usual restart before the render. Read `top` after loading settles. If REAPER exceeds 45 GB, unload it and record the figure.

**Pass:**
- a2 track level over 272.5-286 and 664.5-676 within ±1 dB of c08's Horn 1.
- Join dips no worse than Horn 1's median of 1.1 dB.
- No chord on its Leg row.
- REAPER 46 GB or less after the render.

## 4. Tremolo entries after a held note open with a hole, and the celli's tremolo split points dip 4-5 dB

**Measured** (`tremj.py`: the lowest 0.1 s level within 0.8 s of the change, minus the lower of before and body):

| Change | Stem dip | Master dip | Context |
|---|---|---|---|
| Violins II, 304 (Leg Slur MAX -> Tremolo, p, bar 77) | **-10.2 dB** | -0.6 | 9 dB hole for 0.2 s (-43 -> -52 dB at 304.1) |
| Violins I, 664 (Leg BC -> Tremolo, f, bar 167 arrival) | -5.2 dB | | Stem -44.6 dB at the onset against -35 before; body at +0.15 s |
| Violins I / II, 484 (Leg BC -> Tremolo, fff) | -6.8 / -7.2 dB | -0.4 | Includes the 0.5 qn arrival hold-back |
| Violoncellos, 464 (Leg BC -> Tremolo) | -4.9 dB | | |
| Celli split pieces 469.868 / 476.328 | -4.2 / -4.6 dB | -0.0 / -1.0 | c08's TREM_SPLIT, new tremolo attack at each piece |
| Violins II piece 592.333 | -3.4 dB | | The c08 open item, 0.33 qn after a chord change |

The other 36 tremolo changes dip a median 1.2 dB (master 0.6). Every listed case starts a new note on the Tremolo row without a lead. The previous note ends 0.03-0.07 qn before the score onset, and the tremolo attack takes 0.1-0.2 s to reach body.

**Inferred.** The violins' coda tremolo (bar 167) and the second violins' p tremolo at the start of the development begin with a gap before they sound.

**Fix** (`tools/score_to_parts.py`, generic):
1. `TREM_ENTRY_LEAD_S = 0.08`. A Tremolo note whose previous note on the track (any row) is held to within 0.1 qn of its onset starts that much early; the previous note ends at the score onset + 0.15 qn (the `ABUT_LEAD` pattern; skip re-bowed notes, as `ABUT_LEAD` does). This covers 304, 464, 484 and 664.
2. `TREM_SPLIT["clear_qn"]` 0.3 -> 1.0 (Violins II 592.333; the c08 note).
3. Put the `trem_splits` pieces into `fit_rebows.py` as re-bows (same `rebow_fills.json` keying by qn), or, more simply, give each split piece a fixed +3 dB fill (full at +0.03 s, held to +0.2 s, gone by +0.35 s), the mirror of the timpani re-strike dip.

**Pass:** every listed change dips 3 dB or less on the stem; the master at 484 and 664 unchanged within 0.5 dB.

## 5. The harp's étouffez is not played: the mf chord rings into the sub. p arpeggio (bar 62) and through the damped rests (bars 163-164)

**Measured** (`harp.py`, peak energy within ±1.5% of each pitch, 0.4 s windows). At qn 244 (bar 62, "étouffez", sub. p), the bar-61 chord (F♭: E2, E3, E4, A♭4, C♯5) is still sounding:
- E3 reads 28.7 / 13.8 / 21.5 / 17.9 dB in the first 1.6 s.
- When the arpeggio's E♭3 enters at 245.5, E♭3 reads 24.9 dB with E3 at 21.5. That is a semitone clash 3 dB apart for about 0.8 s.
- Under the new E♭2-A♭2 bass, E4 decays only from 28.8 to 14.4 dB over the first 1.2 s.

The harp stem is 8-14 dB under the master here, in a quiet passage. At 650 (étouffez over a rest) the F2 of the bar-163 chord rings 21 -> 13 dB through the rest, but the stem is 18-25 dB under the master. At 654 (étouffez m.d.) the right-hand A♭5-D6-F6 ring under the new left-hand G1/G2.

`score_to_parts.py` has no étouffez rule. Harp Sus RR rings after note-off and loses only 2-4 dB in 0.4 s (kit section 9), so shortening the note does nothing, and no Hollywood Harp patch is damped.

**Inferred.** In bar 62 the second theme's sub. p arpeggio starts over a ringing E-major chord, so a soft A-flat minor colour sounds blurred and dissonant.

**Fix.** Route the notes that a printed étouffez damps (the 242.0 chord; the 648.0 chord; the 652.0 right-hand chord) to a second `Harp Sus RR.oib` track, "Harp (damped)" (one row, same seat/mics/gain as Harp). Its volume envelope falls by 30 dB over 0.08 s at the étouffez point (244.0, 650.0, 654.0) and is restored before its next note. Use the c06 percussion damp pattern with `tail_hold` off.
- Cheaper alternative: shorten the Opus AMP ENVELOPE release on the Harp instance (HO manual p. 86) and end the damped chords at the étouffez. This is unverified: `opus_state.py` would need the release field located in the state blob.

**Pass:** at 244.0-246.0 the E3/E4 energy is 15 dB or more under the new arpeggio notes within 0.2 s; the 650-652 rest is silent in the harp stem within 0.3 s.

## 6. Smaller items (measured)

- **Wind and brass legato holes left from c07** (`auto_fills.py` was not run in c08): Horn 2 453 (10.1 dB), Flute 2 279 (10.3 dB), Horn 2 266 (6.6 dB). Run `auto_fills.py` on c08 for these three, or hand-fill dip - 3 dB held to the sag minimum (kit section 6).
- **String joins of 6 dB or more**: Violins II 637 (7.8, right after the fff downbeat) and 245; Violins I 720 (7.5, the last Lento phrase) and 279; celli 365/369 (7.6/6.3) and 8.0 (7.3, bar 3 of the Lento, celli stem 1.4 dB under its own line); violas 517. These are `JOIN_NOTCH` / `early_fills` candidates for the next `auto_fills.py` pass.
- **Celli Lento re-bows** 49.683 (dip -8.3 dB) and 37.377 (step +5.1 dB). These are outside any printed hairpin, in the exposed intro, and still deferred since c07. Refit only these two with `fit_rebows.py 8 build/parts.json --tracks Violoncellos` and keep the other celli rows. The full-track refit summary moves 12 holds by 3 dB or more, which is too much to take blind.

**Do not touch:**
- `accent_fits.json` and the `GENTLE_ACCENT` articulations for all three families (2-4 dB on 259 of 319 accents, 2-5 kHz attack minus body negative everywhere).
- `--keep-long-qn` and `--pickup-qn`.
- `ROW_TRIM_DB` with `ROW_TRIM_SKIP`.
- `TREM_JOIN` spans and the celli 464-484 split seeds.
- The c08 horn breaths and Horn 4 re-tongue.
- `WIND_REP_RETONGUE`, the slurred-repeat merges, `REP_SPLIT`, `STR_SHORT_AFTER_SUS`, `DOWNBOW_STROKE_AT` with `LEVEL_SHAPES`.
- `PORT_TARGETS` and `META_DB`.
- `METRIC_TIMP_DB` and `METRIC_BOWED`.
- Staccato rows, pizzicato and harp velocities.
- `AUTO_REBOW` rows, `space_rebows` and the fitted re-bow shapes.
- Re-strike plans and `BREATH_SPLIT_AT`.
- `TIMP_DELAY_S` and the cymbal timing.
- The climax order (160 > 122 > 169).
