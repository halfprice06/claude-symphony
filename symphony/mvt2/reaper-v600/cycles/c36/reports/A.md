# Cycle 36, critic A: articulation and phrasing (on the c35 render)

Sources: `cycles/c35/render/` stems and master (c34's for comparison), `cycles/c35/rendered_build/parts.json` (and c34's), `build/mockup-events.tsv`, `build/score_config.py`, `build/rebow_fills.json`, `tools/score_to_parts.py`, score pages 3 and 6, the May 2021 HO manual pp. 95-99 (group A2) and `loop/MANUAL-GAPS.md`. Levels are RMS in dBFS (30 or 50 ms windows; 200 ms on flute, oboe and cor anglais, whose vibrato a short window reads as holes). Times are in score qn, converted on the parts.json tempo map. Scratch scripts were in `/private/tmp/claude-501/mockup-loop/mvt2-c36-A/` and have been deleted.

## Manual notes (A2, PDF pp. 95-99)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| Pre-recorded runs (1st Violins, Violas, Celli) and playable Slur Runs (1st/2nd Violins only), which need at least sixteenths at about 125 bpm (pp. 95-97) | the violins' run into bar 79 (qn 261.5-261.83, three notes at about 48 bpm) | Not applicable. The run is far slower than the Slur Runs minimum and is not a one-octave scale. Sus MAX notes with `GROUP_LEAD_AT` are the right choice. |
| Tremolo (unmeasured) vs Measured Tremolo TS; neither responds to velocity, so dynamics go on CC11 (p.97) | "trem." (:32) on the violas from bar 61 and on all strings in bars 63-64 | Yes. Every tremolo plays the unmeasured `Tremolo` row (keyswitch 0.06 qn before 204/212). Dynamics are on CC11, and the bar 63 sf fall is on CC7. No tremolo note is longer than 4.5 s (4.41-4.52 s), so none reaches a second loop. |
| Trills (p.98) | none in v600 | n/a |
| Repetitions patch (Violas, Basses only): about a dozen tempo-synced pulses in a little over one second, CC11 crossfades 3 layers (p.98) | the violas' sotto voce portato eighths, bars 48-51 | Not suitable. The eighths come at about 1.8 per second, so the patch would play pulses inside each note. Detache is the right row (see "Checked and fine"). MANUAL-GAPS #2 stays untried for this passage. |
| Sul ponticello, violas only (p.98) | none printed | n/a |
| Legato types: bow change, portamento, slur. The basses have Legato Slur only (p.98) | Leg BC MAX on slur-to-slur joins (Vln I 67.8, 207.8 ...); Leg Port MAX at Vln I 82 and 172; basses on Sus MAX / Leg Slur | Yes. The two portamentos are unprinted expressive shifts (82: bar 28; 172: the "sul A, cantabile" entry of bar 53). They are a liberty the brief allows, and I would keep them. |
| A legato transition needs no significant gap between notes (p.99) | every printed slur | Mostly. I scanned all 210 slurs in parts.json: 73 slurred note pairs are not legato-joined. 69 of them are by design: wind portato tenutos re-tongued (`WIND_REP_PORTATO`), the violas' sextuplets 196-203 and the bar 79 run on Sus MAX, and the harp harmonics. **Two are errors: Violas 248 and 252.5 (finding 3).** |
| Legato instruments are monophonic; CC22 turns on polyphony (p.99; the polarity is reversed there, see 2025 p.91) | all Leg rows | Yes. No pair of different-pitch notes overlaps by more than 0.15 qn on any Leg row (measured on parts.json). |
| Legato Slur Staccato: a slightly stronger attack on the first note of each phrase (p.99) | not loaded | Not needed. v600's string phrase heads are soft. |
| Bow-change legato carries its own bow-reversal sound (p.99) | slur-to-slur joins at mf and above | Yes (LEARNINGS §5 list). |
| MANUAL-GAPS #8 (4 soli on half-section patches) | Cb 220-238, 286-304 | Still not tried. Finding 1 gives the level fix that works without it. |

