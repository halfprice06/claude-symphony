# Cycle 24, critic C (holistic): the c23 render

Lens: the whole movement as a conductor hears it. I compared c23 with the c00 port baseline, with c18 (five cycles back), with Movement I's latest render on the same tools (c61), and with the reference recordings (Dvořák 9/i; the Brahms band shares in metrics.md). All mp3 timings include the 0.30 s head. The scripts were scratch scripts and have been deleted. One of them was a copy of `tools/deliver_master.py` with an environment override for `TOP_ABOVE`; with the c23 settings it reproduced the c23 mp3 exactly (I -14.0, LRA 11.6, limiter 5.9 / 4.8 / 3.8, steps +3.4 / +1.2 / +1.1).

## Manual notes

MANUAL-READING.md has no row for cycle 24, so I picked the pages behind my top problems (PDF pages, as in DIGEST.md) and read them in full.

| Manual (May 2021 HO, PDF page) | Where it applies here | Followed? |
|---|---|---|
| p.91-92 Strings, Marcato Sustain: "plays a marcato sample in addition to the multiple sustain samples ... provides extra power at the start of the note"; one in each section (KS Master key 25 "Sus Marc LITE", enabled in all five string KS Masters) | the accented ff tutti chords held 1-4 qn: bars 1-2, 5-6, 94, 147, 273, 277 (Violins I/II, Violas, Celli) | No. Every one is on "Sus MAX", whose ff sample swells for 0.4 s (finding 1). |
| p.101 Brass Sustain: CC1 crossfades 4 dynamic layers that "all start to play simultaneously" | Horn 3's p inner line, bars 235-237 (G3 / A3 at CC1 36-39) | Partly. c23 raised CC11 only, which stays in the weak low layer (finding 4). |
| p.101 Brass "Sustain Marcato Long and Short": a marcato attack "not as forceful an attack as in the Sustain Accent patch"; velocity sets the low-pass cutoff on the marcato samples ("Marc Sus LITE", 1FH key 33, 1TB key 31, 1TU key 67, off in the KS Masters now) | brass in the same accented ff chords (Horn 1 peaks +364 ms after the beat in bar 1) | Not used. This is MANUAL-GAPS #1. At low velocity it is the gentle option Dan's accent rule asks for (optional part of finding 1). |
| p.101 Short articulations: no release trails; "play the MIDI notes in a connected fashion" | string staccato rows | Followed. Measured repeat separation on the stems is 13.6-19.2 dB median (below), so the scherzo's staccato-release finding does not apply here. |

MANUAL-GAPS.md: #1 (brass marcato attack) is still open and is the brass half of finding 1. TLeg hold / decay (c23) is still unmeasured; it belongs to lens A. #2 (re-tongue rows) is not needed after c23's chorale gaps.

## Where the movement stands (measured)

- **Large-scale shape (master).** Section loudness relative to the integrated level is within about 1 dB of c00 everywhere except T, the last bars (+4.6 -> +5.7). The cycles have changed detail, not the arc.
- **Shape on the mp3.** The delivery compresses that arc from 27 dB (master: L -21.6 to T +5.7 LU) to 10.7 dB (L -8.5 to T +2.2).
- **The loud half of the dynamic scale is flat.** I took the median momentary loudness per bar, grouped by the bar's prevailing printed dynamic:
  - c23 mp3: pp -22.4, p -18.3, mp -17.4, mf -14.9, f -13.9, ff -12.4, fff -8.2.
  - c23 master: f -24.8, ff -19.8.
  - f to ff is 5.0 dB on the master, 2.9 dB on c18's mp3 and 1.4 dB on the c23 mp3.
- **Weakest passages now:**
  1. the opening chords (bars 1-6), which swell instead of striking;
  2. the Allegro sections (A, B, F, K, R), which run at a fixed 84 with every ff stop on the grid;
  3. the f / ff tuttis (B, K, N, R), which on the mp3 are as loud as the f passages and within 0.8 dB of the fff close in mean loudness;
  4. the soft inner horn line of Q (bars 235-237);
  5. the violin cantabile passages (E, M, Q), which are 4 dB brighter above 6 kHz than Movement I and the recordings.
