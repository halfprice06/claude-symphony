# Kit learnings: orchestral mockups with REAPER + EastWest Hollywood Orchestra Opus Edition

Curated 2026-10-11 from the movement II mockup loop (cycles c00-c04 rendered and measured; c05 critic reports read, c05 changes implemented in the tools but not yet rendered or measured). Sources: `symphony/mvt2/reaper/README.md`, `loop/BRIEF.md`, `loop/HISTORY.md`, `cycles/c01-c04/CHANGES.md`, `cycles/c01-c05/reports/*.md`, `tools/*.py`, `build/mix.json`, `build/roles.json`, `build/note_trims.json`, `opus/ (installed at ~/.rpr-bridge/libs/ew_ho/)`.

This file keeps only lessons that apply to another score. Evidence is in parentheses: cycle and measured numbers. "Unverified" means implemented or proposed but not confirmed by a measured render. "Inferred" means reasoned from data or manuals, not measured directly.

Library: Hollywood Orchestra Opus Edition Diamond (KS Master patches for solo winds and brass and string sections, Harp, Timpani), on an external USB/exFAT drive. Pipeline: LilyPond score -> MIDI + event list -> `parts.json` -> Lua jobs through the `~/.rpr-bridge` file bridge -> REAPER, one Opus instance per track.

---

## 1. Loading Opus patches by script

- Patch loading is scriptable. Opus's VST3 state is gzip-compressed JSON (a `Performance` with a `zones` list); write it with `TrackFX_SetNamedConfigParm(tr, 0, "vst_chunk", base64)` (c00).
- An `.oib` patch file is a 20-byte header followed by zlib/gzip JSON holding one `Instrument`; the plugin state is a 28-byte header, the gzip JSON, and a tail (`opus_state.py`: `HDR = 28`, `load_oib` reads from byte 20).
- Put the patch into a zone as `{"class": "InstrumentZone", "keyMin": 0, "keyMax": 127, "velMin": 1, "velMax": 127, "octave": 0, "groupIndex": 0, "instrument": <oib JSON>}` (c00).
- The first 4 bytes of the state (little-endian u32) must equal the total blob length minus 16, or Opus truncates the JSON (c00).
- A zone that holds only a locator path, without the full instrument JSON, crashes Opus (c00).
- Everything a patch does is editable in that JSON before loading: articulation rows, mic columns and volumes, mixer inserts (reverb, sends), script filters (EWSO, RTKiller, ConSordino, FingerPosition), and the starting keyswitch (c01-c05).
- Read keyswitch maps and sample ranges from the `.oib` files, not from screenshots or memory (`opus/dump_ks.py`, `ks_maps.json`). The Harp Maestro range error (finding below) was found by reading every group's keyMin/keyMax from the file (c01).
- Any state change (mics, reverb, rows, pans inside Opus) needs the track rebuilt; a cache that reuses old state files hides the change. The c00 build reused existing `.b64` files, so state edits had no effect until the cache check was removed (c01 critic C).

## 2. KS Master patches: articulation rows and keyswitches

- A KS Master loads only its first rows by default: the string KS Masters load six (Sus MAX, Sus Marc LITE, Leg Slur MAX, Staccatissimo, Stac On Bow, Marc Shrt). Keyswitches to unloaded rows are ignored and the current articulation keeps playing (c02: pizz. notes measured as bowed sustains, time to peak 600-720 ms, decay 1-1.7 dB).
- To load a row, set `layerMatrix.rows[i].loaded = true` and `active = true`, and on the matching `articulations.trigger` entry set `useKey = true` and a `triggerName` (c02). After this, pizz. decayed 10-16 dB within 400 ms of the peak and onsets rose in 0-10 ms (c02, c03).
- Match row names case-insensitively: the cor anglais row is "Sus Max", not "Sus MAX" (c02).
- Opus names keys with C0 = MIDI 24 (`triggerName = NOTE[key % 12] + str(key // 12 - 2)`). String KS Master keyswitches start at 24; examples: 1st Violins Leg BC MAX 48, Slur Runs 42; Celli KS Master keyswitches sit at 80-90; Harp KS Master keyswitches are 21-35 (`ks_maps.json`).
- Setting `articulations.currentKeySwitch` in the state does not reliably select the first articulation. Trombone 1's first two Sus Accent notes (selected only by state) measured -8.8 / -8.6 dB attack brightness against +5.6 dB for the same articulation reached by a keyswitch (c03). Send the first keyswitch as a MIDI note whenever the track's first note is late enough to allow it (c03 fix; `currentTrigger` and `lastArticulationId` fields exist but were not tested).
- Keyswitch notes of velocity 1 and 0.03 qn length work (c00-c04).
- Put keyswitches and CC15 changes in the preceding rest (rest start + min(0.5 qn, 25% of the rest)), not on the note onset. In c00, six of eight 535-650 ms late entries coincided with a CC15 change on the note (c01 critic A; correlation only, cause not isolated).
- With a rest before the note, a keyswitch lead of 55 ms or more was always enough (c03: median lead 69 ms, minimum 55 ms). Unverified: whether a 3 ms lead fails (one case, effect not isolated).
- Do not send a keyswitch while a note on a legato patch is still sounding; end the legato note before the keyswitch. Inferred from one case where a held legato note overlapped a switch to Tremolo and the tremolo came in late (c05 critic A; guard implemented in c05, unverified).

