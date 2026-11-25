# Cycle 13, critic C: blend and space (lens C1), on the c12 render

Measured on `cycles/c12/render/` (31 stems, returns 91-94, master), the delivered `scherzo-mockup-c12.mp3`, `cycles/c12/build_render/parts.json`, `build/mix.json`, the installed DIV patch files, the Dvořák 9/i reference and the stored Brahms 1/ii and 4/ii metrics (`symphony/render/critics/c04/`). Levels are plain RMS dB. "L-R" is left level minus right level in dB. "Correlation" is the L/R correlation of a stem in 300 Hz-8 kHz. "Wet/dry" is a return stem's level minus the summed dry stems of the tracks that send to it, 200 Hz-5 kHz. Scratch scripts were in `/private/tmp/claude-501/mockup-loop/scherzo-c13-C/` (deleted).

Summary: the hall is consistent between families and inside Dan's limits, the low end is not built up, and the DIV tracks' tone matches their sections. The remaining problems in this lens are smaller than in c09. The largest is the placement of the woodwinds.

## Manual notes (cycle 13, slot C: group L2, May 2021 HO manual PDF pp. 219-223, read in full, pp. 220-221 also as images; MANUAL-GAPS.md read)

| manual (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| p.219: Algoverb, an algorithmic stereo reverb insert (pre-delay, size, decay, density, early/late ratio, mix). | A possible "glue" reverb over all families. The template's ALGO GLUE return (`R Glue`) is the same idea. | Not used. `R Glue` is disabled in mix.json. Nothing below needs it. |
| p.220: the convolution Reverb insert: Pre-Delay, Send Mono ("collapse the separate left and right channels of the impulse response"), true-stereo impulses, Bandpass with High Cut and Low Cut, Width 0-200 %, Wet and Dry. | The shared hall. The Opus reverb is off on every track. The four Spaces II returns carry the same controls: pre-delay 19.6 / 18.5 / 10 / 10 ms, a 180 Hz high-pass and a 5.6 kHz (strings 8.5 kHz) low-pass in ReaEQ. | Yes in level and decay. The stereo behaviour is not controlled: each return's left/right balance follows its source and adds a left offset (finding 4). |
| p.221: IR Envelope Preprocessing. Simple mode has one Decay slider. Full mode has start, end, fade-in and fade-out times and curves. | The returns' `irSetup` (envelopeMode 2, endPos 0.5, decayLength 0.5), which shortens the 3.3-3.4 s impulses. The G.P. after the fff (bar 340) and the final chord. | Yes. G.P. RT60 1.32-1.40 s, final chord inside Dan's limit (c12 CHANGES; re-measured below). |
| p.222: "What you are adding in or leaving out ... is the natural ambience of the room exactly as it occurred during the recording sessions. This ambience is heard as long as the samples are playing (including the release trail samples)." A piece can be made with one mic position; "the Main mics are a common choice", and Main is named as "the mic position that will dominate in the final mix". | Depth of each family. Strings and brass are Main-led (Close 4.5-10 dB under). Woodwinds are Close-led (Main 3.4-20.6 dB under, oboes -20.6). | Strings and brass yes. Woodwinds no: their recorded room is mostly left out, and Spaces II replaces it (findings 1 and 3). |
| pp.222-223: three ways to work with several mics: bounce each mic position in its own pass ("requires a smaller computer system", and the passes can be re-balanced afterwards), load all at once, or route each mic to its own output. | Memory is at the 45 GB cap. A mic change can be tested on one track in a short one-track render before it is used in the full render (LEARNINGS c08). | Partly. One-track test renders are used. Separate mic passes are not, and are not needed for the fixes below (the oboes' Main mic is already loaded at -20.6 dB). |

MANUAL-GAPS #13 (Mid instead of Close on the winds and horns) is still open and untested. Finding 1 uses the Main mic instead because it is already loaded.

## Is c12 too wet or too dry, and is the low end built up? (measured)

- G.P. after the fff (cut-off at qn 1015.8): family tails (dry stems plus the family's return) relative to the last 0.5 s:

  | family | +0.15 s | +0.3 s | +0.6 s | +1.0 s |
  |---|---|---|---|---|
  | strings + R Strings | -15.9 | -22.4 | -33.5 | -53.1 |
  | winds + R Winds | -19.1 | -23.3 | -34.6 | -52.4 |
  | brass + R Brass | -20.7 | -25.0 | -35.7 | -44.5 |
  | timpani, harp + R Perc | -21.5 | -26.3 | -42.6 | -65.9 |

  The families now decay together within 4 dB to +0.6 s. In c08 the trumpets were 11 dB below the strings at +0.3 s and the low brass 19 dB below at +0.6 s. c09's send changes hold.
- Six tutti cut-offs in the master (qn 166, 393, 550, 754, 861, 1015) against seven in the Dvořák recording, median drop per band:

  | band | mix +0.1 / +0.2 / +0.3 s | Dvořák +0.1 / +0.2 / +0.3 s |
  |---|---|---|
  | 40-100 Hz | -7.8 / -8.9 / -10.2 | -2.2 / -2.9 / -0.9 |
  | 100-250 Hz | -5.4 / -8.7 / -16.0 | -4.4 / -3.5 / -10.6 |
  | 250 Hz-1 kHz | -3.3 / -8.9 / -15.8 | -6.1 / -10.6 / -16.6 |
  | 1-6 kHz | -6.7 / -13.6 / -16.1 | -7.2 / -12.0 / -16.2 |

  From 250 Hz up the mix's cut-offs decay as the recording's do, within 1 dB at +0.3 s. Below 250 Hz the mix is drier than the recording by 5 dB or more. That is the result of the returns' 180 Hz high-pass and the low instruments' reduced sends, which were chosen against Dan's "mushy" note. It is not a defect to fix now. If Dan later calls the sound thin, the place to add hall is below 250 Hz (the returns' high-pass), not the level of the returns.
- Bar 56 after Dan's score change (tutti staccato at qn 165, then two beats of rest): the master falls 4 / 11 / 19 / 24 dB at +0.2 / +0.3 / +0.45 / +0.55 s after its peak. The loudest stem in the rest is the Double basses (-34.5 dB, R Strings -41.2): their G1 staccato holds its level for 0.2 s where Violins I has fallen 7 dB. The recording's low bands lag in the same way (table above), so this is left alone.
- Horn 1's staccato at qn 165: -40.4 dB in the first 100 ms against Horn 2 -44.5, Violins I -31.6, Double basses -30.6, Clarinet 2 -39.7. It is 4.1 dB over Horn 2 but 9 dB under the strings and level with Clarinet 2. By level it does not stand out (measured); no row is needed.
- Tutti band shares of the master (dB of the total): 100-250 Hz -8.4 / -8.3 / -7.8 in bars 101-120 / 301-320 / 329-339, 250-500 Hz -6.0 / -7.3 / -6.2. Dvořák's loudest 10 %: -6.2 and -6.5. The stored Brahms slow movements: -8.8 / -7.6 and -6.0 / -6.3. There is no 200-500 Hz build-up. The tuttis are 1.6-2.2 dB lighter than Dvořák's at 100-250 Hz. That band is carried by the celli (40-45 %), the basses (16-29 %) and the timpani (13-15 %); the horns give 1-2 % and the trombones and tuba 0-9 % (they are tacet in 305-320). A +4 dB bell at 170 Hz on all the brass and bassoons, simulated on the stems, moves the share by 0.2-0.4 dB. Do not chase this with EQ, and do not cut the low mids.
- The basses' div. pizz. octaves (bars 253-268): 100-250 Hz -8.8, 250-500 Hz -9.0 dB of the total; no build-up.
- Tone by loudness tier (1 s frames): the softest 30 % of the master has band shares within 2 dB of Dvořák's softest 30 % (2-6 kHz -12.4 against -13.6). The loudest 30 % has its spectral centroid at 1016 Hz against Dvořák's 853 Hz. That is for lens B and the pending delivery EQ variants (ONE_TIME_c13 item 6); a static master EQ cannot correct one tier without moving the other.
- Master stereo figures, whole file: correlation 0.54, side/mid -5.2 dB (Dvořák 0.56 / -5.3, Brahms 0.51-0.55 / -4.9..-5.4). L-R +1.24 dB (Dvořák +0.24, Brahms -0.41 and -0.04).

## Findings, ranked by what a listener would hear

### 1. The woodwinds are narrow points placed as far out as the outer string desks, and unison doublings are split left and right (counterstatement bars 29-44, qn 84-132; both tuttis, bars 105-120 and 305-320; trio bars 153-168; codetta 225-236) (stem positions measured; seat fix simulated; Main-mic step inferred)

What is wrong: in an orchestra the principal flute and oboe sit side by side in the middle of the stage, a metre or two apart, behind the strings. Here Flute 1 sits where the first violins sit and Oboe 1 where the double basses sit. Each is a near-mono point, while the string sections around them are wide. In the counterstatement Flute 1 and Oboe 1 play the theme head in unison (both E5 B4 B4 E5 at qn 84-86, read in parts.json). The doubling is heard as one instrument at the left and another at the right, not as one mixed wind colour answering the strings.

Evidence (measured on the c12 stems):

| track | seat in mix.json | whole-stem L-R | correlation, qn 84-132 | Main mic re Close |
|---|---|---|---|---|
| Flute 1 | -0.26 | +4.6 | 0.87 | -4.7 |
| Flute 2 | -0.30 | +3.3 | 0.79 | -3.4 |
| Oboe 1 | +0.28 | -5.2 | 0.99 | -20.6 |
| Oboe 2 | +0.36 | -6.5 | 0.98 | -20.6 |
| Cor anglais | +0.24 | -4.3 | 0.91 | -11.6 |
| Clarinet 1 / 2 | -0.22 / -0.20 | +3.0 / +2.5 | 0.86 / 0.87 | -3.4 |
| Bassoon 1 / 2 | +0.15 / +0.22 | -2.6 / -3.4 | 0.94 / 0.94 | -8.6 |
| Violins I | -0.31, REAPER pan -0.10 | +5.9 | 0.34 | Main-led |
| Violins II | | +3.3 | 0.48 | Main-led |
| Violoncellos | | -3.7 | 0.34 | Main-led |
| Double basses | | -5.1 | 0.66 | Main-led |

- Flute 1 (+4.6) is left of Violins II (+3.3) and 1.3 dB short of Violins I. Oboe 1 (-5.2) is as far right as the Double basses (-5.1). Flute 1 and Oboe 1 are 9.8 dB apart.
- The Close mic's position follows the seat exactly: L-R = 20 log10((1 - seat) / (1 + seat)) gives +4.6, -5.0, -6.5, -4.3, -2.6 dB for Flute 1, Oboe 1, Oboe 2, cor anglais and Bassoon 1, against measured +4.6, -5.2, -6.5, -4.3, -2.6. So a new seat can be set to a known result.
- The correlation follows the Main level within this render: Main at -3.4 dB gives 0.64-0.87, -4.7 gives 0.86-0.88, -8.6 gives 0.93-0.96, -11.6 gives 0.91-0.93, -20.6 gives 0.97-0.99. The strings read 0.3-0.5.
- These seats are the template's Close pans (EW-TEMPLATE-PLAN section 1). The numbers above are the measured reason to narrow them for this score.

Fix, step a (simulated): `build/mix.json` track `"seat"`: Flute 1 -0.26 -> -0.10, Flute 2 -0.30 -> -0.16, Oboe 1 +0.28 -> +0.10, Oboe 2 +0.36 -> +0.16, Clarinet 1 -0.22 -> -0.12, Clarinet 2 -0.20 -> -0.18, cor anglais +0.24 -> +0.22, Bassoon 1 +0.15 -> +0.12, Bassoon 2 +0.22 -> +0.18. Bass clarinet and contrabassoon stay. Predicted stem L-R: Flute 1 +1.7, Flute 2 +2.8, Oboe 1 -1.7, Oboe 2 -2.8, Clarinet 1 +2.1 dB. The seconds and the auxiliaries stay outside their principals, as they sit.
- Simulated on the c12 stems (each wind stem re-balanced to its new L-R at equal power, returns unchanged):

  | passage | wind sum L-R | master L-R | master pan spread (rtk definition; references 0.31-0.35) |
  |---|---|---|---|
  | counterstatement 84-132 | +1.3 -> +0.5 | +2.28 -> +1.90 | 0.354 -> 0.335 |
  | tutti 312-360 | +2.0 -> +1.0 | +1.39 -> +1.13 | 0.364 -> 0.351 |
  | trio 456-504 | +3.3 -> +1.6 | +3.26 -> +2.11 | 0.370 -> 0.334 |
  | codetta 672-708 | -0.6 -> -0.1 | +0.65 -> +1.00 | 0.356 -> 0.324 |

- The seat lives in the Opus state, so the wind tracks need the full rebuild they get anyway. Check each wind stem's K-weighted level against c12 after the build (a pan-law change of up to 0.3 dB is expected) and correct `gain_db` if a track moves more than 0.5 dB.

Fix, step b (inferred; test on one track first): raise the Main mic on the tracks where it is furthest down: `mic_db` Oboe 1 and Oboe 2 Main -20.6 -> -6.0, cor anglais -11.6 -> -6.0. The mic is already loaded, so memory does not change. From the relation above the correlation should fall from 0.98 to about 0.90. Render Oboe 1 alone first (bars 29-44 and 185-196) and keep the change only if the stem's correlation in qn 84-132 is 0.92 or lower, its 250-500 Hz share rises less than 1.5 dB, and its K-weighted level is given back in `gain_db`. If the oboe turns thick, stop at -9.
- This is c09's deferred item 1b with a narrower scope (three tracks) and a measured relation. The flutes, clarinets and bassoons stay.

### 2. The solo violin and the violas' upper div. voice are single-channel sources; the library's own widening tool has not been tried, and its key is now known (Violin I solo bars 349-356, qn 1044-1068; Violas div bars 209-224, qn 624-672, and 349-356) (measured; fix inferred)

What is wrong: both DIV tracks have a correlation of 1.00 (300 Hz-8 kHz) at every point they play. Each is one signal panned to a seat. In the trio's ff return the two viola voices are at the same level (Violas div -46.1 dB, Violas -45.9 dB in qn 624-672), one a point in the middle (L-R 0.0) and the other a wide section (correlation 0.43). In the solo the master's correlation is 0.78 for those eight bars, against 0.52-0.56 in every other section of the movement, so the picture narrows when the solo enters.

What is right and must stay: the solo's tone matches the section. Band levels relative to 1-2 kHz: solo 2-4 kHz -2.5, 4-6 kHz -13.0, 6-9 kHz -18.3 dB; Violins I at the same register (qn 624-672) -0.1, -10.7, -18.1 dB. The solo's hall is at -9.5 dB wet/dry (strings elsewhere -11.0), from c09's +3.6 dB send.

Evidence for the fix (read in the patch files): `1st Violins KS Master DIV A.oib` and `Violas KS Master DIV B.oib` each hold one Stereo Double processor, in `groups[0]` (named "Global Group"), `processors.processors[]`, class `"StereoDouble"`, label `"Stereo Double"`: `{"active": false, "direction": 0, "spread": 0.0, "left": true, "right": false}`. The patches expose it as automation parameters `"Stereo Double/active"` (label "SD On"), `"Stereo Double/spread"` ("SD Spread") and `"Stereo Double/direction"` ("SD Direction"). c09 looked for this key in the mixer channels' inserts and did not find it; it is in the group, not the mixer. The manual (p.141, read by c09) describes Stereo Double as the widener for a patch's stereo output.

Fix: in `tools/build_reaper.py` `apply_mix`, add a mix.json track key `"stereo_double": {"spread": 0.4}` that sets `active` true and `spread` on that processor in the instrument state. Set it on "Violin I solo" and "Violas div". Test with a one-track render of the Violin I solo before the full render.
- Keep it if: the stem's correlation in qn 1044-1068 falls to 0.60-0.90, its L-R stays within 1 dB of +5.9, the band levels above stay within 1 dB, and the stem shows no comb (no notch deeper than 6 dB in the mono sum's 1/3-octave spectrum against c12). Try spread 0.25 and 0.6 if 0.4 fails one of these.
- If the state key has no effect on the sound, set the three automation parameters by name from a bridge job at the pre-roll instead, and record the result in MANUAL-GAPS under #5.

### 3. The trio tune changes hall when it passes from the clarinet to the celli: the woodwinds' return is 1-3.5 dB higher against its dry sound than the strings' (bars 153-168 against 169-184; F major episode bars 73-88; Oboe 1 bars 185-196) (measured; fix by arithmetic)

Evidence (return level minus the dry sum of its senders, 200 Hz-5 kHz):

| passage | return | wet/dry |
|---|---|---|
| strings: theme 36-84, fugato 168-213, celli tune 504-552, trio ff 624-672, tutti 312-360 | R Strings | -11.6, -11.3, -11.0, -11.0, -10.9 |
| winds: F major 216-264 | R Winds | -7.5 |
| winds: clarinet tune 456-504 | R Winds | -8.6 |
| winds: Oboe 1 552-588, codetta 672-708 | R Winds | -9.2, -9.9 |
| winds: counterstatement 84-132, 1032-1044, tutti 312-360 | R Winds | -10.1, -10.3, -10.6 |
| brass: horn call 6-18, F major horns, tutti, coda, 1068-1089 | R Brass | -15.6, -14.7, -16.5, -16.7, -17.1 |

- The strings read -11.0 to -11.6 dB in every passage. The winds read -7.5 to -10.6, median -9.9. The tune T is heard with its hall at -8.6 dB (clarinet, San Francisco Hall impulse) and then at -11.0 dB (celli, S. Cal. Hall impulse) eight bars later.
- c09 raised the wind group's send by 3 dB on a simulation of send levels. Measured on the render, about half of that was needed.
- The brass return is 4-6 dB lower than the strings', but the brass stems carry their own Main-mic room and the family tails agree at the G.P. (table above). Leave the brass.

Fix: `build/mix.json` group "wind": `"send_offset_db": {"R Winds": 3.0}` -> `{"R Winds": 1.5}`. Bassoon 1 and Bassoon 2 keep their `sends` value. Predicted: wind wet/dry -9.0 to -12.1, median -11.4; the G.P. tail 0.4 dB lower at +0.3 s (R Winds is -55.0 dB of a tail whose parts sum to about -50; 20.5 -> about 20.9 dB drop). If step 1b is taken, the oboes and cor anglais gain room of their own, which is a second reason for this trim.
- This changes one of c09's "sends as rendered" (HISTORY do-not-touch) with the measured numbers above. The other c09 sends stay.
- The size is small: 1.5 dB of hall on one family. It is ranked third because it is audible only in the exposed wind passages.

### 4. Each return sits to the left of the instruments that feed it, and the harp is further left than the first violins (all returns; R Winds most; Harp in the F major tune, bars 73-80, qn 216-240) (measured)

Evidence:
- Per 5 s window, return L-R against the L-R of its dry senders: R Winds = 0.67 x dry + 1.85 dB; R Strings = 1.23 x dry + 0.65; R Brass = 0.73 x dry + 0.77; R Perc = 1.25 x dry + 0.57. Whole file: all returns +1.46 dB, all dry stems +1.00 dB, master +1.24 dB (references -0.4 to +0.24).
- R Winds in oboe-led passages: codetta (qn 672-708) dry -0.6, hall +2.0; qn 1032-1044 dry -2.3, hall -0.7; Oboe 1's middle part (qn 552-588) dry +1.8, hall +5.1. The oboe is right of centre and its hall is left of it.
- Harp, seat -0.72 (the template's Close pan): stem L-R in the tune +5.7 dB overall and +8.8 dB at 500 Hz-1 kHz (Violins I +5.3 dB there). Its hall in R Perc reads +11.1 dB in qn 216-240, the most one-sided signal in the mix, in the passage where the harp carries the tune.

Fix:
- `build/mix.json` `"returns"`: add `"pan"` (read by `template_mix.py`, written as the return track's `D_PAN`): R Winds about +0.15, R Strings, R Brass and R Perc about +0.05. Tune so that the median over 5 s windows of (return L-R minus dry L-R) is within 0.5 dB of zero for each return; the starting values assume REAPER's balance law is about 9 dB per unit near the centre and must be checked on the first render's return stems.
- "Harp" and "Harp harmonics": `"seat": -0.72` -> `-0.45`. Predicted Close L-R 15.8 -> 8.4 dB; the stem's 500 Hz-1 kHz L-R should fall to about +5, level with Violins I. The harp harmonics take over from the borrowed Violins II harmonic (L-R +3.3), so the handover gets closer in position too.
- Size: small. The returns are 11-17 dB under the dry sound, so the master's balance moves by about 0.1-0.2 dB. The gain is that each instrument's hall is centred on it.

## Standing checks in this lens (measured on c12)

- **Link handover (bars 147-151):** the borrowed Violins II harmonic reads -54 to -56 dB with R Strings 14 dB under it (qn 440-444). The harp harmonics enter at -43.6 dB with R Perc 14-16 dB under them. Hall level matches on both sides. The harmonics decay 10 dB in 0.54-0.58 s and 20 dB in 1.18 s, alike at 445, 451 and 1123.
- **Con sordino (Violins II 168-196):** 2-4 kHz is -12.4 dB relative to 250 Hz-1 kHz in qn 504-552, against -3.6 and -7.6 dB for the open Violins II (qn 84-132, 588-620). Correlation 0.53 against 0.42-0.48. The mute reads clearly and the track is in the same room.
- **S3 (subitos):** R Strings, R Winds and R Brass fall smoothly through qn 360 and 828 in 0.25 qn steps (R Strings -41.2, -41.5, -44.8, -46.6 across 360). No step, no cut tail.
- **S1 against the hall:** the dry line's pair dips (Violins I alone at 37, 43, 55: 5.7, 5.2, 7.3 dB; Flute 1 plus Oboe 1 at 85, 97: 4.9, 8.0 dB, 20 ms smoothing) lose 0.3-1.4 dB with R Strings added and 1.8-2.6 dB with R Winds added. The wind return fills wind repeats more than the string return fills string repeats. Finding 3 lowers it.
- **Timpani mics (template: Close -8.4, Main -6.9, Surround 0 dB):** on 14 isolated soft strokes the stick sound (1.5-7 kHz) is followed by energy 8-17 dB below its peak until the next stroke (windows to +140 ms). No later arrival is louder than the first, so the Surround mic does not double the attack. The timpani carry 54 % (bars 105-120) and 46 % (305-320) of the dry stems' 60-100 Hz. The kit README advises no Surround mic for the timpani; nothing measured in this lens requires the change, and dropping the mic would free memory for MANUAL-GAPS #6 (hard sticks) if lens B wants the 60-100 Hz share lower.
- **Not measured here:** loop pulsing folded at 3.95 s (item 8) and the legato joins of the seven tracks that were stale after the render. The c10 and c11 stems are no longer on disk, so the stale-track comparison cannot be made from this folder.

Do not touch:
- the returns' faders, 180 Hz high-pass and IR envelope 0.5 / 0.5 (mid and high cut-off decays equal the Dvořák recording within 1 dB; G.P. family tails agree within 4 dB);
- c09's sends for the trumpets, trombones, tuba, bassoons and the two DIV tracks, and the harp harmonics in R Perc;
- the low mids: no cut at 100-500 Hz, and no brass EQ to fill 100-250 Hz;
- the DIV tracks' shelves (the solo's tone matches Violins I within 2.5 dB per band);
- the strings' and brass's Main-at-seat ±0.8 layout and the brass track widths of c10;
- the Violins II con sordino lane, the borrowed Violins II harmonic and its role row;
- Horn 1's staccato at qn 165 (no trim);
- the bass staccato lengths at the tutti cut-offs.
