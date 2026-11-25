# Cycle 40, critic C (holistic) on the c39 render

Compared: c39 against the c27 port baseline, c34 (five cycles back), series 1's c26 (v77) on bars 1-36 and the coda, and the Dvořák 9/i recording (`symphony/render/assets/refs/`, the Adagio introduction, 0-100 s) plus the stored Brahms 1/ii and 4/ii band shares. Scripts were scratch only: per-stem phrase-end decay by articulation row, the c38 `hall38.py` measures, per-note level change against envelope change between renders, band shares per stem, master within-second level movement, loop autocorrelation.

## Manual notes (H1: May 2021 HO manual PDF pages 10-11, 61-63)

| Manual (PDF page) | Where it applies here | Render follows it? |
|---|---|---|
| p.10: new 18 Violins section, "an alternate" to 1st Violins with different players and vibrato, "the legato is the best we have ever recorded" | Violins I in the big themes, bars 23-28, 53-60, 71-78 (1st Violins KS Master now) | Not used. Installed (`18 Violins/04 Legato`, `05 Keyswitch`). Movement I rejected it (no bow-change legato row; every Violins I fit would need redoing). Leave it unless the bow-change finding below fails. |
| p.10-11: new woodwind ensembles (3 flutes, 3 clarinets, 3 bassoons) and new 2 tenor trombones | v600 writes solo winds and two trombones plus bass trombone | Not applicable: the solo KS Masters are the right players. |
| p.61: the Opus Edition contains 7 libraries, including Hollywood Solo Violin and Solo Cello | the bars 17-22 violin solo (DIV A now), the 4 soli passages | The manual lists them as included; MANUAL-GAPS #3 found Solo Violin not installed. Dan could install it from the Installation Center; no action in the loop. |
| p.61: Mood presets Classic (default), Soft, Epic | the muted strings, bars 15-30 and the coda | Classic; the mockup sets its own mutes, CC and EQ. Follows the manual's default. |
| p.62-63: MAX instruments carry the most dynamic and vibrato layers, LITE about half | every sustained note | Follows: all sustained and legato notes play MAX rows; "Sus Marc LITE" appears only in the planned release-cap row list. |
| p.63: every instrument fades to silence with CC11 (no separate niente patches) | the strings' niente in bar 66, the morendo final chord | Follows. The bar 66 niente is in CC7 (c30), which also acts before the hall. The final chord fades CC11 to 8 before the note-offs, so the planned release caps will not clip it (read in parts.json). |
| p.63: finger positions on CC70 | "sul A", "sul D" passages | CC70 is written on Violins I (9 events), Violins II (10), violas (2), celli (6). Follows. |

MANUAL-GAPS.md: #2 (repetition rows) and #6 (slower legato velocity on the cantabile lines) are still the untried items that touch this lens; the findings below do not depend on them.

## Overall judgement

Clarity has improved since c27, but only at the ends of phrases. The stems' median drop 0.3 s after a phrase end went 14.3 dB (c27) -> 12.2 (c34) -> 17.5 (c39). The final chord's late decay is 1.17 s (c27 2.41, c34 2.05), within the 1.1-1.6 s that recordings give. Inside phrases the texture is as smooth as it was in c27. The master's level movement within each second (P90 minus P10 of 20 ms levels, 1-4 kHz, median over 1 s windows) is 5.0 / 5.0 / 5.2 dB in c26 / c27 / c39, against 7.2 dB in the Dvořák introduction (250 Hz-1 kHz: 4.8-5.0 against 7.1). Halving the hall did not change this number, so the remaining smear comes from how the notes are played: long sample releases on the legato rows, and slur boundaries that sound the same as legato joins. It is lowest in the string-led themes: bars 53-56 5.0, 57-60 4.8, 61-62 3.7, 65-70 4.4, 71-78 4.7, 79-82 4.8. The wind solos and pizzicato passages measure 6.2-7.6 (bars 15-18, 37-48), close to the recording. Measured: no loop pulsing on the master (autocorrelation at 3.95 s of the 100-300 Hz band and of the centroid between -0.27 and +0.04 over the opening, bars 3-6, 65-70 and the coda). Delivered bars 61/62 -11.1/-11.4 dB against 79/80 -13.8/-14.4, so the climax order holds without bar 79 sounding weak. The weakest passages are now the string themes of bars 53-60 and 71-82 (smooth, little articulation), the phrase ends of the divisi tracks, and the opening wind chord, where Clarinet 2 has dropped out of the balance.

