# Movement I themes (theme record, v221)

This is a record of movement I's ideas as they stand in the finished movement I, mvt1/v221 (182 bars, 4/4, concert pitch). The other movements quote from it and compare their quotations against it. The notes are in [themes-mvt1.ly](themes-mvt1.ly), one variable per idea. Only the movement I thread edits these two files. Every pitch and rhythm was checked against mvt1/v221/sections/*.ily. Where cyclic-notes.md differs, the v221 source is used, and the differences are listed at the end of this file.

The checker: `themecheck.py themes-mvt1.ly <version dir> --beats 4` reads the `%@` lines. All 35 `%@` lines compare unchanged against v221 when two limits of lyparse.py are fixed in a private copy (see "Checker notes" below). A quotation in another metre or rhythm is judged by the idea's `invariant`, not by the checker's rhythm and start-beat test.

| Variable (id) | Bars, instrument | Use in later movements (cyclic-notes.md) | Invariant |
|---|---|---|---|
| mvtOneMotto (motto-slow) | 1–4, B.cl. + Vc (G2), Cb 8vb, pp | Finale chorale: this form in major, top line `g1 e'1 d'1 c'2 des'2 c'1`, last statement ending `c'2 b2 c'1` | Pitch classes G E♭ D C D♭ C (5 ♭3 2 1 ♭2 1), major form G E D C D♭/B C; transposable; rhythm free |
| mvtOneMottoAnswer (motto-answer-ca) | 5 (beat 4)–9, C.a., p espr. | None planned | D B♭ A G A♭ G; rhythm free |
| mvtOneRisingSixthChain (rising-sixth-chain) | 9 (beat 4)–13, Vln I | New themes in II–IV must not open with a rising sixth; it belongs to the motto | Rising sixths G–E♭, A♭–F, B–A♭; first one in the motto rhythm |
| mvtOneHornCall (horn-call) | 13–14, Hn 1 alone, E♭3–C4–B3 | Scherzo Hn 1 3–6 (G♯3–E4–D♯4, the 7 held and unresolved, as in movement I; no E4 at 7–8); finale trumpets E–C–B→C, horns below (243–246) | Scale degrees 3–1–7 (♭3 or 3), resolution to 1 optional; transposable |
| mvtOneHornCallCoda (horn-call-coda) | 175 (beat 4)–177, Cl 1, pp | As the horn call | As the horn call |
| mvtOneThemeP (theme-p) | 15–22, Vln I, f; D♭6 sf at 20 | Finale: P only as a link; its tutti layout of 27–32 returns in C minor at 199–210 and in major at 247–254 | Intervals and rhythm |
| mvtOneThemePHead (theme-p-head) | 15–16, Vln I (also 27, 131 low, 167 brass/Vla) | Finale: combined with the S head in C major, fast, full brass (247–254, 269–272) | Rhythm `r8 8 4. 8 8 8 \| 4 8 8 4. 8` and intervals; transposable |
| mvtOneThemeSAflat (theme-s-aflat) | 46 (beat 4)–50, Hn 1 + Vc, A♭ major | II must not open with it; II quotes the S head once, minor form with pickup, remote key (II 47–53, C.a.) | Rhythm `4 \| 2.~ 8 8 \| 4 2 4` with its intervals; mode, key and scoring free |
| mvtOneFluteMotto (flute-motto) | 73 (beat 4)–75, Fl 1, p > pp, A♭ pedal | None planned | C A♭ G G♭ F E♭ F♭, rhythm `4 \| 2.~ 8 8 \| 2 4 8 8` |
| mvtOneThemeSBminor (theme-s-bminor) | 97 (beat 4)–102, Vln I + Ob 1 (Fl 1 8va), ff | Model of the minor anacrusis form (`g4 \| es'2.~ es'8 d'8 \| c'4 aes'2 g'4` in C minor), which II quotes once | Rhythm `4 \| 2.~ 8 8 \| 4 2 4` and intervals; transposable |
| mvtOneMottoSecondForm (motto-second-form) | 117–121, Tbn 1·2 + Hn 1·2 + Bsn 1, B.tbn 8vb, ff | None planned | G E♭ D D♭ C (no C before D♭); rhythm free |
| mvtOneMottoHalfAug (motto-half-augmented) | 129–130, Cl 1 | None planned | G E♭ D D♭ C, rhythm `4 2 4 \| 4 2.` |
| mvtOneMottoTail (motto-tail) | 2–3, B.cl. at E♭3 (E♭–D–C–D♭–C) | II (B.cl. E♭3 at 32–34; Cl 1 coda 85–89); scherzo theme A (G–F♯–F–E) and Hn 1 357–360 (B–A♯–A–G♯); not a third time at E♭3 in the B.cl. | E♭ D D♭ C (passing C before D♭ optional); transposable; rhythm free |
| mvtOneThemeSCmajor (theme-s-cmajor) | 146 (beat 4)–150, Hn 1 + Vla (G3), Vc 8vb, mp–mf | Finale: falling major motto G–E–D–C in full brass at f; C-major S head | Rhythm `4 \| 2.~ 8 8 \| 4 2 4` and intervals |
| mvtOneViolinsFlatSeven (s-head-flat-seven) | 155 (beat 4)–157, Vln I·II | None planned | F D D♭ C, rhythm `4 \| 2.~ 8 8 \| 2` |
| mvtOneClimaxLine (climax-line) | 158–161, Vln I·II, Fl 1·2, Ob 2, Tpt 1, Hn 1·2; fff and A♭6 at 160 | Finale's last climax must reach C7, above this A♭6 | Pitches and rhythm as written |
| mvtOneMottoCodaCA (motto-coda-ca) | 171 (beat 4)–174, C.a., p espr. | None planned | G E♭ D C D♭ C; rhythm free |
| mvtOneThemeSCodaMinor (theme-s-coda-cminor) | 171–174, Vc solo (since v270; Tutti at 175), no pickup, C minor | Finale: second theme minor first, major on the repeat | Rhythm and intervals; transposable |
| mvtOneMottoChorale (motto-chorale) | 175–179, B.tbn / Tbn 2 / Tbn 1, pp, tam-tam | Finale chorale: trombone colour, top line in major, f–ff, horns and trumpets added, no tam-tam, independent bass (not this octave doubling); canon with violins two bars later | Top line G E♭ D C D♭ C in semibreves (C–D♭ minims) |
| mvtOneMottoViolins (motto-violins-last) | 177 (beat 4)–182, Vln I, pp > ppp | Canon model for the finale chorale; II takes the C5 at its bar 1 | G E♭ D C D♭ C; rhythm free |
| mvtOneTimpaniPulse (timpani-pulse) | 179–180, timpani, pp | Finale: between chorale phrases, C and G only (unused in II) | Rhythm `4 r8 8 4 r4`, tonic–dominant–tonic |
| mvtOneStopChord (stop-chord) | 26 (bass B), 138 (bass D), 170 (over C pedal), tutti | Recurs unresolved in II: complete at 33 (beat 2, over the A♭ pedal); complete again at II 64 beat 3 with D in the bass as at I 138 (D2 Vc·Cb·B.tbn, F3 Tbn 1, G♯3 violas, B3 Vln II), turning to E7 (Ger6 of A♭) on beat 4; in II its B always falls a semitone; the finale resolves it once to C major with the trumpets' B→C (222→223) | The chord B D F A♭, accented, held |
| mvtOneWithheldSHead (withheld-s-head) | v99 155 (beat 4)–159, Vln I·II. Reserved for finale, not in v221 | Finale: violins mf–f molto cantabile after the chorale's C-major arrival (235–242) | Pitches and rhythm as written, with counter and bass |
| mvtOneWithheldCounter (withheld-s-counter) | v99 156–159, Cl 1 + Hn 2. Reserved for finale, not in v221 | Finale, under the withheld S head | Chromatic descent C–B–B♭–A … G–F, rhythm as written |
| mvtOneWithheldBass (withheld-s-bass) | v99 156–159, Cb (Bsn 1 8va). Reserved for finale, not in v221 | Finale, under the withheld S head | C C \| D F \| G |