## Extra check: c35's new front peaks on Oboe 2 267, Oboe 1 210 and Violins I 249 (measured; judged not audible)

These peaks are the same sample bloom as before, now arriving earlier. They are not a new transient.

| Note | 2-5 kHz, first 80 ms minus body | 200 ms peak over body (c34 / c35) | Stem under master at the peak | Master 2-5 kHz jump |
|---|---|---|---|---|
| Oboe 2 267 | -7.2 dB | +1.5 / +4.7 dB | 12 dB | +2.0 dB |
| Oboe 1 210 | -6.1 dB | +2.3 / +3.5 dB | 13 dB | +1.3 dB |
| Violins I 249 | -5.1 dB | +1.6 / +1.4 dB | 12 dB | -1.9 dB |

- **Oboes.** In c34 both oboes peaked 4-6 dB over their 0.3-1.0 s body at +0.40 s. In c35 the same peak comes at +0.19/+0.23 s, because the re-attack lead moved the note 0.20-0.25 s earlier. The shape is the oboe's first vibrato swell: a second maximum follows 0.25 s later.
- **Violins I 249.** The "4.5 dB" is a single 30 ms spike inside a slow rise. On 200 ms there is no peak.
- **Context.** Oboe 1 210 sits in the ff climax and Oboe 2 267 in the bar 80 ff tutti, so neither stem is exposed.

Fill or trim none of the three.

Related, also measured: the re-attack leads end the previous note 0.02 qn before the moved onset, and on the stems this opened holes the c35 table did not list:

| Note | Stem hole c34 -> c35 |
|---|---|
| Violas 266 | 2.8 -> 8.8 dB |
| Violins II 218 | 2.9 -> 7.9 dB |
| Violins I 249 | 7.7 -> 10.5 dB |
| Horn 3 267 | 1.2 -> 6.0 dB |
| Bassoon 1 198 | 4.7 -> 7.9 dB |
| Violins II 73.5 | 1.5 -> 6.8 dB |

All of these are at or under 3.4 dB on the master (Violas 266: 0.5; Violins II 218: no dip). Inferred: not audible, so no action is needed. One exception: Violas 252.5 should not have been led at all (finding 3).

## Findings, ranked by what a listener hears

### 1. Double basses "4 soli", bar 66 (qn 221.8 and 225.215): two re-bows still sag 4-8 dB, and at 225.2 the basses are almost the only sound (measured)

**Where.** Double basses, the E flat pedal ("4 soli, sul A, change bow at will", pp). It matters most at qn 225.2-226.0, where the upper strings' printed niente has faded out and Horn 1 and the timpani have not yet entered (226).

**Evidence (measured).**
- **225.215 (100 ms bins).** The stem goes from -51 dB before the re-bow to -55 for 0.9 s, falls to -58 at +1.0..+1.2 s, then comes back to -53. The master follows it: -49 before, -53 from 0.0 to +0.8 s. A 4 dB, one-second sag in a passage where little else sounds. Re-bow dip 8.5 dB, step -6.4 dB over the next 1.5 s.
- **221.8.** The stem drops -52 -> -60 at the re-bow and is back to -53 by +0.4 s (dip 9.7 dB). The master dips 3-5 dB for 0.3 s under the held pp string chord.
- **Other pieces in 227.8-238.** They dip 3.7-6.0 dB on the stem and 1.4-4.5 on the master, where Horn 1 is playing.
- **No loop pulse.** The pedal does not pulse at the loop period: the 0.25 s level p95-p5 in 220-238 is 7.3 dB, irregular.
- **The fill at 225.215 is flat.** In `build/rebow_fills.json` its shape is a hand-flattened plateau (+4.31 dB from 0.0 to 0.28 s, +3.31 from 0.44 s, a dip to +2.41 at 0.88 s). It does not follow the stem's deficit, which is about 4 dB over 0-0.9 s and about 6 dB at +1.0..+1.3 s. The neighbouring fitted pieces reach +6..+7.5 at the same times after their starts.

