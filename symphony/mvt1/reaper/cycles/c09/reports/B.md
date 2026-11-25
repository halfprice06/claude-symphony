# Cycle 9, critic B: balance and levels (render c08)

## Method

All numbers are from the stem-fixed c08 render (`cycles/c08/render/`), on the tempo map in `build/parts.json`. Scripts and the simulation spec (`s9.json`) are in `/private/tmp/claude-501/mockup-loop/mvt1-c09-B/`.

- Levels are K-weighted power, the mean of L and R, in 10 ms hops. Only differences are used.
- A note's body runs from the score onset +0.08 s to the note end or onset +1.5 s, whichever comes first. The printed dynamic comes from each track's `dyn_curve`.
- "re master" means stem level minus master level over the same window.
- Simulations (`sim9.py`) apply roles, level shapes and note-trim steps to the c08 stems. The sum is then run through `tools/deliver_master.py`. All six findings together, simulated:
  - Delivered LRA 14.8 -> 14.9 LU; span 18.7 dB unchanged; limiter 1.2 -> 1.1 dB.
  - Climax order unchanged: bar 160 -10.35 > bar 122 -10.94 > bars 167-170 -12.09 LUFS. The margin stays at 0.59 dB.

## What holds (measured)

**The printed-dynamic mapping is consistent across the families from pp to ff.** Note-body medians, dB:

| Family | pp | p | mf | f | ff |
|---|---|---|---|---|---|
| Single winds | -41.6..-46.4 | -41..-46 | | -36.0..-38.9 | -31.1..-34.6 |
| Horns | -41.2..-44.8 | -41.9..-43.5 | -34.6..-37.4 | -34.9..-36.2 | -29.5..-29.8 |
| Trumpets | -41.7..-45.4 | | | -33.8..-34.8 | -26.3..-29.2 |
| Trombones | -40.8..-44.4 | | | -30.9..-31.8 | -26.5..-27.2 |
| Strings | -42.7..-47.6 | -40.1..-44.7 | -34.8..-40.2 | | -24.4..-30.6 |

- At ff, trumpets and trombones sit about +3 dB over the horns. Rimsky-Korsakov's resonance table asks for exactly that (trumpet = trombone = 2 horns), so the new trumpet tracks fit their section.
- **Percussion:**
  - Tam-tam fff: -7.3..-9.4 dB re master in bar 122. That is a solo stroke, and it then decays under the chord.
  - Tam-tam pp at bar 175: -10 dB re master, falling to -20.
  - Suspended cymbal: grows to -17 dB re master just before the crash.
  - Crash cymbals: -12 dB re master at qn 636-637, carrying 53-66% of the master's 5-20 kHz.
- **Bar 167-170 theme:** Trumpet 1 and Horn 1 are on top (-6..-10 re master), which is right. Horns and trumpets a2 carry the ff theme over the f chords.

**Where the balance breaks:** the six passages below. In each, an accompaniment voice covers a printed melody, or a printed shape is missing.

## 1. Coda chorale, bars 175-179: Trombone 1 leads for four bars and covers the Violins I melody entry (measured)

**Where:** qn 696-716. Trombones 1-2 and bass trombone play pp dolce chords. Bass clarinet, Clarinet 1 and the strings are also pp. Violins I enter on the pickup at qn 707.75 (pp, "unis.") with the melody that runs to bar 182.

**What is wrong (measured):**
- Trombone 1 is the loudest stem in 14 of the 20 one-qn windows of 696-716.
- Its bodies sit -4.5..-7.5 dB re master. Trombone 2 sits at -6.8..-11.8 and the bass trombone at -8.4..-12.2. The top voice is therefore 2-5 dB over the rest of its own chord.
- Two Trombone 1 notes are hot against the others: E-flat4 at qn 700 (-37.1 dB, against -40.3..-41.7) and D-flat4 at qn 710 (-37.3 dB).
- Violins I's entry: qn 707.75, 708 and 711.86 at -10.3..-10.8 dB re master, against Trombone 1 at -5.7..-7.0.
- **Inferred:** the melody's first two bars sound under a trombone solo.

