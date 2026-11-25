# Cycle 18, critic A: articulation and phrasing (on the cycle 17 render)

Scripts and data are in `/private/tmp/claude-501/mockup-loop/c18-A/`. They are the c17-A set plus:
- `refit17.py`: the loop profiles refit on the c17 stems, with a split-half test. Its outputs are `loop_profiles_c17.json` (all ten notes) and `loop_profiles_c18_proposed.json` (the file to copy).
- `negtrim.py` and `negsim.py`: legato targets that carry negative trims.
- `pzon.py`: pizzicato and harp onset alignment.
- `ob.py` and `hole.py`: per-note envelope dumps.

Run them with `CYC=17 ~/.venvs/claude-composes-reaper/bin/python`. `build/parts.json` (21:47) is the data behind the c17 render (22:26).

## Checked and working (measured, c17)

- **Chords and slurs.** No chord goes to a legato patch (`chords_leg.py`). Every slurred pitch change plays on a Leg articulation, except the intended ones: the viola sextuplets in bars 59-60 and the CA portato at 157.
- **Ties.** All 104 ties are held. The only re-attacks are the timpani tie strokes at 203 and 211.
- **Keyswitches.** Every keyswitch is at least 20 ms before its note, except the known Ob1 207.952 (13 ms).
- **Legato joins** (`wjoin2.py`):
  - The median dip is 1.5-3.7 dB on every legato track.
  - Only two joins dip 8 dB or more: Vln I 67.5 (10.2) and Vc 240 (8.2). The Vc 124 arco entry also shows up, but it is not a join.
  - Vln I 67.5 and Vln II 80 are covered by the other violin section in unison: the Vln I + Vln II sum has no hole.
- **Printed breaths** dip 13-34 dB (`breath.py`).
- **Phrase-final releases** reach -15 dB in 0.15-0.68 s by family (`ends.py`).
- **Pizzicato** peaks spread 2.2-2.6 dB note to note (`pizz.py`).
- **Harp.** The harp's note-offs in bars 37-44 do not cut the ring: the decay slope after the note-off is no steeper than before it.
- **Pickups.** Every pickup that is louder than its downbeat sits under a printed decrescendo or dynamic drop (`upbeat.py`), for example bars 30 and 81-82.

## 1. Revert the `WIND_VIB_CAP` test: Flute 1's Ab6 at the climax now wobbles more and is louder. Measured.

**Where:** Flute 1, qn 204-212 (bars 61-62, ff Largamente).

**Evidence:** amplitude modulation in the 1.5-4 kHz band over 204.5-211.5 (`bandam.py`):

| | c16 | c17 |
|---|---|---|
| Flute 1, residual p95-p5 | 10.1 dB (4.3 Hz, autocorrelation 0.73) | 15.5 dB (2.9 Hz, autocorrelation 0.31) |
| Flute 1 stem RMS | -31.9 dB | -30.1 dB |
| Master, same band | 5.0 dB | 5.9 dB |

- In c17 the modulation is larger and irregular. This matches the actor's reading that the Non Vib and Vib layers beat against each other at CC1 67.
- No other part changed:
  - Flute 2: 12.2 -> 11.5 dB.
  - Oboe 1: 7.1 -> 7.2 dB.
  - Oboe 2: 7.2 -> 7.7 dB.
  - Flute 1 at 262-266 is not capped: 12.0 -> 13.0 dB.

**Fix:** in `tools/score_to_parts.py`, set `WIND_VIB_CAP = None`. Also guard `cc1_fn`: put `WIND_VIB_CAP is not None and` at the front of the `if family == "wind" ...` condition, because `min(v, None)` raises. Then run `--midi-only`.

**Check:** Flute 1 at 204.5-211.5 measures 10-11 dB and -32 ± 0.5 dB.

## 2. Divisi passages still play two full sections where the score asks for two halves. A better patch exists for each. The cost is measured; the benefit is inferred.

**Where:**
- **Violas, qn 66-90 (bars 23-30, "div.").** There are 13 dyads at p-mf, such as (60,63), (58,68), (61,65), (63,67) and (63,68).
- **Violas at 277 and 283 (bars 84 and 86, "(div.) change bow at will").**
- **Violins II, qn 108-124 (bars 37-40, "senza sord., div., sul tasto").** Two staggered Flautando voices: the upper voice is 65-66-65-66-65 and the lower voice is 61-58-61-63-61.

