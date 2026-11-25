# Cycle 34, critic A: articulation and phrasing (on the c33 render)

Sources: `cycles/c33/render` (master and stems), `cycles/c32/render` for comparison, `cycles/c33/rendered_build/parts.json`, `build/score_config.py`, `build/mix.json`, `build/auto_fills.json`, `build/mockup-events.tsv`, `v600/sections/coda.ily`, score page 8 (bars 87-92), `tools/fit_rebows.py`, `tools/auto_fills.py`, `tools/score_to_parts.py`, the `.oib` JSON of the Violas KS Master and Celli KS Master DIV A (read directly from the patch files), the installed `Basses Divisi` folder, the May 2021 HO manual PDF pp.160-162 and 188-190 (row A7 of `loop/MANUAL-READING.md`, cycle 34), `loop/MANUAL-GAPS.md`, `mockup-kit/LEARNINGS.md` (the listener section and sections 5-8), the c28-c33 critic A reports, and `cycles/c33/CHANGES.md`.

Times are score qn unless marked s. Levels are the RMS of the power sum (L² + R²)/2 over the window stated. The dip at a join or re-bow is the lower of the bodies before and after, minus the minimum around the onset.

## Manual notes (A7, PDF pp.160-162 and 188-190: the Articulations window, trigger options, Zones)

| Manual (PDF page) | Where it applies | Does the render follow it? |
|---|---|---|
| Each articulation cell has a load switch; an unloaded row costs no RAM (p.160) | `UNLOAD_UNUSED_ROWS` on all 32 tracks | Yes. `art_counts` in parts.json lists only the rows each track plays (for example, Violas: 6 rows; Flute 1: 2). |
| KS Masters load with the Keyswitch trigger. Keyswitch notes lie outside the playable range and select the row for the following notes (p.161, p.189) | 401 keyswitch events in parts.json | Yes (measured in parts.json). No keyswitch falls after or on the note it selects. The shortest keyswitch-to-note distance is 0.02 qn on the string tracks and 0.04-0.06 qn on the winds and brass. `ks_clash` is empty on every track. |
| Keyswitch Range, Program Change and Controller triggers (pp.161-162, 189-190) | none | Not used, and not needed. The pipeline's controllers (CC1, CC7, CC11, CC15, CC36) are not articulation triggers in these patches. That is inferred: the build never changes a trigger option, and no row has switched unexpectedly. |
| Velocity trigger: layer a short articulation over a sustain at v110-127 to get an accent (p.162, p.190) | Trombone 1's two accents (213, 218) | Correctly not used. A staccato layer at high velocity adds attack bite, and bite is what Dan rejected (BRIEF item 9). The accents now carry +4.5 dB (213) and +1.1 dB (218) of weight over their neighbours, with a 2-5 kHz front of +0.9 and -8.2 dB against the body (measured). |
| Group: within a group, only the triggered instrument plays (p.188) | rows inside each KS Master | Followed. I found no chord, and no overlap over 0.2 qn, on any Leg row (Leg Slur MAX, Leg BC MAX, Leg Port MAX, Leg Slur) across the 32 tracks (measured in parts.json). The monophonic legato rows never receive two notes at once. |
| Voice limit: raise it if voices drop (p.188) | divisi chords, tremolo dyads, re-bow pieces, harp let-ring | No risk. Both patches read have `voiceLimit` 350 (Violas KS Master and Celli KS Master DIV A), against at most 3 notes plus tails at a time per track. |
| Octave and Key Range for splits on one channel (pp.188-189) | none | Not needed. Each divisi part has its own track (`TRACK_SPLITS`). |

## Findings, ranked by what a listener would hear

### 1. Celli "4 soli" coda pedal (bars 83-86, qn 274-286), new in c33: a 2.3 s sawtooth pulse. Every re-bow piece drops 5-11 dB and needs about 1.5 s to recover, and the entry takes 1.9 s to reach its body

