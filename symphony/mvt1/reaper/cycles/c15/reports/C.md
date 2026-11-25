# Cycle 15, critic C: tempo, timing and transitions (render c14)

## Method

I measured the stem-fixed c14 render (`cycles/c14/render/`) against `build/parts.json`. Its tempo map, notes and keyswitches are identical to `cycles/c14/rendered_build/parts.json`; the stem fix changed levels only. Score qn was converted to file time on that tempo map. Unless stated otherwise, levels are stereo power in 20 ms windows at a 5 ms hop. Scripts are in `/private/tmp/claude-501/mockup-loop/mvt1-c15-C/`:

- `tempo.py`: beat lengths.
- `xover2.py`: pitch crossover, harmonics 1-4.
- `entries.py`, `front.py`, `slowent.py`: entries after a rest.
- `shortn.py`: every onset at 100 bpm or faster.
- `tutti.py`: per-track arrival at tutti downbeats.
- `sync.py`, `timp.py`: ensemble alignment.
- `rel.py`, `relbump.py`: cutoffs.
- `ks.py`: keyswitch lead.
- `loopacc.py`, `loopstem.py`: brief item 7.
- `acc_one.py`: brief item 8.

I use two arrival measures:
- **"t-3" / "t-6":** the first time after the score onset at which a note reaches its body - 3 dB or - 6 dB. For fast music the body is 0.25-0.6 s, or the 0.5 s peak. For slow entries it is +0.8..+1.6 s (kit section 6).
- **"Re-attack arrival":** from the local minimum before the onset to the 0.25 s peak - 3 dB (`shortn.py`).

## Checks that pass (measured)

- **Printed tempos and ramps.** Every ramp in `RAMP_SPANS` starts and ends on its printed step:
  - bar 46 ends at 113 into 112;
  - bar 68 ends at 86.5 into 126;
  - bar 122 ends at 102 into the sostenuto 100;
  - bar 166 ends at 79.5 into 126;
  - bar 178 ends at 51.5 into Tempo I 50;
  - the animandos reach 120.1 (bar 65) and 120.9 (bar 159) against the printed 118/120.

  The only unprinted beat-to-beat changes over 7.5% are the arc returns that c11 listed as section breaks: qn 88 (+8.7%), 220, 332, 408 and 440 (+10.2%), and 696 (+13.6%). The total length is 433.4 s.
- **Bar-170 fermata.** qn 679 is at 380.31 s. The master falls from -13 to -63 dBFS by +2.0 s, and the cello enters at 382.81 s.
- **Attacca ending.** The master is at -60 dB at qn 728 and -89 dB 1.0 s later. The mp3 ends 1.46 s after qn 728.
- **Keyswitches.** All 870 used keyswitches come at least 9.5 ms before their note (6 come at 9.5-10.7 ms), as in c10.
- **Legato crossovers (Allegro, with leads).** Medians:
  - Violins I Leg Slur +0.010 / Leg BC +0.045;
  - Violins II +0.015 / +0.040;
  - Violas +0.025 / +0.035;
  - celli +0.040 / +0.070;
  - Horns a2 -0.003 (n 6, new since c13).

  Ensemble deviation from each onset's median is within ±0.03 s on every track (`sync.py`).
- **Cutoffs at the tutti rests** (qn 103, 126 and 551). Every stem has fallen 15 dB within +0.13..+0.6 s. The master is -13..-17 dB 0.3-0.45 s after each cutoff.
- **Brief item 7.** Master 100-300 Hz / centroid autocorrelation at 3.95 s:

  | Passage | Band | Centroid |
  |---|---|---|
  | Lento 5-12 | +0.01 | +0.02 |
  | coda 175-178 | +0.08 | +0.16 |
  | Tempo I 179-182 | +0.25 (controls +0.10/-0.03) | -0.08 |

  The +0.25 in Tempo I is master-only: every stem is between -0.34 and +0.08 (`loopstem.py`). I read it as chance in a 22 s window, not a loop.
