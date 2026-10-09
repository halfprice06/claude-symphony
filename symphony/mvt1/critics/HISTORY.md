# Critique history (newest last)

## Before the subagent-critic series (v05–v20, composer's own critiques plus two subagent reviews)
Full notes are in each vNN/critique.md. Summary of what was settled:
- v06–v08: all exposed outer-voice parallels removed. Transition sequence fragmented. Second theme opening rewritten so it rises by sixths (answering the motto). D3 in B♭ minor.
- v09: first theme climax (27–32) varied, elided into transition; recap first theme reorchestrated (low instruments + violin counterline); cymbals limited to dev climax and recap ♭VI.
- v10: development D1 dialogue overlapped; wedge with chromatic bass; dev climax B°7 over G pedal; retransition motto stretto.
- v11: coda rewritten (themes combined, motto augmented, ends C minor with violas E♭→E♮).
- v12: cor anglais answers the motto in the intro; intro sequence compressed into the German sixth; E♭7 dominant before the second theme shortened with a cadential bass.
- v13: dominant build in the development rises to a♭''' at the climax (bar 114 at the time).
- v14 (review 2): first theme second phrase peaks on a held d♭''' (Neapolitan); German sixth resolves on the downbeat.
- v15: second theme continuation now leaps an octave instead of sagging chromatically; recap version uses the motto's minor sixth.
- v16: forte codetta (69–72) combining both themes closes the exposition.
- v17: recap restores the first theme's second phrase and peak (4 bars added); coda opens with 4 bars of forte C minor.
- v18: fugato bass doubling removed; D3 doublings thinned; timpani reduced to four drums (G, A♭, B♭/C, E♭).
- v19: faster harmonic rhythm at the second theme climax (60–63); viola and cello figures varied there.
- v20: engraving cleanup.
Rejected so far (with reasons in v17/v18 critique.md): a canon in the coda's opening (parallel fifths), motto rhythm in trumpets under the tuttis (doubles the melody), equal dynamics for horn and cello doubling (balance).
Known open issues listed in v20/critique.md.

## Subagent-critic series

### Cycle 1 (v20 → v21), lens melody. Report: reports/c001.md
Accepted all: motto's slow statements reordered away from Tristan (G–E♭–D–C–D♭–C); recap ♭VI climax now peaks on a♭'''; exposition bar 63 rises; codetta carries the second-theme head on top; flute b''' removed from bar 26; second-theme bars 3–4 now a rising arpeggio + 4–3 suspension in all appearances.

### Cycle 2 (v21 → v22), lens harmony. Report: reports/c002.md
Accepted all 7: false relation at 157 removed; doubled resolution notes fixed (14, 28, 50, 59, 106, 124, 170); D3 (97–102) moved to B minor by direct semitone shift (no F♯7 preparation, because the motto descent above clashes); inner-voice parallel fifths fixed (83, 114, 155–156, 165, 177–178); bars 7–8 bass holds C; 13th at bar 42 resolves; restatement 56–57 over A♭ pedal with chromatic inner voices. Critic 2's all-voice analysis scripts: tools/critic-scripts/ (they need a MIDI with one track per instrument).

### Cycle 3 (v22 → v23), lens form. Report: reports/c003.md
Accepted all 6: only one fff after the development (156); bar 132 to ff and flute b''' at 130 to b''; brass held through 158; retransition crescendo from 119; coda cut to 16 bars with violin stretto over the augmented motto and timpani pulse in the Lento (Lento now at 175); vln II F♯3 at 97 removed; fugato 2nd entry to violas + bsn 1; headers fixed. Movement is now 178 bars (coda 163–178).

### Cycle 4 (v23 → v24), lens orchestration. Report: reports/c004.md
Accepted all 6: violas carry a third octave of the T1 tutti (27–32, 163–165) with hn 3·4 + tpt 3 at f (tpt 2 must match tpt 1 because they are part-combined); violas + cellos carry the tune at the ♭VI climax 154–157; harp out of the low register and silent 154–157; trumpet 1 on the codetta tune with low brass at mf; coda 166 to ff; cor anglais doubles vln II in D3.

### Cycle 5 (v24 → v25), lens engraving. Report: reports/c005.md
Accepted all 8, with variations: partCombineApart in tutti woodwinds; hairpins closed on notes; duplicate dynamics fixed by moving Dynamic_engraver to Staff level in score.ly, not by editing assemble.py (Dynamic_align_engraver must stay in Voice: moving it caused 280 programming errors). With this setup, different simultaneous dynamics on a shared staff give a conflict warning and one is dropped, so keep pairs equal. RemoveEmptyStaves; one named percussion staff that hides when empty (not split into two); boxed rehearsal marks A–L; tempo words fixed; breaks before 47/77/139/163; no ottava on the shared flute staff; horn 3·4 bass clef at 11–12.

## Cycle 6 → v26 (playability)
Accepted: Cb arco 90; staggered breaths in all held pedals (dev 109–118, B-minor block, recap Bsn 2, tTwo horns); Hn1 high f'' handed to Cl1 (52–54, 144–145); harp spellings 63–64 and pedal markings; div./unis.; violin bowings split at 55–68; timpani tuning instructions; bass clarinet octave at 92–96.
Rejected: Hn4 rest 127–130 (not needed after dev breaths); critic's harp pedal string (wrong).

