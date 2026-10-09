# Critique of v9

Method: build log, `analysis.txt`, MIDI note dump around bar 126. Length 7:27.

## Changes from v8 (review points 2 and 5)
- **First-theme climax (bars 27–32) no longer repeats bars 15–18.** After the first ff statement, the head is sequenced up a step (A♭–F) over a bass rising C–D–E♭–E♮–F. A C7♭9/E chord tips it into F minor, the line peaks on a♭''' at bar 31, and it closes on a half cadence (c'''–b'' over G7).
- **The cadence elides into the transition.** The whole orchestra strikes C minor on the downbeat of bar 33 while the cellos begin the transition's motto entry, so the music no longer stops in bar 32.
- **Trumpets** hold sustained chord tones instead of off-beat eighths in bars 27–32 and 123–126. Flute 2 and oboe 2 hold chord tones instead of doubling the melody.
- **Recapitulated first theme (bars 123–126)** is now in cellos, bassoons, trombones and clarinets at the original pitch. The violins and flutes play a new syncopated counterline above it (e♭'''–d'''–c'''–b'', a♭''–f''–d''). The recapitulation therefore restates the theme in a new colour instead of repeating the exposition's tutti.
- **Cymbals removed** at bars 27, 123 and 130. The only crashes left are at the development climax (114) and the recapitulation's ♭VI (152).
- **Second-theme doublings:**
  - from bar 60 and bar 148 the second violins play the melody an octave below the firsts;
  - the clarinet keeps the countermelody alone;
  - the violas play off-beat syncopated chords in place of the unison doubling, in both the exposition and the recapitulation.

## Check results
- No build warnings.
- The analyser flags one octave at bar 126. The note dump shows the violins' a♭'' ends before the f'' that precedes the flute's g''. This is a false positive from the analyser counting a note that has just stopped, not a real parallel.

## Still to do (from the review)
- Development blocks from bar 103 to 122, and the identical A♭ climaxes (points 3 and 4).
- D1 rigidity (point 8).
- Coda (point 6).
- Introduction sequence and cor anglais (point 7).

## Plan for v10
Development: re-voice bar 114 as B°7 over the G pedal; shorten the wedge units; give the bass a chromatic line against the wedge; replace the scale at bar 122 with the motto in stretto over the timpani crescendo; overlap the D1 answers.
