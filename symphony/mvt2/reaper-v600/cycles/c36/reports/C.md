# Cycle 36, critic C (holistic): the c35 render of v600

Lens: listen through the data as a conductor would. I compared the c35 render (stems, master, delivered mp3) with the c27 port baseline, with c30 (five cycles back), with series 1's c26 render of v77 on unchanged passages, and with the stored reference metrics (Dvořák 9/i spectrum, Brahms 1/ii and 4/ii band shares and loudness motion). Levels are plain RMS dB unless marked otherwise. Short-term loudness values come from ffmpeg ebur128 on the mp3s. Bar/qn mapping: BRIEF "The music". Each c26 file is read on its own tempo map (series 1 `build/parts.json`).

## Manual notes (group H3: May 2021 HO Opus manual, PDF pp. 82-88, Hollywood Solo Cello; MANUAL-GAPS.md read)

| PDF page | What the manual says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| 82 | Solo Cello is a separate licensed library. Its mic set is meant for a solo instrument. Dynamics and vibrato are linked on CC1, whereas the section libraries control them separately. | The solo and soli passages: Violin I solo bars 17-22 (DIV A), celli 4 soli bars 83-86 (Violoncellos div, DIV A), basses 4 soli bars 65-70 and 87-92 (full section at -3 dB) | Not installed. I checked: `Hollywood Strings Opus Instruments/` holds only section and divisi folders, with no Solo Violin or Solo Cello. The section model (CC11 dynamics, CC1 vibrato) is the right one for the KS Masters in use. |
| 82-83 | "Long Solo" patches carry a legato script that blends overlapping notes and removes strong attacks. Non-overlapping notes get their normal attack. | Every Leg Slur MAX line works the same way in the KS Masters. | Yes. A note after a gap plays as a first note. Example: Violins I at qn 72 (bar 25, "tutti") dips 12-15 dB for about 0.3 s, but Violins II in unison masks it in the master (the master shows no dip, measured). |
| 83-84 | Grand Détaché RR gives sustained notes that are each clearly attacked, with 2 round robins. | Separated notes inside a slur or a figure. The section counterpart is the Violas KS Master "Detache" row, already loaded for bars 48-51. | Partly. It is not used for the f sextuplets of bars 59-60 (finding 1). |
| 84-85 | The combined sustains (NV NV VB, NV VB VB) play non-vibrato at the soft dynamic layers and vibrato at the loud ones. | All string tracks | Yes, in effect. CC1 follows the dynamic: coda ppp Vc div, Cb and Vln I sit at CC1 38-48, and the climax Vln I and Vc at 97-100 (parts.json). The Violin I solo holds 72 (c32). |
| 85-86 | Sforzando: "a sudden, strong accent that quickly tapers off" into a quiet vibrato. Marcato Long has a strong accent with light vibrato at the end. | The bar 63 trem. sf, the fp at bar 47 | These are built with CC11/CC7 shapes. c35 measured sf weight of +2.2/+3.3 dB on Vln I and Vc, and the master holds -26 dB through 213-218 (measured). Nothing to add. |
| 86-88 | Legato bow change (normal, Fast, Smooth), Legato Slur and LegSus Slur. "Timing between legato intervals is adjusted (tighter or looser)" by note velocity. | Leg BC MAX at slur boundaries and Leg Slur MAX inside slurs on every string line. Legato targets play at v124, the Violin I solo at v72-80. | Yes, in the choice of rows. Kit LEARNINGS section 5 measured that velocity did not move crossovers on the Violins KS Master (c11), so no velocity change is proposed. |
| (H3 question) | Which passages would gain most from solo instruments | | First, the bars 17-22 violin solo: eight players on DIV A play a line marked "solo". Hollywood Solo Violin is the fix (MANUAL-GAPS #3), and Dan would have to install it. Second, the basses' "4 soli" pedals: no new library is needed (finding 4). The celli 4 soli are already on DIV A. |

## Where c35 stands (measured)

- Delivered mp3, maximum and median short-term LUFS per section (c26 / c27 / c30 / c35):

  | Section | c26 | c27 | c30 | c35 |
  |---|---|---|---|---|
  | Climax 61-64 | -9.4 / -10.8 | -11.1 | -10.2 | -9.9 / -11.0 |
  | Cadence 79-82 | -11.1 / -12.6 | -10.2 | -11.4 | -11.9 / -13.6 |
  | Bars 53-60 | -11.6 | -13.7 | -12.3 | -12.0 |
  | Coda 83-92 | -24.7 | -24.2 | -21.9 | -23.0 / -27.1 |

  The climax now leads the cadence by 2.0 LU, the best margin of series 2 (c27 0.9 under, c31 0.9 over). p10 is -28.2 LUFS.
- Master per bar against c27: bars 61-62 are +2.0/+1.4 dB, bars 79-80 -3.7/-3.6, and bars 4-5 and 35 -3 (the bass clarinet fixes). Bars 65-66 are -2.1/-1.7 and bars 85-86 -1.6/-1.9 (the coda clarinet trims). Every other bar is within ±1.6 dB. Against c30, the only changes over 1.5 dB are 55 (+2.1), 65-66 (-2.3/-2.0) and 85-86 (-3.6/-4.1). These are intended (c34/c35 roles), with no unexplained regressions.
- Against recordings: long-term spectrum within 2 dB of Dvořák 9/i from 250 Hz to 4 kHz. Band shares fall inside the reference spread, and 100-250 Hz (-8.8) sits at its lean edge. Master loudness motion 1 s/20 s is 4.30 dB (Brahms 1/ii 4.56, 4/ii 3.92). No action.
- Loop pulsing (BRIEF 8): I scanned all 28 notes held 8 s or longer (re-bow pieces merged), using the 100-300 Hz level and the centroid autocorrelated at 3.95 s. None reaches 0.3 in both measures. The strongest is the bass clarinet pedal at bars 3-6 (level 0.45, centroid 0.04, a 3.2 dB swing), which c35 already reshaped. No action.
- Line smoothness: std of 0.25-qn levels around a 2-qn moving mean, for the main melodies. It is unchanged from c26 within ±0.3 dB, with one exception: the strings of bars 23-29 rose at the port (Vln I 1.75 -> 2.80 -> 2.50, violas 1.78 -> 2.72 -> 2.49). Most of that comes from v600's new per-bar hairpins and the printed rest at 77 (26 b3), so it is not a fault.
- S1: the Violins II portato pairs (44, 47, 50, 51) dip 4.6-7.5 dB in the stem and 3.0-4.0 dB in the master (measured). They pass.

## Findings, ranked by what a listener would hear

### 1. Bars 59-60 (qn 196-204, f, poco a poco animando into the climax): the violas' sextuplets are a smeared wash, not a figure (measured)

- Where: Violas, 48 slurred sixteenth-sextuplets, six to a bow (`bSec.ily` line 239: "six notes per bow (one beat) at f"). They are the rhythmic motor of the last two bars before the bar 61 ff.
- What is wrong: all 48 notes play Sus MAX at 0.157 qn (about 0.15 s each) with v100 (parts.json `ks`: Sus MAX at 195.94 until Tremolo at 203.94). A sustain attack that short never reaches its body. Each note blurs into the next, so the listener hears a chord buzzing at the figure's pitches.
- Evidence (measured, stem): I compared the energy at each note's own pitch (harmonics 1-3, ±half a semitone) with the strongest other pitch of the figure, inside the note's slot.
  - Sextuplets, 196-204: median -2.0 dB, and only 12% of notes stand 3 dB clear.
  - Legato triplets of bars 57-58 (188-196), same track, same measure: +7.6 dB, with 75% clear.
  - The same fault is in series 1's c26 (-1.9 dB, 17%). It has never been addressed.
- These violas are as loud as anything in bars 59-60: per beat -35/-36/-36/-35/-35/-33/-30/-28 dB, against Vln I -34..-27 and celli -32..-25. The wash is heard right where the score asks for momentum.
- Fix: in `build/score_config.py`, add `ART_SPANS` "Violas": (195.9, 204.0) on the KS Master's **Detache** row (key 30).
  - Detache is already loaded on this track for bars 48-51 (c28), so `--midi-only` is enough, with no Opus state change.
  - Keep the c35 onsets and lengths. Turn off the tail joins inside each 6-note group, so every note re-attacks while the bow stays one per beat.
  - Detache played about 17 dB louder than Leg Slur MAX at the same CC11 (c28). Start with a CC7 lane over 195.9-204.0 (the same mechanism as the 152.45-167.98 Detache lane from c29). Pre-hall CC7 also keeps the hall continuous (S3).
  - After the render, level-match per beat to the c35 values above (±1 dB) with stem_fix and `--mix-only`.
- Alternative if Detache sounds too separated for a slur: the "Repetitions TS" row (key 39). PDF p.96 describes it as runs whose script plays an up-slur or down-slur sample by direction, with CC11 setting the loudness and velocity ignored. It is a new row, so the Violas track needs a full rebuild.
- Pass criteria:
  - Own-pitch clarity at least +3 dB on 60% or more of the 48 notes.
  - Perceived attack centres within ±40 ms of the sixteenth grid (S2).
  - Bars 59-60 violas level within ±1 dB of c35.
  - The master crescendo 196-204 still rising monotonically per beat (c35: -24/-26/-24/-25/-23/-22/-20/-18; the beat-2 dip at 197 should not get deeper).

### 2. Bar 61 downbeat (qn 204): Horn 1's attack is the loudest thing in the loudest 50 ms of the piece and sets the delivery limiter (measured)

- Where: Horn 1, qn 204.0-204.8 (225.3-226.2 s). Horns 1-2 hold an ff chord here (Hn1 F4, Hn2 D flat 4 in parts.json). The theme belongs to the violins.
- Evidence (50 ms frames):
  - Horn 1 rises from its breath (-42 dB at 204.0) to -18.4 dB at about 204.4, then settles to -27..-31 dB over 205-208. That is a bloom 9 dB over its own body.
  - On the same chord at the same moment, Horn 2 reads -30.6 dB (12 dB under). Horn 2's body is within 1-2 dB of Horn 1's.
  - In the master's loudest frame (-11.7 dB at 225.57-225.62 s), Horn 1 at -18.4 is the loudest stem, ahead of Violins I (-21.5) and Violins II.
  - metrics.md places the delivery's top pre-limiter peak at 225.73 s (+1.03 dBFS). That is qn 204.39, this frame. The delivery limiter works 2.5 dB (the brief's ceiling is about 3), and the master TP is -0.3 dBFS.
  - c30 has the same bloom shape 4.5 dB lower. The rise came from c33 B #1's role `[203.95, 208, 4.5, 0.25]` in `build/roles.json`, which lifts the attack along with the body.
