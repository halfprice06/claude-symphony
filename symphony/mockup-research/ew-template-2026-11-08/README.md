# EastWest Templates 2 (Hollywood Orchestra, REAPER): extracted data

Read from EastWest's free HO REAPER template ("EW Hollywood Orchestra Template (Midi Included).RPP", Templates 2, 2026; https://www.soundsonline.com/templates-2). The project itself is not committed. Findings are in `FINDINGS.md`.

- `ho-mix-fx.json`: every mix track's fader, pan and receives (with the raw AUXRECV line), plus each FX chunk: the REAPER chunk header and base64 lines exactly as in the .RPP, the decoded ReaEQ bands, and the decoded Spaces II state JSON. Opus chunks are left out; their mic settings are in `opus-mics.txt`.
- `ho-mix-chunks/<track>.txt`: the verbatim `<FXCHAIN>` block of each section bus, reverb return, harp, timpani and the master (`<MASTERFXLIST>`). You can paste them into an .RPP or set them per FX with `TrackFX_SetNamedConfigParm(..., "vst_chunk", ...)`.
- `opus-mics.txt`: loaded Opus mics, their levels and pans, per instrument.
- `midi-report.txt`: per-track MIDI statistics. On KS Master tracks these include the keyswitch notes; `artic-report.txt` separates the notes by articulation and leaves the keyswitches out.
- `ccshape-report.txt`: CC1 movement around phrase starts, legato note changes, phrase ends, and inside long notes.
- `scripts/`: the parsers (run them with `python3 -I`). `extract_fx.py <rpp> <outdir>` regenerates the JSON and the chunks. `fxstate.py <rpp> <fx substring>` prints the strings in an FX state.

Part 4 of `FINDINGS.md` (other experts' mockups, 2026-11-08 evening):
- `expert-report.txt`: statistics for 20 expert MIDI mockups (phrase-shape table, per-family timing, overlap, repeated-note, velocity and CC numbers, beat-level tempo, tutti entry spread, then per-track detail). The MIDI files are not committed.
- `duc-mix.txt`: Bernard Duc's two REAPER projects, mix side: FX per track, routing and send levels, decoded Pro-Q 2 bands, VSR S24 reverb presets and values, the room-noise bed.
- `scripts/smf2.py out.json file.mid ...` (per-track and phrase-shape statistics), `xsum.py` (family summary from the JSON files in `reports/`), `rubato.py`, `async.py`, `rppmix.py <rpp> <first track>`, `rppau.py <rpp> <outdir>` (AU plugin states), `proq2.py <blob> ...` (FabFilter Pro-Q 2 bands).

Part 5 of `FINDINGS.md` (two Cubase projects with VSL instruments, 2026-11-08 night):
- `cubase-report.txt`: the same statistics as `expert-report.txt` for Goldsmith's Mulan overture and Hisaishi's Howl's Moving Castle, read from their Cubase projects. The projects are not committed.
- `cubase-mix.txt`: their reverb settings (Lexicon Random Hall values, Cinematic Rooms presets) and the Vienna Ensemble Pro mixer stored inside each project (faders, pans, reverb sends per channel).
- `scripts/cpr2mid.py in.cpr out.mid` converts the MIDI parts, tempo track and controller curves of a Cubase .cpr into a MIDI file (uses `cprlib.py`; `CURVE=travel|box|linear` picks how curves are read). `cprparts.py` lists the parts, `cprprobe.py` prints the raw tempo, note and controller records, `cproffset.py` tests the part-offset rule, and `vepdump.py <file.cpr>` prints the Vienna Ensemble Pro mixer stored in the project (needs the `zstandard` package). `smf2.py` now takes the CC lanes from `LANES=1,11,2`.

Part 6 of `FINDINGS.md` (Lorne Balfe's MIDI sketches, 2026-11-08 night):
- `balfe/*.mid`: six cues from 14th Street Music's Hightail shares, uploaded by Dan: The Crown main titles, Kung Fu Panda 3 "Father and Son", Bad Boys for Life main theme, 6 Underground "I Am the Danger", Penguins of Madagascar main theme, Genius season 2 main titles. Kept here for study only. Share pages: https://spaces.hightail.com/receive/TCozhRWdeC/bWJpdHRvbkAxNHRoc3RyZWV0bXVzaWMuY29t (The Crown), https://spaces.hightail.com/receive/eRvedVZihV/cWxpQDE0dGhzdHJlZXRtdXNpYy5jb20 (Kung Fu Panda 3), https://spaces.hightail.com/receive/2rJTv1Bj4Y/YWdvZGZyZXlAMTR0aHN0cmVldG11c2ljLmNvbQ (Bad Boys), https://spaces.hightail.com/receive/yLkBMCQegi/bWJpdHRvbkAxNHRoc3RyZWV0bXVzaWMuY29t (6 Underground), https://spaces.hightail.com/receive/gRkmkfxsre (Penguins), https://spaces.hightail.com/receive/v9WZxJ2Fd7/YWdvZGZyZXlAMTR0aHN0cmVldG11c2ljLmNvbQ== (Genius).
- `balfe-report.txt`: entry spread and tempo, the `smf2.py` statistics, then `scripts/balfe_extra.py` (tracks sharing identical CC lanes, CC11 minus CC1 per track with correlation and lag, CC1 at phrase entries, CC7 lanes) and `scripts/accent.py` (short-note velocity by slot within the beat). Both scripts take a MIDI file and need `mido`.
