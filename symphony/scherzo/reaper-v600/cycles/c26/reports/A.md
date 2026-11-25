# Cycle 26, critic A: articulation and phrasing (on the c25 render)

Material: `cycles/c25/render` stems, `cycles/c25/build_render/parts.json` (the data as rendered), `cycles/c25/records/`; `cycles/c18/render` and its parts.json as the older comparison (c24's stems are deleted). Tools read, not changed: `cycles/c25/actor_scripts/fig25.py`, `spic25.py`, `rt25.py acc2`, `tools/pcx.py`. My own scripts: per-pitch harmonic bands (harmonics 2-5, ±0.3 semitone, 2048-point STFT, 5 ms hop), 5 ms power envelopes, and the first-80 ms spectra of accented notes. "Measured" means a number from the render, parts.json or a patch file; "inferred" means reasoned from those numbers.

## Manual notes

`MANUAL-READING.md` has no row for c26. I read group A1 (PDF pages 89-94 of the May 2021 HO manual, strings: sections, divisi, long and short articulations) in full, because three of this cycle's items are string accents and string shorts, and I used `MANUAL-GAPS.md`.

| page | what it says | where it applies here | does the render follow it |
|---|---|---|---|
| 91-92 | Marcato Sustain plays a marcato sample with the looped sustain: "extra power at the start of the note" | the accented half notes of the theme in every statement (123, 315, 327, 345, 351, 915 ... on Violins I, II, violas) | only Violins I's hemiola uses it (Sus Marc LITE). The other string accents play Sus MAX, and their front is 2-3 dB under their body (finding 2). c22 measured Sus Marc LITE as negative on Violins II and violas, so the front has to come from CC11 there |
| 92 | Spiccato: 9 round robins; Spiccato Marcato MOD crossfades to marcato on CC1 for accents inside a short line | Violins I D5 / D sharp 5 / F sharp 5 on Spiccato RRx9 (c24) | followed. The MOD patch is not needed: the scherzo's accents sit on long notes |
| 93 | Staccatissimo is "like Staccato, but with notes of even shorter duration" | Violins I's isolated staccato quarters on "Staccatissimo RRx9" | not what the render gives: Violins I Staccatissimo rings 280 ms to -20 dB, against 210 ms on Violins II's Stac (finding 4) |
| 93 | Staccato Marcato MOD: CC1 raises the accent on single short notes | none needed (see p.92) | not used, correctly |
| 94 | Repetitions: one held note plays about a dozen bow changes, no round robin | the theme's repeated eighths are pairs, not runs | correctly not used |
| 91 | Harmonics only in 2nd Violins, all two octaves above the fundamental | Violins I's E6 (bars 141-149) on the Violins II track's Harmonics row | followed |
| 89-90 | DIV A / B: close mics only; a divisi half is "not much less" loud than the whole section | Violin I solo (DIV A), Violas div (DIV B) | not re-measured this cycle (B / C lenses) |
| MANUAL-GAPS #1 | woodwind staccato rows | the winds' theme heads now play "Stac DblTng RRx9" | in use; but the slurred eighth before each staccato quarter rings over it (finding 1) |

## Findings, ranked by what a listener hears

### 1. Dan's figure in the woodwinds: in both tutti statements the slurred eighth before the staccato quarter keeps sounding over it; 70 ms after the staccato's note-on the old pitch is still louder in Flute 1, Oboe 1, Flute 2 and Clarinet 2 (measured)

Where: the theme figure "staccato quarter, slurred eighth pair, staccato quarter" in the woodwinds, bars 107, 111, 115, 117, 119 (qn 318, 330, 344, 348, 354) and 307-319 (qn 918, 930, 944, 948, 954), plus bar 35 (qn 102). The second eighth of the pair plays "Leg Slur MAX" (Clarinet 2 "Leg Slur Rep"), and the staccato quarter after it plays "Stac DblTng RRx9". The first check (fig25) covers only Violins I and II, so it has never looked at these.

Evidence (measured on the c25 stems). The value is the staccato's band minus the old pitch's band, 70 ms after the staccato's moved note-on. Every pair is a slur end on a Leg or Sus row followed within 0.1 qn by a staccato note of another pitch.

| track | pairs | median | under +3 dB | worst (qn: dB) |
|---|---|---|---|---|
| Flute 1 | 15 | +0.7 | 11 | 348 -9.0, 948 -8.8, 318 -5.6, 354 -5.3, 330 -5.1, 344 -2.8 |
| Oboe 1 | 18 | +8.4 | 6 | 344 -11.6, 944 -9.8, 330 -5.5, 930 -4.9, 102 -2.3 |
| Clarinet 2 | 10 | +3.8 | 4 | 918 -5.1, 954 -4.9, 318 -4.3, 354 -4.2 |
| Flute 2 | 8 | +3.4 | 4 | 348 -10.1 |
| Violins I (same figure) | 17 | +10.6 | 0 | 930 +4.3 |
| Violins II | 15 | +10.2 | 2 | 126 -3.4 |

- Flute 1 at qn 344 (bar 115): the slurred A5 is written to end 9 ms before the B5's note-on. The B5 peaks at +14 dB at its note-on and falls to -0.2 dB by +90 ms, while the A5 is still at +9 dB at +50 ms and +4.9 dB at +110 ms. From +70 ms on, the staccato is quieter than the eighth before it.
- Oboe 1 at 344 has a second cause. The slurred A5 peaks at +27 dB but the staccato B5 only at +11 dB, 16 dB under the eighth before it (CC1 is 110 on the A and 95 on the B). fig25 reads 34.5 dB there only because the B never rises over the A until the A has died away.
- Since c19-c23 the string pairs separate by about 10 dB. The woodwinds doubling the same figure in the tuttis do not, so the figure still blurs "every time it is played" wherever winds double it (inferred).

Fix:
- a) Release cap on the woodwinds' legato rows at f / ff, the method that worked on Violins II's Stac RRx9 (c20). In `build/mix.json`, add a `sus_release_cap_ms` entry for each of Flute 1, Flute 2 and Oboe 1: `{"ms": 120, "rows": ["Leg Slur MAX"], "dyn": ["f", "ff"]}`. Add the same for Clarinet 2 with `"rows": ["Leg Slur Rep"]`.
  - First read each row's release groups and their dynamic words with `load_oib`. If the group names carry no dynamic word, use `any_dyn` limited to these rows.
  - Soft phrase ends (trio, second idea) keep their releases.
