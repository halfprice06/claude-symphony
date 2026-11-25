# Cycle 46, critic A (articulation and phrasing), on the c45 render

## Sources and method

- **Render and data.** The c45 render (`cycles/c45/render/`, dry stems 01-32 plus `00_Master.wav`) and `build/parts.json`, which equals `cycles/c45/delivered_build/parts.json`.
- **Focus.** ONE_TIME c46 asks this lens to measure what the new tempo map will need: legato overlaps, lead times and phrase ends under the slower breaths. So most of this report simulates the map before it is built.
  - I copied `build/` and `tools/` to scratch and confirmed that `score_to_parts.py` reproduces c45's parts.json byte for byte.
  - I then ran critic C's c44 plan (finding 1: depths, arcs, `CAESURA`, `BEAT_STRETCH`, `APEX_LEAD[116]`). This needed C's tool change (a): `PHRASE_*` and `APEX_AGOGIC` read through `globals().get`.
  - Finally I ran a revised plan with my fixes 1-2 (called "plan A" below).
  - Every gap, overlap, lead and tempo below is in seconds on each map's real tempo, caesuras included.
- **Carry-overs.** The c45 carry-overs in my area were measured on the c45 stems: `tools/pcx.py` for the Oboe 1 joins, 30 ms RMS envelopes, and own-band levels by FFT masking.
- **Scratch.** `/private/tmp/claude-501/mockup-loop/mvt2-c46-A/`, deleted at the end.

## Manual notes (MANUAL-READING c46 / A: group A3, May 2021 HO manual PDF pp. 75-81, Hollywood Solo Violin, read in full; MANUAL-GAPS.md read)

| Manual (PDF page) | Where in this mockup | Does the render follow it? |
|---|---|---|
| p.75: the Solo Violin library links dynamics and vibrato on CC1 (HO sections keep them separate). Its Legato Sustain combines legato and sustain in one sample layer, for continuity. | Violin I solo, bars 17-22 (qn 48-65), played by `1st Violins KS Master DIV A` (half section). | Partly. The solo's CC1 is held at 72 (c32: Sus Vib, avoiding the louder Molto Vib set), so its vibrato never grows with the line. The Solo Violin is not installed (MANUAL-GAPS #3, checked). |
| p.75-78: "Long Solo" patches (Flautando, Grand Détaché RR x2, Lyrical Mute, Lyrical Vibrato, Sus Expressive, Sus NV/VB) are monophonic. Overlapping notes are blended without strong attacks; a non-overlapping note re-attacks. | The same rule as the HO KS Masters: a note that does not overlap plays a fresh attack. | Yes, for the solo (all 11 notes on Leg Slur MAX with 45 ms overlaps). Fix 3 uses this rule: a lift made with CC11 keeps the overlap, so no re-attack is triggered. |
| p.79: Leg Bow Change: overlapping notes give an expressive bow change that accents the second note. Velocity sets the transition timing (tighter or looser). Non-legato notes play Détaché RR x2. | Violins I/II Leg BC MAX at phrase seams (77, 188, 196, 249, 259 ...). | Yes. Finding 3 shows the bow change is the only sign of a breath at the new caesuras. |
| p.80: Leg Exp Vib and Leg Lyr Vib are "best suited for slower tempos". Leg Slur "shines at slow to medium tempos". All of these: velocity sets transition timing. | The dolce solo; the slower phrase ends of the new map. | The solo's targets play v72-80 (c32 A #5). That is the slow-transition end, which fits the slower map. |
| p.81: LegSus: CC1 picks the dynamic layer from its initial value and does not crossfade. | A Solo Violin track would need CC1 written before each note, not as a swell. | n/a (not installed). |
| What a Solo Violin track would need (inferred) | qn 48-65 | `Leg Lyr Vib` or `Leg Exp Vib` (slow-tempo legato). CC1 from the printed dynamic (dolce p, about 45-70) and CC11 for shaping, with velocity 50-70. Close plus Mid mics in a separate pass, with the same tempo map, hall and send. The DIV A track can borrow the CC1 link today: let CC1 follow the solo's CC11 within 68-78 (Molto Vib only 0.15 at 72, 0.43 at 80), refitting the solo's level by stem fix. This is optional and outside this cycle's task. |

## Findings, ranked by what a listener would hear

### 1. The new short caesuras shorten printed wind breaths: Horn 1's f breath at 196 drops from 137 to 52 ms (measured in simulation)

**Where.**
- qn 196: Horn 1 and bass clarinet (printed breaths).
- qn 259: Bassoon 1 (printed breath).
- qn 265: Bassoon 1 and Horns 1-2 a2 (printed breaths).