## 1. The planned release caps miss most string and horn phrase ends: extend them to the legato rows and the divisi tracks (measured)

Where: every string and horn phrase end. The worst in c39 (stem drop 0.3 s after the note-off): Violins II div qn 124 7.5 dB, Violas div 268 6.8 and 74 7.8, Violins I 218 9.2, Violas 172 10.7, Violins II 124 10.8, Violoncellos div 286 10.9 and 66 12.4.

What is wrong: loop/ONE_TIME.md item 2 caps only "Sus MAX" and "Sus Marc LITE" on the strings and "Sus MAX" and "LegRep RRx4" on the horns. Most notes, and most phrase ends, play the legato rows (parts.json art_counts: Violins I 92 legato notes of 109, Violins II 122 of 151, violas 150 of 286, celli 113 of 127, Horn 1 47 of 51). The legato rows' first-note sustain groups ship the same long releases as Sus MAX (patch files, read with opus_state: 1st and 2nd Violins and Violas "1V"/"V2" pp 562-931, p 524, mf 394-524, f 333-428, ff 323-524 ms; Violins II slur sustains "V2s" up to 931 ms; Celli and Basses "1V"/"Db" pp 931, p-ff 237-700; 1FH and 1FHs pp 562, mf 394, f 316 ms). On top of these, release-trail groups ship 1245-1741 ms (Violins, Violas legato and Horn), 1660 ms (Violas Sus MAX) and 2371 ms (Celli Leg Slur MAX and Leg BC MAX). Flautando (Violins II bars 37-40 and Violins II div) ships 645 ms with an 848 ms trail.

Evidence (c39 stems, phrase ends with at least 1 s of silence after, median drop at +0.05/+0.15/+0.3/+0.6 s): strings on legato rows 1.9/7.6/15.8/23.8 dB (19 ends), strings on Sus MAX 3.3/5.0/11.8/21.3 (9), Flautando 1.6/6.9/9.4/25.9 (2), horns on legato 2.4/8.9/17.4/24.4 (6), winds 3.5-4.4/12.1-12.8/17.9 (48). The strings fall half as fast as the winds over the first 0.15 s. Movement I's caps took strings to 8.5-13 dB at 0.15 s (mockup-kit LEARNINGS, "Too wet and mushy").

