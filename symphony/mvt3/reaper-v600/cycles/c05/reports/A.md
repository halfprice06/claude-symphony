# Cycle 5, critic A: articulation and phrasing (render c04, score v600)

Method. All numbers come from the c04 stems and master (`cycles/c04/render`). `cycles/c04/rendered_build/parts.json` is identical to `build/parts.json`. Notes are placed on the tempo map with `tools/pcx.py` (TM).

Measures used:
- **pc (S2).** `pcx.attack_pcx`, re the score onset.
- **Repeat dips (S1).** On the note's harmonic band: min(peak before, peak after) minus the minimum around the onset.
- **Accent front (item 4).** 2-5 kHz over the first 80 ms minus the body over +0.15..+0.6 s. "Weight" is the first 0.2 s level minus the median of plain notes within ±4 qn on the same track.
- **Timpani brightness.** 1-5 kHz minus 60-250 Hz over the first 0.3 s of each stroke.

"Measured" means a number from the render, parts.json, the score or a patch. "Inferred" means reasoned, not tested.

## Manual notes (cycle 5, slot A: 2021 manual PDF pages 160-162 and 188-190, read in full; Movement I's c41 A table checked against the Finale)

| Manual (PDF page) | Where it applies in the Finale | Does the render follow it? |
|---|---|---|
| p.160: each articulation cell has a load switch (RAM in/out); KS Masters trigger rows by keyswitch | `build_reaper.py` loads only the rows a track uses | **Yes (measured).** No keyswitch on any of the 31 tracks goes to a row the track does not use (`art_counts` against the `ks` lanes). |
| p.161: keyswitch notes lie outside the playable range | KS Masters whose keys lie inside the range (basses, celli, 1TB, contrabassoon) | **Yes (measured).** No played note on any track sits on a keyswitch key of its patch. |
| p.161, p.189: Keyswitch Range (pass thru, offset); Program Change | | Not used. Not needed. |
| p.162, p.190: Controller trigger (CC value ranges select a row) | CC1 lanes: brass/clarinet dynamics, string/wind vibrato, timpani layers | **Yes (read, Movement I c41).** Plain key triggers only, so no CC lane switches a row. |
| p.162, p.189-190: velocity-range layering (a short row at v110-127 over a sustain gives an accent on hard notes) | 1,109 printed accents; the brass heads 247-262; the chorale | **Not used, and not needed (measured).** Accent fronts are negative on every track and span, median -5..-26 dB. The highest are Flute 1 1068 (+1.5) and Violas 1056 (+0.7). Accent weight medians are +1.5..+6 dB over neighbouring plain notes, Dan's 2-4 dB range. In the same instance a v110-127 layer would also fire under every v124 legato target (inferred, as Movement I c41). |
| Opus p.86 via p.160: Exclusive keyswitch behaviour | 1,000+ row changes | **Yes (measured).** 35-127 row changes per track happen while a note of the old row sounds: Sus -> Leg Slur heads, Leg Slur <-> Leg BC, Tremolo <-> Sus, timpani Rls <-> Lng. Exclusive triggers do not cut the old note. The shortest keyswitch lead before its note is 7.1 ms (string re-bows at 174-181, 425-568); everything else is 9.9 ms or more. No keyswitch falls on or after its note. |
| p.188: Voice Limit (one note uses a voice per mic and per crossfaded layer) | Harp final glissando and chord, div. a 3 tremolos at 1108, string div. chords | **Yes (inferred from counts).** Most notes sounding at once, release included: harp 19 (the 1106-1108 glissando plus the chord), strings 4-6, winds and brass 2-3. Opus limits are 250/350 (Movement I c41). No missing chord tones were found. |
| p.188: Octave, Key Range | Bass trombone B♭1 (key 34) at qn 416 | **No (measured):** the note is effectively silent (finding 6, MANUAL-GAPS #13). |
| p.188-190: Zones (several instruments in one instance with trigger options) | The timpani stick changes the score prints (finding 2) | Not used. It is the manual's alternative to a second instance (finding 2, option b; untested). |
| p.116 (read for finding 3): 22in K Crash has three lengths (long / short / even shorter) | Final crash at 1108 | The long sample is used and held 8.95 s past a printed release (finding 3). |
| p.123 (read for finding 2): felt timpani rolls have "a blended timbre since the individual attacks aren't as strong" | Soft and medium-stick passages | Not used: everything plays on Timpani Hrd KS (finding 2). |

MANUAL-GAPS items in this lens, still open:
- #13: the bass trombone's low note (finding 6).
- #12: recorded crescendo rolls (felt). It belongs with finding 2.
- #5: expressive wind rows. It is not this render's top problem.

## Standing checks

- **Item 4, accents (measured): passes, no bite.** Brass accent fronts (median, per span):
  - Più allegro 984-1080: Horn 1 -21, Horn 3 -21, Trombone 1 -10, Trumpet 3 -12, Tuba -14 dB.
  - Final bars: -7..-26 dB.
  - Accent weight in 984-1080: Trombone 1 +5.7, Horn 3 +1.7, Trumpet 3 +1.7 dB. Trumpet 3's accented halves at 255-262 are at the light end, but they are accompaniment.
- **S1, repeats (measured): passes nearly everywhere.**
  - Coda / Più allegro median dips: basses 7.4 / 8.3 dB (161 eighths), Trumpet 3 7.4, contrabassoon 10.2, violas 9.1 in the coda.
  - Chorale median dips: violas 12.9, Violins II 8.7 dB.
  - Under 3 dB: basses 821-823 and 836-839 (the accelerando to 184 qpm, 2.2-2.8 dB), Bass trombone 836 (2.1), Tuba 932 (1.8).
  - Weak: Violas 1033-1047 (finding 1).
- **S2, Più allegro and coda (measured).**
  - Brass fresh-attack medians -15..+21 ms; tuba, timpani and contrabassoon on time.
  - Strings staccato medians -2..+35 ms.
  - Outliers: finding 1 (violas and celli) and finding 5 (cello pizzicato).
- **Item 7, loops (measured): passes.** Apart from the crashes, no note is held 6 s or longer except Horn 4 168 (6.5 s) and the timpani roll at 920 (7.0 s). Too short to fold. The strings are re-bowed.
- **Tremolo (measured).** Every string note marked tremolo is on the Tremolo row. The marks without their own note (Vln I 1020/1028/1036, all sections 1112) are ties. The harp étouffez marks (326, 520, 534, 968, 1113) are damped: no harp note sounds past any of them.

## 1. Violas' and celli's same-pitch strokes on Sus MAX arrive 60-180 ms late; the violas' ff repeated quarters at bars 259-262 run together (S1, S2; measured)

**Where.**
- **Violas, qn 1033-1047** (bars 259-262, Più allegro, ff crescendo to fff, plain quarters on F4 / F♯4 / G4 under the wind chorale):
  - pc +111 ms median (1033 +132; 10 notes over +60 ms).
  - Repeat dip 4.4 dB median (p10 3.6).
  - Played gap 14 ms.
- **Violas, 840-860** (bars 211-216, Largamente, div. thirds as slurred tenuto half-note pairs): +60..+145 ms (854 +145, 858 +144). 8 of 13 fresh strokes are over +60 ms.
- **Violoncellos, 604 / 606 / 608 / 630 / 658** (the ff bass line of the recapitulation): +136..+184 ms, although they are led 0.28 qn (0.10 s). This is c02's open "cello strokes" item.

**Evidence (measured, `rep_pc`: every string Sus MAX note after a same-pitch note with a played gap under 0.12 s).**

| track | group | n | median pc | over +60 ms |
|---|---|---|---|---|
| Violas | unled, v≤100 | 48 | +60 ms | 25 |
| Violas | led, v>100 | 25 | +90 ms | 15 |
| Violoncellos | unled | 20 | +101 ms | 15 |
| Violoncellos | led | 14 | +132 ms | 11 |
| Double basses (detach dip + 0.10 s lead) | unled | 280 | -19 ms | |
| Violins II | led | 16 | +6 ms | |

- In parts.json the violas' 1033-1047 notes have `qn == sq` (no lead), v96, dur 0.96 qn.
- They are written-out repeated strokes (`rep_sus`), and `retongue_ok` in `tools/score_to_parts.py` returns None for `rep_sus` unless the note is a `sus_min_s` repeat.
- A quarter at 176 qpm lasts 0.34 s, under `STR_REP_NEW_BOW["sus_min_s"]` = 0.4 s. So they get neither the stroke gap (0.06 s) nor the re-tongue lead. This is the gap Movement I c45 closed only for notes over sus_min_s.

**Fix.**
1. **`build/score_config.py`:** `STR_REP_NEW_BOW["sus_min_s"]` 0.4 -> 0.3.
   - Repeated quarters at 168-176 qpm then become new bows: gap min(0.06 s, 25 %), and `RETONGUE_LEAD_S` Violas 0.10 s via `rt_for`.
   - Before the build, diff parts.json for every string note whose gap or lead changes, and list them in CHANGES.md.
   - If the change reaches beyond 1032-1048 and the chorale `skip` spans, restrict it with a span list. A new `"sus_min_spans"` key in the tool would read like `"skip"`.
2. **Celli** (already led 0.10 s, still +130 ms):
   - Add `"Violoncellos": 0.17` for Sus MAX repeat strokes. Either use a new `RETONGUE_LEAD_ART_S["Violoncellos"] = {"Sus MAX": 0.17}` (the table exists for Oboe 1), or put per-onset values in a repeat-lead table. That is 0.6 × the measured +120 ms excess over the target.
   - Also give the celli the basses' dip on the ff bass line: `STR_REP_DETACH["at"]["Violoncellos"] = [(600.0, 664.0, {"max_qn": 2.0, "same_pitch_only": True}), (968.0, 976.0, {"max_qn": 2.0, "same_pitch_only": True})]`.
3. **Violas 840-860 louré pairs:** after step 1, check whether they take the STR_REP_NEW_BOW "tenuto"/"portato" lead. If not, add 0.06 s extra on those onsets.
4. **Targets:** Violas 1033-1047 pc within ±40 ms and dip ≥ 7 dB. Celli 604-658 pc ≤ +50 ms. Viola/cello repeat medians within 40 ms of the basses.

## 2. The score's soft and medium sticks play on the hard-stick patch: the pp "near the rim" figure (bar 178) and the soft rolls into the C-major arrival (bars 219-222) are 9-20 dB too bright (measured; manual p.123)

**Where.**
- `sections/recS.ily` line 170: "soft sticks" at bar 171 (qn 680), the pp "near the rim" figure at 708-711, then "hard sticks" at bar 178 (711).
- `sections/codaTwo.ily` line 64: "muta D♭ in C / medium sticks" at bar 215 (qn 856).
- `sections/finale.ily` line 213: "hard sticks" again at bar 255 (qn 1016).
- So 856-1016 covers the sub. p roll and crescendo 872-888 into the arrival, the chorale's f strokes 892-918, the roll from 920, the soft roll at 970 and the Più allegro's first strokes 984-1015.
- The extraction drops the stick markups on multi-measure rests, so only 708 "near the rim" and 711 "hard sticks" reach `mockup-events.tsv`. The BRIEF's "hard sticks" is therefore incomplete.

**Evidence (measured, brightness per stroke: 1-5 kHz minus 60-250 Hz, first 0.3 s).** Movement I c42 (Timpani Flt KS) against the Finale c04 (Timpani Hrd KS):

| velocity, length | felt (M1 c42) | hard (Finale c04) |
|---|---|---|
| v50-79 short | -34.1 dB | -18.2 dB |
| v50-79 long | -25.0 dB | -15.6 dB |
| v80-127 | -12..-18 dB | -13..-15 dB (the same) |

- Hard sticks are 9-16 dB brighter at soft dynamics. At loud dynamics the two patches match.
- In the soft-stick span: 708-710 (pp, v56) measure -14.5..-19.8.
- In the medium-stick span: the sub. p rolls 872 / 876 (v53, the latter 12 qn long) measure -15.6 / -16.5 dB, and the soft roll at 970 -16.5. Felt soft rolls measured -37.6 (v<50) / -25.0 (v50-79).
- Manual p.123: felt rolls have "a blended timbre since the individual attacks aren't as strong". This is Dan's rule about rolls settling under the texture, done with the beater the score asks for.

**Fix.**
- **(a) Preferred: a second-pass "Timpani felt" track** on `Drums/Timpani/Timpani Flt KS.oib`.
  - Movement I's `ALIAS_TRACKS` / `PASS2_TRACKS`, `TRACK_WINDOWS` {"Timpani felt": [(679.9, 711.9), (855.9, 1015.9)]}. The main Timpani rests inside the windows.
  - Movement I's felt maps (`TIMP_CC1_MAP`, `TIMP_ROLL_TRIM_DB` in `symphony/mvt1/reaper-v621/build/score_config.py`) apply to the alias, and `TIMP_ROW` takes the Flt row names.
  - The main project's memory does not change.
  - The timpani part has no espr./dolce marks, so the alias boost-span bug that holds back "Horns a2" should not apply (inferred). Still diff the alias's notes and CC lanes against the main track before rendering.
  - Level: fit per window on the first render against the c04 levels (stem minus master at 872-888 and 892-918 within ±1.5 dB).
- **(b) Alternative: the manual's Zones route** (p.188-190): both KS patches in the one Opus instance, switched by a Controller trigger range. It is not supported by `opus_state.py` today and is untested.
- **Targets:** brightness of the 708 and 872-888 strokes and rolls ≤ -25 dB. Roll level per item 5 unchanged or lower.

## 3. The final crash and bass drum ring 9 s and 6 s into the silent fermata; after the cut-off the master is the cymbal alone (measured; score finale.ily line 243)

**Where.** qn 1108-1116.
- The score has `cymc1->\fff~ | cymc4 r4 r2\fermata` and `bd1->\ff~ | bd4`: the strokes end with the orchestra's final quarter at 1113. The fermata is on the rest.
- The harp's étouffez at 1113 asks for the same dry stop.
- `build/score_config.py` says "the final quarter at 1112 is under a fermata". It is not.
- PERC_MAP `min_s` 9.0 / 6.0 holds the crash to 1129.6 qn and the bass drum to 1122.4.

**Evidence (measured, 0.25 s RMS after the cut-off at 1113, 421.77 s).**

| time after the cut | master | crash stem |
|---|---|---|
| +1 s | -48.9 dB | -49.3 dB |
| +2 s | -53.8 dB | -54.0 dB |
| +3 s | -59.5 dB | -59.7 dB |
| +4 s | -64.9 dB | -65.1 dB |

- From one second on, the final silence is a crash wash.
- The patch obeys the note-off: the 888 crash fell from -76 to -117 dB within 0.5 s of its note-off. A note-off at 1113 therefore damps it the way a player would.

**Fix.**
- `tools/score_to_parts.py build_perc_track`: a generic per-onset end, `PERC_END_AT = {track: {stroke sq: end qn}}` (default none). It overrides `min_s` for the listed strokes.
- `build/score_config.py`: `PERC_END_AT = {"Crash cymbals": {1108.0: 1113.2}, "Bass drum": {1108.0: 1113.2}}`, and correct the comment.
- Keep `min_s` for 888 and 1048 (whole notes followed by rests; letting them ring is the usual reading).
- **Target:** crash stem at least 10 dB under the master at +1 s after 1113. The master's decay after the cut close to the other tutti cut-offs: drop at 0.3 s ≥ 18 dB, no plateau after 1 s.

## 4. Muted Trumpet 1 trails the cor anglais it doubles by 35 ms (S2; measured)

**Where.** Trumpet 1 con sordino, bars 171-183 (qn 680-694, 712-728), on "Mute Sus" in unison with the cor anglais' legato line.

**Evidence (measured).**
- Over 22 slurred joins, Trumpet 1's pc median is +43 ms (692 +123, 723-726 +58..+69). The cor anglais is at +8 ms over 37 joins.
- The trumpet notes are butted fresh attacks at v53 with no lead (overlap 0 ms). The cor anglais is on Leg Slur MAX with 14 ms overlaps.
- The join dips are similar (trumpet median 3.7 dB, cor anglais 4.7), so the line is connected. The problem is the 35 ms offset in a unison, which smears the doubled solo (inferred: Dan's "mushy").

**Fix.**
- A generic per-row lead in `tools/score_to_parts.py`, e.g. `ROW_LEAD_S = {"Trumpet 1": {"Mute Sus": 0.035}}`. It applies to every note on the row, the previous note ending at the moved onset. The listed `entry_leads.json` path does not reach abutting notes.
- Or close c03's open `SLUR_ON_SUS_OVERLAP` item with the same lead.
- **Target:** Trumpet 1 pc median within ±15 ms of the cor anglais on the shared onsets.

## 5. Cello pizzicato lands 39 ms after the basses on every shared note (S2; measured)

**Where.** Bars 51-66 (qn 200-264). All 24 cello pizzicato onsets coincide with the basses'. The same rows play at 456-488 and 680-744.

**Evidence (measured).**
- Celli "Pizzicato RRx4": pc +42 ms (p90 +78), harmonic-band peak +145 ms.
- Basses "Pizz RRx4": pc +3 ms, peak +88 ms.
- Violins II and violas: pc +25 / +12 ms.
- No pizzicato note is led (`qn == sq`). Under the soft trumpet solo the bass line plucks as a flam (inferred).

**Fix.**
- A generic `PIZZ_LEAD_S` in `tools/score_to_parts.py`, the same mechanism as `STAC_LEAD_S` but keyed on the pizzicato rows: `{"Violoncellos": 0.035, "Violins II": 0.015}`.
- **Target:** cello pc within ±15 ms of the basses on the shared onsets.

## 6. Smaller items (measured)

- **Bass trombone B♭1 at qn 416** (bar 105, sf staccato landing note, doubled only by the basses): stem -56.7 dB against -38.4 dB on the note before. The harmonic band is 17.5 dB lower, so the note is effectively missing (1TB lowest sample key 36, MANUAL-GAPS #13).
  - The tuba rests at 414-418, so the cheapest fix is to move that one note to the Tuba track. That needs a generic note-move rule (`NOTE_MOVE = {("Bass trombone", 416.0, 34): "Tuba"}`).
  - Otherwise a 3TB / "2 Trombones and 1 Bass Trombone" source in the second pass.
- **Basses' accelerando eighths 821-823 and 836-839** (184 qpm): repeat dips 2.2-2.8 dB against a 7.4 median. The 0.08 s detach dip is half an eighth here. Try `dip_s` 0.06 inside 816-840 only if Dan hears it.
- **Violins I "4 soli" / gli altri octaves** (473-476, 485-488, pp dolce, slurred): played as a Sus MAX octave chord, so the slur is not legato. Dips 0.6-5.7 dB against 4.9 on the section's legato eighths, so they do not sound detached. Not ranked.

**Do not touch:**
- The keyswitch layout: Exclusive triggers, 7-10 ms keyswitch leads, row loading.
- GENTLE_ACCENT and the brass accent shaping (no burst, weight 1.5-6 dB).
- The wind staccato rows from c04.
- The basses' STR_REP_DETACH / +1.5 dB hold (Più allegro dips median 8.3).
- WIND_REP_RETONGUE_BY and the horn release cap (brass repeat medians 4.3-12.3 dB).
- The tremolo rows and their ties.
- The harp étouffez damping, harmonics and glissando.
- The crash and bass drum at 888 / 1048 ringing.
- The c03 dry hall and release caps.
