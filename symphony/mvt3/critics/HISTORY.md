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

## Cycle 193 (v193 → v194), lens 3 form (A&S Unit 26, second pass)
- No score change.
- Do-not-touch: key plan III–iv–v/V; recapitulation over the dominant at 151; F2 in A♭ at 171-198; tempi 211-246; rehearsal letters.

## Cycle 194 (v194 → v195), lens 4 orchestration (Rimsky ch. III, second pass)
- Accepted: 16-foot bass octave at 110-113 (Cbsn C1 at 110; Cbsn and tuba F1 at 111.1; tuba, Cbsn and basses F1 at 113).
- Do-not-touch: upper parts 110-113; trumpets at 110 and 112; 91-94 low brass; 147-150.

## Cycle 195 (v195 → v196), lens 5 engraving (Gould ch. 1 beams, second pass) + parts layout
- Accepted: flat rests at 128-142 in global.ily (closes the cor anglais compression); bass clarinet part on two facing pages; cor anglais break before 205; percussion tempo marks spaced; Tpt 1·3 padding; Fl 1 beam slope at 222.
- Do-not-touch: 16-page score layout and score-only breaks; 216-223; 223-234; 259-263; 273-279.

## Cycle 196 (v196 → v197), lens 6 playability (Adler ch. 3, second pass)
- No score change.
- Do-not-touch: 110-113 low octave; 91-94 viola double stops; 144-150 double stops; bars 2 and 6.

## Cycle 197 (v197 → v198), lens 7 texture (Adler ch. 11, second pass)
- No score change.
- Do-not-touch: stretto 139-150; 247-254; 99-109; 205-208; 265-272.

## Cycle 198 (v198 → v199), lens 8 expression (A&S Unit 21, second pass)
- No score change. Open: finale.md wrongly says the basses reach ff at 271; fix at cycle 200.
- Do-not-touch: 87-90 chain; 210-211 suspension; 135-138 and 222→223; horn call 243-246; C pedal 263-279.

## Cycle 199 (v199 → v200), lens 9 master comparison (Casanelles ch. 6; v189)
- No score change. All changes since v189 confirmed.
- Do-not-touch: bars 1-2; 51-66; 110-113; 151-166; 216-223 with 222→223; 223-234; both chorale top lines and the cut at 264.1; 259-263; 273-279.

## Cycle 200 (v200 → v201), lens 10 coherence + final release check
- No score change. finale.md current to v200 (basses f 265-274 corrected). Release check passed. Loop complete.
- Do-not-touch: bars 1-2; 51-66; 110-113; 151-166; 216-223 with 222→223; 223-234; both chorale top lines and the cut at 264.1; 259-263; 273-279.

## Cycle 201 (v201 → v202), lens 1 melody (Rimsky ch. II, third pass)
- Accepted: 35-38 Fl 1 doubles F1's head with the violins at the unison, f, with their articulation (Rimsky PDF 76-77, 67, 54); Fl 2 marked f on the shared staff. F1's notes unchanged.
- Rejected: Fl 1 an octave above with Ob 1 at the unison (PDF 78): adds a page; Fl+Ob unison: page 2 compressed.
- Note for finale.md: 35-38 Fl 1 doubling (no effect on other movements).
- Do-not-touch: 39-42 Fl 1 held A♭5; F2 solo scoring 51-66; chorale; horn call 243-246; 205-206 horn unison.

## Cycle 202 (v202 → v203), lens 2 harmony (A&S Units 11-13, third pass)
- Accepted: 169 violas resolve the iiø7's seventh C4 down to B3 (was up to D4), D4 at 170 (A&S PDF 177, 191); the exposition got the same fix in c112.
- Rejected: 16.3 seventh on beat 3 (would leap or break protected 11-18); deceptive cadence to IV6; I-IV6-I6; ii7 before a cadential 6/4 (all 6/4s protected); 197-198 IV6/5-V6/5-I (melody 1-2-5, protected bass).
- Do-not-touch: 11-18; 26 deceptive cadence; cadential 6/4s at 109, 151, 220, 243; 197-198 bass line.

## Cycle 203 (v203 → v204), lens 3 form (A&S Unit 32, third pass)
- Accepted: 95-98 violas hold E♭4 over B♭3 and inflect it to E4 at 97 (with Cl 2), so the E♭/E♮ thread is a viola line at one pitch (1, 97, 219-220, 223); Vln I and Ob 1 pass through D5 on 95.4, top line E♭-D-D♭-C (A&S PDF 585, 597-598, 600-601). Kept although 97 now anticipates the viola E4: there it is the third of C7 (V of F), p, a different function from the arrival's E4 on C major.
- Rejected: A-major VI♯ at 239 (235-247 plan protected; 243 stays the only chromatic mediant).
- Note for finale.md: 97 is the violas' first E♮ (E4, p, over B♭3); 95.4 D5 in Vln I/Ob 1.
- Do-not-touch: bars 1-2; 113-115; 235-247 plan; 187-223 with 222→223; 223-234; both chorale top lines and the cut at 264.1; 259-263; 273-279.

## Cycle 204 (v204 → v205), lens 4 orchestration (Rimsky tutti chords, third pass)
- Accepted: harp C-major glissando C4-G6 ff on 277 beat 4 into the final chord 278 (Rimsky appendix chords 17-18, PDF 134, 136); answers c114's reasons (it fills the close's only quarter rest); G6 stays under the C7 reserved for 223; harp part gets a Vln I cue at 275-276.
- Also (composer, following movement I v225 cycle 224): 200-203 inner brass no longer double the chromatic bass, as at I 28-31: Tpt 2 G4 (200), B♭4 (202); Tpt 3 F4 (200), F4 (201), G4 (202), A♭4-F4 (203); Hn 2 G4 (202). finale.md updated.
- Rejected: wind trills (protected places; 209-210 would blur the G♭6 seventh); tuba octave at 91-94 (c194 stands); more percussion.
- Do-not-touch: 273-279 apart from the harp glissando; 216-223 with 222→223; 223-234; both chorale top lines and the cut at 264.1; 259-263; percussion plan.

## Cycle 205 (v205 → v206), lens 5 engraving (Gould ch. 1 rests, third pass)
- Accepted: score-only rest offsets on shared staves (Gould PDF 50): Cl 58 (to the centre), Cl 170, Bn 190 and 198 (one space lower); 194 left high (Bn 2 crosses above). Removed the duplicate score-only "1." for Cl 1 at 126.
- Rejected: loco marks after 82 and 242; octave clefs for Cbsn/Cb; score-only 8va to save space.
- Do-not-touch: harp 8 bassa 67-82 and 239-242; rests at 194 and 265-272; 216-223 with 222→223; 223-234; both chorale top lines and the cut at 264.1; 259-263; 273-279.

## Cycle 206 (v206 → v207), lens 6 playability (Adler ch. 4 harp, third pass)
- Accepted: harp harmonics (written B♭3, sounding B♭4, p) on 43, 45, 47 over the transition's B♭ pedal, pedal diagram moved to 43 (E♭-major setting as at 67), MIDI helper \harmOctF (Adler PDF 116, 112); "étouffez" at 131 (Adler PDF 117); final harp left hand C2-G2-C3, as movement I's last harp chord (Adler PDF 114); part prints the glissando tuning at 277.
- Note for finale.md: the harp now first enters with harmonics at 43; last harp chord matches movement I bar 182.
- Do-not-touch: violas 46-49; harp notes and pedals 123-130; 273-279 except the harp.

## Cycle 207 (v207 → v208), lens 7 texture (Adler ch. 5, third pass)
- Accepted: 187-194 soft clarinet background under F2 in A♭ (Cl 2 holds the low chord tone, Cl 1 a rocking three-note eighth figure after an eighth rest, pp, A♭3-F4), stopping at 195 (Adler PDF 132-137, 158-159, 163). Answers c057 (that pad repeated 51-58 note for note; this is a new figure, not in the exposition) and c058 (the clarinets still rest 195-198, inside the horns).
- Note for finale.md: "clarinets rest 187-198" becomes "clarinets pp background 187-194, rest 195-198".
- Do-not-touch: 235-246; 223-234; stretto 139-150; strings and bassoons 187-198; harp rest 187-198; clarinet rest 195-198.

## Cycle 208 (v208 → v209), lens 8 expression (Rimsky ch. IV, third pass)
- Accepted: 35 trombones (and the Cbsn with them) re-enter ff falling to f on beat 4 (tied, no new attack), after 28 bars' rest (Rimsky PDF 136, 129; as c108 at 199). 35 Vln I·II grace-note glide E♭-F-G into F1's head A♭5 (Rimsky PDF 129-130, Ex. 254); F1's notes and rhythm unchanged; 37 left plain (octaves with the bass).
- Kept: Hn 2 mf at 130, trumpets mf at 159 (protected); trombones f at 247 (c184 balance).
- Note for finale.md: F1 at 35 has a violin grace glide.
- Do-not-touch: 130-132; 159-166; 247-254 trombone dynamics.

## Cycle 209 (v209 → v210), lens 9 master comparison (Brahms 1/iv, third pass)
- Accepted: 119 and 122 Vln I pp answers divided, two solo desks on top and the section an octave lower, "unis." at 129 (Rimsky PDF 58-59, 200, 202-203). 35 Fl 1 takes the violins' grace glide too, Fl 2 matching graces (Rimsky Ex. 2, 3, 8).
- Regression check against v199: nothing worse.
- Note for finale.md: 35 grace glide in Vln I·II and Fl 1.
- Do-not-touch: bars 1-2; 51-66; 115-118 and the bassoon solo; 216-223 with 222→223; 223-234; both chorale top lines and the cut at 264.1; 259-263; 273-279.

