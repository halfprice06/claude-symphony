# Cycle 13, critic A: articulation and phrasing (render c12)

Scope: every wind, brass, string, harp, timpani and percussion note in `build/parts.json` (the c12 second render after its two stem fixes, which is what `cycles/c12/render/` carries), measured on the c12 stems and master, plus the patch tables read from the `.oib` files with `opus_state.load_oib`.

Scripts and 5 ms feature files are in `/private/tmp/claude-501/mockup-loop/mvt1-c13-A/` (`feat_c12/`, `out_*.txt`):
- The c12-A battery, rerun on c12: `joins`, `tremj`, `rebow`, `rbctl`, `rbiso`, `longloop`, `final`, `breath`, `hrep`, `stacsep`, `ten2`, `tenm`, `headfig`, `ties`, `timp`, `timpl`, `timpcr`, `harp`, `pizz`, `arco`, `solo`, `susbloom`, `slaud`, `slurc`, `detw2`, `detw3`, `integ`, `integ2`.
- New scripts:
  - `meas16.py` / `meas16b.py`: modulation at the note rate for repeated notes and tremolo.
  - `fold.py` / `fold2.py`: level folded on the score grid at the note rate.
  - `repsep.py`: same-pitch re-attack dips.
  - `pick.py` (`out_pick.txt`): accents against their pickup notes.
  - `accfront.py` / `acchf.py` / `h273.py`: accent fronts and 2-5 kHz.
  - `ovl.py`: overlap of slurred legato targets.
  - `slaud2.py`: slurred notes on Sus rows, by cause.
  - `vibtab.py` / `vibam.py` / `vibam2.py` / `am3.py` / `amref.py`: string CC1 vibrato tables and level modulation, against the Dvořák reference.
  - `tam.py` / `tt.py`: tam-tam patch and strokes.
  - `rel679.py`: the release into the bar-170 fermata.
  - `hem.py`: the bars 23-25 hemiola accents.
- I did not run `tools/fit_accents.py`: it swaps `build/accent_fits.json` during a run, which is a write under `build/`.

## Checks that passed (measured)

- **Legato integrity.**
  - No chord sits on a monophonic Leg row.
  - Of 1101 slurred legato targets, all overlap their previous note except:
    - the three wide-leap portato tenutos (Fl1 395, Ob1 407, Hn1 415), chosen in c06/c07;
    - eight 0.05 qn slur seams.
  - Join dips, median per track: 0.1-3.5 dB.
  - Joins of 6 dB or more: Vln I 2, Vln II 4, Violas 3, Celli 4, the same joins as on c11.
  - Every keyswitch sent while a note sounds falls 0.06 qn before an abutting next note.
- **Tongued against slurred winds** (`detw2.py`): hole -5.7 dB tongued against -4.1 slurred. This passes; brass is #5.
- **Re-bows (item 7).**
  - The master's dip at the 92 re-bows has a median of -1.97 dB; at control times it is -2.08.
  - Final chord: autocorrelation at 3.95 s is under 0.2 in level, 100-300 Hz and centroid, on the master and on every string stem.
