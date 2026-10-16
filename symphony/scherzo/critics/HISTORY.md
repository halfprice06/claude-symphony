# Scherzo critic history

Cycle N reviews vNN and produces v(N+1). Each entry: Accepted, Rejected (with reason), Open, Do-not-touch.

## v01 (composer's first draft, 2026-10-12)
- 392 bars, 3/4, about 4:54 (285 s MIDI); plan in movement-scherzo-plan.md. Sections: intro 1–12, sA 13–56, sB 57–104, sC 105–140, link 141–152, tA 153–184, tB 185–216, tC 217–248, retr 249–264, dA 265–300, dB 301–316, dC 317–340, coda 341–392.
- Build: 0 warnings, 13 A3 pages. Analyser parallels left in v01: 69 (section join), 194 (Ob 1 and cor anglais in octaves, by design), 276 (heterophony), 342–344 (motive x ostinato entering at the fifth, by design), 364, 371.
- v01 was written by generator scripts in kit/v01-generators/; dA, dB and dC were copied from sA, sB and sC and are now independent text (edit each directly).
- Do-not-touch (cyclic rules from cyclic-notes.md "Four movements"; change only by answering the reason there):
  - No C-major key or C-major triad anywhere. Reason: C major belongs to the finale's arrival.
  - Trumpets only in tutti rhythm or motive x (Tpt 3 tacet). Reason: the finale's soft undoubled trumpet solo.
  - No string tremolo, no violin note above B6 (B6 only at 352), no cymbals, no high horn unison, no tuba melody. Reason: kept for the finale.
  - Bars 1–7: Hn 1 G♯4 then G♯–E–D♯–E (movement II's A♭ as G♯; the horn call of movement I in E). Bars 385–392: the last sound is G♯ in Hn 1 and Vln I. Reason: the pivot from movement II and into the finale.
  - Bars 373–376: Hn 1 B–A♯–A–G♯ (the motto's chromatic tail) over E – A♯°7 – A minor – E.
  - Theme A's tail G–F♯–F–E (the motto's tail on E's degrees). Hn 3·4 "senza sord." at their first entry (73). Timpani label at bar 1.

## Cycle 1 (v01 → v02), lens 1 melody, A&S Unit 20
- Accepted: T bar 4 accented passing note A→G♯, bar 8 appoggiatura A♯→B (156, 160, 172, 176, 220, 224, 360, 364); theme A peak `c'''2->( b''8 fis''8)` at 24, 116, 276, 328; second-idea cadence by double neighbour at 55, 131, 299.
- Open: T's third phrase (161–164 and returns) shares the rhythm and contour of the first two; a change must not add a page.
- Do-not-touch (critic): motive x and the chromatic tail of theme A; the harp melody 73–80.

## Cycle 2 (v02 → v03), lens 2 harmony, A&S Unit 5
- Accepted: bass A at 66 (no C-major triad: a whole-movement scan found no other); 127 basses octave slip; leading-tone doubling 64, 68, 308; Bsn fifths 345–348; Vln II under Hn 1 at 374–380; C♯ at 49 and 293.
- Do-not-touch (critic): plagal close harmony 373–376; hemiola cadences 53–55 and 129–131.

## Cycle 3 (v03 → v04), lens 3 form, A&S Unit 14
- BAR NUMBERS from v04: tB 185–208 (24 bars; v03 189–196 cut); v03 bars ≥ 197 are −8. Now: tC 209–240, retr 241–256, dA 257–292, dB 293–308, dC 309–332, coda 333–384 (B6 peak 344, G.P. 348, Meno mosso 349, motto tail 365–368, last G♯ 377–384).
- Accepted: reprise 275–292 now returns the second idea in E minor (no repeat of the move to G); trio middle cut; 7th over B before the trio's return; Vln II arco at 277; Bsn 1 has T's head at 233.
- Do-not-touch, renumbered: motto tail Hn 1 at 365–368; last G♯ 377–384; B6 only at 344.

## Mount-expiry rule (coordinator, 2026-10-13 22:37 UTC)
The shared-folder mount seems to expire about 24 hours after a thread's machine starts and does not come back. At the start of every cycle check `uptime -s` / `cat /proc/uptime`; once uptime passes about 22 hours, finish the current cycle, promote it, send the coordinator a handoff (last promoted version, anything unpromoted, next command) and stop. If any /mnt/project-files path gives an I/O error, do not retry for 30 minutes: send the handoff at once.

## Theme record (2026-10-12; Dan: "I don't want the scherzo themes to be locked")
The themes are free to evolve under the critics. symphony/coherence/themes-scherzo.ly records the current themes (exact notes and rhythms, and every place each appears); kit/promote.sh runs coherence/themecheck.py, which only reports CHANGED or MOVED statements and never blocks. After a promotion that changes a theme or the ending, the composer refreshes the record from the new version (coherence/makelock.py, then the %@ bar lines), logs it below, and sends the finale thread (cse_01VEPkuwEiufbD2AHMw6eKEa) the old and new notes.

## Theme changes
(record taken from v04)
- v11 (cycle 10): horn call. Old Hn 1 G♯4 (bars 1–3) – E4 – D♯4 – E4. New Hn 1 G♯4 (1–2) – G♯3 (3) – E4 (4) – D♯4 (5) – E4 (6–7), restoring movement I's rising sixth 3–1. Record refreshed; finale told.
- v12 (cycle 11): trio tune T, bars 10–11. Old e''2 gis''4 | fis''4. e''8 dis''4. New e''4 gis''2 | a''4. gis''8 fis''4 (peak A5 in the third phrase), in all statements. Record refreshed; finale told.
- v31 (cycle 30): horn call unresolved. Old G♯4 (1–2), G♯3, E4, D♯4, E4. New G♯4 (1–2), G♯3, E4, D♯4 held 5–6, rest at 7 (the finale owns the resolution). Record refreshed; finale told.
- v32 (cycle 31): second idea, bars 4 and 8 of each statement. Old minim + crotchet (d'''2 / e'''2 tied pattern). New dotted crotchet + quaver (G: d'''4. e'''8, e'''4. d'''8; E minor: b''4. d'''8, b''4. cis'''8). Record refreshed; finale told.
- v44: the coda statement of the trio tune (Vln I/Fl 1 349–356, Vln II an octave lower) changes its cadence. Old 353–356: gis''4 b'' e''' | dis'''2 fis'''4 | e'''2.~ | e'''2 r4. New: gis''4 b'' e''' | gis'''2 fis'''8 e''' | dis'''2 fis'''4 | e'''2 r4. Record line now checks 349–353 only. Finale told (it does not quote the trio tune; motto tail 357–360 and last G♯ unchanged).
- v62 (cycle 61): trio tune cadence, bars 13–15 of every full statement (165–167, 181–183, 221–223). Old gis'4 b'4 e''4 | dis''2 fis''4 | e''2. New gis'4 b'4 e''4~ | e''4 dis''4 fis''4 | e''2. Coda 354–355 likewise: gis'''2 fis'''8 e'''~ | e'''4 dis''' fis'''. Record refreshed; finale told.

- v82 (cycle 81): trio tune T, bars 10–11 of every full statement (162, 178, 218, 350). Old e''4 gis''2 | a''4. gis''8 fis''4. New e''4 gis''4 a''4~ | a''4. gis''8 fis''4 (the A anticipated and tied). Record refreshed; finale told (it does not quote T).
- v94 (cycle 93): trio tune T, second statement only (Vln I 169, Vln II an octave lower), bars 180–184. Old cis'''4 b'' a'' | gis''4 b'' e'''~ | e'''4 dis''' fis''' | e'''2.~ | e'''2 r4. New cis'''4 b'' gis'' | dis''4 fis'' b''~ | b''4 ais'' cis''' | b''2.~ | b''2 r4 (T's cadence moved to B, the trio's first V key area). Record line now checks its first 27 notes; finale told (it does not quote T).

## Cycle 4 (lens 4 orchestration, Rimsky-Korsakov ch. I and III) v04 → v05
All 8 findings accepted (reasons in v05/critique.md): horn chords split and tutti balance 105–120/309–324 with Vln II on the theme; harp RH out of the trio off-beats 169–184/209–224; F-major episode thinned (Cl rests, harp chord to LH); Hn 2 lower in the second idea 45–56; Hn 1·2 thirds/sixths 209–224; violas pizz. 257–276; 87–88 doubling; tuba E1 at 341–343. Themes unchanged. Keep: harp alone with the theme head at 73–80; no plucked off-beats doubled by bowed ones.

## Cycle 5 (lens 5 engraving, Gould ch. 1) v05 → v06
All 8 findings accepted (v06/critique.md): Cb pp at 225; Fl 1 pp at 169; duplicate ff at 104–105/308–309; \partCombineApart Ob/Cl in the tutti theme; arco/pizz. clean-up; marks over the strings group; \break at the Trio; horn staff consistency. Themes and ending unchanged.

## Cycle 6 (lens 6 playability, Adler ch. 2) v06 → v07
All 8 findings accepted (v07/critique.md): Hn 1 breath at 375 covered by Hn 3 (373–377); arco/pizz. change time (Cb 204, Vc 223–224, Vln II/Vla 276); Vln I two-bar bows in the second idea; harp C♮ at 188 and pedal marks; Bass Cl B♭2 at 82; timp hard sticks at 246 and the G♯ drum used at 188/200; Bsn 1 rests. Keep: theme A as light spiccato over pizz. bass downbeats.

## Cycle 7 (lens 7 texture, Adler ch. 5) v07 → v08
All 5 findings accepted (v08/critique.md): tenor countermelody in the tutti theme; trio cello in complementary rhythm; accompaniment below theme A's low dips; countersubject in crotchets; fugato entries for strings alone. Record: Bsn 1 doublings at 57/293 dropped from themes-scherzo.ly (not a theme change). Keep: call and response 29–36, trio layering, homophonic climax 69–72, coda motive-x build 333–340, motto tail and last G♯ 365–384.

## Cycle 8 (lens 8 expression, Rimsky-Korsakov ch. IV) v08 → v09
Findings 1–7 accepted (v09/critique.md): built crescendi at the hemiola climaxes (sfp at 305), fugato hairpins, reprise crescendo 275–276, trio-return balance, 200 diminuendo, coda bass mf<, Hn 1 last G♯ pp→ppp. Finding 8 rejected (shared clarinet staff; already pp). Ending dynamics: last sound now ppp in Hn 1 and Vln I (finale told).

## Cycle 9 (lens 9 holistic, Dvořák 9/iii; Rimsky examples 1–68) v09 → v10
All 4 findings accepted (v10/critique.md): Vln II on the second idea's melody an octave below; Vln II doubles the coda climax; tutti theme A 107–108/311–312 up an octave in Vln I/Fl (register only); Vln II doubles T at the trio return, violas div. take the off-beats. Keep: plan, keys, hemiolas, timpani writing, soft trio.

## Cycle 10 (lens 10 cyclic, A&S Unit 32) v10 → v11
Findings 1–3 accepted (v11/critique.md): horn call with the rising sixth (theme change, logged above); Hn 2 common-tone A into the F-major episode 72–74; timpani retune label and soft sticks at 349. 4–5 were notes for the finale (cellos' last note; suggested chain of closes), sent. Keep: the scherzo's ending close 365–368; links into and out of the movement checked and consistent.

## Cycle 11 (lens 1 melody, Rimsky ch. II) v11 → v12
All 5 accepted (v12/critique.md): T's third phrase climbs to A5 (theme change, logged above); Vln II octave doubling of T at 169–184 and 357–364; horns clear of the motto tail at 106/118/310/322; cellos' answer at 189–192 up an octave with the cor anglais.

## Cycle 12 (lens 2 harmony, A&S Units 9–10) v12 → v13
Findings 1–6 accepted (v13/critique.md): trio tune bars 11–12 reharmonised ii–ii6; cadential 6/4 at coda 343; bass E–F♯–G into the cadential 6/4 at 127–128/287–288; no augmented 2nd in violas/Hn 1 at theme A's peak; V6/5 of F at 79; Bsn 2 pedal 145–148. Keep: hemiola cadences 53 and 129 as they are.

## Cycle 13 (lens 3 form, A&S Unit 26) v13 → v14
All 3 accepted (v14/critique.md): coda T first half in A major (IV) with pivot back to E at 356; iv before the returning V at 247; comment bar numbers fixed. Keep: reprise order, length, F-major episode, proportions, coda stage 1.

## Cycle 14 (lens 4 orchestration, Rimsky ch. III) v14 → v15
All 4 accepted (v15/critique.md): Tpt 2 E4 at 109/313; bass trombone short downbeats, Bsn 2 sustains, in the tutti theme; woodwinds above trumpets at 104/308; Bsn 1 inner line at 209–224. Keep: F-major episode colour 73–88, coda brass 341–346, close with moving bassoons 365–368.

## Cycle 15 (lens 5 engraving, Gould beams) v15 → v16
All 5 accepted (v16/critique.md): ledger-line beam positions for Fl 1; Cl 1·2 swapped in the tutti theme; Ob 1 octave at 108/312; coda Fl 2/Ob 2 chord tones; part-combine directives at 200–201. Record lines for theme A's clarinet now ClTwo. Keep: string beaming of theme A and motive x; closing page 365–384.

## Cycle 16 (lens 6 playability, Adler ch. 3) v16 → v17
Both accepted (v17/critique.md): bass clarinet B1 at 340 moved to the contrabassoon; Vln I shift rests at 44 and 340. Keep: bass writing, divisi viola off-beats in the trio, closing page 365–384.

## Cycle 17 (lens 7 texture, Adler ch. 15) v17 → v18
Findings 1–4 accepted (v18/critique.md): three real voices at 65–68; a real stretto at 69–72/301–304; independent viola line in the E-minor second idea; countersubject pp. Keep: tutti 105–120 with tenor countermelody, trio layering 169–184, coda build 333–340, 365–384.

## Cycle 18 (lens 8 expression: bowing, Adler ch. 2) v18 → v19
All 4 accepted (v19/critique.md): bow-length slurs, down-bow signs at accents and climaxes, pizz.→arco time, louré viola off-beats in the trio. Note: removing the staccato dots on the pizz. violas at 257–276 makes the analyser report a false parallel at 263 (MIDI note lengths); leave them.

## Cycle 19 (lens 9 holistic, Beethoven 9/ii; Rimsky examples 69–130) v19 → v20
Findings 1–4 accepted (v20/critique.md): retransition 89–100 in three-bar groups (ritmo di tre battute); Hn 3·4 thirds/sixths in the F-major episode; no doubled sevenths in brass at 104/308; viola double stops in the tutti theme. Record: Vln I head entry at 95 (2 bars). Keep: solo timpani motive x, fugato building from pp, hemiola cadences.

## Cycle 20 (lens 10 cyclic, A&S Unit 26) v20 → v21
All 4 accepted (v21/critique.md): fermata on the opening G♯ (bar 2); timpani sticks and muta labels at both joins; comments and coherence file updated; Trumpet 3 tacet note instead of an empty staff. Keep: G♯ = A♭ frame, 365–368, B6 at 344, final tuning E, G, B, E.

## Cycle 21 (lens 1 melody, Rimsky ch. II winds/brass) v21 → v22
All 3 accepted (v22/critique.md): trio middle calls get their own quaver-turn rhythm (185, 189, 197); cor anglais doubles the lower octave of the tutti theme; clarinets in A.

## Cycle 22 (lens 2 harmony, A&S Units 11–13) v22 → v23
All 8 accepted (v23/critique.md): augmented seconds removed (theme A iv→V, second-idea bass); iv6 at coda 339 (bass E–D–C–B); three inner parallels fixed; 5–6–5 over IV in the trio codetta; doubled third of vi at 47–48.

## Cycle 23 (lens 3 form, A&S Unit 32) v23 → v24
All 4 accepted (v24/critique.md): 4-bar cut in the trio-to-retransition (retr 12 bars), 4-bar cut in the reprise close (dC 20 bars), motto tail B–A♯–A–G♯ anticipated at 205–209, timpani E at 139.
BAR NUMBERS FROM v24 (376 bars): v23 bars 245–328 are −4, v23 bars 333–384 are −8. dA 253–288, dB 289–304, dC 305–324, coda 325–376 (B6 336, G.P. 340, Meno mosso 341, motto tail 357–360, last G♯ 369–376). Earlier entries use older numbers.

## Cycle 24 (lens 4 orchestration, Rimsky tutti chords) v24 → v25
All 3 accepted (v25/critique.md): Hn 4 dC length error from the v24 cut fixed (new kit/partlengths.py in promote.sh; lyparse now reads hyphenated markup commands); reprise tutti rescored with Fl 1 in the upper octave; string multiple stops on the ff chord at 339.

## Cycle 25 (lens 5 engraving, Gould PDF 41–52) v25 → v26
All 3 accepted (v26/critique.md): Hn 3·4 and Ob/Cl voices swapped so "1." is on top; system break at O.

## Cycle 26 (lens 6 playability, Adler harp PDF 110–124) v26 → v27
All 4 accepted (v27/critique.md): harp's last chord in harmonics (ending scoring change, finale told), pedal settings before entries, C♮ pedal mark on the rest, Hn 3·4 breath at 80.

## Cycle 27 (lens 7 texture, Adler ch. 17) v27 → v28
All 3 accepted (v28/critique.md): accompaniment kept out of the solo's register at 81–84 (harp), 189–192 (harp), 209–224 (violas). Keep: homorhythmic second idea 45–56.

## Cycle 28 (lens 8 expression, Adler ch. 11 and 15) v28 → v29
All 5 accepted (v29/critique.md): fff only at the B6 peak 336; diminuendo out of the ff at 72; coda entries held back to pp; crescendo in all groups at 101–104; MIDI rit./accel. at 240–253 matches the print.

## Cycle 29 (lens 9 holistic, Brahms 4/iii; Rimsky examples 126–209) v29 → v30
All 4 accepted (v30/critique.md): reprise tutti rescored (Vln II lower octave); woodwinds fill the peak chord; no doubled seventh at 338; graded close at 321–324.

## Cycle 30 (lens 10 cyclic, Casanelles ch. 5) v30 → v31
Both accepted (v31/critique.md): horn call left unresolved on D♯ (theme change, logged above); comments and coherence files updated. Keep: G♯ pivot, rising sixth, turn to minor at 7; single fff/B6 at 336 below the finale's.

## Cycle 31 (lens 1 melody, Adler ch. 3) v31 → v32
Both accepted (v32/critique.md): the second idea gets a dotted-crotchet-quaver lead-on in bars 4 and 8 (theme change, logged above); "sul A" for T at 169.

## Cycle 32 (lens 2 harmony, A&S Unit 17) v32 → v33
All 3 accepted (v33/critique.md): sequential bass in the second idea 49–52; Vln I tenths over the coda's falling bass; B7 seventh resolved at 196–197. Keep: plagal close 357–360, hemiola cadences, counterstatement 29–37, fugato 57–72.

## Cycle 33 (lens 3 form/pacing, Rimsky ch. IV) v33 → v34
All 5 accepted (v34/critique.md): low brass held back from the reprise for the coda peak; Vln I rises into 333; crescendo into T's return; arco basses at 209–224; comments. Keep: length and proportions.

## Cycle 34 (lens 4 orchestration, Adler ch. 15) v34 → v35
All 4 accepted (v35/critique.md): low brass rest at 336–338 and return on 339; tune doubled at 333–335; no B6 before the coda peak; Fl 1 on the trio's forte call.

## Cycle 35 (lens 5 engraving, Gould PDF 53–68) v35 → v36
Findings 1–7 accepted (v36/critique.md): solo labels on shared staves, aligned hairpins, bassoon solo at 73, oboe unison at 44/276, collision fixes at 369–376, double bar at P. 8 rejected (centring held notes in narrow bars).

## Resumed 2026-10-16 (Dan: "pick up from where their actor critic loops stopped and continue them")
Paused 2026-10-13 after cycle 86. Resumed at cycle 87 from v87 in a new project thread, working in the git checkout (/home/user/claude_composes) instead of /mnt/project-files; kit paths changed accordingly, book PDFs in pdfs/. Checkpoint PRs to main every ten cycles. Theme changes go to the movement IV thread "Continue movement 4 loop". The mount-expiry rule above no longer applies (no shared mount); commit and push after each promotion instead.

## Cycle 96 (lens 6 playability, Adler ch. 2 second pass) v96 → v97
All 3 accepted (v97/critique.md): bar 300 split ⊓/V so 301–306 bow as 101–106; down-bows for low strings and violas at 336–339; Cb tied up-bow at 223–224. Do-not-touch: the bow split at 300 (it sets the reprise's bowing).

## Batch checkpoint after cycle 96 (2026-10-16)
v88–v97 promoted (cycles 87–96); checkpoint PR to main. Next: cycle 97 reviews v97 (lens 7 texture).

## Cycle 95 (lens 5 engraving, Gould ch. 1 second pass) v95 → v96
Accepted (v96/critique.md): stems.ily engraver sets middle-line stems by context in score and parts. Do-not-touch: stems.ily (remove only if a critic shows a wrong stem it causes).

## Cycle 94 (lens 4 orchestration, Rimsky-Korsakov ch. I and III) v94 → v95
All 6 accepted (v95/critique.md): Hn 1·2 thirds at 218–219; harp LH rests 169–184; Ob 2 rests 197–200; Cl 2 A4 at 41–42/273–274 and 51; C.a./Cl 2 order swapped at 133–136/321–323. Open: bass in one octave only at 209–224. Do-not-touch: Hn 1·2 in thirds and sixths in the trio return (c004, c094).

## Cycle 93 (lens 3 form, A&S Unit 14 second pass) v93 → v94
Both accepted (v94/critique.md): the second trio statement modulates to B at 180–184 (theme change, logged above); no doubled A♯ at 175 and 215–216. Do-not-touch: the trio's B key area at 180–184 (A&S PDF 220, 224); the scherzo's key plan and proportions; the first trio statement 153–168; the approaches at 101–104 and 243–250.

## Cycle 92 (lens 2 harmony, A&S Unit 5 second pass) v92 → v93
All 7 accepted (v93/critique.md): Cl 1 G5 resolves the V7 seventh at 105/305; parallels removed at 67–68 (Vc), 194–195 (Cl 2), 199–201 (Bsn 1), 215–216 (Hn 2 holds F♯4), 345–347 (Vla); no doubled leading tone at 182/222 (Vla <a fis'>), Bsn 1 F♯4 at 211. Open: Hn 1 vs cellos 220→221 octaves (no clean fix found). Do-not-touch: the seventh's resolution at 105/305 is in Cl 1, not the flutes (settles c052 vs c065); plagal close 357–360; hemiola cadences; coda cadence voicing 354–355.

## Cycle 91 (lens 1 melody, A&S Unit 20 second pass) v91 → v92
Accepted (v92/critique.md): the trio call's first bar is a true turn E–F♯–E–D♯–E at 185/197 (answer D♯–E–D♯–C♯–D♯ at 189). Do-not-touch: C♯ in the E-minor second idea at 128/284 (cmajor rule).

## Cycle 90 (lens 10 cyclic, Adler ch. 17) v90 → v91
All accepted (v91/critique.md): timpani motive x ppp at 363/367/371 instead of the closing E roll (ending no longer copies movement I's); Hn 2 rests at 4–7, Bsn 1 holds B3 (call for one horn); timpani 9–10 comment and coherence/scherzo.md updated. Finale told (scoring only). Do-not-touch: Hn 1 alone on the call 3–6; no timpani roll at the close; the timpani B–G–E link at 9–10.

## Cycle 89 (lens 9 holistic, Schumann 2/ii; A&S Units 20–32 opening examples) v89 → v90
Both accepted (v90/critique.md): Vln I bar 331 F6–C6 (no augmented 2nd into 332; no other melodic aug. 2nd left by script scan); V7/IV passing seventh in the violas at 172–173 and 212–213 (trio statements 2 and 3). Do-not-touch: the first trio statement's plain harmony (153–168), kept as the reference the later statements colour.

## Cycle 88 (lens 8 expression, Adler ch. 10) v88 → v89
All 5 accepted (v89/critique.md): sustained horn (and Bsn 1) chords slurred by phrase with tenuto at 45–56, 73–88, 121–132, 197–236, 277–288; horn call 3–6 under one slur (notes unchanged). Do-not-touch: soft-tongued slurred horn chords (Adler PDF 309) unless a critic answers it.

## Cycle 87 (lens 7 texture, Rimsky-Korsakov ch. II) v87 → v88
Both accepted (v88/critique.md): Bsn 2 doubles the trio cellos' countermelody at 209–224 (both bassoons mf); cor anglais doubles the violas' lower octave at 333–339. Open: Ob 2 alone on the lower octave at 101–104/301–304. Do-not-touch: no strings on the lower octave at 105–112 (c067).

## Cycle 86 (lens 6 playability, Sebesky ch. 2) v86 → v87
All 3 accepted (v87/critique.md): cor anglais takes Ob 1's low falling figure at 44/276; Bsn 1 breaths at 116/316 and rest at 300; coda low brass f at 333. Do-not-touch (critic): tutti brass writing (horns on beats 1 and 3, trumpets on motive x, single low-brass downbeats), the trio horn pair 209–224, the closing horn page 357–376.

## Cycle 85 (lens 5 engraving, Adler ch. 2) v85 → v86
All 6 accepted (v86/critique.md): five beats for every pizz.→arco change (192, 208, 272, 276); violas unis. at 193; hemiola cadences rebowed with louré violas (53, 129, 285); cello bows at 261–268; non div. at 105/305; down-bow at 306 removed. Do-not-touch: the hemiola bowing (one bow per minim unit) unless a critic answers Adler PDF 38–42.

## Cycle 84 (lens 4 orchestration, Casanelles ch. 6) v84 → v85
Both accepted (v85/critique.md): horns mf and Hn 1 B4 under the second idea at 45–56; Fl 2 a2 with Fl 1 at 197–200. Kept: tutti horn crotchets, unmuted Vln I on the last G♯.

## Cycle 83 (lens 3 form, A&S Unit 15) v83 → v84
Accepted (v84/critique.md): ♮VII sounded at 330 (Vc A–F♯, Vla F♯–D); plan file marked as v01. Large form unchanged. Do-not-touch (critic): the I–♮VII–III–(IV, ♭II6)–V plan of 13–104, the ♮VII7→V6/5→i turn at 273–277, the F-major episode and its F/A exit 84–89, section proportions.

## Cycle 82 (lens 2 harmony, A&S Unit 27) v82 → v83
All 4 accepted (v83/critique.md): no sounded 3rd under theme A's 4–3 tail at 119/319 (Hn 2 B3, Tbn 2 B2, Tpt 2 F♯4); complete V♭9 at 126 (Hn 2 E–D♯, Bsn 1 E–F♯); Hn 1 F♯4 at 116/316 beat 1; Hn 1 ♭9 neighbour C5 at 337. Do-not-touch (critic): trio 4–3 cadences, soft ♭9 peaks at 24/264, common-tone ♭9 at 126/282, 9–8 at 200, plagal close 357–360.

## Cycle 81 (lens 1 melody, A&S Unit 3) v81 → v82
Accepted (v82/critique.md): T's climax A anticipated on beat 3 and tied over the bar line at 162, 178, 218, 350 (theme change, logged above). Closes cycle 1's open point on the third phrase's rhythm. Do-not-touch: the tied A in T's third phrase; T's 4–3 cadence.

## Cycle 80 (lens 10 cyclic, A&S Unit 28) v80 → v81
Accepted (v81/critique.md): bar 331 iv6 → Neapolitan 6/4 C–F–A (Vln II, Vc, Cl 1, Hn 3 E→F; violas C4; Cl 1/Hn 3 F→D♯). No theme change; finale told for information. Do-not-touch: the F-major episode and harp head 73–88 (link to the finale's IV); the ♭II at 331 (c062's augmented-sixth objection does not apply: no A♯ added).

## Cycle 79 (lens 9 holistic, Mendelssohn MND Scherzo; Adler ch. 16) v79 → v80
Accepted (v80/critique.md): oboes lower at 72 and 300. No regressions since v69. c059's loud-arrivals point closed (no change).

## Cycle 78 (lens 8 expression, Adler ch. 7) v78 → v79
All 4 accepted (v79/critique.md): wind phrase slurs at 209–224 and 345–348; flutes a2 in the upper octave of the tuttis; Ob 1 mf at 45; violas ppp under Bsn 1 at 345.

## Cycle 77 (lens 7 texture, Adler ch. 8) v77 → v78
All 3 accepted (v78/critique.md): oboe takes the second head entry at 92; Bsn 1 countermelody under the coda's tune at 345–348; timpani alone at 135.

## Cycle 76 (lens 6 playability, Rimsky-Korsakov ch. I) v76 → v77
All 6 accepted (v77/critique.md): horns a degree louder at 101/105/301/305; "sul A" shortened; Fl 1 breath at 44; harp non arpegg., harmonics split, coda pedal setting at 333.

## Cycle 75 (lens 5 engraving, MOLA on parts) v75 → v76
All 5 accepted (v76/critique.md): instrumental parts created (29 PDFs, cues, page turns, fermatas); Bsn 2 hairpin at 203–204. promote.sh rebuilds parts each promotion. v75 rendered with r07 for Dan (v75/score-r07.mp3).

## Cycle 74 (lens 4 orchestration, Adler ch. 5) v74 → v75
All 3 accepted (v75/critique.md): contrabassoon rests 121–124/277–280; Fl 1 rests 177–184 (strings alone for the first string statement); Cl 2 A3 at 331.

## Cycle 73 (lens 3 form, Aldwell & Schachter 6–8) v73 → v74
Both accepted (v74/critique.md): dominant of A at the reprise fugato seam 296 (the viola entry's fourth bar changes; theme A itself does not, so the finale was not told); plain V at theme A's soft half cadences.

## Cycle 72 (lens 2 harmony, Aldwell & Schachter 30–31) v72 → v73
Accepted: A♯°7 at 88. Rejected: B–D–F–G♯ at 101–102/301–302 (the finale's stop chord; BRIEF.md clarified: reserved in any spelling and role). Do-not-touch: no B–D–F–G♯/A♭ chord anywhere in the scherzo.

## Cycle 71 (lens 1 orchestration of melody, Adler ch. 11) v71 → v72
Both accepted (v72/critique.md): horn and cellos carry the second idea in the tenor at 281–287; violas join the falling line at the fff peak 336–338.

## Cycle 70 (lens 10 cyclic, Aldwell & Schachter Unit 23) v70 → v71
Accepted (v71/critique.md): Vln I C5→B4 at 202–203. Documents: harp E4 at 375 noted as the E4 the finale's E♭4 answers; stale mvt I/II records reported to the coordinator. Do-not-touch: Vln II G4–E4 at 358–359.

## Cycle 69 (lens 9 holistic, Tchaikovsky 4/iii; Adler part 2 examples) v69 → v70
Both accepted (v70/critique.md): Fl 1 enters at 217 in the trio return (record moved, not a theme change); Vln I mp at 253. No regressions since v59.

## Cycle 68 (lens 8 expression, MOLA) v68 → v69
All 3 accepted (v69/critique.md): low strings pp at 349; wind phrase slurs on the trio tune; "espress." spelled one way.

## Cycle 67 (lens 7 texture, Sebesky ch. 3) v67 → v68
All 3 accepted (v68/critique.md): Vln II lower octave at 113–120; flutes mf over the violins at 45 and 209; Bsn 1 rests in the sub. p second idea. v67 rendered with r04 for Dan (v67/score-r04.mp3).

## Cycle 66 (lens 6 playability, Adler App. A) v66 → v67
All 3 accepted (v67/critique.md): Hn 1 lower in the tuttis 105–120/305–320 (Hn 3 in the middle); bassoon rests at 112, 312 and 208.

## Cycle 65 (lens 5 engraving, Gould) v65 → v66
3 of 4 applied (v66/critique.md): flute part-combine clean-up 105–108, 305–308, 316; harp clef at 351; Hn 4 breath placement. Rejected: removing Fl 2/Cl 2 G♯ at 209 (keeps c050's completed motto tail). Do-not-touch: Fl 2/Cl 2 G♯ at 209.

## Cycle 64 (lens 4 orchestration, Adler ch. 11) v64 → v65
All 3 accepted (v65/critique.md): trumpet motive x pitches fitted to the harmony at 113/115/119 and 313/315/319; tuba E1 at 339.

## Cycle 63 (lens 3 form, Adler ch. 15, 17) v63 → v64
Accepted (v64/critique.md): sub. p at 121 with Fl 1/Ob 1 joining at 125 and a crescendo to f at 129, so 101–132 is no longer one loud block (closes c059's open point). Not a theme change (record lines moved).

## Cycle 62 (lens 2 harmony, Aldwell & Schachter 28–29) v62 → v63
Accepted (v63/critique.md): French sixth at retransition 244 (no German sixth anywhere: it contains C–E–G).

## Cycle 61 (lens 1 melody, Aldwell & Schachter Unit 21) v61 → v62
Both accepted (v62/critique.md): theme change, the trio tune's cadence becomes a 4–3 suspension (all statements and the coda); 7/6–5 suspension in the violins at 195–196.

## Cycle 60 (lens 10 cyclic, Sebesky ch. 9) v60 → v61
Accepted (v61/critique.md): Hn 2 rests under the motto tail 357–360. Documents: scherzo.md D♯4 wording corrected; themes-scherzo.md notes that the trio tune and second idea derive from the horn call; finale told both.

## Cycle 59 (lens 9 holistic, Beethoven 3/iii; Adler part 1 examples) v59 → v60
Accepted (v60/critique.md): duplicate rehearsal letters/tempo marks removed (brass marks on the Horns 1·2 staff). Recorded but not changed: four loud arrivals before the trio (41, 72, 104, 121) against Beethoven's long pp; a later form or holistic critic may weigh it again.

## Cycle 58 (lens 8 expression, Sebesky ch. 6) v58 → v59
All 3 accepted (v59/critique.md): swells in the second idea's melody 45–52, 121–128; accompaniment pp under the motto tail at 357–360; character words at 73, 185, 189, 269.

## Cycle 57 (lens 7 texture, Sebesky ch. 1) v57 → v58
All 3 accepted (v58/critique.md): thinner middle in the tutti theme A (105–120, 305–320); Vln II lower at 95; reprise bass F♯ at 313 (iiø7).

## Cycle 56 (lens 6 playability, Adler ch. 12, 14) v56 → v57
All 3 accepted (v57/critique.md): timpani f in the tuttis at 105 and 305; rolls tied; ff on the downbeat at 104 and 304.

## Cycle 55 (lens 5 engraving, Adler ch. 18) v55 → v56
5 of 6 applied (v56/critique.md): tempo/letters above the brass; soft sticks at 146; missing dynamics at 37, 168, 361. Kept B6 at 336 without 8va.

## Cycle 54 (lens 4 orchestration, Adler ch. 8) v54 → v55
Both accepted (v55/critique.md): Fl 1 unison with Ob 1 at 29–34 (no early A6); Hn 2 enters on beat 2 at 212.

## Cycle 53 (lens 3 form, Aldwell & Schachter Unit 18) v53 → v54
Accepted (v54/critique.md): pizzicato iv6 bass at retransition 244 (bass A–C–B into V). Large form again judged sound; no change.

## Cycle 52 (lens 2 harmony, Aldwell & Schachter 24–25) v52 → v53
All 3 accepted (v53/critique.md): reprise 273–276 D7 → V6/5 → i instead of a five-bar B7; sevenths resolved in register at 104/304 (Fl 1 G5) and 44 (Cl 2 B3). Open: leading tones doubled in outer voices at 49, 51 (would need the c032 sequence rewritten).

## Cycle 51 (lens 1 melody, Sebesky ch. 6–7) v51 → v52
All 4 accepted (v52/critique.md): Fl 1 rests 169–176; Bsn 1's tune head freed at 233–236; cello counter-melody moves on at 172, 176, 212, 216; link Hn 1 foreshadows the trio tune at 147–148. v51 rendered with r07 for Dan (v51/score-r07.mp3, 4:38).

## Cycle 50 (lens 10 cyclic, Rimsky-Korsakov prefaces and ch. IV) v50 → v51
All 3 accepted (v51/critique.md): woodwinds p< at 329–332; Fl 2/Cl 2 reach G♯ at 209; inner voices swapped at 357–360 (Hn 1 motto line unchanged). Joins with mvt II v201 and finale v72 match.

## Cycle 49 (lens 9 holistic, Dvořák 7/iii; Rimsky-Korsakov examples 261–312) v49 → v50
All 5 accepted (v50/critique.md): reprise flute line at 254–266 without false relations; bass B at 354; accompaniment swell at 217–221; bassoons rest 225–228; brass re-entries pp at 101, 201, 301.

## Cycle 48 (lens 8 expression, Aldwell & Schachter Unit 3) v48 → v49
Both accepted (v49/critique.md): the whole orchestra except horns and upper woodwinds plays the coda hemiola at 337–338; tenuto on the cadential 6/4 at 353.

## Cycle 47 (lens 7 texture, Rimsky-Korsakov ch. III) v47 → v48
All 4 accepted (v48/critique.md): four real parts in the F-major episode's wind chord 73–88; codetta 229–236 voiced around Cl 1's tune head; Hn 1 B4 not A4 at 211 and 222; horns mf at 197.

## Cycle 46 (lens 6 playability, Adler ch. 9–10) v46 → v47
All 3 accepted (v47/critique.md): horn lines redistributed at 105–132 and 305–320 (Hn 1 rests from 121); breaths for Hn 4 (116, 316) and Hn 1·2 (216).

## Cycle 45 (lens 5 engraving, MOLA) v45 → v46
All 8 accepted (v46/critique.md): missing dynamics at 121, 193, 224; shared clarinet staff dynamics at 87 and 229; rehearsal letters added at 169, 225, 277, 357 (letters after K shifted; use bar numbers in this log); G.P. at 340; harp pedal text placement; duration on page 1.

## Cycle 44 (lens 4 orchestration, Adler ch. 15) v44 → v45
All 4 accepted (v45/critique.md): Fl 1 off the coda's last tune statement (Cl 1 lower octave instead); reprise second idea re-scored by entries (Ob 1 281, Fl 1 285; record updated, notes unchanged, not a theme change); filled middle of the ff A chord at 72 and 300; Cl 2 G4 at 339.

## Cycle 43 (lens 3 form, Aldwell & Schachter 16, 19) v43 → v44
All 3 accepted (v44/critique.md): final cadence 353–356 holds the cadential 6/4 two bars; bass clarinet bridges 139–141; MIDI steps for the fermatas at 340 and 376. Large form: no change.

## Cycle 42 (lens 2 harmony, Aldwell & Schachter 22–23) v42 → v43
All 4 accepted (v43/critique.md): bar 79 C7/E → vii°7 of F (no C–E–G sound anywhere now; cmajor.py cannot see a C–E–G inside a seventh chord, so critics should check by eye); iv at trio codetta 235; violas 358–360 no longer swallow the motto's A4 (Hn 1 line unchanged; finale told); cross relations at 72–73, 85–87, 192–193 taken by one voice.

## Cycle 41 (lens 1 melody, Adler ch. 7) v41 → v42
Both accepted (v42/critique.md): coda 345–348 tune phrase Cl 1 → Ob 1 (record line updated, notes unchanged, so not a theme change); reprise call 269–270 to a Bsn 1 staccato solo with C.a. holding B.

## Cycle 40 (lens 10 cyclic, Adler ch. 1, 15) v40 → v41
Accepted: bar 7–8 clarinets E5/G4 (no E4), so the horn call's D♯4 and movement II's last E♭4 stay unresolved for the finale (IV 219–220). Finale told; coherence/scherzo.md updated to v41. No change: trio tune not quoted in the finale. Do-not-touch: no E4 at bars 7–8; horn call D♯4 at 5–6 (finale relies on it).

## Cycle 39 (lens 9 holistic, Bruckner 7/iii; Rimsky-Korsakov examples 201–260) v39 → v40
All 3 accepted (v40/critique.md): 197–200 held G♯s moved so the tune's A4 does not rub in unison (fixes a c037 side effect); horns enter pp at 331–332 and crescendo into 333; the second idea's third statement 277–288 gets its own dynamics (sub. p, cresc., f at 285).

## Cycle 38 (lens 8 expression, Casanelles ch. 4, 6) v38 → v39
Both accepted (v39/critique.md): melody-only swell on the trio tune's third phrase in all four statements; swell on theme A's climb to C6 at 23–24 and 263–264. Kept bar 301's winds p under strings sf-p (Rimsky-Korsakov PDF 129).

## Cycle 37 (lens 7 texture, Adler ch. 16) v37 → v38
All 4 accepted (v38/critique.md): independent arco cello line in the reprise 253–268; dovetailed suspensions fill 244 and 248 in the retransition; Cl 1 and violas combine the trio tune's first phrase with the oboe call at 197–200 (new recorded statement, not a theme change, so no message to the finale); cellos rest 153–168 so their entry at 169 is fresh.

## Cycle 36 (lens 6 playability, Adler ch. 6–7) v36 → v37
All 7 accepted (v37/critique.md): bass clarinet takes the link's pp pedal; rests for Fl 1/Cl 1 before 209; Fl 1 upper octave in the exposition tutti; Fl 1 out of its weak low register at 40/44; p not pp on high flute lines; woodwind breaths; bass clarinet label.
