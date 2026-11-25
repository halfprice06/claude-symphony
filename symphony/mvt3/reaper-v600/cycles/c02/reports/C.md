# Critic C, cycle 2 (dynamics over time), on the c01 render

Lens: the loudness arc against the score, hairpins and phrase shapes, the climaxes, the sfp of bar 149, the delivered mp3's range, loop pulsing on long notes, decays and the final chord. The c01 stems, master and mp3 were measured against `build/parts.json` (tempo map, CC and volume lanes), `mockup-events.tsv` and score pages 1, 8 and 16. Levels are stereo RMS on score-timed frames, plus EBU short-term loudness (ffmpeg ebur128, 10 Hz, centred). I simulated delivery by running `tools/deliver_master.py` unchanged on edited copies of the master in scratch.

## Manual notes (MANUAL-READING row c2 C: May 2021 HO manual p.53-54, 64, 101-102; Movement I's c36 C table read first; MANUAL-GAPS.md)

| Manual (PDF page) | What it says | Where in this mockup | Does the render follow it? |
|---|---|---|---|
| p.53-54 | Shape held lines with CCs, which change during a note. Velocity is one value at the note start and suits short notes. | Every hairpin (CC11 on strings and winds, CC1 on brass and clarinets); sf and fp attacks. | Mostly. Held-note hairpins move the right way in about 89% of cases (finding 5). But the sfp at bar 149 tries to make its sf with a CC11/CC1 spike only 0.23 qn (80 ms) long, on a note whose velocity is the p value (53). By p.53 the attack belongs to velocity, and the spike is too short to cross the layers. Result: no sf (finding 3). Measured. |
| p.64 | CCs crossfade dynamic and vibrato layers. CC7 sets a track's level against the others; CC11 shapes the line. | Balance lives in the REAPER volume envelope; CC keeps each printed dynamic's layer. | Yes in principle. But at the final fff downbeat (bar 278) the envelope's divisi and tremolo cuts take 6-12 dB off the strings, so the arrival falls in level (finding 1). The envelope sits after the hall (Movement I c36). Measured. |
| p.101 | Brass Sustain: CC1 crossfades 4 recorded layers, so a held note can crescendo or decrescendo. | Brass hairpins; the held brass chords at 223, 263 and 278. | Brass held crescendos median +4.0 dB (n 97, 11% the wrong way); decrescendos -6.0 dB (n 64, 5% wrong way). On the held fff of bar 278 with CC1 constant, Horn 1 sags 5.1 dB, Bass trombone 4.4 and Trumpet 2 3.5 (finding 1). Measured. |
| p.101 | Sustains loop, so notes can be held indefinitely. | BRIEF item 7. | No pulsing. Fold at 3.95 s (100-300 Hz level / spectral centroid autocorrelation): Horn 4 at qn 168 (6.3 s) -0.62 / +0.12; timpani rolls at 920, 970, 1088: +0.19 or lower; Violins I/Vc/Cb over the chorale (892-936): under +0.10; master 888-936 -0.15 / -0.16; master 1088-1112 -0.10 / -0.14. Measured. |
| p.101 | Sustain Accent: velocity sets the attack. Sustain Marcato: velocity opens a low-pass on the attack. | Brass accents. | Not used, by design (GENTLE_ACCENT, MANUAL-GAPS #1). Not re-measured here. |
| p.102 | Shorts have no release trails, so the last note must be held for the room to ring. Brass staccato at top velocity overblows. | Cut-offs; c01's new brass short rows. | Cut-offs ring as the hall allows (do-not-touch line). c01's brass short rows take `vel_by_cc` at most 100 (score_config c01 block), so there is no overblow layer. Read. |
| MANUAL-GAPS #12 (p.123, 125) | Recorded crescendo rolls. | Timpani crescendo hairpins. | Timpani crescendos median +2.8 dB (n 8). The one that falls is the roll under the sfp < ff at 592-596 (-1.2 dB; finding 3). Not a reason to load the Cresc rows yet. Measured. |

## State through this lens (measured)

- Master: -15.8 LUFS, p10 short-term -38.5, max -7.4 (bar 223).
- Delivered mp3: LRA 17.0 LU, p10 -32.9, max -11.6, span 21.4 dB, limiter 1.8 dB, 1 inversion of 214 five-second moves of 3 dB or more, median 84% of each move kept.
- Highest short-term peaks, master: 223.3 -7.4; 263.0 -8.4; 277.9 -8.6; 148.0 -9.5; 259.3 -11.1; 111.0 -11.8; 93.4 -11.8; 272.9 -12.0.
- Highest short-term peaks, mp3: 223.3 -11.6; 278.3 -12.9; 263.0 -13.7; 148.0 -14.0; 111.0 -15.4; 93.4 -15.5.
- The big builds rise as printed:
  - closing 89-91: -23.2 -> -15.6 -> -12.5;
  - development 125-132: -35.4 -> -19.5;
  - 135-147: -35.0 -> -10.5;
  - accelerando 205-211: -20.7 -> -14.6;
  - 219-223: -27.1 -> -7.9, a +3.7 dB step on the downbeat;
  - stringendo 243-247: -21.3 -> -15.2;
  - 257-263: -14.9 -> -9.0.

## Findings

### 1. The final fff (bar 278, qn 1108) is not an arrival: the strings' envelope drops 6-12 dB on the downbeat, and the held brass sag (measured)

**Where:** qn 1104-1113 (bars 277-279). Violins I/II, Violas, Violoncellos; Horn 1, Bass trombone, Trumpet 2. Score: crescendo across 275-277 into a tutti fff whole-note chord with accents (strings div. a 3 tremolo, crash and bass drum), tied to a quarter in 279, then rests under the fermata.

**What is wrong:** after a printed two-bar crescendo the last chord should be the top of the piece with 223. In the render it is level with the accented ff chords of bar 277 before it.

**Evidence:**
- Master, first quarter of 278: -10.7 dB, against -10.9 on 277's accented chords (qn 1104-1104.8). That is +0.2 dB. Over its length the chord falls to -12.0.
- For comparison: 223's head is -9.5, and 263 reads -11.8. Bar levels from metrics: 277 -12.5, 278 -11.4.
- `vol_db` in parts.json steps at qn 1107.9 from about +2.9 dB to:
  - Violins I -7.8 (-10.7 dB);
  - Violins II -8.8 (-11.7);
  - Violas -4.8 (-7.7);
  - Violoncellos -3.0 (-5.9).
  These are the divisi cut of the three-note div. a 3 chords plus `ROW_GAIN_DB` Tremolo -3/-4. At 223 the same tracks move by 0-1 dB.
- Stems, 278 head against the 277 accents: Violins I -27.6 vs -23.2; Violas -32.7 vs -23.2; Violins II -21.4 vs -19.7.
- Held fff, last quarter minus first quarter of 278: Horn 1 -5.1 dB, Bass trombone -4.4, Trumpet 2 -3.5, Violins II -2.7. CC1 is flat there.
- Bar 263 has the same shape on a smaller scale. Master 1047.0 -10.8, then 1048.0 -12.3 / 1048.5 -11.3 at the fff with the crash. Trumpet 1 is 3 dB lower at its fff than at the top of its crescendo (-20.1 -> -23.0).

**Fix:**
- (a) `build/roles.json`: on the final chord, role rows from qn 1107.9 to 1113.5 (start at the downbeat, release with the chord): Violins I +5 dB, Violins II +5, Violas +4, Violoncellos +3. A role at the attack does not cut a ringing forte tail, because 277's chords end at 1106.9. Alternatively, exclude onsets at fff from the divisi cut in `score_to_parts.py`. Do not raise the sum further: the cut exists for loudness, and +4..+5 restores about the 277 level of each section.
- (b) `build/score_config.py`: `ARRIVAL_WEIGHT_AT = {1108.0: (-1.0, 2.0, 0.5), 1048.0: (-1.0, 1.5, 0.5)}`. This is Movement I c06/c08's tool with the short 0.5 qn hold-back, so the crescendo bar keeps its gain.
- (c) `LEVEL_SHAPES` for the brass sag: Horn 1 `[(1108.5, 0), (1112.5, 4.0), (1113.0, 4.0), (1113.2, 0)]`; Bass trombone the same with 3.5; Trumpet 2 with 3.0. Refit after the render as (linear target - measured) on 0.2 s frames (Movement I c38).

**Targets:**
- master 278 first quarter at least +2 dB over 277's accents, and within 1 dB of 223's head;
- 263's downbeat at least +1 dB over 1047;
- delivery limiter unchanged. 278 is not among the five highest pre-limiter peaks, all of which are at least 2.7 dB under the 223 peak that sets the limiter, so +2 dB at 278 should not move it (inferred).

### 2. The delivered mp3 is over the range targets because the soft passages sit at the ride's +10 dB cap (measured; simulated)

**Where:** the p/pp passages:
- bars 43-66 (transition and second theme, qn 168-264);
- 95-98;
- 114-126 (bassoon solo, harp);
- 134-135;
- 170-186 (recapitulated second theme, muted trumpet).

**What is wrong:** delivered LRA 17.0 LU against 14-16, and span 21.4 dB against 16-19 (c00: 15.7 LU, 21.5 dB). c01's accompaniment cuts and cello trims lowered exactly these passages. The ride lifts nothing below -31.3 LUFS short-term (knee -16.3 minus 10/(1-1/3)) by more than its 10 dB cap. The passages sit at -38 to -41 in the master, so every bar of D (51-60) and L (171-180) is in the mp3's bottom decile (-33 to -34). A listener at one volume hears the trumpet's dolce solo and its muted return 20 dB under the tuttis.

**Evidence:** a stem-free simulation added +X dB to the master over the spans above (ramped over 0.8 s) and ran `tools/deliver_master.py` unchanged:

| added dB | LRA | span | limiter | mp3 bar levels (55 / 118 / 175) | climax order |
|---|---|---|---|---|---|
| 0 | 17.0 LU | 21.4 dB | 1.8 dB | -33.4 / -34.4 / -32.9 | |
| +2 | 15.1 LU | 19.4 dB | 2.0 dB | | |
| +3 | 14.2 LU | 18.5 dB | 2.2 dB | -30.0 / -31.2 / -29.6 | 223 -11.7, 278 -13.0, 263 -13.8 (unchanged) |

Inversions stay at 1 and the median share of each move kept goes 84% -> 79%. The transition (43-50, p to pp) should stay below the second theme. Now it is 4 dB above it (bars 43-48 -35 to -36 against 51-60 at -39.5), so the lift belongs mostly on the theme.

**Fix (in the mix, BRIEF item 6):**
- `build/roles.json` rows on every track except Timpani, Crash cymbals and Bass drum: +3 dB at qn 200-264 and 680-744; +2.5 dB at 452-504; +1.5 dB at 168-200 and 376-392. Ramps of 1 qn at each end, ending before the next louder entry: 264 (bar 67, mf), 744 (bar 187, mf), 504 (bar 127, mf), 392 (bar 99, f).
- These are envelope rows on soft passages that do not end under a sounding forte, so S3 is not involved.
- Fallback that leaves the master alone: the same values as `RIDE_TRIMS` rows in `build/score_config.py` (read by `deliver_master.py`).
- Targets: delivered LRA 14.5-15.5 LU, span 18-19.5 dB, limiter at most 3 dB, the D and L bars no longer the file's p10, 223 and 278 still the two loudest moments.

### 3. The sfp at bar 149 has no sf: the attack comes in 2-3 dB under the ff before it (measured)

**Where:** qn 592-596 (bars 149-150, poco rit.). Every brass, timpani and string staff, and the winds: "sfp <" to ff at 596, over the tied whole note.

**What is wrong:** an sfp is a forced attack falling at once to p. Here the "sf" is quieter than the ff bar before it. Only the dip and the crescendo are heard, so the bar sounds like a soft re-entry rather than an accent that collapses.

**Evidence:**
- Master on 1/16-qn frames: -12.5 dB over qn 591-591.5, the gap before the re-attack at -16.5, the sf at -14.2..-15.1, then a fall to -20 by 592.75 and -23.0 at 593.75, rising to -11 by 596.
- Stems, from 591.0-591.4 to the sf: Violins I -22.9..-20.7 -> -25.3; Trombone 2 -19.5 -> -22.3.
- parts.json: the notes at 592 carry velocity 53 (DYN["sfp"] = 46 drives velocity). CC11/CC1 jump to 114-120 at 592.02 and are back at 42-50 by 592.25. That is `FP_SPIKE` ("f", 0.12, 0.25 qn): held 43 ms, gone by 90 ms at this tempo, fitted for Movement I's slower fp.
- The fall is pre-hall (CC). The volume envelope only ramps, so the hall of the ff rings through. S3 is met.
- Timpani and double basses fall across the following crescendo (-1.2 / -2.4 dB from first to last third, 592-596).

**Fix:**
- `tools/score_to_parts.py`: make the sfp spike time-based. Add a new `SFP_SPIKE_S = (0.12, 0.30)`: hold the sf level for 0.12 s, then fall to DYN["sfp"] by 0.30 s, with the qn computed from the tempo map at the mark. Give the sfp note the velocity of the sf level (max(DYN["sf"], level)) instead of DYN["sfp"].
- Keep the fall on CC only, never the envelope (S3).
- Check the timpani roll's `TIMP_ROLL_TRIM_DB` reading of the sfp. Its envelope goes +18.6 -> +11.3 -> +18.6 dB within 0.25 qn at 592 (trim for p).
- The roll and basses should then follow the < to ff. If they do not, add `LEVEL_SHAPES` ramps 0 -> +3 dB over 592.5-596 on Timpani and Double basses.
- Targets: the sf at least as loud as qn 591 (within -1..+2 dB, 2-5 kHz attack not more than 4 dB over the following body); p at least 10 dB under it by +0.3 s; every staff rising at least 6 dB to 596.

### 4. The retransition's stop chord (147-150) is the third-loudest moment, ahead of the final Largamente; one hot trombone note drives it (measured)

**Where:** qn 584-599 (bars 147-150), Trombone 2 D4 (pitch 62) at qn 584, 588 and 592. Compare the final Largamente, bars 273-276.

**What is wrong:**
- The ff dominant chord before the recapitulation reads louder than the ff tutti of the last Largamente (27 staves). It is the 4th-highest short-term peak of master and mp3 (-9.5 / -14.0) and holds the 3rd and 5th pre-limiter peaks.
- Bar means, master: 147-150 -10.5..-10.7 against 273-276 -11.0..-12.6 and 91-93 / 110-112 at -12.
- Bar means, mp3: -15.0..-15.2 against -15.8..-17.4. The ending's ff should be a step above the retransition.

**Evidence:** in all four bars Trombone 2 is the loudest stem by 4.5-5 dB (metrics: bar 147 -18.9, the next stem -23.4). On the same CC, velocity and envelope as Trombone 1, its D4 measures 5.2 dB over Trombone 1's F4 (all its long D4s; every other Trombone 2 pitch is within -2..+2.5 dB of Trombone 1, except D3 at -6.6). Taking 4 dB off the Trombone 2 stem lowers the master by 0.7 dB over 584-592 and 0.5 dB over 596-599.

**Fix:**
- `build/pitch_trims.json`: `{"Trombone 2": {"62": -4.5}}`. Use the table's own key format; check pitch 62 elsewhere on Trombone 2 first.
- If the c02 mp3 still has 147-150 within 1 LU of 273-276, add a +1 dB role on every track except percussion over qn 1088-1104 (ff Largamente; it sits under the 223 peak, so no limiter change, inferred).
- Target: 273-276 at least 1 LU over 147-150 in the mp3.

### 5. Held notes that bloom against their printed hairpin (measured)

**Where and evidence:** hairpins of 1 qn or longer where the track sounds throughout. Median change, last third minus first third:

| family | crescendos | decrescendos |
|---|---|---|
| winds | +4.6 dB (13% wrong way) | -5.1 dB (11% wrong way) |
| strings | +5.1 dB (9%) | -4.2 dB (10%) |
| brass | +4.0 dB (11%) | -6.0 dB (5%) |

The largest errors a listener hears are exposed solos:
- Oboe 1 "solo, espress." mf > p at qn 376-384: rises +6.0 dB. The stem goes -50.9 at 376 -> -42.3 at 382 while CC11 falls 74 -> 56.
- Under it, Violins II "sul tasto, last 2 desks" mp > p on one tied G4, 376-391: rises +7.4 dB. It enters at -63.6 and blooms to -51.5 by 381, while the envelope falls 4 -> 9 dB.
- Clarinet 1 cresc p < at 540-548: falls -8.2 dB. A note-to-note step: the 544 A4 comes in 8 dB under the 540 B flat 4 on rising CC, so this is a per-pitch level, not a shape.

Smaller ones: Horn 3 at 880-884 (-4.2) and Horn 1 at 1040-1048 (-2.7) inside crescendos. The master rises there anyway, because the other parts carry it.

**Fix:**
- `build/cresc_fronts.json` / `LEVEL_SHAPES` counter-shapes fitted on this render (Movement I c34/c36/c38: (linear target in dB - measured) on 0.2 s frames, clipped -7..+1): Oboe 1 376-384, target -46 -> -52 dB; Violins II 376-391, target a flat -54 then -58. The Violins II entry is 12 dB under its body: also add an `early_fills.json` +6 dB over its first 1.5 qn, or start it on a faster-attack row.
- `build/note_trims.json`: Clarinet 1 qn 544 and 548 +6 dB, or a `pitch_trims` entry for its A4 and A flat 4 once checked elsewhere.
- Targets: each listed hairpin moving at least 3 dB the printed way.

### 6. Decays: the hall change worked; do not dry the tail further, and judge "mushy" elsewhere (measured)

**Where:** tutti cut-offs and the final chord: bars 2 (qn 5.2), 6, 94 (373.9), 113 (450.0), 204, and the final release at qn 1113.

**Evidence:**
- Master drop 0.3 s after the cut-off: 18.7, 19.0, 15.9, 20.4, 17.6 and 18.3 dB. Target at least 13; recordings 13-17. So the early tail is now at or below the dry end of real halls.
- Final chord, stem sum without crash and bass drum: -18 dB at 0.3 s, -25 at 0.5, -40 at 1.0, -49 at 1.5. That is a T60 of about 2.0 s over the audible -20..-40 dB range, inside the 1.5-2 s aim. The 3.3 s IR's long low tail (T60 about 3.2 s) only shows below -40 dB.
- The delivered file keeps 1.0 s after the last window above -65 dBFS, so the fermata's ring is cut only at about -50 dB.

**Fix:** none on the hall in c02. A shorter IR (Opus p.133-134) would take ring from the final chord, which is already at the dry edge. If Dan still hears mush, my reading is that it comes from attack smear and 200-500 Hz build-up (blend and articulation lenses), not from decay length (inferred).

**Do not touch:**
- The hall: fx_volume 0.095 with the 160 Hz low cut, and the cut-off drops above.
- No loop pulsing on any held note or passage (all folds under +0.20).
- The 223 arrival: +3.7 dB step, loudest moment, sets the limiter.
- The build shapes listed under State.
- Hairpin medians and the c33/c34 held-decrescendo rules.
- S3: no post-hall envelope fall of 6 dB or more on any sounding track except the timpani stroke notches. The fp at 832 and the sub. p at 872 fall on CC.
- The delivery chain's settings (1 inversion, 84% of moves kept): fix the range in the mix, not by raising the ride cap.
