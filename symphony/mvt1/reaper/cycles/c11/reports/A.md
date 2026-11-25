# Cycle 11, critic A: articulation and phrasing (render c10)

Scope: every wind, brass, string, harp, timpani and percussion note in `build/parts.json` (the c10 build after its stem fix, which is what `cycles/c10/render/` carries), measured on the c10 stems and master. Scripts and 5 ms feature files are in `/private/tmp/claude-501/mockup-loop/mvt1-c11-A/`: the c10-A battery rerun on c10 (`joins.py`, `tremj.py`, `rebow.py`, `longloop.py`, `breath.py`, `hrep.py`, `stacsep.py`, `ten2.py`, `ties.py`, `timp.py`, `harp.py`, `chordleg2.py`, `susbloom.py`, `xall.py`), `tools/fit_accents.py` run without `--write` for all three families (`fa_*.txt`), and new scripts `headfig.py` (second-theme head), `att.py` (attack shapes), `solo.py` (exposed solos note by note), `rbctl.py` (re-bow dips against control times), `pizz.py`, `arco.py`, `fillrel.py`, `lanes.py`. One fix to an old script: c10-A's `harp.py` had `CYC='c09'` hard-coded, so its c10 numbers were c09's. Nothing under `build/` or `tools/` was written.

## Checks that passed (measured)

