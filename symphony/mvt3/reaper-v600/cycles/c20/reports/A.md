# Cycle 20, critic A: articulation and phrasing (on the c19 render)

All numbers were measured on `cycles/c19/render/` (stems and master), `cycles/c18/render/` for comparison, `build/parts.json` (the c19 data), `cycles/c19/before/parts.json` (the c18 data) and the installed `.oib` patch files (read as JSON, nothing written). Stems are post-fader; where notes are compared, the `vol_db` value at the note was subtracted. "Measured" means a number from these files; "inferred" means a conclusion I could not check without a render. Nobody heard the audio. No per-note track volume move is proposed anywhere below.

Not measured this cycle: harp (harmonics at 43, étouffez, glissando at 277), timpani roll loop pulsing, divisi / "4 soli" / sul tasto passages, the muted Trumpet 1 joins, the 89 envelope plateaus, the climax order (lens B / C).

## Manual notes

Third round: pages behind the top open problems, read in full (May 2021 HO manual, PDF page = printed page).

| Manual (PDF page) | Where it applies | Does the render follow it |
|---|---|---|
| p.92, Pizzicato: every section has a round-robin pizzicato with 2 or 4 samples per note | Violoncellos "Pizzicato RRx4", bars 51-66, 115-122, 171-186 | Partly. The c19 CC16 reset before every pluck makes each pluck play one take. The patch file shows that the four takes cover different key ranges, so the c18 per-pitch region gains miss some of the notes. See finding 4. |
| p.93, Marcato: short notes with a strong accent, 4 round robins | candidate row for the basses' eighths | Not used ("Marc Shrt RRx4" was tested in c16: 8.0-11.0 dB separation). Variant V3 of finding 1. |
| p.94, Staccato On Bow: "the bow ... comes to a full stop", a distinctive stopping sound; Staccatissimo is shorter | Double basses' eighths, 199-210 and 247-277 (320 notes) | The row matches the description. It does not separate the eighths, and the cause is in the patch file, not in the note lengths (finding 1). |
| p.94, Repetitions: not round-robin, has release trails; end the note early for fewer repetitions | candidate for the basses' eighths | Not suitable. The basses' "Repetitions TS" row is synced to tempo, and bars 205-210 accelerate. |
| p.102 (brass) and p.110 (winds): short rows have no release trails, only the room at the end of the sample; hold the last note so the room can ring | the basses' short rows; the trumpets' eighths | The basses' short rows carry an extra group the manual does not mention (finding 1). The basses have no hall send (`return: null`), so all of the ring between their strokes comes from the samples. |
| p.109, Sus Expressive: slower attack, vibrato that grows | not a candidate for the cor anglais | Not used, and it should not be: it would make the bloom of finding 2 worse. |
| p.112, woodwind legato: a slur only when there is no gap; within an octave; monophonic (CC22 below 64 for polyphony) | cor anglais solo 171-186 | Followed: no chords on the legato row, and every target overlaps. The fault is the target's own shape (finding 2). |
| p.102 (brass, by implication: only the short rows lack release trails) | trumpet phrase ends and stops (814) | Not followed. The trumpets' sustain notes end with no audible trail (finding 5). |

MANUAL-GAPS items touched: the basses' short rows (Marc Shrt, Staccatissimo, Spiccato, p.92-94; still "not tried", item 353) are finding 1. The row volume knob does not act (c19 learning), so `row_volume_db` Tremolo -3 / -4 on the violins is inert (see "Other checks").

## Findings, ranked by what a listener would gain

### 1. The basses' hammered eighths do not separate because of how the row is built: one stroke's tail is still within 4-6 dB of the next stroke's peak, whatever the note length (measured; the fix values are inferred until a range test)

Where: Double basses, "Stac On Bow RRx9", qn 792-840 (bars 199-210) and 984-1088 (bars 247-270). They are the only hammered eighths in these bars; the timpani strike on the beats.

Measure: for every same-pitch eighth, the stem level (40-3000 Hz, 15 ms window) in the 40 ms around the moved note-on, against the new stroke's own peak in the next 150 ms. This is how far the previous stroke has decayed when the next one starts.

| span | c18 (45 % of the slot, lead 0.04 s) | c19 (70 %, lead 0.075 s) |
|---|---|---|
| 792-816 | -4.4 dB, 26 % of strokes within 3 dB | -4.6 dB, 29 % |
| 816-840 (accelerando) | -4.3, 40 % | -3.7, 38 % |
| 984-1056 | -7.1, 18 % | -6.5, 21 % |
| 1056-1088 | -4.4, 38 % | -4.2, 38 % |

