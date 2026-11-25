# Critic B, cycle 57: balance and levels (c56 render)

Under review: `cycles/c56/render` (dry stems, returns, master) against `cycles/c55/render`, with `cycles/c56/rendered_build/parts.json` and `mix.json`, `cycles/c55/rendered_build/parts.json`, `build/roles.json`, `build/pitch_trims.json`, `build/score_config.py`. `cycles/c57/COORDINATOR-NOTES.md` was read first. Scripts and outputs: `cycles/c57/critic_scripts/B/` (`frames.py`, `ql.py`, `theme.py`, `margin.py` → `margin.txt`, `pernote.py` → `pernote.txt`, `items.py` → `items.txt`, `cb2.py` → `cb2.txt`, `cbctx.py`, `lowspan.py` → `lowspan.txt`, `h34.py`, `phr.py` → `phr.txt`, `variance.py` → `variance.txt`, `bal.py` → `bal.txt`, `chk.py` → `chk.txt`). Nothing was rendered; REAPER, the bridge, the lock, `build/` and `tools/` were not touched, and `build_reaper.py` was not executed. I cannot hear the render; each judgement is marked measured or inferred.

Method. Levels are K-weighted power in 4096-point frames (hop 1024) on the dry stems, averaged per quarter, per bar or per note on the parts.json tempo map; "margin" is a stem (or group) minus the power sum of every other dry stem. The c55 frames are those of `cycles/c56/critic_scripts/B/frames.npz`, the c56 frames were computed with the same script. Bass notes are measured unweighted (30 Hz-8 kHz) from 0.12 s after the note-on to the note end, arco notes of 0.5 s or more (155 notes); "residual" is a note's level minus a straight-line fit of level on the printed dynamic over those 155 notes.

## Manual notes

No row for c57 in `loop/MANUAL-READING.md` (third round, critics pick). Used: May 2021 HO manual section on volume and expression, `MANUAL-GAPS.md`, `EW-TEMPLATE-PLAN.md` sections 3 and 5, Rimsky-Korsakov `reference-books/text/rimsky-principles/p0051.txt`.

| Reading | Where it applies here | Does the render follow it |
|---|---|---|
| Volume "used to set a loudness level relative to other instruments", Expression to shape each instrument's dynamics (manual text line 2436, printed p.64) | Slow layers of the volume envelope (roles, pitch trims, soft trims) | Yes for roles and soft trims. The basses' pitch trims were fitted to an EQ that c56 changed (finding 1) |
| Rimsky-Korsakov: "in piano passages, all wind-instruments, wood or brass are of fairly equal balance" (p0051) | Horns 3-4 at p against clarinets, Horn 1, Horn 2 | No in bars 19-22: 6-10 dB under their own level at the same mark two bars earlier (finding 3) |
| Template plan section 5: phrase shape in the dynamics lane, no per-note bumps | `PHRASE_SHAPE` kind "drive" | Applied to held accompaniment notes too, where it writes a 20-unit CC11 fall under a flat printed p (finding 3) |
| Template plan section 3: timpani +8.6 dB at 84 Hz | `family_eqs.timpani` | Still not applied (as in c56); not pursued this cycle because the basses now supply the band |

## Answers to the coordinator's four questions, in short

1. Single bass pitches after the bell change: one pitch fails. F2 is 4.8 dB louder than in c55 and 5.8 dB over its neighbours, because its +3 dB pitch trim was fitted to the old -10 dB bell. Finding 1.
2. Theme over celli: +3.63 on my frames (actor: +3.56). One number in `roles.json` gives +4.12. Finding 2.
3. Margin changes over 1.5 dB between c55 and c56: 14 track-bars, listed in finding 4. Seven are the basses' EQ (5) and c56's intended rows (2); two are a render difference with identical MIDI (finding 5); the rest are pickup eighths and one horn note.
4. Horns 3-4 at p: the low median comes from bars 19-22, where a phrase shape lowers a flat p pedal by 8-12 dB, and from three single notes; a +2 dB p trim is still supported. Finding 3.

## Routine checks that pass (measured, c56)