- **Accent bite (item 8)** (`acchf.py`). 2-5 kHz in the first 80 ms minus the body, on accents within 15 dB of the master:
  - brass median -7.8 dB (91 accents);
  - winds -5.9;
  - strings -4.5.

  Over +3 dB are:
  - the known window artefacts (Violas/Celli/Bn1/Cb 536, Violas 120);
  - Clarinet 1 120/558 (+5.2/+6.0, not examined; the clarinet is 13-15 dB under the master there);
  - Horn 1 273 (+3.2, unchanged since c11; see #2).
- **Hemiola accents, bars 23-25** (`hem.py`): the accented quarters stand 3-6 dB over their neighbours on violas, Vln II and basses (violas 88/91/94/97 at -35.1/-35.4/-34.0/-28.8 dB against -40..-37 for the notes between).
- **Other articulations.**
  - Tremolo joins: median -0.8 dB, 1 of 35 at 4 dB or more.
  - Staccato separates 6.8-14.8 dB per track.
  - Pizzicato decays a median 11 dB by +0.4 s.
  - Breath marks dip 3.5-15 dB.
  - Timpani tie strokes are present.
  - Harp étouffez is as on c11.
- **Timpani rolls brighten through their crescendos** (1-8 kHz share, `timpcr.py`): 40-44 from -38.5 to -20.7 dB, 156-160 from -32.4 to -15.6, 480-484 from -21.2 to -13.3.
- **Release into the bar-170 fermata rest** (`rel679.py`):
  - All 25 sounding stems end within 0.00-0.05 s of the beat.
  - The master is down 19 dB at +0.5 s and 35 dB at +1.2 s: a clean common cutoff with the hall ringing.
- **No silent notes:** no note sits 30 dB under its track's median.
- **Tam-tam soft stick at 696** (`tt.py`): dark, centroid 130-175 Hz against 740-1640 for the heavy-beater fff at 484. The patch has only one beater (Long/Short/Crs groups), so the low velocity layer is the right choice.

## 1. The celli's measured tremolo (bars 117-121) plays as an unmeasured tremolo: the sixteenth-note motor under the build to the fff of bar 122 is missing

**Score.** `sections/dev.ily` line 365-366: the celli have `g,1:16\f | g,1:16 | g,1:16 | g,1:16 | g,1:16\< | aes1\fff`. These are two-slash whole notes, which means repeated sixteenths.

This is the only `:16` tremolo in the movement. Every other string and timpani tremolo is written `:32`. Bars 127-130 then write the same low G out as quarters, eighths, triplets and sixteenths.

Adler (reference-books/text/adler1, p. 50, Example 11-47) defines bowed measured tremolo as shorthand for "a series of repeated détaché notes" for energy and volume.

**Measured.**
- `score_to_parts.py` builds `trem_q` from every `tremolo` event regardless of its value (line 1309). The three celli notes at 464 / 469.70 / 477.01 (the c08 `TREM_JOIN` span `(464, 484)` and its `TREM_SPLIT` pieces) play the `Tremolo` row.
- On the celli stem, the 1-8 kHz level folded on the sixteenth grid (`fold.py`) has a depth of 0.5 dB over 464-480 (0.4 dB in full-band level). The sixteenth-rate band is -10 dB of the 1-30 Hz modulation, with no peak.
- Bar 130's written-out sixteenths (`REP_SPLIT` strokes on `Stac RRx9`) fold to 4.1 dB at 1-8 kHz on the same stem. Bar 129's triplets fold to 8.0 dB.
- Celli level in bars 117-121: -31.4 / -33.0 / -29.6 dB (464-472 / 472-480 / 480-484), 14 dB under the master.

**Inferred.** A real section playing f détaché sixteenths on low G gives the passage its drive into the fff. The render has a smooth rumble there instead, and the written-out acceleration of bars 127-130 then has no earlier sixteenths to refer back to.

**Fix** (generic, `tools/score_to_parts.py`):
1. Where `trem_q` is built, keep the tremolo value. A note whose tremolo value is 16 or 8, and whose subdivision (4/value qn) lasts at least 0.1 s at the local tempo, is measured.
2. Expand each such note at the input stage into abutting same-pitch notes of 4/value qn (here 80 sixteenths of 0.25 qn, through the bar-121 allargando on the tempo map).
3. Let them take the existing `REP_SPLIT` path: under `stac_s` 0.2 s they play `Stac RRx9`, a row the celli already load, with `REP_SPLIT["stac_vel"]` from CC11. The bar-121 crescendo (CC11 89 to 124) then comes through velocity and CC11, as in bar 130.
4. Remove `"Violoncellos": [(464.0, 484.0)]` from `TREM_JOIN` (build/score_config.py line 331) so no `TREM_SPLIT` pieces are made there.
5. Set the level from the render with a celli role over 464-484 (the strokes and the tremolo row will not match). Fix it by stem fix.

Alternative row: `Meas Trem TS` (Celli KS Master key 81). It is a recorded measured tremolo with pp/mf/f/ff layers, but its samples are tempo-synced at 145 bpm. At 126 that is a 13% stretch, outside the ±10 bpm the HO manual advises (p. 52). Try it only if the strokes sound mechanical.

**Pass:**
- Celli 1-8 kHz fold depth on the sixteenth grid of 3 dB or more over 464-480 (bar 130 gives 4.1).
- Level per bar within ±1.5 dB of c12.
- Master over 464-484 within ±0.5 dB.
- The bar-122 fff arrival unchanged (climax order 160 > 122 > 169).

## 2. Theme-head accents sit under their own slurred pickup (closing-theme head bar 69, recap head bar 131, celli bars 78-81)

**Measured** (`pick.py`, `out_pick.txt`): accent body (score onset +0.05..+0.35 s) minus the body of the eighth before it (its onset +0.03 s to the accent's onset).
- Over 171 accents with a pickup, the median is +4.4 dB.
- 15 are under their pickup, 12 of them legato targets.
- The same figure g8( es'4.->) gives very different results:

| Accent | Track | Accent minus pickup | Stem re master |
|---|---|---|---|
| 273 (bar 69, closing theme, Horns a2 ff) | Horn 1 | -1.2 dB | -13 dB |
| 665 (same figure) | Horn 1 | +6.5 | |
| 673 (same figure) | Horn 1 | +6.6 | |
| 521 (bar 131, recap head) | Trombone 1 | +6.9 | |
| 521 | Bassoon 1 | -6.3 | -16 |
| 521 | Celli | -5.6 | -13.5 |
| 317 | Celli | -4.9 | -9.4 |
| 321 | Celli | -2.4 | |
| 311 | Celli | -2.1 | -8.1 |
| 665 | Violas | -2.6 | |
| 558 | Vln I | -1.5 | -8.9 |
| 118 | Vln I | -1.0 | -10.9 |
| 110 | Flute 1 | -3.1 | |
| 409 | Clarinet 1 | -1.9 | |

- On the master the downbeat stands over the pickup by:
  - +0.6 dB at 273 and +0.7 at 521;
  - against +4.0 at 665 and +3.6 at 529.
- Horn 1 273 level trace (`h273.py`, 40 ms steps): pickup -33/-32 dB, then the accented note -37..-36 for 0.4 s, reaching -32 only at +0.4 s. The legato transition sag fills the swell's window. The 2-5 kHz front (+3.2 dB) is the pickup's tail, not an attack.
- `fit_accents` passes these accents because it compares with unaccented notes within 2.5 qn at the same CC11, not with the pickup (c12-A run: Horn 1 273 "over 2.8", fit 1.14 dB).

**Inferred.** At bars 69 and 131 the theme seems to start on its upbeat. The downbeat accent, the strongest point of the head, is lost.

**Fix:**
1. `tools/fit_accents.py`: add a pickup term.
   - For an accent whose previous note on the track ends at the accent's onset and is 0.5 qn or shorter, set `over_pick` = accent level (+0.05..+0.35 s) minus pickup level.
   - Fit the swell to max(the neighbour fit, the swell that gives `over_pick` = +2.5 dB), capped at 5 dB.
   - Measure on c12; the render already holds all these notes.
2. For legato-target accents, hold the swell through the sag: `GENTLE_ACCENT[...]["swell_s"]` (0.04, 0.35, 0.7) when `keep_legato` applies, instead of (0.04/0.07, 0.25, 0.6).
3. Where the 5 dB cap is not enough (Bassoon 1 and celli 521, celli 317), give the pickup a step trim in `build/note_trims.json` instead: "520.5" -3.0 on Bassoon 1 and celli, "316.5" -3.0 and "320.5"/"310.5" -2.0 on celli. Use `NOTE_TRIM_RAMP_S` 0.1, and end the trim at the accent's moved onset (LEARNINGS section 6: no trim may reach into the target).

**Pass:**
- Every listed accent +2 dB or more over its pickup on the stem.
- Master accent minus pickup at 273 and 521 of +2.5 dB or more.
- 2-5 kHz in the first 80 ms minus body at +3 dB or less.
- No new 30 ms spike over +3 dB.

## 3. The a2 doublings are still one solo sample (Horn 2 84 notes, Trumpet 2 21, Trombone 2 29 dropped as unisons; the ff themes of bars 69-72, 157-161, 166-170, recap 131-134)

**Measured** (parts.json `unison_dropped`):
- Dropped unisons: Horn 2 84, Trumpet 2 21, Trombone 2 29, Clarinet 2 57, Bassoon 2 32, Horn 4 21.
- The kept stem leads the a2 statements at:
  - Horn 1 272.5-286: -10.1 dB
  - Horn 1 628-643.5: -11.1
  - Horn 1 662-676: -9.1
  - Trumpet 1 664.5-676: -8.7
  - Trombone 1 520.5-534: -10.7
- On disk:
  - `Hollywood Brass Opus Instruments/2 French Horns/06 Keyswitch/2FH KS Master.oib`
  - `2 Trumpets/06 Keyswitch/2TP KS Master.oib`
  - `2 Trombones EXP/04 Keyswitch/2TB KS Master.oib`
- Kit section 8: two tracks on one patch render the identical sample (correlation 0.999), so the drop is necessary while the copy is the same patch.

**Inferred.** The loudest theme statements sound like one strong player rather than a pair. This has been deferred since c01. The other items in this report are generic rules or level fits, so this cycle is a good one to make it the single patch change.

**Fix** (the c11-A #6 / c12-A #4 plan):
1. Free a slot by putting the Tam-tam (key 36; 484-505, 696) and the Crash cymbals (key 60; 636) in one Opus instance. They never overlap. Keep each one's `LEVEL_SHAPES`, roles, seat and the tam-tam `_damp`.
2. Load `2FH KS Master` on the freed track and route Horn 1's unison windows to it with `TRACK_WINDOWS`.
3. Set its gain to the solo-horn track's +4.6 dB (kit c18), without the +3 dB unison boost.
4. Record REAPER memory: c12 settled at 43 GB; one two-row instance is about 1 GB.

If memory blocks this, an untested alternative is to keep Horn 2's unison copy instead of dropping it, offset by +0.015 s and +4 cents of pitch bend so the two copies are not the same sample. Measure the correlation of Horn 1 against Horn 2 (target under 0.7) and the level (±1 dB of c12).

**Pass:**
- Level per a2 window within ±1 dB of c12.
- Brass accents refit (`fit_accents.py --family brass --keep-long-qn 1.4`).
- REAPER settled under 45 GB.

## 4. The basses' repeated ff eighths sound as a held tone (bars 27-31, 81-82, 131-134, 139-141, 167-169; 128+ notes)

**Measured** (`fold2.py`, `repsep.py`).
- The Double basses play these same-pitch eighths on Sus MAX at 0.47 qn with a 0.014 s gap. `REP_SPLIT` is limited to tracks with Leg BC, so the basses do not get it.
- Level folded on the eighth grid, full band / 1-8 kHz:

| Span | Full band | 1-8 kHz |
|---|---|---|
| 104.5-124 | 1.8 dB | 1.2 dB |
| 520-536 | 1.9 | 2.0 |
| 556-564 | 1.2 | 2.9 |
| 664-676 | 1.2 | 1.9 |
| Held-note control 640-660 | 0.4 | 0.7 |
| 324-328, the one run doubled by timpani strokes | 4.4 | 5.8 |

- Median same-pitch re-attack dip: 0.8 dB at 104-120, 0.3 dB at 664-676.
- c03 tested `Marc Shrt RRx4`. It gave no more re-attack rise and played 6.6 dB louder, so it was reverted.

**Inferred.** The motor rhythm under the first theme's ff tutti and its recapitulation is there in the score but is heard only through the timpani.

**Fix** (a contained test; it loads one row, a full rebuild of the Double basses).
- In the Basses KS Master the `Detache RRx2` row (key 79) is a one-shot recording (no loop; read from the `.oib`: groups "Db Detache rrx1/2", samples "HS Ma Db Det ..."). Unlike Sus MAX, each note has its own stroke and decay, and this row has never been tried.
- Use `ART_SPANS` `{"Double basses": [{"from": 104.0, "to": 124.0, "art": "Detache RRx2"}]}` at the Sus velocity, written length 0.47 qn. Bars 131-134 (520-536) are the control.

**Pass:**
- 1-8 kHz fold depth of 4 dB or more at 104-124, with the control unchanged.
- Level of the span within ±2 dB of c12 (fix by stem fix).
- No re-attack spike over +3 dB.

If it passes, extend it to every bass run that `REP_SPLIT` would select.

## 5. Brass tongued notes: short notes still get no tonguing gap (84 changes, hole -3.2 dB, as smooth as slurred -3.8)

**Measured** (`detw2.py`, holes by gap, brass). `WIND_DETACH["by"]["brass"]` = gap 0.09 s, frac 0.18 (score_config.py line 535):

| Class | n | Hole median |
|---|---|---|
| Tongued, gap about 0.09 s | 241 | -5.1 dB |
| Tongued, gap over 0.095 s | 25 | -7.0 |
| Tongued, gap under 0.06 s | 84 | -3.2 |
| Slurred | 150 | -3.8 |

- The gap under 0.06 s comes from the frac cap: an eighth at 126 gets 0.18 × 0.238 = 0.043 s.
- These 84 changes are in the brass theme lines: Horn 1 31, Trombone 1 21, Trumpet 1 14 (bars 69-72 at 274-284, 98-102 at 391-408, 131-134 at 522-533).
- Brass overall is tongued -4.8 against slurred -3.8: 1.0 dB, where c12 asked for 1.5. Winds pass, with short notes still at -5.4.

**Fix:** `WIND_DETACH["by"]["brass"] = {"gap_s": 0.09, "frac": 0.30}`. An eighth then gets 0.071 s; quarters and longer keep 0.09 s. The 0.06-0.085 s bin measured -5.4 dB.

Refit brass accents afterwards, since their neighbours change.

**Pass:**
- Brass tongued notes with gaps under 0.075 s at -4.8 dB or deeper.
- Slurred unchanged within ±0.3 dB.
- Master dips at the tutti chord changes of 108-124 / 391-408 / 628-644 no more than 1 dB deeper than c12.

## 6. Smaller items

- **Revert the c12 brass `cc1_front` test** (score_config.py lines 577 and 581): measured on c12 as failed. Keep `swell_s` (0.04, ...) unless #2 changes it.
- **Tenuto at 201** (bar 51, Horn 1 + celli): group body minus the quarter before is -3.0 dB, and the master's is -3.3 (`tenm.py`). It has been open since c10. 189/589/601 are fine. Fix: a celli fill on 201 (`early_fills.json` +2.5 dB held to +0.4 s) and Horn 1 `note_trims` "201.0" +2 with ramp 0.1. Pass: group 0..+3 dB.
- **Final-chord horn breath splits re-enter with a bump** (Horn 3 722.3 / 724.6 / 726.6; Horn 4 721.6 / 724.3 / 725.9; `final.py` and level trace).
  - Each new piece rises 3-7 dB over the decaying piece before it for about 0.25 s.
  - The Horn 3 splits come every 2.0-2.3 qn (Horn 3 acf 0.28/0.33 at 100-300 Hz and centroid, the only stem over 0.2).
  - Horn 3 is 10 dB under the master, which moves less than 1 dB (inferred: faintly audible as a slow horn pulse in the morendo).
  - Fix: level shapes in `LEVEL_SHAPES["Horn 3"/"Horn 4"]`, -4 dB at each split onset rising to 0 over 0.5 s, and move Horn 3's 724.6 split to 725.0 so the spacing is irregular.
- **Basses pizz. at 408** (bar 103, D2 v83): peaks at +0.40 s against +0.01..+0.22 for the other pizz. notes, and is flat for 0.4 s (`pizz.py`). The cause is not established (it could be the sample). Listen before changing it.

Do not touch:
- `REP_SPLIT` and its Stac strokes (bar 130 articulates at 4.1 dB);
- `TREM_JOIN`/`TREM_SPLIT` for the upper strings (only the celli span goes under #1);
- `WIND_DETACH` for winds;
- `GENTLE_ACCENT` without accent samples or CC11 bumps;
- `accent_fits.json` (refit only after #2/#5);
- `_REBOW_FROZEN`/`REBOW_AT` with `rebow_fills.json` and `NOTCH_SKIP` (master re-bow dips equal control times);
- `TIMP_CC1_MAP` with `TIMP_ROLL_TRIM_DB`, and the re-strike plans;
- `PORTATO_JOIN_AT`, `DOWNBOW_STROKE_AT` with its `LEVEL_SHAPES`, `ROW_TRIM_DB`;
- harp `env_release_ms` 200 with `HARP_RING_S`;
- the pizz., staccato and tremolo rows;
- the fermata-679 release;
- the climax order (160 > 122 > 169);
- the sus. cymbal timing.