The note length went from 45 % to 70 % of the slot and nothing changed (within 0.7 dB). The note-off does not end the stroke. The median stroke shape, aligned at the note-on, stays within 1-2 dB of its level for 330 ms, which is almost two eighth slots (0.179 s each). In 816-840 the on-beat peak reads +78 ms and the off-beat strokes have no peak of their own: they are masked, so the line is heard as one pulse per beat. For comparison, the timpani's strokes reach 3 dB under their peak 20-26 ms after the beat, with a 5 ms spread.

Cause (read from `Basses KS Master.oib`):
- The main groups of "Stac On Bow RRx9" ("Db Stac Hrd", 4,810 regions) have AHDSR decay 749 ms to 0.008 and release 749 ms. A 0.125 s note-off therefore takes only about 1 dB off the stroke.
- The same row also carries a group named "release extension" (645 regions). It plays the plain "Db Stac f" takes at source volume 1.47 (+3.3 dB), with attack 656 ms and release 1,330 ms. It is triggered with every stroke, so a second staccato take fades in under each note and rings on for 1.3 s.
- "Spiccato RRx9" has the same extension group. "Staccatissimo RRx9" has its own ("Db Stac" groups: attack 466 ms, hold 1,000 ms, release 2,541 ms, volume 1.14). "Staccato RRx9" has decay and release of 1,330 ms. "Marc Shrt RRx4" has no extension and a 316 ms release.

`tools/build_reaper.py cap_release()` cannot reach these groups. It caps a group only when the last word of its name is a dynamic (pp / mf / f / ff), and these groups are named "Db Stac Hrd rrx1" and "release extension".

Fix (Opus state, so a full rebuild of Double basses):
1. Silence the extension. In `build/mix.json`, Double basses `region_gain_db`, add `{"rows": ["Stac On Bow"], "groups": ["release extension"], "all_db": -60}`. The existing `groups` filter of `region_gain()` already supports this.
2. Let the note-off end the stroke. Extend `cap_release()` with a spec key `"any_dyn": true`, which drops the dynamic-word condition but still skips "RT", "TLeg" and type-3 groups. Allow `sus_release_cap_ms` to be a list of specs, and add `{"ms": 90, "rows": ["Stac On Bow RRx9"], "any_dyn": true}` for Double basses.
3. In `build/score_config.py`, on the basses' short-row spans: note length 60 % of the slot (0.107 s at 168 quarters per minute; research batch 7 gives 50-62 %) and lead 0.10 s (the c19 peak is +39 ms at a 0.075 s lead; 0.12 s, the L12b variant, would put it 35 ms ahead of the timpani).
4. Range test, basses alone, bars 199-204 and 247-252, three variants: V1 = step 1 only; V2 = steps 1-3; V3 = "Marc Shrt RRx4" with the same 90 ms cap and a CC16 reset at each span start. Pass if the level at the new note-on is a median -10 dB or lower under the new peak, no stroke is within 3 dB, and the -3 dB point of the rise lands within 20 ms of the timpani's (+20..+26 ms). If V2 sounds too dry for a hall (no basses send), raise the cap to 150 ms before going back to the extension.
5. Do not use "Repetitions TS" (synced to tempo, not round-robin; bars 205-210 accelerate). If "Staccatissimo RRx9" is tried, its extension is filtered with `"groups": ["Db Stac rr"]`.

### 2. Cor anglais solo (bars 171-186): every slurred long note blooms 5 dB after the beat; the c19 CC11 shape cannot remove it (measured)

Where: Cor anglais, "Leg Slur MAX", legato targets of 0.6 s or more at qn 688-740 (692, 704, 706, 708, 720, 728, 738, 740). Trumpet 1 con sordino doubles the line.

Stem level in [beat -0.05, +0.10 s] against the peak in [+0.2, +0.6 s] (100 ms window, fader removed): median +5.3 dB (+4.9 to +6.7 on 8 of 9 notes). Trumpet 1 ("Mute Sus") on the same notes: -0.8 dB. So the cor anglais swells every note against a flat partner. CC1 is constant (100) on these notes, so this is not the vibrato crossfade.

The c19 shape (CC11 -9..-10 units with its lowest point 0.36 s into the note) took the bloom from c18's 5.3-7.5 dB (median about 6.2) to 4.9-6.7 dB (median 5.3). That is about 0.9 dB for 10 units, about 0.1 dB per unit in this window. Removing the remaining 3 dB this way would need CC11 near 20-30 on a line at 44-54, which is the soft-layer boundary (kit LEARNINGS section 4). CC11 is not the route.