## 3. Controllers in Hollywood Orchestra

- CC11 (Expression) crossfades the dynamic layers and also sets volume (HO manual 2.1.3). Use it as the dynamic control; do not use CC1 for dynamics.
- CC1 (Mod wheel) crossfades the non-vibrato and vibrato sustain layers in the MAX patches (read from `OB Leg Slur MAX.oib`, `OB KS Master.oib`; c04 critic C).
- CC7 is MIDI volume; its curve is not documented and is shallower than 40·log10 at low values (c02: a CC7 change from 16 to 13 measured 0.6-1.5 dB instead of the intended 4 dB). Prefer a REAPER volume envelope for exact dB.
- CC15 drives the Con Sordino script in the string KS Masters and in `1FH KS Master` (c02). It is a filter emulation, not muted samples.
- CC70 is Finger Position in the string KS Masters: 0-38 FP1, 39-76 FP2, 77-114 FP3, 115-127 FP4 (HO manual pp. 92-95). Higher positions move notes to lower strings. Used for sul D/G/C (127) and sul A (20 up to MIDI 74, 127 above). Unverified: no stem difference was measured.
- Other mapped controls in the string KS Masters (`ks_maps.json`): CC5 Legato Time, CC22 True Legato mono/poly (below 64 = polyphonic, HO manual p. 91), CC64 Repetition Sustain, CC65 Portamento, CC68 Legato, CC69 Repetition, CC36 Reset RR. None of these were tested.
- Velocity: on legato targets it sets transition speed, not loudness (HO manual 2.1.1). On short articulations, harp and timpani it sets loudness.
- Velocity on the felt timpani and harp is the dynamic. Harp CC11 should be held constant, or soft notes are attenuated twice (c01: Harp Maestro measured 19 dB from pp to mp against about 7 dB for strings).

## 4. CC11 response and per-track level

- The level per CC11 step differs by patch: fitted 0.17-0.36 dB/CC across tracks (c02: Oboe 0.175, Trombone 0.173, Vln I 0.300, Flute 0.364, Celli 0.358). Later fits: violins 0.23-0.25, violas 0.31-0.325, bassoons 0.30, oboe/clarinets/contrabassoon 0.19-0.22, horns 0.27-0.34 (c03, c05). Balance set at p therefore drifts as the music gets louder.
- Strings barely respond to CC11 below about 40: within single notes about 1.1 dB per 14 CC, and a printed decrescendo from CC 34 to 22 moved the strings only -1.6 to -3.5 dB (c02). Use the volume envelope for fades below pp.
- Some patches jump in mid-range: from the CC 52-64 bin to the 64-80 bin, bass clarinet +10.9 dB, Flute +7.6, Clarinet 2 +7.6, celli +7.3 (c02).
- The top layer runs to CC 127 (FL KS Master layer ranges 0-55, 56-93, 94-127). With ff at CC 104, f to ff measured only +2.5 LU; ff at 114 and fff at 124 restored the growth (c02).
- A dynamic table that worked: ppp 22, pp 34, p 46, mp 58, mf 72, f 88, ff 114, fff 124 (c02-c04).
- A hairpin without a printed target that moves 14 CC measured a median +2.6 dB, and 38 of 95 moved less than 1.5 dB or the wrong way; targeted hairpins of more than 16 CC measured a median 7 dB (c02). Use about 22 CC for untargeted hairpins from mp or softer (c02).
- An +8 CC11 boost is about +2.5-3 dB at the measured slopes (c01 critic B). End such boosts at the next dynamic or rest, and fade them out toward f, or they inflate climaxes (c02: celli 5-10 dB over the tune from a cantabile boost that ran 40 qn).
- Keep CC11 as the layer control and make balance corrections with level only (track volume envelope), so the timbre of each printed dynamic is kept (c02 onward).
- Per-track dynamic trims: a trim that is 0 dB at p (CC 46) and reaches a set value at f (CC 88) and ff (CC 114), read from the printed dynamic curve (not from CC11, so accents do not move it), was enough to correct the slope differences (c02-c04).

