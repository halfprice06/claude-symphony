# Cycle 42, critic C: dynamics over time (on the c41 render)

Render under review: `cycles/c41/render` (master and 32 stems after both c41 stem fixes), `cycles/c41/rendered_build/parts.json`, `build/rebow_fills.json`, and the delivered `mvt2-mockup-c41.mp3`. I compared it with c39 (uncapped string releases) and c40 (150 ms caps), and with the recordings: the stored final-release tails of Brahms 1/ii and 4/ii (`symphony/render/critics/c04/ref_*/metrics.json`, rtk `decay_fit`), and the Brahms 1/i and Dvořák 9/i stop decays that c41 critic C measured with the same rtk code.

Method:
- Plain RMS of stereo power per window in qn, mapped to seconds through each cycle's rendered parts.json tempo map.
- EBU momentary (M) and short-term (S) loudness from ffmpeg, read the same way `deliver_master.py` reads it.
- Simulations change stems by gain curves in qn and add the differences to the master. This is exact for changes to the volume envelope, which acts after the hall.
- Scratch scripts were in `/private/tmp/claude-501/mockup-loop/mvt2-c42-C/` and were deleted at the end.
- Each judgement is labelled measured, simulated or inferred.

## Manual notes (MANUAL-READING row 42, slot C: D1, May 2021 HO manual PDF pages 53-54 and 64; MANUAL-GAPS.md read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.53: shape lines with CCs, played live or drawn; MIDI CCs for sustained instruments because they change loudness mid-note; velocity for short articulations because it cannot change mid-note | Every hairpin on sustained notes is a CC11 ramp (0.125 qn steps). Velocity sets the pizzicato (bars 37-44), harp and timpani strokes. | Yes. Hairpins are drawn as straight lines. p.53 prefers played-in shapes, but nothing measured here traces a fault to the straight lines. |
| p.54: velocity is one value per note; CC1 and CC11 are continuous lanes | parts.json: one `vel` per note; `cc1`/`cc11` lanes per track | Yes |
| p.64: in HO strings and woodwinds CC11 sets loudness and dynamics and CC1 sets vibrato; LITE string patches put dynamics and vibrato on CC1; "MOD" patches switch articulations on CC1 | String and woodwind KS Masters on CC11 and CC1; brass and clarinets on CC1 dynamics since c30 (`CC1_DYN_TRACKS`). No LITE row is used (I checked every keyswitch in parts.json) and no MOD patch is used. | Yes |
| p.64: CC7 sets a track's level against the others; CC11 shapes each instrument's line | Balance lives in REAPER's volume envelope (after the hall). CC7 lanes are used for shaping in a few places so that the ring follows the line (S3): the bar 66 niente (c30, 223.5-226, 0 to -14 dB), Violins II 264-265.75, Trombone 1's floors, Clarinet 1 205-209.9 and the celli portato dips. | Partly, by choice (S3). Finding 1 shows a side effect: `tools/fit_rebows.py` plans for vol_db and CC11 but not CC7, so it treats the niente's CC7 fall as a hole and fills it back in. |

MANUAL-GAPS items for this lens: #7 (Felt Cresc rolls) is still untried; the crescendo rolls were not re-measured this cycle (slot B reads B3 this cycle). Nothing on these pages adds an item.

## State of the arc (measured)

- **Climax order holds.** Master momentary mean per bar: bars 61/62 -11.2 / -11.7 dB, bars 79/80 -16.4 / -17.5. In the mp3: -10.3 / -10.4 against -12.5 / -13.2 LUFS.
- **Delivery is on target.** LRA 15.5 LU, p10-to-max span 18.9 dB (c39 19.0, c40 18.8), true peak -1.6 dBTP, limiter about 2.3 dB.
- **Animando crescendo, bars 53-61.** The master rises in every bar: -32.3, -27.5, -26.4, -24.7, -23.8, -22.1, -20.9, -15.7, -11.2 dB.
- **The delivery squeezes the long crescendos.** Its lift falls from 8.1 to 3.4 dB over qn 178-200, so the mp3 rises only 2.9 LU there (S -19.5 to -16.6) where the master rises 6.7 dB. Bars 71-78 keep 49% of their rise. This follows from the c30 RATIO 2.2, and the LRA and span leave no room to change it. Finding 5 gives the mix-side help.
- **No loop pulsing.** Every same-pitch span over 8 s on every stem was checked (27 spans; 100-300 Hz band, centroid and pitch band, autocorrelation at 3.95 s against nearby lags). No string, brass or timpani span correlates at the loop period. The only span that does is the bass clarinet's pp A flat 2 in bars 3-6 (0.57 against -0.04). That correlation comes from c34's planned breaths every 3.5 qn (4.0 s at q=52), not from a sample loop, and the span ranges only 3.3 dB.
- **Hairpins.** I checked 230 hairpins on the stems, comparing the level in the first and last 30% of each on sounding notes only. 27 change by less than 1 dB in the printed direction. Most are short (0.5-1 qn) or sit on a phrase turn. The ones a listener would hear are in findings 3-5.