Fix (instrument side, one track, range test 676-748):
- Variant A: the legato targets of the solo at velocity 118 (now 80-90). The EWSO LegatoSpeed script maps velocity to a sample start offset of up to about 100 ms, so the slow first part of the target is skipped (inferred effect; measure it).
- Variant B: the targets of 2 qn or more on "Sus Max" at velocity 100, the old note ending 0.04-0.05 s after the new moved note-on (the c19 chorale method on polyphonic sustain rows), with the CC11 lane unchanged. "Sus Max" new notes at velocity 111 rose only +0.8..+1.8 dB in their first 0.4 s (qn 0, 16, 584); at velocity 73-91 they rose 3.4-5.5 dB.
- Keep a variant only if the beat-to-peak rise falls to 2.5 dB or less and the join dip stays at or under 4 dB (c19: median 1.5 dB on a 200 ms window). Remove the -10 unit `note_shape` on this span in whichever variant is kept.

### 3. Horn 1's chorale entry (bar 223) is 5.7 dB quieter because of c19's C5 region gain, not the bar-224 level step (measured)

Horn 1 stem per 4 qn, c18 against c19, with the same notes, velocity 127, CC1 120, CC11 112 and fader +4.0 dB at the fff C5 of qn 888: 888-892 -26.7 -> -32.5 dB (-5.7). The rest of the chorale is within 2 dB (892-900 +1.2..+1.7, 904-932 -0.4..-2.7). So the "3-4 dB over 888-936" is almost all this one note.

c19 added `region_gain_db` `{"rows": ["Sus MAX"], "pitch_db": {"72": -3.5}}` to Horn 1 (c19 critic A had measured "C5 +5.1 dB" on notes at CC1 119, that is, fff arrivals), plus `gain_db` 2.0 -> 1.2. The breath step at 891.79 (c19 `vol_step_at`) only moves the -1 dB point 0.04 qn earlier; c18 reached the same -1 dB by 893.5.

Fix: delete the C5 entry from Horn 1's `region_gain_db` in `build/mix.json` (Opus state, so a full rebuild of Horn 1). That gives back 3.5 dB at 888. The remaining 1-2 dB is the gain change and "Mono From Left"; leave it to B. A C5 that is hot at fff is the printed dynamic, not a sample fault.

### 4. Celli pizzicato: the per-pitch gains miss some notes, because the round-robin take played after each reset shares regions between keys (measured; which take plays is inferred)

After c19's CC16 reset before every pluck, each key plays the same level every time. All plucks are at velocity 41 and CC11 34, with the fader flat within 0.5 dB in each passage. The range is still 9.3 / 8.9 / 7.6 dB in 200-264 / 456-488 / 680-744. Deviation per key from the passage median (immediate repeats excluded): 47 -5.1 and 48 -5.2 dB (identical, although their current gains differ by 4.5 dB: +1.3 / +5.8), 41 -4.8, 38 -2.0, 46 +4.3, 44 +2.1, 43 +1.7, 55 +1.4, 54 +1.4, 57 +2.5, others within 1 dB.

In `Celli KS Master.oib` the four takes cover different keys. In take rrx2 the keys 47 and 48 share one region (root 48), 43 and 44 share one (root 43), 45 and 46 share one, and 49 and 50 share one. `region_gain()` gives a shared region the value of the first listed pitch it meets (it stops at the first match), so 48's +5.8 never applies and 44 gets 43's -6.0. That 47 and 48 read the same means the plucks play rrx2 (inferred).

Fix: in `build/mix.json`, the Violoncellos "Pizz" `pitch_db` becomes (equal values on shared keys, so the order does not matter): 38 +5.0, 39 +2.4, 41 +4.8, 42 -3.6, 43 -7.9, 44 -7.9, 46 -1.3, 47 +6.5, 48 +6.5, 50 0.0, 51 +0.6, 53 +1.0, 54 -1.4, 55 -6.1, 57 -2.5, 58 -2.3. Predicted range 4.2 / 1.3 / 2.7 dB (target 6). Check: 47 and 48 within 1 dB of each other. If they are not, the reset plays another take; then add `"groups": ["rrx2"]` only after reading which take it is. Keep the CC16 reset before each pluck.

### 5. Trumpet note ends are cut off: -44 to -47 dB 0.2 s after the note-off, where trombones and horns ring 15-21 dB down (measured; the cause is partly inferred)