- **What no longer limits it (measured).** Loop pulsing on long holds: the master's 100-300 Hz band and centroid, folded at 3.95 s, show no pulse in P (autocorrelation -0.07 / -0.03). In T, the basses' and tuba's figures are the repeated eighths and quarters of the score, not sample loops. Repeat separation is fine: the basses' "Stac On Bow" eighths separate by 10-28 dB median per bar. Stops on the mp3 fall 14.8-16.1 dB.

## 1. The accented ff tutti chords swell for 0.3-0.5 s instead of striking, starting with the first sound of the movement (measured; fix inferred, range test first)

**Where.** Strings on the accented chords of 1-4 qn:
- qn 0 and 16 (bars 1 and 5; also qn 4 and 20);
- qn 372 (bar 94), 584 (bar 147), 1088 (bar 273), 1104 (bar 277).

All four string tracks play them on "Sus MAX" (vel 111, CC11 105 -> 110 then falling).

**Evidence.**
- Master, bar 1, 50 ms windows from the beat, dB relative to the 0.5 s maximum: -4.3, -1.9, -1.8, -1.5, -0.5, -0.3, -0.5, 0.0. The maximum comes at +475 ms (bar 5: +375 ms).
- Violins I start 11.4 dB under their own maximum and peak at +400-450 ms. Violins II and Violas behave the same way.
- CC11 falls through the note, so the swell is in the sample, not the controller.
- Of the 44 accented tutti chords (14 staves or more, 8 or more accented, held 1 qn or more), the master's peak comes a median 212 ms after the beat, and 45 % peak later than 250 ms.
- On strong onsets in the Dvořák recording the peak comes a median 125 ms after the onset, and 27 % peak later than 250 ms.
- What c23 measured as the opening chord's "126 ms spread" is mostly this slow body: the strings' first sound is led (-20 dB at -40..-48 ms) while their -6 dB point is at +112 / +130 ms. More lead would not help.
- Movement I c58 measured the same rows: Sus MAX quarters reach their level 160-220 ms late; on "Sus Marc LITE" with an 85 ms lead they reach it at +9..+51 ms.

