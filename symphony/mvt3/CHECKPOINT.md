# Finale (movement IV) loop checkpoint

## Third series (2026-10-19, thread "Finale, 200 more loops", session cse_01S169UKdVsqhaxTmmz6YB7N)
Cycles 201-400 (v201 -> v401), branch claude/project-thread-v69o8h (pushed after every cycle, no PR). Latest: **v241** (cycle 240 done). Next cycle: 241.
Per cycle: `bash kit/genprompt.sh N ""`; background Agent "Read your full task from .../kit/pN.txt ..."; review the diff; `bash kit/promote.sh N+1 N /tmp/critic-N/work`; write the decision notes to a file and `bash kit/finish.sh N "lens ..." FILE` (writes critique.md, HISTORY, commits, pushes, mirrors the latest text files to /mnt/project-files). promote.sh keeps score.pdf in the newest version and pdf+mp3 in v211, v221, ...


Thread "Continue movement 4 loop" (session cse_01QDtx9SfJvuVALZjuqD7wEm) resumed the loop on 2026-10-16 in the git checkout /home/user/claude_composes (the kit's paths now point there, not at /mnt/project-files, which no longer holds symphony/).

- Last promoted version: **v201** (cycle 200 done; the loop's final version). 279 bars, 2/2, ~7:02 (MIDI 422 s), 16 A3 pages, 0 warnings, 0 outer-voice parallels, quotation record 36/36; scherzo quotations checked against the scherzo thread's current themes (scherzo v171). Parts rebuilt in v201/parts with 0 warnings. score.pdf/score.mp3 kept only in v191 and v201 (and v111, v160, v181 keep their r07 renders as score-r07.mp3).
- The planned loop (to cycle 200 → v201) is complete. To run more cycles, next would be **201** (reviews v201, produces v202).
- Resume:
  1. Container: `apt-get install -y lilypond fluidsynth fluid-soundfont-gm poppler-utils`; `pip install mido soundfile scipy numpy`.
  2. `bash symphony/mvt3/kit/genprompt.sh 201 "<focus>"`.
  3. Background general-purpose Agent: "Read your full task from /home/user/claude_composes/symphony/mvt3/kit/p201.txt and carry it out exactly. Do not call any mcp__hearthbot tools and do not message anyone; write only your report file and your scratch copy under /tmp/critic-201. Do not run git commands."
  4. Review the diff of /tmp/critic-201/work against v201, `bash kit/promote.sh 202 201 /tmp/critic-201/work`, drop the stale v202/parts copy, write v202/critique.md, append to critics/HISTORY.md.
- Book PDFs are in /home/user/claude_composes/pdfs/ (the critic prompt says so).
- Standing rules: unchanged (see the previous checkpoint text in git history, critics/HISTORY.md and coherence/finale.md). R at 247 stays 2 = 88; C7 only at 223; fff only at 223, 263, 278; only root-position V–I in C at 262–263.
- Scherzo loop: thread "Continue movement 3 loop" (session cse_019MVHJqMqMN1aRTnYSzHgLw), branch claude/mvt3-loop-continue-60m9cq; it messages this thread when a scherzo theme changes. Its latest coherence files may be on that branch before main.
- Checkpoint PRs: #20 (v121, cycles 111-120); batches 121-200 were added to #20 while it was unmerged (now v201).
- Rendering: r04/r07 perc.py may need the two-voice percussion at 223 (since v147) and <cymc bd> chords simplified in a temp copy.
