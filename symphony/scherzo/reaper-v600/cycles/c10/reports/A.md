# Cycle 10, critic A: articulation and phrasing (render c09)

All measurements use `cycles/c09/render/` (stems 01-31 after the Flute 2 stem fix, plus `00_Master.wav`) with `cycles/c09/build_render/parts.json` (the data that rendered) and its tempo map. "Stem" means a dry stem. "Master" means `00_Master.wav`. pcX is `tools/pcx.py` `attack_pcx`: the perceived attack, in ms against the score beat. Envelopes are RMS over 10 or 30 ms windows. Scripts were in `/private/tmp/claude-501/mockup-loop/scherzo-c10-A/` (deleted at the end).

## Manual notes (cycle 10 slot A: group A4, May 2021 HO manual PDF pp. 108-113, Hollywood Orchestral Woodwinds; plus MANUAL-GAPS.md)

| What the manual says (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| "Flute 2" is a different player in a different seat, with no shared samples, so a unison with Flute does not collapse into one sound (p.108) | Fl1/Fl2 unisons: the counterstatement pairs 121 / 127, the reprise 817 / 823, the sfp at 900 | Yes: two tracks on two patches. At the low unison pairs, though, Flute 2's row blurs (finding 5). |
| Instrument list: one oboe, one clarinet and one bassoon player (p.108-109; DIGEST 7.1 infers that 1/2 share samples) | Oboe 1/2, Clarinet 1/2, Bassoon 1/2 | Yes: `unison_dropped` Oboe 2 19, Bassoon 2 14. |
| Sustain dynamics "with the Mod Wheel" (p.109). This is Play-era text: in Opus CC11 sets the dynamic and CC1 the vibrato, except on the clarinet (2025 p.52; DIGEST 7.2) | every wind Sus / Leg note | Yes: CC11 dynamics, CC1 vibrato layer, clarinets in `CC1_DYN_TRACKS`. |
| Sus Expressive: slower attack and gently increasing vibrato (p.109) | the dolce / espress. lines: Clarinet 1's trio tune 153-168, Oboe 1 185-196, the codetta 225-236, the second idea 45-56 | Not used (MANUAL-GAPS #8). See finding 4. |
| Legato Repetitions (LegRep RRx4): a re-tongued attack for repeated notes inside a legato phrase (p.109-110); Legato Slur Repetitions (p.112) | slurred same-pitch repeats in the winds | Clarinets: yes (whole-piece "Leg Slur Rep"). Flute / oboe / cor anglais / bassoons: re-tongued on Leg Slur MAX or Sus MAX (`rep_retongued`). Example: Oboe 1 at 156 (bar 53, a new slur on the same pitch) falls into a 15-20 dB hole for about 0.3 s, pcX -127 ms. It is masked on the master, because the strings are 20 dB over the oboe there. |
| Short articulations have no release trails, only the room at the end of the sample: "be sure to hold the MIDI notes long enough to hear the natural reverberation" (p.110) | every printed wind staccato on "Stac DblTng RRx9" (Flute 1 121, Oboe 1 137, cor anglais 125, Clarinet 2 79, Flute 2 70) | **Not for the flutes**: the MIDI note-off cuts the sample at -2..-4 dB under its peak (finding 1). |
| Staccatissimo (StacSs), double tongue, Marcato RRx4, Shorts MOD SPEED (p.110) | the theme heads | Stac DblTng is in use. Oboe 2, Bassoon 1 and Clarinet 1 play their staccatos on Sus slices (c02 memory remap). The other rows are not used. |
| Runs, trills, flutter, repetition loops at fixed speeds (p.111) | none (no runs; the repeated eighths run at 528 per minute) | n/a (MANUAL-GAPS #15). |
| A legato slur forms only with no gap and within an octave: D3 to D4 slurs, D3 to D#4 does not (p.112) | every wind Leg row | Yes (measured on parts.json): no legato join wider than 12 semitones on any track, no chord sent to any Leg row, no same-pitch overlap. |
| Legato is monophonic by default; CC22 at 64-127 keeps it mono (p.112) | the 20 tracks with Leg rows | Yes: `LEGATO_MONO_CC22` 127 in the pre-roll since c09. The 2021 polarity on p.112 agrees with 2025 p.91. |
| Slur Runs give their strong slur only for steps of a minor or major second (p.112-113) | none | n/a. |
| Keyswitch Masters: switch rows by key (p.113) | all tracks | Not re-measured (c09: no keyswitch within 3 ms of a note-on). |

## Findings, ranked by what a listener would hear

### 1. Flutes: every staccato note is cut off by its MIDI note-off, a 7.5 dB step within 45 ms (measured; cause read from the manual)

Where: Flute 1 (121 staccatos) and Flute 2 (70) on "Stac DblTng RRx9", in every statement. The counterstatement (bars 29-44, qn 84-132) is the most exposed place, because Flute 1 leads the call and response there. In bars 29-36 the Flute 1 stem sits at about -40 dB (mp median -40.2) against a master of -39..-41 per bar. The tuttis (312-360, 912-960) and the coda build follow.

What is wrong: the staccato quarters are written at 0.5 of their value (0.114 s at quarter 264, eighths 0.057 s). On the flutes the note-off arrives while the recorded staccato is still at -2..-4 dB under its peak, so the release cuts the sample's own decay and the room at its end. The manual (p.110) says these rows have no release trails and that the MIDI note must be held long enough for the room to ring.

Evidence (stem level 25-5 ms before the note-off against 20-40 ms after it, staccato quarters):

| track | step at note-off, median (p25-p75) | n |
|---|---|---|
| Flute 1 | **7.7 dB** (5.3-11.1) | 75 |
| Flute 2 | **7.5 dB** (5.6-9.8) | 42 |
| Clarinet 2 | 4.7 (3.3-6.6) | 51 |
| cor anglais | 3.9 (2.4-5.3) | 85 |
| Oboe 1 | 1.5 (-1.4-3.3); phrase-end quarters 7 dB | 87 |
| Violins I / II / violas / celli | 2.3 / 2.6 / 1.4 / 1.9 | 70-216 |

- The median envelope of Flute 1's phrase-end quarters, relative to the note-off, reads -2 dB at -30 ms, -4 at -10 ms, -7 at 0, -10 at +20 and -15 at +40.
- The cor anglais at the same points falls smoothly at about 1 dB per 10 ms, with no knee.
- Neither CC11 nor vol_db changes at these note-offs (Flute 1 at 90.4 and 102.4: the lanes are flat until 90.5 / 102.5), so the knee comes from the note-off itself.

Fix (`tools/score_to_parts.py`, the generic `STAC_LEN_SPANS` block, plus `build/score_config.py`):
- Let a `STAC_LEN_SPANS` entry lengthen as well as shorten. Accept a 4-tuple `(from, to, frac, min_written_qn)`. For printed staccatos whose written value is `min_written_qn` or more, set `n["end"] = max(n["end"], min(n["qn"] + frac × written, next moved onset - 0.02 qn))`. Today the block can only shorten (`min`). Keep the 3-tuple behaviour unchanged.
- Set `STAC_LEN_SPANS["Flute 1"] = STAC_LEN_SPANS["Flute 2"] = [(0.0, 1128.0, 0.85, 1.0)]`. This holds the written quarters for 0.193 s instead of 0.114 s. Leave the eighths alone: the next note follows within 0.057 s, and the pair dips are already 7.1-7.3 dB.
- Optional second step after measuring: Clarinet 2 at the same values (4.7 dB step).
- Pass: median note-off step 3.5 dB or less on both flutes. Flute 1 / 2 pair dips stay 5 dB or more (median). Staccato pcX within ±20 ms (now -16..+15 per section). All staccato quarters still the same length in every section.
- Measured: every flute staccato quarter today has the same 0.114 s, so the change is uniform.

### 2. Bar 301 sfp: Flute 1 plays no sf (measured)

Where: qn 900 (bar 301), the tutti sfp < into ff at 304. Flute 1 doubles Violins I's A5 there.

Evidence (30 ms envelope; sf = peak over 900 ± 0.15 s; p = median over 900.9-901.9, before the accented 902):

| track | drop (dB) |
|---|---|
| Violins I | 16.4 |
| Violins II | 16.6 |
| violas | 20.0 |
| celli | 18.5 |
| basses | 17.5 |
| Clarinet 1 | 16.5 |
| contrabassoon | 16.2 |
| Bassoon 1 / 2 | 10.9 / 10.3 |
| Clarinet 2 | 10.1 |
| Oboe 1 | 8.4 |
| Flute 2 | 4.1 |
| **Flute 1** | **-0.2** |
| master | 12.4 |

Cause:
- Flute 1's 900 is an unslurred Sus MAX re-attack at v100, with a moved onset 0.04 s early.
- Its stem rises from -49 dB to -37 at +0.07 s and peaks at -32 only at +0.23 s.
- By then CC11 has already fallen from 114 to 46 (at 900.5-900.9, from parts.json).
- So the attack never reaches the sf level, and the line enters at its p level.
- Flute 2 and Oboe 1 start a slur at 900 and take Leg Slur MAX first notes, which speak faster.

Fix (`build/score_config.py`):
- `VEL_SET["Flute 1"] = {**VEL_SET.get("Flute 1", {}), 900.0: 118}`.
- `REATTACK_LEAD_AT["Flute 1"] = {**REATTACK_LEAD_AT.get("Flute 1", {}), 900.0: 0.07}`.
- If the sf still falls short, move the CC11 fall 0.25 qn later on this note only (a `LEVEL_SHAPES` +4 dB pre-hall is not available, so use the FP_SPIKE end for this track).
- Pass: Flute 1's drop 8 dB or more, the sf peak within 0.12 s of the beat, and Flute 2 / Oboe 1 unchanged.

### 3. Horns 1-2: the slurred tenuto repeats in the Trio's return are not re-articulated (S1; measured)

Where: bars 209-222 (qn 624-666), ff, the slurred tenuto dotted halves under the tune.
- Horn 2 same-pitch repeats: 627, 642, 651, 657.
- Horn 1: 630, 633, 663 (on 1FH "Port Lng", `REATTACK_LEAD_AT` 0.342 qn).

Evidence (10 ms envelope around the moved onset):
- Horn 2 at 627 / 642 / 651: the old note falls only 1-2 dB in its 70 ms MIDI gap (the 237 ms release fills it). The new note then bumps +3-4 dB. The stem reads as one held note with a small accent, not as a portato.
- Horn 1 at 630 / 633: a smooth 0.15 s sag from -38 to -45 dB, then a plateau at -42, with no new attack front. The 30 ms dip against the lower neighbouring body is 2.0 / 2.2 / 1.4 dB (663).
- c06 measured these Port Lng repeats at 5.4 dB. The target is 3-6 dB.
- Horn 2 at 657 dips 5.4 dB. That is the one in range.
- Audibility: the horns sit 12-15 dB under the master here (Horn 1 -39.4, Horn 2 -42.3, master -27.4 over 624-666), so they are inner voices. Inferred: the repeats are audible as merged notes in a section that is otherwise detached.

Fix (`build/score_config.py`):
- Horn 2: `WIND_REP_RETONGUE_BY["Horn 2"]` gap_s 0.07 -> 0.10 and frac 0.25 -> 0.30, with fall_cc 12 kept. Only in 624-666 if the global change moves the tutti repeats (they dip 7-14 dB already).
- Horn 1: end the notes before 630, 633 and 663 0.06 s ahead of the moved onset with `NOTE_END_AT` (`{"Horn 1": {627.0: 629.42, 630.0: 632.42, 660.0: 662.42}}`, the c09 breath method). Today's 5 ms gap comes from `REATTACK_LEAD_AT` (LEARNINGS c05).
- Pass: 3-6 dB dips at all seven, with no new hole over 8 dB.

### 4. The cantabile string lines join at the fastest legato velocities (inferred from the manual; velocities measured)

Where:
- celli trio tune, arco espress. p (169-184, qn 504-552)
- Violins I dolce espress. (177-184)
- the second idea (Violins I 132-168)
- the Trio's return (Violins I 624-672)

Evidence (parts.json legato targets per span):

| line | joins | target velocities |
|---|---|---|
| celli 504-552 | 30 | 106 / 112 |
| Violins I 528-552 | 14 | 106 / 112 |
| Violins I 132-168 | 15 | 118 / 124 |
| Violins I 624-672 | 30 | 118 / 124 |
| Clarinet 1 trio tune, Oboe 1 185-196, the codetta winds | | 80 / 100 |
| Violin I solo | | 82 |

- The HO true-legato scripts read velocity as transition speed: 110-127 gives the shortest slide, about 50-75 plays more of the recorded slide (T1 p.144; MANUAL-GAPS #8).
- Woodwind p.109: Sus Expressive has a slower attack for expressive lines.
- At quarter 228 these notes last 0.26-0.79 s, long enough for an audible slide.
- The join timings are fine (probe windows 66-91 ms), so this is about colour: the dolce / espress. lines sound like fast technical slurs.

Fix (an A/B on one line first, `build/score_config.py`):
- `LEG_VEL_SPANS = {"Violoncellos": [(504.0, 552.0, 80)]}`.
- Add 0.03 s to those targets' legato lead (`LEG_ART_EXTRA_S` or per-onset `leg_leads.json`). Movement I c37 measured that soft targets need 0.04 s more lead (LEARNINGS 588).
- Pass: celli 504-552 pcX median within ±30 ms, join window median 100 ms or less, no join dip over 5 dB.
- If it passes, extend at 80-90 to Violins I 528-552 and to the Clarinet 1 trio tune (its row has no Leg Slur Exp).
- Leave the ff return at 118 / 124.

### 5. Flute 2: the low unison repeated eighths blur into one note (measured; small)

Where: 121 / 121.5 and 127 / 127.5 (bars 41, 43), and the same figure in the reprise at 817 and 823 (bars 273, 275). These are D5 and F sharp 5 at v96, in unison with Flute 1.

Evidence:
- Flute 2's stem stays within ±1 dB for 0.25 s across both eighths. Stem pair dips are 1.8 / 0.6 / 1.0 / 0.6 dB.
- Flute 1 on the same pitches dips 5.1 / 11.4 / 2.8 / 8.1 dB.
- Flute 2's row takes about 0.1 s to reach its peak (-55 -> -39 dB at +0.10 s), so the second eighth arrives while the first is still rising.
- 127 and 823 replay the same round robins: the envelopes are identical to 0.5 dB (the c08 reprise lesson).
- Flute 2 carries only 6-9 % of the energy in these gaps, and the clarinets' held notes carry 22-24 %. The master gain is therefore small, but Flute 2 thickens and blurs Flute 1's articulation in the unison.

Fix:
- `build/note_trims.json` Flute 2: 121.0, 121.5, 127.0, 127.5, 817.0, 817.5, 823.0, 823.5 at -5 dB.
- `NOTE_TRIM_RAMP_S` 0.02 for those onsets.
- `RR_RESET_AT["Flute 2"] = [817.0]` (Opus's reset CC). This makes the reprise start one round-robin cycle apart from the counterstatement. Check that it changes the samples, not only the counter.
- Pass: Flute 1 + 2 sum dips 3 dB or more at all four pairs.

### 6. Violins I: the soft theme heads at 51 and 75 still drop their first slurred eighth (measured; the c09 open item, with the cause narrowed)

Where: qn 53 and 77 (bars 18, 26), the first eighth after the accented half note, Violins I (Leg Slur MAX target, v88). The quarter that follows is at 54 / 78.

Evidence (stem RMS over the first 0.2 s of each note):

| head | half note (dB) | first eighth (dB) | second eighth (dB) | following quarter (dB) |
|---|---|---|---|---|
| 51 | -37.2 | **-46.9** | -42.9 | -34.0 |
| 75 | -34.1 | **-44.5** | -43.9 | -32.9 |
| 39, 285, 759, 771, 795 (others) | | | | 1-9 dB under the quarter |

- The quarters at 54 / 78 are on "Stac RRx14". A regression on theme A and the counterstatement (row, vol_db and pitch as predictors, CC11 parked at 120) gives that row only +1.3 dB over Staccatissimo RRx9. So the gap is mainly the first eighth being low, not the quarter being loud.

Fix:
- `VEL_SET["Violins I"]` 53.0: 100 and 77.0: 100 (from 88). The legato velocity also speeds this first transition.
- Plus `note_trims` +3 dB with `NOTE_TRIM_RAMP_S` 0.02 on those two onsets.
- Pass: the first eighth within 8 dB of the half-note body and not more than 6 dB under the following quarter, with 39 / 69 / 285 / 7xx unchanged.

## Checked and fine (measured)

- **Staccato attack centres (S2).** Every wind and string staccato row is within -18..+15 ms per section, in the counterstatement, fugato, both tuttis, reprise and coda: Flute 1 -16..+7, Oboe 1 -8..-5, cor anglais -27..0, Clarinet 2 -13 / -12, Violins I -18..+3, Violins II -15..-2, violas -17..-1, celli -32..+7. The Sus-slice players read earlier: Clarinet 1 -28 / -39, Bassoon 1 -34 / -33, Oboe 2 -77 in the counterstatement (n 4).
- **Wind staccato pair dips (S1, stem medians).** Flute 1 7.3, Oboe 1 8.0, Clarinet 2 8.1, cor anglais 4.6 dB.
- **Master pair dips.** Violins I's 51 repeated-eighth pairs measure the same on c07, c08 and c09 (median change c08 -> c09 -0.01 dB). c09's higher sends did not fill the gaps. Where the master gap stays shallow (121, 127, 817), the clarinets' printed held notes fill it.
- **Legato data.** No join over an octave, no chord on a Leg row, no same-pitch overlap on any track (manual p.112).
- **Flute 1 "col Vl. solo" against the Violin I solo (1044-1068).** Flute minus solo pcX median -7 ms (IQR -22..+34), n 19.
- **Harp.** The non arpegg. chords are simultaneous (0 ms spread, v40-50) in 81-84, 153-168, 185-192, 225-238 and 341-348. The arpeggios at 708 and 1080 spread 80 / 200 ms.
- **Re-bows.** Violins I's held G sharp: dips 2.0-5.8 dB, steps -2.2..+0.7 dB.
- **Masked inner holes.** The violas' ppp repeated E's under the solo (1047, 1050, 1053: 10-15 dB holes after each Sus MAX v38 re-bow) and the celli's pp portato at 618 (14 dB) sit 13-15 dB under the master, which stays flat within ±1.5 dB there.

Do not touch: the wind and string short-row leads and the eighth lengths (pair dips and S2 above); the c08 reprise row split; `SHORT_CC11_PARK` and the downbeat weight; the c09 `SHORT_SUS_LEG_AT` head tails (only 51 / 75 get more, finding 6); `LEGATO_MONO_CC22` and the full legato rebuild; the celli `JOIN_NOTCH` pair; the Horn 1 breath at 648; the harp's chords, arpeggios and étouffez; the timpani roll ends and `TIMP_DAMP_AT`; the Violins I re-bow fills; and every item in HISTORY's c09 do-not-touch list.
