# One-time notes for the cycle 18 actor

The cycle 17 actor received item 1 as a message while it worked. Read `cycles/c17/CHANGES.md` first and skip what it already did.

## 1. Movement I c58 results (`symphony/mvt1/reaper-v621/cycles/c58/CHANGES.md`, `envelope_table.md`, `faults_table.md`, read only)

- Per-note envelope items 0 and fitted level rows 0 on every track (the 368 bar rows of c57 deleted, not refitted); points 6962 to 4515; strings 0.49-0.73 points/s.
- Theme over celli lower quartile +1.7 to +5.9 dB; pitches 4 dB out 23 to 7 (region gains refitted); Violins II repeated quarters +220 ms late to +9 ms.
- Accents by a flat CC11 value for the note's length: strings +2.6 / +1.7 dB at f / ff, winds +1.2 / +0.9, brass +0.9 / +0.5.
- Deleting rows fitted to old layers and fixing causes instead (roles, region gains, dynamic mapping) cost 23 master bars more than 1.5 dB up and 17 down against c57. The largest came from shapes with no instrument-side replacement yet (Cor anglais bar 7 -8.4, Horn 1 bar 111 -9.4, a solo cello that lost its shapes +3 to +4.7). Check the master per bar against the previous cycle after deleting role rows.
- Failed there, do not repeat: re-bow overlap on a second MIDI channel (channel 2 is silent in Opus); CC16 round-robin reset before every beat on the basses' eighths (no change); a soft-layer region gain on Horn 4 (F3 still 12 dB over G3 at p).
- Raising the no-split limit to 5.2 s removed 25 re-bows; 17 holes of 7-13 dB remain.
- Entry steps keyed to the moved note-on; role edges in rests or as 2 s ramps; role rows over fewer than three notes became flat CC11 offsets or were dropped.
- Scripts should not import from the temp folder: theme_S.py depended on a /private/tmp path that no longer existed after a four-day stop.

## 2. Movement I c59 critic findings (`symphony/mvt1/reaper-v621/cycles/c59/reports/A.md, B.md, C.md`, read only)

1. Accents measured on isolated accents matched on track, pitch, row and resting CC11: median +1.4 dB but quartiles +0.7 / +2.6, maximum +8.8; only 16 of 155 land in +1.5 to +2. One rule gives Violins I and II +3.8 and trumpets +0.5. Set the CC11 target per track and dynamic from each track's own CC11-to-dB curve. Family slopes are wrong (winds 0.07 dB per unit at CC11 88-104, horns 0.55-0.61 at 46-58).
2. Staff-count scaling of accents is not needed: when every track rises E dB the sum rises E dB; at onsets with 16+ accented staves the predicted rise of the stem sum was +0.3 dB.
3. sf handled as an ff arrival plus the accent rule stacks (+5.2 dB on Violins I): no accent value on an sf note. An fp spike held 57 ms left the note 13 dB under the one before.
4. A soft trim sized for one pitch's weak sample layer makes the neighbouring pitch 11 dB hot when that pitch's layer does not thin out (Horn 4 F3 against G3 at p). A pp region gain did nothing because the pp group is not what sounds at that CC11. Under test there: raise the soft CC11 (p 46 to 56) and cut the trim.
5. Solo level can follow the sample row, not the phrase: a solo cello had 15 dB between held notes at one CC11 (Leg Port MAX against Leg BC MAX). Row gains first, then one CC11 lane for the phrase.
6. Carry or role rows that held up a whole dynamic (Oboe 1 p/mp/mf lost 2.3-7.6 dB when they went) belong in the track's soft trims.
7. A 5.2 s no-split limit caused no pulse, but a 13 s single bow on Leg Slur MAX pulses at the 3.95 s loop period (autocorrelation +0.87, 11.4 dB range) where Sus MAX does not.
8. Held same-pitch repeats on strings must not take the repeated-note gap of 90 ms (32 joins, 9.5 dB median dips): about 0.03 s for held notes.
9. Hairpin gain is not the main source of envelope points; the dynamic-trim lane alone is 0.36-0.54 points/s on strings. Thinning tolerance 0.5 to 0.75 dB brings strings to 0.41-0.61.
10. Horn 1 B flat 4 is in anti-phase between L and R too (correlation -0.43 / -0.33, mono loss about 5 dB); no other horn pitch.
11. Upper-woodwind dry stems fall 24-39 dB within 0.2 s of a note end (strings 10-17.5, horns 11-14): range test planned there with the cor anglais Main mic raised.

