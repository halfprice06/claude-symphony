# Finale (movement IV) loop checkpoint — 2026-10-16, after cycle 150

Thread "Continue movement 4 loop" (session cse_01QDtx9SfJvuVALZjuqD7wEm) resumed the loop on 2026-10-16 in the git checkout /home/user/claude_composes (the kit's paths now point there, not at /mnt/project-files, which no longer holds symphony/).

- Last promoted version: **v151** (cycle 150 done). 279 bars, 2/2, ~7:01 (MIDI 421 s), 16 A3 pages, 0 warnings, 0 outer-voice parallels, quotation record 36/36; scherzo quotations checked against the scherzo thread's current themes (scherzo v101+). Parts rebuilt in v151/parts. score.pdf/score.mp3 kept only in v151 (and v111 with its r07 render).
- Next cycle: **151** (reviews v151, produces v152). The loop runs to cycle 200 → v201, in batches of 10, each checkpointed to main by PR.
- Resume:
  1. Container: `apt-get install -y lilypond fluidsynth fluid-soundfont-gm poppler-utils`; `pip install mido soundfile scipy numpy`.
  2. `bash symphony/mvt3/kit/genprompt.sh 151 "<focus>"`.
  3. Background general-purpose Agent: "Read your full task from /home/user/claude_composes/symphony/mvt3/kit/p151.txt and carry it out exactly. Do not call any mcp__hearthbot tools and do not message anyone; write only your report file and your scratch copy under /tmp/critic-151. Do not run git commands."
  4. Review the diff of /tmp/critic-151/work against v151, `bash kit/promote.sh 152 151 /tmp/critic-151/work`, drop the stale v152/parts copy, write v152/critique.md, append to critics/HISTORY.md.
- Book PDFs are in /home/user/claude_composes/pdfs/ (the critic prompt says so).
- Standing rules: unchanged (see the previous checkpoint text in git history, critics/HISTORY.md and coherence/finale.md). R at 247 stays 2 = 88; C7 only at 223; fff only at 223, 263, 278; only root-position V–I in C at 262–263.
- Scherzo loop: thread "Continue movement 3 loop" (session cse_019MVHJqMqMN1aRTnYSzHgLw), branch claude/mvt3-loop-continue-60m9cq; it messages this thread when a scherzo theme changes. Its latest coherence files may be on that branch before main.
- Checkpoint PRs: #20 (v121, cycles 111-120); batches 121-150 were added to #20 while it was unmerged (now v151).
- Rendering: r04/r07 perc.py may need the two-voice percussion at 223 (since v147) and <cymc bd> chords simplified in a temp copy.
