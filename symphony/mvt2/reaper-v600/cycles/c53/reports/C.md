# Cycle 53, critic C: blend and space (review of the c52 render)

## Method

I measured the c52 master, its 36 stems (32 instruments and the four return stems) and the delivered mp3 with my own numpy scripts, and read the note data from `cycles/c52/rendered_build/` (parts.json, mix.json, score_config.py, mockup-events.tsv). Every position was converted on the c52 tempo map. For the wetness question I also measured the c37 delivered mp3 (the render Dan called "too wet and mushy") on its own map (`cycles/c37/rendered_build/parts.json`). Recordings: the two Brahms slow movements exist here as stored measurements only (`symphony/render/critics/c04/ref_brahms*_ii_musopen/metrics.json`: third-octave spectrum, stereo figures, final-chord decay times); the Dvořák 9/i figures are those in `metrics.md`. I did not use REAPER, changed no audio setting and deleted nothing. The delivered stems carry the c52 stem fix.

The line of the task file gives this slot the blend and space lens; the lead's message also asks for a ranked answer on what a listener now hears as weakest, on the "too wet and mushy" note, on Horn 1's breath at 196 and on the finale's techniques 46 and 50. Both are answered here. Each judgement is marked measured, simulated or inferred.

## Manual notes

`loop/MANUAL-READING.md` has no row for cycle 53 (its last row is cycle 47), so there was no page range. From `loop/MANUAL-GAPS.md` and the May 2021 HO manual text:

| Manual (May 2021 HO manual) | Where it applies | Does the render follow it |
|---|---|---|
| "The Divisi instruments include only Close mics because anything further away would capture both halves of the section, however, you can mix the divisi close mics and the other non-divisi mics. For the other mic positions in your projects, include the same articulations (in their non-divisi versions) and adjust the loudness." (Divisi Instruments, p.89-90 as cited in MANUAL-GAPS item 8 and DIGEST.md; text lines 3637-3640) | Violas div (bars 23-30, 80-81, 84-92), Violins II div (bars 37-40), Violin I solo (17-22), Violoncellos div (18, 21-22, 83-86) | No. The four tracks play the Close mic alone: finding 2 |
| Half-section patches for the "4 soli" basses (MANUAL-GAPS item 8) | Double basses bars 65-70 and 87-92 | Not used; no finding from this lens (the basses' level and width there are the section's) |
| Round-robin reset on CC16 (MANUAL-GAPS item 10; p.34, 143, 145) | Repeatability of takes between sessions | In the pre-roll and at Violas 152.06 only; see the answer on technique 46 |

## Answer to the lead: what a listener now hears as weakest, ranked

