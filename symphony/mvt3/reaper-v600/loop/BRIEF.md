# Movement IV (Finale) mockup loop: brief for every critic and actor

## Goal

The mockup is movement IV of the symphony, the Finale (Allegro con fuoco, C minor to C major; work folder `symphony/mvt3/`, score `symphony/mvt3/v600`), played in REAPER by EastWest Hollywood Orchestra Opus Edition (Diamond) through the Opus plugin and improved by actor-critic cycles. Each cycle makes it sound more like a real orchestra playing this score well. The score is fixed. Only the rendering changes.

Dan (2026-11-07): REAPER mockup actor-critic loops for the Finale, the same work as the Movement I and Movement II mockups, at least 20 loops, critiques from independent subagents. Cycle 0 is the port baseline: Movement I series 2's tools and generic settings (its c42), Movement I's mix, empty per-note tables, no Finale-specific tuning (`cycles/c00/PORT.md`). Cycles 1-20 are the improvement loops. Dan will judge the result by ear, so favour changes a listener hears; his priorities are articulations, per-track volume and blend, and long timpani rolls must not drown other parts.

Read `mockup-kit/LEARNINGS.md` (from "What a listener noticed that measurement missed" on) and Movement I series 2's `symphony/mvt1/reaper-v621/loop/LEARNINGS.md` before your first change: they hold about 70 cycles of measured lessons about this library and pipeline (Movement II series 2's `symphony/mvt2/reaper-v600/loop/LEARNINGS.md` adds a few). Do not relearn them. Movement I's `loop/MANUAL-GAPS.md` lists library features with what was tried and measured; this folder's `loop/MANUAL-GAPS.md` starts from it.

