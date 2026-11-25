# Cycle 09, critic C: blend and space (lens C1), on the c08 render

Measured on `cycles/c08/render/` (stems after the c08 stem fix, returns 91-94, master), `build/parts.json`, `build/mix.json` and `cycles/c08/before/` (the c07 data). Return simulations follow c07's method (LEARNINGS "Hall and returns (c07)"): each return's transfer was fitted from the summed send input (mono, post-fader send levels from mix.json) to the rendered return stem with 10.9 s rectangular windows; fit residuals -11.1 dB (R Brass), -11.8 dB (R Winds), -7.0 dB (R Strings, rough). Decay figures use `check08.py`'s G.P. method. Scratch scripts were in `/private/tmp/claude-501/mockup-loop/scherzo-c09-C/` (deleted).

## Manual notes (cycle 9, slot C: group L1, May 2021 HO manual PDF pp. 138-139 and 141-142, read in full, p.138 as an image; MANUAL-GAPS.md read)

| manual (PDF page) | where it applies here | does the render follow it |
|---|---|---|
| p.138: Close mics give presence. Mid mics, at the stage edge, give definition without proximity. Main mics (Decca tree in the fifth row) carry more room reflections than direct sound, "a big, unified sound". Surround adds depth. | Depth of each family. Strings and brass run Main 0 dB with Close 4.5-10 dB under it. Woodwinds run Close 0 dB with Main 3.4-20.6 dB under it (Oboes -20.6). The DIV A / DIV B tracks have only a Close mic. | Partly. The winds and the two DIV tracks have the close perspective. The strings and brass have the Main perspective (findings 1 and 3). |
| p.139: each mic sub-mix has its own volume, pan and on/off control. Turning a mic off unloads its samples. | `mic_db` / `pan_by_mic` in mix.json. The DIV patches load only a Close channel (`.oib` read: channels Master, Close and Reverb only). | Yes. A DIV track has no Main mic to turn on, so its depth can only come from the send. |
| p.141: Channel Routing (Stereo, Mono, Mono from L/R, Swap). Stereo Double widens the stereo spread and works only with the Stereo channel source. | The DIV tracks measure L/R correlation 1.00 (300 Hz-8 kHz). | Not used. Stereo Double is the library's own tool for a near-mono Close pair (finding 3). Its key in the Opus state has not been read yet. |
| pp.141-142: the per-instance convolution reverb (preset, pre-delay, volume, Master button). | Opus reverb is off on every track. The hall comes from four Spaces II returns (template). | Yes (template item 2). |
| p.142: the five-stage envelope, with release in ms. "All instruments are programmed with envelope values to achieve a natural result." | String release caps 150 / 350 ms, horn 237 ms. These set how much of each note's own tail reaches the hall. | Yes. The caps were fitted by measurement; staccato tails are measured below. |

MANUAL-GAPS #13 (Mid instead of Close on the winds and horns) is the manual's other route to wind depth, and it costs no memory. The Mid mic is not loaded on the winds now, so trying it means loading a mic and checking memory.

## Is c08 too wet, or now too dry? (measured)