- **Where.** Violoncellos div (stem 29), A flat 2, ppp. The pedal plays six pieces: 273.91 (entry), then re-bows at 275.53, 277.60, 279.67, 281.72 and 284.14, each about 2 qn (2.3 s) long.
- **What is wrong (measured).**
  - In c33 the pedal moved to the DIV A half section, and its five full-section re-bow fills were dropped, as fitted to other samples. `fit_rebows.py` was not re-run (CHANGES.md "Not done").
  - Each new piece is a fresh soft Sus MAX attack with a 0.03 qn gap before it. Over 0.5 s it falls 6-9 dB below the end of the previous piece, then climbs back over about 1.5 s. The 0.1 s envelope after each re-bow:
    - 275.53: -50 → -60 → -54 → -50
    - 277.60: -49 → -61 → -53 → -50
    - 281.72: -51 → -62 → -55 → -53
  - Re-bow dips on the stem: 5.6, 11.2, 5.4, 7.8 and 1.6 dB. Level steps after them: -2.5, -4.8, -1.9, -4.9 and +4.5 dB.
  - The master dips 4.9 dB at 277.60.
  - Over 274.5-285.5 the stem swings 8.1 dB (p10-p90 of 200 ms windows). The c32 full section played the same pedal with a 3.9 dB swing.
  - The entry at 273.91 reaches body - 6 dB only after about 1.0 s, and its body after about 1.9 s.
  - A ppp pedal that pulses every 2.3 s sounds like bowing, not a held pedal. This is the effect Dan heard on the series 1 final chord (BRIEF item 8).
- **Fix.**
  1. Run `~/.venvs/claude-composes-reaper/bin/python tools/fit_rebows.py 33 cycles/c33/rendered_build/parts.json --tracks "Violoncellos div" --write`. This fits the five re-bows (their pieces are over `MIN_PIECE_S`). Check that the fill reaches its +6..+9 dB clamp in the first 0.5 s.
  2. Lengthen the pieces so there are fewer seams. Add a generic per-track override in `tools/score_to_parts.py`, `REBOW_SEG_S_BY = {}`, defaulting to `REBOW_SEG_S`. In `build/score_config.py` set `REBOW_SEG_S_BY = {"Violoncellos div": 4.2}`: three re-bows instead of five, each piece still under `REBOW_MAX_S` 4.5. Then re-run `space_rebows.py` for this track only (do not use `--write` wholesale, which resets the hand-set moves; HISTORY c33), and fit as in step 1.
  3. Entry: `build/entry_leads.json` "Violoncellos div" 274.0 +0.15 s, plus an `early_fills.json` entry `{"db": 4, "pre_s": 0, "hold_s": 0.6}`. This is the soft-chord lead-plus-fill recipe (kit §6: lead 0.06-0.15 s plus a 3-4 dB fill held 0.3-0.4 s). Hold longer here because this attack is slower.
- **Pass.** Stem p10-p90 over 274.5-285.5 at most 4 dB. Every re-bow dip at most 3 dB. Master dip at 277.6 at most 2 dB. Entry body within 1 s.
- **Fallback.** If the fitted half section still swings over 5 dB, return the pedal to the full section (c32 swung 3.9 dB at -6 dB). That means removing the (274, 286, 0) window from `TRACK_SPLITS["Violoncellos div"]` and restoring the c32 fills from `cycles/c33/before`.

### 2. Double basses: every second re-bow piece of the long pedals swells +4 dB and then collapses -6 dB between 1.2 and 2.4 s after its start. On the master the bass band (60-170 Hz) swings 14 dB in bars 67-70

- **Where.** Double basses (stem 26).
  - E flat pedal, bars 65-70 ("4 soli", 220-238): pieces from 221.80, 225.22, 227.78, 230.39, 233.04 and 235.66.
  - Coda A flat pedal: pieces from 273.23, 276.05, 278.35, 282.20 and 283.61.