**Fix.**
- `build/score_config.py` `ART_SPANS` on Violins I, Violins II, Violas and Violoncellos: "Sus Marc LITE" (key 25) for the chord notes only, at qn 0, 4, 16, 20, 372, 584, 1088, 1104, with a 0.085 s onset lead (Movement I c58).
- The LITE sustain body sits 7-9 dB under the marcato front on the violins (Movement I c55). Hold the ff body with a row region gain on that row's sustain groups (`region_gain_db` `{"rows": ["Sus Marc LITE"], "all_db": +4}`). Do not use a fader move.
- Targets (bars 1-6 range test first):
  - the master's maximum within 150 ms of the beat;
  - the first 50 ms within 2 dB of it;
  - the marcato front 2-4 dB over the body at 0.3-0.5 s (Dan's accent rule).
- Optional, brass, MANUAL-GAPS #1: the same onsets on "Marc Sus LITE" at velocity 60-70 (low-pass mostly closed, p.101). Horn 1 reaches its body -3 dB at +126 ms and peaks at +364 ms in bar 1.

## 2. The delivery makes f and ff the same loudness; let the top ride start higher (measured, simulated)

**Where.** The ff tuttis: B (bars 27-42), K (151-170), N (199-210), R (247-270), bars 1 / 5 against the fff at 223 and 278.

**Evidence (mp3).**
- f to ff is 1.4 dB (master 5.0) and mf to f 1.1 dB (master 2.4).
- Section B's mean is +1.4 LU above the integrated level, against T's +2.2.
- Bar 5 is 0.8 dB under bar 223 on the in-bar maxima.
- Cause: `TOP_ABOVE` -10 dB (2:1) starts the top ride about 7 dB under the ff level, so it takes 2.5-3.5 dB off every f-ff passage.

**Fix.** In `tools/deliver_master.py`, `TOP_ABOVE` -10 -> -6. Make it settable from mix.json `"deliver": {"top_above": -6}`, like `ratio`. Raise the quiet-lift `ratio` from 1.8 to 2.1 so p10 holds.

Simulated on the c23 master with the c23 ride rows:

| measure | c23 | simulated |
|---|---|---|
| integrated / true peak | -14.0 / -1.1 | -14.0 / -1.0 dBTP |
| LRA | 11.6 | 12.0 LU |
| p10 short-term | -22.4 | -22.5 LUFS |
| limiter, final / 223 / 263 | 5.9 / 4.8 / 3.8 | 5.8 / 5.5 / 4.5 dB |
| f to ff | 1.4 | 2.2 dB |
| bar 5 under bar 223 | 0.8 | 1.9 dB |
| B / R / T relative to I | +1.4 / +1.7 / +2.2 | +1.2 / +2.3 / +2.6 LU |
| in-bar steps 223 / 263 / final | +3.4 / +1.2 / +1.1 | +3.0 / +1.0 / +1.0 dB |
| D, L | unchanged | unchanged |

Variants:
- -6 without the ratio change: LRA 13.1, but p10 -23.7.
- -8: f to ff 2.2 with p10 -23.1.
- Ratio 1.5 alone: f to ff 2.1, limiter 6.2.

After the change, refit the 263 ride row by -0.3 dB to bring its step back to +1.2.

## 3. The Allegro is played on a click: no breath at the ff stops, no phrase motion (measured; listener effect inferred)

**Where.** A, B, F, K, N and R, which have no phrase arcs (score_config line 470: "no arc in the Allegro sections").

**Evidence (tempo map, half-note beats).**
- Exactly 84.0 over bars 40-48, 92-97 and 112-116.
- 1 beat of 557 is more than 15 % slower than its neighbours (bar 150, the printed rit.).
- The 90th percentile of beat deviation is 1.6 %. Research Part 5: Howl's 5 % and Mulan 8 %, with 20-26 breaths over 15 % slower.
- Movement I's map is the same (1.3 %, 4 breaths).
- The ff chord-stops followed by a subito soft entry get no time: bar 94 (qn 372) -> p at 376, and bar 113 (qn 448) -> p at 452. Real orchestras take a breath there.

**Fix (`build/score_config.py`; the tools already have these keys).**
- `BEAT_STRETCH` `{375.0: 0.90, 451.0: 0.90, 167.0: 0.95}`: about 40 ms before each subito entry.
- `PHRASE_ARCS` "light" arcs (0.99 / 0.975 on the last two beats, no push) on the Allegro's 16-qn phrases:
  - (40, 56), (56, 72);
  - (104, 120), (120, 136);
  - (328, 344), (344, 360);
  - (600, 616), (616, 632), (632, 648), (648, 664);
  - (984, 1000), (1000, 1016).
- An "open" arc (no slowing) on (1016, 1032) and none over the 1032-1048 build.
- Check that no arc touches a `RAMP_SPANS` start. The time added is about 20-40 ms per phrase.
- Rerun the c19 / c23 checks that depend on tempo (caesura gaps, entry leads) with `--midi-only --tempo`.

## 4. Horn 3's soft upper line in bars 235-237 is in the horn's weak layer; raise CC1, not CC11 (measured; value from Movement I)

**Where.** Horn 3 G3 / A3 against Horn 4 E3 / F3, p, qn 936-948.

**Evidence.**
- Horn 3 is 7.8 dB under Horn 4 (stem medians; c23's table gives 8.5).
- Both sit at CC1 36-39. c23 raised Horn 3's CC11 by 8 dB (34-46 -> 54-73).
- Movement I c59: the 1FH layer under CC1 about 50 is about 10 dB weaker from G-flat 3 up but not on F3 and below. A CC11 remap alone does not change the layer (manual p.101: CC1 crossfades the layers). CC1 42 -> 52 raised G3 by about 7 dB.

**Fix.**
- Horn 3 `cc_scale` on CC1 over 935.6-947.75: +12 units (36-39 -> 48-51).
- Take the CC11 lift back from +8 to +3 dB.
- Target: Horn 3 1-3 dB under Horn 4.

## 5. The violins are 4 dB brighter above 6 kHz than Movement I and the recordings; restore Movement I's violin shelves (measured; partial fix)

**Where.** The violin cantabile passages E (67-82), M (187-198), Q (235-246), and the mid-level music in general.

**Evidence (mp3).**
- In the mid-loudness 2 s windows, the 6-20 kHz share is -32.0 dB. Movement I c61: -35.9; Dvořák: -35.9; c00: -34.1.
- The 2-6 kHz share is -9.8 (-11.8 / -12.9 / -13.0).
- The violins carry 87 / 83 / 67 % of the 2-6 kHz energy in E / M / Q, and 92 / 92 / 85 % of 6-20 kHz.
- At equal stem level, the 6 kHz+ share against Movement I c61's stems:
  - Violins I: 3-6 dB higher (-22.5 against -25.8 at -38..-31 dB);
  - Violins II: 6-8 dB higher (-25.7 against -32.5).
- mix.json differs from Movement I's exactly here:
  - Violins I high shelf -4 dB at 5 kHz (Movement I -6);
  - Violins II none (Movement I -4).

**Fix.** mix.json `tracks` "Violins I" eq highshelf 5000 Hz -4 -> -6, and "Violins II" add highshelf 5000 Hz -4. These are track EQs, so `--mix-only` should be enough.

On the stems this takes the mid-level 6 kHz+ share from -28.3 to -29.6 dB (E -26.4 -> -27.8) and 2-6 kHz by 0.4 dB. That closes about a third of the gap. The rest is inferred to be the violins' CC1 (vibrato layer) and Close mic. Measure after this step before going further.

## 6. c23 items and the other movements' findings: what applies, with values

**Breath before 223 / 263 (inferred from the score: no breath is printed).**
- No caesura, fermata or breath mark is printed at 888 or 1048. The last breath marks are at 884 (Bn1, Cbn) and 1040-1044.
- At 888 the Flute 1 / Violins I scale (886.5-887.5) runs straight into the arrival. At 1048 the eighths of Clarinet 1, Violins II and the basses do.
- A 6 dB master hole would contradict that. Drop the 6 dB dip target and keep the 0.05-0.06 s caesuras.
- Judge the arrivals by the in-bar step on the mp3 (met: +3.4 / +1.2 / +1.1 dB) and by the attack shape (finding 1 applies at 1088 / 1104).

**Master sample peak 1.218.** A float stem sum on the final chord; the delivery limiter handles it (5.9 dB, 5.8 in finding 2). No action.

**Oboe 1, bars 143-144 (measured).** 1.0 dB under Clarinet 1. `cc_scale` +5 -> 0 dB gives the asked-for 5 under.

**Violins II against the violas, 920-936 (measured).** Median 3.1 dB under, within the 2-4 dB target. Keep.

**Opening chord spread.** See finding 1. Do not add leads.

**Scherzo findings:**
- Pre-fff delivery rides: applied in c23 and met.
- Slurred staccato pairs on Détaché: only 10 notes in the Finale (Violins I 6, celli 4). Does not apply.
- `any_dyn` cap: does not apply (c23).
- Range-render keyswitches: the procedure applies; keep `rangechk.py`.
- Staccato release caps: measured, does not apply. String staccato rows separate by 13.6-19.2 dB median; 3-5 notes per row are under 6 dB.
- Hall tail after loud stops on the mp3: 14.8-16.1 dB at +0.3 s. Met.
- Quietest music on the mp3: bar 97 -26.6 LUFS short-term, bars 7 / 123 / 175 -25.8..-26.0, p10 -22.4. About 12.5 LU under the programme. Acceptable; finding 2 keeps it.
- Phrase-rule swells on long held bass notes with no hairpin: 18 of 31 basses notes and 25 of 39 celli notes rise more than 4 dB after +0.3 s. The two largest are the build rule inside the retransition's printed crescendo (celli qn 568.9 +12 dB, 516 +11 dB, CC1 / CC11 76 -> 88) and the dal-niente pp pedal at 170.9. The rest are not reviewed (open).

**Do not touch:**
- the c23 fff ride rows and the -14 loudness loop (only `TOP_ABOVE` and `ratio` change, finding 2);
- the chorale's 0.12 / 0.08 s same-pitch gaps;
- the basses' "Stac On Bow" eighths (0.06 s lead, 90 ms release; separation 10-28 dB per bar);
- string staccato rows as they are;
- the hall and return levels (stops 14.8-16.1 dB on the mp3);
- the re-bow layout of the chorale and the final chord (no loop pulse);
- the trumpets' v95 off-beats;
- Violins II's 888-936 role split;
- the mp3 head of 0.30 s.
