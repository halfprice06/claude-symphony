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
  - Theme A's tail G–F♯–F–E (the motto's tail on E's degrees).
  - (Added 2026-10-19, third series) Closing timpani motive x at 363–371 (B–B–B–E; pp at 363 and 367, ppp near the rim at 371): the finale v231 quotes it at IV 9. Theme A bar 2 G5–F♯5–F5–E5 in its register: movement I bar 79 and finale 273–275 quote it at pitch. Tell those threads before changing either. Hn 3·4 "senza sord." at their first entry (73). Timpani label at bar 1.

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
- v122 (cycle 121): trio tune T, bar 6 of every statement (158, 174, 214; coda 346 in A major). Old cis''2 fis''4. New cis''4 fis''2 (the second phrase's peak on beat 2 and held, not the first phrase's rhythm a step higher; open since cycle 1). Record refreshed; finale told (it does not quote T).
- v322 (cycle 321): trio tune T, bar 3 of every statement. Old D♯5 (dotted crotchet)–C♯5 (quaver)–B4; new D♯5–F♯4–B4, a falling sixth (Cl 1 155, Vln I/II 171, Cl 1/Vln II/Vla 199, Cl 1/Vln I/Vln II 211; Hn 3 343 in A: G♯4–B3–E4, was G♯4–F♯4–E4). Head G♯4–A4–B4–E5 unchanged. Record refreshed (51/51); finale and movement I told.
- v332 (cycle 331): trio tune T, bars 3–4. Old dis''4. fis'8 b'4 | a'4 gis'2. New dis''4. fis'8 a'4~ | a'4 gis'2 (the V7's seventh held over the bar line as a 4–3 suspension, A&S Ex. 21-23a), in all 7 statements incl. coda Hn 3 in A. Record refreshed (tie merges notes; %@ counts adjusted); finale and movement I told (neither quotes bars 3–4).
- v384 (cycle 383): second idea, reprise antecedent 277–280 only (Fl 1, Ob 1 an octave lower). Old b''2 g''4~ | g''4 e'''2 …; new b''2 gis''4~ | gis''4 e'''2 … (E major, 280 V6/5 of iv, minor again at 281). New record line secondIdeaEmaj; exposition statements 45 and 121 unchanged. Finale told (it does not quote the second idea).

- v412 (cycle 411): second idea. Each phrase's first minim becomes a dotted crotchet and a passing quaver, tie over the bar line kept: G major 45/49 old d'''2 b''4~ | e'''2 cis'''4~, new d'''4. c'''8 b''4~ | e'''4. d'''8 cis'''4~; E minor 121/125 and 281 old b''2 g''4~ | c'''2 a''4~, new b''4. a''8 g''4~ | c'''4. b''8 a''4~; reprise E-major antecedent 277 old b''2 gis''4~, new b''4. a''8 gis''4~ (all doubling octaves alike). Record refreshed. No other movement quotes the second idea, so no message was needed.
- v413 (cycle 412): second idea, E-minor consequent bar 8 (128, 284, all octaves): old dis'''4 b''4. cis'''8, new dis'''4 cis'''4. b''8 (D♯–C♯–B over VII°7 of V, bass F♯–A♯–B). Record refreshed; no message needed.
- v422 (cycle 421): trio tune T, bars 7–8 (159–160 Cl 1, 175–176 Vc, 215–216 Cl 1/Vln I/II): old e''4. dis''8 cis''4 | ais'4 b'2, new e''4. dis''8 ais'4~ | ais'4 b'2 (7–8 suspension of the leading tone). Coda Ob 1 345–348 keeps the old form (record line trioTcoda). Head unchanged; movement I quotes only the head and the finale does not quote T, so no message was needed.
- v442 (cycle 441): second idea's cadence (bars 10–11 of each statement: 54–55, 130–131, 286–287, all octaves): G old a''2 fis''4 | a''4 g''2, new b''2 a''4~ | a''4 g''2; E minor old fis''2 dis''4 | fis''4 e''2, new g''2 fis''4~ | fis''4 e''2 (3–2–1 in hemiola minims, 9–8 tie). Record refreshed; no other movement quotes it.
- v452 (cycle 451): second idea, bar 9 of each statement (53, 129, 285; Vln I/II, Fl 1, Ob 1): G old d'''4 b''4 g''4, new d'''4 e'''8 d''' c'''4; E minor old b''4 g''4 e''4, new b''4 cis'''8 b'' a''4 (upper neighbour + passing note in motive x's rhythm; low doubling at 285 keeps B–G–E). Record refreshed; no other movement quotes it.
- v481 (cycle 480): trio tune T, the forte call 197–200 only (Cl 1, Vln II; violas an octave lower): bar 3 (199) old dis''4. fis'8 a'4~, new d''4. fis'8 a'4~ (Neapolitan sixth of C♯ minor, D over F♯, into A major at 201). Head and the other statements unchanged. New record line trioTcall; no other movement quotes this statement.

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

## Batch checkpoint after cycle 96 (2026-10-16)
v88–v97 promoted (cycles 87–96); checkpoint PR to main. Next: cycle 97 reviews v97 (lens 7 texture).

## Batch checkpoint after cycle 106 (2026-10-16)
v98–v107 promoted (cycles 97–106); added to checkpoint PR #21. Next: cycle 107 reviews v107 (lens 7 texture).

## Batch checkpoint after cycle 116 (2026-10-16)
v108–v117 promoted (cycles 107–116); added to checkpoint PR #21. Next: cycle 117 reviews v117 (lens 7 texture).

## Batch checkpoint after cycle 126 (2026-10-16)
v118–v127 promoted (cycles 117–126); added to checkpoint PR #21. Next: cycle 127 reviews v127 (lens 7 texture).

## Batch checkpoint after cycle 136 (2026-10-16)
v128–v137 promoted (cycles 127–136); added to checkpoint PR #21; v133 rendered with r07 for Dan (assets rebuilt to /mnt/project-files/render-assets/). Next: cycle 137 reviews v137 (lens 7 texture).

## Batch checkpoint after cycle 146 (2026-10-16)
v138–v147 promoted (cycles 137–146); added to checkpoint PR #21. Four cycles (133, 140, 141, 144) found nothing to change. Next: cycle 147 reviews v147 (lens 7 texture).

## Batch checkpoint after cycle 156 (2026-10-16)
v148–v157 promoted (cycles 147–156); added to checkpoint PR #21; v153 rendered with r07 for Dan. Next: cycle 157 reviews v157 (lens 7 texture).

## Batch checkpoint after cycle 166 (2026-10-17)
v158–v167 promoted (cycles 157–166); added to checkpoint PR #21. Next: cycle 167 reviews v167 (lens 7 texture).

## Batch checkpoint after cycle 176 (2026-10-17)
v168–v177 promoted (cycles 167–176); added to checkpoint PR #21. Next: cycle 177 reviews v177 (lens 7 texture).

## Batch checkpoint after cycle 186 (2026-10-17)
v178–v187 promoted (cycles 177–186); added to checkpoint PR #21. Next: cycle 187 reviews v187 (lens 7 texture).

## Loop finished after cycle 200 (2026-10-17)
v188–v201 promoted (cycles 187–200); added to checkpoint PR #21. v201 is the release copy. The 200-cycle loop is complete.

## Cycle 484 (lens 4 orchestration, Adler ch. 15 Scoring for Orchestra: unison-octave tutti, foreground and background (adler2 PDF 146-158) (sixth pass)) v484 → v485
Accepted: cellos on theme A at 333–335 (coda.ily). Do-not-touch: cellos back on the bass at 336–339; the bass E at 333–335 keeps basses, contrabassoon, bassoons, tuba.

## Cycle 483 (lens 3 form, Rimsky-Korsakov ch. IV Composition of the orchestra: tutti, range limits, transfer of phrases, sf-p, crescendo and diminuendo (rimsky-principles PDF 115-136) (sixth pass)) v483 → v484
Accepted: trumpets pp< at 332 (coda.ily, parts-cues.json). Do-not-touch: trumpets and low brass return together at 332 (c428).

## Cycle 482 (lens 2 harmony, Aldwell & Schachter Unit 17 Diatonic Sequences (aldwell-schachter PDF 263-288) (sixth pass)) v482 → v483
Accepted: Hn 1 C♯5 on beat 3 of 198 (tB.ily). Do-not-touch: Hn 1 resolves to A4 at 199 (c322).

## Cycle 481 (lens 1 melody, Adler ch. 3 Individual Bowed Strings: melodic writing for violin, viola, cello, bass (adler1 PDF 71-109) (sixth pass)) v481 → v482
Accepted: cellos on the second idea's low octave 45–55, Bsn 2 bass (sA.ily). Do-not-touch: the 45–55 statement is now full (Vln I/Fl/Ob, Vln II, Vla/C.a./Vc); add no more doublings there.

## Cycle 480 (lens 10 cyclic, Aldwell & Schachter Unit 28 the Neapolitan as a long-range device (aldwell-schachter PDF 482-502) (fifth pass)) v480 → v481
Accepted: Neapolitan sixth at 199 (tB.ily), B♭5 at 300 (dB.ily). Record: new line trioTcall for 197–200.

## Cycle 479 (lens 9 holistic, Adler part 2 transcription examples in ch. 16 (adler2 PDF 202-244) (fifth pass)) v479 → v480
Accepted: Fl 1 at 223–224 (tC.ily).

## Cycle 478 (lens 8 expression, Adler ch. 7 woodwind articulation and dynamics by register (adler1 PDF 184-232) (fifth pass)) v478 → v479
Accepted: Cl 1 octave up 329–332 (coda.ily). Do-not-touch: the F on beats 1–2 of 331 (finale IV 272).

## Cycle 477 (lens 7 texture, Adler ch. 8 Variety of orchestral treatments (adler1 PDF 251-281) (fifth pass)) v477 → v478
Accepted: Cl 1 answers at 194/196 (tB.ily). Do-not-touch: c302's sequence and the 196 breath.

## Cycle 476 (lens 6 playability, Adler ch. 4 Plucked Strings: harp and pedalling (adler1 PDF 110-124) (sixth pass)) v476 → v477
Accepted: harp harmonics at 149/151 (link.ily). Do-not-touch: the harp's only harmonics are 149, 151 and 375, the same chord.

## Cycle 475 (lens 5 engraving, Gould ch. 1: ledger lines, octave signs, rests (gould-behind-bars PDF 41-52) (sixth pass)) v475 → v476
Accepted: Hn 4 rest position at 166 (tA.ily). Print only.

## Cycle 474 (lens 4 orchestration, Rimsky-Korsakov appendix of single tutti chords (rimsky-principles PDF 505-510) and the tutti examples cited in ch. IV (sixth pass)) v474 → v475
Accepted: Hn 3·4 at 300 (dB.ily, parts-cues.json). Do-not-touch: bar 72 (Hn 3·4's first unmuted entry is 73).

## Cycle 473 (lens 3 form, Aldwell & Schachter Unit 32 Chromaticism in Larger Contexts (aldwell-schachter PDF 584-606) (sixth pass)) v473 → v474
Accepted: ♭II6 at 301–302 (dB.ily). Do-not-touch: the Italian sixth at 300 (c422) and the F/♭II at 331 (finale IV 272 link); the ♭II at 301 is a two-bar reminder, not a new episode.

## Cycle 472 (lens 2 harmony, Aldwell & Schachter Units 11-13 VI and IV6; supertonic and subdominant sevenths; other uses of IV and VI (aldwell-schachter PDF 163-210) (sixth pass)) v472 → v473
Accepted: 54 Cl 2/violas (sA.ily), 176 basses/Bsn 2 (tA.ily).

## Cycle 471 (lens 1 melody, Rimsky-Korsakov ch. II Melody: woodwind, brass, combined groups (rimsky-principles PDF 64-80) and the examples it cites (sixth pass)) v471 → v472
Accepted: C.a. lower octave of the second idea at 45–55 (sA.ily). Do-not-touch: 121–124 stays undoubled (soft, intimate).

## Cycle 470 (lens 10 cyclic, Aldwell & Schachter Unit 23 Mixture as a long-range device (aldwell-schachter PDF 386-397) (fifth pass)) v470 → v471
Accepted: Vln I G5 at 7–8 (intro.ily). Do-not-touch: no C♮ in 341–358 (♭6 must not precede ♮6, A&S PDF 388); Cl 2's G4 and no E4 at 7–8 (c040, c270).

## Cycle 469 (lens 9 holistic, Adler part 2 full-score examples in ch. 11 and 15 (adler2 PDF 18-54, 143-186) (fifth pass)) v469 → v470
Accepted: Hn 3 A3 at 163–164 (tA.ily).

## Cycle 468 (lens 8 expression, MOLA guidelines on dynamics, articulation and bowing marks in parts (mola PDF 1-16) (fifth pass)) v468 → v469
Accepted: swells 110–111/310–311 (sC.ily, dC.ily), Cl accents 281 (dA.ily), timpani pp 367 (coda.ily).

## Cycle 467 (lens 7 texture, Sebesky ch. 3 Voicing the strings; combining strings with winds (sebesky PDF 133-173) (fifth pass)) v467 → v468
Accepted: Vln II la metà 349–356 (coda.ily). Do-not-touch: c445's rejection of la metà at 169–184 stands (Vln II is the only harmony there).

## Cycle 466 (lens 6 playability, Adler ch. 3 Individual Bowed Strings: ranges and technique (adler1 PDF 71-109) (sixth pass)) v466 → v467
Accepted: sul A at 177–180 (tA.ily) and 349–352 (coda.ily). Playing word only.

## Cycle 465 (lens 5 engraving, Gould ch. 1: beams (gould-behind-bars PDF 31-41) (sixth pass)) v465 → v466
Accepted: beams.ily flat-beam stem minimum, Vln II 171 stems down (tA.ily). Print only.

## Cycle 464 (lens 4 orchestration, Rimsky-Korsakov ch. III Harmony: brass and combined groups; overlaying, crossing, enclosure (rimsky-principles PDF 100-114) (sixth pass)) v464 → v465
Accepted: Hn 1·2 tied thirds at 54–56 (sA.ily). Do-not-touch: c410's B♭4 at 56 and c282's bass D4 at 53–54.

## Cycle 463 (lens 3 form, Aldwell & Schachter Unit 26 Diatonic Modulation, incl. modulation and form (aldwell-schachter PDF 442-461) (sixth pass)) v463 → v464
No change. Do-not-touch: 60–61 and 64–65 (c373), now also because the leading tone belongs before the goal entry at 69.

## Cycle 462 (lens 2 harmony, Aldwell & Schachter Units 9-10 Leading to V; the Cadential 6/4 (aldwell-schachter PDF 134-162) (sixth pass)) v462 → v463
Accepted: ii°6 at 26 (sA.ily), viola 6/4 resolution at 355 (coda.ily). Do-not-touch: bass G at 118/266/318 (tenor countermelody steps G–A there).

## Cycle 461 (lens 1 melody, Rimsky-Korsakov ch. II Melody: strings, unison and octave doublings (rimsky-principles PDF 54-63) and the examples it cites (sixth pass)) v461 → v462
Accepted: Vln I octave above the cellos' T at 177–184, violas rest (tA.ily, parts-cues.json). Do-not-touch: the A6 is still first heard at 218 (c344); three string sections stay on T at 177–184 at most (c436). Don't flip 177–184 back and forth between violas and Vln I.

## Cycle 460 (lens 10 cyclic, Sebesky ch. 9 General Advice and ch. 1 (sebesky PDF 240-242, 11-20) (fifth pass)) v460 → v461
Accepted: C.a. inner line 358–360 (coda.ily, parts-cues.json). Do-not-touch: the 6–♭6–5 inner line under the motto tail at 357–360 is shared with movements II and IV.

## Cycle 459 (lens 9 holistic, Adler part 1 full-score examples in ch. 5 and 8 (adler1 PDF 137-165, 235-281) (fifth pass)) v459 → v460
Accepted: Vc/Cb arco under the answers at 31–44 (sA.ily). Do-not-touch: the opening statement 13–28 stays bare (c259, c359). Open: tenor clef for the cellos' F♯4 at 35–36 (engraving lens).

## Cycle 458 (lens 8 expression, Sebesky ch. 1 focus and variety, ch. 6 melodic considerations (sebesky PDF 11-20, 204-218) (fifth pass)) v458 → v459
Accepted: 277–280 accompaniment pp (dA.ily). Do-not-touch: 121–124 stays sub. p (two violin octaves carry the tune, c308).

## Cycle 457 (lens 7 texture, Sebesky ch. 1 Basics: balance, economy, focus, variety (sebesky PDF 11-20) (fifth pass)) v457 → v458
Accepted: Vln I solo alone 349–356 (coda.ily). Do-not-touch: Vln II alone carries the lower octave of T at 349–356.

## Cycle 456 (lens 6 playability, Adler ch. 2 Bowed String Instruments: divisi, bowing, harmonics (adler1 PDF 24-70) (sixth pass)) v456 → v457
Accepted: Vc/Cb pizz. 137–139 (sC.ily, link.ily, tA.ily). Do-not-touch: the reprise close at 321–324 stays arco (runs into the bowed coda).

## Cycle 455 (lens 5 engraving, Gould ch. 1: stave, clefs, noteheads, stems, tails (gould-behind-bars PDF 17-30) (sixth pass)) v455 → v456
No change. Do-not-touch: the closing Vln I G♯5 stays a stopped note (finale takes it as its first sound).

## Cycle 454 (lens 4 orchestration, Rimsky-Korsakov ch. I Comparison of resonance and combination of tone qualities, and ch. III Harmony: number of parts, distribution, strings, woodwind (rimsky-principles PDF 51-53, 81-99) (sixth pass)) v454 → v455
Accepted: flutes a2 at 105–108 (sC.ily). Do-not-touch: both theme-A tuttis (105, 305) have the flutes on top; no flute note above A6 there.

## Cycle 453 (lens 3 form, Aldwell & Schachter Unit 14 V as a Key Area (aldwell-schachter PDF 211-229) (sixth pass)) v453 → v454
Accepted: timpani B at 184 (tA.ily, parts-cues.json). Rejected: repeat of 13–56. Record: the half cadence at 159–160 is an applied V7/V since c421.

## Cycle 452 (lens 2 harmony, Aldwell & Schachter Unit 5 Procedures of Four-Part Writing (aldwell-schachter PDF 74-91) (sixth pass)) v452 → v453
Accepted: bass steps at 53, 128, 180, 284 (sA, sC, dA, tA). Do-not-touch: c412's VII°7 of V resolves by a rising semitone in the bass.

## Cycle 451 (lens 1 melody, Aldwell & Schachter Unit 20 Melodic Figuration (aldwell-schachter PDF 327-345) (sixth pass)) v451 → v452
Accepted (theme change): second idea bar 9 (sA, sC, dA). Do-not-touch: the second idea's descent 5–4–3–2–1 into the tied 9–8 cadence; C♯ (not C♮) at 129/285.

## Cycle 450 (lens 10 cyclic, Rimsky-Korsakov author's prefaces and ch. IV transfer of phrases (rimsky-principles PDF 13-23, 125-128) (fifth pass)) v450 → v451
Accepted: no change. Do-not-touch confirmed: the closing groups 361/365/369/373 (horn alone 365–368).

## Cycle 449 (lens 9 holistic, Rimsky-Korsakov examples No. 261-312 (rimsky-principles PDF 441-504) (fifth pass)) v449 → v450
Accepted: Hn 3 from 261 only (dA.ily, parts-cues.json); reduces c447. Do-not-touch: the reprise countermelody 253–268 grows phrase by phrase (cellos alone, then + Hn 3). Open: second idea's memorability (scoring readings give no reason to change its notes).

## Cycle 448 (lens 8 expression, Aldwell & Schachter Unit 3 Rhythm and Meter: accent, hypermeter (aldwell-schachter PDF 47-57) (fifth pass)) v448 → v449
Accepted: cadence hairpins at 54–55, 130–131, 286–287 (sA, sC, dA). Do-not-touch: every melodic suspension swells into the dissonance and falls to the resolution.

## Cycle 447 (lens 7 texture, Rimsky-Korsakov ch. III overlaying, crossing and enclosure (rimsky-principles PDF 106-114) and the examples cited (fifth pass)) v447 → v448
Accepted: Hn 3 with the cellos at 253–268 (dA.ily, parts-cues.json). Kept: Hn 1/Hn 4 octaves at 105/305, Cl 2 inside the horns at 130, Hn 2 between bassoons at 284, clarinets under trumpets 101–103.

## Cycle 446 (lens 6 playability, Sebesky ch. 2 Wind instruments (sebesky PDF 21-110) (fifth pass)) v446 → v447
Accepted: no change. Do-not-touch: mixed unisons at 41–43/273–275; flutes' octave layout 109–120; horn pairs 336–338; breathing plan (104, 160, 176, 196, 216, 304; Hn 3 covers 365–369).

## Cycle 445 (lens 5 engraving, Adler ch. 2 notation of bowings, divisi and harmonics (adler1 PDF 30-55) as engraving rules (fifth pass)) v445 → v446
Accepted: \upb at 45 and 121 (global.ily, sA.ily, sC.ily). Rule: use \upb / \dnb (not bare \upbow / \downbow) at the start of a slurred string phrase.

## Cycle 444 (lens 4 orchestration, Casanelles ch. 6 spectral orchestration and acoustic mixing in Mahler's First Symphony (hyper-orchestra PDF 257-290) (fifth pass)) v444 → v445
Accepted: Vln II and violas rest 233–236 (tC.ily, parts-cues.json).

## Cycle 443 (lens 3 form, Aldwell & Schachter Unit 15 III and VII (aldwell-schachter PDF 230-247) (fifth pass)) v443 → v444
Accepted: Vln II at 330 (coda.ily). Do-not-touch: 330 is a clean ♮VII (D–F♯–A) in all strings.

## Cycle 442 (lens 2 harmony, Aldwell & Schachter Unit 27 Seventh chords with added dissonance (aldwell-schachter PDF 463-481) (fifth pass)) v442 → v443
Accepted: senza sord. at 1 (Vln I) and 13 (Vln II, Vla) (intro.ily, sA.ily). Rejected: V♭9 at 103–104/301–304, 9ths at 48–53 (stop chord), V♭9 by mixture at 202–208. Do-not-touch: upper strings enter senza sord. after movement II's muted coda.

## Cycle 441 (lens 1 melody, Aldwell & Schachter Unit 3 Rhythm and Meter (aldwell-schachter PDF 47-57) (fifth pass)) v441 → v442
Accepted (theme change): second-idea cadence (sA, sC, dA). Rejected: 5–2–1 close. Do-not-touch: the second idea's cadences are hemiolas with the tied 9–8; the phrase lengths (quoted bar numbers).

## Cycle 440 (lens 10 cyclic, Adler ch. 1 The Orchestra, Yesterday and Today, and ch. 15 additional thoughts (adler1 PDF 19-23, adler2 PDF 187-196) (fifth pass)) v440 → v441
Accepted: Vln II rests 361–364 (coda.ily). Do-not-touch, reason replaced: 365–368 the upper G♯5 rests between Fl 1 (to 364) and Vln I (from 369) because the close reverses the opening (pair → horn alone at 1–6, horn alone → pair at 365–376) and each four-bar group 361/365/369/373 changes colour on its downbeat around one timpani motive x (c440, replacing c140/c340's 'horn alone mirrors bars 1–2', false since c430). Kept: violas' G♯4 with Hn 1 at 237–239.

## Cycle 439 (lens 9 holistic, Rimsky-Korsakov examples No. 201-260 (rimsky-principles PDF 376-440) (fifth pass)) v439 → v440
Accepted: Fl 1 with the solo violin at 349–356 (coda.ily); reverses the v45 'no Fl 1' at 349 for the top octave only. Do-not-touch: coda T top octave = solo violin + Fl 1 (one player per instrument).

## Cycle 438 (lens 8 expression, Casanelles ch. 4 dynamics layering and expression in performance (hyper-orchestra PDF 145-161) and ch. 6 volume and dynamics (PDF 290-291) (fifth pass)) v438 → v439
Accepted: one solo violin at 349 (coda.ily). Do-not-touch: the coda's T is carried by single players throughout (Hn 3, Ob 1, solo violin, Hn 1).

## Cycle 437 (lens 7 texture, Adler ch. 16 The Orchestral Transcription (adler2 PDF 197-255) (fifth pass)) v437 → v438
Accepted: violas an octave lower at 197–200 (tB.ily). Do-not-touch: 197–200 layering (call a level above T; T in two octaves).

## Cycle 436 (lens 6 playability, Rimsky-Korsakov ch. I General review of orchestral groups (rimsky-principles PDF 24-50) (fifth pass)) v436 → v437
Accepted: Bsn 2 on the bass 169–180 (tA.ily, parts-cues.json). Note: the second trio statement 169–184 now carries cellos + Hn 3 (to 176) + violas (from 177) on T, Vln II con sord. quavers, arco basses + Bsn 2, Fl 1 answers; it is full, so later critics should thin rather than add there. Kept: Cbsn 210–220, harp LH 75–80, solo violins 349–356.

## Cycle 435 (lens 5 engraving, MOLA second pass, applied to the instrumental parts (parts.ily) rather than the score (fifth pass)) v435 → v436
Accepted: parts only (parts-cues.json, parts-gen.py, parts-lib.ily). Rule from c435: any cycle that moves or silences a line reruns the cue check and the parts' page-turn check.

## Cycle 434 (lens 4 orchestration, Adler ch. 5 Scoring for Strings (adler1 PDF 125-167) (fifth pass)) v434 → v435
Accepted: Vln II at 170 (tA.ily). Do-not-touch: in I6 chords the bass's third is not doubled in the top voice.

## Cycle 433 (lens 3 form, Aldwell & Schachter Units 6-8 I, V, V7 and their inversions: phrase structure (aldwell-schachter PDF 92-133) (fifth pass)) v433 → v434
Accepted: Cb G♯1 at 170 (tA.ily). Do-not-touch: T's three statements gain bass motion in turn (root under the drone 153, I6 at 170, moving bass from 209).

## Cycle 432 (lens 2 harmony, Aldwell & Schachter Units 30-31 Other chromatic chords; Chromatic voice-leading techniques (aldwell-schachter PDF 530-583) (fifth pass)) v432 → v433
Accepted: applied V7 at 48 (sA.ily). Do-not-touch: both phrases of the G-major second idea end with a rising chromatic bass (G♯–A at 48–49, C♯–D at 52–53).

## Cycle 431 (lens 1 melody, Adler ch. 11 Scoring for Brass: melodic presentation (adler2 PDF 19-36) (fifth pass)) v431 → v432
Accepted: Hn 3 with the cellos at 169–176 (tA.ily; Hn 4 adjusted). Open: the second idea is still the least memorable theme. Do-not-touch: horn melodies stay soft and middle-register.

## Cycle 430 (lens 10 cyclic, Casanelles ch. 5 Hyperorchestral aesthetic frameworks: themes and their transformation (hyper-orchestra PDF 199-254) (fifth pass)) v430 → v431
Accepted: Vln I G♯5 ppp at 1–2 (intro.ily). Rejected: Vln II G♯4 unison (hidden in the horn); violin held into 3 (clashes with D♯ at 5–6). Do-not-touch: the G♯ pair Hn 1 G♯4 + Vln I G♯5 frames the movement (1–2 and 369–376).

## Cycle 429 (lens 9 holistic, Rimsky-Korsakov examples No. 126-200 (rimsky-principles PDF 305-375) (fifth pass)) v429 → v430
Accepted: Cb arco pp 169–183 (tA.ily, tB.ily). Kept: bassoon above Hn 3 at 75–76/82–83 (c019's horn thirds; Rimsky Ex. 158). Do-not-touch: the two trio statements differ in bass (harp/pizz. 153–168, arco basses 169–183).

## Cycle 428 (lens 8 expression, Adler ch. 11 climactic uses of brass (adler2 PDF 37-40) and ch. 15 special effects (adler2 PDF 187-196) (fifth pass)) v428 → v429
Accepted: trumpets tacet 289–324 (dB.ily, dC.ily). Do-not-touch: the reprise tutti 305–320 without trumpets; trumpets and low brass return together at 333.

## Cycle 427 (lens 7 texture, Adler ch. 17 The Orchestra as Accompanist (adler2 PDF 256-290) (fifth pass)) v427 → v428
Accepted: C.a. rests 189–192 (tB.ily); timpani rests at 245 (retr.ily); four C.a. cues at 189 removed from parts-cues.json. Rejected: B4 suspension for Hn 1 at 199 (c322); Vln I in unison at 209–216 (c426's C♯5). Do-not-touch: timpani motive x at 241 and 249 (finale IV 143–145).

## Cycle 426 (lens 6 playability, Adler App. A ranges, professional and amateur limits (adler2 PDF 302-312) (fifth pass)) v426 → v427
Accepted: 'via sord.' at 185 (tB.ily, score.ly). Rejected: lower Hn 1 at 213–216. Do-not-touch: Hn 1 C♯5 held at 213–216 (common tone of the three chords).

## Cycle 425 (lens 5 engraving, Gould introduction and contents (gould-behind-bars PDF 7-13), then a second pass over PDF 17-68 for any rule not yet checked (fifth pass)) v425 → v426
Accepted: harp clef change at 358 (coda.ily). No sound change.

## Cycle 424 (lens 4 orchestration, Adler ch. 11 Scoring for Brass: homophonic unit and climactic uses (adler2 PDF 14-18, 37-54) (fifth pass)) v424 → v425
Accepted: Hn 1 G4 on tonic bars 105–120/305–320 (sC.ily, dC.ily). Do-not-touch: brass chords in the tuttis are complete (third present); single horns at 72 and 300 (Hn 3·4 senza sord. at 73; high horn unison kept for the finale).

## Cycle 423 (lens 3 form, Adler ch. 15 Additional thoughts and special effects (adler2 PDF 187-196) with ch. 17 The Orchestra as Accompanist (adler2 PDF 256-290) for pacing of background and foreground (fifth pass)) v423 → v424
Accepted: Vln II rests 229–232 (tC.ily). Do-not-touch: nothing held above the codetta's wind solos at 225–236.

## Cycle 422 (lens 2 harmony, Aldwell & Schachter Units 28-29 Neapolitan; Augmented Sixth Chords (aldwell-schachter PDF 482-529) (fifth pass)) v422 → v423
Accepted: Italian sixth at 300 in the strings (dB.ily), after rejections by c062, c242, c332 (c422 answered each). Do-not-touch: three different augmented-sixth approaches (French pp pizz. 244, Italian ff arco 300, French 331); the Neapolitan route 85–89; plagal close 357–360. Do not remove the Italian sixth at 300 without a stronger reason than c332's.

## Cycle 421 (lens 1 melody, Aldwell & Schachter Unit 21 Rhythmic Figuration: suspensions, anticipations, pedal (aldwell-schachter PDF 346-371) (fifth pass)) v421 → v422
Accepted (theme change): T bars 7–8 suspension (tA.ily, tC.ily). Kept: coda fragment 345–348 in the old form; second idea's ties consonant (c411); theme A peak at 24. Do-not-touch: T's two tied suspensions (bars 3–4 4–3, bars 7–8 7–8).

## Cycle 420 (lens 10 cyclic, Aldwell & Schachter Unit 26 modulation and form (aldwell-schachter PDF 442-461) (fifth pass)) v420 → v421
Accepted: Vc F♯3 held at 352 (coda.ily). Rejected: bass E under 349, harp D♯ at 347 (octaves), ii under T at 157, cutting 149–152 (renumbers quoted bars). Do-not-touch: c202's progression 351–353 with the held F♯ at 352.

## Cycle 419 (lens 9 holistic, Rimsky-Korsakov examples No. 61-125 (rimsky-principles PDF 241-305) (fifth pass)) v419 → v420
Accepted: violas on the second idea at 45–52 (sA.ily). Do-not-touch: the second idea's forte G-major statement in three octaves (Fl 1/Vln I, Ob 1/Vln II, violas).

## Cycle 418 (lens 8 expression, Adler ch. 2 bowing and its expressive effect (adler1 PDF 36-55) (fifth pass)) v418 → v419
Accepted: bowing at 173–178, 205–208, 209, 213–218 (tA, tB, tC). Do-not-touch: T's climax A at 162/178/218/350 is attacked down-bow, its crescendo up-bow; any slur change in T must recount the bows (c418 bows.py method).

## Cycle 417 (lens 7 texture, Adler ch. 15 polyphonic texture (adler2 PDF 172-186) (fifth pass)) v417 → v418
Accepted: cellos quote the second idea's head at 65–66 (sB.ily). Rejected: the quote in the reprise fugato 289–296 (keeps the reprise's shortening). Do-not-touch: the fugato stays strings alone; the second idea's head in the cellos at 65–66.

## Cycle 416 (lens 6 playability, Adler ch. 12 The Percussion Ensemble: timpani tuning and technique, cymbals, bass drum (adler2 PDF 55-91), and ch. 14 Scoring for Percussion (adler2 PDF 106-145) (fifth pass)) v416 → v417
Accepted: damped timpani strokes at 200, 287, 323, 339 (tB, dA, dC, coda). Do-not-touch: timpani strokes before a rest or a change of harmony are damped (staccato) unless meant to ring.

## Cycle 415 (lens 5 engraving, Adler ch. 18 Preparation of Score and Parts, and App. A (adler2 PDF 291-312) (fifth pass)) v415 → v416
Accepted: choir spacing and fixed page starts (score.ly, global.ily); five player labels (sA, tA, tC). Note for later critics: page starts are now fixed in global.ily (\tag #'score \pageBreak); a change that widens a system may need these moved. Do-not-touch: B6 at 336 without 8va; Hn 4 clef plan 229–236.

## Cycle 414 (lens 4 orchestration, Adler ch. 8 Woodwinds in the symphony orchestra and woodwind-string combinations (adler1 PDF 233-281) (fifth pass)) v414 → v415
Accepted: Fl 2 rests 205–209 (tB.ily, tC.ily), reversing c387. Do-not-touch: one flute (not two) over Hn 1's preview at 205–209 (c414 answered c387's Rimsky PDF 75 reason with Adler PDF 249–250: the flute only colours the horn line); do not flip back without a stronger reason.

## Cycle 413 (lens 3 form, Aldwell & Schachter Unit 18 6/3-chord techniques (aldwell-schachter PDF 289-303) (fifth pass)) v413 → v414
Accepted: Bsn 2 C♯4 at 146 (link.ily). Rejected: 6/3 run at 81–84 (C-major triad; c202). Do-not-touch: no 6/3 colour over E minor or F major anywhere (a 6 over E minor gives E–G–C, a C-major triad; c413).

## Cycle 412 (lens 2 harmony, Aldwell & Schachter Units 24-25 Remaining uses of seventh chords; Applied V and VII (aldwell-schachter PDF 398-441) (fifth pass)) v412 → v413
Accepted (theme change): VII°7 of V at 128/284 (sC.ily, dA.ily, global.ily breaks). Rejected: A♯ under T's cadences (clash with A♮); applied chords at 201–203 (C♮ mixture), 221–225, 329–332 (C-major triad). Do-not-touch: VII°7 of V at 128/284 with c392's tenths under it.

## Cycle 411 (lens 1 melody, Sebesky ch. 6 Melodic Considerations and ch. 7 The Importance of the Lyric (sebesky PDF 204-230) (fifth pass)) v411 → v412
Accepted (theme change): second-idea passing quavers at 45, 49, 121, 125, 277, 281 (sA.ily, sC.ily, dA.ily, global.ily break). Rejected: cello counter-line under 45–52 (horns re-strike, c027). Do-not-touch: the second idea's tie over the bar line, rising sixths and hemiola cadence 53–55.

## Cycle 410 (lens 10 cyclic, Aldwell & Schachter Unit 32 chromatic tonal areas and large-scale motion (aldwell-schachter PDF 584-606) (fifth pass)) v410 → v411
Accepted: Hn 1 B4–B♭4 at 56, rest at 57 (sA.ily, sB.ily). Kept: reprise join 288→289 (B3→B♭3 at 290, c293). Do-not-touch: the strings-only fugato entry at 57 (c007/c017/c254/c269). Note for the finale (no scherzo change): Hn 1 A♭4→G4 at IV 1–2 and the harp E4 → finale E♭4 links.

## Cycle 409 (lens 9 holistic, Rimsky-Korsakov examples No. 1-60 (rimsky-principles PDF 173-240) (fifth pass)) v409 → v410
Accepted: Vln II con sord. 169–192, senza sord. at 193 (tA.ily, tB.ily). Rejected: solo oboe call at 29–34 (protected register reason); pulse figure under 45–52 (horns re-strike). Open: memorability of the second idea and T (no scoring reading supports rewriting them).

## Cycle 408 (lens 8 expression, Rimsky-Korsakov ch. IV sf-p chords, crescendo and diminuendo (rimsky-principles PDF 129-136) (fifth pass)) v408 → v409
Accepted: woodwind p< at 101–104 (sB.ily). Do-not-touch: the crescendo into 105 and 305 is built by groups in order strings, woodwind, brass.

## Cycle 407 (lens 7 texture, Adler ch. 5 foreground, middleground, background; strings as accompaniment (adler1 PDF 132-167) (fifth pass)) v407 → v408
Accepted: Vln II quaver arpeggios 169–184 (tA.ily), 'unis.' at 193 removed (tB.ily). Do-not-touch: the second trio statement's background differs in rhythm from the first (harp off-beats 153–168 vs Vln II quavers 169–184).

## Cycle 406 (lens 6 playability, Adler ch. 9-10 Brass: horn, trumpet, trombone, tuba, endurance and ranges (adler1 PDF 282-329, adler2 PDF 1-13) (fifth pass)) v406 → v407
Accepted: Hn 1·2 mp at 209 (tC.ily). Rejected: stopped horn at 241 (soft-brass rule, G♯=A♭ turn); Hn 1 on T at 209 (c087, c251); soft trombone/tuba chord (kept for the finale). Do-not-touch: Hn 1 slur 72–74 (c042, c136, c266).

## Cycle 405 (lens 5 engraving, MOLA Guidelines for Music Preparation, whole document (mola PDF 1-16) (fifth pass)) v405 → v406
Accepted: no change. Rejected: Fl 1 mp at 253 (descant stays a level under Vln I's theme). Do-not-touch: winds doubling a string tune print a level under it (45, 125, 179, 197, 253) by design.

## Cycle 404 (lens 4 orchestration, Adler ch. 15 Scoring for Orchestra: homophonic and polyphonic texture (adler2 PDF 159-186) (fifth pass)) v404 → v405
Accepted: 197–200 call dynamics one level under T (tB.ily). Rejected: flutes an octave up at 113–114 (weakens the C6 peak at 116; B6/C7 protected); thinning the second idea 45–56 (c224/c314). Do-not-touch: T is the principal voice at 197–200, the call stays a level under it.

## Cycle 403 (lens 3 form, Aldwell & Schachter Units 16 and 19 5/3- and 6/4-chord techniques: prolongation (aldwell-schachter PDF 249-262, 304-325) (fifth pass)) v403 → v404
Accepted: no change. Do-not-touch reason reworded: the coda's A-major stage 341–348 is the upper neighbour IV in an I–IV–I prolongation of E (A&S PDF 256–257), not 'the upper 5th of IV' (c313). Rejected: a III divider in the retransition 241–252 (inside the protected G♯–G–F♯ span).

## Cycle 402 (lens 2 harmony, Aldwell & Schachter Units 22-23 Leading-tone seventh chords; Mixture (aldwell-schachter PDF 373-397) (fifth pass)) v402 → v403
Accepted: no change. Rejected: vii°7 or viiø7 in the trio codetta 226–236 (IV–iv mixture is the point, A&S Ex. 23-8); 44→45 hidden fifths (Cl 2 B3 takes the resolution); 331 F/F♯ cross-relation (F protected for finale IV 272). Open: none.

## Cycle 401 (lens 1 melody, Adler ch. 7 Individual Woodwinds: melodic writing, registers (adler1 PDF 184-232) (fifth pass)) v401 → v402
Accepted: no change. Do-not-touch wording: T in Cl 1 at 153 lies in the clarino except the bar-3 quaver F♯4 (throat; kept as a passing note). Open: the second idea is still the least memorable of the four ideas (c401 found no reading reason to change its notes).

## Cycle 400 (lens 10 cyclic, Release check: every do-not-touch item in HISTORY.md, every change in the last 100 cycles, and every book rule cited in them (fourth pass)) v400 → v401
Accepted: no score change; record wording fixes in coherence/scherzo.md and themes-scherzo.md. Open: none. Do-not-touch: as c400's closing line (G♯ frame, timpani labels at 1 and 376, motive x 9–12 and 363–371, theme A bar 2 at pitch, F at 331, motto close 357–360 and its preview 205–209, harp harmonics at 375, Cl 2 G4 at 7, single B6/fff at 336).

## Cycle 399 (lens 9 holistic, Casanelles ch. 6 analysis of Mahler's First Symphony (hyper-orchestra PDF 271-280) (fourth pass)) v399 → v400
c399 harp pp at 81; last cycle of the run

## Cycle 398 (lens 8 expression, Aldwell & Schachter Unit 21 suspensions and pedal points as expressive devices (aldwell-schachter PDF 346-371) (fourth pass)) v398 → v399
c398 swells on T's 4-3 suspension; Hn 9-8 diminuendo at 216

## Cycle 397 (lens 7 texture, Adler ch. 11 Scoring for brass: contrapuntal use (adler2 PDF 41-54) (fourth pass)) v397 → v398
c397 coda stretto 325–328 voices continue with the chromatic tail; horns mf at 45

## Cycle 396 (lens 6 playability, Adler ch. 6-7 Woodwind choir and individual woodwinds: breathing, registers, technique (adler1 PDF 168-232) (fifth pass)) v396 → v397
c396 bass clarinet B2 pedal at 245–252; Cl 2 breath at 196

## Cycle 395 (lens 5 engraving, Gould ch. 1-2: rhythmic spacing, spacing of symbols, chords, unisons, double-stemmed writing (gould-behind-bars PDF 53-68) (fifth pass)) v395 → v396
c395 system breaks 269–359 for rhythmic spacing

## Cycle 394 (lens 4 orchestration, Adler ch. 15 Scoring for Orchestra: unison-octave tutti, foreground and background (adler2 PDF 146-158) (fifth pass)) v394 → v395
c394 Vln II with Vln I on theme A at 309–320; part cues fixed

## Cycle 393 (lens 3 form, Rimsky-Korsakov ch. IV Composition of the orchestra: tutti, range limits, transfer of phrases, sf-p, crescendo and diminuendo (rimsky-principles PDF 115-136) (fifth pass)) v393 → v394
c393 low brass enter pp< at 332 and 101–104

## Cycle 392 (lens 2 harmony, Aldwell & Schachter Unit 17 Diatonic Sequences (aldwell-schachter PDF 263-288) (fifth pass)) v392 → v393
c392 parallels removed at 280 and 127–128

## Cycle 391 (lens 1 melody, Adler ch. 3 Individual Bowed Strings: melodic writing for violin, viola, cello, bass (adler1 PDF 71-109) (fifth pass)) v391 → v392
c391 violas double the cellos' T at 177–184

## Cycle 390 (lens 10 cyclic, Adler ch. 17 The Orchestra as Accompanist: transformations of material (adler2 PDF 256-290) (fourth pass)) v390 → v391
c390 cyclic check passed; Hn 3·4 rest at 205–208, harp lower at 345–348

## Cycle 389 (lens 9 holistic, Aldwell & Schachter: the literature example that opens each unit, Units 20-32 (fourth pass)) v389 → v390
c389 second-idea bass: no octaves with the tune at 45–52, 121–122, 277–278

## Cycle 388 (lens 8 expression, Adler ch. 10 brass dynamics, mutes, stopped horn (adler1 PDF 299-329) (fourth pass)) v388 → v389
c388 articulation: slurs 73–89, espress. at 3, Cl 2 ties

## Cycle 387 (lens 7 texture, Rimsky-Korsakov ch. II Melody in combined groups (rimsky-principles PDF 74-80) (fourth pass)) v387 → v388
c387 flutes a2 over Hn 1 at 205–209

## Cycle 386 (lens 6 playability, Adler ch. 4 Plucked Strings: harp and pedalling (adler1 PDF 110-124) (fifth pass)) v386 → v387
c386 harp: étouffez at 192 in the score

## Cycle 385 (lens 5 engraving, Gould ch. 1: ledger lines, octave signs, rests (gould-behind-bars PDF 41-52) (fifth pass)) v385 → v386
c385 parts: octave cue labels fixed

## Cycle 384 (lens 4 orchestration, Rimsky-Korsakov appendix of single tutti chords (rimsky-principles PDF 505-510) and the tutti examples cited in ch. IV (fifth pass)) v384 → v385
c384 bass spacing at 210–212 and 253–268

## Cycle 383 (lens 3 form, Aldwell & Schachter Unit 32 Chromaticism in Larger Contexts (aldwell-schachter PDF 584-606) (fifth pass)) v383 → v384
c383 THEME CHANGE (second idea, reprise only): E major at 277–280

## Cycle 382 (lens 2 harmony, Aldwell & Schachter Units 11-13 VI and IV6; supertonic and subdominant sevenths; other uses of IV and VI (aldwell-schachter PDF 163-210) (fifth pass)) v382 → v383
c382 harmony: IV6 at 209, Cl 1 A4 at 345

## Cycle 381 (lens 1 melody, Rimsky-Korsakov ch. II Melody: woodwind, brass, combined groups (rimsky-principles PDF 64-80) and the examples it cites (fifth pass)) v381 → v382
c381 coda: Cl 1 sixths under Ob 1's T at 345–348

## Cycle 380 (lens 10 cyclic, Aldwell & Schachter Unit 28 the Neapolitan as a long-range device (aldwell-schachter PDF 482-502) (fourth pass)) v380 → v381
c380 cyclic check passed; no change

## Cycle 379 (lens 9 holistic, Adler part 2 transcription examples in ch. 16 (adler2 PDF 202-244) (fourth pass)) v379 → v380
c379 coda: Cl 1 rests at 349–356

## Cycle 378 (lens 8 expression, Adler ch. 7 woodwind articulation and dynamics by register (adler1 PDF 184-232) (fourth pass)) v378 → v379
c378 winds: shaping hairpins at 81–83 and 345–347

## Cycle 377 (lens 7 texture, Adler ch. 8 Variety of orchestral treatments (adler1 PDF 251-281) (fourth pass)) v377 → v378
c377 coda: clarinets up an octave at 361–364

## Cycle 376 (lens 6 playability, Adler ch. 3 Individual Bowed Strings: ranges and technique (adler1 PDF 71-109) (fifth pass)) v376 → v377
c376 strings: no change

## Cycle 375 (lens 5 engraving, Gould ch. 1: beams (gould-behind-bars PDF 31-41) (fifth pass)) v375 → v376
c375 beams: shared-staff beamed stems lengthened

## Cycle 374 (lens 4 orchestration, Rimsky-Korsakov ch. III Harmony: brass and combined groups; overlaying, crossing, enclosure (rimsky-principles PDF 100-114) (fifth pass)) v374 → v375
c374 brass: horn 7ths at 207–208 split between colours

## Cycle 373 (lens 3 form, Aldwell & Schachter Unit 26 Diatonic Modulation, incl. modulation and form (aldwell-schachter PDF 442-461) (fifth pass)) v373 → v374
c373 form/modulation: no change, three record corrections

## Cycle 372 (lens 2 harmony, Aldwell & Schachter Units 9-10 Leading to V; the Cadential 6/4 (aldwell-schachter PDF 134-162) (fifth pass)) v372 → v373
c372 harmony: bass under cadential 6/4 at 181–182, VII6 at 76, Cl 2 at 129

## Cycle 371 (lens 1 melody, Rimsky-Korsakov ch. II Melody: strings, unison and octave doublings (rimsky-principles PDF 54-63) and the examples it cites (fifth pass)) v371 → v372
Coda T at 349–356 for two solo violins over the section an octave lower.

## Cycle 370 (lens 10 cyclic, Aldwell & Schachter Unit 23 Mixture as a long-range device (aldwell-schachter PDF 386-397) (fourth pass)) v370 → v371
Cl 2 at 42/274 clears the motto tail's b6; cyclic check passed.

## Cycle 369 (lens 9 holistic, Adler part 2 full-score examples in ch. 11 and 15 (adler2 PDF 18-54, 143-186) (fourth pass)) v369 → v370
Flutes bring back the quaver figure in the reprise tutti 305–320.

## Cycle 368 (lens 8 expression, MOLA guidelines on dynamics, articulation and bowing marks in parts (mola PDF 1-16) (fourth pass)) v368 → v369
Playing words restated and no longer struck by bar lines; Fl 1 p at 176.

## Cycle 367 (lens 7 texture, Sebesky ch. 3 Voicing the strings; combining strings with winds (sebesky PDF 133-173) (fourth pass)) v367 → v368
Texture: cellos thinned at 149–151 and 225–240; C.a. octave doubling at 41/273; Cl 1 levels balanced.

## Cycle 366 (lens 6 playability, Adler ch. 2 Bowed String Instruments: divisi, bowing, harmonics (adler1 PDF 24-70) (fifth pass)) v366 → v367
No change; string writing already follows Adler ch. 2.

## Cycle 365 (lens 5 engraving, Gould ch. 1: stave, clefs, noteheads, stems, tails (gould-behind-bars PDF 17-30) (fifth pass)) v365 → v366
Engraving: stem length and thickness to Gould; cello clef at 189.

## Cycle 364 (lens 4 orchestration, Rimsky-Korsakov ch. I Comparison of resonance and combination of tone qualities, and ch. III Harmony: number of parts, distribution, strings, woodwind (rimsky-principles PDF 51-53, 81-99) (fifth pass)) v364 → v365
Harp silent at 209–224 under the bowed bass.

## Cycle 363 (lens 3 form, Aldwell & Schachter Unit 14 V as a Key Area (aldwell-schachter PDF 211-229) (fifth pass)) v363 → v364
No change; the trio's short B area does all the unit asks of a modulation.

## Cycle 362 (lens 2 harmony, Aldwell & Schachter Unit 5 Procedures of Four-Part Writing (aldwell-schachter PDF 74-91) (fifth pass)) v362 → v363
Four-part-writing fixes in the reprise tutti and coda.

## Cycle 361 (lens 1 melody, Aldwell & Schachter Unit 20 Melodic Figuration (aldwell-schachter PDF 327-345) (fifth pass)) v361 → v362
No change; passing-tone rewrite of the second idea rejected because it broke the hemiola.

## Cycle 360 (lens 10 cyclic, Sebesky ch. 9 General Advice and ch. 1 (sebesky PDF 240-242, 11-20) (fourth pass)) v360 → v361
Timpani rolls now sound as rolls in the MIDI; cyclic check passed.

## Cycle 359 (lens 9 holistic, Adler part 1 full-score examples in ch. 5 and 8 (adler1 PDF 137-165, 235-281) (fourth pass)) v359 → v360
Cellos preview the tutti countermelody alone at 253–268.

## Cycle 358 (lens 8 expression, Sebesky ch. 1 focus and variety, ch. 6 melodic considerations (sebesky PDF 11-20, 204-218) (fourth pass)) v358 → v359
Expression words matched across doubled parts; Fl 1 p at 183.

## Cycle 357 (lens 7 texture, Sebesky ch. 1 Basics: balance, economy, focus, variety (sebesky PDF 11-20) (fourth pass)) v357 → v358
Harp chord at 343 cleaned; flute answer at 176 raised an octave.

## Cycle 356 (lens 6 playability, Sebesky ch. 2 Wind instruments (sebesky PDF 21-110) (fourth pass)) v356 → v357
Cl 1 out of the throat register at 133–136 and 321–323.

## Cycle 355 (lens 5 engraving, Adler ch. 2 notation of bowings, divisi and harmonics (adler1 PDF 30-55) as engraving rules (fourth pass)) v355 → v356
'unis.' at 193 moved to Vln II.

## Cycle 354 (lens 4 orchestration, Casanelles ch. 6 spectral orchestration and acoustic mixing in Mahler's First Symphony (hyper-orchestra PDF 257-290) (fourth pass)) v354 → v355
Harp rests at 214–215.

## Cycle 353 (lens 3 form, Aldwell & Schachter Unit 15 III and VII (aldwell-schachter PDF 230-247) (fourth pass)) v353 → v354
Violas at 314 remove a root-position augmented triad.

## Cycle 352 (lens 2 harmony, Aldwell & Schachter Unit 27 Seventh chords with added dissonance (aldwell-schachter PDF 463-481) (fourth pass)) v352 → v353
No change; corrected the recorded reason for the plain V7 at 101-104.

## Cycle 351 (lens 1 melody, Aldwell & Schachter Unit 3 Rhythm and Meter (aldwell-schachter PDF 47-57) (fourth pass)) v351 → v352
No change; rhythm and meter already follow the reading.

## Cycle 350 (lens 10 cyclic, Rimsky-Korsakov author's prefaces and ch. IV transfer of phrases (rimsky-principles PDF 13-23, 125-128) (fourth pass)) v350 → v351
No score change; shared theme checker now checks pitch; records updated.

## Cycle 349 (lens 9 holistic, Rimsky-Korsakov examples No. 261-312 (rimsky-principles PDF 441-504) (fourth pass)) v349 → v350
Flute answers the cellos' trio tune in its held notes at 172/176/183.

## Cycle 348 (lens 8 expression, Aldwell & Schachter Unit 3 Rhythm and Meter: accent, hypermeter (aldwell-schachter PDF 47-57) (fourth pass)) v348 → v349
Dynamic peaks moved to the attack of T's high A; timpani level steady into 105/305.

## Cycle 347 (lens 7 texture, Rimsky-Korsakov ch. III overlaying, crossing and enclosure (rimsky-principles PDF 106-114) and the examples cited (fourth pass)) v347 → v348
Two voice-leading fixes at 212–213 (Bsn 1) and 343 (violas).

## Cycle 346 (lens 6 playability, Rimsky-Korsakov ch. I General review of orchestral groups (rimsky-principles PDF 24-50) (fourth pass)) v346 → v347
Harp bass at 214–215 avoids two pedal changes on the ringing low A string.

## Cycle 345 (lens 5 engraving, MOLA second pass, applied to the instrumental parts (parts.ily) rather than the score (fourth pass)) v345 → v346
Parts: cues refreshed after c344; tempo words aligned with rehearsal letters.

## Cycle 344 (lens 4 orchestration, Adler ch. 5 Scoring for Strings (adler1 PDF 125-167) (fourth pass)) v344 → v345
Trio tune's second statement moved to the cellos (169–184), saving the high violin octave for 209.

## Cycle 343 (lens 3 form, Aldwell & Schachter Units 6-8 I, V, V7 and their inversions: phrase structure (aldwell-schachter PDF 92-133) (fourth pass)) v343 → v344
Codetta bass varied at 230 (E–G#–A–E).

## Cycle 342 (lens 2 harmony, Aldwell & Schachter Units 30-31 Other chromatic chords; Chromatic voice-leading techniques (aldwell-schachter PDF 530-583) (fourth pass)) v342 → v343
Cl 2 voice leading fixed at 86–88.

## Cycle 341 (lens 1 melody, Adler ch. 11 Scoring for Brass: melodic presentation (adler2 PDF 19-36) (fourth pass)) v341 → v342
No change; brass melodic presentation already follows the reading.

## Cycle 340 (lens 10 cyclic, Adler ch. 1 The Orchestra, Yesterday and Today, and ch. 15 additional thoughts (adler1 PDF 19-23, adler2 PDF 187-196) (fourth pass)) v340 → v341
Hn 1's pivot G# held into 149; records brought up to date.

## Cycle 339 (lens 9 holistic, Rimsky-Korsakov examples No. 201-260 (rimsky-principles PDF 376-440) (fourth pass)) v339 → v340
Second idea at 277-280 rescored for flute and oboe.

## Cycle 338 (lens 8 expression, Casanelles ch. 4 dynamics layering and expression in performance (hyper-orchestra PDF 145-161) and ch. 6 volume and dynamics (PDF 290-291) (fourth pass)) v338 → v339
Trio tune's second phrase restored to its level after the tied suspension; Vln I crescendo at 329.

## Cycle 337 (lens 7 texture, Adler ch. 16 The Orchestral Transcription (adler2 PDF 197-255) (fourth pass)) v337 → v338
Reprise fugato gets single pp wind notes on the entries' downbeats (289–296).

## Cycle 336 (lens 6 playability, Adler App. A ranges, professional and amateur limits (adler2 PDF 302-312) (fourth pass)) v336 → v337
Timpani muta labels reworded at 145/226; ranges and transpositions all checked.

## Cycle 335 (lens 5 engraving, Gould introduction and contents (gould-behind-bars PDF 7-13), then a second pass over PDF 17-68 for any rule not yet checked (fourth pass)) v335 → v336
Engraving: horn and clarinet solo labels at 213–236 and 341–365; label filter fixed.

## Cycle 334 (lens 4 orchestration, Adler ch. 11 Scoring for Brass: homophonic unit and climactic uses (adler2 PDF 14-18, 37-54) (fourth pass)) v334 → v335
No change; brass scoring already follows Adler ch. 11.

## Cycle 333 (lens 3 form, Adler ch. 15 Additional thoughts and special effects (adler2 PDF 187-196) with ch. 17 The Orchestra as Accompanist (adler2 PDF 256-290) for pacing of background and foreground (fourth pass)) v333 → v334
Horn drone starts at 149, four bars before the trio tune.

## Cycle 332 (lens 2 harmony, Aldwell & Schachter Units 28-29 Neapolitan; Augmented Sixth Chords (aldwell-schachter PDF 482-529) (fourth pass)) v332 → v333
French sixth on beat 3 of 331 between the Neapolitan 6/4 and V7.

## Cycle 331 (lens 1 melody, Aldwell & Schachter Unit 21 Rhythmic Figuration: suspensions, anticipations, pedal (aldwell-schachter PDF 346-371) (fourth pass)) v331 → v332
THEME CHANGE: T bars 3–4 gain a tied 4–3 suspension (A over the bar line to G#).

## Cycle 330 (lens 10 cyclic, Casanelles ch. 5 Hyperorchestral aesthetic frameworks: themes and their transformation (hyper-orchestra PDF 199-254) (fourth pass)) v330 → v331
No score change; shared records brought up to date with T's new bar 3 and c323-c330.

## Cycle 329 (lens 9 holistic, Rimsky-Korsakov examples No. 126-200 (rimsky-principles PDF 305-375) (fourth pass)) v329 → v330
No change; holistic check against Rimsky-Korsakov's examples found nothing to fix.

## Cycle 328 (lens 8 expression, Adler ch. 11 climactic uses of brass (adler2 PDF 37-40) and ch. 15 special effects (adler2 PDF 187-196) (fourth pass)) v328 → v329
No change; climactic brass and special effects already follow Adler.

## Cycle 327 (lens 7 texture, Adler ch. 17 The Orchestra as Accompanist (adler2 PDF 256-290) (fourth pass)) v327 → v328
Timpani answers the retransition heads at 91/94/97; accompaniment cleared under T's falling sixth at 199, 211, 343.

## Cycle 326 (lens 6 playability, Adler ch. 12 The Percussion Ensemble: timpani tuning and technique, cymbals, bass drum (adler2 PDF 55-91), and ch. 14 Scoring for Percussion (adler2 PDF 106-145) (fourth pass)) v326 → v327
Accepted: timpani E3–E3–E3–E2 at 333, octave E2+E3 at 339. Kept: reprise tutti timpani 305–320; ranges, retunings, sticks, rolls.

## Cycle 325 (lens 5 engraving, Adler ch. 18 Preparation of Score and Parts, and App. A (adler2 PDF 291-312) (fourth pass)) v325 → v326
Accepted: system labels at 111, 131 (Hn 2, Hn 3), 214 (Cl 1); Hn 3 label at 365. Kept: B6 at 336 without 8va, no tempo words over the timpani, mixed-language terms.

## Cycle 324 (lens 4 orchestration, Adler ch. 8 Woodwinds in the symphony orchestra and woodwind-string combinations (adler1 PDF 233-281) (fourth pass)) v324 → v325
Accepted: Hn 1 on the tail preview at 205–209 (Cl 2 rests). Kept: no held winds under theme A 13–28, unison at 41–43/273–275 (flutes would pass B6), 89–100 without held winds, tenor unison 281–287, tutti scorings 105–120/305–320.

## Cycle 323 (lens 3 form, Aldwell & Schachter Unit 18 6/3-chord techniques (aldwell-schachter PDF 289-303) (fourth pass)) v323 → v324
Accepted: violas B3 on beats 2–3 of 27/267. Kept: no parallel 6/3 run in the trio (201–204 c070/c177, 145–148 c051, 225–240), coda bass with ♭II 6/4 at 331 (finale IV 272), harp 6/3 chords 341–344, proportions.

## Cycle 322 (lens 2 harmony, Aldwell & Schachter Units 24-25 Remaining uses of seventh chords; Applied V and VII (aldwell-schachter PDF 398-441) (fourth pass)) v322 → v323
No change. Do-not-touch (critic): T's new bar 3 and the inner resolutions under it; Hn 1 B4→A4 at 198–199. Kept: 49–52 (second idea), 104→105/304→305, 212→213, 188→189, passing cross relations at 61/66/70/86/293/298 (c232).

## Cycle 321 (lens 1 melody, Sebesky ch. 6 Melodic Considerations and ch. 7 The Importance of the Lyric (sebesky PDF 204-230) (fourth pass)) v321 → v322
Accepted: THEME CHANGE, T bar 3 dis''4. fis'8 b'4 (was dis''4. cis''8 b'4) in all statements (155, 171, 199, 211, 343 in A). Record refreshed; finale and movement I told. Kept: second idea (every rewrite lost the rising sixth or the hemiola).

## Cycle 320 (lens 10 cyclic, Aldwell & Schachter Unit 26 modulation and form (aldwell-schachter PDF 442-461) (fourth pass)) v320 → v321
No change. Cyclic check clean against I v335, II v310, finale v294. Record corrected: horn D♯4→E4 steps (Hn 3 at 338–339 plays F♯4→E4, not D♯4).

## Cycle 319 (lens 9 holistic, Rimsky-Korsakov examples No. 61-125 (rimsky-principles PDF 241-305) (fourth pass)) v319 → v320
No change. Kept: Hn 3·4 sevenths and ninth at 308–319 (Hn 4 F♯3 would make octaves with the tune), Hn 1·2 suspensions at 55/216, Cl 1 A4 at 87, strings-only 169–184, trio key. Open: T and the second idea not memorable (c289–c319).

## Cycle 318 (lens 8 expression, Adler ch. 2 bowing and its expressive effect (adler1 PDF 36-55) (fourth pass)) v318 → v319
Accepted: Vln I/II up-bow at 277 (reverses c265), slur splits at 284 (violins, violas); Vc one bow per bar 293–294; Cb slurs 217–220. Kept: violas 65–69, Vc/Cb at 200, violins at 193, accents on up-bows at 45/49 and 101–104, staccato in the tutti.

## Cycle 317 (lens 7 texture, Adler ch. 15 polyphonic texture (adler2 PDF 172-186) (fourth pass)) v317 → v318
Accepted: Hn 4 on the cello countermelody at 217–224 (bass clef). Kept: coda build 325–332 (Rimsky's crescendo order), strings-only fugato 57–68 (c007), no horn on the coda countermelody 349–356 (c314).

## Cycle 316 (lens 6 playability, Adler ch. 9-10 Brass: horn, trumpet, trombone, tuba, endurance and ranges (adler1 PDF 282-329, adler2 PDF 1-13) (fourth pass)) v316 → v317
No change. Correction to c226: Ex. X-6 stacks horns I–IV from the top. Kept: Hn 1's last G♯ 368–376 at ppp; no soft low-brass chord (finale chorale); no stopped-horn echo at 241.

## Cycle 315 (lens 5 engraving, MOLA Guidelines for Music Preparation, whole document (mola PDF 1-16) (fourth pass)) v315 → v316
Accepted: max-systems-per-page 10 for parts 26, 27, 28, 30. Kept at 12: cello and winds (page turns or page count would get worse). Kept: rehearsal letters, harp pedal settings, timpani f at 200, viola f at 41.

## Cycle 314 (lens 4 orchestration, Adler ch. 15 Scoring for Orchestra: homophonic and polyphonic texture (adler2 PDF 159-186) (fourth pass)) v314 → v315
No change. Correction to c217: Hn 3·4 are free at 209–224, but no horn octave fits. Kept: coda T at 349–356 (c251), flutes held to 109/309 (c124), 45–56 spacing, T at pitch in four instruments at 197–200, builds at 101–104/301–304, fading chords at 339 and 361–376.

## Cycle 313 (lens 3 form, Aldwell & Schachter Units 16 and 19 5/3- and 6/4-chord techniques: prolongation (aldwell-schachter PDF 249-262, 304-325) (fourth pass)) v313 → v314
No change. Kept: coda proportions, 133–152, 241–252, 89–98, development key plans, length 4:38.

## Cycle 312 (lens 2 harmony, Aldwell & Schachter Units 22-23 Leading-tone seventh chords; Mixture (aldwell-schachter PDF 373-397) (fourth pass)) v312 → v313
No change. Kept: tritone to fifth inside V7 at 102–103/302–303, D→D♯ at 275–276 (c083), seventh resolutions at 104–105/304–305, viola passing seventh at 212–213, no vii°7 of E in the trio.

## Cycle 311 (lens 1 melody, Adler ch. 7 Individual Woodwinds: melodic writing, registers (adler1 PDF 184-232) (fourth pass)) v311 → v312
No change. Kept: T in Cl 1 at 153, Cl 1 at 81–88, no flute below B4, Fl/Ob unison at 29–36, Cbsn doubling at 213–220, codetta relay 225–236. Open: T's first phrase still the least memorable idea (c289, c299, c301, c309, c311).

## Cycle 310 (lens 10 cyclic, Aldwell & Schachter Unit 32 chromatic tonal areas and large-scale motion (aldwell-schachter PDF 584-606) (fourth pass)) v310 → v311
No change. Cyclic check clean against I v327, II v300, finale v288. Do-not-touch (added): T's head G♯4–A4–B4–E5 at 153 and the motive-x links (II 84–85 → III 9; III 363–371 → IV 9, 143) are relied on by movement I; tell that thread before changing them.

## Cycle 309 (lens 9 holistic, Rimsky-Korsakov examples No. 1-60 (rimsky-principles PDF 173-240) (fourth pass)) v309 → v310
No change. Open (c289, c299, c309): T and the second idea are well made but not memorable.

## Cycle 308 (lens 8 expression, Rimsky-Korsakov ch. IV sf-p chords, crescendo and diminuendo (rimsky-principles PDF 129-136) (fourth pass)) v308 → v309
No change. Kept: Hn 4 sub. p at 121 vs Hn 3 pp at 277 (c208), ff chord dying in one bar at 72, low brass f (soft-brass rule), Hn 1 p at 357, trio entries at 169/197/209/217, crescendo at 328 (c108).

## Cycle 307 (lens 7 texture, Adler ch. 5 foreground, middleground, background; strings as accompaniment (adler1 PDF 132-167) (fourth pass)) v307 → v308
Accepted: violas A4–G♯4 at 70/298. Kept: E4 meeting at 68, pizz. violas under held cellos 253–266, brief viola–cello meetings at 171/211/220, theme A off-beats (c006), fugato entry order.

## Cycle 306 (lens 6 playability, Adler ch. 6-7 Woodwind choir and individual woodwinds: breathing, registers, technique (adler1 PDF 168-232) (fourth pass)) v306 → v307
No change. Kept: Fl 1 at 37–56, Cbsn at 209–224 and its ninth at 220–221, flutes A6 ff at 110/310, Fl 1 A6 p at 254–266 (c036, c069), Bsn 1 breaths at 104/116, bass clarinet holds.

## Cycle 305 (lens 5 engraving, Gould ch. 1-2: rhythmic spacing, spacing of symbols, chords, unisons, double-stemmed writing (gould-behind-bars PDF 53-68) (fourth pass)) v305 → v306
Accepted: DynamicText vertical-skylines from extents in score.ly. Kept: accidentals after barlines (PDF 57), Fl 1 turn spacing at 255–267, crotchet width at 338 (c215).

## Cycle 304 (lens 4 orchestration, Adler ch. 15 Scoring for Orchestra: unison-octave tutti, foreground and background (adler2 PDF 146-158) (fourth pass)) v304 → v305
No change. Do-not-touch (critic): tutti layouts 105–120, 305–320, 333–339; trio foreground/background plan 149–240; closing page.

## Cycle 303 (lens 3 form, Rimsky-Korsakov ch. IV Composition of the orchestra: tutti, range limits, transfer of phrases, sf-p, crescendo and diminuendo (rimsky-principles PDF 115-136) (fourth pass)) v303 → v304
No change. Kept: Hn 1 p at 357, horn entries p< at 101/301/332, low brass f at 71/105/299/333 (soft-brass rule, c123, c266), violins mp at 169, harp mf at 209.

## Cycle 302 (lens 2 harmony, Aldwell & Schachter Unit 17 Diatonic Sequences (aldwell-schachter PDF 263-288) (fourth pass)) v302 → v303
No change. Do-not-touch (critic): 29–37, 45–55, 61–68, 73–78, 121–128/277–284, 185–196, 329–332, 357–360.

## Cycle 301 (lens 1 melody, Adler ch. 3 Individual Bowed Strings: melodic writing for violin, viola, cello, bass (adler1 PDF 71-109) (fourth pass)) v301 → v302
No change. Kept: T never in the cello section; second idea D6–A6 on the E string; 276→277 entry without breath (c286); bow change on T's tied A. Open: T's first phrase has no leap of its own (also c299).

## Cycle 300 (lens 10 cyclic, Release check: every do-not-touch item in HISTORY.md, every change in the last 100 cycles, and every book rule cited in them (third pass)) v300 → v301
No change. Release check passed (48 principles from the books behind cycles 200–299). Kept: clarinets inside the horns at 45–56, 121–128 (accepted earlier). Coherence: other movements' files in the checkout refreshed from /mnt.

## Cycle 299 (lens 9 holistic, Casanelles ch. 6 analysis of Mahler's First Symphony (hyper-orchestra PDF 271-280) (third pass)) v299 → v300
No change. Remaining gap noted by the critic: the second idea and trio tune are well made but not memorable; not rewritten on the last cycle because the finale quotes them. Do-not-touch (critic): closing page 357–376, soft trio 153–216, coda peak 333–339, F-major episode spacing 73–88.

## Cycle 298 (lens 8 expression, Aldwell & Schachter Unit 21 suspensions and pedal points as expressive devices (aldwell-schachter PDF 346-371) (third pass)) v298 → v299
No change. Kept: Hn 1 9–8 at 216 unmarked (15 pages with a hairpin; c198), hemiola 4–3s unmarked, suspension shadings, swells on T's tied A, dominant pedals into 105, 209, 253.

## Cycle 297 (lens 7 texture, Adler ch. 11 Scoring for brass: contrapuntal use (adler2 PDF 41-54) (third pass)) v297 → v298
No change. Kept: Hn 3 alone on the tenor line 305–320 (c114), 329–332 (c129, c279), fugato without brass.

## Cycle 296 (lens 6 playability, Adler ch. 4 Plucked Strings: harp and pedalling (adler1 PDF 110-124) (fourth pass)) v296 → v297
No change. Kept: low bass at 81–84, close chords in the trio and coda, repeated chords, harmonics at 375 with Hn 1's G♯4.

## Cycle 295 (lens 5 engraving, Gould ch. 1: ledger lines, octave signs, rests (gould-behind-bars PDF 41-52) (fourth pass)) v295 → v296
Accepted: \partCombineChords for the clarinets at 361–364 (Cl 2 B3 printed); rest positions at 209 and 366. Kept: Hn 3·4 treble clef at 153–168, B6 at 336 without 8va, tuba and harp ledger lines, Hn 4 rests at 166, second players' rests.

## Cycle 294 (lens 4 orchestration, Rimsky-Korsakov appendix of single tutti chords (rimsky-principles PDF 505-510) and the tutti examples cited in ch. IV (fourth pass)) v294 → v295
Accepted: Bsn 1 D3/G3 at 53–56; timpani f at 333, cresc. at 335, ff roll at 336. Kept: 211–212, 37–39, 92–94, the tutti and soft-chord layouts.

## Cycle 293 (lens 3 form, Aldwell & Schachter Unit 32 Chromaticism in Larger Contexts (aldwell-schachter PDF 584-606) (fourth pass)) v293 → v294
No change. Kept: 288→289 (c003), 133–152, 237–253 without an added F♮, coda weighting.

## Cycle 292 (lens 2 harmony, Aldwell & Schachter Units 11-13 VI and IV6; supertonic and subdominant sevenths; other uses of IV and VI (aldwell-schachter PDF 163-210) (fourth pass)) v292 → v293
No change. Kept: harp at 159 (c089/c093; each fix adds a fault), iv7 at 243 (C-major rule), no deceptive cadence in E minor (VI is C major).

## Cycle 291 (lens 1 melody, Rimsky-Korsakov ch. II Melody: woodwind, brass, combined groups (rimsky-principles PDF 64-80) and the examples it cites (fourth pass)) v291 → v292
Accepted: octave climb at 335 in Vln II, violas, C.a. Kept: coda T 341–356 scoring, Ob 1 octave change 197–198 (c117/c119), Bsn octaves 299–301, three winds on Vln I 113–116/313–316, T's rhythm.

## Cycle 290 (lens 10 cyclic, Adler ch. 17 The Orchestra as Accompanist: transformations of material (adler2 PDF 256-290) (third pass)) v290 → v291
No change. Cyclic check clean against I v313, II v300, finale v273. Notes for the stop: coherence/scherzo.md to list v282–v300; at the merge take only the scherzo's own coherence files from this branch; print version and date on the v300 title page.

## Cycle 289 (lens 9 holistic, Aldwell & Schachter: the literature example that opens each unit, Units 20-32 (third pass)) v289 → v290
Accepted: Cl 1 4–3 at 54–55, 130–131, 286–287 (answers the cycle 2 do-not-touch: rhythm and harmony unchanged). No structural change (Brahms's loud trio and unbroken motion would undo protected decisions).

## Cycle 288 (lens 8 expression, Adler ch. 10 brass dynamics, mutes, stopped horn (adler1 PDF 299-329) (third pass)) v288 → v289
Accepted: wind slurs with tenuto at 101–104/301–304, 336–338, 133–136/321–323, 141–148, 225–228; ties at 361–362 in Hn 2, Fl 1, Cl 1·2. Kept: horns ff>pp at 72, no mutes, horns 73–88 without hairpins, E pedal 357–360, low winds 333–335, clarinets 249–252.

## Cycle 287 (lens 7 texture, Rimsky-Korsakov ch. II Melody in combined groups (rimsky-principles PDF 74-80) (third pass)) v287 → v288
Accepted: viola beat 3 B3 at 106/118/306/318, C4–E4 at 110/310. Kept: tenor countermelody's tied E4 at 106/306 (c017, c187); 333–337, 113–116, 129/285, 349–355 follow the reading.

## Cycle 286 (lens 6 playability, Adler ch. 3 Individual Bowed Strings: ranges and technique (adler1 PDF 71-109) (fourth pass)) v286 → v287
No change. Kept: Vc G2–C4 at 280–281, Vln I A5–F6 at 330–331, crossings at 272–277, viola motive x pp at 326–332, Cb open A1 at 213, tied E at 361–364.

## Cycle 285 (lens 5 engraving, Gould ch. 1: beams (gould-behind-bars PDF 31-41) (fourth pass)) v285 → v286
Accepted: stems.ily second pass for middle-line beam groups (10 stems at 107, 307, 331). Kept: long Fl 1 stems 254–266, convex turn slopes at 189/193/195, Fl 1 run at 256, 8 middle-line pairs with disagreeing neighbours.

## Cycle 284 (lens 4 orchestration, Rimsky-Korsakov ch. III Harmony: brass and combined groups; overlaying, crossing, enclosure (rimsky-principles PDF 100-114) (fourth pass)) v284 → v285
Accepted: Tpt 1 B4 (was D♯5) at 104/304, same dynamic. Kept: horn minor ninth at 337, Tbn 1 seventh at 103–104, Cl 2 inside the horns at 121–128/277–280, octave woodwind over short trumpet strokes 105–119 (PDF 114), horns between Bcl and Bsn at 75–76/83 (c080).

## Cycle 283 (lens 3 form, Aldwell & Schachter Unit 26 Diatonic Modulation, incl. modulation and form (aldwell-schachter PDF 442-461) (fourth pass)) v283 → v284
No change. Do-not-touch (critic): pivot at 33–34; trio key plan 153–209; coda A major 341 with E pivot at 348; I–III–(IV, ♭II)–V plan of 13–105 and its reprise; proportions.

## Cycle 282 (lens 2 harmony, Aldwell & Schachter Units 9-10 Leading to V; the Cadential 6/4 (aldwell-schachter PDF 134-162) (fourth pass)) v282 → v283
Accepted: Hn 2 D4 at 53–55 (answers c223: no doubled fourth); 5–6 at 173 (Vc F♯) and 345 (Bsn 1 B); Bsn 1 and Vla F♯ at 220, held E kept. Kept: ii→I6 at 76–77 (c080, c192).

## Cycle 281 (lens 1 melody, Rimsky-Korsakov ch. II Melody: strings, unison and octave doublings (rimsky-principles PDF 54-63) and the examples it cites (fourth pass)) v281 → v282
No change. Kept: Vln I alone on C6 at 21–24/257–264; trio call 198–200 (protected c107/c117); tutti unison/octave switches (c010); fugato single-section entries; coda register hand-overs (c150, c191).

## Cycle 280 (lens 10 cyclic, Aldwell & Schachter Unit 28 the Neapolitan as a long-range device (aldwell-schachter PDF 482-502) (third pass)) v280 → v281
No change. Cyclic check clean against I v304, II v291, finale v265. Kept: leading tone at 332, tritone leaps 331–332, Cl 1 at 86; no Neapolitan in the trio or coda (would need C major).

## Cycle 279 (lens 9 holistic, Adler part 2 transcription examples in ch. 16 (adler2 PDF 202-244) (third pass)) v279 → v280
Accepted: duplicate Ob "1." at 197 removed. No structural change; a slower trio not re-raised (c129 reason stands). Do-not-touch (critic): trio colourings and hand-overs 185–200, fugato 57–72, build 89–104, reprise tutti 305–320, coda stretto 325–339, G.P. 340, closing page 357–376.

## Cycle 278 (lens 8 expression, Adler ch. 7 woodwind articulation and dynamics by register (adler1 PDF 184-232) (third pass)) v278 → v279
Accepted: "leggiero" Fl 1/Ob 1 at 29; hairpins on the trio calls 185–192 (Ob 1, C.a., Vc), hidden mp peak. Kept: call and response 29–36, layering 197–200, c078/c178 slurs and swells, heterophony 253–268, closing page.

## Cycle 277 (lens 7 texture, Adler ch. 8 Variety of orchestral treatments (adler1 PDF 251-281) (third pass)) v277 → v278
Accepted: violas G4–D4–G4 at 45–46 (fifth of the I6, no unison with Cl 2). Kept with reasons: 121–122/277–278 (root and fifth present), ff unison doublings at 118/318 (Tbn 1 B3 would make fifths into 119), fugato and countersubject, coda ostinato 325–328.

## Cycle 276 (lens 6 playability, Adler ch. 2 Bowed String Instruments: divisi, bowing, harmonics (adler1 PDF 24-70) (fourth pass)) v276 → v277
c276 lens 6 Adler ch. 2: no change. Keep the down-bow series at 333–339 (c096), the up-bow accents in crescendos at 49/125/103/303, the arco return at 273, the one-beat pizz. changes at 205/225, the viola triple stop at 339, the violas' double-stop spiccato at 105–120/305–320, and Vln I's last G♯ "change bow freely".

## Cycle 275 (lens 5 engraving, Gould ch. 1: stave, clefs, noteheads, stems, tails (gould-behind-bars PDF 17-30) (fourth pass)) v275 → v276
c275 lens 5 Gould ch. 1: no change. Keep stems.ily and the beam fix, the clef plan, the low-brass tenuto placement (c125), Cl 2's ledger notes at 87–88/285–287, the harp LH ledger notes, and the closing page.

## Cycle 274 (lens 4 orchestration, Rimsky-Korsakov ch. I Comparison of resonance and combination of tone qualities, and ch. III Harmony: number of parts, distribution, strings, woodwind (rimsky-principles PDF 51-53, 81-99) (fourth pass)) v274 → v275
c274 lens 4 Rimsky ch. I/III: Cl 2 on the tenor line 281–288. Keep the harp LH under arco basses at 209–224, Bsn 1 on the bass at 129–131, the clarinet pair's fourths and fifths at 45–56/121–128, the open B–F♯ at 123/279, and the doubled F♯5 at 101–104.

## Cycle 273 (lens 3 form, Aldwell & Schachter Unit 14 V as a Key Area (aldwell-schachter PDF 211-229) (fourth pass)) v273 → v274
c273 lens 3 A&S Unit 14: no change. Keep the trio's second A to B (169–184) with its pivot on C♯ minor at 177, the middle section on vi (185–208), the 4–♯4–5 approaches at 213–216 and 243–245, the coda's A-major statement and the E chord at 348, and the current proportions.

## Cycle 272 (lens 2 harmony, Aldwell & Schachter Unit 5 Procedures of Four-Part Writing (aldwell-schachter PDF 74-91) (fourth pass)) v272 → v273
c272 lens 2 A&S Unit 5: Vla/Hn 2 A at 47; Hn 1 rest beat 3 of 110/310 (c202's fifths fix holds); Hn 2 A3 at 52; Bsn 1 E3 at 197; Vln II F♯4 at 259/264. Keep 255–256, 54, 40/44, 102–103, 105/305, 326–329 and 200, the hemiola cadences, the V♭9 at 126/282, the 197–200 layering, the plagal close 357–360 and the closing page.

## Cycle 271 (lens 1 melody, Aldwell & Schachter Unit 20 Melodic Figuration (aldwell-schachter PDF 327-345) (fourth pass)) v271 → v272
c271 lens 1 A&S Unit 20: Cl 1·2 G4/E4 at 253. Keep theme A, the trio tune's four dissonances and the coda's 354, the trio call's five-note turn, the second idea's chord-tone frame and hemiola, the harp melody 73–80, the Vc/Bsn 2 double neighbour at 221–223, the motto tail order, and the closing page.

## Cycle 270 (lens 10 cyclic, Aldwell & Schachter Unit 23 Mixture as a long-range device (aldwell-schachter PDF 386-397) (third pass)) v270 → v271
c270 lens 10 cyclic: no change. Keep Cl 2's G4 at bar 7 (movement II A♭4 → Hn 1 G♯4 → G4, mirrored by the finale's A♭4 → G4 at its bar 2; A&S PDF 388, 395), Hn 3's C4–C♯4–B3 at 87–89, and no ♭VI (C major belongs to the finale).

## Cycle 269 (lens 9 holistic, Adler part 2 full-score examples in ch. 11 and 15 (adler2 PDF 18-54, 143-186) (third pass)) v269 → v270
c269 lens 9 holistic (Mahler 5/iii): timpani mf at 332. Keep the timpani roll f at 129–130/285–286, the strings-only fugato 57–68, and the reprise tutti 305–320 as scored.

## Cycle 268 (lens 8 expression, MOLA guidelines on dynamics, articulation and bowing marks in parts (mola PDF 1-16) (third pass)) v268 → v269
c268 lens 8 MOLA: Bsn/Cbsn accents at 72/300 (horns stay unaccented, soft-brass rule); Cl 1 and Vln I hairpins 247–252; Timp p at 28/268; muta whiteout at 376. Keep the strings' entries at 31/35 without a dynamic, no espress. at 121/277, and the bowing signs.

## Cycle 267 (lens 7 texture, Sebesky ch. 3 Voicing the strings; combining strings with winds (sebesky PDF 133-173) (third pass)) v267 → v268
c267 lens 7 Sebesky ch. 3: Vc rests 341–347. Keep the cellos doubling the basses at 193–204 (the fifth gives octaves with Cl 1), the inner G4/F♯4 at 121–124, the tonic pedal 225–240, the cellos on the bass at 333–339, the flutes at 37–40, the fugato 57–68, the call and response at 29–36/185–192, and the closing page.

## Cycle 266 (lens 6 playability, Sebesky ch. 2 Wind instruments (sebesky PDF 21-110) (third pass)) v266 → v267
c266 lens 6 Sebesky ch. 2: Ob 2 rests at 44/276. Keep the f/fff oboe unisons at 41–43/273–275/334–338, the horns' motive x at 71/299, Hn 1's high pp at 72–74, Hn 4's A2 at 305–320, B.tbn and tuba on the root at 105–120/333–339, and Bsn 1 at 209–216.

## Cycle 265 (lens 5 engraving, Adler ch. 2 notation of bowings, divisi and harmonics (adler1 PDF 30-55) as engraving rules (third pass)) v265 → v266
c265 lens 5 Adler ch. 2: Cb 207 hairpin removed (p); Vla "unis." at 13. Keep Vln I's one long ff bow at 218–220, viola unis. at 352–353, the up-bow at 103 in the hemiola, the down-bows at 72 and 277, and the two pizz. notes under a hairpin at Vla 271.

## Cycle 264 (lens 4 orchestration, Casanelles ch. 6 spectral orchestration and acoustic mixing in Mahler's First Symphony (hyper-orchestra PDF 257-290) (third pass)) v264 → v265
c264 lens 4 Casanelles ch. 6: no change. Keep the coda's A6 statement of T at 349–356, the harp chords at 153–168/185–188/341–344, the tutti layout 105–120, the pp trumpet entry at 101–104, and the closing page 363–375.

## Cycle 263 (lens 3 form, Aldwell & Schachter Unit 15 III and VII (aldwell-schachter PDF 230-247) (third pass)) v263 → v264
c263 lens 3 A&S Unit 15: Bsn 1 F♯4 at 215. Keep 214 (the same move makes fifths with Cl 1 and Vln II), Hn 2's E4→D♯4 (c093/c157), the Hn 1·2 sixths (c094), the reprise without G major, the 288→289 join, Vln II's E5 at 330, the diminished triads at 27 and 214, and the proportions.

## Cycle 262 (lens 2 harmony, Aldwell & Schachter Unit 27 Seventh chords with added dissonance (aldwell-schachter PDF 463-481) (third pass)) v262 → v263
c262 lens 2 A&S Unit 27: Hn 1·2 move to G on beat 3 of 47. Keep the trio's horn drone under V7 at 155/160, the 9–8 at 200, the flat 9ths at 111/311, 126/282 and 337, the bassoon's E3 at 347, the plain V7 at 101–104, and the horns' held notes elsewhere in 45–56.

## Cycle 261 (lens 1 melody, Aldwell & Schachter Unit 3 Rhythm and Meter (aldwell-schachter PDF 47-57) (third pass)) v261 → v262
c261 lens 1 A&S Unit 3: no change. Keep theme A's metric placement, the second idea's 3/2 and its cadential hemiola (c002, c085), the four-bar phrasing of the themes with the three-bar groups at 89–100, the trio tune's dissonances at 156/160/162/165–166, and Ob 1's sixth at 129/285 (c131).

## Cycle 260 (lens 10 cyclic, Sebesky ch. 9 General Advice and ch. 1 (sebesky PDF 240-242, 11-20) (third pass)) v260 → v261
c260 lens 10 cyclic: no score change; theme record +10 exact-pitch lines (kit/themecheck_abs.py). Told the finale its bar 1 needs "arco" for cellos and basses after the scherzo's pizz. ending.

## Cycle 259 (lens 9 holistic, Adler part 1 full-score examples in ch. 5 and 8 (adler1 PDF 137-165, 235-281) (third pass)) v259 → v260
c259 lens 9 holistic (Schumann 4/iii, Adler ch. 5/8 examples): no change. Keep the light opening and the four-stage build of theme A, the cello F♯2 at 330, no cello doubling of theme A's dips at 15–16/255–256, and the plain first statement of T (c089, c224).

## Cycle 258 (lens 8 expression, Sebesky ch. 1 focus and variety, ch. 6 melodic considerations (sebesky PDF 11-20, 204-218) (third pass)) v258 → v259
c258 lens 8 Sebesky ch. 1/6: strings out at 240 under Hn 1's G♯; espress./dolce on doubling parts at 45/209/349. A printed hairpin at 238–240 makes 15 pages (six variants tried). Keep Hn 1's G♯ at 237–240 and its turn at 241, the timpani roll 237–240, the coda arc 325–339 with its single fff, Fl 1/Ob 1 unmarked at 45, and the closing page.

## Cycle 257 (lens 7 texture, Sebesky ch. 1 Basics: balance, economy, focus, variety (sebesky PDF 11-20) (third pass)) v257 → v258
c257 lens 7 Sebesky ch. 1: Vln II off-beats at 36/39; bass G♯ (I6) at 210 with cellos and Bsn 2 swapping, Hn 2 holds E4. Keep the plain first trio statement 153–168 and the coloured second 169–184, the strings-only fugato 57–68, the call and response 29–36, the codetta hand-overs 225–236, and the closing page.

## Cycle 256 (lens 6 playability, Rimsky-Korsakov ch. I General review of orchestral groups (rimsky-principles PDF 24-50) (third pass)) v256 → v257
c256 lens 6 Rimsky ch. I: "non arpegg." at harp 81/185/225 (below the stave; above made 15 pages). Keep Hn 1's C♯5 (c156/c166), Cl 2's octave leap at 332–333, the soft low clarinet at 83/87–88, pizz. basses alone at 170–184 and 252–268, and the arco→pizz. changes at 205/225 (c096).

## Cycle 255 (lens 5 engraving, MOLA second pass, applied to the instrumental parts (parts.ily) rather than the score (third pass)) v255 → v256
c255 lens 5 MOLA parts: cues C.a. 101, strings 169, timpani 89; muta texts below the stave in parts. Keep the part system spacing (c165), the trumpet parts without key signatures, and no extra cues at rehearsal-letter entries (153, 357, 363).

## Cycle 254 (lens 4 orchestration, Adler ch. 5 Scoring for Strings (adler1 PDF 125-167) (third pass)) v254 → v255
c254 lens 4 strings (Adler ch. 5): no change. Keep the trio's string layering (153, 169–184, 209–224, 341–356), the strings-only fugatos 57–68 and 289–296, the viola off-beats at 106/113–116/306/313–316 (c207), the pizz. downbeats 225–240, the tutti 105–120 and 305–320, the peak at 336–339, and the closing page.

## Cycle 253 (lens 3 form, Aldwell & Schachter Units 6-8 I, V, V7 and their inversions: phrase structure (aldwell-schachter PDF 92-133) (third pass)) v253 → v254
c253 lens 3 A&S Units 6–8: no change. Keep the large form, the V pedal 89–104 and the F episode, the link 141–152 on a plain V, the retransition, theme A's period structure, the triad half cadences, the hemiola cadences, and the two-stage coda with the plagal close 357–360 and the G♯ ending.

## Cycle 252 (lens 2 harmony, Aldwell & Schachter Units 30-31 Other chromatic chords; Chromatic voice-leading techniques (aldwell-schachter PDF 530-583) (third pass)) v252 → v253
c252 lens 2 A&S Units 30–31: no change. Keep the B♮ against Cl 2's B♯ at 199–200, the viola leap at 296–297 (Bsn 1 resolves), the common-tone °7 at 358, and the ♭II6/4 at 331 (c081, c242).

## Cycle 251 (lens 1 melody, Adler ch. 11 Scoring for Brass: melodic presentation (adler2 PDF 19-36) (third pass)) v251 → v252
c251 lens 1 brass melody (Adler ch. 11): no change. Keep theme A, the trio tune with the coda hand-over 341–356, the stretto colour groups, the horn and cello tenor lines, the horns' beat-3 crotchets at 112/120/312/320, no horn at 209–224 and 349–356, and the closing page 357–376.

## Cycle 250 (lens 10 cyclic, Rimsky-Korsakov author's prefaces and ch. IV transfer of phrases (rimsky-principles PDF 13-23, 125-128) (third pass)) v250 → v251
c250 lens 10 cyclic: short names in F/in C, page 1 numbered, mm-rest bar ranges in parts, Cl muta in B♭ at 376. The finale's IV 9 takes the closing figure's rhythm and instrument, not its pitches or dynamics (the finale plays it mf <) (scherzo B–B–B–E, finale G–G–G–G). Keep the transfers at 369/375 (c150).

## Cycle 249 (lens 9 holistic, Rimsky-Korsakov examples No. 261-312 (rimsky-principles PDF 441-504) (third pass)) v249 → v250
c249 lens 9 holistic (Tchaikovsky 6/iii, Rimsky Ex. 275–312): no change. Keep the brass and timpani economy, the soft wind solos over harp and pizzicato, the four colourings of T, the 197–200 layering, the hemiola cadences, and the closing page 357–376.

## Cycle 248 (lens 8 expression, Aldwell & Schachter Unit 3 Rhythm and Meter: accent, hypermeter (aldwell-schachter PDF 47-57) (third pass)) v248 → v249
c248 lens 8 A&S Unit 3: timpani roll 205–208 sustained, crescendo into 209. Keep the accents on the second idea's first minim, the cadential hemiolas, the tied A in the trio tune, timpani at 100–101/240/252, Hn 3·4 at 205–208, and the tempo-word placement.

## Cycle 247 (lens 7 texture, Rimsky-Korsakov ch. III overlaying, crossing and enclosure (rimsky-principles PDF 106-114) and the examples cited (third pass)) v247 → v248
c247 lens 7 Rimsky ch. III: Bsn 1 F♯4 at 216 (was D♯4). Keep Hn 2's E4→D♯4 at 214–216 (c093/c157), the Hn 1·2 sixths (c094), the doubled third at 80 (c132), horns inside the reeds at 75–76/82–83 (c104/c147), and the closing page.

## Cycle 246 (lens 6 playability, Adler App. A ranges, professional and amateur limits (adler2 PDF 302-312) (third pass)) v246 → v247
c246 lens 6 ranges (Adler App. A): Bsn 1·2 breath marks at the end of 104/304 with Hn 3·4. Keep Hn 1's last G♯ at 368–376 (Hn 3 covers the breath), the arco/pizz. changes at 205/225 (c096), and "senza sord." for Hn 3·4 at 73.

## Cycle 245 (lens 5 engraving, Gould introduction and contents (gould-behind-bars PDF 7-13), then a second pass over PDF 17-68 for any rule not yet checked (third pass)) v245 → v246
c245 lens 5 engraving (Gould): Hn 1 solo labels/hidden Hn 2 rests 357–366, Cb tutti/pizz. two lines at 3, Bsn scherz. 269, harp rest spacing 149/151. Keep the clef plan (Hn 3·4 bass clef 301–330, harp bass clef 341–344), the double barlines at the section joins, beams.ily and stems.ily, and the closing page's spacing.

## Cycle 244 (lens 4 orchestration, Adler ch. 11 Scoring for Brass: homophonic unit and climactic uses (adler2 PDF 14-18, 37-54) (third pass)) v244 → v245
c244 lens 4 brass (Adler ch.11): no change. Keep the trombones' first entry at 101 and their rest from 121 to 332, the single-horn ff at 101–104/301–304/333–338, the paired tenor horns at 105–120, and the timpani alone at 89–100.

## Cycle 243 (lens 3 form, Adler ch. 15 Additional thoughts and special effects (adler2 PDF 187-196) with ch. 17 The Orchestra as Accompanist (adler2 PDF 256-290) for pacing of background and foreground (third pass)) v243 → v244
- No change from the critic (pacing confirmed against Adler ch. 15, 17). Composer: Cb "tutti pizz." at 3 (movement II ends 4 soli).

## Cycle 242 (lens 2 harmony, Aldwell & Schachter Units 28-29 Neapolitan; Augmented Sixth Chords (aldwell-schachter PDF 482-529) (third pass)) v242 → v243
- No change (harmony confirmed against A&S Units 28–29).

## Cycle 241 (lens 1 melody, Aldwell & Schachter Unit 21 Rhythmic Figuration: suspensions, anticipations, pedal (aldwell-schachter PDF 346-371) (third pass)) v241 → v242
- No change (melody confirmed against A&S Unit 21).

## Cycle 240 (lens 10 cyclic, Adler ch. 1 The Orchestra, Yesterday and Today, and ch. 15 additional thoughts (adler1 PDF 19-23, adler2 PDF 187-196) (third pass)) v240 → v241
- No score change; joins with I v261, II v252, finale v234 checked; records corrected (closing timpani dynamics; 9–12 timpani motive x framing the finale's bar 9).
- Do-not-touch: timpani motive x at 9–12 (finale v231 bar 9).

## Cycle 239 (lens 9 holistic, Rimsky-Korsakov examples No. 201-260 (rimsky-principles PDF 376-440) (third pass)) v239 → v240
- No change (Dvořák 6/iii comparison; v229→v239 nothing worse).

## Cycle 238 (lens 8 expression, Casanelles ch. 4 dynamics layering and expression in performance (hyper-orchestra PDF 145-161) and ch. 6 volume and dynamics (PDF 290-291) (third pass)) v238 → v239
- Accepted: c178 swell peaks one level up in the MIDI; timpani and bass crescendos at 98–100 and 249–252 (Casanelles PDF 148–150, 290).
- Do-not-touch (critic): trio's graded layering; soft-brass builds 101–104/301–304; leggiero theme over pizz.

## Cycle 237 (lens 7 texture, Adler ch. 16 The Orchestral Transcription (adler2 PDF 197-255) (third pass)) v237 → v238
- Accepted: Vln II contrary arpeggios at 99–100 (Adler PDF 217, 229).

## Cycle 236 (lens 6 playability, Adler ch. 12 The Percussion Ensemble: timpani tuning and technique, cymbals, bass drum (adler2 PDF 55-91), and ch. 14 Scoring for Percussion (adler2 PDF 106-145) (third pass)) v236 → v237
- Accepted: "near the rim" at 371–375 (Adler PDF 80).

## Cycle 235 (lens 5 engraving, Adler ch. 18 Preparation of Score and Parts, and App. A (adler2 PDF 291-312) (third pass)) v235 → v236
- Accepted: \sysLabel player labels at system breaks; Bsn 1 pp above at 7; last timpani muta above the staff (Adler PDF 294–295).

## Cycle 234 (lens 4 orchestration, Adler ch. 8 Woodwinds in the symphony orchestra and woodwind-string combinations (adler1 PDF 233-281) (third pass)) v234 → v235
- Accepted: Bsn 1 B3 at 141–144 (spacing, Adler PDF 257).

## Cycle 233 (lens 3 form, Aldwell & Schachter Unit 18 6/3-chord techniques (aldwell-schachter PDF 289-303) (third pass)) v233 → v234
- No change (form confirmed against A&S Unit 18).

## Cycle 232 (lens 2 harmony, Aldwell & Schachter Units 24-25 Remaining uses of seventh chords; Applied V and VII (aldwell-schachter PDF 398-441) (third pass)) v232 → v233
- No change (harmony confirmed against A&S Units 24–25).

## Cycle 231 (lens 1 melody, Sebesky ch. 6 Melodic Considerations and ch. 7 The Importance of the Lyric (sebesky PDF 204-230) (third pass)) v231 → v232
- No change (melody confirmed against Sebesky ch. 6–7).

## Cycle 230 (lens 10 cyclic, Casanelles ch. 5 Hyperorchestral aesthetic frameworks: themes and their transformation (hyper-orchestra PDF 199-254) (third pass)) v230 → v231
- Accepted: MIDI fades at 362–364 and 372–375 via CC11, last bar \mt 50 (print unchanged). Joins with I v251, II v240, finale v226 checked.

## Cycle 229 (lens 9 holistic, Rimsky-Korsakov examples No. 126-200 (rimsky-principles PDF 305-375) (third pass)) v229 → v230
- No change (Beethoven 5/iii comparison; v219→v229 nothing worse).
- Do-not-touch (critic): soft horn–bassoon voicing at 201–204.

## Cycle 228 (lens 8 expression, Adler ch. 11 climactic uses of brass (adler2 PDF 37-40) and ch. 15 special effects (adler2 PDF 187-196) (third pass)) v228 → v229
- No change (expression confirmed against Adler PDF 37–40, 187–196).

## Cycle 227 (lens 7 texture, Adler ch. 17 The Orchestra as Accompanist (adler2 PDF 256-290) (third pass)) v227 → v228
- Accepted: Vln II off-beats out of the tune's unison at 15–16/31–32; Hn 1 rest at 242 (Adler PDF 259–274).

## Cycle 226 (lens 6 playability, Adler ch. 9-10 Brass: horn, trumpet, trombone, tuba, endurance and ranges (adler1 PDF 282-329, adler2 PDF 1-13) (third pass)) v226 → v227
- Accepted: Hn 4 breath at 309/310; coda T head 341–344 to Hn 3, Hn 1 rests 340–356 (Adler PDF 292, 303–304). Record line trioT moved to HnThree 341.

## Cycle 225 (lens 5 engraving, MOLA Guidelines for Music Preparation, whole document (mola PDF 1-16) (third pass)) v225 → v226
- Accepted: duplicate "1." at 193 removed; percussion tacet in the heading and a tacet part; espress. clear of W at 357 (MOLA PDF 5–8).

## Cycle 224 (lens 4 orchestration, Adler ch. 15 Scoring for Orchestra: homophonic and polyphonic texture (adler2 PDF 159-186) (third pass)) v224 → v225
- Accepted: cor anglais B4 (was B3) at 133–136/321–323 (Adler PDF 198, 205).
- Do-not-touch (critic): tutti layouts 105–120/305–320, 333–339; four colourings of the trio tune (153, 169, 209, 341–356).

## Cycle 223 (lens 3 form, Aldwell & Schachter Units 16 and 19 5/3- and 6/4-chord techniques: prolongation (aldwell-schachter PDF 249-262, 304-325) (third pass)) v223 → v224
- Accepted: Hn 2 A3 at 54 (doubled 4th of the cadential 6/4, A&S PDF 316).

## Cycle 222 (lens 2 harmony, Aldwell & Schachter Units 22-23 Leading-tone seventh chords; Mixture (aldwell-schachter PDF 373-397) (third pass)) v222 → v223
- No change (harmony confirmed against A&S Units 22–23).

## Cycle 221 (lens 1 melody, Adler ch. 7 Individual Woodwinds: melodic writing, registers (adler1 PDF 184-232) (third pass)) v221 → v222
- Accepted: cor anglais B4 (was B3) pp at 269–271 (Adler PDF 198, 205, 226).

## Cycle 220 (lens 10 cyclic, Aldwell & Schachter Unit 26 modulation and form (aldwell-schachter PDF 442-461) (third pass)) v220 → v221
- No score change; joins with I v231, II v228, finale v217 checked; scherzo.md updated (theme A bar 2 link, harp B4 → C5).
- Do-not-touch: theme A statements' register (I 79 and IV 273–275 quote bar 2 at pitch); harp harmonics E4–G♯4–B4 at 375.

## Cycle 219 (lens 9 holistic, Rimsky-Korsakov examples No. 61-125 (rimsky-principles PDF 241-305) (third pass)) v219 → v220
- No change (Mendelssohn 3/ii comparison; v209→v219 nothing worse).

## Cycle 218 (lens 8 expression, Adler ch. 2 bowing and its expressive effect (adler1 PDF 36-55) (third pass)) v218 → v219
- Accepted: hemiola cadences down-bow again via separate up-bow quaver at 52/128; cello countermelody bowing at 176/216/222; viola louré dashes 45–46, 127–128, 283–284 (Adler PDF 37–43, 54).
- Do-not-touch (critic): c085 hemiola bowing; c118 up-bow swells; bowings at 300 and 333–339; up-bows before pizz. at 204/223; trio viola louré.

## Cycle 217 (lens 7 texture, Adler ch. 15 polyphonic texture (adler2 PDF 172-186) (third pass)) v217 → v218
- No change (texture confirmed against Adler PDF 172–186).

## Cycle 216 (lens 6 playability, Adler ch. 6-7 Woodwind choir and individual woodwinds: breathing, registers, technique (adler1 PDF 168-232) (third pass)) v216 → v217
- No change (woodwinds confirmed against Adler ch. 6–7).
- Do-not-touch (critic): breathing points (Cl 1 160/216, winds' rest 300, Bsn 1 116/316, Fl 2 for Fl 1 205–208); climb to B6 335–336; A clarinets.

## Cycle 215 (lens 5 engraving, Gould ch. 1-2: rhythmic spacing, spacing of symbols, chords, unisons, double-stemmed writing (gould-behind-bars PDF 53-68) (third pass)) v215 → v216
- Accepted: hairpin minimum 3.9, barline spacing (Gould PDF 54, 57); Cl 2 rest at 85 (PDF 55).
- Do-not-touch (critic): shared unison noteheads, Ob minim/crotchet offset at 338, dot placement, chord stems, last page 357–376.

## Cycle 214 (lens 4 orchestration, Adler ch. 15 Scoring for Orchestra: unison-octave tutti, foreground and background (adler2 PDF 146-158) (third pass)) v214 → v215
- Accepted: Ob 1 E5 (was E4) at 132/288 (Adler PDF 198).
- Do-not-touch (critic): tutti layout 105–120/305–320; coda build 336–339; trio foreground/background 153–184; last page 357–376.

## Cycle 213 (lens 3 form, Rimsky-Korsakov ch. IV Composition of the orchestra: tutti, range limits, transfer of phrases, sf-p, crescendo and diminuendo (rimsky-principles PDF 115-136) (third pass)) v213 → v214
- Accepted: contrabassoon enters p at 330 on the bass clarinet's D2 (Rimsky PDF 125–127).

## Cycle 212 (lens 2 harmony, Aldwell & Schachter Unit 17 Diatonic Sequences (aldwell-schachter PDF 263-288) (third pass)) v212 → v213
- Accepted: violas A♮ in the sequence at 195 (A&S PDF 265, 394).

## Cycle 211 (lens 1 melody, Adler ch. 3 Individual Bowed Strings: melodic writing for violin, viola, cello, bass (adler1 PDF 71-109) (third pass)) v211 → v212
- No change (melody confirmed against Adler ch. 3).

## Cycle 210 (lens 10 cyclic, Aldwell & Schachter Unit 32 chromatic tonal areas and large-scale motion (aldwell-schachter PDF 584-606) (third pass)) v210 → v211
- No score change; joins with II v215 and finale v209 checked; scherzo.md updated.

## Cycle 209 (lens 9 holistic, Rimsky-Korsakov examples No. 1-60 (rimsky-principles PDF 173-240) (third pass)) v209 → v210
- No change (Bruckner 9/ii comparison; v199→v209 nothing worse).

## Cycle 208 (lens 8 expression, Rimsky-Korsakov ch. IV sf-p chords, crescendo and diminuendo (rimsky-principles PDF 129-136) (third pass)) v208 → v209
- Accepted: Hn 1·2 out at 224 (Rimsky PDF 130); Hn 3 pp at 277 (PDF 136); Cl 2 fade at 227–228.

## Cycle 207 (lens 7 texture, Adler ch. 5 foreground, middleground, background; strings as accompaniment (adler1 PDF 132-167) (third pass)) v207 → v208
- Accepted: violas F♯3 at 40 (string order, Adler PDF 135, 151).
- Kept: viola off-beats 113–118/309–318; strings-only reprise fugato.

## Cycle 206 (lens 6 playability, Adler ch. 4 Plucked Strings: harp and pedalling (adler1 PDF 110-124) (third pass)) v206 → v207
- Accepted: harp LH rest at 189 (B pedal change after B♯3 at 188, Adler PDF 111–113); ♮ printed in the pedal settings at 1, 73, 141, 333 (PDF 112).

## Cycle 205 (lens 5 engraving, Gould ch. 1: ledger lines, octave signs, rests (gould-behind-bars PDF 41-52) (third pass)) v205 → v206
- Accepted: Ob 2 rests level at 105/305 (Gould PDF 49–51).

## Cycle 204 (lens 4 orchestration, Rimsky-Korsakov appendix of single tutti chords (rimsky-principles PDF 505-510) and the tutti examples cited in ch. IV (third pass)) v204 → v205
- Accepted: \partCombineChords at 339 so the score keeps Tbn 2's B2 (Rimsky PDF 101, 505–507).
- Note: \partCombine can drop a note after shared multi-bar rests; critics should compare shared staves with the parts.

## Cycle 203 (lens 3 form, Aldwell & Schachter Unit 32 Chromaticism in Larger Contexts (aldwell-schachter PDF 584-606) (third pass)) v203 → v204
- No change (form confirmed against A&S PDF 584–606). Kept: cut at 339–341; joins 72–73, 141–153; reprise without the F episode.

## Cycle 202 (lens 2 harmony, Aldwell & Schachter Units 11-13 VI and IV6; supertonic and subdominant sevenths; other uses of IV and VI (aldwell-schachter PDF 163-210) (third pass)) v202 → v203
- Accepted: Hn 1 A4 (was C5) on beat 3 of 110/310, removing fifths with the tune (A&S PDF 190).
- Do-not-touch (critic): plagal close 357–360; tenor 9–8 at 110–111/310–311; held E ii7–ii6/5 into the 6/4 at 219–221/351–353; voice exchange 313–315; F-episode harmony 81–84; hemiola cadences.

## Cycle 201 (lens 1 melody, Rimsky-Korsakov ch. II Melody: woodwind, brass, combined groups (rimsky-principles PDF 64-80) and the examples it cites (third pass)) v201 → v202
- No change (melody confirmed against Rimsky-Korsakov PDF 64–80). Title "draft v202" (third series started from release copy v201).

## Cycle 200 (lens 10 cyclic, release check, second pass) v200 → v201 (release copy)
- Accepted: title without "draft" (v201, 17 October 2026); parts title matches the score; coda.ily comment on current brass dynamics.
- Checked: cyclic rules, do-not-touch list, joins with II v201 and finale v201, finale quotations; all hold.

## Cycle 199 (lens 9 holistic, Casanelles ch. 6, second pass) v199 → v200
- Accepted: horns stay ff at 335–338 (no brass fff).
- Kept: 72/300, 29–34, 197–198, 111/311, 341–344; four-bar phrasing.

## Cycle 198 (lens 8 expression, A&S Unit 21, second pass) v198 → v199
- Accepted: cello swell on the 9–8 at 110–111/310–311 (hidden end dynamics).
- Rejected: Hn 1 diminuendo at 216 (adds two pages).
- Kept: 195–196, 126/282, 55/131/287, 337–338, 241–244.

## Cycle 197 (lens 7 texture, Adler part 2 ch. 11, second pass) v197 → v198 (no change)
- Kept: 89–100, 101/103 and 333/335 trumpets, 105–120 trombone, 71/299 horns, 337–338.

## Cycle 196 (lens 6 playability, Adler ch. 3, second pass) v196 → v197 (no change)
- Kept: 282 clef, viola alto-clef high notes, 46/50, 105–120/305–320, 60–61, 218–220.

## Cycle 195 (lens 5 engraving, Gould ch. 1 beams, second pass) v195 → v196
- Accepted: beam callback in beams.ily, included by score.ly and the parts (parts now get the c015/c105 beam fix).
- Kept: 2.92-space stems at 23/76/115/263/315/354, slope at 38/74.

## Cycle 194 (lens 4 orchestration, Rimsky-Korsakov ch. III brass, second pass) v194 → v195
- Accepted: Tbn 2 B2 at 333–334/339 (E3 at 335); Tpt 1·2 stay f at 335–338 (no fff).
- Kept: Tpt seventh at 337–338 (c082), Tbn 2 E3 at 105–120, Tbn 1 seventh at 103–104 (c104), clarinets inside horns 45–56/121–128.

## Cycle 193 (lens 3 form, A&S Unit 26, second pass) v193 → v194 (comments only)
- Accepted: header comments in sC, tB, retr corrected.
- Kept: G minor at 289, trio C♯ minor, 349–354, fades 133–152/225–252, length and coda.

## Cycle 192 (lens 2 harmony, A&S Units 9–10, second pass) v192 → v193
- Accepted: Vc fis2. at 181 (real cadential 6/4); harp RH <fis' ais' cis''> / LH fis, at 192.
- Kept: 4, 221/353–355, 76–77/83–84, 128–129, 26–27, 151, 335–336.

## Cycle 191 (lens 1 melody, Rimsky-Korsakov ch. II strings, second pass) v191 → v192 (no change)
- Kept: 349–356, 15–16/31–32, 113–116, coda hand-overs of T, 209.

## Cycle 190 (lens 10 cyclic, Adler part 2 ch. 17, second pass) v190 → v191
- Accepted: Bsn 1·2 hold E4/B3 at 145–148 instead of the clarinets (Cl 1 rests 137–152 before the trio tune).
- Checked: joins with II v201 and finale v201 unchanged; finale quotations unchanged since scherzo v171.

## Cycle 189 (lens 9 holistic, A&S Units 20–32 literature examples, second pass) v189 → v190
- Accepted: Ob 2 e''4 at 105/305; tenor countermelody g2( e'4~ at 117/317; Hn 1 c''4-- r4 a'4-. at 113/313.
- Kept: form and scoring; no structural change.

## Cycle 188 (lens 8 expression, Adler ch. 10, second pass) v188 → v189
- Accepted: slur + tenuto on held brass at 101–104/301–304, horns 331–335 and 336–338, low brass 333–335; Tbn 1·2 tenuto at 120.
- Kept: horn ff→pp at 72, staccato horns in motive x 71/299, no mutes, last horn G♯, coda horn trio tune without hairpin.

## Cycle 187 (lens 7 texture, Rimsky-Korsakov ch. II, second pass) v187 → v188
- Accepted: cor anglais doubles Vln II's hemiola at 101–104/301–304 (ff moved to 104/304).
- Kept: 105–112, 341–344, 349–356, 253–268.

## Cycle 186 (lens 6 playability, Adler ch. 2, second pass) v186 → v187
- Accepted: "non div." on the 339 chords (Vln II, Vla, Vc).
- Kept: viola triple stop 339, 223–224 bowing, spiccato double stops 105–120/305–320, 369–376 bowing, 375.

## Cycle 185 (lens 5 engraving, Gould ch. 1, second pass) v185 → v186 (no change)
- Kept: stems.ily and the beam callback (beamed stems are 2.56 spaces), clefs at 286, 331, 341–345, harp ledger lines 153–168.

## Cycle 184 (lens 4 orchestration, Rimsky-Korsakov ch. I/III, second pass) v184 → v185
- Accepted: Hn 2 A3 at 49–52 (supersedes c094/c119 E3); oboes F♯5/D♯5 at 101–104/301–304; Cbsn B1 at 221–222; Cl 1 A4 / Cl 2 F♯4 at 251–252.
- Kept: clarinet tritones at 336–338 and 101/103, bassoon spacing 37–39, doublings at 87/259, 105–118 middle.

## Cycle 183 (lens 3 form, A&S Unit 14, second pass) v183 → v184 (no change)
- Kept: no repeats (a trio repeat adds ~32 s), short B area in the trio, F episode without V–I (C-major ban), E 105–179, coda 42 s vs reprise 49 s, C♯ at 49–50.

## Cycle 182 (lens 2 harmony, A&S Unit 5, second pass) v182 → v183
- Accepted: violas 201 e'4 a'2; Hn 1 48 g'2.; Cl 1 125–126/281–282 c''2 a'4~ a'2.; Vc and Bsn 2 216 fis2 b,4 (no doubled D♯); violas 229–232 G♯3 (third in the codetta chord).
- Do-not-touch: 357–360, hemiola cadences, V♭9 at 126, 361–376.

## Cycle 181 (lens 1 melody, A&S Unit 20, second pass) v181 → v182
- Accepted: Fl 1 at 263 steps down to E6 before C6 instead of leaping a diminished fifth from F♯6.
- Kept: G♯3 at 172/212, 326–328, Hn 1 115–116/315–316, second-idea lead-in, 73–88 lines; themes need no change.

## Cycle 180 (lens 10 cyclic, A&S Unit 28, second pass) v180 → v181
- Accepted: Cl 2 F3 at 86 doubling Hn 4, falling to D♯3 at 87 (the Neapolitan note descends; Hn 4's F→F♯ kept).
- Checked: links II v201 → bar 1 and scherzo end → finale v201 bar 1 match; finale record 36/36; no theme change.

## Cycle 179 (lens 9 holistic, Adler part 2 ch. 16, second pass) v179 → v180
- Accepted: Bsn 1 crescendo with the violas at 207; Bsn 2 and Cbsn B pedal pp< at 207–208; no hairpin on the single pizz. note at 271 (Vln II).
- Kept: form and proportions; no structural change.

## Cycle 178 (lens 8 expression, Adler ch. 7, second pass) v178 → v179
- Accepted: swell on the held peak note of T's second phrase at 158, 174, 214, 346, with hidden end dynamics; "dolce" on the codetta solos 225/229/233.

## Cycle 177 (lens 7 texture, Adler ch. 8, second pass) v177 → v178
- Accepted: violas double Vln I's top line A4–C5–B4 at 201–203 instead of a fourth E4/D♯4 (Adler PDF 255, 257, 270).
- Kept: wind imitation candidates (protected or colliding, 270–271), codetta 225–236, tutti viola voicing 108–118/308–318, 13–28 accompaniment.

## Cycle 176 (lens 6 playability, Sebesky ch. 2 Wind instruments, second pass) v176 → v177
- Accepted: Cl 1 \breathe at T's half cadence, bars 160 and 216 (Sebesky PDF 24, 70).
- Kept after testing: horn staccato in motive x 71/299 (Dvořák 9/iii does the same), Hn 1 G♯5 72–73, Ob 1 low E4 staccato 132/288, Hn 4 pedal 305–320, bass trombone + tuba root 333–344, cor anglais/Cl 2 inside the brass chord 336, woodwind seconds 101–106/336.

## Cycle 175 (lens 5 engraving, Adler ch. 2, second pass) v175 → v176
- Accepted: non div. at 72/300; pizz.→arco time at 271; unis./div. at 352–354; up-bow at 358 (Vc/Cb); no dots on viola pizz. 253–271 (supersedes c018).
- Do-not-touch: bow signs at 300 and 333–339, hemiola bowing, louré trio violas, 369.

## Cycle 174 (lens 4 orchestration, Casanelles ch. 6, second pass) v174 → v175
- Accepted: harp bass with the basses at 151, 214–215; fifth in the 223–224 chord; horns mf at 129/285; violas ppp at 349.
- Do-not-touch: 73–88, trio layering 153–240, coda build and fff/B6 at 336, 357–376.

## Cycle 173 (lens 3 form, Aldwell & Schachter Unit 15, second pass) v173 → v174
- No change; key plan matches Unit 15. Five points tested and kept.

## Cycle 172 (lens 2 harmony, Aldwell & Schachter Unit 27, second pass) v172 → v173
- Accepted: cluster at 55 removed (as c139); Hn 1 doubles Vln II at 196; violas F♯3 at 205–208.
- Kept: 9–8 at 200, ♭9 at 111/311 (c112), plain V7 at 101–104/301–304, codetta tonic (c082).

## Cycle 171 (lens 1 melody, Aldwell & Schachter Unit 3, second pass) v171 → v172
- No change. Kept: flute register at 113–116/313–316 (B6 limit; c025, c036, c078, c124).

## Cycle 170 (lens 10 cyclic, Aldwell & Schachter Unit 23, second pass) v170 → v171
- Accepted: harp B♯ spelling at 188 with pedal marks; records to finale v193.
- Kept: 352 C♯; 199–200 inner B→B♯ (c070).
- Do-not-touch: G♯ = A♭ frame, 237–245 G♯–G–F♯, codetta IV IV iv, ♮6–♭6–5 close 357–360, both muta labels.

## Cycle 169 (lens 9 holistic, Adler part 2, second pass; Schubert 9/iii) v169 → v170
- Accepted: low brass f (not ff) at 339 (Dan's rule; refines c128).
- Do-not-touch: recolouring of theme A and T, timpani motive x, held-back low brass, 357–376.

## Cycle 168 (lens 8 expression, MOLA, second pass) v168 → v169
- Accepted: printed peak dynamics at 217–221; hairpin targets at 207–208 and 329–331; Hn 4 mf at 128; Ob 1 accent at 334.
- Do-not-touch: 357–376, coda build to fff at 336, soft brass at 339, theme A down-bow retakes.

## Cycle 167 (lens 7 texture, Sebesky ch. 3, second pass) v167 → v168
- Accepted: wind doublings a level under the violins at 197–200, 125, 281.
- Kept: 193–204 bass doubling, 195–196, 105–120 horns (c097).

## Cycle 166 (lens 6 playability, Rimsky-Korsakov ch. I, second pass) v166 → v167
- Accepted: stepwise climb to B6 at 335 (Vln I, Fl 1); Hn 4 relieves Hn 3 at 121–128.
- Kept: Vln I G6/A6 at 46/50, low harp at 341–344, Cbsn octave at 213–222.

## Cycle 165 (lens 5 engraving, MOLA on the parts, second pass) v165 → v166
- Accepted: cues after long rests (C.a., Hn 2, Cbsn, harp); horns' repeated ff removed at 105/305; harp étouffez before the page turn.
- Kept: no composer line on parts, multi-rest numbering (c075), other part-layout points.

## Cycle 164 (lens 4 orchestration, Adler ch. 5, second pass) v164 → v165
- Accepted: basses rest at 121–124/277–280, return at 125/281 (completes c074).

## Cycle 163 (lens 3 form, Aldwell & Schachter Units 6–8, second pass) v163 → v164
- Accepted: Vln II A4→G4 at the cadences 19–20, 27–28 (supersedes c002's unison cadence).
- Do-not-touch: large form and proportions, hemiola cadences, V pedal 89–104, link and retransition, three trio statements, two-stage coda, G♯ frame.

## Cycle 162 (lens 2 harmony, Aldwell & Schachter Units 30–31, second pass) v162 → v163
- Accepted: vii°7 at 88 resolves to the cadential 6/4 at 89 in the winds (beats 1–2 only).

## Cycle 161 (lens 1 melody, Adler ch. 11, second pass) v161 → v162
- Accepted: Cl 1 takes theme A's head at 245 (colour change in the retransition canon); theme record moved to ClOne 245.
- Do-not-touch: theme A, trio tune, harp melody 73–80, tenor second idea 281–287, 357–376.

## Cycle 160 (lens 10 cyclic, Sebesky ch. 1 and 9, second pass) v160 → v161
- Accepted: Hn 4 part "senza sord." at 73; Bsn 2 B2 pedal under the horn call (Bsn 1 B3 from 7); records to finale v182.
- Kept: soft ending before the finale; motto-close rhyme with the finale (c060).

## Cycle 159 (lens 9 holistic, Adler part 1 full scores, second pass; Borodin 2/ii) v159 → v160
- Accepted: Vln II unison with Vln I at 305–308; stale comment fixed.
- Verdict: nothing worse since v149. Do-not-touch: hemiola cadences, timpani motive x, strings-only fugato/stretto, trio layering 153–224, 357–376.

## Cycle 158 (lens 8 expression, Sebesky ch. 1 and 6, second pass) v158 → v159
- Accepted: focus on the moving line at 205–208; cello countermelody shaped at 177–184; codetta swells 225–236; bass pp at 185.
- Kept: second idea dynamic plans, fugato p entries, 339 accents (non-brass), 375 levels.

## Cycle 157 (lens 7 texture, Sebesky ch. 1, second pass) v157 → v158
- Accepted: V6/5 of V reharmonisation at 213–216; cello countermelody mf at 209–224.
- Do-not-touch: trio first statement 153–168, fugato 57–68, 29–36, codetta 225–236, 357–376.

## Cycle 156 (lens 6 playability, Adler App. A, second pass) v156 → v157
- Accepted: reprise second-idea horn line to Hn 3 at 277–288 (Hn 1 endurance); Cl 2 breath at 204.
- Kept: Hn 1 C♯5 at 72/213–215/220/300; B6 at 336; Cl 2 C♯3 at 88 (A clarinet's lowest note).

## Cycle 155 (lens 5 engraving, Gould, second pass) v155 → v156
- Accepted: hairpin minimum length; duplicate solo label at 269; Hn 3·4 clef before the entry at 331; separator clear of bar numbers.

## Cycle 154 (lens 4 orchestration, Adler ch. 11, second pass) v154 → v155
- Accepted: brass chord balance at the coda peak (Hn 3 F♯4 at 336–338, Hn 1 B4 at 339).
- Kept: 101–104/301–304, 105–120, 305–320 (c115), 333–335, trio horns.

## Cycle 153 (lens 3 form, Adler ch. 15 and 17, second pass) v153 → v154
- Accepted: harp accompaniment thins through the codetta 225–236 (answers c133's one static place without a cut).
- Kept: proportions, both E-pedal closes, link, retransition, coda timing.

## Cycle 152 (lens 2 harmony, Aldwell & Schachter Units 28–29, second pass) v152 → v153
- Accepted: bassoons sustain and resolve the French sixth at 243–245; flat spelling of the falling tail at 38.

## Cycle 151 (lens 1 melody, Aldwell & Schachter Unit 21, second pass) v151 → v152
- Accepted: Hn 4 drone breaks at 166 so the trio cadence's 4–3 resolves.
- Kept: 155/160 drone, 200 (c117), 110–111/310–311 (c112). Rejected: 4–3 at 187–192.

## Cycle 150 (lens 10 cyclic, Rimsky-Korsakov prefaces and ch. IV, second pass) v150 → v151
- Accepted: Bsn 1 pp under the horn call at 4–8; records to v151 / finale v174.
- Kept: coda T hand-overs 344–349; additions during the dying ending 369–375 (G♯ hand-over, c050/c130).

## Cycle 149 (lens 9 holistic, Rimsky-Korsakov examples, second pass; Mahler 1/ii) v149 → v150
- Accepted: horns re-enter pp < mf at 41–43/273–275 (refines c147).
- Rejected: Mahler's stopped/bells-up horns and portamento (soft-brass rule, models).

## Cycle 148 (lens 8 expression, Aldwell & Schachter Unit 3, second pass) v148 → v149
- Accepted: bass tenutos in the tuttis; accented hemiola minims at 101–104/301–304 (no brass); pizz. bass pp at 153/341.

## Cycle 147 (lens 7 texture, Rimsky-Korsakov ch. III, second pass) v147 → v148
- Accepted: Hn 4 own part at 201–204; horns mf at 41/273.
- Kept: 79/87, 75–76/83, 45–56, 105–120, 276 (earlier protections).

## Cycle 146 (lens 6 playability, Adler ch. 12 and 14, second pass) v146 → v147
- Accepted: timpani tenuto at tutti downbeats (supersedes c056's accent); medium sticks 225–288; ppp on the last stroke.
- Kept: tunings and retunings, tied rolls, 337–339 accents.

## Cycle 145 (lens 5 engraving, Adler ch. 18 and App. A, second pass) v145 → v146
- Accepted: brass-choir tempo/rehearsal marks restored with a hide-if-no-brass callback; horn and trombone sub-brackets.
- Rejected: tempo marks above the timpani (crowding).

## Cycle 144 (lens 4 orchestration, Adler ch. 8, second pass) v144 → v145
- No findings needing change; five points kept (c127/c132/c016, c107/c111, c054).
- Do-not-touch: F-major episode 73–88, call and response 29–37, trio layering 153–224, 357–376.

## Cycle 143 (lens 3 form, Aldwell & Schachter Unit 18, second pass) v143 → v144
- Accepted: applied V6 of iv (bass G♯) at theme A bar 10: bars 22, 114, 262.
- Kept: form and length; 125–126/281–282, 329–332, link, trio exit, 201–203, 313–315.

## Cycle 142 (lens 2 harmony, Aldwell & Schachter Units 24–25, second pass) v142 → v143
- Accepted: inner octaves at 220–221 removed (Vc/Bsn 2 hold F♯3).
- Rejected: added-6th IV in the codetta/close; applied 4/3 chords at 81–84 (c052).

## Cycle 141 (lens 1 melody, Sebesky ch. 6–7, second pass) v141 → v142
- No findings needing change; six points kept (c094, c027, c047, c110 protections; closing page; pizz. bass level).

## Cycle 140 (lens 10 cyclic, Adler ch. 1 and ch. 15, second pass) v140 → v141
- No score change. Records updated; kit/ceg.py added (C–E–G inside larger chords: six passing cases kept).
- Rejected: G♯5 gap 365–368, trumpet/timpani alternation, second idea's rising sixth, Hn 1 rests at 144/240.

## Cycle 139 (lens 9 holistic, Rimsky-Korsakov examples, second pass; Tchaikovsky 5/iii) v139 → v140
- Accepted: appoggiatura clash at 131/287 resolved; horns re-enter pp at 195; oboes together on the tail at 334.
- Do-not-touch: form and length, second idea and hemiola, trio tune and 197–200 layering, 325–339, 357–376.

## Cycle 138 (lens 8 expression, Casanelles ch. 4 and 6, second pass) v138 → v139
- Accepted: hidden one-step dynamics so untargeted swells stay one level in the MIDI; F-major episode phrasing (harp slurs/swells, Cl portato); tapers at the trio hand-overs 167–168, 183–184.
- Note: untargeted hairpins in LilyPond MIDI jump about +28 velocity; give every swell a (hidden) target.

## Cycle 137 (lens 7 texture, Adler ch. 16, second pass) v137 → v138
- Accepted: viola turn figure at 193–196; viola chords clear of the cello countermelody at 177/179, 217/219.
- Kept: theme A inner voices, coda ostinato, link 141–148, tutti octaves 109–118, Hn 1 held B4, codetta, fugato and stretto.

## Cycle 136 (lens 6 playability, Adler ch. 9–10, second pass) v136 → v137
- Accepted: held fade for Hn 1·2 at 72–73; Hn 2 tenuto, not accent, at 281; Hn 3·4 breath at 104/304.

## Cycle 135 (lens 5 engraving, MOLA, second pass) v135 → v136
- Accepted: solo labels after rests on combined staves; pp at 271 (Vln II, Va); cue starts moved off empty bars; Hn cue at 193 from Vln II; harp part pedal line stripped; parts top margin 20 mm.

## Cycle 134 (lens 4 orchestration, Adler ch. 15, second pass) v134 → v135
- Accepted: hidden MIDI dynamics after bare \! hairpin ends at 52 (Vln II), 265 (Fl 1, Vln I), 353/355 (Vln I); violas mf at 45.
- Note for later critics: a hairpin ended by \! keeps fading in the MIDI to the next printed dynamic; check melody velocities against accompaniment (scan idea: compare with a no-hairpin build).

## Cycle 133 (lens 3 form, Aldwell & Schachter Units 16 and 19, second pass) v133 → v134
- No findings (all c043 points fixed; every 6/4 functional; development key plan matches Ex. 16-2b).
- Kept: trio exit length (as c103/c113/c123), coda stages, direct V–I joins.
- Do-not-touch: large form and length, development and reprise key plans, the dominant pedals' 6/4 openings, 353–356, 357–376.

## Cycle 132 (lens 2 harmony, Aldwell & Schachter Units 22–23, second pass) v132 → v133
- Accepted: d5→P5 removed at 79→80 (Hn 4, harp LH) and 126→127 (Bsn 1); the D♯°7 seventh prepared at 85–88 (Hn 3/Bsn 1 swap undone).
- Kept: 282→283 Hn 1 C5 (c082 rule); 266→267 passing quaver; 87→88 Cl 2.
- Do-not-touch: c082's V♭9 voicings at 126–127 and 282.

## Cycle 131 (lens 1 melody, Adler ch. 7, second pass) v131 → v132
- Accepted: doubling winds change octave a beat early at 39/107/307 (no maj-7 leap in the closing arpeggio); Ob 1 on the top line at 129–131/285–287.
- Kept: Ob 197–200 (c117), coda T colours, clarinet break 81–88, Cl breathing at 153, Cbsn 213–222, Fl/Ob unison 29–36.
- Do-not-touch: Vln I octave change on the head's leap (c010).

## Cycle 130 (lens 10 cyclic, Casanelles ch. 5, second pass) v130 → v131
- Accepted: 375 harp harmonics play at sounding pitch and p in the MIDI (\harmOct); coherence file brought to v131 / finale v154.
- Rejected: changes to the soft held Vln I ending, the Hn 1 + Hn 3 G♯4 overlap at 365–369, and the 339 brass diminuendo (reasons in c130.md).
- Do-not-touch: joins into and out of the movement; closing page 357–376.

## Cycle 129 (lens 9 holistic, Rimsky-Korsakov examples 126–200, second pass; Beethoven 7/iii) v129 → v130
- Accepted: trio register clashes removed at 193 (Cl 1), 209 (Hn 2), 219 (Bsn 2).
- Rejected/kept: slower trio tempo (proportions); ff trio tutti and trumpet pedal (cyclic rules).
- Do-not-touch: trio first statement 153–168, coda build and B6 peak 325–339, closing page 357–376.

## Cycle 128 (lens 8 expression, Adler ch. 11 brass climaxes and ch. 15 special effects) v128 → v129
- Accepted: 339 brass held tenuto minims with diminuendo, low brass ff (no accented brass stroke); 335–338 trumpets crescendo, tenutos not accents; 101–104/301–304 brass build to f, not ff, so the arrival at 105/305 is not a drop.
- Open: none.
- Do-not-touch: closing page 357–376.

## Cycle 127 (lens 7 texture, Adler ch. 17 second pass) v127 → v128
Both accepted (v128/critique.md): Cl 2 an octave lower at 87–88; Cl 2 rests and Hn 4 pedal from 229. Do-not-touch: no instrument of the solo's own colour beside a wind solo (Adler PDF 267) in the codetta statements 225–236.

## Cycle 126 (lens 6 playability, Adler ch. 6–7 second pass) v126 → v127
All 3 accepted (v127/critique.md): winds and Hn 1·2 breathe at 300; Fl 1 by step to B6 at 335; Hn 3 rests 233–236 under Bsn 1. Do-not-touch: the breath at 300 (winds) and the ⊓/V split at 300 (strings, c096).

## Cycle 125 (lens 5 engraving, Gould spacing second pass) v125 → v126
Both accepted (v126/critique.md): oboe lines swapped at 333–339 (no crossing); tenutos at the stem end at 105–120 (low brass) and 201–202 (Vln II).

## Cycle 124 (lens 4 orchestration, Adler ch. 15 second pass) v124 → v125
All 3 accepted (v125/critique.md): staff-level MIDI dynamics (shared staves now play as printed); brass downbeats tenuto in the tutti theme; flutes rest 105–108/305–308 and enter high at 109/309. Do-not-touch: Dynamic_performer at Staff level in \midi; tenuto (not accent) brass downbeats in the tutti theme.

## Cycle 123 (lens 3 form, Rimsky-Korsakov ch. IV) v123 → v124
Accepted (v124/critique.md): diminuendo of the held chord 362–364. Rejected: ff-attack low-brass re-entry at 333 (Dan's rule: soft brass accents, weight not bite). Do-not-touch: low brass f at 333 (c086); no ff/sfz attacks on brass re-entries.

## Cycle 122 (lens 2 harmony, A&S Unit 17 second pass) v122 → v123
Both accepted (v123/critique.md): sequence octaves removed at 76–77 (Hn 4) and 82–83 (Hn 3, Bsn 1); no doubled leading tone at 52 (Cl 1). c052's open point on 49–51 closed. Do-not-touch: the episode's rising bass F–G–A (C-major rule).

## Cycle 121 (lens 1 melody, Adler ch. 3 second pass) v121 → v122
Both accepted (v122/critique.md): T bar 6 `cis4 fis2` in all statements (theme change, logged above; closes cycle 1's open point); "sul A" removed at 169. Do-not-touch: theme A; second-idea hemiola; T's tied A and 4–3 cadence; harp melody 73–80; B6 at 336; motto tail 357–360.

## Cycle 120 (lens 10 cyclic, A&S Unit 26 second pass) v120 → v121
No musical change; coherence/scherzo.md refreshed; finale thread pointed to the current scherzo coherence files. Do-not-touch: applied V of V (not IV) in the G-major cadence 51–55 (C-major rule).

## Cycle 119 (lens 9 holistic, Bruckner 4/iii; Rimsky-Korsakov examples 61–130 second pass) v119 → v120
Accepted (v120/critique.md): Fl 2 rests at 197–200 (call is Fl 1 + Ob 1 on Vln I). Do-not-touch: at most two winds in unison on one string section (Rimsky PDF 76; c111, c119).

## Cycle 118 (lens 8 expression, Adler ch. 2 bowing second pass) v118 → v119
All 4 accepted (v119/critique.md): up-bow crescendos at 45/121, the trio third phrase, 335 and 193 (Cb). Do-not-touch: theme A spiccato over pizz. downbeats; trio violas' louré off-beats; bowings at 300 and 336–339 (c096); hemiola bowing 53/129/285 (c085).

## Cycle 117 (lens 7 texture, Adler ch. 15 second pass) v117 → v118
Both accepted (v118/critique.md): the trio's oboe call moves against the tune's held notes at 198–200; basses pp at 65. Do-not-touch: 197–200 layering (call above, tune below, distinct rhythms) after c091, c094, c107, c117.

## Cycle 116 (lens 6 playability, Adler ch. 4 harp second pass) v116 → v117
Both accepted (v117/critique.md): harp starting pedals at bar 1; étouffez at 87, 193, 241. Open: harmonics at 375 an octave low in the MIDI render only.

## Cycle 115 (lens 5 engraving, Gould ledger lines and rests second pass) v115 → v116
Accepted (v116/critique.md): Hn 3·4 in bass clef at 301–320 in the score only.

## Cycle 114 (lens 4 orchestration, Rimsky-Korsakov tutti chords second pass) v114 → v115
All 3 accepted (v115/critique.md): Hn 4 holds the bass an octave up at 305–320 (c097 kept at 105–120); contrabassoon an octave above the basses at 213–222; Fl 2/Ob 1 order at 104/304. Do-not-touch: the octave above the bass filled in every tutti (Rimsky appendix).

## Cycle 113 (lens 3 form, A&S Unit 32 second pass) v113 → v114
Both accepted (v114/critique.md): smooth MIDI tempo curve through the rit. and accelerando 237–264; comment fix. Do-not-touch: the large form and length (c083, c103, c113).

## Cycle 112 (lens 2 harmony, A&S Units 11–13) v112 → v113
All 8 accepted (v113/critique.md): inner-voice fifths removed at 108/308, 110–111/310–311 (♭9 suspension), 124/280, 157, 196–201, 219–221, 346, 351–352; harp common tones at 82–83. Open: Hn 1/cellos octaves 220–221 (c092).

## Cycle 111 (lens 1 melody, Rimsky-Korsakov ch. II winds second pass) v111 → v112
Accepted (v112/critique.md): Vln II with Vln I at 41–43/273–275 under the a2 winds. Do-not-touch: wind a2 at 37–44/273–275 (c107) with both violin sections on the tune.

## Cycle 110 (lens 10 cyclic, A&S Unit 32 second pass) v110 → v111
No musical change; coherence/scherzo.md refreshed; finale told the scherzo ends ppp. Do-not-touch: G♯ = A♭ frame (1–2, 360–376); held A with C♯→C at 72–73; F→F♯ exit at 86–88; motto tail 205–209 and 357–360; timpani tunings at both joins.

## Cycle 109 (lens 9 holistic, Brahms 2/iii; Rimsky-Korsakov examples 1–60 second pass) v109 → v110
Accepted (v110/critique.md): Hn 3 an octave lower at 121–128. Nothing worse than v99. Open: Cl 1 crossing Ob 1/Vln II in the second idea (protected by c014).

## Cycle 108 (lens 8 expression, Rimsky-Korsakov ch. IV second pass) v108 → v109
All 5 accepted (v109/critique.md): accompaniment a level under the tune at 29–35 and 45; crescendo into 336; crescendos through 249–252; fades at 8 and 147–148. Do-not-touch: leggiero theme over pp off-beats 13–28; coda build 325–333; sfp at 301; closing page 357–376.

## Cycle 107 (lens 7 texture, Adler ch. 5 second pass) v107 → v108
All 3 accepted (v108/critique.md): Vln II with the violas' tune head at 197–200; arco cello countermelody under the coda statement 349–356; flutes and oboes a2 on the theme at 37–44/273–275. Do-not-touch: fugato exposition 57–68; flute heterophony 253–268; trio layering 169–184.

## Cycle 106 (lens 6 playability, Adler ch. 3 second pass) v106 → v107
Accepted (v107/critique.md): cellos div. at 244 for the French-sixth pizz. Do-not-touch: viola lines 241–248 (c037/c062/c098).

## Cycle 105 (lens 5 engraving, Gould beams second pass) v105 → v106
All 3 accepted (v106/critique.md): beam callback in score.ly (c015) corrected for mid-space ends, slopes and concave groups. Do-not-touch: stems.ily (c095); stem lengths in shared two-voice staves; string beaming of theme A and motive x.

## Cycle 104 (lens 4 orchestration, Rimsky-Korsakov ch. III second pass) v104 → v105
Both accepted (v105/critique.md): Hn 2 F♯4 at 119/319 (no horn second); Fl 2 B5 at 339 (fifth in the final woodwind chord). Do-not-touch: clarinets inside the horns in the second idea (c014); the F-major episode wind chord 73–88.

## Cycle 103 (lens 3 form, A&S Unit 26 second pass) v103 → v104
Both accepted (v104/critique.md): stale header comments in coda/dA/tC corrected; coherence/scherzo.md key plan refreshed. No musical change. Do-not-touch: the key plan 13–104 (c083); G minor at 289; link 133–152; the length.

## Cycle 102 (lens 2 harmony, A&S Units 9–10 second pass) v102 → v103
All 3 accepted (v103/critique.md): cadential 6/4 at 195 (bass B); V4/2 passing chord at 123/279; prepared fourth (Vla G4) at 52. Do-not-touch: c032's sequence bass 49–52; hemiola cadences.

## Cycle 101 (lens 1 melody, Rimsky-Korsakov ch. II strings, second pass) v101 → v102
Both accepted (v102/critique.md): Vln II lower octave of the hemiola melody at 101–104/301–304 (closes c087 open); contrabassoon with the basses at 209–224 (closes c094 open).

## Cycle 100 (lens 10 cyclic, release check) v100 → v101
Release check passed; both accepted (v101/critique.md): subtitle with tempo; coherence/scherzo.md refreshed. No musical change. Finale exports unchanged v86–v101 (41/41).

## Cycle 99 (lens 9 holistic, Dvořák 8/iii; Casanelles ch. 6) v99 → v100
All 3 accepted (v100/critique.md): coda harp chords up an octave at 345–348; harp pp under the trio solos at 153/185; Hn 1 pp at 241. Do-not-touch: accompaniment one dynamic level under the tune and out of its register (Casanelles PDF 271–278).

## Cycle 98 (lens 8 expression, A&S Unit 21) v98 → v99
All 4 accepted (v99/critique.md): suspension hairpins (swell into the dissonance, softer resolution) at the trio cadences 165/181/221, Hn 1's motto tail 357–360, coda 355 and retransition 245–249. Do-not-touch: accent-then-softer shaping of suspensions (A&S PDF 348, 350).

## Cycle 97 (lens 7 texture, Adler ch. 11) v97 → v98
All 3 accepted (v98/critique.md): stretto entries a bar apart at 69–71/297–299; Hn 1·2 unison motive x at 71/299; Hn 3 doubles Hn 4's tenor countermelody at 105–120/305–320 (c066 partly reversed). Do-not-touch: fugato entries 57–68 with countersubject; timpani motive x with pizz. at 89–100; hemiola brass 101–104; the stretto layout 69–71.

## Cycle 96 (lens 6 playability, Adler ch. 2 second pass) v96 → v97
All 3 accepted (v97/critique.md): bar 300 split ⊓/V so 301–306 bow as 101–106; down-bows for low strings and violas at 336–339; Cb tied up-bow at 223–224. Do-not-touch: the bow split at 300 (it sets the reprise's bowing).

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