## Findings, ranked by what a listener would gain

### 1. The bar 66 niente rises for its first two beats: the c40/c41 re-bow refit filled in the c30 CC7 fade (measured; fix simulated)

**Where.** Violins II, violas and celli, qn 223-226 (printed decrescendo to niente on the tied note, with the down-bow at 223). The re-bow lists are keyed "223" in `build/rebow_fills.json`.

**What is wrong.**
- **Mechanism (read).** The niente is played by CC11 33 -> 12 together with c30's pre-hall CC7 lane (127 -> 25, 0 to -14 dB over 223.5-226, `_c30_niente_cc7`). `fit_rebows.py`'s plan is "vol_db + PLAN_DB_PER_CC x CC11". CC7 is not in it, so the fit reads the CC7 fall as an unplanned level loss and holds against it.
- **Fill values (read).** After the c40 and c41 refits, the 223 holds over 224-226 are:
  - Violins II +3.3..+4.0 dB (c39 -2.3..-4.0), and its fill sits at the +10 dB clamp from +0.08 s;
  - violas +6.5..+8.0 dB (c39 +1.2..-1.4);
  - celli +0.4..+1.3 dB (c39 -4.4..-5.9).
- **Result (measured).** Stem and master level per 0.5 qn:

| qn | 222.5 | 223 | 223.5 | 224 | 224.5 | 225 | 225.5 |
|---|---|---|---|---|---|---|---|
| master c39 | -45.4 | -45.8 | -47.1 | -48.5 | -49.6 | -53.0 | -53.0 |
| master c41 | -44.3 | -43.3 | -44.2 | -43.2 | -43.8 | -48.9 | -50.5 |
| **master, fix simulated** | -44.3 | -43.8 | -46.2 | -48.0 | -48.9 | -52.6 | -52.3 |
| Violins II c41 | -48.4 | -45.4 | -46.2 | -44.9 | -45.6 | -52.0 | -55.0 |
| violas c41 | -54.2 | -54.4 | -55.7 | -55.3 | -54.9 | -61.8 | -65.4 |

- **Bar means.** The master's bar 66 mean is only 0.6 dB under bar 65 (c39: 3.6 dB under).
- **In the mp3 the fade runs backwards.** Momentary loudness goes 222.5 -30.1, 223.5 -29.3, 224.5 -28.7, 225.5 -36.0 LUFS: the loudest moment of the niente is in its middle. c39: -30.7, -31.9, -34.5, -39.6.
- **Why c41's check missed it.** c41 recorded the niente as "223 vs 225.5: 6.4 dB". That number compares the two ends, so it cannot see a fade that holds for two beats and then drops in the last beat.
- This is the one printed niente in the movement, and it is on the S3 list.