## 3. Movement II c56 results (`symphony/mvt2/reaper-v600/cycles/c56/CHANGES.md`, read only)

These also apply to the cycle 17 render if a resumed actor does it.

1. Doubling held notes on idle DIV instances with interleaved bow changes: re-bow dip medians Violins I 6.2 to 2.3 dB, Violins II 8.1 to 4.6, celli 5.5 to 1.5. A CC11 lift at the new bow helped upper strings a little (violas 6.4 to 4.9) and deepened the basses' dips.
2. The Opus row volume knob (layerMatrix.rows[].volume) had no effect on a range pass there; row levels written as region volumes arrived within 0.3 dB (one bassoon pitch -2.7 for -3.5). Check that our row-level changes are region volumes.
3. Region-gain tables fitted per pitch made string, flute and second-wind lines worse in simulation: the hot celli notes are long notes, not pitches. Fit per pitch only where the pitch is the cause.
4. An envelope edge slew of 3 dB/s while the track sounds, with printed sudden steps moved to the led note-on: moves of 1.5 dB within 0.25 s inside a note 140 to 14 (unmarked 58 to 11).
5. Velocity 53 to 86 on oboe sustain heads changed nothing; CC11 was used. CC11 barely acts near the top on Trombone 1; CC1 carries its accents (aimed at +1.5 to +2.5 dB).
6. Bar 63 sf there: CC7 half-pairs left from the old envelope removed, tremolo row level as region volume, CC7 fall after the head: sf against the bar before -3.5 to +0.2 dB, monotonic fall.
7. REAPER reached 55 GB (41 GB compressed) after 17 full rebuilds in one run and the bridge stopped answering in a --midi-only job; a restart without save and a rebuild of the changed tracks recovered it. Restart between batches of rebuilds.

## 4. Movement II c57 critic findings (`symphony/mvt2/reaper-v600/cycles/c57/reports/A.md, B.md, C.md`, read only)

1. Bow changes: the string sustain patch loops only from 1.93 to 5.90 s, so a bow up to about 5.5 s cannot pulse; splitting at 5.6 / 5.0 s instead of the old limits removed 46 of 97 bow changes there.
2. A CC11 lift at a new bow that ends before the new bow speaks, with a pre-fall, deepens the hole: hold 0.30 s, return 0.55 s, no pre-fall.
3. A CC shape keyed to the moved note-on is half gone at the beat when the lead is 120-300 ms: hold soft-entry shapes (and check accent shapes) to score onset + 0.15 s.
4. Legato velocity 84-108 fits the references, but by the patch's LegatoSpeed table it delays violin transitions 25-45 ms (violas 13-22, celli 15-27) unless leads are corrected. Bursts do not depend on velocity.
5. "Long notes over short ones" in legato lines is short slurred notes reading 2-4.6 dB low: a 6-12 dB dip for 0.25-0.4 s after each slurred note-on that the old early fills covered; its depth does not depend on CC11.
6. Timpani level split between CC7 and a fader rule that switch at different times caused 10 of 14 remaining moves inside notes: one CC7 lane for the whole envelope.
7. Fitted section rows sorted by cause (117): 33 under 1 dB (delete), 21 covering one or two notes, 20 sample level (region gains), 22 unexplained of which 13 are ff cells with one sign per track (move into the ff dynamic trim), 16 bar means of removed shapes, 5 phrase decisions (roles).
8. A sustained bass pedal (A flat 1) pulses every 1.3 s inside the sample, 11-12 dB on the stem; no tested instrument-side fix yet.
9. DIV copies used for doubling are Close-only and mono: doubled pairs are 1.7-3.0 dB narrower (L/R correlation 0.5 to 0.71-0.78); no comb, bump or pulse at overlaps. Check our last G sharp doubling for width.
10. Horn 1 and Horn 3: B flat 4 and A flat 4 have whole-note L/R correlation 0.14 and 0.01 (fundamental of A flat 4 at -0.73). A flat 4 is our G sharp 4.

