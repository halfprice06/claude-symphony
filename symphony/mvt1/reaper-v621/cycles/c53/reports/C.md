# Critic C, cycle 53: blend and space (render c52)

Under review: `cycles/c52/render/` (40 instrument stems, 4 return stems, `00_Master.wav`) and the delivered `cycles/c52/mvt1-mockup-c52.mp3`, against c49 (the last cycle before the EW template), c51, and the stored reference metrics (Brahms 1/i, 1/ii, 4/i, 4/ii from Musopen; Dvořák 9/i, a lossy MP3).

Labels used below. Measured: computed from the audio or the build data. Simulated: computed by re-mixing the c52 stems (exact for return faders; a filter model for EQ, checked within 0.5 dB on the timpani side channel; a width model fitted to the c51 and c52 brass stems). Inferred: reasoning from those numbers. Nobody listened to anything.

## Manual notes

Pages are PDF pages of the May 2021 Hollywood Orchestra Opus manual. This cycle has no assigned row; I chose the pages behind the brass and percussion blend questions.

| Manual says (PDF page) | Where it applies here | Does the render follow it? |
|---|---|---|
| Hollywood Brass instruments share the same mic positions so that they blend; Solo Trumpet and 2 Trumpets are separate recordings (p.100) | Trumpets 1-3 use `1TP KS Master`, Trumpets a2 uses `2TP KS Master`, both Close -10.1 / Main 0 | Mic layout yes. The two patches end notes differently: the Solo Trumpet stems have almost no release (finding 2) |
| Brass shorts have no release trails, only some reverberation at the end of the sample; hold a last note long enough to let it ring (p.102) | Brass sustains do have release-trail groups (patch) | Solo Trumpet trail groups are 9-16 dB quieter than the 2 Trumpets' (patch); finding 2 |
| Tam-tams: long, short and crescendo keys, 12 velocity levels; crash pair: 3 lengths, 7 levels; suspended cymbal crescendos in 4 lengths (p.118-119) | Tam-tam from 277.0 s, suspended cymbal 352.5 s, crash 354.9 s | Yes. Main mic only, centred (R-L -0.6 to +0.3 dB), side/mid -3.6 to -4.1 dB |
| Close mics are in front of each section for presence; Main is a Decca tree at the fifth row with more room than direct sound; Surround is high at the back of the stage (p.138) | `mic_db` on every track | Mostly. Main leads on strings, brass, harp, percussion. Winds lead with Close (Close 0, Main -3.4 to -20.6), as in the EW template. Timpani has no Surround (template: Surround 0) |
| Each mic position has its own volume, pan and on/off (p.139) | `mic_db`, `pan_by_mic` | Yes |
| Channel Routing and Stereo Double set the stereo spread inside Opus (p.141) | Brass width | Not used. Width is REAPER `D_WIDTH` (`track_width`), whose law is not linear (finding 3) |
| FX bus sends have a POST switch; post-fader is usual for reverb (p.196, 198) | REAPER sends to the four returns | Yes, post-fader |
| Convolution reverb: pre-delay, true-stereo impulses, envelope on the impulse (p.220) | Spaces II on the returns (pre-delay 10-19.6 ms) | Yes, with the impulse cut to half length (`endPos` 0.5) |
| The room in the mics "is heard as long as the samples are playing (including the release trail samples)"; mic sliders set the near/far balance (p.222-223) | Note endings on dry stems: the tail is the release trail in the Main mic plus the return | Not for Trumpets 1-3 (finding 2). Mid mics on the woodwinds (`loop/MANUAL-GAPS.md` item 4) are still untried |

## EW-TEMPLATE-PLAN sections in this lens

