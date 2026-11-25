# Cycle 17, critic B: balance and levels (render c16)

## Method

All numbers are from the stem-fixed c16 render (`cycles/c16/render/`, 33 stems) and the build it was measured with (`build/parts.json` 19:51, `mix.json`, `roles.json`, `accent_fits.json`, `score_config.py`). Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c17-B/` (the c16-B set re-pointed at c16, plus `top6.py` per-beat ranking with short names, `rank.py` loudest stem per beat by printed dynamic, `cbloud.py`, `sim131.py`, `simfug.py`, `sim121.py`). Level means K-weighted power in 10 ms hops; "re master" is stem minus master over the same window; "melody top minus accompaniment top" is the loudest melody stem minus the loudest other sounding stem. Simulations scale the c16 stems by the proposed dB change and rebuild the master as their sum. Melody and accompaniment were assigned from the score pages (pp. 3, 5-18 at 90 dpi).

## What holds (measured)

- Family mapping by printed dynamic, as heard (median note bodies): p winds -41.6, brass -43.9, strings -42.5 dB; f -37.3 / -32.8 / -33.4; ff -32.2 / -28.2 / -26.6. Same-dynamic held-beat comparisons: horn minus woodwind p -1.6, mp -1.9, f +1.2; trumpet minus horn f +3.6, ff +3.0; low brass minus horn f +3.4, ff +2.8; trumpet minus woodwind f +5.7. These match Rimsky-Korsakov's ratios (in p one wind = one string group; in f a horn = two woodwinds, a trumpet or trombone = two horns).
- The new trumpet tracks: the c16 B #6 roles worked. Trumpets 1/2/3 re master at qn 112 -15.7/-15.3/-14.3, 552 -12.3/-12.2/-11.8, 484 -14.3/-13.8/-14.7 (the inversions are gone). Trumpet 1 leads the coda theme (bars 167-169) at -6.6..-7.7, 2.3 dB over Horns a2, with the violas under them. Trumpets play soft only in bars 113-115 (pp cresc.), where they sit 15-22 dB under the master.
- Strings mf to f, pitch-matched, is now +2.6 dB (31 pitches; c15 +1.1). The c16 B #5 pass range was +2.5..+4. f to ff is +5.1.
- Percussion. The tam-tam fff (qn 484) is the loudest stem for about 3 s (-6.9..-10.1 re master) with no melody under it. The pp soft-stick stroke at 175 is a 60-100 Hz hum (-1.4..-5 re master in that band, -44..-48 in 2-5 kHz), which suits a pp tam-tam. Crash and suspended-cymbal levels and timing are as in c16.
- Dan's checks:
  - Accents, 2-5 kHz in the first 80 ms minus the body: brass median -7.1 dB (2 of 133 over +3), winds -6.2 (8 of 220), strings -3.5 (9 of 186). The worst cases (Va/Bn1/Hn3 at qn 536 +16/+7.4/+6.7) are the known artefact of the bar-134 ff tail falling inside the attack window of bar 135's mf downbeat.
  - Loop pulsing: 8 unsplit notes last 6 s or more. Bass clarinet 11 (100-300 Hz / centroid autocorrelation 0.81/0.75) carries printed hairpins. Horn 4 289 (0.58/0.55, -9.7 re master) shows one +3 dB rise from +2.2 to +4.5 s and a 4 dB fall after it, which is borderline (inferred). The master windows are 0.06 or less except 160-176 (+0.44, the printed ff > p decrescendo trend, as in c16).

## 1. Recapitulation, bars 131-134: the trombones, printed f, are 6-11 dB over the ff celli and bassoons that carry the same theme, and over the violins (measured)

**Where.** qn 520.5-536. Trombone 1 holds the merged a2 line; Trombone 2 has no notes (29 unison notes dropped).

**Score (p. 12).** The first theme's head is in Bassoons a2 ff, Trombones a2 f and Celli ff, with the high line in Flutes, Oboes and Violins I/II ff, Cb ff eighths, and the tuba and bass trombone ff. The composer marks the trombones one level under everyone else.

**Evidence.**
- At the theme-head accents Trombone 1 is the loudest stem, by up to 7.4 dB. Trombone 1 re master: 131.25 -3.7 (next V1 -11.1), 131.5 -7.7, 131.75 -6.6, 133.25 -6.4, 133.5 -7.6, 133.75 -7.5.
- Absolute levels at 521 (+0.05..0.35 s): Trombone 1 -17.5, celli -26.3, Violins I -25.5, Bassoon 1 -31.3. Over the body after the accent (521.6-522.4): -19.9 / -30.4 / -24.3 / -31.6.
- Per half beat, Trombone 1 minus celli is +6.4/+11.4/+6.7/+6.6/+8.2 over 521-523.5, and +7.6 at 529.5.
- The accent measure puts Trombone 1 521/529 at +8.3/+8.6 dB over the unaccented notes around them, the two largest brass values in the movement (target 2-4).
- **Cause** (`build/roles.json`, `build/accent_fits.json`):
  - Trombone 1 `[520, 536, 2.5]`.
  - Accent fits 521 `[5.0, 1.01]` and 529 `[5.0, 3.0]`. Both swells sit at the fit's 5 dB cap.
  - The volume envelope reaches +11.5 dB at 521.08-521.75.
  - The trombone's own f is already a heavier layer than the celli's ff.

**Fix.**
- `build/roles.json`: Trombone 1 `[520, 536, 2.5]` to `[520, 536, -0.5]`. Delete the inert Trombone 2 row, or leave it.
- `build/accent_fits.json`: Trombone 1 "521" to `[3.0, -1.5]` and "529" to `[3.0, 0.0]`.
- Leave these two accents out of the next refit (or re-enter these values after it). The fit compares each accent with its own slur neighbours and will push the swell back to the cap; the trombone's level against the other sections is not part of the fit.
- Level only, so `stem_fix.py` can apply it.

**Estimated** (stem simulation, role only; the fit change takes another 1.5-3 dB off the accent bodies):
- Trombone 1 minus celli over 521-523.5: +6..+11 to about +1..+6.
- Trombone 1 minus Violins I: -2..+9 to about -5..+3.
- The master falls 0.3 dB on average and 1.0-1.7 dB at the two accents.
- With the fit change the accents end about 0..+4 dB over the celli: brass weight inside a ff string-and-bassoon theme, not a trombone solo (inferred).

## 2. Fugato, bars 91-93: the third subject entry (cor anglais + Violins II, f) is 3-9 dB under the celli and basses (measured)

**Where.** qn 360.5-372, p. 8.

**Score.** The entries are celli mf (bar 85), Bassoon 1 + violas mf (bar 88), then cor anglais f with an accent plus Violins II f (bar 91), then Flute 1 / Clarinet 1 / Violins I f (bar 94). Under entry 3: celli f (long notes), basses f half notes, violas and Bassoon 1 f counterpoint, BCl / Bn2 f held.

**Evidence.**
- Averaged over 360-372, re master: celli -6.3, basses -6.5, Violins II -8.4, violas -8.5, Bassoon 1 -10.9, BCl -11.1, cor anglais -12.0.
- The basses are the loudest stem at 91.5, 92.5, 93.0 and 93.5 (-4.2..-5.7 re master).
- Subject top minus accompaniment top, per half beat: median -3.2 dB, worst -9.0 (363), -8.2 (364), -7.0 (365.5), -6.7 (370).
- The other entries come through: entry 1 celli +2.9 dB (melody group minus the rest), entry 2 +1.8, entry 4 Violins I at -4.8 re master and on top.
- **Cause.** `roles.json` has fugato roles for entries 1-2 (celli, basses, violas, Bassoon 1 to 358) and none for entry 3. The basses' c16 f/ff trims (2.5/4) add 1.5 dB here.
  - Over the movement, beats where the basses are the loudest stem went from 6 to 10 at f and from 2 to 7 at ff, c15 to c16 (`cbloud.py`). Cases include bar 27 beats 2-3 (+0.6/+1.4 over the Violins I theme) and 131.0/132.0.
  - Basses re master moved -12.4 to -11.5 dB at f and -14.4 to -12.1 at ff.

**Fix** (`build/roles.json`, level only):
- Cor anglais `[360.25, 372, 4, 0.5]`.
- Violins II `[360.25, 372, 3, 0.5]`.
- Violoncellos `[360, 372, -2, 0.5]` (on top of the existing `[360, 408, -3]`).
- Double basses `[358, 372, -3, 0.5]`.
- Violas `[360, 372, -2, 0.5]`.
- Leave the basses' global f/ff trims, which keep the tutti's 100-160 Hz (finding "What holds"). Where the basses top a theme, add short roles: bar 27 Double basses `[104.5, 108, -2, 0.25]`.

**Simulated.**
- Subject top minus accompaniment top: median -3.2 to +1.0 dB. The remaining dips are -3.0 (363) and -5.2 (364), on the subject's turn eighths.
- Master +0.2 dB median.

## 3. Bars 121 and 124-125: a role that ends on a held note lifts the trombones 5.7 dB at the start of the allargando, and the brass and celli cover the melody as the fff decays (measured)

**Bar 121** (qn 480-484, p. 11). The melody is the allargando dotted figure in Flutes, Oboe 1, Clarinet 1, Violins I (8va) and Violins II, under a printed crescendo to the fff. Trombones and bass trombone hold tied notes (479-483.6).

- `roles.json` Trombone 1 `[464, 480, -5]` and Bass trombone `[464, 480, -3]` end at 480 with the default 0.5 qn ramp.
- The trombone's envelope therefore jumps from -1.2 to +4.5 dB between 480 and 480.5, on a tied note. This is the kit's "role that ends on a held note" case, here as a rise.
- Trombone 1 becomes the loudest stem: -7.7 / -5.9 / -5.9 re master at 480 / 480.5 / 481, against the melody's top stem at -10.2 / -10.3 / -8.7.
- From 482 the tuba (the c16 letter-G lift, +4 at 483.5) takes over at -8.0..-9.0.
- Melody top minus accompaniment top: median -1.9 dB, worst -4.4 at 480.5.

**Bar 124** (qn 492-496, p. 11). The only moving line is Violins I (loco) with Flute 1 and Oboe 1 ("1."), all under a printed decrescendo, over the brass and celli fff > chord.

- The brass roles `[484, 492.5, +2.5/+2, 1]` and the celli `[484, 492, -3, 1]` both end at 492.5. From there, bass trombone, Trombone 1 and the celli (-7.9..-10.8 re master) stand over the melody's top stem (-11.5..-14.6).
- Melody top minus accompaniment top: median -2.5 dB, worst -3.8 (492.5).
- At bar 125 Bassoon 2 enters on a held G2 at CC 108 (the long fff > p) and is the loudest stem at 125.0-125.5 (-7.1..-9.2), over the Violins I p melody at 125.25 (-10.4).

**Fix** (`build/roles.json`, level only):
- Bar 121: Trombone 1 `[464, 480, -5]` to `[464, 484, -5, 4]`, and Bass trombone `[464, 480, -3]` to `[464, 484, -3, 4]`. With the end ramp the cut opens linearly through the crescendo and is 0 at the fff.
- Bar 124: new rows `[492.5, 496.5, -3.5, 1.5]` on Trombone 1, Trombone 2, Bass trombone and Tuba. Violoncellos `[492.5, 496.5, -3, 1.5]`. Violins I, Oboe 1 and Flute 1 `[492, 496.5, 2.5, 0.5]`.
- Bar 125: Bassoon 2 `[496, 500, -3, 1]`.

**Simulated.**
- Bar 121: melody top minus accompaniment top median -1.9 to -0.3 dB (480.5: -4.4 to -0.5). Master -0.8..-1.05 dB over 480-481.5 and unchanged from 483. The bar-121 crescendo grows by about 1 dB more inside the bar; the fff step at 484 is unchanged.
- Bar 124: median -2.5 to +1.4 dB (492.5: -3.8 to +1.2). Master -0.16 dB.

## 4. Woodwinds: mf to f is still flat (+0.7 dB pitch-matched), because every wind envelope falls from mf to f (measured; the size of the fix is inferred)

**Evidence.**
- Pitch-matched mf to f, as heard: winds +0.7 dB over 18 pitches (Bassoon 1 +0.4 over 8, Clarinet 1 +1.2, Bassoon 2 +1.4). With roles removed: +2.1. Strings are +2.6 / +4.1 and brass +7.4 / +4.1.
- The wind family median ladder as heard is p -41.6, mp -40.7, mf -38.7, f -37.3, ff -32.2: 4.3 dB from p to f, against strings 9.1 and brass 11.1.
- Gain + trim (dB) at p / mf / f / ff, from `mix.json`:

  | Track | p | mf | f | ff |
  |---|---|---|---|---|
  | Oboes | -0.3 | -2.2 | -3.3 | +0.7 |
  | Bassoon 1 | +5.0 | +1.6 | -0.5 | +0.5 |
  | Bassoon 2 | +6.0 | +2.3 | 0.0 | +1.0 |
  | Bass clarinet | +6.0 | +2.0 | -0.5 | +1.0 |
  | Cor anglais | +4.0 | +1.5 | 0.0 | +2.0 |
  | Flutes | +3.7 | +1.2 | -5.3 | -2.3 |

  The f anchor dips under both mf and ff, the same pattern c16 B #5 fixed on the strings.
- The clarinets' f trims (-4.2/-3.8) are justified by their +9.5 dB raw jump at the mf/f layer change (c16 B).

**Fix** (`build/mix.json`; level only; add mf anchors at the current values so that mf does not move):

| Track | `dyn_trim_db` f | `soft_trim_db` |
|---|---|---|
| Oboe 1/2 | 2 to 3.5 | add `{"ppp": 7, "pp": 7, "p": 5, "mf": 3.1}` (the global values plus the current mf) |
| Bassoon 1 | 1.5 to 3.5 | add `"mf": 3.6` |
| Bassoon 2 | 2 to 4.0 | add `"mf": 4.3` |
| Bass clarinet | -1.5 to 0.5 | add `"mf": 1.0` |
| Cor anglais | 1 to 2.5 | `{"ppp": 7, "pp": 7, "p": 5, "mf": 2.5}` |

- Leave flutes and clarinets (no pitch-matched mf/f evidence; layer jumps).
- Re-run `steps.py`. Pass: wind mf to f +2..+4, f to ff at least +4, winds at f still 1.5-3 dB under a string section (RK), no wind accompaniment as loudest stem in an f tutti.
- Expected: wind f passages +1.5-2 dB, mf unchanged, delivery span within 0.2 dB (inferred, as in c04 when mf/f moved together).

## 5. Soft timpani rolls sit over the quietest sustained string section (measured, smaller)

**Evidence** (roll level, median per passage):

| Bars (qn) | Printed | Re master | Re quietest held string | Re loudest string |
|---|---|---|---|---|
| 43-44 (168-173) | pp | -12.8 | +2.7 | -6.1 |
| 62-63 (244-251) | pp-p, with a printed swell | -10.1..-12.5 | +0.9..+5.2 | -3.7..-8.4 |
| 76 (300-304) | ppp | -9.6 | +0.5 | -4.0, fourth-loudest stem of the pp chord |

The kit target (LEARNINGS 13) is a pp/ppp roll 3-5 dB under the quietest sustained string section. The opening (bars 1-4, ppp), the coda rolls (174, 181) and the tutti rolls are within it or under it.

**Fix** (`build/roles.json`, Timpani):
- `[168, 176, -3, 0.5]` and `[300, 304.5, -3, 0.5]`.
- Bars 62-63: `[244, 252, -2, 0.5]`, which keeps the printed swell's shape.
- `TIMP_ROLL_TRIM_DB` stays.
- Expected: these rolls end 0..-3 dB re the quietest string section, still -12..-16 re master. Rule 5's caution: the c25 movement II rolls went too far, at 14-23 dB under; do not go lower (inferred).

## Do not touch

- The family ratios at p, f and ff, and the c16 trumpet trims and roles (the chords are now even).
- Trumpet 1's coda and climax lead, and the string f trims with their mf anchors (strings mf to f +2.6).
- The basses' global f/ff trims and the 80/100 Hz bells (use passage roles instead).
- Percussion patches, gains, roles and timing: tam-tam fff and pp with damp, sus. cymbal key 64 / lead 0.25, crash.
- `TIMP_CC1_MAP` with `TIMP_ROLL_TRIM_DB`.
- The letter-G lift shapes, except the bar-121 trombone role ends above.
- The c16 bar-130 and soft-solo roles. The Horn 4 trims.
- `_REBOW_FROZEN` and the re-bow fills.
- `accent_fits.json`, except the two Trombone 1 entries in finding 1. Refit the rest after the role changes.
- The climax order (160 > 122 > 169) with `FAST_CAP_ABOVE` 4 and the top ride 1.6.
