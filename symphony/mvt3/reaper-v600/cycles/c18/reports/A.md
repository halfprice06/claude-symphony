# Cycle 18, critic A: articulation and phrasing (on the c17 render)

All numbers were measured on `cycles/c17/render/` stems and master and on `build/parts.json`, unless marked "inferred". Stems are post-fader; "fader removed" means the `vol_db` value at the note was subtracted. Nobody heard the audio.

Limits of this report. Not measured this cycle: loop pulsing folded at 3.95 s, the stops of bars 2 / 166 / 204 and their return rides, the section make-ups of bars 1-10 and 83-98, the pizzicato velocity refit, the F2 region gain (decided from the actor's numbers only), harp, cymbals, bass drum, the divisi and "4 soli" passages, class leads in 247-270, the dal niente entries. Of the required reading I read BRIEF.md, c17 CHANGES.md, the c17 report A, FINDINGS parts 1 (section 4), 2, 4 (sections 11-12) and 6, and MANUAL-READING / the roles and mix tables; HISTORY.md, the two LEARNINGS files and EW-TEMPLATE-PLAN.md were searched by keyword, not read in full.

Dan's note after c17 ("The accents are little bit over done now") is taken as the rule for finding 1: no accent is to be raised to +3 dB.

## Manual notes

Third round, own choice of pages: May 2021 HO manual, PDF pages 92-94 (string shorts), read in full.

| Manual (PDF page) | Where it applies | Does the render follow it |
|---|---|---|
| p.94, Staccato On Bow: the bow does not lift at the end of the note but comes to a full stop | Double basses, eighths of bars 199-210 and 247-277 (qn 792-840, 984-1108), 320 strokes on "Stac On Bow RRx9" | The row is used, but its strokes are slow at these pitches: an isolated stroke takes 95 ms to half amplitude and 140 ms to its peak, and the eighth is 167-181 ms. Finding 2. |
| p.93, Marcato: "notes of a short duration that begin with a strong accent", 4 round robins; the Basses also have Marcato Long | the same eighths ("Marc Shrt RRx4" is loaded on the Basses KS Master, key 77) | Not used. c16 tested it for separation only (8.0-11.0 dB against 9.8-12.8). Its start time has never been measured. Finding 2. |
| p.93, Spiccato: the bow is in contact "for a very short time"; 9 round robins | the same eighths ("Spiccato RRx9" exists on the KS Master, key 84, not loaded) | Not used, not tested. A candidate for the off-beat eighths. |
| p.94, Staccatissimo: like Staccato but shorter | the same eighths ("Staccatissimo RRx9" is loaded, key 75) | Not used on the basses, not tested. |
| p.94, Shorts MOD SPEED: CC1 moves through Staccatissimo, Staccato, Staccato On Bow, Marcato Short; 8 round robins | beat weight on the eighths (strong beat on Marcato Short, off-beat on Staccatissimo, one patch) | Not used. It needs another instance or a patch swap on the basses track, so it is a pass-2 test only. |
| p.94, Repetitions: about a dozen bowed repeats in one sample, with release trails, not round robin | hammered eighths | Not used (MANUAL-GAPS: the fixed speed has to match 168-184 qn per minute). Unchanged. |
| p.92-94: every staccato patch is a round robin of 9-16 samples | all short rows | Confirmed on the basses: with the CC16 resets the nine samples repeat exactly (the same position reads within 2-4 ms on six passes), and the nine have different starts. Finding 2. |

MANUAL-GAPS items that bear on the findings: individual accent rows stay closed (Dan: weight, not bite, and now "over done"); region volumes and row volumes in the Opus state are the tools for findings 1, 3 and 5.

## Findings, ranked

### 1. Accents are too large on some tracks and are a bulge after the front, not a weighted front (measured; the new values partly inferred)

Where: every printed accent on wind, brass and string tracks (`INSTR_POST["accent"]`, `_C17_ACC`, `_C17_ACC_SHAPE`).

What I measured (single notes of 0.12 s or longer, accent over the mean of its unaccented neighbours within 4 qn, fader in):

| track | n | median | 75th pct | 90th pct | over +4 dB | over +6 dB |
|---|---|---|---|---|---|---|
| Flute 1 / 2 | 46 / 33 | +4.7 / +4.3 | +6.9 / +7.9 | +9.1 / +8.9 | 24 / 17 | 17 / 14 |
| Contrabassoon | 10 | +3.7 | +6.1 | +7.2 | 5 | 3 |
| Horn 1 / Horn 4 | 28 / 6 | +3.7 / +4.3 | +6.2 / +6.7 | +7.5 / +12.6 | 13 / 3 | 8 / 2 |
| Violins I / II | 56 / 52 | +2.7 / +3.3 | +5.0 / +4.5 | +7.2 / +6.5 | 22 / 18 | 9 / 8 |
| Violoncellos | 41 | +2.9 | +6.4 | +7.5 | 16 | 12 |
| Bassoon 1 / 2 | 37 / 20 | +2.3 / +2.8 | +5.5 / +5.1 | +7.7 / +7.4 | 12 / 8 | 7 / 4 |
| Clarinet 1 / 2 | 33 / 11 | +2.8 / +3.2 | +4.3 / +4.0 | +8.6 / +5.9 | 11 / 3 | 6 / 1 |
| Trombones, Tuba, Bass clarinet | 6-20 | +2.0 to +2.3 | +2.5 to +4.7 | +2.9 to +5.9 | 0-4 | 0-1 |
| Oboe 1, Horn 3, Trumpets 1 / 2, Double basses | 7-38 | +0.2 to +1.4 | +2.4 to +7.2 | | | |

The medians agree with the actor's table. The spread is the problem: a quarter of the accents on flutes, Horn 1, celli, bassoons and contrabassoon stand 5-8 dB over their neighbours. Part of the largest values (bars 6, 94, 113: +13 to +26 dB) are entries after a rest whose only neighbour is a soft note, so read the 75th percentile, not the maximum.

Shape. Level of accented notes of 0.6 s or longer in four windows after the note-on, against the same note at 0.45-0.60 s (plain f/ff notes in brackets):

| track | 0-60 ms | 60-160 ms | 160-300 ms | 300-450 ms |
|---|---|---|---|---|
| Flute 1 | -2.5 (-1.9) | +1.7 (-0.1) | +1.7 (-1.2) | +2.0 (-0.5) |
| Bassoon 1 | -1.2 (-3.1) | +0.8 (-1.3) | +1.9 (-0.2) | +1.4 (0.0) |
| Contrabassoon | -0.1 (-2.5) | +1.5 (-0.7) | +2.1 (-0.1) | +1.2 (0.0) |
| Bass trombone | -2.8 (-4.6) | +2.4 (-0.5) | +2.0 (-0.2) | +1.2 (+0.4) |
| Horn 1 | -6.1 (-4.0) | -0.2 (-2.9) | +1.3 (-0.8) | +0.9 (-0.5) |
| Violins I | -2.8 (-0.3) | -3.1 (-0.3) | -0.3 (-1.4) | +0.2 (-0.9) |
| Violins II | -5.4 (+0.6) | -3.5 (-2.0) | -0.9 (-2.8) | -0.3 (-1.5) |
| Violoncellos | -0.1 (-0.9) | +1.0 (-1.9) | +0.4 (-2.7) | +1.1 (-1.3) |

On every family the extra level sits from 60 ms to 450 ms after the onset. The first 60 ms are no stronger than on a plain note (on the violins and Horn 1 they are 2-5 dB weaker relative to the body). So the accent is heard as a swell that lasts about 0.4 s after the note has spoken: a bulge, not a hit. The cause is the shape (`hold_s` 0.15, `end_s` 0.45) on rows whose level follows CC11 with a lag.

Brightness. The 2-5 kHz level of the first 80 ms against the note's own body is the same or lower on accented notes than on plain f/ff notes on 24 of 27 tracks (for example Violins I -11.3 against -6.5 dB, Horn 1 -33.7 against -20.5). Exceptions: Trombone 2 (+6.7 dB against plain notes), Bass trombone (+5.2), Double basses (+4.4). On the two trombones the CC1 part of the accent is the likely cause (CC1 88 -> 103 on the bass trombone). In the master the 2-5 kHz front over body at accent onsets is negative at every size of tutti (medians -4.3 to -6.1 dB). So there is no bite; the fault is size and length.

Doubling. At onsets where 16 or more staves carry an accent (24 onsets) the master's first 0.2 s stands a median 2.0 dB over the same chord 0.45-0.65 s later; with 9-15 staves +1.2 dB; with 1-8 staves 0.0 to +0.8 dB. Against c16 the same measure rose by a median 1.0 dB (90th percentile 2.0 dB) at the 43 onsets with nine or more accented staves. The loudest in the master: bars 91-92 (qn 360-366, 22-26 staves, front 4.7-10.8 dB over the later body, partly because the notes are short), bar 132 (qn 524, 17 staves, +9.1), bar 277 (qn 1104 / 1106, 21-22 staves, +5.5 / +5.9), bars 266-270 (qn 1060, 1068, 1076, 9 staves, +3.6 to +4.4).

Why Oboe 1 / 2, Horn 3, Trumpets 1 / 2 and the basses read low. This is not a missing bump, and they should not be raised:
- Oboes: per-pitch sample level on "Sus MAX". Against the track median at CC11 98 or more: C5 -7.8 dB (both oboes), D5 -5.8, E flat 5 -2.9, E5 +3.6, F5 +8.7 / +9.3. C5 also starts slowly (-54 dB in the first 50 ms, -45 dB at 0.3-0.45 s; F5 is flat at -31 dB). Most printed accents sit on C5 (qn 72, 100, 600, 632, 660, 1072, 1104, 1106) and read -3 to -6 dB; those on F5 (qn 358, 612, 644, 1092) read +9 to +13 dB.
- Oboes, Trumpets 1 / 2, Horn 1: the accented note is on the sustain row and its neighbours on "Leg Slur MAX", and the legato row is louder at the same pitch: Trumpet 1 +4.2 dB, Trumpet 2 +3.3, Oboe 2 +3.2, Horn 1 +3.2, Oboe 1 +2.1, Flute 1 +1.7. Trumpet 1's accents next to sustain notes read +3.9 dB, next to legato notes -3.0 dB.
- Double basses: the accents of bars 27-34 lie on C3-G3 (pitches 48-55), which play 9-10 dB under the track median on "Sus MAX" (D3 -9.0, E flat 3 -8.7, F3 -10.3). The region gains of c17 cover E flat 1 to F2 only.
- Horn 3: accents between sustain notes read +1.0 dB with CC11 100 -> 121 and CC1 108 -> 115, where Horn 4 reads +3.8 with 88 -> 106. Leave it.

Fix (`build/score_config.py`, last block):
- Target: median +1.5 to +2 dB per track, no accent over about +3 dB, and the extra level inside the first 0.2 s.
- `_C17_ACC_SHAPE = {"pre_s": 0.03, "hold_s": 0.05, "end_s": 0.20}` (the CC1 part of the brass keeps `pre_s` 0.08). This is the largest change a listener will hear: the bulge at 160-450 ms goes.
- Amounts (from the measured dB per unit of the c17 bumps): strings `amt` [(46, 5), (72, 6), (88, 9), (114, 11)], `max` 118 (Violins II and Violoncellos (114, 10)). Woodwinds [(34, 2), (46, 4), (72, 7), (88, 10), (114, 13)], `max` 118; flutes [(88, 6), (114, 8)]; contrabassoon [(88, 8), (114, 10)]. Brass `amt_rel` 0.21 -> 0.16 (trombones, tuba, Horn 3), Horn 1 0.16 -> 0.08, Horns 2 / 4 0.21 -> 0.11, trumpets 0.13 -> 0.10, clarinets 0.21 -> 0.13. Remove the CC1 part on Trombone 2 and Bass trombone (the only brighter fronts) and halve it elsewhere (horns +3, others +2).
- Doubling: scale the bump by the number of staves that carry an accent at the same score onset: 1-8 staves 1.0, 9-15 staves 0.75, 16 or more 0.6 (new key in `instr_post.py` `accent`, for example `"tutti_scale": [(9, 0.75), (16, 0.6)]`, counted from `mockup-events.tsv`).
- Even the level under the accents instead of pushing them (these also fix row-to-row jumps a listener hears on plain notes):
  - `mix.json` `region_gain_db`, both oboes, "Sus MAX": C5 +6, D5 +4.5, E flat 5 +2, E5 -3, F5 -7; "Leg Slur MAX": C5 +3, D5 +1.5, E5 -3.5, F5 -4. Check on a range render (bars 151-166) before the full render; the scherzo's cor anglais A4 did not take a region gain.
  - Double basses "Sus MAX": pitches 48-55 +6 dB (range test on bars 27-34; the old low-pitch gains stay).
  - `_C17_NOTE_CC` `row_dyn` on the legato rows of Trumpet 1 and 2: "Leg": [(72, 0), (88, -12), (114, -18)] CC11 units (CC11 is plain volume there; 100 -> 82 is about -3.5 dB); Horn 1 and Oboe 2 "Leg": [(88, -8), (114, -12)]; Oboe 1 [(88, -5), (114, -8)].
  - The c17 string `row_dyn` overshot on two tracks: legato minus sustain at the same pitch now reads Violoncellos +3.2 dB and Violas -3.7 dB (Violins I -0.4, Violins II -1.7). Violoncellos "Leg" (114, 10) -> (114, 2); Violas "Leg" (114, 10) -> (114, 22) or "Sus MAX" (114, -2) -> (114, -12).
- Check after the render: per-track median +1.5 to +2, 90th percentile under +3.5, the four-window shape within 1 dB of plain notes after 160 ms, master front over later body under +1 dB at the 16-stave onsets.

### 2. Double basses' eighths (bars 199-210, 247-277): the row is too slow for the figure, so no lead can put the strokes on the beat; the timing dispute settled (measured)

Detector, stated. Stem band-passed 30-2000 Hz, Hilbert envelope smoothed with a 25 ms Hann window (longer than one period of F1, 23 ms). For each stroke, in the window from 10 ms before its note-on to the next note-on plus 30 ms: the envelope minimum before the peak, the peak, and the half-rise (first time the envelope passes minimum + half of peak minus minimum, in amplitude).

Checked on a stroke whose start can be read: qn 816 (bar 205), A flat 1, the first stroke after the silence of the bar 204 stop (0.77 s of digital silence before it in the stem). The waveform starts at the note-on (0 ms; -61 dB peak in the first 5 ms). Peak level in 5 ms steps: -50 dB at 15 ms, -41 at 35 ms, -37 at 55 ms, -35 at 75 ms, -32 at 100 ms, -30 at 120 ms, -29 dB (the maximum) at 140 ms. The detector reads the half-rise at 95 ms after the note-on, which agrees with the waveform (6 dB under the peak is passed between 75 and 100 ms). With the 40 ms lead that is +55 ms after the beat, and the peak is +100 ms after the beat. The note itself is 75 ms long: the sample goes on rising for 65 ms after the note-off. In the 110 Hz high-pass band that the c16 detector used, this stroke never exceeds -47 dB (16 dB under its fundamental band), and the actor's 30-300 Hz detector with 6 ms frames is shorter than one period (19 ms at A flat 1). Neither was reading the stroke.

On the running eighths the same detector gives:

| span | n | half-rise against the beat, median (10th-90th pct) | SD | peak against the beat | depth of the dip between strokes | within 25 ms of the beat |
|---|---|---|---|---|---|---|
| 792-816 | 40 | +1 ms (-48 to +84) | 54 | +40 | 6.6 dB | 17 |
| 816-840 | 48 | -2 ms (-49 to +95) | 58 | +83 | 8.2 dB | 6 |
| 984-1056 | 128 | +3 ms (-45 to +78) | 47 | +44 | 7.7 dB | 54 |
| 1056-1108 | 104 | +11 ms (-50 to +65) | 47 | +75 | 6.3 dB | 52 |

c16 by the same detector: +20 / +7 / +4 / +24 ms, depth 5.3-7.1 dB. The other strings' short rows by the same detector: half-rise +6 to +51 ms, peak +30 to +128 ms, depth 10.4-19.4 dB.

What this settles:
- The medians say "on the beat", but they are not a timing of strokes. The dip between strokes is only 6-8 dB, the previous stroke's tail sets the minimum, and the half-rise of a single stroke scatters over 130 ms inside a 170 ms slot. In 28 of the 104 strokes of 1056-1108 the envelope has no rise at all inside the stroke's window (the stroke is under the tail of the one before). Both earlier readings were of this scatter. Neither the c16 "late" nor the c17 "early" is right; the strokes are smeared.
- The round robin is real and fixed. On the C2 strokes of 1056-1108, before the level changes, the same round-robin position reads the same on each pass: position 2: 64, 61, 60, 62, 60, 61 ms; position 4: 37, 36, 37, 33, 35, 36; position 1: 50, 42, 44, 41, 45, 42; position 3: 113, 93, (30), 111, 109, 109; position 8: 83, 94, 85, 93, 92; positions 0, 5 and 7 mostly have no rise. So the nine samples do start differently (33 to 113 ms), as the c16 report said, but the values are those of a stroke on top of the previous tail, and they changed when CC11 began to alternate. A per-position table cannot be fitted from a running passage.
- An isolated stroke needs 95 ms to half amplitude and 140 ms to its peak. The figure's slot is 167-181 ms. A lead that put the half-rise on the beat (0.095 s) would start each note before the previous one has reached its peak. The row cannot articulate this figure at this tempo and register. That is why the basses' eighths stay weak in Movement I too.

Fix:
- Do not change the lead of "Stac On Bow RRx9" again (keep 0.04 s) and do not add per-position leads.
- Under the lock, one calibration range (one build, about 40 s of audio, the Double basses track alone, added after bar 279 or in a pass-2 project): for each of "Stac On Bow RRx9", "Marc Shrt RRx4", "Staccatissimo RRx9" and, if memory allows the row, "Spiccato RRx9" (KS Master key 84; `ks_maps.json`): CC16 reset, then nine strokes one second apart on A flat 1, C2, D2 and F2 at velocity 100 and CC11 105, note length 0.08 s. Read each stroke with the detector above (start = first sample over -60 dB, half-rise, peak, level). This gives the true note-on-to-half-rise of every sample, which no running passage can give.
- Choose the row whose median half-rise is under 50 ms and whose nine samples lie within 25 ms of each other, set `row_onset` `lead_s` to that median minus 0.015 s, and use it in `ART_SPANS["Double basses"]` for 792-840 and 984-1108. If only "Marc Shrt RRx4" qualifies, use it on the half-note beats and the shorter row on the off-beats (the beat weight then comes from the row, and the CC11 -22 on off-beats can go to -8). Refit the row's level with `row_volume_db` (the short rows stood 9-11 dB over the sustain strokes in c16), and delete the fitted role rows `Double basses [792, 840, -4.0]` and `[984, 1080, -2.0]`.
- Target with the same detector: dip between strokes 10 dB or more (the other strings' rows give 10-19), half-rise SD under 25 ms.
- If no row qualifies, say so in LEARNINGS and leave the figure; I see no other instrument-side fix.

### 3. The chorale's bar-line dips (bars 229-233) are the common breath of the whole orchestra, not the pedal's bow change (measured)

Where: qn 912-932, master and every sustaining track.

The master's lowest 20 ms frame lies 20-50 ms before each bar line (916: -4.3 dB at -50 ms; 924: -5.2 dB at -20 ms; 932: -1.8 dB at -40 ms; the actor's -5.5 / -3.2 / -5.5 / -3.2 / -2.6 are the same holes). At that instant the stems read, against their own level in the 0.26 s before: Clarinet 1 -13.8 / -9.7 dB (the loudest stem in bar 229 together with Violins I), Oboe 2 -10.9, Flute 2 -8.7, Bassoon 2 -8.6, Violoncellos -5.1 / -7.4, Violas -3.0 / -5.2, Trumpet 1 -5.2, Trumpet 2 -4.3, Violins I -5.1, Double basses -3.8. Every track ends its whole note at the same moment: woodwinds with the 68-85 ms `gap_floor`, brass with the 45 ms `gap_set`, celli and basses with a new bow on the bar line.

Test: I moved the celli stem by 2 qn and the basses stem by 1 qn inside the passage (the pedal repeats bar by bar) and summed the master again. The bar-line dips stayed where they were (920 / 924 / 928 / 932: -2.3 / -5.2 / -2.8 / -1.8 as rendered, -1.7 / -5.7 / -2.1 / -2.2 after the move). So neither a longer no-split limit nor interleaved re-bows on a second instance nor a CC11 swell on the pedal will reach the 2 dB target. The measure also has a floor: at points of the bar where nothing changes (+1 and +2 qn) the same measure reads -0.8 to -5.3 dB, because the tremolo and the roll fluctuate.

The brass breath itself is now right: per-track dips of 3-9 dB at chord changes (Horn 1 -3.6 to -9.0, Trombone 1 -2.4 to -9.7, Tuba -5.1 to -7.7), back to level within 0.5 s. Same-pitch whole notes still re-attack (Horn 1 at 896 / 900 -8.7 / -9.0 dB; Trombone 1 at 920-928 -2.4 to -3.2 dB, which is the weakest: S1).

Fix (`build/score_config.py`, `INSTR_POST`):
- `gap_set` for the woodwinds in 888-936.5, notes of 3 qn or longer: `{"wind": [{"from": 888.0, "to": 936.5, "min_qn": 3.0, "gap_s": 0.035}]}` (oboes and cor anglais the same; they have 0.085 s now).
- Do not end every track at one instant. Give each track a fixed offset of its note end in this passage, earlier by: flutes 0 ms, oboes 15, clarinets 30, bassoons 10, horns 20, trumpets 0, trombones 35, tuba 15 (new key, for example `"end_spread_s": {track: value}` inside `gap_set`; the note-ons stay). Players do not release a chord in the same 20 ms; this is a release spread, not a timing change of attacks.
- Trombone 1's same-pitch whole notes (qn 920, 924, 928): gap 0.07 s instead of 0.045 (S1).
- The pedal is marked "change bow at will" (`mockup-events.tsv`). Move the bow changes off the bar line so they never meet the wind and brass breath: Violoncellos at bar line + 2.5 qn, Double basses at bar line + 1.25 qn (`STR_REP_NEW_BOW` / `rebow_join` positions; the printed whole notes become ties with a re-bow inside). Keep the 5 ms gap and the 8-unit swell.
- Judge by the 50 ms window at the master's minimum and by the stems' dips, with the floor above in mind: target 3 dB at the bar lines.

### 4. The sfp of bar 149 has no "sf": the front is 2.7 dB under the ff before it (measured)

Where: qn 592, every wind, brass (not the trumpets), timpani and string staff; crescendo printed from 592 to ff at 596.

Master in 0.1 s frames: -18.3 dBFS in the 0.15 s before, -21.0 at +0.05 and +0.15 s, -19.8 at +0.3 s, -27.7 at +0.5 s, -25.2 at +0.8 s, -21.6 at +1.2 s, -17.3 at +1.6 s. The soft part and the rise are right now (the hole is 9.4 dB under the chord before and lasts about 0.5 s; the `cc_cap` holds the strings at CC11 53-54 until +0.8 s; no swell of 5-11 dB as in the other movement). The front is wrong: Violins I -34.0 dBFS at +0.05 s against -31.7 before, Violas -36.4 against -32.2, Double basses -35.6 against -29.8, Oboe 1 -48.1 against -35.9, Bassoon 1 -45.6 against -40.4, Trombone 1 -33.3 against -29.1. CC11 at the front is the resting value (strings 103, winds 104, brass 100) and falls from +0.15 s; no track has a bump. The c17 change of the resting level took the sf away (c16 had 114 here).

Also here: the p of the sfp is still partly on the fader. `roles.json` rows `[593.0, 596.0, x, 3.0]` (Flutes -12, Clarinet 1 -7.5, Clarinet 2 -9, Bassoons -5.5 / -8.5, Cor anglais -6, Tuba -4.5, Horn 3 -3.5, Double basses -3, Timpani -1) move Flute 1's fader -7.8 dB within 0.5 s of the attack and +12 dB over the next 1.1 s. That is a fast fader fall under a ringing chord (S3). The same construction stands at the fp of bar 209 (`[833.25, 839.0, ...]`, eight tracks) and the sub. p of bar 219 (`[871.7, 878.0, -4, 4]` and `[872, 880, ...]`, nine tracks).

Fix:
- `INSTR_POST["cc_shape"]` at 592.0 on every sfp staff: CC11 +14 units over the resting value (strings and woodwinds to 118, brass 100 -> 112) from 0.03 s before the note-on, held 0.10 s, then the existing fall. The oboes need the region gains of finding 1 first (their note at 592 is one of the weak pitches).
- Move the three groups of sfp / fp / sub. p role rows into CC11 (`cc_cap` with the same depth: 12 dB is about 45 units on the wind rows at this level, 7 dB about 28; measure one range, bars 148-150) and delete the rows.

### 5. Fader audit: what still moves fast, and the fitted rows by cause (measured on `parts.json`; causes partly inferred from `roles.json` notes)

Count. Segments of `vol_db` steeper than 3 dB/s, merged into moves of 1.5 dB or more, final fade excluded: 845 on 28 tracks. Inside printed hairpins 263, at printed fp / sfp / sf / sub. p 52, in rests 159. That leaves 409 that are neither printed nor in a rest: 122 strictly inside a sounding note and 287 across a note edge. Point density: Double basses 2.83 per second, Violoncellos 2.63, Violas 2.53, Violins II 2.46, Violins I 2.31, woodwinds 0.85-2.16, brass 0.59-1.44 (Movement I's strings without fitted rows 0.48-0.76; Duc's Mahler 0.01-0.21).

The largest unprinted moves (track, qn, dB, seconds):
- Violins II 934.6-935.5 +9.7 dB in 0.48 s inside a note (the end of the fitted row `[888, 936, -7]`); Violins I / II 1087.5-1088 -7.5 / -8.5 in 0.20 s (start of the `[1088, 1116]` rows).
- Horn 4 551.9-553.1 -9.5 in 0.43 s inside a note (`[548, 552, 7.5]`; Horn 3 `[548, 552, 10.5]`); Horn 2 667.5-668 +8.5 in 0.18 s; Horn 3 1015.5-1016 +8.0 in 0.17 s; Trombone 1 984-984.5 +7.0 in 0.17 s.
- Bar 199 (qn 792.5-797): Flute 1 and Oboe 1 -7.0 in 0.36 s, Bassoon 1 -7.0 at 794-795 and Bassoon 2 -7.0 at 796-797, both inside notes. This looks like a hairpin-gain release with no printed hairpin there; check its source.
- qn 891.5-893 (the first bar line of the chorale): Violins I -9.0, Violas -6.0, Horns 1-4 and Violins II -5.0, Trumpet 1 -7.0 (892-893, inside the note), Bassoon 2 and Contrabassoon -4.8 (inside the note), all in 0.5-0.8 s: the arrival's settle is made by the fader inside the first chorale note on ten tracks. Move it to CC11 / CC1 (a fall of the same size from 0.3 s after the attack; Balfe's accented-brass shape, FINDINGS section 22).
- Clarinet 2 183.5-184 +9.0 in 0.18 s; Violas 456.5-458 +8.5; Violoncellos 263.5-264.5 +8.0; Flute 1 319.8-320.7 +7.0 inside a note; Violins I 167.5-168.6 -8.0 inside a note; Violins I 476.75-477 +7.0 in 0.09 s (end of the "4 soli" row); Bass trombone 1031.9-1032.15 +6.0 in 0.09 s inside a note; Violoncellos 1030.9-1031.7 -5.9 inside a note; Double basses 488-488.5 +5.0 inside a note.
- A group of exactly -4.0 dB over one quarter at 440-441, 598-599, 840-841, 987.5-988.5 on four to seven wind tracks, several inside notes: a release of a 4 dB hairpin gain or unison level after its span. Key these to the next rest or drop the gain.
Rule for the actor: any role or gain whose edge falls inside a sounding note takes a ramp no steeper than 3 dB/s, or moves to the nearest rest of 0.2 s or more; `vol_guard` now catches only 2 dB inside 60 ms.

