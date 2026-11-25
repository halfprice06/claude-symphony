# Cycle 6, critic C (dynamics over time), on the c05 render

Render under review: `cycles/c05/render` (stems and master after the crash / bass drum stem fix) and `cycles/c05/rendered_build/parts.json`. Levels are stereo power on the stems and master, placed on the parts.json tempo map with `tools/pcx.py` TM. CC values are read from the parts.json lanes as REAPER plays them: held steps. The dynamics lane is CC1 on `CC1_DYN_TRACKS` (horns, trumpets, trombones, tuba, Clarinets 1-2) and CC11 on every other track. Phrases come from `build/mockup-events.tsv`. A phrase is a run of notes in one staff, bounded by a slur start, a breath mark or a printed rest, plus any played gap over 0.25 s. Short rows (staccato, pizzicato, Marc Shrt) are left out. Percussion, timpani and harp are excluded, and only phrases of 2 s or more count. That gives 713 phrases, 336 of them with no printed hairpin. Each judgement is marked measured or inferred.

Sources read: BRIEF.md, including "EastWest template mix" and research batches 2-4; `mockup-kit/EW-TEMPLATE-PLAN.md` sections 5-8; HISTORY.md; c05 CHANGES.md and CARRYOVER.md; my lens's c02 report; Movement I HISTORY c46-c48 (release caps, `rt_gain_db`).

## Manual notes (MANUAL-READING row c6 C: May 2021 HO manual PDF pp. 44-45 and 134-136, read in full; MANUAL-GAPS.md read)