- **Measured.** Swing within each piece (p10-p90, 100 ms frames; the steady pieces swing 2.7-3.5 dB):

  | piece | 225.22 | 230.39 | 235.66 | 273.23 | 278.35 |
  |---|---|---|---|---|---|
  | swing, dB | 9.5 | 8.8 | 9.0 | 11.0 | 9.7 |

  - In those five pieces the shape is the same: flat for 1.2 s, then +4 dB at about +1.2..+1.5 s, then -5..-6 dB from +1.8 s to the end. For 225.22 the 0.3 s frames read -52 -53 -53 -54 -49 -51 -57 -60 -59. The pieces between them stay flat.
  - Master 60-170 Hz relative to each piece start: 225.22 reads +0 +4 +3 +1 +3 +8 +6 +1 -1, and 230.39 reads +0 -3 +7 +0 +1 +8 +8 -5 -2. The steady pieces stay within ±4 dB.
  - In bars 67-70 the basses carry the whole low register under Horn 1 and the ppp timpani roll, so this sounds like a slow "wah" in the bass every 5 s.
  - Series 1 c32 critic A #2 reported this, and c33 deferred it again (it would need a basses-only CC16 test).
- **Why the fitted fills miss it (read).** `tools/fit_rebows.py` fits each piece only over `W = min(WINDOW_S, piece - 0.3)`, with `WINDOW_S = 1.5` (line 42). From there to the next re-bow it holds a single mean level. The swell and collapse sit at +1.2..+2.4 s, mostly outside the fitted window. The hold averages them away, so it corrects nothing.
- **Fix (deterministic, no test render).**
  - Add a per-track window to fit_rebows: `--window "Double basses:2.6"` (or a `WINDOW_S_BY` dict). The fill then follows the measured shape to 0.3 s before the next re-bow on these pieces (about 2.3-2.8 s long).
  - Run `fit_rebows.py 33 cycles/c33/rendered_build/parts.json --tracks "Double basses" --window "Double basses:2.6" --skip "Double basses:273.229" --write`. The skip keeps c29's "no fill on 273.229".
  - Clamp as now (-6..+9 dB).
  - If 273.229 must then stay unfilled, take its swing out with a `LEVEL_SHAPES["Double basses"]` entry: -4 dB over +1.2..+1.6 s and +4 dB over +1.9..+2.6 s after the moved start.
- **Pass.** Every listed piece swings at most 4 dB. Master 60-170 Hz within ±4 dB over each piece. The steady pieces unchanged within 1 dB.
- **Evidence.** Measured; the cause is read in the tool. Which bow direction the alternation follows is inferred (it alternates piece by piece and repeats in both pedals).

### 3. Violins II, bars 65-66 (qn 220-223): the held pp C sharp 4 swells 7 dB by itself before the printed niente, then the 223 re-bow drops it back

- **Where.** Violins II (stem 23). The pp chord of bars 65-66: Violins II, violas and celli tied from bar 64, with the basses' pedal under them; Horn 1 enters at 226.
- **Measured.**
  - CC11 is a constant 34 from 220 to 223. The volume envelope ramps only +1.5 dB (220.15 -3.5 to 222.9 -2.0).
  - Yet the stem rises from -47 dB (220-221.5) to -40..-39 dB (222.2-222.9), then falls to -45 dB at the printed down-bow re-bow at 223. The re-bow step measures -2.6 dB, master dip 1.8 dB.
  - Over 222-223 Violins II sits 6-10 dB over the violas (-49) and celli (-50..-53). All three are marked pp, and Violins II is not a melody voice here.
  - The master rises -42 → -39 dB inside a held pp chord with nothing else moving.
  - This is a Leg Slur MAX sample bloom (kit §6: some MAX sustains swell 8-17 dB at a constant CC11).
  - The 223 re-bow fill (`rebow_fills.json` Violins II 223.0, vol +5.7 dB at 223.25) was fitted to match the bloomed level, so it also holds the new piece up.
- **Fix.**
  - `build/score_config.py`: `LEVEL_SHAPES["Violins II"] += [[(221.0, 0.0), (222.1, -5.0), (222.95, -5.5), (223.0, -5.5)]]`. Then subtract 5 dB from every point of the Violins II 223.0 entry in `build/rebow_fills.json`, or refit it with `fit_rebows.py --tracks "Violins II"` after the shape is in.
  - The shape falls slowly (1.1 s) at a constant printed dynamic, so it cuts no hall tail (S3 concerns sudden drops). If the actor prefers it pre-hall, use the same values as `CC7_POINTS["Violins II"]` (127 → 72) and keep the bar 66 niente CC7 lane starting from 72 instead of 127.
