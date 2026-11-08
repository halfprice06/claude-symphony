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

- **Opus's own reverb is off on almost every instrument** (on only in the extra layers of the combined "Full STR" pizz, spiccato and sustain patches, the Basses KS Master and the tam-tam). All the hall comes from **EW Spaces II on REAPER send tracks, one per section**, each 100 % wet, **pre-delay 19.6 ms**, true stereo:
  - STRING VERB: "S. Cal. Hall Strings TS RR 3.3s"; send from the STRINGS bus at **−5.6 dB**
  - BRASS VERB: "S. Cal. Hall Brass TS RR 3.3s"; send −8.8 dB
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
3. Turn Opus's reverb off and use Spaces II as REAPER sends per family (same IR family, about 3.3 s, pre-delay about 20 ms), sent from section buses. Put an EQ before each Spaces: HPF 90 to 100 Hz, −5 to −7 dB at 2.5 kHz, LPF 5.6 to 8.5 kHz.
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
