# Scherzo checkpoint (2026-10-13 ~23:10 UTC, paused at Dan's request before the usage limit)

- Last promoted version: **v87** (cycle 86). 376 bars, 13 A3 pages, ~4:36; 0 warnings, 7 known analyser parallels, theme record 41/41, no C-major triad, part lengths match, parts rebuilt. Cycles 1–86 are logged in critics/HISTORY.md and v87/critique.md.
- Render: v87/score-r07.mp3 (r07, 4:38) made for Dan at the pause.
- Unpromoted: nothing. Cycle 87's critic (lens 7 texture, Rimsky-Korsakov ch. II) was stopped a few minutes after it started; it wrote no report. Its prompt kit/p87.txt is ready and can be reused as is.
- Next cycle: **87** (reviews v87, produces v88). Resume with:
  1. Container setup: `apt-get update && apt-get install -y lilypond fluidsynth fluid-soundfont-gm poppler-utils` and `pip install mido soundfile scipy numpy`.
  2. `bash /mnt/project-files/symphony/scherzo/kit/genprompt.sh 87 ""` (already written once; re-running is harmless).
  3. Start the critic (Agent tool, general-purpose, background) with the one-line prompt "Read your full task from /mnt/project-files/symphony/scherzo/kit/p87.txt and carry it out exactly."
  4. Review the diff of /tmp/critic-087/work against v87, then `bash kit/promote.sh 88 87 /tmp/critic-087/work` (2–3 minutes; long timeout).
- Relays: cycles 71–80 sent to the coordinator. The next relay (cycles 81–90) is due after cycle 90.
- Theme changes since the last relay: v82 trio tune bars 10–11 (A tied over the bar line); record refreshed, finale told. coherence/scherzo.md is current to v87.
- Uptime/handoff rule (coordinator, 2026-10-13): the shared-folder mount seems to expire about 24 h after a thread's machine starts. Check `cat /proc/uptime` at the start of each cycle; past about 22 h, finish and promote the current cycle, send the coordinator a handoff and stop. On any /mnt/project-files I/O error, send the handoff at once and do not retry for 30 minutes. (Also in critics/HISTORY.md, "Mount-expiry rule".)
- Coordination: finale thread cse_01VEPkuwEiufbD2AHMw6eKEa; stop chord B–D–F–A♭/G♯ reserved for the finale; themes not locked; renders only on Dan's request, r07 by default.