**What is wrong (measured from `parts.json`):**
- Each voice is a full-section sample: Violas KS Master Sus MAX, and Violins II KS Master Flautando.
- `chord_segs` lowers each voice by 3 dB (-10 log10 2).
- So the inner harmony under the bar 23 tune, and the sul tasto pad of bars 37-40, sound like 2 x 12 players played softer instead of 2 x 6.
- The c13 cello answers had the same problem, and the "Violoncellos div" track fixed it (`TRACK_SPLITS`).
- The viola item has been deferred twice. The Violin II part is new.

**Patches** (on the drive):
- `Violas Divisi/06 Keyswitch/Violas KS Master DIV B.oib`.
- `2nd Violins Divisi/01 Long/2nd Violins Flautando DIV B.oib`. This is a single-articulation patch, so it needs no keyswitch.

**Fix:**
- **"Violins II div" track** (Flautando DIV B):
  - Route with `TRACK_SPLITS` `("Violins II", [(108.0, 124.0)], 64)`. A pitch threshold works here: the upper voice is always 65 or more and the lower voice 63 or less, so the lower voice stays on the main track.
  - Keep `FLAUT_JOIN_TRACKS` holds and leads (`FLAUT_LEAD_S` 0.45, `FLAUT_OVERLAP_QN` 0.7) on both tracks.
- **"Violas div" track** (Violas KS Master DIV B, only the Sus MAX row loaded):
  - Pitch cannot split these chords, because the voices cross at 61 and 63. Add a rank mode to `TRACK_SPLITS`, `("Violas", [(66.0, 90.0), (277.0, 289.0)], "upper")`, which moves the upper note of every two-note onset group. Single notes stay on the main track.
- **On both div tracks:**
  - Set no `chord_segs` cut.
  - Keep the -3 dB cut on the main track inside the windows. The main track is still a full section playing one voice, so this makes it about the level of a half section.
  - Centre the main channel and give each div track the same seat as its section, as `apply_mix` does for the Vc div track.
  - Start each div track's gain at +3 dB and set it from the measured level after the render, as was done for the Vc div track.

**Check:**
- Main + div RMS within ±1 dB of the c17 stem over each window.
- No new re-articulation trough of 6 dB or more (`rebow.py`) at 69-72 or 112-122.
- Memory: if REAPER's memory is over 56 GB after loading, drop the 277-289 window first.

## 3. Loop-seam pulse: refit four profiles on the new hall. Measured in-sample; the out-of-sample effect is inferred.

**Where:** Violins I at 0 and 292, Violoncellos at 164, Double basses at 220.

**Evidence** (`loops.py` and `refit17.py`; residual p95-p5 in dB / autocorrelation):

| Note | c17 as rendered | c17 with no profile | Refit on c17 |
|---|---|---|---|
| Vln I 0 | 8.3 / 0.38 | 10.3 / 0.46 | 5.0 / 0.25 |
| Vln I 292 | 7.6 / 0.56 | 10.2 / 0.64 | 5.6 / 0.39 |
| Vc 164 | 7.8 / 0.26 | 13.1 / 0.36 | 5.7 / 0.30 |
| Cb 220 | 3.7 / 0.62 | 6.6 / 0.73 | 1.9 / 0.19 |

- The c16-fitted profiles still help on the new hall: every note is 2-7 dB better than with no profile.
- On the other six notes (Vc 274/292, Cb 271/292, Vla 292, Vln II 286) the refit gains less than 1 dB, so keep their current profiles.
- The period is unchanged (3.96-3.97 s).

**Caveats:**
- The refit is in-sample.
- A split-half test can only be run on the long notes, and there the half fits are mixed (Cb 220 2.0, Vln I 292 6.8). Vln I 0 and Vc 164 are too short (2 cycles) to validate.
- The c15 -> c16 test showed that these profiles carry over to the next render as long as the patch, mics and hall do not change.
- The Vc 164 refit reaches +8.9 dB at its deepest seam trough. That is above the c16 maximum of +6.6, so cap it at +7 if you are cautious.

**Fix:** copy `/private/tmp/claude-501/mockup-loop/c18-A/loop_profiles_c18_proposed.json` to `build/loop_profiles.json`. Only those four entries are new. Then run `--midi-only`; no code change is needed.

**Check:** p95-p5 at most 6 dB on these four notes, and the bar RMS of bars 1-4, 51-53, 65-70 and 89-92 within ±0.7 dB of c17.

## 4. The Horns 1-2 a2 at bars 79-82 is played by one solo horn. Measured; the gain in tone is inferred.

**Where:** Horns 1-2, qn 261-272. The score prints one line for "Hn. 1-2" from the bar 78 pickup to bar 82. There are 9 unison notes: 60, 61, 60, 58, 56, 58, 58, 61, 60.

