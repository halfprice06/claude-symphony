# Cycle 44, critic A: articulation and phrasing (render c43, score v621)

## Method

All measurements are on the final c43 stems and master (`cycles/c43/render`, 40 stems). Notes are placed with `cycles/c43/rendered_build/parts.json`, which is byte-identical to `build/parts.json` now.

**The merge list.** I took it from the pipeline itself rather than from the events:
- A scratch copy of `tools/score_to_parts.py` printed one line per same-pitch merge, both in the legato merge loop (the CC11-notch merge) and in the tremolo/flautando common-tone join.
- It was run on `build/` with its output in scratch, and its parts.json came out byte-identical to `build/parts.json`.

**Measures.**
- **Repeat dips.** These use the repeated pitch's harmonic band (`tools/pcx.py band_env`, no exclusion, 2048-point FFT, 5 ms hop, 30 ms box). The dip is min(body before, body after) minus the minimum in -0.12..+0.15 s around the score onset. The rise is the 0-0.25 s peak minus that minimum.
- **Motif repeats.** These use c38's definitions with a finer envelope (1024-point FFT above 180 Hz, 2.5 ms hop, 10 ms box):
  - the "dip below the eighth" is the eighth's peak minus the minimum between the two notes;
  - the "re-attack" is the 0-0.25 s peak minus that minimum.
- **Timing.** pcX (`tools/pcx.py attack_pcx`).
- **Exposure.** "rel" is the stem minus the master over the onset's first 0.3 s.

I touched nothing in build/, tools/ or REAPER.

Evidence labels: **measured** = a number from the render, parts.json or a patch file; **inferred** = reasoned, not tested.

## Manual notes (second round: c38 slot A's pages, 2021 manual PDF pp. 100, 103-107, read again in full; MANUAL-GAPS.md and DIGEST.md read)

### MANUAL-GAPS items still open in this lens

- **#1, brass accents on Marc Sus LITE / Leg Slur Accent.** Still not tried. It is not needed now (measured):
  - all 177 brass accents have a 2-5 kHz front (first 80 ms) minus body of median -9.2 dB (p90 -3.7);
  - their level over unaccented neighbours has a median of 3.2 dB.
- **#5, expressive wind rows:** untried.
- **#7, half-section divisi:** open; finding 4.
- **#9, horn portato rows:** untried (the Horn 1 tenutos were evened in level in c38).
- **#13, 3TB for the bass trombone's MIDI 36-38:** untried. The second pass could carry it.
- **Repetitions TS:** untried.

### c38's notes checked against the c43 render