## Cycle 210 (v210 → v211), lens 10 cyclic review (A&S Unit 32, third pass)
- Accepted: 194 Cl 1 F♭4 → E♭4 (V7♭9 of A♭), the movement's first F♭, resolving to E♭ (A&S PDF 597-601, 603), echoing movement II's F♭4 → E♭4 at 80-81.
- Composer: coherence/finale.md rewritten for v211 (header, "Changes in cycles 201-210", scherzo facts, item 3 per the movement I thread: I 138's spacing differs from 222).
- Checks: link from the scherzo, stop chord only at 222→223, E♭/E♮ thread, C7 only at 223, cymbals/bass drum plan, tremolo from 223; records 36/36, scherzo 41/41, movement I 35/35.
- Do-not-touch: bars 1-2; 51-66; 187-198 strings and bassoons; 216-223 with 222→223; 223-234; both chorale top lines and the cut at 264.1; 259-263; 273-279.

## Cycle 211 (v211 → v212), lens 1 melody (Adler ch. 3, third pass)
- Accepted: 123-124 cellos "sul D" on F2's development entry, so the line avoids the open A3 and the hand-over Vc → Vla → Cl 1 → Vln I starts on the warmest colour (Adler PDF 73-74, 99). No note changed.
- Rejected: Vln II sul D at 67-76 (c094/c098/c121 balance); sul G on F1 at 11-16 (protected, string crossing to A♭5).
- Do-not-touch: 123-130 hand-over order and notes; 11-18; 67-82 balance.

## Cycle 212 (v212 → v213), lens 2 harmony (A&S Unit 17, third pass)
- Accepted: 36-37 ascending 5-6 link (Fl 2, Ob 1, Tbn 1 E♭→F on 36.4, ii6 of E♭, tied into 37 as the fifth of B♭ minor), removing octaves with the bass (Ob 2, Cl 1, Hn 4) and fifths into 38 (Hn 2 C4 at 38.1) (A&S PDF 265-266, 273-275). 111-112 Cl 1 holds D♭5 into 112 and falls to C5 with Ob 2 and Tpt 2 (no octaves with the falling-third bass; PDF 267, 276-277).
- Kept: two-statement sequence 99-106; Hn 1 at 196-197 (protected area).
- Tool: tools/critic-scripts/c212/par8.py checks every part against the bass (the analyser checks outer voices only).
- Do-not-touch: F1 at 11-18 and 35-38; 6/3 bridge 83-90; lament bass 107-110; 216-223 with 222→223; both chorale top lines; 259-263; 273-279.

## Cycle 213 (v213 → v214), lens 3 form (Rimsky ch. IV, third pass)
- Accepted: 108-109 Ob 1 and Cl 1 double Vln II's suspension line G5-F5-E5, p <, so the winds enter before the brass's ff at 110 (Rimsky PDF 127, 130; Dvořák 9/iv 8-10); lament bass and strings unchanged (answers c187's protection: only a doubling added). 89 Hn 1-4 enter p < (was Hn 3·4 mf <) after 46 bars' rest (Rimsky PDF 136).
- Kept: 5-6 repeating 1-2; low brass in 199-234 (protected).
- Do-not-touch: lament bass 107-110; 6/3 bridge 83-90 harmony; bars 1-6; 199-234.

## Cycle 214 (v214 → v215), lens 4 orchestration (Adler ch. 15, third pass)
- Accepted: 170 violas start their pp sul tasto figure on the dominant two beats before L, so the cor anglais and muted trumpet enter fresh at 171 (Adler PDF 156-157, Weber Ex. XV-7). 153, 161, 164 bass trombone without the octave leap G2-G3 (g,4 g,4 f,4 d,4; 164 g,2 es,4 d,4) (Adler PDF 150).
- Kept: 265-268 rests (c036, c046, c124; protected).
- Note for finale.md: violas enter at 170.3; bass trombone lower octave at 153, 161, 164.
- Do-not-touch: 167-170 diminuendo order; 151-158 layout; 265-272.

## Cycle 215 (v215 → v216), lens 5 engraving (Gould ch. 1-2 spacing, third pass)
- Accepted: score-only \cen spacing for bar-length notes at 96, 97, 136-138, 147, 221 (Gould PDF 55); crossed held notes split into stemmed tied halves (Hn 1·2 at 256; Fl 2 and Ob 2 at 199-202) (PDF 67); trombone staff kept apart 103-105 (no mid-bar "1."); f at 200 (Hn 3·4) offset; "sul tasto" at 170 centred.
- Also (composer, following movement I v239 cycle 238): portato dash on the P head's repeated note under the slur, c4--), at 200 (Fl 1, Ob 1, Cl 1, Vln I·II, Vla) and at 248 (Vln I·II, Fl 1·2, Bn 1, Vc, Tbn 1·2). Notes, rhythms, slurs unchanged.
- Do-not-touch: 222→223 and 223-234; both chorale top lines and the cut at 264.1; 259-263; 273-279; separate-stem crossings from c035, c185, c205.

## Cycle 216 (v216 → v217), lens 6 playability (Adler ch. 6-7, third pass)
- Accepted: 209-210 upper woodwinds fp < (was f <) on the A♭7 into 211 (Adler PDF 177-178); clarinet pp pads "dal niente" at 51 and 171 (PDF 211; level and scoring unchanged, answering the 51-66/171-186 protection); breaths: Bn 2 at 198.4, Bn 1-2 at 82, Cl 1 at 242, Cl 2 at 186 (PDF 175, 188, 226).
- Kept: Bn 2 B♭1 p at 191; Ob 1 E6-D6 at 227-228; Cbsn quarters 199-203.
- Tool: tools/critic-scripts/c216/breath.py (breathing-gap scan).
- Do-not-touch: 216-223 with 222→223; 223-234; both chorale top lines and the cut at 264.1; 259-263; 273-279.

## Cycle 217 (v217 → v218), lens 7 texture (Adler ch. 15 polyphony, third pass)
- Accepted: 187-194 Bn 1 doubles the cellos' counter-melody at pitch, p, breath after 190 (Adler PDF 176, 178-179); Bn 2 and all string notes unchanged. 27-34 Cl 1·2 a2 double the violins' countersubject at pitch, f, mf at 35 (Adler PDF 172, 178); their old held notes duplicated the horns. global.ily breaks kept 16 pages (Vln II "unis." label part-only at 27).
- Note for finale.md: Cl a2 with the countersubject 27-34; Bn 1 with the cello counter-melody 187-194.
- Do-not-touch: 223-234 with 222→223; 247-254; both chorale top lines and the cut at 264.1; 259-263; 273-279.

## Cycle 218 (v218 → v219), lens 8 expression (Adler ch. 2 bowing, third pass)
- Accepted (bow signs only): 199-204 movement I's bowing of I 27-32 (down-bow pickup, hooked up-bow at 200, down-bows at 204; violas' up-bow below the note) (Adler PDF 38, 42-43; answers c175 by c186 and movement I's own marks); 90-94 down-bows on every accented quarter (PDF 42-43; c167/c168 layout unchanged); 167 up-bow in Vc/Cb so the B ends at the frog before the pizz. at 171 (PDF 54); 9-10 crescendo starts up-bow so the f accent at 10.3 is down-bow (PDF 38).
- Note for finale.md: 199-204 carries movement I's string bowing.
- Do-not-touch: 223-234 with 222→223; 247-254 with c186 bowing; both chorale top lines and the cut at 264.1; 259-263; 273-279.

## Cycle 219 (v219 → v220), lens 9 master comparison (Tchaikovsky 5/iv, third pass)
- Accepted: 272 cellos hold C3 and Bn 2 holds A3 through the IV6/4, filling the C2-F4 gap (Rimsky PDF 85-86; no horn or trombone rest filled, answering the 265-272 protection); 91-92 beat 3 Ob 1 D6 / Ob 2 B♭5, no second in the oboe pair (PDF 90, 96; c167/c168 layout kept); 208 Ob 2 c''2 r2, no minor second under Ob 1 and a breath before 209 (PDF 90, 102).
- Kept: leading-tone doublings in the brass at 141-142, 160, 222 (protected).
- Regression check against v209: nothing worse.
- Do-not-touch: 141-142; 160; 216-223 with 222→223; 223-234; both chorale top lines and the cut at 264.1; 259-263; 265-272 horn and trombone rests; 273-279.

## Cycle 220 (v220 → v221), lens 10 cyclic review (A&S Unit 26, third pass)
- No score change (v221 = v220's music).
- Composer: coherence/finale.md updated for v221 (header versions: movement I v241, movement II v233, scherzo.md v220; "Changes in cycles 211-220"; 27-34, 170, 209, 272, 204 sentences; open request to the scherzo rewritten).
- Checks: records 36/36, movement I 35/35, scherzo 41/41; I 27-32 part by part = 199-204; theme B unchanged; cyclic rules hold.
- Kept: E major at 243 as a chord only (tonicizing it needs D♯→E reserved for 219-220, and bars in the protected 235-247 plan).
- Do-not-touch: bars 1-2; 143-145; 199-204; 216-223 with 222→223; 223-234; 235-247 plan; both chorale top lines and the cut at 264.1; 259-263; 265-272 horn and trombone rests; 273-279.

## Cycle 221 (v221 → v222), lens 1 melody (Adler ch. 7, third pass)
- Accepted: 95-98 Ob 1 alone, "solo, espress.", mf > p, on the motto tail E♭5-D5-D♭5-C5; Vln I rests 95-102 (Adler PDF 184, 198-199). The oboe's first solo line in the movement; pitches, harmony and the violas' E♭4→E4 at 97 unchanged.
- Rejected: two low clarinets in unison at 95-98 (would hide the violas' E4).
- Kept: cor anglais register at 171-186 and 217-220; oboe low fifth at 102 and 270-271 (loud doublings, c131).
- Note for finale.md: 95-98 oboe solo, Vln I rests 95-102.
- Do-not-touch: 95-98 violas; 171-186; 217-220.

## Cycle 222 (v222 → v223), lens 2 harmony (A&S Units 22-23, third pass)
- Accepted: 30 V4/2 over F becomes VII°4/3 (B-D-F-A♭) resolving to i6 (A&S PDF 375, 383, Ex. 22-1); Fl 1 and Ob 2 G-A♭-G across 29-31 (PDF 381); Hn 1 F4→E♭4 on 30.3 (removes the d5→P5 of PDF 375, Ex. 22-3c). The dim7 already resolves to C minor at 22, 162, 169-171, so the stop-chord rule is not affected.
- Kept: 222→223 D-bass stop chord to I (movement I 138's harmony; protected); no ♭VI in the C-major coda (protected; would anticipate 259-261).
- Do-not-touch: 216-223 with 222→223; 223-234; 235-247; both chorale top lines and the cut at 264.1; 259-263; 273-279; F1's bass statement and countersubject 27-34.

## Cycle 223 (v223 → v224), lens 3 form (A&S Units 16 and 19, third pass)
- Accepted: 38 beats 3-4 cadential 6/4 B♭-E♭-G♭ → B♭-D-F before the half cadence on V of E♭ at 39 (A&S PDF 259, 306-307, 314, 316-317); seven accompaniment parts (Hn 1, Bn 1, Hn 3, Tbn 1, Cl 1, Vla, Vc); F1 melody, Fl 1 A♭5 39-42 and dynamics unchanged.
- Kept: coda proportions and stage tempi (c043/c063); repeated neighbouring IV6/4 over the tonic pedal (263-279 protected); 189.1 passing 6/4.
- Do-not-touch: 39-42 Fl 1 A♭5; 135-171; 263-279.

## Cycle 224 (v224 → v225), lens 4 orchestration (Adler ch. 15, third pass)
- Accepted: 187-194 Ob 1 doubles Vln I's F2 at pitch, p dolce, breath after 190, rest 195-196 (Adler PDF 178-179); 187-198 now has its own colour against 67-82 (strings + harp). 95-96 the held chord under the oboe solo starts mp > (Cl 1·2, Bn 2, Vln II, Vla, Vc, Cb) (PDF 159, 184); violas' pitches and E♭4→E4 unchanged.
- Kept: 205-206 F1 head in four horns (protected, rescored three times). Note: 187-194 now has clarinet background (c207), Bn 1 counter-melody (c217) and Ob 1 tune doubling; no further thickening there.
- Note for finale.md: Ob 1 with Vln I 187-194; mp at 95.
- Do-not-touch: 187-198 scoring as of v225; 205-210; violas 95-98.

## Cycle 225 (v225 → v226), lens 5 engraving (MOLA, third pass)
- Accepted (engraving and part-only; MIDI identical): rehearsal letters K, N, O above their tempo text (MOLA PDF 4); 243-246 "poco a poco stringendo" on two lines and violins' "unis." above the slur (PDF 8); 197-198 Ob 2 score rests as spacers; harp part cue (Vln I) at 39-42 before the harmonics at 43 and trombone parts cue (Vc) at 33-34 before 35 (PDF 5).
- Not applied: 129 Vln I "unis." above the staff (17 pages).
- Do-not-touch: 16-page layout and score-only breaks; 216-223 with 222→223; 223-234; both chorale top lines and the cut at 264.1; 259-263; 273-279; 187-198 scoring.

## Cycle 226 (v226 → v227), lens 6 playability (Adler ch. 9-10 brass, third pass)
- Accepted: 149 horns, Tpt 3, trombones and tuba re-attack sfp < ff at 150 under the allargando (Adler PDF 290, 323, adler2 PDF 8; notes, voicing and Tpt 1-2 strokes unchanged); Tpt 3 rests 251-254 with Tpt 1-2 (endurance, PDF 292); breaths Hn 3-4 after 242, Hn 4 after 246 (PDF 292, 309); trumpet parts without key signatures (PDF 297-298; parts only).
- Kept: 224-228 chorale holds; muted Tpt 1 B3 at 185.
- Do-not-touch: 147-150 notes and voicing; 223-234; 255-263; 273-279.

## Cycle 227 (v227 → v228), lens 7 texture (Adler ch. 17, third pass)
- Accepted: 212 and 214 Hn 3·4 and Bn 1 move in the theme's held dotted halves (212 A♭4-G♭4-F4-E♭4 into D♭4, Bn 1 an octave below; 214 A♭3-B♭3-C4 in Hn 3 and Bn 1, Hn 4 G♭3), f (Adler PDF 259-260, 274); theme B and its doublings, the 211 suspension and Hn 3·4's rest at 215-218 unchanged (answers c151, c155, c157, c171, c198). 95-98 Cl 1 rests under the oboe solo (PDF 267, 274); chord still complete.
- Note for finale.md: tenor answers under theme B at 212 and 214; Cl 1 rests 95-98.
- Do-not-touch: theme B line and doublings 211-218 with 210-211; 216-223 with 222→223; 223-234; both chorale top lines and the cut at 264.1; 259-263; 273-279; violas and oboe 95-98.

## Cycle 228 (v228 → v229), lens 8 expression (Adler ch. 11 and 15, third pass)
- Accepted: 43-50 the held A♭3 passes from Bn 1 (tied 43-47.2) to Cl 2 (pp, 47-50), overlapping, instead of Bn 1 re-attacking at 47 and 49 (Adler PDF 190-192, Ex. XV-37).
- Kept: break-offs 94→95 and 113→114 (PDF 38); timpani f at 110 (c056); sforzandi at 101, 105, 138.
- Note for finale.md: 43-50 A♭3 Bn 1 → Cl 2.
- Do-not-touch: 1-2; violas 46-49 and harp harmonics 43-47; 95-98; 216-223 with 222→223; 223-234; both chorale top lines and the cut at 264.1; 259-263; 273-279.

## Cycle 229 (v229 → v230), lens 9 master comparison (Dvořák 9/iv, third pass)
- Accepted: 95-98 the held chord under the oboe solo moves from Cl 2 to the horns (Hn 3 G4-E♭4-E4, Hn 4 B♭3, p > pp); clarinets rest 95-98 (Rimsky PDF 116, Ex. 136 PDF 312). Pitches unchanged; break-off at 94.3, oboe and violas untouched.
- Kept: no soft brass restatement in the coda (219-222 does that job; protected).
- Regression check against v219: nothing worse.
- Do-not-touch: 95-98 scoring as of v230 (changed in c203, c221, c224, c227, c229; settled); 197-279 protected items.

## Cycle 230 (v230 → v231), lens 10 cyclic review (Casanelles ch. 5, third pass)
- Accepted: 95-98 Hn 3 holds G4 (c229's G4-E♭4-E4 took the reserved D♯4→E4 step of 219-220 early; Casanelles PDF 227, 235); the violas carry E♭4→E4 alone; c229's horn scoring kept. 9 timpani g,4 g,8 g,8 g,4: the scherzo's closing motive x taken up in the finale's first dominant preparation (PDF 200, 211-212, 216-217, 239); record line added in themes-finale-quotes.ly; scherzo thread told.
- Composer: coherence/finale.md updated for v231 ("Changes in cycles 221-230", header versions, 95-98, item 13, open request).
- Do-not-touch: bars 1-2; 7-10 timpani; 95-98; 216-223 with 222→223; 223-234; both chorale top lines; 259-263; 273-279.

## Cycle 231 (v231 → v232), lens 1 melody (Sebesky ch. 6-7, third pass)
- Lens 1 melody, Sebesky ch. 6-7 (PDF 204-230, third pass).
- Accepted: 66 Cl 2 G♭3→G3 pp under the trumpet's last note, a chromatic inner line into the E♭-major F2 at 67, handing its G3 to the violas/cellos (Sebesky PDF 207, 216, 222-223).
- Kept: the static pad top line at 51-66, the codetta 91-94, no F2 return in the coda.

## Cycle 232 (v232 → v233), lens 2 harmony (A&S Units 24-25, third pass)
- Lens 2 harmony, A&S Units 24-25 (PDF 398-441, third pass).
- Accepted: 80 beats 1-2 V6/5 of V (A♮-C-E♭-F) between IV and V, bass A♭-A♮-B♭ (A&S PDF 428 Ex. 25-12a); 70 beats 3-4 V4/3 of ii for I6, so 70-73 falls by fifths C7-Fm7-B♭7-E♭ and the tune's B♭ resolves as a 7th (PDF 399-400, 424, 433). F2's tune, rhythm, scoring and dynamics unchanged.
- Kept: the 187-198 A♭ recapitulation of F2 (protected).
- Note for finale.md: F2 at 67-82 now has two applied chords (70, 80).

## Cycle 233 (v233 → v234), lens 3 form (A&S Unit 18, third pass)
- Lens 3 form, A&S Unit 18 (6/3 chords, PDF 289-303, third pass).
- Accepted: 121 beat 2 passing pizz. F in cellos and basses (i4/2), so the bass to the G-minor Phrygian half cadence runs G-F-E♭-D stepwise (A&S PDF 298-299 Ex. 18-12); 88 accents removed inside the 6/3 series (Vln I, Vln II, Fl 1; PDF 291-292 Ex. 18-3).
- Kept: 239-242 in root position, 57-58 and 177-178 unchanged (protected solos), coda proportions.

## Cycle 234 (v234 → v235), lens 4 orchestration (Adler ch. 8, third pass)
- Lens 4 orchestration, Adler ch. 8 (adler1 PDF 233-281, third pass).
- Accepted: 101-102 and 105-106 bass clarinet doubles Bn 1 an octave below (E2, A2, p) under the string-free wind answers (Adler 257 Ex. VIII-25, 252-253, 260); 105 Cl 1 an octave lower, so the third statement of the scale figure spans Fl F6, Ob F5, Cl F4 (Adler 255, 250-251, 237).
- Rejected: winds sustaining the 7-6 chain at 87-90 (protected); pad change at 82-83 (protected). Kept: 131 close chord.
- Note: intro.ily comment corrected to the scherzo's closing timpani dynamics (pp, pp, ppp near the rim; scherzo v241).

## Cycle 235 (v235 → v236), lens 5 engraving (Adler ch. 18, third pass)
- Lens 5 engraving, Adler ch. 18 and App. A (adler2 PDF 291-312, third pass).
- Accepted: score-only padding overrides (c185/c225) tagged score, so rehearsal letters N, O, R sit at their barlines in the parts (Adler 299, 301); tempo marks over the timpani/percussion group and barlines joined through it (Adler 293-294); timpani label "4 timpani: G, A♭, C, E♭" (Adler 292); parts-only padding so "animando" (81) no longer touches "Tempo I" (83). No MIDI change; parts page counts unchanged.
- Kept: trumpet/trombone staff layout 1·2 + 3; Vln I C7 at 223 with ledger lines (cycles 5, 115).
- Note: the finale's percussion barlines now join, unlike movement I's (its drum staff carries text across barlines).

## Cycle 236 (v236 → v237), lens 6 timpani (Adler ch. 12, third pass)
- Lens 6 (timpani and percussion), Adler ch. 12 (PDF 79-81, third pass).
- Accepted: the C drum retuned to D♭ (muta at 206) so the timpani strike the D♭ tonic ff at 211 and f at 212 when the A♭ pedal resolves, then "muta D♭ in C" with medium sticks at 215 (Adler PDF 79-81, Ex. XII-51); "near the rim" on the pp C roll at 235-238, "ord." at 243 (Adler PDF 80).
- Rejected: bass-drum roll at 138-142 (unpitched percussion held back to 223), soft cymbal stroke (first cymbals reserved for 223), timpani doubling pizz. bass (protected solos).
- Note for finale.md: done (one retuning in the movement since v237).

## Cycle 237 (v237 → v238), lens 7 texture (Adler ch. 16, third pass)
- Lens 7 (texture and dynamics in orchestration), Adler ch. 16 (adler2 PDF 197-255, third pass).
- Accepted: 39-42 diminuendo scored by drop-outs: Hn 3·4, Ob 1 and B.tbn stop after 40, Ob 2, Cl 1·2 and Hn 1 after 41, so the violins' F4 is no longer covered at the unison and 42 already has the transition's group (Adler PDF 201, 202, 212-213, 224, 229). No pitch changed.
- Kept: 83-86, 19-26, 255-262, 265-272.
- Note for finale.md: 39-42 diminuendo scored by drop-outs; Hn 3·4 rest 41-88.

## Cycle 238 (v238 → v239), lens 8 dynamics (Casanelles ch. 4, 6, third pass)
- Lens 8 (dynamics and phrasing), Casanelles ch. 4 and 6 (PDF 145-161, 290-291, third pass).
- Accepted: 239-240 swells as in movement I's phrase and as at 235-238; 243 strings and bassoons drop to mf under the horn call, then mf < to 247; Fl 2 enters mf at 242, harp diminuendo at 242, Ob 1 f on its G♯ at 243 (Casanelles PDF 149-150, 152, 155, 290). No note changed.
- Kept: wind canon 226-230 unslurred, brass diminuendo 231-234, repeated-note figures at 247-277, 255-262, 11-26.

## Cycle 239 (v239 → v240), lens 9 holistic (Beethoven 5 finale, third pass)
- Lens 9 holistic comparison with Beethoven 5's finale; Rimsky-Korsakov examples 201-274 (PDF 364-440, third pass); compared with v229.
- Accepted: 70 violas end on G (es'4( f'4 g'2)) again, so the violas' E♭/E♮ thread keeps its first E♮ at 97; cellos keep E♮ for the V4/3 of ii (c232); 103-104 the held F moves from Hn 1·2 F4 (same register as the Hn 3·4 theme) to Cl 1 F5 p, Hn 1·2 rest and return p at 105, Cb D♭ at 104 held full length (Rimsky PDF 132-133, 115-116); 75 Hn 1·2 re-enter pp (Rimsky PDF 136).
- Kept: coda tempo and the broad ending (protected); motive x against its augmentation at 143-145 (exact quotation, protected); pads at 101-102, 105-106.
- Note for finale.md: done (viola thread wording; cellos' E♮ at 70).

## Cycle 240 (v240 → v241), lens 10 cyclic review (Adler ch. 1, 15, third pass)
- Lens 10 cyclic review, Adler ch. 1 and ch. 15 (adler1 PDF 19-23, adler2 PDF 187-196), third pass; read the mount's coherence files (movement I v261, movement II v259, scherzo v241).
- Accepted: 138 Tpt 1 B4 and Tpt 2 F4 one sf eighth over the strings' stop chord, movement I's trumpet layout at I 26/138 (Adler PDF 189-190, Ex. XV-35); B4 cut off, B→C still only at 222→223; part-only Vln I cue at 136-137; \noPageBreak before 128 keeps 16 pages.
- Rejected: timpani stroke at 138; heterophonic doubling (only fits protected quotations).
- Note for finale.md: done (header, record 37/37, timpani label and retuning, cycles 231-240 list).

## Cycle 241 (v241 → v242), lens 1 melody (A&S Unit 21, third pass)
- Lens 1 melody, A&S Unit 21 (suspensions, PDF 346-371, third pass).
- Accepted: 80-81 the E♭-major F2's cadence delays 2̂ over V7: Vln I, Vln II, Fl 1 tie G from 80 beat 4 into 81, resolving to F on beat 2 (A&S PDF 353-354 Ex. 21-15e/f, 348, 352); the trumpet's minor cadence at 64-65 and Ob 1 unchanged.
- Rejected: anticipation at 25/165, 9-8 at 17-18, bass 5/2 at 68/76, shifted counterpoint against the chorale (protected), rising 4-3 sequence.
- Note for finale.md: done (F2 line).

## Cycle 242 (v242 → v243), lens 2 harmony (A&S Units 28-29, third pass)
- Lens 2 harmony, A&S Units 28-29 (augmented sixths, PDF 482-529, third pass).
- Accepted: 167-170 VI → French sixth A♭-C-D-F♯ (168) → V7♭9 over G (169) → V6/5 (170) → i (171), so the bass runs A♭-A♭-G-B-C and the root G sounds before the recap's Phrygian cadence at 177; the movement's first French sixth (A&S PDF 503-507, 512-515). Dynamics and diminuendo order unchanged.
- Rejected: inner fifths 1-6 (protected, c002), augmented sixths at 243, 245-246, 38, 57/177, 147-150 and in the coda (protected or clashing).

## Cycle 243 (v243 → v244), lens 3 form (Adler ch. 15, 17, third pass)
- Lens 3 form, Adler ch. 15 and 17 (PDF 187-196, 256-290, third pass).
- Accepted: 231-234 Vln I rests after the canon's C6 at 230 and re-enters with the pickup G4 mf at 234.4, so movement I's S head at 235 comes in on a rested colour (Adler PDF 263-264, 267-269); Fl 2 joins Fl 1 a2 on the top line; harp cue now quotes Vln II.
- Kept: coda stage pacing, the break-offs at 94-95 and 113-114, F2's six statements, 115-122.

## Cycle 244 (v244 → v245), lens 4 orchestration (Adler ch. 11, third pass)
- Lens 4 orchestration (brass), Adler ch. 11 (adler2 PDF 14-18, 37-54, third pass).
- Accepted: 224-228 Tbn 2 doubles Tbn 1 on the chorale's motto line G-E-D-C-D♭-C a2, as in Adler's Tchaikovsky 4/i model (Ex. XI-21, PDF 38-41) and movement I's chorale (two trombones); Tbn 2's old notes are held by Hn 3·4. Top line, bass, canon and dynamics unchanged.
- Kept: trumpets at 263 (protected unison B→C), bar 1 F♯ in Hn 4, tuba with bass trombone at 91-94.

## Cycle 245 (v245 → v246), lens 5 engraving (Gould, third pass)
- Lens 5 engraving, Gould (Behind Bars) PDF 9-68, third pass.
- Accepted: Metronome_mark_engraver moved from the percussion group to the Timpani staff, so tempo words at 81, 83 and 197 no longer print a second time inside the flute staff when the drum staves are hidden (Gould PDF 41, 43, 55-57; regression from cycle 235); gould-mid-stems engraver: unbeamed middle-line stems follow the neighbouring stems (Gould PDF 27-28, 61); margins top 4 mm, bottom 5 mm to keep page 2. MIDI byte-identical.
- Deferred: whole-note centring at 219 after the key change (override given in c245.md; page 12 full).

## Cycle 246 (v246 → v247), lens 6 playability (Adler App. A, third pass)
- Lens 6 playability and ranges, Adler App. A (adler2 PDF 302-312, third pass).
- Accepted: double-bass C extension (Adler PDF 302; adler1 PDF 108): 171-186 the recap's pizz. bass keeps its 16-foot octave (E♭1 at 174.3, 179, 181, 183; D1 at 175) instead of folding up to the cellos; 166 accented E♭1 with tuba and contrabassoon; header "(double basses: C extension at 166 and 174-183)". The analysis flags these 6 notes below E1: accepted, like the trumpet C6.
- Kept: 241-243 basses with the cellos; no bass C1 at 223, 263, 278 (contrabassoon has it).

## Cycle 247 (v247 → v248), lens 7 winds and brass (Rimsky ch. III, third pass)
- Lens 7 (wind and brass combination), Rimsky-Korsakov ch. III (PDF 106-114, examples 151-167, 174), third pass.
- Accepted: 49-50 Hn 1 D4 stopped, p, in the soft oboe-horn-clarinet chord before the trumpet solo (Rimsky PDF 107, 110 Ex. 164; adler1 PDF 308); 239-242 inner pad revoiced, horns hold the concords and bassoons take the moving notes below them (Hn 3 C4-C4-D4-D4, Hn 4 C4-A3-A3-A3, Bn 1 E3-F3-F3, F3→C4 at 242 resolving to B3 at 243; Rimsky PDF 108); c182's horn unison C4 at 239 kept. Tune, counter-melody, bass, harp and dynamics unchanged.
- Kept: 101-102, 105-106 horn neighbour chord over the held bassoon.

## Cycle 248 (v248 → v249), lens 8 rhythm (A&S Unit 3, third pass)
- Lens 8 rhythm and metre, A&S Unit 3 (PDF 47-57, third pass).
- Accepted: 93 the ff codetta's I chord enters on beat 2 as an accented half held across the half-bar, V on beat 4 as an upbeat, in all 26 parts (timpani r4 es2-> r4); 94.1 restores the metre (A&S PDF 51-52 Ex. 3-6 to 3-8; Eroica i). Replaces c219's down-bows at 93 only. 80-81 the diminuendo starts on the resolution F, not on the suspension's preparation (A&S PDF 53-55).
- Rejected: hemiola (needs triple metre), sf at 111 (protected), F2 bowings, 132.

## Cycle 249 (v249 → v250), lens 9 holistic (Dvořák 7 finale, third pass)
- Lens 9 holistic comparison with Dvořák 7's finale; Rimsky-Korsakov Ex. 261-312 (PDF 428-503, text PDF 130-170), third pass; compared with v239: nothing got worse.
- Accepted: 277-278 harp glissando lengthened to a half note from G3 on beat 3 to G6, f < ff into 278 (Rimsky PDF 134, Ex. 275 PDF 441-442); top note, pedals and landing chord unchanged.
- Kept: Tpt 3 f at 247, Bn a2 at 67-76 (protected), timpani roll with Cb pedal at 235-238.

## Cycle 250 (v250 → v251), lens 10 cyclic review (Rimsky preface, ch. IV, third pass)
- Lens 10 cyclic review, Rimsky-Korsakov preface and ch. IV (PDF 13-23, 125-129, Ex. 237-238), third pass; read the mount's coherence files (movement I v281, movement II v274, scherzo v251).
- Accepted: 239 Cl 1 and violas f (movement I's chromatic counter), harp left hand mf, so the counter is detached from the harp's broken chords (Rimsky PDF 18-20). Manager: "arco" at bar 1 in cellos and basses (scherzo v261 request; Adler part 1 PDF 54); record line choraleFirst TbnTwo 224 (38/38).
- Rejected: muted-brass echo and a scale handed across the orchestra (protected bars).
- Note for finale.md: done (header, versions, cycles 241-250 list, link Ob 1 95-98 = movement II's last tail).

## Cycle 251 (v251 → v252), lens 2 brass (Adler ch. 11, third pass)
- Lens 2 (brass), Adler ch. 11 (adler2 PDF 19-36, third pass).
- Accepted: 27-32 new tuba part doubling the contrabassoon's bass statement of F1, ff, tongued (tenuto/staccato, no slur), resting from 33 (Adler PDF 20, 28, 33-34 Ex. XI-16); the tuba's first thematic line; score-only staff distances on page 2 keep 16 pages.
- Not applicable: the Lohengrin diminuendo (231-234 protected).
- Note for finale.md: the tuba doubles F1's bass statement at 27-32.

## Cycle 252 (v252 → v253), lens 2 harmony (A&S Units 30-31, third pass)
- Lens 2 harmony, A&S Units 30-31 (PDF 530-583, third pass).
- Accepted: 92.1 common-tone diminished seventh E♭-F♯-A-C over the E♭ bass resolving to I, so the two ff codetta bars 91-92 are no longer identical; top line G-G-A♭ | F♯-G-A♭ (A&S PDF 543-545, Ex. 30-19 to 30-21). Rhythm, bowings, dynamics unchanged; no E♮ added.
- Rejected: augmented triad in major at 77, 212, 197, 209-210, 81.4, 250, 271 (protections, the reserved E♭→E♮ step, clashes); V7♯5 at 72 and 93.4.

## Cycle 253 (v253 → v254), lens 3 form (A&S Units 6-8, third pass)
- Lens 3 form and phrase, A&S Units 6-8 (PDF 92-133, third pass). No change to the score.
- Rejected: 72 V6/5 in place of root V7 (bass D): the violas' and cellos' counter-line has D4 on 72 beats 1-2, so the leading tone would be doubled with the bass (A&S PDF 122 on V6/5 voicing); c232's falling-fifth chain C7-Fm7-B♭7-E♭ is kept. Also not applied: 56-57 and 128-129 (protected), 192-193 (protected).
- Kept: proportions (exposition 35%, development and retransition 18%, recapitulation 16%, coda 31%) and the coda stages; 76-77.

## Cycle 254 (v254 → v255), lens 4 strings (Adler ch. 5, third pass)
- Lens 4 strings, Adler ch. 5 (adler1 PDF 125-167, third pass).
- Accepted: 83-86 violas' broken-chord eighths mf (were f), since they run through the tune's lower octave and cannot be moved out of its register (Adler PDF 135, 144); 81.2-82 violas diminish with the violins and play mp < into 83; redundant mf at 87 removed. No note changed.
- Rejected: pizz. basses at 67-74 (arco change at 67 is the texture change); cellos on the violins' descent at 39-42 (B♭ pedal; c237).

## Cycle 255 (v255 → v256), lens 5 parts (MOLA, third pass)
- Lens 5 parts, MOLA guidelines (all 16 PDF pages, third pass). Parts only; score PDF and MIDI unchanged.
- Accepted: string page turns moved to rests (Vla, Vc, Cb after 66 and 186; Vln II at 61|62 and after 186), removing the Vln II compression warning (MOLA PDF 7); part-only cues for tuba and bass clarinet at 25-26 and bass clarinet at 99-100 (MOLA PDF 5); padding for colliding tempo texts in Tpt 1 (197/199) and harp (221/223) (MOLA PDF 8); percussion part header "Cymbals, Bass drum (2 players)" with a notation key (MOLA PDF 5-6).
- Kept: harp pedal setting at 43, harp 8va bassa at 67-82 and 239-242, A4 parts.

## Cycle 256 (v256 → v257), lens 6 playability (Rimsky ch. I, third pass)
- Lens 6 playability, Rimsky-Korsakov ch. I (PDF 24-50, third pass).
- Accepted: 277 harp glissando set enharmonically as a C pentatonic chord glissando (B♯ = C, F♭ = E; diagram "--v|-^--"), so no F or B rings against the fff C chord (Rimsky PDF 46-47); 150 beat 4 Bn 2 drops its pickup D3 to breathe after 17 s ff (Rimsky PDF 37, 44); 190 Bn 2 breath with Bn 1 and Hn 1.
- Kept: harp at 123-130 and 239-242, violins sul A C6 at 238, tuba E♭1-D1 at 27-29.

## Cycle 257 (v257 → v258), lens 7 arranging (Sebesky ch. 1, third pass)
- Lens 7 arranging, Sebesky ch. 1 (PDF 11-20, third pass).
- Accepted: 20 F1's consequent no longer repeats the antecedent's harmony: v6 - iv6/5 - iv7 into V7 at 21, so the bass from 19 falls E♭-C-B♭-A♭-F-G and the tune's E♭ becomes a seventh resolving to D (Sebesky PDF 19, Ex. 3/3A); Cl 1 D4-E♭4 to avoid fifths, Hn 4 off-beats G4, F4. F1's tune, bar 12 and bar 160 unchanged.
- Kept: 51-66, 115-130, 217-218, F2's second phrases, the recapitulation 171-198.

## Cycle 258 (v258 → v259), lens 8 expression (Sebesky ch. 1, 6, third pass)
- Lens 8 expression, Sebesky ch. 1 and 6 (PDF 11-20, 204-218, third pass). Marks only; no note, dynamic or tempo word changed.
- Accepted: 211 "cantabile" on movement II's theme B in Tpt 1·2, Fl 1·2, Ob 1, Cl 1 (its echo at 217 is espress.), with the downbeat accent in Ob 2 and Cl 2 (Sebesky Ex. 281, PDF 214-215); "leggiero" on F1's slurred broken-chord accompaniment at 11 and 151 (Cl 1·2) and 19 and 83 (violas) (Sebesky PDF 13-14, Ex. 2A, 279-280).
- Kept: harp mf at 67-82, 223-230 (protected), 235-246.

## Cycle 259 (v259 → v260), lens 9 holistic (Tchaikovsky 4 finale, third pass)
- Lens 9 holistic comparison with Tchaikovsky 4's finale; Adler (adler1 PDF 137-165, 235-281), third pass; compared with v249.
- Accepted: 20.1 Cl 1 holds G4 (was D4), so c257's v6 over B♭ has its root on the downbeat instead of a bare B♭-D third (Adler PDF 152 Ex. V-27, 257 Ex. VIII-25). This was the one thing that got worse since v249.
- Kept: F2's re-scorings, the octave unison 265-268, the coda's form (protected), 135-137 (change comes at 138), the c251 tuba.

## Cycle 260 (v260 → v261), lens 10 cyclic review (Sebesky ch. 9, 1, third pass)
- Lens 10 cyclic review, Sebesky ch. 9 and ch. 1 (PDF 240-242, 11-20), third pass; read the mount's coherence files (movement I v291, movement II v286, scherzo v271, scherzo record 51/51). No change to the score.
- Kept: the harp's F♭ pedal at 277 (sounds E; the only setting that keeps F out of the C chord); the tuba theme at 27-32; the coda's recalls 243-279 (protected).
- Note for finale.md: done (header, cycles 251-260 list, the two links at bars 1-2 that the scherzo and movement I rely on, harp glissando wording).

## Cycle 261 (v261 → v262), lens 1 melody (A&S Unit 3, third pass)
- Lens 1 melody and rhythm, A&S Unit 3 (PDF 47-57, third pass).
- Accepted: F2 anticipates its half-cadence note: 73.4 the violins' F enters a beat early, tied into 74; the same at 193.4→194 in the recapitulation (Vln I, Vln II, Vla, Ob 1, Hn 1) (A&S PDF 51, 56 Ex. 3-19; Beethoven 9/iv 103-104). The first half's cadence now pushes ahead of the beat and the second half's (the 80-81 suspension) holds back. No part, level, register or doubling changed.
- Rejected: counter-accents at 89-90 and 205-210, anticipation at 25/165 (c241), a five-bar F2 half, hemiola.
- Note for finale.md: F2 anticipates F at 73.4 and B♭ at 193.4 (since v262).

## Cycle 262 (v262 → v263), lens 2 harmony (A&S Unit 27, third pass)
- Lens 2 harmony, A&S Unit 27 (ninth chords, PDF 463-481, third pass).
- Accepted: 72-73 the falling-fifth chain ends on a major-ninth dominant whose 9th and 7th resolve together (violas D4-C4-B♭3, cellos A♭3-G3; the 7th no longer rises) (A&S PDF 463-466, 468, 479); 192-193 the same in the A♭ recapitulation, with the basses in root position on E♭2 (the first inversion dated from cycle 12, when the passage was in C), Bn 1 G3-F3-E♭3, cellos D♭3-C3; 22 Cl 1 A♭4 and 162 Tpt 1 F4, Hn 4 G3, so the root G is a minor ninth below the A♭ peak, not a semitone (A&S PDF 469-470 Ex. 27-10).
- Rejected: 9/7 chain at 70-72, applied ninths at 135-137 (protected), a major ninth in the coda (protected).
- Note for finale.md: major-ninth dominant at 72 and 192.

## Cycle 263 (v263 → v264), lens 3 form (A&S Unit 15, third pass)
- Lens 3 form, A&S Unit 15 (III and VII, PDF 230-247, third pass).
- Accepted: 172 and 180 Cl 2 G3 on beats 1-2 (was F3), so the recapitulated F2's downbeats are V6/5 (B-D-F-G) instead of a root-position diminished triad, as at 52 and 60 (A&S PDF 243, 245).
- Kept: 83 (closing theme settled), 198-199 section joint, 223-279 (C pedal, protected). The tonal plan (III at 17-18% as in Dvořák 9/iv) follows the unit.

## Cycle 264 (v264 → v265), lens 4, Casanelles ch. 6
- 43–50: Vln I B♭5 pp sul tasto over the B♭ pedal, so the dominant sounds as one spectrum up to the violins (Casanelles PDF 271–273, Mahler 1/i); "ord., cantabile" at 67. Accepted.
- 151–164: Tbn 1·2 mf (were f) under the clarinets' broken chords and Hn 3·4 off-beats, crescendo on 165 to f at 166 (Casanelles PDF 286–289, Rimsky PDF 51). Accepted; no notes change in the protected range.
- 215–218: Tbn 2 C3–D♭3–D♭3–D♭3 (was A♭2 a minor third above B.tbn F2), C3 at 219 (Rimsky PDF 85). Accepted; doubled D♭s still at 219.
- 200 beat 3 (composer, coherence): Tpt 2 F4 (was G4) following movement I v303's bar 28, vii°4/3 with Tpt 1 B4. Accepted.

## Cycle 265 (v265 → v266), lens 5, Adler ch. 2 bowing notation
- 217: `\textLengthOn` so "change bow at will" (Vln II, Vc, Cb) no longer crosses the 217|218 barline (Adler PDF 39; MOLA PDF 10). Accepted.
- 119 and 122: Vln I octave answers written as two voices, "2 soli" upper and "gli altri" lower, replacing the inconsistent "div." at 122 (Adler PDF 30–32). Accepted; pitches unchanged.
- 92: "sim." replaces the repeated down-bow marks of 91 in all strings (Adler PDF 38, 43–45). Accepted.
- 91: Vln II "non div." on the double stops, as the violas (Adler PDF 30). Accepted.

## Cycle 266 (v266 → v267), lens 6, Sebesky ch. 2 winds
- 269–271: Ob 1 moves up an octave to double the flutes and Vln I instead of unison oboes in the coarse low register (Sebesky PDF 71, 79–80); back to A5 at 272. Accepted; F1's notes unchanged.
- 277: horns play quarters `c''4-> r4 c''4-> r4` / `e'4-> r4 e'4-> r4`, leaving the eighth upbeat to trumpets and trombones (Sebesky PDF 32, 46). Accepted; the protected close's harmony, line, glissando and final chord are unchanged.

## Cycle 267 (v267 → v268), lens 7, Sebesky ch. 3 strings
- 43–50: cellos divide B♭2/F3 under the dominant pedal, filling the seventh gap (Sebesky PDF 139–147); "unis., pizz." at 51. Accepted.
- 83, 87: flutes mf (were f) where they double Vln I on E♭6, as at 35, 78, 129 (Sebesky PDF 164). Accepted.

## Cycle 268 (v268 → v269), lens 8, MOLA dynamics
- 145: violas get f on F1's head, ending their crescendo like every other part (MOLA PDF 8, 10–11). Accepted.
- 141–145: long hairpins across the 143|144 page turn written as "cresc." in Bn, Vla, Vc, Cb, Cbsn, timpani (MOLA PDF 12; Adler2 PDF 10, 201). Accepted.
- 269: Hn 3·4 ff moved from the rest to the beat-2 entry (MOLA Ex. 3; cycle 68 rule). Accepted.

## Cycle 269 (v269 → v270), lens 9, Adler part 2 holistic
- 247–254: timpani f (were ff) under the combined theme heads, the level of Tpt 3's same figure (Adler2 PDF 172–176, 184). Accepted.
- Combining F1 and F2 in the coda: not applied, protected coda and cyclic plan. Agreed.
- Tpt 3 rest 251–254: kept for its fresh entry at 255. Agreed.

## Cycle 270 (v270 → v271), lens 10, cyclic review
- 197.4–198: mixture B♭–D♭–F♭–A♭ over the D♭ bass, F♭3 → E♭3 in violas and Hn 2, movement II's 87–89 line at pitch; cellos A♭3 on that beat (A&S PDF 388, 395, Ex. 23-5, 23-9). Accepted; tune, bass, bowing and dynamics unchanged.
- finale.md: seven stale sentences corrected (header versions, Tpt 2 at 200, Ob 1 at 269, open request version, F♭ wording). Applied.
- Bar 80 cross relation A♮1/A♭5: kept, c232's chromatic bass. Agreed.

## Cycle 271 (v271 → v272), lens 1, A&S Unit 20
- 75: F2's E♭-major violin statement varies its repeat with a five-note turn on beat 3, Vln I `bes''2( c'''16 bes'' aes'' bes'' g''4)`, Vln II an octave lower (A&S PDF 333, 338–339, Ex. 20-21b). Accepted; F2 changes only in this bar.
- Escape tone + accented passing tone idiom (A&S PDF 337): only fits in protected 83–86. Not applied; agreed.

## Cycle 272 (v272 → v273), lens 2, A&S Unit 5
- 75–77: Bn 1 holds B♭3 into 77 and steps to A♭3 instead of leaping a sixth down to double the bass at 76 (A&S PDF 76, 80, 89); Bn 2 keeps the bass. Accepted.
- 9–10 leading-tone doubling, 77–78 inner crossing, 107–109 spacing, 278 final chord, 10.4–11 cello: kept. Agreed.

## Cycle 273 (v273 → v274), lens 3, A&S Unit 14
- 73.3–4: F2's E♭-major half cadence approached by IV – V6/5 of V with the bass rising A♭–A♮–B♭ (A&S PDF 214–215, Ex. 14-2, 14-3d, 14-4); inner voices adjusted so no A♭ sounds against A♮, harp needs no pedal change. Accepted; tune unchanged, 193 protected and left as is.
- 112–113, 57–58, 177–178, 5–6 modulation, PAC in V: checked, no change. Agreed.

## Cycle 274 (v274 → v275), lens 4, Rimsky-Korsakov ch. I and III
- 277: the short ff string chords are double stops "non div." in Vln I, Vln II, violas (Rimsky PDF 87); cellos stay divided. Accepted; MIDI identical.
- 277–278: oboes in thirds/sixths in the middle register (Ob 1 E5–D5–E5 over Ob 2 C5–B4–C5; at 278 Ob 1 C6, Ob 2 E5) instead of low E4 and a fourth (Rimsky PDF 90, 95–96). Accepted; harmony unchanged.
- Cor anglais silent 221–end: kept. Agreed.

## Cycle 275 (v275 → v276), lens 5, Gould ch. 1
- 279: cymbal quarter gets a plain cross, not a circled one (Gould PDF 26). Accepted.
- 278–279: cymbal and bass drum in two voices (stems up/down) as at 223, so the ties no longer stack (Gould PDF 27, 65). Accepted. Note for r07 renders: finalePerc now has two voices at 278–279, so the render temp copy must also simplify finalePerc.

## Cycle 276 (v276 → v277), lens 6, Adler ch. 2
- 43–50: Vln I's held B♭5 is an artificial harmonic (stop B♭3, touch E♭4), sounding pitch printed in parentheses; a hidden voice plays it in the MIDI (Adler PDF 55–62). Accepted.
- Vln II "pizz. div." at 51 and 115, "unis." restored at 67 and 127 (Adler on divisi pizzicato chords). Accepted.

## Cycle 277 (v277 → v278), lens 7, Adler ch. 8
- 35–38: Bn 1 doubles the violas' countersubject instead of the horns' held notes (Adler PDF 255, 257, 267–268, 271). Accepted.
- 35: Hn 3·4 f (were ff), in line with trombones and Hn 1·2 (Adler PDF 268). Accepted.
- 67–69 unison bassoons, 95–98 horn third, imitation passages: no change. Agreed.

## Cycle 278 (v278 → v279), lens 8, Adler ch. 7
- 43–48: Fl 1 (44) and Cl 1 (46) crescendo into the top of the scale figure, Ob 1 diminuendo at 48 into its pp (Adler PDF 185–186, 198, 210, 227). Accepted.
- 236–237: Cl 1 and violas swell on the tied C5 and recede at 237 as the violins climb (Adler PDF 188, 212). Accepted.
- 119–122, 171–178, 95–98, 87–94: no change. Agreed.

## Cycle 279 (v279 → v280), lens 9, Adler part 2 ch. 16 holistic
- 9–10: the opening crescendo built by staggered entries (horns, violas, Cbsn, Cb 9.1; clarinets 9.3; oboes and flutes 10.1) instead of 13 parts entering together (Adler2 PDF 205, 213, 215–216, 224). Accepted; c189's no-re-attack rule and the timpani motive x kept.
- 66–67: Cl 2 G3 tied into 67.1 so the background overlaps the seam (Adler2 PDF 217, 224). Accepted.
- 43–50 horn pulse, 11–26 arpeggios, 65–66 doubling, register swaps: protected, not applied. Agreed.

## Cycle 280 (v280 → v281), lens 10, cyclic review
- Unused Neapolitan techniques (N6–V4/2, Neapolitan 6/4, ♭II pivot, rising sequence) would only fit in protected passages. Not applied; agreed.
- Neapolitan 6/4 at 167.3–4: rejected (second ♭II colour after 163, protected Hn 1 line). Agreed.
- finale.md: twelve stale sentences corrected (header versions, opening crescendo, ♭II at 16/156/32, bass clarinet 101–106, Vln I at 67, 38 checks, viola E4 at 126–127). Applied.
- Movement I's theme record reads 34/35 because lyparse.py misreads `\set Staff.soloText`; fix sent to the movement I thread. Cyclic checks against I v321, II v300 and scherzo v300 clean.

## Cycle 281 (v281 → v282), lens 1, Rimsky-Korsakov ch. II
- 77–81: cellos leave the counter and double F2 an octave below Vln II, so the tune is in three octaves at its f peak (Rimsky PDF 54, 60–62, Ex. 29–30); violas keep the counter, 78 changed to `es'2( g2)` to avoid fifths; cellos rejoin at 82. Accepted; F2's notes unchanged.
- Violins–violas–cellos unison at 27–34, same doubling at 197–198, 19–26 layout: not applied. Agreed.

## Cycle 282 (v282 → v283), lens 2, A&S Units 9-10
- 18 and 158: F1's antecedent half cadence gets a cadential 6/4 (clarinets; at 158 also Tbn 1 tied 4–3 and Tbn 2), which also removes Cl 2's octaves with the bass at 17.4→18.1 and 157.4→158.1 (A&S PDF 152–155, 158–160). Accepted; tune and bass unchanged.
- 220 whole-bar 6/4, 74/194, 243–244, 151: kept. Agreed.

## Cycle 283 (v283 → v284), lens 3, A&S Unit 26
- 113–114 pivot chord: tested, not applied (the unit allows a seam without pivot; it would repeat 121–122's cadence). Agreed.
- 77–78 tonicized vi: tested, not applied (cross relation with the tune). Agreed.
- 186→187, 115–150, key plan: follow the unit. Agreed.

## Cycle 284 (v284 → v285), lens 4, Rimsky-Korsakov ch. III
- 243–246: Cl 1 moves up an octave out of the horns' C4–C5 octave and its throat register, above the horn call (Rimsky PDF 108, 110–111; Adler1 PDF 210). Accepted; the horn call quotation is unchanged.
- 11–26, 42, 169, 219–222, 231–234, 171–186, 110: no change. Agreed.

## Cycle 285 (v285 → v286), lens 5, Gould ch. 1 beams
- Concave groups and groups starting and ending on one note are horizontal via a `gould-concave-damping` callback in score.ly at Staff level (Gould PDF 36, 38); c105's manual overrides still win. Accepted for the score; parts-book.ly does not include it yet (parts are not rebuilt in this series).
- Groups above the first ledger line get Gould's slope at 90, 101, 104, 125, 206, 250, 253, 265, 267 (Gould PDF 35–36). Accepted.
- Cl 1·2 159–164 no longer forced flat against Vln II's sloping beams (revert moved to 159). Accepted.
- Repeated two-pitch figures 171–186, 277: kept. Agreed.

## Cycle 286 (v286 → v287), lens 6, Adler ch. 3
- 124.4–126: violas "sul D" for F2's hand-over, so the A4 at 125 is stopped on the D string, as the cellos' "sul D" at 123 (Adler PDF 73–74, 86–87). Accepted.
- Other open strings in lyrical lines, chords, bass lines, ranges, the harmonic at 43–50: no change. Agreed.

## Cycle 287 (v287 → v288), lens 7, Rimsky-Korsakov ch. II combined groups
- 67–74: Hn 1 pp "dolce" doubles the strings' counter-melody under F2 at the cellos' pitch, one horn so the strings lead (Rimsky PDF 76, 79); G4 at 70.3 avoids doubling the violas' E♮ thread; Hn 2's pp entry at 75 kept. Accepted.
- 247–250 hollow middle, 123–126: no change. Agreed.

## Cycle 288 (v288 → v289), lens 8, Adler ch. 10
- 168–169: Hn 1·2 stopped on the French sixth's A♭4/D4 after the open chord at 167, before the muted trumpet's theme at 171, as at 49–50 (Adler PDF 308, 320). Accepted.
- 133–134: the diminuendo gets both ends: Hn 3·4 f at 133, strings p at 134 before pp at 135 (Adler PDF 305–320; MOLA PDF 8). Accepted.
- Muted horns, echo at 139–140, cuivré, sfp at 209: not applied. Agreed.

## Cycle 289 (v289 → v290), lens 9, holistic (Sibelius 2/iv)
- 213→214: Bn 1 skips to G♭3 on 213.3 (`bes2 ges2)`) to remove parallel 12ths with the tune's F5→E♭5 (A&S PDF 329, Ex. 20-2b). Accepted.
- 70–72/190–192 seventh chain, 139–150 augmented sixth, 12.3/160.3 inner fifths, 135–138: not applied or kept. Agreed.

## Cycle 290 (v290 → v291), lens 10, cyclic review
- 178: timpani play the scherzo's motive x pp near the rim (`g,4 g,8 g,8 g,4 r4`) in the gap between the recapitulated F2's phrases, as Beethoven's Violin Concerto timpani (Adler2 PDF 273); the soft form of the scherzo's last statements. "ord." at 199. Accepted; new record line `%@ motiveXretr Timp 178 4`, record 39/39; scherzo thread told.
- finale.md: stale sentences corrected (header versions, open request, 81 cellos, 167–169 stopped horns, Hn 1 at 67–74, Bn 1 at 213); running list 22–25 added, including the cor anglais duet link with movement I 171–174. Applied.
- Cyclic checks against I v321 (record to v329), II v310, scherzo v311: clean.

## Cycle 291 (v291 → v292), lens 2, Rimsky-Korsakov ch. II wind doubling
- 77–80: Cl 1 doubles the cellos' octave of F2 at pitch and Cl 2 rests, replacing c149's clarinet thirds that now crossed the cellos' tune (Rimsky PDF 67, 69, 76–78). Accepted; F2 unchanged.
- 224–228 bassoon, brass melody 211–218, soft horn melody, parallel thirds, 19–26: no change. Agreed.

## Cycle 292 (v292 → v293), lens 3, A&S Units 11-13
- 128–132: bar 129 no longer cadences V7–I in G four bars early; it is G with B then D in the bass, D held to 131, root position only at 132 (A&S PDF 182, 184, 201–202). Accepted; the protected hand-over tune and dynamics unchanged.
- 129 as vi, 38, 17–18/157–158, 82, 67/75, 249–250: no change. Agreed.

## Cycle 293 (v293 → v294), lens 4, A&S Unit 32
- 198.3–4: violas and cellos C♭4, so the recapitulation's A♭ area turns minor before the C-minor tutti at 199 (A&S PDF 585, 592, 596, 601–602); the violas' C♭4 recalls 47–49 and rises for the first time. Accepted; movement II told.
- Exposition E♭ minor→major, 11–66, motto-tail enlargement 198–223: no change. Agreed.

## Cycle 294 (v294 → v295), lens 5, Rimsky-Korsakov tutti
- 5: timpani roll A♭ ff through the restated German sixth, so the return is scored larger than bar 1 and matches every other held ff tutti (Rimsky PDF 117–118, 368–369, 505–507). Accepted; bar 1's single stroke and the links unchanged.
- Roll at 1, wind trills, soft brass chords, roll at 90, tuba at 91–94, string-free passages: no change. Agreed.

## Cycle 295 (v295 → v296), lens 5, Gould ch. 1 rests
- Rests on shared staves sat half a space off the grid at 13 places (Bn 11, 19, 24; Cl 62, 182, 210, 259, 268; Fl 201, 222, 276); a Staff-level `gould-rest-grid` callback moves them outward to whole spaces (Gould PDF 49, 51). Accepted.
- 210: Fl 1's floating crotchet rest lowered to its G♭6 (Gould PDF 50–51). Accepted.
- Harp 8 bassa, Tbn rests 103–105, ledger counts: kept. Agreed.

## Cycle 296 (v296 → v297), lens 6, Adler harp
- 132: harp plays one solid ff G chord at the cadence, ringing through the V4/2 at 133–134 and damped at 134.3 before the pp (Adler PDF 113–115; Rimsky PDF 46–47). Accepted.
- 73: harp RH E♭4–C5–E♭5–F5 so no A♭ rings into the bass's A♮ (Adler PDF 111). Accepted.
- 82: harp LH `es,2 r2` to match the "étouffez" (Adler PDF 117). Accepted.
- Pedals, harmonics 43–47, bisbigliando, 70.3, 235–242, 277: no change. Agreed.

## Cycle 297 (v297 → v298), lens 7, Adler part 2 ch. 11
- 37–38: the third statement of F1's head goes to Hn 3·4 a2 ff "ben marc." at B♭4 while the violins take the countersubject, instead of a third violin statement over held brass (Adler2 PDF 41, 44–46); supporting rests and a 9–8 suspension at 38.3 remove octaves and fifths. Accepted; F1's notes unchanged.
- 67, 187, 195: "open" marks on horn entries after stopped passages (Adler2 PDF 50–54). Accepted.
- Stretto 139–146, F1 inversion, 211–218, 167–171: no change. Agreed.

## Cycle 298 (v298 → v299), lens 8, A&S Unit 21
- 37–39: dynamics after c297: countersubject (violas, cellos, Bn 1·2) f under the horns' ff head at 37–38; violins ff > and Hn 3·4 f > at 39 (A&S PDF 348, 350, 367–368; Adler2 PDF 44, 201). Accepted; no note changed.
- 81→82: "animando" starts at 82, after c241's suspension resolves at 81, with its MIDI tempo steps (A&S PDF 348, 353–354, 359–360). Accepted.
- 108 bow change, 87–89 7–6 chain and others: not applied. Agreed.

## Cycle 299 (v299 → v300), lens 9, holistic (Elgar 1/iv)
- 37–38: Hn 1·2 rest until 38.3 so c297's horn statement of F1's head is not masked by held horns in its own octave, then G♭4–F4 mf under the 4–3 (Casanelles PDF 272, 277–278). Accepted; the one regression since v289.
- 38.1–2: Tbn 2 C3 (was A♭2) to avoid a minor third over the F2 bass (Casanelles PDF 274; Rimsky PDF 85). Accepted.
- 171–186, bow position, 115–122: kept. Agreed.

## Cycle 300 (v300 → v301), lens 10, cyclic review
- 119–123: the Vln I solo desks' answers had no dynamic of their own, so the MIDI played them at velocity 90 against the printed pp; now in their own voice with a hidden pp (Rimsky PDF 128; Casanelles PDF 272). Accepted; printed page unchanged. The v300 r07 render still has the loud desks.
- finale.md: eight stale sentences contradicted by running-list items 26–33 corrected. Applied.
- Quotations against I v340, II, scherzo (trio change not quoted): 39/39, clean. Brahms-3 cross relation and 94→95 overlap: declined. Agreed.

## Cycle 301 (v301 → v302), lens 1, Adler ch. 3 strings in melody
- 189–192: Vln I·II "sul A" on the recapitulated F2's peak and descent, so the A♭ statement is veiled where 69–72 is bright (Adler PDF 73, 75, Ex. III-7). Accepted; notes and bowing unchanged.
- 178: pizz. cellos play motive x with the timpani, pp (Adler PDF 103), giving the near-the-rim quotation a pitch. Accepted; scherzo thread told.
- Open strings at 67 and 232, a phrase sul G: no change. Agreed.

## Cycle 302 (v302 → v303), lens 2, A&S Unit 17
- 207–208: the second statement of F1's head moves up a step to B♭ minor over E♭m7 on the A♭ pedal, so 205–211 runs V7 – ii7 – V7 – I and repeats the exposition's 35–38 sequence (A&S PDF 264–266, 279); Tbn 1's seventh D♭4 resolves to C4 at 209. Accepted; scoring, the 205–206 horn statement and 209–211 unchanged.
- 99–106, 239–240, ascending fifths, 19–26, 67–82: no change. Agreed.

## Cycle 303 (v303 → v304), lens 3, Rimsky-Korsakov ch. IV
- 234: the plagal close's last chord no longer stops all groups together; brass and timpani end on a p quarter, woodwinds on an mp half, strings keep their dotted half into 235 (Rimsky PDF 116, 127, 130), as the score's other fades. Accepted; every pitch kept.
- 243–246, 159, 247, 235, 89: protected, kept. Proportions kept. Agreed.

## Cycle 304 (v304 → v305), lens 4, Adler part 2 ch. 15
- 89–90: Ob 1 now doubles Vln II's scale figure mf with a crescendo ("1."), after Adler part 2 ch. 15 on doubling a string line with a woodwind to give it colour.
- 102.4: Ob 1 rests instead of an accented low C4; the low oboe register was weak and Cl 1 already has the note.

## Cycle 305 (v305 → v306), lens 5, Gould PDF 53–68
- 32, 65, 185, 214, 251: on shared staves a semibreve sat against the other player's stem and read like a minim (Gould PDF 66). Score-only NoteColumn.force-hshift now puts the semibreve on the far side (Fl 1·2 at 32, Cl 1·2 at 65 and 185, Hn 3·4 at 214 and 251). Parts unchanged; MIDI identical.
- 219: tested c245's deferred spacing override; no change on the page, notes already sit just left of centre (Gould PDF 55). Closes c245's item.
- 24, 38, 103, 112, 200, 202: meeting stems match Gould's own example on PDF 66; left alone.

## Cycle 306 (v306 → v307), lens 6, Adler ch. 6–7 woodwinds
- 27–34: Fl 1·2 a2 now double the violins' countersubject at pitch, f, and the clarinets rest. The flutes had a middle-register pad that copied the oboes and could not be heard; the clarinets were at written D6–G6 (Adler PDF 184–185, 187, 192, 210). Flutes breathe at different points; Fl 1 holds A♭5–G5 at 30 to avoid octaves with the bass.
- 33–38, Bn 1 part only: tenor clef for the eighths up to B♭4 (Adler PDF 225).
- Checked, no change: low flutes 43–44, Cbn G2 at 24/87/164, bass clarinet line, clarinet E6–F♯6 in the ff tutti at 227–230 and 265–268.

## Cycle 307 (v307 → v308), lens 7, Adler ch. 5 strings in the orchestra
- 3–4: the cellos join the opening scale figure an octave below the violas, f, so the answer to the ff chord at 1–2 has a bass below G3 (Adler PDF 137, 139–141). Bars 1–2 and 5–6 unchanged; the basses still enter at 9.
- 115–122: the pizzicato accompaniment under the bassoon solo repeats the 51–66 formula; an imitative inner-string figure (Adler PDF 160) is proposed in the report but not applied, since 115–130 is protected.
- 9–10: with the cellos at 3–4 the octaves now build up step by step to the tutti; no change.

## Cycle 308 (v308 → v309), lens 8, Rimsky-Korsakov ch. IV
- 135–137: the crescendo into the stop chord is staged: strings alone at pp from 135, Cl and Bn join p < at 136, Hn 3·4 at 137 (Rimsky-Korsakov PDF 130). No pitch changes; the pp < into sf curve and the stopped horns at 138 are kept.
- 138: Vln I A♭4–F5 and Vln II F4–D5 as double stops, "non div.", for a fuller string sf over the soft wind chord (Rimsky-Korsakov PDF 129). Top lines, bass B and the 222→223 resolution unchanged.
- Brass re-entries after long rests (PDF 136) and strings' sf at the end of a wind crescendo (PDF 129): checked, no change.

## Cycle 309 (v309 → v310), lens 9, holistic, Brahms 2/iv; Rimsky-Korsakov examples 1–68
- 27–30: after c306 moved the countersubject to the flutes, Ob 1's held D5 sat above their line at 27.4, 28.1, 29.1 and 30.1 (Rimsky-Korsakov PDF 54, 65, 67: flutes below oboes sound unnatural). Ob 1 now rests 27.3–30.2 and returns mf on E♭5 at 30.3; Ob 2 and Hn 1·2 still hold the harmony.
- Brahms 2/iv comparison: the large plan holds; the one regression since v299 was this oboe pad.
- Considered, not applied: muted strings (no time for mutes, or protected bars), a bass clarinet solo, the second theme in violins and violas in unison (67–82, 187–198 protected).

## Cycle 310 (v310 → v311), lens 10, cyclic review; A&S Unit 32
- 243: Vln I upper desk plays G♯5→G5 (was E5 held), so the E-major chord, the finale's only sound in the scherzo's key, has the scherzo's last pitch on top in the same instrument, falling to G as bar 1's A♭5 does (A&S PDF 588, 593, 600–601). Harmony, horn call and dynamics unchanged.
- 1–2: tested A♭ on top in the flutes; it made outer-voice octaves with the bass at 2 and 6, so it was reverted.
- finale.md updated to cite movement I v351, movement II v350 and the scherzo v341; nothing the finale quotes has changed.
- Checked, no change: E♭ at 261 and 273.3, the stop chord's resolutions, C7 and tremolo only from 223, the one root-position V–I at 262→263, all quotations.

## Cycle 311 (v311 → v312), lens 1, Adler ch. 7 individual woodwinds
- 35–38: Fl 2 rests (it doubled Ob 1's pad at pitch in the flute's weak middle octave under ff strings, and had played without a break since 27; Adler PDF 185, 188, 192, 201). It re-enters f on D5 at 39, taking the held D5 from Ob 1, which stops at 41; Fl 1 also marked f at 39.
- Not applied: Fl 1's F6–B♭6 leap at 78 (protected F2 climax), low clarinets in unison at 95–98 (collides with the violas' E♭–E line), a bass clarinet line, a wind chorale at 247–264.

## Cycle 312 (v312 → v313), lens 2, A&S ch. 22 leading-tone sevenths
- 75.3: under F2's turn to the sixth degree over the tonic, the harmony is now VIIø7 (D–F–A♭–C) over the E♭ pedal, back to I on beat 4; it had been a cluster E♭–G–A♭–B♭–C (A&S PDF 377, 379, 381–382). Hn 1·2, Bn 1 and harp RH revoiced; no new parallels.
- 178→179: Bn 1 B2–D3 instead of rising to C3, so the diminished fifth with Cl 2 no longer moves to a perfect fifth (A&S PDF 375 Ex. 22-3c), as at the exposition's 58.
- Not applied: VIIø4/3 → I6 at 74→75 and 194→195; other tritone-to-fifth moves stay within one harmony or are protected; ♭VI in major has no unprotected place.

## Cycle 313 (v313 → v314), lens 3, A&S Units 16 and 19 six-four chords
- 19: the bass of F1's second statement now passes E♭–D–C through a passing V6/4 on beat 3 (A&S PDF 256–257, 309–310, 324), instead of repeating the first statement's leap; cellos, basses, Bn 2 and Cbn `es2 d4 c4`, violas and Cl 1 revoiced. Melody and the recapitulation's 159 unchanged.
- Proportions: the coda is 31% of the movement, longer than Dvořák 9/iv's, because the plan saves C major and the only root-position V–I for it; no change.
- Rejected: a passing 6/4 at 258 (G in the bass before the final V at 262), a neighbouring i6/4 at 147–150 (anticipates 151).

## Cycle 314 (v314 → v315), lens 4, Adler part 2 ch. 15
- 37–38: the third F1 head statement (Hn 3·4) had no string support; the cellos now double it an octave lower, ff, with the horns' articulation, f at 39 (Adler part 2 PDF 165, 176–179). Cl 2 holds C4 to 38.4 to avoid fifths with the new cello line.
- 273–276: the timpani roll on C starts f instead of ff, like the cellos and basses, and keeps its crescendo from 275 to fff at 278 (Bloch, Adler part 2 PDF 184). The chain, the quotation and the top C6 are unchanged.
- Not changed: 205–206 brass-only head (protected; cellos hold the pedal), the unison at 247–254 and 265–272, the arpeggios at 255–262.

## Cycle 315 (v315 → v316), lens 5, MOLA guidelines, parts
- Parts: rehearsal letters and tempo words landed at different heights at D, F, K, N, O, P, Q, R, T (the problem movement II found in its parts; MOLA PDF 10 Ex. 4). A new `\lt` helper in global.ily draws the tempo text inside the letter's mark, active only with `isPartsBook = ##t` (set in parts-head.ily; keep that line if the file is regenerated). Percussion and timpani padding adjusted.
- Fl 2 part: fixed page turn in the rest at 198|199, back to 2 pages.
- Part titles: "Symphony No. 1 in C minor — IV. Finale" (MOLA PDF 6).
- Bar 10: part-only minimum hairpin length in Fl 1, Fl 2 and Ob 2, so the crescendo prints (MOLA PDF 8 Ex. 7). Parts now build with 0 warnings (were 5).
- Score pixel-identical and MIDI byte-identical to v315. mkparts.py is stale; parts-book.ly is the real parts source.

## Cycle 316 (v316 → v317), lens 6, Adler ch. 9–10 brass
- 207–210: Hn 1 no longer holds concert E♭5 mp for four bars after entering a ninth below (Adler PDF 284, 303). The held horn chord is re-voiced in high/low order: Hn 1 B♭4 (C5 at 209), Hn 3 G♭4, Hn 2 E♭4, Hn 4 A♭3. The dropped E♭5 is still in the clarinets, flute, violas and Tbn 2.
- Breaths: tuba and bass trombone at 220|221, Tpt 3 at 258|259, the two longest loud brass stretches without one (Adler PDF 292; part 2 PDF 8). No pitch, rhythm or dynamic change.
- Checked, no change: four-horn chord order elsewhere (mostly protected), special brass effects (not in the Brahms/Dvořák models), tuba register, tuba eighths at 27–32.

## Cycle 317 (v317 → v318), lens 7, Adler part 2 ch. 15 texture
- 255–258: under the last chorale statement, the cellos and Hn 3·4 play F2's third phrase in C major, f under the ff chorale (G3–E3 | D3 C3 E3 G3 | C4–D4 | G4 F4 E4 D4), with Bn 1 from 257 (Adler part 2 PDF 175–181: a second theme against a long-note melody, as in the Jupiter finale). F2 had not returned after 198; its 5–3–2–1 head is the chorale's opening. Harmony, bass, chorale top line and the 259–263 cadence unchanged.
- Checked, kept: the three-octave head doubling at 247–254, the canon at 223–230, F1 against the motto rhythm at 265–272.

## Cycle 318 (v318 → v319), lens 8, Adler ch. 2 bowing
- Bowing (Adler ch. 2, PDF 38: strong attacks on a down-bow), six places, signs only: 259 cellos down-up (the two-bar ff F was on one bow), Vln I down-bow on the fff C at 263; down-bows on the accented heads at 267 and 269 and their pickups (as at 247); 198 violins down-up so the pickup to 199 is down-bow, violas E♭ and C♭ on separate bows; 147 violins down-bow on the ff dominant; 110 Vln II and violas down-bow at the climax; 101 and 105 sf chords down-bow in the lower strings.
- No pitch, rhythm or dynamic change; MIDI byte-identical. Other string techniques in the reading (spiccato, jeté, ponticello, col legno, trills) do not fit the style or fall in protected bars.

## Cycle 319 (v319 → v320), lens 9, holistic, Schumann 4/iv; Rimsky-Korsakov examples 69–130
- 257–258: the violas play E4 instead of C4, so the held C4 of c317's F2 phrase (cellos, Hn 3·4) is no longer hidden in a unison (Rimsky-Korsakov PDF 81, 91, Ex. 90). 255–256 left alone (protected chorale voicing).
- 38.4–41: Cl 2 moves C4→D4 and holds it, so the clarinets hold D4/F4 instead of a bare fifth for 13 beats in the diminuendo (Rimsky-Korsakov PDF 66, 90, 97).
- Schumann 4/iv comparison: the plan matches; the lyrical development centre and the Largamente ending differ and stay (protected).
- Not applied: cor anglais doubling the violas (would cover them; its solos are kept for 171 and 217–220); other open fifths are in tutti, horn pairs or protected bars.

## Cycle 320 (v320 → v321), lens 10, cyclic review; A&S Unit 26
- No score change (A&S Unit 26, tonicization). The one unused technique, a sequence of tonicized chords, fits only at 238, where an E-major applied chord would weaken the single scherzo-key chord at 243.
- Kept: the opening Ger6 → V7 as the dominant the whole symphony needs; C confirmed only at 259–263; E major at 243 as a chord, not a key; E♭ minor to E♭ major as mixture.
- Quotations against movement I v361 (35/35), movement II v376 (18/18, 11/11), scherzo v352 (52/52), finale record 41/41: unchanged. finale.md header updated; link to movement I's transient E♭ recorded.

## Cycle 321 (v321 → v322), lens 1, Sebesky ch. 6–7
- 255–258: F2's coda phrase was covered by held brass ff on its own pitches. The violas now join the cellos in unison on the line, ff espress.; cellos and Hn 3·4 go to ff; the held brass harmony (Hn 1·2, Tbn 1·2, bass trombone, Tpt 3) is f at 255 with a crescendo from 257 to ff at 259 (Sebesky PDF 208, 211–213, 219, 224). Chorale top line, tuba, woodwinds, violins and harmony unchanged. Supersedes c319's viola E4 at 257–258.
- Kept: no trills (no free held note needs one), Ob at 95–98, motive x three times, violas at 259–262.

## Cycle 322 (v322 → v323), lens 2, A&S Units 24–25 applied chords
- 20.4: VII°7 of V before the consequent's V7 (bass B♭–F–F♯; Cl 1 G–A♭–A♮; violas D–F–C, revoiced to avoid fifths with Hn 1·2) (A&S PDF 425, 428, Ex. 25-12a, 25-14).
- 36: the 5–6 link from A♭ to B♭ minor gets a chromatic bass E♭–A♭–A♮, V6/5 of B♭ minor on beat 4 (A&S PDF 435, Ex. 25-32). The violas', cellos' and Bn 1's figure is now C–F–E♭–C (C–E♭–F–C made octaves with Ob 1 and Tbn 1).
- Not applied: a deceptive cadence on VII°7 of V at 82; ♮VII7 → V6/5 has no free place.

## Cycle 323 (v323 → v324), lens 3, A&S Unit 18
- 121–122: the Italian sixth closing the development's G-minor area was not audible (the pizzicato E♭ and C♯ never sounded together) and had no 7–6 (A&S PDF 297–298, Ex. 18-12). Cl 1 enters pp on D6 at 121, holds it over the bass E♭ as a seventh, falls to C♯6 and resolves to D6 at 122, where Vln I's solo desks take it over. The bassoon solo and the 123–130 hand-over are unchanged; the line is a tenth or more above the solo.
- Checked, no change: proportions against Dvořák 9/iv, the C bass at 223–238, leading-tone doublings, augmented seconds; the Phrygian cadences at 57–58 and 177–178 also lack the 7–6 but are protected.

## Cycle 324 (v324 → v325), lens 4, Adler ch. 8 woodwinds and horns in the orchestra
- 91–94: in the ff codetta every part played short strokes with rests between. Ob 1·2 now hold E♭6/E♭5 and Hn 1·2 E♭4/E♭3, ff, through 94 beat 2, and Hn 2 leaps E♭3→E♭4 onto the dominant at 93.4 (Adler PDF 238, 240–241, 243, Ex. VIII-7 to VIII-11: Mozart 29 and Figaro). The strokes, the diminished seventh at 92 and the displaced tonic at 93 stay.
- Checked, no change: wind-only passage at 95–96 (breaks the violas' E♭→E at 97), held notes before upbeats, single players on solos, horn third, clarinet figures (protected), lower bass octave at 91–94 (saved for 110, 223, 263, 278).

## Cycle 325 (v325 → v326), lens 5, Adler PDF 282–301 score layout; MIDI rolls
- MIDI: timpani rolls now play as repeated strokes (they were one held stroke, so crescendo rolls could not grow). score.ly wraps the orchestra in a music function taking the timpani music; the MIDI-only score passes the timpani through \rollStrokesByBar, which applies the scherzo's shared rolls-midi.ily \rollStrokes to each roll only (applying it to the whole score would turn the string tremolo into notes). rollStrokeTable gives 11–23 strokes per second. Only the timpani track differs (172 → 1002 note-ons); print unchanged by this change.
- Brass family sub-brackets for horns, trumpets and trombones inside the brass bracket (Adler PDF 293–294), as in the scherzo. Breaks unchanged.
- 224, 226: the bowing text "unis., change bow at will" on three lines and the lower strings' text shifted, so they no longer cross the barline (Gould PDF 41, 55).

## Cycle 326 (v326 → v327), lens 6, Adler ch. 12 and 14 percussion
- 39–40: the exposition's half cadence on V of E♭ had no timpani, unlike every other dominant arrival. The A♭ drum is retuned to B♭ in the rest at 37 ("muta A♭ in B♭") and rolls B♭2 f > p with the contrabassoon, bass trombone and Hn 3·4, then goes back to A♭ at 43 (Adler part 2 PDF 79, 81).
- 178: the pp motive x near the rim quotes the scherzo's soft-stick ending; "soft sticks" at 171 and "hard sticks" on 178's closing rest, before the ff at 199 (Adler part 2 PDF 61, 80, 88, 110–111).
- Not applied: a soft cymbal after 223 (protected percussion plan), two drums together, a pp roll at 43–50, a bass-drum roll.

## Cycle 327 (v327 → v328), lens 7, Adler ch. 17 accompaniment
- 107–109: Bn 1 doubles the chromatic lament bass F–E–E♭–D–D♭–C two octaves up, p <, so the line is heard as a melody as well as the bass (Adler part 2 PDF 283, 288: Fidelio canon, Creation). Bass, strings, suspensions and entry order unchanged.
- Not applied: a string/wind dialogue at 87–90 (the bridge needs instruments added; protected), a chord change at 244 (protected harmony), 147–150 (a stop, not an accompaniment).

## Cycle 328 (v328 → v329), lens 8, Adler part 2 PDF 37–40, 187–196 dynamics and colour
- 42→43: the basses hold the low B♭ p > into the pp at 43 instead of stopping on 42.4 and re-attacking, so the dominant pedal 39–50 is unbroken (Adler part 2 PDF 190, 192, Ex. XV-36, XV-40). The other strings and bassoons still breathe at 42.4.
- 121→122: Cl 1's D6 lasts a dotted quarter, overlapping Vln I's solo desks' D6 instead of meeting it end to end (Ex. XV-37, XV-40).
- Not applied: sforzandi at 101 and 105 (no long note to carry them; protected), woodwind fp < at 209–210 (decided in c216 and c288), break-offs at 94→95 and 113→114.

## Cycle 329 (v329 → v330), lens 9, holistic, Dvořák 8/iv; Rimsky-Korsakov examples 131–180
- 43–47: the scale figure passes flute → clarinet → oboe over a held A♭3, the seventh of V7 of E♭; the held note moves from Bn 1 to Hn 4 (open, pp, dolce, same pitch and rhythm), so the woodwind phrase takes its harmony from a horn (Rimsky-Korsakov PDF 105, 108, 116, Ex. 136, 140), as c229 did at 95–98. Bn 1 rests 42.4–51.
- Dvořák 8/iv comparison: the plan holds; 43–47 was the one weaker texture. Compared with v319 nothing got worse (c324's held Ob 1 E♭6 at 91–94 kept).
- Not applied: a soft muted-brass chord (fits only at the protected 171–186), trills on held tutti notes (254, protected), a shorter slow coda (protected proportion).

## Cycle 330 (v330 → v331), lens 10, cyclic review; Casanelles ch. 5
- 276–277: after the theme-A quotation at 275–276 the timpani leave the roll on 276.3 and play G–G–G, landing on C at 277.1, the first stroke of movement I's pulse there. Motive x had appeared only on G as an unresolved dominant figure (9, 143–145, 178); its closing form, ending on the tonic as the scherzo's B–B–B–E does, now arrives at the end (Casanelles PDF 200–201, 225, 227, 235–239). Chain G–F♯–F–E, quotation, dynamics and fff close unchanged. New record line motiveXcloseC (42/42).
- finale.md: item 63 and HISTORY's cycle 329 entry wrongly called the woodwinds' scale figure at 43–47 "motive x"; corrected. Header updated to movement I v371, movement II v390, scherzo v362.
- Checks: owed items once each, the viola E♭/E thread, the one root-position V–I at 262→263, the stop chord's resolution only at 222→223, C7 and tremolo only from 223, all quotations: unchanged.

## Cycle 331 (v331 → v332), lens 1, A&S Unit 21 suspensions
- 226–230: the canon on the chorale (Vln I·II, Fl 1, Ob 1, Cl 1) repeated the brass chorale in the same whole notes and sounded like an echo. It now enters on G5 at 226 and each later note arrives half a bar late, tied over the barline, as in the Jupiter finale's opening (A&S Ex. 21-1, PDF 346–347), giving a 7th over vi, a 7–6 over IV and a 9–8 over I. Fl 2 and Ob 2 tie G5 into 227; Cl 2 at 229 is g'2. f'4. Two pairs of fifths at 228–230 are gone. Brass chorale, top line, bass, violas, dynamics and 222→223 unchanged. Record line choraleFirst VlnOne 226 replaced by choraleCanon (same pitches, displaced rhythm); 42/42.
- Not applied: a 5/2 bass suspension at 68 and 76 (the dominant lasts two beats; the harp sounds the leading tone first), anticipations at F1's cadences, suspensions in sequences (protected).

## Cycle 332 (v332 → v333), lens 2, A&S Units 28–29
- 17: ♯IV7 (F♯–A♭–C–E♭, the diminished-third chord) replaces the root-position ii°7 before the antecedent's half cadence: the bass rises F–F♯–G while the tune's A♭5 falls to G (A&S PDF 528–530, Ex. 29-31a). Cellos, basses and Bn 2 F♯; Cl 1·2 and Hn 4 adjusted. F1 unchanged; the recapitulation's 157 keeps the old chord.
- Not applied: a French sixth at 23 (a third chromatic approach to G in ten bars), a French sixth at 47–48 (would stop the A♭3 seventh falling to G♭ at 51).
- Checked: spelling of all augmented sixths and Neapolitans (1, 5, 16, 109, 121, 163, 168, 219, 261).

## Cycle 333 (v333 → v334), lens 3, Adler part 2 ch. 15 and 17
- 251–254: in the second phrase of the combination of movement I's two theme heads, the trumpets rest (to enter fresh on the chorale at 255), which left the second-theme head only in the middle. Fl 1·2 a2 now play its second phrase two octaves above Hn 1·2 and the violas (Adler part 2 PDF 288, Haydn's device; also 257, 261, 279). Vln I·II, Bn 1, Vc and Tbn 1·2 keep the first-theme head; the flutes still rest 255–256. No theme pitch changes.
- Checked, no change: the coda stages, the sub. p at 217–219, the timpani G–G–G at 18/34/158 (kept apart from motive x), dialogue and registral distance.

## Cycle 334 (v334 → v335), lens 4, Adler ch. 11 brass in the orchestra
- 255–256: the last chorale statement began with Hn 1–4 and Tbn 1 all on G3 while the I6 chord's root had only Tpt 3's low C4 (Adler part 2 PDF 15, Ex. XI-1; earlier noted by c084 and c319). Hn 1 now holds E4 and Hn 2 C4 at 255 (Hn 2 to B3 at 256 as before; Hn 1 re-attacks E4 at 257). Chorale top line, Tbn 1, F2's phrase, bass and dynamics unchanged.
- Checked, no change: the D-less brass V7 at 262 (every D makes fifths; protected), low trumpets at 159–166 (protected), soft trombone theme, string-free brass choir, brass under the timpani at 229, mute markings.

## Cycle 335 (v335 → v336), lens 5, Gould PDF 7–13, 17–68
- 82: the harp's 8 bassa line ran under the half rest to the barline since c296; it now ends right after the E♭ (Gould PDF 44).
- 229.3: on the shared flute staff Fl 2's B♭5 was shifted right with its flat printed in front of Fl 1's C6, reading as C♭6 over B♮5; score-only force-hshift puts the B♭ left with its own flat (Gould PDF 61–64, 66). MIDI byte-identical.
- Checked, no change: 103 seconds on shared staves (229 the only one with an accidental), ledger lines, spacing at 102/107/146/148, the harp octave line at 242, the basses' tenor clef at 27–34.

## Cycle 336 (v336 → v337), lens 6, Adler App. A ranges and terms
- 28.4–29.1: the tuba no longer tongues E♭1–D1 ff quarters below its professional range (Adler App. A PDF 306; part 2 PDF 8); it breathes on 28.4 and takes D2 on 29.1 with the bass clarinet. The contrabassoon keeps E♭1–D1. The held E♭1 at 166 stays.
- 51: the owed trumpet solo is marked "solo, dolce cantabile" instead of the combiner's "1.", as for the oboe (95) and bassoon (115) solos (App. A PDF 312). Not added at 171, where the cor anglais doubles the muted trumpet.
- Checked, no change: timpani ranges and retunings, the basses' C-extension notes, desk directions, stick words, highest horn and trumpet notes.

## Cycle 337 (v337 → v338), lens 7, Adler ch. 16 melody and countermelody
- 191–194: Ob 1 doubled the recapitulated F2 in unison with both violin sections throughout, and nothing answered the tune's held B♭4 at 194. Ob 1 keeps 187–190, rests 191–193 and at 194 echoes the tune's bar 192 at pitch, mp espress., from beat 2 (Adler part 2 PDF 211, 213: Dvořák's delayed oboe; PDF 229: like colours at the same pitch absorb each other). Beat 1 avoided for Cl 1's F♭4; no pickup, which made octaves with the bass.
- Not applied: a countertheme passed between instruments at 205–208 or 159–166; clarinets in contrary motion at 11–18.

## Cycle 338 (v338 → v339), lens 8, Casanelles ch. 4 and 6 expression
- 236: the violins' rising sixth C5→A5 sul A in movement I's second-theme head is marked "port." with a glissando line, the symphony's one marked string slide (Casanelles PDF 151, 154–155; Adler PDF 33). Not at 240. Pitches and MIDI unchanged.
- 212–214: movement II's theme B recall now swells to 213 and recedes before the breath instead of holding ff for five bars, as movement II shapes it (Casanelles PDF 148–150, 155). Hairpins in Tpt 1·2, Fl, Ob, Cl, Vln I·II; ff at 211, f at 216–217, sub. p at 219 and fff at 223 kept; hidden dynamics restore the MIDI levels from 215.
- Not applied: sul tasto → ord. at 219–222 (protected), vibrato marks, level changes inside the protected solos.

## Cycle 339 (v339 → v340), lens 9, holistic, Rachmaninoff 2/iv; Rimsky-Korsakov examples 206–274
- 191–196: Ob 1 rests again, as in v329, undoing c337's echo at 194: a woodwind cannot echo strings with a different timbre, and the echo ended on the violins' held B♭4 (Rimsky-Korsakov PDF 128–129). The one regression since v329.
- 110: the violins rise D–E–F in grace notes into the ff G6/G5 where the lament arrives and the brass enter (Rimsky-Korsakov PDF 129–130, Ex. 254), used before only at 35.
- Rachmaninoff 2/iv comparison: his second theme returns in full in the tonic major in the coda; here F2 has only 255–258. Kept (Brahms 1/iv model, protected bars, page cap).

## Cycle 340 (v340 → v341), lens 10, cyclic review; Adler ch. 1 and 15
- 95–98: movement II ends its last tail E♭5–D5–D♭5–C5 in Cl 1, dolce (II 85–90); the finale's quotation at the same pitches now passes the held C5 from Ob 1 to Cl 1, which enters pp dolce at 97.3 and fades through 98, overlapping the oboe by two beats (Adler PDF 19, 22; part 2 PDF 188, 191–192). Pitches, violas' E♭4→E4 at 97 and the horn chord unchanged.
- Quotations against movement I v381 (35/35), movement II v400 (11/11), scherzo v372 (52/52), finale 42/42; cyclic rules intact. finale.md header updated.
- Not applied: heterophonic doubling at cyclic places (protected; would compete with the quotation), an overlap at 223→224 (same players).

## Cycle 341 (v341 → v342), lens 1, Adler ch. 11 brass melodic presentation
- 77–80: on F2's first major-key climax (B♭6 at 78) Hn 1 left its pad and now doubles the cellos and Cl 1 at pitch (E♭4–F4 | B♭4. A♭ G F | E♭4. D4 | C B♭ A♭ G), breathing with Cl 1 after 78 and returning to D4 at 81 (Adler part 2 PDF 27, Ex. XI-10: horn and cello double long sustained melodies; also PDF 19, 26). Dynamics, Hn 2 and the tune unchanged.
- Not applied: Hn 3·4 high doubling at 37–38, trombones on F1 (withheld since c161), a Lohengrin-style hand-off (only protected places fit), a timpani dominant pedal at 43–50/255–260 (protected).
- Quotations: finale 42/42; movement I v391 35/35; scherzo v382 changes (trio tune, second idea) are not quoted here.

## Cycle 342 (v342 → v343), lens 2, A&S ch. 31 diminished sevenths
- 20.3: in F1's consequent the thin iv chord (F–A♭, no C) before c322's F♯–A–C–E♭ becomes F–A♭–B (rising diminished seventh, 4/3), so F→F♯, A♭→A and B→C all rise a semitone into beat 4: the paired rising diminished sevenths on F then F♯ (A&S PDF 561–562, Ex. 31-14, 31-15). Only the violas change (D4–B♭3–B3–C4); tune, bass and the recapitulation's 160 unchanged.
- Not applied: a common-tone diminished seventh into V7 (24–25 clashes with the tune's E♭; 39–42 with the F1 tail; other places protected); a common-tone augmented sixth over the final tonic (only 273 fits, protected).
- Checked, no change: diminished-seventh spelling at 135–138 and 20 (A&S PDF 558–560).

## Cycle 343 (v343 → v344), lens 3, A&S Units 6–8 phrase structure
- 159: the recapitulation's second F1 statement still leapt E♭–C in the bass, while the exposition's 19 has moved by step since c313. The bass now falls E♭–D–C through a complete passing V4/3 (D–F–G–B) on beat 3, the seventh F resolving to E♭ (A&S PDF 121–124, Ex. 8-5; 127, Ex. 8-10; 101, Ex. 6-17; 131). Vc, Cb, Bn, Cbsn, B.tbn, Tuba; Tbn 1·2, Cl 2 and four eighths of the Vln II/Cl 1 counter-line adjusted. Tune, Vln I divisi, dynamics and scoring of 159–166 unchanged.
- Not applied: VII6 as passing chord (no unprotected place at 3–8, 43–50, 67–76, 167–170); bass double neighbours (no unprotected tonic).
- Checked, no change: the coda's proportions (31%) and stages 223, 234, 246→247, 262–263.

## Cycle 344 (v344 → v345), lens 4, Adler ch. 5 strings in the orchestra
- 41–42: as the violins drop to F4–D4–E♭4–F4 in unison, fading to p, the cellos double them an octave lower (F3–D3–E♭3–F3) instead of holding B♭2, before the woodwind scale passage at 43 (Adler PDF 141, Ex. V-19, Shostakovich 6). c254 had rejected cellos here for the B♭ pedal; the pedal stays in Cb B♭1, Bn 2 B♭2, Hn 2 B♭3, and the cellos hold B♭2 at 39–40. c237's staggered drop-outs and Fl 1's A♭5 unchanged.
- Not applied: the string accompaniment under the bassoon solo 115–122 and the violas' dynamic balance at 83–86 (both protected and already sound by Adler PDF 128, 133–135, 144).
- Checked, no change: 242–244 and 255.

## Cycle 345 (v345 → v346), lens 5, MOLA parts
- Parts move from A4 to B4 with 7.5 mm staves, like movements I, II and the scherzo (MOLA PDF 7–8). c255 kept A4 to protect page turns; all 30 parts were rebuilt and every turn checked against each player's MIDI: Vln I now turns at 126 (234|235 had become a turn in the music), Vln II at 66 (removing the last turn in the music, 61|62), B. Cl fits one page, Ob 1 bar 10 has a part-only minimum hairpin length. 88 → 65 part pages.
- Six part-only cues after 15–46 bars' rest (MOLA PDF 5, Ex. 4): Fl 1 at 61.4 and 181.4 (Tpt 1), Cbsn at 87 (Vc), Hn 2 at 195 (Vln I), C.A. at 217 (Tpt 1), B. Cl at 257 (Vc).
- Score page 1 prints the instrumentation (MOLA PDF 6); pages 2–16 unchanged; score.midi byte-identical.
- Not changed: harp pedals at 43 and its 8va bassa (c255); no composer line.

## Cycle 346 (v346 → v347), lens 6, Rimsky-Korsakov ch. I orchestral groups
- 149: the timpani roll, tied ff from 147, covered the brass sfp < ff added by c226. It now re-strikes at 149 sfp < and reaches ff at 150 (Rimsky-Korsakov PDF 48, 41); the movement's first timpani sfp. Notes and rhythm unchanged (c174's protection predates the brass sfp).
- 207: the four horns mf instead of mp against Tbn 1·2 mp in the same chord (Rimsky-Korsakov PDF 41: horns one degree stronger than the other brass).
- 132 and 278: the harp's solid G chord and the left hand's C chord on the fff downbeat are marked "non arpegg." (Rimsky-Korsakov PDF 46). MIDI unchanged there.
- Checked, no change: stopped horn 168–169, basses' C-extension pizzicato 171–186, timpani retunings 206 and 215, Vc B♭4 at 78, breathing (no wind or brass player over 14.5 s without a breath).

## Cycle 347 (v347 → v348), lens 7, Rimsky-Korsakov ch. III combining timbres
- 141–142: over the B bass the four horns hold the chord tones G3–D4–B4–D5 and the seventh F4 was only in the violas, enclosed by the horns. Bn 1 now takes F4 with the violas instead of doubling Hn 3's D4, returning to F3 at 143 (Rimsky-Korsakov PDF 108: horns the chord tones, bassoons the dissonance; PDF 113).
- Not applied: soft woodwind thirds between trumpet octaves (219–221 already close; other places break the trumpet plan or protected bars); bassoon instead of Hn 4 on the seventh at 97–98 (c340 protects it); clarinets with the stopped horns at 168–169 (c108, c210); clarinets inside the horns at 39–41 (c319's tie).

## Cycle 348 (v348 → v349), lens 8, A&S Unit 3 rhythm and meter
- 243–246: the poco a poco stringendo began at 243, where one chord and a held 6/4 give no audible beat and the horn call enters off the beat, so it only hurried the call (A&S PDF 49). "stringendo" now prints at 245; 243–244 stay 2 = 66, the MIDI pushes 68–73–78–83, then 88 at R as before. c193's tempo plan kept.
- 227–229: the canon's tied 7–6 (228) and 9–8 (229) suspensions swell from the weak-half entry into the barline and recede to the resolution (A&S PDF 51, 55, Ex. 3-16, 3-7). Fl, Ob, Cl 1·2, Vln I·II; second players' whole notes at 228 become tied halves; partCombine fixed for the flutes' a2 at 231. Notes, ff level and brass chorale unchanged.
- Not applied: accents at 36.4/38.3, sf at 111, a slower Largamente at 211–218, tenutos on the horn call, a "ten." group.

## Cycle 349 (v349 → v350), lens 9, holistic, Bruckner 4/iv; Rimsky-Korsakov examples 261–312
- 175–178: the cor anglais and muted trumpet doubled the recapitulated F2 in unison for all 16 bars (171–186); Rimsky-Korsakov doubles a solo line only in single phrases (PDF 140–141, Ex. 284, 289). The muted trumpet now rests 175–178, so that phrase is the cor anglais alone; it returns at 179 ("1."). The duet at 171–174 (linked to movement I 171–174) is unchanged.
- Not applied (protected): Cl 1's pp E♭4 at 51–66, Ob 1·2 unison at 219–222, an obbligato beside the bassoon solo at 115–122.
- Bruckner 4/iv comparison: his coda is one long crescendo, this coda has several peaks; its plan is protected, observation only. v339 comparison (built in scratch): nothing got worse in c339–c348.

## Cycle 350 (v350 → v351), lens 10, cyclic review; Rimsky-Korsakov PDF 13–23, 124–129
- No score change. Cyclic review: quotations at pitch against movement I v401 (35/35), movement II v400 (18/18, 11/11), scherzo v391 (52/52; c383's E-major reprise second idea is not quoted); C7, tremolo, trumpet, cymbal and B→C rules intact. The muted trumpet's rest at 175–178 (c349) leaves the cor anglais duet at 171–174 intact.
- finale.md: eleven stale sentences corrected (header versions and MIDI length, scherzo record line, dynamics at 255, items 4, 8 and 10, the timpani's two retunings, open requests).
- themes-finale-quotes.ly: eight at-pitch link checks added (movement II's last tail in Ob 1 at 95; theme B's answer in Hn 1·2 and C.a. at 217; Hn 3 D♯4→E4 at 219; Tpt 1 B4→C5 at 222–223; Hn 4 F♯3→G3 and Cl 1 A♭4→G4 at 1–2); record 50/50. The violas' D♯→E at 219–220 cannot be recorded until lyparse expands `q`.
- Not applied: a relay across the orchestra at 7–10 (would replace c280's staggered crescendo) or 263–264; a muted-trumpet echo of the cor anglais at 178 (covers motive x).

## Cycle 351 (v351 → v352), lens 1, A&S Unit 3 rhythm and melody
- 258: F2's third phrase under the last chorale statement (c317) had even quarters from the minor solo's 62, but it is the major statement's 75–78 a sixth lower, whose peak bar has the dotted figure. Now `g'4. f'8 e'4 d'4` in Vc, Vla, Hn 3·4 and Bn 1, so F2's tonic-major return keeps its climax rhythm (A&S PDF 50–52, 54). Pitches, slurs, dynamics, chorale top line and harmony unchanged.
- Not applied: a turn at 195, upbeat openings for the themes (protected), a counter-metre (Ex. 3-7; protected places), a re-struck anticipation at 81–82, five-bar extensions, the dotted peak at 198 (cut off on purpose).

## Cycle 352 (v352 → v353), lens 2, A&S Unit 27 ninth chords
- 120.4: under the bassoon solo the V7 of G minor's second pizzicato chord becomes a full minor-ninth chord: Vln II E♭5 (5–♭6–5 neighbour) and violas C5 (the seventh), falling together in thirds to D5/B♭4 at 121.2; the score's first root-position V♭9 resolving 9th and 7th together (A&S PDF 463–464, 467, 470; Ex. 27-1, 27-2, 27-4a, 27-9, 27-11). Solo, Vln I, bass, dynamics unchanged (c209 narrowed the protection to the solo).
- 81.2: the violas' ♭9 neighbour C♭4 sounded a major seventh under the harp's B♭4, its own resolution; the harp's first group is now F4–A♭4–D5–F5 (A&S PDF 463, 469–470). No new pedal change.
- Not applied: 254→255, 74, 70.3, 204, the coda dominants at 238, 244, 250.

## Cycle 353 (v353 → v354), lens 3, A&S Unit 15 V6/5 and leading-tone chords
- 68.1: F2's second bar in E♭ major had D–F–A♭ over a D bass with the leading tone tripled (Cb, Bn 1·2) and no B♭ until the harp's third eighth. Bn 1 now holds B♭2 for the bar, so the downbeat is a complete V6/5 as in the other five statements and at 76 (A&S PDF 243–245). Bn 1 and Bn 2 split into two voices for that bar.
- Not applied: the B♭–B♮–C bass of Ex. 15-14 (no place: B♮ in the tune at 13, 21, 153, 161; 169–171 protected; 184–186 deceptive); III under the passing D6 at 69 (would rewrite c027's counter-melody).
- Checked, no change: the rising-third joints 26→27 and 198→199; key plan and coda stages (37, 26, 21, 50 s).

## Cycle 354 (v354 → v355), lens 4, Casanelles ch. 6 orchestration
- 164.3–4: the bass trombone doubled the cellos' E♭3–D3 an octave lower, a minor sixth E♭2 over G1 in tuba, contrabassoon and basses at f (Casanelles PDF 274–275; Rimsky-Korsakov PDF 85: only octaves and fifths that low). It now holds G2 for the bar; c214's reasons (no octave leap, no passing F2 under the basses' G2) still met.
- Not applied: Hn 3·4's low E3–G3 third over the C pedal at 235–242 (protected, p); passing a line between violin sections, string mutes, the low flute register, a strings-silent passage (each considered; no unprotected place where it helps).
- Checked, no change: bass trombone F2 under D3 at 153.3 and 161.3.

## Cycle 355 (v355 → v356), lens 5, Adler ch. 2 bowing
- 131–132: the violins' f run of six eighths was slurred into the accented cadence note at 132.1 (and in Vln II read like a tie D5–D5); the slur now ends on the sixth eighth, as at 9–10 (Adler PDF 38–39, Ex. II-19, II-20, II-22).
- 211–218: the violas' repeated half-note thirds under theme B take one bow per bar, louré (dashes under slurs), the score's second louré after 224–233 (Adler PDF 42–43, Ex. II-30). Pitches, div. and dynamics unchanged.
- 236: "port." moved above the slur, under the "sul A" line (Adler PDF 33).
- Not applied: tremolo under the horn call at 243–245 (strings mf on purpose), la metà at 43–50, 95–98, 171–186, other string effects. MIDI note-for-note identical.

## Cycle 356 (v356 → v357), lens 6, Sebesky ch. 2 wind instruments
- 91–92: Hn 3·4 dropped the ff eighth-note upbeats (`r8 x8` → `r4`) and land on the downbeats, while trumpets, trombones, tuba and timpani keep them, as the score already does at 199–204, 269, 271 and 277 (Sebesky PDF 32 and fn. 1, PDF 46, Ex. 51).
- Checked, no change: breathing (longest about 20 s, Cl 1 181–195, with eighth rests), ranges, Tpt 1's rests in the coda, flute above the lead trumpet at 211–218 and 257–262, C.A. with the horns at 217–218, stopped horn at 138, trombone slides at 248 and 250.

## Cycle 357 (v357 → v358), lens 7, Sebesky ch. 1 arranging fundamentals
- 188.3: F2's second bar was V6/5 → I in all ten statements of its head. In the A♭-major statement the bass (Cb, Bn 2) now takes G♭ on beat 3, V6/5 → V4/2 of IV, falling A♭–G–G♭–F into 189 against the rising tune (Sebesky PDF 19, Ex. 3A; PDF 14, 20). 189 unchanged; tune, counter-melody, clarinet background and bowing of 187–198 unchanged (the protection covers scoring; pitch changes there accepted before in c262, c270, c293).
- Not applied: thinning the clarinets' pp figure at 187–194 (c207, c224); the minor-mode line cliché at F2's heads (would undo c312 or resolve the stop chord before 223).

## Cycle 358 (v358 → v359), lens 8, Sebesky ch. 1 and backgrounds
- 245–246: under the stringendo (2 = 66 → 88 by 247, since c348 from 245) the cellos and basses held whole notes, so nothing low marked the quickening beat. They now restrike their D in tenuto halves at 245 and quarters at 246 into the basses' eighths at 247 (Sebesky PDF 207–208, Ex. 273; A&S PDF 49), as the violas push at 259–262. Pitches, hairpin, Bn 2's held D3 and the horn call unchanged.
- Checked, no change: the animando run at 82, the basses' eighths at 209–210, Cl 1's static line under the trumpet solo at 51–66, marcato accents.

## Cycle 359 (v359 → v360), lens 9, holistic, Mahler 1/iv; Adler part 1 full-score examples
- 255–262: on the chorale's last statement Vln I doubled the top line in tied whole notes ff; it now plays the same notes as bowed tremolo, tied as before (the composer restored the ties so the choraleLast record reads the held notes), the chorale's own violin colour from 223–225 and an agitated pedal over the brass theme (Adler PDF 243, Ex. VIII-11; PDF 161, Ex. V-37; PDF 261–262). Pitches, rhythm, dynamics and the entry at 263 unchanged; the cyclic rule (string tremolo first at 223) holds.
- Mahler 1/iv comparison: shared devices (outburst, lyrical flat-key second theme, first-movement recalls, failed early goal at 138, closing brass chorale); his coda rises continuously, this one moves in six stages (protected). v349 → v359: nothing worse; at 188 the root A♭ now sounds only in Cl 1's soft off-beat A♭3s, which must stay.
- Not applied: violin pedal at 111–113, 243–245, 265–272.

## Cycle 360 (v360 → v361), lens 10, cyclic review; Sebesky ch. 9 and ch. 1
- No score change. Cyclic review: quotations at pitch against movement I v411 (35/35; 199–204 compared part by part with I 27–32), movement II v400 (18/18, 11/11), scherzo v400 (52/52; c383 and c397 not quoted), finale 50/50; C7, tremolo (223–225, 255–262, 273–276), trumpet, cymbal and D♯4→E4 rules intact.
- finale.md: twelve stale sentences corrected (header versions and record counts, movement II's record location, Vln I tremolo at 255–262, muted trumpet resting 175–178, Tpt 1 B→C now recorded, open requests).
- Not applied: the bass clarinet doubling the motto at 224–228 (inaudible under the brass; protected; mvt1.md asks for no further bass-clarinet motto tail).

## Cycle 361 (v361 → v362), lens 1, A&S Unit 20 melodic figuration
- 71.4–72.1 and 191.4–192.1: F2's second phrase takes the escape tone followed by an accented passing tone (A&S PDF 337, Ex. 20-17), the one figuration idiom the movement had not used: violins C6–D6 | C6–B♭5 at 71–72, and F5–G5 | F5–E♭5 in the A♭ statement with violas and Hn 1 an octave lower. It is the turn at 75 a step higher, so the turn becomes a motive. Trumpet solo, 171–186, the turn at 75 and 255–258 unchanged; no record line covers these bars.
- 19.3: Cl 1's arpeggio G4→D4 made fifths with Hn 1·2's C4→G3 on a strong beat; now B3 (A&S PDF 331, Ex. 20-5).
- 191→192: Cl 2's F3→E♭3 moved in octaves with the tune; it now holds G3 at 192 and returns to E♭3 at 193 (A&S PDF 342–343).
- Not applied: the turn in F2's coda phrase at 255 (clashes with the low brass); F1's peak at 272→273 (protected). Kept: weak-beat or dissonant fifths at 12.3, 16.1, 156.1, 160.3 (Ex. 20-6, 20-25).

## Cycle 362 (v362 → v363), lens 2, A&S Unit 5 voice leading
- 167–168: Bn 1's augmented second E♭3→F♯3 becomes E♭–F–F♯–G, a chromatic line against the falling bass (A&S PDF 80, 82).
- 141–144: Hn 2 and Tbn 2 doubled the leading tone B over the B bass in the brass pads; both now hold G (Hn 2 G4 leads by common tone into its head entry at 143) (A&S PDF 76, Ex. 5-4).
- 82: V7 of E♭ resolves to an incomplete tonic with tripled root (Ex. 5-5, PDF 76–77), the first use of the device: Hn 1 E♭4 (was B♭3), cellos E♭ (was G); every pad voice moves by step, the harp still has B♭.
- Not applied: the Vln II–viola gap at 114 (one fading chord), d5→P5 in inner voices at 72.3/192.3, contrary fifths at 198→199 (protected), Vln II at 144 (protected stretto), emphatic outer octaves (Ex. 5-27a; no free cadence).

## Cycle 363 (v363 → v364), lens 3, A&S Unit 14 approaching the dominant
- 157–158: the recapitulation's F1 half cadence repeated F–D in the bass (ii°7); it now has the exposition's ♯IV7 approach from c332, bass F–F♯–G (Bn 1·2, B.tbn, Vc, Cbsn, Cb), Hn 4 F→E♭, Tbn 2 F–E♭ tied, Cl 1·2 as at 17 (A&S Unit 14, PDF 211–229). Tune, scoring and dynamics unchanged.
- 193–194: the A♭ statement of F2 goes IV – V6/5 of V – V7, bass D♭–D♮–E♭, as c273 did at 73–74 (A&S Ex. 14-3): Bn 2, Cb; Vc and Bn 1 hold F3 on beat 4; Cl 1 `r8 aes8( f8 aes8)` (B♭3 made octaves with the tune). Pitches only; c273's scoring protection kept.
- Not applied: the Phrygian half cadence at 177–178 (as at 57), modulation through I5–6 (only 95–98 fits, protected), an applied chord at 249–250 (protected).

## Cycle 364 (v364 → v365), lens 4, Rimsky-Korsakov ch. III chords and pairs
- 154 and 162: Tbn 1 held B3 over the B bass of the V6/5 and the V♭9, doubling the bass of a dominant inversion (Rimsky-Korsakov PDF 83–84); it now plays D4, an octave above Tbn 2, and steps to C4, as c362 fixed at 141–144.
- 136–138: in the falling diminished-seventh chain the clarinet and bassoon pairs each held a tritone; Cl 2 now G4–F♯4–F4 and Bn 1 E3–E♭3–D3, so each pair moves in minor thirds (PDF 90 rule 4, 91–92). Every chord keeps its notes.
- Not applied: three of a family with C.A./B. Cl as bass (PDF 93–95; only protected places fit), the oboes' fourth at 232/234 and clarinets' at 233 (protected plagal close; Ob 2 E4 noted as the fix), clarinets at 147–149 (protected stretto).

## Cycle 365 (v365 → v366), lens 5, Gould PDF 17–30 clefs and staves
- 33–38: the shared bassoon staff stayed in bass clef in the score, putting Bn 1's ff A♭4–B♭4 eighths on 3–4 ledger lines while the cellos play them in tenor clef; the tenor clef at 33 and bass clef at 39 (part-only since c306) now apply in the score too (Gould PDF 21–23). MIDI byte-identical.
- Checked, no change: the basses' tenor clef at 27–34 (c335), harmonics (only Vln I 43–50), ledger lines elsewhere (none beyond three), all-up bass stems at 199–210 and 247–262 (c015).

## Cycle 366 (v366 → v367), lens 6, Adler ch. 2 strings
- 50→51: the cellos' and basses' held pedal now ends up-bow, at the frog, before "pizz." on 51.1, the bass of the trumpet solo's first chord (Adler PDF 38, Ex. II-20; PDF 54), as at 114 (c085) and 167 (c318).
- 1 and 5: the opening ff double stops get "non div." in Vln I and Vln II and "arco, non div." in the cellos, so every first violin plays the A♭5 of the scherzo link (Adler PDF 30). Text only; notes, voicing and bowing of the protected bars unchanged; MIDI byte-identical.
- Not applied: undulating tremolo at 243–245 (settled by c355/c359), string trills, natural harmonics, mutes, la metà, non vibrato, ponticello, col legno.

## Cycle 367 (v367 → v368), lens 7, Sebesky ch. 3 strings
- 135–139: in the falling chain of diminished sevenths (pp < into the sf stop chord at 138) every line fell by semitone and the cellos only doubled the basses. The upper cellos now split at 136 and rise D3–E3–G♭3–A♭3, one chord tone per bar, take A♭3 to G3 with Hn 4 at 139 (c172) and rejoin for F1's head at 140 (Sebesky PDF 140, 145–147, 149, 159: one voice always rising in a build). The lower cellos keep the bass (c267); no B above the bass at 138 (c094); stop chord, Ob 1's B5, dynamics and the resolution only at 222→223 unchanged.
- Not applied: cellos on the bass at 125–131 (protected hand-over), a cello double stop at 114 and 133–134, flutes off Vln I at 239–242 (protected), a horn on the cello line at 7–8, solo strings (only protected places fit).

## Cycle 368 (v368 → v369), lens 8, MOLA dynamics notation
- 211–215: c338's swell on theme B hid its target levels, so the page showed a diminuendo with no goal; the twelve levels are now printed (ff at 215 in Fl, Ob, Cl, Tpt 1·2; ff at 213 and f at 215 in Vln I·II) (MOLA Ex. 3, Ex. 6, PDF 8). MIDI for 211–218 unchanged.
- 243–246: the strings' crescendo under the stringendo stopped before the ff at 247; it is now "cresc. molto" with dashes to the ff (new \crescMolto in global.ily; Vln I·II, Vla, Vc, Cb) (MOLA Ex. 7). Violas drop f > mf at 242 with the cellos; Bn 1·2's hairpin ends on f at 246; score-only spacing at 243.
- Checked, no change: wedges at 259–263, the 212–213 peak (fff kept for 223, 263, 278), Vln I·II f at 217–218.

## Cycle 369 (v369 → v370), lens 9, holistic, Franck D minor/iv; Adler part 2 full-score examples
- 154, 160, 162: Tbn 1 made octaves with the bass at 154→155 and 162→163 (from c364's D4) and at 159→160 (older). It now plays D4–G3 at 154 and 162, moving G3→C4 against the falling bass, and F4–C4 at 160 (Adler part 2 PDF 160–162: voice-lead full-orchestra chords as four-part writing). The one regression since v359.
- Franck D minor/iv comparison: the score uses all four of his cyclic devices; the coda is close to continuous tutti from 197 (Adler PDF 146), protected, observation only.
- Not applied: low horn under 3–4, high flute doubling at 67–76, a Lohengrin hand-over at 231–234, a timpani pedal at 255–260.

## Cycle 370 (v370 → v371), lens 10, cyclic review; A&S Unit 23 mixture
- 195–196: F2's restated opening bars in the A♭ statement no longer repeat 187–188 note for note; they turn to A♭ minor (A&S PDF 392, 395, Ex. 23-8, 23-12b): tune `es''2.( ces''4) | bes'4 aes'4 ces''4 es''4` in Vln I·II and violas, C♭2 bass on the i6 at 195 (Cb, Bn 1), cellos C♭3–D♭3–E♭3 then C♭3→C3 at 196.3–4; major returns on 196.4, so the minor turn at 198.3 and the C-minor tutti at 199 follow from the same C♭. F2's tune changes only there; no other movement quotes it.
- Cyclic review: quotations at pitch against movement I v421 (35/35; I 27–32 = IV 199–204 part by part), movement II v400 (18/18, 11/11), scherzo v400 (52/52); cyclic rules intact. The violas' D♯4→E4 at 219–220 is now in the record (threadViola; 51/51). finale.md: nine stale sentences corrected.
- Not applied: ♭VI as deceptive goal in major (Ex. 23-6; only protected places, and at 194→195 a major seventh over F♭). No change at 222→223 (A♭→G at pitch in Vln II, Tpt 2, Tbn 1).

## Cycle 371 (v371 → v372), lens 1, Rimsky-Korsakov ch. II melody
- 255–258: F2's last statement (C3–G4 in violas, cellos, Hn 3·4, Bn 1 from 257) sat in the middle register among the trombone chords. Vln II now doubles it an octave higher, ff espress., and returns to its arpeggio at 259; Cl 1 carries the arpeggio from 257 (Rimsky-Korsakov PDF 54, 61, 63, Ex. 8). F2's notes, the chorale top line, harmony and the woodwind rest at 255–256 unchanged.
- Not applied: a lower octave for the first-theme head at 247–254 (protected; c049), violas on the B♭-minor F1 head at 37–38. Checked, no change: the violin layout of 187–194 (sul A).

## Cycle 372 (v372 → v373), lens 2, A&S Units 9–10 cadential 6/4
- 129.3–4: in the development's G-major F2 the weak half of the bar sounded a 6/4 (bass D under the tune's G) resolving to V7 over the same D at 130, the metric error of A&S Ex. 10-6a (PDF 149, 154–155, 160). Beats 3–4 are now IV6 before V (PDF 135): cellos and basses E, Bn 1 B3–C4 held into 130 as V7's prepared seventh (PDF 139), Hn 3 D4–G4, Hn 4 G3–E3, violas rest on beats 3–4, harp E–G–C–E (same pedals). Tune, hand-over, rhythms, dynamics and 130–134 unchanged.
- Checked, no change: the cadential 6/4s at 18, 38, 109, 158, 243–244, 250 and 220 (c282). Not applied: a 6/4 → 4/2 joint at 74/194 (c282), the diminished-fifth soprano leap of Ex. 9-10.

## Cycle 373 (v373 → v374), lens 3, A&S Unit 26 tonal plan
- No score change. Key plan checked against A&S Unit 26 (PDF 442–461): exposition and development follow Mozart K. 457's plan (Ex. 26-8), the recapitulation K. 488's VI → ♭II → German sixth → V → I path (Ex. 26-14); every key is confirmed by a cadence with II or IV (PDF 443, 445); G minor and D♭ are transient (PDF 447–448).
- Not applied: a tonicized IV in the C-major coda (251 clashes with the head's B5; 248–250 protected; 271 has B♮; 265–272 over the tonic pedal); a descending-third sequence of tonicized chords at 235–242 (would anticipate 243's E major); a tonicized VI inside the development's dominant.

## Cycle 374 (v374 → v375), lens 4, Rimsky-Korsakov ch. III brass chords
- 249: Tpt 3's hammered C5 clashed by a second with Tpt 2's and Tpt 1's D5 and crossed above Tpt 2; it now plays A4 in the same rhythm, doubling Hn 3, while the timpani keep the C (Rimsky-Korsakov PDF 102–103: such discords in different instruments).
- 145–146: the brass V7 had a gap between the bass trombone's G2 and D4, with four instruments in unison on D4 and F4; Tbn 2 now holds G3 from 143 and moves to D4 at 147 as before (PDF 100). 147–150 unchanged.
- Not applied: low-flute thirds between trumpet octaves (PDF 108; c347), two horns and tuba on the bass under three trombones (PDF 101), Tbn 2 off the bass trombone's D♭3 at 211–212 (every alternative makes fifths at 212→213; PDF 112).

## Cycle 375 (v375 → v376), lens 5, Gould PDF 31–41 beams
- Beams: 95 groups of 2–4 notes sloped 1.65–2 staff-spaces (harp 67–82, 123–130, 235–242; violins 17, 28, 157, 259–262; violas; Cl 1 257–262; bassoon and cellos 35). A score-level `gould-max-slope` callback in score.ly keeps the shorter-stem end and limits the slope to one space (Gould PDF 33–35); no short group now slopes more than 1.35. parts-book.ly does not have it yet (as with c285's callback).
- Stem direction made uniform inside figuration that spans the stave at Vc 3.3, Vla 38.1, Vln II 163.3 and 165.3 (Gould PDF 39), so their slurs no longer drop below the notes.
- MIDI byte-identical; nothing else in the reading needed a change.

## Cycle 376 (v376 → v377), lens 6, Adler ch. 3 string colours
- 263–264: at the symphony's only root-position V–I the cellos hold open C2 with C3, "non div.", their first open C string in the movement (Adler PDF 73–74, 76, 99, Ex. III-56). Bowing, dynamics, progression, trumpets' B→C and timpani unchanged.
- 255–257: Vln II's ff octave doubling of F2 (c371) is marked "sul G" with a dashed line, keeping it off the weak D string under the brass chorale (Adler PDF 74–76, Ex. III-5); the G5 peak at 258 crosses strings. No notes changed.
- Checked, no change: the violins' C5→F6 leap at 36→37, double stops, basses' simplified lines, bow-change words, C-extension notes, ranges.

## Cycle 377 (v377 → v378), lens 7, Adler part 2 PDF 251–281 contrast of choirs
- 87–90: the scale figure was played twice in the same mix (violins in octaves with flute, oboe at 89–90). Now 87–88 is violins alone, and 89–90 winds alone: Fl 1 leads at F6, f <, with Ob 1 (F5) and Cl 1 (F4) a beat later in canon at the octave, meeting on F5 at 90.4; the violins return ff at 91 (Adler part 2 PDF 253–255, 271–272: a gesture passed between choirs before the tutti; two woodwinds in imitation, new in the score). Undoes c304's oboe doubling. Bass, inner chords, horns and 91 onward unchanged.
- Checked, no change: further wind imitation (protected places or too close to this one); third returns are already rescored.

## Cycle 378 (v378 → v379), lens 8, Adler ch. 7 expression marks
- 239–246: the counter's second statement (Cl 1 with the violas) swells on its tied A4 at 240–241 as the first does at 236–237 (c278); Cl 1 drops with the violas at 242, mf at 243, cresc. to f at 246 with the bassoons (its crescendo had no end level); Fl 1 and Ob 1 end their diminuendo on mf at 242, removing the one unequal dynamic on a shared staff (Adler PDF 185, 188, 212, 218; Ex. VII-9, VII-63, VII-75).
- 102 and 106: in the development's wind statements of the scale figure (Fl 1, Ob 1, Cl 1) the rising half crescendos into the accented top note, as at 44, 46 and 89–90 (Adler PDF 186, 227; Ex. VII-4, VII-93). Level stays mf; notes unchanged.
- Checked, no change: fp on long notes, sfp attacks, Fl 1's B♭6 at 78, the clarinet figure at 151–158, the bassoon solo at 119–122.

## Cycle 379 (v379 → v380), lens 9, holistic, Saint-Saëns 3/iv; Adler part 2 ch. 16 transcriptions
- 258–262: Cl 1 no longer doubles Vln II's arpeggio in unison under the last chorale statement; it breaks the same chords in contrary motion (Adler part 2 PDF 205, 208: Brahms's clarinets against the flutes' arpeggio), below the chorale top line, with its breaths. 258's last eighth E5 and 260's ending D5 avoid octaves with Tpt 3, Tbn 2 and the violas. Harmony unchanged.
- Saint-Saëns 3/iv comparison: running figuration as an independent layer against the hymn was the weak point; addressed above. Coda's six stages: observation only (protected). v369 → v379 (built in scratch): nothing worse.
- Not applied: a new timpani rhythm at 269–271 (repeats movement I 179–180), a quiet tritone figure with timpani at 133–134, open strings in the final cello chord at 278 (protected).

## Cycle 380 (v380 → v381), lens 10, cyclic review; A&S Unit 28 Neapolitan
- 184: at the recapitulated F2's last minor cadence iv becomes ♭II6 (Cl 1 and Bn 1 D♭ instead of C, falling to B over V7), so the tune's D4 at 185 sounds as ♮2 over V and the same D♭/F chord returns as IV6 of A♭ at 189 after the deceptive cadence, as movement II does at its 87 (A&S PDF 483–484, 494–495, Ex. 28-6). Tune, deceptive cadence and scoring of 171–186 unchanged.
- Cyclic review: records match movement I v421 (35/35), movement II v400 (18/18, 11/11), scherzo v400 (52/52), finale 51/51; rules intact. finale.md: nine stale sentences corrected.
- Not applied: N6 → V4/2 at 133–134 (clashes with the harp's G chord; c183), ♭II at 64 or 195–197.

## Cycle 381 (v381 → v382), lens 1, Rimsky-Korsakov ch. II wind melody
- 205–206: F1's head over the A♭ pedal had four horns a2 on A♭4 over one trombone; Tbn 2 now plays the head with Tbn 1 instead of holding E♭3 (still in the violas and the head), giving Rimsky-Korsakov's 4 horns over 2 trombones (PDF 74). Horns and 207–210 unchanged.
- Not applied: winds an octave above the B♭-minor head at 37–38 (would collide with the violins' figure and Fl 1's B♭5), a wind pair in thirds on a theme, a soft horn solo. Kept: the two horns with the cor anglais at 217–218 (protected).

## Cycle 382 (v382 → v383), lens 2, A&S Units 11–13 IV and VI
- 81–83: the E♭-major F2 cadenced at 81→82, then 82 held E♭ and the closing theme began on E♭ again at 83, two tonic downbeats in a row. 82 is now IV6 for three beats (bass C), V on beat 4 (bass B♭), so V7 → IV6 is a deceptive cadence and the closing theme at 83 is the goal (A&S PDF 170, 191, 200–201, 204–205; Ex. 11-12d, 13-15, 13-20i). Cb, Vc, Bn 1·2, Hn 1·2, Vla, harp. Tune, violin run, animando, dynamics and 83 unchanged; c362's incomplete tonic now falls on 83.
- Not applied: a second V7 → IV6 at 89–90 (c377's canon), IV6 passing inside V at 120 or 130–131, IV6 → V6/5 over a rising bass (octaves), I–IV6–I6, II6/5 → V4/2 at 84.

## Cycle 383 (v383 → v384), lens 3, A&S Unit 32 form (proposal declined)
- Not applied (composer's decision): c383 proposed moving the development's second F1-head statement at 103–106 from B♭ minor to D♭ major (A&S PDF 592–593, 599–601). Rejected: D♭ is the coda's key, tonicized at length only at 205–218 as the long-range ♭II that resolves at 222→223; a D♭-major statement in the development would sound that key area 100 bars early and weaken it (c380 declined an N6 at 133–134 for the same reason). F minor → B♭ minor at 99–106 is a descending-fifth sequence, and its link to 37–38 is a recall, not a fault. c373 protects the i–III–iv–v–V–I plan; c197 lists 99–109.
- Not applied: an E♭ or A key area in the coda, a passing IV at 243–244, a D♭-minor statement, a third sequential statement.
- No score change; v384 = v383.

## Cycle 384 (v384 → v385), lens 4, Rimsky-Korsakov tutti chords
- 278–279: the final fff chord's divided strings (Vln I·II, violas, cellos, basses) play tremolo, as at the same C-major chord at 223 and through 273–276; in Rimsky-Korsakov's tutti appendix every held f–fff chord with divided strings has tremolo (PDF 505–510, chords 1–20; PDF 88). Pitches, divisi, dynamics and the cut unchanged; string tremolo still begins only at 223.
- Not applied: brass a degree below the others at 223/263 (they carry the owed events), wind trills, a pp wind-and-brass chord, a wind tutti over pizz. basses, a twice-struck final chord, tremolo at 263 (protected).

## Cycle 385 (v385 → v386), lens 5, Gould rests
- Gould PDF 50–51 rest placement: Cl 1 eighth rests at 187–194 and Fl 2 quarter rest at 222 beat 4 moved to the centre line (score only), matching c205's bar 58.
- Gould PDF 51–52 beat grouping: 13 dotted half rests across mid-bar in 2/2 (234 brass/timpani and Vln I; 124 Vla) rewritten as r4 r2. MIDI byte-identical.

## Cycle 386 (v386 → v387), lens 6, Adler harp
- Adler PDF 117 / Rimsky PDF 46 harp damping: "étouffez" on 279 beat 2 so the final low harp chord C2–G2–C3 stops with the orchestra, as at 82, 131, 134, 243 and movement I's bar 182.
- Harmonic chords considered and declined (no unprotected spot fits).

## Cycle 387 (v387 → v388), lens 7, Rimsky-Korsakov combined groups
- Rimsky-Korsakov PDF 76–79: Bn 2 doubles the cellos' lower octave of the B♭-minor F1 head at 37–38 (f; rests 36 beat 4 to breathe).
- Rimsky-Korsakov PDF 74–75: Bn 2 doubles Tbn 1·2 on the head at 205–206, handing to Bn 1 at 207–208; Bn 2 returns to the A♭2 pedal at 207.

## Cycle 388 (v388 → v389), lens 8, Adler horns and trumpets
- Adler PDF 304–305 (Brahms 1/iv Ex. X-8, Don Juan Ex. X-12): swells on the horn call's long notes at 243.3 and 244.2 in Hn 1·2 and Tpt 1·2, returning to the printed level; "molto espr." added. \partCombineChords keeps the a2 horns at 251–266 in one MIDI voice; MIDI notes and velocities unchanged.
- Con sordino and echo effects considered and declined.

## Cycle 389 (v389 → v390), lens 9, Borodin 2 holistic; A&S double suspension
- A&S Unit 21 (Ex. 21-2, PDF 346–348) double suspension at 80.4–81: Ob 1 E♭5 tied into 81, resolving to D5 on 81.2, a third under the tune's G5→F5 over V7; Hn 1 ties G3 and plays D4 only from 81.3.
- Borodin 2/iv holistic comparison and v379 → v389 check: nothing worse. 90.1 surface fifths in c377's wind canon kept (passing dissonance, A&S PDF 341, 343).

## Cycle 390 (v390 → v391), lens 10, cyclic review (no score change)
- Cyclic review (Adler ch. 17): all quotations at pitch against movement I v421, II v400 and scherzo v400 (records 35/35, 18/18, 11/11, 52/52); cyclic rules hold. No score change.
- coherence/finale.md: eight stale sentences corrected (header, F1 coda 205–208, Bn 2 at 37–38, F2 at 81 and its pad, motive x item 13, open requests, movement I heading).
- Heterophonic doubling and solo string over winds considered and declined (spots are protected quotations or inaudible).

## Cycle 391 (v391 → v392), lens 1, Adler ch. 3 strings
- Adler PDF 73–76, 99 (open strings at soft fades): "sul G" for Vln and Vc at 41–42, and for Vln I and Vla at 169.4–170, so the soft D is stopped, not an open string. No notes or MIDI changed.
- Viola-as-bass, F2 low-octave start at 67–70, Vln II 46.3: considered, not applied.

## Cycle 392 (v392 → v393), lens 2, A&S Unit 17 sequences
- A&S Unit 17 (PDF 265–267, Ex. 17-1, 17-2) sequence: Vln II's run at 207–208 now moves up a step with the other voices (B♭3 upward to the accented G♭5), instead of repeating 205's pitches; removes a second against the head's passing F5 at 208.2.5.

## Cycle 393 (v393 → v394), lens 3, Rimsky-Korsakov ch. IV combination
- Rimsky-Korsakov PDF 136 (brass re-entry after long rest at pp or ff, not f): bass trombone at 255–258 now enters ff on E2 with the tuba (was f on E3, doubling Tbn 2 and the theme note), crescendo from 259 to fff at 263 as before. Clears the 257.1 doubling flag.
- Form proportions checked (exp 35%, dev 18%, recap 16%, coda 31%); no change.

## Cycle 394 (v394 → v395), lens 4, Adler ch. 15 flute octave
- Adler part 2 ch. 15 (Mozart 40/iv and Beethoven 9/i, PDF 150–152): flutes no longer drop to the unison with Vln I at the loud cadences; Fl 1 an octave up at 24–26 and 35–36, both flutes at 164–166 (highest A♭6, below the C7 reserved for 223).

## Cycle 395 (v395 → v396), lens 5, Gould spacing
- Gould PDF 56–57: score-only rule keeps last stems at least one space clear of barlines (0.86 on page 15, 253–265; Cl 2 shift at 257–262 now -1.0).
- Gould PDF 54: c368's widening of bar 243 removed; strings' "cresc. molto" now starts at 244 (mf stays at 243, ff at 247 unchanged).
- Gould PDF 54, 57: bar 217 viola text now a three-line "change / bow / at will" (\cbawN in global.ily) instead of \textLengthOn.
- Gould PDF 53: double barlines at letter F (83) and letter T (273).

## Cycle 396 (v396 → v397), lens 6, Adler woodwind breathing
- Adler PDF 188 (Ex. VII-9, Brahms 1/iv), 192, 198: staggered eighth-note breaths in the Fl 1 / Ob 1 / Cl 1 unison at 226–230 (Fl 1 at 227, Cl 1 at 228, Ob 1 at 229), the other two holding; pitches and swells unchanged.
- Adler PDF 230: breath marks for Bn 2 after 220, Bn 1 and Cbsn after 221 on re-struck notes before the fff C1 at 223 (score only).

## Cycle 397 (v397 → v398), lens 7, Adler ch. 11 brass entries
- Adler ch. 11 (Hindemith PDF 42, Bartók PDF 44–47): the last F1-head entry of the retransition stretto at 145–146 now goes to Hn 3·4 a2 at G4, "ben marc." (horn pairs alternate: Hn 1 at 139, Hn 1·2 at 143, Hn 3·4 at 145); the other held brass keep a complete V7.
- "ben marc." on the brass answer of F1's head at 103 (Hn 3·4, Tbn 1); text only.

## Cycle 398 (v398 → v399), lens 8, A&S Unit 21 suspensions
- A&S Unit 21 (PDF 352 sec. 12, Ex. 21-12; PDF 369): Hn 2 at 81 now B♭2 (V7 root) instead of F3, so the 7/6 suspension G3 no longer sounds against its own resolution note.
- A&S PDF 347–348: Ob 1's diminuendo at 81 starts on D5 with the tune's resolution.

## Cycle 399 (v399 → v400), lens 9, Beethoven 9 holistic; release check
- Casanelles PDF 272–276 (bow position and tone colour): strings start the falling chain at 135 "sul tasto" at pp and return to "ord." on the sf stop chord at 138 (text only; merged with the existing div./non div.).
- Release check: subtitle now "Full score in C — v400, 27 October 2026"; title "IV. Finale: Allegro con fuoco" and part headers agree; parts build with 0 warnings.
- Beethoven 9/iv holistic comparison and v389 → v399 check: nothing worse.

## Cycle 400 (v400 → v401), lens 10, cyclic review
- Cyclic review: every quotation of movements I (v421), II (v400) and the scherzo (v400) matches at pitch; records 35/35, 18/18, 11/11, 52/52, finale 51/51. No score change.
- coherence/finale.md: five stale sentences corrected (movement II record location, scherzo request date, scherzo.md path, bass trombone at 255 since v394, Hn 4 at 43–47 since v330).

## Cycle 401 (v401 → v402), lens 1, Adler woodwinds
- Adler ch. 7 (PDF 184–232): woodwind solos, registers and breathing checked (Bn 1 116–122 peak mp per PDF 210; breath spans per PDF 188, 198, 214); low-clarinet theme and low-flute colour considered and declined. No score change.

## Cycle 402 (v402 → v403), lens 2, A&S mixture
- A&S Unit 23 (PDF 387–388, Ex. 23-2b and 23-2h; PDF 395): bar 82, the chord before the closing group's V is now minor iv6 over C♭ (Vc, Cb, Bn 2, harp; violas C♭4–B♭3 an octave above the cellos), so the violas' C♭ at 81 is no longer contradicted by a C♮ bass before B♭; Hn 1 E♭4–D4 gives V its third; score-only harp pedal mark "C♭" at 81. F2's tune and bar 83 unchanged.
- Considered and declined: ♭9 in V7 of G at 131, ♮7 appoggiatura at 135, °6/5 passing chord at 19 and 159 (protected or against the melody).

## Cycle 403 (v403 → v404), lens 3, A&S 6/4 prolongation
- A&S Units 16 and 19 (PDF 255–257, 309–310, Ex. 19-4 and 19-9): bars 75–76 the bass steps G–F–E♭ through a passing V6/4 into the E♭-major statement's I (was a leap G1→E♭2 on 75.3 a beat early, leaving a minor 9th under the violins' turn); Cb and harp LH `g,,2 f,,4 es,,4 | d,,2 es,,2`, Bn 2 `g2 f4 es4 | d2 es2`, Hn 2 `g2 bes2~ | bes2 g2` (avoids octaves with the new bass).
- Considered and declined: cadential 6/4 at 89–90, expanded dominants at 39–42 and 147–150. Proportions checked (exp 34.9%, dev 12.2%, retrans 5.5%, recap 16.3%, coda 31.2%).

## Cycle 404 (v404 → v405), lens 4, Adler ch. 15 texture
- Adler part 2 ch. 15 (PDF 159–166): Fl 2 at 263–264 now resolves the chorale's B5 to C6 with Fl 1 (a2) instead of leaping down to E5, its weak register and already in Vln II; C7 still only at 223.
- Considered and declined: V7 seventh at 262, brass on the motto at 265–268, timpani at 231–233, chorale doubling at 257–263.

## Cycle 405 (v405 → v406), lens 5, MOLA
- MOLA PDF 7–8, Ex. 7: a text crescendo broken by a line or page break now restates "(cresc.)" on the new line (callback c405-broken-cresc in global.ily, on in score.ly and parts-book.ly; in the score only bar 144, after the 143|144 page turn). Parts book builds with 0 warnings.
- MOLA Ex. 7: harp "étouffez" kept inside its bar at 134, 243 and 279 (placement only).
- Ob 1's solo number at 187 now bold like the others.

## Cycle 406 (v406 → v407), lens 6, Adler brass endurance
- Adler (adler2 PDF 8, adler1 PDF 292, brass need frequent rests): the tuba now rests at 217–218 (was 211–228 with breath marks only, about 33 s); F still held by contrabassoon F1 and bass trombone, basses and Bn 2 F2 under the horns' echo.
- Considered and declined: Hn 1 C5–D♭5 at 105–106, stopped-horn echo at 217–218, low-brass balance at 207–208.

## Cycle 407 (v407 → v408), lens 7, Adler ch. 5 strings
- Adler ch. 5 (PDF 137 Ex. V-14, PDF 141 Ex. V-19): cellos join the violins' third rising run at 209–210, an octave below Vln II (A♭2 up to G♭4, f <), adding an octave to the crescendo into 211; the A♭ pedal stays in basses, Bn 2, Cbsn, bass trombone, tuba and timpani.
- Considered and declined: agitated inner strings at 115–122 (protected), a Vln II counter-line at 19–26 (keeps the recap's growth).

## Cycle 408 (v408 → v409), lens 8, Rimsky sf-p
- Rimsky-Korsakov PDF 129–130 (sf-p and crescendo by groups): bar 149, all woodwinds now join the brass and timpani's sfp < into ff at 150 (they had re-attacked ff over the dip); strings and Tpt 1·2 keep the attack. Notes unchanged.
- Considered and declined: Hn 1 pp at 187, Tpt 3 ff at 247, clarinet morendo at 39–42.

## Cycle 409 (v409 → v410), lens 9, Brahms 1 holistic
- Rimsky-Korsakov Ex. 18 (PDF 58, 195): a solo cello doubling Vln II on F2 at 67–76 tested in a scratch build and declined (inaudible inside the section, costs the counter-melody's first desk).
- Brahms 1/iv holistic comparison and v400 → v409 check (v399 is not in the checkout; v400 differs only by text): nothing worse. No score change.

## Cycle 410 (v410 → v411), lens 10, cyclic review
- Cyclic review against movement I v421, movement II v400 and scherzo v400: all quotations at pitch, records 51/51, 35/35, 18/18, 11/11, 52/52; cyclic rules hold.
- A&S Unit 32 (PDF 586–593): Hn 1 common-tone E♭4 from 186 into 187 tested and declined (17 pages, covers the protected 171–186 cadence). No score change.
- coherence/finale.md: six stale passages corrected (bar 82 iv6, Fl 2 at 263, Vln II and cello runs at 207–210, E♭ silence now 217–218, running list moved under its heading, open request now as of v410); note added on the scherzo's last horn phrase continuing into bars 1–2.

## Cycle 411 (v411 → v412), lens 1, Sebesky melody
- Sebesky ch. 6–7 (PDF 204–230, Ex. 273): carrying F2's fourth phrase in violas and cellos into the cadence at 259–262 tested and declined (octaves or fifths into 263, masked by the brass, loses the viola pulse). No score change.

## Cycle 412 (v412 → v413), lens 2, A&S applied chords
- A&S Units 24–25 (PDF 419, 429 Ex. 25-21b, 439): bar 77 beats 1–2, the I6 under F2's climb to the B♭6 at 78 becomes V6/5 of IV (violas D♭4 falling to C4; Hn 2 B♭3–A♭3 so the leading tone G is not doubled; harp RH drops its G4 for the half bar). Tune, bass and dynamics unchanged.
- Applied chords at 17.3, 20.4, 36.4, 70.3, 73.4, 80.1, 157.3, 168, 202 checked: no fault. V4/3 of ii at 126.3, VII°7 of V at 38.3, a third ♯4 approach at 23.4/160.4 and C7 at 78 declined.

## Cycle 413 (v413 → v414), lens 3, A&S 6/3 techniques
- A&S Unit 18 (PDF 297–298, Ex. 18-12, the 7–6 into iv6 of a Phrygian cadence): Cl 2 at 57–58 `bes2~ bes4 aes4~ | aes4( bes4 f4 aes4)` and at 177–178 `es4 g4~ g4 f4~ | f4( g4 d4 f4)`, holding over the bass and resolving on beat 4 into V7's seventh; violas at 177.3 start on G instead of F. Clears the octave flag at 178.1. Solo and pizzicato unchanged.
- Declined: stepwise bass at 57/177, voice exchange at 87–89, rising 6/3 chains, moving bass under 223–238. Proportions unchanged.

## Cycle 414 (v414 → v415), lens 4, Adler ch. 8 woodwind-string
- Adler ch. 8 (PDF 245 Strauss, PDF 270 Copland, PDF 249–250): Fl 2, Ob 2 and Tpt 2 now end with the 216 diminuendo and rest at 217–218, so the cor anglais and Hn 1·2 echo of theme B's head is heard; they re-enter on their old notes at the 219 sub. p. Top line and the 205–223 dynamic path unchanged.
- Checked, no change: Ob 1 unison with the violins at 187–190, the overlapped wind pairs at 219–222.

## Cycle 415 (v415 → v416), lens 5, Adler ch. 18 score preparation
- Adler PDF 291, 301; Gould PDF 41, 55: "change bow at will" no longer crosses barlines: three-line text at 149 (Vc, Cb) and 224 (Cb), a new four-line text with "unis." at 224 (Vc) and 226 (Vln II) (global.ily); the basses' text moves from 139 to 140 within the same held B♭. MIDI unchanged.
- Checked, no change: five ledger lines at 78, 213–214, 223 (Gould PDF 47); timpani retuning placement (Adler PDF 292, 294).

## Cycle 416 (v416 → v417), lens 6, Adler percussion
- Adler part 2 ch. 12 (PDF 79, timpani on tonic and dominant at cadences): the A♭ drum stays on B♭ from 37 to 94 so the timpani strike E♭/B♭ with the trumpets, tuba and basses in the codetta (91–94: `es4-> r8 es8 bes,4-> r4` twice, then `r4 es2-> bes,4->`); "muta B♭ in A♭" moves from 43 to 95.
- Same source: bar 113, the timpani play F2 with the bass on the development's F-minor cadence instead of C (G drum to F at 95, back to G at 114). Range now F2–E♭3. Parts book builds with 0 warnings.

## Cycle 417 (v417 → v418), lens 7, Adler ch. 15 polyphony
- Adler part 2 ch. 15 polyphonic texture (PDF 172–186): violas in thirds and sixths under Vln II at 255–258 (Mozart, PDF 176) tested and declined (new fifth at 258.1 with Cl 1, masked by held brass, undoes c327's viola–cello unison). 247–254 three-octave doubling kept (register gap holds the second theme). No score change.

## Cycle 418 (v418 → v419), lens 8, Adler bowing
- Adler PDF 38–39 (about six notes per bow at forte): the cellos' run at 209–210 now slurs 4 + 8 like Vln II (was 12 on one bow); Vln I down-bow at 209, so all three lines reach the accented G♭ at 210.3 on a down-bow.
- Adler PDF 38, 42–43: down-bows for the lower strings on the accented arrivals at 113 (Vla, Cb) and 132 (Vla, Vc, Cb), matching the violins. Bow signs only; MIDI unchanged.

## Cycle 419 (v419 → v420), lens 9, Tchaikovsky 5 holistic
- Rimsky-Korsakov examples No. 69–130 (PDF 241–305; Ex. 87, 91, 98; PDF 78–79, 129–130): the contrabassoon no longer doubles the basses under the soft lament bass at 107–109; it rests from 94 and enters ff on its C1 at 110, the loud goal.
- Tchaikovsky 5/iv holistic comparison and v409 → v419 check: nothing worse.

## Cycle 420 (v420 → v421), lens 10, cyclic review
- Cyclic review against movement I (mvt1.md v441), movement II (mvt2.md v420) and the scherzo (scherzo.md v412): all quotations at pitch; the scherzo record's 9 changed entries are the second idea (c411), which the finale does not quote.
- A&S Unit 26 (PDF 446, 451, 457): tonicizing IV at 270–272 (B♭ in F1's third bar) tested and declined (clashes with movement I's head in major; loses F1's leading tone). No score change.
- coherence/finale.md: header, the scherzo motto-tail bar numbers (357–360), the scherzo and movement II headings and the open request brought up to date; movement I's two seeds of the finale (I 79→80, the development's B–D–F–A♭ stations) recorded.

## Cycle 421 (v421 → v422), lens 1, A&S figuration
- A&S Unit 21 (PDF 352–353, 363–364, Ex. 21-35): the E♭-major counter-melody at 74 (Vc, Vla, Hn 1) now goes B♭–A♭–F–G, the G a weak-beat anticipation tied into 75, instead of G3 on beat 3 against the bass's passing seventh A♭ and the harp's A♭4; matches the recapitulation at 194.
- Tested and declined: a melodic resolution of the C6 at 242. Checked, kept: F2's cadences at 73–74 and 80–81, the 4–3 at 210–211.

## Cycle 422 (v422 → v423), lens 2, A&S Neapolitan and augmented sixths
- A&S Units 28–29 (PDF 482–529): the critic proposed ♭II6 (B♭–D♭–G♭, top line G♭6–F6–E6) at 112 in place of ii°6/5. Rejected by the composer: 107–113 (lament and F-minor climax cadence) is on the do-not-touch list (c276, c551, c623), the change gives up the prepared F–E suspension at the climax, and ♭II is kept for its cross-movement thread (movement I's N6 at 20–22 and 140–143, the finale's D♭ episode at 205–223 and 184). No score change.
- Spelling check (A&S PDF 496–499): all 27 chromatic spellings correct.

## Cycle 423 (v423 → v424), lens 3, Adler accompaniment and pacing
- Adler ch. 15/17 (PDF 190, Ex. XV-36): a soft horn chord overlapping the ff stroke at 94→95 tested and declined (the half-bar silence ends the exposition and sets off the movement II quotation). Coda stages, the second-theme head at 235–239, the horn call's accompaniment and the subito pianos checked. No score change.

## Cycle 424 (v424 → v425), lens 4, Adler ch. 11 brass
- Adler ch. 11 (PDF 15, brass balance above mf): Tbn 1 now plays F♯3 instead of E♭3 in the German sixth at bars 1 and 5, stepping to its G3 at 2 and 6, so the chord's defining F♯ is no longer only in Hn 4. E♭ stays in Hn 2, Ob 1, Cl 2, Vln II, violas and cellos; link pitches unchanged.
- Recorded only: the single brass F♯4 in the German sixth at 261 (protected). Declined: bars 2 and 6 low third, the plagal close at 231–234.

## Cycle 425 (v425 → v426), lens 5, Gould clefs
- Gould PDF 21–22: the cellos' run at 209–210 stays in bass clef (G♭4 on three ledger lines) instead of switching to tenor mid-slur and back before the rest.
- Gould PDF 13, 23: score-only bass clef for Hn 1·2 at 79–82 (after Hn 1's breath at 78|79, back to treble at the 82|83 double bar), as at 25–26 and 165–166, so Hn 2's B♭2 no longer sits on five ledger lines. Parts unchanged; MIDI unchanged.

## Cycle 426 (v426 → v427), lens 6, Adler ranges
- Adler App. A (PDF 306; adler2 PDF 8): the bass trombone's short ff dominant notes at 91–93 rise to B♭2 (were B♭1, the bottom of its range); B♭1 stays in tuba, contrabassoon and basses.
- Adler PDF 302: score header now names the basses' C extension at 75–76, 166 and 174–183.
- Checked, no change: Tpt 1 C6s at 243–250, timpani drum sizes, woodwind extremes.

## Cycle 427 (v427 → v428), lens 7, Adler ch. 17 accompaniment
- Parts book: the bass clarinet's sfp < at 149 is now drawn in its part (part-only minimum hairpin length, as at bar 10); the parts book builds with 0 warnings again. Score MIDI unchanged.
- Adler ch. 17 (PDF 279, Bizet octave lift at the climax): Fl 1 an octave above the cor anglais and muted trumpet at 181–183 tested and declined (takes the climax from the soloists). No score change.

## Cycle 428 (v428 → v429), lens 8, Adler climactic brass
- Adler Ex. XI-19, XI-21 (PDF 37–40), Rimsky-Korsakov PDF 130: in the last cadence the brass hold ff at 259–260 and crescendo from 261 with the timpani's roll into fff at 263; woodwinds and strings still crescendo from 259; the horns' breath after 260 now precedes their crescendo. Pitches, voicing and the 263 fff unchanged; MIDI notes identical.
- Declined: chorale accents after 255, timpani on the sforzandi at 101 and 105.

## Cycle 429 (v429 → v430), lens 9, Dvořák 9 holistic
- Rimsky-Korsakov PDF 107–108 (Ex. 148, 151: stopped horns over low clarinets): Cl 2 at 167–170 now plays A♭3–F♯3–G3–F3 in its low register with Bn 1 (`aes1 | fis1\> | g1 | f1\pp`), no longer in unison with the stopped Hn 2; Cl 1 still carries A♭4 to the cor anglais at 171. Dynamics unchanged.
- Dvořák 9/iv holistic comparison and v419 → v429 check: nothing worse.

## Cycle 430 (v430 → v431), lens 10, cyclic review
- Cyclic review against movement I v461, movement II v445 and scherzo v421 (their newest versions): all quotations and joins at pitch; records 35/35, 19/19, 11/11, 52/52, finale 51/51. Movement I's new cello tremolo at its 122 checked against 223: the arrival stays distinct.
- Casanelles PDF 222: score title stamp now "draft v431" (was "v400, 27 October 2026"), bumped each version.
- Casanelles ch. 5 (PDF 219–220, 239, 245–248): cor anglais in the close at 273–279 tested and declined. No musical change.
- coherence/finale.md: header, records and open request brought to c430; scoring-rules note on movement I's 122 added.

## Cycle 431 (v431 → v432), lens 1, Adler brass melody
- Adler ch. 11 (PDF 28–29, Ex. XI-12 Schubert Rosamunde; PDF 30–32, Ex. XI-14): Tbn 1 now holds its F3 from 40 and plays F1's last fragment F–D–E♭–F with the cellos at 41–42, fading to p; Tbn 2 and the bass trombone still stop after 40. The score's first soft melodic trombone phrase; F1's notes unchanged.
- Checked, no change: high horn unisons, trombones on F1's head at 37–38.

## Cycle 432 (v432 → v433), lens 2, A&S chromatic voice leading
- A&S Unit 31 (PDF 563–564, Ex. 31-17; PDF 532, 537): bar 129 beat 4 is now minor iv6 (E♭–G–C) before V7 at 130, so the bass moves E–E♭–D (♮6–♭6–5): Vc `e4 es4`, Cb `e,4 es,4`, Hn 4 C4 on beat 4, harp LH's last note G4 (no E♮, no pedal change). Tune, the 123–130 hand-over and dynamics unchanged; a German sixth there was tested and rejected (C♯ against Bn 1's C4).
- Declined: voice swap at 146→147, ♭VII at 237, common-tone °7 at 39–42, swaps at 131–134.

## Cycle 433 (v433 → v434), lens 3, A&S phrase and V7
- A&S Units 6–8 (PDF 98, 100, 102 Ex. 6-19, 117): the long V7's seventh F now resolves down by step into the recapitulation at 151: Tbn 1 `es'2 c'2`, Tbn 2 `c'2 es2` (F–D to E♭–C in thirds, then exchanging), Bn 1 `es2 g,2`, Vc `<g, es>2 g,2` (all three had leapt away from F). F1, the G pedal, dynamics and the 4–3 and 6–5 at 151–153 unchanged.
- Checked, no change: bass octave leap to the 7th, root-position long dominant at 139–146, i6 at 11 and 166.

## Cycle 434 (v434 → v435), lens 4, Adler ch. 5 strings
- Adler ch. 5 (PDF 141, Ex. V-19; PDF 152): the cellos double Vln I an octave lower in the fall at 169–170 (`g,4 d'8( c' b aes g f | d2.)\p r4`), as at 41–42 (c344), instead of holding G2–B2 above the basses; G and B stay in basses and Bn 2.
- Checked, no change: the major F2 register at 187–198, the plagal close at 231–234, viola-over-violin crossing.

## Cycle 435 (v435 → v436), lens 5, MOLA parts
- MOLA PDF 5, Ex. 4; Adler part 2 PDF 299: part-only cues before five entries after long rests at 127–132 (Fl 1 at 129, Hn 1 at 127, Hn 3·4 at 129, Ob 1 at 131, timpani at 132); new \addQuote "clOne".
- MOLA PDF 8, Ex. 7: in the cor anglais and bass clarinet parts, line breaks before 235 (and 255 in the cor anglais) so letters P and Q each stand over their own rest. Score and MIDI unchanged; parts book 0 warnings.

## Cycle 436 (v436 → v437), lens 6, Rimsky ch. I
- Rimsky-Korsakov PDF 26 (highest notes on the lower strings in fourth position): Vln II's "sul G" at 255–257 now ends on 256's G4, so the ff C5–D5 at 257 are played on the D string. Marking only.
- Rimsky-Korsakov PDF 36 (clarinet leaps across the break): the soft held F5 at 103–104 moves from Cl 1 (just off an accented C4 at 102.4) to Cl 2, resting since 95; same sounding pitches.

## Cycle 437 (v437 → v438), lens 7, Adler ch. 16 transcription
- Adler ch. 16 (PDF 211–213, Ex. XVI-10 Dvořák; PDF 203, 230–231): the violas enter at 8 answering the cellos' F1-head figure a fourth higher and two octaves up (`g'2 d'4. es'8`), the E♭4 falling to their held D4 at 9 (6–5 over V); before, they entered at 9. Bars 1–6 and the other staggered entries at 9–10 unchanged.
- Declined: a late oboe answer at 19–26, moving the counter at 159–166, a rhythmic B♭ pedal at 83–86, a cello rhythm at 171–186.

## Cycle 438 (v438 → v439), lens 8, Casanelles dynamics
- Casanelles PDF 147–148 (two like instruments in unison sound like two players; use one or three or more): Vln I's exposed pp unison at 119 and 122 is now marked "4 soli" (was "2 soli", meant as two desks since c209). Text only; MIDI unchanged.
- Checked, no change: Ob 1 and Cl 1 unison at 107–110, repeated-note figures at 247–277.

## Cycle 439 (v439 → v440), lens 9, Beethoven 5 holistic
- Rimsky-Korsakov ch. IV (PDF 127 "Amplification", Ex. 248): at 9.1 horns 1–4, contrabassoon and basses now enter p < instead of mf, so the crescendo's second group grows from below rather than stepping up; entry order, violins' mf and the f at 10.3 unchanged.
- Beethoven 5/iv holistic comparison and v429 → v439 check: nothing worse. Declined: flute on the 4 soli at 119/122 (page 7 overfull), pizz. chords at 89–90.

## Cycle 440 (v440 → v441), lens 10, cyclic review
- Adler (adler2 PDF 188, 190–191, Ex. XV-36, XV-37): Tpt 1 now ends with the 216 diminuendo and rests at 217–218 (as Tpt 2 since v415), so the cor anglais and horns' echo of theme B has no trumpet a fourth above it; the held D♭ continues in Fl 1, Ob 1, Cl 1 and the violins; Tpt 1 re-enters on the 219 sub. p C5. Theme B, the D♭–C–B–C top line and 222→223 unchanged.
- Cyclic review against movement I v476, movement II v461 and scherzo v435: all quotations and joins at pitch; records 35/35, 19/19, 11/11, 52/52, finale 51/51. coherence/finale.md brought up to date (seven sentences).

## Cycle 441 (v441 → v442), lens 1, A&S rhythm and meter
- A&S Unit 3 (PDF 50, 52–54, Ex. 3-10, 3-11: a group ends on its tonal goal): F2's climax slur now runs from 59 to 63.1 (exposition, Tpt 1) and 179 to 183.1 (recapitulation, cor anglais and Tpt 1), so the deceptive V7→VI and V→i6 resolutions belong to the phrase; the breath moves to 63.3/183.3 and the last phrase starts with an upbeat. Fl 1's doubling ends on the downbeat. F2's notes unchanged; phrasing only.
- Declined: a 9–8 at 17–18/157–158, a dotted peak at 62.

## Cycle 442 (v442 → v443), lens 2, A&S added dissonance
- A&S Unit 27 (PDF 469–470, Ex. 27-10): the harp's second group at 72 no longer sounds the root B♭4 a seventh above the violas' 9th C4 in the B♭9 dominant (`f'8 aes'8 d''8 f''8`), as c352 did at 81.
- Tested and declined: a dominant ninth at 128 (cluster under Vln II's F♯4). Checked: the violas' 9th at 46.3.

## Cycle 443 (v443 → v444), lens 3, A&S III and VII
- A&S Unit 15 (PDF 236 Ex. 15-9; PDF 243–245): bar 16 beat 3 now sounds the full ii∅7 (D–F–A♭–C) as at 156.3: Cl 1 `aes'2( f'2)`, Cl 2 `f'2( c'2)` (the chord stood a quarter note as a bare diminished triad).
- Declined: ♮VII → IV6 → V at 16–18, III under the passing 7 at 69. Key plan and proportions checked.

## Cycle 444 (v444 → v445), lens 4, Casanelles spectral
- Casanelles PDF 272–273, 283–287 (sul tasto removes upper partials; a remembered, distant sound): the strings' held chord under the oboe's movement II recollection at 95–98 is now "sul tasto", with "ord." at each part's return (99 for Vla, Vc, Cb; 103 for Vln II). Text only; MIDI unchanged.
- Declined: stopped Hn 3·4 at 95–98. Checked: the receding returns of the second theme, theme B and the scherzo motive.

## Cycle 445 (v445 → v446), lens 5, Adler string notation
- Adler PDF 30, Ex. II-12 (double notes divided, every change written, "unis." for the return): violas at 95 now read "sul tasto, / div." and at 99 "ord., unis." (the "non div." from 91 was still in force under the soft chord). Text only.
- Tested and declined: measured-tremolo shorthand for the basses at 266–276 (MIDI would lose the pulse).

## Cycle 446 (v446 → v447), lens 6, Sebesky winds
- Sebesky ch. 2 (PDF 63, 70–72, 106: the oboe's lowest fifth is coarse; the cor anglais is not, and blends with the clarinet below): Ob 2's held inner line at 159–166 (ending E♭4, D4, E♭4) moves to the cor anglais, resting 151–170 before; same pitches, slurs and dynamics; the separate Ob 2 staff added in c135 is removed. Parts book 0 warnings.
- Tested and declined: Fl 1 instead of Cl 1 on the pp D6 at 121–122. Checked: 143–150.

## Cycle 447 (v447 → v448), lens 7, Rimsky overlaying
- Rimsky-Korsakov PDF 108 (soft horn-and-bassoon writing: concords and held notes to the horns, discords to the bassoons): in the off-beat chords under F1 at 13–15 and 21–23, Hn 4 now holds G3 and Bn 1 takes the seventh F3, resolving it to E♭3 on 15.2 and 23.2, so that C-minor chord gains its third (Hn 4's F3 used to rise to G3). 24–26, tune and bass unchanged.
- Checked: horns inside the 136–138 chain, 95–98, 101–106.

## Cycle 448 (v448 → v449), lens 8, A&S accent and hypermeter
- A&S Unit 3 (PDF 50–51, Ex. 3-6: a note entering on a weak beat and held over the strong beat is marked): accents on the IV chord entering on 272 beat 2 in Bn 1, Hn 3·4 and violas, held into the Largamente at 273. Notes, dynamics and tempo unchanged.
- Checked: the four-bar grid 11–264, accents and tempo words on it. Declined: accents in the 7–6 chain at 87–89 and on every downbeat at 265–272.

## Cycle 449 (v449 → v450), lens 9, Dvořák 7 holistic
- Rimsky-Korsakov PDF 130–131 (Ex. 262: a long crescendo adds instruments): the oboes join the cresc. molto at 245–246 on a sixth G5 over B4, p <, resolving into their own ff entry (E5 over C5) at 247, instead of entering ff from silence (new sHeadOboeTwo).
- Dvořák 7/iv holistic comparison and v439 → v449 check: nothing worse. Declined: percussion in the hammered tuttis.

## Cycle 450 (v450 → v451), lens 10, cyclic review
- Rimsky-Korsakov PDF 126–127 (a part taken over keeps the group's progression): Ob 2 at 245–246 now moves B4→C5 on 245.3 with Tpt 2 and Hn 1 (`b'2( c''2~ | c''1)`), so no B is held under the horn call's resolution; the oboes' crescendo into the 247 ff is kept.
- Cyclic review against movement I v490, movement II v474 and scherzo v443: all quotations and joins at pitch; records 35/35, 19/19, 11/11, 52/52, finale 51/51. coherence/finale.md updated (header, headings, open request). Declined: range relays at 245–246, 7–10, 222, 205–210.

## Cycle 451 (v451 → v452), lens 1, A&S melodic figuration
- A&S Unit 20 (PDF 332 Ex. 20-7a, PDF 336 Ex. 20-16): bar 69, a passing B♭1 on beat 4 fills the bass's C2–A♭1 third inside IV6 → IV (Cb, Bn 2, harp LH), a tenth under the tune's passing D6. Tune, counter-melody and dynamics unchanged.
- Declined: a passing bass at 77.4 (outer-voice fifths), a double neighbour in a main tune.

## Cycle 452 (v452 → v453), lens 2, A&S four-part writing
- A&S Unit 5 (PDF 76, 83) and Unit 21 (PDF 351, the 9–8 always has its 3rd): violas at 228–229 now `e2.( f4 | g1)`, so the canon's 9–8 at 229 has an E and the octaves A→G with Cl 2 at 228→229 are gone. Canon, chorale, bass, timpani and dynamics unchanged.
- Tested and declined: Cl 2's ninth leap at 228→229, Tbn 2's line at 151. Checked: hidden fifths and octaves in the outer voices.

## Cycle 453 (v453 → v454), lens 3, A&S V as key area
- A&S Unit 14 (PDF 215–220): V6/5 of V at 129 and a pivot chord at 114 tested and declined (the tune's G would rise, new octaves; the bare D7 is an accepted phrase modulation). V4/2 at 133–134 and the French sixth at 168 follow the reading. Proportions checked. No score change.

## Cycle 454 (v454 → v455), lens 4, Rimsky harmony
- Rimsky-Korsakov PDF 51, 82, 85–86 (balance at ff, no gaps, harmonic notes in the upper parts): the bass trombone plays C3 at 259–260 instead of doubling the tuba's F, so the iiø6/5's seventh C is heard in the brass (it was only in Ob 2) and the tenth above the bass is filled; it rejoins the tuba at 261.
- Rimsky-Korsakov PDF 90–91 (concords in a pair of like instruments): Fl 2 moves to F5 at 40–42, a third under Fl 1's A♭5, instead of a three-bar tritone D5.
- Kept: oboes' second and trombones' tritone at 259–260, Tpt 3 and violas doubling F, oboes at 40.

## Cycle 455 (v455 → v456), lens 5, Gould staves and clefs
- Gould PDF 21–23: score-only bass clef for Hn 3·4 at 255–258 (F2's last statement, down to C3 on four ledger lines), back to treble at 259, as at 25–26 and 79–82. Parts and MIDI unchanged.
- Checked, no change: single horn D3s at 13, 21, 29, 153, 161; clarinets' D3 at 178; basses' tenor clef at 27–34.

## Cycle 456 (v456 → v457), lens 6, Adler bowing
- Adler PDF 38, 42–43 (Ex. II-20) and PDF 54 (up-bow before pizz.): down-bows on the accented F at 113 in Vln I and II (matching c418's lower strings), up-bows at 114 in Vln II and violas before the pizz. at 115. Bow signs only.
- Considered and declined: viola div. at 101, "al tallone" at 91–94, a trill at 82, staggered bowing at 219–221.

## Cycle 457 (v457 → v458), lens 7, Sebesky basics
- Sebesky ch. 1 (PDF 12–13, Ex. 1): Bn 1 resting at 87–88 to clear the violins' scale tested and declined (weakens the 7–6 suspensions at 87.3 and 88.1). 187–194, 159–166, 153–158 and 67–74 checked. No score change.

## Cycle 458 (v458 → v459), lens 8, Sebesky focus
- Sebesky Ex. 269 (PDF 205, 207), Ex. 281 (PDF 215–216): the violas' and cellos' counter-melody at 74 swells to 74.3 and back to mp at 75 while the tune holds F5 (`bes4(\< aes4 f4\> g4~ | g2\! ...`); Hn 1 left as it was.
- Declined: a swell at 46–48 (protected violas), changes to F1's steady f, a swell at 119–122, matching 194 to 74.

## Cycle 459 (v459 → v460), lens 9, holistic comparison
- Bar 251 beats 1-2: the E-major chord had no G (E in 15 of 16 notes, E in the bass). Hn 4 now plays G3 to C4 instead of E4 to D4, which supplies the third near the bottom (Adler Ex. V-27, VIII-25). The two score-only force-hshift overrides at 251 were removed because the horns no longer share a note. Rejected alternatives: Hn 4 D4 to C4 (octaves with Ob 2) and a held G3 (contrary fifths into 252).
- Holistic comparison with Tchaikovsky 4/iv and v449 against v459: no change needed.

## Cycle 460 (v460 → v461), lens 10, cyclic review
- Sebesky PDF 19–20 (Ex. 3/3A, harmonic variety): at 270 beats 2–4 Bn 1 holds A3 and the violas D4 with Tpt 3's F4, ii7 over the C pedal, so 269–272 run I – ii7 – V – IV6/4 and no longer repeat 266's harmony; F1's notes, the horn and trombone rests and 266 unchanged. Cyclic review against movement I v506, movement II v493 and scherzo v453: all quotations and joins at pitch; records 35/35, 19/19, 11/11, 52/52, finale 51/51.

## Cycle 461 (v461 → v462), lens 1, Rimsky-Korsakov strings
- Rimsky-Korsakov PDF 58–59, 62 (a very high violin line wants an octave below): at 212–214 Vln II divides; the upper half plays theme B at Tpt 1's pitch, an octave under Vln I and the flutes, the lower half keeps the existing line (c051/c054); unis. at 215. Theme B's notes, the 205–223 dynamic path and the D♭–C–B–C top line unchanged.

## Cycle 462 (v462 → v463), lens 2, A&S cadential 6/4
- A&S PDF 152–160 (cadential 6/4): bar 82 now runs iv6 (beats 1–2), V6/4 (beat 3, the tune's G as 3̂), V (beat 4) into the E♭ cadence at 83; the low strings, Bn 2 and Hn 2 move to B♭ on beat 3 and Bn 1 falls A♭3–G3–F3, so the tune's G5 no longer clashes with A♭ over C♭. Hn 1's E♭–D becomes the held 4th falling to the 3rd. Tune, harp, dynamics, breaths and the 75–82 pad's instruments unchanged.

## Cycle 463 (v463 → v464), lens 3, A&S tonicization
- A&S Unit 26 (tonicization and key plan): no change. Tested an applied V6/5 of A♭ on 34.4 and declined it: it would turn the 26 and 34→35 V→VI chain that prepares the A♭ statement at 187 into a plain tonicization and lose the rest ending F1's bass statement. Key plan, arrivals in new keys and the long coda (accepted c219) checked.

## Cycle 464 (v464 → v465), lens 4, Rimsky-Korsakov brass and winds
- Rimsky-Korsakov PDF 110–111 (woodwind harmony above the trumpets): the oboes swap at 262–264; Ob 1 takes V7's seventh F5 and resolves it to E5, the tonic's third above the trumpets at the 263 fff, and Ob 2 takes the chorale line B4–C5 at the trumpets' pitch (it sat on E4 at fff). Progression, chorale top line, the seventh's resolution and the cut at 264.1 unchanged. Declined the critic's second change (Hn 3 C5 at 259–260): C5 over F to E♭4 over A♭ at 261 makes contrary fifths with the bass, the reason c190 gave against C–E♭ there.

## Cycle 465 (v465 → v466), lens 5, Gould beams
- Gould PDF 31–41 (beam slopes for closely spaced notes): a score-level `gould-close-slope` callback (after c375's `gould-max-slope`) keeps the shorter-stem end and sets close-spaced groups of three or four to a ½ slope (¼ when the outer interval is a second); 194 groups changed, the harp at 67–82 now has one slope throughout; the harp left hand at 123–130 is excluded (page 7 would overfill). Bar 222 Fl 1's beam is fixed at 9.25–9.75 in the score so it matches Vln I (the part keeps c195's offset). Notes, pages and MIDI unchanged; parts-book.ly still lacks the c285, c375 and c465 beam callbacks.

## Cycle 466 (v466 → v467), lens 6, Adler strings playability
- Adler PDF 73–74, 87 (open strings on held expressive notes): violas "sul G" at 8–10 (the c437 answering phrase's held D4 crescendo, 4th position) and at 133–134 (the held D4 fading to p, as c391 did at 41–42 and 169–170). Text only; MIDI identical.

## Cycle 467 (v467 → v468), lens 7, Sebesky strings
- Sebesky PDF 140, 144–146, 166 (cellos on a counter line, not just doubling the bass): at 125–128, after their F2 solo, the cellos join Bn 1's dolce counter line at pitch, pp (E3–F♯3–G3 | C4–D4–A3 | A3–B3–C4 | A3), back on the bass at 128.3; the basses keep the roots. Answers c367's decline: the hand-over's order and notes, the harp, the instruments present and the 129–131 bass (c432) are unchanged.

## Cycle 468 (v468 → v469), lens 8, MOLA dynamics
- MOLA PDF 7–8, Ex. 6–7 (page turns, long changes as words): at 143 Tbn 1·2 and the bass trombone take "cresc." instead of a hairpin, like every other part in the build (c268, restated after the turn by c405), so page 8 no longer opens with an unlabelled wedge fragment. Notes and MIDI unchanged.

## Cycle 469 (v469 → v470), lens 9, holistic comparison
- Holistic comparison with Mozart 41/iv (Adler part 2 PDF 175–178): the coda's theme combination follows the Jupiter model (themes heard alone first, fixed colours, tonic–dominant pedal); no change. Tested and declined a pp timpani roll on B♭ at 43–46 (blurs the new colour two bars after the 39–40 roll and the c264/c276 overtone chord). v459 → v469 checked: nothing got worse.

## Cycle 470 (v470 → v471), lens 10, cyclic review
- A&S Unit 23 (PDF 387–388, Ex. 23-2; PDF 395 Points 2a, 3, 5–6): 242 is iiø7 (D–F–A♭–C) before III♯; Hn 4 A3–A♭3–G♯3–G3 (♮6–♭6–5), harp G♯ (pedal text at 241). Tune, bass and the approach by II unchanged. Cyclic review against movement I v519, movement II v508 and scherzo v461: all quotations and joins at pitch; records 35/35, 19/19, 11/11, 52/52, finale 51/51.

## Cycle 471 (v471 → v472), lens 1, Rimsky-Korsakov brass
- Rimsky-Korsakov PDF 64–80 (brass): no change. Tested and declined the bass trombone joining Tbn 1·2 on F1's head at 247–254 (thickens the band above the C2 pedal that c072 cleared, weighs against the S head in Hn 1·2 and spends the bass trombone's fresh ff entry at 255). Tpt 1 f under the ff woodwinds at 247 confirmed (Rimsky's note to Ex. 75).

## Cycle 472 (v472 → v473), lens 2, A&S supertonic seventh
- A&S PDF 173, 177, 179 (II6/5; the seventh held as the 4th of the cadential 6/4): at 249 Hn 4 plays C4 instead of doubling the bass F3, holds it into the 6/4 and falls to B3 on 250.3, so 248–250 run ii7 → ii6/5 → 6/4 → V7 and the F3–E4 seventh leap is gone. Corrects c382's reading of 248–249. Themes, the combination's lines and the c374 spacing unchanged.

## Cycle 473 (v473 → v474), lens 3, A&S chromatic plans
- A&S Unit 32 (chromatic voice leading and large-scale plans): no change. Tested and declined a voice exchange putting F in the bass at 242 (parallel fifths 242.3→243.1, and a third F-bass ii in nine bars) and Vln I resolving F♯5 to G5 at 115 (Vln II already takes G5; the slur would cross the page turn into the bassoon solo). Proportions timed from the MIDI: coda 31% (accepted c219); its slow (211–246) and fast parts are now about equal in length.

## Cycle 474 (v474 → v475), lens 4, Rimsky-Korsakov tutti
- Rimsky-Korsakov PDF 505–507, Ex. 209 (held tutti chords with timpani take a roll): at 167–168 the timpani's single A♭ stroke under the link chords becomes a roll fading f > p (`aes,1:32\f\>~ | aes,2:32~ aes,4:32\p r4`), as at the matching link 39–40 and the other augmented sixths over A♭ (5, 219, 261). It ends before the horns fade, so c108's diminuendo order holds; 166 and the soft sticks at 171 unchanged.

## Cycle 475 (v475 → v476), lens 5, Gould rests
- Gould PDF 50–51 (rests on shared staves sit inside the staff below the middle line): score.ly sets `Rest.voiced-position` to 2 for whole and half rests (shorter rests keep c295's default) and `MultiMeasureRest.voiced-position = #2`, so the second player's rests no longer hang at or below the bottom line (e.g. Fl 2 and Ob 2 at 217–218); LilyPond still moves a rest out when a note collides. Pages 2–4, 6, 11–12, 15–16 change; no system or page moved; MIDI identical.

## Cycle 476 (v476 → v477), lens 6, Adler harp
- Adler PDF 111–112 (the harp's two lowest strings have no pedal and are tuned by hand): since v404 the harp plays D1 at 76, so a text "low D string (D1): tune D♮" now stands at the harp's first entry, 43, with the starting pedal setting, in score and part. Notes and MIDI unchanged. Tested and declined a wider harp chord at 132 (page 7 overfills).

## Cycle 477 (v477 → v478), lens 7, Adler woodwind combinations
- Adler PDF 255–257, 271–272 (vary the third statement; imitation between winds; enclosed voicing): at 105–106 Ob 1 enters a beat later and follows Fl 1 and Cl 1 in canon at the octave between their F6/F4, ending on F5 at 106.4, so the scale figure's third statement is no longer the same block as 101–102. Answers c377: 15 bars from 89–90 and a different shape (two leaders, one follower). Only Ob 1 changed.

## Cycle 478 (v478 → v479), lens 8, Adler woodwind articulation
- Adler PDF 187, 199 (Ex. VII-34; keep the slur to the phrase's end): Ob 1's motto tail E♭5–D5–D♭5–C5 at 95–97 is now one slur to the C5, which was re-tongued on 97.1 before Cl 1 takes it over at 97.3; this matches movement II's source tail (Cl 1, II 85–90). Notes, dynamics and MIDI unchanged.

## Cycle 479 (v479 → v480), lens 9, holistic comparison
- Holistic comparison with the Eroica finale (Adler part 2 ch. 16): no change; the movement follows its plan (off-tonic ff opening, brass apotheosis at 223, fast coda, the opening scale returning at 263–264). Tested and declined timpani strokes accelerating into 247 in place of the G roll at 246 (repeats 143–146's figure and cuts the roll's crescendo). v469 → v479 checked: nothing got worse.

## Cycle 480 (v480 → v481), lens 10, cyclic review
- A&S Unit 28 (Neapolitan): no change. Tested and declined a Neapolitan 6/4 in place of the French sixth at 168 (a second ♭II five bars after 163, a D♭5–D5 cross-relation on top, and it loses the A♭/F♯ sixth that ties the passage to 1 and 219). Cyclic review against movement I v534, movement II v525 and scherzo v471: all quotations and joins at pitch; records 35/35, 19/19, 11/11, 52/52, finale 51/51; the scherzo's new Vln I G♯5 → G5 at 1–7 recorded (movement I's 78–79 has those pitches in Cl 1, then Ob 1 and Vln I).

## Cycle 481 (v481 → v482), lens 1, Adler strings
- Adler ch. 3 (strings): no change. Tested and declined a single solo violin at 119 and 122 (covered by Vln I an octave lower; reverses c209/c438) and a solo cello at 123–124 (masked by the harp; thinner than the violas that follow).

## Cycle 482 (v482 → v483), lens 2, A&S 5-6 sequences
- A&S PDF 267–277 (5–6 motion against parallel fifths): at 239–240 the tune's E over A moved to C over F, outer-voice fifths on two downbeats (par8 flags all four tune parts). The bass (Vc, Cb, Bn 2, harp LH) now holds A over the bar line and moves to F on 240 beat 2, so Bn 1's E3→F3 becomes a 5–6 over A (IV6 at 240.1) and the outer voices run 5–10–10. Tune, counter-line and the A–F–D bass unchanged; answers c032/c212/c302, whose reason (the tune is movement I's) covered only the tune.

## Cycle 483 (v483 → v484), lens 3, Rimsky-Korsakov tutti
- Rimsky-Korsakov PDF 120, 127, 130, 136 (no tutti at p; a new group enters pp and crescendos; brass join a crescendo last): the tuba rests 217–220, where it only doubled the contrabassoon and basses under the sub. p, and re-enters pp < on G1 at 221 with the allargando, mf < at 222, fff at 223. Bass pitches, the sub. p at 219, the stop chord and 222→223 unchanged; resting the tuba until 223 was tested and declined.

## Cycle 484 (v484 → v485), lens 4, Adler scoring examples
- Adler part 2 PDF 147–148, 154 (background distinct from the tune): at 255 Tbn 1·2 enter mf instead of f on G3/E3, the very notes F2's last phrase starts on and returns to in violas, cellos and Hn 3·4 ff; their crescendo from 257 to ff at 259 is unchanged. Notes unchanged.

## Cycle 485 (v485 → v486), lens 5, Gould spacing
- Gould PDF 55, 65–67 (centred bar-length notes; crossing voices on a shared staff): at 68 Bn 1's crossing B♭2 semibreve is printed as tied up-stem halves set to the right of Bn 2's D3 (part keeps `bes,1`), and at 69 Bn 2's dotted half is shifted clear; c215's `\cen` is removed at 97 and 138 (no longer bar-length in every part) and added at 5. Score-only; MIDI identical.

## Cycle 486 (v486 → v487), lens 6, Adler woodwind playability
- Adler PDF 175, 188, 192, 230 (wind endurance; second player relieves the first; contrabassoon rests): Fl 2 takes Fl 1's B♭5 at 37–38 so Fl 1 breathes (back on B♭5 at 38.3; sound unchanged, Fl 2 still rests 35–36); the contrabassoon rests 205–208, where it only doubled the tuba and basses' A♭1, and re-enters f < at 209; staggered bassoon breaths after 241 (Bn 1) and 242 (Bn 2).

## Cycle 487 (v487 → v488), lens 7, Rimsky-Korsakov doublings
- Rimsky-Korsakov PDF 74–80 (unison doublings): no change. The critic proposed Bn 2 on F2's last phrase at 255–256 (strings and horns alone do not blend, PDF 79); declined, because the woodwinds' rest at 255–256 and fresh entry at 257 (since v130, kept by c486) was not answered. Other doubling checks (205–206, 211–218, 247–254, 107–109) pass.

## Cycle 488 (v488 → v489), lens 8, Adler brass expression
- Adler PDF 304–305 (Ex. X-8, X-12: horns on a passionate unison marked espress.): Hn 3·4 now carry "espress." with their ff at 255, like the strings on F2's last phrase (marked on both horns so it prints once over a2, as c138 found at 217). Text only; MIDI identical. Phrase slurs on the brass chorale considered and declined (repeated common tones would read as ties; 223–234 protected).

## Cycle 489 (v489 → v490), lens 9, holistic comparison
- A&S PDF 585–586 (Ex. 32-3, a common tone held across a chromatic key change): Hn 4 now ties A♭3 into G♯3 at 242→243 (iiø7 → E major) instead of breathing and re-striking it; its breath moves to after 240, with Hn 3 breathing and crescendoing there too. No pitches changed. Holistic comparison with Sibelius 2/iv and v479 → v489 check: no further change.

## Cycle 490 (v490 → v491), lens 10, cyclic review
- Adler part 2 PDF 264–274 (keep the accompaniment away from a soft soloist's register): Cl 2 and Tpt 3 end with the 216 diminuendo and rest 217–218, as Fl 2, Ob 2, Tpt 1·2 already do, so nothing holds F4 on or a half step under the cor anglais and Hn 1·2 echo of theme B; they return on the 219 chord. Cyclic review against movement I v549, movement II v543 and scherzo v481: all quotations and joins at pitch; records 35/35, 19/19, 11/11, 52/52, finale 51/51.

## Cycle 491 (v491 → v492), lens 1, Adler woodwinds
- Adler ch. 7 (woodwinds): no change. Tested and declined the bass clarinet doubling the cellos' F1-head entry at 140–143 (its staff would appear on page 7, which then overfills; the cello tone would predominate anyway, PDF 226). Register and dynamic scans of all woodwind parts pass.

## Cycle 492 (v492 → v493), lens 2, A&S mixture
- A&S PDF 374, 387–388, 395 (Ex. 23-2d, ♭6 colours ii7 and falls to 5): bar 38's chord before the E♭-minor cadential 6/4 is now iiø7 (F–A♭–C♭–E♭) instead of ii7 with C♮, so the bar no longer mixes the major sixth with the minor third that follows; every C♭ falls to B♭ (Vln I·II, violas, Bn 1, Ob 1·2, Cl 2, Tbn 1·2; Cl 2 C♭4 then B♭3–D4 eighths on beat 4). Bass, F1's head, dynamics and 39–42 unchanged.

## Cycle 493 (v493 → v494), lens 3, A&S 6/4 chords and form
- A&S PDF 256–258, 309–310, 324 (passing 6/4, stepwise bass): at 195–196 the bass no longer holds C♭ for the whole bar and leaps to G; it runs C♭–B♭–A♭–G–A♭ (Cb, Bn 1), with Hn 1's A♭–G–A♭ neighbour and Bn 2 on E♭2, matching c403's 75–76 a third lower; removes the Bn 1/violin octaves at 195.4→196.1. Tune, cellos, violas, Hn 2, dynamics and 197–198 unchanged; answers c403's skip (works in minor; no instrument added).

## Cycle 494 (v494 → v495), lens 4, Adler percussion
- Adler part 2 PDF 184 (crescendo rolls start p): the timpani's A♭ roll at 209–210 is now fp < (was f <) under the woodwinds' fp < (c216), so it no longer fills their dip and has room to grow into the ff at 211, as at 149 (c346) and 167–168 (c474).

## Cycle 495 (v495 → v496), lens 5, MOLA score layout
- MOLA PDF 5–6 (explain non-standard notation in the score): page 1's header now keys the one-line percussion stave ("⊗ above the line = crash cymbals (pair); ● below the line = bass drum"), which the part has had since c255. Header text only; MIDI and pages 2–16 identical.

## Cycle 496 (v496 → v497), lens 6, Adler brass
- Adler adler1 PDF 292, adler2 PDF 8 (brass need rests): Tbn 1·2 and the bass trombone held whole notes 211–228 (about 33 s) and sat on F3/D♭3 just under the cor anglais and Hn 1·2 echo at 217–218; they now end with the 216 diminuendo, rest 217–218 and re-enter p at 219, as the tuba and Tpt 3 do. The chord stays complete (F in strings, Bn 2, Cbsn; D♭ in violins, violas, woodwinds); dynamics, 222→223 and the chorale unchanged.

## Cycle 497 (v497 → v498), lens 7, Adler brass in combination
- Adler part 2 PDF 41–44 (brass in modern scoring): no change. Tested and declined short brass strokes on 2 and 4 at 207–208 (no gaps in the head to fill; drifts back to 199–204's hammered texture) and Hn 3 on the chromatic counter-melody at 239–242 (undoes c247 and drops the F chord's held fifth).

## Cycle 498 (v498 → v499), lens 8, A&S suspensions
- A&S PDF 348 (a dissonant suspension leans; its resolution is softer): the violas' held C♭4 at 49 (♭9 of V7 of E♭ over the B♭ pedal) now has a diminuendo into its B♭3 on beat 3. Notes, the pp level and the poco rit. unchanged.

## Cycle 499 (v499 → v500), lens 9, holistic comparison
- Holistic comparison with Elgar 1/iv; Casanelles PDF 271–273 (distance is a different sound from soft playing in place): under Ob 1's recollection of movement II at 95–98 the held string chord is played by the back desks only ("last 2 desks" Vln II, Vla, Vc; "last desk" Cb), "tutti" at 99 (Vla, Vc, Cb) and 104 (Vln II); c444's sul tasto kept. Text only; MIDI identical. v489 → v499 checked: nothing got worse.

## Cycle 500 (v500 → v501), lens 10, cyclic review
- Adler part 2 PDF 264, 274 (accompaniment away from a soloist's register): Bn 1 rests 217–218 instead of re-attacking A♭3 with the first note of the cor anglais and Hn 1·2 echo of theme B; harmony, the D♭–C–B–C top line and the dynamics unchanged. Cyclic review against movement I v564, movement II v560 and scherzo v488: all quotations and joins at pitch; records 35/35, 19/19, 11/11, 52/52, finale 51/51.

## Cycle 501 (v501 → v502), lens 1, Sebesky lines
- Sebesky PDF 209, 211 (Ex. 276, 279: contrary motion between lead and bass): at 85 the bass no longer rises with F1's head in parallel sixths; cellos and basses play B♭–B♭–A♭–F (F1's own bar-13 bass shape), and the violas' last eighth is A♭4, taking the seventh and resolving it to G4 at 86. Tune, the I6 at 86 (c143) and dynamics unchanged; answers c187's unexplained do-not-touch on 83–86.

## Cycle 502 (v502 → v503), lens 2, A&S applied dominants
- A&S PDF 419–423 (Ex. 25-11a: over 6–5 in the bass, the chord is almost always V4/3 of V): at 89 the last 7–6 of the closing bridge resolves to A♮3 (violas, Bn 1), so the bridge ends V6 – 7–6 into V4/3 of V – V7 – I; Bn 1 passes B♭–A♭ into G3 at 90; Hn 1 F4 and Hn 4 F3 on 89.2 so no horn doubles the leading tone. Bass, violin and wind figures, dynamics and the 90 cadence unchanged; every earlier change in 87–89 (c053, c061, c062, c143, c377) kept.

## Cycle 503 (v503 → v504), lens 3, A&S 6/3 chords
- A&S Unit 18 (6/3 chords and form): no change. Tested and declined a chromatic 6/3 (B bass) at 198.3–4 into the C-minor tutti at 199 (leading tone in three octaves before the tonic; loses c294's A♭-minor turn; the root-position A♭ is the stronger close). Proportions and coda stages checked.

## Cycle 504 (v504 → v505), lens 4, Adler woodwind spacing
- Adler PDF 257–258 (Ex. VIII-25 to 27: widest gap just above the bass): Bn 2 holds D3 through 85 (it held B♭2 a whole tone above the basses' A♭2 after c501's new bass), and plays B♭2 instead of G2 at 192 (left from the old G bass that c262 replaced with E♭2), stepping to A♭2 at 193 as before.

## Cycle 505 (v505 → v506), lens 5, Adler score layout
- Adler part 2 PDF 291–292 (space between choirs must be discernible): c325's nested horn, trumpet and trombone StaffGroups made the gap below the lowest playing brass staff collapse to a within-family gap (37–50, 67–86, 171–178). The brass StaffGroup now draws the same brackets with `systemStartDelimiterHierarchy`, so the choir gap holds below whichever brass staff is lowest (65, 81–82, 55 px); every other gap and all 16 pages unchanged; MIDI identical.

## Cycle 506 (v506 → v507), lens 6, Adler timpani
- Adler part 2 PDF 58, 79 (timpani strengthen the tonic; Ex. XII-46): at 99, where the development starts f in F minor, the timpani play F2 (the 30" drum has been on F since 95, c416) instead of the old bass note C3, so the F-minor area has a timpani F at its first bar and at its cadence (113). 103, 111 and the retuning marks at 95 and 114 unchanged.

## Cycle 507 (v507 → v508), lens 7, Adler accompaniment
- Adler ch. 5 (accompaniment and counter-melody): no change. Tested and declined lower strings alone under Ob 1 at 95–98 (Vln II resting, divided cellos: too close above the bass, two players per note); cellos imitating F2's head at 75–76 and violas/cellos in thirds or sixths at 71–74 worked out on paper and declined.

## Cycle 508 (v508 → v509), lens 8, Rimsky-Korsakov dynamics
- Rimsky-Korsakov PDF 129, Ex. 253 (sf-p: the strings attack, the dip must be audible): at 149 the strings now play sfp < into ff at 150 with the 21 wind, brass and timpani parts (c226, c346, c408), instead of holding ff through the bar in the same registers as the wind chord. Notes, ties, bowings and Tpt 1·2's ff strokes unchanged; answers c408 (the strings still give the attack).

## Cycle 509 (v509 → v510), lens 9, holistic comparison
- Holistic comparison with Brahms 2/iv; Rimsky-Korsakov PDF 54–68 (melody doublings): no change. Tested and declined Vln II an octave below Vln I at 265–268 (lands on the trumpets' F1 head at C5 and blurs the two themes). v499 → v509 checked: nothing got worse.

## Cycle 510 (v510 → v511), lens 10, cyclic review
- A&S PDF 586–587 (Ex. 32-3: the common tone linking two keys held in an exposed voice): Fl 2 keeps F5 on 242 beats 1–2, then takes A♭5, holds it as G♯5 into 243 and falls to G5 on 243.3 with Vln I's upper desk, so the A♭ = G♯ link into the E-major chord sounds high, at bar 1's pitch, not only in Hn 4. Cyclic review against movement I v578, movement II v576 and scherzo v498: all quotations and joins at pitch; records 35/35, 19/19, 11/11, 52/52, finale 51/51.

## Cycle 511 (v511 → v512), lens 1, A&S suspensions in melody
- A&S PDF 352 (Ex. 21-12: do not sound a suspension's resolution elsewhere before it resolves): at 81 the harp's first eighth is G4 instead of F4, which had sounded the tune's resolution under its held G (c398 removed the same F from Hn 2); c352's no-B♭ rule holds and no pedal change is needed.

## Cycle 512 (v512 → v513), lens 2, A&S augmented sixths
- A&S PDF 522–523 (Ex. 29-37: an augmented sixth in place of the dominant at a cadence): at 22's last beat the bass falls D–D♭–C (cellos, basses, Bn 2, Cbsn; violas and Hn 3 adjusted), so the consequent's V4/3 becomes a French sixth on D♭ resolving to C minor at 23 instead of repeating the antecedent's V4/3–i at 14→15. Melody and the recapitulation's 162–163 unchanged; no root-position V–I in C added.

## Cycle 513 (v513 → v514), lens 3, Adler form
- Adler part 2 ch. 15, 17 (form, soloist entries, heterophony): no change. Tested and declined Haydn's device at 269–270 (flutes doubling the head-rhythm figure two octaves up: already audible ff in Hn 3·4, violas, Bn 1, and a C6/B♭5 second on 270.1). Proportions, break-offs and soloist entries checked.

## Cycle 514 (v514 → v515), lens 4, Adler brass balance
- Adler part 2 PDF 14–18, 37–54 (brass balance by units): no change. The critic proposed Hn 3 F4 instead of D4 in the stop chord at 222 to strengthen its F; declined, because the Hn 1/Hn 3 voicing at 222 is an accepted part of the protected 216–223 approach and the stop chord is the movement's most guarded bar. Other balance checks (92, 247, 247–254, 265–268, 213) need no change.

## Cycle 515 (v515 → v516), lens 5, Gould octave signs
- Gould PDF 44, 46–48 (an octave sign only where it saves ledger lines): the harp left hand's 8 bassa line now ends after 240 (where it still saves ledger lines for A1 and F1), and the D2–D3 octaves at 241–242 are written at pitch on the stave instead of a ledger line above it. Notes and MIDI identical.

## Cycle 516 (v516 → v517), lens 6, Adler ranges
- Adler part 2 PDF 8, 306 (the tuba needs the most breath; F1 at the chart's bottom): a tuba breath after 254, where the second-theme head ends and the bass trombone enters on the same E2, so the tuba no longer plays 251–258 ff (about 11 s) without a break. Notes and MIDI unchanged. Range, terms, timpani and harp checks pass.

## Cycle 517 (v517 → v518), lens 7, Adler combination
- Adler part 2 PDF 178–179, 184 (each combined line needs a string, a woodwind and a brass colour): at 212–214 the cellos leave the bass and play Bn 1's counter line under theme B at pitch, f, with its slurs (with Hn 3·4), back to F3 at 215; the bass stays in the basses, Bn 2, Cbsn, bass trombone and tuba. Theme B, the dynamics, Vln II and violas unchanged.

## Cycle 518 (v518 → v519), lens 8, Adler bowing
- Adler PDF 38–39 (crescendo on the up-bow, strong notes down-bow; no phrase slurs in string parts; fewer notes to a bow at f): at 211–214 Vln I changes bow on its tied G♭6 at the Largamente barline, so it bows theme B with Vln II and the violas (212 up-bow crescendo, 213's ff peak down-bow, D♭6 a fresh down-bow); the cellos' copy of Bn 1's breath slur at 212–213 becomes one bar per bow. Bn 1 and Hn 3·4 keep their slur; pitches, dynamics and MIDI unchanged.

## Cycle 519 (v519 → v520), lens 9, holistic comparison
- Rimsky-Korsakov PDF 83 (never double the bass of an inverted dominant in an upper part): in the soft horn pad at 101–102 and 105–106 Hn 2 no longer doubles the leading tone; it holds the chord's seventh a sixth below Hn 1 (B♭3–C4–B♭3; E♭4–F4–E♭4). Hn 1's neighbour line and c247's neighbour chord kept. Holistic comparison with Schumann 4/iv and v509 → v519 check: no further change.

## Cycle 520 (v520 → v521), lens 10, cyclic review
- A&S Unit 26 (diatonic modulation): no change. Tested and declined a pivot chord (i6 of C) at 114 (sounds the home tonic mid-development and anticipates 121–122's Phrygian approach to D); declined tonicizing the falling-thirds bass at 123–127 (each applied chord contradicts F2).
- Cyclic review against movement I v592, movement II v594 and scherzo v509: all quotations and joins at pitch; records 35/35, 19/19, 11/11, 52/52, finale 51/51. finale.md updated for the scherzo's held opening G♯5 (c499) and closing Vln I G♯5 from 364.3 (c500), and movement I's soft horn-call recall at I 125–126 (c581).

## Cycle 521 (v521 → v522), lens 1, cellos on F1's head at 205–206
- Adler ch. 11 (brass melodic presentation; Ex. XI-13, horns with lower strings on a tune): the cellos join F1's head at 205–206 (A♭3, f, with the four horns, Tbn 1·2 and Bn 2) and return to the A♭2 pedal at 207; the pedal stays in the bass trombone, tuba and basses.
- Declined: Tbn 1 doubling the last chorale top line an octave lower at 255–263 (thins chord tones in the protected final approach). Checked, no change: loud high horn unisons (none above A♭4 concert) and a Lohengrin-style hand-over (231–234 protected; 211–218 already does one).

## Cycle 522 (v522 → v523), lens 2, chromatic voice exchange at 189
- A&S Units 30–31 (chromatic voice exchange, Ex. 31-17/31-19; French sixth as V7♭5 4/3): bar 189, inside IV of the recapitulated F2, the bass (Cb, Bn 2) falls F–F♭–E♭–D♭ against the counter-melody (Vc, Bn 1) rising D♭3–D3–E♭3–F3 (m6–A6–P8–M10, French sixth on beat 2, passing 6/4 at the octave); Cl 2 to A♭3 after beat 1, Cl 1 D♭4→D4. F♭ resolves to E♭. The basses use the C extension at 189 (E♭1, D♭1); header note updated. Tune, dynamics, bowing and scoring unchanged.
- Checked, no change: m6–M10 exchange at 146→147 (c432's reason holds), common-tone °7 at 24–25 and 39–42 (c342), augmented triads at 72 and 93.4 (c252); 92, 273, 129, 135–138 and the C–A♭–E key plan follow the reading.

## Cycle 523 (v523 → v524), lens 3, V4/2 at 58 and 178
- A&S Units 6–8 (V7 and its inversions; Ex. 8-8 V4/2 with the 7th resolving in the bass; Ex. 7-7 hidden octaves): at the joins of F2's minor statements, 58→59 and 178→179, the 7th moves into the bass on beat 4 (V4/2 → i6), as at the major statements 74 and 194. Bar 58: pizz. cellos and basses add A♭ on beat 4, falling to G♭ at 59; violas F3–B♭3. Bar 178: basses add F1 on beat 4 after motive x; violas end D3–G3. Removes the violas' unresolved A♭ at 58 and the hidden octaves at 178.
- Checked, no change: the held 7th on 58.1/178.1 (c413's protected 7–6), proportions and the coda's stage order.

## Cycle 524 (v524 → v525), lens 4, violins' scale an octave higher at 263–264
- Adler ch. 5 (Haydn saves the octave transposition for the end, PDF 129; crescendo by added octaves, PDF 137): after the last cadence, Vln I·II play the bar 3–4 scale figure an octave higher at 263.2–264 (G6–B5, up to G6, ending on G5), above the held fff wind and brass chord instead of inside it, so the opening scale returns at 263–264 an octave higher in the violins. Vln I's C6 on 263.1, the violas' G4–B3, the Vln I+II pairing and the cut at 264.1 kept; top note G6, C7 still only at 223.
- Declined: violas with Vln II on F2 at 75–76; bass drop-outs at 97–98 and 171–178. Checked, no change: the B doublings at 129, the combination passages 247–254 and 265–272.

## Cycle 525 (v525 → v526), lens 5, MOLA parts: rest widths at lettered tempo changes
- MOLA second pass (parts only; score MIDI, pages and analysis unchanged): a new `\ltRest` (called from `\lt`) widens a multi-bar rest that starts at a lettered tempo change to its text plus 10 staff spaces, and `\partNoBreak` before D keeps 51 off a line start, so letter E no longer sits on "Poco meno mosso" (51–67) and A no longer on "Allegro con fuoco" (1–11); Ob 1's stray "1." at 187 is score-only; the running header skips page 1; a part-only minimum hairpin for the bass trombone at 149; harp system padding 0.5 keeps it at 2 pages with the turn after 122. Parts book 0 warnings, 65 pages, page turns unchanged.
- Tested, not applied: widening the harp's rest at 205 (over-full page).

## Cycle 526 (v526 → v527), lens 6, woodwind breath at 146
- Rimsky-Korsakov ch. I (wind breathing, PDF 37, 44; wide clarinet leaps, PDF 36): Fl 1, Ob 1, Cl 1 and Bn 1 breathe after the staccato B at the end of 146, with the brass, contrabassoon and bass clarinet, ending a 14-second unbroken stretch from 141 and giving Cl 1 time before its leap to the ff G5 at 147. Marking only; MIDI unchanged.
- Tested and declined: cellos an octave lower at 35–36 (B♭4 above Rimsky's limit, but lower they lose the A-string tone, sit inside the held brass and leap into 37). Checked, no change: horn dynamics at 219–222 (p–mf, protected), ranges, divisi, harp, timpani and percussion.

## Cycle 527 (v527 → v528), lens 7, Hn 3 rests under the solo horn at 139–140
- Adler ch. 17 (solo horn; the orchestral horns rest while the soloist plays, PDF 264; accompaniment kept out of the soloist's register, PDF 274): Hn 3 rests 139–140 under Hn 1's solo F1 head, where its held D4 sounded the head's D4 and sat inside its descent (the clash c174 fixed at 143–144), and re-enters p < open on D4 at 141. Hn 4 still opens its stopped A♭3 to G3 (c088, c172) and restates p < at 141. Bar 138, 143–150 and 222→223 untouched.
- Checked, no change: bassoon solo against the solo violins at 119–122. Declined: Haydn's oboe doubling at 191–194, a timpani link at 74 (would pre-empt motive x at 178), a held horn tonic at 115, heterophonic oboe at 187–190.

## Cycle 528 (v528 → v529), lens 8, no change
- Adler part 2 (dynamics and colour in combination, PDF 37–40, 187–196): no change. Tested and declined a timpani A♭ roll crescendo at 198→199 (adds a 17th page, duplicates the device at 209–210, and spends the timpani's held-back colour before their ff entry at 199); declined soft strings overlapping the ff cut at 113→114 (c228, c328). Checked, follows the reading: the stop chord at 138, 149–151, 234→235, the mixed f/ff at 166, the horn call at 243–246.

## Cycle 529 (v529 → v530), lens 9, holistic comparison (Dvořák 8)
- Holistic comparison with Dvořák 8/iv, plus a v519 → v529 check (Rimsky-Korsakov Ex. 130–209; prose PDF 100–123): at the soft end of the staged diminuendo, Cl 2 holds B♭3 with Hn 2 from 38.4 to 41 (was D4, inside the horn pair and in unison with Bn 1; Rimsky PDF 106, 108). The C♭→B♭ resolution at 38 (c492) is kept and the held B♭3 makes no octaves with Ob 1 or Tbn 2.
- Declined on paper: Hn 4 resting at 139–140 (c527's reason holds), trumpets out of the plagal close at 231–234 (protected). Not reopened: trills, a muted brass pad, a soft cymbal (c321, c329, c429). Cycles 519–527 rechecked in the pages and MIDI: nothing got worse.

## Cycle 530 (v530 → v531), lens 10, cyclic review
- Cyclic review (Sonic Design reading; team-shared themes and current records): no score change. Against movement I v607, movement II v600 and scherzo v520: all quotations and joins at pitch; records 35/35, 19/19, 11/11, 52/52, finale 51/51; cyclic rules hold. finale.md stamps brought up to date (scherzo v510–v520 changes listed, none touching a quoted bar), and movement II's last tail at 95–97 added as item 16 under movement II.
- Tested and declined: copying the scherzo's flute-to-violin G♯5 hand-over at 242–243 (Fl 2 stopping at the barline leaves the G♯ link too weak under the horn call's ff; c510's reason holds).

## Cycle 531 (v531 → v532), lens 1, no change
- A&S Unit 3 (rhythm and metre): no change. Tested and declined a violin G–B upbeat at 18.4 and 158.4 into F1's consequent (weakens the f wind entry after the silence, turns the downbeat head into an upbeat group, adds parallel octaves). Declined on paper: an anticipation at 17.4→18 (c441), a lengthened C at 70. Checked, follows the reading: F2's climaxes at 62 and 78, F1's rhythm against the metre, the chorale's broader last statement (56 → 44 main notes a minute).

## Cycle 532 (v532 → v533), lens 2, oboes resolve the dominant ninth at 10
- A&S Unit 27 (the dominant ninth; its typical 6–5 resolution over V, Ex. 27-5, 27-6b): on the f stroke at 10.3 the oboes resolve the V7♭9 top: Ob 1 A♭5→G5 (was a leap to F5, leaving both the ninth and the seventh unresolved), Ob 2 D5→F5, so the stroke keeps the seventh and is still a full V7. Same 6–5 as F1's head at 11–12. The staged entries at 9–10 (v280), with the V7♭9 top on 10.1, are unchanged.
- Declined: II7 over the pedal at 7–8, an applied ♭9 at 36.4, V♭9 of IV at 235.4 (protected, clashes), an A♭ neighbour at 133–134 (pre-empts 135, c259).

## Cycle 533 (v533 → v534), lens 3, complete V6/5 at 176
- A&S Unit 15 (III, VI and VII; avoid root-position vii° with the seventh doubled, use V6/5, PDF 243, 245): bar 176, Cl 2 holds G3 through the bar instead of falling to F3 on beat 3 with the violas, so 176.3 is a complete V6/5 over Bn 1's B2 and the seventh F stays only in the violas, resolving to E♭ at 177 (as c263 did at 172 and 180). Cl 2's 177–178 line unchanged.
- Declined: ♮VII–V6/5–i at 175–177 (breaks the stepwise bass), III at 20.1 (weak-to-strong, undoes c257/c322), a passing IV6 at 96 (octaves with Ob 1's movement II tail). Form and proportions follow the unit.

## Cycle 534 (v534 → v535), lens 4, no change
- Casanelles ch. 6 (masking, density and register): no change. Tested and declined Hn 3 F4 for A4 at 252 (five parallel fifths on 252.1, c139's reason holds) and Hn 1 on B♭3 at 83–86 (loses the pedal's octave ring; the tune already outweighs one horn at mf). Checked, follows: Ob 1 with the violins at 187–190, woodwinds against brass, brass density at 205–208, 243–254 and 265–272, low thirds (Bn 2 at 84 declined, c504's line).

## Cycle 535 (v535 → v536), lens 5, violas non div. at 204
- Adler ch. 2 (string notation: chords as double-stops, "non div." is safer, PDF 30, Ex. II-12): the violas' two ff D4/F4 down-bow strokes at 204 are marked "non div.", as at the other ff string strokes (1, 5, 91, 277), before "div." at 205. Text only; MIDI byte-identical.
- Tested and declined: measured-tremolo shorthand for the basses' eighths at 199–208 and 247–275 (no space saved, misreadable beside the violins' tremolo, and the MIDI would lose the drive). The reprinted "div." at 211 left as is.

## Cycle 536 (v536 → v537), lens 6, cor anglais with Ob 1 at 151–158
- Sebesky ch. 2 (oboe unisons are harsh, oboe with cor anglais in unison is endorsed; the oboe's low F4–B♭3 is coarse, PDF 70–72, 80): at the ff recapitulation 151–158 the cor anglais takes Ob 2's unison copy of F1 (down to E♭4, D4 and F4 at 152–153 and 157), so 147–166 is one cor anglais passage (c446 gave it 159–166); Ob 2 rests from 151. Pitches, slurs, accents and dynamics unchanged; layout unchanged.
- Tested and declined: the same swap at 19–26 (page 2 over-full against c251's layout). Checked, no change: trombone slides at 248/251 (protected, playable with the F attachment), horn attacks and stopped notes, ranges and endurance.

## Cycle 537 (v537 → v538), lens 7, no change
- Adler part 2 ch. 16 (transcription and layering): no change. Tested and declined the timpani hammered rhythm of 199 in place of the A♭ roll at 209–210 (doubles the basses' pitch and pulse; the roll is the only sustained layer under the winds' fp < chord into 211). Declined on paper: a dovetailed string scale at 209–210, a second clarinet line at 89–90 (c502), a passed counter-theme at 205–208, a held note under the bassoon solo at 115–118. F1's doublings at 11–26 and 151–166 follow the reading.

## Cycle 538 (v538 → v539), lens 8, Hn 4 crossfade into Cl 2 at 47
- Casanelles (crossfade and overlap, PDF 149, 153, 155): Hn 4's held A♭3 pp over the B♭ pedal now fades (`aes2\> r2\!`) as Cl 2 enters on the same A♭3 at 47.1, so the colour change is a crossfade rather than a step. Dynamic only; no notes changed.
- Declined: accents on the basses' repeated eighths at 265–275 (c438), a morendo on the B♭ pedal at 49–50. The final fff chord at 278 already holds its level.

## Cycle 539 (v539 → v540), lens 9, holistic comparison (Rachmaninoff 2)
- Holistic comparison with Rachmaninoff 2/iv, plus a v529 → v539 check (Rimsky-Korsakov PDF 132–133: passing notes against chord notes in the same timbre and register sound harsh): the off-beat horn chord no longer strikes a semitone against F1's passing notes in Hn 1·2 and the violas: Hn 3 F4 for D♭4 at 16.2 and 156.2, Hn 4 D4 for G3 at 20.2. The ♭II6 colour stays in the tune's D♭ over F; tune, bass and dynamics unchanged.
- Cor anglais at 157–158: the arpeggio an octave lower, with Hn 1·2 and the violas (c536 had it at written E♭6–D6 ff, its thin top), so its G4 at 158 leads into its inner line at 159; Ob 2 still rests.
- Kept: the semitone at 164.2 (every alternative anticipates the tune, leaps or doubles the seventh), the horns at 207–208 (protected). F2 still has no full tonic-major return (c339). Cycles 529–538 rechecked: nothing got worse.

## Cycle 540 (v540 → v541), lens 10, cyclic review; Bn 1 F♯3 at 1 and 5
- Adler (unison and octave doubling, PDF 19–23; part 2 PDF 190–191, Ex. XV-37): Bn 1 plays F♯3→G3 at 1–2 and 5–6 (was C3→B2), so the finale's opening chord has the same players and pitches as scherzo bar 200 (V7 of C♯ minor since scherzo v521), and the ff V chord at 2 and 6 loses one of its seven leading-tone B's. Pitch content, dynamics, the A♭ link in Hn 1 and Vln I, and the E♭4 answers unchanged.
- Cyclic review against movement I v621 (series 4 complete), movement II v600 and scherzo v521: all quotations and joins at pitch; records 35/35, 19/19, 11/11, 52/52, finale 51/51; cyclic rules hold. finale.md: stamps updated, movement I v608–v621 listed (Tbn 1 E4 at I 158, still a 6/4 over G), the scherzo-200 anticipation of IV 1 recorded under Opening, and the 159–166 held line credited to the cor anglais.
- Declined: theme B in three octaves at 211–216; kept Fl 1 with the trumpet solo at 61–63 (c041).

## Cycle 541 (v541 → v542), lens 1, no change
- A&S Unit 20 (melodic figuration): no change. Tested and declined a five-note turn on the violins' held G6 at 254 (competes with the S head's B→C cadence in the same beats; F♮ is a chord tone, F♯ clashes with V7's F). Declined on paper: a double incomplete neighbour at 268.4 (protected 265–272). Follows: F2's plain minor and decorated major statements, F1's implied two-line melody, leap dissonances (all chord tones), chromatic passing and neighbour tones.

## Cycle 542 (v542 → v543), lens 2, complete V6/5 at 29
- A&S Unit 5 (doubling and spacing; no doubled leading tone, complete seventh-chord inversions, PDF 76, Ex. 5-4): bar 29, Hn 2 plays B3–D4–B3 (`b2 d'4 b4~`, was `b1~`), so the V6/5 on 29.3 under F1's bass statement is complete (B–D–F–G) with B no longer doubled; Hn 2 returns to B3 on 29.4, swapping with the theme's B3–D4, and keeps c222's held B at 30.1–2 and its resolution to C at 30.3. Tested and rejected: back to B3 on 30.1 (octaves with the countersubject), D4 held into 30 (undoes c222).
- Checked, no change: spacing gaps, the V4/2 at 133.4 (c183, c453), diminished-to-perfect fifths, hidden outer-voice fifths, other leading-tone doublings (octave lines), F1's augmented 2nd.

## Cycle 543 (v543 → v544), lens 3, no change
- A&S Unit 14 (V7 and its inversions in the larger form; approaches to V): no change. Tested and declined the V4/2's bass F stepping to E♭ at 134 (sounds a C-minor tonic 16 bars before the recapitulation, fills the break before J; 131–134 protected). Declined on paper: E7 before the S head at 238→239 (changes the movement I quotation's harmony and pre-empts the G♯ link at 242–243). Proportions, coda stages, key-area confirmations and approaches to V follow the reading.

## Cycle 544 (v544 → v545), lens 4, bass clarinet pad at 171–186
- Rimsky-Korsakov (wind chords: never three different timbres; three of one family with the low member, PDF 92–94): Bn 1's held pad under the recapitulated F2 at 171–186 moves to the bass clarinet, same pitches, pp "dal niente", so the pad is one family (Cl 2 + bass clarinet, Cl 1 from 181) set apart from the cor anglais and muted trumpet melody, and differs in colour from the exposition's pad. Bn 1 rests 16 bars before its counter-melody at 187 (part-only cue at 185–186). Notes, dynamics and harmony unchanged (c092, c312, c380, c413, c533 kept).
- Kept: open fourths and fifths in the held middle parts at 173–179 (the violas supply the third), the oboes at 231–234 (protected) and 259–260 (c454), the full divisi at 278. The exposition pad at 51–66 is protected and already follows PDF 92.

## Cycle 545 (v545 → v546), lens 5, clefs at 35
- Gould (clefs: before the barline; change between phrases, after rests, PDF 21–22): at 35, the bar that starts with grace notes in Fl 1 and Vln I·II, the basses' return to bass clef now prints before the 34|35 barline (spacer grace notes), and the bassoons' tenor clef moves from 33 to 35, after the rest at 34.4, so 33–34 (the end of the F1 statement with the cellos) stay in bass clef and the clef comes before the eighths up to B♭4 that were c365's reason. MIDI byte-identical; only page 2 at 33–35 changes.
- Checked, no change: the horns' score-only bass clefs, the basses' tenor clef at 27–34 (c335, c365, c455), the harmonics at 43–50, cymbal crosses, stems.

## Cycle 546 (v546 → v547), lens 6, cello bowing before pizz. at 171
- Adler ch. 2 (bowing; end on an up-bow at the frog before pizz., PDF 54; slurs on diminuendos, PDF 38): the cellos' A♭ at 168 slurs into the G at 169.1 on the diminuendo down-bow, and the run and held D3 are an up-bow ending at the frog before "pizz." at 171, restoring c218's intent after c434 gave the cellos the descent. Notes, dynamics and MIDI unchanged; the basses already ended at the frog.
- Weighed, not applied: cellos sul G at 170, a string trill at 147–150 (protected), senza vibrato at 95–98, a natural harmonic at 43–50 (none gives B♭5), punta d'arco at 19–26. Long slurs within Adler's limits.

## Cycle 547 (v547 → v548), lens 7, horns hold through 129
- Rimsky-Korsakov ch. III (overlaying and enclosure; in quick chord changes the brass hold the common notes and the woodwind move, PDF 108): bar 129, Hn 3 `d'4 d'4 c'4 c'4` and Hn 4 holds G3 in quarters (Hn 3 leapt D4→G4 onto Hn 1's G4 and Hn 4 went G3–G3–E3–C4), so through the bar's I6–IV6–iv6 the motion is in the bass (E–E♭–D), Bn 1 and Fl 1; the horns step into 130. c033's quarter-note pulse kept; IV6 and iv6 complete.
- Checked, no change: horns between the bassoons at 80.3–4 (c147), the horn neighbour chord at 101–106 (c247, c519). Follows: four soft horns under clarinets at 9–10, horns with violas or cellos at 67–74 and 130–131.

## Cycle 548 (v548 → v549), lens 8, diminuendo on F2's held note at 74 and 194
- A&S Unit 3 (a phrase ends on its goal; an anticipation is unaccented; a note's start is stronger than its continuation, PDF 51, 54, 56): F2's held half-cadence note now fades: Vln I·II `f''1\>` at 74 with mf restated at 75, and in the recapitulation Vln I·II and violas `d''1\>`/`d'1\>` at 194 with mf/mp at 195, so the counter-melody's move into the next bar is heard and the second half starts afresh. No pitch, slur or overall level change (c458's declined swell not reopened).
- No change: tenuto on the winds' syncopated pad at 36.4/38.3 (c348), a swell in the bassoon solo at 119–122 (c458), tempo words (graded, on third bars).

## Cycle 549 (v549 → v550), lens 9, holistic comparison (Bruckner 4)
- Holistic comparison with Bruckner 4/iv, plus a v539 → v549 check (Rimsky-Korsakov: double a solo only in isolated phrases, PDF 140–141; examples at PDF 449, 457): the muted trumpet now also rests from 183.4 to 186, after ending with Fl 1 on C5 at 183, so the recapitulated F2 runs duet – cor anglais alone – duet at the climax – cor anglais alone, and the muted trumpet's weak low D4–B3–C4 goes; "togli sord." moves to 184. F2's notes unchanged.
- No change: the coda's short soft stretches against Bruckner (219–223 protected, models are Brahms and Tchaikovsky); the coda's tempo plan; the c544 side effect at 170→171 (Cl 2 with the bass clarinet for one pp beat) kept; the basses under Ob 1 at 95–98 not reopened (c507, c524). Cycles 539–548 rechecked: nothing got worse.

## Cycle 550 (v550 → v551), lens 10, cyclic review; sul A at 243
- Rimsky-Korsakov prefaces and ch. IV (a work's colours belong to it; transfer of a held note between instruments, PDF 20, 125–126): Vln I's upper desk marks "div., sul A" on the scherzo's G♯5 at 243–245.2, as the scherzo marks that note since its v527. Text only; MIDI byte-identical.
- Cyclic review against movement I v621, movement II v600 and scherzo v532: all quotations and joins at pitch; records 35/35, 19/19, 11/11, 52/52, finale 51/51; cyclic rules hold. The scherzo's horn call now ties E4 into bar 5 with D♯4 on beat 3 (c530); the D♯4 still resolves only at the finale's 219–220. finale.md updated: stamps, scherzo v522–v532, sul A, the shared tie in item 7.
- Declined: low brass pp growing into 247 (blurs the horn call's C, c450); splitting the major horn call between horns and trumpets (the owed item is the call in the trumpets).

## Cycle 551 (v551 → v552), lens 1, violas with Vln II at 39–40
- Rimsky-Korsakov ch. II (violas join the violins' low octave; Vln I over Vln II + violas, PDF 60, Ex. 28): at 39–40 the violas double Vln II's lower octave of F1's head (ff >, down to A♭3–G3), instead of holding D4 with Bn 1, so the violins' answer to the cellos' B♭-minor head has a full lower octave. F1's notes unchanged; 41–42 unchanged.
- Declined: Vln II an octave below Vln I at 207–208 (loses its rising scale), F2 in unison before the octaves at 67–74, Vln I over Vln II + violas at 187–198 (protected since c191). Cellos sul G at 41–42 kept (c391).

## Cycle 552 (v552 → v553), lens 2, ii6/5 into the codetta's cadence at 93
- A&S Units 9–10 (II and IV lead into V; back-relating dominants then II6–V7–I, Ex. 9-2c, 9-8, 10-10 Mozart K. 332): bar 93, the chord on beats 2–3 is ii6/5 (A♭–C–E♭–F) instead of a third tonic, so the codetta's back-relating I–V strokes end with ii6/5–V7–I. The bass steps A♭–B♭; Tbn 1 and Vln II hold A♭ into V7 as its prepared seventh; the top line stays E♭6–D6–E♭6. c248's displaced rhythm, c252's single chromatic chord at 92, c324's pedals and c416's timpani kept.
- Checked, no change: the 6/4s at 152.4→153.1 and 243.3→244.2, the doubled fourths at 220 and 250 (protected). Declined a cadential 6/4 at 93.4.

## Cycle 553 (v553 → v554), lens 3, no change
- A&S Unit 26 (diatonic modulation), seventh pass: no change. Tested and declined an applied V6/5 of A♭ at 186 (adds a 17th page, loses the deceptive VI reinterpreted as the new tonic and the V→VI chain at 26, 34→35, 186→187, fills the breath before 187; A♭ is confirmed at 191–193). Proportions, the K.457 key plan, key confirmations, melodic tonicizations and arrivals follow the reading.

## Cycle 554 (v554 → v555), lens 4, ii6/5 at 93 spread across families
- Rimsky-Korsakov ch. III (sevenths and seconds go to instruments of different colour, PDF 102–103): c552's ii6/5 on 93.2–3 had its E♭–F second held ff inside one family twice (Tpt 2 F4 over Tpt 3 E♭4; Hn 4 F3 under Hn 2's E♭3). Tpt 3 now plays C4 (`r4 c'2-> d'4->`) and Hn 4 A♭3 (`r4 aes2-> f4->`), so the second lies between trumpet and horn; harmony, bass, Tbn 1's held A♭, top line, rhythm and dynamics unchanged, and two octaves with the flutes and violins at 93 are gone.
- No change: Tbn 1 C4 over Tbn 2 D3 at 152/156 (a prepared 4–3 at mf); other same-family seconds are protected or kept (c454 at 259).

## Cycle 555 (v555 → v556), lens 5, two-pitch beam rule
- Gould beams (two pitches only: horizontal when the one different note is at the end, PDF 37): a `gould-two-pitch-flat` helper inside c285's `gould-concave-damping` flattens the basses' `c,8 c,8 c,8 g,,8` at 277.1–2, the only group in the score it changes; groups with equal numbers of each pitch (171–186) keep their slope. Engraving only; MIDI byte-identical.
- Tested and rejected: the rule by staff position (it also flattened the chromatic D–D♭–C groups at 199 and 247). Checked across the score: stem directions, equidistant groups, kneed beams, clef changes in beams.

## Cycle 556 (v556 → v557), lens 6, violas sul G at 43–46
- Adler ch. 3 (open strings stand out in soft held passages; mark one-string passages; the viola's dark G string, PDF 73–76, 87): the violas' held pp D4 at 43–46 is marked "sul G", as every other unprotected soft held D4 in the score already is (8–10, 41–42, 81, 133–134, 169–170). Text only; MIDI byte-identical.
- No change: double stops and divisi, wide skips (Vln II at 38 kept in unison, c551), basses (low C1 at 263/278 not reopened, c246), the harmonic at 43–50.

## Cycle 557 (v557 → v558), lens 7, no change
- Sebesky ch. 1 (economy, focus, contrary motion in the background): no change. Tested and declined the cellos leaving the A♭ pedal for a rising line at 207–208 (doubles and inverts the ii7's seventh, covers Bn 1's lowest octave of the head, c158). Declined on paper: the countersubject under F1 at 151–158, contrary motion in Vln II at 167–168. Economy checks at 41–42 (c431), 9–10 and 205–206 hold.

## Cycle 558 (v558 → v559), lens 8, low strings in quarters at 82
- Sebesky Ex. 273 (halves to quarters for extra push into the next phrase, PDF 208): at 82 under "animando" the cellos and basses play C♭–C♭–B♭–B♭ in tenuto quarters with a crescendo (were two half notes), so the low strings mark the quickening beat into the walking quarters at 83, as at 245–246 (c358). Pitches, harmony and dynamics unchanged; c167's balance reason still holds.
- Declined: the chromatic counter at 239–242 to mf (set f on purpose over the harp), marcato accents (unused in the symphony), swells or "no vib." on the protected pads at 51–66 and 171–186. Kept: the held build-up at 133–138, the chorale top line at 224–227.

## Cycle 559 (v559 → v560), lens 9, holistic comparison with Mahler 1, no change
- Holistic comparison with Mahler 1/iv, plus a v549 → v559 check (Adler part 1 ch. 5 and 8): no change. Tested and declined Hn 1·2 an octave higher at 25–26 (unison with Vln II and the oboes, over-full page 2). Declined: pausing the harp at 74 (protected), moving the doubled third at 251 (the themes' own notes, protected), a horn on the third at 97–98 (doubles F minor's leading tone). The finale shares Mahler's outburst after a soft end, flat-key second theme, first-movement recalls, false goal and winning brass chorale; cycles 549–558 rechecked: nothing got worse.

## Cycle 560 (v560 → v561), lens 10, cyclic review, no change
- Cyclic review (Sebesky ch. 1 and 9): no score change. Against movement I v621, movement II v600 and scherzo v542: all quotations and joins at pitch; records 35/35, 19/19, 11/11, 52/52, finale 51/51; cyclic rules hold. The scherzo's Hn 1 now previews the motto tail alone at its 205–209 (c540), at the pitch and player of the close the finale's Hn 1 continues at 1–2. finale.md stamps and scherzo v533–v542 list updated.
- Tested and declined: Hn 4 an octave higher at 241–244 for the scherzo's G♯4/G♯5 pair (covers the chromatic counter, sits above the horn call's E4, crosses Hn 3). Declined on paper: movement I's bar 18 in major at 250 (B5 against the head's C6).

## Cycle 561 (v561 → v562), lens 1, Cl 2 on F2's peak at 257–258
- Rimsky-Korsakov ch. II (a soprano melody doubled in one octave: winds above, strings below, PDF 78, Ex. 90; clarinet over bassoon, PDF 76): at 257–258, F2's last climax bar, Cl 2 leaves the chorale's E5 and doubles Vln II on F2's upper octave (`c''2.(\f\< d''4 | g''4. f''8 e''4 d''4)`), returning to the chorale's D5 at 259. The E5 stays in Tpt 1·2, Ob 1, the flutes and Vln I. F2's notes, the chorale top line, the harmony, the woodwind rest at 255–256 and the cor anglais's silence unchanged.
- Declined: thinning the winds on Vln II's octave at 83–86 (protected), a wind above the horns at 205–206, filling Vln II's upper octave at 255–256 (protected rest, c430).

## Cycle 562 (v562 → v563), lens 2, 5–6 into IV6 at 78
- A&S Units 11–13 (5–6 from VI to IV6, PDF 168, Ex. 11-12a; IV7 with an accented passing 3, PDF 183–185; no dominant sound between vi and IV, PDF 172): at F2's E♭-major climax, bar 78 beats 3–4 move vi7 → IV6 by a 5–6 instead of sounding a B♭ triad over the C bass: Hn 2 G3–A♭3 (was B♭3), violas hold E♭4, harp RH E♭–A♭–C–E♭ (was F–B♭–D–F). 78–80 now run vi7 – IV6 – IV – V6/5 of V – V, as at 257–259, and the harp/Vln I octaves into 79.1 are gone. F2's notes, the harp's low line (c205) and the pad's rhythm and breath (c166) unchanged.
- Kept: the cellos' chromatic E♮→E♭ at 71, the codetta's leaping A♭6 at 91–93 (c248, c252, c552). Phrygian cadences at 57–58 and 177–178 follow the book.

## Cycle 563 (v563 → v564), lens 3, no change
- A&S Unit 32 (chromatic joins, common tones in exposed voices, the ♭VI–♭II–V path): no change. Tested and declined putting the F5–F♯5–G5 inflection and the seventh both in Vln II at 113–115 (same sound, loses Vln I's held F♯5 bridge into the bassoon solo). Declined on paper: A♭ minor through 195–198 (undoes c270, c293, c370), A♯ at 122.4 (augmented octave with Bn 1, protected). Proportions, the A♭ area, the G minor/major turn and every chromatic join's exposed link follow the reading.

## Cycle 564 (v564 → v565), lens 4, timpani roll at 35
- Rimsky-Korsakov tutti chords (appendix PDF 505–507; ch. IV, Ex. 204–221: every held loud chord with timpani has a roll on the bass): bar 35, under the trombones', contrabassoon's and basses' held A♭ ff > f, the timpani roll A♭ ff > f through the bar (`aes,2.:32->~\ff\> aes,4:32\f`, was one f stroke). The retuning to B♭ at 37 and the roll at 39–40 unchanged.
- Checked, no change: 166 (protected), a tutti without woodwind, short low strokes at 35–38. Not reopened: wind trills, a restruck final chord, brass a degree softer at 223/263/278.

## Cycle 565 (v565 → v566), lens 5, no change
- Gould ch. 1 (ledger lines, octave signs, rests): no change. Tested and declined writing the harp's 239–240 chords at pitch in the part with the 8 bassa score-only (the part grows to 3 pages with a page turn before 255–279). Checked, no change: ledger lines (at most five, in Fl 1 and Vln I), the horns' four lines inside F1's phrase, rests on shared staves, the harp's 8 bassa at 67–82.

## Cycle 566 (v566 → v567), lens 6, advance harp pedal marks
- Adler ch. 4 (harp pedals: one foot changes one pedal at a time, PDF 112–113): advance pedal marks in the two long harp rests before entries that need several changes: "Ped.: C♮ B♮ / E♮ F♯ A♮" at 115 (letter H) for the entry at 123, and "Ped.: B♯ / F♭ G♮" at 247 (letter R) for the glissando at 277, in the score's existing form. Notation only; MIDI byte-identical.
- Tested and declined: a ringing E-major harp chord at 243 (inaudible under the horn call, undoes the étouffez and c116/c238). Pedalling, range, the D1 tuning, harmonics, the glissando tuning and damping all follow the reading.
