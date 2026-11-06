# Hollywood Orchestra Opus Edition: digest of the May 2021 manual for the movement I mockup

Written 2026-11-06 for the `symphony/mvt1/reaper-v621` loop. Source: `text/EW-Hollywood-Orchestra-Opus-Edition-User-Manual-2021.txt` (228 PDF pages), checked against the Dec 2025 library manual and the Oct 2025 Opus engine manual. Where they disagree, the 2025 manuals win, and the installed patch files win over both (section 9).

How to read the citations:
- `p.N` is a PDF page of the 2021 manual (render it with `pdftoppm -f N -l N -r 110 -png pdfs/EW-Hollywood-Orchestra-Opus-Edition-User-Manual-2021.pdf out`).
- `2025 p.N` is a PDF page of `EW-Hollywood-Orchestra-Opus-Edition-User-Manual.pdf` (Dec 2025).
- `Opus p.N` is a PDF page of `EW-Opus-Software-Manual.pdf` (Oct 2025).
- `(patch)` marks a fact read from the installed `.oib` files on `/Volumes/MAC DRIVE`, not from a manual. The 2021 manual has no range tables, and its woodwind and brass chapters refer to articulation tables that are not in this edition (p.108). Ranges below therefore come from the patch files.
- `(KIT §n)` is `mockup-kit/LEARNINGS.md`; `(M1 cNN)` is `symphony/mvt1/reaper-v621/loop/LEARNINGS.md`. Both are measurements made on this library.

Note names: EastWest names MIDI 60 "C3" (p.45, p.161; keyswitch "C0" = MIDI 24). This digest gives MIDI numbers and scientific names (MIDI 60 = C4). So the manual's timpani range "C1-A2" (p.124) is MIDI 36-57 = C2-A3 here.

## 1. What is installed for this score

| Library | Installed | Used in v621 mockup |
|---|---|---|
| Hollywood Strings Diamond (incl. 18 Violins, divisi, Full Strings, Ensemble) | yes | 1st/2nd Violins, Violas, Celli, Basses KS Masters |
| Hollywood Brass Diamond | yes | Solo French Horn (x4), 2 French Horns (a2), Solo Trumpet (x3), Solo Trombone (x3, incl. bass trombone), Solo Tuba KS Masters |
| Hollywood Orchestral Woodwinds Diamond | yes | Flute, Flute 2, Oboe (x2), English Horn, Clarinet (x2), Bass Clarinet, Bassoon (x2), Contrabassoon KS Masters |
| Hollywood Orchestral Percussion Diamond | yes | Timpani Flt KS, 32in Med Tam Tam, 18in Zildjian Sus Cymbal Cres (22in K Crash track silent in v621) |
| Hollywood Harp Diamond | yes | Harp Sus RR |
| Hollywood Solo Cello, Hollywood Solo Violin | licensed, not installed | none (the coda "Solo espr." is played by the Celli section) |

Diamond is 24-bit with all mic positions (5 or more), about 944 GB (p.14-15).

## 2. Controllers and note velocity, all libraries

### 2.1 What each input does

| Input | What it does in Hollywood Orchestra | Pages |
|---|---|---|
| Note velocity | Loudness and dynamic layer of short articulations (staccato, staccatissimo, marcato, pizzicato, percussion, harp). Cannot change mid-note, so it is used for shorts. | p.53, p.64, p.150; 2025 p.52 |
| Velocity on true-legato patches | Sets the legato transition timing, not loudness: about 50-60 gives a longer, slower transition, about 110-127 a shorter one. | p.144; 2025 p.52, p.91 |
| Velocity on sustain patches | Ignored on the KS Master sustain rows (measured: 485 accents 10-15 velocity lower rendered identically, M1 c06). Exceptions: brass Sustain Accent (velocity = accent loudness), brass Sustain Marcato (velocity = low-pass cutoff on the marcato attack), Mariachi Sustain (velocity = dynamics). | p.101-102 |
| CC1 (Mod Wheel) | Depends on the instrument. Strings and woodwinds: vibrato amount (CC11 has the dynamics). Strings LITE patches: dynamics and vibrato together. Brass sustains and legato: dynamics (4 layers), and near 127 it opens a low-pass filter for an overblown sound. Timpani rolls: 8 dynamic layers. Solo Cello: dynamics and vibrato linked. Harp "Bisbigliando MOD": bisbigliando level. "MOD" patches: selects the articulation. | p.45, p.64, p.101, p.106, p.124, p.151, p.82; 2025 p.52 |
| CC7 (Volume) | Sets a track's upper level relative to other tracks; not for shaping a line. | p.64, p.151 |
| CC11 (Expression) | Shapes loudness over time; on long instruments with more than one dynamic layer it crossfades the layers. All instruments fade to silence on CC11 (the old "Ni" niente patches are gone). | p.63-64, p.151; 2025 p.52 |
| CC5 | Legato / portamento time of the Legato and Portamento scripts (0 least, 127 most). | p.143-144 |
| CC14 | Repetitions Runs Script: 0-64 up samples, 65 repetition samples, 66-127 down samples (script turned off with the "Other" button). | p.96 |
| CC15 | Con Sordino script (strings): 0-63 off, 64-127 on. | p.143-144; 2025 p.90-91 |
| CC22 | True legato: 0-63 polyphonic, 64-127 monophonic (default). p.99 states the opposite for strings; p.105, p.112, p.144 and 2025 p.91 agree on 64-127 = monophonic. | p.144 |
| CC36 | Listed as "Round Robin Reset" (p.143, p.145). In the installed KS Masters CC36 is mapped as "Repetition: Reset RR" (patch). 2025 p.92 and Opus p.29-30: the sample round-robin reset uses the CC set in Preferences > MIDI > Round Robin; this machine's `/Library/Application Support/East West/Opus/Preferences.json` has `RoundRobinResetCC: 16`. | p.34, p.143, p.145 |
| CC57 / CC68 | Legato script on/off. 2021 says CC57 (p.143-144); 2025 p.90-91 and the installed patches say CC68. Use CC68. | p.143 |
| CC64 | Timpani and crotales "Sus Pedal" patches: off = short hits, on = long hits. In the KS Masters CC64 is mapped as "Repetition: Sustain" (patch). | p.124, p.126-127 |
| CC65 | Portamento script on/off. | p.143-144 |
| CC69 | Repetition script on/off. | p.143, p.145 |
| CC70 | Finger Position (strings): FP1 0-38, FP2 39-76, FP3 77-114, FP4 115-127. | p.63, p.143, p.145-149 |

### 2.2 Rules the manual gives for programming

