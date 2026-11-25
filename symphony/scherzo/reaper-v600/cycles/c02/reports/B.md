# Cycle 02, critic B (balance and levels), on the c01 render

Measured on `cycles/c01/render/` (stems after c01's stem fix) and `cycles/c00/render/` for comparison. Unless marked otherwise, levels are dBFS RMS through an approximate K-weighting: a high-pass near 40-80 Hz and a +4 dB shelf above 1.5 kHz, applied to the spectrum of each window. Windows sit on the parts.json tempo map. "Two bars" means a 6 qn window. The scratch scripts were per-window levels, per-pitch residuals, loop autocorrelation at 3.95 s, repeat dips, and accent band ratios.

## Manual notes (cycle 2, slot B: group B2, PDF pages 194-200; MANUAL-GAPS.md read)

| page | what it says | where it applies here | render follows? |
|---|---|---|---|
| 194, 196 | Each instrument has a Mix-page strip with Sub Mixer channels, one per mic position, each with its own load button and volume | `mix.json` group `mics` (wind Close 0.5 / Main 0.8, horn and trumpet Close 0.5 / Main 1.0, harp Close 0.6 / Main 1.0, timpani Close 0.2 / Main 0.5; strings `null` = the patch's own mics), written by `build_reaper.apply_mix` | Yes. Unloaded mics are unloaded in the layer matrix too, so they cost no memory. |
| 195 | "Store Mix" / "Restore Mix" save and recall every channel's settings | the mix | Not used, and not needed: every build writes the mix again from `mix.json`, so the project can be rebuilt (BRIEF rule). |
| 196 | An FX Bus channel holds the reverb insert; Sub Mixer channels feed it through Reverb Send inserts | the shared hall on `fx:0` in every instance (one IR, `fx_volume` 0.095, low cut 160 Hz, high cut 5.5 kHz) | Yes |
| 198 | The send has a level slider and a Post switch: "for reverb, post fader is typically used", so the hall gets the same proportion as the dry mix | `reverb.send_pre_fader` true: the send is taken pre-fader and its level is multiplied by the channel volume (build_reaper c09) | Yes in effect. With fixed mic volumes the hall input equals a post-fader send. Pre-fader also keeps the seat panning out of the hall. All balance moves are made in REAPER after Opus, so they scale dry and hall together. |
| 199-200 | Opus EQ inserts: Bass Comp (32-256 Hz boost), Channel Equalizer (3-band), Equalizer (6-band with HP/LP/shelf/peak) | the pipeline's EQ is REAPER EQ after Opus (`eq`, `side_shelf`, `loud_eq` in `mix.json`), so it acts on each instance's dry and hall output together | Partly. An Opus insert on the Sub Mixer channels would act before the hall. This matters only for low-end boosts such as the celli 125/170 Hz bells and the basses' 180 Hz bell, which also lift their hall return. Measured: no 200-500 Hz build-up. The 250-500 Hz band share is -6.73 dB against Dvořák 9/i -6.31, 500 Hz is +2.9 against the reference's +4.2, and 250 Hz is +3.8 against +4.4. So BRIEF S4's 200-500 Hz cut is not needed for balance. |

MANUAL-GAPS: #6 (hard sticks) and #7 (Crs rolls) do not cause the timpani problem in finding 3. That one is an envelope sum. #9 (half-section basses) is not a balance problem on this render.

## Standing checks (Dan's ears), measured on c01

- **Loop pulsing (item 8).** I folded the level, the 100-300 Hz band and the spectral centroid at 3.95 s on Violins I 1089-1128, Horn 1 1089-1128, the Horn 3 and Horn 4 trio drone 456-504, and the master 1089-1128. Every autocorrelation lies between -0.22 and +0.16. No pulsing (measured).
- **S3, the sub. p's.** The master in 50 ms frames across qn 360 and 828 falls smoothly (360: -30, -33, -34, -33, -35, -38, -36 ... dB), with no step to silence (measured).
- **Accents (item 9).** The 2-5 kHz energy in the first 80 ms against the body: Flute 1 median -4.5 dB, cor anglais -6.6, Oboe 1 -7.7, Violins I -3.2, Violins II -2.0. None is harsh. The accent level over the 0.3 s before it is -2.0 / +0.7 / -4.5 / -1.9 / -2.1 dB, so the accents carry no weight. That is critic A's open c01 item, so it is not ranked here (measured).
- **S1.** The theme head's B-B pairs separate by 7.5-7.8 dB on the Violins I stem and 2.7-3.4 dB on the master. In the counterstatement, Flute 1 and Oboe 1 separate by 6 dB on their stems but only 1.0-1.2 dB on the master at qn 85 and 97. Finding 5 explains why.

## Findings, ranked by what a listener would hear

### 1. The harp's pp off-beat chords sit level with or above every tune they accompany (bars 81-88, 153-168, 185-192, 225-236, 345-348)

- **Where.** These are the Harp's "non arpegg." pp chords, under:
  - Clarinet 1 p dolce at bar 81 (qn 240) and in the trio tune (153-168, qn 456-504);
  - Oboe 1 p "1. espress." (185-188, qn 552-564);
  - the codetta's Oboe 1, Clarinet 1 and Bassoon 1, p dolce (225-236, qn 672-708);
  - the coda's woodwinds, p dolce (345-348, qn 1032-1044).
- **Evidence (measured).**
  - **Bars 81-84:** Harp -35.8 / -39.6 against Clarinet 1 -42.0 / -43.4, so the harp is 4-6 dB over the tune.
  - **Trio (two-bar windows from 456):** Harp -40.8, -39.3, -39.5, -41.3 against Clarinet 1 -43.7, -40.5, -40.6, -41.7. The harp is 0.4-2.9 dB over the tune whenever it plays. The clarinet only comes through in bars 161-164 (-37.7), where the harp rests.
  - **Bars 185-188:** Harp -41.6 / -42.7 against Oboe 1 -45.1 / -46.1 (+3.4..+3.5 dB). Unweighted, the harp is 9 dB over the oboe across 552-576.
  - **Codetta:** Harp -40.3..-41.5 against Clarinet 1 -45.1 / -46.0 (bars 229-232) and Bassoon 1 -43.0 / -43.6 (233-236).
  - **Bars 345-348:** Harp -38.7 / -38.8 against Bassoon 1 -40.4, Oboe 1 -39.6..-43.1 and Clarinet 1 -42.1..-46.6.
  - **Cause (read).** The Harp entry in `mix.json` has no `soft_trim_db`, so it takes the global table (`soft_trim_db` pp +7, p +5; only Timpani and Harp harmonics are in `_except`). At pp the harp therefore plays at gain -4 + 7 = +3 dB, at velocities 40-52.
  - In c00 the horn drone hid this. With c01's horn trims the harp is now the loudest stem in every trio bar it plays (metrics "loudest three": bars 153-160, 165-168, 185-188, 225-236, 345-348).
- **Judgement.** In a pp accompaniment the harp should sit 3-6 dB under the p tune. As rendered, a listener hears harp chords with a clarinet or oboe beside them (inferred).
- **Fix.**
  - In `build/mix.json`, add to `tracks.Harp`: `"soft_trim_db": {"ppp": 2, "pp": 2, "p": 5}`. That is -5 dB at pp only.
  - The harp's p espress. melody at bars 73-80 (qn 216-240) keeps its +5.
  - Expected result: harp about -45..-47 in these passages, with the tunes 3-6 dB over it.
  - Afterwards, check that the trio role `Clarinet 1 [456, 504, +2]` is still wanted. Keep it if the clarinet is 3-5 dB over the harp.

### 2. The summit's top note: Violins I's fff B6 (bar 336, qn 1005) lands 4-7 dB under Violins II and Flute 1; single woodwinds still lead at 1008-1014

- **Evidence (measured).**
  - Per quarter note at 1004 / 1005 / 1006, Violins I reads -19.0 / **-26.4** / -24.5. Over the same quarters Violins II reads -20.6 / -22.0 / -20.9 and Flute 1 reads -31.5 / -19.3 / -19.2.
  - The fff downbeat of the melody (B6, Sus MAX v96, CC11 124, vol +3) is 7.4 dB under the staccato eighth before it. It is 4.4 dB under the B5 of Violins II and 7 dB under the flute doubling it.
  - At 1008-1013, Violins I reads -21.9 to -25.4, against Violins II -18.3 to -22.9.
  - The cor anglais is the loudest wind at 1008 / 1009 (-19.3 / -20.2, accented A4), 2.6-5 dB over Violins I.
  - Bassoon 1 (F sharp 3) holds -23.6..-26.8 from 1005 to 1013, level with or over Violins I.
  - The c01 roles (Cor anglais -3, Bassoon 1 -3) and the stem fix (Violins II -2, celli -6) did not reach the melody.
  - Likely cause of the B6 deficit (inferred): a slow Sus MAX attack on the top-range 1st Violins sample at quarter 288. The note keeps its deficit through its second quarter, so the cause is level as well as attack.
- **Fix.** Add to `build/roles.json`:
  - `"Violins I"`: `[1004.75, 1008, 4]` and `[1008, 1014, 2]`.
  - `"Cor anglais"`: `[1008, 1010, -4]`, on top of its existing -3.
  - `"Bassoon 1"`: `[1005, 1017, -3]`.
  - Expected sum change is about +0.3 dB at 1005 (inferred: Violins I is 12 dB under the master there), so the delivery limiter stays near c01's 3.1 dB.
  - Target: Violins I within 1-2 dB of Violins II at 1005-1014, and no single woodwind over Violins I.

### 3. The final tutti stroke (bar 339, qn 1014): the timpani is 8 dB over the orchestra and fills the G.P. with its own ring

- **Evidence (measured).**
  - Per half quarter at 1014 / 1014.5 / 1015, the timpani reads -16.0 / -19.3 / -24.0. Over the same windows Violins I reads -24.3 / -24.1 / -26.5 and the basses -26.9 / -29.7 / -34.3.
  - In the G.P. the timpani is the hall. At 1016.5 / 1017 / 1018 it reads -33.5 / -36.7 / -45.3, against Violins I -44.3 / -53.2 / -71.5 and Violins II -42.1 / -50.9 / -69.0. That is 9-24 dB over every other stem.
  - Metrics: bar 339's loudest stem is the timpani at -20.7, 6 dB over the violins.
- **Cause (read in parts.json).**
  - The E2+E3 accented double stop at 1014 plays v125 on "Timpani Flt Lng". The volume envelope rises to **+12.0 dB** at 1014.048, where the single accented strokes at 1008, 1010 and 1012 get +6.0.
  - The per-note accent envelopes of the two chord notes add, the same summing that c01's LEARNINGS records for pitch trims.
  - The printed mark is staccato + accent, but the track has no damped stroke: all 174 strokes play the Lng row. The patch's "LH/RH Sht" regions (DIGEST §9.1, patch check; manual p.124) are unused.
- **Fix.**
  - Generic: in `tools/score_to_parts.py`, apply the accent envelope (the `ACCENT_DB` / timpani accent `vol_parts` entry) once per onset, not once per chord note, as the pizz. note trims already do ("once per onset (a chord counts once)").
  - Quick alternative: `build/roles.json` `"Timpani": [[1013.9, 1015.5, -6]]` (keep the existing `[300.0, 300.5, -12]`).
  - Articulation (critic A's call): play printed timpani staccatos (qn 12, 165, 393, 549, 597, 722, 861, 968, 984, 1014) on the Sht row so they are damped. The hall ringing into the G.P. should then be the orchestra's.
  - Target: the timpani no more than 2-3 dB over the violins at 1014, and under them by 1016.

### 4. Horns at pp/p doubling or countering a string line sit level with it or above it; Hn 1's final G sharp sits under the Violins I ppp

- **Bars 169-176 (qn 501-528).** Horn 3 p dolce doubles the celli's trio tune (mp, arco, espress.) in unison. Two-bar windows (measured):
  - Horn 3: -43.5, -38.6, -40.0, -39.3, -41.7
  - Violoncellos: -40.7, -40.3, -39.2, -41.4, -39.0
  - The horn is over the celli in three of five windows, by up to +2.1 dB, so the tune sounds like a horn tune. It should be a cello tune coloured by the horn.
- **Bars 261-268 (qn 780-804).** Horn 3 plays a pp dolce countermelody, measured -39.1 / -36.5 / -39.3 / -41.4. Violins I's p leggiero theme measures -39.6 / -36.2 / -42.7 / -43.8. The pp countermelody is 0-3 dB over the p theme.
- **Bars 281-284 (qn 840-852).** Horn 2 p doubles the celli's espress. line, measured -36.4 against the celli at -40.6: 4.2 dB over (metrics: Horn 2 is the loudest stem in bars 281-282).
- **Cause (read).** The horn soft trims come from Movement I: pp +13 to +14 dB, p +9.7 to +12. c01 lowered only Horn 4's.
- **Bars 373-376 (qn 1116-1128).** Hn 1's last G sharp (pp to ppp, the pivot to the finale) measures -47.7 / -50.1 / -49.8 / -50.0 / -50.8. Violins I's ppp G sharp 5 measures -47.0 / -46.4 / -46.0 / -47.1 / -47.6, and rises slightly into the re-bow fill capped at +3 after 1120. The horn is 3-4 dB under the violins at the close (measured).
- **Fix.** Add to `build/roles.json`:
  - `"Horn 3"`: add `[501, 528, -4]` and `[780, 804, -4]`.
  - `"Horn 2"`: add `[828, 852, -5]`.
  - `"Horn 1"`: `[1113, 1128, 3]`.
  - `"Violins I"`: `[1116, 1128, -1.5]` (inferred safe: the re-bow fills are kept; this is a flat offset over them).
  - Target: the doubling horn 2-4 dB under the string line, and Hn 1 level with or 1-2 dB over Violins I in bars 373-376.
  - Generic alternative: Horns 1-3 `soft_trim_db` pp 13-14 -> 10, as Horn 4's 9.5. This would also lower Hn 1's solos at bars 1-6 and 141-148. Those are currently the loudest stems by 5-10 dB, so they can afford it, but the roles are the safer first step.

### 5. Counterstatement (bars 29-34, qn 84-102): the pp wind chord covers the p leggiero theme and hides its repeated eighths

- **Evidence (measured).**
  - The theme is Flute 1 + Oboe 1, p leggiero. Clarinet 1, Clarinet 2, Bassoon 1 and Bassoon 2 hold a pp chord (Sus Non Vib, CC1 28, CC11 34, v41, no envelope offset).
  - Bar 29: Flute 1 -46.9, Oboe 1 -48.3; the chord parts -47.4..-48.9 each, four of them.
  - Bars 33-34: Clarinet 1's held A4 reads -39.4 / -40.0, 7-9 dB over Flute 1 and Oboe 1 (-46.2..-48.3). The same clarinet with the same controls on G4 at bar 29 reads -47.9.
  - Across all Clarinet 1/2 notes of 1.5 qn or longer, the per-pitch residual (fit on CC1, CC11 and vol_db) gives A4 (69) a median of +3.0 dB over 19 notes, with this note at +9.
  - On the master, the theme's B-B pair separates by only 1.0 / 1.2 dB at qn 85 / 97. The Flute 1 and Oboe 1 stems separate by 6 dB, so the chord masks the S1 repeat.
- **Fix.** Add to `build/roles.json`:
  - `"Clarinet 1"`: `[84, 96, -4]`, `[96, 102, -9]`, `[102, 108, -4]`.
  - `"Clarinet 2"`, `"Bassoon 1"`, `"Bassoon 2"`: `[84, 108, -4]`.
  - Leave 108-120 alone (p cresc. to f).
  - Generic option, if other A4s confirm the residual: `build/pitch_trims.json` `"Clarinet 1": {"69": -3, "_all_arts": true}`.
  - Target: the theme 3-5 dB over the chord, and master pair separation of 3 dB or more at 85 and 97.

### 6. Celli pizz. under theme A (bars 13-28, also 3-12) is uneven by pitch and as loud as the theme's peaks

- **Evidence (measured).** The celli and basses play pizz. p on every downbeat, all at v53, under Violins I's p leggiero theme.
  - Celli pizz. peaks in the first 0.25 s, bars 13-28:
    - E2: -35.6..-37.7
    - A2: -32.4..-35.7
    - G sharp 2: -30.9
    - B2: -27.2..-32.3
    - G2: -28.6
  - Violins I's downbeat notes peak at -27.5..-34.1. In the bars with a B2 or G2 bass (16, 19, 24, 26, 27) the celli bar level is over Violins I by 1-7 dB (bar 26: -39.8 against -47.2).
  - The basses' pizz. (pitch-trimmed in c01) peaks at -35.8..-42.5, 3-9 dB under the celli an octave above at the same printed p.
  - The per-pitch residual over all 50 single celli pizz. notes (first 120 ms, velocity removed): E2 -1.8 (12 notes), A2 -0.6, B2 +1.4 (23, spread 4.4), G2 +8.4, F sharp 2 +8.1, D sharp 2 +7.9, G sharp 2 +5.7.
- **Fix.**
  - Add to `build/pitch_trims.json`: `"Violoncellos": {"_arts": ["Pizzicato RRx4"], "43": -6, "42": -6, "39": -6, "44": -4, "47": -3}`.
  - Add to `build/roles.json`: `"Violoncellos": [[36, 84, -2]]`. The theme is p; the celli should be the base of the texture, not its peak.
  - Re-measure B2, which has only a moderate residual but a wide spread.
  - The reprise's pizz. (253-272) takes the pitch trims automatically.

## Do not touch

- The trumpets in 105-120 (-34.9..-36.5, present and not on top).
- Theme A's Violins I over violas and Violins II (6-10 dB).
- The Violin I solo and flute roles at 349-356.
- Hn 1's motto tail 357-360.
- The trio clarinet over the horn drone (c01: now 1-5 dB over Horn 4; the harp is now the problem).
- The re-bow fills (no loop pulsing at 3.95 s on any held note checked).
- The smooth sub. p transitions at 360 and 828.
- The hall and low-end settings (no 200-500 Hz excess against the references).
- The 105-120 / 305-320 tutti balance (Violins I level with Flute 1, over Horn 3 by 6 dB, low brass and timpani 8-10 dB under).
