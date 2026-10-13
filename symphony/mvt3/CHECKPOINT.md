# Finale (movement IV) loop checkpoint — paused 2026-10-13 23:10 UTC

Paused at Dan's request (usage limit). Resume in a fresh thread (shared-folder mount expires ~24 h after a machine starts).

- Last promoted version: **v111** (cycle 110 done). Rendered with r07 for Dan: v111/score-r07.mp3 (7:08). 279 bars, 2/2, ~7:01 (MIDI 421 s), 16 A3 pages, 0 warnings, 0 outer-voice parallels, quotation record 36/36, scherzo record 41/41 vs scherzo v86.
- Unpromoted work: none. Cycle 111's critic was started and stopped early; it wrote nothing (no report, no scratch). Re-run cycle 111 from scratch.
- Next cycle: **111** (reviews v111, produces v112). The loop runs to cycle 200 → v201.
- Resume commands (the prompt kit/p111.txt already exists; regenerating is fine):
  1. `cd /mnt/project-files/symphony/mvt3 && bash kit/genprompt.sh 111 "<focus>"` (lens = ((N-1) mod 10)+1; lens 9 takes line (N-9)/10+1 of critics/MASTERS.txt; lens 10 cycles read all of symphony/coherence/).
  2. Launch a background general-purpose Agent: "Read your full task from /mnt/project-files/symphony/mvt3/kit/p111.txt and carry it out exactly. Do not call any mcp__hearthbot tools and do not message anyone; write only your report file and your scratch copy under /tmp/critic-111. Do not write any files inside /home/user/claude_composes."
  3. On its report, accept or reject every finding yourself (Dan makes no musical choices), then `bash kit/promote.sh 112 111 /tmp/critic-111/work`, write v112/critique.md, append `## Cycle 111 (v111 → v112), lens …` to critics/HISTORY.md, `rm -rf /tmp/critic-111 /tmp/m3/v111`.
  - Container setup if missing: apt-get install -y lilypond fluidsynth fluid-soundfont-gm; pip install mido soundfile scipy numpy.
- Standing rules (see critics/HISTORY.md and coherence/finale.md):
  - R at 247 stays "Più allegro" 2 = 88 (Dan found 100 too fast). C7 in any part only at 223. fff only at 223, 263, 278. Only root-position V–I in C at 262–263.
  - Keep coherence/finale.md current (only this thread edits it). Message the scherzo thread (now session cse_011uo61BdJV54PsP5ATLYMHU, "Scherzo loops, cycles 80–200") about changes affecting it; movement II is final at v201.
  - Relay to the coordinator every 10 cycles (next after cycle 120); get its id with get_channel_session_id.
  - Renders only when Dan asks, one at a time across threads. r04 and r07 perc.py cannot parse the part-only `\tag #'part` cue in codaTwoPerc (and r04 also not `\tweak style` or `<cymc bd>` chords): render from a temp copy with those simplified.
  - MOUNT RULE: check `cat /proc/uptime` at the start of each cycle; past ~22 h, promote the current cycle, send the coordinator a handoff (last version, unpromoted work, next command) and stop. On any I/O error under /mnt/project-files, hand off at once without retrying.