- **Pass.** Violins II over 221.5-222.9 within 2 dB of 220-221.5. Master flat within 1.5 dB across 220-223. The 223 re-bow step within ±2 dB.
- **Evidence.** Measured.

### 4. Trombone 1's quotation, bars 63-64 (qn 212.5-219.5): uneven inside the slurs. The slur heads at 214.5 and 217 sink 4-5 dB, and the unaccented 215 is as heavy as the accented 213

- **Where.** Trombone 1 (stem 16), ff "marcato". Slurs 212.5-213, 214.5-216, 217-217.5. Accents on 213 and 218. Tenuto on 216, a slurred repeat of 215.5.
- **Measured.** Stem body (+0.05..+0.5 s):

  | qn | 212.5 | **213 >** | 214.5 | 215 | 215.5 | 216 – | 217 | 217.5 | **218 >** |
  |---|---|---|---|---|---|---|---|---|---|
  | body, dB | -25.9 | -21.4 | -26.5 | -22.3 | -24.3 | -24.8 | -27.9 | -23.7 | -22.6 |
  | 2-5 kHz front - body, dB | -0.9 | +0.9 | +1.0 | +1.7 | +2.5 | -2.9 | -2.6 | -0.3 | -8.2 |
  | master 2-5 kHz jump, dB | -4.2 | -0.2 | +0.1 | **+4.8** | -3.2 | -0.7 | -4.6 | +0.8 | -1.0 |

  - Both accents carry weight with no bite: 213 is 4.5 dB over its neighbours, 218 is 1.1 dB over 217.5. Dan's item 9 holds.
  - The line between them is uneven. The new-slur heads 214.5 and 217 sit 4-5 dB under the notes after them.
  - The unaccented 215 is only 0.9 dB under the 213 accent. On the master it has the biggest bright front of the passage (+4.8 dB 2-5 kHz jump), so it sounds like an unprinted accent.
  - Cause (read): c29's +4.5 dB shape on 215 (`LEVEL_SHAPES_S`, made when 215 sagged 6 dB) is still in place. Since then c32 retimed the 212.5 entry and c33 added CC7 95 over 215's head. The c28 slur-head swells on 214.5 and 217 are only +2 dB, held to +0.15 s.
  - The tenuto repeat 215.5 → 216 dips only 1.5 dB on the stem and the master (S1).
- **Fix (`build/score_config.py`).**
  - In the c29 `LEVEL_SHAPES_S["Trombone 1"]` entry, change 215.0 from +4.5 to +1.5 dB (same timing).
  - Change the c28 214.5 and 217.0 shapes to `[(-0.01, 0.0), (0.04, 4.0), (0.40, 4.0), (0.50, 0.0)]`.
  - For S1 at 216, set `REP_RETONGUE_AT["Trombone 1"] = [216.0]` with a deeper fall: `WIND_REP_RETONGUE_BY = {"Trombone 1": {"gap_s": 0.08, "fall_cc": 10}}`, or a per-onset `BREATH_GAP_AT`-style 0.08 qn gap. Keep the +3.5 dB body on 216.
- **Pass.**
  - 214.5, 215, 215.5, 216 and 217.5 within 1.5 dB of each other (about -24.5 dB); 217 within 2 dB.
  - The accents 213 and 218 2-4 dB over that.
  - Master 2-5 kHz jump at 215 under +2 dB.
  - Dip at 216 3-6 dB on the stem.
- **Evidence.** Measured; the shapes are read in the config.

### 5. String legato joins: the violas have 14 joins dipping 6-8.7 dB, and the two violin sections sag together at 67.5/68. Auto fills have not been re-run since c31