- Timpani: loudest dry stem in 4 quarters (0, 1, 2, 328; c55: 5). Every roll of 3 s or more is 7-26 dB under the sum of the other stems after its first quarter (316-329 is the closest, -6.9 to -8.4 in its second half).
- Trumpets: under Violins I by 0.6 dB at 636-644 (fff), 1.8-10.3 dB in the other tutti spans. "Trumpets a2" is the loudest stem in 665-674, where it carries the coda theme at ff with Horns a2 and Violas: correct.
- Percussion: tam-tam leads only 484-492 (its fff stroke; 40-400 Hz 10-11 dB under the other stems). The suspended-cymbal stroke at 636 is 2.2 dB under the sum of all other stems at 6-14 kHz and 8.2 dB under at 3-6 kHz in its first half bar: present, not covering.
- Dynamic mapping (body medians, notes of 0.6 s or more on a flat mark): every track rises from p to f to ff to fff; no track changed by more than 1.7 dB against c55 (Clarinet 1 f +1.7 from the c56 trim).
- Named melody passages, margin median / lower quartile, c55 → c56: Violins I 56-88 +1.6 / +0.8 → +1.6 / +0.3; celli 184-216 +2.4 / +0.4 → +2.4 / +0.6; celli, Clarinet 1, Bassoon 1, Trombone 1 520-536 -0.5 / -1.4 → -0.9 / -1.3; Violas and celli 584-620 +3.2 / +1.5 → +3.2 / +1.3; Cello solo 680-696 +5.8 / +4.5 → +5.8 / +4.6. No passage median moved by more than 0.6 dB.
- Horn 1's counter line under the second theme (201-203, 588-589) went from -0.4 / -1.5 dB against the melody to -3.4 / -5.2: inside the 3-5 dB target of `roles.json`. An improvement, leave it.

## Findings

### 1. Double basses: F2 now stands 5.8 dB over its neighbours and is the loudest stem under five soft passages; the pitch trims no longer match the EQ (measured)

Where. `build/pitch_trims.json` "Double basses" (`"41": 3`, `"39": 3`, `"40": 4`, `"43": -6`, `"44": -6`, `"32": -3.5`, `"31": -2`, `"29": 3`), fitted while the 87.3 Hz bell stood at -10 dB and the two `mute_eq` bells existed. c56 set the bell to -4 and deleted the others; the trims stayed.

Evidence (`cb2.txt`; pitch, trim, notes, level c55 → c56, residual c55 → c56, residual minus the median of the pitches within 3 semitones):

| pitch | trim | n | c55 → c56 | residual | against neighbours |
|---|---|---|---|---|---|
| Bb1 | 0 | 10 | +1.1 | +1.6 → +0.6 | -1.1 |
| B1 | 0 | 4 | +2.4 | +3.1 → +3.6 | +3.0 |
| C2 | 0 | 34 | +2.1 | -2.5 → -2.3 | -2.9 |
| Db2 | 0 | 10 | +3.6 | +0.8 → +1.7 | +1.2 |
| D2 | 0 | 10 | +3.6 | -1.4 → +0.5 | -1.2 |
| Eb2 | +3 | 15 | +1.7 | -3.3 → -4.1 | -5.7 |
| E2 | +4 | 6 | +1.3 | +2.0 → +1.6 | +1.2 |
| **F2** | **+3** | 11 | **+4.8** | +3.3 → **+4.5** | **+5.8** |
| G2 | -6 | 7 | +1.3 | -1.6 → -2.6 | -4.2 |
| Ab2 | -6 | 4 | +1.1 | -0.7 → -1.4 | -2.3 |

- F2: 6 of 11 notes are more than 4 dB over the fit; the long ones read +7.0 (bar 10, qn 36), +7.4 (bar 38, qn 148), +7.3 (bar 68, qn 268), +8.6 (bar 111, qn 440), +5.4 (bar 7, qn 26). Its fundamental band rose 7.2 dB.
- In context (`cbctx.py`, unweighted): the basses are now the loudest dry stem in bar 10 (-37.8, Violins I -39.1), bar 11 on D2 (-29.8, Violins I -32.7), bar 68 (-38.4 at p, Violins I -40.5) and bar 111 (-35.8, celli -36.0); their margin against all other stems rose by 3.8-5.8 dB in each.
- Bar 44 (qn 172, Db2 at pp, +5.5 dB against c55): the basses read -42.7, the Horn 1 solo at p -45.8; Horn 1's K margin fell from -2.5 / -1.7 to -6.2 / -4.7 in quarters 173-174. This is the largest margin loss of a solo in the c55-c56 comparison and it comes from the EQ, not from NOTE_LEVEL.
- Against the celli on the same pitch class (unweighted, c56): C2 -2.5 dB (8 notes), G1 +2.6 (4), G2 -2.8 (3), F1 +0.6 (4), F2 +3.3 (1), D2 bar 11 +5.0. Against the tuba only three notes coincide (C2 +2.4, G1 +7.4 twice at 632, ff): no pattern. Outside F2 and the two notes named, the basses sit within 3 dB of the celli they double, which is the norm.
- The weak pitches are the tonic and its third: C2 (34 notes, 69 s, the most played) -2.9 and Eb2 -5.7 against their neighbours.