Notes followed by 0.6 s or more of rest, stem level after the note-off against the 0.1 s before it (medians):

| track, row | n | +0.1 s | +0.2 s | +0.3 s |
|---|---|---|---|---|
| Trumpet 1 / 2 / 3, "Sus Non Vib MAX" | 8 / 8 / 10 | -11.5 / -13.7 / -12.9 | -43.7 / -46.0 / -46.8 | -55 to -57 |
| Trumpet 1, "Leg Slur MAX" | 3 | -9.8 | -36.2 | -54.7 |
| Trombone 1 / 2, "Sus MAX" | 16 / 19 | -6.3 / -6.8 | -15.2 / -17.8 | -23 / -26 |
| Horn 1 / 3, "Sus MAX" | 19 / 22 | -7.6 / -7.4 | -20.6 / -16.5 | -27 / -22 |
| Tuba, "Sus MAX" | 21 | -10.7 | -19.7 | -30.3 |

At the stop of 814 the three trumpets fall 12-14 dB at +0.1 s and 46-48 dB at +0.2 s. Trombone 1 falls 21 dB, Horn 1 10 dB and Violins I 15 dB at +0.2 s. The controllers are flat there (no CC7, no envelope point, CC1 108). In `1TP KS Master.oib` the "Sus Non Vib MAX" sustain groups release over 178 ms at f / ff (237 at p / mf), against 237 ms on the trombone. The release-trail groups ("1V ff RT" etc., `releaseTrail: true`, chosen by CC1 range) are at source volume 0.58-0.91, against 1.22-1.76 on the trombone. No trail is visible in the stems: a trail even 20 dB down would show at +0.2 s. So either the trails do not fire on this row, or they are far quieter (inferred).

Fix (Opus state, so full rebuilds of the three trumpets):
- Range test first, Trumpet 2 alone over 792-816: (a) `region_gain_db` `{"rows": ["Sus Non Vib MAX", "Leg Slur MAX"], "groups": [" RT"], "all_db": 6}`; (b) release of the sustain groups raised to 330 ms at every dynamic. `cap_release()` only lowers, so add a mix.json key `sus_release_set_ms` (same spec, sets the value) in `tools/build_reaper.py`.
- Adopt whichever brings the trumpets' +0.2 s level to -15..-22 dB (the trombones and horns). Then recheck the 814 stop on the master: 16.8 dB now, limit 15-17.

### 6. Accents by family (c19 is about right), with one track overdone (measured)

Measure: each accented note held 0.3 s or more, first 0.3 s, fader removed, against the median of same-row, unaccented, non-staccato notes on the same track held 0.3 s or more, within 4 qn, within 4 semitones, under the same printed dynamic. Excluded: any accent with a printed dynamic on it or a step up into it, and any accent inside a printed crescendo.

| family | n | median | quartiles | isolated n | isolated median | isolated under +1 dB |
|---|---|---|---|---|---|---|
| woodwinds | 29 | +1.7 | +0.6 / +2.5 | 26 | +1.7 | 27 % |
| brass | 32 | +1.0 | 0.0 / +1.7 | 24 | +1.0 | 50 % |
| strings | 77 | +0.9 | -0.8 / +2.6 | 70 | +0.8 | 56 % |

- Woodwinds: right (the +0.8 to +1.5 band, slightly over).
- Brass: right at the low edge. Do not raise (Dan, c17).
- Strings: right on Violins I (+1.2, n 25) and Violas (+0.9). Violins II are under (-0.4, n 21): their accents mostly double Violins I, so leave them.
- Violoncellos are over: +5.5 (n 9), with 116, 985, 990 and 1001 at +4.6 to +5.7 dB, and 100 and 660 on "Leg BC MAX" at +10.1 / +6.9. The celli and violin accents at 985 / 990 carry the same CC11 bump (about +10) and the same velocity step (111 against 91), so the celli's response to them is steeper.
- Fix: in `build/score_config.py`, `_C18_ACC["Violoncellos"]` amounts halved to `[(46, 2), (72, 3), (88, 4), (114, 5)]`. Check by this measure: celli median +1.5..+2.5, none over +4.

## Other checks (measured unless marked)

