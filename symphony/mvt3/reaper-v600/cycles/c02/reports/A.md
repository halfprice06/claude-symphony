# Cycle 2, critic A: articulation and phrasing (render c01, score v600)

Method. All numbers come from the c01 stems and master (`cycles/c01/render`, after the stem fix), placed on the tempo map in `build/parts.json`. Note rows come from each track's keyswitch lane; score marks, slurs and ties come from `build/mockup-events.tsv`.

- **Repeat dip (S1).** Built from the repeated pitch's harmonics 1-4 (4096-point FFT, 5 ms hop, 30 ms box). The dip is min(peak in the 0.15 s before, peak in the 0.03-0.25 s after) minus the minimum in -0.10..+0.06 s around the score onset. Tied notes are excluded.
- **Low notes.** Under about 100 Hz the band measure blurs gaps under 0.1 s, so for the bass line I also give a broadband 10 ms dip and the master's 35-180 Hz dip.
- **Staccato length.** Time from the band peak to 10 dB under it. This measure reads shorter than c01's (strings 0.14 s here, 0.27-0.33 s in c01), so compare rows only within this table.
- **Accents.** 2-5 kHz energy over the first 80 ms minus the note body (+0.15..+0.6 s).
- **Timing (S2).** Perceived attack is `tools/pcx.py attack_pcx` (pc, seconds from the score onset).

"Measured" means a number from the render, parts.json or a patch file. "Inferred" means reasoned, not tested.

## Manual notes (cycle 2, slot A: 2021 manual PDF pages 95-99, strings effects and legato)

| Manual (PDF page) | Where it applies in the Finale | Does the render follow it? |
|---|---|---|
| p.95-96: pre-recorded runs (Vln I, Vla, Vc) are one-octave scales sampled whole; KS/MOD/SPLIT pick the direction. | No one-octave scale runs are printed. The runs at bars 3-4 and 263-264 are slurred eighth turn figures of 4+6 and 4+2+4 notes. | n/a. |
| p.96: "Repetitions Runs" script picks up/down slur samples. All samples are repetitions, velocity is ignored and CC11 sets the level. | none | n/a. |
| p.96-97: Slur Runs (Vln I/II only): fast notes, slurs and sustained notes; CC1 picks 3 vibrato levels and CC11 5 dynamics. Minimum speed is about sixteenths at 125 bpm (0.12 s per note). | The turn figures are eighths at 168-176 qpm, 0.17-0.18 s per note, slower than the stated minimum. Both KS Masters have the row (ks_maps). | **Not used, and probably not the right tool at this speed (inferred).** The figure's problem is timing between sections (finding 2), not the row. |
| p.97: Spiccato Runs (Vln II only). | none printed | n/a. |
| p.97: unmeasured Tremolo and Meas Trem TS (tempo-synced). Neither responds to velocity; CC11 changes level and timbre during the note. | Unmeasured tremolos (`:32`) at qn 888-899, 1016-1047 (Vln I under the chorale), 1088-1100 and 1108-1113 ("div. a 3"). All are on the Tremolo row. | **Yes.** The fff to mf subito at bar 224 (qn 892) is a CC11 step (Vln I 122 -> 72), so it acts before the hall (S3). The tremolo velocities (73-127) do nothing, as the page says. Meas Trem TS is not needed: the score asks for unmeasured tremolo. |
| p.98: Trills (half/whole step by KS). | none printed | n/a. |
| p.98: Repetitions (Violas, Basses): about a dozen pulses in a little over a second, tempo-synced, CC11 crossfades 3 dynamics, velocity ignored. | The basses' hammered eighths, coda and Più allegro (qn 792-840, 984-1108). | **Not used** (`STR_REP_DETACH` instead; MANUAL-GAPS Results c42: probe the internal rate first). No change proposed this cycle. |
| p.98: Sul ponticello (Violas only). | none printed | n/a. |
| p.98-99: legato types (bow change, portamento, slur). Basses have Legato Slur only. A legato needs no gap. Patches are monophonic by default; CC22 64-127 makes them polyphonic. | Leg BC MAX is used for 410 string notes (Vln I 78, Vln II 77, Vla 82, Vc 173) and the basses only on Leg Slur. The printed "port." at bar 236 (qn 940-941, Vln I and II, C5 to A5, `\glissando` in sHead.ily) is a portamento. | **Mono rule: yes.** A scan of every legato row for different-pitch overlaps over 0.12 qn found none apart from one legato lead overlap (Horn 2 996-998). **Portamento: no.** `PORT_TARGETS` is empty and qn 941 plays Leg Slur MAX (finding 4). |
| p.99: Legato Slur Staccato adds a stronger attack to phrase-first notes. | The rows are in the KS Masters ("StacSl Leg BC + Slur + Port MAX", "Stac Leg BC + ..."). | Not used. `STACLEG_SPANS` was emptied after Movement I's c16 test failed. No change. |
| p.99: keyswitches select rows. | All tracks. | **Yes.** `ks_clash` is empty on every track, and no keyswitch falls at or after the onset of the note it serves (measured on parts.json). |
| MANUAL-GAPS.md: "Checked" (finger position), Results c38 (`SUL_SPANS`), #2 repetition rows. | The score prints sul G/D/A as TextSpanners at bars 8-10, 41-42, 123-126, 133-134, 169-170, 189-194, 235-245 and 255-256. mockup-events.tsv does not carry them, and `SUL_SPANS` is empty. | **No.** On Movement I, slurred notes did not change string under `SUL_SPANS` (Results c38), so the audible gain is uncertain (finding 4). |

