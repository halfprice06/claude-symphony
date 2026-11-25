# Cycle 28, critic C (holistic comparison): the c27 render and its delivered mp3

Sources: `cycles/c27/scherzo-mockup-c27.mp3` against the c00, c18, c22 and c24 mp3s; the c27 and c18 stems and masters (the only cycles with stems; c27 numbers compared with c18 add back the global -3 dB); `cycles/c27/build_render/parts.json`; `build/mockup-events.tsv`; score page 4; Movement I c62 and Movement II c57 mp3s; the Dvořák 9/i reference (`symphony/render/assets/refs/`). Measured with my own scripts (ffmpeg ebur128 momentary loudness at 10 Hz, numpy FFT band shares, 10 ms and 50 ms envelopes on the stems). The mp3 lags the master by 239 samples; I allowed for it. "Measured" = a number from the files; "inferred" = reasoned, not tested.

## Manual notes

MANUAL-READING.md has no row for c28 ("cycles after c20 pick their own pages"). I read B3 (PDF p.123-126, timpani) and A6 (p.68-71, harp) in full, because the lens names "a harp that ticks" and the timpani is the longest-open library gap, plus p.93 and p.101 for the rows proposed in finding 1. MANUAL-GAPS.md read in full.

| Reading (PDF page) | Where it applies | Does the render follow it? |
|---|---|---|
| p.123-124: Timpani Felt KS. C0 long hits (LH C1-A2, RH C3-A4 variations), C#0 short, D0 flam, D#0 rolls on CC1 in 8 layers, E0 recorded crescendos; two notes within 65 ms trigger a double (damped) hit. | every timpani note | Partly. Long/short/roll rows and the LH/RH tables are used, and only one pair of notes is within 65 ms (the deliberate two-drum chord at 1014). The recorded crescendos (E0) are not used (MANUAL-GAPS #7). |
| p.125-126: Timpani Hard KS has the same five rows and keys; hard mallets give "a brighter timbre overall", rolls "with clear individual hits", and the short hits' stop "is more pronounced ... due to the strength of the initial attack". | the score prints "hard sticks" at bar 1 and "soft sticks" at bar 341 | **No.** Felt throughout (finding 2). Measured: Allegro strokes carry 1-5 kHz shares of -18..-29 dB in their first 50 ms and almost all their energy under 150 Hz. |
| p.68-70: Harp "Sustain RR": pluck and thumb pick alternate by round robin at velocities 1-123 (5 dynamic layers), nail pick at 124-127. | the trio's off-beat chords, codetta, Meno mosso | Yes. Velocities 40-42 everywhere: never the nail pick. Measured: the 1 ms peak sits +8.1..+9.1 dB over the 70-200 ms body and the 2-5 kHz share of the first 90 ms is -24.7..-29.8 dB in all four passages. **The harp does not tick.** It is identical to c18 apart from the global -3 dB. |
| p.70: Harp "Repetition Rep" lets earlier notes ring when the same notes repeat. | the repeated off-beat chords | Not needed: the chords are 0.26 s apart and the RR alternation already varies them. |
| p.93: Basses (and 2nd Violins) have "Marcato Long": a strong attack with a slightly longer duration than Marcato. | the basses' tenuto downbeat quarters in the ff tuttis | Not used: they play "Sus MAX" (finding 1). |
| p.101: brass Portato: "holds each note its full length ... without tying it ... not staccato"; Sustain Marcato: a marcato attack "not as forceful" as Sustain Accent. | the trombones', bass trombone's and tuba's tenuto downbeat quarters in 105-120 | Not used: "Sus MAX" (finding 1). MANUAL-GAPS #10 has been open since c00. |
| MANUAL-GAPS #6 (hard sticks), #9 (half-section basses div.), #10 (portato rows for tenutos) | as above | #6 and #10 are still open; finding 1 uses #10, finding 2 is #6. |

## The movement as a whole on the delivered mp3 (measured)