- Section 1 (mic layout): applied, with two deviations: timpani Close -14 / Main -6 and no Surround (template Close -8 / Main -7 / Surround 0); harp Close -4.4 / Main 0 (template Close 0 / Main -9 / Mid 0).
- Section 2 (returns): applied with the return faders 8 / 12 / 4 / 4 dB under the template's (strings / brass / winds / percussion), the impulse cut to half, and the glue return (`R Glue`) off.
- Section 3 (section EQ and master EQ): applied. Brass and timpani bells and shelves are at about half the plan's values, the strings have no +4 dB shelf, the harp high-pass is 80 Hz instead of 183 Hz. The master EQ is applied only at delivery (`tools/deliver_master.py`), so `render/00_Master.wav` and the metrics made from it do not include it.
- Section 8: not applied: Duc's send profile (`R Duc` is defined, profile `ew` is in use), the basses EQ, the tutti entry spread, the room-noise bed.
- Section 9: applied: sends by register (trumpets -6 dB, low brass -10 dB; this is the cause of finding 1), the 2.3 kHz low-pass on each return, brass as narrow sources (c52 `track_width`).

## The four questions for this cycle

**1. Side bell -4.5 or -3.5 dB: keep -4.5 dB** (simulated on the c52 stems). Reference ranges: correlation below 250 Hz 0.54-0.62, 250 Hz-5 kHz 0.47-0.56, above 5 kHz 0.37-0.48, side/mid -4.7 to -5.4 dB.

| Variant | < 250 Hz | 250 Hz-5 kHz | > 5 kHz | side/mid dB |
|---|---|---|---|---|
| c52 as rendered | 0.589 | 0.566 | 0.495 | -5.53 |
| bell -4.0 | 0.568 | 0.563 | 0.495 | -5.46 |
| bell -3.5 | 0.545 | 0.560 | 0.495 | -5.38 |
| bell -3.0 | 0.521 | 0.557 | 0.495 | -5.29 |
| bell off | 0.335 | 0.536 | 0.495 | -4.67 |
| bell -4.5, trumpets 0.59, trombones 0.69 | 0.588 | 0.558 | 0.486 | -5.44 |
| bell -4.5, trumpets 0.65, trombones 0.75 | 0.587 | 0.551 | 0.478 | -5.37 |

One dB of bell moves the low band by 0.044, the mid band by 0.006 and side/mid by 0.15 dB. At -3.5 dB the mid band and side/mid reach the reference edges exactly, the low band falls to 0.545 (0.004 above the lowest reference), and the band above 5 kHz stays outside. The mid-band excess comes from the brass width, not from the bell (finding 3). Correcting the width puts all four figures inside the references with the bell unchanged.

**2. Is the brass in the same room as the rest after the width change: no** (measured). The early level is unchanged (0.05-0.15 s after a cut-off: brass -10.6 dB under the note body, c49 -9.8, strings -9.8, winds -12.7). The seats are within 1.6 dB of c49 (R-L: horns -4.5 dB, trumpets +3.9, trombones +5.0, tuba +7.0). The tail is not: 0.3-0.6 s after a cut-off the brass is 6.6 dB under the strings and 7.8 dB under the winds; in c49 it was 4 dB over the strings. The width change did not cause this (c51 has the same decay), but it narrowed the brass tail (side/mid -6.3 dB at 0.05-0.3 s, c51 -3.3, strings -6.1, winds -2.1). Findings 1 and 2.

**3. Wetness against c49: not wetter** (measured on the masters). At the one clean tutti cut-off (bar 169, 379.5 s) c52 is drier by 1.7 / 1.8 / 0.7 dB at 0.15-0.3 / 0.3-0.6 / 0.6-1.0 s; the level 0.3-0.6 s after the cut-off is 16.9 dB under the chord (c49 15.2; S4 asks for at least 13). At bars 31, 71 and 82, where other parts continue, c52 minus c49 is -0.5 to +0.4 dB at 0.3-0.6 s and +0.9 to +2.8 dB at 0.6-1.0 s. That later excess does not change when the string, wind and percussion returns are lowered 2-4 dB in simulation, so it is sounding notes and dry release, not return level. By family, strings, winds and percussion carry 1-5 dB more tail than in c49 and the brass 6-8 dB less.