Fix (levels only; applicable with `tools/stem_fix.py` before any render, then written to REAPER):
- `pitch_trims.json` "Double basses": `"41"` 3 → **-1.5**; `"37"` (Db2) add **-2**; `"39"` 3 → **5**; `"43"` -6 → **-4**; `"36"` (C2) add **+1.5** with 8.0 in `_skip_onsets` (bar 3 already reads +14 from its role row).
- `note_trims.json` "Double basses": `"172.0": -3` (with the Db2 trim, -5: back to the c55 level under the horn solo) and `"42.0": -3` (D2, bar 11).
- Leave the EQ as c56 set it.

Acceptance: `cb2.py` on the new stem: residual medians of B1-Ab2 within ±2.5 dB, no F2 note over +4; Horn 1 margin at 173-174 at -3.5 dB or better; master 70-112 Hz share still -14.2 or higher (F2 is 20 s of 433 s, so the share should lose under 0.3 dB); no bar's master K level up by more than 1 dB.

Judgement: measured. That a 5 dB louder F2 is heard as a boomy note is inferred (Adagio c54 found the same after its bell removal).

### 2. Theme over the celli, bars 15-22: +3.63 against the +3.9 target; extending one existing role row to bar 22 gives +4.12 (measured, fix simulated)

Evidence (`theme.py`, Violins I minus celli per quarter 56-88): c55 median +6.31, lower quartile +4.81; c56 +6.43 / +3.63, 7 quarters under +3. The quarters that fell are 66 (-3.9 dB on Violins I), 69 (-3.2), 72 (-3.7), 77 (-2.1), 86 (-3.2), 87 (-13.2). Quarter 87 is a rest in Violins I (the quarter at 86 ends at 86.9): c55's +4.8 there was the 14 dB envelope jump on the release, so that quarter should not count; without it c56 reads +4.03. The others are pickup eighths and note tails whose single level c56 lowered.

The lower quartile is set by two places where the celli's own note levels are highest: 64-67 (celli envelope -0.5, +1.1, +1.6, margin +1.6, +2.7, -1.1, +3.0) and 84-87 (+1.4, +2.4, +0.4, margin +6.8, +2.5, +1.4, rest). The celli role `[56, 84, -2]` ends at 84, so bar 22, where Violins I fall from f to mf under a printed diminuendo, has the celli 2 dB higher than in bars 15-21.

Fix, cheapest first (all slow layer, `build/roles.json`):
- **"Violoncellos" `[56, 84, -2]` → `[56, 88, -2]`**: lower quartile +4.12, quarters under +3: 7 → 5, bars 15-21 untouched, bar-22 margin of Violins I against all stems back from -1.9 to about -0.9.
- Alternative with the same result on the number: "Violoncellos" `[56, 88, -0.5]` → `[56, 88, -1.0]` (+4.13, 6 under +3); it lowers the celli under the whole theme, including where the margin is already +8 to +16.
- Both together: +4.42, 4 under +3. Not needed.
- Do not raise Violins I: the body lifts were fitted at this level.

Judgement: measured; the fix is arithmetic on the per-quarter table (a role row is a constant gain).

### 3. Horns 3-4 at p: in bars 19-22 a "drive" phrase shape lowers their held pedal by 8-12 dB under a flat printed p (measured)

Where. Horn 3 and Horn 4, qn 72-88, held notes at p under the theme; `parts.json` `phrase_shapes` `[72.0, 88.0, "drive"]`; `build/score_config.py` `PHRASE_SHAPE["types"]["drive"] = (6, (10, 0.15), -10)`.