- Fix: keep the +4.5 on the body and keep it off the front.
  - Remove that role row and write the same lift as a `LEVEL_SHAPES` curve on Horn 1 (the mechanism c35 used for the bass clarinet): 203.95: 0, 204.15: -1, 204.6: 0, 205.0: +4.5, 207.75: +4.5, 208.0: 0.
  - This is level only, so a stem fix can check it before the render.
- Targets:
  - Horn 1's 50 ms maximum over 204.0-204.8 no more than 4 dB over Horn 2 there, and no more than 3 dB over its own 205-207 body.
  - Master maximum frame at 225.5-225.8 s at or below -13 dB.
  - Delivery limiter at or below about 1.8 dB.
  - Bar 61's mean level within 0.5 dB of c35 (-14.3), so the climax margin of 2.0 LU stays.

### 3. Bars 61-62 (qn 204-212): the printed "a2" of Horns 3-4 is played by one horn sample raised 3 dB (measured; audible effect inferred)

- Where: Hn 3-4 staff, bar 61 "a2", f tenuto: A flat 4 at 204, B flat 4 at 208, B4/C flat 5 at 210.
- Evidence (measured):
  - parts.json Horn 4 `unison_dropped` 3. The generic unison rule (`find_unisons`, `score_to_parts.py` line 5141) drops Horn 4's copies because both tracks use the same patch file, and raises Horn 3 by 10·log10(2) dB.
  - Horn 4's stem is silent in bar 62 (-180 dB) and in bar 61 holds only its bar-60 tail (-59.8). The c26 render had both horns (-32.2 and -31.3).
