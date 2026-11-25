# Critic C, cycle 3 (tempo, timing and transitions), on the c02 render

Lens: the tempo map against the printed tempos and steps, attack timing at this tempo (Dan's S2), keyswitch lead times, note starts between sections, phrase endings and tutti cut-offs, breaths before big entries, the final fermata. Everything below is measured on `cycles/c02/render/` (stems and master) against `build/parts.json` (written 13:25, two minutes before the c02 render; it is the render's data) and `build/mockup-events.tsv`.

Method (measured). Each note's perceived attack was measured with `tools/pcx.py attack_pcx` (harmonic bands, the previous pitch's partials excluded; pc = mean of the half-amplitude crossing and the reference -10 dB crossing). The value is in seconds relative to the score onset `sq`, on the parts.json tempo map. I measured 8935 onsets on 29 stems (chords counted once) and kept 8484 with a rise of 6 dB or more. Instant attacks set the estimator's own offset: harp +4 ms and timpani +11 ms (median). The strongest measure is relative: each note's pc minus the median pc of the brass and timpani at the same onset, at onsets where 5 or more tracks attack (650 onsets). Legato joins were measured with `tools/pcx.py` itself.

## Manual notes (MANUAL-READING row c3 C: May 2021 HO manual p.143-149; Movement I's c37 C table read first; MANUAL-GAPS.md)