- b) Oboe 1's staccato quarters in the two tuttis (312-360, 912-960): raise their velocity to the row's top layer.
  - Read the "Stac DblTng RRx9" layer bounds first.
  - Either use `VEL_SET["Oboe 1"]` on the onsets 318, 330, 344, 348, 354 and 918 ... 954, or use a velocity offset on the Stac DblTng notes in those spans.
  - This is velocity, not a level move.
- Acceptance (range test 312-360 against a same-start control):
  - staccato over old pitch at +70 ms is +3 dB or more at every pair listed;
  - the slurred eighth's 60 ms peak stays within 1 dB;
  - the phrase-end falls in the master are unchanged.
- Add Flute 1, Flute 2, Oboe 1 and Clarinet 2 at 318-354 / 918-954 to the first check of every cycle.

### 2. Accents on sustain rows have no front: the note's first 80 ms is 2-3.6 dB under its body, and the weight peaks 0.23-0.27 s after the beat. Accents read as late swells, and they sit under the staccato before them (measured; cause partly inferred)

Where: accented half and dotted-half notes on "Sus MAX" / "Leg Slur Rep":
- Violins I and II: 123, 207, 213, 315, 327, 345, 351, 819, 891, 897, 915, 927, 945, 951, 999;
- violas;
- cor anglais (all 16 measurable accents);
- Clarinet 2 (315 ... 951);
- Oboe 1 on Sus MAX (207, 819, 891).

Evidence (measured on c25):

| track | accent over the detached note before (acc2) | peak after the beat | first 100 ms minus 150-350 ms |
|---|---|---|---|
| Violins I | -3.2 dB | 0.25 s | -3.0 |
| Violins II | -3.2 | 0.27 | -3.2 |
| cor anglais | -2.3 | 0.23 | -2.0 |
| Clarinet 2 | -5.4 | 0.28 | -1.6 |
| violas | -0.4 | 0.14 | -1.6 |
| Flute 1 ("Sus Accent MAX") | -0.1 | 0.06 | **+0.9** |
| Oboe 1 accents on "Sus Accent MAX" | | 0.00-0.04 | **+1.3..+4.4** |
| Oboe 1 accents on Sus MAX (207, 819, 891) | -5.5..-5.8 | 0.16-0.38 | |