**What is wrong.**
- In `score_to_parts.py`'s breath branch (line about 2448), a loud wind or brass note ends 0.3 qn before a printed breath. Where a `CAESURA` also exists, it ends only `CAESURA_BREATH_QN` (0.12 qn) before it (c19, written for 204 and 268).
- C's plan adds short caesuras at 196 (0.08 s), 259 (0.10 s) and 265 (0.12 s). So the gap switches to 0.12 qn, and the next note's entry lead (up to 0.10 s) then eats most of it.
- Silence between the notes, c45 -> plan:

| qn | track | c45 | plan |
|---|---|---|---|
| 196 | Horn 1 | 137 ms | 52 ms |
| 196 | bass clarinet | 284 ms | 152 ms |
| 259 | Bassoon 1 | 338 ms | 183 ms |
| 265 | Bassoon 1 | 374 ms | 207 ms |
| 265 | Horns 1-2 a2 | 374 ms | 207 ms |

- c13 measured Horn 1's 196 breath as inaudible at 0.2 qn; the plan undoes c13's fix there.
- Every other printed breath gets longer under the plan:
  - Horn 1 and bass clarinet at 29: 420 -> 563 ms;
  - Horn 1 at 188: 244 -> 364 ms;
  - cor anglais at 164: 299 -> 376 ms;
  - Clarinet 1 at 286: 414 -> 543 ms;
  - bass clarinet and Bassoon 1 at 102: 231/288 -> 351/438 ms.

**Fix (`tools/score_to_parts.py`, generic, default off).**
- Change the line to `gap_ = max(CAESURA_BREATH_QN, lead_qn(e0, CAESURA_BREATH_S)) if <caesura> and e0 not in CAESURA_BREATH_SKIP else 0.3`.
- Movement II values in `build/score_config.py`: `CAESURA_BREATH_S = 0.24`, `CAESURA_BREATH_SKIP = {204.0, 268.0}`. The skip keeps c19's tuned climax breaths, which would otherwise widen from 136 to 200 ms.
- Simulated result:
  - Horn 1 196: 140 ms;
  - bass clarinet 196: 240 ms;
  - Bassoon 1 259 and 265: 240 ms;
  - Horns a2 265: 240 ms.
- Target after the render: every printed wind breath has 0.14 s or more of silence in the stem, and the master shows a dip of 3 dB or more in the breathing instrument's band.

### 2. Caesura 66 and arc (60, 66) fall inside the violins' slurred pickup: the pickup beat runs 25 % slow, and the breath stalls between the F and the A flat (measured in simulation)

**Where.** Violins I/II, qn 65-66 (bar 22.3 into bar 23). The tutti violins enter on the pickup E flat-F at 65 ("gli altri con sord., espr., sul D"), slurred 65-67.5. The solo's phrase ends on its E flat 5 at 63-65.

**What is wrong.**
- This is the trap C fixed at 29, 77, 139, 237 and 249, but C's plan keeps it here.
- The arc's last beat (x0.80) and the BEAT_STRETCH 66 entry land on the pickup. Beat tempi:
  - c45: 64 = 49.4 bpm, 65 = 42.5, 66 = 50.4;
  - plan: 64 = 47.3, 65 = **36.5**, 66 = 48.9.
- `CAESURA[66]` (0.20 s in the plan) slows 65.75-66, which lies inside the slur. The violins hold the F and join the A flat with a 90 ms Leg Slur overlap, so the breath sounds as a stall in mid-slur.
- Two of the plan's "same-pitch restarts" are ties in v600: bass clarinet and cor anglais at 96 (E flat 93 tied to 96, inside the solo slur 91-101), and Horn 1 at 235 (tied from 232). At 96 the 0.15 s caesura therefore only stretches a tied note, and no breath is heard (read in `mockup-events.tsv` and parts.json).

