# Movement III critic history

Cycle N reviews vNN and produces v(N+1). Each entry: Accepted, Rejected (with reason), Open, Do-not-touch.

## v01 (composer's first draft, 2026-10-12)
- 262 bars, 2/2, about 6:40 (402 s MIDI); plan in movement-3-plan.md. Sections: intro 1–10, pOne 11–26, pTwo 27–42, trans 43–50, sOne 51–66, sTwo 67–82, clos 83–98, dev 99–134, retr 135–150, recP 151–170, recS 171–198, codaOne 199–210, codaTwo 211–218, arrival 219–230, sHead 231–242, finale 243–262.
- Build: 0 warnings, 0 outer-voice parallels, 16 A3 pages (the page cap). Range flag: trumpet C6 at 239 and in the finale, accepted for C trumpet.
- Do-not-touch (cyclic rules from cyclic-notes.md "Start here for movement III"; change only by answering the reason there):
  - Bars 1–2: movement II's A♭ chord as a German sixth A♭–C–E♭–F♯ resolving to V, ff. Reason: mvt II critics 120 and 130, A&S p. 593.
  - No root-position V–I or V–i cadence in C before 254–255. Reason: the last cadence is the symphony's first since movement I bar 135.
  - Trumpets tacet 1–50; soft undoubled trumpet solo at 51. Reason: owed item 1.
  - String tremolo and the violins' C7 only from 219. Reason: owed item 2.
  - Stop chord B–D–F–A♭ (138, 218) resolves only at 218→219, trumpets B→C with the timpani.
  - Violas D♯→E at 215–216 (E♭/E♮ thread). Chorale top line `g1 | e'1 | d'1 | c'2 des'2 | c'1` (219–223) and its last statement ending `c'2 b2 | c'1` (251–255).
  - No tam-tam; Hn 3·4 "senza sord." at their first entry; timpani label "retune D♭ → G during the pause".

## Cycle 1 (v01 → v02), lens 1 melody, A&S Unit 20
- Accepted: F1 head in C major ff in horns and trombones 256–259; consequent peak A♭6–G–F at 22 and 162; appoggiatura at F2's first peak (53, 69, 173, 189); new F1 bar rhythm at 17 and 157; clarinet eighths held in 12, 16, 20, 24.
- Rejected: turn in F2 at 64, 80, 184 (the solo stays plain; it already has the appoggiaturas).
- Do-not-touch (critic): both chorale statements; the D–D♭–C passing tone in movement I's head; F1's head bar.

## Cycle 2 (v02 → v03), lens 2 harmony, A&S Unit 5
- Accepted: 218 bass D (stop chord over G; no V–I in C before 254–255); 254 cadence voice leading; iv6 at 57/177; 247 bass; chorale bass A at 222–223; brass revoicing 36–37, 111–112, 165–166, 243–249; 211–212; Tbn 1 and cellos at 1–2, 5–6.
- Kept: fifths at 244, 246 (quoted themes) and in upper voices of the German sixth (A&S PDF 526).
- Tool: tools/critic-scripts/c002/par.py checks every pair of staves for parallels (analysis.txt only checks top vs bass).

## Cycle 3 (v03 → v04), lens 3 form, A&S Unit 14
- Accepted: ending 256–262 aligned (all parts 20 bars, final chord 261–262, V–I echo at 260); 237–238 V6/5 of V into the 239 cadential 6/4; G7 at 133–134; crescendo 129–131; leading-tone doubling at 131–132 removed.
- Do-not-touch (critic): 218→219 arrival; both chorale statements; exposition key plan with the B♭ pedal into 51.
- Note for critics: the build does not warn when the last section's parts are short; check last onsets in the MIDI.

## Cycle 4 (v04 → v05), lens 4 orchestration, Rimsky-Korsakov ch. I, III
- Accepted: chorale f / canon ff balance 220–227; Hn 1 and Hn 3 voicing at 220, 222; second winds doubling at 243–250, 256–260; Fl 2 and Ob 1 registers 151–166; strings below the harp 123–130; Hn 1·2 mf at 11–26; bass drum at 219 and 261.
- Do-not-touch (critic): arrival chord scoring at 219; muted trumpet with cor anglais 171–186; accompaniment of the trumpet solo 51–66.
- Open (relay from movement II, 2026-10-12 14:18): add a starting harp pedal diagram at the harp's first entry, as movement II did at its bar 1 (cycle 116). Assigned to cycle 6 (playability). Timpani first tuning G, A♭, C, E♭ matches movement II's "muta D♭ in G" note.

## Cycle 5 (v05 → v06), lens 5 engraving, Gould ch. 1
- Accepted: circled cymbal semibreves and drum-staff positions; bassoons apart 11–26; horn bass clef 25–26, 165–166; viola treble clef 241–242; single fermata at 262; page break at 219 with `page-count = 16`; one "senza sord.".
- Kept: ledger lines (no 8va) for Fl 1/Vln I B6–C7 at 218, 219, 242.
- Note for critics: `page-count = 16` is now fixed in score.ly, so a page count of 16 no longer proves nothing was added. Check that systems are not crowded (look at the page images) after adding material.

## Cycle 6 (v06 → v07), lens 6 playability, Adler ch. 2
- Accepted: viola pizz. div. 171–186; div. a3 final chord; harp pedal diagrams (67, 123, 187, 231) and changes (197, 198, 238), which closes the open item; arco marks and pizz.→arco time; bow-length slurs in the violins at 67–82, 187–198, 230–238; Tpt 1 senza sord. at 199; down-bows at 2 and 6; viola divisi; wind breaths 178–194.
- Timpani tuning checked: G, A♭, C, E♭ throughout.

## Cycle 7 (v07 → v08), lens 7 texture, Adler ch. 5
- Accepted: countersubject 35–38; recap clarinet eighths 151–166; violas with cellos 243–250 and 67–82/187–198; Vln II unison 231–234; viola repeated quarters 220–224; retransition overlaps 140, 142; spacing 1.6 to hold 16 pages.
- Kept: Ob at 162 a third below (critic 001).
- Open: combine the development's two ideas at 99–106 (cycle 17).
- Do-not-touch (critic): 27–34 bass statement with countersubject; 51–66 pizz. accompaniment; the 250→251 switch to the chorale.

## Cycle 8 (v08 → v09), lens 8 expression, Rimsky-Korsakov ch. IV
- Accepted: dynamic plan 205–219 (f, ff at 211, sub. p 215, fff 219); fff at 255 and 261, timpani rolls 254; sf-p at 101, 105, 138; pp re-entry of trombones at 143; staged diminuendo 39–42; p entries of doublings; tuba f at 159.
- Do-not-touch: the strong marks are limited to 101, 105, 138, 215, 219, 255, 261 (fff only at 219, 255, 261).

## Cycle 9 (v09 → v10), lens 9 holistic, Brahms 1/iv
- Accepted: 211 ff then f under the trumpets' recall; flutes above oboes 211–218; p accompaniment at 231–234; "ffff" and "2." at 199 fixed; Hn 1 alone at 139–140.
- Kept: Maestoso at 251 (the chorale needs the broad tempo; at Allegro molto it would last about six seconds).

## Cycle 10 (v10 → v11), lens 10 cyclic design, A&S Unit 32
- Accepted: German sixth at 254 (♭VI → Ger6 → V7 → I, the bar-1 chord); D♯ spelling at 215 in Ob 1 and Hn 3; no cymbal at 210 (first crash at 219); Ob 1 B5 on top of the stop chord at 138.
- Rejected: D♯ on top at 215 (mvt II c110); the top line D♭–C–B–C is protected.
- Do-not-touch (critic): join at 1–2; 205–218 path with D♭–C–B–C on top; 218→219 (Tpt B→C, timpani G→C); chorale top lines.

## Cycle 11 (v11 → v12), lens 1 melody, Rimsky-Korsakov ch. II
- Accepted: F2 climax by a rising fourth with appoggiaturas at 62, 78 (B♭6), 182; violas and cellos on F1 at 256–259; Fl 1 octave at 181–183; Cl 1 held notes at 65–66, 185–186.
- Do-not-touch (critic): chorale top lines; 218→219; F1 head bar and consequent peak 22/162; the trumpet solo's p entry at 51.
- Open (relay from movement II critic 160, 2026-10-12 16:36): the trumpets' recall of theme B at 211–214 runs about 2.4× faster than in movement II (6.7 s against 16 s). Decided: augment it (double the note values, 211–214 becomes 8 bars) so it is recognisable; assigned to cycle 13 (form), which must keep the 205–219 dynamic plan, the D♭–C–B–C top line and 218→219. MIDI instrument equalizer stays on, as in movement II.

## Cycle 12 (v12 → v13), lens 2 harmony, A&S Units 9–10
- Accepted: earlier root V–I in C removed (14, 22, 154, 162 V4/3; 192 V6/5); 252 inner voices; 239–240 6/4 resolution; 246 voicing; 216→217; 150→151 bass; 185→186 bassoon.
- Do-not-touch (critic): German-sixth approaches at 1–2, 215–216, 254; 239–243 6/4 → V4/3 → I; plagal close 227–230; chorale top lines.

## Cycle 13 (v13 → v14), lens 3 form, A&S Unit 26
- BAR NUMBERS from v14: old 211–214 → 211–218; old 215–250 → +4; old 251–255 → 255–264; old 256–262 → 265–271. Entries above use old numbers.
- Accepted: theme B recall augmented (211–218); last chorale at Allegro molto in doubled values 255–264, no Maestoso (reverses cycle 9, answered: 12 s not 6 s); viola F1 entry at 130–131.
- Protected items at new numbers: stop chord 222 → C at 223 (Tpt B→C, timpani G→C); violas D♯→E 219–220; sub. p 219; fff at 223, 263, 270; tremolo and C7 only from 223; chorale top lines 223–227 and 255–264; last cadence (♭VI–Ger6–V7–I) 261–263, the only root V–I in C.
- Open: combine the development's two ideas at 99–106 (cycle 17).

## Cycle 14 (v14 → v15), lens 4 orchestration, Rimsky-Korsakov ch. III
- Accepted: horn call layout 243–246 (Tpt 1 E5, Tpt 2 + Hn 1 E4, Hn 2 E3); Tbn 2 G3 at 255–256; Tpt 2 A4 at 227; violas f at 224.
- Do-not-touch (critic): arrival chord 223; German-sixth brass layout 1–2; trumpets' B→C at 262–263.

