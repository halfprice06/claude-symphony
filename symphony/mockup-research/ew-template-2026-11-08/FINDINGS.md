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

# Part 3: a hand-played pro mockup for comparison (Ashton Gleckman's "Polar Express" MIDI)

Source: the MIDI file of Ashton Gleckman's Polar Express suite mockup, which he shared publicly as a free download (linked from a Young Composers forum thread; a Google Drive file, 36 tracks, 62 s at 120 bpm). Libraries: Spitfire Symphonic Woodwinds, Brass and Strings, Chamber Strings, Jaeger violins, NI Symphony Series, 8Dio choirs, NI The Gentleman piano. This is a different library family (CC1 = dynamics, CC11 = expression), so the absolute values don't transfer, but the shapes and timing practice do. The MIDI itself is not kept in the repo (it is a mockup of a copyrighted score); the statistics are in `polar-report.txt`, made by `scripts/smf.py`.

- **CC lanes are far denser than EastWest's: CC1 at 13-44 points/s** (EastWest 7-13), with a second CC11 lane on winds and choirs (15-22/s). So dynamics (CC1) and expression (CC11) are drawn separately.
- **Every phrase swells in.** Unlike EastWest, where about half of phrase starts were flat, here the median moves: CC1 +5 by 200 ms, **+14 by 400 ms, +24 by 800 ms** (IQR +17..+35 at 800 ms). CC11 adds +10 / +16 on top. Nothing moves before the onset.
- **Every phrase tapers.** The median CC1 is **19 units higher 1 s before the final note-off** and 8 units higher 0.5 s before (CC11: 11 and 4).
- **Notes inside a legato line shade down slightly after they start:** the median CC1 is −1 at 200 ms and −2 at 400-800 ms after a legato onset (IQR −16..+10). Each note leans a little into a gentle diminuendo, and the next phrase-level swell lifts it back.
- **Timing: winds and choirs are quantized and then shifted early by a fixed amount per track** (92-100 % of onsets share one offset): oboe −27 ms, clarinets −38 / −46, bass clarinet −17, bassoons −40 / −85, flute −75, choirs −25 / −27, piano −43. Strings and brass were played in instead (no common offset; −20 to −120 ms early on average). **Percussion, bells and sub bass sit exactly on the grid.** This is the usual negative-track-delay practice: each patch is moved early by its attack latency, and percussion is not moved.
- **Legato overlaps are long for these libraries:** 46-230 ms (Spitfire winds 70-230 ms, strings 46-130 ms), against 24-80 ms in EastWest's demo. The right overlap depends on the patch's legato script.
- **Legato velocities** run 67-115 (median about 90-100), the same range as EastWest's.

What this adds for our mockup: (a) shape every phrase, not some: a swell of about +15 by 0.4 s and +25 by 0.8 s after the first onset, and a taper of about 20 over the last second; (b) a small per-note lean-off inside legato lines; (c) a fixed per-patch early shift for wind legato and chorale lines, with percussion left on the grid. Our kit already does (c) through measured lead tables.

# Part 4: nineteen more expert mockups (2026-11-08, evening)

Dan asked for as many human expert examples as possible. VI-Control's "Consolidated list of MIDI mockups and project files for study" (read in Dan's Chrome) and Ashton Gleckman's Film Score Hub led to these free files. All were downloaded and analysed in the cloud; nothing was put on the Mac. The MIDI files and projects are not kept in the repo (they are mockups of copyrighted scores). The statistics are in `expert-report.txt` and Bernard Duc's mix in `duc-mix.txt`; the scripts are `scripts/smf2.py`, `rubato.py`, `async.py`, `xsum.py`, `rppmix.py`, `rppau.py` and `proq2.py`.

