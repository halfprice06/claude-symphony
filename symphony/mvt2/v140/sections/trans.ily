% TRANSITION, bars 31-36 (3/4). Bass clarinet solo over an A flat pedal (bassoon 2, contrabassoon),
% the theme's arpeggio and chromatic tail re-heard over the tonic. Woodwinds alone (no strings, no timpani).

% c020: 31-36 are a woodwind choir alone on the tonic (critic 119's woodwind-choir note; Rimsky-Korsakov PDF 89-90):
% the A section closes on A flat and D flat enters at 37 by phrase modulation, with no V7 of D flat before it
% (A&S PDF 452, Ex. 26-11; cyclic-notes, changes 111-120). The common-tone diminished seventh at 33 is kept.
transBassCl = {
  r4 es8(\mp^\markup \italic "solo, espr." f8 aes8 c'8 | es'2.~\< | es'4\mf\> d'4 des'4 | c'2\p bes4) \breathe |
  aes2.~(\> | aes4\pp\< bes4 c'4 |
}
% c027: the clarinets leave 32-36. They lay a third below the bass clarinet in its own register and family, moved in its
% rhythm at 33, doubled its C4 at 34 and sat above its A flat3 at 35-36 (Adler part 2 PDF 264 and 267: Mozart keeps the
% solo's own family out of the accompaniment; PDF 259-260: the accompaniment neither duplicates nor imitates the solo's
% rhythm; PDF 274: keep the accompanying forces registrally distant, especially under a woodwind solo).
% The same harmony (common-tone diminished seventh at 33 b2 kept) goes to cor anglais and bassoon 1, a double-reed colour;
% the lower voice holds F from 33 b2 into 34 and falls to E flat3 on 34 b2; the cor anglais steps to A flat3 at 34, so nothing doubles the solo's C4.
% At 35-36 the solo's A flat3 is the top voice over bassoon 1's E flat3 and bassoon 2's A flat2 pedal.
transCorAnglais = { R2. | c''2.(\pp^\markup \italic "dolce" | c''4 b'4 bes'4 | aes'2.) | R2. | r2 c''4(\p | }  % c111: an octave higher, a sixth above the bass clarinet (normal order Ob over Cl; sixths in different colours), pp under the solo (Rimsky-Korsakov PDF 67, 70). 36 b3: C5 pickup into flute 1 F5 at 37, theme B's rising fourth at its first statement as at 44 and 52 (c071; flute pickup dropped at c072 for the 8-page layout)
transBsnOne = { R2. | aes2.(\pp | aes4 f2~ | f4 es2) \breathe | es2.~ | es2 r4 | }  % c066: breath at 34/35 (about 17 s held at pp from 32 to 36), staggered from bassoon 2's at 33 (Adler part 1 PDF 175, 188)  % F tied over the bar (6-5 over the pedal): the two accompanying voices do not move together into 34, and no parallel fourths with the cor anglais
transBsnTwo = { aes,2.~\pp | aes,2.~ | aes,2 \once \override BreathingSign.direction = #DOWN \breathe aes,4~ | aes,2.~ | aes,2.~ | aes,2 r4 | }
transCbsn = { aes,,2.~ |  % c063: tied from 30
  aes,,2.~ | aes,,2 r4 | R2.*3 | }

% c071: flute 1's pickup C5 into theme B (rising fourth C-F, the plan's "opens with a rising fourth"; phrase 2 at 41 opens A flat-D flat, the same interval a third lower).
% It takes over the bass clarinet's C4 an octave higher, so the solo hands its anacrusis to the next colour (Adler part 2 PDF 30, Ex. XI-14).
transFluteOneX = { R2.*5 | r2 c''4(\p^\markup \italic "dolce cantabile" | }

% c075: a cue for the flute part before its solo at 37, after 36 bars' rest (MOLA PDF 5 and Ex. 4, PDF 10: logical, audible cues in long rests). Rests in the score.
transFluteOne = { R2.*3 | \tag #'score { R2.*3 } \tag #'part { \cueDuring #"bassClQ" #DOWN { <>^\markup \tiny "B.cl." R2.*3 } } | }
% c075: advance mute warning in the string parts where the players stop (MOLA PDF 5 and Ex. 5, PDF 10: a change is marked at the end of
% the previous passage, not only at the next entry). The string staves are hidden in the score at 31-36.
transVlnOne = { R2.^\markup \italic "(tutti) via sord." | R2.*5 | }
transVlnTwo = { R2.^\markup \italic "via sord." | R2.*5 | }
transVla = { R2.^\markup \italic "via sord." | R2.*5 | }
transVc = { R2.^\markup \italic "via sord." | R2.*5 | }
transCb = { R2.*6 | }  % c119: basses played 21-30 senza sord., so no mute to remove
