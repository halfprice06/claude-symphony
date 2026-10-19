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

# Second series (cycles 101–200, v121–v220): critics must cite Dan's reference books (BRIEF research item 3)

## Cycle 101 → v121 (melody: rising-sixth density)
Accepted: pickup G (not A♭) at 29, 139, 169; Vln I octave leap at 19; semitone head at 38.
Rule: the rising sixth stays in theme heads, the motto, the ladder 117–120 and the climax 156–160; elsewhere prefer other intervals. Movements II and III open new themes with a different interval.
Do-not-touch: first-theme head 15–16 and second-theme head in all statements; motto; ladder 117–120; climax sequence 156–160.

## Cycle 102 → v122 (harmony: codetta and inner fifths)
Accepted: codetta 69–72 on bass A♭–E♮–F–D♭–E♭–A♭ (V6/5 of vi, ii6/5); inner-voice fifths removed at 24–25, 45–47, 52; Cb A♭ at 34.
Open: clarinet arpeggio fifths 97–99 (protected B-minor block; fix in c102).
Do-not-touch: chromatic tutti bass 27–32; Ger6–V at 12–13; iv–N6–i6/4–V at 172–174; G pedal 117–130; climax harmony 158–166.

## Cycle 103 → v123 (form: codetta cadence)
Accepted: codetta 69–71 now I–I6 | ii7–vii°7/V | V7 (replaces cycle 102's V6/5 of vi; no third arrival on F minor after the deceptive cadence at 68).
Closed: the first-theme counterstatement option from cycle 69 (not needed).
Do-not-touch: codetta bass A♭–C–B♭–D♮–E♭ (do not tonicize vi again here); recap climax 147–160; 122–131 spans; key plan; saved colours; no trombone rhyme at 73–76.

## Cycle 104 → v124 (orchestration: fill the octave under the top line)
Accepted: Cl 1 counterline up an octave at 158–162; Fl 2 fills at 31 and 140.
Open: Cl 2 on the tenor line at 27–32; gap at 72 and other bars listed in c104.
Do-not-touch: 117–122, 96, 131–134; soft scoring 47–55, 73–76, 147–155, 175–182.

## Cycle 105 → v125 (engraving)
Accepted: no 8va at 139–141 (Vln I); Hn 1 mp at 154; system break 163 instead of 167; bar-55 text alignment; bold "3." at 180.
Do-not-touch: K page break and 17 pages; part-combine modes; marks above Fl and Vln I; bar numbers under the basses; 8va at 31, 71–72, 121–123.

## Cycle 106 → v126 (playability)
Accepted: no 8va for Fl 1 at 98–100.
For parts (when built): Vln I ottavas score-only; viola/cello part breaks after 33 and 103; harp pedal letters score-only.
Do-not-touch: Cl 1 counterline 158–162; codetta scoring 69–72; low horns 23–26; brass load plan; harp 147–166.

# From cycle 107: each critic has an assigned reading (critics/READING.md) and bases its findings on it (Dan, 2026-10-09).

## Cycle 107 → v127 (texture; Adler ch. 5)
Accepted: fugato countersubject bar 2 rhythmically independent (89, 92, 95); Vln II rests 171–174; Vln I rests 147–154 (Vln II div. tremolo).
Do-not-touch: fugato subject, entries and countersubject bars 1 and 3 (85–96); cello/harp accompaniment 56–68; theme combination 103–110; cello/CA duet 171–174.

## Cycle 108 → v128 (expression; Rimsky-Korsakov ch. IV)
Accepted: trumpets enter at 113 not 111; sf-dim under the horn call 41–42; brass out of the p chord at 43; all f at 138; horns/bassoons mp< at 156.
Do-not-touch: slurred runs into 33 and 41; brass-first fade 162–166; sparing percussion (tam-tam 122, 175; cymbal roll into 160); ppp opening and close.

## Cycle 109 → v129 (holistic; Rimsky-Korsakov examples 1–60)
Accepted: Fl 1 rests at 107–108, enters 109 espr. mp.
Verdict: melody scoring at master level; nothing worse since v119.
Do-not-touch: horn + cello 47–55; violins 56–63; horn call 41–42; solo-wind accompaniments; climax 158–161 with the clarinet counterline.

## Cycle 110 → v130 (cyclic; Aldwell & Schachter Unit 32)
No musical change; comment fix only. cyclic-notes.md updated with changes from cycles 101–109 and critic 110's plans for II and III.
Do-not-touch: 77–82 key plan; key arrivals 97, 103, 111 and A♭ over G at 122; bass 111–116; bars 12 and 75 (same chord spelled Ger6 / V7 of D♭); E♭/E♮ inflections 8–9, 145–147, 166, 181–182; bar 182 (C5 on top, viola's lone E♮).

## Cycle 111 → v131 (melody; Aldwell & Schachter Unit 20)
Accepted: B♭♭ spelling at 60 (Vln I, II).
Closed: fifths at 97–99 (acceptable figuration); octaves at 72.
Do-not-touch: second-theme appoggiaturas 50, 59, 101; chromatic spellings 15, 35–40, 58, 78; motto C–D♭–C at 3–4 and 177–178.

## Cycle 112 → v132 (harmony; Aldwell & Schachter Unit 5)
Accepted: bass F♭ through bar 61; chorale revoiced at 6; Hn 3 at 22; Vla at 173; Cl 1/Hn 2 at 66.
Do-not-touch: orchestral octave doublings at 12–13 and 161–162 (allowed, PDF 84–85).

## Cycle 113 → v133 (form; Aldwell & Schachter Unit 14)
No change.
Open: the development establishes no key for more than ~6 bars (c113 F1); consider a held key area (12–20 bars with a cadence) at cycle 123, which would add development bars and needs a strong case.
Do-not-touch: 5–6 shift at 77–78; swerve B minor → D minor at 102→103; codetta cadence 69–72; A♭7 at 75.

## Cycle 114 → v134 (orchestration; Rimsky-Korsakov ch. I, III)
Accepted: brass sf > mf under the horn call 41–42 (replaces cycle 98's brass f); oboes in octaves 41–43; horn pad fixes 57, 65; Vln II metà 47–54.
Do-not-touch: horn + cello second theme 47–55; violins' tune 56–63; wind pad at 145; stop chords 26, 138, 170.

## Cycle 115 → v135 (engraving; Gould ch. 1)
Accepted: Vc clef before the pickup at 46 and 146; Hn 3·4 treble at end of 14; one-line cymbal/tam-tam staff; violas stay in alto at 109–110.
Do-not-touch: cello clef plan 47–56; horn bass-clef passages 23–26, 103–106, 162–166.

## Cycle 116 → v136 (playability; Adler ch. 2)
Accepted: shorter string bows at 3–4, 155–157, 177–182; Cb rest before pizz. at 84; viola div./unis. 56–69; down-bows on the theme head.
Do-not-touch: notes and dynamics of the coda 171–182; separate string bows 158–160; div./metà scheme 47–55 and 147–155.

## Cycle 117 → v137 (texture; Adler ch. 15)
Accepted: cellos on the second-theme head 103–106; layered dynamics f→fff at 117–122; violas and Hn 3·4 pp at 56–59.
Do-not-touch: codetta 69–72; B-minor block 97–102; fugato entry colours 85–96; stretto with timpani roll 126–130.

## Cycle 118 → v138 (expression; Adler ch. 2 bowing)
Accepted: down-bow entries at 19 and 139; hooked up-bows before the accented A♭ (16, 28, 132, 168); down-bow hammer strokes 32, 72, 83, 142; mf at 60.
Do-not-touch: D♭6 peaks at 20 and 63 and sub. p at 62; separate bows and down-bows 158–160; the head's slurs and accents; sul tasto 147 / ord. 155; coda 171–182.

## Cycle 119 → v139 (holistic; Rimsky-Korsakov examples 61–125)
Accepted: Ob 2 rests 23–25, 135–137; Hn 4 B♭3 at 63, 67; bass trombone F♯3 at 101–102.
Verdict: orchestration at master level against Tchaikovsky 6/i; nothing worse since v128.

## Cycle 120 → v140 (cyclic; Aldwell & Schachter Unit 26)
Accepted: Hn 2 F4 at 130 (seventh over the G pedal into the reprise).
Do-not-touch: key plan incl. the A♭ upper neighbour at 122; route 36–47; 156–166; stretto 126–130; the coda's stepwise close with unresolved B♮s.

## Cycle 121 → v141 (melody; Rimsky-Korsakov ch. II)
Accepted: Vln II doubles the D♭6 peak an octave below at 20–21.
Do-not-touch: string layout 27–32; violins 56–63; violas and cellos 147–155; motto 1–4 and 175–178.

## Cycle 122 → v142 (harmony; Aldwell & Schachter Units 9–10)
Accepted: suspensions not doubled by their resolution at 32, 141–142 and 54; complete cadential 6/4 at 13–14; strings with the bassoon at 144.
Open: 6/4 after V7 at 101–102 (c122 F5, sketch in report).

## Cycle 123 → v143 (form; Aldwell & Schachter Units 16, 19)
No change. Closed: held key area in the development (c113) — not added; 6/4 at 101–102 (c122) — correct as a neighbouring 6/4.
Do-not-touch: development bass plan C–A♭–F–G–C; 6/4s on the G pedal 117–130; ♭VI neighbour thread 82→83, 122, 159→160.

## Cycle 124 → v144 (orchestration; Rimsky-Korsakov ch. III brass)
Accepted: Cl 2 up an octave 158–161; Ob 2 D5 at 122–123; Hn 4 F3 at 39–40; Hn 4 D at 164.
Open (optional): Cl 2 B♭3 inside the horns at 41–42.
Do-not-touch: brass doublings and dynamic grading at 12, 27–32, 82, 140, 167–170; Hn 3·4 octave pedal 117–121; horns with cellos/violas 47–55, 147–155; pp trombone chorale 175–179.

## Cycle 125 → v145 (engraving; Gould beams)
Accepted: soloStemsOn/Off helpers for shared-staff solos at 33–40 and 77–78; \partCombineApart 139–142; harp beam damping 47–63.
Open: up-stems on flutes a2 158–162 and Bn 1 88–90 (c125 F2–F3).
Do-not-touch: beaming and metric grouping in strings and winds; cello clef plan at 46/146/157; no triplet numbers at 117–121.

## Cycle 126 → v146 (playability; Adler ch. 3 strings)
Accepted: "change bow at will" Cb 117, 179; up-bows before pizz. at Cb 46, Vc 61; Vln II "div."/"unis." at 55.
Do-not-touch: string ranges; divisi and clef scheme; Cb sustain under Vc arpeggios 56–64, 158–166; coda notes and dynamics 171–182.

## Cycle 127 → v147 (texture; Adler ch. 17 accompaniment)
Accepted: viola E♭3 at 77; viola `c'2 aes2` at 173 (replaces cycle 112's F4).
Do-not-touch: accompaniment design of 15–22, 47–68, 147–155; fugato entry colours 85–96; cello/cor anglais duet pitches 171–174.

## Cycle 128 → v148 (expression; Adler brass climaxes and sforzando)
Accepted: brass short sf eighth at 41 (replaces cycle 114); Hn 1·2, Tbn 1, B.Tbn f from 98.
Open: "sub. mf" at 135 (needs a MIDI volume rule for the markup).
Rule: the brass scoring under the horn call at 41–42 has now been changed in cycles 84, 98, 114 and 128. Do not change it again without listening evidence or a new source.

## Cycle 129 → v149 (holistic; Rimsky-Korsakov examples 125–206; Dvořák 8/i)
Accepted: low brass rest 135–137 (closes "sub. mf at 135"); bass clarinet takes the solo at 77–78; composer added "attacca" at the end.
Bar 41's short brass sf is now supported by two sources (Adler Ex. XV-35, Rimsky Ex. 165); the cycle-128 rule stands.
Do-not-touch: "attacca" at the end (movement II begins on movement I's last chord).

## Cycle 130 → v150 (cyclic; Casanelles ch. 5)
Accepted: thin double barline at the end; ties out of 182 in Vln I, Vln II, Vla, Vc, Hn 3.
Do-not-touch: coda 167–182 (notes, dynamics, fermatas, tempo); spacing of 182 with the viola's lone E♮; tam-tam only at 122 and 175; low motto 1–4 returning 175–179; "attacca", "||" and the outgoing ties.

## Cycle 131 → v151 (melody; Rimsky-Korsakov ch. II winds and brass)
Accepted: Hn 2 (not Tpt 1) on the chromatic counterline 56–68; Cl a2 and Fl a2 at 69–72; Fl a2 at 115–116.
Do-not-touch: horn + cello 47–55, horn + viola 147–155; Fl/Ob + Vln I at 97–102; solo-wind statements; four-horn call 41–42; theme pitches.

## Cycle 132 → v152 (harmony; Aldwell & Schachter Units 11–13)
Accepted: Vla C→B at 11 (seventh chord, not bare diminished triad); Hn 4 C at 82 (no augmented second); Vc A♭ held at 46 (II6/5).
Open: IV6 for VI at the deceptive cadence 68 (c132 F4).
Closed: second-theme chain I–IV–ii–V (cycle 22).
Do-not-touch: deceptive cadences 159–162; codetta 69–72; plagal coda 167–170, 178–182; 172–174 iv7–ii6/5–N6–cad. 6/4.

## Cycle 133 → v153 (form; Aldwell & Schachter Unit 31)
No change. Do-not-touch: bass 77–82 with E♭–E♮–E♭ (Vln II) and C♭→B (Vla); fugato entries; key arrivals 97, 103, 111, 122; 108→109 join; wedge 111–116 (no A♭ in the bass before 122); alternating chords over the G pedal 117–121.

## Cycle 134 → v154 (orchestration; Rimsky-Korsakov tutti chords)
Accepted: full strings with multiple stops at 33; Cb pizz. under the winds 103–106 (closes cycle 79's point); timpani G at 26; B.tbn G at 122–123.
Do-not-touch: tutti layouts 27–32, 83, 138, 158–161; low arrival at 97; stop chords and silences at 26, 138, 170.

## Cycle 135 → v155 (engraving; Gould ledger lines, octave signs, rests)
Accepted: no 8va for Vln I at 40–43; rest positions at 157, 161, 162.
Closed: cycle 125's up-stem items (stems already down).
Do-not-touch: 8va layout at 31, 71–72, 121–123; part-combine modes and soloStemsOn/Off; fixed breaks and 17 pages; one-line percussion stave.

## Cycle 136 → v156 (playability; Adler ch. 4 harp)
Accepted: harp RH at 59–60 avoids the pedal change on a ringing string; étouffez at 62; pedal marks at 53 and 57 beat 3; harp mp at 164.
Do-not-touch: harp notes and voicings 47–55, 147–166; pedal diagrams at 47, 155; étouffez marks 163–164; harp tacets.

## Cycle 137 → v157 (texture; Adler ch. 16)
Accepted: Vc bass octave at 35–36 (Bsn 1 solo ends alone); flutes join the Vln I run at 68.
Open (relay from movement II, its cycle 30): Hn 3 holds C4 ppp for about 18 s at 180–182 with the fermata and on across the attacca; consider a relief by Hn 4 or a breath inside movement I (playability lens, cycle 146, or earlier).

## Cycle 138 → v158 (expression; Casanelles ch. 4, 6)
Accepted: Bsn 1 solo slurred at 34–36.

## Cycle 139 → v159 (holistic; Rimsky-Korsakov examples 206–274; Tchaikovsky Violin Concerto/i)
Accepted: Vln II double stop at 33; Hn 4 half note at 28 and 132.
Do-not-touch: tutti layouts 27–32, 131–134, 167–170; Vla/Vc triple stops at 33; crescendo and diminuendo entry orders; G pedal 117–130; fugato; B-minor block 97–102.

## Cycle 140 → v160 (cyclic; Adler ch. 1, 15)
Accepted: Tbn 1 overlaps the C into 180–181; Hn 3 enters at 181 with Hn 4 (closes the movement II relay's open item).
Do-not-touch: chorale 175–179 notes and slurs; Vln I last motto 177–182; viola E♭→E♮ at 181–182; the five outgoing ties, "attacca", "||"; harp l.v. final chord; Cl 1 at 175–177; at-pitch bass tripling 175–179.

## Cycle 141 → v161 (melody; Adler ch. 3 string colour)
Accepted: Vln I·II sul A 57–59; Vln II sul G 98–102.
Do-not-touch: cello + horn 47–55; violas + flute 107–110; E-string climax 156–161.

## Cycle 142 → v162 (harmony; Aldwell & Schachter Unit 17 sequences)
Accepted: bar 93 prepares B♭ minor (Vla, Bsn 1, Vc on F); viola D♭→D at 35.
Do-not-touch: fugato subject and entry order 85–96; wedge 111–116; G pedal and rising figure 117–130; codetta 69–72; falling-thirds approach 64–68.

## Cycle 143 → v163 (form and pacing; Rimsky-Korsakov ch. IV)
Accepted: timpani rest 135–137; wedge brass enter p at 113–114.
Do-not-touch: crescendo entry orders 9–12, 19–26, 85–97, 110–117; diminuendo exit orders 102→107, 123–127, 162–166; G-pedal timpani roll 117–130; trumpet fff at 122 and ff at 158.

## Cycle 144 → v164 (orchestration; Adler ch. 15 unison tutti, foreground and background)
Accepted: Tbn 1·2 f (not ff) at 131; Fl 2 rests 23–25 and 135–137 and enters on the stop chord.
Do-not-touch: brass grading 27–32, 139, 167; trumpets' timpani rhythm 27–30; low brass and timpani entering on the stop chords 26/138; Fl 1 alone at the top 97–100; octave layouts 82, 158–161; pp trombone/B.cl/Vc unison 175–179.

## Cycle 145 → v165 (engraving; Gould spacing, chords, unisons)
Accepted: spacing section 73–76; note-column shifts at 70, 126, 134, 140, 158.
Open: Fl 2 dot at 119; Hn 1 half rests without ledger line at 43, 102.
Open (relay from movement II, its cycle 40): the harp's l.v. on the final chord at 182 rings into movement II's bar 2 (A♭ bass); movement II damps it with "étouffez" at its bar 2. Decide at cycle 150 (cyclic) whether movement I should drop the l.v. (protected by cycle 140).

## Cycle 146 → v166 (playability; Adler ch. 6–7 woodwinds)
Accepted: Bsn 1/2 share the pp bass 147–155; bassoon breaths after 10; Cbsn breath at 115; "in B♭" on the clarinet staff; Ob 1 D5 at 40.
Do-not-touch: woodwind ranges and registers; cor anglais octave 171–174; B♭ clarinets in the B-minor block; bass clarinet low-C passages and label.

## Cycle 147 → v167 (texture; Rimsky-Korsakov crossing and enclosure)
Accepted: Cl 1 doubles the theme's lower octave at 117–121.
Open (optional, protected): clarinets rest 131–134; Bsn 1 with the horn counter 69–70.
Do-not-touch: clarinet-completed p horn chords at 145, 156–157; Hn 3·4/bassoon crossing 37–40; Cl 2 + Hn 2 counterline over the Hn 3·4 pad 56–63; solo winds over tremolo strings 77–81.

## Cycle 148 → v168 (expression; Aldwell & Schachter Unit 3 meter)
Accepted: motto swell turns on D♭ at 3; diminuendo from the suspension at 66; tenuto on the appoggiatura at 101.
Do-not-touch: beat-2 syncopation accents on the theme head; three-beat groups 23–25, 135–137; weak-beat accents 32, 72, 80–81, 119–120.

## Cycle 149 → v169 (holistic; Rimsky-Korsakov examples 275–312; Brahms 4/i)
Accepted: low brass rest 69–71 and enter f at 72; Fl 1 off the soft peak at 62–63; horns enter p< at 156.
Open (protected): Bsn 2 rest at 56–59 (bass quadrupled).
Note: READING.md's example ranges are off; PDF 376–440 = Ex. 206–274, PDF 441–504 = Ex. 275–312.
Do-not-touch: the four settings of the second theme (47, 56, 147, 158); brass attack at 158 and trumpets' fff at 122; strings-only first theme 15–22; stop chords 26, 138; final-chord spacing 181–182.

## Cycle 150 → v170 (cyclic; Rimsky-Korsakov prefaces and transfer of phrases) — 50 of 100
Accepted: harp damps at 182 (closes the movement II relay item); Bsn 1 with the cellos 167–170; cor anglais overlaps into 9; "change bow at will" at 181.
Do-not-touch: motto colours; coda notes and dynamics 171–182; viola E♭→E♮ 181–182; the five tied parts and "attacca"; overlapping hand-offs 174/175, 180/181; crescendo 9–12.

## Cycle 151 → v171 (melody; Adler ch. 7 woodwinds)
Accepted: bass clarinet solo an octave lower at 77–78; viola mp at 34.
Do-not-touch: B.cl motto 1–4; cor anglais 5–8, 171–174; flute motto 73–76; Cl 1 counterline 56–68; bassoon solo notes and slurs 33–36.

## Cycle 152 → v172 (harmony; Aldwell & Schachter Units 22–23)
Accepted: Tpt 1/Tbn 1 D♭ at 30; stop-chord bass B♮ at 26 (138 keeps D, which rises to F); Hn 3 A♭→G at 164.

## Cycle 153 → v173 (form; Aldwell & Schachter Units 26, 14 — recapitulation and coda)
Accepted: Hn 3 holds B3 145–146 and resolves to C at 147.
Decided: stop chord at 138 keeps D in the bass on purpose (goes to iv; 26 goes to i and has B♮). Do not make them match.

## Cycle 154 → v174 (orchestration; Adler ch. 15 texture)
Accepted: E♭ added at 160 (Tpt 3, Cl 2).
Do-not-touch: rest of the 160 scoring; trumpets' fff entry at 122; flute-free final chord; stop chords 26, 138, 170.

## Cycle 155 (engraving, MOLA) → v175
Accepted: front page (unnumbered; PDF now 18 pages, music pages 1–17); staff names with transposing keys (Hn in F, Tpt in C, B.cl in B♭ low C); Hn 1 rest at 102 pitched on ledger line; Fl 2 dot at 119 up; no key signature on timpani.
Open: composer name for the header; parts-stage notes for cycle 185 (horn parts without key signature; harp pedal marks out of harp part).
Closed: Hn 1 half rests 43/102; Fl 2 dot 119.
Do-not-touch: front page and timpani key handling. Page check is now 18 PDF pages.
Open (relay from mvt II c50): cue the harp retuning "Ré → Ré♭" (lowest D string to D♭ for mvt II bar 10) in the harp rests 175–181, compatible with the damping at 182.

## Cycle 156 (playability, Adler brass) → v176
Accepted: staggered brass breaths 158–162; Tbn 1 breath/restrike at 180; Hn 4 enters beat 2 of 73; Hn 4 restrike at 129; Hn 3 breath before 65; harp retune cue at 176 (closes the mvt II c50 relay item).
Open: Hn 1 written B5 at 106 (composer's choice); cycle 185 parts notes (horn bass clef modern notation; horn/trumpet parts without key signatures).
Do-not-touch: brass ranges and four-horn layout; low horns 23–26; tuba rests 117–125; trumpets' soft entries at 113.

## Cycle 157 (texture, Sebesky) → v177
Accepted: Vc/Bsn 1 tenor counterline 139–142; harp RH up an octave at 56–59 (protected harp design kept; only the octave changed).
Open: clarinets and violas swap the same pitches at 97–102 (critic recommends clarinets rest 97–102; would undo cycle 17's viola figure; needs a cycle that can justify touching the B-minor block); Tpt 3 duplicates Hn 3 at 113–116 (optional rest).
Do-not-touch: theme heads as the source of counterlines; held-back harp and percussion; reharmonized returns; C.a. answers 147–153; Vc/C.a. duet 171–174.
Note: critic 157 used the books only (no corpus or web); later critics should keep all three sources.

## Cycle 158 (expression, Sebesky) → v178
Accepted: Vc p at 35–36; Tbn 1·2 slurred at 131–134 (supersedes cycle 8's unexplained exclusion); Cl 1 p< at 127.
Open: Bsn 1 f while doubling at 103–106 (shared staff; note only).
Do-not-touch: solo/background dynamic grading at 5–8, 43–46, 73–78, 145–155, 171–174; swells 47–55; rit. placements; C.a. answers at plain p.

## Cycle 159 (holistic, Adler/Schubert 8/i) → v179
Accepted: Hn 1/Vla/Vc rest on beat 4 of 55 so the second-theme pickup is exposed.
Closed: c157's items at 97–102 (Cl a2 with Vla is normal accompaniment doubling) and 113–116 (Tpt 3/Hn 3 unison supported by Adler).
Watch: harp RH octave at 56–59 (v177).

## Cycle 160 (cyclic, Sebesky) → v180
Accepted: bar 180 inner voices held (Vln II G, Vla E♭), so the last D♭ is a bare neighbour, not a third D♭ triad.
Open: horn/trumpet key-signature convention shared with mvt II (decide before parts, cycle 185).
Do-not-touch: motto colours and statement order (1–4, 5–8, 73–76, 117–121, 171–182); low motto return 175–179; Vln I's last motto 177–182; Vla E♭→E♮ 181–182; delayed harp, percussion and Vln I entries.

## Cycle 161 (melody, Sebesky ch. 6–7) → v181
Accepted: Ob 1 link at 45–46 uses the second theme's dotted cadence figure.
Open (note only): no moving fill under held notes at 150.
Confirmed: E♭–C pre-echoes; counterlines do not shadow the tune; percussion colour on held notes only; climax register used sparingly.

## Cycle 162 (harmony, A&S 24–25) → v182
Accepted: d5→P5 fixes in Hn 3 at 24/136, Cl 2 at 30, Fl 2 at 31/141.
Closed: IV6 for vi at 68 (cycle 132 item) — keep vi.
Notes: cross relation 59–60 and 64.3 neighbour chord accepted as written.

## Cycle 163 (form, A&S 18) → v183
Accepted: ii6 at the second-theme answer cadence, 53 and 153 (answers the cycle-22 item on bass-motion grounds; I–IV–ii–V chain kept).
Do-not-touch: lead-in 43–47; G pedal with motto 117–130; timpani C under the opening motto; root-position question phrases 47–50 and 147–150; transition route 33–46.

## Cycle 164 (orchestration, Adler ch. 8) → v184
Accepted: Fl 2 close position at 167–170; Cl 2 out of the horn call's unison at 41–43 (closes c124's optional Cl 2 item).
Do-not-touch: layout at 82; bassoon unison 163–166.

## Cycle 165 (engraving, Adler ch. 18) → v185
Accepted: choir brackets on single-staff systems; timpani+percussion bracket (barlines separate); Hn 2 label clear at 102.
Agreed with mvt II (relay c060): key signatures on all pitched score staves except timpani; horns and trumpets without signatures in the parts only.
Parts-stage notes for cycle 185: extract from single-player variables; horn bass clef modern notation; no key signatures in horn/trumpet parts; harp pedal marks out of the harp part.

## Cycle 166 (playability, Adler ch. 12) → v186
Accepted: roll release strokes (12, 14, 63, 141, 146, 161); tam-tam damped at 127; stick indications at 1, 15, 175; timpani dotted half at 170; roll through 116.1.
Open (optional): B♭ at 40 on the 28" drum.
Confirmed: timpani notes inside the harmony; ranges; retuning time; two-player percussion layout; cymbal writing.

## Cycle 167 (texture, Sebesky ch. 3) → v187
Accepted: Bsn 2 rests 56–59 (closes c149's item); Fl 1 mf at 64, pp at 109.
Note: middle register crowded at 56–68 (protected).
Do-not-touch: economical string divisi; unison violins 56–59 and 158–161; lower-octave melody doubling 60–68, 139–142, 158–161; independent Vln II and Vla lines.
Tooling note: full.midi is not rebuilt by build.sh; critics who use it must rebuild it.

## Cycle 168 (expression, MOLA) → v188
Accepted: Bsn 2 dynamics 60–68; bassoons mf 103–106 (closes c158); dynamics moved onto notes at 69/107/131/135/137; woodwind crescendo 139; C.a. tenuto 101; Hn 4 part-only mp at 67 (first use of the 'part tag); Vln II tie above at 181.
Open: unify "damp"/"étouffez with Cb." wording (127, 182) — one language.
Do-not-touch: bowing marks; tempo-mark placement; swells 47–55 and 147–155; graded brass 27–32, 131, 167; coda dynamics.

## Cycle 169 (holistic, Brahms 3/i via Adler) → v189
Accepted: Tbn 1 D4 at 159, Tpt 3 D4 at 161; violas in eighth-note chord tones at 158–161 (supersedes c167's "unison violins 158–161 / lower-octave doubling" protection for the viola only).
Open (protected): Fl 1 rests on the violins' low pickups at 117–119.

## Cycle 170 (cyclic, A&S 23) → v190
Accepted: ♭6→5 at 161 (Ob 2, Cl 1, Hn 3); Cl 1 at 156 without A♮.
Do-not-touch: mixture sequence 159–166; E♭/E♮ turns at 8–9, 166, 181–182; flute motto 73–76 with F♭→E♭ into 77; Vc minor second-theme head 171–174; viola E♮ at 182.

## Cycle 171 (melody, A&S 21) → v191
Accepted: harp RH at 50 avoids early G and ringing G under the G♭ pedal change.
Do-not-touch: first-theme head 9–8 and restruck C anticipation; cadential 4–3s; dominant pedal 117–130 and ♭VI at 122; fugato suspensions 92–95; Vln I tied counterline 131–134.

## Cycle 172 (harmony, A&S 30) → v192
Accepted: Cl 1 at 161 fixes fifths introduced in v190; common-tone °7 at 73 (Vln II, Vla).
Open (note): bass tritone A♭→D at 160→161 at fff (protected).
Rule: a critic who changes a voice must rerun the voice-leading script on full.midi (the 161 fifths came from a change made without it).

## Cycle 173 (form, Adler 15/17) → v193
Accepted: low strings overlap into the pp pedal at 72→73.
Open (optional): Vln II chord register at 107–108.
Closed: 103–106, 77–84, 147–155 kept as written.
Do-not-touch: proportions and loud/soft alternation; dialogue scoring 47–63, 103–110, 147–157; stop chords 26/138/170; rests 83→84; fermata 170→171; G-pedal colouring 117–130.

## Cycle 174 (orchestration, Adler 11) → v194
Accepted: trumpets in timpani rhythm at 131–134; Hn 4 doubles Hn 3's counter at 158–161.
Open: Tpt 1 A♭5 at 72 pre-empts the climax (protected; suggestion in c174); Tpt 3/Tbn 1 held E♭4 at 167–169.
Do-not-touch: trumpets held back until 122; horn/trombone motto 117–121; trombone chorale 175–179; Hn 1·2 on the tune 158–161; short brass chords at 41, 83, 143.

## Cycle 175 (engraving, Gould) → v195
Accepted: clarinet unison at 69; flute unison 115–116; Vln I "loco" at 124; "dolce" placement at 146.
Do-not-touch: 8va layouts at 31, 71–72, 121–123; clef plan; part-combine modes; fixed breaks (17 pages of music).

## Cycle 176 (playability, Adler App. A) → v196
Accepted: timpani retunings on the A♭ drum (34–46, 84–111); horn breaths at end of 134.
Open: Hn 1 written B5 at 106 is undoubled (correcting c156) — Ob 1 doubling or part ossia; "étouffez with Cb." → "étouffez" at 182 (closes c168 wording item if applied).
Do-not-touch: current ranges; B.cl low-C labelling; G–A♭–C–E♭ timpani tuning; horn layout and rests.

## Cycle 177 (texture, Adler 8) → v197
Accepted: Hn 1·2 enter late at 136 in the recap (varies 23–25's scoring).
Closed: Hn 1 B5 at 106 — keep undoubled; optional part-only 8va bassa ossia at the parts stage.
Do-not-touch: 103–110 scoring (incl. Ob 1 rest 103–114, Hn 1 undoubled); fugato entries 85–96; transition hand-offs 34–41; wedge 111–117.

## Cycle 178 (expression, Adler 7) → v198
Accepted: Fl 1 mp at 109–110 (reverses c167 on register grounds); harp "étouffez" at 182 (closes wording item).
Settled: Fl 1 dynamic at 109–110 has now changed twice (c167, c178). Do not change it again; if it is still a problem, the alternative is for Fl 1 to rest at 109–110.

## Cycle 179 (holistic, Adler 16) → v199
Accepted: Fl 1 drops out after the G6 sf at 41.
Do-not-touch: motto colours and order (1–8, 73–76, 77–83, 117–121, 175–182); climax chain 117–130 with Fl 1's octave drop at 124; brass under the horn call 41–42; scoring of 158–166.

## Cycle 180 (cyclic, A&S 28) → v200
Accepted: top line at 115 approaches D from E♭ (no D♭→D♮ in the top voice).
Do-not-touch: Neapolitan settings at 7–8, 20–22, 140–142, 172–174, 178, 180; D♭ key held back for movement II.

## Cycle 181 (melody, Adler 11) → v201 (no change)
Kept: Hn 3·4 unison G5 at 158–161; held Hn 3·4 at 131–134. Parts note: "a2 with 3." in Hn 4 at 158–161.

## Cycle 182 (harmony, A&S 30–31) → v202
Accepted: Fl 1 F♭5 at the end of 75 (no cross relation into 76).
Do-not-touch: bar 73; the bar-60 join; 77–83; 111–116; 117–130; 156–166.
Open (relay from mvt II c071–c080): remove the harp retune cue at 176 ("Retune lowest D string (D1) / to D♭ for movement II"); movement II no longer uses D♭1.

## Cycle 183 (form, A&S 6–8) → v203
Accepted: plain V (no seventh) at the medial caesura 41–42 (Cl 1, Hn 3, Tpt 3); harp retune cue at 176 removed (closes the mvt II relay item).
Do-not-touch: horn call and dynamics at 41–42; final cadence bass 177–178 (motto).

## Cycle 184 (orchestration, Adler 5) → v204
Accepted: clarinets rest 97–102 (register clash with the theme's lower octave; c157 and c184 for, c159 against). Settled; do not reverse without new evidence.
Open: Vln I A♭6 at 140–141 pre-empts the 160 climax; proposed Vln I 8vb at 139–142 with Fl 1 keeping A♭6 (conflicts with the cycle 24/61 rule).
Do-not-touch: second-group plan (Hn+Vc 47–55, violins an octave higher from 56); fugato entry order 85–96; coda string spacing 175–182.

## Cycle 185 (parts stage, MOLA) → v205
Accepted: separate parts build (build-parts.sh, parts-gen.py, parts-lib.ily, parts-clefs.ily; 30 parts in partsout/); transposed key signatures; part-only markings; harp pedal marks score-only. Full score unchanged.
Open: composer name; B.cl clef choice at 91–106.
Process: after each promote, run build-parts.sh to refresh the parts.

## Cycle 186 (playability, Rimsky ch. I) → v206
Accepted: sul G ends at 100; staggered breaths 117–123 and 158–163; Hn 1 at 154 lowered; wedge brass pp cresc. under p horns at 111–116.
Open (protected): harp inaudible at f under the ff tutti at 162.
Do-not-touch: cello high notes and theme leaps 47–55; brass/horn layout 117–123 and 158–161 (apart from breaths); timpani tuning plan; harp voicings 147–166.

## Cycle 187 (texture, Rimsky ch. II) → v207
Accepted: Cl 1 unison with Vln II at 94–95; Cl 1 at 162 without G♮ against G♯.
Open (optional, protected): Fl 1 rest / Ob 1 lower-octave doubling at 162–163.
Do-not-touch: Hn+Vc 47–55; Hn+Vla 147–155; Hn 2+Cl 1 counterline 56–68; codetta doublings 69–72; Fl 1 over Ob 1+Vln I 97–102; low motto 1–4; chorale 175–179.

## Cycle 188 (expression, Adler 10) → v208
Accepted: Tbn 2 chorale slurs; Hn 2 slur at 156; horn legato slurs 103–106 and 164; "dolce" at 175.
Open: Hn 1 part shows no end level after the diminuendo at 162 (protected exit order).
Do-not-touch: horn solos/swells 47–55 and 147–155; graded brass 27–32, 131, 167; trumpets' soft dynamics 113–116; horn call 41–42; chorale 175–179 notes, dynamics and slurs.

## Cycle 189 (holistic, A&S 20–32 / Bruckner 8, Beethoven Op. 37) → v209
Accepted: timpani first-group rhythm at 179–180; Hn 2 at 44.
Closed: bass tritone 160–161 (cycle 172 note).
Do-not-touch: coda order of events 163–182; ♭VI–°7–V climax at 160–161; Ger6–V at 12–13.

## Cycle 190 (cyclic, Adler 17) → v210
Accepted: horn call at 13–14 undoubled (Vla and Hn 3 adjusted).
Open (optional): Vln II D5 at 150 under the C.a. answer.
Do-not-touch: motto colours and order (1–4, 5–8, 73–76, 117–121, 171–182); flute motto over the A♭ pedal 73–76; C.a./Vc duet 171–174; chorale canon 175–182 with the timpani link 179–180; viola E♭→E♮ and five tied parts at 182.

## Cycle 191 (melody, A&S 3) → v211
Accepted: tenuto on the appoggiatura at 59 and 110.
Open, now supported by two critics (c184, c191): Vln I A♭6 at 140–141 pre-empts the climax at 160. The next orchestration critic (cycle 194) should decide it and apply c184's tested fix (Vln I 8vb at 139–142, Fl 1 keeps A♭6) if it holds up, despite the cycle 24/61 rule.

## Cycle 192 (harmony, A&S 27) → v212
Accepted: Hn 3/Tbn 1 hold C into B at 28 (no anticipated resolution); final dominant's 7th resolves at 177–178 (Vln II, Vla).
Open: check whether the bar-28 fix also applies to the parallel tutti bars (140, 168) for consistency.
Do-not-touch: ♭9-on-top dominants at 83, 117, 122; common-tone A♭ 82→83 with the fugato's A♭–G answer at 85; soprano 13th at 145–146.

## Cycle 193 (form, A&S Unit 15) — v213, no score change
- Accepted: none.
- Closed: c192 open item (B sounded before the tune's C→B at 132/142/168) — no clash.
- Kept: 70→71 bass D♮ / soprano D♭ cross-relation (normal vii°7/V→V7; bass protected c103).
- Open, for cycle 194 to decide: Vln I A♭6 at 139–142. c184, c191 and c193 support Vln I 8vb with Fl 1 keeping A♭6.
- Cyclic note: movement III could put its second group in E♭ (III is never a key in mvt I).

## Cycle 194 (orchestration, Casanelles ch. 6) — v214
- Accepted: Vln I 8vb at 139–142 (Fl 1 alone keeps A♭6; violins first reach A♭6 at 160). Closes the A♭6 open item. Do not restore the violins' A♭6 at 140.
- Accepted (optional): Vln II 150 `<f'' a''>` to avoid the unison with the C.a. D5 (closes the c190 item).
- Closed: bar-28 fix at 140/168 is not applicable (no C→B in the tune there).
- Kept/protected: bar 82 Fl 2 under Tpt 1; bar 122 A♭6.

## Cycle 195 (engraving, Adler ch. 2) — v215
- Accepted: Vc duet 171–174 one bow per bar; Cb 102 `f,,2. r4` before pizz.; "change bow at will" at Cb 13–14 and Vc/Cb 72–76; Vln II div./unis. at 73–74 and 124–125.
- Open (composer): Vln I fff→p single bow at 124–125 (Ob 1 shares the slur; c88 identical-slur rule).
- Do not touch: bowing scheme at 15–32 and 131–142; div./metà/unis. at 47–69 and 147–177; sul tasto→ord. at 147–155.

## Cycle 196 (playability, Sebesky ch. 2) — v216
- Accepted: B.cl part in treble clef throughout (closes the B.cl clef item at 91–106); Cl 2 quarter rest on beat 4 of 120.
- Open (composer): Ob 1 low link at 45–46 → cor anglais; C.a. 5–9 "breathe ad lib." in the part.
- Note: the v215 full.midi was stale; v216 is rebuilt.

## Cycle 197 (texture, Adler ch. 11) — v217
- Accepted: cellos mp→f at 88–91 so the fugato entry is heard; Ob 1 replaces Fl 1 as the doubling at 162–163 (closes c187).
- Closed (decided, no change): c104 Cl 2 27–32; c147 clarinets rest 131–134; c147 Bsn 1 69–70; c161 no fill at 150; c167 56–68; c169 Fl 1 117–119; c173 Vln II 107–108; c174 Tpt 3/Tbn 1 E♭4 167–169; c186 harp at 162.
- Still open (must be decided by cycle 200, since there are no later cycles): c174 Tpt 1 A♭5 at 72; c195 Vln I single bow at 124–125; c196 Ob 1 link 45–46 → cor anglais; c196 C.a. 5–9 "breathe ad lib."; c194 Vln II 150 (keep or revert); composer name on the title page.

## Cycle 198 (expression, A&S Unit 21) — v218
- Accepted: Vln I/Ob 1 slur split at 125 (closes c195); Hn 1·2 dim. at 44 (7–6 suspension); C.a. part-only "(breathe ad lib.)" at 8 (closes c196 breath item).
- Closed (no change): Ob 1 link 45–46 stays on oboe (c196); Vln II 150 `<f'' a''>` kept (c194); Tpt 1 A♭5 at 72 kept (c174); composer name not printed.
- No open items remain.

## Cycle 199 (holistic, Casanelles on Mahler 1) — v219
- Accepted: duplicate "a2" removed at Cl 103.
- Kept: c194 and c197 changes reviewed and confirmed; no open items.

## Cycle 200 (final release check) — v220. Series 101–200 complete.
- Accepted: "attacca" in all parts; front-page timpani tunings corrected; release subtitle with version and date.
- No open items. Cyclic notes are in c200.md (correction: since c194 the violins reach A♭6 only at 31, 72, 122 and 160; at 140 it is Fl 1 alone).

## Cycle 201 (parts layout, attacca page turns) — v221
- Accepted: parts that cross the join end movement I on an even page (strings 2 pp; Cb cover + 3 pp; Hn 3·4 and timpani cover + 1 p). Score unchanged.
- Do not touch: these layouts; any change to the parts must keep each of them ending on an even page.

# Series 3 (Dan, 2026-10-19): cycles 221–420, cycle N reviews vN → v(N+1)
Kit: kit/, BRIEF3.md, LENSES3.md, READING3.md, MASTERS.md. Movement I may change freely, including its themes and foreshadowing of movements II–IV; changes that touch quoted material are reported to the other movements.

## Cycle 221 (Melody and memorability; Aldwell & Schachter Unit 20 Melodic Figuration (aldwell-schachter PDF 327-345)) → v222
- Accepted: Vln I·II turn C–D♭–C–B♭ on beat 4 of 56 (tTwo), the motto's C–D♭–C inside the S restatement (A&S PDF 333–339); the horn/cello statement at 47 stays plain.
- Open / not applied: None. Kept with reasons: P descent 21–22 (A&S PDF 333), échappée D♭6 at 63 (PDF 334–335).
- Do-not-touch: horn call 13–14; motto spelling and D♭; P descent 21–22; 63–64.
- Cross-movement: none (bar 56 is not quoted elsewhere).

## Cycle 222 (Harmony and voice leading; Aldwell & Schachter Unit 5 Procedures of Four-Part Writing (aldwell-schachter PDF 74-91)) → v223
- Accepted: Vln II G4 on beat 4 of 46 (V7 of A♭ regains its third; no hidden octave into 47) (trans); Vc D3 tied at 145 instead of doubled leading tone B2 (recOne); Hn 3 B3→C4 at 165–166 so the leading tone resolves (recTwo). A&S PDF 76, 80, 83, 87–88.
- Open / not applied: None. Kept: dominant without third at 16 (protected; PDF 82); tutti doublings of tendency tones at 12–13, 26–27, 142–143 (PDF 84–87); the bar-162 doubling 'fifths' (PDF 85).
- Do-not-touch: 12–13 Ger6–V; stop-chord doublings 26–27, 142–143; bar 16.
- Cross-movement: none.

## Cycle 223 (Form, pacing and proportion; Aldwell & Schachter Unit 14 V as a Key Area (aldwell-schachter PDF 211-229)) → v224
- Accepted: none (score unchanged).
- Open / not applied: None. Kept with reasons: 73–80 exposition→development (A&S PDF 217–220); recap turn to iv at 139–143; coda without root-position V–i (PDF 219, protected c183 bass); F♯ doubling at 116→117 (PDF 84–85).
- Do-not-touch: 73–80; 139–146; 174–179; 111–117.
- Cross-movement: none.

## Cycle 224 (Orchestration; Rimsky-Korsakov ch. I Comparison of resonance and combination of tone qualities, and ch. III Harmony: number of parts, distribution, strings, woodwind (rimsky-principles PDF 51-53, 81-99)) → v225
- Accepted: Hammered tutti 28–31: Tpt 2, Tpt 3 and Hn 2 no longer double the chromatic bass D–E♭–E–F (Tpt 2 G4 at 28, B♭4 at 30; Tpt 3 F4 F4 G4 A♭4–F4 at 28–31; Hn 2 G4 at 30) (Rimsky-Korsakov PDF 82–84); Cl 1 F4 at 145–146 so the clarinets hold a third, not an open fifth (PDF 90, 97) (recOne).
- Open / not applied: None. Kept: stop-chord doublings 26/138 (PDF 98); Vln II divisi 111–116; B.cl + Vc unison 1–4 (PDF 52).
- Do-not-touch: bass, tune and rhythm of 27–32; 26/138 stop chords.
- Cross-movement: Inner brass of the hammered tutti 28–31 changed (finale told).

## Cycle 225 (Engraving and notation (Gould's *Behind Bars*, MOLA); Gould ch. 1: stave, clefs, noteheads, stems, tails (gould-behind-bars PDF 17-30)) → v226
- Accepted: Middle-line stems follow their neighbours (Gould PDF 27–28): gould-middle-line-engraver in global.ily, switched on in score.ly and parts-gen.py (48 places, e.g. motto D♭3 at 3 and 178); solo stems up on shared staves at Fl 1 64–65, Ob 1 121, Hn 1 106, Bsn 1 130 (tTwo, dev).
- Open / not applied: None. Kept: forced stems inside two-voice bars (PDF 28); stem thickness; clef plan (PDF 21–23); cymbal noteheads (PDF 26).
- Do-not-touch: clef plan; Hn 3·4 bass clef 103–106.
- Cross-movement: none.

## Cycle 226 (Playability, instrument by instrument; Adler ch. 2 Bowed String Instruments: divisi, bowing, harmonics (adler1 PDF 24-70)) → v227
- Accepted: Vln I 11–13 slur ends on the crotchet A♭5, down-bows marked at 12 and 13 (Adler PDF 38–40) (intro); Vc pizz. E2 on beat 3 of 63 cut so the return to arco at 64 has time (PDF 54; Cb and Bsn 2 keep the E♮) (tTwo); Vln II 'unis.' moved to beat 3 of 73 (PDF 30) (clos).
- Open / not applied: None. Kept: long pp slurs 1–3, 175–179 (one bow at pp); ff triple-stops at 33 on open strings.
- Do-not-touch: notes of 9–13; bass E♭–E♮–F 63–64.
- Cross-movement: none.

## Cycle 227 (Texture and counterpoint; Adler ch. 5 foreground, middleground, background; strings as accompaniment (adler1 PDF 132-167)) → v228
- Accepted: Vln II and violas enter after the P pickup at 15 and 17 (r4 r8 then tie), so the pickup sounds alone (Adler PDF 135) (tOne); Cb rest 85–89 so the fugato subject in the cellos is heard alone, return at 90 (PDF 145) (dev); violas 156–157 re-voiced in sixths with the cellos, no unison with Vln II (PDF 135, 144) (recTwo).
- Open / not applied: None. Kept: cello countersubject above the second entry 88–90 (B→C resolution); viola arpeggio 97–102; violas 60–61 (protected).
- Do-not-touch: P melody 15–18; fugato subject/countersubject; harmony at 156–157 (c182).
- Cross-movement: none (melody of 15–17 unchanged).

## Cycle 228 (Expression; Rimsky-Korsakov ch. IV sf-p chords, crescendo and diminuendo (rimsky-principles PDF 129-136)) → v229
- Accepted: Tam-tam 122–126 now diminuendo from 124 with 'damp gradually' to p at 126 (Rimsky-Korsakov PDF 135, 130) (dev); brass crescendo into the arrivals: bar 121 Hn 1–4, Tbn 1·2, B.tbn; bar 40 Hn 3·4, Tbn 1·2, B.tbn (PDF 130, Ex. 255) (dev, trans); Cl 1 B4 at 177 fades (b'2\>) instead of stopping at pp (PDF 130) (coda; protection on coda notes and levels kept).
- Open / not applied: None. Kept: trombones mf at 12; trombone/tuba f at 72; sf-p at 33 and 41; crash l.v. at 160.
- Do-not-touch: coda notes, levels and timing; graded brass at 12.
- Cross-movement: none (tam-tam line in coherence/mvt1.md to be updated).

## Cycle 229 (Holistic comparison with one specific master first movement, the one named in your task (see MASTERS.md). Would a conductor believe a master wrote this? Also compare with the version 10 cycles earlier and flag anything that got worse.; Rimsky-Korsakov examples No. 1-60 (rimsky-principles PDF 173-240)) → v230
- Accepted: Vln II an octave below Vln I at the climax 158–161 (E5–A♭5), as at 31 and 122 (Rimsky-Korsakov PDF 58–62; Brahms 2/i letter E); reopens c167's unison rule, answered (no divisi involved) (recTwo); Cb unison G2 and F2 at 6–7 instead of divided octaves (PDF 62 Note II) (intro).
- Open / not applied: Kept: Cl 1 above Ob 2 at 158–161 (protected line; fff).
- Do-not-touch: low motto 1–8; chorale and last motto 175–182.
- Cross-movement: none quoted; coherence/mvt1.md facts updated (6–7 basses; Vln II no longer on A♭6 at 160).

## Cycle 230 (Cyclic design and emotional arc across four movements; Aldwell & Schachter Unit 32 chromatic tonal areas and large-scale motion (aldwell-schachter PDF 584-606)) → v231
- Accepted: Cl 1 at 78: re-struck A♭5 spelled G♯5 and cut to one beat (gis''4) r4), so the E-major beat is a common-tone link, not a clash with the horns' G4 (A&S PDF 586–588, 596, 599–600) (dev).
- Open / not applied: No foreshadowing added: movement I already holds seeds of the scherzo (79 G–F♯–F–E = scherzo theme A bar 2; P bar 2 rhythm = motive x; Hn 1 D♯5 at 106) and the finale (D♯/E♭ at 108; Ger6 at 12). Seeds recorded in coherence/mvt1.md.
- Do-not-touch: E♭/E♮ viola thread 166, 182; attacca join; 77–83 key circle; seeds at 79, 106, 108, 12.
- Cross-movement: Scherzo told that I 79 carries its theme A bar 2; finale told its record of I 138 is wrong (violas F4–B4, Tpt 1 A♭4, Tpt 2 F4).

## Cycle 231 (Melody and memorability; Rimsky-Korsakov ch. II Melody: strings, unison and octave doublings (rimsky-principles PDF 54-63) and the examples it cites) → v232
- Accepted: Cellos take the S lower octave with Vln II and C.a. at 97.4–102 (pickup F♯3, tenor clef 98–102), as at 158–161 (Rimsky-Korsakov PDF 54–62, Ex. 30, 32) (dev).
- Open / not applied: None. Kept: 15–22, 56–63, 107–110, 147–155, 177–182.
- Do-not-touch: 97–102 brass counter, viola arpeggio, Vln II sul G, B.tbn F♯3.
- Cross-movement: none.

## Cycle 232 (Harmony and voice leading; Aldwell & Schachter Units 9-10 Leading to V; the Cadential 6/4 (aldwell-schachter PDF 134-162)) → v233
- Accepted: Cadential 4–3 over V tied across the barline at 66→67 and 164→165, resolving on the second eighth (A&S Ex. 10-6a, PDF 149–160); the six-beat dominant (c023/c032) kept. Vln I·II (tTwo, recTwo); Hn 3 B3 on beat 2 of 165; harp G5–D6–F6 at 165 (recTwo).
- Open / not applied: None. Kept: leap to the 4th at 54 (Ex. 10-3c; protected S); tonic 6/4 at 175; Neapolitan→I at 7→8 and 178→179 (motto); doubled 4ths at 142/158.
- Do-not-touch: S 47–55; motto neighbour chords 7–8, 178–179; six-beat dominant 66, 164.
- Cross-movement: none.

## Cycle 233 (Form, pacing and proportion; Aldwell & Schachter Unit 26 Diatonic Modulation, incl. modulation and form (aldwell-schachter PDF 442-461)) → v234
- Accepted: none (score unchanged).
- Open / not applied: None. Kept: key plan C–A♭–(dev ends on F)–V pedal–C (A&S PDF 454–456); E♭ passing cadence at 41 (PDF 447–448); no B♮ 128–131 (major dominant; protected); B minor 97 and D minor 103 as passing keys; recap 139–166 (PDF 451–455).
- Do-not-touch: key plan; 41–47; 117–131; 139–166.
- Cross-movement: none.

## Cycle 234 (Orchestration; Rimsky-Korsakov ch. III Harmony: brass and combined groups; overlaying, crossing, enclosure (rimsky-principles PDF 100-114)) → v235
- Accepted: Bar 72 Tbn 1 E♭4, Tbn 2 C4 so the brass chord has its fifth in a close layout (Rimsky-Korsakov PDF 100–101) (clos); Hn 4 G3 at 166 instead of doubling the bass C (PDF 100) (recTwo); Hn 4 D4 with Hn 3 at 40 so the leading tone has a horn pair (PDF 102; Adler2 PDF 44) (trans).
- Open / not applied: None. Kept: B.tbn + tuba unison 114–116; trombone dissonances 83, 122; Tpt 3 with Tbn 1 141–142, 167–168; strings in the chorale 175–179; no stopped/muted brass.
- Do-not-touch: chorale 175–179; 83, 122.
- Cross-movement: none.

## Cycle 235 (Engraving and notation (Gould's *Behind Bars*, MOLA); Gould ch. 1: beams (gould-behind-bars PDF 31-41)) → v236
- Accepted: Beam slopes per Gould PDF 33–37: gould-beam-positions callback in global.ily, on in score.ly and parts-gen.py; flattens steep arpeggio beams (Vc 56–68, 157–166; harp 62–65), concave/repeating groups (Vla 69–71, 97–102, 163, 165) and high flute groups (29, 139–140); 94 of 500 beams; no notes or groupings change.
- Open / not applied: Kept: clarinet voices interlocking 117–121; Vc stems at 61.
- Do-not-touch: c125 harp beams; c225 stem rule.
- Cross-movement: none (engraving only).

## Cycle 236 (Playability, instrument by instrument; Adler ch. 3 Individual Bowed Strings: ranges and technique (adler1 PDF 71-109)) → v237
- Accepted: Cb 'change bow at will' at bar 3 (8-beat slur at Lento; Adler PDF 108) (intro).
- Open / not applied: None. Kept: Cb arco→pizz. 46→47 at pp; Vln II fff tremolo double stops 122–123 without div. (PDF 76); viola double stops 158–161; viola alto clef 151–153 (PDF 85).
- Do-not-touch: lead-in 43–47; 158–166 scoring.
- Cross-movement: none.

## Cycle 237 (Texture and counterpoint; Adler ch. 15 polyphonic texture (adler2 PDF 172-186)) → v238
- Accepted: Fugato 94–95: violas (with Bsn 1 an octave below) take the free voice f'2.( aes'4~ | aes'4 ges'4 f'2), keeping three moving parts at the fourth entry (Adler2 PDF 175–176) (dev).
- Open / not applied: None. Kept: woodwind-only head 103–106; brass-only motto 117–121; Bsn 1 at 167–169 (c150); all voices f at 91–96.
- Do-not-touch: fugato subject, countersubject, entries and colours (c142).
- Cross-movement: none.

## Cycle 238 (Expression; Adler ch. 2 bowing and its expressive effect (adler1 PDF 36-55)) → v239
- Accepted: Portato dashes on repeated notes under a slur (P head second bar at 16, 28, 132, 144, 168; figure at 34–36, 78–79, 104, 108, 128; counterlines 59, 161; 38 places) (Adler PDF 42–43); bowings: down-bows at 161 (Vln I·II, Vc, Cb) and Vc 158/160 so 162 lands down-bow; 34–41 head entries and sf at 41; Vln II 69–71; Vc up-bow at 139 (answers c195: the cello line postdates that scheme) (PDF 38, 42–43).
- Open / not applied: None. Kept: cello hemiola 23–26, 135–138; long pp coda bows; sul tasto, pizz., tremolos.
- Do-not-touch: notes, slurs; hemiola bowing.
- Cross-movement: P head now has a tenuto on its repeated C (c4--) at 16, 28, 132, 144, 168; finale told for its 200.

## Cycle 239 (Holistic comparison with one specific master first movement, the one named in your task (see MASTERS.md). Would a conductor believe a master wrote this? Also compare with the version 10 cycles earlier and flag anything that got worse.; Rimsky-Korsakov examples No. 61-125 (rimsky-principles PDF 241-305)) → v240
- Accepted: none (score unchanged); holistic vs Beethoven 5/i and v229: no regressions.
- Open / not applied: Closed (decided by the composer): partial divisi at 124–125 stays (c196 playability). Kept: sectional development; collapse 123–126; Cl fourth at 35; low four-horn call 41–42; short coda (9%) for the attacca.
- Do-not-touch: 117–130 chain; 143–150 lead-in; coda length.
- Cross-movement: none.

## Cycle 240 (Cyclic design and emotional arc across four movements; Aldwell & Schachter Unit 26 modulation and form (aldwell-schachter PDF 442-461)) → v241
- Accepted: none (score unchanged).
- Open / not applied: None. Records updated: seeds list (37–44 B♭ pedal into E♭ = finale's transition; 73–76 = movement II 3–6; single-pitch E♭4/E4 thread); themes-mvt1.md lines on movement II 64 and Vln II at 160 corrected.
- Do-not-touch: 37–44; 73–76; 154–155 and 165–166 soft C-major cadences (no forte C major before the finale); attacca join.
- Cross-movement: none in the score.

## Cycle 241 (Melody and memorability; Rimsky-Korsakov ch. II Melody: woodwind, brass, combined groups (rimsky-principles PDF 64-80) and the examples it cites) → v242
- Accepted: Oboes swap lines at 158–163: Ob 1 plays the countermelody in unison with Cl 1 over Hn 3·4; Ob 2 takes the tune's middle octave with Tpt 1 and Vln II (Rimsky-Korsakov PDF 67, 70, 75, 79) (recTwo). Answers c229/c236: the line and fff are kept.
- Open / not applied: None. Kept: Fl 1 with violas on S 107–110; horn/trombone unison motto 117–121 (protected).
- Do-not-touch: motto, P, S, horn calls; 117–121; 107–110.
- Cross-movement: none quoted; mvt1.md climax line updated (Ob 2, not Ob 1, an octave below at 160).

## Cycle 242 (Harmony and voice leading; Aldwell & Schachter Units 11-13 VI and IV6; supertonic and subdominant sevenths; other uses of IV and VI (aldwell-schachter PDF 163-210)) → v243
- Accepted: Tpt 1 holds B4 at 133 (was A♭4: two augmented seconds B–A♭–B; A&S Ex. 11-10d, PDF 169) (recOne); Cb and Bsn 2 D at 25 beat 4 so the bass avoids A♭–B–C into the stop chord: iv – iiø7 – vii°7 (A&S Ex. 11-14b, PDF 171–179) (tOne).
- Open / not applied: None. Kept: 7̂–6̂ top line at the deceptive cadence 161→162 (B→C forte reserved for the finale); iv7 seventh at 10 (protected chain); C.a. leap at 153→154.
- Do-not-touch: stop chord 26 root B (c152); 9–13 chain; 131–134 theme (c84).
- Cross-movement: none (bar 25 bass and Tpt 1 at 133 are not quoted).

## Cycle 243 (Form, pacing and proportion; Aldwell & Schachter Unit 32 Chromaticism in Larger Contexts (aldwell-schachter PDF 584-606)) → v244
- Accepted: none (score unchanged); proportions measured: development 0.85, recapitulation 0.61 of the exposition.
- Open / not applied: None. Considered and rejected: longer approach to 158 (c083, c143), cutting 103–110, removing the collapse 123–126, longer forte coda. Kept: 77–83 key circle; recap changes; three A♭ climaxes; 117–131.
- Do-not-touch: section lengths; 77–83; 117–131; recap plan.
- Cross-movement: none.

## Cycle 244 (Orchestration; Rimsky-Korsakov appendix of single tutti chords (rimsky-principles PDF 505-510) and the tutti examples cited in ch. IV) → v245
- Accepted: Held brass harmony at the 160 climax (Tpt 3, Tbn 1·2, B.tbn, tuba) ff under the fff tune; crescendo at 159 removed, redundant ff at 162 dropped (Rimsky-Korsakov PDF 505, Ex. 206, 209; PDF 41) (recTwo).
- Open / not applied: None. Kept: six instruments on D4 in the 170 stop chord (matches 27–32; cross-movement list); low trumpets at 122; dynamics at 82 (protected).
- Do-not-touch: fff only at 122 and 160; stop chord layouts.
- Cross-movement: none (no notes changed).

## Cycle 245 (Engraving and notation (Gould's *Behind Bars*, MOLA); Gould ch. 1: ledger lines, octave signs, rests (gould-behind-bars PDF 41-52)) → v246
- Accepted: gould-rest-snap callback: 15 shared-stave rests moved onto the line grid (Gould PDF 49, 51) (global.ily, score.ly, parts-gen.py); the score's 8va signs no longer print in the Vln I part (31, 71–72, 121–124), harp 8va kept (PDF 47) (parts-lib.ily, dev.ily).
- Open / not applied: None. Kept: 8va at 31/122 vs at pitch at 140/160 in the score; horn ledger lines at 13 and 141.
- Do-not-touch: c135 rest overrides; clef plan; layout.
- Cross-movement: none.

## Cycle 246 (Playability, instrument by instrument; Adler ch. 4 Plucked Strings: harp and pedalling (adler1 PDF 110-124)) → v247
- Accepted: Harp: 'étouffez' at 68 so the V7 chord does not ring over the deceptive cadence (Adler PDF 113–117) (tTwo); B♮ pedal change at 158 dropped and A♮ moved to 161 (recTwo); 47 pedal diagram sets G♭, change at 50 removed (PDF 112) (global.ily, tTwo); answers c136 (diagram still correct).
- Open / not applied: None. Kept: C2 into D♭2 at 51→52; 56–59 figures; F♭ spelling at 56; harp at 162.
- Do-not-touch: harp part layout.
- Cross-movement: Harp ends movement I with the B pedal on B♭ (movement II told).

## Cycle 247 (Texture and counterpoint; Adler ch. 17 The Orchestra as Accompanist (adler2 PDF 256-290)) → v248
- Accepted: Violas hold G3 at 144–146 instead of doubling Bsn 1's answer at pitch (Adler2 PDF 257–258, 274) (recOne); Vln II holds G4 at 175–176 so Cl 1's horn-call recall starts on its own E♭4 (PDF 264, 274, 283) (coda).
- Open / not applied: None. Kept: viola pad 47–52 (protected); Hn 3 C4 at 147; brief overlaps at 153, 172, 177; fugato and bass.
- Do-not-touch: 47–52; 147; chorale 175–179 notes of brass and Vln I.
- Cross-movement: none.

## Cycle 248 (Expression; Adler ch. 11 climactic uses of brass (adler2 PDF 37-40) and ch. 15 special effects (adler2 PDF 187-196)) → v249
- Accepted: Per-bar < > swells of 47–52 copied onto the six tune parts of the ff B-minor S at 97–102 (Fl 1, Ob 1, C.a., Vln I·II, Vc) (Adler2 PDF 38 Ex. XI-20, PDF 188) (dev).
- Open / not applied: None. Kept: fff restated at 122; graded brass at 160 (c244); sf at 41, fp at 33; sub. p at 62 and 84.
- Do-not-touch: 97–102 counter, viola arpeggio, bass (c128, c186, c231).
- Cross-movement: none.

## Cycle 249 (Holistic comparison with one specific master first movement, the one named in your task (see MASTERS.md). Would a conductor believe a master wrote this? Also compare with the version 10 cycles earlier and flag anything that got worse.; Rimsky-Korsakov examples No. 126-200 (rimsky-principles PDF 305-375)) → v250
- Accepted: none (score unchanged); holistic vs Schumann 4/i and v239: no regressions; c241 and c244 judged improvements.
- Open / not applied: None. Kept: no new development theme; varied rescoring of returns (Rimsky PDF 118); grading at 69–72 and 167; trombone use; discords at 122, 170; retransition 117–130; soft attacca ending.
- Do-not-touch: coda dynamics; 117–130.
- Cross-movement: none.

## Cycle 250 (Cyclic design and emotional arc across four movements; Casanelles ch. 5 Hyperorchestral aesthetic frameworks: themes and their transformation (hyper-orchestra PDF 199-254)) → v251
- Accepted: Bar 160: the clashed cymbals are replaced by one soft-stick suspended-cymbal stroke fff l.v. ending the 159 roll, so the finale's crash at IV 223 is the symphony's first clashed cymbals (Casanelles PDF 227, 235–238; Dvořák 9 single stroke); percussion is one player (front page, staff name, part header, labels) (recTwo, dev, coda, score.ly, parts-gen.py).
- Open / not applied: Records corrected: I 138 has Tpt 1 B4 and Hn 1 A♭4 (not Tpt 1 A♭4); mvt1.md brought up to v251. Recommended to movement II: P-head articulation at II 63–64 (slur and portato as in I since v239). Recommended to the finale: limit its C7 rule to violins and flutes (I's harp reaches C7 at 56).
- Do-not-touch: 159 roll (c108); join into movement II.
- Cross-movement: Finale told (cymbal; 138 layout; C7 rule); movement II told (63–64 articulation).

## Cycle 251 (Melody and memorability; Adler ch. 3 Individual Bowed Strings: melodic writing for violin, viola, cello, bass (adler1 PDF 71-109)) → v252
- Accepted: Cellos sul G for the motto at 1–3 and 175–178 (no open D, the sixth on one string; Adler PDF 73–76); Vln I sul D for the last motto 177–182 (PDF 73–75) (intro, coda).
- Open / not applied: None. Kept: E string at 62–63 (c141); cello S head on the A string at 171–174 (PDF 72, 99).
- Do-not-touch: coda notes, dynamics, timing (c228/c249).
- Cross-movement: Vln I's tied C5 into movement II is now sul D (movement II told).

## Cycle 252 (Harmony and voice leading; Aldwell & Schachter Unit 17 Diatonic Sequences (aldwell-schachter PDF 263-288)) → v253
- Accepted: Cl 1 at 164: A♭4→G4 instead of the augmented second A♭4→B4 (A&S PDF 268, Ex. 17-26c; c152 rule that borrowed A♭ falls to G); unused recTwoCounter kept identical (recTwo).
- Open / not applied: None. Kept: motto statements over C–A♭–B♭ at 33–36 (c102); doubled D at 40→41 (c234); F♭ against F at 38; B4–A♭4 at 114→115 (protected wedge).
- Do-not-touch: 33–36; 111–116 wedge.
- Cross-movement: none.

## Cycle 253 (Form, pacing and proportion; Rimsky-Korsakov ch. IV Composition of the orchestra: tutti, range limits, transfer of phrases, sf-p, crescendo and diminuendo (rimsky-principles PDF 115-136)) → v254
- Accepted: Trombones (1·2, bass) enter p< at 40 and swell into the sf at 41 (was f<) (Rimsky-Korsakov PDF 127, 130, 136) (trans).
- Open / not applied: None. Kept: transition 33–46 proportions and stages; closing 69–76 (12–13% of the exposition); trumpets f at 69.
- Do-not-touch: 33–46 route; 69–76.
- Cross-movement: none.

## Cycle 254 (Orchestration; Adler ch. 15 Scoring for Orchestra: unison-octave tutti, foreground and background (adler2 PDF 146-158)) → v255
- Accepted: Bar 82: Fl 2 doubles Fl 1 on the top octave of the head (was G4–E♭5 under Tpt 1); Cl 2 joins Cl 1 on the head (was buried E♭4 eighths), 'a2' (Adler2 PDF 150–152) (dev). Answers c144/c194: the middle octave still has five instruments.
- Open / not applied: None. Kept: climaxes 122 and 158–161; brass head over held winds at 167–169 (finale's reserve).
- Do-not-touch: 167–169; 122; 158–161.
- Cross-movement: none.

## Cycle 255 (Engraving and notation (Gould's *Behind Bars*, MOLA); Gould ch. 1-2: rhythmic spacing, spacing of symbols, chords, unisons, double-stemmed writing (gould-behind-bars PDF 53-68)) → v256
- Accepted: Part-combine fixes (Gould PDF 60–65): Hn 3·4 unisono at 158; Cl 1·2 chords at 43; Ob 1·2 apart 41–42 (trans, recTwo).
- Open / not applied: None. Kept: whole-note placement at 76, 176; Fl/Ob overlap at 134 (PDF 66); rhythmic spacing; Fl 1·2 at 41–43.
- Do-not-touch: c145 spacing 73–76.
- Cross-movement: none.

## Cycle 256 (Playability, instrument by instrument; Adler ch. 6-7 Woodwind choir and individual woodwinds: breathing, registers, technique (adler1 PDF 168-232)) → v257
- Accepted: Cbsn breathes on beat 4 of 134 (14.8 s of low crotchets at 131–138; Adler PDF 230) (recOne).
- Open / not applied: None. Kept: B.cl low C at 92–93, 105–106 (c146); oboe low notes at p 43–46; long single-breath phrases; bassoon low fifth; staggered breaths at 117–126.
- Do-not-touch: c146 B.cl low C.
- Cross-movement: none.

## Cycle 257 (Texture and counterpoint; Adler ch. 16 The Orchestral Transcription (adler2 PDF 197-255)) → v258
- Accepted: Vc rests beat 1 of 91 so the third fugato entry's C is not masked (Adler2 PDF 213, 229, 239) (dev); Vln II tremolo halo at 152 moves to A5/C6 on beats 3–4 so the violas' and Cl 1's peak F5 is fresh (PDF 217, 224, 229) (recTwo).
- Open / not applied: None. Kept: Ob G4 dovetail 145 (c144); viola arpeggio 60–61; 47–55; short held-pitch entries.
- Do-not-touch: fugato entry plan 85–96; Cb pulse 15–22; climax 158–161.
- Cross-movement: none.

## Cycle 258 (Expression; Casanelles ch. 4 dynamics layering and expression in performance (hyper-orchestra PDF 145-161) and ch. 6 volume and dynamics (PDF 290-291)) → v259
- Accepted: Vln I·II swells on the held C5 and tenuto F5 of the S statement at 56–57, as at 47–48 (Casanelles PDF 152, 155) (tTwo); Fl 1 and Vln I fade to p on beat 2 of 13 where Hn 1's call enters mp (PDF 148, 290; Rimsky-Korsakov PDF 133) (intro).
- Open / not applied: None. Kept: Vln I pp last motto at 177; tutti quavers unmarked; tempo plan.
- Do-not-touch: phrasing 47–58 (c88); coda levels.
- Cross-movement: none.

## Cycle 259 (Holistic comparison with one specific master first movement, the one named in your task (see MASTERS.md). Would a conductor believe a master wrote this? Also compare with the version 10 cycles earlier and flag anything that got worse.; Rimsky-Korsakov examples No. 201-260 (rimsky-principles PDF 376-440)) → v260
- Accepted: Hn 4 breathes on beat 4 of 25 (g,4 f,2-> r4) to avoid a low minor third over the D2 bass (Rimsky-Korsakov PDF 85, 124); answers c106/c156 (tOne).
- Open / not applied: None. Kept: v249→v259 changes; bar-160 passing G (c241/c244); scale, recap join, soft ending.
- Do-not-touch: low horns 23–26 accents; 27–32.
- Cross-movement: none.

## Cycle 260 (Cyclic design and emotional arc across four movements; Adler ch. 1 The Orchestra, Yesterday and Today, and ch. 15 additional thoughts (adler1 PDF 19-23, adler2 PDF 187-196)) → v261
- Accepted: No score change (cyclic check). Records corrected: 158 full-brass ff cadential 6/4 of C (not root position) in mvt1.md; 108 seed wording (D♯4 rises to F4, no E♭ at 109–110); Vln II top C6 at 152; themes-mvt1.md Ob 2 at 158–161; harp D♭7 at 57–59.
- Open / not applied: None. Kept: no finale F1/F2 hints in mvt I (Tchaikovsky 4/5, Brahms 1 precedent).
- Do-not-touch: attacca join (Tbn 1 → Hn 3 → mvt II Hn 4 C4); three A♭ climaxes 82/122/160.
- Cross-movement: finale told: wording of 'first full-brass C-major triad' and harp D♭7.

## Cycle 261 (Melody and memorability; Adler ch. 7 Individual Woodwinds: melodic writing, registers (adler1 PDF 184-232)) → v262
- Accepted: Bsn 1's answer to the P head at 144 made audible: Vln II, Vla, Vc, Cb start mp at 144 and fade to pp at 145 (Adler PDF 226: accompaniment of the bassoon softer); no note changes (recOne).
- Open / not applied: None. Kept: B.cl P head 107–109 (c151); cor anglais 147–153/171–174; flute motto 73–76; themes.
- Do-not-touch: motto woodwind colours.
- Cross-movement: none.

## Cycle 262 (Harmony and voice leading; Aldwell & Schachter Units 22-23 Leading-tone seventh chords; Mixture (aldwell-schachter PDF 373-397)) → v263
- Accepted: Coda 177 viola A♭3 (seventh of vii°6/5 over D) now resolves to G3 on beat 4 (aes2. g4), so 176–178 is i6 – V4/3 – i (A&S PDF 375–378; answers c192's PDF 466 reason, which concerns root-position V9).
- Open / not applied: None. Kept: 26→27 d5–P5 in horns (finale quotes 27); 23–24/135–136 rising seventh in a doubled inner voice (hemiola); cross relations 79→80, 108→109 (seeds).
- Do-not-touch: bar 70 vii°7/V; 73 common-tone °7; 168–170; A♭/A♮ mixture 156–166.
- Cross-movement: none (coda viola 177 is not quoted).

## Cycle 263 (Form, pacing and proportion; Aldwell & Schachter Units 16 and 19 5/3- and 6/4-chord techniques: prolongation (aldwell-schachter PDF 249-262, 304-325)) → v264
- Accepted: No change (prolongation review: all 22 six-four chords have a named function).
- Open / not applied: None. Kept: 127–131 V without leading tone over the 14-bar G pedal (A&S PDF 322–323; answers c233); 158–166 expanded cadential 6/4; coda i6/4 at 175.
- Do-not-touch: horn call as melodised cadential 6/4; development key plan C–A♭–F.
- Cross-movement: none.

## Cycle 264 (Orchestration; Adler ch. 15 Scoring for Orchestra: homophonic and polyphonic texture (adler2 PDF 159-186)) → v265
- Accepted: Fugato 94–95: C.a. stays in unison with Vln II through the countersubject (rests at 96), Cl 1 rests 94–95 and enters at the ff of 96 (Adler PDF 176–178: keep established colours) (dev). Recap 131: violas and Hn 3·4 f (were ff) under the low P theme (Adler PDF 159, 184) (recOne).
- Open / not applied: None. Kept: trombones f at 131 (c144); pad 111–114; violas alone at 82; low trumpets 122; Tpt 1 A♭5 at 72; A♭6 at 31/72.
- Do-not-touch: A♭ climaxes 82/122/160; final chord 182.
- Cross-movement: none.

## Cycle 265 (Engraving and notation (Gould's *Behind Bars*, MOLA); MOLA Guidelines for Music Preparation, whole document (mola PDF 1-16)) → v266
- Accepted: Engraving (MOLA): nine cues in parts (harp 47, Vln I 55, Hn 2 56/156, Bsn 2 60, timp 62, Fl 1 64, Fl 2 68, Ob 2/Cl 2 103); bar ranges over multi-bar rests; score pages numbered so music runs 2–18 (odd on the right; answers c155); short staff names keep the key; parts top margin 20 mm (score.ly, parts-gen.py, parts-lib.ily).
- Open / not applied: None. Kept: string parts at 7.2 mm (7.5 mm puts the viola part on an odd last page, breaking the attacca).
- Do-not-touch: page breaks and part page counts.
- Cross-movement: mvt II told: score page numbering (odd on the right).

## Cycle 266 (Playability, instrument by instrument; Adler ch. 9-10 Brass: horn, trumpet, trombone, tuba, endurance and ranges (adler1 PDF 282-329, adler2 PDF 1-13)) → v267
- Accepted: Brass breaths (Adler PDF 292, 303, 309; adler2 PDF 8): tuba breathes on the last eighth of 121 and strikes 122 fresh; Hn 3 breathes on beat 4 of 123 with Hn 4 (dev).
- Open / not applied: None. Kept: Hn 1 soft high entry at 43; Hn 2 56–72; Hn 4 to written G5 at 158–160; Hn 1 B5 at 106 (ossia); Tpt 3 B3 fff at 122.
- Do-not-touch: coda chorale breaths 175–181.
- Cross-movement: none.

## Cycle 267 (Texture and counterpoint; Rimsky-Korsakov ch. III overlaying, crossing and enclosure (rimsky-principles PDF 106-114) and the examples cited) → v268
- Accepted: Bar 37 Bsn 1 B♭3 (was G♭3, unison with Hn 4): the soft bassoon–horn chord gets its fifth and four real parts, crossed as Rimsky-Korsakov PDF 108; Bsn 1 steps B♭–A♭ into 38 (trans).
- Open / not applied: None. Kept: violas/Vln II among pp trombones 175–178 (continuous inner lines; answers c234); Cl 2 inside horns 117–120; brass head over winds 167–169; horn pair on D4 at 40; short chord 43.
- Do-not-touch: coda inner lines 175–178; 167–169.
- Cross-movement: none.

## Cycle 268 (Expression; Aldwell & Schachter Unit 3 Rhythm and Meter: accent, hypermeter (aldwell-schachter PDF 47-57)) → v269
- Accepted: Tenutos on the syncopated long notes of the S climax, E6 at 158 and A♭6 at 160, in every part with the tune (as at 48, 51, 57, 70, 99, 102, 104, 148, 151, 172), and on the violins' C6/C5 at 62 (A&S PDF 50, 51, 53) (recTwo, tTwo).
- Open / not applied: None. Kept: accents at 142 (c118); Vln I D♭ at 180; ties 131–134; tempo plan; hemiolas.
- Do-not-touch: fff downbeat at 160; sub. p at 62.
- Cross-movement: finale told: S-climax tenutos at 158/160.

## Cycle 269 (Holistic comparison with one specific master first movement, the one named in your task (see MASTERS.md). Would a conductor believe a master wrote this? Also compare with the version 10 cycles earlier and flag anything that got worse.; Rimsky-Korsakov examples No. 261-312 (rimsky-principles PDF 441-504)) → v270
- Accepted: Cellos 171–174 become one solo cello ('Solo espr.'), Tutti at 175 on the chorale's motto bass with sul G (Rimsky-Korsakov PDF 122–123, 138–139, 142, Ex. 284; Elgar 1/i coda SOLO/TUTTI) (coda). No regressions v259→v269.
- Open / not applied: None. Kept: harp gliss 158–161; no mutes 177–182 (c076); viola soli.
- Do-not-touch: Tutti re-entry at 175 with sul G.
- Cross-movement: themes-mvt1.md: S coda minor statement now Vc solo.

## Cycle 270 (Cyclic design and emotional arc across four movements; Rimsky-Korsakov author's prefaces and ch. IV transfer of phrases (rimsky-principles PDF 13-23, 125-128)) → v271
- Accepted: No score change (cyclic check: every change since v261 keeps its links). Records updated: mvt1.md v262–v270 line, seeds (solo cello 171–174 beside C.a. matches the finale's single-voice minor S; bar 37 first E♭-minor sound), 'high four-horn unison' wording.
- Open / not applied: None.
- Do-not-touch: solo cello's unresolved B4 at 174 (passes to Cl 1 C5 at 176).
- Cross-movement: finale told (information): solo cello at 171–174.

## Cycle 271 (Melody and memorability; Sebesky ch. 6 Melodic Considerations and ch. 7 The Importance of the Lyric (sebesky PDF 204-230)) → v272
- Accepted: No change (Sebesky ch. 6–7: themes, fills and countermelodies follow the reading; closes c161's bar-150 note).
- Open / not applied: None. Kept: themes; 70–71 brief octave contact (Ex. 280); coda 171 without upbeat (fermata rest, C.a. G4–E♭5); A♭6 at 31/72/122/160 (c194, c264); pads 47–49/147–150.
- Do-not-touch: S head prepared by 13–14 and 41–44.
- Cross-movement: none.

## Cycle 272 (Harmony and voice leading; Aldwell & Schachter Units 24-25 Remaining uses of seventh chords; Applied V and VII (aldwell-schachter PDF 398-441)) → v273
- Accepted: 116: A♭ held through the bar in Ob 2, Cl 1, Hn 1, Tbn 2, Vln II (was A♭–A♮–G, the 'poor' order, A&S PDF 402) (dev). 51: viola A♭3 (was C4) gives V6/5 of IV its root and stops tripling the applied leading tone (A&S PDF 419, 439) (tTwo).
- Open / not applied: None. Kept: doubled D at 40 (c234, c252); Vln I leap off D♭6 at 63 (c221).
- Do-not-touch: 27–32 bass; 33–47 modulation chain; coda chorale.
- Cross-movement: none.

## Cycle 273 (Form, pacing and proportion; Aldwell & Schachter Unit 18 6/3-chord techniques (aldwell-schachter PDF 289-303)) → v274
- Accepted: 60: bass holds G♭ for the whole bar (E♭ minor 6/3 on beats 3–4, passing v6), so 59–62 is G♭–F♭–E♭ and the dominant is first struck at the cadential 6/4 of 62 (A&S PDF 290–291, 297–298, Ex. 18-12); Cb, Bsn 2, Vc, harp (tTwo).
- Open / not applied: None. Kept: wedge 111–116; 33–47 route; 6-for-5 over V at 106/127/130/144; Neapolitans 20–21/140–141/172–173; proportions.
- Do-not-touch: violins 56–63; counterline; sub. p at 62.
- Cross-movement: none.

## Cycle 274 (Orchestration; Adler ch. 8 Woodwinds in the symphony orchestra and woodwind-string combinations (adler1 PDF 233-281)) → v275
- Accepted: 45–46: the link into S moves from Ob 1 (p, rit., down to its honking low F4/E♭4) to Cl 1, same notes (Adler PDF 237, 238, 270–271; answers c198); oboes rest 44–68 (trans). Composer: harp part cue at 45–46 now quotes Cl. 1 (parts-gen.py).
- Open / not applied: None. Kept: A♭ climaxes; Ob/Cl unison on P head 103–106; Ob/Cl/Hn 111–114; Fl 1/Ob 1/Vln I 23–25, 135–137; 139–142.
- Do-not-touch: notes of 45–46 (c161).
- Cross-movement: none.

## Cycle 275 (Engraving and notation (Gould's *Behind Bars*, MOLA); Adler ch. 18 Preparation of Score and Parts, and App. A (adler2 PDF 291-312)) → v276
- Accepted: Parts only: Ob 1 gets a Cl. 1 cue at 67–68 before its f entry at 69 (Adler PDF 299); parts drop the score's spacing sections so rests are not split at 73 (Adler Ex. XVIII-5/6); viola part spacing 1.42 keeps it at 2 pages (parts-gen.py, parts-lib.ily).
- Open / not applied: None. Kept: tempo marks above top staff and Vln I only (MOLA; c165); three small near-touches in parts.
- Do-not-touch: score engraving.
- Cross-movement: none.

## Cycle 276 (Playability, instrument by instrument; Adler ch. 12 Percussion: timpani tuning and technique (adler2 PDF 55-91)) → v277
- Accepted: Percussion: the fff suspended-cymbal stroke at 160 is tied to 163 and damped at 164 with the harp (was open l.v.); the coda tam-tam (175) is damped at the release of 182 (Adler PDF 70–73, 80; answers c166) (recTwo, coda).
- Open / not applied: Viola part once built at 3 pages in one of four runs (spacing 1.42 is near the edge); watch it. Kept: two near-touches in the percussion part.
- Do-not-touch: timpani part (ranges, retunings, 85 attacks checked).
- Cross-movement: mvt II told: its coherence note 'G drum to D♭' at its bar 5 needs another drum.

## Cycle 277 (Texture and counterpoint; Sebesky ch. 1 Basics: balance, economy, focus, variety (sebesky PDF 11-20)) → v278
- Accepted: Violas rest 56–59 (their pp off-beat dyads only doubled the Cl 1/Hn 2 counterline, the Hn 3·4 pad and the cello arpeggio) and enter p< at 60 with Bsn 2 (Sebesky PDF 12–13 Ex. 1; Adler part 2 PDF 229) (tTwo). Viola part: forced page turn after 106 so it is reliably 2 pages (parts-gen.py).
- Open / not applied: None. Kept: violas double the counterline 64–67 (c67); 147–150 harmonised as 47–50; 162–165 middle register (c236, c252).
- Do-not-touch: violas 60–67.
- Cross-movement: none.

## Cycle 278 (Expression; Sebesky ch. 1 focus and variety, ch. 6 melodic considerations (sebesky PDF 11-20, 204-218)) → v279
- Accepted: Dynamics: Vc/Cb mf under the f P tune from 15 (was f, then mf at 19) (tOne); Vln I 'pp espr.' on the last motto at 177 (coda); B.cl mf at 103 (was f) (dev); Ob 2 accents C5–B4 at 142 like its doublings (recOne) (Sebesky PDF 12–14, 18, 214–215).
- Open / not applied: None. Kept: equal p of tune and counterline 56–59 (Sebesky Ex. 269); horn a level below strings 46–52/146–154; two ff lines 117–121; swells 97–102 (c248).
- Do-not-touch: coda dynamics.
- Cross-movement: none.

## Cycle 279 (Holistic comparison with one specific master first movement, the one named in your task (see MASTERS.md). Would a conductor believe a master wrote this? Also compare with the version 10 cycles earlier and flag anything that got worse.; Adler part 1 full-score examples in ch. 5 and 8 (adler1 PDF 137-165, 235-281)) → v280
- Accepted: No change (holistic vs Mendelssohn 3/i and v269: no regressions).
- Open / not applied: None. Kept: A♭6 at 31 (finale quotes 27–32); 167–170 layout as 27–32; Ob/Cl unison 103–106; two flutes 69–72; Cb pizz f at 103; Hn 1 a level below strings 146–154.
- Do-not-touch: coda 171–182 return of the opening colour; fugato 85–96 strings alone first.
- Cross-movement: none.
- Note (c280): c067's protection 'viola E♭–E♮–F 56–57' is closed: the line stays at pitch in Cl 1 + Hn 2; violas rest 56–59 (c277).

## Cycle 280 (Cyclic design and emotional arc across four movements; Sebesky ch. 9 General Advice and ch. 1 (sebesky PDF 240-242, 11-20)) → v281
- Accepted: No score change (cyclic check: changes since v271 keep every link; Do-not-reuse list holds in MIDI). Records: mvt1.md to v280 (percussion damping, 60–62 bass, two new seeds of mvt II at 45–47 and 60–62, peak ladder A♭6–B♭6–B6–C7, v272–v280 changes); themes-mvt1.md 'pp espr.' at 177.
- Open / not applied: None.
- Do-not-touch: peaks below the later movements.
- Cross-movement: mvt II told: tam-tam damped at 182 and the two seeds; finale told: cymbal tied to 163, 'pp espr.' at 177.

## Cycle 281 (Melody and memorability; Aldwell & Schachter Unit 21 Rhythmic Figuration: suspensions, anticipations, pedal (aldwell-schachter PDF 346-371)) → v282
- Accepted: 45: cellos G3–A♭3 (was A♭3 whole bar) so Cl 1's 7–6 suspension B♭–A♭ is not anticipated by its note of resolution (A&S PDF 350–354, Ex. 21-12c) (trans).
- Open / not applied: None. Kept: climax E6 rising at 159 (c101; finale quotes); cello G3 at 59 (c107; octave exception); themes; Cl 1 7–6 at 175–177.
- Do-not-touch: 43–47 lead-in and 33–46 route (c163, c236).
- Cross-movement: none.

## Cycle 282 (Harmony and voice leading; Aldwell & Schachter Units 28-29 Neapolitan; Augmented Sixth Chords (aldwell-schachter PDF 482-529)) → v283
- Accepted: 143: Vc and Bsn 1 hold C3 (was C3–D3), so Vln I's passing D♭5 sits over the held tonic as at 27 and 167, with no diminished octave in the outer voices (A&S PDF 484, 488, 495) (recOne).
- Open / not applied: None. Kept: aug6 at 116 with C bass (motivic bass, PDF 516); 12–13 octaves with the bass (c112); no new aug6 at 178 (B→C reserved), 68, 162, 82→83.
- Do-not-touch: 143–150 lead-in events (c239).
- Cross-movement: none.

## Cycle 283 (Form, pacing and proportion; Adler ch. 15 Additional thoughts and special effects (adler2 PDF 187-196) with ch. 17 The Orchestra as Accompanist (adler2 PDF 256-290) for pacing of background and foreground) → v284
- Accepted: No change (form and pacing vs Adler ch. 15, 17). Closed open items: development opening 77–84 stop-start (c079; Adler PDF 195, 276); light texture 103–110 after the ff S (PDF 262, 267); recapitulated second group 'too complete' (one statement 147–155).
- Open / not applied: None. Kept: dense 139–141 below the 158 arrival; reversed recap order; two-bar approach 156–157 (c083, c143, c243); viola/solo cello C4 at 172.
- Do-not-touch: climax arrival 158 (14 players return).
- Cross-movement: none.

## Cycle 284 (Orchestration; Adler ch. 11 Scoring for Brass: homophonic unit and climactic uses (adler2 PDF 14-18, 37-54)) → v285
- Accepted: Brass (Adler PDF 15, Ex. XI-1): Hn 3 holds the leading tone B3 at 122–124 (was D4), resolving to C4 at 125 (dev); Hn 4 F♯3 a2 with Hn 3 on the Ger6 at 12 (was A♭2 doubling the bass) (intro); Tpt 2 E♭4 on the ff stroke at 33 (was G4), as at 143 (trans).
- Open / not applied: None. Kept: low trumpets at 122 (c244); Tpt 1·2 G4 at 131–132; single horns at ff at 26, 27–32, 82, 138; climax order.
- Do-not-touch: three-climax order.
- Cross-movement: finale told: Ger6 at 12 horn layout (Hn 4 F♯3 instead of A♭2), pitches unchanged.

## Cycle 285 (Engraving and notation (Gould's *Behind Bars*, MOLA); Gould introduction and contents (gould-behind-bars PDF 7-13), then a second pass over PDF 17-68 for any rule not yet checked) → v286
- Accepted: Cello tenor clef at 97 moved before the pickup F♯3 so the B-minor S phrase reads in one clef, as at 46 and 146 (Gould PDF 22) (dev).
- Open / not applied: None. Kept: Vln I 8va at 31, 71–72, 121–123 (c245); 73–76 spacing (c145); breath marks on Hn 3·4; dotted minim rests at 170.
- Do-not-touch: fixed 17-page layout.
- Cross-movement: none.

## Cycle 286 (Playability, instrument by instrument; Adler App. A ranges, professional and amateur limits (adler2 PDF 302-312)) → v287
- Accepted: No change (ranges vs Adler App. A: every part inside professional range).
- Open / not applied: None. Kept: B.cl low C 92–93/105–106 (c146, c256); Ob 1 B3 at 117; Hn 1 B5 at 106 (ossia); A♭6 at f–fff; Cl 1 D6 at 158/160; Vc F5 at 52; timpani retunes.
- Do-not-touch: parts page turns.
- Cross-movement: none.

## Cycle 287 (Texture and counterpoint; Sebesky ch. 3 Voicing the strings; combining strings with winds (sebesky PDF 133-173)) → v288
- Accepted: No change (string voicing vs Sebesky ch. 3).
- Open / not applied: None. Kept: violas inside the brass register 117–121/131–134 (c264); low strings under fff brass at 122; P on Vln I alone 15–18 (graded build to 27); Fl 1 mp at 109–110 (settled); cellos double basses only on pedals, strokes and the motto.
- Do-not-touch: graded build 15–27.
- Cross-movement: none.

## Cycle 288 (Expression; MOLA guidelines on dynamics, articulation and bowing marks in parts (mola PDF 1-16)) → v289
- Accepted: Accents on C–B at 142 in Hn 3, Tpt 3, Tbn 1 like every other doubling (MOLA Ex. 6) (recOne); Bsn 2/Cbsn diminuendo starts on the note at 125, not on the beat-4 rest (MOLA PDF 8) (dev).
- Open / not applied: None. Closed: 'damp' vs 'étouffez' (c168). Kept: Ob 2 hairpin into rest 116→117; Vln I 179–182 text spacing; Hn 3·4/Tbn f at 139–142 (c264, c283).
- Do-not-touch: coda part layout.
- Cross-movement: none.

## Cycle 289 (Holistic comparison with one specific master first movement, the one named in your task (see MASTERS.md). Would a conductor believe a master wrote this? Also compare with the version 10 cycles earlier and flag anything that got worse.; Adler part 2 full-score examples in ch. 11 and 15 (adler2 PDF 18-54, 143-186)) → v290
- Accepted: Fl 1 joins the violins' octave on the downbeat of 100 instead of falling a sixth on beat 3 mid-climb (Adler PDF 147–151); narrows c144 ('Fl 1 alone at the top 97–100') to 97–99 (dev). Holistic vs Borodin 2/i and v279: no regressions.
- Open / not applied: None. Kept: no ff unison tutti of the motto (finale's reserve); horn unison 158–161 (c181).
- Do-not-touch: motto colours; 117–121 brass motto; 122–131 collapse.
- Cross-movement: themes-mvt1.md: B-minor S Fl 1 8va now 97–99 only.

## Cycle 290 (Cyclic design and emotional arc across four movements; Aldwell & Schachter Unit 23 Mixture as a long-range device (aldwell-schachter PDF 386-397)) → v291
- Accepted: No score change (cyclic check: changes since v281 keep every link). Records: mvt1.md to v290 (v282–v290 line; bar-12 seed with Hn 3·4 F♯3 = finale Hn 4 F♯3; E♭4/E4 thread adds Vln II 77–80).
- Open / not applied: None.
- Do-not-touch: Hn 3 B3→C4 at 122–125 resolves into i6/4 (not the finale's B→C).
- Cross-movement: none (finale already told at c284).

## Cycle 291 (Melody and memorability; Adler ch. 11 Scoring for Brass: melodic presentation (adler2 PDF 19-36)) → v292
- Accepted: No change (brass melodic presentation vs Adler ch. 11).
- Open / not applied: None. Kept: motto in Hn/Tbn unison 117–121; Hn 3·4 high unison 158–161 (c174, c181, c266); P in the tenor at 131 (c144); coda chorale canon 175–181; Tpt doubling Ob 69–72, 82, 158–161.
- Do-not-touch: themes.
- Cross-movement: none.

## Cycle 292 (Harmony and voice leading; Aldwell & Schachter Units 30-31 Other chromatic chords; Chromatic voice-leading techniques (aldwell-schachter PDF 530-583)) → v293
- Accepted: 119–120: the Vla and Cl 2 triplets' middle note follows the motto (E♭–D–D♭–C) instead of sounding D4 against its E♭4 and D♭4 against its C4 (♭6 replaces the 5th of V, A&S PDF 537, 301); answers c133 (alternating chords kept) (dev).
- Open / not applied: None. Kept: B°7 over D → iv at 138→139 (A&S PDF 545; finale quotes); 77–83 major-third cycle (PDF 573); passing D at 119.1.5.
- Do-not-touch: development key plan B–D–F–A♭ (vii°7 of C composed out).
- Cross-movement: none.

## Cycle 293 (Form, pacing and proportion; Aldwell & Schachter Units 6-8 I, V, V7 and their inversions: phrase structure (aldwell-schachter PDF 92-133)) → v294
- Accepted: No change (phrase structure and cadences vs A&S Units 6–8).
- Open / not applied: None. Kept: contrapuntal cadences at 175–182 (attacca; structural cadences at 143, 166); intro ends on V7 at 14; F-minor deflections 64, 68.
- Do-not-touch: large-scale I–VI–iv–V–I plan; cadence order 55/72, 155/166.
- Cross-movement: none.

## Cycle 294 (Orchestration; Adler ch. 5 Scoring for Strings (adler1 PDF 125-167)) → v295
- Accepted: Background strings clear the Vln I pickup into P (Adler PDF 135), as c227 did at 15/17: Vln II enters on 2-and at 19 (tOne); Vln II tremolo starts on beat 2 at 37 (trans); Vln II and Vla drop their first off-beat eighth at 143 (recOne). Rhythm only.
- Open / not applied: None. Kept: violas' A♭4 at 19; Vln I A♭6 at 72; P on Vln I alone 15–18; viola arpeggio 97–102; Vln II pad 147–154; viola chords 158–161; climax string scoring.
- Do-not-touch: three A♭ climaxes.
- Cross-movement: none.

## Cycle 295 (Engraving and notation (Gould's *Behind Bars*, MOLA); MOLA second pass, applied to the instrumental parts (parts.ily) rather than the score) → v296
- Accepted: Parts (MOLA PDF 5, 8, 10, 12): cues for Vln I/Fl 1 at 94, Ob 1 and timp at 115, Hn 3·4 at 181, harp at 182; Cbsn cue at 67–68 from the cello 8vb (new cueVcLow); multi-bar rest numbers counted in spacing; parts drop the score's partCombine commands (Fl 1 rest 42–44 no longer split). Score: viola triplet number up at 117 (dev, parts-gen.py, parts-lib.ily).
- Open / not applied: None. Kept: no composer name (c200); 7.2 mm strings; bowings (c238); percussion near-touches (c276, c285).
- Do-not-touch: attacca page plan.
- Cross-movement: mvt II may reuse the parts-library changes.

## Cycle 296 (Playability, instrument by instrument; Rimsky-Korsakov ch. I General review of orchestral groups (rimsky-principles PDF 24-50)) → v297
- Accepted: Timpani 'muta B♮ in A♭' printed at 98, right after the B stroke at 97 (was 111), as at 34, 44, 84 (Rimsky-Korsakov PDF 48) (dev). Composer rejected the critic's cellos 8vb at 101–102: professional cellos play B4/D5 at ff (Adler App. A, c286), and c231's at-pitch doubling of the B-minor S stays.
- Open / not applied: None. Kept: cellos 101–102 at pitch (above); cello high notes 51–54 (c186); solo cello C5 at 174.
- Do-not-touch: c231 cello doubling 97–102.
- Cross-movement: none (mvt1.md timpani table updated).

## Cycle 297 (Texture and counterpoint; Adler ch. 8 Variety of orchestral treatments (adler1 PDF 251-281)) → v298
- Accepted: Hn 1·2 rest 23 to beat 2 of 24 and enter mp< on beat 3 of 24 (as at 136–137), so the hemiola's third cell changes colour instead of doubling the clarinets at pitch throughout (Adler PDF 253, 255, 257) (tOne).
- Open / not applied: None. Kept: rising P calls 117–120; Cl 1 + Hn 2 counterline 56–59; fugato 85–96.
- Do-not-touch: Hn 3·4 at 23–26.
- Cross-movement: none.

## Cycle 298 (Expression; Adler ch. 7 woodwind articulation and dynamics by register (adler1 PDF 184-232)) → v299
- Accepted: Cl 1 'dolce' and a diminuendo onto E♭4 at 45–46 (link into S) (trans); Cl 1 'espr.' under its pp at 175, matching Vln I's 'pp espr.' at 177 (coda) (Adler PDF 187, 205–206, 210–212).
- Open / not applied: None. Kept: winds f inside 'mp cresc.' at 115–116; C.a. p against solo Vc mp at 171–174.
- Do-not-touch: no register/dynamic breaches found in woodwinds.
- Cross-movement: none.

## Cycle 299 (Holistic comparison with one specific master first movement, the one named in your task (see MASTERS.md). Would a conductor believe a master wrote this? Also compare with the version 10 cycles earlier and flag anything that got worse.; Adler part 2 transcription examples in ch. 16 (adler2 PDF 202-244)) → v300
- Accepted: No change (holistic vs Franck D minor/i and v289: no regressions). Closed c406 (Cl 1 already rests on beat 3 of 162).
- Open / not applied: None. Kept: proportions (c215, c243, c283); 167–170 layout as 27–32; cellos at pitch 97–102 (c296); Ob/Cl unison 103–106.
- Do-not-touch: coda colours and final-chord spacing.
- Cross-movement: none.

## Cycle 300 (Cyclic design and emotional arc across four movements; Aldwell & Schachter Unit 28 the Neapolitan as a long-range device (aldwell-schachter PDF 482-502)) → v301
- Accepted: No score change (cyclic check vs A&S Unit 28: ♭II is always a chord, each structural N6 goes to V at 20–22, 140–143, 172–174). Records: mvt1.md to v301 (v292–v301 line; three Do-not-reuse items: D♭ as key, ♭VI→♭II, theme on ♭II; bar-75 seed V7/D♭ → D♭ 6/4).
- Open / not applied: None. Kept: coda N6 at 173 (one beat, protected); chromatic spellings (A&S PDF 496–499).
- Do-not-touch: Spellings at 12 (Ger6) and 75 (G♭ in A♭7).
- Cross-movement: Finale told to correct finale.md's ♭II thread (add I 20–22, 115, 140–143, 178, 180; finale completes I 173–175's N6–6/4–V).
