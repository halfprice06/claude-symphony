# Cycle 17, critic C: blend and space (lens C1), on the c16 render

Measured on `cycles/c16/render/` (31 stems, returns 91-94, master) against `cycles/c15/render/` and the c05 master, with `build/parts.json`, `build/mix.json`, the installed patch files (`.oib`, read with `opus_state.load_oib`), the Dvořák 9/i reference and the stored Brahms metrics (`symphony/render/critics/c04/`). Levels are mean-square dB (mean of the two channels' powers). "L-R" is left level minus right level. "Correlation" is the L/R correlation, 300 Hz-8 kHz unless a band is named. "Mono loss" is the level of (L+R)/2 minus the stereo level: 0 dB for identical channels, -3 dB for unrelated channels. Positions are score qn; bar b starts at qn 3(b-1). Scratch scripts were in `/private/tmp/claude-501/mockup-loop/scherzo-c17-C/` (deleted).

Summary: the hall is unchanged from c15 and inside Dan's limits, the lower resting CC11 at ff did not make anything duller or drier, and the low end is not built up. Three things in this lens are audible: Horn 1's G sharp, the movement's first and last sound, has its fundamental in anti-phase between left and right; the second instance on the last violin G sharp plays a thinner sample from its first bow change on; and the woodwinds have almost no stage sound of their own, so the picture narrows each time they play alone.

## Manual notes (cycle 17, slot C: group L1, May 2021 HO manual PDF pp. 138-139 and 141-142, read in full, p.138 also as an image; MANUAL-GAPS.md read)

| manual (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| p.138: Close mics "in front of each section", for presence. Mid "at the edge of the stage ... definition without the sound of close proximity". Main "in what would be the fifth row", "more room reflections than direct sound", a Decca tree with outriggers, "a big, unified sound". Surround "high up at the back of the stage", "lacks definition", adds depth when mixed in. | The depth of each family. Strings and brass are Main-led (Close 4.5-10 dB under). Woodwinds are Close-led (Main 3.4-20.6 dB under). Timpani: Surround 0, Main -6.9, Close -8.4 dB. DIV tracks: Close only. | Strings, brass, timpani: yes. Woodwinds: their stems carry 11-20 dB less room than the strings' (finding 3). Horn 1: the Main pair's outriggers put the G sharp 4 fundamental in anti-phase (finding 1). |
| p.139: each mic position is a sub-mix with its own volume, pan, on/off (loads or unloads the samples), mute and solo. The Main sub-mix is three M50s in a Decca tree plus two outriggers. | `mix.json` `mic_db`, `pan_by_mic`. The loaded mics are Close and Main on strings, brass and woodwinds; Mid on the harp; Surround on the timpani and trumpets. | Yes. The factory balance of the patches is read below: 1FH KS Master Close +2.6 / Main -7.1 dB; OB KS Master Close 0 / Main -27.2 dB; the mockup's horns are the reverse of their patch (Close -6.3 / Main 0, the template's value). |
| p.141, 4.2.6 Channel Routing: Stereo, Mono (sum), Mono From Left, Mono From Right, Swap Left And Right. | A one-pitch phase fault in a stereo mic pair (Horn 1, finding 1). The patch state has one routing field, `channelMap` (0 on every patch read). | Not used. Proposed as the second test in finding 1. |
| p.141, 4.2.7 Stereo Double: sets the width of the stereo spread; works only when the Master Channel's source is Stereo. | The two DIV tracks (Close only, one signal). | In use on the Violin I solo (spread 0.4, correlation 0.93-0.94). Not on Violas div, which is still at correlation 1.00 (finding 4). |
| pp.141-142, 4.2.8 Reverb: the Opus convolution reverb, pre-delay, volume, Master button. | The Opus reverb is off on every track; four Spaces II returns carry the hall. | Yes (measured below; no change wanted). |
| p.142, 4.2.9 Envelope: attack, hold, decay, sustain, release; "be careful when changing them". | `sus_release_cap_ms` (strings 150 / 350 ms, Horn 1 237 ms), Harp `env_sustain`. Staccato decays in the rests. | Yes. Note-end tails of the stems are in finding 3; nothing here asks for a release change. |

MANUAL-GAPS #13 (Mid instead of Close on the woodwinds and horns) is still untested. It is the fallback in findings 1 and 3.

## Hall, tone and low end on c16 (measured; no change wanted)

- G.P. after the fff (master, cut-off at 242.77 s): 10 dB fall 0.09 s, 20 dB fall 0.28 s, -20.5 / -31.4 / -46.0 dB at +0.3 / +0.6 / +1.0 s. c15: 0.09 s, 0.28 s, -20.9 / -32.0 / -45.7. c05 (Dan's limit): 0.13 s, 0.32 s, -19.3 / -32.6 / -44.8. The late slope fitted from -25 to -55 dB reads 1.54 s on c16, 1.64 s on c15 and 2.02 s on c05 with the same script, so the 1.30 to 1.36 s in CHANGES is not a real rise: by one method c16 is slightly shorter than c15. Per band at +0.3 s, c15 / c16: 250 Hz-1 kHz -19.5 / -19.3, 1-6 kHz -23.9 / -23.1.
- Families at the G.P. (dry stems plus return), +0.3 / +0.6 s: strings -20.1 / -31.1, winds -22.6 / -33.0, brass -22.2 / -33.8, timpani and harp -20.8 / -34.4. They agree within 2.7 dB.
- Return against the dry sum of its senders (200 Hz-5 kHz), c15 / c16: strings -11.0..-12.1 / -10.0..-12.0; winds -11.2..-13.3 / -11.5..-13.2 (F major episode -8.6, which contains the tail of the bar 72 chord); brass -15.1..-17.4 / -15.1..-17.5; timpani and harp -10.7..-13.2 / -10.8..-13.2. Nothing moved by more than 0.3 dB except the fugato strings (qn 168-213, -11.5 to -10.0).
- Trumpets and horns in one room: note-end drop of the dry stems at +0.2 / +0.3 s (medians over 10-17 isolated note ends): Trumpet 1 -17.6 / -24.7, Trumpet 2 -19.2 / -25.7, Horn 1 -21.9 / -29.6, Horn 3 -17.1 / -28.0, Trombone 1 -17.8 / -27.0, Violins I -18.8 / -28.3. The trumpets carry the same stage sound as the horns and strings. In the tutti of bars 105-120 the trumpets read L-R -3.1 / -3.6 dB, correlation 0.87; horns +1.8..+2.6, 0.61-0.76.
- Lower resting CC11 at ff: band shares of the string stems in bars 105-120, 305-320 and 329-339 are within 0.5 dB of c15 in every octave band from 250 Hz to 10 kHz; spectral centroids Violins I 1652 / 1653 Hz, Violins II 1092 / 1101, violas 602 / 612, celli 559 / 552 (c15 / c16). Woodwinds: within 1 dB, except Flute 1 in bars 105-120 (2-5 kHz share -16.5 to -18.6 dB, level -0.9 dB) and Oboe 1 (level -1.5 dB). Master centroid in the three tuttis 971 / 959, 1057 / 1045, 1154 / 1166 Hz. Nothing became duller, thinner or drier.
- Low end in the tuttis (bars 101-120, 301-320, 329-339), share of the master's power: 100-250 Hz -9.3 / -9.6 / -10.6 dB, 250-500 Hz -5.5 / -6.5 / -6.2 dB. Dvořák's loudest tenth: -6.6 and -6.5; Brahms 1/ii and 4/ii, whole movements: -8.8 / -7.6 and -6.0 / -6.3. There is no 200-500 Hz build-up. The 100-250 Hz band is 0.5-4 dB lighter than each reference (c05: -7.8 / -8.0 / -7.3). It is carried by the celli (23-32 %), the basses (18-31 %) and the timpani (14-20 %). This is the result of the cuts made for Dan's "mushy" note; leave it unless Dan calls the sound thin. The basses' div. pizz. octaves (bars 253-268): 100-250 Hz -10.0 dB, no build-up.
- For critic B, not this lens: Clarinet 2 reads -32.5 dB in bars 105-120 and 305-320, level with Flute 1 and Horn 3, 5-8 dB over the oboes, cor anglais and bassoons, and it carries 15-19 % of the whole tutti's 250-500 Hz (more than the violas).
- Standing checks that pass: con sordino (Violins II 504-552: 2-4 kHz -13.2 dB against 250 Hz-1 kHz, open strings -3.7 to -9.3; correlation 0.53); the link handover (borrowed harmonic -49.2 dB, L-R +4.9; harp harmonics -48.9 dB, L-R +4.2); S3 (returns fall smoothly through qn 360 and 828 in 0.25 qn steps, no cut tail); the solo passage (solo L-R +5.5, correlation 0.94; master correlation 0.74, c15 0.77; one violin is a point, leave it); loop pulsing folded at 3.95 s (autocorrelation of the detrended 50 ms level: Horn 1's last note -0.21, the two violin instances summed 0.02, the opening G sharp 0.23, the harmonic -0.11: no pulse).

## Findings, ranked by what a listener would hear

### 1. Horn 1's G sharp 4 has its fundamental in anti-phase between left and right: the first and last sound of the movement has no position and loses 8-11 dB of its fundamental in mono (bars 1-2, qn 0-5.7; bars 145-152, qn 432; bars 237-240, qn 708; bars 359-376, qn 1076.8-1128; Horn 3 at qn 1092) (measured; fix to be tested on one track)

What is wrong: the note is a single horn, seated left (seat -0.25, REAPER pan -0.18). On the stem it reads L-R -0.6..+0.1 dB (no side) and its two channels are close to opposite polarity at the fundamental. On headphones such a tone is diffuse and cannot be located; on one speaker most of the fundamental cancels. It is the pivot note of the symphony (movement II's A flat, the finale's A flat), heard alone.

Evidence (c16; c15 is the same within 0.01):

| passage | Horn 1 stem correlation | 415 Hz partial: correlation, mono loss | master correlation | master mono loss at 400-430 Hz |
|---|---|---|---|---|
| bars 1-2 (qn 0.3-5.5) | -0.34 | -0.72, -8.0 dB | -0.13 | -7.9 dB |
| last note (qn 1113-1127.5) | -0.53 (per second -0.61 to -0.10) | -0.86, -11.2 dB | +0.05 | -9.8 dB |
| horn call, bars 3-6 (qn 6-18), for comparison | +0.82, L-R +3.4 | | +0.78 | |

- It belongs to the pitch, not the dynamic or the instance. Over every held, unaccompanied brass note in the stems: 1FH on G sharp 4 reads -0.72 to -0.78 at the fundamental on four Horn 1 notes (stem levels -41 to -50 dB) and -0.73 on Horn 3's (qn 1092); F sharp 4 -0.35; G4 +0.24; all other pitches (Horns 2-4 on E3, B3, D4, E4, A4; trombone, tuba) +0.88 to +0.98.
- The higher partials of the same note are in phase (831 Hz +0.51, 1661 Hz +0.55, 2076 Hz +0.85) and sit left (+8 to +9 dB at 1.7-2.1 kHz), so the Close mic is placed correctly; the fault is in the Main pair, which is the louder mic here (Close -6.3 dB, Main 0 dB, Main's channels at seat ±0.8).
- The Dvořák recording's 2 s frames have correlation 0.47-0.77 (5th to 95th percentile). The c05 master (before the template mix) read +0.68 in bars 1-2.
- The existing side-only low shelf (200 Hz, -6 dB) does not reach 415 Hz, and extending it is the wrong tool: at 415 Hz the side signal is 11 dB over the mid, so a 12 dB side cut removes 8.9 dB of the fundamental in stereo as well. The same holds for a narrower Main (`width_by_mic`) and for `track_width`: each sums the two channels, and the sum cancels.

Fix: test on Horn 1 alone (one-track range render of qn 0-18, 426-456 and 1068-1128) before the full render.
- Test A, `build/mix.json` track "Horn 1": `"mic_db": {"Close": 0.0, "Main": -6.0}` (the patch's own balance is Close +2.6 / Main -7.1 dB, read in `1FH KS Master.oib`), `gain_db` re-fitted so bars 3-6 keep their c16 level (-38.4 dB).
- Test B, if A fails: keep the c16 mic levels and route the instrument from one channel (manual p.141, Channel Routing, "Mono From Left"). The state field is the instrument's `channelMap` (0 = Stereo in every patch read); set it in `tools/build_reaper.py` `apply_mix` from a new mix.json track key (`"channel_map": N`), try the menu's order (Stereo 0, Mono 1, Mono From Left 2), and confirm on the stem that the two channels differ only by the pan. Record the result in MANUAL-GAPS.
- Fallback C: Mid in place of Main on Horn 1 (MANUAL-GAPS #13; p.138), same test.
- Keep the first variant that gives, on the notes at qn 0, 432, 708 and 1101-1127: correlation of the 400-430 Hz band +0.3 or more, stem L-R between +1 and +5 dB, mono loss 3 dB or less; with the horn call (qn 6-18) within 1 dB of c16 in level and L-R, and the note-end drop at +0.2 s no more than 6 dB faster than c16's -21.9 dB (so Horn 1 stays in the room with Horns 2-4).
- Horn 3 (qn 1092, the same pitch for 6 s under Horn 1): give it the same setting only if its drone in bars 153-168 stays within 1 dB in level and L-R.
- If no variant passes, the fault stays and is reported; do not correct it with the envelope.

### 2. The second instance on the last G sharp plays a thinner, noisier sample from its first bow change on, so a second colour fades in and out under the held note (bars 364-376, qn 1096-1128; Violin I solo, the DIV A copy) (measured; fix is a row choice)

What is wrong: c16 doubled the note on the "Violin I solo" instance to cover the bow changes. Position is right: the copy reads L-R +5.3 dB against Violins I +5.8. The first piece of the copy also matches the section in tone. Every later piece, which is a same-pitch re-attack on "Leg Slur MAX", is a different sample: its fundamental is 7 dB weaker and its bow noise 4 dB stronger. The two instances alternate in level every 2-4 s, so the listener hears the full section and then a thin, airy half section in turn.

Evidence (stems, band levels on the same scale):

| piece | level | 500 Hz-1.5 kHz | 1.5-4 kHz | 4-8 kHz | 8-16 kHz |
|---|---|---|---|---|---|
| Violins I, first bow (0.3-3.5 s after qn 1089) | -50.1 | 21.3 | 20.3 | 6.8 | -13.2 |
| Violins I, second bow (4.5-7.3 s) | -51.0 | 20.0 | 19.9 | 5.4 | -14.8 |
| copy, first piece (0.3-1.7 s) | -49.8 | 20.8 | 21.6 | 7.2 | -13.3 |
| copy, second piece (2.5-5.5 s) | -51.1 | 13.6 | 22.1 | 11.1 | -9.1 |
| copy, third piece (6.3-9.2 s) | -51.3 | 13.4 | 22.1 | 11.0 | -9.2 |

- 4-8 kHz against 500 Hz-1.5 kHz, per second through the note: Violins I alone -11.4 to -17.1 dB (c15 the same); the copy -14.3, -10.1, then -1.9 to -4.9 dB; the sum of the two swings between -5.1 and -15.7 dB (c15: -12.0 to -17.1). Correlation of the sum per 2 s: 0.54 to 0.71 (Violins I alone 0.33-0.44), since the copy is a narrow source (0.88).
- An EQ on the copy does not solve it: a -7 dB shelf at 4 kHz with +3.5 dB at 815 Hz, simulated on the stems, leaves the swing at 8.1 dB (9.4 as rendered), because the weak fundamental is in the sample.
- The dips at the five bow changes are as CHANGES says (sum 4.3-8.2 dB by my 40 ms frames at qn 1096.14, 1103.8, 1110.7, 1116.3, 1121.0); the three largest are at the copy's own changes.

Fix (`build/score_config.py`): play the copy on its plain sustain row. Add "Sus MAX" to the copy for the span, as Violins I already has it: `ART_AT` "Violin I solo" 1088.5 "Sus MAX" (the DIV A KS Master has the row at key 24; it is one more row on a Close-only instance). The track plays nothing after qn 1128, so no keyswitch back to "Leg Slur MAX" is needed; the solo of bars 349-356 keeps "Leg Slur MAX". Violins I's own second and third bows on "Sus MAX" stay within 1.4 dB of its first in every band (table), so the same row on the copy should hold its first-piece tone. Keep `HELD_DOUBLE`'s times and the CC11 lift.
- Check on the stems: each later piece of the copy within 2 dB of its first piece at 500 Hz-1.5 kHz and at 4-8 kHz; the sum's 4-8 kHz against 500 Hz-1.5 kHz inside -11 to -17 dB for every second; dips no larger than c16's.
- If the copy's re-attacks on "Sus MAX" bloom too slowly and the dips grow past c16's, the choice is between the dips (c15: 12-13 dB on one instance) and the colour. In that case end the doubling after the copy's first piece (drop `rebow_at` 1110.66 and 1121.0 and let the copy hold one bow from 1096.14, re-bowed only where Violins I is at full level) and report what remains.

### 3. The woodwinds have almost no stage sound of their own, so the picture narrows to near mono whenever they play without the strings (counterstatement bars 29-36, qn 84-108; Oboe 1 bars 185-196; the clarinet tune bars 153-168; the F major episode) (measured; mic step inferred, to be tested on one track)

What is wrong: strings and brass are Main-led and bring the recorded stage with them. The woodwinds are Close-led (the template's values, and the patches' own), and the template gave them their room through returns that are 6 dB higher and twice as long as ours. After the cuts made for Dan's "too wet" note, the strings and brass kept their stage sound and the woodwinds lost most of theirs. In the counterstatement the winds call and the strings answer every two bars, and the stereo picture closes and opens with them.

Evidence:
- Counterstatement, master: winds' call (qn 84-90, 96-102) correlation 0.87, side/mid -11.1 dB; strings' answer (qn 90.4-96, 102.4-108) correlation 0.42, side/mid -3.6 dB. Levels are equal (-40.7 / -40.3 dB). The Dvořák recording's 2 s frames lie between 0.47 and 0.77.
- Stems in those bars: Flute 1 correlation 0.94, Oboe 1 0.99, Clarinet 1 0.91, Clarinet 2 0.98, bassoons 0.96-0.97; Violins I 0.42, celli 0.38. Oboe 1 in its solo (qn 552-588): 0.99, side/mid -17.3 dB.
- Note-end drop of the dry stems at +0.2 s (medians over 9-26 isolated note ends): Flute 1 -32.7, Oboe 1 -40.6, Clarinet 1 -30.3, cor anglais -28.5 dB; Bassoon 1 -18.2; Violins I -18.8, Violins II -14.6, violas -17.7, Horn 1 -21.9, Trumpet 1 -17.6. The upper woodwinds' stems are 10-22 dB drier than the strings' and brass's.
- The return does not make up for it: R Winds stands -11.5 to -13.2 dB against the dry winds, R Strings -10.0 to -12.0 against the strings. At the G.P. the winds fall 20 dB in 0.15 s, the strings in 0.28 s.
- Main levels against Close, mix.json (patch file): Flute 1 -4.7 (-11.1), Oboe 1 -20.6 (-27.2), cor anglais -11.6 (-25.9), Clarinet 1 -3.4 (-24.8), Bassoon 1 -8.6 (-17.5). The Main mic is loaded on all of them.

Fix (the item c13 deferred as C #1b, with the scope widened by these numbers): raise the Main mic, which adds the recorded stage (short, decorrelated) and no hall tail.
- Step 1, one-track range render of Oboe 1 (bars 29-44 and 185-196) at `mic_db` Main -6.0 and at 0.0. Keep the lower value that gives: stem correlation in qn 552-588 of 0.90 or less, note-end drop at +0.2 s between -22 and -32 dB, 250-500 Hz share up by less than 1.5 dB; give the K-weighted level back in `gain_db`. If the oboe turns thick at both, try Mid in place of Close (MANUAL-GAPS #13) on the same range, or stop.
- Step 2, if step 1 passes, in `build/mix.json` tracks: Oboe 1 / 2 Main -20.6 -> the tested value; cor anglais -11.6 -> the same; Bassoon 1 / 2 -8.6 -> -4.0; Flute 1 -4.7 -> -1.5; Flute 2, Clarinet 1 / 2 -3.4 -> -1.5. Re-fit each `gain_db` to its c16 K-weighted level on the whole-piece pass.
- Pass for the render: the winds' call (qn 84-90, 96-102) at master correlation 0.75 or less; winds' 20 dB fall at the G.P. 0.30 s or less; master G.P. numbers inside Dan's limits (20 dB fall 0.50 s, soft ends 0.30 s). Do not raise the wind sends or the return.
- This departs from a template default (Close-led woodwinds). The measured reason is above: with the returns 6 dB under the template's, the default leaves this family 10-22 dB drier at the stage than the others.

### 4. The violas' upper div. voice is still a single-channel point in the centre, at the level of the full section beside it (bars 209-224, qn 624-672; bars 349-356) (measured; fix as tested on the solo in c13)

Evidence: Violas div correlation 1.00, side/mid under -80 dB, L-R 0.0 in both passages; Violas 0.42-0.48, side/mid -4.6. In the trio's ff return the two voices are level (Violas div -45.6, Violas -45.3 dB). Stereo Double (p.141) on the other DIV track gave correlation 1.00 -> 0.93 at spread 0.4 with the tone within 0.4 dB (c13); Violas div and a larger spread were never tried (c13 and c14 deferred them).

Fix: `build/mix.json` track "Violas div": `"stereo_double": {"spread": 0.6}` (the key `build_reaper.py` already reads), `gain_db` raised by the measured loss (the solo lost 2.5 dB at 0.4). One-track range test on qn 624-672 first: keep it if the correlation is 0.60-0.92, L-R within 1 dB of 0, band levels within 1 dB of c16 and no notch deeper than 6 dB in the mono sum's third-octave spectrum; otherwise 0.4. The effect is small: the violins are 10 dB over this voice in bars 209-224.

Do not touch:
- the returns' faders, pans, 180 Hz high-pass and IR envelope, and every send (hall numbers equal c15's and are inside Dan's limits; families agree within 2.7 dB at the G.P.);
- the low mids: no cut at 100-500 Hz, no boost either without Dan's word;
- `CC11_REST_MAP` and the ff make-up trims as far as tone goes (band shares within 0.5 dB of c15 on the strings);
- the trumpets' mics, seats and widths (same stage sound as the horns);
- the Violin I solo's Stereo Double 0.4, seat and shelf in bars 349-356;
- the doubled G sharp's position (L-R within 0.5 dB), bow-change times and CC11 lifts; Violins I's own pieces on "Sus MAX";
- the con sordino lane, the borrowed harmonic and the harp harmonics' level and seat at the handover;
- Horns 2 and 4 and the horn call of bars 3-6 (correlation +0.8).