| Manual (PDF page) | What it says | Where in this mockup | Does the render follow it? |
|---|---|---|---|
| p.143 | Performance-script CCs: CC5 legato/portamento time, CC15 con sordino, CC22 mono/poly true legato, CC36 RR reset, CC57 legato script, CC65 portamento script, CC69 repetition, CC70 finger position. | parts.json writes CC1, CC11 and the pre-roll CC36/CC69. CC15 and CC70 lanes are empty on all 31 tracks. No CC5, CC22, CC57 or CC65. | Yes. As Movement I c37 read, CC5 times only the emulated scripts, and those are off in the KS Masters, so CC5 does nothing for the slow transitions. Trumpet 1's mute is the "Mute Sus" row, not CC15 (CC15 is a strings script anyway). Read. |
| p.144 | True legato: velocity sets transition time (50-60 slower, 110-127 tighter), not loudness. CC22 64-127 = monophonic. | String and brass legato targets get v124 (`LEG_VEL_STRONG`). | Partly. Legato targets follow it. But about 190 legato-row notes are not treated as targets: no overlap, no lead, velocity 83-91 from the printed dynamic. They play as first notes and land +87..+137 ms late (finding 1). Measured. |
| p.145 | The Repetition script varies repeats at random. RR reset (CC36) makes playback repeat identically. | CC36 127 in the pre-roll, CC69 0 on the strings. | Not fully. `/Library/Application Support/East West/Opus/Preferences.json` reads `"RoundRobinResetCC": 16`, so CC36 may not reset (MANUAL-GAPS #6). Symptom: the attack probe's Violoncellos qn 24, with unchanged notes, read +0.42 / +0.15 / +0.36 s in c00 / c01 / c02. Not a ranked finding: Movement I measured timing as repeatable between renders (c35-c36, median 0 ms). Send CC16 in a cycle that refits anyway. Measured / read. |
| p.145-149 | Finger position on CC70, with string-by-note tables for violins, violas and celli (p.147-149 pictures; text tables read). Not every note exists on every string; FP4 is warmer. | No sul G/D/C/A is printed, and the CC70 lanes are empty. A freshly rebuilt track plays FP4 (README). | Nothing to apply for timing. c03's full rebuild of every track (ir_setup, release caps) puts every string section on FP4; that changes colour, not timing. Read. |

MANUAL-GAPS items that touch timing:
- #2 (repetition rows): would move every repeat's attack time. The hammered tutti is in time now (Do not touch), so re-measure S2 if it is tried.
- #8 (slower legato velocity on cantabile lines): would make finding 4 worse unless the leads grow with it.

## State through this lens (measured)

- **Tempo map.** It equals the printed tempos exactly. Section lengths: 0-192 68.57 s, 200-324 51.67, 328-592 94.29, 600-784 65.71, 840-880 16.67, 888-936 25.71, 936-976 18.18, 984-1080 32.73, 1088-1116 11.67, all identical to the printed tempo. The eight ramps follow `global.ily`'s \mt steps. Between ramps every beat is identical: `CAESURA`, `PHRASE_ARCS`, `TEMPO_PUSH` and `BEAT_STRETCH` are empty.
- **Keyswitches.** Every keyswitch precedes its note, by 7.1 ms at least (strings) and 10-27 ms typically. None comes after its note-on. No problem.
- **Hammered tutti, relative to brass/timpani (holes excluded).**
  - Coda 199-204 (qn 792-816): upper strings -2 ms, low strings -1, winds 0, timpani +5.
  - Accelerando 205-210: -14 / +6 / +6.
  - Più allegro 247-270 (qn 984-1080): upper strings -5, low strings -7, winds +12, timpani -1.
  - The hammered eighths of strings, brass and timpani sound together.
- **Where sections are late, relative to brass/timpani (holes excluded).**

  | passage | upper strings | low strings | winds |
  |---|---|---|---|
  | Closing group F, qn 328-392 | +51 | +52 | |
  | Maestoso chorale P, 888-936 | +44 | +71 | +25 |
  | Largamente O, 840-888 | | +38 | |
  | Recapitulation K, 600-680 | | +30 | |
  | Final Largamente T, 1088-1116 | +37 | | |

- **Tutti spread.** Median p10-p90 spread of perceived attacks across tracks at tutti onsets: 77 ms (N), 82 (K-M), 92 (R), 94 (A-B, F-J), 104 (D-E), 110 (O-P), 128 (Q).

## Findings

### 1. About 190 legato-row notes play as unled first notes, 0.09-0.12 s late: the F1 theme's second note after its accented head, and the violins' long note after slurred eighths (measured)

**Where:** 331 notes on legato rows (Leg Slur MAX / Leg Slur / Leg BC MAX) have no overlapping note of another pitch before them and no lead. Of these, 312 are measured.

**Groups (median pc after the score onset):**
- **Accented slur head, then the next note (wind/brass):** wind 71 notes at +87 / +101 ms (after a Sus MAX / Sus Non Vib head); brass 34 at +94 / +137; strings 4 at +80.
- **Slurred short eighths, then the long note (strings):** 80 notes at +118 ms, with Sus MAX `short_sus` eighths before them.
- **The rest:** 117 notes after a slur break on the legato row, or after a staccato row. They are on time (-23..+5). Leave them.

**Examples:**
- F1's head motive. Accented half, slurred to a dotted quarter:
  - Horn 1 qn 74 +140 ms, 602 +157, 634 +156, 650 +169, 1058 +157;
  - Oboe 1 90 +194, 578 +227, 826 +165, 1074 +151;
  - Flute 1 578 +200;
  - Bassoon 1 106 +255, 122 +370;
  - Trumpets 1 / 2 970 +219 / +214;
  - Horn 1 970 +241.
- Violins I / II 66 +260 / +270, 626 +259 / +256, 97.5 +226 / +241, 657.5 +234; Violins II 328 +246.
- Bar 263's fff with the crash (qn 1048): Violins I +220 and Violas +237 ms, against the brass at -17..+11.

At 0.36 s per beat, these second notes arrive a third to two thirds of a beat late.

**Why (read in `tools/score_to_parts.py`):**
- The wind/brass branch puts an accented slur head at f or louder on `GENTLE_ACCENT[...]["arts"]` (Sus MAX, `acc_art`). The next note of the slur goes to Leg Slur MAX.
- But `slur_start_ok()` rejects accented heads (`q in accent_q`) and heads over 0.6 qn, so the head is not marked `slur_start_sus`.
- The next note therefore gets no `SOST_JOIN_LEAD_S`, no overlap and no `SOST_VEL`. It is a disconnected Leg Slur note at the printed velocity (83-91), which plays the slow first-note layer (p.144; kit section 6).
- Strings: a slur's long last note after `short_sus` eighths (the Sus MAX notes end at the onset, gap 0.01 qn) is a Leg Slur MAX note with no predecessor on its own row and no lead.
- c02's LEARNINGS asks for a scan of exactly these "legato-row notes with no overlapping note before them". c02 checked only that none were added; the 331 from c01 remain.

**Fix:**
- (a) Wind/brass: a generic option in `tools/score_to_parts.py`, `ACC_HEAD_JOIN = True` (default off; on in `build/score_config.py`).
  - In the wind/brass articulation branch, after `n["acc_art"] = True` for a monophonic slur head, set `n["slur_start_sus"] = True` when the slur's next note abuts (|onset - end| < 0.05), has another pitch, is monophonic and is on a legato row.
  - The existing SLUR_START_SUS join then gives that note `min(SOST_JOIN_LEAD_S, 0.45 x head)` = 0.12 s, `SOST_VEL` 100 and the legato overlap.
  - The head keeps its swell and its Sus MAX attack.
- (b) Strings: in the same pass, mark the last `short_sus` note before a long Leg Slur MAX note of the same slur as a join source. The long note then takes the string legato lead (`LEG_LEAD_S` string 0.17, Violins II / Violas 0.20), capped by `LEG_CAP_FRAC` 0.75 of the eighth (about 0.13 s at 168 qpm), with `LEG_OVERLAP` and `LEG_VEL_STRONG` 124.
  - If the KS Master does not join Sus MAX into Leg Slur MAX on the strings (Movement I used SLUR_START_SUS on winds and brass only), fall back: play the long note on Sus MAX with the `SHORT_SUS_LEAD_S` 0.06 s lead.
  - For comparison, string Sus MAX long notes with a lead read +41 ms here, against +71 without one.
- **Check:** rescan parts.json for legato-row notes with no overlapping other-pitch predecessor and no lead. Target: 0 in the two groups above.
- **Targets:** after the render, these notes' pc within ±40 ms of the brass/timpani median at the same onset (now +87..+137 ms); none more than 100 ms late.

### 2. String entries after rests on Leg Slur MAX and Tremolo come in 0.04-0.1 s behind the brass: the recapitulation downbeat and the 223 arrival (measured)

**Where:** string notes entering after a rest of 0.3 qn or more, at onsets with 5+ tracks.
- Leg Slur MAX long notes: n 64, median +68 ms after brass/timpani, 58% more than 60 ms late. The lead is 0.06 s (`ENTRY_LEAD_S` string (0.12, 0.06, 0.12); f/ff takes 0.06).
- Tremolo entries (all): n 33, +40 ms, 39% more than 60 ms late (`TREM_ENTRY_LEAD_S` 0.04; many trem pieces at 1090-1100 have no lead).

For comparison, entries after rests elsewhere:
- brass long 0 ms, winds long +6 (they have `ENTRY_LEAD_ART_S` wind Leg Slur +0.055);
- string Sus MAX short -6, Stac 0.

**Examples (pc re score, brass/timpani at -25..+28 ms at the same onset):**
- Recapitulation, bar 151 (qn 600, Tempo I ff): Violins I +123, Violins II +107, Violas +82, Violoncellos +137 ms.
- Arrival, bar 223 (qn 888, fff): Violins II tremolo +84, Violoncellos +48, Basses +43, against brass -25..+18 and timpani -16.
- Final Largamente, 273 (1088): Violins II tremolo +84, Violins I +60.
- Final Largamente tremolo pieces at 1090-1096: Violins II +105..+126, Violoncellos +103..+142.

**Fix (`build/score_config.py`):**
- `ENTRY_LEAD_ART_S["string"] = {"Leg Slur MAX": 0.06}`, the extra on top of the family entry lead. This is the wind rule's model (Movement I c03 measured winds' Leg Slur first notes at +0.150 s). Total 0.12 s at f/ff, still under `ENTRY_CAP_S` 0.30.
- `TREM_ENTRY_LEAD_S` 0.04 -> 0.08.
- The tremolo split/re-strike pieces get the same lead where they follow a gap: check `trem_splits` in parts.json at 1088-1104.
- **Targets:** string entries after rests within ±30 ms of the brass median at 600, 888 and 1088; tremolo entries median under +25 ms.