- Why it matters (inferred): the level is right, but the timbre is one horn. At the movement's only ff tutti, the horn choir's middle (two unison horns under the Hn 1-2 chord) is thin. Two players in unison sound fuller and blend better, and the kit's own c18 experience showed this for Horns 1-2 at bars 79-82.
- Fix: the "Horns 1-2 a2" track (2FH KS Master, stem 32) plays only 261-272, so it is idle here. Route the Hn 3-4 a2 notes 203.9-212.1 to it.
  - In `build/score_config.py`, add `TRACK_SPLITS["Horns 1-2 a2"] = ("Horn 3", [(203.9, 212.1, 0)], 0)`, or widen its `TRACK_WINDOWS` to read Hn3 in that window. The a2 track currently reads staff Hn1 only, so check which of the two the code supports.
  - Drop Horn 4's notes in the window. Remove Horn 3's +3 dB unison boost there.
  - Copy Horn 3's level rows (roles, the c30 CC1 dynamics refit) for 204-212 onto the a2 track.
  - Check whether the tenutos need a row the a2 track has not loaded. If so, the a2 track needs a full rebuild, with no new instance (memory unchanged).
- Target: the a2 track over 204-212 within ±1 dB of c35's Horn 3 per beat (bar 61 -31.5, bar 62 -30.3 dB). Master bars 61-62 unchanged within 0.3 dB.
- Alternative if routing is too invasive this cycle: put Horn 4 back on its own track with an offset round robin, the way movement I separated same-patch unisons. Check the correlation of the two stems first: series 1 c04 measured 0.999.

