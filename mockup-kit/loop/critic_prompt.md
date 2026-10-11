You are critic {SLOT} for cycle {N} of the movement II REAPER mockup loop.

Read first: symphony/mvt2/reaper/loop/BRIEF.md (goal, files, rules), symphony/mvt2/reaper/README.md, and symphony/mvt2/reaper/loop/HISTORY.md (what earlier cycles changed and protected). All paths are under /Users/gooby/sandbox/claude_composes/.

Under review: the render of cycle {PREV}: symphony/mvt2/reaper/cycles/c{PREV2}/ (render/00_Master.wav, render/NN_<track>.wav stems, metrics/metrics.md and metrics.json, spectrogram.png, waveform.png) and the data that produced it (symphony/mvt2/reaper/build/parts.json, the tools, and any cycles/c{PREV2}/CHANGES.md).

Your lens: {LENS}

Work:
1. Study the score passages that matter for your lens (symphony/mvt2/v77/score.pdf; render pages with `pdftoppm -f N -l N -r 90 -png` and look at them; sections/*.ily give exact notes and marks; build/mockup-events.tsv has every mark with its position in quarter notes).
2. Measure. Use metrics.md, and write your own analysis scripts (numpy/soundfile/mido in ~/.venvs/claude-composes-reaper/bin/python, ffmpeg) on the stems and the master: per-note onsets and lengths, levels per bar or per phrase, spectra, the MIDI/CC data in parts.json. Compare with the reference recording where it helps. Use the HO/Opus manuals in guides/eastwest-hollywood-orchestra/text/ to check what the patches and controllers actually do, and the orchestration books in reference-books/ for balance and idiom.
3. Find the problems that most limit how real and musical the mockup sounds through your lens. Rank them by how much fixing them would improve what a listener hears.

Write your report to symphony/mvt2/reaper/cycles/c{N2}/reports/{SLOT}.md: plain prose, at most 6 ranked findings. Each finding: where (bars, tracks), what is wrong, the evidence (numbers you measured, score marks, manual pages), and a concrete fix the actor can implement in the tools or config (name the file and function, the parameter values, the patch file if a different patch is needed). Mark each judgement as measured or inferred. End with a "Do not touch" line for things that work and must be kept.

Rules: do not run ~/.rpr-bridge/rpr.py or touch REAPER, the bridge folder, the .rpp, build/, tools/ or any other report. Write only your report and scratch files under /private/tmp/claude-501/mockup-loop/c{N2}-{SLOT}/. Do not install software. Return a 3-6 line summary of your top findings as your final answer.
