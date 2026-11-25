# Cycle 47, critic A: articulation and phrasing (render c46, score v621)

## Method

All measurements are on the delivered c46 stems and master (`cycles/c46/render`, 40 stems after the swaps, splices and stem fix), placed with `build/parts.json`. I checked that this file equals the render-time builds (`cycles/c46/rendered_build*/parts.json`) in every note, keyswitch and CC lane, and differs only in the stem-fix volume rows of Violins I, Violins I f62 and Cello solo. Comparisons with c45 use `cycles/c45/render` with `cycles/c46/before/parts.json`, and with c44 use `cycles/c44/render` with `cycles/c45/before/parts.json`. The scratch scripts were deleted after the run, as the brief asks.

Measures:
- **pcX** (`tools/pcx.py attack_pcx`): the perceived attack in ms after the score onset, measured on 5,231 notes of all melodic tracks.
- **Crossover** (`pcx.pair_window`).
- **Band arrival**: the time the note's own harmonic band reaches 6 dB under its level at +0.05..+0.2 s and at +0.3..+0.5 s. I used this to check pcX wherever a note blooms after its attack.
- **Join dip**: 30 ms and 100 ms stereo power over the lower body, on all 1,397 monophonic legato joins.
- **S1**: pitch-band dip of 751 monophonic written repeats.
- **Item 8**: 2-5 kHz in the first 80 ms minus the body, on 633 accents.
- **Item 7**: the c25 loop scan (100-300 Hz band and centroid autocorrelation at 3.95 s on every held span of 6 s or more).
- **Re-bows**: `cycles/c44/actor_scripts/rebows44.py`.
- **Strokes**: `cycles/c46/actor_scripts/strokes46.py` and `under46.py`.
- **Envelope simulations**: a stem scaled by a volume row. They are exact for level-only changes, because the envelope sits after the Opus hall.
- **rel**: stem minus master over a note's first 0.3 s.

Labels: **measured** (render or parts.json), **read** (code, config or patch file), **inferred** (reasoned, not tested).

## Manual notes

This is the second round. c47 re-reads c41 slot A's pages: 2021 manual PDF pp. 160-162 (the Articulations window and trigger options) and pp. 188-190 (the Zones window). I read them in full and looked at pp. 162 and 188 as images. I also read MANUAL-GAPS.md and DIGEST.md (sections 2.3, 5, 7 and 8).

**MANUAL-GAPS items still open in this lens:**
- **#3 Solo Cello:** still not installed (`ls "/Volumes/MAC DRIVE/"`: Brass, Harp, Percussion, Woodwinds and Strings only).
- **#5 expressive wind rows:** untried. The wind espr. solos already ramp CC1 65 -> 100 over each phrase's first note (delayed vibrato; Cor anglais 18.9-19.4 and 682.9-683.4, read).
- **#7 half-section divisi:** untried. Pass 2 has the memory now.
- **#9 horn portato rows:** untried (the four Horn 1 tenutos were evened in level in c38).
- **#12 Felt Cresc:** untried.
- **#13 bass trombone low notes:** still transposed E2 samples.

None of these is behind a problem I measured this cycle. Finding 1 is a render-state problem, not a patch choice.