- **Bernard Duc, Mahler 5 Adagietto** (Cinematic Studio Strings, Embertone solo violin, VSL harp): the full REAPER project and the MIDI.
- **Bernard Duc, LOTR "The White Tree"** (VSL woodwinds, Spitfire Symphonic Brass, Cinematic Studio Strings with Spitfire Studio Strings, Spitfire percussion): the full REAPER project and the MIDI.
- **Star Wars Main Title (2024)** (Cinematic Studio Strings and Solo Strings, CS Brass, CS Woodwinds, Hans Zimmer and Spitfire Studio percussion): 64 tracks, played in, with a tempo map.
- **Ashton Gleckman, 11 suites** (Atonement, Band of Brothers, The Danish Girl, The Da Vinci Code, Harry Potter 7/8, The Hunger Games, The Imitation Game, The Lion King, The Martian, Pirates of the Caribbean, The Shape of Water), mostly Spitfire (Albion, Mural, Chamber Strings, BOI) with CSS, 8Dio and others.
- **A four-cue set**: Finding Nemo Main Title, Concerning Hobbits, No Time to Die "Final Ascent" and "Matera" (Spitfire Originals, Intimate Strings, LABS, Symphonic Strings).
- **Hans Zimmer "Time"** (VSL brass, hybrid) and **James Newton Howard "The Village"** (track names lost in export; all played in).

The libraries differ from ours (CC1 means dynamics in all of them), so absolute CC values don't carry over. The shapes, timing and mix choices do.

## 11. Phrase dynamics: every phrase is an arch, and long notes move
Measured on CC1 for every phrase of 1.5 s or more (a phrase ends at a gap over 150 ms), as CC1 minus that phrase's peak:
- **Phrases start well below their peak and end well below it.** The per-file median start is 8-60 units under the peak (17 of 20 files: 17-60), and the end is 2-62 under (15 of 20: 13-62). The files with ends near the peak (LOTR, Hobbits, Pirates, Martian, HP) are full of phrases that build into the next one.
- **The peak sits near the middle**: median peak position 0.33-0.62 of the phrase in 18 of 20 files. The exceptions are Hobbits (0.30) and Star Wars (0.25); in Star Wars the fanfare notes are accented and then decay.
- **Phrase range** (peak minus lowest point): median 16-73 units per file, 30-60 in 12 of 20 files.
- **Long notes (1.2 s or more) are almost never held flat.** Flat (within 2 units of the onset value all the way) is 0-13 % of long notes in 15 of 20 files; only Hobbits (50 %), LOTR (43 %), Mahler (25 %), Star Wars (21 %) and Matera (18 %) have more. Typically a third to a half rise 4 or more units by their middle, and about half fall 4 or more from the middle to the end. In Star Wars, long brass and string notes decay: median −11 at half-way and −23 at the end.
- **Nothing moves before the onset** (median change in the 300 ms before a phrase starts: 0 in 17 of 20 files, −1 to +3 in the other three).

Compared with our plan item 7 (+15 by 0.4 s, +25 by 0.8 s, a taper of about 20 over the last second): the experts' arch is roughly symmetric. The start sits about as far under the peak as the end does, and the peak comes around the middle of the phrase, not in the first second. In lyrical music the depth is 30-60 units of a 0-127 lane.

## 12. Timing, overlaps, repeated notes and velocity
By instrument family (family guessed from track names; median per track, IQR in brackets):

| | string longs | brass | winds | string shorts | perc |
|---|---|---|---|---|---|
| tracks | 220 | 79 | 59 | 96 | 80 |
| onsets exactly on the 16th grid | 0 % [0..3] | 0 % [0..3] | 0 % [0..3] | 16 % [0..100] | 9 % [0..98] |
| legato overlap | 52 ms [34..105] | 47 ms [35..67] | 26 ms [20..64] | | |
| gap between repeated notes | 90 ms [66..136] | 98 ms [72..114] | 63 ms [43..75] | 116 ms [101..143] | 116 ms |
| velocity spread (IQR width) | 18 | 16 | 17 | 15 | 22 |
| r(velocity, CC1 at onset) | 0.35 | 0.33 | 0.31 | 0.05 | |
| CC1 points per second | 8.3 | 10.2 | 7.2 | | |

