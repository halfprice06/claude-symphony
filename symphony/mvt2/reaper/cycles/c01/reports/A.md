# Cycle 1, critic A: articulation and phrasing

Under review: cycle 0 render (`cycles/c00/render/*.wav`) and `build/parts.json`. My scripts are in `/private/tmp/claude-501/mockup-loop/c01-A/`: `harp.py` (harp onsets), `an3.py` (slur-end articulations), `an4.py` (same-pitch overlaps), `env.py` (40 ms envelope of one track over a bar range), `f0.py` (time until the pitch reaches each legato target) and `delay.py` (silence after note-on for entries after rests). Bar numbers are score bars. Times are in quarter notes (qn) from the start, as in parts.json.

## 1. The harp's whole bass register is silent (Harp, bars 7-14, 37-44, 71-83)

What is wrong: `Harp Maestro.oib` has no sample groups below MIDI 48 (C3). I read every group's keyMin and keyMax from the .oib: they run from 48 to 103. The harp part runs from 27 (E flat 1) to 75. As a result 79 of the 175 harp notes play nothing, including every left-hand octave and every 8va-bassa bass note.

Evidence (measured): in `harp.py`, every chord whose notes are all below 48 adds 0.0 dB at its onset: bar 7 [A flat 1, E flat 2], 9, 10, 11, 13, 14, 37, 38, 40 and 42. The stem is digital silence (-120 dB) from 7 b1 until the right hand comes in at 7 b2, about 200 ms late. At 81 b1 [E flat 1, B flat 1] at f there is 1.3 s of silence. In bars 7-14 the harp therefore gives no bass under the horn theme, which critic 004 wrote in on purpose.

These patches cover the range (group ranges read from the files): `Harp Pluck Long.oib` 24-103, `Harp Sus RR.oib` 24-103 and `Harp Thumb Pick.oib` 24-103. `Harp KS Master` only reaches down to 36, and its keyswitches clash with the part's low notes.

Fix: in `tools/score_to_parts.py` `TRACKS`, change the Harp patch to `H + "02 Individual Articulation Patches/Harp Pluck Long.oib"`, or `H + "01 Maestro Patches/Harp Sus RR.oib"` for a fuller ring. The harmonics at 82-83 ("harm. (sound 8va)", notes at qn 273-277, already at sounding pitch 63-75 in the MIDI) currently sound as ordinary plucks. Put those six notes on a second harp track, "Harp harm.", with `H + "02 Individual Articulation Patches/Harp Harmonics.oib"` (range 48-96), and take them off the main harp track. Check on the render whether that patch expects written or sounding pitch (inferred: probably sounding).

## 2. The last note of every slur is re-attacked instead of slurred into (all slurred lines, about 160 slurs)

What is wrong: in `build_track`, `in_slur(q, e)` requires the note's end `e` to be at or before the slur's stop position. LilyPond's slur stop event sits at the start of the slur's last note (for example Ob1: slur -1 at qn 42 and slur 1 at qn 47, the onset of the last note E flat 5). So the last note never counts as slurred and gets `Sus MAX` / `Sus Non Vib`. A keyswitch back to Sus fires 0.06 qn before it, and the note before it gets no overlap, so the legato script never joins the two. Every slurred phrase ends with a fresh sustain attack on its final note, which is usually the note of arrival (cadence notes such as 10, 14, 16, 20, 34 and 60).

Evidence (measured, `an3.py`): the last note's articulation is Sus in 8/8 slurs in Flute 1, 8/8 in Oboe 1, 5/5 in Cor anglais, 5/5 in Clarinet 1, 5/5 in Bassoon 1, 7/7 in Horn 1, 26/26 in Violins I, 32/32 in Violins II, 21 in Violas and 22 in Celli. At the legato-to-Sus boundary the envelope dips further than at legato-to-legato joins: median -7.9 vs -6.0 dB in Vln I, -6.1 vs -4.2 in Vln II and -6.3 vs -3.8 in Violas (`an5.py`).