| Manual (PDF page) | c41 A's note | Now (c46 render) |
|---|---|---|
| p.160: each articulation cell has a load switch; KS Masters select rows by keyswitch | Every row a track switches to is loaded and keyed | **Still followed** (read). In all 33 main-project states in `jobs/`, every row parts.json uses is loaded and active (Cor anglais "Sus MAX" maps to the patch's "Sus Max" row, case only). |
| p.161: keyswitch notes lie outside the playable range | No note on a keyswitch key | **Still followed** (measured). 0 notes on a keyswitch key of their patch, on all 40 tracks. |
| p.161: Keyswitch Range and Program Change triggers | Not set | **Still not set** (read). Every trigger entry carries only key, keyMax, pass, volume and behaviour 0. |
| p.162, p.190: Controller trigger (a CC range selects a row) | No controller triggers, so the CC1 lanes cannot switch rows | **Still followed** (read). |
| p.162, p.189-190: velocity-range layering (sustain plus a short at velocity 110-127 as an accent) | Not used, and should not be in the same instance, because velocity sets legato speed | **Still right** (measured). Accents carry weight without bite. 2-5 kHz front minus body: brass median -11.6 dB (p90 -2.8), winds -6.2 (p90 +0.2), strings -4.0 (p90 +2.8). The master's 2-5 kHz jump at accents is -1.2..+0.3 dB median. The two exposed bright string accents come from a pickup lift, not from an accent layer (finding 3). |
| Opus p.86: Exclusive / Toggle / Temporary | All Exclusive; row changes under a sounding note do not cut it | **Still followed** (measured). 1,178 keyswitches (1,143 after the pre-roll). The shortest lead is 9.5 ms. None falls on or after its note. 485 are sent while a note of the track sounds (c41: 480). No chord goes to a legato row, no same-pitch notes overlap, and no legato overlap is longer than 0.16 s. |
| p.188: Voice Limit | 350 strings, 250 others; no dropped chord notes | **Still followed** (read and measured). Same limits. The silent-note list holds only its two known false alarms (Trombone 1 552, Timpani 727). |
| p.188-189: Octave and Key Range | Every zone 0-127, octave 0 | **Still the same** (read). |
| New on this reading: p.188 Zones / p.189 trigger options make two instruments in one instance switch together (Group), not just rows | | The c41 reading covered the use that matters (layering). Nothing new to apply. |

## 1. Trumpet 1's slurred notes rendered in the "flipped" legato state again: 4-12 dB louder and 65 ms earlier than c45, with identical data, so at letter D the trumpet stands 6-11 dB over the violins' tune (measured)

**Where.** Trumpet 1 (Solo Trumpet KS Master, Leg Slur MAX targets): bars 69-71 (qn 275.5-283.5, the closing theme at f, doubling Oboe 1 and Violins I) and bars 113-114 (qn 451.5-455.5, the stringendo). Also one Horn 3 note, 164 (bar 42, ff a2).

**What is wrong (measured).** Trumpet 1's notes, keyswitches, CC1 and CC11 are identical in c45 and c46. Its volume envelope differs only at bars 122 and 160 (the fff lifts). Yet its stem changed:

| | c44 | c45 | c46 |
|---|---|---|---|
| pcX median, 15 legato targets (ms) | -9 | -10 | **-76** |
| Crossover median (ms) | 0 | 0 | **-38** |

- **Level, first 0.3 s of each target, c45 -> c46:** +1.4..+11.7 dB, median +6.4. Examples: 277 +8.8, 283 +11.7, 283.5 +9.2.
- **Per bar:** 70 +6.7, 71 +8.5, 114 +5.9 dB.
- **Timing.** The band of each new pitch now jumps to its body level 0.02 s after the moved onset, so with the 0.10 s brass lead it sounds 60-100 ms early. Band arrival at 277 is -0.058 s and at 283 -0.090 s.
- **Balance against the tune, per quarter, Trumpet 1 minus Violins I:**
  - c45: qn 276 -4.2, 277 -3.2, 279 -7.4, 282 -6.9, 283 -0.9 dB;
  - c46: +1.9, +5.3, -0.3, -0.2, +9.8 dB.
  - Trumpet 1 minus the master at 277 went from -10.3 to -3.5 dB.
- **No other brass track moved.** Horns 1-4, Trombones 1-2, Bass trombone, Horns a2 and Trumpets a2 stayed within 5 ms. The scan of every main track for bars with unchanged data and over 1.5 dB of change found only:
  - Trumpet 1 (bars 70, 71, 113, 114);
  - Horn 3 bar 42 (+3.6; the 164 Leg Slur target +5.6 dB);
  - the known c45 Violas swap;
  - small celli and basses differences (1.8-2.5 dB in four bars).

**Cause (inferred from the loop record).** This is the state c43 reported: "Horn 1 and Trumpet 1 Leg Slur targets flipped to a louder (1-14.5 dB), about 50 ms earlier state". c42 also had to splice c41 Trumpet 1 audio over three Leg Slur phrases. c44 found that a full rebuild of the instance brings the normal state back (MANUAL-GAPS Results c44).
- c44 and c45 both followed full rebuilds and are normal.
- c46 was a `--midi-only` build and flipped.

This is the third such render in five. The probe cannot catch it, because its legato check looks at robust SD, not at a shift of the median.

**Fix.**
1. **Before the c47 main render:** fully rebuild the Trumpet 1 and Horn 3 instances, as c47 already does for the five string tracks:
   `~/.venvs/claude-composes-reaper/bin/python tools/build_reaper.py build/parts.json jobs "Trumpet 1"`, and the same for "Horn 3".
   Do the same for Horn 1 if any of its Leg Slur data changes.
2. **After the render:** check every Leg Slur target of Trumpet 1, Horns 1-4 and Horn 3 against c45. Use `pcx.legato_joins` and `attack_pcx`, plus the level over the target's first 0.3 s. Pass:
   - median pcX within ±20 ms of c45 (Trumpet 1 -10 ms);
   - median level change within ±1.5 dB where the data did not change.
3. **If it flips anyway:** splice the c45 Trumpet 1 audio over qn 272-288 and 448-464, where the data is identical. Use the method of `cycles/c46/actor_scripts/splice46.py` or `cycles/c42/actor_scripts/splice42.py`, with 30 ms crossfades. That repairs level and timing.
   - A per-note level restore (`cycles/c43/actor_scripts/statefix43.py`) fixes only the level; the notes stay 65 ms early.
4. **Tools, optional:** a `probe.json` "legato_median" entry, e.g. [["Trumpet 1", -10, 25]], with `probe_attacks.py` failing when a track's median legato pcX leaves that range. Then the next flip shows up in the probe.

**Target.** Trumpet 1 minus Violins I at qn 276-283 back to its c45 values (-0.9..-7.4 dB per quarter); Trumpet 1's legato pcX median -10 ± 20 ms.

## 2. The coda cello solo's 687 and 694 sag 6-8 dB right after the change of note. The pitch arrives on time, so they sound late; more lead would not help, but a level fill does (S2, legato; measured and simulated)

**Where.** "Cello solo" (pass 2, Celli KS Master DIV A), bar 172 beat 4 (687: A-flat4 -> G4, from the Leg Port target) and bar 174 (694: C5 -> B4). Both are descending steps on Leg Slur MAX at v70. The line is the most exposed string line of the coda (rel -1.8 / -1.7 dB).

**What is wrong (measured).**
- **pcX** +118 ms (687) and +102 ms (694), the two worst notes of the solo (c46 actor open item). But the crossover is +24 / +82 ms, and the new band reaches its early level at -0.036 / +0.006 s.
- **The cause is a hole after the transition.**
  - 687: the stem's 40 ms frames read -41.7 / -38.0 / -41.7 / -38.5 / -38.4 / -37.6 dB at +0.04..+0.24 s, against bodies of -33.9 before and -32.0 after: a dip of 8.2 dB (7.5 on 100 ms windows).
  - 694: -41.2..-44.0 dB at +0.04..+0.16 s against -38.0 / -37.3: a dip of 6.0 dB (6.0 on 100 ms windows).
- **Part of 687's hole is the envelope.** The c46 contour crossfades from the A-flat4's cut to the G4's level from 686.85 (-9.6 dB) through 687.05 (-5.5) and 687.225 (+0.7) to 687.35 (+3.3). So the G4's first 0.29 s still carries part of the A-flat4's cut. The rest is the Leg Slur descending-step sag.
- **694:** the c46 fill (693.93-694.07, +3 dB) sits before the hole, which is at 694.02-694.30.
- **More lead made 687 worse** (c46 CHANGES). Lead 0.155 -> 0.22 s moved the crossover +93 -> +24 ms but pcX +89 -> +118 ms.

**Fix** (`build/score_config.py`, append to `ALIAS_TRACKS["Cello solo"]["tables"]["LEVEL_SHAPES"]`; additive to the existing rows; level only, so stem-fixable):
- 687: `[(686.99, 0.0), (687.03, 6.0), (687.16, 6.0), (687.29, 4.0), (687.36, 0.0)]`
- 694: `[(693.985, 0.0), (694.025, 5.0), (694.15, 5.0), (694.26, 2.5), (694.33, 0.0)]`

Simulated on the c46 stem:

| Join | Dip (dB) | Peak over the louder body (dB) | pcX (ms) |
|---|---|---|---|
| 687 | 8.2 -> 2.2 | +0.1 -> +1.8 | +118 -> +2 |
| 694 | 6.0 -> 2.1 | -1.4 -> +1.2 | +102 -> +18 |

The master over the same frames rises by 3-4 dB. Leave the leads and the contour as they are. 688 dips 3.5 dB on 100 ms windows: leave it.

**Optional, same pattern, smaller** (`LEVEL_SHAPES`, simulated):
- **Bassoon 1 135** (bar 34 solo, G3 -> F3, rel -1.0): -40..-42.3 dB at -0.06..+0.14 s against -36.8 / -36.0. `[(134.84, 0), (134.90, 4.5), (135.30, 4.5), (135.42, 0)]` brings it to -36.2..-37.9.
- **Clarinet 1 700** (coda espr., E-flat4 -> C5, rel -1.9): sags to -45.7 / -47.8 dB at +0.21 / +0.29 s under a -39.5 body. `[(700.14, 0), (700.20, 5), (700.40, 5), (700.50, 0)]` brings it to -40.7 / -42.8.

**Target.** Every solo join's dip at most 3.5 dB on 100 ms windows and no peak over +2 dB; 687 / 694 pcX within ±40 ms of +15.

## 3. Two exposed accents sit under their own lifted pickup: the pickup is as loud as or louder than the accented note, and the accent's "front" is the tail of the pickup's lift (articulation; measured and simulated)

**Where.**
- **Violins I, bar 35** (136.5 downbow eighth G4, mf -> 137 accented dotted quarter D-flat5). This is the answer to the bassoon solo; rel -1.2 / -4.1 dB.
- **Clarinet 1, bar 127** (504.5 -> the accented 505, the theme over the crescendo pedal; rel -0.7).

**What is wrong (measured).**
- **Violins I.** `PICKUP_LIFT["Violins I"][136.5]` is 12 dB, the cap: c17 set it when the pickup sat 11-12 dB under its target.
  - Now the pickup plays at -30.5..-31.2 dB (136.75-137.0). The accented note plays -29.4 for 0.06 s, then -36.0..-39.9 dB through 137.25-137.75. So the accented note's body is 5-9 dB under the unaccented pickup.
  - The envelope shows why: +12 dB from 136.143, still +11.1 at 137.0 and +10.5 at 137.063 (`PICKUP_LIFT_TAIL_S` string hold 0.06 s), then +4.5 at 137.147. The 0.06 s "accent front" is the pickup's lift, and the accent's 2-5 kHz front minus body reads +7.0 dB.
  - c44 and c45 measure the same, so this is not new in c46.
- **Clarinet 1.** The lift is 9.5 dB (`PICKUP_LIFT["Clarinet 1"]` 504.5).
  - The pickup plays -33.3..-35.4 dB, the accented 505 -33.2..-34.5. The envelope goes +16.9 (pickup) -> +15.5 at 505.0 -> +8.7 at 505.147.
  - The accented note is no louder than its pickup.
- **No other lifted pickup does this.** I checked every PICKUP_LIFT entry against its target's body (+0.15..+0.5 s). Only Trombone 1 406.5 (+4.0 dB, rel -14) also sits over its target, and it is buried.

**Fix** (`build/score_config.py`; level only, stem-fixable):
- `PICKUP_LIFT["Violins I"].update({136.5: 6.0})`. Simulated:
  - pickup -30.5 -> -36.5 dB;
  - the accent's front -28.5 -> -32.0, then body -36..-40;
  - so the accent stands about 4.5 dB over the pickup, and its 2-5 kHz front minus body falls about 4 dB (to about +3).
  - The pickup is still 4.5 dB under its target's 200 ms peak, the c17 rule.
- `PICKUP_LIFT["Clarinet 1"].update({504.5: 6.5})`. Simulated: pickup -33.9..-35.4 -> -36.9..-38.4 dB against the accented note's -33.2..-34.1.

**Target.** Each accented note's first 0.3 s 2-4 dB over its pickup; 2-5 kHz front minus body at most +3 dB.

## 4. The repeated-note strokes still swell in: the stroke-row test from c46 needs one tools change (S1, S2; measured and read)

**Where.** `STR_REP_NEW_BOW` strokes:
- **Violoncellos:** 47, 156, 448, 456 (bars 12, 40, 113, 115);
- **Violas:** 372 (bar 94).

**What is wrong (measured, c46).**
- **pcX.** The strokes' median improved from +44 to +30 ms. Still late: celli 456 +150 ms, Violas 372 +88. Celli 152 reads -179 because the same pitch sounds before it.
- **Time with the band more than 6 dB under the body:**

  | Stroke | c45 (ms) | c46 (ms) |
  |---|---|---|
  | celli 47 | 92 | 110 |
  | celli 84 | 144 | 96 |
  | celli 88 | 82 | 6 |
  | celli 152 | 220 | 0 |
  | celli 156 | 296 | 200 |
  | celli 448 | 190 | 124 |
  | celli 456 | 316 | 366 |
  | Violas 372 | 162 | 150 |

- **At the beat** the band is still 6.6-12.5 dB under the body (156, 448, 456, 372). `NOTE_TRIM_FROM_MOVED` fixed the envelope part. What is left is the slow mf Sus MAX bow start.
- These strokes are inner and bass voices (rel -7.5..-19.5 dB), so the gain is real but moderate (inferred).

**Why the c46 A/B did not run (read).** In `tools/score_to_parts.py`, the `STR_REP_NEW_BOW` loop (about line 2412, right after the `if cls_ == "soft"` branch) always sets `n["art"] = ks_lookup(stem, "Sus MAX")[0]`. So an `ART_SPANS` row on a stroke is overwritten.

**Fix.**
1. **Tools.** In that loop, keep a span row that is listed as a stroke row:
   ```
   sp_ = n.get("art_span")
   if not (sp_ and sp_["art"] in STR_STROKE_ROWS):
       n["art"] = ks_lookup(stem, "Sus MAX")[0]
   ```
   The rest of the stroke path (`down_stroke`, `rep_stroke`, the gap, the re-tongue lead) stays.
2. **Pass-2 test aliases** (`TEST_TRACKS`, windows from `tw_own`):
   - **"Vc stroke A":** alias "tables" with `ART_SPANS` spans exactly `[q, q + 0.01)` on 47, 84, 88, 152, 156, 448, 456. Spans that cover the next note are what made celli 88's next note continue on the test row in c46. Art "Stac Leg BC + Slur + Port MAX" (Celli key 90; p.99), `vel_by_cc` [(60, 40), (90, 50), (120, 60)]. Add alias "globals" `{"STR_STROKE_ROWS": ("Sus MAX", "Sus Marc LITE", "Stac Leg BC + Slur + Port MAX")}`.
   - **"Vc stroke B":** the same spans on "Sus Marc LITE" with `vel_by_cc` [(60, 25), (90, 35), (120, 45)]. It is already a stroke row and is not a legato row by name.
   - **"Vla stroke A":** Violas 372 (and 80, 500) on the Violas row, key 44.
   - Run `alias_check.py` with only the keyswitch rows and velocities allowed to differ.
   - Check in parts.json that the note after each stroke still gets its Leg BC MAX keyswitch while the stroke sounds. The combination row is a legato row by name (`_lg`), so the c05 keyswitch guard might end the stroke early. If it does, judge variant B only.
3. **Pass criteria** (c46 A's):
   - time under body ≤ 90 ms;
   - front (moved onset..+0.10 s) within -3..+2 dB of the body;
   - 2-5 kHz first 80 ms minus body ≤ -3 dB;
   - stem dip before the stroke ≥ 6 dB;
   - pcX within ±40 ms of the section's legato median (c46: celli +3, violas +20 ms).
   Keep a variant only on the onsets where all pass.

## 5. The final chord and the soft phrase ends stop too fast for a morendo ppp: confirm the planned 500 ms / uncapped pp-p test, on these criteria (releases; measured and read)

**Where.** Every string section's final ppp chord (bars 179-182, qn 712-728, "change bow at will", morendo, attacca). Also the end of the Lento (bar 14, qn 56) and the soft phrase end of bar 146.

**What is wrong (measured).** With the c46 caps (`build/mix.json` `sus_release_cap_ms`: 150 ms mf-ff, 350 ms on the pp / p layers of Sus MAX and Sus Marc LITE), the final note-off falls 10 dB in 0.11-0.17 s and 20 dB in 0.22-0.33 s per section (c46 CHANGES table). The master:
- final chord: 0.12 / 0.33 s (c46 actor); 0.07 / 0.28 s on my measure from the last note-off;
- end of bar 14: 0.16 / 0.28 s.

References (c46 CHANGES):
- Brahms 1/ii 0.40 / 0.79 s and Brahms 4/ii 0.20 / 0.48 s;
- c43 (uncapped, old hall) 0.40 / 0.67 s;
- Movement II's 300 / 400 ms caps gave soft ends 0.21 / 0.34 s.

The patches ship 524-931 ms releases on these layers (read, DIGEST 5.5). The last sound of the movement therefore stops more abruptly than in either reference (inferred: heard as a cut, not a morendo).

**Fix.** The c46 actor's next step, kept narrow:
- **Pass-2 test aliases** of the five sections over qn 704-728 (and 52-56) with the pp / p spec at 500 ms and uncapped (`sus_release_cap_ms` list: keep the 150 ms mf-ff spec unchanged).
- **Pass:**
  - master final release ≥ 0.20 s to -10 dB and ≥ 0.45 s to -20 dB;
  - no stem ending dropping more than 10 dB in its first 0.05 s;
  - the 0.3 s drop after the tutti cut-offs 679 / 288 / 125.9 unchanged (they are mf-ff; Dan's S4 "too wet" stays answered);
  - the final chord's re-bow dips not deeper than now (automatic re-bow dip medians 1.6-2.8 dB; `rebows44.py`).
- Refit the final chord's `rebow_fills.json` lists after the cap change, as the c44 rule asks.

## 6. Smaller items: the Violas 78 swell is a role ramp on the note before; three carry-over timing items re-ranked (measured and simulated)

**a. Violas 78 (bar 20, c46 open item).**
- `build/roles.json` Violas `[77.5, 82.75, 6.5, 0.5]` ramps in over 77.0-77.5, on the last half beat of the F4 half note (76-78). That note also blooms by itself about 7 dB.
- The F4's end reaches -25.1 dB against the A-flat4's body of -32.5 (+7.4). This is the "+9 dB at 77.6-77.66" the actor saw.
- **Fix:** start the row at the A-flat4's moved onset: `[77.75, 82.75, 6.5, 0.1]` (ramp 77.65-77.75; the A-flat4 moves to 77.67).
- **Simulated:** the F4's last 0.35 s goes from -25.1..-28.8 to -30.0..-35.3 dB, and the pre-join peak over the A-flat4 body from +7.4 to +2.8 dB.
- Keep the (77.723, 78.112, -4.9) `JOIN_NOTCH`: without it the transition bursts +6.0 dB (simulated).

**b. Violins I 472.5 / 474.5 (letter G pickups).**
- They speak early. Each new band jumps to its body 0.02 s after the moved onset (-0.16 / -0.15 s), and band arrival against the +0.05..+0.2 s level is -0.020 / -0.046 s.
- **Confirm the actor's plan:** `build/entry_leads.json` Violins I 472.5 0.10 -> 0.05, 474.5 0.09 -> 0.04.

**c. Violins I 88 and 536.**
- These are not late. Band arrival is -0.004 s (88) and +0.022 s (536) against their +0.05..+0.2 s level.
- pcX (+83 / +170) reads a 3-8 dB bloom after +0.2 s.
- Do not add lead. 536 sits at rel -12.4 dB.

**d. Bar 58, the molto cantabile top note (Violins I f62 / Violins II f62 232, tenuto).**
- Both sections arrive late: band arrival +0.056 / +0.037 s (+0.076 / +0.039 against the later body); rel -2.8 / -5.0 dB.
- **Fix:** `build/leg_leads.json` Violins I "232.0": +0.04, Violins II "232.0": +0.02. These are read by the f62 aliases, as 231.5's entries are. Check the `LEAD WARNING` lines: 231.5 is a 0.27 s eighth on the listed cap.

## Standing checks (measured)

**S1, repeated notes** (751 monophonic written repeats, pitch-band dip):

| Family | Repeats | Stem dip (dB) | Master dip (dB) |
|---|---|---|---|
| Strings | 521 | 4.1 | 1.8 |
| Winds | 153 | 6.0 | 2.1 |
| Brass | 77 | 10.2 | 2.7 |

- Exposed repeats (rel > -6) with a master dip under 2 dB: seven. They are Bassoon 1 132, Bassoon 1 stac 352, Violins I 572, Violins II 28.9, celli 21.4 / 528.5 and basses 570. Most are on repetition rows or doubled.
- Bassoon 1 132's broadband dip is 7 dB (-44 -> -51.6); the band measure underestimates it after a short eighth.

**S2, perceived attack** (pcX median / robust SD / share more than 60 ms late):

| Family | Class | Median (ms) | Robust SD (ms) | > 60 ms late |
|---|---|---|---|---|
| Strings | legato | +12 | 50 | 17% |
| Strings | entries | +13 | 28 | 17% |
| Strings | re-attacks | +16 | 52 | 20% |
| Winds | legato | +17 | 31 | 16% |
| Winds | re-attacks | +13 | 31 | 14% |
| Brass | entries | -8 | 24 | 3% |
| Brass | legato | +5 | 37 | 10% |
| Brass | re-attacks | +4 | 30 | 7% |
| Timpani | entries / re-attacks | +16 / +10 | 3 / 22 | |
| Harp | | +1..+4 | 3-16 | |
| Pizzicato (basses) | | +8 | 9 | |

- The probe's legato SD (c46): 51 / 42 / 52 / 50 ms.
- The outliers that matter are findings 1, 2 and 6. The harp outliers (+225..+291 ms on the arpeggios' second notes, bars 47-53) are an estimator artefact: A-flat4 and B-flat4 are the 6th and 8th harmonics of the D-flat2 and B-flat1 bass notes, whose harmonics the measure excludes.

**S3.** The bar-62 sub. p master falls -1.0 / -3.6 / -6.7 / -8.6 / -10.4 / -12.2 / -13.0 dB at 0..0.3 s in 0.05 s steps. That is c42's release shape, so no glitch.

**Item 7, loop pulse.**
- No held span of 6 s or more on one sample flagged (autocorrelation ≥ 0.4).
- Master at 3.95 s, band / centroid: final chord -0.02 / +0.19; Lento bars 1-14 +0.28 / -0.15.
- Bass clarinet 492 (G2, three breath pieces, 7.3 s) reads 0.68 / 0.68, but it is buried (rel -13.1 dB, under the bar-124 fff).
- **Re-bows.** Automatic dip medians 2.8 / 1.6 / 2.1 / 2.2 / 2.4 dB (Violins I / II, violas, celli, basses); printed 2.4-4.8. Steps of 3 dB or more: 1 / 1 / 1 / 2 / 6.

**Item 8, accents.** See the manual table. 2-5 kHz front minus body: brass -11.6 dB median, one over +3. The 18 string accents over +3 dB are all buried (rel ≤ -10), except Violins I 137 (finding 3) and celli 526 (+5.5, rel -3.4, a Sus MAX accent at f).

**Legato joins.**

| Family | Median dip (dB) | Joins with a dip ≥ 6 dB |
|---|---|---|
| Strings | 1.6 | 30 |
| Winds | 2.0 | 36 |
| Brass | 1.2 | 3 |

- On 100-200 ms windows, the exposed wind joins that the 30 ms frames flag (Oboe 1 582, Flute 1 395 / 439, Horn 1 613) dip at most 3.3 dB (vibrato).
- The real exposed holes are in finding 2.

**Tremolo.** Chord changes dip 0.7 / 1.0 / 1.6 dB median (Violins II, Violas, Violins I). The 11 dB dips at 484 are the planned breath before the fff.

**Breath marks.** The printed breaths dip 2.4-15 dB on their stems, except Oboe 2 644, which is buried (rel -15.9).

**Do not touch:**
- `TREM_JOIN` / `TREM_SPLIT`, the pizzicato and staccato rows, `REP_ROW` with the c38 gap rules, and the pass-2 wind staccato windows.
- `GENTLE_ACCENT` and `accent_fits.json` (weight without bite).
- `AUTO_REBOW` with its re-bow fills, `TIMP_RH_ALT`, the timpani strokes and roll settings, and the harp ring and damp.
- The breath gaps.
- The f62 aliases with `SUBITO_SILENT_QN` / `POST_SHAPES_S`.
- `NOTE_TRIM_FROM_MOVED`, `alias_dup` / `tw_own` / `alias_check`, and the c46 notches (Violas 78's included).
- The Cello solo's DIV A patch, v70 and its leads (add only the fills in finding 2).
- The 150 ms mf-ff caps and the hall.
- Every keyswitch rule (no keyswitch late, no chord on a legato row).