- **Sustained lines are played in, not quantized.** Shorts, percussion and harp are sometimes quantized and sometimes played.
- **Repeated notes get a real gap: 60-100 ms, 2-3 times our plan's 20-45 ms on legato lines.** The one exception is Star Wars, where 28 tracks let repeated notes touch (gap 0) on patches that re-attack every note. Dan's mockup notes asked for audible separation on repeated notes; this is the expert value for it.
- **Legato velocity follows the dynamic** (r about 0.3-0.35): louder passages are played harder, and the middle half of a track's legato velocities spans about 16-18 steps. On shorts, velocity is set independently of CC1 (r 0.05).
- **Quantized tracks get a fixed per-track shift.** Star Wars: every pitched track +13 ms against the grid, timpani, snare and taiko 38-43 ms earlier than that, glockenspiel and cymbal 16 ms later, harp exactly on the grid. Several Ashton suites shift tracks by −10 to −60 ms (Pirates by +11 to +15 ms).
- **Tutti entries are spread.** When three or more tracks start together, the first and last are a median 36-55 ms apart in the orchestral pieces (Star Wars 37, Mahler 36, LOTR 50, Band of Brothers 55, Lion King 48, The Village 55) and 1-35 ms in the rest, which quantize more tracks. Only 0-12 % of orchestral entries have every track exactly together. Brass and string longs sit 0-16 ms ahead of the entry's median (0-6 ms in the orchestral pieces); percussion and harp mostly sit on it or up to 16 ms behind. These are MIDI times, so part of the spread compensates slower attacks and the audible spread is smaller. Our kit aligns each note's measured attack to the beat (Dan asked for attacks on the beat), which makes entries tighter than any of these.

## 13. Tempo
- **Duc's Adagietto follows a real recording beat by beat.** The project holds a commercial recording on a track whose master send is off, and the MIDI tempo map has 412 tempo events over 103 bars, a change on 98 % of beats. Each beat deviates from the local (4-bar) median by a median 8 % and by 23 % at the 90th percentile. The fourth beat of the bar averages 7 % slower than the others. 20 of 403 beats (5 %) are more than 25 % slower than the local median: the breaths at phrase ends. The 4-bar median runs from 30 to 76 bpm; the climax (bars 50-66, median 73) moves at 1.8 times the opening (bars 1-12, median 40), following Mahler's own tempo changes and the conductor's push.
- **The film-style mockups keep the tempo steady inside a section.** Rits are stepped ramps (Star Wars: about −3 % per beat over 6 beats, plus 5 held beats more than 25 % slower at section joins), and the live feel comes from played-in note timing.
- **For us:** our phrase arcs push 1.5 %, slow 4-8 % over the last two beats (2-5 % on sub-phrases, 5-12 % at section cadences), and give the apex beat 4 %. A real performance of a late-Romantic adagio moves more: every beat varies by about 8 %, and the breath at a phrase end is often 15-30 % slower (49 beats over 15 %, 20 over 25 %). Movement II (Adagio) is the place to test larger values.