- G.P. after the fff (qn 1016): the master drops 21.1 / 32.1 / 46.9 dB at +0.3 / +0.6 / +1.0 s, t20 is 0.30 s and RT60 1.30 s. The final chord drops 21.4 / 32.8 / 41.7 dB, RT60 1.28 s. Soft ends measure 0.13 / 0.21 / 0.31 s. These are all at c05's figures (22.2 / 34.8 / 47.5 at the G.P.), so Dan's limit holds.
- The other clean cut-offs in the movement (all tracks silent for 0.45 s or more, at qn 393.6 and 861.6) fall 21.0 / 23.3 and 16.4 / 20.6 dB at +0.2 / +0.3 s. Recordings fall 13-17 dB at +0.3 s (BRIEF S4), so the cut-offs are drier than a real hall but inside Dan's limit. Nothing below adds more than 0.5 dB of hall at +0.3 s.
- Returns carry -12.94 dB of the dry energy (c07 target -13.4).
- No 200-500 Hz build-up in the tuttis. Master band shares (dB of total) were compared with the loudest 10 % of the Dvořák frames:

  | passage | 100-250 Hz | 250-500 Hz | 500 Hz-2 kHz | 2-6 kHz |
  |---|---|---|---|---|
  | Dvořák loudest 10 % | -6.4 | -6.4 | -3.4 | -10.9 |
  | 105-120 | -8.1 | -6.0 | -3.1 | -10.4 |
  | 305-320 | -8.7 | -7.4 | -2.5 | -9.8 |
  | 329-339 | -7.5 | -6.8 | -3.2 | -9.4 |
  | 253-268 (basses div. pizz.) | -6.8 | -7.7 | -3.1 | -10.0 |

  The tuttis are 1-2 dB thin at 100-250 Hz, not heavy. 60-100 Hz sits 6 dB over Dvořák, but that MP3 has almost nothing below 100 Hz, and the stored Brahms metrics are far heavier there. Do not cut the low mids.

## Findings, ranked by what a listener would hear

### 1. The woodwinds sit in front of the strings: close, near-mono and with less hall (counterstatement bars 29-44, qn 84-132; trio bars 153-168 and 185-196; codetta 225-236; 345-356) (measured; mic fix inferred, send fix simulated)

What is wrong: in a hall the winds sit behind the strings and sound at least as distant. Here each wind is a narrow, close point in front of a wide, roomy string section. The counterstatement's call and response therefore sounds like two recordings taking turns, not one orchestra.

Evidence (measured):

| family | stem L/R correlation, 300 Hz-8 kHz, qn 84-132 | stem tail after short notes, +0.1 / +0.2 s re note peak (median over the piece) | hall re dry (send dB + return gain, 200 Hz-5 kHz) |
|---|---|---|---|
| Flute 1 | 0.90 | -19.0 / -35.5 | -13.2 dB |
| Oboe 1 | 0.99 | -17.5 / -38.9 | -13.2 |
| Clarinet 1 / 2 | 0.87 / 0.87 | -12.2 / -32.8, -13.3 / -29.7 | -13.2 |
| Cor anglais | 0.93 | -14.1 / -26.6 | -13.2 |
| Violins I / II | 0.42 / 0.47 | -11.3 / -21.0, -9.8 / -16.4 | -11.2 |
| Violas / celli | 0.46 / 0.36 | -6.1 / -15.2, -9.1 / -15.7 | -11.2 / -12.8 |
| Horn 1 | 0.10 | -13.1 / -23.7 | -15.9 |

- At +0.2 s the wind stems carry 9-24 dB less of their own room than the string stems. They also get 2 dB less hall.
- At the G.P. the late hall tails of the two families already agree (winds plus R Winds -31.8 dB at +0.6 s, strings plus R Strings -29.8). The difference is in the early room and the stereo spread, which come from the Main mic (p.138) and which the template turned down for the winds (Main 3.4-20.6 dB under Close).

Fix:
- **a. Simulated.** `build/mix.json` group "wind": add `"send_offset_db": {"R Winds": 3.0}`. That gives the high winds -5.36 dB, level with the strings' -5.56. Bassoon 1, Bassoon 2 and the contrabassoon keep their `sends` override at -150 dB, so they stay dry (finding 2 has the bassoons).
  - Simulated on the c08 stems: G.P. 21.1 / 32.1 / 46.9 dB -> 20.6 / 31.6 / 43.8 dB, RT60 1.30 -> 1.34 s. The final chord does not change.
  - Counterstatement master level +0.1 dB, 250-500 Hz +0.2 dB.