### 3. Double basses: every abutting pitch change on a long note lands 66 ms after the rest of the orchestra; Movement I's ABUT_LEAD was not carried over (measured)

**Where:** Double basses, abutting new-pitch Sus MAX notes of 0.75 qn or longer, 166 notes. Median +66 ms after the other tracks at the same onset; 55% more than 60 ms late. Their short abutting notes are on time (+1 ms, n 27).

**By section, relative to brass/timpani:**
- closing F +59;
- Largamente O +105 (qn 848 +145, 856 +125, 884 +131);
- Maestoso chorale P +93 (900 +113, 908 +138, 928 +99).

The cellos double the same line on Leg BC MAX with legato leads at +7..+20, so the bass line's octave arrives in two places about 0.05-0.1 s apart. Stems: Cb 644 +274 ms, 90 +246, 774 +221, 764 +213 (pc re score).

The same holds for Violins I / II long abutting Sus notes: +69 / +45 ms (n 19 / 23).

**Why:** the Basses KS Master has no Leg BC row, so connected unslurred bass notes are Sus MAX strokes that abut with no lead. Movement I measured the same lag (c20: Cb crossover +0.155 s against celli +0.05) and fixed it with `ABUT_LEAD["Double basses"]` = 0.12 s (`symphony/mvt1/reaper-v621/build/score_config.py` line 264). That is score config, so the port left `ABUT_LEAD = {}`.

