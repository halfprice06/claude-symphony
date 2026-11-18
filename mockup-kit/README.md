# Mockup kit: orchestral mockups in REAPER with EastWest Hollywood Orchestra (Opus)

Tools, method and learnings for turning a LilyPond score from this repo into a REAPER mockup played by Hollywood Orchestra Opus Edition, built and improved by Claude without using the REAPER GUI. It comes from the movement II mockup (`symphony/mvt2/reaper/`, 27 rendered cycles c00-c26) and the movement I mockup (`symphony/mvt1/reaper/`, 31 rendered cycles c00-c30; this kit holds its final tools). Neither work folder is committed: the projects, renders and generated plugin states stay local.

Read `LEARNINGS.md` before starting, beginning with "What a listener noticed that measurement missed". It records what was measured about Opus, the HO patches, REAPER and the bridge, and where `guides/reaper-claude-scripting-guide.md` is wrong for this library (patch loading is scriptable; in HO CC11 crossfades the dynamic layers, and CC1 crossfades a non-vibrato and a vibrato layer).

## Contents

- `bridge/install_bridge.py`: installs the file bridge from the scripting guide (`~/.rpr-bridge`, the REAPER runner, `__startup.lua`).
- `opus/opus_state.py`: reads `.oib` patch files and builds Opus plugin states, so a script can load any HO patch into a track (`TrackFX_SetNamedConfigParm(tr, fx, "vst_chunk", state)`). `opus/dump_ks.py` reads a patch's keyswitch map and controllers; `opus/ks_maps.json` and `ks_maps_extra.json` have the maps of the patches used.
- `pipeline/`: the reference pipeline (movement II's, generalised in movement I). Movement-specific tables live in a per-score `build/score_config.py` that `score_to_parts.py` runs after its generic defaults; `example-config/` (movement II) and `example-config-mvt1/` hold complete configs (`score_config.py`, `mix.json`, `probe.json`; mvt1 also its `mockup.ly`). New tools from movement I: `fit_rebows.py` (a level shape per re-bow, from a render), `space_rebows.py` (sections' re-bows at least 0.6 s apart), `fit_loops.py` (periodic loop profiles on long notes), `stem_fix.py` (exact level-only fixes on the stems), `rendermap.py` (file time of a score qn in renders made with a shifted tempo map). `mockup.ly` (one staff per player plus a DrumStaff, here with movement I's staves; dumps MIDI plus an event list of every articulation, text, dynamic, hairpin, slur and tremolo), `score_to_parts.py` (score data to notes, keyswitches, CC lanes and volume envelopes per track), `build_reaper.py` (tracks, patches with unused rows unloaded, mix, envelopes, tempo map into REAPER; `--midi-only` and `--mix-only` for cheaper updates), `render_cycle.py` (save, wait for samples, render master + stems at 1x, attack probe, measure, delivery mp3), `deliver_master.py` (the headphone delivery master), `measure.py`, `probe_attacks.py`, `motion.py` (loudness-motion figures), `auto_fills.py` (legato-sag fills from the previous render). `example-config/` holds the movement II mix, role, trim, lead, fill and loop-profile files.
- `loop/`: the actor-critic method: `BRIEF-mvt2-example.md` and `BRIEF-mvt1-example.md` (the briefs every agent read, with Dan's listening notes), `DYNAMICS-RESEARCH.md` (delivery targets), and movement I's `critic_prompt.md`, `actor_prompt.md` and `workflow.js` (three critics in parallel per cycle, then one actor who edits, rebuilds, restarts REAPER and renders; run one cycle per workflow call with args {start, end, prev}). Replace the work-folder paths in them for a new score.
- `sync_from_work.sh <work folder> [name]`: copies a work folder's tools (and with a name, its config) into the kit.

## Movement I series 2 and sharing REAPER (2026-11-06)

- `loop/mvt1-series2/`: the current loop documents of Movement I series 2 (score v621, cycles c31 on): BRIEF.md (with Dan's listening notes S1-S3: separate repeated notes, attack centres on the beat, subitos that keep the hall), LEARNINGS.md, HISTORY.md, MANUAL-GAPS.md (library features not yet used, ranked), MANUAL-READING.md (a manual chapter per critic per cycle), and the critic and actor prompts. They are a snapshot of the git-excluded work folder `symphony/mvt1/reaper-v621/loop/`; the work folder is newer while the loop runs.
- `pipeline/` is synced from that work folder (`sync_from_work.sh symphony/mvt1/reaper-v621 mvt1-v621`); `pipeline/example-config-mvt1-v621/` holds its score config, and `pipeline/reaper_ctl.py` drives REAPER for one work folder (set OWNER).
- Library reference: `guides/eastwest-hollywood-orchestra/DIGEST.md` (per-instrument digest of the HO manuals with page numbers) and the May 2021 manual in `text/`.
- Two threads share one REAPER on this Mac (only one 46 GB project fits). `bridge/reaper_lock.py` (installed in `~/.rpr-bridge/`) holds `~/.rpr-bridge/REAPER.lock` for one owner and work folder; `bridge/rpr.py` refuses jobs without the lock or from outside the holder's folder. Lock before starting REAPER (`reaper_ctl.py lock`), quit REAPER, then unlock. Never break the other thread's lock.

## Starting a new mockup

These are the lessons that cost the most cycles to learn. Do them from the first build.

1. **Unload unused articulation rows** (`UNLOAD_UNUSED_ROWS` in `build_reaper.py`). It cut a 32-track project from 61 GB to 43 GB with no change in sound; before that, renders ended with under 1 GB free on a 96 GB Mac.
2. **Render at 1x offline** (`RENDER_1X 1` in the `.rpp`; it cannot be set by API) with a silent pre-roll bar that carries each track's first keyswitch, first CC values and the CC36 round-robin reset (CC69 = 0 on strings). Full-speed renders start notes up to 0.6 s late.
3. **Restart REAPER before every render and quit it after.** Save, quit, start with `-new`, open the project with `Main_openProject("noprompt:...")`, wait until memory is flat, render once, save and quit. Fix level-only problems on the stems afterwards instead of rendering twice.
4. **Deliver through `deliver_master.py`.** An unprocessed orchestral master has a 20-24 LU loudness range, which is unusable on headphones; target 14-16 LU delivered, with soft levels also raised in the mix.
5. **Find each patch's dynamic-layer controller in the `.oib`.** CC11 crossfades the layers in the string and most woodwind KS Masters (there CC1 is only the vibrato layer: do not hold it inside the non-vib/vib crossfade, about 55-76); in the Hollywood Brass KS Masters and the Clarinet KS Master CC1 crossfades the layers (`CC1_DYN_TRACKS`). Make balance corrections in the volume envelope so the printed dynamic keeps its timbre.
6. **Read keyswitch maps and CC11 layer tables from the `.oib` files** (`dump_ks.py`), never from screenshots or memory. A keyswitch to an unloaded row is ignored, and soft swells near a layer boundary jump 8-11 dB.
7. **Use the true-stereo hall** (HO's `S. Cal Hall Perc TS FR 3.3s` IR with `trueStereo: true`, one shared insert copied into every patch, depth set by send level) at `reverb.fx_volume` 0.095 (Dan, 2026-11-07: "too wet" and "a bit mushy" at 0.19; the hall return is linear amplitude, so 0.095 is -6 dB), with the hall input filtered: `low_cut_hz` 160 and `high_cut_hz` 5500. Shorten the IR with Opus's IR envelope, `reverb.ir_setup` `{"envelopeMode": 2, "endPos": 0.5, "decayLength": 0.5}` (Movement I c44; Opus manual p.133-134; the 3.3 s IR otherwise runs about 2.5 s against 1.1-1.6 s in real recordings). Once the hall is this dry, drop any side-only low cuts (they narrowed the image) and widen the Main mic pair with `width_by_mic` (`build_reaper.py apply_mix`): `{"Main": 0.35}` on wind and brass groups, `{"Main": 0.45}` on celli and basses; Close keeps the track width and the seat (Movement I c45: master correlation below 250 Hz 0.78 -> 0.57, side/mid -7.3 -> -6.3 dB, references -4.7..-5.4).
11. **Cap the sustain releases** (`sus_release_cap_ms` per track in `mix.json`; one spec or a list of specs applied in turn): strings 150 ms at mf / f / ff and at least 350 ms at pp / p on Sus MAX and Sus Marc LITE (the patches ship 323-931 ms), horns 237 ms at pp / mf / f on Sus MAX and LegRep RRx4 (the patches' own ff value). Without a cap every loud note rings into the next and running figures blur. 150 ms at every dynamic (Movement I c44) made soft endings stop: the final ppp chord fell 10 dB in 0.07 s, against 0.20-0.40 s in recordings. 350 ms at pp / p (Movement I c46) gave the master's final chord 0.12 s to -10 dB and 0.33 s to -20 dB, still short of the references (Brahms 1/ii 0.40 / 0.79 s, Brahms 4/ii 0.20 / 0.48 s); Movement II c41 used 300 / 400 ms and measured 0.21 / 0.34 s at soft phrase ends. Movement I c47 tested no cap at pp (keeping 350 ms at p and 150 ms at mf-ff) on Violins II, violas, celli and basses: the final chord fell -10 dB in 0.21 s and -20 dB in 0.61 s, inside the reference range, and the old pitch at pp chord changes lingered no longer on the upper strings. The basses got worse (old pitch within 10 dB at +0.35 s on 6 changes instead of 1), so check bass chord changes. A 700 ms pp cap was rejected: the basses' test had 8-11 dB level steps at four re-bows. Adopted in Movement I: no cap at pp, 350 ms at p, 150 ms at mf-ff. mf-ff endings and levels did not change in either test. A pp-only horn cap does little: soft horns play CC1 18-42, which is mostly the mf layer (1FH layers at CC1 0 / 50 / 82 / 118). Refit the re-bow fills after any release change (`fit_rebows.py`). The release-trail samples are a separate one-shot layer that the cap does not touch; `rt_gain_db` scales them. Movement I c46, with matched test data: -6 dB passes on the violas (shorter early tail, no more legato dips) and fails on Violins II and Horn 1 (legato joins dipping 5 dB or more rose from 26 to 43 and from 1 to 8). Test it per section.
12. **Re-attack repeated string notes** that are not under one slur, or carry a tenuto, or are loud: a fresh Sus MAX stroke after a gap of min(0.06 s, 25% of the note). Merging them into one note with a CC11 notch makes them inaudible (Dan, 2026-11-07). Code: Movement I's `STR_REP_NEW_BOW` in `symphony/mvt1/reaper-v621/tools/score_to_parts.py` (not yet in this kit's copy).
8. **Re-bow long held string notes.** Split any note over about 4.5 s into same-pitch Sus MAX pieces at staggered times per section, and fit a level shape for each re-bow. One sample held for 15-25 s pulses with its 3.95 s loop.
9. **Give the pre-roll bar its own meter** (3/4 for the 3 qn pre-roll; `build_reaper.py` does this and stops if any tempo marker lands off its qn). With the score's 4/4 there, everything played 1/6 qn early (LEARNINGS section 11).
10. **Keep accents gentle.** Plain Sus MAX at moderate velocity, CC11 at the printed dynamic, and a short volume swell (full at +0.07 s, gone by +0.6 s) of about +3-6 dB; check 2-5 kHz attack energy against the body as well as level. Accent samples and CC11 bumps into the top layer sound harsh.

Then, as in movement II:

1. Install the bridge (`python3 mockup-kit/bridge/install_bridge.py`), start REAPER, check `python3 ~/.rpr-bridge/rpr.py status`. Copy `opus/*` to `~/.rpr-bridge/libs/ew_ho/`.
2. Make a work folder next to the score (keep it out of git). Copy `pipeline/mockup.ly` and point its includes and `\pl` staff list at the new score's part variables. Run LilyPond (convert-ly first if the score is older than your LilyPond).
3. Write `build/score_config.py` from an example config: `TRACKS` (track name, source staves, `.oib` patch, family, seat), `SCORE_END`, `SCORE_TITLE`, `RAMP_SPANS` for the printed rit./accel. steps, `PERC_MAP` for unpitched percussion, and `build/probe.json` (attack-probe checks). Keep the per-onset tables empty. Dump keyswitch maps for new patches and check every track's pitch range against its patch's keyswitch keys and sample range.
4. Start the per-note config files empty (`note_trims`, `pitch_trims`, `leg_leads`, `entry_leads`, `early_fills`, `loop_profiles`, `rebow_fills`, `roles`): they are keyed to a score's onsets. Keep `mix.json` (mics, hall, seats, EQ) as a starting point.
5. Generate `parts.json`, build with `build_reaper.py`, restart REAPER, then `render_cycle.py 0`. Ask a person to listen early and often; then run improvement cycles with the `loop/` prompts and `workflow.js`, adapting the brief to the new score.

`LEARNINGS.md` section 19 lists what movement II left open; section 20 adds movement I's lessons.

**State flips after a MIDI-only build (Movement I c42-c47).** A legato instance (Trumpet 1, Horn 3, Horn 1) can come back from a `--midi-only` build in a different state: +4.5 to +6.4 dB and 30-65 ms early on slurred phrases, with unchanged data. A full rebuild of that track restores it. `pipeline/state_check.py` compares every note whose data did not change with the previous render's stems and lists the steps; `render_cycle.py` runs it after each render. Brass "Marc Sus LITE" at velocity 45-75 failed (attack heard 100-365 ms late, no brighter, smaller accent step); strings "Sus Marc LITE" on cello strokes removed a 64-124 ms swell-in.

**Timpani ring through a general pause (scherzo c04).** The timpani, not the hall, held the late decay at the G.P. (master late T60 about 3.3 s). A generic `TIMP_DAMP_AT` option in the scherzo pipeline (a pre-hall CC7 fall after the last stroke before the rest) took the ring at +0.3 s from -43.8 to -71 dB. See symphony/scherzo/reaper-v600 for the code.

**EastWest's own HO REAPER template (Templates 2, "Midi Included", decoded 2026-11-08): adopted as the default for all four movements (Dan, 2026-11-08: "take every bit of this").** Full findings: `EW-TEMPLATE-FINDINGS.md`; the adoption plan and exact values: `EW-TEMPLATE-PLAN.md` (Movement I does the mix in c50 and the performance data in c51 and will post the tool changes here). Critics still measure each item. Summary:
1. Strings and brass: Close mic 4-10 dB under Main, Close panned to the seat, Main at full width and never re-panned. (Our groups narrow Main to width 0.35, which the c49 critic measured as a narrower image than every reference.)
2. Winds: Close-dominant (Close 0 dB, Main -3 to -21 dB). Ours are Main-dominant (Close 0.5 / Main 0.8).
3. Opus reverb off; one Spaces II return per family (S. Cal Hall Strings / Brass, 3.3 s, 19.6 ms pre-delay), fed from section buses at -5.6 to -8.8 dB. Each return: HPF 90-100 Hz, -5 to -7 dB dip at 2.5 kHz, LPF 5.6-8.5 kHz before the IR.
4. Section-bus EQ: cuts at 450 Hz and 0.8-1 kHz of 2-8 dB, +4 dB shelf above 5-7 kHz.
5. CC1 only (no CC11), 7-13 points/s. Legato velocity median about 95, legato overlap 45-80 ms, repeated-note gaps 20-60 ms.
Movement II c44 is testing a closer mic mix (point 1); Movement I c49 may test point 1 in pass 2. The Spaces II returns need the IR state chunks from the research thread.

**Render only after the samples have finished loading (finale c05).** render_cycle's 30 GB memory check passed while Opus was still loading samples, and the strings rendered 30-60 ms late. Wait until REAPER's memory has settled (Movement I settles at about 44 GB for the main pass) before rendering; a fixed threshold is not enough.

**First render with the EW template mix (finale c06, 2026-11-08).** Tools in symphony/mvt3/reaper-v600/tools/build_reaper.py, verified in REAPER by read-back:
- pan_by_mic and track_pan;
- Opus hall off (sends 0, fx:0 0, ConvolutionReverb removed);
- four returns with the template FX chains pasted verbatim (pre-delays, Horns IR and full IR read back correctly);
- post-fader sends;
- family EQ as a second ReaEQ named "FAMILY EQ" that set_eq skips;
- deliver_master applying the template master EQ.
Movement I has equivalent tools, offline-tested, behind new mix.json keys (symphony/mvt1/reaper-v621/tools/template_mix.py, return_stems.py; tools_next/TEMPLATE-TOOLS.md).

Measured:
- Brass needs about +4 to +6 dB make-up after the family EQ.
- The mix comes out bright: the 6-20 kHz share is -25 dB against -29 to -32 in the references, so the +4-5 dB family shelves may need halving.
- Tutti stops take 0.62-0.73 s to fall 20 dB (0.41-0.50 with the Opus hall), because the full IRs are long; lowering the return levels barely shortens them. The Duc hall (2.3 s) is the fallback.

**Template checks before the first build (Movement I c50 critic B, 2026-11-08; simulated on c49's dry stems, report symphony/mvt1/reaper-v621/cycles/c50/reports/B.md).**
- Timpani: the template's +8.6 dB bell at 84 Hz plus its Surround mic at 0 dB conflicts with Dan's rule that timpani rolls must not drown parts. The EQ alone took the timpani's share of 30-150 Hz from 13 % to 31 % over a 14-bar roll. Keep the previous timpani mics (no Surround) and use the finale's reduced timpani EQ.
- Brass: the brass family EQ removes 6-9 dB (K-weighted) against 1.3-1.9 dB on strings; make-up +5 to +6.5 dB, with soft and loud trims re-fitted per instrument.
- Winds about 1.5-2 dB hot (Close-led), tam-tam and cymbals about 3 dB hot (no family EQ), harp HPF 183 Hz cuts a third of its fundamentals (use 80 Hz).
- Wetness (scherzo c06): the template return levels made the render wetter than the previous cycle, against Dan's "too wet" note (BRIEF S4). Measure against the previous cycle before accepting them.

**Template wetness and width, three movements agree (finale c07, Movement II c44, scherzo c06; 2026-11-08).** The template returns as shipped make every family wetter than the old Opus hall (finale tutti stops 0.41-0.50 s to fall 20 dB became 0.62-0.73 s; Movement II strings 0.52 to 0.72 s, final chord 0.45 to 0.83 s). Lowering return levels barely helps and Duc's 2.3 s hall did no better (0.50-0.62 s). What worked in both the finale and Movement II:
- the Spaces II IR envelope on each return: `irSetup` envelopeMode 2, endPos 0.5, decayLength 0.5;
- no hall sends from the low instruments (low brass, bassoons, contrabassoon, basses);
- lower return faders (Movement II: strings -18, winds -4, brass -2, perc -3 dB; finale: returns 12.5 dB under the dry sum).
Results: finale median 0.41 s and RT60 1.22 s (from about 2.3 s); Movement II strings 0.55, winds 0.35, brass 0.34, final chord 0.44 s, level with its pre-template cycle. Limit in every BRIEF: no wetter than the pre-template cycle.
Still open: the 6-20 kHz share runs -30 to -25 dB against -29 to -32 in the references (halve the strings and brass family shelves; the finale did), and the full-width Main pairs make the bass image too wide (correlation below 250 Hz down to 0.06-0.33, side/mid up to -2.2 dB, against 0.54-0.62 and about -5 dB; Movement II c44 and Movement I c49 both measured it). Next to try: a side-only low cut or a narrower Main below 250 Hz.

**Movement I c50, the template mix in a fourth movement (2026-11-08; symphony/mvt1/reaper-v621/cycles/c50/CHANGES.md).**
- Short range renders before the full render (`cycles/c50/actor_scripts/rangetest50.py`) caught the two template problems early: as written, the bass image was anti-phase (correlation below 250 Hz -0.23 against 0.43 in c49 over the same seconds; 250 Hz-5 kHz 0.29 against 0.61) and the hall so wet that the cut-off detector found no tutti stops.
- Width fix that met the references: Main mics panned to the seat at ±0.8 instead of full width, plus a side-only 200 Hz -6 dB shelf on strings, brass, timpani and harp. Result: correlation below 250 Hz 0.584, 250 Hz-5 kHz 0.483, side/mid -4.71 dB (references 0.54-0.62, 0.47-0.56, -4.7 to -5.4).
- Wetness fix: the IR envelope (0.5 / 0.5), register sends, a 160 Hz high-pass on the strings return, a 2.3 kHz low-pass after Spaces II, and return faders 8 / 12 / 4 / 4 dB under the template (strings, brass, winds, percussion). Tutti stops fall 20 dB in 0.49-0.51 s (c49 0.44-0.55), drop at +0.3 s 15.7-20.3 dB, late slope 1.84 s. Returns end up 13.7 dB under the dry stems. Still open: the 60-250 Hz share of the tails rose more than 2 dB at 3 of 8 stops.
- Brightness: strings family shelf off, brass shelf +1 dB, Violins I 5 kHz shelf -6 dB, Violins II 5 kHz shelf -4 dB gave a 6-20 kHz share of -27.8 dB (references -28.8 to -32.3). Movement II's c45 critics simulated the same set at -28.1.
- Balance: brass make-up worked out at about +5 to +6.5 dB as predicted. Winds needed +0.5 to +2.5 dB more than critic B's estimate (measured per track against the previous render of the same notes, `kres50.py`). Loudness and climax order were unchanged within 0.2 dB.
- `stem_fix.py --return-gain` adjusts a return stem; `template_mix.py` writes Spaces II's `envelopeMode` as an integer.

**Movement I c51, articulation rules and brass tone (2026-11-09; symphony/mvt1/reaper-v621/cycles/c51/CHANGES.md).**
- Brass tone: bells at 475 Hz -2.7 dB and 821 Hz -3.9 dB plus a 3.2 kHz -3 dB bell moved the climax centroids down 64-114 Hz (bars 121-126: 1240 to 1126 Hz). Movement II's render with the same bells went from 929 to 887 Hz.
- Phrase shapes in score_to_parts.py (rise over the first 0.8 s, taper into the phrase end) work on brass (rise +2.7 dB, taper +4.5 dB on the dry stems). Winds needed the offsets ×1.4 and still rise only +1.1 dB.
- Re-fit soft brass levels on the whole movement, not on a range test. The range test's "+3.7 dB at pp" came from two Lento trombone windows; over the full render brass at pp-mf moved -2.0 to +3.4 dB per part and dynamic, and each was corrected separately.
- String repeated-note gaps (0.08 s, frac 0.35, minimum 0.06 s) separate repeated notes on the stems (dips 2.3-4.7 dB became 5.1-9.0 dB) but not in the master for violins and violas (1.0-2.8 dB), because the other parts and the hall returns fill a gap that short. They did fix the basses' weak downbeats (11 of 12 pass, c50 0 of 12), which swapping to a pedal layer could not.
- Celli tremolo strokes at 55 % doubled the stem's peak-to-trough (5.2 to 10.0 dB) but left the master's 100-800 Hz band unchanged. Give the tremolo part +3.7 dB to hold the bar level.
- A new held diminuendo can raise an inner held note under a tune: Horn 3's Bb3 under the Horns a2 tune came out 4-6.6 dB louder and needed -4 dB over those bars. Check the inner parts after any change to held-note dynamics.
- Unchanged: loudness -19.8 LUFS, LRA 14.6, climax order, tutti stops 0.46-0.50 s, width and the 6-20 kHz share within the references.

**Finale techniques for every movement (finale c07-c09, 2026-11-09).** The finale keeps a list of twelve techniques with exact settings and measured results in `symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md` and updates it after each cycle. New beyond the items above: the sf spike written at the moved note-on (a crescendo on the same onset had overwritten it), a "drop" phrase type and HELD_DECRESC_CARRY for subito piano, a side-only 60 Hz -3 dB shelf plus 180 Hz -5.5 dB bell for low-end width, `track_width` for narrow brass, 315 Hz cuts on horns and violas, FINAL_RING on the last chord, CC16 round-robin resets before ostinatos, harp velocity capped at 123 (124 and up triggers the Nail Pick layer), and the tilt jump instead of the 2-5 kHz jump for brass accents.

**Stale legato state after `--midi-only` builds (scherzo c09, 2026-11-09).** After an Opus instance has played, the saved project keeps 52 legato sustain-group envelope attacks at 20 ms instead of 841-1501 ms. A `--midi-only` build reloads that state, so loud legato joins come about 85 ms early. A full track rebuild fixes it. Details in `symphony/scherzo/reaper-v600/loop/LEARNINGS.md`.

**Finale c10 additions (items 13-17 of `symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md`).** A short post-fader bump at a string sf (+3 dB violins and violas, +5 dB celli and basses, 0.35 qn) restores the sf of an sfp. Two players on one line need separate join leads. Never end a delivery ride trim inside a printed crescendo. The LilyPond event dump needs a multi-measure-text-event listener for text on full-bar rests. Repeat gaps on doubled bass eighths do not deepen the master's repeat dips, as Movement I c51 also found.

**Movement I c52, stale-state guard and the finale's techniques in a second movement (2026-11-09; symphony/mvt1/reaper-v621/cycles/c52/CHANGES.md).**
- `tools/state_guard.py` decodes every Opus block of a saved project and compares each legato group's envelope attack with the written state. On the c51 project it found five stale tracks (Horn 1, Horn 3, Trumpet 1, Trumpet 2, pass-2 Bassoon 1 stac). `build_reaper.py --midi-only` now fully rebuilds every stale track and `render_cycle.py` refuses a stale project. Legato joins went from 18-45 ms early back to within -8..+1 ms of c50. Soft trims fitted on the stale audio in c51 had to be reverted, so never fit levels on a render whose guard has not passed.
- `state_check.py` must remove EQ changes before it compares two renders (`tools/eqresp.py`), or every EQ edit shows up as a state run. It does not model the level loss of track width.
- The "drop" phrase type with the 6-CC rule made 283 spans on 33 tracks, many 16-64 qn long, which would have removed most phrase arches. Restricted to printed subito marks it makes 16 spans, and the bar-62 subito passes.
- REAPER's track width costs level: trumpets at width 0.5 lose 2.2-2.8 dB, trombones at 0.6 lose 1.0-1.9 dB (range test repeatable to 0.00 dB). Measured make-up gains of +1.3 to +2.8 dB put every stem within ±0.28 dB.
- The side EQ (60 Hz -3 dB shelf, 180 Hz -4.5 dB bell) and the brass widths were each predicted inside the references alone; together they land just past the edges (250 Hz-5 kHz correlation 0.566 against 0.56, side/mid -5.53 dB against -5.4). Simulate width changes together, not one at a time.
- Low winds whose phrase swell is clamped by a CC cap: put the clamped part into the volume envelope (`SWELL_CAP_TO_VOL_DB_PER_CC`, 0.20-0.32 dB per CC unit, peaks 2.2-3.6 dB). Their stems then arch 8-14 dB.
- Phrase shape over short hairpins: inside a crescendo shorter than 4 qn, do not let the phrase offset fall below its value at the hairpin start (`hp_hold_cresc`). Reversed crescendos on the dolce lanes went from 13 to 2.
- sf with a legato lead: write the spike at the moved note-on so the led note starts on the ff layer. The first 0.1 s is then within 1.1-2.3 dB of the peak. A stroke-row note needs to count as a new bow, or the next same-pitch note becomes a legato join.
- The template's CC1 vibrato macro on the celli is not shown to hurt legato joins. The c52 count (8 of 147 joins dipping 2 dB or more deeper, against 3 of 71 on violas without it) was re-measured in c53 with controls: 6 of 261 celli joins (2.3 %) against 2.9 % and 3.2 % on two tracks without the macro. Movement I keeps the macro. Compare a join count against control tracks before removing a template feature.
- A render refused because REAPER had closed its audio device was fixed by `reaper.Audio_Init()` from a script.

**Finale c11 additions (items 18-23 of `symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md`).** Measure repeated low-string eighths at the fundamental (30-120 Hz) and dip the volume only in the played gap before each beat. The post-fader sf bump also works on winds and brass. Add a negative per-onset legato lead to the total lead before the clamp. A tenuto repeat inside a slur and one that starts a new slur need different gaps (0.06 s and 0.12 s). Note trims ramp in over 0.6 s and barely act on eighths. Hold a delivery ride at 0 through a subito bar and ramp it in over about 10 qn.

**Finale c12 additions (items 24-33 of `symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md`).** A same-pitch string repeat that must take a new bow at p or pp needs a volume notch inside the data gap as well as the gap itself, because the release tail fills 74-90 ms ((-0.085 s, 0), (-0.060, g), (-0.015, g), (0, 0) before the note-on; g = -8 dB gave a 10.1 dB dip; level-only, so it can go in by stem fix). Detached f-ff cello repeats: detach dip -10 dB over 0.10 s. A late sfp peak in a tutti: notch the stems that keep rising (horns, trombones, tuba, -3 to -5 dB at 0.11-0.40 s after the mark) and add the +3 dB front on the low brass. Measure slurred joins on a sustain row per pitch (harmonics 2-7 of the old and new pitch), not by wide-band RMS; on Solo Trumpet "Mute Sus" keep overlaps at 0-10 ms. A pre-render simulation (`stem_fix.py --out` on the last stems, then `deliver_master.py`) predicts each bar within -0.30 / +0.21 dB for envelope-only changes. A drift check on unchanged data with a clean state guard shows medians of 0.00 dB per track but single notes moving 2-6.7 dB on 12 of 31 tracks, so a single-note difference of that size is normal variation, not stale state. After adding a phrase arc, rebuild every track with `--midi-only --tempo` and rename the keys of seconds-spaced fits. A delivery ride over a soft passage should rise linearly across it, so a printed morendo keeps falling. HO Basses need pitch trims (E2 +6, F2 / E flat 2 / F1 +3 dB). Removing a 167 Hz -1.6 dB delivery bell raised the limiter figure from 1.6 to 2.6 dB, so re-check the limiter after any change to a low-mid delivery cut.

**State guard, second movement results (2026-11-09).** The scherzo's c11 project read 0 stale tracks after a full build and 5 in the project saved after the render; the finale's c12 project read 0 at three checks. Run the guard before the render and again on the post-render save.

## Movement I c53 results (2026-11-09)

- **State guard after every render.** The legato attack value is a runtime value of the Opus instance; a save made after playback stops can store a stale 20 ms value. The render that preceded the save is unaffected; the next load is. Run `state_guard.py` before the render and on the post-render save, and rebuild stale tracks in full.
- **Wait about 45 s** after a REAPER restart, a full rebuild or creating a track before rendering. A range render 10 s after a rebuild was off by up to 90 ms and 4 dB. Run the audio-init script after a restart.
- **Range renders.** Prime the governing keyswitch. Never render into a folder that already holds files (the overwrite dialog hangs REAPER). Do not fit a row on a range render where the keyswitch changes between overlapping notes; a lead fitted that way (cor anglais, +158 ms late) came out 84 ms early in the full render.
- **Delivery EQ variants** are compared on one master, including limiter reduction and stop decays. A bell near 167 Hz changes the stop decays; a 3 kHz shelf of -1.3 dB restored the 2-6 kHz share after a 260 Hz cut.
- **Return-level changes** are tested by substituting the previous cycle's return stem into the sum before a re-render.
- **Staccato per-pitch level shapes** go on the alias track only, as steps ending 0.01-0.04 qn before each onset (`ALIAS_TRACKS[alias]["tables"]`), not a table row keyed by alias name. Spread fell from 10-14 dB to under 3 dB.
- **Trims on short notes** need `NOTE_TRIM_RAMP_S` 0.1.
- **Front-weighted sf bumps** are simulated on the stems before a render.
- **Onset measures.** Cross-correlation reads swelling notes early or late; check a band envelope before acting. Take score-to-seconds from parts.json, not from a map rebuilt from printed tempos (a critic's own map produced a false 0.3-0.45 s lateness).
- **Release-trail gain** (`rt_gain_db`) acts only from 0.3 s after the note end.
- **`stem_fix.py --apply`** runs once only; the return stems are not re-simulated, so wet/dry ratios on corrected stems are off by the correction.

## Steady rhythm in fast string themes (Movement I c54, Movement II c51-c52, 2026-11-10)

Dan heard the Movement I first theme (bars 15-23, eighths at 126) as choppy and not in steady time. Measured cause and cure:
- **Measure with S** (the earlier of pcX and a robust band crossover; `symphony/mvt2/reaper-v600/tools/s_onsets.py`, wrapper `symphony/mvt1/reaper-v621/cycles/c54/coordinator_scripts/theme_S.py`). A dominant-pitch measure reads late when the previous note's ring is louder than the new note's start.
- **Cause 1: row changes inside a line.** A legato target whose patch row differs from the row of the note it overlaps takes one of two start times, a fixed shift apart (Violins I 105 ms, celli 59, violas 45-50, basses 112), about 1 time in 9, and differently on each render. The Movement I theme changed row on 53 of 108 joins.
- **Cause 2: Leg Slur MAX at fast tempo.** The transition takes 186-240 ms, so the second of two slurred eighths sounds for about 20 ms.
- **Cause 3: unprinted tempo steps** (phrase arcs, pushes, beat stretches) of 2-8 % on single beats.
- **Cure:** one row for the whole line. Movement I's rule `STEADY_LINE` (tools/score_to_parts.py) puts the theme on Sus Marc LITE with one lead per class (slurred 90 ms, after a bow change 50, entry 100, same-pitch repeat 85), per-note level steps and round-robin resets before entries. Violins I bars 15-23: robust SD 46 → 6 ms, notes over 40 ms from the median 15 → 1, row changes 53 → 2, two renders identical. Range-test variants (S SD): Sus Marc LITE 22, Sus MAX 44, Slur Runs 40, legato with one lead 57.
- Remove unprinted tempo changes in Allegro themes. Movement II removed all of them and its critic found no phrase that read as mechanical.
- After a tempo-map change: refit re-bow and join fills, keep stop lists by qn, compare renders on their own maps.
- Winds and brass: one row lead per track plus a pitch-pair table beats per-onset rows (Movement II: joins outside 25 ms 97 → 26 of 263). The STEADY_LINE rule gave no gain on wind legato rows.

## Movement I c55 results and the volume-envelope check (2026-11-11)

**Long notes on a marcato sustain row.** Moving a fast theme to one row (Sus Marc LITE) fixed timing in c54 but long notes started strong and sagged: front minus tail 9.1 dB median on the 13 notes of 1.4 quarter notes or more. Cure in c55, timing kept (S robust SD 6 → 9 ms):

- no accent shapes on notes of that row (the sample has its own attack);
- per-note body and tail lifts fitted on the stem (`build/steady_body55.json`), in place on the note-on or rising after +0.45 s, because a 3 dB rise inside the first 0.45 s shifts measure S by about +70 ms;
- long notes end at the next note-on; level steps refitted on a body window.

Result: front minus tail 0.6 dB median, long notes under 60 % of their length 13 → 1, theme over celli lower quartile +3.0 → +4.95 dB. Tested and rejected: Sus MAX for the long notes (7.9 dB sag, 8 of 39 over 40 ms), lower velocity (10.6 dB sag), longer overlaps at slurs (0.3 dB).

**Limits found.** One-row treatment is not suitable where long notes carry hairpins (the lift fit flattens the diminuendo). Lyrical cello lines: Leg Slur 71 ms spread, Sus MAX with overlap 46, Marc row 27 with a 6.4 dB sag; none is good enough yet.

**Winds.** Per-onset lead rows fitted from S, without a row-lead table, cut the spread: Clarinet 1 14 → 9 ms, Trombone 1 30 → 16, Oboe 1 37 → 16, cor anglais 18 → 8.

**Tempo.** Printed tempo on every beat of the Allegro outside marked changes; breath gaps unchanged in milliseconds.

**Queue.** Two `wait_lock.py` waiters started in the same second list each other as ahead and never take a free lock. Start waiters a few seconds apart, and keep a waiter process running for the whole wait.

### Check the per-note volume envelope

The track volume envelope (`vol_db` in parts.json, written by `tools/score_to_parts.py`, turned into points by `vol_points` in `tools/build_reaper.py`) carries every per-note correction the loops have added: accent shapes, join notches, re-bow and loop fills, pitch trims, level steps. In Movement I this reached 2,200-4,200 points per string track, 4-11 per note, with a within-note swing of 2-3 dB median, 6-9 dB at the 90th percentile and 21-24 dB at most. Dan saw it in REAPER and called it unnatural.

Test whether it helps: per note, take the stem RMS over the first 0.35 s, and the same value minus the envelope's mean over that window (valid because the envelope is a gain after the instrument). Compare the median note-to-note step.

| Line (Movement I c55) | with envelope | without |
|---|---|---|
| Violins I theme, bars 15-23 | 1.4 dB | 1.3 dB |
| Violins I bars 27-32 | 2.4 | 3.8 |
| Violins I development | 2.9 | 3.9 |
| Celli second theme | 2.7 | 2.5 |
| Oboe 1 bars 23-26 | 3.4 | 2.4 |
| Clarinet 1 bars 131-134 | 3.1 | 1.9 |

So the envelope helps in some lines, does nothing in others and harms a few. Rule from now on: a per-note envelope layer stays only where it lowers this measured step or cures a named fault; new rows need a before/after measurement; musical shape belongs on CC11, CC1 and velocity.

## Movement I c56 results: reducing the per-note volume envelope (2026-11-11)

Correction to the c55 table above: on the theme at rehearsal A the body and tail lifts are needed (long notes front
minus tail 3.8 dB with them, 9.3 dB without). The "1.4 with / 1.3 without" figure came from a window of 0.35 s from
the moved note-on and does not measure them.

What c56 did and what it measured (Movement I, 5282 notes):

- One level per onset on every track (`NOTE_LEVEL` pass): removes trims that return to 0 dB between the notes of a run
  (314 notes had them).
- Level changes and lift ends sit on the next note's score onset with a 40 ms crossfade, not on the moved note-on:
  join holes over 9 dB on Violins I 66 -> 49, theme timing kept (S robust SD 10 ms).
- Swells capped at 3 dB and refitted as residuals; fitted accents more than 5 dB over their neighbours 51 -> 20 of 273.
- Point thinning at 0.1 dB tolerance removes 38 % of the points (largest change 0.11 dB).
- Points written 52200 -> 32612; strings 9-14 points per second -> 5-10.
- Notes with 3 dB or more of movement inside fell only 2334 -> 2129; on the strings almost nothing. What still counts:
  fitted per-note level steps, kept accents and fills, repeated-note dips, body lifts, re-bow fills.

Limits found:

- Repeated-note dips are needed: separation falls from 5.5-7.3 dB to 2.1-4.8 dB without them.
- A plain +4 dB cap on final-chord re-bow fills leaves 6-10 dB holes; refit the residual instead.
- A common level for fast notes of one line can make the line less even (theme eighths 1.8 -> 2.2 dB step); test first.
- Moving a level step changes S readings by 10-20 ms with no note-on changed; do not fit timing from S after an
  envelope change without a control.
- Removing a release jump lowers melody-over-accompaniment readings that included it (theme over celli 4.95 -> 3.56);
  recheck such margins after any envelope cut.

Double basses: deleting `mute_eq` and raising the 87.3 Hz bell from -10 to -4 dB lifted the master's 70-112 Hz share
-15.0 -> -13.7 dB with no peak problem. A further 120 Hz +3 dB bell on celli and basses raised single bars by 3 dB and
was not adopted.

## Rule: the track volume envelope is for slow balance only (2026-11-11, all movements)

Dan looked at the tracks in REAPER, found a volume move on nearly every note, and heard c56 (fewer of them) as
better. None of the references does this: EastWest's own templates carry no volume automation, and the two
professional projects have 0.01-0.36 envelope points per second against our 5-14. Our loops added the per-note layers
one measured unevenness at a time, because a post-instrument gain change is cheap and leaves the sample alone.

The rule:

1. The track volume envelope carries gain, dynamic trims, roles, hairpin gain, divisi cuts and fades, drawn as ramps.
   No layer keyed to single notes.
2. A fault on single notes is fixed on the instrument side, as the references do it
   (`EW-TEMPLATE-FINDINGS.md` sections 5-8 and 12):

   | fault | reference practice |
   |---|---|
   | repeated notes run together | a note-off gap of 60-100 ms (winds about 60, strings 90, brass 100, shorts 115) |
   | unclear or bumpy legato joins | overlap 45-80 ms on strings, 33-58 ms on winds and brass; legato velocity 90 or more; the controller lane flat across the join |
   | long note sags | a row that sustains; the phrase controller shapes the note |
   | dip where a long note is re-struck | do not re-strike; hold the note, or overlap at the split |
   | one pitch or row louder than its line | velocity, or one controller value at the note-on |
   | accents | velocity or the accent row |
   | soft short notes too weak | controller parked high, dynamic by velocity alone |

3. The controller lane is shaped per phrase: flat across legato note changes, nothing before an onset, a swell after
   the first onset and a taper at the end where the phrase asks for it.
4. No exceptions (Dan, 2026-11-11: "i want to nuke all the volume adjustments per note"). If a fault cannot be fixed
   on the instrument side, it stays audible and is reported with what was tried. No per-note volume move goes back.
   Every cycle reports, per track, that the count of envelope points from per-note layers is 0.
5. Moving the same per-note bumps from the volume envelope into CC11 is not a fix; CC11 is also a level.
6. A worse median of note-to-note steps is not by itself a reason to add a layer.

## Movement I c57 results: first cycle with no per-note track volume (2026-11-11)

- Envelope items from per-note rules: 0 on every pitched track. Points 32712 -> 6962. Strings 0.9-1.35 points/s, winds and brass 0.2-0.8.
- Removing the layers alone moved single tracks 5-11 dB in single bars and put the theme 14 dB over the celli (simulated). The c57 build held this with 375 bar-length level rows fitted to the old layers' bar means. That is a stopgap: rows fitted to the old layers are the old layers at bar resolution. Check your own slow rows for the same thing. c58 moves those levels into the dynamic mapping, region and row volumes, and role rows.
- Theme timing without body lifts: Sus MAX on every theme note with class leads (slurred 80, new bow 62, after a rest 29, repeat 50 ms) read 27 ms spread; per-note leads on 103 notes (timing only) read 9 ms with no sag. Sus Marc LITE without lifts is steady (7 ms) but sags 7.5 dB over long notes.
- Same-pitch repeats: real note-off gaps of 90 / 65 / 100 ms (strings / winds / brass, at most 40 % of the slot) hold separation at the level the dips gave (82 of 406 under 3 dB; 158 with no dips and no gap). Fast bass eighths stay weak.
- Pitch trims as Opus region volumes work (basses' F2 4.0-5.8 dB lower), but a trim table fitted with the other layers in place does not hold every pitch once they are gone. Refit on the new render.
- A "drive" phrase shape on held notes made horns fall 7-12 dB over pedals. Limit the shape to phrases whose mean note length is under 2 qn.
- Cost, left audible: re-bow holes 1 -> 16 (7-16 dB, from our own split of the long note), accents without emphasis, pitches 4 dB out 18 -> 23, theme over celli lower quartile 3.56 -> 1.7 dB. Gains: join holes 44 -> 25, long-note sags 84 -> 62.
- Range renders left 4 tracks stale; run the state guard and rebuild in full before the main render.

## Movement I c58 results: fitted level rows removed (2026-11-15)

- 368 bar-length rows fitted to the old layers deleted and nothing refitted. Per-note envelope items 0. Points 6962 -> 4515; strings 0.49-0.73 points/s, winds and brass 0.18-0.55. Hairpin gain is what keeps strings above 0.4.
- Replacements that worked: role spans of a phrase or more with edges in rests or 2 s ramps; region gains refitted on the new render (pitches 4 dB out 23 -> 7); entry steps keyed to the moved note-on; spans for repeated quarters that had no lead (+220 ms late -> +9 ms); no re-bow and a lower CC11 on the last fermata chord (rise inside the chord +2.5 -> +0.5 dB).
- A CC + envelope pair breaks when the envelope half goes: SHORT_CC11_PARK left 184 string shorts up to 11 dB hot. Check every such pair when a layer is removed.
- Accents as a flat CC11 value for the note's length from a lower resting value: strings +2.6 / +1.7 dB at f / ff, winds +1.2 / +0.9, brass +0.9 / +0.5. One size does not fit all tracks (Violins I +3.3, celli -0.8); size per track. Dan found +2.1 to +4.1 dB overdone on the finale: aim +1.5 to +2, no track over +3.
- Velocity does nothing on sustain rows (0.0 dB per 10 units on winds, brass, Sus MAX, Sus Marc LITE).
- Failed: re-bow overlap on a second MIDI channel (channel 2 is silent in Opus); CC16 reset before every beat on fast bass eighths; a soft-layer region gain on Horn 4.
- Cost: passages whose shape had no instrument-side replacement yet moved 4-9 dB (a cor anglais solo, a horn solo, a solo cello). Write the phrase in CC11 in the same cycle that deletes the envelope shape.
- Scripts must not import from the temp folder: it was emptied during a four-day stop and a guard script stopped working.

## Movement I c59 results (2026-11-16)

- Accents sized per track and dynamic from each track's own CC11-to-dB curve: isolated accents median +1.7 dB (was +1.4), notes under +1 dB 61 -> 20. Measure isolated accents matched on track, pitch, row and resting CC11; report quartiles and the maximum, not only the median. Singles at +5 to +9.6 dB remain and look like sample level by pitch.
- Staff-count scaling of accents is not needed: when every track rises E dB the sum rises E dB.
- No accent value on an sf note that is already an ff arrival (they stacked to +5.2 dB).
- A solo whose level follows the sample row (15 dB between held notes at one CC11): region volumes over the row first, then one CC11 lane for the phrase. Range-render two or three lanes and pick by "printed crest is the loudest note".
- On Horn 4 the sample layer follows CC1, not CC11. A soft trim sized for one pitch's weak layer left the next pitch 12 dB hot; remapping both lanes brought it to 1.7 dB.
- A CC11 offset sized from a family slope overshoots (+8 units gave +6.5 dB on a horn). Use the track's curve and range-test.
- REBOW_NONE over a span also removes printed bow changes; unlist the automatic points instead.
- Held same-pitch repeats on strings take a 30 ms gap, not the 90 ms of detached repeats.
- Envelope thinning tolerance 0.75 dB: points 4515 -> 3951, strings 0.41-0.61 points/s.

## Shared delivery loudness target (2026-11-17, all movements)

Dan: "i have to turn the volume on my airpods to almost max to really hear all the detail and instruments especially in quiet parts, basically overall the tracks are too soft and in some places there are still instruments with interesting internal lines that are hidden behind the melody or other instruments."

The old target (-19 to -20 LUFS, LRA 14-16 LU, from the BBC classical guideline) is replaced for these mockups, which are heard on headphones:

| | old | new |
|---|---|---|
| Integrated loudness, delivered mp3 | -19.5 to -19.8 LUFS | -14 LUFS (within 0.5; Dan 2026-11-17: "-14 goal please", replacing a first -16) |
| True peak | -1.5 dBTP | -1.0 dBTP |
| Loudness range | 14-16 LU | about 12 LU |
| Quiet passages: 10th percentile of short-term loudness | about -30 LUFS | -23 LUFS or higher |
| Climax order | | the printed order holds on the delivered file (momentary maximum per bar), not only on the master |
| Limiter work | | list every passage with more than 6 dB of gain reduction (pre-limiter minus delivered peak, 50 ms windows, with the delivered signal shifted back by the limiter's 5 ms look-ahead (240 samples at 48 kHz) before subtracting; the finale's first unaligned readings of 8-10 dB were 5 dB once aligned); more than 6 dB on a sustained climax or final chord is a fault to fix with the top ride or the mix, not by lowering the target |

How Movement I does it (symphony/mvt1/reaper-v621/tools/deliver_master.py): constant gain to -14 LUFS; the existing slow lift of quiet passages with its knee 7 dB under the 95th percentile of short-term loudness (was 5); the slow top ride starting 10 dB under that percentile at 3:1 (was 3 dB at 2.5:1); limiter ceiling 0.87 (-1.2 dBFS; the finale's c19 missed -1.0 dBTP by 0.1 dB at 0.891 after mp3 encoding). At -14 on the Movement I c59 master: I -19.8 -> -14.5 LUFS, LRA 12.2 LU, TP -1.2 dBTP, p10 short-term -30.1 -> -22.8, coda -26.0 -> -17.6; the limiter takes 4-6 dB on the five highest peaks (pre-limiter peak over the ceiling, which needs no alignment: +4.9 dBFS at 378 s is 6.1 dB) (bar 160 region, 117 s, 89 s, 203 s): listen for dulled timpani and cymbal strokes there. A stronger top ride (12 dB under at 3.5:1) gave LRA 11.3 with no less limiting. At -16 it was: I -19.8 -> -16.4 LUFS, LRA 14.8 -> 12.5 LU, p10 short-term -30.1 -> -24.8, coda -26.0 -> -19.6, limiter 4.4 dB on the single loudest sample peak. Raising only the gain to -16 left LRA at 14.7 and the limiter at 4.5 dB; a higher lift ratio alone raised LRA.

Rules:
- This is the delivery stage only; the mix and the REAPER master stay as they are. No per-note volume, as before.
- The louder top ride compresses the climaxes against each other. Movement I's c59 put an ff tutti over both fff climaxes at any setting; that is fixed in the mix (dynamic trims per printed dynamic), not in the delivery.
- The finale at -14 (-14.6 LUFS): the limiter took 7.6 dB on the final chord, 5-5.8 dB at two other bars and 8-9.6 dB on single peaks, and its fff fell under several ff bars. Check the delivered file's limiter work by passage: the finale's 4.3-4.8 dB was all on the final chord. A top ride ratio of 3.0 took the finale's LRA to 11.3; read the result against 12-13 LU per movement.
- Loudness loop (adopted for all four movements; finale c21, ported to Movement I's deliver_master.py): measure the mp3's integrated loudness after the limiter and encode; if it is more than 0.1 LU under -14, raise the pre-limiter gain by the shortfall plus 0.05 dB and run the limiter again (3 passes at most). Measure true peak after the encode and lower the ceiling by any excess (2 retries). Movement I c59: -14.5 -> -14.1 LUFS in two passes, TP -1.1, LRA 12.1, limiter 6.7 dB on the loudest peak.
- Finale c21 at -14: climax peaks are tutti sums; cutting one family 3-4 dB moved the limiter only 0.1-0.7 dB, and the delivery top ride undid about two thirds of mix trims. What worked there: delivery ride rows on the climaxes and ff stabs (-2 to -4.5 dB), quiet-lift ratio 2.0 -> 1.8, and a loudness loop that sets the pre-limiter target so the mp3 lands at -14 (-13.9 LUFS, LRA 11.5, limiter 6.0 / 3.5 / 3.1 dB on the fff moments). A climax margin of 1 dB or more was not reachable at -14 with 6 dB of limiting or less: if the printed order cannot hold, report the margin and the limiter figure rather than limiting harder.
- The top-ride ratio depends on the movement: 3:1 gave Movement I LRA 12.2 but Movement II 10.6, with a pre-climax bar lifted level with the climax; 2:1 gave Movement II 12.0. Choose 2:1 to 3:1 per movement so LRA lands near 12, and check the bar before each climax.
- Change leads by half the measured error: leads sized from one measurement overshoot (Movement II).
- Final-chord decay: the quiet-passage lift raises a dying chord's tail (finale c23: a 16.1 dB drop on the master became 7.8 dB on the mp3; a -8 dB ride row over the tail restored 15.6). Measure the last chord's decay on the delivered file.
- Keep about 0.30 s of pre-roll before score qn 0 in the delivered file: cutting at qn 0 clipped the opening chord's led attacks (finale: Horn 1 +131 -> +26 ms).
- Render-to-render changes of 1-2 dB on unchanged data can be a different round-robin take (stem correlation 0.02 against 0.998 for a true repeat). Do not fit levels to such a render.
- Hidden inner lines are a balance job (roles of a phrase or more, CC11 phrase lanes, region volumes), not a delivery job.

## Movement I c60 results (2026-11-17)

- First render delivered at -14 LUFS (two loudness-loop passes): -14.0, LRA 11.2, TP -1.2 dBTP; limiter over 6 dB at one Violins I peak only.
- The delivery lift can raise a loud chord after a quiet bar above a climax on momentary loudness while bar levels stay in order (bar 170 = bar 160 at -12.2 LUFS momentary). Check momentary maxima per bar on the delivered file.
- Climax order fixed in the mix by per-dynamic trims: ff -2.5 dB on strings, -1.5 on winds and brass, fff unchanged; positive rows at an fff kept as slow role rows (the trumpets at bar 122 +2.3 to +4.3 dB) because their CC11 was already at the top.
- Sustained wind and brass chord changes: old note ends 0.03-0.04 s after the new note-on on long notes (polyphonic sustain rows), 0.025 s gap at the same pitch: the wind-and-brass dip at tutti changes 6.5-7.5 -> 1.8-3.6 dB.
- Re-listing automatic bow changes so pieces run up to 5.3 s (the loop starts near 5.9 s): re-bow holes 14 -> 8.
- Removing the timpani's per-stroke +6 dB shape (a per-note shape) left loud strokes 0.4-4.8 dB softer with velocity already 117-127; timpani points 1.28 -> 0.40 per second.
- Five more fitted rows turned up in config tables after "fitted rows 0" had been reported by rule name. Search the tables, not only the rule dump.
- render_cycle's memory gate: restart REAPER immediately before the main render, and make shell chains stop (and keep the lock) on any failure: a chain that went on after a refused render released the lock with no render made.

## Movement I c61 results: inner lines (2026-11-17)

- 71 inner lines read from the score, each measured as K-weighted level under the tune and best 1/3-octave band against everything else; 35 brought forward by phrase-length roles (+2 to +5 dB, edges in rests), tune on top in every changed span (+2 to +13.5 dB). Causes found: stale negative rows from early cycles, and a row-wide region cut meant to even one row's bumps that took a section's own counter-lines down 2.5-4.5 dB.
- A role row that ends before a chord with no rest before it fades across the chord's attack: run it to the next rest.
- A delivery ride row starting before a crescendo's printed p inverted it on the mp3; start it at the printed p.
- CC11 lane rises written on the score onset while note-ons move earlier left 55 notes starting 8-38 units under their level; moved to the moved note-on (37 left).
- After a REAPER restart the audio device can be stopped and render_cycle refuses: run an audio-init step before the render.
- Report for loops c52-c61: https://claude.ai/artifact/7eCgYEwuBJXZQF5emdM2So

## CC11 law and delivery top ride (finale c24, 2026-11-17)

- In the brass and clarinet KS Masters (1FH, 1TP, 1TB, 1TU, CL), CC11 scales sample volume linearly: dB = 20 log10(CC / ref), not 40 log10 (measured: Horn 3 CC11 46 -> 73 = +4.0 dB). An offset sized with 40 log10 on these delivers half its planned dB. Strings and other woodwinds are not checked; measure each track's own curve before sizing (as Movement I's c59 rule says).
- At -14 the top ride starting 10 dB under the 95th percentile with 3 s smoothing flattened f against ff to about 1.4 dB on the finale's mp3. Its simulated fix: top ride from 6 dB under p95, quiet-lift ratio 2.1. Check the f-to-ff step on the delivered file per movement; Movement I's c61 was not checked for it.
- Accented ff tutti on Sus MAX peak about 212 ms late (finale).

## Decision: climax margin before loudness range (2026-11-17, all movements)

At -14 LUFS no delivery setting both keeps LRA near 12 and lets the printed summit stand clear (scherzo c22, finale c24: everything loud sat within about 1 LU of the summit). Climax order and the f-to-ff step are the music; LRA is a measure. So the targets are now, in this priority:

1. Integrated -14 LUFS within 0.5, true peak -1.0 dBTP (unchanged).
2. On the delivered file, by loudest 0.4 s per bar: the printed summit leads every rival ff or fff passage by 0.5 LU or more, and the printed order of the other climaxes holds.
3. On the delivered file, a printed f -> ff step reads 2 LU or more where the score marks one.
4. Quiet passages: 10th percentile of short-term loudness -23 LUFS or higher (Dan's request; unchanged).
5. Limiter: no sustained climax or final chord over 6 dB.
6. LRA: 10.5 LU or more (was about 12). An LRA between 10.5 and 12 is accepted when it buys items 2-3.

Allowed tools to get there: top ride from 6 dB under the 95th percentile (was 10), quiet-lift ratio about 2.1, a peak compressor before the limiter (scherzo's best: -9 dB threshold, 3:1), and delivery ride rows that lower rival ff passages or the bars before an fff (not the arrival itself). Scherzo's simulated result with all of these: summit lead 0.72 LU, f-ff 2.2 LU, LRA 10.6.

Finale c24 met all six with top ride 6 dB under p95, quiet lift 2.1 and ride rows: summit +0.6 LU, f-ff +3.7 LU, LRA 11.8, limiter 5.8 dB. Woodwind and string CC11 also switches sample layers, so fit their levels per passage rather than by one law.

Movement I c61 (delivered before this decision) reads 160 > 122 by 0.2 LU, 122 > 26 by 0.3, 26 > 170 by 0.5: item 2 is met for order but not for the 0.5 LU summit lead over bar 122. Movement I is paused for Dan's room-bed decision; this is listed for a later pass, not re-rendered now.

## Required check after every build: fader slope inside notes (2026-11-18, all movements)

"0 envelope items from per-note rules" is not enough. Check the written envelope by slope: list every move of 1.5 dB or more steeper than 3 dB/s that lies inside a sounding note of that track, split into "inside a held note" and "at a new note while the previous one still sounds". Target: none inside held notes; at new notes only printed sudden dynamics (sf, fp, subito), placed 0.03 s before the moved note-on.
- Finale c26 found 30 such steps (mostly a held-decrescendo rule releasing -3 dB at the hairpin end inside the next note). Movement I c61 had 354 (137 inside held notes, 15 of them 6 dB or more outside percussion), from slow-balance rules: hairpin-gain releases, role and section-row edges, player-count marks, timpani dynamics.
- Sources to fix: release hairpin gain at 2.8 dB/s or less or at the next printed dynamic or rest; role and row edges in rests or as ramps of 2 s or more; then a generic post-pass guard after vol_points (scherzo: tools/build_reaper.py note_move_guard; finale: tools/instr_post.py).
- Measure the written lane with no skipped windows: the scherzo's guard skipped printed hairpin spans, windows around printed marks and legato overlaps, and so listed 9 of 67 offending notes.
- Tool: symphony/mvt1/reaper-v621/cycles/c61/actor_scripts/env61.py edges() measures it on any build folder (loads build_reaper.py cut before ENV_LUA, no REAPER contact).

## Room-noise bed in the delivery (Dan approved 2026-11-18, all movements)

Dan, after the audition: "The bed is fine." Every delivered mockup gets a quiet synthetic hall-air bed so rests and fades end in room hiss, not digital silence.
- Level: -60 LUFS integrated (about 46 dB under the music at -14). Added after the limiter, before the mp3 encode, so the quiet-passage lift does not raise it and make it pump.
- Noise: pink, an extra first-order fall above 2.5 kHz, a fourth-order low cut at 84 Hz (as in the Duc reference's bed), partly correlated stereo (L = 0.8 a + 0.6 c, R = 0.8 b + 0.6 c), fixed seed.
- Scherzo check: about 40 dB under its quietest music, audible only at general-pause ends and after the final note.
- It is synthetic: no free room recording is in the repo. A real recording would sound more natural if one is found.
- Movement I's tools/deliver_master.py gets it in c62 (env DELIVER_ROOM_BED_LUFS, default -60, "off" to disable); the other movements can port that function.
