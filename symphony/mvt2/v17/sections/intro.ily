% INTRODUCTION, bars 1-6 (Adagio, 3/4). Concert pitch; Cb and Cbsn at sounding pitch.
% Common-tone link from movement I: its last chord (C major, C5 on top in Vln I, E natural only in the violas)
% turns to A flat major. The C stays on top; the violas' E falls to E flat; the cellos fall C to A flat.
% c010: bar 1 at ppp (movement I ends ppp); the moving voices reach pp at 2 while the common tone C stays (A&S PDF 585-587).
% c010: clarinets an octave lower at 3-6, so horn 3's C4-D flat4-C4 is the top voice: the common tone and its plagal neighbour stay exposed (A&S PDF 587).
% Bars 3-6: the winds take the chord over (strings out), with the plagal neighbour C-D flat-C in horn 3.

introVlnOne = { c''2.~\ppp | c''2.~ | c''2.\> | R2.\! | R2.*2 | }
introVlnTwo = { g'2.\ppp | aes'2.~\pp | aes'2.\> | R2.\! | R2.*2 | }
introVla = { e'2.\ppp | es'2.~\pp | es'2.\> | R2.\! | R2.*2 | }
introVc = { c2.\ppp | aes,2.~\pp | aes,2.\> | R2.\! | R2.*2 | }
introCb = { R2. | aes,,2.\pp~ | aes,,2.\> | R2.\! | R2.*2 | }

introHnThree = { c'2.~\ppp | c'2.~\< | c'2.~\pp | c'2. | des'2. | c'2 r4 | }
introHnFour = { R2.*2 | aes2.\pp | aes2. | aes2. | aes2 r4 | }
introClOne = { R2.*2 | aes2.\pp | aes2. | aes2. | aes2 r4 | }
introClTwo = { R2.*2 | es2.\pp | es2. | fes2. | es2 r4 | }
introBassCl = { R2.*2 | aes,2.\pp | aes,2. | aes,2. | aes,2 r4 | }
introTimp = {
  R2. | aes,2.:32\ppp~^\markup \small "Timp. in A♭, C, D♭, E♭" | aes,2.:32\> | R2.\! | R2.*2 |
}
% The horn's pickup into the theme (bar 7).
introHnOne = { R2.*5 | r2 es8(\p^\markup \italic "solo, dolce espr." f8 | }
