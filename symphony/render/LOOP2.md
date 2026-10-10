# Series 2 loop procedure (r03–r22)

Numbering: critic N reviews rN and writes critics/cNN.md (with numbers in critics/cNN/); actor N+1 builds r(N+1) from
rN and that report. Critic 2 (r02) starts the series; actor 22 builds r22; critic 22 gives the final review.
Every critic and actor is an independent subagent. A critic never reviews its own work and does its own web research.

## Each actor (N+1)
1. Copy rN/ to r(N+1)/ (code, config, sfz; not out*.mp3, not meas/). One command must rebuild each test input:
   `python3 render.py --score <symphony/mvtX/vNN> --out <file.mp3> --work /tmp/render-NN-mX`
   (r02 calls the option --v120; keep --v120 as an alias).
2. Implement the critic's ranked plan (or say in NOTES.md why an item was not done), render both test inputs from
   TESTSET.md to r(N+1)/out-m1.mp3 and r(N+1)/out-m2.mp3, measure them, and write r(N+1)/NOTES.md: what changed and
   why (with web sources), before/after numbers marked [measured] or [inferred], what got worse, what is open.
3. Keep the processed MIDIs next to the script (rNN-m1.midi, rNN-m2.midi) for the critic.

## Each critic (N)
1. Read BRIEF.md (all of it, including Dan's priorities and timpani notes), LOOP2.md, TESTSET.md, HISTORY.md,
   rN/NOTES.md and the previous critic report.
2. Research on the web: orchestral mockup and MIDI-orchestration practice, mixing and staging an orchestra, sample-library
   documentation, free sample sets, acoustics. Cite URLs.
3. Measure rN on both test inputs with tools/ (and new scripts in critics/cNN/scripts/) against the reference
   recordings in assets/refs and against rN-1. Check Dan's three priorities (articulations, per-track volume, blend)
   and the timpani rules per movement, against the printed score (sections/*.ily of each test version).
4. Write critics/cNN.md: what improved, what got worse (measured vs inferred), accepted / rejected / open ideas, research,
   and a ranked plan for actor N+1. Append one dated entry to HISTORY.md in the same style as the earlier entries.

## Shared rules for both
- Do not change any score; never write into symphony/mvt1/ or symphony/mvt2/. Never delete files in /mnt/project-files.
- Software: only the base tools may be installed (apt: lilypond fluidsynth fluid-soundfont-gm; pip: mido numpy scipy
  soundfile matplotlib). Freely licensed data assets (samples, IRs, recordings) are fine; add them under assets/ with a
  line in assets/README.md (URL, licence).
- Disk: a render needs about 5 GB in /tmp. Run one render at a time; before starting, check `ps aux | grep render.py`
  and wait if one is running. Delete your own /tmp work folders when done. Never put WAV stems in /mnt/project-files.
- The shared folder sometimes has slow or failing I/O: work in /tmp and copy results back; re-read a file before editing.