Evidence.
- CC11 runs 56 (qn 74) → 47 (80) → 38-41 (84-87) on Horn 3 and to 34-40 on Horn 4, with no hairpin printed until the crescendo at 88. Stem level per bar 19-22: Horn 3 -41.0, -47.9, -50.6, -48.7; Horn 4 -41.2, -42.4, -47.2, -53.0. Over the same bars the other stems read -26.8, -22.5, -25.8, -30.7, so the pedal is 24-27 dB under the texture in bars 20-21 and the horns' p in bar 22 is 8-12 dB under their p in bar 19.
- These bars supply 9 of the 21 "p" notes behind c56's medians (Horn 3 -48.9, Horn 4 -49.1 against Horn 1 -45.6, Horn 2 -42.7, Clarinet 1 -42.7, Violas -43.6).
- The other p notes: bar 164 (four horns on one chord) Horn 1 -47.3, Horn 2 -47.1, Horn 4 -47.1, Horn 3 -52.0 and -52.6 (qn 652, 654); bar 62 Horn 3 -49.0, Horn 4 -53.5 against Horn 2 -48.5; bar 126 Horn 3 -46.5, Horn 4 -49.6 against Horn 1 -45.3. All are inner harmony notes, none a solo; they sit 11-23 dB under the rest.
- The same shape on other held accompaniment phrases under a flat mark (`phr.txt`, first 30 % against last 30 %): Bassoon 1 72-88 mf -4.1 dB, Clarinet 2 137-144 p -5.0, celli 286-304 pp -5.0, Tuba 520-536 f -4.8, Bassoon 2 384-399 ff -5.3, basses 384-407 ff -4.0. Phrases with moving notes fall 0.7-2.1 dB in the median, which is the intended size.

Fix.
- `tools/score_to_parts.py`, the kind selection near line 3487: a phrase whose notes average 2 qn or longer (or under one onset per second) does not take "drive"; give it no offset (flat `tp_ = [(0, 0), (L_, 0)]`), behind a new key such as `PHRASE_SHAPE["types"]["drive_max_mean_qn"] = 2.0` in `score_config.py`. This changes CC11 on about ten phrases, so it needs the render; check Horn 3 / Horn 4 bars 19-22 (target: within 3 dB from bar 19 to bar 22) and Bassoon 1 72-88.
- `mix.json` Horn 3 and Horn 4 `soft_trim_db` "p" +2.0 (11.8 → 13.8, 12.4 → 14.4), pp unchanged: with the shape removed their p median comes to about -46.5, level with Horn 1 and Clarinet 2 (Rimsky-Korsakov p0051).
- Horn 3 qn 652-656: `note_trims.json` +3 on 652.0 and 654.0 (5 dB under the other three horns on the same chord).

Judgement: measured; that the pedal should hold is from the score (flat p, crescendo printed only from 88).

### 4. Where c56 changed the melody-minus-accompaniment margin by more than 1.5 dB (measured; list for the actor)

Per bar, tracks within 6 dB of the rest in either cycle (`margin.txt`), with the cause from `items.txt`:

| bar (qn) | track | margin c55 → c56 | cause |
|---|---|---|---|
| 2, 3, 8, 84 | Double basses | +1.6 to +2.0 | EQ, intended |
| 44 (172) | Double basses | -8.7 → -3.7 | EQ on Db2, finding 1 |
| 44 (172) | Horn 1 solo | -3.3 → -5.4 | the basses' Db2, finding 1 |
| 22 (84) | Violins I | 0.0 → -1.9 | quarter 86 -3.2 dB and the rest at 87, finding 2 |
| 46 (180) | Violoncellos | -4.0 → -6.2 | the quarter note at 183 (entry before the second theme) -2.3, envelope -1.6 |
| 102 (404) | Violins II | -4.6 → -6.8 | render difference, finding 5 |
| 103 (408) | Violoncellos | -4.2 → -6.2 | render difference, finding 5 |
| 108 (428) | Violas | +5.8 → +4.1 | Bass clarinet +4.5 dB at 429 with the same envelope (render difference) |
| 146 (580) | Violoncellos | -1.1 → -3.5 | pickup at 583 -2.5, envelope -1.0 to -1.5 |
| 151 (600) | Violoncellos | -1.8 → +0.1 | c56 row 601-603, intended |
| 154 (612) | Violas | -4.7 → -7.7 | c56 diminuendo row, intended |