The fitted rows that c17 lists as stopgaps, by cause:

| rows | cause | what to do |
|---|---|---|
| Violins I / II, Violas `[792, 816]` (-1.3 / -3.3 / -2.0), `[984, 1056]` (-0.9 / -2.5 / -2.4), `[40, 104]`, `[600, 680]` (+0.7 to -5.0); Violoncellos `[792, 816, 1.1]`, `[984, 1012, 2.0]` | mapping: the passage plays on one row ("Sus MAX"), which stands over the legato row | delete; put the value into `row_dyn` "Sus MAX" at ff for those tracks (0.15 dB per unit: Violins II -3 dB is about -20 units, too much for one lane, so split: `row_volume_db` "Sus MAX" -1.5 dB on Violins II and Violas plus -8 units) |
| Violins I / II, Violas `[1088, 1116]` (-7.5 / -8.5 / -4.0), Violins II `[888, 936, -7]` | sample level: the tremolo row and two- and three-note chords at CC11 118-124. The tremolo stems read -36.4 / -33.0 / -36.1 dBFS after a fader of -7.2 / -8.5 / -4.0, where the sustain notes of 1056-1088 read -38.0 / -40.9 / -35.0 with no fader | delete; `row_volume_db` "Tremolo": Violins I -3 -> -6, Violins II -4 -> -8, Violas 0 -> -2; `note_cc` by chord size on the tremolo and sustain rows: 2 notes -10 units, 3 notes -16. The single-note tremolos of 888-936 and 1000-1080 (fader -1.0 to -3.6) then need about +2 dB from CC11, which they have room for (CC11 72-114). The chord CC rule of ruling 9 is this item. |
| Double basses `[792, 840, -4.0]`, `[984, 1080, -2.0]` | sample level of the short row | delete; `row_volume_db` of the row chosen in finding 2 |
| Trumpet 1 `[680, 684]` to `[728, 732]` (0 / -1 / +2 / +5 / +1.5 / 0 / -6.5 / +3.5) | sample level by pitch on "Mute Sus"; bar means of a removed per-note layer (a row of 4 qn covers one to three notes) | delete all eight; refit the `note_cc` pitch table on "Mute Sus" from one range render of bars 171-186, or use `region_gain_db` on the row |
| the ride rows at 164 and 679 | phrase decision (stop rides) | keep |
| sfp / fp / sub. p rows at 593, 833.25, 871.7 / 872 | CC and envelope pair for a subito | move to CC11 (finding 4) |
| the `[x, y, 3.0, 4]` rows on Bass trombone, Tuba, Bass clarinet, Bassoon 2, Contrabassoon, Double basses (13 tutti spans, c01) | phrase decision (bass octave in the tuttis) | keep; give them the 3 dB/s edge rule |
| Horn 3 / 4 `[548, 552, 10.5 / 7.5]`, Horn 2 `[668, 676, 8.5]`, Horn 2 `[296, 310, 6]` | phrase decision with a size (7.5-10.5 dB over 4 qn) that points to a soft sample region | check the pitches of those notes against a region gain; then keep a smaller row |