## 5. Legato patches (Leg Slur MAX, Leg BC MAX)

- Legato patches are monophonic: a chord on a legato patch drops notes. Keep chords and simultaneous divisi notes on Sus patches (c00-c05: 0 chord onsets on legato patches).
- A legato transition needs overlap; 0.04 qn worked (c00-c05). Apply the overlap only inside one slur, and end the last note of a slur 0.05 qn early when a new slur starts, so the patch re-attacks (c01).
- Never overlap into the same pitch: the old note-off arrives after the new note-on and stops it (c01: dips of -18 to -33 dB; an ff oboe half note fell from -37 to -98 dB).
- A disconnected note on Leg Slur MAX plays the sustain layer (HO manual 2.1.3), so one patch can carry a whole line (c02).
- Leg BC MAX (bow-change legato) is in the 1st/2nd Violins, Violas and Celli KS Masters, not in the Basses KS Master. For connected unslurred string notes and slur-to-slur joins it cut join dips from -8..-12 dB to -4..-5 dB (c02 -> c03). Joins inside a slur measured about -2 dB (c03).
- Turn on legato speed: KS Masters ship with `EWSO.legato_speed_active = false` and `RTKiller.active = false`; the dedicated Leg Slur MAX patches have both true (c02). The LegatoSpeed script maps velocity 30-127 to a sample start offset of 0-4800 samples (about 100 ms).
- Measured legato lag (crossover of new-pitch over old-pitch energy, harmonics 1-4, from the MIDI onset): with velocity from the printed dynamic (41-63), strings 200-250 ms median, horns 125 ms, woodwinds 80-140 ms (c01). With legato speed on and velocity 105-120, strings 222-310 ms, horns 185-385 ms (c02, c03). Velocity 120 against 105 gained 25-80 ms (Vln I 225 vs 265 ms, Vla 210 vs 298 ms; c03 critic C).
- The legato lag is deterministic (interquartile range about ±40 ms; two renders identical note for note, c03 critic C), so compensate by moving legato target notes earlier and keeping CC11/CC1/volume on score time.
- Leads that worked: strings 0.17 s with velocity 124, brass 0.10 s with velocity 124 (< 0.9 s) / 112. Result: string crossover medians 250-275 -> 50-85 ms, horns 190-200 -> 85-108 ms (c03). Woodwinds: oboe/bassoon 0.06 s, bass clarinet 0.05 s, cor anglais 0.08 s, flute/clarinet 0.03 s (c03, c04; the woodwind values after c04 are unverified by a new crossover measurement).
- Cap the lead at 0.45 of the previous note's length and move the previous note's end with it so the overlap survives (c03).
- Woodwind legato targets at velocity 60 cross over 100-150 ms late; the cor anglais measured 150-185 ms at v60-80 (c04 critic A). The crossover point is the middle of the transition; the lag a listener hears is about 40 ms less (c03 critic C).
- Fast slurred notes under 0.25 s smear on legato patches (transitions of 160-320 ms; a viola sextuplet figure ran 230 ms behind, c03 critic C). Sus MAX with 0.03 qn overlap was used instead; a residual 90-120 ms lag remained (c03). The Violins KS Masters have Slur Runs rows (keys 42/43) that were not tried.
- Measure note lengths for articulation choice on the tempo map without caesuras or other expressive time, or a fermata-like slowing turns a short note into a legato target (c05 critic A).

## 6. Soft entries, re-attacks and sample blooms

- Soft sustained string and brass entries reach level slowly: arrival (within 6 dB of the early peak) 300-1010 ms for pp/p strings, 355-495 ms for soft horn/trombone/tuba entries, against 60-150 ms for winds at the same moments (c03 critic C). The times repeated exactly across two renders, so they are sample attack, not streaming.
- Moving soft entries earlier (strings 0.12 s at CC11 <= 50 / 0.06 s above; brass 0.10 / 0.05 s; bassoons 0.06 s) with CC11 held at the entry's own level from the moved onset brought string arrival medians to Vln I 310, Vln II 488, Vla 230, Vc 100 ms (c03). Still late; larger leads not tested.
- A same-pitch re-attack on Leg Slur MAX at pp takes 300+ ms to reach level, leaving 7-15 dB holes in the stem (c03 critic A: median Vln II -10.7, Vla -8.9, Vc -8.7 dB; master -6 to -10 dB at one point). Merge same-pitch repeats in legato string lines into one note with a CC11 notch (10 CC portato, 14 CC bow change, 8 CC at CC11 <= 40) (c03, c04).
- Long notes on some MAX sustain layers swell 8-17 dB at constant CC11: Oboe F5, cor anglais A4, Flute B♭6 (c02: cor anglais -49 -> -32 dB over a held p note). Soft unslurred Sus MAX string chords bloom 6-9 dB inside each note (c02). A soft re-attack on Leg Slur MAX after a gap rose 14 dB over 2.5 qn (c04 critic C). These are per-sample, so correct them per note.
- Fixes that worked: per-note level trims keyed by onset (0 dB at the onset to the full trim at onset + 0.6 s), found by a residual scan against the track's CC11 fit (c03: notes over +5 dB); a volume ramp of 0 to -4.5 dB over 2 qn on soft re-attacks (c04). Keying trims by pitch and minimum length hit the wrong notes (c03 critic B: an oboe trim landed on ff climax notes and missed the swelling p note).
- Tenuto inside a slur (portato) on a legato patch re-starts on the slow non-legato layer: Flute 2 bloomed 0.6 s after the beat and Oboe 1 sat 5-9 dB low for a half note at ff (c04 critic A). Play wind portato on Sus; it measured -1 to -8 dB at the joins on Sus patches (c04).