**Fix.**
- **Generic, in `tools/fit_rebows.py`.** Add the track's CC7 lane to the plan: P(t) += 20·log10(cc7(t)/127). Score_config's comment says CC7 acts as linear amplitude before the hall. Then refit the 223 lists on Violins II, violas and celli.
- **Same blind spot elsewhere.** It is the only other re-bow under a CC7 lane: Violins II 263.921 (CC7 101, -2 dB, c41 B #2). Its c41 refit will have filled back part of B #2's -2 dB.
- **If the tool change waits.** Run `--skip "Violins II:223" --skip "Violas:223" --skip "Violoncellos:223"`. From 223.45 on, set the three lists' holds to their c39 values: Violins II about -2.5, violas from +1.2 falling to -1.4, celli about -5. Keep the first 0.45 qn of the c41 lists (the re-bow attack).
- **What I simulated.** I applied the c39 vol from 223.45 to 226.0 to the c41 stems, which gave the table row above. The master now falls steadily by 2-4 dB per beat. The cut runs in the volume envelope while the notes sound and ends at 226, before Horn 1's entry, so the ring of the louder level is not cut (S3).
- **Accept when** the master per 0.5 qn falls monotonically from 223 to 225.5, by at least 7 dB in total, and the mp3's momentary loudness falls over the same span.

### 2. Soft endings (extra check): c41's 400 ms caps stop the ring at -17 dB after 0.3 s, where c39 and the recordings were still ringing; the fix is longer pp/p releases plus a CC11 fall at soft repeats (measured; fix inferred)

**Where.** Every string phrase end at pp/p, the coda (bars 83-92), the final chord (note-off at qn 304), and the soft horn ends (Horn 1 bars 7-14 and 65-70, Horns 3-4 in the coda).

**Evidence.**

Final chord, master, level against the 0.3 s before the note-off:

| s after note-off | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.75 | 1.0 | to -10 / -20 / -30 dB |
|---|---|---|---|---|---|---|---|---|
| c39 (no caps) | -3.7 | -6.9 | -9.7 | -12.4 | -15.6 | -24.6 | -38.1 | 0.31 / 0.62 / 0.82 s |
| c40 (150 ms) | -9.4 | -18.3 | -21.2 | -24.1 | -28.0 | -32.6 | -46.1 | 0.11 / 0.23 / 0.58 s |
| c41 (300/400 ms) | -3.3 | -9.3 | -17.4 | -23.1 | -27.2 | -31.6 | -45.0 | 0.22 / 0.32 / 0.59 s |
| Brahms 1/ii, 4/ii final releases (rtk) | | | | | | | | 0.40, 0.20 / 0.79, 0.48 / 1.23, 1.15 s |

- **c40 cut the ending off.** The chord dropped 9 dB in 0.1 s and 18 dB in 0.2 s.
- **c41 starts like a natural release and then breaks.** It falls 9 dB in the first 0.2 s, then 8 dB in the next 0.1 s (81 dB/s) where the 400 ms release ends, then the IR envelope's hall plateau takes over (-23..-31 dB).
- **c39 rings like the recordings.** It falls smoothly at about 30 dB/s, with -10 dB inside the recordings' 0.20-0.40 s and -20 dB inside their 0.48-0.79 s.
- **The string stems show the same break.** For the Violins I C5 (movement I's last pitch) at +0.1 / 0.2 / 0.3 s: c39 -1.7 / -4.5 / -7.1, c40 -12.0 / -21.0 / -26.6, c41 -4.0 / -10.0 / -20.0 dB.
- **The mp3 behaves the same** (0.22 / 0.32 / 0.60 s). It ends 1 s after the last window above -65 dBFS, so anything past about -17 dB is faded out together with the file.
- **String phrase ends** (the actor's m41.py, soft ends; median time to -20 dB): c39 0.44, c40 0.26, c41 0.34 s. The recordings measure 0.43-0.58 s (Brahms 1/i stops median 0.485, Dvořák 0.49). The time to -10 dB is back (0.21 s, the same as c39), and no ending falls more than 10 dB in 0.05 s except Violoncellos 87 (10.6).
- **Horns.** Soft horn ends: t20 c39 0.38, c40/c41 0.31 s. The soft horns play the mf CC1 layers (c31), so the 237 ms mf/f cap acts on them; the 350 ms pp cap never does (c41 LEARNINGS).
- **The trade-off (measured).** Longer releases close the gaps at same-pitch repeats (S1). On printed repeats that had no other change between the renders, the dip (pre-level minus the minimum 30 ms window around the onset) shrank from c40 to c41:
  - Double basses 81: 11.0 -> 6.6 dB; 253: 10.4 -> 5.6;
  - violas 81: 5.7 -> 4.2; 82: 12.2 -> 8.8;
  - Violas div 82: 7.9 -> 5.0;
  - celli 66: 8.0 -> 2.8.
  - Median over 11 soft (CC11 <= 52) printed repeats: 8.0 -> 3.9 dB. Some of these, such as Violins II 44/50 and celli 128, also had c41 A #3's shorter portato gap.
  - So a single release value cannot give both a ringing phrase end and a separated soft repeat. The repeat has to be separated some other way.

**Fix.**
- **(a) pp/p releases.** In `build/mix.json` `sus_release_cap_ms`, for Violins I, Violins II, Violas, Violoncellos and Double basses, raise the pp/p entry from 400 to **700 ms**. That is the shipped release (524-931 ms) except on the longest groups. Keep 300 ms at mf-ff.
  - Inferred: section soft t20 about 0.42-0.44 s (c39 measured 0.44); final chord -20 dB at about 0.5-0.6 s; no 80 dB/s break at 0.2-0.3 s.
  - Do the same on the div and solo tracks, which play pp/p almost everywhere (Violas div in the final chord; Violoncellos div 274-286): 300 -> 600 ms at pp/p.
- **(b) Soft repeats.** Extend `STR_REP_NEW_BOW["sus_fall"]` from the basses (10 CC over the last 0.06 s at p or softer) to all string sections and the div tracks at p or softer. CC11 acts before the hall and also lowers the release's level, so the fall cuts the old note's tail at a repeat while a phrase end keeps its full release.
  - c41 measured the basses at 5.7-7.1 dB dips with a 400 ms cap and this fall; with 700 ms, start at 12 CC.
  - Check: printed soft repeat dips median at least 5 dB (c41 3.9; c40 8.0).
- **(c) Horns, optional.** Horns 1-4 and Horns 1-2 a2: mf groups 237 -> 350 ms, f/ff kept at 237. Check Horn 3's coda repeats (c34: under 3 dB) after the change.
- **(d) Order.** Make finding 1's `fit_rebows.py` change first, then refit the re-bows on the new render: longer releases fill the re-bow dips (c41 LEARNINGS).
- **Accept when:**
  - final chord master -10 dB at 0.25-0.40 s and -20 dB at 0.45-0.70 s after the note-off, with no 0.1 s step over 6 dB in the first 0.5 s;
  - section soft phrase ends t20 median at least 0.40 s;
  - soft repeat dips median at least 5 dB;
  - legato-join dip median within 0.5 dB of c41.

### 3. The bar 47 fp is hidden: Oboe 1's goal note swells 3.5 dB in its first 0.75 qn under a printed decrescendo, so the master dips only 1.8 dB after the fp (measured; fix simulated)

**Where.** Oboe 1, the D flat 5 at qn 148 (mf, decrescendo 148-151), over the fp at 148 in Violins II, violas and basses (FP_SPIKE). The celli have a decrescendo at 148 too.

**Evidence.**
- **The strings' fp works on the stems.** From the peak at 147.75-148.25 to 148.5-148.75: Violins II -43.5 -> -47.6, violas -40.2 -> -49.4, basses -40.1 -> -46.9 dB.
- **The oboe swells where it should taper.** Oboe 1's vol_db rises from +8.0 at 148.0 to +12.2 at 148.59. That is the ramp-in of the role `[148.0, 151.0, 3.5, 2.0]` (`build/roles.json`), on top of note trim +5 and HP_SOFT_DEC 4. The stem goes 148.25 -39.1, 148.5 -36.8, 148.75 -35.6, 149.0 -36.0, while its CC11 falls 72 -> 67.
- **The master hides the fp.** Per 0.25 qn from the fp peak: 148.25 -33.2, 148.5 -33.8, 148.75 -35.0, then 149.25 back up to -33.9. The fp reads as a bump in a level line, not as forte-then-piano.

**Fix.** In `build/roles.json`, have Oboe 1's 148 role reach its full value at the onset instead of 0.6 qn later. For example `[147.95, 151.0, 3.5, 0.1]` with the HP_SOFT_DEC 4 running from 148 to 151 under it, so vol_db steps to about +12.2 at 148.0 and falls to +5.5 at 151.
- **Simulated** (vol 12.2 at 148.0 falling linearly to 5.5 at 151; unchanged before 148): the oboe body goes 148.25 -38.2, 148.5 -38.0, 148.75 -37.2, 149.0 -37.6. That leaves a 1 dB bloom from the sample instead of 3.5 dB. The master goes 148.25 -32.9, 148.5 -34.4, 148.75 -36.1, 149.0 -35.1: the dip after the fp is 3.2 dB instead of 1.8.
- The change is a vol shape on a held note, with no fast fall, so S3 does not apply.

### 4. The bar 91 morendo: Violas div re-bow piece at 298.3 swells 3.7 dB at the start of the printed decrescendo and now sits on top of the first violins (measured)

**Where.** Violas div (C4 in the coda chord), re-bow 298.3 and the hold after it, qn 297.5-301. The other strings play the printed decrescendo 298-301 into the ppp chord.

**Evidence.**
- **Fill values (read).** The c41 refit's 298.3 piece peaks at vol +2.57 at 298.47 (c39 -3.38) and holds -5..-6.8 dB (c39 -7.5..-9). The 301.25 piece starts at +3.75 (c39 -7.1). The `--hold-max-after 301:0` cap does not reach the 298.3 piece's attack.
- **Stem level (measured), qn 297.0 / 297.5 / 298.0 / 298.5 / 299.0 / 300.0:**
  - c41: -55.2, -53.4, -51.5, -52.0, -53.3, -55.2;
  - c39: -56.0, -56.1, -54.6, -55.6, -56.1, -59.1.
- **Balance against the violins (measured).** At 298-299 Violas div is the loudest upper string (-51.5 against Violins I -52.3 and Violins II -54.0). In c39 it sat 3 dB under Violins I.
- The master effect is small (+0.4 dB at 297.5-298, measured). What a listener would hear is an inner voice that grows as the morendo begins and then covers the violins' C5 (inferred).

**Fix.** Re-level the Violas div lists at 298.3 and 301.25 to the c39 piece means, the way `relevel41.py` re-levelled the basses' pedal. Alternatively refit them with `--hold-max-after 295:0` for Violas div and clamp the 298.3 attack fill at +2 dB over the previous hold. Accept when Violas div falls from 298 to 301 with no window louder than at 297.5, and stays 2-3 dB under Violins I at 298-301.

### 5. Bars 56-59 and 75-76: printed crescendos are flat in the lead voice (measured; fix simulated for bars 56-59)

**Bars 56-59 (qn 184-200).**
- **Score.** mf at 184; crescendo 188-195 to f at 196 (Violins I/II, celli, winds, Horn 1).
- **Lead violins flat (measured).** Violins I per qn from 188: -32.4, -33.0, -34.3, -34.6, -34.1, -32.4, -32.5, -32.8, then -31.2 at the f. That is a 0.2 dB fall across the crescendo. The line climbs to E6, and with CC11 77 -> 88 and vol +5 -> +7 the top register still does not get louder.
- **Celli fall.** They drop 2.4 dB (188 -33.2 to 194 -35.6) because their role `[190.5, 204, -3, 4]` ramps in during the hairpin.
- **The f does not hold.** After the f the master falls 1.7 dB (196 -22.8; 197-199 -24.5 / -24.1 / -24.5) before the bar 60 crescendo.
- In the mp3 the delivery takes away 55% of the remaining rise.

**Fix (simulated).**
- In `build/score_config.py`, `LEVEL_SHAPES` for Violins I and Violins II: add `[(190.0, 0.0), (194.0, 2.0), (199.6, 2.0), (200.2, 0.0)]`.
- In `build/roles.json` for Violoncellos, move the -3 role so that it is fully in by 188, before the hairpin: `[186.5, 204, -3, 1.5]`. The celli's level from 194.5 on does not change.
- **Simulated master per qn 188-199:** c41 -27.9, -26.8, -26.6, -27.6, -26.9, -25.7, -25.6, -25.7, -22.8, -24.5, -24.1, -24.5 -> -28.6, -27.4, -27.2, -27.8, -26.4, -24.9, -24.6, -24.8, -22.2, -24.1, -23.6, -23.9.
- That is a 6.4 dB rise from the mf to the f instead of 5.1. Violins I now rises 3.8 dB from 190 to 196, and bar 59 sags 1.6 dB instead of 1.7.
- From 200 on nothing changes, so the climax order and the limiter stay as they are (inferred: these bars are under the delivery knee).

**Bar 75-76 (qn 250-254), crescendo in both violin sections.**
- **The sag (measured).** Violins II's F5 (the Leg BC target at 251.775, tied over the up-bow at 253) sags 5-7 dB after its arrival: 251.0 -37.7, 252.0 -42.6, 252.5 -43.5, 253.0 -44.7, 254.0 -37.6.
- **The master stalls** for six windows (0.5 qn each, 3 qn) inside the hairpin: -31.6, -31.5, -31.9, -31.7, -31.1, -32.1.
- **Fix.** Add `LEVEL_SHAPES["Violins II"]` += `[(252.25, 0.0), (252.5, 4.0), (253.2, 4.0), (253.45, 0.0)]`. Not simulated; check it against the 253 notch.

## Do not touch

- The climax order (bars 61/62 over 79/80 by 5 dB in the master and 2.1 LU in the mp3) and the delivery settings (LRA 15.5, span 18.9, limiter 2.3).
- The bar 53-61 animando rise in the master.
- The hall (fx_volume 0.095, 160 Hz low cut, ir_setup 0.7).
- c41's 300 ms mf-ff string caps (they gave back the time to -10 dB without the c40 cut-offs).
- FP_SPIKE on the bar 47 strings.
- The c38 basses' niente cut and c30's niente CC7 lane: keep the lane and fix the fit that undoes it.
- The re-bow layout (no loop pulsing anywhere).
- The bass clarinet's bar 3-6 breaths.
- The final chord's CC11 fade.