- **Brief item 8.** Accents at 0.6 qn or longer, 2-5 kHz in the first 80 ms minus the body:

  | | n | median | max |
  |---|---|---|---|
  | brass | 116 | -14.3 dB | 0.0 |
  | winds | 192 | -14.6 dB | +2.6 |
  | strings | 168 | -9.8 dB | |

  The one string value over +3 (Violas 536, +10.6) is the f double stop of 535.5 ringing into the sub. mf quarter: 2-5 kHz falls from -8.6 to -22 dB within 0.12 s of the onset. It is not an attack.

## 1. String phrase entries after rests reach their body 0.2-0.5 s late while the basses, winds and brass beside them are on time, including the Allegro's first downbeat (measured; effect on the listener inferred)

**Where.** First notes after a rest, on Leg Slur MAX or Sus MAX:
- **The Allegro's first downbeat, qn 56 (bar 15).** Celli f half note on Leg Slur MAX. The basses enter with it on Sus MAX.
- **The Allegro.** 136 (Vc p), 220 (Cb p arco), 372 (Vln II), 384 (Cb ff), 424 (Vln II and Vla pp), 440 (Vln I mp), 653 (Vla mp).
- **The Lento, Più lento and Tempo I.** 3 (Vc pp, unison with Cb and BCl), 20 (Vla, Vc and Vln II pp chord), 35 (Vln I), 680 (Vla and Vc), 696 (Vln II and Cb), 707 (Vln I).

**What is wrong.**
- **qn 56.** The celli are 10-12 dB under their body for the first 0.2 s and reach t-6 at +0.28 s and t-3 at +0.33 s. The basses reach t-3 at +0.10 s. On the master the Allegro's opening beat is -16 dB at the onset, -7.6 dB at +0.2 s and -0.5 dB at +0.4 s. At 126 bpm a beat lasts 0.476 s, so the f downbeat arrives two thirds of a beat late.
- The volume envelope adds to this: it rises 2.5 dB across the note (`vol_db` -7.5 at 56.0 to -5.0 at 57.0).
- **The other entries** (t-6 / t-3, s after the score onset; the parts beside them reach t-6 at -0.03..+0.06):

  | Entry | t-6 / t-3 |
  |---|---|
  | Vc 136 | +0.26 / +0.39 (Cb with it: -0.14 / -0.08) |
  | Vln I 440 | +0.37 / +0.40 |
  | Vla 653 | +0.37 / +0.39 |
  | Vln II 424 | +0.48 / +0.57 |
  | Vla 424 | +0.27 / +0.51 |
  | Cb 384 | +0.18 / +0.25 |
  | Cb 220 | +0.16 / +0.20 |
  | Vln II 372 | +0.16 / +0.31 |
  | Vc 3 | +0.38 / +0.45 (Cb +0.01 at t-6, BCl -0.03) |
  | Vla 20 | +0.26 / +0.34 (Cb on time) |
  | Vc 20 | +0.38 / +0.83 |
  | Vln II 20 | +0.20 / +0.51 |
  | Vln I 35 | +0.20 / +0.45 |
  | Vla 680 | +0.31 / +0.59 |
  | Vc 680 | +0.33 / +0.71 |
  | Vln II 696 | +0.20 / +0.52 (the trombone chorale -0.07) |
  | Cb 696 | +0.30 / +0.36 |
  | Vln I 707 | +0.28 / +0.36 |

  Each has a 0.12 s (soft) or 0.06 s (f) entry lead already. The shape is the kit's "soft first-note sample grows" case (section 6): -10..-25 dB at the onset and still -5..-12 dB at +0.2 s.