**Fix (`build/score_config.py`):**
- `ABUT_LEAD = {"Double basses": {"lead_s": 0.07, "max_cc": 127, "overlap_qn": 0.0, "skip_next_same": True, "rebow_ok": True, "cap_frac": 0.45}}`.
- Restrict it to the long notes, either by an `at` list (the actor generates it: Cb abutting new-pitch Sus notes of written length 0.75 qn or more), or with a new `min_qn` key in `abut_cond()`. The hammered short changes are already in time and must not move.
- 0.07 s is the measured +66 ms. Movement I's transfer was about 0.9 s of pcX per second of lead (its c42 note).
- Violins I / II: the same entry with `lead_s` 0.05 and an `at` list of their 42 long abutting notes.
- **Target:** Cb long pitch changes within ±30 ms of the onset median; Cb minus Vc at shared changes under 30 ms.

### 4. String legato joins: robust SD 59-75 ms and 38-41% more than 60 ms off, with no per-onset lead table yet (measured)

**Where:** `tools/pcx.py` on c02.

| section | joins | pcX median | robust SD | more than 60 ms off |
|---|---|---|---|---|
| Violins I | 196 | +21 ms | 75 ms | 40% |
| Violins II | 185 | -11 | 73 | 41% |
| Violas | 192 | -12 | 67 | 40% |
| Violoncellos | 279 | +24 | 59 | 38% |

Window medians are 72-83 ms. `build/leg_leads.json` is empty: Movement I reached about 750 per-onset entries by its c42-c44.

The section medians also drift by passage:
- Violins I: meno mosso D-E +46, closing F +48, recapitulation K-M +30, against Largamente O -22.
- Violoncellos in closing F: Leg Slur MAX targets +113 ms against brass/timpani (365.5, 369, 364 at +113..+182).
- Violins I in closing F: +71.

