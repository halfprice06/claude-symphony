# EastWest Templates 2 (Hollywood Orchestra, REAPER): extracted data

Read from EastWest's free HO REAPER template ("EW Hollywood Orchestra Template (Midi Included).RPP", Templates 2, 2026; https://www.soundsonline.com/templates-2). The project itself is not committed. Findings are in `FINDINGS.md`.

- `ho-mix-fx.json`: every mix track's fader, pan and receives (with the raw AUXRECV line), plus each FX chunk: the REAPER chunk header and base64 lines exactly as in the .RPP, the decoded ReaEQ bands, and the decoded Spaces II state JSON. Opus chunks are left out; their mic settings are in `opus-mics.txt`.
- `ho-mix-chunks/<track>.txt`: the verbatim `<FXCHAIN>` block of each section bus, reverb return, harp, timpani and the master (`<MASTERFXLIST>`). You can paste them into an .RPP or set them per FX with `TrackFX_SetNamedConfigParm(..., "vst_chunk", ...)`.
- `opus-mics.txt`: loaded Opus mics, their levels and pans, per instrument.
- `midi-report.txt`: per-track MIDI statistics. On KS Master tracks these include the keyswitch notes; `artic-report.txt` separates the notes by articulation and leaves the keyswitches out.
- `ccshape-report.txt`: CC1 movement around phrase starts, legato note changes, phrase ends, and inside long notes.
- `scripts/`: the parsers (run them with `python3 -I`). `extract_fx.py <rpp> <outdir>` regenerates the JSON and the chunks. `fxstate.py <rpp> <fx substring>` prints the strings in an FX state.
