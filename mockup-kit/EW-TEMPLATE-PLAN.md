# Adopting EastWest's own template mix (Dan, 2026-11-08)

Dan: "we need to take every bit of this and use it to improve our own scoring." The source is EastWest's official HO REAPER
template (Templates 2, "Midi Included" demo). The findings are in `mockup-kit/EW-TEMPLATE-FINDINGS.md`. The default is to
adopt each item; critics still measure each one and can reject it with numbers. The research thread will send more.

Order: c50 does the mix (items 1-4), c51 does the performance data (item 5) and judges the whole. Both cycles keep the
usual critic lenses, plus a check on these items.

## 1. Mic layout inside Opus (c50; small tool change)
- Strings: Close on at about -6 dB under Main (Close 0.5, Main 1.0; template range -3 to -9 dB). Close is panned to the seat
  (template seats: Vln I -0.31, Vln II -0.07, Va 0, Vc +0.33, Cb +0.62). Main stays at full width (panLeft -1, panRight +1)
  and is not re-panned.
- Brass: the same, with Close -6 to -10 dB under Main (Hn -0.25, Tpt +0.31, Tbn +0.25, Tuba +0.35).
- Woodwinds: Close 1.0 is the main mic, Main under it (Fl -4.7, Cl -3.4, Bn -8.6, BCl -9.8, CA -11.6, Ob -20.6 dB).
- Harp Close 0 / Main -9 / Mid 0 dB. Timpani Close -8 / Main -7 / Surround 0 dB. Cymbals, tam-tam, glock: Main only.
- A small REAPER track pan does the rest (Vln I -0.10, Vln II -0.21, Va 0, Vc +0.15, Cb +0.23; horns -0.13..-0.18,
  trumpets +0.03..+0.10, trombones +0.15, tuba +0.23).
- Tool: `apply_mix` in build_reaper.py gets a per-mic pan rule ("pan_by_mic": Close at the seat with the track width, Main
  and Surround full width). This replaces `width_by_mic` and the seat-narrowed Main from c35/c45.

## 2. Reverb: Opus reverb off, Spaces II returns per family (c50; new tool work)
- Opus fx:0 volume 0 on every track (template leaves it on only in a few combined patches; we turn it off everywhere).
- REAPER return tracks, 100 % wet, true stereo, the full IR (endPos 1.0) with the rear-position impulses; pre-delay by
  family: strings 19.6 ms, winds 18.5 ms, brass 10 ms, perc 10 ms. The brass return loads the hall's Horns impulses.
  - Strings: "S. Cal. Hall Strings TS RR 3.3s", send -5.6 dB
  - Brass (horns, trumpets, trombones, tuba): "S. Cal. Hall Brass TS RR 3.3s", send -8.8 dB
  - Woodwinds: "San Francisco Hall TS RR 3.4s", send -8.4 dB
  - Percussion, timpani, harp: "Northwest Hall TS RR 2.6s", send -6.4 dB (perc), -8.8 dB (harp)
  - Optional "ALGO GLUE" ReaVerbate return fed from every family at -6 to -10 dB (test in pass 2).
- Each return: ReaEQ before Spaces II with a high-pass at 90-100 Hz, a -5 to -7 dB bell at 2.5-2.7 kHz, and a low-pass at
  5.6 kHz (strings 8.5 kHz).
- Sends are post-fader. The template sends from section buses; we send from each track at the family level, which is the
  same signal (the bus EQ of item 3 sits on each track, so each send carries it too).
- Rendering: return tracks are rendered as extra stems ("R Strings", "R Brass", ...). The master is the sum of the dry
  stems and the return stems. Critics measure dry stems for balance and the master for blend; say so in CHANGES.md.
- The exact Spaces II and ReaEQ states are in `symphony/mockup-research/ew-template-2026-11-08/` (`ho-mix-chunks/*_VERB.txt`,
  `ho-mix-fx.json` with the decoded JSON). Load each return's FX from its chunk with
  `TrackFX_SetNamedConfigParm(fx, "vst_chunk", ...)` rather than setting parameters one by one. The section-bus EQ chunks
  are there too (STRINGS.txt, BRASS.txt, WOODWINDS.txt, MASTER.txt).
- Then re-fit the delivery chain (deliver_master.py) to the new levels, keeping the delivered targets (LRA 14-16 LU,
  span 16-19 dB, true peak -1.5 dBTP or lower).

## 3. Section EQ (c50; per-track ReaEQ, existing tool)
Put on every track of the family (linear, so the same as a bus EQ):
- Strings: HPF 53 Hz, -2.2 dB at 456 Hz, -5 dB at 1 kHz (wide), +4 dB high shelf at 4.7 kHz
- Brass: HPF 41 Hz, -5.4 dB at 475 Hz, -7.8 dB at 821 Hz, +4 dB shelf at 7.5 kHz
- Woodwinds: -5.1 dB at 447 Hz, -3.1 dB at 1 kHz, -4.7 dB at 2.2 kHz, +5.1 dB shelf at 7.6 kHz
- Harp: HPF 183 Hz, -8 dB at 304 Hz and 1.27 kHz, +8 dB shelf at 7.7 kHz
- Timpani: HPF 44 Hz, +8.6 dB at 84 Hz, -11.5 dB at 385 Hz, +9 dB shelf at 7 kHz
- Master (before delivery): HPF 42 Hz, -1.6 dB at 167 Hz, -1.9 dB at 1.18 kHz, +0.8 dB shelf at 8 kHz
Existing per-track EQs from earlier cycles stay where they fix a specific sample problem; remove ones that only did what
the family EQ now does. Re-check balance after the EQ (it removes 2-8 dB in the body bands).

## 4. What this replaces
- c44 hall settings (fx_volume 0.095, the Opus IR envelope, 160 Hz low cut, 5.5 kHz high cut) and the per-group Opus sends.
- c35/c45 seat-narrowed mics and width_by_mic.
Keep a pass-2 copy of the old layout for one cycle so the critics can compare.

## 5. Performance data (c51)
- Legato overlap 45-80 ms on string legato lines, 33-58 ms on winds and brass.
- Repeated-note gap 20-45 ms on legato lines, 40-60 ms on short-note rows.
- Legato velocity 90 or more where a clear change of note is wanted (check what velocity does on each legato patch in the
  2021 manual first).
- CC1 drawn at 7-13 points per second on sustained and legato lines, using the full range.
- CC1 only, no CC11. Every KS Master in the template uses the Opus macro "Mod + Expression Combo" on CC1, which drives
  controller_1 (vibrato) and controller_11 (dynamic layers) together, linearly; one CC1 lane does dynamics and vibrato.
  Check what our patches map CC1 and CC11 to before the test (`opus-mics.txt`, `ccshape-report.txt` show the CC1 shapes
  around phrase starts, legato changes and phrase ends). Our level work (LEVEL_SHAPES, fills, trims) is written in CC11, so this is a staged change. c51 runs a
  pass-2 test on the strings with CC11 held fixed and the dynamics and shapes moved into CC1, and the critics compare it
  with the CC11 version. Adopt it if it is no worse; otherwise record why in LEARNINGS.
- Winds and brass played slightly early (-2 to -13 ms mean) is already covered by our lead tables.