Mean momentary loudness per section (LUFS; c00 is the undelivered port at -20 LUFS):

| section | c00 | c18 | c22 | c24 | c27 |
|---|---|---|---|---|---|
| intro 1-12 | -25.8 | -18.2 | -16.9 | -16.9 | -16.9 |
| theme A 13-28 | -25.4 | -17.2 | -16.1 | -16.3 | **-16.8** |
| counterstatement 29-44 | -22.2 | -14.5 | -14.4 | -14.2 | -14.3 |
| fugato 57-72 | -22.4 | -14.1 | -14.7 | -14.6 | **-15.0** |
| ritmo di tre battute 89-100 | -28.0 | -19.5 | -18.9 | -18.7 | **-19.3** |
| tutti 101-120 | -16.0 | -9.7 | -9.6 | -9.6 | -9.7 |
| link 141-152 | -25.1 | -20.0 | -18.7 | -18.7 | -18.7 |
| trio, clarinet tune 153-168 | -22.2 | -17.0 | -15.9 | -15.8 | -15.8 |
| trio, celli tune 169-184 | -23.5 | -16.0 | -14.4 | -14.6 | -14.6 |
| trio ff 209-224 | -19.6 | -13.8 | -13.7 | -13.6 | -13.5 |
| codetta 225-240 | -23.5 | -18.8 | -17.6 | -17.4 | -17.6 |
| reprise 253-276 | -22.9 | -14.7 | -14.7 | -14.6 | -14.9 |
| tutti 301-320 | -15.6 | -10.3 | -9.9 | -9.9 | -10.1 |
| coda build 325-335 | -19.0 | -11.6 | -12.6 | -12.8 | -12.7 |
| summit 336-339 | -8.6 | -7.5 | -7.9 | -7.8 | -7.9 |
| Meno mosso 341-348 / solo 349-356 | -26.6 / -24.9 | -19.9 / -17.1 | -19.1 / -15.7 | -19.1 / -15.8 | -19.1 / -15.2 |
| close 364-376 | -30.9 | -20.8 | -19.1 | -19.3 | -19.3 |

- **Improved since c18.**
  - Every quiet section is 0.8-1.9 LU louder: intro, link, codetta, accelerando, close, the solo +1.9.
  - The coda now builds: bars 331-336 read -12.3 / -10.7 / -9.5 / -9.3 / -8.0 / -7.7 (c18: -10.8 / -8.8 / -8.0 / -8.0 / -7.3 / -7.3, a plateau).
  - The trio's cantabile lines are steadier, by the note-body level jump (median / jumps over 6 dB):
    - Clarinet 1 ff return: 2.8 / 3 -> 2.0 / 2;
    - Oboe 1 middle part: swells over +5 dB 7 -> 4;
    - the soft legato heads arrive 80 ms sooner (c27 records).
  - No loop pulsing on the held notes: Violins I bars 364-374 has a detrended level std of 2.4 dB and an autocorrelation at 3.95 s of +0.22, as on c18.
- **Worse or unchanged since c18 / c24.**
  - LRA 12.0 -> 10.6 (spec floor). Holding that floor cost the fugato 1.3-2.3 LU per bar against c24 (bars 57-66 and 289-294; the delivery ride +1.5 -> +0.5 of c26).
  - Theme A's Violins I is 2.0-3.8 dB lower than c18 in bars 21-23 and 27 (net of the -3 dB; the Spiccato layer cuts and the -6 dB marcato layer). The first statement still has the melody +2.9 dB over everything else (median per bar). The reprise does not (finding 4).
  - The summit leads the loudest tutti bar (104, -8.7) by 1.0 LU and bar 335 by 0.3 LU per bar mean. The ff tutti arrivals read softer than the crescendo bar before them: 105 -9.4 against 104 -8.7.
  - Weakest passages now:
    - the ff tuttis and the coda as rhythm: no one-in-a-bar (finding 1);
    - the Allegro's timpani colour (finding 2);
    - the celli's statement of the trio tune (finding 3);
    - the reprise of theme A, where the tune is covered (finding 4).