**Cause:** the c07 role +2.5 dB on all three trombones [696, 712]. It was set to bring the chorale level with the strings, and it lifted Trombone 1 over them. The group level it aimed at is now reached.

**Fix:**
- `build/roles.json`, Trombone 1: add [696, 712, -2.5]. This cancels its share of the c07 lift. Keep Trombone 2 and the bass trombone at +2.5.
- `build/note_trims.json`:
  - Trombone 1: "700.0": -2, "710.0": -2.
  - Trombone 2: "708.0": -2.
- `build/roles.json`, Violins I: add [707.5, 717, 3.5, 2]. The 2 qn release ends inside the held bar-180 note, so the line does not drop at a downbeat (kit LEARNINGS 4).

**Simulated** (with +3, so +3.5 lands about 0.5 dB higher):
- Trombone 1 is top in 2 of 20 windows (was 14).
- Violins I: -6.3..-8.0 dB re master over 708-716. It is top or second in every window, with the trombone chord 0-2 dB under it.
- Delivery unchanged: the ride is at its cap here.

## 2. Recapitulation theme, bars 139-142: the tune is 3 dB weaker against the accompaniment than in the exposition (measured)

**Where:** qn 552-568. The tune is in Flutes, Oboes, Clarinets and Violins I/II in octaves, f < ff. Accompaniment:
- Horn, trumpet and trombone chords (f < ff).
- Violas in eighths (ff).
- Celli and basses.

**What is wrong (measured):**

| | Exposition, bars 27-30 (qn 104-120) | Recapitulation, bars 139-142 |
|---|---|---|
| Melody stems minus all other stems (median, 2 qn windows) | +0.8 dB | -1.4 dB |
| Violins I re master | -5.4 dB | -8.6 dB |

- In the recapitulation the loudest accompaniment stem is only 0-4 dB under the loudest melody stem.
- At qn 556 (the bar-140 ff downbeat) the celli (-10.3) are over Violins I (-10.7).
- Violas (-14.0), Horn 2 (-13.3) and the brass chords (-13.9..-16.8) all sit within 4-5 dB of the tune. The recapitulation adds a ff brass chord that the exposition does not have.
- c08 noted the same open item ("bar 140 Violins I only level with the celli and low winds").

**Fix, `build/roles.json`:**
- Violins I: [552, 568, 2.5, 1].
- Violins II: [552, 568, 2.5, 1].
- Violas: [552, 566, -2] (their figure is accompaniment here, unlike bars 27-30).
- Horn 2: [552, 566, -2] (the loudest horn of the chord).
- Leave the trumpets' existing [556, 568, -3].

**Simulated:**
- Melody minus accompaniment: -1.4 -> +0.2 dB.
- Violins I: -4.3..-8.3 dB re master, against the loudest accompaniment stem at -10.5..-13.6.
- Delivery and climax order unchanged.

## 3. The timpani's printed crescendo roll into the fff climax (bar 159) does not grow (measured)

**Where:** qn 628-641. The timpani play a G roll ff in bar 158, a printed crescendo in bar 159, and an A-flat roll fff at bar 160.

**What is wrong (measured):**
- Bar 159 roll: -30.8 dB at qn 632 and -30.0 at qn 635, a growth of +0.8 dB. Over the same beats the master rises 2.3 dB.
- The CC7 lane rises 67 -> 76: +1.1 dB by the linear CC7 law (kit LEARNINGS 3). The volume envelope adds +0.9.
- Through bars 158-161 the timpani rank 14th to 22nd of 31 stems, at -16..-21 dB re master.
- Brief rule 5 says only a printed crescendo makes a roll grow. Here one is printed, and the roll that should drive the movement's climax stays flat.

