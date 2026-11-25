# Cycle 43, critic A: articulation and phrasing (render c42, score v621)

Method. All measurements are on the final c42 stems and master (`cycles/c42/render`, 40 stems), placed with `build/parts.json` as it stood at the end of c42. That file equals the render data, including the stem-fix rows; for c41-c42 comparisons I used each cycle's `rendered_build/parts.json`.

- **Timing.** Every timing figure is pcX (`tools/pcx.py`: the t50/h10 perceived attack on harmonic bands that leave out the other pitches' partials). For notes inside chords or overlaps I extended the exclusion to every other pitch the track sounds in the window. Legato joins also carry pcx's crossover (`pair_window`) as a second estimator. The synthetic instant-switch error for these wind and brass joins is robust SD 1-3 ms, median -1..-4 ms.
- **Exposure.** "Exposed" means the stem is within 10 dB of the master over the score onset +0..0.3 s.
- **Repeats (S1).** Repeat dips are the lower body minus the 30 ms minimum, on the repeated pitch's harmonic band, for the stem and for the master.
- **Accents.** Accent shapes are 30 ms stereo-power windows relative to the score onset.

Scripts and scratch files were in `/private/tmp/claude-501/mockup-loop/mvt1-c43-A/` and were deleted at the end. I touched nothing in build/, tools/ or REAPER.

## Manual notes (second round: c37 slot A's pages, 2021 manual PDF pp. 95-99, read again in full, pp. 96 and 99 also as images; MANUAL-GAPS.md and DIGEST.md read)

MANUAL-GAPS items still open in this lens, first:
- **#1 brass accents on Marc Sus LITE / Leg Slur Accent MAX:** never run; finding 4.
- **#2 repetition rows:** in use on 49 notes of Cbn, Bn1, Cl1, BCl, Hn1, Hn4 and Tpt2; status under "Standing checks".
- **#5 expressive wind rows, #9 horn portato, #13 3TB:** still untried.
- **#7 half-section divisi:** still open (c42 A #3).
- **#11 woodwind staccato rows:** done in the fugato windows. The bar-30 staccatos of Flute 1, Oboe 1 and Clarinet 1 (qn 116-117.5) still play clipped Sus notes of 0.08-0.13 s, but they sit 14-26 dB under the master in the tutti (measured), so the gain is low.
- **Repetitions TS (p.98):** finding 5.

| Manual (PDF page) | c37 A's note | Now (c42 render) |
|---|---|---|
| p.95: pre-recorded one-octave runs | n/a | n/a |
| p.96: Repetitions Runs Script (CC14) | n/a | n/a |
| p.96-97: Slur Runs need sixteenths at about 125 bpm or faster ("less realistic" slower); CC1 vibrato, CC11 5 dynamics, no velocity | Yes (123.5 / 126 / 126 bpm) | **Partly** (measured). The phrase arcs now put the runs at 127.0-127.75 and 159.0-159.75 at 119.7 bpm, 5% under the manual's floor; 158 runs at 123.5 and 270 at 126. The run notes' attacks are on time (pcX median -20 ms, n = 11). Minor (inferred); one fix is to exempt those two beats from the arcs' slowing. |
| p.97: Spiccato Runs | n/a | n/a |
| p.97-98: unmeasured / measured tremolo; CC11 moves dynamics and timbre; no velocity | Yes | **Yes**: the same-pitch tremolo continuations of Violins II 152→156 and Violas 153→154 dip 1.6 / -1.0 dB on the stem, as a continuing tremolo should. Tremolo onsets pcX -29 ms (n = 10). |
| p.98: Trills; Sul ponticello (violas) | n/a | n/a |
| p.98: **Repetitions**: one note repeated "for a little more than one second", "about a dozen pulses", bow reversals in the sample, tempo-synced, CC11 crossfades 3 dynamics, no velocity | Not used; A/B proposed (celli bar 130) | **Still not used.** New on this reading: a dozen pulses in a little over a second is about 9-11 pulses per second. That fits sixteenths at the recorded 120 bpm (8 per second; 12 pulses in 1.5 s), not eighths, which would need 3 s for 12 pulses, longer than the 2.5 s files c42 A read (inferred). Finding 5. |
| p.98-99: slur vs portamento vs bow change; a transition needs no gap; the first note of a phrase has no legato; monophonic by default (CC22; p.99 has the polarity backwards) | Yes | **Yes, with one exception** (measured). No chord on any legato row, no same-pitch overlap on a legato row. The shortest keyswitch-to-note distance is 9.5 ms, and none falls after its note. Of 1,043 slurred adjacent-pitch pairs on legato rows, 1,042 are joined; the exception is Violas 76→78 (finding 3). |
| p.99: Legato Slur Staccato: "the first note of each legato phrase" gets "a slightly stronger attack" | n/a, not used | **Now relevant.** Phrase-first notes on Leg Slur MAX are the latest class of string note in the render (finding 2). The "StacSl Leg BC + Slur + Port MAX" row is the library's own answer, but it is a whole-phrase combination row (kit c16: 3.3 dB lower on the violas). Fix the timing with leads first; the row stays an optional A/B. |
| p.99 (new on this reading): in the bow-change combination rows "Opus decides which of the components to play based on the MIDI data", in a "Combinations section" that this edition lacks | not noted | Not needed: the pipeline picks Leg Slur, Leg BC or Leg Port per join itself. |
| MANUAL-GAPS #2: LegRep / Leg Slur Rep (p.101, 106, 109-110, 112) | Not used | Used since c37-c41 (49 notes). |

Standing checks (measured unless marked):
- **S2.** 1,428 exposed notes. The ensemble pcX median is +10 ms with a robust SD of 43 ms.

  | Family | Robust SD by class | Medians by class | Note |
  |---|---|---|---|
  | Strings | 46-55 ms in every class | +8..+12 ms | symmetric scatter |
  | Winds | 29-34 ms | legato +19, re-attacks +27 ms | later than the strings |
  | Brass | 21-42 ms | entries -13, repeats -23 ms | early |
  | Timpani | 1-13 ms | +10..+16 ms | |

- **Per-join repeatability.** Between c41 and c42 the per-join pcX on joins with identical data was the same to the millisecond (p75 |diff| 0 ms) for 89-100% of joins. Violins I / II, whose instances were fully rebuilt in c42, moved by more than 40 ms on 9% of joins; Bassoon 1 on 11%. Per-onset leads therefore act on stable data.
- **S1.** Stem repeat dips by family:
  - winds/brass median 2.1-9.3 dB per track; the weakest are Bass clarinet 2.1 dB (4 exposed), Contrabassoon 2.8 (none exposed), Bass trombone 3.1 and Bassoon 2 3.3;
  - strings 2.7-3.9 dB.

  Exposed wind/brass repeats under 3 dB are few and most have a 7-15 dB re-attack: Horn 1 452 / 528 / 624 on LegRep (dip -0.8..1.8, rise 9.6-15.1, as c41 accepted), Horn 2 122 and 238.5, Bass clarinet 388, Bassoon 2 156, Trombone 2 568. The celli G2 pedal in bars 127-130 has master dips of 1.1-2.3 dB and master rises of 2.9-4.9 dB (bar 130: 2.9), as c42 A found.
- **S3.** Not re-measured: bar 62 was fixed in c42 and is unchanged since.
- **Item 7 (re-bows).** Dips and steps are identical to c41: medians 2.7 / 3.0 / 3.4 / 3.8 dB (Cb, Vc, Vla, Vln II). Violins I measures 6.1 dB, but over only 6 re-bows, one of them the printed down-bow at 48, where the printed f > p decrescendo starts (the step is the decrescendo). No held-note data changed, so c41 C's 3.95 s loop result stands.
- **Item 8 (accents).** No bite: 2-5 kHz front (80 ms) minus body has median -9.5 / -11.2 / -13.5 dB (strings / winds / brass) and a brass maximum of -2.2.
- **Breath marks.** All 35 have played gaps: 62-300 ms where the line continues (the shortest, 62 ms, is Flute 1 before the bar-160 caesura).
- **Tenutos.** Slurred string tenutos are joined (overlaps of 19-24 ms).
- **Staccatos.** Every printed string staccato is on a Stac row.

## 1. Wind and brass legato note changes were never refit on pcX. Horn 2 trails the Clarinet 1 it doubles in the bars 56-63 espr. duet, and the bass clarinet and bassoon solos have the slowest transitions in the score (measured; fix gain inferred)

**Where.**
- Horn 2 and Clarinet 1, bars 56-67 (qn 223-267): "2. espr." p, in unison under the violins' molto cantabile.
- Bass clarinet: Lento bars 2-4, "Solo espr." bars 77-78 (qn 305) and 107-109 (425-436), coda bars 177-178 (708-710).
- Bassoon 1: solo bars 33-34 (131-135, 1.4-2.5 dB under the master, the most exposed line there); also 413, 517, 575.5.
- Single exposed joins on Flute 1, Oboe 1, Cor anglais, Clarinet 1 and Horn 1 (list below).

**What is wrong (measured).**
- **Never refit on pcX.** The c37 per-onset legato leads were fitted on the m37 estimator, which c42 showed shares partials under 220 Hz. Only strings were refit on pcX (c42).
- **Winds and brass run late overall.** 237 exposed wind/brass joins have pcX median +20 ms and crossover median +30 ms, against +8 ms for the strings' legato.
- **Two tracks are systematically late:**

  | Track | Joins | pcX median | More than 60 ms late | Exposed |
  |---|---|---|---|---|
  | Bass clarinet | 19 | +65 ms | 58% | 18 |
  | Horn 2 | 25 | +44 ms | 44% | 18 |
  | Bassoon 1 | 46 | +28 ms (robust SD 61) | 39% | 21 |

  The bass clarinet's legato lead is 0.05 s (set in c03 on an earlier crossover measure). The family lead is "Horn" 0.06, with no per-onset entries for Horn 2.
- **Horn 2 against Clarinet 1, same pitches at the same onsets** (15 shared joins):
  - Horn 2 is later by a median +38 ms (pcX) and +14 ms (crossover).
  - At 227, 239, 239.5, 240 and 249 both estimators put Horn 2 38-167 ms behind (pcX / crossover):

    | Join | Horn 2 | Clarinet 1 |
    |---|---|---|
    | 227 | +71 / +86 | +14 / +10 |
    | 239 | +84 / +102 | +12 / +26 |
    | 240 | +143 / +72 | -24 / -34 |
    | 249 | +78 / +78 | +18 / +26 |

  - Band shapes: at 226 / 227 / 239.5 the new pitch is 15 / 6 / 0 dB under its body at the beat and reaches it by +0.05-0.15 s, while the old pitch still sounds. At 240 it stays 7 dB under until +0.2 s (a sag).
- **Bass clarinet.** The solo joins are late by both estimators: 305 +73 / +60, 425 +64 / +64, 435 +101 / +143, 435.5 +75 / +102. The soft Lento and coda joins (4, 10, 708, 710; v60, CC11 34) cross over on time (-20..+14 ms) but the new note sags 8-14 dB for 0.2-0.3 s (pcX +72..+230). Their broadband join dips are 4.2-6.5 dB.
- **Bassoon 1 solo:** 131 +99 / +74, 134 +62 / +64, 135 +69 / +96.
- **Inferred:** in a doubled line a 50-170 ms lag is heard as two players not together; in an exposed solo, as a sluggish legato that drags behind the accompaniment.

**Fix.**
1. **`build/leg_leads.json`, new key "_c43".** The c42 A #1 rule with the target at the ensemble value: exposed joins with |pcX - 0.010| > 0.05 s whose crossover (relative to the wind/brass median +0.030) agrees in sign by more than 0.03 s. New total = old + 0.6 x (pcX - 0.010), change clamped ±0.12 s. Horn 1 411.5 is left out (pcX -158 against crossover -32). New totals:
   ```
   "Flute 1": {"115.0": -0.08, "296.0": -0.03, "299.5": -0.04, "395.0": 0.07},
   "Oboe 1": {"315.5": 0.06}, "Cor anglais": {"24.0": 0.05},
   "Clarinet 1": {"215.0": 0.09, "247.0": 0.04, "507.0": 0.08},
   "Bass clarinet": {"425.0": 0.03, "435.0": 0.05, "435.5": 0.04},
   "Bassoon 1": {"131.0": 0.05, "134.0": 0.03, "135.0": 0.04, "366.0": -0.03, "413.0": 0.09, "517.0": 0.06, "575.5": 0.04},
   "Horn 1": {"50.0": 0.03, "171.0": 0.04, "188.0": 0.02, "195.0": 0.04, "419.0": 0.08, "420.0": 0.12},
   "Horn 2": {"226.0": 0.06, "227.0": 0.04, "239.0": 0.04, "240.0": 0.08, "246.0": 0.04, "262.0": 0.03},
   "Trombone 1": {"521.0": -0.06, "710.0": -0.06}, "Horns a2": {"313.0": -0.05},
   "Trumpet 1": {"673.0": -0.04}   (the Trumpets a2 alias join; check that the key reaches the alias)
   ```
   Also give Horn 2 239.5 / 249 / 256 (+60 / +78 / +99 by both estimators, 8.6-11.2 dB under the master) +0.03 each, so the whole duet moves together.
2. **Lead caps.** Before building, diff the moved onsets (`cycles/c33/actor_scripts/pdiff.py`). Joins after eighths (Horn 2 240 / 246 / 262, Bassoon 1 135) hit the 0.45 cap at about 0.12 s. Any listed lead that does not move its note must be set back, together with any fill keyed to it. Celli 266 in c42 is the example: finding 3.
3. **Fills on the soft sagging joins.** These joins cross over on time; leading them would only make the crossover early. Use `tools/auto_fills.py` on c42 restricted to Bass clarinet 4 / 10 / 708 / 710, Horn 2 240 and Horn 2 172 (dip 7.5). Start from +3..+4 dB held to +0.20-0.25 s after the moved onset; simulate on the stem first.

**Pass.**
- Every listed join |pcX - 0.010| ≤ 0.04 s.
- Horn 2 minus Clarinet 1 at the 15 shared joins: median within ±0.02 s, none over 0.06 s.
- Bass clarinet pcX median ≤ +0.035 s.
- No new dips ≥ 5 dB or bursts ≥ 3 dB at moved joins.
- The soft bass clarinet joins dip ≤ 3 dB.

## 2. String phrase-first notes on Leg Slur MAX at f/ff arrive about 50 ms late on Violins I. At letter G the first violins' six upbeats trail the second violins' unison upbeats by 66-118 ms (measured)

**Where.**
- Letter G, bars 117-120: the Violins I upbeats at qn 464.5, 468.5, 472.5, 474.5, 476.5 and 478.5 (ff, each after an eighth rest, slurred into an accented downbeat), in unison with Violins II and doubled by Flute 1 and Oboe 2.
- Also Violins I 72.5, 372.5 (the violins' fugato entry, bar 94) and 380.5; Violas 360 and 569.5; celli 324 and 552.

**What is wrong (measured).**
- **Where the lead comes from.** A phrase-first note after a rest plays Leg Slur MAX's first-note layer. At CC11 above 80 it takes the loud string entry lead of 0.06 s (`ENTRY_LEAD_S` string (0.12, 0.06, 0.12)). In c23 Violins II alone got `ENTRY_LEAD_ART_S["Violins II"] = {"Leg Slur MAX": 0.06}` (total 0.12, `build/score_config.py` line 1246). Violins I never got the equivalent.
- **Violins I is late.** Its 14 exposed loud Leg Slur MAX phrase-first notes have pcX median +51 ms, and 9 of them are later than +40 ms. Violins II's equivalents with the 0.12 s lead have median +7 ms (n = 6).
- **Letter G, two estimators:**
  - Violins I pcX +79 / +55 / +72 / +52 / +50 / +46 ms; arrival at the harmonic body - 6 dB +114 / +62 / +76 / +68 / +66 / +112 ms.
  - Violins II at the same onsets: -46..+1 ms pcX.
  - Flute 1 arrives at +0..+36 ms, Oboe 2 at -20..+70.
  - The unison flams by +78 / +78 / +118 / +76 / +91 / +66 ms on every bar's upbeat of the development's climax theme.
- **Other late phrase-first notes:** Violins I 372.5 +70, 380.5 +66, 72.5 +52; Violas 360 +77, 569.5 +106; celli 324 +118, 552 +81.
- **Inferred:** the upbeat is where each phrase is heard to start, so a 0.1 s flam between the two violin sections there reads as ragged ensemble.

**Fix.** Use `build/entry_leads.json` "Violins I" extras rather than a generic rule: Violins I's on-time loud entries (56.5 at -46, 104.5 at -3, 318.5 / 322.5 / 387 at +11..+14) would turn early under a blanket extra. Extras, added to the 0.06 s:
```
"Violins I": {"464.5": 0.05, "468.5": 0.04, "472.5": 0.05, "474.5": 0.04, "476.5": 0.04, "478.5": 0.03,
              "372.5": 0.04, "380.5": 0.04, "72.5": 0.03}
"Violas": {"360.0": 0.05, "569.5": 0.06}, "Violoncellos": {"324.0": 0.06, "552.0": 0.05}
```
Each value is about 0.8 x (pcX - 0.01), because loud entries transfer close to 1:1 (kit c07). Keep the existing 35 / 118 / 440 / 707 entries. The library's alternative is the "StacSl Leg BC + Slur + Port MAX" row (p.99) on the letter-G phrases as an optional pass-2 test alias; it needs its own level fit.

**Pass.**
- At letter G each Violins I upbeat is within ±0.03 s of Violins II's at the same onset (now +0.066..+0.118 s).
- All listed notes have |pcX - 0.01| ≤ 0.04 s.
- The pickups' levels against their accented targets are unchanged within 1 dB (PICKUP_LIFT acts from the moved onset).

## 3. String legato refit on pcX: the violins (planned for c43) must include the bar 55-61 aliases, where the two sections playing the tune are 60-160 ms apart at 7 of 20 shared onsets. Revert celli 266 for a different reason than c42 gave, and join the Violas' slurred A-flat at qn 78 (measured)

**Where.**
- Violins I and II, all monophonic legato joins.
- The "Violins I f62" / "Violins II f62" aliases, bars 55-61 molto cantabile (219-244), where the two sections play the tune in unison and octaves.
- Violoncellos 266 (bar 67).
- Violas 78 (bar 20, f, the slurred espr. counter-line; the stem is 4.7 dB under the master).

**What is wrong (measured).**
- **Main tracks.** Violins I: 245 joins, pcX robust SD 52 ms, 24% more than 60 ms off the median (+18 ms). Violins II: 125 joins, 46 ms, 25%.
- **The f62 aliases are the widest legato in the strings:** robust SD 74 / 73 ms (17 joins each). At their 20 shared unison/octave onsets the two sections differ by 60 ms or more at 7 (35%), for example 224 (70 ms), 225 (161), 230 (121), 236 (108), 239.5 (84) and 242 (60).
- **Celli 266.** c42's +0.10 s lead did not move the note: it played at 265.6250 against 265.6274 in c41, so the lead was absorbed by a cap. Its early fill moved 0.10 s earlier anyway (pre_s 0 → 0.10), and pcX went from +170 to +227 ms. The revert is right, but the cause is the cap, not the lead's direction.
- **Violas 78.** The printed slur runs 72-78 (checked on the score page), but the A-flat at 78 plays as a new phrase:
  - velocity 83, not the legato 124;
  - a CC1 phrase-start point (70) at 78;
  - the E-flat before it ends at 77.95, the slur-break gap from the `elif o.get("art") and _lg(o["art"])` branch in `score_to_parts.py` (about line 2635), so `same_slur(76, 78)` returned false;
  - result: no legato transition, pcX +138 ms, on Leg Slur MAX's first-note layer.

  It is the only slurred pair on a legato row in the score that is not joined.

**Fix.**
1. **`build/leg_leads.json` "_c43" violins.** Use the c42 A #1 rule against each section's own median (pcX +18 / +21 ms, crossover -3 / +9 ms). Keys under "Violins I" / "Violins II" also reach the f62 aliases (ALIAS_TRACKS inherit the source tables; confirm in parts.json). New totals:
   ```
   "Violins I": {"39.0": -0.09, "47.0": 0.02, "67.0": -0.04, "97.0": -0.05, "98.0": -0.04, "137.0": -0.07, "249.0": -0.07,
     "255.5": -0.06, "257.5": -0.04, "260.0": -0.04, "267.0": 0.05, "271.0": -0.05, "277.0": -0.04, "323.0": -0.03,
     "395.0": 0.08, "397.5": -0.05, "544.0": 0.11, "558.0": -0.08, "562.0": 0.05, "647.5": 0.10, "650.0": 0.06,
     "657.5": 0.07, "660.0": -0.05,
     "227.0": -0.04, "231.0": 0.04, "232.0": 0.04, "243.5": 0.01}
   "Violins II": {"255.5": -0.07, "256.0": -0.04, "257.5": -0.07, "260.0": -0.05, "361.0": -0.05, "404.0": -0.05,
     "644.0": -0.05, "649.5": -0.07,
     "230.0": 0.07, "231.0": 0.03, "231.5": 0.05, "234.0": 0.04, "239.5": -0.07, "242.0": 0.07}
   ```
   - The alias entries (227-243.5 on Violins I, 230-242 on Violins II) use the beat target +0.01 s and the crossover's sign, so the two sections converge on the same time.
   - 225 (Violins II +178 ms) and 236 (Violins I +114) fail the crossover test. Check them by eye on the stem (`cycles/c42/actor_scripts/jf42.py`) before adding them.
   - Both sections are early together at 255.5-260 (bars 64-65, after the poco animando): -63..-120 ms.
2. **Celli 266.** Lead back to 0, early-fill pre_s back to 0 (as c42 said). Also check the two other c42 changes that moved about a third of their planned amount: celli 351 (0.060 of 0.189 qn) and 625.5 (0.023 of 0.075 qn).
3. **Violas 78.** Print `slur_of()` for the notes at 76 and 78 in `build_track` and fix whichever input splits them; one candidate is the moved-onset leg join from the 75.5 short_sus pickup. Then 78 should come out as a legato target from 76 (velocity 124, LEG_OVERLAP).
4. **Order against the CC16 reset.** If B #4's CC16 reset lands in the same render, expect about 10% of string joins to move by more than 40 ms: c42's full rebuild of the violins moved 9% against 0-5% on untouched instances. Apply the list, then re-measure every listed join on the CC16 render before the next refit.

**Pass (c42 A #1's).**
- pcX robust SD: Violins I ≤ 45 ms, Violins II ≤ 42; each f62 alias ≤ 55.
- At most 2 of the 20 shared alias onsets more than 60 ms apart.
- No moved join further from its median than now; no new dips ≥ 5 dB or bursts ≥ 3 dB.
- Violas 78 joined, with pcX within ±0.04 s of the section median.

## 4. Accents are the plain note 2-4 dB louder, with the same front; the emphasis peaks 0.17-0.20 s after the beat. Run MANUAL-GAPS #1 as c41 C #2 wrote it, in the second pass (measured; gain inferred)

**Where.** 663 printed accents. The brass accents cluster in bars 23-26, 32-33, 41, 69-72, 80-83, 131-138, 142-143 and 167-170; the strings' accented quarter strokes in bars 131-138.

**What is wrong (measured).**
- **Same front as plain notes.** On the same row, non-legato notes of 0.3 s or more, the accents' fronts match the plain notes':

  | Row | 2-5 kHz front minus body, accented / plain | Broadband first 0.15 s minus body, accented / plain |
  |---|---|---|
  | Strings Sus MAX | -7.2 / -6.5 dB (n = 42 / 179) | -0.8 / -0.9 dB |
  | Winds Sus MAX | -11.4 / -10.4 dB | -0.1 / -2.9 dB |
  | Brass Sus MAX | -14.4 / -11.4 dB (n = 31 / 92) | -3.0 / -2.9 dB |

- **Weight spread over the first 0.4 s.** Against unaccented same-row, same-dynamic neighbours within 4 qn, the accents are louder by:

  | Family | 0-0.1 s | 0.1-0.2 s | 0.2-0.4 s |
  |---|---|---|---|
  | Strings | +3.0 | +4.2 | +2.0 |
  | Winds | +3.5 | +3.7 | +2.5 |
  | Brass | +2.3 | +2.4 | +2.3 |

- **Late peak.** The accents' 30 ms peak falls at a median +0.170 / +0.170 / +0.195 s; 61 / 65 / 72% peak after +0.15 s. The brass accent's own first 100 ms sits 1.9 dB under its 0.2-0.4 s level.
- **Compared with a real orchestra.** The brass accent 2-5 kHz front-minus-body median is -13.5 dB, against -4.2 dB measured on a real orchestra (the c12 note in `build/score_config.py`).
- **Inferred:** the GENTLE_ACCENT swell meets Dan's "weight, not bite" rule, but every accent is a louder plain note whose emphasis grows over the first fifth of a second. At 126 bpm that peak lands near the following eighth, so the accent can read as a small swell after the beat rather than an accent on it.

**Fix.** The test is already written in `cycles/c41/reports/C.md` #2 and costs no main-project memory:
- Test aliases (`TEST_TRACKS`, left out of the sum) for Trombones 1-2, Bass trombone and Horns 1-4 (Horns a2 where a2) on "Marc Sus LITE" over qn 124-132 and 564-572.
- Velocity 45-70 from the printed dynamic, so the low-pass on the marcato attack stays mostly closed (p.101); never the top velocities (p.102).
- CC1 from `CC1_DYN_MAP`, no CC11 bump, the GENTLE swell cut to about +1 dB, and `fit_accents.py` refit on the test stems.
- Add one string test alias: Violins I on "Sus Marc LITE" for the accented quarters of bars 131-138 (520-552), with its level step taken from the body (kit §20, c23-c24).

**Pass (c41 C's, plus timing).**
- 2-5 kHz front minus body -6..-2 dB, never over +3.
- The master's 2-5 kHz jump under +3 dB with the test stem substituted.
- Level over same-dynamic neighbours 2-4 dB.
- The accent's 30 ms peak at or before +0.10 s.
- pcX within ±0.02 s of the GENTLE version.

Keep GENTLE_ACCENT as the fallback. Dan has not yet heard an accent with a front.

## 5. Repetitions TS: the manual's rate points to sixteenths, so probe one note before choosing between the celli's bar-130 sixteenths and the basses' eighths (manual read; rate inferred)

**Where.** Two candidates:
- the celli's G2 sixteenths in bar 130 (qn 516-520, f <, 16 Stac RRx9 strokes, 7.6 dB under the master);
- the basses' eighth pedals (c42 A #2: 104-124, 520-536, 556-568, 664-676).

**What is wrong (measured).**
- Bar 130's repeats re-attack 8.1 dB on the stem but only 2.9 dB in the master's G2 band (S1). Bars 127-129 are similar: master dips 1.1-2.3 dB, rises 3.5-4.9 dB.
- The basses' pedals are c42 A's numbers, unchanged.

**Manual (p.98).**
- "A little more than one second", "about a dozen pulses" means 9-11 pulses per second. Tempo-synced to the host; CC11 crossfades three dynamics; no velocity. 2021 lists Violas and Basses only; the installed KS Masters have the row in every section (DIGEST §11).
- At the recorded 120 bpm, sixteenths are 8 per second: 12 pulses fill 1.5 s of a 2.5 s file, the rest being release. Eighths would need 3 s for 12 pulses.
- So the internal grid is most likely sixteenths (inferred), which fits bar 130, not the eighth pedals. The c42 actor already flagged the disagreement with A's eighth reading.

**Fix.**
1. **Probe.** One pass-2 test alias of Violoncellos on "Repetitions TS" playing one held G2 over 516-520 at the render's tempo (126 bpm), CC11 from the printed curve, one note per 2 qn (the sample holds about 12 pulses, 1.43 s at 126 bpm).
2. **Measure** the inter-onset interval of the internal pulses on the test stem (G2 band, 10 ms frames): 0.119 s means sixteenths, 0.238 s eighths.
3. **Then.**
   - If sixteenths: A/B bar 130 against the Stac strokes. Pass: master G2-band re-attack rise ≥ 4 dB (now 2.9), pulses within ±15 ms of the sixteenth grid, bar level within ±1 dB K, front minus body ≤ +3 dB.
   - If eighths: run c42 A #2's basses test as written.

## Do not touch

Do not touch:
- `tools/pcx.py` and pcX as the only lead estimator;
- the c42 viola/celli leads and their moved fills and notches, except celli 266;
- the f62 aliases' release fit (POST_SHAPES_S) and SUBITO_SILENT_QN;
- REP_ROW with REP_ROW_GAP_S (0.06, 0.15) and the LegRep / Leg Slur Rep notes on Cbn, Bn1, Cl1, BCl, Hn1, Hn4 and Tpt2 456;
- GENTLE_ACCENT and `accent_fits.json`, until finding 4's test passes;
- STAC_ROW Violins I, the pass-2 fugato staccato windows, and the 14 Sus Marc LITE strokes;
- AUTO_REBOW with its fitted re-bow shapes (identical to c41);
- the legato overlaps and keyswitch placement (no chords on legato rows, shortest keyswitch 9.5 ms);
- the breath gaps and the tenuto joins;
- the DIV A coda solo as fitted;
- every per-onset lead in `leg_leads.json` and `entry_leads.json` not listed above.
