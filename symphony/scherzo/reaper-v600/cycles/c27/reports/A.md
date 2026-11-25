# Cycle 27, critic A: articulation and phrasing (on the c26 render)

Material: `cycles/c26/render` stems, `cycles/c26/build_render/parts.json` (the data as rendered), `cycles/c26/records/`; `cycles/c18/render` and its parts.json as the older comparison (allow -3 dB for the c26 global gain; every number below is relative inside one render unless it says otherwise). Patch data read with `mockup-kit/opus/opus_state.load_oib`. Tools run read-only: `cycles/c26/actor_scripts/spic26.py`. My own scripts: per-pitch bands (harmonics 2-5, ±0.3 semitone, 2048-point STFT, 5 ms hop), 5 ms power envelopes, 2-5 kHz band envelopes. "Measured" means a number from the render, parts.json or a patch file; "inferred" means reasoned from those numbers.

## Manual notes

`MANUAL-READING.md` has no row for c27. I read group A4 (PDF pages 108-113 of the May 2021 HO manual, Hollywood Orchestral Woodwinds) in full, because c26's main change was the woodwinds' share of Dan's figure and two of this cycle's open accent items are woodwinds. I also used `MANUAL-GAPS.md`.

| page | what it says | where it applies here | does the render follow it |
|---|---|---|---|
| 108 | Flute 2 is a different player; no samples are shared with Flute, so a unison does not collapse | Flute 1 / Flute 2 doubling the theme in both tuttis | followed (separate tracks and patches) |
| 109 | Sus Expressive: slower attack, gradually increasing vibrato | the second idea "espress." lines (bars 45-56, 121-140, 277-288) | not used (Leg Slur MAX / Sus MAX); not measured this cycle, a candidate for a later A cycle |
| 109-110 | Legato Repetitions RRx4: a sustained note plus a short re-tongued attack for repeats inside a legato phrase | the clarinets play every slurred line on "Leg Slur Rep" (p.112's variant) | followed for repeats; but Clarinet 2's detached accented half notes are first notes on that legato row and get no accent shaping (finding 2) |
| 110 | Shorts have no release trails: hold short notes long enough to hear the room; Staccatissimo is shorter than Staccato | the woodwinds' "Stac DblTng RRx9" theme heads | followed: Oboe 1 / Flute 1 staccato quarters ring 234-246 ms to -20 dB, the same as the strings' Violins II / violas rows |
| 110 | Marcato: short notes with a strong accent (Marc DblTng RRx4) | none of the scherzo's wind accents are short | correctly not used |
| 112 | Legato slur only with no gap and within an octave; monophonic unless CC22 < 64 | the slurred eighth pairs before the tutti staccatos; c26's 35 ms slur end now sits after the pair, not inside it | followed: the pair's own join is unchanged (eighth 2 minus eighth 1 within 0.6 dB of c18, below) |
| 112 | Legato Slur Repetitions: re-tongued samples for same-pitch notes inside a slur | Clarinet 1 / 2 | in use |
| MANUAL-GAPS #5 | woodwind staccato rows | the winds' theme heads play "Stac DblTng RRx9" | in use; the c26 slur-end change works (first check below) |

## First check: Dan's figure at every occurrence, with the woodwinds

- Strings (the actor's pitch-resolved `records/fig25.txt`, c25 -> c26): Violins I bar 23 18.0 / 4.3 / 8.9 / 9.4 -> 18.1 / 4.4 / 8.3 / 9.1; bars 115 / 263 / 315 within 0.6 dB; Violins II within 0.1 dB except bar 315 B -> C 17.3 -> 14.3. Nothing is more than 2 dB worse except that one Violins II value, and 14.3 dB is still a clean change of note (the low values in this table are 4-5 dB). Not a defect (measured).
- Woodwinds, the slurred eighth pair before each staccato quarter in 312-360 / 912-960 (my measure, c18 -> c26; c25's stems are deleted). The question was whether c26's slur end 35 ms early, 120 ms cap and -6 dB f trails have clipped or thinned the eighths:

| track (pairs) | eighth 2 minus eighth 1 (band peaks) | eighth 2 to -20 dB | broadband trough eighth -> staccato |
|---|---|---|---|
| Flute 1 (6) | +2.5 -> +3.0 dB | 276 -> 193 ms | 3.4 -> 6.6 dB |
| Flute 2 (6) | -3.4 -> -3.4 | 304 -> 216 | 6.6 -> 10.0 |
| Oboe 1 (10) | +4.3 -> +3.7 | 273 -> 216 | 3.6 -> 5.2 |
| Clarinet 2 (10) | +0.2 -> +0.2 | 313 -> 213 | 2.9 -> 4.8 |

  The eighths keep their level against the first eighth of the pair (within 0.6 dB median). What was removed is 60-100 ms of ringing tail, and the trough before the staccato deepened 1.6-3.4 dB. The 5 dB "peak loss" at Flute 1 318 / Flute 2 344 was that tail (fig26w's slur_peak window runs 60 ms into the staccato). The one thin eighth, Flute 2's F sharp 5 at 347.5 / 947.5 (-12.1 / -10.1 dB under the B5 before it), was -12.2 / -6.6 in c18 too: it is the flute's low F sharp after a leap, not a c26 effect (measured). Keep the c26 woodwind state.

## Findings, ranked by what a listener hears

### 1. The theme's own accented half note (Violins I, the nine p / mp statements) is a bright marcato spike followed by a 7-13 dB hole, so the slur from the half note into its two eighths is not heard (measured)

Where: Violins I, the soft theme heads on "Sus Marc LITE" (`_MARC_HEADS`): qn 39, 51, 69, 75 (bars 14, 18, 24, 26), 285 (bar 96), 759, 771, 789, 795 (bars 254, 258, 264, 266), with their slurred eighths at q+2 / q+2.5 and the landing staccato at q+3. Score: accented half note under one slur with the two eighths and the landing quarter (bar 14: accent at 39, slur 39-42, p leggiero). This is the first thing the theme does, in its most exposed statements.

Evidence (c26 Violins I stem; median over the nine heads, relative to the staccato quarter before each head):

| time after the head's beat | -0.2 s (staccato) | +0.03 to +0.15 s (head) | +0.21 to +0.39 s | +0.46 / +0.57 s (eighths) |
|---|---|---|---|---|
| broadband | 0 | -2..+2 dB | **-7..-13 dB** | -2 / -2 |
| 2-5 kHz | 0 | **+4..+6 dB** | -3..-9 | +1 / +3 |

- The same profile on the twelve tutti heads on Sus MAX (123 ... 951): broadband -1..-5 through the half note (no hole), 2-5 kHz 0..-2 (no bite).
- Pitch-resolved: the head's band peaks 0.04-0.16 s after the beat (median +0.15 s, at 160 ms lead) and is 16.3 dB under the staccato's peak 0.35 s after the beat (Sus MAX tutti heads: -4.8 dB). By the end of the written half note the head's band is 24-31 dB under its peak.
- Against all unaccented notes within ±2 qn: first 100 ms +5.2 dB median (six of nine over +3; 69 +9.3, 771 +7.4, 51 +6.5); 2-5 kHz first 80 ms +8.6 dB over the neighbours' fronts. This is the one accent family over Dan's +3 limit, and the one with bite ("weight, not bite").
- Cause (patch, measured with load_oib): the Marc LITE row is two sets of groups, the sustain "1V pp / mf / f / ff" (velocity 1-127, CC11 crossfade) and the marcato overlay "V1 Marc Shrt rrx1 / rrx2" (velocity layers 1-65 / 66-108 / 109-127). At the heads' CC11 (44-80, median 56) the sustain sits 16+ dB under the mp marcato. Since c15 the per-head level rows (`_MARC_FIX`, c14's lift "u" of the half note's second beat) no longer reach the envelope, and under Dan's rule they must not come back there. The two eighths play the same row at v78-94, so each slurred eighth starts with the *f* marcato attack (2-5 kHz +1..+3 dB over the staccato).
- c18 had the same shape (hole and peak timing within a few dB; its 2-5 kHz front over the neighbours' fronts was +11.1 dB), so this is not a c26 regression. It has stood since the level rows were dropped (inferred from the config history).

Fix, inside Opus and CC11 only:
- a) `build/mix.json` "Violins I" `region_gain_db`: the existing `{"row_dyn_db": {"Sus Marc LITE": {"vel<66": -4.0}}}` -> **-8.0**. Only the nine heads are under v66 on that row (measured: the eighths are v78-94, the hemiola strokes v74-88, the summit v112), and only the marcato regions have velMax under 66 (the sustain groups span 1-127). This lowers the spike and the bite by 4 dB and leaves the sustain alone.
- b) A CC11 lift after the marcato, as a generic rule in `tools/score_to_parts.py` `_acc_cc_build`. New ACCENT_CC key `"marc_lift": {"cc": 14, "s": (0.10, 0.22), "rows": ("Sus Marc LITE",), "vel_max": 65}`. On an accented note on a listed row under vel_max, CC11 rises by cc units from score onset + s[0] to full at score onset + s[1]. It holds to the next moved note-on minus 0.02 qn and is back at the resting value at that note-on. Set it in `build/score_config.py` for "Violins I".
  - This is the c14 lift moved from the envelope into CC11, before the hall.
  - The rise is placed after the marcato's peak (+0.04..+0.16 s). With Opus's ~120 ms CC11 smoothing it fills the +0.21..+0.39 s hole.
  - At CC11 44-80 a unit is about 0.4-0.5 dB, so 14 units is about +6 dB.
- c) Optional, in the same range test: the eighths after the nine heads at v62 (`VEL_SET["Violins I"]` at q+2, q+2.5), so that they take the mp marcato layer and the same cut. c14 measured that on this row velocity selects the layer, not the level.
- Range test (36-90 and 756-800 against a same-start control; variants a+b with cc 14 and 20, and a+b+c). Acceptance:
  - the head's band at +0.35 s within 8 dB of the staccato before it (now -16.3);
  - first 100 ms over the ±2 qn neighbours +1..+3 dB (now +5.2);
  - 2-5 kHz front over the neighbours' fronts +3 dB or less (now +8.6);
  - head peak no later than +0.10 s after the beat (now +0.15);
  - broadband trough between the head and the first eighth 4 dB or less (now 7-13);
  - bar 23 figure (fig25, the head at 69 precedes it) within 2 dB of c26.

### 2. Clarinet 2's tutti accents get no shaping at all: CC11 is flat at 104 under every one, so c26's accent fix never reached it; they sit 1.6 dB under their neighbours and peak 0.31 s after the beat (measured)

Where: Clarinet 2, the accented half and dotted-half notes 306-310, 315, 327, 345, 351, 906-910, 915, 927, 945, 951 (16 notes), all first notes on "Leg Slur Rep" after staccato eighths.

Evidence:
- parts.json: Clarinet 2 has no CC11 or CC1 point in 314-318, 326-328, 944-952. CC11 is 104 at every tutti accent (112 at 213 / 897), above ACCENT_CC's `loud_cc` 98, and `_ACC_BY["Clarinet 2"]` = (12, **0**, 116) gives add_loud 0. So there is no bump, and c26's `body_cc` -6 (applied after a bump) did nothing. The c26 acc2 record shows it: Clarinet 2 -5.4 -> -5.4 dB, peak 0.28 -> 0.28 s.
- My measure against all unaccented notes within ±2 qn (first 100 ms): Clarinet 2 **-1.6 dB**, front minus body -1.8, peak 0.31 s, 2-5 kHz front -1.6 under the neighbours' fronts. The cor anglais plays the same notes an octave lower with a 6-unit bump at 314.77 and reads +2.0 dB, peak 0.19 s.
- The manual (p.112) makes Leg Slur Rep a legato row. A detached note on it plays the first-note attack, which is the slow one (BRIEF facts; c23 found the clarinet's "Sus Accent" row worse, -4.5 -> -6.8).

Fix: `build/score_config.py`
- `_ACC_BY["Clarinet 2"]` -> (12, **8**, 116), and Clarinet 2's ACCENT_CC `lead_s` 0.06 (as the strings since c26), so the bump is up before the moved note-on;
- keep `body_cc` -6, which then applies;
- CC11 only: on this CC1-dynamics track, CC1 would change the layer and the brightness.
- Range test 300-360 / 900-960. Acceptance: first 100 ms over neighbours +1..+2 dB, peak 0.22 s or earlier, 2-5 kHz front not above the neighbours' fronts, Dan's figure (+70 ms measure) for Clarinet 2 unchanged within 2 dB.

### 3. The other tutti accents are already at Dan's level on a neighbour measure; what is left is their timing, so no accent should be made louder (measured; the lead change is inferred)

Where: Violins I / II, violas, cor anglais tutti accents (312-360, 900-960, 999).

Evidence: CHANGES' "still under target" uses acc2, which compares the accent with the one detached note before it. In the tutti that note is always the staccato quarter on the downbeat, the hottest note of the bar. Against the median of all unaccented notes within ±2 qn (first 100 ms) the same accents read:

| track | acc2 (CHANGES) | vs ±2 qn neighbours | front - body | 2-5 kHz front - body | peak after beat |
|---|---|---|---|---|---|
| Violins I (Sus MAX, 17) | -2.9 | **+0.9..+1.1** | -1.9 | -1.9 | 0.21 s |
| Violins II (Sus MAX, 27) | -2.8 | **+1.2** | -1.5..-2.0 | -1.4 | 0.26 |
| cor anglais (Sus MAX, 25) | -2.3 | **+1.4..+2.0** | -1.6 | -3.2 | 0.19 |
| violas (Sus MAX, 24) | +0.9 | +4.5 | -0.6 | | 0.10 |
| Flute 1 (Sus Accent MAX, 30) | -1.9 | +0.2 | -0.2 | | 0.07 |

- Dan's +1..+2 dB target is met by Violins I / II and the cor anglais on this measure, and none has bite. Raising their bumps would push them over "a little overdone" (Dan, 2026-11-11).
- What a listener still hears is weight that arrives 0.19-0.26 s after the beat: a short swell on each accent, not a stress on the beat (inferred from the front-body and peak numbers).
- The violas read +4.5 on this measure: over +3. They are inner chord tones under the tune and partly masked, and C / B own the balance side.

Fix:
- Change no accent levels on these tracks. Report accents with both measures from now on (acc2 and the ±2 qn neighbour median) so the target is judged on the second.
- For the timing: ACCENT_CC `lead_s` 0.06 -> **0.10** on Violins I and II, so the bump is fully in before the sustain samples bloom (c26's 0.06 moved the peak 0.25 -> 0.21 s).
- Violas: add_loud 20 -> 14 in `_ACC_BY["Violas"]` (their neighbour measure +4.5, peak already 0.10 s).
- Range test 312-360. Acceptance: peak 0.16 s or earlier; Violins neighbour measure +1..+2; violas +1..+3; 2-5 kHz front minus body at 0 dB or below.

### 4. Violins I's F sharp 5 on "Spiccato RRx9" is hot in the loud layer: +2.7 dB median over its neighbours, up to +5.0, where the D sharp 5 on the same row and layer reads -0.3 (measured)

Where: the rerouted tutti staccatos at v95 (90-114 layer): F sharp 5 at 321, 342, 356, 921, 942, 956 ..., with the D sharp 5s next to them. Also two soft outliers (752 +8.8, 54 +5.9; 1-54 layer).

Evidence (`spic26.py -v` on the c26 render, 70 ms peak over the median of the short neighbours within ±3 qn):
- by pitch and layer: F sharp 5 v90+ (10 notes) median **+2.7**, values 2.9, 4.9 (342), 4.7 (356), 4.6 (942), 5.0 (956);
- D sharp 5 v90+ (14 notes) median -0.3; D5 / D sharp 5 under v90 median -1.9 / -2.1; F sharp 5 under v90 -1.5.
- The five F sharps over +2.9 are the unprinted accents of c26's "over +3: 8": the 342 / 942 F sharps lead into bars 115 / 315, Dan's figure.
- Patch: every Spiccato round-robin group has its own F sharp 5 region (key 78), so a per-pitch region gain reaches exactly this note. Two regions also span 77-78 / 78-79, and Violins I plays one G5 on this row in the whole piece.

Fix:
- `tools/build_reaper.py` `region_gain`: add an optional spec key `"vel_min"` (skip regions whose velMin is under it) to the `pitch_db` loop.
- `build/mix.json` "Violins I" `region_gain_db`: add `{"rows": ["Spiccato RRx9"], "pitch_db": {"78": -3.0}, "vel_min": 90}`.
- This is a region volume in the Opus state, before the hall. No velocity change, so the round-robin sequence is untouched.
- Acceptance (range 312-360 / 912-960): F sharp 5 v90+ median within ±1 dB of the D sharp 5's; 342 / 942 still under the accented C at 345 / 945; fig25 bars 115 / 315 within 2 dB of c26.

### 5. Violins I's isolated staccato quarters still ring 271-291 ms to -20 dB, against 206-251 ms on every other string and wind short row; the data has been unchanged since c24 (measured; fix inferred, not yet range-tested)

Where: Violins I staccato quarters followed by 0.4 s or more of rest or a leap: the theme heads' landing notes and phrase ends (81, 95, 165, 393, 801, 827, 861, 957, ...).

Evidence (c26, onset to -20 dB under the note's band peak; written length 114 ms on every row):

| row | n | peak | -10 dB | -20 dB |
|---|---|---|---|---|
| Violins I Stac RRx14 | 6 | 121 ms | 186 | **291** |
| Violins I Staccatissimo RRx9 | 9 | 81 | 181 | **271** |
| Violins II Stac RRx9 | 26 | 71 | 161 | 206 |
| violas Stac RRx9 | 27 | 101 | 186 | 221 |
| celli Stac RRx9 | 13 | 71 | 166 | 251 |
| Oboe 1 Stac DblTng | 12 | 56 | 171 | 246 |

- The difference is all below -10 dB, 90-110 ms of quiet tail. It is what is left of Dan's "lasting too long" on the strings' isolated notes, and less audible than findings 1-4 (inferred).
- The Stac RRx14 peak comes after the 114 ms note-off. That is why c21 / c23's short caps cut the peaks.

Fix (as c26 A #4, still not run):
- `STAC_MIN_SOUND_S` {"Violins I": 0.14} only on the `STAC_MIN_SOUND_GAP_S` path (0.2 s or more to the next note), so the eighth pairs keep their length;
- a 220 ms `sus_release_cap_ms` with `any_dyn` on "Staccatissimo RRx9" and "Stac RRx14" (Violins I).
- Acceptance (range 84-132, 950-960): 60 ms peaks within 0.5 dB of the control; onset to -20 dB 235 ms or less; eighth-pair separation (`records/stac.txt` method) within 0.3 dB.

## Not ranked

- Violins I's slurred eighth pairs after the tutti accented half notes (317 / 317.5, 329 ..., 917 ...) sit 8-9 dB under the staccato quarters around them (c18 -8.1 / -7.2, c26 -8.3 / -8.7). The second eighth lost 1.5 dB since c18, consistent with c26's body dip still recovering when it starts (inferred). The tutti woodwinds double these eighths. Watch it if finding 3's lead change moves the dip.
- Flute 2 347.5 / 947.5 (low F sharp 5 after B5, -10..-12 dB under the first eighth): unchanged since c18; a property of the sample, no fix proposed.
- Not re-measured this cycle (no data change in c26 for these): pizzicato / arco changes, harp, timpani rolls, con sordino, re-bows, sul A.

Do not touch:
- the c26 woodwind figure state: SLUR_END_BEFORE_STAC 35 ms, the 120 ms caps on the f sustain and TLeg groups, f trails -6 dB, Oboe 1 tutti staccatos v118. The eighths keep their level within 0.6 dB, and the tail before the staccato is 60-100 ms shorter;
- the strings' figure treatment (bar 23 lead, ends and lift; bar 38 / 263 lifts);
- the Spiccato three-row split and its layer cuts (finding 4 adds a pitch cut only);
- the summit's "Sus Marc LITE" stroke on Violins I (front +4.2 dB over its body, peak 0.07 s);
- the flutes' and Oboe 1's "Sus Accent MAX" accents (peak 0.02-0.07 s);
- the 150 ms short-row caps on Violins II and violas;
- the CC11 sfp shape at 900.
