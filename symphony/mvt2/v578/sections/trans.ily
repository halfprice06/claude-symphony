% TRANSITION, bars 31-36 (3/4). Bass clarinet solo over an A flat pedal (bassoon 2, contrabassoon),
% the theme's arpeggio and chromatic tail re-heard over the tonic. Woodwinds alone (no strings, no timpani).

% c020: 31-36 are a woodwind choir alone on the tonic (critic 119's woodwind-choir note; Rimsky-Korsakov PDF 89-90):
% the A section closes on A flat and D flat enters at 37 by phrase modulation, with no V7 of D flat before it
% (A&S PDF 452, Ex. 26-11; cyclic-notes, changes 111-120). The common-tone diminished seventh at 33 is kept.
% c140: the solo an octave lower (sounding E flat3-D3-D flat3-C3, written F4-E4-E flat4-D4): the bass clarinet's chalumeau, its most distinctive
% register (Adler part 1 PDF 217), and the pitch and instrument of movement I's first motto statement (mvt I bars 2-3, B.cl. + Vc: es2.~ es8 d8 | c2 des4 c4)
% and of its coda bass (175-179). Was es8 f8 aes8 c'8 | es'2.~ | es'4 d'4 des'4 | c'2 bes4 | aes2.~ | aes4 bes4 c'4 (clarino; Adler part 2 PDF 188:
% the tune's register decides the instrument). The cor anglais follows it down, so the two stay a sixth apart in the same order (c111).
transBassCl = {
  r4 es,8(\p^\markup \italic "solo, espr." f,8 aes,8 c8 | << es2.~-\tweak stencil ##f \mf \< \tag #'score { \set Staff.midiExpression = #0.7 s4 \set Staff.midiExpression = #0.85 s2 } >> | \set Staff.midiExpression = #1.0 es4\mf\> d4 des4 | c2\mp bes,4) \breathe |
  aes,2.~(\> | aes,4\pp\< bes,4 c4 |
}  % c368: MIDI only: the printed crescendo p < mf peaks on the tied E flat3 (33 b1), but a held note has one velocity, so score.midi played the E flat at p (37) and the D at mf (49), the reverse of the print; hidden mf on the attack with CC11 0.7-0.85-1.0 across 32 renders the swell inside the note (Casanelles PDF 124, 142, Fig. 4.5; PDF 130, Fig. 4.4). Clarinets 1-2 (same channel) rest 31-36  % c218: p < mp > p (was mp < mf > p): the solo re-enters after 16 bars' rest; mp/mf re-entries are 'colourless' (Rimsky-Korsakov PDF 136), and one degree over the pp cor anglais and bassoon is enough (PDF 133)
% c027: the clarinets leave 32-36. They lay a third below the bass clarinet in its own register and family, moved in its
% rhythm at 33, doubled its C4 at 34 and sat above its A flat3 at 35-36 (Adler part 2 PDF 264 and 267: Mozart keeps the
% solo's own family out of the accompaniment; PDF 259-260: the accompaniment neither duplicates nor imitates the solo's
% rhythm; PDF 274: keep the accompanying forces registrally distant, especially under a woodwind solo).
% The same harmony (common-tone diminished seventh at 33 b2 kept) goes to cor anglais and bassoon 1, a double-reed colour;
% the lower voice holds F from 33 b2 into 34 and falls to E flat3 on 34 b2; the cor anglais steps to A flat3 at 34, so nothing doubles the solo's C4.
% At 35-36 the solo's A flat3 is the top voice over bassoon 1's E flat3 and bassoon 2's A flat2 pedal.
% c140: since the solo moved down an octave, 35-36 have the solo on A flat2 with bassoon 2's pedal, under bassoon 1's E flat3, rising to D flat3 at 37.
transCorAnglais = { \tag #'score R2. \tag #'part { \transposedCueDuring #"bassClQ" #UP c''' { <>^\markup \tiny "B.cl." R2. } } | c'2.~(\p^\markup \italic "dolce" | c'4 ces'4 bes4 | aes2.) | R2. | r2 c''4-\shape #'(((0 . 0) (0 . 0) (-1.5 . 0) (-2.6 . -0.6)) ()) (\p | }  % c435: the broken slur's first half ends at the double bar, clear of the warning key signature (Gould PDF 44, 55)  % c365: cue stems up so the player's whole-bar rest sits below the stave centre, clear of the cue notes (Gould PDF 50-51)  % c276: p at 32 (was pp): c111's pp was written for C5-A flat4; since c140 lowered the line an octave, 33 b3-34 (B flat3, A flat3 = written F4, E flat4) lie in the cor anglais's lowest fifth, where the oboe family cannot be asked for pp (Adler part 1 PDF 174-175, 198, 205); c036's p restored  % c140: 32-34 an octave lower again (sounding C4-A flat3, written G4-E flat4), a sixth above the bass clarinet's lowered line  % c111: an octave higher, a sixth above the bass clarinet (normal order Ob over Cl; sixths in different colours), pp under the solo (Rimsky-Korsakov PDF 67, 70). 36 b3: C5 pickup into flute 1 F5 at 37, theme B's rising fourth at its first statement as at 44 and 52 (c071; flute pickup dropped at c072 for the 8-page layout)
transBsnOne = { R2.*2 | r4 f2~(\pp | f4 es2) \breathe | es2.~-\tweak stencil ##f \pp | es2 r4 | }  % c338: hidden pp (MIDI only): after the breath the part-combiner moves the E flat3 to a solo voice without a dynamic, so it played at velocity 53 over the bass clarinet's 44-32  % c140: enters with the F of the common-tone diminished seventh at 33 b2 (was A flat3 from 32): with the solo in the tenor, A flat3 lay between the cor anglais and the solo; C4/E flat3/A flat2 completes the chord at 32  % c066: breath at 34/35 (about 17 s held at pp from 32 to 36), staggered from bassoon 2's at 33 (Adler part 1 PDF 175, 188)  % F tied over the bar (6-5 over the pedal): the two accompanying voices do not move together into 34, and no parallel fourths with the cor anglais
transBsnTwo = { aes,2.~\pp | aes,2.~ | aes,2.~ | aes,4 r2 | R2.*2 | }  % c220: holds the A flat2 through 33 into 34 b1, over the contrabassoon's breath at 33 b3, so the common tone sounds unbroken under the common-tone diminished seventh and its resolution (A&S printed pp. 553-554 = PDF 543-544, corrected c400: the bass is the stable, sustained tone of the embellishing chord; PDF 544-545, Ex. 30-21: the minor-3rd spelling, here C flat, carries the minor of the preceding C-minor movement into this one, as Brahms Op. 87 after its C-minor Scherzo)  % c149: off at 33 b3; the contrabassoon keeps the A flat pedal, so the solo's A flat2 at 35-36 is not a unison with the pedal (Rimsky-Korsakov PDF 139-141)
transCbsn = { aes,,2.~ |  % c063: tied from 30
  aes,,2.~ | aes,,2 \breathe aes,,4~ | aes,,2.~ | aes,,2.~ | aes,,2 r4 | }  % c149: holds the pedal to 36 (bassoon 2 leaves at 33 b3)

% c071: flute 1's pickup C5 into theme B (rising fourth C-F, the plan's "opens with a rising fourth"; phrase 2 at 41 opens A flat-D flat, the same interval a third lower).
% It takes over the bass clarinet's C4 an octave higher, so the solo hands its anacrusis to the next colour (Adler part 2 PDF 30, Ex. XI-14).
transFluteOneX = { R2.*5 | r2 c''4(\p^\markup \italic "dolce cantabile" | }

% c075: a cue for the flute part before its solo at 37, after 36 bars' rest (MOLA PDF 5 and Ex. 4, PDF 10: logical, audible cues in long rests). Rests in the score.
transFluteOne = { R2.*3 | \tag #'score { R2.*3 } \tag #'part { \transposedCueDuring #"bassClQ" #DOWN c'' { <>^\markup \tiny "B.cl." R2. \noBreak R2. \noBreak R2. } } | }  % c575: \noBreak keeps the three-bar cue on one system once the 1-6 rest is widened for letter A (c455 finding 4)  % c165: cue an octave up (transposedCueDuring ... c''): the bass clarinet sounds at A flat3-D flat4, three to five ledger lines under the flute staff; MOLA PDF 5: cues must be obvious to the reader
% c075: advance mute warning in the string parts where the players stop (MOLA PDF 5 and Ex. 5, PDF 10: a change is marked at the end of
% the previous passage, not only at the next entry). The string staves are hidden in the score at 31-36.
% c315: part-only cue for the harp before its entry with the poco rit. and the change to 4/4, Poco più mosso at 37, after 22 bars' rest (MOLA PDF 5, Ex. 4); an octave up, as Fl 1 (c165). Score: rests.
transHarpR = { R2.*3 | \tag #'score { R2.*3 } \tag #'part { \transposedCueDuring #"bassClQ" #DOWN c'' { <>^\markup \tiny "B.cl." R2.*3 } } | }
transVlnOne = { R2.^\markup \italic "(tutti) via sord." | R2.*5 | }
transVlnTwo = { R2.^\markup \italic "via sord." | R2.*5 | }
transVla = { R2.^\markup \italic "via sord." | R2.*5 | }
transVc = { R2.^\markup \italic "via sord." | R2.*5 | }
transCb = { R2.*6 | }  % c119: basses played 21-30 senza sord., so no mute to remove
