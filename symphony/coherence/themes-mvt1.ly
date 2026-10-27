% THEME RECORD for movement I (Allegro, C minor). Recorded 2026-10-12 from mvt1/v221, the finished movement I (182 bars, 4/4).
% This is a record of movement I's ideas at v221. Movements II-IV quote from it and compare their quotations against it.
% Movement I is finished, so nothing here changes unless movement I itself is revised. Only the movement I thread edits this file.
% Pitches and rhythms were checked against mvt1/v221/sections/*.ily (the v221 source wins over cyclic-notes.md; differences are
% listed in coherence/themes-mvt1.md). Exception: the withheld violin statement is not in v221; it comes from mvt1/v99/sections/recTwo.ily.
%
% Format (same structure as coherence/themes-scherzo.ly): one LilyPond variable per idea, absolute pitch, Dutch note names,
% concert pitch, exact rhythm, 4/4 bars. Bar 1 of the variable = the idea's first bar; a pickup is written as leading rests
% (r2. g4 = a crotchet pickup on beat 4), as in themes-scherzo.ly, so that themecheck.py reads the beat the idea starts on.
% A chord gives the voicing bottom to top. No \key or \clef inside a variable (lyparse.py would read "c" or "bass" as notes);
% the printed \score at the end uses no key signatures and takes its clefs from \autoChange; each idea's key is in its key/mode: field.
% Above each variable:
%   % <variable>: v221 <part suffix> bars <a>-<b>     (the scherzo file's one-line header)
%   % id:          short slug
%   % source:      mvt1 v221 bars, instrument(s)
%   % key/mode:
%   % use:         where later movements quote it or are meant to (from cyclic-notes.md)
%   % invariant:   what a quotation must keep
% %@ lines at the end of the file use themecheck.py's syntax (theme, part suffix, bar[, notes[, first note]]) and give where
% each idea sits in mvt1 v221; compare with --beats 4. Two limits of coherence/lyparse.py as of 2026-10-12 when it reads mvt1/v221
% itself: it skips sections.txt rows without a third (beats) column, and mvt1's sections.txt has two columns (name, bars); and it
% reads "\clef bass/alto", "\override X.y = #n" and "#'symbol" as notes. With those two fixed in a private copy, all %@ lines
% below compare unchanged against v221. A quotation of movement I in another metre or rhythm is judged by its % invariant: field,
% not by the checker's rhythm and start-beat test.
\version "2.24.0"
\language "nederlands"

% mvtOneMotto: v221 BassCl bars 1-4
% id: motto-slow
% source: mvt1 v221 bars 1–4, bass clarinet and cellos in unison (G2), double basses an octave lower (sounding G1); pp, over a timpani C3 roll ppp
% key/mode: C minor
% use: finale brass chorale = this intro form in major, top line g1 | e'1 | d'1 | c'2 des'2 | c'1 (last statement ends c'2 b2 | c'1), trombone colour f–ff with an independent bass; II and the scherzo quote only its tail (see mvtOneMottoTail)
% invariant: pitch-class sequence G Eb D C Db C (scale degrees 5 b3 2 1 b2 1); in the finale's major form G E D C Db C or G E D C B C; transposable; rhythm free (slow, the G a pickup)
mvtOneMotto = { \time 4/4 r2. g,4 | es2.~ es8 d8 | c2 des4 c4~ | c1 }

% mvtOneMottoAnswer: v221 CorAnglais bars 5-9
% id: motto-answer-ca
% source: mvt1 v221 bars 5 (beat 4) – 9, cor anglais solo, p espr.; the G4 reached at 7.4 is held to bar 9, beat 3
% key/mode: the motto a fifth higher (on D) in C minor; harmony C (5) – Eb/G (6) – Db/F (7) – C major with E natural in Vln II (8) – C minor (9)
% use: none planned; recorded because it is the motto's first transposition
% invariant: pitch-class sequence D Bb A G Ab G (the motto's intervals); rhythm free
mvtOneMottoAnswer = { \time 4/4 r2. d'4 | bes'2.~ bes'8 a'8 | g'2 aes'4 g'4~ | g'1 }

% mvtOneRisingSixthChain: v221 VlnOne bars 9-13
% id: rising-sixth-chain
% source: mvt1 v221 bars 9 (beat 4) – 13, Violins I, mp < f; Vln II echoes 10–11 (f'2. c'4 | aes'2 f'2)
% key/mode: C minor: i (9) – iv (10) – iiø7 over D (11) – German sixth Ab-C-Eb-F# (12) – V (13)
% use: rule since critic 101: the rising sixth belongs to the motto; new themes in II–IV must not open with it
% invariant: three rising sixths G–Eb, Ab–F, B–Ab with the motto's opening rhythm on the first (4 | 2. 4); transposable
mvtOneRisingSixthChain = { \time 4/4 r2. g'4 | es''2. aes'4 | f''2 b'4 aes''4~ | aes''2. g''4~ | g''1 }

% mvtOneHornCall: v221 HnOne bars 13-14
% id: horn-call
% source: mvt1 v221 bars 13–14, Horn 1 alone (undoubled), mp > p, over the dominant (G pedal); the B3 is left unresolved
% key/mode: C minor, scale degrees b3 – 1 – 7 (Eb3 – C4 – B3)
% use: Scherzo Hn 1 3–6 (G#3–E4–D#4, the 7 held and unresolved, as in movement I; no E4 at 7–8); finale: major form E–C–B→C in the trumpets with horns below (finale 243–246)
% invariant: scale degrees 3 – 1 (rising sixth) – 7, mode free (b3 or 3), may add the resolution to 1; transposable; rhythm free
mvtOneHornCall = { \time 4/4 r4 es4 c'2~ | c'4 b2 r4 }

% mvtOneHornCallCoda: v221 ClOne bars 175-177
% id: horn-call-coda
% source: mvt1 v221 bars 175 (beat 4) – 177, Clarinet 1, pp, against the trombone chorale; the B4 is left unresolved
% key/mode: C minor, b3 – 1 – 7 (Eb4 – C5 – B4)
% use: as mvtOneHornCall
% invariant: as mvtOneHornCall
mvtOneHornCallCoda = { \time 4/4 r2. es'4 | c''1~ | c''2 b'2 }

% mvtOneThemeP: v221 VlnOne bars 15-22
% id: theme-p
% source: mvt1 v221 bars 15–22, Violins I, f (Allegro appassionato); peak Db6 sf at 20 (Vln II doubles it an octave lower 20–21)
% key/mode: C minor
% use: finale: P is used only as a link; its hammered tutti layout (27–32) returns in the finale in C minor (199–210) and in major (247–254); scherzo: candidate for a quotation in diminution in triple metre
% invariant: pitches and rhythm of the head (see mvtOneThemePHead); for the whole theme, interval sequence and rhythm, transposable
mvtOneThemeP = { \time 4/4 r8 g'8 es''4. d''8 des''8 c''8 | c''4 b'8 c''8 aes'4. g'8 | r8 g'8 f''4. es''8 d''8 c''8 | b'4 d''8 c''8 g'2 |
  r8 aes'8 aes''4. g''8 f''8 es''8 | des''8 es''8 f''8 aes''8 des'''2~ | des'''8 c'''8 bes''8 aes''8 g''4. f''8 | es''8 d''8 c''8 b'8 c''4 r4 }

% mvtOneThemePHead: v221 VlnOne bars 15-16
% id: theme-p-head
% source: mvt1 v221 bars 15–16, Violins I (also in octaves at 27–28, low at 131–132, and in Hn 1·2/Tpt 1·2/Vla at 167–168)
% key/mode: C minor
% use: finale: combined with the second-theme head in C major, fast, full brass (finale 247–254, 269–272)
% invariant: rhythm r8 8 4. 8 8 8 | 4 8 8 4. 8 and intervals (G–Eb–D–Db–C | C–B–C–Ab–G: the motto head in diminution with the tail C–B–C); transposable
mvtOneThemePHead = { \time 4/4 r8 g'8 es''4. d''8 des''8 c''8 | c''4 b'8 c''8 aes'4. g'8 }

% mvtOneThemeSAflat: v221 HnOne bars 46-50
% id: theme-s-aflat
% source: mvt1 v221 bars 46 (beat 4) – 50, Horn 1 (dolce) and cellos in unison, pp–p; harp broken chords; continues to 55
% key/mode: Ab major
% use: II must not open with it; II quotes the S head once, in minor with the pickup and in a remote key (II 47–53, cor anglais)
% invariant: rhythm 4 | 2.~ 8 8 | 4 2 4 (anacrusis and two-bar head) with intervals rising sixth, falling step, falling step | rising sixth, falling step; mode, key and scoring may change
mvtOneThemeSAflat = { \time 4/4 r2. es4 | c'2.~ c'8 bes8 | aes4 f'2 es'4 | des'4. c'8 bes4 des'8 f'8 | aes'2 g'2 }

% mvtOneFluteMotto: v221 FluteOne bars 73-75
% id: flute-motto
% source: mvt1 v221 bars 73 (beat 4) – 75, Flute 1 solo, p espr. > pp, over the Ab pedal (Vc, Cb, Hn 4); bar 76 rests
% key/mode: Ab major darkened to Ab minor (Gb, Fb; Vln II Fb4 at 76, mixture iv6/4)
% use: none planned
% invariant: C – Ab (rising minor sixth) – G – Gb – F – Eb – Fb, rhythm 4 | 2.~ 8 8 | 2 4 8 8; transposable
mvtOneFluteMotto = { \time 4/4 r2. c''4 | aes''2.~ aes''8 g''8 | ges''2 f''4 es''8 fes''8 }

% mvtOneThemeSBminor: v221 VlnOne bars 97-102
% id: theme-s-bminor
% source: mvt1 v221 bars 97 (beat 4) – 102, Violins I and Oboe 1, Flute 1 an octave higher, ff; Vln II (sul G) and cor anglais an octave lower from 98 without the pickup
% key/mode: B minor (written in the source as C minor material inside \transpose c cis)
% use: the model of the minor anacrusis form, in C minor g4 | es'2.~ es'8 d'8 | c'4 aes'2 g'4; II quotes this form once in a remote key (II 47–53)
% invariant: rhythm 4 | 2.~ 8 8 | 4 2 4 and its intervals (rising minor sixth, falling semitone, falling tone | rising minor sixth, falling semitone), transposable
mvtOneThemeSBminor = { \time 4/4 r2. fis'4 | d''2.~ d''8 cis''8 | b'4 g''2 fis''4 | e''4. d''8 cis''4 e''8 g''8 | b''2 ais''2 | fis''4 d'''2 cis'''8 gis''8 }

% mvtOneMottoSecondForm: v221 TbnOne bars 117-121
% id: motto-second-form
% source: mvt1 v221 bars 117–121, Trombones 1·2, Horns 1·2 and Bassoon 1 at this pitch, bass trombone an octave lower, ff over the G pedal; arrives on the fff Ab climax at 122
% key/mode: C minor, on the dominant pedal
% use: none planned
% invariant: pitch-class sequence G Eb D Db C (no return to C before Db); rhythm free
mvtOneMottoSecondForm = { \time 4/4 g1 | es'1~ | es'2. d'4 | des'2. c'4~ | c'2.. r8 }

% mvtOneMottoHalfAug: v221 ClOne bars 129-130
% id: motto-half-augmented
% source: mvt1 v221 bars 129–130, Clarinet 1 (retransition stretto; Vla 129–130, Vln II and Bsn 1 at 130 on the first four notes)
% key/mode: C minor, over the G pedal
% use: none planned
% invariant: pitch-class sequence G Eb D Db C, rhythm 4 2 4 | 4 2.
mvtOneMottoHalfAug = { \time 4/4 g4 es'2 d'4 | des'4 c'2. }

% mvtOneMottoTail: v221 BassCl bars 2-3
% id: motto-tail
% source: mvt1 v221 bars 2–3, bass clarinet (and cellos) at Eb3, pp. In bars 2–3 the order is Eb3–D3–C3–Db3–C3; the bare tail Eb–D–Db–C occurs in movement I in the motto's second form (118–121) and in Vln I's D6–Db6–C6 at 156–157
% key/mode: C minor (in Ab major: 5 – #4 – 4 – 3)
% use: II builds on it (II 32–34 B.cl at Eb3; II coda 85–89 Cl 1); scherzo theme A G–F#–F–E and Hn 1 357–360 (B–A#–A–G#); the Eb3 bass-clarinet register has been used twice and must not be used a third time
% invariant: pitch-class sequence Eb D Db C (falling semitones from b3 to 1; the passing return to C before Db may be included), transposable, rhythm free
mvtOneMottoTail = { \time 4/4 es2.~ es8 d8 | c2 des4 c4 }

% mvtOneThemeSCmajor: v221 HnOne bars 146-150
% id: theme-s-cmajor
% source: mvt1 v221 bars 146 (beat 4) – 150, Horn 1 (mp dolce) and violas (mf dolce) in unison at G3, cellos an octave lower, over Vln II sul tasto tremolo; cor anglais answers 147–155
% key/mode: C major (the falling major motto G–E–D–C, heard only here and only at mp–mf)
% use: finale: the falling major motto G–E–D–C in full brass at forte; the C-major S head in the finale's second theme and combinations
% invariant: rhythm 4 | 2.~ 8 8 | 4 2 4 and intervals of the head; the falling G–E–D–C may be stated in other rhythms in the finale's brass
mvtOneThemeSCmajor = { \time 4/4 r2. g4 | e'2.~ e'8 d'8 | c'4 a'2 g'4 | f'4. e'8 d'4 f'8 a'8 | c''2 b'2 }

% mvtOneViolinsFlatSeven: v221 VlnOne bars 155-157
% id: s-head-flat-seven
% source: mvt1 v221 bars 155 (beat 4) – 157, Violins I and II (Vln II an octave lower), mf <; Hn 2 D4–Db4 at 156
% key/mode: C major, on bVII (Bb); the motto's D–Db–C at the top
% use: none planned
% invariant: F – D (rising sixth) – Db – C, rhythm 4 | 2.~ 8 8 | 2
mvtOneViolinsFlatSeven = { \time 4/4 r2. f''4 | d'''2.~ d'''8 des'''8 | c'''2 bes''4 aes''8 g''8 }

% mvtOneClimaxLine: v221 VlnOne bars 158-161
% id: climax-line
% source: mvt1 v221 bars 158–161, Violins I and II, Flutes 1·2 (same octave), Ob 1, Tpt 1 and Hn 1·2 an octave or two lower; ff (158), fff (160) with Ab bass, crash cymbal at 160
% key/mode: C major, bVI (Ab) at 160
% use: the finale's last climax must top the Ab6 here with C7
% invariant: G – E (rising sixth) – F – G | C – Ab (rising minor sixth, Ab6 peak) – G – F – D – B – C, rhythm as written
mvtOneClimaxLine = { \time 4/4 g''4 e'''2.~ | e'''4 f'''4 g'''2 | c'''4 aes'''2~ aes'''8 g'''8 | f'''2 d'''4 b''8 c'''8 }

% mvtOneMottoCodaCA: v221 CorAnglais bars 171-174
% id: motto-coda-ca
% source: mvt1 v221 bars 171 (beat 4) – 174, cor anglais, p espr., against the cellos' minor S head
% key/mode: C minor (Più lento)
% use: none planned
% invariant: pitch-class sequence G Eb D C Db C, rhythm free
mvtOneMottoCodaCA = { \time 4/4 r2. g'4 | es''2.~ es''8 d''8~ | d''4 c''4 des''2 | c''2 r2 } % since v401: D-flat5 for two beats (N6), C5 on the 6/4 at 174

% mvtOneThemeSCodaMinor: v221 Vc bars 171-174
% id: theme-s-coda-cminor
% source: mvt1 v221 bars 171–174, cellos, mp espr., no pickup; the B4 at 174 is left unresolved (cadential 6/4 – V)
% key/mode: C minor: i – iv – Neapolitan sixth (173) – cadential 6/4 – V (174)
% use: finale: second theme minor first, major on the repeat (the reverse of movement I)
% invariant: rhythm 2.~ 8 8 | 4 2 4 | 4. 8 4 8 8 | 2 2 and intervals; transposable
mvtOneThemeSCodaMinor = { \time 4/4 es'2.~ es'8 d'8 | c'4 aes'2 g'4 | f'4. es'8 des'4 f'8 aes'8 | c''2 b'2 }

% mvtOneMottoChorale: v221 TbnOne bars 175-179
% id: motto-chorale
% source: mvt1 v221 bars 175–179, Trombone 1 (top), Trombone 2, bass trombone (bottom), pp dolce, tam-tam pp at 175; bass clarinet, cellos and double basses (an octave lower) double the bass trombone; written here as chords bass trombone – Tbn 2 – Tbn 1
% key/mode: C minor
% use: finale chorale: keep the trombone colour and the top line in major, f–ff, horns and trumpets added, no tam-tam, an independent bass (not this octave doubling of Tbn 1 and B.tbn); may be set in canon with the violins two bars later
% invariant: top line G Eb D C Db C in semibreves (C–Db minims); in the finale in major, top line G E D C Db C (first) / G E D C B C (last)
mvtOneMottoChorale = { \time 4/4 <g, es g>1 | <es g es'>1 | <d f d'>1 | <c g c'>2 <des f des'>2 | <c es c'>1 }

% mvtOneMottoViolins: v221 VlnOne bars 177-182
% id: motto-violins-last
% source: mvt1 v221 bars 177 (beat 4) – 182, Violins I, pp > ppp; in canon two bars after the chorale's bass; the C5 crosses into movement II (fermata, l.v.)
% key/mode: C minor, ending on C major (viola E natural at 182)
% use: canon model for the finale's chorale (violins two bars after the brass); II takes the C5 over at its bar 1
% invariant: pitch-class sequence G Eb D C Db C, rhythm free
mvtOneMottoViolins = { \time 4/4 r2. g'4 | es''1~ | es''2. d''4 | c''2 des''2 | c''1~ | c''1 }

% mvtOneTimpaniPulse: v221 Timp bars 179-180
% id: timpani-pulse
% source: mvt1 v221 bars 179–180, timpani, pp (soft sticks), C3 and G2
% key/mode: C minor (tonic and dominant)
% use: finale: between phrases of the major chorale, on C and G only; not used in II
% invariant: rhythm 4 r8 8 4 r4 on tonic – dominant – tonic
mvtOneTimpaniPulse = { \time 4/4 c4 r8 g,8 c4 r4 | c4 r8 g,8 c4 r4 }

% mvtOneStopChord: v221 VlnOne bars 26, 138, 170
% id: stop-chord
% source: mvt1 v221 bar 26 (ff tutti; bass B1 in Cb, Cbsn, tuba; Fl 1, Tpt 1, Vln I on B; timpani G2), bar 138 (f tutti; bass D2), bar 170 (ff tutti under a fermata over the C pedal in Cb/tuba/B.cl/Bsn 2/B.tbn; B only in Tpt 1·2 B4 and Hn 1·2 B3). Reduced voicings, string chords as written
% key/mode: C minor, vii°7 (B D F Ab); 26 resolves to i at 27, 138 to iv (F minor) at 139, 170 is cut off (fermata) and followed by the C-minor coda
% use: recurs unresolved in II (33, 64); the finale resolves it once to C major with the trumpets' B→C (finale 222→223, also 138)
% invariant: the chord B D F Ab (fully diminished seventh on the leading tone of C), accented, on a held note value; spelling kept
mvtOneStopChord = { \time 4/4 <b,, b, aes f' b' d'' aes'' b''>2. r4 | <d, d aes f' b' d'' aes'' b''>2. r4 | <c, b d' f' b' d'' aes'' f'''>2. r4 }

% mvtOneWithheldSHead: v99 VlnOne bars 155-159 (reserved for finale, not in v221)
% id: withheld-s-head
% source: mvt1 v99 bars 155 (beat 4) – 159, Violins I and II in unison, mf, from mvt1/v99/sections/recTwo.ily (recTwoMelodyA with its pickup). Reserved for finale, not in v221 (v221 keeps recTwoMelodyA unused, without the pickup)
% key/mode: C major, over a C tonic pedal
% use: finale: the violins, mf–f molto cantabile, after the brass chorale has arrived in C major (finale 235–242)
% invariant: pitches and rhythm g'4 | e''2.~ e''8 d''8 | c''4 a''2 g''4 | f''4. e''8 d''4 f''8 a''8 | c'''2 b''2, with mvtOneWithheldCounter and mvtOneWithheldBass under it
mvtOneWithheldSHead = { \time 4/4 r2. g'4 | e''2.~ e''8 d''8 | c''4 a''2 g''4 | f''4. e''8 d''4 f''8 a''8 | c'''2 b''2 }

% mvtOneWithheldCounter: v99 ClOne bars 156-159 (reserved for finale, not in v221)
% id: withheld-s-counter
% source: mvt1 v99 bars 156–159, Clarinet 1 and Horn 2 in unison, mp, from mvt1/v99/sections/recTwo.ily (recTwoCounter, first four bars). Reserved for finale, not in v221
% key/mode: C major
% use: finale, under mvtOneWithheldSHead
% invariant: the chromatic descent C–B–Bb–A | (A) C | C–Bb–A | G–F, rhythm as written, a third to a sixth below the melody
mvtOneWithheldCounter = { \time 4/4 r4 c''4 b'4 bes'4 | a'2 c''2~ | c''4 bes'4 a'2 | g'2 f'2 }

% mvtOneWithheldBass: v99 Cb bars 156-159 (reserved for finale, not in v221)
% id: withheld-s-bass
% source: mvt1 v99 bars 156–159, double basses (sounding pitch; arco, mp), Bsn 1 an octave higher (c1 | c1 | d2 f,2 | g,2. r4), harp octaves. Reserved for finale, not in v221
% key/mode: C major: I (tonic pedal) – ii – V
% use: finale, under mvtOneWithheldSHead
% invariant: bass C C | D F | G (tonic pedal two bars, then ii – V)
mvtOneWithheldBass = { \time 4/4 c,1 | c,1 | d,2 f,,2 | g,,1 }

% ---- where each idea appears in mvt1 v221 (themecheck.py %@ syntax; suffixes as in the section files) ----
%@ mvtOneMotto BassCl 1
%@ mvtOneMotto Vc 1
%@ mvtOneMotto Cb 1
%@ mvtOneMottoAnswer CorAnglais 5
%@ mvtOneRisingSixthChain VlnOne 9
%@ mvtOneHornCall HnOne 13
%@ mvtOneHornCallCoda ClOne 175
%@ mvtOneThemeP VlnOne 15
%@ mvtOneThemePHead VlnOne 15
%@ mvtOneThemePHead VlnOne 27
%@ mvtOneThemePHead Vc 131
%@ mvtOneThemePHead HnOne 167
%@ mvtOneThemePHead TptOne 167
%@ mvtOneThemePHead Vla 167
%@ mvtOneThemeSAflat HnOne 46
%@ mvtOneThemeSAflat Vc 47 12 2
%@ mvtOneFluteMotto FluteOne 73
%@ mvtOneThemeSBminor VlnOne 97
%@ mvtOneThemeSBminor OboeOne 97
%@ mvtOneThemeSBminor FluteOne 97
%@ mvtOneMottoSecondForm TbnOne 117
%@ mvtOneMottoSecondForm BassTbn 117
%@ mvtOneMottoHalfAug ClOne 129
%@ mvtOneMottoTail BassCl 2
%@ mvtOneThemeSCmajor HnOne 146
%@ mvtOneThemeSCmajor Vla 147 12 2
%@ mvtOneThemeSCmajor Vc 147 12 2
%@ mvtOneViolinsFlatSeven VlnTwo 156 6 2
%@ mvtOneClimaxLine VlnTwo 158
%@ mvtOneClimaxLine FluteOne 158
%@ mvtOneMottoCodaCA CorAnglais 171
%@ mvtOneThemeSCodaMinor Vc 171
%@ mvtOneMottoChorale TbnOne 175
%@ mvtOneMottoViolins VlnOne 177
%@ mvtOneTimpaniPulse Timp 179
% ("47 12 2" = 12 notes from note 2: the cellos, violas and Vln II play other notes earlier in the pickup bar.)
% not listed: mvtOneStopChord (a chord; the checker compares single lines), the three mvtOneWithheld* variables (not in v221).
% Vln I at 155-161 is stored in the source as \recTwoMelody (a variable reference lyparse does not expand), so 155-161 are listed
% for Vln II and Flute 1, which play the same notes.

% ---- printed record: every variable, labelled ----
lbl = #(define-music-function (txt) (markup?)
  #{ \mark \markup \override #'(box-padding . 0.4) \box \small #txt #})

\paper { #(set-paper-size "a4") indent = 0 ragged-last = ##t max-systems-per-page = 7 }
\header { title = "Movement I — theme record (v221)" subtitle = "Concert pitch, no key signatures (accidentals as written). Each excerpt starts on its own line." tagline = ##f }

\score {
  \new PianoStaff \with { \override StaffGrouper.staff-staff-spacing.basic-distance = #9 }
  \autoChange {
    \lbl "mvtOneMotto · 1–4 · B.cl., Vc." \mvtOneMotto \bar "||" \break
    \lbl "mvtOneMottoAnswer · 5–9 · C.a." \mvtOneMottoAnswer \bar "||" \break
    \lbl "mvtOneRisingSixthChain · 9–13 · Vln I" \mvtOneRisingSixthChain \bar "||" \break
    \lbl "mvtOneHornCall · 13–14 · Hn 1" \mvtOneHornCall \bar "||" \break
    \lbl "mvtOneHornCallCoda · 175–177 · Cl 1" \mvtOneHornCallCoda \bar "||" \break
    \lbl "mvtOneThemeP · 15–22 · Vln I" \mvtOneThemeP \bar "||" \break
    \lbl "mvtOneThemePHead · 15–16 · Vln I" \mvtOneThemePHead \bar "||" \break
    \lbl "mvtOneThemeSAflat · 46–50 · Hn 1, Vc" \mvtOneThemeSAflat \bar "||" \break
    \lbl "mvtOneFluteMotto · 73–75 · Fl 1" \mvtOneFluteMotto \bar "||" \break
    \lbl "mvtOneThemeSBminor · 97–102 · Vln I, Ob 1" \mvtOneThemeSBminor \bar "||" \break
    \lbl "mvtOneMottoSecondForm · 117–121 · Tbn 1·2, Hn 1·2" \mvtOneMottoSecondForm \bar "||" \break
    \lbl "mvtOneMottoHalfAug · 129–130 · Cl 1" \mvtOneMottoHalfAug \bar "||" \break
    \lbl "mvtOneMottoTail · 2–3 · B.cl." \mvtOneMottoTail \bar "||" \break
    \lbl "mvtOneThemeSCmajor · 146–150 · Hn 1, Vla" \mvtOneThemeSCmajor \bar "||" \break
    \lbl "mvtOneViolinsFlatSeven · 155–157 · Vln I·II" \mvtOneViolinsFlatSeven \bar "||" \break
    \lbl "mvtOneClimaxLine · 158–161 · Vln I·II, Fl" \mvtOneClimaxLine \bar "||" \break
    \lbl "mvtOneMottoCodaCA · 171–174 · C.a." \mvtOneMottoCodaCA \bar "||" \break
    \lbl "mvtOneThemeSCodaMinor · 171–174 · Vc" \mvtOneThemeSCodaMinor \bar "||" \break
    \lbl "mvtOneMottoChorale · 175–179 · B.tbn, Tbn 2, Tbn 1" \mvtOneMottoChorale \bar "||" \break
    \lbl "mvtOneMottoViolins · 177–182 · Vln I" \mvtOneMottoViolins \bar "||" \break
    \lbl "mvtOneTimpaniPulse · 179–180 · Timp." \mvtOneTimpaniPulse \bar "||" \break
    \lbl "mvtOneStopChord · 26, 138, 170 · tutti (reduced)" \mvtOneStopChord \bar "||" \break
    \lbl "mvtOneWithheldSHead · v99 155–159 · Vln I·II — reserved for finale, not in v221" \mvtOneWithheldSHead \bar "||" \break
    \lbl "mvtOneWithheldCounter · v99 156–159 · Cl 1, Hn 2 — reserved for finale, not in v221" \mvtOneWithheldCounter \bar "||" \break
    \lbl "mvtOneWithheldBass · v99 156–159 · Cb (sounding) — reserved for finale, not in v221" \mvtOneWithheldBass \bar "|."
  }
  \layout { \context { \Score \override RehearsalMark.self-alignment-X = #LEFT \override RehearsalMark.break-align-symbols = #'(left-edge) } }
}
