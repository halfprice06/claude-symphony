# Template mix tools (mvt1 c50)

These tools let c50 adopt EastWest's own HO REAPER template mix (`loop/TEMPLATE-PLAN.md` sections 1-4 and 8; data in
`symphony/mockup-research/ew-template-2026-11-08/`). Every behaviour is off unless its `mix.json` key is present. With
the c49 `build/mix.json` the Lua jobs and Opus states are byte-identical to the c49 tools, and so are the render outputs
(see "Verified offline").

Where the files are (2026-11-08): the changed and new tools are already in `tools/` (frozen for c49 at that state, see
`tools/TOOLS_FROZEN_FOR_C49`). `tools_next/` is a copy of `tools/` holding the later edits: this file, a smaller memory
footprint for `return_stems.py fit`, two test fixes and one more test in `test_template_tools.py`, and
`c49_originals/` (the five tools as they were before the change; the work folder is not in git). After c49 has rendered,
copy `tools_next/TEMPLATE-TOOLS.md`, `return_stems.py` and `test_template_tools.py` into `tools/`.

The proposed mix is `build/mix_template50.json`: a full copy of `build/mix.json` (2026-11-08, c49 data) with the template
keys added. If c49 changes `build/mix.json` after that, regenerate it rather than copying an old file:
`python3 tools/make_template_mix.py build/mix.json build/mix_template50.json` (it never writes `build/mix.json`).
To adopt it, copy it over `build/mix.json` at the start of c50 and do a full build of both passes.

## Files