**Evidence:**
- `find_unisons` drops Horn 2's copies (`unison_dropped` 8). The ninth note was treated separately by `UNI_DELAY`.
- The Horn 2 stem is silent from 262 to 271: -158 dB, then -180 dB.
- Horn 1 (Solo French Horn KS Master) carries the a2 at -30.5/-31.2 dB over 262-268, with a role of +4 dB.
- So the second climax's horn line is one player pushed up 4 dB rather than two players. A solo horn raised in level keeps a single player's tone.
- HO has `2 French Horns/06 Keyswitch/2FH KS Master.oib`. Its map is already in `ks_maps.json`: Sus MAX 24, Leg Slur MAX 26, Portato 30.

**Fix:**
- Add a track "Horns 1-2 a2" on 2FH KS Master, staves `["Hn1"]`, with only the Leg Slur MAX and Sus MAX rows loaded.
- In `TRACK_WINDOWS` add:
  - `"Horns 1-2 a2": (261.0, 272.0, True)`
  - `"Horn 1": (261.0, 272.0, False)`
  - `"Horn 2": (261.0, 272.0, False)`

  The window starts on the phrase's first note (261 v53, not a legato target), so no slur is cut.
- Move the Horn 1 role `[262, 268, 4, 0.5]` to the new track at 0. Set its gain after the render so that it measures within 1 dB of Horn 1's c17 level over 262-268.
- Seat it at Horn 1's seat.
- Give it Horn 1's legato leads (`LEG_LEAD_S` brass and `leg_leads.json` entries in the window, if any) and the v124 legato velocity.

**Check:**
- The a2 track's joins have a median dip under 3 dB (`wjoin2.py`).
- The horns at 262-268 stay within ±1 dB of c17.
- The breath at 264.7 still dips 10 dB or more.

## 5. Eight wind fills still add a 2.5-5 dB swell at slurred joins. That reads as an unprinted accent. Measured.

**Where and evidence** (`fljoin.py`, 200 ms window, peak over the louder body):

| Join | Over | Fill | New value |
|---|---|---|---|
| Fl1 252 | +4.9 | 6.0 | 2.1 |
| Cl1 256 | +4.9 | 3.6 | remove |
| Ob1 143 | +3.1 | 5.3 | 3.2 |
| CA 132 | +3.1 | 5.2 | 3.1 |
| CA 134 | +3.3 | 4.0 | 1.7 |
| Cl1 258.5 | +2.9 | 2.4 | 0.5 |
| Cl1 178 | +2.8 | 2.4 | 0.6 |
| CA 97 | +2.5 | 2.6 | 1.1 |

**Cl1 256 in detail (`ob.py`):**
- The new G5 sample (pitch 79) is about 13 dB louder than the Ab5 before it.
- The pitch trim (-6) and note trim (-5) bring the envelope from +6.5 to -9 dB. The note trim ramps in over 0.6 s from the score onset, so the note peaks at -34.4 dB at +0.14 s against a body of -43.
- The c17 auto fill (+3.6, "dip 6.6 dB at +0.00 s") adds to that peak. The 30 ms "dip" it measured is the gap before the transition.

**Fix:**
- In `build/early_fills.json`, apply new = fill - (over - 1), as in the table. Delete Cl1 256 and keep `pre_s` and `hold_s`.
- `auto_fills.py`'s overshoot rule should produce the same values when it is rerun on c17. If it does not, set them by hand and list them under `_auto` as "c18 lowered".
- Leave Ob1 140/189 alone:
  - Their 10-11 dB "dips" are the soft pickup (139/188, p) against a louder target.
  - At 140, the target's body arrives at +0.16-0.36 s under a printed crescendo.

**Check:** no listed join over +2.5 dB at 200 ms, and no 200 ms dip deeper than in c17.

**Do not touch:**
- **Ties, slurs, keyswitches.** Tie handling and the timpani tie strokes. Keyswitch placement. Slur-scoped overlap. The Leg Slur/Leg BC split, v124 legato velocity with its leads, `LEG_ART_EXTRA_S`, `LEG_SOFT_EXTRA_S`, `leg_leads.json`.
- **Joins and notches.** `BC_SOFT`/`BC_SOFT_SKIP` and the halved notches. `SOST_HOLD_THROUGH`. `slur_out`. The Flautando lead and overlap.
- **Marcato and accents.** `MARCATO_SPANS`, `ACCENT_DB_AT` and the Tbn1 accents.
- **Pizzicato, harp, tremolo.** Pizzicato step trims. The harp rolls, the harp note-off lengths and the harmonics track. Tremolo in bars 61-64.
- **Mutes, breaths, phrase ends.** CC15 placement. Breath gaps and phrase-end releases.
- **Loop profiles.** The six loop profiles not refit above. The `UNI_DELAY` rule (it stays for the other unisons).