## 14. Mix: Bernard Duc's REAPER projects
Both projects use the same template. The instruments run in Vienna Ensemble Pro; each instrument comes back on its own audio track; the returns feed group buses (Woodwinds −5.4 dB, Brass −5.4, Strings Hi −5.4, Strings Lo −3.7 in LOTR and −5.4 in Mahler, Percussion −2.1), each with Airwindows Console5, plus one shared Hall bus. The LOTR master has Pro-Q 2, Airwindows Logical4 (bus compressor), ToTape5 (tape) and a "Concert Hall Short" VSR S24 instance (decay about 1.2 s). The Mahler master FX are bypassed.
- **One shared algorithmic hall, shorter and darker than ours.** Relab VSR S24. LOTR: "Large Warm Hall", with values that read as decay 2.45 s, low cut 184 Hz and high cut 3.0 kHz, returned at −6.6 dB. Mahler: "Cincinnati Music Hall", decay 2.1 s, low cut 184 Hz, high cut 14.6 kHz, returned at −5.5 dB. The preset names are certain; the parameter names are inferred from their values. Our plan item 2 uses EastWest's 3.3-3.4 s IRs with a 5.6 kHz low-pass (strings 8.5 kHz).
- **Less reverb on low and short material.** Post-fader sends per instrument: violins, violas and brass 0 dB; celli and basses longs −1.6 dB; low string shorts −7 dB; the solo violin +3.6 dB (Mahler). Dan's last reverb note was "still a bit mushy"; the low-string sends are a direct fix to try.
- **Dry VSL woodwinds get their own room and are darkened to sit behind the strings.** The woodwind folder has TDR Proximity ("Depth Enhancer" preset), then Pro-Q 2 (−10.7 dB at 158 Hz, −10.5 dB at 3.7 kHz, low cut 76 Hz, high shelf −16.7 dB at 19 kHz), then an insert VSR S24 "Cincinnati Music Hall", and then the shared Hall send. Single flutes, oboes and clarinets add cuts of −9 to −16 dB at 117-192 Hz, −4 to −9 dB at 0.8-2 kHz and a −3.5 to −7.6 dB high shelf at 14-15 kHz. HO woodwinds are recorded in a hall, so the insert room doesn't apply to us; the presence and top cuts that push winds back might.
- **String EQ on CSS** (a library recorded in a hall, like HO), then an Ozone 5 exciter on violins and violas:
  - Violins: low cut 65 Hz (30 dB/oct), a wide −0.7 to −2.5 dB dip at 490-710 Hz, +1.9 to +3 dB at 8.8-10.8 kHz, a +0.5 to +2.5 dB high shelf at 12-15 kHz.
  - Violas: low cut 70 Hz, −1.3 to −2.5 dB at 590-607 Hz, a +2.5 to +4 dB high shelf at 7.4 kHz.
  - Celli: low cut 39-50 Hz, −1.5 to −3.4 dB at 129-558 Hz, +1.8 to +2.6 dB at 2.7-3 kHz, +1 to +3.5 dB at 9.3-12.9 kHz.
  - Basses: −2.4 to −3.6 dB at 205-250 Hz, +1.6 to +3.6 dB at 9.4-10 kHz.
  - Brass group: −6.9 dB at 500 Hz, +2.7 dB at 3.6 kHz; trumpets +2 to +3 dB at 10 kHz; tuba −4.3 dB at 143 Hz.
  This is the same direction as EastWest's section EQ (cut 450 Hz to 1 kHz), with smaller cuts and the lift placed at 9-11 kHz instead of a shelf from 4.7 kHz.
- **A room-noise bed (Mahler).** A 62.6 s recording of room noise is looped under the whole piece on its own track (fader +5.6 dB, item gain +3.4 dB, low cut 84 Hz) and sent to the hall at −1.6 dB. It gives the mockup the constant noise floor of a real hall recording, so rests and soft entries never fall to digital silence.