**Fix:** `build/score_config.py`, add `LEVEL_SHAPES["Timpani"] = [[(632.0, 0.0), (635.9, 5.0), (636.1, 0.0)]]`.
- The shape meets the existing +4.5 dB at the qn 636 fff stroke, so the roll arrives at the stroke's level with no step.
- Alternatively, raise the CC7 ramp to 67 -> 120 over 632-636 (+5 dB by the linear law). Then leave the shape out.

**Simulated:**
- Roll at qn 632/633/634/635: -30.2 / -28.6 / -27.9 / -25.8 dB (+4.4 dB).
- Rank 14-16 at the end of bar 159. Peak and delivery unchanged.

## 4. Second theme, bars 47-52 and 147-152: the horn half of the horn-cello unison is 2.5-3.3 dB under the celli (measured; norm inferred)

**Where:** qn 183-207 and 583-607. Horn 1 ("1. dolce") and the celli ("dolce") play the A-flat major theme in unison (Poco meno mosso). The harp and divided strings accompany pp-p.

**What is wrong (measured):**

| Bars | Horn 1 minus loudest other stem (median) | Horn 1 on top |
|---|---|---|
| 47-52 | -3.3 dB | 1 of 17 one-qn windows |
| 147-152 | -2.5 dB | 1 of 17 |

- The celli are 2-7 dB over the horn in almost every window.
- Rimsky-Korsakov (*Principles*, "Comparison of resonance") puts a horn level with a string section in piano. The theme's colour is horn and celli together.
- **Inferred:** at this margin the horn reads as a faint doubling of a cello tune.
- The Solo Horn F4 is hot (+3.5 dB median over 18 notes, kit LEARNINGS 13). It sits at qn 189 and 206 here (-4.5 / -3.3 re master), so the line is uneven.

**Fix:**
- `build/roles.json`, Horn 1: [183, 207, 2.5] and [583, 607, 2.5].
- `build/note_trims.json`, Horn 1: "189.0": -2, "206.0": -2.
- Keep the existing trims at 192 (+4) and 592 (+5).

**Simulated** (roles only):

| Bars | Horn 1 minus loudest other stem | Horn on top | Celli on top |
|---|---|---|---|
| 47-52 | -0.8 dB | 7 of 17 windows | 10 |
| 147-152 | 0.0 dB | 8 of 17 | 6 |

## 5. Bars 56-61: hot accompaniment notes cover the "espr." countermelody (measured)

**Where:** qn 220-244. Violins I/II have the "molto cantabile" tune. Clarinet 1 and Horn 2 play the p "espr." countermelody in unison. Horns 3-4 hold pp chords; Bassoon 2 plays a p < line.

**What is wrong (measured):**
- **Countermelody level** (median margin to the loudest other stem): Clarinet 1 -5.3 dB, Horn 2 -4.9 dB (min -11). Neither is on top in any window, which is expected under the tune.
- **Accompaniment over it:** the pp Horns 3-4 and the Bassoon 2 bass go above the countermelody on single notes:
  - Horn 4 F3 at qn 224: -8.0 dB re master, against Clarinet 1 -8.3 and Horn 2 -7.2.
  - Horn 4 E3 at qn 240: -10.0, with a residual of +6.5 dB over its own p median.
  - Bassoon 2 E3 at qn 240: -8.9 (residual +5.2), and -6.6 at qn 242, where it is the second-loudest stem.
- **Existing roles:** Horn 2 carries [220, 244, -1] and Clarinet 1 carries [220, 244, +3].

**Fix:**
- `build/note_trims.json`:
  - Horn 4: "224.0": -4, "240.0": -5.
  - Bassoon 2: "240.0": -5.
- `build/roles.json`, Horn 2: add [220, 244, 2] (net +1).

**Simulated:** Horn 2 margin -4.9 -> -2.9 dB. The Violins I tune is still on top in 13 of 17 windows (+1.8 dB median).