1. **Low-mid weight (finding 1, measured).** The master carries 3.2-3.7 dB more energy at 140-355 Hz than the two Brahms slow movements and 5-7 dB less at 70-110 Hz. The celli supply 51-75 % of that band in the string themes. With the hall now measured at or under recording level, this is the part of "mushy" that is left.
2. **String theme timing in bars 22-27 (the actor's figures, not re-measured by me; inferred rank).** Violins II 5 of 24 notes outside 60 ms, to -127 ms, against Violins I on a doubled theme. Dan's notes named timing first, so for him this may rank above item 1. It is slot A's; my only contribution is the answer on technique 46 below.
3. **The divisi tracks are mono sources without a room (finding 2, measured).** Violas div is exactly mono; the stereo image narrows by 4-5 dB in bars 17-22, 37-44 and 83-86.
4. **Horn 1's pickup at 195.5 is 7 dB under its line (finding 3, measured).** This is also why the breath at 196 reads 5.9 dB.
5. **The diminuendo of bars 81-82 falls late on eight tracks (finding 4, measured; technique 50).** Small.
6. **Wetness is no longer on the list (finding 5, measured).** No change asked; two do-not-touch items follow from it.

## Findings

### 1. Low-mid build-up: the cello EQ boost and the harp bass put the weight at 160-320 Hz

**Where.** Whole movement; most in bars 23-30, 53-60 and 71-78. Tracks Violoncellos and Harp. `build/mix.json`.

**What is wrong (measured).** Third-octave levels of the master relative to total energy, minus the mean of Brahms 1/ii and 4/ii:

| Passage | 79 Hz | 99 | 125 | 158 | 198 | 250 | 315 | 397 | 500 | 140-355 Hz share |
|---|---|---|---|---|---|---|---|---|---|---|
| whole | -6.8 | -4.6 | -2.0 | +0.7 | **+4.8** | +1.2 | **+5.2** | -1.4 | -1.8 | -5.3 dB (Brahms -9.0, -8.5) |
| bars 23-30 | -10.5 | -2.1 | -6.4 | **+6.0** | **+5.8** | -1.8 | +3.1 | -0.2 | -1.3 | -4.8 |
| bars 53-60 | -11.8 | -0.4 | -8.2 | +2.5 | **+6.0** | -1.7 | **+5.9** | -0.6 | +0.2 | -4.7 |
| bars 71-78 | -4.1 | -9.4 | -9.3 | +1.7 | **+7.8** | +3.2 | +1.5 | -2.2 | +1.2 | -4.7 |

The same excess shows against the Dvořák reference in `metrics.md` (250 Hz band +7.3 against +4.4 relative to 1 kHz). The 62 Hz band of both Brahms files is not used: it reads -11.4 dB in both and is probably mains hum (inferred). Part of the 198 and 315 Hz peaks is the key (A flat 3 is 208 Hz, E flat 4 is 311 Hz), so the target is not zero; the band sum is the figure to move.

Who supplies the 140-355 Hz band (share of the sum of all stems): whole movement Violoncellos 31 %, Horn 1 12 %, Violas 8 %, Double basses 7 %; bars 23-30 Violoncellos 75 %; bars 53-60 Violoncellos 51 %, Horn 1 23 %; bars 71-78 Harp 43 %, Violoncellos 19 %. The cello track still has the bell from c08-c09 (`"eq": [{"band": "bell", "hz": 170, "db": 3, "bw_oct": 1.5}]`), added for "tutti low-mid weight" before the family EQs and the template mix existed. In bars 75-78 the harp's bass octaves (MIDI 27-46, velocities 64-104) play at the level of each violin section (bar 77: Harp -39.3, Violins I -38.3; bar 78: -32.4 against -31.4) and nearly all of that energy is under 355 Hz. That harp level is a balance question for slot B; the spectrum part is mine.

**Simulated** (per-passage power spectra, the stem's contribution rescaled by the EQ response; cross terms ignored):

| Change | bars 23-30: 158 / 198 Hz | bars 53-60: 158 / 198 | bars 71-78: 198 | 140-355 share, 23-30 / 53-60 / 71-78 |
|---|---|---|---|---|
| now | +6.0 / +5.8 | +2.5 / +6.0 | +7.8 | -4.8 / -4.7 / -4.7 |
| cello bell 170 Hz +3 removed | +4.2 / +3.8 | +0.9 / +4.2 | +7.8 | -5.9 / -5.3 / -4.9 |
| and Harp bell 200 Hz -4 dB, 1.2 oct | same | same | +5.5 | -5.9 / -5.3 / -5.8 |

A further cello cut (220 Hz -2 dB) gains 0.2-0.6 dB more and is not asked. Raising the basses' 80 Hz cut from -6 to -3 dB lifts the 79 Hz band by 2.4 dB (whole) but that cut was fitted in c25 to a boom on C2-G2; not asked.

**Fix.** `build/mix.json`: (a) `tracks.Violoncellos.eq`: remove the 170 Hz bell (the copy on `Violoncellos div` stays: that track plays only soft solo passages and supplies under 1 % of the band). Keep the `loud_eq` 150 Hz +4 dB of the two ff tutti (c16) and the family EQ. (b) `tracks.Harp.eq`: add `{"band": "bell", "hz": 200, "db": -4, "bw_oct": 1.2}`. Both by `--mix-only`. The cello stem loses about 1 dB of plain level where its fundamentals sit at 150-250 Hz: restore the counter-melody's A-weighted level per passage with `gain_db` or a stem fix, not with the bell.

**Acceptance.** Master 140-355 Hz share at most -5.8 dB in bars 23-30 and 71-78 and at most -5.3 dB in bars 53-60 (now -4.8, -4.7, -4.7); celli A-weighted level in bars 23-28 and 71-76 within 0.5 dB of c52; bars 7-14 (Horn 1 over the harp) harp level within 1 dB of c52 after any make-up.

### 2. Violas div and Violins II div are mono point sources with no room; the image narrows where they and the close-led winds carry the texture

**Where.** Violas div (bars 23-30, 80-81, 84-92 including the final chord), Violins II div (bars 37-40); also Violin I solo and Violoncellos div.

**What is wrong (measured).** Stem stereo figures, 250 Hz-4 kHz correlation and side/mid over the whole file:

| Track | correlation | side/mid |
|---|---|---|
| Violas | 0.46 | -4.5 dB |
| Violas div | 1.00 | **-112 to -123 dB** (the two channels are identical) |
| Violins II | 0.46 | -4.0 |
| Violins II div | 1.00 | -14.8 (a panned mono source) |
| Violoncellos div | 1.00 | -15.9 |
| Violin I solo | 1.00 | -10.8 |

In bars 23-30 the two halves of the violas play at the same level (-49.4 dB each): one half is a wide section image with its stage sound, the other a single point in the centre. The same holds through the coda (Violas -63.6, Violas div -62.2 dB over bars 83-92). The `width` and `side_shelf` settings of these four tracks do nothing, because the Close mic of the divisi patches is mono and there is no side signal to shape. The extra hall send these tracks used to get (`"send": 0.5` and 0.8 against the strings' 0.25, kit LEARNINGS section 8) has had no effect since c44: those are Opus sends and the Opus hall is off; the tracks now send to R Strings at the family level, and that return sits 22-26 dB under the dry strings.

Master width by passage: bars 23-30 correlation 0.47, side/mid -4.5 dB; bars 17-22 0.71, -7.6; bars 37-40 0.83, **-9.8**; bars 41-44 0.76, -8.3; bars 83-86 0.80, -9.4; whole 0.57, -5.6 (Brahms 1/ii 0.51, -4.9; Brahms 4/ii 0.55, -5.4). The room appears to shrink by 4-5 dB of side level whenever the texture is a divisi track plus close-led woodwinds (Oboe 1 stem 0.96 / -15.4, Flute 1 0.88 / -11.4). How strongly a listener hears this is inferred; on headphones a signal identical in both ears sits inside the head, which is why Violas div is the first to fix.

A hall send cannot do it: with a return at -11 dB under the track (12 dB more send than now) the track's side/mid would only reach about -14 dB (computed from the returns' side/mid of 0 to +1.5 dB), and c49's R Stage test on the solo violin found the same (correlation 0.98 to 0.89 only).

**Fix.** The manual's method (table above): the missing mics come from the non-divisi patch. The brief forbids adding an Opus instance without removing one, so swap the patch instead of layering it: in `build/score_config.py` give the tracks "Violas div" and "Violins II div" the section's own KS Master (`Violas KS Master.oib`, `2nd Violins KS Master.oib`) with the string group's mics (Close 0.5, Main 1.0), seat and width, and remove their `side_shelf` and `"send"` keys in `build/mix.json`. Two instances of one patch on different pitches do not collide (the identical-sample problem is for equal pitches, kit LEARNINGS section 8). Keep the divisi level cut the section voice already has (-3 dB). This is an Opus state change on two tracks (full rebuild); their fills need refitting: Violas div re-bows at 289 and 291.7 and the c52 level rows, Violins II div 120. Leave Violin I solo and Violoncellos div on DIV A: a soloist and four soli players are narrow sources. Test first with one range render of bars 23-30 and 84-92 (finale technique 37) before the full render.

**Acceptance.** Violas div and Violins II div stems: correlation at most 0.6 and side/mid within 2 dB of their section's; master side/mid in bars 37-40 at least -8.5 dB; the div tracks' level per bar within 1 dB of c52 after the gain is reset; final chord t20 inside 0.45 ± 0.02 s; REAPER memory still under 45 GB (it was 40 GB after the c52 render).

### 3. Horn 1 at 195.5-196: the pickup eighth is 7 dB under the line, so the breath after it reads as shallow

**Where.** Horn 1, qn 195.5 (F4 eighth, slurred from the E flat 4 of 193-195.5, under the crescendo to the f of bar 59) and the breath at 196.

**What is wrong (measured on the stem, 20 ms frames).** The E flat 4 holds -32.6 dB until 0.55 s before the beat. The F4 eighth (note-on 0.57 s before the beat, 285 ms long) reaches only -39.7 dB, and reaches it 0.24 s before the beat, after its own note-off; during the note the stem falls from -33 to -44 dB. The gap then goes to -45.2 dB (0.12 s before the beat) and the f entry is at -32 dB on the beat. So the breath is 12.6 dB under the line's level, which meets the 10 dB the actor wanted; the check reads 5.9 dB because it compares the gap with the last 0.3 s, and that is the weak eighth. What a listener hears is the horn fading out half a second before the bar line in the middle of a printed crescendo, and the pickup note missing.

Cause (read from parts.json and `score_config.py`): the +3 dB shape of line 1004 ends exactly on the pickup (`(195.35, 3.0), (195.5, 0.0)`; the track's volume lane falls from +6.84 to +4.27 dB between 195.35 and 195.5), the legato change from the E flat needs longer than the 285 ms the note now has (c52 took 0.3 qn off it for the breath), and nothing lifts it.

**Fix.** `build/score_config.py`: (a) in the Horn 1 shape of line 1004 hold the +3 through the pickup: `[(183.95, 0.0), (184.1, 3.0), (195.76, 3.0), (195.82, 0.0)]` (the fall then lies inside the breath gap; the horn has no Opus hall, so the post-plugin envelope cuts nothing that should ring); (b) add a lift on the pickup, `LEVEL_SHAPES["Horn 1"] += [[(195.42, 0.0), (195.5, 4.0), (195.74, 4.0), (195.8, 0.0)]]`, and fit its size on the c52 stem as the nine wind joins were fitted (`joinfit52.py`). Both are level-only, so a stem fix can apply them without a new take. Do not lengthen the gap again and do not change the leads. Change the check in `breath52.py` for this row to compare the gap with the body of the note at 193 (0.9 to 0.6 s before the beat).

**Acceptance.** The F4 eighth's highest 50 ms level within 3 dB of the E flat body (now -7.1); gap floor at least 10 dB under that body (now 12.6); master dip at 196 not over 5 dB.

### 4. Technique 50 (long diminuendos): one place here, bars 81-82

**Where.** The printed diminuendo 268-271 (ff to p, 3.9 s) on Flute 1, Oboe 1, Cor anglais, Clarinet 1, Bassoon 1, Horn 3, Horn 4, Violins I.

**What is measured.** Hairpins longer than 6 s are already linear here (`HP_CURVE` `max_s` 6.0), so the first half of technique 50 is in place. Among the 3-6 s diminuendos the curve (control point at 68 % of the time with 27 % of the fall) puts most of the fall in the last quarter at 268-271: stem steps per quarter Flute 1 -2.7 / -2.9 / -8.6, Horn 3 -3.3 / -2.9 / -8.2, Horn 4 -2.6 / -4.2 / -7.2, Cor anglais -0.8 / -1.7 / -5.4, Clarinet 1 -2.8 / +0.8 / -5.4, Bassoon 1 -0.5 / -2.8 / -6.2, Violins I 0.0 / -0.4 / -6.4 (94 % of its fall in one quarter). The tracks already listed as linear there fall evenly (Violoncellos -5.1 / -6.0 / -4.5). Master steps over 268-272: -3.2, -2.6, **-5.9**, -1.7; mp3 -3.0, -0.7, -4.6, 0.0. The finale's case was a 9.5 dB step, so the gain here is smaller. The other curved diminuendos are soft and short (bars 3, 28-29, 100) and their master steps are under 3 dB, except 83 to 84 (-5.9 dB), which is the phrase end of the theme and not the curve (the curve's fall would lie after 85.4).

**Fix.** `build/score_config.py`, with the existing line 1282 pattern: add `(268.0, 271.0)` to `HP_CURVE["linear"]` for the eight tracks named above. CC11 only, `--midi-only` on those tracks. I do not ask for the finale's `decresc_last_max_qn` / `decresc_last_min_s` keys: no other hairpin here needs them.

**Acceptance.** No quarter of 268-271 carries more than 50 % of a track's fall; master step into 271 at most 4.5 dB; bar 82's level within 1 dB of c52.

### 5. Wetness: measured at or under recording level; leave the hall alone

**What is measured.**

- **Against the render Dan heard.** How far the previous pitch has fallen 0.15-0.25 s after each slurred note change, in its own partials, median per line, c37 mp3 against c52 mp3: Horn 1 bars 7-14 6.2 -> 12.5 dB; Oboe 1 15-16 11.7 -> 16.5; Violin I solo 10.1 -> 15.2; Violins I 23-30 7.7 -> 11.2; Violoncellos 23-30 2.8 -> 7.2; Flute 1 37-40 7.9 -> 11.9; Cor anglais 41-44 6.6 -> 12.4; Violins I 53-60 9.8 -> 12.2; Violins I 71-78 10.1 -> 12.1. Every thematic line is 2-6 dB clearer than in c37.
- **What the returns still cost.** The same measure on the c52 master with the four return stems subtracted: winds 1.3-3.3 dB better (Oboe 1 16.6 -> 19.9, Cor anglais 12.3 -> 14.8), strings 0.0-0.4 dB. Return level against the dry stems of its family, by passage: strings -19 to -26 dB, winds -10 to -15, brass -9 to -21, harp and timpani -6 to -10; all returns against all dry stems -10.6 (bars 31-36) to -21.8 dB (bars 23-30). The rest of the gap between a stem's own figure (15-20 dB) and the master's (11-12 dB) is other instruments on the same pitch, not the hall.
- **Against recordings.** Final chord of the master: -10 dB at 0.26 s, -20 at 0.43, -30 at 0.68, -40 at 0.94 s (mp3 0.27 / 0.41 / 0.61 / 0.92). Brahms 1/ii: 0.40 / 0.79 / 1.23 / 1.64 s. Brahms 4/ii: 0.20 / 0.48 / 1.15 / 1.72 s. The mockup reaches -20 dB as fast as the drier recording and -40 dB in a little over half the time of either.
- **By family at their stops (dry stems plus own return).** Level 1.0 s after the stop: strings 48-49 dB down, winds 40-54, brass 29-43, median 36 (time to -40 dB: strings 0.91-0.94 s, winds 0.71-1.00, brass 0.87-1.50). The brass keep about 12 dB more late tail than the strings (median), and the brass figure is the one nearest the recordings. The families are therefore not in quite the same room late in the tail, but the difference lies 30 dB or more under the note.
- **Simulated: R Strings fader +3 / +6 / +9 dB** (master plus the scaled return stem): final chord t20 0.44 / 0.47 / 0.51 s, t40 0.94 / 0.94 / 0.96 s, violin theme clarity -0.0 to -0.6 dB. The return's shortened IR (envelope 0.5) ends before 1 s, so raising it fills only 0.3-0.8 s and breaks the t20 limit at +6 dB without lengthening the late tail.

**Verdict.** The "too wet" part of Dan's note is answered by c44-c52 as far as measurement can tell. Drying further would take the ending and the wind solos below both recordings; raising the string return buys nothing. Final chord t20 0.46 s is inside its limit and should leave the open list. If Dan still hears mush after this cycle, finding 1 is the place to look, not the returns. No change asked.

## Answer on the finale's technique 46 (CC16 resets before each section)

Not measured by me; weighed from the c52 tables and the finale's notes 40, 46-48. Since c52 the string lines stay on one row, so the finale's remaining cause of moving joins (note 47: joins whose row differs from the row before) is mostly gone here, and what still moves between sessions is one track in one passage (Violins II bars 22-27, 6 joins). A reset on every track at every section is a data change for the rest of each track (finale note 40: 73 later long notes moved 2 dB or more), and this movement has several hundred fitted rows on the present takes (66 level rows from c52, re-bow fills, nine wind join lifts, lead tables). I would not adopt 46 wholesale now. A narrow trial costs little: `RR_RESET_AT["Violins II"] = [58.0]` (the track rests from 57.0 to 59.0; the table and the CC16 lane exist since c49), one range render of bars 20-30 in two separate sessions, compared by `tools/s_onsets.py`. Adopt it on that track if the 6 joins stop moving; then refit Violins II's leads and level rows from 59 on, since its takes after the reset will change. If the joins still move, the cause is not round robin and the reset should be removed.

## Checked, no finding (measured)

- Master stereo against the Brahms pair, whole movement: correlation 0.57 (0.51, 0.55), under 250 Hz 0.63 (0.60, 0.62), side/mid -5.6 dB (-4.9, -5.4), right minus left -0.2 dB.
- Seats of the dry stems (right minus left, dB): Violins I -5.5, Violins II -3.2, Violas +0.2, Violoncellos +4.2, Double basses +4.4, horns -1.0 to -4.0, trombones +1.7 to +3.1, tuba +4.9, harp -3.1, harp harmonics -3.0. The two harp tracks now share one seat.
- The master equals the sum of the 36 stems (difference 148 dB under the master).
- Harp harmonics against the harp in the coda: same seat, level -61.6 against -65.0 dB (the harp's ring), no finding.

## Not measured by me

String join timing and the one-row string tone (the lead's first two open items), S1 dips, loop pulsing and re-bow dips, Violins II 197.5, Horn 2 208 and Violas 81. The previous-pitch measure is not valid below about 150 Hz (bass clarinet solo, bars 31-36): its 12 Hz resolution cannot separate neighbouring low pitches.

Scripts and cached data are in `/private/tmp/claude-501/mockup-loop/mvt2-c53-C/` (149 MB; no simulated audio kept apart from two mono copies of the c37 and c52 mp3s). I left the folder in place, as the lead's rules say not to delete files.

**Do not touch:** the four returns (faders, IR envelope 0.5, the 2.3 kHz low pass, the family sends) and the final chord's tail; the template mic levels and seats of the section tracks; the horn `track_width` 0.8; the basses' 80 Hz cut and 140 Hz bell and both `loud_eq` rows at the ff tutti; Violin I solo and Violoncellos div on their DIV A patches; the breath gaps set in c52 (Flute 1, Oboe 1, Horn 1 at 196; Trombone 2 and Bass trombone at 204); `HP_CURVE` outside 268-271; the delivery settings (`rise_delay_s` 0.6, `TARGET_I`, `RATIO`, `TOP_RATIO`).