25 variables for 23 ideas: the withheld statement is one idea in three variables (melody, counter, bass).

## Differences between cyclic-notes.md and v221 (v221 used)

1. **Motto tail, bars 2–3.** cyclic-notes ("Start here", "Already used in movement II") says the bass clarinet plays the tail E♭3–D3–D♭3–C3 at 2–3. In v221 it plays E♭3–D3–C3–D♭3–C3 (the intro form, with the return to C before D♭). The bare E♭–D–D♭–C occurs in movement I only in the motto's second form (118–121) and as D6–D♭6–C6 in the violins at 156–157.
2. **Cor anglais answer.** cyclic-notes gives "bars 5–8" with the pickup `d'4`. In v221 the pickup is on beat 4 of bar 5, the answer runs 6–8, and the G4 is held to beat 3 of bar 9.
3. **Rising-sixth chain.** cyclic-notes gives Vln I 9–12. The line ends on G5 held through bar 13 (diminuendo, rest at 14).
4. **Flute motto, 73–76.** cyclic-notes §1 ends it `es''8 f''8`. v221 has `es''8 fes''8` (F♭5, since cycle 182), and Fl 1 rests in bar 76. The motto runs from beat 4 of 73 to the end of 75.
5. **First theme, bar 19.** cyclic-notes §1 gives `r8 c''8 aes''4.`. v221 has `r8 aes'8 aes''4.` (the octave-leap pickup that the cycles 101–110 note mentions, but §1 was never updated).
6. **Second form of the motto, 117–121.** cyclic-notes says "Trombones 1·2 (and B.tbn/Hn 1·2 in octaves)". In v221 Hn 1·2 and Bsn 1 play in unison with Tbn 1·2 (G3); only the bass trombone is an octave lower. Hn 1·2 breathe before the D at 119.
7. **Stop chord.** cyclic-notes treats 26, 138 and 170 as the same chord. The pitch classes are the same, but only bar 26 has B in the bass (B1). At 138 the bass is D (Cb D2, Vc D3). At 170 the chord sits over a C pedal (Cb C2, tuba, B.cl., Bsn 2, B.tbn, Cbsn, timpani C3), and B is heard only in Tpt 1·2 (B4) and Hn 1·2 (B3).
8. **Trumpets' B→C.** cyclic-notes lists it as withheld ("trumpets last play B♮ at 170"). That is true of the last note, but Tpt 1 already moves B4 → C5 into the C-minor tuttis at 26→27 (after a crotchet rest) and 138→139, and passes B4–C5 at the end of 161 in the climax line. What movement I withholds is B→C on a C-major arrival that resolves the stop chord.
9. **Last bars, Hn 3.** The "Changes since cycle 90" note gives Hn 3 C4 at 180–182. In v221 Hn 3 enters at 181 (with Hn 4), and Tbn 1's C4 overlaps it to beat 1 of 181.
10. **Withheld bass (v99).** cyclic-notes §2 gives the bass as `c1 | c1 | d2 f,2 | g,1`. In v99 that is Bsn 1's line, which ends `g,2. r4`. The double basses sound an octave lower (`c,1 | c,1 | d,2 f,,2 | g,,1`), which is the version used in the record.
11. **A♭6 peaks.** The cycle 200 note is correct (violins at 31, 72, 122, 160; Fl 1 alone at 140). In addition, Fl 1 doubles the A♭6 at 31, 72, 122 and 160, Fl 2 at 72 and 160. Since v230 Vln II plays A♭5 at 160 (an octave below Vln I).

Unchanged and confirmed: the motto at 1–4, the coda cor anglais 171–174, the chorale 175–179, the violins 177–182, the horn call 13–14 and Cl 1 175–177, the S head in A♭ (47–50), B minor (97–102), C major (147–150) and C minor (171–174), the violins 155–157, the climax line 158–161, the half-augmented motto 129–130, the timpani pulse 179–180, and the withheld violin statement and counter in v99.

## Checker notes

- lyparse.py reads mvt1/v221 only with two fixes, made here in a private copy and not in this folder. (1) `sections()` skips rows without a third (beats) column, and mvt1's sections.txt has two columns (name, bars), so every part comes back empty. (2) It reads `\clef bass`/`\clef alto`, `\override X.y = #n` and `#'symbol` as notes, and it does not expand variable references. For example, Vln I 156–166 is `\recTwoMelody`, so Vln II and Fl 1 stand in for it in the `%@` lines.
- `themecheck.py` needs `--beats 4` for movement I.
- The stop chord is not in a `%@` line, because the checker compares single lines. Neither are the withheld v99 variables, because they are not in v221.