| Manual (PDF page) | c38 A's note | Now (c43 render) |
|---|---|---|
| p.100: brass instruments; no solo bass trombone | followed | **Followed.**<br>• Since c39 the "2 Trumpets" patch plays the Trumpet 1-2 unisons, and 2FH plays the horn a2 passages.<br>• 3TB is still unused (#13). |
| p.103: Repetitions Fast 170 / Med 145 / Slow 120; Triple Performance; double tongue | n/a | **Still n/a** (measured). No brass staff has a same-pitch run of 4 or more notes of half a beat or less. |
| p.103: Sforzando Crescendo (Solo Horn, Solo Tuba); "when a note is played short enough to end before the crescendo, this patch can act as a sforzando staccato" | n/a | **New on this reading.**<br>• The brass sf at qn 160 (bar 41) is an eighth plus a rest in Trumpets 1-3, Trombones 1-2, Bass trombone and Tuba, i.e. a sforzando staccato.<br>• Only the Tuba has the patch. It would serve one note, so I do not recommend it. |
| p.104-105: crescendo patches (no release trails) | not used; CC1/volume crescendos barely grew | **Still not used, and not needed** (measured, first versus last quarter of the note).<br>• Bar 11 horns (p < f, qn 40-44): +7.5 / +8.9 / +10.6 / +5.7 dB (Horns 1-4).<br>• Bar 40 trombones (p < sf, 156-160): +7.3 / +12.3 / +8.6 dB. |
| p.105: legato only within an octave and with no gap; monophonic unless CC22 < 64 | followed | **Followed** (measured on parts.json):<br>• no legato join wider than 12 semitones;<br>• no same-pitch overlap on any legato row;<br>• no simultaneous onsets (chord) on any legato row in any track;<br>• no CC22 lane. |
| p.106: Legato Slur CC1 = volume, overblow filter near 127; velocity = transition speed | followed | **Followed:** CC1 maximum is 120 on all 13 brass tracks (measured). |
| p.106: Legato Slur Accent (velocity = accent strength) | not used (8 slurred brass accents) | **Still not used, and not needed** (measured).<br>• Horns a2 273 / 311 / 665 / 673, Trumpets a2 665 / 673 and Trombone 1 521 / 529 sit +2.4..+5.8 dB over their slur neighbours.<br>• Their 2-5 kHz fronts are 5.4-12.2 dB under the body: weight, no bite. |
| p.106: Legato Slur Repetitions ("without space between the notes", re-tongued sample) | not used; 6 slurred brass repeats re-tongued on Sus, 4.2-7.7 dB | **Still re-tongued on Sus** (`WIND_REP_PORTATO`). Dip below the eighth / re-attack (measured):<br>• Horns a2 314: 7.8 / 11.0 dB; Horns a2 668: 8.3 / 9.0;<br>• Trumpets a2 524: 8.0 / 9.2; Trumpets a2 668: 4.1 / 10.0;<br>• Trombone 1 524: 5.9 / 3.6;<br>• Horn 3 640: 3.7 / 9.9;<br>• **Horn 2 232: 3.5 / 4.5, exposed (rel -4.9).** This is the one that needs the row (finding 1). |
| p.106: Slur Runs; p.106-107: mutes, stopped horn | n/a / none printed | Unchanged. |
| p.107: keyswitch masters | no keyswitch under 9.5 ms before its note | **Followed:** the smallest keyswitch-to-note distance is 0.02 qn (9.5 ms at 126 bpm), and none falls after its note (measured). |
| MANUAL-GAPS #2 (p.101): LegRep RRx4 | used with a 0.03 s gap (c37) | Used since c38 with the re-tongue gap (0.06-0.15 s) on 49 notes: Contrabassoon, Bassoon 1, Clarinet 1, Bass clarinet, Horns 1 and 4, Trumpet 2. |
| MANUAL-GAPS #1 (p.101): Marc Sus LITE velocity filter | the patch disagrees (velocity sets volume only) | Unchanged. |

### Standing checks (measured)

- **S1, strings.** This is the open problem: findings 1-3.
  - **Merged repeats.** 49 string same-pitch repeats are merged into the note before with a 6-14 CC CC11 notch, plus 24 tremolo common tones.
  - **Unmerged repeats.** The other 348 printed string repeats dip a median of 2.0-4.2 dB in the stems and 0.9-2.7 dB in the master, by length class.
  - **Bass pedals.** The basses' repeated-eighth pedals (`STR_REP_DETACH`) are not a problem in the low band. The master's 40-160 Hz eighth-rate modulation there is 2.5-6.5 dB peak to peak (bars 27-31, 82, 131-142, 167-170). In the Dvořák 9/i reference's loud windows it is a median of 2.9 dB, p90 4.1, maximum 5.2.
- **Item 8, accents.** Front minus body, median: winds -7.3, brass -9.2, strings -5.9 dB. Level over neighbours, median: 2.9 / 3.2 / 3.5 dB. The brightest fronts are all buried (rel -7 dB or lower):
  - Violas 536 +5.9, Clarinet 1 558 +5.2, Celli 526 +4.6, Trombone 1 128 +3.3.
- **Item 7, re-bows.** Unchanged by the CC16 reset.
  - Dips (c42 / c43 median): Violins I 5.7 / 5.7, Violins II 3.4 / 3.1, Violas 3.4 / 3.8, celli 2.7 / 2.6, basses 2.5 / 2.4 dB.
  - Level steps: median |step| 0.6-1.5 dB.
  - Over the final chord (qn 712-727.5) the master's residual level SD is 1.31 dB, with no periodic component over 0.9 dB peak to peak between 0.2 and 8 Hz.
- **Legato rows.** Chords, same-pitch overlaps and joins over an octave: none (see the table).

## 1. The motif's slurred portato repeat is merged in the strings while winds and brass re-tongue it in the same bars (S1; measured)

**Where.** The first-theme motif `d''8( des'' c'' | c''4--)` (slur plus tenuto on the repeated note). The 10 string occurrences are all merged:

| Section | Score qn (bar) | rel (dB) |
|---|---|---|
| Violins I | 60 (16), 108 (28), 140 (36), 572 (144) | -2.8 / -9.3 / -6.4 / -4.4 |
| Violins II | 108 (28) | |
| Violas | 108 (28), 136 (35), 668 (168) | |
| Violoncellos | 314 (79), 524 (132) | |

In bars 16 and 144 Violins I is the leading voice.

**What is wrong (measured).**
- **One note in the strings, two notes in the winds.** The merge loop (`tools/score_to_parts.py`, `SLUR_REP_MERGE_SUS`, notch `SLUR_REP_NOTCH` 6 / 8 CC) plays the eighth and the tenuto as one Sus MAX note with a small CC11 notch. In the same bars, Clarinet 1, Horn 2, Horns a2, Trumpets a2 and Trombone 1 re-tongue the figure (`WIND_REP_PORTATO`).
- **Strings vs winds/brass, dip below the eighth / re-attack (stem medians):**
  - strings: 4.2 / 6.6 dB (dips 0.7-7.5, re-attacks 3.7-9.7);
  - re-tongued winds and brass: 7.4 / 10.5 dB (Clarinet 1 108: 11.4 / 15.1; 508: 9.4 / 14.6; 232: 9.2 / 11.2).
- **No attack in the envelope.** The string envelopes show a CC11 dip-and-return or no dip at all, never an attack. Examples (20 ms steps, dB re the window's maximum):
  - Violins I bar 16 falls from -3 (the eighth) to -9 at +0.04 s and swells back to 0 only by +0.3 s, with no front at the downbeat;
  - celli 524 has no dip at all: the level rises from -5 to 0 across the onset;
  - Clarinet 1 108, for comparison, falls to -15 at -0.04 s and is back at -2 by +0.08 s.
- **The octave mixes both articulations.** At bar 28 Violins I / II and violas double Clarinet 1, so the listener hears the motif re-tongued in the wind and slurred through in the strings.
- **Horn 2 at 232 (bar 59, "2. espr." p, unison with Clarinet 1) is too weak as well:**
  - dip 3.5 / re-attack 4.5 dB, exposed (rel -4.9);
  - Clarinet 1 on the same note: 9.2 / 11.2;
  - because the horn is the louder voice, the master dips only 2.5 dB;
  - its data has a 0.18 qn gap, a 53 → 46 CC11 fall and a -4 dB volume dip, so the Solo Horn's release fills the gap.

**Why this needs a change beyond ONE_TIME item 4.** Item 4 keeps the merge for repeats inside one slur and exempts printed portato. But a slurred tenuto on a repeated pitch is a louré: same bow, with an audible stop and re-pressure. Dan's S1 asks for separation "slurred or not".

**Fix.**
1. **New generic option `STR_REP_PORTATO` in `tools/score_to_parts.py`.** In the merge loop, when `portato` is true (the repeat has a tenuto and the same slur as the note before), do not merge.
   - The tenuto takes the `STR_REP_AFTER_STAC` / `DOWNBOW_STROKE_AT` path: Sus MAX, `down_stroke`, velocity from `REBOW_VEL_BY_CC`, and the string re-tongue lead. It must not become a Leg Slur MAX target, or it plays the c05 first-note hole.
   - The eighth (already a short_sus Sus MAX note) ends min(0.05 s, 25% of its length) early, with a 6-8 CC CC11 fall over its last 0.04 s. These are the `WIND_REP_PORTATO` values.
   - Keep the tenuto weight (`merged_ten`) and `ROW_TRIM_DB`.
   - On Violins I / II, whose Sus MAX release is not capped (`build/mix.json` caps only violas, celli and basses at 250 ms), the gap may not reach the target. If the stem dip is under 6 dB, add a pre-hall CC7 dip (`CC7_POINTS`, about CC7 90, i.e. -6 dB on the 40·log10 scale, over the gap), not a post-hall volume dip. CC7 acts before Opus's hall (MANUAL-GAPS Results c36).
2. **Horn 2 232:** put it on "LegRep RRx4" with the c38 gap rules (`REP_ROW` span 231.9-232.1). On Horn 1 452 / 528 / 624 in c41 this raised the re-attack over the gap from 4-5 to 8-10 dB. Re-measure after c44's drier hall first, since the hall fill may already be smaller.

**Targets per repeat.**
- Dip below the eighth ≥ 6 dB and re-attack ≥ 8 dB in the stem.
- Master ≥ 4 dB where the strings lead (bars 16, 36, 144).
- The tenuto no more than 2 dB over the eighth's peak.
- pcX of the string tenuto within ±30 ms of the winds' re-tongue in bars 28, 79, 132 and 168.

## 2. The other 39 merged string repeats are printed new bows, played as one note with a notch; a stroke list, a soft re-bow list, and the re-bow points that must go with them (S1, S2; measured)

**Rule check.** Every one of the 39 has the note before in another slur, or no slur on either note. Where the composer wants held strings with free bowing he writes ties with "change bow at will" (Vc / Cb qn 8, Cb 48 / 160 / 464, Vc / Cb 288, the final chord 712 / 720). These repeats are written as separate notes, so all 39 are new bows. None of them belongs inside one slur.

**Stem dips now (measured), by the class I propose:**
- strokes (the 15 of lists A and the two slur heads below): median 3.6 dB (range -5.4..6.3), master median 3.1;
- soft re-bows: median 2.1 dB, master 1.5.

The 24 tremolo common-tone joins (Violins II 18, Violas 6; `TREM_JOIN` / `FLAUT_JOIN`) are continuing tremolo; keep them merged.

### A. Strokes (mf or louder, an accent, or a new louder dynamic): 13 notes

| Track | qn (bar) | What is printed | Stem / master dip now (dB), rel |
|---|---|---|---|
| Violoncellos | 47 (12) | f: dotted half, then a quarter on its own bow | 4.9 / 3.1, rel -10.8 |
| | 84 (22) | unslurred half notes | 0.8 / 2.2 |
| | 88 (23) | **accented** dotted half starting a crescendo | the merged note falls to -11 dB at +0.08 s and recovers slowly: a hole, no accent |
| | 152, 156 (39-40) | whole notes, crescendo to f | 3.8 / 4.7, 5.0 / 4.8, rel -8.5 / -7.5 |
| | 164 (42) | new mf after sf > | 1.3 / 2.9 |
| | 326 (82) | two **ff** half notes before the accented down-bows | -5.4 / -1.0: the second note is lower than the first, no dip |
| | 374 (94) | f half notes | 5.3 / 3.7 |
| | 448 (113), 456 (115) | stringendo whole notes, mf-f | 6.3 / 4.3, 6.3 / 2.1 |
| | 668 (168) | f half notes | 2.0 / 4.1 |
| Violas | 80 (21) | f: slur end into a new slur with decrescendo | 2.2 / 2.3, rel -3.8 |
| | 372 (94) | f: whole note into a new slur | 2.6 / 3.6 |

**Strokes on a slur head at p-mp:** Violas 500 (bar 126, a new p) and Violoncellos 656 (bar 165, mp, an arpeggio slur): 2.4 / -0.6 and 6.3 / 1.8.

### B. Soft re-bows at the printed note (pp-p, notes of 0.9 s or more): 24 notes

- **Violins II:** 176 (45); 188, 192 (48-49, pp metà); 208 (53); 292 (74, after a slur end); 576, 580 (145-146).
- **Violas:** 32, 36, 40 (9-11, the Lento, p > pp <); 52 (14); 292, 296 (74-75); 576, 580 (145-146); 688 (173); 700 (176).
- **Violoncellos:**
  - 32 (9); 40 (11, mp inside the crescendo); 52 (14); 168, 172 (43-44);
  - 176 (45, pp, a slur head: re-bow plus join to 178);
  - 180 (46).

### What the merges do to the re-bows now (measured, parts.json `rebows`)

The frozen automatic re-bows (`_REBOW_FROZEN`, c11) fall inside these merged notes, near but not at the printed bow changes. In several places a printed notch and an automatic re-bow land within a second of each other, i.e. two bow events:
- Violas: the 32 notch, then 32.364 (0.44 s later); 36 then 36.856 (1.0 s); 39.353 then the 40 notch (0.8 s);
- Violoncellos: 31.393 then 32 (0.7 s); 152 notch then 152.461 (0.2 s at 126 bpm);
- Violins II: 188 then 189.62 (0.9 s).

After un-merging, these points would cut the printed notes into odd pieces. The ones under `NOTCH_SKIP` (celli 39.879 / 51.87 / 163.877) would re-attack 0.06-0.16 s before the printed stroke.

### Fix (tools/score_to_parts.py, build/score_config.py, build/rebow_fills.json)

**Strokes (A):**
- Gap min(0.06 s, 25% of the earlier note), as in ONE_TIME item 4.
- Sus MAX at `REBOW_VEL_BY_CC`, with the string re-tongue lead, refit per onset on pcX (`build/retongue_leads.json`).
- Slur heads (Violas 80 / 372 / 500, celli 656) take the `DOWNBOW_STROKE_AT` path, so the slur's next note joins them as a Leg BC target.
- Celli 88 keeps the `GENTLE_ACCENT["string"]` swell on its new stroke.
- Targets: stem dip ≥ 6 dB, master ≥ 3 dB where rel > -10 (Violas 80, celli 152 / 156 / 326 / 656).
- Reference for what a re-stroke gives in this mix: celli 340 (bar 86, a Stac → Sus MAX stroke after a 0.093 qn gap) dips 6.2 dB in the stem and 6.1 dB in the master.

**Soft re-bows (B):** feed each printed onset into the re-bow machinery as a `REBOW_AT` point. That gives a Sus MAX piece after `REBOW_GAP_QN` 0.03 qn at the re-bow velocity, fitted by `tools/fit_rebows.py` on the c44 render.
- Targets: stem dip 3-5 dB and |level step| ≤ 1.5 dB, like the automatic re-bows now (2.4-3.8 dB, steps 0.6-1.5).
- A 6 dB hole in a pp pad would be wrong.

**Remove these frozen points, their `rebow_fills.json` rows, and `NOTCH_SKIP` Violoncellos 40 / 52 / 164 and Violas 52:**
- Violins II 189.62;
- Violas 32.364, 39.353, 52.384, 686.694, 699.507;
- Violoncellos 31.393, 39.879, 45.371, 51.87, 152.461, 163.877, 169.146.

**Keep one point inside each printed Lento note longer than `REBOW_MAX_S` 4.5 s** (whole notes at q=50 last 4.7-4.95 s), the existing point nearest the middle:
- Violas 30.034, 34.694, 36.856;
- Violoncellos 29.383, 33.403, 37.377, 41.38, 49.683.

Then run `tools/space_rebows.py --write`.

**Scope.** Apply the stroke rule to every string same-pitch re-attack not under one slur, not only to merged ones. The 85 unmerged Sus MAX repeats of 0.4 s or longer at mf and louder dip a median of only 3.5 dB in the stem and 2.3 dB in the master (86% under 6 dB; violas 41, basses 30). The bass pedals' eighths stay on `STR_REP_DETACH` (low-band modulation already at reference level, above).

## 3. Slurred eighths in Violins II, violas and celli are re-bowed Sus MAX notes, while Violins I plays them legato; in octave doublings the attacks spread (articulation and S2; measured)

**Where.** 58 slurred non-first notes of 0.15 s or more play the short_sus Sus MAX path:
- Violins II (25): bars 21, 27-29, 32, 65, 69-71, 92-95, 100, 139-140;
- Violas (26): bars 27, 29, 34, 38, 70-71, 89, 92, 109-116, 167, 169;
- Violoncellos (7): bars 86, 88, 131-134.

Since series-1 c06-c07, Violins I plays these notes as Leg Slur MAX targets (`SHORT_SUS_LEG_TRACKS = ("Violins I",)`, `LEG_CAP_FRAC` 0.75). It has 51 slurred non-first short notes on Leg Slur MAX and only 4 on Sus MAX. 23 of the Sus MAX notes fall on onsets where Violins I plays the same figure legato: Violins II at 81, 107, 109.5, 115, 275.5-281.5, 399.5, 555-557.5; violas at 107, 115, 149, 277, 283.5, 443.5-451.5.

**What is wrong (measured).**
- **A re-attack inside each slur.** Each Sus MAX note in a slur has a small front bump and a brighter front, against Leg Slur notes in the same tracks:

  | Row | Front bump (dB, median) | 2-5 kHz front minus body (dB) |
  |---|---|---|
  | Sus MAX | +1.0 / +1.2 (Violins II / violas) | -4.8 / -4.4 |
  | Leg Slur MAX | -0.1 / -0.9 | -5.2 / -6.8 |

- **The doubled attacks spread.** At the 23 shared onsets, pcX differs from Violins I by more than 30 ms at 15 of them:
  - Violins II runs early by 26-170 ms (bars 21, 27-28, 139-140);
  - the violas run late by 28-68 ms (bars 29, 70-71, 111-113).
- The same slurred figure in octaves is therefore both re-articulated and ragged. That adds to the mush Dan hears (S4) as well as to S2.

**Why the old reason no longer holds.** The original reason for short_sus came from series-1 c03: "transitions of 160-320 ms" on legato rows. That figure was measured with an estimator that c42 showed reads shared low partials as overlap. On pcX, every section's legato transition lasts 82-98 ms (MANUAL-GAPS Results c42). The HO legato itself needs only no gap and an interval within an octave (p.98-99; p.105 for brass).

**Fix.**
- `SHORT_SUS_LEG_TRACKS = ("Violins I", "Violins II", "Violas", "Violoncellos")`, and `LEG_CAP_FRAC` [(56.0, 728.0, 0.75)] for the three new tracks, as Violins I has.
- The slur-repeat eighths before a same-pitch note stay on Sus MAX (the existing condition), as do sixteenths and sextuplets (under 0.20 s).
- After the render:
  - put any join that dips 6 dB or more into `SHORT_SUS_LEG_SKIP` (Violins I needed three in c07);
  - refit the 23 shared onsets' legato leads on pcX against Violins I, target |difference| ≤ 30 ms.

## 4. The soft divisi pads are full-section chords; the half-section patches would fit "div." and "metà" (MANUAL-GAPS #7, open; troughs measured, gain inferred)

**Where.**
- Violas "div." pp, bars 47-59 (qn 184-236.5) and 62-68 (245-272): 10 and 13 two-note chords.
- Violins II "metà" pp, bars 47-54 (184-216).

The pads sit 14-18 dB under the master, under the celli's dolce tune, the horn and the harp.

**What is wrong.**
- **Full-section samples per voice.** Each chord note is a full-section Sus MAX sample with a -3 dB divisi cut (and `META_DB` -3 dB for metà). Each voice therefore sounds like a whole section (KIT §8: twice as thick as written).
- **Troughs at every chord change** (measured, violas stem). The chords re-attack every bar:
  - bars 48-54: 0.6-6.3 dB;
  - bars 62-67: 12.3 dB at 251, 6.6 at 255, 6.2 at 259, 8.8 at 267.
- **The patch that matches exists.** p.89-90: DIV A / DIV B are the left or right chair of every stand, Close only, "the loudness of a divisi part is not much less than if the whole section were playing the part". "Metà" is exactly one chair per stand (DIV A).

**Fix (second pass, where memory is free).**
- **Violas.** Upper voice to "Violas KS Master DIV A" by `TRACK_SPLITS` with "rank" (the c18 viola voices cross, KIT §8), lower voice to DIV B, both windows 184-236.5 and 245-272, `PASS2_TRACKS`, Violas resting there (`TRACK_WINDOWS`).
- **Violins II.** 184-216 on "2nd Violins KS Master DIV A" as an alias, with no `META_DB`.
- **Mix and legato.** Close only, send 0.5, as the Cello solo. Each voice is monophonic, so moving voices can use Leg BC joins instead of chord re-attacks.
- **Memory.** About 0.7 GiB per Close-only instance (c35 measured 0.68-0.75).
- **Measures:**
  - level per voice against c43's chord level;
  - troughs at the bar changes (target under 4 dB);
  - centroid and 2-5 kHz share (a half section is thinner);
  - loop check on the whole notes.

## Do not touch

- The re-bow machinery and its fitted fills on notes that stay held (dips and steps unchanged by CC16; the final chord's master is smooth). Change only the points named in finding 2.
- `STR_REP_DETACH` on the basses' eighth pedals.
- `WIND_REP_PORTATO`, `REP_ROW` and the LegRep / Leg Slur Rep spans on the winds and brass (their motif repeats are the target for the strings).
- `GENTLE_ACCENT` with keep_legato on slurred brass accents (2.4-5.8 dB, dark fronts).
- The bar-11 / bar-40 crescendo shapes.
- `SHORT_SUS_LEG` on Violins I with its three skips.
- The tremolo common-tone joins.
- Every c43 and earlier do-not-touch item.
