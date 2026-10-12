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
introHnThree = { c'2\repeatTie\ppp r4 | R2. | c'2.~\pp | c'2. | des'2. | c'2 r4 | }
introHnFour = { r4 c'2~\ppp-\tag #'score _\markup \bold "4." |  % c045: label the second player's entry on the shared staff, as "3." labels the first (MOLA Ex. 6, PDF 11: players named on paired staves)
  c'2.\< | aes2.\pp | aes2. | aes2. | aes2 r4 | }
% c060: clarinet 1 rests at 3-6: its A flat3 was a unison with horn 4 (c030 relief) for four bars (Sebesky PDF 12-13, Ex. 1: economy;
% the lower-middle register lightened so horn 3's C-D flat-C, the preview of the plagal close, stays the focus, PDF 13-14). Was aes2.\pp | aes2. | aes2. | aes2 r4
introClOne = { R2.*6 | }
introClTwo = { R2.*2 | es2.\pp | es2. | fes2. | es2 r4 | }
introBassCl = { R2.*2 | aes,2.\pp | aes,2. | aes,2. | aes,2 r4 | }
introTimp = {
  << R2. { s2.^\markup \small \column { "Timp. in G, A♭, C, E♭ (as in movement I)" "soft sticks" } } >> | aes,2.:32\ppp~ | aes,2:32\>~ aes,8\! r8 | R2. | R2.^\markup \small "muta in A♭, C, D♭, E♭" | R2. |  % c056: tuning and sticks before the first note; roll ends on a tied stroke (Adler part 2 PDF 80-81, Ex. XII-47, XII-51; PDF 88 beaters)
}
% The horn's pickup into the theme (bar 7).
introHnOne = { R2.*5 | r2 \set Staff.soloText = "1. solo" es8(\p-\tag #'score ^\markup \italic "dolce espr." -\tag #'part ^\markup \italic "solo, dolce espr." f8 | }  % c035: one label, "1. solo", instead of "1." plus "solo"

% c040/c045: movement I's last harp chord (C2-G2-C3) is now damped in movement I at its bar 182 ("étouffez with Cb."), so movement II has no étouffez.
introHarpL = { R2.*6 | }  % c076: no scordatura: bar 9 D flat is D flat2 (Rimsky-Korsakov PDF 46: extreme notes only in special circumstances and for octave doubling)  % c050: retune during 1-6; movement I runs attacca into bar 1, so there is no pause between movements (Rimsky-Korsakov PDF 21, axiom II)