- Coordinator's eighths plan: row, length, lead and release are in finding 1 (lead 0.10 s, not 0.12).
- Cor anglais row change: finding 2.
- Horn 1 chorale: finding 3.
- Celli pizzicato table: finding 4.
- The trumpets' 814 drop: finding 5.
- Isolated accents: finding 6.
- Tremolo rows. Fader removed, at matched chord size: Violins I tremolo 2-note chords at 1088-1092 read -29.8..-30.4 dB against the "Sus MAX" 2-note chord at 1096, -33.0 (CC11 111 / 109). A single-note tremolo at 1016 reads -30.3 against "Sus MAX" at 1012, -36.5. Violins II tremolo 2-note -23.3..-25.6 against "Sus MAX" 2-note -29.4 (1104). Violas tremolo 2-note -32.5..-33.9 against "Sus MAX" 2-note -28.3 (1104, velocity 127). The `row_volume_db` Tremolo -3 / -4 on the violins does nothing (c19: the row knob does not act). Instrument-side values: `region_gain_db` `{"rows": ["Tremolo"], "all_db": -4}` on Violins I, -5 on Violins II, +3 on Violas (range-check the violas, whose comparison chord is at velocity 127). Lift the 1080-1116 passage roles by the same amounts so the balance stays.
- Detached pitch changes on the sustain rows (Movement I c60 #6, scherzo c18 #6): the finding applies outside the chorale. Brass Sus-to-Sus joins 0.9 qn or more apart: 410 with gaps of 60-250 ms dip the stem 7.5-8.8 dB (311 of them over 6 dB); 8 at 30-60 ms dip 5.4; 49 overlapped dip 0.5. Winds: 590 at 60-100 ms dip 5.8 (281 over 6 dB); 43 overlapped dip 1.0. These are the c17 `_C17_GAP` floors (brass 0.09, horns and trombones 0.12, winds 0.068, oboes and cor anglais 0.085 s). Proposal: where both notes are 1.5 qn or longer, floor 0.04 s on brass and 0.03 s on winds (the 30-60 ms bin still separates by 5 dB). Keep the current floors on shorter notes and on every same-pitch repeat (S1). Inferred benefit; check the master dips at the brass heads of 247-262.
- Tutti entries (Movement I c60 #10): applies. Oboe 2 is first in 3 of 5 measured chords (-38 / -50 / -48 ms; median -37 over 6 chords); Trumpet 2 median -33. Late: Horn 4 +50, Cor anglais +38, Horn 2 +32. Entry-lead corrections in `build/entry_leads.json` or the class leads: Oboe 2 -0.035 s, Trumpet 2 -0.03, Horn 4 +0.045, Cor anglais +0.035, Horn 2 +0.03.
- Horn 4 on CC1 (Movement I c59): already done here. All four horns use the 1FH KS Master with CC1 lanes (Horn 4 CC1 18-120, 101 values). No action.
- Horn legato sag at velocity 106-112 (scherzo c18 #5): does not apply. Horn 1 legato joins: median dip 0.9 dB, 2 of 43 over 6 dB.
- String legato peaks before the beat (scherzo c18 #4): smaller here. The peak in [beat -0.15, +0.10 s] over the new note's body is a median +1.9 to +2.2 dB on the four upper and middle sections; over +3 dB on 28-60 joins per section (Violoncellos 60 of 151). Not ranked.
- S1, same-pitch repeats on sustain rows: winds median dip 7.8 dB (6 of 118 under 3), brass 6.9 (17 of 146 under 3, mostly measure artefacts after rests), strings 5.7 (28 of 116 under 3). The clear fault is the printed tenuto repeated quarters of bar 246 (qn 980-983): Violoncellos and Double basses dip -1.0 to +2.9 dB, with notes at 0.31-0.38 s in a 0.36 s slot. Fix: add 980-983 to the `STR_REP_NEW_BOW` "force" list with a 0.06 s gap (Dan's rule, min(0.06 s, 25 %)).
- Crash cymbals at 888 / 1048 / 1108: the -3 dB point of the rise is at +30..+36 ms after the beat (the bass drum +6..+8, the timpani +20..+26). Raise the crash lead from 0.02 to 0.04 s.
- Loop pulsing: no string or wind note is longer than 6.4 s (longest: Horn 4 at 168, 6.4 s; timpani rolls 5.7-7.0 s, not measured), so there is nothing to re-bow.

Do not touch: the chorale overlaps and staggered same-pitch gaps (c19); the CC16 reset before each celli pluck; "Mono From Left" on Horns 1 / 3; the entry lead cuts of c19 (apart from the five tracks named above); the brass and woodwind accent amounts; the basses' pizzicato tables (range 6.6-9.9 dB on fewer, softer plucks: next after the celli); the legato rows and overlaps of the open Trumpet 1 solo (joins median dip 1.9 dB); the muted Trumpet 1 "Mute Sus" line (flat against the bloom of finding 2).