- **What still sounds like a machine.**
  - The second ff tutti is a sample-for-sample replay of the first on most strings and winds (finding 5).
  - The repeated staccato eighths of theme A do not repeat takes between statements: Violins I bars 13-20 against 253-260 correlates 0.41. Not a machine-gun problem.
  - The harp does not tick (above).

## Ranked findings

### 1. The ff tuttis have no one-in-a-bar: the downbeat is carried only by the bass group's tenuto quarters, and those play "Sus MAX" sustains that swell to their peak 95-170 ms after the beat (measured; fix effect inferred)

**Where.** Bars 105-120 (qn 312-360) and 305-320 (qn 912-960). Double basses, Contrabassoon, Tuba, Bass trombone, Trombones 1-2, Timpani: tenuto quarters on every downbeat, rests on beats 2-3 (events: `Cb 312 note 28 1.0 / script tenuto`, the same for Cbn, Tbn1 and Timp).

**Evidence (measured).**
- Downbeat weight on the mp3 (10 ms peak in the 90 ms after the downbeat minus beats 2-3, median per bar, broadband / 2-5 kHz):

  | passage | c18 | c24 | c27 |
  |---|---|---|---|
  | theme A 13-28 (p) | +2.6 / +3.6 | +2.4 / +3.3 | +2.5 / +3.2 |
  | ritmo di tre battute 89-100 | +2.4 / +1.7 | +2.0 / +0.7 | +2.6 / +0.9 |
  | tutti 105-120 | -0.1 / +1.5 | +0.3 / +0.4 | **+0.4 / +0.9** |
  | tutti 305-320 | +0.5 / +0.5 | +1.0 / +1.3 | **+0.9 / +1.0** |
  | coda 329-335 | -0.3 / -0.3 | -0.1 / +1.5 | **-0.4 / +0.9** |
  | trio ff 209-224 | +0.1 / +0.2 | +0.1 / +0.3 | -0.1 / +0.5 |

  The scherzo's loudest passages have less downbeat than its softest. c26-c27 worked on the upper strings' accents (body dip, violas' off-beat velocity). The master's tutti weight did not move.
- **The low band shows where the weight is missing.** Below 200 Hz, an 80 ms window on the downbeat against beats 2-3:
  - theme A +7.2 dB (pizz. basses); tuttis +2.6 / +2.4; c18 +2.7 / +2.9.
  - The low band's share of the downbeat is -6.7 dB at p and only -11.8 dB in the tuttis.
- **The bass group's attacks (c27 stems, 105-120, median).**

  | stem | peak after the downbeat (ms) | -6 dB point (ms) |
  |---|---|---|
  | Double basses (Sus MAX, v91, CC11 109-111) | +172 | -17 |
  | Trombone 1 | +166 | +21 |
  | Tuba (Sus MAX) | +162 | +30 |
  | Contrabassoon | +114 | -46 |
  | Bass trombone | +95 | -15 |
  | Timpani (felt) | +55 | +20 |
  | Trumpet 1 | +48 | -31 |

  The quarter lasts 227 ms, so the bass notes peak in their last quarter. The onsets are on time; the stroke is a swell.
- **What sounds through beats 2-3.** The tenor countermelody holds its level: celli -35.6 / -34.8 dB, Horn 3 -35.5 / -35.0, Bassoon 1 -39.5 / -37.2 (downbeat / beats 2-3). The basses' downbeat is -36.4 dB.

**Fix (instrument side: articulation rows, no level moves).**
- `build/score_config.py`, new block. Use `ART_SPANS` with a `"mark": "tenuto"` filter, as Violins I's staccato spans use `"mark": "staccato"`, on [311.9, 360) and [911.9, 960):
  - Double basses -> "Marc Lng RRx4" (manual p.93; in the Basses KS Master row list);
  - Tuba, Bass trombone, Trombone 1, Trombone 2 -> "Portato" (p.101; in the 1TU / 1TB KS Masters);
  - leave the contrabassoon on Sus MAX.
- Make it generic for later scores: in `tools/score_to_parts.py`, a rule `TENUTO_SHORT_ROW = {track: row}` for printed tenutos of 0.35 s or less at f or louder, default off.
- Range-test first: one 12 s range at 312-330, primed for the keyswitch (LEARNINGS c21).
  - Basses and low brass peak within +60 ms;
  - body level (60-200 ms) within 1.5 dB of the Sus MAX notes at the same CC11 / CC1;
  - no harder 2-5 kHz front than the trumpets' (score c200: weight, not bite).
- Targets on the full render:
  - tutti downbeat weight +2 dB or more broadband on the mp3;
  - low-band downbeat +5 dB or more;
  - Dan's bar 110 / 115 / 310 / 315 figure (A's measure) no more than 1 dB worse.