- **Where (measured, legato targets on Leg rows, 50 ms window; stem dip / master dip in dB).**

  | onset | 46.5 | 109 | 111 | 120 | 121.67 | 189 | 192 | 193.67 | 240 | 241.5 | 243.5 | 249 | 253.5 | 256 |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
  | stem | 6.4 | 6.6 | 6.2 | 6.2 | 6.4 | 7.5 | 6.4 | 7.2 | 7.1 | 7.2 | 7.5 | 6.1 | 8.7 | 8.4 |
  | master | 3.5 | 2.1 | 3.9 | 1.4 | 1.3 | 2.3 | 2.3 | 0.8 | 3.0 | 1.1 | 1.2 | 4.3 | 3.0 | 1.3 |

  - The violas carry the inner line of bars 37-40, 63-64 and 71-77, so holes of 3-4 dB on the master (46.5, 111, 249, 253.5) break the line.
  - Violins I 67.5 (9.2 / 2.7) and Violins II 68.0 (8.1 / 2.9) are the unison theme of bar 23. Two sections in unison sag together and do not fill each other (kit §6).
  - Other stems (stem / master): Violins I 251.5 (7.9 / 1.4); Violoncellos 142.5, 199 and 202 (7-8.3 / 0.8-2.2); Horn 4 289 (6.5 / 3.3).
  - Every other track has at most one join of 6 dB or more.
- **Fix.**
  - Run `~/.venvs/claude-composes-reaper/bin/python tools/auto_fills.py 33 cycles/c33/rendered_build/parts.json --write`. The violas and violins are already in `build/auto_fills.json`. Keep the overshoot rule and check each new fill against the 30 ms peak (kit §6, c21).
  - Add `--exclude "Violoncellos div:63.0"`: that is the bar 21-22 div entry, master dip 0.5 dB.
  - For the unison 67.5/68, fill both sections (kit §6 c23: 2.5-5 dB each, held to the sag minimum).
  - Horn 4 289 (con sord., pp) is not on an auto-fill line. Give it an `early_fills.json` entry of 3 dB held to its sag minimum.
- **Pass.** Violas joins of 6 dB or more down from 14 to at most 5. Master dips at 46.5, 111, 249, 253.5, 67.5/68 at most 2.5 dB. No fill over the louder body by more than 2 dB.
- **Evidence.** Measured.

### 6. Repeated notes that are not heard as two notes (S1): the cor anglais at 271, Horn 3 at 289 and 265, Violins II at 45 and 50

