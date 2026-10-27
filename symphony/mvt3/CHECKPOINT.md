# Finale (movement IV) loop checkpoint

- Since v326 the timpani rolls are repeated strokes in score.midi (score.ly's MIDI score uses \rollStrokesByBar with v*/rolls-midi.ily). Before the next r07 render, test prep_render.py on a copy: the percussion variables keep their names, but each roll is now 8–64 MIDI notes.

## Third series, continued (session cse_01JYb3wFaQo49G4BVrXbmdSc, thread "Finale, loops from v341", since 2026-10-26 18:12)
Latest: **v391** (cycle 390 done, cyclic, no score change). Next cycle: **391** (lens 1). For lens-9 cycles pass the next MASTERS.txt entry as the focus; for lens-10 pass the cyclic-review focus as go.sh arg 5 of cycle N-1 or regenerate pN. Series ends at cycle 399 → v400. Theme record now 51/51 (c370 added threadViola) (c350 added eight at-pitch link checks). Helper scripts: /mnt/project-files/symphony/mvt3/kit-helpers/ plus go.sh (addnote + cyc.sh). cyc.sh commits only finale.md from coherence/: commit themes-finale-quotes.ly by hand when it changes. For lens-10 cycles take sibling coherence files from their branches (git show origin/claude/project-thread-{ytvxdy,wtf58k,y9u1tb}:symphony/coherence/...), then git checkout them back.

## Third series, continued (session cse_01SWLBceYg6ZWKih28Euwaj4, thread "Finale, loops from v264", since 2026-10-19 22:10)
Latest: **v341** (cycle 340 done, cyclic). Next cycle: **341** (lens 1). Series ends at cycle 399 → v400 (Dan 2026-10-25: 100 more loops). v300 was the merge snapshot and was rendered with r07. Handoff 2026-10-26 ~18:15 UTC at 21.2 h uptime (mount expiry), branch claude/project-thread-v69o8h at the commit after 26f38cc8.
Per cycle helper (scratchpad, recreate if lost): promote.sh N+1 N /tmp/critic-N/work; add a running-list line to coherence/finale.md; finish.sh N "lens ..." notes; copy finale.md and themes-finale-quotes.ly to the mount; genprompt N+1. Lens 9 cycles add the "v(N-10) has no score.pdf" note; lens 10 cycles add the cyclic focus and the stale-sentence request.
r07 render: copy the version, simplify arrivalPerc to `<cymc bd>1\fff | R1*11 |`, codaTwoPerc to `R1*8 | R1*2 | R1*2 |`, and finalePerc's two-voice 278–279 to `<cymc bd>1->\fff~ | <cymc bd>4 r4 r2\fermata`; assets from /mnt/project-files/symphony/render/assets/{iowa,philharmonia,vpo3,sf2}.
Theme record 42/42 (v316 added the at-pitch G♯ lines at 1 and 243, v331 motiveXcloseC at 276, v332 replaced choraleFirst VlnOne 226 by choraleCanon). coherence/themecheck.py is the scherzo's at-pitch ('abs') version; coherence/lyparse.py includes movement II's patches (mvt2 triplets, c370 ties, c390 braced branch).
Helper scripts were in the old session's scratchpad (cyc.sh, addnote.py, prep_render.py); their logic: promote, add a numbered line to finale.md's running list ('## Changes in cycles 261–') and update 'running list for v262–vNNN', finish.sh, mirror finale.md + themes-finale-quotes.ly to the mount, genprompt N+1. Before each lens-10 cycle, copy the siblings' coherence files from the mount into the checkout (do not commit them).

## Third series (2026-10-19, thread "Finale, 200 more loops", session cse_01S169UKdVsqhaxTmmz6YB7N)
Cycles 201-400 (v201 -> v401), branch claude/project-thread-v69o8h (pushed after every cycle, no PR). Latest: **v264** (cycle 263 done). Next cycle: 264.
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