Fix in `score_to_parts.py`:
(a) Count a note as slurred if `a - 1e-6 <= q <= b + 1e-6`, where `b` is the stop position, so the last note gets the legato articulation.
(b) Apply `LEG_OVERLAP` only when both notes lie in the same slur span. Without this check, fix (a) would join back-to-back slurs into one long line.
(c) Where a new slur starts on the note right after a slur's last note, end the last note 0.05 qn early so the legato script sees a disconnected note and plays a new attack. That is the bow change or re-tonguing the slur marks.

Two related patch choices for strings (inferred):
- Unslurred, monophonic, connected notes of different pitch (the Vla/Vc/Vln accompaniment lines; the c00 parts have 60-86 Sus-to-Sus joins with no gap per string track) should use `Leg BC MAX` (bow-change legato). Its keyswitches are already in the KS Masters: Vln I 48, Vln II 45, Vla 42, Vc 88. The Basses KS Master has no BC articulation, so basses keep Sus.
- The slurred upper-cello answers at 18 and 22 (`c'8( es'8 c'4 des'4)` over the lower half's bass) are monophonic per voice but polyphonic per track, so they get Sus. Put them on `Celli Divisi/06 Keyswitch/Celli KS Master DIV A.oib` (Leg Slur) and keep the lower half on DIV B. A div. half playing a half-section patch is also the right size.

## 3. A legato note into a repeated pitch is cut off: the oboe's ff half note at the climax disappears (Ob1 62, CA 33, Bn1 33, Cl1 88, Vc 42)

What is wrong: the legato overlap extends a note 0.04 qn into the next one even when the next note has the same pitch. The old note's note-off then arrives 46 ms after the new note-on and stops it.

Evidence (measured, `an4.py` + `env.py`): Oboe 1 `f''1--( | f''2-- fes''2--)` at 61-62. The F5 at 62 b1 (qn 208, vel 91, ff) starts at -37 dB, falls to -55 dB within 0.2 s and is at -98 dB by the end of the half note. The tutti ff arrival loses its top woodwind line for two beats. The dip at the onset is -24 dB at Ob1 62, -18 dB at CA 33, -19 dB at Bn1 33, -23 dB at Cl1 88 and -33 dB at Vc 42.

Fix: in the overlap loop of `build_track`, skip the extension when `nxt[0]["pitch"] == n["pitch"]`. Instead end the first note 0.06 qn early and give the repeat its own attack (`Sus MAX`). This is also the right reading of tenuto under a slur (portato): Ob1 61-62, and Vln II 15-21 `aes'2--( aes'4--)`, where each repeat should be a gentle re-articulation inside one bow, not a legato join.

## 4. Legato transitions are too slow, worst in the viola triplets and violin lines

What is wrong: note velocities come from LilyPond's dynamics (41-63 at pp-mp). In the Legato patches velocity sets transition speed (HO manual, section 2.1.1 "Instrument programming": "timing between legato intervals is adjusted (tighter or looser) based on how hard or soft you play"). The patch's LegatoSpeed filter maps VELO_MIN 41 to VELO_MAX 127. Velocity 41 is the slowest setting, and the volume already comes from CC11.

Evidence (measured, `f0.py`: time from the MIDI onset until the pitch is stable within half a semitone of the target):
- Median legato arrival is 80 ms for Flute 1 and Cor anglais, 125 ms for Horn 1, 140 ms for Oboe 1, 200 ms for Violas, 235 ms for Violins I and 250 ms for Celli.
- Viola triplet eighths at 37-40 (vel 41, each note 333-373 ms long) take 210-450 ms to arrive. The transition fills most of each note, so the figure sounds smeared and late against the pizzicato bass.

Fix in `score_to_parts.py`: for notes with a Leg articulation, set velocity from the note's length in seconds (computed from the tempo map in parts.json), not from the dynamic. Suggested values: under 0.45 s, 100; 0.45-0.9 s, 80; over 0.9 s, 60 (expressive slow slur). Keep CC11 for loudness. Then measure again with `f0.py`. If strings still arrive more than about 120 ms late, move legato target notes (not the first note of a slur) earlier by the measured lag minus 40 ms: about -0.1 to -0.15 qn for strings, -0.05 qn for horn and oboe. The patches also map CC5 to "Legato Time" (controllerMap in the .oib) if the actor prefers a controller to velocity.

## 5. First notes after a rest start up to 0.6 s late, and some short ones never sound (strings, trombones, tuba, timpani, harp)

Evidence (measured, `delay.py`: silence until the stem passes -90 dB, for notes entered from digital silence):
- Woodwinds and horns start within 0-15 ms at every entry.
- Strings: Vln I 70.67, Vln II 70.67, Vln II 15, Vln II 37, Vla 15, Vla 37 and Vc 15 start 535-565 ms late. Vc 2 is 545 ms late, Cb 2 is 385 ms and Cb 21 is 245 ms. Vln I 17 and 21 are 180-240 ms late.
- Trombone 2, bass trombone and tuba at 60: 230 ms. Timpani 2: 545 ms. Timpani 84: 360 ms.
- Short first notes vanish completely. Vln I's E flat 5 eighth at 70 b3 is silent and the sound starts with the second note. Trombone 1's accented, marcato E3 at 63 b1 (the first note of its quotation, ff) is silent for 425 ms, so the accent is missing. The first viola triplet at 37 is missing.
- Other string entries start promptly (Vla 19 and 23, Vln II 45, Vln I 52.75 and 89: 0-25 ms). So this is not a constant attack time.
- The cause is unknown (inferred candidates: sample streaming or preload not ready during the offline render, or the strings' legato/attack scripting). Six of the eight 535-650 ms delays coincide with a CC15 (con sordino) change at the same qn as the note, but not all delayed entries have one.

Fix:
(1) In `score_to_parts.py`, never place a CC15 change on a note onset. Put it at the start of the preceding rest. The score puts the mutes on during the rests: CC15 at qn 42 belongs in bars 4-14, and the senza at qn 108 belongs in bars 31-36.
(2) Put every keyswitch at the start of the preceding rest when there is one, instead of `KS_LEAD` = 0.06 qn before the note.
(3) The actor should then render once more, or try REAPER's online (1x) render, and rerun `delay.py`. If identical delays remain, the patch itself is slow, and entry notes after rests in strings, low brass and timpani need moving earlier by the measured amount.

## 6. Breath marks, tenuti and accents are not rendered

What is wrong:
- Breath marks: `score_to_parts.py` ignores the event kind `breathe`. All 29 are played full length into the next note. That includes the seven winds breathing before the ff downbeat of 61 (Fl1, Ob1, Cl1, Cl2, Bn1, Bn2, BCl), the same at 81, and Hn1 at 10 b3 and 57/59. Measured: the note before each breath ends exactly at the next onset (gap 0).
- Tenuto: 77 marks, mostly the tutti chords at 61-62 and the Vln II portato at 15-21. They are ignored apart from the accidental same-pitch bug in finding 3.
- Accents: only Tbn1 has them (63-64, "marcato"). Its first accented note is silent (finding 5). On the second (C4 at 63 b2) the onset is -36 dB against a sustain of -35 dB, so there is no audible accent.
- Dan's rule is about 2-4 dB of weight with no click.

Fix in `score_to_parts.py`:
- For `breathe` at qn B: end the note sounding before B at `B - min(0.25, 0.2 * dur)` qn. Shorter notes than that keep 80% of their length.
- For `tenuto`: keep the full length but leave a 0.06 qn gap before the next note. Add a CC11 bump of +5 (about 2 dB) at the onset, returning over 0.5 qn.
- For `accent`: keep `Sus Accent MAX` only at f or louder. Otherwise use `Sus MAX` with a CC11 bump of +8 for 0.3 qn and velocity +10.
- Strings have no accent handling at all. None are printed now, so this matters only if the score changes.

Horn 3's "con sord." at 87 still has no muted-horn patch on the drive. The Solo, 2 and 6 French Horns Mutes folders contain only stopped horn (Stop Sus), which is a different sound. Do not substitute it.

Do not touch: the Leg Slur choice for slurred single lines and the polyphony check that keeps chords off legato patches (I measured 0 chord starts on legato patches); the 0.04 qn overlap for different-pitch legato joins inside a slur; pizz./arco switching from text (pizzicato onsets are clean, 0-10 ms); string tremolo and timpani roll keyswitch selection; the felt-stick timpani patch; clarinets on Sus Non Vib.