- **Accents (Dan's item 8).** Predicted from c10: brass 32 of 37 in 2-4 dB over their neighbours, strings 117/135, winds 123/140. 2-5 kHz in the first 80 ms is under the note body for every accent except the known artefacts (Violas 120/536, Bassoon 1 536, Clarinet 1 120, Oboe 1 328). No accent has bite.
- **Re-bows (Dan's item 7).** Across all 92 re-bows, the master's dip at the re-bow is a median -2.01 dB (p10 -3.74). At control times 1.3 s before and after, it is -1.89 (p10 -3.76). The re-bows cannot be told apart from the music around them. No held note of 6 s or more loops above 0.6 in level, 100-300 Hz or centroid at a stem level within 8 dB of the master.
- **Legato.** No chord sits on a Leg row. Keyswitches sent during a legato note are all Leg Slur <-> Leg BC switches for one target (the kit's exception). String legato crossovers have a median of +0.06-0.085 s.
- **Other articulations.** Tremolo joins: median -0.8 dB. Pizzicato onsets: -0.03..+0.05 s, decay about 11 dB at 0.4 s. Staccato separates 5-19 dB per note. Breaths dip 4-19 dB. The 650 harp damp holds (-61..-81 dB).

## 1. The second theme's head still dips at the tenuto that the printed < leads to; the coda statement falls 9 dB (bars 48, 51, 148, 151, 171-172)

**Measured** (`headfig.py`). Level against the quarter before (quarter = from the quarter's onset + 0.12 s to the tenuto - 0.15 s; hole = lowest 100 ms window within -0.3..+0.4 s of the tenuto):

| Tenuto at qn | Master hole | Master, tenuto's first 0.35 s | Stem holes |
|---|---|---|---|
| 189 | **-4.6** | -1.9 | Horn 1 -4.4, celli -4.4 |
| 201 | **-5.1** | -1.8 | Horn 1 -4.1, celli -4.6 |
| 589 | -3.0 | -2.1 | Horn 1 -4.3, violas **-7.1** |
| 601 | +0.2 | +1.2 | (fine) |
| 685 | **-5.6** | -1.1 | celli **-9.1** |

The c10 fills cured the quarter, but in four of five statements the melody now drops at the tenuto, where the printed < arrives.

**Cause** (from `vol_db` in parts.json and `early_fills.json`): the quarter fills (`hold_s` 0.40, gone 0.25 s later) release across the join.
- Horn 1, 188: the envelope is +7.2 dB at 188.75 and -0.2 at 189.25. The tenuto's moved onset is 188.888.
- Celli, 684 (coda, q=72, quarter = 0.83 s): the 684 fill ends 0.12 s before the 685 moved onset (684.796). The envelope falls from +8.0 (684.0) to -0.2 (684.91), 8.2 dB, inside one slur with no hairpin printed between the > that ends at 684 and the < that starts at 685.
- The celli stem goes -32.1 -> -44.9 dB, the master -30.4 -> -38.4. The 685 fill (`pre_s` 0.031) only starts at 684.99, after the hole.
- The tenuto note trims (-4..-6 dB, 0.6 s ramp) then cut the start of the tenuto as well as its bloom at +0.45..+1.0 s.

**Inferred.** This is the most exposed tune after the first theme. A listener hears the line give way on the note it leans toward, most clearly at the coda's portamento (Leg Port MAX, `PORT_TARGETS` 685), where the slide falls into a hole.

**Fix** (level only, so it can be stem-fixed):
1. `build/early_fills.json`: run each quarter fill to the tenuto's moved onset.
   - `hold_s` 0.40 -> 0.55 on Horn 1 `188` / `588`, Violoncellos `188` / `588` and Violas `588`.
   - Violoncellos `684`: `hold_s` 0.40 -> 0.72.
   - Violoncellos `685`: `pre_s` 0.031 -> 0.15, `hold_s` 0.239 -> 0.30.
2. `build/score_config.py` `NOTE_TRIM_RAMP_S`: 1.0 s for the tenuto trims, so the first 0.4 s of each tenuto keeps its level. The trims are Horn 1 189/201/589/601, Violoncellos 189/589/601/685 and Violas 601. Keep the 0.25 s ramps on 191/591.
3. Leave `PORTATO_JOIN_AT` / `PORTATO_JOIN_NOTCH` (4 CC) as they are. They should give a separation of about 2 dB, not 4-9 dB.

**Pass:**
- The master hole is 2.5 dB or less at all five tenutos.
- Each tenuto's first 0.35 s is at least the quarter's level - 0.5 dB on the Horn 1, celli and violas stems.
- No new 30 ms spike over +3 dB at the joins.
- The arrival notes 191/591 stay at or over the crest, as c10 left them.

## 2. The sf of bar 20 is not heard (Violins I/II, qn 78)

**Measured** (`att.py`).
- **The score:** a crescendo through bars 19-20 arrives on an unslurred sf half note: Vln I D♭6, Vln II D♭5 (a new bow, tied into bar 21, then a > to mf).
- **How it is played:** both are Leg BC MAX legato targets (v127, moved to 77.638). Vln II's join is an octave leap, 61 -> 73. The sf CC spike (Vln II 58 -> 87 at 78.25, Vln I 102 -> 107) lands inside the transition.
- **The result**, against the eighth / note before:
  - Violins I: +0.8 dB in the first 0.15 s, +2.2 over 0.15-0.4 s. The peak comes at 78.75, 0.75 qn late.
  - Violins II: **-5.5 dB** in the first 0.15 s and -4.0 after. The sf sits under the note before it.
  - Master: **-0.3 dB** in the first 0.15 s, +0.6 over 0.15-0.4 s.

  2-5 kHz first 80 ms minus body: Vln I -0.7, master -0.8 (no bite, but no attack either).
- This is the only string sf in the movement. The other sf is Fl1 160, and `SF_ARRIVAL_AT` covers it.

**Inferred.** The first theme's first climax arrives with no impulse. A real section takes a new bow there, with weight.

**Fix:**
1. `build/score_config.py`: `DOWNBOW_STROKE_AT` += {"Violins I": [78.0], "Violins II": [78.0]}. This gives a fresh Sus MAX stroke on the Leg -> Sus entry path, and the tie continues on it.
2. `SF_ARRIVAL_AT[78.0] = "ff"` (the crescendo's arrival: the spike reaches ff, then f).
3. Refit only these two notes with `fit_accents.py --family string` if they become neighbours of an accent (none within 2.5 qn now).

**Pass:**
- On both stems, the first 0.25 s of 78 is +3..+5 dB over the note before.
- The master is +2 dB or more over 77.5-78.
- 2-5 kHz first 80 ms minus body is +3 dB or less (Dan: weight, not bite).
- No hole of 4 dB or more at 78.0.

## 3. The development's viola espr. solo drops 4-9 dB on its tenuto peak (bars 107-108, qn 424-431)

**Measured** (`solo.py`, stem 0.1 qn windows).
- The violas play p espr. over Violins II pp div. chords, with the bass clarinet answering. Violas lead alone until the flute doubles them at 432.
- G4 at 424 reads about -40 dB. The E4 quarter at 428 blooms to -36.7 (Leg Slur target, v124).
- The tenuto C5 at 429, the top of the phrase after a rising minor sixth, falls to **-48.7 at +0.12 s** and settles at about -44.5. That is 4.5 dB under the G4 and 8 dB under the E4.
- The master goes -37.2 (428.5) -> **-41.3** (429.0) -> -38.0 (430.0). `ten2.py`: join dip -10.2 dB, tenuto body 7.0 dB under the note before.
- **Causes:**
  - The plan has nothing here. CC11 is flat at 49 apart from the +5 CC tenuto bump, `vol_db` is +0.1, there is no fill, and the violas are not a `LEAD_SPANS` track, so there are no phrase-top contours.
  - The samples fall with pitch at CC 49: C5/D♭5 at -45..-46, against G4 at -40.
- The violas also sit only 2 dB over the pp Vln II chord at 425-427 (-40 against -42).

**Inferred.** The listener hears the solo sag on exactly the note marked for weight.

**Fix:**
1. `build/score_config.py` `LEAD_SPANS["Violas"]`: add (424, 432).
2. `build/early_fills.json` Violas `"429"`: {db 5.0, pre_s 0.10, hold_s 0.30}.
3. `build/note_trims.json` Violas: `"429.0"` +3 (with `NOTE_TRIM_RAMP_S` 0.25: tenuto weight), `"428.0"` -2.5 (the E4 bloom).
4. `build/roles.json` Violas [424, 432, +2.5, 0.5] (espr. solo over pp div.).

**Pass:**
- The 429 tenuto's first 0.5 s is within ±2 dB of the 428 quarter on the stem, and its body is at or over the 424 G4.
- The master dip at 429 is 1.5 dB or less.
- Violas are 4 dB or more over Violins II at 425-431.

## 4. The harp étouffez at 244 and 654 still rings; the patch's own envelope can damp it with no second harp track (bars 62, 164)

**Measured** (`harp.py`, rerun on c10).
- At 244 (sub. p), the bar-61 E-major chord ends at 244.000 in the MIDI but keeps ringing. When E♭3 enters at 245.5, E3 is still 21.5 dB (relative units) against 24.9 for E♭3: a semitone clash 3.4 dB apart for about 0.8 s.
- E4 falls only 28.8 -> 14.4 over 1.2 s.
- At 654 (étouffez m.d.), A♭5 and F6 ring on (14.7, then 4.3 / 18.3) under the new G1/G2.
- The harp stem sits 7-14 dB under the master there, the only moving part over the cello pizz. at 244.

**Read from the patch file** (`Harp Sus RR.oib`, loaded with `opus_state.load_oib`): all three sample groups (HSH Harp Pluck Lng RR1, Thumb Pick RR2, Nail Pick) have an Envelope AHDSR with decay 5989.6 ms to sustain 0.001 and **release 3019 ms**. Every note rings 3 s after its note-off, which is why a note-off at the étouffez does nothing. The same decay takes the final ppp chord (724, l.v. to an étouffez at 727) from -52 dB to -66 within 2 s and to -85 by 4 s, 2-3 s before its printed end.

**Fix** (inferred; one patch reload of the Harp track, no new instance):
1. In the Harp state (`build_reaper.py`, wherever the Harp patch JSON is edited before `vst_chunk`), set `release` to 200 ms in the three groups' AHDSR.
2. In `score_to_parts.py`, for family "harp": extend each note to min(written end + `HARP_RING_S`, the next étouffez mark, the next same-pitch onset - 0.02 qn). Start with `HARP_RING_S` 2.5 s, which keeps about the present ring. Optionally raise `decay` to about 9000 ms so the final chord lasts to 727.
3. Then remove the 650 `LEVEL_SHAPES` damp. The note-offs do it now.

**Test** (written before the render):
- Five unaffected harp notes (e.g. 236, 238, 252, 256 and one arpeggio note) decay within ±2 dB of c10 over 1.5 s.
- At 244.0-244.3 and 654.0-654.3, the old pitches fall 15 dB or more within 0.25 s, while the new notes are unchanged.

If the decay check fails, keep the release edit and tune `HARP_RING_S`.

## 5. Smaller items (measured)

- **Basses' fp at 128 (bar 33).**
  - `DYN["fp"]` = 46 gives no f attack (CC11 goes straight from 114 to 46 at 128.0), and the p note then blooms from -40.7 to **-36.6 dB** at 129.0.
  - That puts it level with the bassoon solo entering at 128.5 (-39.9..-36.3).
  - Fix:
    - `score_to_parts.py`: an fp is a short f (CC 88 for 0.12 qn, falling to p by 0.25 qn).
    - `note_trims.json` Double basses `"128.0"` -4 (0.6 s ramp).
  - Pass: the basses are 3 dB or more under Bassoon 1 over 129-131.
- **Lento celli, bar 3 (qn 8.0).**
  - The celli carry the line 4 dB under the master.
  - The master dips **5.9 dB** at the 7.5 -> 8.0 join (the printed > < valley at CC 31, filled +6 by `early_fills` 8). It dips again by 5 dB at 8.75-8.875: a sample seam in the C3 at +0.93..+1.2 s after the moved start (stem -40 -> -47..-49).
  - Fix: `loop_fills.json` Violoncellos `"8.0"`: [[1.0, 5.0, 0.35]] (seconds after the moved start, as the c10 ones).
- **Legato holes of 6 dB or more on the stems** (`joins.py`): Vc 112 (8.2), Vln II 637 (7.8), Vln I 720 (7.5), Vc 365 (7.6), Vln I 279 (6.9), Vln II 236 (6.2). On the master these are 0.8-2.8 dB, because these stems sit 6.5-13 dB under it. Leave them for `auto_fills.py`; none is urgent.
- **Unslurred brass repeat at 456 (bar 115).**
  - The re-articulation after the slurred F3 (453 -> 456) has a 0.028 s gap, and the 456 F3 is not re-tongued.
  - Measured repeat dips: Trombone 1 +0.4 dB, Horn 4 -2.1 dB. Horn 4's repeats are a median -0.75 dB, with 0 of 4 re-tongued.
  - Fix: `WIND_REP_RETONGUE` should also apply when the previous note is a slur's last note.

## 6. Patch choice: the a2 doublings are still one solo sample; the blocker is the track count, not memory

**Measured.**
- 88 of Horn 2's 189 notes are unisons with Horn 1. `find_unisons` drops them and plays Horn 1 +3 dB on `1FH KS Master`. The windows are 272.5-288 (20 notes), 310.5-316 (7), 381.5-406 (20), 464-484 (7), 628-644 (13) and 664.5-679 (16).
- Kit section 8: identical-patch unisons are coherent, so this is one louder horn, not two.
- Trumpets 1-2 (664.5-679, 16 notes, "a2" ff) and Trombones 1-2 (520.5-536) are the same case.
- The recorded `2FH KS Master` (movement II c18: gain +4.6 dB over the solo-horn track, Close 0.5 / Main 1.0) is on disk, as are `2 Trumpets/06 Keyswitch` and `2 Trombones EXP/04 Keyswitch`.
- Memory is not the limit: c10 settled at 43 GB, and one two-row instance adds about 1 GB (kit c24: rows, not instances, set the footprint). What blocks it is the actor prompt's "32 tracks" check.

**Fix** (inferred): free a track instead of adding one.
- Tam-tam (key 36, strokes at 484 and one pp) and the crash (key 60, one stroke at 636) never sound together and do not share keys. They can be two instrument zones in one Opus instance: `zones` with keyMin/keyMax 36/36 and 60/60, each instrument keeping its own mixer, mics and seat.
- Give the merged track the crash's and tam-tam's `LEVEL_SHAPES` / roles, which never overlap in time, and the tam-tam `_damp`.
- Put the 2FH a2 track on the freed slot (`TRACK_WINDOWS` as a list of windows: the c10-A item 3 recipe).
- Do this in a cycle with no other build change, and measure Horn 1/a2 level per window (±1 dB of c10) and REAPER memory.

The bass trombone's three development notes below E2 (452/456/460) are tenor samples pitched down. They are too few to change patch for.

Do not touch: `accent_fits.json` and GENTLE_ACCENT for all three families (with `--keep-long-qn 1.4`, `--pickup-qn`); `AUTO_REBOW`, `space_rebows` rows and the fitted re-bow shapes (the master cannot tell re-bows from control times); `NOTCH_SKIP` and the c10 `loop_fills`; the c09 Violins I theme-head strokes and `DOWNBOW_STROKE_AT` with its `LEVEL_SHAPES`; `TREM_JOIN` / `TREM_SPLIT` / `TREM_ENTRY_LEAD_S`; `REP_SPLIT`, `STR_SHORT_AFTER_SUS`, `ROW_TRIM_DB`; `PORTATO_JOIN_AT` and the 191/591 arrival trims; `WIND_REP_RETONGUE`, breath gaps, `BREATH_SPLIT_AT`; pizzicato rows, staccato rows, timpani strokes and re-strike plans, `TIMP_DELAY_S` and the cymbal timing; `CC1_DYN_MAP` with the c09 trims; the 650 harp damp until item 4 replaces it; the climax order (160 > 122 > 169).
