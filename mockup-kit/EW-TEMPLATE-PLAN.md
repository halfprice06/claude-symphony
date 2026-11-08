# Adopting EastWest's own template mix (Dan, 2026-11-08)

Dan: "we need to take every bit of this and use it to improve our own scoring." The source is EastWest's official HO REAPER
template (Templates 2, "Midi Included" demo), and 20 expert MIDI mockups (sections 6-8). The findings are in
`mockup-kit/EW-TEMPLATE-FINDINGS.md`. Dan, 2026-11-08: "yes to anything you can do ... get them integrated into other
projects, don't wait for me." **Every item in sections 1-9 is a default for all four movements from each movement's
next cycle.** Critics tune the values by measurement; an item is dropped only with numbers showing it made the render
worse, recorded in LEARNINGS. Where two sources disagree, the rule given here is the default.

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
- Repeated-note gap: see section 8 (60-100 ms is now the default; EW's own template used 20-45 ms on legato lines and
  40-60 ms on short-note rows).
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

## 6. Research batch 2 (FINDINGS.md part 2, confirmed by the ComposerCloud+ edition's different demo)
- **Macro caveat (c51).** EW's sustained CC1 medians are 57-79. That falls in the 55-76 zone where our LEARNINGS measured the
  Non Vib and Vib woodwind layers both sounding, which doubles the amplitude modulation. If the "Mod + Expression Combo"
  macro is tested, measure mp-mf sustained notes for that doubling, and consider a non-linear macro spline that crosses
  55-76 quickly.
- **Short notes (c51).** On string short rows EW parks CC1 (and so CC11) at 118-127 and sets the dynamic by velocity alone
  (medians 24-52). Brass and wind shorts use velocity 62-95. This is the same fix as our harp's CC11 at 110. Test holding
  CC11 at 110-127 over short-note passages with dynamics mapped to velocity. Shorts are 60-90 ms long and exactly on the grid.
- **CC1 is shaped per phrase, not per note (c51).** It stays flat across legato note changes: no bumps and no pre-onset
  dips. About half of phrase starts swell after the onset (upper quartile +12-15 by 200 ms, +23 by 800 ms). A quarter to a
  half of phrase ends taper 13-37 units over the last 0.25-1 s. Long notes are late-peak swells, hairpins peaking at
  40-60 %, or fades to 0. Compare with our per-note shapes and fills, and remove per-note bumps where the phrase shape does
  the work.
- **Strings use two tracks per section (c51, test).** A legato track ("Leg Slur + Port LITE", with LegatoSpeed and
  RTKiller on) and a KS Master track for shorts, sustains and tremolo. Keyswitches sit 40-800 ms before the note.
- **Release times (information only).** EW keeps the patch releases (700-931 ms), except Basses legato 56, oboe 177, tuba 372
  and 1FH 562 ms. Our release caps were fitted by measurement and stay.

## 7. Research batch 3: a hand-played professional mockup (FINDINGS.md part 3, polar-report.txt)
Ashton Gleckman's Polar Express suite MIDI (Spitfire, NI and 8Dio; CC1 dynamics plus CC11 expression). The shapes and the
timing carry over to us; the absolute values do not.
- **Phrase rule for c51 (adopt by default).** Every phrase swells in after its first onset: median CC1 +14 by 0.4 s and +24
  by 0.8 s (IQR +17..+35 at 0.8 s), with nothing before the onset. Every phrase tapers: CC1 19 units higher 1 s before
  the last note-off, 8 higher at 0.5 s. EW's template shows the same (section 6). c51 rule: about +15 by 0.4 s and +25 by
  0.8 s from the phrase start, a taper of about 20 over the last second, scaled to the printed dynamic and overridden by
  printed hairpins.
- **Inside slurs** each note leans off slightly after its onset (median -2 by 0.4-0.8 s); the phrase swell carries the line.
  Add a small per-note lean-off inside slurs.
- **Timing.** Winds are quantized and shifted early by a fixed amount per track: oboe -27, clarinets -38/-46, bass clarinet
  -17, bassoons -40/-85, flute -75 ms. Strings and brass are played in, -20 to -120 ms early on average. Percussion and
  bells sit exactly on the grid. Our lead tables already do this per note against measured attacks; keep percussion
  unshifted and compare our per-track median leads with these.
- **CC density** 13-44 points/s, denser than EW's 7-13.
- **Legato overlaps** 46-230 ms in those libraries: the right overlap depends on the patch. For HO use EW's 45-80 ms
  (section 5) and measure.