- **b. Inferred; check stems before keeping.** Raise the Main mic on the winds whose Main is furthest under Close, in `build/mix.json` track `mic_db`:
  - Oboe 1 / Oboe 2 Main -20.6 -> -9
  - Cor anglais -11.6 -> -6
  - Bass clarinet -9.8 -> -6
  - Flutes -4.7 / -3.4 -> -2
  - Clarinets stay at -3.4
  - Then give back level in `gain_db` from the K-weighted stem loudness against c08, as c06 did after its mic change.
- Targets for b:
  - wind stem correlation in 84-132 at 0.75 or lower;
  - short-note stem tail at +0.2 s within 8 dB of the violins' -21 dB;
  - G.P. at +0.3 s still 20 dB or more, RT60 1.5 s or less.
  - If the oboe turns dull or thick at 250-500 Hz (Main carries more room low-mid), stop at -12.
- This rejects part of the template's item 1 (Close as the winds' main mic) with the numbers above. The hall level remains the template's own.

### 2. The trumpets, trombones, tuba and bassoons are not in the horns' hall: their cut-offs stop dead while the horns and strings ring (bar 120 into the sub. p, qn 359.4; the G.P., qn 1015.8; every exposed bassoon end, e.g. the codetta 225-236 and 1032) (measured; fix simulated)

