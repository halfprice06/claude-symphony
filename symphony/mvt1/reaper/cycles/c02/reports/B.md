# Cycle 2, critic B: balance and levels (render c01)

Method. I measured K-weighted levels (the BS.1770 filter applied per FFT frame, 25 ms hop) on every stem and on the master of `cycles/c01/render/`, which is the stem-fixed version.

- Note bodies run from onset +0.08 s to min(note end, +1.0 s). I compared them at the same score onset and the same printed dynamic (`parts.json` `dyn_curve`).
- "A minus B" is the median, over A's note bodies, of A's level minus B's level in the same window.
- Residuals are note level minus the track's volume envelope (`build_reaper.vol_points`), fitted against CC11 per track.
- Delivery effects come from an audio simulation: the c01 master plus each changed stem multiplied by its role envelope (0.5 qn ramps), then `tools/deliver_master.py` into my scratch folder. Unchanged, this reproduces c01 exactly: 16.0 LU, span 20.4 dB, limiter 1.9 dB.
- The balance targets are the ones mockup-kit LEARNINGS section 13 found to work: Rimsky-Korsakov's resonance ratios, a melody 3-5 dB over the accompaniment, and 4-6 dB melody margins at climaxes.

Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c02-B/` (`pair.py`, `samedyn.py`, `steps.py`, `hot.py`, `pitchmed.py`, `artlvl.py`, `sim2.py` with `sets.json`, `stpeaks.py`, `acc.py`, `loop.py`).

One incident. A first attempt imported `tools/build_reaper.py` as a module, and its top-level code tried to send a tempo job through `rpr.py`. It failed with "bridge not running" and wrote only a stub Lua file into my scratch folder, which I deleted. Nothing reached REAPER, and nothing outside scratch was written. Every later call exec'd only the part of the file before `ENV_LUA`, as `stem_fix.py` does.

**Overall.** `roles.json` has four rows and `pitch_trims.json` is empty, so this movement has no accompaniment cuts and no pitch evening yet. Most of what follows comes from that.

## 1. Sustained brass harmony and pedals cover the melody in the ff tuttis (bars 117-120, 131-134, 140-142, 158-161)

Where and what (measured; melody per the score pages):

- **Bars 117-120 (qn 464-480).** The theme motif is in Violins I/II, flutes and oboes, ff. Trombone 1 holds the a2 line in long notes; Trombone 2's unison is dropped onto it. Trombone 1 is the loudest stem in every bar: -21.4 dB against Violins I -24.0. Over the Violins I note bodies, Violins I is -3.0 dB under Trombone 1 and +0.4 dB over the bass trombone. Trombone 1's envelope reaches +6 to +9 dB there: ff trim 3, the a2 +3, the hairpin hold and the long-note CC11 swell to 116-118.
- **Bars 131-134 (qn 520-536).** The recapitulation theme is in Trombones a2 (f), celli (ff), clarinets and bassoons. The bass trombone's ff whole-note pedal is the loudest or second-loudest stem in all four bars (-25.2 to -26.7 dB). The theme sits under it: Trombone 1 is 5.1 dB under it and the celli 4.2 dB under. The tuba is 1.3 dB over the theme trombone.
- **Bars 140-142 (qn 556-568).** The melody is in Fl/Ob/Cl and Violins I/II. The trumpets play harmony half and whole notes, and Trumpets 1/2 are level with the Violins I melody (Violins I +0.7 / +1.6 dB over them). This is c01's open item "trumpets 4-5 dB over the trombones in bars 140-143". By the score that is harmony, not theme, so it is wrong here. In bars 167-170 the trumpets carry the ff theme, so being on top is right there.
- **Bars 158-161, the main climax (qn 628-644).** The melody is in Violins I/II, flutes, Horn 1 (158-159), Trumpet 1 and celli. Violins I is 1.6 dB under Trombone 1's held harmony. Trumpet 1, on the melody, is 1.9 dB under Trombone 1 and level with the bass trombone and Horn 3 (harmony). The melody margins are -2 to +2 dB, against the 4-6 dB that worked in movement II.

These are held notes on the a2 / ff layer with no accompaniment cut. Section 13 of the kit says accompaniment at the same printed dynamic needs a 3-7 dB cut (measured cause; the fix size is inferred).

Fix in `build/roles.json`. Each row is level only, so it can be applied with `stem_fix.py`.

- Trombone 1: [464, 480, -5], [628, 644, -3]
- Trombone 2: [628, 644, -3]
- Bass trombone: [464, 480, -3], [520, 536, -6], [628, 644, -3]
- Tuba: [520, 536, -3], [628, 644, -2]
- Trumpets 1, 2 and 3: [556, 568, -3]; Trumpet 3 also [628, 644, -3]
- Melody lift at the climax: Violins I, Violins II, Flute 1, Flute 2, Horn 1 and Trumpet 1, [628, 644, +1.5] each
- Violins I and II: [520, 536, -2] (their countermelody is 4.4-5.4 dB over the theme)

Expected margins, from the measured gaps:

| Passage | Pair | Before | After |
|---|---|---|---|
| Bars 117-120 | Violins I over Trombone 1 | -3.0 | +2.0 |
| Bars 131-134 | Theme trombone over bass trombone | -5.1 | +0.9 |
| Bars 140-142 | Violins I over Trumpet 1 | +0.7 | +3.7 |
| Bar 160 | Violins I over Trombone 1 | -1.6 | +2.9 |

Check after the render that the trombone a2 line in bars 117-120 is still the second voice (no more than 3 dB under the violins).

## 2. String accompaniment and harp over the melody: celli in the first theme, Violins II chords, harp

Where and what (measured):

- **Bars 15-18 (qn 56-72), the first entry of the Allegro theme.** Violins I (f) are 3.7 dB under the celli's f half-note bass line over the theme's 19 note bodies. Per bar, the celli measure -30.1 / -29.3 / -28.9 dB against Violins I -35.4 / -35.8 / -34.8.
  - The celli play these notes on Leg BC MAX. At f that row measures 4.5 dB louder than Leg Slur MAX at the same CC11 and envelope: celli f, Leg BC median -31.6 dB (n=43) against Leg Slur -36.1 dB (n=22).
  - These cello notes have residuals of +6.6 to +6.9 dB.
- **Bars 27-32 (qn 104-128).** The ff theme in Violins I is only +0.6 dB over the celli's ff half notes. The celli are the loudest stem in bars 25, 26, 29, 31 and 32.
- **Bars 111-116 (qn 440-464).** Violins II's 2-note accompaniment chords (tremolo in bar 114) are 1.2 dB over the Violins I melody. Violins II is the loudest stem in bars 113-114.
  - The Tremolo and Sus MAX chord rows measure 7-12 dB hotter than the legato rows at the same CC11 and envelope, after the 3 dB that two notes add. For Violins II at ff: tremolo chords -23.8 dB against Leg BC singles -36.4 dB.
  - The divisi cut in `score_to_parts.py` (-10 log k, tremolo -3) compensates only for the stacking (inferred).
- **Bars 167-170 (qn 664-680).** The ff theme in the violas is 8.1 dB under Violins II's f divisi chords and 4.8 dB under Violins I's. Horn 1's half of the theme is 4.2 dB under Violins II. Trumpet 1 carries the theme alone, level with Violins II (-0.8 dB).
- **Bars 56-66 (qn 232-268).** The harp's mf arpeggios are only 2.0 dB under the f violin melody, and the harp is the loudest stem in bars 61 and 66 (-31.7, -32.8 dB). Harp mf median -34.0 dB, against strings at mf -37 to -39 dB.

Fix in `build/roles.json`:

- Violoncellos: [56, 72, -5], [104, 128, -3]
- Violins I: [56, 72, +2] (theme), [664, 676, -3]
- Violins II: [440, 464, -4], [664, 680, -4], [676, 680, -3] (the bar-170 fermata chord, the loudest stem of bar 170)
- Violas: [664, 680, +3]
- Horn 1: [664, 680, +2]
- Harp: [232, 268, -3], released over 2 qn into bar 62

Expected margins (simulated as level-only changes):

| Passage | Melody minus accompaniment | Before | After |
|---|---|---|---|
| Bars 15-18 | Violins I over celli | -3.7 | +3.3 |
| Bars 27-32 | Violins I over celli | +0.6 | +3.6 |
| Bars 111-116 | Violins I over Violins II | -1.2 | +2.8 |
| Bars 167-170 | Violas against Violins II | -8.1 | -1.1 |
| Bars 167-170 | Horn 1 against Violins II | -4.2 | -0.2 |
| Bars 56-66 | Violins I over harp | +2.0 | +5.0 |

The general cause, accompaniment rows (Leg BC at f, Tremolo and Sus chords at f/ff) hotter than the legato melody rows, is measured. Treating it with a per-articulation trim, a new `mix.json` key read in `vol_points`, is my inference; for now the roles are the safer fix.

## 3. The climax order is wrong: the bar-122 violin chord is the loudest moment, and the ff bar 169 matches the main fff climax

Where and what (measured, delivered short-term loudness):

| Bar | Short-term loudness | Note |
|---|---|---|
| 122 (qn 486) | -9.9 LUFS | the loudest moment |
| 160 (qn 636) | -11.3 LUFS | the main climax |
| 169 (qn 676) | -11.5 LUFS | printed ff, not fff |

**Bar 122.** The violins make the bar-122 peak.

- Violins I hold a single Ab6 at fff with a +9.5 to +10.9 dB envelope (gain 5, ff trim 1.5, the crescendo hold) and CC11 127.
- Violins I measure -16.5 dB and Violins II -16.8 dB. That is 8 dB over every brass stem (Trumpet 1 -25.1, Trombone 2 -25.0, horns -28 to -31) and 4.7 dB over the tam-tam's fff stroke (-21.2 dB).
- A fff tutti chord with the brass 8 dB under the violins does not sound like this score (inferred).

**Bar 169.** Bar 169 is set by Trumpet 1's F5 (qn 673).

- That note measures -14.4 dB in its half beat, 7 dB over the trumpet's other theme notes. Trumpet 1 F5 has a residual of +8.2 dB (n=5).
- It is also the melody note at the climax: qn 633 and 640 (bars 159 and 161) have residuals of +8.9 and +8.2 dB.

Fix:

- `roles.json`: Violins I [484, 496, -5], Violins II [484, 496, -5].
- `pitch_trims.json`: "Trumpet 1": {"77": -6, "_all_arts": true}.
- Keep the +1.5 dB melody lift at qn 628-644 from finding 1.

Simulated together with findings 1, 2 and 6:

| | c01 | Simulated |
|---|---|---|
| Delivered LRA | 16.0 LU | 15.8 LU |
| p10-to-max span | 20.4 dB | 19.1 dB (target 16-19) |
| Limiter | 1.9 dB | 2.0 dB |
| Master peak | 1.177 | 1.096 |
| Bar 122 | -9.9 | -10.7 |
| Bar 160 | -11.3 | -10.9 |
| Bar 169 | -11.5 | -11.7 |

Bars 122 and 160 are then the two loudest moments and level with each other, both printed fff, with bar 169 below them.

To make bar 160 clearly the top, as the brief calls it the main climax, add +1 dB on all tracks at [632, 644] (`"_all"`), then re-check the limiter.

## 4. Hot pitches stick out at every dynamic, including the subito p in bar 84 and the pp entry in bar 175 (pitch_trims.json is empty)

Where and what (measured). Each figure is the per-pitch median residual against the track's CC11 fit, single notes of 0.6 qn or longer.

| Track | Pitch | Residual | Where it matters |
|---|---|---|---|
| Violoncellos | G2 (43) | +6.4 dB, n=15 | Bar 84 sub. p +13.6 dB: the subito-p note is 5.4 dB over the bar after it. Bar 175 pp +13.0 dB: the pp cello entry is 6.8 dB over the end of the mp solo before it and 9-11 dB over the trombones' pp dolce chorale it accompanies. The c01 opening-pickup bloom was the same pitch. |
| Violoncellos | Eb3 (51) | +6.5 dB, n=13 | |
| Trumpet 1 | F5 (77) | +8.2 dB | See finding 3 |
| Clarinet 1 | G5 (79) | +7.5 dB | |
| Clarinet 1 | Ab5 (80) | +5.0 dB | |
| Clarinet 1 | Ab4 (68) | -6.9 dB | |
| Flute 1 | G6 (91) | +8.4 dB | |
| Flute 1 | D5 (74) | -6.3 dB | |
| Horn 1 | C5 (72) | +7.0 dB | |
| Oboe 1 | E5 (76) | +6.5 dB | |
| Oboe 1 | C5 (72) | -4.7 dB | |
| Bassoon 1 | Db4 (61) | +6.2 dB | |
| Bassoon 1 | F#3 (54) | +6.1 dB | |

The same patches showed the same deviations in movement II: Clarinet 1 G5 -6 / Ab4 +6, Flute 1 G6 -4 (`symphony/mvt2/reaper/build/pitch_trims.json`). That supports treating them as properties of the samples.

Fix in `build/pitch_trims.json`, in movement II's format:

```
"Violoncellos": {"43": -5, "51": -4, "_all_arts": true, "_skip_onsets": [3.0]}
"Trumpet 1": {"77": -6, "_all_arts": true}
"Clarinet 1": {"79": -6, "68": 6, "80": -3, "_all_arts_pitches": [68]}
"Flute 1": {"91": -5, "74": 4, "_all_arts_pitches": [91]}
"Horn 1": {"72": -5, "_all_arts": true}
"Oboe 1": {"76": -5, "72": 3}
"Bassoon 1": {"61": -5, "54": -5}
```

- The Violoncellos `_skip_onsets` [3.0] avoids stacking on the existing `note_trims` -8 at qn 3; re-measure that pickup.
- Apply the Clarinet 1 values to Clarinet 2 as well if it shows the same deviation. That is inferred: Clarinet 2 has too few long notes to measure.
- After the render, check each trimmed pitch at each dynamic it appears at (kit section 13).

## 5. Dynamic mapping: Flute 1 is flat from pp to mf and 6 dB under the other woodwinds at mf

Where and what (measured):

- Flute 1's note medians are pp -44.8, p -44.1, mp -44.8, mf -44.4, then f -36.8 dB.
- At the same onsets and the same printed mf, Flute 1 is 6.0 dB under Oboe 1, 2.4 under Clarinet 1, 4.7 under Bassoon 1 and 8.4 under Violins I. At f and ff it is level with or over the other woodwinds.
- The audible case is bars 64-65 (qn 252-258): the "1." flute doubles the Violins I f melody at mf and is 14-15 dB under it (Flute 1 -44.9 / -44.4 dB against -30.2 / -33.3 dB). That is a doubling that cannot be heard.

The cause (measured from the data) is the soft-trim taper in `build_reaper.vol_points`. The trim falls linearly from the p anchor (+5 at CC 46) to the f anchor (CC 88). Flute's f trim is -4, so the trim is +2.4 dB at mp and -0.6 dB at mf, and it cancels most of CC11's growth from p to mf.

The same taper flattens the middle dynamics in every family that has a negative f trim. Pitch-matched medians across tracks:

| Step | Strings | Woodwinds | Brass |
|---|---|---|---|
| p > mp | 1.1 dB | 0.1 dB | |
| mp > mf | 1.6 dB | 1.8 dB | |
| mf > f | 2.0 dB | 1.7 dB | 2.5 dB |

A printed mp, mf or f differs little in level.

Fix:

- `tools/build_reaper.py` `vol_points`: accept optional "mp" (CC 58) and "mf" (CC 72) anchors in `soft_trim_db` (global or per track) and insert them into `tbl`.
- `build/mix.json`: Flute 1 and Flute 2 `soft_trim_db` {"ppp": 7, "pp": 7, "p": 5, "mf": 2.5}. This gives +3.1 dB at mf and +1.4 dB at mp. The expected Flute 1 mf median is about -41 dB: 1-2 dB under the oboe and level with the clarinet.
- If the tool change is not wanted, Flute 1/2 `dyn_trim_db` f -4 -> -2 gives +1.9 dB at mf. It also raises f by 2 dB, where the flute is already level with Oboe 1.

Do not lower the global soft trims to restore the steps. The delivered span is still over its target (finding 3).

## 6. Percussion and timpani at the soft end: the pp tam-tam cannot be heard, and the final ppp timpani roll is 8 dB under

Where and what (measured):

**Tam-tam pp, soft stick (qn 696, bar 175).**

- It measures -45.1 dB in its first beat and -51.9 dB over qn 700-708, against a master of -32.7 / -34.3 dB: 12-18 dB under.
- In 100-300 Hz it is 13-18 dB under, and it has nothing above 2 kHz (-103 dB).
- c01's velocity 60 did not bring it into the texture. The percussion tracks are excluded from the +7 dB pp soft trim.
- I infer that a pp tam-tam colouring the dolce trombone chorale should be about 8-10 dB under the master.

**Timpani ppp roll (qn 720-728, bars 181-182).**

- It measures -59.8 dB against the double basses at -52.0 dB: 7.8 dB under. The target that worked is 3-5 dB under the quietest sustained string section (kit section 13).
- The other soft rolls meet it: bar 1 is 2 dB under the basses, bar 76 4.4 dB under the violas, bar 13 3.8 dB under the celli.

Fix in `build/roles.json`:

- Tam-tam: [696, 712, +8]. Simulated: the master and delivery do not move.
- Timpani: [720, 728, +4], ending with the final fade rather than at a note start (kit section 13, roles ending on a held note).

The trumpets against the rest are fine at soft levels (measured). At pp, Trumpets 1-3 are -41.6 to -45.1 dB against the horns' -41.5 to -44.5 dB; at mp, -37 to -42 against -39 to -41.5. At f they are 3 dB under the trombones and 1 dB over the horns; at ff 2 dB under the trombones and 3 dB over the horns, which matches Rimsky's ratios. Do not change the trumpet trims; use the roles above.

## Checks for Dan's two listening items (no finding)

**Loop pulse** (measured), 100-300 Hz level and spectral centroid autocorrelation at 3.95 s:

| Passage | Stem | Level | Centroid |
|---|---|---|---|
| Final chord, qn 712-728 | Master | +0.15 | +0.09 |
| Final chord, qn 712-728 | Basses | +0.28 | |
| Final chord, qn 712-728 | Other string stems | -0.16 to +0.15 | |
| Tam-tam ring, qn 484-500 | Master | -0.46 | -0.26 |
| Coda chorale, qn 696-712 | Celli, Trombone 1 | at most +0.20 | at most +0.20 |

All are under movement II's 0.39-0.63 problem level.

**Accents** (measured), 2-5 kHz in the first 80 ms minus the body, accented notes, median (p90):

| Track | Median (p90) |
|---|---|
| Trumpet 1 | +0.5 (+2.5) dB |
| Trumpet 2 | +0.1 dB |
| Trumpet 3 | -2.8 dB |
| Trombone 1 | -2.5 dB |
| Bass trombone | -0.9 dB |
| Horn 1 | -0.5 (+3.6) dB |

None comes near the 7-13 dB burst Dan heard, so the c01 trumpet trims of +7/+8 did not bring back a harsh attack.

Do not touch: the trumpet `dyn_trim_db` (7/8, Trumpet 3 8/11), which is consistent with the horns and trombones at every dynamic. The global `soft_trim_db` 7/7/5. The basses' level and EQ: no boom; 20-100 Hz share -15.4 dB and 100-250 Hz share -9.1 dB, if anything slightly light, so do not raise them. The timpani settle and the opening and bar-76 roles (2-4.4 dB under the quietest strings). The crash level at qn 636 (2-5 kHz 6 dB under the master in its first beat). Brass and woodwind GENTLE_ACCENT. The c01 subito-p handling (fix the bar-84 cello through the G2 pitch trim, not the subito rule). The coda cor anglais role (the cello solo is now 1.3 dB over the rest, the cor anglais 3-4 dB under the cello).
