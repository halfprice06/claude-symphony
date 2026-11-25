# Movement I mockup loop: brief for every critic and actor

## Goal

Dan (2026-10-12): a high-quality REAPER mockup of symphony movement I, score `symphony/mvt1/v221`, played by EastWest Hollywood Orchestra Opus Edition (Diamond) through the Opus plugin, improved with 30 actor-critic cycles, made the same way as the movement II mockup (`symphony/mvt2/reaper/`, 27 rendered cycles). Each cycle makes it sound more like a real orchestra playing this score well. The score is fixed. Only the rendering changes.

Read `mockup-kit/LEARNINGS.md` (from "What a listener noticed that measurement missed" on) before your first change: it records 26 cycles of measured lessons about this library and pipeline. Do not relearn them.

Dan's standing priorities for renders (from `symphony/render/BRIEF.md`, still his rules):
1. Articulations must be audible and correct: slurs/legato, tenuto, accents, tremolo, pizzicato, as printed.
2. Each track's level must match its printed dynamic and its role (melody above accompaniment) at every dynamic level.
3. Blend: one ensemble in one room (common reverb, seating, matched colours, nothing sticking out because of a sample set).
4. Accents: emphasis and weight, not a hard click (about 2-4 dB, no sharp transient).
5. Timpani rolls: start at the printed dynamic, then settle under the texture. Only a printed crescendo makes a roll grow. A long roll is never the loudest stem unless the timpani lead.
6. The delivered mp3 must be comfortable at one headphone volume: soft passages clearly audible, loud passages not painful. Targets (`loop/DYNAMICS-RESEARCH.md`): delivered LRA 14-16 LU, 16-19 dB from the 10th-percentile short-term loudness to the loudest, no reversed crescendos or diminuendos, the climaxes still clearly the loudest, delivery limiter at most about 3 dB. `render_cycle.py` masters the mp3 with `tools/deliver_master.py`; do part of the work in the mix (soft_trim_db, solo roles), not with CC11.

Dan's listening notes on movement II, which apply here from the first cycle (each came from a person hearing a render after the measurements had passed it):
7. **No audible sample-loop pulsing on long held notes.** Hollywood Strings sustains loop every 3.95 s; one sample held for many seconds pulses in level and tone colour, and sections that start a chord together pulse in step ("a weird bowing effect"). `score_to_parts.py` re-bows every string note longer than 4.5 s automatically (`AUTO_REBOW`, `REBOW_SEG_S`, `REBOW_TRACK_JITTER`): same-pitch Sus MAX pieces at staggered times per section. Check every held note over about 6 s on the stems and the master: the 100-300 Hz band level and the spectral centroid folded at the loop period (autocorrelation at 3.95 s), and the level dip and step at each re-bow (Sus MAX and Leg Slur MAX sustains differ by 3-9 dB at one CC11; mvt II c26 fitted a level shape per re-bow, `build/rebow_fills.json`). Brass, winds and timpani rolls loop too; check the long ones.
8. **Brass accents soft: weight, not bite.** The HO accent samples and an accent CC11 bump into the top layer put a 2-5 kHz burst 7-13 dB over the note body, heard as harsh. `score_to_parts.py` plays every brass accent as plain Sus (`GENTLE_ACCENT`: no accent sample, no CC11 bump, no extra velocity, a volume swell full at +0.07 s, held to +0.25 s, gone by +0.6 s; +4 dB at f and louder, +2.5 dB softer). Measure 2-5 kHz energy over the first 80 ms of each accent against the note's body and against the other sections, as well as level over the neighbours. Movement I's Allegro has many accented brass and string notes; the same caution applies to winds and strings.
9. Memory: keep REAPER's settled footprint under about 45 GB on this 96 GB Mac (unused articulation rows are unloaded: `UNLOAD_UNUSED_ROWS`). Restart REAPER before every render and quit it after (save first); record REAPER memory after the render in CHANGES.md. Another user process may hold several GB; check `top -o mem` before rendering.

## The music (score `symphony/mvt1/v221`, 182 bars of 4/4, about 7 min 11 s at the printed tempos)