## Cycle 7 → v27 (texture/counterpoint)
Accepted all: fugato 91–95 rebuilt with Vln II entry, Vla on countersubject, Vc as a free third voice; Hn1·2 double the ♭VI countermelody 154–157; Cl1 counter moves at 62–63, 66–67, 160–161; recap 123 counterline des''' (no augmented octave), Fl2 124 c''2 d''2; coda Vla 170 es'2 d'2.
Do-not-touch list from critic: hemiola 23–26; Hn/Bsn/Tbn counter at 97–102; layering 109–113; codetta 69–72; motto canon 171–177.

## Cycle 8 → v28 (expression)
Accepted: mf/mp cresc. restart at dev 103 and f< at 131 (low brass stay f); internal tempo words (poco rit. 45, rit. 66, allargando 113/a tempo 115, poco rit. 137, rit. 161, allargando 166, rit. 173); phrased second theme 46–52 with swells, Hn mp at 138; first theme slurs and peak at 20 (also recap 123–126 and coda 163–166, not trombones); motto hairpins; brass one level softer at 12, 131, 163; largamente 97/154, espr. 73, morendo ppp ending.
Not fixed: Hn3·4 bar 84 "decrescendo too small" warning (cosmetic).

## Cycle 9 → v29 (holistic, Tchaikovsky 6/i and v18)
Accepted: flute 100–101 down an octave (no B6 peak outside the climaxes); Hn1 bar 28 f' (no m2 under Tpt1); Tbn1 and B.tbn pp on the augmented motto 171–175.
Open: F♯ arpeggio at 102 slides to F at 103 without resolving.
Do-not-touch: second-theme hairpins 47–52; V–♭VI climax 154–158; plagal tonic-pedal coda opening 163–166; motto canon 171–177; viola E♭→E♮ ending.

## Cycle 10 → v30 (cyclic design / emotional arc)
Accepted: E♮→E♭ turn with crescendo on beats 3–4 of bar 162 (Vln II/Vla sync, Cl1 counter, Hn1, cello arpeggio, timp roll on C) so the coda's C minor is prepared; cor anglais (not Hn1) answers the cello with the motto at 167–170.
For later movements: open mvt II by letting the final E♮ fall to E♭; mvt III chorale uses intro motto form in major (G–E–D–C, cf. 147–148).
Do-not-touch: E♭/E♮ pivot 8–9 and 177–178; violins' major motto 147–148; second theme key chain A♭/Bm/C/Cm; flute A♭ motto 73–76; augmented motto 171–175.

## Cycle 11 → v31 (melody)
Accepted: second-theme ending 64–68 and recap 159–161 rebuilt from the theme's own figures (dotted rise of 49–50, falling line of 53); bar 102 beat 4 c'''8 g''8 (lands on G♯=A♭ of 103) in all doublings.
Cycle 1 fixes judged successful.
Do-not-touch: first theme sentence 15–22; intro violin leaps 9–12; second theme 47–55; codetta 69–72; climax 154–157.

## Cycle 12 → v32 (harmony/voice leading)
Accepted all 8: bar 96 fifths removed (lower line a third below); 123–124 Tpt1/Hn3 no longer sound resolution notes against suspensions; 156 counterline es'4 c''4 resolves the V7's 7th; 42 Hn1·2 c'4 bes2.; Hn4 rest 66, Tpt2 a♭' 70, Tpt3 f' 132; Vla 169 c'2 des'2; Cb/harp follow Vc D at 64; cello arpeggio tops at 67/161 end on the 7th.
analyze.py now reports fifth runs (only octave runs ignored).
Do-not-touch: Ger6 into V 12–13; chromatic bass 27–32; plagal coda opening 163–166; iv–N6–i6/4–V 168–170; V–♭VI 155–156.

