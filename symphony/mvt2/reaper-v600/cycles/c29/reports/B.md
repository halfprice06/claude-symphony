# Cycle 29, critic B: balance and levels (on the c28 render)

Levels are K-weighted, ungated, summed over both channels (about 3 dB above the per-channel RMS in `metrics.md`), from 4096-point frames every 50 ms on `cycles/c28/render/`, averaged per qn on the `build/parts.json` tempo map. "Wobble" below means the median, over 1 s windows, of the range of 100 ms broadband RMS frames. c26 numbers come from the series 1 render (v77) and are used only where the notes are the same. "Measured" means a number from the render, parts.json or a build table. "Inferred" means a judgement about what a listener hears.

## Manual notes (B2: May 2021 HO manual pp. 194-200; `loop/MANUAL-GAPS.md` read)

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.194, 196: the Mix page has a strip per instrument with volume, pan, mute, solo, load state, output and inserts. Its Sub Mixer channels are the mic positions, and each one's Load button loads or unloads that mic's samples. | `mix.json` `mics` (for example woodwinds Close 0.5 / Main 0.8, horns 0.5 / 1.0, Cb Close 0.6 / Main 1.0, tuba 0.45 / 1.0). Unlisted mics are unloaded. | Yes. The mic volumes are written into each Opus state, and track level is REAPER volume. |
| p.195: Store Mix and Restore Mix save the settings of every channel. | The mix is rebuilt from `mix.json` on every full rebuild. | Not used, and not needed: a script rebuild keeps the same information. |
| p.196, 198: an FX Bus channel holds the Reverb. The Sub Mixer channels feed it through Effects Send inserts, each with a Level slider and a Post switch. The manual says post-fader is typical for reverb. | `mix.json` `reverb` (one true-stereo hall copied into every patch's fx:0) and per-group `send` levels: strings 0.25, harp 0.3, winds 0.35, low brass/timpani 0.45, horns 0.5, DIV tracks 0.5. `send_pre_fader: true` (series 1 c09). | Partly. The sends are pre-fader, unlike the manual's typical setting. That is deliberate (send = level x channel volume, series 1 c09), and depth comes from the send levels. Nothing in this cycle's balance findings comes from the sends. |
| pp.199-200: the EQ inserts are Bass Comp (a 32-256 Hz boost), Channel Equalizer (low shelf, peak, high shelf, 30 Hz-18 kHz) and Equalizer (6 bands with HP/LP). | All EQ is ReaEQ after Opus: Cb bell2 80 Hz -6 and bell 160 Hz +4.5, Vc bell 170 Hz +3, `loud_eq` at the climaxes, high-passes, side shelves. | Equivalent. A ReaEQ after the instrument acts on both the dry sound and the hall, as an insert on the Opus master channel would. No Opus mic choice would replace these EQs. The coda's low-end excess (finding 2) is a level problem, not an EQ or mic one. |

## 1. Four carried-over loop profiles now run over re-bowed notes. They make the held pedals swell and dip 8-11 dB every second (measured)

**Where.** `build/loop_profiles.json`:
- Double basses `220` (bars 65-70, qn 220-238) and `271` (bars 82-86, qn 271-286)
- Violoncellos `274` (bars 83-86)
- Violins I `0` (the opening C5, bars 1-3)
- Timpani `226` (the ppp roll, bars 67-70)

**What.** Each profile was fitted in series 1 to one long note's 3.95 s sample loop. `score_to_parts.py` (around line 4027) still applies each one from the original onset to the note's original end (`orig_end`). Since c27, AUTO_REBOW and REBOW_AT split these notes into new bows: Cb at 221.8, 225.2, 227.8, 230.4, 233.0, 235.7 and at 273.2, 276.05, 278.35, 282.2, 283.6; Vc at 275.5, 277.6, 279.6, 281.7, 284.15; Vln I at 2.4, 4.6, 7.35. Each new bow restarts the sample, so the profile's phase no longer matches the loop and the correction adds modulation instead of cancelling it.

On Cb 278.4-282.2, the vol_db and the 271 profile alone correlate at 0.82. vol_db swings from -0.6 to +11.8 dB within 0.3 s. The stem follows it, at 100 ms frames from -50 to -35 dB (279.0-279.6).

| Wobble (median 1 s range, dB) | c26 | c27 | c28 |
|---|---|---|---|
| Double basses 222-238 | 1.8 | 10.0 | 9.2 |
| Double basses 273.3-286 | 3.9 | 12.2 | 11.0 |
| Violoncellos 275-286 | 2.1 | 9.0 | 8.3 |
| Violins I 1-9 | 3.7 | 12.0 | 10.6 |
| Timpani 226-237 | 1.2 | 1.0 | 4.6 |
| Master 274-285.5 | 4.6 | 7.1 | 7.1 |

For comparison, re-bowed held notes in c28 with no profile measure 3.9 dB (Vc 293-301) and 5.9 dB (Cb 286-299, with two note changes). The timpani profile matched its layer through c27. c28's `TIMP_CC1_MAP` moved the roll to another CC1 layer, which has a different loop.

Inferred: the bass pedal under Horn 1's bars 67-70 solo and under the coda harmonics wobbles in level instead of holding, and the opening ppp C5 pulses. This is exactly the kind of periodic movement Dan heard in series 1 (BRIEF item 8).

**Fix.**
- Delete Double basses `220` and `271`, Violoncellos `274` and Violins I `0` from `build/loop_profiles.json`. Re-bows already break those loops.
- Generic option: in `score_to_parts.py`, end a profile at the note's own end after the re-bow split, not at `orig_end`.
- Delete Timpani `226`, or refit it with `tools/fit_loops.py` on the c28 Timpani stem. Its layer is now the one c28 plays.
- The c28 re-bow fills on these notes were fitted on c27 stems that already carried the profile. Remove the profile from the c28 stems in a simulation (the volume envelope comes after the hall, so this is exact), then rerun `tools/fit_rebows.py` on the simulated stems for those tracks.
- Target: wobble at most about 4 dB on all five passages.

## 2. Coda bars 83-86: the ppp basses are the loudest stem and cover the dolce harp harmonics and Clarinet 1's entry. The basses' ppp is louder than their pp (measured)

**Where.** Double basses (stem 26) and Harp harmonics (stem 27), qn 274-286. The score prints Cb tutti ppp ("change bow at will"), Vc 4 soli ppp, harp harmonics p "dolce" at 274-277, and Clarinet 1 "dolce" from 280.

**What.**

| qn (2-qn means) | 274 | 276 | 278 | 280 | 282 | 284 |
|---|---|---|---|---|---|---|
| Cb, c28 | -44.9 | -44.7 | -43.1 | -43.8 | -45.5 | -45.8 |
| Cb, c26 | -52.9 | -51.9 | -51.4 | -49.9 | -54.1 | -55.7 |
| Harp harmonics, c28 | -51.3 | -59.3 | | | | |
| Harp harmonics, c26 | -45.8 | -51.0 | | | | |

- The basses are 6-9 dB louder than in c26, and the harmonics 5-8 dB softer.
- At note peaks the harmonics reach -42.5 to -47 against the Cb's -36 to -43, so they never top the basses.
- At 280 Clarinet 1 enters at -43.9, under the Cb (-42.8).
- Per printed dynamic, the basses' note bodies measure ppp -46.3, pp -49.0 and p -46.4 dB, so their ppp is as loud as their p.
- The master's 40-100 Hz band sits only 6-8 dB under its K level here, against a median of 21 dB over the movement. That is the most bass-heavy stretch of the piece.

**Cause (read).**
- The basses' mean vol_db over 274-286 is +2.9 dB (series 1: -3.9). The c28 re-bow fills hold +4.2, +5.7 and +9.0 after 273.2, 276.05 and 282.2, and several are clamped at +9 to +10. They hold the ppp pedal at the level of the p note at 271. The role [274,282.5,2] adds 2 dB more.
- The Harp harmonics' mean vol_db over 274-277 is +1.8 (series 1 +4.9). The port lost series 1's +7 dB shape at 276-277.3, which went with the dropped 273/273.5 notes.

**Fix (`build/roles.json`).**
- Double basses: replace [274,282.5,2] with [273.25,286,-5,0.75]. The cut begins at the 273.229 re-bow and ramps in over 0.75 qn, so it is not a step under the sounding note (S3). Keep [282.25,291.5,-2.0,0.5].
- Harp harmonics: add [273.9,277.6,4]. The track is silent before 274.
- Simulated on the c28 stems: Cb -46.4 to -52.1 dB, harmonics -46.2 to -48.6 and on top at 274-275, Clarinet 1 3.9 dB over the Cb at 280 and 9-15 dB over it at 281-284, Vc 4 soli unchanged.
- After finding 1 is fixed, check that the re-bow fills no longer reach the +9 clamp. Refit them with a target that falls with the printed decrescendo of bar 82 (271-274) instead of holding the p level.

## 3. Bars 67-70: the 4-soli basses' E♭ pedal fell about 8 dB below series 1. The ppp timpani roll is now over it and does not play its decrescendo (measured)

**Where.** Double basses qn 220-238 (pp, "4 soli, sul A", tied through bar 70; no Cb hairpin), Timpani 226-237.5 (ppp roll "near the rim", decrescendo hairpin 232-237), under Horn 1's solo.

**What.**

| qn (2-qn means) | 226 | 228 | 230 | 232 | 234 | 236 |
|---|---|---|---|---|---|---|
| Cb, c28 | -51.0 | -55.6 | -54.9 | -55.8 | -55.8 | -52.8 |
| Cb, c26 | -46.4 | -47.6 | -47.0 | -47.4 | -46.7 | -46.7 |
| Timpani, c28 | -49.9 | -51.5 | -51.7 | -51.6 | -52.1 | -52.3 |
| Bassoon 1 (pp), c28 | | -49.7 | -44.9 | -43.8 | -46.4 | -45.5 |

- In c26 the pedal was 3-6 dB over the roll. In c28 it is 3-4 dB under it, against the brief's rule that a pp/ppp roll sits 3-5 dB under the quietest sustained string section (KIT §13).
- The basses sit 8-11 dB under the pp bassoons, which carry the same printed dynamic.
- The roll's printed decrescendo 232-237 falls 0.7 dB.

**Cause (read).**
- Cb mean vol_db over 226-238 is -2.9 (series 1 +4.8). That is SOLI_AS_META's -3 plus re-bow fills that hold -5.3 to -6.0 dB, the clamp, after 227.8, 230.4 and 233.0. Inferred: the fits followed the c27 render's fall into the upper strings' niente in bar 66, which the basses do not play.
- The timpani vol_db holds +9 to +10 dB from 227 to 237 (TIMP_ROLL_TRIM_DB ppp 17.6 at CC7 16). The hairpin has no target, so nothing falls.

**Fix.**
- `build/roles.json` Double basses: add [225.5,238,4,1], a 1 qn ramp inside the held note. Or set the hold values of the Cb re-bow fills 222.452-235.659 in `build/rebow_fills.json` to 0 to -1 dB.
- `build/score_config.py` `LEVEL_SHAPES["Timpani"]`: add [(226.0,0),(226.5,-2),(232.0,-2),(237.0,-6),(237.6,-6)]. These are slow ramps, so the hall tail is kept (S3). Leave CC7 as it is.
- Simulated: Cb -47.0 to -51.8, timpani -51.9 to -53.7 before the decrescendo, the roll 0-3 dB under the pedal and falling under it from 232.

## 4. Climax bars 61-62: Clarinet 1's held F5 is as loud as the Violins I tune (measured)

**Where.** Clarinet 1 (stem 06) at qn 204-210: F5 tied 4 qn, then F5 for 2 qn, an inner note doubled by Oboe 1. The melody is Violins I, D♭6-D♭6-F6-E6/A♭6, ff molto sostenuto.

**What.**

| qn | 206 | 207 | 208 | 209 |
|---|---|---|---|---|
| Clarinet 1 | -21.2 | -20.0 | -21.3 | -23.4 |
| Violins I | -22.4 | -20.8 | -19.9 | -23.2 |
| Flute 2 | | -22.9 | -22.0 | -22.9 |

- Violins II also measure -20.4 at 206, over Violins I. Over 206-209 the tune is the loudest stem in only one beat, and by at most 1.4 dB.
- Rimsky-Korsakov's ratio, already used as a target in this kit (KIT §13), puts a string section in forte about 3 dB over one woodwind. Series 1 reached a 3.2-3.5 dB melody margin over every single wind at both climaxes (c05).

**Cause (read).** Clarinet 1's vol_db is +6.6 to +7.6 dB from 204 to 208. That is the crescendo gain hpgain [200,204,7], held through `SOSTENUTO_SPANS` (204,212), with no role against it. Oboe 1, on the same F5, has [204,208,-3], and Clarinet 2 has [204,208,-2.5]. Meanwhile the Violins I re-bow fill at 205.949 holds -4.3 dB to about 208, so the tune dips just where the clarinet peaks.

**Fix (`build/roles.json`).**
- Clarinet 1: add [204,210,-4]. It begins at the ff arrival and ends at the 210 note onset.
- Flute 2: add [206,210,-2].
- Check the Violins I fill at 205.949. Its -4.3 hold was fitted on c27; a hold near -2 would give back half the dip.
- Simulated with the two roles: Clarinet 1 -24.0 at 207, about 3 dB under Violins I. The master changes by at most -1.0 dB (at qn 207), and bars 61-62 stay the loudest bars (simulated -11.4 against -13.5 at bars 79-80).

## 5. Bars 79-80: Bassoon 2, the celli's A♭3 and the cor anglais rise to the level of Violins I and Flute 1's B♭6 (measured)

**Where.** qn 262-268. Bassoon 2 holds D♭3 (262-265), the Violoncellos play A♭3 (265-267), the cor anglais plays A♭4 (266-268), and Oboe 1 plays 262-268.

**What.**
- Bassoon 2: -23.9/-23.6/-24.0 at 262-264 against Violins I -21.7/-23.6/-23.0. Level with the tune on a bass-line note doubled by Cb, contrabassoon and bass clarinet.
- Violoncellos: -20.5 at 265, 3.9 dB over Violins I and 3.6 over Flute 1. The same line measures -27.2 at 264 (B♭3) and -26.3 at 267 (B♭3), so the A♭3 stands 6-7 dB over its neighbours. KIT §13 records this pitch as hot at f/ff (c25: note trims -3/-4). The bar 61 A♭3 at 204 has a -3 trim; 265 has none.
- Cor anglais: -22.7 at 266, 2.7 dB over Violins I.
- Oboe 1: -24.4 at 266.

**Cause (read).**
- Bassoon 2's vol_db is +9.6 to +10.1. Series 1's role [262,268,4], written when the winds entered "cold" with no hairpin (KIT §13, c11-c12), now adds to v600's crescendo gain hpgain [261,262,7] (chained) and the bass-octave weight [261.5,269,3,1]. The D♭3 pitch trim of -5 is not enough.
- Oboe 1's [262,268,6] has the same origin.
- c28 lowered Flute 1 and the strings here but kept these wind roles.

**Fix.**
- `build/roles.json`: Bassoon 2 [262,268,4] -> [262,268,-1]; Oboe 1 [262,268,6] -> [262,268,4].
- `build/note_trims.json`: Violoncellos "265": -4; Cor anglais "266": -3.
- Simulated: Violins I and Flute 1 are the top two stems at 262-266. Bassoon 2 drops out of the top six, the celli sit at 0.1 dB under Violins I at 265, and the cor anglais 0.3 under at 266. Bars 79-80 fall 0.2-1.2 dB, which widens the climax lead (delivered 1.2 LU in c28). Recheck the delivered figures (LRA, span, limiter).

## 6. Bars 41-44: the pp celli are within 1-2 dB of the cor anglais solo (measured levels; importance inferred)

**Where.** Violoncellos (stem 25) and Cor anglais (stem 05), qn 124-138. Cor anglais: "solo, dolce cantabile" p < mp. Celli: pp < p > pp, "senza sord., ord.".

**What.** Cor anglais against celli per 2 qn: 126 -36.2/-38.1, 130 -37.5/-42.7, 136 -39.9/-40.8, 138 -47.0/-45.3. The solo's margin over the whole accompaniment is -0.8 to +2.3 dB, against +2.7 to +5.2 for Flute 1's solo in bars 37-40. A printed pp line under a p/mp solo usually sits 4-6 dB under it (KIT §13: accompaniment at a softer printed dynamic still needs 3-7 dB).

**Fix (`build/roles.json`).** Violoncellos: add [124,138,-3,1], with a 1 qn ramp in and out. Keep the bar 45 entry (139, "sul D", with Oboe 1) as it is.

## Checks for items 8, 9 and S1-S3 in this lens

- Item 8: finding 1. The c26-fitted series 1 profiles are now the largest source of periodic level movement in the render.
- Item 9: no brass accent is a balance outlier. Trombone 1's quotation is the loudest stem through bars 63-64 (-20.3 to -25.1), 9-11 dB over Violins I. That is printed (ff marcato over a p/pp tutti) and was kept by critic B in c28.
- Climax checks asked for in this lens:
  - Bars 61-64: the timpani roll is under the strings (-30 to -37 at 204-211, the f stroke at 203 -25.7 against the strings' -20/-21). Trombone 2, bass trombone and tuba (printed f) sit 1-5 dB under Violins I and do not cover.
  - Bars 79-82: there is no low brass, and the timpani rolls are out of the top seven stems.
  - The basses carry the master's 40-100 Hz at the climax, with that band 16 dB under the master's K level at 207, which is not boomy.
- S3: every change above is a slow ramp, starts at a note onset, or is a hold value. None is a fast fall in the volume envelope under a sounding note.
- Divisi and soli tracks against the sections (measured):
  - Violas div is within ±2 dB of the Violas from 286 (c28's -4 worked).
  - Violins II div is 1-2 dB under the Violins II in bars 37-40.
  - The Cb 4 soli are 6-9 dB under the celli in the final chord, as c28 intended.
  - The Vc 4 soli in bars 83-86 are -48 to -58, under the Cb tutti: finding 2.

**Do not touch:**
- Horn 1's solo margins in bars 7-14 (+2.2 to +5.8 dB over the accompaniment sum, 5-11 dB over each stem).
- The Violin I solo in bars 17-22 and Oboe 1 in bars 15-22 and 45-47 (5-8 dB over every single stem).
- The bass clarinet in bars 31-36 and Flute 1 in bars 37-40.
- Clarinet 1's coda solo once the basses are lowered.
- Trombone 1's quotation level.
- The climax order (bars 61-62 louder than 79-80).
- The Violas div coda cut and the basses' +5 in the last four beats.
- The low-end EQ set (Cb bell2 80 Hz, 160 Hz +4.5, climax loud_eq).
