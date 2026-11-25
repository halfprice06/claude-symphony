# Cycle 14, critic C: dynamics over time (lens C2), on the c13 render

Sources: `cycles/c13/render/` (master, 31 stems, 4 return stems), `cycles/c13/scherzo-mockup-c13.mp3`, `cycles/c13/build_render/parts.json` and `mix.json`, `build/score_config.py`, `build/roles.json`, `build/early_fills.json`, `build/pitch_trims.json`, `build/rebow_fills.json`, `tools/build_reaper.py` (`vol_points`), `build/mockup-events.tsv`, the c12 render and data for comparison. Levels are K-weighted mean-square dB (BS.1770 filter, no gating) on the c13 tempo map unless marked "plain" (the plain RMS of `metrics.md`). Bar b starts at qn 3(b-1). "Measured" = a number from the render or the data; "inferred" = reasoned, not tested.

## Manual notes (cycle 14, slot C: group D1, May 2021 HO manual PDF pages 53-54 and 64; MANUAL-GAPS.md read)

| Page | What the manual says | Where it applies here | Does the render follow it? |
|---|---|---|---|
| p.53, p.64 | Velocity sets loudness and dynamics on short articulations and cannot change inside a note; CCs shape sustained notes. | Every Stac / Spic / Pizz row; the theme head. | Yes (measured in parts.json): the string staccatos play at CC11 120 with the dynamic in the velocity (v57 at p in Violins I bar 13, celli bar 57, violas bar 61). |
| p.64 | LITE instruments: CC11 is overall loudness, CC1 carries dynamics and vibrato together. | Violins I's 39 notes on Sus Marc LITE (the theme head's half note and, from c13, its two slurred eighths; the hemiola half notes 300-310 and 900-910). | Yes (measured): on that row CC1 follows the printed dynamic (51-58 at p, 60-66 at mp, 92-98 at f/ff) and CC11 runs with it (43-52, 55-64, 94-114). |
| p.64 | CC7 sets a track's level against the other instruments; CC11 shapes the changing dynamics of each instrument. | All tracks. The pipeline uses the REAPER volume envelope in place of CC7 (CC7 lanes are empty). | In part. The envelope also carries `soft_trim_db` / `dyn_trim_db`, which are keyed to the printed dynamic curve, so they move inside every hairpin and take back 0.9 dB of each 10 CC of a crescendo (winds 1.05). This is finding 2. |
| p.64 | The CCs cross-fade samples of different dynamics, so loudness and timbre change together. | Layer edges on the solo winds. | Checked on Clarinet 1 (CC1 is its dynamics lane): note-body level against CC1 is flat within 3 dB from CC1 40 to 80 and rises 11 dB from 80 to 105; single pitches differ far more than the CC does (F5 to G sharp 5 are 3.6-8.3 dB over the track's curve). Finding 4. |
| p.54 (figure) | CC1 and CC11 lanes are drawn as continuous curves through the phrase. | Legato lines. | Yes: 16 points per second on Clarinet 1's trio tune (CC1 18-69) and on the celli's (CC11 38-85). |

MANUAL-GAPS #7 (recorded crescendo rolls) is still unused; the three printed roll crescendos grow without it (below), so I do not ask for it.

## Checks the cycle note asked for

- **Soft ends over 0.30 s (measured).** Nothing became wetter. Timed from the note-off, with the level at the note-off as the reference, Violins II at 444.786 falls 10 dB in 0.22 s dry and 0.29 s with R Strings (c12: 0.22 / 0.30 s), and the solo at 1066.81 in 0.11 s dry (c12: 0.08 s). The actor's 0.31 and 0.33 s come from the measure's reference, the loudest 10 ms frame in the last 0.3 s before the end: in c13 the solo's last note peaks 0.21 s before its end (c12: 0.09 s), so 0.12 s of the note's own printed diminuendo (1062-1067) is counted as decay. R Strings is 7.9 dB under the dry solo there and adds 0.03 s. To bring the figures back, change the reference in the check to the mean of the 50 ms before the note-off. No hall, send or Stereo Double change is needed for this.
- **Stale state (measured).** No effect on the render. Legato notes whose data are identical in c12 and c13, first 150 ms, c13 minus c12: Horn 4 (35 notes), Violins I (84), Violoncellos (170), Violas (56), Horn 3 (87): median 0.00 dB, none over 3 dB.
- **S3 (measured).** Both sub. p's follow a played rest and the hall decays under them: at 360 R Strings falls -37.9 to -45.5 dB over 0.4 s with no step; at 828 -46.1 to -52.3 dB. Bar 73 (216): master falls 13.9 dB in the 0.3 s after the cut-off. G.P.: master -37.3 dB at the bar line, -47.6 at +0.3 s, -60.9 at +0.6 s.
- **Loop pulsing (measured).** At these tempos no string note lasts 3.95 s between re-bows (the longest pieces are 3.4-3.7 s). Horn 1's last G sharp (10.9 s): envelope standard deviation 1.3 dB, autocorrelation at 3.95 s -0.07 (level) and 0.25 (centroid): no loop period. The horn drone of 456-504: -0.21 / -0.15. One re-bow step fails: finding 3.
- **Range and summit (measured).** Master LRA 23.4; delivered LRA 15.0, p10-to-max span 19.8 dB (target 16-19). The summit is the loudest passage: 3 s loudness -12.0 at bar 336 against -15.1 at bar 104 (master), -9.6 against -13.7 (mp3); 0.4 s loudness -10.6 against -12.2 at bar 300 (mp3 -8.4 / -10.1). No bar-to-bar step of 2 dB or more is reversed by the delivery ride.
- **Timpani rolls (measured).** 101-103: -35.2 to -28.8 dB (+6.4, 14 dB under the master). 205-208: flat at -48.5 for two bars, then -40.3 to -35.8 under the printed crescendo. 301-303: -40.9 to -33.3. 129-130 and 285-286 (no crescendo): start -33.2, settle to -42. One roll grows without a printed crescendo: finding 5.
- **sfp at bar 301 (measured).** Works: master -12.7 dB on beat 1, -23.5 at 901.5, -21 to -22.7 through bar 302, -13.9 at 908.

## Findings, ranked by what a listener would gain

### 1. The fugato's p entries are the softest music in the delivered file, and the exposition does not grow (measured)

**Where.** Bars 57-66 (qn 168-198) and 289-294 (864-882): the theme head as a fugato subject, celli p alone, then violas p (celli pp), then Violins II p. Also the coda's pp entries, bar 326 (975-978).

**What is wrong.**
- Theme A at bar 13 and the subject at bar 57 carry the same printed p and the same data (v57, CC11 120). Master, K per bar: theme A bars 13-20 -36.8 / -31.4 / -35.5 / -38.5 / -34.8 / -35.0 / -33.7 / -37.8; subject bars 57-60 -40.1 / -43.8 / -40.8 / -41.0. The subject is 5-12 dB under the theme.
- The second entry adds nothing. Bars 61-64 (violas p over the celli's pp): master -43.0 / -42.4 / -39.9 / -40.3, mean -41.4, the same as the celli alone (-41.4). The violas' subject measures -44.4 / -46.6 / -41.2 / -42.3 on the stem against the celli's -40.0 / -44.2 / -40.8 / -41.1. Violins II's entry (bars 65-66, role +4 from an earlier cycle) gives -37.9 / -39.2. Ten bars of a fugato sit within 2 dB of each other; the growth starts only at bar 67 (-34.1) under the printed crescendo.
- Delivered: bars 57-62 are -34.6 / -37.5 / -34.3 / -34.3 / -35.9 / -35.4 and bars 289-293 -36.7 / -37.9 / -35.6 / -35.6 / -37.3. Theme A p is -19.8 to -27.4, the ppp opening -28.1, the ppp close -29.0. So a printed p is 6-9 dB softer than the two ppp passages and 15-18 dB under the programme loudness (-19.8). These bars and the coda's pp entries (bars 323-327, -32.0) hold most of the delivered file's lowest tenth of 3 s windows (p10 -29.4): they are why the span is 19.8 and not 16-19. The ride is at +5.5 to +7.2 dB here (theme A: +11) because it is still recovering from the ff of bars 53-55; the mix has to do this, as BRIEF item 6 says.
- Bar 326: master 325-328 -42.5 / -45.3 / -39.7 / -34.2; the violas' pp entry (-46.7) is 3.7 dB under the celli's (-43.0), so the second entry falls.

**Fix (roles, `build/roles.json`; CC11 and velocities unchanged).**
- Violoncellos `[168, 180, 3]`, `[864, 876, 3]`.
- Violas `[180, 192, 5]`, `[876, 888, 4]`, `[975, 978, 3]`.
- Violins II: keep `[192, 198, 4]`.
- If the delivered bars 57-60 stay under -31, add delivery rows to `RIDE_TRIMS` in `build/score_config.py`: `[(167.5, 0.0), (168.5, 2.0), (196.0, 2.0), (204.0, 0.0)]` and `[(863.5, 0.0), (864.5, 2.0), (882.0, 2.0), (888.0, 0.0)]` (positive rows are inferred to work; the existing rows are all negative).

**Targets.** Master K means: bars 57-60 about -38.5, 61-64 about -37, 65-66 about -36 (each entry 1-1.5 dB over the last); bars 289-292 about -39, 293-294 about -38; bar 326 within 1 dB of bar 325. Delivered bars 57-66 and 289-294 at -31 or higher; delivered span 19 dB or less (the effect on the span is inferred).

### 2. The dynamic-trim tables take back the crescendos of single instruments: 40 of 215 printed crescendos do not rise on their own stem (measured)

**Where.** Whole movement; worst on the clarinets, flutes and violas between mf and f. Examples: bars 125-128 (372-384), 193-196 (576-588), 281-284 (840-852), 49-52 (144-156), 329-332 (984-996).

**What is wrong.**
- `build_reaper.py` `vol_points` adds `soft_trim_db` / `dyn_trim_db` to the volume envelope, read from the printed dynamic curve (anchors: p CC 46, mp 58, mf 72, f 88, ff 114). The tables (Movement I's) fall steeply toward f: Flute 1 and 2 p +5, mf +2.5, f -4, ff -1; Clarinet 1 p +5, mp +2.2, mf +0.1, f -4.2, ff 0; Clarinet 2 p +7.1, mp +4.3, mf +1.0, f -3.8; Violas p +5, f -2, ff -3; trombones and tuba pp +14, f about -1. A crescendo that crosses these anchors loses that much level while CC11 rises.
- Audit of every hairpin of 2 qn or more with sustained notes (body level of the first note in the hairpin against the arrival note): 215 crescendos, median rise 4.6 dB, 40 with less than +0.5 dB (19 %); 125 decrescendos, 22 that do not fall. Over the 144 crescendos whose curve rises 10 CC or more, the stems gain a median 1.8 dB per 10 CC and the trim takes away 0.9 (winds: gain 1.5, trim -1.05, 10 flat or reversed; brass 2.6 / -0.6, none reversed; strings 2.1 / -0.7).
- Cases (stem change, curve, trim change over the hairpin): Clarinet 1 840-852 -3.3 dB (CC 48 to 82, trim -7.1); Clarinet 2 372-384 -3.0 (48 to 83, -8.9); Clarinet 2 576-588 -2.7 (49 to 88, -10.2); Clarinet 1 984-996 0.0 (51 to 101, -5.9); Flute 1 144-156 -1.9 (73 to 88, -6.1); Violas 900-910 -0.6 (49 to 114, -7.5).
- Per-note check on Flute 1 (B5, 18 legato notes): body level after removing the parts.json envelope is -32 to -40 dB at every CC11 from 42 to 98 with no trend, then -32.5 at 117. The stem medians in `metrics.md` say the same: Flute 1 mp -39.5, mf -38.2, f -39.7, ff -31.4; Clarinet 1 p -41.4, mp -40.4, mf -40.9, f -39.5, ff -34.1. One wind instrument has 2-4 dB between p and f and 5-8 dB between f and ff.
- What it does to the crescendos into f: the wind choir stops growing while the strings go on. Winds minus strings (family sums per bar): bars 125-129 +0.1, +0.2, -4.0, -4.8; bars 281-285 +0.4, +2.8, -1.1, -4.6; bars 193-197 +1.5, +2.8, -0.7, -3.2. At the f arrivals of bars 129 and 285 the winds gain +1.0 and -0.1 dB over the bar before while the strings gain +1.8 and +3.4. The master still rises (5-6 dB over each of these four-bar crescendos), so this is heard as the winds receding inside the crescendo, not as a missing crescendo (inferred).

**Fix.**
- Generic, `tools/build_reaper.py` `vol_points`: a crescendo counterpart of the existing `SOFT_DECRESC_HOLD` block. New `CRESC_TRIM_HOLD = {"keep": 0.3, "release_s": 0.8}` (None = off): for every `"cresc"` hairpin whose table trim at its end is lower than at its start, from the hairpin's start to the moved onset of the first note at or after its end, the trim may fall only by `keep` of its fall below the value at the start; from that onset the held amount returns to the table value linearly over `release_s`. This matches the adopted hairpin default (EW-TEMPLATE-PLAN section 9: a crescendo rises, then settles). Since the c50 template mix the hall is fed by post-fader REAPER sends (`mix.json` `opus_reverb_off`, `send_profiles`), so this envelope acts before the hall and the release does not cut a tail (read in mix.json; check one arrival on R Winds).
- Tables, `build/mix.json` `tracks`: Flute 1 and Flute 2 `dyn_trim_db.f` -4 to -1.5; Clarinet 1 `f` -4.2 to -1.5; Clarinet 2 `f` -3.8 to -1.0. The winds are 3.2-4.8 dB under the strings at the f arrivals above, so this goes the right way for balance too; if critic B's f passages (bars 41-52, 129-131, 273-275, 285-287) end with the winds over target, take it back with roles on those bars, not in the tables.

**Targets.** Fewer than 15 of the 215 crescendos under +0.5 dB; Clarinet 1 840-852 and Clarinet 2 576-588 rising 2 dB or more; winds minus strings at bars 129, 197 and 285 within 3 dB of its value two bars earlier. Re-run the delivery and check the limiter stays at about 3 dB.

### 3. The last bar: Violins I's ppp G sharp dips 5-6 dB for 0.35 s at its last re-bow, under the fermata (measured; BRIEF item 8)

**Where.** Violins I, re-bow at qn 1125.156 (bar 376 starts at 1125; only Horn 1 and Violins I sound from there to the end, 3.6 s).

**What is wrong.**
- Violins I stem in 50 ms frames around the re-bow (plain dB): -45.0 to -46.4 before it; then -48.2, -49.1, -50.0, -50.0, -50.9, -51.9, -50.8, -47.6; back to -46.1 at +0.40 s. The master goes -42.1 to -46.1 dB over the same 0.35 s (Horn 1 holds -48). The re-bow at 1116.3 dips 2.5-3 dB for 0.4 s and the one at 1103.8 about 1.5 dB.
- This is the same size as in c12 (4.3 dB) and it is on the movement's last note, with nothing to cover it. Dan's note on Movement II was about exactly this place in a piece ("some kind of weird bowing effect being applied on the last note").

**Fix.**
- Fit the residual with `tools/fit_rebows.py` on the c13 Violins I stem (it can fit corrections on a stem that already carries fills, ONE_TIME_c14 item 7) for 1125.156 and 1116.299 and add it to `build/rebow_fills.json`; the residual at 1125.156 is about +2, +3, +4, +4, +5, +6, +5, +1.5 dB at 0.00 to +0.35 s.
- If the fitted fill does not hold, move the point in `build/rebow_moves.json` from 1125.156 to 1123.0 (bar 375 beat 2), where the harp harmonics enter and the celli and basses' pizzicato of 1122 still rings. The last bow is then 4.46 s (limit 4.5 s for `AUTO_REBOW`), and the 3.95 s loop point falls in the final fade (inferred; check the last second for a step).

**Target.** No frame of the Violins I stem more than 2 dB under the mean of the 0.3 s before the re-bow at 1125.156 and 1116.299; master dip at 1125.2 under 1.5 dB.

### 4. Single notes stand 6-10 dB out of three soft wind solos, against the printed hairpins (measured)

**Where and what.**
- **Clarinet 1, bar 82 (qn 243, F5, p dolce, peak of the printed < >) in the pp F major episode.** Body -30.5 dB against -40.2 for the notes each side (+9.6); the master is +4.8 dB over its neighbours and bar 82 (plain -32.6) is the loudest bar of the episode after bar 73 (which holds the ff chord's tail), 1.9 dB over the next loudest (bar 85). CC1 is 60 on this note and 63 on the one before, so the controller is not the cause. Clarinet 1's F5 to G sharp 5 measure 3.6 to 8.3 dB over the track's level-against-CC1 curve (13 notes); `pitch_trims.json` has rows for 68-73, 75, 80 and 81 but none for 77-79. The same pitches give +6.5 dB at bar 246 (qn 735, G5, pp, master +2.3), +8.7 at bar 302 (qn 904, F5: Clarinet 1 is the loudest stem of the sfp's p bar at -30.4 plain) and +7.7 at bar 214 (qn 640, covered by the violins).
- **Bassoon 1, bars 233-235 (qn 696-705, p dolce, < 699-702, > 702-705), the codetta.** The B3 at 699 measures -34.6 / -30.9 / -32.2 (thirds of the note) and the printed peak, the C4 at 702, -37.8: the crescendo runs 8.4 dB backwards and the master's bar 234 is 5.4-6.3 dB over bars 233 and 235. Causes: `early_fills.json` Bassoon 1 `"699": {"db": 4.6, "hold_s": 0.2}` (fitted in c04 to a join dip that is no longer there; the envelope is +11.1 dB at 699 and +9.0 at 702), and B3 is 2.1 dB over the track's curve while C4 is 3.0 under.
- **Oboe 1, bars 346-347 (qn 1035-1040, p dolce, < 1035-1036, > 1036-1038), the Meno mosso.** The printed peak, B5 at 1036, has a body of -36.7 / -35.2; the A5 after the hairpin (1038) reaches -32.1 / -28.7 and the G sharp at 1039.5 -32.0. The line peaks one bar after the hairpin, 6 dB over the printed peak, and the master's bar 347 (plain -34.6) is the loudest of 345-348. Causes: Oboe 1's B5 is 4.7 dB under its level-against-CC11 curve on the legato rows (7 notes; C6 -3.6, E5 +5.0 over 12 notes), and `PHRASE_SHAPE` raises CC11 from 50 to 58 at 1038.1-1038.8, straight after the printed diminuendo ends.

**Fix.**
- `build/pitch_trims.json` Clarinet 1: add `"77": -4.0, "78": -3.0, "79": -5.0` (rows as listed in `_arts`); add 904.0 to `_skip_onsets` only if the bar-302 chord then lacks the clarinet.
- `build/early_fills.json` Bassoon 1 `"699"`: `db` 4.6 to 1.0. `build/pitch_trims.json` Bassoon 1 (new entry, `_arts` `["Leg Slur", "Sus"]`): `"59": -2.0, "60": 3.0`.
- `build/pitch_trims.json` Oboe 1: a second entry for the legato rows if the file allows one per row set (the present one is for `Stac DblTng RRx9` only): `"83": 4.0, "84": 3.0, "76": -4.0`. And keep the phrase arch off the notes that follow a printed hairpin: `LEVEL_SHAPES["Oboe 1"]` `[(1038.0, 0.0), (1038.5, -3.0), (1040.0, -3.0), (1041.0, 0.0)]`; the generic form is a `PHRASE_SHAPE` option that holds the arch at zero for the rest of the note-group after a printed > (new key, off by default).

**Targets.** Clarinet 1 at 243 within 4 dB of its neighbours and master bar 82 within 2 dB of bars 81 and 83; Bassoon 1's C4 at 702 at or over the B3 at 699; Oboe 1's B5 at 1036 the loudest note of 1035-1040 by 1-3 dB.

### 5. Two small level events against the print (measured)

- **Timpani pp roll, bars 237-240 (qn 708-718), no crescendo printed.** Per qn: -47.2, -48.5, -47.2, -49.2, -53.9, -54.1, -53.3, -52.4, -50.1, -48.9: it settles 7 dB by 712, then grows 5.2 dB over 714-717 while the master falls from -36.9 to -41.9 into the fermata (poco rit., everything else pp >). The envelope is flat there (+12 dB from 711 to 718.2), so the growth is the roll sample. At 717 the roll is 7 dB under the master and the second-loudest stem of bar 240. Fix: `LEVEL_SHAPES["Timpani"]` add `[(713.5, 0.0), (715.0, -2.5), (717.0, -5.0), (718.0, -5.0)]`. Target: no qn of the roll after 712 more than 1 dB over the qn before it (Dan's priority 5).
- **Downbeats of the ff tutti, bars 105 and 305 (qn 312, 912).** Master over the first eighth -11.3 and -11.5 dB, the level of the fff summit's bars (-11.2 / -10.9 / -11.2), then -17.4 and -18.3 on the second eighth and -15 to -17 through the tutti. Flute 1's staccato E6 on that beat is -18.5 / -20.5 dB, 8-10 dB over its own next notes at the same velocity and pitch (314: -26.3) and level with Violins I (-17.9 / -17.8). Fix: `build/note_trims.json` Flute 1 `"312.0": -5.0, "912.0": -4.0`. Target: master first eighth of 312 and 912 at -13 dB or lower, still 2 dB or more over bar 104 / 304's last beat (inferred that the flute supplies about 1.5 dB of the peak; check before and after).

## Do not touch

The summit chain and its margin (3 s loudness 3.1 dB over the next loudest passage on the master, 4.1 on the mp3); the sfp at bar 301 (`FP_SPIKE_FROM_ONSET`, sfp roles: -12.7 to -23.5 to -13.9 dB); both sub. p's and their tails (S3 holds); the three crescendo rolls and the settle of the f rolls at 129-130 and 285-286; the coda build 329-336 (-25.2, -24.8, -23.4, -20.0, -15.8, -15.1, -13.4, -11.2 per bar, `cresc_long`); Horn 1's closing contour (flat within 0.5 dB over 1122-1127, then the fade); the hall, sends and return pans (the two soft-end figures are a measurement effect); the delivery settings other than the two optional `RIDE_TRIMS` rows of finding 1; `SOFT_DECRESC_HOLD` as set; Violins I's Sus Marc LITE rows with CC1 following the dynamic.