### 6. Timpani bars 247-270: the half-bar beat is the weak stroke; tongued joins and smaller checks (measured)

Timpani, "Hrd Lng" strokes, first 0.25 s, by position in the bar (bars 247-270, 38 strokes): downbeat -36.6 dB (velocity 102), beat 2 (qn +2.0) -40.9 dB (velocity 93, nine of eleven on the low C, key 48), the eighth before each beat (+1.5 / +3.5) -39.7 / -40.3 dB at velocity 83 / 72. By key: left-hand G and C (43, 48) -40.7 / -40.6 dB at velocity 90 / 95; right-hand keys (67, 72) -39.6 / -38.2 dB at velocity 75 / 76. So the right-hand keys are still about 5 dB louder at equal velocity after the -12 steps (0.17 dB per step), and the second beat gets -4 from `TIMP_METRIC_VEL` on top. Fix: `vel_pitch` right-hand keys -12 -> -24 (floor 40), `TIMP_METRIC_VEL` "beat" -4 -> +2, "off" -10 -> -8. Bars 11-34 and 199-210 keep the beat over the off-beat (-37.7 / -38.9 and -36.2 / -37.8).
Timpani against the basses: bars 11-34 timpani stem -46.2 dBFS against the basses' -39.3, and 8 dB under them in the 30-150 Hz band; bars 151-170 -44.0 against -34.7; 247-270 -41.1 against -34.7. The +3.4 dB of c17 is not too loud against the basses. The 2-5 kHz share of the first 80 ms is -22.6 to -23.6 dB on downbeats (unchanged from the actor's -22.9).