- Send CC1 and CC11 before the first note of a track (a short ramp in the sequencer works) (p.151).
- Use CC7 or the track fader for each track's ceiling and CC11 for the line inside it (p.64, p.151).
- MAX patches hold the most dynamic and vibrato layers; LITE patches about half (p.62-63). The instrument description in the browser lists each patch's layer counts (p.56, p.62; 2025 p.51).
- Round robins: "RR" alone = 2 samples per note, "RRx3"/"RRx4" = 3 or 4. Opus continues the cycle from where it stopped, so a sequence plays differently on each pass unless the cycle is reset; automate the reset at the start and at important points (p.145; 2025 p.92).
- The Repetition script detunes the sample by a few cents or borrows a neighbouring note's sample on repeated notes. It is random, so renders are not repeatable with it on; the RR reset gives repeatable results (p.145).
- Monophonic true legato: a transition is played only when the next note starts with no significant gap after the previous one ends; the first note of a phrase has no transition (p.99, p.105, p.112). Brass and woodwind transitions only within an octave (D3 to D4 yes, D3 to D#4 no) (p.105, p.112). Two simultaneous legato lines need two instances, or CC22 polyphonic with the risk of wrong transitions (p.99, p.144).
- Short articulations have no release trails, only the room sound at the end of the sample. Hold short notes, and the last note of a staccato phrase, long enough for the room to ring (brass p.102, woodwinds p.110). String "Repetitions" and brass "Repetitions" are the exceptions; they do have release trails (p.94, p.103).
- Tempo-synced (TS) patches follow the host tempo; stay within about 10 bpm of the recorded tempo (2025 p.52; repetitions recorded at 170, 145 and 120 bpm, p.103).

### 2.3 Articulation switching and layering

- KS Master rows can be loaded or unloaded and each has its own volume knob (p.137; 2025 p.84). A keyswitch to an unloaded row is ignored (KIT §2).
- Trigger options per articulation: Keyswitch (any MIDI note C-2..G8), Keyswitch Range (with pass-through and offset), Program Change, Controller (a CC value range), Velocity (a velocity range) (p.160-162; Opus p.86-88).
- Behaviour per trigger: Exclusive (default: activating one row deactivates the others), Toggle, Temporary (active while the trigger note is held) (Opus p.86).
- The manual's own example of layering: a sustain on all velocities plus a staccato limited to velocity 110-127 gives an accent on hard notes (p.162, p.189-190; Opus p.87).
- Zones: per instrument key range, octave, group, voice limit (p.188-189, p.192). A voice limit that is too low drops voices; one note can use many voices (all mics, all crossfaded layers) (p.188, p.192). Patches here ship voice limits of 250 (brass, woodwinds, timpani) and 350 (strings) (patch).

## 3. Engine settings that affect a render

| Setting | What the manual says | This machine (read 2026-11-06) |
|---|---|---|
| Default preload size | HDD keeps the most of each sample in RAM, SSD (SATA) less, SSD (PCIe) least; "Never Preload" streams everything and needs very fast drives (RAID 0) (p.32-33; Opus p.27-28). | `PreloadSize: 1` (SSD/SATA; index order read from the Opus binary, KIT §11), `NeverPreload: false`. The samples are on a 10 TB USB exFAT drive reported as "Expansion Desk" (diskutil), a Seagate desktop model; the manual's setting for a hard drive is HDD. KIT §11 kept 1 on purpose. |
| Purge / Quick Load | A purged instrument loads samples as notes are played (yellow state) (p.43, p.59, p.134, p.191). | Not used; an offline 1x render from a USB drive needs the samples loaded. |
| Round-robin reset controller | p.34 (preference), p.143/145 (CC36); 2025 p.92 (the preference CC). | `RoundRobinResetCC: 16`. |
| Load with effects off | Loads instruments without their reverb (p.35, p.49). | `false`; the pipeline replaces every patch's reverb with one shared hall (KIT §12). |
| Multi-threaded reverb / voice renderer | p.33. | both off, 1 voice-render thread. |
| Plugin stereo outputs | Up to 16 stereo pairs; route mics to separate outputs (p.33, p.49-51). | 9. |
| Opus version | Movie Mixes need Opus 1.6.2 or later (2025 p.83). | 1.6.5. No Movie Mix data was found in the installed 1st Violins KS Master (patch), so the feature does not apply to these patches. |
| Multi-timbral use | Up to 16 instruments in one instance (p.52). Samples still load per instrument, so this does not save sample memory (inferred). | One instance per track. |

## 4. Mic positions, Player window and mixer

### 4.1 Microphones

| Mic | Where | Sound (manual) | Pages |
|---|---|---|---|
| Close ("C") | In front of each section | Presence, "far enough away to allow room for them to breathe". AKG C12, Neumann U47/U67, Nordic Audio Labs NU-47. | p.138-139 |
| Mid ("m") | Edge of the stage, about the middle of the first row | "Definition without the sound of close proximity". Neumann KMi, KM 254, Sony C37A, U-47. | p.138-139 |
| Main ("M") | About the fifth row | More room than direct sound; "big, unified sound". Three Neumann M50 (Decca tree) plus Brauner VM1 KHE outriggers. | p.138-139 |
| Surround ("S") | High at the back of the stage | Lush, little definition; adds depth when mixed in. Neumann KM 83. | p.138-139 |
| Vintage ("v") | Like Surround | Classic Hollywood sound; the producers recommend a little Close with it. RCA 44 ribbons. Surround and Vintage cannot be loaded together (2025 p.86). | p.138-139 |
| Stage | Two outriggers | Wider image; only on the expansion instruments (18 Violins, new brass and wind ensembles). | p.138-139 |

- Each mic is a sub-mixer channel with volume, pan, on/off (load/unload from RAM), mute and solo (p.139, p.196). Loading a mic adds sample memory (p.139, p.196; KIT §12).
- Harp, Solo Cello and Solo Violin have vintage alternatives for Close and Mid instead of Surround and Vintage (p.68, p.82).
- Divisi patches have only Close mics; mix them with the non-divisi section's other mics if wanted (p.89-90).
- Factory mic mixes differ widely by patch (patch; KIT §12): woodwind KS Masters Close 1.0 with Main 0.01-0.28 (Flute Main 0.28, Clarinet 0.06), Solo Horn Close 1.35 / Main 0.44, Solo Trombone Close 0.49 / Main 1.0, Solo Tuba 1.0 / 1.0, Solo Trumpet Close 0.25 / Main 0.47 / Surround 1.0, string KS Masters Close 0.66 / Main 1.0, Timpani Flt KS Close 0.43 / Main 0.24 / Surround 0.46, 32in Tam Tam Close 1.0 / Main 0.44, 18 Violins Close 0.13 / Main 0.25 / Stage 1.0.

### 4.2 Moods (Player window)

| Mood | Settings | Pages |
|---|---|---|
| Classic (default) | Main mic mix (Decca tree and outriggers); large Southern California hall, 3.4 s | p.136; 2025 p.82 |
| Soft | Mid and Surround (or Vintage) mics through Abravanel Hall; 2025 adds: enables the Con Sordino script and a MIDI Compressor that favours lower velocities | p.136; 2025 p.82 |
| Epic | Close, Main and Surround (or Vintage); cathedral, 2.8 s; 2025 adds a MIDI Compressor favouring higher velocities | p.136; 2025 p.82 |

The pipeline loads the `.oib` files directly and sets mics and reverb itself, so no mood is applied. The SSL channel strips that ship on the main channels are inactive (patch).

### 4.3 Other Player-window controls

- Master channel: pan (keeps the mics' relative pans), gain, output pair, mute/solo (p.140). In this pipeline the main channel is centred because the DIV A patches ship it panned (KIT §12).
- Tune: transpose in semitones, fine in cents (p.140); 2025 adds microtuning scales and A = 432 Hz style global tuning (2025 p.88).
- Channel routing: stereo, mono, mono from left/right, swap (p.141). Stereo Double widens the image; works only in stereo routing (p.141).
- Reverb: convolution IR, pre-delay, volume; "Master" applies one reverb to all instruments in an instance (p.141-142). The Mix-page Reverb insert adds true-stereo IRs, IR envelope shaping, band-pass, width, wet/dry (p.220-221).
- Envelope: curve, attack, hold, decay, sustain (dB), release (p.142). 2025 adds a Release Trails on/off button (2025 p.87). The harp patches ship decay 5990 ms to sustain 0.001, which cut every note to -60 dB within 6 s (M1 c35, patch).
- Sensitivity: velocity curve from -100 (less responsive) to +100 (p.150; 2025 p.89).
- MIDI tools per instance: arpeggiator, chord tools, glide (5 ms-2.5 s), humanizer (note on/off delay 0-100 ms, velocity up to 50%, tuning 0-100 cents, volume, pan), MIDI compressor (threshold, ratio, makeup; on velocity or one CC), MIDI echo, pocket recorder, restrict to scale, transpose (p.152-157; Opus p.72-78).

### 4.4 Mix page

- Every instrument has a master channel, sub-mixer channels (one per mic, with a load button) and FX bus channels (p.196).
- An FX-bus send can be pre- or post-fader; the manual suggests post-fader for reverb so the reverb follows the fader (p.198). The pipeline uses pre-fader sends scaled by the mic volume (KIT §12).
- Insert effects: EQ (Bass Comp, Channel EQ, 6-band Equalizer, Tone Enhancer), dynamics (De-Esser, Level Amp, Limiter, Limiting Amp, SSL Bus Compressor, SSL Channel Strip, SSL Transient Shaper, Tape Saturation), distortion, modulation, harmonics, delay, reverb (Algoverb, convolution Reverb) (p.199-221). The Transient Shaper adds attack; it does not soften one (p.208).

### 4.5 Mixing approaches the manual describes (p.222-223)

- One mic for the whole piece is possible; Main is the usual choice, Close or Mid sometimes (p.222).
- Render each mic position on its own pass and mix the passes afterwards: "it requires a smaller computer system than trying to load multiple sets of samples into RAM at once" (p.222). The same principle allows rendering an extra track in its own REAPER session.
- Or load several mics at once and balance them inside Opus, or send each mic to its own output (p.222-223).

## 5. Strings (Hollywood Strings)

### 5.1 Sections and patch types

- Sections: 18 Violins (new, a different section with different players and vibrato, "the legato is the best we have ever recorded", an alternative to 1st Violins), 1st Violins, 2nd Violins, Violas, Celli, Basses, Full Strings, Ensemble (3 flutes, 3 clarinets, 3 bassoons, 2 trumpets, 2 trombones, 18 violins, 7 basses together) (p.10-11, p.89).
- Categories: Long, Short (with a MOD COMBOS subfolder), Effects (runs, tremolos, trills, repetitions, sul ponticello), Legato, Mutes, Keyswitch (p.91; 2025 p.45).
- Divisi: DIV A and DIV B patches for 1st/2nd Violins, Violas, Celli, Basses and Full Strings, each the left or right chair of every stand, recorded at the same time as the other mics. Close mics only. "The loudness of a divisi part is not much less than if the whole section were playing the part" (p.89-90).
- Full Strings performances load all five sections with fixed key splits (roughly Violins from C4 (EW), Violas G2-B3, Celli C1-F#2, Basses C0-B0, EW names); three "Full STR Sus + Leg" combinations put a legato line over sustained chords (p.90).

### 5.2 Articulations (all sections unless noted)

| Articulation | What it is / how it responds | Pages |
|---|---|---|
| Sustain (Sus MAX, Sus LITE) | Looped, plays as long as held. Bow direction alternates by round robin (up/down). Finger position selectable. Vibrato in three levels: non-vibrato, vibrato, molto vibrato (2025: "2 intensities" on CC1 in the 18 Violins legato example). CC11 = dynamics, CC1 = vibrato. | p.91, p.64; 2025 p.51 |
| Détaché | Separated, longer than staccato, with a defined end; not loopable; may be cut short. All sections. | p.91 |
| Marcato Sustain (Sus Marc LITE; "Marc Sus LITE" in Basses) | A marcato sample plus the sustain samples: "extra power at the start of the note". One per section. | p.91-92 |
| Flautando | 2nd Violins only: bow over the fingerboard, breathy, no vibrato, no finger position, no RR. In other sections, Sustain at pp with CC1 at 0 is similar. | p.92 |
| Harmonics | 2nd Violins only; all two octaves above the fundamental, lowest sounding G4 (EW) = MIDI 79. | p.92 |
| Pizzicato | All sections; RR x2 or x4. | p.92 |
| Bartók pizzicato | All but 2nd Violins; RR x2. | p.93 |
| Ricochet (jeté) | 3-4 bounces per note; RR x2. | p.93 |
| Col legno | RR x4 or x2. | p.93 |
| Marcato (short) | Short, strong accent; RR x4. 2nd Violins and Basses also have Marcato Long. | p.93 |
| Spiccato | Very short bounced bow; RR x9. Spiccato Marcato MOD crossfades to marcato on CC1 (RR x8). | p.93 |
| Staccato, Staccato On Bow, Staccatissimo, Staccato Marcato MOD | Staccato On Bow: the bow stops on the string. Staccato Marcato MOD: CC1 raises the accent per note. RR x9-16. | p.94 |
| Shorts MOD SPEED | CC1 moves through staccatissimo, staccato, staccato on bow, marcato short; RR x8. | p.94 |
| Repetitions | About a dozen repeats in one sample, with bow changes; has release trails; not RR; end the note early for fewer repeats. 2021 says Violas and Basses only (p.98); 2025 and the installed KS Masters have "Repetitions TS" in every section. Tempo-synced; CC11 crossfades 3 dynamics; no velocity. | p.94, p.98; 2025 p.53-57 |
| Runs (pre-recorded) | 1st Violins, Violas, Celli; one octave; Up/Dn; Maj/Min/WT/8va (chromatic); KS (C0 down, C#0 up), MOD (CC1 low half down) or SPLIT key layouts. | p.95-96 |
| Repetitions Runs Script | Playable runs with slurs by direction; repetition samples on held notes; no velocity, CC11 only; CC14 overrides. | p.96 |
| Slur Runs | 1st and 2nd Violins; fast runs (16ths at 125 bpm or faster), with held notes in 3 vibrato levels (CC1) and 5 dynamics (CC11); no velocity. | p.96-97 |
| Spiccato Runs | 2nd Violins (2021); steps up to a whole tone only; "Smooth" version adds staccato. 2025 lists Spiccato Runs for 1st and 2nd Violins and 18 Violins. | p.97; 2025 p.53-55 |
| Tremolo (unmeasured) | No velocity; CC11 changes dynamics and timbre during the note. All sections. | p.97-98 |
| Measured Tremolo TS | Pulses with the host tempo; no velocity; CC11. All sections. | p.97-98 |
| Trills | Half tone (C0 keyswitch) or whole tone (C#0) in one patch; Basses half tone only. | p.98 |
| Sul ponticello | Violas only (2021); no velocity, CC11. 2025 adds 18 Violins "Sul Pont Tremolo" and Ensemble "Sul Pont". | p.98; 2025 p.53, p.57-58 |
| Sul tasto | Not in the 2021 manual. 2025: 18 Violins "Sul Tasto Flautando", Ensemble "Sul Tasto". No sul tasto tremolo in any section. | 2025 p.53, p.57 |
| Con sordino | No muted string samples; the Con Sordino script (CC15) imitates the mute (fewer high overtones). | p.144; 2025 p.91 |

### 5.3 Legato types

| Type | Behaviour | Pages |
|---|---|---|
| Slur | The pitch moves toward the next note as the first ends; skips most intervening pitches. All five sections (Basses have only this one). | p.98-99 |
| Portamento | The pitch slides all the way, passing quickly over the intervening pitches. Not Basses. | p.98-99 |
| Bow change | A bow-direction change with its own sound, independent of slur or portamento. Not Basses. | p.99 |
| Combination patches (Bow Change + Slur + Portamento) | Opus picks the component from the MIDI data; the manual points to a "Combinations section" that is not in this edition. In the patch's LegatoSpeed script a parameter `BOWCHANGE_THRESHOLD` is 75 (patch); what it switches was not checked. | p.99 |
| Legato Slur Staccato ("StacSl Leg BC + Slur + Port MAX") | Adds a slur-staccato accent to notes with no legato connection: the first note of each phrase gets a firmer attack. | p.99 |
| Rules | Transition only with no gap between notes; monophonic by default (CC22); velocity sets transition speed (LegatoSpeed script: velocity 30-127 maps to a sample start offset of 0-4800 samples, about 0-100 ms, in the string KS Masters, patch; KIT §5). The 2025 example: 18 Violins Legato Slur MAX joins up to an octave in either direction, CC11 = 5 dynamics, CC1 = 2 vibrato intensities. | p.99, p.144; 2025 p.51 |

### 5.4 Finger position (CC70)

String KS Masters for 1st/2nd Violins, Violas and Celli (not Basses) select the string a note is played on for Détaché and Sustain; it is a preference where the note exists on that string. FP4 moves notes to lower strings (warmer, "more emotional"); open strings marked "O" sound clearly different. String breaks (EW names): Violins open strings G2/D3/A3/E4, notes below C3 only on string 1, above A#4 only on string 4; Violas and Celli breaks at C/G/D/A, celli an octave below violas (p.145-149; tables p.147-149, also as staves). Default in the KS Masters: FP1 (patch).

### 5.5 Per-section summary (installed KS Masters, patch; default-loaded rows first)

| Section | KS Master rows loaded by default | Other rows (off) | Sampled roots of the sustain/legato rows |
|---|---|---|---|
| Violins I | Sus MAX, Sus Marc LITE, Leg Slur MAX, Staccatissimo RRx9, Stac On Bow RRx9, Marc Shrt RRx4 | Detache, Bartok Pizz RR, Col Legno RRx4, Pizzicato RRx4, Ricochet RR, Spiccato RRx9, Stac RRx14, Stac Slur, Meas Trem TS, Repetitions TS, Tremolo, Trill HT WT MOD, Slur Runs, Spic Runs, four run MOD rows, Leg BC MAX, Leg Port MAX, StacSl Leg BC + Slur + Port MAX | MIDI 55-101 (G3-F7) |
| Violins II | Sus MAX, Sus Marc LITE, Leg Slur MAX, Stac On Bow RRx9, Marc Shrt RRx4, Marc Lng RRx4 | Detache, Flautando, Harmonics, Col Legno RR, Pizz RRx4, Ricochet RR, Spiccato RRx9, Stac RRx9, Stac Slur RRx6, Meas Trem TS, Repetitions TS, Tremolo, Trill HT WT MOD, Slur Runs, Spic Runs, Leg BC MAX, Leg Port MAX, StacSl combination | G3-F7; harmonics G5-C8 |
| Violas | Sus MAX, Sus Marc LITE, Leg Slur MAX, Staccatissimo RRx16, Stac On Bow RRx9, Marc Shrt RRx4 | Detache, Sul Pont, Bartok Pizz RR, Col Legno RR, Pizz RRx4, Ricochet RR, Spiccato RRx9, Stac RRx9, Meas Trem TS, Repetitions TS, Tremolo, Trill HT WT MOD, Leg BC MAX, Leg Port MAX, Stac combination | C3-A6 |
| Celli | Sus MAX, Sus Marc LITE, Leg Slur MAX, Staccatissimo RRx16, Stac On Bow RRx9, Marc Shrt RRx4 | Detache, Bartok Pizz RR, Col Legno RRx4, Pizzicato RRx4, Ricochet RR, Spiccato RRx9, Stac RRx9, Meas Trem TS, Repetitions TS, Tremolo, Trill HT WT MOD, three run MOD rows, Leg BC MAX, Leg Port MAX, Stac combination | C2-G5 |
| Basses | Sus MAX, Marc Sus LITE, Leg Slur MAX, Staccatissimo RRx9, Stac On Bow RRx9, Marc Shrt RRx4 | Marc Lng RRx4, Detache, Bartok Pizz RR, Col Legno RRx4, Pizz RRx4, Ricochet RR, Spiccato RRx9, Staccato RRx9, Meas Trem TS, Repetitions TS, Tremolo, Trill HT | C1-B3 (sounding; the part sounds an octave below written) |
| 18 Violins (not used) | Sus NV VB, Sus Accent, Leg Slur + Port, Spicatto RRx8, Staccatissimo RRx8, Staccato RRx8, Marc Shrt RRx4, Marc Vib Lng RR, Sul Pont Trem, Sul Tasto Flaut | Marc Sus NV VB, Reps RRx8, Spicatto Runs Script, Stac Runs, Stac Slur, Penderecki, Repetitions, Tremolo. No bow-change legato. Mics Close/Main/Stage. | (not measured) |

The five section KS Masters map CC1, CC5, CC7, CC10, CC11, CC15, CC22, CC36 ("Repetition: Reset RR"), CC64 ("Repetition: Sustain"), CC65, CC68 and CC69; all but the Basses also map CC70 (finger position) (patch). No patch used in the mockup maps CC16, the round-robin reset controller set in this machine's Opus preferences (patch, section 3). Envelope release 931 ms on 1st Violins (patch), so a note-off lets the sample fade over about 0.9 s.

Score range check (v621 parts against the sampled roots, patch): every string note lies inside the recorded range.

## 6. Solo cello (Hollywood Solo Cello, licensed, not installed)

| Item | What the manual says | Pages |
|---|---|---|
| Mics | Same number of positions as the orchestra, but vintage alternatives for Close and Mid instead of Surround and Vintage | p.82 |
| Controllers | Dynamics and vibrato depth are linked on CC1 (the orchestral strings separate them). Most patches: CC11 and CC1 control loudness; CC1 also the dynamic layer (2 or 3 levels). Détaché, marcato, sforzando: velocity controls loudness. | p.82-86 |
| Long Solo folder | Patches with a legato performance script (not true legato): overlapping notes blend without strong attacks, monophonic; non-overlapping notes have their normal attacks. Flautando, Grand Détaché RR (x2), Lyrical Vibrato, Sustain Expressive (molto vibrato), Sustain Light Vibrato, Sustain Non Vibrato, Sustain NV NV VB, Sustain NV VB VB (vibrato type changes with the dynamic layer), Tremolo. | p.82-84 |
| Long folder | The same articulations without legato; every note has its attack. | p.84-85 |
| Short folder | Marcato Long Vibrato RR (x2), Marcato Short RRx4 (velocity 3 levels), Pizzicato RRx4 (velocity 3 levels), Sforzando (strong accent tapering to an expressive vibrato for a couple of beats), Spiccato (RRx4, velocity 3 levels). | p.85-86 |
| Legato (true legato, monophonic, transitions recorded at several dynamics) | Legato Bow Change (crossfades into a sustain: light vibrato soft, lyrical vibrato loud; CC1 2 levels), Bow Change Fast (into détaché RRx2), Bow Change Smooth (soft non-slurred attack), Legato Runs (runs layer up to a minor third, bow change from 4 to 12 semitones, then détaché), Legato Slur (crossfades into sustain vibrato; CC1 2 levels). All join up to an octave; velocity sets transition timing. | p.86-87 |
| LegSus Slur ("Legato Sus Slur") | Legato and sustain in one sample layer, so less crossfading. Unconnected notes play a sustain expressive vibrato layer. CC1 picks the dynamic layer (2 levels) from its value at the note start and does not crossfade; CC11 and CC1 still change loudness during the note. | p.82, p.87-88 |
| Keyswitch | KS Master switches articulations. | p.88 |

2025 p.45 confirms the Solo Cello categories (Long, Short, Effects, Legato, Keyswitch), and 2025 p.19 lists its articulations (sustain vibrato and non-vibrato, flautando, grand détaché, tremolo, marcato, pizzicato, sforzando, spiccato, legato, keyswitch). The 2025 manual has no per-patch descriptions for it, so the 2021 pages are the only reference for controllers and legato behaviour.

## 7. Woodwinds (Hollywood Orchestral Woodwinds)

### 7.1 Instruments

Flutes: Piccolo, Flute, Flute 2 (a different player in a slightly different seat; no shared samples, so Flute and Flute 2 in unison do not collapse into one sound), 3 Flutes (new), Alto Flute, Bass Flute. Clarinets: Clarinet, 3 Clarinets (new), Eb Clarinet, Bass Clarinet, Contrabass Clarinet. Double reeds: Oboe, English Horn, Bassoon, 3 Bassoons (new), Contrabassoon (p.108-109). There is only one oboe, clarinet and bassoon player, so Oboe 1/2, Clarinet 1/2 and Bassoon 1/2 share samples (inferred from p.108).

### 7.2 Patch types

| Type | Behaviour | Pages |
|---|---|---|
| Sustain | Looped. 2021 p.109 says the Mod Wheel controls dynamics (3 layers playing at once). This is the Play-era text: p.64, p.151 and 2025 p.52 say CC11 = dynamics, CC1 = vibrato for Opus woodwinds. Patch files: Flute, Oboe, English Horn, Bassoon and Contrabassoon KS Masters crossfade a Sus Non Vib and a Sus Vib layer on CC1 (Vib fades in over CC1 55-64; KIT §3); the Clarinet KS Master crossfades its dynamic layers on CC1 (M1 c09). | p.109; p.64; 2025 p.52 |
| Sus Expressive (Sus Exp, Sus Exp Vib) | Slower attack and gently increasing vibrato. In every solo woodwind but the Eb and contrabass clarinets (2025 lists). | p.109; 2025 p.69-76 |
| Legato Repetitions (LegRep RRx4) | For repeated notes inside a legato phrase: each note plays a non-vibrato sustain plus a short re-tongued attack; the attack has 4 round robins. | p.109-110 |
| Staccato, Staccatissimo (StacSs), Double Tongue (DblTng) | Shorts with no release trails; hold notes so the room rings. | p.110 |
| Marcato | Short with a strong accent; RR x4. | p.110 |
| Shorts MOD SPEED | CC1 quarters: staccatissimo, staccato, marcato short, marcato short + sustain. | p.110 |
| Effects | Runs (chromatic, major, minor, whole tone; one octave up or down, fixed speed; the MIDI note is the lowest note), trills HT/WT (CC1 loudness, 3 layers, no velocity), flutter tongue (CC1 loudness), repetitions (slow/medium/fast), FX, Sing RR (flute). | p.111-112 |
| Legato Slur | Joins without a gap and within an octave; 3 sustain samples plus slur samples per note. | p.112 |
| Legato Slur Repetitions (Leg Slur Rep) | Same-pitch notes played consecutively without space use a re-tongued sample instead of a slur. | p.112 |
| Legato Slur Accent, Legato Slur Exp, Legato Slur Runs, Legato Staccato Runs | Rows present in the KS Masters (patch); Slur Runs: strong slur only for steps of a minor or major second; up to 40+ voices per patch in fast runs. | p.112-113 |

### 7.3 Installed KS Masters (patch)

| Instrument (tracks) | Rows loaded by default | Rows off | Sampled roots (sustain/legato) | v621 range |
|---|---|---|---|---|
| Flute (Flute 1) | Sus MAX, Sus Accent MAX, Leg Slur MAX, StacSs DblTng RRx9, Stac DblTng RRx9, Marc DblTng RRx4 | Sus Exp, LegRep RRx4, Trill HT/WT, Leg Slur Accent MAX, Leg Slur Exp, Leg Slur Rep, Leg Slur Runs, Leg Stac Runs, Flutter Tng, Sing RR, runs, Rep Fst/Med/Slw, FX | C4-C7 | Fl1 A#4-G#6, Fl2 B4-G#6 |
| Flute 2 (Flute 2) | as Flute (Marc Shrt DblTng RRx4) | Sus Exp Vib, LegRep RRx4, trills, Flutter Tng, Leg Slur Accent MAX, Leg Slur Exp, Leg Slur Rep, runs, repetitions | C4-C7 | |
| Oboe (Oboe 1, 2) | as Flute | Sus Exp Vib, LegRep RRx4, trills, Leg Slur Accent MAX, Leg Slur Exp, Leg Slur Rep, runs, Rep Med/Slw | A#3-G6 | Ob1 F4-D6, Ob2 B3-B5 |
| English Horn (Cor anglais) | Sus Max, Sus Accent MAX, Leg Slur MAX, StacSs, Stac, Marc DblTng | Sus Exp Vib, LegRep RRx4, trills, Leg Slur Accent MAX, Leg Slur Exp, Leg Slur Runs, Leg Stac Runs | E3-G5 | B3-F5 |
| Clarinet (Clarinet 1, 2) | Sus Non Vib, Sus Accent, Leg Slur, StacSs, Stac, Marc DblTng | Sus Exp, LegRep RRx4, trills, Leg Slur Accent, Leg Slur Rep, Leg Slur Runs, Leg Stac Runs, runs, Rep Slw, FX | D3-G6 | Cl1 G3-C6, Cl2 A#3-C5 |
| Bass Clarinet | Sus Non Vib, Sus Accent, Leg Slur, StacSs RRx5, Stac RRx5, Marc Shrt DblTng | Sus Exp, LegRep RRx4, trills, FX Lng, Leg Slur Accent, Leg Slur Runs, Leg Stac Runs | A#1-F5 (legato to D#5) | A#1-G3 |
| Bassoon (Bassoon 1, 2) | Sus MAX, Sus Accent MAX, Leg Slur MAX, StacSs, Stac, Marc DblTng | Sus Exp Vib, LegRep RRx4, trills, Leg Slur Accent MAX, Leg Slur Exp, Leg Stac Runs, Rep Med/Slw, runs | A#1-A#4 | Bn1 F2-F4, Bn2 A#1-G3 |
| Contrabassoon | Sus MAX, Sus Accent MAX, Leg Slur MAX, StacSs RRx5, Stac RRx5, Marc DblTng | Sus Exp Vib, LegRep RRx4, Leg Slur Accent MAX, Leg Slur Exp, Leg Slur Rep, Leg Slur Runs, Leg Stac Runs | A#0-D3 (sounding) | C1-F2 |

Woodwind KS Master envelopes: release 177 ms (patch). Release-trail ("RT") groups exist with releases of about 1.8 s on the flute (patch). The CC1 vibrato layer change makes CC1 values between 55 and 76 a blend of the two layers, not a vibrato depth (KIT §3).

## 8. Brass (Hollywood Brass)

### 8.1 Instruments

Solo Cimbasso, Solo French Horn, Solo Trombone, Solo Trumpet, Solo Tuba, 2 French Horns, 2 Trombones (new; "warm, full, extremely precise"), 2 Trombones and 1 Bass Trombone, 2 Trumpets, 2 Trumpets Exp (new; "legato is blazing at high velocities"), 3 Trumpets, 6 French Horns, Low Brass (p.10-11, p.100; 2025 p.45-46). There is no solo bass trombone; the bass trombone exists only inside "2 Trombones and 1 Bass Trombone" (3TB KS Master) and Low Brass.

### 8.2 Patch types

| Type | Behaviour | Pages |
|---|---|---|
| Sustain | CC1 = dynamics; all 4 dynamic layers play at once and CC1 decides which one or two are heard; crescendo and decrescendo during a note. Sustain Lite uses fewer voices. | p.101 |
| Sustain Accent | An accent at the start; velocity = loudness of the attack, CC1 = loudness of the sustained note. | p.101 |
| Sustain Marcato Long / Short (KS row "Marc Sus LITE") | A marcato attack, "not as forceful an attack as in the Sustain Accent patch"; Long/Short = length of the marcato part. Velocity sets the cutoff of a low-pass filter on the marcato samples: harder = brighter, harsher attack. | p.101 |
| Portato (Port Lng / Port Shrt on the horn) | Each note held its full length, or nearly, without being tied: non-legato, not staccato. | p.101 |
| Legato Repetitions (LegRep RRx4) | Re-tongued repetitions for repeated notes inside a legato phrase; the same samples the Legato Slur Repetitions script uses. | p.101 |
| Mariachi Sustain | Strong attack, wide vibrato; velocity = dynamics. Solo Trumpet. | p.101-102 |
| Expressive Vibrato | Solo Trumpet only: starts without vibrato and adds it as the note continues. | p.102 |
| Staccato, Staccatissimo | The highest velocities add an overblown attack with more high harmonics. No release trails. | p.102 |
| Marcato (Short, Long) | Short notes with a strong accent; RR x4. | p.102 |
| Shorts MOD SPEED | CC1: staccatissimo 0-25, staccato 26-51, marcato short 52-77, marcato long 78-103, marcato long + sustain 104-127. | p.102 |
| Repetitions Fast 170 / Medium 145 / Slow 120 | A dozen or more repeats per note, tempo-synced to the host; CC1 = loudness; has release trails; pick the version nearest the tempo. | p.103 |
| Triple Performance | 3 Trumpets: three repeats per note; no CC1 loudness. | p.103 |
| Double tongue | Faster repeated tonguing ("tiki tiki"). | p.103 |
| Sforzando Crescendo | Solo Horn and Solo Tuba (2025 adds Solo Trombone and 2 Trumpets): sforzando attack then a strong crescendo; velocity sets attack loudness and timbre and the crescendo; a short note works as a sforzando staccato. | p.103; 2025 p.59-64 |
| Effects | Trills HT/WT (KS: C0 half, C#0 whole; CC1 loudness, no velocity); rips, shakes, rip shakes, rip flutter (velocity for the rip, CC1 for the flutter); crescendo patches Fast/Medium/Slow ("often more realistic than using MIDI volume or expression"), Crescendo MOD SPEED (CC1 1-42 slow, 43-85 medium, 86-127 fast; no release trails); flutter tongue (CC1 loudness); clusters (CC1); FX. | p.104-105 |
| Legato Slur | Slur only with no gap and within an octave. CC1 = dynamics; in the loudest range CC1 opens a low-pass filter for an overblown sound as it nears 127. Velocity = transition speed. 4 sustain samples plus slur samples per note. | p.105-106 |
| Slide legato | Trombones: a portamento-like slide between notes ("Leg Slide MAX" row in 3TB; "Legato Slide" in Solo Trombone). | p.105; 2025 p.60, p.64 |
| Legato Slur Accent | Legato slur with an accented attack; velocity = accent strength, CC1 = loudness. | p.106 |
| Legato Slur Repetitions | Repeated same-pitch notes inside a legato phrase use re-tongued samples. | p.106 |
| Slur Runs | Strong portamento slur only on steps of a second; 4 voices per note. | p.106 |
| Mutes | Muted versions of many articulations; horns also have "stopped" (hand in the bell). | p.106-107; 2025 p.47 |

### 8.3 Installed KS Masters (patch)

| Instrument (tracks) | Rows loaded by default | Selected rows off | Sampled roots (sustain/legato) | v621 range |
|---|---|---|---|---|
| Solo French Horn 1FH (Horns 1-4) | Sus MAX, Sus Accent MAX, Leg Slur MAX, StacSs RRx9, Marc Shrt RRx4, Marc Lng RRx4 | Sus Pitch Waver, Port Lng, Port Shrt, Marc Sus LITE, LegRep RRx4, Stop Sus, Stop Sus Accent, Stop Stac RRx4, Leg Slur Accent MAX, Leg Slur Rep MAX, Slur Runs MAX, Trill HT, Rep Fst/Med/Slw, Sfz Cres, Cres Fst/Med/Slw, rips and shakes | C2-E5 | Hn1 D#3-E5, Hn2 F#3-A#4, Hn3 D#3-C5, Hn4 F2-B3 |
| 2 French Horns 2FH (Horns a2) | Sus MAX, Sus Accent MAX, Leg Slur MAX, StacSs DblTng RRx9, Marc Shrt DblTng RRx4, Marc Lng RRx4 | Portato, Marc Sus LITE, LegRep RRx4, Stop rows, Trill HT/WT, Leg Slur Accent MAX, Leg Slur Rep MAX, Slur Runs MAX, Cres Fst/Med/Slw, rips, repetitions | C2-E5 | D#3-G#4 |
| Solo Trumpet 1TP (Trumpets 1-3) | Sus Non Vib MAX, Sus Accent MAX, Leg Slur MAX, StacSs DblTng RRx9, Stac DblTng RRx9, Marc Shrt DblTng RRx4 | Marc Lng DblTng, Sus Vib MAX, Sus Exp, Marc Sus LITE, Mariachi Sus, LegRep RRx4, mute rows, Leg Slur Accent MAX, Vib Leg Slur MAX, Leg Slur Rep MAX, Slur Runs MAX, trills, repetitions, Cres Fst/Med/Slw | E3-D6 (legato to C6) | Tpt1 F4-G#5, Tpt2 D4-A#4, Tpt3 B3-G4 |
| Solo Trombone 1TB (Trombones 1-2, Bass trombone) | Sus MAX, Sus Accent MAX, Leg Slur MAX, StacSs DblTng RRx9, Marc Shrt RRx4, Marc Lng RRx4 | Portato, Marc Sus LITE, LegRep RRx4, Leg Slur Accent MAX, repetitions, Sfz Cres, pedal rows, Cres Fst/Med/Slw, Flutter Tongue, Sus Vib, jazz, mute and plunger rows | E2-C5 (sustain keys mapped down to C2) | Tbn1 G2-F4, Tbn2 D#3-C4, Bass trombone C2-F#3 |
| Solo Tuba 1TU (Tuba) | Sus MAX, Sus Accent MAX, Leg Slur MAX, StacSs DblTng RRx9, Marc Shrt RRx4, Marc Lng RRx4 | Portato, Marc Sus LITE, LegRep RRx4, mute rows, Leg Slur Accent MAX, Leg Slur Rep MAX, Slur Runs, Flutter Tongue, repetitions, Sfz Cres, Cres Fst/Med/Slw | D1-B3 | F1-F2 |
| 2 Trombones and 1 Bass Trombone 3TB (not used) | Sus MAX, Sus Accent MAX, Leg Slur MAX, StacSs DblTng RRx9, Marc Shrt DblTng RRx4, Marc Lng RRx4 | Portato, Marc Sus LITE, LegRep RRx4, mutes, Leg Slur Accent MAX, Leg Slur Rep MAX, Leg Slide MAX, flutter, Cres Fst/Med/Slw, clusters, repetitions | (not measured) | |

Brass KS envelopes: release 562 ms (horn), 237 ms (trombone), 700 ms (trumpet), 372 ms (tuba) (patch). Legato speed: the horn's LegatoSpeed script maps velocity 0-127 to a start offset of 0-2281 samples (about 50 ms), a narrower range than the strings' 0-4800 (patch). CC1 above about 108 adds brightness quickly (trumpet 4-8 kHz +6.7 dB from f to ff; KIT §20 / M1 c09).

The bass trombone's three lowest notes (MIDI 36-38, C2-D2, at qn 451.78, 455.89 and 459.89, bars 113-115) lie under the Solo Trombone's lowest recorded root (E2, MIDI 40), so they play E2 samples transposed down 2-4 semitones (patch).

## 9. Percussion used in v621

### 9.1 Timpani (Timpani Flt KS: felt mallets; Hrd versions for hard mallets)

| Row / patch | Behaviour | Pages |
|---|---|---|
| Felt Long (KS C0 = MIDI 24) | Long hits on a 22-note chromatic range, with left-hand variations at C1-A2 (EW) = MIDI 36-57 and right-hand variations at C3-A4 (EW) = MIDI 60-81. Two notes more than 65 ms apart play long hits; within 65 ms the second plays a double hit that damps the first. Velocity: up to 16 dynamic layers. RR x2. CC11 and velocity = loudness. | p.123-124 |
| Felt Short (C#0 = 25) | Quickly muted hits, LH/RH ranges as above; for stops within a beat or two; up to 16 layers; RR x2. | p.124 |
| Felt Flam (D0 = 26) | Soft double hits ("thicker, more complex", like several players); 2 layers; RR x2. | p.123, p.125 |
| Felt Rolls (D#0 = 27) | CC1 = dynamics in 8 layers, for crescendos and decrescendos of any length; CC11 and velocity = loudness. | p.124-125 |
| Felt Cresc (E0 = 28) | Recorded crescendo rolls ending in a strong final stroke, three lengths on three key ranges (MIDI 36-57, 60-81, 84-105); 2 velocity layers. "The most realism" for a roll crescendo. | p.123, p.125 |
| Felt Sus Pedal | CC64 off = short hits, on = long and double hits. | p.124 |
| Hard mallet versions | Same set, brighter, with "clear individual hits" in rolls. | p.125-127 |

Patch check: the Timpani Flt KS has regions "LH Lng/Sht/Dbl" at MIDI 36-57 and "RH Lng/Sht/Dbl" at MIDI 60-81, "Rls" at 36-57 and "Crs p/f" at 36-105 (patch). Its controller map has no CC1 or CC11 entry, but CC1 does crossfade the Rls row's eight layers (V1 at CC1 0-9 ... V8 at 118-127, fade 120 ms; M1 c12, measured). Default mics Close 0.43 / Main 0.24 / Surround 0.46 (patch). v621 timpani notes lie at MIDI 43-51.

### 9.2 Tam-tam

32in Med Tam Tam: C1 (EW) = MIDI 36 long, MIDI 38 short, MIDI 40 fast crescendo, 41 medium-fast crescendo, 43 slow crescendo; RR x2; velocity = 12 dynamic layers for long and short, 2 for the crescendos. "A bassy resonance coupled with its high frequency splash". 38in Large Tam Tam adds bowed FX (MIDI 45-64) and scraped FX (65-71), with "a strong bassy resonance and firm body". 28in Small Tam Tam: mellower (p.118). The 32in's strongest partial is about 86 Hz and decays slowly (KIT §20).

### 9.3 Suspended cymbal

18in Zildjian Sus Cymbal Cresc: four lengths of "crescendo sustain" (the roll grows to a peak and rings) at MIDI 60, 62, 64, 65 (shortest to longest) and four of "crescendo stopped" (grows, then damped) at MIDI 67, 69, 71, 72; RR x2; velocity = 2 layers; CC11 and velocity = loudness. "Profile close to a standard suspended cymbal" (p.119; patch roots C4-F4 "LtRg" and G4-C5 "Chk"). Other sizes: 14in Paiste (rain-like), 18in Wuhan (deeper), 20in Zildjian with cutouts (splashy), 22in Dream (gong-like), Large Sizzle (rivets, long sizzle) (p.118-120). Recorded let-ring takes are 6.8-15.0 s long (M1 c35 critic C, .ews headers).

### 9.4 Crash cymbals (track silent in v621)

Pairs from 12 to 22 inches, three lengths each (long/short/shorter) on white keys from C3 (EW), RR x3, up to 7 velocity layers (p.116-118).

## 10. Harp (Hollywood Harp)

| Patch | Behaviour | Pages |
|---|---|---|
| Sustain RR (used) | Alternates Pluck Long and Thumb Pick by round robin at velocity 1-123 (5 layers each); velocity 124-127 plays a Nail Pick in either cycle. CC11 and velocity = loudness. Measured layer splits: Pluck p 1-57 / mp 58-85 / mf 86-107, Thumb p 1-42 / mp 43-70 / mf 71-97 (M1 c33). | p.69 |
| Sustain RR Bisbigliando | As Sustain RR plus a bisbigliando layer on CC1 (2 levels). | p.69-70 |
| Angels, Angels Harmonics, Maestro, Maestro Bisbigliando | Velocity selects articulation zones: e.g. Maestro: Double Hit 1-60, Gliss Technique 61-102, Nail Picks 103-127. | p.68-69 |
| Individual articulations | Bisbigliando (light fingered tremolo), Double Hit (grace-note pair, soft then stronger), Gliss Technique (single notes from glissandi, softer than plucks), Harmonics (no fundamental), Nail Pick (hard, overtone-rich), Pluck (5 levels), Près de la table (dry, bright, twangy; 4 levels), Repetition Rep (repeated notes ring fully, no machine-gun effect), Thumb Pick (rounder, more guitar-like; 5 levels). | p.70-71 |
| FX, Gliss, Gliss Angelic Slow/Fast | Recorded glissandi on white keys, with a table of root and scale per key. | p.71-74 |
| Mics | Vintage Close and Vintage Mid instead of Surround and Vintage. | p.68 |

Patch facts: Harp Sus RR covers roots D#1-G7 (MIDI 27-103), ships release 3019 ms and decay 5990 ms to sustain 0.001 (M1 c11, c35); Harp Maestro patches load only the Close mic (KIT §9). There is no damped (étouffé) articulation; damping is a note-off with a short release.

## 11. Where the manuals and the patches disagree

| Topic | 2021 manual | 2025 manuals | Installed patches / measured | Use |
|---|---|---|---|---|
| CC22 polarity (strings) | p.99: 64-127 polyphonic | 2025 p.91: 0-63 polyphonic, 64-127 mono (also 2021 p.105, p.112, p.144) | not tested | 64-127 = monophonic |
| Legato script CC | CC57 (p.143-144) | CC68 (2025 p.90-91) | CC68 mapped (patch) | CC68 |
| Round-robin reset | CC36 (p.143, p.145) | the CC set in Preferences (2025 p.92; Opus p.29-30) | Preferences: CC16; patches map CC36 to "Repetition: Reset RR"; CC36 inside the music did not reset a Stac RRx9 cycle (M1 c14) | CC16 for samples; CC36 for the Repetition script |
| Woodwind sustain dynamics | Mod Wheel (p.109) | CC11 dynamics, CC1 vibrato (2025 p.52; also 2021 p.64, p.151) | Flute/Oboe/EH/Bassoon/Contrabassoon: CC1 = vibrato layer crossfade; Clarinet: CC1 = dynamic layers (KIT §3, M1 c09) | the patch behaviour per instrument |
| Brass sustain dynamics | CC1 (p.101) | CC11 crossfades dynamics where more than one exists (2025 p.52, general text) | Brass KS Masters: CC1 crossfades the dynamic layers (M1 c09) | CC1 |
| String repetitions | Violas and Basses only (p.98) | all sections (2025 p.53-57) | "Repetitions TS" row in every section KS Master | all sections |
| String vibrato levels | 3: non, vib, molto (p.91) | "2 intensities" (2025 p.51, 18 Violins example) | KS Masters have Non Vib, Sus Vib and Molto Vib sample folders (patch) | per patch |
| Combination legato details | "Combinations section below" (p.99), missing | not described | `BOWCHANGE_THRESHOLD` 75 in LegatoSpeed (patch) | unverified |
| Woodwind/brass articulation tables | referred to (p.108), missing | lists per instrument (2025 p.59-76) | KS rows (sections 7.3, 8.3) | 2025 lists and patch rows |