- Memory: two to five rows of RRx4 shorts. Check the settled footprint against 45 GB in the range pass.
- If "Marc Lng" bites on the basses, use "Detache" (Violins I uses it already).

### 2. The Allegro's timpani play felt sticks where the score prints hard sticks: every motive x stroke, the ritmo di tre battute heads and the tutti downbeats are woolly thumps (measured spectrum; benefit inferred; MANUAL-GAPS #6, open since c03)

**Where.** Every timpani note in bars 1-340: the motive x of bars 3-12, 91 / 94 / 97-100, 101-120, 285-320 and 329-339. The score prints "hard sticks" at bar 1, "medium sticks" later, and "soft sticks" from 341.

**Evidence (measured).**
- First 50 ms of the c27 timpani strokes:

  | passage | 1-5 kHz share (dB) | 20-150 Hz share (dB) | peak after the note-on (ms) |
  |---|---|---|---|
  | intro | -28.7 | -3.2 | +29 |
  | ritmo 89-100 | -19.8 | -3.8 | +15 |
  | tutti 105-120 | -17.8 | -3.8 | +55 |
  | coda | -19.9 | -3.7 | +52 |

- The stroke has no stick sound. It also adds low bass to the quiet passages: in the quietest quarter of the movement the timpani stem makes about a quarter of the 20-150 Hz energy (basses about 44 %, celli about 23 %; finding 6).
- Manual p.125: the Hard KS rows are the same five rows on the same keys, "brighter", with rolls of "clear individual hits". In a Beethoven 9/ii-style scherzo the timpani's motive is thematic and is heard as a stick stroke.