## 1. Same-pitch repeats in the strings and the low winds run together; the bass line's half-note pulse is gone in the ff recapitulation (S1; measured)

**Where.**
- The bass line, f-ff:
  - Vc, Cb, Bn 1-2 and Cbn: G repeated half notes at qn 602-608 (bars 151-153), 630 (158) and 656-658 (164-165).
  - Vc 70, 98 (bars 18, 25), 156 (40), 668 (168) and 828 (208).
- Viola: 38 (bar 10, the accented f arrival of the crescendo).
- Violins: Vln I/II 444 (bar 112, ff); Vln II 842 (211).
- The louré figure (eighth slurred into a tenuto quarter on the same pitch): Vln I, Vln II and Vla at 796 (bar 200); Vln I, Vln II and Vc at 988 (bar 248).

**What is wrong.**
- **Strings are merged.** The merge loop in `tools/score_to_parts.py` (about line 2427, the c03 rule for repeats inside a legato line) also merges unslurred repeats and printed new bows. Each pair becomes one note with a 10-14 CC CC11 notch.
  - Example: Vc 602 is one 6.62 qn Leg Slur MAX note covering four printed half notes.
  - 49 printed string repeats are merged this way, the 24 "change bow at will" chorale notes included.
- **The basses get no real gap.** They are not merged (Sus MAX), but get only the 0.03 qn same-pitch gap (10 ms at 168 qpm).
- **The bassoons' gap is too short.** Bassoons and contrabassoon get `WIND_REP_RETONGUE`'s 0.06 s gap with a 6 CC fall, which the release and the hall fill at G1-G2.
- **Only the low brass separate.** Of the instruments on this line, only the bass trombone (and the tuba where it plays) re-attack.

**Evidence (measured).**

| onset (bar) | Vc | Cb | Bn1 | Cbn (band / broadband) | B.tbn | master 35-180 Hz |
|---|---|---|---|---|---|---|
| 604 (152) | 0.1 merged | -0.1 | 2.2 | -0.1 / 3.4 | 7.0 | 6.9 |
| 606 (152) | 4.7 merged | 4.2 | 1.7 | -0.1 / 3.5 | 6.9 | 2.6 |
| 608 (153) | 0.0 merged | 0.0 | 1.9 | -0.1 / 3.2 | 6.9 | 1.0 |
| 658 (165) | -0.1 merged | -0.1 | 2.3 | -0.1 / 3.6 | 7.0 | -0.3 |

- **Elsewhere in the bass line.** Vc 70 / 98 / 156 measure 2.1 / 0.2 / 1.7 dB.
- **Basses outside the coda spans.** The basses' repeats outside the two `STR_REP_DETACH` spans (40 notes) have a median of 2.2 dB, and 25 are under 3 dB.
- **Viola accent.** Vla 38 (accent, f) measures 0.4 dB: the accent on the repeated note is not heard as a new stroke.
- **Louré figure.** Vln I 796 / 988 measures -0.4 / -0.4 dB, Vln II 2.0 / 2.6 and Vla 1.7. In the same bars the flutes re-tongue the figure (`rep_retongued` 796, 988), so the winds play two notes where the strings play one.
- **String totals.** String repeat medians are Vln I 2.8, Vln II 3.0, Vla 4.5 and Vc 2.7 dB. Wind and brass are 4.5-7.8, except Cbn at 5.1 with p10 -0.1.