| file | what it is |
|---|---|
| `tools/build_reaper.py` | per-mic levels and pans, REAPER track pan, Opus reverb off (in `apply_mix`); the returns job, family EQ and sends (the block above `item_lua`) |
| `tools/template_mix.py` | chunk parsing (REAPER's three base64 runs), ReaEQ and Spaces II decoding / encoding, the returns-job Lua, the family-EQ and send Lua, the read-back check. `python3 tools/template_mix.py check` decodes every template chunk against `ho-mix-fx.json` |
| `tools/return_stems.py` | return stems: renumbering (91..), the pass-2 merge, and `fit` (send levels measured from a render) |
| `tools/render_cycle.py`, `measure.py`, `deliver_master.py`, `stem_fix.py` | return stems in the render and the master sum; the return section of metrics.md; the master EQ of the delivery; return stems passed through a stem fix |
| `tools/make_template_mix.py` | writes `build/mix_template50.json` from a `mix.json` (with the value sources in its docstring) |
| `tools/build_identity_check.py` | proves a build_reaper.py change leaves the build unchanged: `python3 tools/build_identity_check.py OLD_build_reaper.py` (e.g. `tools_next/c49_originals/build_reaper.py`); about 3.5 minutes |
| `tools/test_template_tools.py` | the offline tests listed below; run with the venv python (`~/.venvs/claude-composes-reaper/bin/python tools/test_template_tools.py`), about 8 minutes, about 1 GB of scratch |

## Keys

All keys below are new; absent means the c49 behaviour.

| key | level | what it does |
|---|---|---|
| `mic_db` `{mic: dB}` | group or track | the Opus mic levels in dB (0 dB = volume 1.0); the listed mics are loaded and the others unloaded (as `mics`). It wins over `mics`, except that a track's own `mics` (with no `mic_db` of its own) wins over its group's `mic_db`. `"mic_db": null` on a track falls back to `mics`. A mic the patch does not have is reported on stderr. |
| `pan_by_mic` `{mic: rule}` | group or track | `"seat"`: panLeft/panRight = seat -/+ width, pan 0 (the c05 rule; `width_by_mic` still widens); `"full"`: pan 0, panLeft -1, panRight +1 (Main, Mid, Surround in the template); `"factory"`: panLeft -1, panRight +1 with the patch's own pan knob (HO's Close pans are the template's seats: 1st Violins -0.31, Celli +0.33, horns -0.25, ...); a number: that pan knob with panLeft -1, panRight +1. An unlisted mic is `"seat"`. |
| `reaper_pan` | group or track | REAPER's track pan (D_PAN, stereo pan mode, width 1) after Opus. Set in full, MIDI-only and `--mix-only` builds. Absent: centre. |
| `opus_reverb_off` | top level; group or track overrides | every Opus reverb send level 0, the fx:0 channel volume 0, and no ConvolutionReverb in fx:0 (the shared hall is not loaded). The `reverb` block is then unused (it stays for old-layout tracks). |
| `family_eqs` `{name: [bands]}` | top level | band lists: `{"band": "highpass"|"lowpass"|"bell"|"lowshelf"|"highshelf", "hz", "db", "bw_oct"}`, at most 5, in ReaEQ slots 0-4 in list order. Or `{"chunk": "STRINGS.txt", "fx": "ReaEQ"}` to load the template's ReaEQ state itself with `vst_chunk`. |
| `family_eq` `name` | group or track | one more ReaEQ after every other FX of the track (after the per-track EQ, the wet EQs and the side shelf), set like the per-track EQ (`set_by_fmt`). `set_eq` deletes every ReaEQ on a re-run and the family EQ is added again after it, so `--midi-only` / `--mix-only` re-runs give the same chain. `null` = none. |
| `returns` `{name: def}` | top level | REAPER return tracks. `def`: `"fx"` (a list, see below), `"fader_db"`, `"pan"`, `"enabled"` (false: no sends reach it, not built), `"bypass"` (true: its FX are bypassed, so it outputs the plain sum of its sends; for the send-level check). A return is built only when some track of the pass sends to it. Order = stem numbers 91, 92, ... (at most 9). Names must differ from track names. |
| `returns.*.fx[]` | | `{"chunk": "STRING_VERB.txt", "fx": "ReaEQ"}`: an FX state verbatim from a chunk file (`fx` = a name substring or an index); `{"chunk": "PERC_VERB.txt", "fx": "Spaces", "set": {key: value}}`: Spaces II with values of its JSON replaced (any key but `class`, e.g. `impulseA`, `delay`, `irSetup`: `{"endPos": 0.8}`); `{"reaeq": [bands]}`: a ReaEQ written from a band list. |
| `return_chunks_dir` | top level | where the chunk files are (absolute, or relative to the mix.json folder). Default: the research folder's `ho-mix-chunks`. |
| `return_load` | top level | `"vst_chunk"` (default): TrackFX_AddByName + TrackFX_SetNamedConfigParm(fx, "vst_chunk", state). `"fxchain"`: the `<FXCHAIN>` block written into the return's track chunk (SetTrackStateChunk). |
| `send_profiles` `{profile: {group: {return: dB}}}` | top level | post-fader sends per group. |
| `send_profile` | top level; group or track overrides | the active profile; `null` = no sends. |
| `sends` `{return: dB}` | group or track | replaces the profile's group entry for this track. |
| `send_offset_db` | group or track | added to the track's sends: a number (all sends) or `{return: dB}`. |
| `send_row_db` `{return or "*": {KS row: dB}}` | group or track | adds the row's offset while that articulation row plays: the send gets a volume envelope (square steps, D_VOL 1) that steps at the onset of the first note of each run of a row (the row of a note is the last keyswitch at or before its moved onset). Keyed by return name, so an entry for `R Duc` does nothing under the `ew` profile. |
| `master_eq` `[bands]` | top level | deliver_master.py equalises render/00_Master.wav before the ride, the gain and the limiter (ffmpeg RBJ biquads, bandwidth in octaves as ReaEQ). The render itself is not changed. |

A parts.json `"test"` track (pass 2) sends to `"<return> test"`, a copy of the return built in the pass-2 project; its stem
goes to `cycles/cNN/test_stems/` and never into the master. So a test track can carry its own send levels or profile
without touching the real returns.

### Build order and re-runs

The returns job (`jobs/90_returns.lua`) runs after the tempo map and before the track jobs, in every mode (full,
`--midi-only`, `--mix-only`, named tracks, `--pass2`). A missing return is added at the end of the project; an existing
one keeps its place and its receives, and its FX are rebuilt. The job reads each FX's `vst_chunk` back and compares it
with what it wrote (ReaEQ bands; Spaces II impulses, pre-delay, wet, dry, irSetup, filter); a difference stops the build
with the list. Track jobs remove every send of the track and make them again; a send that cannot be made (no return
track, no send envelope) prints `SEND ERROR` and stops the build.

## What the chunks hold (read from `ho-mix-chunks/*.txt`)

- A plugin block is three base64 runs: REAPER's header (plugin id, magic 0xFEED5EEE or ...EF, pin masks, the state size),
  the plugin state (what `vst_chunk` reads and writes; the same kind of run as the Opus states the build already loads),
  and a trailer (VST2 program name, VST3 six zero bytes).
- ReaEQ: version 0x21, band count, per band type / enabled / frequency / linear gain / bandwidth in octaves.
- EW Spaces II: a JSON object. The IR is `impulseA` / `impulseB`, the left and right halves of a true-stereo impulse;
  the template loads the rear-position impulses (`... L Rear N` / `... R Rear N`; the brass return pairs
  `S. Cal. Hall Horns L Rear N` with `S. Cal. Hall Brass R Rear N`; San Francisco Hall `RL` / `RR`). `trueStereo` true.
  Pre-delay is `delay` in seconds: strings 0.0196, winds 0.018496, brass and perc 0.0100. Wet is `wet` (linear,
  0.98-1.004) with `dry` 1e-6 (100 % wet). The IR envelope is `irSetup` with `endPos` 1.0 (the full IR). The input
  filter is off (`filterActive` false). `selectedPreset` only labels the GUI.
- ReaVerbate (ALGO GLUE): eight floats after two magic words; which slider is which is not decoded here.

## The proposed mix (`build/mix_template50.json`)

- `opus_reverb_off` true; `send_profile` "ew".
- Returns: R Strings (STRING VERB: S. Cal. Hall Strings TS RR 3.3s, 19.6 ms, fader +1.03 dB), R Brass (BRASS VERB, 10 ms,
  +1.03), R Winds (WW VERB: San Francisco Hall TS RR 3.4s, 18.5 ms, +1.03), R Perc (PERC VERB: Northwest Hall TS RR 2.6s,
  10 ms, +0.66), each its ReaEQ then Spaces II verbatim; R Glue (ALGO GLUE: ReaEQ + ReaVerbate, +5.82 dB, `enabled`
  false); R Duc (the Duc variant, used by profile `duc` only).
- Sends (`ew`), from ho-mix-fx.json: strings -5.56, brass (horn, trumpet, lowbrass) -8.77, winds -8.36, timpani and
  percussion -6.41, harp -8.77 dB; R Glue -9.62 / -5.65 / -7.27 / -6.41 / -6.81 dB (skipped while disabled).
- Mics (`mic_db` per track, from opus-mics.txt by patch): 1st Violins Close -9.0, 2nd Violins -7.7, Violas -7.0, Celli
  -6.6 and Basses -3.3 (the template's Leg Slur patches; its Celli / Basses KS Masters load Main only), Main 0; horns
  Close -6.3 (1FH) / -7.7 (2FH), trumpets -10.1 (1TP; also used for 2TP, which the template does not load), trombones
  -9.3 (the template's 2TB), tuba -10.2; winds Close 0 with Main flute -4.7, flute 2 -3.4, oboes -20.6, cor anglais
  -11.6, clarinets -3.4, bass clarinet -9.8, bassoons and contrabassoon -8.6; harp Close 0 / Mid 0 / Main -9; timpani
  Close -8.4 / Main -6.9 / Surround 0; tam-tam and cymbals Main only. Cello solo keeps its own `mics` (DIV A has only
  Close). Note: 1TP KS Master loads Surround at 1.0 by default; `mic_db` unloads it.
- `pan_by_mic` on every group: Close `seat`, Mid / Main / Surround `full` (the plan's rule). `factory` would give the
  template's exact Close pans (with full width) instead of our seats -/+ width.
- `reaper_pan`: Vln I -0.10, Vln II -0.21, Va 0, Vc +0.15, Cb +0.23, Horns 1-4 -0.18 / -0.16 / -0.15 / -0.13 (a2 -0.16),
  Trumpets 1-3 +0.03 / +0.06 / +0.10 (a2 +0.05), trombones +0.15, tuba +0.23; aliases and tests take their source's.
  None for winds, harp, timpani, percussion (the plan gives none).
- `family_eq`: strings, brass (horn, trumpet, lowbrass), woodwinds, harp, timpani: the decoded template bands (with their
  bandwidths); percussion none. `master_eq`: HPF 42, -1.6 dB at 167 Hz, -1.9 dB at 1.18 kHz, +0.8 dB shelf at 8 kHz.
- The old keys stay (`mics`, `width_by_mic`, `send`, `reverb`): inert where the new ones apply, and back in force for a
  track that sets `"mic_db": null, "pan_by_mic": null, "family_eq": null, "send_profile": null, "reaper_pan": null,
  "opus_reverb_off": false`. That is the recipe for the plan's pass-2 copy of the old layout (a test alias in
  score_config with those overrides in its mix.json entry).

### Per-track EQs that meet the family EQ (decide in c50; the plan says to drop those that only did the family EQ's job)

Violins I high shelf 5 kHz -4 dB against the strings' +4 dB shelf at 4.73 kHz (they cancel); Trombones 1-2 high shelf
4 kHz -4 dB against the brass +4 dB shelf at 7.49 kHz; Trumpets high shelf 4 kHz +2.5 dB stacks on it; Horns a2 high
shelf 1.25 kHz -3 dB; Bass clarinet high shelf 2.5 kHz -4 dB against the woodwinds' +5.1 dB at 7.59 kHz; the many
40 Hz high-passes now sit under the family HPFs (53 / 41 Hz). The harp's family HPF at 183 Hz removes its fundamentals
below about F#3: check the harp's low notes.

### Duc variant (plan section 8)

R Duc: a ReaEQ (high pass 184 Hz, low pass 3 kHz) before Spaces II loaded from the PERC VERB state with the IR replaced
by "Hollywood Scoring Stage TS RR 2.3s" (rear true-stereo impulses `//ir/LA Scoring Stages/S-S/Hollywood Scoring Stage
L Rear` / `R Rear`, from its .preset), pre-delay 12 ms (Duc's VSR value read as pre-delay; inferred), fader -5.5 dB.
Profile `duc`: every group sends 0 dB to R Duc; celli and basses `send_offset_db` -1.6, their short rows
(Pizzicato RRx4, Stac RRx9, Stac On Bow RRx9; Basses Pizz RRx4) `send_row_db` -5.4 (so -7 dB). Alternatives: Northwest
Hall 2.6s shortened with `"set": {"irSetup": {"envelopeMode": 2, "endPos": 0.85, "decayLength": 0.3}}` (measure the
RT; LEARNINGS c44), or "Burbank Scoring Stage Large TS RR 2.1s".
Two ways to A/B: (a) the whole mix: set `"send_profile": "duc"` and render into a separate folder (a full render each);
(b) pass 2: test aliases of the tracks under test with `"send_profile": "duc"` in their mix.json entries; they feed
`R Duc test` (a test stem). For (b) remember the main tracks' reverb is in R Strings etc., so compare the
dry-plus-return sums, not single stems. Duc's instruments reach his master through -5.4 dB group buses while his hall
sends are taken before them, and VSR's wet level is not Spaces II's, so match the wet level by measurement before
judging (raising the R Duc fader by about 5.4 dB copies his routing). The low-string short cut can be used with the EW
returns too: add `"R Strings": {"Pizzicato RRx4": -7, "Stac RRx9": -7, "Stac On Bow RRx9": -7}` (Basses `Pizz RRx4`)
to those tracks' `send_row_db` once the send envelope is verified in REAPER.

## Rendering and the master sum

- REAPER renders each return as a stem, numbered by its track position (after the instrument tracks in the main
  project). `render_cycle.py` renumbers them right after the pre-roll cut: `91_R Strings.wav`, `92_R Brass.wav`,
  `93_R Winds.wav`, `94_R Perc.wav` (`95_R Glue`, `96_R Duc`), so every instrument stem keeps its name and number and the
  returns come last. A `"<return> test"` stem goes to `test_stems/`.
- Where the master sum is computed: in the main render, REAPER's own master mix (`render/00_Master.wav`) is the dry
  tracks plus the returns (no master FX); `render_cycle.py` replaces it with the float sum of every stem in `render/`
  (returns included) when it clips. With `--pass2`, `render_cycle.py` rebuilds `render/00_Master.wav` as the float sum
  of every stem in `render/`, after `return_stems.merge_pass2` has made each return stem the sum of the main project's
  return (kept in `render_pass2/returns_main/`) and the pass-2 project's return of the same name (re-runs start from
  the kept copy). `deliver_master.py` reads that master (then `master_eq`, the ride, the limiter).
- `measure.py`: return stems are left out of the per-track tables and listed under "Return stems (c50)" (peak, RMS,
  median bar level) with the energy of all returns against all instrument stems (`returns_re_dry_db` in metrics.json).
  Critics: balance on the dry stems, blend on the master.
- `stem_fix.py`: return stems are summed unchanged; their reverb keeps the old send levels of any track the fix changes.
- Critics' scripts that glob `render/[0-9][0-9]_*.wav` and look each name up in parts.json must skip the 9x return stems.

## Verified offline

- Byte-identical build for the c49 `build/mix.json` (`tools/build_identity_check.py` against the pre-change
  build_reaper.py): full build, `--midi-only` (which compares states), `--mix-only` and a two-track `--midi-only
  --tempo` build, each for the main pass and `--pass2`: 166 job files (Lua and Opus .b64 states) plus the stdout,
  stderr and exit status of the 8 runs, all byte-identical (run twice, the second time after every edit to tools/).
- Render side, c49 `build/mix.json`, original against current tools (render_cycle.py main and `--pass2`, measure.py,
  deliver_master.py, motion.py, stem_fix.py, on synthetic stems with a fake REAPER): 76 WAVs identical sample for sample
  (their bytes differ only in libsndfile's PEAK-chunk timestamp), 16 other files (metrics.md / json, mp3, logs)
  byte-identical.
- `template_mix.py check`: all 24 FX states of the template's chunks decode and match ho-mix-fx.json (ReaEQ bands within
  0.05 dB, Spaces II JSON equal), ReaEQ encode round trips, Spaces II edits change only the named values and keep the
  editor and JUCE bytes.
- `test_template_tools.py` on `build/mix_template50.json` (57 checks, all pass; the check of a family EQ given as a
  chunk was added afterwards and passes on its own): the returns job builds R Strings / Brass / Winds /
  Perc with the template's states byte for byte and their faders; every main Opus state has the `mic_db` levels and
  loading, the `pan_by_mic` rules, fx:0 volume 0 with no ConvolutionReverb and sends 0; every track's sends, family EQ
  (after the side shelf) and pan line match the mix; `--midi-only` and `--mix-only` re-add them; pass-2 test tracks send
  only to test returns; profile `duc` builds R Duc (ReaEQ 184 Hz / 3 kHz, the 2.3 s rear impulses, 12 ms) and the
  celli send envelope steps -1.6 / -7.0 dB at the first note of each row; a wrong read-back stops the build; the
  `fxchain` text round-trips; Lua blocks balanced (no Lua interpreter here: a token-level check). Return stems on
  synthetic audio: renumbering, test copies, the pass-2 merge (main + pass 2, idempotent), the master = dry + returns
  (test returns excluded), `fit` recovers send levels to 0.01 dB. render_cycle.py end to end with the template mix:
  names and order, measure.py's return section, the master EQ in the delivery; the master EQ's response on noise
  matches the band list.

## What the c50 actor must verify in REAPER

1. Chunk loading: the returns job must finish without "return tracks differ" (it compares what REAPER reads back). Open
   each return's Spaces II window once: the preset name and the IR should show; listen to a few seconds. If
   `vst_chunk` does not load Spaces II, set `"return_load": "fxchain"` and rebuild the returns (`--mix-only` is enough).
2. Send levels: render a short range with `"bypass": true` on the returns (each return is then the plain sum of its
   sends), then `~/.venvs/claude-composes-reaper/bin/python tools/return_stems.py fit cycles/cNN/render build/parts.json
   build/mix.json --start S --dur 20`: each track's send should read its profile level (-5.56 strings, ...) within
   0.05 dB with a residual under -60 dB; that also proves the sends are post-fader (they carry the volume envelope and
   the track pan). Remove `bypass` afterwards. The build log prints each send's D_VOL and mode (0 = post-fader).
3. Opus fx:0 silent: in the saved .rpp, decode one track's Opus state (LEARNINGS c40 method) and check fx:0 volume 0, no
   ConvolutionReverb, sends 0; and on a render, a short note's tail on its dry stem must fall like the dry sample (no
   hall), e.g. timpani or a string staccato: compare with the c49 stem.
4. Return stems at full length: every `9x_R ...wav` must be as long as the instrument stems and carry the tail to the
   end of the render (render_cycle pads only in `--pass2`); the stems of the selected return tracks must include their
   receives (REAPER's stem render), so `00_Master.wav` should equal the float sum of render/ (check once: max
   difference under 1e-5).
5. The send envelope (only if `send_row_db` is used, e.g. the Duc A/B): the build stops with `SEND ERROR` if
   `GetTrackSendInfo_Value(..., "P_ENV:<VOLENV")` does not give an envelope; otherwise check one envelope in REAPER and
   the -7 dB steps with `fit` on a bypassed render, over a window where only short rows play (`fit` assumes one
   level per track in its window).
6. The family EQ: the job result prints each band's formatted value and type; check one track per family in the ReaEQ
   window (5 bands; the type of each).
7. Re-balance after the change (the plan: the EQ removes 2-8 dB in the body bands; mic levels change; the hall now
   comes from the returns), re-fit the delivery (LRA 14-16 LU, span 16-19 dB, true peak -1.5 dBTP or lower), and check
   CPU / memory with four Spaces II instances per project.

## Open risks

- `vst_chunk` on Spaces II is untested in this REAPER (the Opus states load this way; the read-back check will say).
- The send envelope API (`P_ENV:<VOLENV`) returning a usable pointer in Lua is untested; only `send_row_db` needs it.
- Removing the ConvolutionReverb from fx:0 leaves Opus's FX channel with no insert; if Opus misbehaves, keep the insert
  with `"active": false` instead (one line in apply_mix).
- ReaVerbate's Dry slider in R Glue is not decoded; if it is up, the glue return adds dry signal.
- ReaEQ via `set_by_fmt` assumes the default 5-band instance and Hz display without "k" (as the per-track EQ does).
- The harp HPF at 183 Hz and the timpani +8.6 dB at 84 Hz / +9.1 dB shelf are large; the per-track shelves above meet
  the family shelves.
- `stem_fix.py` cannot re-simulate the returns.
- The Duc wet level is not comparable by numbers (bus routing and engine); match it by measurement.
- Rules that exist because the hall sat inside Opus, before the volume envelope (`tail_hold` c17/c19, `SUBITO_TAIL`
  c36, the release caps and release-trail gains fitted against the c44 hall): with the returns fed post-fader the hall
  now sits after the envelope, so an envelope move in a rest no longer cuts a hall tail. They still shape the dry
  release; re-check them after the change rather than assuming they still do what their notes say.
- Gains: every `gain_db`, trim and fill was fitted with the old mics and the Opus hall; the new mic levels, the family
  EQ and the returns change every stem's level and spectrum.

## Verified in REAPER (c50, 2026-11-08)

- `vst_chunk` loads Spaces II and ReaEQ; the read-back of every return FX matched (impulses, pre-delay, wet, dry, irSetup
  with envelopeMode 2). A `{"reaeq": [bands]}` entry after Spaces II in `returns.*.fx` builds a third FX as written.
- Sends are post-fader (mode 0): `return_stems.py fit` on a bypassed 22 s range read every send at its profile level with
  a residual of -106..-112 dB. Send envelopes (`send_row_db`) read back active with the scherzo c06 fix.
- Opus fx:0 decoded from the saved .rpp: volume 0, no ConvolutionReverb, every mic's send 0.
- Return stems render at full length; `00_Master.wav` equals the float sum of render/ within 1e-6.
- `spaces_set` keeps a value the plugin writes as an integer literal integral (`"envelopeMode":2`), c50.
- Measured settings that differ from the template (cycles/c50/CHANGES.md): Main at the seat -/+ 0.8 with a side-only
  200 Hz -6 dB shelf (full-width Mains gave anti-phase bass), return faders -8 / -12 / -4 / -4 dB, the IR envelope 0.5 /
  0.5, strings family shelf off, brass +1.