**Fix (`build/score_config.py`, the c46 tempo block).**
- `PHRASE_ARCS`: replace `(60, 66, "main")` and `(66, 77)` with `(60, 65, "main")` and `(65, 77)`.
- `CAESURA`: drop 66, add `65.0: 0.20`; drop `BEAT_STRETCH[66]`.
- Simulated (plan A):
  - beat 64 (the solo's held E flat 5) 36.5 bpm, the phrase-end broadening;
  - pickup beat 65 at 51.0 bpm;
  - beat 66 at 53.6 bpm;
  - total length 353.16 s (c45 348.11 s, C's plan 353.21 s).
- Either drop `CAESURA[96]` or relabel it as an agogic hold on the crest (the BCl/CA crest already has `BEAT_STRETCH` 97).

### 3. The strings play legato straight through the new breaths: the theme pickups at 65, 77 and 249 get a connected bow change, with no lift (measured state; the effect of the fix is inferred)

**Where.** Violins I and II at 77 and 249 (the E flat-F pickups into bars 27 and 75, lead line); Violins II at 65 (plan A).

**What is wrong.**
- A caesura slows the 0.25 qn before the beat. A string note held into it simply gets longer and still joins its target.
- At 77 and 249 the slur ends on the held G (75-77, 247-249) and the pickup starts a new slur, so the pipeline plays a Leg BC MAX join. The overlap grows from 48 to 79 ms in the slowed span; at 65 (Vln II) it is 90 ms.
- The held note's CC11 drifts only 61 -> 56 (77) and 52 -> 44 (249) into the join. So the breath C wants ("a player breathes before the pickup") is heard only as a later pickup. No string lift is heard.
- No string join changes between overlap and gap anywhere under the plan, so there is no lift at any caesura (count 0).

**Fix (`tools/score_to_parts.py` plus `build/score_config.py`).**
- New table `CAESURA_LIFT = {"Violins I": {77.0: 9, 249.0: 9}, "Violins II": {65.0: 8, 77.0: 9, 249.0: 9}}`: a CC11 fall of N units over the last 0.25 s before the target's moved onset, appended to `cc_falls`. The target's own CC11 and the +6 dB early fill restore the level.
- Keep the overlap. The join stays a bow change (manual p.79), so the legato leads and the S2 probe are unaffected. CC11 acts before the hall, so the room keeps ringing (S3).
- Do not use a real gap. It would switch these targets to the KS Master's non-legato attack, which needs the entry leads instead.
- Target: a 2-4 dB dip in the master's violin band (harmonics 1-4) just before 77 and 249, with no change to the pickup's pcX.

### 4. What else the new map moves: four transition notches and 20 re-bow fills come loose; leads, overlaps and rows stay correct (measured in simulation)

**Leads.** Leads are converted in seconds on the real map (`qn_before`). Of all notes on all 32 tracks, only one lead changes by more than 15 ms: Violas 249.5, 282 -> 250 ms, capped by the previous note's end. No lead table needs a refit for the tempo change.

**Legato overlaps.**
- Median 45 ms, as in c45. The 0.04 qn `LEG_OVERLAP` grows only inside the slowed caesura spans: 48 -> 79 ms at 77 and 249 (Vln I/II Leg BC, Vc and Violas Leg Slur), and 90 ms at Vln II 65 in plan A.
- That is still inside the references' range (The Crown 31, Atonement 94, Duc 181 ms). Keep `LEG_OVERLAP` at 0.04 qn.

**Rows and keyswitches.** No articulation changes on any note, apart from the automatic re-bows.

**Qn-placed notches (`JOIN_NOTCH`, written in qn at measured transition peaks).** Four are now off by more than half their window:

| track | current window | lands off by | plan-A window |
|---|---|---|---|
| Violins I | 258.85-258.93 | -60 ms | 258.889-258.948 |
| Violins II | 258.81-258.98 | partly | 258.860-258.985 |
| Flute 1 | 258.86-258.93 | +44 ms | 258.897-258.948 |
| Violoncellos | 76.82-76.98 | -139 ms | 76.890-76.988 |

- All other `JOIN_NOTCH` rows are within ±17 ms.
- Recompute these windows in the final map by the same method: keep each window's offset in seconds from its target's moved onset.
- Better, generically: a `JOIN_NOTCH_S` keyed by score onset, like `LEVEL_SHAPES_S`.

**Re-bows.**
- 20 `REBOW_FILLS` keys come loose because the `AUTO_REBOW` points move. Per track: Violins I 1, Violins II 2, Violas 2, celli 2, basses 7, Violoncellos div 5, Violas div 1.
- The basses' 164-172 note gains a new re-bow at 166.04, because the note is now longer.
- Run `space_rebows.py` and then `fit_rebows.py` (relevel41) on the final map, as C's trap 1 says. Do not freeze the c45 points: the basses' 164-170 segment would then exceed 4.5 s.

**Phrase shapes.**
- `PHRASE_SHAPE` finds phrases with a gap rule in seconds (gaps under 0.15 s). It keeps all 33 lyrical phrases and their classes under plan A.
- The only splits are the 188-212 runs, which break at 204 into skip:hairpin and skip:span. Flute 1's 108-124 changes from skip:hairpin to skip:long. No new arcs appear.

**Held notes over 6 s (loop check, BRIEF 8).**

| note | c45 | plan |
|---|---|---|
| Horn 1 232 | 7.34 s | 7.63 s |
| Contrabassoon 87 | 12.63 s | 12.97 s |
| Contrabassoon 98 | 10.88 s | 11.08 s |
| Bassoon 2 90 | 11.53 s | 11.69 s |
| timpani roll 226 | 13.51 s | 13.89 s |
| Oboe 2 262 | 6.00 s | 6.12 s |
| harp 39 | 5.8 s | 6.1 s |

- On the c45 stems, folded pulse depth: Bassoon 2 90 2.9 dB at 4.1 s, contrabassoon 1.9-2.2 dB at 4.75 s, timpani 226 3.0 dB at 3.95 s (autocorrelation +0.39). Each covers only 2-3 periods, so the evidence is weak.
- These are pp inner pedals. Listen-check them after the render; no data change now.

**Hairpin curves (ONE_TIME, plan section 8).** `LEG_VEL_BY_CC` moves about 0.2 velocity per CC unit, so a curve that shifts mid-hairpin CC11 by 10 changes legato-target velocity by about 2. That is negligible for slur speed. Keep the timpani lanes linear, as ONE_TIME says.

### 5. Trombone 1's qn 213 accent: the role ramp lifts the pickup into it, so the accent is only 1.5 dB over the end of its pickup (measured)

**Where.** Trombone 1, qn 212.5-213.6 (bar 63, the quotation's head). The climax is unchanged by the tempo plan.

**What.**
- `roles.json` [212.4, 213.6, +3] ramps the volume envelope 0.4 -> 3.0 dB over 212.0-212.4, under the 212.5 pickup.
- Stem levels:
  - pickup: -31.4 dB in its first 0.3 s, then -29.6 over 0.3-0.8 s (it swells into the accent);
  - 213: -28.1 dB in its first 0.3 s.
- So the accent is 1.5 dB over the pickup's end (3.3 over its start). Rule 4 asks for 2-4 dB of weight.
- 213's moved onset is 212.91 (a 0.09 qn lead).

**Fix.**
- `build/roles.json` Trombone 1: [212.4, 213.6, 3] -> **[212.88, 213.6, 3, 0.03]**. The role then starts with 213's moved onset, and the pickup plays at 0 dB.
- Expected: pickup about -3 dB, accent about 4.5 dB over the pickup body.
- Keep the Sus MAX swell, the CC7 110/85 points and v112.
- Rebuild Trombone 1 with `--midi-only`; ONE_TIME notes the saved project lacks its role.

### 6. Oboe 1's legato arrivals: +46 ms, all from its rising joins (+69 ms); crossovers on time (measured)

**What (`pcx.py`, c45 stems).** Joins: Oboe 1 +46 ms median (robust SD 73, n=32), Violin I solo +6, Violins I +17, Horn 1 -14.
- Oboe 1 rising joins: median +69 ms (n=14). Falling: +25 ms (n=18).
- Crossover median +6 ms (on time).
- Late rising joins (pcX / lead):

| qn | 43.5 | 55 | 140 | 142 | 146 | 189 | 197.5 | 200 |
|---|---|---|---|---|---|---|---|---|
| pcX | +97 | +94 | +157 | +88 | +131 | +166 | +61 | +76 |
| lead | 0.06 | 0.06 | 0.06 | 0.06 | 0.11 | 0.06 | 0.06 | 0.12 |

- The new level arrives slowly after an on-time transition on upward slurs.

**Fix.**
- `build/leg_leads.json` Oboe 1: +0.04 s on 43.5, 55, 140, 142, 189 and 197.5; +0.02 on 146. Leave 200, already at 0.12.
- Target: Oboe 1 median within ±30 ms, rising joins under +60, falling joins unchanged. Leads are in seconds, so the new tempo map does not affect this.

**Smaller carry-overs (measured).**
- **Violas 87** (now a down-bow stroke): stem dip 4.0 dB, own band 4.3, master 1.2 dB (master band 0.1). Violins and celli hold over it. This inner-voice repeat will not reach 3 dB in the master without a hole in the stem; leave it.
- **Violas' portato, bars 48-51.** Every peak now falls by +0.22 s (c44: +0.31). Levels are -50.5 (152.5, 154.5, 157.5, 161.5) and -52.4 dB (153.5, 156.5, 160.5): a 2 dB step that alternates with the round-robin take. This meets c45's 1-3 dB spread target, so no change.
- **CC16 repeatability.** Not testable this cycle: c46 changes every track's timing. Test it on the first later render that leaves some tracks' data unchanged.

## Do not touch

- The 0.04 qn legato overlap.
- All entry and legato leads (they follow the new map in seconds).
- Trombone 1's Sus MAX accent swells, CC7 points and brass CC1 at most 108.
- The violas' portato velocities and leads.
- The Violin I solo's v72-80 legato targets and CC1 72.
- c19's 0.12 qn breaths at 204 and 268.
- The CC15 mute placement.
- The basses' coda and final-chord re-bow points: refit their fills, do not move them.