**4. 6-20 kHz share:** -28.86 dB on the render master (the actor's -28.9), -28.50 dB on the delivered MP3, which has the master EQ's +0.8 dB shelf. The delivered figure is above all five references (-28.59 to -32.26) and 2.9 dB above c49's delivered file (-31.38). Finding 5.

## Findings

### 1. The brass tail is 6-8 dB shorter than in c49 and 7-8 dB under the strings and winds (bars 31, 71, 79, 82, 141, 169; all brass tracks, `R Brass`)

Level after cut-offs, dB under the note body, in the windows 0.05-0.15 / 0.15-0.30 / 0.30-0.60 / 0.60-1.00 s (medians; c52 family stems plus their return; measured):

| Family (cut-offs) | c52 | c49 | c52 minus c49, paired |
|---|---|---|---|
| strings (2) | -9.8 / -14.4 / -25.5 / -33.7 | -12.5 / -17.7 / -29.4 / -38.5 | +2.7 / +3.3 / +4.0 / +4.8 |
| winds (3) | -12.7 / -18.4 / -24.3 / -37.4 | -12.9 / -21.1 / -27.9 / -39.7 | +0.9 / +2.1 / +5.3 / +1.7 |
| timpani, percussion, harp (3) | -7.6 / -11.6 / -21.0 / -26.4 | -9.7 / -18.9 / -23.3 / -27.6 | +3.0 / +3.8 / +5.6 / +1.2 |
| brass (6) | -10.6 / -18.4 / -32.1 / -46.3 | -9.8 / -16.8 / -25.2 / -38.0 | -1.1 / -2.4 / -5.9 / -8.3 |
| horns, dry stems (5) | -9.1 / -16.1 / -32.4 / -47.0 | -8.6 / -16.1 / -26.4 / -36.9 | -0.2 / -0.5 / -5.1 / -9.7 |
| trombones, dry stems (11) | -10.6 / -21.5 / -33.9 / -46.5 | -10.0 / -18.7 / -27.0 / -37.7 | -0.8 / -2.1 / -7.6 / -9.6 |
| tuba, dry stem (7) | -13.5 / -31.6 / -43.9 / -58.1 | -11.3 / -20.4 / -26.8 / -40.0 | -2.2 / -11.6 / -16.9 / -18.2 |
| trumpets, dry stems (10) | -17.6 / -49.6 / -61.0 / -68.5 | -12.0 / -18.1 / -24.6 / -34.9 | -8.0 / -31.7 / -36.9 / -33.0 |

Cause (measured from `build/mix.json` and the stems): the `R Brass` return is 23.9 dB under the dry brass over the whole file (strings 13.7, winds 12.0, percussion 6.6). Its fader is 12 dB under the template's (c50 lowered it for the bar-14 horn ending), and the section-9 register offsets take the trumpets a further 6 dB and the low brass 10 dB down. Send plus fader: strings -12.5 dB, winds -11.3, horns -19.7, trumpets -25.7, low brass -29.7. The return adds 0.3-3 dB to the dry brass decay. The register rule comes from a project on a wet stage library; the plan itself says "or nothing, if the critics measure no loss of blend". This is that measurement: there is a loss of blend. `mockup-kit/LEARNINGS.md` (mvt II c09) also records that the Solo Trumpet needs more hall than the trombones.

Simulated on the c52 stems (uniform `R Brass` fader change; exact):

| `R Brass` fader | Brass decay, four windows | Brass tail side/mid, 0.05-0.3 / 0.3-0.6 s | Master minus c49 at 0.3-0.6 s, bars 31 / 71 / 82 / 169 | Bar 14 horn ending, time to -20 dB |
|---|---|---|---|---|
| +0 (c52) | -10.3 / -18.4 / -31.9 / -46.3 | -6.3 / -5.0 | +0.4 / +0.3 / -0.5 / -1.8 | 0.28 s |
| +4 | -10.3 / -18.1 / -30.6 / -43.7 | -6.0 / -3.9 | | 0.43 s |
| +6 | -10.3 / -17.9 / -29.6 / -42.5 | -5.8 / -3.2 | +0.4 / +0.4 / -0.4 / -1.6 | 0.51 s |
| +12 (template fader) | -9.9 / -16.6 / -26.0 / -38.0 | -4.7 / -1.6 | +0.5 / +0.7 / -0.2 / -1.0 | 0.61 s |
| c49 | -9.8 / -16.8 / -25.2 / -38.0 | -3.8 / -0.8 | | 0.27 s |

Even at +12 dB the master's level after the tutti stops changes by at most 0.8 dB and stays at or under c49 at bar 169, and the width figures stay as they are (0.584 / 0.558 / 0.495 / -5.43). The stored reference median for time to -20 dB after a cut-off is 0.485 s.

Fix, `build/mix.json`:
- `returns["R Brass"]["fader_db"]`: -10.97 to -4.97.
- `groups["horn"]`: add `"send_offset_db": {"R Brass": -2.0}` (the key the trumpet and lowbrass groups already use). Net horns +4 dB, so the bar-14 ending stays near 0.43 s.
- `groups["trumpet"]["send_offset_db"]["R Brass"]`: -6.0 to 0.0. Net +12 dB.
- `groups["lowbrass"]["send_offset_db"]["R Brass"]`: -10.0 to -4.0. Net +12 dB.

Expected (inferred from whole-file levels and the return's own decay; the return stem cannot be split by instrument): level 0.3-0.6 s after a cut-off about -28 dB for horns, -28 for trumpets, -30 for trombones, -31 for tuba, all still under their c49 values (-26.4, -24.6, -27.0, -26.8) and 2-6 dB under the c52 strings (-25.5). Each group rises by 12 dB at most, so the +12 dB row bounds the effect on the master. The return also moves toward the centre: it now sits at R-L -2.0 dB because the left-seated horns feed it 6-10 dB more than the right-seated brass.

Checks after the render: brass decay at 102.2, 183.8, 197.9, 204.1, 319.8, 379.5 s (0.3-0.6 s window between -26 and -30 dB); master at bar 169 no wetter than c49 (-15.2 dB at 0.3-0.6 s); bar 14 time to -20 dB at or under 0.49 s, measured full band from the cut-off near 66.3 s (the 250 Hz-5 kHz measure reads 0.64 s already in c52, because the dry Horn 1 stem itself falls slowly there). If bar 14 fails, set the horn offset to -4.0.

One conflict for the coordinator: BRIEF S4 says "Do not raise sends to win back depth". This change raises one return. It restores part of what the brass lost in the template change, and it keeps the brass family and the master at or under c49, which is the state after Dan's dial-back.

### 2. Trumpets 1-3 stop without any release (every Solo Trumpet note end; clearest at bars 31, 71, 82, 141, 169)

Measured: the three Solo Trumpet stems fall 45-50 dB within 180 ms of a note end and reach the noise floor by 0.5 s (table above: -49.6 dB at 0.15-0.30 s; trombones -21.5, horns -16.1). Trumpets a2, Solo Trombone and Solo Horn stems decay smoothly. c51 shows the same, so the c52 width change is not the cause. In c49 the Opus hall on each track covered this.

Patch data (read with `mockup-kit/opus/opus_state.py`, `1TP KS Master.oib`, row "Sus Non Vib MAX"): the release-trail groups have volumes 0.95 / 0.95 / 0.67 / 0.91 / 0.58. The same groups are 2.51-3.98 in `2TP KS Master`, 1.22-1.76 in `1TB KS Master`, 1.37-3.19 in `1FH KS Master`. That is 9-16 dB less trail than the 2 Trumpets and 3-13 dB less than the horn and trombone. It explains part of the missing tail. A 50 dB fall in 180 ms is more than this difference, so the full cause is not confirmed (inferred: the trail samples are quiet as well, or the trail does not trigger; the 1TP trail groups combine their start conditions with "And" on the Controller 1 range, the 2TP groups with "Or").

Fix: `build/mix.json`, tracks "Trumpet 1", "Trumpet 2", "Trumpet 3": add `"rt_gain_db": {"db": 9.0, "rows": ["Sus Non Vib MAX", "Leg Slur MAX"]}` (function `rt_gain` in `tools/build_reaper.py`; 0.95 becomes 2.68, 0.58 becomes 1.64, inside the range of the other brass patches). Test it in pass 2 on Trumpet 1 alone before the full render: the note that ends at 101.88 s (bar 31; velocity 83, CC1 81-88 to the end, no controller cut) should show about -20 to -25 dB at 0.15-0.30 s after the end instead of -49.6. If the stem does not change, the trail is not sounding; then leave `rt_gain_db` out and rely on the finding-1 send, which gives the trumpets a return tail of about -28 dB at 0.3-0.6 s (inferred).

### 3. REAPER's width control narrows the brass more than c52 intended (Trumpets 1-3, Trumpets a2, Trombones 1-2, Bass trombone)

Measured by fitting the c52 brass stems to the c51 stems: `D_WIDTH` w gives side/mid = tan(w x 45 degrees), not w. Width 0.5 gives 0.41 and 0.6 gives 0.51. The intended 0.5 and 0.6 need 0.59 and 0.69. Whole-file side/mid of the trumpets went from -2.6 dB (c51) to -8.3 dB, of the trombones from -3.1 to -7.0 dB. This is the reason the master's 250 Hz-5 kHz correlation, side/mid ratio and correlation above 5 kHz (0.566, -5.53 dB, 0.495) are outside the references.

Fix: `build/mix.json` `track_width`: Trumpet 1, 2, 3 and Trumpets a2 0.5 to 0.65; Trombone 1, Trombone 2, Bass trombone 0.6 to 0.75. Simulated master: 0.587 / 0.551 / 0.478 / -5.37, all four inside the references, with the side bell at -4.5 dB. With finding 1 as well: about 0.586 / 0.550 / 0.478 / -5.35 (sum of two simulated rows). The smaller step 0.59 / 0.69 leaves side/mid at -5.44 dB and the top band at 0.486, both just outside. Re-run the c52 range test (`cycles/c52/actor_scripts/widthtest52.py`) for the make-up `gain_db`: the level loss is smaller at the wider setting, so the make-up gains will be below c52's (+2.8 / +2.2 / +2.45, +2.5 on Trumpets a2, +1.3 / +1.75 / +1.65). The simulation does not model the make-up gains.

### 4. Low-mid build-up at 250-355 Hz in the delivered file; the master EQ cuts 167 Hz, which is already low (whole movement)

Measured on the delivered MP3 (share of total power): 250-500 Hz -5.51 dB, references -5.95 to -7.12 (0.44 dB over the highest). Third-octave bands: 250 Hz -12.1 (reference maximum -13.8), 315 Hz -9.7 (maximum -12.5, so 2.8 dB over), 125 Hz -17.0 (reference minimum -14.4, so 2.6 dB under every reference). The delivery chain adds to it: the render master has -6.37 dB at 250-500 Hz and the delivered file -5.51. The stems that carry 160-355 Hz: Violoncellos 28 %, Double basses 8, Violas 8, Timpani 7, Tuba 6. Third-octave figures depend on each piece's key, so treat the 315 Hz figure as a direction, not a target (inferred).

Below 250 Hz there is no build-up: 100-250 Hz is -8.39 dB (references -6.69 to -8.75) and 20-100 Hz is -17.1 dB, between the Dvořák MP3 (-22.1) and the Brahms recordings (-7.9 to -8.9). Those disagree by 13-14 dB; do not tune the bottom octave to either.

Fix: `build/mix.json` `master_eq`: replace the bell at 167 Hz, -1.6 dB, bandwidth 1.39 with a bell at 260 Hz, -2.0 dB, bandwidth 1.0. Simulated on the delivered spectrum: 250-500 Hz -6.07 dB (inside), 250 Hz band -13.0, 315 Hz band -10.5, 125 Hz band -16.0, 100-250 Hz about -7.9. The cello cut c52 deferred (bell 315 Hz, -3 dB, bandwidth 1.0 in `tracks["Violoncellos"]["eq"]`) adds only -0.17 dB at 250-500 Hz and -0.3 dB in the 315 Hz band (simulated exactly on the stems); it is optional. The master-EQ change needs no render: run `tools/deliver_master.py` on the c52 master and measure the delivered file. The ride and the limiter are not in my model, and BRIEF S4 already prefers cuts in 200-500 Hz to treble boosts for clarity.

### 5. The delivered file is brighter than every reference at 2-6 kHz and 6-20 kHz (whole movement)

Measured on the delivered MP3: 2-6 kHz -9.56 dB (references -10.39 to -12.43), 6-20 kHz -28.50 dB (references -28.59 to -32.26; c49 delivered -31.38). The actor's check uses the render master, before the master EQ's +0.8 dB shelf at 8 kHz. Stems that carry 6-20 kHz: Violins I 35 %, Trumpet 1 9.5, Trombone 1 7.3. At 2-6 kHz the energy is spread over the orchestra (Violins I 11 %, Violoncellos 10, Violins II 6), so the master EQ is the place to change it. Since c49 the 6-20 kHz share of single stems rose by 5.9 dB on the horns, 5.5 on Flute 1, 3.5 on the trombones: dry stems with family high shelves, and returns low-passed at 2.3 kHz. "Too bright" is inferred: the references are older recordings.

Fix: `build/mix.json` `master_eq`: replace the high shelf at 8008 Hz, +0.8 dB with a high shelf at 3000 Hz, -1.0 dB, bandwidth 1.39. Simulated: 2-6 kHz -9.88 dB, 6-20 kHz -29.84 dB. Smaller step: keep 8008 Hz and set it to -0.8 dB (6-20 kHz -29.09, 2-6 kHz unchanged). Measure the top-band share on the delivered file from now on, not only on the render master.

## Dan's checks

- S3 and S4 (measured): no forced stop rings less than in c49 by more than 1.3 dB at +0.3 s in 250 Hz-5 kHz (bars 14, 25, 31, 71, 82, 137, 141, 169: +12.6, +0.2, +3.0, -0.4, +1.3, -0.4, +1.7, -1.3 dB). The bar-14 figure is the slow fall of the dry Horn 1 stem.
- Item 8 (measured, 45 brass accents with a clear onset on the solo stems): 2-5 kHz level in the first 80 ms minus the note body has medians of -10 to 0 dB per instrument and a maximum of +5.2 dB (Trombone 1, bar 131). No harsh accent found.
- Item 7: a weak check only. In the few 10 s windows where the 100-300 Hz level stays within 15 dB (master 10, double basses 4, timpani 4, Violins I 1, bass clarinet 1) the band level shows no periodicity at 3.95 s. Held notes inside moving textures were not isolated.
- S1 and S2 were not measured by this critic. One observation for the critics who cover S2, not confirmed: at bars 25 and 137, beat 2, the horn and double-bass stems are near silent for 0.3-0.45 s after the MIDI note-on of the accented note (Horn 1: note-on 89.95 s, sound from about 90.26 s; Horn 3: 311.36 s and about 311.80 s). It may be an intended gap before the accent or an error in my time map there: isolated timpani strokes at bars 179 and 180 land on the mapped time, but strokes at other bars gave offsets between -185 and +875 ms, which my onset detector may have caused. For the same reason, treat the bar numbers in this report as approximate (up to one beat) and use the times in seconds; the levels and decays were measured from the audio and do not depend on the map.

Do not touch: the side EQ as it is (60 Hz shelf -3 dB and the 180 Hz bell at -4.5 dB); the `R Strings`, `R Winds` and `R Perc` faders and sends (lowering them 2-4 dB narrows the master to 0.573-0.577 at 250 Hz-5 kHz and does not shorten the tails at bars 31 and 82); the brass seats (`reaper_pan`); the Main-only, centred tam-tam and cymbals; the 2.3 kHz low-pass on the returns; the c52 315 Hz cuts on horns and violas; the ride, loudness gain and limiter in delivery.
