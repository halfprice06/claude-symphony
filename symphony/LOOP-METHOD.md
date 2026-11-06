# The actor–critic loop used for movement I

This is the exact procedure used for movement I. The first series was cycles 1–100 (v21–v120); the second series is cycles 101–200 (v121–v220) and is in progress. A movement II thread can follow it step by step. The working copies of every file named here are in `symphony/mvt1/critics/` and `symphony/loop-kit/`.

## Roles

- **Actor (the composer):** the thread's own session. It owns the score, chooses which critic fixes to accept, promotes each new version, and writes the log.
- **Critic:** a new, independent subagent for every cycle, started with the Agent tool (`general-purpose`, run in the background). Dan's rule: the actor never critiques its own work. Every critique comes from a subagent that studies the books, the corpus and the web.
- One cycle runs at a time. Cycle N reviews version v(19+N) and produces v(20+N). In movement I, v1–v20 were the composer's own drafts before the critic series began.

## Folder layout (movement I)

```
symphony/mvt1/
  vNN/                 one folder per version: global.ily, score.ly, parts.ily, sections/*.ily,
                       sections.txt, critique.md, plus build outputs (score.pdf, score.midi, score.mp3,
                       analysis.txt, build.log, build-warnings.txt)
  tools/build.sh       assemble → lilypond → fixmidi → FluidSynth mp3 → analyze.py (parallels, profile)
  critics/BRIEF.md     the brief every critic reads (goal, rules, research requirements, report format)
  critics/LENSES.md    the 10 rotating lenses
  critics/READING.md   the assigned book reading for each cycle (from cycle 107)
  critics/HISTORY.md   one entry per cycle: what was accepted, what is still open, the do-not-touch list
  critics/reports/cNNN.md   each critic's full report
symphony/loop-kit/     critic_prompt.txt (prompt template), genprompt.sh, promote.sh, syllabus.py
symphony/cyclic-notes.md   material shared between movements (owned by the movement I thread)
reference-books/       Dan's books; INVENTORY.md, text/<book>/p0123.txt
guides/eastwest-hollywood-orchestra/   the mockups' sample library manuals (see "The sample library")
reference-corpus/      master scores (LilyPond/MusicXML/PDF); README.md is the index
```

For movement II, create `symphony/mvt2/` with the same layout. Copy `mvt1/tools/` into `mvt2/tools/` and edit only that copy. Write your own BRIEF, LENSES, READING and HISTORY. Do not write into `mvt1/`, and do not write into `loop-kit/` (copy it).

## The lens rotation

Cycle N uses lens ((N−1) mod 10) + 1:

1. melody
2. harmony and voice leading
3. form and pacing
4. orchestration
5. engraving
6. playability
7. texture and counterpoint
8. expression
9. holistic comparison with one master movement (a different one each time) and with the version ten cycles earlier
10. cyclic design and emotional arc

The exact wording is in `mvt1/critics/LENSES.md`.

## The reading plan (from cycle 107, by Dan's instruction)

Dan: "I want greater coverage and use of the books. the focus should be on the books content."

`critics/READING.md` gives each cycle one chapter or page range from the books in `reference-books/`, chosen to fit its lens. The plan covers all the relevant chapters before any reading repeats. `loop-kit/syllabus.py` generated it from per-lens lists: edit those lists and the cycle range for movement II. The critic must:

1. read every text page in the range, not just keyword hits;
2. render every music-example page as an image (`pdftoppm -f N -l N -r 110 -png "<book>.pdf" /tmp/critic-NNN/pg`) and look at it, because the OCR of notation and chord labels is unreliable;
3. open its report with a "Reading notes" table: principle, book and PDF page, bars of the score, verdict (follows / violates / not applicable);
4. base its findings on that reading. The corpus and the web are secondary.

## The sample library (from 2026-11-06, by Dan's instruction)

The DAW mockups are played by EastWest Hollywood Orchestra Opus Edition. Its manuals are in `guides/eastwest-hollywood-orchestra/`; the May 2021 edition (`text/EW-Hollywood-Orchestra-Opus-Edition-User-Manual-2021.txt`) has the most detail per instrument. The composer and the critics use it whenever a choice concerns an articulation, playing technique, mute, divisi, or a solo against a section: they check whether the library has a matching patch and say so, citing the manual page. The score is still written for a real orchestra; a marking with no patch is named so the mockup can plan for it, not removed.