## Cycle 15 (v15 → v16), lens 5 engraving, Gould ch. 1 beams
- Accepted: sloped beams (manual Beam.positions; redo if the notes change); harp and Cb stem direction; pickup hairpin minimum length; hidden duplicate mf; clarinets apart 101–106.

## Cycle 16 (v16 → v17), lens 6 playability, Adler ch. 3
- Accepted: divisi marks; tenor clefs 27–38; Vln I rest at 144; viola run 245–246 down an octave; bow-change marks; viola pizz. div. 51, 115; sul A 235–238.

## Cycle 17 (v17 → v18), lens 7 texture, Adler ch. 15
- Accepted: x overlapping the F1 head at 103–105 with horn pedal (closes the open item); violas on the S head 247–254; held parts f at 247–254; viola quarters 255–262.
- Kept: canon 223–230 in whole notes.
- Do-not-touch (critic): the two ideas apart at 99–102; S-head texture 235–242; retransition stretto 139–146.

## Cycle 18 (v18 → v19), lens 8 expression, Adler ch. 2 bowing
- Accepted: bow-length string slurs (violas, inner counter-melodies); time for pizz. at 114/170; down-bow peaks 78/198; fast runs four notes per bow; bow-change marks; `\dnup` at 1 and 5; portato violas 224–228.
- Do-not-touch (critic): F1 bowing 11–26 and 151–166; tremolo and C7 at 223; sul A/ord. 235/239; pizz./arco timing at 51, 67, 123, 187.
- Open (relay from movement II critics c162/c170, 2026-10-12 19:01): movements I and II outline the major-third cycle C – A♭ – F♭/E. Decided: close it with one I – III♯ (E major) – V progression, approached by II6, in movement III's C-major pages (candidates: the arrival's plagal close 227–234 or the second-theme head 235–246). Assigned to cycle 20 (cyclic lens). Must not add a root V–I in C or touch the protected chorale top lines.

## Cycle 19 (v19 → v20), lens 9 holistic, Tchaikovsky 5/iv
- Accepted: woodwind doubling of the trumpets' theme B recall 211–218; marcato half notes in Hn 3/Tpt 3 under the last chorale; clarinets on the S head 247–254.
- Open: lengthen the C-major close after 263 (about 9 s now). Page cap raised to 17 for this change only. Assigned to cycle 23 (form).
- Do-not-touch (critic): arrival and chorale 223–234; cadence plan with the only root V–I at 262–263; trumpet solo at 51; muted trumpet with cor anglais 171–186.

## Cycle 20 (v20 → v21), lens 10 cyclic design, A&S Unit 26
- Accepted: I – II6/5 – III♯ (E major, 243) – cadential 6/4 – V4/3 – I at 241–247, closing the C – A♭ – E cycle (closes the open item from movement II's critics); header comments.

## Cycle 21 (v21 → v22), lens 1 melody, Rimsky-Korsakov ch. II
- Accepted: trumpets on F1 in C major 265–268; flutes an octave above the theme B recall 211–218.
- Do-not-touch (critic): chorale top lines; 222→223; F1 head bar and peak 22/162; plain trumpet solo 51–60.

## Cycle 22 (v22 → v23), lens 2 harmony, A&S Units 11–13
- Accepted: ii7 → III♯ with the 7th resolving at 241–243; bass C at 78; Phrygian cadences 57–58, 177–178; deceptive-cadence voicing 26, 63, 166, 183, 186; lament suspensions 107–109; inner note A at 228.
- Do-not-touch (critic): plagal close 230–234; final approach 255–263 (I6–vi–iiø6/5–Ger6–V7–I).

## Cycle 23 (v23 → v24), lens 3 form, A&S Unit 32
- BAR NUMBERS from v24: 8 bars after 268; old 269–271 → 277–279. fff at 223, 263, 278.
- Accepted: longer C-major close 269–276 (heads swapped, IV6/4–iv6/4–I over C pedal); `page-count = 16` removed, 16 pages without it; page break before 239. Closes the cycle 19 open item.
- Page cap stays 16 (no 17th page was needed).

## Cycle 24 (v24 → v25), lens 4 orchestration, Rimsky-Korsakov tutti chords
- Accepted: themes in separate registers 269–272; lower brass f at 265–268; complete cadence chord 263–264; trumpets uncrossed at 278; timpani C at 274.
- Do-not-touch (critic): arrival chord 223; chorale top lines; Tpt 1 B→C with timpani 262–263; 273–276 chord layout.

## Cycle 25 (v25 → v26), lens 5 engraving, Gould ch. 1
- Accepted: bassoon part-combining at 101, 107–109, 114, 269–272; harp 8 bassa; percussion dynamics at 263, 265, 278.
- Do-not-touch (critic): arrival at 223 (tremolo, C7, circled crash); chorale top lines; 222→223; page break at 223.

## PAUSED after cycle 25 (2026-10-12 ~21:00 UTC)
- Dan decided (2026-10-12 20:46 UTC) to make the symphony four movements: a scherzo in E (thread "Scherzo actor critic loops", symphony/scherzo/) goes between movement II and this finale, which becomes movement IV.
- Loop paused at v26. Listening renders from now on: r07 (symphony/render/r07, output score-r07.mp3). Resume when the coordinator says the scherzo's themes and ending are settled, with one rework pass (cycle 26 on v26): rebuild the opening link from the end of the scherzo instead of movement II's A♭ chord; bring in scherzo material where it serves the finale; renumber the movement as IV (titles, plan, brief, critic prompt). The E-major chord at 243 then also points back to the scherzo's key.
- Cycles after the rework continue the normal lens rotation up to cycle 200 (v201) unless the coordinator says otherwise.

## RESUMED 2026-10-12 22:30 UTC (Dan: restart the finale; four movements; threads coordinate)
- The finale is now movement IV. The scherzo (symphony/scherzo/, latest vNN; E minor, trio E major) comes before it and ends pp on G♯ (Hn 1 G♯4, Vln I G♯5) over a timpani roll and pizz. E, with a fermata. Scherzo timpani: E, G, B, E (G♯ in the trio and coda).
- Cycle 26 is the rework pass: renumber as IV; rebuild the opening link from the scherzo's ending (G♯ = A♭); new timpani retune label; bring in scherzo material where it serves the finale; the finale's trumpet solo at 51 is no longer "the trumpets' first entry since movement I" (the scherzo uses trumpets in tuttis).
- Coordination: current-state file symphony/coherence/finale.md (only this thread edits it; scherzo and movement II keep their own files in symphony/coherence/). Changes that affect another movement are messaged directly to that thread. Lens-10 cycles read all coherence files and check the links against the latest versions of I (v221, fixed), II and the scherzo.
- Theme lock: proposed 22:25 and withdrawn. Dan (2026-10-12 22:26): "no I don't want the scherzo themes to be locked". The scherzo's themes keep evolving and the finale follows them. The scherzo keeps symphony/coherence/themes-scherzo.ly as a live record and messages this thread with old and new notes when a theme or its ending changes. The finale lists each scherzo quotation (bars, theme, transposition, any deliberate transformation) in coherence/finale.md and, every cycle before promoting, compares them with the current themes-scherzo.ly using the comparison script in symphony/coherence/, updating them in that cycle if the scherzo changed. No promotion check that fails, and no lock on the finale's own themes. A final sync pass against the scherzo's last version comes when both loops reach their last cycles.
- Quotation check (from cycle 27): `python3 /mnt/project-files/symphony/coherence/themecheck.py RECORD.ly VERSION_DIR --beats 4` (report only; exit 1 = something changed). The finale keeps its own record coherence/themes-finale-quotes.ly (written with coherence/makelock.py, BEATS = 4) of its scherzo quotations as they appear in the finale, and compares them by eye with coherence/themes-scherzo.ly each cycle before promoting.

## Cycle 26 (v26 → v27), rework pass for four movements; lens 6 harp, Adler ch. 4
- Accepted: renumbered IV; link from the scherzo's G♯ (Hn 1 A♭4, Vln I A♭5, Hn 4 F♯3), direct ff; timpani retune label E,G,B,E → G,A♭,C,E♭; scherzo motive x on G in the timpani 143–145 (only scherzo quotation); no senza sord. at 1; Tpt 1·2 rest 271–272; harp D string and A♭ pedal timing.
- Kept: nothing added at 243; the Neapolitan D♭→C resolution (216–223, 226–227) is already clear.
- Do-not-touch (new): bars 1–2 voicing with A♭4/A♭5 on top continuing the scherzo's G♯.
- Open (relay from movement I, 2026-10-12 22:43): movement I's record is in symphony/coherence/ (themes-mvt1.ly, themes-mvt1.md, mvt1.md) and takes precedence over cyclic-notes.md. Corrections: movement I's Tpt 1 already moves B→C into minor tuttis (I 26→27); what is withheld for the finale is B→C on a C-major arrival. The bare motto tail E♭–D–D♭–C occurs in movement I only at 118–121 (the bass clarinet at 2–3 plays E♭–D–C–D♭–C). Assigned to cycle 30 (lens 10): check every movement I quotation in the finale against themes-mvt1.ly, and list them in coherence/finale.md.

## Cycle 27 (v27 → v28), lens 7 texture, Adler ch. 17
- Accepted: F2 counter-melody 69–70, 189–190; canon octave 226–230; bassoon solo accompaniment 115–122; Cl 1 at 186.

## Cycle 28 (v28 → v29), lens 8 expression, Adler ch. 11, 15
- Accepted: no cymbals at 247, 251; theme B recall phrased as in movement II (breath after 214); woodwinds ff at 211–212 (partly revises cycle 9); timpani f at 224; sf> at 138; mf at 234.
- Do-not-touch (critic): 219 sub. p → 223 fff arrival with timpani roll and first crash; 222→223; chorale top lines.

## Cycle 29 (v29 → v30), lens 9 holistic, Dvořák 9/iv
- Accepted: scherzo theme A head in C major at 275–276 (second scherzo quotation; recorded and sent to the scherzo thread); Hn 3·4 C4 at 224; no accents on tied notes at 279.
- Kept: woodwind doubling of theme B 211–218.

## Cycle 30 (v30 → v31), lens 10 cyclic design, Casanelles ch. 5
- Accepted: full quotation record (35 checks) and list in coherence/finale.md (closes the movement I open item); stepped crescendo 219–223; cymbals only at 223, 263, 278; pickup G3 at 246 restoring movement I's rising sixth.
- Open (scherzo critic, 2026-10-13 00:08): movements II and III end with the same close a major third apart, 5–♯4–4–3 over a plagal cadence with mixture (E♭–D–D♭–C in A♭; B–A♯–A–G♯ in E). Decided: complete the chain in the finale's C-major close with G–F♯–F–E over C – F♯°7 – F minor – C (theme A's tail pitches), in the existing IV6/4–iv6/4–I area at 273–276 or nearby, audible in one voice. Assigned to cycle 32 (harmony). Keep fff at 278 and the scherzo quotation at 275–276 (record checks).
- Scherzo v11: its horn call opens with a rising sixth G♯3–E4 (bars 2–4); the finale does not quote it. Scherzo cellos end pizz. E2 at 383 (finale.md link text corrected).

