# Movement I workspace

Movement I (Lento – Allegro appassionato, C minor) of Dan's four-movement symphony. Versions are `vNN/` folders; each holds global.ily, score.ly, full.ly, parts-gen.py, build-parts.sh, sections/*.ily, sections.txt, critique.md and the build outputs.

## Series so far
- v1–v20: composer drafts. Series 1: cycles 1–100 (v21–v120). Series 2: cycles 101–200 (v121–v220), book-based readings from cycle 107. Cycle 201: parts page turns (v221). In series 1–2, cycle N reviewed v(19+N).
- **Series 3 (Dan, 2026-10-19): cycles 221–420.** Cycle N reviews vN and produces v(N+1); the last cycle produces v421. Cycles 201–220 do not exist as numbers. Thread "Movement I, 200 more loops".

## Series 3 kit
- `critics/BRIEF3.md`: the brief every critic reads (four movements, coherence, books first, report format).
- `critics/LENSES3.md`: 10 rotating lenses; cycle N uses lens ((N−1) mod 10) + 1. Lens 9 compares with one master first movement from `critics/MASTERS.md`; lens 10 is cyclic design across the four movements and reads /mnt/project-files/symphony/coherence/.
- `critics/READING3.md`: the assigned book reading for each cycle (the movement II plan shifted to cycles 221–420; release checks at 320 and 420).
- `kit/critic_prompt.txt`, `kit/genprompt.sh N "focus"` → `kit/pN.txt`. The critic is a background `general-purpose` Agent whose prompt is one line: "Read your full task from <path>/kit/pN.txt and carry it out exactly."
- `kit/promote.sh NEW PREV SRC`: copies SRC into vNEW, labels the header "draft vNEW", builds (score.pdf, score.mp3, analysis.txt), rebuilds full.midi and the all-pairs parallels list vl.txt, and prints the diff against vPREV. Checks: build-warnings.txt empty, 18 PDF pages, only "bar 96: octaves F5->Bb2 over F2->Bb1", no new fifths or octaves in the vl diff except doublings.
- Parts: `bash vNN/build-parts.sh vNN` (run at least every 10 cycles and whenever a change touches the parts; parts crossing into movement II must end on an even page).
- Log: `vNEW/critique.md`, an entry in `critics/HISTORY.md` (Accepted / Open / Do-not-touch / Cross-movement), the report in `critics/reports/cNNN.md`.

## Where things live (series 3)
- The working copy is the git checkout of halfprice06/claude_composes (this thread's claude/ branch), pushed every 10 cycles as a backup. Project storage is nearly full, so only small text files go to /mnt/project-files: coherence/mvt1.md, coherence/themes-mvt1.*, this README, mvt1/CHECKPOINT.md and the latest version's text sources.
- Books: the PDFs in the repo's pdfs/ and the text in reference-books/text, linked together at /home/user/refbooks/ (recreate after a container restart: symlink every pdfs/*.pdf, reference-books/text and reference-books/INVENTORY.md into it).
- Container setup: `apt-get install -y lilypond fluidsynth fluid-soundfont-gm ffmpeg poppler-utils`; `pip install mido soundfile scipy numpy`.

## Coherence
Changes that affect another movement are sent to that movement's thread with send_message (old and new notes); coherence/mvt1.md and themes-mvt1.ly/.md are updated when such a change is promoted. Lens-10 cycles read the other coherence files.