## 7. Other string and wind articulations

- Pizzicato (after loading the row): on time in every render except c04's slow-streaming render; decay 10-16 dB at 400 ms (c02, c03).
- Tremolo after a held note on another articulation: c03 arrived with 2-6 dB dips; c04 had 9-26 dB holes at the same notes with the same MIDI (c05 critic A). Attributed to streaming (section 11), not to CC11. Unresolved; a fallback is separate tremolo patch tracks so the KS Master never switches at the arrival (unverified).
- Tremolo chords on a section patch are much louder than single notes: Vln II 2-note tremolo +8.2 dB over its single-note fit (c03 critic B).
- Accents: keep `Sus Accent MAX` for f and louder; for softer accents add +8 CC11 decaying over 0.3 qn and velocity +10 (c01). A keyswitched accent measured +3 to +4 dB over the previous bar with +4 to +6 dB attack brightness (c03).
- sf: a short CC11 spike above the current level (+8 from f or louder, held 0.25 qn, then to the post level by 0.75 qn; +12 from softer levels) and velocity +15 (c02-c04). If a decrescendo starts at the sf, start the hairpin after the spike, not before it (c02 critic B: the hairpin had held ff for 0.75 qn).
- Breath marks: end the note before at `min(0.25 qn, 20%)` early (c01). A caesura before a tutti arrival was made by slowing the 0.25 qn before the breath (+0.22 s and +0.15 s) (c04).
- Clarinets on Sus Non Vib were kept throughout; their measured vibrato was 1-8 cents, as expected (c04 critic C).

## 8. Divisi, double stops and shared patches

- Every note of a chord on a section patch is a full-section sample: 2-note chords measured +1.8 to +2.0 dB over single notes on Sus MAX/Flautando, so a divisi passage is about twice as thick as written (c03 critic B). A level cut of -10·log10(k) dB under "div." and -1.5 dB for "non div." double stops, plus -3 dB for tremolo chords, fixed the measured cases (c03 -> c04: violas 5 dB under Vln I at the climax instead of 1.8 dB over).
- The Divisi folders hold DIV A / DIV B KS Masters (half sections) for 1st/2nd Violins, Violas and Celli. Not tried; it is the recommended route for divisi lines that need legato and for a section "solo" when no solo-string library is installed.
- Two tracks on the same patch file playing the same pitch together render the identical sample: correlation 0.999, a +6.5 dB coherent sum (Horns 1+2), or partial cancellation at correlation -0.86 (two clarinets: the sum was quieter than one) (c04 critic A). Drop the copy and give the kept note +10·log10(n) dB (c04). A recorded a2 patch (2FH KS Master) is the alternative (not tried).

## 9. Harp

- `Harp Maestro.oib` has no samples below MIDI 48: 79 of 175 notes in a normal harp part were silent (c01). `Harp Sus RR.oib`, `Harp Pluck Long.oib` and `Harp Thumb Pick.oib` cover 24-103 (c01).
- The Harp KS Master reaches only down to 36, and its keyswitches (21-35) overlap the harp's low notes (c00).
- Harp Maestro loads only the Close mic (c01).
- `Harp Harmonics.oib` (range 48-96) takes sounding pitch: notes measured 311 Hz and 622 Hz as written in sounding pitch (c01).
- Harp dynamics by velocity with CC11 constant at 110 worked: pp 52, p 64, mp 76, mf 90, f 100 (c01-c04). The harp rings after note-off and decays only 2-4 dB in 0.4 s (c03).
- Rolled chords: play from the lowest note up, 40 ms per note at mp or softer and 30 ms louder, top note +4 velocity (c04). A LilyPond extraction must listen for `arpeggio-event` explicitly; it is not an articulation event (c04 critic A).
- The Harmonics patch images further left than the Harp patch at the same pan settings (c05 critic C: R-L -9.5 vs -4.2 dB); match seats by measurement.