**Fix.**
- Swap the Timpani track to `Drums/Timpani/Timpani Hrd KS.oib`: one instance, no memory cost. `score_config.py` track table line 40; `KS_ALIASES` / the Flt row names in `score_to_parts.py` (`ks_lookup(stem, "Timpani Flt Lng")` and `TIMP_STAC_ROW` "Timpani Flt Sht") follow the patch stem.
- Accept hard sticks on the six "soft sticks" strokes of 341-376. They are pp / ppp "near the rim" at low velocity. Alternatively window 1020-1128 to a second instance only if memory allows (MANUAL-GAPS #6).
- Range-test the rolls and strokes first (rolls 300-309, 612-624, 900-909, 1002-1008; motive x 270-300). Refit `TIMP_CC1_MAP` / `TIMP_ROLL_TRIM_DB` and the `TIMP_RH_ALT` lh_vel_add table on that pass. They were fitted on the felt patch.
- Targets:
  - 1-5 kHz share of the stroke fronts -12 dB or more;
  - rolls under the texture as now (Dan's priority 5);
  - G.P. drop at bar 340 still 13 dB or more (the Hrd "Sht" stop is sharper, p.126).
- Of the six findings this one changes the most audible colour for the least work. Do it in c28 so that c29 has a render on which to refit the rolls.

### 3. The celli's statement of the trio tune (bars 169-184) still does not sing: every join dips 5.6 dB under the previous note, twice as deep as any other cantabile line, unchanged since c18 (measured; fix inferred)

**Where.** qn 504-552, Violoncellos on "Leg Slur MAX", CC11 55-67, v80 (v112 on wide leaps).

**Evidence (measured).** For each join: the lowest 50 ms level within -0.05..+0.2 s of the beat, and the highest within 0..+0.4 s, both against the previous note's body.

| line | dip, median (number under -8 dB) | swell, median (number over +5 dB) |
|---|---|---|
| celli tune 504-552, c18 | -5.7 (8) | +2.3 (9) |
| celli tune 504-552, c27 | **-5.6 (5)** | **+1.9 (9)** |
| Violins I 528-552 | -3.1 (0) | +1.6 (1) |
| Violins I ff 624-672 | -2.2 (0) | +1.9 (1) |
| Clarinet 1 456-504 | -2.8 (2) | +1.1 (5) |
| Clarinet 1 624-672 | -3.5 (0) | +1.2 (5) |
| Violin I solo 1044-1068 | -2.9 (0) | +2.8 (4) |

- On the 50 ms envelope, bars 174-175 run -48 / -54 (522) / -41 (523) / -54 (524) / -45 dB: a 13 dB "wah" across three notes.
- 524 (A sharp 3, v112) plays "Sus MAX" as a slur head (keyswitch Sus MAX at 523.514, Leg Slur at 524.404), and its first 0.2 s sits 5-10 dB under the notes around it.
- LEARNINGS c19-c21 record four failed controls on the **swell**: TLeg region gain, CC11 dip, attack cap, RELEASE. The **dip** has not been worked on.
- c14 measured Leg Slur MAX 6.2 dB weaker than "Leg BC MAX" over the first 0.5 s of celli notes. That is the size of this dip.

**Fix (range test; one row for the whole phrase).**
- `ART_SPANS["Violoncellos"]` "Leg BC MAX" on [503.9, 552.0) only. Check the row name in `ks_maps.json`; c14 unloaded it, so it loads again (one row).
- One row across the whole span avoids the mixed-row timing scatter that made c14 drop Leg BC. The keyswitch goes in the rest before 504.
- Then a two-pass `leg_leads` refit on that span alone (LEARNINGS c14: two passes converge, about 15 min).
- Targets: join dip median -3.5 dB or shallower, no dip under -8, swells over +5 no more than 5, crossover timing within ±25 ms.
- If Leg BC is not better on the range test: keep Leg Slur, and give the slur head 524 the same SOFT_LEG_HEAD_CC front as the rest heads, with `rest_qn` 0 for slur heads in 504-552.

### 4. In the reprise (bars 253-268) theme A is covered: Violins I sits 5.2 dB under the rest of the orchestra (median per bar, -10 dB at 266-268), and from bar 261 under Flute 1's p countermelody (measured)

**Where.** qn 756-804. Violins I mp leggiero (the theme). Flute 1 p leggiero from 780, A6-E6. Celli p, basses div. pizz. p.

**Evidence (measured, stems).**
- Melody over the sum of all other stems, median per bar: first statement (13-28) c18 +2.4, c27 +2.9; reprise (253-268) c18 -3.8, **c27 -5.2**.
- Per bar 261-267 (Violins I / Flute 1, dB, c27 + 3): -42/-39, -43/-37, -39/-35, -40/-35, -45/-40, -43/-38, -47/-41. That is Flute 1 3-6 dB over the theme.
- Violins I lost 1.5-3 dB against c18 in bars 259, 262, 264, 267: the c25-c27 Spiccato velocity -13 and layer cuts, applied for the tutti's hot F sharp, also act here.
- A p flute at A6 does carry. But the printed hierarchy is mp theme over p countermelody, and Dan asked for interesting lines to be heard, not to cover the tune.

**Fix.**
- A passage level, not per-note: `cc7_spans_db` Violins I [756, 804, +2.0] (CC7 carries passage levels).
- Or, if B prefers the flute side: Flute 1 [780, 804, -2.0] in CC7.
- Needs `--midi-only`.
- Target: Violins I over Flute 1 at least 0 dB per bar in 261-267; melody over the rest -3 dB or better (c18 level).

### 5. The second ff tutti is a sample-for-sample replay of the first (measured; audibility inferred)

**Evidence (measured).** Waveform correlation of bars 105-112 against 305-312 (best lag within 20 ms), c27 stems:
- Bassoon 1 0.998, violas 0.996, cor anglais 0.994, basses 0.994, Violins I 0.980, Oboe 1 0.953, Horn 3 0.923, Violins II 0.809, Flute 1 0.243;
- master 0.705, because the brass rests in 305-320.

The data is identical (Violins I 26 of 26 notes the same onset, pitch and velocity), and the round robins start on the same take. For the five woodwinds this is the c12 reset at 312 / 912; the strings arrive there in step. A real orchestra never repeats 16 bars identically. After 3 minutes, a listener who knows mockups hears a pasted copy.

**Fix (only if Dan's figure check passes).**
- Shift the take for the reprise: `RR_RESET_AT` on violas, Violins I, basses, Bassoon 1 and cor anglais at 909.0 instead of 912.0 (bar 304). The notes between 909 and 912 then advance the cycle, and the passage starts on a different take, still repeatable.
- Then check bars 310 / 315 / 317 against 110 / 115 / 117 with fig25 and A's measure. They have read alike because they are identical.
- If any reads more than 1 dB worse, revert. The identity is the lesser fault.
- Lowest priority of the six.

### 6. Quiet passages carry 5 dB more low bass and 2 dB less 500-2000 Hz than the reference: this is part of Dan's "detail hidden in quiet parts" on AirPods (measured; cause partly inferred)

**Evidence (measured).** Band shares of the quietest quarter of the mp3 by frame level (20-150 / 150-500 / 500-2k / 2-5k / 5-10k Hz, dB):

| file | 20-150 | 150-500 | 500-2k | 2-5k | 5-10k |
|---|---|---|---|---|---|
| Dvořák 9/i | -12.3 | -3.9 | -3.1 | -13.2 | -32.1 |
| Movement I c62 | -7.9 | -3.6 | -4.5 | -12.7 | -32.8 |
| Movement II c57 | -8.4 | -3.6 | -4.2 | -14.1 | -35.2 |
| scherzo c18 | -7.5 | -3.7 | -5.0 | -11.0 | -29.0 |
| scherzo c27 | **-7.3** | -3.5 | **-5.3** | -11.2 | -28.9 |

- The whole file and the loudest tenth match the reference within 2 dB. The quiet passages are the scherzo's heaviest in the shared pipeline.
- The quietest-quarter frames are mostly the close (84), the intro (43), theme A (38), the link (26) and the fugato (25).
- Their 20-150 Hz energy comes from the basses (about 44 %), the timpani (about 25 %) and the celli (about 23 %).

**Fix.** Finding 2 moves the timpani's part up the spectrum. Measure again after it. If the quietest quarter is still under -9 dB at 20-150 Hz, propose a mix-side low shelf for the Double basses' pizzicato spans. Do not cut the arco basses of the tuttis, which finding 1 needs. Bring in numbers from a render, not this estimate.

## Do not touch

- The delivery chain (-14 LUFS, peak compressor, room bed) and the hall: G.P. drop 17.2 dB, RT60 1.44-1.49 s on the mp3.
- The coda build rows (331-336 is a ramp now).
- The c26 woodwind figure state and the bar 23 state.
- The Spiccato split (but see finding 4 for its side effect in the reprise, fixed by a passage level, not by undoing it).
- SOFT_LEG_HEAD_CC and the celli RR resets before the ritmo di tre battute heads.
- The harp's velocities and patch (it does not tick).
- The Clarinet 1 and Violins I trio lines.
- stretch_cc7, the CC7 trim lane, and the 8 qn hold caps.