**Fix.**
1. **Strings (`tools/score_to_parts.py`, merge loop).** Add a generic option `STR_MERGE_SAME_SLUR_ONLY` (default False, which keeps today's behaviour; True in `build/score_config.py`). With it, a same-pitch repeat is merged only when both notes are in the same slur and the second carries no tenuto or accent.
   - Every other repeat is re-attacked on Sus MAX at `REBOW_VEL_BY_CC`, with the earlier note ending min(0.06 s, 25% of its length) before it. This is Movement I's c44 ONE_TIME item 4; port that code if it lands first.
   - The louré (tenuto inside the slur: 796, 988) takes Movement I c44 A #1's `STR_REP_PORTATO`: the eighth ends min(0.05 s, 25%) early with a 6-8 CC fall over its last 0.04 s, and the tenuto is a Sus MAX stroke.
   - Keep merged: the "change bow at will" whole notes (Vc/Cb 892-940, which keep their staggered re-bows) and the slurred portato quarters (Vla 893-911, Vln II 921-931).
2. **Basses.** Allow a per-span `max_qn` in `STR_REP_DETACH` and add `{"Double basses": [(64.0, 104.0), (148.0, 172.0), (596.0, 672.0), (820.0, 840.25)]}` with `max_qn` 2.0, the same -5 dB / 0.08 s dip and the same 0.06 s gap as the cellos.
3. **Bassoons.** `WIND_REP_RETONGUE_BY` gets `"Bassoon": {"gap_s": 0.10, "frac": 0.3, "fall_cc": 12, "fall_s": 0.15}` and the same values for `"Contrabassoon"`. These are the Horn values; the bass trombone measures 7 dB with its 0.08 s.

**Targets.**
- Stem dip at least 6 dB on Vc, Cb, Bn and Cbn at 602-608, 630 and 656-658.
- Master 35-180 Hz dip at least 4 dB at every one of those onsets.
- Louré: dip at least 6 dB, with the tenuto at most 2 dB over the eighth.
- Re-attacked strokes within ±2 dB of the body before them (Movement I c44 B #5: the new strokes get no `ROW_TRIM_DB`).

## 2. Violins II plays the unison slurred eighths 57 ms ahead of Violins I and the violas (S2, clarity; measured)

**Where.** 120 slurred short notes that Vln I and Vln II play in unison on Sus MAX:
- the F1 tune, bars 11-17, and the counterstatement's countersubject, bars 27-41;
- the recapitulation, bars 151-157, and the coda, 205-206;
- the Più allegro heads, bars 247-253 and 263-267, including the fff turn figure at 263-264 (qn 1049-1054);
- the opening turn figure, bars 3-4 (qn 9-14), which Vla also doubles.

**What is wrong.** `SHORT_SUS_LEAD_TRACKS = ("Violins II",)` (`build/score_config.py`, ported from Movement I). Only Vln II's slurred Sus MAX eighths start 0.1 s early, capped at 0.45 of the slot: about 0.225 qn at 176 qpm. Vln I and the violas play the same notes on the score onset, so the unison sections sound one after the other. At this tempo an eighth lasts 0.17-0.18 s.

**Evidence (measured, pcX).**
- Over the 120 led unison notes, Vln II minus Vln I is a median of -0.057 s. Over all 153 unison short Sus MAX notes it is -0.039 s (p10 -0.110, p90 +0.022). Vln I's pc median is +0.035 s.
- At bar 263, Vln I measures +0.045 s, Vla +0.035 and Vln II -0.038.
- At bar 3, Vln I measures +0.020, Vla +0.017 and Vln II -0.056.
- Own-pitch energy share per note (own harmonics against the previous note's, from onset +0.03 s) at bar 263: Vln I 0.35 (min 0.24), Vln II 0.75. Movement I's pass mark was 0.5. The fff climax figure blurs in Vln I.

**Fix.**
- `build/score_config.py`: `SHORT_SUS_LEAD_TRACKS = ("Violins I", "Violins II", "Violas")`.
- Use a smaller lead for all three: `SHORT_SUS_LEAD_S` 0.06. If the tool only takes a scalar, add a per-track dict option `SHORT_SUS_LEAD_S_BY` in `tools/score_to_parts.py`, defaulting to the scalar.
- Keep `SHORT_SUS_LEAD_KEEP_OVERLAP` 0.03 and `SHORT_SUS_LEAD_CAP_FRAC` 0.45.
- Targets:
  - pc of every section within ±0.025 s on these notes;
  - |Vln II - Vln I| median under 0.02 s;
  - own-pitch share at bar 263 at least 0.5 in Vln I.

## 3. Horn staccatos: the StacSs row is now shorter than every other section, and Horn 1's 38 staccatos still ring twice as long (measured)

**Where.**
- Horns 3/4: the F1 off-beats, qn 40-104 ("StacSs RRx9"), against the recapitulation's "Marc Shrt RRx4" (600-664).
- Horn 1: 38 staccatos on Sus/Leg rows (bars 12-24, 140-164, 206, 266-268), in the same tune where Vln I plays Staccatissimo and the woodwinds play their staccatos short.

**Evidence (same measure for every row).**

| row | -10 dB length, median |
|---|---|
| Horn 3/4 StacSs | 0.10 s (p90 0.13-0.15) |
| Horn 3/4 Marc Shrt | 0.18 s |
| Trumpets 1-3 Stac DblTng | 0.17-0.18 s |
| Bassoon 1 Stac DblTng | 0.15 s |
| String Stac rows | 0.14 s |
| Fl/Ob staccatos | 0.13-0.17 s |
| Horn 1 Leg Slur MAX staccatos | 0.29 s |
| Horn 1 Sus MAX staccatos | 0.26 s |
| Horn 3 Leg staccatos | 0.29 s |

- The F1 horn off-beats are now the shortest notes in the texture.
- Horn 1's staccatos are the longest, twice the string staccato they double.
- c01 also flagged StacSs as too short (0.15 s on its measure), and MANUAL-GAPS "Finale results (c01)" names Marc Shrt for F1 as the next step.

**Fix (`build/score_config.py` `ART_SPANS`).**
- Horns 3 and 4: change the 40-104 span to `"art": "Marc Shrt RRx4"`. Keep `_hn_stac_vel` and the c01 stem-fix level (+3 / +5 dB at 40-104), refit from this render.
- Horn 1: add `{"from": 40.0, "to": 104.0, "art": "Marc Shrt RRx4", "mark": "staccato", "vel_by_cc": _hn_stac_vel}`, with the same entry for 552-664, 816-828 and 1056-1076.
- The slur-end staccatos then re-tongue on the short row instead of sounding as legato targets. That matches the strings, whose slur-end staccatos are already Stac-row strokes.
- Marc Shrt rendered 3.6-8.6 dB under the Sus notes it replaced (c01). Give Horn 1's Marc Shrt notes +2.5 dB (a `roles.json` row per span, or a `ROW_TRIM_DB` entry if the tool takes brass rows), then check level on the render.
- Targets:
  - horn staccato -10 dB length 0.15-0.20 s on this measure (the strings' 0.14, trumpets' 0.17);
  - 2-5 kHz front minus body under +3 dB;
  - level within ±2 dB of the Sus notes around them.

## 4. The printed portamento at bar 236 and the sul A/D/G spans are not rendered (measured in the data; audible effect inferred)

**Where.**
- **Portamento.** Bar 236, qn 940 -> 941: Vln I and II slide C5 -> A5 into the tenuto A5 ("port." with a `\glissando` line, sHead.ily, under "sul A"). Movement I's second theme, "molto cantabile".
- **String choice.** TextSpanners in the score sources:
  - Vla sul G, qn 28-38.9;
  - Vln I/II and Vc sul G, 160-167.9;
  - Vc sul D, 488-495.9; Vla sul D, 493-503.9; Vla sul G, 528-535.9;
  - Vln I and Vla sul G, 673-679.9;
  - Vln I/II sul A, 752-775.9;
  - Vln I sul A, 936-951.9; Vln II sul A, 936-967.9; Vla sul D, 937-947.9;
  - Vln I "div., sul A", 968-979.9;
  - Vln II sul G, 1016-1023.9.
  - Read the exact ends from the `\startTextSpan` / `\stopTextSpan` positions.

**What is wrong.** `PORT_TARGETS` and `SUL_SPANS` are empty in the Finale. parts.json `port` is empty on every track, and the 941 targets play Leg Slur MAX at v124. mockup-events.tsv carries neither TextSpanner texts nor glissandi, so nothing reaches the tools.

**Fix.**
- `build/score_config.py`: `PORT_TARGETS = {"Violins I": {941.0: 100}, "Violins II": {941.0: 100}}`. This is Movement I's format and velocity (its 225.0); kit §7 measured a join with no hole and +17-21 dB of energy at the intermediate semitones on a violin fourth.
  - The Leg Port MAX row must be loaded, so Vln I and Vln II are fully rebuilt. They come back with CC70 127, the default the renders play (`SUL_DEFAULT_CC70` 127).
  - Target: energy at the intermediate semitones (73-80) rising at least 10 dB over the Leg Slur version in the 0.15-0.45 s around the join, and the A5 arrival within ±0.05 s pc.
- `SUL_SPANS` with the spans above. Movement I's Results c38 found that slurred notes did not change string, so expect changes only on the unslurred and Sus MAX notes. Low risk, small gain (inferred). Measure the notes whose CC70 changes and their level, and lift any that drop by more than 3 dB (the celli's open G2 needed +4.5 dB in Movement I).

## 5. The violas' f portato entry at bar 224 opens with a 10.9 dB hole (measured)

**Where.** Violas, qn 892-896: the first portato group, E4 x4 (f) after the fff tremolo of bar 223.

**What is wrong.** The group is one merged Leg Slur MAX note starting from nothing, because the tremolo row note ended at 892. It starts on the slow first-note layer, and the first portato notch (CC11 88 -> 83 at 893) lands in that sag. Kit §5 warns against dipping CC11 there.

**Evidence (measured).**
- Repeat dip at 893: 10.9 dB, against 1.5 and 4.8 at 894 and 895.
- Viola stem per beat from 888: -27, -28, -27, -30 (tremolo), then -39, **-42**, -38, -37.
- The 50 ms envelope falls from -31 dB at the onset to -55 dB at +0.5 s and recovers to -43 by +0.9 s.

**Fix.** `build/score_config.py`: `DOWNBOW_STROKE_AT = dict(DOWNBOW_STROKE_AT, **{"Violas": [892.0]})`. The group's first note becomes a fresh Sus MAX stroke and the slur's next notes join from it. Alternatively, move the 893 notch to the note's end with `MERGE_NOTCH_AT {"Violas": {893.0: 0}}`. Target: no 50 ms frame more than 6 dB under the beat mean in 892-896.

## 6. Trumpet 1's open dolce solo (bars 51-66) still uses the fastest legato velocity (inferred; carried from c01 A #6)

Nothing changed here in c01. The 37 Leg Slur MAX targets at qn 200-264 play v124, the fastest and most present slur (manual p.106, brass legato velocity = transition speed), for a p "dolce cantabile" line. Fix as in c01: a soft brass legato velocity (about 96) at CC11 at or under the p level, as a generic option beside the soft-string rule in `tools/score_to_parts.py`. Measure transition peak minus body (target 0-2 dB, p90 under 3) and pcX crossovers against c01, because the brass leads were fitted at v124. Lowest priority of the six. Do it only if the cycle has room after 1-3.

**Do not touch.**
- **Brass accents** (`GENTLE_ACCENT`). 2-5 kHz front minus body medians: Più allegro heads -6.3 dB (max +2.0, Trombone 1 990), bars 263-272 -7.6, 273-279 -6.4, the chorale arrivals.
- **The tremolo rows** and the CC11 subito at qn 892.
- **Legato rows.** No chords on a legato row; no keyswitch at or after its note.
- **Merges to keep.** The "change bow at will" merges with staggered re-bows (Vc/Cb 892-940) and the slurred portato merges other than Vla 892.
- **Timpani repeated strokes** (median dip 7.0 dB).
- **Trumpet and trombone re-tongues** (p10 2.7-5.6 dB), and the bass trombone's 7 dB.
- **The coda bass detach spans** (`STR_REP_DETACH` 792-840, 984-1108).
- **The rest of c01's do-not-touch list:** pizzicato rows, string staccato rows, harp étouffez, the mute span and its bandpass.