## 10. Timpani (Timpani Flt KS, felt sticks)

- The patch has no CC11; CC7 is the only level control. Velocity hardly changes roll level (c01 critic B).
- The roll articulation (Rls) is about 14 dB louder than single strokes (Lng) at the same CC7 and velocity (c01 critic B: p strokes -38 dB, p roll -24 dB).
- Strokes have a steep velocity step: velocity 41 measured -62 to -68 dB, velocity 53 -38 dB; an 8-16 dB step lies between 56 and 64 (c01, c02). Keep stroke velocity at 56 or more (pp) and 60-64 for pp/p strokes that must be heard.
- CC7 values from `127·10^(dB/40)` with roll targets ppp -36, pp -31, p -26, mp -23, mf -17, f -16, ff -14 dB, and strokes at roll +20 (pp), +12 (p), +16 (above), gave usable levels after track gain -7 dB (c01-c03). Put the roll settle and soft-roll cut in the volume envelope, not CC7: -5 dB over 3 qn measured -3.6 to -3.9 dB (c02, c03), and soft rolls (p or softer) need a further -6 dB to sit under pp strings (c03: bar-2 ppp roll -52.7 settling to -56.4 dB).
- Hold the settle until about 0.5 qn after the roll ends; restoring the level at the roll's last onset lifted its ring (c05 critic B; implemented c05, unverified).
- The KS patch loads Close, Main and Surround mics by default (c01). Timpani take 85-100% of the master's 100-300 Hz energy when the Surround mic and the 3.3 s percussion IR are on (c01 critic C).
- Missing timpani strokes (-94 and -117 dB) occurred in a render made with a cold disk cache after a reboot, and were present in the next render (c04).

## 11. Sample streaming and render timing

- Full-speed offline renders start notes up to 0.6 s late: several tracks at the same moment had about 0.5 s of digital silence then a full attack (510-515 ms in three tracks at once) (c01). Render at 1x offline: woodwind late entries 20 -> 3, strings at one entry 545-575 -> 135-350 ms, brass 515 -> 170 ms (c01).
- `RENDER_1X 1` cannot be set with `GetSetProjectInfo`; edit the `.rpp` line and reopen the project (c01). `render_cycle.py` warns when the line is missing.
- Wait for Opus to finish loading samples after a rebuild: a render right after a full rebuild had 83 late entries; the same project 25 minutes later had 26 (c02). Waiting for three quiet 10 s memory readings of the REAPER process (change under 50 MB) is the current rule (c02-c05).
- Even at 1x and after the memory wait, string timing can differ between renders of identical MIDI: celli pizz. 0.00-0.01 s late in c03, 0.09-0.23 s in one c04 render, 0.25-0.48 s in another; winds, harp and timpani were unaffected (c05 critic A). Only the large Hollywood Strings instances got later, which points to streaming (inferred).
- Gate every render with an attack probe before judging anything else: about ten isolated reference attacks with 0.06-0.20 s limits and a few held-note-to-tremolo arrivals with a 6 dB dip limit (c05: c03 passed 14 of 14, c04 failed 11). Re-render on failure. Implemented as `tools/probe_attacks.py`, called by `render_cycle.py` (c05; not yet run on a c05 render).
- Separate streaming from sample attack by rendering twice: streaming delays change between renders, sample-attack delays repeat exactly (c01, c03 critic C). Do not compensate streaming delays by moving notes (c01).
- Opus `PreloadSize` in `/Library/Application Support/East West/Opus/Preferences.json` (0 = Harddrive, 1 = SSD/SATA, 2 = SSD/PCIe, order from the Opus binary) was 1 throughout. Setting 0 is approved but not yet applied (file still reads 1 on 2026-10-11 09:32); its effect is unverified. Change it only with REAPER closed.
- Close other memory-heavy processes before rendering (c05 critic A found two other Python processes at about 3.2 GB each during the slow c04 render; causal link not measured).

## 12. Mics, reverb and panning inside Opus