## 15. What to try in our mockup (for the Movement I thread to test)
1. **Repeated-note gaps of 60-100 ms** (winds about 60, strings about 90, brass about 100, short rows about 115) in place of 20-45 ms, measured for audible separation (Dan's note on repeated notes).
2. **A symmetric phrase arch**: the peak around 40-55 % of the phrase, start and end both well under it (in lyrical lines 15-30 units or more, scaled to the printed dynamic, with printed hairpins taking precedence). Give long notes motion of their own (a rise to the middle or a fall at the end) instead of flat holds.
3. **Reverb**: a test with a shorter, darker hall (decay 2.1-2.5 s, high cut 3-6 kHz, low cut about 180 Hz), sends about 1.5 dB lower for celli and basses and about 7 dB lower for low string shorts. This targets "still a bit mushy".
4. **Legato velocity tied to the dynamic** (louder passages higher), keeping the legato-speed rules.
5. **Larger rubato in Movement II**: phrase-final beats 15-30 % slower and a stronger push into climaxes, within the printed tempos.
6. **A small ensemble spread** (a fixed ±10-20 ms per track around the beat) as an A/B test only, since Dan asked for attacks on the beat.
7. **A quiet room-noise bed** under the whole movement, just audible in rests.
8. **String EQ variant**: the lift at 9-11 kHz instead of the 4.7 kHz shelf, then compare.

# Part 5: two Cubase projects with VSL instruments (2026-11-08, night)

The two Cubase projects listed under "Leads not taken" are now read: Jerry Goldsmith's Mulan overture (68 MIDI tracks, 8,532 notes) and Joe Hisaishi's Howl's Moving Castle symphonic variation "Merry-Go-Round" (63 tracks, 14,421 notes). There was no parser for Cubase files, so I wrote one (`scripts/cprlib.py`, `cpr2mid.py`). It reads the tempo track, every MIDI part's notes and controller points, and Cubase's controller curves, and writes a MIDI file that the Part 4 scripts analyse. Checks: the tempo track's stored times in seconds match its tempos to within 10 ms on 289 of 290 segments, and the rule used for placing parts in time lines up the parts with each other best on 30 of the 35 tracks where the possible rules differ (the other five tie or hardly overlap with any other part). Both projects also contain their whole Vienna Ensemble Pro project, which holds the instrument mixer: faders, pans and reverb sends (`scripts/vepdump.py`). Statistics are in `cubase-report.txt`, mix settings in `cubase-mix.txt`.

Libraries: VSL Synchron winds, brass, percussion, harp and pianos in both, run in Vienna Ensemble Pro. Strings are Synchron Strings Pro with Synchron Elite Strings in Mulan, and Duality strings (not VSL) in Howl's. Mulan also has a few dry VSL "Synchronized" instruments. Synchron instruments are recorded on a scoring stage, so they are wet like HO.

## 16. Timing and tempo
| | Mulan | Howl's |
|---|---|---|
| onsets exactly on the 16th grid | 80-100 % on most tracks (quantized) | 2-9 % on wind, brass and string tracks (played in) |
| tutti entries: first-to-last spread | median 8 ms; 29 % exactly together | median 32 ms [21..44]; 1 % exactly together |
| tempo events | 139 | 153 |
| beats with a tempo change | 20 % | 19 % |
| beat deviation from the local median, 90th percentile | 8 % | 5 % |
| beats more than 15 % / 25 % slower than the local median | 20 / 4 | 26 / 6 |

- **Both use a detailed tempo track for the breaths and rits**, as Duc does. Mulan keeps every note on the grid and gets all its movement from the tempo track; Howl's plays the notes in as well, with the same entry spread as Part 4's orchestral files (36-55 ms).
- **Repeated notes in Howl's nearly touch** (gaps 5-15 ms). Synchron Player switches to repetition samples by itself, which HO does not, so Part 4's 60-100 ms stays the value for us.

## 17. Dynamics lanes and curve shapes
- **Which lane carries the dynamics differs.** Mulan: CC8 on winds and brass (CC11 mostly parked at 127), CC1 on strings. Howl's: CC2 on strings; on winds and brass CC8 and CC11 stay at 127 in three quarters of the phrases, and the dynamics come from velocity (30-76 distinct velocities per wind track, middle half 16-32 steps wide).
- **Mulan's winds and brass end phrases with deep fades.** Phrases start at the top of the lane and drop a median 43-77 units (of 127) in their last second, depending on how the curves are read (below). Long notes fall a median 27-39 by their end, and 62 % fall 4 or more units from the middle to the end. Strings start a median 21 units under the phrase peak and taper about 6-10 in the last second.
- **These two files do not show Part 4's centred arch**: the peak sits at or near the phrase start. Part 4's arch rests on 20 files and stays the main rule; Mulan adds that a wind or brass phrase before a rest can fade almost to nothing.
- **Curve shapes.** Cubase draws a bent line between two controller points (a quadratic Bezier with one control point). In Mulan, 3,609 of 7,433 controller segments are bent. Rising segments put the control point at 34 % of the time and 88 % of the rise: the value gets most of the way up early, then settles. Falling segments put it at 72 % of the time and 0 % of the drop: the value holds, then falls in the last quarter. Howl's: rising segments are close to straight (49 %, 54 %), falling ones hold and drop late (68 %, 27 %). This assumes Cubase measures the control point from the segment's start value, which fits the music (the fall lands on the held last note). Measured the other way, falls would start early instead.

## 18. Mix
- **Instruments recorded in a hall get little or no extra reverb.** Howl's sends each channel to one shared hall (Cinematic Rooms "Amethyst Hall") at: woodwinds −10 dB, strings −10, basses −16, horns −12, trumpets and the six-horn patch −16, timpani −6, snare −8, bass drum −3; bassoons, contrabassoon, trombones and tuba have no send. Mulan sends only its dry VSL instruments (oboe and clarinet −10), an extra "violins 1 wetter" layer (−4), a doubled violin layer (−10), timpani, taiko and the solo violin (−12); its Synchron instruments have no send at all. Like Duc's low-string sends, this keeps reverb off the low instruments, and it supports giving HO's low brass and bassoons little or no send.
- **A dark hall on the whole mix.** Both put a Lexicon Random Hall in the Cubase mixer: pre-delay 25 ms, reverb time 2.54 s (Mulan) and 3.57 s (Howl's), bass multiplier 1.25x and 1.75x, high frequencies in the tail decaying fast above 2.25 kHz ("heavy" damping), the reverb output low-passed at 1.8 kHz and the early reflections at 2.75 kHz, wet at 35 % (Mulan) and 8 % (Howl's). Both changed only the time, the bass multiplier and the mix of the factory preset, so the filters are the preset's, but both kept them. Ozone Match EQ and Maximizer follow. Mulan has a second Cinematic Rooms ("Subtle Hall") in Cubase.
- Mulan's Vienna Ensemble Pro project has a channel named "Roomtone" (MIR Pro on it, but no instrument and no audio file in the project), so it may have been a room-noise bed like Duc's; I can't confirm it.
- **Brass as narrow sources (Howl's).** Horns sit left (pan centre 0.08-0.24 on a 0-1 scale, stereo width 15-47 %), trumpets right (0.78, width about 43 %), trombones centre to right (0.50-0.72), timpani far left and narrow, marimba far right, second violins right of centre. Brass and percussion faders are +6 dB against 0 dB for winds and strings; the master bus is −6 dB.

## 19. Additions to the Part 4 suggestions
1. **Reverb sends by register**: no hall send (or −16 dB or lower) on low brass, bassoons, contrabassoon and basses, about −10 dB on the rest; percussion keeps its send. This extends item 3.
2. **A darker hall return**: as an A/B, low-pass the hall return at 1.8-2.3 kHz, darker than the 3-6 kHz of item 3.
3. **Curve shapes**: crescendos get most of the way up early and then settle; diminuendos hold and fall on the last held note. Winds and brass may fade almost to nothing before a rest.
4. **Narrower brass**: narrow the brass stereo width and pan horns left, trumpets right, as an A/B.

## Leads not taken
- Lorne Balfe's "The Crown" main titles and five more MIDI files from 14th Street Music's Hightail shares (Genius season 2, Bad Boys for Life, Penguins of Madagascar, Kung Fu Panda 3, 6 Underground): downloaded to Dan's Mac with his OK, but the cloud cannot read his Downloads folder. They can be analysed once they are uploaded to the project.
- Ludwig Göransson's "Can You Hear the Music" (Oppenheimer) MIDI: the Dropbox link needs a key that the post doesn't give.
- VSL Masterpieces: the page is gone, and VSL staff say on their forum that those files are no longer available.