What is wrong: c07 took the low sends off and the trumpets down 6 dB (register sends; research batch 5 and Howl's). After a tutti cut-off each family's tail falls at a different rate, as if they were in different rooms:

Tails (dry stems plus their share of the return, high-passed at 180 Hz) are in dB relative to each family's level in the last 0.5 s.

| family | G.P. +0.15 s | G.P. +0.3 s | G.P. +0.6 s | bar 120 end +0.3 s |
|---|---|---|---|---|
| strings | -15.5 | -20.5 | -29.8 | (sub. p continues) |
| horns | -13.8 | -24.9 | -32.7 | (continues) |
| trumpets (send -14.77) | -18.6 | -31.1 | -38.8 | -37.0 |
| trombones + tuba (no send) | -19.3 | -26.5 | -48.4 | -44.9 (-56.9 at +0.6) |
| bassoons + contrabassoon (no send) | -29.7 | -44.5 | -53.7 | |
| basses (no send) | -27.4 | -34.8 | -42.6 | |

The trumpets' dry stem falls 64 dB in 0.15 s at bar 120. Everything you hear of them after the cut is their -21.9 dB of hall.

Fix (`build/mix.json`):
- Trumpet 1 and Trumpet 2: `send_offset_db` {"R Brass": -6.0} -> {"R Brass": 0.0}. That is the template's -8.77, the same send as the horns.
- Trombone 1, Trombone 2, bass trombone, tuba: `sends` {"R Brass": -150} -> {"R Brass": -11.77}, 3 dB under the horns.
- Bassoon 1, Bassoon 2: `sends` {"R Winds": -150} -> {"R Winds": -11.36}, 3 dB under the other winds.
- Contrabassoon and basses stay off.

R Brass and R Winds high-pass their input at 180 Hz, so these sends put overtones into the hall, not bass.

Simulated on the c08 stems:
- low brass at -8.77 / -14.77: G.P. +0.6 s tail -46.4 -> -33.0 / -38.6 dB;
- trumpets at -8.77: G.P. +0.6 s -40.3 -> -34.5 dB; bar 120 +0.3 s -37.0 -> -31.1 dB;
- master band shares in 105-120, 305-320 and 333-338 change by 0.04 dB or less at 100-250 and 250-500 Hz (no mush);
- the master G.P. moves by 0.2 dB or less at +0.3 s.

All of findings 1-3 together, simulated: G.P. 21.1 / 32.1 / 46.9 -> 20.6 / 31.1 / 40.4 dB, t20 0.30 s, RT60 1.30 -> 1.36 s. The final chord does not change. Returns re dry -12.94 -> -11.85 dB. That is inside Dan's limits (t20 0.50 s or less, RT60 1.5 s or less) and adds 0.5 dB at +0.3 s.

This rejects research batch 5 item 1 / Part 5 section 19.1 (no low sends) for this pipeline. The reason it was given (mush) is handled here by the returns' 180 Hz high-pass, measured at 0.04 dB or less. The cost the research did not measure is the dead cut-offs above.

### 3. The solo violin and the violas' div. upper voice are mono, dry points beside wide, roomy sections (Violin I solo bars 349-356, qn 1044-1068, DIV A; Violas div bars 209-224, qn 624-672, and 349-356, DIV B) (measured; send fix simulated, width fix inferred)

What is wrong: the DIV patches have only a Close mic (`.oib` read), so these two tracks lack the Main room their sections have. In 209-224 one viola section plays two voices, and the upper voice sounds like a separate close-miked group in front of the lower. The solo's dolce line sits closer than everything around it. A solo can be a little in front, but it should still be in the same room. c05's tone fix holds: the solo's harmonic tilt is now within 1 dB of the Violins I section's at the same pitches (3-8 kHz re fundamental -4.5 against -3.3..-4.1 dB), so tone is no longer the problem.

Evidence (measured, stems):

| window | track | L/R correlation, 300 Hz-8 kHz | stem drop after phrase end, +0.1 / +0.2 / +0.3 s |
|---|---|---|---|
| 1044-1068 | Violin I solo | 1.00 | -18.9 / -37.9 / -42.1 (end 1066.8) |
| 528-552 | Violins I | 0.42 | -13.0 / -26.8 / -41.0 (end 550.8) |
| 1044-1068 | Violins II "la metà" | 0.52 | |
| 624-672 | Violas div | 1.00 | -2.9 / -8.0 / -21.8 (end 672) |
| 624-672 | Violas | 0.43 | |

- Both DIV tracks get the same R Strings send as the sections (-5.56 dB). That is their only room, while the sections also have the Main pair.
- Violas div at 1044-1068 is 6.0 dB under the Violas stem (-58.7 / -52.7). That is for lens B.

Fix:
- `build/mix.json` "Violin I solo": add `"send_offset_db": {"R Strings": 3.6}`. That is Duc's solo-violin send (Part 4 section 14).
- "Violas div": add `"send_offset_db": {"R Strings": 4.0}`.
- Simulated (R Strings fit, rough):
  - the solo's tail at +0.6 s after its last note -31.0 -> -27.9 dB;
  - its soft end (time to fall 10 dB, solo plus R Strings) 0.16 -> 0.19 s, under the 0.30 limit;
  - no effect on the G.P. or on the tutti.
- Width (inferred): try Opus Stereo Double (p.141) on the two DIV tracks' Master channel. The Stereo Double key is not in the `.oib` (Close inserts: SendProcessor only; Master: ChannelEq, SSL strip). Read the key from one saved Opus state with it on before scripting it. Keep it only if the Violas div correlation in 624-672 falls to 0.75 or lower. Widening `width` alone did not decorrelate the pair in c01 or c05.

### 4. The link's harmonic changes hall at the handover: the Violins II harmonic E6 is almost dry, and the harp harmonics bloom in a wetter percussion hall (bars 147-151, qn 438-453; Violins II's borrowed harmonic 420-446, Harp harmonics 445 and 451) (measured)

Evidence:
- Before the handover (qn 440-444) R Strings carries the harmonic's hall at -72..-77 dB under a dry -53..-56 dB: 19-21 dB down.
- The c08 stem fix raised the Violins II stem by 5.4 dB, but `stem_fix.py` sums the returns unchanged (its own docstring), so the delivered c08 master has this hall 5.4 dB short.
- The harp harmonics then enter at -41.2 dB (p, printed). R Perc carries them 9.6-11.9 dB under the dry (-54.8 / -42.9 at 446), on the Northwest Hall 2.6 s IR instead of the strings' S. Cal. hall.
- The seats agree (L-R +4.9 dB for Violins II, +4.2 for Harp harmonics).

Fix:
- No change is needed for the 5.4 dB: the role [419, 447, +5.4] is in REAPER now, and the c09 render restores it. That leaves the harmonic's hall about 14-16 dB under its dry, against the harp's 10-12.
- `build/mix.json` "Harp harmonics": `"sends": {"R Perc": -150, "R Strings": -8.77}`, so both halves of the handover ring in the strings' hall. Check that the harp harmonics' hall re dry stays within 2 dB of the harmonic's after the render.
- Tool note for the actor (LEARNINGS candidate, measured): a stem fix of more than 2 dB on a track with a send leaves its hall at the old level. Either re-simulate that track's return contribution with a fitted transfer (the c07 method) or write the change into the next render rather than the stem.

### 5. Lead for the open Violas legato probe: SHORT_CC11_PARK un-parks CC11 with a hard step 0.01 qn before a long note, so the Violas data before 133-162 is not identical to c07 (inferred; for the actor's one-track test)

Measured in parts.json (c07 `cycles/c08/before/parts.json` against c08 `build/parts.json`), Violas:
- From 132.125 to 164.75, CC11, CC1, vol_db, the notes and the keyswitches are identical.
- Before that they differ:
  - c08 holds CC11 at 120 from 125.804 and steps to 88 at 131.726. The Sus MAX note starts at 131.736, 2 ms later. c07 rose gently 85 -> 88.
  - vol_db ramps -4.96 -> +0.63 dB over 131.5-132.125 (c07: 0 / +0.32).
- The same 120 -> 30..97 step, 0.01 qn before a Sus MAX or Leg Slur MAX onset, occurs 14 times on Violas (122.73, 131.73, 182.46, 191.46, 206.46, 359.53, 818.73, 827.51, 878.46, 890.46, ...), 20 on Violins I, 8 on Violins II and 8 on the celli.
- Mechanism (inferred): if Opus smooths CC11 or picks the legato chain's layer at the first note-on, the line after the step starts on a louder layer.

Test (one-track render, about 5 min, LEARNINGS c08): render the Violas with the un-park moved to the previous short note's end, or ramped 120 -> target over 0.25 qn ending 0.1 qn before the onset. Leave everything else as c08. Compare the window median and the stem level in 133-162 with c08's (115 ms, +3 dB).

## Standing checks in this lens (measured on c08)

- **S1 (hall against repeat dips):** the master pair dip of the V1 head eighths is 3.7 dB in the theme, 4.0 in the reprise, 4.8 in both tuttis and 5.7 in the coda; the counterstatement Fl1 / Ob1 pairs are 4.6. The dry stem sum is 0.0-0.4 dB deeper, so the hall no longer fills the gaps. Findings 1-3 add returns at -24 dB re master and cannot change this by more than about 0.1 dB.
- **S3 (subitos):** at the sub. p of bar 121 (qn 360), R Strings decays smoothly from the ff (-36.6, -38.0, -41.2, -44.1 dB at 358.5-360.0) under the p entry, with no step. At 828 the hall carries through in the same way. The tail is on the returns, so vol_db steps no longer cut it.
- **Con sordino (Violins II 168-196):** CC15 is on at 445.3 and off at 552.5, both in rests. At the start of each note the third harmonic sits -11.4 dB re the fundamental and 3-8 kHz sits -15.1, against -6..-10 for the open Violins II at p elsewhere. The stem's correlation is 0.53, the same room as the open sections. The mute reads clearly and is in the same room.
- **Item 8 (loop pulsing):** not re-measured in this lens.

Do not touch:
- the returns' 180 Hz high-pass, IR envelope 0.5 / 0.5 and faders, and the c08 EQ set (the low mids are not built up);
- the strings' and brass's Main-at-seat ±0.8 layout and the string Close at -4.5;
- the contrabassoon and the basses with no send;
- the Violins II con sordino lane;
- the DIV tracks' c05 shelves (the solo's tone now matches the section);
- the borrowed Violins II harmonic and its +5.4 role.