## Cycle 13 → v33 (form/pacing)
Accepted: bar 82 bass to A♭ (i–VI–V7♭9, no tonic feint at the development's start; I changed held G to A♭ in Hn1/Tpt2/Vla to avoid an ff A♭maj7); recap 127–130 hemiola rebuilt from mf/mp; tam-tam alone at 114, cymbal kept for 156; "largamente" removed at 97; sostenuto 115, a tempo 119.
Do-not-touch: proportions; medial caesura 41–43 and fill 43–46; G-pedal 109–114; augmented motto stretto 171–175; E♮→E♭ turn 162.

## Cycle 14 → v34 (orchestration)
Accepted: Hn1·2 double the tune at 154–157 (reverses cycle 7; counterline now Ob2+Cl1 with the cycle-12 E♭ at 156); Hn1 doubles Cl1 counterline 56–68 and 148–151; coda cor anglais motto an octave up (167–170); Vln II/Vla join T1 head at 82; Tpt1·2 f at 27–31 and 163–165, ff at 32/166.
Note: the 154–157 counterline has now been argued both ways (cycle 7: brass needed to be heard; cycle 14: horns blur the tune's bottom octave). Don't flip it again without new evidence.
Do-not-touch: horn+cello second theme over harp 47–55; motto layering 109–113 and tam-tam 114; augmented motto 171–175; Tpt1 codetta tune 69–72; viola third octave 27–32.

## Cycle 15 → v35 (engraving)
Accepted all: Dynamic_align_engraver moved to Staff (dynamics were printing on noteheads since v25; DrumStaff consists line removed); harp pedal names 51–66, bar 56 F♭; flute ottavas removed on shared staff 41–43, 71–72, 113–115 (keep 98–100 where Fl2 rests); duplicate dynamics at 27/69/109/131/163 removed; "1." at oboe 148 and horn 47; expressive words italic; breaks before 15 and 167; rehearsal letters skip I (J follows H); bar numbers font -1, padding 2; harp final fermata.
Rule for future edits: never put \ottava on a shared (part-combined) staff where the other player sounds.

## Cycle 16 → v36 (playability)
Accepted all: counterline doublings 56–68/148–151 moved Hn1→Hn2; violin bowings 97–102 by phrase; Vc/B.cl slurs 171–175 split; breaths Ob1 152–153, Fl1 enters 152, Cl2 108/115, Bsn1 108/116; Hn1 143–144 cello octave; Hn4 rests 127–129; harp 64–65 no D pedal change; B.cl "(low C instr.)" at 92.
Note: cycle 6's rejection of a Hn4 rest at 127–130 was overturned with an endurance count (152 quarters without lip rest).

## Cycle 17 → v37 (texture/counterpoint)
Accepted all 6: recap 148–151 viola eighth-note fills (not a copy of exposition syncopations); fugato 93–95 viola free voice e'–f'–g♭'; transition 37–39 viola imitation; 97–102 viola inverted arpeggio; 131–134 viola turn figure; intro 10–11 Vln II rising-sixth echo.
Open: coda 163–166 cellos only double the bass C eighths (could get a tenor line as at 27–31).
Do-not-touch: fugato 85–93 with free cello; layering 109–113; motto canon 171–177; theme low with counterline above 123–126; hemiola 23–26.

## Cycle 18 → v38 (expression)
Accepted all: recap second-theme phrasing 139–158 matches the exposition; counterline 56–68 grows with the violins, Hn3·4 pad mp, Ob1/Fl1 slurred; final chord all ppp; coda cello phrase 167–170 espr. with pp accompaniment; timp ff→ff crescendos fixed (132, 165); fugato crescendo 95–97, Cb graded; harp hairpin 152 closed; Vc/Cb mf at 23; Cl1 dim 53–54; Ob1 p 136; Fl1 hairpin 113; Fl1 mf at 11; Bsn mf at 37.
Do-not-touch: swells 47–55; cresc. wedge 103–109; sul tasto→ord. 139–147; graded brass 12, 27–32, 131, 163; E♮→E♭ turn 162; morendo viola ending.

## Cycle 19 → v39 (holistic, Dvořák 7/i and v28)
Accepted all: retransition 119–122 cello measured accelerando (quarters→16ths) on G; 16th turn at 40 in Vln I/Fl1/Ob1; Cb pizz. under 47–55 and 139–147; coda 163–166 cello tenor line.
Noted, no action: Tpt1 at 123 now g' (weaker than c''); 97–102 viola arpeggio in clarinets' register. Score now 18 pages: check breaks.
Do-not-touch: 123–134; climaxes 114/156; codetta 69–72; endings 64–68/158–161.

## Cycle 20 → v40 (cyclic/emotional arc)
Accepted: Tbn2 inner voice at 171–175 (pp three-part chorale on the augmented motto, planting mvt III's chorale sound).
Verdicts: second theme memorable enough (head heard 10×, planted at 13, 41–44); keep 47–55 as written. Notes for mvts II/III in /mnt/project-files/symphony/cyclic-notes.md.
Do-not-touch: E♭→C sixth plantings 13, 41–44, 46–47; second-theme head rhythm in every appearance; minor-sixth head 97–98, 167–168; E♮/E♭ frame 8/162/178; CA motto 167–170; ♭VI thread 82/114/156; 47–55.

## Cycle 21 → v41 (melody beyond the main themes)
Accepted all 3: Ob1 dolce sixth g'–e''–d'' at 137–138; second-theme continuation figure at 106 in the wedge; head-rhythm sigh at 116–118 (Vln I, Ob1, Fl1).
Judged fine as is: transition top line 33–46 (motivic, like the models); wedge 103–108; post-climax scale 113–115; counterline module.
Do-not-touch: transition imitation 35–40; wedge 103–108 (apart from 106); climax 114–115; motto dialogue 77–83; coda top line 163–178.

## Cycle 22 → v42 (harmony/voice leading)
Accepted all 6: 106–108 inner fifths removed (Fr6 then A); 101 suspension clashes removed; 148–149 tonic pedal; 40–41 viola twelfths; 69–70 Tbn1 f'2 des'2; 146 violins with the melody.
Open: second-theme groups use one-chord-per-bar root-position I–IV–ii–V repeatedly; possible variation: G pedal at 160 (untested).
Do-not-touch: Ger6 12–13; chromatic bass 27–32; V–♭VI 155–156; iv–N6–i6/4–V 168–170; trombone chorale over C pedal 171–178.

## Cycle 23 → v43 (form/pacing)
Accepted: bass to V on beat 3 of 66 and 160 (4–3 suspension over six-beat dominant before EEC/ESC); "Tempo dell'Allegro" at 69; "poco più tranquillo" at 73 as a word only (no 108).
Open: A♭6 top note seven times (25, 31, 72, 114, 129, 132–133, 156) — 156 lacks registral exclusivity.
Do-not-touch: proportions; MC and fill 41–46; A♭ crash 82; two-wave 123–134; retransition 114–122; E♮→E♭ 162; coda 171–178; intro length.

## Cycle 24 → v44 (orchestration)
Accepted all: 154–157 flutes a2 and Vln I+II unison on top, Cb to G1/A♭1 (156 peak by weight, closes cycle 23's registral note); Bsn1 solo motto at 77; tam-tam pp at 171; susp. cymbal roll 155 into crash 156; Cb rests 167–170.
Do-not-touch: tam-tam alone 114; horn+cello second theme over harp 47–55; CA answers 139–147; Tpt1 codetta 69–72; augmented motto 171–175; Hn1·2 tune doubling 154–157.

## Cycle 25 → v45 (engraving)
Accepted: explicit part-combine modes at 80–82, 109–112, 123–126, 153–156; cello tenor/treble clefs 47–55, 139–147, 167–170; \pageBreak before K with page-count 17; marks/tempi also above Vln I; tam-tam labels and l.v. ties; "1." on flute solos 39 and 77; ottava at 40 removed; "largamente" in global at 156; 163 tempo text "Tempo dell'Allegro".
Open: bar numbers collide with high flute notes at 27–29, 109–112, 123.

## Cycle 26 → v46 (playability)
Accepted all 6: violin bowings 154–157 and 63–64; Tbn1/B.tbn rests 103–105; Ob1 rests 135–136 before the 137 solo; staggered horn rests 158–161; breaths Bsn2 62/68, B.cl 105; tam-tam player number.
Checked fine: Vln II A♭6 at 154–157 (within Vincent's A6 limit); Cb G1/A♭1; percussion changes; timp C for 163.

## Cycle 27 → v47 (texture/counterpoint)
Accepted all 3: new chromatic recap counter 148–151 (Cl1, Hn2); Hn3 joins the counterline 154–157 (Hn1·2 stay on the tune); cello arpeggio descends at 149–150.
Noted for later movements: ff octave tutti over repeated bass eighths used 5× (27, 69, 123, 131, 163).
Do-not-touch: sul tasto tremolo with CA fills 139–147; fugato 85–96; layering 109–113; trombone chorale 171–178; low theme with counter above 123–126.

## Cycle 28 → v48 (expression/articulation)
Accepted all 8: one articulation for the motto head (slurred) except marcato places 82, 85–96, 109–112; hairpins into fff in 155; two-bar wind slurs 97–102; slurs/tenutos in the wedge 103–107; bass hemiola accents 23–25, 127–129; Ob1 p over pp at 137; tenuto on leap note 57, 149, codetta 69–71 phrased; hairpins 113 aligned; Tbn dynamics equal at 105.
Do-not-touch: graded brass 12, 27–32, 131, 163; swells 47–55; sigh 115–117; staggered brass dim. 158–162; tam-tam pp 171; morendo viola ending.

## Cycle 29 → v49 (holistic, Dvořák 9/i and v38)
Accepted all 4: coda 163–166 brass (Tpt1·2, Hn1·2 a2) take the head over violin tremolo chords, winds sustain (revises "graded brass 163" for those four parts only); trumpets in timpani rhythm at 27, 28, 30; Tbn2 E♭ at 156 (chord fifth); tenutos removed at 107.
Do-not-touch: intro prefiguration 9–12; oboe G–E pivot 137; B-minor theme with T1 tail 97–102; augmented trombone motto 109–114; V–♭VI–ii–V–vi 154–158; cello theme vs CA motto 167–170; chorale and viola E♮ ending 171–178.

## Cycle 30 → v50 (cyclic/arc/surprise)
Accepted: fermata on the rest at 166 in all parts (denied tutti made audible).
Open: 139–147 attention risk (protected); MIDI accent velocities make 166 louder than 156 in the MP3 — don't judge the climax hierarchy by the MP3.
Do-not-touch: brass coda opening 163–166 with vii°7 at 166 rhyming with 26/130; cello vs CA motto 167–170; trombone chorale + tam-tam 171–175; E♮→E♭ 162; viola E♮ ending.

## Cycle 31 → v51 (melody/tune clarity)
Accepted: 32nd-note scale into f'' at 144 in Vla and Vc (third-hearing variant; exposition keeps the plain leap). cyclic-notes.md citation corrected.
Note: rising sixth saturated (45× in Vln I); the 156 peak depends on register, cymbal and harmony — don't weaken them.
Do-not-touch: T1 sentence 15–22; second theme 47–55 with plain leaps; ♭VI climax 154–157; B-minor statement 97–102; violins' final motto 173–178.

## Cycle 32 → v52 (harmony/voice leading)
Accepted all 4: 166 Hn4/Tbn2 hold A♭ (Tpt1 keeps B); 28 Tpt1 b' on beat 3; ii6 on beat 3 at 58 and 150; 151 viola fill avoids B under the C suspension.
Verified: cycle 28 changed no notes.
Do-not-touch: beat-3 dominant with 4–3 at 66/160; 154–158 climax with Tbn2 E♭; 148–149 counter; cadence 168–170; trombone chorale 171–178.

## Cycle 33 → v53 (phrase rhythm/pacing)
Accepted: ff tutti quarter chord at 135 eliding the recap first group into the bridge; allargando at 166 removed (fermata suffices).
Do-not-touch: 3-bar fugato spacing 85–96; one-bar cadence suffixes 55, 68, 162.

## Cycle 34 → v54 (orchestration/colour)
Accepted all 4: Ob1 rests 94–96, flutes rest 103–106 (fresh colour at 107/114); ff chords at 33 and 135 cut to accented eighths; div./unis. in violins 163/167/173; Cbsn C1 under 163–166.
Noted for later movements: oboe doubles moving Vln I in 73% of bars (models 2–3%); leave more violin lines undoubled.
Do-not-touch: 47–55; 139–147; 154–157 scoring; brass head 163–166.

## Cycle 35 → v55 (engraving)
Accepted: rests `r8 r4 r2` after eighth chords (33, 97, 135, timp 127); bar numbers below the system (Cb staff, centred); hairpins into fff at 113–114, tuba attacks 114; one 8va bracket Vln I 40–41; flute espr. below p at 73; harp ppp at 178.
Rejected: removing the restated ff at 135 (restatement after an elision chord is normal).
Do-not-touch: rehearsal/tempo marks above Vln I; part-combine modes; divisi scheme 103–119 and 163–173; K page break with page-count 17.

## Cycle 36 → v56 (playability)
Accepted all 4: timp "muta C in B" at 84; breath at 162 for Fl1, Ob1, Bsn1; Hn3·4 bass clef 23–26; BCl slur split in bar 2.
Not applied: optional Hn4 rest at 122.
Verified fine: ranges, 163–166 brass, cello 119–122, scale 144, chorale, harp pedals, timpani, bowings, endurance.

## Cycle 37 → v57 (texture/counterpoint)
Accepted all 3: viola espressivo counterline 19–22 (Vln II takes syncopations; Vc/Bsn f–A♭ in 19); clashes fixed at 56, 57 (Vla) and 63 (Hn4 bes–g); violas in measured eighths on the turn figure 103–108.
Open: recap 127–130 lacks the new viola counterline.
Do-not-touch: 154–157 counterline scoring; fugato 85–96; layering 109–113; low theme with counter 123–126; chorale and motto canon 171–178.

## Cycle 38 → v58 (expression)
Accepted 5: viola counterline dynamics 19–22 with accompaniment lowered; 163–166 surrounding parts at f so the ff brass head stands out; crescendo at 162 in Vln I/II/Cb; Cb fp at 33; slurred neighbour notes in violas 103–108.
Rejected: viola counterline in recap 127–130 (closed: wrong phrase correspondence); Ob = Vln level at 19–22.
Do-not-touch: 19–22 counterline notes; 47–55 swells; 139–147; 154–157; brass head and fermata 163–166; 171–178.

## Cycle 39 → v59 (holistic, Brahms 1/i, Beethoven 9/i; vs v48)
Accepted: fewer tempo changes (removed "poco più tranquillo" 73 and "a tempo" 77; meno mosso 112 not 100); subtitle draft number.
Rejected: removing poco rit. at 137.
Pending Dan: exposition repeat 15–76 (+2:20).
Nothing worse than v48.
Do-not-touch: motto transformations; pedal 109–118; ♭VI climax 154–158; denied tutti 163–166; coda 171–178.

## Cycle 40 → v60 (cyclic/arc)
No note changes. Coda comments corrected; cyclic-notes.md corrected and extended (chorale colour for III, four unresolved B♮s, A♭/D♭ for II, III needs new material).
Do-not-touch: tempo descent 166–178; CA at 5–8 and 167–170; flute A♭-minor motto 73–76 in tempo; Cl1 171–173; chorale + tam-tam 171–175; viola E♭→E♮ 177–178. Do not restore a tempo word at 73.
Decision (2026-10-08, Dan left it to the composer; length is not a constraint): no exposition repeat. Late-Romantic models (Tchaikovsky 4–6, Dvořák 7–8, Brahms 4, Elgar 1) omit it; do not re-raise on length grounds.

## Cycle 41 → v61 (melody)
Accepted: 39–40 use the bar-20 figure instead of the sixth ladder (ladder now unique to 111–113).
Rejected: exposition repeat (decided against).
Do-not-touch: 15–22; 47–55; peak placement of the main themes.

## Cycle 42 → v62 (harmony/voice leading)
Accepted all 8: violas 104/107 follow the chord; viola 39 re-timed; CA suspension D over 168–169 (no fifths with cello); viola 6–5 at 12–13; Hn3 D♭ at 37; d' at 64; Hn3 A♭ at 57; Tpt2/Ob2 at 134–135.
Noted: bar 60 maj7 F/G♭ resolves (kept).
Do-not-touch: Ger6–V 12–13 (except viola); chromatic bass 27–32; V–♭VI 154–158; iv–N6–i6/4–V 168–170; chorale 171–178.

## Cycle 43 → v63 (form/proportion)
No music changes (comment fix in dev.ily). Development (46 bars) and recap first group (16) kept: within corpus ratios.
Rules: no new slow bars or ritardandos (slow music already ~29% of time); do not extend the G pedal 109–122.
Do-not-touch: proportions 14/62/46/40/16; two-core development; half-length recap first group; coda length.

## Cycle 44 → v64 (orchestration: doubling)
Accepted all 4: Ob1 rests 58–61 and 139–153; strings alone 15–22; Ob1 out of 35–38 with clarinet sustain; Ob1 rests 103–106. Oboe doubling of Vln I 74% → 53%.
Open: flute doubles Vln I in 60% of bars.
Do-not-touch: 47–55; 139–147; 154–157 scoring; 163–166.

## Cycle 45 → v65 (engraving)
Accepted all 8: bar-number baseline; part-combine labels at 41, 111, 122, 127–129; one hairpin at 42 (Cl); timpani muta text at 85/103 with break before 85; cello hairpin end 84; BCl text 92.
Do-not-touch: K page break, page-count 17; marks above Vln I; part-combine modes; divisi scheme; bar numbers under Cb.

## Cycle 46 → v66 (playability, section leaders)
Accepted: 10 down-bows (15, 33, 123, 154, 156, 163); viola slur split 19–22; Ob1 rests 135–136 before the 137 solo; percussion beaters at 114/155.
Open: harp 56–68 and 148–159 all on the lower staff; part cues (for part extraction).
Rejected: Hn2→Hn3 at 148–151 (cycle 16 reasoning).
Do-not-touch: 154–158; 47–55; 139–147; 163–166; 171–178.

## Cycle 47 → v67 (texture)
Accepted: two-hand harp writing 56–68 and a new harp figure 148–162; violas 158–161 vary the exposition.
Do-not-touch: harp at 47–55; 139–147; 154–157; fugato 85–96; 109–113; E♮→E♭ at 162.

## Cycle 48 → v68 (expression)
Accepted: ff at 158 after fff; harp dynamics 148–162, étouffez 160, single harp dynamics; second-player dynamics on shared staves; dolce Vc 47, molto cantabile Vln 55.
Open: articulation vocabulary (no staccato/sf/fz anywhere; see c048); Fl/Ob hairpin 108.
Rejected: "tranquillo" at 73 (acts as a tempo word).

## Cycle 49 → v69 (holistic, Beethoven 9/i; vs v58)
Accepted: staccato in the fugato 85–96 and at bar 30; sf instead of accent+ff at bar 20 (Vln I).
Closed: the articulation question from cycle 48 (targeted marks only; no mass pass).
Nothing worse than v58.
Do-not-touch: fugato notes and 3-bar entries; notes of 15–22; head's slurred accent; graded brass 27–32 and 163–166; 154–157; 171–178.

## Cycle 50 → v70 (cyclic: introduction)
Accepted: silence on beat 4 of 14 with diminuendo to pp (Allegro out of silence); string swell 6–8.
Verified: motto recognisable at 73, 109, 138, 167; CA rhythm at 168 still recognisable; v59–v69 weakened no link.
Do-not-touch: scoring of 1–4; CA 5–8; notes 9–13; horn E♭–C–B 13–14; timpani swell 119–122.

## Cycle 51 → v71 (melody: secondary material)
Accepted: countermelody re-pitched at 57, 65, 66, 159, 160 to avoid unisons/octaves with the tune.
Verified sound: codetta, flute motto 73–76, transition, development lines, counterlines, coda.
Do-not-touch: 69–76; 33–46; 77–83; 97–108; 113–122; 19–22; 148–151; 154–157; 171–178.

## Cycle 52 → v72 (harmony: large-scale)
Accepted: three bars of dominant 136–138 (Cb G, timp roll); borrowed iiø7 at 160.
Rules: no more Neapolitan or B–D–F–A♭ cadences; leave the bar-66 cadence diatonic.
Do-not-touch: ♭VI thread; G pedal 109–122; Ger6 12–13; cadence 168–170; motto Neapolitans; 4–3 at 66 and 160; E♮→E♭ 162.

## Cycle 53 → v73 (form: pacing in time)
Accepted: trough 160–162 (mp → p, crescendo into 163 kept); Fl1 rests 77–78.
Rule: development 91–108 should gain dissonance (suspensions), not lose it.
Do-not-touch: 154–157; E♮→E♭ 162; silence at 14; dominant 136–138; fugato and B-minor core; intro and coda.

## Cycle 54 → v74 (orchestration: flute doubling, solo moments)
Accepted all 5: flutes rest 152–153; Fl1 158–159 only, Ob1 rests after 157; Fl1 rests 60–61; soft Tpt1 counterline 60–63; Bsn1 solo head 33–34 (Vc rest).
Noted for movements II/III: give the bass clarinet a line of its own.
Do-not-touch: climax scoring 27–32, 114, 154–157, 163–166; 47–55; fugato wind colours 88/91/94; 69–72; 73–76.

## Cycle 55 → v75 (engraving)
Accepted all 8: harp pedal marks in preceding rests; Hn 3·4 labels "3."/"4."; Hn2 label 64; triplet numbers omitted 110–113; "1. Solo" for bassoon 33, 77; Vln II hairpin 97; bar-number padding 7; étouffez (m.d.) 160.
Do-not-touch: K page break, 17 pages; marks above Vln I; part-combine modes; divisi scheme; harp voicings 148–162.

## Cycle 56 → v76 (playability; parts)
Accepted all 5: harp pedal timings 50, 59, 63, étouffez 159; Bsn1 breath after 36; Cl1 rest at end of 112.
Verified: timpani tuning plan; page turns in Harp/Tpt1/Vln I parts. For part extraction: harp pedal diagram before 148.
Do-not-touch: harp notes 47–55 and 148–162; Tpt1 60–63; timpani plan; down-bows 154–156.

## Cycle 57 → v77 (texture: development tension)
Accepted all 4: suspensions in fugato free voices 91–95; 4–3 across 105–106 in all G→F parts; delayed leading tone 118–120; viola neighbour 167.
Rule (replaces cycle 53's): add suspensions and chromatic passing tones in non-thematic voices of the development; no numeric target; no A♭ in the bass before 114.
Do-not-touch: fugato subject/countersubject/entries; B-minor core 97–102 with brass counter; 109–114 layering and tam-tam; hemiola 127–130; Vc/CA duet 167–170.

## Cycle 58 → v78 (expression: slurs)
Accepted all 7: slur consistency 160–161, 131, 157, 64–65; suspensions slurred into resolutions 91–95, 105–106, 118, 167.
Do-not-touch: slurring of 47–55 and 167–170; separate string bows 154–156.

## Cycle 59 → v79 (holistic, Eroica i, Tchaikovsky 5/i; vs v68)
Accepted: subito p at 62 (prepared crescendo contradicted); bare G octave subito p at 84 instead of the repeated horn/timpani fade.
Open: recapitulation excursion to D♭ at 132 (two added bars; touches protected 123–134; would need a reasoned answer).
Nothing worse than v68.
Do-not-touch: 47–55; E♭/E♮ and D♭ threads (8–9, 20, 147–148, 162, 178); 154–157; 166; coda notes 167–178.

## Cycle 60 → v80 (cyclic: D♭)
No music changes. Decided: no D♭ key excursion in the recap (closed unless the recap is rewritten to arrive softly). D♭ plan for II/III added to cyclic-notes.md.
Do-not-touch: 123–138; absence of D♭ in 139–162; 154–157; 162; D♭ at 169 and 173–177.

## Cycle 61 → v81 (melody: top line)
Accepted: Fl1 in unison (not octave above) at 23–25 and 127–129, so A♭6 is not heard before 31/132.
Rule: do not shorten the A♭6 at 156; keep A♭6 to its current six bars.

## Cycle 62 → v82 (harmony: bass line)
Accepted all 3: viola 119–120 (no doubled resolution under the clarinet); bass steps 4̂→5̂ at 150–151; Hn4 B at 100 (iiø7).
Noted for II/III: more inverted bass (root position 71% vs 40–59% in models); a Brahms-style bass countermelody.
Do-not-touch: wedge 101–108; chromatic ascent 27–32; bass 73–84; C1 at 163–166; augmented bass motto 171–175.

## Cycle 63 → v83 (form: recapitulation)
Accepted: D♭ spelling at 152 (Vln I/II); header comments. Verified: 163–170 replace the codetta; recap changes all audible.
Do-not-touch: do not restore a C-major codetta after 162; first group 123–135; 156–158; 171–177.

## Cycle 64 → v84 (orchestration: tutti spacing)
Accepted all 4: Bsn1 at 157; Hn4 F3 at 26/130; Cl1 f at 69; Cl1 F5 at 116.
Verified: tutti spacing and doubling proportions within the models; brass chord complete at every tutti.

## Cycle 65 → v85 (engraving: notation)
Accepted all 6: modern cautionary accidentals; double bars at key changes; Vc tenor clef 154–157; Bsn a2 159–161; Hn3·4 bass clef 158–162; timp rests 166.
Verified: no spelling errors.

## Cycle 66 → v86 (playability: endurance)
Accepted all 7: Tbn2 rests 103–104; horn breaths 108/112; Hn4 rest 118; bassoon pedal moved to Bsn1 148–151 with staggered breaths; quarter rests in doubling parts 97–104; Bsn2 rest at 12; Hn2 rest at 153.
Do-not-touch: augmented motto 109–113; Hn4/timp swell 119–122; notes of 97–102, 139–147, 154–157; 162.

## Cycle 67 → v87 (texture: motivic accompaniment)
Accepted: cello motto in diminution at 58 and 152.
Do-not-touch: viola E♭–E♮–F 56–57; bass E♭–E♮–F 29–31 and 63–64; viola turn 103–108/131–134; counters 123–126, 148–151, 69–72; CA fills 139–144; brass counter 97–102; neutral accompaniment 47–55, 139–147, violas 60–67.

## Cycle 68 → v88 (expression: dynamic audit)
Accepted all 7: hidden entry dynamics for player 1 on shared staves; timp 107; sub. p in all parts at 62 and in Vc/Cb at 84; Fl/Ob hairpin 108; Vln II mf 23; Vc f 94; cello motto dynamics 58/152.
Do-not-touch: 62 subito and 158–162 trough; graded brass; 47–55 swells; 95–97 f restatement.

## Cycle 69 → v89 (holistic, fresh eyes; Tchaikovsky 4/i; vs v78)
Accepted: Fl2 high at 114–115; Cb f at 163.
Re-raised: overall length (fast music only) — handed to cycle 70.
Nothing worse than v78.

## Cycle 70 → v90 (cyclic: theme combination) — BAR NUMBERS CHANGE HERE
Accepted: 8 new bars 103–110 combining the first- and second-theme heads (f, then p inverted), between the B-minor block and the wedge.
**From v90 on, every bar number above 102 in the entries above is 8 lower than in the score: add 8 to any old reference ≥ 103** (e.g. old 114 climax = 122, old 154 = 162, old 162 E♮→E♭ = 170, old 163–166 brass head = 171–174, old 171–178 chorale/coda = 179–186). Rehearsal marks: G 117, H 131, J 147, K 162, L 171, M 175. 186 bars.
Do-not-touch: 97–102; wedge (now 111–116); G pedal (now 117–130); subito p at 84; coda pairing (now 175–178). The fast full-brass major combination of the two heads is reserved for movement III.

## Cycle 71 → v91 (melody: theme combination)
Accepted all 5 in 103–110: Vln I loco; appoggiatura line at 106; Hn3·4 mp; Hn4 F at 104; minor-sixth approach into 111.
Do-not-touch: first bars of both heads at 103, 105, 107, 109; eighths-against-long-notes layering; 97–102; wedge 111–116; G pedal 117–130.

## Cycle 72 → v92 (harmony: development route)
Accepted: Hn4 B at 106; viola g4( a2.) at 108. Verified: development key route and joins.
Do-not-touch: step-wise key rise D–E–F–G 103–117; joins at 102→103 and 110→111.

## Cycle 73 → v93 (form: pacing after insertion)
Accepted: wedge enters one level lower at 111 (graded); pp sustains 107–109.
Rule: do not add more development bars. Climax position 0.63 is right.

## Cycle 74 → v94 (orchestration: colour plan)
Accepted: 103–106 winds and horns only; 107–110 flute (low) + violas on the second-theme head, Vln I tacet 103–110.
Do-not-touch: notes and f/p contrast of 103–110; 97–102; 111–116; 117–130; 47–55 and 147–155; 131–134.

## Cycle 75 → v95 (engraving)
Accepted 6 + 1: labels at 110 and 145; Vln II div. rests 107–111; Cl2 accent 106; viola hairpin 60–61; CA espr. 175; BCl "(low C)" name and octave-transposition note on the title page.
Verified: marks and tempo words after renumbering.

## Cycle 76 → v96 (playability: new passage)
Accepted all 4: Ob2 takes 103–106; Cl2 rest end of 102; Hn1 rest 102 beats 3–4; Bsn2 takes 107–109.
Decided: no mutes anywhere. Part extraction: viola cue in Vln I at 109–110.

## Cycle 77 → v97 (texture: dialogue)
Accepted: half-bar wind/string chain 37–40; Bsn1 answer 144–145.
Do-not-touch: motto exchanges 77–83; fugato 85–96; brass fills 97–102; theme swap 103–110; stretto 127–130; CA answers 147–153.

## Cycle 78 → v98 (expression: tempo)
Accepted: MIDI tempo map via `mt` helper in global.ily (rit./allargando/fermatas now audible); "poco animando" at 62 and 160.
Do-not-touch: metronome values; allargando–sostenuto–a tempo chain 121–127; silence at 14; coda tempo descent 171–186. Any new tempo word needs a matching `\mt` step.

## Cycle 79 → v99 (holistic)
Accepted: MIDI volume for \subP, sf, fp; harp RH MIDI dynamics; Vln II lower divisi pp at 107; ritardando curves reshaped (poco rit. into meno mosso ends at 114).
Open for later form/melody critics (were protected; a critic may reopen with a stated answer): recap second group 147–161 too complete (Tchaikovsky 6/i keeps ~42%); development opening 77–84 stop-start; 103–106 light after ff.

## Cycle 80 → v100 (cyclic: recap second group)
Accepted: cut old 156–159 (violins' literal repeat of the head). **From v100 on, the movement has 182 bars: references ≥ 160 in entries above are 4 lower in the score** (e.g. ♭VI climax 162 → 158; E♮→E♭ 170 → 166; brass head 171–174 → 167–170; chorale 179–183 → 175–179; end 186 → 182). Rehearsal marks: G 117, H 131, J 147, K 158, L 167, M 171.
Do-not-touch: 147–155; violins' approach 156–157 into K; climax scoring 158–166; do not restore `recTwoMelodyA` in movement I (reserved for movement III).

## Cycle 81 → v101 (melody: development opening, new violin entry)
Accepted: Cb sustain G at 83; Hn2 D–D♭ at 156.
Decided: no countermelody at 77–83 (closes critic 79's "stop-start" item). Violin entry 156–157 confirmed.

## Cycle 82 → v102 (harmony: harmonic rhythm)
Accepted: Vln II C–C♯–D at 148–149 (IV–IV+–ii); E→D at 155 in Vla/Vc/Hn1.
Do-not-touch: plain exposition 47–55 (contrast with recap); climax harmony 158–166; motto D–D♭–C 156–157; wedge bass 111–116.
Noted for movements II/III: faster harmonic rhythm in first-group material.

## Cycle 83 → v103 (form: proportions in seconds)
No change. Proportions within the models' range.
Rules: add no slow time to 167–182; do not raise level or density of 147–157; no more development bars (cycle 73) stands.

## Cycle 84 → v104 (orchestration: balance)
Accepted: Cl 1 on the head 103–106; brass to f under the low theme 131–134; all four horns on the call 41–42.
Do-not-touch: notes and f/p of 103–110; scoring 97–102, 158–161, 167–170; notes of 131–134.

## Cycle 85 → v105 (engraving)
Accepted: forced breaks before 64, 94, 103, 111, 119, 131, 139; numbered short names for all pairs; harp hairpin 156 removed; Cl a2 at 103; Vc sub. p at 62; Cl p offset at 126.
Do-not-touch: K page break and page count 17; part-combine modes; harp voicings 147–166 and pedal diagram 155. Adding bars or systems now risks an 18th page: check page layout after any change.

## Cycle 86 → v106 (playability: breaths)
Accepted: breath rests for low brass 116/121, Hn 157, Hn 3·4 68, Hn 4 102, BCl 100, Fl 2 119, Bsn 2 113.
Open: Cl 1 162–166 has no rest (E♭ at 166 protected).
Do-not-touch: motto pitches and ties 117–124; climax scoring 158–166; pp chorale 175–179.

## Cycle 87 → v107 (texture: breath holes, density)
Accepted: staggered low-brass breaths 114–116; Hn 3 holds at 157; trombone breath at 121 shortened to an eighth.
Rule: when adding breath rests, check that the same line keeps sounding in another player.
Note for movements II/III: thin texture is 30% of movement I (models 15–16%).

## Cycle 88 → v108 (expression: articulation consistency)
Accepted all 7 fixes (tenutos 99–108; slurs 69–71, 139–140, 37–38, 169; dolce 146; accent 36).
Rule: doubling parts within one statement carry identical slurs and accents.
Do-not-touch: second-theme head phrasing 47–58, 146–155, 175–178; fugato marcato 85–96; separate string bows 158–160.

## Cycle 89 → v109 (holistic: generic features)
Accepted: held chords under the hemiola 23–26 and 135–138 (strings keep the pulse); deceptive cadence to F minor at 68.
Open (protected, proposals in c089): same tutti layout at 27–32, 69–72, 131–134, 167–170; root-position bass at 49, 51.

## Cycle 90 → v110 (cyclic: notes, tuttis)
Accepted: broken-chord violas at 69–71; consolidated summary appended to cyclic-notes.md.
Do-not-touch: tutti layout at 27–32 and 167–170 (alike on purpose); 131–134; stops at 26/138/170; E♮→E♭ at 166; coda 171–182.

## Cycle 91 → v111 (melody: memorability)
No change. Theme pitches and rhythms confirmed against earworm research and models.
Do-not-touch: pitches/rhythms of the first theme and the second-theme head in all statements; plain bass 47–55 (closes c089 item); horn + cello at 47 and violins at 56; D♭6 peaks at 20 and 63.

## Cycle 92 → v112 (harmony: inner voices)
Accepted 4 inner voice-leading fixes in dev.ily (94–95, 108–109, 110–111, 112).
Verified: inner parts stricter than the models. Do-not-touch: fugato subject/countersubject/entries; wedge bass and top line; chorale pitches and the unresolved B♮.

## Cycle 93 → v113 (form: joins)
Accepted: Vln I run + crescendo into 69 (bar 68 beats 3–4); violin pickup into 33.
Do-not-touch: pedal joins 76/77, 130/131, 174/175; crescendo chain 110→117; E♮→E♭ crescendo 166/167; fermata stop 170/171.
Open proposal: diminuendo on beats 3–4 of 102 (strings, brass).

## Cycle 94 → v114 (orchestration: instrument use)
Accepted: bass clarinet alone on the first-theme head 107–109 (Bsn 2, Vc rest).
Rejected: diminuendo at 102 (closes c093 proposal).
Notes for II/III: soft solo trumpets; leads for Cl 2 / Ob 2; limit Cl 1 and Fl 1 top-line use.

## Cycle 95 → v115 (engraving proofread)
Accepted: part-combine labels (56–68, 69–72, 78); merged rests; espr. placement 33/77; final-bar fermatas on all staves.
Open small collisions: 167, 156, 162, 110.

## Cycle 96 → v116 (playability: rehearsal read-through)
Accepted: Cl 1 breath at 167; fermatas at 170 (CA, perc, harp); part-only CA cues; Vc measured sixteenths 117–121; Bsn 1 f> at 33.
For parts: \addQuote cue sources; harp cue before 156.

## Cycle 97 → v117 (texture: frame)
Accepted: Hn 3 C4 180–182 and Hn 4 G3 181–182 (final chord spacing); Bsn 1 G3 at 174; Cb divisi in octaves 6–7.
Do-not-touch: motto register G1/G2 at 1–4 and 175–179; low top of the last eight bars; chorale pitches; viola E♭→E♮ 181–182.

## Cycle 98 → v118 (expression: dynamic arc)
Accepted: brass f under the horn call 41–42; crescendo to ff at 96; timpani mf–f at 72.
Do-not-touch: fff only at 122 and 160; graded brass at 27–32, 131, 167; sub. p at 62 and 84; dip 163–166; coda pp/ppp.

## Cycle 99 → v119 (holistic: series assessment)
Accepted: system breaks before 73 and 121 (replacing 77 and 119).
Verdict: no first-rank musical weakness left that can be fixed without reopening settled decisions.

## Cycle 100 → v120 (cyclic + release check) — end of the series
No musical change. Release check passed; breaks before 23, 31, 39; cyclic-notes.md updated with v120 bar numbers.
v120 is the final movement I of the 100-cycle series (2026-10-09).
