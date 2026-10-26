# v326 (cycle 325, lens 5, Adler PDF 282–301 score layout; MIDI rolls)

Report: critics/reports/c325.md.
- MIDI: timpani rolls now play as repeated strokes (they were one held stroke, so crescendo rolls could not grow). score.ly wraps the orchestra in a music function taking the timpani music; the MIDI-only score passes the timpani through \rollStrokesByBar, which applies the scherzo's shared rolls-midi.ily \rollStrokes to each roll only (applying it to the whole score would turn the string tremolo into notes). rollStrokeTable gives 11–23 strokes per second. Only the timpani track differs (172 → 1002 note-ons); print unchanged by this change.
- Brass family sub-brackets for horns, trumpets and trombones inside the brass bracket (Adler PDF 293–294), as in the scherzo. Breaks unchanged.
- 224, 226: the bowing text "unis., change bow at will" on three lines and the lower strings' text shifted, so they no longer cross the barline (Gould PDF 41, 55).

Build: 0 warnings, 0 parallels, 16 pages, theme record: 41/41 unchanged.