**Fix.** The method is the kit section 6 (c23) method, lead plus fill.
- **qn 56.** In `build/score_config.py`:
  - add 56.0 to `DOWNBOW_STROKE_AT["Violoncellos"]` (a fresh Sus MAX stroke; 58 then joins as a Leg BC target);
  - add a `LEVEL_SHAPES["Violoncellos"]` row `[(55.94, 0.0), (55.96, 2.5), (56.5, 1.25), (57.0, 0.0)]`, so the envelope holds -5.0 dB from the moved onset.

  The stroke takes the normal f entry lead. If it still reaches t-3 after +0.12 s, add `entry_leads.json` `"Violoncellos": {"56.0": 0.06}`.
- **The other entries.** `build/entry_leads.json` extras (s, added to the family lead; the total stays under `ENTRY_CAP_S` 0.30), plus hand rows in `build/early_fills.json` (`{"db", "pre_s": 0.0, "hold_s"}`). Pass these entries to `auto_fills.py` with `--exclude`.

  | Track | Onset: extra / fill dB / hold s |
  |---|---|
  | Violoncellos | 136: 0.12 / 3.5 / 0.30; 3: 0.12 / 3 / 0.40; 20: 0.12 / 3.5 / 0.40; 680: 0.12 / 3 / 0.40 |
  | Violins I | 440: 0.12 / 4 / 0.35; 35: 0.10 / 4 / 0.30; 707: 0.10 / 4 / 0.30 |
  | Violas | 653: 0.12 / 4 / 0.35; 424: 0.12 / 3 / 0.40; 20: 0.12 / 4 / 0.35; 680: 0.12 / 3.5 / 0.40 |
  | Violins II | 424: 0.12 / 3 / 0.40; 372: 0.06 / 3 / 0.20; 20: 0.08 / 3 / 0.30; 696: 0.10 / 3 / 0.35 |
  | Double basses | 384: 0.10 / - ; 220: 0.08 / 3 / 0.20; 696: 0.12 / 3.5 / 0.30 |

- **Checks.**
  - Each listed entry reaches t-6 by +0.15 s, with no overshoot of the body over 2 dB in its first 1.8 s.
  - The master at qn 56 is within 3 dB of its body by +0.15 s.
  - The rows of the Lento/coda notes that carry re-bows (Vc 20, Vla 20 and 680, Vln II 696, Cb 696) stay frozen in `_REBOW_FROZEN`. A lead moves only the note-on, but re-measure the first re-bow dip of each.

## 2. Wind and brass re-attacks without a lead land 0.03-0.10 s behind the strings throughout the fast music (measured; the size heard is inferred)

**Where.** About 650 wind and brass notes at 100 bpm or faster that start after a short gap and get no lead:
- WIND_DETACH tongued note changes;
- WIND_REP_RETONGUE same-pitch repeats (half of the brass cases);
- Leg Slur MAX re-attacks at slur boundaries.

The worst are the brass in the motor of bars 15-46 and 131-146, and the Horn 1 second theme (finding 4).

**What is wrong.** Re-attack arrival per track, no lead against led notes (n in brackets):

| Track | No lead | Led |
|---|---|---|
| Horn 1 | +0.150 (18) | +0.076 (42) |
| Horn 2 | +0.136 (18) | +0.029 |
| Trumpet 1 | +0.117 (17) | +0.055 |
| Trumpet 2 | +0.138 (16) | +0.085 |
| Trumpet 3 | +0.137 (14) | +0.096 |
| Tuba | +0.126 (31) | +0.065 |
| Bass trombone | +0.095 | +0.014 |
| Trombone 1 | +0.091 | +0.042 |
| Trombone 2 | +0.089 | +0.035 |
| Oboe 1 | +0.106 | +0.078 |
| Oboe 2 | +0.132 | +0.147 |
| Cor anglais | +0.160 (13) | +0.031 |
| Bassoon 1 | +0.092 | +0.043 |
| Bassoon 2 | +0.087 | +0.060 |
| Clarinet 1 | +0.081 (107) | +0.037 |
| Clarinet 2 | +0.082 | +0.042 |
| Flute 1 | +0.059 | +0.026 |
| Flute 2 | +0.085 | +0.038 |

