# Cycle 43, critic A (articulation and phrasing), on the c42 render

All levels are from the c42 final stems and master (`cycles/c42/render/`) and `build/parts.json` (equal to `cycles/c42` final). The scripts are listed at the end. They ran in my scratch folder, which is now deleted.

## Manual notes (MANUAL-READING row c43 / A: group A2, May 2021 HO manual PDF pages 95-99, read in full; MANUAL-GAPS.md read)

| Manual (PDF page) | Where in this mockup | Does the render follow it? |
|---|---|---|
| Pre-recorded runs exist for 1st Violins, Violas and Celli, one octave each, with KS or MOD direction control (p.95-96) | Bar 78's triplet run into the ff B flat 6 at 262 (Violins I/II) | Not used, and that is right. The printed run is not a one-octave scale. It plays on Sus notes led together (`GROUP_LEAD_AT`). |
| Slur Runs (Violins only) are meant for 16ths at about 125 bpm or faster (p.96-97) | The same run, about 46 bpm in triplet eighths | Correctly not used: the run is far below the patch's minimum speed. |
| Tremolo and Measured Tremolo TS do not respond to velocity; CC11 sets level and timbre continuously (p.97) | Violas trem. from 204; all strings trem. at 212-220 (sf > p) | Yes. The Tremolo row's CC11 is 114 -> 122 at 212.02, then falls smoothly to 46 at 216 (p). The sf decrescendo is in CC11, not in velocity. |
| The Repetitions instrument (Violas, Basses only) is a single note re-bowed about a dozen times in just over 1 s, tempo-synced, CC11 over 3 layers, no velocity (p.98) | MANUAL-GAPS #2 proposes it for S1 repeats | It does not fit the printed repeats here. They are two-note repeats of 1-2 qn, and the patch plays a pulsing train. I recommend striking the string half of gap #2 (inferred from the manual). |
| Legato needs no significant gap between notes; first notes of a phrase have no transition; legato patches are monophonic unless CC22 64-127 (p.98-99; p.99 polarity is backwards, 2025 p.91) | Every Leg Slur / Leg BC / Leg Port row | Yes. A scan of parts.json for overlaps over 0.12 qn, or simultaneous notes on a Leg row: **0 on all 32 tracks**. No chord reaches a monophonic legato patch. |
| Legato Slur Staccato gives the first note of each legato phrase a slightly stronger attack, automatically (p.99) | Slur heads now played as STR_REP_NEW_BOW strokes (Violins II 45/51, Violoncellos 66, Violas 69/248.5, basses 144) | Not used. This is an option for those heads (see finding 3), and it would cost one row per track. |
| Legato Bow Change for bow changes inside a legato line (p.99) | Leg BC MAX on unslurred connected string notes | Yes (`BC_*` tables). The keyswitches between Leg BC and Leg Slur are sent while the source note still sounds (scan: 44 on Violins I, 53 on Violins II, 40 on celli, all before the target). The manual's combination rule allows this. |
| Sul ponticello (violas only), trills (p.98) | none in v600 | n/a |

## Findings, ranked by what a listener would hear

### 1. Double basses: the old pitch rings under the new one at pp pitch changes; worst at bar 87 (qn 286)