- **Where and how much (measured; stem / master dip, 30 ms, dB).**
  - Cor anglais 271 (E flat 4, slurred repeat of 269, no tie, printed p): 0.4 / 1.2. `WIND_SLUR_REP_MERGE` merged it into one note with an 8 CC notch, and the envelope shows no gap (-43..-46 dB straight through). The p at 271 is printed as a new dynamic on a new note, and a player re-tongues there softly.
  - Horn 3 289 (A flat 3, con sord., pp, "slur + tenuto = soft re-articulation" by the composer's own note, `coda.ily` c326): 1.8 / 3.8. It is re-tongued (`rep_retongued`), but the 0.06 s gap is filled by the muted horn's tail and the hall (kit §7: 1-2 dB on soft horns at 0.06 qn). The master reads 3.8 only because Clarinet 1 re-tongues at the same moment (4.6 dB stem).
  - Horn 3 265 (F4 repeat of 262, unslurred, start of a crescendo in bar 80): -0.5 / 2.3. There is no dip at all on the stem.
  - Violins II 45 and 50 (the portato pairs of bars 15-17): master 2.5 and 2.2. 44 (5.0) and 51 (3.8) pass.
- **Fix.**
  - Cor anglais: re-tongue 271 instead of merging it. Either `REP_RETONGUE_AT["Cor anglais"] = [271.0]`, if that list overrides the slur merge (check in `score_to_parts.py`; if it does not, add a generic `WIND_SLUR_REP_MERGE_SKIP = {}` per-onset list), or a deeper notch with `MERGE_NOTCH_AT["Cor anglais"] = {271.0: 18}`. Aim for a 3-5 dB dip.
  - Horn 3: `WIND_REP_RETONGUE_BY = {"Horn 3": {"gap_s": 0.12, "fall_cc": 10, "fall_s": 0.15}}`, applied to 289 and 265 (kit §7 c23: muted and soft horns need longer gaps). Then re-measure Horn 4 289 (finding 5) together with it.
  - Violins II 45/50: `MERGE_NOTCH_AT["Violins II"][50.0]` 14 → 18; for 45 (a re-bow), shorten the previous piece's end by 0.03 qn more.
- **Pass.** Each listed repeat dips 3-6 dB on the master.
- **Evidence.** Measured.

## Smaller observations (measured unless marked)

- **c33 changes in my lens, verified.**
  - Solo violin legato at v72-80: join dips 1.1-4.1 dB (c32 at v124: 1.1-3.7). Pitch crossovers have a median +0.021 s (c32 +0.016), all 9 within -0.016..+0.096 s. No regression; the slower transition is in place.
  - Trombone 1's 213/215 heads: no bite (finding 4 table).
  - Harp let-ring (env_sustain): see CHANGES.md; not re-measured.
- **Keyswitches and rows (parts.json).** All 401 keyswitches come before their notes. There are no chords on mono legato rows, no same-pitch overlaps on Leg rows and no `ks_clash`. Keep.
- **Tremolos, bars 61-64.** At 204, 212 and 216 every string section reaches body - 6 dB before the beat. The energy centroid of the first 150 ms sits at +0.015..+0.078 s (S2 fine). No tremolo is re-bowed (`AUTO_REBOW_SKIP_TREM`).
- **Pizzicato, bars 37-44.** Basses are even: peaks -38.7..-46.3 dB at v53, with peak times +0.02..+0.15 s. On the violas, E flat 3 sits a median 4.0 dB under its neighbours (4 notes) and D flat 3 2.4 dB under (2 notes). Optional fix: `VEL_SET["Violas"]` +3 on the E flat 3 notes at 134.33, 135.0, 136.0 and 137.33.
- **Breath gaps eaten by entry leads.** Bass trombone 204: gap 0.043 qn (0.08 s on the tempo map, with the caesura). Trombone 2 204: 0.069 qn. Bassoon 2 268: 0.046 qn. Every other wind at those breaths has 0.10-0.12 qn (0.23 s). The breath end is taken from the score onset, not the moved one. The master hardly shows it in these tuttis (0.7-1.8 dB). For a generic fix, end the note before a breath at `moved_next_onset - CAESURA_BREATH_QN`.
- **Mutes (CC15) and mute EQ.** They match v600. Violins II from 273.5, violas 273.5 (div. 268.5, in the rest after bar 81), Violins I 274.5; celli and basses open in the coda; Horns 3-4 mute EQ from 278 (both are con sord. at 286 in the parts).
- **Re-bows elsewhere.**
  - Loop pulse: no held note over 7 s shows a 3.95 s pulse except the celli 219.5-226 (autocorrelation 0.72), which is the niente decay plus the bar 66 re-bow, not a loop. Final chord autocorrelations are -0.13..+0.17.
  - The opening Violins I C5 still dips 5.6 dB at 7.35 (master 1.0).
  - Final chord: Violins II 303.4 steps -5.5 dB, inside the morendo.
- **Bars 61-62 molto sostenuto tenutos.** Winds and brass hold full length, re-attacking on Sus with crossfades. Strings play Leg BC at v108 with the printed bows. Not changed since c28 (do not touch).

## Do not touch

- The keyswitch placement and row loading.
- Trombone 1's Sus MAX accents with swells, its CC7 heads and its slurred legato line (adjust only the shapes named in finding 4).
- The solo violin's v72-80 legato and its leads.
- The violas' Detache portato with per-note CC7.
- The tremolo rows and entries of bars 61-64.
- The pizzicato rows and velocity floor.
- CC15 mute placement and the horn mute EQ.
- The final-chord re-bow times and fits.
- The niente CC7 lanes in bar 66.
- The harp env_sustain 1.0, release 200 ms and HARP_RING_S.
- The celli 4 soli on the div track, if finding 1's refit brings the swing under 4 dB.