Dan's standing priorities for renders (from `symphony/render/BRIEF.md`, still his rules):
1. Articulations must be audible and correct: slurs/legato, tenuto, accents, staccato, tremolo, pizzicato, as printed.
2. Each track's level must match its printed dynamic and its role (melody above accompaniment) at every dynamic level.
3. Blend: one ensemble in one room (common reverb, seating, matched colours, nothing sticking out because of a sample set).
4. Accents: emphasis and weight, not a hard click (about 2-4 dB, no sharp transient). Brass accents soft: weight, not bite (the HO accent samples and a CC11 bump into the top layer put a 2-5 kHz burst 7-13 dB over the body and were heard as harsh; `GENTLE_ACCENT` plays accents on the plain sustain with a volume swell). Measure 2-5 kHz energy over the first 80 ms of each accent against the body and against the other sections.
5. Timpani rolls: start at the printed dynamic, then settle under the texture. Only a printed crescendo makes a roll grow. A long roll is never the loudest stem unless the timpani lead. The Finale has many rolls (bars 5, 147-152, 209-210, 219-223, 231-238, 243-246, 261-263, 273-278).
6. The delivered mp3 must be comfortable at one headphone volume: soft passages clearly audible, loud passages not painful. Targets (`loop/DYNAMICS-RESEARCH.md`): delivered LRA 14-16 LU, 16-19 dB from the 10th-percentile short-term loudness to the loudest, no reversed crescendos or diminuendos, the climaxes still clearly the loudest (here the C-major arrival at bar 223 and the final bars 271-279), delivery limiter at most about 3 dB. `render_cycle.py` masters the mp3 with `tools/deliver_master.py`; do part of the work in the mix (soft_trim_db, solo roles), not with CC11.
7. No audible sample-loop pulsing on long held notes. Hollywood Strings sustains loop every 3.95 s; one sample held for many seconds pulses in level and tone colour. `AUTO_REBOW` re-bows string notes over 4.5 s (staggered by `tools/space_rebows.py`). Check every held note over about 6 s (the chorale's whole notes at Maestoso, bars 223-234; the held chords of 271-279) on the stems and the master: 100-300 Hz band level and spectral centroid folded at 3.95 s, and the dip and step at each re-bow. Brass, winds and timpani rolls loop too.
8. Memory: keep REAPER's settled footprint under about 45 GB on this 96 GB Mac (unused articulation rows are unloaded: `UNLOAD_UNUSED_ROWS`). Restart REAPER before every render and quit it after (save first); record REAPER memory after the render in CHANGES.md. Other threads' processes may hold memory; check `top -o mem` before rendering. Do not add Opus instances without removing others; a second render pass (Movement I's `--pass2` tools) is the way to add tracks.

Dan (2026-11-07, after hearing the mockups): "It does sound too wet ... dial it back. Everything still sounds a bit mushy too." Less hall from c01 on, and clarity (separate attacks, clean releases, less smear) is a standing priority for every lens. Shared values (Movement I thread, mockup-kit/README.md item 7 and LEARNINGS section 12): `build/mix.json` reverb.fx_volume 0.19 -> 0.095 (-6 dB hall return), sends, IR, wet, high cut and true stereo unchanged, sends never raised to win the depth back; checks: the master's drop 0.3 s after each tutti cutoff at least 13 dB (recordings 13-17), late decay 1.5-2 s; if it still runs over 2 s, try a shorter hall IR. Also (2026-11-07): a 160 Hz low cut on the hall input (`low_cut_hz` 160 in mix.json reverb; the block from mockup-kit/pipeline/build_reaper.py). Being tested by Movement I c44, follow its results: a 1.5-2 s late decay via Opus's IR envelope (Opus manual p.133-134), and string same-pitch repeats not under one slur re-attacked on Sus MAX after a min(0.06 s, 25%) gap instead of merged with a CC notch. For clarity, look for 200-500 Hz build-up in the master against the references and prefer cuts there to treble boosts.

Dan's listening notes on Movement I series 2 (2026-11-06) and his notes for this mockup (2026-11-07), standing checks for every lens:
- **S1. Repeated notes must be heard as separate notes.** Check every same-pitch repeat (winds, brass and strings, slurred or not) for an audible gap or re-attack in the stem and in the master. The Finale is full of them: the hammered eighths of the coda (bars 199-210, movement I's layout), the basses' and timpani's repeated eighths and quarters, brass repeated notes in the chorale and the Più allegro. The library's repetition rows (LegRep RRx4, Leg Slur Rep) and `STR_REP_DETACH` / `WIND_REP_RETONGUE` are in place in the tools (Movement I c37-c38).
- **S2. The perceived centre of each attack must sit on the beat.** Measure the perceptual onset (`tools/pcx.py`; where the attack reaches its body level, or the energy centroid of the first 80-150 ms), not the MIDI note-on, against the beat grid, per section and per articulation. At this tempo (half note = 84, a quarter = 0.36 s) 40 ms is already audible as late.
- **S3. A subito must not sound like a glitch.** A sudden drop keeps the hall's ring of the louder level decaying under the softer one. CC7 and CC11 act inside Opus, before its hall; REAPER's volume envelope (roles, trims, hairpin dB ramps, fills) acts after the hall and cuts the tail. Put sudden drops in CC11/CC7, never as a fast fall in the volume envelope. The Finale's sudden drops: the sfp of bar 149 (qn 592, every brass, timpani and string staff), the fp chords and subito marks (search `mockup-events.tsv` for "fp", "sub."), ff cut-offs onto a soft entry (the second theme at 51 after the transition, the closing's end), and every role or trim row that ends with a step under a sounding chord.

## The music (score `symphony/mvt3/v600`, 279 bars of 2/2, about 7 minutes)

Symphony No. 1 in C minor, IV. Finale: Allegro con fuoco. Bar b starts at score qn 4(b-1); the half note is the beat (2 = 84 is 168 quarter notes per minute). The score ends at qn 1116 (the final chord is a quarter at qn 1112, then rests with a fermata). Sections (`sections.txt`, `global.ily`, the comments at the top of each `sections/*.ily`):
- Introduction, Allegro con fuoco 2 = 84, bars 1-10 (qn 0-40): after a pause from the scherzo, the German sixth on A flat ff, tutti without trumpets (1-2, 5-6), the strings' turn figure (motive x, 3-4), dominant preparation with a crescendo into A.
- A, first theme (F1), bars 11-26 (qn 40-104), C minor, f: strings with brass on the tune, clarinet broken chords, horn and bassoon off-beats.
- B, counterstatement, bars 27-42 (qn 104-168), ff: F1 in the bass, violin countersubject.
- C, transition over the B flat pedal, bars 43-50 (qn 168-200), p to pp: motive x Fl 1, Cl 1, Ob 1; poco rit. 49-50.
- D, second theme (F2), Poco meno mosso 2 = 72, bars 51-66 (qn 200-264), E flat minor: Trumpet 1's soft solo (dolce cantabile; the trumpets' first entry), pizzicato strings.
- E, F2 in E flat major in the violins, bars 67-82 (qn 264-328), cello counter-melody, harp; animando in bar 82.
- F, closing group, Tempo I, bars 83-98 (qn 328-392), f to ff; codetta with trumpets at 91.
- G-H, development, bars 99-134 (qn 392-536): call and response between wind and string groups, F minor, a bassoon solo in G minor (H, bar 115), the harp's solo in G major.
- J, retransition, bars 135-150 (qn 536-600): chain of diminished sevenths to the stop chord, ff V6/5, poco rit. 149-150 with the sfp at bar 149.
- K, recapitulation of F1, Tempo I, bars 151-170 (qn 600-680), ff, fuller scoring.
- L-M, recapitulated second theme, bars 171-198 (qn 680-792): F2 in C minor with Trumpet 1 con sordino doubling the cor anglais (171-197, "senza sord." at 199), C major statement in the violins (M, 187); poco rit. 197-198.
- N, coda 1, Tempo I, bars 199-210 (qn 792-840): the last C-minor tutti in movement I's hammered layout; poco a poco accelerando 205-210 (172-184 qn bpm).
- O, coda 2, Largamente 2 = 72, bars 211-222 (qn 840-888): theme B of movement II in the trumpets, D flat, ff; allargando 221-222.
- P, the C-major arrival and chorale, Maestoso 2 = 56, bars 223-234 (qn 888-936): Trumpet 1 B to C with the timpani roll, crash cymbals fff and bass drum ff at 223 (qn 888), string tremolo, the brass chorale in whole notes.
- Q, movement I's second theme in C major, Poco più mosso 2 = 66, molto cantabile, bars 235-246 (qn 936-984); stringendo 245-246 into
- R, Più allegro 2 = 88, bars 247-270 (qn 984-1080): both themes' heads combined ff in full brass over hammered eighths, the last chorale statement in doubled values (255-264), crash at 263 (qn 1048); allargando 271-272;
- T, Largamente 2 = 72, bars 273-279 (qn 1088-1116): closing tremolos and held chords, crash cymbals and bass drum at 278-279 (qn 1108-1112), the final C major chord fff.

Instrumentation: 2 flutes, 2 oboes, cor anglais, 2 clarinets, bass clarinet, 2 bassoons, contrabassoon; 4 horns, 3 trumpets in C (written at sounding pitch), 2 trombones, bass trombone, tuba; 4 timpani (hard sticks, "near the rim" at qn 708); percussion (2 players: crash cymbals, bass drum); harp (harmonics at qn 168, étouffez marks, a glissando at 277); strings (div., div. a 3, "4 soli" for Violins I at 473-511, "sul tasto, last 2 desks" at 376, pizz.). The score is in C; contrabassoon and basses sound an octave lower (basses with the C extension at bars 75-76, 166, 174-183, 189).

The mockup's 31 tracks (stems 01-31 in this order): Flute 1, Flute 2, Oboe 1, Oboe 2, Cor anglais, Clarinet 1, Clarinet 2, Bass clarinet, Bassoon 1, Bassoon 2, Contrabassoon, Horn 1-4, Trumpet 1-3, Trombone 1, Trombone 2, Bass trombone, Tuba, Timpani, Crash cymbals, Bass drum, Harp, Violins I, Violins II, Violas, Violoncellos, Double basses. Trumpet 1 plays its con sordino solo (qn 680-792) on the 1TP KS Master's "Mute Sus" row (`ART_SPANS`).

## Nobody can hear

You cannot hear audio. Judge by measurements and by reading the data: per-bar stem levels against the printed dynamics, spectra, loudness range, onset timing, note lengths and keyswitch placement in the MIDI, the measures named in items 4, 5, 7 and S1-S3, and comparison with real orchestral recordings (`symphony/render/assets/refs/`; the Dvořák 9/i recording is a lossy MP3, so do not tune the low end to it alone). Say which judgements are measured and which are inferred.

## Where things are (all under `symphony/mvt3/reaper-v600/`)

- `README.md`: how this mockup is built and what the port did. `mockup-kit/README.md` and `mockup-kit/LEARNINGS.md` (repo root): the method and everything learned so far.
- `mvt3-v600-mockup.rpp`: the REAPER project (31 tracks, one Opus instance each), set to render at 1x offline (`RENDER_1X 1`).
- `build/mockup.ly`, `build/mockup-events.tsv`, `build/mockup.midi`: the per-player extraction of the score (one staff per player plus a DrumStaff; MIDI plus every articulation, text, dynamic, hairpin, slur, tremolo and drum stroke with its position in quarter notes). The score sources are copies of v600 converted to LilyPond 2.26 (`build/global.ily`, `parts.ily`, `score-defs.ily`, `sections/`).
- `build/score_config.py`: the Finale's track table, percussion map, tempo ramps and every per-onset rule table, plus the generic settings carried over from Movement I (`score_to_parts.py` runs it in its own namespace; the defaults in `score_to_parts.py` are the generic rules). Per-note tables in `build/*.json` (roles, note_trims, pitch_trims, entry_leads, early_fills, leg_leads, loop_fills, loop_profiles, rebow_fills, rebow_moves, accent_fits, accent_bodies, cresc_fronts, auto_fills) are keyed by score onset. `build/mix.json`: gains, seats, mics, hall, EQ. `build/probe.json`: the attack-probe checks.
- `build/parts.json`: exactly what is written into REAPER: per track the patch, notes, keyswitches and CC lanes, all in score quarter notes (`sq` = score onset; `qn` = moved onset after leads).
- `tools/`: Movement I series 2's pipeline at its c42 plus the port's edits (README): `score_to_parts.py`, `space_rebows.py`, `build_reaper.py` (`--midi-only`, `--mix-only`, `--tempo`, `--pass2`), `reaper_ctl.py` (owner "mvt3": lock, start, open, save, quit, restart, unlock), `render_cycle.py N` (save, wait for samples, render master + stems at 1x, measure, attack probe, delivery mp3 `cycles/cNN/mvt3-mockup-cNN.mp3`), `measure.py`, `probe_attacks.py`, `pcx.py` (perceived attack and legato timing), `deliver_master.py`, `motion.py`, `auto_fills.py`, `fit_rebows.py`, `fit_loops.py`, `fit_accents.py`, `fit_accent_bodies.py`, `stem_fix.py`, `rendermap.py`.
- `~/.rpr-bridge/`: the REAPER bridge (`python3 ~/.rpr-bridge/rpr.py run job.lua`), `libs/ew_ho/opus_state.py`, `libs/ew_ho/ks_maps.json` and `build/ks_maps_extra.json` (keyswitch maps read from the patch files), `libs/ew_ho/dump_ks.py`; `~/.rpr-bridge/REAPER.lock` (the shared REAPER lock, below).
- The score: `symphony/mvt3/v600/score.pdf` (render pages with `pdftoppm -f N -l N -r 90 -png`), `sections/*.ily`, `global.ily`.
- Sample libraries: `/Volumes/MAC DRIVE/EW Hollywood {Strings,Brass,Harp,Orchestral Woodwinds,Orchestral Percussion} Diamond/*Opus Instruments/` (`.oib` patch files: KS Masters, individual articulations, divisi, ensembles, mutes, percussion). Any of them can be loaded with `opus_state.py`.
- Library knowledge: `guides/eastwest-hollywood-orchestra/` (HO and Opus manuals as text; the May 2021 edition `text/EW-Hollywood-Orchestra-Opus-Edition-User-Manual-2021.txt` has the most per-instrument detail; `DIGEST.md` is a per-instrument digest with page numbers) and `guides/reaper-claude-scripting-guide.md` (where it is wrong for this library: `mockup-kit/LEARNINGS.md` section 18). Orchestration books: `reference-books/` (`INVENTORY.md`; text in `reference-books/text/`).
- Loop records: `loop/HISTORY.md` (one entry per cycle), `loop/LEARNINGS.md` (new lessons from this movement, appended by actors), `loop/MANUAL-READING.md` (which manual pages each critic reads), `loop/MANUAL-GAPS.md` (library features the mockup does not use yet), `cycles/cNN/` (reports, render, metrics, CHANGES.md, mp3).
- Movement I's `symphony/mvt1/reaper-v621/` and Movement II's `symphony/mvt2/reaper-v600/` are references (their `loop/HISTORY.md`, `loop/LEARNINGS.md`, `cycles/*/CHANGES.md`, `cycles/*/actor_scripts/`, `build/score_config.py`); never write into them.

## Facts already established (details and numbers in mockup-kit/LEARNINGS.md and Movement I's loop/LEARNINGS.md)

- HO: CC11 crossfades the dynamic layers and sets volume in the string and most woodwind KS Masters; there CC1 crossfades a non-vibrato and a vibrato layer (not a depth control). In the Hollywood Brass KS Masters and the Clarinet KS Master CC1 crossfades the dynamic layers (`CC1_DYN_TRACKS`). Make balance corrections in the volume envelope so CC11 keeps each printed dynamic's timbre.
- Legato patches are monophonic; transitions need overlap; legato targets start early by measured per-family leads; a same-pitch re-attack on Leg Slur MAX plays the slow first-note layer.
- KS Masters load only some rows; `build_reaper.py` loads the rows a track uses and unloads the rest, so a track whose set of rows changes is fully rebuilt. Opus saves each string group's start-mode CC70 value in the plugin state: a track rebuilt fresh plays finger position 4 (CC70 127) by default (Movement I c38-c41).
- A silent 3 qn pre-roll carries each track's first keyswitch and CC values and the CC36 round-robin reset; `render_cycle.py` cuts it off, so the rendered files are on score time.
- The audio device is part of the render conditions: `render_cycle.py` refuses to render unless REAPER's device is 48000 Hz, 512-sample blocks, no input (REAPER is set to the Mac Studio Speakers with no input device). REAPER closes its audio device when it is not the frontmost app: reopen it with a bridge job calling `reaper.Audio_Init()` just before the render (model: `symphony/mvt1/reaper-v621/cycles/c35/actor_scripts/_c35_audio_init.lua`, read only). Never save with `Main_SaveProjectEx` and a path; use `reaper_ctl.py save`.
- Render-to-render variance: identical data has rendered 4-15 dB different on some legato phrases (Movement I c42, Trumpet 1); compare unchanged passages between renders before crediting or blaming a change.

## Rules

- Only the actor drives REAPER. Critics never run `rpr.py` or `reaper_ctl.py`, never touch the bridge folder, never write into the `.rpp`, and never start renders. Critics may run their own analysis scripts on the rendered files (`~/.venvs/claude-composes-reaper/bin/python` has numpy, soundfile, mido; also ffmpeg, lilypond).
- REAPER is shared with the Movement I, Movement II and scherzo mockup threads through `~/.rpr-bridge/REAPER.lock`. Before any REAPER step the actor runs `~/.venvs/claude-composes-reaper/bin/python symphony/mvt3/reaper-v600/tools/reaper_ctl.py lock "mvt3 cNN actor"` (it waits up to 6 h while another thread holds REAPER; run it again if it times out), keeps every bridge job's `.lua` file inside `symphony/mvt3/reaper-v600/`, and after the render and any `--mix-only` write for a stem fix runs `reaper_ctl.py quit` and then `reaper_ctl.py unlock`. Never break, edit or remove another thread's lock. Turn rule (2026-11-07, refined): the longest waiter goes first. Before locking, run `ps -axo pid,etime,command | grep -E "reaper_ctl.py lock|reaper_lock.py acquire"`; if another thread's waiter has been waiting longer than this actor, let it go first (wait until its lock has come and gone, then lock). Do all non-REAPER work (edits, parts.json, diffs, simulations) before taking the lock, so the lock is held only for the build, the restart, the render and the save.
- Never edit the score or anything in `symphony/mvt3/v600/`, `symphony/mvt1/`, `symphony/mvt2/`, `symphony/scherzo/`, `symphony/render/`, `mockup-kit/`. Never commit or push. Never delete files outside your own cycle folder and your own scratch folder.
- Do not install software (no pip, brew or downloads). No GUI or computer use; REAPER is driven only through the bridge and `reaper_ctl.py`.
- Everything that changes the result lives in scripts or config files under `symphony/mvt3/reaper-v600/` (tools, `build/score_config.py`, `build/*.json`), so the project can be rebuilt from scratch. A setting made only inside REAPER is lost when a track is rebuilt. Keep generic rules generic: a rule that would help any score goes in `tools/` with a default, its Finale values in `build/score_config.py`.
- The printed notes, dynamics, articulations and tempos are the reference. A rendering must not contradict them. Small liberties that real players take (shaping inside a hairpin, a slight swell on a long note, breath before a breath mark, a little rubato inside a printed rit.) are allowed if the score supports them.
- One render per cycle, from a freshly restarted REAPER; fix level-only problems on the stems afterwards (`tools/stem_fix.py`, mockup-kit LEARNINGS section 15) instead of rendering twice.
- Keep scratch under 2 GB per agent, in `/private/tmp/claude-501/mockup-loop/mvt3-<your label>/`, and delete your scratch folder when you finish. Before rendering, check `df -h /System/Volumes/Data`: at least 30 GB must be free. Stem fixes keep copies only of the stems they replace.

## Movement I c44 dry-hall changes (2026-11-07, adopt in every cycle from c02/c03)
1. mix.json reverb "ir_setup": {"envelopeMode": 2, "endPos": 0.5, "decayLength": 0.5}. The code is the irSetup block in mockup-kit/pipeline/build_reaper.py apply_mix. simpleDecay does nothing. Measured on Movement I: fermata slope 2.42 to 1.29 s; recordings give 1.1-1.6 s.
2. mix.json sus_release_cap_ms: section strings {"ms":150,"dyn":["pp","p","mf","f","ff"],"rows":["Sus MAX","Sus Marc LITE"]}; horns {"ms":237,"dyn":["pp","mf","f"],"rows":["Sus MAX","LegRep RRx4"]}. Refit re-bow fills afterwards.
3. S1: STR_REP_NEW_BOW (Movement I tools/score_to_parts.py; settings in mvt1 cycles/c44/CHANGES.md item 3).
Each of these is an Opus state change, so rebuild every track fully.

## Movement I c45 values (2026-11-07; mvt1 cycles/c45/CHANGES.md "Values for the other movements"; kit commit 409ab8de)
- Hall: keep the c44 envelope. Movement I measured it at the dry end of the reference range (tutti stops fall 20 dB in 0.45-0.55 s). If Dan calls it too dry, raise fx_volume to 0.12 and leave the envelope.
- Width: set side-only low cuts to 0 dB. Add mix.json width_by_mic: Main 0.35 on the wind, horn, trumpet and lowbrass groups, Main 0.45 on celli and basses, Main 0.2 on the solo winds (Clarinet 1, Horn 1, Trumpet 1). This is an Opus state change, so rebuild those tracks fully. Target: master side/mid at about -6 dB (references -4.7..-5.4).
- After any re-bow refit: no rebow_fills list may end on a non-zero value (REBOW_FILL_END_S).
- STR_REP_NEW_BOW repeats caught by sus_min_s need the re-tongue lead.
- rt_gain_db: do NOT adopt. Movement I's c45 test was invalid (its pass-2 alias stems had wrong CC data from the espr./dolce boost-span bug near score_to_parts.py line 3024), so the result is unknown either way. Wait for Movement I c46. Before any pass-2 test stem replaces or is compared with a main stem, diff its parts.json notes and CCs against the source track.

## Soft endings warning (2026-11-07, Movements I and II)
A 150 ms string release cap at pp/p makes soft endings stop abruptly. Measured elsewhere: the ppp final chord lost 10 dB in 0.07 s. References: soft ends fall 10 dB in 0.20-0.40 s, and phrase ends fall 20 dB in 0.43-0.58 s. Movement II c41 uses 300 ms at mf-ff and 400 ms at pp/p; Movement I c46 is testing 150 ms at mf-ff and 350 ms at pp/p. Measure the Finale's soft ends against the references and set the cap by dynamic.

## Disk space (2026-11-08, Dan: "They can delete shit if they need")
The disk is nearly full (about 36 GB free). Once a cycle's critics have finished, its stem WAVs are deleted, except for the two most recent cycles. Keep every 00_Master.wav, mp3, report, metrics file and CHANGES.md. Never delete other threads' files.

## EastWest template mix (2026-11-08; Dan wants every finding used). This is the default from c06.
Read mockup-kit/EW-TEMPLATE-PLAN.md and EW-TEMPLATE-FINDINGS.md, plus the mockup-kit README. Movement I made this the default for all four movements (its c50 = mix, c51 = performance data). Port the kit's tool code from mockup-kit/pipeline rather than writing new code.
- c06 (mix, items 1-4):
  - Mic layout: pan_by_mic, replacing width_by_mic. Add the template's REAPER track pans.
  - Reverb: turn the Opus reverb off on every track. Add Spaces II family return tracks with their ReaEQs and the plan's send levels. Render the returns as extra stems, so the master is the dry stems plus the return stems.
  - Section EQ: add the family EQs and the master EQ. Remove the old EQs that only duplicate them.
  - Refit the delivery chain (deliver_master.py) to the targets.
  - Keep one pass-2 copy of the old layout for comparison. Diff its notes and CCs against the source tracks first.
  - This replaces the c44 hall settings (fx_volume 0.095, the IR envelope, the 160 Hz low cut) and width_by_mic. Each change is an Opus state change, so every track needs a full rebuild.
- c07 (performance data, item 5):
  - Legato overlaps and repeated-note gaps.
  - Legato velocity 90 or more where a clear note change is wanted.
  - A pass-2 test on the strings that moves the dynamics from CC11 into CC1, comparing CC1-only with the current CC11.
- Critics measure each item and can reject one only with numbers.
- REAPER memory is at the 45 GB limit. Check the cost of the return tracks.
- Exact template FX states (commit 1e9808d9) are in symphony/mockup-research/ew-template-2026-11-08/:
  - ho-mix-chunks/*.txt: the verbatim FXCHAINs; load them with TrackFX_SetNamedConfigParm(fx,"vst_chunk",...).
  - ho-mix-fx.json, opus-mics.txt, midi-report.txt.
- Corrections to the plan:
  - Pre-delay by family: strings 19.6 ms, winds 18.5, brass 10, perc 10.
  - Every return uses the full IR, and the brass return loads the Horns impulses.
  - The template's KS Masters use the Opus macro "Mod + Expression Combo": a single CC1 lane drives vibrato and dynamics, with no CC11 (c07).
- Research batch 2 is in EW-TEMPLATE-PLAN.md section 6 (commit f5077a89), for c07 and later:
  - CC1 57-79 sits inside the woodwinds' dual Non Vib/Vib zone (55-76). Measure mp-mf sustains for doubled modulation, or cross that zone quickly.
  - String shorts: CC parked at 118-127 and dynamics by velocity. Brass and wind shorts use velocity 62-95. Shorts are 60-90 ms long and on the grid.
  - Shape CC1 per phrase: flat across legato changes, a swell after the phrase start, and a taper of 13-37 units over the last 0.25-1 s.
  - Strings get a separate legato track ("Leg Slur + Port LITE", LegatoSpeed and RTKiller on). Keyswitches go 40-800 ms early.
  - Keep our measured release caps; EW keeps the long releases.
- Research batch 3, EW-TEMPLATE-PLAN.md section 7 (commit 773b0244). It comes from a hand-played mockup on other libraries: take the shapes, not the absolute values.
  - Phrase rule, adopted by default: a CC swell after the first onset (about +15 by 0.4 s, +25 by 0.8 s); a taper of about 20 over the last second; scaled to the dynamic; printed hairpins take over.
  - Lean-off of about -2 per note inside slurs.
  - Fixed early shift per wind track (about -27 to -85 ms). Strings and brass -20 to -120 ms. Percussion on the grid.
  - CC density 13-44 points/s.
  - Measure our lead tables against these shifts before changing them.
- Research batch 4: 20 expert MIDI mockups, in EW-TEMPLATE-PLAN.md section 8 (commit 25bbfbf2). New defaults:
  - Repeated-note gaps 60-100 ms. Medians: winds 63, strings 90, brass 98, short rows 116.
  - Phrase arch peaking at 33-62% of the phrase, with a range of 30-60 units on long phrases. Long notes keep moving.
  - Legato velocity follows the dynamic.
- A/B tests in pass 2:
  - Duc's single hall against the EW returns. The hall: 2.1-2.45 s, low cut about 184 Hz, high cut about 3 kHz, return -5.5/-6.6 dB, low-string shorts sent 7 dB lower.
  - A string EQ variant.
  - A tutti entry spread of 36-55 ms against exact alignment.
  - A room-noise bed, only from a recording we are free to use.
- Dan, 2026-11-08: "yes to anything you can do ... don't wait". Apply every research finding from batches 1-4 now: symphony/mockup-research/ew-template-2026-11-08/FINDINGS.md, plus the raw reports in that folder. Don't wait for Movement I's tools or plan updates; write the generic code here if the kit doesn't have it yet. c06 does the mix. c07 does everything else: PHRASE_SHAPE, legato velocity by dynamic, repeat gaps 60-100 ms, early shifts per track, the CC1-only test, and the A/B pass-2 tests. A finding is rejected only with measured numbers.
- Movement I commit 96d05220: every item in EW-TEMPLATE-PLAN.md sections 1-8 is now a default. Changes that were A/B tests and are now defaults:
  - Duc's sends: 0 dB on violins, violas and brass; -1.6 dB on cello and bass longs; -7 dB on low-string shorts.
  - Basses EQ: -2.4 to -3.6 dB at 205-250 Hz.
  - Seeded tutti entry spread of 36-55 ms.
  - Room-noise bed, only with a free recording.
  - Duc's single shorter hall is the fallback if the EW returns measure mushy.
  An item is dropped only with measured evidence, recorded in LEARNINGS.
- Duc hall fallback, details from Movement I: Spaces II "Hollywood Scoring Stage TS RR 2.3s", a 184 Hz high-pass and a 3 kHz low-pass before the IR, return -5.5 dB. Movement I's tools have it as a second send profile. For brightness, halve the +4-5 dB family shelves before touching the master EQ.
- Research batch 5: FINDINGS.md Part 5 (commit c1cc028d, branch claude/project-thread-cn1rc0; read it with `git show`). Source: the Goldsmith Mulan and Hisaishi Howl Cubase projects on VSL Synchron. Adopt from c07:
  1. No hall send, or -16 dB or lower, on low brass, bassoons, contrabassoon and basses. About -10 dB on everything else. Percussion unchanged.
  2. A/B a 1.8-2.3 kHz low-pass on the hall return, with 25 ms pre-delay.
  3. Crescendos rise early, then settle. Diminuendos fall on the last held note. Winds and brass may fade nearly out before rests.
  4. A/B narrow brass: horns at 15-47% width, panned left; trumpets at about 43%, panned right.
  5. A detailed tempo map: changes on about 20% of beats, and phrase breaths more than 15% slower.
  Keep the 60-100 ms repeat gaps.
- Research batch 6: Balfe MIDI sketches, FINDINGS.md Part 6 (commit 23a6225a, branch claude/project-thread-cn1rc0). Adopt from c08:
  1. Phrase shape by music type:
     - builds to a climax enter near zero (CC under 15) and peak at 0.95 of the phrase;
     - accented brass and fanfares enter at the top and fall 15-25 by the end of a long note;
     - lyrical lines keep the centred arch.
  2. Ostinato velocity, for the hammered eighths and the Più allegro figures:
     - each beat or half-beat group falls 15-17 velocity steps from first note to last;
     - ±5-7 seeded random variation;
     - strong beats +20-25;
     - two layers of one figure may alternate accents.
  3. Instruments doubling a line share one dynamics curve.
  4. A/B: brass timbre 25-35 under its level; strings about 15 over.
  5. Spiccato note length about 60% of the slot.
- Research batch 7: FINDINGS.md Part 6 rewritten (commit b01434e6). It supersedes batch 6:
  - DROPPED: batch 6 item 4, the brass/strings timbre offset. Still ride the level lane in the same shape as the timbre lane.
  1. Phrase shape by music type:
     - driving music at 105-150 bpm (most of the Finale) starts high and falls, or peaks early, at 0.05-0.30 of the phrase;
     - builds peak at the end;
     - lyrical lines keep the centred arch.
  2. Short-note velocity by position in the beat, with 15-25 steps between the strongest and the weakest note. In running 16ths, use either the beat / 16th / and / 16th pattern (95, 72, 83, 72) or a fall of 15-17 across each group. Add ±5-7 seeded random variation.
  3. Spiccato note length 50-62% of the slot.
  4. Instruments doubling a line share one dynamics curve.

## Wetness ceiling (2026-11-08, Dan's "too wet"; the scherzo saw the same)
c06 (EW template returns) was wetter than c05: tutti cut-offs fell 20 dB in 0.62-0.73 s (c05 0.41-0.50) and the RT60 estimate was about 2.0 s (c05 1.0-1.5). From c07 on, no cycle may be wetter than c05: tutti -20 dB in 0.50 s or less, RT60 1.5 s or less, violin soft ends -10 dB in 0.30 s or less. Lower the return levels or use the Duc hall fallback until those numbers hold. Study originals: reference/ (INDEX.md).

## EW template corrections from Movement I c50 (critic B, symphony/mvt1/reaper-v621/cycles/c50/reports/B.md)
- Timpani: the template's +8.6 dB at 84 Hz plus the Surround mic at 0 dB took the timpani's share of 30-150 Hz from 13% to 31% in a roll, against Dan's "rolls must not drown parts". Use a reduced EQ and no Surround mic, and measure the 30-150 Hz share in rolls.
- The brass family EQ costs 6-9 dB K-weighted (strings 1.3-1.9). Set make-up per instrument and dynamic: soft trombones and trumpets lose more, soft horns and tuba less.
- Winds run 1.5-2 dB hot (doubled Close mic); tam-tam and cymbals about 3 dB hot (no family EQ).
- Harp high-pass: 80 Hz, not 183 Hz.
- Also from Movement I c50 (decays and brightness): every tutti stop drops at least 15 dB by +0.3 s; late slope 2.0 s or less; each tail's 60-250 Hz share no more than 2 dB over the previous cycle. Fix order: section-9 register sends (low winds, low brass and basses 10 dB under their family send, trumpets 6 dB under), then the irSetup envelope (mode 2, endPos 0.5, decayLength 0.5), then the Duc 2.3 s hall. Brass accents: the master's 2-5 kHz jump p90 under +2 dB; if over, set the 821 Hz bell to -4 dB or add a 3.2 kHz -3 dB bell, and remove any trumpet 4 kHz shelf that stacks on the family shelf.

## Sharing (Dan, 2026-11-09)
After each cycle, add any new measured technique to loop/SHARED-TECHNIQUES.md and send the update to the Movement I, Movement II and scherzo threads.
