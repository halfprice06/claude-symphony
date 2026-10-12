Movement II REAPER mockup: export for the score video
====================================================

Master audio: mvt2-mockup-c26.mp3
  Delivered master of mockup cycle c26, the last completed cycle of the actor-critic loop.
  The loop was stopped after c26. A c27 folder exists, but it holds only critic reports and
  no render, so c26 is the final master.
  Made by tools/render_cycle.py, which runs tools/deliver_master.py on the rendered
  00_Master.wav. The script applies a gain ride on quiet passages and a true-peak limiter.
  Result: -19.8 LUFS integrated, LRA 16.0 LU, -1.7 dBTP.
  Format: MP3, 48 kHz stereo, 192 kbps, 356.9 s.
  Timing: the 3 qn silent pre-roll was cut from the render, so 0:00 in the audio is score
  qn 0 (the downbeat of bar 1). The audio continues about 8 s past the final score qn
  for the reverb tail.
  Source: symphony/mvt2/reaper/cycles/c26/mvt2-mockup-c26.mp3 (local, not tracked in git).

parts.json: the tempo map REAPER played
  Copied from symphony/mvt2/reaper/build/parts.json. This copy is the state after the c26
  post-render fixes, so it matches the master above. Only note-level gain data changed
  during c26; the tempo and time-signature data are identical to the c25 copy.
  Fields:
    tpb          ticks per quarter note (384)
    tempo        [score_qn, bpm] steps, 418 entries
    timesig      [score_qn, numerator, denominator]
    end_qn       304.0, the last score qn
    preroll_qn   3.0, preroll_bpm 60: the pre-roll REAPER played before score qn 0
                 (cut from the audio; see Timing above)
    tracks       the per-player note, keyswitch and controller data
  Score qn values count quarter notes from the start of bar 1.

Score source: mvt2 v77
  mockup.ly includes score-defs.ily, which includes global.ily, sections/*.ily and
  parts.ily. parts.ily is not in the request but is included here because score-defs.ily
  needs it to compile.
  These files were compared with symphony/mvt2/v76, v77 and v78 after running convert-ly
  to LilyPond 2.26 on each. They match v77 exactly. The only difference is the
  "\version 2.26.0" line that convert-ly added to each section file. v78 differs in
  sections/bSec.ily: bassoon 2 rests in bars 53-56.
  The build copies were converted from LilyPond 2.24 to 2.26 for the local LilyPond.
  mockup.ly still declares 2.24.0.
