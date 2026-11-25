# Cycle 48, critic A: articulation and phrasing (render c47, score v621)

## Method

All measurements are on the delivered c47 stems and master (`cycles/c47/render`), placed with `build/parts.json`, which describes the delivered stems (coordinator). Where a c47 change sits on a spliced stem I compared with `cycles/c47/render_first` (the main-pass stems, 350 ms pp cap) and with `cycles/c46/render` placed by `cycles/c47/before/parts.json`. Horn 1 is c46's stem.

Measures:
- **pcX** (`tools/pcx.py`): the perceived attack on legato joins, 16 melodic tracks.
- **Pitch-band envelopes** (`pcx.band_env`): stroke swell ("under" = time the note's band stays 6 dB or more under its body), re-bow dips and steps, and old-pitch level after chord changes.
- **Accents**: 2-5 kHz energy in the first 80 ms minus the body, and the level step over the 0.3 s before. 633 printed accents were checked.
- **Accent against the staccatos that follow it**: the accent's first 0.3 s against each staccato's first 0.14 s.
- **S1**: the pitch-band dip at every untied monophonic repeat.
- **Simulations**: stem times a volume shape. The envelope sits after the Opus hall, so these are exact for level-only changes.

Labels: **measured** (render or parts.json), **read** (code, config, patch or manual), **inferred** (reasoned, not tested). The scratch scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c48-A/` and are deleted after the run.

## Manual notes

c48 has no fixed pages (MANUAL-READING.md, second round). I read the pages behind this lens's open problems in full:
- **PDF pp. 91-94** (string long and short articulations), behind findings 1 and 2;
- **p. 99** (legato rules, Legato Slur Staccato, bow-change legato), behind finding 2;
- **p. 222** (release trails carry the room), behind finding 3.

I also read MANUAL-GAPS.md and DIGEST.md sections 5.2-5.5. The MANUAL-GAPS items still open in this lens are unchanged since c47:
- #3 Solo Cello: not installed.
- #5 expressive wind rows: untried.
- #7 half-section divisi: untried.
- #9 horn portato: untried.
- #12 Felt Cresc: untried.
- #13 bass trombone low notes: untried.

None of them is behind a problem measured here.

| Manual (PDF page) | What it says | Where it applies | Does the render follow it? |
|---|---|---|---|
| p.91-92 Marcato Sustain | A marcato sample plus the looped sustain: "extra power at the start of the note" | Accents and repeated-note strokes re-attacked on Sus MAX | **Partly.** Celli 84 / 448 moved to "Sus Marc LITE" in c47; their swell went from 96 / 124 ms to 0 ms (measured). Celli 156 / 456 and Violas 372 are still on Sus MAX and still swell in for 222-364 ms (finding 2). The accents 342 / 354 re-attack on Sus MAX at v105 (finding 1). |
| p.92-94 Short bows: Spiccato (bounced, very short), Staccato, Staccato On Bow, Staccatissimo | Each is a different weight of short note; the KS Masters offer Spiccato RRx9 (off by default) | The fugato's printed staccato eighths (bars 85-96) play Stac RRx9 (Violins I: Staccatissimo RRx9) | **Followed in row choice** (read), but the staccatos play as loud as or louder than the accented subject heads (finding 1). Spiccato is the lighter row the manual offers (inferred). |
| p.94 Repetitions: bow changes inside one sample, with release trails | Same-pitch string repeats | `STR_REP_NEW_BOW` re-attacks on Sus MAX / Sus Marc LITE | **Not used** (read). S1 passes without it (string stem dip median 4.9 dB, master 2.5 dB; measured). |
| p.99 Legato needs no gap; legato rows are monophonic; Legato Slur Staccato gives the first note of a phrase "a slightly stronger attack" | Every legato row | All joins | **Followed** (measured). No chord reaches a legato row: 0 overlaps longer than 0.17 s on a legato note. No keyswitch lands on or after its note. Legato Slur Staccato is untried; c47's variant A (the Stac + BC + Port combination) swelled longer on 4 of 6 strokes, so I do not propose it. |
| p.222 The room is heard as long as the samples play, release trails included | The pp release caps on the strings | **c47 removed the pp cap** on Violins II, violas, celli and basses. In the coda this lengthened the final chord (master -10 / -20 dB at 0.21 / 0.61 s), but it also made the basses' old pitch hang over their pp chord changes (finding 3). |

## 1. In the bars 85-96 fugato, 7 of the 12 accented subject heads that have no printed crescendo after them are no louder than the staccato eighths that follow; the celli's second head (bar 86) is 5 dB under them (measured, simulated)

**Where.**
- Violoncellos bars 85-86 (qn 337, 342: the fugato's first, exposed entry; celli rel 0 dB, so they are the whole master there);
- Violas and the Bassoon 1 stac alias, bars 88-89 (349, 354);
- Violins I, bar 94 (373).

The subject is a pickup eighth, an accented dotted quarter, then staccato eighths, at mf (Vc 336.5, Vla / Bn1 348.5) and f (Violins II, CA and Violins I from 360). I left out 376-381, which sit under the printed crescendo into bar 97.

**What is wrong (measured, c47 stems).** Each line gives the accent's first 0.3 s, the loudest following staccato's first 0.14 s, and the accent minus that staccato:
- Vc 337: -31.9 / -31.8 → **-0.1 dB**.
- Vc 342: -37.9 / -33.0 → **-4.9 dB**. The accent is also 0.8 dB under the slurred eighth before it and 6.0 dB under the phrase's first accent (337).
- Vla 349: -40.8 / -38.1 → **-2.6 dB**.
- Vla 354: -39.2 / -35.2 → **-4.1 dB** (and 1.7 dB under the note before).
- Bassoon 1 stac 349: **-3.4 dB**.
- Violins I 373: **-0.2 dB**.
- Flute 1 stac 373: -3.6 dB; Cor anglais stac 361 / 366: -1.0 / -0.8 dB. Both are buried, at rel -10 / -6..-8.
- Only Violins II 361 / 366 (+3.7 / +2.8 dB) and Bassoon 1 354 (+5.4) put the weight on the accent.

**Why (read).**
- 342 and 354 sit after a slurred pair and are re-attacked on Sus MAX at v105 (`acc_sus`). Their band peak is 7.8 dB under 337's Leg BC head.
- The c27 staccato trims (`LEVEL_SHAPES` celli -2 / -4 dB, violas -2.5 dB) left the Stac RRx9 strokes level with the swell of the accents (`accent_fits.json` 4.5, the cap).
- A player puts the weight on the accented note and lightens the eighths after it. Here the eighths carry it, so the subject's rhythm reads as "short-short-short" with no accent (inferred).

**Fix** (`build/score_config.py`, append these rows to the existing ones; level only, so it can be done by stem fix):
- `LEVEL_SHAPES["Violoncellos"]` +=
  - `[(338.45, 0), (338.48, -2.5), (339.92, -2.5), (339.95, 0)]`
  - `[(341.97, 0), (342.0, 4.5), (343.40, 4.5), (343.44, 0)]`
  - `[(343.44, 0), (343.47, -3.5), (347.6, -3.5), (347.72, 0)]`
- `LEVEL_SHAPES["Violas"]` +=
  - `[(350.38, 0), (350.42, -4.5), (351.65, -4.5), (351.75, 0)]`
  - `[(353.97, 0), (354.0, 3.0), (355.36, 3.0), (355.40, 0)]`
  - `[(355.40, 0), (355.42, -3.0), (355.86, -3.0), (355.88, 0)]`
- `ALIAS_TRACKS["Bassoon 1 stac"]["tables"]["LEVEL_SHAPES"]` (new key, next to its `LEVEL_SHAPES_S`) =
  - `[[(348.97, 0), (349.0, 2.5), (350.36, 2.5), (350.40, 0)], [(350.40, 0), (350.44, -3.0), (351.9, -3.0), (351.95, 0)]]`
- `LEVEL_SHAPES["Violins I"]` += `[(374.38, 0), (374.42, -2.5), (375.9, -2.5), (375.95, 0)]`

Simulated on the c47 stems, accent minus loudest following staccato:

| Head | Now (dB) | After (dB) | Note |
|---|---|---|---|
| Vc 337 | -0.1 | +2.4 | |
| Vc 342 | -4.9 | +2.2 | +3.0 over the note before |
| Vla 349 | -2.6 | +1.4 | |
| Vla 354 | -4.1 | +1.6 | |
| Bn1 stac 349 | -3.4 | +2.0 | |
| Vln I 373 | -0.2 | +2.3 | |

Other effects of the simulation:
- The violas' rel at 354 goes -6.6 → -4.7 dB. No other rel moves by more than 1.4 dB.
- The accents' 2-5 kHz front is unchanged, because a level shape adds weight without bite.

Leave the Cor anglais stac alone: its +2.5 dB c39 shapes match it to the Violins II it doubles, and Violins II's heads are already right.

**Optional pass-2 test (inferred):**
- Celli 342 and Violas 354 on "Sus Marc LITE" at `vel_by_cc` [(60, 25), (90, 35), (120, 45)] with the celli 84 / 448 leads. This is `_STR_B` as an `ART_SPANS` span `[q, q + 0.01)`, and puts the weight in the sample (p.91-92).
- The celli / violas fugato staccatos on "Spiccato RRx9" (p.93; Celli key 35, Violas key on their map), each against the trimmed main stem.
- Keep either one only if the accent minus staccato is at least +2 dB and the 2-5 kHz front minus body is at most -3 dB.

**Target.** Every fugato head outside the crescendo 2-3 dB over its staccatos and at least 1 dB over the note before.

## 2. Three repeated-note strokes still swell in for 220-360 ms. The row that cured celli 84 / 448 in c47 failed on 156 / 456 only because their lead was 40-70 ms longer (S1, S2; measured, read)

**Where.** `STR_REP_NEW_BOW` strokes:
- Violoncellos 156 (bar 40, rel -6.2 dB) and 456 (bar 115, rel -16.2);
- Violas 372 (bar 94, rel -7.7);
- celli 47 (bar 12, rel -11.4), which is still untested.

**What is wrong (measured; under = time 6 dB or more under the body, pcX in ms after the beat).**

| Stroke | Row | Under, c46 → c47 (ms) | pcX, c46 → c47 (ms) | Front − body, c47 (dB) |
|---|---|---|---|---|
| celli 84 | Sus Marc LITE (c47) | 96 → **0** | +0 → -32 | |
| celli 448 | Sus Marc LITE (c47) | 124 → **0** | +52 → -4 | |
| celli 156 | Sus MAX | 200 → 222 | +30 → +32 | -7.9 |
| celli 456 | Sus MAX | 366 → 364 | +150 → +85 | -9.6 |
| Violas 372 | Sus MAX | 150 → 230 | +88 → +33 | -9.1 |
| celli 47 | Sus MAX | 110 → 110 | +52 → +52 | -4.6 |

**Why the c47 test rejected 156 / 456 (read).** score_config's c47 note says variant B played them at pcX -73 ms, "the lead is too long for the row". Their total lead is 0.19 / 0.22 s: `STR_REP_NEW_BOW` `sus_lead_s` 0.10 plus `retongue_leads.json` 0.09 / 0.12. 84 and 448 passed at 0.16 / 0.15 s (extras 0.06 / 0.05). Removing the 70 ms excess puts 156 / 456 on the same leads as 84 / 448.

**Fix.**
- `build/score_config.py`, after the c47 decision line: `ART_SPANS["Violoncellos"] += _spans47([156.0, 456.0], _STR_B)`.
- `build/retongue_leads.json` Violoncellos: `"156.0": 0.09 -> 0.02`, `"456.0": 0.12 -> 0.05`.
- Violas 372: the same row with less lead. Run a pass-2 "Vla stroke B" alias (windows `tw_own("Violas", 368.0, 376.0)`, `ART_SPANS` `_spans47([372.0], _STR_B)`, globals `_STROKE_GL`) with `retongue_leads.json` Violas `"372.0": 0.12 -> 0.04` in the alias tables. Variant A at the old lead sped it to -195 ms in c47.
- **Pass criteria** (c46 A's, as used in c47):
  - under ≤ 90 ms;
  - pcX within ±40 ms of the section's legato median (c47: celli +6, violas +20);
  - 2-5 kHz in the first 80 ms minus body ≤ -3 dB.
- If 156 or 456 fails in the main render, the c47 stems for qn 154-158 / 454-458 are a safe splice back (data elsewhere unchanged).

**Target.** No `STR_REP_NEW_BOW` stroke with rel above -12 dB swells in for more than 90 ms.

## 3. With no pp cap, the basses' old pitch hangs 8-17 dB under its body for 0.35 s after a pp chord change. c48 brings this to bars 5-6, 42-46 and 57-58 (releases; measured in the coda, inferred elsewhere)

**Where.**
- **Double basses, coda** (from qn 695.8, the only no-cap audio in c47): changes at 696, 700, 704, 708 and 710.
- **Bars 1-174** (they get the no-cap releases first in c48). Ten pp Sus MAX changes:
  - 18 and 22 (bars 5-6, Lento);
  - 166, 172, 176, 180 and 182 (bars 42-46, the chromatic bass line under the bassoon solo's close);
  - 224, 228 and 230 (bars 57-58).
  - The basses sit at rel -12..-19 dB there.

**What is wrong (measured).** Old-pitch band at +0.30..+0.40 s after the note-off, relative to that note's body, capped (render_first, 350 ms) → no cap (render):

| Change | Old pitch re its body (dB) | Old pitch re the new note (dB) |
|---|---|---|
| 696 | -20.2 → -13.3 | |
| 700 | -20.1 → -16.8 | |
| 704 | -16.6 → -14.8 | |
| 708 | -20.2 → -16.7 | -12.9 → -9.3 |
| 710 | -18.2 → **-8.3** | |

- Median change +3.5 dB, range +1.8..+9.9.
- **The other sections barely moved in the coda.** Violins II, violas and celli are within 0..2.5 dB; the celli's coda changes are on rows the cap does not touch. So this is the basses' problem: their pp release (shipped 931 ms; DIGEST 5.5) is the longest, and in the bass register a semitone hanging under the next note beats and muddies (inferred).
- Bars 42-46 are a chromatic line (E-flat2-C-sharp2-C2-C-sharp2-E-flat2). The capped render already leaves the old pitch -12.1..-22.6 dB under its body there. Adding the coda's +2..+10 dB would put two of these changes near -10 (inferred).
- **The final chord needs the long release.** The basses carry the largest share of the last 2 s (-4.4 dB re master, against -6.6..-10.5 for the other sections). Their last release went from -10 / -20 dB at 0.08 / 0.23 s to 0.13 / 0.45 s. So a full cap would shorten the morendo again (measured).

**Fix** (`build/mix.json`, Double basses `sus_release_cap_ms`): add `{"ms": 600, "dyn": ["pp"], "rows": ["Sus MAX", "Sus Marc LITE"]}`. This is Movement II's measured pp value. Leave Violins II, violas and celli uncapped. The value is inferred, so check after the c48 render:
- every basses pp change listed above: old pitch at +0.35 s at most -12 dB re its body and at most -12 dB re the new note;
- the basses' final release still at least 0.35 s to -20 dB;
- the master's final chord still at least 0.20 / 0.50 s to -10 / -20 dB.

If the basses then fail the first check, try 450 ms. If the final chord fails the last check, raise the cap. The basses' final-chord re-bows moved little with no cap (|step| median about 1.5 dB, two steps of 1.8 / 2.4 dB, dips at most 2.1 dB; measured), so the cap does not need a re-bow refit.

## 4. The violins' and violas' legato joins have been perceived 15-25 ms late for three renders running (S2; measured, effect inferred)

**Where.** Leg Slur / Leg BC targets of Violins I, Violins II and Violas, the whole piece.

**What is wrong (measured).** pcX median on legato joins:

| Track | c45 (ms) | c46 (ms) | c47 (ms) |
|---|---|---|---|
| Violins I | +24 | +15 | +22 |
| Violins II | +19 | +19 | +25 |
| Violas | +12 | +20 | +20 |
| celli (for comparison) | +6 | +3 | +6 |

- The render-to-render noise per note is about 50 ms robust SD (state_check), but the medians do not move.
- Winds sit at +9..+21 ms and the celli at +6, so the upper strings lag their own celli by about 15 ms.

**Fix** (`build/score_config.py`): `LEG_LEAD_S = dict(LEG_LEAD_S, **{"Violins I": 0.185, "Violins II": 0.215, "Violas": 0.215})`, i.e. +0.015 s on the family leads (score_to_parts defaults: string 0.17, Violins II / Violas 0.20). Check the `LEAD WARNING` lines, because joins behind short notes on a listed cap will absorb part of it.

**Effect.** Shifting the c47 joins by -15 ms moves the medians to +7 / +10 / +5 ms. Joins within ±30 ms go 38 → 44%, 39 → 47% and 39 → 42%; the share more than 60 ms early rises 4-8 points (inferred: the caps may absorb part of it). This is a small, global change. Do it only if findings 1-3 leave the build room.

## 5. Smaller items (measured)

- **Re-bows.** Every automatic re-bow dip with rel above -9 dB is at a printed bow change or under a printed diminuendo:
  - Violins I 44 (bar 12) is a printed down-bow at f: master band dip 4.5 dB.
  - Violins I 48 (bar 13) is a printed down-bow into f > p: step -6.1 dB.
  - Celli 40 and 180 are printed repeats: master band dips 4.8 / 7.3 dB, which S1 wants.
  - Celli 26.52 dips 7.8 dB on its stem but -0.6 dB in the master (covered), with its fill already at the +10 dB cap. Leave it.
  - Medians (c47): automatic dips 2.8 / 2.3 / 3.2 / 1.9 / 1.8 dB (Violins I / II, violas, celli, basses).
- **Accent bite.** 2-5 kHz first 80 ms minus body, medians: brass -17.5 dB, strings -10.1, winds -12.6; 4 of 618 over +3 dB, none exposed. The master's 2-5 kHz jump at accents is -1.1 dB median, so there is no bite. Steps over the note before (medians): brass +5.3, strings +3.0, winds +2.8 dB.
  - Of the 41 string Sus MAX accents with a step under 1.5 dB, the exposed ones are the fugato heads in finding 1.
  - The others (celli 100, 124, 542; basses 88, 536, 676; Violins I 125) are at rel -9.4..-11.8, where the step is inside a tutti.
- **S1.** Untied monophonic repeats, median dip stem / master:

  | Family | Repeats | Stem (dB) | Master (dB) |
  |---|---|---|---|
  | Strings | 306 | 4.9 | 2.5 |
  | Winds | 161 | 5.4 | 3.0 |
  | Brass | 199 | 5.5 | 2.8 |

  - Exposed repeats (rel above -6) with a master dip under 2 dB: four. Bass clarinet 308 is filled by the basses' A-flat1 second harmonic; Violins I 270 is a slur run, Violins II 320 a tremolo, and basses 304 is the fourth. None needs a change.
- **Keyswitches and legato rows.** 0 keyswitches on or just after their note. 0 notes on a legato row overlapped by another pitch for more than 0.17 s. The celli 84 / 448 "Sus Marc LITE" keyswitches arrive 30 ms before their notes, and the row returns to Leg BC / Sus MAX before the next note.
- **State.** `state_check` c46 → c47 lists only Trumpet 1's return to c45 (two runs, -6.6 / -5.6 dB, +41 / +46 ms) and one Violins II timing run (398-404, level -0.3 dB, informational). Horn 1 is c46's stem.
  - **For c48:** after the full rebuild of Horn 1 the coordinator planned, check that Horn 1's Leg Slur targets against c46 are within ±1.5 dB median level and ±20 ms median pcX (c47 joins: Horn 1 +12 ms).

## Do not touch

Keep the following as they are:
- The c47 celli 84 / 448 "Sus Marc LITE" strokes and their leads.
- `GENTLE_ACCENT` and `accent_fits.json` (weight without bite).
- `TREM_JOIN` / `TREM_SPLIT`, the pizzicato rows, `REP_ROW` with its gaps, `STR_REP_NEW_BOW`'s gap rules, and the pass-2 wind staccato windows (add only finding 1's shapes).
- `AUTO_REBOW` with its fills and `REBOW_FILL_END_S`.
- No pp cap on Violins II, violas and celli; the 150 ms mf-ff caps; the hall.
- The Cello solo's DIV A patch, v70, leads and c47 fills.
- The pickup lifts as set in c47 (Violins I 136.5 at 6 dB, Clarinet 1 504.5 at 6.5).
- `TIMP_RH_ALT`, the harp ring and damp, and the breath gaps.
- Every keyswitch rule (none late, no chord on a legato row).