### 4. Bars 65-70 and 87-92: the basses' "4 soli" pedal is the full section 3 dB down, at the two places where it is most exposed (inferred; patch checked by c35 A)

- Where:
  - Double basses, 220-238 (4 soli, sul A, change bow at will). Under Horn 1's dolce solo it is the only sustained string sound. In bars 67-70 the three loudest stems are Horn 1 -38.7, Cb -53, and the timpani ppp roll.
  - 286-304 (4 soli again), under the coda's muted chord.
- Evidence: `SOLI_AS_META` plays the full Basses KS Master at -3 dB. That is the level of 4 players but the sound of a whole section: wider, with more room and less bow detail.
  - The manual's H3 pages (82-88) and p.89-90 (DIV A = half section, Close mics only) give the remedy. `Basses Divisi/05 Keyswitch/Basses KS Master DIV A.oib` is installed (c35 A, MANUAL-GAPS #8).
  - The celli 4 soli moved to DIV A in c33 and came out 2.2 dB louder than the full section at -6 dB, with a narrower image (c33, Movement I c40 measured L/R correlation 0.85 against 0.74).
- Fix: a "Double basses soli" track on that patch for 220-238 and 286-304 (`TRACK_WINDOWS`, `META_SKIP_TRACKS`), level-matched by stem fix to c35's Cb bar levels.
  - Memory: about 0.7 GiB against 44 GB settled. If the 45 GB cap is too close, render it in a second REAPER project and sum the stems in float (Movement I c39 showed this equals one render).
  - Refit the basses' re-bow fills in these windows with `fit_rebows.py --window`, re-levelled to the old piece means as in c34.
- This is timbre only: critic B measured the level as already on target. Rank it after 1-3.

## Not ranked

- The Violins I first-note dip at qn 72 (bar 25, "tutti, con sord.") is 12-15 dB in the stem, but Violins II in unison masks it (master within 1 dB). No action.
- Trombone 1's quotation (212.5-220) holds -23..-27 dB to 218 and then falls 22 dB to 219.5 for the printed > p. The strings are at p from 216. That reads correctly.
- The opening Violins I C5 (bars 1-2) shows two 5-6 dB stem dips at about 1.2 s and 2.0 s that c26 did not have (the REBOW_AT pieces). The master moves only 1 dB. Watch it; no action.

Do not touch: the climax order and the c34/c35 bar 61-63 string holds and sf shapes (climax 2.0 LU over the cadence, delivered); AUTO_REBOW, every fitted re-bow and the c35 bass clarinet pedal shape (no loop period anywhere); the Violins II portato notches; the c35 REATTACK_LEAD_AT values; Trombone 1's quotation shapes, CC7 lanes and accents; the coda clarinet and cor anglais balance; GENTLE_ACCENT; the delivery chain (LRA 15.2, span 18.3).