## 6. Double basses: A-flat1 hot and E-flat2 weak at the same printed dynamic (measured)

**Where:**
- Bars 33-34 (qn 128-136): the Bassoon 1 "1. Solo f espr." over held bass notes, printed fp, then p.
- Every E-flat2 in the movement: 29 notes, among them bars 2, 28-29, 36-37, 41-42, 59-62 and 70.

**What is wrong (measured):**
- At p the basses' A-flat1 (MIDI 32) measures -41.5 dB (5 notes) and E-flat2 (MIDI 39) -47.9 dB (6 notes): a 6.4 dB spread at one dynamic.
- Over all dynamics, E-flat2 is -4.1 dB under the track's same-dynamic median (15 notes). Movement II found the same pattern on this patch (kit LEARNINGS 13: A-flat1 +6 to +8, Sus MAX E-flat2 -5.5).
- **Bars 33-34:** the held A-flat1 at qn 132 sits at -3.3..-4.1 dB re master, 0.3-1.2 dB under the bassoon solo. In bar 35 the bass line then drops 5 dB at the same printed p (qn 132 -41.6 -> qn 140 -47.3).
- `pitch_trims.json` has no row for the basses.

**Fix:**
- `build/pitch_trims.json`: "Double basses": {"39": 3, "_all_arts": true, "_skip_onsets": [244.0]}. Skip qn 244, where the basses already stand 3.7 dB over the celli's pizz.
- `build/note_trims.json`, Double basses: "132.0": -4.

**Simulated:**
- Bars 33-34: basses -5.4..-7.4 dB re master, 2.5-5 dB under the solo.
- Basses per bar over 33-37: -41.3 / -45.6 / -46.1 / -44.3 / -43.8 dB, in place of a 5.7 dB step down.

## Dan's two checks (measured)

**Loop pulse.** 17 notes are longer than 6 s. The highest autocorrelations at 3.95 s:

| Note | 100-300 Hz | Centroid | Stem re master |
|---|---|---|---|
| Bass clarinet, qn 492 | 0.83 | 0.58 | -13.7 dB |
| Horn 4, qn 289 | 0.67 | | -9.8 dB |
| Bassoon 2, qn 48 | 0.54 | | |

These are unchanged from c07 and belong to the articulation lens. On the master, the held passages 464-500 and 696-728 measure -0.27 and -0.09 in the band and +0.10 and -0.04 in the centroid. None of the findings above lengthens a held note.

**Accents.** 2-5 kHz in the first 80 ms minus the body:
- Trumpets, trombones and tuba: medians -6.6..-13.0 dB.
- Horns: p90 +7.3..+8.6 dB. Worst cases: Horn 1 qn 665 +10.7, Horn 3 qn 286 +9.4, Horn 2 qn 673 +9.6. These are the same horn accents c07 and c08 listed.
- The level changes proposed here touch no accent note except through the Horn 1 roles in bars 47-52 and 147-152, which have no accents.

## Do not touch

- The soft trims (global 7/7/5 and the per-track overrides) and the trumpet loud trims (f 7, ff 8; Trumpet 3 8/11): they give the even mapping in the table above.
- The tam-tam fff stroke and its roles at [484, 500] and [487, 496]. The suspended-cymbal and crash levels and timing.
- The bar-122 c08 rows (Violins -3, horns +4, violas +6, basses +4, trumpets +1.5).
- The bars 167-170 theme roles and trims (Horn 1/Trumpet 1 +3 notes, Violins I/II cuts).
- The c07 chorale rows on Trombone 2, bass trombone, bass clarinet and Clarinet 1. Only Trombone 1's share changes.
- `ARRIVAL_WEIGHT_AT` 484/636 with the E6 fill. The climax order (160 > 122 > 167-170).
- `accent_fits.json`: refit if any of the roles above moves around an accent.