## Cycle 31 (v31 → v32), lens 1 melody, Adler ch. 3
- Accepted: F1 continuation in major at 271–272 (falls to C at 273); line starts on C at 250; stringendo runs end on held G at 246; Vln II sul G at 81, 194.
- Scherzo v12 (message 2026-10-13 00:22): trio tune T's bars 10–11 changed (peak moves to the third phrase). The finale does not quote T; no change needed. Theme A head, motive x, ending and timpani unchanged.

## Cycle 32 (v32 → v33), lens 2 harmony, A&S Unit 17
- Accepted: closing chain G–F♯–F–E over C – F♯°7 – iv6/4 – I at 273–275 (closes the cycle-30 open item; movement II and scherzo told); parallel fifths/octaves removed at 32, 35, 38, 57, 79, 88–89, 111, 127, 177, 236, 239–240, 247.
- Kept: fifths at 2, 6, 12–20, 25, 152–165, 199, 239–240 tune.
- Tool: /mnt/project-files/symphony/mvt3/tools/critic-scripts/c032/p5.py counts only true fifths (allpairs_par.py also counts fourths).
- Do-not-touch: top C6 over 273–274 with the quotation 275–276 and fff 278; German-sixth openings 1–2, 5–6.
- Scherzo bar numbers (2026-10-13 00:42): its B–A♯–A–G♯ close is at 365–368 since scherzo v04 (earlier entries say 373–376).

## Cycle 33 (v33 → v34), lens 3 form, Rimsky-Korsakov ch. IV
- Accepted: development F2 at 123–130 rescored as an upward hand-over cellos → violas → Cl 1 → Vln I/Fl 1 with a scoring crescendo into 131 (harp loses the melody; the scherzo's 73–80 now has the symphony's harp melody); woodwinds rest 255–256 and re-enter p at 257.
- Kept: the dip at 230–238 (deliberate, Dvořák 9/iv model).
- For the cycle-40 relay: cyclic-notes "Still unused: harp melody" is now covered by the scherzo, not the finale.

## Cycle 34 (v34 → v35), lens 4 orchestration, Adler ch. 15
- Accepted: chain G–F♯–F–E doubled by Vln I lower note and Ob 1 at 273–276 (revises cycle-24 layout, all pitch classes kept); Vln II rests 123–126; upper woodwinds re-enter mf at 257.
- Do-not-touch: 123–131 upward hand-over; held C6 over 273–274 with quotation 275–276; arrival and chorale 223–234.
- Scherzo v14 (2026-10-13 01:07): coda's last trio-tune statement starts in A major (349–356); close 365–368, last G♯, theme A head, motive x and timpani unchanged. No finale change.

## Cycle 35 (v35 → v36), lens 5 engraving, Gould ch. 1–2
- Accepted: shared-staff crossings shown with separate stems (262–264 Tpt, 211, 215, 111–114, 195, 197); unison collisions at 211, 273; \cbaw macros for "change bow at will"; "1." labels at 110, 126, 129. No sounding change.
- 2026-10-13: score-r07.mp3 in v27–v36 were stale copies of v26's render carried by the critics' scratch copies; removed, and promote.sh now excludes score-r0*.mp3.
- Open (mvt II note 2026-10-13 01:36): finale.ily comment says scherzo tail 373–376; correct to 365–368 at the next promotion (comment only).

## Cycle 36 (v36 → v37), lens 6 playability, Adler ch. 6–7
- Accepted: bassoon/contrabassoon rests 231–234, Bn 2 247–254; horn rests 265–268 (Hn 3·4), 269–272 (Hn 1·2); Fl 1 scale into C7 at 222–223; low reeds mf at 257; Bn p at 67, 187; bass clarinet low C up an octave (223, 278). The 373–376 comment open item is fixed.