- Factory mic balances differ widely between KS Masters: woodwinds Close 1.0 with Main 0.01-0.28 (Main 11-40 dB under Close), horns Close 1.35 / Main 0.44, strings Close 0.66 / Main 1.0, Basses Close 0.94 / Main 1.0, Tuba 1.0 / 1.0, Trombones Close 0.486 (c01 critic C, c05 critic C). Woodwinds then sound nearer than the strings.
- Settings used: woodwinds Close 0.5 / Main 0.8, horns 0.5 / 1.0, harp 0.6 / 1.0, strings and trombones at patch default (c01). c05 adds timpani Close 0.2 / Main 0.5 (Surround off), tuba 0.45 / 1.0, basses 0.4 / 1.0 (unverified).
- Mic channels to load are `layerMatrix.columns[n].loaded` plus the `mixer.channels` `sub:` channel `loaded` and `volume` (c01). Loading extra mics (e.g. Surround) adds sample memory (c05 critic C).
- Every patch carries its own reverb: a `ConvolutionReverb` on the `fx:0` channel fed by a `SendProcessor` on each mic channel. Across the KS Masters there were six different IRs and effective reverb levels from -10.6 dB (brass) to -24 dB (harp) (c01 critic C). Replace every patch's reverb insert with one copied from a single patch, set the same `fx:0` volume and `wet` everywhere, and set depth with the per-mic send level only (c01).
- Send levels that kept depth order: strings 0.25, harp 0.3, woodwinds 0.35, trombones/tuba/timpani 0.45, horns 0.5, with `wet` 2.0 (c01-c04).
- "S. Cal. Hall strings LR Rear" (the strings' factory IR) is a long hall (HO manual: 3.4 s). Stems decayed with a median late slope of 3.1 s against 1.5-1.95 s in a real recording, and dropped about 10 dB at 300 ms after a cutoff against 16-19 dB (c05 critic C). c05 switches to "New Hollywood Hall 2.0" from `3BS Sus MAX.oib` at fx volume 0.19 (unverified). It ships with Opus, so no IR file is needed.
- The patches pan their own Close channels (Cb +0.62, Vc +0.33, Bn +0.41, Vln I -0.31, etc.), and REAPER's default pan on a stereo track is a balance control; combined, the c00 mix had master coherence 0.07 at 0.8-3 kHz against 0.70 in a recording (c01 critic C). Set Opus sub-channel pans to 0 and place each track once.
- REAPER stereo pan mode (`I_PANMODE 5`, `D_PAN`, `D_WIDTH`) placed seats correctly (c04: Vln I -8.7 dB R-L ... Cb +5.2). Widths: 0.3 gave master correlation 0.76; wind 0.5, horn 0.6, others 0.5-0.6 gave 0.64 against 0.60 in the reference (c03 -> c04). Do not go below 0.3: the spaced Main pair folds to near mono (c01 critic C, inferred).
- Because the reverb is inside Opus, the REAPER pan and width move and narrow the reverb tail with the dry sound (c05 critic C: tails follow the seat, tail correlation 0.5-0.97). Also, a REAPER volume envelope after Opus changes the tail of notes already sounding (inferred). c05 moves the seat into Opus (each mic channel `panLeft = seat - width`, `panRight = seat + width`, `fx:0` return centred at full width, REAPER pan centre/width 1). Unverified: whether the Opus send is pre-pan. Fallback: Opus reverb off and one convolution on a REAPER bus fed post-FX/pre-fader.

## 13. Starting levels and balance rules

- At equal CC11, the raw patches are far apart. At p (CC 46): solo winds -35 to -45 dB, string sections -46 to -53 dB, double basses -34.6 dB, harp -56 dB (c00, K-weighted). Track gains that brought every solo wind and string section to -46..-52 dB at p: Vln I +5, Vln II +6, Vla +2, Vc 0, Cb -9 (later -7 with Close 0.4, unverified), Fl -1, Ob -5, CA -1, Cl -1, BCl +1, Bn -2, Cbn +2, horns -4, trombones/tuba 0, timpani -7, harp -4 (c01-c02). These depend on the mic settings in section 12.
- Rimsky-Korsakov's resonance ratios worked as targets: in piano one wind equals one string section; in forte a string section is about +3 dB over one woodwind, a horn about two woodwinds, a trombone about two horns (Principles, "Comparison of resonance"). Measured result at both climaxes after c04: Vln I 3.2-3.5 dB over every single wind (c05 critic B).
- Accompaniment at the same printed dynamic as a melody needs a level cut (players do it); 3-7 dB cuts over spans worked (c02-c05). A cut set for a loud passage can bury a soft countermelody in the same span; check both (c04 critic B: cello countermelody 10-15 dB under the tune after a climax cut).
- Find hot notes with a residual scan: per-note level against the track's CC11 fit; correct notes more than 5 dB over (c03-c05).
- A pp/ppp timpani roll should be 3-5 dB under the quietest sustained string section (c02 critic C target; reached in c04 except where a printed crescendo lifts it).
- Use A-weighting or K-weighting, not plain RMS, for balance between high and low instruments; RMS counted celli and basses a few dB higher than a listener hears them (c02 critic B, c04 critic C).

## 14. Low end

- The Basses KS Master carries almost all of the 40-90 Hz energy (c01: 99.7%; c04: within 0.1 dB of the master band). With default gains the master's 63 Hz third-octave band was +14.1 dB re 1 kHz against -6.2 in a recording (c00).
- Gain -9 dB on the basses brought 63 Hz to +4.7 (c01); a ReaEQ low shelf 90 Hz -7 dB plus a bell at 150 Hz +3 dB (1.4 oct) brought it to +1.1, and 40-90 Hz re 200-1000 Hz from -9.3 to -12.9 dB at the climax (c04). Low shelf 70 Hz -4 dB on contrabassoon and tuba (c04).
- The 125-180 Hz band stayed 4-6 dB under the reference (c04, c05 critic C). Inferred cause: the basses' Close mic proximity; c05 lowers it to 0.4 (unverified).
- Upper-string Main-mic stems carry room rumble at 16-29 Hz, 34-40 dB under their level, which sums across instances (c05 critic C). c05 adds 40 Hz high-pass on upper strings and winds, 30 Hz on celli/bassoons/bass clarinet/bass trombone, none on Cb/Cbn/tuba/timpani/harp (unverified).

## 15. REAPER and bridge behaviour

- REAPER ignores `D_VOL` once a track has a volume envelope: the first c02 render lost every track gain (Vln I -7 dB, Cb +8 dB). Put the static gain inside the envelope and set `D_VOL` to 1.0 (c02).
- Writing a volume envelope by script: select the track, get "Volume" (create with action 40406 if missing), make sure it is active (`ACT 1` in the chunk), delete the old points, insert points with `ScaleToEnvelopeMode(GetEnvelopeScalingMode(env), amp)`, then `Envelope_SortPoints` (`build_reaper.py`).
- A level-only update path (`--mix-only`: volume envelope, pan, ReaEQ) avoids reloading patches; anything inside the Opus state needs a full track rebuild (c01-c05).
- ReaEQ by script: add with `TrackFX_AddByName(tr, "ReaEQ", false, -1)`, set band types with `TrackFX_SetNamedConfigParm(..., "BANDTYPEn", ...)` (0 low shelf, 8 bell, 4 high pass) and `BANDENABLEDn`; parameter scales are not linear, so set frequency/gain/bandwidth by binary search on the normalized value until `TrackFX_GetFormattedParamValue` shows the target (c04; high-pass band c05, unverified).
- Render master plus every stem in one pass: `RENDER_SETTINGS 1`, `RENDER_BOUNDSFLAG 2` with the time selection set by `GetSet_LoopTimeRange`, pattern `$tracknumber_$track`, all tracks selected, action 42230 (c00-c04). Keep stem numbering stable by appending new tracks at the end (c01, c04).
- Timing: a 354 s render at 1x plus measurement takes about 5-6 minutes; the bridge call needs a long timeout (`--timeout 1800` used) and REAPER is blocked meanwhile (`render_cycle.py`).
- Reopening a project with 27 Opus instances takes about 15 minutes until all samples are loaded (stated in `loop/ONE_TIME.md`; not timed in a cycle).
- Tempo maps with many markers work: about 300 square markers (0.25 qn steps inside rit./allargando spans) caused no problems (c03). Changing the tempo map changes item timing, so rebuild all tracks after it (c03). Writing MIDI with `MIDI_GetPPQPosFromProjQN` keeps notes on quarter-note positions.
- Crashes and freezes seen: Opus crashed on a locator-only zone (c00); the Mac froze during the second render of c04 and needed a reset (cause not established; c05 critic C infers memory pressure). After the reset REAPER reopened the saved project and a state read-back matched the build data exactly (c04), so save before every render (`render_cycle.py` does).

## 16. Measurement methods that worked

- Render one stem per track with the master, and measure stems, not only the mix (c00-c05).
- Per-note level: K-weighted, from onset + 80 ms to min(note end, onset + 1.5 s), paired with the CC11 at the onset; fit dB against CC11 per track (dB/CC and level at p/f/ff); scan residuals for hot notes (c01-c05 critic B).
- Per-bar and per-beat stem levels against the printed dynamics, the list of loudest stems per bar, and group power sums (melody / harmony / bass) for balance at climaxes (c01-c05).
- Legato lag: time after the onset when energy at the new pitch's harmonics 1-4 exceeds the old pitch's (crossover), plus arrival within 6 dB; split by articulation and velocity (c02-c04). An f0 trace every 20 ms against candidate pitches for fast figures and grace runs (c03).
- Join dips: lowest 20 ms window after a join against the 200 ms before (c01-c03).
- Entry timing: "first sound" (within 20 dB of the early peak) and "arrival" (within 6 dB) for entries after at least 0.5 qn of silence; render twice to separate streaming from sample attack (c03, c05).
- Once notes are moved early for latency, keep the score onset in the data (`sq`) and measure against it; when the tempo map changes between cycles, convert each render with its own tempo map (c03, c05).
- Same-patch unisons: stem correlation in 0.5 s windows (c04).
- Space: per-stem L/R balance and correlation, side/mid ratio, tail balance after cutoffs, decay slopes (-5..-25 and -20..-40 dB) and the drop at 0.3/0.6/1.0 s after cutoffs (c01, c04, c05).
- Spectrum: long-term third-octave bands re 1 kHz against a reference recording, and band shares per stem to find which track makes a band (c01-c05). The reference used was a 128 kb/s live MP3 of a different piece, so allow a few dB in the bass and use it for shape and decay, not exact targets.
- State check: read notes, keyswitches, tempo markers, envelope points, widths and FX back from REAPER and compare with the build data before trusting a render after any crash or restart (c04).

## 17. Pipeline lessons

- Keep everything that changes the result in scripts and config files (`mix.json`, `roles.json`, `note_trims.json`); a setting made only inside REAPER is lost on the next rebuild (BRIEF).
- LilyPond extraction details that cost a cycle each: the slur stop event sits at the onset of the slur's last note, so test `start <= q <= stop` (c01); hairpins often have no stop event or a stop of the other kind, so close a hairpin at the next dynamic, the next hairpin or a rest of 2 qn or more (c01: a third of the printed dynamics were wrong, spans up to 268 qn); `arpeggio-event` needs its own listener (c04); `\removeWithTag #'part` can remove text that a second player on a shared staff needs (c05); a dynamic printed once on a shared staff may reach only one voice (c05).
- Check the extracted dynamic curve against every printed mark and print any miss over 2 CC (c01).
- Change one family of things per cycle and keep before/after snapshots of tools and config; that is how the c04 vibrato change was cleared as a cause of late attacks (c05 critic A).

## 18. Where `guides/reaper-claude-scripting-guide.md` is wrong or incomplete

- §6.2 and §7 say patch loading inside Opus is not reachable from ReaScript. It is: write the patch JSON into the Opus state with `TrackFX_SetNamedConfigParm(tr, fx, "vst_chunk", ...)` (section 1 here).
- §6.3 says CC1 crossfades dynamic layers and CC11 shapes within a layer, and the §6.6 map uses `dynamics = 1, expression = 11, vibrato = 21`. In Hollywood Orchestra CC11 crossfades the dynamic layers and sets volume, CC1 is vibrato, and no CC21 vibrato control is mapped (section 3).
- §6.6 placeholder keyswitches (24-29, "range C0-B0") do not match the KS Masters: string keyswitches run from 24 up to 50, celli use 80-90, harp 21-35. Read them from the `.oib` files rather than from a screenshot (section 2).
- §6.3 "leave 50 ms of keyswitch lead": in practice put keyswitches in the preceding rest, and a keyswitch only works if its articulation row is loaded in the patch state (section 2).
- §10 "Keyswitches have no effect" omits the most common cause here: the articulation row is not loaded in the KS Master.
- §5 `R.tracks()` reports `vol_db` from `D_VOL`, which is wrong once a track has a volume envelope (section 15).
- §6.5 / `R.render` do not mention render speed. Opus on an external sample drive needs 1x offline render (`RENDER_1X 1` in the `.rpp`, not settable through `GetSetProjectInfo`), a wait for sample loading, and an attack-timing check (section 11). `RENDER_SETTINGS 1` with `RENDER_BOUNDSFLAG 2` gave master plus stems in one pass; the guide's `what = 3` was not used.

## 19. Still open or unverified (as of c05 start)

- All c05 changes: hall IR "New Hollywood Hall 2.0" at fx volume 0.19; seat/width inside Opus; basses Close 0.4; timpani Close 0.2 / Main 0.5; tuba Close 0.45; high-pass filters; Horn 4 con sord.; keyswitch-inside-legato guard; timpani settle hold; attack probe gate.
- Opus `PreloadSize` 0 and its effect on string streaming lateness.
- Why held-note-to-tremolo arrivals go silent for 0.4-0.5 qn in some renders (streaming is the leading explanation, c05 critic A).
- Effect of role-based CC1 vibrato (c04): target was 20-40 cents peak-to-peak on solo oboe/cor anglais/flute long notes (c04 critic C measured 1-16 cents on the oboe before the change); not re-measured.
- CC70 finger position effect on sound; CC5, CC22, Slur Runs rows, DIV A/B patches, 2FH a2 patch, `currentTrigger`/`lastArticulationId` state fields: untested.
- Soft string entries remain 230-490 ms to arrival after a 0.12 s lead (c03); larger leads untested.