Tongued joins. With my slur parse (score slur spans) the separation at tongued joins on the sustain rows is 4.3-9.3 dB median on every wind and brass track; the low groups are the bassoons at the 68 ms gap (Bassoon 1 2.7 dB, 74 of 143 under 3 dB; Bassoon 2 3.0 dB, 60 of 120; contrabassoon 3.5 dB), against 6.3-7.7 dB at 80-110 ms on the same tracks. Fix: `_C17_GAP` for Bassoon 1, Bassoon 2 and Contrabassoon `floor_s` 0.068 -> 0.095 (their release fills a 68 ms gap). My measure (lower body minus lowest frame) reads negative when the second note is much softer, so about a third of the "under 3 dB" cases on Horn 1 (120 ms gap, 28 of 82) are level steps, not merged notes; Horn 3's remaining cases are the chorale breaths (finding 3) and joins from the legato row. For the eighths of bars 91-92 and 277 the rows the manual offers are "Stac DblTng RRx9" on trumpets, bassoons and flutes (already used for printed staccatos; in c01 it stood 3.6-8.6 dB under the sustain notes at the same velocity and its -10 dB length is 0.24-0.29 s) and "Marc Shrt RRx4" on horns (0.31 s, 7-8 dB louder than "StacSs"). The eighth there is 0.17-0.18 s, so only the double-tongue rows fit; their cost is the lighter tone and a level refit per row. I did not measure those bars again.