- My own spectral measure on the long accented notes: first 80 ms against 150-400 ms. Broadband -1.9 to -3.6 dB on every family. 2-5 kHz -4 to -9 dB (Violins I -8.0, celli -8.6, cor anglais -9.0). There is no bite anywhere (Dan's rule holds), but there is also no front.
- Why (measured in parts.json, cause inferred):
  - `VOL_CLASSES = ("slow",)` leaves the accent swells and the accent body cuts unwritten. Violins I's `vol_tags` show `shape:accent` 40 and `shape:accent_body` 11, and none of them reaches the envelope. `build/accent_bodies.json` (the c05 hemiola body cuts) has therefore done nothing since c15.
  - What remains is the ACCENT_CC bump. It starts at the moved note-on or 0.01 qn before the score onset, holds 0.08 s and releases over 0.20 s (`_acc17`, `pre_s` 0).
  - Opus fades a CC11 change over about 120 ms (c22 learning), so the bump takes effect at +0.1..+0.3 s, the same time the sustain samples bloom.
  - The cor anglais has no bump at all (add 0 / 0) and still peaks at 0.23 s: the bloom is the sample's.

Fix (instrument side, CC11 only, in the same lane as the existing bump):
- `tools/score_to_parts.py` `_acc_cc_build`: new optional ACCENT_CC keys `"body_cc"` (units, negative) and `"body_s"` (start, full).
  - After the bump's release, CC11 sits at the resting value plus body_cc. The dip ramps in from onset + body_s[0] and is full by onset + body_s[1].
  - It holds to the next moved onset - 0.02 qn and is back at the resting value at that onset.
  - Apply it only on accented notes written 0.42 s or longer that are not legato targets.
  - This is the old ACCENT_BODY shape moved from the envelope into CC11, inside Opus, so the hall keeps the front.
- `build/score_config.py` ACCENT_CC values:
  - Violins I, Violins II, violas: `"body_cc": -8, "body_s": (0.22, 0.36)`, which is about -2.5 dB at a resting 90-104 at 0.3 dB per unit. Use -4 where the resting CC11 is under 60 (0.4-0.5 dB per unit); add a `"body_soft"` key, or reuse `soft_cc`.
  - Cor anglais, Clarinet 2, and Oboe 1 (its Sus MAX accents): `"body_cc": -6`.
  - On the strings also `"pre_s": 0.06`, so that CC11 is already up when Opus picks the group at the note-on. `from_moved` stays.
  - Remove `build/accent_bodies.json`'s entries, or mark them dead.
- Acceptance (range test 312-360 and 912-960, same-start control):
  - first 100 ms minus 150-350 ms at +0.5 dB or more;
  - peak at 0.12 s or earlier (median);
  - accent over the detached note before +1.0..+2.0 dB median, none over +3 (Dan's target);
  - 2-5 kHz front minus body not above 0 dB.

### 3. Seventeen of the rerouted Spiccato notes were not moved into the cut layer: they still sound as unprinted accents, +2.6 dB median over their neighbours, up to +5.9 (measured)

Where: Violins I notes `STAC_ROW_BY_PITCH` sends to "Spiccato RRx9" whose original velocity was 67-87:
- the counterstatement, 115-128;
- 294-299;
- the reprise, 774-775 and **817-824**;
- the coda, **988**.

Evidence (measured):
- The c25 block's comment says the rerouted notes under v90 "all play the 1-54 layer". They do not. Velocity 67-87 less 13 is 54-74, and 17 notes land in the uncut 55-89 layer.
- Over their short neighbours within ±3 qn (70 ms peaks), by the layer each note now plays:

  | layer | notes | median over neighbours | over +3 dB |
  |---|---|---|---|
  | v<55 | 27 | -1.1 | 3 |
  | **v55-74** | **17** | **+2.6** | **7** |
  | v>=90 (cut 4 dB) | 24 | +0.9 | 6 |

- Worst notes:
  - 817.5 +5.1, 823 +4.6, 823.5 +5.7, 824 +5.9 (reprise, original v87);
  - 988 +4.2, 988.5 +3.4 (coda, v82);
  - 127-128 +2.1..+3.2 (counterstatement, v87).
- Tone is not the problem: the spectral centroid of the moved notes is 1.04-1.09 times their neighbours' in every layer.

Fix, with no tool change, in `build/score_config.py` (c25 block). `score_to_parts.py` (line 3646) takes the first matching row whose 5th value is above the note's velocity. Split each pitch range into three rows:

```
(74, 75, "Spiccato RRx9", -13, 67), (74, 75, "Spiccato RRx9", -20, 80), (74, 75, "Spiccato RRx9", -33, 90),
(78, 78, "Spiccato RRx9", -13, 67), (78, 78, "Spiccato RRx9", -20, 80), (78, 78, "Spiccato RRx9", -33, 90)
```

- v67 becomes 47, v70 50, v81 48, v84 51, v87 54: every rerouted note under 90 then plays the 1-54 layer (cut 2 dB). The order is kept except v67-70 against v81-87, which never sit in one phrase.
- Acceptance: these 17 notes -1..+1.5 dB over their neighbours. The F sharp at 342 / 942 stays under the accented C (now -27.8 / -26.9). Separation at D5 / D sharp 5 / F sharp 5 stays at 4.5 dB or more (c25 4.8-6.1).

### 4. Violins I's isolated staccato quarters still ring 280-285 ms to -20 dB, 60-75 ms longer than every other string section; c25 did not run last cycle's fix (measured, fix inferred)

Where: Violins I staccato quarters before rests or leaps. These are the theme-head quarters, and the phrase ends at 81, 95, 165, 393, 801, 827, 861 and 957, which belong to Dan's "lasting too long" family.

Evidence (c25, short-row notes with 0.4 s or more to the next note):

| track (row) | onset to -20 dB under the peak | peak after the note-on |
|---|---|---|
| Violins I Stac RRx14 | **285 ms** | 120 ms |
| Violins I Staccatissimo RRx9 | **280 ms** | 80 ms |
| Violins II Stac RRx9 | 210 ms | 70 ms |
| violas Stac RRx9 | 220 ms | 105 ms |
| violas Staccatissimo RRx16 | 215 ms | 90 ms |
| celli Stac RRx9 | 255 ms | 100 ms |
| Oboe 1 Stac DblTng | 248 ms | 25 ms |

- The Violins I numbers are the same as c24's (283 / 285).
- The V1 samples peak at or after the written note-off (sounding 57-115 ms). That is why the earlier 150 ms caps cut their peaks (c21, c23).

Fix (as c25 A #4, still open):
- `STAC_MIN_SOUND_S` {"Violins I": 0.14} only for short-row notes with 0.2 s or more to the next note (the existing `STAC_MIN_SOUND_GAP_S` path), so eighth pairs keep their length.
- A 220 ms `sus_release_cap_ms` with `any_dyn` on "Staccatissimo RRx9" and "Stac RRx14" (Violins I). The orphan groups are already off, so the cap now reaches only the round-robin groups.
- Acceptance (range 84-132 and 950-960): 60 ms peaks within 0.5 dB of the control, onset to -20 dB at 230 ms or less, eighth-pair separation unchanged.

### 5. Celli trio tune: only 512 is capped. 510 and 528 took the full +0.08 s and are under-corrected, and the joins answer lead unevenly (542 moved 248 ms for 80 ms) (measured)

Where: Violoncellos "Leg Slur MAX", bars 169-192 (qn 504-576), v80 targets.

Evidence (c25 parts.json and pcx):

| join | lead c24 -> c25 | pcX c24 -> c25 | what limits it |
|---|---|---|---|
| 510 | 0.18 -> 0.26 s | +117 -> +79 ms | nothing: the cap is 0.325 s (0.75 x 0.433 s from 509's moved onset) |
| 512 | 0.127 s, unchanged | +105 -> +101 | **`LEG_MIN_GAP_AT` celli (504, 576, 0.06)**: 511.5's moved onset is only 0.187 s before 512 (511.5 has leg_leads -0.065, lead 0.055 s), and 0.187 - 0.06 = 0.127 |
| 528 | 0.20 -> 0.28 | +166 -> +93 | nothing below the 0.35 s `LEG_LEAD_CLAMP` |
| 516 | 0.205 -> 0.285 | +150 -> +70 | |
| 542 | 0.245 -> 0.325 | +159 -> **-89** | overshoot |

- Also late in c25: 514 +87 (lead 0.23), 519 +81 (0.18), 540 +73, 544 +95 (0.155), 570 +281 (0.275, capped near 0.343).
- So 80 ms of lead bought 38, 73, 80 and 248 ms at four joins. The response is not linear (per-join scatter, inferred to come from the transition samples).
- The old pitch swells after every target's note-on (median +5.9 dB within 0.25 s, the known join swell), but its size does not correlate with lateness (r = 0.06), so it does not explain the late joins.

Fix (`build/leg_leads.json` "Violoncellos"; totals stay inside the caps above):
- Change 511.5 from -0.065 to -0.025 (its pcX is +26 ms, so it can move). This opens 512 by 0.04 s; then add +0.04 at 512.
- 510 +0.06 (to 0.32 s), 528 +0.07 (to the 0.35 clamp), 514 +0.06, 519 +0.06, 544 +0.07, **542 -0.07** (back to about 0.255 s).
- Leave 570 (it is at its cap). Its +281 ms is the outlier, and the pair's bands show the new pitch overtaking the old only at +0.28 s after the note-on.
- Check with pcx: trio tune median +15 ms or less, 15 % or less over 60 ms, no join earlier than -40 ms. Keep c10's v80.

### 6. The E -> B residual at bars 117 / 317 is not a blur: the E5's own peak is 2.2 dB lower since c24 and B now stands further over the E's tail. The same kind of reading makes Violins II's 0.4-0.6 dB values look like blur (measured)

Where: Violins I qn 348 -> 349 and 948 -> 949 (E5 staccato quarter, B4 eighth). Violins II 343.5 -> 344, 943.5 -> 944 and 983 -> 983.5.

Evidence (c18 -> c25; data identical at these notes, except a keyswitch at 349.9 after the B ends):

| at 348 / 948 | c18 | c25 |
|---|---|---|
| E5 band peak | 30.5 | 26.6 |
| E5 band at the B's note-on | 16.2 | 17.0 |
| B4 band peak | 23.7 | 26.6 |
| **B peak over the E's tail at the B note-on** | **7.5 dB** | **9.6 dB** |

- fig25's "previous peak minus previous level at the crossover" fell 15.0 -> 11.0 only because the E's peak is lower.
- The E5 notes on Stac RRx14 / Staccatissimo lost 0.9 dB median in their 150 ms peak from c18 to c25 (-2.2 / -2.0 at 348 / 948, +2.1 / +2.2 at 341 / 941). This fits c24's orphan-group switch-off (inferred). The round-robin count per E5 note is unchanged (28th / 60th E5 in both renders).
- Violins II at 344 / 944 (A4 -> B4, 0.4 / 0.6 dB): the slurred A4 is 12 dB under the B4 and still rising when the B4 starts (peak +0.018 s after the B note-on). At 983.5 the F sharp peaks at the F's note-on, and 50 ms later the F is 9 dB over it.
- These values describe weak or late-peaking first notes, not tails that hang over the next note.

Fix (measurement only; no data change for 117 / 317):
- Add a second column to `fig25.py`: the next note's band peak in its first 100 ms, minus the previous pitch's band 40 ms after the next note-on.
- Accept a transition when either column holds within 2 dB of c25.
- Run fig25 with this column, and finding 1's measure, on the winds too.

## Not ranked

- The sfp at bar 301 (qn 900) is already a CC11 shape on every woodwind and string:
  - shape: 127 from the moved note-on, held to 900.45, down to 45-46 by 900.9, then the crescendo;
  - master: -16.9 dB at +0.18 s to -25.4 dB at +0.34 s, with the hall ringing; strings fall about 20 dB;
  - the deep troughs I saw in Clarinet 1 and Flute 1 are the gaps between their notes, not holes inside a note.
  - parts.json `vol_db` for Clarinet 1 still falls 4.8 dB over 900.0-900.5. If build_reaper writes that into the post-hall envelope rather than the CC7 lane, it is an S3 cut (B's lens: the guard).
- Phrase shapes: about 420 `hpgain` entries (printed hairpins) remain in the slow envelope and about 40 are in CC11 (`hp_to_cc11`). Dan allows hairpins as envelope ramps, so I propose no move for articulation reasons. The 13 guard notes are B's.
- Not re-measured this cycle (unchanged data since c24, attack probe clean): pizzicato / arco changes, harp, timpani rolls, con sordino, re-bows.

Do not touch:
- the strings' figure treatment (bar 23's CC11 lift and 0.10 s lead, the bar 38 / 263 lifts; Violins I bar 23 at 18.0 / 4.3 / 8.9 / 9.4 dB, nothing more than 2 dB under c24);
- the Spiccato route and the v95 / 1-54 layer cuts (only finding 3's 17 notes move);
- the orphan groups switched off on Violins I's short rows;
- Violins II's and violas' 150 ms short-row caps;
- the Flute 1 / Flute 2 / Oboe 1 "Sus Accent MAX" accents (the only front-loaded accents);
- the CC11 sfp shape at 900;
- the violins' legato leads (+5..+9 ms);
- c10's v80 celli targets and c15's v112 pickups.
