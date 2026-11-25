# Cycle 23, critic C: tempo, timing and transitions (lens C3), on the c22 render

Material: `cycles/c22/render/` (master and 31 stems), `cycles/c22/scherzo-mockup-c22.mp3`, `cycles/c21/render/00_Master.wav` and `cycles/c21/scherzo-mockup-c21.mp3`, `cycles/c18/render/` (stems), `cycles/c22/build_render/` (parts.json, score_config.py, roles.json, mix.json as rendered), `build/mockup-events.tsv`, `tools/score_to_parts.py`, `tools/deliver_master.py`, `cycles/c22/CHANGES.md` and `records/fig23.txt`, `loop/ONE_TIME_c22.md`, and the c19 C report (this lens on c18).

Methods:
- I ran `cycles/c13/actor_scripts/timing13.py` (copied to scratch, unchanged except for its root path) on c18 and c22: 16 tracks over the Allegro sections, 2,680 readings each. "S" is the earlier of `pcx.attack_pcx` (perceived attack on the note's harmonic bands) and the crossover of the old and new pitch bands, in ms from the score onset.
- For single notes I also read the harmonic-band envelope directly: t50 (the time the attack is halfway up), and the peak time in the 0.45 s after the beat.
- 2-5 kHz beat contrast is the peak in the 90 ms after each beat minus the lowest level before the next beat. "Downbeat weight" is the downbeat's 90 ms peak minus the mean of beats 2 and 3. The mp3 is aligned to the master (it lags by 239 samples on both c21 and c22).
- Delivery variants ran `tools/deliver_master.py` unchanged on the c22 master with c22's parts.json, with only `DELIVER_PEAK_COMP` overridden. The baseline run reproduces the delivered file: -14.0 LUFS, LRA 10.6, limiter 2.7 dB, p10 -20.2.
- "Measured" means a number from the render, the data or a simulation; "inferred" means reasoned but not tested.

## Manual notes

MANUAL-READING.md has no row for cycle 23 ("cycles after c20 pick their own pages"). For the cycle note's Flute 1 question I chose D1 (May 2021 HO manual, PDF pages 53-54 and 64) and the woodwind pages 108-110 of A4, and read them in full. I also read MANUAL-GAPS.md.

| Manual (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| p.53-54: velocity controls the loudness of short notes and cannot change mid-note; CC1 and CC11 shape sustained notes mid-note | Flute 1's crescendos end on sustains shaped by CC11 (902-910), then the ff arrives on a staccato at velocity 112 (912). The two controls are set independently. | Partly. Each control is used as the manual says, but nothing matches the staccato's velocity to the sustain's CC11 at the arrival: a 9.5 dB peak step at 912 (finding 3). |
| p.64: on Opus Strings and Woodwinds, CC11 crossfades dynamics and loudness and CC1 sets vibrato; CC7 sets the level against other instruments, CC11 the shape | the whole pipeline (CC11 for shape, the volume envelope for slow balance) | Yes. Flute 1's CC1 follows CC11 through the crescendo (55 -> 95). |
| p.109: woodwind sustains play all three dynamic layers at once and the controller crossfades them, "so you can create a realistic crescendo during a held note" (the Mod Wheel wording is Play-era; Opus uses CC11, DIGEST section 11) | Flute 1 crescendos 300-310 and 900-910 | The controller works: I measured 0.155 dB per CC11 unit over 35 Flute 1 sustains. But the last 6 qn of each hairpin move CC11 only 94 -> 104, which is about 1.5 dB (finding 3). |
| p.110: short articulations have no release trails; hold the MIDI note long enough for the room to ring in the rests | theme-head staccatos and staccatissimos (114 ms MIDI length, a full eighth at quarter 264) | Yes. Short-note timing in the theme statements is unchanged from c18 (below). |
| p.108-110: the Sus Accent rows are not described in the 2021 pages; the rows exist in all four woodwind KS Masters (`mockup-kit/opus/ks_maps.json`: FL / OB / EH "Sus Accent MAX", CL "Sus Accent", key 25) | the accented tutti half notes of bars 106-118 and 306-318 (finding 2) | Used only on Flute 1 / 2 and four Oboe 1 p accents. |
| MANUAL-GAPS #2, #15 (repetition rows) | the theme head's repeated eighths | Not used, correctly: #15, and the rows are random per playback (T1 p.145, c19). |

## Checks the cycle note asked for

- **Bar 23 figure, first check:** finding 1. Nothing in the data is worse than c21. Bars 38 and 263 improved; bar 23 is unchanged and is still the worst occurrence.
- **Flute 1 crescendos (CC shape, row or target?):** finding 3. Mainly the CC shape and the arrival cap, together with a falling register that nothing compensates. The target is now right; the row costs about 2 dB.
- **Does the stronger delivery compression blur the tutti pulse?** Finding 4. Yes, by about 0.4-0.8 dB more than c21. Changing the compressor's timing does not recover it without breaking spec items, so the fix belongs in the source (finding 2).

## Findings, ranked by what a listener would gain

### 1. Bar 23: both slurred pair eighths reach their peaks only after the next note has started. This is the measured timing behind Dan's "blur together and overlap and last too long" (measured; the fix's effect is inferred)

**Where.** Violins I, bar 23 (qn 67.0 G5 and 67.5 A5, "Sus MAX", CC11 59 / 62, lead 60 ms), landing on B5 at 68 ("Staccatissimo RRx9", lead 45 ms).

**Evidence** (c22 stem, harmonic bands of each note, the previous pitch excluded):
- Bar 23: G t50 +4 ms, peak **+116 ms**; A t50 -24 ms, peak **+138 ms**. One eighth lasts 114 ms. So G is loudest at the moment A starts, and A is loudest 24 ms after B's beat. The notes touch in the MIDI: G ends 5 ms after A's note-on, and A ends 5 ms before B's.
- The same figure elsewhere:
  - bar 38 (c22 lift): G peak +64, A -10;
  - bar 263 (c22 lift): G +84, A +2;
  - tutti bars 115 / 315 (CC11 105, lead 30 ms): G +86..+88, A +26.
- Bar 23 is the only occurrence where both pair notes peak after the next note's beat. It is also the occurrence with the smallest decay before the next note-on in the actor's table (2.9 dB, against 5.1-11.2 elsewhere).
- The c22 CC11 lift made the soft Sus MAX samples peak earlier at 38 and 263 (it reached the louder, faster-speaking groups). At bar 23 it was rejected because the lift raised the preceding quarter's tail. A lead moves the attack without touching CC11.

**Fix** (`build/score_config.py`, Violins I only, bar 23 only):
- `LEAD_SET_AT["Violins I"]`: "67.0": 0.10 and "67.5": 0.10 (now 0.06 as rendered).
- `NOTE_END_AT["Violins I"]`: end 67.0 at 0.03 s before 67.5's moved note-on, and 67.5 at 0.03 s before 68's moved note-on (0.03 s is 0.13 qn at quarter 264).
- There is room for the earlier G: the staccatissimo F sharp at 66 ends 99 ms before G's present moved note-on, so 59 ms of silence remains.
- Print the realised lead next to the requested one (c19 rule). A `PREV_MIN_SOUND_S` cap must not swallow it.
- Targets on a range render of bars 21-25:
  - both pair peaks at +70 ms or earlier;
  - decay before the next note-on 5 dB or more at bar 23 (now 2.9);
  - F sharp -> G decay not under c21's 3.8 dB;
  - nothing worse at any other occurrence (they are not touched).

### 2. In the tutti statements the accented downbeat half notes swell into beat 2: the bar's weight arrives about 0.2-0.4 s after the downbeat. c21's extra 0.04 s lead moved their starts early, not their weight (measured)

**Where.** Bars 106, 110, 116, 118 (qn 315, 327, 345, 351) and 306, 310, 316, 318 (qn 915, 927, 945, 951). Each is an accented half note in Flute 1-2, Oboe 1, cor anglais, Clarinet 2, Violins I and Violins II, under tenuto quarters in the brass and low strings. On beat 2 only the violas play (a staccato double stop).

**Evidence.**
- Peak time in the 0.45 s after the downbeat, per stem (c22). Beat 2 falls at +227 ms:
  - Oboe 1 +350..+412 ms;
  - cor anglais +210..+368;
  - Clarinet 2 ("Leg Slur Rep") mostly +295..+363 (one +81);
  - Violins I +138..+420;
  - Violins II +184..+352.
  - Flute 1 on "Sus Accent MAX" peaks at +0..+126 (one note +307).
  The flutes are the only section whose accent lands on the beat.
- On the master, in bars 106, 110, 116, 118 and 310, the first 100 ms after the downbeat is 1.5-2.9 dB softer than 150-350 ms after it, with peaks at +166..+314 ms. Only bars 306, 316 and 318 have their weight on the beat. c18 read the same.
- Downbeat weight (2-5 kHz) on the master: tutti 105-120 +0.5 dB, tutti 305-320 +1.1, coda 329-336 0.0. Against that: theme A +3.4, reprise +2.6. This is c19's open finding 5, and it is now explained: the accented notes themselves build toward beat 2.
- c21's `ROW_CHANGE_ACC_ADD_S` 0.04 s (Clarinet 2, strings; Oboe 1 from c20) moved the onsets but not the peaks.
  - t50, c18 -> c22: Oboe 1 -8..-22 -> -18..-60 ms; Clarinet 2 -3..+11 -> -29..-73 ms.
  - timing13 S, c18 -> c22: Oboe 1 315 / 327 / 915 / 927: -13 / -25 / -14 / -25 -> -35 / -62 / -37 / -63; Clarinet 2: -7 / +9 / -7 / +9 -> -73 / -31 / -73 / -75; Violins I crossover: -64 / -98 / -64 / -100; Violins II: -88 / -64 / -78 / -64.
  - The peaks did not move (Oboe 1 +356..+398 -> +360..+412). Flutes and horns stay at 0..+36 ms.
  - So at the tutti downbeat the section onsets now spread over about 110 ms (at 315: c18 -38..+32, c22 -88..+24), and the weight still comes late.
  - In the Allegro the strings' sus joins over 60 ms rose from 9 to 25 (timing13). Most of the rise is these notes.

**Fix** (instrument side only, `build/score_config.py`).
- (a) Woodwinds: play the accented tutti half notes on the KS Masters' accent row:
  - `ART_AT`: Oboe 1 and cor anglais "Sus Accent MAX", Clarinet 1 / 2 "Sus Accent";
  - at qn 315, 327, 345, 351, 915, 927, 945, 951;
  - velocity 90 at f/ff and no CC11 bump on that row (`ACCENT_CC` skip_rows), as c22 set for the flutes;
  - remove `ROW_CHANGE_ACC_ADD_S` on these notes, back to the plain sustain lead (Oboe 1 0.04 s, Clarinet 2 0.035 s).
  - c21's range test rejected "Sus Accent MAX" on the cor anglais only at the p hemiola (bar 101). The f/ff tutti is a different layer (75-114 or 115-127), so test it separately.
- (b) Violins I / II: no row change (Sus Marc LITE failed on held chords in c22 and in finale c24). Shape the accented half note in CC11 instead:
  - hold the present CC11 to note-on + 0.05 s, then fall 10 units by + 0.25 s and hold to the end of the note, an accent's decay inside the note;
  - this takes the late swell out of the 150-350 ms window (inferred: about 1.6 dB at 0.16 dB per unit, plus a softer layer);
  - drop the 0.04 s `ROW_CHANGE_ACC_ADD_S` on these eight notes for Violins I / II (their crossover reads -64..-100 ms).
- Test on one range render of qn 312-360. Targets:
  - each of the eight bars' first 100 ms on the master at or above its 150-350 ms window (now -1.5..-2.9 dB);
  - tutti downbeat weight +1.5 dB or more;
  - section onsets at each tutti downbeat within 50 ms of each other;
  - peaks of the woodwind and violin accents at +150 ms or earlier;
  - accent medians inside Dan's +1..+2 dB (no level added: the fix moves the weight, it does not raise it).

### 3. Flute 1's crescendos into bars 105 and 305: the CC11 curve does 80 % of its rise in the first 4 of 10 qn, its top is capped near 104, and the melody falls 8 semitones. The target is now right (measured; the fix's effect is inferred)

**Where.** Flute 1, qn 300-312 and 900-912 (hemiola half notes on "Sus Accent MAX" at velocity 70 / 90, then the ff theme head on "Stac DblTng RRx9" at velocity 112).

**Evidence.**
- A level model from all 35 sustained Flute 1 notes of c22: body level less the envelope's vol_db, fitted by least squares on CC11 and pitch.
  - The fit gives 0.155 dB per CC11 unit and 0.65 dB per semitone, with a residual sd of 3.1 dB.
  - The hemiola notes sit 1.6-2.6 dB under the model. That is the accent row's body falling away after its attack: the row's cost.
- CC shape (parts.json):
  - CC11 46 -> 94 over 900.9-904.0 (and 300-304), then only 94 -> 104 over 904-910 (+1.2 dB by the model);
  - `dyn_curve` does reach 114 at 909.9 (c22's `HP_TARGET_LOOKAHEAD_QN` works), but the CC11 lane stops near 104;
  - Flute 1 is in `HP_GAIN_TO_CC11` with `max_arrival_cc` 100 (score_config, c18 block), so the hairpin's top is capped;
  - the envelope's +4 dB hairpin ramp adds only +2.2 dB over 904-910.
- Register: the line goes F6 D sharp 6 B5 A5 (904-910) and B5 A5 F sharp 5 D sharp 6 B5 A5 (300-310). Over 904-910 that is -5.2 dB by the model, against +1.2 (CC11) and +2.2 (envelope).
  - Instrument level at 904 / 906 / 908 / 910: -34.2 / -35.2 / -38.1 / -38.1 dB.
  - At 300-310: -40.7 / -40.1 / -42.0 / -35.0 / -37.8 / -38.8.
  - The stem is flat or falling while the score asks for a crescendo to ff.
- The step at 912: the E6 staccato at velocity 112 peaks at -20.8 dB, against -30.3 for the A5 sustain before it (9.5 dB). About 4.5 dB of that is register (7 semitones). The rest is the staccato's velocity against the sustain's CC11: the sustained E6 at 897 (CC11 101) peaks at -27.0, 6 dB under the staccato E6.

**Fix** (`build/score_config.py`).
- `HP_GAIN_TO_CC11["Flute 1"]`: `max_arrival_cc` 100 -> 124 for these two hairpins (or for Flute 1 as a whole, after checking its other converted hairpins).
- Shape the CC11 of the f -> ff part linearly in qn over 904-910 / 304-310: 94 -> 124 at the hairpin's stop, held to the ff.
- Predicted by the model: +4.6 dB more at 910 than now, so 902 -> 910 rises about +6 dB on the stem (c22 target) and the step at 912 falls to about 5 dB, of which 4.5 dB is register.
- If the step is still over 4 dB, check the "Stac DblTng RRx9" velocity groups in the FL KS Master (as finale technique 109 did for 1TP) and set 912 / 312 to the lowest velocity of the ff group, not 112.
- Do not compensate the register note by note: 8 semitones would need +34 units.
- Targets:
  - Flute 1 instrument level rising monotonically (note bodies) over 902-910 and 302-310, at least +5 dB from the first to the last hairpin note on the stem;
  - step at 912 / 312 at most 4 dB (peaks);
  - no change at the summit (1005-1014 are separate notes).

### 4. The stronger delivery compression takes 1.3-1.4 dB of beat contrast from the tuttis on the mp3 (c21: 0.5-1.0). Changing the compressor's timing recovers at most 0.4 dB and breaks a spec item, so leave the delivery alone and fix the source (measured, simulated)

**Evidence.** 2-5 kHz beat contrast, master -> mp3:

| | c21 | c22 |
|---|---|---|
| tutti 105-120 | 9.6 -> 8.6 | 9.7 -> 8.3 |
| tutti 305-320 | 10.0 -> 9.5 | 10.0 -> 8.7 |
| coda 329-336 | 7.8 -> 7.6 | 7.8 -> 7.3 |
| hemiola 301-304 | 5.8 -> 5.1 | 6.7 -> 5.8 |
| theme A (13-28) | unchanged | 12.3 -> 12.4 |
| trio 153-168 | unchanged | 4.2 -> 4.1 |

The quiet passages do not change. Downbeat weight on the mp3: theme A +3.4 -> +2.9, reprise +2.6 -> +2.4 (c21 lost nothing there); the tuttis +0.5 / +1.1 -> +1.3 / +0.7.

Delivery variants on the c22 master (all -14.0 LUFS):

| `DELIVER_PEAK_COMP` | beat contrast 105-120 / 305-320 / coda | LRA | limiter at the summit | summit lead (my M max per bar) | f -> ff |
|---|---|---|---|---|---|
| delivered: -9 dB 3:1, attack 2, release 60 | 8.3 / 8.7 / 7.3 | 10.6 | 2.7 | +0.38 | 2.25 |
| release 120 | 8.5 / 8.6 / 7.4 | **10.0** (fails item 6) | 2.6 | +0.52 | 2.10 |
| attack 8, release 120 | 8.6 / 9.1 / 7.3 | 11.0 | **4.1** | **+0.23** (fails item 2) | 2.27 |

**Fix.** None in `tools/deliver_master.py`.
- The tuttis' missing downbeat weight is in the master (finding 2: +0.5 / +1.1 dB, against +3.4 in theme A). The compressor's -0.4..-0.8 dB extra only adds to it.
- Once finding 2 puts the weight on the beat, re-measure these numbers on the mp3. A peak compressor reacting to a sharper downbeat may take a little more (inferred).

## Do not touch

- The tempo map: parts.json `tempo` (321 points) is identical in c18, c22 and build/. The fermatas, the poco rit. into the Trio, the trio rit. plus the accelerando curve, the Più mosso, the G.P. and the final rit. are as c15 checked them.
- The phrase end before the G.P.: master -15.6 dB at 0.3 s and -20.0 dB at 0.4 s after the bar 339 cut, the same as c18.
- The final fermata and the end of the file: identical to c18.
- The "ritmo di tre battute" grouping: master head bars over the bar after +3.8 / +6.2 / +1.0 dB (89 / 92 / 95); the printed f timpani bars 91 / 94 are the loudest, as printed.
- Short-note timing in the theme statements, unchanged from c18 (median S of short entries): Flute 1 +9, Flute 2 +17, Oboe 1 -6, cor anglais -6, Clarinet 2 -10, trumpets -9, Violins I +3, Violins II -10, violas -6, celli +3.
- The c22 CC11 lift on the bar 38 / 263 pairs (pair peaks -10 / +2 ms on the second note).
- The flutes' "Sus Accent MAX" accents (peaks +0..+126 ms).
- The delivery chain and its ride rows.