Symphony No. 1 in C minor, I. Lento — Allegro appassionato. Bar b starts at score qn 4(b-1). Sections (`sections.txt`, `global.ily`):
- Intro, Lento q=50, bars 1-14 (qn 0-56): timpani opening, slow string and wind chords, horn and woodwind solos.
- First theme, Allegro appassionato q=126, bars 15-32 (qn 56-128).
- Transition, bars 33-46 (qn 128-184), poco rit. at 45-46.
- Second theme, Poco meno mosso q=112, A-flat major, bars 47-68 (qn 184-272); poco animando 62-63, rit. 66-68.
- Closing, Tempo dell'Allegro, bars 69-76 (qn 272-304).
- Development, bars 77-130 (qn 304-520): allargando 121-122, sostenuto q=100 at bars 123-126 with the tam-tam fff (heavy beater, qn 484, l.v. to bar 126) and the brass, a tempo 127.
- Recapitulation: first theme bars 131-146 (qn 520-584, poco rit. 145-146); second theme bars 147-166 (qn 584-664) with poco animando 156-158, the suspended-cymbal roll pp < (bar 159) into the fff crash cymbals and largamente at bar 160 (qn 636, the movement's single fff and main climax), rit. 165-166.
- Coda, bars 167-182 (qn 664-728): Tempo dell'Allegro 167-170 (fermata on qn 679), Più lento q=72 from 171, tam-tam pp (soft stick) at bar 175, rit. 177-178, Tempo I (Lento) 179-182, the strings' final ppp chord ("change bow at will", fermata) leading attacca into movement II.

Instrumentation: 2 flutes, 2 oboes, cor anglais, 2 clarinets, bass clarinet, 2 bassoons, contrabassoon; 4 horns, 3 trumpets (in C, written at sounding pitch), 2 trombones, bass trombone, tuba; timpani; percussion (tam-tam, suspended cymbal, crash cymbals); harp; strings. The full score is in C; contrabassoon and basses sound an octave lower.

## Nobody can hear

You cannot hear audio. Judge by measurements and by reading the data: per-bar stem levels against the printed dynamics, spectra, loudness range, onset timing, note lengths and keyswitch placement in the MIDI, the measures named in items 7-8, and comparison with real orchestral recordings (`symphony/render/assets/refs/`; the Dvořák 9/i recording is a lossy MP3, so do not tune the low end to it alone). Say which judgements are measured and which are inferred.

## Where things are (all under `symphony/mvt1/reaper/`)

- `README.md`: how this mockup is built. `mockup-kit/README.md` and `mockup-kit/LEARNINGS.md` (repo root): the method and everything learned on movement II.
- `mvt1-v221-mockup.rpp`: the REAPER project (32 tracks, one Opus instance each), set to render at 1x offline (`RENDER_1X 1`).
- `build/mockup.ly`, `build/mockup-events.tsv`, `build/mockup.midi`: the per-player extraction of the score (MIDI plus every articulation, text, dynamic, hairpin, slur, tremolo and drum stroke with its position in quarter notes).
- `build/score_config.py`: movement I's track table, percussion map, tempo ramps and every per-onset rule table (`score_to_parts.py` runs it in its own namespace; the defaults in `score_to_parts.py` are the generic rules). Per-note tables in `build/*.json` (roles, note_trims, pitch_trims, entry_leads, early_fills, leg_leads, loop_fills, loop_profiles, rebow_fills) are keyed by score onset and start empty. `build/mix.json`: gains, seats, mics, hall, EQ. `build/probe.json`: the attack-probe checks.
- `build/parts.json`: exactly what is written into REAPER: per track the patch, notes, keyswitches and CC lanes, all in score quarter notes (`sq` = score onset; `qn` = moved onset after leads).
- `tools/score_to_parts.py` (score -> parts.json), `tools/build_reaper.py` (parts.json -> REAPER; `--midi-only`, `--mix-only`, `--tempo`), `tools/render_cycle.py N` (save, wait for samples, render master + stems at 1x, measure, attack probe, delivery mp3 `cycles/cNN/mvt1-mockup-cNN.mp3`), `tools/measure.py`, `tools/probe_attacks.py`, `tools/deliver_master.py`, `tools/motion.py`, `tools/auto_fills.py`.
- `~/.rpr-bridge/`: the REAPER bridge (`python3 ~/.rpr-bridge/rpr.py run job.lua`), `libs/ew_ho/opus_state.py`, `libs/ew_ho/ks_maps.json` and `build/ks_maps_extra.json` (keyswitch maps read from the patch files), `libs/ew_ho/dump_ks.py`.
- The score: `symphony/mvt1/v221/score.pdf` (render pages with `pdftoppm -f N -l N -r 90 -png`), `sections/*.ily`, `global.ily`.
- Sample libraries: `/Volumes/MAC DRIVE/EW Hollywood {Strings,Brass,Harp,Orchestral Woodwinds,Orchestral Percussion} Diamond/*Opus Instruments/` (`.oib` patch files: KS Masters, individual articulations, divisi, ensembles, mutes, percussion). Any of them can be loaded with `opus_state.py`.
- Library knowledge: `guides/eastwest-hollywood-orchestra/` (HO and Opus manuals as text) and `guides/reaper-claude-scripting-guide.md` (where it is wrong for this library: `mockup-kit/LEARNINGS.md` section 18). Orchestration books: `reference-books/` (`INVENTORY.md`; text in `reference-books/text/`).
- Loop records: `loop/HISTORY.md` (one entry per cycle), `loop/LEARNINGS.md` (new lessons from this movement, appended by actors), `cycles/cNN/` (reports, render, metrics, CHANGES.md, mp3). Cycle 0 is the first mockup.
- Movement II's work folder `symphony/mvt2/reaper/` is a reference (its `loop/HISTORY.md`, `cycles/*/CHANGES.md`, `build/*.json`); never write into it.

## Facts already established (details and numbers in mockup-kit/LEARNINGS.md)

- HO: CC11 crossfades the dynamic layers and sets volume; CC1 crossfades a non-vibrato and a vibrato layer in the woodwind KS Masters (not a depth control; do not hold it at 55-76). Make balance corrections in the volume envelope so CC11 keeps each printed dynamic's timbre.
- Legato patches are monophonic; transitions need overlap; legato targets start early by measured per-family leads; a same-pitch re-attack on Leg Slur MAX plays the slow first-note layer.
- KS Masters load only some rows; `build_reaper.py` loads the rows a track uses and unloads the rest. The Solo Trumpet KS Master has "Sus Non Vib MAX" / "Sus Vib MAX" instead of "Sus MAX" (`KS_ALIASES`).
- Percussion (`build_perc_track`): tam-tam on `32in Med Tam Tam` (key 36), suspended cymbal on `18in Zildjian Sus Cymbal Cres` (recorded crescendo rolls, keys 60/62/64/65 by length), crash on `19in Zildjian A Crash` (key 60). Velocity is the dynamic. The suspended-cymbal crescendo sample's peak must meet the crash at qn 636 (`PERC_MAP` `lead_s`).
- A silent 3 qn pre-roll carries each track's first keyswitch and CC values and the CC36 round-robin reset; `render_cycle.py` cuts it off, so the rendered files are on score time.

## Rules

- Only the actor drives REAPER. Critics never run `rpr.py`, never touch the bridge folder, never write into the `.rpp`, and never start renders. Critics may run their own analysis scripts on the rendered files (`~/.venvs/claude-composes-reaper/bin/python` has numpy, soundfile, mido; also ffmpeg, lilypond).
- Never edit the score or anything in `symphony/mvt1/v221/`, `symphony/mvt2/`, `symphony/render/`, `mockup-kit/`. Never commit or push. Never delete files outside your own cycle folder and your own scratch folder.
- Do not install software (no pip, brew or downloads). No GUI or computer use; REAPER is driven only through the bridge.
- Everything that changes the result lives in scripts or config files under `symphony/mvt1/reaper/` (tools, `build/score_config.py`, `build/*.json`), so the project can be rebuilt from scratch. A setting made only inside REAPER is lost when a track is rebuilt.
- The printed notes, dynamics, articulations and tempos are the reference. A rendering must not contradict them. Small liberties that real players take (shaping inside a hairpin, a slight swell on a long note, breath before a breath mark, a little rubato inside a printed rit.) are allowed if the score supports them.
- One render per cycle, from a freshly restarted REAPER; fix level-only problems on the stems afterwards (LEARNINGS section 15) instead of rendering twice.
- Keep scratch under 2 GB per agent, in `/private/tmp/claude-501/mockup-loop/mvt1-<your label>/`, and delete your scratch folder when you finish (by c22 old scratch had grown to 96 GB and filled the disk). Before rendering, check `df -h /System/Volumes/Data`: at least 30 GB must be free. Stem fixes keep copies only of the stems they replace.