## 8. Research batch 4: 20 expert MIDI mockups (FINDINGS.md part 4, expert-report.txt, duc-mix.txt)
Dan, 2026-11-08: "we need as much human expert examples as possible." Sources include Bernard Duc's Mahler Adagietto and
LOTR (full REAPER projects), the Star Wars main title, The Village and 11 Ashton Gleckman suites. Where this disagrees
with sections 5-7, the c51 critics settle it by measurement; the defaults below are what c50/c51 start from.
- **Repeated-note gaps: 60-100 ms (replaces section 5's 20-45 ms as the default).** Medians are winds 63, strings 90,
  brass 98 and short rows 116 ms. This also answers Dan's note that repeated notes are hard to hear (S1). Measure the
  repeat dips; keep EW's shorter gap only where a patch needs it.
- **Phrase arch (refines section 7).** The peak falls at 33-62 % of the phrase in 18 of 20 files. Start and end sit well
  below it, with a range of 30-60 units on long phrases. Combine with section 7: the rise begins after the first onset
  (about +15 by 0.4 s, +25 by 0.8 s), the peak sits in the middle third, and the last second tapers. Long notes keep
  moving: in 15 of 20 files only 0-13 % of long notes are flat.
- **Legato velocity follows the dynamic** (r about 0.35), around section 5's 90-or-more median.
- **Reverb sends (default, on top of section 2's EW returns).** From Duc: sends 0 dB for violins, violas and brass,
  -1.6 dB for cello and bass long notes, -7 dB for low-string short notes. His single 2.1-2.45 s hall (low cut ~184 Hz,
  high cut ~3 kHz, return -5.5/-6.6 dB) is the fallback if the critics measure the EW returns as mushy.
- **Basses EQ (default, added to section 3).** From Duc: basses -2.4 to -3.6 dB at 205-250 Hz. His violin EQ (-1 to
  -2.5 dB at 490-710 Hz, +2-3 dB at 9-11 kHz) points the same way as EW's string EQ; use EW's bands.
- **Tutti entry spread (default).** Expert files spread tutti entries 36-55 ms from first to last track (0-12 % exactly
  together). Add a small fixed per-section offset at tutti entries (seeded, so it repeats between renders), and let the
  critics tune it for clarity.
- **Room-noise bed (default when a free recording is available).** Duc loops a quiet room-noise recording, low cut at
  84 Hz, sent to the hall. Use only a recording we are free to use, and keep the noise floor inaudible in soft passages.
- **Tempo for slow movements (Movement II mainly).** Duc's tempo map follows a recording beat by beat: median beat
  deviation 8 %, phrase-end breaths 15-30 % slower, beat 4 about 7 % slower on average. Movement I's Lento and
  ritardandi can use the breath rule.

## 9. Research batch 5: two full Cubase projects on a wet stage library (FINDINGS.md part 5)
Goldsmith's Mulan overture and Hisaishi's Howl's Moving Castle, both on VSL Synchron, which like HO is recorded with its
room. Defaults under Dan's standing rule; critics tune the values.
- **Reverb sends by register (default; targets "still mushy").** Howl's sends nothing to the hall from bassoons,
  contrabassoon, trombones or tuba, -16 dB from basses and trumpets, and -10 dB from the other winds and strings; Mulan
  sends nothing from its Synchron instruments. On top of the section 2 family sends: bassoons, contrabassoon, trombones,
  tuba and basses send 10 dB less than their family (or nothing, if the critics measure no loss of blend); trumpets 6 dB
  less; percussion unchanged. Duc's low-string short cut (section 8) stacks with this.
- **Darker hall tail (default, tuned by measurement).** Both use a Lexicon Random Hall with the tail low-passed at
  1.8 kHz, 25 ms pre-delay, 2.5-3.6 s. Add a low-pass at 2.3 kHz after Spaces II on each return (try 1.8 kHz if still
  bright). The finale's first template render measured too bright (6-20 kHz share -25 dB against -29 to -32), so start
  here before cutting the family shelves.
- **Hairpin shapes (default, inside the section 8 phrase arch).** Crescendos rise early and then settle: the control
  point sits at 34 % of the time with 88 % of the rise. Diminuendos hold, then fall on the last held note. Winds and
  brass may fade nearly to nothing before a rest.
- **Brass as narrow sources (default).** Horns left at 15-47 % width, trumpets right at about 43 %, trombones centre to
  right. Applies to the Close mic seat and the REAPER track pan; Main stays full width (section 1).
- **Tempo.** Both change tempo on about 20 % of beats, with 20-26 breaths more than 15 % slower: supports the section 8
  breath rule.
- **Not for HO.** Howl's repeated notes nearly touch only because VSL switches samples itself; keep 60-100 ms gaps.
