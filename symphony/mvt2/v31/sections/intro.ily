% INTRODUCTION, bars 1-6 (Adagio, 3/4). Concert pitch; Cb and Cbsn at sounding pitch.
% Common-tone link from movement I: its last chord (C major, C5 on top in Vln I, E natural only in the violas)
% turns to A flat major. The C stays on top; the violas' E falls to E flat; the cellos fall C to A flat.
% c010: bar 1 at ppp (movement I ends ppp); the moving voices reach pp at 2 while the common tone C stays (A&S PDF 585-587).
% c010: clarinets an octave lower at 3-6, so horn 3's C4-D flat4-C4 is the top voice: the common tone and its plagal neighbour stay exposed (A&S PDF 587).
% Bars 3-6: the winds take the chord over (strings out), with the plagal neighbour C-D flat-C in horn 3.

introVlnOne = { c''2.\repeatTie~\ppp^\markup \italic "change bow at will" | c''2.~ | c''2.\> | R2.\! | R2.*2 | }
introVlnTwo = { g'2.\repeatTie\ppp | aes'2.~\pp | aes'2.\> | R2.\! | R2.*2 | }
introVla = { e'2.\repeatTie\ppp | es'2.~\pp | es'2.\> | R2.\! | R2.*2 | }
introVc = { c2.\repeatTie\ppp | aes,2.~\pp | aes,2.\> | R2.\! | R2.*2 | }
introCb = { R2. | aes,,2.\pp~ | aes,,2.\> | R2.\! | R2.*2 | }

% c030: horn 3 has held C4 since movement I bar 180 (three bars of Lento and a fermata, about 18 s at ppp); tied on to bar 4 it
% would be over 30 s in one breath. Horn 4 enters under the tie on bar 1 beat 2 and carries the C4 through bar 2, horn 3 breathes
% in bar 2 and takes the C again at 3, so horn 3 stays on top at 3-6 (c010) and the sounding pitches are unchanged.
introHnThree = { c'2.\repeatTie\ppp | R2. | c'2.~\pp | c'2. | des'2. | c'2 r4 | }
introHnFour = { r4 c'2~\ppp | c'2.\< | aes2.\pp | aes2. | aes2. | aes2 r4 | }
introClOne = { R2.*2 | aes2.\pp | aes2. | aes2. | aes2 r4 | }
introClTwo = { R2.*2 | es2.\pp | es2. | fes2. | es2 r4 | }
introBassCl = { R2.*2 | aes,2.\pp | aes,2. | aes,2. | aes,2 r4 | }
introTimp = {
  R2. | aes,2.:32\ppp~^\markup \small "Timp. in G, A♭, C, E♭ (as in movement I)" | aes,2.:32\> | R2.\! | R2.^\markup \small "muta G in D♭: A♭, C, D♭, E♭" | R2. |
}
% The horn's pickup into the theme (bar 7).
introHnOne = { R2.*5 | r2 es8(\p^\markup \italic "solo, dolce espr." f8 | }