## 5. Finale c18 techniques 76-80 (`symphony/mvt3/reaper-v600/loop/SHARED-TECHNIQUES.md`; code in its `tools/instr_post.py`, `cycles/c18/actor_scripts/guard18.py`; read only)

76. Accents after Dan's "over done": bump about half (strings +8 / +10 CC11 units at f / ff, woodwinds +7 / +10, brass 6-10 % of the resting CC11), from 0.03 s before the note-on, held 0.06 s, back by 0.22 s. Medians +2.3..+2.8 to +1.0..+1.3 dB; master front at 16-stave accents +2.0 to +1.1 dB. The 11-16 % of accents still 5 dB out are sample level by pitch.
77. Fader guard at 3 dB/s (1.5 dB or more inside a sounding note): slow the hairpin-gain release at the source (2.8 dB/s), leave moves under printed hairpins, fast ramps only across running notes, and move a passage level whose edge falls on a held note with no rest into CC11 as a factor (10^(dB/40) on brass / clarinet volume). 74 to 4 moves, role rows 267 to 137, 7 master bars moved 1.5 dB or more.
78. sfp on sustain rows: start the fall 0.22 s after the mark (0.10 s leaves no sf), CC11 +10 from 0.03 s before the note-on, hold the p with a ceiling on the dynamic lane ending at the printed arrival: front level with the ff before, p 11.8 dB down.
79. Region volumes by row group: oboe "Sus MAX" C5 / E5 / F5 from -4 / +9 / +11 dB to within 2 dB; pizzicato basses at flat velocity plus a pitch table 8.9-13.4 to 3.7-6.4 dB peak range.
80. Negative: "Sus MAX" strings lose 0.7 dB per CC11 unit under 100 and are flat above 103 (an offset of -10 from 105 cost 7-11 dB). Spreading wind / brass breaths and tying the pedal over two bars did not change chorale bar-line dips (the dip is each new whole note's slow start). A pitch table does not even out pizzicato celli (5 dB between round-robin samples of one pitch). A pizzicato velocity table across 41-85 crosses a layer step of 8-13 dB (our celli pp pizzicato change to velocity 52 sits at such an edge: measure it).

## 6. Finale c19 critic findings (`symphony/mvt3/reaper-v600/cycles/c19/reports/A.md, B.md, C.md`, read only; a colleague's findings to test)

1. Bar-line dips in sustained wind and brass writing (2.3-5.3 dB in the master): the minimum lies 10-90 ms before the bar line. Every wind and brass whole note has a 35-90 ms silence there (note-off 95-155 ms before the bar line, note-on 50-90 ms before, rise 80-135 ms), and woodwind / trumpet dry stems fall 16-49 dB within 0.2 s of a note end. Plan there: old note ends 0.03-0.05 s after the new note-on at joins that change pitch (polyphonic sustain rows), 0.02-0.03 s gap in staggered groups at same-pitch joins, leads sized to each track's rise time (Oboes 0.18-0.20 s, Trombone 1 0.19, Horn 1 0.13, basses 0.18).
2. Tutti entries after a rest spread over a median 148 ms because the same tracks always speak first (leads set early and never re-measured): measure half-rise per track at chords of 8+ entries.
3. Accents by a short CC11 bump (0.22 s) are over before brass rows speak (matched +0.2 to +0.5 dB) and before the beat when the lead exceeds 0.22 s. Our c17 accent shape is 0.06 + 0.20 s from the moved note-on: check brass and led notes.
4. Horn Main mic pair: B flat 4 anti-phase on Horn 1 (correlation -0.68, mono loss 7.7 dB) and Horn 3; L-R level also shifts by pitch (D4 +7.9 dB). Test: Channel Routing "Mono From Left" (manual p.141) or Close 0.85 / Main 0.55.
5. A rule-off switch failed because the rule's tag differed from the name the switch keyed on: check tags when a switch has no effect.
6. Basses' hammered eighths sound as one late pulse per quarter: the 80 ms note is released 30 ms before the stroke's own peak; test length 70 % of the slot and lead 0.075 s.
7. Cello pizzicato unevenness is per sample of one key (7-9 dB), not per pitch.

## 7. Movement I c59 actor findings (a colleague's findings to test)

1. On Horn 4 the sample layer follows CC1, not CC11: remapping CC11 alone could not change the layer; both lanes were remapped.
2. A CC11 offset sized from a family slope overshoots (+8 units gave +6.5 dB on Horn 1; -5 dB asked gave -9.5 on Clarinet 1): use the track's own curve and range-test. Our Horn 1 CC11 +11 from qn 1100.7 is such an offset: measure it.
3. REBOW_NONE over a span also removes printed bow changes; unlist the automatic points instead.
4. Hairpin gains could not be moved into CC11 cheaply in Movement I's build (built after the CC11 lane).

## 8. Movement I c60 critic findings (`symphony/mvt1/reaper-v621/cycles/c60/reports/A.md, B.md, C.md`, read only; a colleague's findings to test)

1. Climax order changed when the level rows went: an ff tutti became louder than both fff climaxes (strings rose 3-5.6 dB at ff; positive rows at the fff were converted to CC11 offsets on a lane already at 124, where nothing plays; the instruments give only +1.3 dB median from ff to fff). Check the momentary-loudness order of the printed climaxes after every removal. Fix there: lower the ff dynamic trims, keep fff, keep positive rows at fff as slow role rows.
2. A role turned into a CC11 offset costs far more than its dB near the top or bottom of a curve (-4 dB asked became 125 to 99 = -7.8 dB on Violins I).
3. "Fitted rows 0" by rule name missed two fitted LEVEL_SHAPES rows in the config and a timpani rule that adds +6 dB on each loud stroke and removes it over 0.75 qn. Search the config tables, not only the rule dump.
4. Hairpins are carried by the instrument (stem rise +6.8 dB median, fader +0.4), but the dynamic trim steps at the end of a printed hairpin and works against 84 crescendos by 1 dB or more. The trim should ramp across the hairpin. 26 diminuendo ends undershoot the arrival dynamic's CC11.
5. Re-bow dips do not show in the master at automatic changes (2.8 dB against 2.6 at control times); only at exposed printed changes and the final chord. Half the "holes" are printed same-pitch repeats whose fault is timing (lead 0, body 365 ms after the beat). Pieces up to 5.3 s cannot pulse.
6. Sustained wind and brass chord changes: every brass long note ends 90 ms before the next note-on (winds 50 ms); the wind-and-brass sum dips 3.3 dB at tutti changes, master 2.4 dB. Under test: old note ends 0.03-0.04 s after the new note-on on long notes. (Our brass gap floor is 0.09 s since c16: check it against this.)
7. Fast bass eighths: every stroke sounds but peaks 74-90 ms late because the note is still rising at its note-off; a longer lead (0.12 s), not a longer note.
8. Single accents of +5 to +9.6 dB were not sample level: three carried a printed ff after f, two sat inside a crescendo, the rest are legato-row scatter. Exclude those from the accent measure.
9. A simulated 3-5 dB decay on static long notes at f and above changed nothing against the recording. Not worth building.
10. Tutti entries: Oboe 2 first in 11 of 13 chords (lead 180 ms, 77-160 ms early), matching the finale.