**Where.** Double basses at every pitch change on the pp layer (CC11 34-40). The worst are:
- 286 (bar 87, A flat 1 -> F 1, the first note of the coda's "4 soli");
- 246 and 247 (bars 73-74);
- 220 (bar 65);
- 61 and 63 (bars 21-22);
- 164 and 292.

**What is wrong (measured).** I used a better measure than `linger42.py`:
- It takes only the old pitch's harmonics that do not coincide with the new pitch's.
- It times the window from the score onset. linger42 timed it from the led onset and counted shared partials, which made the octave and fifth changes read as lingering.

On the 37 arco pp/p changes, c39 / c40 / c41 / c42 give these values for old minus new at +0.35 s:

| | c39 | c40 | c41 | c42 |
|---|---|---|---|---|
| median old minus new | -15.1 dB | -30.6 dB | -29.9 dB | -28.2 dB |
| worst | +6.5 | -15.1 | -11.8 | **-0.1** |
| changes above -15 dB | 18 | 0 | 1 | 3 |

c40 (150 ms) and c41 (400 ms) are almost the same. Only c42 moved, and only at the pp-layer changes: 286 -11.8 -> **-0.1**, 246 -16.1 -> -8.4, 247 -16.0 -> -13.8, 220 -20.4 -> -16.4, 61 -27.3 -> -21.9, 63, 164 and 292 each 4-10 dB worse. The changes at CC11 46-52 did not move.

The build log explains this. On the basses only the "Db pp" / "Dbs pp" groups are capped at pp/p (shipped 931 ms, c41 400, c42 600). The Db p layer ships at 400 ms or less, so it is never capped. At 286 the old A flat 1 is as loud as the new F 1 for about 0.4 s: two pitches a minor third apart in the exposed ppp coda pedal.

**286 also has no lead (measured).** In parts.json, 286.0 starts on the beat (qn 286.0). Every other pitch change shown takes the 0.16 s `ABUT_LEAD`. The `abut_cond` AUTO_REBOW test skips any change that follows an auto-re-bowed held note, so the old note runs to the beat. The new F 1 reaches body -6 dB at +0.15 s and body -3 dB only at +0.75 s. 292 (lead 0.00, -24.6) has the same cause but is not audible. 246 is led and still reaches -8.4, so the cap is the main cause.

**Why a CC11 fall will not fix it (inferred from the data).** CC11 is one channel controller for the releasing old voice and the new note together. It has to be back at the new note's level at the led onset, 0.16 s before the beat. From then on the old voice's release comes back up with it. The measured window, +0.35 s, is 0.51 s after the old note-off.

c42's own `sus_fall` rows show the same limit. The lane is sampled only at fa and fb, so the "fall over 0.06 s" is written as a single step at the note-off: Double basses cc11 [155.25, 34] -> [155.856, 22] at the note end, back to 40 by 155.9. It returns within about 45 ms.

**Fix.**
- (a) `build/mix.json`, Double basses `sus_release_cap_ms`: the pp/p entry `ms` 600 -> **400** (c41's value, measured above: worst -11.8, every other change -16 or lower). This agrees with Movement I c47: 350 ms at p was fine on the upper strings, while uncapped basses held the old pitch within 10 dB at +0.35 s on 5 more of 17 changes. The Violins II, violas and celli entries stay at 600.
  - Cost (measured on the basses stem, final note): -20 dB at 0.36 s -> 0.27 s. The basses would stop about 0.09 s before the upper strings in the final chord.
  - Side gain: the basses' pp repeats separate more (c41 own-band dips at 156 / 168: 7.0 / 9.0 dB; c42: 6.0 / 8.2; 144: 4.1 against 2.8).
  - This is a basses-only Opus state change, so one full rebuild. Do not refit the basses re-bow fills from scratch. Take the "Double basses" rows from `cycles/c42/before/rebow_fills.json`: c41's final rows, fitted on the 400 ms render and re-levelled with `relevel41.py` (pedal at c39 means +1.5, coda at c39 means). The basses have no CC7 lane, so c42's new CC7 term in fit_rebows does not change them.
- (b) `build/score_config.py`: `ABUT_LEAD["Double basses"]["force_at"] = [152.0, 204.0, 286.0]`.
  - 286 gets the 0.16 s lead. The old note ends at the moved start, as at 246 / 61.
  - This moves no re-bow point: the 283.605 piece's note-off moves, not its start.
  - 292.0 can be added the same way (low priority).
- Alternative if the final chord must keep 600 ms on the basses: a new generic `ABUT_LEAD` option, for example `"pp_gap_s": 0.10, "pp_max_cc": 40`, in `tools/score_to_parts.py`. It ends the old note 0.10 s before the new note's moved start at CC11 40 or lower; the 600 ms release covers the gap. Estimate (inferred) from the c42 decay at 246: the old pitch falls from -15.8 to -31 dB re its body between +0.35 and +0.5 s, so 0.1 s earlier puts it near -25 dB at +0.35. This is untested and could open a hole before a slow F 1. (a) is the measured choice.

### 2. S1 (Dan): the four named repeats separate in their own register; the broadband master dip is the wrong test for inner parts

**Where.** The 15 soft repeats in `check42.py`.

**Evidence (measured).** I added a second test. It finds the octave band where the track stands highest over the rest of the mix (rest = master minus stem, over -0.45..-0.15 s, at or above the track's own range). It then takes the master's dip in that band with the same 30 ms windows as check42. Results for c42, with c41 in brackets:

| Repeat | Broadband master | Own-band master | Stem vs rest in that band |
|---|---|---|---|
| Violins II 45 | 1.8 | **5.5** (6.1) | -0.7 dB, 250-500 Hz |
| Violas 69 | 2.1 | **7.1** (6.1) | -7.3 dB |
| Double basses 168 | 2.0 | **8.2** (9.0) | +27 dB, 63-125 Hz |
| Double basses 156 | 2.9 | **6.0** (7.0) | +18 dB |

In their own register all four meet the 3-6 dB aim. The broadband figure is set by louder lines sounding at the same moment (the oboe solo at 45, the bar 23 tutti at 69, the cor anglais and violas at 156/168).

The repeats that really are weak:

| Repeat | Stem | Own-band master | Notes |
|---|---|---|---|
| Double basses 144 | 3.3 | 2.8 | basses are +16.5 dB over the rest in the band, so the stem itself does not separate |
| Violoncellos 66 | 2.9 | 3.8 | the smallest stem dip of the 15 |
| Violoncellos 128 | 8.4 | 0.1 | masked |
| Violas 82 | 8.6 | 2.8 | |

**Fix.**
- Use the own-band dip as the S1 pass test for inner parts. Keep the broadband one only for exposed lines.
- Basses 144 improves with finding 1(a): 2.8 -> about 4.1, the c41 value (measured).
- Violoncellos 66: see finding 3.

### 3. Violoncellos 66 (bar 23, "unis., cantabile, sul D", p): the counter-melody's head re-attacks with no gap or fall

**Where.** Violoncellos at qn 66. The old E flat 3 ends at 65.925 on Leg Slur MAX; the 66 stroke is on Sus MAX at 65.965.

**What is wrong (measured).**
- In parts.json the CC11 has no fall before the stroke: 33 at 65.625, 32 at 65.875, then straight up to 55 at 65.9549.
- c42 extended `sus_fall` to strokes, but this DOWNBOW_STROKE_AT note gets none. The cause is most likely the separate DOWNBOW path in `score_to_parts.py`, which does not reach the `rep_stroke` branch at line ~2425 (inferred from the code and the lane).
- Stem, 40 ms steps from -0.5 s: -43 -44 -44 -43 -43 -44 -45 -45 -43 -42 -45 -46 -46 -46 -44 -41 -40 -39. There is no dip before the beat; the only cue is the new note's +5 dB rise. Stem dip 2.9 dB, own-band master 3.8.

**Fix.**
- In `tools/score_to_parts.py`, let the `sus_fall` lookup also cover notes in `DOWNBOW_STROKE_AT` whose previous note has the same pitch and ends within 0.06 qn. Use the existing Violoncellos entry: 8 CC, 0.06 s, max_cc p.
- Or add a listed CC11 fall for 66 directly: 8 CC from 65.86 to 65.925, back by 65.965.
- Target: a stem dip of 6-9 dB, as Violoncellos 128 has (8.4).
- The manual's Legato Slur Staccato row (p.99, "a slightly stronger attack" on phrase heads) is the library's own answer for such heads, but it needs a row load and a test. Not this cycle.

### 4. Violas' portato eighths, bars 48-51 (sotto voce, Detache row): two pitches speak late, and repeated A3s alternate between two identical samples

**Where.** Violas 152.5-167.5, 15 off-beat eighths with rests between them.

**Evidence (measured).**
- Separation is good: peak minus the following rest is a median 30 dB.
- Perceived attack (first 30 ms window within 3 dB of the peak): median +0.03 s.
- The E flat 4s at 164.5 and 166.5 reach it at **+0.19 s**, against +0.01..+0.09 s for the notes around them (lead 0.20 s each). 165.5 / 167.5, the same pitch, are on time at +0.01 with a 0.12 s lead. It is a sample, not the lead.
- The A3 repeats 152.5 / 154.5 / 157.5 / 161.5 peak at an identical -44.0 dB at +0.16 s. 153.5 / 156.5 / 160.5 peak at an identical -44.6 at +0.30 s. The Detache row alternates two takes on this pitch. With the rests in between it is a regular A-B pattern (inferred: possibly heard as mechanical).

**Fix.**
- `build/score_config.py` `REATTACK_LEAD_AT["Violas"]` (or the portato lead table the c37 A #5 leads came from): +0.12 s at 164.5 and 166.5.
- Optionally break the A-B pattern on the A3s with velocity variation of ±6 on alternate notes (Detache velocity layers). Check the level afterwards.

### 5. Timpani: an 18 dB, 50 ms post-hall notch cuts the crescendo roll just before the p stroke at 172 (bar 53), and 8.7 dB before 262

**Where.** Timpani vol_db 171.94 = +14.05 dB, 171.95 = -3.98, back to +11.4 at 172.0. At 261.875-261.95 there is the same kind of 8.7 dB drop into the f roll.

**Evidence (measured).**
- Timpani stem, 40 ms steps around 172: -41 -42 **-57** -44 -38. A 15 dB hole about 40 ms long, 0.06 s before the stroke.
- The master does not show it (the timpani are 10 dB under the mix there).
- It is in the volume envelope, so it cuts the roll's hall as well as the roll (the S3 mechanism, on a small scale).
- A timpanist's crescendo roll ends on the stroke without a gap (inferred).

**Fix.** In the timpani roll-to-stroke code in `tools/score_to_parts.py`, where it writes the drop at the Flt Lng keyswitch (171.94 / 202.94 / 209.44), replace the post-hall notch with a CC11 dip, or remove it. If the stroke needs separation, make it pre-hall (CC11/CC7, BRIEF S3). Check the timpani stem's dip at -0.06 s afterwards: it should be at most 6 dB.

### 6. S3 check: no printed sudden drop cuts the hall (measured; nothing to fix)

I scanned every track's vol_db for falls of 4 dB or more within 0.15 s while a note sounds or within 2 s after one ends (243 hits).

- **Printed drops** (fp at 147.5-149, the breath at 194.5-196.5, the niente at 222-226, 203-205, 261-263, 270-272): only re-bow fill contours appear there. The stems show no step: Violins II at 223.4-224.6 stays within -40..-44 dB at 40 ms resolution, and the master falls smoothly (c42's 9.3 dB over 223-225.5).
- **In tails**: only three hits. Two sit at the caesura before the ff 204 (Clarinet 2 -5.5 dB 0.03 s after its note end, Horn 1 -4.4 dB) under the tutti attack, so they are masked. The third is Flute 1 124 (-4.4 dB, 0.39 s after its note end).
- **Do not regress**: the fp spike stays in CC11, and the bar 66 fade stays in CC7.

## Other checks, all passing (measured)

- **Trombone 1 accents** (Dan's weight, not bite): 2-5 kHz over the first 80 ms minus the body (0.15-0.45 s) is -3.3 dB at 213 and -11.0 dB at 218. The master's 2-5 kHz jump at each attack is -0.8 / -2.1 dB.
- **215** (legato target v124): +7.9 dB on the stem but -1.1 dB in the master. It holds, as in c42 A #5.
- **Tremolo, bars 61-64**: on the Tremolo row with no lead. Violas from 203.94, the other sections from 211.94; sf and decrescendo in CC11.
- **Basses pizz at 212**: keyswitch at 211.94, arco back at 213.5.
- **Re-bow dips** (c42 `rbdips` final): the dips of 6 dB or more are Violas 50 / 62 / 71, Violins I 295 and Violas div 301.25. All of them are printed repeats, where a dip is wanted for S1. Violas 62 / 71 settle 3.9 / 4.3 dB under the piece before them; this is a small step, left to critic B.

## Do not touch

- Hall: fx_volume 0.095, low cut 160, ir_setup 0.7.
- The 600 ms pp/p caps on Violins II, violas, celli and the div/solo tracks.
- c42's CC7 term in `fit_rebows.py` and the bar 66 niente CC7 fade.
- Trombone 1's Sus MAX and swell accents, its CC7 110/120, and the 214.5/215 shapes.
- The violas' portato on Detache, with its 30 dB separation.
- The Tremolo-row CC11 sf decrescendo at 212-216.
- The bar 91 viola shapes.

## Scripts (in /private/tmp/claude-501/mockup-loop/mvt2-c43-A/, now deleted)

- `linger.py`: the old pitch's unique harmonics re its body, and old minus new, from the score onset.
- `reps.py`: S1 dips, broadband and own-band.
- `arr.py`: new-pitch arrival.
- `fin.py`: final-note release.
- `port.py`: portato attack timing.
- `acc.py`: 2-5 kHz accent attack.
- `s3.py`: fast vol_db falls under sounding notes or tails.
- `scan.py`: chords on legato rows and mid-note keyswitches.