Single quarters over 2.5 dB not in that table: Violins I 144 (-4.7, the pickup eighth at 144.5, margin +1.7 → -3.2) and 148 (-2.6, pickup at 148.5, +1.4 → -1.7); Violins I 479.0 (bar 120, ff, -3.5, still +7.4 over Trombone 1); Horns a2 311.0 (bar 78, -2.7, still +2.8 over the celli); celli 329 (-5.2, mostly the gap between two ff strokes: release level); Oboe 1 100-103 (-4.8 / -4.3 on the held ff note of bar 26, 16-19 dB under the tutti in both cycles). Per note (`pernote.txt`): 2-9 notes per string track and 0-8 per wind or brass track changed by 2.5 dB or more.

The one pattern: a pickup eighth before a long note lost 2.3-4.7 dB against the accompaniment (Violins I 66.5, 69.0, 72.5, 77.5, 144.5, 148.5; celli 183.0, 583.0). In c55 these carried a pickup lift that returned to 0 inside the note; c56 gives the note its mean.

Fix: no row for the theme pickups if finding 2's role change is taken (the acceptance number is met). For Violins I 144.5 and 148.5 (bars 36-37, the mf motif that c47 raised with a role row because it was level with the bassoon): `score_config.py` NOTE_LEVEL values +2.5 on those two onsets, or extend the pickup's level from the following note (same level as the note it leads to). Celli 183.0 and 583.0: +2.

Judgement: measured.

### 5. Two string notes spoke 0.3-0.6 s late in the c56 render with MIDI identical to c55 (measured)

Where. Violoncellos F3 at qn 408 (bar 103, mf, Leg Slur MAX after two Sus MAX eighths) and Violins II D5 at qn 404.5 (bar 102, ff, Leg Slur MAX after a Leg BC MAX note).

Evidence (`variance.txt`, `items.txt`): notes, keyswitches, CC11, CC1 and the envelope are the same in both `rendered_build/parts.json` files. Celli per 0.25 qn from 408: c55 -43 -40 -35 -34 -34; c56 -51 -59 -52 -47 -43 -41 -37 -31 (the note reaches its level at 409.75; quarter 408 -13.4 dB, 409 -4.2). Violins II from 404.5: c55 -32 -28 -28 -25 -23; c56 -31 -30 -31 -34 -32 -30 -29 -28 (quarter 405 -5.4 dB). Scan of every track for quarters that changed by 4 dB or more with the same envelope, CC11 and notes: celli 6 quarters (288, 350, 388, 408, 409, 670), Violins II 1, Clarinet 1 1 (275), Bass clarinet 1 (429); no other track.

This is the slow first-note layer of the legato row playing where the transition did not connect (BRIEF, facts: "a same-pitch re-attack on Leg Slur MAX plays the slow first-note layer"; c54 item 2 found legato notes after a Sus-row note unreliable). It also means single-note comparisons between two renders on the celli carry up to 5 dB of difference that no table caused.

Fix: `score_config.py` `SHORT_SUS_AT` add "Violoncellos" 408.0 and "Violins II" 404.5 (Sus MAX with the re-attack lead, as c54 did for the exposed rows), and the celli onsets at 288, 350, 388 if they are legato targets after a Sus-row note. Check on the next render that quarter 408 of the celli reads within 3 dB of -37.

Judgement: measured; the cause is inferred from the row sequence.

### 6. Low priority: A flat 1 on the basses, and the cymbal stroke (measured)

- Basses A flat 1 (51.9 Hz, trim -3.5): residual +3.4, 5 of 11 notes over +4 (bars 56, 57, 72 at pp +4.2 to +4.4; bar 160 fff +6.2). Unchanged by c56 (c55 +4.1). `pitch_trims.json` `"32"` -3.5 → -5.
- Suspended-cymbal fff stroke at 636, the movement's one fff: 2.2 dB under the sum of the other stems at 6-14 kHz for the first half bar, 11.5 dB under by the second. It does not cover anything. Whether it should be more present is a question for Dan's ear, not a measured fault; no change proposed.

Do not touch: the basses' EQ as c56 left it (only the trims follow it); the timpani levels and roll settle; trumpet and trombone trims; the theme's body lifts and the Violins I role `[56, 88, 2]`; the c56 rows celli 601-603 and Violas 612-616; Horn 1's level on 201 and 588 (now 3.4 / 5.2 dB under the melody); the one-level-per-note rule and its skip spans; the role spans and soft trims not named above.