**Fix (`build/leg_leads.json`, Movement I c42's method):**
- For exposed joins (stem within 10 dB of the master over +0..0.3 s) more than 60 ms off their section's median, whose crossover deviates in the same direction: lead += 0.6 x (pcX - median), clamped ±0.12 s.
- On c02 that selects:
  - Violins I 41 joins (13 late, 28 early; e.g. 750 +0.087, 783 +0.071, 780 -0.070, 280 -0.068, 351 -0.066, 960 -0.065);
  - Violoncellos 28 (e.g. 42 +0.12, 60 +0.11, 334 +0.101, 672 -0.090, 354 +0.069, 164 +0.069);
  - Violas 12 (787 +0.112, 184 -0.093, 1077 -0.089);
  - Violins II 8 (941 +0.074, 154 -0.074, 90 -0.071).
- Refit after findings 1-2, because a join after a fixed hole changes its predecessor.
- Use the section median of each passage (table above) for the closing group, not the whole-piece median.
- **Target:** robust SD under 50 ms, under 25% more than 60 ms off, closing-group string targets within ±40 ms of brass.

### 5. Tutti cut-offs: the cellos and Horn 1 ring 0.43-0.56 s after the release while the violins are gone in 0.1-0.28 s (measured)

**Where:** the ten tutti cut-offs with a rest after them (qn 5, 21, 102, 135, 374, 450, 631, 662, 814, 1113).

**Note-offs:** within -50..+20 ms of the written end, except the deliberate early ends (horns -179 ms at 102 and 662). The tracks release together.

**Time for each stem to fall 20 dB below its pre-cutoff level:**
- median 155-275 ms, p90 260-431;
- Violoncellos 520 (qn 5), 555 (21), 435 (374), 545 (814);
- Horn 1 495-505 (5, 21);
- Violins I 60-275.

The master has already dropped 13 dB by 0.2 s at 5, 21, 450 and 814 (the hall change works). What remains is the low strings' and horn's own release under the clean violin cut. That is the "mushy" low end after cut-offs (inferred).

**Fix:** c03's planned Movement I c44 release caps, which this supports:
- `mix.json sus_release_cap_ms`: strings 150 ms on Sus MAX / Sus Marc LITE, pp-ff; horns 237 ms on Sus MAX / LegRep.
- Make sure Violoncellos and Double basses are in the strings entry and Horn 1 in the horns entry.

**Target:** every stem -20 dB within 300 ms at the ff cut-offs 5, 21, 374, 814; cellos within 100 ms of the violas.

### 6. Tempo map: the allargando into the 223 arrival undershoots to 106 qpm and then speeds up on the fff downbeat; the cantabile sections run exactly metronomic (measured / inferred)

**Where:**
- **880-888 (bars 221-222, allargando into Maestoso 2 = 56).** `smooth_tempo()` places the printed steps 124 / 112 at their step midpoints and extrapolates to the span end: 142.75 -> 106.4 qpm at 887.75, then 112 at 888. The arrival's downbeat is 5% faster than the beat before it, the reverse of an allargando landing (measured, parts.json).
  - The same code gives no such step at the other ends: 192-200 ends at 145.3 -> 144; 1080-1088 at 146.4 -> 144. At 592-600 (132.5 -> 168) and 784-792 the jump is the printed Tempo I.
- **Rubato.** The Poco meno mosso trumpet solo (qn 200-264, 124 qn, dolce cantabile) and the Poco più mosso molto cantabile (936-976) run 62 and 20 half-note beats at one tempo. Movement I added phrase arcs after critics measured the same flatness (its c12, c15, c24). Inferred benefit: a real player shapes the end of each 4-bar phrase. The printed breath marks at 216, 232 and 251 (Trumpet 1) and 960-968 mark the phrases.

**Fix:**
- (a) `tools/score_to_parts.py` `smooth_tempo()`, generic: when a decreasing ramp ends on a printed tempo at or below its last inner step (`step_val(e) <= inner[-1][1]`), set the extrapolated end anchor to `max(extrapolated, step_val(e))`.
  - Effect: 880-888 ends at 112. No other span changes (200: 145.3 > 144; 1088: 146.4 > 144; 600 and 792 are returns to Tempo I and are not clamped).
- (b) Optional weight into the arrival: `BEAT_STRETCH = {887.0: 0.95}` (the last beat of 222, inside the allargando, so the score supports it). It adds about 0.03 s.
- (c) `PHRASE_ARCS = [(200, 216, "sub"), (216, 232, "sub"), (232, 248), (936, 952, "sub"), (952, 968)]`. None of them touches a ramp. Leave the solo's last phrase (248-264) plain in this first try. Generic factors (`PHRASE_SLOW_SUB` 0.98 / 0.95). Re-run the leads afterwards: they are converted on the shaped map.
- **Target:** no beat inside or at the end of a rit./allargando ramp faster than the beat before it, except the printed returns to Tempo I.

## Do not touch

- The tempo map's section lengths: equal to the printed tempos.
- The ramp shapes at 192, 324, 592, 784, 816, 976 and 1080.
- Keyswitch leads: 7-27 ms ahead of every note.
- The hammered tutti alignment of strings, brass and timpani in 199-210 and 247-270: within ±14 ms of brass/timpani.
- Brass and wind entries after rests: 0 / +6 ms.
- Cut-off note-offs: within -50..+20 ms of the written ends.
- The final release and fermata ring: the chord ends at qn 1112.9; the master has 9.2 s after the release; the mp3 cuts near -50 dB.
- The printed breath dips at 584, 856, 1000-1040 and 1088: master 2-6 dB.
- `SFP_SPIKE_S` / `SFP_VEL` timing at 592.