- Family medians, no lead: brass +0.104 (n 239, p75 +0.144) and winds +0.081 (n 361). With a lead: brass +0.062, winds +0.059. All 1223 string onsets measure +0.048.
- The gaps are short: median 0.10 s (brass) and 0.05 s (winds). These notes are therefore not entries, and `ENTRY_LEAD_S`/`ENTRY_LEAD_ART_S` never reach them. `ABUT_LEAD` needs a note that abuts.
- The only re-tongue lead in the tools is `SOST_REP_S` (0.04 s), and it applies only under "Largamente".
- At 126 bpm a sixteenth note lasts 0.119 s, so the brass repeats and tongued changes trail the strings by a third to most of a sixteenth (inferred: a blurred, dragging off-beat motor in the brass).

**Fix.** A new generic rule in `tools/score_to_parts.py`, `RETONGUE_LEAD_S`, as an `elif` before the generic entry branch (next to the `sost_rep` branch).
- **Which notes.** Wind and brass notes on a Sus row (Sus MAX, Sus Non Vib MAX, Sus Non Vib), or a Leg Slur MAX note that is not a legato target, that start under 0.5 qn after the previous note of the track ends (gap > 0), at `ENTRY_MID_MIN_BPM` or faster, and that are not shifted by another rule.
- **What it does.** The note gets `lead_qn(q, s)`. The previous note's end moves earlier by the same amount, so the WIND_DETACH/re-tongue gap is unchanged; cap the lead at 0.3 × the previous note's length.
- **Controllers.** Add the span to `pulls`, so CC11 holds the new note's own level from the moved onset. Move the `cc_falls` return of WIND_REP_RETONGUE and WIND_DETACH "fall_cc" to `new_on(n) - PULL_PAD_QN` (kit section 17: a controller point left at the score onset puts the first 0.05-0.1 s on the fallen level).
- **Values** (by_name; put the track keys first in the dict, because the first capitalised key contained in the name wins): `{"Horn 1": 0.09, "Horn 2": 0.09, "Trumpet 2": 0.08, "Trumpet 3": 0.08, "Tuba": 0.07, "Oboe 2": 0.08, "Cor anglais": 0.08, "Oboe 1": 0.05, "brass": 0.05, "wind": 0.035}`.
- **Run it as a test with these pass criteria.**
  - Brass no-lead median ≤ +0.065 and winds ≤ +0.06; each track within 0.03 s of its led median.
  - Critic A's tongued-hole depth within 1 dB of c14 per family.
  - No same-pitch repeat with a new hole of 6 dB or more (the kit's c15 bassoon failure).
  - Then refit the accents (`fit_accents.py --family brass` and `--family wind`, `--keep-long-qn 1.4`), because the onsets move under the fitted swells.

`TIMP_DELAY_S` 0.045 then matches the brass again: timpani strokes measure +0.042, and the led brass +0.041 by the same measure. Leave it.

## 3. Oboes, flutes and upper brass entries at the f/ff tutti downbeats reach their body 0.12-0.23 s late; the low brass, timpani and clarinets reach it at about +0.05 (measured)

**Where.** f/ff entries at qn 100, 104, 112, 274, 324, 476, 484, 520 (recapitulation), 521, 548, 552, 628 and 664 (Tempo dell'Allegro).

**What is wrong.**
- Of 183 f/ff wind and brass entries in fast music, 52 reach t-3 at +0.12 s or later (median +0.155). The rest have a median of +0.055.
- These are the late entries (onset: t-3 s / level of the first 20-120 ms relative to the body, dB):

  | Track | Late entries |
  |---|---|
  | Oboe 2 | 9 of 10: 100 0.20/-8, 104 0.22/-8, 324 0.23/-8, 484 0.17/-8, 520 0.23/-8, 548 0.21/-10, 552 0.14/-7, 664 0.23/-10, 274 0.13/-5 |
  | Flute 2 | 476 / 520 / 548 / 552 / 664: 0.13-0.19, -6..-7 |
  | Oboe 1 | 521 0.15/-9, 664 0.15/-7 |
  | Horn 1 | 324 / 484 / 520: 0.14, -7..-9 |
  | Horn 2 | 112 0.15/-9 |
  | Trumpet 3 | 112 / 324 / 664: 0.17-0.18, -8 |
  | Trumpet 2 | 628 0.20 |
  | Trombone 1 | 104 0.18, 552 0.28, 664 0.15 |
  | Bassoon 1 | 324 / 552 / 664: 0.21, -6..-8 |

- At qn 324, 520 and 664 the volume envelope is flat within ±0.5 dB over the first second, so the lag comes from the samples.
- At 664 (`tutti.py`): timpani +0.05, tuba +0.07, bass trombone +0.07, Horn 3 +0.12, Trumpet 3 +0.19, Oboe 2 +0.25, Flute 2 +0.33, Oboe 1 +0.34, Bassoon 1 +0.37.
- These tracks get 0.04 s (oboe/flute Sus MAX) or 0.05 s (brass) of entry lead.
- Inferred effect: the tutti chords' top and middle swell in a sixteenth after the bass and timpani on the movement's main downbeats.

**Fix**, in `build/score_config.py`:
- **Entry leads.** The second value of an `ENTRY_LEAD_S` tuple applies to CC11 > 80 in fast tempo; keep the third (mid) value at 0.05:

  ```
  ENTRY_LEAD_S = {"Horn 1": (0.10, 0.12, 0.05), "Horn 2": (0.10, 0.10, 0.05), "Trumpet 2": (0.10, 0.11, 0.05),
                  "Trumpet 3": (0.10, 0.12, 0.05), "Trombone 1": (0.10, 0.11, 0.05), "Bassoon 1": (0.06, 0.12, 0.06),
                  **ENTRY_LEAD_S}
  ENTRY_LEAD_ART_S = {"Oboe 2": dict(ENTRY_LEAD_ART_S["Oboe"], **{"Sus MAX": 0.12}),
                      "Flute 2": dict(ENTRY_LEAD_ART_S["Flute"], **{"Sus MAX": 0.10}), **ENTRY_LEAD_ART_S}
  ```

  The track keys must come before "Oboe", "Flute" and "Bassoon" in the dict, because `by_name` returns the first match.
- **Fills.** Lead alone moves the quiet front earlier rather than shortening it (kit section 6). For entries whose front is -8 dB or lower (Oboe 2 at 100, 104, 324, 484, 520, 548, 664; Oboe 1 521; Horn 1 484; Trumpet 3 112, 324, 664), also add `early_fills.json` rows of +3 dB, `pre_s` 0, `hold_s` 0.10.
- **Checks.**
  - These entries reach t-3 within 0.09 s.
  - First sound (peak - 20 dB) no earlier than -0.15 s.
  - 2-5 kHz in the first 80 ms stays under the body (brief item 8).
  - The 636 extras in `entry_leads.json` are unchanged (the caesura caps them).

## 4. In the second theme the Horn 1 melody trails the celli doubling it by 0.06 s (median), and by 0.1-0.2 s at slur boundaries and the leap at 201 (measured)

**Where.** Horn 1 with the celli in unison, bars 47-52 (qn 184-208) and 147-152 (584-608). This is the movement's main lyrical theme (`LEAD_SPANS` on both).

**What is wrong.**
- At 18 shared pitch changes, Horn 1's crossover minus the celli's has a median of +0.062 s.
- The largest gaps (Horn / celli):

  | Onset | Horn 1 | Celli | Note |
  |---|---|---|---|
  | 201 | +0.205 | -0.005 | 9-semitone leap, Horn lead 0.06 |
  | 588 | +0.145 | +0.02 | |
  | 600 | +0.145 | -0.035 | |
  | 604 | +0.17 | +0.035 | |
  | 192 | +0.055 | -0.02 | |
  | 204 | +0.12 | +0.06 | |
  | 592 | +0.105 | +0.045 | |

- The horn notes at 192, 200, 204, 592, 600 and 604 have lead 0.0. They are Leg Slur MAX re-attacks at slur boundaries (the slur ends at 191, and a new one starts at 192).
- The celli use Leg Slur leads of 0.22 s and land on the beat (median about +0.03).
- Inferred effect: the doubled melody is heard as two lines a sixteenth apart at each slur boundary.

**Fix.**
- The slur-boundary notes (192, 200, 204, 592, 600, 604) get finding 2's `RETONGUE_LEAD_S["Horn 1"]` 0.09.
- The legato targets get per-onset extras in `build/leg_leads.json` (s, added to the Horn 1 legato lead, clamped by `LEG_LEAD_CLAMP`): `"Horn 1": {"188.0": 0.06, "201.0": 0.14, "588.0": 0.10, "591.0": 0.08, "598.0": 0.06, "589.0": 0.04}`.
- **Check.** Horn 1 minus celli is within ±0.03 s median, and no shared onset is over 0.08 s apart.
- The c10-c12 second-theme fills and trims are keyed to these onsets. Re-measure the 189/201 tenuto holes after the move; do not refit them in the same cycle.

## 5. Unison hand-overs re-attack a held note 0.45 s after the beat: Oboe 2 at qn 628 (bar 158) and Horn 3 at qn 418 (bar 105) (measured)

**What is wrong.** `find_unisons` keeps the slurred copy and delays the outlasting copy to where the kept note ends (`UNI_DELAY`, overlap 0.1 qn).
- **Oboe 2, qn 628.** Ob2's G4 half note (with Ob1 on beat 1) is silent until qn 628.9 (+0.453 s). It then attacks: -21 to -12 dB in 0.05 s, with 2-5 kHz rising from -30 to -18 dB, as Ob1 slurs up to E5.
- **Horn 3, qn 418.** Hn3's E4 half note starts at 418.9 (+0.422 s), after its own D4 has ended at 418. That leaves a 0.42 s gap in Hn3 and a second tongued E4 on beat 2.
- The score has one held note in each case, so the render plays a repeated note that is not written.

**Fix.** In `tools/score_to_parts.py` `find_unisons`, for `UNI_DELAY` copies:
- raise the overlap to 0.25 qn (`UNI_DELAY_OVERLAP_QN`);
- add a fade-in to the delayed piece in the volume envelope: -12 dB at its start, 0 dB 0.2 s later (a new `UNI_DELAY_FADE = (-12.0, 0.2)`).

The new attack then sits under the kept note's sound. Equivalent hand rows: `LEVEL_SHAPES["Oboe 2"] += [[(628.74, 0.0), (628.75, -12.0), (629.15, 0.0)]]` and `LEVEL_SHAPES["Horn 3"] += [[(418.74, 0.0), (418.75, -12.0), (419.15, 0.0)]]`, with the overlap change.

**Check.** At the hand-over, the Ob1+Ob2 sum has no rise over 1.5 dB in 2-5 kHz.

## Do not touch

- The `RAMP_SPANS` realisation of every printed rit./allargando/animando and the rit. clamp in `smooth_tempo`.
- The c11 arcs, "open" depth and `BEAT_STRETCH` 284/285/679.
- `CAESURA {636: 0.15}` with the suspended-cymbal key 64 / lead 0.25.
- The final bar at 30 bpm and the 1.0 s mp3 tail (attacca).
- Keyswitch placement.
- The string Leg Slur / Leg BC leads and the c07 mid entry lead 0.12.
- `ABUT_LEAD` on the basses, Horns 3/4, Violins II/Violas hemiola and the brass/oboe/flute 0.05.
- `TIMP_DELAY_S` 0.045.
- Horns a2 timing.
- `_REBOW_FROZEN` and the fitted re-bow shapes (leads move note-ons only; keep the rows frozen).
- `entry_leads.json` 636.