## One cycle, step by step

1. **Write the critic prompt.** `genprompt.sh N "optional focus sentence"` fills `critic_prompt.txt` and writes `pN.txt`. It substitutes the cycle number, the version under review, the lens text from LENSES.md and the reading from READING.md. The focus sentence is optional; use it to point the critic at a known weakness. The prompt tells the critic to:
   - read BRIEF.md, LENSES.md and HISTORY.md first;
   - do the assigned reading as above;
   - copy the version into `/tmp/critic-NNN/work`, edit `sections/*.ily` there, and build it with `tools/build.sh /tmp/critic-NNN/work score.ly`;
   - check that the build has 0 warnings, the parallels check shows only the known exceptions, and the page count is unchanged;
   - follow the score rules: concert pitch; equal simultaneous dynamics on shared (part-combined) staves; no `\ottava` where the other player sounds; slurs opened and closed; any new tempo word gets a matching `\mt` MIDI tempo step in global.ily; protected passages in HISTORY.md change only if the critic answers the stated reason;
   - write the report to `critics/reports/cNNN.md`: plain prose, up to 8 ranked findings, each with bars, problem, evidence and a LilyPond fix, and a closing do-not-touch line;
   - never write anywhere else in /mnt/project-files, never delete files, and keep scratch files under 1 GB.
2. **Start the critic** with the Agent tool, in the background. Its prompt is one line: "Read your full task from <path>/pN.txt and carry it out exactly."
3. **Wait** for the completion notification. Don't poll.
4. **Review.** Read the critic's summary. Diff the scratch copy against the current version:
   ```
   diff -ru vNN/sections /tmp/critic-NNN/work/sections
   ```
   Also diff global.ily and score.ly. Check each change against the report and against HISTORY.md.
5. **Decide.**
   - Accept a fix when its evidence holds and it doesn't break a protection without answering the protection's reason.
   - Reject or defer anything inside a protected passage that the critic didn't justify, and anything that only matters for parts not yet built. Record it as "Open" in HISTORY.
   - If a fix undoes an earlier cycle's change, accept it only when the new argument is stronger. In that case add the outcome to the do-not-touch list so later critics don't flip it back (example: cycles 102 and 103 on the codetta).
   - When accepting only some of the scratch changes, edit a copy of the scratch folder, or make the change by hand in the new version.
6. **Promote.** `promote.sh NEW PREV SRC` copies SRC into `vNEW` (excluding build junk), changes the header text "draft vPREV" to "draft vNEW", runs build.sh, and prints the warnings count, the parallels result, the page count and the header. Then check:
   - `build-warnings.txt` is 0 bytes;
   - the page count is unchanged (17 for movement I);
   - the parallels check shows only the known exception (for movement I: "bar 96: octaves F5->Bb2 over F2->Bb1");
   - score.mp3 is full size. Once a build stopped partway because the analysis script crashed; rebuilding fixed it.
7. **Log.**
   - Write `vNEW/critique.md`: cycle, lens, reading, the report path, the changes applied (with bars and files), the changes not applied, and the build result.
   - Append an entry to `critics/HISTORY.md` with "Accepted:", "Open:" and "Do-not-touch:" lines.
   - If the cycle changes material other movements use, update `cyclic-notes.md`. For movement II: send the change to its owner through the coordinator instead of editing the file.
8. **Next cycle.** Go back to step 1 with N+1.
9. **Status.** Refresh the thread's status checklist after every cycle. Reply to Dan only when he asks, or when something needs his decision.

## Audio

- Every build makes a basic FluidSynth `score.mp3`.
- When Dan asks to hear a version, render it with the improved renderer, r02:
  ```
  cd symphony/render/r02 && python3 render.py --v120 <vNN folder> --work /tmp/render-vNN --out <vNN>/score-r02.mp3
  ```
  It takes about 5 minutes and about 5 GB of scratch space. Run one render at a time, and delete the work folder afterwards.
- r02's melody settings are tied to movement I's bar numbers. Movement II needs its own copy of `render/r02` with its own `config.json` melody list.

## Disk

The container's writable disk is limited (about 9 GB free on 2026-10-09). It filled up once because of render scratch folders. Keep each critic's scratch under 1 GB, and run renders one at a time.