## Cycle 37 (v37 → v38), lens 7 texture, Adler ch. 16
- Accepted: Bn 1 counter-line 125–130; violas enter late at 124; Hn 3·4 repeated quarters 129–130; bass F♯ at 124.
- Kept: E–E♭–F–E meets the chain on F at 274 (copies the scherzo's close).

## Cycle 38 (v38 → v39), lens 8 expression, Casanelles ch. 4, 6
- Accepted: Largamente 2 = 72 from 273; Tpt ff at 273; bassoon solo shaping 115–122; harp pp 123 with crescendo from 129; woodwinds f at 259; hairpins at 134, 210 end on rests.
- Do-not-touch: woodwind rest 255–256 and mf re-entry 257; 219–223 crescendo.

## Cycle 39 (v39 → v40), lens 9 holistic, Beethoven 5/iv
- Accepted: allargando 271–272; 276 held Cs moved off the quotation's D–D♭; timpani tied-note accent at 279; horns end at 133; harp ottava closed at 82.
- Note: syllabus reading for Rimsky examples 201–260 gives PDF 376–440; examples 201–208 are on PDF 364–375.

## Cycle 40 (v40 → v41), lens 10 cyclic design, Adler ch. 1, 15
- Accepted: violas 273–276 keep E♮ (upper violas join the chain, ending E4); finale.md corrections.
- Checked: all quotations against I v221, II v195, scherzo v18; link at bar 1; chain under Largamente.
- Relay for cycles 31–40 sent to the coordinator.

## Cycle 41 (v41 → v42), lens 1 melody, Adler ch. 7
- Accepted: Fl 1 at pitch with Tpt 61–63; Ob 1 rests 181–183, Fl 1 with cor anglais; violas' F2 bar with its leap at 125; oboes up an octave 24–26, 164–166.
- Do-not-touch: F1 head and peak 22/162; trumpet solo 51–62; muted trumpet with cor anglais 171–186.

## Cycle 42 (v42 → v43), lens 2 harmony, A&S Units 22–23
- Accepted: G–A♭–B run at 222; chord changes restored 116/118/124/126; canon second players 226–227; bassoon counter-line 126–129; 210 seventh resolution in violins only.
- Do-not-touch: closing chain 273–276 with viola voicing; plagal close 231–234; III♯ approach 241–247.

## Cycle 43 (v43 → v44), lens 3 form, A&S Units 16, 19
- Accepted: recap begins over G pedal at 151–152 (i6/4), tonic root at 155.
- Noted, no change: the second theme's minor-to-major turn occurs three times; development is short (12%); slow part of coda twice the fast part. All in protected passages.

## Cycle 44 (v44 → v45), lens 4 orchestration, Adler ch. 15
- Accepted: Cl 1 up an octave 255–264; Ob 2/Cl 2 up an octave 226–228; timpani G roll 151–152.
- Do-not-touch: 199 hammered layout; 123–130 hand-over with harp.
- Movement II loop finished at mvt2/v201 (2026-10-13 03:49); theme B and the closing E♭–D–D♭–C unchanged; coherence/mvt2.md final.
- Scherzo v21/v24 (messages 2026-10-13 03:56, 04:48): scherzo now 376 bars; motto-tail close at 357–360, motive x at 241 and 249, last G♯ ends at 376; new B–A♯–A–G♯ in Fl 1/Cl 1 at 206–209. Its timpani muta label now reads "low E in G, G in A♭, B in C, high E in E♭". finale.md line 7 corrected (scherzo cellos end pizz. E2, not arco E3). Open for the next promotion: retr.ily comment bar numbers (v04 → v24), and match the bar-1 timpani label wording.

## Cycle 45 (v45 → v46), lens 5 engraving, MOLA
- Accepted: rehearsal marks over strings when Vln I hidden; 219–222 widened; letters R 255, S 273; tied timpani rolls; duration in header. Scherzo open items (label wording, retr comment) done.

## Cycle 46 (v46 → v47), lens 6 playability, Adler ch. 9–10
- Accepted: brass breaths at 246, 250, 254; Tbn 1·2 rest 265–268; Hn 1·2 rest 211–214; Hn 2/3 swap 207–210; breath marks in the F2 solos.

## Cycle 47 (v47 → v48), lens 7 texture, Rimsky-Korsakov ch. III
- Accepted: movement I head's lower octave moved up at 265–268; Cl 1 on E–E♭–F at 273–274; clarinets rest 75–82.

## Cycle 48 (v48 → v49), lens 8 expression, A&S Unit 3
- Accepted: brass crescendo 244–247; tied top C and timpani roll 273–276; accents only on strong half notes 255–262; earlier diminuendo at 62, 182.
- Do-not-touch: 205–223 dynamic path; breath marks 54/58/62, 214, 250/254; fff only at 278 in the close.

## Cycle 49 (v49 → v50), lens 9 holistic, Dvořák 7/iv
- Accepted: 247–254 Vln II up, oboes with trumpets; Vln II eighth-note arpeggios 255–262; bassoons rest 235–238. finale.md item 8 updated.
- Do-not-touch: close 273–279.

## Cycle 50 (v50 → v51), lens 10 cyclic design, Rimsky-Korsakov prefaces and ch. IV
- Accepted: horns complete the chain at 275–276 (hold E4); scherzo quotation moved into Vln I + Fl 1 (C6) with Tpt 1·2 + Cl 1; quotation record 34 checks; finale.md rewritten (entries 13–15, chain voices).
- Naming rule from now: "motive x" = the scherzo's motive only; the finale's eighth-note figure at 3–4 is "the scale figure".
- Relay for cycles 41–50 sent; themes-mvt1.md correction (major hammered tutti at 247–254) passed to the coordinator for the movement I thread.
- Scherzo v31 (2026-10-13 06:32): its horn call now stays on D♯ (no resolution), so the finale's 243–246 is the call's only resolution in major. Open for the next promotion: intro.ily comment '368–384' → 360–376 (scherzo v24+ numbering).

## Cycle 51 (v51 → v52), lens 1 melody, Sebesky ch. 6–7
- Accepted: violins at 212, 214; Tpt 3 F at 266/268/270; counter-melody quarters at 74, 194. intro.ily comment open item done.

## Cycle 52 (v52 → v53), lens 2 harmony, A&S Units 24–25
- Accepted: 95–97 bass E♭ held; 47–50 suspension and V7 voicing; Ob 2 at 214; no doubled leading tone 147–150.
- Do-not-touch: stretto 139–146.

## Cycle 53 (v53 → v54), lens 3 form, A&S Unit 18
- Accepted: development climax ff 110–113 with trumpets, tuba, timpani; 6/3 bridge replaces F1 head at 87–90; mf at 7–10.
- Do-not-touch: lament 107–110; retransition into the recap over the dominant.

## Cycle 54 (v54 → v55), lens 4 orchestration, Adler ch. 8
- Accepted: climax melody doubled in woodwinds, brass f at 110–113; trombones rest 87–90; Vln I with flutes on theme B 212–214; Bn 2 dominant pedal 7–10.

## Cycle 55 (v55 → v56), lens 5 engraving, Adler ch. 18
- Accepted: page/system breaks for solos; bassoon entries 101/105; letter M at 187 (so letters from cycle 45 are now S at 255 and T at 273); tempo marks over brass; 8va at 223; breath mark 118/119. No sounding change except Bn 1 entering on beat 2 at 101, 105.

## Cycle 56 (v56 → v57), lens 6 playability, Adler ch. 12, 14
- Accepted: div./unis. at 243–245 and 273–278; timpani f at 110.
- Do-not-touch: percussion plan; timpani tuning and bar-1 label; 222→223 timpani G→C with Tpt 1 B→C.

## Cycle 57 (v57 → v58), lens 7 texture, Sebesky ch. 1
- Accepted: scale figure in low strings at 110/112; Vln II and A♭ at 89–90; clarinets rest 67–74, 187–194; violas' figure at 19–26 with Hn 1·2 f.

## Cycle 58 (v58 → v59), lens 8 expression, Sebesky ch. 1, 6
- Accepted: clarinets rest 187–198; dynamics in the bridge 87–90; p at 114; f at 10; bowing at 3–4; Cbn mf at 19.
- Do-not-touch: trumpet solo 51–66 with pp accompaniment; F1 articulation 11–26, 151–166; climax 107–113.

## Cycle 59 (v59 → v60), lens 9 holistic, Tchaikovsky 4/iv
- Accepted: climax melody in octaves 110–113; octave restored at 89–90; Hn 1 with F2 at 187–194.
- Kept: P head 247–254 in one octave.

## Cycle 60 (v60 → v61), lens 10 cyclic design, Sebesky ch. 1, 9
- Accepted: Tpt 3 B♭ at 110/112 (no full-brass C major before 223); F♯→G at 219–220 so E4 comes only from D♯; timpani motive x mf at 143; finale.md updated.
- Relay for cycles 51–60 sent; scherzo thread told about 143 and the Hn 3 D♯→E.

## Cycle 61 (v61 → v62), lens 1 melody, A&S Unit 21
- Accepted: climax melody tie and 4–3 at 110–112; F1 consequent 4–3 at 25, 165 (F1 change, in finale.md); C–D–E–D at 250; 7–6 chain at 87–89.

## Cycle 62 (v62 → v63), lens 2 harmony, A&S Units 28–29
- Accepted: German sixth at 109; Neapolitan D♭ in F1 at 163 (recap only); bassoons 110–113; 7–6 resolution 88; suspension preparation 25/165.

## Cycle 63 (v63 → v64), lens 3 form, Adler ch. 15, 17 (rerun after a lost worker)
- Accepted: Vln II rest 171–186; bassoon-solo accompaniment 114–122 (Bn 2 rest, violas up, Vln II at 119).
- Kept: coda slow/fast proportion (decided twice now, cycles 43 and 63).
- Pending (2026-10-13): the first critic-063 run survived the worker loss and wrote critics/reports/c063-second.md (Vln I answers to the bassoon solo 117/122; violas arco sul tasto at 171–186; harp rests 187–198). Accepted; apply with scratchpad apply_c063b.py on top of critic 064's work at its promotion (v65).

## Cycle 64 (v64 → v65), lens 4 orchestration, Adler ch. 11; plus c063-second
- Accepted (c064): horns doubled at 110–113; Tpt 2 with Tpt 1 on the chorale 255–258.
- Accepted (c063-second, pending item done): Vln I answers 117/122; violas arco sul tasto 171–186; harp rests 187–198.

## Cycle 65 (v65 → v66), lens 5 engraving, Gould
- Accepted: collisions at 262–264 and 111; p at 122; double bars at 151, 171; text placement at 124; "sul tasto" at 171.

## Cycle 66 (v66 → v67), lens 6 playability, Adler App. A
- Accepted: breaths/rests in long wind and brass holds (34, 51–86, 146, 170–198, 214/218/225, 230, 246–254). Ranges all within professional limits.

## Cycle 67 (v67 → v68), lens 7 texture, Sebesky ch. 3
- Accepted: bass and leading tone kept at 170; Vln II octave below Vln I at 128–130; violas ord. at 181–182; Fl 1 mp at 129.

## Cycle 68 (v68 → v69), lens 8 expression, MOLA
- Accepted: dynamics on notes not rests (42, 170); full crescendo 196–198; violas mf at 130; bassoon solo peak mp; duplicate dynamics removed.

## Cycle 69 (v69 → v70), lens 9 holistic, Mozart 41/iv
- Accepted: Neapolitan sixth voicing at 163; Hn 2 down an octave at 250, 265–268; Tpt 2 on the chorale line 259–260.
- Decided: no F2 return in the coda.

## Cycle 70 (v70 → v71), lens 10 cyclic design, A&S Unit 23
- Accepted: Tbn 1·2 on the P head at 247–254 (owed item 6 met; record 36 checks); finale.md updated; comments fixed.
- Relay for cycles 61–70 sent.

## Cycle 71 (v71 → v72), lens 1 melody, Adler ch. 11
- Accepted: Tbn P head an octave lower with Bn 1/Vc at 247–254; trumpets on 271–272 instead of 269–270; Bn 1 up at 273–276.
- For the cycle-80 relay: tell movement I the Tbn doubling of its P head is now three octaves below the violins.

## Cycle 72 (v72 → v73), lens 2 harmony, A&S Units 30–31
- Accepted: B.tbn rests 247–254; Tpt 1·2 unison 262–264 with Tpt 3 on E; trumpet F1 start at 271; Hn 3 at 251; Tbn 1 at 163.
- Do-not-touch: lament 107–110; plagal close 227–234; C–A♭–E key cycle.

## Cycle 73 (v73 → v74), lens 3 form, A&S Units 6–8
- Accepted: F2 recap major statement in A♭ (187–197) instead of C; retransition bass to G at 147–150; no meno mosso at 171.
- Rule now holds inside the finale too: no C-major key area before 223.
- For the cycle-80 relay: F2's key at 187 changed (C → A♭).

## Cycle 74 (v74 → v75), lens 4 orchestration, Adler ch. 5
- Accepted: violins in unison on F2 at 187–196 with violas and Hn 1 below; Cl 1 rests 171–180; Hn 3 C4 at 257–258.

### Dan's note (2026-10-13 13:26 UTC), to apply at the v76 promotion
Dan: the tempo at R (2 = 100) "sounds kind of silly, comically fast". Decision: R 247 becomes "Più allegro" 2 = 88 (the stringendo at 243–246 already ends at \mt 176 = 2 = 88); allargando 271–272 becomes \mt 164, \mt 152 before Largamente 2 = 72. Apply to the cycle-75 scratch global.ily before promoting v76. Later critics must not raise R above 88 without a strong reason.

## Cycle 75 (v75 → v76), lens 5 engraving (MOLA, parts)
- Accepted all six: part-only cues before long-rest entries; mute changes in Tpt 1's rests (167, 187); restated dynamics after rests; score-only marks tagged 'score; \global breaks and \mt tagged 'score; new parts book (parts-book.ly, 30 parts).
- Applied Dan's tempo note: R 247 "Più allegro" 2 = 88 (was Allegro molto 2 = 100); allargando 271–272 \mt 164, 152. Do not raise R above 88.
- 0 warnings, 16 pages, 36/36 quotations.

## Cycle 76 (v76 → v77), lens 6 playability (Rimsky ch. I)
- Accepted: Hn 1·2 ff at 243–246; Tpt 1·2 rest 253–254 (Ob 1·2 take the line); Vln I unis./div. at 275/277; MIDI stringendo now reaches 88 at 247.
- Kept: Cl high E 265–268; Vln II A6 at 252. R stays 88.
- finale.md updated (R tempo, item 9). 0 warnings, 16 pages, 36/36.

## Cycle 77 (v77 → v78), lens 7 texture (Adler ch. 8)
- Accepted: Cl 1 an octave higher on the S head 247–254 (pickup G4 at 246). Kept: Hn ff 243–246, trumpet rest 253–254, heads at 250, 265–272 exchange. R stays 88.

## Cycle 78 (v78 → v79), lens 8 dynamics (Adler ch. 7)
- Accepted: winds/brass release at the end of 264 (quarter rest) before 265; breath marks after 272 in the woodwinds.

## Cycle 79 (v79 → v80), lens 9 master comparison (Eroica; Adler part 2 ch. 16)
- Accepted: opening scale figure (bars 3–4) returns in C major in the strings at 263–264. Kept: trumpet rest 253–254; slow-coda proportion (cycles 43, 63); R 88.

## Cycle 80 (v80 → v81), lens 10 coherence (A&S Unit 28)
- Accepted: violas E4 in the 223 arrival chord; Ob 1 D♭→C at 219; record text fixed (iiø6/5, not ♭VI; scherzo v59). No quotation updates needed.
- Relay to coordinator sent after cycle 80.

## Cycle 81 (v81 → v82), lens 1 (A&S Unit 3)
- Accepted: violas unison E4 at 223 (F4→E4 step); Hn 4 d2 c2 at 254. finale.md item 2 updated.

## Cycle 82 (v82 → v83), lens 2 (A&S Unit 27)
- Accepted: Hn 4 E3 at 239; Bn 1 B–F at 245–246; harp C4 at 238. F2 in A♭ at 187 confirmed.
- Scherzo v62 FYI: trio tune cadence now a 4–3 suspension (not quoted by the finale; no change).

## Cycle 83 (v83 → v84), lens 3 (A&S Unit 15)
- Accepted: Ob 1 G♯ at 243; iii at 256 (protected 255–263 progression now I6–iii–vi–iiø6/5–Ger6–V7–I; top line unchanged).

## Cycle 84 (v84 → v85), lens 4 orchestration (Casanelles ch. 6)
- Accepted all six brass fixes at 243–262 (V7 seventh at 262, E-major third at 243, seventh doubling 244–247, iii at 256, Tpt 1·2 f until 255, Tpt 3 C4 at 257).

## Cycle 85 (v85 → v86), lens 5 engraving (Adler ch. 2)
- Accepted five string-notation fixes (263–264 bowing, viola div. 87/91, cello div. 223/277, viola release 114, violin slur 103–104).

## Cycle 86 (v86 → v87), lens 6 playability (Sebesky ch. 2)
- Accepted: Tpt 1·2 rest 251–254; Ob 2 rests 265–268; Hn 1 octave lower 265–268; no horn pickups 269/271; final-chord horns doubled (1+3 C5, 2+4 E4).

## Cycle 87 (v87 → v88), lens 7 texture (Rimsky ch. II)
- Accepted: Cl 2 upper octave 251–254; Cl 2 and Bn 1 double F1 at 265–268. Kept chorale unison 255–262.

## Cycle 88 (v88 → v89), lens 8 dynamics (Adler ch. 10)
- Accepted: Fl 1 C7 at 263 and Cl 2 up an octave 257–264; strings f at 255 → ff 259; crescendo into 211 aligned; ff print fix at 265; stopped horns at 138. Declined bass drum at 263.
- v88 rendered with r04 for Dan (v88/score-r04.mp3, 7:11). r04 perc.py cannot parse \tag #'part, \tweak style, or <cymc bd> chords; rendered from a temp copy with those simplified.

## Cycle 89 (v89 → v90), lens 9 master comparison (Sibelius 2/iv)
- Accepted: Fl 1 C6 at 263–264 (reverses cycle 88's C7). Protected rule widened: C7 in any part only at 223.

## Cycle 90 (v90 → v91), lens 10 coherence (Adler ch. 17)
- Accepted: oboes/Vln II continue the chain through D–D♭–C at 276; Tpt 3 holds C4 at 220. finale.md corrected. Scherzo and movement II told; relay to coordinator after cycle 90 sent.

## Cycle 91 (v91 → v92), lens 1 (A&S Unit 20)
- Accepted: bar 253 rewritten so the two heads do not meet in octaves. Kept scherzo quotation barring, B♭ in F1, 271 arpeggio.

## Cycle 92 (v92 → v93), lens 2 (A&S Unit 5)
- Accepted five voice-leading fixes (131–132, 185–186 and 65, 111–112, 134, 196–197). Kept lament spacing 107–109.

## Cycle 93 (v93 → v94), lens 3 (A&S Unit 14)
- Accepted: A♭ at 43; leading-tone doublings removed at 52, 60, 116; Bn 1 7th resolves at 51.

## Cycle 94 (v94 → v95), lens 4 orchestration (Rimsky ch. I, III)
- Accepted six fixes in 53–138 (stop-chord doubling, bass at 91–92, oboe spacing, trombones at 110/112, counter-melody level 67–74, chords under the trumpet solo).
- v94 rendered with r07 for Dan. r07 perc.py also fails on the \tag #'part percussion cue at 221–222 (since v76); rendered from a temp copy without it.

## Cycle 95 (v95 → v96), lens 5 engraving (Gould ch. 1)
- Accepted: \mergeRests for the parts; horn clefs score-only at 25–26/165–166; stem fix; violin crescendo at 77.

## Cycle 96 (v96 → v97), lens 6 playability (Adler ch. 2)
- Accepted eight string bowing/playability fixes in 1–150 and a harp cue at 119–122.
- v94 rendered with r07 for Dan (v94/score-r07.mp3, 7:08), from a temp copy without the percussion part cue (r07 perc.py cannot parse \tag inside drum sections).

## Cycle 97 (v97 → v98), lens 7 texture (Adler ch. 11)
- Accepted: Vln II unison on the countersubject 27–38; F2 counter-melody revoiced 70–73/190–193; horns and Tbn 1 on the F1 head at 103–104; chords mf at 27. Internal to the finale; no other movement affected.

## Cycle 98 (v98 → v99), lens 8 (A&S Unit 21)
- Accepted: brass ff at 110–113 (reverses c054); dynamics at 95–97, 105, 67–77, 108.

## Cycle 99 (v99 → v100), lens 9 master comparison (Elgar 1/iv)
- Accepted: bass trombone strike-and-release at 110/112; contrabassoon sounding C1 at 263 and 278.

## Cycle 100 (v100 → v101), lens 10 coherence + release check
- Accepted: Vln II A♭5→G5 at 222→223; finale.md and BRIEF.md corrected. Relay after cycle 100 sent.

## Cycle 101 (v101 → v102), lens 1 (Rimsky ch. II strings)
- Accepted: Vln II with Vln I on the scale figure at 263–264. Phrase lengths 151–279 confirmed.

## Cycle 102 (v102 → v103), lens 2 (A&S Units 9–10)
- Accepted: bass B at 176 (no root ii–V7–i in C minor); 6/4 fourth resolves down at 221; held fourth at 152; Hn 3 Neapolitan at 164.

## Cycle 103 (v103 → v104), lens 3 (A&S Unit 26)
- Accepted: 183 now V–i6 (not a third deceptive cadence).

- 2026-10-13 21:19: scherzo loop moved to session cse_011uo61BdJV54PsP5ATLYMHU ("Scherzo loops, cycles 80–200"); send scherzo messages there.

## Cycle 104 (v104 → v105), lens 4 orchestration (Rimsky ch. III)
- Accepted: horns/Tbn mf at 207; Cl ff at 151; Hn 4 A♭3 at 211–212. Rejected Tpt 3 D4 at 221 (would undo cycle 102's 6/4 resolution; the c104 comment in codaTwo.ily describes the rejected version).

## Cycle 105 (v105 → v106), lens 5 engraving (Gould ch. 1 beams)
- Accepted six engraving fixes (beams, cues before 199, part whole notes, crescendo endings, percussion part settings).

## Cycle 106 (v106 → v107), lens 6 playability (Adler ch. 3)
- Accepted: viola div. at 211; bass change bow at 217–218. Everything else in 151–223 confirmed playable.

## Cycle 107 (v107 → v108), lens 7 texture (Adler ch. 5)
- Accepted: Vln II counter-line 159–165; Hn 1 theme-B echo 217–218 (finale.md item 15; movement II is final, no thread to notify); Vln II scale kept 207–208.

## Cycle 108 (v108 → v109), lens 8 dynamics (Rimsky ch. IV)
- Accepted five dynamic fixes (horn echo a2 at 217–218, staggered crescendo into 223 with brass last, brass re-entry at 199, fade 167–170, Vln II marking at 159).

### Procedure rule (coordinator, 2026-10-13 22:37 UTC)
The shared-folder mount expires about 24 h after a thread's machine starts and does not come back. At the start of each cycle check `cat /proc/uptime`; past ~22 h, finish and promote the current cycle, send the coordinator a handoff (last promoted version, anything unpromoted, next command), then stop. On any I/O error under /mnt/project-files, do not retry; send the handoff at once.

## Cycle 109 (v109 → v110), lens 9 master comparison (Brahms 2/iv)
- Accepted: Vln I octaves 159–164; chorale line in Cl 2 at E5 257–264; violas F1 at C4 265–268. finale.md updated.

## Cycle 110 (v110 → v111), lens 10 coherence (A&S Unit 32)
- Accepted: Hn 2 F♯4 at 219 (respelling carried); held D♭ ff>f at 216–217; finale.md corrected. Relay after cycle 110 sent.

### PAUSED 2026-10-13 23:10 UTC at v111 (Dan: usage limit). Cycle 111 critic stopped early, nothing written. See mvt3/CHECKPOINT.md.

### RESUMED 2026-10-16 01:10 UTC in thread "Continue movement 4 loop" (session cse_01QDtx9SfJvuVALZjuqD7wEm), working in the git checkout /home/user/claude_composes (kit paths changed from /mnt/project-files). Batches of 10 cycles, each checkpointed to main by PR. Scherzo loop: session cse_019MVHJqMqMN1aRTnYSzHgLw ("Continue movement 3 loop"), resumed at scherzo v87.

## Cycle 111 (v111 → v112), lens 1 melody (Rimsky ch. II, PDF 64-80)
- Accepted: Tpt 1-2 half-note fanfare strokes 148-150 (peak G5 at 150); Fl 1 D6 at 150 (top D6-C6 into 151); "poco a poco più animato" and \mt 172 moved from 203 to 205 (199-204 quotation stays at Tempo I), 176 at 207.
- Do-not-touch: stretto 139-146 with timpani motive x; 123-130 hand-over; arrival and chorale 222-234; R at 88.

## Cycle 112 (v112 → v113), lens 2 harmony (A&S Units 11-13)
- Accepted: Hn 3 B3 at 18 and D4 at 23.4 (ii7 seventh resolves down; ii6 under 2-7); Vln II E♭5-G5 at 119 (iiø7, no bare diminished triad).
- Open: 38.1 clarinet leaps into the seventh; 16.3/17.3 root-position diminished triad in F1's accompaniment; 78.1 spacing gap.

## Cycle 113 (v113 → v114), lens 3 form and pacing (A&S Unit 32)
- Accepted: 82 tune holds E♭ a half then runs G-A♭-B♭-D cresc. into 83 (animando now carried); finale.md updated.
- Do-not-touch: the 187-223 path (♭VI-♭II-Ger6-V-I, 222→223); arrival and chorale 223-234; last cadence 259-263.

## Cycle 114 (v114 → v115), lens 4 orchestration (Rimsky tutti appendix, ch. IV examples)
- Accepted: harp RH rests 82.3-4; Hn 1 G4 at 148-150 (strokes not covered); low strings mp 187-196 under F2 in A♭; Hn 1-2 cresc. through 82.
- Note: scherzo v91 (cycle 90) rescored its ends (Hn 2 → Bsn 1 under the opening horn call; closing timpani roll → motive x ppp 363-371); no theme change, nothing the finale quotes.

## Cycle 115 (v115 → v116), lens 5 engraving (Gould ch. 1 ledger lines, octave signs, rests)
- Accepted: Vln I C7 at 223 written at pitch (no one-note 8va; stem up); stray \ottava #0 removed from Cb at 82. Parts build checked (30 parts).

## Cycle 116 (v116 → v117), lens 6 playability (Adler ch. 4 harp)
- Accepted: harp "étouffez" at 82 and 243; no low D1 string (242 now D2-D3, tuning note at 67 removed); harp f with LH octaves 239-242.
- Do-not-touch: the harp's three broken-chord passages and pedal diagrams (67, 123, 235); harp rest 187-198.

## Cycle 117 (v117 → v118), lens 7 texture (Adler ch. 15)
- Accepted: Fl 2 doubles Vln II arpeggio 8va 257-262; Hn 1-2 cresc. 142, f at 143 (dynamics only in the stretto); Vln II E5 only at 275 (clear of the scherzo quotation).
- Do-not-touch: stretto 139-146 notes and timpani motive; strokes 147-150; combination 247-254; chorale top lines 224-228 and 255-264.

## Cycle 118 (v118 → v119), lens 8 expression (Adler ch. 2 bowing)
- Accepted: slurs per bar on theme B recall 212-214; slur split before the top G6 at 246 (Vln, Vla); bow changes on long holds at 149 and 263; Vln II single slur at 276; change bow at will 217-218 (Vln I-II, Vc).
- Do-not-touch: F1 bowing 11-26 and 151-166; the 187-198 bow plan with its down-bow peak at 198; viola portato 224-228.

## Cycle 119 (v119 → v120), lens 9 master comparison (Schumann 4/iv; v109)
- Accepted: 147-150 Ob 2 D5/B4 and Hn 3-4 F4/D4 (concords within pairs); Vc/Cb f at 273 under divided upper strings; Vln I G4-B4 at 245 (V4/3 bass not doubled).
- Open: chorale top octave 257-263 thinner than v109 (protected, still balances).
- Note: scherzo v94 changed the trio tune's second statement (180-184); the finale does not quote the trio.

## Cycle 120 (v120 → v121), lens 10 coherence + release check (A&S Unit 26)
- No score change. finale.md updated to v121 (239-247 harmony and Cbsn C1 corrected); BRIEF.md: scherzo ends with timpani motive x ppp, no roll (since scherzo v91; the 2026-10-12 HISTORY entry above is outdated on this point).
- Batch 111-120 checkpointed to main by PR; parts rebuilt in v121.
- Do-not-touch: link at bars 1-2; I-III-IV-V plan with C7 as V of F and B♮ bass 138-146; 216-223; both chorale top lines; 273-276 close with the scherzo quotation.

## Cycle 121 (v121 → v122), lens 1 melody (Adler ch. 3)
- Accepted: F1 head a third higher at 267-268 (no third identical statement); 272 takes F1's consequent peak A-G-F (A6); cellos mf on F2's counter 187-196, f at 198. finale.md F1 entries updated; no other movement quotes F1.
- Do-not-touch: chorale top lines 224-228 and 255-264; 222→223; last cadence 259-263; close 273-279 with the scherzo quotation.

## Cycle 122 (v122 → v123), lens 2 harmony (A&S Unit 17; Unit 21 pedal)
- Accepted: IV6/4 under the F1 peak at 272 (Hn 3-4, Bn 1, Vla div., Tpt 3 A4); harp LH G2 at 238 (not under the bass pedal).
- Open (kept): motto C-B against F1 B-C at 267.4.

## Cycle 123 (v123 → v124), lens 3 form (Rimsky ch. IV)
- Accepted: 268 Fl/Vln I fill E-D-C-B into 269; 265-272 bass/brass foundation f then cresc. 269-271 (no eight-bar flat ff); tuba ff at 247.
- Confirmed: coda length; A6 at 272 as the close's top note (C7 stays reserved for 223).

## Cycle 124 (v124 → v125), lens 4 orchestration (Adler ch. 15)
- Accepted: Tbn 1-2 rest 269-270, ff at 271; timpani C (not G) at 272 under IV6/4.
- Do-not-touch: cellos mf on F2's counter 187-198 (confirmed twice, c121/c124).

## Cycle 125 (v125 → v126), lens 5 engraving (Gould ch. 1-2 spacing, unisons)
- Accepted: a2 labels for Tpt 1-2 at 271 and Hn 1-2 at 273; ff restated in Vln I-II, Vla at 273.

## Cycle 126 (v126 → v127), lens 6 playability (Adler ch. 6-7 woodwinds)
- Accepted: staggered breaths in the last chorale 258/260/261; Fl 2 breaths 259, 261; Ob 1 rests 265-268 (a2 ff at 269); Bn 2 rest 146; Fl 1/Ob 1 breath after 78; Cbsn/tuba breaths 228, 250; Cl 2/Bn 1 breaths 170, 178.

## Cycle 127 (v127 → v128), lens 7 texture (Adler ch. 17)
- Accepted: 257-262 Fl 2 on the chorale top line with Fl 1 (staggered breath after 260), Cl 1 takes Vln II's arpeggio in unison; violas C4 at 257-258.
- Do-not-touch: no figuration above the chorale top line at 257-262 (c117's 8va Fl 2 doubling was reversed in c127; do not restore it). c119's open note on the thin top octave is closed.

## Cycle 128 (v128 → v129), lens 8 expression (Adler ch. 11, 15)
- Accepted: harmony and timpani cut on 264.1 (top line, woodwinds and low strings dim.) so the scale figure 263-264 is heard; string hairpins 257-259; Cbsn ff at 247; hairpins closed at 277.

## Cycle 129 (v129 → v130), lens 9 master comparison (Dvořák 8/iv; v119)
- Accepted: brass seconds/sevenths moved out of one family at 130-131 (Hn 4 A3), 147-150 (Hn 3 D4), 207-210 (Tbn 2 E♭3), 238 (Hn 3/4 D4/G3); woodwind f at 257 and ff at 259 in the last chorale (c033/c038's plan answered: rest 255-256, re-entry 257 and build kept).
- Do-not-touch: the harmony cut at 264.1 (c128, confirmed c129).

## Cycle 130 (v130 → v131), lens 10 coherence + release check (Casanelles ch. 5)
- Accepted: finale.md current to v131 (147-150 seventh, 255-264 unison, Più allegro corrected); cor anglais joins Hn 1's theme-B answer 217-218, A♭4-G4 219-220.
- Batch 121-130 checkpointed to main by PR (after PR #20).
- Do-not-touch: link 1-2; 222→223; both chorale top lines and the cut on 264.1; last cadence 259-263; close 273-279 with the scherzo quotation.

## Cycle 131 (v131 → v132), lens 1 melody (Adler ch. 7)
- Accepted: Bn 1 F2 at 117 with A4-G4-F4 (c041's register reason answered); Fl 2 with Fl 1 at E♭6 on 83-86.

## Cycle 132 (v132 → v133), lens 2 harmony (A&S Units 22-23)
- Accepted: 117 Vla rest beat 2 and Vln I A♮5; 119.4 Vln II G5 alone (octaves removed); 101/105 Hn 1-2, Cl 2 enter on beat 2; Cl 2 E♭4 at 96; Cl 1 steps into the seventh at 38.
- Closed (no change): c112 open points 16.3/17.3, 78.1.
- Do-not-touch: 107-113 lament and F-minor cadence; pivot 113-114; 115-132 G minor → G major; 6/3 bridge 87-90.

## Cycle 133 (v133 → v134), lens 3 form (A&S Units 16, 19)
- Accepted: 166 V-i6 (bass E♭) instead of the exposition's deceptive cadence; 167-170 falling-fifth link.
- Do-not-touch: return 147-155 over the dominant; 186→187 into A♭ and the 187-223 path; development key plan with the G area 115-134; stretto 139-146.

## Cycle 134 (v134 → v135), lens 4 orchestration (Adler ch. 15)
- Accepted: Ob 2 doubles Vln II's counter-line 159-166; Hn 1-2 with the violas at 165-166; Tpt 3 D4 at 165.2.
- Do-not-touch: 151-158 layout; E♭ bass and timpani at 166; 167-170 diminuendo order.

## Cycle 135 (v135 → v136), lens 5 engraving (MOLA)
- Accepted: unison flute line 83-86; score-only Oboe 2 staff 158-170; page-2 bar numbers; Ob 2 cue 197-198; bar ranges under multi-measure rests in parts; Bn 1 courtesy natural at 116.
- Open: Cl 2 part page 2 over-full (parts-only fix in c135.md).
- Note: scherzo ends ppp (scherzo thread, scherzo v111); intro.ily comment corrected.

## Cycle 136 (v136 → v137), lens 6 playability (Adler ch. 9-10 brass)
- Accepted: Hn 1 enters 141 on beat 2; Hn 1/3 rest on 206.4; Hn 3-4 rest 215-218; brass breaths after 146 and 223; Cl 2 part 10 systems per page (c135 open point closed).

## Cycle 137 (v137 → v138), lens 7 texture (Adler ch. 16)
- Accepted: clarinets hold 159-165 (counter-line clear); Vla/Vc E♭3-F3 at 197; Hn 1 A♭4 at 169; Bn 1 C4-G3 at 126.

## Cycle 138 (v138 → v139), lens 8 expression (Casanelles ch. 4, 6)
- Accepted: low strings dim. under the theme-B echo 217-218 (p at 219); swells at F2's peaks 68-70 and 188-190; movement I's phrasing on the S-head quotation 234-238; Hn espress. at 217.
- Do-not-touch: 219 sub. p → 223 fff with timpani roll, first crash and C7; 187-198 bow plan.

## Cycle 139 (v139 → v140), lens 9 master comparison (Rachmaninoff 2/iv; v129)
- Accepted: B.cl. doubles the B1 pedal from 144 (p<f into 147; Bn 1 cue removed); Tpt 3 C5-F4-C5 at 247-249 (off the horns' S-head pitch).
- Open: Tpt 3 A4 at 252 still at the horns' pitch (alternatives make fifths).

## Cycle 140 (v140 → v141), lens 10 coherence + release check (Adler ch. 1, 15)
- No score change. finale.md current to v141. c139's open item (Tpt 3 A4 at 252) closed, kept.
- Batch 131-140 added to the checkpoint PR.
- Do-not-touch: bars 1-2 with the violas' E♭4; 216-223 with 222→223; both chorale top lines and the cut at 264.1; last cadence 259-263; close 273-279.

## Cycle 141 (v141 → v142), lens 1 melody (Sebesky ch. 6-7)
- Accepted: dotted peak at 78 (Vln I-II, Fl 1, Ob 1); Cl 2 moving under the half cadences at 58 and 178; Vla/Vc counter at 81.
- Do-not-touch: trumpet solo 51-66 and 171-186 (peaks at 62/182 stay plain).

## Cycle 142 (v142 → v143), lens 2 harmony (A&S Units 24-25)
- Accepted: complete iv7 under the solo's climax at 61-62 and 181-182 (Cl 2 6-5, Vla third, Bn 1 root of V); bass A♭-F-D-E♭ at 84; Cl 2 resolves on beat 3 at 58-59 and 178-179.
- Open (kept): V7-I6 at 74→75 and 194→195.

## Cycle 143 (v143 → v144), lens 3 form (A&S Unit 18)
- Accepted: 86 imperfect cadence on I6 (bass A♭→G, arpeggio continues into the 6/3 bridge); 83-90 one phrase. Closing-group length confirmed.

## Cycle 144 (v144 → v145), lens 4 orchestration (Adler ch. 8)
- Accepted: Hn 1-2 B♭ pedal 83-86; Ob 1 rests 81-82.2 (back for the run); Bn 1 D3-F3 at 58; Cl 1 rests 97-98.

## Cycle 145 (v145 → v146), lens 5 engraving (Adler ch. 18, App. A)
- Accepted: clarinet "2." at 97-98; "1." labels at 61, 77, 105; breaths at 58 (Cl 2, Bn 1) and 82 (Hn 1-2); cues in the Ob 1 and Hn 1-2 parts.
- Note: scherzo v122 changed the trio tune's bar 6 (not quoted by the finale).

## Cycle 146 (v146 → v147), lens 6 playability (Adler ch. 12, 14 percussion)
- Accepted: 223 timpani roll fff> to f, bass drum ff (crash fff); stick indications at 1, 215, 255; bass drum tied with cymbals 278-279.
- Render note: simplify the two-voice percussion at 223 in a temp copy for r04/r07.

## Cycle 147 (v147 → v148), lens 7 texture (Rimsky ch. III)
- Accepted: crossed horn/bassoon pad 75-82; Cl 2 B♭3 at 57; Vln II A♭ at 62.4; violas B♭ at 85.4.
- Do-not-touch: horn pedal 83-86 with Bn 1 inside; Cl 2 line at 58; arrival 223-234; 6/3 bridge 87-90.

## Cycle 148 (v148 → v149), lens 8 expression (A&S Unit 3)
- Accepted: cresc. through 198 into 199; pad swells to mp at 78 (p at 81).

## Cycle 149 (v149 → v150), lens 9 master comparison (Bruckner 4/iv; v139)
- Accepted: violin tremolo mf at 224-225; clarinets in thirds at 77-79. finale.md: 263 is the first (not only) root V-I.

## Cycle 150 (v150 → v151), lens 10 coherence + release check (Rimsky prefaces, ch. IV)
- No score change. finale.md current to v151.
- Batch 141-150 added to the checkpoint PR.

## Cycle 151 (v151 → v152), lens 1 melody (A&S Unit 21)
- Accepted: G♭6 suspended 210→211 resolving to F6 (score-only \noBreak 199-210); Hn 2 doubles the violas' F1 head 130-132.
- Do-not-touch: lament and climax 107-113; stretto and strokes 139-150; theme B recall 211-218; 216-223.

## Cycle 152 (v152 → v153), lens 2 harmony (A&S Units 28-29, second pass)
- Accepted: Vln I div. F5 + D♭6 at 217-218 so D♭-C-B-C is the top line; Italian sixth (bass E♭) on 121 beats 3-4 before the G-minor half cadence; Ob 2 D♭5-F5 at 211 under the G♭6 suspension.
- Open: none.
- Do-not-touch: A♭7 209-210 / German sixth 219 (Hn 2 G♭ = F♯); violins' G♭ 215-216; 216-223 top line.

## Cycle 153 (v153 → v154), lens 3 form (Adler ch. 15, 17, second pass)
- Accepted: violas' portato quarters at 231-233 in the plagal close.
- Declined: deceptive cadence D7 → E minor at 131-132 (planned cadence in G; protected G area 115-134).
- Open: whether the settled G at 131-132 slows the approach to the return (raise again only with a form-lens case that keeps the plan's G area).
- Do-not-touch: G cadence 131-134; Italian sixth 121; stretto 139-150.

## Cycle 154 (v154 → v155), lens 4 orchestration (Adler ch. 11, second pass)
- Accepted: Vln II portato F5-E5-F5 at 231-233 above the brass; Hn 4 doubles Hn 2's F1 head 130-132; low winds and strings hold C at 229 under the timpani pulse.
- Open: 131-132 settled G (from c153).
- Do-not-touch: chorale and canon 223-234; 222→223; Italian sixth 121; G cadence 131-134.

## Cycle 155 (v155 → v156), lens 5 engraving (Gould, second pass)
- Accepted: page turn 208|209 instead of a 12-bar system 199-210; Hn 3 mf < at 130; harp 8va bassa from 239.
- Open: 131-132 settled G (from c153).
- Do-not-touch: 16-page layout; arrival 223-234; theme B recall 211-218.

## Cycle 156 (v156 → v157), lens 6 playability (Adler App. A, second pass)
- Accepted: Vln I G♭6 tie 210→211 fixed; Bn 1·2 breath after 228.
- Open: 131-132 settled G (from c153).
- Do-not-touch: 199-204; 211-223 with B→C 222→223; arrival 223-234; harp 235; horn call 243-246 with Tpt 1 C6.

## Cycle 157 (v157 → v158), lens 7 texture (Sebesky ch. 1, second pass)
- Accepted: Vln II unison with Vln I at 205-206; violas A♭4/C5 at 205-206; Hn 3 held D4 at 130; Bn 1 C4→B3 at 131-132.
- Open: 131-132 settled G (from c153).
- Do-not-touch: bassoon solo 115-122; F2 hand-over 123-130; stretto 139-150; D♭ episode 211-222.

## Cycle 158 (v158 → v159), lens 8 expression (Sebesky ch. 1, 6, second pass)
- Accepted: Vln II and violas mf from 207 under the F1 head; Hn 4 mf < at 130.
- Open: 131-132 settled G (from c153).
- Do-not-touch: 211-222 dynamic path; arrival 223-234; horn call 243-246 (no Tpt crescendo, c084).

## Cycle 159 (v159 → v160), lens 9 master comparison (Mahler 1/iv; v149)
- Accepted: Hn 4 back to v149 A3 quarters at 130-131 (reverses c154's doubling); violas whole notes at 231-233 (Vln II keeps the portato); violas C5/E♭5 at 205-206.
- Open: 131-132 settled G (from c153).
- Do-not-touch: 216-223 with B→C and G→C at 222→223; arrival chord and chorale top lines (no more inner layers 223-234); last cadence 259-263; close 273-279.

## Cycle 160 (v160 → v161), lens 10 coherence + release check (Sebesky ch. 9, ch. 1, second pass)
- No score change. finale.md current to v160.
- Closed: "131-132 settled G" (keep the G cadence; it sets up the stop chord at 138).
- Do-not-touch: bars 1-2; 216-223 with 222→223; arrival and chorale 223-234 with the C bass at 229-230; both chorale top lines and the cut at 264.1; last cadence 259-263; close 273-279; 205-208 violas (four changes in five cycles).

## Cycle 161 (v161 → v162), lens 1 melody (Adler ch. 11 melodic, second pass)
- Accepted: bass trombone holds B♭2 through the diminuendo 41-42.
- Do-not-touch: no trombones on F1 at 27-34 (their first melody is the chorale at 224); 235-279.

## Cycle 162 (v162 → v163), lens 2 harmony (A&S Units 30-31, second pass)
- Accepted: Vln II B♭ at 64.4; Fl 2/Ob 1 B♭ at 38.3; viola D-C-C♭-B♭ at 46-47; C♭ neighbour in Vla/Vc at 81.2.
- Do-not-touch: German sixth 1-2; trumpet solo 51-66; horn pedal and 6/3 bridge 83-90; 9-8 at 49; bass trombone B♭ 41-42; 222→223.

## Cycle 163 (v163 → v164), lens 3 form (A&S Units 6-8, second pass)
- Accepted: V4/2 bass at 74 and 194; V without 7th at 165; Bn 1 F3→E♭3 at 171; Vln II D at 46.
- Closed: c142's 74→75 joint.
- Do-not-touch: F1, F2, chorale top line; viola descent 46-47 with 9-8 at 49; 187-223 key path through 222→223; no PAC in the recap (by design).

## Cycle 164 (v164 → v165), lens 4 orchestration (Adler ch. 5, second pass)
- Accepted: Cl 1-2 F1 head up an octave at 83-86; clarinets f at 151; Bn 2 E♭2-E♭3 at 194.
- Do-not-touch: Vln I octave divisi 159-166 (c109); F1, F2, chorale top line.

## Cycle 165 (v165 → v166), lens 5 engraving (MOLA, parts)
- Accepted: cues at 91, 143-147, 197-199; Vln I and cello page turns on rests; rest ranges clear of marks; percussion rest ranges; stray "arco" removed (67, 187); Vln II "sul G" dashed line 81-82.
- Do-not-touch: score MIDI (part-only changes).

## Cycle 166 (v166 → v167), lens 6 playability (Rimsky ch. I, second pass)
- Accepted: Hn 1-2 rest 34.4; breaths at 140 (Bn 1-2, Hn 3-4) and 198 (Hn 1-2); Cl 1 takes the counter-line 159-165 from Ob 2; trumpets mf at 151; basses F at 33.4.
- Do-not-touch: trumpet solo 51-66; horn/bassoon pad 75-82; horn pedal and clarinet octave 83-86; Vln I divisi 159-164; Vln I B♭6 at 78.

## Cycle 167 (v167 → v168), lens 7 texture (Sebesky ch. 3, second pass)
- Accepted: Vln I single top line with Fl 1 at 91-94, Vln II double stops; Vln II f and winds mf under the tune at 159-165; winds mf under F2's string peak at 78-82.
- Do-not-touch: 151-166 layout (c134); Bn 1 at 87-90 (c058).

## Cycle 168 (v168 → v169), lens 8 expression (MOLA, second pass)
- Accepted: one level per attack at 166; f on the 103 re-entry; Vln II "cantabile" at 67 and 187.
- Do-not-touch: trumpet solos 51-66 and 171-186 with pp accompaniment; 77-82 balance (c167); codetta 91-94; 138 stop chord sf > over sub. p (c028); 187-198 bow plan.

## Cycle 169 (v169 → v170), lens 9 master comparison (Franck; v159)
- Accepted: trumpets rest at 151-158, enter mf at 159.
- Do-not-touch: the rest of the 151-166 layout (c134); coda 247-279.

## Cycle 170 (v170 → v171), lens 10 coherence + release check (A&S Unit 23, second pass)
- No score change. finale.md current to v170.
- Do-not-touch: bars 1-2; 46-49; 216-223 with 222→223; 223-234; 242-244; both chorale top lines and the cut at 264.1; last cadence 259-263; close 273-279.

## Cycle 171 (v171 → v172), lens 1 melody (A&S Unit 3, second pass)
- Accepted: Vln I answer moved to 119 over the bassoon solo's held C4; Vln I D♭6 on 211 beat 4 (reverses c159's keep of the passing C6).
- Do-not-touch: bassoon solo 115-122; hand-over 123-130; stretto and strokes 139-150; theme B recall 211-218 with the G♭6-F6 suspension; arrival and chorale 223-234; both chorale top lines.

## Cycle 172 (v172 → v173), lens 2 harmony (A&S Unit 27, second pass)
- Accepted: Hn 4 A♭3→G3 then D4 at 138-146 (no doubled leading tone); Vln II E♭5 alone at 117.2; Vln II B♭4 at 115 (7th of D7 resolves down).
- Do-not-touch: B bass 139-146 with no C (stop chord resolves to C only at 222→223); 147-150 with no ♭9.

## Cycle 173 (v173 → v174), lens 3 form, coda (A&S Unit 15, second pass)
- Accepted: MIDI tempo steps 2 = 88/90/92 at 205-210 under the printed più animato.
- Do-not-touch: R at 247 at 2 = 88; E-major chord at 243 with the horn call; cut on 264.1; 265-272.

## Cycle 174 (v174 → v175), lens 4 orchestration (Casanelles ch. 6, second pass)
- Accepted: Hn 3-4 rest 143-144 under the horns' F1 head; Vln I answers pp at 119 and 122; harp p at 123.
- Do-not-touch: stretto entries and timpani 139-150; harp notes and pedals 123-130 (c116); Hn 1-2 held F4 at 103-104.

## Cycle 175 (v175 → v176), lens 5 engraving (Adler ch. 2, second pass)
- Accepted: ties at 95-96; up-bow at 114; viola div./unis. marks cleaned (199, 219); "change bow at will" removed at 229; text outside the slur at 124.
- Open: bar-number placement at 110, 147, 212, 259, 263, 278 (padding fix costs a page; try a local tweak).
- Do-not-touch: 16-page layout.

## Cycle 176 (v176 → v177), lens 6 playability (Sebesky ch. 2, second pass)
- Accepted: Ob 1 up an octave at 207-208; tuba and Cbsn breath after 208.
- Do-not-touch: horns 138-150; A♭ pedal 205-210 in bass trombone and basses.

## Cycle 177 (v177 → v178), lens 7 texture (Adler ch. 8, second pass)
- Accepted: Cl 2 and Bn 1 (octave below) on the F1 head 207-208, Fl 2 rests 207-208; Tbn 2 E3 at 255-256 stepping to C3.
- Do-not-touch: arrival and chorale 223-234 with 222→223; both chorale top lines and the cut at 264.1; 247-254 (trombones' octave, c071/c091); close 265-279.

## Cycle 178 (v178 → v179), lens 8 expression (Adler ch. 7, second pass)
- Accepted: horns and Tbn 1·2 mp at 207-208; Fl 2 breath before 223; Cl 2 rests at 101-102 and 105-106.
- Do-not-touch: 211-223 dynamic path; flutes' staggered breaths 255-264; bassoon solo 115-122; cor anglais 217-218; arrival and chorale 223-234.

## Cycle 179 (v179 → v180), lens 9 master comparison (Saint-Saëns 3; v169)
- Accepted: MIDI tempo 205-210 rises one step per bar to 92.
- Do-not-touch: 205-210 scoring (rescored in c176, c177, c178); coda tempo plan 199-279.

## Cycle 180 (v180 → v181), lens 10 coherence + release check (A&S Unit 28, second pass)
- No score change. finale.md current to v180.
- Do-not-touch: bars 1-2; 163; 205-223 with 222→223; 223-234; both chorale top lines and the cut at 264.1; 259-263; 273-279.

## Cycle 181 (v181 → v182), lens 1 melody (A&S Unit 20, second pass)
- Accepted: Bn 1 C4-D4-A3 at 126-127 (no fifths with the violas); violas' figure at 25-26 (no augmented second at V-VI).
- Do-not-touch: hand-over 123-130; canon 226-230 (inside 223-234).

## Cycle 182 (v182 → v183), lens 2 harmony, coda (A&S Unit 5, second pass)
- Accepted: F in the ii7 at 242 (harp, Fl 2); P line E6 at 252; Hn 3·4 C4 at 239; Ob 2 holds C5 at 261; A4 at 249; low bass doublings by step at 225-227 and 249-250.
- Note for finale.md item 8: P head continuation E6 at 252.
- Do-not-touch: 223 arrival and 222→223; both chorale top lines and the canon; plagal close 231-234; 235-247 progression with its single G♯ voice; 255-263 cadence with Tpt 1 B→C; close 273-279.

## Cycle 183 (v183 → v184), lens 3 form, whole movement (A&S Unit 14, second pass)
- Accepted: V4/2 at 133-134 (cellos, basses F; violas D) after the G cadence.
- Do-not-touch: development key plan with the G cadence at 131-132; retransition 135-150; coda arrivals 199, 223, 247, 263, 278 with both chorale top lines.

## Cycle 184 (v184 → v185), lens 4 orchestration, coda (Rimsky ch. I, III, second pass)
- Accepted: Tbn 1-2 f at 247-254; Hn 3 A♭3 at 259-260 rising to E♭4.
- Do-not-touch: arrival and chorale 223-234 with 222→223; horn-call layout 243-246; final chord 278-279.

## Cycle 185 (v185 → v186), lens 5 engraving, coda (Gould ch. 1, second pass)
- Accepted: Hn 3·4 note swap at 257-262 (no crossing); Cl 2 shift at 257-262; bar-number row lowered from 209 (closes c175's open item); Q text on two lines in parts; R above its tempo mark.
- Do-not-touch: 223-234 with 222→223; both chorale top lines and the cut at 264.1; flute breaths 255-264; cadence 259-263 with Tpt 1 B→C; close 273-279.

## Cycle 186 (v186 → v187), lens 6 playability, coda (Adler ch. 2, second pass)
- Accepted: bowings 247-254 (accents on down-bows); Hn 3·4 breaths after 250 and 256.
- Do-not-touch: horn call 243-246; flute breaths 255-264; final chord 278-279.

## Cycle 187 (v187 → v188), lens 7 texture (Rimsky ch. II, second pass)
- Accepted: bass clarinet doubles the basses at 27-34; Ob 2 a2 at 19-26; Cl 2 with the violas at 110-113; Bn 1 with the violas at 99-100; score-only breaks at 128, 144, 158.
- Note for finale.md: bars 1-26 changed (Ob 2 doubling at 19-26); tell the scherzo thread at batch end.
- Do-not-touch: 11-18; 77-82; 83-86; 87-90; lament 107-109; bassoon solo; stretto.

## Cycle 188 (v188 → v189), lens 8 expression (Adler ch. 10, second pass)
- Accepted: ties for held winds and brass at 28-34, 39-42, 52-66, 9-10; slurs matching the violins at 111-112.
- Note for finale.md: bars 9-10 changed (ties only).
- Do-not-touch: bars 1-2; trumpet solo 51-66 scoring and pp.

## Cycle 189 (v189 → v190), lens 9 master comparison (Borodin 2/iv; v179)
- Accepted: Hn 3 D4→E♭4 at 259-261 (removes fifths with the bass).
- Do-not-touch: bars 1-2; 216-223 with 222→223; 223-234; both chorale top lines and the cut at 264.1; 259-263 with Hn 3 D4→E♭4 and Hn 4 A♭3; c188 ties; close 273-279.

## Cycle 190 (v190 → v191), lens 10 coherence + release check (Adler ch. 17, second pass)
- No score change. finale.md current to v190.
- Do-not-touch: bars 1-2; 51-66; 115-130; 205-223 with 222→223; 223-234; both chorale top lines and the cut at 264.1; 259-263; 273-279.

## Cycle 191 (v191 → v192), lens 1 melody (Rimsky ch. II, second pass)
- No score change.
- Do-not-touch: 247-254 layout; 187-198 with the bow plan; 159-164 divisi; 27-34.

## Cycle 192 (v192 → v193), lens 2 harmony (A&S Units 9-10, final pass)
- Accepted: Ob 2 C5 (was A♭4) on beats 3-4 of 160, removing parallel 5ths with the tune's upper octave into 161 (iv7→V).
- Kept: inner 5ths at 15→16 and 155→156 (passing eighth); 198→199 horn climb into the quotation; cadential 6/4s at 151, 220, 243-244.
- Do-not-touch: 151-166 scoring and tune; 259-263 cadence; 222→223; both chorale top lines.