**Fix.**
- **225.215.** In `build/rebow_fills.json` "Double basses" "225.215": add +3.5 dB to every point from 0.0 to 0.92 s (4.31 -> 7.8, 3.31 -> 6.8). Add +5 dB from 0.96 to 1.32 s (3.31 -> 8.3), tapering back to the existing values by 1.40 s.
- **221.8.** Add +3 dB to the points from -0.04 to +0.28 s (they are now 4.3-7.5; cap them at 9, the fit's clamp).
- **Check.** Both are level-only, so simulate with `tools/stem_fix.py` on the c35 stem first. Target: stem within 2 dB of the pre-re-bow level from 0 to 1.3 s, and master dip at 225.215 under 2 dB.
- **Alternative (timbre, inferred, MANUAL-GAPS #8).** `Basses KS Master DIV A.oib` for 220-238 and 286-304 would sound like fewer players and might be steadier. It costs a 33rd instance and a refit of every basses fill in these spans.

### 2. Flute 1, bar 44 (qn 136): the slurred repeat of E flat 5 is not heard as a second note; since c35 the flute is the exposed line here (S1, measured)

**Where.** Flute 1, qn 135-136: E flat 5 crotchet slurred to E flat 5 dotted minim (bar 43 b4 into bar 44), over the cor anglais. c35 (B #4) raised the flute +5 dB over 134.3-138, so it now leads the duet by 2-6 dB.

**What is wrong.** `WIND_SLUR_REP_MERGE` merges the two notes and marks the repeat with an 8 CC notch (CC11 34 -> 26). The flute's own vibrato swings the level about ±4 dB every 0.25 s:
- the notch troughs at -55..-57 dB (30 ms) at +0.01 s
- the vibrato troughs either side reach -54..-56 dB (-0.47 s, +0.27 s, +0.49 s)

So the notch sits only 3.1 dB under the note's own 10th-percentile level, and the master shows 2.1 dB. A listener hears one long E flat. A flautist plays a slurred repeat with a soft tongue, and S1 asks for it to be heard. For comparison, the cor anglais 271 repeat (notch 20 CC) measures 5.0 dB under its own troughs and 3.5 dB on the master.

**Fix.** In `build/score_config.py` `MERGE_NOTCH_AT["Flute 1"] = {136.0: 16}`. Target: notch 5-6 dB under the note's own vibrato troughs, master dip 3-4 dB, no hole longer than 0.15 s. Do not re-tongue it on Sus with a gap: the c07 measures (LEARNINGS §6) gave 6-12 dB holes that way.

### 3. Violas, bars 74-75 (qn 248 and 252.5): a slur's last note is merged into the next slur's same-pitch first note, so the slur breaks before the note and the bow change after it disappears (measured)

**Where.** Violas, the slurred eighth figures under the violins' theme.
- Bar 74: E flat 3-G 3-E flat 4 slurred, then E flat 4 starts the next slur at 248.5.
- Bar 75: E flat 4-A flat 3-F 4 slurred, then F 4 starts the next slur at 253 (score p.6, mockup-events.tsv).

**What is wrong.**
- **Cause.** `score_to_parts.py`'s legato merge joins the two same-pitch notes and then gives the merged note the second note's slur (`n["slur"] = o["slur"]`). The note at 248 / 252.5 therefore becomes the first note of the new slur and is no longer the legato target of its own slur.
- **248 in parts.json.** It plays unled at velocity 37, 0.05 qn after the G 3 ends. Its neighbours are led about 0.2 s at v124.
- **252.5 in parts.json.** It plays at velocity 49 after a 0.02 qn gap (and c35 added a 0.25 s re-attack lead to it).
- **248 on the stem.** It falls -51 -> -58 dB at 248.0 and stays 6-8 dB down until about 248.9: the slow first-note layer.
- **No articulation at the bow change.** The repeat at 248.5, where the bow actually changes, gets nothing (the stem is still rising there).
- **Master.** 1-2 dB (an inner voice under the violins).
- **Scope.** These are the only two cases in the movement (a slur ending on a pitch that the next slur starts with, on one note per voice).

**Fix.** Add a per-onset option to the merge in `tools/score_to_parts.py`, for example `MERGE_JOIN_OWN_SLUR_AT = {"Violas": [248.0, 252.5]}`. A listed note keeps its own slur when it absorbs the next slur's same-pitch note:
- it is joined from the note before it as a Leg Slur target, with the normal lead and v124
- the bow change is marked by the merge notch at the second onset (14 CC at 248.5 and 253, or 8 at CC11 40 or below)

Remove `REATTACK_LEAD_AT["Violas"][252.5]` (the note is then led as a legato target). `STR_MERGE_KEEP_SLUR_START` is not the right switch: c32 found it changed tuned joins elsewhere. Target: stem level at 248.0-248.5 within 3 dB of the G 3 before it, and a 3-6 dB dip at 248.5 and 253.

## Checked and fine (measured unless stated)

- **Re-bows.**
  - Final chord: master -50..-54 dB over 301-304, with 1-1.5 dB bin-to-bin changes. Individual sections swing 7-13 dB on 250 ms bins, but the summed chord does not.
  - Opening chord: master within ±1.5 dB at the Violins I re-bows 2.4, 4.6 and 7.35. The stem's ±5 dB grain is the ppp sample.
  - Bar 66 niente: the -6 dB steps at 223 follow the printed decrescendo.
  - Coda 4 soli (Vc div): dips 0.7-3.6 dB on the stem.
  - No held string note is longer than 4.5 s on one sample, and every tremolo is under 4.52 s.
- **Accents.** Trombone 1 213 and 218: 2-5 kHz in the first 80 ms is 2.9 and 6.8 dB under the body, with master 2-5 kHz jumps of -0.3 and -0.1 dB. The unaccented 212.5 is 5.3 dB under. Weight, not bite.
- **Tenutos, bars 61-62 (molto sostenuto).** Master dips at the half-note changes 206/208/210 are 0.9/0.6/3.1 dB, and every section holds its body. Stem dips are 0-7 dB, and the Leg BC row is used on Violins I.
- **Violas' portato, bars 48-51.** All 15 notes on Detache. Peaks within 2.1 dB (-45.6..-47.7). The energy centroid of the first 300 ms is -0.045..+0.093 s from the beat (S2). The rests drop 12.5-23 dB.
- **Keyswitches.** No row change arrives after the note it serves. The only row changes that land inside a sounding note are the intended ones: legato-type switches during the overlap, timpani roll-to-stroke, violas Tremolo at 203.94, and basses pizz at 211.94.
- **Mutes.** CC15 matches every con sord. / mettere sord. / senza sord. mark. The celli and basses stay open in the coda, as v600 prints. Horn 4's con sord. is in its part (`coda.ily` codaHnFour), so muting Horns 3-4 is correct.
- **Harp.** All 29 arpeggios roll from the bottom at 40 ms (30 ms at f on 261). At 31 and 251 the left-hand note sounds with the right hand's first note, as printed (the arpeggio sign is on the right hand only).
- **Legato.** No chords on any legato row. The wind portato re-tongues are as designed. I did not re-measure the breath marks this cycle; c35's critic A found all 44 wind and brass breaths dipping 4-30 dB, and c35 changed no breath gaps.

**Do not touch:**
- the c35 re-attack leads (master unchanged; only the Violas 252.5 entry goes, with finding 3)
- the oboe and Violins I 249 fronts
- Trombone 1's quotation and its accents
- the final-chord, opening-chord and bar 66 re-bows and their fits
- the Vc div coda fills
- the violas' Detache portato and its CC7
- the unmeasured Tremolo rows and the bar 63 CC7 lanes
- the Leg Port shifts at 82/172
- the mute points
- the harp roll timing