Smaller decisions asked for:
- F2 on the basses (from the actor's numbers, not re-measured): with region gain +2.5 and the bell at -9, F2 reads +4.6 dB at ff and -0.6 dB below. Set the F2 region gain to 0: about +2.1 at ff and -3.1 below, both at the 3 dB limit; keep the bell at -9 (E flat 2 is level only with it).
- Pizzicato: refit the per-pluck table on a range render of bars 51-66 and 171-186 in the present state, with velocity floor 20 instead of 8 and the passage median moved up by CC11 rather than velocity, since the table runs into the floor. I did not compute a table.
- Keyswitches 7 ms before a note (ten re-bow keyswitches at 7.1 ms): the scherzo found 7 ms unsafe. Move those ten to 20 ms; this needs no `KS_LEAD_S` change.

Do not touch: the 0.04 s lead and the CC16 section resets on the basses' short row until the calibration range of finding 2 is rendered; the brass breath of 0.045 s on the chorale's chord changes (per-track dips 3-9 dB, recovered in 0.5 s); the `cc_cap` hold and rise of the strings at bar 149 (the soft part and the crescendo now read right); the resting CC11 levels 105 / 104 / 100 (they give the room the smaller accents need); the timpani's CC7 fold and stroke level (+4 dB) and the downbeat velocities; the gap floors of 0.09-0.12 s on brass and 0.085 s on oboes; the bass-octave tutti rows; the stop rides; and no per-note fader move anywhere.