| What the manual says (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| MIDI channel modes: MULTI sends CC1, CC11 and pitch bend only to the voices on the controller's channel; MPE sends per-note messages; OMNI applies CC1 and CC11 to every channel; 1-16 gives one channel per instrument (p.44) | Each of the 31 tracks is one Opus instance with one CC lane per controller, so a CC shapes every voice on the track. That includes chords on one track, such as the violas' div. chords at 184-199 and the div. a 3 tremolo at 278. | Yes, as one channel per instrument. Divided voices cannot be shaped separately. That only matters if the phrase rule (finding 1) is to shape two divisi lines differently, and none of the findings below needs it. |
| CC1 "commonly" crossfades dynamic and/or vibrato layers, sets volume or switches articulations. CC11 sets volume, or the dynamics when CC1 drives vibrato (p.45) | Strings and most woodwinds: dynamics on CC11, CC1 on vibrato. Brass and clarinets: dynamics on CC1 (BRIEF "Facts"). | Yes. This matters for findings 1-2: a phrase swell on the dynamics lane changes the layer, so soft passages get softer in timbre as well as level. In c05 that lane is flat over most phrases (finding 1). |
| Play page and Player window: Mood, Performance scripts, Sensitivity and MIDI control (velocity and CC response), Envelope (each instrument's volume envelope) (pp.134-135) | `build_reaper.py` sets the envelope releases in the Opus state (`cap_release`, `env_release_ms`). Sensitivity curves are left as shipped. | Yes. The envelope release is the setting behind the violas' fast soft ends (finding 3). The shipped CC11 response is gentle: from my stem regression on held notes, about 0.18-0.2 dB per CC unit on violas and violins between CC11 30 and 128. |
| Moods: Classic (Main mics, a 3.4 s Southern California hall), Soft ("slower, more emotional passages", Mid plus Surround/Vintage mics, Abravanel Hall), Epic (Close + Main + Surround, a 2.8 s cathedral). Moods change the mic mix, the reverb and the MIDI Compressor (p.136) | The second theme (51-66, 171-186), the bassoon solo (115-126) and the p-pp transition (43-50) are where a Soft mood would be used. | Not used, and it should stay that way. The pipeline sets mics and reverb itself, and c06 replaces both with the EW template layout and the Spaces returns. The Soft mood's mic change would undo that layout. Page 136 does not mention con sordino. Soft passages therefore get their soft timbre only from CC layer choice and phrase shape (findings 1-2). MANUAL-GAPS line 205 ("Moods ... not applied") stands. |

## State through this lens on c05 (measured; what c06's mix change must not lose)

- **Arc.** Bar levels from metrics.md: 223 -10.0 dB, 278 -10.5, 279 -11.0, 262-263 -11.6 / -11.4. The final chord's head (qn 1108-1109) is -9.1 dB against -11.1 for bar 277's accents and -9.5 for 223's head. That meets c02's target of +2 dB over 277 and within 1 dB of 223. Bar 263's downbeat is +0.8 dB over 1047, against a +1 target.
- **Builds.** 209 (fp) -25.2 -> 210 -19.6 -> 211 -17.8; 219 -30.6 -> 221 -21.0 -> 222 -16.0 -> 223 -10.0; 243 -23.0 -> 247 -17.0; 271 -17.6 -> 278 -10.5.
- **Delivered mp3.** LRA 14.7 LU, p10-to-max span 18.9 dB, limiter 2.0 dB: inside the BRIEF item 6 targets.
- **Loop pulsing (BRIEF item 7).** I folded the 100-300 Hz level and the spectral centroid at 3.95 s (autocorrelation of the detrended 50 ms series). Master 888-936 +0.05 / -0.04; master 1088-1113 -0.08 / -0.16; celli, Violins I and basses over the chorale (892-936) at or under +0.06; timpani roll 1088-1112 -0.02 / -0.11. No pulsing.

## Findings, ranked by what a listener would gain

### 1. Phrases have no swell and no arch: the dynamics lane is flat after almost every phrase start (measured; fix for c07's performance-data cycle)

**Rule (BRIEF, EW-TEMPLATE-PLAN §6-8).** The swell starts after the first onset (about +15 CC by 0.4 s, +25 by 0.8 s). The arch peaks at 33-62% of the phrase, with a range of 30-60 units on long phrases. Long notes keep moving.

**What c05 does.** The pipeline shapes single notes, not phrases. `score_to_parts.py` contour() adds "swell" (+4 CC at 40% of a note of 1.8 s or more, -2 at its end) and "taper" (-6 over the last half of a phrase-final note). It skips any note that is inside a hairpin, has an onset inside it, or follows a same-pitch note. The volume envelope adds `SWELL_DB` (+1.5 dB at 40% of the note).

| family (phrases of 2 s or more) | n | CC rise by +0.4 s / +0.8 s, median (IQR) | rise of 15 or more by 0.8 s | phrases with range under 4 CC (flat) | shaped phrases peaking at 33-62% | range on phrases of 4 s or more, median (IQR) | without a hairpin |
|---|---|---|---|---|---|---|---|
| strings | 166 | 0 / 0 (0..0) | 2% | 23% | 42% | 39 (12..68) | 4 (4..10) |
| winds | 311 | 0 / 0 (0..+2) | 1% | 23% | 45% | 22 (7..39) | 6 (0..12) |
| brass | 236 | 0 / 0 (0..0) | 1% | 47% | 20% | 12 (0..44) | 0 (0..0) |

- Only 20% of all phrases rise at all in their first 0.8 s. The largest rise anywhere is 26-40 units, and it always comes from a printed crescendo.
- No phrase meets all three parts of the rule: swell, mid peak and taper. One brass phrase comes close.
- Where a phrase has any range, the printed hairpins supply it. Without a hairpin, the median range is 0-6 units. At the measured 0.18-0.2 dB per CC that is at most about 1 dB, and the layer does not change.
- Of the shaped phrases, 26% peak in their last 15%. That is the end-weighted shape the rule avoids.
- On the stems, the level from 0.15 s to 0.8 s rises a median +1.7 dB. That rise is the samples' own attack build, not a phrase swell. Stem peak positions fall at 33-62% in only 25% of phrases.

**Exposed soft lines where this is heard most** (CC lane, stem):
- **Trumpet 1, dolce cantabile solo (sq 200, 216, 251; bars 51-66).** CC1 is a flat 42 over all three unhairpinned phrases: range 0, swell 0, taper 0.
- **Cor anglais with the muted Trumpet 1 (sq 680, 696, 731; bars 171-186).** Range 2, 4 and 6 units.
- **Clarinet 1 (sq 200, 232).** A flat CC1 of 28 for 13 s each.
- **Horn 1 at 984 (Più allegro).** Flat at CC1 108, which is ff and has little room to swell anyway.

**Fix (c07, as BRIEF schedules it).**
- **New generic contour.** Add a phrase contour to `tools/score_to_parts.py`, defaulting to off: `PHRASE_SHAPE = None`, read inside `contour()` and so written to whichever lane carries the track's dynamics.
- **Phrase boundaries.** Use the ones measured here: slur starts, breath marks, printed rests and played gaps over 0.25 s. Shape only phrases of 2 s or more.
- **Offsets, in CC units relative to the printed base.**
  - -12 at the first onset;
  - +3 at +0.4 s and +8 at +0.8 s (a rise of +15 / +20);
  - a peak of +10 at 45% of the phrase, kept inside 33-62%;
  - +4 at 1 s before the last note-off and -12 at the note-off: a taper of about 16-22 units over the last second, which is the subject of finding 2;
  - on phrases under 3 s the rise and taper meet at the 45% peak.
- **Mean level.** The printed dynamic stays the phrase mean, not its floor.
- **Scale by printed dynamic:** pp 0.8, p-mf 1.0, f 0.6, ff 0.35, fff 0.2. The loud layers have little headroom (HP_SWELL_CEIL), and the arc above must not move.
- **Floor and caps.** CC never goes below 8. Apply the existing `SWELL_CC_CAP` pitches, so the bassoon, bass clarinet, contrabassoon and clarinet layer jumps stay capped.
- **Hairpins override.** Fade the contour's weight to 0 over 0.25 s at a printed hairpin's start, and back after its end.
- **No double shaping inside shaped phrases.** Drop the per-note "swell", "swell_taper" and "taper" contours and the `swell_db` volume rows. Keep "bloom", "bcsoft", "swell_sost" / `ARRIVAL_HOLD_SPANS` and every fill.
- **Finale config** in `build/score_config.py`: `PHRASE_SHAPE = {"families": ("string", "wind", "brass"), "min_s": 2.0, "start": -12, "rise": [(0.4, 3), (0.8, 8)], "peak": (10, 0.45), "pre_end": (1.0, 4), "end": -12, "scale": {"pp": 0.8, "p": 1.0, "mp": 1.0, "mf": 1.0, "f": 0.6, "ff": 0.35, "fff": 0.2}, "floor": 8}`.
- **Expected size (inferred from the CC response).** About ±2.5 dB on strings and woodwinds, plus a layer change. Brass get a layer crossfade from CC1.

**Things to re-check after the change.**
- Entry leads and early fills fitted on c05 attacks may move a little, because each phrase now starts about 2 dB lower (inferred). Check the attack probe and pcX on the solos.
- The per-dynamic stem medians in metrics.md should stay within ±1 dB of c06's.

**Targets.** On phrases of 2 s or more with no hairpin in their first 0.8 s:
- 70% or more rise +12..+20 by 0.8 s;
- 70% or more of shaped phrases peak at 33-62%;
- 25% or fewer flat.

### 2. Phrase ends do not taper: 30% fall at all in the last second, 3% by 13 units or more, and the stems rise into the end as often as they fall (measured)

**Rule.** A taper of about 20 units over the last second (13-37 in the EW template).

**c05.** CC fall over the last second, last note-off minus 1 s:

| family | falls at all | falls 13 or more | rises into the end | stem, last second (level at -1.0 s minus level at -0.2 s): median, IQR, share rising |
|---|---|---|---|---|
| strings | 38% | 2% | 25% | -0.6 dB (-3.8..+1.6), 57% rising |
| winds | 39% | 4% | 17% | 0.0 dB (-2.5..+1.6), 51% rising |
| brass | 12% | 3% | 14% | +0.2 dB (-1.4..+2.2), 45% rising |

- **Exposed ends.**
  - Trumpet 1's solo phrases: the stem rises 0.4, 2.6 and 5.8 dB into the ends at sq 200, 216 and 251. The last one is the theme's close at bar 66.
  - Bassoon 1's last solo phrase (sq 496, bars 124-126): rises 4.5 dB, with the stem peak at 95% of the phrase.
  - Violoncellos 321 (bars 81-82, 14 s): CC rises 10 units in the last second. A crescendo is printed there.
- **Why it matters here.** A soft phrase that does not thin out before its note-off ends on the sample release alone. That release is fast on the violas (finding 3) and will be drier from c06 on (finding 5). In a real orchestra the bow lightens before it lifts.

**Fix.** The `pre_end` / `end` points of finding 1's `PHRASE_SHAPE`. Two conditions:
- Skip the taper where the phrase's last note carries a printed crescendo or arrives on an accent or sf.
- At the final notes of sections that stop short, such as the ff cut-offs (tutti stop chords, bar 94 or 113), scale the taper by the same per-dynamic factors (0.35 at ff), so the measured tutti cut-offs do not soften.

**Targets.**
- Stem median last-second fall of 2-4 dB on soft and mid phrase ends; it is 0 now.
- Tutti cut-offs on the master unchanged: 0.41-0.50 s to -20 dB.

### 3. The violas' soft ends still stop in 0.05-0.14 s: their legato row ships sustain groups the 500 ms cap cannot lengthen, and a weaker pp release trail than the violins (measured; fix partly inferred)

**Where.** Violas, qn 198.88 (bar 50, pp, the end of the poco rit. before the second theme) and 454.86 (bar 114, pp, the chord before the bassoon solo). Both ends are on Leg Slur MAX.

**Evidence: fall on the stem after the note-off, 10 ms frames.**
- 454.86: the body is -51 dB. The stem is -59 at the note-off, -64 at +0.06 s, -71 at +0.15 s, a release-trail bump to -67 at +0.21 s, and -85 by +0.42 s. In seconds: -10 dB at 0.05-0.07 s and -20 dB at 0.32 s, against the references' 0.20-0.40 and 0.43-0.58 s.
- 198.88: -62 to -74 by +0.15 s and -85 by +0.24 s.
- On the same 454.86 end, Violins II holds -52..-55 until +0.15 s and reaches -10 dB at about 0.17-0.26 s. The fall begins about 0.1 s before the note-off (-51 -> -59), while CC11 moves only 16 -> 12. That is about -1 dB on the measured response, so most of the pre-note-off drop is not the CC.
- c02, with no cap at all, already measured the violas at 0.11 / 0.31 s. So the cap is not the main cause.

**What ships under the cap** (read from `Violas KS Master.oib` with a scratch copy of opus_state.py):
- `cap_release` only lowers a release. It never raises one.
- The Leg Slur MAX row carries "V1s pp" and "V1s p" sustain groups at 237 ms. They are untouched by the 500 ms cap; the c05 build log lists only their 931 / 524 ms siblings as capped. Beside them sit "1V pp" (931 -> 500) and "1V p" (524 -> 500).
- On the same row, the Violas' pp release-trail groups ("1V pp RT", 1245 ms one-shots) carry a source volume of 1.37. Violins II's carry 2.25, so the violas' trail is 4.3 dB lower.
- That matches the stem: the violas' trail bump sits 15-18 dB under the body, against about 8-10 dB for Violins II.

**How audible (measured).** On the master both ends are partly covered.
- At 454.86 the master falls 10 dB in about 0.3 s, because Violins I sounds on to 455.86 and the hall rings.
- At 198.88 the violas are 17 dB under Violins I.
- What a listener hears is the viola voice of the chord switching off under the violins, more than a hole in the master.
- Ranked third because the fix is cheap and c06 rebuilds the Violas track anyway.

**Fix.**
- (a) **`build/mix.json` Violas `sus_release_cap_ms.ms`: drop "pp".** The 1V pp groups go back to their shipped 931 ms. Keep "p" 500. This matches Movement I c47 ("no pp cap" on Violins II, Violas, celli and basses, 350 ms at p). There it moved the master's final chord from 0.12 / 0.33 to 0.21 / 0.61 s.
- (b) **Generic floor in `tools/build_reaper.py` `cap_release`.** Add an optional `"min_ms"` dict keyed like `"ms"`, e.g. `{"pp": 500, "p": 400}`, that raises shorter shipped releases on the listed rows and dynamics, TLeg and RT excluded. The Violas' V1s pp / p groups then release over 500 / 400 ms instead of 237.
- (c) **Optional, and only with a join check.** Port Movement I's `rt_gain()` (`symphony/mvt1/reaper-v621/tools/build_reaper.py` line 276), extended with a `"dyn"` filter. Give the Violas' pp RT groups on Leg Slur MAX +4 dB (1.37 -> about 2.2, the Violins II value). Movement I lowered the Violas' trails by 6 dB to cut the old pitch at running legato joins (f figures). A pp-only gain leaves those joins alone, but measure the violas' pp chord changes for old-pitch hold (Movement I c47 method) before adopting.

Each of these is an Opus state change. c06 fully rebuilds every track anyway.

**Targets** (on the Violas stem plus its string return, see finding 5):
- 198.88 and 454.86 at -10 dB in 0.15 s or more and -20 dB in 0.40 s or more;
- f-ff viola ends unchanged at about 0.12 / 0.32 s.

### 4. The sfp of bar 149 lands about 0.27 s late as a swell: brass notes start at p before the spike, and the strings' sf ends before their attack (measured)

**Where.** qn 592 (bar 149, sfp < to ff at 596), every brass, timpani and string staff. The note is tied into 592 and re-attacked.

**Evidence: master at 1/8-qn steps.**

| qn | 591.0-591.5 | 591.88 | 592.0 | 592.12 | 592.25 | 592.75 | 593.75 | 596.5 |
|---|---|---|---|---|---|---|---|---|
| master dB | -13 | -18 | -16 | -20 | -19 | -12 | -24 | -11 |

- Window means: 590.5-591.5 -13.3 dB, sf window 592.0-592.25 -19.1 dB. The sf is 5.8 dB under the ff before it.
- The loudest moment of the bar is at 592.75, 0.27 s after the beat at about 163 qpm. Trombone 1 shows the same shape (-22 -> -38 at 592.25 -> -24 at 592.75), and so does Horn 1 (-28 -> -37 -> -27).
- **parts.json, brass.** Trombone 1's re-attack is led to 591.86 and Horn 1's to 591.748 (re-tongue leads). The re-tongue fall puts CC1 / CC11 at 42 / 46 at that note-on. The spike (CC1 108, CC11 114) is written at the score position, 592.02. So each brass note starts on the p layer for 57-97 ms, and the 120 ms CC1 layer crossfade carries the sf in late.
- **Violins I.** Note-on at 592.0 with CC11 52, spike to 120 at 592.02, held to 592.33. The stem still falls -26 -> -37 by 592.25: the Sus MAX attack has not reached its body before the 0.12 s hold ends.

**Fix.**
- `tools/score_to_parts.py`, fp/sfp branch (around line 1775: `pts += [(q, level), (q + 0.02, ...)...]`): write the spike from the note's moved onset. For each track, take the earliest moved `qn` among notes with `sq == q`, start the spike 0.005 qn before it, and shift the hold and fall points by the same lead. Also stop the re-tongue CC fall from returning below the spike value after that moved onset. Generic; a flag `SPIKE_FOLLOWS_LEAD = True` is enough.
- Make `SFP_SPIKE_S` accept a per-family dict in `build/score_config.py`: brass and winds (0.12, 0.30), strings (0.20, 0.40). The string hold has to outlast the Sus MAX attack (inferred from the stem shape).
- The fall stays in CC (S3).

**Targets.**
- Master 592.0-592.25 within -1..+2 dB of 591.0-591.5.
- No later peak over the sf before the crescendo.
- At least 8 dB under the sf by 592.75.
- 2-5 kHz over the first 80 ms not more than 4 dB over the body (BRIEF item 4).

### 5. c06's dry stems will make every soft-end and decay check read wrong unless the return stems are added; and the c05 arc is the baseline to keep (inferred, with the c05 numbers measured)

**Why.** From c06 the Opus reverb is off and the hall is in the Spaces II return stems (BRIEF "EastWest template mix"). A per-track stem will then hold no room. The release-time numbers in finding 3 above, in c05's critic C report and in the c05 CHANGES table were all measured on wet stems. Measured on the c06 dry stems they would look worse even if nothing changed: roughly the c04 figures, with 0.06-0.09 s to -10 dB.

**Fix (measurement protocol for the c06 actor and c07 critics; no REAPER work).**
- Run `actor_scripts/softends.py` and `tutti.py`, and any decay check, on each string stem plus its family return stem summed at render gain, or on the master.
- State in CHANGES.md which method was used.
- Re-measure the c05 baselines above on the c06 master after the delivery refit:
  - 278 head at least +2 dB over 277's accents and within 1 dB of 223;
  - 263 downbeat at least +1 dB over 1047;
  - builds 219-223, 243-247 and 271-278 rising as listed in "State";
  - delivered LRA 14-16 LU, span 16-19 dB, limiter at most 3 dB;
  - no fold over +0.20.
- Treat a fall in any of these as a mix regression of the reverb, EQ or delivery change, not of performance data.

**Do not touch:**
- the per-dynamic string caps at mf-ff (150 / 300 ms; tutti cut-offs 0.41-0.50 s to -20 dB);
- the c02-c03 final-chord and arrival work (278 head -9.1 dB, +2.0 over 277; 223 the loudest bar);
- `HP_GAIN_*` / `hpgain` printed-hairpin ramps, which carry all the phrase range there is now (keep them as the override in finding 1);
- the crash / bass drum damp at 1113.2;
- no pulsing anywhere: keep `AUTO_REBOW` and `space_rebows`;
- the delivery chain targets as met in c05: LRA 14.7, span 18.9, limiter 2.0.
