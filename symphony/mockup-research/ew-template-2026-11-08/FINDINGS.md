# What EastWest's own REAPER template does (inspected 2026-11-08)

Source: **EastWest Templates 2, Hollywood Orchestra edition, REAPER version** (free download from EastWest for Hollywood Orchestra Opus owners; https://www.soundsonline.com/templates-2, zip https://media.soundsonline.com/zip/HO-Reaper-EW-2026-Template.zip, 264 MB). Built by Ryan Thomas (file paths in the project), tested with REAPER 7.52, Opus 1.6.1, Spaces II 2.5.3. It ships a "Midi Included" project: a ~92 s cinematic demo at 130 bpm played on HO Opus, fully mixed. That makes it the only free, official, EastWest-on-REAPER mockup with real performance data we found.

Everything below was read straight out of the .RPP (mixer, sends, ReaEQ bands, Spaces II JSON state, Opus JSON state decoded with the same gzip method as `mockup-kit/opus/opus_state.py`, and every MIDI event). Raw dumps: `opus-mics.txt`, `midi-report.txt`; parsers: `rpp.py`, `fxstate.py`, `midi.py` (all in this folder). The downloaded project itself is not kept (97 MB per .RPP).

## 1. Mic mix inside Opus

| Family | Close | Main | Other mics |
|---|---|---|---|
| Strings (legato, KS masters, sus, spiccato) | on, **−3 to −9 dB** under Main, Close panned to the seat (Vln I −0.31, Vln II −0.07, Va 0, Vc +0.33, Cb +0.62) | 0 dB, **full stereo, not re-panned** | Mid, Surround, Vintage not loaded |
| Brass (horns, trumpets, trombones, tuba) | on, **−6 to −10 dB** under Main, panned (Hn −0.25, Tpt +0.31, Tbn +0.25, Tuba +0.35) | 0 dB, full stereo | none |
| Woodwinds (fl, ob, ca, cl, bn, bcl, alto fl) | **0 dB (the main mic)** | **−3 to −21 dB** under Close (Fl −4.7, Cl −3.4, Bn −8.6, BCl −9.8, CA −11.6, Ob −20.6, AFl −15.7) | none |
| Harp | 0 dB | −9 dB | Mid 0 dB |
| Timpani | −8 dB | −7 dB | **Surround 0 dB** |
| Cymbals, tam-tam, glock, xylo | — | Main only | — |

Every mic sub-mix has panLeft/panRight at −1/+1 (full width). Seating comes from the panned Close mic plus a small REAPER track pan (Vln I −0.10, Vln II −0.21, Va 0, Vc +0.15, Cb +0.23; horns −0.13 to −0.18, trumpets +0.03 to +0.10, trombones +0.15, tuba +0.23).

**Compared with our kit (mix.json for mvt1 v621):** strings and most brass leave the patch's default mics (`mics: None`); winds use Close 0.5 / Main 0.8 (Main louder than Close); and every mic, including Main, is narrowed and re-centred on the seat (width 0.3 to 0.5, seats out to ±0.55). EastWest does three things differently that bear directly on "mushy":
1. Strings and brass get a Close mic 4 to 10 dB under Main. That adds definition and attack without making the sound dry.
2. Woodwinds use Close as the main mic and keep Main well below it. The hall comes from the shared reverb, not from the Main room mic.
3. The Main pair is never narrowed or panned. HO was recorded in seat, so Main already carries the position, and the panned Close mic does the rest.

## 2. Reverb

- **Opus's own reverb is off on almost every instrument** (on only in the extra layers of the combined "Full STR" pizz, spiccato and sustain patches, the Basses KS Master and the tam-tam). All the hall comes from **EW Spaces II on REAPER send tracks, one per section**, each 100 % wet, true stereo, the full IR (no envelope truncation), and rear-position impulses ("L/R Rear N"). Pre-delay: strings 19.6 ms, winds 18.5 ms, brass and perc 10 ms:
  - STRING VERB: "S. Cal. Hall Strings TS RR 3.3s"; send from the STRINGS bus at **−5.6 dB**
  - BRASS VERB: "S. Cal. Hall Brass TS RR 3.3s" (its impulse files are the hall's Horns position); send −8.8 dB
  - WW VERB: "San Francisco Hall TS RR 3.4s"; send −8.4 dB
  - PERC VERB: "Northwest Hall TS RR 2.6s"; sends −8.8 (keys/harp) and −6.4 dB (perc)
  - CHOIR VERB (Hamburg Cathedral 4.0 s) and LONG VERB (Abandoned Abbey 6.0 s) are present but receive nothing in the demo.
  - Plus an "ALGO GLUE" ReaVerbate return (+5.8 dB fader) fed from every section at −6 to −10 dB.
- Sends come from the **section bus**, post-fader, so the CC1/fader balance and the reverb level move together.
- **Every reverb return has an EQ before Spaces:** high-pass at **87 to 100 Hz**, a **−5 to −7 dB dip around 2.5 to 2.7 kHz**, and a low-pass at **5.6 kHz** (strings 8.5 kHz). This keeps low-mid and presence energy out of the tail, which is the usual cause of a mushy hall.
- Ours: a single Opus-internal convolution (S. Cal Hall Perc TS FR 3.3 s, truncated with endPos 0.5), low cut 160 Hz, high cut 5.5 kHz. Filtering is similar; the EastWest version uses section-matched IRs and pulls the 2.5 kHz band out of the tail.

## 3. Bus and master EQ (ReaEQ)

- STRINGS bus: HPF 53 Hz, **−2.2 dB at 456 Hz**, **−5 dB at 1 kHz** (wide), **+4 dB high shelf at 4.7 kHz**
- BRASS bus: HPF 41 Hz, **−5.4 dB at 475 Hz**, **−7.8 dB at 821 Hz**, +4 dB shelf at 7.5 kHz
- WOODWINDS bus: −5.1 dB at 447 Hz, −3.1 dB at 1 kHz, −4.7 dB at 2.2 kHz, +5.1 dB shelf at 7.6 kHz
- Harp: HPF 183 Hz, −8 dB at 304 Hz and 1.27 kHz, +8 dB shelf at 7.7 kHz
- Timpani: HPF 44 Hz, +8.6 dB at 84 Hz, −11.5 dB at 385 Hz, +9 dB shelf at 7 kHz
- Master: ReaComp → ReaEQ (HPF 42 Hz, −1.6 dB at 167 Hz, −1.9 dB at 1.18 kHz, +0.8 dB shelf at 8 kHz) → ReaLimit

The pattern is the same on every section: **cut 450 Hz and 800 Hz to 1 kHz by 2 to 8 dB, add a 4 to 5 dB shelf above 5 to 7 kHz.** These are the frequencies where close-miked samples plus a hall pile up.

## 4. Performance data (MIDI)

- **Dynamics are CC1 only.** No CC11 anywhere; one CC7 lane on harp and timpani. CC1 is drawn densely on every sustained or legato line: **7 to 13 points per second**, using the full 0 to 127 range (medians 57 to 79). Short-note tracks carry sparse CC1 (2 to 6 per second) and rely on velocity.
- **Velocity on legato patches is high and varied:** 57 to 124, median about 92 to 98, 26 to 29 distinct values per part. (My understanding, not checked against the manual: in HO legato patches velocity affects the transition and attack, so high velocity gives quicker, clearer note changes.) Spiccato is held in a narrow band (65 to 69); pizz 38 to 79.
- **Legato overlaps:** median **45 to 80 ms** of overlap into the next note on string legato lines, and 33 to 58 ms on winds and brass.
- **Repeated notes:** the next attack comes **20 to 45 ms after the note-off** on legato lines (some at 0 on violas), and **40 to 60 ms** on short-note KS tracks.
- **Timing:** string legato parts are mostly quantized (84 to 97 % of onsets exactly on a 16th). Winds and brass were played in live: only 20 to 50 % on the grid, offsets within ±58 ms, **mean slightly early (−2 to −13 ms; bassoon median −19 ms)**. No track delays or negative offsets are used anywhere.
- Durations of short notes: spiccato about 70 ms, staccatissimo about 110 ms, pizz about 125 ms (at 130 bpm).

## 5. What to try in our mockup (suggestions for the Movement I guide)

1. Strings and brass: load Close at about −6 dB (0.5) under Main 1.0, pan only the Close mic to the seat, and leave Main at full width.
2. Woodwinds: flip to Close 1.0 / Main about 0.35 (−9 dB), with Oboe Main lower still.
3. Turn Opus's reverb off and use Spaces II as REAPER sends per family (same IR family, about 3.3 s, pre-delay 10 to 20 ms), sent from section buses. Put an EQ before each Spaces: HPF 90 to 100 Hz, −5 to −7 dB at 2.5 kHz, LPF 5.6 to 8.5 kHz.
4. Section-bus EQ: −2 to −5 dB around 450 Hz, −3 to −8 dB around 800 Hz to 1 kHz, +4 dB shelf at 5 to 7 kHz.
5. Keep the repeated-note gap at 20 to 60 ms and the legato overlap at 45 to 80 ms; use legato velocity of 90 or more where a clear change of note is wanted.
6. Use EastWest's demo, rendered on Dan's Mac with Dan's own instruments, as a reference track for spectrum and dry/wet comparisons. This needs Dan's go-ahead: 264 MB download, plus any Opus instruments it calls that are not installed.

## Other sources found (not inspected)

- EastWest ComposerCloud+ edition of the same template (same page; needs CC+).
- Ryan Thomas's paid EastWest template with full demo production (synthestration.com/product/rt-eastwest-template/); Synthestration's paid Cubase/Logic project files ("Beyond the Storm", "Symphonic Explorations").
- Spitfire BBC SO Discover (free) plus a free REAPER template on reaper.blog (2020).
- Sonuscore's free demo MIDI files (sonuscore.com/demos-and-midifiles/).
- VI-Control's "Consolidated list of MIDI mockups and project files for study" thread (blocks automated fetches; readable through Dan's Chrome).
- Young Composers forum: a free beginner masterclass with project files, and a Polar Express mockup with MIDI download.

# Part 2: deeper read of the performance data (2026-11-08, later)

Sources: the HO demo above, plus the **ComposerCloud+ edition's demo** (a different 94 s cue by the same author, using the same mix framework; HO instruments are set up the same way down to the dB). Reports: `artic-report.txt` (per-articulation stats, keyswitch notes excluded), `ccshape-report.txt`, and `artic-report-cc.txt` for the CC+ demo. Both demos agree on every point below.

## 6. The CC1 macro, and a caveat from our own measurements
- Every KS Master (strings, brass, winds, choir) has an Opus macro, "Mod + Expression Combo", on MIDI CC1. It drives controller_1 and controller_11 together on a linear 0-1 curve, so the one CC1 lane moves the dynamic-layer crossfade (CC11) and the non-vib/vib crossfade (CC1) together. The dedicated "Leg Slur + Port LITE" legato patches have no macro and play dynamics on CC1 directly.
- Caveat: our LEARNINGS (section 3) measured that holding the woodwind KS Masters' CC1 between about 55 and 76 leaves both the Non Vib and the Vib layers sounding, which doubled the amplitude modulation. EastWest's sustained lines sit at CC1 medians of 57 to 79, which is right in that zone. If the macro is tested, measure mp-mf sustained woodwind and string notes for that doubling, and consider a non-linear macro curve that steps across 55-76 quickly. The macro has a spline (`splineSegments`) that allows this.

## 7. Short notes: CC1 parked high, dynamics by velocity only
- On string short rows (Staccatissimo, Spiccato) CC1 sits at **118-127** (so CC11 is also at the top through the macro), and the dynamic comes from **velocity alone: medians 24-52**. Brass and wind shorts: velocity 62-95, CC1 75-127.
- So soft shorts play the soft recorded samples with no extra CC11 attenuation. Our LEARNINGS found the same double-attenuation problem on the harp (velocity plus CC11 both lowering soft notes) and fixed it by holding CC11 at 110. Worth testing on string and wind shorts: hold CC11 at 110-127 during short-note passages and map the printed dynamic to velocity.
- Short notes are written shorter than their slot: string shorts 60-90 ms and brass 70 ms at 130 bpm (a 16th is 115 ms); wind staccatissimo about 90 ms. The sample's own release supplies the tail.
- Short notes are **exactly on the grid** (100 % of onsets in both demos). None of the short-note timing is humanized.

## 8. CC1 shape: phrase-level, not note-level
- **Across legato note changes CC1 is flat:** within ±200 ms of a legato onset the change is 0 at the median, with an IQR of −3..+1. There are no per-note bumps and no dip before an onset.
- **Phrase starts (after a gap of more than 150 ms):** about half start flat. The rest swell after the onset: the upper quartile is +8 at 100 ms, +12 to +15 at 200 ms, +18 at 400 ms and +23 to +24 at 800 ms. CC1 never moves before the onset.
- **Phrase ends:** a quarter to a half taper into the release. The upper quartile is 13 to 37 CC units higher 0.25 to 1 s before the note-off. Many final long notes end at CC1 0 (a fade to nothing).
- **Long notes (over 1.2 s)** take one of three shapes: a swell to a late peak (peak at 70 to 100 % of the note), a hairpin with the peak at 40 to 60 %, or a decay to 0.

## 9. Track layout and legato
- Strings: each section has a **dedicated legato track** ("Leg Slur + Port LITE" patch, with the LegatoSpeed and RTKiller scripts on) for melodic lines, plus a KS Master track for shorts, sustains and tremolo. Brass and winds play everything on their KS Masters, with the Leg Slur MAX row for melodies.
- Legato velocity: strings 57-124 (median 92-98); winds and brass 80-111 (median about 90-105). `USE_VELO_SPEED` is on, mapping velocity 30-127 to legato speed.
- Legato overlap: strings 41-80 ms; winds and brass 24-57 ms (CC+ demo 31-48 ms).
- Legato timing: string legato lines are mostly on the grid (84-97 %). Wind and brass legato lines were played in: 37-73 % of onsets sit ahead of the grid, by about 10-30 ms. Our kit's legato leads (0.10-0.20 s) are much larger because they were fitted to measured transition lag, so this is not a reason to cut them. It only shows that EastWest does not compensate for legato lag at all.
- Keyswitches sit 40-800 ms before the note they switch (typically 100-600 ms), almost never on the same tick.

## 10. Opus release times
- EastWest mostly leaves the patch release envelopes alone: string KS Masters 931 ms, legato and brass 700 ms. A few are shortened: Basses legato 56 ms, oboe 177 ms, tuba 372 ms, 1FH 562 ms. Our 150 ms caps at mf-ff are much shorter than any of these. The template keeps release tails and controls blur with the reverb EQ and shorter sends instead.