Fix (build/mix.json, read by `tools/build_reaper.py cap_release`, in the same full rebuild as ONE_TIME):
- Violins I, Violins II, Violas, Violoncellos, Double basses: `"sus_release_cap_ms": {"ms": 150, "dyn": ["pp","p","mf","f","ff"], "rows": ["Sus MAX","Sus Marc LITE","Leg Slur MAX","Leg BC MAX","Leg Port MAX","Flautando"]}`. cap_release already leaves the "TLeg" transition groups and the release trails alone.
- Name the divisi and solo tracks explicitly, so they are not read as outside "every section string track": Violins II div (rows ["Flautando"]), Violas div and Violoncellos div (Sus MAX plus the legato rows), Violin I solo (["Leg Slur MAX"]).
- Every horn track and Horns 1-2 a2: add "Leg Slur MAX" to the 237 ms rows.
- If the dump shows the legato first-note groups are shared with the transition path, use 237 ms (the patches' own legato release) instead of 150 on the legato rows.
- As a second key on the celli and violas only, `"rt_ms": 400` (Movement I c22 used this on its violas; the trails are 2371 and 1660 ms). Measure it, keep it only if no phrase end falls more than 10 dB in its first 0.05 s.

Check after the render:
- String phrase-end drop at +0.15 s of at least 9 dB, with the legato-row and Sus MAX medians within 2 dB of each other.
- The join dips inside slurs (hall38.py "joins", median 2.5 dB in c39) not more than 1 dB deeper. A deeper median means the outgoing legato voice's release was covering the transition: go back to 237 ms on the legato rows.
- Refit the re-bow fills with fit_rebows.py as ONE_TIME says.

## 2. Slur boundaries in the string themes are no more audible than legato joins (measured; fix inferred)

Where: Violins I/II and celli, bars 53-60 (qn 171-204) and 71-78 (qn 238-262); also bars 23-30 (qn 66-90).

What is wrong: a new slur means a new bow. In a section that is a small re-articulation, clearly different from a finger change inside a slur. In the render the two cannot be told apart. Median dip at the join (30 ms windows, c39 stems), slur-start joins against joins inside a slur:

| Track | qn 171-204 (slur start / inside) | qn 238-262 (slur start / inside) |
|---|---|---|
| Violins I | 3.0 / 3.0 dB (7 / 20 joins) | 2.6 / 2.7 |
| Violins II | 1.9 / 2.4 | 2.7 / 0.2 |
| Violoncellos | -1.2 / 1.0 | 4.0 / 2.6 |

These are the bars with the lowest within-second level movement in the whole render (finding above: 4.7-5.0 dB against 7.2 in the recording), and they have not changed since c27. Earlier cycles deliberately softened bow-change joins (`BC_SOFT` notches, JOIN_NOTCH cuts over transition peaks) to remove ticks. That was right for the ticks, but the printed phrasing went with them. This is what most still sounds like a machine in the loud string passages.

Fix:
- Add a generic option in `tools/score_to_parts.py`, e.g. `BOW_CHANGE_DIP = {"tracks": ("Violins I","Violins II","Violas","Violoncellos"), "db": 3.0, "pre_s": 0.08, "post_s": 0.06, "min_prev_qn": 0.75}`, with movement II's spans in build/score_config.py (171-204, 238-262, 66-90).
- At every string note that starts a printed slur directly after a note of the same track (not tied, no rest, the previous note at least 0.75 qn long), write a pre-hall CC7 dip of 3 dB. It runs from the onset minus 0.08 s down to the onset and back by the onset plus 0.06 s. Use CC7, not the volume envelope, so the hall's ring is kept (S3).
- Skip onsets that already carry a JOIN_NOTCH or BC_SOFT notch, or take the deeper of the two.

Target: slur-start dips 2-3 dB deeper than the inside-slur dips on all three tracks, and the master's 1-4 kHz within-second movement over bars 53-60 and 71-78 up by about 1 dB. Check no new 30 ms peak over 2.5 dB at those joins.

## 3. The drier hall and the 160 Hz low cut took 3-7 dB off low notes with no data change (measured; cause inferred)

Where: Clarinet 2's E flat 3 at sq 6.0 and 15.0 (the opening wind chord, bars 3-6); celli E flat 3 at 63, 64.843, 136, 170, 200, 238; basses at 136, 220, 221.8; bass clarinet at 29 and 93; timpani at 277.

What is wrong: c37 against c39, each note's level change minus its volume-envelope change (the MIDI and envelopes are identical at these notes):
- Clarinet 2: 6.0 -7.0 dB, 15.0 -5.7.
- Violoncellos: -3.1 to -4.0 on all six E flat 3 notes.
- Double basses: -3.0 to -3.2.
- Bass clarinet: -3.3 and -3.6.
- Timpani 277: -3.8.

No higher note on any track moved by more than 3 dB, except Violas 218 at +3.7 and the cor anglais and Violins II at 266/264 by about -4.3. The low notes evidently got much of their level from the hall, and c38's low cut and halved return removed it. Results:
- Bars 3-6: Clarinet 2 fell from level with the bass clarinet and over Horn 3 (c37 -49.2/-47.5/-49.3/-49.8 dB per bar) to 5-6 dB under Horn 3 and the bass clarinet (c39 -55.7/-54.9/-48.7/-55.5 per bar). The opening A flat chord has lost its middle voice.
- The master's 100-250 Hz share went from -8.81 (c37) to -9.26 dB (c39), against -6.6 / -8.75 / -7.55 in the three references.
- The 250-500 Hz share is now -5.58, slightly over the references (-5.95..-6.34). The low-mid weight sits at 250 Hz instead of 125 Hz. The celli and basses make 71% of the 100-250 Hz band.

Fix (after the c40 rebuild, which may move these notes again):
- Re-run the same comparison: per note, the audio change minus the envelope change against c37. Restore the notes that lost 3 dB or more with `build/note_trims.json` (Clarinet 2 6.0 and 15.0 about +6 dB).
- Raise the low strings: `gain_db` +2 dB on Violoncellos and Double basses (and Violoncellos div) in build/mix.json, or the celli's existing 160 Hz bell +2. Aim for a 100-250 Hz share of about -8.5 dB.
- Keep the low cut and the fx_volume (Dan's request).

## 4. Start the IR envelope at 0.7, not 0.5, on this movement (measured on c39, inferred for the change)

Where: the hall (`reverb.ir_setup`, loop/ONE_TIME.md item 1).

What is wrong: Movement I needed the IR envelope because its late decay ran 2.13 s. Here the drier return alone has already brought the late decay to 1.17 s after the final chord (c38 1.19). The stems fall a median 35.6 dB in the first second after a phrase end. Both are inside the recordings' range (1.1-1.6 s; 13-17 dB at 0.3 s on the master in recordings, 17.5 dB on the c39 stems). What still sounds mushy is the sample releases (finding 1) and the unarticulated legato (finding 2), not the hall's length. endPos/decayLength 0.5 took a test track's late slope from 2.61 to 1.54 s in Movement I, about 40% shorter. Applied to 1.17 s, that would give about 0.7 s, under ONE_TIME's own 1.0 s floor, and the coda's morendo would end in a dry room.

Fix: `"ir_setup": {"envelopeMode": 2, "endPos": 0.7, "decayLength": 0.7}` first. Then measure with hall38.py: late decay after the final chord 1.0-1.3 s, and stem drop at +0.3 s at least 17 dB. Use 0.5 only if the late decay stays above 1.3 s. Record both numbers as ONE_TIME asks.

## 5. The divisi tracks' send is still the one chosen for the old, wetter hall (inferred; measure after finding 1)

Where: Violins II div (bars 37-40), Violas div (bars 23-30, 80-81, 84-92), Violoncellos div (bars 18, 21-22, coda 4 soli), Violin I solo (send 0.8).

What is wrong: these Close-only tracks send 0.5 to the hall (0.8 on the solo) against 0.25 on the sections. The values were set so they would sit as deep as the sections in the 0.19 hall (mockup-kit LEARNINGS section 12). They have the slowest phrase ends in the render (Violins II div 7.5 dB and Violas div 6.8-7.8 dB at +0.3 s, against 17.4-20.7 on Violins I and the violas). Part of that is the Flautando and Sus MAX pp releases (finding 1), and part is that they carry twice the sections' share of hall.

Fix: first let finding 1's caps act. If their +0.3 s drop is still under 12 dB in c40, lower the send to 0.35 on the three div tracks (and Violin I solo 0.8 -> 0.6) in build/mix.json. Re-match their level by gain so the early-tail ratio against their section matches.

## Do not touch

fx_volume 0.095 and the 160 Hz hall low cut (Dan); the climax order (delivered bars 61/62 2.7-3 dB over 79/80) and the c39 bar 61-62 / 79-80 balances; the re-bow layout (no loop pulsing on the master in any long hold); the final chord's CC11 fade to 8, which makes the planned release caps safe there; the wind solos' shaping and level (bars 15-22, 31-50: within-second movement 6.2-7.6 dB, close to the recording); Trombone 1's quotation and its CC7 lanes.
